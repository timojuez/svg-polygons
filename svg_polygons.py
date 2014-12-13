#! /usr/bin/env python

class Canvas:

  width = 0
  height = 0
  canvas = ''
  count = 0

  def __init__(self, width=500, height=500):
    self.width = width
    self.height = height


  def draw(self, shape, border_colour='black', fill_colour=None, centroid=None):
    canvas = "\n  <g id='shape%s'>" % self.count
    points = []
    for vertex in shape:
      points.append(str(vertex[0]) + "," + str(vertex[1]))
    point_string = " ".join(points)
    canvas += "\n    <polygon points='" + point_string + "' style='fill:%s; stroke:%s; stroke-width:3; stroke-linejoin:miter;' />" % (fill_colour, border_colour)
    if centroid != None:
      canvas += "\n    <circle cx='%s' cy='%s' r='8' style='stroke:black; fill:black;' />" % (centroid[0], centroid[1])
    canvas += "\n  </g>\n"
    self.canvas += canvas
    self.count += 1

  def save(self, filename='drawing'):
    canvas = self.addHeader()
    canvas += self.addCanvas()
    canvas += self.addFooter()
    f = open(filename + '.svg', 'w')
    f.write(canvas)
    f.close()
    print "File saved as %s.svg" % filename

  def clear(self):
    self.canvas = ''
    self.count = 0

  def addHeader(self):
    return "<svg xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#' xmlns:svg='http://www.w3.org/2000/svg' xmlns='http://www.w3.org/2000/svg' version='1.1' width='" + str(self.width) + "' height='" + str(self.height) + "'>\n"

  def addCanvas(self):
    return self.canvas + "\n"

  def addFooter(self):
    return "</svg>"
