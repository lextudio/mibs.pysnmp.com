# SNMP MIB module (AGGREGATED-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AGGREGATED-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:56 2024
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
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "snmpModules")

(DisplayString,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

softSwitch = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lucent_ObjectIdentity = ObjectIdentity
lucent = _Lucent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1)
)
_Excel_ObjectIdentity = ObjectIdentity
excel = _Excel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67)
)
_Excel1_ObjectIdentity = ObjectIdentity
excel1 = _Excel1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 1)
)
_Excel2_ObjectIdentity = ObjectIdentity
excel2 = _Excel2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2)
)
_Excel3_ObjectIdentity = ObjectIdentity
excel3 = _Excel3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 3)
)
_Excel4_ObjectIdentity = ObjectIdentity
excel4 = _Excel4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 4)
)
_H323DeviceServer_ObjectIdentity = ObjectIdentity
h323DeviceServer = _H323DeviceServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 3)
)
_H323DS1_ObjectIdentity = ObjectIdentity
h323DS1 = _H323DS1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 3, 1)
)
_H323DS2_ObjectIdentity = ObjectIdentity
h323DS2 = _H323DS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 3, 2)
)
_ResourceMonitor_ObjectIdentity = ObjectIdentity
resourceMonitor = _ResourceMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4)
)
_Rm1_ObjectIdentity = ObjectIdentity
rm1 = _Rm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 1)
)
_Rm2_ObjectIdentity = ObjectIdentity
rm2 = _Rm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2)
)
_Rm3_ObjectIdentity = ObjectIdentity
rm3 = _Rm3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3)
)
_Rm4_ObjectIdentity = ObjectIdentity
rm4 = _Rm4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 4)
)
_SipDeviceServer_ObjectIdentity = ObjectIdentity
sipDeviceServer = _SipDeviceServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5)
)
_SipDS1_ObjectIdentity = ObjectIdentity
sipDS1 = _SipDS1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 1)
)
_SipDS2_ObjectIdentity = ObjectIdentity
sipDS2 = _SipDS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 2)
)
_PsaxDeviceServer_ObjectIdentity = ObjectIdentity
psaxDeviceServer = _PsaxDeviceServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 6)
)
_PsaxDS1_ObjectIdentity = ObjectIdentity
psaxDS1 = _PsaxDS1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 6, 1)
)
_PsaxDS2_ObjectIdentity = ObjectIdentity
psaxDS2 = _PsaxDS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 6, 2)
)
_CdrDeviceServer_ObjectIdentity = ObjectIdentity
cdrDeviceServer = _CdrDeviceServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7)
)
_CdrDS1_ObjectIdentity = ObjectIdentity
cdrDS1 = _CdrDS1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 1)
)
_CdrDS2_ObjectIdentity = ObjectIdentity
cdrDS2 = _CdrDS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2)
)
_SpinsDeviceServer_ObjectIdentity = ObjectIdentity
spinsDeviceServer = _SpinsDeviceServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 8)
)
_SpinsDS1_ObjectIdentity = ObjectIdentity
spinsDS1 = _SpinsDS1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 8, 1)
)
_SpinsDS2_ObjectIdentity = ObjectIdentity
spinsDS2 = _SpinsDS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 8, 2)
)
_FcDeviceServer_ObjectIdentity = ObjectIdentity
fcDeviceServer = _FcDeviceServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9)
)
_FcDS1_ObjectIdentity = ObjectIdentity
fcDS1 = _FcDS1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 1)
)
_FcDS2_ObjectIdentity = ObjectIdentity
fcDS2 = _FcDS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 2)
)
_SoftswitchTraps_ObjectIdentity = ObjectIdentity
softswitchTraps = _SoftswitchTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10)
)
_MantraTrapVars_ObjectIdentity = ObjectIdentity
mantraTrapVars = _MantraTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 1)
)
_PepName_Type = DisplayString
_PepName_Object = MibScalar
pepName = _PepName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 1, 1),
    _PepName_Type()
)
pepName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pepName.setStatus("current")
_DevName_Type = DisplayString
_DevName_Object = MibScalar
devName = _DevName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 1, 2),
    _DevName_Type()
)
devName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    devName.setStatus("current")
_File_Type = DisplayString
_File_Object = MibScalar
file = _File_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 1, 3),
    _File_Type()
)
file.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    file.setStatus("current")
_Host_Type = DisplayString
_Host_Object = MibScalar
host = _Host_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 1, 4),
    _Host_Type()
)
host.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    host.setStatus("current")


