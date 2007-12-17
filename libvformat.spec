%define name	libvformat
%define version	1.13
%define release  %mkrel 2

%define major	0
%define libname %mklibname vformat %major

Name: 	 	%{name}
Summary: 	Library to read and write vcard files
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
Patch:		%name-1.13-debian.diff.bz2
URL:		http://sourceforge.net/projects/vformat/
License:	GPL
Group:		System/Libraries

%description
Library to read and write vcard files

%package -n 	%{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries
#Provides:	%name
#Obsoletes:	%name = %version-%release

%description -n %{libname}
Dynamic libraries from %name.

%package -n 	%{libname}-devel
Summary: 	Header files and static libraries from %name
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides: 	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes: 	%name-devel

%description -n %{libname}-devel
Libraries and includes files for developing programs based on %name.

%prep
%setup -q -n %name-%version.orig
%patch -p1

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
# since we currently don't have c2man
perl -p -i -e 's|install-data-hook|||g' doc/Makefile
%makeinstall
rm -fr $RPM_BUILD_ROOT/%_bindir/vformat

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la

