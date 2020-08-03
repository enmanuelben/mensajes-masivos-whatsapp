# mensajes-masivos-whatsapp

![GitHub followers](https://img.shields.io/github/followers/enmanuelben?label=Follow&style=social)
[![Twitter](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Fenmanuelben%2Fpopup_box)](https://twitter.com/intent/tweet?text=Wow:&url=https://github.com/enmanuelben/mensajes-masivos-whatsapp/)
![Twitter Follow](https://img.shields.io/twitter/follow/enmanuelbn?label=Follow&style=social)

Un código de Python que utiliza la automatización web para enviar mensajes masivos de WhatsApp a las personas sin tener que guardar los números de teléfono que se proporcionan en el archivo CSV.
## Versiones disponibles
<ul>
<li><strong>1.0.0</strong> - Las variables message_text, no_of_message y mobile_no_list tienen su significado habitual y están definidas explícitamente en el código. 
<li><strong>1.1.0</strong> - El código se modifica para que el número de números teléfono se extraiga del archivo csv "test_numbers.csv".
  <br>
  Para extraer los números usa el código:
  <br>
  <code>
  with open('test_numbers.csv', 'r') as csvfile:
    moblie_no_list = [int(row[0])
      for row in csv.reader(csvfile, delimiter=';')]
  # obtener el número de teléfono del archivo csv
  </code>
  </li>
<li>
  <strong>1.2.0</strong> - El código se modifica para que el número de números móviles se extraiga del archivo csv "test_numbers.csv" y el mensaje se extraiga de un archivo de texto.
  El código puede tomar el mensaje en cualquier idioma, para demostración he nombrado el archivo "prueba_message.txt".
  <br> Para extraer el texto, use el código:
  <br>
  <code>
  with open('prueba_message.txt') as message_file:
    for text in message_file:
        message_text+=text
  </coode>
  </li>
</ul>
