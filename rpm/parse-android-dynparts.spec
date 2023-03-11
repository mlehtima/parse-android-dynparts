Name:       parse-android-dynparts
Summary:    Android Dynamic Partitions mount program
Version:    0.0.1
Release:    1
License:    ASL 2.0
URL:        https://github.com/mlehtima/parse-android-dynparts
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig(openssl)

%description
Allows mounting Android Dynamic Partitions (a.k.a. super.img) files on Linux
using "dmsetup create".

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
mkdir -p _build
pushd _build
cmake ..

%make_build
popd

%install
mkdir -p %{buildroot}%{_bindir}
install -m0755 _build/parse-android-dynparts %{buildroot}%{_bindir}

%files
%defattr(-,root,root,-)
%license LICENSE
%{_bindir}/parse-android-dynparts
