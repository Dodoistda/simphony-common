HDF5 Storage
============

Cuds containers can be stored in HDF5 files using the
:class:`~.H5CUDS` class. The provided api is currently a reduced
version of the Modelling Engine api and supports adding and
manipulating CUDS containers. Please also note that returned
containers from the get methods are live proxy objects on top of the
HDF5 storage (in contrast to the common offline save and read
operations).


HDF5 Stored Layout
------------------

Data are stored in HDF5 files using a separate layout for each type of
CUDS container.  The stored layout of the containers is provided
below using a pseudo-uml description for the HDF5 based layout of the
data stored in the files.

.. warning::

   This is the provisional storage layout and is under continuous
   development. Backwards compatibility is not expected to be
   supported before version 1.0.0 of the simphony-common library.

.. rubric:: File

.. figure:: ./images/h5cuds.png

   **Figure 1:** Diagram of the top level layout of the HDF5 based files.

   Each type of CUDS container is stored under the related section as an
   independent group.

.. rubric:: Lattice

.. figure:: ./images/h5lattice.png

   **Figure 2:** Diagram of the Lattice based storage.

   The Lattice is stored using two table nodes, one for the container
   `data` attribute and one for the lattice nodes data
   information. The nodes data are stored using the
   ``numpy.ndenumerate`` function to convert from i,j,k lattice
   coordinates to a flat index.

.. rubric:: Particles

.. figure:: ./images/h5particles.png

   **Figure 3:** Diagram of the Particles based storage.

   The Particles container is stored using one table for the container
   `data` attribute and two groups to holding the particle and bond
   items separately. Each item group has two tables one for the item
   information (i.e. particle or bond) and one for the item
   `data`. Indexing into the item and data tables takes place by using
   the same uid hex for both.

.. rubric:: Mesh

.. figure:: ./images/h5mesh.png

   **Figure 4:** Diagram of the Mesh based storage.

   The Mesh container is stored using 6 tables, one for the container
   `data` attribute, one for all the item data information, one for
   the points and one for each type of elements (i.e. edge, face and
   cell). Indexing to the point or element tables is using the item
   uid while the item ``data`` information is accessed using a
   separate set of uids mapping to the entries in the ``data`` table.
