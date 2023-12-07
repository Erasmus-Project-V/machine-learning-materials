import numpy as np


class GeneralMathOps:
    meth_name: str
    result_cntnr: float
    children: any([tuple, list])
    bases = {"a": 0.0, "s": 0.0, "m": 1.0}

    def calculate(self):
        return self.exec_operation()

    def exec_operation(self):
        return self.bases[self.meth_name]

    def return_printable(self):
        # bgn, sep, end
        return "?", "?", "??"

    def __str__(self):
        return self.return_printable()


class VariableController:

    def __init__(self):
        self.variable_cont = {}
        self.variable_values = {}

    def link_variable(self, key, variable_link):
        if key in self.variable_cont:
            self.variable_cont[key].append(variable_link)
            variable_link.set_val(self.get_variable(key))
        else:
            self.variable_cont[key] = [variable_link]
            self.variable_values[key] = 0.0

    def unlink_variable(self, key, variable_link):
        if key in self.variable_cont:
            if variable_link in self.variable_cont[key]:
                self.variable_cont[key].remove(variable_link)
                return 1
        raise IndexError("The variable is not linked or wrong!")

    def get_all_variables(self):
        return self.variable_cont.keys(), self.variable_values.values()

    def get_variable(self, key):
        if key in self.variable_values:
            return self.variable_values[key]

    def set_variable(self, key, value):
        if key in self.variable_cont:
            self.variable_values[key] = value
            for var_inst in self.variable_cont[key]:
                var_inst.set_val(value)
        else:
            self.variable_cont[key] = []
            self.variable_values[key] = value


class Number(GeneralMathOps):

    def __init__(self, val):
        self.meth_name = f"n"
        self.result_cntnr = val

    def exec_operation(self):
        return self.result_cntnr

    def return_printable(self):
        return str(round(self.result_cntnr, 4))


class Variable(GeneralMathOps):

    def __init__(self, name):
        self.meth_name = f"v"
        self.name = name
        self.result_cntnr = 0
        var_center.link_variable(name, self)

    def set_val(self, val):
        self.result_cntnr = val

    def exec_operation(self):
        return self.result_cntnr

    def return_printable(self):
        return self.name


class Negative(GeneralMathOps):
    def __init__(self, item):
        self.meth_name = f"ng"
        self.item = item

    def exec_operation(self):
        return self.item.exec_operation() * -1

    def return_printable(self):
        ptbl = self.item.return_printable()
        if ptbl[0] == "-":
            return ptbl[1:]
        else:
            return "-" + ptbl


class Add(GeneralMathOps):

    def __init__(self, *args):
        self.meth_name = f"a"
        self.children = args

    def exec_operation(self):
        self.result_cntnr = super().exec_operation()
        for child in self.children:
            self.result_cntnr += child.exec_operation()
        return self.result_cntnr

    def return_printable(self):
        bg = ""
        sep = "+"
        end = ""
        structure = bg
        for child in self.children:
            ptbl = child.return_printable()
            if ptbl[0] == "-":
                structure = structure[:-len(sep)] + ptbl + sep
            else:
                structure += ptbl + sep
        return structure[:-len(sep)] + end


class Mult(GeneralMathOps):

    def __init__(self, *args):
        self.meth_name = f"m"
        self.children = args

    def exec_operation(self):
        self.result_cntnr = super().exec_operation()
        for child in self.children:
            self.result_cntnr *= child.exec_operation()
        return self.result_cntnr

    def return_printable(self):
        bg = ""
        sep = "*"
        end = ""
        structure = bg
        for child in self.children:
            ptbl = child.return_printable()
            structure += ptbl + sep
        return structure[:-len(sep)] + end


class Power(GeneralMathOps):
    def __init__(self, item, power_item):
        self.meth_name = f"p"
        self.item = item
        self.power = power_item

    def exec_operation(self):
        bases = self.item.exec_operation()
        self.result_cntnr = bases ** self.power.exec_operation()
        return self.result_cntnr

    def return_printable(self):
        if self.item.meth_name not in ("b", "v", "n"):
            return f"({self.item.return_printable()})^{self.power.return_printable()}"
        return f"{self.item.return_printable()}^{self.power.return_printable()}"


class Bracket(GeneralMathOps):
    def __init__(self, item):
        self.meth_name = f"b"
        self.item = item

    def exec_operation(self):
        self.result_cntnr = self.item.exec_operation()
        return self.result_cntnr

    def return_printable(self):
        return f"({self.item.return_printable()})"


class Container:

    def __init__(self):
        self.text = ""
        self.children = []
        self.se: tuple

    def add_child(self,child):
        self.children.append(child)

    def set_text(self,text):
        self.text = text

    def set_se(self,start,end):
        self.se = (start,end)


class Parser:

    def __init__(self, text):
        self.c = Container()
        self.parse(-1, text, -1,self.c)
        self.__parse2(self.c,0)
        self.__parse3(self.c)
    def parse(self, start, text, level,rc):
        i = start + 1
        c0 = Container()
        print(len(text))
        while i < len(text):
            if text[i] == "(":
                i = self.parse(i, text, level + 1,c0)
            elif text[i] == ")":
                print(start, i, level)
                c0.set_text(text[start+1:i])
                c0.set_se(start,i+1)
                rc.add_child(c0)

                return i
            i += 1
        c0.set_text(text)
        c0.set_se(0,len(text))
        self.c = c0

    def __parse2(self,c,remvd):
        text =c.text
        for child in c.children:
            text = text[:child.se[0]-remvd] + "B" + text[child.se[1]-remvd:]
            remvd += child.se[1]-child.se[0]-1
            if child.children:
                self.__parse2(child,child.se[0]+1)

        c.set_text(text)

    def __parse3(self,c):
        text = c.text
        print("text: ",text)
        t0 = ""
        ##negatives
        for char in text:
            if char == "-":
                if t0:
                   if t0[-1] == "*":
                       t0 += "*N"
                   else:
                       t0 += "+N"
                else:
                    t0 +="N"
                continue
            t0 += char
        c.text = t0
        for child in c.children:
            self.__parse3(child)
        print(t0)






p = Parser("(x**2+9x-2031)+9-(2-(4*3+(y+9)))+(8-x)+(9+2392392)")
quit()

detail = 2000
var_center = VariableController()
min = -10
max = 10

x = np.linspace(min, max, detail)
y = np.linspace(max, min, detail).reshape(-1, 1)
x, y = np.meshgrid(x, y)

var_center.set_variable("x", x)
var_center.set_variable("y", y)
Equation_one = Power(Add(Number(8), Variable("x"), Number(19), Number(-102), Mult(Number(20), Number(5))),
                     Variable("y"))
Equation_two = Power(Add(Power(Variable("x"), Number(1)),
                         Negative(Power(Variable("y"), Number(1)))), Number(1))
print(Equation_two)
Equation_three = Negative(Equation_two)
plotting = Equation_two.calculate()

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure(1, (20, 8))
ax = fig.add_axes((0.1, 0.1, 0.9, 0.9), projection="3d")

x = var_center.get_variable("x")
y = var_center.get_variable("y")
z = plotting
# z[z>=10.0] = 10.0


z2 = Equation_three.calculate()
z = np.nan_to_num(z, copy=True, nan=0.0)
# ax.plot_surface(x, y, z2,color="b")
ax.plot_surface(y, x, z)
ax.plot_surface(y, x, -z)
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

fig.show()
