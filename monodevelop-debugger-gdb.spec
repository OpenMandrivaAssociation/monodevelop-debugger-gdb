Name:     	monodevelop-debugger-gdb
Version:	2.1.1
Release:	%mkrel 1
License:	MIT
BuildArch:      noarch
URL:		http://www.go-mono.com
Source0:	http://ftp.novell.com/pub/mono/sources/monodevelop-debugger-gdb/%{name}-%{version}.tar.bz2
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
