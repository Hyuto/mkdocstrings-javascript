import typer

main = typer.Typer(add_completion=False)


@main.command("setup", help="Intalling javascript dependencies")
def scrape(package_manager: str = typer.Argument("npm", help="Package Manager [npm|yarn]")) -> None:
    from .utils import setup

    setup(pm=package_manager)


@main.command("clean", help="Delete javascript dependencies")
def scrape() -> None:
    from .utils import clean

    clean()


main()
