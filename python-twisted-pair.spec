Summary:        A module to do low level tcp stuff with Twisted
Name:           python-twisted-pair
Version: 0.1.0
Release: %mkrel 3
%define directory_down %(echo %version|perl -n -e  '/^(\d+\.\d+).*$/; print \$1 ')
Source0:        http://tmrc.mit.edu/mirror/twisted/Pair//%directory_down/TwistedPair-%{version}.tar.bz2
License:        MIT
Group:          Development/Python
URL:            http://twistedmatrix.com/projects/pair/
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel python-twisted-core
Requires:       python-twisted-core
# do not work on x86_64 du to module loading issue
#BuildArch:      noarch
%description
A module to do low level tcp stuff with Twisted.


%prep
%setup -q -n TwistedPair-%version

%build
%__python setup.py build

%install
%__rm -rf %buildroot
%__python setup.py install --root  %buildroot --install-purelib=%py_platsitedir

%clean
%__rm -rf %buildroot

%files
%defattr(0644,root,root,0755)
%doc LICENSE README doc/*
%py_platsitedir/twisted/pair/

