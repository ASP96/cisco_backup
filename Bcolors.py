class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = "\033[92m"
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def header(text):
        return Bcolors.HEADER + str(text) + Bcolors.ENDC

    @staticmethod
    def blue(text):
        return Bcolors.OKBLUE + str(text) + Bcolors.ENDC

    @staticmethod
    def cyan(text):
        return Bcolors.OKCYAN + str(text) + Bcolors.ENDC

    @staticmethod
    def green(text):
        return Bcolors.OKGREEN + str(text) + Bcolors.ENDC

    @staticmethod
    def warning(text):
        return Bcolors.WARNING + str(text) + Bcolors.ENDC

    @staticmethod
    def fail(text):
        return Bcolors.FAIL + str(text) + Bcolors.ENDC

    @staticmethod
    def bold(text):
        return Bcolors.BOLD + str(text) + Bcolors.ENDC

    @staticmethod
    def underline(text):
        return Bcolors.UNDERLINE + str(text) + Bcolors.ENDC
