from queue_adt import *
from copy import copy, deepcopy

# class maze(Exception):
#     def __init__(self):
#         pass
class MazeError(Exception):
    def __init__(self,message):
        self.message = message
class Maze:
    #Python will raise a FileNotFoundError exception, that does not need to be caught
    #so, do I need this part of code?
#     if not os.path.exists(filename):
#         #raise FileNotFoundError
#         sys.exit()
    maze_data = None
    maze_result = None
    def __init__(self,filename):
        self.filename = filename 
        self.maze_data = self._data_validity()
    def _read_file(self):
        with open (self.filename) as f:
            file = f.read()
        f_l = file.split('\n')
        file_data = []
        #no spaces between digits
        for e in f_l:
            t = []
            if e.split()!= []:
                for digit in e.split():
                    #error: contain non-number element
                    for d_e in digit:
                        if d_e not in {'0','1','2','3'}:
                            raise MazeError('Incorrect input.')
                        else:
                            t.append(int(d_e))
                    #若digit是0002这样的字符，直接用int就会丢掉三个0，然后导致行宽不一致而报错
#                     if int(digit) > 3:
#                         for i in range(len(digit)):
#                             t.append(int(digit[i]))
#                     else:
#                         t.append(int(digit))
                file_data.append(t)
        return file_data
    def _data_validity(self):
        f_data = self._read_file()
        #error: contain too many or too few lines
        if len(f_data) > 41 or len(f_data) <2:
            raise MazeError('Incorrect input.')
        #error: no 2 or 3 in the last line
        for e in f_data[-1]:
            if e in [2,3]:
                raise MazeError('Input does not represent a maze.')
        width = len(f_data[0])
        for line in f_data:
            #error: no 1 or 3 in the last digit of each line
            if line[-1] in [1,3]:
                raise MazeError('Input does not represent a maze.')
            #error: two of its nonblank lines contain different number of digits
            if len(line) != width:
                raise MazeError('Incorrect input.')
            #error: contain too many or too few digits
            if len(line) > 31 or len(line) < 2:
                raise MazeError('Incorrect input.')
        return f_data
    
    def find_gates(self):
        count = 0
        for dig in self.maze_data[0][:-1]:
            if dig in [0,2]:
                count += 1
        for dig in self.maze_data[-1][:-1]:
            if dig in [0,2]:
                count += 1
        for i in range(len(self.maze_data)-1):
            if self.maze_data[i][0] in [0,1]:
                count += 1
        for i in range(len(self.maze_data)-1):
            if self.maze_data[i][-1] in [0,1]:
                count += 1
        return count
    def leaves_dict(self,pnt):
        d = {1:(0,1),
             2:(1,0)
            }
        if self.maze_data[pnt[0]][pnt[1]] == 3:
            move1 = d[1]
            move2 = d[2]
            return (pnt[0]+ move1[0],pnt[1]+ move1[1]),(pnt[0]+ move2[0],pnt[1]+ move2[1])
        else:
            move = d[self.maze_data[pnt[0]][pnt[1]]]
            return (pnt[0]+ move[0],pnt[1]+ move[1])
    
    def find_walls(self):
        queue = Queue()
        sets_of_walls = []
        for i in range(len(self.maze_data)):
            for j in range(len(self.maze_data[0])):
                if self.maze_data[i][j] > 0:
                    wall = set()
                    old_wall = set()
                    queue.enqueue((i,j))
                    while not queue.is_empty():
                        pt = queue.dequeue()
                        wall.add(pt)
                        if self.maze_data[pt[0]][pt[1]] == 0:
                            continue
                        if self.maze_data[pt[0]][pt[1]] == 3:
                            next_pt1,next_pt2 = self.leaves_dict(pt)
                            queue.enqueue(next_pt1)
                            queue.enqueue(next_pt2)
                        else:
                            next_pt = self.leaves_dict(pt)
                            queue.enqueue(next_pt)
                    #case 1: when visiting some wall, if 0 is encountered the visit
                        #will stop, however the wall may be not ended up yet
                        #So, to avoid this, if some 0 is a part of some previously
                        #visited wall, then the wall we are visiting is a part of that wall.
                    #case 2: to see if any leave point is a part of some wall
                    #case 3: to see if the starting point is a part of some wall
                    remove_l = []
                    for k in range(len(sets_of_walls)):
                        if sets_of_walls[k] & wall:
                            wall = wall | sets_of_walls[k]
                            remove_l.append(sets_of_walls[k])
                    for re_e in remove_l:
                        sets_of_walls.remove(re_e)
                    sets_of_walls.append(wall)
        return sets_of_walls
