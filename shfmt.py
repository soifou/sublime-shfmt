import os
import sublime
import sublime_plugin
import subprocess
import tempfile

PLUGIN_NAME = 'shfmt'


def minification(enabled=False):
    global minify
    minify = enabled


def load_settings():
    return sublime.load_settings('%s.sublime-settings' % PLUGIN_NAME)


def log_to_console(msg):
    print("{0}: {1}".format(PLUGIN_NAME, msg))


def format_code(edit, view, region):
    file_changed = False
    code = view.substr(region)
    fd, tmp_file = tempfile.mkstemp()
    encoding = "utf8"
    with open(tmp_file, 'wb') as file:
        file.write(code.encode(encoding))
        file.close()
    try:
        content = pipe(tmp_file)
    finally:
        os.close(fd)
        os.remove(tmp_file)

    if content and content != code:
        file_changed = True
        view.replace(edit, region, content)

    if file_changed:
        sublime.set_timeout(
            lambda: sublime.status_message('{0}: File formatted.'.format(
                PLUGIN_NAME)), 0)
    else:
        sublime.set_timeout(
            lambda: sublime.status_message('{0}: File already formatted.'.
                                           format(PLUGIN_NAME)), 0)
    return


def pipe(tmp_file):
    cmd1 = subprocess.Popen(["cat", tmp_file], stdout=subprocess.PIPE)
    cmd2 = subprocess.Popen(
        shfmt_cmd(),
        stdin=cmd1.stdout,
        stdout=subprocess.PIPE,
        shell=(not minify),
        env=get_env())

    cmd1.stdout.close()
    output = cmd2.communicate()[0]
    return output.decode('utf-8')


def shfmt_cmd():
    config = load_settings().get('config')
    cmd = ['shfmt']

    if minify:
        cmd.append('-s')
        cmd.append('-mn')
    else:
        for element in config:
            if (element == 'indent'):
                cmd.append("-i {}".format(config[element]))
            if (element == 'switch_case_indent' and config[element]):
                cmd.append("-ci")
            if (element == 'binary_ops_line_start' and config[element]):
                cmd.append("-bn")
            if (element == 'redirect_ops_space' and config[element]):
                cmd.append("-sn")
            if (element == 'keep_column_align_paddings' and config[element]):
                cmd.append("-kp")

    return cmd


def get_env():
    env = {}
    env.update(os.environ)

    paths = load_settings().get('paths')
    env['PATH'] = paths[sublime.platform()] + os.pathsep + env['PATH']
    return env


class ShfmtListener(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        config = load_settings().get('config')
        if config.get('autoformat'):
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
