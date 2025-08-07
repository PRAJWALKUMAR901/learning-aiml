import matplotlib.pyplot as plt

tests = ['Test 1', 'Test 2', 'Test 3']
physics = [70, 75, 80]
chemistry = [65, 60, 70]
maths = [90, 85, 95]

# Add labels to each plot
plt.plot(tests, physics, marker='o', label='Physics')
plt.plot(tests, chemistry, marker='s', label='Chemistry')
plt.plot(tests, maths, marker='^', label='Maths')

plt.title("Subject-wise Performance Over Tests")
plt.xlabel("Tests")
plt.ylabel("Marks")
plt.legend()
plt.ylim(0, 100)  # Optional: sets y-axis range
plt.grid(True)    # Optional: adds grid for readability
plt.show()


