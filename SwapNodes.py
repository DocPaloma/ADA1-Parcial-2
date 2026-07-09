import os


def inorder(node, indexes, result):
    
    if node == -1:
        return
        
    left, right = indexes[node -1]
    
    inorder(left, indexes, result)
    
    result.append(node)
    
    inorder(right, indexes, result)
    
def swap(node, depth, k, indexes):
    if node == -1:
        return
    
    if depth % k == 0:
        indexes[node - 1][0], indexes[node - 1][1] = indexes[node - 1][1], indexes[node - 1][0]
    
    left, right = indexes[node -1]
    
    swap(left, depth + 1, k, indexes)
    
    swap(right, depth + 1, k, indexes)

def swapNodes(indexes, queries):
    result = []
    
    for k in queries:
        
        swap(1, 1, k, indexes)
        
        recorrido = []
        
        inorder(1, indexes, recorrido)
        
        result.append(recorrido)
    
    return result



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
