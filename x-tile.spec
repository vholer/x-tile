Name:           x-tile
Version:        3.1
Release:        1%{?dist}
Summary:        A GTK application to tile windows in different ways

License:        GPLv2+
URL:            http://www.giuspen.com/%{name}/
Source0:        http://www.giuspen.com/software/%{name}-%{version}.tar.xz
Source1:        %{name}.appdata.xml

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
Requires:       gtk3
Requires:       python3-gobject
Requires:       librsvg2
BuildArch:      noarch

%description
X-tile is a GTK application that allows you to select a number of windows and
tile them in different ways. This is especially useful for comparing products in
separate web pages, or for programmers referring to documentation as they are
programming.


%prep
%autosetup


%build
mkdir -p build/scripts-%{python3_version}/
%py3_build


%install
%py3_install
install -Dpm 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_metainfodir}/%{name}.appdata.xml

%find_lang %{name}


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/%{name}.appdata.xml


%files -f %{name}.lang
%license license
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{python3_sitelib}/*.egg-info
%{_mandir}/man1/%{name}.1.*
%{_metainfodir}/%{name}.appdata.xml


%changelog
* Fri Aug 09 2019 Vlastimil Holer <vlastimil.holer@gmail.com> - 3.1-1
- Update to 3.1

* Fri Aug 09 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.6-1
- Update to 2.6
- Add AppData file

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 03 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.5.1-1
- Update to 2.5.1
- Spec cleanup

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.5-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.5-9
- Remove obsolete scriptlets

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Sep 20 2012 Mohamed El Morabity <melmorabity@fedorapeople.org> - 2.5-1
- Update to 2.5

* Wed Jul 18 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.4-1
- Update to 2.4

* Sat Jul 14 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.3.1-1
- Update to 2.3.1
- Remove useless Provides/Obsoletes

* Mon Feb 20 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1

* Tue Jan 03 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.2-1
- Update to 2.2

* Tue Jul 19 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1-1
- Update to 2.1

* Sun Jul 10 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.0-1
- Update to 2.0
- There is now a single version of x-tile (no more "ng" version), since x-tile
  sets now an icon in the notification zone

* Sun Jun 26 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.9-1
- Update to 1.9
- Only provide the "no applet" version of x-tile since the applet is no loger
  supported by GNOME 3
- merge all former subpackages into a single one

* Thu Mar 17 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.8.6-1
- Update to 1.8.6

* Thu Mar 10 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.8.5-1
- Update to 1.8.5

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 08 2010 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.8.4-1
- Update to 1.8.4
- Split x-tile into three packages: x-tile-common, x-tile (GNOME application)
  and x-tile-ng (desktop-independant application)

* Mon Nov 22 2010 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.8.3-1
- Update to 1.8.3

* Tue Nov 09 2010 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.8.2-2
- Add missing BuildRequires python2

* Tue Nov 09 2010 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.8.2-1
- Update to 1.8.2 (no more manual installation, setup.py provided by this
  version)

* Thu Jun  3 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 1.5.2-1
- Update to 1.5.2

* Wed Jun  2 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 1.5-2
- Bump release

* Wed Jun  2 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 1.5-1
- Update to 1.5
- Drop x-tile-1.4-desktop.patch patch

* Fri May 14 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 1.4-3
- Remove useless Requires python-psutil
- Correct Icon entry in desktop file

* Sat Apr 24 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 1.4-2
- Use install instead of cp

* Mon Apr 12 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 1.4-1
- Update to 1.4

* Sun Mar  7 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 1.3.2-1
- Update to 1.3.2

* Mon Feb 22 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 1.3.1-1
- Update to 1.3.1
- Correct mispelling in %%description
- Update .spec from new Python guidelines

* Tue Jan 12 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 1.3-1
- Initial RPM release
