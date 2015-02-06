%define		_class		DB
%define		_subclass	ldap2
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.5.0
Release:	9
Summary:	DB drivers for LDAP v2 and v3 database
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/DB_ldap2/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
DB_ldap2 and DB_ldap3 classes extend DB_common to provide DB compliant
access to LDAP servers with protocol version 2 and 3. The drivers
provide common DB interface as much as possible and support
prepare/execute statements.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-6mdv2012.0
+ Revision: 741848
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-5
+ Revision: 679292
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-4mdv2011.0
+ Revision: 613633
- the mass rebuild of 2010.1 packages

* Wed Dec 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.0-3mdv2010.1
+ Revision: 479291
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.5.0-2mdv2010.0
+ Revision: 440975
- rebuild

* Mon Apr 20 2009 Raphaël Gertz <rapsys@mandriva.org> 0.5.0-1mdv2009.1
+ Revision: 368307
- Update php pear DB_ldap2 to 0.5.0 version

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.4-9mdv2009.1
+ Revision: 321963
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4-8mdv2009.0
+ Revision: 236829
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.4-7mdv2007.0
+ Revision: 81562
- Import php-pear-DB_ldap2

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.4-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-1mdk
- initial Mandriva package (PLD import)

