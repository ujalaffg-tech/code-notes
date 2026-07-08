#.1 github(remote) se local system pe lane ke liye
# copy paste ## git clone repo link

#.2 local system se github pe upload karne ke liye
#| mkdir folder name ( folder name repo name same rakho)
#| cd folder name
#| touch file name
#  folder ko git me convert karne ke liye ## git init
#= git add .
#= git commit -m ".."
## git remote add origin repolink
## git push -u origin main
#| edit karne per
#| git add .
#| git commit -m ".."
#| git push

#.3 undoing changes 
#/case1 - (staged to unstage)
#= ye sirf stage se unstage karega
#= changes delete nahi karega
## git restore --staged file name
#= ye changes delete karega
#= unstage nahi karega
## git restore file name
#/case2 - (commit )
# file ko unstage kar dega
# (no change in code) - code same to same rahega pahle bhi ab bhi 
# sirf commit delete hoga
#= 1 commit piche le jane ke liye 
## git reset  HEAD~1
#= 2 commit piche ke liye
## git reset HEAD₹~2
#/case3
# jis commit pe jaoge uska code dikhega
# jo commit delete hoga uska code bhi delete hoga 
## git reset --hard HEAD
#/ second way - ( jab bahut sare commit ho tab )
## git log
## git reset hash
## git reset hard hash

#.4 real merge
#| coflict lane ke liye dono ke same line me naya change lao ,nahi to conflict ki jagah 
# update ho jayega ushi branch me jisme ho 
# step1 #: create a repo
# step2 #: create folder and file in local 
# step3 #: cd foldername 
# step4 #: git clone repo link 
# step5 #: git checkout -b branch name
# step6 #: git add ./git cummit -m ".."
# step7 #: git checkout main
# step8 #: git merge branch name
# step9 #: conflict resolved
# step10 #: git add ./git cummit -m ".."
# step 12 #: git push -u origin main
#| itna se sirf main branch hi repo me add hoga
# next #: git checkout branch name
# next #: git push -u origin main
#. way 2
#| github pe jao pull requeset se kar lo ho jayega lakin merge sirf github pe dikhega na ki local pe

# repo se latest changes local pe upload karne ke liye - #: git pull origin branch name