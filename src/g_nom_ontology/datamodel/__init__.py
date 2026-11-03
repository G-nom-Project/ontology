"""Data model package for g-nom_ontology."""

from pathlib import Path
from .g_nom_ontology import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "g_nom_ontology.yaml"
