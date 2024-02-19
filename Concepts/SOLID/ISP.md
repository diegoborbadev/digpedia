# Interface Segregation Principle
## What is ISP?
The *Interface Segregation Principle* states that **a client should not be forced to implement an interface that it doesn't use**. This means that we should not have a single interface that contains methods that are not used by the client. Instead, we **should have multiple interfaces, each containing methods that are used by the client**.

For example, consider the following interface:

```java
public interface Animal {
    public void eat();
    public void run();
    public void hunt();
    public void giveAPaw();
}
```

Imagine now a `Dog` class that implements the `Animal` interface:

```java
public class Dog implements Animal {
    @Override
    public void eat() {
        // Dogs can eat
    }

    @Override
    public void run() {
        // Dogs can run
    }

    @Override
    public void hunt() {
        // Dogs don't hunt (Exception!)
        throw new UnsupportedOperationException();
    }

    @Override
    public void giveAPaw() {
        // Dogs can give a paw
    }
}
```

And now imagine a `Wolf` class that also implements the `Animal` interface:

```java
public class Wolf implements Animal {
    @Override
    public void eat() {
        // Wolves can eat
    }

    @Override
    public void run() {
        // Wolves can run
    }

    @Override
    public void hunt() {
        // Wolves can hunt
    }

    @Override
    public void giveAPaw() {
        // Wolves don't give a paw (Exception!)
        throw new UnsupportedOperationException();
    }
}
```

Both `Dog` and `Wolf` classes are forced to implement **methods that they don't use**, this is a violation of the *Interface Segregation Principle*. To fix this, we should have multiple interfaces, each containing the correct methods:

The `Animal` interface should contain only the `eat` and `run` methods:
```java
public interface Animal {
    public void eat();
    public void run();
}
```

And know we have the **segregated** interface `DomesticAnimal`:
```java
public interface DomesticAnimal extends Animal {
    public void giveAPaw();
}
``` 

And `WildAnimal`:
```java
public interface WildAnimal extends Animal {
    public void hunt();
}
```

By consequence, the `Dog` class should implement the `DomesticAnimal` interface:
```java
public class Dog implements DomesticAnimal {
    @Override
    public void eat() {
        // Dogs can eat
    }

    @Override
    public void run() {
        // Dogs can run
    }

    @Override
    public void giveAPaw() {
        // Dogs can give a paw
    }
}
```

And the `Wolf` class should implement the `WildAnimal` interface:
```java
public class Wolf implements WildAnimal {
    @Override
    public void eat() {
        // Wolves can eat
    }

    @Override
    public void run() {
        // Wolves can run
    }

    @Override
    public void hunt() {
        // Wolves can hunt
    }
}
```
Now, both `Dog` and `Wolf` classes are implementing only the methods that they use, and we are following the *Interface Segregation Principle* correctly.

See the [*source code here*](https://github.com/diegoborbadev/solid-principles-java/tree/main/src/main/java/ISP).