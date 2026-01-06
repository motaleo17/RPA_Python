import sys
from pywinauto import Application
from lib.calculator import Calculator

# =========================
# VALIDAÇÃO DE PARÂMETROS
# =========================
if len(sys.argv) != 4:
    print("Uso correto:")
    print("python script.py <numero1> <operador> <numero2>")
    sys.exit(1)

n1 = sys.argv[1]
op = sys.argv[2]
n2 = sys.argv[3]

if not n1.isdigit() or not n2.isdigit():
    print("Os números devem ser inteiros")
    sys.exit(1)

if op not in ["+", "-", "*", "/"]:
    print("Operador inválido")
    sys.exit(1)

# =========================
# ABRIR CALCULADORA
# =========================
print("Abrindo calculadora...")

app = Application(backend="uia").start("calc.exe")

# 🔑 Conecta ao processo correto
calc_window = app.window(title_re="Calculadora")

# Aguarda ficar pronta
calc_window.wait("exists ready visible", timeout=15)

print("Calculadora pronta")

# =========================
# OPERAÇÃO
# =========================
calc = Calculator(calc_window)

calc.number(n1)

if op == "+":
    calc.add()
elif op == "-":
    calc.subtract()
elif op == "*":
    calc.multiply()
elif op == "/":
    calc.divide()

calc.number(n2)
calc.equals()

print("Operação executada com sucesso")

sys.exit(0)
