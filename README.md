Auth0 Client
============
Features
========
python click program for auth0

Installation
============
auth0_client is on PyPI so all you need is:

``` {.sourceCode .console
    $ pip install auth0_client
```

Demonstration
=============

<p><a target="_blank" rel="noopener noreferrer" href="https://github.com/rubelw/auth0_client/blob/master/images/demo.gif"><img src="https://github.com/rubelw/auth0_client/raw/master/images/demo.gif" alt="Auth0_Client tutorial" style="max-width:100%;"></a></p>


Example
=======
Getting help

``` {.sourceCode .console
   $ Usage: auth-client [OPTIONS] COMMAND [ARGS]...

    Options:
      -v, --version  Show the current version, and check for latest
      -h, --help     Show this message and exit.
    
    Commands:
      blacklists          Blacklists
      client-grants       ClientGroups
      clients             Clients
      connections         Connections
      custom-domains      Custom Domains
      device-credentials  Device Credentials
      email-templates     Email Templates
      emails              Emails
      grants              Grants
      guardian            Guardian
      jobs                Jobs
      logs                Logs
      resource-servers    Resource Servers
      rule-configs        Rule Configs
      rules               Rule
      stats               Stats
      tenants             Tenants
      tickets             Tickets
      user-blocks         User Blocks
      users               Users
      users-by-email      Users By Email


    auth-client users
    Usage: auth-client users [OPTIONS] COMMAND [ARGS]...
    
      Connections
    
    Options:
      -h, --help  Show this message and exit.
    
    Commands:
      create-a-user
      delete-a-user
      delete-a-users-multifactor-provider
      generate-new-guardian-recovery-code
      get-a-list-of-guardian-enrollments
      get-a-user
      get-users-log-events
      link-a-user-account
      list-or-search-users
      unlink-a-user-identity
      update-a-user
```



To setup autocomplete to enable tabbing on commands
===================================================
Add the following to your ~/.bash_profile

``` {.sourceCode .console
      eval "$(_AUTH_CLIENT_COMPLETE=source auth-client)"
```



Example Ini file
================

``` {.sourceCode .console
    [parameters]
    domain = xxx.auth0.com
    id = xxx
    secret = xxxx
```


