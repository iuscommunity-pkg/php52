
# Optional Modules
#
# Additional modules are configured to build here.  To skip a module
# remove the definition (setting it to 0 will not work):
#
# _with_module          1 
#
#
# Or you can specify at command line:
#
# --with module
# 

%define _with_mssql     1
%define _with_mcrypt    1
%define _with_tidy      1
%define _with_mhash     1

# need to get these package deps into EPEL
#%%define _with_oci8    1

%define with_mssql 0%{?_with_mssql:1}
%define with_mhash 0%{?_with_mhash:1}
%define with_mcrypt 0%{?_with_mcrypt:1}
%define with_t1lib 0%{?_with_t1lib:1}
%define with_tidy 0%{?_with_tidy:1}
%define with_pear 0%{?_with_pear:1}
%define with_oci8 0%{?_with_oci8:1}


%define contentdir /var/www
%define apiver 20041225
%define zendver 20060613
%define pdover 20060511
%define instantclient_ver 10.2.0.3

%define real_name php
%define name php52
%define base_ver 5.2

Summary: The PHP HTML-embedded scripting language. (PHP: Hypertext Preprocessor)
Name: %{name}
Version: 5.2.17
Release: 5.ius%{?dist}
License: The PHP License v3.01
Group: Development/Languages
Vendor: Rackspace US, Inc.
URL: http://www.php.net/

Source0: http://www.php.net/distributions/%{real_name}-%{version}.tar.gz
Source1: php.conf
Source2: php.ini
Source3: macros.php
Source4: macros.pear 

Patch1: php-5.2.4-gnusrc.patch
Patch2: php-4.3.3-install.patch
Patch3: php-5.2.4-norpath.patch
Patch4: php-4.3.2-libtool15.patch
Patch5: php-5.0.2-phpize64.patch

# Fixes for extension modules
Patch22: php-4.3.11-shutdown.patch

# Functional changes
Patch30: php-5.0.4-dlopen.patch
Patch31: php-5.2.4-easter.patch

# Fixes for tests
Patch51: php-5.0.4-tests-wddx.patch

# New Patches
Patch300: php-5.2.1-PQfreemem.patch 
Patch302: php-5.2.8-oci8-lib64.patch  
Patch310: php-5.2.10-bug47285.patch
#Patch314: php-5.2.13-bug51263.patch
#Patch315: php-5.3.2-bug51192.patch

# Security patches
Patch400: php-5.3.3-CVE-2011-4885.patch

BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: bzip2-devel, curl-devel >= 7.9, db4-devel, expat-devel
BuildRequires: gmp-devel, aspell-devel >= 0.50.0
BuildRequires: httpd-devel >= 2.0.46-1, libjpeg-devel, libpng-devel, pam-devel
BuildRequires: libstdc++-devel, openssl-devel, sqlite-devel >= 3.0.0
BuildRequires: zlib, zlib-devel, smtpdaemon, readline-devel
BuildRequires: bzip2, fileutils, file >= 3.39, perl, libtool >= 1.4.3, gcc-c++
BuildRequires: apr-devel, elfutils-libelf-devel, apr-util-devel
# Enforce Apache module ABI compatibility
Requires: httpd-mmn = %(cat %{_includedir}/httpd/.mmn || echo missing-httpd-devel)
Requires: file >= 3.39
Requires: libxslt >= 1.1.11 
#Requires: epel-release
Provides: mod_php = %{version}-%{release}
Provides: mod_%{name} = %{version}-%{release}
Provides: %{real_name} = %{version}-%{release}
Conflicts: %{real_name} < %{base_ver}
Conflicts: php51, php53
Requires: %{name}-common = %{version}-%{release}
# For backwards-compatibility, require php-cli for the time being:
Requires: %{name}-cli = %{version}-%{release}

%if %{with_t1lib}
BuildRequires: t1lib-devel
Requires: t1lib
%endif

%if 0%{?el4}
BuildRequires: pcre-devel >= 4.5
%endif

%if 0%{?el5}
Requires: libtool-ltdl
BuildRequires: libtool-ltdl-devel, e2fsprogs-devel
%endif

%description
PHP is an HTML-embedded scripting language. PHP attempts to make it
easy for developers to write dynamically generated webpages. PHP also
offers built-in database integration for several commercial and
non-commercial database management systems, so writing a
database-enabled webpage with PHP is fairly simple. The most common
use of PHP coding is probably as a replacement for CGI scripts. 

The php package contains the module which adds support for the PHP
language to Apache HTTP Server.

%package cli
Group: Development/Languages
Summary: Command-line interface for PHP
Requires: %{name}-common = %{version}-%{release}
Provides: %{real_name}-cli = %{version}-%{release}
Conflicts: %{real_name}-cli < %{base_ver}
Provides: %{name}-cgi = %{version}-%{release}, %{real_name}-cgi = %{version}-%{release}
Provides: %{name}-pcntl, %{name}-readline, %{name}-pcntl, %{name}-readline

%description cli
The php-cli package contains the command-line interface 
executing PHP scripts, /usr/bin/php, and the CGI interface.

%package common
Group: Development/Languages
Summary: Common files for PHP
Requires: %{name} = %{version}-%{release}
Provides: %{real_name}-common = %{version}-%{release}
Conflicts: %{real_name}-common < %{base_ver}
Provides: %{name}-api = %{apiver}, %{name}-zend-abi = %{zendver}
Provides: %{real_name}-api = %{apiver}, %{real_name}-zend-abi = %{zendver}
Provides: %{name}(api) = %{apiver}, %{name}(zend-abi) = %{zendver}
Provides: %{real_name}(api) = %{apiver}, %{real_name}(zend-abi) = %{zendver}

# Provides for all builtin modules for php52:
Provides: %{name}-bz2, %{name}-calendar, %{name}-ctype, %{name}-curl
Provides: %{name}-date, %{name}-exif, %{name}-ftp, %{name}-gettext
Provides: %{name}-gmp, %{name}-hash, %{name}-iconv, %{name}-libxml
Provides: %{name}-mime_magic, %{name}-openssl, %{name}-pcre, %{name}-posix
Provides: %{name}-pspell, %{name}-reflection, %{name}-session, %{name}-shmop 
Provides: %{name}-simplexml, %{name}-sockets, %{name}-spl, %{name}-sysvsem
Provides: %{name}-sysvshm, %{name}-sysvmsg, %{name}-tokenizer, %{name}-wddx
Provides: %{name}-zlib, %{name}-json, %{name}-zip

# add for php
Provides: %{real_name}-bz2, %{real_name}-calendar, %{real_name}-ctype
Provides: %{real_name}-curl, %{real_name}-date, %{real_name}-exif 
Provides: %{real_name}-ftp, %{real_name}-gettext, %{real_name}-gmp
Provides: %{real_name}-hash, %{real_name}-iconv, %{real_name}-libxml
Provides: %{real_name}-mime_magic, %{real_name}-openssl, %{real_name}-pcre, 
Provides: %{real_name}-posix, %{real_name}-pspell, %{real_name}-reflection
Provides: %{real_name}-session, %{real_name}-shmop, %{real_name}-simplexml
Provides: %{real_name}-sockets, %{real_name}-spl, %{real_name}-sysvsem
Provides: %{real_name}-sysvshm, %{real_name}-sysvmsg, %{real_name}-tokenizer
Provides: %{real_name}-wddx, %{real_name}-zlib, %{real_name}-json
Provides: %{real_name}-zip


%description common
The php-common package contains files used by both the php
package and the php-cli package.

%package devel
Group: Development/Libraries
Summary: Files needed for building PHP extensions.
Requires: %{name} = %{version}-%{release}, autoconf, automake
Provides: %{real_name}-devel = %{version}-%{release}
Conflicts: %{real_name}-devel < %{base_ver}

%description devel
The php-devel package contains the files needed for building PHP
extensions. If you need to compile your own PHP extensions, you will
need to install this package.

%if %{with_pear}
%package pear
Group: Development/Languages
Summary: PHP Extension and Application Repository Components
Requires: %{name} = %{version}-%{release}
Provides: %{real_name}-pear = %{version}-%{release}
Conflicts: %{real_name}-pear < %{base_ver}

%description pear
PEAR is a framework and distribution system for reusable PHP
components.  This package contains a set of PHP components from the
PEAR repository.
%endif

%package imap
Summary: A module for PHP applications that use IMAP.
Group: Development/Languages
Requires: %{name}-common = %{version}-%{release}
Provides: %{real_name}-imap = %{version}-%{release}
Conflicts: %{real_name}-imap < %{base_ver}
BuildRequires: krb5-devel, openssl-devel

%if 0%{?el3}
BuildRequires: imap-devel
%elseif 0%{?el4}
BuildRequires: libc-client-devel
%endif

%description imap
The php-imap package contains a dynamic shared object (DSO) for the
Apache Web server. When compiled into Apache, the php-imap module will
add IMAP (Internet Message Access Protocol) support to PHP. IMAP is a
protocol for retrieving and uploading e-mail messages on mail
servers. PHP is an HTML-embedded scripting language. If you need IMAP
support for PHP applications, you will need to install this package
and the php package.

