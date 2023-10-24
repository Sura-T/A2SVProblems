from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # Create a dictionary to store file content as keys and corresponding file paths as values
        content_to_paths = defaultdict(list)
        
        # Iterate through each directory info string
        for info in paths:
            # Split the directory info string into directory path and file information
            parts = info.split()
            directory = parts[0]
            
            # Iterate through the file information
            for file_info in parts[1:]:
                # Split the file information into file name and content
                file_parts = file_info.split('(')
                file_name = file_parts[0]
                file_content = file_parts[1][:-1]
                
                # Construct the file path
                file_path = directory + '/' + file_name
                
                # Add the file path to the dictionary using the content as the key
                content_to_paths[file_content].append(file_path)
        
        # Filter out the file groups with only one file
        duplicate_groups = [paths for paths in content_to_paths.values() if len(paths) > 1]
        
        return duplicate_groups