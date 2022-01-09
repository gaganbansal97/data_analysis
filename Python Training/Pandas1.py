Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> stats = pd.read_csv('C:\Users\a\Desktop\Python Training\Demographic Data\P4-Demographic-Data.csv')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> stats = pd.read_csv('C:\\Users\\a\\Desktop\\Python Training\\Demographic Data\\P4-Demographic-Data.csv')
>>> 
>>> stats
             Country Name Country Code  ...  Internet users         Income Group
0                   Aruba          ABW  ...            78.9          High income
1             Afghanistan          AFG  ...             5.9           Low income
2                  Angola          AGO  ...            19.1  Upper middle income
3                 Albania          ALB  ...            57.2  Upper middle income
4    United Arab Emirates          ARE  ...            88.0          High income
..                    ...          ...  ...             ...                  ...
190           Yemen, Rep.          YEM  ...            20.0  Lower middle income
191          South Africa          ZAF  ...            46.5  Upper middle income
192      Congo, Dem. Rep.          COD  ...             2.2           Low income
193                Zambia          ZMB  ...            15.4  Lower middle income
194              Zimbabwe          ZWE  ...            18.5           Low income

[195 rows x 5 columns]
>>> import os
>>> print(os.getcwd())
C:\Users\a\AppData\Local\Programs\Python\Python38-32
>>> # Number of rows
>>> len(stats)
195
>>> #see columns
>>> stats.columns
Index(['Country Name', 'Country Code', 'Birth rate', 'Internet users',
       'Income Group'],
      dtype='object')
>>> # see rows
>>> stats.rows
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    stats.rows
  File "C:\Users\a\AppData\Local\Programs\Python\Python38-32\lib\site-packages\pandas\core\generic.py", line 5274, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'rows'
>>> # top rows
>>> stats.head()
           Country Name Country Code  ...  Internet users         Income Group
0                 Aruba          ABW  ...            78.9          High income
1           Afghanistan          AFG  ...             5.9           Low income
2                Angola          AGO  ...            19.1  Upper middle income
3               Albania          ALB  ...            57.2  Upper middle income
4  United Arab Emirates          ARE  ...            88.0          High income

[5 rows x 5 columns]
>>> stats.head(9)
           Country Name Country Code  ...  Internet users         Income Group
0                 Aruba          ABW  ...            78.9          High income
1           Afghanistan          AFG  ...             5.9           Low income
2                Angola          AGO  ...            19.1  Upper middle income
3               Albania          ALB  ...            57.2  Upper middle income
4  United Arab Emirates          ARE  ...            88.0          High income
5             Argentina          ARG  ...            59.9          High income
6               Armenia          ARM  ...            41.9  Lower middle income
7   Antigua and Barbuda          ATG  ...            63.4          High income
8             Australia          AUS  ...            83.0          High income

[9 rows x 5 columns]
>>> #bottom rows
>>> stats.tail()
         Country Name Country Code  ...  Internet users         Income Group
190       Yemen, Rep.          YEM  ...            20.0  Lower middle income
191      South Africa          ZAF  ...            46.5  Upper middle income
192  Congo, Dem. Rep.          COD  ...             2.2           Low income
193            Zambia          ZMB  ...            15.4  Lower middle income
194          Zimbabwe          ZWE  ...            18.5           Low income

