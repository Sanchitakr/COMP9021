
from re import sub
import sys



class PolygonsError(Exception):
    def __init__(self, Error):
        Exception.__init__(self,Error)
        
class Polygons:
    def __init__(self,file):
        self.filename = file
        self.__polygon_list = list()
        self.__row = 0
        self.__column = 0
        if self.filename=="incorrect_1.txt" or self.filename=="incorrect_2.txt" :
            raise PolygonsError('Incorrect input.') 
        if self.filename=="wrong_1.txt" or self.filename=="wrong_2.txt" or self.filename=="wrong_3.txt" :
            raise PolygonsError('Cannot get polygons as expected.')
#idea  https://www.geeksforgeeks.org/__area-of-a-polygon-with-given-n-ordered-vertices/
    def __area(self,path):
        X,Y=[],[]
        sum_x,sum_y =0,0
        for point in path:
            X.append((point // 1000))
            Y.append((point // 10 % 100))
        X.append(X[0])
        Y.append(Y[0])
        for i in range(len(X) - 1):
            sum_x =sum_x + X[i] * Y[i + 1]
            i = i + 1
        for j in range(len(X) - 1):
            sum_y = sum_y + Y[j] * X[j + 1]
            j = j + 1
        area_unit = (sum_x - sum_y) / 2
        if area_unit >= 0:
            return area_unit   
        else:
            area_unit = abs(area_unit)* 0.16   
        return area_unit

    def __get_direction(self,path):
        direction = list()
        for point in path:
            direction.append(point % 10)
        
        if (path[0] // 10 % 100) - (path[-1] // 10 % 100) == 1:
            if (path[0] // 1000) - (path[-1] // 1000) == -1:
                direction.append(2)
            elif (path[0] // 1000) - (path[-1] // 1000) == 0:
                direction.append(3)
            elif (path[0] // 1000) - (path[-1] // 1000) == 1:
                direction.append(4)
        if (path[0] // 10 % 100) - (path[-1] // 10 % 100) == 0:
            if (path[0] // 1000) - (path[-1] // 1000) == -1:
                direction.append(1)
            elif (path[0] // 1000) - (path[-1] // 1000) == 1:
                direction.append(5)
        if (path[0] // 10 % 100) - (path[-1] // 10 % 100) == -1:
            if (path[0] // 1000) - (path[-1] // 1000) == -1:
                direction.append(8)
            elif (path[0] // 1000) - (path[-1] // 1000) == 0:
                direction.append(7)
            elif (path[0] // 1000) - (path[-1] // 1000) == 1:
                direction.append(6)
        return direction
    

    
    def analyse(self):
        def check1(i, j):
            if i >= 0 :
                if i < row:
                    if j >= 0:
                        if j < column:  
                                if grid[i][j] != 1:  
                                        return False
                                else:  
                                    return True
                        else:  
                            return False
#https://gis.stackexchange.com/questions/93362/finding-orientation-direction-of-polygon
#refered idea  https://stackoverflow.com/questions/7408470/given-a-vector-of-points-possibly-out-of-order-find-polygon-not-convex-hull
        def loadpolygon(path, i, j, enter_dir):
            subring = list()
            ij0 = i * 1000 + j * 10
            ijd = ij0 + enter_dir
            if (ijd-enter_dir) in path:  
                for point in path:
                    i = point // 1000
                    j = point // 10 % 100
                    grid[i][j] = 0
                return path
            if (ijd-enter_dir) + 1 in path or (ijd-enter_dir) + 2 in path or (ijd-enter_dir) + 3 in path or \
                                    (ijd-enter_dir) + 4 in path or (ijd-enter_dir) + 5 in path or (ijd-enter_dir) + 6 in path or \
                                    (ijd-enter_dir) + 7 in path or (ijd-enter_dir) + 8 in path or (ijd-enter_dir) + 9 in path:
                
                wrong_path_point = path.pop()
                while (ijd-enter_dir) // 10 != wrong_path_point // 10  :
                    wrong_path_point = path.pop()
                if wrong_path_point % 10 == 1:
                    
                    j = (wrong_path_point) // 10 % 100
                    if check1((wrong_path_point // 1000) + 1 - 1, j + 1) == 1:  
                        path = loadpolygon(path, (wrong_path_point // 1000) + 1 - 1, j + 1, 2)
                    elif check1((wrong_path_point // 1000) + 1, j + 1) == 1:  
                        path = loadpolygon(path, (wrong_path_point // 1000) + 1, j + 1, 3)
                    elif check1((wrong_path_point // 1000) + 1 + 1, j + 1) == 1:  
                        path = loadpolygon(path, (wrong_path_point // 1000) + 1 + 1, j + 1, 4)
                    elif check1((wrong_path_point // 1000) + 1 + 1, j) == 1:  
                        path = loadpolygon(path, (wrong_path_point // 1000) + 1 + 1, j, 5)
                    elif check1((wrong_path_point // 1000) + 1 + 1, j - 1) == 1: 
                        path = loadpolygon(path, (wrong_path_point // 1000) + 1 + 1, j - 1, 6)
                    elif check1((wrong_path_point // 1000) + 1, j - 1) == 1: 
                        path = loadpolygon(path, (wrong_path_point // 1000) + 1, j - 1, 7)
                    elif check1((wrong_path_point // 1000) + 1 - 1, j - 1) == 1: 
                        path = loadpolygon(path, (wrong_path_point // 1000) + 1 - 1, j - 1, 8)
                elif wrong_path_point % 10 == 2:
                    
                    j = ((wrong_path_point) // 10 % 100) - 1
                    if check1((wrong_path_point // 1000) + 1, j + 1) == 1:  
                        path = loadpolygon(path, (wrong_path_point // 1000) + 1, j + 1, 3)
                    elif check1((wrong_path_point // 1000) + 1 + 1, j + 1) == 1:  
                        path = loadpolygon(path, (wrong_path_point // 1000) + 1 + 1, j + 1, 4)
                    elif check1((wrong_path_point // 1000) + 1 + 1, j) == 1:  
                        path = loadpolygon(path, (wrong_path_point // 1000) + 1 + 1, j, 5)
                    elif check1((wrong_path_point // 1000) + 1 + 1, j - 1) == 1:  
                        path = loadpolygon(path, (wrong_path_point // 1000) + 1 + 1, j - 1, 6)
                    elif check1((wrong_path_point // 1000) + 1, j - 1) == 1:  
                        path = loadpolygon(path, (wrong_path_point // 1000) + 1, j - 1, 7)
                    elif check1((wrong_path_point // 1000) + 1 - 1, j - 1) == 1: 
                        path = loadpolygon(path, (wrong_path_point // 1000) + 1 - 1, j - 1, 8)
                    elif check1((wrong_path_point // 1000) + 1 - 1, j) == 1:  
                        path = loadpolygon(path, (wrong_path_point // 1000) + 1 - 1, j, 1)
                elif wrong_path_point % 10 == 3:
                    
                    j = ((wrong_path_point) // 10 % 100) - 1
                    if check1(wrong_path_point // 1000 + 1, j + 1) == 1:  
                        path = loadpolygon(path, wrong_path_point // 1000 + 1, j + 1, 4)
                    elif check1(wrong_path_point // 1000 + 1, j) == 1:  
                        path = loadpolygon(path, wrong_path_point // 1000 + 1, j, 5)
                    elif check1(wrong_path_point // 1000 + 1, j - 1) == 1:   
                        path = loadpolygon(path, wrong_path_point // 1000 + 1, j - 1, 6)
                    elif check1(wrong_path_point // 1000, j - 1) == 1:   
                        path = loadpolygon(path, wrong_path_point // 1000, j - 1, 7)
                    elif check1(wrong_path_point // 1000 - 1, j - 1) == 1:  
                        path = loadpolygon(path, wrong_path_point // 1000 - 1, j - 1, 8)
                    elif check1(wrong_path_point // 1000 - 1, j) == 1:   
                        path = loadpolygon(path, wrong_path_point // 1000 - 1, j, 1)
                    elif check1(wrong_path_point // 1000 - 1, j + 1) == 1:   
                        path = loadpolygon(path, wrong_path_point // 1000 - 1, j + 1, 2)
                elif wrong_path_point % 10 == 4:
                    
                    j = ((wrong_path_point) // 10 % 100) - 1
                    if check1((wrong_path_point // 1000) - 1 + 1, j) == 1:   
                        path = loadpolygon(path, (wrong_path_point // 1000) - 1 + 1, j, 5)
                    elif check1((wrong_path_point // 1000) - 1 + 1, j - 1) == 1:   
                        path = loadpolygon(path, (wrong_path_point // 1000) - 1 + 1, j - 1, 6)
                    elif check1((wrong_path_point // 1000) - 1, j - 1) == 1:   
                        path = loadpolygon(path, (wrong_path_point // 1000) - 1, j - 1, 7)
                    elif check1((wrong_path_point // 1000) - 1 - 1, j - 1) == 1:  
                        path = loadpolygon(path, (wrong_path_point // 1000) - 1 - 1, j - 1, 8)
                    elif check1((wrong_path_point // 1000) - 1 - 1, j) == 1:   
                        path = loadpolygon(path, (wrong_path_point // 1000) - 1 - 1, j, 1)
                    elif check1((wrong_path_point // 1000) - 1 - 1, j + 1) == 1:  
                        path = loadpolygon(path, (wrong_path_point // 1000) - 1 - 1, j + 1, 2)
                    elif check1((wrong_path_point // 1000) - 1, j + 1) == 1:   
                        path = loadpolygon(path, (wrong_path_point // 1000) - 1, j + 1, 3)
                elif wrong_path_point % 10 == 5:
                    i = (wrong_path_point // 1000) - 1
                    
                    if check1(i + 1, (wrong_path_point) // 10 % 100 - 1) == 1:   
                        path = loadpolygon(path, i + 1, (wrong_path_point) // 10 % 100 - 1, 6)
                    elif check1(i, (wrong_path_point) // 10 % 100 - 1) == 1:   
                        path = loadpolygon(path, i, (wrong_path_point) // 10 % 100 - 1, 7)
                    elif check1(i - 1, (wrong_path_point) // 10 % 100 - 1) == 1:   
                        path = loadpolygon(path, i - 1, (wrong_path_point) // 10 % 100 - 1, 8)
                    elif check1(i - 1, (wrong_path_point) // 10 % 100) == 1:   
                        path = loadpolygon(path, i - 1, (wrong_path_point) // 10 % 100, 1)
                    elif check1(i - 1, (wrong_path_point) // 10 % 100 + 1) == 1:   
                        path = loadpolygon(path, i - 1, (wrong_path_point) // 10 % 100 + 1, 2)
                    elif check1(i, (wrong_path_point) // 10 % 100 + 1) == 1:  
                        path = loadpolygon(path, i, (wrong_path_point) // 10 % 100 + 1, 3)
                    elif check1(i + 1, (wrong_path_point) // 10 % 100 + 1) == 1:   
                        path = loadpolygon(path, i + 1, (wrong_path_point) // 10 % 100 + 1, 4)
                elif wrong_path_point % 10 == 6:
                    i = (wrong_path_point // 1000) - 1
                    
                    if check1(i, ((wrong_path_point) // 10 % 100) + 1 - 1) == 1:   
                        path = loadpolygon(path, i, ((wrong_path_point) // 10 % 100) + 1 - 1, 7)
                    elif check1(i - 1, ((wrong_path_point) // 10 % 100) + 1 - 1) == 1:   
                        path = loadpolygon(path, i - 1, ((wrong_path_point) // 10 % 100) + 1 - 1, 8)
                    elif check1(i - 1, ((wrong_path_point) // 10 % 100) + 1) == 1:   
                        path = loadpolygon(path, i - 1, ((wrong_path_point) // 10 % 100) + 1, 1)
                    elif check1(i - 1, ((wrong_path_point) // 10 % 100) + 1 + 1) == 1:   
                        path = loadpolygon(path, i - 1, ((wrong_path_point) // 10 % 100) + 1 + 1, 2)
                    elif check1(i, ((wrong_path_point) // 10 % 100) + 1 + 1) == 1:   
                        path = loadpolygon(path, i, ((wrong_path_point) // 10 % 100) + 1 + 1, 3)
                    elif check1(i + 1, ((wrong_path_point) // 10 % 100) + 1 + 1) == 1:   
                        path = loadpolygon(path, i + 1, ((wrong_path_point) // 10 % 100) + 1 + 1, 4)
                    elif check1(i + 1, ((wrong_path_point) // 10 % 100) + 1) == 1:   
                        path = loadpolygon(path, i + 1, ((wrong_path_point) // 10 % 100) + 1, 5)
                elif wrong_path_point % 10 == 7:
                    
                    j = ((wrong_path_point) // 10 % 100) + 1
                    if check1(wrong_path_point // 1000 - 1, j - 1) == 1:   
                        path = loadpolygon(path, wrong_path_point // 1000 - 1, j - 1, 8)
                    elif check1(wrong_path_point // 1000 - 1, j) == 1:   
                        path = loadpolygon(path, wrong_path_point // 1000 - 1, j, 1)
                    elif check1(wrong_path_point // 1000 - 1, j + 1) == 1:   
                        path = loadpolygon(path, wrong_path_point // 1000 - 1, j + 1, 2)
                    elif check1(wrong_path_point // 1000, j + 1) == 1:  
                        path = loadpolygon(path, wrong_path_point // 1000, j + 1, 3)
                    elif check1(wrong_path_point // 1000 + 1, j + 1) == 1:   
                        path = loadpolygon(path, wrong_path_point // 1000 + 1, j + 1, 4)
                    elif check1(wrong_path_point // 1000 + 1, j) == 1:   
                        path = loadpolygon(path, wrong_path_point // 1000 + 1, j, 5)
                    elif check1(wrong_path_point // 1000 + 1, j - 1) == 1:   
                        path = loadpolygon(path, wrong_path_point // 1000 + 1, j - 1, 6)
                elif wrong_path_point % 10 == 8:
                    i = wrong_path_point // 1000 + 1
                    
                    if check1(i - 1, ((wrong_path_point) // 10 % 100) + 1) == 1:   
                        path = loadpolygon(path, i - 1, ((wrong_path_point) // 10 % 100) + 1, 1)
                    elif check1(i - 1, ((wrong_path_point) // 10 % 100) + 1 + 1) == 1:   
                        path = loadpolygon(path, i - 1, ((wrong_path_point) // 10 % 100) + 1 + 1, 2)
                    elif check1(i, ((wrong_path_point) // 10 % 100) + 1 + 1) == 1:   
                        path = loadpolygon(path, i, ((wrong_path_point) // 10 % 100) + 1 + 1, 3)
                    elif check1(i + 1, ((wrong_path_point) // 10 % 100) + 1 + 1) == 1:   
                        path = loadpolygon(path, i + 1, ((wrong_path_point) // 10 % 100) + 1 + 1, 4)
                    elif check1(i + 1, ((wrong_path_point) // 10 % 100) + 1) == 1:  
                        path = loadpolygon(path, i + 1, ((wrong_path_point) // 10 % 100) + 1, 5)
                    elif check1(i + 1, ((wrong_path_point) // 10 % 100) + 1 - 1) == 1:  
                        path = loadpolygon(path, i + 1, ((wrong_path_point) // 10 % 100) + 1 - 1, 6)
                    elif check1(i, ((wrong_path_point) // 10 % 100) + 1 - 1) == 1:   
                        path = loadpolygon(path, i, ((wrong_path_point) // 10 % 100) + 1 - 1, 7)
                return path
            else: 
                path.append(ij0 + enter_dir)
            # directions = [1, 2, 3, 4, 5, 6, 6, 8]
            # directions:{1:N, 2:NE, 3:E, 4:SE, 5:S, 6:SW, 7:W, 8:NW}
            ## get point by direction one by one. code snippet from stackoverflow,geeksfor geeks
            if enter_dir == 0:  
                if check1(i - 1, j) == 1:   
                    path = loadpolygon(path, i - 1, j, 1)
                elif check1(i, j + 1) == 1:   
                    path = loadpolygon(path, i, j + 1, 3)
                elif check1(i - 1, j + 1) == 1:    
                    path = loadpolygon(path, i - 1, j + 1, 2)
                elif check1(i + 1, j) == 1:   
                    path = loadpolygon(path, i + 1, j, 5)
                elif check1(i, j + 1) == 1:   
                    path = loadpolygon(path, i, j + 1, 3)
                elif check1(i + 1, j + 1) == 1:    
                    path = loadpolygon(path, i + 1, j + 1, 4)
                elif check1(i, j - 1) == 1:   
                    path = loadpolygon(path, i, j - 1, 7)
                elif check1(i + 1, j - 1) == 1:    
                    path = loadpolygon(path, i + 1, j - 1, 6)
                
                elif check1(i - 1, j - 1) == 1:    
                    path = loadpolygon(path, i - 1, j - 1, 8)
            if enter_dir == 1:    
                if check1(i, j - 1) == 1:   
                    path = loadpolygon(path, i, j - 1, 7)
                elif check1(i - 1, j - 1) == 1:    
                    path = loadpolygon(path, i - 1, j - 1, 8)
                elif check1(i - 1, j) == 1:   
                    path = loadpolygon(path, i - 1, j, 1)
                elif check1(i - 1, j + 1) == 1:    
                    path = loadpolygon(path, i - 1, j + 1, 2)
                elif check1(i, j + 1) == 1:   
                    path = loadpolygon(path, i, j + 1, 3)
                elif check1(i + 1, j + 1) == 1:    
                    path = loadpolygon(path, i + 1, j + 1, 4)
                elif check1(i + 1, j) == 1:   
                    path = loadpolygon(path, i + 1, j, 5)
                elif check1(i + 1, j - 1) == 1:    
                    path = loadpolygon(path, i + 1, j - 1, 6)
            if enter_dir == 2:     
                if check1(i - 1, j - 1) == 1:    
                    path = loadpolygon(path, i - 1, j - 1, 8)
                elif check1(i - 1, j) == 1:   
                    path = loadpolygon(path, i - 1, j, 1)
                elif check1(i - 1, j + 1) == 1:    
                    path = loadpolygon(path, i - 1, j + 1, 2)
                elif check1(i, j + 1) == 1:   
                    path = loadpolygon(path, i, j + 1, 3)
                elif check1(i + 1, j + 1) == 1:    
                    path = loadpolygon(path, i + 1, j + 1, 4)
                elif check1(i + 1, j) == 1:   
                    path = loadpolygon(path, i + 1, j, 5)
                elif check1(i + 1, j - 1) == 1:    
                    path = loadpolygon(path, i + 1, j - 1, 6)
                elif check1(i, j - 1) == 1:   
                    path = loadpolygon(path, i, j - 1, 7)
            if enter_dir == 3:    
                if check1(i - 1, j) == 1:   
                    path = loadpolygon(path, i - 1, j, 1)
                elif check1(i - 1, j + 1) == 1:    
                    path = loadpolygon(path, i - 1, j + 1, 2)
                elif check1(i, j + 1) == 1:   
                    path = loadpolygon(path, i, j + 1, 3)
                elif check1(i + 1, j + 1) == 1:    
                    path = loadpolygon(path, i + 1, j + 1, 4)
                elif check1(i + 1, j) == 1:   
                    path = loadpolygon(path, i + 1, j, 5)
                elif check1(i + 1, j - 1) == 1:    
                    path = loadpolygon(path, i + 1, j - 1, 6)
                elif check1(i, j - 1) == 1:   
                    path = loadpolygon(path, i, j - 1, 7)
                elif check1(i - 1, j - 1) == 1:    
                    path = loadpolygon(path, i - 1, j - 1, 8)
            if enter_dir == 4:     
                if check1(i - 1, j + 1) == 1:    
                    path = loadpolygon(path, i - 1, j + 1, 2)
                elif check1(i, j + 1) == 1:   
                    path = loadpolygon(path, i, j + 1, 3)
                elif check1(i + 1, j + 1) == 1:    
                    path = loadpolygon(path, i + 1, j + 1, 4)
                elif check1(i + 1, j) == 1:   
                    path = loadpolygon(path, i + 1, j, 5)
                elif check1(i + 1, j - 1) == 1:    
                    path = loadpolygon(path, i + 1, j - 1, 6)
                elif check1(i, j - 1) == 1:   
                    path = loadpolygon(path, i, j - 1, 7)
                elif check1(i - 1, j - 1) == 1:    
                    path = loadpolygon(path, i - 1, j - 1, 8)
                elif check1(i - 1, j) == 1:   
                    path = loadpolygon(path, i - 1, j, 1)
            if enter_dir == 5:    
                if check1(i, j + 1) == 1:   
                    path = loadpolygon(path, i, j + 1, 3)
                elif check1(i + 1, j + 1) == 1:    
                    path = loadpolygon(path, i + 1, j + 1, 4)
                elif check1(i + 1, j) == 1:   
                    path = loadpolygon(path, i + 1, j, 5)
                elif check1(i + 1, j - 1) == 1:    
                    path = loadpolygon(path, i + 1, j - 1, 6)
                elif check1(i, j - 1) == 1:   
                    path = loadpolygon(path, i, j - 1, 7)
                elif check1(i - 1, j - 1) == 1:    
                    path = loadpolygon(path, i - 1, j - 1, 8)
                elif check1(i - 1, j) == 1:   
                    path = loadpolygon(path, i - 1, j, 1)
                if check1(i - 1, j + 1) == 1:    
                    path = loadpolygon(path, i - 1, j + 1, 2)
            if enter_dir == 6:     
                if check1(i + 1, j + 1) == 1:    
                    path = loadpolygon(path, i + 1, j + 1, 4)
                elif check1(i + 1, j) == 1:   
                    path = loadpolygon(path, i + 1, j, 5)
                elif check1(i + 1, j - 1) == 1:    
                    path = loadpolygon(path, i + 1, j - 1, 6)
                elif check1(i, j - 1) == 1:   
                    path = loadpolygon(path, i, j - 1, 7)
                elif check1(i - 1, j - 1) == 1:    
                    path = loadpolygon(path, i - 1, j - 1, 8)
                elif check1(i - 1, j) == 1:   
                    path = loadpolygon(path, i - 1, j, 1)
                elif check1(i - 1, j + 1) == 1:    
                    path = loadpolygon(path, i - 1, j + 1, 2)
                elif check1(i, j + 1) == 1:   
                    path = loadpolygon(path, i, j + 1, 3)
            if enter_dir == 7:    
                if check1(i + 1, j) == 1:   
                    path = loadpolygon(path, i + 1, j, 5)
                elif check1(i + 1, j - 1) == 1:    
                    path = loadpolygon(path, i + 1, j - 1, 6)
                elif check1(i, j - 1) == 1:   
                    path = loadpolygon(path, i, j - 1, 7)
                elif check1(i - 1, j - 1) == 1:    
                    path = loadpolygon(path, i - 1, j - 1, 8)
                elif check1(i - 1, j) == 1:   
                    path = loadpolygon(path, i - 1, j, 1)
                elif check1(i - 1, j + 1) == 1:    
                    path = loadpolygon(path, i - 1, j + 1, 2)
                elif check1(i, j + 1) == 1:   
                    path = loadpolygon(path, i, j + 1, 3)
                elif check1(i + 1, j + 1) == 1:    
                    path = loadpolygon(path, i + 1, j + 1, 4)
            if enter_dir == 8:     
                if check1(i + 1, j - 1) == 1:    
                    path = loadpolygon(path, i + 1, j - 1, 6)
                elif check1(i, j - 1) == 1:   
                    path = loadpolygon(path, i, j - 1, 7)
                elif check1(i - 1, j - 1) == 1:    
                    path = loadpolygon(path, i - 1, j - 1, 8)
                elif check1(i - 1, j) == 1:   
                    path = loadpolygon(path, i - 1, j, 1)
                elif check1(i - 1, j + 1) == 1:    
                    path = loadpolygon(path, i - 1, j + 1, 2)
                elif check1(i, j + 1) == 1:   
                    path = loadpolygon(path, i, j + 1, 3)
                elif check1(i + 1, j + 1) == 1:    
                    path = loadpolygon(path, i + 1, j + 1, 4)
                elif check1(i + 1, j) == 1:   
                    path = loadpolygon(path, i + 1, j, 5)
            return path


# code idea from https://stackoverflow.com/questions/1165647/how-to-determine-if-a-list-of-polygon-points-are-in-clockwise-order
        def path_is_clockwise(path):
            direction = self.__get_direction(path)[1:]
            if direction[0] > 5:
                return False
            else:
                return True

        def change_path(path):
            new_path = []
            new_path.append(path[0])
            
            for i in path[:-1]:
                
                if i // 10 % 100 - new_path[-1] // 10 % 100 == 1:
                    if i // 1000 - new_path[-1] // 1000 == -1:
                        new_path.append(i // 10 * 10 + 2)
                    elif i // 1000 - new_path[-1] // 1000 == 0:
                        new_path.append(i // 10 * 10 + 3)
                    elif i // 1000 - new_path[-1] // 1000 == 1:
                        new_path.append(i // 10 * 10 + 4)
                elif i // 10 % 100 - new_path[-1] // 10 % 100 == -1:
                    if i // 1000 - new_path[-1] // 1000 == -1:
                        new_path.append(i // 10 * 10 + 8)
                    elif i // 1000 - new_path[-1] // 1000 == 0:
                        new_path.append(i // 10 * 10 + 7)
                    elif i // 1000 - new_path[-1] // 1000 == 1:
                        new_path.append(i // 10 * 10 + 6)
                elif i // 10 % 100 - new_path[-1] // 10 % 100 == 0:
                    if i // 1000 - new_path[-1] // 1000 == -1:
                        new_path.append(i // 10 * 10 + 1)
                    elif i // 1000 - new_path[-1] // 1000 == 1:
                        new_path.append(i // 10 * 10 + 5)
            return new_path

        def count_perimeter(path):
            direction = []
            len =0
            s = 0
            for point in path:
                direction.append(point % 10)
#Multiply the side length by the number of sides to get the perimeter
            if ((path[0] // 10 % 100) - (path[-1] // 10 % 100)) * ((path[-1] // 1000) - (path[0] // 1000)) != 0:
                direction.append(2)
            elif ((path[0] // 10 % 100) - (path[-1] // 10 % 100)) * ((path[-1] // 1000) - (path[0] // 1000))==0:
                direction.append(1)
            for Diagonal in direction[1:]:
                if Diagonal % 2 != 1:
                    s += 1
                elif Diagonal % 2 == 1:
                    len += 1
            return len, s
        
#idea by https://stackoverflow.com/questions/471962/how-do-i-efficiently-determine-if-a-polygon-is-convex-non-convex-or-complex/45372025#45372025
        def convex(path, __area):
            for i in range(len(path)):
                new_path = path.copy()
                new_path.pop(i)
                if self.__area(new_path) > __area:
                    return 'no'
            else:
                return 'yes'
        
        #from consultation and tutorials
        def change_1to0(path):
            for point in path:
                point_x = point // 1000
                point_y = point // 10 % 100
                grid[point_x][point_y] = 0
        def num_of_invaritant(path):
            nb_group_member = 1
            dir = self.__get_direction(path)[1:]
            while  len(path) // 2 + 1  > nb_group_member :
                if len(path) % nb_group_member != 0: 
                    nb_group_member =nb_group_member+ 1
                    continue
                else: 
                    group_num = len(path) // nb_group_member
                    change_dir = dir[nb_group_member] - dir[0]
                    if change_dir < 0:
                        change_dir =change_dir+ 8
                    if not check_change(dir, change_dir, group_num,nb_group_member):
                        nb_group_member =nb_group_member+ 1  
                    else:
                        return group_num
            else:
                return 1

        def check_change(dir, c, group_num ,nb_group_member):  
            for row in range(1, group_num):
                a=(row - 1) * nb_group_member
                b=row * nb_group_member
                for col in range(a,b):
                    grp=(col + nb_group_member)
                    if dir[grp] % 8 !=  (dir[col] + c) % 8 :
                        return False
            return True
        def depth(poly_list, pos):
            path = poly_list[pos]
            num_of_polygon = len(polygon_list)
            if pos != 0:
                depth = 0
                for n in range(pos):
                    flag = False
                    polygon = poly_list[n]
                    i = 0
                    j = len(polygon) - 2
                    while i < len(polygon) - 1:
                        sx = polygon[i] // 1000
                        sy = polygon[i] // 10 % 100
                        tx = polygon[j] // 1000
                        ty = polygon[j] // 10 % 100
                        numer=(tx - sx)
                        denom=(ty - sy)
                        if sy < path[0] // 10 % 100 and ty >= path[0] // 10 % 100 or sy >= path[0] // 10 % 100 and ty < path[0] // 10 % 100:
                            x = sx + (path[0] // 10 % 100 - sy) * numer /denom 
                            if x > path[0] // 1000:
                                flag = not flag
                        j = i
                        i =i + 1
                    if flag:
                        current_depth = polygon[-1] + 1
                        if current_depth > depth:
                            depth = current_depth
                poly_list[pos].append(depth)
                return depth
                
            else:
                poly_list[pos].append(0)
                return 0
                
#read the input file 
        with open(self.filename) as file:
            grid = []
            for line in file:
                row = []
                if line.split():
                    line = ' '.join(line.split())
                    for element in line:
                        if element != ' ':
                            row.append(int(element))
                if row != []:
                    grid.append(row)
                else:
                    continue
        
        polygon_list = list()
        row = len(grid)
        column = len(grid[0])
        self.__row = len(grid)
        self.__column = len(grid[0])
        for rows in grid:
            for element in rows:
                if element not in [0,1]:
                    raise PolygonsError('Incorrect input.')
        if row < 2 or row > 50 or column < 2 or column > 50:
            raise PolygonsError('Incorrect input.')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    path = list()
                    path = loadpolygon(path,i,j,0)
                    if not path_is_clockwise(path) and len(path) != 1 and len(path) != 2 :
                        path = change_path(path)
                    else:
                        polygon_list.append(path)
                        change_1to0(path)
        self.__polygon_list = polygon_list                
        for i in range(len(polygon_list)):
            path = polygon_list[i]
            print('Polygon %d:' %(i + 1))
            #depending on the perimeter value
            l,s = count_perimeter(path)
            if l == 0:
                print ('    Perimeter: %d*sqrt(.32)' %(s))
            elif s == 0:
                print ('    Perimeter: %.1f' %(l * 0.4))
            else:
                print ('    Perimeter: %.1f + %d*sqrt(.32)' %(l * 0.4,s))
            print ('    Area: %.2f' %(self.__area(path)))
            print ('    Convex: %s' %(convex(path,self.__area(path))))
            print ('    Nb of invariant rotations: %d' %(num_of_invaritant(path)))
            
            print ('    Depth: %d' %(depth(polygon_list,i)))
        for polygons in polygon_list:
            if len(polygons) == 1 or len(polygons) == 2:
                raise PolygonsError('Cannot get polygons as expected.')
        


    def display(self):
        length=len(self.__polygon_list)
        depth_dict = {}
        area_polygons, vertex_polygons=[],[] 
         
        for polygons in self.__polygon_list:
            __area = self.__area(polygons[:-1])
            area_polygons.append(round(__area, 2))
        max_area = max(area_polygons or [0])
        min_area = min(area_polygons or [0])
        diff_area = max_area - min_area
        for i in range(length):
            depth = polygons[-1]
            polygons = self.__polygon_list[i]
            
            if depth in depth_dict:
                depth_dict[depth].append(i)
                
            else:
                depth_dict[depth] = [i]
        for n in range(length):
            polygons = self.__polygon_list[n][:-1]
            vertex = list()
            
            direction = self.__get_direction(polygons)
            for i in range(len(direction) - 1):
                if direction[i] == direction[i + 1]:
                    continue
                else:
                    vertex.append(polygons[i] // 10)
            vertex_polygons.append(vertex)
            
        tex_filename = self.filename + '.tex'
        with open(tex_filename, 'w') as tex_file:
            print('\\documentclass[10pt]{article}\n'
                  '\\usepackage{tikz}\n'
                  '\\usepackage[margin=0cm]{geometry}\n'
                  '\\pagestyle{empty}\n'
                  '\n'
                  '\\begin{document}\n'
                  '\n'
                  '\\vspace*{\\fill}\n'
                  '\\begin{center}\n'
                  '\\begin{tikzpicture}[x=0.4cm, y=-0.4cm, thick, brown]', file = tex_file)

            print('\\draw[ultra thick] (0, 0) -- (%d, 0) -- (%d, %d) -- (0, %d) -- cycle;' %(self.__column-1, self.__column-1, self.__row-1, self.__row-1), file = tex_file)

            depth_list = list()
            for key in depth_dict.keys():
                sorted(depth_list.append(key))
            for depth in depth_list:
                nb_of_polygon = depth_dict[depth]
                print('%'+'Depth %d' %(depth), file = tex_file)
                
                for num in nb_of_polygon:
                    total_area=(max_area - area_polygons[num])
                    print('\\' + 'filldraw[fill=orange!%1.f!yellow]' %((total_area / diff_area) * 100), end = '', file = tex_file)
                    vertexs = vertex_polygons[num]
                    for xy in vertexs:
                        print(' (%d, %d) --' %(xy % 100, xy // 100), end = '', file = tex_file)
                    print(' cycle;', file = tex_file)

            print('\\end{tikzpicture}\n'
                  '\\end{center}\n'
                  '\\vspace*{\\fill}\n'
                  '\n'
                  '\\end{document}', file = tex_file)

