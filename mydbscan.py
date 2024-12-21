import random
import pandas as pd
    
def get_distance_arr(point_id, data, eps):
    point = data[point_id]
    dist_arr = []
    for i in range(0, len(data)):
        d = ((data[i][0] - point[0])**2 + (data[i][1] - point[1])**2)**0.5
        if d < eps:
            dist_arr.append(i) #data: 0-id, 1-dist
    return dist_arr

def get_distance_value(first_point, second_point):
    return ((first_point[0] - second_point[0])**2 + (first_point[1] - second_point[1])**2)**0.5


def closest_core(dist):
    points = []
    for i in range(0, len(dist)):
        if 'core' in dist[i]:
            return True
        else:
            return False
        
def get_cluster_core(dist):
    for i in range(0, len(dist)):
        if 'core' in dist[i]:
            return dist[i][2]
        
    
def calc(data, eps, min_samples):
    print(len(data))
    for i in range(0, len(data)):
        if 'visited' not in data[i] and 'core' not in data[i]:
            dist = get_distance_arr(i, data, eps)
            if len(dist) >= min_samples:
                data[i].append(random.randint(0, len(data)))
                data[i].append('core')
            elif len(dist) <  min_samples and closest_core(dist):
                data[i].append(get_cluster_core(dist))
                data[i].append(dist['visited'])
        else:
            pass
    print(data)
    return data