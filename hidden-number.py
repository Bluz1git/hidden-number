import random

def tro_choi_doan_so():
    so_bi_mat = random.randint(1, 20)
    so_luot_choi = 0
    gioi_han = 5

    print("--- CHÀO MỪNG ĐẾN VỚI GAME ĐOÁN SỐ ---")
    print(f"\nGiới hạn trò chơi chỉ nằm trong 1-20. Bạn có {gioi_han} lượt đoán nhé!")

    while so_luot_choi < gioi_han:
        try:
            du_doan = int(input(f"\nLượt {so_luot_choi + 1} - Nhập số bạn đoán: "))
        except ValueError:
            print("\nVui lòng nhập số nguyên nha!")
            continue

        so_luot_choi += 1

        if du_doan == so_bi_mat:
            print(f"\nChúc mừng! Bạn đoán đúng số {so_bi_mat} trong {so_luot_choi} lượt.")
            break
        elif du_doan > so_bi_mat:
            if du_doan - so_bi_mat <= 3:
                print("\nSắp đúng rồi đó. Gợi ý nhỏ nè, số bạn nhập lớn hơn số bí mật và nằm trong phạm vi 3 đơn vị.")
            else:    
                print("\nSố bạn nhập lớn quá, nhỏ lại chút!")
        else:
            if so_bi_mat - du_doan <= 3:
             print("\nSắp đúng rồi đó. Gợi ý nhỏ nè, số bạn nhập nhỏ hơn số bí mật và nằm trong phạm vi 3 đơn vị.")
            else:
             print("\nSố bạn nhập nhỏ quá, to lên xíu!")
    
    if du_doan != so_bi_mat:
        print(f"\nGame Over! Số bí mật là: {so_bi_mat}")
    input("\nNhấn phím bất kỳ để thoát game...")

tro_choi_doan_so()