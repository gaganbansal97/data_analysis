Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> stats = pd.read_csv('C:\\Users\\a\\Desktop\\Python Training\\Demographic Data\\P4-Demographic-Data.csv')
>>> stats.head()
           Country Name Country Code  ...  Internet users         Income Group
0                 Aruba          ABW  ...            78.9          High income
1           Afghanistan          AFG  ...             5.9           Low income
2                Angola          AGO  ...            19.1  Upper middle income
3               Albania          ALB  ...            57.2  Upper middle income
4  United Arab Emirates          ARE  ...            88.0          High income

[5 rows x 5 columns]
>>> #----FILTERING DAATAFRAMES__________________
>>> 
>>> # FILTERING ABOUT ROWS
>>> 
>>> stats.InternetUsers < 2
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    stats.InternetUsers < 2
  File "C:\Users\a\AppData\Local\Programs\Python\Python38-32\lib\site-packages\pandas\core\generic.py", line 5274, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'InternetUsers'
>>> stats.columns= ['CountryName', 'CountryCode',
		'BirthRate', 'InternetUsers', 'IncomeGroup']
>>> stats.InternetUsers < 2
0      False
1      False
2      False
3      False
4      False
       ...  
190    False
191    False
192    False
193    False
194    False
Name: InternetUsers, Length: 195, dtype: bool
>>> Filter = stats.InternetUsers < 2
>>> Filter
0      False
1      False
2      False
3      False
4      False
       ...  
190    False
191    False
192    False
193    False
194    False
Name: InternetUsers, Length: 195, dtype: bool
>>> stats[Filter]
      CountryName CountryCode  BirthRate  InternetUsers          IncomeGroup
11        Burundi         BDI     44.151            1.3           Low income
52        Eritrea         ERI     34.800            0.9           Low income
55       Ethiopia         ETH     32.925            1.9           Low income
64         Guinea         GIN     37.337            1.6           Low income
117       Myanmar         MMR     18.119            1.6  Lower middle income
127         Niger         NER     49.661            1.7           Low income
154  Sierra Leone         SLE     36.729            1.7           Low income
156       Somalia         SOM     43.891            1.5           Low income
172   Timor-Leste         TLS     35.755            1.1  Lower middle income
>>> stats.BirthRate > 40
0      False
1      False
2       True
3      False
4      False
       ...  
190    False
191    False
192     True
193     True
194    False
Name: BirthRate, Length: 195, dtype: bool
>>> Filter2 = stats.BirthRate>40
>>> stats[Filter2]
          CountryName CountryCode  ...  InternetUsers          IncomeGroup
2              Angola         AGO  ...           19.1  Upper middle income
11            Burundi         BDI  ...            1.3           Low income
14       Burkina Faso         BFA  ...            9.1           Low income
65        Gambia, The         GMB  ...           14.0           Low income
115              Mali         MLI  ...            3.5           Low income
127             Niger         NER  ...            1.7           Low income
128           Nigeria         NGA  ...           38.0  Lower middle income
156           Somalia         SOM  ...            1.5           Low income
167              Chad         TCD  ...            2.3           Low income
178            Uganda         UGA  ...           16.2           Low income
192  Congo, Dem. Rep.         COD  ...            2.2           Low income
193            Zambia         ZMB  ...           15.4  Lower middle income

