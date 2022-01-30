import numpy as np
import pandas as pd

n = 1 
hora = np.arange(0,24)
day = np.arange(0,3)

d = {'turn': [1, 2, 3], 'shift': ['B', 'C', 'D'], 'begin': [1514012400, 1514041200, 1514070000]}
e = pd.DataFrame(data=d)

ouput = []
for j in day:
    counter=1
    g = e.iloc[j,2]+np.random.rand(n)*300
    for i in hora:
        datos =np.arange(n)
        df =pd.DataFrame(data =datos, columns=["random"])
        df['nro'] = counter
        counter+=1
        df['date'] =pd.to_datetime(g, unit="s")
        g+=1200+np.random.rand(n)*59
        df['shift'] = e.iloc[j,1]
        df['turn'] = e.iloc[j,0]
        df['0PYBW']=1420+np.random.rand(n)*3+np.random.rand(n)*6
        df['3TCPC']=1510+np.random.rand(n)*3+np.random.rand(n)*6
        df['4TCPE']=1530+np.random.rand(n)*3+np.random.rand(n)*6
        df['4TCPW']=1532+np.random.rand(n)*3+np.random.rand(n)*6
        df['8TCRW']=1250+np.random.rand(n)*3+np.random.rand(n)*6
        df['8TCRE']=1255+np.random.rand(n)*3+np.random.rand(n)*6
        df['8TCRU']=1260+np.random.rand(n)*3+np.random.rand(n)*6
        df['8PYRU']=1210+np.random.rand(n)*3+np.random.rand(n)*6
        df['9TCWIE']=42+np.random.rand(n)*2+np.random.rand(n)*2
        df['9TCWIW']=42+np.random.rand(n)*2+np.random.rand(n)*2
        df['9TCWOE']=70+np.random.rand(n)*2+np.random.rand(n)*4
        df['9TCWOW']=70+np.random.rand(n)*1+np.random.rand(n)*4
        ouput.append(df)
ouput=pd.concat(ouput)

# Burning side (it changes every 20 minutes)
ouput['burn_side'] = ouput['nro'].apply(lambda x: 'East' if x % 2 == 0 else 'West')

#Change datatype to integer
ouput['0PYBW']=ouput['0PYBW'].astype(np.int64)
ouput['3TCPC']=ouput['3TCPC'].astype(np.int64)
ouput['4TCPE']=ouput['4TCPE'].astype(np.int64)
ouput['4TCPW']=ouput['4TCPW'].astype(np.int64)
ouput['8TCRW']=ouput['8TCRW'].astype(np.int64)
ouput['8TCRE']=ouput['8TCRE'].astype(np.int64)
ouput['8TCRU']=ouput['8TCRU'].astype(np.int64)
ouput['8PYRU']=ouput['8PYRU'].astype(np.int64)
ouput['9TCWIE']=ouput['9TCWIE'].astype(np.int64)
ouput['9TCWIW']=ouput['9TCWIW'].astype(np.int64)
ouput['9TCWOE']=ouput['9TCWOE'].astype(np.int64)
ouput['9TCWOW']=ouput['9TCWOW'].astype(np.int64)

data=ouput[['nro','date','turn','shift','0PYBW','3TCPC','4TCPE','4TCPW','8TCRW','8TCRE','8TCRU','8PYRU','9TCWIE','9TCWIW','9TCWOE','9TCWOW','burn_side']]
data.to_csv(a+"_GTM.csv",sep=",")
