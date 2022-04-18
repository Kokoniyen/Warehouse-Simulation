# Read me


```javascript
fetch("http://127.0.0.1:8080/generate_heat_map", {
  "method": "POST",
  "headers": {
    "Content-Type": "application/json"
  },
  "body": "{\"density\":1.205,\"specific_heat\":300,\"heat_conductivity\":0.001,\"init_temp\":20,\"length\":10,\"breadth\":10,\"height\":10,\"num_hours\":5,\"image_path\":\"/Users/mac/Downloads/test.png\"}"
})
.then(response => {
  console.log(response);
})
.catch(err => {
  console.error(err);
});

```

```python
import requests

url = "http://127.0.0.1:8080/generate_heat_map"

payload = {
    "density": 1.205,
    "specific_heat": 300,
    "heat_conductivity": 0.001,
    "init_temp": 20,
    "length": 10,
    "breadth": 10,
    "height": 10,
    "num_hours": 5,
    "image_path": "/Users/mac/Downloads/test.png"
}
headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
```