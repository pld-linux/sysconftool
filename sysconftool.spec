Summary:	Macros for aclocal to install configuration files
Summary(pl.UTF-8):	Makra dla aclocal do instalacji plików konfiguracyjnych
Name:		sysconftool
Version:	0.16
Release:	1
License:	GPL v3 with OpenSSL exception
Group:		Development/Building
Source0:	http://downloads.sourceforge.net/courier/%{name}-%{version}.tar.bz2
# Source0-md5:	cca4ee11427dc1c0462b861cd785cdf1
URL:		http://www.courier-mta.org/sysconftool/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sysconftool is a development utility that helps to install application
configuration files. sysconftool allows an existing application to be
upgraded without losing the older version's configuration settings.

%description -l pl.UTF-8
sysconftool jest narzędziem, które pomaga instalować pliki
konfiguracyjne aplikacji. sysconftool pozwala na uaktualnienie
istniejących aplikacji bez utraty starszych wersji plików
konfiguracyjnych.

%prep
%setup -q

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
%doc AUTHORS COPYING ChangeLog NEWS
%attr(755,root,root) %{_bindir}/sysconftoolcheck
%attr(755,root,root) %{_bindir}/sysconftoolize
%dir %{_datadir}/sysconftool
%attr(755,root,root) %{_datadir}/sysconftool/sysconftool
%attr(755,root,root) %{_datadir}/sysconftool/sysconftoolcheck
%attr(755,root,root) %{_datadir}/sysconftool/sysconftoolize.pl
%{_datadir}/sysconftool/sysconftoolize.am
%{_mandir}/man1/sysconftool.1*
%{_mandir}/man1/sysconftoolcheck.1*
%{_mandir}/man7/sysconftool.7*
%{_aclocaldir}/sysconftool.m4
