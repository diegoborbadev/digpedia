# Single-Responsibility Principle
## What is SRP?
This principle states that a class/method/interface **should only have one responsibility**. For example:

```java
public class Book {
    // Properties
    private String name;
    private String author;
    private String text;

    // Constructor

    /*
    * Methods relate to the book properties
     */

    // Replace a word in text
    public String replaceWordInText(String word, String replacementWord){
        return text.replaceAll(word, replacementWord);
    }

    // Check if a word is in text
    public boolean isWordInText(String word){
        return text.contains(word);
    }

    /*
    * Method unrelated to the book, it is just output
     */

    // Print text to console
    public void printTextToConsole(){
        System.out.println(text);
    }

    // Getters and setters
}
```

The `Book` class should only handle the book properties, but, it violates the *SRP* because it has **two responsibilities: managing the book properties and printing the text to the console**. The `isWordInText` method should be in a different class, for example, in a `BookPrinter` class:

```java
public class BookPrinter {
    /*
     * Method unrelated to the book, it is just output
     */

    // Print the book text to console
    public void printTextToConsole(Book book){
        System.out.println(book.getText());
    }
}
```

See the [*source code here*](https://github.com/diegoborbadev/solid-principles-java/tree/main/src/main/java/SRP).

## Why is SRP important?
The *SRP* is important because it **makes the code more readable, maintainable, and testable**. It also helps to avoid the [*God Object*](../Anti-patterns/God_Object.md) anti-pattern.

### Hints:
Try to describe the main responsibility of a class, method, or interface. If you **can't describe it in a single sentence, it may have more than one responsibility**.

Also, try to write the name of the methods describing their responsibility. For example, if you have the `signUpAndLogin()` method, it probably violates the *SRP* principle.
