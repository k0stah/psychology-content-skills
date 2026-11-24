---
name: content-measurement
description: Assess a psychology blog using observed inquiries, bookings, paid first consultations, revenue, and author effort. Use for content-performance reviews, outcome exports, attribution questions, or choosing what to continue. Deduplicate events, distinguish unknown from zero, preserve attribution uncertainty, and keep attention metrics separate from business outcomes.
---

# Content Measurement

Connect publishing decisions to observed outcomes and production effort. Report what the available evidence can establish, in the user's chosen language.

## Inputs and private context

Read the relevant goals, services and accepted measurement definitions in `private/psychology-content/context.md` in the user's working project if available. Accept manually supplied totals or exports; do not require a live integration. Obtain the reporting window, timezone, observation cutoff, currency and meaning of each status before drawing comparisons.

Use anonymous operational references only. Exclude names, contact details, message bodies, symptoms and clinical notes; request minimized or aggregate inputs when necessary. Before writing, verify that `private/psychology-content/` is ignored by Git, or use a user-approved directory outside Git. Keep chat-only work in chat. Never save real outcome records in this installed skill or public collection.

For event-level data, read [the measurement definitions](references/measurement-definitions.md). Use [outcomes-template.csv](assets/outcomes-template.csv) only if a new ledger is useful; preserve compatible user schemas instead of forcing a migration. The [synthetic fixture](assets/outcomes-synthetic.csv) demonstrates duplicate handling, refunds and unknown attribution; it is not business evidence.

## Workflow

1. **Define comparable scope.** State the time window, eligible services, event definitions and data sources. Separate events occurring during the reporting period from outcomes of a publication or inquiry cohort. Include the observation cutoff so recent content's incomplete follow-up remains visible.
2. **Inspect coverage.** Identify missing channels, dates, statuses, counts or payment records. Record `unknown` when no observation exists. Use zero only for a measured zero in the stated scope. An absent row in a partial export is not proof of no event.
3. **Deduplicate and reconcile.** Use stable event/booking/payment identifiers where available. Distinguish duplicate exports from distinct events and distinct people. Resolve conflicting copies against their evidence; do not arbitrarily pick one. If only aggregates exist, state that deduplication and overlap could not be verified.
4. **Count business outcomes.** Report observed relevant inquiries, confirmed bookings and completed paid first consultations using explicit definitions. Mark inquiry relevance unknown unless supported by the author's non-clinical service-fit classification. Reconcile recorded payments and refunds per currency; distinguish cash received from any accounting revenue measure. Keep repeat consultations separate from acquisition outcomes.
5. **State attribution.** Use observed tracked links, explicit self-reports or other documented evidence. Label the basis and any assignment rule. Count each outcome once in overall totals. Show assisted content separately without adding the same outcome or payment to several channel totals. Keep unknown and unassigned attribution visible; do not treat a tracked association as proof of causation.
6. **Add supporting measures.** Report views, saves, watch time and other available attention measures with platform definitions and capture dates. Report author minutes per approved or published item when measured, with a declared allocation for shared batch effort. Do not invent revenue per like, convert views into clients, or substitute assumed effort for observed time.
7. **Compare carefully.** Compute conversion rates only with matched, eligible cohorts and a clear denominator. A zero or unknown denominator yields `not calculable`. Account for follow-up delay, channel/service differences and small samples. Use low-volume results to propose hypotheses; do not declare statistical significance or causal lift without an appropriate study.
8. **Recommend a focused continuation.** Identify what to repeat, revise or investigate, tied to the observed outcomes and effort. Separate findings from hypotheses and name the missing evidence that could change the decision. Preserve the author's topic and service boundaries.

## Output contract

Return:

- **Scope and coverage:** period, cutoff, definitions, sources and known gaps.
- **Observed outcomes:** inquiries with known/unknown relevance, bookings, completed paid first consultations, payments/refunds/net cash by currency, and author effort where available.
- **Attribution:** assigned, assisted and unknown outcomes; assignment rule and deduplication limitations.
- **Interpretation:** what the evidence suggests, what remains uncertain, and one or a few justified content decisions.

If files are requested, save minimized records and reports under `private/psychology-content/results/` after the privacy check. Add only explicitly accepted learnings to `context.md`; never turn an association from one small batch into an enduring audience fact.

## Failure handling

If outcomes are unavailable, report available attention or effort data and explain that commercial performance is unknown. If amounts or currencies conflict, keep unresolved amounts out of a claimed reconciled total and show the gap. If exact duplicates cannot be distinguished, report a defensible range or unreconciled totals with their basis; do not fabricate precision. Never change booking/payment records or contact people as part of measurement.
