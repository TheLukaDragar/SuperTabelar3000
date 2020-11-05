# Tablelar.py
enter as many expressionslike  a+b a>>b a*b a&&b... a+c+d .. and It will create and add to a truth table.
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


# SuperTabelar3000

```
Automatic DS homework solver just copy and paste "t∨p∨u,t⇒(p∨u),¬u∨¬q∨s⊨¬t∧p" and you will get the table out
--------------------Results------------------------------
TPUQS
00000 011 0 
00001 011 0 
00010 011 0 
00011 011 0 
00100 111 0 protiprimer
00101 111 0 protiprimer
00110 110 0 
00111 111 0 protiprimer
01000 111 1 
01001 111 1 
01010 111 1 
01011 111 1 
01100 111 1 
01101 111 1 
01110 110 1 
01111 111 1 
10000 101 0 
10001 101 0 
10010 101 0 
10011 101 0 
10100 111 0 protiprimer
10101 111 0 protiprimer
10110 110 0 
10111 111 0 protiprimer
11000 111 0 protiprimer
11001 111 0 protiprimer
11010 111 0 protiprimer
11011 111 0 protiprimer
11100 111 0 protiprimer
11101 111 0 protiprimer
11110 110 0 
11111 111 0 protiprimer
-------------------------------------------------------
Protiprimerov: 13

```

Enjoy
