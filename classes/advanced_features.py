import os


class ConfigDict(dict):

    def __init__(self, config_file):
        self.__config_file = config_file

        if not os.path.isfile(self.__config_file):
            fh = open(self.__config_file, 'w+')
            fh.close()
        fh = open(self.__config_file, 'r')

        contents = fh.readlines()
        for line in contents:
            k, v = line.strip().split('=', 1)
            dict.__setitem__(self, k, v)
        fh.close()

    def __str__(self):
        out = ''
        for k, v in self.items():
            out += f'{k}={v}\n'
        return out

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        fh = open(self.__config_file, 'a')
        fh.write(f'{key}={value}\n')
        fh.close()


cc = ConfigDict('hello.txt')
# cc['one'] = 1
# cc['two'] = 2
# cc['three'] = 3
# cc['two'] = 22
#
# cc['four'] = 4
# cc['five'] = 5
# cc['six'] = 6
# cc['seven'] = 7
# cc['eleven'] = 11
cc['twelve'] = 12
print(cc)