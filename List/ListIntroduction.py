Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = []
>>> x.append(2)
>>> x
[2]
>>> x.append(4)
>>> x.append(6)
>>> x.append(8)
>>> x
[2, 4, 6, 8]
>>> x = []
>>> for i in range(51):
	if i % 2 == 0:
		x.append(i)

		
>>> x
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> x.pop()
50
>>> x.pop(6)
12
>>> del x[6]
>>> x
[0, 2, 4, 6, 8, 10, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> del x
>>> x
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> x = [0, 2, 4, 6, 8, 10, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> x.insert(0,100)
>>> x
[100, 0, 2, 4, 6, 8, 10, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> x2 = [i for i in range(51)]
>>> x2
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
>>> x2 = [i for i in range(50) if i % 2 == 0]
>>> x2
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> x2 = [i for i in range(50) if i % 2 != 0]
>>> x2
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
>>> x + x2
[100, 0, 2, 4, 6, 8, 10, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
>>> x
[100, 0, 2, 4, 6, 8, 10, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> x.append(x2)
>>> x
[100, 0, 2, 4, 6, 8, 10, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]]
>>> x.pop()
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
>>> x.extend(x2)
>>> x
[100, 0, 2, 4, 6, 8, 10, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
>>> sorted(x)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 100]
>>> sorted(x, reverse = True)
[100, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 13, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> x
[100, 0, 2, 4, 6, 8, 10, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
>>> x.sort()
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 100]
>>> x.remove(99)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    x.remove(99)
ValueError: list.remove(x): x not in list
>>> x.remove(100)
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> y = x
>>> y[0] = 'bye'
>>> y
['bye', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> x
['bye', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> z = x[:]
>>> z
['bye', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> x
['bye', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> z[0] = 'hello'
>>> z
['hello', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> x
['bye', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> x == z
False
>>> z = x[:]
>>> z
['bye', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> x
['bye', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> z == x
True
>>> y == z
True
>>> y == x
True
>>> y is x
True
>>> z is x
False
>>> x = [1,2,2,4,5,6,6,7]
>>> y = x
>>> z = x[:]
>>> y == x
True
>>> y is x
True
>>> z is x
False
>>> x = [1,2,2,4,5,6,6,7,[9,1,2,4,5,45]]
>>> y = x[:]
>>> x[0] = 'hello'
>>> x
['hello', 2, 2, 4, 5, 6, 6, 7, [9, 1, 2, 4, 5, 45]]
>>> y
[1, 2, 2, 4, 5, 6, 6, 7, [9, 1, 2, 4, 5, 45]]
>>> x[-1][0] = 'nine'
>>> x
['hello', 2, 2, 4, 5, 6, 6, 7, ['nine', 1, 2, 4, 5, 45]]
>>> y
[1, 2, 2, 4, 5, 6, 6, 7, ['nine', 1, 2, 4, 5, 45]]
>>> import copy
>>> z = copy.deepcopy(x)
>>> x
['hello', 2, 2, 4, 5, 6, 6, 7, ['nine', 1, 2, 4, 5, 45]]
>>> z
['hello', 2, 2, 4, 5, 6, 6, 7, ['nine', 1, 2, 4, 5, 45]]
>>> x[-1][0] = 100
>>> x
['hello', 2, 2, 4, 5, 6, 6, 7, [100, 1, 2, 4, 5, 45]]
>>> z
['hello', 2, 2, 4, 5, 6, 6, 7, ['nine', 1, 2, 4, 5, 45]]
>>> 
