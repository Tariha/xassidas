from dataclasses import dataclass, field
from typing import List

@dataclass
class TranslatedName:
    lang: str
    transcription: str
    translation: str

@dataclass
class VerseTiming:
    verse_number: int
    timestamp_from: str
    timestamp_to: str
    duration: str

@dataclass
class Audio:
    file: str
    duration: str
    reciter: str
    verse_timings: List[VerseTiming] = field(default_factory=list)

@dataclass
class Reciter:
    name: str
    picture: str
    #audios: List[Audio] = None

@dataclass
class Word:
    position: int
    text: str
    transcription: str

@dataclass
class VerseTranslation:
    lang: str
    text: str
    author: str = None

@dataclass
class Verse:
    number: int
    key: str
    text: str
    words: List[Word] = None
    translations: List[VerseTranslation] = field(default_factory=list)

@dataclass
class Chapter:
    name: str
    number: int
    verses: List[Verse]
    translated_names: List[TranslatedName] = field(default_factory=list)

@dataclass
class Xassida:
    name: str
    chapters: List[Chapter]
    translated_names: List[TranslatedName] = field(default_factory=list)
    audios: List[Audio] = field(default_factory=list)
    translated_lang : List = field(default_factory=list)

@dataclass
class AuthorInfo:
    lang: str
    text: str

@dataclass
class Author:
    name: str
    tariha: str
    picture: str = ""
    xassidas: List[Xassida] = field(default_factory=list)
    infos: List[AuthorInfo] = field(default_factory=list)
