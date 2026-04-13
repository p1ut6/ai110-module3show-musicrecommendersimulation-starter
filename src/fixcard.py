code = '''# Model Card: Music Recommender Simulation

## 1. Model Name
**VibeFinder 1.0**

---

## 2. Intended Use
VibeFinder is a rule-based music recommender designed to suggest songs based on a user's genre preference, mood, energy level, and acousticness taste. It is intended for classroom exploration of how recommendation algorithms work, not for production use. It assumes users can describe their preferences numerically and that a small curated catalog is sufficient for demonstration purposes.

---

## 3. How the Model Works
The model scores every song in the catalog against a user profile and ranks them highest to lowest. A song earns points for matching the user's preferred genre (+2 points), matching their mood (+1 point), and being close in energy level to what the user wants (up to 3 points, using a curve that rewards closeness and penalizes distance). If the user prefers acoustic music, songs with high acousticness earn bonus points, and vice versa. Extra bonus points are awarded for songs that are danceable and uplifting when the user wants high energy. The top 5 scoring songs are returned as recommendations with an explanation of why each one scored the way it did.

---

## 4. Data
The catalog contains 10 songs across genres including pop, lofi, and rock. Moods represented include happy, chill, and angry. The dataset is small and hand-curated for classroom use. Several genres common in real music libraries such as jazz, classical, hip-hop, and country are not represented, which limits the diversity of recommendations for users with those tastes.

---

## 5. Strengths
The system works well for users with clear, consistent preferences. The High-Energy Pop profile correctly surfaced Sunrise City and Gym Hero at the top, which intuitively fit that profile. The Chill Lofi profile cleanly separated lofi and acoustic songs from the rest of the catalog. The energy scoring curve does a good job rewarding songs that are close to the target rather than applying a hard cutoff.

---

## 6. Limitations and Bias
The system over-prioritizes genre matching because the +2 genre bonus is large relative to other scores, especially in a 10-song catalog where several songs share the same genre. The Deep Intense Rock profile exposed a weakness: there is only one rock song in the catalog, so the remaining results were driven entirely by energy similarity rather than genre or mood relevance. The adversarial profile (pop/sad/high-energy/acoustic) revealed that conflicting preferences produce lower overall scores and less confident recommendations, but the system does not warn the user that their preferences may be contradictory. The dataset is too small to surface meaningful variety and does not represent many common genres or moods.

---

## 7. Evaluation
Four user profiles were tested: High-Energy Pop, Chill Lofi, Deep Intense Rock, and an adversarial profile with conflicting preferences (high energy but acoustic, pop genre but sad mood). The Chill Lofi and High-Energy Pop profiles produced intuitive results. The Rock profile was surprising because non-rock songs ranked highly due to energy similarity alone, showing that a small catalog limits genre-based filtering. The adversarial profile produced noticeably lower scores across the board, which makes sense since no single song could satisfy all the conflicting preferences simultaneously.

---

## 8. Future Work
- Expand the catalog to at least 50-100 songs across more genres and moods
- Add a tempo preference so users who want fast or slow songs get better matches
- Introduce a diversity penalty so the same artist does not dominate the top 5
- Warn users when their preferences conflict so they can adjust their profile
- Replace hard-coded weights with learned weights based on user feedback

---

## 9. Personal Reflection
Building VibeFinder made it clear how much a recommendation system depends on the quality and diversity of its data. Even a well-designed scoring algorithm produces mediocre results when the catalog is too small or unbalanced. The most interesting discovery was the adversarial profile: when preferences conflict, scores drop across the board and the system quietly returns its best guess without any indication that it struggled. Real recommendation systems likely face this problem constantly with users who have complex or contradictory tastes.
'''

with open("model_card.md", "w", encoding="utf-8") as f:
    f.write(code)
print("Done!")