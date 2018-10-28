from MisteriumGameParsers.PrecompiledExpressions import CHARACTERISTIC_EXPRESSIONS, PROCENT_EXPRESSION

def get_characteristic_from_line(line):
    for expr in CHARACTERISTIC_EXPRESSIONS:
        res = expr.search(line)
        if res:
            return res.group()

def get_first_procents_from_line(line):
    expr = PROCENT_EXPRESSION
    res = expr.search(line)
    if res:
        return res.group()
