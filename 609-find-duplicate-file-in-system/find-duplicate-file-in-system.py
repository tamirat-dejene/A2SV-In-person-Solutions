class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dir_files_map = {folder: files for folder, files in [[path.split()[0], path.split()[1:]] for path in paths]}

        content_dir_map = {}

        for folder in dir_files_map.keys():
            files = dir_files_map[folder]
            for file_ in files:
                file_name, content = file_[:file_.index('(')], file_[file_.index('(') + 1: -1]
                dirs = content_dir_map.get(content, [])
                dirs.append('/'.join([folder, file_name]))

                content_dir_map[content] = dirs

        return [files for files in content_dir_map.values() if len(files) > 1]