# CPSC449Project2 - Group 20

### Group Members:
##### Shreya Bhattacharya

---
## **Setting up NginxConfig**
#### Add Nginx config file "project2NginxConfig"  at path `/etc/nginx/sites-enabled`

## **Initializing Database & Start Service:**

##### `./bin/init.sh`
##### `foreman start`

---

## **Testing the APIs**
### Note: In order to run the API, you will ocasionally have to to supply specific variables. Any time this is required, please replace the < variable > with the correct information.

### **Leaderboard Service**

#### Api for posting game result of the users:
#### `http POST http://games.local.gd/user/registration username=<USERNAME> userpassword=<PASSWORD>`

#### API for retreiving top 10 users by average score
http GET http://127.0.0.1:5200/top-scorers
or
http POST http://games.local.gd/docs/top-scorers