class _Port_Type(Integer32):
    """Custom type port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 32565),
    )


_Port_Type.__name__ = "Integer32"
_Port_Object = MibScalar
port = _Port_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 1, 5),
    _Port_Type()
)
port.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    port.setStatus("current")
_OldFile_Type = DisplayString
_OldFile_Object = MibScalar
oldFile = _OldFile_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 1, 6),
    _OldFile_Type()
)
oldFile.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    oldFile.setStatus("current")
_NewFile_Type = DisplayString
_NewFile_Object = MibScalar
newFile = _NewFile_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 1, 7),
    _NewFile_Type()
)
newFile.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    newFile.setStatus("current")
_Minutes_Type = DisplayString
_Minutes_Object = MibScalar
minutes = _Minutes_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 1, 8),
    _Minutes_Type()
)
minutes.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    minutes.setStatus("current")
_Result_Type = DisplayString
_Result_Object = MibScalar
result = _Result_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 1, 9),
    _Result_Type()
)
result.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    result.setStatus("current")
_Reason_Type = DisplayString
_Reason_Object = MibScalar
reason = _Reason_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 1, 10),
    _Reason_Type()
)
reason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    reason.setStatus("current")
_SnName_Type = DisplayString
_SnName_Object = MibScalar
snName = _SnName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 1, 11),
    _SnName_Type()
)
snName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    snName.setStatus("current")
_MyHost_Type = DisplayString
_MyHost_Object = MibScalar
myHost = _MyHost_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 1, 12),
    _MyHost_Type()
)
myHost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    myHost.setStatus("current")


class _MyPort_Type(Integer32):
    """Custom type myPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 32565),
    )


_MyPort_Type.__name__ = "Integer32"
_MyPort_Object = MibScalar
myPort = _MyPort_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 1, 13),
    _MyPort_Type()
)
myPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    myPort.setStatus("current")
_MateHost_Type = DisplayString
_MateHost_Object = MibScalar
mateHost = _MateHost_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 1, 14),
    _MateHost_Type()
)
mateHost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mateHost.setStatus("current")


class _MatePort_Type(Integer32):
    """Custom type matePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 32565),
    )


_MatePort_Type.__name__ = "Integer32"
_MatePort_Object = MibScalar
matePort = _MatePort_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 1, 15),
    _MatePort_Type()
)
matePort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    matePort.setStatus("current")
_DeviceType_Type = DisplayString
_DeviceType_Object = MibScalar
deviceType = _DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 1, 16),
    _DeviceType_Type()
)
deviceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    deviceType.setStatus("current")
_Domain_Type = DisplayString
_Domain_Object = MibScalar
domain = _Domain_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 1, 17),
    _Domain_Type()
)
domain.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    domain.setStatus("current")
_Group_Type = DisplayString
_Group_Object = MibScalar
group = _Group_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 1, 18),
    _Group_Type()
)
group.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    group.setStatus("current")
_Name_Type = DisplayString
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 1, 19),
    _Name_Type()
)
name.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    name.setStatus("current")


class _RunStatus_Type(Integer32):
    """Custom type runStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_RunStatus_Type.__name__ = "Integer32"
_RunStatus_Object = MibScalar
runStatus = _RunStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 1, 20),
    _RunStatus_Type()
)
runStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    runStatus.setStatus("current")
_H323TrapVariables_ObjectIdentity = ObjectIdentity
h323TrapVariables = _H323TrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 2)
)
_TimeOccurred_Type = DisplayString
_TimeOccurred_Object = MibScalar
timeOccurred = _TimeOccurred_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 2, 1),
    _TimeOccurred_Type()
)
timeOccurred.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    timeOccurred.setStatus("current")


class _Code_Type(Integer32):
    """Custom type code based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Code_Type.__name__ = "Integer32"
_Code_Object = MibScalar
code = _Code_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 2, 2),
    _Code_Type()
)
code.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    code.setStatus("current")


class _CsID_Type(Integer32):
    """Custom type csID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CsID_Type.__name__ = "Integer32"
