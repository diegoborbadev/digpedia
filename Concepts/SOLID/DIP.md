# Dependency Inversion Principle
## What is DIP?
The *Dependency Inversion Principle* states that **high-level modules should not depend on low-level modules**, but rather both should depend on abstractions. Furthermore, abstractions should not depend on details, but rather details should depend on abstractions.

For example:
```java
public class ClassA {
    ClassB objectB;

    public ClassA(ClassB objectB) {
        this.objectB = objectB;
    }

    public void foo() {
        // Some code
        // And then call the method of ClassB
        objectB.doSomething();
    }
}
```

In the above example, `ClassA` is a high-level module and `ClassB` is a low-level module. `ClassA` is directly dependent on `ClassB`.

But, *DIP* is telling us to invert the dependency using an abstraction. So, we can do it by creating an interface: 
```java
public interface InterfaceB {
    public void doSomething();
}
```

By doing this, we can change the `ClassA` to use the `InterfaceB` instead of `ClassB`:
```java
public class ClassA {
    InterfaceB objectB;

    public ClassA(InterfaceB objectB) {
        this.objectB = objectB;
    }

    public void foo() {
        // Some code
        // And then call the method of InterfaceB
        objectB.doSomething();
    }
}
```

Now, `ClassA` is not directly dependent on `ClassB`, but rather on `InterfaceB`, the same goes for `ClassB`. This is the essence of *DIP*.

See the [*source code here*](https://github.com/diegoborbadev/solid-principles-java/tree/main/src/main/java/DIP).

## Why is the DIP important?
When developing code for applications, it is common to organize our logic into multiple modules. However, this can lead to a codebase with dependencies. One of the motivations behind the *Dependency Inversion Principle* is to **prevent us from depending upon modules that often change**. Concrete classes often experience frequent modifications, whereas abstractions and interfaces are subject to less frequent changes. This approach simplifies tasks like bug fixing, code recompiling, or merging different branches.

Nevertheless, the significance of *DIP* extends beyond this. It plays a pivotal role in achieving loosely coupled and maintainable systems, complementing concepts such as [*Polymorphism*](../Polymorphism.md) and [*Dependency Injection*](../Dependency_Injection.md)
