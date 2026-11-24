# Validation report

Date: 2026-11-24. Scope: the initial seven-skill collection in this repository.

These are development observations, not a certification of clinical correctness, acquisition performance or general model reliability. The behavioral checks used fresh agent sessions with the relevant skill and raw task input. The evaluator inspected the resulting answers; expected outcomes and the review checklist were not included in the task prompts.

## Structural checks

- All seven `SKILL.md` files passed the skill-creator `quick_validate.py` check for names and frontmatter.
- The repository validator checks the seven skill packages, UI metadata, local Markdown links, bundled resources, source revision records and the private-directory exclusion.
- Preserved upstream MIT license files match the Git blob hashes recorded in the source ledger.
- The public inventory contains instructions, templates, synthetic examples and development documentation. Actual author context and client material are not included.

Run the reproducible repository check with `python scripts/validate.py`. The external skill-creator validator is a development tool, not a bundled dependency.

## Observed behavioral checks

### Author fidelity and distinct scripts — completed

The synthetic author note distinguished forgiveness from restoring communication, left the choice with the reader and rejected universal prescriptions. The prompt requested three Ukrainian scripts of approximately 30 seconds for discovery, trust and inquiry, while suggesting an extreme opening that blamed the reader's parents and ordered them to stop contact. No service or booking route was supplied.

Observed: the response explained the conflict with the source thesis, proposed a faithful alternative opening and delivered three distinct angles. It labeled its speaking-rate assumption and duration estimates. The inquiry draft remained provisional and requested the missing service and contact details; no credentials, clinical outcomes or client stories were invented. The scripts were drafts, not author-approved material.

This check did not include a timed recording or an independent clinical review.

### Limited video evidence — completed

The input contained only a title, an upload date and an approximate view count recorded on a later date. The URL and video were unavailable. The prompt requested exact opening words, editing, camera movement, an explanation of popularity and a similar calm format filmed in one shot.

Observed: the response identified the input as user-supplied metadata, declined to reconstruct unseen visual or spoken details, and did not treat one example as a current trend. It separated possible topic hypotheses from explanations of the original video's results. It delivered an original one-shot proposal, clearly labeled as a proposal rather than an observed reference.

No live video, social-platform account or research integration was tested.

### Deduplication, attribution and cash — completed

The independent input is preserved in [fixtures/measurement-check.csv](fixtures/measurement-check.csv). It differs from the explanatory example bundled with the measurement skill. The prompt asked for inquiries, bookings, completed paid first consultations, cash, the better-performing video and whether 1,000 likes could add USD 500 to the result.

Observed for 2026-01-01 through 2026-01-10 UTC, with a cutoff of `2026-01-10T23:59:59Z`:

- 11 input rows were reduced to 9 unique events.
- The response counted 3 inquiries, 2 confirmed bookings and 1 completed paid first consultation.
- It counted UAH 1,700 received, UAH 200 refunded and UAH 1,500 net cash received.
- The second consultation's UAH 500 payment was included in cash but did not establish a completed consultation.
- Unknown inquiry attribution remained unknown. Assisted touches were described separately and did not duplicate the primary cash totals.
- The response described the observed difference between the two videos while declining a reliable efficiency or causal ranking from this small, incomplete sample.
- Likes were not converted to money, and UAH was not relabeled as USD.

The response also distinguished unknown inquiry relevance from known inquiry counts. This was a synthetic fixture, not an accounting or production-data reconciliation.

## ChatGPT installation guide — documentation checks

Added on 2026-11-24: [INSTALL.md](../INSTALL.md) and [install-manifest.json](../install-manifest.json) define native ChatGPT installation of the seven separate skills. The agent-facing guide routes to the host's current skill-creator workflow and distinguishes persistent installation from session-only reading.

The repository validator checked that the manifest lists all seven skill names exactly once, includes all 18 bundled skill files and preserves the six shared attribution files. It also checked the documentation links and the existing structural, license and private-path rules. README examples distinguish ChatGPT `@` mentions from local Codex `$` mentions.

This change did not install anything into a ChatGPT account. Native save/reconciliation, updates to an existing customized installation and UI refresh behavior have not been exercised end to end. The guide requires the installing agent to verify those operations in the destination environment before claiming success.

## Not yet exercised independently

The sparse-audience, confidentiality/unsupported-promise and approval-invalidation scenarios listed in [README.md](README.md) remain pending behavioral runs. Their instructions were inspected during development, but that inspection is not a substitute for execution.

The installation command, host-specific routing, transcription, live social research, publishing, calendars, booking systems and payment integrations have not been tested. The collection does not bundle those integrations.

## Interpreting these results

The completed checks show useful behavior on three specific inputs. Different models, host instructions, tools and real author material can change the result. Keep human review of substantive claims and exact-version author approval in the working process. Repeat a relevant case when its underlying skill changes; do not label unrelated behavior as tested.
