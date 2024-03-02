# Specify the URL and data
$url = 'http://localhost:8080/cloud-function'
$data = '{"object_of_interest": "Artificial Intelligence"}'

# Send the POST request
$response = Invoke-WebRequest -Method POST -Uri $url -ContentType 'application/json' -Body $data

# Display the response
Write-Output $response
