%include	/usr/lib/rpm/macros.perl
%define		pdir	Data
%define		pnam	Buffer
Summary:	Data::Buffer Perl module - read/write buffer class
Summary(pl):	Modu³ Perla Data::Buffer - klasa bufora odczytu/zapisu
Name:		perl-Data-Buffer
Version:	0.04
Release:	2
# same as erl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d971f7b92684cc4f4cba7a9c774b8480
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::Buffer implements a low-level binary buffer in which you can get
and put integers, strings, and other data.

%description -l pl
Modu³ Data::Buffer jest implementacj± niskopoziomowego, binarnego
bufora. Mo¿na w nim umieszczaæ i z niego pobieraæ liczby ca³kowite,
³añcuchy i inne dane.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Data/Buffer.pm
%{_mandir}/man3/*
