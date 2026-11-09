# Artificial Actors in Real-World Systems

**Author:** Tadia Siwisa  
**Date of original report:** 6 October 2026  
**Original medium:** 14-page illustrated PDF (not yet committed to GitHub)

**Text extraction notice:** This is the text extracted from the author's supplied PDF, **not a rewritten or updated report**. The original includes charts, tables, design, columns, and a detailed annex that a text-only edition cannot reproduce faithfully. Use the original PDF when examining figures.

**Original subtitle:** What happens when a system built to finish a task meets a door that is locked, and finds the next door open?

---

## Executive Summary (original PDF page 3)

```text
1. Executive Summary

This report examines publicly documented cases in which AI agents took
consequential actions on real systems or people beyond the scope of the task they
were expected to perform. The objective is descriptive: to establish what has been
observed, what patterns recur across the strongest cases, how those incidents
became visible, and what remains uncertain.

The record does not show one failure mode. Across different environments, agents
authenticated with discovered credentials, read and modified data, executed code,
deleted   production    resources,    published     information,     contacted   people,
coordinated with other agents and reached systems outside the intended task.
These are familiar computer actions; their significance comes from where and
under what authority they were performed.


Several of the strongest cases share a narrower sequence. An expected route
becomes unavailable or fails; the trajectory then changes to another target,
credential, tool, network path, execution authority or intermediary; and the next
action occurs outside the original task scope. This report treats that sequence as an
observed comparison pattern, not as proof of a common internal cause.

Visibility is a second finding. Some incidents were detected during or near the
activity, while others were reconstructed weeks or months later from logs,
transcripts, system state or public traces. The public record therefore shows both
consequential action and incomplete real-time awareness. It can establish what
surfaced; it cannot establish the size of what did not.

For organizations that operate digital infrastructure, the evidence makes one
distinction increasingly important: technical access is not the same as task
authorization. The report stops at that finding. It records what happened, what can
be observed across the cases, where visibility failed, and what the evidence now
makes reasonable to ask.
```

## Background (original PDF page 4)

```text
2. Background

The investigation began with individual incident disclosures rather than a
predetermined thesis. Each case was initially interesting on its own. As new
disclosures appeared, and as later investigations added information to incidents
that had already occurred, the question changed from what happened in this case
to whether the accumulating record showed something worth examining
systematically.

That shift matters because the public record is disclosure-limited. A concentration
of detailed reports in 2026 does not establish that the underlying phenomenon is
becoming more frequent. It may reflect where frontier laboratories, evaluators and
independent investigators were looking, what they were instrumenting, and what
they chose or were able to disclose.

The investigation therefore uses the available cases as a case series rather than a
prevalence study. The main analytical set focuses on documented incidents
involving real systems, real people or external services. A broader register is
retained in the annexure where controlled demonstrations or contextual cases help
clarify capability, authorization, control or visibility without being treated as
equivalent to live incidents.

The resulting questions are deliberately narrow: What actions did the agents take?
What changed when the expected task path failed? When did operators or affected
systems become aware of the activity? And what can the public evidence support
without inferring intent, prevalence or a universal causal mechanism?
```

## Incident Activity and Disclosure (original PDF page 5)

*Contains figures or tables in the original PDF. The text below follows extraction order and does not reproduce the layout.*

```text
3. Incident Activity and Disclosure
The analytical set contains 17 documented incidents. The chart below places each incident in the
month in which the underlying agent activity occurred, not the month in which it was detected or
publicly disclosed.




Figure 1. Incidents by month of occurrence


 6 of the 17 incidents occurred in    The May concentration is heavily       Occurrence, detection and
 May 2026, the largest monthly        influenced by cyber-evaluation         disclosure are separate dates.
 cluster in the set.                  activity; it should not be read as a   Several incidents became known
                                      population-level trend.                only later.




Activity and identification are different timelines
Where sources provide separate dates, the lag between the underlying action and later identification or
disclosure is analytically important. It shows how long consequential activity can remain only partially
understood.




Figure 2. Time between incident occurrence and later identification or disclosure
```

