# SNMP MIB module (DATALINK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DATALINK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:18 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 ObjectName,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 internet,
 iso,
 mgmt,
 private) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "ObjectName",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "internet",
    "iso",
    "mgmt",
    "private")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Asentria_ObjectIdentity = ObjectIdentity
asentria = _Asentria_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052)
)
_Datalink_ObjectIdentity = ObjectIdentity
datalink = _Datalink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1)
)
_ProductIds_ObjectIdentity = ObjectIdentity
productIds = _ProductIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 1)
)
_DatalinkThisProduct_Type = DisplayString
_DatalinkThisProduct_Object = MibScalar
datalinkThisProduct = _DatalinkThisProduct_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 1, 1),
    _DatalinkThisProduct_Type()
)
datalinkThisProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datalinkThisProduct.setStatus("mandatory")
_ProductConfig_ObjectIdentity = ObjectIdentity
productConfig = _ProductConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 2)
)
_Productname_Type = DisplayString
_Productname_Object = MibScalar
productname = _Productname_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 2, 1),
    _Productname_Type()
)
productname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productname.setStatus("mandatory")
_Systemversion_Type = Integer32
_Systemversion_Object = MibScalar
systemversion = _Systemversion_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 2, 2),
    _Systemversion_Type()
)
systemversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemversion.setStatus("mandatory")
_Appversion_Type = DisplayString
_Appversion_Object = MibScalar
appversion = _Appversion_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 2, 3),
    _Appversion_Type()
)
appversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appversion.setStatus("mandatory")
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 2, 4)
)
_Numberports_Type = Integer32
_Numberports_Object = MibScalar
numberports = _Numberports_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 2, 4, 1),
    _Numberports_Type()
)
numberports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberports.setStatus("mandatory")
_Netcard_Type = Integer32
_Netcard_Object = MibScalar
netcard = _Netcard_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 2, 4, 2),
    _Netcard_Type()
)
netcard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netcard.setStatus("mandatory")
_Modems_Type = Integer32
_Modems_Object = MibScalar
modems = _Modems_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 2, 4, 3),
    _Modems_Type()
)
modems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modems.setStatus("mandatory")
_Networkenabled_Type = Integer32
_Networkenabled_Object = MibScalar
networkenabled = _Networkenabled_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 2, 4, 4),
    _Networkenabled_Type()
)
networkenabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkenabled.setStatus("mandatory")
_Memorysize_Type = Integer32
_Memorysize_Object = MibScalar
memorysize = _Memorysize_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 2, 4, 5),
    _Memorysize_Type()
)
memorysize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorysize.setStatus("mandatory")
_Factorysetup_ObjectIdentity = ObjectIdentity
factorysetup = _Factorysetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 2, 5)
)
_Modemreport_Type = DisplayString
_Modemreport_Object = MibScalar
modemreport = _Modemreport_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 2, 5, 1),
    _Modemreport_Type()
)
modemreport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemreport.setStatus("mandatory")
_Modemportspeed_Type = Integer32
_Modemportspeed_Object = MibScalar
modemportspeed = _Modemportspeed_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 2, 5, 2),
    _Modemportspeed_Type()
)
modemportspeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemportspeed.setStatus("mandatory")
_Modemsetupstring_Type = DisplayString
_Modemsetupstring_Object = MibScalar
modemsetupstring = _Modemsetupstring_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 2, 5, 3),
    _Modemsetupstring_Type()
)
modemsetupstring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemsetupstring.setStatus("mandatory")
_Modemcddelay_Type = Integer32
_Modemcddelay_Object = MibScalar
modemcddelay = _Modemcddelay_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 2, 5, 4),
    _Modemcddelay_Type()
)
modemcddelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemcddelay.setStatus("mandatory")
_Modemtype_Type = Integer32
_Modemtype_Object = MibScalar
modemtype = _Modemtype_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 2, 5, 5),
    _Modemtype_Type()
)
modemtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemtype.setStatus("mandatory")
_Serialnumber_Type = DisplayString
_Serialnumber_Object = MibScalar
serialnumber = _Serialnumber_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 2, 5, 6),
    _Serialnumber_Type()
)
serialnumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialnumber.setStatus("mandatory")
_Dateofmanufacture_Type = DisplayString
_Dateofmanufacture_Object = MibScalar
dateofmanufacture = _Dateofmanufacture_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 2, 5, 7),
    _Dateofmanufacture_Type()
)
dateofmanufacture.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateofmanufacture.setStatus("mandatory")
_Databasemode_Type = Integer32
_Databasemode_Object = MibScalar
databasemode = _Databasemode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 2, 6),
    _Databasemode_Type()
)
databasemode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databasemode.setStatus("mandatory")
_UnitIds_ObjectIdentity = ObjectIdentity
unitIds = _UnitIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 3)
)
_DatalinkSiteId_Type = DisplayString
_DatalinkSiteId_Object = MibScalar
datalinkSiteId = _DatalinkSiteId_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 3, 1),
    _DatalinkSiteId_Type()
)
datalinkSiteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    datalinkSiteId.setStatus("mandatory")
_IdByPortTable_Object = MibTable
idByPortTable = _IdByPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 3, 2)
)
if mibBuilder.loadTexts:
    idByPortTable.setStatus("mandatory")
_Sitebyport_Object = MibTableRow
sitebyport = _Sitebyport_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 3, 2, 1)
)
sitebyport.setIndexNames(
    (0, "DATALINK-MIB", "siteindex"),
)
if mibBuilder.loadTexts:
    sitebyport.setStatus("mandatory")
_Siteindex_Type = Integer32
_Siteindex_Object = MibTableColumn
siteindex = _Siteindex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 3, 2, 1, 1),
    _Siteindex_Type()
)
siteindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteindex.setStatus("mandatory")
_SiteID_Type = DisplayString
_SiteID_Object = MibTableColumn
siteID = _SiteID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 3, 2, 1, 2),
    _SiteID_Type()
)
siteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteID.setStatus("mandatory")
_SerialPorts_ObjectIdentity = ObjectIdentity
serialPorts = _SerialPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 4)
)
_NumberPorts_Type = Integer32
_NumberPorts_Object = MibScalar
numberPorts = _NumberPorts_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 4, 1),
    _NumberPorts_Type()
)
numberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberPorts.setStatus("mandatory")
_PortSetupTable_Object = MibTable
portSetupTable = _PortSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 4, 2)
)
if mibBuilder.loadTexts:
    portSetupTable.setStatus("mandatory")
_PortSetupEntry_Object = MibTableRow
portSetupEntry = _PortSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 4, 2, 1)
)
portSetupEntry.setIndexNames(
    (0, "DATALINK-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portSetupEntry.setStatus("mandatory")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 4, 2, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("mandatory")
_PortBaud_Type = Integer32
_PortBaud_Object = MibTableColumn
portBaud = _PortBaud_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 4, 2, 1, 2),
    _PortBaud_Type()
)
portBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaud.setStatus("mandatory")
_PortWord_Type = Integer32
_PortWord_Object = MibTableColumn
portWord = _PortWord_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 4, 2, 1, 3),
    _PortWord_Type()
)
portWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portWord.setStatus("mandatory")
_PortParity_Type = DisplayString
_PortParity_Object = MibTableColumn
portParity = _PortParity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 4, 2, 1, 4),
    _PortParity_Type()
)
portParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portParity.setStatus("mandatory")
_PortStopbits_Type = Integer32
_PortStopbits_Object = MibTableColumn
portStopbits = _PortStopbits_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 4, 2, 1, 5),
    _PortStopbits_Type()
)
portStopbits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portStopbits.setStatus("mandatory")
_PortDataStore_Type = Integer32
_PortDataStore_Object = MibTableColumn
portDataStore = _PortDataStore_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 4, 2, 1, 6),
    _PortDataStore_Type()
)
portDataStore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDataStore.setStatus("mandatory")
_PortBinaryMode_Type = Integer32
_PortBinaryMode_Object = MibTableColumn
portBinaryMode = _PortBinaryMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 4, 2, 1, 7),
    _PortBinaryMode_Type()
)
portBinaryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBinaryMode.setStatus("mandatory")
_PortWrapMode_Type = Integer32
_PortWrapMode_Object = MibTableColumn
portWrapMode = _PortWrapMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 4, 2, 1, 8),
    _PortWrapMode_Type()
)
portWrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portWrapMode.setStatus("mandatory")
_PortHskMode_Type = Integer32
_PortHskMode_Object = MibTableColumn
portHskMode = _PortHskMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 4, 2, 1, 9),
    _PortHskMode_Type()
)
portHskMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portHskMode.setStatus("mandatory")
_PortDateTimeStampMode_Type = Integer32
_PortDateTimeStampMode_Object = MibTableColumn
portDateTimeStampMode = _PortDateTimeStampMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 4, 2, 1, 10),
    _PortDateTimeStampMode_Type()
)
portDateTimeStampMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDateTimeStampMode.setStatus("mandatory")
_PortPTMode_Type = Integer32
_PortPTMode_Object = MibTableColumn
portPTMode = _PortPTMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 4, 2, 1, 11),
    _PortPTMode_Type()
)
portPTMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPTMode.setStatus("mandatory")
_PortPTTime_Type = Integer32
_PortPTTime_Object = MibTableColumn
portPTTime = _PortPTTime_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 4, 2, 1, 12),
    _PortPTTime_Type()
)
portPTTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPTTime.setStatus("mandatory")
_PortStoreFile_Type = Integer32
_PortStoreFile_Object = MibTableColumn
portStoreFile = _PortStoreFile_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 4, 2, 1, 13),
    _PortStoreFile_Type()
)
portStoreFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portStoreFile.setStatus("mandatory")
_PortPtStripOutputLfs_Type = Integer32
_PortPtStripOutputLfs_Object = MibTableColumn
portPtStripOutputLfs = _PortPtStripOutputLfs_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 4, 2, 1, 14),
    _PortPtStripOutputLfs_Type()
)
portPtStripOutputLfs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPtStripOutputLfs.setStatus("mandatory")
_PortPtStripInputLfs_Type = Integer32
_PortPtStripInputLfs_Object = MibTableColumn
portPtStripInputLfs = _PortPtStripInputLfs_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 4, 2, 1, 15),
    _PortPtStripInputLfs_Type()
)
portPtStripInputLfs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPtStripInputLfs.setStatus("mandatory")
_PortlowDTR_Type = Integer32
_PortlowDTR_Object = MibTableColumn
portlowDTR = _PortlowDTR_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 4, 2, 1, 16),
    _PortlowDTR_Type()
)
portlowDTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portlowDTR.setStatus("mandatory")
_Time_ObjectIdentity = ObjectIdentity
time = _Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 5)
)
_Currenttime_Type = DisplayString
_Currenttime_Object = MibScalar
currenttime = _Currenttime_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 5, 1),
    _Currenttime_Type()
)
currenttime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currenttime.setStatus("mandatory")
_AutoDstAdjust_Type = Integer32
_AutoDstAdjust_Object = MibScalar
autoDstAdjust = _AutoDstAdjust_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 5, 2),
    _AutoDstAdjust_Type()
)
autoDstAdjust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoDstAdjust.setStatus("mandatory")
_Snmpsetup_ObjectIdentity = ObjectIdentity
snmpsetup = _Snmpsetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 6)
)
_SnmpTrapsEnabled_Type = Integer32
_SnmpTrapsEnabled_Object = MibScalar
snmpTrapsEnabled = _SnmpTrapsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 6, 1),
    _SnmpTrapsEnabled_Type()
)
snmpTrapsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapsEnabled.setStatus("mandatory")
_SnmpManagerTable_Object = MibTable
snmpManagerTable = _SnmpManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 6, 2)
)
if mibBuilder.loadTexts:
    snmpManagerTable.setStatus("mandatory")
_SnmpTableEntry_Object = MibTableRow
snmpTableEntry = _SnmpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 6, 2, 1)
)
snmpTableEntry.setIndexNames(
    (0, "DATALINK-MIB", "snmpMgrIndex"),
)
if mibBuilder.loadTexts:
    snmpTableEntry.setStatus("mandatory")
_SnmpMgrIndex_Type = Integer32
_SnmpMgrIndex_Object = MibTableColumn
snmpMgrIndex = _SnmpMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 6, 2, 1, 1),
    _SnmpMgrIndex_Type()
)
snmpMgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpMgrIndex.setStatus("mandatory")
_SnmpManagerIp_Type = IpAddress
_SnmpManagerIp_Object = MibTableColumn
snmpManagerIp = _SnmpManagerIp_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 6, 2, 1, 2),
    _SnmpManagerIp_Type()
)
snmpManagerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpManagerIp.setStatus("mandatory")
_SnmpManagerName_Type = DisplayString
_SnmpManagerName_Object = MibTableColumn
snmpManagerName = _SnmpManagerName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 6, 2, 1, 3),
    _SnmpManagerName_Type()
)
snmpManagerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpManagerName.setStatus("mandatory")
_SnmpTrapsAutoRepeatTime_Type = Integer32
_SnmpTrapsAutoRepeatTime_Object = MibScalar
snmpTrapsAutoRepeatTime = _SnmpTrapsAutoRepeatTime_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 6, 3),
    _SnmpTrapsAutoRepeatTime_Type()
)
snmpTrapsAutoRepeatTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapsAutoRepeatTime.setStatus("mandatory")
_SnmpSendTestTrap_Type = Integer32
_SnmpSendTestTrap_Object = MibScalar
snmpSendTestTrap = _SnmpSendTestTrap_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 6, 4),
    _SnmpSendTestTrap_Type()
)
snmpSendTestTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSendTestTrap.setStatus("mandatory")
_Passwords_ObjectIdentity = ObjectIdentity
passwords = _Passwords_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 7)
)
_ModemPasswords_Type = Integer32
_ModemPasswords_Object = MibScalar
modemPasswords = _ModemPasswords_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 7, 1),
    _ModemPasswords_Type()
)
modemPasswords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemPasswords.setStatus("mandatory")
_TcpPasswords_Type = Integer32
_TcpPasswords_Object = MibScalar
tcpPasswords = _TcpPasswords_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 7, 2),
    _TcpPasswords_Type()
)
tcpPasswords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpPasswords.setStatus("mandatory")
_FtpPasswords_Type = Integer32
_FtpPasswords_Object = MibScalar
ftpPasswords = _FtpPasswords_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 7, 3),
    _FtpPasswords_Type()
)
ftpPasswords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPasswords.setStatus("mandatory")
_PromptPasswords_Type = Integer32
_PromptPasswords_Object = MibScalar
promptPasswords = _PromptPasswords_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 7, 4),
    _PromptPasswords_Type()
)
promptPasswords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promptPasswords.setStatus("mandatory")
_CommandPassword_ObjectIdentity = ObjectIdentity
commandPassword = _CommandPassword_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 7, 5)
)
_CommandNeedsPassword_Type = Integer32
_CommandNeedsPassword_Object = MibScalar
commandNeedsPassword = _CommandNeedsPassword_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 7, 5, 1),
    _CommandNeedsPassword_Type()
)
commandNeedsPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandNeedsPassword.setStatus("mandatory")
_CommandPasswordTimeout_Type = Integer32
_CommandPasswordTimeout_Object = MibScalar
commandPasswordTimeout = _CommandPasswordTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 7, 5, 2),
    _CommandPasswordTimeout_Type()
)
commandPasswordTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandPasswordTimeout.setStatus("mandatory")
_PasswordTable_Object = MibTable
passwordTable = _PasswordTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 7, 6)
)
if mibBuilder.loadTexts:
    passwordTable.setStatus("mandatory")
