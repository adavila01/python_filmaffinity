"""Config."""
# -*- coding: utf-8 -*-

FIELDS_MOVIE = ['title', 'id']
TEXT_FIND = 'text_find'
SEARCH_IN = 'search_in'
LANG_AUTO = 'filmaffinity'
# FIELDS_TYPE = ['title', 'director', 'cast', 'stext']
FIELDS_TYPE = [TEXT_FIND,'title', 'director', 'cast', 'stext']
FIELDS_SEARCH_IN = ['title','director','cast','script','photo','music','producer']
FIELDS_SEARCH_BY = ['country','genre','from_year','to_year']
LANGUAGES_BY_COUNTRY = [LANG_AUTO,'en', 'es', 'mx', 'ar', 'cl', 'co']


FIELDS_PAGE_MOVIES = ['id', 'title', 'rating', 'directors', 'poster']
FIELDS_DETAIL = ['description', 'votes', 'year', 'country', 'duration',
                 'genre', 'awards', 'reviews', 'actors']
FIELDS_PAGE_DETAIL = FIELDS_PAGE_MOVIES + FIELDS_DETAIL
