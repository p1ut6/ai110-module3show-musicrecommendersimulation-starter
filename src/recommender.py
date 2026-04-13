from typing import List, Dict, Tuple
from dataclasses import dataclass
import csv
import math

@dataclass
class Song:
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    def __init__(self, songs):
        self.songs = songs

    def recommend(self, user, k=5):
        scored = []
        for song in self.songs:
            score, reasons = self._score_song_oop(song, user)
            scored.append((song, score, reasons))
        scored.sort(key=lambda x: x[1], reverse=True)
        return [s for s, _, _ in scored[:k]]

    def _score_song_oop(self, song, user):
        score = 0.0
        reasons = []
        if song.genre == user.favorite_genre:
            score += 2.0
            reasons.append("Genre match: " + song.genre)
        if song.mood == user.favorite_mood:
            score += 1.0
            reasons.append("Mood match: " + song.mood)
        energy_diff = abs(song.energy - user.target_energy)
        energy_score = 3.0 * math.exp(-((energy_diff) ** 2) / (2 * 0.15 ** 2))
        score += energy_score
        reasons.append("Energy similarity: " + str(round(energy_score, 2)))
        if user.likes_acoustic and song.acousticness > 0.6:
            score += 2.0
            reasons.append("Acoustic preference matched")
        elif not user.likes_acoustic and song.acousticness < 0.4:
            score += 2.0
            reasons.append("Non-acoustic preference matched")
        if user.target_energy > 0.7 and song.danceability > 0.7:
            score += 0.75
            reasons.append("High-energy danceability bonus")
        if song.valence > 0.65:
            score += 0.75
            reasons.append("Positive/uplifting vibe bonus")
        return score, reasons

    def explain_recommendation(self, user, song):
        score, reasons = self._score_song_oop(song, user)
        return "Score: " + str(round(score, 2)) + "/10.0"

def load_songs(csv_path):
    songs = []
    print("Loading songs from " + csv_path + "...")
    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)
    print("Loaded songs: " + str(len(songs)))
    return songs

def score_song(user_prefs, song):
    score = 0.0
    reasons = []
    if song.get("genre") == user_prefs.get("genre"):
        score += 2.0
        reasons.append("Genre match: " + song["genre"])
    if song.get("mood") == user_prefs.get("mood"):
        score += 1.0
        reasons.append("Mood match: " + song["mood"])
    if "energy" in user_prefs:
        energy_diff = abs(song["energy"] - user_prefs["energy"])
        energy_score = 3.0 * math.exp(-((energy_diff) ** 2) / (2 * 0.15 ** 2))
        score += energy_score
        reasons.append("Energy similarity: " + str(round(energy_score, 2)))
    likes_acoustic = user_prefs.get("likes_acoustic", False)
    if likes_acoustic and song.get("acousticness", 0) > 0.6:
        score += 2.0
        reasons.append("Acoustic preference matched")
    elif not likes_acoustic and song.get("acousticness", 1) < 0.4:
        score += 2.0
        reasons.append("Non-acoustic preference matched")
    if user_prefs.get("energy", 0) > 0.7 and song.get("danceability", 0) > 0.7:
        score += 0.75
        reasons.append("High-energy danceability bonus")
    if song.get("valence", 0) > 0.65:
        score += 0.75
        reasons.append("Positive/uplifting vibe bonus")
    return score, reasons

def recommend_songs(user_prefs, songs, k=5):
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons) if reasons else "General match"
        scored.append((song, score, explanation))
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]
