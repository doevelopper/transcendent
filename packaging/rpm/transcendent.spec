Name:           transcendent
Version:        1.0.0
Release:        1%{?dist}
Summary:        Comprehensive application for user and transaction management

License:        MIT
URL:            https://github.com/yourorg/transcendent
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  postgresql-devel
BuildRequires:  bazel

Requires:       postgresql-libs
Requires:       openssl-libs

%description
Transcendent is a high-performance C++ application designed for managing
users and transactions with enterprise-grade security and scalability.

Features include:
- RESTful API for user and transaction management
- JWT-based authentication and authorization
- PostgreSQL database integration
- Comprehensive logging and monitoring
- Docker and Kubernetes deployment support

%prep
%autosetup

%build
bazel build //src/main/cpp:transcendent

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/transcendent
mkdir -p %{buildroot}%{_var}/log/transcendent
mkdir -p %{buildroot}%{_unitdir}

# Install binary
install -m 755 bazel-bin/src/main/cpp/transcendent %{buildroot}%{_bindir}/transcendent

# Install configuration files
cp -r config/environments/production/* %{buildroot}%{_sysconfdir}/transcendent/

# Install systemd service file
install -m 644 packaging/rpm/transcendent.service %{buildroot}%{_unitdir}/transcendent.service

%post
%systemd_post transcendent.service

# Create transcendent user if it doesn't exist
if ! getent passwd transcendent > /dev/null; then
    useradd -r -s /sbin/nologin -d /usr/share/transcendent transcendent
fi

# Set ownership and permissions
chown -R transcendent:transcendent %{_var}/log/transcendent
chmod 755 %{_var}/log/transcendent

%preun
%systemd_preun transcendent.service

%postun
%systemd_postun_with_restart transcendent.service

%files
%license LICENSE
%doc README.md
%{_bindir}/transcendent
%config(noreplace) %{_sysconfdir}/transcendent/*
%{_unitdir}/transcendent.service
%attr(755,transcendent,transcendent) %dir %{_var}/log/transcendent

%changelog
* Mon Jan 01 2024 Transcendent Team <team@transcendent.example.com> - 1.0.0-1
- Initial RPM release
- Features user and transaction management
- RESTful API with JWT authentication
- PostgreSQL database integration