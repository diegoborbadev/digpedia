# Repository
### Create a new empty repository
```bash
$ git init
```

### Clone an existing repository
```bash
$ git clone <url>
```

### Fetch from a remote repository
```bash
$ git fetch
```

### Pull from a remote repository
```bash
$ git pull
```

### Merge 
#### Merge two branches
```bash
$ git merge <branch_name>
```

# Branch

### Create a new branch
#### Just create a new branch
```bash
$ git branch <branch_name>
```

#### Create a new branch and switch
```bash
$ git switch -c <branch_name>
```

### Switch Branch
```bash
$ git switch <branch_name>
```

### Delete a branch
```bash
$ git branch -d <branch_name>
```

### Return to previously checked out branch
```bash
$ git switch -
```

### Show the branch pointers
```bash
$ git log --oneline --decorate
```
**Note:** `git log` doesn’t show all the branches all the time, it will only show commit history below the branch you’ve checked out. To show all of the branches, use `--all`.

### Check HEAD value
```bash
$ git show head
```

### Check ORIG_HEAD value
```bash
$ git log -1 ORIG_HEAD
```