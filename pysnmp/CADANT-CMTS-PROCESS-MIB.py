# SNMP MIB module (CADANT-CMTS-PROCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-CMTS-PROCESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:42 2024
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

(cardNumber,
 trapCounter,
 trapSeverity) = mibBuilder.importSymbols(
    "CADANT-CMTS-EQUIPMENT-MIB",
    "cardNumber",
    "trapCounter",
    "trapSeverity")

(cadSystem,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadSystem")

(CardId,
 OverloadStatus) = mibBuilder.importSymbols(
    "CADANT-TC",
    "CardId",
    "OverloadStatus")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TimeTicks,
 Unsigned32,
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
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

cadProcessMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3)
)
cadProcessMib.setRevisions(
        ("2013-07-02 00:00",
         "2011-05-22 00:00",
         "2010-12-20 00:00",
         "2005-10-20 00:00",
         "2003-03-29 00:00",
         "2003-03-20 00:00",
         "2002-04-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CadProcessTraps_ObjectIdentity = ObjectIdentity
cadProcessTraps = _CadProcessTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 0)
)
_CadProcessGroup_ObjectIdentity = ObjectIdentity
cadProcessGroup = _CadProcessGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 1)
)
_CadCpu_Object = MibTable
cadCpu = _CadCpu_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cadCpu.setStatus("current")
_CadCpuEntry_Object = MibTableRow
cadCpuEntry = _CadCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 1, 1, 1)
)
cadCpuEntry.setIndexNames(
    (0, "CADANT-CMTS-PROCESS-MIB", "cadCpuCardId"),
)
if mibBuilder.loadTexts:
    cadCpuEntry.setStatus("current")
_CadCpuCardId_Type = CardId
_CadCpuCardId_Object = MibTableColumn
cadCpuCardId = _CadCpuCardId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 1, 1, 1, 1),
    _CadCpuCardId_Type()
)
cadCpuCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadCpuCardId.setStatus("current")
_CadCpuRecentTime_Type = Counter64
_CadCpuRecentTime_Object = MibTableColumn
cadCpuRecentTime = _CadCpuRecentTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 1, 1, 1, 2),
    _CadCpuRecentTime_Type()
)
cadCpuRecentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCpuRecentTime.setStatus("current")
if mibBuilder.loadTexts:
    cadCpuRecentTime.setUnits("nanoseconds")
_CadCpuTotalTime_Type = Counter64
_CadCpuTotalTime_Object = MibTableColumn
cadCpuTotalTime = _CadCpuTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 1, 1, 1, 3),
    _CadCpuTotalTime_Type()
)
cadCpuTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCpuTotalTime.setStatus("current")
if mibBuilder.loadTexts:
    cadCpuTotalTime.setUnits("nanoseconds")
_CadIdleCpuRecentTime_Type = Counter64
_CadIdleCpuRecentTime_Object = MibTableColumn
cadIdleCpuRecentTime = _CadIdleCpuRecentTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 1, 1, 1, 4),
    _CadIdleCpuRecentTime_Type()
)
cadIdleCpuRecentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIdleCpuRecentTime.setStatus("current")
if mibBuilder.loadTexts:
    cadIdleCpuRecentTime.setUnits("nanoseconds")
_CadIdleCpuTotalTime_Type = Counter64
_CadIdleCpuTotalTime_Object = MibTableColumn
cadIdleCpuTotalTime = _CadIdleCpuTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 1, 1, 1, 5),
    _CadIdleCpuTotalTime_Type()
)
cadIdleCpuTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIdleCpuTotalTime.setStatus("current")
if mibBuilder.loadTexts:
    cadIdleCpuTotalTime.setUnits("nanoseconds")
_CadSwitchRecentCount_Type = Counter64
_CadSwitchRecentCount_Object = MibTableColumn
cadSwitchRecentCount = _CadSwitchRecentCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 1, 1, 1, 6),
    _CadSwitchRecentCount_Type()
)
cadSwitchRecentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSwitchRecentCount.setStatus("current")
_CadSwitchTotalCount_Type = Counter64
_CadSwitchTotalCount_Object = MibTableColumn
cadSwitchTotalCount = _CadSwitchTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 1, 1, 1, 7),
    _CadSwitchTotalCount_Type()
)
cadSwitchTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSwitchTotalCount.setStatus("current")


