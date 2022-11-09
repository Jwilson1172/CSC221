
<h1>
CSC 221 Development Assignment 2
</h1>
<h2>
PURPOSE: To use if/else and sentinel controlled while loops.
</h2>
PROBLEM:
1. Write a Python program to calculate the surface area, volume, or “Girth + Depth” of a
Box.   The formulas are as follows:
<br>

 ```text
 
 Volume = LWD (Length X Width X Depth)
 Surface area = 2LW plus 2WD plus 2LD
 Girth+Depth = 2(L+W) plus D (Girth+Depth is used in shipping)

 ```

<p>
<br>
The formulas above are given in algebra; you will have to translate to Python.
<br>
    2. The input of the program will be a letter. “C” will calculate all 3 formulas and display the
results, and “Q” will stop the loop (Q is the sentinel).  The second part of the input will
be three (float) numbers representing the Length, Width, and Depth respectively.
 For example:   C 2.0 3.0 4.0 means calculate a box with the dimensions
Length =2.0, Width = 3.0 and Depth = 4.0
<br>
    3. When you enter C it will calculate all 3 formulas. The output should have
appropriate labels.  Use format to control the appearance of your answers.
<br>
    4. Use sentinel controlled while loops to read the data.  The Q for the operation will be the
sentinel.  The program should work for any data set, not just the data set below.
<br>
    5. Save your Python file as DA2.py and submit in Canvas
</p>
<br><br>

```
INPUT: C 1.0 2.0 3.0
C 5.0 4.0 3.0
C 2.3 4.9 6.7
C 3.7 4.3 9.6
Q
```


OUTPUT:

```
Volume = 6.0
Area = 5.0
Girth and Depth = 12.0
```

<h2>
    GRADING:
<br>
    -60% if program does not build
<br>
    Input and looping are worth 50 points
<br>
    Output is worth 30 points
<br>
    Each formula and its functionality are worth 40 points (120 points total)
</h2>
