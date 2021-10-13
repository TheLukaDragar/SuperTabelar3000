# Tabelar.py
Run python Tabelar_2.0.py
enter as many expressions as you like  a+b a>>b a*b a&&b... a+c+d .. and It will create and add to a truth table and minimize every function. you can name variables whatever you want.
```
enter expression
a or b && d + x1 >> x2
a  or  b  and  d  or  x1  ^1 or  x2
['a', 'b', 'd', 'x1', 'x2']
------------------------------
a  or  b  and  d  or  x1  ^1 or  x2
------------------------------
0  or  0  and  0  or  0  ^1 or  0 ~ 1
0  or  0  and  0  or  0  ^1 or  1 ~ 1
0  or  0  and  0  or  1  ^1 or  0 ~ 0
0  or  0  and  0  or  1  ^1 or  1 ~ 1
0  or  0  and  1  or  0  ^1 or  0 ~ 1
0  or  0  and  1  or  0  ^1 or  1 ~ 1
0  or  0  and  1  or  1  ^1 or  0 ~ 0
0  or  0  and  1  or  1  ^1 or  1 ~ 1
0  or  1  and  0  or  0  ^1 or  0 ~ 1
0  or  1  and  0  or  0  ^1 or  1 ~ 1
0  or  1  and  0  or  1  ^1 or  0 ~ 0
0  or  1  and  0  or  1  ^1 or  1 ~ 1
0  or  1  and  1  or  0  ^1 or  0 ~ 1
0  or  1  and  1  or  0  ^1 or  1 ~ 1
0  or  1  and  1  or  1  ^1 or  0 ~ 1
0  or  1  and  1  or  1  ^1 or  1 ~ 1
1  or  0  and  0  or  0  ^1 or  0 ~ 1
1  or  0  and  0  or  0  ^1 or  1 ~ 1
1  or  0  and  0  or  1  ^1 or  0 ~ 1
1  or  0  and  0  or  1  ^1 or  1 ~ 1
1  or  0  and  1  or  0  ^1 or  0 ~ 1
1  or  0  and  1  or  0  ^1 or  1 ~ 1
1  or  0  and  1  or  1  ^1 or  0 ~ 1
1  or  0  and  1  or  1  ^1 or  1 ~ 1
1  or  1  and  0  or  0  ^1 or  0 ~ 1
1  or  1  and  0  or  0  ^1 or  1 ~ 1
1  or  1  and  0  or  1  ^1 or  0 ~ 1
1  or  1  and  0  or  1  ^1 or  1 ~ 1
1  or  1  and  1  or  0  ^1 or  0 ~ 1
1  or  1  and  1  or  0  ^1 or  1 ~ 1
1  or  1  and  1  or  1  ^1 or  0 ~ 1
1  or  1  and  1  or  1  ^1 or  1 ~ 1
------------------------------
['a  or  b  and  d  or  x1  ^1 or  x2']
--------------------Results------------------------------
abdx1x2
00000 1
00001 1
00010 0
00011 1
00100 1
00101 1
00110 0
00111 1
01000 1
01001 1
01010 0
01011 1
01100 1
01101 1
01110 1
01111 1
10000 1
10001 1
10010 1
10011 1
10100 1
10101 1
10110 1
10111 1
11000 1
11001 1
11010 1
11011 1
11100 1
11101 1
11110 1
11111 1
-------------------------------------------------------
PDNO: a  or  b  and  d  or  x1  ^1 or  x2 
 a'b'd'x1'x2' + a'b'd'x1'x2 + a'b'd'x1x2 + a'b'dx1'x2' + a'b'dx1'x2 + a'b'dx1x2 + a'bd'x1'x2' + a'bd'x1'x2 + a'bd'x1x2 + a'bdx1'x2' + a'bdx1'x2 + a'bdx1x2' + a'bdx1x2 + ab'd'x1'x2' + ab'd'x1'x2 + ab'd'x1x2' + ab'd'x1x2 + ab'dx1'x2' + ab'dx1'x2 + ab'dx1x2' + ab'dx1x2 + abd'x1'x2' + abd'x1'x2 + abd'x1x2' + abd'x1x2 + abdx1'x2' + abdx1'x2 + abdx1x2' + abdx1x2
DNO: a  or  b  and  d  or  x1  ^1 or  x2 
 a + bd + x1' + x2
enter expression




Enjoy
