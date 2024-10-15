# SNMP MIB module (WBSN-APPLIANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WBSN-APPLIANCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:40 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")

(dskErrorMsg,
 dskPath,
 fileErrorMsg,
 fileName,
 memAvailReal,
 memAvailSwap,
 memBuffer,
 memCached,
 memErrorName,
 memShared,
 memSwapErrorMsg,
 memTotalFree,
 memTotalReal,
 memTotalSwap,
 ssCpuIdle,
 ssCpuSystem,
 ssCpuUser,
 ssErrorName) = mibBuilder.importSymbols(
    "UCD-SNMP-MIB",
    "dskErrorMsg",
    "dskPath",
    "fileErrorMsg",
    "fileName",
    "memAvailReal",
    "memAvailSwap",
    "memBuffer",
    "memCached",
    "memErrorName",
    "memShared",
    "memSwapErrorMsg",
    "memTotalFree",
    "memTotalReal",
    "memTotalSwap",
    "ssCpuIdle",
    "ssCpuSystem",
    "ssCpuUser",
    "ssErrorName")


# MODULE-IDENTITY

websense = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 23365)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Appliance_ObjectIdentity = ObjectIdentity
appliance = _Appliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23365, 10000)
)
_ModuleName_Type = DisplayString
_ModuleName_Object = MibScalar
moduleName = _ModuleName_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 1),
    _ModuleName_Type()
)
moduleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleName.setStatus("current")
_MemUsageFlag_Type = Integer32
_MemUsageFlag_Object = MibScalar
memUsageFlag = _MemUsageFlag_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 2),
    _MemUsageFlag_Type()
)
memUsageFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memUsageFlag.setStatus("current")
_VmTable_Object = MibTable
vmTable = _VmTable_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 3)
)
if mibBuilder.loadTexts:
    vmTable.setStatus("current")
_VmEntry_Object = MibTableRow
vmEntry = _VmEntry_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 3, 1)
)
vmEntry.setIndexNames(
    (0, "WBSN-APPLIANCE-MIB", "vmName"),
)
if mibBuilder.loadTexts:
    vmEntry.setStatus("current")


