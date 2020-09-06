'''
	Contains code for plotting graphs
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''
	Displays State Wise Toatal Count of all Crimes
	over the year 2001 to 2010
	Plots a Bar Graph 
'''
def state_wise_count():
	lbl = [i[0] for i in stateswise_crime]
	x = list(range(len(stateswise_crime)))
	y = [i[1] for i in stateswise_crime]

	plt.title('STATE WISE TOTAL COUNT OF CRIMES',fontsize=20,style='italic',family='serif')
	plt.xlabel('STATES AND UNION TERRITORIES ------->')
	plt.ylabel('NUMBER OF CRIMES ------->')
	plt.xticks(x,lbl,rotation=85)
	plt.bar(x,y,label='States/UT',color='g')
	plt.tight_layout()
	plt.legend()
	plt.savefig('Images/statewise_crime_distribution.png',bbox_inches='tight',dpi=70)
	plt.clf()

'''
	Lists TOP 5 Safest States
'''
def safestcities():
	safest = tosort_stateswise_crime[:5]

	lbl = [i[0] for i in safest]
	x = list(range(len(safest)))
	y = [i[1] for i in safest]

	plt.title('TOP 5 SAFEST STATES/UT',fontsize=18,style='italic',family='serif')
	plt.xlabel('STATES AND UNION TERRITORIES ------->')
	plt.ylabel('NUMBER OF CRIMES ------->')
	plt.xticks(x,lbl)
	plt.bar(x,y,label='States/UT',color='#8080ff',width=0.5)
	plt.legend(loc = "upper left")
	plt.savefig('Images/top5safestcities.png',bbox_inches='tight',dpi=72)
	plt.clf()

'''
	Lists TOP 5 Dangerous Cities
'''

def dangercity():

	dangerous = tosort_stateswise_crime[-5:]
	lbl = [i[0] for i in dangerous]
	x = list(range(len(dangerous)))
	y = [i[1] for i in dangerous]

	plt.title('TOP 5 DANGEROUS STATES/UT',fontsize=20,style='italic',family='serif')
	plt.xlabel('STATES AND UNION TERRITORIES ------->')
	plt.ylabel('NUMBER OF CRIMES ------->')
	plt.xticks(x,lbl)
	plt.bar(x,y,label='States/UT',color='#8080ff',width=0.5)
	plt.legend(loc='upper left')
	plt.savefig('Images/top5dangerouscities.png',bbox_inches='tight',dpi=70)
	plt.clf()

'''
	Total Percentage of crimes against Male And Female (2001 - 2012)
	Donut plot
'''
def male2female():

	pieval =[crimebygender['F'],crimebygender['M']]
	lbl = ['Female','Male']
	my_circle=plt.Circle( (0,0), 0.7, color='white')
	p=plt.gcf()
	p.gca().add_artist(my_circle)
	plt.title('CRIMES AGAINST MALE V/S FEMALE\n (2001-2010)',fontsize=20,style='italic',family='serif')
	plt.pie(pieval,labels=lbl,colors=['r','b'],explode=[0,0.1],shadow=True,autopct='%0.2f%%')
	plt.axis('equal')
	plt.savefig('Images/male2female.png',bbox_inches='tight',dpi=70)
	plt.clf()

'''
	Display the Percentage of Major crimes over the years 2001 - 2010
	
'''
def major_crime():
	crimeval=[crimedict["Murder"],crimedict['Rape'],crimedict['Kidnap'],crimedict['Robbery'],crimedict['Dacoity']]
	lbl=["Murder","Rape",'Kidnap','Robbery','Dacoity']

	plt.title('MAJOR CRIMES \n IN YEAR\n (2001-2010)',fontsize=20,style='italic',family='serif')
	plt.pie(crimeval,labels=lbl,shadow=True,autopct='%0.2f%%',explode=[0.08,0.09,0,0,0])
	plt.axis('equal')
	plt.plot()
	plt.savefig("Images/major_crime.png",bbox_inches='tight',dpi=70)
	plt.clf()    

'''
	It gives the trend of crime rates over the years 2001 to 2010
'''
def total_crime():
	years = []
	cases = []
	for key,values in yeardict.items():
		years.append(key)
		cases.append(values)
	plt.xlabel('YEAR ------->')
	plt.ylabel('NUMBER OF CRIMES ------->')   
	plt.title('TOTAL NUMBER OF CRIME \n IN YEARS FROM\n 2001-2010',fontsize=20,style='italic',family='serif')    

	plt.plot(years,cases)
	plt.xticks(years,years)
	plt.savefig("Images/total_crime.png",bbox_inches='tight',dpi=65)
	plt.clf()

TOTAL_RECORDS = 21751

df = pd.read_csv('Datasets/Final Dataset.csv')

stlist={}
for i in df['State/UT'].unique().tolist():
    stlist[i]=0

for i in range(TOTAL_RECORDS):
    row = df.iloc[i].tolist()
    stlist[row[0]]+=row[6]

tosort_stateswise_crime=[]
for key,value in sorted(stlist.items(),key=lambda kv : kv[1]):
	tosort_stateswise_crime.append([key,value])

stateswise_crime=[]
for key,value in stlist.items():
	stateswise_crime.append([key,value])

crimebygender = {'F':0,'M':0}
for i in range(TOTAL_RECORDS):
    row = df.iloc[i].tolist()
    crimebygender[row[2]]+=row[6]

crimedict={}
    
for i in df['Crimes'].unique().tolist():
	crimedict[i]=0
for i in range(TOTAL_RECORDS):
	row = df.iloc[i].tolist()            
	crimedict[str(row[5])]+=row[6]

yeardict={}

for i in df['Year'].unique().tolist():
	yeardict[i]=0
for i in range(TOTAL_RECORDS):
	row = df.iloc[i].tolist()
	yeardict[row[1]]+=row[6]

del yeardict[2011],yeardict[2012],yeardict[2013]