Name:           odroid-xu3-base
Version:        0.1.0
Release:        1%{?dist}
Summary:        Basic system configurations for ODROID-XU3

Group:          System Environment/Base
License:        BSD
URL:            http://odroid.com/dokuwiki/doku.php?id=en:odroid-xu3
Source0:        10-odroid.conf
Source1:        10-odroid-mali.rules
Source2:        10-odroid-shield.rules
Source3:        60-odroid-cec.rules
Source4:        odroid-audio.conf

BuildArch:      noarch

Requires:       udev
Requires:       dracut

%description
Basic system configurations for ODROID-XU3, such as firmware scripts and rules
for udev.

%prep

%build

%install
install -p -m0644 -D %{SOURCE0} %{buildroot}%{_prefix}/lib/dracut/dracut.conf.d/10-odroid.conf
install -p -m0644 -D %{SOURCE1} %{buildroot}%{_prefix}/lib/udev/rules.d/10-odroid-mali.rules
install -p -m0644 -D %{SOURCE2} %{buildroot}%{_prefix}/lib/udev/rules.d/10-odroid-shield.rules
install -p -m0644 -D %{SOURCE3} %{buildroot}%{_prefix}/lib/udev/rules.d/60-odroid-cec.rules
install -p -m0644 -D %{SOURCE4} %{buildroot}%{_datadir}/alsa/cards/odroid-audio.conf

%files
%{_prefix}/lib/dracut/dracut.conf.d/10-odroid.conf
%{_prefix}/lib/udev/rules.d/10-odroid-mali.rules
%{_prefix}/lib/udev/rules.d/10-odroid-shield.rules
%{_prefix}/lib/udev/rules.d/60-odroid-cec.rules
%{_datadir}/alsa/cards/odroid-audio.conf
%dir %{_datadir}/alsa
%dir %{_datadir}/alsa/cards

%changelog
* Tue May 12 2015 Scott K Logan <logans@cottsay.net> - 0.1.0-1
- Initial package
