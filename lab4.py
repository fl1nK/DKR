import random



def task1(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return "Орієнтований" + '\n'
    return "Неорієнтований" + '\n'


def get_graph_list(matrix):
    res = []
    for i in range(len(matrix)):
        res.append([])
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                res[i].append(j)
    return res


def printCircuit(adj):
    print('Ейлерів шлях: ')
    if len(adj) == 0:
        return
    curr_path = [0]
    circuit = []
    while curr_path:
        curr_v = curr_path[-1]
        if adj[curr_v]:
            next_v = adj[curr_v].pop()
            curr_path.append(next_v)
        else:
            circuit.append(curr_path.pop())

    for i in range(len(circuit) - 1, -1, -1):
        print(circuit[i], end="")
        if i:
            print(" -> ", end="")
    print('\n')
    if circuit[0] == circuit[-1]:
        print("Також є Єйлерів цикл")


def dijkstra(N, S, matrix):
    print('граф: ', matrix)
    valid = [True] * N
    weight = [1000000] * N
    weight[S] = 0
    for i in range(N):
        min_weight = 1000001
        ID_min_weight = -1
        for j in range(N):
            if valid[j] and weight[j] < min_weight:
                min_weight = weight[j]
                ID_min_weight = j
        for z in range(N):
            if weight[ID_min_weight] + matrix[ID_min_weight][z] < weight[z]:
                weight[z] = weight[ID_min_weight] + matrix[ID_min_weight][z]
        valid[ID_min_weight] = False
    return weight


def get_graph_for_dijkstra(graph):
    res = []
    for i in range(len(graph)):
        res.append([])
        for j in range(len(graph)):
            if graph[i][j] == 1:
                res[i].append(random.randint(1, 10))
            else:
                res[i].append(10000000)
    return res




PRIORITY = {1: ['+', '-'], 2: ['*', '/']}


def priority(value: str) -> int:
    for k, v in PRIORITY.items():
        if value in v:
            return k
    return -1


def infix_to_postfix(expression):


    OPERATORS = {'+', '-', '*', '/', '(', ')', '^'}
    PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = ''
    for ch in expression:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output += stack.pop()
            stack.append(ch)

    while stack:
        output += stack.pop()

    return output


OPERATORS = {'*', '-', '+', '%', '/', '^'}


def evaluate_postfix(expression):
    stack = []
    res = []
    for i in expression:
        if i not in OPERATORS:
            stack.append(i)
        else:

            a = stack.pop()
            b = stack.pop()
            if i == '+':
                res = int(b) + int(a)
            elif i == '-':
                res = int(b) - int(a)
            elif i == '*':
                res = int(b) * int(a)
            elif i == '%':
                res = int(b) % int(a)
            elif i == '/':
                res = int(b) / int(a)
            elif i == '^':
                res = int(b) ** int(a)
            print(b, i, a, '=', res)
            stack.append(res)
    return (''.join(map(str, stack)))


def postfix_to_prefix(expression):
    ops = ['*', '-', '+', '%', '/', '^']
    res = ''
    tmp = ''
    for i in range(len(expression) - 1, -1, -1):
        res += expression[i]

    res1 = ''
    for i in range(len(res)):
        if res[i] in ops:
            res1 += (''.join(list(reversed(tmp))))
            tmp = ''
            res1 += res[i]
        else:
            tmp += res[i]
    res1 += (''.join(list(reversed(tmp))))
    return res1

graph = [[0, 1, 0, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 1], [1, 0, 0, 0, 1]]

print(task1(graph))

printCircuit(get_graph_list(graph))

print('найкоротша відстань від першої до останньої вершини: ', dijkstra(5, 0, get_graph_for_dijkstra(graph))[-1], '\n')

expression = '5^2+8/2*(7-4)'
print('вираз: ', expression)
print('зворотній польскький запис: ', infix_to_postfix(expression))
print('прямий польський запис: ', postfix_to_prefix(infix_to_postfix(expression)))
print(evaluate_postfix(infix_to_postfix(expression)), '\n')