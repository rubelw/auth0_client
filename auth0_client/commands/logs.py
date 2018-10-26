import click
from auth0_client.Auth0Client import Auth0Client
from auth0_client.cli_util import ( get_config_dict, group, highlight)


@group(short_help='Logs')
def logs():
    """ Connections """


logs.help = highlight(logs.help, ['Create:', 'Delete:', 'Update:'], 'green')

@logs.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--page', '-p', help='Page number, zero based', required=True)
@click.option('--per-page', '-r', help='The amount of entries per page, max 100', required=True)
@click.option('--sort', '-s', help='The field to use for sorting. Use field:order where order is 1 for ascending and -1 for descending. For example date:-1', required=True)
@click.option('--fields', '-f', help='A comma separated list of fields to include or exclude (depending on include_fields) from the result, empty to retrieve all fields', required=True)
@click.option('--include-fields', '-n', help='if the fields specified are to be included in the result, false otherwise. Defaults to true', required=False, is_flag=True, default=True)
@click.option('--include-totals', '-t', help='if a query summary must be included in the result, false otherwise. Default false.', required=False, is_flag=True, default=True)
@click.option('--from-param', '-r', help='Log Event Id to start retrieving logs. You can limit the amount of logs using the take parameter.', required=True)
@click.option('--take', '-k', help='The total amount of entries to retrieve when using the from parameter. Default: 50. Max value: 100', required=True)
@click.option('--query', '-q', help='Query in Lucene query string syntax.', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def search_log_events(
        ini,
        page,
        per_page,
        sort,
        fields,
        include_fields,
        include_totals,
        from_param,
        take,
        query,
        debug
    ):

    fields = fields.split(',')
    client = Auth0Client(get_config_dict(ini, debug))
    print(client.search_log_events(
        page=page,
        per_page=per_page,
        sort=sort,
        fields=fields,
        include_fields=include_fields,
        include_totals=include_totals,
        from_id=from_param,
        take=take,
        query=query
    )

@logs.command()
@click.option('--ini', '-i', help='INI file with needed information', required=True)
@click.option('--log-id', '-u', help='log id', required=True)
@click.option('--debug', help='Turn on debugging', required=False, is_flag=True)
def get_log_event_by_id(
        ini,
        log_id,
        debug
    ):

    client = Auth0Client(get_config_dict(ini, debug))
    print(client.get_log_events_by_id(log_id))





