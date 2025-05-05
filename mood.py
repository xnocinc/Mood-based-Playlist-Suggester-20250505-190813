python
mood_songs = {
    "happy": ["Taylor Swift - Bad Weather", "Billie Jean", "Shape of You"],
    "sad": ["Stairway to Heaven", "Layla", "Wannnnner"], 
    "energetic": ["Thriller", "Can't Stop the Feeling!", "Runnin'"], 
    "relaxed": ["Chim Chim Cheree'", "White Christmas", "The Most Wonderful Thing"]
}

mood = input("What is your current mood? ").lower()

if mood in mood_songs:
    print(f"For {mood} mood, here's a suggested playlist of 3 songs:")
    for song in mood_songs[mood]:
        print(song)
else:
    print("No songs found for this mood.")