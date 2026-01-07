def get_room(arr):
    h,w,n = arr[0], arr[1], arr[2]
    
    # 2차원 배열
    rooms = [[0]*w for _ in range(h)]
    for i in range(len(rooms)):
        for j in range(len(rooms[i])):
            rooms[i][j] = 100 * (h-i) + (j+1)
    
    # 호실
    col = n // h
    row = n % h
    
    print(rooms[h-row][col])

def solve(): 
    # 입력
    n = int(input())
    arr = [] 
    for i in range(n):
        arr.append(list(map(int,input().split())))
    
    # 출력
    for row in arr:
        get_room(row)


if __name__ == "__main__":
    solve()
    
            