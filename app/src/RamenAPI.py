from fastapi import APIRouter
from app.src.models import Manga_Pydantic, MangaIn_Pydantic, Manga
from tortoise.contrib.fastapi import register_tortoise

ramen_views = APIRouter()


@ramen_views.get('/getManga/{id}', response_model=Manga_Pydantic)
async def get_manga_list(id: int):
    return await Manga_Pydantic.from_queryset_single(Manga.get(id=id))


@ramen_views.post('/addManga', response_model=Manga_Pydantic)
async def add_manga(manga: MangaIn_Pydantic):
    manga_obj = await Manga.create(**manga.dict(exclude_unset=True))
    return await Manga_Pydantic.from_tortoise_orm(manga_obj)
