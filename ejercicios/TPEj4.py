import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

def p(x):
    return st.norm.pdf(x, loc=40, scale=6)


def q(x):
    return st.norm.pdf(x, loc=50, scale= 20)


x = np.arange(-50, 151)
k = max(p(x) / q(x))


def rejection_sampling(iter=1000):
    samples = []

    for i in range(iter):
        z = np.random.normal(50, 20)
        u = np.random.uniform(0, k*q(z))

        if u <= p(z):
            samples.append(z)

    return np.array(samples)


if __name__ == '__main__':
    plt.plot(x, p(x), label = 'target distribution')
    plt.plot(x, k*q(x), label = 'proposed distribution')
    plt.legend(loc='upper left')
    plt.show()
    print('Rejection sampling in progress..')
    s = rejection_sampling(iter=100000)
    mean = round(s.mean(), 2)
    var = round(s.var(), 2)
    print('La media de la muestra generada es: '+str(mean)+', y la varianza: '+str(var))
    plt.plot(x, p(x), label = 'target distribution', color = 'red')
    plt.hist(s, label = 'histogram rejection sampling', normed=True)
    plt.legend(loc='upper left')
    plt.show()

