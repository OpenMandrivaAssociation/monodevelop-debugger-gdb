Name:     	monodevelop-debugger-gdb
Version:	2.8.5.1
Release:	%mkrel 1
License:	MIT
BuildArch:      noarch
URL:		http://www.go-mono.com
Source0:	http://download.mono-project.com/sources/%name/%name-%version.tar.bz2
BuildRequires:  monodevelop >= %version
BuildRequires:  mono-devel
Requires: gdb
Summary:	Monodevelop GDB Addin
Group:		Development/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Monodevelop Addin to integrate the GNU debugger.


%prep
%setup -q

%build
./configure --prefix=%_prefix
%make

%install
rm -rf "$RPM_BUILD_ROOT" %name.lang
%makeinstall_std

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-, root, root)
%_prefix/lib/monodevelop/AddIns/MonoDevelop.Debugger/


%changelog
* Mon Jan 23 2012 Götz Waschk <waschk@mandriva.org> 2.8.5.1-1mdv2012.0
+ Revision: 766763
- update to new version 2.8.5.1

* Thu Jan 05 2012 Götz Waschk <waschk@mandriva.org> 2.8.5-1
+ Revision: 757877
- update to new version 2.8.5

* Thu Nov 17 2011 Götz Waschk <waschk@mandriva.org> 2.8.2-1
+ Revision: 731188
- update to new version 2.8.2

* Mon Oct 10 2011 Götz Waschk <waschk@mandriva.org> 2.8-1
+ Revision: 703991
- new version
- new source URL

* Thu Sep 08 2011 Götz Waschk <waschk@mandriva.org> 2.6-1
+ Revision: 698947
- new version
- new source URL

* Thu Jul 14 2011 Götz Waschk <waschk@mandriva.org> 2.4-2
+ Revision: 689965
- rebuild

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 2.4-1mdv2011.0
+ Revision: 550716
- new version

* Thu Feb 04 2010 Götz Waschk <waschk@mandriva.org> 2.2.1-1mdv2010.1
+ Revision: 500675
- update to new version 2.2.1

* Tue Dec 15 2009 Götz Waschk <waschk@mandriva.org> 2.2-1mdv2010.1
+ Revision: 478914
- update to new version 2.2

* Fri Dec 11 2009 Götz Waschk <waschk@mandriva.org> 2.1.2-1mdv2010.1
+ Revision: 476490
- update to new version 2.1.2

* Tue Nov 10 2009 Götz Waschk <waschk@mandriva.org> 2.1.1-1mdv2010.1
+ Revision: 464199
- update to new version 2.1.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 2.0-2mdv2010.0
+ Revision: 440066
- rebuild

* Tue Mar 31 2009 Götz Waschk <waschk@mandriva.org> 2.0-1mdv2009.1
+ Revision: 362823
- new version

* Tue Mar 17 2009 Götz Waschk <waschk@mandriva.org> 1.9.3-1mdv2009.1
+ Revision: 356878
- update to new version 1.9.3

* Thu Feb 12 2009 Götz Waschk <waschk@mandriva.org> 1.9.2-1mdv2009.1
+ Revision: 339835
- new version
- remove pkgconfig file

* Mon Nov 24 2008 Götz Waschk <waschk@mandriva.org> 1.9.1-1mdv2009.1
+ Revision: 306279
- import monodevelop-debugger-gdb


