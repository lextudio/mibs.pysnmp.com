# SNMP MIB module (NSS324-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NSS324-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:35 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

nssAthens = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114)
)
nssAthens.setRevisions(
        ("2011-03-24 00:00",)
)


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cisco_ObjectIdentity = ObjectIdentity
cisco = _Cisco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9)
)
_OtherEnterprises_ObjectIdentity = ObjectIdentity
otherEnterprises = _OtherEnterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6)
)
_CiscoSB_ObjectIdentity = ObjectIdentity
ciscoSB = _CiscoSB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1)
)
_Nas004_ObjectIdentity = ObjectIdentity
nas004 = _Nas004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103)
)
_Nss_ObjectIdentity = ObjectIdentity
nss = _Nss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41)
)
_Nss324_ObjectIdentity = ObjectIdentity
nss324 = _Nss324_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324)
)
_StorageSystem_ObjectIdentity = ObjectIdentity
storageSystem = _StorageSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1)
)
_SystemEventMsg_ObjectIdentity = ObjectIdentity
systemEventMsg = _SystemEventMsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 1)
)
_EventInformMsg_Type = DisplayString
_EventInformMsg_Object = MibScalar
eventInformMsg = _EventInformMsg_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 1, 101),
    _EventInformMsg_Type()
)
eventInformMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInformMsg.setStatus("current")
_EventWarningMsg_Type = DisplayString
_EventWarningMsg_Object = MibScalar
eventWarningMsg = _EventWarningMsg_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 1, 102),
    _EventWarningMsg_Type()
)
eventWarningMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventWarningMsg.setStatus("current")
_EventErrorMsg_Type = DisplayString
_EventErrorMsg_Object = MibScalar
eventErrorMsg = _EventErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 1, 103),
    _EventErrorMsg_Type()
)
eventErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventErrorMsg.setStatus("current")
_SystemInfo_ObjectIdentity = ObjectIdentity
systemInfo = _SystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2)
)
_SystemCPU_Usage_Type = DisplayString
_SystemCPU_Usage_Object = MibScalar
systemCPU_Usage = _SystemCPU_Usage_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 1),
    _SystemCPU_Usage_Type()
)
systemCPU_Usage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCPU_Usage.setStatus("current")
_SystemTotalMem_Type = DisplayString
_SystemTotalMem_Object = MibScalar
systemTotalMem = _SystemTotalMem_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 2),
    _SystemTotalMem_Type()
)
systemTotalMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTotalMem.setStatus("current")
_SystemFreeMem_Type = DisplayString
_SystemFreeMem_Object = MibScalar
systemFreeMem = _SystemFreeMem_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 3),
    _SystemFreeMem_Type()
)
systemFreeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFreeMem.setStatus("current")
_SystemUptime_Type = TimeTicks
_SystemUptime_Object = MibScalar
systemUptime = _SystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 4),
    _SystemUptime_Type()
)
systemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUptime.setStatus("current")
_Cpu_Temperature_Type = DisplayString
_Cpu_Temperature_Object = MibScalar
cpu_Temperature = _Cpu_Temperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 5),
    _Cpu_Temperature_Type()
)
cpu_Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpu_Temperature.setStatus("current")
_SystemTemperature_Type = DisplayString
_SystemTemperature_Object = MibScalar
systemTemperature = _SystemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 6),
    _SystemTemperature_Type()
)
systemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTemperature.setStatus("current")
_IfNumber_Type = Integer32
_IfNumber_Object = MibScalar
ifNumber = _IfNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 8),
    _IfNumber_Type()
)
ifNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifNumber.setStatus("mandatory")
_SystemIfTable_Object = MibTable
systemIfTable = _SystemIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 9)
)
if mibBuilder.loadTexts:
    systemIfTable.setStatus("mandatory")
_IfEntry_Object = MibTableRow
ifEntry = _IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 9, 1)
)
ifEntry.setIndexNames(
    (0, "NSS324-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ifEntry.setStatus("mandatory")
_IfIndex_Type = Integer32
_IfIndex_Object = MibTableColumn
ifIndex = _IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 9, 1, 1),
    _IfIndex_Type()
)
ifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIndex.setStatus("mandatory")


