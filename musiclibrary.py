import random
import webbrowser

#a different music library module to handle music playing functionality
music = {
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "hello": "https://www.youtube.com/watch?v=YQHsXMglC9A",
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "waka waka": "https://www.youtube.com/watch?v=pRpeEdMmmQ0",
    "blank space": "https://www.youtube.com/watch?v=e-ORhEE9VVg",
    "uptown funk": "https://www.youtube.com/watch?v=OPf0YbXqDm0",
    "sugar": "https://www.youtube.com/watch?v=09R8_2nJtjg",
    "bad guy": "https://www.youtube.com/watch?v=DyDfgMOUjCI",
    "levitating": "https://www.youtube.com/watch?v=TUVcZfQe-Kw",
    "blinding lights": "https://www.youtube.com/watch?v=4NRXx6U8ABQ",
    "thank u next": "https://www.youtube.com/watch?v=gl1aHhXnN1k",
    "gods plan": "https://www.youtube.com/watch?v=xpVfcZ0ZcFM",
    "circles": "https://www.youtube.com/watch?v=wXhTHyIgQ_U",
    "bad romance": "https://www.youtube.com/watch?v=qrO4YZeyl0I",
    "roar": "https://www.youtube.com/watch?v=CevxZvSJLk8",
    "diamonds": "https://www.youtube.com/watch?v=lWA2pjMjpBs",
    "stitches": "https://www.youtube.com/watch?v=VbfpW0pbvaU",
    "havana": "https://www.youtube.com/watch?v=BQ0mxQXmLsk",
    "sorry": "https://www.youtube.com/watch?v=fRh_vgS2dFE",
    "chandelier": "https://www.youtube.com/watch?v=2vjPBrBU-TM",
    "viva la vida": "https://www.youtube.com/watch?v=dvgZkm1xWPE",
    "thunder": "https://www.youtube.com/watch?v=fKopy74weus",
    "rolling in the deep": "https://www.youtube.com/watch?v=rYEDA3JcQqw",
    "perfect": "https://www.youtube.com/watch?v=2Vv-BfVoq4g",
    "love story": "https://www.youtube.com/watch?v=8xg3vE8Ie_E",
    "starboy": "https://www.youtube.com/watch?v=34Na4j"
}

def play_random_song():
    """Play a random song from the music library on YouTube."""
    if not music:
        print("No songs available in the music library.")
        return

    song_name = random.choice(list(music.keys()))
    song_url = music[song_name]
    
    print(f"Playing: {song_name}")
    webbrowser.open(song_url)

def play_song_by_name(song_name):
    """Play a specific song by searching for it in the library."""
    song_name = song_name.lower().strip()
    
    for title, url in music.items():
        if song_name in title.lower():
            print(f"Playing: {title}")
            webbrowser.open(url)
            return True
    
    # If not found in library, search YouTube
    print(f"Song '{song_name}' not in library. Searching YouTube...")
    search_url = f"https://www.youtube.com/results?search_query={song_name.replace(' ', '+')}"
    webbrowser.open(search_url)
    return False