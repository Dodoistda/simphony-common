import os
import tempfile
import shutil
import unittest

from simphony.cuds.mesh import Point
from simphony.cuds.mesh import Edge
from simphony.cuds.mesh import Face
from simphony.cuds.mesh import Cell

from simphony.io.cuds_file import CudsFile


class TestFileMesh(unittest.TestCase):

    def setUp(self):

        self.temp_dir = tempfile.mkdtemp()

        self.filename = os.path.join(self.temp_dir, 'test_file.cuds')
        self.file = CudsFile.open(self.filename)
        self.mesh = self.file.add_mesh("test")

        self.pids = []
        self.points = [
            Point((0.0, 0.0, 0.0)),
            Point((1.0, 0.0, 0.0)),
            Point((0.0, 1.0, 0.0)),
            Point((0.0, 0.0, 1.0)),
            Point((1.0, 0.0, 1.0)),
            Point((0.0, 1.0, 1.0))
        ]

    def tearDown(self):
        if os.path.exists(self.filename):
            self.file.close()
        shutil.rmtree(self.temp_dir)

    def test_emtpy_edges(self):
        """ Checks that the list of edges is empty

        """

        self.assertFalse(self.mesh.has_edges())

    def test_emtpy_faces(self):
        """ Checks that the list of faces is empty

        """

        self.assertFalse(self.mesh.has_faces())

    def test_emtpy_cells(self):
        """ Checks that the list of cells is empty

        """

        self.assertFalse(self.mesh.has_cells())

    def test_add_point(self):
        """ Check that a point can be added correctly

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:1]]

        self.assertIsNotNone(self.mesh.get_point(puuids[0]))

    def test_add_edge(self):
        """ Check that an edge can be added correctly

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:2]]

        edge = Edge(puuids[0:2])

        euuids = [self.mesh.add_edge(edge)]

        self.assertIsNotNone(self.mesh.get_edge(euuids[0]))

    def test_add_face(self):
        """ Check that a face can be added correctly

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:3]]

        face = Face(puuids[0:3])

        fuuids = [self.mesh.add_face(face)]

        self.assertIsNotNone(self.mesh.get_face(fuuids[0]))

    def test_add_cell(self):
        """ Check that a cell can be added correctly

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:4]]

        cell = Cell(puuids[0:4])

        cuuids = [self.mesh.add_cell(cell)]

        self.assertIsNotNone(self.mesh.get_cell(cuuids[0]))

    def test_add_duplicated_point(self):
        """ Check that a point can be added correctly

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:1]]

        self.assertRaises(KeyError, self.mesh.add_point, self.points[0])

    def test_add_duplicated_edge(self):
        """ Check that an edge can be added correctly

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:2]]

        edges = [
            Edge(puuids[0:2])
        ]

        euuids = [self.mesh.add_edge(edge) for edge in edges]

        self.assertRaises(KeyError, self.mesh.add_edge, edges[0])

    def test_add_duplicated_face(self):
        """ Check that a face can be added correctly

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:3]]

        faces = [
            Face(puuids[0:3])
        ]

        fuuids = [self.mesh.add_face(face) for face in faces]

        self.assertRaises(KeyError, self.mesh.add_face, faces[0])

    def test_add_duplicated_cell(self):
        """ Check that a cell can be added correctly

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:4]]

        cells = [
            Cell(puuids[0:4])
        ]

        cuuids = [self.mesh.add_cell(cell) for cell in cells]

        self.assertRaises(KeyError, self.mesh.add_cell, cells[0])

    def test_non_emtpy_edges(self):
        """ Checks that the list of edges is not empty

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:2]]

        edge = Edge(puuids[0:2])

        self.mesh.add_edge(edge)

        self.assertTrue(self.mesh.has_edges())

    def test_non_emtpy_faces(self):
        """ Checks that the list of faces is not empty

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:3]]

        face = Face(puuids[0:3])

        self.mesh.add_face(face)

        self.assertTrue(self.mesh.has_faces())

    def test_non_emtpy_cells(self):
        """ Checks that the list of cells is not empty

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:4]]

        cell = Cell(puuids[0:4])

        self.mesh.add_cell(cell)

        self.assertTrue(self.mesh.has_cells())

    def test_get_point(self):
        """ Check that a point can be retrieved correctly

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:1]]

        point_ret = self.mesh.get_point(puuids[0])

        self.assertTrue(isinstance(point_ret, Point))
        self.assertEqual(puuids[0], point_ret.uuid)

    def test_get_edge(self):
        """ Check that an edge can be retrieved correctly

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:2]]

        edges = [
            Edge(puuids[:]),
        ]

        euuids = [self.mesh.add_edge(edge) for edge in edges]

        edge_ret = self.mesh.get_edge(euuids[0])

        self.assertTrue(isinstance(edge_ret, Edge))
        self.assertEqual(euuids[0], edge_ret.uuid)

    def test_get_face(self):
        """ Check that a face can be retrieved correctly

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:3]]

        faces = [
            Face(puuids[:])
        ]

        fuuids = [self.mesh.add_face(face) for face in faces]

        face_ret = self.mesh.get_face(fuuids[0])

        self.assertTrue(isinstance(face_ret, Face))
        self.assertEqual(fuuids[0], face_ret.uuid)

    def test_get_cell(self):
        """ Check that a cell can be retrieved correctly

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:4]]

        cells = [
            Cell(puuids[:])
            ]

        cuuids = [self.mesh.add_cell(cell) for cell in cells]

        cell_ret = self.mesh.get_cell(cuuids[0])

        self.assertTrue(isinstance(cell_ret, Cell))
        self.assertEqual(cuuids[0], cell_ret.uuid)

    def test_get_all_edges_iterator(self):
        """ Checks the edge iterator

        Checks that an interator over all
        the edges of the mesh is returned
        when the function iter_edges is called
        without arguments

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:3]]

        edges = [
            Edge(puuids[0:2]),
            Edge(puuids[1:3])
        ]

        euuids = [self.mesh.add_edge(edge) for edge in edges]

        iedges = self.mesh.iter_edges()

        iedges_id = [edge.uuid for edge in iedges]

        self.assertItemsEqual(iedges_id, euuids)

    def test_get_all_faces_iterator(self):
        """ Checks the face iterator

        Checks that an interator over all
        the faces of the mesh is returned
        when the function iter_faces is called
        without arguments

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:4]]

        faces = [
            Face(puuids[0:3]),
            Face(puuids[1:4])
        ]

        fuuids = [self.mesh.add_face(face) for face in faces]

        ifaces = self.mesh.iter_faces()

        ifaces_id = [face.uuid for face in ifaces]

        self.assertItemsEqual(fuuids, ifaces_id)

    def test_get_all_cells_iterator(self):
        """ Checks the cell iterators

        Checks that an interator over all
        the cells of the mesh is returned
        when the function iter_cells is called
        without arguments

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:5]]

        cells = [
            Cell(puuids[0:4]),
            Cell(puuids[1:5])
            ]

        cuuids = [self.mesh.add_cell(cell) for cell in cells]

        icells = self.mesh.iter_cells()

        icells_id = [cell.uuid for cell in icells]

        self.assertItemsEqual(icells_id, cuuids)

    def test_get_subset_edges_iterator(self):
        """ Checks the edge iterator

        Checks that an interator over a subset of
        the edges of the mesh is returned
        when the function iter_edges is called
        selecting a list of uuid's

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:4]]

        edges = [
            Edge(puuids[0:2]),
            Edge(puuids[2:3]),
            Edge(puuids[3:4])
            ]

        euuids = [self.mesh.add_edge(edge) for edge in edges]

        iedges = self.mesh.iter_edges([euuids[0], euuids[2]])

        source_id = [euuids[0], euuids[2]]
        iedges_id = [edge.uuid for edge in iedges]

        self.assertItemsEqual(source_id, iedges_id)

    def test_get_subset_faces_iterator(self):
        """ Checks the face iterator

        Checks that an interator over a subset of
        the faces of the mesh is returned
        when the function iter_faces is called
        selecting a list of uuid's

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:5]]

        faces = [
            Face(puuids[0:3]),
            Face(puuids[1:4]),
            Face(puuids[2:5])
            ]

        fuuids = [self.mesh.add_face(face) for face in faces]

        ifaces = self.mesh.iter_faces([fuuids[0], fuuids[2]])

        source_id = [fuuids[0], fuuids[2]]
        ifaces_id = [face.uuid for face in ifaces]

        self.assertItemsEqual(source_id, ifaces_id)

    def test_get_subset_cells_iterator(self):
        """ Checks the cell iterator

        Checks that an interator over a subset of
        the cells of the mesh is returned
        when the function iter_cells is called
        selecting a list of uuid's

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:6]]

        cells = [
            Cell(puuids[0:4]),
            Cell(puuids[1:5]),
            Cell(puuids[2:6])
            ]

        cuuids = [self.mesh.add_cell(cell) for cell in cells]

        icells = self.mesh.iter_cells([cuuids[0], cuuids[2]])

        source_id = [cuuids[0], cuuids[2]]
        icells_id = [cell.uuid for cell in icells]

        self.assertItemsEqual(source_id, icells_id)

    def test_update_point(self):
        """ Check that a point can be updated correctly

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:1]]

        point_ret = self.mesh.get_point(puuids[0])
        point_ret.coordinates = [-1.0, -1.0, -1.0]
        self.mesh.update_point(point_ret)

        point_upd = self.mesh.get_point(puuids[0])

        self.assertItemsEqual(point_upd.coordinates, point_ret.coordinates)

    def test_update_edge(self):
        """ Check that an edge can be updated correctly

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:3]]

        edges = [
            Edge(puuids[0:2])
        ]

        euuids = [self.mesh.add_edge(edge) for edge in edges]

        edge_ret = self.mesh.get_edge(euuids[0])
        edge_ret.points[1] = puuids[2]
        self.mesh.update_edge(edge_ret)

        edge_upd = self.mesh.get_edge(euuids[0])

        self.assertItemsEqual(edge_upd.points, edge_ret.points)

    def test_update_face(self):
        """ Check that a face can be updated correctly

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:4]]

        faces = [
            Face(puuids[0:3])
        ]

        fuuids = [self.mesh.add_face(face) for face in faces]

        face_ret = self.mesh.get_face(fuuids[0])
        face_ret.points[2] = puuids[3]
        self.mesh.update_face(face_ret)

        face_upd = self.mesh.get_face(fuuids[0])

        self.assertItemsEqual(face_upd.points, face_ret.points)

    def test_update_cell(self):
        """ Check that a cell can be updated correctly

        """

        puuids = [self.mesh.add_point(point) for point in self.points[:5]]

        cells = [
            Cell(puuids[0:4])
        ]

        cuuids = [self.mesh.add_cell(cell) for cell in cells]

        cell_ret = self.mesh.get_cell(cuuids[0])
        cell_ret.points[3] = puuids[4]
        self.mesh.update_cell(cell_ret)

        cell_upd = self.mesh.get_cell(cuuids[0])

        self.assertItemsEqual(cell_upd.points, cell_ret.points)

if __name__ == '__main__':
    unittest.main()
