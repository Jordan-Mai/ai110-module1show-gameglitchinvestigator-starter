# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
Number guessing game that allows the user to attempt to guess numbers with multiple difficulty settings and earn points for every correct guess.

- [ ] Detail which bugs you found.
logic_utils.py had NotImplementedError stubs, so tests could not pass.
app.py used wrong hint logic: "Too High" returned "Go HIGHER!" and vice versa.
The secret number reset incorrectly on submit and new game due to session state handling.
The UI range text always showed 1 to 100 instead of the current difficulty range.
The New Game button reset secret range incorrectly to 1-100 instead of difficulty-specific bounds.

- [ ] Explain what fixes you applied.
Found and fixed the following issues:
Go Higher and Go Lower logic was fixed.
Resets secret number correctly.
Showed proper difficulty range for each difficulty.
Changed bounds to proper difficulty-based bounds.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Difficulties now set proper alotted attempts and number range.
2. Hints now accurately describe given positioning.
3. UI range text now shows proper difficulty range.
4. Reset button now properly resets secret number.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
========================================================================== test session starts ==========================================================================
platform win32 -- Python 3.14.4, pytest-9.1.0, pluggy-1.6.0
rootdir: C:\Users\mylev\OneDrive\Desktop\Game Glitch Investigator
plugins: anyio-4.14.0
collected 3 items                                                                                                                                                        

ai110-module1show-gameglitchinvestigator-starter\tests\test_game_logic.py ...                                                                                      [100%]

=========================================================================== 3 passed in 0.09s ===========================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
