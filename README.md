# ServiceManager credit exam
Directory `services` contains several configuration files describing various services that must be highly available
(always running).
The configuration service has the following format:
```
SERVICE_NAME=name
PROGRAM=path_to_the_program
RUN_ARGS=program arguments to pass
HEALTH_ENDPOINT={path}
PORT={port}
ENABLED=true
```
Your program must start all the services and continuously monitor them using the health endpoints. If 3 continuous 
responses from health endpoints do not return `2xx`, then you must restart the service.

Response status can be retrieved by:
```java
HttpURLConnection http = (HttpURLConnection) url.openConnection();
int statusCode = http.getResponseCode();
```

The health endpoints probing happens every 15 seconds. Your program also accepts the following commands from `STDIN`:
- `show-status` – shows status of all services
    - `HEALTHY` - last 3 probes were successful
    - `TENTATIVE` - at least 1 error in the last 3 probes
    - `DOWN` - all 3 probes failed or the startup was not successful
    - `DISABLED` - service is disabled
- `disable ${name}` - stop the service and do not attempt to start it again
- `enable ${name}` - enables the disabled service

## server.py
Copy the `server.py` file to `/tmp` folder. You can test it yourself from command line by running `curl ${URL}`.
