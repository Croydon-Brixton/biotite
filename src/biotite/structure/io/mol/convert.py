# This source code is part of the Biotite package and is distributed
# under the 3-Clause BSD License. Please see 'LICENSE.rst' for further
# information.

__name__ = "biotite.structure.io.mol"
__author__ = "Patrick Kunzmann"
__all__ = ["get_structure", "set_structure"]

from ...bonds import BondType


def get_structure(mol_file):
    """
    Get an :class:`AtomArray` from the MOL file.

    Ths function is a thin wrapper around
    :meth:`MOLFile.get_structure()`.

    Parameters
    ----------
    mol_file : MOLFile
        The MOL file.

    Returns
    -------
    array : AtomArray
        This :class:`AtomArray` contains the optional ``charge``
        annotation and has an associated :class:`BondList`.
        All other annotation categories, except ``element`` are
        empty.
    """
    return mol_file.get_structure()


def set_structure(mol_file, atoms, default_bond_type=BondType.ANY,
                  version=None):
    """
    Set the :class:`AtomArray` for the MOL file.

    Ths function is a thin wrapper around
    :meth:`MOLFile.set_structure()`.

    Parameters
    ----------
    mol_file : MOLFile
        The MOL file.
    array : AtomArray
        The array to be saved into this file.
        Must have an associated :class:`BondList`.
    version : {"V2000", "V3000"}, optional
        The version of the CTAB format.
        ``"V2000"`` uses the *Atom* and *Bond* block, while ``"V3000"``
        uses the *Properties* block.
        By default, ``"V2000"`` is used unless the number of atoms or
        bonds exceed the fixed size columns in the table, in which case
        ``"V3000"`` is used.
    """
    mol_file.set_structure(atoms, default_bond_type, version)
