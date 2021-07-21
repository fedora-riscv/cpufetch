Name: cpufetch
Summary: Simple tool for determining CPU architecture
License: MIT

Version: 0.98
Release: 2%{?dist}

URL: https://github.com/Dr-Noob/cpufetch
Source0: %{URL}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make

# Supports only x86_64 and ARM
ExclusiveArch: %{arm} aarch64 x86_64


%description
%{name} is a simple, yet fancy, CPU architecture fetching tool.
It currently supports x86_64 CPUs (both Intel and AMD) and ARM.


%prep
%setup -q


%build
%set_build_flags
%make_build


%install
%make_install

# "make install" installs the LICENSE file as well
rm %{buildroot}%{_datadir}/licenses/cpufetch-git/LICENSE


%files
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.98-1
- Update to v0.98
- Use "make install" instead of copying files manually

* Mon Apr 05 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.94-2
- Preserve timestamps when installing

* Sat Apr 03 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.94-1
- Initial packaging
