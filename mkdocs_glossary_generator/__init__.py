import subprocess
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options

class GlossaryGeneratorPlugin(BasePlugin):
    config_scheme = (
        ('script', config_options.Type(str, default='generate_glossary_json.py')),
    )

    def on_config(self, config):
        script = self.config['script']
        print(f"📚 Running glossary generation script: {script}")
        try:
            result = subprocess.run(['python3', script], check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Error running glossary script: {e}")
        return config