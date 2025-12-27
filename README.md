<!--
VERIFRAX-verify — Public Verifier
Repo: https://github.com/Verifrax/VERIFRAX-verify
Pages: https://verifrax.github.io/VERIFRAX-verify/
-->

<div align="center">

<!-- Minimal vector mark (inline SVG). Replace with your actual logo if desired. -->
<svg width="92" height="92" viewBox="0 0 92 92" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="VERIFRAX mark">
  <rect x="6" y="6" width="80" height="80" rx="18" stroke="#111" stroke-width="4"/>
  <path d="M24 30L46 68L68 30" stroke="#111" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M33 30H59" stroke="#111" stroke-width="6" stroke-linecap="round"/>
</svg>

<h1>VERIFRAX — Public Verifier</h1>

<p>
  A static, public verification surface for <code>verifrax.proof.v1</code> artifacts.<br/>
  Proofs are generated privately (engine stays private). Verification is public and portable.
</p>

<p>
  <a href="https://verifrax.github.io/VERIFRAX-verify/"><strong>Open Verifier UI</strong></a>
  &nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="https://github.com/Verifrax/VERIFRAX-verify"><strong>Repository</strong></a>
</p>

<!-- Badges (no emoji). -->
<p>
  <a href="https://github.com/Verifrax/VERIFRAX-verify/actions">
    <img alt="Build" src="https://img.shields.io/badge/build-static-111?style=flat&labelColor=111&color=333">
  </a>
  <a href="https://github.com/Verifrax/VERIFRAX-verify/deployments">
    <img alt="Deployment" src="https://img.shields.io/badge/deploy-github%20pages-111?style=flat&labelColor=111&color=333">
  </a>
  <a href="https://verifrax.github.io/VERIFRAX-verify/">
    <img alt="Verifier UI" src="https://img.shields.io/badge/verifier-live-111?style=flat&labelColor=111&color=333">
  </a>
  <a href="https://github.com/Verifrax/VERIFRAX-verify/blob/main/THREAT_MODEL.md">
    <img alt="Threat Model" src="https://img.shields.io/badge/security-threat%20model-111?style=flat&labelColor=111&color=333">
  </a>
</p>

<!-- Clean "capability strip" with icon-like inline SVG. -->
<table>
  <tr>
    <td align="center" width="220">
      <svg width="26" height="26" viewBox="0 0 24 24" fill="none" aria-label="portable icon" xmlns="http://www.w3.org/2000/svg">
        <path d="M8 7h12M8 12h12M8 17h12" stroke="#111" stroke-width="2" stroke-linecap="round"/>
        <path d="M4 7h.01M4 12h.01M4 17h.01" stroke="#111" stroke-width="3" stroke-linecap="round"/>
      </svg><br/>
      <strong>Portable Proofs</strong><br/>
      Copy/paste JSON anywhere.
    </td>
    <td align="center" width="220">
      <svg width="26" height="26" viewBox="0 0 24 24" fill="none" aria-label="lock icon" xmlns="http://www.w3.org/2000/svg">
        <path d="M7 11V8a5 5 0 0 1 10 0v3" stroke="#111" stroke-width="2" stroke-linecap="round"/>
        <path d="M6 11h12v10H6V11Z" stroke="#111" stroke-width="2" />
      </svg><br/>
      <strong>Engine Stays Private</strong><br/>
      UI contains no engine/IP.
    </td>
    <td align="center" width="220">
      <svg width="26" height="26" viewBox="0 0 24 24" fill="none" aria-label="audit icon" xmlns="http://www.w3.org/2000/svg">
        <path d="M7 3h10v18H7V3Z" stroke="#111" stroke-width="2"/>
        <path d="M9 7h6M9 11h6M9 15h4" stroke="#111" stroke-width="2" stroke-linecap="round"/>
      </svg><br/>
      <strong>Audit Surface</strong><br/>
      Parse + sanity-check schema.
    </td>
  </tr>
</table>

</div>

---

## What this repository is

**`VERIFRAX-verify` is the public verifier surface** for `verifrax.proof.v1` proofs.

