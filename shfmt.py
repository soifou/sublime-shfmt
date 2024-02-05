import os
import sublime
import sublime_plugin
import subprocess
import shutil

PLUGIN_NAME = "shfmt"


def minification(enabled=False):
    global minify
    minify = enabled


def load_settings():
    return sublime.load_settings("%s.sublime-settings" % PLUGIN_NAME)


def log_to_console(msg):
    print("{0}: {1}".format(PLUGIN_NAME, msg))


def format_code(edit, view, region):
    view_context = view.substr(region)

    cmd = shfmt_cmd()
    if cmd is None:
        sublime.set_timeout(
            lambda: sublime.error_message(
                "{0}: not found in PATH ".format(PLUGIN_NAME)
            ),
            0,
        )
        return

    process = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    output, error = process.communicate(input=view_context.encode())

    if error:
        log_to_console(error.decode())
        sublime.set_timeout(
            lambda: sublime.error_message(
                "{0}: Error occured while formatting, see console log ".format(
                    PLUGIN_NAME
                )
            ),
            0,
        )

    if output and output != view_context:
        view.replace(edit, region, output.decode())
        sublime.set_timeout(
            lambda: sublime.status_message("{0}: File formatted.".format(PLUGIN_NAME)),
            0,
        )


def shfmt_cmd():
    shfmt = shutil.which("shfmt", path=get_path())
    if shfmt is None:
        return

    cmd = [shfmt]

    if minify:
        cmd.append("-s")
        cmd.append("-mn")
    else:
        config = load_settings().get("config")
        for element in config:
            if element == "indent":
                cmd.append("-i")
                cmd.append("{}".format(config[element]))
            if element == "binary_ops_line_start" and config[element]:
                cmd.append("-bn")
            if element == "switch_case_indent" and config[element]:
                cmd.append("-ci")
            if element == "redirect_ops_space" and config[element]:
                cmd.append("-sr")
            if element == "keep_column_align_paddings" and config[element]:
                cmd.append("-kp")
            if element == "func_opening_braces_separate_line" and config[element]:
                cmd.append("-fn")

    return cmd


def get_path():
    env = {}
    env.update(os.environ)

    paths = load_settings().get("paths")
    return os.path.expanduser(paths[sublime.platform()]) + os.pathsep + env["PATH"]


class ShfmtListener(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        config = load_settings().get("config")
        scopes = view.scope_name(view.sel()[0].b)
        if config.get("autoformat") and scopes.startswith("source.shell"):
            view.run_command("shfmt")


class ShfmtSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            format_code(edit, self.view, region)


class ShfmtMinifyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        minification(True)
        region = sublime.Region(0, self.view.size())
        format_code(edit, self.view, region)


class ShfmtCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        minification(False)
        region = sublime.Region(0, self.view.size())
        format_code(edit, self.view, region)
