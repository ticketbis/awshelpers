"""
	Main
"""
import pprint
from lib import awsroute53helper
import argparse

if __name__ == '__main__':

    __prettyprinter__ = pprint.PrettyPrinter(indent=4)


    parser = argparse.ArgumentParser(description="AWS Helpers")
    parser.usage = 'bin/awshelpers'
    parser.add_argument("-l",
        "--list-zones",
        help="List hosted zones",
        action="store_true")
    parser.add_argument("-zid",
        "--zone-id",
        help="Get zone id",
        metavar="domain-name",
        type=str)
    parser.add_argument("-cz",
        "--create-zone",
        help="Create zone with the given domain-name and \
            the values specified in settings file under the domain-type block",
        metavar=("domain-name", "domain-type"),
        type=str,
        nargs=2)
    parser.add_argument("-rz",
        "--remove-zone",
        help="Remove zone",
        metavar="domain-name",
        type=str)
    args = parser.parse_args()

    if args.list_zones: # List zones
        __prettyprinter__.pprint(awsroute53helper.get_hosted_zones())
    elif args.zone_id: # Get zone id
        __prettyprinter__.pprint(\
    	   awsroute53helper.get_hosted_zone_id(args.zone_id))
    elif args.create_zone: # Create zone
        awsroute53helper.create_zone(args.create_zone[0], args.create_zone[1])
    elif args.remove_zone: # Delete zone
        answer = raw_input('Delete %s are you sure? (y/N)' % (args.remove_zone))
        if answer == 'y':
            awsroute53helper.delete_zone(args.remove_zone)
    else:
        parser.print_help()



