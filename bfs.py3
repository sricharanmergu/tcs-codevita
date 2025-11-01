import sys
from collections import deque

def solve():
    try:
        n_line = sys.stdin.readline().strip()
        if not n_line:
            return
        n = int(n_line)

        sys.stdin.readline()
        shuffled_list = []
        for _ in range(n):
            shuffled_list.append(sys.stdin.readline().strip())
        start_state = tuple(shuffled_list)

        sys.stdin.readline()
        original_list = []
        for _ in range(n):
            original_list.append(sys.stdin.readline().strip())
        target_state = tuple(original_list)

        if start_state == target_state:
            print(0)
            return

        queue = deque([(start_state, 0)])
        visited = {start_state}

        while queue:
            current_state_tuple, cost = queue.popleft()
            current_list = list(current_state_tuple)
            n_len = len(current_list)
            for i in range(n_len):
                for j in range(i, n_len):
                    segment_to_move = current_list[i : j + 1]
                    remaining_list = current_list[:i] + current_list[j + 1:]
                    for k in range(len(remaining_list) + 1):
                        if k == i:
                            continue
                        new_list = remaining_list[:k] + segment_to_move + remaining_list[k:]
                        new_state_tuple = tuple(new_list)
                        if new_state_tuple == target_state:
                            print(cost + 1)
                            return
                        if new_state_tuple not in visited:
                            visited.add(new_state_tuple)
                            queue.append((new_state_tuple, cost + 1))
    except EOFError:
        pass
    except Exception as e:
        pass

solve()
