import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const src = path.join(root, "index.html");
const outDir = path.join(root, "dist");
const out = path.join(outDir, "index.html");

if (!fs.existsSync(src)) throw new Error("E_NO_INDEX_HTML");
fs.mkdirSync(outDir, { recursive: true });

const html = fs.readFileSync(src, "utf8");
fs.writeFileSync(out, html, "utf8");
console.log("OK: built", out);