class _VmStatus_Type(Integer32):
    """Custom type vmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("offline", 1),
          ("online", 0))
    )


_VmStatus_Type.__name__ = "Integer32"
_VmStatus_Object = MibTableColumn
vmStatus = _VmStatus_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 3, 1, 1),
    _VmStatus_Type()
)
vmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStatus.setStatus("current")
_VmName_Type = DisplayString
_VmName_Object = MibTableColumn
vmName = _VmName_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 3, 1, 2),
    _VmName_Type()
)
vmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmName.setStatus("current")
_Hostname_ObjectIdentity = ObjectIdentity
hostname = _Hostname_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 4)
)
_HostnameChangeFlag_Type = Integer32
_HostnameChangeFlag_Object = MibScalar
hostnameChangeFlag = _HostnameChangeFlag_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 4, 1),
    _HostnameChangeFlag_Type()
)
hostnameChangeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostnameChangeFlag.setStatus("current")
_PrevHostname_Type = DisplayString
_PrevHostname_Object = MibScalar
prevHostname = _PrevHostname_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 4, 2),
    _PrevHostname_Type()
)
prevHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prevHostname.setStatus("current")
_CurrHostname_Type = DisplayString
_CurrHostname_Object = MibScalar
currHostname = _CurrHostname_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 4, 3),
    _CurrHostname_Type()
)
currHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currHostname.setStatus("current")
_IfaTable_Object = MibTable
ifaTable = _IfaTable_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 5)
)
if mibBuilder.loadTexts:
    ifaTable.setStatus("current")
_IfaEntry_Object = MibTableRow
ifaEntry = _IfaEntry_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1)
)
ifaEntry.setIndexNames(
    (0, "WBSN-APPLIANCE-MIB", "ifaName"),
)
if mibBuilder.loadTexts:
    ifaEntry.setStatus("current")
_IfaChangeFlag_Type = Integer32
_IfaChangeFlag_Object = MibTableColumn
ifaChangeFlag = _IfaChangeFlag_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 1),
    _IfaChangeFlag_Type()
)
ifaChangeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaChangeFlag.setStatus("current")
_IfaName_Type = DisplayString
_IfaName_Object = MibTableColumn
ifaName = _IfaName_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 2),
    _IfaName_Type()
)
ifaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaName.setStatus("current")
_IfaPrevAddress_Type = DisplayString
_IfaPrevAddress_Object = MibTableColumn
ifaPrevAddress = _IfaPrevAddress_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 3),
    _IfaPrevAddress_Type()
)
ifaPrevAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaPrevAddress.setStatus("current")
_IfaCurrAddress_Type = DisplayString
_IfaCurrAddress_Object = MibTableColumn
ifaCurrAddress = _IfaCurrAddress_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 4),
    _IfaCurrAddress_Type()
)
ifaCurrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaCurrAddress.setStatus("current")
_IfaSpeed_Type = Integer32
_IfaSpeed_Object = MibTableColumn
ifaSpeed = _IfaSpeed_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 5),
    _IfaSpeed_Type()
)
ifaSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaSpeed.setStatus("current")
_IfaInboundExceedFlag_Type = Integer32
_IfaInboundExceedFlag_Object = MibTableColumn
ifaInboundExceedFlag = _IfaInboundExceedFlag_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 6),
    _IfaInboundExceedFlag_Type()
)
ifaInboundExceedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaInboundExceedFlag.setStatus("current")
_IfaOutboundExceedFlag_Type = Integer32
_IfaOutboundExceedFlag_Object = MibTableColumn
ifaOutboundExceedFlag = _IfaOutboundExceedFlag_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 7),
    _IfaOutboundExceedFlag_Type()
)
ifaOutboundExceedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaOutboundExceedFlag.setStatus("current")
_IfaPhysAddress_Type = DisplayString
_IfaPhysAddress_Object = MibTableColumn
ifaPhysAddress = _IfaPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 8),
    _IfaPhysAddress_Type()
)
ifaPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaPhysAddress.setStatus("current")
_IfaChangeFlagv6_Type = Integer32
_IfaChangeFlagv6_Object = MibTableColumn
ifaChangeFlagv6 = _IfaChangeFlagv6_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 9),
    _IfaChangeFlagv6_Type()
)
ifaChangeFlagv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaChangeFlagv6.setStatus("current")
_IfaPrevAddressv6_Type = DisplayString
_IfaPrevAddressv6_Object = MibTableColumn
ifaPrevAddressv6 = _IfaPrevAddressv6_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 10),
    _IfaPrevAddressv6_Type()
)
ifaPrevAddressv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaPrevAddressv6.setStatus("current")
_IfaCurrAddressv6_Type = DisplayString
_IfaCurrAddressv6_Object = MibTableColumn
ifaCurrAddressv6 = _IfaCurrAddressv6_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 11),
    _IfaCurrAddressv6_Type()
)
ifaCurrAddressv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaCurrAddressv6.setStatus("current")
_RaidStatus_ObjectIdentity = ObjectIdentity
raidStatus = _RaidStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 6)
)
_RaidErrorFlag_Type = Integer32
_RaidErrorFlag_Object = MibScalar
raidErrorFlag = _RaidErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 6, 1),
    _RaidErrorFlag_Type()
)
raidErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidErrorFlag.setStatus("current")
_DskPhysicalNr_Type = DisplayString
_DskPhysicalNr_Object = MibScalar
dskPhysicalNr = _DskPhysicalNr_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 6, 2),
    _DskPhysicalNr_Type()
)
dskPhysicalNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskPhysicalNr.setStatus("current")
_DskCriticalNr_Type = DisplayString
_DskCriticalNr_Object = MibScalar
dskCriticalNr = _DskCriticalNr_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 6, 3),
    _DskCriticalNr_Type()
)
dskCriticalNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskCriticalNr.setStatus("current")
_DskFailedNr_Type = DisplayString
_DskFailedNr_Object = MibScalar
dskFailedNr = _DskFailedNr_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 6, 4),
    _DskFailedNr_Type()
)
dskFailedNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskFailedNr.setStatus("current")
_DskPhysErrMsg_Type = DisplayString
_DskPhysErrMsg_Object = MibScalar
dskPhysErrMsg = _DskPhysErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 6, 5),
    _DskPhysErrMsg_Type()
)
dskPhysErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskPhysErrMsg.setStatus("current")
_DskVirtualNr_Type = DisplayString
_DskVirtualNr_Object = MibScalar
dskVirtualNr = _DskVirtualNr_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 6, 6),
    _DskVirtualNr_Type()
)
dskVirtualNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskVirtualNr.setStatus("current")
_DskDegradedNr_Type = DisplayString
_DskDegradedNr_Object = MibScalar
dskDegradedNr = _DskDegradedNr_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 6, 7),
    _DskDegradedNr_Type()
)
dskDegradedNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskDegradedNr.setStatus("current")
_DskOfflineNr_Type = DisplayString
_DskOfflineNr_Object = MibScalar
dskOfflineNr = _DskOfflineNr_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 6, 8),
    _DskOfflineNr_Type()
)
dskOfflineNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskOfflineNr.setStatus("current")
_SvcTable_Object = MibTable
svcTable = _SvcTable_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 7)
)
if mibBuilder.loadTexts:
    svcTable.setStatus("current")
_SvcEntry_Object = MibTableRow
svcEntry = _SvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 7, 1)
)
svcEntry.setIndexNames(
    (0, "WBSN-APPLIANCE-MIB", "svcName"),
)
if mibBuilder.loadTexts:
    svcEntry.setStatus("current")


class _SvcStatus_Type(Integer32):
    """Custom type svcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("down", 1),
          ("resetting", 3),
          ("up", 0),
          ("yellow", 2))
    )


