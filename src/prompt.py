def generate_prompt(title, description, genres):
    prompt = "create an album cover inspired by a playlist named \"" + title.strip() + "\""
    stripped_description = description.strip()
    description_part = " described as \"" + stripped_description + "\"" if len(stripped_description) > 0 else ""
    genres_size = len(genres)
    genres_part = ""

    if genres_size > 0:
        if genres_size == 1:
            genres_part = " that contains " + genres[0] + " music"
        else:
            joined_genres = " ".join(genres)
            genres_part = " that is a blend of different music genres including \""+ joined_genres +"\""

    return prompt + description_part + genres_part + ", digital art"
