code = '''# Reflection: Music Recommender Evaluation

## High-Energy Pop vs Chill Lofi

The High-Energy Pop profile surfaced fast, upbeat pop songs like Sunrise City and Gym Hero at the top, while the Chill Lofi profile surfaced calm acoustic songs like Library Rain and Midnight Coding. This makes sense because the energy scoring curve heavily rewards songs close to the target energy, and these two profiles sit at opposite ends of the energy spectrum (0.9 vs 0.2). The genre and acousticness preferences reinforced the separation further, producing two very distinct and intuitive top-5 lists.

## High-Energy Pop vs Deep Intense Rock

Both profiles wanted high energy (0.9 and 0.95), so there was overlap in the middle of the rankings — Gym Hero appeared in both top 5 lists. The key difference was genre: the Pop profile rewarded pop songs with a +2 bonus, while the Rock profile rewarded rock songs. Since only one rock song exists in the catalog (Storm Runner), the Rock profile quickly ran out of genre matches and fell back on energy similarity alone. This shows that a small, genre-imbalanced dataset limits how well the system can serve users outside the dominant genre.

## Chill Lofi vs Adversarial (Conflicting Prefs)

The Chill Lofi profile produced confident, high-scoring recommendations (top score 6.82) because the preferences were consistent and well-matched by songs in the catalog. The adversarial profile — which combined high energy, pop genre, sad mood, and acoustic preference — produced lower scores across the board (top score 6.44) and less coherent results. No single song could satisfy all four preferences at once, so every recommendation was a partial match. This comparison demonstrates that the system works best when user preferences are internally consistent, and struggles silently when they are not.
'''

with open("reflection.md", "w", encoding="utf-8") as f:
    f.write(code)
print("Done!")