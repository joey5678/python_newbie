from nova.compute import compute_context
from nova.compute import clients


def keystone_test():
    kwargs = {
        'username': 'admin',
        'password': 'openstack',
        'tenant': 'admin',
        'auth_url': 'http://162.2.110.185:5000/v2.0/',
        'region_name': 'CascadedOne'
    }

    reqCon = compute_context.RequestContext(**kwargs)
    openStackClients = clients.OpenStackClients(reqCon)

    #Nova client
    cascadedNovaCli = openStackClients.nova()
    search_opts_args = {'all_tenants': True}
    #servers = cascadedNovaCli.servers.list()

    #Neutron client
    neutron_client = openStackClients.neutron()
    port_search_opts = {'status':'ACTIVE'}
    ports = neutron_client.list_ports(**port_search_opts)
    if ports['ports']:
        ports = ports['ports']
        print 'number of ports: '
        print (len(ports))
    else:
        return
    for port in ports:
        print port
    networks = neutron_client.list_networks()
    print 'number of networks'
    if networks['networks']:
        networks = networks['networks']
    else:
        return
    for net in networks:
        print net

keystone_test()
