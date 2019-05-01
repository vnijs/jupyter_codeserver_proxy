# Code Server

http://coder.com is a port of microsoft VScode to the browser

This package is a plugin for `jupyter-server-proxy` <https://jupyter-server-proxy.readthedocs.io/>
that lets you run an instance of code-server alongside your notebook, for example,
in a JupyterHub / Binder environment. This fork is a (slightly) modified version of the plugin
developed by Dirk Grunwald (@dirkcgrunwald on GitHub)

# Installing code-server

```
RUN	cd /opt && \
	mkdir /opt/code-server && \
	cd /opt/code-server && \
	wget -qO- https://github.com/codercom/code-server/releases/download/1.939-vsc1.33.1/code-server-1.939-vsc1.33.1-linux-x64.tar.gz | tar zxvf - --strip-components=1

ENV	PATH=/opt/code-server:$PATH
```
