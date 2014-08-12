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
