Summary:	Macros for aclocal to install configuration files
Summary(pl):	Makra dla aclocal do instalacji plików konfiguracyjnych
Name:		sysconftool
Version:	0.14
Release:	2
License:	GPL
Group:		Development/Building
Source0:	http://dl.sourceforge.net/courier/%{name}-%{version}.tar.bz2
# Source0-md5:	899bd76c99c9654160c046e04f74d2b1
Patch0:		%{name}-am18.patch
URL:		http://zekiller.skytech.org/coders_en.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sysconftool is a development utility that helps to install application
configuration files. sysconftool allows an existing application to be
upgraded without losing the older version's configuration settings.

%description -l pl
sysconftool jest narzêdziem, które pomaga instalowaæ pliki
konfiguracyjne aplikacji. sysconftool pozwala na wymienienie
istniej±cych aplikacji na nowsze wersje, bez straty starszych wersji
plików konfiguracyjnych.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS ChangeLog
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/sysconftool
%attr(755,root,root) %{_datadir}/sysconftool/sysconftool
%attr(755,root,root) %{_datadir}/sysconftool/sysconftoolcheck
%attr(755,root,root) %{_datadir}/sysconftool/sysconftoolize.pl
%{_datadir}/sysconftool/sysconftoolize.am
%{_mandir}/man1/*
%{_mandir}/man7/*
%{_aclocaldir}/sysconftool.m4
