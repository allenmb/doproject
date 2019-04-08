from gekko import GEKKO
import pandas as pd
import matplotlib.pyplot as plt

# load data and parse into columns
data       = pd.read_csv('trial6.csv')
t_m        = data['Time (min)']
eo_m       = data['Oil (mL)']
hydrosol_m = data['Hydrosol (mL)']
u_m        = data['u (Temp sp)']

# generate time-series model
m = GEKKO()

# system identification
na = 3 # output coefficients
nb = 3 # input coefficients
yp,p,K = m.sysid(t_m,u_m,eo_m,na,nb,diaglevel=1)

plt.figure()
plt.subplot(2,1,1)
plt.plot(t_m,u_m,label='u')
plt.legend()
plt.subplot(2,1,2)
plt.plot(t_m,eo_m,label='meas')
plt.plot(t_m,yp,label='model')
plt.legend()
plt.xlabel('Time')
plt.savefig('sysid.png')
plt.show()

print(p)
print(K)
'''
from gekko import GEKKO
import pandas as pd
import matplotlib.pyplot as plt

# load data and parse into columns
url = 'http://apmonitor.com/do/uploads/Main/tclab_dyn_data2.txt'
data = pd.read_csv(url)
t = data['Time']
u = data[['H1','H2']]
y = data[['T1','T2']]

# generate time-series model
m = GEKKO(remote=False) # remote=True for MacOS

# system identification
na = 2 # output coefficients
nb = 2 # input coefficients
yp,p,K = m.sysid(t,u,y,na,nb,diaglevel=1)

'''