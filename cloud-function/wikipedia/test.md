


### Bash Linux Ubuntu 22.04 
```
curl --request POST --url "http://localhost:8080/cloud-function" --header "Content-Type: application/json" --header "accept: application/json" --data '{"object_of_interest": "Artificial Intelligence"}'
```

### Command Prompt - Windows 11
```
curl --request POST --url "http://localhost:8080/cloud-function" --header "Content-Type: application/json" --header "accept: application/json" --data "{\"object_of_interest\": \"Artificial Intelligence\"}"
```

### Power Shell - Windows 11
```
Invoke-WebRequest -Method POST -Uri 'http://localhost:8080/cloud-function' -ContentType 'application/json' -Body '{"object_of_interest": "Artificial Intelligence"}'
```

```
.\test.ps1

```
### Python
python test.py