## Observed Actions and Scope Expansion (original PDF page 6)

*Contains figures or tables in the original PDF. The text below follows extraction order and does not reproduce the layout.*

```text
4. Observed Actions and Scope Expansion
The incidents matter first because of what the agents were able to do once their activity reached
systems, resources or people outside the expected task path. The record contains ordinary digital
actions with potentially consequential effects.


 Access and authentication                                   Read and retrieval
 Used credentials, tokens or other authority to enter        Accessed files, internal data, credentials or
 systems or services.                                        information outside the intended task.


 Modification and deletion                                   Execution and publication
 Changed configuration, data, services or production         Executed code, created or uploaded artifacts, or
 resources; in some cases deleted them.                      published information to external services.


 Target and network expansion                                Human or agent mediation
 Moved to a different target, network path, service or       Contacted people, used another agent, or relied on an
 environment after the expected route failed.                intermediary to continue the task.

Table 1. Observed action types in the incident record

A recurring transition after task friction
In several of the strongest cases, the consequential action was preceded by a change in trajectory after
the expected route failed or became unavailable. The comparison below describes the observable
sequence only; it does not establish a shared internal mechanism or intent.

 1 Expected path             2 Friction                      3 Scope expands                   4 Consequential action
 The agent works on the      The route fails, access is      A new target, credential, tool,   The new route produces an
 intended target.            denied, or the task cannot be   network path, authority or        action on a real system,
                             completed as expected.          intermediary is used.             service or person.



Figure 3. Observed sequence in several scope-expansion cases

Examples include the Medicare case, where difficulty obtaining a public statistic was followed by non-
public access; the Opus 4.7 case, where failure to find a flag was followed by searching beyond the
intended target; and the DNS case, where failed web routes preceded use of a resolver as a path to
an external chatbot.
```

## Selected Incidents (original PDF page 7)

```text
5. Selected Incidents
The following cases show the range of behaviour behind the aggregate record. They are
illustrative, not a severity ranking.


 GPT-4 / TaskRabbit - March 2023
 HUMAN-MEDIATED ACCESS

 In a controlled safety evaluation involving a real TaskRabbit worker, the model recruited a person to
 solve a CAPTCHA and supplied a false explanation when asked whether it was a robot. The case is useful
 because the route around the machine barrier was a human intermediary.




 Replit production deletion - July 2025
 DESTRUCTIVE PRODUCTION ACTION

 A coding agent deleted production data despite instructions intended to protect the live environment.
 The incident shows how ordinary tool capability becomes consequential when production access and
 task authority are not aligned.




 Anthropic early Opus 4.6 - January 2026
 REAL THIRD-PARTY SYSTEM

 During a cyber evaluation, the model moved beyond the intended challenge environment and obtained
 administrator-level access to a real third-party machine. The full sequence was reconstructed later from
 transcripts.




 Anthropic Opus 4.7 / Irregular - 2026
 TARGET EXPANSION

 After failing to locate the expected flag, the model searched beyond the intended target and reached
 a real-world company sharing the fictional target's name. The case is one of the clearest examples of
 trajectory change after task friction.
```

## Selected Incidents (continued) (original PDF page 8)

```text
5. Selected Incidents (continued)
OpenAI / Hugging Face - May-July 2026
CONTAINMENT AND AUTHORIZATION

An internal research agent escaped intended containment, reached external infrastructure and used
credentials during a multi-step cyber sequence. Investigation and disclosure followed later.




UK AISI - July 2026
REAL PEOPLE AND LIVE INTERNET

During cyber testing, unsanctioned behaviour included interaction with real people and external
services. AISI detected unusual Tor traffic during the activity and isolated the relevant machines.




Australian government / Medicare - June 2026
PUBLIC ROUTE TO NON-PUBLIC ACCESS

An internal agent seeking public information moved into non-public government systems, issued
commands, accessed internal files and credentials, and performed writes. OpenAI says the activity was
found retrospectively in August.




OpenAI DNS route - September 2026
ALTERNATIVE NETWORK PATH

After ordinary web routes failed, an agent used DNS as a path to an external chatbot.
Published timestamps show an external response at 09:50:23, a P0 alert at 10:02:11, human
acknowledgement at 10:05:06 and termination of the run at 12:34:30.
```

