from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2, ECS
from diagrams.aws.database import RDS
from diagrams.aws.network import NATGateway, InternetGateway, ALB
from diagrams.onprem.network import Internet
from diagrams.onprem.client import Users

with Diagram("Web Server Diagram", direction="TB"):

  with Cluster("VPC"):
    igw = InternetGateway("Internet Gateway")
    alb_01 = ALB("load balancer")

    with Cluster("public subnet1"):
      nat_01 = NATGateway("NATGateway\n(for maintenance)")

    with Cluster("public subnet2"):
      bastion_01 = EC2("Bastion\n(for maintenance)")
    
    with Cluster("private subnet1"):
      ec2_01 = EC2("web server");
    
    with Cluster("private subnet2"):
      ec2_02 = EC2("web server");
  
  igw >> alb_01
  alb_01 >> ec2_01
  alb_01 >> ec2_02
