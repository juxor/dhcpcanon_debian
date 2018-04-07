dhcpcanon - DHCP anonymity profile
==================================

|PyPI| |Build Status| |Coverage Status| |Documentation status| |CII Best
Practices|

DHCP client disclosing less identifying information.

Python implementation of the DHCP Anonymity Profile
(`RFC7844 <https://tools.ietf.org/html/rfc7844>`__) designed for users
that wish to remain anonymous to the visited network minimizing
disclosure of identifying information.

Technologies
------------

This implementation uses the Python `Scapy
Automata <https://www.secdev.org/projects/scapy/doc/advanced_usage.html#automata>`__

What is the Anonymity Profile?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As the RFC7844 stats:

    Some DHCP options carry unique identifiers. These identifiers can
    enable device tracking even if the device administrator takes care
    of randomizing other potential identifications like link-layer
    addresses or IPv6 addresses. The anonymity profiles are designed for
    clients that wish to remain anonymous to the visited network. The
    profiles provide guidelines on the composition of DHCP or DHCPv6
    messages, designed to minimize disclosure of identifying
    information.

What is DHCP?
~~~~~~~~~~~~~

From `Wikipedia <https://en.wikipedia.org/wiki/DHCP>`__:

    The **Dynamic Host Configuration Protocol** (**DHCP**) is a
    standardized `network
    protocol <https://en.wikipedia.org/wiki/Network_protocol>`__ used on
    `Internet
    Protocol <https://en.wikipedia.org/wiki/Internet_Protocol>`__ (IP)
    networks. The DHCP is controlled by a DHCP server that dynamically
    distributes network configuration parameters, such as `IP
    addresses <https://en.wikipedia.org/wiki/IP_address>`__, for
    interfaces and services. A
    `router <https://en.wikipedia.org/wiki/Router_%28computing%29>`__ or
    a `residential
    gateway <https://en.wikipedia.org/wiki/Residential_gateway>`__ can
    be enabled to act as a DHCP server. A DHCP server enables computers
    to request IP addresses and networking parameters automatically,
    reducing the need for a `network
    administrator <https://en.wikipedia.org/wiki/Network_administrator>`__
    or a user to configure these settings manually. In the absence of a
    DHCP server, each computer or other device (eg., a printer) on the
    network needs to be statically (ie., manually) assigned to an IP
    address.

Documentation
-------------

A more extensive online documentation is available in `Read the
docs <https://dhcpcanon.readthedocs.io/>`__. The documentation source is
in `this repository <docs/source/>`__.

Visit `DHCPAP <https://github.com/dhcpap>`__ for an overview of all the
repositories related to the RFC7844 implementation work.

Installation
------------

See `Installation <docs/source/install.rst>`__ and
`Running <docs/source/running.rst>`__

Download
--------

You can download this project in either
`zip <http://github.com/juga0/dhcpcanon/zipball/master()>`__ or
`tar <http://github.com/juga0/dhcpcanon/tarball/master>`__ formats.

You can also clone the project with Git by running:

::

    git clone https://github.com/juga0/dhcpcanon

Bugs and features
-----------------

If you wish to signal a bug or report a feature request, please fill-in
an issue on the `dhcpcanon issue
tracker <https://github.com/juga0/dhcpcanon/issues>`__.

Current status
--------------

WIP, still not recommended for end users. Testers welcomed.

See `TODO <./docs/source/todo.rst>`__

License
-------

``dhcpcanon`` is copyright 2016-2018 by juga ( juga at riseup dot net)
and is licensed by the terms of the MIT license.

Acknowledgments
---------------

To all the persons that have given suggestions and comments about this
implementation, the authors of the `RFC
7844 <https://tools.ietf.org/html/rfc7844>`__, the `Prototype Fund
Project <https://prototypefund.de>`__ of the `Open Knowledge Foundation
Germany <https://okfn.de/>`__ and the `Federal Ministry of Education and
Research <https://www.bmbf.de/>`__ who partially funds this work.

.. |PyPI| image:: https://img.shields.io/pypi/v/dhcpcanon.svg
   :target: https://pypi.python.org/pypi/dhcpcanon
.. |Build Status| image:: https://www.travis-ci.org/juga0/dhcpcanon.svg?branch=master
   :target: https://www.travis-ci.org/juga0/dhcpcanon
.. |Coverage Status| image:: https://coveralls.io/repos/github/juga0/dhcpcanon/badge.svg?branch=master
   :target: https://coveralls.io/github/juga0/dhcpcanon?branch=master
.. |Documentation Status| image:: https://readthedocs.org/projects/dhcpcanon/badge/?version=latest
  :target: http://dhcpcanon.readthedocs.io/en/latest/?badge=latest
.. |CII Best Practices| image:: https://bestpractices.coreinfrastructure.org/projects/1020/badge
   :target: https://bestpractices.coreinfrastructure.org/projects/1020
