# syndicator

5 websites/apps where Pulsd events can be reposted:

1. eventbrite.com
2. Facebook.com
3. Groupon.com
4. nyc.com
5. Thrillest

There are two parts to this appication - the Frontend and the backend.
Please start both of them seperately as shown below.

The file requirements.txt has all of the modules needed for the flask app.
You will also need ng to run the angular frontend.

NOTE: I have a weird bug where the background process gets called twice
everytime is runs. I'm sure it is because of the way I set up the daemon
but I couldn't figure out the bug.


To start the api:
./start

Examples:

curl -X GET http://localhost:5000/events
curl -X GET http://localhost:5000/events/<id>
curl -X POST http://localhost:5000/events -H 'Content-Type: application/json' -d '{"name":"event2","price":"99.99","start_time":"2018-06-20T06:00:00","start_timezone":"America/New_York","end_time":"2018-06-20T10:00:00","end_timezone":"America/New_York","currency":"USD"}'

To start the ui:

cd portal

ng serve -open