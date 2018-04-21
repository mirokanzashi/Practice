# CH5 將本地repo推送到遠端repo

          
本地repo ========(push)==========>遠端repo

本地repo <===(pull/fetch/clone)===遠端repo

前置作業:在github上申請帳號並開一個新的repo，在此命名為Practice。
建立之後頁面會有一串類似下面的網址，就是repo的位址

    https://github.com/mirokanzashi/Practice.git #https 版本
    git@github.com:mirokanzashi/Practice.git #ssh版本

1-1 從github上複製repo到本地端

    git clone https://github.com/mirokanzashi/Practice.git

1-2 推送一個本地repo到遠端新建的repo

    git remote add origin https://github.com/mirokanzashi/Practice.git

2 推送本地repo到已建立連結的遠端repo

    git push

需輸入github的帳密

待續:

1 設定帳密免每次輸入的方法

2 git push -u origin master 參數意義
