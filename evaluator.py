#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class Node:
    pass


class Number(Node):
    def __init__(self, value):
        self.value = value


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand


class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOperator):
    pass


class Sub(BinaryOperator):
    pass


class Mul(BinaryOperator):
    pass


class Div(BinaryOperator):
    pass


class Negate(UnaryOperator):
    pass


# Representation of 1 + 2 * (3 - 4) / 5
t1 = Sub(Number(3), Number(4))
t2 = Mul(Number(2), t1)
t3 = Div(t2, Number(5))
t4 = Add(Number(1), t3)


class Visitor:
    def visit(self, node):
        cls_name = type(node).__class__.__name__
        method_name = f"visit_{cls_name}"
        method = getattr(self, method_name, self.visit_generic)
        return method(node)

    def visit_generic(self, node):
        raise TypeError(f"Do not know how to visit {node}")


class Evaluator(Visitor):
    def visit_number(self, node):
        return node.value

    def visit_sub(self, node):
        return self.visit(node.left) - self.visit(node.right)


if __name__ == "__main__":
    res = Evaluator(t1)
    print(f"{res = }")
