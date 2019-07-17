# Tolya Will Be Shocked
Tolya Will Be Shocked (TWBS) is a trial to make autolearning model which will prepare your dataset and find the best model and parameters to it. Besides it is made to shock Tolya

## Getting Started
Brief [plan](https://gist.github.com/MarcDiethelm/7303312) of collaboration

### [Forking](https://help.github.com/articles/fork-a-repo/)
First of all you need to fork our joint repository.
To do this go to [repository](https://github.com/RageAgainstTheMachine101/Tolya_will_be_shoked) and press button `Fork` at the top right corner. It will clone repo to your github account.
Next you should add forked repository to your local machine. Press button `Clone or download` at forked repository page in **your** account. Copy url and paste it into terminal command:

*Note:  {} are used to indicate placeholder for substitution*

```git clone {copied link}```

After it go to main repository from which you have forked. Again press button `Clone or download` here and run this command:

```git remote add upstream {copied link}```

Now origin is your own copy where you will commit changes first and upstream is a shared repo where you will push afterwards.
You can use command 

```git remote -v```

to make sure that you have your own copy of repository and joint repo (output normally contains 4 lines - 2 for origin and 2 for upstream).


### Branches
To make commits you should create branches where you will make them first. You 
- make changes at files in your new branch
- commit it
- merge with master
- push changes to your local repo (`git push origin`)
- create a pull request (look below for this)
After merging branch with joint repository you can delete it.

Look at branches

```git branch```


Create branch

```git branch new_branch```


Switch to branch

```git checkout new_branch```


Merge branch with master - go to master branch and run

```git merge new_branch```


Delete branch

```git branch -d new_branch```


These topics are quite enough:
https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging
https://git-scm.com/book/en/v2/Git-Branching-Branch-Management


### [Pull requests](https://help.github.com/articles/about-pull-requests/)
After pushing something new in your own repository go to fork in your github account, `Pull requests` tab and press button `New pull request`. You\`ll see changed files which you can send in request to joint repository. Press `Create pull request` to do it.


To type co instead of checkout and other substitutions look for git aliases [here](https://githowto.com/ru). Aliases which proposed in one chapter are common, so use them.


## Prerequisites
- Python
	- numpy
	- pandas
	- scikit

## Authors
Will be added later
