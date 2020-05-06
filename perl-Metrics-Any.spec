#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Metrics-Any
Version  : 0.03
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Metrics-Any-0.03.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Metrics-Any-0.03.tar.gz
Summary  : 'abstract collection of monitoring metrics'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Metrics-Any-license = %{version}-%{release}
Requires: perl-Metrics-Any-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

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
%setup -q -n Metrics-Any-0.03
cd %{_builddir}/Metrics-Any-0.03

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Metrics-Any
cp %{_builddir}/Metrics-Any-0.03/LICENSE %{buildroot}/usr/share/package-licenses/perl-Metrics-Any/7e88e362b09da4b18d7e611c14945b5734383496
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
/usr/share/man/man3/Metrics::Any::Adapter::Null.3
/usr/share/man/man3/Metrics::Any::Adapter::Test.3
/usr/share/man/man3/Metrics::Any::Collector.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Metrics-Any/7e88e362b09da4b18d7e611c14945b5734383496

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.2/Metrics/Any.pm
/usr/lib/perl5/vendor_perl/5.30.2/Metrics/Any/Adapter.pm
/usr/lib/perl5/vendor_perl/5.30.2/Metrics/Any/Adapter/Null.pm
/usr/lib/perl5/vendor_perl/5.30.2/Metrics/Any/Adapter/Test.pm
/usr/lib/perl5/vendor_perl/5.30.2/Metrics/Any/Collector.pm
