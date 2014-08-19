import sublime
import sublime_plugin
import os

class QuickCreateProjectCommand(sublime_plugin.WindowCommand):
    def run(self):
        full_path = self.window.folders()[0]
        file_name = os.path.basename(full_path) + ".sublime-project"

        project_file = os.path.join(full_path, file_name)

        file_ref = open(project_file, "w")
        file_ref.write(("{\n"
                        "    \"folders\":\n"
                        "    [\n"
                        "        {\n"
                        "            \"follow_symlinks\": true,\n"
                        "            \"path\": \".\"\n"
                        "        }\n"
                        "    ]\n"
                        "}\n"));
        file_ref.close()
