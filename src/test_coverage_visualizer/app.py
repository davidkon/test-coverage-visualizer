# src/test_coverage_visualizer/app.py
from coverage import Coverage


def main():
    cov = Coverage()
    cov.load()
    report = cov.get_data()

    for filename in report.measured_files():
        print(f"\n{filename}")
        executed = report.lines(filename)
        print(f"  Executed lines: {executed}")


if __name__ == "__main__":
    main()