_SvcStatus_Type.__name__ = "Integer32"
_SvcStatus_Object = MibTableColumn
svcStatus = _SvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 7, 1, 1),
    _SvcStatus_Type()
)
svcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcStatus.setStatus("current")
_SvcName_Type = DisplayString
_SvcName_Object = MibTableColumn
svcName = _SvcName_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 7, 1, 2),
    _SvcName_Type()
)
svcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcName.setStatus("current")
_LoadAvg_ObjectIdentity = ObjectIdentity
loadAvg = _LoadAvg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 8)
)
_LoadErrorFlag_Type = Integer32
_LoadErrorFlag_Object = MibScalar
loadErrorFlag = _LoadErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 8, 1),
    _LoadErrorFlag_Type()
)
loadErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadErrorFlag.setStatus("current")
_LoadName_Type = DisplayString
_LoadName_Object = MibScalar
loadName = _LoadName_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 8, 2),
    _LoadName_Type()
)
loadName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadName.setStatus("current")
_LoadErrorMessage_Type = DisplayString
_LoadErrorMessage_Object = MibScalar
loadErrorMessage = _LoadErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 8, 3),
    _LoadErrorMessage_Type()
)
loadErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadErrorMessage.setStatus("current")
_WsAlert_ObjectIdentity = ObjectIdentity
wsAlert = _WsAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 9)
)
_WsAlertMessage_Type = DisplayString
_WsAlertMessage_Object = MibScalar
wsAlertMessage = _WsAlertMessage_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 9, 1),
    _WsAlertMessage_Type()
)
wsAlertMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAlertMessage.setStatus("current")
_EvtInfo_ObjectIdentity = ObjectIdentity
evtInfo = _EvtInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10)
)
_EvtTimestamp_Type = DisplayString
_EvtTimestamp_Object = MibScalar
evtTimestamp = _EvtTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10, 1),
    _EvtTimestamp_Type()
)
evtTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtTimestamp.setStatus("current")


