'''
python index.py --name nghia --age 20
python index.py --age 20 --name nghia
'''
import click

@click.command()
@click.option('--name', prompt='Your name')
@click.option('--age', default=20)

def hello(name,age):
    # """Simple program that greets NAME for a total of COUNT times."""
    # for x in range(count):
    #     click.echo('Hello %s!' % name)
    print(name, age)

# if __name__ == '__main__':
hello()