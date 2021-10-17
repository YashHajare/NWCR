import numpy as np

mat1 = np.array([[3,1,7,4],
                 [2,6,5,9],
                 [8,3,3,2]])
supply = np.array([300,400,500])
demand = np.array([250,350,400,200])

##mat1 = np.array([[2,3,1],
##                 [5,4,8],
##                 [5,6,8]])
##supply = np.array([10,35,25])
##demand = np.array([20,25,25])

print("Given problem:")
print(mat1)
print("Supply:",supply)
print("Demand:",demand)
print("----------------------------")
total = 0;
for x in range(mat1.shape[0]):
    for z in range(mat1.shape[1]):
##        print("Cost:",mat1[x][z],", S:",supply[x],", D:",demand[z])
        minn = min(supply[x],demand[z])
        if (minn != 0):
            print("X",x+1,z+1,":",minn)
        if (minn != 0):
            total = total + minn * mat1[x][z]
            print(mat1[x][z],"*",minn)
        supply[x] -= minn
        demand[z] -= minn
print("----------------------------")
print("Total Transportation cost:",total)
