# Echo Server
Test Server for Arcturus Platform

```
docker run -p 8080:8080 -it mcntech/test-srv-echo
```

```
curl -X POST -H "Content-Type: application/json" --data '{"message": "Hello"}' localhost:8080/api/echo
```