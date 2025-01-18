# Overview and Terminology

## Expressions and Environments

Scheme works by evaluating **expression** in **environments**. Every expression evaluates to a **value**. Some expressions are **self-evaluating**.which means they are both an expression and a value, and that it evaluates to itself.

A **frame** is a mapping from symbols(names) to values, as well as an optional parent frame. The current environment refers to the current frame, as well as a chain of parent frames up to the **global frame**(which has no parent). When looking up a symbol in an environment, Scheme first checks the current frame and returns the corresponding value if it exists. If it doesn't, it repeats this process on each subsequent parent frame, until either the symbol is found, or there are no more parent frames to check.

## Atomic Expressions

There are several **atomic** or **primitive** expressions. Numbers, booleans, strings, and the empty list (`nil`) are all both atomic and self-evaluating. Symbols are atomic, but are not self-evaluating (they instead evaluate to a value that was previously bound to it in the environment).

## Call Expressions

The Scheme expressions that are not atomic are called **combinations**, and consist of one or more **subexpressions** between parentheses. Most forms are evaluated as **call expressions**, which have three evaluation steps:

1. Evaluate the first subexpression (the operator), which must evaluate to a **procedure** (see below).
2. Evaluate the remaining subexpressions (the operands) in order.
3. Apply the procedure from step 1 to the evaluated operands (**arguments**) from step 2.

These steps mirror those in Python and other languages.

## Special Forms

However, not all combinations are call expressions. Some are **special forms**. The interpreter maintains a set of particular symbols (sometimes called **keywords**) that signal that a combination is a special form when they are the first subexpression. Each special form has it's own procedure for which operands to evaluate and how (described below). The interpreter always checks the first subexpression of a combination first. If it matches one of the keywords, the corresponding special form is used. Otherwise, the combination is evaluated as a call expression.

## Symbolic Programming

Scheme's core data type is the **list**, built out of pairs as described below. Scheme code is actually built out of these lists. This means that the code `(+ 1 2)` is constructed as a list of the `+` symbol, the number 1, and the number 2, which is then evaluated as a call expression.

Since lists are normally evaluated as combinations, we need a special form to get the actual, unevaluated list. `quote` is a special form that takes a single operand expression and returns it, unevaluated. Therefore, `(quote (+ 1 2))` returns the actual list of the symbol `+`, the number 1, and the number 2, rather than evaluating the expression to get the number 3. This also works for symbols. `a` is looked up in the current environment to get the corresponding value, while `(quote a)` evaluates to the literal symbol `a`.

Because `quote` is so commonly used in Scheme, the language has a shorthand way of writing it: just put a single quote in front of the expression you want to leave unevaluated. `'(+ 1 2)` and `'a` are equivalent to `(quote (+ 1 2))` and `(quote a)`, respectively.

