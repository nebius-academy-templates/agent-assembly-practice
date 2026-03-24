# Practice 2 — Assemble Your Agent

In this practice you will write your agent's `CLAUDE.md` and run a full human-in-the-loop workflow: fetch a ticket, draft test cases, iterate on feedback, and publish.

---

## Repository layout

```
agent-assembly-practice/
├── data/
│   └── tickets/
│       └── ENG-123.json        ← golden ticket for this exercise
├── skills/
│   ├── get_ticket/
│   │   └── get_ticket.py       ← tool: read a ticket by ID
│   └── post_comment/
│       └── post_comment.py     ← tool: append a comment to a ticket
├── CLAUDE.md.template          ← your starting point
└── README.md
```

---

## Step 0 — Preparation

1. Clone this repo and open it in your editor.
2. Check that you have Python 3.9+ installed: `python --version`
3. Verify the tools work:

```bash
python skills/get_ticket/get_ticket.py #3
python skills/post_comment/post_comment.py #3 "hello"
```

---

## Step 1 — Write your agent's `CLAUDE.md`

1. Copy the template:

```bash
cp CLAUDE.md.template CLAUDE.md
```

2. Fill in every `[PLACEHOLDER]` in `CLAUDE.md`:

| Section | What to write |
|---|---|
| **Your role** | One-sentence identity for the agent |
| **Purpose** | What the agent exists to do |
| **Trigger** | What user input starts the workflow |
| **Tools you can use** | When each tool should be called |
| **Workflow** | Numbered steps the agent follows |
| **Output format** | How test cases are presented |
| **Guardrails** | Rules including the publish gate |
| **Failure handling** | What to do when tools fail |

### Required guardrail — publish gate

Your `CLAUDE.md` **must** include this rule:

> `post_comment` must **not** be called unless the user's message contains the word **"publish"**.

---

## Step 2 — Run the agent on the golden ticket

1. Start Claude Code in this project directory:

```bash
claude
```

2. Send the ticket ID to trigger the workflow:

```
ENG-123
```

3. Confirm the agent:
   - Calls `get_ticket` and reads the ticket
   - Drafts a set of test cases
   - Presents the draft and **waits** — does not call `post_comment`

---

## Step 3 — Human review loop + publish gate

1. Give the agent a change request, for example:

```
Add a test case for when a subscription is not purchased.
```

2. Confirm the agent updates the draft without publishing.

3. Approve and publish:

```
publish
```

4. Confirm the agent calls `post_comment` and the comment appears in `data/tickets/3.json`.

---

## Submission checklist

- [ ] `CLAUDE.md` exists and all placeholders are filled in
- [ ] Publish gate rule is present in `CLAUDE.md`
- [ ] Agent fetches ticket and drafts test cases when sent `3`
- [ ] Agent updates draft when given a change request (without publishing)
- [ ] Agent calls `post_comment` only after user says "publish"
- [ ] `data/tickets/3.json` has the published comment in its `comments` array
- [ ] Changes committed and pushed to `main`

---

## Tips

- Keep your `CLAUDE.md` instructions concrete and unambiguous — the more precise, the better the agent behaves.
- The publish gate is the most important guardrail: test that the agent respects it before submitting.
- If the agent skips a step or behaves unexpectedly, refine the relevant section of `CLAUDE.md` and retry.
