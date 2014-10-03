Summary:	LDL: a simple LDL^T factorization for sparse matrices
Summary(pl.UTF-8):	LDL - prosty rozkład LDL^T dla macierzy rzadkich
Name:		LDL
Version:	2.2.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.cise.ufl.edu/research/sparse/ldl/%{name}-%{version}.tar.gz
# Source0-md5:	9420881cadb9b55177d7f9a504674f40
Patch0:		%{name}-ufconfig.patch
Patch1:		%{name}-shared.patch
URL:		http://www.cise.ufl.edu/research/sparse/ldl/
BuildRequires:	SuiteSparse_config >= 4.3.0
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LDL is a set of concise routines for factorizing symmetric
positive-definite sparse matrices, with some applicability to
symmetric indefinite matrices. Its primary purpose is to illustrate
much of the basic theory of sparse matrix algorithms in as concise a
code as possible, including an elegant new method of sparse symmetric
factorization that computes the factorization row-by-row but stores it
column-by-column. The entire symbolic and numeric factorization
consists of a total of only 49 lines of code. The package is written
in C, and includes a MATLAB interface.

%description -l pl.UTF-8
LDL to zbiór zwięzłych procedur do dokonywania rozkładów
symetrycznych, dodatnio określonych macierzy rzadkich, z częściową
możliwością stosowania do macierzy symetrycznych nieokreślonych.
Główny cel tych procedur to zademonstrowanie dużej części podstawowej
teorii algorytmów dla macierzy rzadkich w jak najbardziej zwięzłym
kodzie, w tym eleganckiej nowej metody rozkładu symetrycznych macierzy
rzadkich, liczącej rozkład wierszami, ale zapisującej go kolumnami.
Cały rozkład symboliczny i numeryczny składa się z jedynie 49 linii
kodu. Pakiet został napisany w C i zawiera interfejs dla MATLAB-a.

%package devel
Summary:	Header files for LDL library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki LDL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SuiteSparse_config >= 4.3.0

%description devel
Header files for LDL library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki LDL.

%package static
Summary:	Static LDL library
Summary(pl.UTF-8):	Statyczna biblioteka LDL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static LDL library.

%description static -l pl.UTF-8
Statyczna biblioteka LDL.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/ldl

%{__make} -C Lib install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

install Include/*.h $RPM_BUILD_ROOT%{_includedir}/ldl

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt Doc/ChangeLog
%attr(755,root,root) %{_libdir}/libldl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libldl.so.0

%files devel
%defattr(644,root,root,755)
%doc Doc/ldl_userguide.pdf
%attr(755,root,root) %{_libdir}/libldl.so
%{_libdir}/libldl.la
%{_includedir}/ldl

%files static
%defattr(644,root,root,755)
%{_libdir}/libldl.a
