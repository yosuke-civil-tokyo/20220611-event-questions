def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 50, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述

    # 配列長さ
    len_array = len(sorted_array)

    # 配列の先頭と末尾のインデックス
    idx_head = 0
    idx_tail = len_array - 1

    # 配列の中央値と比べて、どちら側にあるかの判定を繰り返す
    while True:
        # 配列長、中央のidxと値を更新
        len_array = idx_tail - idx_head + 1
        idx_mid = idx_head + (len_array // 2)
        value_mid = sorted_array[idx_mid]

        # 配列中央の値が探索対象と一致すれば、配列中央インデックスが正解値
        if value_mid == target_number:
            return idx_mid

        # 配列の長さが1で(配列先頭のidx=先頭末尾のidx)、探索対象と一致していなければ、終了。-1を返す。
        elif len_array == 1:
            break

        # 中央の値が探索対象と一致しなければ、配列を絞り込んで、繰り返し処理に戻る
        else:
            # 配列中央の値が探索対象より小さければ、それより大きい部分に絞り込み
            if value_mid < target_number:
                idx_head = idx_mid + 1

            # 配列中央の値が探索対象より大きければ、それより小さい部分に絞り込み
            elif value_mid > target_number:
                idx_tail = idx_mid - 1

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
