In this post I'll go on explaining how your computer can grow nicely looking trees and plants. You can find the first part introducing the little turtle who does all the gardening in [PART 1](https://steemit.com/science/@smcaterpillar/l-systems-how-your-computer-grows-flowers-and-trees-free-turtle-inside).

![turtle](https://raw.githubusercontent.com/SmokinCaterpillar/blog/master/lsystems/pencil_turtle.png)

As a reminder, we established L-Systems as so called generative grammars. These are rewriting rules like: `F -> F+F-`. We can apply these rules iteratively as often as we please. The resulting string like `F+F-F+F-` can be read by a little obedient turtle with a pencil. The turtle moves either `F`orward or turns left (`+`) or right (`-`) accordingly. Thereby, it draws nice structures such as the Kochcurve:

![Kochcurve](https://raw.githubusercontent.com/SmokinCaterpillar/blog/master/lsystems/kochkurve.jpg)


### Our Turtle needs a Memory

Still, this does not really look like a plant, yet. Our rule system needs one further adjustment. Let us now introduce the `[` and `]` opening and closing bracket operators. Thereby we add a particular type of memory, also called *stack* in computer science, to our turtle. This means whenever the turtle reads a `[` it should remember its current position and orientation and keep it in mind. If it stumbles upon a `]` it should recall its former state from its memory and return to the remembered position and orientation **without** drawing stuff on its way back. In other words, a `]` teleports the turtle back to where it was when the last `[` appeared before. With this simple addition our turtle is able to draw realistic looking plants. See below for a whole set of different grammars and corresponding plants:

![Stack Plants](https://raw.githubusercontent.com/SmokinCaterpillar/blog/master/lsystems/stackplants.jpg)
*In this figure n is the number of iterations, sigma denotes the fixed turning angle, the character `X` is only needed for the grammar. It is ignored by the drawing turtle. Image taken from [1]*

Note that the `X` symbol is needed here for some plants. Since our turtle has no clue
what `X` means, it will simply ignore it. It is only used to generate the strings and is irrelevant for the drawing. Furthermore, I wrote a little Python script that you can use to draw these plants by yourself, the code is published in [my github repository](https://github.com/SmokinCaterpillar/blog/blob/master/lsystems/stackturtle.py).

## More advanced L-Systems

Of course, our simple turtle drawings are not the end of L-Systems. We could modfiy the drawing process and allow for three-dimensional rotations, add color, and allow additions of entire leaves:

![3d-plant](https://raw.githubusercontent.com/SmokinCaterpillar/blog/master/lsystems/3dplant.jpg)
*Image taken from [1]*

And this really does look like a realistic plant.

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

Or the development of trees that compete for sunlight and, therefore, grow in opposite directions:

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

[7] StackOverflow: [L-Systems to grow city models](https://gamedev.stackexchange.com/questions/18799/what-is-a-good-algorithm-for-fractal-based-procedural-city-layout)