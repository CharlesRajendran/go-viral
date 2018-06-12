import Rules



def recommend(d, file_name):
    file_handler = open(file_name,"r").read()
    final_recommendations = {}

    key_list = list(d.keys())

    if 'rule1' in key_list:
        final_recommendations['rule1'] = Rules.rule1(d.get('rule1'))

    if 'rule2' in key_list:
        final_recommendations['rule2'] = Rules.rule2(d.get('rule2'), file_handler)

    if 'rule3' in key_list:
        final_recommendations['rule3'] = Rules.rule3(d.get('rule3'))

    if 'rule4' in key_list:
        final_recommendations['rule4'] = Rules.rule4(d.get('rule4'), file_handler)

    if 'rule5' in key_list:
        final_recommendations['rule5'] = Rules.rule5(d.get('rule5'), file_handler)

    if 'rule6' in key_list:
        final_recommendations['rule6'] = Rules.rule6(d.get('rule6'))

    if 'rule7' in key_list:
        final_recommendations['rule7'] = Rules.rule7(d.get('rule7'), file_handler)

    if 'rule8' in key_list:
        final_recommendations['rule8'] = Rules.rule8(d.get('rule8'))

    if 'rule9' in key_list:
        final_recommendations['rule9'] = Rules.rule9(d.get('rule9'), file_handler)

    if 'rule10' in key_list:
        final_recommendations['rule10'] = Rules.rule10(d.get('rule10'))

    if 'rule11' in key_list:
        final_recommendations['rule11'] = Rules.rule11(d.get('rule11'), file_handler)

    if 'rule12' in key_list:
        final_recommendations['rule12'] = Rules.rule12(d.get('rule12'))

    if 'rule13' in key_list:
        final_recommendations['rule13'] = Rules.rule13(d.get('rule13'), file_handler)

    if 'rule14' in key_list:
        final_recommendations['rule14'] = Rules.rule14(d.get('rule14'))

    if 'rule15' in key_list:
        final_recommendations['rule15'] = Rules.rule15(d.get('rule15'), file_handler)

    if 'rule16' in key_list:
        final_recommendations['rule16'] = Rules.rule16(d.get('rule16'))

    if 'rule17' in key_list:
        final_recommendations['rule17'] = Rules.rule17(d.get('rule17'), file_handler)

    if 'rule18' in key_list:
        final_recommendations['rule18'] = Rules.rule18(d.get('rule18'))

    if 'rule19' in key_list:
        final_recommendations['rule19'] = Rules.rule19(d.get('rule19'), file_handler)

    if 'rule20' in key_list:
        final_recommendations['rule20'] = Rules.rule20(d.get('rule20'))

    if 'rule21' in key_list:
        final_recommendations['rule21'] = Rules.rule21(d.get('rule21'), file_handler)

    if 'rule22' in key_list:
        final_recommendations['rule22'] = Rules.rule22(d.get('rule22'))

    if 'rule23' in key_list:
        final_recommendations['rule23'] = Rules.rule23(d.get('rule23'), file_handler)

    if 'rule24' in key_list:
        final_recommendations['rule24'] = Rules.rule24(d.get('rule24'))

    if 'rule25' in key_list:
        final_recommendations['rule25'] = Rules.rule25(d.get('rule25'), file_handler)

    if 'rule26' in key_list:
        final_recommendations['rule26'] = Rules.rule26(d.get('rule26'))

    if 'rule27' in key_list:
        final_recommendations['rule27'] = Rules.rule27(d.get('rule27'), file_handler)

    if 'rule28' in key_list:
        final_recommendations['rule28'] = Rules.rule28(d.get('rule28'))

    if 'rule29' in key_list:
        final_recommendations['rule29'] = Rules.rule29(d.get('rule29'), file_handler)

    if 'rule30' in key_list:
        final_recommendations['rule30'] = Rules.rule30(d.get('rule30'))

    if 'rule31' in key_list:
        final_recommendations['rule31'] = Rules.rule31(d.get('rule31'), file_handler)

    if 'rule32' in key_list:
        final_recommendations['rule32'] = Rules.rule32(d.get('rule32'))

    if 'rule33' in key_list:
        final_recommendations['rule33'] = Rules.rule33(d.get('rule33'), file_handler)

    if 'rule34' in key_list:
        final_recommendations['rule34'] = Rules.rule34(d.get('rule34'))

    if 'rule35' in key_list:
        final_recommendations['rule35'] = Rules.rule35(d.get('rule35'), file_handler)

    if 'rule36' in key_list:
        final_recommendations['rule36'] = Rules.rule36(d.get('rule36'))

    if 'rule37' in key_list:
        final_recommendations['rule37'] = Rules.rule37(d.get('rule37'), file_handler)

    if 'rule38' in key_list:
        final_recommendations['rule38'] = Rules.rule38(d.get('rule38'))

    if 'rule39' in key_list:
        final_recommendations['rule39'] = Rules.rule39(d.get('rule39'), file_handler)

    if 'rule40' in key_list:
        final_recommendations['rule40'] = Rules.rule40(d.get('rule40'))

    if 'rule41' in key_list:
        final_recommendations['rule41'] = Rules.rule41(d.get('rule41'), file_handler)
    

    
    
    return final_recommendations

if __name__ == "__main__":

    print(recommend({'rule34': {'trust': 0, 'fear': 0, 'ant': 1, 'anger': 0, 'sadness': 1, 'joy': 0, 'surprise': 0, 'disgust': 0}, 'rule37': {'negativity': 0, 'positivity': 0}, 'rule35': {'trust': 1, 'fear': 0, 'ant': 0, 'anger': 0, 'sadness': 0, 'joy': 0, 'surprise': 0, 'disgust': 0}, 'rule39': {'trust': 1, 'fear': 0, 'ant': 0, 'anger': 0, 'sadness': 0, 'joy': 0, 'surprise': 0, 'disgust': 0}}, "89.txt"))
    
