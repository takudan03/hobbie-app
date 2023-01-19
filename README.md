


To run app in minikube cluster

-ensure that your minikube cluster is active by running the following:
`minikube start`

-ensure that you deploy your application and config yaml files to the cluster. As all the yaml files are located in the k8s-config directory, you can run the following to install them all:
`kubectl apply -f k8s-config`
This will start the mongo db app, and the mongo-express app for debugging as well as the flask app. 

-As the flask app is accessible only within the container, you will need to set up port-forwding for the service so you can access it from your host machine. You can assign a port using the following command:
`kubectl port-forward svc/hobbie-app-service 5001:5000`
This allows you to access the flask app through the localhost:5001 port on your host machine. 

-If you want to access mongo-express for debugging and testing the db connection, you can expose the external service set up using the minikube command here:
`minikube service mongo-express-service`