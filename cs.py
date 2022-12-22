from numpy import *
from numpy import linalg as la
import random
import numpy as np
import scipy
import cvxpy as cvx

# f = open("data.txt", "r", encoding="utf8")
# lines = f.readlines()
# for i in range (len(lines)):
#     lines[i] = lines[i][:-1].split(" ")
#     for j in range(len(lines[i])):
#         lines[i][j] = eval(lines[i][j])
lines = np.loadtxt("data.txt")
print("read finished")
def reconstruct(sample, n, time_idx):
    Psi = la.inv(scipy.fft.dct(eye(n, n)))
    # A = Phi @ Psi
    A = Psi[time_idx]
    vx = cvx.Variable(n)
    # sample = sample.reshape(1, -1).tolist()
    # sample = sample[0]
    objective = cvx.Minimize(cvx.norm(vx, 1))
    constraints = [A @ vx == sample]
    prob = cvx.Problem(objective, constraints)
    result = prob.solve()
    return scipy.fft.ifft(vx.value)
    
def cs(lines, sample_num, modal_num):
    n = len(lines)
    time_idx = np.random.choice(n, sample_num, replace=False)
    time_idx.sort()
    Phi = np.zeros((sample_num, n), dtype=float)
    for i in range(sample_num):
        Phi[i][time_idx[i]] = 1
    # cur_data = []
    # for i in time_idx:
    #     cur_data.append(lines[i])
    # cur_data = mat(cur_data)
    # cur_data = np.transpose(cur_data)
    cur_data = lines[time_idx].T
    U, S, V = la.svd(cur_data, full_matrices=0)
    new_v = V[:modal_num, :]
    new_u = U[:, :modal_num]
    new_s = S[:modal_num]
    new_s = np.diag(new_s)
    ret_v = np.zeros((modal_num, n), dtype=float)
    for i in range(modal_num):
        ret_v[i] = reconstruct(new_v[i], n, time_idx)
    return np.transpose(new_u @ new_s @ ret_v)

# f2 = open("out.txt", "w", encoding="utf8")
# output = cs(lines, 500, 2).tolist()
# print("cs finished")
# for i in range(len(output)):
#     tmp = [str(x) for x in output[i]]
#     string1 = " ".join(tmp)
#     f2.write(string1+"\n")
# # f.close()
# f2.close()
output = cs(lines, 500, 2)
np.savetxt("out.txt", output)

    