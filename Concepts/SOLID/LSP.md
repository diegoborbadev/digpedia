# Liskov Substitution Principle
## What is LSP?
The *Liskov Substitution Principle* states that **objects of a superclass should be replaceable with objects of its subclass without affecting the functionality of the program**. In other words, a subclass should override the methods of the superclass in a way that does not break the functionality of the program. 

For example, if you have the interface `Bird`:
```java
public interface Bird {
    public void fly();
    public void peck();
}
```

And you decide to create a class `Duck` that implements `Bird`:
```java
public class Duck implements Bird {
    @Override
    public void fly() {
        // Duck flies
    }

    @Override
    public void peck() {
        // Duck pecks
    }
}
```

That's fine, but if you decide to create a class `Penguin` that also implements `Bird`:
```java
public class Penguin implements Bird {
    @Override
    public void fly() {
        // Penguin can't fly (Exception!)
        throw new UnsupportedOperationException();
    }

    @Override
    public void peck() {
        // Penguin pecks
    }
}
```

The `Penguin` class violates the *Liskov Substitution Principle* because it throws an exception when the `fly` method is called. **This is not the expected behavior of the `Bird` interface**.

So, what is the correct way to implement the `Penguin` class? **With the correct level of abstraction**:
```java
public interface Bird {
    public void peck();
}   
```

Not all birds can fly, so the `fly` method should not be part of the `Bird` interface, it should be part of a more specific interface, like `FlyingBird`:
```java
public interface FlyingBird extends Bird {
    public void fly();
}
```

Now, the `Duck` class should implement the `FlyingBird` interface:
```java
public class Duck implements FlyingBird {
    @Override
    public void fly() {
        // Duck flies
    }

    @Override
    public void peck() {
        // Duck pecks
    }
}
```

And the `Penguin` class should implement the `Bird` interface:
```java
public class Penguin implements Bird {
    @Override
    public void peck() {
        // Penguin pecks
    }
}
```

If you have many classes that don't implements correctly some methods of an interface, you are probably violating the *Liskov Substitution Principle*.

See the [*source code here*](https://github.com/diegoborbadev/solid-principles-java/tree/main/src/main/java/LSP).