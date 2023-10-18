import datetime
import os
import shutil
import tempfile


class FSService:
    temp_dir = '/tmp'

    def createTemp(self, prefix):
        current_datetime = datetime.datetime.now()
        formatted_date_time = current_datetime.strftime("%Y-%m-%d-%H-%M-%S.%s")
        return tempfile.mkdtemp(dir=self.temp_dir, prefix=f"{prefix}_", suffix=f"_{formatted_date_time}")

    def deleteTemp(self, tempdir):
        shutil.rmtree(tempdir)

    def extractFilenameWithoutExt(self, full_path):
        file_name_without_extension, file_extension = os.path.splitext(os.path.basename(full_path))
        return file_name_without_extension
