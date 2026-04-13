"""
Command line runner for the Music Recommender Simulation.
"""

from recommender import load_songs, recommend_songs


def run_profile(label, user_prefs, songs):
    print("\n" + "="*55)
    print(f"  Profile: {label}")
    print(f"  Prefs: {user_prefs}")
    print("="*55)
    recommendations = recommend_songs(user_prefs, songs, k=5)
    for i, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        print(f"\n#{i}: {song['title']} by {song['artist']}")
        print(f"    Score: {score:.2f}")
        print(f"    Why: {explanation}")
    print()


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = [
        ("High-Energy Pop", {"genre": "pop", "mood": "happy", "energy": 0.9, "likes_acoustic": False}),
        ("Chill Lofi", {"genre": "lofi", "mood": "chill", "energy": 0.2, "likes_acoustic": True}),
        ("Deep Intense Rock", {"genre": "rock", "mood": "angry", "energy": 0.95, "likes_acoustic": False}),
        ("Adversarial: Conflicting Prefs", {"genre": "pop", "mood": "sad", "energy": 0.9, "likes_acoustic": True}),
    ]

    for label, prefs in profiles:
        run_profile(label, prefs, songs)


if __name__ == "__main__":
    main()
