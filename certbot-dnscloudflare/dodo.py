def task_list_certificates():
    '''List the SSL certificates available'''
    return {
        'actions': [
            'docker compose -f ./certbot-dnscloudflare/docker-compose.list.yml up'
        ],
        'verbosity': 2
    }

def task_issue_certificate():    
    '''Issue a certificate for a given domain - usage: issue_certificate -d domain.com (required)'''
    return {
        'actions': [
            'DOMAIN=%(domain)s docker compose -f ./certbot-dnscloudflare/docker-compose.issue.yml up'
        ],
        'params': [
            {
                'name': 'domain',
                'short': 'd',
                'default': 'no domain provided'
            },
        ],
        'verbosity': 2
    }

def task_revoke_certificate():    
    '''Revoke the certificate for a given domain - usage: revoke_certificate -d domain.com (required)'''
    return {
        'actions': [
            'DOMAIN=%(domain)s docker compose -f ./certbot-dnscloudflare/docker-compose.revoke.yml up'
        ],
        'params': [
            {
                'name': 'domain',
                'short': 'd',
                'default': 'no domain provided'
            },
        ],
        'verbosity': 2
    }