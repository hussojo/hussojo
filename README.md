firs I'm installing virtualenv:
```
josefina@x230:~$ sudo apt-get -y install virtualenv
```
activating virtualenv:
```
josefina@x230:~$ source env/bin/activate
(env) josefina@x230:~$ 
```
making sure my django is up to date:
```
(env) josefina@x230:~$ django-admin --version
4.0.4
```
## Starting a project named hussojo:
```
(env) josefina@x230:~$ django-admin startproject hussojo
```
testing if the projects development server is up:
```
(env) josefina@x230:~/hussojo$ ./manage.py runserver
```
And it works
![Screenshot from 2022-05-26 12-24-12](https://user-images.githubusercontent.com/106306928/170511443-1ee27e36-148b-44f5-bc7d-12649c2639b8.png)

## Adding admin and users

I already had pwgen installed so I went ahead and asked it to randomize one password of 10 characters
```
^C(env) josefina@x230:~/hussojo$ pwgen -s 10 1
```
Then created a superuser and used the pasword:
```
(env) josefina@x230:~/hussojo$ ./manage.py createsuperuser
Username (leave blank to use 'josefina'): 
Email address: husso.josefina@gmail.com
Password: 
Password (again): 
Superuser created successfully.
```
Testing my new superuser, tried adding /admin to http://127.0.0.1:8000/ but it didn't work
![Screenshot from 2022-05-26 13-04-21](https://user-images.githubusercontent.com/106306928/170511678-8f6d1bea-ba57-40f5-986a-dd917e14f8bc.png)

Made migrations and run server again and it worked
```
(env) josefina@x230:~/hussojo$ ./manage.py makemigrations
(env) josefina@x230:~/hussojo$ ./manage.py migrate
(env) josefina@x230:~/hussojo$ ./manage.py runserver
```
![Screenshot from 2022-05-26 13-05-54](https://user-images.githubusercontent.com/106306928/170511813-d979b567-d903-480f-9614-750f6a8d730f.png)

![Screenshot from 2022-05-26 13-09-17](https://user-images.githubusercontent.com/106306928/170511843-c92ee0ec-d457-45a2-b132-7a2f8804d608.png)


Next added another superuser named Ari, and started ofcourse with generating random password
```
C(env) josefina@x230:~/hussojo$ pwgen -s 10 1
```
```
josefina@x230:~/hussojo$ ./manage.py createsuperuser
Username: Ari
Email address: 
Password: 
Password (again): 
Superuser created successfully.
```

After making migrations I tested superuser Ari, and it worked. I also noticed that username is case-sensitive.
![Screenshot from 2022-05-26 13-19-14](https://user-images.githubusercontent.com/106306928/170511920-e420df21-3f98-40e7-a120-0b8db06d1d36.png)


Now I have a Django development server with two admins.
