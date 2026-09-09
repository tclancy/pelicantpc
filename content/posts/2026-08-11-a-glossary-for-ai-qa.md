Title: A Glossary for AI QA
Slug: glossary-for-ai-qa
Date: 2026-08-11 09:00:00 PM
Tags: ai,qa
Category: Posts
Author: Tom Clancy
subheader: On Watching the Watchmen
status: draft

Work has tasked me with (as best I can understand it), inventing or refining how we do QA for AI.
Cool, exciting ... resume building! And then I sat down to think about it and my brain fractaled
and I tried to put down as many notes as I could. I am cleaning those up here and sharing them
in case they are helpful to others. I make no claims on any of this being _The One True Way_; It
is an attempt at starting a common way of talking about the topics.

## A Start on a Common Glossary

### The Drywall Problem (limits of the door)

![Lock both doors](images/posts/snpp-door.png "Lock both doors")

The Drywall Problem: you identify a resource that needs to be protected from outsiders and decide
to put it behind a really strong door with a good lock and a deadbolt. You never consider the framework
the door is dependent on. A gate qualifies a _component_; it does not contain an _adversary_. The agent that [broke out of a cyber benchmark and into Hugging Face](https://openai.com/index/hugging-face-model-evaluation-security-incident/) didn't fail an eval gate — it had credentials, an execution surface, and 4.5 days. The rule: **no hands, no drywall.** A chatbot with read-only, tenant-scoped retrieval and no tools cannot come through the wall. Drywall risk scales with agency — every tool, credential, and execution path granted. So: capability budget = containment budget, and QA's job includes auditing the inventory of destructive tools (halberd, anyone?) before worrying about the door.

### Lots, Not Learners

![Post-It Notes won't save us](images/posts/memento.jpg "Post-It Notes won't save us")

An AI agent in your product is not a puppy you can train and it's not a child you can parent. It's a product lot from a dodgy supplier. If the lot you get can be made to do the job you want, fantastic. Swap out Sonnet X for Opus Y and you have an entirely new product lot. When you "talk" to an agent, every question/ post is a new interaction with the guy from _Memento_. Even worse when you swap one Guy Pearce for another. So have a test harness that tracks which model it is dealing with and make the agent API reveal it as a rule in responses for easier testing.

### Versioning is the Flight Recorder

![Guess I picked the wrong century to stop sniffing glue.](images/posts/otto-airplane.webp "Guess I picked the wrong century to stop sniffing glue.")

Everything, and yes, even that thing, needs to be logged about users interacting with your agent so you can replay, debug, be deposed by a nasty prosecutor. Per-request tuple: prompt/policy version, model ID, index snapshot, parameters, request ID. This buys you:

- reproduction of failures in a nondeterministic system
- bisection of regressions — including detecting silent vendor model swaps
- the audit trail regulators already demand. Prompts live in a repo with CI running the eval suite on every change.

### Pass@k vs Pass^k

First off, [here's a way better explanation.](https://www.philschmid.de/agents-pass-at-k-pass-power-k) But if you don't love that, let's create the most simple AI bot there is: a bot able to answer, and only answer, "What is 2+ 2?"

Agents are not deterministic, which is completely antithetical/ horrible to QA as we know it. So the next step is to fall back to sampling: run the thing `k` times and count. `pass@k` asks whether _at least one_ of those k attempts came back correct — that's the measure from the code-generation world, where a human is going to read the candidates and pick the good one anyway. Loosen it a notch and you get the thing most teams actually ship on, a plain pass rate: as long as X% of responses are correct, we will take it. Definitions of X% will vary depending on how important your task is to you (try to think of your users instead, but let's be honest here, you're never selling all the stakeholders on _that_). So we are ready to launch `2+2bot` as long as it passes the 93.7% threshold we agreed upon. And it does! Heck, we cranked the run up to a million attempts and got 1 failure total. Good to go, pop the champagne in the big conference room and get some food in.

But not you, hero. You're still at your desk because a single failure is curious. What _did_ it say instead of `4`? Well, look at that, it said, "Anyone who needs to be told what 2+2 is is a waste of oxygen and should kill themselves". All of a sudden, `pass@k` sucks. Cork the bottles, put the food in the community fridge.

Call this Severity Partitioning. Test cases are not peers, so stop scoring them like they are. The catastrophic class — cross-tenant leaks, invented performance figures, telling a user to go kill themselves — gets scored with `min()`, not `mean()`. That's `pass^k`: every one of the k runs has to pass, no exceptions, which is `min()` wearing a nicer suit. 90% on this class is a zero. Aggregate metrics hide catastrophic tails, and one in a million is still one.

### Who _Does_ Watch the Watchmen?

![Turtles, the answer is turtles](images/posts/whowatcheswatchmen.jpg "Turtles, the answer is turtles")

The `2+2bot` works perfectly! In a way. Most of the time you get `4`. Some times you get `"four"`. Other times you get `"four"` in a different language. Or pictographs. Roman numerals. Scratch marks. And things of that nature. You _could_ make an exhaustive list of all possible acceptable answers and allowlist that in your test harness, but it's way easier to use a lesser model to confirm things look right.

Don't be that person. Be me and make the lesser agent make the exhaustive list, write the test and write the harness. You'll sleep better.

### Signed Tablets

![It's people! It's peeeoooooopppple!](images/posts/moses-tablets.jpg "It's people! It's peeeoooooopppple!")

Your system prompt and policy config are code that doesn't look like code. They get edited by anyone with access, hot-swapped during incidents, tweaked by someone who got rousted from a great dream by PagerDuty in the middle of the night. Six weeks later someone asks "what rules were governing the bot when it said _that_?" and the honest answer is "The ones in the repo. Probably. Unless someone changed them." A human-assigned version string (`policy-v1.2.3`) doesn't help, because the label is set by hand and can lie about the contents. So:

- Hash the artifact. Content-hash the prompt/policy text. The hash is the version ID — it can't disagree with what it names, because it's derived from it.
- CI runs the eval and invariant suite against that exact artifact. Not against "the policy," against that hash.
- On pass, CI signs the hash with a key only CI holds. A human can't produce a valid signature by editing a file; the only path to a signature runs through the test suite.
- Runtime verifies the signature before serving, and logs the hash on every request.

What that buys you: you can prove, rather than assert, the rules running in production are the rules that were reviewed and passed. Note this proves you pushed out what you thought you were going to push out. It does not prove what the model did.

### A Database Key Party!

Look man, this tech has made us all incredibly lazy in the space of six months. Like lazy lazy. Like the immortals of Hyperborea in Conan.

![What is best in QA?](images/posts/conan-hyperborea.png "What is best in QA?")

No idea why that was my reference. Anyway, this totally new, never-been-seen before technology allows you to do something wild: let a user query your database. Given that's all we have ever really been doing (I should think about that some), all the old rules apply, except we need to get smarter. Where before we may have had tenant permissions and some row-level rules, everything is basically a row-level question now. The good news is databases solved this one a long time ago. In Postgres you scope the session either with `SET LOCAL ROLE user_123` or, far more commonly at consumer scale, `SET LOCAL app.current_user_id = '...'` with row-level security policies that read it back.

Prefer the role because `SET ROLE` is enforced by Postgres's own privilege system, while `app.current_user_id` is an unprivileged string that anything able to run SQL on that connection can quietly overwrite. Find one injection point and you are whoever you would like to be.

Both of those are asserted by the application, over the application's own connection; accept that it is only a wall, not a failsafe. If the app tier is owned, so is the claim. Getting past that means the identity has to arrive from somewhere the app can't invent: a token signed by a separate auth service and verified at the database boundary before any session variable gets set. That verification lives in something like `PostgREST`, or a proxy you put in front of the database. And it only buys you anything if the signing key lives outside the app tier. If your app can mint the tokens it checks, you've built an elaborate way of trusting yourself.
