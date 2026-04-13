# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

VibeFinder 1.0 scores every song in a 10-song catalog against a user taste profile and returns the top 5 matches with explanations. It uses genre, mood, energy, and acousticness preferences to calculate a numeric score for each song. The project was built in Python using a functional scoring approach and tested across four distinct user profiles including an adversarial profile with conflicting preferences.

---

## How The System Works

This is a **content-based music recommender** that suggests songs similar to what a user likes, based on song attributes from our dataset. It doesn't use other users' data—just the characteristics of the songs themselves.

### Song Features
Each song is represented by:
- **Categorical**: genre (e.g., pop, rock, lofi) and mood (e.g., happy, intense, chill)
- **Numerical (0-1 scale)**: energy, valence, danceability, acousticness
- **Continuous**: tempo_bpm (beats per minute)

### User Profile
The user profile stores:
- Favorite genre and mood (exact match preferences)
- Target energy level (0-1)
- Acoustic preference (boolean)

### Scoring Algorithm Recipe

For each song, we calculate a total score out of ~9.5 points:

| Component | Points | How It Works |
|-----------|--------|-------------|
| **Genre Match** | +2.0 | Exact match to favorite genre |
| **Mood Match** | +1.0 | Exact match to favorite mood |
| **Energy Similarity** | 0–3.0 | Gaussian curve: rewards closeness to target energy. Formula: `3.0 × exp(-(diff²) / (2 × 0.15²))` |
| **Acousticness Preference** | 0–2.0 | If user likes acoustic: +2.0 if acousticness > 0.6. Otherwise: +2.0 if acousticness < 0.4 |
| **Danceability Bonus** | +0.75 | +0.75 if target energy > 0.7 AND danceability > 0.7 |
| **Valence Bonus** | +0.75 | +0.75 if valence > 0.65 (uplifting/positive) |

**Ranking Rule**: Score all songs, sort descending, return top N (default: 5).

### Example Workflow
```
User Profile: {genre: "rock", mood: "intense", energy: 0.88, likes_acoustic: false}
  ↓
Score Song 1 "Storm Runner" (rock, intense, 0.91 energy) → 6.8 pts
Score Song 2 "Focus Flow" (lofi, focused, 0.40 energy) → 0.9 pts
  ↓
Rank by score
  ↓
Recommend top 5
```

### Expected Biases & Limitations

⚠️ **This system may over-prioritize genre**. A rock user will rarely see pop recommendations, even if a pop song has near-perfect energy/mood alignment.

⚠️ **It ignores diversity**. If a user likes "rock/intense," they'll get 5 similar rock songs, all with high energy—no exploration of adjacent genres.

⚠️ **Small catalog bias**. With only 10 songs (soon 18+), matching rare mood/genre combinations is unlikely. Real systems have millions of songs.

⚠️ **No lyrical or thematic understanding**. Two songs can have identical energy/valence but totally different themes (e.g., "Gym Hero" vs. "Night Drive Loop").

⚠️ **Exact mood/genre matching is brittle**. A song labeled "chill" vs. "relaxed" might be musically identical but score differently.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Example Output

When you run `python -m src.main`, the recommender generates personalized recommendations with scores and detailed explanations:

```
Top recommendations:

#1: Sunrise City by Neon Echo
Score: 8.30
Why:
  • Genre match: pop
  • Mood match: happy
  • Energy similarity: 2.97 (your target: 0.8, song: 0.82)
  • Non-acoustic preference matched: 0.18
  • High-energy danceability bonus
  • Positive/uplifting vibe bonus

#2: Gym Hero by Max Pulse
Score: 7.56
Why:
  • Genre match: pop
  • Energy similarity: 2.06 (your target: 0.8, song: 0.93)
  • Non-acoustic preference matched: 0.05
  • High-energy danceability bonus
  • Positive/uplifting vibe bonus

#3: Rooftop Lights by Indigo Parade
Score: 7.40
Why:
  • Mood match: happy
  • Energy similarity: 2.9 (your target: 0.8, song: 0.76)
  • Non-acoustic preference matched: 0.35
  • High-energy danceability bonus
  • Positive/uplifting vibe bonus

#4: Night Drive Loop by Neon Echo
Score: 5.59
Why:
  • Energy similarity: 2.84 (your target: 0.8, song: 0.75)
  • Non-acoustic preference matched: 0.22
  • High-energy danceability bonus
```

Each recommendation includes a **transparency breakdown**: users can see exactly which features matched and why each song ranked higher than others.

---

## Experiments You Tried

**Four user profiles were tested:**

- **High-Energy Pop** (`genre: pop, mood: happy, energy: 0.9`) — Sunrise City and Gym Hero ranked at the top, which felt intuitive. Both are upbeat pop songs with high energy and danceability.
- **Chill Lofi** (`genre: lofi, mood: chill, energy: 0.2, likes_acoustic: True`) — Library Rain and Midnight Coding ranked highest. The acoustic preference bonus clearly separated lofi songs from the rest of the catalog.
- **Deep Intense Rock** (`genre: rock, mood: angry, energy: 0.95`) — Storm Runner ranked first as the only rock song, but the remaining slots were filled by non-rock songs based on energy similarity alone. This exposed the catalog imbalance problem.
- **Adversarial: Conflicting Prefs** (`genre: pop, mood: sad, energy: 0.9, likes_acoustic: True`) — Scores dropped across the board. No song could satisfy all four conflicting preferences, so every result was a partial match with no warning to the user.

---

## Limitations and Risks

- The catalog only has 10 songs, so users with niche tastes (rock, jazz, classical) get weak recommendations after the first genre match runs out.
- The genre weight (+2.0) is large enough to dominate rankings, meaning a pop fan will almost always see pop songs in their top 5 regardless of other preferences.
- The system has no diversity control — the same artist can appear multiple times in the top 5.
- It does not understand lyrics, themes, or cultural context. Two songs with identical energy and valence scores could feel completely different to a real listener.
- Conflicting preferences produce quietly degraded results with no feedback to the user that their profile may be self-contradictory.

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Building VibeFinder made it clear that recommendation quality depends more on data than on algorithm design. Even a well-structured scoring system produces poor results when the catalog is small or imbalanced. With 60% of songs being pop, the system naturally over-serves pop fans and under-serves everyone else — not because of a bug, but because the data reflects a bias that the algorithm faithfully reproduces.

The most interesting discovery was how quickly simple math starts to feel like intelligence. Watching Sunrise City score 9.47 for a happy pop profile felt genuinely correct, even though the logic is just addition and one exponential curve. This made me think differently about real recommenders like Spotify — at their core they are doing something similar, just with millions of songs, learned weights, and listening history instead of hand-tuned rules.


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

