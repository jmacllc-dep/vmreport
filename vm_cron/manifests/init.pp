class vm_cron{

    file { '/etc/cron.hourly/vm.cron':
        ensure => present,
        source => 'puppet:///modules/vm_cron/vm.cron',
    }
}
