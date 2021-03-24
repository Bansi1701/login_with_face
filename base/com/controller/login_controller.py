import csv
import datetime
import time
from email import message

import cv2
import numpy as np
import os
import pandas as pd
from PIL import Image
from jsonschema._types import is_number

from flask import *

from base import *


@app.route('/')
def index():
    return render_template('index.html')