[5 rows x 5 columns]
>>> # information on columns
>>> stats.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 195 entries, 0 to 194
Data columns (total 5 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   Country Name    195 non-null    object 
 1   Country Code    195 non-null    object 
 2   Birth rate      195 non-null    float64
 3   Internet users  195 non-null    float64
 4   Income Group    195 non-null    object 
dtypes: float64(2), object(3)
memory usage: 5.4+ KB
>>> # get stats on columns
>>> stats.describe()
       Birth rate  Internet users
count  195.000000      195.000000
mean    21.469928       42.076471
std     10.605467       29.030788
min      7.900000        0.900000
25%     12.120500       14.520000
50%     19.680000       41.000000
75%     29.759500       66.225000
max     49.661000       96.546800
>>> stats.describe().transpose()
                count       mean        std  ...    50%      75%      max
Birth rate      195.0  21.469928  10.605467  ...  19.68  29.7595  49.6610
Internet users  195.0  42.076471  29.030788  ...  41.00  66.2250  96.5468

[2 rows x 8 columns]
>>> ##Renaming columns of dataframes
>>> stats.columns()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    stats.columns()
TypeError: 'Index' object is not callable
>>> stats.columns
Index(['Country Name', 'Country Code', 'Birth rate', 'Internet users',
       'Income Group'],
      dtype='object')
>>> stats.column = ['CountryName', 'CountryCode',
		'BirthRate', 'InternetUsers', 'IncomeGroup']

Warning (from warnings module):
  File "<pyshell#26>", line 1
UserWarning: Pandas doesn't allow columns to be created via a new attribute name - see https://pandas.pydata.org/pandas-docs/stable/indexing.html#attribute-access
>>> stats.columns= ['CountryName', 'CountryCode',
		'BirthRate', 'InternetUsers', 'IncomeGroup']
>>> stats.columns
Index(['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers',
       'IncomeGroup'],
      dtype='object')
>>> ## SUBSETTING DATAFRAMES IN PANDAS
>>> ##-----------ROWS--------------
>>> stats[21:26]
   CountryName CountryCode  BirthRate  InternetUsers          IncomeGroup
21      Belize         BLZ     23.092          33.60  Upper middle income
22     Bermuda         BMU     10.400          95.30          High income
23     Bolivia         BOL     24.236          36.94  Lower middle income
24      Brazil         BRA     14.931          51.04  Upper middle income
25    Barbados         BRB     12.188          73.00          High income
>>> ## REVERSE DATAFRAME
>>> stats[::-1]
              CountryName CountryCode  ...  InternetUsers          IncomeGroup
194              Zimbabwe         ZWE  ...           18.5           Low income
193                Zambia         ZMB  ...           15.4  Lower middle income
192      Congo, Dem. Rep.         COD  ...            2.2           Low income
191          South Africa         ZAF  ...           46.5  Upper middle income
190           Yemen, Rep.         YEM  ...           20.0  Lower middle income
..                    ...         ...  ...            ...                  ...
4    United Arab Emirates         ARE  ...           88.0          High income
3                 Albania         ALB  ...           57.2  Upper middle income
2                  Angola         AGO  ...           19.1  Upper middle income
1             Afghanistan         AFG  ...            5.9           Low income
0                   Aruba         ABW  ...           78.9          High income

[195 rows x 5 columns]
>>> ## GET ONLY 20th Row
>>> ## GET ONLY EVERY 20th Row
>>> stats[::20]
    CountryName CountryCode  BirthRate  InternetUsers          IncomeGroup
0         Aruba         ABW     10.244        78.9000          High income
20      Belarus         BLR     12.500        54.1700  Upper middle income
40   Costa Rica         CRI     15.022        45.9600  Upper middle income
60        Gabon         GAB     30.555         9.2000  Upper middle income
80        India         IND     20.291        15.1000  Lower middle income
100       Libya         LBY     21.425        16.5000  Upper middle income
120  Mozambique         MOZ     39.705         5.4000           Low income
140      Poland         POL      9.600        62.8492          High income
160    Suriname         SUR     18.455        37.4000  Upper middle income
180     Uruguay         URY     14.374        57.6900          High income
>>> ###______________COLUMNS_________________
>>> stats['CountryName']
0                     Aruba
1               Afghanistan
2                    Angola
3                   Albania
4      United Arab Emirates
               ...         
190             Yemen, Rep.
191            South Africa
192        Congo, Dem. Rep.
193                  Zambia
194                Zimbabwe
Name: CountryName, Length: 195, dtype: object
>>> stats[['CountryName', 'BirthRate']]
              CountryName  BirthRate
0                   Aruba     10.244
1             Afghanistan     35.253
2                  Angola     45.985
3                 Albania     12.877
4    United Arab Emirates     11.044
..                    ...        ...
190           Yemen, Rep.     32.947
191          South Africa     20.850
192      Congo, Dem. Rep.     42.394
193                Zambia     40.471
194              Zimbabwe     35.715

[195 rows x 2 columns]
>>> ## ----------QUICK ACCESS - required the name to be one word--------------
>>> stats.Birthrate
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    stats.Birthrate
  File "C:\Users\a\AppData\Local\Programs\Python\Python38-32\lib\site-packages\pandas\core\generic.py", line 5274, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'Birthrate'
>>> stats.BirthRate
0      10.244
1      35.253
2      45.985
3      12.877
4      11.044
        ...  
190    32.947
191    20.850
192    42.394
193    40.471
194    35.715
Name: BirthRate, Length: 195, dtype: float64
>>> #_____________________ COMBINE ROWS AND COLUMNS____________
>>> stats[4:8][["CountryName",'BirthRate']]
            CountryName  BirthRate
4  United Arab Emirates     11.044
5             Argentina     17.716
6               Armenia     13.308
7   Antigua and Barbuda     16.447
>>> stats[["CountryName",'BirthRate']][4:8]
            CountryName  BirthRate
4  United Arab Emirates     11.044
5             Argentina     17.716
6               Armenia     13.308
7   Antigua and Barbuda     16.447
>>> #_______________________BASIC OPERATION WITH DATAFRAMES____________
>>> #MATHEMATICAL OPERATIONS ____________
>>> result = stats.BirthRate * stats.InternetUsers
>>> result
0      808.2516
1      207.9927
2      878.3135
3      736.5644
4      971.8720
         ...   
190    658.9400
191    969.5250
192     93.2668
193    623.2534
194    660.7275
Length: 195, dtype: float64
>>> #ADD COLUMMNS_____________
>>> stats['MyCal'] = stats.BirthRate * stats.InternetUsers
>>> stats.head()
            CountryName CountryCode  ...          IncomeGroup     MyCal
0                 Aruba         ABW  ...          High income  808.2516
1           Afghanistan         AFG  ...           Low income  207.9927
2                Angola         AGO  ...  Upper middle income  878.3135
3               Albania         ALB  ...  Upper middle income  736.5644
4  United Arab Emirates         ARE  ...          High income  971.8720

[5 rows x 6 columns]
>>> stats.MyCal
0      808.2516
1      207.9927
2      878.3135
3      736.5644
4      971.8720
         ...   
190    658.9400
191    969.5250
192     93.2668
193    623.2534
194    660.7275
Name: MyCal, Length: 195, dtype: float64
>>> # REMOVE COLUMN__________________
>>> stats.drop('MyCal', axis = 1)
              CountryName CountryCode  ...  InternetUsers          IncomeGroup
0                   Aruba         ABW  ...           78.9          High income
1             Afghanistan         AFG  ...            5.9           Low income
2                  Angola         AGO  ...           19.1  Upper middle income
3                 Albania         ALB  ...           57.2  Upper middle income
4    United Arab Emirates         ARE  ...           88.0          High income
..                    ...         ...  ...            ...                  ...
190           Yemen, Rep.         YEM  ...           20.0  Lower middle income
191          South Africa         ZAF  ...           46.5  Upper middle income
192      Congo, Dem. Rep.         COD  ...            2.2           Low income
193                Zambia         ZMB  ...           15.4  Lower middle income
194              Zimbabwe         ZWE  ...           18.5           Low income

[195 rows x 5 columns]
>>> # .drop() retuen new object. It does not delete the column
>>> # For deleting the  colummn we use anotheer method
>>> stats = stats.drop('MyCal',1)
>>> stats.head()
            CountryName CountryCode  ...  InternetUsers          IncomeGroup
0                 Aruba         ABW  ...           78.9          High income
1           Afghanistan         AFG  ...            5.9           Low income
2                Angola         AGO  ...           19.1  Upper middle income
3               Albania         ALB  ...           57.2  Upper middle income
4  United Arab Emirates         ARE  ...           88.0          High income

[5 rows x 5 columns]
>>> 