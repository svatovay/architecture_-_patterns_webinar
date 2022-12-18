from jinja2 import Template


def render(template_name, **kwargs):
    """
    Минимальный пример работы с шаблонизатором
    :param template_name: имя шаблона
    :param kwargs: параметры для передачи в шаблон
    :return:
    """
    # Открытие шаблона по имени
    with open(template_name, encoding='utf-8') as f:
        # Чтение
        template = Template(f.read())
        # рендер шаблона с параметрами
        return template.render(**kwargs)
