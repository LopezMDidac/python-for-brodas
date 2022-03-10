# retocar while para que en impares la cuelta sea "corriendo" y en los pares "saltando"
# ejemplo de output:
# 1 --> corriendo
# 2 --> saltando
# 3 --> corriendo
# 4 --> saltando
# 5 --> corriendo


vueltas = 1
final = 5
is_running = True
# <> =

while vueltas != final:
    vueltas = vueltas +1
    if is_running:
        print (str(vueltas) + "--> corriendo")
    else:
        print(str(vueltas) + "--> saltando")
        is_running = not is_running



#\n - Newline.
#\t- Horizontal tab.
#\r- Carriage return.
#\b- Backspace.
#\f- Form feed.
#\'- Single Quote.
#\"- double quote.
#\\-Backslash.

    


    