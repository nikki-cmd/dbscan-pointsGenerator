import random

def get_distance_arr(point_id, data, eps):
    """
    Calculate indices of points within `eps` distance from the given point.
    """
    point = data[point_id]
    dist_arr = []
    for i in range(len(data)):
        distance = ((data[i][0] - point[0]) ** 2 + (data[i][1] - point[1]) ** 2) ** 0.5
        if distance < eps:
            dist_arr.append(i)
    return dist_arr

def calc(data, eps, min_samples):
    """
    Perform DBSCAN clustering on the input data.
    """
    data_tags = [{'point': p, 'visited': False, 'core': False, 'cluster': None} for p in data]
    cluster_id = 0

    for i in range(len(data_tags)):
        if data_tags[i]['visited']:
            continue

        data_tags[i]['visited'] = True
        neighbors = get_distance_arr(i, data, eps)

        if len(neighbors) < min_samples:
            # Mark as noise (not part of any cluster)
            data_tags[i]['cluster'] = -1
        else:
            # Expand cluster
            cluster_id += 1
            expand_cluster(data_tags, i, neighbors, cluster_id, eps, min_samples)

    # Return cluster assignments
    return [tag['cluster'] for tag in data_tags]

def expand_cluster(data_tags, point_id, neighbors, cluster_id, eps, min_samples):
    """
    Expand a cluster by iterating through neighbors.
    """
    data_tags[point_id]['cluster'] = cluster_id
    data_tags[point_id]['core'] = True

    i = 0
    while i < len(neighbors):
        neighbor_id = neighbors[i]

        if not data_tags[neighbor_id]['visited']:
            data_tags[neighbor_id]['visited'] = True
            new_neighbors = get_distance_arr(neighbor_id, [tag['point'] for tag in data_tags], eps)

            if len(new_neighbors) >= min_samples:
                neighbors += new_neighbors

        if data_tags[neighbor_id]['cluster'] is None:
            data_tags[neighbor_id]['cluster'] = cluster_id

        i += 1
