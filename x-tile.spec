%if ! (0%{?fedora} > 12)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

Name:           x-tile
Version:        1.8.4
Release:        1%{?dist}
Summary:        A GNOME panel applet to tile windows in different ways

Group:          User Interface/Desktops
License:        GPLv2+
URL:            http://www.giuspen.com/x-tile/
Source0:        http://www.giuspen.com/software/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  desktop-file-utils
BuildRequires:  python2
Requires:       gnome-python2-applet
# Owns /usr/lib/bonobo/servers
Requires:       libbonobo
Requires:       %{name}-common = %{version}-%{release}
BuildArch:      noarch

%description
X-tile is a GNOME applet for your panel (or optionally a standalone application)
that allows you to select a number of windows and tile them in different
ways. This is especially useful for comparing products in separate web pages, or
for programmers referring to documentation as they are programming.


%package common
Summary:        X-tile common files
Group:          User Interface/Desktops
Requires:       gnome-python2-gconf
Requires:       pygtk2
BuildArch:      noarch

%description common
X-tile is a GNOME applet for your panel (or optionally a standalone application)
that allows you to select a number of windows and tile them in different
ways. This is especially useful for comparing products in separate web pages, or
for programmers referring to documentation as they are programming.

This package contains all the common files needed by x-tile or x-tile-ng.


%package ng
Summary:        A GTK application to tile windows in different ways
Group:          User Interface/Desktops
Requires:       %{name}-common = %{version}-%{release}
BuildArch:      noarch

%description ng
X-tile is a GNOME applet for your panel (or optionally a standalone application)
that allows you to select a number of windows and tile them in different
ways. This is especially useful for comparing products in separate web pages, or
for programmers referring to documentation as they are programming.

This package contains a desktop-independent version of X-tile, which doesn't
require the GNOME panel and works only without the applet


%prep
%setup -q

# Remove import of cons module in setup.py, only needed to get the current
# version of x-tile and supported languages. The cons module calls the gtk one,
# which needs a running graphical session
sed -i "\|import cons|d; s|cons.VERSION|\"%{version}\"|" setup.py
LANGUAGES=$(sed -n "s/^AVAILABLE_LANGS = //p" modules/cons.py)
sed -i "s|cons.AVAILABLE_LANGS|$LANGUAGES|" setup.py

# Fix permissions
chmod 0644 glade/*.svg linux/*


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
  --skip-build \
  --root $RPM_BUILD_ROOT

# Install x-tile-ng executable and desktop file
install -Dp %{name}-ng $RPM_BUILD_ROOT%{_bindir}/%{name}-ng
install -Dpm 0644 linux/%{name}-ng.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-ng.desktop

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-ng.desktop

%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_prefix}/lib/bonobo/servers/*.server


%files -f %{name}.lang common
%defattr(-,root,root,-)
%doc license
%{_datadir}/%{name}
%{_datadir}/pixmaps/*.svg
%{python_sitelib}/*.egg-info


%files ng
%defattr(-,root,root,-)
%{_bindir}/%{name}-ng
%{_datadir}/applications/%{name}-ng.desktop


%changelog
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
