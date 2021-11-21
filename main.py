
from flask import Flask

from wsgiref import simple_server

from flask import Flask, session, request, Response, jsonify



import atexit
import uuid
import os
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "Flask app is running on docker Image with Circle Ci pipeline."

port = int(os.getenv("PORT", 5001))

if __name__ == "__main__":
    host = '0.0.0.0'
    #app.run()
    httpd = simple_server.make_server(host=host, port=port, app=app)
    #httpd = simple_server.make_server(host='127.0.0.1', port=5000, app=app)
    # print("Serving on %s %d" % (host, port))
    httpd.serve_forever()


# Summary of task - docker image will be created at circle ci machine by using instructions provided in Dockerfile and config.yml
# this docker image will deploy on docker hub repository
# Our app deployed in Heroku will use this docker image as run time env

# Steps
# 1. Commands to setup project
# conda create -n env_name python==3.7
# pip install -r requirements.txt
# 2. Git hub local repo initalization
# git init

# To move all files in staging area
# git add .

# To commit files present in staging area in local repo
# git commit -m "initial wafer_circleci commit"

# Renaming master branch as main
# git branch -M main

# Adding remote github repo as a origin for local repo
# git remote add origin https://github.com/atulgaikwad12/wafer_circleci-main.git

# Final push to remote repo ( all file commited in local repo different from remote repo)
# git push -u origin main

# 3. To check git repo status use
# git status

# 4. Create Heroku app and Get heroku API key
# Account setting of heroku revel api key ->ae8e078f-204c-4760-9bd2-22e000b8d855

# 5. Create CircleCi account login with github and select project
# select existing config.yml by giving branch name as -> main
# stop running workflow

# 6. Go to Project Settings of Circle ci -> Environment Variables -> add below variables
# DOCKERHUB_USER=atulgaikwad12
# DOCKER_HUB_PASSWORD_USER = AtulAnil12@
# HEROKU_API_KEY = ae8e078f-204c-4760-9bd2-22e000b8d855
# HEROKU_APP_NAME = wafercircleci-main
# HEROKU_EMAIL_ADDRESS = atulanilgaikwad12@gmail.com
# DOCKER_IMAGE_NAME=wafercircleci-atul12