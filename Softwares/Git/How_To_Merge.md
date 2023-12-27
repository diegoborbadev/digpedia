# How it works
*Merge* will **combine multiple sequences of commits into one unified history**, in the most frequent use cases, `git merge` is used to combine two branches.

## Combining two branches
### Before merge
Before performing a merge there are a couple of preparation steps to take to ensure the merge goes smoothly:
- Ensure that `HEAD` is pointing to the correct *merge-receiving branch*, if it isn't, you can [*switch*](Basic_Commands.md#switch-branch) to it.
- Make sure the receiving branch and the merging branch are up-to-date with the latest remote changes. See: [*Pull*](Basic_Commands.md#pull-from-a-remote-repository) & [*Fetch*](Basic_Commands.md#fetch-from-a-remote-repository).

### Performing the merge
Assume the following history exists and the current branch is `master`:
```bash
      A---B---C dev
     /
D---E---F---G master
```

Then [*merge*](Basic_Commands.md#merge-two-branches) will replay the changes made on the `dev` branch since it diverged from `master` (`E`) until its current commit (`C`) on top of `master`, and record the result in a new commit along with the names of the two parent commits and a log message from the user describing the changes. 

```bash
      A---B---C dev
     /         \
D---E---F---G---H master
```

**Note:** Before the operation, `ORIG_HEAD` is set to the tip of the current branch (`C`), after the operation, `ORIG_HEAD` is set to the commit that was created (`H`).

