

# объявляем функцию высшего порядка
def benchmark(func):
    import time
    
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
    return wrapper

@benchmark
def fetch_webpage():
    import requests
    webpage = requests.get('https://google.com')
    print(webpage)
fetch_webpage()


# Используем аргументы и возвращаем значения
print("\n-----------------------------------------\n")

def benchmark2(func):
    import time

    def wrapper2(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
        return return_value

    return wrapper2

@benchmark2
def fetch_webpage2(url):
    import requests
    webpage = requests.get(url)
    return webpage.text

webpage = fetch_webpage2('https://google.com')
#print(webpage)

#  Декораторы с аргументами
print("\n-----------------------------------------\n")


def benchmark3(iters):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total += (end - start)
            print('[*] Среднее время выполнения: {} секунд.'.format(total/iters))
            return return_value

        return wrapper
    return actual_decorator

@benchmark3(iters=10)
def fetch_webpage3(url):
    import requests
    webpage = requests.get(url)
    return webpage.text
    
webpage3 = fetch_webpage3('https://google.com')
# print(webpage3)