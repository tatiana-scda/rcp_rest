# RCP REST
client-server solution for a consult system for Peering Data Base  
Client makes HTTP request using API Rest and server will process the response  

You should install Flask and export the FLASK_APP environment  

to run the server:
```
python server.py 8080 net.json ix.json netixlan.json
```
where 8080 can be the port you'd like and you can change the files  


to run the client
```
python client.py 127.0.0.1:8080 1  
```
where you can change IP:PORT and the last digit is the analysis that will be applyed (can be  1 or 0)  


