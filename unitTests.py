import requests
import json
import xml.etree.ElementTree as ET
import subprocess
import time
import psutil
from datetime import datetime
import matplotlib.pyplot as plt


"""
UNIT TESTS FOR ECSE 429 PROJECT A
ON LOCALHOST:4567 
API DOCUMENTATION CAN BE FOUND ON LOCALHOST:4567/docs
"""

t1_start = datetime.now()
t1_end = datetime.now()

t2_start = datetime.now()
t2_end = datetime.now()

sample_time_POST = []
num_objects_POST = []
time_t2_POST = []
free_memory_POST = []
cpu_usage_POST = []

sample_time_DELETE = []
num_objects_DELETE = []
time_t2_DELETE = []
free_memory_DELETE = []
cpu_usage_DELETE = []

sample_time_PUT = []
num_objects_PUT = []
time_t2_PUT = []
free_memory_PUT = []
cpu_usage_PUT = []


def setup_module(objects):
    
        t1_start = datetime.now()

        
        print("T1 start time: ",t1_start)
    
        subprocess.Popen(["java", "-jar", "runTodoManagerRestAPI-1.5.5.jar"], close_fds=True)
        subprocess.Popen(["sleep", "1s"]).communicate()
        
        num_objects_POST.append(objects)
        
        for x in range(objects):
        
            json_input = {
                    
                    "title": "ecse 429",
                    "description": "project"
                    
            }
            request_json = json.dumps(json_input)
            
            #create post request
            response = requests.post("http://localhost:4567/todos", request_json)
            assert response.status_code == 201
            
            #check json output
            response_body = response.json()
            assert response_body["title"] == "ecse 429"
        
        

def teardown_module():
    
        subprocess.Popen(["curl", "--location", "--request", "GET", "http://localhost:4567/shutdown"], close_fds=True)
        subprocess.Popen(["sleep", "1s"]).communicate()
        t1_end = datetime.now()
        print("T1 end time: ",t1_end)
        
        print("T1: ", (t1_end - t1_start).total_seconds())


# # check if http status code is 200 when service is running
# def test_http_returns_code_200():
#       response = requests.get("http://localhost:4567")
#       assert response.status_code == 200

# """ localhost:4567/todos TESTS
# ------------------------------------------------------------------- """


# test POST /todos with title
def test_POST_todo_with_title():
    """Test for POST /todo with JSON request
    Expecting: 201 OK, JSON output [title] """
    
        
    t2_start = datetime.now()
    print("T2 start time: ",t2_start)
    
    json_input = {
            
            "title": "ecse 429",
            "description": "project"
            
    }
    request_json = json.dumps(json_input)
    
    #create post request
    response = requests.post("http://localhost:4567/todos", request_json)
    assert response.status_code == 201
    
    #check json output
    response_body = response.json()
    assert response_body["title"] == "ecse 429"
    
    t2_end = datetime.now()
    print("T2 (Sample Time): ",t2_end)
    sample_time_POST.append(t2_end)
    
    print("T2: ", (t2_end - t2_start).total_seconds())
    time_t2_POST.append((t2_end - t2_start).total_seconds())
    
    # print("% cpu usage: ", psutil.cpu_percent())
    cpu_usage_POST.append(psutil.cpu_percent())
    
    print("% free memory", round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total, 1))
    free_memory_POST.append(round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total, 1))
    
        
    
#Test for DELETE /todos/:id
def test_DELETE_todo():
    """Test for DELETE /todo/:id with valid ID request
    Expecting: 200 """
    
    t2_start = datetime.now()
    print("T2 start time: ",t2_start)
    
    response = requests.delete("http://localhost:4567/todos/1")
    assert response.status_code == 200
    
    t2_end = datetime.now()
    print("T2 (Sample Time): ",t2_end)
    sample_time_DELETE.append(t2_end)
    
    print("T2: ", (t2_end - t2_start).total_seconds())
    time_t2_DELETE.append((t2_end - t2_start).total_seconds())
    
    # print("% cpu usage: ", psutil.cpu_percent())
    cpu_usage_DELETE.append(psutil.cpu_percent())
    
    print("% free memory", round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total, 1))
    free_memory_DELETE.append(round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total, 1))
    

# Test for PUT /todos/:id with VALID ID of 1
def test_PUT_validID():
    """Test for PUT /todo/:id with JSON request and Valid ID
    Expecting: 200 OK """
    
    t2_start = datetime.now()
    
    json_input = {
            
            "title": "Testing PUT with updated Title",
            "description": "updated Description"
            
        }
    
    request_json = json.dumps(json_input)
    response = requests.put("http://localhost:4567/todos/2",request_json)
    assert response.status_code == 200
    
    t2_end = datetime.now()
    print("T2 (Sample Time): ",t2_end)
    sample_time_PUT.append(t2_end)
    
    print("T2: ", (t2_end - t2_start).total_seconds())
    time_t2_PUT.append((t2_end - t2_start).total_seconds())
    
    # print("% cpu usage: ", psutil.cpu_percent())
    cpu_usage_PUT.append(psutil.cpu_percent())
    
    print("% free memory", round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total, 1))
    free_memory_PUT.append(round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total, 1))
    
    
    
    
    
numbers_sizes = (i*10**exp for exp in range(2, 4) for i in range(1,13))
for n in numbers_sizes:
    
    print("n: ", n)
    
    setup_module(n)
    
    test_POST_todo_with_title()
    test_DELETE_todo()
    test_PUT_validID()
    
    teardown_module()

plt.plot(sample_time_POST, time_t2_POST, '-', label='POST')
plt.plot(sample_time_DELETE, time_t2_DELETE, '-', label='DELETE')
plt.plot(sample_time_PUT, time_t2_PUT, '-', label='PUT')

plt.legend()
plt.xlabel('Sample time')
plt.ylabel('Transaction time')
plt.show()




   
            

