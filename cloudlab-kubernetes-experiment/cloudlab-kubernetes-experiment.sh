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
https://github.com/angelhof/dapr-quickstarts.git
cd dapr-quickstarts/tutorials/hello-kubernetes

## Apply the redis installation 
kubectl apply -f ./deploy/redis.yaml

## See the dashboard by using a new ssh connection just to port forward
ssh -i ${private_key} -L 9999:127.0.0.1:9999 ${node_username}@${node_address}
## Very useful to investigate logs etc

## Cleanup by being in the deploy directory and then running the following command
cd deploy
kubectl delete -f .
