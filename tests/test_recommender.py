from src.recommender import Song, UserProfile, Recommender

def test_guardrail_prevents_duplicate_artists():
    # Give the system two songs by the exact same artist with high scores
    songs = [
        Song(1, "Pop Hit 1", "Same Artist", "pop", "happy", 0.9, 120, 0.8, 0.8, 0.1),
        Song(2, "Pop Hit 2", "Same Artist", "pop", "happy", 0.9, 120, 0.8, 0.8, 0.1),
        Song(3, "Other Hit", "Different Artist", "pop", "happy", 0.8, 120, 0.8, 0.8, 0.1)
    ]
    rec = Recommender(songs)
    user = UserProfile("pop", "happy", 0.9)
    
    playlist, confidence = rec.generate_playlist(user, k=3)
    
    # Even though 1 and 2 are tied for highest, the guardrail should filter out the duplicate artist
    assert len(playlist) == 2
    assert playlist[1][1].artist == "Different Artist"
