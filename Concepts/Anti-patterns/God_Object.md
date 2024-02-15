# What is a God Object?
In short a *God Object* (a.k.a. *Omniscient* or *All-Knowing Object*) is a data structure that **does too many things and knows too much**. It references a large number of distinct types, has too many unrelated or uncategorized methods, or some combination of both.

## What is the problem?
The *God Object* is a violation of the [*Single-Responsibility Principle*](../SOLID/SRP.md) and the [*Open-Closed Principle*](../SOLID/OCP.md). It is a sign of a poor design and it makes the code **difficult to maintain, test, and understand**.