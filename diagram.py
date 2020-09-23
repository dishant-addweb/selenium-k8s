from diagrams import Diagram,Cluster,Edge
from diagrams.k8s.compute import Pod,Deploy,RS
from diagrams.k8s.network import SVC,Ing
from diagrams.generic.compute import Rack


with Diagram("selenium-k8s"):
    client = Rack("client")
    hub_ing=Ing("hub")
    hub_svc=SVC("hub")
    hub_deploy=Deploy("hub")
    hub_pod=Pod("hub")
    hub_rs=RS("hub")
    
    with Cluster ("Node"):
        node_deploy=Deploy("node")
        with Cluster ("Nodes"):
            node_pod1=Pod("node")
            node_pod2=Pod("node")
            node_pod3=Pod("node")
        node_rs=RS("node")
        node_deploy >> node_pod1
        node_deploy >> node_pod2
        node_deploy >> node_pod3
        node_rs >> Edge(color="blue", style="dashed") >> node_deploy
        

    hub_deploy << Edge(color="blue", style="dashed") << hub_rs
    hub_ing >> hub_svc >> hub_deploy >> hub_pod
    
    node_pod1 >> hub_svc
    node_pod2 >> hub_svc
    node_pod3 >> hub_svc
    client >> hub_ing