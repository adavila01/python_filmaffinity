
Explication:
============

In Filmaffinity, the language and the country, are linked to the searches, so; It is not the same to search for "Les Misérables" in the USA as in England, since there is local programming.
Filmaffinity detects the country of origin, and adapts the information to that reality. 

language
********

- Spanish: 'es'
- USA, UK: 'en'
- México: 'mx'
- Argentina: 'ar'
- Chile: 'cl'
- Colombia: 'co'
- filmaffinity (new)

You can manually configure the language as follows:

.. code-block:: python

  import python_filmaffinity as pf
  sv = pf.FilmAffinity(lang='es')
  sv.lang
  'es'
  
But the new option allows filmaffinity to choose the language, according to the country of origin from which the query is made, which in turn makes the search more relevant, it is used:

.. code-block:: python
  
  import python_filmaffinity as pf
  sv = pf.FilmAffinity(lang='filmaffinity')
  sv.lang
  'ec' #my country

Additionally, there are 2 properties that will help you to search more finely, and they are:

    | instance.countries
    | and
    | instance.genres
  
Both return a dict with the code and the name of the country or the genre of the film.

Example
-------

.. code-block:: python

  #Alternative mode
  sv = pf.FilmAffinity(lang='filmaffinity')
  sv.lang                                                                                                                 
  'ec' #my country
  mvs = sv.search(text_find='pesadilla en elm street', from_year='2010', to_year='2010')                                  
  for mv in mvs: mv['title']                                                                                              
  'Pesadilla en la calle Elm  (2010) '
  
  # Classic mode
  sv = pf.FilmAffinity(lang='es')
  sv.lang
  'es'
  mvs = sv.search(text_find='pesadilla en elm street', from_year='2010', to_year='2010')
  for mv in mvs: mv['title']
  'Pesadilla en Elm Street (El origen)  (2010) '
  'Pesadilla en Elm Street: Desde dentro  (2010) ' #documentary, which did not come out in my country

