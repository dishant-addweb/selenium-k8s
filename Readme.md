# Selenium Grid (Hub + Nodes) for Kubernetes

This repo consists of initial deployment templated for deploying selenium grid on Kubernetes Cluster

## Usage

To deploy the templates you need to have access to a Kubernetes Cluster. For single node cluster you may use Minikube

### Prerequisites

- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-on-linux)
- [virtualbox](https://www.virtualbox.org/)
- [minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/)

### Local Deployment (Minkube)

To deploy to minikube you need to configure ingress accordingly.

- **Start Minikube**

    ```bash
    minikube start --driver virtualbox
    ```

- **Generate Ingress URL**

    ```bash
    echo "hub.$(minikube ip).nip.io"
    ```

    **OR** Directly copy to clipboard with xclip

    ```bash
    echo "hub.$(minikube ip).nip.io" | xclip -sel copy
    ```

- **Copy the IP and Replace the ingress configuration  in `selenium-hub-svc.yaml` as shown:**

    ```diff
    spec:
        rules:
    -    - host: "hub.9f7e5668-5cd5-482a-b441-0ebc0adc47c6.nodes.k8s.fr-par.scw.cloud"
    +    - host: hub.192.168.99.107.nip.io
            http:
            paths:
            - pathType: Prefix
    ```

- **Configure Replica Count and Resource Limits in `selenium-node-chrome-deployment.yaml`**

    ```diff
    spec:
    -    replicas: 3
    +    replicas: 1
        selector:
            matchLabels:
            app: selenium-node-chrome
    ```

    ```diff
    resources:
          requests:
    -        memory: "2048M"
    +        memory: "256M"
            cpu: ".1"
          limits:
            memory: "3072M"
            cpu: "1"
    ```

- **Apply the templates**

  - Create Namespace

  ```bash
  kubectl apply -f selenium-namespace.yaml
  ```

  - Apply the Deployments
  
  ```bash
  kubectl apply -f .
  ```

  - That should create the deployments,you can check for the status.
  
  ```bash
  kubectl get all -n selenium
  ```
  
  - Open the ingress URL in browser you Generated in previous step i.e hub.192.168.99.107.nip.io to access Selenium hub.

## Kubernetes Diagram

![Diagram](selenium-k8s.png)