class _EvtDir_Type(Integer32):
    """Custom type evtDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("assertion", 0),
          ("deassertion", 1))
    )


_EvtDir_Type.__name__ = "Integer32"
_EvtDir_Object = MibScalar
evtDir = _EvtDir_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10, 2),
    _EvtDir_Type()
)
evtDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtDir.setStatus("current")
_EvtSensor_Type = DisplayString
_EvtSensor_Object = MibScalar
evtSensor = _EvtSensor_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10, 3),
    _EvtSensor_Type()
)
evtSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtSensor.setStatus("current")
_EvtDesc_Type = DisplayString
_EvtDesc_Object = MibScalar
evtDesc = _EvtDesc_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10, 4),
    _EvtDesc_Type()
)
evtDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtDesc.setStatus("current")
_TriggerReading_Type = DisplayString
_TriggerReading_Object = MibScalar
triggerReading = _TriggerReading_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10, 5),
    _TriggerReading_Type()
)
triggerReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerReading.setStatus("current")
_TriggerThreshold_Type = DisplayString
_TriggerThreshold_Object = MibScalar
triggerThreshold = _TriggerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10, 6),
    _TriggerThreshold_Type()
)
triggerThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerThreshold.setStatus("current")
_ErrorClear_ObjectIdentity = ObjectIdentity
errorClear = _ErrorClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10000)
)

# Managed Objects groups


# Notification objects

testEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 10)
)
if mibBuilder.loadTexts:
    testEvent.setStatus(
        ""
    )

cpuMaxUsageExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 1000)
)
cpuMaxUsageExceed.setObjects(
      *(("UCD-SNMP-MIB", "ssErrorName"),
        ("UCD-SNMP-MIB", "ssCpuUser"),
        ("UCD-SNMP-MIB", "ssCpuSystem"),
        ("UCD-SNMP-MIB", "ssCpuIdle"))
)
if mibBuilder.loadTexts:
    cpuMaxUsageExceed.setStatus(
        ""
    )

memMaxUsageExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 1001)
)
memMaxUsageExceed.setObjects(
      *(("UCD-SNMP-MIB", "memTotalReal"),
        ("UCD-SNMP-MIB", "memAvailReal"),
        ("UCD-SNMP-MIB", "memTotalFree"),
        ("UCD-SNMP-MIB", "memShared"),
        ("UCD-SNMP-MIB", "memBuffer"),
        ("UCD-SNMP-MIB", "memCached"),
        ("UCD-SNMP-MIB", "memTotalSwap"),
        ("UCD-SNMP-MIB", "memAvailSwap"))
)
if mibBuilder.loadTexts:
    memMaxUsageExceed.setStatus(
        ""
    )

networkMaxBandwidthExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 1002)
)
networkMaxBandwidthExceed.setObjects(
      *(("WBSN-APPLIANCE-MIB", "ifaName"),
        ("WBSN-APPLIANCE-MIB", "ifaCurrAddress"),
        ("WBSN-APPLIANCE-MIB", "ifaSpeed"),
        ("WBSN-APPLIANCE-MIB", "ifaPhysAddress"))
)
if mibBuilder.loadTexts:
    networkMaxBandwidthExceed.setStatus(
        ""
    )

diskFreeMinSizeExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 1003)
)
diskFreeMinSizeExceed.setObjects(
      *(("UCD-SNMP-MIB", "dskPath"),
        ("UCD-SNMP-MIB", "dskErrorMsg"))
)
if mibBuilder.loadTexts:
    diskFreeMinSizeExceed.setStatus(
        ""
    )

swapMinFreeExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 1004)
)
swapMinFreeExceed.setObjects(
      *(("UCD-SNMP-MIB", "memErrorName"),
        ("UCD-SNMP-MIB", "memSwapErrorMsg"))
)
if mibBuilder.loadTexts:
    swapMinFreeExceed.setStatus(
        ""
    )

systemLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 1005)
)
systemLoad.setObjects(
      *(("WBSN-APPLIANCE-MIB", "loadName"),
        ("WBSN-APPLIANCE-MIB", "loadErrorMessage"))
)
if mibBuilder.loadTexts:
    systemLoad.setStatus(
        ""
    )

logFileMaxSizeExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 1006)
)
logFileMaxSizeExceed.setObjects(
      *(("UCD-SNMP-MIB", "fileName"),
        ("UCD-SNMP-MIB", "fileErrorMsg"))
)
if mibBuilder.loadTexts:
    logFileMaxSizeExceed.setStatus(
        ""
    )

logCacheMinFreeExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 1007)
)
logCacheMinFreeExceed.setObjects(
    ("WBSN-APPLIANCE-MIB", "wsAlertMessage")
)
if mibBuilder.loadTexts:
    logCacheMinFreeExceed.setStatus(
        ""
    )

moduleDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 1050)
)
moduleDown.setObjects(
    ("WBSN-APPLIANCE-MIB", "vmName")
)
if mibBuilder.loadTexts:
    moduleDown.setStatus(
        ""
    )

serviceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 1051)
)
serviceDown.setObjects(
      *(("WBSN-APPLIANCE-MIB", "svcStatus"),
        ("WBSN-APPLIANCE-MIB", "svcName"))
)
if mibBuilder.loadTexts:
    serviceDown.setStatus(
        ""
    )

backupFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 1052)
)
backupFailure.setObjects(
    ("WBSN-APPLIANCE-MIB", "wsAlertMessage")
)
if mibBuilder.loadTexts:
    backupFailure.setStatus(
        ""
    )

logServerConnectionLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 1053)
)
logServerConnectionLost.setObjects(
    ("WBSN-APPLIANCE-MIB", "wsAlertMessage")
)
if mibBuilder.loadTexts:
    logServerConnectionLost.setStatus(
        ""
    )

hostnameChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 1061)
)
hostnameChange.setObjects(
      *(("WBSN-APPLIANCE-MIB", "prevHostname"),
        ("WBSN-APPLIANCE-MIB", "currHostname"))
)
if mibBuilder.loadTexts:
    hostnameChange.setStatus(
        ""
    )

ipAddressChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 1062)
)
ipAddressChange.setObjects(
      *(("WBSN-APPLIANCE-MIB", "ifaName"),
        ("WBSN-APPLIANCE-MIB", "ifaPrevAddress"),
        ("WBSN-APPLIANCE-MIB", "ifaCurrAddress"),
        ("WBSN-APPLIANCE-MIB", "ifaPrevAddressv6"),
        ("WBSN-APPLIANCE-MIB", "ifaCurrAddressv6"))
)
if mibBuilder.loadTexts:
    ipAddressChange.setStatus(
        ""
    )

powerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 2001)
)
powerSupply.setObjects(
      *(("WBSN-APPLIANCE-MIB", "evtTimestamp"),
        ("WBSN-APPLIANCE-MIB", "evtDir"),
        ("WBSN-APPLIANCE-MIB", "evtSensor"),
        ("WBSN-APPLIANCE-MIB", "evtDesc"))
)
if mibBuilder.loadTexts:
    powerSupply.setStatus(
        ""
    )

redundancy = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 2002)
)
redundancy.setObjects(
      *(("WBSN-APPLIANCE-MIB", "evtTimestamp"),
        ("WBSN-APPLIANCE-MIB", "evtDir"),
        ("WBSN-APPLIANCE-MIB", "evtSensor"),
        ("WBSN-APPLIANCE-MIB", "evtDesc"))
)
if mibBuilder.loadTexts:
    redundancy.setStatus(
        ""
    )

temps = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 2003)
)
temps.setObjects(
      *(("WBSN-APPLIANCE-MIB", "evtTimestamp"),
        ("WBSN-APPLIANCE-MIB", "evtDir"),
        ("WBSN-APPLIANCE-MIB", "evtSensor"),
        ("WBSN-APPLIANCE-MIB", "evtDesc"),
        ("WBSN-APPLIANCE-MIB", "triggerReading"),
        ("WBSN-APPLIANCE-MIB", "triggerThreshold"))
)
if mibBuilder.loadTexts:
    temps.setStatus(
        ""
    )

fans = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 2004)
)
fans.setObjects(
      *(("WBSN-APPLIANCE-MIB", "evtTimestamp"),
        ("WBSN-APPLIANCE-MIB", "evtDir"),
        ("WBSN-APPLIANCE-MIB", "evtSensor"),
        ("WBSN-APPLIANCE-MIB", "evtDesc"),
        ("WBSN-APPLIANCE-MIB", "triggerReading"),
        ("WBSN-APPLIANCE-MIB", "triggerThreshold"))
)
if mibBuilder.loadTexts:
    fans.setStatus(
        ""
    )

volt = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 2005)
)
volt.setObjects(
      *(("WBSN-APPLIANCE-MIB", "evtTimestamp"),
        ("WBSN-APPLIANCE-MIB", "evtDir"),
        ("WBSN-APPLIANCE-MIB", "evtSensor"),
        ("WBSN-APPLIANCE-MIB", "evtDesc"),
        ("WBSN-APPLIANCE-MIB", "triggerReading"),
        ("WBSN-APPLIANCE-MIB", "triggerThreshold"))
)
if mibBuilder.loadTexts:
    volt.setStatus(
        ""
    )

logs = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 2006)
)
logs.setObjects(
      *(("WBSN-APPLIANCE-MIB", "evtTimestamp"),
        ("WBSN-APPLIANCE-MIB", "evtDir"),
        ("WBSN-APPLIANCE-MIB", "evtSensor"),
        ("WBSN-APPLIANCE-MIB", "evtDesc"))
)
if mibBuilder.loadTexts:
    logs.setStatus(
        ""
    )

mem = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 2007)
)
mem.setObjects(
      *(("WBSN-APPLIANCE-MIB", "evtTimestamp"),
        ("WBSN-APPLIANCE-MIB", "evtDir"),
        ("WBSN-APPLIANCE-MIB", "evtSensor"),
        ("WBSN-APPLIANCE-MIB", "evtDesc"))
)
if mibBuilder.loadTexts:
    mem.setStatus(
        ""
    )

intrusion = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 2008)
)
intrusion.setObjects(
      *(("WBSN-APPLIANCE-MIB", "evtTimestamp"),
        ("WBSN-APPLIANCE-MIB", "evtDir"),
        ("WBSN-APPLIANCE-MIB", "evtSensor"),
        ("WBSN-APPLIANCE-MIB", "evtDesc"))
)
if mibBuilder.loadTexts:
    intrusion.setStatus(
        ""
    )

battery = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 2009)
)
battery.setObjects(
      *(("WBSN-APPLIANCE-MIB", "evtTimestamp"),
        ("WBSN-APPLIANCE-MIB", "evtDir"),
        ("WBSN-APPLIANCE-MIB", "evtSensor"),
        ("WBSN-APPLIANCE-MIB", "evtDesc"))
)
if mibBuilder.loadTexts:
    battery.setStatus(
        ""
    )

raid = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 0, 2010)
)
raid.setObjects(
      *(("WBSN-APPLIANCE-MIB", "dskPhysicalNr"),
        ("WBSN-APPLIANCE-MIB", "dskCriticalNr"),
        ("WBSN-APPLIANCE-MIB", "dskFailedNr"),
        ("WBSN-APPLIANCE-MIB", "dskPhysErrMsg"),
        ("WBSN-APPLIANCE-MIB", "dskVirtualNr"),
        ("WBSN-APPLIANCE-MIB", "dskDegradedNr"),
        ("WBSN-APPLIANCE-MIB", "dskOfflineNr"))
)
if mibBuilder.loadTexts:
    raid.setStatus(
        ""
    )

cpuMaxUsageExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10000, 0, 1000)
)
cpuMaxUsageExceedClear.setObjects(
      *(("UCD-SNMP-MIB", "ssErrorName"),
        ("UCD-SNMP-MIB", "ssCpuUser"),
        ("UCD-SNMP-MIB", "ssCpuSystem"),
        ("UCD-SNMP-MIB", "ssCpuIdle"))
)
if mibBuilder.loadTexts:
    cpuMaxUsageExceedClear.setStatus(
        ""
    )

memMaxUsageExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10000, 0, 1001)
)
memMaxUsageExceedClear.setObjects(
      *(("UCD-SNMP-MIB", "memTotalReal"),
        ("UCD-SNMP-MIB", "memAvailReal"),
        ("UCD-SNMP-MIB", "memTotalFree"),
        ("UCD-SNMP-MIB", "memShared"),
        ("UCD-SNMP-MIB", "memBuffer"),
        ("UCD-SNMP-MIB", "memCached"),
        ("UCD-SNMP-MIB", "memTotalSwap"),
        ("UCD-SNMP-MIB", "memAvailSwap"))
)
if mibBuilder.loadTexts:
    memMaxUsageExceedClear.setStatus(
        ""
    )

networkMaxBandwidthExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10000, 0, 1002)
)
networkMaxBandwidthExceedClear.setObjects(
      *(("WBSN-APPLIANCE-MIB", "ifaName"),
        ("WBSN-APPLIANCE-MIB", "ifaCurrAddress"),
        ("WBSN-APPLIANCE-MIB", "ifaSpeed"),
        ("WBSN-APPLIANCE-MIB", "ifaPhysAddress"))
)
if mibBuilder.loadTexts:
    networkMaxBandwidthExceedClear.setStatus(
        ""
    )

diskFreeMinSizeExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10000, 0, 1003)
)
diskFreeMinSizeExceedClear.setObjects(
      *(("UCD-SNMP-MIB", "dskPath"),
        ("UCD-SNMP-MIB", "dskErrorMsg"))
)
if mibBuilder.loadTexts:
    diskFreeMinSizeExceedClear.setStatus(
        ""
    )

swapMinFreeExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10000, 0, 1004)
)
swapMinFreeExceedClear.setObjects(
      *(("UCD-SNMP-MIB", "memErrorName"),
        ("UCD-SNMP-MIB", "memSwapErrorMsg"))
)
if mibBuilder.loadTexts:
    swapMinFreeExceedClear.setStatus(
        ""
    )

systemLoadClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10000, 0, 1005)
)
systemLoadClear.setObjects(
      *(("WBSN-APPLIANCE-MIB", "loadName"),
        ("WBSN-APPLIANCE-MIB", "loadErrorMessage"))
)
if mibBuilder.loadTexts:
    systemLoadClear.setStatus(
        ""
    )

logFileMaxSizeExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10000, 0, 1006)
)
logFileMaxSizeExceedClear.setObjects(
      *(("UCD-SNMP-MIB", "fileName"),
        ("UCD-SNMP-MIB", "fileErrorMsg"))
)
if mibBuilder.loadTexts:
    logFileMaxSizeExceedClear.setStatus(
        ""
    )

logCacheMinFreeExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10000, 0, 1007)
)
logCacheMinFreeExceedClear.setObjects(
    ("WBSN-APPLIANCE-MIB", "wsAlertMessage")
)
if mibBuilder.loadTexts:
    logCacheMinFreeExceedClear.setStatus(
        ""
    )

moduleDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10000, 0, 1050)
)
moduleDownClear.setObjects(
    ("WBSN-APPLIANCE-MIB", "vmName")
)
if mibBuilder.loadTexts:
    moduleDownClear.setStatus(
        ""
    )

serviceDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10000, 0, 1051)
)
serviceDownClear.setObjects(
      *(("WBSN-APPLIANCE-MIB", "svcStatus"),
        ("WBSN-APPLIANCE-MIB", "svcName"))
)
if mibBuilder.loadTexts:
    serviceDownClear.setStatus(
        ""
    )

logServerConnectionLostClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10000, 0, 1053)
)
logServerConnectionLostClear.setObjects(
    ("WBSN-APPLIANCE-MIB", "wsAlertMessage")
)
if mibBuilder.loadTexts:
    logServerConnectionLostClear.setStatus(
        ""
    )

powerSupplyClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10000, 0, 2001)
)
powerSupplyClear.setObjects(
      *(("WBSN-APPLIANCE-MIB", "evtTimestamp"),
        ("WBSN-APPLIANCE-MIB", "evtDir"),
        ("WBSN-APPLIANCE-MIB", "evtSensor"),
        ("WBSN-APPLIANCE-MIB", "evtDesc"))
)
if mibBuilder.loadTexts:
    powerSupplyClear.setStatus(
        ""
    )

redundancyClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10000, 0, 2002)
)
redundancyClear.setObjects(
      *(("WBSN-APPLIANCE-MIB", "evtTimestamp"),
        ("WBSN-APPLIANCE-MIB", "evtDir"),
        ("WBSN-APPLIANCE-MIB", "evtSensor"),
        ("WBSN-APPLIANCE-MIB", "evtDesc"))
)
if mibBuilder.loadTexts:
    redundancyClear.setStatus(
        ""
    )

tempsClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10000, 0, 2003)
)
tempsClear.setObjects(
      *(("WBSN-APPLIANCE-MIB", "evtTimestamp"),
        ("WBSN-APPLIANCE-MIB", "evtDir"),
        ("WBSN-APPLIANCE-MIB", "evtSensor"),
        ("WBSN-APPLIANCE-MIB", "evtDesc"),
        ("WBSN-APPLIANCE-MIB", "triggerReading"),
        ("WBSN-APPLIANCE-MIB", "triggerThreshold"))
)
if mibBuilder.loadTexts:
    tempsClear.setStatus(
        ""
    )

fansClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10000, 0, 2004)
)
fansClear.setObjects(
      *(("WBSN-APPLIANCE-MIB", "evtTimestamp"),
        ("WBSN-APPLIANCE-MIB", "evtDir"),
        ("WBSN-APPLIANCE-MIB", "evtSensor"),
        ("WBSN-APPLIANCE-MIB", "evtDesc"),
        ("WBSN-APPLIANCE-MIB", "triggerReading"),
        ("WBSN-APPLIANCE-MIB", "triggerThreshold"))
)
if mibBuilder.loadTexts:
    fansClear.setStatus(
        ""
    )

voltClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10000, 0, 2005)
)
voltClear.setObjects(
      *(("WBSN-APPLIANCE-MIB", "evtTimestamp"),
        ("WBSN-APPLIANCE-MIB", "evtDir"),
        ("WBSN-APPLIANCE-MIB", "evtSensor"),
        ("WBSN-APPLIANCE-MIB", "evtDesc"),
        ("WBSN-APPLIANCE-MIB", "triggerReading"),
        ("WBSN-APPLIANCE-MIB", "triggerThreshold"))
)
if mibBuilder.loadTexts:
    voltClear.setStatus(
        ""
    )

logsClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10000, 0, 2006)
)
logsClear.setObjects(
      *(("WBSN-APPLIANCE-MIB", "evtTimestamp"),
        ("WBSN-APPLIANCE-MIB", "evtDir"),
        ("WBSN-APPLIANCE-MIB", "evtSensor"),
        ("WBSN-APPLIANCE-MIB", "evtDesc"))
)
if mibBuilder.loadTexts:
    logsClear.setStatus(
        ""
    )

memClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10000, 0, 2007)
)
memClear.setObjects(
      *(("WBSN-APPLIANCE-MIB", "evtTimestamp"),
        ("WBSN-APPLIANCE-MIB", "evtDir"),
        ("WBSN-APPLIANCE-MIB", "evtSensor"),
        ("WBSN-APPLIANCE-MIB", "evtDesc"))
)
if mibBuilder.loadTexts:
    memClear.setStatus(
        ""
    )

intrusionClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10000, 0, 2008)
)
intrusionClear.setObjects(
      *(("WBSN-APPLIANCE-MIB", "evtTimestamp"),
        ("WBSN-APPLIANCE-MIB", "evtDir"),
        ("WBSN-APPLIANCE-MIB", "evtSensor"),
        ("WBSN-APPLIANCE-MIB", "evtDesc"))
)
if mibBuilder.loadTexts:
    intrusionClear.setStatus(
        ""
    )

batteryClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10000, 0, 2009)
)
batteryClear.setObjects(
      *(("WBSN-APPLIANCE-MIB", "evtTimestamp"),
        ("WBSN-APPLIANCE-MIB", "evtDir"),
        ("WBSN-APPLIANCE-MIB", "evtSensor"),
        ("WBSN-APPLIANCE-MIB", "evtDesc"))
)
if mibBuilder.loadTexts:
    batteryClear.setStatus(
        ""
    )

raidClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 23365, 10000, 10000, 0, 2010)
)
raidClear.setObjects(
      *(("WBSN-APPLIANCE-MIB", "dskPhysicalNr"),
        ("WBSN-APPLIANCE-MIB", "dskCriticalNr"),
        ("WBSN-APPLIANCE-MIB", "dskFailedNr"),
        ("WBSN-APPLIANCE-MIB", "dskPhysErrMsg"),
        ("WBSN-APPLIANCE-MIB", "dskVirtualNr"),
        ("WBSN-APPLIANCE-MIB", "dskDegradedNr"),
        ("WBSN-APPLIANCE-MIB", "dskOfflineNr"))
)
if mibBuilder.loadTexts:
    raidClear.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WBSN-APPLIANCE-MIB",
    **{"websense": websense,
       "appliance": appliance,
       "testEvent": testEvent,
       "cpuMaxUsageExceed": cpuMaxUsageExceed,
       "memMaxUsageExceed": memMaxUsageExceed,
       "networkMaxBandwidthExceed": networkMaxBandwidthExceed,
       "diskFreeMinSizeExceed": diskFreeMinSizeExceed,
       "swapMinFreeExceed": swapMinFreeExceed,
       "systemLoad": systemLoad,
       "logFileMaxSizeExceed": logFileMaxSizeExceed,
       "logCacheMinFreeExceed": logCacheMinFreeExceed,
       "moduleDown": moduleDown,
       "serviceDown": serviceDown,
       "backupFailure": backupFailure,
       "logServerConnectionLost": logServerConnectionLost,
       "hostnameChange": hostnameChange,
       "ipAddressChange": ipAddressChange,
       "powerSupply": powerSupply,
       "redundancy": redundancy,
       "temps": temps,
       "fans": fans,
       "volt": volt,
       "logs": logs,
       "mem": mem,
       "intrusion": intrusion,
       "battery": battery,
       "raid": raid,
       "moduleName": moduleName,
       "memUsageFlag": memUsageFlag,
       "vmTable": vmTable,
       "vmEntry": vmEntry,
       "vmStatus": vmStatus,
       "vmName": vmName,
       "hostname": hostname,
       "hostnameChangeFlag": hostnameChangeFlag,
       "prevHostname": prevHostname,
       "currHostname": currHostname,
       "ifaTable": ifaTable,
       "ifaEntry": ifaEntry,
       "ifaChangeFlag": ifaChangeFlag,
       "ifaName": ifaName,
       "ifaPrevAddress": ifaPrevAddress,
       "ifaCurrAddress": ifaCurrAddress,
       "ifaSpeed": ifaSpeed,
       "ifaInboundExceedFlag": ifaInboundExceedFlag,
       "ifaOutboundExceedFlag": ifaOutboundExceedFlag,
       "ifaPhysAddress": ifaPhysAddress,
       "ifaChangeFlagv6": ifaChangeFlagv6,
       "ifaPrevAddressv6": ifaPrevAddressv6,
       "ifaCurrAddressv6": ifaCurrAddressv6,
       "raidStatus": raidStatus,
       "raidErrorFlag": raidErrorFlag,
       "dskPhysicalNr": dskPhysicalNr,
       "dskCriticalNr": dskCriticalNr,
       "dskFailedNr": dskFailedNr,
       "dskPhysErrMsg": dskPhysErrMsg,
       "dskVirtualNr": dskVirtualNr,
       "dskDegradedNr": dskDegradedNr,
       "dskOfflineNr": dskOfflineNr,
       "svcTable": svcTable,
       "svcEntry": svcEntry,
       "svcStatus": svcStatus,
       "svcName": svcName,
       "loadAvg": loadAvg,
       "loadErrorFlag": loadErrorFlag,
       "loadName": loadName,
       "loadErrorMessage": loadErrorMessage,
       "wsAlert": wsAlert,
       "wsAlertMessage": wsAlertMessage,
       "evtInfo": evtInfo,
       "evtTimestamp": evtTimestamp,
       "evtDir": evtDir,
       "evtSensor": evtSensor,
       "evtDesc": evtDesc,
       "triggerReading": triggerReading,
       "triggerThreshold": triggerThreshold,
       "errorClear": errorClear,
       "cpuMaxUsageExceedClear": cpuMaxUsageExceedClear,
       "memMaxUsageExceedClear": memMaxUsageExceedClear,
       "networkMaxBandwidthExceedClear": networkMaxBandwidthExceedClear,
       "diskFreeMinSizeExceedClear": diskFreeMinSizeExceedClear,
       "swapMinFreeExceedClear": swapMinFreeExceedClear,
       "systemLoadClear": systemLoadClear,
       "logFileMaxSizeExceedClear": logFileMaxSizeExceedClear,
       "logCacheMinFreeExceedClear": logCacheMinFreeExceedClear,
       "moduleDownClear": moduleDownClear,
       "serviceDownClear": serviceDownClear,
       "logServerConnectionLostClear": logServerConnectionLostClear,
       "powerSupplyClear": powerSupplyClear,
       "redundancyClear": redundancyClear,
       "tempsClear": tempsClear,
       "fansClear": fansClear,
       "voltClear": voltClear,
       "logsClear": logsClear,
       "memClear": memClear,
       "intrusionClear": intrusionClear,
       "batteryClear": batteryClear,
       "raidClear": raidClear}
)
