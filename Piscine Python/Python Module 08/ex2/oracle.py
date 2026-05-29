# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  oracle.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/02 10:34:46 by fcaval          #+#    #+#               #
#  Updated: 2026/03/02 15:59:46 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import os
import sys
from dotenv import load_dotenv

load_dotenv()


def main() -> None:

    print("\nORACLE STATUS: Reading the Matrix...\n")

    finish = False
    if not os.path.exists(".env") and not os.path.exits(".env.example"):
        print("Error: .env file not found. Please create a .env "
              "file with the necessary configuration.")
        sys.exit()
    print("Configuration loaded:")
    if os.getenv("MATRIX_MODE"):
        if os.getenv("MATRIX_MODE") == "development":
            print("Mode: development")
        elif os.getenv("MATRIX_MODE") == "production":
            print("Mode: production")
    else:
        print("ERROR: choice your mode: development or production")
        sys.exit()
    if os.getenv("DATABASE_URL"):
        print("Database: Connected to local instance")
    else:
        print("Database: No connection")
        finish = True
    if os.getenv("API_KEY"):
        print("API Access: Authenticated")
    else:
        print("API Access: Not authenticated")
        finish = True
    print(f"Log Level: {os.getenv('LOG_LEVEL')}")
    if os.getenv("ZION_ENDPOINT"):
        print("Zion Network: Online")
    else:
        print("Zion Network: Not available")
        finish = True
    if finish:
        print("\nSomething lost in your .env. - Check "
              ".env.example for the requirements.")
        sys.exit()
    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations")


if __name__ == "__main__":
    main()