_CsID_Object = MibScalar
csID = _CsID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 2, 3),
    _CsID_Type()
)
csID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csID.setStatus("current")
_CsType_Type = DisplayString
_CsType_Object = MibScalar
csType = _CsType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 2, 4),
    _CsType_Type()
)
csType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csType.setStatus("current")
_RegistrationStatus_Type = DisplayString
_RegistrationStatus_Object = MibScalar
registrationStatus = _RegistrationStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 2, 5),
    _RegistrationStatus_Type()
)
registrationStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    registrationStatus.setStatus("current")
_Comment_Type = DisplayString
_Comment_Object = MibScalar
comment = _Comment_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 2, 6),
    _Comment_Type()
)
comment.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    comment.setStatus("current")
_GwID_Type = DisplayString
_GwID_Object = MibScalar
gwID = _GwID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 2, 7),
    _GwID_Type()
)
gwID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gwID.setStatus("current")


class _ModuleID_Type(Integer32):
    """Custom type moduleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ModuleID_Type.__name__ = "Integer32"
_ModuleID_Object = MibScalar
moduleID = _ModuleID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 2, 8),
    _ModuleID_Type()
)
moduleID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    moduleID.setStatus("current")


class _Percent_Type(Integer32):
    """Custom type percent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Percent_Type.__name__ = "Integer32"
_Percent_Object = MibScalar
percent = _Percent_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 2, 9),
    _Percent_Type()
)
percent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    percent.setStatus("current")
_GwIP_Type = IpAddress
_GwIP_Object = MibScalar
gwIP = _GwIP_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 2, 10),
    _GwIP_Type()
)
gwIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gwIP.setStatus("current")


class _GwType_Type(Integer32):
    """Custom type gwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_GwType_Type.__name__ = "Integer32"
_GwType_Object = MibScalar
gwType = _GwType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 2, 11),
    _GwType_Type()
)
gwType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gwType.setStatus("current")
_RmTrapVariables_ObjectIdentity = ObjectIdentity
rmTrapVariables = _RmTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 3)
)


class _Percentage_Type(Integer32):
    """Custom type percentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Percentage_Type.__name__ = "Integer32"
_Percentage_Object = MibScalar
percentage = _Percentage_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 3, 1),
    _Percentage_Type()
)
percentage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    percentage.setStatus("current")


class _Status_Type(Integer32):
    """Custom type status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Status_Type.__name__ = "Integer32"
_Status_Object = MibScalar
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 3, 2),
    _Status_Type()
)
status.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    status.setStatus("current")


class _Load_Type(Integer32):
    """Custom type load based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Load_Type.__name__ = "Integer32"
_Load_Object = MibScalar
load = _Load_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 3, 3),
    _Load_Type()
)
load.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    load.setStatus("current")
_Disk_Type = DisplayString
_Disk_Object = MibScalar
disk = _Disk_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 3, 4),
    _Disk_Type()
)
disk.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    disk.setStatus("current")


class _CurSize_Type(Integer32):
    """Custom type curSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CurSize_Type.__name__ = "Integer32"
_CurSize_Object = MibScalar
curSize = _CurSize_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 3, 5),
    _CurSize_Type()
)
curSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    curSize.setStatus("current")


class _MaxSize_Type(Integer32):
    """Custom type maxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_MaxSize_Type.__name__ = "Integer32"
_MaxSize_Object = MibScalar
maxSize = _MaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 3, 6),
    _MaxSize_Type()
)
maxSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    maxSize.setStatus("current")
_ProcessName_Type = DisplayString
_ProcessName_Object = MibScalar
processName = _ProcessName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 3, 7),
    _ProcessName_Type()
)
processName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    processName.setStatus("current")


class _ProcessID_Type(Integer32):
    """Custom type processID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ProcessID_Type.__name__ = "Integer32"
_ProcessID_Object = MibScalar
processID = _ProcessID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 3, 8),
    _ProcessID_Type()
)
processID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    processID.setStatus("current")


class _CpuUsage_Type(Integer32):
    """Custom type cpuUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CpuUsage_Type.__name__ = "Integer32"
_CpuUsage_Object = MibScalar
cpuUsage = _CpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 3, 9),
    _CpuUsage_Type()
)
cpuUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cpuUsage.setStatus("current")


