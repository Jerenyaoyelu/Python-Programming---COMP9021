for dim in [10, 50, 100, 1000]:
    for for_seed in [0, 1, 2]:
        for n in [-4, -3, -2, -1, 1, 2, 3, 4]:
            def produce_8(pts):
                x=pts[0]
                y=pts[1]
                #print(x,y)
                coordinate=[(x-i, y-j) for i in [-2, -1, 1, 2] for j in [-2, -1, 1, 2] if i!=j and (i**2+j**2)==5 and ( (x-i>=0 and x-i<=dim-1) and ( y-j>=0 and y-j<=dim-1))]
                return coordinate

            def explore_board(pts):
                x=pts[0]
                y=pts[1]
                if grid[x][y]==0:
                    return {()}
                else:
                    grid[x][y]=0
                    related_pts=produce_8(pts)
                    #print(related_pts)
                    pts_set_l=[explore_board(e) for e in related_pts]
                    s={(x,y)}
                    for k in pts_set_l:
                        if k!={()}:
                            s=s|k
                    return s
            seed(for_seed)
            if n > 0:
                grid = [[randrange(n) > 0 for _ in range(dim)] for _ in range(dim)]
            else:
                grid = [[randrange(-n) == 0 for _ in range(dim)] for _ in range(dim)]    
            nb_of_knights=len([explore_board((i,j)) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j]==1 and explore_board((i,j))!={()}])
            print(f'dim: {dim:<4},   for_seed: {for_seed},   n: {n:2} ---> knights: {nb_of_knights}')
