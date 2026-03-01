import fs from "node:fs";
import assert from "node:assert";

const html = fs.readFileSync("index.html", "utf8");
assert(html.includes("verifrax.proof.v1"), "E_VERIFY_UI_MISSING_SCHEMA_GATE");
assert(html.includes("Verify"), "E_VERIFY_UI_MISSING_BUTTON");
console.log("OK: ui sanity");
