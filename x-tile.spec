%if ! (0%{?fedora} > 12)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

Name:           x-tile
Version:        1.8.2
Release:        1%{?dist}
Summary:        A GNOME panel applet to tile windows in different ways

Group:          User Interface/Desktops
License:        GPLv2+
URL:            http://www.giuspen.com/x-tile/
Source0:        http://www.giuspen.com/software/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  desktop-file-utils
Requires:       gnome-python2-applet
Requires:       gnome-python2-gconf
# Owns /usr/lib/bonobo/servers
Requires:       libbonobo
BuildArch:      noarch

%description
X-tile is a GNOME applet for your panel (or optionally a standalone application)
that allows you to select a number of windows and tile them in different
ways. This is especially useful for comparing products in separate web pages, or
for programmers referring to documentation as they are programming.


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

# Remove useless header x-tile.glade.h
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/glade/x-tile.glade.h

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc license
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.svg
%{_prefix}/lib/bonobo/servers/*.server
%{python_sitelib}/*.egg-info


%changelog
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
