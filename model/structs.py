import operator
from collections import namedtuple
from pprint import pformat
import numpy as np
import uuid
import math
from matplotlib.path import Path
import matplotlib.patches as patches
from matplotlib.lines import Line2D

Point = None
Triangle = None


class Vec:
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b
        self.x = b.x - a.x
        self.y = b.y - a.y

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_line(self):
        return Line2D([self.a.x, self.b.x], [self.a.y, self.b.y])

    def intersect(self, other):
        start1 = self.a
        start2 = other.a
        end1 = self.b
        end2 = other.b
        dir1 = Point(self.x, self.y)
        dir2 = Point(other.x, other.y)
        a1 = -dir1.y
        b1 = +dir1.x
        d1 = -(a1 * start1.x + b1 * start1.y)
        a2 = -dir2.y
        b2 = +dir2.x
        d2 = -(a2 * start2.x + b2 * start2.y)

        seg1_line2_start = a2 * start1.x + b2 * start1.y + d2
        seg1_line2_end = a2 * end1.x + b2 * end1.y + d2
        seg2_line1_start = a1 * start2.x + b1 * start2.y + d1
        seg2_line1_end = a1 * end2.x + b1 * end2.y + d1

        if seg1_line2_start * seg1_line2_end >= 0 or seg2_line1_start * seg2_line1_end >= 0:
            return False
        else:
            return True

    @staticmethod
    def inside_triangle(vec1, vec2, p):
        diag = Vec(Point(0, 0), Point(vec1.x + vec2.x, vec1.y + vec2.y))
        x = p.x + diag.x / 4
        y = p.y + diag.y / 4
        return Point(x, y)


class Edge:
    def __init__(self, a: Point, b: Point, edged=False):
        self.id = uuid.uuid4().int
        self.a = a
        self.b = b
        self.edged = edged
        self.triangles = {}

    def get_another_triangle(self, t_id):
        return list(filter(lambda t: t.id != t_id, self.triangles.values()))[0]

    def add_triangle(self, triangle: Triangle):
        self.triangles[triangle.id] = triangle

    def delete_triangle(self, t_id: uuid.UUID):
        self.triangles.pop(t_id)

    def __hash__(self):
        return self.id


class Point:
    def __init__(self, x, y):
        self.id = uuid.uuid4().int
        self.x = x
        self.y = y

    def __repr__(self):
        return "({} , {})".format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def inside(self, t):
        triangle = Path([(p.x, p.y) for p in t.p])
        points = np.array([self.x, self.y]).reshape(1, 2)
        res = triangle.contains_points(points)
        return res[0]

    def __hash__(self):
        return self.id


class Triangle:
    def __init__(self, points=None):
        self.id = uuid.uuid4().int
        self.edges = []
        self.color = "#0000ff"
        self.p = points
        self.x = None
        self.y = None
        self.cent_prop = None

    def __repr__(self):
        return self.centroid().__repr__()

    def centroid(self):
        if self.x is None:
            res = Point(0, 0)
            for p in self.get_vertices():
                res += p
            self.x = res.x / 3
            self.y = res.y / 3
        return Point(self.x, self.y)

    def get_vertices(self):
        if self.p is None:
            p = set()
            for e in self.edges:
                p.add(e.a)
                p.add(e.b)
            self.p = list(p)
            self.centroid()
        return self.p

    def add_edge(self, edge: Edge):
        self.edges.append(edge)
        edge.add_triangle(self)

    def add_edges(self, *args):
        for e in args:
            self.edges.append(e)
            e.add_triangle(self)

    def get_patch(self):
        p = self.get_vertices()
        verts = [(p.x, p.y) for p in p] + [(p[0].x, p[0].y)]
        codes = [Path.MOVETO] + [Path.LINETO for i in range(len(p) - 1)] + [Path.CLOSEPOLY]
        return patches.PathPatch(Path(verts, codes), edgecolor=self.color,
                                 facecolor='none', lw=2, linewidth=0.01)

    def get_other_edges(self, id):
        return list(filter(lambda v: v.id != id, self.edges))

    def cent(self):
        if self.cent_prop is None:
            [p1, p2, p3] = self.get_vertices()
            ax, ay, bx, by, cx, cy = p1.x, p1.y, p2.x, p2.y, p3.x, p3.y
            dx = bx - ax
            dy = by - ay
            ex = cx - ax
            ey = cy - ay
            bl = dx * dx + dy * dy
            cl = ex * ex + ey * ey
            d = dx * ey - dy * ex
            x = ax + (ey * bl - dy * cl) * 0.5 / d
            y = ay + (dx * cl - ex * bl) * 0.5 / d

            self.cent_prop = Point(x, y)
        return self.cent_prop

    def point_inside(self):
        [p1, p2, p3] = self.get_vertices()
        vec1 = Vec(p1, p2)
        vec2 = Vec(p1, p3)

        return Vec.inside_triangle(vec1, vec2, p1)

    def delauney(self, point: Point):
        x0, y0 = point.x, point.y
        p = self.get_vertices()[0]
        cent = self.cent()
        r = Vec(cent, p).length()
        condition = (x0 - cent.x) ** 2 + (y0 - cent.y) ** 2 >= r ** 2
        return condition

    def __hash__(self):
        return self.id


class Node(namedtuple('Node', 'item axis left right')):
    def __repr__(self):
        return pformat(tuple(self))


def search(point, node, best_node, min_dist):
    if node is None:
        return

    d = Vec(point, node.item.centroid()).length()
    if d < min_dist[0]:
        best_node[0] = node
        min_dist[0] = d

    p_val = point.__getattribute__(node.axis)
    node_val = node.item.__getattribute__(node.axis)
    if p_val <= node_val:
        if p_val - min_dist[0] <= node_val:
            search(point, node.left, best_node, min_dist)
        if p_val + min_dist[0] > node_val:
            search(point, node.right, best_node, min_dist)
    else:
        if p_val + min_dist[0] > node_val:
            search(point, node.right, best_node, min_dist)
        if p_val - min_dist[0] <= node_val:
            search(point, node.left, best_node, min_dist)


def kdtree(triangles, depth=0):
    if not triangles:
        return None

    k = 2
    axis = 'x' if depth % k == 0 else 'y'
    triangles.sort(key=operator.attrgetter(axis))
    median = len(triangles) // 2

    return Node(
        item=triangles[median],
        axis=axis,
        left=kdtree(triangles[:median], depth + 1),
        right=kdtree(triangles[median + 1:], depth + 1)
    )