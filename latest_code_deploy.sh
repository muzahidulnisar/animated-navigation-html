#!/bin/bash

REPO_URL=https://github.com/muzahidulnisar/animated-navigation-html
DEPLOY_DIR=/home/ubuntu/animated-navigation-html

cd $DEPLOY_DIR
sudo git pull $REPO_URL main
sudo systemctl restart nginx