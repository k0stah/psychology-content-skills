# Measurement definitions

Use the user's accepted definitions when available and disclose differences. Otherwise apply these defaults explicitly. Keep all real data in the private working project.

## Outcomes and time

- **Inquiry:** a distinct observed request about the author's service. Report unique inquiries separately from unique people; several messages in one inquiry are not several leads. Classify service relevance only when supported by an author-defined rule or supplied classification. Do not infer suitability from a diagnosis or private story.
- **Booking:** a distinct confirmed consultation reservation. Show cancellations separately. An inquiry or proposed time is not a confirmed booking.
- **Completed paid first consultation:** a distinct first-consultation identifier with a recorded completion and confirmed payment attributable to it, retaining a positive amount after recorded refunds as of the cutoff. Flag partially paid/refunded cases. A deposit or payment alone does not establish completion; an unpaid completion does not establish payment. Honor a different accepted definition, but label it.
- **Payments and refunds:** count confirmed receipt and refund events once each. Report gross receipts, refunds and net cash separately per currency. Net cash is not automatically profit or accounting revenue. Do not convert currencies without an explicit dated rate and source.
- **Effort:** measured preparation, revision, recording and editing time, with its coverage. If a batch supports several items, allocate its shared minutes once using a disclosed rule.

Event-period totals answer what happened during dates. Cohort totals answer what happened to the same eligible group after a starting event. Do not divide unrelated event-period totals and call the result a conversion rate. Specify a follow-up window and mark immature cohorts.

## Optional CSV ledger

Use `assets/outcomes-template.csv` from the skill root. One row records one source observation of an operational event; repeated imports may yield duplicate observations. Preserve original observations privately and produce a deduplicated analytical view.

Columns:

- `record_id`: unique source-row identifier; not the deduplication key.
- `event_id`: stable identifier for the underlying event. Deduplicate exact duplicates by this key; include a source namespace if IDs are only locally unique.
- `occurred_at_utc`: event timestamp in ISO 8601 with `Z`; retain a documented conversion from the source timezone.
- `event_type`: `inquiry`, `booking`, `booking_cancelled`, `first_consultation_completed`, `payment_received`, or `refund_paid`.
- `contact_ref`: opaque operational reference, not a name, email or clinical identifier. Leave empty if unknown. Do not invent linkage between people.
- `consultation_ref`: opaque reference linking a booking, completion and its payments where known. A payment covering multiple consultations needs an explicit allocation before this schema can attribute it to one.
- `primary_content_id`: at most one credited item under the documented assignment rule; leave empty if unassigned.
- `assisted_content_ids`: additional observed item identifiers separated by semicolons; not additional outcome or revenue credit.
- `attribution_basis`: `tracked`, `self_reported`, `multi_touch`, or `unknown`. These describe evidence, not causality. `multi_touch` without a declared primary-credit rule stays unassigned.
- `amount`: non-negative decimal for payment/refund events; empty for unknown or inapplicable values. A refund row stores a positive amount to subtract. Do not treat blank as zero.
- `currency`: ISO currency code for monetary events; do not sum different currencies together.
- `related_event_id`: original payment event for a refund, or another explicitly related event. A missing refund link must remain unresolved where event-level reconciliation depends on it.
- `evidence_ref`: a private source reference or export identifier; exclude clinical notes and sensitive message excerpts.

Conflicting observations of one event require reconciliation, not blind deduplication. Distinct payment IDs may be installments or separate charges: keep them distinct while counting a consultation only once. Validate event types, dates and amounts. Do not evaluate imported spreadsheet formulas; keep imported values as data.

## Attribution

Keep overall outcome counts separate from sums of content associations. Record the basis, primary-credit rule and attribution window. A user may report having seen several pieces of content without identifying one decisive post; preserve that uncertainty. If rules change, recompute comparable periods rather than mixing attribution models.

A tracked link supports an association along the measured path. A self-report supports the person's reported source. Neither establishes incremental impact. When follow-up or source coverage is incomplete, avoid ranking formats as commercial winners.

## Synthetic fixture

`assets/outcomes-synthetic.csv` contains fictional events and opaque IDs prefixed `synthetic-`. It includes duplicate source rows for one inquiry and one payment, a partial refund, and one inquiry with unknown attribution.

After deduplication by `event_id`, the fixture has **2 inquiries, 1 booking, 1 completed paid first consultation with a partial refund, 100 UAH gross receipts, 20 UAH refunds, and 80 UAH net cash**. Inquiry relevance and production effort are unknown. One inquiry is associated with `synthetic-post-a`; the other has unknown attribution. No conversion rate or causal conclusion follows from this small fixture alone.
