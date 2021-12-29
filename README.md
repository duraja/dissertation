# Predictive Analysis of Key Performance Indicators for Applications deployed in Kubernetes using Machine Learning and Propose an efficient Cost management solution for the organization

Step1:
`aws eks --region us-east-1 describe-cluster --name kpi-k8s-master --query cluster.status`

Step2:
`aws eks --region us-east-1 update-kubeconfig --name kpi-k8s-master`

Step3:
`kubectl get svc`

Step4:
`kubectl get nodes`

