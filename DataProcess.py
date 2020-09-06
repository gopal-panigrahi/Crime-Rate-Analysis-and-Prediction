'''
	Consists of various Data Processing operations such as Data Cleaning
	and Multiple Linear Regression for Prediction in near future
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import *

'''
	This function Plots and Predicts Number of Crimes  in Future.
	It takes inputs from user like Gender , State, Crime , Age and a Future year
	and creates a model which gives the expected count of crimes
'''
def plotting(State,Crime,Year,Age,Gender):
	Gender=Gender[0]
	if Crime in ['Attempt To Murder', 'Riots', 'Arson', 'Robbery', 'Dacoity', 'Dowry Deaths', 'Preparation & Assembly For Dacoity', 'Molestation', 'Sexual Harassment', 'Cruelty By Husband And Relatives', 'Importation Of Girls', 'Immoral Traffic (Prevention) Act', 'Indecent Representation Of Women (Prohibition) Act']:
			minage=1
			maxage=100
	else:
		if Age <10:
			maxage = 9
			minage = 1
		elif Age >=10 and Age<14:
			maxage = 13
			minage = 10
		elif Age >=14 and Age<18:
			maxage = 17
			minage = 14
		elif Age >=18 and Age<30:
			maxage = 29
			minage = 18
		elif Age >=30 and Age<50:
			maxage = 50
			minage = 30
		else:
			maxage=100
			minage = 51

	X=df1.drop(['#Cases'],axis=1)

	Y=df1['#Cases']

	model=LinearRegression()

	reg = model.fit(X,Y)

	col = df1.columns.tolist()
	col.remove('#Cases')

	attributes=[Year,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	if State!='West Bengal':
		attributes[col.index(State)]=1
	if Gender!='M':
		attributes[col.index('F')]=1
	if maxage!=100:
		attributes[col.index(maxage)]=1
	if minage!=1:
		attributes[col.index(minage)]=1
	if Crime!='Sexual Harassment':
		attributes[col.index(Crime)]=1

	output=reg.predict([attributes])


	df2=df[(df['State/UT']==State)&(df['Crimes']==Crime)&(df['MaxAge']==maxage)&(df['MinAge']==minage)&(df['Gender']==Gender)]
	yr = [str(i) for i in df2['Year'].tolist()]
	plt.scatter(df2['Year'].tolist(),df2['#Cases'].tolist(),label=Crime)
	plt.xlabel('YEAR')
	plt.ylabel('Number Of Cases')
	plt.title(Crime,fontsize=20,style='italic',family='serif')
	plt.legend(loc='upper left')
	plt.xticks(df2['Year'].tolist(),yr)
	plt.savefig('Images/plot.png',dpi=95,bbox='tight')
	plt.clf()
	return round(output[0])

'''
	Returns Sample Dirty Data from the Dataset
	Records shows how the data can be scattered
'''
def retrieve_dirty():
	records=[]
	records.append(dirtydf2.columns.tolist())
	for i in range(9):
		row = dirtydf2.iloc[i].tolist()
		nrow = [str(i) for i in row]
		records.append(nrow)
	return records

'''
	Returns Sample Clean Data from the Dataset
	Records shows how the data can be scattered
'''
def retrieve_clean():
	global dirtydf

	del dirtydf['Total']

	dirtydf.loc[dirtydf['STATE/UT']=='A&N Islands','STATE/UT']='Andaman & Nicobar Islands'
	dirtydf.loc[dirtydf['STATE/UT']=='Delhi UT','STATE/UT']='Delhi'
	dirtydf.loc[dirtydf['STATE/UT']=='D&N Haveli','STATE/UT']='Dadra & Nagar Haveli'

	col_name = ['State/UT','Year','Gender','1-9','10-13','14-17','18-29','30-50','51-100']

	dirtydf.columns=col_name

	dirtydf.fillna(0,inplace=True)
	
	dirtydf.drop(dirtydf.index[dirtydf['Gender']=='Total'],axis=0,inplace=True)

	dirtydf['Crimes']='Murder'

	dirtydf=pd.melt(dirtydf,id_vars=['State/UT','Year','Gender','Crimes'],var_name='Age',value_name='#Cases')

	newcols = dirtydf['Age'].str.split('-',expand=True)

	newcols.columns=['MinAge','MaxAge']

	dirtydf=pd.concat([dirtydf,newcols],axis=1)

	del dirtydf['Age']

	col_name = dirtydf.columns.tolist()

	col_name = ['State/UT','Year','Gender','MaxAge','MinAge','Crimes','#Cases' ]

	dirtydf = dirtydf[col_name]


	dirtydf['MinAge']=dirtydf['MinAge'].astype(int)
	dirtydf['MaxAge']=dirtydf['MaxAge'].astype(int)

	dirtydf.loc[dirtydf['Gender']=='Male','Gender']='M'
	dirtydf.loc[dirtydf['Gender']=='Female','Gender']='F'

	records=[]
	records.append(dirtydf.columns.tolist())
	for i in range(9):
		row = dirtydf.iloc[i].tolist()
		nrow = [str(i) for i in row]
		records.append(nrow)
	return records
'''
	This function calculates the statistics of the data(eg mean,median,count etc)
	and return for displaying on screen
'''
def eda():
	global dirtydf
	edadata = dirtydf[['MaxAge','MinAge','#Cases']].describe()
	records = [['','MaxAge','MinAge','#Cases']] + edadata.index.tolist()
	for i in range(8):
		row = edadata.iloc[i].tolist()
		records[i+1] = [records[i+1]]+row
	return records

dirtydf=pd.read_csv('Datasets/VOM 2001-2012.csv')
dirtydf2=pd.read_csv('Datasets/VOM 2001-2012.csv')
df = pd.read_csv('Datasets/Final Dataset.csv')
df2=pd.get_dummies(df['State/UT'])
del df2['West Bengal']
df1=df
df1=pd.concat([df1,df2],axis=1)
del df1['State/UT']
df2=pd.get_dummies(df['Crimes'])
del df2['Sexual Harassment']
df1=pd.concat([df1,df2],axis=1)
del df1['Crimes']
df2=pd.get_dummies(df['Gender'])
del df2['M']
df1=pd.concat([df1,df2],axis=1)
del df1['Gender']
df2=pd.get_dummies(df['MaxAge'])
del df2[100]
df1=pd.concat([df1,df2],axis=1)
del df1['MaxAge']
df2=pd.get_dummies(df['MinAge'])
del df2[1]
df1=pd.concat([df1,df2],axis=1)
del df1['MinAge']

del df2