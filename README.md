Auth0 Client
============
Features
========
python click program for auth0

There is the normal click program called auth-client, for interating with the api.

The is also and administration program called auth-menu for administering Auth0 from the command line.

Installation
============
auth0_client is on PyPI so all you need is:

``` {.sourceCode .console
    $ pip install auth0_client
```

Demonstration
=============

<p><a target="_blank" rel="noopener noreferrer" href="https://github.com/rubelw/auth0_client/blob/master/images/demo.gif"><img src="https://github.com/rubelw/auth0_client/raw/master/images/demo.gif" alt="Auth0_Client tutorial" style="max-width:100%;"></a></p>


Example for auth-client
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

Example for auth-menu
=====================

``` (.sourceCode .console

Host: Williams-MacBook-Pro.local                                  User: rubelw
==============================================================================
  Main Menu
------------------------------------------------------------------------------
  [1] | Blacklists
  [2] | Client Grants
  [3] | Clients
  [4] | Connections
  [5] | Custom Domains
  [6] | Device Credentials
  [7] | Emails
  [8] | Email Templates
  [9] | Grants
  [10] | Guardian
  [11] | Jobs
  [12] | Logs
  [13] | Resource Servers
  [14] | Rules
  [15] | Rules Configs
  [16] | Stats
  [17] | Tenants
  [18] | Tickets
  [19] | User Blocks
  [20] | Users
------+-----------------------------------------------------------------------
  [0] | Quit
==============================================================================
Press menu number (0-20) [ENTER]: 



Host: Williams-MacBook-Pro.local                                  User: rubelw
==============================================================================
  Main Menu > Client Grants
------------------------------------------------------------------------------
  [1] | List Client Grants
------+-----------------------------------------------------------------------
  [0] | Return to Main Menu
==============================================================================
Press menu number (0-1) [ENTER]: 


```
Example Ini file
================

``` {.sourceCode .console
    [parameters]
    domain = xxx.auth0.com
    id = xxx
    secret = xxxx
```


