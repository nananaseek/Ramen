from fastapi import APIRouter
from app.src.models import Manga_Pydantic, MangaIn_Pydantic, Manga

from .randoM import *

ramen_views = APIRouter()


@ramen_views.get('/getRandomManga')
async def get_random_manga():
    return await rand_mod()


@ramen_views.get('/getManga/{id}', response_model=Manga_Pydantic)
async def get_manga(id: int):
    return await Manga_Pydantic.from_queryset_single(Manga.get(id=id))


@ramen_views.post('/addManga', response_model=Manga_Pydantic)
async def add_manga(manga: MangaIn_Pydantic):
    manga_obj = await Manga.create(**manga.dict(exclude_unset=True))
    return await Manga_Pydantic.from_tortoise_orm(manga_obj)
