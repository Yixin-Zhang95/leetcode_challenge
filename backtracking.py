def A_n_k(a, n, k, depth, used, curr, ans):
    if depth == k:  # end condition
        ans.append(curr[::])  # use deepcopy because curr is tracking all partial solution, it eventually become []
        return

    for i in range(n):
        if not used[i]:
            # generate the next solution from curr
            curr.append(a[i])
            used[i] = True
            print(curr)
            # move to the next solution
            A_n_k(a, n, k, depth + 1, used, curr, ans)

            # backtrack to previous partial state
            curr.pop()
            print('backtrack: ', curr)
            used[i] = False
    return


a = [1, 2, 3]
n = len(a)
ans = [[None]]
used = [False] * len(a)
ans = []
A_n_k(a, n, n, 0, used, [], ans)
print(ans)
