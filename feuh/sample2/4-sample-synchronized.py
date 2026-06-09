from threading import Thread

from feuh.sample2.thread.print_phrases_task import PrintPhrasesTask

t1 = Thread(target=PrintPhrasesTask('Hola como estas? como siempre bien chido?', 'que tal como estas compañero'))
t1.start()

t2 = Thread(target=PrintPhrasesTask('Quien eres te importa si te presentas primero\noh quieres problemas con mi amigo', 'quien eres tu para hablarme de tu?'))
t2.start()

t3 = Thread(target=PrintPhrasesTask('Muchas', 'gracias amigo!\nHasta luego compañero me agrada tu actitud siempre fuerte\nSaludos'))
t3.start()

t4 = Thread(target=PrintPhrasesTask('que hay compañeros', 'Todo bien en su casa o por que tanto rollo'))
t4.start()
