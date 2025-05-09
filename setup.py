from setuptools import setup

setup(
    name="mkdocs-glossary-generator",
    entry_points={
        'mkdocs.plugins': [
            'glossary-generator = mkdocs_glossary_generator.__init__:GlossaryGeneratorPlugin'
        ]
    }
)