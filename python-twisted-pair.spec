Summary:        A module to do low level tcp stuff with Twisted
Name:           python-twisted-pair
Version: 9.0.0
Release: 2
%define directory_down %(echo %version|perl -n -e  '/^(\d+\.\d+).*$/; print \$1 ')
Source0:        http://tmrc.mit.edu/mirror/twisted/Pair//%directory_down/TwistedPair-%{version}.tar.bz2
License:        MIT
Group:          Development/Python
URL:            http://twistedmatrix.com/projects/pair/
BuildRequires:	python-devel python-twisted-core
Requires:       python-twisted-core
# do not work on x86_64 du to module loading issue
#BuildArch:      noarch

%define debug_package %{nil}

%description
A module to do low level tcp stuff with Twisted.


%prep
%setup -q -n TwistedPair-%version

%build
%__python setup.py build

%install
%__python setup.py install --root  %buildroot --install-purelib=%py_platsitedir

%files
%defattr(0644,root,root,0755)
%doc LICENSE README doc/*
%py_platsitedir/*



%changelog
* Sat Jan 02 2010 Frederik Himpe <fhimpe@mandriva.org> 9.0.0-1mdv2011.0
+ Revision: 485572
- Update to new version 9.0.0

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 8.2.0-2mdv2010.0
+ Revision: 442517
- rebuild

* Sat Jan 03 2009 Jérôme Soyer <saispo@mandriva.org> 8.2.0-1mdv2009.1
+ Revision: 323857
- New upstream release

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Jan 25 2006 Michael Scherer <misc@mandriva.org> 0.1.0-2mdk
- make it arch dependant
- use macro
- make it rpmbuildupdatable

* Sat May 14 2005 Michael Scherer <misc@mandriva.org> 0.1.0-1mdk
- Initial package