class _MemUsage_Type(Integer32):
    """Custom type memUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_MemUsage_Type.__name__ = "Integer32"
_MemUsage_Object = MibScalar
memUsage = _MemUsage_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 3, 10),
    _MemUsage_Type()
)
memUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    memUsage.setStatus("current")
_FcTrapVariables_ObjectIdentity = ObjectIdentity
fcTrapVariables = _FcTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 4)
)
_SbProducerHost_Type = DisplayString
_SbProducerHost_Object = MibScalar
sbProducerHost = _SbProducerHost_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 4, 1),
    _SbProducerHost_Type()
)
sbProducerHost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sbProducerHost.setStatus("current")


class _SbProducerPort_Type(Integer32):
    """Custom type sbProducerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_SbProducerPort_Type.__name__ = "Integer32"
_SbProducerPort_Object = MibScalar
sbProducerPort = _SbProducerPort_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 10, 4, 2),
    _SbProducerPort_Type()
)
sbProducerPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sbProducerPort.setStatus("current")
_UnknownDeviceTrapContents_Type = DisplayString
_UnknownDeviceTrapContents_Object = MibScalar
unknownDeviceTrapContents = _UnknownDeviceTrapContents_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 98),
    _UnknownDeviceTrapContents_Type()
)
unknownDeviceTrapContents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unknownDeviceTrapContents.setStatus("current")
_MantraAdmin_ObjectIdentity = ObjectIdentity
mantraAdmin = _MantraAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 99)
)
_MantraTraps_ObjectIdentity = ObjectIdentity
mantraTraps = _MantraTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 99, 0)
)
_LastAggNode_Type = DisplayString
_LastAggNode_Object = MibScalar
lastAggNode = _LastAggNode_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 100),
    _LastAggNode_Type()
)
lastAggNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastAggNode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AGGREGATED-EXT-MIB",
    **{"lucent": lucent,
       "products": products,
       "excel": excel,
       "excel1": excel1,
       "excel2": excel2,
       "excel3": excel3,
       "excel4": excel4,
       "softSwitch": softSwitch,
       "h323DeviceServer": h323DeviceServer,
       "h323DS1": h323DS1,
       "h323DS2": h323DS2,
       "resourceMonitor": resourceMonitor,
       "rm1": rm1,
       "rm2": rm2,
       "rm3": rm3,
       "rm4": rm4,
       "sipDeviceServer": sipDeviceServer,
       "sipDS1": sipDS1,
       "sipDS2": sipDS2,
       "psaxDeviceServer": psaxDeviceServer,
       "psaxDS1": psaxDS1,
       "psaxDS2": psaxDS2,
       "cdrDeviceServer": cdrDeviceServer,
       "cdrDS1": cdrDS1,
       "cdrDS2": cdrDS2,
       "spinsDeviceServer": spinsDeviceServer,
       "spinsDS1": spinsDS1,
       "spinsDS2": spinsDS2,
       "fcDeviceServer": fcDeviceServer,
       "fcDS1": fcDS1,
       "fcDS2": fcDS2,
       "softswitchTraps": softswitchTraps,
       "mantraTrapVars": mantraTrapVars,
       "pepName": pepName,
       "devName": devName,
       "file": file,
       "host": host,
       "port": port,
       "oldFile": oldFile,
       "newFile": newFile,
       "minutes": minutes,
       "result": result,
       "reason": reason,
       "snName": snName,
       "myHost": myHost,
       "myPort": myPort,
       "mateHost": mateHost,
       "matePort": matePort,
       "deviceType": deviceType,
       "domain": domain,
       "group": group,
       "name": name,
       "runStatus": runStatus,
       "h323TrapVariables": h323TrapVariables,
       "timeOccurred": timeOccurred,
       "code": code,
       "csID": csID,
       "csType": csType,
       "registrationStatus": registrationStatus,
       "comment": comment,
       "gwID": gwID,
       "moduleID": moduleID,
       "percent": percent,
       "gwIP": gwIP,
       "gwType": gwType,
       "rmTrapVariables": rmTrapVariables,
       "percentage": percentage,
       "status": status,
       "load": load,
       "disk": disk,
       "curSize": curSize,
       "maxSize": maxSize,
       "processName": processName,
       "processID": processID,
       "cpuUsage": cpuUsage,
       "memUsage": memUsage,
       "fcTrapVariables": fcTrapVariables,
       "sbProducerHost": sbProducerHost,
       "sbProducerPort": sbProducerPort,
       "unknownDeviceTrapContents": unknownDeviceTrapContents,
       "mantraAdmin": mantraAdmin,
       "mantraTraps": mantraTraps,
       "lastAggNode": lastAggNode}
)
