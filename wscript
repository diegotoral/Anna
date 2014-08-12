# -*- coding: utf-8 -*-
# encoding: utf-8


# App configuration
APPNAME = 'anna'
VERSION = '0.0.1'

# Waf configuration
top = '.'
out = 'build'


def options(opt):
    """
    Add options and flags.
    """
    opt.load('compiler_c')


def configure(conf):
    """
    Check and configure project dependencies.
    """
    conf.load('compiler_c')


def build(bld):
    """
    Build the project into a binary.
    """
    pass


def test(ctx):
    """
    Build and run the tests.
    """
    import waflib.Context

    ctx.recurse('test', name='build')
    ctx.cmd_and_log(
        'build/test\n',
        shell=True,
        output=waflib.Context.STDOUT,
        quiet=waflib.Context.BOTH
    )
