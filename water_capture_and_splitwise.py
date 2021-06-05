
# Problem 1
# Example 1: [1,8,6,2,5,4,8,3,7]  -> 1,8
# [1, 1, 2, 1000, 1000]
# [1,1,1,1]
# [1]
# None

# 1 -> [1,8,6,2,5,4,8,3,10000, 7]
# Approach 1: tc: O(n^2)
# Approach 2: using two pointers. tc: O(n)


def solution(walls):
    if walls is None:
        raise Exception('Invalid input.')
    head_idx = 0
    tail_idx = len(walls) - 1
    area = 0
    sol_idx = ()
    while head_idx < tail_idx:
        min_length = min(walls[head_idx], walls[tail_idx])
        width = tail_idx - head_idx
        curr_area = min_length * width
        if curr_area > area:
            sol_idx = (head_idx, tail_idx)
            area = curr_area
        if min_length == walls[head_idx]:
            head_idx += 1
        else:
            tail_idx -= 1
    return sol_idx, area


#tests = [[1,8,6,2,5,4,8,3,7], [1, 1, 2, 1000, 1000], [1,1,1,1], [1], None]

#for data in tests:
#    print(data, solution(data))



# Problem2: A,B,C are three friends. Settle debts with minimal transactions
# 1. A ---50----> B
#  [-50, 50, 0]
#--> A: -50, B: 50
# 2. B ---30----> C
#--> B: 20, C: 30, A: -50
# [-50, 20, 30]
# 3. C ---50----> A
#--> B:20 C:-20  A:0
#  [0, 20, -20]
# Soln: B --20--> C

# [120, -60, -60, -10, 30, -10, -10]

# def sol(values):
#     final = 0
#     for value in values:
#         transaction[values[0]] = values[1]
#         final -= values[2]



####################################################################################

import typing


def solution2(transactions: typing.Sequence[typing.Tuple[str, str, float]]):
    # T = O(N), S = O(N)
    amount_by_users = {p: 0 for transaction in transactions for p in transaction[:2]}
    for src, dst, amt in transactions:
        amount_by_users[src] -= amt
        amount_by_users[dst] += amt

    final_transactions = []
    # T = O(NlogN), S = O(N)
    transaction_users = sorted(amount_by_users.keys(), key=lambda p: amount_by_users.get(p))
    payee_idx = 0
    payer_idx = len(transaction_users) - 1
    # T = O(N), S = O(N)
    while payee_idx < payer_idx:
        payee = transaction_users[payee_idx]
        payer = transaction_users[payer_idx]
        if amount_by_users[payee] < 0:
            balance = amount_by_users[payee] + amount_by_users[payer]
            if balance >= 0:
                paid = abs(amount_by_users[payee])
                amount_by_users[payer] = balance
                amount_by_users[payee] = 0
                payee_idx += 1
            else:
                amount_by_users[payee] = balance
                paid = amount_by_users[payer]
                payer_idx -= 1
            final_transactions.append((payer, payee, paid))
        elif amount_by_users[payee] == 0:
                payee_idx += 1
        else:
            break
    return final_transactions


inputs = ((('A', 'B', 50), ('B', 'C', 30), ('C', 'A', 50)),
          (('A', 'B', 50), ('B', 'C', 40), ('C', 'A', 20), ('C', 'D', 10), ('D', 'E', 5)),
          (('A', 'B', 10), ('B', 'C', 20), ('C', 'A', 40), ('C', 'D', 60), ('D', 'E', 90)))

for ins in inputs:
    print(solution2(ins))
