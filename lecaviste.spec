%define name lecaviste
%define version 0.5
%define fileversion 0.5
%define release %mkrel 4
%define title Le Caviste

Summary: Wine cellar managing application
Name: %{name}
Version: %{version}
Release: %{release}
License: GPLv2
Group: Editors
Url: http://www.lecaviste.org
Source:  http://www.lecaviste.org/download/src/%{name}-%{fileversion}.tar.bz2

BuildRequires:	qt4-devel	>= 4.3
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

Requires: qt4-common >= 4.3
%if %mdkversion < 200901
Requires: qt4-database-plugin-sqlite-lib >= 4.3
%else
Requires: qt4-database-plugin-sqlite >= 4.3
%endif
			
%description
Wine cellar managing application

%prep
%setup -q -n %{name}

%build
%configure
%make

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Le Caviste
GenericName=Cellar Manager
GenericName[fr]=Gestionnaire de cave
Comment=Le Caviste - wine cellar manager
Exec=%{_bindir}/%{name} %f
Icon=%{name}
MapNotify=true
MimeType=application/x-lecaviste;
Terminal=false
Type=Application
StartupNotify=true
Categories=Qt;Utility;
EOF

mkdir -p %{buildroot}%{_datadir}/mimelnk/application
cat > %{buildroot}%{_datadir}/mimelnk/application/x-%{name}.desktop <<EOF
[Desktop Entry]
Type=MimeType
Encoding=UTF-8
MimeType=application/x-lecaviste
Icon=lecaviste-document
Patterns=*.cel;
Comment=Le Caviste File
Comment[fr]=Fichier Le Caviste
EOF

mkdir -p %{buildroot}/%{_iconsdir}
mkdir -p %{buildroot}/%{_miconsdir}
mkdir -p %{buildroot}/%{_liconsdir}
%__install %{_builddir}/%{name}/src/icons/lecaviste-16.png $RPM_BUILD_ROOT/%_miconsdir/%{name}.png
%__install %{_builddir}/%{name}/src/icons/lecaviste-32.png $RPM_BUILD_ROOT/%_iconsdir/%{name}.png
%__install %{_builddir}/%{name}/src/icons/lecaviste-document-32.png $RPM_BUILD_ROOT/%_iconsdir/%{name}-document.png
%__install %{_builddir}/%{name}/src/icons/lecaviste-48.png $RPM_BUILD_ROOT/%_liconsdir/%{name}.png

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}


%if %mdkversion < 200900
%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%files
%defattr(644,root,root,755)
%doc README TODO AUTHORS INSTALL LICENSE LICENSE-GPL NEWS
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mimelnk/application/x-%{name}.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_iconsdir}/%{name}-document.png
%{_miconsdir}/%name.png
%dir %{_datadir}/%{name}
%lang(fr) %{_datadir}/%{name}/%{name}_fr.qm
%lang(fr) %{_datadir}/%{name}/qt_fr.qm

