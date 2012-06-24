#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	DBM
%define		pnam	Deep
Summary:	DBM::Deep - A pure Perl multi-level hash/array DBM
Summary(pl):	DBM::Deep - czysto perlowy modu� DBM dla wielopoziomowych haszy/tablic
Name:		perl-DBM-Deep
Version:	0.94
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	157130c0e4e25e2baaf2dd2adfde70fd
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A unique flat-file database module, written in pure Perl. True
multi-level hash/array support (unlike MLDBM, which is faked), hybrid
OO/tie() interface, cross-platform FTPable files, and quite fast.
Can handle millions of keys and unlimited hash levels without
significant slow-down. Written from the ground-up in pure Perl -
this is NOT a wrapper around a C-based DBM. Out-of-the-box
compatibility with Unix, Mac OS X and Windows.

%description -l pl
Jest to unikalny modu� bazy danych na p�askim pliku, napisany w
czystym Perlu. Ma prawdziw� obs�ug� wielopoziomowych haszy/tablic (w
przeciwie�stwie do MLDBM, kt�ry jest oszukany), hybrydowy interfejs
obiektowy/tie(), wieloplatformowe pliki po FTP i jest do�� szybki.
Mo�e obs�u�y� miliony kluczy i nieograniczon� liczb� poziom�w tablic
asocjacyjnych bez znacznego spowolnienia. Napisany jest od pocz�tku w
czystym Perlu - NIE jest to wrapper na modu� DBM napisany w C. Jest
kompatybilny z Uniksami, Mac OS X oraz Windows.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/DBM
%{perl_vendorlib}/DBM/Deep.pm
%{_mandir}/man3/*
