Для создания бд необходимо выполнить пустую миграцию
 python .\manage.py makemigrations --empty numedy_app

после в нее добавить скрипт и поставить на выполнение

from django.db import migrations


from ..scripts.initial_data import create_initial_data


class Migration(migrations.Migration):

    dependencies = [
        ('numedy_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data),
    ]

бд готова

надо создать команду создания тестовых данных


сикрет ки
Заходим в терминал:

python manage.py shell
Импортируем utils:

from django.core.management import utils
Генерируем:

utils.get_random_secret_key()

здравствуйте! еще вопрос по формулировке.
"Реализовать отображение отчета по остаткам на каждом складе и общем остатке по каждой единице техники."
Имеется ввиду отчет вида:
Склад 1: всего {сумма всех остатков на складе 1}
остатки по единицам техники: 
    [item1: {штук},
    item2:{штук}...item100:{штук}]
Склад 2: всего {сумма всех остатков на складе 2}
остатки по единицам техники: 
    [item1: {штук},
    item2:{штук}...item100:{штук}]
    
Вывести гистограмму частот для общих остатков по единицам техники."
