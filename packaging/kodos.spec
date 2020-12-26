Name:           kodos
Version:        2.5.2
Release:        1%{?dist}
Summary:        Visual regular expression editor

Group:          Development/Tools
# No version specified.
License:        GPL+
URL:            http://kodos.sourceforge.net/
Source0:        https://github.com/sergiomb2/kodos/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  python3-PyQt4-devel

Requires:       python3-PyQt4


%description
Kodos is a visual regular expression editor and debugger written in Python.


%prep
%setup -q


%build
%py3_build


%install
%py3_install

rm -f %{buildroot}%{python3_sitelib}/kodos/py2exe*
mkdir -p -m 0755 %{buildroot}%{_datadir}/pixmaps
install -m 0644 images/kodos_icon.png %{buildroot}%{_datadir}/pixmaps/
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
    kodos.desktop


%files
%doc CHANGELOG.txt
%license LICENSE.txt
%{_bindir}/*
%{_datadir}/kodos
%{python3_sitelib}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*


%changelog
* Fri Dec 25 2020 Sérgio Basto <sergio@serjux.com> - 2.5.2-1
- Update to 2.5.2 (pyhton3 version)

* Fri Dec 25 2020 Sérgio Basto <sergio@serjux.com> - 2.5.1-1
- Update to 2.5.1 (teythoon branch)

* Sun Jun 24 2018 Sérgio Basto <sergio@serjux.com> - 2.5.0-1
- Unofficial Kodos 2.5.0 but with pyqt4

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.9-19
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar  6 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 2.4.9-14
- Remove vendor prefix from desktop files in F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 2.4.9-9
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.4.9-6
- Rebuild for Python 2.6

* Tue Aug  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.4.9-5
- fix license tag

* Sat Jun 16 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.4.9-4
- Remove leftover useless Requires.

* Sun Jun 10 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.4.9-3
- Don't add X-Fedora to desktop-file-install
- Don't run update-desktop-database, since there's no MimeType to worry about

* Sun Mar 11 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.4.9-2
- BR desktop-file-utils
- Set permissions correctly to appease rpmlint

* Mon Jan 29 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.4.9-1
- Initial packaging for Extras.
