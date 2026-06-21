# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->
I asked for it to identify and fix the problems with the code.

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->
1. Reviewing the app and logic files for bugs first.
2. Running the test suite to confirm broken behavior and catch failing expectations.
3. Pytest isn’t on PATH; switching to Python module execution to validate the code.
4. Inspecting references and package context to map bugs and ensure no hidden dependency issues.
5. Checking the project instructions and intended refactor so the bug fixes align with requirements.
6. Found multiple logic and state bugs, including wrong hint direction, broken new-game reset, and unimplemented test functions. Applying fixes now.
7. I’ve refactored app logic; now validating the updated code and completing
8. Updating logic utility functions to match the application flow and passing tests.
9. Great, logic functions are now implemented. Running tests to confirm the fix.

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->
I had to fix the code in logic_utils, the values and parameters were set incorrectly.
Same with the % 2 logic error in the update score function.
---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case|      Prompt Used        | AI-Suggested Test | Did It Pass? | Your Reasoning |
|----------|-------------------------|-------------------|--------------|----------------|
|Secret Num| Test valid secret num.  | Test if in bounds | Yes          |Secret in bounds|
|Hint      | Test if hint correct.   | Input test val    | Yes          |Accurate read   |
|UI Range  | Test if UI correct.     | Start game and see| Yes          |UI correct      |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
Read through this code file and identify any logic problems.
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
logic_utils.py had NotImplementedError stubs, so tests could not pass.
app.py used wrong hint logic: "Too High" returned "Go HIGHER!" and vice versa.
The secret number reset incorrectly on submit and new game due to session state handling.
The UI range text always showed 1 to 100 instead of the current difficulty range.
The New Game button reset secret range incorrectly to 1-100 instead of difficulty-specific bounds.
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->
Found and fixed the following issues:

Go Higher and Go Lower logic was fixed.
Resets secret number correctly.
Showed proper difficulty range for each difficulty.
Changed bounds to proper difficulty-based bounds.

Files changed:
app.py
logic_utils.py
---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->
I asked both models to analyze the code, find logic errors, and resolve them.

| | Model A | Model B |
|-|---------|---------|
| **Model name** | Codex | Claude Sonnet 4.6|
| **Response summary** | Offers very comprehensive responses and fixes most things. | Does a very detailed analysis, fixes all known issues, and returns simple answers to errors.|
| **More Pythonic?** | Understands Python well. | Extremely proficient in Python. |
| **Clearer explanation?** | Offers straightforward answers. | Claude definitely has a clearer response. |

**Which did you prefer and why?**

<!-- Your conclusion -->
Codex is good for small bug-fixing and logic assistance, but Claude is stronger.