class _IfDescr_Type(DisplayString):
    """Custom type ifDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IfDescr_Type.__name__ = "DisplayString"
_IfDescr_Object = MibTableColumn
ifDescr = _IfDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 9, 1, 2),
    _IfDescr_Type()
)
ifDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifDescr.setStatus("mandatory")
_IfPacketsReceived_Type = Counter32
_IfPacketsReceived_Object = MibTableColumn
ifPacketsReceived = _IfPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 9, 1, 3),
    _IfPacketsReceived_Type()
)
ifPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPacketsReceived.setStatus("mandatory")
_IfPacketsSent_Type = Counter32
_IfPacketsSent_Object = MibTableColumn
ifPacketsSent = _IfPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 9, 1, 4),
    _IfPacketsSent_Type()
)
ifPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPacketsSent.setStatus("mandatory")
_IfErrorPackets_Type = Counter32
_IfErrorPackets_Object = MibTableColumn
ifErrorPackets = _IfErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 9, 1, 5),
    _IfErrorPackets_Type()
)
ifErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifErrorPackets.setStatus("mandatory")
_HdNumber_Type = Integer32
_HdNumber_Object = MibScalar
hdNumber = _HdNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 10),
    _HdNumber_Type()
)
hdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdNumber.setStatus("mandatory")
_SystemHdTable_Object = MibTable
systemHdTable = _SystemHdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 11)
)
if mibBuilder.loadTexts:
    systemHdTable.setStatus("mandatory")
_HdEntry_Object = MibTableRow
hdEntry = _HdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 11, 1)
)
hdEntry.setIndexNames(
    (0, "NSS324-MIB", "hdIndex"),
)
if mibBuilder.loadTexts:
    hdEntry.setStatus("mandatory")
_HdIndex_Type = Integer32
_HdIndex_Object = MibTableColumn
hdIndex = _HdIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 11, 1, 1),
    _HdIndex_Type()
)
hdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdIndex.setStatus("mandatory")


class _HdDescr_Type(DisplayString):
    """Custom type hdDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HdDescr_Type.__name__ = "DisplayString"
_HdDescr_Object = MibTableColumn
hdDescr = _HdDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 11, 1, 2),
    _HdDescr_Type()
)
hdDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdDescr.setStatus("mandatory")
_HdTemperature_Type = DisplayString
_HdTemperature_Object = MibTableColumn
hdTemperature = _HdTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 11, 1, 3),
    _HdTemperature_Type()
)
hdTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdTemperature.setStatus("mandatory")


class _HdStatus_Type(Integer32):
    """Custom type hdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-9,
              -6,
              -5,
              -4,
              0)
        )
    )
    namedValues = NamedValues(
        *(("invalid", -6),
          ("noDisk", -5),
          ("ready", 0),
          ("rwError", -9),
          ("unknown", -4))
    )


_HdStatus_Type.__name__ = "Integer32"
_HdStatus_Object = MibTableColumn
hdStatus = _HdStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 11, 1, 4),
    _HdStatus_Type()
)
hdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdStatus.setStatus("mandatory")
_HdModel_Type = DisplayString
_HdModel_Object = MibTableColumn
hdModel = _HdModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 11, 1, 5),
    _HdModel_Type()
)
hdModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdModel.setStatus("mandatory")
_HdCapacity_Type = DisplayString
_HdCapacity_Object = MibTableColumn
hdCapacity = _HdCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 11, 1, 6),
    _HdCapacity_Type()
)
hdCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdCapacity.setStatus("mandatory")
_HdSmartInfo_Type = DisplayString
_HdSmartInfo_Object = MibTableColumn
hdSmartInfo = _HdSmartInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 11, 1, 7),
    _HdSmartInfo_Type()
)
hdSmartInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdSmartInfo.setStatus("mandatory")
_ModelName_Type = DisplayString
_ModelName_Object = MibScalar
modelName = _ModelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 12),
    _ModelName_Type()
)
modelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelName.setStatus("current")
_HostName_Type = DisplayString
_HostName_Object = MibScalar
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 13),
    _HostName_Type()
)
hostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostName.setStatus("current")
_SysFanNumber_Type = Integer32
_SysFanNumber_Object = MibScalar
sysFanNumber = _SysFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 14),
    _SysFanNumber_Type()
)
sysFanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFanNumber.setStatus("mandatory")
_SystemFanTable_Object = MibTable
systemFanTable = _SystemFanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 15)
)
if mibBuilder.loadTexts:
    systemFanTable.setStatus("mandatory")
_SysFanEntry_Object = MibTableRow
sysFanEntry = _SysFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 15, 1)
)
sysFanEntry.setIndexNames(
    (0, "NSS324-MIB", "sysFanIndex"),
)
if mibBuilder.loadTexts:
    sysFanEntry.setStatus("mandatory")
_SysFanIndex_Type = Integer32
_SysFanIndex_Object = MibTableColumn
sysFanIndex = _SysFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 15, 1, 1),
    _SysFanIndex_Type()
)
sysFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFanIndex.setStatus("mandatory")


class _SysFanDescr_Type(DisplayString):
    """Custom type sysFanDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysFanDescr_Type.__name__ = "DisplayString"
