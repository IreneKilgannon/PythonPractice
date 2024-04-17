# Histogram of Sepal Length by species. 
fig, ax = plt.subplots(1, 3, sharex= True, sharey= True)
ax[0].hist(setosa['sepal_length_cm'], edgecolor = 'black', alpha = 1.0, bins = 7)
ax[1].hist(versicolor['sepal_length_cm'], label = 'Iris versicolor', color = 'orange', edgecolor = 'black', alpha = 1.0, bins = 7)
ax[2].hist(virginica['sepal_length_cm'], label = 'Iris virginica', color = 'green', edgecolor = 'black', alpha = 1.0, bins = 7)

ax[0].set_xlabel('Sepal length (cm) \nIris setosa')
ax[1].set_xlabel('Sepal length (cm), \nIris versicolor')
ax[2].set_xlabel('Sepal length (cm), \nIris virginica')
ax[0].set_ylabel('No of instances')

fig.suptitle('Histogram of Sepal Length by Iris species')

#plt.savefig('sepal_length.png')
plt.show()

# Histogram of Petal Length
fig, ax = plt.subplots(1, 3, sharex= True, sharey= True)
ax[0].hist(setosa['petal_length_cm'], edgecolor = 'black', alpha = 1.0, bins = 7)
ax[1].hist(versicolor['petal_length_cm'], label = 'Iris versicolor', color = 'orange', edgecolor = 'black', alpha = 1.0, bins = 7)
ax[2].hist(virginica['petal_length_cm'], label = 'Iris virginica', color = 'green', edgecolor = 'black', alpha = 1.0, bins = 7)

ax[0].set_xlabel('Petal length (cm) \nIris setosa')
ax[1].set_xlabel('Petal length (cm), \nIris versicolor')
ax[2].set_xlabel('Petal length (cm), \nIris virginica')
ax[0].set_ylabel('No of instances')

fig.suptitle('Histogram of Petal Length by Iris species')

#plt.savefig('petal_length.png')
plt.show()

# Histogram of Petal Width
fig, ax = plt.subplots(1, 3, sharex= True, sharey= True)
ax[0].hist(setosa['petal_width_cm'], edgecolor = 'black', alpha = 1.0, bins = 7)
ax[1].hist(versicolor['petal_width_cm'], label = 'Iris versicolor', color = 'orange', edgecolor = 'black', alpha = 1.0, bins = 7)
ax[2].hist(virginica['petal_width_cm'], label = 'Iris virginica', color = 'green', edgecolor = 'black', alpha = 1.0, bins = 7)

ax[0].set_xlabel('Petal Width (cm) \nIris setosa')
ax[1].set_xlabel('Petal Width (cm), \nIris versicolor')
ax[2].set_xlabel('Petal Width (cm), \nIris virginica')

ax[0].set_ylabel('Count')
ax[1].set_ylabel('Count')
ax[2].set_ylabel('Count')

fig.suptitle('Histogram of Petal Width by Iris species')

#plt.savefig('petal_width.png')
plt.show()

# Histogram of Sepal Length by species. 
fig, ax = plt.subplots()
ax.hist(setosa['sepal_length_cm'], label = 'Iris setosa', edgecolor = 'black', alpha = 0.4, bins = 7)
ax.hist(versicolor['sepal_length_cm'], label = 'Iris versicolor', edgecolor = 'black', alpha = 0.4, bins = 7)
ax.hist(virginica['sepal_length_cm'], label = 'Iris virginica', edgecolor = 'black', alpha = 0.4, bins = 7)
ax.set_title('Histogram of sepal length for Iris species')
ax.set_xlabel('Sepal length (cm)')
ax.set_ylabel('Count')
ax.legend()
plt.savefig('sepal_length_overlap.png')
plt.show()