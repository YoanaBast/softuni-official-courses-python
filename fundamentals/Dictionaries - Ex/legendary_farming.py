# "Shadowmourne" - requires 250 Shards
# "Valanyr" - requires 250 Fragments
# "Dragonwrath" - requires 250 Motes
quant_mat_dic = {'shards': 0, 'fragments': 0, 'motes': 0}
legendary_won = False


def nice_print(sorted_dict: dict):
    result = []
    for key, value in sorted_dict.items():
        result.append(f"{key}: {value}")
    return '\n'.join(result)


while True:
    if legendary_won == True:
        break

    command = input().split()  # 123 silver 6 shards 8 shards 5 motes
    for i in range(0, len(command), 2):
        material = command[i + 1].lower()
        value = int(command[i])

        if material not in quant_mat_dic:
            quant_mat_dic.update({material: value})

        else:
            quant_mat_dic[material] += value

        if 'shards' in quant_mat_dic and quant_mat_dic['shards'] >= 250:
            quant_mat_dic['shards'] -= 250
            print('Shadowmourne obtained!')
            legendary_won = True
            break
        elif 'fragments' in quant_mat_dic and quant_mat_dic['fragments'] >= 250:
            quant_mat_dic['fragments'] -= 250
            print('Valanyr obtained!')
            legendary_won = True
            break

        elif 'motes' in quant_mat_dic and quant_mat_dic['motes'] >= 250:
            quant_mat_dic['motes'] -= 250
            print('Dragonwrath obtained!')
            legendary_won = True
            break

print(nice_print(quant_mat_dic))