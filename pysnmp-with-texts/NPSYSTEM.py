#
# PySNMP MIB module NPSYSTEM (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NPSYSTEM
# Produced by pysmi-0.3.4 at Wed May  1 14:24:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, NotificationType, Counter64, IpAddress, Unsigned32, Integer32, iso, Counter32, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "NotificationType", "Counter64", "IpAddress", "Unsigned32", "Integer32", "iso", "Counter32", "Bits", "ModuleIdentity")
TextualConvention, RowStatus, DisplayString, DateAndTime, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "DateAndTime", "MacAddress")
zhoneWtn, = mibBuilder.importSymbols("Zhone", "zhoneWtn")
npsystem = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11))
if mibBuilder.loadTexts: npsystem.setLastUpdated('200711260000Z')
if mibBuilder.loadTexts: npsystem.setOrganization('Zhone Technologies MIB Working Group Other information about group editing the MIB')
if mibBuilder.loadTexts: npsystem.setContactInfo('Zhone Technologies, Inc. Florida Design Center 8545 126th Avenue North Largo, FL 33773 www.zhone.com General Comments to: largo-mibwg-team@zhone.com')
if mibBuilder.loadTexts: npsystem.setDescription('This file defines the private Enterprise MIB extensions. This file specifies the configuration & status of the System module.')
systemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1))
serialNumber = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('current')
if mibBuilder.loadTexts: serialNumber.setDescription('serial no. of the device')
firmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: firmwareVersion.setStatus('current')
if mibBuilder.loadTexts: firmwareVersion.setDescription('firmware version')
systemDate = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemDate.setStatus('current')
if mibBuilder.loadTexts: systemDate.setDescription('Set the system date')
systemTime = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemTime.setStatus('current')
if mibBuilder.loadTexts: systemTime.setDescription('Set the time.')
systemUpTime = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUpTime.setStatus('current')
if mibBuilder.loadTexts: systemUpTime.setDescription('Tell how long the system has been running')
systemReboot = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemReboot.setStatus('current')
if mibBuilder.loadTexts: systemReboot.setDescription('Set 1 to reboot the box')
systemHostName = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemHostName.setStatus('current')
if mibBuilder.loadTexts: systemHostName.setDescription('configure host name')
systemDomainName = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemDomainName.setStatus('current')
if mibBuilder.loadTexts: systemDomainName.setDescription('configure domain name.')
systemPrimaryDnsServer = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemPrimaryDnsServer.setStatus('current')
if mibBuilder.loadTexts: systemPrimaryDnsServer.setDescription('The IP address of the DNS server.')
systemSecondaryDnsServer = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 10), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemSecondaryDnsServer.setStatus('current')
if mibBuilder.loadTexts: systemSecondaryDnsServer.setDescription('The IP address of the DNS server.')
systemGateway = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 11), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemGateway.setStatus('current')
if mibBuilder.loadTexts: systemGateway.setDescription('The IP address of the gateway')
systemRemoteSyslogStatus = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemRemoteSyslogStatus.setStatus('current')
if mibBuilder.loadTexts: systemRemoteSyslogStatus.setDescription('configure the remote syslog status.')
systemRemoteSyslogServer = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 13), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemRemoteSyslogServer.setStatus('current')
if mibBuilder.loadTexts: systemRemoteSyslogServer.setDescription('configure the remote syslog server.')
systemSyslogLocalStatus = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemSyslogLocalStatus.setStatus('current')
if mibBuilder.loadTexts: systemSyslogLocalStatus.setDescription('configure the local syslog status.')
systemSyslogMaxSize = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemSyslogMaxSize.setStatus('current')
if mibBuilder.loadTexts: systemSyslogMaxSize.setDescription('configure the max syslog size.')
systemSyslogRotateNum = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemSyslogRotateNum.setStatus('current')
if mibBuilder.loadTexts: systemSyslogRotateNum.setDescription('configure the rotate num.')
systemTimezone = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 17), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemTimezone.setStatus('current')
if mibBuilder.loadTexts: systemTimezone.setDescription('configure the time zone.')
systemDaylightSavingStatus = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemDaylightSavingStatus.setStatus('current')
if mibBuilder.loadTexts: systemDaylightSavingStatus.setDescription('configure the day light saving status.')
systemNtpServer = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 19), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemNtpServer.setStatus('current')
if mibBuilder.loadTexts: systemNtpServer.setDescription('configure the ntp server.')
systemNtpStatus = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemNtpStatus.setStatus('current')
if mibBuilder.loadTexts: systemNtpStatus.setDescription('configure the ntp status.')
systemAction = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 21), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemAction.setStatus('current')
if mibBuilder.loadTexts: systemAction.setDescription('action parameter to handle the action on other scalars')
systemRemoteSyslogServerPort = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 22), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemRemoteSyslogServerPort.setStatus('current')
if mibBuilder.loadTexts: systemRemoteSyslogServerPort.setDescription('Port no of remote syslog server')
systemServicesTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 23), )
if mibBuilder.loadTexts: systemServicesTable.setStatus('current')
if mibBuilder.loadTexts: systemServicesTable.setDescription('Table to hold system services. The SNMP agent will populate the rows of this table, depending upon the services for which the system module lets set the status.')
systemServicesTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 23, 1), ).setIndexNames((0, "NPSYSTEM", "serviceName"))
if mibBuilder.loadTexts: systemServicesTableEntry.setStatus('current')
if mibBuilder.loadTexts: systemServicesTableEntry.setDescription('One table entry per service')
serviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 23, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceName.setStatus('current')
if mibBuilder.loadTexts: serviceName.setDescription('Name of the service.')
serviceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 23, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: serviceStatus.setStatus('current')
if mibBuilder.loadTexts: serviceStatus.setDescription('Status of the service.')
serviceAction = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 23, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: serviceAction.setStatus('current')
if mibBuilder.loadTexts: serviceAction.setDescription('action parameter to handle the action')
mibBuilder.exportSymbols("NPSYSTEM", serviceStatus=serviceStatus, PYSNMP_MODULE_ID=npsystem, systemRemoteSyslogStatus=systemRemoteSyslogStatus, npsystem=npsystem, systemServicesTableEntry=systemServicesTableEntry, serialNumber=serialNumber, systemDomainName=systemDomainName, systemRemoteSyslogServer=systemRemoteSyslogServer, serviceName=serviceName, systemHostName=systemHostName, systemNtpServer=systemNtpServer, systemReboot=systemReboot, systemAction=systemAction, systemGateway=systemGateway, systemPrimaryDnsServer=systemPrimaryDnsServer, systemSecondaryDnsServer=systemSecondaryDnsServer, systemObjects=systemObjects, firmwareVersion=firmwareVersion, systemDate=systemDate, systemSyslogLocalStatus=systemSyslogLocalStatus, serviceAction=serviceAction, systemUpTime=systemUpTime, systemTimezone=systemTimezone, systemTime=systemTime, systemRemoteSyslogServerPort=systemRemoteSyslogServerPort, systemServicesTable=systemServicesTable, systemSyslogMaxSize=systemSyslogMaxSize, systemDaylightSavingStatus=systemDaylightSavingStatus, systemNtpStatus=systemNtpStatus, systemSyslogRotateNum=systemSyslogRotateNum)