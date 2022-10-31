#!/bin/bash

##
## Cannot be run as is due to the relogin
##

git clone https://github.com/angelhof/util-microservice-scripts.git
cd util-microservice-scripts

./docker-install-amd64-ubuntu.sh

sudo su - ${USER}

./kubectl-install-ubuntu.sh
./minikube-install-amd64-ubuntu.sh
./dapr-install.sh
./helm-install.sh

## Make sure that you have run the relogin here

## Start a minikube cluster for dapr
minikube start --cpus=4 --memory=4096
# Enable dashboard
minikube addons enable dashboard
# Enable ingress
minikube addons enable ingress

## Initialize dapr
dapr init --kubernetes --wait

## Install redis for the state store in k8s
./redis-install-kubernetes.sh

## Clone the quickstart repo

kubectl apply -f redis-state.yaml

