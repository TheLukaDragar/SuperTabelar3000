# Tabelar.py
enter as many expressionslike  a+b a>>b a*b a&&b... a+c+d .. and It will create and add to a truth table. you can name variables whatever you want.
```
vnesi izraz
a+b
['A', 'B']
------------
A+B
------------
-------------------------
A or B
-------------------------
0 or 0 ~ 0
0 or 1 ~ 1
1 or 0 ~ 1
1 or 1 ~ 1
------------
['A or B']
--------------------Results------------------------------
AB
00 0
01 1
10 1
11 1
-------------------------------------------------------
vnesi izraz
['A', 'B', 'C']
------------
A+B
A>>C
------------
-------------------------
A or B
-------------------------
0 or 0 ~ 0
0 or 0 ~ 0
0 or 1 ~ 1
0 or 1 ~ 1
1 or 0 ~ 1
1 or 0 ~ 1
1 or 1 ~ 1
1 or 1 ~ 1
-------------------------
 not  ( A  )  or  C
-------------------------
 not  ( 0  )  or  0 ~ 1
 not  ( 0  )  or  1 ~ 1
 not  ( 0  )  or  0 ~ 1
 not  ( 0  )  or  1 ~ 1
 not  ( 1  )  or  0 ~ 0
 not  ( 1  )  or  1 ~ 1
 not  ( 1  )  or  0 ~ 0
 not  ( 1  )  or  1 ~ 1
------------
['A or B', ' not  ( A  )  or  C']
--------------------Results------------------------------
ABC
000 01
001 01
010 11
011 11
100 10
101 11
110 10
111 11
-------------------------------------------------------
vnesi izraz
```




Enjoy
