import fnmatch
import os
import shutil


class DeployService:

    def _ignore_patterns(self, names, exclude=None, patterns=None):
        # print(f"/{names} / exclude={exclude} / pattern={patterns}")
        ignored_names = set()
        if exclude is not None:
            for pattern in exclude:
                ignored_names.update(fnmatch.filter(names, pattern))
        # print(f"ignored_names={ignored_names}")
        if patterns is not None:
            all_names = set(names)
            pattern_names = set()
            for pattern in patterns:
                pattern_names.update(fnmatch.filter(all_names, pattern))
            # print(f"pattern_names={pattern_names}")
            # all_differenced = (
            all_names.difference_update(pattern_names)
            ignored_names = ignored_names.union(all_names)
        # print(f"ignored_names={ignored_names}")
        return ignored_names

    def deploy(self, src_path, dest_path, project_name, exclude=None, pattern=None):
        dest = f"{dest_path}"
        shutil.rmtree(dest, ignore_errors=True)
        src = f"{src_path}/{project_name}"

        os.mkdir(dest)
        self.walk_through_tree(src, dest, exclude=exclude, pattern=pattern)
        # shutil.copytree(src_path, dest_path, ignore=shutil.ignore_patterns(self._ignore_patterns, exclude, pattern), dirs_exist_ok=True)

    def walk_through_tree(self, folder_src, folder_dest, exclude=None, pattern=None):
        # print(f"{folder_src}")
        # print(f"{os.scandir(folder_src)}")
        for root, dirs, files in os.walk(folder_src, topdown=False):
            # print(f"{root} dirs={dirs} files={files}")
            dirs_filtered = self.filter_names(dirs, exclude=exclude, pattern=pattern)
            # print(f"{folder_src} dirs_filtered={dirs_filtered}")
            for df in dirs_filtered:
                dirs.remove(df)
            # for subdir in dirs_filtered:
            #     self.walk_recursively(f"{folder_src}/{subdir}", folder_dest, f"{related_path}{subdir}/", exclude=exclude, pattern=pattern)
            #
            files_filtered = self.filter_names(files, exclude=exclude, pattern=pattern)
            # print(f"{root} files_filtered={files_filtered}")
            related_path = root.replace(folder_src, "")
            for file in files_filtered:
                os.makedirs(os.path.dirname(f"{folder_dest}{related_path}/"), exist_ok=True)
                # print(f"copy {root}/{file} to {folder_dest}{related_path}/{file}")
                shutil.copyfile(f"{root}/{file}", f"{folder_dest}{related_path}/{file}")


    def filter_names(self, names, exclude=None, pattern=None):
        names_excluded = self._ignore_patterns(names, exclude=exclude, patterns=pattern)

        names_set = set(names)
        a = names_set.difference(names_excluded)
        # print(f"names={names_set} / names_excluded={names_excluded} / diff={a}/ exclude={exclude} / pattern={pattern}")
        return a

