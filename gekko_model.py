from gekko import GEKKO()
import numpy as np
import pandas as pd


m         = GEKKO()
nt        = 21
m.time    = np.linspace(0,1,nt)

y         = m.Var(value=0)
eo        = m.Var(value=0)
t         = m.Var()
u_np      = np.zeros(nt)
u_np[1:]  = 100
u_np[15:] = 50
u         = m.Param(u_np)

K         = m.MV(1)
tau       = m.MV(0.08)
theta     = m.MV(0.1)

A         = m.MV(0.01)
B         = m.MV(-0.03)

m.Equation(tau * y.dt() == -y + K * u * (t - theta))
m.Equation(t.dt() == 1)
m.Equation(eo == A * np.exp(B))

#m.sysid(time,u,y"data",na,nb,nk(number of delay cycles))