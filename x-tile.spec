Name:           x-tile
Version:        1.5.2
Release:        1%{?dist}
Summary:        A GNOME panel applet to tile windows

Group:          User Interface/Desktops
License:        GPLv2+
URL:            http://open.vitaminap.it/en/x_tile.htm
Source0:        http://open.vitaminap.it/software/%{name}-%{version}.tar.gz
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

# Remove shebangs
for file in modules/*.py; do
  sed -i.orig -e 1d $file && \
  touch -r $file.orig $file && \
  rm $file.orig
done


%build


%install
rm -rf $RPM_BUILD_ROOT

install -Dpm 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dpm 0644  linux/%{name}.server $RPM_BUILD_ROOT%{_prefix}/lib/bonobo/servers/%{name}.server
install -Dpm 0644  linux/%{name}.svg $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.svg
desktop-file-install \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
  linux/%{name}.desktop


pushd glade
for file in *.{glade,png,svg}; do
  install -Dpm 0644 $file $RPM_BUILD_ROOT%{_datadir}/%{name}/glade/$file
done
popd

pushd modules
for file in *.py; do
install -Dp -m 0644 $file $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/$file
done
popd

install -d $RPM_BUILD_ROOT%{_datadir}/locale
cp -a locale/{fr,it,ru,zh_TW} $RPM_BUILD_ROOT%{_datadir}/locale

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc license readme
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.svg
%{_prefix}/lib/bonobo/servers/*.server


%changelog
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