%package ldap
Summary: A module for PHP applications that use LDAP.
Group: Development/Languages
Requires: %{name}-common = %{version}-%{release}
Provides: %{real_name}-ldap = %{version}-%{release}
Conflicts: %{real_name}-ldap < %{base_ver}
BuildRequires: cyrus-sasl-devel, openldap-devel, openssl-devel

%description ldap
The php-ldap package is a dynamic shared object (DSO) for the Apache
Web server that adds Lightweight Directory Access Protocol (LDAP)
support to PHP. LDAP is a set of protocols for accessing directory
services over the Internet. PHP is an HTML-embedded scripting
language. If you need LDAP support for PHP applications, you will
need to install this package in addition to the php package.

%package pdo
Summary: A database access abstraction module for PHP applications
Group: Development/Languages
Requires: %{name}-common = %{version}-%{release}
Provides: %{real_name}-pdo = %{version}-%{release}
Conflicts: %{real_name} < %{base_ver}
Provides: %{name}-pdo-abi = %{pdover}
Provides: %{real_name}-pdo-abi = %{pdover}

%description pdo
The php-pdo package contains a dynamic shared object that will add
a database access abstraction layer to PHP.  This module provides
a common interface for accessing MySQL, PostgreSQL or other 
databases.

%package mysql
Summary: A module for PHP applications that use MySQL databases.
Group: Development/Languages
Requires: %{name}-common = %{version}-%{release}, %{name}-pdo
Provides: %{real_name}-mysql = %{version}-%{release}
Conflicts: %{real_name}-mysql < %{base_ver}
Provides: php_database, %{name}-mysqli, %{real_name}-mysqli
%if 0%{?rhel} >= 5 
BuildRequires: mysql-devel < 5.0.91 
%endif

%if 0%{?el3} || 0%{?el4}
Requires: mysqlclient15 >= 5.0.45
BuildRequires: mysql50 mysql50-devel
%endif

%description mysql
The php-mysql package contains a dynamic shared object that will add
MySQL database support to PHP. MySQL is an object-relational database
management system. PHP is an HTML-embeddable scripting language. If
you need MySQL support for PHP applications, you will need to install
this package and the php package.

%package pgsql
Summary: A PostgreSQL database module for PHP.
Group: Development/Languages
Requires: %{name}-common = %{version}-%{release}, %{name}-pdo
Provides: %{real_name}-pgsql = %{version}-%{release}
Conflicts: %{real_name}-pgsql < %{base_ver}
Provides: php_database
BuildRequires: krb5-devel, openssl-devel, postgresql-devel

%description pgsql
The php-pgsql package includes a dynamic shared object (DSO) that can
be compiled in to the Apache Web server to add PostgreSQL database
support to PHP. PostgreSQL is an object-relational database management
system that supports almost all SQL constructs. PHP is an
HTML-embedded scripting language. If you need back-end support for
PostgreSQL, you should install this package in addition to the main
php package.

%package odbc
Group: Development/Languages
Requires: %{name}-common = %{version}-%{release}, %{name}-pdo
Provides: %{real_name}-odbc = %{version}-%{release}
Conflicts: %{real_name}-odbc < %{base_ver}
Summary: A module for PHP applications that use ODBC databases.
Provides: php_database
BuildRequires: unixODBC-devel

%description odbc
The php-odbc package contains a dynamic shared object that will add
database support through ODBC to PHP. ODBC is an open specification
which provides a consistent API for developers to use for accessing
data sources (which are often, but not always, databases). PHP is an
HTML-embeddable scripting language. If you need ODBC support for PHP
applications, you will need to install this package and the php
package.

%package soap
Group: Development/Languages
Requires: %{name}-common = %{version}-%{release}, libxml2 >= 2.6.16
Provides: %{real_name}-soap = %{version}-%{release}
Conflicts: %{real_name}-soap < %{base_ver}
Summary: A module for PHP applications that use the SOAP protocol
BuildRequires: libxml2-devel >= 2.6.16

%description soap
The php-soap package contains a dynamic shared object that will add
support to PHP for using the SOAP web services protocol.

%package snmp
Summary: A module for PHP applications that query SNMP-managed devices.
Group: Development/Languages
Requires: %{name}-common = %{version}-%{release}, net-snmp >= 5.1
Provides: %{real_name}-snmp = %{version}-%{release}
Conflicts: %{real_name}-snmp < %{base_ver}
BuildRequires: net-snmp-devel >= 5.1

%description snmp
The php-snmp package contains a dynamic shared object that will add
support for querying SNMP devices to PHP.  PHP is an HTML-embeddable
scripting language. If you need SNMP support for PHP applications, you
will need to install this package and the php package.

%package xml
Summary: A module for PHP applications which use XML
Group: Development/Languages
Requires: %{name}-common = %{version}-%{release}, libxml2 >= 2.6.16, 
Requires: libxslt >= 1.1.11
Provides: %{real_name}-xml = %{version}-%{release}
Conflicts: %{real_name}-xml < %{base_ver}
Provides: %{name}-dom, %{name}-xsl, %{name}-domxml
Provides: %{real_name}-dom, %{real_name}-xsl, %{real_name}-domxml
BuildRequires: libxslt-devel >= 1.1.11, libxml2-devel >= 2.6.16

%description xml
The php-xml package contains dynamic shared objects which add support
to PHP for manipulating XML documents using the DOM tree,
and performing XSL transformations on XML documents.

%package xmlrpc
Summary: A module for PHP applications which use the XML-RPC protocol
Group: Development/Languages
Requires: %{name}-common = %{version}-%{release}
Provides: %{name}-xmlrpc = %{version}-%{release}
Conflicts: %{real_name}-xmlrpc < %{base_ver}
BuildRequires: expat-devel

%description xmlrpc
The php-xmlrpc package contains a dynamic shared object that will add
support for the XML-RPC protocol to PHP.

%package mbstring
Summary: A module for PHP applications which need multi-byte string handling
Group: Development/Languages
Requires: %{name}-common = %{version}-%{release}
Provides: %{real_name}-mbstring = %{version}-%{release}
Conflicts: %{real_name}-mbstring < %{base_ver}

%description mbstring
The php-mbstring package contains a dynamic shared object that will add
support for multi-byte string handling to PHP.

%package ncurses
Summary: A module for PHP applications for using ncurses interfaces
Group: Development/Languages
Requires: %{name}-common = %{version}-%{release}
Provides: %{real_name}-ncurses = %{version}-%{release}
Conflicts: %{real_name}-ncurses < %{base_ver}
BuildRequires: ncurses-devel

%description ncurses
The php-ncurses package contains a dynamic shared object that will add
support for using the ncurses terminal output interfaces.

%package gd
Summary: A module for PHP applications for using the gd graphics library
Group: Development/Languages
Requires: %{name}-common = %{version}-%{release}
Provides: %{real_name}-gd = %{version}-%{release}
Conflicts: %{real_name}-gd < %{base_ver}
BuildRequires: gd-devel, freetype-devel

%description gd
The php-gd package contains a dynamic shared object that will add
support for using the gd graphics library to PHP.

%if %{with_t1lib}
This package is built against t1lib adding Postscript Type 1 font support 
to PHP/GD.
%endif

%package bcmath
Summary: A module for PHP applications for using the bcmath library
Group: Development/Languages
Requires: %{name}-common = %{version}-%{release}
Provides: %{real_name}-bcmath = %{version}-%{release}
Conflicts: %{real_name}-bcmath < %{base_ver}

%description bcmath
The php-bcmath package contains a dynamic shared object that will add
support for using the bcmath library to PHP.

%package dba
Summary: A database abstraction layer module for PHP applications
Group: Development/Languages
Requires: %{name}-common = %{version}-%{release}
Provides: %{real_name}-dba = %{version}-%{release}
Conflicts: %{real_name}-dba < %{base_ver}

%description dba
The php-dba package contains a dynamic shared object that will add
support for using the DBA database abstraction layer to PHP.

%package tidy
Summary: Utility to clean up and pretty print HTML/XHTML/XML
Group: Development/Languages
Requires: %{name}-common = %{version}-%{release}
Provides: %{real_name}-tidy = %{version}-%{release}
Conflicts: %{real_name}-tidy < %{base_ver}
Requires: libtidy
BuildRequires: libtidy, libtidy-devel

%description tidy
The php-tidy package contains a dynamic shared object that will add
support for using libtidy to PHP.

# Conditional Module Support
%if %{with_mcrypt}
%package mcrypt
Summary: A module for PHP applications that use Mcrypt.
Group: Development/Languages
Requires: %{name}-common = %{version}-%{release}, libmcrypt
Provides: %{real_name}-mcrypt = %{version}-%{release}
Conflicts: %{real_name}-mcrypt < %{base_ver}
BuildRequires: libmcrypt-devel

%description mcrypt
The php-mcrypt package is a dynamic shared object (DSO) for the Apache
Web server that adds Mcrypt support to PHP.
%endif

%if %{with_mhash}
%package mhash
Summary: A module for PHP applications that use Mhash.
Group: Development/Languages
Requires: %{name}-common = %{version}-%{release}, mhash
Provides: %{real_name}-mhash = %{version}-%{release}
Conflicts: %{real_name}-mhash < %{base_ver}
BuildRequires: mhash, mhash-devel

