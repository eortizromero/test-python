*************************************************
Diferencia entre `LEFT OUTER JOIN` e `INNER JOIN`
*************************************************

Cuando se realiza un **INNER JOIN** en dos tablas,
se obtienen la intersección de las filas que
tienen en cómun.

Ejemplo:

Tenemos dos tablas (users, groups), con una columna y 3 registros cada una.

+--------------+  +--------------+
| table_groups |  | table_users  |
+--------------+  +--------------+
|   user_id    |  |   	  id     |
+==============+  +==============+
|	1      |  |	  2	 |
+--------------+  +--------------+
|	2      |  |	  3      |
+--------------+  +--------------+
|	3      |  |	  4      |
+--------------+  +--------------+

El `INNER JOIN` en este caso, haciendo la siguiente consulta:

``SELECT`` * ``FROM`` `table_groups` ``INNER JOIN`` `table_users` ``ON`` (table_groups.user_id==table_users.id)

Nos devuelve:

+---------+--------+
| user_id |  id    |
+=========+========+
|    2    |   2	   |
+---------+--------+
|    3    |   3    |
+---------+--------+

Por otro lado, un **LEFT OUTER JOIN**, nos retorna todas las filas de `table_groups`, pero también filas comunes entre ambas tablas.

Ejemplo:

``SELECT`` * ``FROM`` `table_groups` ``LEFT OUTER JOIN`` `table_user` ON (table_groups.user_id==table_users.id)

Devuelve:

+---------+--------+
| user_id |   id   |
+=========+========+
|    1    | null   |      
+---------+--------+
|    2    |  2     |
+---------+--------+
|    3    |  3     |
+------------------+


