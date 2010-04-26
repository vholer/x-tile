Name:           x-tile
Version:        1.4
Release:        2%{?dist}
Summary:        A GNOME panel applet to tile windows

Group:          User Interface/Desktops
License:        GPLv2+
URL:            http://open.vitaminap.it/en/x_tile.htm
Source0:        http://open.vitaminap.it/software/%{name}_%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  desktop-file-utils
Requires:       gnome-python2-applet
Requires:       gnome-python2-gconf
# Required to own /usr/lib/bonobo/servers
Requires:       libbonobo
Requires:       python-psutil
BuildArch:      noarch

%description
X-tile is a GNOME applet for your panel (or optionally a standalone application)
that allows you to select a number of windows and tile them in different
ways. This is especially useful for comparing products in separate web pages, or
for programmers referring to documentation as they are programming.


%prep
%setup -q -n %{name}
chmod a-x {glade,linux}/*

# Remove shebangs
pushd modules
for file in cons.py core.py globs.py support.py; do
  sed -i.orig -e 1d $file && \
  touch -r $file.orig $file && \
  rm $file.orig
done
popd


%build


%install
rm -rf $RPM_BUILD_ROOT

install -Dp -m 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dp -m 0644  linux/%{name}.server $RPM_BUILD_ROOT%{_prefix}/lib/bonobo/servers/%{name}.server
install -Dp -m 0644  linux/%{name}.svg $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.svg
install -Dp -m 0644 linux/%{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
pushd glade
for file in *.{glade,png,svg}; do
  install -Dp -m 0644 $file $RPM_BUILD_ROOT%{_datadir}/%{name}/glade/$file
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
%doc license readme linux/multiple-monitors-readme
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.svg
%{_prefix}/lib/bonobo/servers/*.server


%changelog
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
