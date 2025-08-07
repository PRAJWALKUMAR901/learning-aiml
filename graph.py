import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Name': ['Prajwal', 'Alex', 'Riya', 'Steve'],
    'Physics': [85, 72, 90, 66],
    'Chemistry': [78, 80, 65, 70],
    'Maths': [92, 88, 84, 75]
}
df = pd.DataFrame(data)
print(df)

average=df[['Physics','Chemistry','Maths']].mean()
print(average)

subject=['Physics', 'Chemistry', 'Maths']
plt.plot(subject, df.loc[0,subject],marker='o',label='Prajwal')
plt.plot(subject, df.loc[1,subject],marker='<',label='Alex')
plt.plot(subject, df.loc[2,subject],marker='^',label='Steve')
plt.plot(subject, df.loc[3,subject],marker='v',label='Riya')
plt.plot(subject, average,marker='d',label='Average')
plt.legend()
plt.grid(True)
plt.show()
