import click


@click.command()
# basic option
@click.option('--name', '-n', default='Jonathan', help='Firstname Description')
# multiplr values
@click.option('--salary', '-s', nargs=2, help='Your Monthly Salary')
def main(name, salary):
    print("Hello World My name is {}, my salary is {}".format(name, salary))


if __name__ == "__main__":
    main()
