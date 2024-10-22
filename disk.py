class Disk:
    def __init__(self,total,used):
        self.total=total
        self.used=used
    
    def free(self):
        return self.total-self.used
    
    def used_perc(self):
        return self.used/self.total
    
    def __repr__(self) -> str:
        return f"Disk[total : {self.total} Gb, used : {self.used} Gb]"
    
    def __lt__(self,other):
        return self.used_perc() < other.used_perc()
    
if __name__ == '__main__':
    disk = Disk(10,2)
    disk2 = Disk(20,5)
    print(disk.free())
    print(disk2.free())
    print(disk.used_perc())
    print(disk2.used_perc())
    disks = [disk, disk2, Disk(2000,1)]
    print(sorted(disks))