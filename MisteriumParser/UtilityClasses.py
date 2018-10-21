class PostContent:

    def __init__(self):
        self.content = [] # must be a list of strings

    def show(self):
        print("=== NEW POST ===")
        for line in self.content:
            print(line, end="\n")

    def add_line(self, line):
        if line:
            self.content.append(line)