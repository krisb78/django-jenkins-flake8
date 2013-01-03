import os
import pep8
import sys

import flake8.run


from django_jenkins.tasks import (
    BaseTask,
    get_apps_locations
)

from StringIO import StringIO


class Task(BaseTask):

    def __init__(self, test_labels, options):
        super(Task, self).__init__(test_labels, options)
        self.test_all = options['test_all']
        if options.get('flake8_file_output', True):
            output_dir = options['output_dir']
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            self.output = open(
                os.path.join(
                    output_dir,
                    'flake8.report'
                ),
                'w'
            )
        else:
            self.output = sys.stdout

    def teardown_test_environment(self, **kwargs):
        locations = get_apps_locations(
            self.test_labels,
            self.test_all
        )

        paths = flake8.run._get_python_files(locations)
        flake8.run.pep8style = pep8.StyleGuide(
            parse_argv=False,
            config_file=False
        )
        old_stdout, flake8_output = sys.stdout, StringIO()
        sys.stdout = flake8_output
        warnings = 0
        for path in paths:
            # We could pass ignore paths and max complexity there,
            # but I need to figure out first how to do it
            warnings += flake8.run.check_file(path)

        sys.stdout = old_stdout

        flake8_output.seek(0)

        while True:
            line = flake8_output.readline()
            if not line:
                break
            # message = re.sub(r': ', r': [E] PYFLAKES:', line)
            self.output.write(line)

        self.output.close()
