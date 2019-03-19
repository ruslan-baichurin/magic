import abc
import datetime


class GetSetParent:
    __metaclass__ = abc.ABCMeta

    def __init__(self, value):
        self.val = 0

    def set_val(self, value):
        self.val = value

    def get_val(self):
        return self.val

    @abc.abstractmethod
    def showdoc(self):
        return


class GetSetInt(GetSetParent):

    def set_val(self, value):
        if not isinstance(value, int):
            value = 0
        super().set_val(value)

    def showdoc(self):
        print(f'GetSetInt object {id(self)} only accepts integer values')


class GetSetList(GetSetParent):
    def __init__(self, value=0):
        self.vallist = [value]

    def get_val(self):
        return self.vallist[-1]

    def get_vals(self):
        return self.vallist

    def set_val(self, value):
        self.vallist.append(value)

    def showdoc(self):
        print(f'GetSetList object. len {len(self.vallist)} stores history of values set.')


# x = GetSetInt(3)
# x.set_val(5)
# print(x.get_val())
# x.showdoc()

# gsl = GetSetList(5)
# gsl.set_val(10)
# gsl.set_val(20)
# print(gsl.get_val())
# print(gsl.get_vals())
# gsl.showdoc()


class WriteFile:
    def __init__(self, file_name):
        self.file_name = file_name

    def write(self, message):
        with open(self.file_name, 'a') as f:
            f.write(message + '\n')


class LogFile(WriteFile):
    def __init__(self, file_name):
        super().__init__(file_name)

    def write(self, message):
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        message = current_time + '    ' + message
        super().write(message)


class DelimFile(WriteFile):
    def __init__(self, file_name, dlm):
        self.dlm = dlm
        super().__init__(file_name)

    def write(self, message):
        out = ''
        for item in message:
            if ',' in item:
                item = f'"{item}"'
            if out:
                out = out + self.dlm + item
            else:
                out = item
        super().write(out)


# log = LogFile('log.txt')
# log.write('This is my first message')
# log.write('This is my second message')

c = DelimFile('text.csv', ',')
c.write(['a', 'b', 'c', 'd'])
c.write(['a', 'b,2', 'c', 'd'])
c.write(['1', '2', '3', '4'])