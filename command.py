class Command:
    _exutabled = False
    _result = False

    def __init__(self, cmd):
        self.value = cmd
        #self.type = cmd_type

    # Запуск команды
    def execute(self):
        self._exutabled = True

    def execute(self):
        return True

    def setResult(self, result):
        self._result = result

    def getResult(self):

        return self._result