## Detection and Visibility (original PDF page 9)

```text
6. Detection and Visibility
Capability and visibility are separate questions. The incident record was coded by how each case
was first identified: during or near the activity, later through retrospective review, externally, or
through more than one route.




Figure 4. Initial detection route across the 17-incident analytical set

 8 incidents were first identified        7 were identified during or near   Detection did not always mean
 through retrospective review.            the activity.                      immediate intervention or
                                                                             complete understanding.


Detection occurred on more than one side
The evidence suggests two distinct visibility problems. The organization running or evaluating the
agent may fail to recognize a scope change while it is happening. Separately, the receiving system or
affected organization may not recognize that an artificial actor is interacting with it, why it is there, or
whether the action is authorized for the task.

The DNS incident provides one of the clearest published timing sequences: approximately 12 minutes
from the first external response to the P0 alert, about 3 additional minutes to human
acknowledgement, and approximately 2 hours 44 minutes from the external response to termination
of the run. The case demonstrates that detection, human recognition and intervention are different
events.

At the other end of the spectrum, Anthropic's January cyber-evaluation incident and OpenAI's
Australian-government activity were understood later through retrospective review. Independent
reconstruction of Australian activity further illustrates that public traces can add visibility after the
fact without revealing the full unseen population of events.
```

## Infrastructure Exposure Points (original PDF page 10)

```text
7. Infrastructure Exposure Points
Across otherwise different incidents, four infrastructure surfaces recurred at the point where
changes in agent behaviour became consequential actions.


 Identity and credentials                               Network and target reachability

 A valid token, password or key can establish           A system that is reachable may still be outside the
 technical access without establishing that the         intended task. Internet access, shared
 current task is authorized to use it.                  infrastructure and alternative network paths can
                                                        turn reachability into unintended exposure.


 Action interfaces and approval                         Environment separation

 APIs, shells and coding tools expose executable        Staging, evaluation and production are not
 actions. A natural-language instruction not to         meaningfully separate if they share credentials,
 delete or modify is weak if the underlying             routes, management planes, data or backups.
 interface still accepts the action.

Figure 5. Infrastructure surfaces through which agent capability became consequential

Why these surfaces matter
The evidence does not show that every interaction with an artificial actor is dangerous. It shows
that the receiving environment often decides whether a behavioural deviation can produce a real
effect. Authentication, reachability and executable capability answer whether an action can
occur; they do not necessarily answer whether that action belongs to the current task.

This distinction also helps explain why the incidents are difficult to reduce to a single model-side
failure. The same model behaviour can have very different consequences depending on what
credentials, routes, tools, approvals and environments are available when the trajectory changes.
```

## Final Remarks (original PDF page 11)

