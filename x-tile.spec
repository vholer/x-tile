Name:           x-tile
Version:        2.0
Release:        1%{?dist}
Summary:        A GTK application to tile windows in different ways

Group:          User Interface/Desktops
License:        GPLv2+
URL:            http://www.giuspen.com/x-tile/
Source0:        http://www.giuspen.com/software/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  python-setuptools
Requires:       gnome-python2-gconf
Requires:       pygtk2
Provides:       %{name}-common = %{version}-%{release}
Provides:       %{name}-ng = %{version}-%{release}
Obsoletes:      %{name}-common < %{version}-%{release}
Obsoletes:      %{name}-ng < %{version}-%{release}
BuildArch:      noarch

%description
X-tile is a GTK application that allows you to select a number of windows and
tile them in different ways. This is especially useful for comparing products in
separate web pages, or for programmers referring to documentation as they are
programming.


%prep
%setup -q

# Remove import of cons module in setup.py, only needed to get the current
# version of x-tile and supported languages. The cons module calls the gtk one,
# which needs a running graphical session
sed -i "\|import cons|d; s|cons.VERSION|\"%{version}\"|" setup.py
LANGUAGES=$(sed -n "s/^AVAILABLE_LANGS = //p" modules/cons.py)
sed -i "s|cons.AVAILABLE_LANGS|$LANGUAGES|" setup.py


%build
%{__python} setup.py build


%install
%{__python} setup.py install \
  --no-compile \
  --root $RPM_BUILD_ROOT

# Remove useless header
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/glade/*.h

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%find_lang %{name}


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc license
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*.svg
%{python_sitelib}/*.egg-info


%changelog
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
