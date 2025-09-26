#README
following is the description of the code
make some revision
ctrl + S
try to use GUI interface
this sentence will be show at github

#Install
. Git
. DB Browser for SQLite

#Initialize Environment
- in terminal
. git --version
. git config --global user.name 'Aaron name'
. git config --global user.email 'email'
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