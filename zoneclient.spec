%include	/usr/lib/rpm/macros.python
Summary:	zoneclient - zoneedit.com service client written in Python
Summary(pl):	Klient serwisu zoneedit.com napisany w Pythonie
Name:		zoneclient
Version:	0.43
Release:	0.1
License:	GNU v2
Group:		Networking/Daemons
Source0:	http://ep09.pld-linux.org/~domelu/pld/zoneclient/%{name}-%{version}.tar.gz
# Source0-md5:	3d9fc83fc70482135a17e241a7b86138
URL:		http://zoneclient.sourceforge.net/
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
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
