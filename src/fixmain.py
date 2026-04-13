code = '''"""
Command line runner for the Music Recommender Simulation.
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\\n" + "="*50)
    print("  Top Recommendations for your profile:")
    print("  Genre: pop | Mood: happy | Energy: 0.8")
    print("="*50)

    for i, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        print(f"\\n#{i}: {song['title']} by {song['artist']}")
        print(f"    Score: {score:.2f}")
        print(f"    Why: {explanation}")

    print("\\n" + "="*50)


if __name__ == "__main__":
    main()
'''

with open("src/main.py", "w", encoding="utf-8") as f:
    f.write(code)
print("Done!")