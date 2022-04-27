### Description

Simple API project for interacting with an Inventory Management System implemented in Python using the following libraries.
* FastAPI (API implementation)
* pydantic (Data classes)
* uvicorn (runs the server)

The API implements simple endpoints for
* Querying current inventory
* Creating product entries
* Updating product entries
* Deleting product entries

The code orients at the following tutorial: https://www.youtube.com/watch?v=-ykeT6kk4bk 


### Instructions
* Run from console with 

~~~
uvicorn myapi:app --reload   
~~~

* The documentation for the API is automatically generated on running and can be accessed in the browser at

~~~
localhost:8000/docs
~~~

