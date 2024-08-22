# MockServer - Demo in Kubernetes Cluster

Welcome to the **MockServer Demo**! This project demonstrates how to use Microcks and Kubernetes to mock external services and run feature tests against a microservice in a local Kubernetes cluster. The goal is to simulate a simple payment processing workflow.

## 📁 Project Structure
    .
    ├── app.py                          # Flask application for Order Service
    ├── Dockerfile                      # Dockerfile to build the Order Service image
    ├── mockserver.yaml                 # Kubernetes deployment for Microcks 
    ├── order-service.yaml              # Kubernetes deployment for Order Service
    ├── order-service-ft.yaml           # Feature test pod for Order Service
    ├── payment-gateway-openapi.yaml    # OpenAPI spec for the Payment Service
    └── upload-spec-job.yaml            # Kubernetes Job to upload the OpenAPI spec to Microcks
    
## 🚀 Getting Started

### Prerequisites

-   **Kubernetes Cluster:** Make sure you have a running Kubernetes cluster (e.g., `ccs-k8s`).
-   **kubectl:** Ensure `kubectl` is configured to interact with your cluster.
-   **Docker:** For building and pushing container images.

### 1. Clone the Repository

Start by cloning this repository to your local machine:
```bash
git clone https://github.com/Santhanabalan/mockserver.git
cd mockserver
```

### 2. Build and Push Docker Images

Build the Docker image for the Order Service:
> Update the repo inside order-service.yaml as well since it uses my repo
```bash
docker build -t your-docker-repo/order-service:latest .
docker push your-docker-repo/order-service:latest
```

### 3. Deploy Microcks (MockServer)

Deploy Microcks in your Kubernetes cluster using the provided `mockserver.yaml`:
```bash
kubectl apply -f mockserver.yaml
```

### 4. Deploy the Order Service

Deploy the Order Service in your Kubernetes cluster:
```bash
kubectl apply -f order-service.yaml
```
### 5. Upload the OpenAPI Spec to Microcks

Upload the OpenAPI spec for the Payment Service using the provided Kubernetes job:
```bash
kubectl apply -f upload-spec-job.yaml
```
This job will automatically upload the OpenAPI spec to Microcks and set up the mock for the Payment Service.

### 6. Run Feature Test

Deploy the feature test pod to validate the Order Service using the mocked Payment Service:
```bash
kubectl apply -f order-service-ft.yaml
```
This pod will trigger the `/createOrder` endpoint on the Order Service, simulating a payment process.

### 7. Verify the Results

Check the logs of the feature test pod to see if the order was successfully created:
```bash
kubectl logs pod/order-service-ft
```

### 🎉 Congratulations!

You have successfully set up a demo to mock external services and run feature tests in a Kubernetes cluster. This setup can be adapted to more complex workflows and microservices.

## 📝 Notes

-   This demo assumes a local Kubernetes cluster (`like Minikube`).
-   The `payment-gateway-openapi.yaml` provides a simple OpenAPI spec that will always return a successful payment transaction.