import asyncio
import aiohttp  # pip install aiohttp aiodns
import json
import urllib.parse

ITUNES_QUERY = "https://itunes.apple.com/search?term={query}&limit=1"

async def get_genre(session: aiohttp.ClientSession, title: str):
    song_title = title.strip().lower()

    if len(song_title) == 0:
        return ""

    try:
        encoded_title = urllib.parse.quote_plus(song_title)
        url = ITUNES_QUERY.format(query = encoded_title)
        response = await session.request("GET", url=url)
        content = json.loads(await response.text())
        genre = content["results"][0]["primaryGenreName"].lower()
        return genre
    except:
        return ""

async def get_songs_genres(songs_titles):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for title in songs_titles:
            tasks.append(get_genre(session=session, title=title))
        # asyncio.gather() will wait on the entire task set to be
        # completed.  If you want to process results greedily as they come in,
        # loop over asyncio.as_completed()
        genres = await asyncio.gather(*tasks, return_exceptions=True)
        filtered_genres = filter(lambda genre: len(genre) > 0, genres)
        return list(set(filtered_genres))
