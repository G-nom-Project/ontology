<p align="center"><a href="https://laravel.com" target="_blank"><img src="https://github.com/G-nom-Project/g-nom/blob/main/public/images/gnom.png?raw=true" width="200" alt="Laravel Logo"></a></p>
<p align="center">
<a href="https://www.w3.org/RDF/"><img src="https://www.w3.org/Icons/SW/Buttons/sw-rdf-green-v.svg" alt="RDF Badge" height="20"></a>
<a href="https://www.w3.org/RDF/"><img src="https://www.w3.org/Icons/SW/Buttons/sw-sparql-green-v.svg" alt="SPARPQL Badge" height="20"></a>
<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>
</p>


# G-nom Ontology

G-nom is a software for the storage, visualization and linking of genome assemblies and associated analyses with SPARQL and AI integrations.
The G-nom Ontology describes the underlying schema of the knowledge graph linking data within a G-nom instance. This schema is constantly updated as the scope of data types supported by G-nom expands. 






## Documentation Website

[https://G-nom-Project.github.io/g-nom_ontology](https://G-nom-Project.github.io/g-nom_ontology)

## Repository Structure

* [docs/](docs/) - mkdocs-managed documentation
  * [elements/](docs/elements/) - generated schema documentation
* [examples/](examples/) - Examples of using the schema
* [project/](project/) - project files (these files are auto-generated, do not edit)
* [src/](src/) - source files (edit these)
  * [g_nom_ontology](src/g_nom_ontology)
    * [schema/](src/g_nom_ontology/schema) -- LinkML schema
      (edit this)
    * [datamodel/](src/g_nom_ontology/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests
  * [data/](tests/data) - Example data

## Developer Tools

There are several pre-defined command-recipes available.
They are written for the command runner [just](https://github.com/casey/just/).
To list all pre-defined commands, run `just` or `just --list`.

## Credits

This project uses the template [linkml-project-copier](https://github.com/linkml/linkml-project-copier).
