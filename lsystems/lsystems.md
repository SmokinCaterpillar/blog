# L-Systems: Or how to draw beautiful plants algorithmically

I am a fan of self-organizing systems and complexity that can emerge from simple rules. Today I want to tell you about such a very simple system that can draw beautiful plant like structures.

In the late sixties the Hungarian biologist Aristid Lindenmayer developed so called L-Systems (yes, L stands for his last name), a formal grammar to simulate plant growth and development.

What is so special and fascinating about these L-Systems? Well, first of all, the underlying principles are relatively straightforward, yet they can yield very complex behaviour; I'll give you some examples below, bear with me for a second, though. By the way this phenomenon of simple rules leading to complex dynamics is often termed *Emeregence*. Secondly, even the mathematically notation of these system's is easy to understand. In contrast to other *simple systems* like coupled differential equations giving rise to complex phenomena.

Basically, L-Systems are generative grammars, that is a set of rewriting rules for characaters and strings. I'll skip the formal definition, but like to show an example instead. Consider the following to rules:

`A -> ABA`

`B -> A`

The arrow can be interpreted as *replace the stuff on the left hand side with the other stuff on the right*. In this example the character `A` will be replaced by the string `ABA` and `B` simply by `A`. It is important that both rules are applied simultaneously and not one after the other.

Let's say we start with character `A`. After the first iteration `A` will be replaced by
`ABA`. The second rule `B -> A` cannot be applied, because `B` does not exist, yet. Next, a second application of the rule set to `ABA` will yield `ABAAABA` (replacing both `A`s by `ABA` and the sinlge `B` by `A`). The simultaneous replacement makes sense from a biological perspective because plants grow as a whole and not leave by leave.

Well, this nice rule set allows us to genarete exponentially growing strings. Still, this does not really look like plant growth. A first step in this direction are the famous [turtle drawings], older generations may rember them from the educational programming language LOGO.

Imagine a turtle living on a paper plane. Moroever, someone very mean put a pencil right through the poor animal. However, the turtle doesn't die from the gruesome deed of being stabbed with a pencil. Instead, if the turtule wanders across the paper plane, it will draw a line along its path on the ground. It's also a very obient turtle, it will walk in any direction you command it to. In fact, the turtle knows three commands `F` for moving a fixed length forward, `+` for turning left with a fixed angle, and `-` for turning right into the opposite direction. See below for a turtle with a turing angle of 90 degrees. See how happily it draws the cube?

##### Insert turtle image

Now we can use our set of symbols `F`, `+`, and `-` in combination with an L-Systems grammer to draw beautiful structures. For examples let's take a look at this very simple rule:

`F -> F+F--F+F`

With this we can generate the following strings iteratively:
We begin with `F`, then we get `F+F--F+F` (1st iteration), next `F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F` (2nd iteration), and so on.

