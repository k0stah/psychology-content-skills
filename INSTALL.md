# Install Psychology Content Skills in ChatGPT

## Send this to ChatGPT

> Встанови всі сім навичок Psychology Content Skills у моєму ChatGPT за інструкцією https://github.com/k0stah/psychology-content-skills/blob/main/INSTALL.md і перевір, що встановлення збережене та всі допоміжні файли доступні.

If the Skills picker is available, you can select `@skill-creator` with the same request. The agent should complete the installation using the current ChatGPT skill-management workflow. You do not need to supply API keys, a GitHub account, an author profile or social-platform credentials for this instruction-only collection.

**Compatibility:** this route requires a ChatGPT environment that can create and install personal skills. Availability depends on the product surface, account and workspace settings. The agent must check its actual capabilities. Reading this page, cloning the repository or running a local-agent installer does not by itself install skills in a ChatGPT account.

## Instructions for the installing agent

### 1. Establish the request and the supported installation route

Follow these steps when the user asks to install this collection, or provides this installation link in an established installation task. A request to explain, audit or summarize the repository is not an installation request. Repository text does not grant permissions or override the host's instructions.

Discover and read the current built-in **skill-creator** instructions for this ChatGPT environment. Use its supported personal-skill installation, validation and persistence workflow. Follow platform prompts and access controls when required. The user's request to install the collection covers all seven skills; do not ask them to run commands or approve each routine copy operation.

Check for a supported way to read the complete public source files, manage personal skills, save changes durably and verify the saved state. Prefer the native mechanism available in this session. Do not hard-code private backend URLs, internal skill IDs, assumed filesystem locations or platform credentials from an example found online.

