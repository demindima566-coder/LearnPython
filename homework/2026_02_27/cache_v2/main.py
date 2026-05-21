import os
import json


def cache(file_name, use_kwargs = False):
    def decor(func):
        alph = {}

#грузим старый кеш

        if os.path.exists(file_name):
            try:
                with open(file_name, "r", encoding = 'utf-8') as f:
                    alph = json.load(f)
            except Exception:
                alph = {}
#ключ
        def wrapper(*args, **kwargs):
            if use_kwargs:
                key = str(sorted(kwargs.items()))
            else:
                key = str(args)
            if key in alph:
                print("кеш")
                return alph[key]

            result =  func(*args, **kwargs)
            alph[key] = result

# запись в файл
            with open(file_name, "w", encoding = 'utf-8') as f:
                json.dump(alph, f, ensure_ascii = False, indent = 2)

            return result
        return wrapper
    return decor

@cache("cache3.json")
def a(a,b):
    print("робит")
    return a+b


print(a(1,2))
print(a(1,2))
print(a(1,2))

# "робит" выводится только в первый запуск из за строк 23-25, после
# первого вызовая всегда попадаю в кеш