_PasswordTableEntry_Object = MibTableRow
passwordTableEntry = _PasswordTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 7, 6, 1)
)
passwordTableEntry.setIndexNames(
    (0, "DATALINK-MIB", "passwordIndex"),
)
if mibBuilder.loadTexts:
    passwordTableEntry.setStatus("mandatory")
_PasswordIndex_Type = Integer32
_PasswordIndex_Object = MibScalar
passwordIndex = _PasswordIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 7, 6, 1, 1),
    _PasswordIndex_Type()
)
passwordIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passwordIndex.setStatus("mandatory")
_PasswordCommand_Type = DisplayString
_PasswordCommand_Object = MibScalar
passwordCommand = _PasswordCommand_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 7, 6, 1, 2),
    _PasswordCommand_Type()
)
passwordCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    passwordCommand.setStatus("mandatory")
_PasswordAccess_Type = DisplayString
_PasswordAccess_Object = MibScalar
passwordAccess = _PasswordAccess_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 7, 6, 1, 3),
    _PasswordAccess_Type()
)
passwordAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    passwordAccess.setStatus("mandatory")
_Ftpsetup_ObjectIdentity = ObjectIdentity
ftpsetup = _Ftpsetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 8)
)
_FtpAutoDelete_Type = Integer32
_FtpAutoDelete_Object = MibScalar
ftpAutoDelete = _FtpAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 8, 1),
    _FtpAutoDelete_Type()
)
ftpAutoDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpAutoDelete.setStatus("mandatory")
_FtpDataMode_Type = Integer32
_FtpDataMode_Object = MibScalar
ftpDataMode = _FtpDataMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 8, 2),
    _FtpDataMode_Type()
)
ftpDataMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpDataMode.setStatus("mandatory")
_FtpPush_ObjectIdentity = ObjectIdentity
ftpPush = _FtpPush_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 8, 3)
)
_FtpPushEnabled_Type = Integer32
_FtpPushEnabled_Object = MibScalar
ftpPushEnabled = _FtpPushEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 8, 3, 1),
    _FtpPushEnabled_Type()
)
ftpPushEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushEnabled.setStatus("mandatory")
_FtpPushTiming_Type = Integer32
_FtpPushTiming_Object = MibScalar
ftpPushTiming = _FtpPushTiming_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 8, 3, 2),
    _FtpPushTiming_Type()
)
ftpPushTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushTiming.setStatus("mandatory")
_FtpPushTimer_Type = Integer32
_FtpPushTimer_Object = MibScalar
ftpPushTimer = _FtpPushTimer_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 8, 3, 3),
    _FtpPushTimer_Type()
)
ftpPushTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushTimer.setStatus("mandatory")
_FtpPushIPAddress_Type = IpAddress
_FtpPushIPAddress_Object = MibScalar
ftpPushIPAddress = _FtpPushIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 8, 3, 4),
    _FtpPushIPAddress_Type()
)
ftpPushIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushIPAddress.setStatus("mandatory")
_FtpPushUser_Type = DisplayString
_FtpPushUser_Object = MibScalar
ftpPushUser = _FtpPushUser_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 8, 3, 5),
    _FtpPushUser_Type()
)
ftpPushUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushUser.setStatus("mandatory")
_FtpPushPass_Type = DisplayString
_FtpPushPass_Object = MibScalar
ftpPushPass = _FtpPushPass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 8, 3, 6),
    _FtpPushPass_Type()
)
ftpPushPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushPass.setStatus("mandatory")
_FtpPushAcct_Type = DisplayString
_FtpPushAcct_Object = MibScalar
ftpPushAcct = _FtpPushAcct_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 8, 3, 7),
    _FtpPushAcct_Type()
)
ftpPushAcct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushAcct.setStatus("mandatory")
_FtpPushDir_Type = DisplayString
_FtpPushDir_Object = MibScalar
ftpPushDir = _FtpPushDir_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 8, 3, 8),
    _FtpPushDir_Type()
)
ftpPushDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushDir.setStatus("mandatory")
_FtppushTable_Object = MibTable
ftppushTable = _FtppushTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 8, 3, 9)
)
if mibBuilder.loadTexts:
    ftppushTable.setStatus("mandatory")
_FtppushTableEntry_Object = MibTableRow
ftppushTableEntry = _FtppushTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 8, 3, 9, 1)
)
ftppushTableEntry.setIndexNames(
    (0, "DATALINK-MIB", "ftppushIndex"),
)
if mibBuilder.loadTexts:
    ftppushTableEntry.setStatus("mandatory")
_FtppushIndex_Type = Integer32
_FtppushIndex_Object = MibTableColumn
ftppushIndex = _FtppushIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 8, 3, 9, 1, 1),
    _FtppushIndex_Type()
)
ftppushIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftppushIndex.setStatus("mandatory")
_FtppushEnable_Type = Integer32
_FtppushEnable_Object = MibTableColumn
ftppushEnable = _FtppushEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 8, 3, 9, 1, 2),
    _FtppushEnable_Type()
)
ftppushEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftppushEnable.setStatus("mandatory")
_FtpPushAlarms_Type = Integer32
_FtpPushAlarms_Object = MibScalar
ftpPushAlarms = _FtpPushAlarms_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 8, 3, 10),
    _FtpPushAlarms_Type()
)
ftpPushAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushAlarms.setStatus("mandatory")
_FtpPushCount_Type = Integer32
_FtpPushCount_Object = MibScalar
ftpPushCount = _FtpPushCount_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 8, 3, 11),
    _FtpPushCount_Type()
)
ftpPushCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpPushCount.setStatus("mandatory")
_FtpPushStatusMode_Type = Integer32
_FtpPushStatusMode_Object = MibScalar
ftpPushStatusMode = _FtpPushStatusMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 8, 3, 12),
    _FtpPushStatusMode_Type()
)
ftpPushStatusMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushStatusMode.setStatus("mandatory")
_FtpPushServerName_Type = DisplayString
_FtpPushServerName_Object = MibScalar
ftpPushServerName = _FtpPushServerName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 8, 3, 13),
    _FtpPushServerName_Type()
)
ftpPushServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushServerName.setStatus("mandatory")
_Databases_ObjectIdentity = ObjectIdentity
databases = _Databases_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9)
)
_EntireDatabase_ObjectIdentity = ObjectIdentity
entireDatabase = _EntireDatabase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 1)
)
_DatabaseStatus_ObjectIdentity = ObjectIdentity
databaseStatus = _DatabaseStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 1, 1)
)
_DatabasePfull_Type = Integer32
_DatabasePfull_Object = MibScalar
databasePfull = _DatabasePfull_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 1, 1, 1),
    _DatabasePfull_Type()
)
databasePfull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databasePfull.setStatus("mandatory")
_DatabaseSize_Type = Integer32
_DatabaseSize_Object = MibScalar
databaseSize = _DatabaseSize_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 1, 1, 2),
    _DatabaseSize_Type()
)
databaseSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseSize.setStatus("mandatory")
_DatabaseRecordsAvailable_Type = Integer32
_DatabaseRecordsAvailable_Object = MibScalar
databaseRecordsAvailable = _DatabaseRecordsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 1, 1, 3),
    _DatabaseRecordsAvailable_Type()
)
databaseRecordsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseRecordsAvailable.setStatus("mandatory")
_DatabaseRecordsDeleted_Type = Integer32
_DatabaseRecordsDeleted_Object = MibScalar
databaseRecordsDeleted = _DatabaseRecordsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 1, 1, 4),
    _DatabaseRecordsDeleted_Type()
)
databaseRecordsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseRecordsDeleted.setStatus("mandatory")
_DatabaseAlarmTable_Object = MibTable
databaseAlarmTable = _DatabaseAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    databaseAlarmTable.setStatus("mandatory")
_DatabaseAlarmEntry_Object = MibTableRow
databaseAlarmEntry = _DatabaseAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 1, 2, 1)
)
databaseAlarmEntry.setIndexNames(
    (0, "DATALINK-MIB", "databaseAlarmIndex"),
)
if mibBuilder.loadTexts:
    databaseAlarmEntry.setStatus("mandatory")
_DatabaseAlarmIndex_Type = Integer32
_DatabaseAlarmIndex_Object = MibTableColumn
databaseAlarmIndex = _DatabaseAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 1, 2, 1, 1),
    _DatabaseAlarmIndex_Type()
)
databaseAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseAlarmIndex.setStatus("mandatory")
_DatabaseAlarmActive_Type = Integer32
_DatabaseAlarmActive_Object = MibTableColumn
databaseAlarmActive = _DatabaseAlarmActive_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 1, 2, 1, 2),
    _DatabaseAlarmActive_Type()
)
databaseAlarmActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseAlarmActive.setStatus("mandatory")
_DatabaseAlarmThreshold_Type = Integer32
_DatabaseAlarmThreshold_Object = MibTableColumn
databaseAlarmThreshold = _DatabaseAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 1, 2, 1, 3),
    _DatabaseAlarmThreshold_Type()
)
databaseAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseAlarmThreshold.setStatus("mandatory")
_DatabaseAlarmBeeperActions_Type = Integer32
_DatabaseAlarmBeeperActions_Object = MibTableColumn
databaseAlarmBeeperActions = _DatabaseAlarmBeeperActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 1, 2, 1, 4),
    _DatabaseAlarmBeeperActions_Type()
)
databaseAlarmBeeperActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseAlarmBeeperActions.setStatus("mandatory")
_DatabaseAlarmSerialActions_Type = Integer32
_DatabaseAlarmSerialActions_Object = MibTableColumn
databaseAlarmSerialActions = _DatabaseAlarmSerialActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 1, 2, 1, 5),
    _DatabaseAlarmSerialActions_Type()
)
databaseAlarmSerialActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseAlarmSerialActions.setStatus("mandatory")
_DatabaseAlarmPagerActions_Type = Integer32
_DatabaseAlarmPagerActions_Object = MibTableColumn
databaseAlarmPagerActions = _DatabaseAlarmPagerActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 1, 2, 1, 6),
    _DatabaseAlarmPagerActions_Type()
)
databaseAlarmPagerActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseAlarmPagerActions.setStatus("mandatory")
_DatabaseAlarmCalloutActions_Type = Integer32
_DatabaseAlarmCalloutActions_Object = MibTableColumn
databaseAlarmCalloutActions = _DatabaseAlarmCalloutActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 1, 2, 1, 7),
    _DatabaseAlarmCalloutActions_Type()
)
databaseAlarmCalloutActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseAlarmCalloutActions.setStatus("mandatory")
_DatabaseAlarmTrapActions_Type = Integer32
_DatabaseAlarmTrapActions_Object = MibTableColumn
databaseAlarmTrapActions = _DatabaseAlarmTrapActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 1, 2, 1, 8),
    _DatabaseAlarmTrapActions_Type()
)
databaseAlarmTrapActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseAlarmTrapActions.setStatus("mandatory")
_DatabaseAlarmFileStore_Type = Integer32
_DatabaseAlarmFileStore_Object = MibScalar
databaseAlarmFileStore = _DatabaseAlarmFileStore_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 1, 3),
    _DatabaseAlarmFileStore_Type()
)
databaseAlarmFileStore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseAlarmFileStore.setStatus("mandatory")
_DatabaseAlarmFileMaxSize_Type = Integer32
_DatabaseAlarmFileMaxSize_Object = MibScalar
databaseAlarmFileMaxSize = _DatabaseAlarmFileMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 1, 4),
    _DatabaseAlarmFileMaxSize_Type()
)
databaseAlarmFileMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseAlarmFileMaxSize.setStatus("mandatory")
_DatabaseFiles_ObjectIdentity = ObjectIdentity
databaseFiles = _DatabaseFiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2)
)
_Filesetup_ObjectIdentity = ObjectIdentity
filesetup = _Filesetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 1)
)
_CharmaskEnabled_Type = Integer32
_CharmaskEnabled_Object = MibScalar
charmaskEnabled = _CharmaskEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 1, 1),
    _CharmaskEnabled_Type()
)
charmaskEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charmaskEnabled.setStatus("mandatory")
_Charmask_Type = DisplayString
_Charmask_Object = MibScalar
charmask = _Charmask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 1, 2),
    _Charmask_Type()
)
charmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charmask.setStatus("mandatory")
_MaxRecordChars_Type = Integer32
_MaxRecordChars_Object = MibScalar
maxRecordChars = _MaxRecordChars_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 1, 3),
    _MaxRecordChars_Type()
)
maxRecordChars.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxRecordChars.setStatus("mandatory")
_BinRecordBlocking_Type = Integer32
_BinRecordBlocking_Object = MibScalar
binRecordBlocking = _BinRecordBlocking_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 1, 4),
    _BinRecordBlocking_Type()
)
binRecordBlocking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    binRecordBlocking.setStatus("mandatory")
_RecordCollectionTimeout_Type = Integer32
_RecordCollectionTimeout_Object = MibScalar
recordCollectionTimeout = _RecordCollectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 1, 5),
    _RecordCollectionTimeout_Type()
)
recordCollectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    recordCollectionTimeout.setStatus("mandatory")
_FileTable_Object = MibTable
fileTable = _FileTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    fileTable.setStatus("mandatory")
_FileTableEntry_Object = MibTableRow
fileTableEntry = _FileTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 2, 1)
)
fileTableEntry.setIndexNames(
    (0, "DATALINK-MIB", "fileTableIndex"),
)
if mibBuilder.loadTexts:
    fileTableEntry.setStatus("mandatory")