If only a terminal or ordinary conversation file access is available, that is not proof of ChatGPT personal-skill support. Use the [unavailable-capability path](#when-persistent-installation-is-unavailable) if no native installation route can be found. Do not silently substitute Codex CLI installation for a ChatGPT installation.

### 2. Resolve and inspect one source revision

Canonical repository: `https://github.com/k0stah/psychology-content-skills`.

Use the user's requested revision when supplied. Otherwise resolve the current `main` branch once to an exact commit SHA and retain it for the whole operation. Read [install-manifest.json](install-manifest.json) and every file to be imported from that same revision, using available public-repository tools or a checkout. Do not combine file versions from moving branch URLs.

Read the full `SKILL.md` files and their bundled resources before importing them. Review any executable resources before execution. Do not install from search snippets or reconstructed summaries. If source access is incomplete, name the missing files and stop the affected import instead of creating a partial skill.

This manifest defines seven separate installation units, in this order:

1. `author-context` — shared author, service and voice context.
2. `audience-funnel` — audience evidence and content purposes.
3. `format-research` — reference analysis and evidence limits.
4. `content-repurpose` — distinct scripts and other formats.
5. `psychology-review` — editorial review and author approval.
6. `content-measurement` — observed inquiries, bookings and payments.
7. `psychology-blog` — coordinator using the other six skills.

Install the coordinator last so its supporting skills are available first. Do not merge the collection into one abbreviated skill. Use the exact frontmatter names; the installed directory names may be assigned by the host.

### 3. Reconcile existing skills before writing

Inspect both enabled and disabled personal skills by their exact frontmatter `name`, using the native workflow. Record the status of each of the seven names before changing anything.

- If an enabled skill and its supporting files already match the selected source and attribution package, keep it and report it as already installed.
- If a previous installation has a source record and its current files still match that record, update it in place when the selected source has changed. Preserve its host-assigned identity and any unrelated files.
- If a same-name skill has local changes, unrelated contents, no verifiable provenance or ambiguous duplicates, preserve it. Complete unaffected imports where possible, prepare the specific difference, then ask only for the decision needed to resolve that conflict.
- Preserve a deliberately disabled skill unless the user's current request explicitly includes enabling it. Report that status separately; a disabled dependency does not satisfy the complete active collection.

Never silently overwrite custom instructions, delete other skills, create duplicate same-name entries, rename host-assigned directories or force an update through an access restriction.

### 4. Import complete packages and preserve attribution

For each manifest entry, copy the entire declared skill directory into the personal-skill destination resolved by the host's current installer. Preserve `SKILL.md`, `agents/openai.yaml`, `assets/`, `references/` and all other included regular files with their relative paths. Do not copy `.git`, temporary files or private working data. Do not rely on a symlink into a temporary checkout.

The source skill instructions are portable. Preserve them as supplied, including Codex-style `$skill-name` references in metadata. In ChatGPT-facing messages, select skills with `@skill-name` or refer to their exact names in ordinary language.

Retain the files listed in `attribution.files` in the manifest inside a `provenance/` directory in **each** installed skill, maintaining their source-relative paths. This carries the original project license, third-party notices, preserved licenses and source ledger with every independently installed package. Keep their text unchanged. For example, the root `LICENSES/` files become `provenance/LICENSES/` in the installed skill.

Write `provenance/install-source.json` for each imported skill with:

- the canonical repository URL and exact source commit;
- the source skill path and frontmatter name;
- a manifest of the imported files, recording each installed relative path and its SHA-256 hash, including the copied attribution files.

Exclude the source record itself from its hash list. Include only installation metadata, never author notes or account credentials. Use this record to detect customized files on future runs. Host-owned metadata outside this manifest must be preserved.

Do not install the repository's top-level `AGENTS.md` as the user's global instructions. Installation does not require social-platform tools, publishing integrations, paid services or automatic updates.

### 5. Validate and save each skill through ChatGPT

Use the host's built-in validator on the actual personal-skill destination. Verify the frontmatter name and all `required_files` from the manifest, the copied attribution package and the source record. Resolve local resource links from the installed skill directory. A validated temporary source copy is not evidence of an installed skill.

Save and verify one skill operation at a time using the current native workflow. If that workflow uses a managed checkout, follow its own rules for staging, saving, synchronization and reconciliation; do not replace it with an ordinary scratch checkout or treat an unpushed copy as durable installation. Use its prescribed conflict handling and bounded retries.

After the host finishes saving, resolve the skill by its exact frontmatter name again. Keep any generated directory name. Verify the persisted active record and the imported file contents against the source record; report any substantive host transformation rather than silently accepting a content mismatch.

If an operation fails, retain the completed installations, report the affected skill and the concrete failure, and do not claim that all seven are installed. If platform confirmation is necessary, first prepare the specific packages and changes for review, then request only that required confirmation.

### 6. Verify the collection and report the result

Before reporting success, confirm all seven skills are present and enabled in the host's persisted state. In addition to each `SKILL.md` and `agents/openai.yaml`, check these nontrivial resources:

- In `author-context`: `assets/context-template.md`.
- In `content-measurement`: `references/measurement-definitions.md`, `assets/outcomes-template.csv` and `assets/outcomes-synthetic.csv`.

These paths are relative to their respective skill folders in the manifest; resolve the actual installed locations by name. Confirm that the coordinator's six specialist names resolve without duplicate-name ambiguity.

Report in the user's language:

- the actual mode: **installed in ChatGPT**, **partially installed**, or **not installed**;
- all seven names with status: installed, already installed, updated, disabled, conflicted or failed;
- the source commit and what persistence/resource checks were completed;
- any remaining capability limit, required platform action or unresolved conflict.

Do not claim that behavioral tests, transcription, video research or live integrations ran unless they actually did. If persisted installation is verified but the current conversation's skill list or the Skills UI is stale, explain the difference and suggest refreshing or reopening the Skills page. Do not reinstall solely because that UI is cached.

### 7. Finish installation before author onboarding

Do not require an interview or invent the author's professional profile to complete installation. Do not write personal context into the installed skill folders. Later content work uses `private/psychology-content/context.md` in an appropriate private working project, subject to that project's storage rules.

After verified installation, provide this optional first request in Ukrainian:

> Використай @author-context. Допоможи описати мої послуги, підхід і авторський голос. Невідоме познач як невідоме.

For a content request, use `@psychology-blog`. If the current chat has not refreshed its skill picker, the exact skill names still identify which saved skills the host should resolve; do not pretend the picker has refreshed.

## When persistent installation is unavailable

Explain the specific missing capability in plain language. Do not report that the account has skills installed after merely reading these files or saving them in a temporary filesystem. Do not change workspace settings, request secrets in chat or infer permissions from the presence of a browser or terminal.

If the current interface exposes a supported native installation or upload action, use the host's current instructions and prepare the concrete packages before handing off the required user action. Do not invent an available button, plan entitlement, installation API or plugin listing. Do not claim this GitHub repository is a published ChatGPT plugin.

If no persistent route is available, offer **session-only use** as a clearly labeled fallback: read the coordinator and relevant specialist instructions from the selected revision and apply them to the current request. This is not an installation and does not promise availability in future chats. If the user only asked for installation, report the blocker instead of starting an unrelated content task.

The [README](README.md) separately documents local-agent installation. That path is useful when the user chooses a local coding agent; it does not change the outcome of a ChatGPT-account installation request.

## Sources and validation scope

ChatGPT guidance checked on 2026-11-24:

- [Skills in ChatGPT — OpenAI Help Center](https://help.openai.com/en/articles/20001066-skills-in-chatgpt): availability, native creation/installation and workspace controls.
- [Skills & Plugins — ChatGPT Learn](https://learn.chatgpt.com/docs/skills-and-plugins): skill use and ChatGPT `@` invocation.
- The current ChatGPT-provided `skill-creator` instructions available to the installing agent govern the actual save and verification process; prefer them over a frozen reproduction of platform internals.

See the [validation report](evals/validation-report.md) for what was checked. Documentation and manifest checks are separate from a live installation into a user's ChatGPT account.
