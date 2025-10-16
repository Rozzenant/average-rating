import argparse
from tabulate import tabulate
from utils import read_csv_files
from reports.average_rating import AverageRatingReport

REPORTS = {"average-rating": AverageRatingReport}


def main():
    parser = argparse.ArgumentParser(description="Brand reports generator")
    parser.add_argument(
        "--files", nargs="+", required=True, help="CSV files with product data"
    )
    parser.add_argument(
        "--report", required=True, help="Report name (e.g., average-rating)"
    )
    args = parser.parse_args()

    if args.report not in REPORTS:
        print(f"Unknown report: {args.report}")
        return

    data = read_csv_files(args.files)
    report_class = REPORTS[args.report]()
    result = report_class.generate(data)

    print(tabulate(result, headers=["Brand", "Average Rating"], tablefmt="github"))


if __name__ == "__main__":
    main()
