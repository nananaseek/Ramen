from random import randint
from pydantic  import BaseModel

from .models import Manga_Pydantic, Manga

rand_count = []


class MangaPy(BaseModel):
    id: int
    type: str
    title: str
    link: str
    image: str


async def rand_mod():
    all_manga_id = len(await Manga_Pydantic.from_queryset(Manga.all()))
    rand_manga = await Manga_Pydantic.from_queryset_single(Manga.get(id=randint(1, all_manga_id)))
    manga = MangaPy.parse_raw(rand_manga.json())
    # await rand_def(manga_id=dict(rand_manga))
    return manga


"""
TODO: создать защиту от рандома rand_def
"""
