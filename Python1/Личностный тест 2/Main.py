print('Welcome!')
print('Какой жанр музыки вы слушаете? Вы можете выбрать один из трех', 
      'вариантов (рок, поп-музыка, рэп)')
 
question1 = input()
 
if question1 == 'Rock':
    print('Люди, слушающие рок, чаще всего пассивные.')
elif question1 == 'pop':
    print('Те, кто слушает электронную и танцевальную музыку, как можно было', 
          'догадаться, общительны, упрямы, креативны и любят вечеринки не', 
          'меньше тех, кто слушает рэп ')
elif question1 == 'Rap':
    print('Вы отличаетесь высокой самооценкой, любите потусоваться и не', 
          'слишком заботитесь об окружающей среде')
    
if question1 == quest1 or question1 == quest2 or question1 == quest3: 
    
    print('Какое ваше любимое время года? Вы можете выбрать один из', 
          'четырех вариантов (Winter, Spring, Summer, Autumn)')
    
    question2 = input()
 
    if question2 == 'Winter':
        print('У людей, которые предпочитают холодные зимние месяцы,', 
              'в характере преобладает индивидуализм и лидерство.')
    elif question2 == 'Spring':
        print('В большинстве своем это очень мягкие люди, чей характер', 
              'отличается веселостью, легкостью и беззаботностью.')
    elif question2 == 'Summer':
        print('Безусловно, любители летнего сезона - это настоящие лидеры,', 
              'которых природа наградила соответствующими качествами.')
    elif question2 == 'Autumn':
        print('Это время года зачастую нравится людям строгим, уверенным в', 
              'себе и замкнутым, которые обладают слабой нервной системой,', 
              'склонностью к депрессиям, а также подавленному внутреннему', 
              'состоянию.')
    else:
        print('ERROR')
else:
    print('ERROR')