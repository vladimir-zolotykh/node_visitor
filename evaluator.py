#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class Node:
    pass


class Number(Node):
    def __init__(self, value):
        self.value = value


class UnaryOperator(Node):
    pass


class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOperator):
    pass


class Negate(UnaryOperator):
    pass


"""
t1 = Sub(10, 3)
"""
