隨機導入

高 =  1000

secret_number  = 隨機。randint ( 1 ,嗨)
num_guesses  =  0

而 真：
    猜測 = 輸入（“你的猜測是什麼？”）
    猜測 =  int (猜測)

    num_guesses  =  num_guesses  +  1

    ＃ 太高
    如果 猜測 >  secret_number：
        打印（“太高”）

    ＃ 太低
    如果 猜測 <  secret_number：
        打印（“太低”）

    ＃ 正確的
    如果 猜測 ==  secret_number：
        打印（“你猜對了”）
        打印（“IT TOOK YOU”，num_guesses，“GUESSES”）
        休息
