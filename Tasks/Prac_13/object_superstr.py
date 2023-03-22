class SuperStr(str):

    def __init__(self, string):
        self.string = string

    def is_repeatance(self, s):
        if type(s) != str:
            return False
        if len(s) == 0:
            return False
        spisok = []
        for i in self.string:
            if i not in spisok:
                spisok.append(i)
        l = ''.join(spisok)
        if l == s[-len(l):]:
            return True
        else:
            return False

    def is_palindrom(self):
        s2 = ''
        i = 1
        while i <= len(self.string):
            s2 += self.string[-i]
            i += 1
        if s2 == self.string:
            return True
        else:
            return False


s = SuperStr("123123123123")
print(s.is_repeatance("123"))
print(s.is_repeatance("123123"))
print(s.is_repeatance("123123123123"))
print(s.is_repeatance("12312"))
print(s.is_repeatance(123))
print(s.is_palindrom())
print(s)
print(int(s))
print(s + "qwe")
p = SuperStr("123_321")
print(p.is_palindrom())
