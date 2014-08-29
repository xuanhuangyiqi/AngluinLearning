AngluinLearning
==============

# Introduction:

## 中文:

这是一个 Angluin Learning Algorithm 的Python实现，算法通过反复询问每个句子是否属于正则语言L，来学习出L对应的最简DFA。本程序在此基础上可以生成该语言对应的正则表达式形式。关于该算法，慕尼黑工业大学的Helli提供了[Haskell的实现](https://github.com/Helli/LearningFormalLanguages)

## Deutsch:

Dieses Projekt ist Python implementiert Anluin Learning Algorismus, dies durch mehrere malige Anfrage, ob ein Satz zu der regulärer Sprache L gehört, ein reduziertes DFA gelernt. Auf dieser Basis produziert dieses Program die entsprechende Form der Regex. Außerdem hat Helli aus TUM ein [Haskell Implementiertes Program](https://github.com/Helli/LearningFormalLanguages) angeboten.

# Usage:

    > python main.py
    Enter the charset in a line:
    12
    Is '' a word of your language?(y/n)
    y
    Is '1' a word of your language?(y/n)
    n
    Is '2' a word of your language?(y/n)
    n
    Is '11' a word of your language?(y/n)
    n
    Is '12' a word of your language?(y/n)
    y
    Observation Table:
    |R/S    |ϵ |
    |ϵ  | 1 |
    |1  | 0 |
    |ϵ.2    | 0 |
    |1.1    | 0 |
    |1.2    | 1 |
    Regex:  ((12(1)*2))*
    Is the result right?(y/n)n
    Can you give a counter example?22
    Is '21' a word of your language?(y/n)
    n
    Is '22' a word of your language?(y/n)
    n
    Is '221' a word of your language?(y/n)
    n
    Is '222' a word of your language?(y/n)
    n
    Is '112' a word of your language?(y/n)
    n
    Is '122' a word of your language?(y/n)
    n
    Is '212' a word of your language?(y/n)
    n
    Is '2212' a word of your language?(y/n)
    n
    Is '2222' a word of your language?(y/n)
    n
    Observation Table:
    |R/S    |ϵ  |2 |
    |ϵ  | 1     | 0 |
    |1  | 0     | 1 |
    |2  | 0     | 0 |
    |22     | 0     | 0 |
    |1.1    | 0     | 0 |
    |1.2    | 1     | 0 |
    |2.1    | 0     | 0 |
    |22.1   | 0     | 0 |
    |22.2   | 0     | 0 |
    Regex:  ((12))*
    Is the result right?(y/n)y
