import numpy as np
import matplotlib.pyplot  as plt

a=2
p=-2
nor_vec_tan1=np.array([1,-1])


omat=np.array([[0,1],[-1,0]])
dir_vec_tan1=np.matmul(omat,nor_vec_tan1)

slope=0
nor_vec_tan2=dir_vec_tan1

slope=dir_vec_tan1[0]


nor_vec_tan2=np.array([-slope,1])
p1=np.array([a/slope,p])



normal=np.vstack((nor_vec_tan1,nor_vec_tan2))

pt_int=np.matmul(np.linalg.inv(normal),p1)
print('the point if intersection is',pt_int)
x=np.zeros((2,20))

tan1=np.zeros((2,20))
tan2=np.zeros((2,20))
t=np.linspace(-2,2,20)

lamda=np.linspace(-5,5,20)
for i in range(20):
    
    X=np.array([a*t[i]**2,2*a*t[i]])    
    x[:,i]=X.T
    y1=pt_int+lamda[i]*dir_vec_tan1
    
    tan1[:,i]=y1.T
    
    y2=pt_int+lamda[i]*nor_vec_tan1
    tan2[:,i]=y2.T

x1=[pt_int[0]]*20
y=[0]*20
x4=np.linspace(-7,7,20)
plt.plot(x4,y,label='$y=0$')
plt.plot(x[0,:],x[1,:],label='$y^2=8x$')
plt.plot(pt_int[0],0,'o')
plt.text(-4,0,'P(-2,0)')
plt.plot(tan1[0,:],tan1[1,:],label='$x - y + 2 = 0$')
plt.plot(tan2[0,:],tan2[1,:])
plt.plot(x1,lamda,label='$x=-2$')
plt.legend(loc='best')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid()
plt.show()
    
