# PathFinder
A Python script that finds the deepest subdirectory within a path

### Option 1 - Run Script:

1. Clone the repo
2. You can run the following command directly from your terminal:

```shell
python3 PathFinder/main.py. --path YOUR/PATH/HERE
```

### Option 2 - Run Docker Image:

```shell
docker pull mwapechintu/path_finder
docker run -v <YOUR_HOST_PATH>:/app -i -d mwapechintu/path_finder --path /app
docker ps -a
docker start -i <CONTAINER_ID>
```

