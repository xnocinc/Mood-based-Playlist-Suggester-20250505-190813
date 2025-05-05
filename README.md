# Mood-based Playlist Suggester

**Model Used:** `deepseek-r1:latest`

**Filename:** `mood.py`

**Prompt:**

```
Write a Python script that asks the user for their current mood (e.g., happy, sad, energetic, relaxed) and suggests a short playlist of 3 songs for that mood. Use dictionaries to store mood-to-songs mapping.
```

**Reasoning:**

```
Alright, I need to write a Python script that takes a user's current mood and suggests a playlist based on that. The output should be just the code without explanations.

First, I'll define a dictionary where each key is a mood like 'happy', 'sad', etc., and the value is a list of song names or identifiers. This makes it easy to map moods to playlists.

Next, I'll prompt the user to input their current mood using the input() function. Then, I'll check if this mood exists in the dictionary keys. If it does, I'll display the associated playlist.

I should also handle cases where the mood isn't in the dictionary by letting Python raise a KeyError, which will naturally inform the user that no songs are suggested for that mood.

Choosing song titles is important; they should be relevant to each mood. For example, 'happy' could have upbeat songs like Taylor Swift's 'Bad Weather'. I'll list three songs per mood to provide variety.

I need to make sure the code is clean and well-structured. Using variables for song lists keeps it organized. Also, using a loop or straightforward access should suffice since each key has exactly three songs.

Putting it all together: create the mood dictionary, get user input, check existence, print the playlist if available, else inform them no songs are suggested.
```