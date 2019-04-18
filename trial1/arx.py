from gekko import GEKKO
import pandas as pd
import matplotlib.pyplot as plt

# load data and parse into columns
data1       = pd.read_csv('trial1.csv')
t_m1        = data1['Time (min)']
eo_m1       = data1['Oil (mL)']
hydrosol_m1 = data1['Hydrosol (mL)']
u_m1        = data1['u (Temp sp)']

# generate time-series model
m1 = GEKKO()

# system identification
na = 3 # output coefficients
nb = 3 # input coefficients
yp1,p1,K1 = m1.sysid(t_m1,u_m1,eo_m1,na,nb,diaglevel=1)

# load data and parse into columns
data2       = pd.read_csv(r'..\trial7\trial7.csv')
t_m2        = data2['Time (min)']
eo_m2       = data2['Oil (mL)']
hydrosol_m2 = data2['Hydrosol (mL)']
u_m2        = data2['u (Temp sp)']

# generate time-series model
m2 = GEKKO()

# system identification
na = 3 # output coefficients
nb = 3 # input coefficients
yp2,p2,K2 = m2.sysid(t_m2,u_m2,eo_m2,na,nb,diaglevel=1)

plt.figure(figsize=(10,10))
plt.subplot(2,1,1)
#plt.title("ARX Comparison",fontsize=15)
plt.plot(t_m1,u_m1,linewidth=2,label='u')
#plt.plot(t_m2,u_m2,linewidth=2,label='u7')
plt.ylabel("Heat Output (Temp SP)",fontsize=15)
plt.legend()
plt.subplot(2,1,2)
plt.plot(t_m1,eo_m1,linewidth=2,label='Data')
plt.plot(t_m1,yp1,linewidth=2,label='Model')
#plt.plot(t_m2,yp2,linewidth=2,label='model7')
plt.ylabel("Volume of Oil Collected (mL)",fontsize=15)
plt.legend()
plt.xlabel('Time',fontsize=15)
plt.savefig('sysid.png')
plt.show()

#fo = open("params.txt","w")
#fo.write(str(p))