_FileTableIndex_Type = Integer32
_FileTableIndex_Object = MibTableColumn
fileTableIndex = _FileTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 2, 1, 1),
    _FileTableIndex_Type()
)
fileTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileTableIndex.setStatus("mandatory")
_FileName_Type = DisplayString
_FileName_Object = MibTableColumn
fileName = _FileName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 2, 1, 2),
    _FileName_Type()
)
fileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileName.setStatus("mandatory")
_FileType_Type = DisplayString
_FileType_Object = MibTableColumn
fileType = _FileType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 2, 1, 3),
    _FileType_Type()
)
fileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileType.setStatus("mandatory")
_FileSize_Type = Integer32
_FileSize_Object = MibTableColumn
fileSize = _FileSize_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 2, 1, 4),
    _FileSize_Type()
)
fileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSize.setStatus("mandatory")
_FileRecords_Type = Integer32
_FileRecords_Object = MibTableColumn
fileRecords = _FileRecords_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 2, 1, 5),
    _FileRecords_Type()
)
fileRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileRecords.setStatus("mandatory")
_FileRecordsAvailable_Type = Integer32
_FileRecordsAvailable_Object = MibTableColumn
fileRecordsAvailable = _FileRecordsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 2, 1, 6),
    _FileRecordsAvailable_Type()
)
fileRecordsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileRecordsAvailable.setStatus("mandatory")
_FileRecordsDeleted_Type = Integer32
_FileRecordsDeleted_Object = MibTableColumn
fileRecordsDeleted = _FileRecordsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 2, 1, 7),
    _FileRecordsDeleted_Type()
)
fileRecordsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileRecordsDeleted.setStatus("mandatory")
_FilePercentNow_Type = Integer32
_FilePercentNow_Object = MibTableColumn
filePercentNow = _FilePercentNow_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 2, 1, 8),
    _FilePercentNow_Type()
)
filePercentNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filePercentNow.setStatus("mandatory")
_FileAlarms_Object = MibTable
fileAlarms = _FileAlarms_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 3)
)
if mibBuilder.loadTexts:
    fileAlarms.setStatus("mandatory")
_FileAlarmEntry_Object = MibTableRow
fileAlarmEntry = _FileAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 3, 1)
)
fileAlarmEntry.setIndexNames(
    (0, "DATALINK-MIB", "fileAlarmFileIndex"),
    (0, "DATALINK-MIB", "fileAlarmThreshold"),
)
if mibBuilder.loadTexts:
    fileAlarmEntry.setStatus("mandatory")
_FileAlarmFileIndex_Type = Integer32
_FileAlarmFileIndex_Object = MibTableColumn
fileAlarmFileIndex = _FileAlarmFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 3, 1, 1),
    _FileAlarmFileIndex_Type()
)
fileAlarmFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileAlarmFileIndex.setStatus("mandatory")
_FileAlarmThresholdIndex_Type = Integer32
_FileAlarmThresholdIndex_Object = MibTableColumn
fileAlarmThresholdIndex = _FileAlarmThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 3, 1, 2),
    _FileAlarmThresholdIndex_Type()
)
fileAlarmThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileAlarmThresholdIndex.setStatus("mandatory")
_FileAlarmActive_Type = Integer32
_FileAlarmActive_Object = MibTableColumn
fileAlarmActive = _FileAlarmActive_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 3, 1, 3),
    _FileAlarmActive_Type()
)
fileAlarmActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileAlarmActive.setStatus("mandatory")
_FileAlarmThreshold_Type = Integer32
_FileAlarmThreshold_Object = MibTableColumn
fileAlarmThreshold = _FileAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 3, 1, 4),
    _FileAlarmThreshold_Type()
)
fileAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileAlarmThreshold.setStatus("mandatory")
_FileAlarmBeeperActions_Type = Integer32
_FileAlarmBeeperActions_Object = MibTableColumn
fileAlarmBeeperActions = _FileAlarmBeeperActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 3, 1, 5),
    _FileAlarmBeeperActions_Type()
)
fileAlarmBeeperActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileAlarmBeeperActions.setStatus("mandatory")
_FileAlarmSerialActions_Type = Integer32
_FileAlarmSerialActions_Object = MibTableColumn
fileAlarmSerialActions = _FileAlarmSerialActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 3, 1, 6),
    _FileAlarmSerialActions_Type()
)
fileAlarmSerialActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileAlarmSerialActions.setStatus("mandatory")
_FileAlarmPagerActions_Type = Integer32
_FileAlarmPagerActions_Object = MibTableColumn
fileAlarmPagerActions = _FileAlarmPagerActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 3, 1, 7),
    _FileAlarmPagerActions_Type()
)
fileAlarmPagerActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileAlarmPagerActions.setStatus("mandatory")
_FileAlarmCalloutActions_Type = Integer32
_FileAlarmCalloutActions_Object = MibTableColumn
fileAlarmCalloutActions = _FileAlarmCalloutActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 3, 1, 8),
    _FileAlarmCalloutActions_Type()
)
fileAlarmCalloutActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileAlarmCalloutActions.setStatus("mandatory")
_FileAlarmTrapActions_Type = Integer32
_FileAlarmTrapActions_Object = MibTableColumn
fileAlarmTrapActions = _FileAlarmTrapActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 9, 2, 3, 1, 9),
    _FileAlarmTrapActions_Type()
)
fileAlarmTrapActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileAlarmTrapActions.setStatus("mandatory")
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10)
)
_DataAlarmTable_Object = MibTable
dataAlarmTable = _DataAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 1)
)
if mibBuilder.loadTexts:
    dataAlarmTable.setStatus("mandatory")
_DataAlarmEntry_Object = MibTableRow
dataAlarmEntry = _DataAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 1, 1)
)
dataAlarmEntry.setIndexNames(
    (0, "DATALINK-MIB", "dataAlarmIndex"),
)
if mibBuilder.loadTexts:
    dataAlarmEntry.setStatus("mandatory")
_DataAlarmIndex_Type = Integer32
_DataAlarmIndex_Object = MibTableColumn
dataAlarmIndex = _DataAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 1, 1, 1),
    _DataAlarmIndex_Type()
)
dataAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataAlarmIndex.setStatus("mandatory")
_DataAlarmActive_Type = Integer32
_DataAlarmActive_Object = MibTableColumn
dataAlarmActive = _DataAlarmActive_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 1, 1, 2),
    _DataAlarmActive_Type()
)
dataAlarmActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataAlarmActive.setStatus("mandatory")
_DataAlarmName_Type = DisplayString
_DataAlarmName_Object = MibTableColumn
dataAlarmName = _DataAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 1, 1, 3),
    _DataAlarmName_Type()
)
dataAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataAlarmName.setStatus("mandatory")
_DataAlarmCounter_Type = Integer32
_DataAlarmCounter_Object = MibTableColumn
dataAlarmCounter = _DataAlarmCounter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 1, 1, 4),
    _DataAlarmCounter_Type()
)
dataAlarmCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataAlarmCounter.setStatus("mandatory")
_DataAlarmThreshold_Type = Integer32
_DataAlarmThreshold_Object = MibTableColumn
dataAlarmThreshold = _DataAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 1, 1, 5),
    _DataAlarmThreshold_Type()
)
dataAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataAlarmThreshold.setStatus("mandatory")
_DataAlarmClearMode_Type = Integer32
_DataAlarmClearMode_Object = MibTableColumn
dataAlarmClearMode = _DataAlarmClearMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 1, 1, 6),
    _DataAlarmClearMode_Type()
)
dataAlarmClearMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataAlarmClearMode.setStatus("mandatory")
_DataAlarmClearTime_Type = DisplayString
_DataAlarmClearTime_Object = MibTableColumn
dataAlarmClearTime = _DataAlarmClearTime_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 1, 1, 7),
    _DataAlarmClearTime_Type()
)
dataAlarmClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataAlarmClearTime.setStatus("mandatory")
_DataAlarmAcked_Type = Integer32
_DataAlarmAcked_Object = MibTableColumn
dataAlarmAcked = _DataAlarmAcked_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 1, 1, 8),
    _DataAlarmAcked_Type()
)
dataAlarmAcked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataAlarmAcked.setStatus("mandatory")
_DataAlarmBeeperActions_Type = Integer32
_DataAlarmBeeperActions_Object = MibTableColumn
dataAlarmBeeperActions = _DataAlarmBeeperActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 1, 1, 9),
    _DataAlarmBeeperActions_Type()
)
dataAlarmBeeperActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataAlarmBeeperActions.setStatus("mandatory")
_DataAlarmSerialActions_Type = Integer32
_DataAlarmSerialActions_Object = MibTableColumn
dataAlarmSerialActions = _DataAlarmSerialActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 1, 1, 10),
    _DataAlarmSerialActions_Type()
)
dataAlarmSerialActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataAlarmSerialActions.setStatus("mandatory")
_DataAlarmPagerActions_Type = Integer32
_DataAlarmPagerActions_Object = MibTableColumn
dataAlarmPagerActions = _DataAlarmPagerActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 1, 1, 11),
    _DataAlarmPagerActions_Type()
)
dataAlarmPagerActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataAlarmPagerActions.setStatus("mandatory")
_DataAlarmCalloutActions_Type = Integer32
_DataAlarmCalloutActions_Object = MibTableColumn
dataAlarmCalloutActions = _DataAlarmCalloutActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 1, 1, 12),
    _DataAlarmCalloutActions_Type()
)
dataAlarmCalloutActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataAlarmCalloutActions.setStatus("mandatory")
_DataAlarmTrapActions_Type = Integer32
_DataAlarmTrapActions_Object = MibTableColumn
dataAlarmTrapActions = _DataAlarmTrapActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 1, 1, 13),
    _DataAlarmTrapActions_Type()
)
dataAlarmTrapActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataAlarmTrapActions.setStatus("mandatory")
_DataAlarmString_Type = DisplayString
_DataAlarmString_Object = MibTableColumn
dataAlarmString = _DataAlarmString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 1, 1, 14),
    _DataAlarmString_Type()
)
dataAlarmString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataAlarmString.setStatus("mandatory")
_DataAlarmPort_Type = Integer32
_DataAlarmPort_Object = MibScalar
dataAlarmPort = _DataAlarmPort_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 1, 1, 15),
    _DataAlarmPort_Type()
)
dataAlarmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataAlarmPort.setStatus("mandatory")
_DataAlarmAutoClear_Type = Integer32
_DataAlarmAutoClear_Object = MibTableColumn
dataAlarmAutoClear = _DataAlarmAutoClear_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 1, 1, 16),
    _DataAlarmAutoClear_Type()
)
dataAlarmAutoClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataAlarmAutoClear.setStatus("mandatory")
_SensorAlarmTable_Object = MibTable
sensorAlarmTable = _SensorAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 2)
)
if mibBuilder.loadTexts:
    sensorAlarmTable.setStatus("mandatory")
_SensorAlarmEntry_Object = MibTableRow
sensorAlarmEntry = _SensorAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 2, 1)
)
sensorAlarmEntry.setIndexNames(
    (0, "DATALINK-MIB", "sensorAlarmIndex"),
)
if mibBuilder.loadTexts:
    sensorAlarmEntry.setStatus("mandatory")
_SensorAlarmIndex_Type = Integer32
_SensorAlarmIndex_Object = MibTableColumn
sensorAlarmIndex = _SensorAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 2, 1, 1),
    _SensorAlarmIndex_Type()
)
sensorAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorAlarmIndex.setStatus("mandatory")
_SensorAlarmActive_Type = Integer32
_SensorAlarmActive_Object = MibTableColumn
sensorAlarmActive = _SensorAlarmActive_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 2, 1, 2),
    _SensorAlarmActive_Type()
)
sensorAlarmActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorAlarmActive.setStatus("mandatory")
_SensorAlarmName_Type = DisplayString
_SensorAlarmName_Object = MibTableColumn
sensorAlarmName = _SensorAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 2, 1, 3),
    _SensorAlarmName_Type()
)
sensorAlarmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorAlarmName.setStatus("mandatory")
_SensorAlarmMode_Type = Integer32
_SensorAlarmMode_Object = MibTableColumn
sensorAlarmMode = _SensorAlarmMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 2, 1, 4),
    _SensorAlarmMode_Type()
)
sensorAlarmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorAlarmMode.setStatus("mandatory")
_SensorAlarmCounter_Type = Integer32
_SensorAlarmCounter_Object = MibTableColumn
sensorAlarmCounter = _SensorAlarmCounter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 2, 1, 5),
    _SensorAlarmCounter_Type()
)
sensorAlarmCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorAlarmCounter.setStatus("mandatory")
_SensorAlarmThreshold_Type = Integer32
_SensorAlarmThreshold_Object = MibTableColumn
sensorAlarmThreshold = _SensorAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 2, 1, 6),
    _SensorAlarmThreshold_Type()
)
sensorAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorAlarmThreshold.setStatus("mandatory")
_SensorAlarmAcked_Type = Integer32
_SensorAlarmAcked_Object = MibTableColumn
sensorAlarmAcked = _SensorAlarmAcked_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 2, 1, 7),
    _SensorAlarmAcked_Type()
)
sensorAlarmAcked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorAlarmAcked.setStatus("mandatory")
_SensorAlarmBeeperActions_Type = Integer32
_SensorAlarmBeeperActions_Object = MibTableColumn
sensorAlarmBeeperActions = _SensorAlarmBeeperActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 2, 1, 8),
    _SensorAlarmBeeperActions_Type()
)
sensorAlarmBeeperActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorAlarmBeeperActions.setStatus("mandatory")
_SensorAlarmSerialActions_Type = Integer32
_SensorAlarmSerialActions_Object = MibTableColumn
sensorAlarmSerialActions = _SensorAlarmSerialActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 2, 1, 9),
    _SensorAlarmSerialActions_Type()
)
sensorAlarmSerialActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorAlarmSerialActions.setStatus("mandatory")
_SensorAlarmPagerActions_Type = Integer32
_SensorAlarmPagerActions_Object = MibTableColumn
sensorAlarmPagerActions = _SensorAlarmPagerActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 2, 1, 10),
    _SensorAlarmPagerActions_Type()
)
sensorAlarmPagerActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorAlarmPagerActions.setStatus("mandatory")
_SensorAlarmCalloutActions_Type = Integer32
_SensorAlarmCalloutActions_Object = MibTableColumn
sensorAlarmCalloutActions = _SensorAlarmCalloutActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 2, 1, 11),
    _SensorAlarmCalloutActions_Type()
)
sensorAlarmCalloutActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorAlarmCalloutActions.setStatus("mandatory")
_SensorAlarmTrapActions_Type = Integer32
_SensorAlarmTrapActions_Object = MibTableColumn
sensorAlarmTrapActions = _SensorAlarmTrapActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 2, 1, 12),
    _SensorAlarmTrapActions_Type()
)
sensorAlarmTrapActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorAlarmTrapActions.setStatus("mandatory")
_SensorAlarmState_Type = Integer32
_SensorAlarmState_Object = MibTableColumn
sensorAlarmState = _SensorAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 2, 1, 13),
    _SensorAlarmState_Type()
)
sensorAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorAlarmState.setStatus("mandatory")
_NodataAlarms_ObjectIdentity = ObjectIdentity
nodataAlarms = _NodataAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3)
)
_NodataAlarmStatus_Object = MibTable
nodataAlarmStatus = _NodataAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 1)
)
if mibBuilder.loadTexts:
    nodataAlarmStatus.setStatus("mandatory")
