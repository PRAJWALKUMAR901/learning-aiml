import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create the student marks data
data = {
    'Name': ['Prajwal', 'Alex', 'Riya', 'Steve', 'Anu'],
    'Physics': [85, 72, 90, 66, 95],
    'Chemistry': [78, 80, 65, 70, 60],
    'Maths': [92, 88, 84, 75, 91]
}

# Step 2: Create the DataFrame
df = pd.DataFrame(data)

# Step 3: Print basic info
print(df)
print("\nStatistics:\n", df.describe())

# Step 4: Calculate and print median of each subject
print("\nMedians:")
print("Physics:", np.median(df['Physics']))
print("Chemistry:", np.median(df['Chemistry']))
print("Maths:", np.median(df['Maths']))

# Step 5: Calculate total marks
df['Total'] = df[['Physics', 'Chemistry', 'Maths']].sum(axis=1)

# Step 6: Print updated table
print("\nWith Total Marks:\n", df)
topper=df[df['Total']==df['Total'].max()]
print('Topper\n', topper)

import matplotlib.pyplot as plt

# Subjects to be shown on x-axis
subjects = ['Physics', 'Chemistry', 'Maths']

# Loop through each student to plot their marks
for i in range(len(df)):
    student_name = df.loc[i, 'Name']
    marks = df.loc[i, ['Physics', 'Chemistry', 'Maths']].values
    plt.plot(subjects, marks, marker='o', label=student_name)

# Add labels and title
plt.title("Performance of Each Student Across Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.legend()  # Show legend for student names
plt.grid(True)
plt.show()