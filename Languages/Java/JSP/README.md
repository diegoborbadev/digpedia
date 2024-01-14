# What is JSP?
It is a server-side technology which is used for creating web applications. It is used to create dynamic web content. *JSP* consists of both *HTML* tags and *JSP* tags. In this, *JSP* tags are used to insert *JAVA* code into *HTML* pages. It is an advanced version of [*Servlet Technology*](../Servlet.md) i.e. a web-based technology that helps us to create dynamic and platform-independent web pages.

# JSP Elements (Tags)
*JSP* elements can be divided **into 4 different types**:

## Expression (<%=)
Is used to **output any data** on the generated page. These data are automatically converted to string and printed on the output stream.

**Example:**
```jsp
<html>  
    <body>  
        <p>The time is now: <%= new java.util.Date() %></p>
    </body>  
</html>  
```

##  Scriplets (<%)
Is used to **insert any amount of valid java code** and these codes are placed in the `_jsp Service` method by the *JSP* engine.

**Example:**
```jsp
<html>  
    <body>  
        <%  
        String name = "name_here";  
        out.print("welcome "+ name);  
        %>  
    </body>  
</html> 
```

Variables available to the *JSP* Scriptlets are:
- request
- response
- session
- out

TODO: Explain variables

## Directives (<%@)
Is used to import packages, and define error-handling pages or the session information of the *JSP* page.

There are three types of directives:
- page
- include
- taglib

TODO: Explain types

**Example:**
```jsp
<%@page import="java.util.Date" %>  

<html>  
    <body>  
        <p>The time is now: <%= new java.util.Date() %></p>
    </body>  
</html> 
```

## Declarations (<%!)
Is used to defining the functions and variables to be used in the *JSP*.

**Example:**
```jsp
<%@page import="java.util.Date" %>  

<html>  
    <body> 
        <%!
        Date the Date = new Date(); 
        Date getDate() {
            return theDate;
        }
        %>
        <p>The time is now: <%= getDate() %></p>
    </body>  
</html> 
```