%global cartridgedir %{_libexecdir}/openshift/cartridges/nodejs-python
%global httpdconfdir /etc/openshift/cart.conf.d/httpd/nodejs-python

Name:          openshift-cartridge-nodejs-python
Version: 0.1
Release:       1%{?dist}
Summary:       Node.js + Python 3 cartridge
Group:         Development/Languages
License:       ASL 2.0
URL:           http://github.com/ominee/openshift-cartridge-nodejs-python
Source0:       http://github.com/ominee/openshift-cartridge-nodejs-python/archive/master.tar.gz
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
%if 0%{?fedora}%{?rhel} <= 6
Requires:      python >= 2.6
Requires:      python < 2.7
Requires:      scl-utils
BuildRequires: scl-utils-build
#FIXME: Use %scl_require macro to properly define dependencies
Requires:      python27
Requires:      mod_wsgi >= 3.2
Requires:      mod_wsgi < 3.4
%endif
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
%if 0%{?fedora} >= 19
Requires:      python >= 2.7
Requires:      python < 2.8
Requires:      mod_wsgi >= 3.4
Requires:      mod_wsgi < 3.5
%endif
Requires:      python-virtualenv
%if 0%{?fedora}%{?rhel} <= 6
Requires:      python27-python-pip-virtualenv
Requires:      python27-mod_wsgi
Requires:      python33-python-virtualenv
Requires:      python33-mod_wsgi
%endif
%if 0%{?fedora}%{?rhel} <= 6
Requires:      %{scl}
%endif
Requires:      %{?scl:%scl_prefix}npm
Requires:      %{?scl:%scl_prefix}nodejs-pg
Requires:      %{?scl:%scl_prefix}nodejs-options
Requires:      %{?scl:%scl_prefix}nodejs-supervisor
Requires:      %{?scl:%scl_prefix}nodejs-async
Requires:      %{?scl:%scl_prefix}nodejs-express
Requires:      %{?scl:%scl_prefix}nodejs-connect
Requires:      %{?scl:%scl_prefix}nodejs-mongodb
Requires:      %{?scl:%scl_prefix}nodejs-mysql
Requires:      %{?scl:%scl_prefix}nodejs-node-static
Requires:      nodejs
Requires:      nodejs-async
Requires:      nodejs-connect
Requires:      nodejs-express
Requires:      nodejs-mongodb
Requires:      nodejs-mysql
Requires:      nodejs-node-static
Requires:      nodejs-pg
Requires:      nodejs-supervisor
Requires:      nodejs-options
Provides:      openshift-cartridge-nodejs-python = 0.1
BuildArch:     noarch

%description
Node.js + Python 3 cartridge for OpenShift. (Cartridge Format V2)


%prep
%setup -q

%build
%__rm %{name}.spec
%__rm logs/.gitkeep
%__rm run/.gitkeep
find versions/ -name .gitignore -delete
find versions/ -name .gitkeep -delete

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}
%__mkdir -p %{buildroot}%{httpdconfdir}

%__mkdir -p %{buildroot}%{cartridgedir}/env

%__mkdir -p %{buildroot}%{cartridgedir}/usr/versions/3.3
%if 0%{?fedora}%{?rhel} <= 6
%__cp -anv %{buildroot}%{cartridgedir}/usr/versions/3.3-scl/* %{buildroot}%{cartridgedir}/usr/versions/3.3/
%endif
%__cp -anv %{buildroot}%{cartridgedir}/usr/versions/shared/* %{buildroot}%{cartridgedir}/usr/versions/3.3/

%__rm -rf %{buildroot}%{cartridgedir}/usr/versions/shared
%__rm -rf %{buildroot}%{cartridgedir}/usr/versions/3.3-scl

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%dir %{httpdconfdir}
%attr(0755,-,-) %{httpdconfdir}
%attr(0755,-,-) %{cartridgedir}/usr/versions/3.3/bin/*
%{cartridgedir}/env
%{cartridgedir}/lib
%{cartridgedir}/logs
%{cartridgedir}/metadata
%{cartridgedir}/run
%{cartridgedir}/usr
%{cartridgedir}/versions
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE
%exclude %{cartridgedir}/usr/versions/*/template/*.pyc
%exclude %{cartridgedir}/usr/versions/*/template/*.pyo
