# Workshop 1: First-Win Task Specs

This is the assigned task for the thirty-minute first win in the Workshop 1
live session. Pick **one variant** (A, B, or C) below.
All three are the same size and difficulty; they differ so that neighbours
work on different features.

The rules of the exercise (from the runbook):

- You may **not** type or edit code by hand. Direct the agent for everything.
- **Plan mode first.** Review the plan, correct at least one thing, then build.
- Approvals stay **on**. Read each command before you allow it.
- **Done** = the command works, the tests pass, the diff is read, and you can
  explain every line.

Each variant adds one new read-only reporting command to the CLI. None of them
change how expenses are stored. Follow the shape of the existing commands
(`add`, `list`, `delete`): a module in `expense_tracker/commands/`, listed in
`expense_tracker/commands/__init__.py`, exposing `add_parser` and `handle`.

---

## Variant A — `total`

Add a `total` command that prints the sum of all expenses, formatted as money.

- Optional `--category CATEGORY`: total only that category.
- If there are no matching expenses, print `$0.00`.
- Money stays in integer cents until the moment it is formatted for display.

**Example**

```
$ expense-tracker total
$62.50
$ expense-tracker total --category groceries
$12.50
```

**Verification:** a test that seeds a few expenses and asserts the printed
total, plus a test for the empty case and the `--category` filter.

---

## Variant B — `search`

Add a `search` command that prints every expense whose category or note
contains a given term (case-insensitive).

- Positional argument `term`.
- Output format matches `list`.
- If nothing matches, print `No expenses found.`

**Example**

```
$ expense-tracker search coffee
#3  2026-01-08       $4.20  food  (morning coffee)
```

**Verification:** a test that seeds expenses and asserts a match is found by
note and by category, plus a test for the no-match case.

---

## Variant C — `top`

Add a `top` command that prints the N largest expenses, biggest first.

- Optional `--limit N` (default 3).
- Fewer than N expenses: print all of them, still largest first.
- Output format matches `list`.

**Example**

```
$ expense-tracker top --limit 2
#2  2026-01-16      $40.00  transport
#1  2026-01-15      $12.50  groceries  (weekly shop)
```

**Verification:** a test that seeds expenses of different sizes and asserts the
order and the count, plus a test for `--limit` larger than the number of
expenses.

---

## When you finish early

Run the same task against a second model and start your token/model comparison
(see the token note). Then capture your baseline row on the metrics sheet:
your completion time, an estimate for a comparable task done by hand, and your
usage snapshot.

## How to Submit

Submit your completed first-win task by [opening a GitHub issue](https://github.com/A3copilotprogram/starter-expense-tracker/issues/new?template=exercise.yml) in this repository.

Before submitting, **make sure you have completed the definition of Done above**:
the command works, the tests pass, you have read the diff, and you can explain
your changes.

1. Push your completed implementation to your GitHub repository.
2. Create a new issue in this repo using the **Workshop Exercise Submission** template.
3. Use the issue title format `Exercise: First Win - Variant X`, replacing `X`
   with `A`, `B`, or `C`.
4. Fill in the issue fields:
   - **Description:** briefly state which variant you completed and summarize
     the command you added.
   - **GitHub Repo URL:** paste the link to the repo containing your
     implementation. If the repo is private, grant access to the instructor
     (`pibzion`) before submitting.
   - **Other (optional):** include anything useful for review, such as the test
     command you ran, notes about your agent/model comparison, or anything you
     want the reviewer to know.
5. Submit the issue.