[12 rows x 5 columns]
>>> Filter and Filter2
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    Filter and Filter2
  File "C:\Users\a\AppData\Local\Programs\Python\Python38-32\lib\site-packages\pandas\core\generic.py", line 1478, in __nonzero__
    raise ValueError(
ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
>>> #_____________WE HAVE GOT ABOVE ERROR AS "and" fuinction only takes single value, in this line may values are present in each list(Filter and Filter2
>>> 0
0
>>> Filter & Filter2
0      False
1      False
2      False
3      False
4      False
       ...  
190    False
191    False
192    False
193    False
194    False
Length: 195, dtype: bool
>>> stats[Filter & Filter2]
    CountryName CountryCode  BirthRate  InternetUsers IncomeGroup
11      Burundi         BDI     44.151            1.3  Low income
127       Niger         NER     49.661            1.7  Low income
156     Somalia         SOM     43.891            1.5  Low income
>>> stats[(stats.BirthRate > 40)&(stats.InternetUsers<2)]
    CountryName CountryCode  BirthRate  InternetUsers IncomeGroup
11      Burundi         BDI     44.151            1.3  Low income
127       Niger         NER     49.661            1.7  Low income
156     Somalia         SOM     43.891            1.5  Low income
>>> #____________ANOTHER ONE____________
>>> 
>>> stats[stats.IncomeGroup == 'High Income']
Empty DataFrame
Columns: [CountryName, CountryCode, BirthRate, InternetUsers, IncomeGroup]
Index: []
>>> stats[stats.IncomeGroup == 'High income']
               CountryName CountryCode  BirthRate  InternetUsers  IncomeGroup
0                    Aruba         ABW     10.244          78.90  High income
4     United Arab Emirates         ARE     11.044          88.00  High income
5                Argentina         ARG     17.716          59.90  High income
7      Antigua and Barbuda         ATG     16.447          63.40  High income
8                Australia         AUS     13.200          83.00  High income
..                     ...         ...        ...            ...          ...
174    Trinidad and Tobago         TTO     14.590          63.80  High income
180                Uruguay         URY     14.374          57.69  High income
181          United States         USA     12.500          84.20  High income
184          Venezuela, RB         VEN     19.842          54.90  High income
185  Virgin Islands (U.S.)         VIR     10.700          45.30  High income

[67 rows x 5 columns]
>>> # ________HOW TO GET UNIQUE CATEGORIES____
>>> 
>>> stats.IncomeGroup.unique()
array(['High income', 'Low income', 'Upper middle income',
       'Lower middle income'], dtype=object)
>>> stats[stats.CountryName = 'Malta']
SyntaxError: invalid syntax
>>> stats[stats.CountryName == 'Malta']
    CountryName CountryCode  BirthRate  InternetUsers  IncomeGroup
116       Malta         MLT        9.5        68.9138  High income
>>> 
>>> 
>>> ###__________ACCESSING INDIVIDUAL ELEMENTS_____
>>> # .at   #FOR LABELS. Note: INTEGERS are treated as labels
>>> # .iat    FOR INTEGER LOCATION
>>> 
>>> stats.iat[3,4]
'Upper middle income'
>>> stats.head()
            CountryName CountryCode  ...  InternetUsers          IncomeGroup
0                 Aruba         ABW  ...           78.9          High income
1           Afghanistan         AFG  ...            5.9           Low income
2                Angola         AGO  ...           19.1  Upper middle income
3               Albania         ALB  ...           57.2  Upper middle income
4  United Arab Emirates         ARE  ...           88.0          High income

[5 rows x 5 columns]
>>> stats.iat[0,0]
'Aruba'
>>> stats.at[1,1]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    stats.at[1,1]
  File "C:\Users\a\AppData\Local\Programs\Python\Python38-32\lib\site-packages\pandas\core\indexing.py", line 2178, in __getitem__
    key = self._convert_key(key)
  File "C:\Users\a\AppData\Local\Programs\Python\Python38-32\lib\site-packages\pandas\core\indexing.py", line 2219, in _convert_key
    raise ValueError(
ValueError: At based indexing on an non-integer index can only have non-integer indexers
>>> stats.at[2,'BirthRate']
45.985
>>> 
>>> 
>>> 
>>> #--INTRO TO SEABORN-----------
>>> import matplotlib.pyplot
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    import seaborn as sns
ModuleNotFoundError: No module named 'seaborn'
>>> import seaborn as sns
>>> #DISTRIBUTION------------
>>> vis1=sns.distplot(stats['InternetUsers'])
>>> plt.show
<function show at 0x08799898>
>>> plt.show()
>>> vis2 = sns.boxplot(sata=stats, x="IncomeGroup", y="BirthRate")
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    vis2 = sns.boxplot(sata=stats, x="IncomeGroup", y="BirthRate")
  File "C:\Users\a\AppData\Local\Programs\Python\Python38-32\lib\site-packages\seaborn\categorical.py", line 2233, in boxplot
    plotter = _BoxPlotter(x, y, hue, data, order, hue_order,
  File "C:\Users\a\AppData\Local\Programs\Python\Python38-32\lib\site-packages\seaborn\categorical.py", line 436, in __init__
    self.establish_variables(x, y, hue, data, orient, order, hue_order)
  File "C:\Users\a\AppData\Local\Programs\Python\Python38-32\lib\site-packages\seaborn\categorical.py", line 152, in establish_variables
    raise ValueError(err)
ValueError: Could not interpret input 'IncomeGroup'
>>> vis2 = sns.boxplot(data=stats, x="IncomeGroup", y="BirthRate")
>>> plt.show()
>>> 
>>> 
>>> 
>>> 
>>> vis3 = sns.lmplot(data = stats, x="InternetUsers", y='BirthRate')
>>> plt.show()
>>> vis3 = sns.lmplot(data = stats, x="InternetUsers", y='BirthRate', 	fit_regr=False)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    vis3 = sns.lmplot(data = stats, x="InternetUsers", y='BirthRate', 	fit_regr=False)
TypeError: lmplot() got an unexpected keyword argument 'fit_regr'
>>> vis3 = sns.lmplot(data = stats, x="InternetUsers", y='BirthRate', 	fit_reg=False)
>>> plt.show()
>>> vis3 = sns.lmplot(data = stats, x="InternetUsers", y='BirthRate', 	fit_reg=False, hue = "IncomeGroup")
pl
>>> plt.show()
>>> 
>>> 
>>> 
>>> #-------KEYWORDS ARGUMNETSS IN PYTHON
>>> 
>>> # markersize
>>> 
>>> vis3 = sns.lmplot(data = stats, x="InternetUsers", y='BirthRate', 	fit_reg=False, hue = "IncomeGroup" size=8, scatter_kws={"s":100})
SyntaxError: invalid syntax
>>> vis3 = sns.lmplot(data = stats, x="InternetUsers", y='BirthRate', 	fit_reg=False, hue = "IncomeGroup", size=8, scatter_kws={"s":100})

Warning (from warnings module):
  File "C:\Users\a\AppData\Local\Programs\Python\Python38-32\lib\site-packages\seaborn\regression.py", line 573
    warnings.warn(msg, UserWarning)
UserWarning: The `size` parameter has been renamed to `height`; please update your code.
>>> vis3 = sns.lmplot(data = stats, x="InternetUsers", y='BirthRate', 	fit_reg=False, hue = "IncomeGroup", size=8, scatter_kws={"s":100})
>>> vis3 = sns.lmplot(data = stats, x="InternetUsers", y='BirthRate', 	fit_reg=False, hue = "IncomeGroup", height=8, scatter_kws={"s":100})
>>> plt.show()
>>> 