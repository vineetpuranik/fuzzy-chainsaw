# A file system keeps a log each time some user performs a change folder operation.
# The operations are described below:
   #  "../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
   #  "./" : Remain in the same folder.
   # "x/" : Move to the child folder named x (This folder is guaranteed to always exist).

# You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.
# The file system starts in the main folder, then the operations in logs are performed.
# Return the minimum number of operations needed to go back to the main folder after the change folder operations.


# Used a linked list
# Using a map is problematic because multiple folders at different levels can have the same name.

class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        root = Folder("root", None)
        current = root
        
        for log in logs:
            if log == "../":
                # if we are already at root then we should stay in the root folder
                if current.name != "root":
                    current = current.parent

            # if log == ./ then we stay in the same folder
            elif log == "./":
                # in this case do not do any thing
                continue

            # if log == "x/" move to child folder named x
            else:
                current_folder_name = log.split("/")[0]
                new_folder = Folder(current_folder_name, current)
                current = new_folder

        min_steps = 0
        
        while current.name != "root":
            current = current.parent
            min_steps += 1
            
        
        return min_steps        
        
        