%description mhash
The php-hash package is a dynamic shared object (DSO) for the Apache
Web server that adds Mhash support to PHP.
%endif

%if %{with_mssql}
%package mssql
Summary: A module for PHP applications that use MSSQL databases.
Group: Development/Languages
Requires: %{name}-common = %{version}-%{release}, freetds >= 0.64
Provides: %{real_name}-mssql = %{version}-%{release}
Conflicts: %{real_name}-mssql < %{base_ver}
Provides: php_database
BuildRequires: freetds-devel >= 0.64

%description mssql
The mssql package contains a dynamic shared object that will add
support for accessing MSSQL databases to PHP.
%endif

%if %{with_oci8}
%package oci8
Summary: A module for PHP applications that connect to Oracle.
Group: Development/Languages
Requires: %{name}-common = %{version}-%{release}
Provides: %{real_name}-oci8 = %{version}-%{release}
Conflicts: %{real_name}-oci8 < %{base_ver}
Requires: oracle-instantclient-basic >= %{instantclient_ver}
BuildRequires: oracle-instantclient-basic >= %{instantclient_ver}
BuildRequires: oracle-instantclient-devel >= %{instantclient_ver}

%description oci8 
The php-oci8 package is a dynamic shared object (DSO) for the Apache
Web server that adds Oracle support to PHP.
%endif


%prep
%setup -q -n %{real_name}-%{version} 

%patch1 -p1 -b .gnusrc
%patch2 -p1 -b .install
%patch3 -p1 -b .norpath
%patch4 -p1 -b .libtool15
%patch5 -p1 -b .phpize64
#%patch6 -p1 -b .curl716
#%patch7 -p1 -b .filterm4

%patch22 -p1 -b .shutdown

%patch30 -p1 -b .dlopen
%patch31 -p1 -b .easter

%patch51 -p1 -b .tests-wddx
%patch300 -p1 -b .PQfreemem
%patch302 -p1 -b .oci8-lib64
%patch310 -p1 -b .bug47285
#%%patch314 -p1 -b .bug51263 
#%%patch315 -p1 -b .bug51192

# Security patches
%patch400 -p1 -b .cve-2011-4885

# Prevent %%doc confusion over LICENSE files
cp Zend/LICENSE Zend/ZEND_LICENSE
cp TSRM/LICENSE TSRM_LICENSE
cp regex/COPYRIGHT regex_COPYRIGHT
cp ext/gd/libgd/README gd_README

# Source is built twice: once for /usr/bin/php, once for the Apache DSO.
mkdir build-cgi build-apache

# Remove bogus test; position of read position after fopen(, "a+")
# is not defined by C standard, so don't presume anything.
rm -f ext/standard/tests/file/bug21131.phpt

# Tests that fail.
rm -f ext/standard/tests/file/bug22414.phpt \
      ext/iconv/tests/bug16069.phpt

# Safety check for API version change.
vapi=`sed -n '/#define PHP_API_VERSION/{s/.* //;p}' main/php.h`
if test "x${vapi}" != "x%{apiver}"; then
   : Error: Upstream API version is now ${vapi}, expecting %{apiver}.
   : Update the apiver macro and rebuild.
   exit 1
fi

vzend=`sed -n '/#define ZEND_MODULE_API_NO/{s/^[^0-9]*//;p;}' Zend/zend_modules.h`
if test "x${vzend}" != "x%{zendver}"; then
   : Error: Upstream Zend ABI version is now ${vzend}, expecting %{zendver}.
   : Update the zendver macro and rebuild.
   exit 1
fi

# Safety check for PDO ABI version change
vpdo=`sed -n '/#define PDO_DRIVER_API/{s/.*[	]//;p}' ext/pdo/php_pdo_driver.h`
if test "x${vpdo}" != "x%{pdover}"; then
   : Error: Upstream PDO ABI version is now ${vpdo}, expecting %{pdover}.
   : Update the pdover macro and rebuild.
   exit 1
fi


%build
# Force use of system libtool:
libtoolize --force --copy
cat `aclocal --print-ac-dir`/libtool.m4 > build/libtool.m4

# Regenerate configure scripts (patches change config.m4's)
./buildconf --force

CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export CFLAGS

# Install extension modules in %{_libdir}/php/modules.
EXTENSION_DIR=%{_libdir}/php/modules; export EXTENSION_DIR

# Set PEAR_INSTALLDIR to ensure that the hard-coded include_path
# includes the PEAR directory even though pear is packaged
# separately.
PEAR_INSTALLDIR=%{_datadir}/pear; export PEAR_INSTALLDIR

# Shell function to configure and build a PHP tree.
build() {
# bison-1.875-2 seems to produce a broken parser; workaround.
mkdir Zend && cp ../Zend/zend_{language,ini}_{parser,scanner}.[ch] Zend
ln -sf ../configure
%configure \
    --cache-file=../config.cache \
        --with-libdir=%{_lib} \
    --with-config-file-path=%{_sysconfdir} \
    --with-config-file-scan-dir=%{_sysconfdir}/php.d \
    --disable-debug \
    --with-pic \
    --disable-rpath \
    %{?_with_pear:--with-pear=/usr/share/pear} \
    %{?!_with_pear:--without-pear} \
    --with-bz2 \
    --with-curl \
    --with-exec-dir=%{_bindir} \
    --with-freetype-dir=%{_prefix} \
    --with-png-dir=%{_prefix} \
    --enable-gd-native-ttf \
    --without-gdbm \
    --with-gettext \
    --with-gmp \
    --with-iconv \
    --with-jpeg-dir=%{_prefix} \
    --with-openssl \
    --with-png \
    --with-pspell \
    --with-expat-dir=%{_prefix} \
    %{?el3:--with-pcre-regex} \
    %{?el4:--with-pcre-regex} \
    --with-zlib \
    --with-zlib-dir=%{_includedir} \
    --with-layout=GNU \
    --enable-exif \
    --enable-ftp \
    --enable-magic-quotes \
    --enable-sockets \
    --enable-sysvsem --enable-sysvshm --enable-sysvmsg \
    --enable-track-vars \
    --enable-trans-sid \
    --enable-yp \
    --enable-wddx \
    --with-kerberos \
    --enable-ucd-snmp-hack \
    --with-unixODBC=shared,%{_prefix} \
    --enable-memory-limit \
    --enable-shmop \
    --enable-calendar \
    --enable-dbx \
    --enable-dio \
    --with-mime-magic=%{_sysconfdir}/httpd/conf/magic \
    --without-sqlite \
    --with-libxml-dir=%{_prefix} \
    --with-xml \
    %{?_with_tidy:--with-tidy=shared,%{_prefix}} \
    %{?_with_mhash:--with-mhash=shared,%{_prefix}} \
    %{?_with_mcrypt:--with-mcrypt=shared,%{_prefix}} \
    %{?_with_mssql:--with-mssql=shared,%{_prefix}} \
    %{?_with_oci8:--with-oci8=shared,instantclient,%{_libdir}/oracle/%{instantclient_ver}/client/lib} \
    %{?_with_t1lib:--with-t1lib} \
    $* 
if test $? != 0; then 
  tail -500 config.log
  : configure failed
  exit 1
fi

make %{?_smp_mflags}
}

# Build /usr/bin/php-cgi with the CGI SAPI, and all the shared extensions
pushd build-cgi
build --enable-force-cgi-redirect \
      --enable-pcntl \
      --with-imap=shared --with-imap-ssl \
      --enable-mbstring=shared --enable-mbstr-enc-trans \
      --enable-mbregex \
      --with-ncurses=shared \
      --with-gd=shared \
      --enable-bcmath=shared \
      --enable-dba=shared --with-db4=%{_prefix} \
      --with-xmlrpc=shared \
      --with-ldap=shared \
      --with-mysql=shared,%{_prefix} \
      --with-mysqli=shared,%{_bindir}/mysql_config \
      --enable-dom=shared \
      --with-dom-xslt=%{_prefix} --with-dom-exslt=%{_prefix} \
      --with-pgsql=shared \
      --with-snmp=shared,%{_prefix} \
      --enable-soap=shared \
      --with-xsl=shared,%{_prefix} \
      --enable-xmlreader=shared --enable-xmlwriter=shared \
      --enable-fastcgi \
      --enable-pdo=shared \
      --with-pdo-odbc=shared,unixODBC,%{_prefix} \
      --with-pdo-mysql=shared,%{_prefix} \
      --with-pdo-pgsql=shared,%{_prefix} \
      --with-pdo-sqlite=shared,%{_prefix} \
      --enable-json=shared \
      --enable-zip=shared \
      --with-readline
popd

# Build Apache module, and the CLI SAPI, /usr/bin/php
pushd build-apache
build --with-apxs2=%{_sbindir}/apxs \
      --without-mysql --without-gd \
      --without-odbc --disable-dom \
      --disable-dba --without-unixODBC \
      --disable-pdo --disable-xmlreader --disable-xmlwriter \
      --disable-json
popd

%check
cd build-apache
# Run tests, using the CLI SAPI
export NO_INTERACTION=1 REPORT_EXIT_STATUS=1 MALLOC_CHECK_=2
unset TZ LANG LC_ALL
if ! make test; then
  set +x
  for f in `find .. -name \*.diff -type f -print`; do
    echo "TEST FAILURE: $f --"
    cat "$f"
    echo "-- $f result ends."
  done
  set -x
  #exit 1
