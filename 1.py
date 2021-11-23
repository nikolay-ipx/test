def hello_logic(fun):
    def iner(*n):
        fun(*n)
        n = input('Фраза - ')
        if n == 'NULL':
            hello_null()
        elif n == 'DEFAULT' or n == 'Да':
            recommend_main()
        elif n == 'Нет' or n == 'Занят':
            hangup_wrong_time()
        elif n == 'Еще раз':
            hello_repeat()
        else:
            recommend_main()
    return iner


def main_logic(fun):
    def iner(*n):
        fun(*n)
        a = str(list(range(1, 9)))
        b = str(list(range(9, 11)))
        answer = input('Ответ - ')
        if answer == 'NULL':
            recommend_null()
        elif answer == 'DEFAULT':
            recommend_default()
        elif a.count(answer) == 1:
            hangup_negative()
        elif b.count(answer) == 1:
            hangup_positive()
        elif answer == 'Нет':
            recommend_score_negative()
        elif answer == 'Возможно':
            recommend_score_neutral()
        elif answer == 'Да':
            recommend_score_positive()
        elif answer == 'Еще раз':
            recommend_repeat()
        elif answer == 'Не знаю':
            recommend_repeat_2()
        elif answer == 'Занят':
            hangup_wrong_time()
        elif answer == 'Вопрос':
            forward()
        else:
            recommend_default()
    return iner


def counter_1(fun):
    count = 0
    def inner(*args):
        nonlocal count
        count += 1
        if count == 2:
            hangup_null()
            exit()
        return fun(*args)
    return inner


@counter_1
@hello_logic
def hello():
    print('\tДобрый день! Вас беспокоит компания Х, мы проводим опрос удовлетворенности\n '
          '\tнашими услугами. Подскажите, Вам удобно сейчас говорить?')


@counter_1
@hello_logic
def hello_repeat():
    print('\tЭто компания Х. Подскажите, Вам удобно сейчас говорить?')


@counter_1
@hello_logic
def hello_null():
    print('\tИзвините, Вас не слышно. Вы могли бы повторить')


@counter_1
@main_logic
def recommend_main():
    print('\tСкажите, а готовы ли Вы рекомендовать нашу компанию своим друзьям? Оцените, пожалуйста, \n'
          '\tпо шкале от "0" до "10", где "0" - не буду рекомендовать, "10" - обязательно порекомендую')


@counter_1
@main_logic
def recommend_repeat():
    print('\tКак бы Вы оценили возможность порекомендовать нашу компанию своим знакомым по шкале от \n'
          '\t 0 до 10 где 0 - точно не порекомендую, 10 - обязательно порекомендую')


@counter_1
@main_logic
def recommend_repeat_2():
    print('\tНу если бы Вас попросили порекомендовать нашу компанию друзьям или знакомым, \n'
          '\tВы бы стали это делать? Если да то оценка 10, если точно нет - 0')


@counter_1
@main_logic
def recommend_score_negative():
    print('\tНу а от 0 до 10 как бы Вы оценили бы: 0, 5 или может 7?')


@counter_1
@main_logic
def recommend_score_neutral():
    print('\tНу а от 0 до 10 как бы Вы оценили?')


@counter_1
@main_logic
def recommend_score_positive():
    print('\tХорошо, а по 10-ти бальной шкале как бы Вы оценили 8, 9 или может быть 10?')


@counter_1
@main_logic
def recommend_null():
    print('\tИзвините Вас совсем не  слышно, повторите пожалуйста?')


@counter_1
@main_logic
def recommend_default():
    print('\tПовторите пожалуйста')


def hangup_positive():
    print('\tОтлично! Большое спасибо за уделенное время! Всего доброго!')
    print('Высокая оценка')


def hangup_negative():
    print('\tЯ Вас понял. В любом случае большое спасибо за уделенное время! Всего доброго.')
    print("Низкая оценка")


def hangup_wrong_time():
    print('\tИзвините пожалуйста за беспокойство. Всего доброго')
    print("Нет времени для разговора")


def hangup_null():
    print('\tВас все равно не слышно, будет лучше если я перезвоню. Всего Вам доброго')
    print("Проблема с распознованием")


def forward():
    print('\tЧтобы разобраться в Вашем вопросе, я переключу звонок на моих коллег.\n'
          '\tПожалуста оставатесь на линии.')
    print("Перевод на оператора")


hello()