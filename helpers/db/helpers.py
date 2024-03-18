import os
from dotenv import load_dotenv
from pathlib import Path
from supabase import create_client
from slugify import slugify


load_dotenv()

url = os.environ.get("SUPABASE_URL") or ""
key = os.environ.get("SUPABASE_SERVICE_ROLE") or ""
supabase = create_client(url, key)

bucket_name = "images"


def create_author(data, *args):
    """Author insertion"""
    img_path = Path(f"../../xassidas/{data['tariha']}/{data['name']}")
    img_file = next(img_path.glob("profile.*"), None)
    data["slug"] = slugify(f"{data['tariha']}*{data['name']}")
    data["picture"] = f"authors/{data['name']}_profile.png"
    # upsert on supabase database
    try:
        if img_file:
            f = img_file.open("rb")
            supabase.storage.from_(bucket_name).upload(
                file=f,
                path=data["picture"],
                file_options={"content-type": "image/png", "x-upsert": "true"},
            )
        resp = supabase.table("author").upsert(data, on_conflict="slug").execute()
        return resp.data[0]
    except Exception as e:
        raise Exception(f"Error inserting author: {e}")


def create_xassidas(data, author):
    """Xassida insertion"""
    del data["translated_lang"]
    data["author_id"] = author["id"]
    data["slug"] = slugify(f"{author['slug']}*{data['name']}")
    # Assuming 'xassida' table in Supabase
    try:
        resp = supabase.table("xassida").upsert(data, on_conflict="slug").execute()
        return resp.data[0]
    except Exception as e:
        raise Exception(f"Error inserting Xassida: {e}")


def create_chapters(data, xassida):
    """Chapter insertion
    :param xassida a Xassida instance
    """
    data["xassida_id"] = xassida["id"]
    data["slug"] = slugify(f"{xassida['slug']}*{data['number']}")
    # Assuming 'Chapter' table in Supabase
    try:
        resp = supabase.table("chapter").upsert(data, on_conflict="slug").execute()
        return resp.data[0]
    except Exception as e:
        raise Exception(f"Error inserting Chapter: {e}")


def create_verses(data, chapter):
    """Verse insertion
    :param chapter a Chapter instance
    """
    data["chapter_id"] = chapter["id"]
    data["slug"] = slugify(f"{chapter['slug']}*{data['number']}")
    # Assuming 'Verse' table in Supabase
    try:
        resp = supabase.table("verse").upsert(data, on_conflict="slug").execute()
        return resp.data[0]

    except Exception as e:
        raise Exception(f"Error inserting Verse: {e}")


def create_translations(data, verse):
    """VerseTranslation insertion
    :param verse a Verse instance
    """
    data["verse_id"] = verse["id"]
    data["slug"] = verse["slug"] if data["lang"]=="en" else f"{data['lang']}_{verse['slug']}"
    # Assuming 'VerseTranslation' table in Supabase
    try:
        resp = (
            supabase.table("verse_translation")
            .upsert(data, on_conflict="slug")
            .execute()
        )
        return resp.data[0]
    except Exception as e:
        raise Exception(f"Error inserting VerseTranslation: {e}")


def create_reciter(data, *args):
    """Reciter insertion"""
    data["slug"] = slugify(f"{data['tariha']}*{data['name']}")
    # Assuming 'Reciter' table in Supabase
    try:
        resp = supabase.table("reciter").upsert(data, on_conflict="slug").execute()
        return resp.data[0]
    except Exception as e:
        raise Exception(f"Error inserting Reciter: {e}")


def create_translated_names(data, *args):
    pass


def create_audios(data, *args):
    pass


def create_infos(data, author):
    pass


def create_words(data, *args):
    pass
