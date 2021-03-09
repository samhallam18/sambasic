import sambasic

while True:
    text = input('sambasic > ')
    result, error = sambasic.run(text)

    if error:
        print(error.as_string())
    else:
        print(result)