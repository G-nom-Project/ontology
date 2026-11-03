"""g-nom_ontology.

Ontology used by G-nom's RDF triple store.
"""

try:
    from g_nom_ontology._version import __version__, __version_tuple__
except ImportError:  # pragma: no cover
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)
