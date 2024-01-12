Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> our_list=[1,2,3,[4,5,6],True,False]
>>> for i in range(0,len(our_list)):
	print(our_list[i])

	
1
2
3
[4, 5, 6]
True
False
>>> our_list[2][0]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    our_list[2][0]
TypeError: 'int' object is not subscriptable
>>> our_list[3][0]
4
>>> table1=[[1,2,3],[4,5,6],[7,8,9]]
>>> table1[0]
[1, 2, 3]
>>> table1[-1]
[7, 8, 9]
>>> 