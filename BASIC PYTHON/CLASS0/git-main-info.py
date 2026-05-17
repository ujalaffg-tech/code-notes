
#.1 untrack file 
# git file ko nahi janta hain 
#.2 unstaged file 
# file edit kiya lakin git add . nahi kiya
#.3 staged file
# commit ke liye ready 
#.4 modiefied file 
# red color - edit kiya lakin git add . ke liye ready
# green color - edit kiya lakin commit ke liye ready 

#.5 optional
# tum kaha ho #: pwd
# ak step bahar #: cd ..
# jis folder pe jana hain #: cd foldername , na ki file name
# folder ke ander - files aur folder batata hain #: ls
# hidden folder #: ls -a
# naya folder bana dega #: mkdir folder name
# folder uda dega #: rm -rf folder name
# naya file bana dega jis folder me hoge #: touch file name
# file ko uda dega #: rm file name
# file me kya hai dikhayega #: cat f#: git remote add origin repolink
#: git pull origin main
#: git checkout -b branch name
# git hub pe veja - #: git push -u origin main
#| -u use karne se bar bar branch ka name nahi dalna padega 
#| direct likho git push o khud samgh jayega
# status dekhne ke liye #: git status 
#: git remote remove origin repo link
#: git remote -v 
# screen clear #: clear
# file data rakhta hain, aur folder file ko rakhta hain

#.6 branch 
#: git branch
# rename #: git branch -M branchname
# create new branch #: git checkout -b new branch name
# change branch #: git checkout new branch name
#: git diff branch Name
# local se branch delete #: git branch -D branch name
# repo se branch delete #: git push origin --delete branch name
# repo pe branch dikhe #: git push -u origin branch name
#| jise delete karna hai us branch se alg raho
#| jis branch me change karoge bas vahi hoga
#.7 ubdate branch  
#= main branch me code 
print("hello")
#= naya branch banaya nik name se usme same code hoga 
print("hello")
#= ab edit karke code ko banaya 
print("ka hal ba ho")
#= fir main me jake git merge nik kar diya to main me code nik vala ubdate hoga
print("ka hal ba ho")
#.8 conflict branch 
#= main branch me code likha
print("hello")
#= naya branch banaya nik, name se usme same code hoga main vala
print("hello")
#= ab edit karke code ko banaya 
print("ka hal ba ho")
#= ab fir main me gya vaha tha
print("hello")
#= ab edit kar ke code ko banaya
print("kuch bhi")
#= fir merge karne pe conflict ayega
#= then conflict resolved kiya aur cummit kiya 
#: git push -u origin main se sirf min vala push hoga
#: git push -u origin nik  se nik vala 

#.9 undoing changes -(staged cahnges)
#= file me mujuhe likhna tha 
print("login working")
#= maine galti se kuch aur likh diya
print(" login not working")
#= maine ishe staged bhi kar diya | git add . file name 
#| lakin main commit nahi karna chahta, main unstaged pe jana chahta hoon
# solution #: git restore --staged file name

## git restore --staged file name
#step1 - create file-folder
#step2 - git add .
#step3 - git commit -m ".."
