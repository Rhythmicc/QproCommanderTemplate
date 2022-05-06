from QuickProject.Commander import Commander


app = Commander()


@app.command()
def hello(name: str):
    print(f"Hello {name}!")


if __name__ == '__main__':
    app()
