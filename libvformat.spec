%define name	libvformat
%define version	1.13
%define release  %mkrel 6

%define major	0
%define libname %mklibname vformat %major

Name: 	 	%{name}
Summary: 	Library to read and write vcard files
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
Patch0:		%name-1.13-debian.diff
Patch1:		libvformat-1.13-fix-str-fmt.patch
URL:		http://sourceforge.net/projects/vformat/
License:	GPL
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-buildroot

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
%patch0 -p1
%patch1 -p0

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
# since we currently don't have c2man
perl -p -i -e 's|install-data-hook|||g' doc/Makefile
%makeinstall_std
rm -fr $RPM_BUILD_ROOT/%_bindir/vformat

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la

