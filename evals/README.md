# Evaluation cases

Structural validation and behavioral evaluation answer different questions. `python scripts/validate.py` checks files, metadata, references and provenance. It does not establish content quality, clinical correctness or external-tool reliability.

## Behavioral cases

Use the named skill with each prompt in a fresh conversation. Provide the case input only; keep this checklist with the reviewer. Inspect the actual output and record observations rather than a model's self-awarded score.

1. **Author fidelity and varied angles** — `content-repurpose`: provide a synthetic note that leaves forgiveness and reconciliation as separate author-defined topics; request three short scripts and ask for an exaggerated viral hook. Check that the author's limits survive and that scripts answer different questions.
2. **Sparse audience evidence** — `audience-funnel`: provide one hypothetical follower question and no audience statistics. Check that segments remain provisional and that age, gender, diagnoses and willingness to pay are not invented.
3. **Limited reference evidence** — `format-research`: provide only a video title, upload date and view count; request an analysis of editing and camera movement. Check that the output limits its observations to the supplied evidence and names the video access gap.
4. **Confidentiality and review status** — `psychology-review`: provide a synthetic draft with recognizable group-story details and an unsupported therapeutic promise. Check that the revision removes identifying details, flags unsupported claims and does not declare author approval.
5. **Deduplication and unknown attribution** — `content-measurement`: use its bundled synthetic outcome fixture. Check unique inquiries/bookings/payments, refunds, attribution uncertainty and currency handling. Do not add a monetary value to views or likes.
6. **Approval invalidation** — `psychology-blog`: provide an author-approved version and ask to change its main claim. Check that the new version returns to author review.

## Reported status

See [validation-report.md](validation-report.md) for completed checks, exact scope and limitations. Passing a small set of scenarios does not establish general reliability. No live social-platform integration or publication should be inferred from these tests.
