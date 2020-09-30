

class combine():
    def __init__(self, words, base=""):
        self.words = words
        self.base = base
        # print("Words: " + "".join(words))
        # print("Base: " + base)

        for _ in self.words:
            print(self.base + self.words[0])
            combine(self.words[1:len(self.words)], self.base+self.words[0])
            self.rotate()

    def rotate(self):
        self.words.append(self.words[0])
        self.words.pop(0)


words = ["usr.", "share.", "lib.", "etc.", "tomcat9.", "doc.", "tomcat-doc."]
combine(words)
