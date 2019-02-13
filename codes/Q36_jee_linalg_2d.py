import numpy as np
import matplotlib.pyplot as plt

n=[2,1]
m=[1,-1]
normal=np.vstack((n,m))
p=[3,1]
print("point of intersection",np.matmul(np.linalg.inv(normal),p))
pt_int=np.matmul(np.linalg.inv(normal),p)

omat=np.array([[0,1],[-1,0]])
a=np.array([1,-1])
line1=np.array([2,1])
line1_dir=np.matmul(line1,omat)
line2=np.array([1,-1])
line2_dir=np.matmul(line2,omat)
pt_int_a=np.vstack((pt_int,a)).T
dvec=np.array([-1,1])
radius_vec=np.matmul(pt_int_a,dvec)

dir_vec_tangent=np.matmul(radius_vec,omat)

x=np.zeros((2,20))
x1=np.zeros((2,20))
x2=np.zeros((2,20))
lamda=np.linspace(-1.8,1.8,20)

for i in range(20):
    y=a+lamda[i]*dir_vec_tangent
    x[:,i]=y.T
    y1=pt_int+lamda[i]*line1_dir
    x1[:,i]=y1.T
    y2=pt_int+lamda[i]*line2_dir
    x2[:,i]=y2.T

    
r=np.sqrt(17)/3
t=np.linspace(-np.pi,np.pi,100)
pt_int_mat=np.vstack(pt_int)
circle_parameters=q=np.array([np.cos(t),np.sin(t)])
circle_parameters_mat=np.vstack(circle_parameters)

x3=pt_int_mat+r*circle_parameters_mat

plt.plot(x3[0,:],x3[1,:],label='$x^2 + y^2 - 8/3 x - 2/3 y = 0$')
plt.plot(a[0],a[1],'o')
plt.text(a[0]*(1),a[1]*(1+0.4),'(1,-1)')
plt.text(a[0],a[1],'P')
plt.plot(pt_int[0],pt_int[1],'o')
plt.text(pt_int[0]*(1+0.1),pt_int[1]*(1-0.1),'O')
plt.text(pt_int[0]*(1+0.5),pt_int[1]*(1+0.4),'(4/3,1/3)')
plt.axis('equal')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.plot(x[0,:],x[1,:],label='$x+4y+3=0$')
plt.plot(x1[0,:],x1[1,:],label='$2x+y-3=0$')
plt.plot(x2[0,:],x2[1,:],label='$x-y-1=0$')
plt.legend(loc='upper right')
plt.grid()
plt.show()
