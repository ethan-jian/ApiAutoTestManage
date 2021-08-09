import os
from interface_app.libs.reponse import Reponse
from interface_app.util.utils import get_file_path

class FileView(Reponse):

    def api_upload(self, request, *args, **kwargs):
        """
        上传文件接口
        """
        up_file = request.FILES.get("file", None)
        if not up_file:
            return self.response_failed("上传不能为空")
        else:
            file_path = get_file_path() + up_file.name
            if os.path.exists(file_path):
                self.message = "已存在"
                return self.response_success(0, file_path)
            else:
                with open(file_path, 'wb+') as f:
                    for chunk in up_file.chunks():
                        f.write(chunk)
                self.message = "上传成功"
                return self.response_success(0, file_path)


    def api_update(self, request, *args, **kwargs):
        """
        更新文件接口
        """
        old_file = request.get("filePath", None)
        if (os.path.exists(old_file)):
            os.remove(old_file)
            with open(old_file, 'wb+') as f:
                for chunk in old_file.chunks():
                    f.write(chunk)
            self.message = "上传成功"
            return self.response_success(0, old_file)


