import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def get_data(path='fake_data.csv'):
    'Get data from a file as useable arrays'
    return  np.loadtxt(path, delimiter=',', usecols=(0, 1, 2, 3), skiprows=1, unpack=True)

def model(use_different_fake_data=False):

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

    # Fake data read in from another soure
    if use_different_fake_data:
        time, u, y_data, eo_data = get_data()
        print(time, u, y_data, eo_data)
        nt = len(time)
        dt = (time[-1] - time[0]) / nt
        y0 = y_data[0]
        u0 = u[0]

    u_func = interp1d(time, u)

    # System parameters
    K = 1.1                           # FOPDT gain
    tau = 0.08                      # FOPDT time constant
    theta = 0.1                     # FOPDT deadtime
    A = 0.01                        # Fractional flow pre-exponential constant
    B = -0.03                       # Fractional flow exponential constant

    y_model = []                    # condensate flowrates
    eo_frac = []                    # condensate eo fraction
    eo_model = []                   # collected essential oil

    y_prev = 0
    eo_prev = 0
    for i, t in enumerate(time):
        u_val = 0
        if (t-theta) >= 0:
            u_val = u_func(t-theta)
        flow = np.exp(-dt/tau)*(y_prev-y0) + K*(1-np.exp(-dt/tau))*(u_val)
        y_model.append(flow)
        eo_yield = A*np.exp(B*eo_prev)
        eo_frac.append(eo_yield)
        eo_model.append(eo_prev + eo_yield*flow)
        y_prev = y_model[-1]
        eo_prev = eo_model[-1]

    plt.subplot(3, 1, 1)
    plt.plot(time, y_model, label='condensate')
    if use_different_fake_data:
        plt.plot(time, y_data, label='condensate data')
    plt.plot(time, u, label='heat')
    plt.ylabel('Flow rates')
    plt.legend()
    plt.subplot(3, 1, 2)
    plt.plot(time, eo_frac)
    plt.ylabel('Oil fraction in condensate')
    plt.subplot(3, 1, 3)
    plt.plot(time, eo_model)
    plt.ylabel('Essential oil collected')
    plt.xlabel('time (dimensionless)')
    plt.show()


if __name__ == "__main__":
    model(use_different_fake_data=False)
