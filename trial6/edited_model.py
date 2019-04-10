import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import minimize

def get_data(path):
    data     = pd.read_csv(path)
    t        = data['Time (min)']
    eo       = data['Oil (mL)']
    hydrosol = data['Hydrosol (mL)']
    total    = eo + hydrosol
    flow     = np.zeros(len(total))
    for i in range(len(total)-1):
        flow[i+1] = (total[i+1] - total[i]) / (t[i+1] - t[i])
    y        = flow
    y[0]     = 10
    u        = data['u (Temp sp)']
    eo_frac  = eo / total
    'Get data from a file as useable arrays'
    return  np.array([t,u,y,eo_frac,eo])

def model(use_data=False):

    # Fake data for testing the model
    nt = 1000                       # number of time points
    time = np.linspace(0, 1, nt)    # time array - dimensionless
    dt = time[-1]/nt                # time step
    y0 = 0                          # initial condensate flowrate
    u0 = 0                          # initial heat flowrate
    u = np.zeros(nt)                # heat flowrate array
    u[10:] = 100
    u[600:] = 50

    y_data = None
    eo_data = None

    # Data read in from another soure
    if use_data:
        time, u, y_data, eo_data, eo_coll = get_data('trial6.csv')
        #print(time, u, y_data, eo_data)
        nt = len(time)
        dt = (time[-1] - time[0]) / nt
        y0 = y_data[0]
        u0 = 0

    
    def objective(params):
        
        K = params[0] # 0.01000502 # 0.01 params[0]
        tau = params[1] #2.08396  # 0.08 params[1]
        A = params[2] #0.01052282 # 0.0134 params[2]
        B = params[3] #-0.3363548     # -0.07  #params[3]
        

        y_model = np.zeros(nt)                    # condensate flowrates
        eo_frac = np.zeros(nt)                    # condensate eo fraction
        eo_model = np.zeros(nt)                   # collected essential oil
        sse = 0

        y_prev = y0
        u_prev = u0
        eo_prev = 0
        for i, t in enumerate(time):
            if i > 0:
                flow = np.exp(-dt/tau)*(y_prev-y0) + K*(1-np.exp(-dt/tau))*(u_prev-u0)
                y_model[i] = flow
                eo_yield = A*np.exp(B*eo_prev)
                eo_frac[i] = eo_yield
                eo_model[i] = eo_prev + eo_yield*flow
                y_prev = flow
                u_prev = u[i]
                eo_prev = eo_model[i]
                sse = sse +  100*(eo_frac[i] - eo_data[i])**2
                sse = sse + 100*(y_model[i] - y_data[i])**2
        return sse
    params0 = [0.01000502,2.08396,0.01052282,-0.3363548]
    #print(objective(params0))
    #res = minimize(objective, params0, options={"disp":True})
    res = minimize(objective, params0, bounds=[(0,5),(0,30),(-5,5),(-5,5)])
    #print(res)
    K,tau,A,B = res['x']
    
    y_model = np.zeros(nt)                    # condensate flowrates
    eo_frac = np.zeros(nt)                    # condensate eo fraction
    eo_model = np.zeros(nt)                   # collected essential oil
    sse = 0

    y_prev = y0
    u_prev = u0
    eo_prev = 0
    for i, t in enumerate(time):
        if i > 0:
            flow = np.exp(-dt/tau)*(y_prev-y0) + K*(1-np.exp(-dt/tau))*(u_prev-u0)
            y_model[i] = flow
            eo_yield = A*np.exp(B*eo_prev)
            eo_frac[i] = eo_yield
            eo_model[i] = eo_prev + eo_yield*flow
            y_prev = flow
            u_prev = u[i]
            eo_prev = eo_model[i]
    
    plt.figure(figsize=(10,15))
    plt.subplot(3, 1, 1)
    plt.plot(time, u, label='heat')
    plt.ylabel('Heat Profile (Temp SP)')
    plt.subplot(3,1,2)
    plt.plot(time, y_model, label='model')
    if use_data:
        plt.plot(time, y_data, label='data')
    plt.ylabel('Condensate Flow rate')
    plt.legend(loc='best')
    plt.subplot(3, 1, 3)
    plt.plot(time, eo_frac,label='model')
    plt.plot(time,eo_data,label='data')
    plt.legend(loc='best')
    plt.ylabel('Oil fraction in condensate')
    plt.xlabel('Time (min)')
    plt.savefig('edited_model.png')
    plt.show()
    
    fo = open("params.txt","a")
    fo.write('\n\n[K, tau, A, B]\n')
    fo.write(str(res['x']))
    fo.close()
    
    plt.figure(figsize=(10,10))
    plt.plot(time, eo_frac,label='model')
    plt.plot(time,eo_data,label='data')
    plt.legend(loc='best')
    plt.ylabel('Oil fraction in condensate')
    plt.xlabel('Time (min)')
    plt.savefig('edited2.png')
    plt.show()

if __name__ == "__main__":
    model(use_data=True)
