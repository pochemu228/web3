from fastapi import HTTPException, status
from schemas.movie import Movie
from .crud import movie_storage


def get_movie_by_slug(slug: str) -> Movie:

    return movie_storage.get_by_slug(slug)
