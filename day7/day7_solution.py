def part1(lines):
    root = Directory('/')
    collectDir = False
    ignoreDir = False
    cur_dir = Directory("")
    for line in lines:
        split_line = line.split(' ')
        if split_line[1] == 'cd':
            cur_dir.listed = True
            ignoreDir = False
            collectDir = False
            if split_line[2].strip() == '..':
                cur_dir = cur_dir.parentDirectory
            if split_line[2].strip() == '/':
                cur_dir = root
            else:
                if cur_dir.hasDir(split_line[2].strip()):
                    parentDir = cur_dir
                    cur_dir = cur_dir.changeDirectory(split_line[2].strip())
                    cur_dir.parentDirectory = parentDir

        if split_line[1].strip() == 'ls':
            collectDir = True
            continue
        if collectDir and not ignoreDir:
            if cur_dir.listed:
                ignoreDir = True
            elif split_line[0] == 'dir':
                cur_dir.addDirectory(Directory(split_line[1].strip()))
            else:
                cur_dir.addSize(int(split_line[0]))

    result = searchTreePart1(root)
    print(result)

def part2(lines):
    root = Directory('/')
    collectDir = False
    ignoreDir = False
    cur_dir = Directory("")
    for line in lines:
        split_line = line.split(' ')
        if split_line[1] == 'cd':
            cur_dir.listed = True
            ignoreDir = False
            collectDir = False
            if split_line[2].strip() == '..':
                cur_dir = cur_dir.parentDirectory
            if split_line[2].strip() == '/':
                cur_dir = root
            else:
                if cur_dir.hasDir(split_line[2].strip()):
                    parentDir = cur_dir
                    cur_dir = cur_dir.changeDirectory(split_line[2].strip())
                    cur_dir.parentDirectory = parentDir

        if split_line[1].strip() == 'ls':
            collectDir = True
            continue
        if collectDir and not ignoreDir:
            if cur_dir.listed:
                ignoreDir = True
            elif split_line[0] == 'dir':
                cur_dir.addDirectory(Directory(split_line[1].strip()))
            else:
                cur_dir.addSize(int(split_line[0]))

    # Calculate how much space needs to be freed
    totalDiskSpace = 70000000
    spaceNeeded = 30000000
    freeSpace = totalDiskSpace - root.size
    spaceNeededToDelete = spaceNeeded - freeSpace
    result = searchTreePart2(spaceNeededToDelete, root)
    result.sort()
    print(result[0])

    # Directory class to construct directory tree
class Directory:
    def __init__(self, name):
        self.name = name
        self.directories = []
        self.size = 0
        self.parentDirectory = None
        self.listed = False

    def addDirectory(self, directory : 'Directory'):
        if self.directories.count(directory) < 1:
            self.directories.append(directory)

    def addSize(self, size):
        if size == 0:
            self.size = size
            if self.parentDirectory != None:
                self.parentDirectory.addSize(size)
        else:
            self.size += size
            if self.parentDirectory != None:
                self.parentDirectory.addSize(size)

    def changeDirectory(self, name):
        for dir in self.directories:
            if dir.name == name:
                return dir
    
    def hasDir(self, name):
        for dir in self.directories:
            if dir.name == name:
                return True
        return False

# Recursive function to iterate over tree
def searchTreePart1(directory : 'Directory'):
    result = 0
    for dir in directory.directories:
        if dir.size < 100000:
            result += dir.size
        result += searchTreePart1(dir)
    return result

def searchTreePart2(spaceNeededToDelete, directory : 'Directory'):
    result = []
    for dir in directory.directories:
        if dir.size >= spaceNeededToDelete:
            result.append(dir.size)
        result.extend(searchTreePart2(spaceNeededToDelete, dir))
    return result

with open('day7.txt') as f:
    lines = f.readlines()
part1(lines)
part2(lines)