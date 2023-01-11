from unittest import TestCase

import click

from click_lazy import LazyGroup


class TestLazyCall(TestCase):
    def test_call(self):

        cl = click.Group()
        cl.add_command(LazyGroup(name='lg', import_name='cli.lg:cli', help='Group to import'))

        args = ['lg', 'thecmd', ]

        try:
            cl(args)
        except SystemExit as e:
            pass

        from cli import lg
        res = getattr(lg.run_thecmd, '_called')
        self.assertTrue(res)
