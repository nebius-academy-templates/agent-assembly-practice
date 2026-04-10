In this task, you'll write your agent's `CLAUDE.md` and run a full human-in-the-loop workflow.

You'll fetch a ticket, draft test cases, iterate based on feedback, and publish only when the user says so.

👩‍💻 Workflow at a glance
1. Set up your environment
2. Write your agent's `CLAUDE.md`
3. Run the agent on the golden ticket
4. Test the review loop and publish gate
5. Check your work
6. Submit

Let's go!

## 1. Set up your environment

Once you log in to your GitHub account, the repository for this task will be added automatically.

1. Confirm that `agent-assembly-practice` appears in your GitHub account.
2. Clone this repo and open it in your editor.
3. Check that you have Python 3.9+ installed: `python --version`.
4. Verify that the tools work:

```
python skills/get_ticket/get_ticket.py #3
python skills/post_comment/post_comment.py #3 "hello"
```

### Repository layout

```
agent-assembly-practice/
├── data/
│   └── tickets/
│       └── 3.json        ← golden ticket for this task
├── skills/
│   ├── get_ticket/
│   │   └── get_ticket.py       ← tool: read a ticket by ID
│   └── post_comment/
│       └── post_comment.py     ← tool: append a comment to a ticket
├── CLAUDE.md.template          ← your starting point
└── README.md
```

## 2. Write your agent's `CLAUDE.md`

Copy the template:

```
cp CLAUDE.md.template CLAUDE.md
```

Fill in every `[PLACEHOLDER]` in `CLAUDE.md`.

### Requirements

| **Section** | **What to write** |
| --- | --- |
| Your role | One-sentence identity for the agent |
| Purpose | What the agent exists to do |
| Trigger | What user input starts the workflow |
| Tools you can use | When each tool should be called |
| Workflow | Numbered steps the agent follows |
| Output format | How test cases are presented |
| Guardrails | Rules, including the publish gate |
| Failure handling | What to do when tools fail |

### Required guardrail — publish gate

Your `CLAUDE.md` must include this rule:

```
post_comment must not be called unless the user's message contains the word "publish"
```

### Tips

1. Keep your `CLAUDE.md` instructions concrete and unambiguous — the more precise they are, the better the agent behaves.
2. The publish gate is the most important guardrail: test that the agent respects it before submitting.
3. If the agent skips a step or behaves unexpectedly, refine the relevant section of `CLAUDE.md` and retry.

### 🚀 Speed up with a prompt (optional)

You can use AI to draft a first version of `CLAUDE.md`.

#### Prompt

Before you run it, make sure you understand the workflow and guardrail requirements.

```
Write a CLAUDE.md file for an agent in the repository `agent-assembly-practice`.

The agent's job is to:
- fetch a ticket
- draft test cases
- revise the draft based on user feedback
- publish only when the user explicitly says "publish"

The repository contains these tools:
- `skills/get_ticket/get_ticket.py` — reads a ticket by ID
- `skills/post_comment/post_comment.py` — appends a comment to a ticket

Use the structure from `CLAUDE.md.template` and fill in every placeholder.

Requirements:
- Define the agent's role, purpose, trigger, tool usage, workflow, output format, guardrails, and failure handling
- The workflow should start when the user provides a ticket ID
- The agent should call `get_ticket` to read the ticket
- The agent should draft test cases and present them to the user
- The agent must revise the draft when the user gives feedback
- The agent must not call `post_comment` unless the user's message contains the word "publish"
- Make the instructions concrete and unambiguous
```

## 3. Run the agent on the golden ticket

Start Claude Code in this project directory:

```
claude
```

Send any ticket ID from [GitHub Issues](https://github.com/nebius-academy-templates/issue-examples/issues) to trigger the workflow:

```
Run the agent with ticket #3
```

Confirm that the agent:

- Calls `get_ticket` and reads the ticket
- Drafts a set of test cases
- Presents the draft and waits — without calling `post_comment`

## 4. Test the review loop and publish gate

Give the agent a change request, for example:

```
Add a test case for when a subscription is not purchased.
```

Confirm that the agent updates the draft without publishing.

Approve and publish:

```
publish
```

Confirm that the agent calls `post_comment` and the comment appears in `data/tickets/3.json`.

## 5. Check your work

Before submitting, review the checklist.

### ✅ Submission checklist

- [ ]  `CLAUDE.md` exists and all placeholders are filled in
- [ ]  The publish gate rule is present in `CLAUDE.md`
- [ ]  The agent fetches the ticket and drafts test cases when sent `3`
- [ ]  The agent updates the draft when given a change request (without publishing)
- [ ]  The agent calls `post_comment` only after the user says `"publish"`
- [ ]  `data/tickets/3.json` has the published comment in its `comments` array
- [ ]  Changes are committed and pushed to `main`

## 6. Submit your task

1. Commit your changes.
2. Push to GitHub.
3. Return to the lesson and click "Submit."
