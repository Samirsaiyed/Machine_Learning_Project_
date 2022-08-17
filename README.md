# Machine_Learning_Project_
# This is machine learning project  

Creating conda environment
```
conda create -p venv python==3.7 -y
```
    
Create a Conda activated
```
conda activate venv/
```

```
pip install -r requirements.txt
```

To add Files to git
```
git add .
```
OR
```
git add <file_name>
```

Note : To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
```
git status
```

To check all version main by git 
```
git log
```

TO create version/commit all changes by git 
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = samirsaiyed49@gmail.com
2. HEROKU_API = 3d62e333-69c9-41f1-b5d2-bac3ecf8a79f
3. HEROKU_APP_NAME = ml-regression-app7  

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```

> Note : Image name for docker must be lowercase

To list docker image 
```
docker images
```

Run docker image 
```
docker run -p 5000:5000 -e PORT=5000 <img-id>
```

To check running containers in Docker
```
docker ps
```

To stop docker container
```
docker stop <container_id>
```
