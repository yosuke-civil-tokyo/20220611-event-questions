import random
def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    # 配列内の値の入れ替えを繰り返す
    while True:
        # 入れ替える値のインデックス
        idx_searched_head = 0
        idx_searched_tail = len(array) - 1

        # 先頭から、基準値以上の値を探索
        while (array[idx_searched_head]<pivot):
            idx_searched_head += 1

        # 末尾から、基準値未満の値を探索
        while (array[idx_searched_tail]>=pivot):
            idx_searched_tail -= 1
            # 基準値が最小値の場合、先頭まで探索を進めて終える
            if idx_searched_tail==0:
                break

        # 値を入れ替えて、繰り返しに戻る
        if idx_searched_head < idx_searched_tail:
            value_searched_head = array[idx_searched_head]
            value_searched_tail = array[idx_searched_tail]
            array[idx_searched_head] = value_searched_tail
            array[idx_searched_tail] = value_searched_head

        # 探索がぶつかった場合は、基準値以上の配列と基準値未満の配列で分け、それぞれの中でsortする
        elif idx_searched_head > idx_searched_tail:
            array1 = array[:idx_searched_head]
            array2 = array[idx_searched_head:]

            return [sort(array1), sort(array2)]

        # 基準値が最小の場合、探索したインデックスは両者0となる
        # この場合、先頭のみを分離してsortを続ける
        elif idx_searched_head == idx_searched_tail:
            array1 = array[:idx_searched_head+1]
            array2 = array[idx_searched_head+1:]

            return [sort(array1), sort(array2)]

    # ここまで記述

if __name__ == '__main__':
    main()
