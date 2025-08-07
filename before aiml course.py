import numpy as np
from fontTools.unicodedata.Scripts import NAMES

a=np.array([1,2,3,4,5])
print("array=",a)

print("Mean=",np.mean(a))

print("Variance=",np.var(a))

b=np.array([[1,2],[3,4]])

print("2*2 matrix:\n", b )

import pandas as pd
data={'Name' : ['Prajwal','alex','steve'],
      'Marks' : [90,80,70]}
df=pd.DataFrame(data)
print(df)
print(df.describe())

import numpy as np
import matplotlib.pyplot as plt
A=np.array([[70,20],[20,70]])
B=np.array([[20,70],[70,20]])
C=A+B
print(C)

print(np.dot(A,B))

marks=np.array([[95,93,96],
               [80,70,85],
                [60,70,40]])

students=['Student 1', 'Student 2', 'Student 3']

#Weightage=0.5,0.2,0.3
Weightage=np.array([0.5,0.2,0.3])
Total_weightage=np.dot(marks,Weightage)
print(Total_weightage)


plt.bar(students,Total_weightage)
plt.title("GRAPH OF MARKS WEIGHTAGE OF EACH STUDENT")
plt.xlabel("Students")
plt.ylabel("Mark's Weightage")
plt.show()




