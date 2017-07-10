from git import *
from git.repo import Repo

repo_dir='/tmp/test'
url="https://github.com/narasimha18sv/test.git"
#Repo.clone_from(url, repo_dir)
repo = Repo(repo_dir)
file_list=["anaconda-ks.cfg"]
commit_message = 'Add simple regression analysis'
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()
