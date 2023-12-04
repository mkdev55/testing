resp=$(curl -s https://jsonplaceholder.typicode.com/users/1)


email=$(echo $resp | jq -r '.email')

if [[ $email = 'Sincere@april.biz' ]];
then
    echo "logged in"
else
    echo "bad credential"
fi