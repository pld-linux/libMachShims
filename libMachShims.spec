Summary:	Shims for Mach datatypes and functions
Summary(pl.UTF-8):	Przejściówki do typów danych i funkcji systemu Mach
Name:		libMachShims
Version:	0
%define	subver	svn20
Release:	0.%{subver}.1
License:	Apache v2.0
Group:		Libraries
# svn co svn://mark.heily.com/libMachShims
Source0:	%{name}.tar.xz
# Source0-md5:	37e5d017c28e0487d24462c73550f351
Patch0:		%{name}-headers.patch
URL:		http://mark.heily.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shims for Mach datatypes and functions.

%description -l pl.UTF-8
Przejściówki do typów danych i funkcji systemu Mach

%package devel
Summary:	Header files for libMachShims library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libMachShims
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libMachShims library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libMachShims.

%package static
Summary:	Static libMachShims library
Summary(pl.UTF-8):	Statyczna biblioteka libMachShims
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libMachShims library.

%description static -l pl.UTF-8
Statyczna biblioteka libMachShims.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
# NOTE: not autoconf configure
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
CPPFLAGS="%{rpmcppflags}" \
LDFLAGS="%{rpmldflags}" \
./configure \
	--prefix=%{_prefix} \
	--includedir=%{_includedir}/mach \
	--libdir=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/mach}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	INCLUDEDIR=%{_includedir}/mach \
	LIBDIR=%{_libdir}

install libMachShims.a $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libMachShims.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libMachShims.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libMachShims.so
%{_includedir}/mach

%files static
%defattr(644,root,root,755)
%{_libdir}/libMachShims.a
