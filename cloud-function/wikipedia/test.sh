 #* Running on all addresses (0.0.0.0)
 #* Running on http://127.0.0.1:8080
 #* Running on http://192.168.1.188:8080

echo "Test1"
curl --request POST \
    --url 'http://localhost:8080/cloud-function' \
    --header 'accept: application/json' \
    --data '{"object_of_interest": "Artificial Intelligence"}'

echo "Test2"

curl --request POST \
--url 'http://localhost:8080/cloud-function' \
--header 'accept: application/json' \
--data '{"object_of_interest": "Artificial Intelligence"}'


echo "Test3"

curl -X POST \
-H "Content-Type: application/json" \
-d '{"object_of_interest": "Artificial Intelligence"}' \
http://localhost:8080/cloud-function

echo "Test4"

curl --request POST \
--url 'http://127.0.0.1:8080/cloud-function' \
--header 'accept: application/json' \
--data '{"object_of_interest": "Artificial Intelligence"}'
