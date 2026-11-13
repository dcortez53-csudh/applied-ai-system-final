from src.recommender import load_songs, UserProfile, Recommender

def main():
    songs = load_songs('data/songs.csv')
    rec = Recommender(songs)

    user = UserProfile(favorite_genre="pop", favorite_mood="happy", target_energy=0.85)
    
    print(f"--- Agentic Output for {user.favorite_genre} fan ---")
    playlist, confidence = rec.generate_playlist(user, k=5)
    
    for rank, (score, song) in enumerate(playlist, start=1):
        print(f"{rank}. {song.title} by {song.artist} (Score: {score:.2f})")
        
    print(f"\nSystem Confidence Score: {confidence * 100:.1f}%")

if __name__ == "__main__":
    main()