We may stop at some iteration of our choice and let our turtle draw the resulting string
using an angle of 60 degrees for `+` and `-`. The resulting fractal graphs are called [Koch curves](https://en.wikipedia.org/wiki/Koch_snowflake):

### Koch kurve image

We can draw some slightly more complex structures. If we tell the turtle to also move forward not only on the letter `F` but also `G` we may feed it the following grammer:

`F -> F-G+F+G-F`

`G -> GG`

Starting with the string `F-G-G` and using a turning angle of 120 degrees, the turtle can draw nice so called Sierpinski triangles (below n stands for the number of rule iterations):

### Sierpinsky triangle image

Still, this does not really look like a plant (yet). Our rule system needs one final further adjustment. Let us now introduce the `[` and `]` opening and closing bracket operators, adding a particular memory, also called *stack* in computer science, to our turtle. This means whenever the turtle reads a `[` it should remember it's current position and orientation and keep it in mind. If it stumbles upon a `]` it should recall it's former state from it's memory and return to the remembered position and orientation **without** drawing stuff on it's way back.
With this simple addition our turtle is able to draw realistic looking plants:

## plants image

Note that the `X` symbol is needed here for some plants. Since our turtle has no clue
what `X` means, it will simply ignore it. It is only used to generate the strings and is irrelavant for drawing. Furthermore, I wrote a little Python script you can use to draw these plants by yourself, the code is given below and in my github repository.

Of course, our simple turtle drawings are not the end of L-Systems. We could modfiy the drawing process and allow for three-dimensional rotations, add color, and allow additions of entire leaves:

### 3d image

And this really does look like a realistic plant.

We can further augment our L-System by introducing randomness. We can allow for alternative rules for the same initial character. The selection of rules is random following a certain probability:

`A -> AB : 20%`

`A -> BA : 80%`

Here `A` will be replaced by `AB` with 20% chance and by `BA` in the remaining 80% of cases. With these kind of stochastic rules we can introduce variations in our plants:

### stochastic image

Although these individual plants

Obwohl die Pflanzen unterschiedlich sind, könnte man sie gut der gleichen Art zuordnen.

Darüber hinaus lässt sich noch Kontextsensitivität definieren:

B<A>C -> ACA

Hier wird A nur durch ACA ersetzt falls sich zur Linken von A ein B und zur Rechten ein C befindet. Zuvor war es unmöglich zu simulieren, dass ein Baum in der Krone anders wächst als unten am Stamm, durch Kontextsensitivität lässt sich dies jedoch erreichen. Kontextsensitive Pflanzen sehen zum Beispiel so aus:
Name:  contextplants.jpg
Hits: 714
Größe:  77,6 KB
Wiederum stammt das Bild aus [1].

Dennoch wird Kontextsensitivität etwas komplizierter wenn man die Klammeroperatoren [ und ] hinzunimmt mit denen sich Verästelung simulieren lassen. Der Kontext eines Zeichens ist dann definiert als der obere und untere Teil in der Zeichnung und nicht notwendigerweise als der Kontext direkt im String.
Zum Beispiel würde die obere Regel auch in diesem Fall greifen B[ACA]AC, A befindet sich zwischen B und C und der Nebenast [ACA] wird ignoriert. In der resultierenden Pflanzenzeichnung lägen B und A nämlich neben bzw. untereinander.
Kontextsensitivität kann auch genutzt werden um Informationsfluss in Pflanzen zu simulieren, beispielsweise Chemikalien die durch den Stängel transportiert werden oder ähnliches.

Die letzte Erweiterung parametrisiert L-Systeme und die Simulation kann durch logische Ausdrücke und mathematische Operatoren und Funktionen ergänzt werden:

A(t): t > 3 -> B(4t) C(t^2+sin(t),ln(t))

A wird nur durch BC ersetzt wenn der Parameter t größer als 3 ist, darüber hinaus wird t weiter an B und C übergeben. Sehr komplexe Modelle sind möglich wenn nun zusätzlich noch ein mathematisches Modell der Umgebung der Pflanze gegeben ist, das beispielsweise Parameter bestimmen kann, welche das einfallende Licht, Nährstoffe im Boden oder Hindernisse wie Felsen oder Steine beschreiben. Solche mit der Umgebung kommunizierenden L-Systeme werden auch Open L-Systems genannt. Die Schildkrötenbefehle lassen sich ebenso gut parametrisieren: F(t) oder +(t) könnten beispielsweise einen Schritt oder Drehung um den Faktor t bedeuten.

Zum Beispiel lässt sich damit eine Pflanze in einer Box simulieren, die Umgebung definiert die Grenzen der Box,
Name:  boxplant.jpg
Hits: 634
Größe:  85,7 KB
Bild entnommen aus [2].

oder auch Bäume die um Sonnenlicht konkurrieren und deshalb voneinander weg wachsen:
Name:  competingtrees.jpg
Hits: 590
Größe:  31,5 KB
Bild entnommen aus [3].

Wie gezeigt sind L-System ein sehr mächtiges Werkzeug um Pflanzen naturgetreu zu modellieren. L-Systeme werden auch vielfach in der Wissenschaft verwendet, beispielsweise um den Metabolismus von Bäumen zu untersuchen [4] oder die Entwicklung von Wurzelwerk in verschiedenen Bodenarten [5]. Aber nicht nur künstliche Pflanzen werden erstellt, auch andere wachsende biologische Strukturen wie das Wachstum von neuronalem Gewebe [6]. MWn werden L-System auch in 3D-Spielen häufig verwendet um Wälder und andere Landschaften zu kreieren, leider konnte ich dazu aber keine Quellen finden.

Wer interessiert ist, HIER gibt es sehr viele kostenlose Literatur zu dem Thema.

[1] P. Prusinkiewicz and A. Lindenmayer, The Algorithmic Beauty of Plants. Springer, 1990.

[2] P. Prusinkiewicz, M. James and R. Mech, Synthetic Topiary, Computer Graphics Proceedings, 1994.

[3] R. Mech and P. Prusinkiewicz, “Visual models of plants interacting with their environment,” in Proceedings of the 23rd annual conference on Computer graphics and interactive techniques, ser. SIGGRAPH ’96. New York, NY, USA: ACM, 1996, pp. 397–410.

[4] M. T. Allen, P. Prusinkiewicz, and T. M. DeJong, “Using l-systems for modeling source-sink interactions, architecture and physiology of growing trees: The l-peach model,” New Phytologist, vol. 166, no. 3, pp. pp. 869–880, 2005.

[5] D. Leitner, S. Klepsch, G. Bodner, and A. Schnepf, “A dynamic root system growth model based on l-systems,” Plant and Soil, vol. 332, pp. 177–192, 2010, 10.1007/s11104-010-0284-7.

[6] H. Jelinek, A. Karperien, D. Cornforth, R. M. C. Junior, J. de Jesus Gomes, R. Marcondes, C. Junior, J. Jesus, and G. Le, “Micromod - an l-systems approach to neuron modelling,” in National University, 2002, pp. 156–163.
ZitierenZitieren