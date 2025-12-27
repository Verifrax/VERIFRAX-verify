
# **VERIFRAX** — Public Verifier

<!--
VERIFRAX-verify — Public Verifier
Repo: https://github.com/Verifrax/VERIFRAX-verify
Pages: https://verifrax.github.io/VERIFRAX-verify/
-->

<div align="center">

<svg width="92" height="92" viewBox="0 0 92 92" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="VERIFRAX mark">
  <rect x="6" y="6" width="80" height="80" rx="18" stroke="#111" stroke-width="4"/>
  <path d="M24 30L46 68L68 30" stroke="#111" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M33 30H59" stroke="#111" stroke-width="6" stroke-linecap="round"/>
</svg>

<h1><strong>VERIFRAX</strong> — Public Verifier</h1>

<p>
  A <strong>static, public verification surface</strong> for <code>verifrax.proof.v1</code> artifacts.<br/>
  Proofs are generated privately (<strong>engine stays private</strong>). Verification is <strong>public, portable, and offline-capable</strong>.
</p>

<p>
  <a href="https://verifrax.github.io/VERIFRAX-verify/"><strong>Open Verifier UI</strong></a>
  &nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="https://github.com/Verifrax/VERIFRAX-verify"><strong>Repository</strong></a>
</p>

<p>
  <img alt="build" src="https://img.shields.io/badge/build-static-111?style=flat&labelColor=111&color=333" />
  <img alt="deploy" src="https://img.shields.io/badge/deploy-github%20pages-111?style=flat&labelColor=111&color=333" />
  <img alt="verifier" src="https://img.shields.io/badge/verifier-live-111?style=flat&labelColor=111&color=333" />
  <img alt="security" src="https://img.shields.io/badge/security-threat%20model-111?style=flat&labelColor=111&color=333" />
</p>

<table>
  <tr>
    <td align="center" width="220"><strong>Portable Proofs</strong><br/>Copy/paste JSON anywhere</td>
    <td align="center" width="220"><strong>Engine Private</strong><br/>No engine code or IP here</td>
    <td align="center" width="220"><strong>Audit Surface</strong><br/>Deterministic schema validation</td>
  </tr>
</table>

</div>

---

## What this repository is

**<strong>VERIFRAX</strong>-verify** is the **public verifier surface** for <code>verifrax.proof.v1</code> proofs.

* **Private:** The <strong>VERIFRAX</strong> engine that generates proofs (IP, internals, implementation).
* **Public:** This repository, hosting a <strong>static verifier UI</strong> over GitHub Pages.
* **Portable:** Proofs are plain JSON. Anyone can validate without repo or engine access.

This repository is intentionally minimal:

* no servers
* no secrets
* no signing keys
* no privileged trust

---

## Live Verifier

**URL:** [https://verifrax.github.io/VERIFRAX-verify/](https://verifrax.github.io/VERIFRAX-verify/)

### Verification contract (current)

The verifier validates:

* JSON parses correctly
* <code>schema === "verifrax.proof.v1"</code>
* required fields are present and well-formed
* <code>artifact.sha256</code> is a valid 64-hex digest
* canonical fields are displayed deterministically

<strong>Note:</strong> Hash recomputation requires local file access. The verifier intentionally avoids fetching or executing anything remotely.

---

## Core invariant

> <strong>Proofs travel without you.</strong>

Once generated, a proof can be shared, archived, or audited without access to:

* the <strong>VERIFRAX</strong> engine
* the private repository
* any secrets or credentials

---

## Proof format

A <code>verifrax.proof.v1</code> document includes:

* <code>schema</code>
* <code>created_at</code>
* <code>repo</code>
* <code>baseline_tag</code>
* <code>core_dist_hash</code>
* <code>artifact</code> { name, path, sha256 }
* <code>certificate_v1</code>
* <code>verify_ref</code> (this verifier URL)

---

## Security and threat model

This repository is a <strong>verification surface</strong>, not a signing authority.

* No secrets
* No engine internals
* No remote execution

See:

* <code>THREAT_MODEL.md</code>
* <code>CLI_SPEC.md</code>

---

## Repository structure

* <code>index.html</code> — Verifier UI
* <code>THREAT_MODEL.md</code> — Threat model
* <code>CLI_SPEC.md</code> — CLI and proof contract
* <code>MARKET_WEDGE.md</code> — Adoption framing
* <code>WHAT_VERIFRAX_SOLVES.md</code>
* <code>WHY_NOT_BLOCKCHAIN.md</code>
* <code>UI_WIREFRAME.md</code>

---

## Deployment

Deployed via <strong>GitHub Pages</strong>:

* Branch: <code>main</code>
* Folder: <code>/</code>
* Build: none (static)

---

## Roadmap (public verifier)

* Local file upload for SHA-256 recomputation
* Strict canonical field rendering
* Schema version registry
* Anchor visualization (engine-gated)

---

## License

MIT License

Copyright (c) 2025 **VERIFRAX**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## Maintainer

<strong>VERIFRAX</strong><br/>
Public verifier: [https://verifrax.github.io/VERIFRAX-verify/](https://verifrax.github.io/VERIFRAX-verify/)

