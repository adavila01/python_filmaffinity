
***********
Search page
***********


Explanatory comment:
====================

In filmaffinity, there are two types of searches, the simple, and the advanced, the simple form, will result in what filmaffinity considers most important, according to the country of origin of the search, while the advanced search is more explicit, and it is always limited to what you ask to look for.

Classic method
---------------

.. block-code:: python
  
  import Python_Filmaffinity as pf
  sv = pf.FilmAffinity() 
  sv.lang
  'es'
  mvs = sv.search(title='pesadilla en elm street')
  len(mvs)
  5
  mvs = sv.search(title='pesadilla en elm street',from_year='1990')
  len(mvs)
  5
