site=int(input('Введите http код: '))
if site<199 and site>103:
    print('Для 1xx группы')
if site>203 and site<299:
    print('Для 2хх группы')
if site>303 and site<399:
    print('Для 3хх группы')
if site>403 and site< 499:
    print('Для 4хх группы ')
if site>503 and site<599:
    print('Для 5хх группы')
match site:
    case 100:
        print('Continue')
    case 101:
        print('Switching Protocols')
    case 102:
        print('Processing')
    case 103:
        print('Early Hints')
    case 200:
        print('OK')
    case 201:
        print('Created')
    case 202:
        print('Accepted')
    case 203:
        print('Non-Authoritative Information')
    case 300:
        print('Multiple Choices')
    case 301:
        print('Moved Permanently')
    case 302:
        print('Found')
    case 303:
        print('See Other')
    case 400:
        print('Bad Request')
    case 401:
        print('Unauthorized')
    case 402:
        print('Payment Required')
    case 403:
        print('Forbidden')
    case 500:
        print('Internal Server Error')
    case 501:
        print('Not Implemented')
    case 502:
        print('Bad Gateway')
    case 503:
        print('Service Unavailable')
    case _:
        print('Не найдено')