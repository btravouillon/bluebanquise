%{!?version: %define version 1.3.0}

%define roles_addons clone clustershell diskless grafana kernel_config lmod lvm nhc \
nic_nmcli ofed ofed_sm openldap_client openldap_server powerman prometheus_client \
prometheus_server report root_password singularity slurm sssd users_basic

Name:           arcticstack
Version:        %{version}
Release:        1%{?dist}
Summary:        Ansible roles Collections to install cluster stack

License:        MIT
URL:            https://www.bluebanquise.com
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Conflicts:      bluebanquise
# BuildRequires:
Requires:       ansible

%if 0%{?el8}
Requires:       python36
Requires:       python3-clustershell
Requires:       python3-jmespath
Requires:       python3-netaddr
%else
Requires:       python3 >= 3.6
Requires:       python36-clustershell
Requires:       python2-jmespath
Requires:       python-netaddr
%endif

%description
BlueBanquise is an opensource project, based on the wish to provide a simple
but flexible stack to deploy and manage cluster of servers or workstations.

The stack is using Ansible, and relies heavily on inventory merge
hash_behaviour and groups.


%prep
%autosetup

# Use default roles_path in ansible.cfg
sed -i -e 's/^roles_path/# roles_path/' ansible.cfg

# Delete CICD files
find roles/{core,addons} -type d -name 'molecule' -print0 \
 | xargs -0 rm -rf

# Remove dead symlink (../../roles)
rm -f resources/documentation/roles

# Define readme.rst as documentation
find roles/core -type f -name readme.rst \
  -printf "%%%doc %{_datadir}/ansible/roles/%%P\n" > rolesfiles.core

# Build list of files for each addon role
ROLES_ADDONS="%{roles_addons}"
for ROLE in ${ROLES_ADDONS//$'\n'/}; do
    find roles/addons/${ROLE} -type f -name readme.rst \
      -printf "%%%doc %{_datadir}/ansible/roles/${ROLE}/readme.rst\n" > rolesfiles.addons.${ROLE}
done

%build


%install
# Config
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
cp -a ansible.cfg %{buildroot}%{_sysconfdir}/%{name}/
cp -aL internal %{buildroot}%{_sysconfdir}/%{name}/

# Core roles
mkdir -p %{buildroot}%{_datadir}/ansible/roles
cp -aL roles/core/* %{buildroot}%{_datadir}/ansible/roles/

# Add-on roles
cp -aL roles/addons/* %{buildroot}%{_datadir}/ansible/roles/

# Executables
mkdir -p %{buildroot}%{_sbindir}
cp -a tools/arcticstack-playbook %{buildroot}%{_sbindir}/


%files -f rolesfiles.core
%defattr(-,root,root,-)
%license LICENSE
%doc CHANGELOG.md README.md resources/documentation/ resources/examples/
%dir %{_sysconfdir}/%{name}/
%dir %{_datadir}/ansible
%dir %{_datadir}/ansible/roles
# Core roles
%{_datadir}/ansible/roles/access_control
%{_datadir}/ansible/roles/bluebanquise
%{_datadir}/ansible/roles/conman
%{_datadir}/ansible/roles/dhcp_server
%{_datadir}/ansible/roles/display_tuning
%{_datadir}/ansible/roles/dns_client
%{_datadir}/ansible/roles/dns_server
%{_datadir}/ansible/roles/firewall
%{_datadir}/ansible/roles/hosts_file
%{_datadir}/ansible/roles/log_client
%{_datadir}/ansible/roles/log_server
%{_datadir}/ansible/roles/nfs_client
%{_datadir}/ansible/roles/nfs_server
%{_datadir}/ansible/roles/nic
%{_datadir}/ansible/roles/pxe_stack
%{_datadir}/ansible/roles/repositories_client
%{_datadir}/ansible/roles/repositories_server
%{_datadir}/ansible/roles/set_hostname
%{_datadir}/ansible/roles/ssh_master
%{_datadir}/ansible/roles/ssh_slave
%{_datadir}/ansible/roles/time
%config(noreplace) %{_sysconfdir}/%{name}/ansible.cfg
%config %{_sysconfdir}/%{name}/internal/
%attr(750,root,root) %{_sbindir}/arcticstack-playbook


# Create subpackages for each addon role
%{lua:
local name = rpm.expand("%{name}")
local version = rpm.expand("%{version}")

for role in string.gmatch(rpm.expand("%{roles_addons}"), "[%w_-]+")
do
  print("%package addons-" .. role .. "\n")
  print("Summary: Add-on role " .. role .. " for ArcticStack\n")
  print("Requires: " .. name .. " == " .. version .. "\n")
  print("%description addons-" .. role .. "\n")
  print("%files addons-" .. role .. " -f rolesfiles.addons." .. role .. "\n")
  print(rpm.expand("%{_datadir}") .. "/ansible/roles/" .. role .. "\n")
end}


%changelog
* Sat Mar 13 2021 Bruno Travouillon <devel@travouillon.fr>
- Initial spec file
