#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Metrics-Any
Version  : 0.10
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Metrics-Any-0.10.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Metrics-Any-0.10.tar.gz
Summary  : 'abstract collection of monitoring metrics'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Metrics-Any-license = %{version}-%{release}
Requires: perl-Metrics-Any-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Metrics::Any - abstract collection of monitoring metrics
SYNOPSIS
In a module:

%package dev
Summary: dev components for the perl-Metrics-Any package.
Group: Development
Provides: perl-Metrics-Any-devel = %{version}-%{release}
Requires: perl-Metrics-Any = %{version}-%{release}

%description dev
dev components for the perl-Metrics-Any package.


%package license
Summary: license components for the perl-Metrics-Any package.
Group: Default

%description license
license components for the perl-Metrics-Any package.


%package perl
Summary: perl components for the perl-Metrics-Any package.
Group: Default
Requires: perl-Metrics-Any = %{version}-%{release}

%description perl
perl components for the perl-Metrics-Any package.


%prep
%setup -q -n Metrics-Any-0.10
cd %{_builddir}/Metrics-Any-0.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Metrics-Any
cp %{_builddir}/Metrics-Any-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Metrics-Any/df9f2d29a10846c30925e18b0273e53356f88a79 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Metrics::Any.3
/usr/share/man/man3/Metrics::Any::Adapter.3
/usr/share/man/man3/Metrics::Any::Adapter::File.3
/usr/share/man/man3/Metrics::Any::Adapter::Null.3
/usr/share/man/man3/Metrics::Any::Adapter::Stderr.3
/usr/share/man/man3/Metrics::Any::Adapter::Tee.3
/usr/share/man/man3/Metrics::Any::Adapter::Test.3
/usr/share/man/man3/Metrics::Any::AdapterBase::Stored.3
/usr/share/man/man3/Metrics::Any::Collector.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Metrics-Any/df9f2d29a10846c30925e18b0273e53356f88a79

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
