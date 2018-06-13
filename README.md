# syndicator

5 websites/apps where Pulsd events can be reposted:

1. eventbrite.com
2. Facebook.com
3. Groupon.com
4. nyc.com
5. Thrillest

We can call the apis for eventbrite to post events. I am not actually
going to call those apis though.

I couldn't get the frontend to connect to the api because of
cross-origin issues. I ran out of time to figure it out.

To start the api:
./start

Examples:
curl -X GET http://localhost:5000/events
curl -X GET http://localhost:5000/events/<id>
curl -X POST http://localhost:5000/events -H 'Content-Type: application/json' -d '{"name":"event4","price":"99.99","start_time":"2018-06-20T06:00:00","start_timezone":"EST","end_time":"2018-06-20T10:00:00","end_timezone":"EST"}'

To start the ui:
cd portal
ng serve -open