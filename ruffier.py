txt_index = "Ваш индекс Руфье: "
txt_workheart = "Работоспособность сердца: "
txt_nodata = '''
нет данных для такого возраста'''
txt_res = []
txt_res.append(''' низкая.
Срочно обратитесь к врачу!''')
txt_res.append(''' удовлетворительная.
Обратитесь к врачу!''')
txt_res.append(''' средняя.
Возможно стоит дополнительно обследоваться у врача!''')
txt_res.append(''' 
выше среднего''')
txt_res.append(''' 
высокая''')

def test_ruffier(p1, p2, p3):
    index = (4 * (p1 + p2 + p3) - 200) / 10
    return index

def neud_level(age):
    norm_age = (min(age, 15) // 2)
    result = 21 - norm_age * 1.5
    return result

def ruffier_result(r_index, level):
    if r_index >= level:
        return 0
    level = level - 4
    if r_index >= level: 
        return 1
    if r_index >= level: 
        return 2
    if r_index >= level: 
        return 3
    return 4

def test(p1,p2,p3,age):
    if age < 7:
        return (txt_index + "0", txt_nodata)
    else:
        ruf_index = test_ruffier(p1,p2,p3)
        result = txt_res[ruffier_result(ruf_index,neud_level(age))]
        res = txt_index + str(ruf_index) + "\n" + txt_workheart + result
        return res
            