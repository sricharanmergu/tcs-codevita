import sys
def solve():
	try:
    N, M = map(int,sys.stdin.readline().split())
    grid = []
    for _ in range(N):
    	grid,append(list(sys.stdin.readline().strip()))
        except EOFError:
        retrun
        except Exception as e:
        	return
        total_cost = 0
        def calculate_segment_cost(segment):
        	if not segment:
            	return 0
            groups = []
            if segment[0] != '.':
            	groups.append(segment[0])
            for i in range(1, len(segment)):
            	if segment[i] != '.':
                	if segment[i] != segment[i-1] and segment[i-1] != '.':
            groups.append(segment[i])
            r_groups = groups.count('R')
            c_groups = groups.count('C')
            
            if r_groups > 0 and c_groups > 0:
            	return min(r_groups, c-groups)
            return 0
    	for r in range(N):
        row = grid[r]
        segment = []
        for c in range(M):
        	char = row[c]
            if char != '.': segment.append(char)
            else:
            total_cost += claculate_segment_cost(segment)
            
		for c in range(M):
        	segment = []
            for r in range(N):
            	char = grid[r][c]
                if char != '.': segment.append(char)
                else:
                total_cost += claculate_segment_cost(segment)
                segment = []
                total_cost += claculate_segment_cost(segment)
                print(total_cost)
                if __name__ == "__main__":
                	solve()
