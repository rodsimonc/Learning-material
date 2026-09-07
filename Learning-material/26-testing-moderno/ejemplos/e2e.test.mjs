import { chromium } from '/home/claude/widdemo/node_modules/playwright/index.mjs';
import { createServer } from 'node:http';
import { readFileSync, existsSync } from 'node:fs';
import { extname, join } from 'node:path';
const types={'.html':'text/html','.js':'text/javascript','.css':'text/css'};
const srv=createServer((req,res)=>{let f=join('dist',req.url==='/'?'index.html':req.url);if(!existsSync(f))f='dist/index.html';res.setHeader('Content-Type',types[extname(f)]||'text/plain');res.end(readFileSync(f));});
await new Promise(r=>srv.listen(4188,r));
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await b.newPage();
let pasados=0, fallidos=0;
function check(nombre, cond){ if(cond){pasados++;console.log("  PASS:",nombre);} else {fallidos++;console.log("  FAIL:",nombre);} }
await p.goto('http://localhost:4188/');
await p.waitForSelector('.tarjeta');
console.log("== E2E: flujo de compra en la tienda ==");
check("se muestran 6 productos", await p.locator('.tarjeta').count()===6);
check("el carrito arranca vacío", (await p.locator('.carrito p').first().textContent()).includes('Vacío'));
// agregar milanesa (index 3) x2 y napolitana (index 2)
const btns=p.locator('.tarjeta button');
await btns.nth(3).click(); await btns.nth(3).click(); await btns.nth(2).click();
await p.waitForTimeout(150);
check("el carrito tiene 2 líneas", await p.locator('.carrito li').count()===2);
check("el total es $28.800", (await p.getByTestId('total').textContent()).includes('28.800'));
await p.locator('.carrito .x').first().click(); await p.waitForTimeout(150);
check("tras quitar, total $9.800", (await p.getByTestId('total').textContent()).includes('9.800'));
console.log(`\nResultado E2E: ${pasados} pasados, ${fallidos} fallidos`);
await b.close(); srv.close();
