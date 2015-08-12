"""
	Main
"""
import pprint
from lib import awsroute53helper
import argparse

# def main(params):
if __name__ == '__main__':

    __prettyprinter__ = pprint.PrettyPrinter(indent=4)


    PARSER = argparse.ArgumentParser(description="AWS Helpers")
    PARSER.usage = 'bin/awshelpers'
    PARSER.add_argument("--list-zones",
        help="List hosted zones",
        action="store_true")
    PARSER.add_argument("--zone-id",
        help="Get zone id",
        metavar="domain-name",
        type=str)
    PARSER.add_argument("--create-zone",
        help="Create zone with the given domain-name and \
            the values specified in settings file under the domain-type block",
        metavar=("domain-name", "domain-type"),
        type=str,
        nargs=2)
    PARSER.add_argument("--remove-zone",
        help="Remove zone",
        metavar="domain-name",
        type=str)
    PARSER.add_argument("--add-record-a",
        help="Add subdomain A to a specific domain",
        metavar=("domain-name", "subdomain-name", "hosted_zone_id", "dns_name"),
        type=str,
        nargs=4)
    PARSER.add_argument("--remove-record-a",
        help="Remove subdomain A from a specific domain",
        metavar=("domain-name", "subdomain-name", "hosted_zone_id", "dns_name"),
        type=str,
        nargs=4)
    PARSER.add_argument("--add-record-a-all",
        help="Add subdomain A to all domains",
        metavar=("subdomain-name", "hosted_zone_id", "dns_name"),
        type=str,
        nargs=3)
    PARSER.add_argument("--remove-record-a-all",
        help="Remove subdomain A from all domains",
        metavar=("subdomain-name", "hosted_zone_id", "dns_name"),
        type=str,
        nargs=3)
    PARSER.add_argument("--check-settings-file",
        help="Check the settings file",
        metavar=("settings file"),
        type=str,
        nargs=1)

    ARGS = PARSER.parse_args()

    try:
        if ARGS.list_zones: # List zones
            __prettyprinter__.pprint(awsroute53helper.get_hosted_zones())
        elif ARGS.zone_id: # Get zone id
            __prettyprinter__.pprint(awsroute53helper.get_hosted_zone_id(ARGS.zone_id))
        elif ARGS.create_zone: # Create zone
            awsroute53helper.create_zone(ARGS.create_zone[0], ARGS.create_zone[1])
        elif ARGS.remove_zone: # Delete zone
            ANSWER = raw_input('Delete %s are you sure? (y/N) ' % (ARGS.remove_zone))
            if ANSWER == 'y':
                awsroute53helper.delete_zone(ARGS.remove_zone)
        elif ARGS.add_record_a: # Add subdomain
            awsroute53helper.add_record_a(ARGS.add_record_a[0],
                ARGS.add_record_a[1],
                ARGS.add_record_a[2],
                ARGS.add_record_a[3])
        elif ARGS.remove_record_a: # Remove subdomain
            awsroute53helper.remove_record_a(ARGS.remove_record_a[0],
                ARGS.remove_record_a[1],
                ARGS.remove_record_a[2],
                ARGS.remove_record_a[3])
        elif ARGS.add_record_a_all: # Add subdomain
            awsroute53helper.add_record_a_all(ARGS.add_record_a_all[0],
                ARGS.add_record_a_all[1],
                ARGS.add_record_a_all[2])
        elif ARGS.remove_record_a_all: # Remove subdomain
            awsroute53helper.remove_record_a_all(ARGS.remove_record_a_all[0],
                ARGS.remove_record_a_all[1],
                ARGS.remove_record_a_all[2])
        elif ARGS.check_settings_file:
            awsroute53helper.check_settings_file(ARGS.check_settings_file[0])
        else:
            PARSER.print_help()
    except ValueError, value_error:
        print value_error



