import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 100)

def fractional_flow_model(x):
    return 0.01*np.exp(-0.03*x)

    plt.plot(x, model(x))
    plt.show()

def crm_model():

    y0 = 0
    u0 = 0
    nt = 1000
    dt = 1/nt
    K = 1
    tau = 0.08
    u = np.zeros(nt)
    u[10:] = 100
    u[600:] = 50
    eo_total = 100
    A = 0.01
    B = -0.03
    time = np.linspace(0, 1, nt)

    y_model = []
    eo_model = []
    eo_frac = []
    y_prev = 0
    eo_prev = 0

    for i, t in enumerate(time):
        flow = np.exp(-dt/tau)*(y_prev-y0) + K*(1-np.exp(-dt/tau))*(u[i] - u0)
        y_model.append(flow)
        eo_yield = A*np.exp(B*eo_prev)
        eo_frac.append(eo_yield)
        eo_model.append(eo_prev + eo_yield*flow)
        y_prev = y_model[-1]
        eo_prev = eo_model[-1]

    plt.subplot(3, 1, 1)
    plt.plot(time, y_model, label='model')
    plt.plot(time, u, label='u')
    plt.legend()
    plt.subplot(3, 1, 2)
    plt.plot(time, eo_model)
    plt.subplot(3, 1, 3)
    plt.plot(time, eo_frac)
    plt.show()


if __name__ == "__main__":
    crm_model()
