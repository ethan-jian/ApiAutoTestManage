from django.http import JsonResponse


class Reponse(object):
    totalCount = 0
    code = 200
    message = "操作成功"
    data = None

    def common_response(self):
        """
        通用的返回接口数据结构
        :return:
        """
        response = {
            "totalCount": self.totalCount,
            "code": self.code,
            "message": self.message,
            "data": self.data
        }

        return JsonResponse(response, safe=False)

    def response_success(self, totalCount, data):
        """
        :return:
        """
        self.totalCount = totalCount
        self.code = 200
        self.message = "操作成功"
        self.data = data

        self.common_response()


    def response_failed(self):
        """
        :return:
        """
        self.totalCount = 0
        self.code = 500
        self.message = "操作失败"
        self.data = None

        self.common_response()

