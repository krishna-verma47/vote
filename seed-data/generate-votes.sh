# #!/bin/sh

# # create 3000 votes (2000 for option a, 1000 for option b)
# ab -n 1000 -c 50 -p posta -T "application/x-www-form-urlencoded" http://vote/
# ab -n 1000 -c 50 -p postb -T "application/x-www-form-urlencoded" http://vote/
# ab -n 1000 -c 50 -p posta -T "application/x-www-form-urlencoded" http://vote/

#!/bin/bash

# Use the environment variable or default to "vote"
VOTE_HOST=${1:-"vote"}

# Use the obtained hostname in your ab command
ab -n 1000 -c 10 -p /seed/data.txt -T application/json http://$VOTE_HOST:5000/vote

