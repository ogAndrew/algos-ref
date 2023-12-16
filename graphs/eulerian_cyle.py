
def check_if_eulerian_cycle_exists(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     bool
    """
    # Write your code here.
    # Create a list `degree` of length n initialized with zeros.
    degree = [0] * n
    
    #iterate through each edge in the edges list.
    for edge in edges:
        #increment the degree of both vertices of the edge
        degree[edge[0]] += 1 
        degree[edge[1]] += 1
    #check if any vertex has an odd degree.
    for d in degree:
        if d % 2 != 0:
            #if any vertex has an odd degree(Eulerian cycle doesn't exist)
            return False
    #if all vertices have even degree (Eulerian cycle exists)
    return True