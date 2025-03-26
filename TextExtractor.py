## TextExtractor 1.0 by Peter S. Richards
## for Sublime Text 4.x Package Control Plugin.

import sublime
import sublime_plugin
import os
import re

class TextExtractorCommand(sublime_plugin.WindowCommand):
    def __init__(self, window):  # Fixed double asterisks
        self.window = window
        self.base_filename = None
        self.file_counter = 0

    def run(self, **args):
        # Get active view
        view = self.window.active_view()
        if not view:
            return

        if (args["commandtype"] == "reset"):
            self.base_filename = None
            self.file_counter = 0
            sublime.message_dialog("Base File Cleared.")
        
        # Get selected text or clipboard
        region = view.sel()[0] if view.sel() else None
        text = view.substr(region) if region and not region.empty() else sublime.get_clipboard()

        if not text:
            sublime.message_dialog("No text selected or in clipboard!")
            return

        # Prompt for filename if not set
        if not self.base_filename:
            self.window.show_input_panel(
                "Enter Base Filename, no Extension",
                "basefilename",
                self.on_filename_entered,
                None,
                None
            )
        else:
            self.create_file(text)

    def on_filename_entered(self, filename):
        # Sanitize filename
        sanitized_base = re.sub(r'[^a-zA-Z0-9]', '', filename)
        
        if not sanitized_base:
            sublime.message_dialog("Invalid filename!")
            return

        self.base_filename = sanitized_base
        self.file_counter = 0 # ensures starting at 1, because we increment right before creating.
        
        # Get selected text or clipboard again
        view = self.window.active_view()
        region = view.sel()[0] if view.sel() else None
        text = view.substr(region) if region and not region.empty() else sublime.get_clipboard()
        
        self.create_file(text)

    def create_file(self, text):
        # Increment counter
        self.file_counter += 1
        
        # Generate filename
        filename = "{}_{:04d}.txt".format(self.base_filename, self.file_counter)
        
        # Get current file's directory
        vars = self.window.extract_variables()
        file_path = vars.get('file_path', sublime.packages_path())
        
        # Full file path
        full_path = os.path.join(file_path, filename)
        
        # Check if file exists
        if os.path.exists(full_path):
            sublime.message_dialog("File {} already exists! Try changing base filename.".format(filename))
            self.file_counter -= 1
            return

        # Create new view and insert text
        new_view = self.window.new_file()
        new_view.set_name(filename)
        new_view.run_command('append', {'characters': text})
        
        # Save the file
        new_view.run_command('save')

    def ResetFileName(self):
        # Reset the file counter and prompt for a new base filename
        self.base_filename = None
        self.file_counter = 0
        sublime.message_dialog("Base Filename Cleared. New file with start at 0001.")
