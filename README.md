# Jenkins Vagrant CI

Infrastructure as Code for a Jenkins CI/CD server using Vagrant and VirtualBox. Provisions an automated Jenkins instance with a Flask application to demonstrate pipeline configuration.

## Overview

Automates the setup of a Jenkins server in a VirtualBox VM using Vagrant provisioning. Includes a sample Python Flask application with a Jenkinsfile to demonstrate a complete CI/CD pipeline.

## Tech Stack

- Vagrant
- VirtualBox
- Jenkins
- Python / Flask
- Docker

## Setup

```bash
vagrant up
# Access Jenkins at http://localhost:8080
```

## Structure

- `Vagrantfile` - VM configuration and provisioning
- `Dockerfile` - Container for pipeline steps
- Flask app for pipeline testing
