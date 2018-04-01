# CH2 新增檔案操作

檔案有3種狀態:還在本地資料夾中的local、放到舞台上的stage，放入本地repo。
stage是舞台的意思。將檔案放到stage是代表該檔案已經準備好，隨時可以送往repo了

1 將檔案加入stage 

    git add .

add後面的.代表是所有檔案，也可以替換成單一的檔名

2 檢查狀態

    git status

3 提交更新到本地repo

    git commit -m "message"

4 查詢記錄

    git log



### 練習範例

1 建立一個文件example.txt，並隨意輸入一個內容
2 使用git add將文件放上stage
3 使用git stage查看狀態
4 使用git commit送出report
5 再使用git status查看狀態
6 使用git log查看記錄
7 修改example.txt後存檔
8 使用git status查看狀態
9 使用git commit指令後查看訊息
10 使用git add指令後查看訊息
11 使用git commit指令後查看訊息
12 使用git log查看記錄
