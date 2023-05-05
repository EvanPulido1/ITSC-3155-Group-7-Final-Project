from app import contacts, answers, answers2, answers3, answers4, answers5, answers6, answers7, answers8, answers9, answers10

def test_contacts():
    name = contacts.name('Braxton Williams')
    email = contacts.email('bwilliams@gmail.com')
    qc = contacts.qc('forgot my password')

    assert contacts.name == 'Braxton Williams'
    assert contacts.email == 'bwilliams@gmail.com'
    assert contacts.qc == 'forgot my password'

def test_answers():
    answer = answers.answer('Good idea')

    assert answers.answer == 'Good idea'

def test_answers2():
    answer2 = answers2.answer2('Good idea 2')

    assert answer2.answer2 == 'Good idea 2'

def test_answers3():
    answer3 = answers3.answer3('Good idea 3')

    assert answer3.answer3 == 'Good idea 3'

def test_answers4():
    answer4 = answers4.answer4('Good idea 4')

    assert answer4.answer4 == 'Good idea 4'

def test_answers5():
    answer5 = answers5.answer5('Good idea 5')

    assert answer5.answer5 == 'Good idea 5'

def test_answers6():
    answer6 = answers6.answer6('Good idea 6')

    assert answer6.answer6 == 'Good idea 6'

def test_answers7():
    answer7 = answers7.answer7('Good idea 7')

    assert answer7.answer7 == 'Good idea 7'

def test_answers8():
    answer8 = answers8.answer8('Good idea 8')

    assert answer8.answer8 == 'Good idea 8'

def test_answers9():
    answer9 = answers9.answer9('Good idea 9')

    assert answer9.answer9 == 'Good idea 9'

def test_answers10():
    answer10 = answers10.answer10('Good idea 10')

    assert answer10.answer10 == 'Good idea 10'