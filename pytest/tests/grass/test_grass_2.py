import nose2
import shutil
import os
import tempfile
import pytest

from fixtures import *

def test_1(app_grass,request):
    print('Hello world!', request.node.name)
    app,grass = app_grass
    print(app)
    print(grass)

def test_2(app_grass):
    app,grass = app_grass
    print(app)
    print(grass)

def test_3(app_grass):
    app,grass = app_grass
    print(app)
    print(grass)
