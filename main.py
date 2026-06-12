import argparse

parser = argparse.ArgumentParser(
    description="BuildTrack CLI"
)

subparsers = parser.add_subparsers(dest="command")


add_manager = subparsers.add_parser(
    "add-manager"
)

add_manager.add_argument("--name")
add_manager.add_argument("--email")


list_managers = subparsers.add_parser(
    "list-managers"
)

args = parser.parse_args()


if args.command == "add-manager":

    print(
        f"Manager {args.name} created."
    )

elif args.command == "list-managers":

    print(
        "Listing managers..."
    )