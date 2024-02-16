# Open-Closed Principle
## What is OCP?
The *Open-Closed Principle* states that software entities **should be OPEN for extension, but CLOSED for modification**. This means that a component **should be easily extendable without modifying the component itself**. For example:

```java
public class PaymentManager {
    public void pay(double amount) {
        if (validateCard()) {
            // Payment Logic
        }
    }

    private Boolean validateCard() {
        // Validation Logic
    }
}
```

Let's suppose that you wrote the `PaymentManager` class to manage Credit card payments, and it is working fine. But now, you need to add a new payment method, for example, Debit card. It's ok, because Credit cards and Debit cards are similar.

But, what if you need to add a new payment method, for example, Bitcoin? You will need to **modify the `PaymentManager` class, and this violates the *OCP***.

```java
public class PaymentManager {
    public void pay(double amount) {
        if(isCard()) {
            if (validateCard()) {
                // Payment Logic
            }
        } else if(isBitcoin()) {
            if (validateBitcoin()) {
                // Payment Logic
            }
        }
    }

    private Boolean validateCard() {
        // Validation Logic
    }

    private Boolean validateBitcoin() {
        // Validation Logic
    }
}
```

So, how to solve this problem? **With the correct level of abstraction**:

### PaymentManager class:
```java
public class PaymentManager {
    public void pay(PaymentMethod paymentMethod, double amount) {
        if(paymentMethod.validate()) {
            paymentMethod.pay(amount);
            // Send a confirmation email (Example)
        } else {
           // Handle the validation error
        }
    }
}
```

### PaymentMethod interface:
```java
public interface PaymentMethod {
    public void pay(double amount);
    public boolean validate();
}
```

Now you can add any payment method without modifying the `PaymentManager` class, you just need to create a new class that implements the `PaymentMethod` interface.

See the [*source code here*](https://github.com/diegoborbadev/solid-principles-java/tree/main/src/main/java/OCP).