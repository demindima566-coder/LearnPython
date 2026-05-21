def retry(count = 1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0

            while attempts < count:
                try:
                    attempts += 1
                    result = func(*args, **kwargs)
                    return result

                except ValueError:
                    continue
                except OSError:
                    print(f"{func.__name__} OsError exception")
                    return
            return None
        return wrapper
    return decorator