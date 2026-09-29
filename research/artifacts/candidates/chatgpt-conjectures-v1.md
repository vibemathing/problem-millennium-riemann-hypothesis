# Candidate-only Eight-Category Conjecture Map (ChatGPT export)

- Repository: vibemathing/problem-millennium-riemann-hypothesis
- Problem: problem:millennium-riemann-hypothesis (RH)
- Source: user-provided ChatGPT export `ChatGPT-提出黎曼猜想-20260909-1842.md`, content SHA-256 `6abe3426bfb7995c3ffaf0a16b4d95ce755f1227c55da1142e296b4c1e692fa9`
- Status: candidate_only; statement_faithfulness pending; prior-art review pending; independent verification pending
- Transport classification: computation (bounded classification/catalog audit). This file claims no proof, counterexample, Evidence, Result, or Solution.

## Boundary

The export itself repeatedly states that: (1) the repository root statement (RH) remains open; (2) the entries below are pre-admission drafts, not admitted Attempts; (3) known equivalences (Li criterion, de Bruijn-Newman Lambda=0, fixed-parameter asymptotics) are not new claims; (4) finite checks cannot close the universal statement.

## Eight-category candidate entries

1. C1 existence/negation certificate (RH-E): if RH is false, some generalized Li coefficient at a resonance parameter for an off-line zero becomes strictly negative. Open items: summation convention, multi-zero cancellation, joint parameter growth.
2. C2 universal (RH-U): every nontrivial zero has Re rho = 1/2; equivalently generalized Li nonnegativity for all h>0, n>=1 (root statement, not new).
3. C3 rigidity (RH-R): de Bruijn-Newman constant Lambda = 0; classical equivalence Lambda>=0 (Rodgers-Tao) plus RH iff Lambda<=0.
4. C4 equivalence (RH-Q): not-RH iff some resonance finite negative certificate exists; direction left-to-right is the candidate content.
5. C5 classification (RH-K): off-line zeros split into exposed (lower-envelope) versus masked; "Li-visible iff exposed" is a working candidate needing a frozen definition.
6. C6 extremal bound (RH-B): first negative certificate order bounded by (T/delta) log(2+T^2/delta); export notes the single-quadruple version may be provable before being conjectural.
7. C7 asymptotic/sign (RH-A): unique dominant off-line quadruple gives exponential oscillation with sign density governed by phase; fixed-h n log n asymptotics do not apply to growing h.
8. C8 decidability (RH-D): interval-arithmetic search over rational h,n that never outputs a false negative certificate under RH and terminates with one when RH fails; correctness and termination are the open claims.

## Suggested first lane

Freeze definitions for C6/C7 (summation convention, resonance parameter, certificate scale), verify the generalized-Li literature status, then treat the single-quadruple background bound as an atomic obligation. All numerical work remains bounded evidence.

## Falsifiers / unresolved

- Multi-zero phase cancellation; finite-coefficient sign results already in the literature; parameter h ~ T is not covered by fixed-parameter asymptotics.
- Statement faithfulness of every "known theorem" citation inside the export is pending source-lock.
