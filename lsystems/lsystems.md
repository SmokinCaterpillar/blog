# L-Systems: How Computers grow Flowers and Trees (Free Turtle inside)

I am a fan of self-organizing systems and complexity that can emerge from simple rules. Today I want to tell you about such a very simple system that can draw beautiful plant like structures. In the late sixties the Hungarian biologist Aristid Lindenmayer developed so called L-Systems (yes, L stands for his last name), a formal grammar to simulate plant growth and development.

What is so special and fascinating about these L-Systems? Well, first of all, the underlying principles are relatively straightforward, yet they can yield very complex behavior; I'll give you some examples below, bear with me for a second, though. Secondly, even the mathematically notation of these systems is easy to understand (I swear, do not panic because I said math :-D); in contrast to other *simple systems* like coupled differential equations (yes, you are allowed to panic if you see coupled differential equations).

## The Basics of L-Systems: Meet the happy Turtle!

Basically, L-Systems are generative grammars, that is a set of rewriting rules for characters and strings. I'll skip the formal definition, but like to show an example instead. Consider the following two rules:

`A -> ABA`

`B -> A`

The arrow can be interpreted as *replace the stuff on the left hand side with the other stuff on the right*. In this example the character `A` will be replaced by the string `ABA` and `B` simply by `A`. It is important that both rules are applied simultaneously and not one after the other. In addition, we can repeat the string replacements as often as we want.

Let's say we start with character `A`. After the first iteration `A` will be replaced by
`ABA`. The second rule `B -> A` cannot be applied, because `B` does not exist, yet. Next, a second application of the rule set to `ABA` will yield `ABAAABA` (replacing both `A`s by `ABA` and the single `B` by `A`). We could go on for a third, fourth or fifth time, as often as it pleases you.

