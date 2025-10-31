#README
following is the description of the code
make some revision
ctrl + S
try to use GUI interface
this sentence will be show at github

download python git db browser

#Install
. Git
. DB Browser for SQLite

#Initialize Environment
- in terminal
- installing git
- using 'git clone repository.git' to hard copy github repository
- git clone https://github.com/zaoa3345678-arch/SSD_Midterm.git
- rd .git (remove .git folder (hidden in the repository))
. git --version
. git config --global user.name 'Aaron name'
. git config --global user.email 'a@gmail.com'
. git init

#Linux command
mkdir [folder.name] #create new folder in currnet directory
cd [folder.name]
ls #show file and folder list...

#Common Used Instruction
git status
git log --oneline

#Track File and Folder
create a new README.md file,ctrl + S
git add [full file name]
git add * .file_sub_name
git add .
git commit -m 'message'

#Regular Process
. git add .
. git commit -m 'message'
. git push


#other instruction of modify file
. git reset --soft HEAD~ #回到上一動
. git reset --hard [version.number]
. git diff [version.number] -- [filename]
. git checkout [version.number] -- [filename]

#github
- create a new repository
- git remote add origin something_from_github.git
- git branch -M main
- git push -u origin main

#github and git
- git branch -M main
- git push -u origin main
- check status of the new github repository

# in git: checkout
- git checkout -b Branch_0583404
- do some modification to integration.py
- git add .
- git commit -m 'modifying integration.py'
- git push --set upstream origin Branch_0583404

#in github
- click compare & merge request
- create pull reauest
- merge request
- confirm merge