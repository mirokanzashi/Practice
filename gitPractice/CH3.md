# CH3 還原檔案操作

1 撤下舞台(unstaged)

    git reset HEAD #撤下所有stage中的檔案
    git reset HEAD 檔案名稱  #撤下單一檔案

2 從本地repo還原檔案

    git checkout 檔案名稱

3 還原所有的stage和工作目錄至最後一次的commit

    git reset --hard

相當暴力的指令，需小心使用

5 刪除最近一次 commit 

    git reset --hard "HEAD^" 
 
6 上面語法如果刪除錯了可以再用此語法還原

    git reset --hard ORIG_HEAD 
 
7 刪除最近一次 commit，但保留異動內容

    git reset --soft "HEAD^" 

### 範例練習

1 新增檔案example2.txt

2 使用git status查看狀態，example2.txt為unstage狀態

3 使用git add

4 使用git status查看，example2.txt為stage狀態

5 使用git reset HEAD

6 使用git status查看狀態，example2.txt為unstage狀態

7 查看現在example2.txt內容後，將example2.txt commit

8 修改example2.txt內容

9 使用git checkout

10 查看現在example2.txt內容，應該是和commit時相同

11 使用git status查看，確保現在是沒有東西在stage上或unstage的狀態

12 修改example2.txt

13 使用git status，會看見example2.txt是unstage

14 使用git add，加入stage

16 使用git status查看，example2.txt應為stage的狀態

15 使用git reset --hard

16 使用git status查看，應該是無檔案，和最後一次commit相同

17 5~9自行修改example2.txt練習