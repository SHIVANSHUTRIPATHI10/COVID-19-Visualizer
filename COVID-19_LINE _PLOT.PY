import matplotlib.pyplot as plt
data = ('january', 'feberuary', 'march', 'april', 'may', 'june')
confirmed = (1000,12000,18000,25000,42000,61000)
recovered = (200,1200,7000,15000,32000,45000)
deaths = [50, 300, 1000, 2000, 4000, 6000]
plt.figure(figsize=(10, 6))
plt.plot(data,confirmed,label = 'confirmed cases',color = 'orange',linewidth = 2,marker = 'o')
plt.plot(data,recovered,label = 'Recovered case',color = 'green',linewidth = 2,marker = 's')
plt.plot(data,deaths,label = 'death cases',linewidth = 2,color = 'red',marker = '^')

plt.fill_between(data,deaths,color ='red',alpha = 0.2)
# Add title and labels
plt.title("COVID-19 Cases Over 6 Months", fontsize=23)
plt.xlabel("months",fontsize = 13)
plt.ylabel("number of cases",fontsize = 13)

plt.grid(True,linestyle = '-',alpha = 0.5)
plt.tight_layout()
plt.legend()
plt.show()