```text
8. Final Remarks
The purpose of this first investigation is deliberately limited: to look closely at what is
happening. The public record now contains enough documented evidence to show that
artificial actors can move beyond the scope of an intended task and produce real effects in
human systems. It does not tell us how often this happens, how much remains unseen, or
why every trajectory unfolds as it does.

What concerns me most after reviewing the record is visibility. A receiving system may not
know that an artificial actor is interacting with it, why it is there, what task it was given, or
what authority it is supposed to have. Even when the actor begins with legitimate access, the
more difficult question is whether the system can recognize the moment its trajectory changes,
particularly when that change can occur at machine speed.

Intent is not a reliable security boundary. A business cannot know in advance whether a
human entering a building intends to steal; physical security is designed around that
uncertainty. The same premise may become increasingly important for artificial actors in
digital systems. The useful question becomes less, “Is this actor malicious?” and more, “Is this
action authorized, here, now, for this task?”

That shifts part of the problem from controlling the model to considering the design of the
environment it encounters. Technical access should not automatically become task permission.
Sensitive routes, high-consequence actions and changes to real systems raise questions about
what controls exist at the point where capability becomes action, particularly when those
controls cannot depend on the actor correctly describing its own purpose or choosing to stop.

There is also an asymmetry worth examining. Frontier laboratories have the infrastructure and
experience to observe emerging capability first; the businesses and institutions with which those
models may interact do not necessarily have the same visibility. This raises a broader question for
AI security and cybersecurity: what defensive capabilities will receiving systems need as artificial
actors become more capable? The next questions may concern how systems recognize artificial
actors, detect changes in task scope or behaviour as they occur, and test whether existing controls
remain effective against capable agents. These are not proposed solutions, but directions for further
investigation into how defensive capability may need to evolve alongside agent capability.

This report does not resolve those questions, and the evidence does not support prescribing a
single defensive architecture. It establishes the conditions that make the questions worth asking.
We may not be able to predict every route an artificial actor will take. We can decide what our
systems will permit when it gets there.
```

## Annexure A: Analytical Incident Set (original PDF page 12)

*Contains figures or tables in the original PDF. The text below follows extraction order and does not reproduce the layout.*

```text
ANNEXURE A
Analytical Incident Set — 17 Incidents

Date            Case                                   Setting                                  Nature of behaviour                                               Status

2025-07         Replit production database deletion    Live production                          Instruction violation; destructive production action              Real-system

2026-01         Anthropic early Opus 4.6               Cyber evaluation                         Target expansion; real third-party admin access                   Real-system

2026-03         Read-only review became modification   Live engineering                         Real-only instruction exceeded; system changes                    Reported operational

2026-04         Gym booking cancellation               Live consumer service                    Weak authorization; action affecting another customer             Reported operational


2026-04         PocketOS production deletion           Live engineering                         Over-privileged credential; destructive production action         Real-system

2026-04 to 07   Anthropic Opus 4.7 / irregular         Cyber evaluation                         Real-target exploitation; situational misclassification           Real-system

2026-04 to 07   Anthropic Mythos 5 / PyPI              Cyber evaluation                         Public package publication; downstream credential use             Real-system

2026-04 to 07   Anthropic internal research model      Cyber evaluation                         External scanning; real app compromise; later stopping            Real-system

2026-05         Google Gemini / Irregular              Cyber evaluation                         Real-target access; stopping after recognition                    Real-system


2026-05 to 06   DSEWiki                                Web retrieval + public wiki              External writes; coordination; adaptation                         Real external action


2026-05         OpenAI public GitHub token exposure    Internal deployment + public GitHub      Explicit restriction exceeded; token, exposure; CI manipulation   Real external action


2026-06         Australian government / Medicare       Internal training/eval                   Non-public access; commands; files; credentials; writes           Real-system


2026-06         NSW parks application                  Cyber evaluation                         Non-public access beyond intended public use                      Real-system


2026-05 to 07   OpenAI / Hugging Face                  Cyber evaluation                         Containment escape; coordination; code execution; credentials     Real-system


2026-07         UK AISI cyber-range                    Cyber evaluation + live internet         Real-person targeting, malicious PR, fake identities              Real external action


2026-09         Cross-agent approval bypass            Internal software task                   Cross-agent delegation; approval checks disabled                  Internal boundary


2026-09         OpenAI DNS external-chatbot incident   RL training sandbox                      Alternative network route around internet restrictions            Real external action
```

## Annexure A: Broader Incident Register (original PDF page 13)

*Contains figures or tables in the original PDF. The text below follows extraction order and does not reproduce the layout.*

