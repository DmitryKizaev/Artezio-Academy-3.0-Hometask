"""Homework 7 Task 2, additional"""

# а вдруг где-то пригодится


def for_all_methods(decorator):
    """Декорирует выбранным декоратором все методы класса"""
    def class_decorator(my_class):
        for name in my_class.__dict__:
            if callable(getattr(my_class, name)) and not name.startswith('_'):
                setattr(my_class, name, decorator(getattr(my_class, name)))
        return my_class
    return class_decorator
