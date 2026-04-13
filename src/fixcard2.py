code = '''# Model Card: Music Recommender Simulation

## 1. Model Name
**VibeFinder 1.0** — a rule-based music recommender that matches songs to user taste profiles.

---

## 2. Goal / Task
VibeFinder suggests songs from a small catalog based on what a user tells us they like. Given preferences like genre, mood, energy level, and whether they enjoy acoustic music, the system scores every song and returns the top 5 best matches with an explanation for each pick.

---

## 3. Data Used
The catalog contains 10 songs. Each song has the following features: title, artist, genre, mood, energy (0.0-1.0), tempo in BPM, valence, danceability, and acousticness. Genres represented include pop, lofi, and rock. Moods include happy, chill, and angry. The dataset is hand-curated for classroom use and is too small and genre-imbalanced to represent real musical diversity. Many common genres like hip-hop, jazz, classical, and country are missing entirely.

---

## 4. Algorithm Summary
Every song gets a numeric score based on how well it matches the user profile. Genre match adds 2 points. Mood match adds 1 point. Energy similarity adds up to 3 points using a smooth curve that rewards songs close to the user's target energy and penalizes songs far away. Acousticness preference adds up to 2 points depending on whether the user likes or dislikes acoustic sounds. Bonus points are added for danceable songs when the user wants high energy, and for songs with a positive, uplifting feel. All scores are added together and songs are ranked highest to lowest.

---

## 5. Observed Behavior / Biases
The genre weight (+2.0) is large relative to the total possible score, which means genre dominates the ranking whenever there are multiple songs in the same genre. In testing, the pop genre appeared so frequently in the catalog that pop-preferring users always got strong matches while rock-preferring users ran out of genre matches after one song and fell back on energy alone. The adversarial profile test (high energy + acoustic + sad mood) showed that conflicting preferences produce noticeably weaker recommendations with no warning to the user. The system also has no diversity control, so the same artist can appear multiple times in the top 5.

---

## 6. Evaluation Process
Four user profiles were tested: High-Energy Pop, Chill Lofi, Deep Intense Rock, and an adversarial profile with intentionally conflicting preferences. Results were compared against musical intuition to check whether the rankings felt reasonable. A weight shift experiment was also considered to test whether doubling energy weight and halving genre weight would change the rankings meaningfully. The Chill Lofi and High-Energy Pop profiles produced the most intuitive results. The Rock profile revealed the catalog imbalance problem most clearly.

---

## 7. Intended Use and Non-Intended Use
**Intended use:** Classroom demonstration of how rule-based recommendation scoring works. Useful for understanding how weights, features, and ranking combine to produce suggestions.

**Not intended for:** Real music streaming or production use. The catalog is too small, the weights are hand-tuned rather than learned, and the system has no user history, feedback loop, or diversity controls. It should not be used to make decisions about what music people actually want to hear outside a learning context.

---

## 8. Ideas for Improvement
- Expand the catalog to at least 50-100 songs with better genre and mood diversity so users outside pop have meaningful options.
- Replace hard-coded weights with learned weights based on user feedback, so the system improves over time instead of relying on guesses.
- Add a diversity penalty so the same artist cannot appear more than once in the top 5, and so results feel more varied.

---

## 9. Personal Reflection
The biggest learning moment in this project was realizing how much the quality of recommendations depends on the data, not just the algorithm. Even with a well-designed scoring system, a 10-song catalog with 60% pop songs will always over-serve pop fans and under-serve everyone else. AI tools helped speed up the implementation significantly, but I had to double-check the output every step of the way because the generated code sometimes mixed up variables or produced syntactically broken files. The most surprising thing was how quickly a few simple math rules started to feel like real recommendations. Seeing Sunrise City score 9.47 for a happy pop profile felt genuinely correct, even though the logic behind it is just addition and one exponential curve. If I extended this project I would add a feedback mechanism where users can thumbs up or down results, and use that signal to adjust the weights automatically over time.
'''

with open("model_card.md", "w", encoding="utf-8") as f:
    f.write(code)
print("Done!")