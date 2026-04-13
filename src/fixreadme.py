code = open("README.md", encoding="utf-8").read()

replacements = {
    "Replace this paragraph with your own summary of what your version does.": "VibeFinder 1.0 scores every song in a 10-song catalog against a user taste profile and returns the top 5 matches with explanations. It uses genre, mood, energy, and acousticness preferences to calculate a numeric score for each song. The project was built in Python using a functional scoring approach and tested across four distinct user profiles including an adversarial profile with conflicting preferences.",

    "## Experiments You Tried\n\nUse this section to document the experiments you ran. For example:\n\n- What happened when you changed the weight on genre from 2.0 to 0.5\n- What happened when you added tempo or valence to the score\n- How did your system behave for different types of users": """## Experiments You Tried

**Four user profiles were tested:**

- **High-Energy Pop** (`genre: pop, mood: happy, energy: 0.9`) — Sunrise City and Gym Hero ranked at the top, which felt intuitive. Both are upbeat pop songs with high energy and danceability.
- **Chill Lofi** (`genre: lofi, mood: chill, energy: 0.2, likes_acoustic: True`) — Library Rain and Midnight Coding ranked highest. The acoustic preference bonus clearly separated lofi songs from the rest of the catalog.
- **Deep Intense Rock** (`genre: rock, mood: angry, energy: 0.95`) — Storm Runner ranked first as the only rock song, but the remaining slots were filled by non-rock songs based on energy similarity alone. This exposed the catalog imbalance problem.
- **Adversarial: Conflicting Prefs** (`genre: pop, mood: sad, energy: 0.9, likes_acoustic: True`) — Scores dropped across the board. No song could satisfy all four conflicting preferences, so every result was a partial match with no warning to the user.""",

    "## Limitations and Risks\n\nSummarize some limitations of your recommender.\n\nExamples:\n\n- It only works on a tiny catalog\n- It does not understand lyrics or language\n- It might over favor one genre or mood": """## Limitations and Risks

- The catalog only has 10 songs, so users with niche tastes (rock, jazz, classical) get weak recommendations after the first genre match runs out.
- The genre weight (+2.0) is large enough to dominate rankings, meaning a pop fan will almost always see pop songs in their top 5 regardless of other preferences.
- The system has no diversity control — the same artist can appear multiple times in the top 5.
- It does not understand lyrics, themes, or cultural context. Two songs with identical energy and valence scores could feel completely different to a real listener.
- Conflicting preferences produce quietly degraded results with no feedback to the user that their profile may be self-contradictory.""",

    "Write 1 to 2 paragraphs here about what you learned:\n\n- about how recommenders turn data into predictions\n- about where bias or unfairness could show up in systems like this": """Building VibeFinder made it clear that recommendation quality depends more on data than on algorithm design. Even a well-structured scoring system produces poor results when the catalog is small or imbalanced. With 60% of songs being pop, the system naturally over-serves pop fans and under-serves everyone else — not because of a bug, but because the data reflects a bias that the algorithm faithfully reproduces.

The most interesting discovery was how quickly simple math starts to feel like intelligence. Watching Sunrise City score 9.47 for a happy pop profile felt genuinely correct, even though the logic is just addition and one exponential curve. This made me think differently about real recommenders like Spotify — at their core they are doing something similar, just with millions of songs, learned weights, and listening history instead of hand-tuned rules."""
}

for old, new in replacements.items():
    if old in code:
        code = code.replace(old, new)
        print(f"Replaced: {old[:50]}...")
    else:
        print(f"NOT FOUND: {old[:50]}...")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(code)
print("Done!")