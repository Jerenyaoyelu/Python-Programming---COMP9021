# Defines two classes, Point() and Disk().
# The latter has an "area" attribute and three methods:
# - change_radius(r)
# - intersects(disk), that returns True or False depending on whether
#   the disk provided as argument intersects the disk object.
# - absorb(disk), that returns a new disk object that represents the smallest
#   disk that contains both the disk provided as argument and the disk object.
#
# Written by *** and Eric Martin for COMP9021


from math import pi, hypot



class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x:.2f}, {self.y:.2f})'

class Disk:
    area=0
    def __init__(self,*,centre=None, radius=0):
        if centre==None:
            self.centre=Point()
        else:
            self.centre=centre
        self.radius=radius
        self.area=pi*(radius**2)
    def __repr__(self):
        return f'Disk(Point({self.centre.x:.2f}, {self.centre.y:.2f}), {self.radius:.2f})'
    def change_radius (self, r):
        self.radius=r
        self.area=pi*(self.radius**2)
        return self.area
    def intersects (self,disk_2):
        distance=hypot((self.centre.x-disk_2.centre.x),(self.centre.y-disk_2.centre.y))
        if distance >self.radius + disk_2.radius:
            return False
        else:
            return True
    def absorb (self, disk_2):
        d=hypot((self.centre.x-disk_2.centre.x),(self.centre.y-disk_2.centre.y))
        if min(self.radius, disk_2.radius)==0:
            if d<=max(self.radius, disk_2.radius):
                if self.radius==0:
                    return disk_2
                else:
                    return self
            else:
                c_r=(d+self.radius+disk_2.radius)/2
                c_p=Point((((c_r-self.radius)*disk_2.centre.x)+(c_r-disk_2.radius)*self.centre.x)/(2*c_r-self.radius-disk_2.radius),(((c_r-self.radius)*disk_2.centre.y)+(c_r-disk_2.radius)*self.centre.y)/(2*c_r-self.radius-disk_2.radius))
                return Disk(centre=c_p,radius=c_r)
        else:
            c_r=(d+self.radius+disk_2.radius)/2
            c_p=Point((((c_r-self.radius)*disk_2.centre.x)+(c_r-disk_2.radius)*self.centre.x)/(2*c_r-self.radius-disk_2.radius),(((c_r-self.radius)*disk_2.centre.y)+(c_r-disk_2.radius)*self.centre.y)/(2*c_r-self.radius-disk_2.radius))
            return Disk(centre=c_p,radius=c_r)
        
            
            
