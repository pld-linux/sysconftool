Summary:	macros for aclocal to install configuration files
Summary(pl):	makra dla aclocal do instalacji plików konfiguracyjnych
Name:		sysconftool
Version:	0.12
Release:	1
License:	GPL
Group:		Development/Building
Group(de):	Entwicklung/Bauen
Group(fr):	Librairies
Group(pl):	Programowanie/Budowanie
Source0:	http://download.sourceforge.net/courier/%{name}-%{version}.tar.gz
URL:		http://zekiller.skytech.org/coders_en.html
BuildArch:	noarch
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
aclocal
autoconf
automake 

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
%{_datadir}/sysconftool/*
%{_mandir}/man1/*
%{_mandir}/man7/*
%{_aclocaldir}/sysconftool.m4