class _CadIdleCpuRecentPercent_Type(Integer32):
    """Custom type cadIdleCpuRecentPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadIdleCpuRecentPercent_Type.__name__ = "Integer32"
_CadIdleCpuRecentPercent_Object = MibTableColumn
cadIdleCpuRecentPercent = _CadIdleCpuRecentPercent_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 1, 1, 1, 8),
    _CadIdleCpuRecentPercent_Type()
)
cadIdleCpuRecentPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIdleCpuRecentPercent.setStatus("current")
if mibBuilder.loadTexts:
    cadIdleCpuRecentPercent.setUnits("percent")
_CadMemoryGroup_ObjectIdentity = ObjectIdentity
cadMemoryGroup = _CadMemoryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 2)
)
_CadMemory_Object = MibTable
cadMemory = _CadMemory_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cadMemory.setStatus("current")
_CadMemoryEntry_Object = MibTableRow
cadMemoryEntry = _CadMemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 2, 1, 1)
)
cadMemoryEntry.setIndexNames(
    (0, "CADANT-CMTS-PROCESS-MIB", "cadMeCardId"),
)
if mibBuilder.loadTexts:
    cadMemoryEntry.setStatus("current")
_CadMeCardId_Type = CardId
_CadMeCardId_Object = MibTableColumn
cadMeCardId = _CadMeCardId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 2, 1, 1, 1),
    _CadMeCardId_Type()
)
cadMeCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadMeCardId.setStatus("current")
_CadMeHeapSize_Type = Unsigned32
_CadMeHeapSize_Object = MibTableColumn
cadMeHeapSize = _CadMeHeapSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 2, 1, 1, 2),
    _CadMeHeapSize_Type()
)
cadMeHeapSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMeHeapSize.setStatus("current")
if mibBuilder.loadTexts:
    cadMeHeapSize.setUnits("bytes")
_CadMeHeapRemaining_Type = Unsigned32
_CadMeHeapRemaining_Object = MibTableColumn
cadMeHeapRemaining = _CadMeHeapRemaining_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 2, 1, 1, 3),
    _CadMeHeapRemaining_Type()
)
cadMeHeapRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMeHeapRemaining.setStatus("current")
if mibBuilder.loadTexts:
    cadMeHeapRemaining.setUnits("bytes")
_CadOverloadGroup_ObjectIdentity = ObjectIdentity
cadOverloadGroup = _CadOverloadGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 3)
)
_CadOverload_Object = MibTable
cadOverload = _CadOverload_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cadOverload.setStatus("current")
_CadOverloadEntry_Object = MibTableRow
cadOverloadEntry = _CadOverloadEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 3, 1, 1)
)
cadOverloadEntry.setIndexNames(
    (0, "CADANT-CMTS-PROCESS-MIB", "cadOvCardId"),
)
if mibBuilder.loadTexts:
    cadOverloadEntry.setStatus("current")
_CadOvCardId_Type = CardId
_CadOvCardId_Object = MibTableColumn
cadOvCardId = _CadOvCardId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 3, 1, 1, 1),
    _CadOvCardId_Type()
)
cadOvCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadOvCardId.setStatus("current")


class _CadOvCpuStatus_Type(OverloadStatus):
    """Custom type cadOvCpuStatus based on OverloadStatus"""


_CadOvCpuStatus_Object = MibTableColumn
cadOvCpuStatus = _CadOvCpuStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 3, 1, 1, 2),
    _CadOvCpuStatus_Type()
)
cadOvCpuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadOvCpuStatus.setStatus("current")


class _CadOvMemStatus_Type(OverloadStatus):
    """Custom type cadOvMemStatus based on OverloadStatus"""


_CadOvMemStatus_Object = MibTableColumn
cadOvMemStatus = _CadOvMemStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 3, 1, 1, 3),
    _CadOvMemStatus_Type()
)
cadOvMemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadOvMemStatus.setStatus("deprecated")


class _CadOvSysCpuStatus_Type(OverloadStatus):
    """Custom type cadOvSysCpuStatus based on OverloadStatus"""


_CadOvSysCpuStatus_Object = MibScalar
cadOvSysCpuStatus = _CadOvSysCpuStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 3, 2),
    _CadOvSysCpuStatus_Type()
)
cadOvSysCpuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadOvSysCpuStatus.setStatus("current")


class _CadOvSysMemStatus_Type(OverloadStatus):
    """Custom type cadOvSysMemStatus based on OverloadStatus"""


_CadOvSysMemStatus_Object = MibScalar
cadOvSysMemStatus = _CadOvSysMemStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 3, 3),
    _CadOvSysMemStatus_Type()
)
cadOvSysMemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadOvSysMemStatus.setStatus("current")
_CadProcessTrapInfo_ObjectIdentity = ObjectIdentity
cadProcessTrapInfo = _CadProcessTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 4)
)


class _CadProcessOverloadStatus_Type(OverloadStatus):
    """Custom type cadProcessOverloadStatus based on OverloadStatus"""


_CadProcessOverloadStatus_Object = MibScalar
cadProcessOverloadStatus = _CadProcessOverloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 4, 1),
    _CadProcessOverloadStatus_Type()
)
cadProcessOverloadStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cadProcessOverloadStatus.setStatus("current")
_CadProcessMibConformance_ObjectIdentity = ObjectIdentity
cadProcessMibConformance = _CadProcessMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 5)
)
_CadProcessCompliances_ObjectIdentity = ObjectIdentity
cadProcessCompliances = _CadProcessCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 5, 1)
)
_CadProcessGroups_ObjectIdentity = ObjectIdentity
cadProcessGroups = _CadProcessGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 5, 2)
)

# Managed Objects groups


# Notification objects

cardOverloadNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 0, 1)
)
cardOverloadNotification.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber"),
        ("CADANT-CMTS-PROCESS-MIB", "cadProcessOverloadStatus"))
)
if mibBuilder.loadTexts:
    cardOverloadNotification.setStatus(
        "current"
    )

sysOverloadNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 0, 2)
)
sysOverloadNotification.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-PROCESS-MIB", "cadProcessOverloadStatus"))
)
if mibBuilder.loadTexts:
    sysOverloadNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

cadProcessCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 5, 1, 1)
)
if mibBuilder.loadTexts:
    cadProcessCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-CMTS-PROCESS-MIB",
    **{"cadProcessMib": cadProcessMib,
       "cadProcessTraps": cadProcessTraps,
       "cardOverloadNotification": cardOverloadNotification,
       "sysOverloadNotification": sysOverloadNotification,
       "cadProcessGroup": cadProcessGroup,
       "cadCpu": cadCpu,
       "cadCpuEntry": cadCpuEntry,
       "cadCpuCardId": cadCpuCardId,
       "cadCpuRecentTime": cadCpuRecentTime,
       "cadCpuTotalTime": cadCpuTotalTime,
       "cadIdleCpuRecentTime": cadIdleCpuRecentTime,
       "cadIdleCpuTotalTime": cadIdleCpuTotalTime,
       "cadSwitchRecentCount": cadSwitchRecentCount,
       "cadSwitchTotalCount": cadSwitchTotalCount,
       "cadIdleCpuRecentPercent": cadIdleCpuRecentPercent,
       "cadMemoryGroup": cadMemoryGroup,
       "cadMemory": cadMemory,
       "cadMemoryEntry": cadMemoryEntry,
       "cadMeCardId": cadMeCardId,
       "cadMeHeapSize": cadMeHeapSize,
       "cadMeHeapRemaining": cadMeHeapRemaining,
       "cadOverloadGroup": cadOverloadGroup,
       "cadOverload": cadOverload,
       "cadOverloadEntry": cadOverloadEntry,
       "cadOvCardId": cadOvCardId,
       "cadOvCpuStatus": cadOvCpuStatus,
       "cadOvMemStatus": cadOvMemStatus,
       "cadOvSysCpuStatus": cadOvSysCpuStatus,
       "cadOvSysMemStatus": cadOvSysMemStatus,
       "cadProcessTrapInfo": cadProcessTrapInfo,
       "cadProcessOverloadStatus": cadProcessOverloadStatus,
       "cadProcessMibConformance": cadProcessMibConformance,
       "cadProcessCompliances": cadProcessCompliances,
       "cadProcessCompliance": cadProcessCompliance,
       "cadProcessGroups": cadProcessGroups}
)
