# Shfmt (Shell formatter)

This is a Sublime Text 3 plugin to format your shell scripts using [shfmt](https://github.com/mvdan/sh).

## Features

-   Format current file/selection(s)
-   Format current file on save
-   Minify current file

## Requirements

Install shfmt (tested with v3.0.0-alpha1):

```sh
$ go get -u github.com/mvdan/sh/cmd/shfmt
```

By default it should be available at `$HOME/.go/bin/shfmt`.

## Installation

**Not available on Package Control at the moment.**

Open Command Palette: <kbd>Package Control: Add Repository</kbd>
Add `https://github.com/soifou/sublime-shfmt`
Reopen Command: <kbd>Package Control: Install Package</kbd>
Search for `sublime-shfmt`

Or git clone this repository directly in your sublime `Packages/` folder.

## Configuration

-   Look at default values here `Preferences > Package Settings > Shfmt > Settings - Default`.
-   Edit your user configuration file via `Preferences > Package Settings > Shfmt > Settings - User`.
-   Override needed values.

Done.

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

-   Linux: <kbd>alt+f</kbd>
-   OS X: <kbd>ctrl+f</kbd>
-   Windows: <kbd>alt+f</kbd>

Selection(s):

-   Linux: <kbd>alt+shift+f</kbd>
-   OS X: <kbd>ctrl+shift+f</kbd>
-   Windows: <kbd>alt+shift+f</kbd>

Or add a [custom key bindings](https://www.sublimetext.com/docs/3/settings.html) using the following commands:

-   `shfmt`
-   `shfmt_selection`
-   `shfmt_minify`