fi
unset NO_INTERACTION REPORT_EXIT_STATUS MALLOC_CHECK_

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

# Install everything from the CGI SAPI build
pushd build-cgi
make install INSTALL_ROOT=$RPM_BUILD_ROOT 

# ========================================================================
# PHP install the CLI by default as of 5.2.3... the following code is deprecated
# =======================================================================
# mv $RPM_BUILD_ROOT%{_bindir}/php $RPM_BUILD_ROOT%{_bindir}/php-cgi
# Install the CLI SAPI as /usr/bin/php
# make install-cli INSTALL_ROOT=$RPM_BUILD_ROOT
popd

# Install the Apache module
pushd build-apache
make install-sapi INSTALL_ROOT=$RPM_BUILD_ROOT
popd

# Install the default configuration file and icons
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/
install -m 644 $RPM_SOURCE_DIR/php.ini $RPM_BUILD_ROOT%{_sysconfdir}/php.ini
install -m 755 -d $RPM_BUILD_ROOT%{contentdir}/icons
install -m 644    *.gif $RPM_BUILD_ROOT%{contentdir}/icons/

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rpm
# For PEAR packaging:
%if %{with_pear}
install -m 755 -d $RPM_BUILD_ROOT%{_libdir}/php/pear
install -m 644 %SOURCE4 $RPM_BUILD_ROOT%{_sysconfdir}/rpm/macros.pear
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rpm
%endif


# Use correct libdir
sed -i -e 's|%{_prefix}/lib|%{_libdir}|' $RPM_BUILD_ROOT%{_sysconfdir}/php.ini

# install the DSO
install -m 755 -d $RPM_BUILD_ROOT%{_libdir}/httpd/modules
install -m 755 build-apache/libs/libphp5.so $RPM_BUILD_ROOT%{_libdir}/httpd/modules

# Apache config fragment
install -m 755 -d $RPM_BUILD_ROOT/etc/httpd/conf.d
install -m 644 $RPM_SOURCE_DIR/php.conf $RPM_BUILD_ROOT/etc/httpd/conf.d

install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php.d
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/lib/php
install -m 700 -d $RPM_BUILD_ROOT%{_localstatedir}/lib/php/session


# Generate files lists and stub .ini files for each subpackage
for mod in pgsql mysql mysqli odbc ldap snmp xmlrpc imap \
    mbstring ncurses gd dom xsl soap bcmath dba xmlreader xmlwriter \
    pdo pdo_mysql pdo_pgsql pdo_odbc pdo_sqlite json zip \
    %{?_with_mhash:mhash} %{?_with_mcrypt:mcrypt} \
    %{?_with_mssql:mssql} %{?_with_oci8:oci8} %{?_with_tidy:tidy} ; do
    cat > $RPM_BUILD_ROOT%{_sysconfdir}/php.d/${mod}.ini <<EOF
; Enable ${mod} extension module
extension=${mod}.so
EOF
    cat > files.${mod} <<EOF
%attr(755,root,root) %{_libdir}/php/modules/${mod}.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.d/${mod}.ini
EOF
done

# The dom, xsl and xml* modules are all packaged in php-xml
cat files.dom files.xsl files.xml{reader,writer} > files.xml

# The mysql and mysqli modules are both packaged in php-mysql
cat files.mysqli >> files.mysql

# Split out the PDO modules
cat files.pdo_mysql >> files.mysql
cat files.pdo_pgsql >> files.pgsql
cat files.pdo_odbc >> files.odbc

# Package pdo_sqlite with pdo; isolating the sqlite dependency
# isn't useful at this time since rpm itself requires sqlite.
cat files.pdo_sqlite >> files.pdo

# Package json and zip in -common.
cat files.json files.zip > files.common

# Install the macros file:
install -d $RPM_BUILD_ROOT%{_sysconfdir}/rpm
sed -e "s/@PHP_APIVER@/%{apiver}/;s/@PHP_ZENDVER@/%{zendver}/;s/@PHP_PDOVER@/%{pdover}/" \
    < $RPM_SOURCE_DIR/macros.php > macros.php
install -m 644 -c macros.php \
           $RPM_BUILD_ROOT%{_sysconfdir}/rpm/macros.php

# Remove PEAR testsuite
rm -rf $RPM_BUILD_ROOT%{_datadir}/pear/tests