_NodataAlarmStatusEntry_Object = MibTableRow
nodataAlarmStatusEntry = _NodataAlarmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 1, 1)
)
nodataAlarmStatusEntry.setIndexNames(
    (0, "DATALINK-MIB", "nodataAlarmStatusIndex"),
)
if mibBuilder.loadTexts:
    nodataAlarmStatusEntry.setStatus("mandatory")
_NodataAlarmStatusIndex_Type = Integer32
_NodataAlarmStatusIndex_Object = MibTableColumn
nodataAlarmStatusIndex = _NodataAlarmStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 1, 1, 1),
    _NodataAlarmStatusIndex_Type()
)
nodataAlarmStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodataAlarmStatusIndex.setStatus("mandatory")
_NodataAlarmStatusCounter_Type = Integer32
_NodataAlarmStatusCounter_Object = MibTableColumn
nodataAlarmStatusCounter = _NodataAlarmStatusCounter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 1, 1, 2),
    _NodataAlarmStatusCounter_Type()
)
nodataAlarmStatusCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodataAlarmStatusCounter.setStatus("mandatory")
_NodataAlarmStatusAcked_Type = Integer32
_NodataAlarmStatusAcked_Object = MibTableColumn
nodataAlarmStatusAcked = _NodataAlarmStatusAcked_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 1, 1, 3),
    _NodataAlarmStatusAcked_Type()
)
nodataAlarmStatusAcked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodataAlarmStatusAcked.setStatus("mandatory")
_NodataTable_Object = MibTable
nodataTable = _NodataTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 2)
)
if mibBuilder.loadTexts:
    nodataTable.setStatus("mandatory")
_NodataTableEntry_Object = MibTableRow
nodataTableEntry = _NodataTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 2, 1)
)
nodataTableEntry.setIndexNames(
    (0, "DATALINK-MIB", "nodataTablePortIndex"),
    (0, "DATALINK-MIB", "nodataTableScheduleIndex"),
    (0, "DATALINK-MIB", "nodataTableLevelIndex"),
)
if mibBuilder.loadTexts:
    nodataTableEntry.setStatus("mandatory")
_NodataTablePortIndex_Type = Integer32
_NodataTablePortIndex_Object = MibTableColumn
nodataTablePortIndex = _NodataTablePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 2, 1, 1),
    _NodataTablePortIndex_Type()
)
nodataTablePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nodataTablePortIndex.setStatus("mandatory")
_NodataTableScheduleIndex_Type = Integer32
_NodataTableScheduleIndex_Object = MibTableColumn
nodataTableScheduleIndex = _NodataTableScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 2, 1, 2),
    _NodataTableScheduleIndex_Type()
)
nodataTableScheduleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nodataTableScheduleIndex.setStatus("mandatory")
_NodataTableLevelIndex_Type = Integer32
_NodataTableLevelIndex_Object = MibTableColumn
nodataTableLevelIndex = _NodataTableLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 2, 1, 3),
    _NodataTableLevelIndex_Type()
)
nodataTableLevelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nodataTableLevelIndex.setStatus("mandatory")
_NodataTableActive_Type = Integer32
_NodataTableActive_Object = MibTableColumn
nodataTableActive = _NodataTableActive_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 2, 1, 4),
    _NodataTableActive_Type()
)
nodataTableActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodataTableActive.setStatus("mandatory")
_NodataTableSchedule_Type = DisplayString
_NodataTableSchedule_Object = MibTableColumn
nodataTableSchedule = _NodataTableSchedule_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 2, 1, 5),
    _NodataTableSchedule_Type()
)
nodataTableSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodataTableSchedule.setStatus("mandatory")
_NodataTableThreshold_Type = Integer32
_NodataTableThreshold_Object = MibTableColumn
nodataTableThreshold = _NodataTableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 2, 1, 6),
    _NodataTableThreshold_Type()
)
nodataTableThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodataTableThreshold.setStatus("mandatory")
_NodataTableBeeperActions_Type = Integer32
_NodataTableBeeperActions_Object = MibTableColumn
nodataTableBeeperActions = _NodataTableBeeperActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 2, 1, 7),
    _NodataTableBeeperActions_Type()
)
nodataTableBeeperActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodataTableBeeperActions.setStatus("mandatory")
_NodataTableSerialActions_Type = Integer32
_NodataTableSerialActions_Object = MibTableColumn
nodataTableSerialActions = _NodataTableSerialActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 2, 1, 8),
    _NodataTableSerialActions_Type()
)
nodataTableSerialActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodataTableSerialActions.setStatus("mandatory")
_NodataTablePagerActions_Type = Integer32
_NodataTablePagerActions_Object = MibTableColumn
nodataTablePagerActions = _NodataTablePagerActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 2, 1, 9),
    _NodataTablePagerActions_Type()
)
nodataTablePagerActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodataTablePagerActions.setStatus("mandatory")
_NodataTableCalloutActions_Type = Integer32
_NodataTableCalloutActions_Object = MibTableColumn
nodataTableCalloutActions = _NodataTableCalloutActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 2, 1, 10),
    _NodataTableCalloutActions_Type()
)
nodataTableCalloutActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodataTableCalloutActions.setStatus("mandatory")
_NodataTableTrapActions_Type = Integer32
_NodataTableTrapActions_Object = MibTableColumn
nodataTableTrapActions = _NodataTableTrapActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 2, 1, 11),
    _NodataTableTrapActions_Type()
)
nodataTableTrapActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodataTableTrapActions.setStatus("mandatory")
_NodataAlarmHolidays_ObjectIdentity = ObjectIdentity
nodataAlarmHolidays = _NodataAlarmHolidays_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 3)
)
_NodataNumberHolidays_Type = Integer32
_NodataNumberHolidays_Object = MibScalar
nodataNumberHolidays = _NodataNumberHolidays_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 3, 1),
    _NodataNumberHolidays_Type()
)
nodataNumberHolidays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodataNumberHolidays.setStatus("mandatory")
_NodataHolidayTable_Object = MibTable
nodataHolidayTable = _NodataHolidayTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 3, 2)
)
if mibBuilder.loadTexts:
    nodataHolidayTable.setStatus("mandatory")
_NodataHolidayTableEntry_Object = MibTableRow
nodataHolidayTableEntry = _NodataHolidayTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 3, 2, 1)
)
nodataHolidayTableEntry.setIndexNames(
    (0, "DATALINK-MIB", "nodataHolidayIndex"),
)
if mibBuilder.loadTexts:
    nodataHolidayTableEntry.setStatus("mandatory")
_NodataHolidayIndex_Type = Integer32
_NodataHolidayIndex_Object = MibTableColumn
nodataHolidayIndex = _NodataHolidayIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 3, 2, 1, 1),
    _NodataHolidayIndex_Type()
)
nodataHolidayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodataHolidayIndex.setStatus("mandatory")
_NodataHolidayItem_Type = DisplayString
_NodataHolidayItem_Object = MibTableColumn
nodataHolidayItem = _NodataHolidayItem_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 3, 2, 1, 2),
    _NodataHolidayItem_Type()
)
nodataHolidayItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodataHolidayItem.setStatus("mandatory")
_NodataHolidayAdd_Type = DisplayString
_NodataHolidayAdd_Object = MibScalar
nodataHolidayAdd = _NodataHolidayAdd_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 3, 3),
    _NodataHolidayAdd_Type()
)
nodataHolidayAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodataHolidayAdd.setStatus("mandatory")
_NodataHolidayDelete_Type = DisplayString
_NodataHolidayDelete_Object = MibScalar
nodataHolidayDelete = _NodataHolidayDelete_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 3, 4),
    _NodataHolidayDelete_Type()
)
nodataHolidayDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodataHolidayDelete.setStatus("mandatory")
_NodataHolidayClear_Type = Integer32
_NodataHolidayClear_Object = MibScalar
nodataHolidayClear = _NodataHolidayClear_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 3, 3, 5),
    _NodataHolidayClear_Type()
)
nodataHolidayClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodataHolidayClear.setStatus("mandatory")
_ScheduleAlarmTable_Object = MibTable
scheduleAlarmTable = _ScheduleAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 4)
)
if mibBuilder.loadTexts:
    scheduleAlarmTable.setStatus("mandatory")
_ScheduleAlarmEntry_Object = MibTableRow
scheduleAlarmEntry = _ScheduleAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 4, 1)
)
scheduleAlarmEntry.setIndexNames(
    (0, "DATALINK-MIB", "scheduleIndex"),
)
if mibBuilder.loadTexts:
    scheduleAlarmEntry.setStatus("mandatory")
_ScheduleIndex_Type = Integer32
_ScheduleIndex_Object = MibTableColumn
scheduleIndex = _ScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 4, 1, 1),
    _ScheduleIndex_Type()
)
scheduleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scheduleIndex.setStatus("mandatory")
_ScheduleActive_Type = Integer32
_ScheduleActive_Object = MibTableColumn
scheduleActive = _ScheduleActive_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 4, 1, 2),
    _ScheduleActive_Type()
)
scheduleActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scheduleActive.setStatus("mandatory")
_ScheduleTime_Type = DisplayString
_ScheduleTime_Object = MibTableColumn
scheduleTime = _ScheduleTime_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 4, 1, 3),
    _ScheduleTime_Type()
)
scheduleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scheduleTime.setStatus("mandatory")
_ScheduleAcked_Type = Integer32
_ScheduleAcked_Object = MibTableColumn
scheduleAcked = _ScheduleAcked_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 4, 1, 4),
    _ScheduleAcked_Type()
)
scheduleAcked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scheduleAcked.setStatus("mandatory")
_ScheduleBeeperActions_Type = Integer32
_ScheduleBeeperActions_Object = MibTableColumn
scheduleBeeperActions = _ScheduleBeeperActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 4, 1, 5),
    _ScheduleBeeperActions_Type()
)
scheduleBeeperActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scheduleBeeperActions.setStatus("mandatory")
_ScheduleSerialActions_Type = Integer32
_ScheduleSerialActions_Object = MibTableColumn
scheduleSerialActions = _ScheduleSerialActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 4, 1, 6),
    _ScheduleSerialActions_Type()
)
scheduleSerialActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scheduleSerialActions.setStatus("mandatory")
_SchedulePagerActions_Type = Integer32
_SchedulePagerActions_Object = MibTableColumn
schedulePagerActions = _SchedulePagerActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 4, 1, 7),
    _SchedulePagerActions_Type()
)
schedulePagerActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedulePagerActions.setStatus("mandatory")
_ScheduleCalloutActions_Type = Integer32
_ScheduleCalloutActions_Object = MibTableColumn
scheduleCalloutActions = _ScheduleCalloutActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 4, 1, 8),
    _ScheduleCalloutActions_Type()
)
scheduleCalloutActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scheduleCalloutActions.setStatus("mandatory")
_ScheduleTrapActions_Type = Integer32
_ScheduleTrapActions_Object = MibTableColumn
scheduleTrapActions = _ScheduleTrapActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 10, 4, 1, 9),
    _ScheduleTrapActions_Type()
)
scheduleTrapActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scheduleTrapActions.setStatus("mandatory")
_Actions_ObjectIdentity = ObjectIdentity
actions = _Actions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11)
)
_ActionsBuzzer_ObjectIdentity = ObjectIdentity
actionsBuzzer = _ActionsBuzzer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 1)
)
_ActionsBuzzerState_Type = Integer32
_ActionsBuzzerState_Object = MibScalar
actionsBuzzerState = _ActionsBuzzerState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 1, 1),
    _ActionsBuzzerState_Type()
)
actionsBuzzerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionsBuzzerState.setStatus("mandatory")
_ActionsSerialTable_Object = MibTable
actionsSerialTable = _ActionsSerialTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 2)
)
if mibBuilder.loadTexts:
    actionsSerialTable.setStatus("mandatory")
_ActionsSerialTableEntry_Object = MibTableRow
actionsSerialTableEntry = _ActionsSerialTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 2, 1)
)
actionsSerialTableEntry.setIndexNames(
    (0, "DATALINK-MIB", "serialTableIndex"),
)
if mibBuilder.loadTexts:
    actionsSerialTableEntry.setStatus("mandatory")
_SerialTableIndex_Type = Integer32
_SerialTableIndex_Object = MibTableColumn
serialTableIndex = _SerialTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 2, 1, 1),
    _SerialTableIndex_Type()
)
serialTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialTableIndex.setStatus("mandatory")
_SerialTableMessage_Type = DisplayString
_SerialTableMessage_Object = MibTableColumn
serialTableMessage = _SerialTableMessage_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 2, 1, 2),
    _SerialTableMessage_Type()
)
serialTableMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialTableMessage.setStatus("mandatory")
_ActionsPagerTable_Object = MibTable
actionsPagerTable = _ActionsPagerTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 3)
)
if mibBuilder.loadTexts:
    actionsPagerTable.setStatus("mandatory")
_ActionsPagerTableEntry_Object = MibTableRow
actionsPagerTableEntry = _ActionsPagerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 3, 1)
)
actionsPagerTableEntry.setIndexNames(
    (0, "DATALINK-MIB", "pagerTableIndex"),
)
if mibBuilder.loadTexts:
    actionsPagerTableEntry.setStatus("mandatory")
