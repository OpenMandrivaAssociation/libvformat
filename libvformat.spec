%define name	libvformat
%define version	1.13
%define release  7

%define major	0
%define libname %mklibname vformat %major

Name: 	 	%{name}
Summary: 	Library to read and write vcard files
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
Patch0:		%name-1.13-debian.diff
Patch1:		libvformat-1.13-fix-str-fmt.patch
URL:		https://sourceforge.net/projects/vformat/
License:	GPL
Group:		System/Libraries

%description
Library to read and write vcard files

%package -n 	%{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries

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
# since we currently don't have c2man
perl -p -i -e 's|install-data-hook|||g' doc/Makefile
%makeinstall_std
rm -fr $RPM_BUILD_ROOT/%_bindir/vformat


%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{libname}-devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.13-6mdv2011.0
+ Revision: 609785
- rebuild

* Sat Feb 20 2010 Funda Wang <fwang@mandriva.org> 1.13-5mdv2010.1
+ Revision: 508669
- fix str fmt

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Jul 27 2008 Thierry Vignaud <tv@mandriva.org> 1.13-4mdv2009.0
+ Revision: 250654
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.13-2mdv2008.1
+ Revision: 129180
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import libvformat


* Wed Dec 29 2004 Austin Acton <austin@mandrake.org> 1.13-2mdk
- steal debian patch to get header working
- add URL

* Wed Dec 29 2004 Austin Acton <austin@mandrake.org> 1.13-1mdk
- initial package
