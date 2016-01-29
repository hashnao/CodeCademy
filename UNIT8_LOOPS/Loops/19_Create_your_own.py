fruits_list = ['apple', 'banana', 'carrot', 'watermelon' ]
vege_list = ['tomato', 'carrot' ]

for index, fruit in enumerate(fruits_list):
    for vege in vege_list:
        if fruit == vege:
            print 'The list contains a vegetable:', fruit
            break
    print index + 1, fruit
else:
    print 'Fruit list is completed!'
