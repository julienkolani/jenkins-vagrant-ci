# Jenkins Vagrant CI

Infrastructure as Code pour un serveur Jenkins CI/CD provisionné automatiquement avec Vagrant.

## Contenu

- `vagrant-jenkins-master/` — Vagrantfile et script de provisioning
- `Presentation_Jenkins/` — Application Flask de test de pipeline (Python)
- `Rendu_groupe_11/` — Application Spring Boot avec Jenkinsfile, stack Docker Nginx + Jenkins, rapport CI/CD

## Stack technique

- Vagrant, VirtualBox
- Jenkins, Docker, Nginx
- Python/Flask, Spring Boot (Java)

## Utilisation

```bash
cd vagrant-jenkins-master
vagrant up
# Jenkins disponible sur http://localhost:8080
```
