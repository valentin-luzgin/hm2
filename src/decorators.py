def log(filename):
    """логирует результат работы функции в файл src/mylog.txt"""

    def log_(func):
        def inner(*args, **kwargs):
            message = ""
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                print(result)
            except Exception as e:
                message = f"{func.__name__} {type(e).__name__}. Inputs: {args} {kwargs}"
            finally:
                if filename:
                    with open(filename, "at") as file:
                        file.write(message + "\n")
                else:
                    print(message)

        return inner

    return log_
