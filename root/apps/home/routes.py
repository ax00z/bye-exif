# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from urllib import request
from werkzeug.utils import secure_filename
from flask import flash, Request
import exiftool
import os
from apps.home import blueprint
from flask import render_template
from flask_login import login_required
from jinja2 import TemplateNotFound


@blueprint.route('/index')
def index():

    return render_template('home/index.html', segment='index')