_PagerTableIndex_Type = Integer32
_PagerTableIndex_Object = MibTableColumn
pagerTableIndex = _PagerTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 3, 1, 1),
    _PagerTableIndex_Type()
)
pagerTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagerTableIndex.setStatus("mandatory")
_PagerType_Type = Integer32
_PagerType_Object = MibTableColumn
pagerType = _PagerType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 3, 1, 2),
    _PagerType_Type()
)
pagerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagerType.setStatus("mandatory")
_PagerPhonenumber_Type = DisplayString
_PagerPhonenumber_Object = MibTableColumn
pagerPhonenumber = _PagerPhonenumber_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 3, 1, 3),
    _PagerPhonenumber_Type()
)
pagerPhonenumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagerPhonenumber.setStatus("mandatory")
_PagerID_Type = DisplayString
_PagerID_Object = MibTableColumn
pagerID = _PagerID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 3, 1, 4),
    _PagerID_Type()
)
pagerID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagerID.setStatus("mandatory")
_PagerDialDelay_Type = Integer32
_PagerDialDelay_Object = MibTableColumn
pagerDialDelay = _PagerDialDelay_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 3, 1, 5),
    _PagerDialDelay_Type()
)
pagerDialDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagerDialDelay.setStatus("mandatory")
_PagerHangupDelay_Type = Integer32
_PagerHangupDelay_Object = MibTableColumn
pagerHangupDelay = _PagerHangupDelay_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 3, 1, 6),
    _PagerHangupDelay_Type()
)
pagerHangupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagerHangupDelay.setStatus("mandatory")
_PagerMessage_Type = DisplayString
_PagerMessage_Object = MibTableColumn
pagerMessage = _PagerMessage_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 3, 1, 7),
    _PagerMessage_Type()
)
pagerMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagerMessage.setStatus("mandatory")
_PagerSendId_Type = Integer32
_PagerSendId_Object = MibTableColumn
pagerSendId = _PagerSendId_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 3, 1, 8),
    _PagerSendId_Type()
)
pagerSendId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagerSendId.setStatus("mandatory")
_PagerSendReason_Type = Integer32
_PagerSendReason_Object = MibTableColumn
pagerSendReason = _PagerSendReason_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 3, 1, 9),
    _PagerSendReason_Type()
)
pagerSendReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagerSendReason.setStatus("mandatory")
_PagerMaxAttempts_Type = Integer32
_PagerMaxAttempts_Object = MibTableColumn
pagerMaxAttempts = _PagerMaxAttempts_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 3, 1, 10),
    _PagerMaxAttempts_Type()
)
pagerMaxAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagerMaxAttempts.setStatus("mandatory")
_PagerAttempts_Type = Integer32
_PagerAttempts_Object = MibTableColumn
pagerAttempts = _PagerAttempts_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 3, 1, 11),
    _PagerAttempts_Type()
)
pagerAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagerAttempts.setStatus("mandatory")
_PagerAttemptDelay_Type = Integer32
_PagerAttemptDelay_Object = MibTableColumn
pagerAttemptDelay = _PagerAttemptDelay_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 3, 1, 12),
    _PagerAttemptDelay_Type()
)
pagerAttemptDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagerAttemptDelay.setStatus("mandatory")
_PagerRepeat_Type = Integer32
_PagerRepeat_Object = MibTableColumn
pagerRepeat = _PagerRepeat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 3, 1, 13),
    _PagerRepeat_Type()
)
pagerRepeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagerRepeat.setStatus("mandatory")
_PagerRepeatDelay_Type = Integer32
_PagerRepeatDelay_Object = MibTableColumn
pagerRepeatDelay = _PagerRepeatDelay_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 3, 1, 14),
    _PagerRepeatDelay_Type()
)
pagerRepeatDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagerRepeatDelay.setStatus("mandatory")
_ActionsCalloutTable_Object = MibTable
actionsCalloutTable = _ActionsCalloutTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 4)
)
if mibBuilder.loadTexts:
    actionsCalloutTable.setStatus("mandatory")
_ActionsCalloutTableEntry_Object = MibTableRow
actionsCalloutTableEntry = _ActionsCalloutTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 4, 1)
)
actionsCalloutTableEntry.setIndexNames(
    (0, "DATALINK-MIB", "calloutTableIndex"),
)
if mibBuilder.loadTexts:
    actionsCalloutTableEntry.setStatus("mandatory")
_CalloutTableIndex_Type = Integer32
_CalloutTableIndex_Object = MibTableColumn
calloutTableIndex = _CalloutTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 4, 1, 1),
    _CalloutTableIndex_Type()
)
calloutTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calloutTableIndex.setStatus("mandatory")
_CalloutPhonenumber_Type = DisplayString
_CalloutPhonenumber_Object = MibTableColumn
calloutPhonenumber = _CalloutPhonenumber_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 4, 1, 2),
    _CalloutPhonenumber_Type()
)
calloutPhonenumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloutPhonenumber.setStatus("mandatory")
_CalloutMaxConnecttime_Type = Integer32
_CalloutMaxConnecttime_Object = MibTableColumn
calloutMaxConnecttime = _CalloutMaxConnecttime_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 4, 1, 3),
    _CalloutMaxConnecttime_Type()
)
calloutMaxConnecttime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloutMaxConnecttime.setStatus("mandatory")
_CalloutMessage_Type = DisplayString
_CalloutMessage_Object = MibTableColumn
calloutMessage = _CalloutMessage_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 4, 1, 4),
    _CalloutMessage_Type()
)
calloutMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloutMessage.setStatus("mandatory")
_CalloutSendId_Type = Integer32
_CalloutSendId_Object = MibTableColumn
calloutSendId = _CalloutSendId_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 4, 1, 5),
    _CalloutSendId_Type()
)
calloutSendId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloutSendId.setStatus("mandatory")
_CalloutSendReason_Type = Integer32
_CalloutSendReason_Object = MibTableColumn
calloutSendReason = _CalloutSendReason_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 4, 1, 6),
    _CalloutSendReason_Type()
)
calloutSendReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloutSendReason.setStatus("mandatory")
_CalloutCommandWait_Type = Integer32
_CalloutCommandWait_Object = MibTableColumn
calloutCommandWait = _CalloutCommandWait_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 4, 1, 7),
    _CalloutCommandWait_Type()
)
calloutCommandWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloutCommandWait.setStatus("mandatory")
_CalloutMaxAttempts_Type = Integer32
_CalloutMaxAttempts_Object = MibTableColumn
calloutMaxAttempts = _CalloutMaxAttempts_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 4, 1, 8),
    _CalloutMaxAttempts_Type()
)
calloutMaxAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloutMaxAttempts.setStatus("mandatory")
_CalloutAttempts_Type = Integer32
_CalloutAttempts_Object = MibTableColumn
calloutAttempts = _CalloutAttempts_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 4, 1, 9),
    _CalloutAttempts_Type()
)
calloutAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloutAttempts.setStatus("mandatory")
_CalloutAttemptDelay_Type = Integer32
_CalloutAttemptDelay_Object = MibTableColumn
calloutAttemptDelay = _CalloutAttemptDelay_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 4, 1, 10),
    _CalloutAttemptDelay_Type()
)
calloutAttemptDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloutAttemptDelay.setStatus("mandatory")
_CalloutRepeat_Type = Integer32
_CalloutRepeat_Object = MibTableColumn
calloutRepeat = _CalloutRepeat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 4, 1, 11),
    _CalloutRepeat_Type()
)
calloutRepeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloutRepeat.setStatus("mandatory")
_CalloutRepeatDelay_Type = Integer32
_CalloutRepeatDelay_Object = MibTableColumn
calloutRepeatDelay = _CalloutRepeatDelay_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 4, 1, 12),
    _CalloutRepeatDelay_Type()
)
calloutRepeatDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloutRepeatDelay.setStatus("mandatory")
_ActionsTraps_ObjectIdentity = ObjectIdentity
actionsTraps = _ActionsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 5)
)
_ActionsTrapsEntSpecific_Type = Integer32
_ActionsTrapsEntSpecific_Object = MibScalar
actionsTrapsEntSpecific = _ActionsTrapsEntSpecific_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 5, 1),
    _ActionsTrapsEntSpecific_Type()
)
actionsTrapsEntSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionsTrapsEntSpecific.setStatus("mandatory")
_ActionsTrapsEntSpecCount_Type = Integer32
_ActionsTrapsEntSpecCount_Object = MibScalar
actionsTrapsEntSpecCount = _ActionsTrapsEntSpecCount_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 11, 5, 2),
    _ActionsTrapsEntSpecCount_Type()
)
actionsTrapsEntSpecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionsTrapsEntSpecCount.setStatus("mandatory")
_Controls_ObjectIdentity = ObjectIdentity
controls = _Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12)
)
_OpSettings_ObjectIdentity = ObjectIdentity
opSettings = _OpSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 1)
)
_Linefeeds_Type = Integer32
_Linefeeds_Object = MibScalar
linefeeds = _Linefeeds_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 1, 1),
    _Linefeeds_Type()
)
linefeeds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linefeeds.setStatus("mandatory")
_Duplex_Type = Integer32
_Duplex_Object = MibScalar
duplex = _Duplex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 1, 2),
    _Duplex_Type()
)
duplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    duplex.setStatus("mandatory")
_Response_Type = Integer32
_Response_Object = MibScalar
response = _Response_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 1, 3),
    _Response_Type()
)
response.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    response.setStatus("mandatory")
_DatafilterEnabled_Type = Integer32
_DatafilterEnabled_Object = MibScalar
datafilterEnabled = _DatafilterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 1, 4),
    _DatafilterEnabled_Type()
)
datafilterEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    datafilterEnabled.setStatus("mandatory")
_AlarmfilterEnabled_Type = Integer32
_AlarmfilterEnabled_Object = MibScalar
alarmfilterEnabled = _AlarmfilterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 1, 5),
    _AlarmfilterEnabled_Type()
)
alarmfilterEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmfilterEnabled.setStatus("mandatory")
_AuxportMode_ObjectIdentity = ObjectIdentity
auxportMode = _AuxportMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 1, 6)
)
_OperatingMode_Type = Integer32
_OperatingMode_Object = MibScalar
operatingMode = _OperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 1, 6, 1),
    _OperatingMode_Type()
)
operatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    operatingMode.setStatus("mandatory")
_InlineMode_Type = Integer32
_InlineMode_Object = MibScalar
inlineMode = _InlineMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 1, 6, 2),
    _InlineMode_Type()
)
inlineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inlineMode.setStatus("mandatory")
_InlineSource_Type = Integer32
_InlineSource_Object = MibScalar
inlineSource = _InlineSource_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 1, 6, 3),
    _InlineSource_Type()
)
inlineSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inlineSource.setStatus("mandatory")
_InlineHskMode_ObjectIdentity = ObjectIdentity
inlineHskMode = _InlineHskMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 1, 6, 4)
)
_InlineHsk2_Type = Integer32
_InlineHsk2_Object = MibScalar
inlineHsk2 = _InlineHsk2_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 1, 6, 4, 1),
    _InlineHsk2_Type()
)
inlineHsk2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inlineHsk2.setStatus("mandatory")
_InlineHsk4_Type = Integer32
_InlineHsk4_Object = MibScalar
inlineHsk4 = _InlineHsk4_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 1, 6, 4, 2),
    _InlineHsk4_Type()
)
inlineHsk4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inlineHsk4.setStatus("mandatory")
_InlineHsk6_Type = Integer32
_InlineHsk6_Object = MibScalar
inlineHsk6 = _InlineHsk6_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 1, 6, 4, 3),
    _InlineHsk6_Type()
)
inlineHsk6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inlineHsk6.setStatus("mandatory")
_SureEnabled_Type = Integer32
_SureEnabled_Object = MibScalar
sureEnabled = _SureEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 1, 7),
    _SureEnabled_Type()
)
sureEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sureEnabled.setStatus("mandatory")
_CommandTcpipTimeout_Type = Integer32
_CommandTcpipTimeout_Object = MibScalar
commandTcpipTimeout = _CommandTcpipTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 1, 8),
    _CommandTcpipTimeout_Type()
)
commandTcpipTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandTcpipTimeout.setStatus("mandatory")
_SysadminTcpipTimeout_Type = Integer32
_SysadminTcpipTimeout_Object = MibScalar
sysadminTcpipTimeout = _SysadminTcpipTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 1, 9),
    _SysadminTcpipTimeout_Type()
)
sysadminTcpipTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysadminTcpipTimeout.setStatus("mandatory")
_BypassEndchar_Type = Integer32
_BypassEndchar_Object = MibScalar
bypassEndchar = _BypassEndchar_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 1, 10),
    _BypassEndchar_Type()
)
bypassEndchar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bypassEndchar.setStatus("mandatory")
_RouterAutoPing_Type = Integer32
_RouterAutoPing_Object = MibScalar
routerAutoPing = _RouterAutoPing_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 1, 11),
    _RouterAutoPing_Type()
)
routerAutoPing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routerAutoPing.setStatus("mandatory")
_ModemSettings_ObjectIdentity = ObjectIdentity
modemSettings = _ModemSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 2)
)
_ModemParity_Type = Integer32
_ModemParity_Object = MibScalar
modemParity = _ModemParity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 2, 1),
    _ModemParity_Type()
)
modemParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemParity.setStatus("mandatory")
_ModemUserSetup_Type = DisplayString
_ModemUserSetup_Object = MibScalar
modemUserSetup = _ModemUserSetup_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 2, 2),
    _ModemUserSetup_Type()
)
modemUserSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemUserSetup.setStatus("mandatory")
_ModemTapSetup_Type = DisplayString
_ModemTapSetup_Object = MibScalar
modemTapSetup = _ModemTapSetup_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 2, 3),
    _ModemTapSetup_Type()
)
modemTapSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemTapSetup.setStatus("mandatory")
_ModemAnswerString_Type = DisplayString
_ModemAnswerString_Object = MibScalar
modemAnswerString = _ModemAnswerString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 2, 4),
    _ModemAnswerString_Type()
)
modemAnswerString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAnswerString.setStatus("mandatory")
_ModemExtSetup_Type = DisplayString
_ModemExtSetup_Object = MibScalar
modemExtSetup = _ModemExtSetup_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 2, 5),
    _ModemExtSetup_Type()
)
modemExtSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemExtSetup.setStatus("mandatory")
_ModemExtSetupTime_Type = Integer32
_ModemExtSetupTime_Object = MibScalar
modemExtSetupTime = _ModemExtSetupTime_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 2, 6),
    _ModemExtSetupTime_Type()
)
modemExtSetupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemExtSetupTime.setStatus("mandatory")
_ModemInactivityTimer_Type = Integer32
_ModemInactivityTimer_Object = MibScalar
modemInactivityTimer = _ModemInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 2, 7),
    _ModemInactivityTimer_Type()
)
modemInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemInactivityTimer.setStatus("mandatory")
_ModemAutoexecString_Type = DisplayString
_ModemAutoexecString_Object = MibScalar
modemAutoexecString = _ModemAutoexecString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 2, 8),
    _ModemAutoexecString_Type()
)
modemAutoexecString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAutoexecString.setStatus("mandatory")
_ModemAutoexecEnabled_Type = Integer32
_ModemAutoexecEnabled_Object = MibScalar
modemAutoexecEnabled = _ModemAutoexecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 2, 9),
    _ModemAutoexecEnabled_Type()
)
modemAutoexecEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAutoexecEnabled.setStatus("mandatory")
_ModemTimeBetweenOutbound_Type = Integer32
_ModemTimeBetweenOutbound_Object = MibScalar
modemTimeBetweenOutbound = _ModemTimeBetweenOutbound_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 2, 10),
    _ModemTimeBetweenOutbound_Type()
)
modemTimeBetweenOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemTimeBetweenOutbound.setStatus("mandatory")
_DataRelease_ObjectIdentity = ObjectIdentity
dataRelease = _DataRelease_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 3)
)
_ReleaseMode_Type = Integer32
_ReleaseMode_Object = MibScalar
releaseMode = _ReleaseMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 3, 1),
    _ReleaseMode_Type()
)
releaseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    releaseMode.setStatus("mandatory")
_AutodeleteEnable_Type = Integer32
_AutodeleteEnable_Object = MibScalar
autodeleteEnable = _AutodeleteEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 3, 2),
    _AutodeleteEnable_Type()
)
autodeleteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autodeleteEnable.setStatus("mandatory")
_ReleaseCompressed_Type = Integer32
_ReleaseCompressed_Object = MibScalar
releaseCompressed = _ReleaseCompressed_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 3, 3),
    _ReleaseCompressed_Type()
)
releaseCompressed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    releaseCompressed.setStatus("mandatory")
_OtherControls_ObjectIdentity = ObjectIdentity
otherControls = _OtherControls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 4)
)
_WaitMode_Type = Integer32
_WaitMode_Object = MibScalar
waitMode = _WaitMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 4, 1),
    _WaitMode_Type()
)
waitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waitMode.setStatus("mandatory")
_TagMode_Type = Integer32
_TagMode_Object = MibScalar
tagMode = _TagMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 4, 2),
    _TagMode_Type()
)
tagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tagMode.setStatus("mandatory")
_CrcMode_Type = Integer32
_CrcMode_Object = MibScalar
crcMode = _CrcMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 4, 3),
    _CrcMode_Type()
)
crcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crcMode.setStatus("mandatory")
_DleMode_Type = Integer32
_DleMode_Object = MibScalar
dleMode = _DleMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 4, 4),
    _DleMode_Type()
)
dleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dleMode.setStatus("mandatory")
_CbbRetransmits_Type = Integer32
_CbbRetransmits_Object = MibScalar
cbbRetransmits = _CbbRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 4, 5),
    _CbbRetransmits_Type()
)
cbbRetransmits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbbRetransmits.setStatus("mandatory")
_CbbTimeout_Type = Integer32
_CbbTimeout_Object = MibScalar
cbbTimeout = _CbbTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 4, 6),
    _CbbTimeout_Type()
)
cbbTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbbTimeout.setStatus("mandatory")
_ActiveDatabase_Type = Integer32
_ActiveDatabase_Object = MibScalar
activeDatabase = _ActiveDatabase_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 12, 5),
    _ActiveDatabase_Type()
)
activeDatabase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeDatabase.setStatus("mandatory")
_Alarmhistory_ObjectIdentity = ObjectIdentity
alarmhistory = _Alarmhistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13)
)
_ActionQueue_ObjectIdentity = ObjectIdentity
actionQueue = _ActionQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 1)
)
_ActionCount_Type = Integer32
_ActionCount_Object = MibScalar
actionCount = _ActionCount_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 1, 1),
    _ActionCount_Type()
)
actionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionCount.setStatus("mandatory")
_ActionTable_Object = MibTable
actionTable = _ActionTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 1, 2)
)
if mibBuilder.loadTexts:
    actionTable.setStatus("mandatory")
