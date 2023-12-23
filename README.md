# DigPedia

[My own](http://github.com/diegoborbadev) knowledge base: explanations, links, and examples on various subjects.

[Click here](Summary.md) to access summary; more explanations below.

## Structure
The file structure is based on 3 things:
- **Topics:** Each folder is one ***topic***; a ***topic*** can have ***subtopics***, each ***subtopic*** can have its own ***subtopics***, and so on.
- **Articles:** Each file, except for *READMEs* and *summaries*, is an *article*.
- **READMEs:** Except for this one that you are currently reading, all *READMEs* are introductions to their respective ***topics***.

## Summaries

All summaries are automatically generated by [*Script.py*](Script.py), based on the directory structure.

The summaries structure is:
- *README.md first (if it exists)*
- *Articles*
- ***Topics***

For example:

```
.
├── Topic1/
│   ├── Subtopic1/
│   │   ├── Subtopic1_Article.md
│   │   └── Summary.md
│   ├── Topic1_Article.md
│   ├── README.md
│   └── Summary.md
└── Topic2/
    ├── Topic2_Article.md
    └── Summary.md
```

Considering this structure, the content of `Topic1/Summary.md` will be:
- [*README*]()
- [*Topic1 Article*]()
- [***Subtopic1***]()

But, the content of `Topic2/Summary.md` will be:
- [*Topic2 Article*]()