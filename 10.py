#Segmentar datos de un correo
email = input("Cual es tu direccion de correo? ").strip()
user_name = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
output = "Your username is '{}' and your domain name is '{}'".format(user_name,domain_name)

# Display output message
print(output)