# Person Registration API

This project is an API designed to register people and manage their career information. The system allows individuals to provide details about their career, and the API handles the data for further processing.

### Features:
- People can register their information including career details.
- The API is built with Django and exposed via a RESTful interface.
  
### Steps to Get Started

#### 1. Update your `hosts` file for local development

##### On Linux:
Run the following command to update your `/etc/hosts` file:

```bash
sudo python3 update_host.py dev.codeleap.co.uk 172.19.0.10
```
Run the following command to update your hosts file:
##### On Windows:

```bash
python3 update_hosts_windows.py dev.codeleap.co.uk 172.19.0.10
```

>Note: This step is necessary to use the service locally with the custom URL https://dev.codeleap.co.uk/. Although a significant amount of time was dedicated to finding a solution that wouldn't require this step, after extensive research and attempts to use local DNS services like dnsmasq, it was determined that this workaround was necessary to resolve the domain locally.
>
>However, if you wish to skip this step, you can make the requests directly to http://0.0.0.0:8000/careers/ instead.

#### 2. Build and start the application
To start the application, run the following command:

bash
Copiar código
docker-compose up --build
This will build the Docker images and start the services defined in docker-compose.yml.

#### 3. Access the API
Once the application is up and running, you can access the API locally by navigating to:


https://dev.codeleap.co.uk/
Make sure to have your local hosts file updated to resolve the custom domain to 127.0.0.1 or the appropriate IP of the Django container.

#### API Endpoints:
 - POST /register: Register a new person with their career information.
 - GET /people: Retrieve a list of all registered people.
 - GET /people/{id}: Retrieve a person's details by their ID.

#### Development:
 - This API is developed using Django, and Docker is used for containerization. The backend is accessible at port 8000 inside the container and is served via Nginx on ports 80 and 443.
