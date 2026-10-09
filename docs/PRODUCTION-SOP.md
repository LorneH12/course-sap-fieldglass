# Portfolio course production SOP · v1.0

Owner: Lorne Hopkins. Scope: seven independent portfolio sample lessons, not seven exhaustive curricula. Updated 9 October 2026. This SOP governs work artifacts and release evidence; it does not invent human approvals.

## 1. Analyze

Record audience, job task, prerequisite, performance-gap hypothesis, objective, context and exclusions in each ADDIE record. Separate assumptions from interview or pilot evidence. Verify current software terminology in primary vendor documentation. Use original fictional cases; never import employer-only content or customer records. Name the parent course and this sample’s boundary. Estimate 12–15 minutes without enforcing seat time.

## 2. Design

Write outcome, example, practice, assessment and transfer evidence together. Each assessment item needs a keyed response and a rationale. Distinguish attendance, knowledge-check performance, self-review and independently reviewed work. Use consistent navigation, readable typography, purposeful color and original imagery. Keep brand configuration independent of content; provisional branding is not evidence of actual employer use or approval. Document interaction states, missing answers, retries, completion and data loss.

## 3. Develop

Each course repository owns index.html, css/, js/, assets/, docs/, scripts/ and qa/. Edit content source, regenerate the derived JavaScript, and build the SCORM candidate. Do not hand-edit a distribution ZIP. Bloom’s retains its richer bespoke interaction code; the other six share the same player version. All seven use one tracking adapter. Record a hash of the shared engine and adapter in release evidence. Patch and test the shared source before copying updates into courses.

Architecture decision: the custom player preserves the high-fidelity visual design and the requested separate file structure. It is a documented addition to the existing Adapt proof, not a claim that this is an Adapt export. The Adapt forks and infrastructure remain intact. The suite’s JSON editor is a lightweight authoring aid; it is not the unverified Adapt visual editor.

## 4. Verify

Required automated checks: all course assets resolve; all questions score correctly; zero and full score boundaries; first/latest attempts; missing-input recovery; exact response export; completion distinct from passing; reflow at narrow width; SCORM init/set/commit/finish against a contract harness; package launch path and all manifest files exist; xAPI browser events reach real local SQL LRS and can be retrieved by exact ID. Failures block the affected claim until repaired and rerun.

Required manual gates: independent subject-matter review, full keyboard route, NVDA/VoiceOver, 200% text and 400% zoom, Firefox/Safari, representative learner pilot, actual Moodle import/launch/resume/score/status, and deployment security/backup checks. Do not mark these passed from code inspection or automated smoke tests.

## 5. Implement

Public static previews are demonstration mode and collect no learner records. SCORM mode uses the host LMS. Local xAPI mode requires an explicit lab launch and synthetic identity; never expose the loopback lab gateway or LRS secrets publicly. GitHub stores code and static previews, not a running database. A production Moodle/LRS service requires a separate runtime, HTTPS, identity binding and operational ownership.

Publish a release candidate with its limitations visible. Call it production-ready only after the manual and runtime gates pass. Never present a self-review as certification or a local event receipt as authenticated learner reporting.

## 6. Evaluate and revise

Collect pilot task success, item reasoning, navigation problems and independently scored work. Review items with unexpected distractor patterns. Check workplace transfer using a later work sample and agreed criteria. Do not fabricate learner results, effectiveness metrics, brand approvals or SME sign-off. Update source, version, change log, test evidence and package together.

## Data contract

No free text, real names, email addresses or customer data in xAPI events. Local actors are random synthetic accounts. Event IDs remain stable across retries; delivery status changes only on an acknowledged store. The browser queue is in memory, so closing the tab can lose pending events. SCORM compact resume excludes writing; the player explains that the writing activity must be repeated after relaunch. First/latest results remain separate. SCORM 1.2 lesson_status is completed for participation, while the score conveys check performance; pass/fail is a separate xAPI event in lab mode. Never run both modes simultaneously.

## Release record

For each repository retain: source references/date; ADDIE record; storyboard/script; brand/asset provenance; version/hash; package; functional report; known gaps. Source and published preview are public; learner records and runtime credentials are never committed.
