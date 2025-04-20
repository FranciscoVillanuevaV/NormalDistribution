"""navbar"""
from dash import Input, Output, clientside_callback
import dash_bootstrap_components as dbc

#from dash_bootstrap_templates import ThemeSwitchAIO

#dbc.NavItem(dbc.NavLink(theme_switch))"""
# theme_switch = ThemeSwitchAIO(
#     aio_id="theme", themes=[dbc.themes.COSMO, dbc.themes.DARKLY]
# )

color_mode_switch = [
    dbc.Label(className="fa fa-moon", html_for="switch-theme"),
    dbc.Switch( id="switch-theme", value=True, className="d-inline-block ms-1", persistence=True),
    dbc.Label(className="fa fa-sun", html_for="switch-theme"),
]

clientside_callback(
    """
    (switchOn) => {
       document.documentElement.setAttribute('data-bs-theme', switchOn ? 'light' : 'dark');  
       return window.dash_clientside.no_update
    }
    """,
    Output("switch-theme", "id"),
    Input("switch-theme", "value"),
)

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Sinopsis", href="/about")),
        dbc.NavItem(dbc.NavLink("Interpolación", href="/interpolation")),
        dbc.NavItem(dbc.NavLink("Simpson 1/3", href="/simpson")),
        dbc.NavItem(dbc.NavLink("Referencias", href="/reference")),
        dbc.NavItem(dbc.NavLink(color_mode_switch))
    ],
    brand="Probabilidad Gaussiana",
    brand_href="/",
    color="secondary",
    dark=True,
    fluid=True,
    class_name="navbar-expand-lg sticky-top"
)


def get_navbar():
    """get navbar"""
    return navbar