- **Private:** The engine that generates proofs (IP, internals, implementation).
- **Public:** This repo, hosting a **static** verifier UI over GitHub Pages.
- **Portable:** Proofs are plain JSON. Anyone can validate without repo access.

This repo is intentionally minimal:
- no servers
- no secrets
- no dependencies required to verify structure

---

## Live Verifier

**URL:** https://verifrax.github.io/VERIFRAX-verify/

### Verification contract (current)
The UI validates:
- JSON parses correctly
- `schema === "verifrax.proof.v1"`
- presence + shape of required fields (including 64-hex `artifact.sha256`)
- displays parsed, canonical subset of proof fields

**Note:** Hash recomputation requires local file access. A future enhancement can add a file upload and recompute SHA-256 in-browser.

---

## Confirm the core property: "Proofs travel without you"

### 1) Generate proof locally (engine stays private)
From your private engine repo:

```bash
echo "verifrax" > /tmp/vx.txt
./scripts/console.sh prove /tmp/vx.txt
cat out/console/vx.txt.proof.v1.json
```

### 2) Verify anywhere (no repo access required)

1. Open: [https://verifrax.github.io/VERIFRAX-verify/](https://verifrax.github.io/VERIFRAX-verify/)
2. Paste the JSON
3. Click **Verify**

Expected outcome:

* Status shows **VERIFIED (STRUCTURE OK)**
* Parsed panel shows the canonical fields

---

## Proof format

A `verifrax.proof.v1` is a JSON document that includes:

* `schema` — fixed string
* `created_at` — ISO timestamp
* `repo` — issuing repo identifier
* `baseline_tag` — issuance baseline tag
* `core_dist_hash` — engine distribution hash (if frozen)
* `artifact` — `{ name, path, sha256 }`
* `certificate_v1` — embedded certificate object
* `verify_ref` — canonical public verifier URL (this site)

Example excerpt:

```json
{
  "schema": "verifrax.proof.v1",
  "artifact": { "name": "vx.txt", "sha256": "<64-hex>" },
  "verify_ref": "https://verifrax.github.io/VERIFRAX-verify/"
}
```

---

## Security and threat model

This repo is a **public presentation + validation surface**, not a signing authority.

* The verifier **must never** require secrets.
* The verifier **must never** embed private engine internals.
* The verifier provides **auditability**, not privileged trust.

Read:

* Threat model: `THREAT_MODEL.md`
* CLI spec: `CLI_SPEC.md`

---

## Repository structure

* `index.html` — Verifier UI (static)
* `THREAT_MODEL.md` — Security model and assumptions
* `CLI_SPEC.md` — CLI contract and proof expectations
* `MARKET_WEDGE.md` — Adoption wedge positioning (public-safe)
* `WHAT_VERIFRAX_SOLVES.md` — Problem framing
* `WHY_NOT_BLOCKCHAIN.md` — Framing against chain-only approaches
* `UI_WIREFRAME.md` — UI contract

---

## Deployment

### GitHub Pages configuration

This repository is deployed via **GitHub Pages**:

* Source: Deploy from a branch
* Branch: `main`
* Folder: `/ (root)`

### Release discipline (recommended)

Tag releases for verifier UI changes:

* `verify-v0.1.0` — initial public verifier UI
* `verify-v0.1.1` — schema display changes / hardening
* `verify-v0.2.0` — hash recomputation (file upload) support

---

## Roadmap (public verifier)

### Near-term hardening

* File upload support to recompute SHA-256 locally in-browser
* Strict field validation + deterministic rendering of canonical subset
* Optional: schema version banner + "known versions" table
* Optional: verify_ref sanity check (must match canonical URL)

### Anchors (when enabled by engine)

* Display anchor list
* Validate anchor object shapes
* Optional: provide "verify on explorer" links

---

## Contributing

This verifier should remain:

* minimal
* deterministic
* dependency-light
* security-first

If you propose changes:

* explain threat implications
* show failure modes
* keep UI and parsing logic explicit and auditable

---

## License

Add a license if you want downstream reuse. Otherwise leave unlicensed.

---

## Maintainer

**Owner:** `Verifrax`
**Public verifier:** [https://verifrax.github.io/VERIFRAX-verify/](https://verifrax.github.io/VERIFRAX-verify/)

