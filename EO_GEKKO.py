import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as plt

eofile = '''time,oil,hydro,u
0.0,0.0,0.001,550
10.0,1.6,117,550
20.0,2.5,201,465
30.0,3.0,282,415
40.0,3.0,322,385
50.0,4.0,345,365
60.0,4.0,372,355
70.0,4.0,392,350
80.0,4.0,407,345
90.0,4.0,426,340
100.0,4.0,445,340
'''

fid = open('data.csv','w')
fid.write(eofile)
fid.close()

m = GEKKO()

nt = 101
m.time = np.linspace(0,100,nt)

eo_collect = m.CV(value=0,lb=0)
eo_collect.STATUS = 1

usp = np.zeros(nt)
usp[0:]=550
#usp[10:]=500

u = m.MV(value=usp,lb=340,ub=550)
u.STATUS = 1
u.DMAX = 4

flow = m.Var(value=10,lb=0)
eo_frac = m.Var(value=0.01,lb=0)
eo_tot = m.Var(value=0,lb=0)

K = m.FV(value=0.0198)
tau = m.FV(value=2.85)
theta = m.FV(value=0.1)
A = m.Param(value=0.009)
B = m.Param(value=-1.1029)

p = np.zeros(nt)
p[-1] = 100.0
final = m.Param(value=p)

m.Equation(eo_tot.dt() == eo_collect)
m.Equation(tau * flow.dt() == -flow + K * u)
m.Equation(eo_frac == A*m.exp(B*eo_tot))
m.Equation(eo_collect == flow*eo_frac)

m.Obj(-eo_tot)
m.Obj(u)


m.options.IMODE = 6
#eo_yeild.STATUS = 1
#eo_yeild.FSTATUS = 1
m.solve()


#eo_tot = np.zeros(nt)
#for i in range(nt-1):
#	eo_tot[i+1] = eo_collect[i+1] + eo_tot[i]

plt.figure()
plt.subplot(4,1,1)
plt.plot(m.time,eo_frac.value)
plt.ylabel('eo_frac')
plt.subplot(4,1,2)
plt.plot(m.time,eo_tot.value)
plt.ylabel('eo_collect')
plt.subplot(4,1,3)
plt.plot(m.time,flow.value)
plt.ylabel('flow')
plt.subplot(4,1,4)
plt.plot(m.time,u.value)
plt.ylabel('u')
plt.xlabel('time')
plt.show()

print(eo_frac.value)
