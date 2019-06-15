import click


@click.command()
#basic option
@click.option('--name', '-n')

def main(name):
    print("Hello World My name is {}".format(name))


if __name__ == "__main__":
    main()
