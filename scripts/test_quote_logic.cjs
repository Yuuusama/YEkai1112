// Offline VM test: no browser, no network, no WhatsApp messages are sent.
// Usage: node scripts/test_quote_logic.cjs /path/to/extracted-cases.json
const fs=require('fs'),vm=require('vm'),assert=require('assert'),path=require('path');
const root=path.resolve(__dirname,'..');
const cases=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const source=fs.readFileSync(path.join(root,'quote.js'),'utf8');
let tested=0;
class Element {
 constructor(){this.events={};this.children=[];this.value='';this.href='';}
 addEventListener(n,fn){this.events[n]=fn}
 replaceChildren(){this.children=[]}
 append(...nodes){this.children.push(...nodes)}
}
for(const c of cases){
 const form=new Element();form.dataset={product:c.product};form.elements={};
 for(const [k,v] of Object.entries(c.fields))form.elements[k]={value:v};
 const sticky=new Element(),quick=new Element(),config=new Element(),custom=new Element(),box=new Element(),radio=new Element();
 config.querySelector=s=>s==='.selected-specifications'?box:radio;
 config.querySelectorAll=()=>[radio];
 const elements={'product-inquiry':form,'sticky-quote':sticky,'product-configurator':config,'custom-configuration':custom,'configuration-data':{textContent:JSON.stringify(c.choices)}};
 const document={documentElement:{lang:c.lang},getElementById:id=>elements[id],querySelector:s=>quick,createElement:()=>new Element()};
 const opened=[];
 class FormData {constructor(form){this.form=form}get(k){return this.form.elements[k]?.value||''}}
 vm.runInNewContext(source,{document,FormData,window:{open:(...a)=>opened.push(a)},encodeURIComponent,JSON});
 function message(){const u=new URL(sticky.href);assert.equal(u.host,'wa.me');assert.equal(u.pathname,'/8619883954016');assert.equal(quick.href,sticky.href);const t=u.searchParams.get('text');assert(t.includes(c.product));assert(!t.includes('undefined'));return t}
 message();tested++;
 const lang=c.lang.startsWith('es')?'es':'en';
 for(let i=0;i<c.choices.length;i++){
  config.events.change({target:{name:'configuration',value:String(i)}});
  assert.equal(form.elements.size.value,c.choices[i][lang],c.path);assert(message().includes(c.choices[i][lang]));tested++;
 }
 custom.value='125 mm / M14 — confirmar con Frank';custom.events.input();
 assert(message().includes(custom.value));assert.equal(radio.checked,true);tested++;
 form.elements.destination.value='México & envío';form.elements.quantity.value='5,000';form.events.input({target:{name:'quantity'}});
 assert(message().includes('México & envío'));assert(message().includes('5,000'));
 let prevented=false;form.events.submit({preventDefault(){prevented=true}});assert(prevented);assert.equal(opened.length,1);assert.equal(opened[0][0],sticky.href);assert.deepEqual(opened[0].slice(1),['_blank','noopener']);tested++;
}
console.log(JSON.stringify({environment:'Node VM with simulated DOM; no browser/no network',pages:cases.length,configurations:cases.reduce((n,c)=>n+c.choices.length,0),cases:tested,failures:0}));
