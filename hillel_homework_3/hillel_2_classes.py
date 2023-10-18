first_class = int(input("Кількість учнів у першому класі: "))
desk_fc_two = first_class // 2
desk_fc_one = first_class % 2

second_class = int(input("Кількість учнів у другому класі: "))
desk_sc_two = second_class // 2
desk_sc_one = second_class % 2

third_class = int(input("Кількість учнів у третьому класі: "))
desk_tc_two = third_class // 2
desk_tc_one = third_class % 2

desk_all_two = desk_fc_two + desk_sc_two + desk_tc_two
desk_all_one = desk_fc_one + desk_sc_one + desk_tc_one
desk_all = desk_all_one + desk_all_two

print("Потрібно закупити парт:", desk_all)