from gekko import GEKKO
import pandas as pd
import matplotlib.pyplot as plt

# load data and parse into columns
data       = pd.read_csv('trial2.csv')
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

fo = open("params.txt","w")
fo.write(str(p))