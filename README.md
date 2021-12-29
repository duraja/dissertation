# Predictive Analysis of Key Performance Indicators for Applications deployed in Kubernetes using Machine Learning and Propose an efficient Cost management solution for the organization

Step1:
`aws eks --region us-east-1 describe-cluster --name kpi-k8s-master --query cluster.status`

Step2:
`aws eks --region us-east-1 update-kubeconfig --name kpi-k8s-master`

Step3:
`kubectl get svc`

Step4:
`kubectl get nodes`

Wavefront Installation:
`kubectl create namespace wavefront`
`kubectl get namespaces`

Helm based installation --> `helm install wavefront wavefront/wavefront --namespace wavefront \
    --set clusterName=kpi-k8s-master \
    --set wavefront.url=<wavefront_url> \
    --set wavefront.token=<token name> \
    --set collector.useReadOnlyPort=true`


