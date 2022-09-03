

class CycleError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)  # 初始化父类
        self.errorinfo = "cause Endless loop:  {0}".format(ErrorInfo)

    def __str__(self):
        return self.errorinfo