_ActionTableEntry_Object = MibTableRow
actionTableEntry = _ActionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 1, 2, 1)
)
actionTableEntry.setIndexNames(
    (0, "DATALINK-MIB", "actionTableIndex"),
)
if mibBuilder.loadTexts:
    actionTableEntry.setStatus("mandatory")
_ActionTableIndex_Type = Integer32
_ActionTableIndex_Object = MibTableColumn
actionTableIndex = _ActionTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 1, 2, 1, 1),
    _ActionTableIndex_Type()
)
actionTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionTableIndex.setStatus("mandatory")
_ActionAcked_Type = Integer32
_ActionAcked_Object = MibTableColumn
actionAcked = _ActionAcked_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 1, 2, 1, 2),
    _ActionAcked_Type()
)
actionAcked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionAcked.setStatus("mandatory")
_ActionReason_Type = Integer32
_ActionReason_Object = MibTableColumn
actionReason = _ActionReason_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 1, 2, 1, 3),
    _ActionReason_Type()
)
actionReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionReason.setStatus("mandatory")
_ActionReasonID_Type = Integer32
_ActionReasonID_Object = MibTableColumn
actionReasonID = _ActionReasonID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 1, 2, 1, 4),
    _ActionReasonID_Type()
)
actionReasonID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionReasonID.setStatus("mandatory")
_ActionReasonLevel_Type = Integer32
_ActionReasonLevel_Object = MibTableColumn
actionReasonLevel = _ActionReasonLevel_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 1, 2, 1, 5),
    _ActionReasonLevel_Type()
)
actionReasonLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionReasonLevel.setStatus("mandatory")
_ActionType_Type = Integer32
_ActionType_Object = MibTableColumn
actionType = _ActionType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 1, 2, 1, 6),
    _ActionType_Type()
)
actionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionType.setStatus("mandatory")
_ActionTypeID_Type = Integer32
_ActionTypeID_Object = MibTableColumn
actionTypeID = _ActionTypeID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 1, 2, 1, 7),
    _ActionTypeID_Type()
)
actionTypeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionTypeID.setStatus("mandatory")
_ActionRepeatTime_Type = Integer32
_ActionRepeatTime_Object = MibTableColumn
actionRepeatTime = _ActionRepeatTime_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 1, 2, 1, 8),
    _ActionRepeatTime_Type()
)
actionRepeatTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionRepeatTime.setStatus("mandatory")
_ActionAttempts_Type = Integer32
_ActionAttempts_Object = MibTableColumn
actionAttempts = _ActionAttempts_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 1, 2, 1, 9),
    _ActionAttempts_Type()
)
actionAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionAttempts.setStatus("mandatory")
_ActionNextAttempt_Type = Integer32
_ActionNextAttempt_Object = MibTableColumn
actionNextAttempt = _ActionNextAttempt_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 1, 2, 1, 10),
    _ActionNextAttempt_Type()
)
actionNextAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionNextAttempt.setStatus("mandatory")
_ActionTimeStamp_Type = DisplayString
_ActionTimeStamp_Object = MibTableColumn
actionTimeStamp = _ActionTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 1, 2, 1, 11),
    _ActionTimeStamp_Type()
)
actionTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionTimeStamp.setStatus("mandatory")
_ActionHistory_ObjectIdentity = ObjectIdentity
actionHistory = _ActionHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 2)
)
_HistoryCount_Type = Integer32
_HistoryCount_Object = MibScalar
historyCount = _HistoryCount_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 2, 1),
    _HistoryCount_Type()
)
historyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyCount.setStatus("mandatory")
_HistoryTable_Object = MibTable
historyTable = _HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 2, 2)
)
if mibBuilder.loadTexts:
    historyTable.setStatus("mandatory")
_HistoryTableEntry_Object = MibTableRow
historyTableEntry = _HistoryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 2, 2, 1)
)
historyTableEntry.setIndexNames(
    (0, "DATALINK-MIB", "historyTableIndex"),
)
if mibBuilder.loadTexts:
    historyTableEntry.setStatus("mandatory")
_HistoryTableIndex_Type = Integer32
_HistoryTableIndex_Object = MibTableColumn
historyTableIndex = _HistoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 2, 2, 1, 1),
    _HistoryTableIndex_Type()
)
historyTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyTableIndex.setStatus("mandatory")
_HistoryEntryType_Type = Integer32
_HistoryEntryType_Object = MibTableColumn
historyEntryType = _HistoryEntryType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 2, 2, 1, 2),
    _HistoryEntryType_Type()
)
historyEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    historyEntryType.setStatus("mandatory")
_HistoryReason_Type = Integer32
_HistoryReason_Object = MibTableColumn
historyReason = _HistoryReason_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 2, 2, 1, 3),
    _HistoryReason_Type()
)
historyReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyReason.setStatus("mandatory")
_HistoryReasonID_Type = Integer32
_HistoryReasonID_Object = MibTableColumn
historyReasonID = _HistoryReasonID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 2, 2, 1, 4),
    _HistoryReasonID_Type()
)
historyReasonID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyReasonID.setStatus("mandatory")
_HistoryReasonLevel_Type = Integer32
_HistoryReasonLevel_Object = MibTableColumn
historyReasonLevel = _HistoryReasonLevel_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 2, 2, 1, 5),
    _HistoryReasonLevel_Type()
)
historyReasonLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyReasonLevel.setStatus("mandatory")
_HistoryType_Type = Integer32
_HistoryType_Object = MibTableColumn
historyType = _HistoryType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 2, 2, 1, 6),
    _HistoryType_Type()
)
historyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyType.setStatus("mandatory")
_HistoryTypeID_Type = Integer32
_HistoryTypeID_Object = MibTableColumn
historyTypeID = _HistoryTypeID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 2, 2, 1, 7),
    _HistoryTypeID_Type()
)
historyTypeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyTypeID.setStatus("mandatory")
_HistoryTimeStamp_Type = DisplayString
_HistoryTimeStamp_Object = MibTableColumn
historyTimeStamp = _HistoryTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 2, 2, 1, 8),
    _HistoryTimeStamp_Type()
)
historyTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyTimeStamp.setStatus("mandatory")
_HistoryClearLog_Type = Integer32
_HistoryClearLog_Object = MibTableColumn
historyClearLog = _HistoryClearLog_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 2, 2, 1, 9),
    _HistoryClearLog_Type()
)
historyClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    historyClearLog.setStatus("mandatory")
_LastCalloutPageReason_Type = DisplayString
_LastCalloutPageReason_Object = MibScalar
lastCalloutPageReason = _LastCalloutPageReason_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 13, 3),
    _LastCalloutPageReason_Type()
)
lastCalloutPageReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastCalloutPageReason.setStatus("mandatory")
_Realtimesocket_ObjectIdentity = ObjectIdentity
realtimesocket = _Realtimesocket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 14)
)
_RtsShowAnswer_Type = Integer32
_RtsShowAnswer_Object = MibScalar
rtsShowAnswer = _RtsShowAnswer_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 14, 1),
    _RtsShowAnswer_Type()
)
rtsShowAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsShowAnswer.setStatus("deprecated")
_RtsNeedPassword_Type = Integer32
_RtsNeedPassword_Object = MibScalar
rtsNeedPassword = _RtsNeedPassword_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 14, 2),
    _RtsNeedPassword_Type()
)
rtsNeedPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtsNeedPassword.setStatus("deprecated")
_RtsWaitXon_Type = Integer32
_RtsWaitXon_Object = MibScalar
rtsWaitXon = _RtsWaitXon_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 14, 3),
    _RtsWaitXon_Type()
)
rtsWaitXon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsWaitXon.setStatus("deprecated")
_RtsIdleTimeout_Type = Integer32
_RtsIdleTimeout_Object = MibScalar
rtsIdleTimeout = _RtsIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 14, 4),
    _RtsIdleTimeout_Type()
)
rtsIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsIdleTimeout.setStatus("deprecated")
_RtsEmptyClose_Type = Integer32
_RtsEmptyClose_Object = MibScalar
rtsEmptyClose = _RtsEmptyClose_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 14, 5),
    _RtsEmptyClose_Type()
)
rtsEmptyClose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsEmptyClose.setStatus("deprecated")
_RtsTable_Object = MibTable
rtsTable = _RtsTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 14, 6)
)
if mibBuilder.loadTexts:
    rtsTable.setStatus("mandatory")
_RtsTableEntry_Object = MibTableRow
rtsTableEntry = _RtsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 14, 6, 1)
)
rtsTableEntry.setIndexNames(
    (0, "DATALINK-MIB", "rtsTableIndex"),
)
if mibBuilder.loadTexts:
    rtsTableEntry.setStatus("mandatory")
_RtsTableIndex_Type = Integer32
_RtsTableIndex_Object = MibTableColumn
rtsTableIndex = _RtsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 14, 6, 1, 1),
    _RtsTableIndex_Type()
)
rtsTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtsTableIndex.setStatus("mandatory")
_RtsNoStore_Type = Integer32
_RtsNoStore_Object = MibTableColumn
rtsNoStore = _RtsNoStore_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 14, 6, 1, 2),
    _RtsNoStore_Type()
)
rtsNoStore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsNoStore.setStatus("mandatory")
_RtsDenied_Type = Integer32
_RtsDenied_Object = MibTableColumn
rtsDenied = _RtsDenied_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 14, 6, 1, 3),
    _RtsDenied_Type()
)
rtsDenied.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsDenied.setStatus("mandatory")
_RtsSocketState_Type = Integer32
_RtsSocketState_Object = MibTableColumn
rtsSocketState = _RtsSocketState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 14, 6, 1, 4),
    _RtsSocketState_Type()
)
rtsSocketState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtsSocketState.setStatus("mandatory")
_RtsPortShowAnswer_Type = Integer32
_RtsPortShowAnswer_Object = MibTableColumn
rtsPortShowAnswer = _RtsPortShowAnswer_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 14, 6, 1, 5),
    _RtsPortShowAnswer_Type()
)
rtsPortShowAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsPortShowAnswer.setStatus("mandatory")
_RtsPortNeedPassword_Type = Integer32
_RtsPortNeedPassword_Object = MibTableColumn
rtsPortNeedPassword = _RtsPortNeedPassword_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 14, 6, 1, 6),
    _RtsPortNeedPassword_Type()
)
rtsPortNeedPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtsPortNeedPassword.setStatus("mandatory")
_RtsPortWaitXon_Type = Integer32
_RtsPortWaitXon_Object = MibTableColumn
rtsPortWaitXon = _RtsPortWaitXon_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 14, 6, 1, 7),
    _RtsPortWaitXon_Type()
)
rtsPortWaitXon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsPortWaitXon.setStatus("mandatory")
_RtsPortIdleTimeout_Type = Integer32
_RtsPortIdleTimeout_Object = MibTableColumn
rtsPortIdleTimeout = _RtsPortIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 14, 6, 1, 8),
    _RtsPortIdleTimeout_Type()
)
rtsPortIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsPortIdleTimeout.setStatus("mandatory")
_RtsPortEmptyClose_Type = Integer32
_RtsPortEmptyClose_Object = MibTableColumn
rtsPortEmptyClose = _RtsPortEmptyClose_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 14, 6, 1, 9),
    _RtsPortEmptyClose_Type()
)
rtsPortEmptyClose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsPortEmptyClose.setStatus("mandatory")
_Iprestrictions_ObjectIdentity = ObjectIdentity
iprestrictions = _Iprestrictions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 15)
)
_IprestrictTable_Object = MibTable
iprestrictTable = _IprestrictTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 15, 1)
)
if mibBuilder.loadTexts:
    iprestrictTable.setStatus("mandatory")
_IprestrictTableEntry_Object = MibTableRow
iprestrictTableEntry = _IprestrictTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 15, 1, 1)
)
iprestrictTableEntry.setIndexNames(
    (0, "DATALINK-MIB", "iprestrictTableIndex"),
)
if mibBuilder.loadTexts:
    iprestrictTableEntry.setStatus("mandatory")
