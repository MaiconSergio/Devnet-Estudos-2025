# Lab: Git Basics

## Introduction

In this laboratory, we will apply the principles of Git version control not to a traditional software development context, but rather to managing and versioning configurations for Cisco routers. Networking equipment such as routers have configurations that can be critical for the operation and security of the entire network, hence managing changes and keeping a history of configurations can be as vital as managing changes to software code.

Cisco routers, like many other network devices, have textual configuration files which can be viewed, edited, saved, and loaded by network administrators. This makes them suitable for versioning using Git, allowing us to track changes, branch configurations for different requirements or testing, and revert to previous states in case of misconfiguration or other issues.

Throughout this lab, we will simulate scenarios where we are making changes to the configuration files of Cisco routers. We will use Git commands to initialize a repository, make and commit changes, create branches, and explore other functionalities such as merging and working with remote repositories.

Let's dive in and see how Git can be a powerful tool for network configuration management!

### Configuration Reference

https://www.cisco.com/c/en/us/support/docs/switches/nexus-9000-series-switches/118978-config-vxlan-00.html

### Git Lab

1. **Install Git**
   - `apt-get install git`
   - **Q:** Install on MAC, Windows, and other Linux distributions?
   - For MAC, use `brew install git`
   - For Windows download from the official Git website.
   - For other Linux distros, use the package manager like `yum` or `zypper`.

### Checking Current Git User

2. **Initialize Git Repository**
   To initialize a new Git repository and begin tracking an existing directory, run:
   - `git init`
   Next, create a folder named `assets` to store your assets.
   Copy the diagram image into the `assets` folder.

3. **Set Initial Branch Name**
   - `git init --initial-branch=<name>`

4. **Check Repository Status**
   - `git status`

5. **View Commit Logs**
   - `git log`

6. **Create a Commit**
   - `git commit -m "message"`
   - **Q:** Example without any file added?
   - **A:** This command will result in an error as there are no changes to commit.

7. **Configure User Name**
   To check the current Git user in your system, use the following command:
   - `git config --global user.name`
   To set a new user name, use:
   - `git config --global user.name "<name>"`
   To remove the configured user name, use:
   - `git config --global --unset user.name`

8. **Add Files to Stage**
   - `git add <name>` 
   - `git add .`

9. **Q:** How to remove files from stage?
   - **A:** Use `git restore --staged <file>`.

10. **Commit Changes**
    - `git commit -m "message"`
    - **Q:** With a first file added?
    - **A:** This will create a new commit in the history.

11. **View Commit Logs**
    - `git log`

12. **Amend in Last Commit**
    - `git commit --amend`

13. **Undo Changes**
    - `git reset`
    - `git reset --hard HEAD~1`
    - **Q:** Explain HEAD -> main.
    - **A:** HEAD points to the latest commit in the current branch, which is 'main' by default.

    **Load a Previous Commit**
    To check out a specific commit, you first need to find the commit hash:
    - `git log`
    Once you have the commit hash, use the `git checkout` command:
    - `git checkout <commit-hash>`

    **Revert to a Previous Version**
    If you've made a mistake in the latest commit you can use the `git reset` command. You first need to find the commit hash:
    - `git log`
    Revert to the Previous Version:
    - `git reset --hard <commit-hash>`
    Be cautious while using `git reset --hard` as it will discard all the changes made after the specified commit, including those in the working directory and staging area.

14. **Q:** What is a commit hash?
    - **A:** It's a unique identifier for each commit, generated through a cryptographic hash function.

15. **Q:** Git commit without any parameter?
    - **A:** It opens a text editor to write a commit message.

16. **Show Commit Details**
    - `git show`
    - **Q:** What does +++ and --- represent in git?
    - **A:** They represent lines added (+++) or removed (---) in the file.

17. **Compare Changes**
    Show the changes between commits, commit and working tree, etc:
    - `git diff-tree -p <commit-hash or branch>`
    Show differences between the working directory and the index (staging area). It is useful to see the changes you made before staging them:
    - `git diff [branch]`
    View differences using external tools, providing a side-by-side view of the changes:
    - `git difftool`

18. **Discarding Changes Without Restore**
    If you have made changes to a file and want to discard them, reverting the file to its state at the last commit:
    - `git checkout -- <filename>`
    If you want to discard changes in all files, you can use:
    - `git checkout -- .`

19. **List, Create, and Switch Branches**
    To list all the branches in your repository:
    - `git branch`
    - **Q:** What does the * represent in the current branch?
    - **A:** The * indicates the branch that is currently checked out.
    To create a new branch:
    - `git branch <new-branch-name>`
    To switch to the new branch:
    - `git checkout <new-branch-name>`    
    Alternatively, you can create a new branch and switch to it directly using:
    - `git checkout -b <new-branch-name>`

20. **Delete Branch**
    - `git checkout <name>`
    - `git branch -d <name>`

21. **Delete Branch Forcefully**
    - `git branch -D <name>`

22. **Merge Branch**    
    - `git merge <branch>`
    - **Q:** Create a new commit in the branch main.
    - **A:** This will merge changes from the specified branch into the main.

    - **Q:** Bring the new changes in main to an old branch?
    - **A:** Use `git merge main` while on the old branch.

23. **Resolve Conflicts**
    When you try to merge branches using:
    - `git merge main`

    You might encounter merge conflicts like the one shown:
    ```
    Auto-merging <filename>
    CONFLICT (content): Merge conflict in <filename>
    Automatic merge failed; fix conflicts and then commit the result.
    ```
    This indicates that there are conflicting changes in the `<filename>` file that Git couldn’t resolve automatically.
    
    **Resolving Conflicts:**
    1. **Open the Conflicted File** and look for the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`). Edit the file to fix the conflicts.
    2. **Mark the File as Resolved**:
       - `git add <filename>`
    3. **Commit the Resolved Changes**:
       - `git commit`

24. **Basic Integration with GitHub**
    - **Q:** Create a new repo on GitHub.
    - **A:** Go to GitHub, click on 'New', and follow the instructions. 
    - **Q:** Add the working copy as origin.
    - **A:** Use `git remote add origin <url>`.

25. **Set Main Branch and Push**
    If necessary set the main branch:
    - `git branch -M main`
    - `git push -u origin main`
    To push all local branch:
    - `git push --all`

26. **Manage Remote Repositories**
    - `git remote --verbose`
    - `git remote add origin <url>`
    - `git remote remove <name>`

27. **Update Local Repository**
    - `git pull`

28. **Update Local Branch List**
    When a branch has been removed from the remote repository, it may still appear in your local branch list. To synchronize:
    - `git fetch --prune`

29. **Clone a Repository**
    - `git clone <repo_url>`

30. **Git Ignore**
    - **Q:** How to use .gitignore?
    - **A:** Create a `.gitignore` file in the root of your repo and list files or directories to ignore.

31. **Best Practices**
    - **Q:** What are the basic best practices for GIT?
    - **A:** Commit often, write meaningful commit messages, sync regularly, and resolve conflicts promptly.

32. **GitHub Compare and Pull Request**
    - **Q:** How to use compare and create a pull request in GitHub?
    - **A:** Use the 'compare' feature on GitHub to select branches and create a pull request for review and merging.
