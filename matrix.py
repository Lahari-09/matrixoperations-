#matrix operations
print ("User instructions:")
print ("1-size of matrix\n2-matrix addition\n3-matrix substraction\n4-matrix multiplication\n5:transpose of matrices\n6-det of matrices\n7-inverse of matices\n8-rank of matrices\n9-eigen matrices\n10-norms\n11-trace of matrices\n12-triangular upper matrices\n13-triangular lower matrices\n14-square root\n15-logirthm\n16-exponential\n17-appending two arrays\n18-sorting of elements\n19-maximum element\n20-length of array")
import numpy as np
import scipy
from scipy import linalg
a=np.matrix('6 4;2 1')
b=np.matrix('5 3;1 6')
m=np.asarray([6,2,3])
n=np.asarray([4,5,6])
print "matrix a:\n",a
print "matrix b:\n",b
print "array m:\n",m
print "array n:\n",n
x=input("enter the number of operation you want:")
#1-size
if(x==1):
	print "matrix size of a:",np.size(a)
	print "matrix size of b:",np.size(b)
#2-addition
elif(x==2):
	print "matrix addition:\n",np.add(a,b)
#3-substraction
elif(x==3):
	c=a-b
	print "matrix substraction:\n",c
#4-multiplication
elif(x==4):
	d=a*b
	print "matrix multiplication:\n",d
#5-transpose
elif(x==5):
	print "transpose of a:\n",np.transpose(a)
	print "transpose of b:\n",np.transpose(b)
#6-determinant
elif(x==6):
	print "det of a:\n",np.linalg.det(a)
	print "det of b:\n",np.linalg.det(b)
#7-inverse
elif(x==7):
	print "inverse of a:\n",np.linalg.inv(a)
	print "inverse of b:\n",np.linalg.inv(b)
#8-rank
elif(x==8):
	print "rank of a:\n",np.linalg.matrix_rank(a)
	print "rank of b:\n",np.linalg.matrix_rank(b)
#9-eigen
elif(x==9):
	print "eigen matrix of a:\n",np.linalg.eig(a)
	print "eigen matrix of b:\n",np.linalg.eig(b)
#10-norm
elif(x==10):
	print "norm of a:\n",np.linalg.norm(a)
	print "norm of b:\n",np.linalg.norm(b)
#11-trace
elif(x==11):
	print "trace of a:\n",np.trace(a)
	print "trace of b:\n",np.trace(b)
#12-triangular upper
elif(x==12):
	print "upper of a:\n",np.triu(a)
	print "upper of b:\n",np.triu(b)
#13-triangular lower
elif(x==13):
	print "lower of a:\n",np.tril(a)
	print "lower of b:\n",np.tril(b)
#14-square root 
elif(x==14):
	print "square root of a:\n",np.sqrt(a)
#15-logirthm
elif(x==15):
	print "logirthm of a:\n",np.log(a)
#16-exponential
elif(x==16):
	print "exponential of a:\n",np.exp(a)
#array operations
#17-append
elif(x==17):
	print "appending of array:\n",np.append(m,n)
#18-sorting
elif(x==18):
	print "sorting array elements:\n",np.sort(m)
#19-maximum
elif(x==19):
	print "maximum value in array:\n",np.max(m)
#20-length
elif(x==20):
	print "length of m:\n",np.size(m)
	print "length of n:\n",np.size(n)	
else:
	print "enter valid number"
