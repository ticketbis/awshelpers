"""
	Main
"""
import pprint
from lib import awsroute53helper
import argparse

# def main(params):
if __name__ == '__main__':

    __prettyprinter__ = pprint.PrettyPrinter(indent=4)


    parser = argparse.ArgumentParser(description="AWS Helpers")
    parser.usage = 'bin/awshelpers'
    parser.add_argument("--list-zones",
        help="List hosted zones",
        action="store_true")
    parser.add_argument("--zone-id",
        help="Get zone id",
        metavar="domain-name",
        type=str)
    parser.add_argument("--create-zone",
        help="Create zone with the given domain-name and \
            the values specified in settings file under the domain-type block",
        metavar=("domain-name", "domain-type"),
        type=str,
        nargs=2)
    parser.add_argument("--remove-zone",
        help="Remove zone",
        metavar="domain-name",
        type=str)
    parser.add_argument("--add-record-a",
        help="Add subdomain A to a specific domain",
        metavar=("domain-name", "subdomain-name", "hosted_zone_id", "dns_name"),
        type=str,
        nargs=4)
    parser.add_argument("--remove-record-a",
        help="Remove subdomain A from a specific domain",
        metavar=("domain-name", "subdomain-name", "hosted_zone_id", "dns_name"),
        type=str,
        nargs=4)
    parser.add_argument("--add-record-a-all",
        help="Add subdomain A to all domains",
        metavar=("subdomain-name", "hosted_zone_id", "dns_name"),
        type=str,
        nargs=3)
    parser.add_argument("--remove-record-a-all",
        help="Remove subdomain A from all domains",
        metavar=("subdomain-name", "hosted_zone_id", "dns_name"),
        type=str,
        nargs=3)

    args = parser.parse_args()

    try:
        if args.list_zones: # List zones
            __prettyprinter__.pprint(awsroute53helper.get_hosted_zones())
        elif args.zone_id: # Get zone id
            __prettyprinter__.pprint(awsroute53helper.get_hosted_zone_id(args.zone_id))
        elif args.create_zone: # Create zone
            awsroute53helper.create_zone(args.create_zone[0], args.create_zone[1])
        elif args.remove_zone: # Delete zone
            answer = raw_input('Delete %s are you sure? (y/N) ' % (args.remove_zone))
            if answer == 'y':
                awsroute53helper.delete_zone(args.remove_zone)
        elif args.add_record_a: # Add subdomain
            awsroute53helper.add_record_a(args.add_record_a[0], 
                args.add_record_a[1],
                args.add_record_a[2],
                args.add_record_a[3])
        elif args.remove_record_a: # Remove subdomain
            awsroute53helper.remove_record_a(args.remove_record_a[0], 
                args.remove_record_a[1],
                args.remove_record_a[2],
                args.remove_record_a[3])
        elif args.add_record_a_all: # Add subdomain
            awsroute53helper.add_record_a_all(args.add_record_a_all[0], 
                args.add_record_a_all[1],
                args.add_record_a_all[2])
        elif args.remove_record_a_all: # Remove subdomain
            awsroute53helper.remove_record_a_all(args.remove_record_a_all[0], 
                args.remove_record_a_all[1],
                args.remove_record_a_all[2])
        else:
            parser.print_help()
    except ValueError, value_error:
        print value_error



