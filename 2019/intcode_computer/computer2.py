import sys 
class IntCodeComputer():
    def __init__(self):
        self.pointer = 0

    def run(self, code):
        self.code = code[:]
        while self.pointer < len(self.code):
            command = str(self.code[self.pointer])
            opcode = int(command[-1])
            mode_a = True
            mode_b = True
            mode_c = True
            if len(command) == 5:
                mode_c = not int(command[0])
                mode_b = not int(command[1])
                mode_a = not int(command[2])
            if len(command) == 4:
                mode_b = not int(command[0])
                mode_a = not int(command[1])
            if len(command) == 3:
                mode_a = not int(command[0])
            if opcode == 99 or command == '99':
                break
            elif opcode == 1:
                self.add(mode_a,mode_b,mode_c)
            elif opcode == 2:
                self.multiply(mode_a,mode_b,mode_c)
            elif opcode == 3:
                self.input(1)
            elif opcode == 4:
                self.output(mode_c)
        return self.code

    def add(self, mode_a, mode_b, mode_c):
        a = self.code[self.pointer + 1] if mode_a else self.pointer + 1
        b = self.code[self.pointer + 2] if mode_b else self.pointer + 2
        out = self.code[self.pointer + 3] if mode_c else self.pointer + 3
        self.code[out] = self.code[a] + self.code[b]
        self.pointer += 4

    def multiply(self, mode_a, mode_b, mode_c):
        a = self.code[self.pointer + 1] if mode_a else self.pointer + 1
        b = self.code[self.pointer + 2] if mode_b else self.pointer + 2
        out = self.code[self.pointer + 3] if mode_c else self.pointer + 3
        self.code[out] = self.code[a] * self.code[b]
        self.pointer += 4

    def input(self, input):
        out = self.code[self.pointer + 1]
        self.code[out] = input
        self.pointer += 2

    def output(self, mode):
        out = self.code[self.pointer + 1] if mode else self.pointer + 1
        print("out: " + str(self.code[out]))
       # if self.code[out] != 0:
       #     sys.exit()
        self.pointer += 2




if __name__ == "__main__":
    with open("input2.txt") as f:
        code = [int(x) for x in f.readline().split(',')] 

    computer = IntCodeComputer()
    result = computer.run(code)