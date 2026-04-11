# VERIFRAX-verify

Deterministic public verdict surface.

![License](https://img.shields.io/badge/license-Apache--2.0-blue)
![Surface](https://img.shields.io/badge/surface-public%20verifier-111111)
![Host](https://img.shields.io/badge/host-verify.verifrax.net-1f6feb)

Public verification repository for `https://verify.verifrax.net/`, serving a static verification surface for Verifrax proof material without becoming an authority issuer, proof publisher, execution runtime, archive surface, or evidence-root repository.


## Terminal planes

- **[ANAGNORIUM](https://github.com/Verifrax/ANAGNORIUM)** — terminal recognition
- **[REGRESSORIUM](https://github.com/Verifrax/REGRESSORIUM)** — terminal recourse

## Public verdict contract

This surface publishes a reproducible public verdict contract.

Required fields:
- `law_ref`
- `state_ref`
- `proof_ref`
- `execution_ref`
- `verifier_version`
- `verdict`
- `reason_codes`
- `contradictions`
- `generated_at`

Demo artifact:
- `public/verdict.json`

## Status

* Repository role: public verifier surface only
* Public host ownership: `verify.verifrax.net`
* npm package: `@verifrax/verifrax-verify`
* Surface class: public-facing static verification UI
* Deployment model: static site surface
* Package status: public npm package `@verifrax/verifrax-verify@0.1.2` plus public verification UI surface
* Stack position: verification surface, downstream of authority and execution, separate from proof publication
* Artifact-chain relation: public verification path for the broader chain, but not the authority source, receipt issuer, or artifact registry root
* License: Apache License Version 2.0

## One-sentence role

`VERIFRAX-verify` exposes the public verifier for inspectable Verifrax proof material at `https://verify.verifrax.net/` while preserving a hard separation between verification, proof publication, authority issuance, governed execution, and evidence-root chain registration.

## What this repository is

This repository owns the public verifier surface.

Verification is not publication. Verification is not execution. Verification is not authority.

## Verifier role boundary

This repository is the public verification surface only.

It exists to inspect published proof material and return verification results.

It is not proof publication.
It is not authority issuance.
It is not governed execution.


Its job is to make verification available publicly, portably, and inspectably.

It exists so a reader can:

* open a public verifier at `https://verify.verifrax.net/`
* inspect proof-shaped material through a static verification surface
* review proof fields without trusting an opaque server runtime
* keep verification separate from proof publication
* keep verification separate from authority issuance
* keep verification separate from governed execution

This repository is the read-only verification-facing boundary in the main Verifrax perimeter.

The key role is narrow and deliberate:

* authority comes from `AUCTORISEAL`
* execution and receipts come from `CORPIFORM`
* authored source and evidence-root chain truth live in `VERIFRAX`
* proof publication lives in `proof`
* public verification lives here

That separation is the point.

## What this repository is not

This repository is not proof publication.
This repository is not authority issuance.
This repository is not governed execution.
This repository is not intake.
## Public host ownership

This repository owns exactly this public host:

* `https://verify.verifrax.net/`

It does not own:

* `https://proof.verifrax.net/`
* `https://api.verifrax.net/`
* `https://auctoriseal.verifrax.net/`
* `https://corpiform.verifrax.net/`
* `https://sigillarium.verifrax.net/`
* `https://apply.verifrax.net/`
* `https://docs.verifrax.net/`
* `https://status.verifrax.net/`

A verifier README must say this explicitly so no second public host is silently claimed.

## Position in the Verifrax system

The main perimeter is intentionally separated:

* [`.github`](https://github.com/Verifrax/.github) — governance root
* [`AUCTORISEAL`](https://github.com/Verifrax/AUCTORISEAL) — authority issuance and authority reference
* [`CORPIFORM`](https://github.com/Verifrax/CORPIFORM) — governed execution and receipt boundary
* [`VERIFRAX`](https://github.com/Verifrax/VERIFRAX) — authored source, maintained implementation surface, and evidence-root chain record
* [`proof`](https://github.com/Verifrax/proof) — public proof publication surface
* [`VERIFRAX-verify`](https://github.com/Verifrax/VERIFRAX-verify) — public verifier surface
* [`SIGILLARIUM`](https://github.com/Verifrax/SIGILLARIUM) — seal/archive reference surface

This repository belongs to the verification slot only.

## Proof versus verify

This distinction must stay hard:

### `proof.verifrax.net`

* publishes public proof material
* exposes proof retrieval semantics
* is the proof-facing publication surface

### `verify.verifrax.net`

* verifies or inspects proof-shaped material
* is the public verification tooling surface
* is intentionally distinct from publication

The failure mode here is obvious:

if `verify` starts reading like `proof`, then there are two public proof surfaces.
That is boundary collapse.

So this README must keep the distinction visible everywhere.

## Authority versus verify

Verification does not create authority.

This repository can inspect and present proof material, but it cannot mint, elevate, or repair authority state.

Authority belongs upstream to `AUCTORISEAL` and governed chain references, not to this UI surface.

A useful limiting case:

if the verifier displays a proof object perfectly, that still does not turn the verifier into the authority issuer behind the proof.

## Execution versus verify

This repository does not execute governed actions.

It does not:

* authorize a command
* enforce a runtime boundary
* emit a receipt
* lock replay resistance
* mutate chain state

Those belong to `CORPIFORM` and the governed execution path.

A verifier can inspect a result.
A verifier is not the runtime that produced it.

## Artifact-0005 relationship

`artifact-0005` must remain visible across the repo perimeter because it is a load-bearing chain boundary in the broader Verifrax system.

But this repository must describe that relationship precisely.

`VERIFRAX-verify` is relevant to artifact-0005 because the public verification path must be visible and inspectable across the system boundary.

It is not relevant in these false ways:

* it does not author artifact-0005
* it does not issue the authority object for artifact-0005
* it does not produce the governed receipt for artifact-0005
* it does not register artifact-0005 in the evidence root
* it must not claim artifact-0005 is sealed unless the evidence-root chain truth actually says so

The correct statement is narrower:

this repository is part of the public verification-facing perimeter that must remain aligned with artifact-0005 and its verification path.

## What problem this repository solves

Without a separate verifier surface, public proof inspection tends to collapse into one of two bad patterns:

* trust a private engine blindly
* confuse proof publication with proof verification

This repository solves that by exposing a dedicated public verifier surface.

It lets a reader inspect proof-shaped material without converting the publication host into the verifier and without converting the verifier into the authority or runtime.

## Verification surface contract

This repository should describe only the verification surface that is actually present.

That means the README must speak in terms of public inspection and verification-facing behavior, not inflated protocol claims.

A truthful verifier contract includes only surfaces that are really present, such as:

* static UI loading
* deterministic field presentation
* schema or structure checks if implemented
* digest-format validation if implemented
* local-file-assisted comparison if implemented

It must not claim:

* hidden remote execution
* server-side trust guarantees
* authority issuance
* proof publication ownership
* chain registration

## Trust model

The trust posture here should stay minimal.

This repository should remain understandable as:

* static where possible
* inspectable in code
* explicit in limits
* separate from proof generation
* separate from authority and runtime

That is stronger than a glossy UI with hidden behavior.

## Inputs and outputs

### Inputs

This repository works on proof-shaped inputs supplied by the user or loaded into the public verification surface.

### Outputs

This repository emits verification-facing inspection results only.

It does not emit:

* authority objects
* execution receipts
* proof publication records
* artifact registrations
* legal or institutional decisions

## Package truth boundary

This repository README must not imply a public package surface unless package metadata proves one exists.

So the safe current boundary is:

* repository surface: yes
* public verifier host: yes
* package claim: only if mechanically proven elsewhere in metadata

That rule matters because verification UIs often drift into package theater.

## Why this repository must stay visually and mechanically distinct

A verifier surface should never feel like:

* the commercial landing page
* a proof archive
* the execution API
* the authority portal
* a docs mirror

The reader must know within seconds:

this is the verifier.
Nothing else.

## Canonical related repositories and surfaces

* [`.github`](https://github.com/Verifrax/.github) — governance root
* [`VERIFRAX`](https://github.com/Verifrax/VERIFRAX) — authored source and evidence-root chain record
* [`AUCTORISEAL`](https://github.com/Verifrax/AUCTORISEAL) — authority issuance/reference
* [`CORPIFORM`](https://github.com/Verifrax/CORPIFORM) — governed execution and receipt boundary
* [`proof`](https://github.com/Verifrax/proof) — proof publication repository
* [`https://proof.verifrax.net/`](https://proof.verifrax.net/) — public proof publication surface
* [`https://verify.verifrax.net/`](https://verify.verifrax.net/) — public verifier surface
* [`SIGILLARIUM`](https://github.com/Verifrax/SIGILLARIUM) — seal/archive reference surface

## Reader contract

A reader landing here must be able to answer immediately:

1. Is this the public verifier? Yes.
2. Does it own `verify.verifrax.net`? Yes.
3. Is it the proof publication host? No.
4. Is it the authority issuer? No.
5. Is it the execution runtime? No.
6. Is it the evidence-root chain registry? No.
7. Is it part of the public verification-facing perimeter for artifact-0005? Yes.

If any of those answers are blurry, the README is still weak.

## CI and governance expectations

If CI exists here, it should validate verifier-surface properties only, such as:

* static build integrity
* deterministic asset output where applicable
* host and deployment alignment
* verifier contract consistency
* no drift between claimed host and deployed host

This README must not imply authority, execution, or evidence-root guarantees just because a build is green.

## Contributing

A contribution here is wrong if it:

* turns the verifier into a proof publication surface
* turns the verifier into an authority surface
* turns the verifier into an execution surface
* adds package claims not backed by metadata
* claims artifact-0005 is sealed without evidence-root backing
* removes the proof-versus-verify distinction
* removes the execution-versus-verify distinction
* removes the authority-versus-verify distinction


## Verifrax system path labels

The governed Verifrax path that this README must stay compatible with is:

1. `.github` — organization governance and governed repository boundary
2. `AUCTORISEAL` — authority issuance and public authority reference
3. `CORPIFORM` — governed execution and receipt emission
4. `VERIFRAX` — authored protocol, evidence root, and artifact-chain registration boundary
5. `VERIFRAX-SPEC` — derived specification publication surface
6. `VERIFRAX-PROFILES` — deterministic profile-constraint surface
7. `VERIFRAX-SAMPLES` — pinned sample and reproducibility surface
8. `VERIFRAX-verify` — public verification repository and UI boundary
9. `VERIFRAX-DOCS` — explanatory documentation surface
10. `cicullis` — enforcement boundary
11. `proof` — proof publication surface
12. `SIGILLARIUM` — seal and archive reference surface
13. `apply` — intake surface

The live host-label map that must remain explicit and non-contradictory is:

* `https://api.verifrax.net/` — execution surface
* `https://proof.verifrax.net/` — proof publication surface
* `https://auctoriseal.verifrax.net/` — authority issuance and authority reference surface
* `https://corpiform.verifrax.net/` — runtime and receipt reference surface
* `https://cicullis.verifrax.net/` — enforcement reference surface
* `https://verify.verifrax.net/` — public verification surface
* `https://sigillarium.verifrax.net/` — seal and archive reference surface
* `https://apply.verifrax.net/` — intake surface
* `https://docs.verifrax.net/` — documentation surface

This README must remain compatible with `artifact-0005` as the load-bearing authority → execution → verification → evidence boundary without claiming that this repository alone authors, proves, seals, or registers `artifact-0005` unless that role is actually true for this repository.


## Security

Treat this repository as a public verification surface.

Do not introduce:

* hidden server trust
* secret-dependent verification behavior
* privileged remote execution
* implicit proof mutation

## License

Apache License Version 2.0. See `LICENSE`.

## Adjacent sovereign surfaces

This repository is part of the Verifrax sovereign stack and remains bounded relative to:

- **[ANAGNORIUM](https://github.com/Verifrax/ANAGNORIUM)** for terminal recognition
- **[REGRESSORIUM](https://github.com/Verifrax/REGRESSORIUM)** for terminal recourse

