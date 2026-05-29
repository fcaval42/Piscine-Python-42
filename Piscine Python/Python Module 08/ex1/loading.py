# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  loading.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/26 13:11:06 by fcaval          #+#    #+#               #
#  Updated: 2026/03/02 15:59:31 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def main() -> None:
    try:
        print("\n" + "LOADING STATUS: Loading programs..." + "\n")

    #     Check dependencies     #

        print("Checking dependencies:")
        import pandas as panda
        print(f"[OK] pandas ({panda.__version__}) - Data manipulation ready")
        import requests as request
        print(f"[OK] requests ({request.__version__}) - Network access ready")
        import matplotlib as plt
        print(f"[OK] matplotlib ({plt.__version__}) - Visualization ready")
        import matplotlib.pyplot as pltp
        import numpy as np
        print()

    #   Simulation Matrix    #

        print("Analyzing Matrix data...")
        print("Processing 1000 data points...")
        raw_data = np.random.randn(1000)
        df = panda.DataFrame(raw_data, columns=['Matrix_Value'])

    #    Matplotlib    #

        print("Generating visualization...")
        pltp.plot(df['Matrix_Value'])
        pltp.title("Matrix Analysis")
        pltp.savefig("matrix_analysis.png")
        print()
        print(df.describe())

        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")

    except (ImportError, AttributeError) as e:
        print(f"Error: {e}")
        print("Missing dependencies. Please try:")
        print("  $> pip install -r requirements.txt")
        print("  OR")
        print("  $> poetry install")
        print("  $> poetry run python loading.py")


if __name__ == "__main__":
    main()
