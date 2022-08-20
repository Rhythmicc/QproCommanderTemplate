# QproCommanderTemplate

## Install

```sh
pip3 install Qpro -U
# clone this project
git clone <your url>
cd QproCommanderTemplate
# register as Global Command
Qpro register-global
```

## Usage

get help: `QproCommanderTemplate --help`

### SubCommands

| Command  | Demo                           | Description        |
| -------- | ------------------------------ | ------------------ |
| hello | `QproCommanderTemplate hello <who>` | say hello to \<who> |

### Call registered function

```python
app.real_call('<function name>', *args, **kwargs)
```

## How to Register as Global Command

1. Set `QproGlobalDir` in your environment variable, such as `/home/<user>/.local/QproGlobalDir`
2. Register this project to global: `Qpro register-global`
3. Generate Fig completion script: `Qpro gen-fig-script`
4. Generate zsh completion script: `Qpro gen-zsh-comp`

## Other Cautions

None
