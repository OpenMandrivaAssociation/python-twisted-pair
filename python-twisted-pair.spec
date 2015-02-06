Summary:        A module to do low level tcp stuff with Twisted
Name:           python-twisted-pair
Version: 14.0.0
Release: 2
%define directory_down %(echo %{version}|perl -n -e  '/^(\d+\.\d+).*$/; print \$1 ')
Source0:        http://twistedmatrix.com/Releases/Pair/14.0/TwistedPair-%{version}.tar.bz2
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
%setup -q -n TwistedPair-%{version}

%build
%__python setup.py build

%install
%__python setup.py install --root  %{buildroot} --install-purelib=%{py_platsitedir}

%files
%defattr(0644,root,root,0755)
%doc LICENSE README *
%{py_platsitedir}/*
