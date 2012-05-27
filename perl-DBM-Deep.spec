#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	DBM
%define		pnam	Deep
Summary:	DBM::Deep - A pure Perl multi-level hash/array DBM
Summary(pl.UTF-8):	DBM::Deep - czysto perlowy moduł DBM dla wielopoziomowych haszy/tablic
Name:		perl-DBM-Deep
Version:	2.0006
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/SP/SPROUT/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f0e009da2d5919031ce5b9c595e2c1e1
URL:		http://search.cpan.org/dist/DBM-Deep/
BuildRequires:	perl-devel >= 1:5.8.4
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Digest-MD5 >= 1.00
BuildRequires:	perl-File-Temp >= 0.01
BuildRequires:	perl-IO-stringy >= 0.01
BuildRequires:	perl-Pod-Parser >= 1.3
BuildRequires:	perl-Scalar-List-Utils >= 1.14
BuildRequires:	perl-Test-Builder-Tester >= 0.13
BuildRequires:	perl-Test-Deep >= 0.095
BuildRequires:	perl-Test-Exception >= 0.21
BuildRequires:	perl-Test-Simple >= 0.88
BuildRequires:	perl-Test-Warn >= 0.08
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A unique flat-file database module, written in pure Perl. True
multi-level hash/array support (unlike MLDBM, which is faked), hybrid
OO/tie() interface, cross-platform FTPable files, and quite fast. Can
handle millions of keys and unlimited hash levels without significant
slow-down. Written from the ground-up in pure Perl - this is NOT a
wrapper around a C-based DBM. Out-of-the-box compatibility with Unix,
Mac OS X and Windows.

%description -l pl.UTF-8
Jest to unikalny moduł bazy danych na płaskim pliku, napisany w
czystym Perlu. Ma prawdziwą obsługę wielopoziomowych haszy/tablic (w
przeciwieństwie do MLDBM, który jest oszukany), hybrydowy interfejs
obiektowy/tie(), wieloplatformowe pliki po FTP i jest dość szybki.
Może obsłużyć miliony kluczy i nieograniczoną liczbę poziomów tablic
asocjacyjnych bez znacznego spowolnienia. Napisany jest od początku w
czystym Perlu - NIE jest to wrapper na moduł DBM napisany w C. Jest
kompatybilny z Uniksami, Mac OS X oraz Windows.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	destdir=$RPM_BUILD_ROOT \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/DBM/Deep.pod \
	$RPM_BUILD_ROOT%{perl_vendorlib}/DBM/Deep/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/DBM
%{perl_vendorlib}/DBM/Deep.pm
%{perl_vendorlib}/DBM/Deep
%{_mandir}/man3/DBM::Deep*.3pm*
