# Sources and adaptation decisions

Reviewed on 2026-11-24. This collection selectively adapts reusable instruction patterns and adds an author-led psychology content workflow. It does not install upstream collections or run their integrations.

The authoritative provenance record is [sources/upstream.json](../sources/upstream.json). It records the exact commit observed from each repository's `main` ref, every instruction path reviewed, its Git blob SHA, the applicable upstream license, the local target skills and the adaptation decision. Source-file links use the recorded commit, so later upstream changes do not silently change this review.

## What was adapted

### Shared context, audience research, editing and measurement

[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/tree/8fd2fcade2fd6629026e9dfe6d133b55b36968b9) supplies the source patterns reviewed in `product-marketing`, `customer-research`, `social`, `copy-editing` and `attribution`.

The local adaptations are:

- `author-context`: one reusable context, with the author's services, language, voice, intended audience and accepted learnings.
- `audience-funnel`: audience needs and objections tied to evidence; provisional assumptions stay labeled.
- `content-repurpose`: one theme developed into distinct audience questions and content jobs.
- `psychology-review`: focused editorial checks that preserve meaning and identify unsupported claims. The psychological-content rules and author approval requirement are local additions.
- `content-measurement`: observed outcomes, one count for each actual payment, an explicit attribution basis and clearly stated unknowns.

Upstream marketing toolkits have broader commercial and technical scopes. This collection omits their advertising, outreach, publishing and event-tracking implementations. It replaces their separate context locations with `private/psychology-content/context.md`. It also replaces generic commercial persuasion with professional boundaries and a relevant-inquiry goal.

The full MIT notice is retained in [coreyhaines31-marketingskills-MIT.txt](../LICENSES/coreyhaines31-marketingskills-MIT.txt).

### Author voice and shootable scripts

[social-media-skills/skills](https://github.com/social-media-skills/skills/tree/f28cef2b7067ec64e79c9d85421c022c06659e03) supplies the source patterns reviewed in `brand-profile`, `voice-builder` and `short-form-video-script`.

The author-context adaptation derives voice rules from actual author samples and explicit corrections. The content-repurpose adaptation separates spoken text, on-screen text and filming notes. It keeps the author's intended meaning, names missing facts, and checks the expected recording time instead of assuming any script fits a fixed duration.

WoopSocial publishing assumptions, unbundled sibling-skill dependencies and universal retention benchmarks are removed. Each draft serves its chosen discovery, trust or inquiry job. A filming suggestion is not a claim that the system watched or rendered a video.

The full MIT notice is retained in [social-media-skills-MIT.txt](../LICENSES/social-media-skills-MIT.txt).

## What was reviewed only

### Discovery and video analysis

[bradautomates/head-of-content](https://github.com/bradautomates/head-of-content/tree/d841dcff2e4d74a4c31cb3ed2de6c2184de3a970) was reviewed for its YouTube, Instagram, TikTok and video-content-analyzer instruction documents. It illustrates a separation between finding candidates and analyzing their content.

The reviewed upstream instructions depend on services including Apify, TubeLab and Gemini. None is installed, configured or required by this collection. No upstream scripts or instruction files are bundled. A future integration must separately establish authorized access, available media, actual cost and what the returned data supports.

The local `format-research` skill accepts available evidence and labels whether an observation came from metadata, a transcript or actual video. It preserves the source URL and observation date. It does not treat a page URL as proof that the agent obtained the video, or explain high view counts as if a particular format's causal effect had been established.

### Creator-script alternative and excluded remakes

[Melvynx/video-agent-skills](https://github.com/Melvynx/video-agent-skills/tree/f4542923f7f796a1fa0e544cbfc1109d5eec87d8) was reviewed through `studio-script` and `outliers`. The former is a relevant alternative for creator-voice scripting and timing. Neither skill's instructions, tool configuration nor executable code is redistributed here.

The `outliers` approach includes closely remaking selected videos. That approach is excluded. This collection may describe an abstract device, such as opening with a question and contrasting two concepts, but it requires original arguments, examples and wording. It does not reproduce another creator's full transcript or preserve another script's sentence-by-sentence sequence.

Treg, yt-dlp, upstream account connections, video editing and publishing are not part of this release.

## Why integration is selective

The collection has a single shared context and seven focused skills. Copying multiple complete frameworks would introduce competing context files, repeated onboarding, incompatible defaults and extra tool dependencies. The local workflow instead keeps author decisions and evidence consistent across the editorial steps.

The following rules are deliberate local design choices:

- The author's thesis is preserved; an AI review identifies issues and does not replace professional judgment.
- Client and group details that could identify people are excluded from intake. Working material stays outside the public collection.
- A theme produces distinct questions and perspectives. If the source material supports fewer useful pieces, the agent produces fewer.
- Borrowing an abstract format does not authorize a close remake of someone else's content.
- No dollar-per-like or dollar-per-view formula is used. Revenue is an observed outcome from supplied records, not an inferred value of attention.
- Platform views, saves and engagement are supporting measures. Relevant inquiries, bookings, paid first consultations and recorded revenue are reported separately with their attribution limits.
- Only explicit author corrections and accepted decisions become enduring context. Unreviewed model output does not become a new fact.

## License and review scope

Both adapted upstreams use the MIT License at the pinned revisions. Their notices are preserved in `LICENSES/` and identified in [NOTICE.md](../NOTICE.md). Reference-only entries retain their source and license URLs for traceability; their presence is not a claim that their code was incorporated.

This review inspected selected instruction documents and license notices through read-only GitHub retrieval. It did not execute upstream scripts, install packages, request credentials or test live platform integrations. The source manifest is a provenance record, not a security certification or a promise that a referenced provider remains available.

When an adaptation changes, review the new source revision deliberately, update the manifest and modification notes, and retain all applicable notices. Do not silently replace a pinned source with a moving branch reference.
