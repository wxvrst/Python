class LeftParagraph:
    def __init__(self,width,words=""):
        self.width=width
        self.words=words
        print("Создадим объект LeftParagraph")
    def add_word(self,word):
        self.words+=word.ljust(self.width)
        self.words+="\n"
    def end(self):
        return (self.words)


class RightParagraph:
    def __init__(self,width,words=""):
        self.width=width
        self.words=words
        print("Создадим объект RightParagraph")
    def add_word(self,word):
        self.words+=word.rjust(self.width)
        self.words+="\n"
    def end(self):
        return (self.words)


par1= LeftParagraph(20)
par2= RightParagraph(40)
par1.add_word("awdwa")
par1.add_word("a3333")
par1.add_word("12321")
print(par1.end())
par2.add_word("eqwewqewqeqwe")
par2.add_word("ewqeqw")
print(par2.end())
print("\n\n\n")