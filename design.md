Tank Game
Design Specification

The design specification is a counterpart to the Functional Speciffication. Where a functional specification concerns itself with inputs and outputs from the program, or the experience of a user running the program, the design specification is concerned with decisions that the engineer and programmer must make during its creation.

The design specification should include information like:

What tools or frameworks will you use to build the project (e.g. http://runpython.com or ggame)?
What language will you use for coding (usually Python 3)?
For every element of the Functional Specification, what code will need to be written to support it?
What data will be stored or manipulated by the program? How will it be encoded and organized?
Describe the logic and/or code behind every interaction with the user, and behind everything displayed.
If your program uses an unusual or notable algorithm, what is the algorithm and how does it work?

We will use http://runpython.com to code and ggame as our graphical interface. We will code in Python 3. 
We will need a bullet class, along with two tank classes (because the two tanks are not identical), and an app class. We will need to write collision code in the bullet class, when the bullet collides with the ground or a tank. At this point, the bullet will explode, and any tanks it is hitting will explode. This explosion will be done with an explosion class. We will ask each of the two users to input an angle and magnitude to fire the bullet at. We will use trigonometry to calculate the direction, and multiply the bullet's velocity by the magnitude. 
