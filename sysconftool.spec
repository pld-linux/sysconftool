Summary:	Macros for aclocal to install configuration files
Summary(pl):	Makra dla aclocal do instalacji plików konfiguracyjnych
Name:		sysconftool
Version:	0.13
Release:	1
License:	GPL
Group:		Development/Building
Group(de):	Entwicklung/Bauen
Group(fr):	Librairies
Group(pl):	Programowanie/Budowanie
Source0:	http://download.sourceforge.net/courier/%{name}-%{version}.tar.gz
URL:		http://zekiller.skytech.org/coders_en.html
BuildArch:	noarch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sysconftool is a development utility that helps to install application
configuration files. sysconftool allows an existing application to be
upgraded without losing the older version's configuration settings.

%description -l pl
sysconftool jest narzêdziem które pomaga instalowaæ pliki
konfiguracyjne aplikacji. sysconftool pozwala na wymienienie
istniej±cych aplikacji na nowsze wersje, bez straty starszych wersji
plików konfiguracyjnych.

%prep
%setup -q

%build
rm -f missing
aclocal
autoconf
automake -a -c 
%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS NEWS ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_datadir}/sysconftool/sysconftool
%attr(755,root,root) %{_datadir}/sysconftool/sysconftoolcheck
%attr(755,root,root) %{_datadir}/sysconftool/sysconftoolize.pl
%{_datadir}/sysconftool/sysconftoolize.am
%{_mandir}/man1/*
%{_mandir}/man7/*
%{_aclocaldir}/sysconftool.m4
