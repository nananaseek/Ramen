from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Manga(models.Model):

    id = fields.IntField(pk=True)
    type = fields.CharField(max_length=320)
    title = fields.CharField(max_length=320)
    link = fields.CharField(max_length=320)
    image = fields.CharField(max_length=320)


Manga_Pydantic = pydantic_model_creator(Manga, name="Manga")
MangaIn_Pydantic = pydantic_model_creator(Manga, name="MangaIn", exclude_readonly=True)
