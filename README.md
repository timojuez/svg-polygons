svg-polygons
============

A Python class for drawing polygons and saving as an SVG file


Usage
-----

First import the module:

```python
import svg_polygons
```

Let's say you want to draw two triangles. These should be represented as a list of three tuples. Each tuple gives the x and y coordinates for a vertex of the triangle.

```python
triangle1 = [(100, 70), (325, 210), (60, 300)]
triangle2 = [(455, 346), (39, 231), (80, 312)]
```

Now create a Canvas object specifying its width and height (in this case the canvas is 500×500):

```python
my_drawing = svg_polygons.Canvas(500, 500)
```

Now you can draw your triangles to the canvas, optionally specifying a border colour, fill colour, and opacity level:

```python
my_drawing.polygon(triangle1, 'red', 'blue', 1.0)
my_drawing.polygon(triangle2, 'green', 'yellow', 0.75)
```

If you want to draw a circle, specify the position of the circle and its radius, followed by the border colour, fill colour and opacity level:

```python
my_drawing.circle((250, 250), 20, 'black', 'black', 0.5)
```

Finally, save your drawing to an SVG file. See example_drawing.svg (part of this repo) for the resulting image.

```python
my_drawing.save('example_drawing')
```

If you need to clear your canvas, use:

```python
my_drawing.clear()
```

If you don't want a border or fill colour, use None to leave it transparent:

```python
my_drawing.draw(triangle1, 'red', None)
```

You can also specify colours using a hex triplet:

```python
my_drawing.polygon(triangle1, 'black', '#2E578C', 0.8)
```


Notes
-----

Be aware that svg-polgons follows the convention of placing the origin (0, 0) in the top left corner of the canvas, not the bottom left.
