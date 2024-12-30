# Shfmt (Shell formatter)

This is a Sublime Text 3/4 plugin to format your shell scripts using [shfmt](https://github.com/mvdan/sh).

## Features

- Format current file, selections and scopes
- Format current file on save
- Minify current file

## Requirements

Obviously shfmt, you can install it in many ways:

```sh
apt install shfmt
pacman -Sy shfmt
brew install shfmt
```

And so on, I'm sure if you are here you already have it.

## Installation

**Not available on Package Control.**

Git clone this repository directly in your packages folder.

> [!WARNING]
> The plugin name must be called `shfmt` not `sublime-shfmt`

```sh
cd ~/.config/sublime-text/Packages
git clone https://github.com/soifou/sublime-shfmt shfmt
```

## Configuration

- Look at default values here `Preferences > Package Settings > Shfmt > Settings - Default`.
- Edit your user configuration file via `Preferences > Package Settings > Shfmt > Settings - User`.
- Override needed values.

Default configuration:

```json
{
    "paths": {
        "linux": "",
        "osx": "",
        "windows": ""
    },
    "config": {
        // Turns on autoformatting on save
        "autoformat": false,
        // Autoformat: if scope contains any of these, it will be auto-formatted
        "autoformat_scopes": ["source.shell"],
        // Autoformat: if scope contains any of these, it will never be
        // auto-formatted
        "autoformat_blacklisted_scopes": ["source.shell.nu"],
        // Indentation: 0 for tabs (default), >0 for number of spaces
        "indent": 4,
        // Switch cases will be indented
        "switch_case_indent": true,
        // Binary operators like && and | may start a line
        "binary_ops_line_start": true,
        // Redirect operators will be followed by a space
        "redirect_ops_space": true,
        // Keep column alignment paddings
        "keep_column_align_paddings": false,
        // Function opening braces are placed on a separate line
        "func_opening_braces_separate_line": false
    }
}
```

If `shfmt` is available in your `$PATH` environment, you're already set!

Else add manually the folder where `shfmt` live.
For instance, if `shfmt` live in `~/.bin/shfmt`, add the following value:

```json
"paths": {
    "linux": "~/.bin",
    "osx": "",
    "windows": ""
},
```

## Usage

### Command Palette

<dl>
    <dt>Format entire file:</dt>
    <dd><code>Shfmt: Format file</code></dd>
    <dt>Format one or more selections:</dt>
    <dd><code>Shfmt: Format selection(s)</code></dd>
    <dt>Minify entire file:</dt>
    <dd><code>Shfmt: Minify file</code></dd>
</dl>

### Hotkeys

Entire file:

- Linux: <kbd>alt+f</kbd>
- OS X: <kbd>ctrl+f</kbd>
- Windows: <kbd>alt+f</kbd>

Selection(s):

- Linux: <kbd>alt+shift+f</kbd>
- OS X: <kbd>ctrl+shift+f</kbd>
- Windows: <kbd>alt+shift+f</kbd>

Or add a [custom key bindings](https://www.sublimetext.com/docs/settings.html) using the following commands:

- `shfmt`
- `shfmt_selection`
- `shfmt_minify`
