import matplotlib.pyplot as plt

states = ['NY', 'CA', 'VA', 'TX', 'OH', 'MD', 'DC']
positive = [412, 400, 78, 346, 76, 79, 11]

plt.title('Coronavirus Cases in Various States')

plt.xlabel('States')
plt.ylabel('Coronavirus Cases by Thousands')
plt.bar(states, positive, color = 'lightblue', label = 'Cases by the Thousand')
plt.legend(facecolor = 'lightgreen')

plt.show()