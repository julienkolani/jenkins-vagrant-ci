#!/usr/bin/env bash

# Mettre à jour les paquets
sudo apt-get update -y
sudo apt-get upgrade -y

# Installer Java (Jenkins en a besoin)
sudo apt-get install -y openjdk-11-jdk

# Ajouter la clé et le dépôt Jenkins
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'

# Installer Jenkins
sudo apt-get update -y
sudo apt-get install -y jenkins

# Démarrer Jenkins et l'activer au boot
sudo systemctl enable jenkins
sudo systemctl start jenkins

# (Optionnel) Vérifier que Jenkins tourne
sudo systemctl status jenkins | grep Active

# Afficher le mot de passe initial
echo "Mot de passe admin Jenkins :"
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
