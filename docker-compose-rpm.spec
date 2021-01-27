%global _prefix /usr/local

Name:    docker-compose
Version: 1.28.0
Release: 1
Summary: Define and run multi-container applications with Docker https://docs.docker.com/compose/
Group:   Development Tools
License: ASL 2.0
Source0: https://github.com/docker/compose/releases/download/%{version}/docker-compose-Linux-x86_64

%description
Compose is a tool for defining and running multi-container Docker applications.
With Compose, you use a Compose file to configure your application's services.
Then, using a single command, you create and start all the services from your configuration.

%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
