# Introduction
*Git* is a free and open-source [*Version Control Software (VCS)*](../../Concepts/Version_Control/README.md) created by *Linus Torvalds* in 2005.

# Git vs GitHub
***Git* is a version control system** that allows developers to track changes in their code, and ***GitHub* is a web-based hosting service** for *Git* repositories. In other words, you can use *Git* without *Github*, but you cannot use *GitHub* without *Git*.

# Concepts
Some of the important concepts in *Git*.  
See: [*Git Documentation*](https://git-scm.com/doc)

## What is a repository?  
A repository is the most basic element of *Git*, it contains all of the project files (including documentation), and stores each file's revision history.  
See: [*Repository Basic Commands*](Basic_Commands.md#repository)

### Types of Repositories
**Bare Repositories:** is a ***server-side repository*** that does not have a working directory, the central hub for collaboration, it only contains the versioned data and the *Git* history 

**Working  Repositories:** a.k.a. *Non-Bare Repositories*, is a ***client-side repository*** that has a working directory, it contains the versioned data, the *Git* history, and the working directory, they are typically [*cloned*](Basic_Commands.md#clone-an-existing-repository) from a bare repository or another non-bare repository.

## What is a commit?  
A *commit* is a set of changes to the files and folders in your project. A commit exists in a branch. For more information, see: [*About commits*](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/about-commits).

## What HEAD means?  
Well, `HEAD` is a special pointer to the local *branch* you’re currently on. In other words, `HEAD` is a reference to the last *commit* in the currently checked-out *branch*.

## What is a branch?  
A *branch* is a **independent line of development**, in other words, a parallel version of your *repository*. *Branches* serve as an abstraction for the *edit/stage/commit* process, new **commits are recorded in the history for the current branch**, which results in a *fork* in the history of the project.

### Creating a New Branch
When you [*create a new branch*](Basic_Commands.md#create-a-new-branch), you are creating a new pointer to the same commit you’re currently on for you to move around. 

### Switching Branches
When you [*switch branches*](Basic_Commands.md#switch-branch), this moves `HEAD` to point to the selected branch.

It’s important to note that **when you switch branches in Git, files in your working directory will change**. If you switch to an older branch, your working directory will be reverted to look like it did the last time you committed on that branch, and if *Git* cannot do it cleanly, it will not let you switch at all.

<!-- ## What is a fork?  
TODO -->

<!-- ## What is a merge?
TODO -->