_IprestrictTableIndex_Type = Integer32
_IprestrictTableIndex_Object = MibTableColumn
iprestrictTableIndex = _IprestrictTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 15, 1, 1, 1),
    _IprestrictTableIndex_Type()
)
iprestrictTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprestrictTableIndex.setStatus("mandatory")
_IprestrictIpAddress_Type = IpAddress
_IprestrictIpAddress_Object = MibTableColumn
iprestrictIpAddress = _IprestrictIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 15, 1, 1, 2),
    _IprestrictIpAddress_Type()
)
iprestrictIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iprestrictIpAddress.setStatus("mandatory")
_SuspendIPRestrictions_Type = Integer32
_SuspendIPRestrictions_Object = MibScalar
suspendIPRestrictions = _SuspendIPRestrictions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 15, 2),
    _SuspendIPRestrictions_Type()
)
suspendIPRestrictions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    suspendIPRestrictions.setStatus("mandatory")
_KillIPRestrictions_Type = Integer32
_KillIPRestrictions_Object = MibScalar
killIPRestrictions = _KillIPRestrictions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 15, 3),
    _KillIPRestrictions_Type()
)
killIPRestrictions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    killIPRestrictions.setStatus("mandatory")
_AddIPRestrictions_Type = IpAddress
_AddIPRestrictions_Object = MibScalar
addIPRestrictions = _AddIPRestrictions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 15, 4),
    _AddIPRestrictions_Type()
)
addIPRestrictions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addIPRestrictions.setStatus("mandatory")
_Ipsetup_ObjectIdentity = ObjectIdentity
ipsetup = _Ipsetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 16)
)
_IpCurrent_ObjectIdentity = ObjectIdentity
ipCurrent = _IpCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 16, 1)
)
_IpCurrentStatic_Type = Integer32
_IpCurrentStatic_Object = MibScalar
ipCurrentStatic = _IpCurrentStatic_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 16, 1, 1),
    _IpCurrentStatic_Type()
)
ipCurrentStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurrentStatic.setStatus("mandatory")
_IpCurrentAddress_Type = IpAddress
_IpCurrentAddress_Object = MibScalar
ipCurrentAddress = _IpCurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 16, 1, 2),
    _IpCurrentAddress_Type()
)
ipCurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurrentAddress.setStatus("mandatory")
_IpCurrentSubnetMask_Type = IpAddress
_IpCurrentSubnetMask_Object = MibScalar
ipCurrentSubnetMask = _IpCurrentSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 16, 1, 3),
    _IpCurrentSubnetMask_Type()
)
ipCurrentSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurrentSubnetMask.setStatus("mandatory")
_IpCurrentDefaultRouter_Type = IpAddress
_IpCurrentDefaultRouter_Object = MibScalar
ipCurrentDefaultRouter = _IpCurrentDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 16, 1, 4),
    _IpCurrentDefaultRouter_Type()
)
ipCurrentDefaultRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurrentDefaultRouter.setStatus("mandatory")
_IpNew_ObjectIdentity = ObjectIdentity
ipNew = _IpNew_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 16, 2)
)
_IpNewStatic_Type = Integer32
_IpNewStatic_Object = MibScalar
ipNewStatic = _IpNewStatic_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 16, 2, 1),
    _IpNewStatic_Type()
)
ipNewStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewStatic.setStatus("mandatory")
_IpNewAddress_Type = IpAddress
_IpNewAddress_Object = MibScalar
ipNewAddress = _IpNewAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 16, 2, 2),
    _IpNewAddress_Type()
)
ipNewAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewAddress.setStatus("mandatory")
_IpNewSubnetMask_Type = IpAddress
_IpNewSubnetMask_Object = MibScalar
ipNewSubnetMask = _IpNewSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 16, 2, 3),
    _IpNewSubnetMask_Type()
)
ipNewSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewSubnetMask.setStatus("mandatory")
_IpNewDefaultRouter_Type = IpAddress
_IpNewDefaultRouter_Object = MibScalar
ipNewDefaultRouter = _IpNewDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 16, 2, 4),
    _IpNewDefaultRouter_Type()
)
ipNewDefaultRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewDefaultRouter.setStatus("mandatory")
_IpNewSetup_Type = Integer32
_IpNewSetup_Object = MibScalar
ipNewSetup = _IpNewSetup_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 16, 2, 5),
    _IpNewSetup_Type()
)
ipNewSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewSetup.setStatus("mandatory")
_Pppsetup_ObjectIdentity = ObjectIdentity
pppsetup = _Pppsetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 17)
)
_PppIdentification_ObjectIdentity = ObjectIdentity
pppIdentification = _PppIdentification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 17, 1)
)
_PppIDString_Type = DisplayString
_PppIDString_Object = MibScalar
pppIDString = _PppIDString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 17, 1, 1),
    _PppIDString_Type()
)
pppIDString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppIDString.setStatus("mandatory")
_PppIPAddress_Type = IpAddress
_PppIPAddress_Object = MibScalar
pppIPAddress = _PppIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 17, 1, 2),
    _PppIPAddress_Type()
)
pppIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIPAddress.setStatus("mandatory")
_Ccode_ObjectIdentity = ObjectIdentity
ccode = _Ccode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 18)
)
_CcodeLoaded_Type = Integer32
_CcodeLoaded_Object = MibScalar
ccodeLoaded = _CcodeLoaded_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 18, 1),
    _CcodeLoaded_Type()
)
ccodeLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccodeLoaded.setStatus("mandatory")
_CcodeRunning_Type = Integer32
_CcodeRunning_Object = MibScalar
ccodeRunning = _CcodeRunning_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 18, 2),
    _CcodeRunning_Type()
)
ccodeRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccodeRunning.setStatus("mandatory")
_CcodeStackMainWas_Type = Integer32
_CcodeStackMainWas_Object = MibScalar
ccodeStackMainWas = _CcodeStackMainWas_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 18, 3),
    _CcodeStackMainWas_Type()
)
ccodeStackMainWas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccodeStackMainWas.setStatus("mandatory")
_CcodeStackMainNow_Type = Integer32
_CcodeStackMainNow_Object = MibScalar
ccodeStackMainNow = _CcodeStackMainNow_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 18, 4),
    _CcodeStackMainNow_Type()
)
ccodeStackMainNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccodeStackMainNow.setStatus("mandatory")
_CcodeStackT2Was_Type = Integer32
_CcodeStackT2Was_Object = MibScalar
ccodeStackT2Was = _CcodeStackT2Was_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 18, 5),
    _CcodeStackT2Was_Type()
)
ccodeStackT2Was.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccodeStackT2Was.setStatus("mandatory")
_CcodeStackT2Was2_Type = Integer32
_CcodeStackT2Was2_Object = MibScalar
ccodeStackT2Was2 = _CcodeStackT2Was2_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 18, 6),
    _CcodeStackT2Was2_Type()
)
ccodeStackT2Was2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccodeStackT2Was2.setStatus("mandatory")
_Techsupport_ObjectIdentity = ObjectIdentity
techsupport = _Techsupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 1, 99)
)
_TechsupportInt1_Type = Integer32
_TechsupportInt1_Object = MibScalar
techsupportInt1 = _TechsupportInt1_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 99, 1),
    _TechsupportInt1_Type()
)
techsupportInt1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techsupportInt1.setStatus("mandatory")
_TechsupportInt2_Type = Integer32
_TechsupportInt2_Object = MibScalar
techsupportInt2 = _TechsupportInt2_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 99, 2),
    _TechsupportInt2_Type()
)
techsupportInt2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techsupportInt2.setStatus("mandatory")
_TechsupportInt3_Type = Integer32
_TechsupportInt3_Object = MibScalar
techsupportInt3 = _TechsupportInt3_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 99, 3),
    _TechsupportInt3_Type()
)
techsupportInt3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techsupportInt3.setStatus("mandatory")
_TechsupportInt4_Type = Integer32
_TechsupportInt4_Object = MibScalar
techsupportInt4 = _TechsupportInt4_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 99, 4),
    _TechsupportInt4_Type()
)
techsupportInt4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techsupportInt4.setStatus("mandatory")
_TechsupportInt5_Type = Integer32
_TechsupportInt5_Object = MibScalar
techsupportInt5 = _TechsupportInt5_Object(
    (1, 3, 6, 1, 4, 1, 3052, 1, 99, 5),
    _TechsupportInt5_Type()
)
techsupportInt5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techsupportInt5.setStatus("mandatory")

# Managed Objects groups


# Notification objects

datalinkDbasePfullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 0, 501)
)
datalinkDbasePfullTrap.setObjects(
      *(("DATALINK-MIB", "databaseAlarmIndex"),
        ("DATALINK-MIB", "databasePfull"))
)
if mibBuilder.loadTexts:
    datalinkDbasePfullTrap.setStatus(
        ""
    )

datalinkFilePfullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 0, 502)
)
datalinkFilePfullTrap.setObjects(
      *(("DATALINK-MIB", "fileAlarmFileIndex"),
        ("DATALINK-MIB", "fileAlarmThresholdIndex"),
        ("DATALINK-MIB", "filePercentNow"))
)
if mibBuilder.loadTexts:
    datalinkFilePfullTrap.setStatus(
        ""
    )

datalinkDataAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 0, 503)
)
datalinkDataAlarmTrap.setObjects(
      *(("DATALINK-MIB", "dataAlarmIndex"),
        ("DATALINK-MIB", "dataAlarmName"),
        ("DATALINK-MIB", "dataAlarmString"),
        ("DATALINK-MIB", "dataAlarmPort"))
)
if mibBuilder.loadTexts:
    datalinkDataAlarmTrap.setStatus(
        ""
    )

datalinkSensorAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 0, 504)
)
datalinkSensorAlarmTrap.setObjects(
      *(("DATALINK-MIB", "sensorAlarmIndex"),
        ("DATALINK-MIB", "sensorAlarmName"),
        ("DATALINK-MIB", "sensorAlarmState"))
)
if mibBuilder.loadTexts:
    datalinkSensorAlarmTrap.setStatus(
        ""
    )

datalinkNoDataAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 0, 505)
)
datalinkNoDataAlarmTrap.setObjects(
      *(("DATALINK-MIB", "nodataTablePortIndex"),
        ("DATALINK-MIB", "nodataTableScheduleIndex"),
        ("DATALINK-MIB", "nodataTableLevelIndex"),
        ("DATALINK-MIB", "nodataAlarmStatusCounter"),
        ("DATALINK-MIB", "nodataTableThreshold"))
)
if mibBuilder.loadTexts:
    datalinkNoDataAlarmTrap.setStatus(
        ""
    )

datalinkSchedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 0, 506)
)
datalinkSchedTrap.setObjects(
    ("DATALINK-MIB", "scheduleIndex")
)
if mibBuilder.loadTexts:
    datalinkSchedTrap.setStatus(
        ""
    )

datalinkImmediateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 0, 507)
)
if mibBuilder.loadTexts:
    datalinkImmediateTrap.setStatus(
        ""
    )

datalinkPPPupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 0, 509)
)
datalinkPPPupTrap.setObjects(
      *(("DATALINK-MIB", "pppIDString"),
        ("DATALINK-MIB", "pppIPAddress"))
)
if mibBuilder.loadTexts:
    datalinkPPPupTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DATALINK-MIB",
    **{"asentria": asentria,
       "datalinkDbasePfullTrap": datalinkDbasePfullTrap,
       "datalinkFilePfullTrap": datalinkFilePfullTrap,
       "datalinkDataAlarmTrap": datalinkDataAlarmTrap,
       "datalinkSensorAlarmTrap": datalinkSensorAlarmTrap,
       "datalinkNoDataAlarmTrap": datalinkNoDataAlarmTrap,
       "datalinkSchedTrap": datalinkSchedTrap,
       "datalinkImmediateTrap": datalinkImmediateTrap,
       "datalinkPPPupTrap": datalinkPPPupTrap,
       "datalink": datalink,
       "productIds": productIds,
       "datalinkThisProduct": datalinkThisProduct,
       "productConfig": productConfig,
       "productname": productname,
       "systemversion": systemversion,
       "appversion": appversion,
       "hardware": hardware,
       "numberports": numberports,
       "netcard": netcard,
       "modems": modems,
       "networkenabled": networkenabled,
       "memorysize": memorysize,
       "factorysetup": factorysetup,
       "modemreport": modemreport,
       "modemportspeed": modemportspeed,
       "modemsetupstring": modemsetupstring,
       "modemcddelay": modemcddelay,
       "modemtype": modemtype,
       "serialnumber": serialnumber,
       "dateofmanufacture": dateofmanufacture,
       "databasemode": databasemode,
       "unitIds": unitIds,
       "datalinkSiteId": datalinkSiteId,
       "idByPortTable": idByPortTable,
       "sitebyport": sitebyport,
       "siteindex": siteindex,
       "siteID": siteID,
       "serialPorts": serialPorts,
       "numberPorts": numberPorts,
       "portSetupTable": portSetupTable,
       "portSetupEntry": portSetupEntry,
       "portIndex": portIndex,
       "portBaud": portBaud,
       "portWord": portWord,
       "portParity": portParity,
       "portStopbits": portStopbits,
       "portDataStore": portDataStore,
       "portBinaryMode": portBinaryMode,
       "portWrapMode": portWrapMode,
       "portHskMode": portHskMode,
       "portDateTimeStampMode": portDateTimeStampMode,
       "portPTMode": portPTMode,
       "portPTTime": portPTTime,
       "portStoreFile": portStoreFile,
       "portPtStripOutputLfs": portPtStripOutputLfs,
       "portPtStripInputLfs": portPtStripInputLfs,
       "portlowDTR": portlowDTR,
       "time": time,
       "currenttime": currenttime,
       "autoDstAdjust": autoDstAdjust,
       "snmpsetup": snmpsetup,
       "snmpTrapsEnabled": snmpTrapsEnabled,
       "snmpManagerTable": snmpManagerTable,
       "snmpTableEntry": snmpTableEntry,
       "snmpMgrIndex": snmpMgrIndex,
       "snmpManagerIp": snmpManagerIp,
       "snmpManagerName": snmpManagerName,
       "snmpTrapsAutoRepeatTime": snmpTrapsAutoRepeatTime,
       "snmpSendTestTrap": snmpSendTestTrap,
       "passwords": passwords,
       "modemPasswords": modemPasswords,
       "tcpPasswords": tcpPasswords,
       "ftpPasswords": ftpPasswords,
       "promptPasswords": promptPasswords,
       "commandPassword": commandPassword,
       "commandNeedsPassword": commandNeedsPassword,
       "commandPasswordTimeout": commandPasswordTimeout,
       "passwordTable": passwordTable,
       "passwordTableEntry": passwordTableEntry,
       "passwordIndex": passwordIndex,
       "passwordCommand": passwordCommand,
       "passwordAccess": passwordAccess,
       "ftpsetup": ftpsetup,
       "ftpAutoDelete": ftpAutoDelete,
       "ftpDataMode": ftpDataMode,
       "ftpPush": ftpPush,
       "ftpPushEnabled": ftpPushEnabled,
       "ftpPushTiming": ftpPushTiming,
       "ftpPushTimer": ftpPushTimer,
       "ftpPushIPAddress": ftpPushIPAddress,
       "ftpPushUser": ftpPushUser,
       "ftpPushPass": ftpPushPass,
       "ftpPushAcct": ftpPushAcct,
       "ftpPushDir": ftpPushDir,
       "ftppushTable": ftppushTable,
       "ftppushTableEntry": ftppushTableEntry,
       "ftppushIndex": ftppushIndex,
       "ftppushEnable": ftppushEnable,
       "ftpPushAlarms": ftpPushAlarms,
       "ftpPushCount": ftpPushCount,
       "ftpPushStatusMode": ftpPushStatusMode,
       "ftpPushServerName": ftpPushServerName,
       "databases": databases,
       "entireDatabase": entireDatabase,
       "databaseStatus": databaseStatus,
       "databasePfull": databasePfull,
       "databaseSize": databaseSize,
       "databaseRecordsAvailable": databaseRecordsAvailable,
       "databaseRecordsDeleted": databaseRecordsDeleted,
       "databaseAlarmTable": databaseAlarmTable,
       "databaseAlarmEntry": databaseAlarmEntry,
       "databaseAlarmIndex": databaseAlarmIndex,
       "databaseAlarmActive": databaseAlarmActive,
       "databaseAlarmThreshold": databaseAlarmThreshold,
       "databaseAlarmBeeperActions": databaseAlarmBeeperActions,
       "databaseAlarmSerialActions": databaseAlarmSerialActions,
       "databaseAlarmPagerActions": databaseAlarmPagerActions,
       "databaseAlarmCalloutActions": databaseAlarmCalloutActions,
       "databaseAlarmTrapActions": databaseAlarmTrapActions,
       "databaseAlarmFileStore": databaseAlarmFileStore,
       "databaseAlarmFileMaxSize": databaseAlarmFileMaxSize,
       "databaseFiles": databaseFiles,
       "filesetup": filesetup,
       "charmaskEnabled": charmaskEnabled,
       "charmask": charmask,
       "maxRecordChars": maxRecordChars,
       "binRecordBlocking": binRecordBlocking,
       "recordCollectionTimeout": recordCollectionTimeout,
       "fileTable": fileTable,
       "fileTableEntry": fileTableEntry,
       "fileTableIndex": fileTableIndex,
       "fileName": fileName,
       "fileType": fileType,
       "fileSize": fileSize,
       "fileRecords": fileRecords,
       "fileRecordsAvailable": fileRecordsAvailable,
       "fileRecordsDeleted": fileRecordsDeleted,
       "filePercentNow": filePercentNow,
       "fileAlarms": fileAlarms,
       "fileAlarmEntry": fileAlarmEntry,
       "fileAlarmFileIndex": fileAlarmFileIndex,
       "fileAlarmThresholdIndex": fileAlarmThresholdIndex,
       "fileAlarmActive": fileAlarmActive,
       "fileAlarmThreshold": fileAlarmThreshold,
       "fileAlarmBeeperActions": fileAlarmBeeperActions,
       "fileAlarmSerialActions": fileAlarmSerialActions,
       "fileAlarmPagerActions": fileAlarmPagerActions,
       "fileAlarmCalloutActions": fileAlarmCalloutActions,
       "fileAlarmTrapActions": fileAlarmTrapActions,
       "alarms": alarms,
       "dataAlarmTable": dataAlarmTable,
       "dataAlarmEntry": dataAlarmEntry,
       "dataAlarmIndex": dataAlarmIndex,
       "dataAlarmActive": dataAlarmActive,
       "dataAlarmName": dataAlarmName,
       "dataAlarmCounter": dataAlarmCounter,
       "dataAlarmThreshold": dataAlarmThreshold,
       "dataAlarmClearMode": dataAlarmClearMode,
       "dataAlarmClearTime": dataAlarmClearTime,
       "dataAlarmAcked": dataAlarmAcked,
       "dataAlarmBeeperActions": dataAlarmBeeperActions,
       "dataAlarmSerialActions": dataAlarmSerialActions,
       "dataAlarmPagerActions": dataAlarmPagerActions,
       "dataAlarmCalloutActions": dataAlarmCalloutActions,
       "dataAlarmTrapActions": dataAlarmTrapActions,
       "dataAlarmString": dataAlarmString,
       "dataAlarmPort": dataAlarmPort,
       "dataAlarmAutoClear": dataAlarmAutoClear,
       "sensorAlarmTable": sensorAlarmTable,
       "sensorAlarmEntry": sensorAlarmEntry,
       "sensorAlarmIndex": sensorAlarmIndex,
       "sensorAlarmActive": sensorAlarmActive,
       "sensorAlarmName": sensorAlarmName,
       "sensorAlarmMode": sensorAlarmMode,
       "sensorAlarmCounter": sensorAlarmCounter,
       "sensorAlarmThreshold": sensorAlarmThreshold,
       "sensorAlarmAcked": sensorAlarmAcked,
       "sensorAlarmBeeperActions": sensorAlarmBeeperActions,
       "sensorAlarmSerialActions": sensorAlarmSerialActions,
       "sensorAlarmPagerActions": sensorAlarmPagerActions,
       "sensorAlarmCalloutActions": sensorAlarmCalloutActions,
       "sensorAlarmTrapActions": sensorAlarmTrapActions,
       "sensorAlarmState": sensorAlarmState,
       "nodataAlarms": nodataAlarms,
       "nodataAlarmStatus": nodataAlarmStatus,
       "nodataAlarmStatusEntry": nodataAlarmStatusEntry,
       "nodataAlarmStatusIndex": nodataAlarmStatusIndex,
       "nodataAlarmStatusCounter": nodataAlarmStatusCounter,
       "nodataAlarmStatusAcked": nodataAlarmStatusAcked,
       "nodataTable": nodataTable,
       "nodataTableEntry": nodataTableEntry,
       "nodataTablePortIndex": nodataTablePortIndex,
       "nodataTableScheduleIndex": nodataTableScheduleIndex,
       "nodataTableLevelIndex": nodataTableLevelIndex,
       "nodataTableActive": nodataTableActive,
       "nodataTableSchedule": nodataTableSchedule,
       "nodataTableThreshold": nodataTableThreshold,
       "nodataTableBeeperActions": nodataTableBeeperActions,
       "nodataTableSerialActions": nodataTableSerialActions,
       "nodataTablePagerActions": nodataTablePagerActions,
       "nodataTableCalloutActions": nodataTableCalloutActions,
       "nodataTableTrapActions": nodataTableTrapActions,
       "nodataAlarmHolidays": nodataAlarmHolidays,
       "nodataNumberHolidays": nodataNumberHolidays,
       "nodataHolidayTable": nodataHolidayTable,
       "nodataHolidayTableEntry": nodataHolidayTableEntry,
       "nodataHolidayIndex": nodataHolidayIndex,
       "nodataHolidayItem": nodataHolidayItem,
       "nodataHolidayAdd": nodataHolidayAdd,
       "nodataHolidayDelete": nodataHolidayDelete,
       "nodataHolidayClear": nodataHolidayClear,
       "scheduleAlarmTable": scheduleAlarmTable,
       "scheduleAlarmEntry": scheduleAlarmEntry,
       "scheduleIndex": scheduleIndex,
       "scheduleActive": scheduleActive,
       "scheduleTime": scheduleTime,
       "scheduleAcked": scheduleAcked,
       "scheduleBeeperActions": scheduleBeeperActions,
       "scheduleSerialActions": scheduleSerialActions,
       "schedulePagerActions": schedulePagerActions,
       "scheduleCalloutActions": scheduleCalloutActions,
       "scheduleTrapActions": scheduleTrapActions,
       "actions": actions,
       "actionsBuzzer": actionsBuzzer,
       "actionsBuzzerState": actionsBuzzerState,
       "actionsSerialTable": actionsSerialTable,
       "actionsSerialTableEntry": actionsSerialTableEntry,
       "serialTableIndex": serialTableIndex,
       "serialTableMessage": serialTableMessage,
       "actionsPagerTable": actionsPagerTable,
       "actionsPagerTableEntry": actionsPagerTableEntry,
       "pagerTableIndex": pagerTableIndex,
       "pagerType": pagerType,
       "pagerPhonenumber": pagerPhonenumber,
       "pagerID": pagerID,
       "pagerDialDelay": pagerDialDelay,
       "pagerHangupDelay": pagerHangupDelay,
       "pagerMessage": pagerMessage,
       "pagerSendId": pagerSendId,
       "pagerSendReason": pagerSendReason,
       "pagerMaxAttempts": pagerMaxAttempts,
       "pagerAttempts": pagerAttempts,
       "pagerAttemptDelay": pagerAttemptDelay,
       "pagerRepeat": pagerRepeat,
       "pagerRepeatDelay": pagerRepeatDelay,
       "actionsCalloutTable": actionsCalloutTable,
       "actionsCalloutTableEntry": actionsCalloutTableEntry,
       "calloutTableIndex": calloutTableIndex,
       "calloutPhonenumber": calloutPhonenumber,
       "calloutMaxConnecttime": calloutMaxConnecttime,
       "calloutMessage": calloutMessage,
       "calloutSendId": calloutSendId,
       "calloutSendReason": calloutSendReason,
       "calloutCommandWait": calloutCommandWait,
       "calloutMaxAttempts": calloutMaxAttempts,
       "calloutAttempts": calloutAttempts,
       "calloutAttemptDelay": calloutAttemptDelay,
       "calloutRepeat": calloutRepeat,
       "calloutRepeatDelay": calloutRepeatDelay,
       "actionsTraps": actionsTraps,
       "actionsTrapsEntSpecific": actionsTrapsEntSpecific,
       "actionsTrapsEntSpecCount": actionsTrapsEntSpecCount,
       "controls": controls,
       "opSettings": opSettings,
       "linefeeds": linefeeds,
       "duplex": duplex,
       "response": response,
       "datafilterEnabled": datafilterEnabled,
       "alarmfilterEnabled": alarmfilterEnabled,
       "auxportMode": auxportMode,
       "operatingMode": operatingMode,
       "inlineMode": inlineMode,
       "inlineSource": inlineSource,
       "inlineHskMode": inlineHskMode,
       "inlineHsk2": inlineHsk2,
       "inlineHsk4": inlineHsk4,
       "inlineHsk6": inlineHsk6,
       "sureEnabled": sureEnabled,
       "commandTcpipTimeout": commandTcpipTimeout,
       "sysadminTcpipTimeout": sysadminTcpipTimeout,
       "bypassEndchar": bypassEndchar,
       "routerAutoPing": routerAutoPing,
       "modemSettings": modemSettings,
       "modemParity": modemParity,
       "modemUserSetup": modemUserSetup,
       "modemTapSetup": modemTapSetup,
       "modemAnswerString": modemAnswerString,
       "modemExtSetup": modemExtSetup,
       "modemExtSetupTime": modemExtSetupTime,
       "modemInactivityTimer": modemInactivityTimer,
       "modemAutoexecString": modemAutoexecString,
       "modemAutoexecEnabled": modemAutoexecEnabled,
       "modemTimeBetweenOutbound": modemTimeBetweenOutbound,
       "dataRelease": dataRelease,
       "releaseMode": releaseMode,
       "autodeleteEnable": autodeleteEnable,
       "releaseCompressed": releaseCompressed,
       "otherControls": otherControls,
       "waitMode": waitMode,
       "tagMode": tagMode,
       "crcMode": crcMode,
       "dleMode": dleMode,
       "cbbRetransmits": cbbRetransmits,
       "cbbTimeout": cbbTimeout,
       "activeDatabase": activeDatabase,
       "alarmhistory": alarmhistory,
       "actionQueue": actionQueue,
       "actionCount": actionCount,
       "actionTable": actionTable,
       "actionTableEntry": actionTableEntry,
       "actionTableIndex": actionTableIndex,
       "actionAcked": actionAcked,
       "actionReason": actionReason,
       "actionReasonID": actionReasonID,
       "actionReasonLevel": actionReasonLevel,
       "actionType": actionType,
       "actionTypeID": actionTypeID,
       "actionRepeatTime": actionRepeatTime,
       "actionAttempts": actionAttempts,
       "actionNextAttempt": actionNextAttempt,
       "actionTimeStamp": actionTimeStamp,
       "actionHistory": actionHistory,
       "historyCount": historyCount,
       "historyTable": historyTable,
       "historyTableEntry": historyTableEntry,
       "historyTableIndex": historyTableIndex,
       "historyEntryType": historyEntryType,
       "historyReason": historyReason,
       "historyReasonID": historyReasonID,
       "historyReasonLevel": historyReasonLevel,
       "historyType": historyType,
       "historyTypeID": historyTypeID,
       "historyTimeStamp": historyTimeStamp,
       "historyClearLog": historyClearLog,
       "lastCalloutPageReason": lastCalloutPageReason,
       "realtimesocket": realtimesocket,
       "rtsShowAnswer": rtsShowAnswer,
       "rtsNeedPassword": rtsNeedPassword,
       "rtsWaitXon": rtsWaitXon,
       "rtsIdleTimeout": rtsIdleTimeout,
       "rtsEmptyClose": rtsEmptyClose,
       "rtsTable": rtsTable,
       "rtsTableEntry": rtsTableEntry,
       "rtsTableIndex": rtsTableIndex,
       "rtsNoStore": rtsNoStore,
       "rtsDenied": rtsDenied,
       "rtsSocketState": rtsSocketState,
       "rtsPortShowAnswer": rtsPortShowAnswer,
       "rtsPortNeedPassword": rtsPortNeedPassword,
       "rtsPortWaitXon": rtsPortWaitXon,
       "rtsPortIdleTimeout": rtsPortIdleTimeout,
       "rtsPortEmptyClose": rtsPortEmptyClose,
       "iprestrictions": iprestrictions,
       "iprestrictTable": iprestrictTable,
       "iprestrictTableEntry": iprestrictTableEntry,
       "iprestrictTableIndex": iprestrictTableIndex,
       "iprestrictIpAddress": iprestrictIpAddress,
       "suspendIPRestrictions": suspendIPRestrictions,
       "killIPRestrictions": killIPRestrictions,
       "addIPRestrictions": addIPRestrictions,
       "ipsetup": ipsetup,
       "ipCurrent": ipCurrent,
       "ipCurrentStatic": ipCurrentStatic,
       "ipCurrentAddress": ipCurrentAddress,
       "ipCurrentSubnetMask": ipCurrentSubnetMask,
       "ipCurrentDefaultRouter": ipCurrentDefaultRouter,
       "ipNew": ipNew,
       "ipNewStatic": ipNewStatic,
       "ipNewAddress": ipNewAddress,
       "ipNewSubnetMask": ipNewSubnetMask,
       "ipNewDefaultRouter": ipNewDefaultRouter,
       "ipNewSetup": ipNewSetup,
       "pppsetup": pppsetup,
       "pppIdentification": pppIdentification,
       "pppIDString": pppIDString,
       "pppIPAddress": pppIPAddress,
       "ccode": ccode,
       "ccodeLoaded": ccodeLoaded,
       "ccodeRunning": ccodeRunning,
       "ccodeStackMainWas": ccodeStackMainWas,
       "ccodeStackMainNow": ccodeStackMainNow,
       "ccodeStackT2Was": ccodeStackT2Was,
       "ccodeStackT2Was2": ccodeStackT2Was2,
       "techsupport": techsupport,
       "techsupportInt1": techsupportInt1,
       "techsupportInt2": techsupportInt2,
       "techsupportInt3": techsupportInt3,
       "techsupportInt4": techsupportInt4,
       "techsupportInt5": techsupportInt5}
)
