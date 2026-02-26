# Inventory management API

Backend system to manage your inventory effectively.

## Overview

This API is a control environment that helps you to have a complete vision about your products.

## Core Features

- Real-time tracking of inbound and outbound inventory movements
- Full lot traceability across storage locations
- Monitor real-time stock levels and product availability
- Intelligent alerts for slow-moving and low-stock products


## Project Structure

```text
inventory_management_api/
├──apps/
│   ├──inventory/
│      ├──migrations/
│      ├──models.py
│      ├──tests.py
│      ├──views.py
│   ├──user
│      ├──migrations/
│      ├──models.py
│      ├──tests.py
│      ├──views.py
├──logs
├──settings
│   ├──base.py
│   ├──dev.py
│   ├──prod.py
│   ├──test.py
asgi.py
urls.py
wsgi.py
.gitignore
docker-compose.yaml
manage.py
README.md
requirements.txt
```

## Tech Stack

- Python
- Django
- PostgreSQL
- Git
- Docker