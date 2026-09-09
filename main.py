import flet as ft
from team_profiles import get_initial_team, build_profile_card


def main(page: ft.Page):
    page.title = "Team Profiles - CCCS 106"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    page.add(
        ft.Text("Project Development Team", size=24, weight=ft.FontWeight.BOLD),
        ft.Divider(),
    )

    team_members = get_initial_team()
    for member in team_members:
        page.add(build_profile_card(member))


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)