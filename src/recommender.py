import csv
import logging

# Set up logging for guardrails
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class Song:
    def __init__(self, id, title, artist, genre, mood, energy, tempo_bpm, valence, danceability, acousticness):
        self.id = id
        self.title = title
        self.artist = artist
        self.genre = genre
        self.mood = mood
        self.energy = energy

class UserProfile:
    def __init__(self, favorite_genre, favorite_mood, target_energy):
        self.favorite_genre = favorite_genre
        self.favorite_mood = favorite_mood
        self.target_energy = target_energy

class Recommender:
    def __init__(self, songs):
        self.songs = songs

    def score_song(self, user, song):
        score = 0.0
        if song.genre.lower() == user.favorite_genre.lower():
            score += 2.0
        if song.mood.lower() == user.favorite_mood.lower():
            score += 1.0
        energy_gap = abs(song.energy - user.target_energy)
        score += (1.0 - energy_gap)
        return score

    def generate_playlist(self, user, k=5):
        """Agentic workflow: Ranks, checks guardrails, and assigns confidence."""
        logging.info(f"Agent started. Generating playlist for {user.favorite_genre}.")
        
        scored_songs = [(self.score_song(user, song), song) for song in self.songs]
        scored_songs.sort(key=lambda x: x[0], reverse=True)
        
        # Guardrail: Prevent Filter Bubble (No duplicate artists)
        final_playlist = []
        seen_artists = set()
        
        for score, song in scored_songs:
            if song.artist not in seen_artists:
                final_playlist.append((score, song))
                seen_artists.add(song.artist)
            if len(final_playlist) == k:
                break
                
        if len(final_playlist) < k:
            logging.warning("Guardrail triggered: Not enough unique artists in dataset.")

        # Calculate Confidence Score (Average of top scores normalized)
        avg_score = sum([s for s, _ in final_playlist]) / len(final_playlist) if final_playlist else 0
        confidence = min(avg_score / 4.0, 1.0) # 4.0 is max possible score
        
        logging.info(f"Agent finished. Playlist confidence: {confidence*100:.1f}%")
        return final_playlist, confidence

def load_songs(filepath):
    songs = []
    try:
        with open(filepath, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                songs.append(Song(
                    id=int(row['id']), title=row['title'], artist=row['artist'],
                    genre=row['genre'], mood=row['mood'], energy=float(row['energy']),
                    tempo_bpm=int(row['tempo_bpm']), valence=float(row['valence']),
                    danceability=float(row['danceability']), acousticness=float(row['acousticness'])
                ))
    except FileNotFoundError:
        logging.error("Guardrail: songs.csv file not found!")
    return songs
