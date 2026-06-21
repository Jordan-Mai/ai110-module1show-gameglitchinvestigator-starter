# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The game looked normal, but had a lot of mechanic errors like incorrect range based on difficulty and conflicting hints.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Reset | Game resets secret| Incorrect reset | Number is not in bounds|
| Answer| Proper hint       | Reversed hint   | Hint is incorrect      |
| Score | Minus when wrong  | Even # = +5 pts | Point calculation wrong|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

For this project I used ChatGPT Codex and Claude Sonnect 6.5.
+ The AI suggested logic fixes on the hints reversing the existing logic.
- AI did not find any issue with logic-utils scoring system, even though there was a large one messing up the difficulty system.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided that a bug was really fixed after running the website and testing it physically.
One manual test I ran was just loading up the website and recreating the bugs to see if they occur again.
AI helped design and understand my tests by describing to me what an outcome my say about the code.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns are basically retests and the session state is like a notepad where you store results after a test.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit from this project I want to reuse is checking and testing AI fixes to see if they are actually applied.
Next time I work with AI on a coding task, I'll provide a more specific prompt that covers all the things I want it to do.
This project altered the way I perceive AI accuracy on correcting coding logic.