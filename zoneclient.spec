Summary:	zoneclient - zoneedit.com service client written in Python
Summary(pl):	Klient serwisu zoneedit.com napisany w Pythonie
Name:		zoneclient
Version:	0.44
Release:	1
License:	GNU v2
Group:		Networking
Source0:	http://ep09.pld-linux.org/~domelu/pld/zoneclient/%{name}-%{version}.tar.gz
# Source0-md5:	221a2ddbba356b111d1c0319926eca4b
URL:		http://zoneclient.sourceforge.net/
BuildRequires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zoneedit.com service client written in Python.

%description -l pl
Klient serwisu zoneedit.com napisany w Pythonie.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install zoneclient.py $RPM_BUILD_ROOT%{_bindir}/zoneclient.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/zoneclient.py
