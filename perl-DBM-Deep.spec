#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	DBM
%define	pnam	Deep
Summary:	DBM::Deep - A pure perl multi-level hash/array DBM
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
A unique flat-file database module, written in pure perl. True
multi-level hash/array support (unlike MLDBM, which is faked), hybrid
OO/tie() interface, cross-platform FTPable files, and quite fast.
Can handle millions of keys and unlimited hash levels without
significant slow-down. Written from the ground-up in pure perl --
this is NOT a wrapper around a C-based DBM. Out-of-the-box
compatibility with Unix, Mac OS X and Windows.

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
