.. image:: https://badges.gitter.im/xonsh/xonsh.svg
   :alt: Join the chat at https://gitter.im/xonsh/xonsh
   :target: https://gitter.im/xonsh/xonsh?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. image:: https://img.shields.io/badge/%23xonsh%3Afeneas.org-Matrix-green
   :alt: Matrix room: #xonsh:feneas.org
   :target: https://matrix.to/#/#xonsh:feneas.org

.. image:: https://travis-ci.org/xonsh/xonsh.svg?branch=master
    :target: https://travis-ci.org/xonsh/xonsh

.. image:: https://ci.appveyor.com/api/projects/status/github/xonsh/xonsh?svg=true
    :target: https://ci.appveyor.com/project/xonsh/xonsh

.. image:: https://circleci.com/gh/xonsh/xonsh.svg?style=shield
    :target: https://circleci.com/gh/xonsh/xonsh

.. image:: https://codecov.io/gh/xonsh/xonsh/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/xonsh/xonsh

xonsh — Python-powered shell
============================

**xonsh** (pronounced *conch*) is a Python-powered, cross-platform, Unix-gazing shell language and command prompt.

If you like the idea of xonsh click ⭐ on the repo and stay tuned by watching releases.

Install
*******

**Conda:**

.. code-block:: console

    $ conda config --add channels conda-forge
    $ conda install xonsh


**PyPi:** 

.. code-block:: console

    $ pip install xonsh[full]

**Linux AppImage:** 

With AppImage you don't need to have Python installed.

.. code-block:: console

    wget https://github.com/xonsh/xonsh/releases/latest/download/xonsh-x86_64.AppImage -O xonsh
    chmod +x xonsh
    ./xonsh

Projects that use xonsh
***********************

- `gitsome <https://github.com/donnemartin/gitsome>`_: A supercharged Git/shell autocompleter with GitHub integration.
- `rever <https://regro.github.io/rever-docs/>`_: Cross-platform software release tool.
- `Regro autotick bot <https://github.com/regro/cf-scripts>`_: Regro Conda-Forge autoticker.
- `xxh <https://github.com/xxh/xxh>`_: Using xonsh wherever you go through the ssh.