Well, this nice rule set allows us to generate exponentially growing strings. Still, this does not really look like plant growth. A first step in this direction are the famous [turtle drawings](https://en.wikipedia.org/wiki/Logo_(programming_language)#Turtle_and_graphics). Older generations may remember them from the educational programming language LOGO.

Imagine a turtle living on a paper plane. Moreover, someone very mean put a pencil right through the poor animal. However, the turtle doesn't die from the gruesome deed of being stabbed with a pencil. Instead, if the turtle wanders across the paper plane, it will draw a line along its path on the ground. It's also a very obedient turtle, it will walk in any direction you command it to. In fact, the turtle knows three commands `F` for moving a fixed length forward, `+` for turning left with a fixed angle, and `-` for turning right into the opposite direction. See below for a turtle with a turning angle of 90 degrees. See how happily it draws the cube?

![turtle](https://raw.githubusercontent.com/SmokinCaterpillar/blog/master/lsystems/turtle.png)

Now we can use our set of symbols `F`, `+`, and `-` in combination with an L-Systems grammar to draw beautiful structures. For example, let's take a look at this very simple rule:

`F -> F+F--F+F`

With this we can generate the following strings iteratively:
We begin with `F`, then we get `F+F--F+F` (1st iteration), next `F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F` (2nd iteration), and so on.

We may stop at some iteration of our choice and let our turtle draw the resulting string
using an angle of 60 degrees for `+` (left) and `-` (right). Our turtle will read the string character by character and draw for us. For instance, let us take `F+F--F+F`, in this case the turtle will start to move forward, then turn left, forward, right twice, forward again, left and another last time forward. The resulting fractal graphs are called [Koch curves](https://en.wikipedia.org/wiki/Koch_snowflake):

![Kochcurve](https://raw.githubusercontent.com/SmokinCaterpillar/blog/master/lsystems/kochkurve.jpg)
*You see the initial start `F`on the top left, followed by the first application `F+F--F+F` on the top right, and so on.*

We can draw some slightly more complex structures. If we tell the turtle to also move forward not only for the letter `F` but also for `G`, we may feed it the following grammar:

`F -> F-G+F+G-F`

`G -> GG`

Starting with the string `F-G-G` and using a turning angle of 120 degrees, the turtle can draw so called Sierpinski triangles:

![Sierpinski](https://raw.githubusercontent.com/SmokinCaterpillar/blog/master/lsystems/triangle.png)

### Our Turtle needs a Memory

Still, this does not really look like a plant, yet. Our rule system needs one final further adjustment. Let us now introduce the `[` and `]` opening and closing bracket operators. Thereby we add a particular type of memory, also called *stack* in computer science, to our turtle. This means whenever the turtle reads a `[` it should remember its current position and orientation and keep it in mind. If it stumbles upon a `]` it should recall its former state from its memory and return to the remembered position and orientation **without** drawing stuff on its way back. In other words, a `]` teleports the turtle back to where it was when the `[` appeared before. With this simple addition our turtle is able to draw realistic looking plants. See below for a whole set of different grammars and corresponding plants:

![Stack Plants](https://raw.githubusercontent.com/SmokinCaterpillar/blog/master/lsystems/stackplants.jpg)
*In this figure n is the number of iterations and sigma denotes the fixed angle. Image taken from [1]*

Note that the `X` symbol is needed here for some plants. Since our turtle has no clue
what `X` means, it will simply ignore it. It is only used to generate the strings and is irrelevant for the drawing. Furthermore, I wrote a little Python script you can use to draw these plants by yourself, the code is published in [my github repository](https://github.com/SmokinCaterpillar/blog/blob/master/lsystems/stackturtle.py).

Of course, our simple turtle drawings are not the end of L-Systems. We could modfiy the drawing process and allow for three-dimensional rotations, add color, and allow additions of entire leaves:

![3d-plant](https://raw.githubusercontent.com/SmokinCaterpillar/blog/master/lsystems/3dplant.jpg)
*Image taken from [1]*

And this really does look like a realistic plant.

## More advanced L-Systems

We can further augment our L-System by introducing randomness. We can allow for alternative rules for the same initial character. The selection of rules is random following a certain probability:

`A -> AB : 20%`

`A -> BA : 80%`

Here `A` will be replaced by `AB` with 20% chance and by `BA` in the remaining 80% of cases. With these kind of stochastic rules we can introduce variations in our plants:

![stochastic](https://raw.githubusercontent.com/SmokinCaterpillar/blog/master/lsystems/stochastic_plant.jpg)
*Stochastic plants taken from [1]*

Although these individual plants are different, you might think they belong to the same species.

As a next augmentation to our system we can introduce context sensitivity:

`B<A>C -> ACA`

In this rule `A` will only be replaced by `ACA` if a `B` can be found to the left and a `C` to the right of `A`. Context sensitive plants look like this, for example:

![context](https://raw.githubusercontent.com/SmokinCaterpillar/blog/master/lsystems/contextplants.jpg)
*Context sensitive plants from [1]*

Context sensitive grammars can not only be used for drawing, but also simulate nutrient flow within plants or the diffusion of other chemicals.

Finally, we can complicate our system further by introducing parametrized L-Systems. We can add logical and mathematical operators, for instance:


`A(t): t > 3 -> B(4t) C(t^2+sin(t),ln(t))`

`A` will be replaced by `BC` if `t` is larger than 3. Moreover, `t` is passed onto `B` and `C` via some complex functions. With these kinds of mathemtical parametrizations, one can add a model of the plant's environment such as soil nutrients or light sources.

For instance, we could simulate plant growth within a restricted box:

![boxplant](https://raw.githubusercontent.com/SmokinCaterpillar/blog/master/lsystems/boxplant.jpg)
*Image taken from [2]*

or the development of trees that compete for sunlight and, therefore, grow in opposite directions:

![competing](https://raw.githubusercontent.com/SmokinCaterpillar/blog/master/lsystems/competingtrees.jpg)
*Image taken from [3]*

L-Systems are powerful tools to model realistic plants. They are heavily used in science, for example, to investigate tree metabolism [4] or root growth [5]. L-Systems are not restricted to plants, they can also be used for other natural phenomena such as the growth of nerve tissue [6] or to generate realistic scenarios in computer games [7].

Finally, as a reminder, if you want to play around with L-Systems yourself, I provided a little Python script to do so [on my Github profile](https://github.com/SmokinCaterpillar/blog/blob/master/lsystems/stackturtle.py).

``` python

import turtle as t

def init_turtle():
    ...
```


# References

[1] P. Prusinkiewicz and A. Lindenmayer, The Algorithmic Beauty of Plants. Springer, 1990.

[2] P. Prusinkiewicz, M. James and R. Mech, Synthetic Topiary, Computer Graphics Proceedings, 1994.

[3] R. Mech and P. Prusinkiewicz, “Visual models of plants interacting with their environment,” in Proceedings of the 23rd annual conference on Computer graphics and interactive techniques, ser. SIGGRAPH ’96. New York, NY, USA: ACM, 1996, pp. 397–410.

[4] M. T. Allen, P. Prusinkiewicz, and T. M. DeJong, “Using l-systems for modeling source-sink interactions, architecture and physiology of growing trees: The l-peach model,” New Phytologist, vol. 166, no. 3, pp. pp. 869–880, 2005.

[5] D. Leitner, S. Klepsch, G. Bodner, and A. Schnepf, “A dynamic root system growth model based on l-systems,” Plant and Soil, vol. 332, pp. 177–192, 2010, 10.1007/s11104-010-0284-7.

[6] H. Jelinek, A. Karperien, D. Cornforth, R. M. C. Junior, J. de Jesus Gomes, R. Marcondes, C. Junior, J. Jesus, and G. Le, “Micromod - an l-systems approach to neuron modelling,” in National University, 2002, pp. 156–163.
ZitierenZitieren

[7] StackOverflow: [L-Systems to grow city models](https://gamedev.stackexchange.com/questions/18799/what-is-a-good-algorithm-for-fractal-based-procedural-city-layout)
