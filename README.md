# TextExtractor Package
 A plugin package for sublime 4.x that makes extracting text to a set of new files super simple.

## Copyright and License
Copyright © 2024 Peter Richards, RichWEB, LLC
GNU General Public License v3.0

# TextExtractor Version 1.0

## Description
TextExtractor is a Sublime Text plugin that enables quick and efficient text extraction from existing documents to new files
with automatic file numbering.

## How to Use: Using Control+m keys prompts for a base filename, and after you enter it, the plugin will automatically add the appropriate number to the end of the file and use a .txt extesnion.  All files will be places in the same path as the file that is being cut from.

To choose a new filename, use Control+Option+m and the plugin will reset the file number counter to 0001 and prompt for
a new base filename.

## Note: the super key may be different on the windows and linux versions. You'll have to try whats to the left of the space
bar on most keyboards, as I do not own a Linux or Windows system to test on.)

## Installation for Sublime Text 4.0

### Manual Installation Steps
1. Open Sublime Text
2. Go to `Preferences > Browse Packages...`
3. Create a new folder named `TextExtractor`
4. Place these files in the folder:
   - `TextExtractor.py`
5. Navigate to Packages/User
6. Place these files in this folder:
   - `Default (OSX).sublime-keymap`
   -  Main.sublime-menu`

### Keymap Configuration
This was originally created for a Mac version of Sublime. You can easily add
the keymap config to Windows and Linux versions by renaming the
Default (OSX).sublime-keymap file to the appropriate name for your OS.

For Windows:
- Rename to: `Default (Windows).sublime-keymap`

For Linux:
- Rename to: `Default (Linux).sublime-keymap`

### Restart Sublime Text
Restart the application to activate the plugin.

## Requirements
- Sublime Text 4.0+
- Python 3.3+