# Remove unpackaged files
rm -rf  $RPM_BUILD_ROOT%{_libdir}/php/modules/*.a \
        $RPM_BUILD_ROOT%{_bindir}/{phptar} \
        $RPM_BUILD_ROOT/.channels/.alias/pear.txt \
        $RPM_BUILD_ROOT/.channels/.alias/pecl.txt \
        $RPM_BUILD_ROOT/.channels/__uri.reg \
        $RPM_BUILD_ROOT/.channels/pear.php.net.reg \
        $RPM_BUILD_ROOT/.channels/pecl.php.net.reg \
        $RPM_BUILD_ROOT/.depdb \
        $RPM_BUILD_ROOT/.depdblock \
        $RPM_BUILD_ROOT/.filemap \
        $RPM_BUILD_ROOT/.lock 

# Remove irrelevant docs
rm -f README.{Zeus,QNX,CVS-RULES}

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
rm files.* macros.php


%pre common

# If PHP < 5 is installed, lets move the php.ini so we can replace it with the new one
tmp_file="/tmp/rs-rpmupgrade-`date +"%Y-%m-%d"`_current_php_version"
php -v 2> /dev/null | head -n1 | awk {' print $2 '} | awk -F . {' print $1 '} > $tmp_file 
php_cur_version=$(cat $tmp_file)
if [ "$php_cur_version" ]; then
  if [ "$php_cur_version" -lt 5 ]; then
    if [ -e /etc/php.ini ]; then
      echo -n "moving /etc/php.ini to /etc/php.ini-pre-%{version} . . . "
      %{__mv} /etc/php.ini /etc/php.ini-pre-%{version}
      [ "$?" == "0" ] && echo "ok" || echo "failed"
    fi
  fi
fi

%post common

# If PHP < 5 was installed prio to upgrade, we need to copy php.ini.rpmnew to php.ini
tmp_file="/tmp/rs-rpmupgrade-`date +"%Y-%m-%d"`_current_php_version"
php_cur_version=$(cat $tmp_file)
if [ "$php_cur_version" ]; then
  if [ "$php_cur_version" -lt 5 ]; then
    echo -n "copying php.ini.rpmnew to /etc/php.ini . . . "
    %{__cp} /etc/php.ini.rpmnew /etc/php.ini
    [ "$?" == "0" ] && echo "ok" || echo "failed"
  fi
fi


%files
%defattr(-,root,root)
%{_libdir}/httpd/modules/libphp5.so
%attr(0770,root,apache) %dir %{_localstatedir}/lib/php/session
%config %{_sysconfdir}/httpd/conf.d/php.conf
%{contentdir}/icons/php.gif

%files common -f files.common
%defattr(-,root,root)
%doc CODING_STANDARDS CREDITS EXTENSIONS INSTALL LICENSE NEWS README*
%doc Zend/ZEND_* gd_README TSRM_LICENSE regex_COPYRIGHT
%config(noreplace) %{_sysconfdir}/php.ini
%dir %{_sysconfdir}/php.d
%dir %{_libdir}/php
%dir %{_libdir}/php/modules
%dir %{_localstatedir}/lib/php

%files cli
%defattr(-,root,root)
%{_bindir}/php
%{_bindir}/php-cgi
%{_mandir}/man1/php.1*
%{_bindir}/phpize
%{_mandir}/man1/phpize.1*

%files devel
%defattr(-,root,root)
%{_bindir}/php-config
%{_includedir}/php
%{_libdir}/php/build
%{_mandir}/man1/php-config.1*
%config %{_sysconfdir}/rpm/macros.php

%if %{with_pear}
%files pear
%defattr(-,root,root)
%{_bindir}/pear
%{_datadir}/pear
%{_bindir}/pecl
%{_bindir}/peardev
%config %{_sysconfdir}/rpm/macros.pear
%config %{_sysconfdir}/pear.conf
%dir %{_libdir}/php/pear
%endif

%files pgsql -f files.pgsql
%files mysql -f files.mysql
%files odbc -f files.odbc
%files imap -f files.imap
%files ldap -f files.ldap
%files snmp -f files.snmp
%files xml -f files.xml
%files xmlrpc -f files.xmlrpc
%files mbstring -f files.mbstring
%files ncurses -f files.ncurses
%files gd -f files.gd
%files soap -f files.soap
%files bcmath -f files.bcmath
%files dba -f files.dba
%files pdo -f files.pdo
%files tidy -f files.tidy

# Files for conditional Module Support
%if %{with_mhash}
%files mhash -f files.mhash
%endif

%if %{with_mcrypt}
%files mcrypt -f files.mcrypt
%endif

%if %{with_mssql}
%files mssql -f files.mssql
%endif

%if %{with_oci8}
%files oci8 -f files.oci8
%endif


%changelog
* Tue Apr 10 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 5.2.17-5.ius
- Removing old psa-comat package

* Mon Feb 13 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 5.2.17-4.ius
- Adding Patch400 to address 
  http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2011-4885

* Wed Feb 01 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 5.2.17-3.ius
- Removing 'Requires: epel-release', ius-release package requires
  epel-release so this is redundant and causes issues internally.

* Thu May 05 2011 BJ Dierkes <wdierkes@rackspace.com> - 5.2.17-2.ius
- Remove 'Requires: php52' (base package) as the -common subpackage
  does not necessarily need base... and php52-cli doesn't need the
  added deps of the base package (httpd, etc).

* Tue Jan 11 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 5.2.17-1.ius
- Latest sources from upstream.  Full changelog available at:
  http://www.php.net/ChangeLog-5.php#5.2.17

* Thu Dec 16 2010 BJ Dierkes <wdierkes@rackspace.com> - 5.2.16-1.ius
- Latest sources from upstream.  Full changelog available at:
  http://www.php.net/ChangeLog-5.php#5.2.16
  Resolves CVE-2010-4150, CVE-2010-3436, CVE-2010-3709
- Move phpize under -cli subpackage (see BZ#657812)

* Fri Jul 23 2010 BJ Dierkes <wdierkes@rackspace.com> - 5.2.14-1.ius
- Latest sources from upstream. Full changelog available at:
  http://www.php.net/ChangeLog-5.php#5.2.14
- Removed Patch314: php-5.2.13-bug51263.patch (applied upstream)
- Removed Patch315: php-5.3.2-bug51192.patch (applied upstream)

* Wed Jul 07 2010 BJ Dierkes <wdierkes@rackspace.com> - 5.2.13-6.ius
- Added -psa-compat subpackage which adds Plesk (psa) compatibility
  Resolves LP#583485.

* Tue Jun 15 2010 BJ Dierkes <wdierkes@rackspace.com> - 5.2.13-5.ius
- Add small hack to BuildRequire mysql-devel < 5.0.91 to force mock to 
  pull the stock verson of mysql-devel (el5+)
- Removed preset elX macros, changed references to 0{?elX} instead 
  (this uncovered that el4 was actually using the bundled pcre so 
  fixing that to reflect how it is actually building).

* Tue Apr 27 2010 BJ Dierkes <wdierkes@rackspace.com> - 5.2.13-4.ius
- Set enable_dl = Off in php.ini.  Resolves RS #377 (internal)
- Set error_reporting = E_ALL & ~E_NOTICE.  Resolves RS #585 (internal)

* Mon Mar 29 2010 BJ Dierkes <wdierkes@rackspace.com> - 5.2.13-3.ius
- Altered Patch315: php-5.3.2-bug51192.patch 

* Mon Mar 29 2010 BJ Dierkes <wdierkes@rackspace.com> - 5.2.13-2.ius
- Added Patch314: php-5.2.13-bug51263.patch resolves Bug 51263 imagettftext 
  and rotated text uses wrong baseline (regression).  Resolves LP #551189.
- Added Patch315: php-5.3.2-bug51192.patch resolves Bug 51192 
  FILTER_VALIDATE_URL will invalidate a hostname that includes '-'.  Resolves
  LP #548985.

* Wed Mar 03 2010 BJ Dierkes <wdierkes@rackspace.com> - 5.2.13-1.ius
- Latest sources from upstream.

* Thu Dec 17 2009 BJ Dierkes <wdierkes@rackspace.com> - 5.2.12-1.ius
- Latest sources from upstream.
- Removed Patch350: php-5.2.8-dashn.patch (applied upstream)
- Removed Patch311: php-5.2.11-bug447752.patch (applied upstream)
- Removed Patch312: php-5.2.11-bug462057.patch (applied upstream)
- Removed Patch313: php-5.2.11-error_log-bug49627.patch (applied upstream)

* Wed Nov 11 2009 BJ Dierkes <wdierkes@rackspace.com> - 5.2.11-6.ius
- Added Patch313: php-5.2.11-error_log-bug49627.patch
- Re-enable mhash subpackage. Resolves LP #480778

* Sat Oct 31 2009 BJ Dierkes <wdierkes@rackspace.com> - 5.2.11-4.ius
- Adding missing 'Conflicts' for every subpackage, conflicing with
  < base_ver of that subpackage

* Tue Oct 27 2009 BJ Dierkes <wdierkes@rackspace.com> - 5.2.11-3.ius
- Added Patch312: php-5.2.11-bug462057.patch - Resolves LaunchPad 
  Bug 462057 PHP 'posix_mkfifo()' 'open_basedir' Restriction Bypass 
  Vulnerability

* Thu Oct 22 2009 BJ Dierkes <wdierkes@rackspace.com> - 5.2.11-2.1.ius
- php52-mysql Requires: php52-common (not php-common)
- Remove Obscoletes from all subpackages.

* Sat Oct 10 2009 BJ Dierkes <wdierkes@rackspace.com> - 5.2.11-2.ius
- Only install /etc/rpm/macros.pear if building with pear.  Resolves
  LaunchPad Bug #448260.
- Added Patch311: php-5.2.11-bug447752.patch resolves LaunchPad Bug
  447752, Security Focus Bugtraq ID 36555 PHP tempname() safe_mode
  Restriction-Bypass Vulnerability

* Thu Oct 01 2009 BJ Dierkes <wdierkes@rackspace.com> - 5.2.11-1.1.ius
- Rebuilding for EL4/EL5

* Fri Sep 18 2009 BJ Dierkes <wdierkes@rackspace.com> - 5.2.11-1.ius
- Latest sources from upstream
- Removed Patch303: php-5.2.10-imap_bug48619.patch (applied upstream)
- Removed Patch309: php-5.2.10-bug47351.patch (applied upstream)

* Thu Sep 03 2009 BJ Dierkes <wdierkes@rackspace.com> - 5.2.10-4.ius
- MySQL subpackage provides php-mysql

* Thu Aug 06 2009 BJ Dierkes <wdierkes@rackspace.com> - 5.2.10-3.ius
- BuildRequires: mysql50 mysql50-devel for el4

* Fri Jul 31 2009 BJ Dierkes <wdierkes@rackspace.com> - 5.2.10-2.ius
- Set mysql.allow_persistent = Off in php.ini.  Resolves internal
  Rackspace tracker [#1402].
- Added Patch303: php-5.2.10-imap_bug48619.patch
- Added Patch309: php-5.2.10-bug47351.patch
- Added Patch310: php-5.2.10-bug47285.patch

* Wed Apr 29 2009 BJ Dierkes <wdierkes@rackspace.com> - 5.2.10-1.2.ius
- Rebuilding for IUS.
- Changed name to php52
- Require/BuildRequire: mhash rather than libmhash (EPEL)

* Mon Apr 27 2009 BJ Dierkes <wdierkes@rackspace.com> - 5.2.9-2.rs
- Only build php-pear for el3/4 
- BuildRequires e2fsprogs-devel on el5

* Fri Feb 27 2009 BJ Dierkes <wdierkes@rackspace.com> - 5.2.9-1.rs
- Latest sources from upstream.
- Removed Patch307: php-5.2.8-timelib_no_clone.patch (applied upstream)
- Removed Patch308: php-5.2.8-array.patch (applied upstream)

* Mon Jan 26 2009 BJ Dierkes <wdierkes@rackspace.com> - 5.2.8-3.1.rs
- Adding Vendor tag.

* Tue Jan 06 2009 BJ Dierkes <wdierkes@rackspace.com> - 5.2.8-3.rs
- Adding macros.pear
- Provides php(api), php(zend-abi)

* Tue Dec 23 2008 BJ Dierkes <wdierkes@rackspace.com> - 5.2.8-2.rs
- Added Patch307: php-5.2.8-timelib_no_clone.patch 
  (resolves PHP Bug #46889)
- Added Patch308: php-5.2.8-array.patch (resolves PHP Bug #46893)

* Tue Dec 09 2008 BJ Dierkes <wdierkes@rackspace.com> - 5.2.8-1.rs
- Latest sources
- Replaces Patch350: php-5.2.4-dashn.patch with 
  Patch350: php-5.2.8-dashn.patch
- Replaced Patch302: php-5.2.6-oci8-lib64.patch with 
  Patch302: php-5.2.8-oci8-lib64.patch
- Removed Patch303: php-5.2.6-CVE-2008-3658.patch (applied upstream)
- Removed Patch304: php-5.2.6-CVE-2008-3659.patch (applied upstream)
- Removed Patch305: php-5.2.6-CVE-2008-3660.patch (applied upstream)
- Removed Patch306: php-5.2.6-CVE-2008-2829.patch (applied upstream)

* Thu Nov 20 2008 BJ Dierkes <wdierkes@rackspace.com> - 5.2.6-4.rs
- Added Patch306: php-5.2.6-CVE-2008-2829.patch which backports 
  fixes for PHP Bug #45460

* Wed Oct 22 2008 BJ Dierkes <wdierkes@rackspace.com> - 5.2.6-3.rs
- Added Patch303: php-5.2.6-CVE-2008-3658.patch
- Added Patch304: php-5.2.6-CVE-2008-3659.patch
- Added Patch305: php-5.2.6-CVE-2008-3660.patch
- BuildRequires: zlib

* Fri May 16 2008 BJ Dierkes <wdierkes@rackspace.com> - 5.2.6-2.rs
- php-mysql requires mysqlclient15 on el3 and el4. Resolves Rackspace
  Bug [#486].
- Requires libxslt under main php, Resolves Rackspace Bug [#487].

* Mon May 05 2008 Shawn Ashlee <shawn.ashlee@rackspace.com> 5.2.6-1.rs
- latest sources from upstream
- replaced (Patch302) php-5.2.3-oci8-lib64.patch with php-5.2.6-oci8-lib64.patch

* Thu Apr 03 2008 Shawn Ashlee <shawn.ashlee@rackspace.com> 5.2.5-3.rs
- add tidy module

* Fri Jan 01 2008 BJ Dierkes <wdierkes@rackspace.com> - 5.2.5-2.1.rs
- Requires: libtool-ltdl on el5 (as well)

* Thu Dec 13 2007 BJ Dierkes <wdierkes@rackspace.com> - 5.2.5-2.rs
- BuildRequires: mysql-devel >= 5.0.22 (el5 compatible)
- BuildRequires: libtool-ltdl-devel on el5

* Mon Nov 19 2007 BJ Dierkes <wdierkes@rackspace.com> - 5.2.5-1.rs
- Latest sources.

* Tue Oct 23 2007 BJ Dierkes <wdierkes@rackspace.com> - 5.2.4-2.1.rs
- Disable allow_url_fopen in php.ini
- BuildRequires: mysql-devel >= 5.0.45, Requires mysqlclient15 

* Sun Sep 02 2007 BJ Dierkes <wdierkes@rackspace.com> - 5.2.4-1.1.rs
- Fixed %pre/post common scripts to properly organize php.ini if 
  the current version of php is < 5.

* Fri Aug 31 2007 BJ Dierkes <wdierkes@rackspace.com> - 5.2.4-1.rs
- Latest sources from upstream.
- Replaces Patch1: Patch1: php-5.1.4-gnusrc.patch with
  Patch1: php-5.2.4-gnusrc.patch
- Replaced Patch3: php-5.0.4-norpath.patch with 
  Patch3: php-5.2.4-norpath.patch
- Replaced Patch31: php-5.0.0-easter.patch with
  Patch31: php-5.2.4-easter.patch
- Replaced Patch350: php-5.2.2-tests-dashn.patch with
  Patch350: php-5.2.4-dashn.patch
- Removed Patch21: php-4.3.1-odbc.patch (modified upstream)

* Mon Jul 23 2007 BJ Dierkes <wdierkes@rackspace.com> - 5.2.3-4.rs
- Re-Marking php.ini as noreplace (upgrades for non major versions
  break customer configs).  There is a prein script to move php.ini out
  of the way if the php major version is 4 before upgrade.
- Remove post script that warned about ioncube loader.  Our ioncube
  loader package has a triggerin script that reconfigs after php
  upgrade.
- php.ini pre script goes under the common package

* Thu Jul 12 2007 BJ Dierkes <wdierkes@rackspace.com> - 5.2.3-3.1.rs
- Adding conditional t1lib support, not enabled by default

* Mon Jul 09 2007 BJ Dierkes <wdierkes@rackspace.com> 5.2.3-3.rs
- Adding Patch302: php-5.2.3-oci8-lib64.patch (Bug #41941)

* Fri Jun 29 2007 BJ Dierkes <wdierkes@rackspace.com> 5.2.3-2.rs
- Making spec 'Mock' compatible.
- Adding oci8 module by default
- 'rhelX' vars become 'elX' vars.

* Fri Jun 01 2007 BJ Dierkes <wdierkes@rackspace.com> 5.2.3-1.rs
- Latest sources
- Removing Patch301: php-5.2.2-http_raw_post_data.patch (applied upstream)
- Removed workaround for installing CLI as /usr/bin/php .... PHP now installs
  the CLI by default.

* Tue May 08 2007 BJ Dierkes <wdierkes@rackspace.com> 5.2.2-2.rs
- Adding Patch301: php-5.2.2-http_raw_post_data.patch (PHP BugID: 41293)

* Fri May 03 2007 BJ Dierkes <wdierkes@rackspace.com> 5.2.2-1.rs
- Latest sources
- Replaced Patch50: php-5.0.4-tests-dashn.patch with Patch350: php-5.2.2-tests-dashn.patch
- Removed Patch79: php-5.2.1-CVE-2007-1285.patch (applied upstream)
- Removed Patch80: php-5.1.6-CVE-2007-1583.patch (applied upstream)
- Removed Patch81: php-5.1.6-CVE-2007-0455.patch (applied upstream)
- Removed Patch82: php-5.1.6-CVE-2007-1001.patch (applied upstream)
- Removed Patch83: php-5.1.6-CVE-2007-1718.patch (applied upstream)

* Fri Apr 20 2007 BJ Dierkes <wdierkes@rackspace.com> 5.2.1-5.1.rs
- BuildRequires: apr-devel, elfutils-libelf-devel, apr-util-devel

* Mon Apr 16 2007 BJ Dierkes <wdierkes@rackspace.com> 5.2.1-5.rs
- Security updates.
- Added Patch79: php-5.2.1-CVE-2007-1285.patch
- Added Patch80: php-5.1.6-CVE-2007-1583.patch
- Added Patch81: php-5.1.6-CVE-2007-0455.patch
- Added Patch82: php-5.1.6-CVE-2007-1001.patch
- Added Patch83: php-5.1.6-CVE-2007-1718.patch

* Tue Mar 27 2007 BJ Dierkes <wdierkes@rackspace.com> 5.2.1-4.rs
- Adding optional support for Oracle (oci8) additional module
- Requires/BuildRequires oracle-instantclient-{basic,devel} >= 10.2.0.3

* Fri Feb 23 2007 BJ Dierkes <wdierkes@rackspace.com> 5.2.1-3.2.rs
- Obsoletes any-php-sqlite2
- Add %post script to detect /etc/php.d/ioncube-loader.ini, and if so
  warn installer to verify it's configuration

* Thu Feb 22 2007 BJ Dierkes <wdierkes@rackspace.com> 5.2.1-3.1.rs
- Obsoletes php-sqlite2 

* Tue Feb 13 2007 BJ Dierkes <wdierkes@rackspace.com> 5.2.1-3.rs
- Bring Additional Module definitions in house (set in spec, not at command line)
- Being back mssql support (Requires/BuildRequires freetds/freetds-devel) 
  built in by default

* Fri Feb 09 2007 BJ Dierkes <wdierkes@rackspace.com> 5.2.1-2.rs
- Adding Patch300: php-5.2.1-PQfreemem.patch (PQfreemem requires
  postgresql > 7.4)
 
* Thu Feb 08 2007 BJ Dierkes <wdierkes@rackspace.com> 5.2.1-1.rs
- Latest sources add many features, and improve stability.  The official
  release announcement can be found here: http://www.php.net/releases/5_2_1.php
- Requires libxslt >= 1.1.11, BuildRequires libxslt-devel >= 1.1.11
- Add a -e check on /etc/php.ini in %pre script
- Requires mysqlclient14 on rhel3
- Removed Patch6: php-5.1.6-curl716.patch (applied upstream)
- Removed Patch7: php-5.2.0-filterm4.patch (applied upstream)

* Fri Jan 12 2007 BJ Dierkes <wdierkes@rackspace.com> 5.2.0-9.rs
- Removed '-Wno-pointer-sign' from CFLAGS
- Modified BuildRequires file >= 4.0 to 3.39 (rhel3 savvy, builds fine)
- Modified BuildRequires for imap package to do conditional requires for
  rhel3 (imap-devel) and rhel4 (libc-client-devel)
- Added a %pre script to check for php < 5 php.ini and move it out of the way if it isn't
  (i.e. allow the new php.ini to install to /etc/php.ini)
- Requires/BuildRequires: libxml2 and libxml2-devel >= 2.6.16
- Add conditional change - Use internal pcre on rhel3
- Requires/BuildRequires net-snmp and net-snmp-devel >= 5.1
- Added php-pear back in as a subpackage
- Adding conditional support for Mhash and Mcrypt

* Tue Dec  5 2006 Joe Orton <jorton@redhat.com> 5.2.0-8
- fix filter.h installation path
- fix php-zend-abi version (Remi Collet, #212804)

* Tue Nov 28 2006 Joe Orton <jorton@redhat.com> 5.2.0-7
- rebuild again

* Tue Nov 28 2006 Joe Orton <jorton@redhat.com> 5.2.0-6
- rebuild for net-snmp soname bump

* Mon Nov 27 2006 Joe Orton <jorton@redhat.com> 5.2.0-5
- build json and zip shared, in -common (Remi Collet, #215966)
- obsolete php-json and php-pecl-zip
- build readline extension into /usr/bin/php* (#210585)
- change module subpackages to require php-common not php (#177821)

* Wed Nov 15 2006 Joe Orton <jorton@redhat.com> 5.2.0-4
- provide php-zend-abi (#212804)
- add /etc/rpm/macros.php exporting interface versions
- synch with upstream recommended php.ini

* Wed Nov 15 2006 Joe Orton <jorton@redhat.com> 5.2.0-3
- update to 5.2.0 (#213837)
- php-xml provides php-domxml (#215656)
- fix php-pdo-abi provide (#214281)

* Tue Oct 31 2006 Joseph Orton <jorton@redhat.com> 5.1.6-4
- rebuild for curl soname bump
- add build fix for curl 7.16 API

* Wed Oct  4 2006 Joe Orton <jorton@redhat.com> 5.1.6-3
- from upstream: add safety checks against integer overflow in _ecalloc

* Tue Aug 29 2006 Joe Orton <jorton@redhat.com> 5.1.6-2
- update to 5.1.6 (security fixes)
- bump default memory_limit to 16M (#196802)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 5.1.4-8.1
- rebuild

* Fri Jun  9 2006 Joe Orton <jorton@redhat.com> 5.1.4-8
- Provide php-posix (#194583)
- only provide php-pcntl from -cli subpackage
- add missing defattr's (thanks to Matthias Saou)

* Fri Jun  9 2006 Joe Orton <jorton@redhat.com> 5.1.4-7
- move Obsoletes for php-openssl to -common (#194501)
- Provide: php-cgi from -cli subpackage

* Fri Jun  2 2006 Joe Orton <jorton@redhat.com> 5.1.4-6
- split out php-cli, php-common subpackages (#177821)
- add php-pdo-abi version export (#193202)

* Wed May 24 2006 Radek Vokal <rvokal@redhat.com> 5.1.4-5.1
- rebuilt for new libnetsnmp

* Thu May 18 2006 Joe Orton <jorton@redhat.com> 5.1.4-5
- provide mod_php (#187891)
- provide php-cli (#192196)
- use correct LDAP fix (#181518)
- define _GNU_SOURCE in php_config.h and leave it defined
- drop (circular) dependency on php-pear

* Mon May  8 2006 Joe Orton <jorton@redhat.com> 5.1.4-3
- update to 5.1.4

* Wed May  3 2006 Joe Orton <jorton@redhat.com> 5.1.3-3
- update to 5.1.3

* Tue Feb 28 2006 Joe Orton <jorton@redhat.com> 5.1.2-5
- provide php-api (#183227)
- add provides for all builtin modules (Tim Jackson, #173804)
- own %%{_libdir}/php/pear for PEAR packages (per #176733)
- add obsoletes to allow upgrade from FE4 PDO packages (#181863)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 5.1.2-4.3
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 5.1.2-4.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Joe Orton <jorton@redhat.com> 5.1.2-4
- rebuild for new libc-client soname

* Mon Jan 16 2006 Joe Orton <jorton@redhat.com> 5.1.2-3
- only build xmlreader and xmlwriter shared (#177810)

* Fri Jan 13 2006 Joe Orton <jorton@redhat.com> 5.1.2-2
- update to 5.1.2

* Thu Jan  5 2006 Joe Orton <jorton@redhat.com> 5.1.1-8
- rebuild again

* Mon Jan  2 2006 Joe Orton <jorton@redhat.com> 5.1.1-7
- rebuild for new net-snmp

* Mon Dec 12 2005 Joe Orton <jorton@redhat.com> 5.1.1-6
- enable short_open_tag in default php.ini again (#175381)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Dec  8 2005 Joe Orton <jorton@redhat.com> 5.1.1-5
- require net-snmp for php-snmp (#174800)

* Sun Dec  4 2005 Joe Orton <jorton@redhat.com> 5.1.1-4
- add /usr/share/pear back to hard-coded include_path (#174885)

* Fri Dec  2 2005 Joe Orton <jorton@redhat.com> 5.1.1-3
- rebuild for httpd 2.2

* Mon Nov 28 2005 Joe Orton <jorton@redhat.com> 5.1.1-2
- update to 5.1.1
- remove pear subpackage
- enable pdo extensions (php-pdo subpackage)
- remove non-standard conditional module builds
- enable xmlreader extension

* Thu Nov 10 2005 Tomas Mraz <tmraz@redhat.com> 5.0.5-6
- rebuilt against new openssl

* Mon Nov  7 2005 Joe Orton <jorton@redhat.com> 5.0.5-5
- pear: update to XML_RPC 1.4.4, XML_Parser 1.2.7, Mail 1.1.9 (#172528)

* Tue Nov  1 2005 Joe Orton <jorton@redhat.com> 5.0.5-4
- rebuild for new libnetsnmp

* Wed Sep 14 2005 Joe Orton <jorton@redhat.com> 5.0.5-3
- update to 5.0.5
- add fix for upstream #34435
- devel: require autoconf, automake (#159283)
- pear: update to HTTP-1.3.6, Mail-1.1.8, Net_SMTP-1.2.7, XML_RPC-1.4.1
- fix imagettftext et al (upstream, #161001)

* Thu Jun 16 2005 Joe Orton <jorton@redhat.com> 5.0.4-11
- ldap: restore ldap_start_tls() function

* Fri May  6 2005 Joe Orton <jorton@redhat.com> 5.0.4-10
- disable RPATHs in shared extensions (#156974)

* Tue May  3 2005 Joe Orton <jorton@redhat.com> 5.0.4-9
- build simplexml_import_dom even with shared dom (#156434)
- prevent truncation of copied files to ~2Mb (#155916)
- install /usr/bin/php from CLI build alongside CGI
- enable sysvmsg extension (#142988)

* Mon Apr 25 2005 Joe Orton <jorton@redhat.com> 5.0.4-8
- prevent build of builtin dba as well as shared extension

* Wed Apr 13 2005 Joe Orton <jorton@redhat.com> 5.0.4-7
- split out dba and bcmath extensions into subpackages
- BuildRequire gcc-c++ to avoid AC_PROG_CXX{,CPP} failure (#155221)
- pear: update to DB-1.7.6
- enable FastCGI support in /usr/bin/php-cgi (#149596)

* Wed Apr 13 2005 Joe Orton <jorton@redhat.com> 5.0.4-6
- build /usr/bin/php with the CLI SAPI, and add /usr/bin/php-cgi,
  built with the CGI SAPI (thanks to Edward Rudd, #137704)
- add php(1) man page for CLI
- fix more test cases to use -n when invoking php

* Wed Apr 13 2005 Joe Orton <jorton@redhat.com> 5.0.4-5
- rebuild for new libpq soname

* Tue Apr 12 2005 Joe Orton <jorton@redhat.com> 5.0.4-4
- bundle from PEAR: HTTP, Mail, XML_Parser, Net_Socket, Net_SMTP
- snmp: disable MSHUTDOWN function to prevent error_log noise (#153988)
- mysqli: add fix for crash on x86_64 (Georg Richter, upstream #32282)

* Mon Apr 11 2005 Joe Orton <jorton@redhat.com> 5.0.4-3
- build shared objects as PIC (#154195)

* Mon Apr  4 2005 Joe Orton <jorton@redhat.com> 5.0.4-2
- fix PEAR installation and bundle PEAR DB-1.7.5 package

* Fri Apr  1 2005 Joe Orton <jorton@redhat.com> 5.0.4-1
- update to 5.0.4 (#153068)
- add .phps AddType to php.conf (#152973)
- better gcc4 fix for libxmlrpc

* Wed Mar 30 2005 Joe Orton <jorton@redhat.com> 5.0.3-5
- BuildRequire mysql-devel >= 4.1
- don't mark php.ini as noreplace to make upgrades work (#152171)
- fix subpackage descriptions (#152628)
- fix memset(,,0) in Zend (thanks to Dave Jones)
- fix various compiler warnings in Zend

* Thu Mar 24 2005 Joe Orton <jorton@redhat.com> 5.0.3-4
- package mysqli extension in php-mysql
- really enable pcntl (#142903)
- don't build with --enable-safe-mode (#148969)
- use "Instant Client" libraries for oci8 module (Kai Bolay, #149873)

* Fri Feb 18 2005 Joe Orton <jorton@redhat.com> 5.0.3-3
- fix build with GCC 4

* Wed Feb  9 2005 Joe Orton <jorton@redhat.com> 5.0.3-2
- install the ext/gd headers (#145891)
- enable pcntl extension in /usr/bin/php (#142903)
- add libmbfl array arithmetic fix (dcb314@hotmail.com, #143795)
- add BuildRequire for recent pcre-devel (#147448)

* Wed Jan 12 2005 Joe Orton <jorton@redhat.com> 5.0.3-1
- update to 5.0.3 (thanks to Robert Scheck et al, #143101)
- enable xsl extension (#142174)
- package both the xsl and dom extensions in php-xml
- enable soap extension, shared (php-soap package) (#142901)
- add patches from upstream 5.0 branch:
 * Zend_strtod.c compile fixes
 * correct php_sprintf return value usage

* Mon Nov 22 2004 Joe Orton <jorton@redhat.com> 5.0.2-8
- update for db4-4.3 (Robert Scheck, #140167)
- build against mysql-devel
- run tests in %%check

* Wed Nov 10 2004 Joe Orton <jorton@redhat.com> 5.0.2-7
- truncate changelog at 4.3.1-1
- merge from 4.3.x package:
 - enable mime_magic extension and Require: file (#130276)

* Mon Nov  8 2004 Joe Orton <jorton@redhat.com> 5.0.2-6
- fix dom/sqlite enable/without confusion

* Mon Nov  8 2004 Joe Orton <jorton@redhat.com> 5.0.2-5
- fix phpize installation for lib64 platforms
- add fix for segfault in variable parsing introduced in 5.0.2

* Mon Nov  8 2004 Joe Orton <jorton@redhat.com> 5.0.2-4
- update to 5.0.2 (#127980)
- build against mysqlclient10-devel
- use new RTLD_DEEPBIND to load extension modules
- drop explicit requirement for elfutils-devel
- use AddHandler in default conf.d/php.conf (#135664)
- "fix" round() fudging for recent gcc on x86
- disable sqlite pending audit of warnings and subpackage split

* Fri Sep 17 2004 Joe Orton <jorton@redhat.com> 5.0.1-4
- don't build dom extension into 2.0 SAPI

* Fri Sep 17 2004 Joe Orton <jorton@redhat.com> 5.0.1-3
- ExclusiveArch: x86 ppc x86_64 for the moment

* Fri Sep 17 2004 Joe Orton <jorton@redhat.com> 5.0.1-2
- fix default extension_dir and conf.d/php.conf

* Thu Sep  9 2004 Joe Orton <jorton@redhat.com> 5.0.1-1
- update to 5.0.1
- only build shared modules once
- put dom extension in php-dom subpackage again
- move extension modules into %%{_libdir}/php/modules
- don't use --with-regex=system, it's ignored for the apache* SAPIs

* Wed Aug 11 2004 Tom Callaway <tcallawa@redhat.com>
- Merge in some spec file changes from Jeff Stern (jastern@uci.edu)

* Mon Aug 09 2004 Tom Callaway <tcallawa@redhat.com>
- bump to 5.0.0
- add patch to prevent clobbering struct re_registers from regex.h
- remove domxml references, replaced with dom now built-in
- fix php.ini to refer to php5 not php4

* Wed Aug 04 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- rebuild

* Wed Jul 14 2004 Joe Orton <jorton@redhat.com> 4.3.8-3
- update to 4.3.8
- catch some fd > FD_SETSIZE vs select() issues (#125258)

* Mon Jun 21 2004 Joe Orton <jorton@redhat.com> 4.3.7-4
- pick up test failures again
- have -devel require php of same release

* Thu Jun 17 2004 Joe Orton <jorton@redhat.com> 4.3.7-3
- add gmp_powm fix (Oskari Saarenmaa, #124318)
- split mbstring, ncurses, gd, openssl extns into subpackages
- fix memory leak in apache2handler; use ap_r{write,flush}
  rather than brigade interfaces

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jun  3 2004 Joe Orton <jorton@redhat.com> 4.3.7-1
- update to 4.3.7
- have -pear subpackage require php of same VR

* Wed May 26 2004 Joe Orton <jorton@redhat.com> 4.3.6-6
- buildrequire smtpdaemon (#124430)
- try switching to system libgd again (prevent symbol conflicts
  when e.g. mod_perl loads the system libgd library.)

* Wed May 19 2004 Joe Orton <jorton@redhat.com> 4.3.6-5
- don't obsolete php-imap (#123580)
- unconditionally build -imap subpackage

* Thu May 13 2004 Joe Orton <jorton@redhat.com> 4.3.6-4
- remove trigger

* Thu Apr 22 2004 Joe Orton <jorton@redhat.com> 4.3.6-3
- fix umask reset "feature" (#121454)
- don't use DL_GLOBAL when dlopen'ing extension modules

* Sun Apr 18 2004 Joe Orton <jorton@redhat.com> 4.3.6-2
- fix segfault on httpd SIGHUP (upstream #27810)

* Fri Apr 16 2004 Joe Orton <jorton@redhat.com> 4.3.6-1
- update to 4.3.6 (Robert Scheck, #121011)

* Wed Apr  7 2004 Joe Orton <jorton@redhat.com> 4.3.4-11
- add back imap subpackage, using libc-client (#115535)

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 18 2004 Joe Orton <jorton@redhat.com> 4.3.4-10
- eliminate /usr/local/lib RPATH in odbc.so
- really use system pcre library

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com> 4.3.4-9
- rebuilt

* Mon Feb  2 2004 Bill Nottingham <notting@redhat.com> 4.3.4-8
- obsolete php-imap if we're not building it

* Wed Jan 28 2004 Joe Orton <jorton@redhat.com> 4.3.4-7
- gd fix for build with recent Freetype2 (from upstream)
- remove easter egg (Oden Eriksson, Mandrake)

* Wed Jan 21 2004 Joe Orton <jorton@redhat.com> 4.3.4-6
- php-pear requires php
- also remove extension=imap from php.ini in upgrade trigger
- merge from Taroon: allow upgrade from Stronghold 4.0

* Wed Jan 21 2004 Joe Orton <jorton@redhat.com> 4.3.4-5
- add defattr for php-pear subpackage
- restore defaults: output_buffering=Off, register_argc_argv=On
- add trigger to handle php.ini upgrades smoothly (#112470)

* Tue Jan 13 2004 Joe Orton <jorton@redhat.com> 4.3.4-4
- conditionalize support for imap extension for the time being
- switch /etc/php.ini to use php.ini-recommended (but leave
  variables_order as EGPCS) (#97765)
- set session.path to /var/lib/php/session by default (#89975)
- own /var/lib/php{,/session} and have apache own the latter
- split off php-pear subpackage (#83771)

* Sat Dec 13 2003 Jeff Johnson <jbj@jbj.org> 4.3.4-3
- rebuild against db-4.2.52.

* Mon Dec  1 2003 Joe Orton <jorton@redhat.com> 4.3.4-2
- rebuild for new libxslt (#110658) 
- use --with-{mssql,oci8} for enabling extensions (#110482)
- fix rebuild issues (Jan Visser, #110274)
- remove hard-coded LIBS
- conditional support for mhash (Aleksander Adamowski, #111251)

* Mon Nov 10 2003 Joe Orton <jorton@redhat.com> 4.3.4-1.1
- rebuild for FC1 updates

* Mon Nov 10 2003 Joe Orton <jorton@redhat.com> 4.3.4-1
- update to 4.3.4
- include all licence files
- libxmlrpc fixes

* Mon Oct 20 2003 Joe Orton <jorton@redhat.com> 4.3.3-6
- use bundled libgd (#107407)
- remove manual: up-to-date manual sources are no longer DFSG-free;
  it's too big; it's on the web anyway; #91292, #105804, #107384

* Wed Oct 15 2003 Joe Orton <jorton@redhat.com> 4.3.3-5
- add php-xmlrpc subpackage (#107138)

* Mon Oct 13 2003 Joe Orton <jorton@redhat.com> 4.3.3-4
- drop recode support, symbols collide with MySQL

* Sun Oct 12 2003 Joe Orton <jorton@redhat.com> 4.3.3-3
- split domxml extension into php-domxml subpackage
- enable xslt and xml support in domxml extension (#106042)
- fix httpd-devel build requirement (#104341)
- enable recode extension (#106755)
- add workaround for #103982

* Thu Sep 25 2003 Jeff Johnson <jbj@jbj.org> 4.3.3-3
- rebuild against db-4.2.42.

* Sun Sep  7 2003 Joe Orton <jorton@redhat.com> 4.3.3-2
- don't use --enable-versioning, it depends on libtool being
 broken (#103690)

* Sun Sep  7 2003 Joe Orton <jorton@redhat.com> 4.3.3-1
- update to 4.3.3
- add libtool build prereq (#103388)
- switch to apache2handler

* Mon Jul 28 2003 Joe Orton <jorton@redhat.com> 4.3.2-8
- rebuild

* Tue Jul 22 2003 Nalin Dahyabhai <nalin@redhat.com> 4.3.2-7
- rebuild

* Tue Jul  8 2003 Joe Orton <jorton@redhat.com> 4.3.2-6
- use system pcre library

* Mon Jun  9 2003 Joe Orton <jorton@redhat.com> 4.3.2-5
- enable mbstring and mbregex (#81336)
- fix use of libtool 1.5

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  3 2003 Joe Orton <jorton@redhat.com> 4.3.2-3
- add lib64 and domxml fixes

* Tue Jun  3 2003 Frank Dauer <f@paf.net>
- added conditional support for mssql module (#92149)

* Fri May 30 2003 Joe Orton <jorton@redhat.com> 4.3.2-2
- update the -tests and -lib64 patches
- fixes for db4 detection
- require aspell-devel >= 0.50.0 for pspell compatibility

* Thu May 29 2003 Joe Orton <jorton@redhat.com> 4.3.2-1
- update to 4.3.2

* Fri May 16 2003 Joe Orton <jorton@redhat.com> 4.3.1-3
- link odbc module correctly
- patch so that php -n doesn't scan inidir
- run tests using php -n, avoid loading system modules

* Wed May 14 2003 Joe Orton <jorton@redhat.com> 4.3.1-2
- workaround broken parser produced by bison-1.875

* Tue May  6 2003 Joe Orton <jorton@redhat.com> 4.3.1-1
- update to 4.3.1; run test suite
- open extension modules with RTLD_NOW rather than _LAZY
