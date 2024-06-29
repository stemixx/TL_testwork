from django import template
from django.utils.safestring import mark_safe
from employee.models import Department

register = template.Library()


@register.simple_tag
def get_employees_tree(node: Department) -> str:
    """
    Функция - кастомный тег. Выполняет рекурсивный обход по дереву подразделений и возвращает информацию
    по сотрудникам внутри этих подразделений.
    :param node: <class 'employee.models.Department'> Объект подразделения
    :return: result: <clss 'str'> HTML-разметка с данными по сотрудникам и подразделениям,
    к которым относятся эти сотрудники
    """
    result = ''
    # для каждого дочернего подразделения из головных филиалов составим html-разметку
    for child_department in node.get_children():
        result += f'<li><span><i class="fa fa-minus-square"></i>{child_department.name}</span>'
        # если подразделения не является конечным узлом, рекурсивно составим разметку
        if not child_department.is_leaf_node():
            result += '<ul>'
            result += get_employees_tree(child_department)
            result += '</ul>'
        # составим разметку по сотруднику внутри подразделения, к которому он относится
        for employee in child_department.employees.all():
            result += f'<ul><li><span>' \
                      f'{employee.full_name}. ' \
                      f'{employee.position}. ' \
                      f'Дата назначения {employee.hire_date}. ' \
                      f'Зарплата {employee.salary}' \
                      f'</span></li></ul>'
        result += '</li>'
    # результируем строку и оборачиваем в функцию mark_safe для предотвращения экранирования Django тегов html
    return mark_safe(result)
