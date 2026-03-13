graph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6', '7'],
    '4': [],
    '5': [],
    '6': [],
    '7': [],
}

visited=[]
stack = []

def dfs(visited,graph,node):
    visited.append(node)
    stack.append(node)

    while stack:
        m = stack.pop()
        print(m, end="")

        for n in reversed(graph[m]):
            if n not in visited:
                visited.append(n)
                stack.append(n)

dfs(visited,graph,'1')