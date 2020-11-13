# Tabelar.py
enter as many expressionslike  a+b a>>b a*b a&&b... a+c+d .. and It will create and add to a truth table. you can name variables whatever you want.
```
enter expression
a or b
a  or  b
['a', 'b', 'c']
------------------------------
(a ^1 or b  and   not  b) ^1 or c
------------------------------
(0 ^1 or 0  and   not  0) ^1 or 0 ~ 0
(0 ^1 or 0  and   not  0) ^1 or 1 ~ 1
(0 ^1 or 1  and   not  1) ^1 or 0 ~ 0
(0 ^1 or 1  and   not  1) ^1 or 1 ~ 1
(1 ^1 or 0  and   not  0) ^1 or 0 ~ 1
(1 ^1 or 0  and   not  0) ^1 or 1 ~ 1
(1 ^1 or 1  and   not  1) ^1 or 0 ~ 1
(1 ^1 or 1  and   not  1) ^1 or 1 ~ 1
------------------------------
a  or  b
------------------------------
0  or  0 ~ 0
0  or  0 ~ 0
0  or  1 ~ 1
0  or  1 ~ 1
1  or  0 ~ 1
1  or  0 ~ 1
1  or  1 ~ 1
1  or  1 ~ 1
------------------------------
['(a ^1 or b  and   not  b) ^1 or c', 'a  or  b']
--------------------Results------------------------------
abc
000 00
001 10
010 01
011 11
100 11
101 11
110 11
111 11
-------------------------------------------------------
enter expression
a+b
a or b
['a', 'b', 'c']
------------------------------
(a ^1 or b  and   not  b) ^1 or c
------------------------------
(0 ^1 or 0  and   not  0) ^1 or 0 ~ 0
(0 ^1 or 0  and   not  0) ^1 or 1 ~ 1
(0 ^1 or 1  and   not  1) ^1 or 0 ~ 0
(0 ^1 or 1  and   not  1) ^1 or 1 ~ 1
(1 ^1 or 0  and   not  0) ^1 or 0 ~ 1
(1 ^1 or 0  and   not  0) ^1 or 1 ~ 1
(1 ^1 or 1  and   not  1) ^1 or 0 ~ 1
(1 ^1 or 1  and   not  1) ^1 or 1 ~ 1
------------------------------
a  or  b
------------------------------
0  or  0 ~ 0
0  or  0 ~ 0
0  or  1 ~ 1
0  or  1 ~ 1
1  or  0 ~ 1
1  or  0 ~ 1
1  or  1 ~ 1
1  or  1 ~ 1
------------------------------
a or b
------------------------------
0 or 0 ~ 0
0 or 0 ~ 0
0 or 1 ~ 1
0 or 1 ~ 1
1 or 0 ~ 1
1 or 0 ~ 1
1 or 1 ~ 1
1 or 1 ~ 1
------------------------------
['(a ^1 or b  and   not  b) ^1 or c', 'a  or  b', 'a or b']
--------------------Results------------------------------
abc
000 000
001 100
010 011
011 111
100 111
101 111
110 111
111 111
-------------------------------------------------------
enter expression




Enjoy
