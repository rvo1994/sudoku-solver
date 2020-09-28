# GitHub best practices

Find here below some best practices when using GitHub.

## Launching the Front App

To launch the SPA on linux or mac, you have to follow these steps (inside bash console):

1. Clone the repo: `git clone git@github.com:rvo1994/sudoku-solver.git`

2. Change directory: `cd sudoku-solver`


## GitHub issues

Issues are kind of like tasks you can assign to people you are working with. To create a new issue:

1. Press the "New issue" button

2. Enter a title

3. Assign someone (you can assign yourself) - Optional

4. Add a label - Optional


## Create a new Pull Request (PR)

Generally, you want to create a new branch before adding code to the repo. Before creating a new branch, make sure that the origin branch is up-to-date.

### Update origin branch

1. `git fetch`

2. `git pull`

### Create new branch

1. `git checkout -b new_branch_name`

### Push changes to the origin branch

Notice: the message you add to your commit can contain keywords like 'close', 'fix', 'resolve'...

1. `git add .`

2. `git commit -am "...message..."`

3. `git push -u origin new_branch_name`

## Switch to origin branch and delete local branch

1. `git checkout dev`

2. `git branch -d new_branch_name`

## Staging and Production Branches

GitHub does not provide a flow with staging and production stage. As a result, we have to do it manually in the console.

When merging all changes to staging branch:

1. `git checkout staging`

2. `git merge dev`

3. `git push`

When merging all changes to production branch:

1. `git checkout production`

2. `git merge staging`

3. `git push`

