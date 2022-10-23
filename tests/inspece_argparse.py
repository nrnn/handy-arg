import argparse
import sys

#sys.argv.append("--help")
ap = argparse.ArgumentParser("Demo")

ap.add_argument("hello", )
print("="*10)
ap.print_help()
print("="*20)
help_str = ap.format_help()
print(help_str)
print("="*30)

# ap.exit(status=0, message="Force exit!!!")
# import sys
# sys.exit(0)

ap.parse_known_args()
print("Done.")
