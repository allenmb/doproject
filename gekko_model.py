from gekko import GEKKO
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data       = pd.read_csv(r'.\trial6\trial6.csv')
t_m        = data['Time (min)']
eo_m       = data['Oil (mL)']
hydrosol_m = data['Hydrosol (mL)']
u_m        = data['u (Temp sp)']

m          = GEKKO()
nt         = len(t_m)
m.time     = np.linspace(0,10,5)

y          = m.Var(value=0)
eo_frac    = m.Var(value=0)
eo_prev    = m.Param(value=0)
u          = m.MV(value=0)
u.FSTATUS = 1
u.STATUS = 0

K          = m.MV(1)
tau        = m.MV(0.08)
K.STATUS  = 1
tau.STATUS = 1
#theta     = m.MV(0.1) took out dead time because measured data starts at passover

A          = m.MV(0.01)
B          = m.MV(-0.03)
A.STATUS  = 1
B.STATUS  = 1

eo_flow = m.Intermediate(eo_frac * y)
m.Equation(tau * y.dt() == -y + K * u)
m.Equation(eo_frac == A * m.exp(B * eo_prev))

m.Obj((y - eo_m+hydrosol_m)**2)
m.Obj((eo_flow - eo_m)**2)
m.options.IMODE = 5

#Arrays for storage
eo_flow    = np.zeros(len(t_m))
eo_frac    = np.zeros(len(t_m))
flow       = np.zeros(len(t_m))
K_plt      = np.zeros(len(t_m))
tau_plt    = np.zeros(len(t_m))
A_plt      = np.zeros(len(t_m))
B_plt      = np.zeros(len(t_m))

for i in range(len(t_m)):
    u.MEAS = u_m[i]
    m.solve()
    
    flow[i]       = y.value[-1]
    A_plt[i]      = A.value[-1]
    B_plt[i]      = B.value[-1]
    K_plt[i]      = K.value[-1]
    tau_plt[i]    = tau.value[-1]
    eo_frac[i]    = eo_yield.value[-1]
    eo_prev.value = eo_yield.value[-1]
    
plt.figure()
plt.subplot(4,1,1)
plt.plot(t_m,eo_flow,label='eo_flow')
plt.plot(t_m,eo_frac,label='eo_frac')
plt.legend()
plt.subplot(4,1,2)
plt.plot(t_m,flow,label='flow')
plt.legend()
plt.subplot(4,1,3)
plt.plot(t_m,K_plt,label='K')
plt.legend()
plt.subplot(4,1,4)
plt.plot(t_m,A_plt,label='A')
plt.plot(t_m,B_plt,label='B')
plt.plot(t_m,tau_plt,label='tau')
plt.legend()
plt.show()
plt.savefig('model.png')

#m.sysid(time,u,y"data",na,nb,nk(number of delay cycles))