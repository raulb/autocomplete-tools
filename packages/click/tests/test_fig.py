from importlib.metadata import requires
import pytest
from click_complete_fig import fig
import click
  
@pytest.fixture
def large_spec():
    return '''
// Autogenerated by click_complete_fig
const completionSpec: Fig.Spec = {
  "name": "fig",
  "options": [
    {
      "name": [
        "-r",
        "--root-option"
      ],
      "description": "Root option"
    },
    {
      "name": [
        "--help"
      ],
      "description": "Show this message and exit."
    }
  ],
  "args": [
    {
      "name": "choice",
      "suggestions": [
        "A",
        "B"
      ]
    }
  ],
  "subcommands": [
    {
      "name": "command",
      "description": "Debug fig",
      "deprecated": true,
      "hidden": true,
      "options": [
        {
          "name": [
            "--help"
          ],
          "description": "Show this message and exit."
        }
      ]
    },
    {
      "name": "command-with-args",
      "options": [
        {
          "name": [
            "--help"
          ],
          "description": "Show this message and exit."
        }
      ],
      "args": [
        {
          "name": "text",
          "isVariadic": true
        },
        {
          "name": "text"
        },
        {
          "name": "text"
        },
        {
          "name": "filename",
          "template": "filepaths"
        },
        {
          "name": "text"
        },
        {
          "name": "integer"
        },
        {
          "name": "path",
          "template": [
            "folders",
            "filepaths"
          ],
          "suggestCurrentToken": true
        },
        {
          "name": "path",
          "template": [
            "folders",
            "filepaths"
          ]
        }
      ]
    },
    {
      "name": "command-with-options",
      "options": [
        {
          "name": [
            "-s",
            "--string-to-echo"
          ],
          "args": [
            {
              "name": "text"
            }
          ]
        },
        {
          "name": [
            "--multiple"
          ],
          "isRepeatable": true
        },
        {
          "name": [
            "-r"
          ],
          "description": "Deprecated and required option",
          "isRequired": true
        },
        {
          "name": [
            "-c"
          ],
          "args": [
            {
              "name": "choice",
              "suggestions": [
                "A",
                "B"
              ]
            }
          ]
        },
        {
          "name": [
            "--arg-repeatable"
          ],
          "args": [
            {
              "name": "text"
            },
            {
              "name": "text"
            }
          ]
        },
        {
          "name": [
            "--shout"
          ],
          "exclusiveOn": [
            "--no-shout"
          ]
        },
        {
          "name": [
            "--no-shout"
          ],
          "exclusiveOn": [
            "--shout"
          ]
        },
        {
          "name": [
            "--help"
          ],
          "description": "Show this message and exit."
        }
      ]
    },
    {
      "name": "nested-command",
      "description": "Nested",
      "options": [
        {
          "name": [
            "--help"
          ],
          "description": "Show this message and exit."
        }
      ],
      "subcommands": [
        {
          "name": "double-nested-command",
          "description": "Double nested command",
          "options": [
            {
              "name": [
                "--help"
              ],
              "description": "Show this message and exit."
            }
          ],
          "args": [
            {
              "name": "text"
            }
          ]
        }
      ]
    }
  ]
}

export default completionSpec;
'''

### CLI Definition
@click.group("fig")
@click.option('-r', '--root-option', help="Root option", is_flag=True)
@click.argument("choices", type=click.Choice(['A', 'B']))
def cli():
    pass

@cli.command("command", help="Debug fig", short_help="Debug", deprecated=True, hidden=True)
def cmd():
    pass

@cli.group("nested-command", short_help="Nested")
def nested_command():
    pass

@nested_command.command("double-nested-command", help="Double nested command")
@click.argument("string")
def double_nested_command():
    pass

@cli.command("command-with-options")
@click.option('-s', '--string-to-echo')
@click.option('--multiple', multiple=True, is_flag=True)
@click.option('-r', required=True, help="Deprecated and required option", is_flag=True)
@click.option('-c', type=click.Choice(['A', 'B']))
@click.option('--arg-repeatable', nargs=2)
@click.option('--shout/--no-shout', default=False)
def command_with_options():
    pass

@cli.command("command-with-args")
@click.argument('string', nargs=-1)
@click.argument('int', nargs=2)
@click.argument('filename', type=click.File())
@click.argument('filename', type=click.Tuple([str, int]))
@click.argument('filename', type=click.Path(dir_okay=True, file_okay=True))
@click.argument('filename', type=click.Path(dir_okay=True, file_okay=True, exists=True))
def command_with_args():
    pass

### Test case
def test_large_spec(large_spec):
    assert fig.generate_completion_spec(cli) == large_spec
