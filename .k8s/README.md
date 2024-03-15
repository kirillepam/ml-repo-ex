# multipass
```bash
multipass launch minikube
multipass info minikube
multipass stop minikube
multipass set local.minikube.memory=7G
multipass set local.minikube.cpus=4
multipass mount . minikube:/home/ubuntu/toy-manual-deployment
multipass start minikube
multipass shell minikube
multipass stop minikub
```

# minikube
```bash
minikube stop
minikube profile list
minikube delete
minikube start --memory=3000mb
minikube profile list
minikube status
kubectl get deploy,svc,ingress -A
```

# local testing
```bash
azmlinfsrv --entry_script src/score.py
python src/test.py
```

# ingress controller
```bash
curl https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.9.1/deploy/static/provider/cloud/deploy.yaml > .k8s/ingress/ingress-controller.yaml

kubectl apply -k .k8s/ingress/
kubectl get deploy,svc,ingress -A
kubectl logs deployment.apps/ingress-nginx-controller -n ingress-nginx
kubectl get po -A
kubectl get svc -n ingress-nginx
minikube tunnel
minikube service list (???)
```

# docker image
```bash
docker build . -t toy-model --n network host
docker run --rm toy-model
docker run -it toy-model /bin/sh (inside container)
docker run --rm -p 5001:5001 toy-model
```

# deploy
```bash
minikube image load toy-model
kubectl delete -k .k8s/workload/
kubectl apply -k .k8s/workload/
kubectl logs deployment.apps/deploy-toy-model -n nsp-toy-model
kubectl get deploy,svc,ingress -A
sudo bash -c "echo 10.110.131.113 webserver.io >> /etc/hosts"
kubectl get deploy,svc,ingress -A
minikube tunnel
python3 src/test.py
```
