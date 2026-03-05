# Inventory Management API v1.0

![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)
![Django](https://img.shields.io/badge/Django-6.0.2+-092e20.svg)

Backend for Real-time Stock Control.

## Overview

This is a robust RESTful API built with Django & Django Rest Framework (DRF) designed as a control environment that helps you to have a complete vision about your products.

## Key Features

- Real-time tracking of inbound and outbound inventory movements
- Monitor real-time stock levels and product availability


## Project Structure

```text
inventory_management_api/
├──apps/
│   ├──inventory/
│   │  ├──migrations/
│   │  ├──models.py
│   │  ├──tests.py
│   │  └──views.py
│   └──user
│      ├──migrations/
│      ├──models.py
│      ├──tests.py
│      └─views.py
├──logs
├──settings
│   ├──base.py
│   ├──dev.py
│   ├──prod.py
│   └──test.py
asgi.py
urls.py
wsgi.py
.gitignore
docker-compose.yaml
manage.py
README.md
requirements.txt
```

## Tech Stack & Tools

- Backend: Python 3.x, Django, Django REST Framework.
- Database: PostgreSQL
- Version Control: Git
- DevOps: Docker & Docker Compose (Containerized DB and App).
- Documentation: Drf-spectacular (Swagger UI).