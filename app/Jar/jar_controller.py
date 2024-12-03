from flask import render_template, current_app, url_for, send_file
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import io

def home():
    return render_template('jar.html')
