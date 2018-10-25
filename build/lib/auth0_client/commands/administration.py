import click
import json
import sys
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import (pretty, get_config_dict, group, highlight)

@group(short_help='Administration')
def administration():
    """ Connections """


administration.help = highlight(administration.help, ['Create:', 'Delete:', 'Update:'], 'green')

@administration.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def dump_account_details(
        ini,
        debug
    ):

    # Get client
    client = Auth0Client(get_config_dict(ini, debug))

    # Get all clients applications
    print("\n#######################")
    print('Client Applications')
    print("#########################")

    client_data = client.get_all_client_applications()

    print(client_data)
    client_data = json.loads(client_data)
    client_ids = {}
    for client_info in client_data:
        if 'client_id' in client_info:
            temp={}
            temp['client_id'] = client_info['client_id']
            temp['name']= client_info['name']
            client_ids[client_info['client_id']] = client_info['name']

    print('client ids:')
    print(pretty(client_ids))
    # Get all users
    print("\n#######################")
    print('Users')
    print("#########################")


    user_data = client.list_users()
    #print(user_data)
    user_data = json.loads(user_data)

    user_ids = []

    for user in user_data:
        print('user: '+str(pretty(user)))
        if 'user_id' in user and 'email' in user:
            user_ids.append(user['user_id'])
            print('###################')
            print('id: ' + str(user['user_id']))
            print('email:'+str(user['email']))
            print('###################')


            print("\n\t#######################")
            print("\t"+'Guardian Enrollments')
            print("\t#########################")

            guardian_enrollment_data = client.get_list_of_guardian_enrollments(user_id=user['user_id'])
            print(guardian_enrollment_data)

            print("\n\t#######################")
            print("\t"+'User Blocks')
            print("\t#########################")

            user_blocks_data = client.list_user_blocks(user_id=user['user_id'])
            print(user_blocks_data)

            print("\n\t#######################")
            print("\t"+'User Logs')
            print("\t#########################")

            user_logs_data = client.get_user_log_events(user_id=user['user_id'])
            print(user_logs_data)





    # Get all rules
    print("\n#######################")
    print('Rules')
    print("#########################")


    rules_data = client.get_all_rules()
    print(rules_data)


    # Get all grants
    print("\n#######################")
    print('Grants')
    print("#########################")


    grants_data = client.get_client_grants()
    print(grants_data)

    grants_data = json.loads(grants_data)
    grant_ids = {}
    for grants_info in grants_data:
        if 'client_id' in grants_info and 'audience' in grants_info:
            temp={}
            temp['client_id']= grants_info['client_id']
            temp['audience'] = grants_info['audience']
            grant_ids[grants_info['id']]=[]
            grant_ids[grants_info['id']].append(temp)


    print("\n###### Grant Ids #########")
    print(pretty(grant_ids))


    # Get more grants

    for id in grant_ids:
        print(grant_ids[id])

        for user in user_ids:

            print('user: '+str(user))
            user_grants = client.get_all_grants(user_id=user, client_id=grant_ids[id][0]['client_id'], audience=grant_ids[id][0]['audience'])
            print(user_grants)
    sys.exit(1)
    #print(client.get_all_grants(user_id=user_id, client_id=client_id, audience=audience))








    # Get all connections
    print("\n#######################")
    print('Connections')
    print("#########################")


    connection_data = client.get_all_connections()
    print(connection_data)



    # Get all Guardian Factors
    print("\n#######################")
    print('Guardian Factors')
    print("#########################")


    factor_data = client.list_factors()
    print(factor_data)

    # Get all Guardian Enrollment Templates
    print("\n#######################")
    print('Guardian Enrollment Templates')
    print("#########################")


    template_data = client.list_enrollment_templates()
    print(template_data)

    # Get all Guardian SNS Factor Provider Config
    print("\n#######################")
    print('Guardian SNS Factor Provider Config')
    print("#########################")


    sns_factor_config_data = client.list_sns_factor_provider_config()
    print(sns_factor_config_data)



    # Get all Guardian Twilio Factor Provider Config
    print("\n#######################")
    print('Guardian Twilio Factor Provider Config')
    print("#########################")


    twilio_factor_config_data = client.list_twilio_factor_provider_config()
    print(twilio_factor_config_data)



    # Get all Resource Servers
    print("\n#######################")
    print('Resource Servers')
    print("#########################")


    resource_data = client.get_all_resource_servers()
    print(resource_data)

    # Daily Stats
    print("\n#######################")
    print('Daily Stats')
    print("#########################")


    stats_data = client.daily_stats(2)
    print(stats_data)


    # Tenants
    print("\n#######################")
    print('Tenants')
    print("#########################")


    tenants_data = client.get_tenants()
    print(tenants_data)
