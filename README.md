# Viernes de Crafters
Este repositorio contiene las soluciones retos que ponemos cada viernes.

# Instrucciones
Para poder contribuir con los retos publicados por la comunidad [Code Crafters](https://www.facebook.com/groups/883425011685153) es necesario tener conocimientos básicos de git y github. A continuación se describen los pasos para poder compartir tu solución.

## Hacer fork de este proyecto
1. Da clic a este enlace: [https://github.com/code-crafters/crafters-fridays](https://github.com/code-crafters/crafters-fridays)
2. En la parte superior derecha da clic en el botón que dice Fork.
3. Da clic en continuar.
4. Una vez terminado el proceso tendrás un nuevo repositorio al cuál vas a poder acceder con una url similar a: https://github.com/[tu_nombre_de_usuarii]/crafters-fridays. 
  Por ejemplo, en mi caso el url de mi repositorio resultado de hacer fork es: [https://github.com/jesuslerma/crafters-fridays](https://github.com/jesuslerma/crafters-fridays)
5. Listo ya hiciste fork al proyecto.

## Solucionar reto.
Cada solución a cada reto debe estar disponible en algún sevidor en donde podamos ver cómo lo solucionaste. Si ya tienes cuenta en github y la solución del reto es sencilla (como en el caso del [Reto 1](https://gist.github.com/rodolfomg/6db0ef03e015ecc3dd7edfe34e9e4732)) entonces puedes usar [Gist](https://gist.github.com/). 

Si la solución es más compleja te recomendamos que crees un nuevo repositorio en github con la solución y lo compartas.

Una vez que tengas la solución debes de clonar tu repositorio de crafters-fridays (en mi caso es (https://github.com/jesuslerma/crafters-fridays y lo usaremos de ejemplo) a tu máquina local. Desde tu línea de comandos con git ejecuta las siguientes instrucciones:
```bash
git  clone git@github.com:jesuslerma/crafters-fridays.git
cd crafters-fridays/
```

Después de haber clonado el repositorio es hora de editar el archivo `README.md` con tu editor de preferencia.
```bash
subl README.md
```
En el archivo busca el Reto en el que vas a participar y agrega lo siguiente en una nueva línea * [nombre_completo](tu_url_a_github), Lenguaje en el que solucionaste el problema, [url a tu solución]().

Por ejemplo uno de nuestros participantes agregó su solución: `[Rodolfo Montes G.](https://github.com/rodolfomg), C, https://gist.github.com/rodolfomg/6db0ef03e015ecc3dd7edfe34e9e4732 .` la cual puedes encontrar dentro de las soluciones al Reto 1.

Ahora guardas los cambios al archivo README.md. Haces un commit y lo subes a tu repositorio.
```bash
git add .
git commit -m "Add Rodolfo Solution"
git push origin master
```
Listo ya tienes la solución. Ahor hay que enviarla.

## Pull Request
El Pull Request nos va a servir para agregar tu solución a este repositorio. Recuerda que los cambios al archivo `README.md` hechos por ti se encuentran en tu repositorio y no en el de [nosotros](https://github.com/code-crafters/crafters-fridays). Para que esos cambios se reflejen en nuestro repositorio es necesario aprobar tus cambios y hacer un merge que los incluya.
Para esto necesitas hacer un pull request. A continuación te mostramos los pasos para hacerlo.

1. Ve a nuestro repositorio: [https://github.com/code-crafters/crafters-fridays](https://github.com/code-crafters/crafters-fridays).
2. Da clic en el botón New pull request para ser redireccionado a [https://github.com/code-crafters/crafters-fridays/compare?expand=1](https://github.com/code-crafters/crafters-fridays/compare?expand=1).
3. Da clic en donde dice compare accross fork. Si pones atención te muestra cuatro select boxes.
    1. Cada select box, vistos de izquierda a derecha, contene un texto similar a este: base fork: code-craters/crafters-fridays, base:master, head fork: code-crafters/crafters-fridays, compare: master. 
    2. En el select vox que dice head fork: code-crafters/crafters-fridays debes de buscar tu repositorio: por ejemplo el mio sería jesuslerma/crafters-fridays y en el siguiente select box seleccionar el branch en donde tienes la solución, en mi caso es master.
    3. Al hacer esos cambios los botones tendrán el siguiente texto: istos de izquierda a derecha, contene un texto similar a este: base fork: code-craters/crafters-fridays, base:master, head fork: jesuslerma/crafters-fridays, compare: master. 
4. Cuando hagas el paso anterior momento vas a tener una previsualización de los cambios agregados.
5. Si los cambios están bien entonces da clic en el botón que dice: Create pull request.
6. Se te va a redireccionar a un url similar a este: https://github.com/code-crafters/crafters-fridays/pull/8 ojo el numero 8 es variable y en tu caso será diferente.

## Eso es todo crafters
Bueno así es como contribuyes. Ahora espera a que uno de los colaboradores de este proyecto te acepte el pull request. 

Toma en cuenta que por el momento esto puede llevarse algo de tiempo ya que estamos revisando manualmente cada solución enviada.

También puede que a tu solución se te pidan cambios así que mantente al pendiente de las notificaciones de github o de tu correo.

# Reto 1:
## Busca Dígitos.
[Aquí](https://mentealgoritmica.blogspot.com/2018/06/reto-001.html) encontrarás las instrucciones del ejercicio.
### Soluciones
* Autor, Lenguaje, Enlace a la solución.
* Ludim Salo, Python 3, [Solucion Reto 1](https://gist.github.com/Ludim/ab2d772b2fe56e5f7a7d4d2d38492578)
* [Oswaldo D. Gomez Huerta](https://github.com/oswaldo89), Javascript, https://gist.github.com/oswaldo89/e6f687c63f4d693030a1a1eef85dde70 .
* [Juan C. del Valle](https://github.com/imekinox), Python, https://gist.github.com/imekinox/48221a083faddd9aeb2b0600cb97c194.
* [Javier Garza Cantisani](https://github.com/javiergarzac), Javascript, https://gist.github.com/javiergarzac/a767f6b1c2887f1b9688c735b9f1d684 .
* [Rodolfo Montes G.](https://github.com/rodolfomg), C, https://gist.github.com/rodolfomg/6db0ef03e015ecc3dd7edfe34e9e4732 .
* [Miguel Puerto](https://github.com/mike890), (js html), https://jsfiddle.net/atki890/w4g6pva9/3/
* [Armando Martínez](https://github.com/jmartinezpena), C#, [Find Digits](https://github.com/jmartinezpena/CodeCraftersChallenges/tree/master/Challenge001)

# Reto 2:
## Anagramas.
[Aquí](https://mentealgoritmica.blogspot.com/2018/06/reto-002.html) encontrarás las instrucciones del ejercicio.
Ejemplos de Anagramas: http://www.ejemplos.co/50-ejemplos-de-anagramas
### Soluciones
* Autor, Lenguaje, Enlace a la solución.
* [Oswaldo D. Gomez Huerta](https://github.com/oswaldo89), javascript, https://gist.github.com/oswaldo89/1b8f09fbb9e5b9ba948ba0bf4370b4d2.
* [Armando Martínez](https://github.com/jmartinezpena), C#, [Anagrams](https://github.com/jmartinezpena/CodeCraftersChallenges/tree/master/Challenge002)

# Reto 3:
## Torneo de futbol
[Aquí](https://mentealgoritmica.blogspot.com/2018/06/reto-003.html) encontrars las instrucciones del ejercicio.
### Soluciones
* Autor, Lenguaje, Enlace a la solución.
