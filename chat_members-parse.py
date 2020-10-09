# chat-members-parse.py (c) 2020 Daniel P. Maloney
# count up how long each member stayed in the chat
import fileinput
total_time = {}
# read from log file specified on command line
for record in fileinput.input():
    fields = []
    fields = record.split('\t')
    # not actually using the time - just assuming 2 minutes per log entry
    time = fields.pop(0)
    users_in_chat = fields
    # tally up times for each user, assuming 2 minute cron timing
    for user in users_in_chat:
        if user in total_time:
            total_time[user] += 2
        else:
            total_time[user] = 2

for key in total_time.keys():
    print(key.strip(), '\t', total_time[key])
      
