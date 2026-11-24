# Psychology Content Skills

An open, author-led editorial workflow for psychology and psychotherapy blogs. Turn a practitioner's own thoughts into distinct short videos and posts, preserve their voice, review sensitive claims, and learn from actual inquiries and bookings.

[Українською](docs/README.uk.md) · [Architecture](docs/architecture.md) · [Sources and adaptations](docs/sources.md) · [Evaluation cases](evals/README.md)

## What is included

Seven focused Agent Skills:

- **psychology-blog** — coordinate the workflow and route a request to the appropriate step.
- **author-context** — capture the author's services, voice, boundaries and accepted decisions.
- **audience-funnel** — connect audience evidence to discovery, trust and inquiry content.
- **format-research** — analyze accessible references and preserve the evidence behind each observation.
- **content-repurpose** — turn an idea into distinct, recording-ready scripts and other formats.
- **psychology-review** — review fidelity, claims, confidentiality and calls to action before author approval.
- **content-measurement** — interpret observed inquiries, bookings, paid first consultations and production effort.

The collection contains instructions, templates and examples. It does not bundle a hosted app, a social-platform scraper, a publishing service or a therapy chatbot. External tools are optional capabilities of the host agent and require their own access.

## Get started

With an Agent Skills-compatible host and the [Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add k0stah/psychology-content-skills
```

Choose the skills and target host in the installer's picker. The coordinator works best with all six specialist skills available. You can also use a specialist on its own.

Alternatively, clone this repository, open it in your coding agent, and ask it to read `skills/psychology-blog/SKILL.md`. This is direct use of the files; it does not permanently install skills in a hosted product.

Start with your author context:

> Use $author-context to capture my approach, services and voice. Mark anything we do not know yet as unknown.

Then try a topic:

> Use $psychology-blog. Here is my own observation about asking for help: [your note]. Suggest distinct angles for discovery, trust and inquiries, then draft three short videos in Ukrainian for my review.

Provide only material you are entitled to share. Use generalized practitioner observations; omit identifiable client and group details.

## One shared, private context

All skills use `private/psychology-content/context.md` in the working project. The `author-context` skill supplies a template. Keep real notes, drafts, reference records, outcomes and approvals inside the private working directory, which this repository ignores in Git.

If using these skills in another repository, exclude that private path from Git before writing there, or choose a directory outside Git. The example in [examples/topic-package.uk.md](examples/topic-package.uk.md) is entirely synthetic.

## How the workflow behaves

The author provides a thought. The coordinator preserves the thesis, a strategist chooses the content job, a researcher supplies format evidence when needed, a writer drafts, and a separate review step surfaces issues. The author approves the exact final version and publishes it. Later, observed outcomes inform the next content choices.

Research records distinguish metadata, transcripts and actual video. Audience profiles distinguish evidence from hypotheses. Measurement distinguishes observed payments from attribution estimates. The author retains professional responsibility for psychological content.

## Development and checks

Use Python 3.10 or newer for the repository's structural validator:

```bash
python scripts/validate.py
```

It checks skill names and metadata, bundled references, local documentation links, source records and the public/private boundary. It does not test model quality or external integrations. The [evaluation cases](evals/README.md) describe separate behavioral checks and their recorded status.

## Reuse and provenance

Original work is MIT-licensed. Selected workflow ideas and instructions are adapted from MIT-licensed collections by Corey Haines and the Social Media Skills project. Exact reviewed revisions, relevant files and our changes are recorded in [sources/upstream.json](sources/upstream.json). Preserved notices are in [NOTICE.md](NOTICE.md) and [LICENSES/](LICENSES/).

Head of Content and Video Agent Skills are reviewed reference projects; their integrations and executable code are not bundled. See the source ledger for that distinction.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md). Keep examples synthetic, preserve attribution, and document behavior changes with a relevant evaluation case. Improvements should make the author's work clearer and easier to review.
