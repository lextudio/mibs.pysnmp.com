#
# PySNMP MIB module Dell-VRTX-DHCPCL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-VRTX-DHCPCL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:57:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("Dell-VRTX-MIB", "rnd")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, NotificationType, TimeTicks, Counter64, Bits, Gauge32, MibIdentifier, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "TimeTicks", "Counter64", "Bits", "Gauge32", "MibIdentifier", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "iso", "Unsigned32")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
rlDhcpCl = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 76))
rlDhcpCl.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlDhcpCl.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlDhcpCl.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlDhcpCl.setOrganization('Dell')
if mibBuilder.loadTexts: rlDhcpCl.setContactInfo('www.dell.com')
if mibBuilder.loadTexts: rlDhcpCl.setDescription('This private MIB module defines DHCP CL private MIBs.')
rlDhcpClActionTable = MibTable((1, 3, 6, 1, 4, 1, 89, 76, 3), )
if mibBuilder.loadTexts: rlDhcpClActionTable.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClActionTable.setDescription(' The (conceptual) table mentione IP address which must be released/renewed on the interface.')
rlDhcpClActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 76, 3, 1), ).setIndexNames((0, "Dell-VRTX-DHCPCL-MIB", "rlDhcpClActionIfIndex"))
if mibBuilder.loadTexts: rlDhcpClActionEntry.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClActionEntry.setDescription('An entry (conceptual row) in dhcpClActionTable.')
rlDhcpClActionIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClActionIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClActionIfIndex.setDescription(' The interface which the action is implemented for or NULL if it implemented for all device. ')
rlDhcpClActionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlDhcpClActionStatus.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClActionStatus.setDescription('The status of this entry. Creating the entry renewing Dhcp address on the interface; destroying the entry release Dhcp address on the interface.')
rlDhcpClActionHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 3, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlDhcpClActionHostName.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClActionHostName.setDescription(' This option specifies the name of the client.')
rlDhcpApprovalEnabled = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpApprovalEnabled.setStatus('current')
if mibBuilder.loadTexts: rlDhcpApprovalEnabled.setDescription('DHCP Approval feature status - enable (True) or desable (False). Must be True only if DHCP Approval supported, device has only one ip interface and default ip exist.')
rlDhcpApprovalWaitingTable = MibTable((1, 3, 6, 1, 4, 1, 89, 76, 5), )
if mibBuilder.loadTexts: rlDhcpApprovalWaitingTable.setStatus('current')
if mibBuilder.loadTexts: rlDhcpApprovalWaitingTable.setDescription('IP addresses waiting for approval.')
rlDhcpApprovalWaitingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 76, 5, 1), ).setIndexNames((0, "Dell-VRTX-DHCPCL-MIB", "rlDhcpApprovalWaitingIfIndex"))
if mibBuilder.loadTexts: rlDhcpApprovalWaitingEntry.setStatus('current')
if mibBuilder.loadTexts: rlDhcpApprovalWaitingEntry.setDescription('An entry in rlDhcpApprovalWaitingTable.')
rlDhcpApprovalWaitingIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 5, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpApprovalWaitingIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlDhcpApprovalWaitingIfIndex.setDescription('IP interface ifIndex.')
rlDhcpApprovalWaitingAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 5, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpApprovalWaitingAddress.setStatus('current')
if mibBuilder.loadTexts: rlDhcpApprovalWaitingAddress.setDescription('IP Address waiting for approval.')
rlDhcpApprovalWaitingMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 5, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpApprovalWaitingMask.setStatus('current')
if mibBuilder.loadTexts: rlDhcpApprovalWaitingMask.setDescription('Mask waiting for approval.')
rlDhcpApprovalWaitingGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 5, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpApprovalWaitingGateway.setStatus('current')
if mibBuilder.loadTexts: rlDhcpApprovalWaitingGateway.setDescription('Default gateway of received address.')
rlDhcpApprovalActionTable = MibTable((1, 3, 6, 1, 4, 1, 89, 76, 6), )
if mibBuilder.loadTexts: rlDhcpApprovalActionTable.setStatus('current')
if mibBuilder.loadTexts: rlDhcpApprovalActionTable.setDescription('Action for waiting ip address (approve/decline).')
rlDhcpApprovalActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 76, 6, 1), ).setIndexNames((0, "Dell-VRTX-DHCPCL-MIB", "rlDhcpApprovalActionIfIndex"), (0, "Dell-VRTX-DHCPCL-MIB", "rlDhcpApprovalActionAddress"), (0, "Dell-VRTX-DHCPCL-MIB", "rlDhcpApprovalActionMask"))
if mibBuilder.loadTexts: rlDhcpApprovalActionEntry.setStatus('current')
if mibBuilder.loadTexts: rlDhcpApprovalActionEntry.setDescription('An entry in rlDhcpApprovalActionTable.')
rlDhcpApprovalActionIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 6, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpApprovalActionIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlDhcpApprovalActionIfIndex.setDescription('IP interface ifIndex.')
rlDhcpApprovalActionAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 6, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpApprovalActionAddress.setStatus('current')
if mibBuilder.loadTexts: rlDhcpApprovalActionAddress.setDescription('IP Address.')
rlDhcpApprovalActionMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 6, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpApprovalActionMask.setStatus('current')
if mibBuilder.loadTexts: rlDhcpApprovalActionMask.setDescription('IP Address mask.')
rlDhcpApprovalActionApprove = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 6, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpApprovalActionApprove.setStatus('current')
if mibBuilder.loadTexts: rlDhcpApprovalActionApprove.setDescription('Approve or decline ip address.')
rlDhcpClCommandTable = MibTable((1, 3, 6, 1, 4, 1, 89, 76, 7), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClCommandTable.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClCommandTable.setDescription('Action MIB for DHCP Renew command.')
rlDhcpClCommandEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 76, 7, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlDhcpClCommandEntry.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClCommandEntry.setDescription('The row definition for this table.')
rlDhcpClCommandAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("renew", 1), ("renewForceAutoconfig", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClCommandAction.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClCommandAction.setDescription('Action to apply. When the field is renew_force_autoconfig the meaning is that every time when DHCP option 67 is received, the configuration is downloaded from DHCP server. The default value is false.')
rlDhcpClConfigurationFileName = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClConfigurationFileName.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClConfigurationFileName.setDescription('The configuration file name that loaded into the device. The filename is a relative path on the TFTP server, without the server IP address.')
rlDhcpClOption67Enable = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClOption67Enable.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClOption67Enable.setDescription('Defines whether the configuration file can be downloaded from DHCP packet option 67.')
rlDhcpClManualTftpServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 10), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClManualTftpServerAddress.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClManualTftpServerAddress.setDescription('Manually configured TFTP server IP Address.')
rlDhcpClSelectedTftpServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 11), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClSelectedTftpServerAddress.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClSelectedTftpServerAddress.setDescription('Currently selected TFTP server IP Address.')
rlDhcpClSelectedTftpServerAddressOrigin = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("sname", 1), ("option66", 2), ("option150", 3), ("option129", 4), ("siaddr", 5), ("manual", 6), ("unknown", 7), ("none", 8), ("optionv6-59", 9), ("broadcastReply", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClSelectedTftpServerAddressOrigin.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClSelectedTftpServerAddressOrigin.setDescription("Currently selected TFTP server IP Address's origin")
rlDhcpClManualConfigurationFileName = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 13), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClManualConfigurationFileName.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClManualConfigurationFileName.setDescription('The manually configured file name.')
rlDhcpClSelectedConfigurationFileName = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClSelectedConfigurationFileName.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClSelectedConfigurationFileName.setDescription('The selected configuration file name.')
rlDhcpClSelectedConfigurationFileNameOrigin = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("file", 1), ("option67", 2), ("manual", 3), ("none", 4), ("hostname", 5), ("defaultConfigFile", 6), ("optionv6-60", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClSelectedConfigurationFileNameOrigin.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClSelectedConfigurationFileNameOrigin.setDescription('The selected configuration files name origin.')
rlDhcpClEnabledByDefaultRemovedIfindex = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClEnabledByDefaultRemovedIfindex.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClEnabledByDefaultRemovedIfindex.setDescription('DHCP Client flag is relevant when host parameter dhcp_client_active_on_start is TRUE. If the MIB has non zero value the meaning is that DHCP client has removed from configuration by the user on the interface and signs to application not to add DHCP client entry. Otherwise (zero value) - the meaning is that DHCP client entry must be added. ')
rlDhcpClAutoUpdateEnabled = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 17), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClAutoUpdateEnabled.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClAutoUpdateEnabled.setDescription('Setting this MIB value to True/False enables/disables DHCP auto-update process in the device (through option 125).')
rlDhcpClAutoUpdateStatus = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))).clone(namedValues=NamedValues(("noData", 1), ("openingIndirectFile", 2), ("downloadedIndirectFile", 3), ("startDownloadImageFile", 4), ("failedToDownloadImageFile", 5), ("quitFileContentsLenZero", 6), ("quitImageFileNameLenZero", 7), ("quitVersionAlreadyUpdated", 8), ("quitIndirectFileNotFound", 9), ("quitImageFileNotFound", 10), ("quitImageVersionNotSupported", 11), ("quitNoTftpOutgoingInterface", 12), ("quitUsbSetupFileOpenError", 13), ("quitUsbSetupFileFormatError", 14), ("quitUsbSetupFileReadWriteError", 15), ("quitUsbSetupFileSetIpAddrError", 16), ("quitUsbSetupFileImageFileNotExist", 17), ("quitUsbSetupFileConfigFileNotExist", 18)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClAutoUpdateStatus.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClAutoUpdateStatus.setDescription('Describes the status of current/last DHCP auto-update process.')
rlDhcpClAutoConfigForce = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 19), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClAutoConfigForce.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClAutoConfigForce.setDescription('Setting this MIB value to True will force DHCP auto-config process after next reboot. This configuration will take effect only during the time period between the next 2 reboots of the device (like a deffered action).')
rlDhcpClAutoConfigAutoSave = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 20), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClAutoConfigAutoSave.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClAutoConfigAutoSave.setDescription('Setting this MIB value to True configures automatic saving of running-cdb into startup-cdb, to be done at the end of successful DHCP auto-config process to running-cdb.')
rlDhcpClAutoConfigStatus = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21))).clone(namedValues=NamedValues(("noData", 1), ("openingDhcpConfigFile", 2), ("openingIndirectFile", 3), ("searchingHostnameInIndirectFile", 4), ("openingHostnameConfigFile", 5), ("openingHostnameCfgFile", 6), ("openingDefaultConfigFile", 7), ("downloadingConfigFile", 8), ("savingConfigInStartupCDB", 9), ("quitDhcpFileNotGivenOrNotExists", 10), ("quitFailedToFindAnyExistingConfigFile", 11), ("quitConfigFileContentsLenZero", 12), ("quitConfigFileDownloadFailed", 13), ("quitConditionsForAutoConfigChanged", 14), ("quitSelectedConfigFileNameUpdateFailed", 15), ("quitSelectedConfigFileNameOriginUpdateFailed", 16), ("quitSelectedTftpServerAddressUpdateFailed", 17), ("quitSelectedTftpServerAddressOriginUpdateFailed", 18), ("quitCopyRunningToStartupFailed", 19), ("quitNoTftpOutgoingInterface", 20), ("finishedSuccessfully", 21)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClAutoConfigStatus.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClAutoConfigStatus.setDescription('Describes the status of current/last DHCP auto-config process.')
rlDhcpClAutoConfigProtocol = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tftp", 1), ("scp", 2), ("auto", 3))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClAutoConfigProtocol.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClAutoConfigProtocol.setDescription("Describes the auto-config process protocol. tftp - only the TFTP protocol is used by auto-configuration. scp - only the SCP protocol is used by auto-configuration. auto-(Default) Auto-configuration uses the TFTP or SCP protocol depending on the configuration file's extension. If this option is selected, the extension parameter may be specified or, if not, the default extension is used.")
rlDhcpClAutoConfigScpFileExtention = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 23), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128)).clone('scp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClAutoConfigScpFileExtention.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClAutoConfigScpFileExtention.setDescription("Describes the SCP file extention. When no vlaue is specified, 'scp' extension is used.")
rlDhcpClSelectedTftpServerInetAddressType = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 24), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClSelectedTftpServerInetAddressType.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClSelectedTftpServerInetAddressType.setDescription('Currently selected TFTP server Inet Address type.')
rlDhcpClSelectedTftpServerInetAddress = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 25), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClSelectedTftpServerInetAddress.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClSelectedTftpServerInetAddress.setDescription('Currently selected TFTP server inet Address.')
rlDhcpClManualAutoConfigDataTable = MibTable((1, 3, 6, 1, 4, 1, 89, 76, 26), )
if mibBuilder.loadTexts: rlDhcpClManualAutoConfigDataTable.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClManualAutoConfigDataTable.setDescription(' A table for configuring default values for auto-config/ auto-update process. These values during the process, in case no appropriate data was received from the DHCP server.')
rlDhcpClManualAutoConfigDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 76, 26, 1), ).setIndexNames((0, "Dell-VRTX-DHCPCL-MIB", "rlDhcpClManualAutoConfigDataIndex"))
if mibBuilder.loadTexts: rlDhcpClManualAutoConfigDataEntry.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClManualAutoConfigDataEntry.setDescription('An entry (conceptual row) in rlDhcpClManualAutoConfigDataTable.')
rlDhcpClManualAutoConfigDataIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 26, 1, 1), Integer32())
if mibBuilder.loadTexts: rlDhcpClManualAutoConfigDataIndex.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClManualAutoConfigDataIndex.setDescription('The index of this row. There is only one entry in this table, whose index is 1.')
rlDhcpClManualServerInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 26, 1, 2), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClManualServerInetAddressType.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClManualServerInetAddressType.setDescription('Manually configured inet Address type of remote server.')
rlDhcpClManualServerInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 26, 1, 3), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClManualServerInetAddress.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClManualServerInetAddress.setDescription('Manually configured inet Address of remote server.')
rlDhcpClManualImageIndirectFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 26, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClManualImageIndirectFileName.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClManualImageIndirectFileName.setDescription('Manually configured indirect file name, that holds the name of the image file to download.')
rlDhcpClInformationTable = MibTable((1, 3, 6, 1, 4, 1, 89, 76, 27), )
if mibBuilder.loadTexts: rlDhcpClInformationTable.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClInformationTable.setDescription(' The (conceptual) table mentione IP address which must be released/renewed on the interface.')
rlDhcpClInformationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 76, 27, 1), ).setIndexNames((0, "Dell-VRTX-DHCPCL-MIB", "rlDhcpClInformationIfIndex"))
if mibBuilder.loadTexts: rlDhcpClInformationEntry.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClInformationEntry.setDescription('An entry (conceptual row) in dhcpClActionTable.')
rlDhcpClInformationIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 27, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClInformationIfIndex.setDescription(' The DHCPv4 client informational table. Contains information received by DHCP client from DHCP server')
rlDhcpClInformationIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 27, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationIpAddress.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClInformationIpAddress.setDescription('IP Address allocated by DHCP server.')
rlDhcpClInformationIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 27, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationIpMask.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClInformationIpMask.setDescription('IP Address mask allocated by DHCP server.')
rlDhcpClInformationT1 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 27, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationT1.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClInformationT1.setDescription('T1 timer value.')
rlDhcpClInformationT2 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 27, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationT2.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClInformationT2.setDescription('T2 timer value.')
rlDhcpClInformationDefaultGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 27, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationDefaultGateway.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClInformationDefaultGateway.setDescription('Default Gateway IP Address.')
rlDhcpClInformationHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 27, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationHostName.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClInformationHostName.setDescription(' Specifies the name of the client.')
rlDhcpClInformationDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 27, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationDomainName.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClInformationDomainName.setDescription('The Domain name received by DHCP client.')
rlDhcpClInformationTftpServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 27, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationTftpServerName.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClInformationTftpServerName.setDescription('The Tftp server name received by DHCP client.')
rlDhcpClInformationTftpFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 27, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationTftpFileName.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClInformationTftpFileName.setDescription('Name of file to use in configuration process received by DHCP client.')
rlDhcpClInformationTimeZone = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 27, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationTimeZone.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClInformationTimeZone.setDescription('The timezone received by DHCP client.')
rlDhcpClInformationTftpImageName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 27, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationTftpImageName.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClInformationTftpImageName.setDescription('Image filename to use in autoupdate process received by DHCP client.')
rlDhcpClInformationDnsServerListTable = MibTable((1, 3, 6, 1, 4, 1, 89, 76, 28), )
if mibBuilder.loadTexts: rlDhcpClInformationDnsServerListTable.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClInformationDnsServerListTable.setDescription(' The table saved the list of DNS servers received by DHCP client.')
rlDhcpClInformationDnsServerListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 76, 28, 1), ).setIndexNames((0, "Dell-VRTX-DHCPCL-MIB", "rlDhcpClInformationDnsServerListIfIndex"), (0, "Dell-VRTX-DHCPCL-MIB", "rlDhcpClInformationDnsServerListPriority"))
if mibBuilder.loadTexts: rlDhcpClInformationDnsServerListEntry.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClInformationDnsServerListEntry.setDescription('An entry in rlDhcpClInformationDnsServerListTable.')
rlDhcpClInformationDnsServerListIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 28, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlDhcpClInformationDnsServerListIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClInformationDnsServerListIfIndex.setDescription(' The IfIndex in rlDhcpClInformationDnsServerListEntry. ')
rlDhcpClInformationDnsServerListPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 28, 1, 2), Integer32())
if mibBuilder.loadTexts: rlDhcpClInformationDnsServerListPriority.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClInformationDnsServerListPriority.setDescription(' The priority of the entry. ')
rlDhcpClInformationDnsServerListAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 28, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationDnsServerListAddress.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClInformationDnsServerListAddress.setDescription('DNS server address received by DHCP client')
rlDhcpClInformationTftpServerListTable = MibTable((1, 3, 6, 1, 4, 1, 89, 76, 29), )
if mibBuilder.loadTexts: rlDhcpClInformationTftpServerListTable.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClInformationTftpServerListTable.setDescription(' The table saved the list of Tftp servers received by DHCP client.')
rlDhcpClInformationTftpServerListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 76, 29, 1), ).setIndexNames((0, "Dell-VRTX-DHCPCL-MIB", "rlDhcpClInformationTftpServerListIfIndex"), (0, "Dell-VRTX-DHCPCL-MIB", "rlDhcpClInformationTftpServerListPriority"))
if mibBuilder.loadTexts: rlDhcpClInformationTftpServerListEntry.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClInformationTftpServerListEntry.setDescription('An entry in rlDhcpClInformationTftpServerListTable.')
rlDhcpClInformationTftpServerListIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 29, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlDhcpClInformationTftpServerListIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClInformationTftpServerListIfIndex.setDescription(' The IfIndex in rlDhcpClInformationTftpServerListEntry. ')
rlDhcpClInformationTftpServerListPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 29, 1, 2), Integer32())
if mibBuilder.loadTexts: rlDhcpClInformationTftpServerListPriority.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClInformationTftpServerListPriority.setDescription(' The priority of the entry. ')
rlDhcpClInformationTftpServerListAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 29, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationTftpServerListAddress.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClInformationTftpServerListAddress.setDescription('Tftp server address received by DHCP client')
rlDhcpClAutoUpdateProtocol = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tftp", 1), ("scp", 2), ("auto", 3))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClAutoUpdateProtocol.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClAutoUpdateProtocol.setDescription("Describes the auto-update process protocol. tftp - only the TFTP protocol is used by auto-update. scp - only the SCP protocol is used by auto-update. auto-(Default) Auto-update uses the TFTP or SCP protocol depending on the configuration file's extension. If this option is selected, the extension parameter may be specified or, if not, the default extension is used.")
rlDhcpClAutoUpdateScpFileExtention = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 31), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128)).clone('scp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClAutoUpdateScpFileExtention.setStatus('current')
if mibBuilder.loadTexts: rlDhcpClAutoUpdateScpFileExtention.setDescription("Describes the SCP file extention used for auto-update. When no vlaue is specified, 'scp' extension is used.")
mibBuilder.exportSymbols("Dell-VRTX-DHCPCL-MIB", rlDhcpClManualAutoConfigDataTable=rlDhcpClManualAutoConfigDataTable, rlDhcpClSelectedTftpServerAddressOrigin=rlDhcpClSelectedTftpServerAddressOrigin, rlDhcpClInformationIfIndex=rlDhcpClInformationIfIndex, rlDhcpClInformationTftpServerListPriority=rlDhcpClInformationTftpServerListPriority, rlDhcpApprovalEnabled=rlDhcpApprovalEnabled, rlDhcpClCommandEntry=rlDhcpClCommandEntry, rlDhcpClInformationT2=rlDhcpClInformationT2, rlDhcpClInformationDefaultGateway=rlDhcpClInformationDefaultGateway, rlDhcpClManualAutoConfigDataEntry=rlDhcpClManualAutoConfigDataEntry, rlDhcpClManualConfigurationFileName=rlDhcpClManualConfigurationFileName, rlDhcpClInformationTftpFileName=rlDhcpClInformationTftpFileName, rlDhcpClInformationTftpServerListAddress=rlDhcpClInformationTftpServerListAddress, rlDhcpClAutoConfigForce=rlDhcpClAutoConfigForce, rlDhcpClManualServerInetAddressType=rlDhcpClManualServerInetAddressType, rlDhcpClInformationTftpServerListTable=rlDhcpClInformationTftpServerListTable, rlDhcpClAutoUpdateScpFileExtention=rlDhcpClAutoUpdateScpFileExtention, rlDhcpClInformationTftpServerListIfIndex=rlDhcpClInformationTftpServerListIfIndex, rlDhcpApprovalWaitingTable=rlDhcpApprovalWaitingTable, rlDhcpApprovalActionIfIndex=rlDhcpApprovalActionIfIndex, rlDhcpApprovalWaitingMask=rlDhcpApprovalWaitingMask, rlDhcpClActionTable=rlDhcpClActionTable, rlDhcpClInformationTftpServerName=rlDhcpClInformationTftpServerName, rlDhcpClInformationT1=rlDhcpClInformationT1, rlDhcpClEnabledByDefaultRemovedIfindex=rlDhcpClEnabledByDefaultRemovedIfindex, rlDhcpApprovalActionTable=rlDhcpApprovalActionTable, rlDhcpClActionEntry=rlDhcpClActionEntry, rlDhcpClInformationDomainName=rlDhcpClInformationDomainName, rlDhcpClInformationHostName=rlDhcpClInformationHostName, rlDhcpClAutoConfigScpFileExtention=rlDhcpClAutoConfigScpFileExtention, rlDhcpClActionIfIndex=rlDhcpClActionIfIndex, rlDhcpClConfigurationFileName=rlDhcpClConfigurationFileName, rlDhcpClAutoUpdateStatus=rlDhcpClAutoUpdateStatus, rlDhcpClAutoConfigAutoSave=rlDhcpClAutoConfigAutoSave, rlDhcpClManualServerInetAddress=rlDhcpClManualServerInetAddress, rlDhcpClManualImageIndirectFileName=rlDhcpClManualImageIndirectFileName, rlDhcpClInformationTimeZone=rlDhcpClInformationTimeZone, rlDhcpClInformationDnsServerListAddress=rlDhcpClInformationDnsServerListAddress, rlDhcpClSelectedTftpServerAddress=rlDhcpClSelectedTftpServerAddress, rlDhcpApprovalActionApprove=rlDhcpApprovalActionApprove, rlDhcpCl=rlDhcpCl, rlDhcpClInformationTftpImageName=rlDhcpClInformationTftpImageName, rlDhcpClActionStatus=rlDhcpClActionStatus, rlDhcpApprovalActionEntry=rlDhcpApprovalActionEntry, rlDhcpClSelectedConfigurationFileName=rlDhcpClSelectedConfigurationFileName, rlDhcpApprovalWaitingEntry=rlDhcpApprovalWaitingEntry, rlDhcpApprovalWaitingGateway=rlDhcpApprovalWaitingGateway, rlDhcpClInformationIpAddress=rlDhcpClInformationIpAddress, rlDhcpClInformationDnsServerListPriority=rlDhcpClInformationDnsServerListPriority, rlDhcpClInformationDnsServerListIfIndex=rlDhcpClInformationDnsServerListIfIndex, rlDhcpClManualAutoConfigDataIndex=rlDhcpClManualAutoConfigDataIndex, rlDhcpClActionHostName=rlDhcpClActionHostName, rlDhcpClAutoUpdateEnabled=rlDhcpClAutoUpdateEnabled, PYSNMP_MODULE_ID=rlDhcpCl, rlDhcpApprovalActionMask=rlDhcpApprovalActionMask, rlDhcpClCommandAction=rlDhcpClCommandAction, rlDhcpClOption67Enable=rlDhcpClOption67Enable, rlDhcpClSelectedConfigurationFileNameOrigin=rlDhcpClSelectedConfigurationFileNameOrigin, rlDhcpClInformationIpMask=rlDhcpClInformationIpMask, rlDhcpClInformationTftpServerListEntry=rlDhcpClInformationTftpServerListEntry, rlDhcpApprovalWaitingAddress=rlDhcpApprovalWaitingAddress, rlDhcpApprovalActionAddress=rlDhcpApprovalActionAddress, rlDhcpClManualTftpServerAddress=rlDhcpClManualTftpServerAddress, rlDhcpClAutoConfigStatus=rlDhcpClAutoConfigStatus, rlDhcpClAutoUpdateProtocol=rlDhcpClAutoUpdateProtocol, rlDhcpClInformationEntry=rlDhcpClInformationEntry, rlDhcpClInformationDnsServerListTable=rlDhcpClInformationDnsServerListTable, rlDhcpClAutoConfigProtocol=rlDhcpClAutoConfigProtocol, rlDhcpClSelectedTftpServerInetAddress=rlDhcpClSelectedTftpServerInetAddress, rlDhcpClInformationTable=rlDhcpClInformationTable, rlDhcpApprovalWaitingIfIndex=rlDhcpApprovalWaitingIfIndex, rlDhcpClSelectedTftpServerInetAddressType=rlDhcpClSelectedTftpServerInetAddressType, rlDhcpClInformationDnsServerListEntry=rlDhcpClInformationDnsServerListEntry, rlDhcpClCommandTable=rlDhcpClCommandTable)