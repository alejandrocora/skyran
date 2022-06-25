from time import sleep

def retry_func(method, arg, num, delay):
    done = False
    results = []
    for i in range(0, num):
        if done == True:
            continue
        try:
            if arg == None:
                results = method()
            elif type(arg) == list:
                results = method(*arg)
            else:
                results = method(arg)
            done = True

        except Exception as E:
            sleep(delay)
    if done == False:
        raise Exception("Method couldn't be completed.")
    else:
        return results

# def retry_func(method, num, delay):
#     retry_func(method, None, num, delay)

def retry_while(method, arg, exc_method, exc_arg, num, delay):
    done = False
    results = []
    for i in range(0, num):
        if done == True:
            continue
        try:
            if arg == None:
                results = method()
            else:
                results = method(arg)
            done = True
        except Exception as E:
            print(E)
            exc_method(exc_arg)
            sleep(delay)
    if done == False:
        return done
    else:
        return results
