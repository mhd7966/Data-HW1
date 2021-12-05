import pickle
import numpy as np

def eucl_dist(a, b, axis=1):
    return np.linalg.norm(a - b, axis=axis)

def k_mean(x, k):

    cluster = np.zeros(x.shape[0])

    minv = np.min(x,axis=0)
    maxv = np.max(x,axis=0)

    error = 0

    center = np.zeros((k, x.shape[1]))
    for i in range(k):
        for j in x.shape[1]:
            center[i,j] = np.random.randint(minv, maxv)

    center_old = np.zeros(center.shape)

    err = eucl_dist(center, center_old, None)

    while err != 0:

        for i in range(len(x)):
            distances = eucl_dist(x[i], center)
            clust = np.argmin(distances)
            cluster[i] = clust

        center_old = np.copy(center)

        for i in range(k):
            points = [x[j] for j in range(len(x)) if cluster[j] == i]
            if points:
                center[i] = np.mean(points, axis=0)

        err = eucl_dist(center, center_old, None)

    for i in range(k):
        d = [eucl_dist(x[j],center[i],None) for j in range(len(x)) if cluster[j] == i]
        error += np.sum(d)

    count = {key: 0.0 for key in range(k)}
    for i in range(len(x)):
        count[cluster[i]] += 1

    print k, error/len(x), count

    return cluster

if name == 'main':

    inp = pickle.load(open('test.pickle', 'rb'))
    x = np.array([i[0] for i in inp])

    cluster = k_mean(x, 5)