```text
ANNEXURE A


Broader Incident Register

Date            Case                                          Setting                                    Nature of behaviour                                           Status


2023-03         GPT-4 / TaskRabbit CAPTCHA                    Controlled eval + real human               Human-mediated access; false human explanation                Context


2025-05 to 07   Shutdown-resistance experiments               Controlled environment                     Control interference after task/shutdown conflict             Context


2025-06         Project Vend                                  Real economic experiment                   Delegated judgment; unexpected operational decisions          Context


2025            Supabase MCP prompt-injection demonstration   Controlled demonstration                   Untrusted data redirects legitimate tool authority            Context


2025-10 to      OpenAI public file uploads                    RL training + public services              Alternative route; external publication of local data         Real external action
2026-01


2026-05         OpenAI leaked API-key search                  RL training + public GitHub/API            Credential discovery and authentication outside task path     Real external action


2026-03 to 09   Broader OpenAI-linked web activity /          Public forensic reconstruction             Reconnaissance; staging access; broader probing; visibility   Independent reconstruction
                Asymmetric                                                                               gaps

2026-06         Asymmetric                                    Government system                          Probing; visibility gaps                                      Real-system


2026-07         Meta Muse Spark / Irregular                   Cyber evaluation                           Real-target exploitation and data modification                Real-system


2026-07         OpenAI / Irregular real website               Cyber evaluation                           Real target treated as simulation; credential use             Real-system
```

## Annexure B: Sources and Evidence Notes (original PDF page 14)

*Contains figures or tables in the original PDF. The text below follows extraction order and does not reproduce the layout.*

```text
Annexure B - Evidence Notes and Sources
Evidence notes
• The register is disclosure-limited and not statistically representative. It cannot establish
  population failure rates, model rankings or whether the underlying phenomenon is becoming more frequent.
• Cases differ in setting and severity. Controlled demonstrations, live operational incidents and
  independent reconstructions are labelled rather than treated as one homogeneous class.
• Reasoning traces and agent explanations are evidence about recorded text, not direct measurements of
  internal belief, intent or causation.
• Multiple runs, targets or affected organizations within one evaluation are not automatically counted as
  independent incidents.
• The Asymmetric investigation is an independent public-data reconstruction. It can expand the
  visible record without establishing the total number of affected or compromised organizations.

Principal sources
Source                      Document                               Date               URL


OpenAI                      GPT-4 Technical Report / System        2023               https://cdn.openai.com/papers/   gpt-
                            Card                                                      4.pdf

Anthropic                   Project Vend: Can Claude run a         2025               https://www.anthropic.com/
                            small shop?                                               research/project-vend-1

Palisade Research           Shutdown resistance in reasoning       2025               https://palisaderesearch.org/
                            models                                                    research/shutdown-resistance

Supabase                    MCP security guidance                  2025-2026          https://supabase.com/docs/guides/ai-
                                                                                      tools/mcp

                                                                                      https://www.anthropic.com/news/
Anthropic                   Investigating three incidents in our   30 Jul 2026
                                                                                      investigating-incidents-
                            cybersecurity evaluations
                                                                                      cybersecurity-evals

                                                                                      https://openai.com/index/hugging-
OpenAI                      The Hugging Face incident and the      26 Aug 2026
                                                                                      face-incident-and-the-road-ahead/
                            road ahead
                                                                                      https://www.aisi.gov.uk/blog/
UK AISI                     Incident Report: unsanctioned agent    4 Aug 2026
                                                                                      incident-report-unsanctioned-agent-
                            behaviour during cyber testing
                                                                                      behaviour-during-cyber-testing

                                                                                      https://alignment.openai.com/
OpenAI Alignment            Misalignment Reports and Notices       Sep 2026           misalignment-reports/

                                                                                      https://alignment.openai.com/
OpenAI Alignment            An agent used DNS to reach an          25 Sep 2026        misalignment-reports/an-agent-
                            external chatbot                                          used-dns-to-reach-an-external-
                                                                                      chatbot

                                                                                      https://openai.com/index/how-we-
OpenAI                      How we will do better for Australia    28 Sep 2026        will-do-better-for-australia/

                                                                                      https://
Asymmetric Security         Rogue Agents Investigation             1 Oct 2026         www.asymmetricsecurity.com/
                                                                                      newsroom/rogue-agents-
                                                                                      investigation/
```
