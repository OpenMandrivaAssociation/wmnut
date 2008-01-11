%define name 		wmnut
%define version 	0.62
%define release %mkrel 2
%define summary		A wmaker dock app that displays UPS statistics from NUT's upsd

Name: 			%{name}
Summary: 		%{summary}
Version: 		%{version}
Release: 		%{release}
License:		GPL
URL:			http://osx.freshmeat.net/projects/wmnut/
Source: 		http://wmnut.mgeups.org/files/%{name}-%{version}.tar.bz2
Patch0:         wmnut-0.62-lib64.patch
Group:			Graphical desktop/WindowMaker
BuildRequires:		nut-devel >= 2.0.0
BuildRequires:		libx11-devel
BuildRoot: 		%{_tmppath}/%{name}-%{version}-buildroot

%description
A wmaker dock app that displays UPS statistics from NUT's upsd.
WMNUT monitors UPS statistics through the NUT (Network UPS Tools,
www.exploits.org/nut) framework on Linux and other systems.  This information,
presented in a nice visual format, can be invaluable on stations using an UPS.

%prep
%setup -q
%patch0 -p0 -b .lib64

%build
aclocal
automake -a
autoconf
%configure

%make

%install
[ -d %buildroot ] && rm -rf %buildroot

%makeinstall

%{__strip} %buildroot/%{_bindir}/*

install -D -m 644 icons/%{name}-mdk-16.png %buildroot%{_miconsdir}/%{name}.png
install -D -m 644 icons/%{name}-mdk-32.png %buildroot%{_iconsdir}/%{name}.png
install -D -m 644 icons/%{name}-mdk-48.png %buildroot%{_liconsdir}/%{name}.png


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=WMNut
Comment=UPS monitoring in a dockapp
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-System-Monitoring;
EOF





%clean
rm -rf %buildroot

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr (-,root,root)
%doc AUTHORS BUGS ChangeLog COPYING INSTALL NEWS README TODO
%_bindir/wmnut
%{_datadir}/applications/mandriva-%{name}.desktop
%_iconsdir/*
%_mandir/man1/wmnut.*

