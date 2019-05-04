# Pandas: powerful Python data analysis toolkit, Release 0.24.2

import numpy as np
import pandas as pd

## Create series by passing list of values; Pandas creates defaul integer index
s = pd.Series([1,3,4,np.nan,6,8])
#print(s)


## Create DataFrame by passing a NumPy array, wiht datetime index and labeled columns
dates = pd.date_range('20130101', periods=6)
#print(dates)
## .randn generates number from normal (Gaussian) distribution; 
## generate array index + 6y, 4x
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
#print(df)

##                   A         B         C         D
##2013-01-01 -2.353663 -0.682054  0.342326  1.105452
##2013-01-02  0.779095 -0.504246  0.479368  1.527086
##2013-01-03  0.369629 -0.893179  0.836324  0.715014
##2013-01-04 -1.259110  1.468122 -2.309988 -0.532411
##2013-01-05 -0.847186 -0.792407  0.354179  0.372700
##2013-01-06  0.328138 -1.086908  0.473596 -0.512442


## Create DataFrame by passing a dict of objects that be converted to series-like
## all arrays must be same length
#df2 = pd.DataFrame({'A': 1.,
#                    'B': pd.Timestamp('20130102'),
#                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
#                    'D': np.array([3] * 4, dtype='int32'),
#                    'E': pd.Categorical(["test", "train", "test", "train"]),
#                    'F': 'foo'})
#print(df2)

## Show column data types
#print(df2.dtypes)
##    A           float64
##    B    datetime64[ns]
##    C           float32
##    D             int32
##    E          category
##    F            object
##    dtype: object

#print(df.index)
    #DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
    #               '2013-01-05', '2013-01-06'],
    #              dtype='datetime64[ns]', freq='D')

## Data statistics
#print(df.describe())
##                  A         B         C         D
##    count  6.000000  6.000000  6.000000  6.000000
##    mean   0.575435 -0.079601  0.672154 -0.464231
##    std    1.050562  1.209965  0.964800  1.415339
##    min   -1.312383 -1.457512 -0.556824 -1.807526
##    25%    0.446816 -1.166484 -0.126297 -1.595666
##    50%    0.705740  0.083003  0.962756 -0.692530
##    75%    1.073270  0.711318  1.357166  0.253489
##    max    1.797224  1.476122  1.664917  1.735082

## Transpose data
#print(df.T)

## Sort by axis
#df.sort_index(axis=1, ascending=True)
#df.sort_index(axis=0, ascending=False)
#df.sort_values(by='B')


## Select a single column, i.e., a series or df.A
#print(df['C'])
#
### Slice the rows via []
print(df)
#print(df[0:3]) ## First three rows
#print()
#print(df[3:6]) ## Last three rows
#print(df[3:])  ## Last three rows
#print(df[:3])  ## First three rows


## Returns values in row 0
#print(df.loc[dates[0]])

## Returns values in several columns
#print(df.loc[:, ['A','B']])






#print(df)