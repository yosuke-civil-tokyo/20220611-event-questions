for num in range(1, 101):
    string = ''

    # ここから記述

    # 3の倍数の場合、'Fizz'を追加
    if num%3==0: string += 'Fizz'

    # 5の倍数の場合、'Buzz'を追加
    if num%5==0: string += 'Buzz'

    # どちらでもない場合，数字を出力
    if string=='': string += str(num)

    # ここまで記述

    print(string)