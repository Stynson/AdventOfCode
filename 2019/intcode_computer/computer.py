class IntCodeComputer():
    def __init__(self):
        self.pointer = 0

    def run(self, code):
        self.code = code[:]
        while self.pointer < len(self.code):
            #command = str(self.code[self.pointer])
            #opcode = command[-2:-1] 
            if self.code[self.pointer] == 99:
                break
            elif self.code[self.pointer] == 1:
                self.add()
            elif self.code[self.pointer] == 2:
                self.multiply(True,True,True)
        return self.code

    def add(self):
        a = self.code[self.pointer + 1]
        b = self.code[self.pointer + 2]
        out = self.code[self.pointer + 3]
        self.code[out] = self.code[a] + self.code[b]
        self.pointer += 4

    def multiply(self, mode_a, mode_b, mode_c):
        a = self.code[self.pointer + 1] if mode_a else self.pointer + 1
        b = self.code[self.pointer + 2] if mode_b else self.pointer + 1
        out = self.code[self.pointer + 3] if mode_c else self.pointer + 1
        self.code[out] = self.code[a] * self.code[b]
        self.pointer += 4

    def input(self):
        pass




if __name__ == "__main__":
    with open("input.txt") as f:
        code = [int(x) for x in f.readline().split(',')] 

    code[1] = 12
    code[2] = 2
    computer = IntCodeComputer()
    result = computer.run(code)
    print(result[0])