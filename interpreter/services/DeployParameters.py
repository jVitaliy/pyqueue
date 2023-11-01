class DeployParameters:
    def __init__(self, src_path=None, dest_path=None, exclude=None, pattern=None, is_merge=False, project_name=None):
        self.src_path = src_path
        self.dest_path = dest_path
        self.exclude = exclude
        self.pattern = pattern
        self.is_merge = is_merge
        self.project_name = project_name

    def __eq__(self, other):
        if isinstance(other, DeployParameters):
            res = self.src_path == other.src_path
            if not res:
                print(f"error src_path {self.src_path} !={other.src_path}")
                return False
            res = res and self.dest_path == other.dest_path
            if not res:
                print(f"error dest_path {self.dest_path} !={other.dest_path}")
                return False
            res = res and self.project_name == other.project_name
            if not res:
                print(f"error project_name {self.project_name} !={other.project_name}")
                return False
            res = res and self.exclude == other.exclude
            if not res:
                print(f"error exclude {self.exclude} !={other.exclude}")
                return False
            res = res and self.pattern == other.pattern
            if not res:
                print(f"error pattern {self.pattern} !={other.pattern}")
                return False
            res = res and self.is_merge == other.is_merge
            if not res:
                print(f"error is_merge {self.is_merge} !={other.is_merge}")
                return False

            return res
            # return (self.src_path == other.src_path
            #         and self.dest_path == other.dest_path
            #         and self.project_name == other.project_name
            #         and self.exclude == other.exclude
            #         and self.pattern == other.pattern
            #         and self.is_merge == other.is_merge)
        return False
