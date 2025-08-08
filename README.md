## Zen - Digital Logger-like Diary

Zen is a CLI tool that I made for myself. It's basically a digital diary in a log style.

### Installing...

Just clone the repo and install zen.

```bash
cd zen
pip install .
```

> On Linux, you might need to create a venv since most distros don't allow user packages to infect system libs.

### Basic Usage

Create a domain. For your first time running this, it will also do set everything up.
```bash
zen domain --create me
```

Create a log in a specific domain.
```bash
zen log "Hello!" --domain me
```

Read the log of a specific date.
```bash
zen read 2025/7/4 --domain me
```

Typing **--domain name** again and again is annoying if you have only one domain. Set a default domain!
```bash
zen settings --set default_domain me
```
Now this will automatically log into **me**.
```bash
zen log "Hello!"
```
