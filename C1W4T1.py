#modified notebook to run graph comparison as a function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts
from math import sqrt

mu = 15
sigma = 15
normal = sts.norm(loc=mu, scale=sigma)
maxwell = sts.maxwell(loc=mu, scale=sigma)

x1 = np.linspace(-50, 80, 1000)
pdf1 = normal.pdf(x1)

x2 = np.linspace(-50, 80, 1000)
pdf2 = maxwell.pdf(x2)

plt.plot(x1, pdf1, label='norm')
plt.plot(x2, pdf2, label='maxwell')
plt.ylabel('pdf')
plt.xlabel('x')
plt.legend()
plt.show()


#MAXWELL 5, 15, 125, 625
def build_graph(mu, sigma, n):
    maxwell = sts.maxwell(loc=mu, scale=sigma)
    maxwell_hist = [maxwell.rvs(n).mean() for x in range(1000)]
    plt.hist(maxwell_hist, density=True, alpha=0.5, color='r', label='Sample_hist n=5')

    x_maxwell = np.linspace((maxwell.expect()-4*sqrt(maxwell.std())), (maxwell.expect()+4*sqrt(maxwell.std())), 1000)
    maxwell_norm = sts.norm(maxwell.expect(), sqrt(maxwell.var()/n))
    pdf_maxwell = maxwell_norm.pdf(x_maxwell)
    plt.plot(x_maxwell, pdf_maxwell, label='Norm', color='black')
    plt.ylabel('pdf')
    plt.xlabel('x')
    plt.legend()
    plt.show()

build_graph(15, 15, 5);
build_graph(15, 15, 25);
build_graph(15, 15, 125);
build_graph(15, 15, 625);

#maxwell.expect() #ожидаемое среднее
#sqrt(maxwell.std()) #сигма = корень из дисперсии
