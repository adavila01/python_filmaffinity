
***********
Search page
***********


Explanatory comment:
====================

In filmaffinity, there are two types of searches, the simple, and the advanced, the simple form, will result in what filmaffinity considers most important, according to the country of origin of the search, while the advanced search is more explicit, and it is always limited to what you ask to look for.

Classic mode
-------------

+-----------+----------+--------+-----------------------------------+
| Parameter | Required |   Type | Description                       |
+===========+==========+========+===================================+
| title     |   False  | String | Search for the title of the movie |
+-----------+----------+--------+-----------------------------------+
| cast      |   False  | String | Search movies by actor            |
+-----------+----------+--------+-----------------------------------+
| director  |   False  | String | Search movies by the director     |
+-----------+----------+--------+-----------------------------------+
| from_year |   False  | String | Search start date                 |
+-----------+----------+--------+-----------------------------------+
| to_year   |   False  | String | Search end date                   |
+-----------+----------+--------+-----------------------------------+

Example
-------

.. code-block:: python
  
  import Python_Filmaffinity as pf
  sv = pf.FilmAffinity() 
  sv.lang
  'es' # Default lang
  mvs = sv.search(title='pesadilla en elm street')
  len(mvs)
  5
  mvs = sv.search(title='pesadilla en elm street',from_year='1990')
  len(mvs)
  5
  for m in mvs: m['title']
  'Pesadilla en Elm Street  '
  'Pesadilla en Elm Street (El origen)  '
  'Pesadilla en Elm Street 2: La venganza de Freddy  '
  'Pesadilla en Elm Street 3: Los guerreros del sueño  '
  'Pesadilla en Elm Street 4: El amo del sueño  '

The classic mode, considers a simple search, if you do a search with one and only one of the following arguments ('title', 'director', 'cast'), so it does not matter if you try to apply a filter, the search it will always be the same.

One solution is to prepend another argument, to force the advanced search, and then apply the filter.

**NOTE**
In classic mode, only the last of the three search arguments will be considered ('title', 'director', 'cast')

.. code-block:: python

  mvs = sv.search(cast='',title='pesadilla en elm street',from_year='1990')
  for m in mvs: m['title']
  'Pesadilla en Elm Street (El origen)  (2010) '
  'Pesadilla en Elm Street: Desde dentro  (2010) '
  'Pesadilla final: La muerte de Freddy (Pesadilla en Elm Street 6)  (1991) '
  

Alternative mode
----------------

+-----------+----------+--------+-----------------------------------+
| Parameter | Required |   Type | Description                       |
+===========+==========+========+===================================+
| text_find |   False  | String | searches in simple or advanced    |
|           |          |        | mode, concepts separated by commas|
+-----------+----------+--------+-----------------------------------+
| search_in |   False  | String | Look for concepts (described in   | 
|           |          |        | text_find) in the following       |
|           |          |        | categories:                       |
|           |          |        |                                   |
|           |          |        | * title                           |
|           |          |        | * director                        |
|           |          |        | * cast                            |
|           |          |        | * script                          |
|           |          |        | * photo                           |
|           |          |        | * music                           |
|           |          |        | * producer                        |
+-----------+----------+--------+-----------------------------------+
| country   |   False  | String |                                   |
+-----------+----------+--------+                                   |
| genre     |   False  | String |                                   |
+-----------+----------+--------+  Filter the results found         |
| from_year |   False  | String |                                   |
+-----------+----------+--------+                                   |
| to_year   |   False  | String |                                   |
+-----------+----------+--------+-----------------------------------+
| top       |   False  | String | From the results found, only the  |
|           |          |        | 'top' first results are taken, up |
|           |          |        | to a maximum of 40                |
+-----------+----------+--------+-----------------------------------+

The alternate mode is activated when the "text_find" argument is used, in which case the classic mode arguments ('title', 'director', 'cast') will be skipped even if you send them as a parameter, however; if you only use "text_find", without using the "search_in" argument, or without any of the filters ('country', 'genre', 'from_year', 'to_year'), the search will be done in simple mode.

**Example**

.. code-block:: python

  import Python_Filmaffinity as pf
  sv = pf.FilmAffinity(lang='filmaffinity')
  sv.lang
  'ec' # my country
  mvs = sv.search(text_find='pesadilla en elm street')
  for m in mvs: m['title']
  'Pesadilla en la calle del infierno  '
  'Pesadilla en la calle Elm  '
  'Pesadilla en la calle del infierno 2 - La venganza de Freddy  '
  'Pesadilla en la calle del infierno 3 - Los guerreros del sueño  '
  'Pesadilla en la calle del infierno 4 - El amo de los sueños  '

But, if you use any argument of find_search or the filters ('country', 'genre', 'from_year', 'to_year'), then it forces an advanced search.

**Example**


.. code-block:: python
  
  # considering the previous example
  mvs = sv.search(text_find='pesadilla en elm street',from_year='1990')
  for m in mvs: m['title']
  'Pesadilla en la calle Elm  (2010) '
  'Pesadilla en la calle del infierno 6 - La muerte de Freddy  (1991) '


** Understanding search in alternate mode. **

In alternate mode, it is based on the following concept. text_find = "what should I look for", search_in = "the categories where I should search", ('country', 'genre', 'from_year', 'to_year') filters that I should apply.

**Example**

.. code-block:: python

  import Python_Filmaffinity as pf
  sv = pf.FilmAffinity(lang='filmaffinity')
  sv.lang
  'ec' # my country
  #Example 1
  mvs = sv.search(text_find='pesadilla en elm street, johnny depp',search_in='title,cast')
  for m in mvs: m['title']
  'Pesadilla en la calle del infierno 6 - La muerte de Freddy  (1991) '
  'Pesadilla en la calle del infierno  (1984) '
  # Example 2
  mvs = sv.search(text_find='pesadilla en elm street, johnny depp',search_in='title,cast',from_year='1990')
  for m in mvs: m['title']
  'Pesadilla en la calle del infierno 6 - La muerte de Freddy  (1991) '


