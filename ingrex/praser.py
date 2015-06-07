"Ingrex praser deal with message"
import datetime

def message(raw_msg):
    "message praser"
    msg = {}
    msg['guid'] = raw_msg[0]
    msg['timestamp'] = raw_msg[1]
    daytime = datetime.datetime.fromtimestamp(raw_msg[1] // 1000)
    daytime += datetime.timedelta(milliseconds=(raw_msg[1] % 1000))
    msg['time'] = daytime.strftime('%Y/%m/%d %H:%M:%S:%f')[:-3]
    msg['text'] = raw_msg[2]['plext']['text']
    msg['type'] = raw_msg[2]['plext']['plextType']
    msg['team'] = raw_msg[2]['plext']['team']
    if raw_msg[2]['plext']['categories'] == 1:
        msg['tab'] = 'all'
    elif raw_msg[2]['plext']['categories'] == 2:
        msg['tab'] = 'resfaction'
    elif raw_msg[2]['plext']['categories'] == 3:
        msg['tab'] = 'enlfaction'
    elif raw_msg[2]['plext']['categories'] == 4:
        msg['tab'] = 'alerts'
    atom = raw_msg[2]['plext']['markup']
    if msg['type'] == 'SYSTEM_BROADCAST':
        if atom[1][1]['plain'] == ' captured ':
            msg['action'] = 'CAPTRUE_PORTAL'
            msg['user'] = atom[0][1]['plain']
            msg['portal'] = atom[2][1]['guid']
        elif atom[1][1]['plain'] == ' deployed an ':
            msg['action'] = 'DEPLOY_RES'
            msg['user'] = atom[0][1]['plain']
            msg['info'] = atom[2][1]['plain']
            msg['portal'] = atom[4][1]['guid']
        elif atom[1][1]['plain'] == ' destroyed an ':
            msg['action'] = 'DESTROY_RES'
            msg['user'] = atom[0][1]['plain']
            msg['info'] = atom[2][1]['plain']
            msg['portal'] = atom[4][1]['guid']
        elif atom[1][1]['plain'] == ' linked ':
            msg['action'] = 'CREATE_LINK'
            msg['user'] = atom[0][1]['plain']
            msg['portal'] = [atom[2][1]['guid'], atom[4][1]['guid']]
        elif atom[1][1]['plain'] == ' destroyed the Link ':
            msg['action'] = 'DESTROY_LINK'
            msg['user'] = atom[0][1]['plain']
            msg['portal'] = [atom[2][1]['guid'], atom[4][1]['guid']]
        elif atom[1][1]['plain'] == ' created a Control Field @':
            msg['action'] = 'CREATE_FIELD'
            msg['user'] = atom[0][1]['plain']
            msg['info'] = atom[4][1]['plain']
            msg['portal'] = atom[2][1]['guid']
        elif atom[1][1]['plain'] == ' destroyed a Control Field @':
            msg['action'] = 'DESTROY_FIELD'
            msg['user'] = atom[0][1]['plain']
            msg['info'] = atom[4][1]['plain']
            msg['portal'] = atom[2][1]['guid']
        elif atom[0][1]['plain'] == 'The Link ':
            msg['action'] = 'DECAY_LINK'
            msg['user'] = 'NEUTRAL'
            msg['portal'] = [atom[1][1]['guid'], atom[3][1]['guid']]
        elif atom[0][1]['plain'] == 'Control Field @':
            msg['action'] = 'DECAY_FIELD'
            msg['user'] = 'NEUTRAL'
            msg['portal'] = atom[1][1]['guid']
    elif msg['type'] == 'PLAYER_GENERATED':
        pass
    elif msg['type'] == 'SYSTEM_NARROWCAST':
        pass
    return msg