_SysFanDescr_Object = MibTableColumn
sysFanDescr = _SysFanDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 15, 1, 2),
    _SysFanDescr_Type()
)
sysFanDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFanDescr.setStatus("mandatory")


class _SysFanSpeed_Type(DisplayString):
    """Custom type sysFanSpeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysFanSpeed_Type.__name__ = "DisplayString"
_SysFanSpeed_Object = MibTableColumn
sysFanSpeed = _SysFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 15, 1, 3),
    _SysFanSpeed_Type()
)
sysFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFanSpeed.setStatus("mandatory")
_SysVolumeNumber_Type = Integer32
_SysVolumeNumber_Object = MibScalar
sysVolumeNumber = _SysVolumeNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 16),
    _SysVolumeNumber_Type()
)
sysVolumeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVolumeNumber.setStatus("mandatory")
_SystemVolumeTable_Object = MibTable
systemVolumeTable = _SystemVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 17)
)
if mibBuilder.loadTexts:
    systemVolumeTable.setStatus("mandatory")
_SysVolumeEntry_Object = MibTableRow
sysVolumeEntry = _SysVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 17, 1)
)
sysVolumeEntry.setIndexNames(
    (0, "NSS324-MIB", "sysVolumeIndex"),
)
if mibBuilder.loadTexts:
    sysVolumeEntry.setStatus("mandatory")
_SysVolumeIndex_Type = Integer32
_SysVolumeIndex_Object = MibTableColumn
sysVolumeIndex = _SysVolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 17, 1, 1),
    _SysVolumeIndex_Type()
)
sysVolumeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVolumeIndex.setStatus("mandatory")


class _SysVolumeDescr_Type(DisplayString):
    """Custom type sysVolumeDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysVolumeDescr_Type.__name__ = "DisplayString"
_SysVolumeDescr_Object = MibTableColumn
sysVolumeDescr = _SysVolumeDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 17, 1, 2),
    _SysVolumeDescr_Type()
)
sysVolumeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVolumeDescr.setStatus("mandatory")


class _SysVolumeFS_Type(DisplayString):
    """Custom type sysVolumeFS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SysVolumeFS_Type.__name__ = "DisplayString"
_SysVolumeFS_Object = MibTableColumn
sysVolumeFS = _SysVolumeFS_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 17, 1, 3),
    _SysVolumeFS_Type()
)
sysVolumeFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVolumeFS.setStatus("mandatory")


class _SysVolumeTotalSize_Type(DisplayString):
    """Custom type sysVolumeTotalSize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SysVolumeTotalSize_Type.__name__ = "DisplayString"
_SysVolumeTotalSize_Object = MibTableColumn
sysVolumeTotalSize = _SysVolumeTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 17, 1, 4),
    _SysVolumeTotalSize_Type()
)
sysVolumeTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVolumeTotalSize.setStatus("mandatory")