#     #nodes in help_metrix
#     class help_block:
#         def __init__(self,surrended_nodes = [],way_to_go = None,is_gate = False):
#             self.surrended_nodes = surrended_nodes
#             self.way_to_go = way_to_go
#             self.is_gate = is_gate
    def help_metrix(self):
        help_metrix = []
        property_dict = {}
        for i in range(len(self.maze_data)-1):
            row = []
            for j in range(len(self.maze_data[0])-1):
                ways = 4
                direction = ['L','R','U','D']
                gate = 0
                if self.maze_data[i][j+1] in [2,3]:
                    ways -=1
                    direction.remove('R')
                if self.maze_data[i+1][j] in [1,3]:
                    ways -=1
                    direction.remove('D')
                if self.maze_data[i][j] == 1:
                    ways -=1
                    direction.remove('U')
                if self.maze_data[i][j] == 2:
                    ways -=1
                    direction.remove('L')
                if self.maze_data[i][j] == 3:
                    ways -=2
                    direction.remove('U')
                    direction.remove('L')
                if i == 0 and 'U' in direction:
                    gate +=1
                if i == len(self.maze_data)-2 and 'D' in direction:
                    gate +=1
                if j == 0 and 'L' in direction:
                    gate +=1
                if j == len(self.maze_data[0])-2 and 'R' in direction:
                    gate +=1
                property_dict[(i,j)] = (gate,direction)
                row.append(ways)
            help_metrix.append(row)
        return help_metrix, property_dict
    
    #walk through the maze with help_metrix
    def walking(self,pnt,help_m,pro_d):
        di_move = {'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}
        di_pair = {'L':'R','R':'L','U':'D','D':'U'}
        area = []
        ip_queue = Queue()
        ip_queue.enqueue(pnt)
        while not ip_queue.is_empty():
            pt = ip_queue.dequeue()
            dr = pro_d[pt][1]
            area.append(pt)
            x,y = pt
            if dr != []:
                for d in dr:
                    next_x,next_y = (x+di_move[d][0],y+di_move[d][1])
                    if next_x < 0 or next_x > len(help_m)-1 or next_y < 0 or next_y > len(help_m[0])-1:
                        continue
                    ip_queue.enqueue((next_x,next_y))
                    #avoiding going back
                    pro_d[(next_x,next_y)][1].remove(di_pair[d])
                # clear all directions
            while pro_d[pt][1]:
                pro_d[pt][1].pop()
            help_m[x][y] = 0
        return area
    
    #what left after accessing all areas
    def find_inaccessible_inner_point(self,help_m):
        t_m,_ = self.help_metrix()
        sets_of_inacc_area = []
        for t_i in range(len(t_m)):
            for t_j in range(len(t_m[0])):
                if t_m[t_i][t_j] == 0:
                    sets_of_inacc_area.append((t_i,t_j))
        for h_i in range(len(help_m)):
            for h_j in range(len(help_m[0])):
                if help_m[h_i][h_j] != 0:
                    #本来就是辅助矩阵里的一个点就算一个inaccessible_inner_point，所以算完accessible area之后直接输剩下的点就行
                    sets_of_inacc_area.append((h_i,h_j))
#                     i_area = self.walking((h_i,h_j),help_m,pro_d)
#                     for inacc_pt in i_area:
#                         sets_of_inacc_area.append(inacc_pt)
        return sets_of_inacc_area
    
    def find_accessible_areas(self,help_m,pro_d):
        sets_of_areas = []
        for i in range(len(help_m)):
            for j in range(len(help_m[0])):
                if i in [0,len(help_m)-1] or j in [0,len(help_m[0])-1]:
                    # pro_d[(i,j)][1] != [] avoid pts with gates but have been visited from other gate
                    if pro_d[(i,j)][0] > 0 and pro_d[(i,j)][1] != []:
                        sets_of_areas.append(self.walking((i,j),help_m,pro_d))
        return sets_of_areas
    #start from point with value 1 in help_metrix
    def find_accessible_cul_de_sacs(self,accessible_area):
        di_move = {'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}
        di_pair = {'L':'R','R':'L','U':'D','D':'U'}
        cul_de_sacs = []
#         inaccessible_pt_list = [pt for in_area in inaccessible_area for pt in in_area]
        help_m_of_cul, dire_of_cul = self.help_metrix()
        for area in accessible_area:
            cul = []
            while True:
                nb_of_1 = 0
                for pt in area:
                    i,j = pt
                    if help_m_of_cul[i][j] == 1:
                        nb_of_1 += 1
                        cul.append(pt)
                        help_m_of_cul[i][j] = help_m_of_cul[i][j] - 1
                        for d_of_next in dire_of_cul[pt][1]:
                            next_x,next_y = (i+di_move[d_of_next][0],j+di_move[d_of_next][1])
                            if (next_x,next_y) in cul:
                                continue
                            else:
                                if next_x < 0 or next_x > len(help_m_of_cul)-1 or next_y < 0 or next_y > len(help_m_of_cul[0])-1:
                                    break
                                else:
                                    help_m_of_cul[next_x][next_y] = help_m_of_cul[next_x][next_y] - 1
                                    break
                if nb_of_1 == 0:
                    break
            #seprate culs which from different set
            if cul !=[]:
                stack = []
                single_cul = []
                stack.append(cul[0])
                while cul != []:
                    c_x,c_y = stack.pop()
                    cul.remove((c_x,c_y))
                    single_cul.append((c_x,c_y))
                    for dc in dire_of_cul[(c_x,c_y)][1]:
                        next_c_x,next_c_y = (c_x+di_move[dc][0],c_y+di_move[dc][1])
                        if (next_c_x,next_c_y) in cul:
                            stack.append((next_c_x,next_c_y))
                    if stack == []:
                        cul_de_sacs.append(single_cul)
                        single_cul = []
                        if cul != []:
                            stack.append(cul[0])       
        return cul_de_sacs
    #accessible_areas with 2 gates
    def find_entry_exit_paths(self,accessible_area,cul_de_sacs):
        di_move = {'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}
        di_pair = {'L':'R','R':'L','U':'D','D':'U'}
        help_m2,pro_d2 = self.help_metrix()
        entry_exit_paths = []
        culs = [cul_p for cul in cul_de_sacs for cul_p in cul]
        #WILL RETURN PATH WHEN EXIT MAZE AND CUT THOSE BRANCHES THAT CANT EXIT
        #will ignore another 'path' in the the same area which has only 2 gates
        # and if another 'path' exists, then it is not an entry-exit path, so should not be returned
        #which makes this logic not "perfect"
    # so, we should use this split function can achieve two:
    #1st: to eliminate accessible_points that are not in the entry_exit path
    #2nd: to eliminate the special situation described as followed
    #Then we just need to see if the length of the result of split is 1, then it is a path, 
    #otherwise, it is the situation described below
    #这里面还包含了特殊情况：虽然只有2 gates，但是路径上有点（inner point）可走出maze的方向超过2个
    #这种情况不属于路径，应该被排除
    #split path to exit maze starting from one point in some area
    #and only path with exit can be added in the list named "sp_paths"
        def split(gpt):
            #use list as a stack
            sp_stack = []
            sp_stack.append([gpt])
            sp_paths = []
            single_pt_path = set()
            while sp_stack != []:
                sp_path = sp_stack.pop()
                sp_x,sp_y = sp_path[-1]
                for sp_d in pro_d2[(sp_x,sp_y)][1]:
                    sp_next_x,sp_next_y = (sp_x+di_move[sp_d][0],sp_y+di_move[sp_d][1])
                    if sp_next_x < 0 or sp_next_x > len(help_m2)-1 or sp_next_y < 0 or sp_next_y > len(help_m2[0])-1:
                        #会将只有一个点的路径给排除掉
                        if len(sp_path) == 1:
                            single_pt_path = set(sp_path)
                            continue
                        else:
                            sp_paths.append(sp_path)
                            continue
                    #avoid going back
                    if (sp_next_x,sp_next_y) not in sp_path:
                        sp_stack.append(sp_path+[(sp_next_x,sp_next_y)])
                    #pro_d2[(sp_next_x,sp_next_y)][1].remove(di_pair[sp_d])
            if sp_paths == []:
                sp_paths.append(list(single_pt_path))
            return sp_paths
        for area in accessible_area:
            gate_pt = []
            path = []
            nbofgates = 0
            mini = float('inf')
            maxi = -float('inf')
            #但area是只有一个点的情况，len（gate_pt）就永远只会为1，即便是一个点的path
            for pt in area:
                nbofgates += pro_d2[pt][0]
                if pro_d2[pt][0] > 0:
                    gate_pt.append(pt)
                if help_m2[pt[0]][pt[1]] > maxi:
                    maxi = help_m2[pt[0]][pt[1]]
                if help_m2[pt[0]][pt[1]] < mini:
                    mini = help_m2[pt[0]][pt[1]]
            # so nbofgates is needed.  
            if nbofgates == 2:
                #MIN AND MAX WAYS TO GO OF ALL POINTS IN HELP_METRIX
                if mini == maxi == 2:
                    entry_exit_paths.append(area)
                else:
                    #将只有一个点的路径排除掉了
                    final_path = split(gate_pt[0])
                    #即便len（final_path）为1，也依然包含了“虽然只有两扇门，但是路径上有点的值超过2，其中有不在路径上的children并不属于cul-de-sacs”
                    #按照定义，这条路径不算是entry-exit path
                    #但是因为split的功能，将这个分支当成是cul-de-sacs 给切除掉了
                    #所以还要在判断一下
                    if len(final_path) == 1:
                        #print('fp',final_path)
                        is_ee_path = True
                        #gate_pt[0]:just starts from the first point which has gates
                        #coz we have eliminate the special situation mentioned above, 
                        #split() will only return one path
                        for ppt in final_path[0]:
                            if help_m2[ppt[0]][ppt[1]] > 2:
                                ppt_x,ppt_y = ppt
                                for ppt_d in pro_d2[(ppt_x,ppt_y)][1]:
                                    ppt_next_x,ppt_next_y = (ppt_x+di_move[ppt_d][0],ppt_y+di_move[ppt_d][1])
                                    if ppt_next_x < 0 or ppt_next_x > len(help_m2)-1 or ppt_next_y < 0 or ppt_next_y > len(help_m2[0])-1:
                                        continue
                                    if (ppt_next_x,ppt_next_y) not in final_path[0] and (ppt_next_x,ppt_next_y) not in culs:
                                        is_ee_path = False
                                        break
                        if is_ee_path == True:
                            entry_exit_paths = entry_exit_paths + final_path
        return entry_exit_paths           
    def analyse(self):
        #IF I call the _data_validity() here, the exception will not be raised in ED, although it works in jupyter,idle.
        #I dont know why, but it just is.
        #self.maze_data = self._data_validity()
        help_m,pro_d = self.help_metrix()
        
        numOfgates = self.find_gates()
        #walls are list of sets
        walls = self.find_walls()
        accessible_area = self.find_accessible_areas(help_m,pro_d)
        inacceseeible_inner_points = self.find_inaccessible_inner_point(help_m)
        accessible_cul_de_sacs = self.find_accessible_cul_de_sacs(accessible_area)
        entry_exit_paths = self.find_entry_exit_paths(accessible_area,accessible_cul_de_sacs)
        self.maze_result = [walls,accessible_cul_de_sacs,entry_exit_paths]
        
        if numOfgates == 0:
            print(f'The maze has no gate.')
        elif numOfgates == 1:
            print(f'The maze has a single gate.')
        else:
            print(f'The maze has {numOfgates} gates.')

        if len(walls) == 0:
            print(f'The maze has no wall.')
        elif len(walls) == 1:
            print(f'The maze has walls that are all connected.')
        else:
            print(f'The maze has {len(walls)} sets of walls that are all connected.')

        if len(inacceseeible_inner_points) == 0:
            print(f'The maze has no inaccessible inner point.')
        elif len(inacceseeible_inner_points) == 1:
            print(f'The maze has a unique inaccessible inner point.')
        else:
            print(f'The maze has {len(inacceseeible_inner_points)} inaccessible inner points.')

        if len(accessible_area) == 0:
            print(f'The maze has no accessible area.')
        elif len(accessible_area) == 1:
            print(f'The maze has a unique accessible area.')
        else:
            print(f'The maze has {len(accessible_area)} accessible areas.')

        if len(accessible_cul_de_sacs) == 0:
            print(f'The maze has no accessible cul-de-sac.')
        elif len(accessible_cul_de_sacs) == 1:
            print(f'The maze has accessible cul-de-sacs that are all connected.')
        else:
            print(f'The maze has {len(accessible_cul_de_sacs)} sets of accessible cul-de-sacs that are all connected.')
        
        if len(entry_exit_paths) == 0:
            print(f'The maze has no entry-exit path with no intersection not to cul-de-sacs.')
        elif len(entry_exit_paths) == 1:
            print(f'The maze has a unique entry-exit path with no intersection not to cul-de-sacs.')
        else:
            print(f'The maze has {len(entry_exit_paths)} entry-exit paths with no intersections not to cul-de-sacs.')
        
    def display(self):
        if self.maze_result is not None:
            wal,ac_cul,ene_p = self.maze_result
        else:
            help_m_d,pro_d_d = self.help_metrix()
            wal = self.find_walls()
            acc_area = self.find_accessible_areas(help_m_d,pro_d_d)
            ac_cul = self.find_accessible_cul_de_sacs(acc_area)
            ene_p = self.find_entry_exit_paths(acc_area,ac_cul)
        h_m,p_d = self.help_metrix()
        di_move = {'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}
        di_pair = {'L':'R','R':'L','U':'D','D':'U'}
        #reverse x,y cordinate
        content_start = r'''\documentclass[10pt]{article}
\usepackage{tikz}
\usetikzlibrary{shapes.misc}
\usepackage[margin=0cm]{geometry}
\pagestyle{empty}
\tikzstyle{every node}=[cross out, draw, red]

\begin{document}

\vspace*{\fill}
\begin{center}
\begin{tikzpicture}[x=0.5cm, y=-0.5cm, ultra thick, blue]
'''
        content_wall = r'''% Walls
'''
        #1.横线先打
        #2.纵线从左往右依次打
        #3.同一条直线（纵线和横线）的一次性打
        horizonal = {}
        vertical = {}
        for i in range(len(self.maze_data)):
            for j in range(len(self.maze_data[0])):
                if self.maze_data[i][j] in [1,3]:
                    horizonal[(j,i)] = (j+1,i)
                    #content_wall = content_wall + f'    \draw {(j,i)} -- {(j+1,i)}'+';\n'
        for i in range(len(self.maze_data)):
            for j in range(len(self.maze_data[0])):
                if self.maze_data[i][j] in [2,3]:
                    vertical[(j,i)] = (j,i+1)
                    #content_wall = content_wall + f'    \draw {(j,i)} -- {(j,i+1)}'+';\n'
        #合并同一条直线（纵线和横线）的打印点
        def concat(dic):
            delete_keys = []
            for k in dic:
                if dic[k] != k:
                    if dic[k] in dic:
                        delete_keys.append(dic[k])
                        dic[k] = dic[dic[k]]
                        dic,dk = concat(dic)
                        delete_keys = delete_keys + dk
                    else:
                        continue
            return dic,delete_keys
        new_horizonal,dlt_k1 = concat(horizonal)
        for dlk1 in dlt_k1:
            if dlk1 in new_horizonal:
                new_horizonal.pop(dlk1)
        for nh in new_horizonal:
            content_wall = content_wall + f'    \draw ({nh[0]},{nh[1]}) -- ({new_horizonal[nh][0]},{new_horizonal[nh][1]})'+';\n'
        new_vertical,dlt_k2 = concat(vertical)
        for dlk2 in dlt_k2:
            if dlk2 in new_vertical:
                new_vertical.pop(dlk2)
        for nv in sorted(new_vertical):
            content_wall = content_wall + f'    \draw ({nv[0]},{nv[1]}) -- ({new_vertical[nv][0]},{new_vertical[nv][1]})'+';\n'
        
        content_pillars = r'''% Pillars
'''
        for i in range(len(self.maze_data)):
            for j in range(len(self.maze_data[0])):
                if self.maze_data[i][j] == 0:
                    if self.maze_data[i-1][j] not in [2,3] and self.maze_data[i][j-1] not in [1,3]:
                        content_pillars = content_pillars + f'    \\fill[green] ({j},{i}) circle(0.2);\n'
                        
        content_inner_points = r'''% Inner points in accessible cul-de-sacs
'''
        new_cul = [ac for acl in ac_cul for ac in acl]
        for i in range(len(self.maze_data)):
            for j in range(len(self.maze_data[0])):
                if (i,j) in new_cul:
                    content_inner_points = content_inner_points + f'    \\node at ({j+0.5},{i+0.5})'+' {};\n'
        
        content_paths = r'''% Entry-exit paths without intersections
'''
        horiz_p = {}
        verti_p = {}
        for pat in ene_p:
            for pa_p in pat:
                x,y = pa_p
                for dd in p_d[(x,y)][1]:
                    next_x,next_y = (x+di_move[dd][0],y+di_move[dd][1])
                    if (next_x,next_y) in pat:
                        if x == next_x:
                            if y < next_y:
                                horiz_p[(y+0.5,x+0.5)] = (next_y+0.5,next_x+0.5)
                            else:
                                horiz_p[(next_y+0.5,next_x+0.5)] = (y+0.5,x+0.5)
                        if y == next_y:
                            if x < next_x:
                                verti_p[(y+0.5,x+0.5)] = (next_y+0.5,next_x+0.5)
                            else:
                                verti_p[(next_y+0.5,next_x+0.5)] = (y+0.5,x+0.5)
                        #content_paths = content_paths + f'    \draw[dashed, yellow] ({y+0.5},{x+0.5}) -- ({next_y+0.5},{next_x+0.5});\n'
                    if next_x < 0 or next_x > len(h_m)-1 or next_y < 0 or next_y > len(h_m[0])-1:
                        if y == len(h_m[0])-1 and dd == 'R':
                            horiz_p[(y+0.5,x+0.5)] = (y+1.5,x+0.5)
                            #content_paths = content_paths + f'    \draw[dashed, yellow] ({y+1.5},{x+0.5}) -- ({y+0.5},{x+0.5});\n'
                        if y == 0 and dd == 'L':
                            horiz_p[(y-0.5,x+0.5)] = (y+0.5,x+0.5)
                            #content_paths = content_paths + f'    \draw[dashed, yellow] ({y-0.5},{x+0.5}) -- ({y+0.5},{x+0.5});\n'
                        if x == len(h_m)-1 and dd == 'D':
                            verti_p[(y+0.5,x+0.5)] = (y+0.5,x+1.5)
                            #content_paths = content_paths + f'    \draw[dashed, yellow] ({y+0.5},{x+1.5}) -- ({y+0.5},{x+0.5});\n'
                        if x == 0 and dd == 'U':
                            verti_p[(y+0.5,x-0.5)] = (y+0.5,x+0.5)
                            #content_paths = content_paths + f'    \draw[dashed, yellow] ({y+0.5},{x-0.5}) -- ({y+0.5},{x+0.5});\n'
                        continue
                    p_d[(next_x,next_y)][1].remove(di_pair[dd])
        def sort_by_2nd_nb_in_tuple(lis):
            new_list = [(y,x) for x,y in lis]
            sorted_new_list = [(i,j) for j,i in sorted(new_list)]
            return sorted_new_list
        new_horiz_p, dl_p1= concat(horiz_p)
        new_verti_p, dl_p2= concat(verti_p)
        for dlp1 in dl_p1:
            if dlp1 in new_horiz_p:
                new_horiz_p.pop(dlp1)
        h_order = sort_by_2nd_nb_in_tuple(list(new_horiz_p.keys())) 
        for nhp in h_order:
            content_paths = content_paths + f'    \draw[dashed, yellow] ({nhp[0]},{nhp[1]}) -- ({new_horiz_p[nhp][0]},{new_horiz_p[nhp][1]});\n'
        for dlp2 in dl_p2:
            if dlp2 in new_verti_p:
                new_verti_p.pop(dlp2)
        for nvp in sorted(new_verti_p):
            content_paths = content_paths + f'    \draw[dashed, yellow] ({nvp[0]},{nvp[1]}) -- ({new_verti_p[nvp][0]},{new_verti_p[nvp][1]});\n'
        content_end = r'''\end{tikzpicture}
\end{center}
\vspace*{\fill}

\end{document}
'''
        content = content_start+content_wall+content_pillars+content_inner_points+content_paths+content_end
        name_string = self.filename
        with open(f'{name_string[:-4]}.tex','w') as f:
            f.write(content)
