# check-verifica-copertura
We needed to check that our CDN was distributing the correct version of a js.
To verifiy the correct file I check the presence of a json in the javascript code and if it's not correct
the script sends a message to a telegram channel.
As debug information I add which CND **nodes** are at work ("**via**" header), the **Etag** and the **size**.
Positive checks are only logged
This script was setup in cron to run every 10 minutes