class _SysVolumeFreeSize_Type(DisplayString):
    """Custom type sysVolumeFreeSize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SysVolumeFreeSize_Type.__name__ = "DisplayString"
_SysVolumeFreeSize_Object = MibTableColumn
sysVolumeFreeSize = _SysVolumeFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 17, 1, 5),
    _SysVolumeFreeSize_Type()
)
sysVolumeFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVolumeFreeSize.setStatus("mandatory")


class _SysVolumeStatus_Type(DisplayString):
    """Custom type sysVolumeStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysVolumeStatus_Type.__name__ = "DisplayString"
_SysVolumeStatus_Object = MibTableColumn
sysVolumeStatus = _SysVolumeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 2, 17, 1, 6),
    _SysVolumeStatus_Type()
)
sysVolumeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVolumeStatus.setStatus("mandatory")
_SystemTraps_ObjectIdentity = ObjectIdentity
systemTraps = _SystemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 10)
)

# Managed Objects groups


# Notification objects

eventInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 10, 0, 1)
)
eventInform.setObjects(
    ("NSS324-MIB", "eventInformMsg")
)
if mibBuilder.loadTexts:
    eventInform.setStatus(
        ""
    )

eventWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 10, 0, 2)
)
eventWarning.setObjects(
    ("NSS324-MIB", "eventWarningMsg")
)
if mibBuilder.loadTexts:
    eventWarning.setStatus(
        ""
    )

eventError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 103, 41, 324, 114, 1, 10, 0, 4)
)
eventError.setObjects(
    ("NSS324-MIB", "eventErrorMsg")
)
if mibBuilder.loadTexts:
    eventError.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSS324-MIB",
    **{"DisplayString": DisplayString,
       "cisco": cisco,
       "otherEnterprises": otherEnterprises,
       "ciscoSB": ciscoSB,
       "nas004": nas004,
       "nss": nss,
       "nss324": nss324,
       "nssAthens": nssAthens,
       "storageSystem": storageSystem,
       "systemEventMsg": systemEventMsg,
       "eventInformMsg": eventInformMsg,
       "eventWarningMsg": eventWarningMsg,
       "eventErrorMsg": eventErrorMsg,
       "systemInfo": systemInfo,
       "systemCPU-Usage": systemCPU_Usage,
       "systemTotalMem": systemTotalMem,
       "systemFreeMem": systemFreeMem,
       "systemUptime": systemUptime,
       "cpu-Temperature": cpu_Temperature,
       "systemTemperature": systemTemperature,
       "ifNumber": ifNumber,
       "systemIfTable": systemIfTable,
       "ifEntry": ifEntry,
       "ifIndex": ifIndex,
       "ifDescr": ifDescr,
       "ifPacketsReceived": ifPacketsReceived,
       "ifPacketsSent": ifPacketsSent,
       "ifErrorPackets": ifErrorPackets,
       "hdNumber": hdNumber,
       "systemHdTable": systemHdTable,
       "hdEntry": hdEntry,
       "hdIndex": hdIndex,
       "hdDescr": hdDescr,
       "hdTemperature": hdTemperature,
       "hdStatus": hdStatus,
       "hdModel": hdModel,
       "hdCapacity": hdCapacity,
       "hdSmartInfo": hdSmartInfo,
       "modelName": modelName,
       "hostName": hostName,
       "sysFanNumber": sysFanNumber,
       "systemFanTable": systemFanTable,
       "sysFanEntry": sysFanEntry,
       "sysFanIndex": sysFanIndex,
       "sysFanDescr": sysFanDescr,
       "sysFanSpeed": sysFanSpeed,
       "sysVolumeNumber": sysVolumeNumber,
       "systemVolumeTable": systemVolumeTable,
       "sysVolumeEntry": sysVolumeEntry,
       "sysVolumeIndex": sysVolumeIndex,
       "sysVolumeDescr": sysVolumeDescr,
       "sysVolumeFS": sysVolumeFS,
       "sysVolumeTotalSize": sysVolumeTotalSize,
       "sysVolumeFreeSize": sysVolumeFreeSize,
       "sysVolumeStatus": sysVolumeStatus,
       "systemTraps": systemTraps,
       "eventInform": eventInform,
       "eventWarning": eventWarning,
       "eventError": eventError}
)
