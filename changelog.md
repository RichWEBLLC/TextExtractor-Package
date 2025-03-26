# TextExtractor 1.0.0

## Initial Feature Release:
- Text extraction with filename prompt on initial call to plugin.
- Files append a number to the base filename entered, padded with 0's to 4 places (ie: basefile_0001.txt)
- Each successive call increments the number by one and creates a new tab with the text and a prompt to save the file.
- All files are saved in the same path as the original master file being cut from.
- Text for the new file is either from current selection or the active clipboard.
- Implemented menu and keyboard shortcuts
- Added error handling for file creation to avoid overriting existing files.
