import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (10, 5))
plt.subplot(1,2,1)

x_labels = ['Smeets 2016', 'Lin 2017','Park 2017']

# Create dummy x values, with a value for every label entry
x = np.r_[:len(x_labels)]
Res_MPS = [8.4, 4, 5.6]
Res_KES = [23.7, 21.1, 21.1]

Eff_MPS = [3.27E-4, 6.63E-5, 5.68E-4]
Eff_KES = [1.20E-3, 4.66E-4, 2.10E-3]

plt.plot(x,Eff_MPS,linestyle='-',marker='o',label="MPS")
plt.plot(x,Eff_KES,linestyle='-',marker='^',label="KES")
plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
plt.legend()

plt.xticks(x, x_labels)
plt.ylabel('Efficiency')
plt.ylim((0,2.25E-3))

## Second plot
plt.subplot(1,2,2)

plt.plot(x,Res_MPS,linestyle='-',marker='o',label="MPS")
plt.plot(x,Res_KES,linestyle='-',marker='^',label="KES")
plt.legend()

# Change the xticks as desired
plt.xticks(x, x_labels)
plt.ylabel('Resolution (mm)')
plt.ylim((0,25))

plt.show()

fig.savefig("Literature.pdf")
