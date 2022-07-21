# Importando a biblioteca troposphere
from troposphere import Template, ec2
# importando a biblioteca YAML
from yaml import dump

temp = Template()  # variavel para receber a estancia

# Servidor AWS Linux
AwsLinux = ec2.Instance(
    "AmazonLinux",
    ImageId="ami-0cff7528ff583bf9a",
    InstanceType="t2.micro"
)

# Servidor Ubuntu Server
UbuntuServer = ec2.Instance(
    "Ubuntu",
    ImageId="ami-052efd3df9dad4825",
    InstanceType="t3.large"
)

# Servidor windoes server 2019
WindowsServer = ec2.Instance(
    "MicrosoftWindowsServer",
    ImageId="ami-05912b6333beaa478",
    InstanceType="t2.2xlarge"
)

# Servidor REd Hat
RedHat = ec2.Instance(
    "RedHat",
    ImageId="ami-06640050dc3f556bb",
    InstanceType="t3.medium"
)

# Servidor Suse
Suse = ec2.Instance(
    "SUSELinuxEnterpriseServer",
    ImageId="ami-08895422b5f3aa64a",
    InstanceType="ti.micro"
)


# adicionando a instancia na variavel temp
temp.add_resource(AwsLinux)  # AWS - Amazon Linux
temp.add_resource(UbuntuServer)  # Ubuntu Server
temp.add_resource(WindowsServer)  # Windows Server 2019
temp.add_resource(RedHat)  # Red Hat
temp.add_resource(Suse)  # SUSE


# Escrevendo um arquivo YAML para as instancia dos servidores
with open("Servidores_ec2.yaml", "w") as file:
    dump(temp, file)
