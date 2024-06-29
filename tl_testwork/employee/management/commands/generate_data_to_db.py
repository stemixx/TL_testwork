from django.core.management.base import BaseCommand
from pytils.translit import slugify
import random
from faker import Faker
from employee.models import Department, Employee

fake = Faker('ru_RU')

# кастомная структура подразделений для проекта, так как в модуле faker генерируются только названия организации
depart_data = {
    1: [
        'Холдинг Олл Инкорпорэйтед',
        'Северный филиал Холдинг Олл Инкорпорэйтед',
        'Южный филиал Холдинг Олл Инкорпорэйтед',
        'Восточный филиал Холдинг Олл Инкорпорэйтед',
        'Западный филиал Холдинг Олл Инкорпорэйтед',
    ],
    2: [
        'Департамент разработки',
        'Департамент финансов',
        'Департамент маркетинга',
        'Департамент логистики',
        'Департамент технического обслуживания',
    ],
    3: [
        'Управление проектами',
        'Управление по связям с общественностью',
        'Управление разработками',
        'Управление хозяйством',
        'Управление по взаимодействию'
    ],
    4: [
        'Отдел кадров',
        'Отдел бухгалтерии',
        'Отдел администрирования',
        'Отдел информационных технологий',
        'Отдел маркетинга',
    ],
    5: [
        'Служба связи',
        'Техническая служба',
        'Служба продаж',
        'Служба взысканий',
        'Хозяйственная служба'
    ]
}


class Command(BaseCommand):
    help = 'Generate random hierarchy departments from "depart_data" and random 50.000 employees data'

    def create_department(self):
        """
        Создание в БД записях о департаментах со случайной вложенной структурой на основе depart_data
        :return Department.objects.create
        """
        for level_number in range(1, len(depart_data) + 1):
            for dep_name in depart_data[level_number]:
                parent_level = level_number - 1
                # создадим головные подразделения, у которых нет родителя, поэтому parent_id=None
                # это необходимо для моделей, наследующихся от MPTTModel
                if parent_level == 0:
                    Department.objects.create(
                        name=dep_name,
                        slug=slugify(dep_name),
                        parent_id=None
                    )

                else:
                    # для всех уровней начиная с 2 и далее
                    # возьмём случайное родительское имя по случайному индексу родительского подразделения
                    random_parent_index = random.randint(0, len(depart_data[parent_level]) - 1)
                    random_parent_dep_name = depart_data[parent_level][random_parent_index]
                    dep_parent_id = Department.objects.get(name=random_parent_dep_name).id
                    # создадим дочернее подразделение, указав его имя и id родителя
                    Department.objects.create(
                        name=dep_name,
                        slug=slugify(dep_name),
                        parent_id=dep_parent_id
                    )

    def create_employee(self):
        """
        Создание в БД записи о работнике со случайными ФИО, должностью, датой приёма, зарплатой
        и подразделением (не головным)
        :return Employee.objects.create
        """
        full_name = fake.name()
        Employee.objects.create(
            full_name=full_name,
            position=fake.job(),
            # дата приёма на работу. '-5y' - за последние 5 лет
            hire_date=fake.date_between(start_date='-5y', end_date='today'),
            salary=random.randint(50, 350) * 1000,
            department=Department.objects.filter(parent__isnull=False).order_by('?').first(),
            slug=slugify(full_name)
        )

    def handle(self, *args, **options):
        # создаём сначала подразделения
        self.create_department()
        # создаём сотрудников в подразделениях
        for i in range(50000):
            self.create_employee()
        self.stdout.write(self.style.SUCCESS('Data generation completed'))
