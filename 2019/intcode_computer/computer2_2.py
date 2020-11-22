import sys 
class IntCodeComputer():
    def __init__(self):
        self.pointer = 0

    def run(self, code, input):
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
                self.input(input)
            elif opcode == 4:
                self.output(mode_a)
            elif opcode == 5:
                self.jump_if_true(mode_a, mode_b)
            elif opcode == 6:
                self.jump_if_false(mode_a, mode_b)
            elif opcode == 7:
                self.less_than(mode_a,mode_b, mode_c)
            elif opcode == 8:
                self.equals(mode_a,mode_b, mode_c)
        return self.code

    def less_than(self, mode_a, mode_b, mode_c):
        a = self.code[self.pointer + 1] if mode_a else self.pointer + 1
        b = self.code[self.pointer + 2] if mode_b else self.pointer + 2
        out = self.code[self.pointer + 3] if mode_c else self.pointer + 3
        self.code[out] = int(self.code[a] < self.code[b]) 
        if out != self.pointer:
            self.pointer += 4

    def equals(self, mode_a, mode_b, mode_c):
        a = self.code[self.pointer + 1] if mode_a else self.pointer + 1
        b = self.code[self.pointer + 2] if mode_b else self.pointer + 2
        out = self.code[self.pointer + 3] if mode_c else self.pointer + 3
        self.code[out] = int(self.code[a] == self.code[b]) 
        if out != self.pointer:
            self.pointer += 4

    def jump_if_true(self, mode_a, mode_b):
        a = self.code[self.pointer + 1] if mode_a else self.pointer + 1
        b = self.code[self.pointer + 2] if mode_b else self.pointer + 2
        if self.code[a] != 0:
            self.pointer = self.code[b]
        else:
            self.pointer += 3

    def jump_if_false(self, mode_a, mode_b):
        a = self.code[self.pointer + 1] if mode_a else self.pointer + 1
        b = self.code[self.pointer + 2] if mode_b else self.pointer + 2
        if self.code[a] == 0:
            self.pointer = self.code[b]
        else:
            self.pointer += 3



    def add(self, mode_a, mode_b, mode_c):
        a = self.code[self.pointer + 1] if mode_a else self.pointer + 1
        b = self.code[self.pointer + 2] if mode_b else self.pointer + 2
        out = self.code[self.pointer + 3] if mode_c else self.pointer + 3
        self.code[out] = self.code[a] + self.code[b]
        if out != self.pointer:
            self.pointer += 4

    def multiply(self, mode_a, mode_b, mode_c):
        a = self.code[self.pointer + 1] if mode_a else self.pointer + 1
        b = self.code[self.pointer + 2] if mode_b else self.pointer + 2
        out = self.code[self.pointer + 3] if mode_c else self.pointer + 3
        self.code[out] = self.code[a] * self.code[b]
        if out != self.pointer:
            self.pointer += 4

    def input(self, input):
        out = self.code[self.pointer + 1]
        self.code[out] = input
        if out != self.pointer:
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
    result = computer.run(code,5)