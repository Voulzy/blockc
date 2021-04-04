# blockc

POC for a distributed immutable Car data registration  
##Pre requis  
python x >=3.8  
pyota  
numpy

###Configuration  
* Create a seed with cat /dev/urandom |tr -dc A-Z9|head -c${1:-81} (Linux)  // Or use ours, from seed folder  
* Generate some transactions to the tangle, with send_data.py  

###Get your transcations  
* run ui.py, with the UID of your transaction (VIN later)

####Additional feature  
Request transaction from your car. Send a request (send_request.py), then read it from your car (read_request). After, you can see it with ui.py

