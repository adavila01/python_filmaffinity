
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

Exanple
-------

.. code-block:: python
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

El modo clásico, considera una busqueda simple, si usted hace una busqueda con uno y solo uno de los siguientes argumentos ('title', 'director', 'cast'), por lo que no importa si intenta aplicar un filtro, la busqueda será siempre la misma.

Una solución, es anteponer otro argumento, para obligar a la busqueda avanzada, y despues aplicar el filtro.

**NOTA**
En el modo classico, solo se considerara el último de los tres argumentos de busqueda('title', 'director', 'cast')
 

.. block-code:: python

  mvs = sv.search(cast='',title='pesadilla en elm street',from_year='1990')
  for m in mvs: m['title']
  'Pesadilla en Elm Street (El origen)  (2010) '
  'Pesadilla en Elm Street: Desde dentro  (2010) '
  'Pesadilla final: La muerte de Freddy (Pesadilla en Elm Street 6)  (1991) '
