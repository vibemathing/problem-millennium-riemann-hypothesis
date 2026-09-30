# Pending migration proposal

Base: 22e12db0044bb0f54ffee367418f7a0ac828d233. All IDs here are proposed, not admitted.

The canonical contract and Harness remain unchanged. The source-enriched contract proposal targets the current upstream template schema, which is newer than this repository's frozen schema. Its source-list consolidation and changed contract digest require owner/importer review. Attempt and graph proposals intentionally bind the existing contract digest 7cac6709e27ac95484f50c4dc11f19611230eab525665df7feccc260455d0ba9, not the proposed digest 54f69f22bcd27dbd92ad5c37e6c94a016742fa532f1b60b880ad6449a94f24ee. If the contract changes, rebase all proposal bindings atomically through the trusted path before admission.

No independent verification receipt is supplied. Research drafts preserve the exact scoped result and open root bridge. The leaf is deliberately not a sufficient dependency for root closure. The richer six-way exploration is in RESEARCH.zh.md.

Reasoning checks: scope and assumptions explicit; dependency chain and witness explicit; exact negative controls included; symmetry (RH) and valuation invariant (BSD) examined; bounded loops terminate at 88 or six points; probability/extremal method not applicable to these exact deterministic checks; finite-to-global transition explicitly prohibited.

Expected compatibility boundary: pending inbox validation supports admission_request; strict diff validation still requires pre-admitted Attempt/Graph. Do not weaken this gate or manufacture truth-ledger entries to make CI green. A Harness maintainer must reconcile the gate separately, or a trusted importer must admit reviewed objects. Full root problem remains open in this submission.

Best local result: scoped prior exploratory draft and exact regression. Next obligation: source/statement review plus trusted admission; then the open bridge or next leaf described in the draft.
