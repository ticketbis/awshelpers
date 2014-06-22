"""
    AWS Route53 Helpers
"""
import boto.route53
from boto.route53.record import (ResourceRecordSets)
import settings

def _get_connection():
    """Returns a route53 connection"""
    return boto.connect_route53()

def get_hosted_zones():
    """
        Get a zone list
    """
    conn = _get_connection()
    hosted_zones = conn.get_zones()
    return hosted_zones

def get_hosted_zone_id(domain):
    """Get the zone id of a provided domain"""
    conn = _get_connection()
    zone = conn.get_zone(domain)
    if zone:
        return zone.id
    else:
        raise ValueError("The domain %s doesn't exists" % (domain))

def create_zone(domain, domain_type):
    """
        Create a hosted zone.
        Parameters:
        - domain - the domain to create
        - domain_type - Type specified in the settings.py
    """
    print "Creating domain: %s ...." % (domain)
    conn = _get_connection()

    # Check if the hosted zone exists. If it exists, exit
    if conn.get_zone(domain):
        raise ValueError("The domain %s already exists!" % (domain))
    else:
        zone = conn.create_zone(domain)

    try:
        domain_settings = getattr(settings, domain_type)
        changes = ResourceRecordSets(conn, zone.id)

        ## Adding A records
        for key_record in domain_settings["records_a"].iterkeys():
            # TODO revisar comportamiento de @ . Actualizar los docs de settings
            if key_record == "@":
                name_sub = domain
            else:
                name_sub = key_record + "." + domain
            record_a = domain_settings["records_a"][key_record]
            print "Creating A record %s values %s" % (name_sub, record_a)
            if len(record_a) > 1:
                change = changes.add_change(
                    action="CREATE",
                    name=name_sub,
                    type="A",
                    alias_hosted_zone_id=record_a[0],
                    alias_dns_name=record_a[1],
                    alias_evaluate_target_health=False)
            elif len(record_a) == 1:
                change = changes.add_change("CREATE", name_sub, "A")
                change.add_value(record_a[0])

        ## Adding CNAME records
        for key_record in domain_settings["records_cname"].iterkeys():
            value_cname = domain_settings["records_cname"][key_record]
            if value_cname == "@":
                value_cname = domain
            name_sub = key_record + "." + domain
            print "Creating CNAME record %s values %s" % (name_sub, value_cname)
            change = changes.add_change("CREATE", name_sub, "CNAME")
            change.add_value(value_cname)

        ## Adding MX records
        for key_record in domain_settings["records_mx"].iterkeys():
            print "Creating MX record %s values:" % (domain)
            change = changes.add_change("CREATE", domain, "MX")
            for value_mx in domain_settings["records_mx"][key_record]:
                print value_mx
                change.add_value(value_mx)

        result = changes.commit()
        print result
        print "Zone %s created" % (domain)
    except Exception, exception:
        print exception
        delete_zone(domain)

def delete_zone(domain):
    """
        Delete hosted zone by name
    """
    conn = _get_connection()

    # Check if the hosted zone exists. If not exit
    zone = conn.get_zone(domain)
    if zone:
        print "Deleting %s zone. ID: %s ..." % (zone.name, zone.id)
        for record_set in zone.get_records():
            # Dejamos los records NS y SOA que son obligatorios en una zona
            if record_set.type != "NS" and record_set.type != "SOA":
                zone.delete_record(record_set)
        zone.delete()
        print "%s zone. ID: %s DELETED" % (zone.name, zone.id)
    else:
        raise ValueError("The domain %s does not exists!" % (domain))

def add_record_a_all(subdomain, hosted_zone_id, dns_name):
    """
        Add an A record subdomain with ELB configurations
    """
    hosted_zones = get_hosted_zones()
    for zone in hosted_zones:
        add_record_a(zone.name, subdomain, hosted_zone_id, dns_name)

def remove_record_a_all(subdomain, hosted_zone_id, dns_name):
    """
        Remove an A record subdomain with ELB configurations
    """
    hosted_zones = get_hosted_zones()
    for zone in hosted_zones:
        remove_record_a(zone.name, subdomain, hosted_zone_id, dns_name)

def add_record_a(domain, subdomain, hosted_zone_id, dns_name):
    """
        Add subdomain from a domain
    """
    conn = _get_connection()

    zone = conn.get_zone(domain)
    if zone:
        record_set = zone.get_a(subdomain + "." + domain)
        if record_set:
            raise ValueError("The subdomain %s exists in the %s domain!" % (subdomain, domain))
        else:
            record_sets = zone.get_records()
            record_sets.add_change(
                action="CREATE",
                name=subdomain + "." + domain,
                type="A",
                alias_hosted_zone_id=hosted_zone_id,
                alias_dns_name=dns_name,
                alias_evaluate_target_health=False)

            record_sets.commit()
            print "Subdomain %s created at domain %s" % (subdomain, domain)
    else:
        raise ValueError("The domain %s does not exists!" % (domain))

def remove_record_a(domain, subdomain, hosted_zone_id, dns_name):
    """
        Remove subdomain from a domain
    """
    conn = _get_connection()

    zone = conn.get_zone(domain)
    if zone:
        record_set = zone.get_a(subdomain + "." + domain)
        if record_set:
            # zone.delete_a(domain)
            record_sets = zone.get_records()
            record_sets.add_change(
                action="DELETE",
                name=subdomain + "." + domain,
                type="A",
                alias_hosted_zone_id=hosted_zone_id,
                alias_dns_name=dns_name,
                alias_evaluate_target_health=False)

            record_sets.commit()
            print "Subdomain %s removed from domain %s" % (subdomain, domain)
        else:
            raise ValueError("The subdomain %s does not exist in the %s domain!" % (subdomain, domain))
    else:
        raise ValueError("The domain %s does not exists!" % (domain))


