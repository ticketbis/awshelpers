"""
	Main
"""
import pprint
from lib import awsroute53helper
import argparse
import settings

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.usage = 'bin/awshelpers'
    parser.add_argument("-l", "--list-zones", help="List hosted zones", action="store_true")
    parser.add_argument("-zid", "--zone-id", help="Get zone id", metavar="domain-name", type=str)
    parser.add_argument("-cz", "--create-zone", help="Create zone", metavar=("domain-name", "domain-type"), type=str, nargs=2)
    parser.add_argument("-rz", "--remove-zone", help="Remove zone", metavar="domain-name", type=str)
    args = parser.parse_args()

    __prettyprinter__ = pprint.PrettyPrinter(indent=4)

    # List zones
    if args.list_zones:
        __prettyprinter__.pprint(awsroute53helper.get_hosted_zones())

    # Get zone id
    if args.zone_id:
        __prettyprinter__.pprint(\
    	   awsroute53helper.get_hosted_zone_id(args.zone_id))

    # Create zone
    if args.create_zone:
        awsroute53helper.create_zone(args.create_zone[0], args.create_zone[1])

    # Delete zone
    if args.remove_zone:
        confirm = raw_input('Delete %s Are you sure? (y/n)' % (args.remove_zone))
        if confirm == 'y':
            awsroute53helper.delete_zone(args.remove_zone)
