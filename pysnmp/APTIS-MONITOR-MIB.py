# SNMP MIB module (APTIS-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APTIS-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:07 2024
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

(Boolean,
 aptis_monitoring) = mibBuilder.importSymbols(
    "APTIS-MIB",
    "Boolean",
    "aptis-monitoring")

(aptis_modules,) = mibBuilder.importSymbols(
    "APTIS-REG-MIB",
    "aptis-modules")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

aptisMonitorModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 1, 1, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SystemSummaryTable_Object = MibTable
systemSummaryTable = _SystemSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 10)
)
if mibBuilder.loadTexts:
    systemSummaryTable.setStatus("current")
_SystemSummaryEntry_Object = MibTableRow
systemSummaryEntry = _SystemSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 10, 1)
)
systemSummaryEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "systemSummaryData"),
)
if mibBuilder.loadTexts:
    systemSummaryEntry.setStatus("current")


class _SystemSummaryData_Type(OctetString):
    """Custom type systemSummaryData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SystemSummaryData_Type.__name__ = "OctetString"
_SystemSummaryData_Object = MibTableColumn
systemSummaryData = _SystemSummaryData_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 10, 1, 1),
    _SystemSummaryData_Type()
)
systemSummaryData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSummaryData.setStatus("current")
_PowerStatusTable_Object = MibTable
powerStatusTable = _PowerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 11)
)
if mibBuilder.loadTexts:
    powerStatusTable.setStatus("current")
_PowerStatusEntry_Object = MibTableRow
powerStatusEntry = _PowerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 11, 1)
)
powerStatusEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "powerStatusShelf"),
)
if mibBuilder.loadTexts:
    powerStatusEntry.setStatus("current")
_PowerStatusShelf_Type = Integer32
_PowerStatusShelf_Object = MibTableColumn
powerStatusShelf = _PowerStatusShelf_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 11, 1, 1),
    _PowerStatusShelf_Type()
)
powerStatusShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStatusShelf.setStatus("current")
_PowerStatusFanStatus_Type = Boolean
_PowerStatusFanStatus_Object = MibTableColumn
powerStatusFanStatus = _PowerStatusFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 11, 1, 2),
    _PowerStatusFanStatus_Type()
)
powerStatusFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStatusFanStatus.setStatus("current")
_PowerStatusExternalDC1_Type = Boolean
_PowerStatusExternalDC1_Object = MibTableColumn
powerStatusExternalDC1 = _PowerStatusExternalDC1_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 11, 1, 3),
    _PowerStatusExternalDC1_Type()
)
powerStatusExternalDC1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStatusExternalDC1.setStatus("current")
_PowerStatusExternalDC2_Type = Boolean
_PowerStatusExternalDC2_Object = MibTableColumn
powerStatusExternalDC2 = _PowerStatusExternalDC2_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 11, 1, 4),
    _PowerStatusExternalDC2_Type()
)
powerStatusExternalDC2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStatusExternalDC2.setStatus("current")
_PowerStatusInternalAC1_Type = Boolean
_PowerStatusInternalAC1_Object = MibTableColumn
powerStatusInternalAC1 = _PowerStatusInternalAC1_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 11, 1, 5),
    _PowerStatusInternalAC1_Type()
)
powerStatusInternalAC1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStatusInternalAC1.setStatus("current")
_PowerStatusInternalAC2_Type = Boolean
_PowerStatusInternalAC2_Object = MibTableColumn
powerStatusInternalAC2 = _PowerStatusInternalAC2_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 11, 1, 6),
    _PowerStatusInternalAC2_Type()
)
powerStatusInternalAC2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStatusInternalAC2.setStatus("current")
_PowerStatusInternalACDC1_Type = Boolean
_PowerStatusInternalACDC1_Object = MibTableColumn
powerStatusInternalACDC1 = _PowerStatusInternalACDC1_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 11, 1, 7),
    _PowerStatusInternalACDC1_Type()
)
powerStatusInternalACDC1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStatusInternalACDC1.setStatus("current")
_PowerStatusInternalACDC2_Type = Boolean
_PowerStatusInternalACDC2_Object = MibTableColumn
powerStatusInternalACDC2 = _PowerStatusInternalACDC2_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 11, 1, 8),
    _PowerStatusInternalACDC2_Type()
)
powerStatusInternalACDC2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStatusInternalACDC2.setStatus("current")
_PowerStatusInternalACDC3_Type = Boolean
_PowerStatusInternalACDC3_Object = MibTableColumn
powerStatusInternalACDC3 = _PowerStatusInternalACDC3_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 11, 1, 9),
    _PowerStatusInternalACDC3_Type()
)
powerStatusInternalACDC3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStatusInternalACDC3.setStatus("current")
_PowerStatusCsr1Register_Type = Integer32
_PowerStatusCsr1Register_Object = MibTableColumn
powerStatusCsr1Register = _PowerStatusCsr1Register_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 11, 1, 10),
    _PowerStatusCsr1Register_Type()
)
powerStatusCsr1Register.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStatusCsr1Register.setStatus("current")
_SoftwareVersionTable_Object = MibTable
softwareVersionTable = _SoftwareVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 12)
)
if mibBuilder.loadTexts:
    softwareVersionTable.setStatus("current")
_SoftwareVersionEntry_Object = MibTableRow
softwareVersionEntry = _SoftwareVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 12, 1)
)
softwareVersionEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "softwareVersionMibVersion"),
)
if mibBuilder.loadTexts:
    softwareVersionEntry.setStatus("current")
_SoftwareVersionMibVersion_Type = Integer32
_SoftwareVersionMibVersion_Object = MibTableColumn
softwareVersionMibVersion = _SoftwareVersionMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 12, 1, 1),
    _SoftwareVersionMibVersion_Type()
)
softwareVersionMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersionMibVersion.setStatus("current")


class _SoftwareVersionSoftwareRevision_Type(DisplayString):
    """Custom type softwareVersionSoftwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SoftwareVersionSoftwareRevision_Type.__name__ = "DisplayString"
_SoftwareVersionSoftwareRevision_Object = MibTableColumn
softwareVersionSoftwareRevision = _SoftwareVersionSoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 12, 1, 2),
    _SoftwareVersionSoftwareRevision_Type()
)
softwareVersionSoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersionSoftwareRevision.setStatus("current")


class _SoftwareVersionProductId_Type(Integer32):
    """Custom type softwareVersionProductId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cvx1800", 1),
          ("cvx600", 2))
    )


_SoftwareVersionProductId_Type.__name__ = "Integer32"
_SoftwareVersionProductId_Object = MibTableColumn
softwareVersionProductId = _SoftwareVersionProductId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 12, 1, 3),
    _SoftwareVersionProductId_Type()
)
softwareVersionProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersionProductId.setStatus("current")
_SoftwareVersionMibRevision_Type = Integer32
_SoftwareVersionMibRevision_Object = MibTableColumn
softwareVersionMibRevision = _SoftwareVersionMibRevision_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 12, 1, 4),
    _SoftwareVersionMibRevision_Type()
)
softwareVersionMibRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersionMibRevision.setStatus("current")
_SystemTimeTable_Object = MibTable
systemTimeTable = _SystemTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 15)
)
if mibBuilder.loadTexts:
    systemTimeTable.setStatus("current")
_SystemTimeEntry_Object = MibTableRow
systemTimeEntry = _SystemTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 15, 1)
)
systemTimeEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "systemTimeFixedBootTime"),
)
if mibBuilder.loadTexts:
    systemTimeEntry.setStatus("current")
_SystemTimeFixedBootTime_Type = Integer32
_SystemTimeFixedBootTime_Object = MibTableColumn
systemTimeFixedBootTime = _SystemTimeFixedBootTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 15, 1, 1),
    _SystemTimeFixedBootTime_Type()
)
systemTimeFixedBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTimeFixedBootTime.setStatus("current")
_SystemTimeUTCOffset_Type = Integer32
_SystemTimeUTCOffset_Object = MibTableColumn
systemTimeUTCOffset = _SystemTimeUTCOffset_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 15, 1, 2),
    _SystemTimeUTCOffset_Type()
)
systemTimeUTCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTimeUTCOffset.setStatus("current")
_SystemTimeUpTime_Type = Integer32
_SystemTimeUpTime_Object = MibTableColumn
systemTimeUpTime = _SystemTimeUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 15, 1, 3),
    _SystemTimeUpTime_Type()
)
systemTimeUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTimeUpTime.setStatus("current")
_SessionCountersTable_Object = MibTable
sessionCountersTable = _SessionCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 100)
)
if mibBuilder.loadTexts:
    sessionCountersTable.setStatus("current")
_SessionCountersEntry_Object = MibTableRow
sessionCountersEntry = _SessionCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 100, 1)
)
sessionCountersEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "sessionCountersActiveLowest"),
)
if mibBuilder.loadTexts:
    sessionCountersEntry.setStatus("current")
_SessionCountersActiveLowest_Type = Integer32
_SessionCountersActiveLowest_Object = MibTableColumn
sessionCountersActiveLowest = _SessionCountersActiveLowest_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 100, 1, 1),
    _SessionCountersActiveLowest_Type()
)
sessionCountersActiveLowest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionCountersActiveLowest.setStatus("current")
_SessionCountersActiveHighest_Type = Integer32
_SessionCountersActiveHighest_Object = MibTableColumn
sessionCountersActiveHighest = _SessionCountersActiveHighest_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 100, 1, 2),
    _SessionCountersActiveHighest_Type()
)
sessionCountersActiveHighest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionCountersActiveHighest.setStatus("current")
_SessionCountersActiveCount_Type = Integer32
_SessionCountersActiveCount_Object = MibTableColumn
sessionCountersActiveCount = _SessionCountersActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 100, 1, 3),
    _SessionCountersActiveCount_Type()
)
sessionCountersActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionCountersActiveCount.setStatus("current")
_SessionCountersInactiveLowest_Type = Integer32
_SessionCountersInactiveLowest_Object = MibTableColumn
sessionCountersInactiveLowest = _SessionCountersInactiveLowest_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 100, 1, 4),
    _SessionCountersInactiveLowest_Type()
)
sessionCountersInactiveLowest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionCountersInactiveLowest.setStatus("current")
_SessionCountersInactiveHighest_Type = Integer32
_SessionCountersInactiveHighest_Object = MibTableColumn
sessionCountersInactiveHighest = _SessionCountersInactiveHighest_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 100, 1, 5),
    _SessionCountersInactiveHighest_Type()
)
sessionCountersInactiveHighest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionCountersInactiveHighest.setStatus("current")
_SessionCountersInactiveCount_Type = Integer32
_SessionCountersInactiveCount_Object = MibTableColumn
sessionCountersInactiveCount = _SessionCountersInactiveCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 100, 1, 6),
    _SessionCountersInactiveCount_Type()
)
sessionCountersInactiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionCountersInactiveCount.setStatus("current")
_SessionCountersSessionTableSize_Type = Integer32
_SessionCountersSessionTableSize_Object = MibTableColumn
sessionCountersSessionTableSize = _SessionCountersSessionTableSize_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 100, 1, 7),
    _SessionCountersSessionTableSize_Type()
)
sessionCountersSessionTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionCountersSessionTableSize.setStatus("current")
_SessionCountersHistoryLowest_Type = Integer32
_SessionCountersHistoryLowest_Object = MibTableColumn
sessionCountersHistoryLowest = _SessionCountersHistoryLowest_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 100, 1, 8),
    _SessionCountersHistoryLowest_Type()
)
sessionCountersHistoryLowest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionCountersHistoryLowest.setStatus("current")
_SessionCountersHistoryHighest_Type = Integer32
_SessionCountersHistoryHighest_Object = MibTableColumn
sessionCountersHistoryHighest = _SessionCountersHistoryHighest_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 100, 1, 9),
    _SessionCountersHistoryHighest_Type()
)
sessionCountersHistoryHighest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionCountersHistoryHighest.setStatus("current")
_SessionCountersBootEra_Type = Integer32
_SessionCountersBootEra_Object = MibTableColumn
sessionCountersBootEra = _SessionCountersBootEra_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 100, 1, 10),
    _SessionCountersBootEra_Type()
)
sessionCountersBootEra.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionCountersBootEra.setStatus("current")
_SessionCountersHistoryTableSize_Type = Integer32
_SessionCountersHistoryTableSize_Object = MibTableColumn
sessionCountersHistoryTableSize = _SessionCountersHistoryTableSize_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 100, 1, 11),
    _SessionCountersHistoryTableSize_Type()
)
sessionCountersHistoryTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionCountersHistoryTableSize.setStatus("current")
_SessionStatusTable_Object = MibTable
sessionStatusTable = _SessionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101)
)
if mibBuilder.loadTexts:
    sessionStatusTable.setStatus("current")
_SessionStatusEntry_Object = MibTableRow
sessionStatusEntry = _SessionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1)
)
sessionStatusEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "sessionStatusSessionID"),
)
if mibBuilder.loadTexts:
    sessionStatusEntry.setStatus("current")
_SessionStatusSessionID_Type = Integer32
_SessionStatusSessionID_Object = MibTableColumn
sessionStatusSessionID = _SessionStatusSessionID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 2),
    _SessionStatusSessionID_Type()
)
sessionStatusSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusSessionID.setStatus("current")


class _SessionStatusState_Type(Integer32):
    """Custom type sessionStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_SessionStatusState_Type.__name__ = "Integer32"
_SessionStatusState_Object = MibTableColumn
sessionStatusState = _SessionStatusState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 3),
    _SessionStatusState_Type()
)
sessionStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusState.setStatus("current")


class _SessionStatusPermanentFlag_Type(Integer32):
    """Custom type sessionStatusPermanentFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permanent", 2),
          ("switched", 1),
          ("unknown", 0))
    )


_SessionStatusPermanentFlag_Type.__name__ = "Integer32"
_SessionStatusPermanentFlag_Object = MibTableColumn
sessionStatusPermanentFlag = _SessionStatusPermanentFlag_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 10),
    _SessionStatusPermanentFlag_Type()
)
sessionStatusPermanentFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusPermanentFlag.setStatus("current")
_SessionStatusVpopId_Type = Integer32
_SessionStatusVpopId_Object = MibTableColumn
sessionStatusVpopId = _SessionStatusVpopId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 11),
    _SessionStatusVpopId_Type()
)
sessionStatusVpopId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusVpopId.setStatus("current")


class _SessionStatusName_Type(DisplayString):
    """Custom type sessionStatusName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 68),
    )


_SessionStatusName_Type.__name__ = "DisplayString"
_SessionStatusName_Object = MibTableColumn
sessionStatusName = _SessionStatusName_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 12),
    _SessionStatusName_Type()
)
sessionStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusName.setStatus("current")
_SessionStatusRemoteIP_Type = IpAddress
_SessionStatusRemoteIP_Object = MibTableColumn
sessionStatusRemoteIP = _SessionStatusRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 13),
    _SessionStatusRemoteIP_Type()
)
sessionStatusRemoteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusRemoteIP.setStatus("current")
_SessionStatusRemoteIPMask_Type = IpAddress
_SessionStatusRemoteIPMask_Object = MibTableColumn
sessionStatusRemoteIPMask = _SessionStatusRemoteIPMask_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 14),
    _SessionStatusRemoteIPMask_Type()
)
sessionStatusRemoteIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusRemoteIPMask.setStatus("current")
_SessionStatusLocalIP_Type = IpAddress
_SessionStatusLocalIP_Object = MibTableColumn
sessionStatusLocalIP = _SessionStatusLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 15),
    _SessionStatusLocalIP_Type()
)
sessionStatusLocalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusLocalIP.setStatus("current")
_SessionStatusLocalIPMask_Type = IpAddress
_SessionStatusLocalIPMask_Object = MibTableColumn
sessionStatusLocalIPMask = _SessionStatusLocalIPMask_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 16),
    _SessionStatusLocalIPMask_Type()
)
sessionStatusLocalIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusLocalIPMask.setStatus("current")


class _SessionStatusLinkService_Type(Integer32):
    """Custom type sessionStatusLinkService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 11),
          ("hssi", 14),
          ("hub", 15),
          ("isdn56K", 3),
          ("isdn64K", 4),
          ("isdnV110", 6),
          ("isdnV120", 5),
          ("loopback", 13),
          ("modemK56", 9),
          ("modemV32", 7),
          ("modemV34", 8),
          ("modemV90", 10),
          ("none", 1),
          ("other", 2),
          ("t1Trunk", 12),
          ("unknown", 0),
          ("voice", 16))
    )


_SessionStatusLinkService_Type.__name__ = "Integer32"
_SessionStatusLinkService_Object = MibTableColumn
sessionStatusLinkService = _SessionStatusLinkService_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 17),
    _SessionStatusLinkService_Type()
)
sessionStatusLinkService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusLinkService.setStatus("current")


class _SessionStatusServiceMode_Type(Integer32):
    """Custom type sessionStatusServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("atmp", 20),
          ("ciscoHDLC", 6),
          ("dvs", 18),
          ("fax", 19),
          ("frameRelay", 5),
          ("ftp", 17),
          ("hub", 16),
          ("iptest", 21),
          ("l2f", 12),
          ("l2tp", 11),
          ("none", 1),
          ("other", 2),
          ("ppp", 3),
          ("rawTCP", 9),
          ("rlogin", 10),
          ("slip", 4),
          ("tandem", 15),
          ("telnet", 8),
          ("terminalServer", 7),
          ("trunk", 13),
          ("unknown", 0),
          ("voice", 14))
    )


_SessionStatusServiceMode_Type.__name__ = "Integer32"
_SessionStatusServiceMode_Object = MibTableColumn
sessionStatusServiceMode = _SessionStatusServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 18),
    _SessionStatusServiceMode_Type()
)
sessionStatusServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusServiceMode.setStatus("current")
_SessionStatusStartTime_Type = Integer32
_SessionStatusStartTime_Object = MibTableColumn
sessionStatusStartTime = _SessionStatusStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 19),
    _SessionStatusStartTime_Type()
)
sessionStatusStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusStartTime.setStatus("current")
_SessionStatusStopTime_Type = Integer32
_SessionStatusStopTime_Object = MibTableColumn
sessionStatusStopTime = _SessionStatusStopTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 20),
    _SessionStatusStopTime_Type()
)
sessionStatusStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusStopTime.setStatus("current")
_SessionStatusTimeOfModemSync_Type = Integer32
_SessionStatusTimeOfModemSync_Object = MibTableColumn
sessionStatusTimeOfModemSync = _SessionStatusTimeOfModemSync_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 21),
    _SessionStatusTimeOfModemSync_Type()
)
sessionStatusTimeOfModemSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusTimeOfModemSync.setStatus("current")
_SessionStatusTimeOfService_Type = Integer32
_SessionStatusTimeOfService_Object = MibTableColumn
sessionStatusTimeOfService = _SessionStatusTimeOfService_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 22),
    _SessionStatusTimeOfService_Type()
)
sessionStatusTimeOfService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusTimeOfService.setStatus("current")


class _SessionStatusTerminatingComponent_Type(Integer32):
    """Custom type sessionStatusTerminatingComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("atmp", 32),
          ("atmptunnel", 33),
          ("chdlc", 9),
          ("cleartcp", 13),
          ("df", 3),
          ("ds0", 4),
          ("dvs", 28),
          ("dvstunnel", 29),
          ("ether", 15),
          ("fax", 30),
          ("fepdf", 17),
          ("fr", 10),
          ("hdlc", 6),
          ("hssi", 22),
          ("ip", 11),
          ("iptest", 34),
          ("l2f", 26),
          ("l2ftunnel", 27),
          ("l2tp", 14),
          ("l2tproute", 31),
          ("lineip", 18),
          ("loopback", 19),
          ("modem", 5),
          ("none", 1),
          ("other", 2),
          ("ppp", 7),
          ("rlogin", 21),
          ("shell", 20),
          ("slip", 8),
          ("sm", 23),
          ("telnet", 12),
          ("trunkip", 16),
          ("unknown", 0),
          ("vl", 24),
          ("voip", 25))
    )


_SessionStatusTerminatingComponent_Type.__name__ = "Integer32"
_SessionStatusTerminatingComponent_Object = MibTableColumn
sessionStatusTerminatingComponent = _SessionStatusTerminatingComponent_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 23),
    _SessionStatusTerminatingComponent_Type()
)
sessionStatusTerminatingComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusTerminatingComponent.setStatus("current")
_SessionStatusTerminationCause_Type = Integer32
_SessionStatusTerminationCause_Object = MibTableColumn
sessionStatusTerminationCause = _SessionStatusTerminationCause_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 24),
    _SessionStatusTerminationCause_Type()
)
sessionStatusTerminationCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusTerminationCause.setStatus("current")


class _SessionStatusLastComponent_Type(Integer32):
    """Custom type sessionStatusLastComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("atmp", 32),
          ("atmptunnel", 33),
          ("chdlc", 9),
          ("cleartcp", 13),
          ("df", 3),
          ("ds0", 4),
          ("dvs", 28),
          ("dvstunnel", 29),
          ("ether", 15),
          ("fax", 30),
          ("fepdf", 17),
          ("fr", 10),
          ("hdlc", 6),
          ("hssi", 22),
          ("ip", 11),
          ("iptest", 34),
          ("l2f", 26),
          ("l2ftunnel", 27),
          ("l2tp", 14),
          ("l2tproute", 31),
          ("lineip", 18),
          ("loopback", 19),
          ("modem", 5),
          ("none", 1),
          ("other", 2),
          ("ppp", 7),
          ("rlogin", 21),
          ("shell", 20),
          ("slip", 8),
          ("sm", 23),
          ("telnet", 12),
          ("trunkip", 16),
          ("unknown", 0),
          ("vl", 24),
          ("voip", 25))
    )


_SessionStatusLastComponent_Type.__name__ = "Integer32"
_SessionStatusLastComponent_Object = MibTableColumn
sessionStatusLastComponent = _SessionStatusLastComponent_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 25),
    _SessionStatusLastComponent_Type()
)
sessionStatusLastComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusLastComponent.setStatus("current")


class _SessionStatusLayer1Slot_Type(Integer32):
    """Custom type sessionStatusLayer1Slot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_SessionStatusLayer1Slot_Type.__name__ = "Integer32"
_SessionStatusLayer1Slot_Object = MibTableColumn
sessionStatusLayer1Slot = _SessionStatusLayer1Slot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 26),
    _SessionStatusLayer1Slot_Type()
)
sessionStatusLayer1Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusLayer1Slot.setStatus("current")


class _SessionStatusLayer2Slot_Type(Integer32):
    """Custom type sessionStatusLayer2Slot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_SessionStatusLayer2Slot_Type.__name__ = "Integer32"
_SessionStatusLayer2Slot_Object = MibTableColumn
sessionStatusLayer2Slot = _SessionStatusLayer2Slot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 27),
    _SessionStatusLayer2Slot_Type()
)
sessionStatusLayer2Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusLayer2Slot.setStatus("current")


class _SessionStatusCalledNumber_Type(DisplayString):
    """Custom type sessionStatusCalledNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SessionStatusCalledNumber_Type.__name__ = "DisplayString"
_SessionStatusCalledNumber_Object = MibTableColumn
sessionStatusCalledNumber = _SessionStatusCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 28),
    _SessionStatusCalledNumber_Type()
)
sessionStatusCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusCalledNumber.setStatus("current")


class _SessionStatusCallingNumber_Type(DisplayString):
    """Custom type sessionStatusCallingNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SessionStatusCallingNumber_Type.__name__ = "DisplayString"
_SessionStatusCallingNumber_Object = MibTableColumn
sessionStatusCallingNumber = _SessionStatusCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 29),
    _SessionStatusCallingNumber_Type()
)
sessionStatusCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusCallingNumber.setStatus("current")


class _SessionStatusOriginateMode_Type(Integer32):
    """Custom type sessionStatusOriginateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("answer", 0),
          ("originate", 1))
    )


_SessionStatusOriginateMode_Type.__name__ = "Integer32"
_SessionStatusOriginateMode_Object = MibTableColumn
sessionStatusOriginateMode = _SessionStatusOriginateMode_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 30),
    _SessionStatusOriginateMode_Type()
)
sessionStatusOriginateMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusOriginateMode.setStatus("current")
_SessionStatusOctetsIn_Type = Integer32
_SessionStatusOctetsIn_Object = MibTableColumn
sessionStatusOctetsIn = _SessionStatusOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 31),
    _SessionStatusOctetsIn_Type()
)
sessionStatusOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusOctetsIn.setStatus("current")
_SessionStatusOctetsOut_Type = Integer32
_SessionStatusOctetsOut_Object = MibTableColumn
sessionStatusOctetsOut = _SessionStatusOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 32),
    _SessionStatusOctetsOut_Type()
)
sessionStatusOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusOctetsOut.setStatus("current")
_SessionStatusPacketsIn_Type = Integer32
_SessionStatusPacketsIn_Object = MibTableColumn
sessionStatusPacketsIn = _SessionStatusPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 33),
    _SessionStatusPacketsIn_Type()
)
sessionStatusPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusPacketsIn.setStatus("current")
_SessionStatusPacketsOut_Type = Integer32
_SessionStatusPacketsOut_Object = MibTableColumn
sessionStatusPacketsOut = _SessionStatusPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 34),
    _SessionStatusPacketsOut_Type()
)
sessionStatusPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusPacketsOut.setStatus("current")
_SessionStatusMultiLinkId_Type = Integer32
_SessionStatusMultiLinkId_Object = MibTableColumn
sessionStatusMultiLinkId = _SessionStatusMultiLinkId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 35),
    _SessionStatusMultiLinkId_Type()
)
sessionStatusMultiLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusMultiLinkId.setStatus("current")
_SessionStatusPort_Type = Integer32
_SessionStatusPort_Object = MibTableColumn
sessionStatusPort = _SessionStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 36),
    _SessionStatusPort_Type()
)
sessionStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusPort.setStatus("current")
_SessionStatusTimeslot_Type = Integer32
_SessionStatusTimeslot_Object = MibTableColumn
sessionStatusTimeslot = _SessionStatusTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 37),
    _SessionStatusTimeslot_Type()
)
sessionStatusTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusTimeslot.setStatus("current")
_SessionStatusLinkCount_Type = Integer32
_SessionStatusLinkCount_Object = MibTableColumn
sessionStatusLinkCount = _SessionStatusLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 38),
    _SessionStatusLinkCount_Type()
)
sessionStatusLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusLinkCount.setStatus("current")
_SessionStatusTxStartDataRate_Type = Integer32
_SessionStatusTxStartDataRate_Object = MibTableColumn
sessionStatusTxStartDataRate = _SessionStatusTxStartDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 39),
    _SessionStatusTxStartDataRate_Type()
)
sessionStatusTxStartDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusTxStartDataRate.setStatus("current")
_SessionStatusRxStartDataRate_Type = Integer32
_SessionStatusRxStartDataRate_Object = MibTableColumn
sessionStatusRxStartDataRate = _SessionStatusRxStartDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 40),
    _SessionStatusRxStartDataRate_Type()
)
sessionStatusRxStartDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusRxStartDataRate.setStatus("current")
_SessionStatusTxEndDataRate_Type = Integer32
_SessionStatusTxEndDataRate_Object = MibTableColumn
sessionStatusTxEndDataRate = _SessionStatusTxEndDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 41),
    _SessionStatusTxEndDataRate_Type()
)
sessionStatusTxEndDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusTxEndDataRate.setStatus("current")
_SessionStatusRxEndDataRate_Type = Integer32
_SessionStatusRxEndDataRate_Object = MibTableColumn
sessionStatusRxEndDataRate = _SessionStatusRxEndDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 42),
    _SessionStatusRxEndDataRate_Type()
)
sessionStatusRxEndDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusRxEndDataRate.setStatus("current")
_SessionStatusTxMinDataRate_Type = Integer32
_SessionStatusTxMinDataRate_Object = MibTableColumn
sessionStatusTxMinDataRate = _SessionStatusTxMinDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 43),
    _SessionStatusTxMinDataRate_Type()
)
sessionStatusTxMinDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusTxMinDataRate.setStatus("current")
_SessionStatusRxMinDataRate_Type = Integer32
_SessionStatusRxMinDataRate_Object = MibTableColumn
sessionStatusRxMinDataRate = _SessionStatusRxMinDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 44),
    _SessionStatusRxMinDataRate_Type()
)
sessionStatusRxMinDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusRxMinDataRate.setStatus("current")
_SessionStatusTxMaxDataRate_Type = Integer32
_SessionStatusTxMaxDataRate_Object = MibTableColumn
sessionStatusTxMaxDataRate = _SessionStatusTxMaxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 45),
    _SessionStatusTxMaxDataRate_Type()
)
sessionStatusTxMaxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusTxMaxDataRate.setStatus("current")
_SessionStatusRxMaxDataRate_Type = Integer32
_SessionStatusRxMaxDataRate_Object = MibTableColumn
sessionStatusRxMaxDataRate = _SessionStatusRxMaxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 46),
    _SessionStatusRxMaxDataRate_Type()
)
sessionStatusRxMaxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusRxMaxDataRate.setStatus("current")
_SessionStatusIop_Type = Integer32
_SessionStatusIop_Object = MibTableColumn
sessionStatusIop = _SessionStatusIop_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 47),
    _SessionStatusIop_Type()
)
sessionStatusIop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusIop.setStatus("current")
_SessionStatusDmm_Type = Integer32
_SessionStatusDmm_Object = MibTableColumn
sessionStatusDmm = _SessionStatusDmm_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 48),
    _SessionStatusDmm_Type()
)
sessionStatusDmm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusDmm.setStatus("current")
_SessionStatusPack_Type = Integer32
_SessionStatusPack_Object = MibTableColumn
sessionStatusPack = _SessionStatusPack_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 49),
    _SessionStatusPack_Type()
)
sessionStatusPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusPack.setStatus("current")
_SessionStatusDevice_Type = Integer32
_SessionStatusDevice_Object = MibTableColumn
sessionStatusDevice = _SessionStatusDevice_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 50),
    _SessionStatusDevice_Type()
)
sessionStatusDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusDevice.setStatus("current")
_SessionStatusTdmStream_Type = Integer32
_SessionStatusTdmStream_Object = MibTableColumn
sessionStatusTdmStream = _SessionStatusTdmStream_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 51),
    _SessionStatusTdmStream_Type()
)
sessionStatusTdmStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusTdmStream.setStatus("current")
_SessionStatusTdmTimeSlot_Type = Integer32
_SessionStatusTdmTimeSlot_Object = MibTableColumn
sessionStatusTdmTimeSlot = _SessionStatusTdmTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 52),
    _SessionStatusTdmTimeSlot_Type()
)
sessionStatusTdmTimeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusTdmTimeSlot.setStatus("current")


class _SessionStatusTerminationReason_Type(DisplayString):
    """Custom type sessionStatusTerminationReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SessionStatusTerminationReason_Type.__name__ = "DisplayString"
_SessionStatusTerminationReason_Object = MibTableColumn
sessionStatusTerminationReason = _SessionStatusTerminationReason_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 53),
    _SessionStatusTerminationReason_Type()
)
sessionStatusTerminationReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusTerminationReason.setStatus("current")
_SessionStatusDuration_Type = Integer32
_SessionStatusDuration_Object = MibTableColumn
sessionStatusDuration = _SessionStatusDuration_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 54),
    _SessionStatusDuration_Type()
)
sessionStatusDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusDuration.setStatus("current")


class _SessionStatusDurationHMS_Type(DisplayString):
    """Custom type sessionStatusDurationHMS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SessionStatusDurationHMS_Type.__name__ = "DisplayString"
_SessionStatusDurationHMS_Object = MibTableColumn
sessionStatusDurationHMS = _SessionStatusDurationHMS_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 55),
    _SessionStatusDurationHMS_Type()
)
sessionStatusDurationHMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusDurationHMS.setStatus("current")


class _SessionStatusSs7SessionId_Type(DisplayString):
    """Custom type sessionStatusSs7SessionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_SessionStatusSs7SessionId_Type.__name__ = "DisplayString"
_SessionStatusSs7SessionId_Object = MibTableColumn
sessionStatusSs7SessionId = _SessionStatusSs7SessionId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 56),
    _SessionStatusSs7SessionId_Type()
)
sessionStatusSs7SessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusSs7SessionId.setStatus("current")
_SessionStatusModemNumber_Type = Integer32
_SessionStatusModemNumber_Object = MibTableColumn
sessionStatusModemNumber = _SessionStatusModemNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 57),
    _SessionStatusModemNumber_Type()
)
sessionStatusModemNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusModemNumber.setStatus("current")


class _SessionStatusTunnelType_Type(Integer32):
    """Custom type sessionStatusTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("atmp", 6),
          ("dvs", 5),
          ("l2f", 3),
          ("l2tp", 4),
          ("none", 1),
          ("other", 2),
          ("unknown", 0))
    )


_SessionStatusTunnelType_Type.__name__ = "Integer32"
_SessionStatusTunnelType_Object = MibTableColumn
sessionStatusTunnelType = _SessionStatusTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 58),
    _SessionStatusTunnelType_Type()
)
sessionStatusTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusTunnelType.setStatus("current")


class _SessionStatusTunnelMediumType_Type(Integer32):
    """Custom type sessionStatusTunnelMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 3),
          ("none", 1),
          ("other", 2),
          ("unknown", 0))
    )


_SessionStatusTunnelMediumType_Type.__name__ = "Integer32"
_SessionStatusTunnelMediumType_Object = MibTableColumn
sessionStatusTunnelMediumType = _SessionStatusTunnelMediumType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 59),
    _SessionStatusTunnelMediumType_Type()
)
sessionStatusTunnelMediumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusTunnelMediumType.setStatus("current")
_SessionStatusTunnelServerAddress_Type = IpAddress
_SessionStatusTunnelServerAddress_Object = MibTableColumn
sessionStatusTunnelServerAddress = _SessionStatusTunnelServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 60),
    _SessionStatusTunnelServerAddress_Type()
)
sessionStatusTunnelServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusTunnelServerAddress.setStatus("current")
_SessionStatusCallClass_Type = Integer32
_SessionStatusCallClass_Object = MibTableColumn
sessionStatusCallClass = _SessionStatusCallClass_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 61),
    _SessionStatusCallClass_Type()
)
sessionStatusCallClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusCallClass.setStatus("current")
_SessionStatusTandemPort_Type = Integer32
_SessionStatusTandemPort_Object = MibTableColumn
sessionStatusTandemPort = _SessionStatusTandemPort_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 62),
    _SessionStatusTandemPort_Type()
)
sessionStatusTandemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusTandemPort.setStatus("current")
_SessionStatusTandemTimeslot_Type = Integer32
_SessionStatusTandemTimeslot_Object = MibTableColumn
sessionStatusTandemTimeslot = _SessionStatusTandemTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 63),
    _SessionStatusTandemTimeslot_Type()
)
sessionStatusTandemTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusTandemTimeslot.setStatus("current")


class _SessionStatusCallClassArray_Type(OctetString):
    """Custom type sessionStatusCallClassArray based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SessionStatusCallClassArray_Type.__name__ = "OctetString"
_SessionStatusCallClassArray_Object = MibTableColumn
sessionStatusCallClassArray = _SessionStatusCallClassArray_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 64),
    _SessionStatusCallClassArray_Type()
)
sessionStatusCallClassArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusCallClassArray.setStatus("current")
_SessionStatusCallClassLen_Type = Integer32
_SessionStatusCallClassLen_Object = MibTableColumn
sessionStatusCallClassLen = _SessionStatusCallClassLen_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 65),
    _SessionStatusCallClassLen_Type()
)
sessionStatusCallClassLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusCallClassLen.setStatus("current")


class _SessionStatusActualAuthMethod_Type(Integer32):
    """Custom type sessionStatusActualAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("radius", 1),
          ("remote", 3))
    )


_SessionStatusActualAuthMethod_Type.__name__ = "Integer32"
_SessionStatusActualAuthMethod_Object = MibTableColumn
sessionStatusActualAuthMethod = _SessionStatusActualAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 66),
    _SessionStatusActualAuthMethod_Type()
)
sessionStatusActualAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActualAuthMethod.setStatus("current")


class _SessionStatusModemModulation_Type(Integer32):
    """Custom type sessionStatusModemModulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("bell103", 2),
          ("bell208", 3),
          ("bell212", 4),
          ("k56", 17),
          ("none", 0),
          ("unknown", 1),
          ("v17", 5),
          ("v21", 6),
          ("v22", 7),
          ("v22bis", 8),
          ("v23", 9),
          ("v27", 10),
          ("v29", 11),
          ("v32", 12),
          ("v32bis", 13),
          ("v33", 14),
          ("v34", 15),
          ("v90", 18),
          ("vFC", 16))
    )


_SessionStatusModemModulation_Type.__name__ = "Integer32"
_SessionStatusModemModulation_Object = MibTableColumn
sessionStatusModemModulation = _SessionStatusModemModulation_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 67),
    _SessionStatusModemModulation_Type()
)
sessionStatusModemModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusModemModulation.setStatus("current")


class _SessionStatusModemErrorCorrection_Type(Integer32):
    """Custom type sessionStatusModemErrorCorrection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mNP", 2),
          ("none", 0),
          ("unknown", 1),
          ("v42", 3))
    )


_SessionStatusModemErrorCorrection_Type.__name__ = "Integer32"
_SessionStatusModemErrorCorrection_Object = MibTableColumn
sessionStatusModemErrorCorrection = _SessionStatusModemErrorCorrection_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 68),
    _SessionStatusModemErrorCorrection_Type()
)
sessionStatusModemErrorCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusModemErrorCorrection.setStatus("current")


class _SessionStatusModemDataCompression_Type(Integer32):
    """Custom type sessionStatusModemDataCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mNP5", 2),
          ("none", 0),
          ("unknown", 1),
          ("v42bis", 3))
    )


_SessionStatusModemDataCompression_Type.__name__ = "Integer32"
_SessionStatusModemDataCompression_Object = MibTableColumn
sessionStatusModemDataCompression = _SessionStatusModemDataCompression_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 69),
    _SessionStatusModemDataCompression_Type()
)
sessionStatusModemDataCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusModemDataCompression.setStatus("current")
_SessionStatusModemTxBlocks_Type = Integer32
_SessionStatusModemTxBlocks_Object = MibTableColumn
sessionStatusModemTxBlocks = _SessionStatusModemTxBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 70),
    _SessionStatusModemTxBlocks_Type()
)
sessionStatusModemTxBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusModemTxBlocks.setStatus("current")
_SessionStatusModemRetransmits_Type = Integer32
_SessionStatusModemRetransmits_Object = MibTableColumn
sessionStatusModemRetransmits = _SessionStatusModemRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 71),
    _SessionStatusModemRetransmits_Type()
)
sessionStatusModemRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusModemRetransmits.setStatus("current")
_SessionStatusModemSNR_Type = Integer32
_SessionStatusModemSNR_Object = MibTableColumn
sessionStatusModemSNR = _SessionStatusModemSNR_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 72),
    _SessionStatusModemSNR_Type()
)
sessionStatusModemSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusModemSNR.setStatus("current")
_SessionStatusModemLocalRetrains_Type = Integer32
_SessionStatusModemLocalRetrains_Object = MibTableColumn
sessionStatusModemLocalRetrains = _SessionStatusModemLocalRetrains_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 73),
    _SessionStatusModemLocalRetrains_Type()
)
sessionStatusModemLocalRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusModemLocalRetrains.setStatus("current")
_SessionStatusModemRemoteRetrains_Type = Integer32
_SessionStatusModemRemoteRetrains_Object = MibTableColumn
sessionStatusModemRemoteRetrains = _SessionStatusModemRemoteRetrains_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 74),
    _SessionStatusModemRemoteRetrains_Type()
)
sessionStatusModemRemoteRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusModemRemoteRetrains.setStatus("current")
_SessionStatusModemLocalRenegotiations_Type = Integer32
_SessionStatusModemLocalRenegotiations_Object = MibTableColumn
sessionStatusModemLocalRenegotiations = _SessionStatusModemLocalRenegotiations_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 75),
    _SessionStatusModemLocalRenegotiations_Type()
)
sessionStatusModemLocalRenegotiations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusModemLocalRenegotiations.setStatus("current")
_SessionStatusModemRemoteRenegotiations_Type = Integer32
_SessionStatusModemRemoteRenegotiations_Object = MibTableColumn
sessionStatusModemRemoteRenegotiations = _SessionStatusModemRemoteRenegotiations_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 76),
    _SessionStatusModemRemoteRenegotiations_Type()
)
sessionStatusModemRemoteRenegotiations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusModemRemoteRenegotiations.setStatus("current")
_SessionStatusModemReceiveLineLevel_Type = Integer32
_SessionStatusModemReceiveLineLevel_Object = MibTableColumn
sessionStatusModemReceiveLineLevel = _SessionStatusModemReceiveLineLevel_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 77),
    _SessionStatusModemReceiveLineLevel_Type()
)
sessionStatusModemReceiveLineLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusModemReceiveLineLevel.setStatus("current")
_SessionStatusRemoteIPXNetwork_Type = Integer32
_SessionStatusRemoteIPXNetwork_Object = MibTableColumn
sessionStatusRemoteIPXNetwork = _SessionStatusRemoteIPXNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 78),
    _SessionStatusRemoteIPXNetwork_Type()
)
sessionStatusRemoteIPXNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusRemoteIPXNetwork.setStatus("current")


class _SessionStatusRemoteIPXNode_Type(DisplayString):
    """Custom type sessionStatusRemoteIPXNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SessionStatusRemoteIPXNode_Type.__name__ = "DisplayString"
_SessionStatusRemoteIPXNode_Object = MibTableColumn
sessionStatusRemoteIPXNode = _SessionStatusRemoteIPXNode_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 79),
    _SessionStatusRemoteIPXNode_Type()
)
sessionStatusRemoteIPXNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusRemoteIPXNode.setStatus("current")
_SessionStatusCleartcpRemoteIP_Type = IpAddress
_SessionStatusCleartcpRemoteIP_Object = MibTableColumn
sessionStatusCleartcpRemoteIP = _SessionStatusCleartcpRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 80),
    _SessionStatusCleartcpRemoteIP_Type()
)
sessionStatusCleartcpRemoteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusCleartcpRemoteIP.setStatus("current")
_SessionStatusCleartcpRemotePort_Type = Integer32
_SessionStatusCleartcpRemotePort_Object = MibTableColumn
sessionStatusCleartcpRemotePort = _SessionStatusCleartcpRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 81),
    _SessionStatusCleartcpRemotePort_Type()
)
sessionStatusCleartcpRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusCleartcpRemotePort.setStatus("current")
_SessionStatusTunnelId_Type = Integer32
_SessionStatusTunnelId_Object = MibTableColumn
sessionStatusTunnelId = _SessionStatusTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 82),
    _SessionStatusTunnelId_Type()
)
sessionStatusTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusTunnelId.setStatus("current")
_SessionStatusLinkId_Type = Integer32
_SessionStatusLinkId_Object = MibTableColumn
sessionStatusLinkId = _SessionStatusLinkId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 101, 1, 83),
    _SessionStatusLinkId_Type()
)
sessionStatusLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusLinkId.setStatus("current")
_SessionStatusActiveTable_Object = MibTable
sessionStatusActiveTable = _SessionStatusActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102)
)
if mibBuilder.loadTexts:
    sessionStatusActiveTable.setStatus("current")
_SessionStatusActiveEntry_Object = MibTableRow
sessionStatusActiveEntry = _SessionStatusActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1)
)
sessionStatusActiveEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "sessionStatusActiveSessionID"),
)
if mibBuilder.loadTexts:
    sessionStatusActiveEntry.setStatus("current")
_SessionStatusActiveSessionID_Type = Integer32
_SessionStatusActiveSessionID_Object = MibTableColumn
sessionStatusActiveSessionID = _SessionStatusActiveSessionID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 2),
    _SessionStatusActiveSessionID_Type()
)
sessionStatusActiveSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveSessionID.setStatus("current")


class _SessionStatusActiveState_Type(Integer32):
    """Custom type sessionStatusActiveState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_SessionStatusActiveState_Type.__name__ = "Integer32"
_SessionStatusActiveState_Object = MibTableColumn
sessionStatusActiveState = _SessionStatusActiveState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 3),
    _SessionStatusActiveState_Type()
)
sessionStatusActiveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveState.setStatus("current")


class _SessionStatusActivePermanentFlag_Type(Integer32):
    """Custom type sessionStatusActivePermanentFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permanent", 2),
          ("switched", 1),
          ("unknown", 0))
    )


_SessionStatusActivePermanentFlag_Type.__name__ = "Integer32"
_SessionStatusActivePermanentFlag_Object = MibTableColumn
sessionStatusActivePermanentFlag = _SessionStatusActivePermanentFlag_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 10),
    _SessionStatusActivePermanentFlag_Type()
)
sessionStatusActivePermanentFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActivePermanentFlag.setStatus("current")
_SessionStatusActiveVpopId_Type = Integer32
_SessionStatusActiveVpopId_Object = MibTableColumn
sessionStatusActiveVpopId = _SessionStatusActiveVpopId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 11),
    _SessionStatusActiveVpopId_Type()
)
sessionStatusActiveVpopId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveVpopId.setStatus("current")


class _SessionStatusActiveName_Type(DisplayString):
    """Custom type sessionStatusActiveName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 68),
    )


_SessionStatusActiveName_Type.__name__ = "DisplayString"
_SessionStatusActiveName_Object = MibTableColumn
sessionStatusActiveName = _SessionStatusActiveName_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 12),
    _SessionStatusActiveName_Type()
)
sessionStatusActiveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveName.setStatus("current")
_SessionStatusActiveRemoteIP_Type = IpAddress
_SessionStatusActiveRemoteIP_Object = MibTableColumn
sessionStatusActiveRemoteIP = _SessionStatusActiveRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 13),
    _SessionStatusActiveRemoteIP_Type()
)
sessionStatusActiveRemoteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveRemoteIP.setStatus("current")
_SessionStatusActiveRemoteIPMask_Type = IpAddress
_SessionStatusActiveRemoteIPMask_Object = MibTableColumn
sessionStatusActiveRemoteIPMask = _SessionStatusActiveRemoteIPMask_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 14),
    _SessionStatusActiveRemoteIPMask_Type()
)
sessionStatusActiveRemoteIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveRemoteIPMask.setStatus("current")
_SessionStatusActiveLocalIP_Type = IpAddress
_SessionStatusActiveLocalIP_Object = MibTableColumn
sessionStatusActiveLocalIP = _SessionStatusActiveLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 15),
    _SessionStatusActiveLocalIP_Type()
)
sessionStatusActiveLocalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveLocalIP.setStatus("current")
_SessionStatusActiveLocalIPMask_Type = IpAddress
_SessionStatusActiveLocalIPMask_Object = MibTableColumn
sessionStatusActiveLocalIPMask = _SessionStatusActiveLocalIPMask_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 16),
    _SessionStatusActiveLocalIPMask_Type()
)
sessionStatusActiveLocalIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveLocalIPMask.setStatus("current")


class _SessionStatusActiveLinkService_Type(Integer32):
    """Custom type sessionStatusActiveLinkService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 11),
          ("hssi", 14),
          ("hub", 15),
          ("isdn56K", 3),
          ("isdn64K", 4),
          ("isdnV110", 6),
          ("isdnV120", 5),
          ("loopback", 13),
          ("modemK56", 9),
          ("modemV32", 7),
          ("modemV34", 8),
          ("modemV90", 10),
          ("none", 1),
          ("other", 2),
          ("t1Trunk", 12),
          ("unknown", 0),
          ("voice", 16))
    )


_SessionStatusActiveLinkService_Type.__name__ = "Integer32"
_SessionStatusActiveLinkService_Object = MibTableColumn
sessionStatusActiveLinkService = _SessionStatusActiveLinkService_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 17),
    _SessionStatusActiveLinkService_Type()
)
sessionStatusActiveLinkService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveLinkService.setStatus("current")


class _SessionStatusActiveServiceMode_Type(Integer32):
    """Custom type sessionStatusActiveServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("atmp", 20),
          ("ciscoHDLC", 6),
          ("dvs", 18),
          ("fax", 19),
          ("frameRelay", 5),
          ("ftp", 17),
          ("hub", 16),
          ("iptest", 21),
          ("l2f", 12),
          ("l2tp", 11),
          ("none", 1),
          ("other", 2),
          ("ppp", 3),
          ("rawTCP", 9),
          ("rlogin", 10),
          ("slip", 4),
          ("tandem", 15),
          ("telnet", 8),
          ("terminalServer", 7),
          ("trunk", 13),
          ("unknown", 0),
          ("voice", 14))
    )


_SessionStatusActiveServiceMode_Type.__name__ = "Integer32"
_SessionStatusActiveServiceMode_Object = MibTableColumn
sessionStatusActiveServiceMode = _SessionStatusActiveServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 18),
    _SessionStatusActiveServiceMode_Type()
)
sessionStatusActiveServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveServiceMode.setStatus("current")
_SessionStatusActiveStartTime_Type = Integer32
_SessionStatusActiveStartTime_Object = MibTableColumn
sessionStatusActiveStartTime = _SessionStatusActiveStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 19),
    _SessionStatusActiveStartTime_Type()
)
sessionStatusActiveStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveStartTime.setStatus("current")
_SessionStatusActiveStopTime_Type = Integer32
_SessionStatusActiveStopTime_Object = MibTableColumn
sessionStatusActiveStopTime = _SessionStatusActiveStopTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 20),
    _SessionStatusActiveStopTime_Type()
)
sessionStatusActiveStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveStopTime.setStatus("current")
_SessionStatusActiveTimeOfModemSync_Type = Integer32
_SessionStatusActiveTimeOfModemSync_Object = MibTableColumn
sessionStatusActiveTimeOfModemSync = _SessionStatusActiveTimeOfModemSync_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 21),
    _SessionStatusActiveTimeOfModemSync_Type()
)
sessionStatusActiveTimeOfModemSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveTimeOfModemSync.setStatus("current")
_SessionStatusActiveTimeOfService_Type = Integer32
_SessionStatusActiveTimeOfService_Object = MibTableColumn
sessionStatusActiveTimeOfService = _SessionStatusActiveTimeOfService_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 22),
    _SessionStatusActiveTimeOfService_Type()
)
sessionStatusActiveTimeOfService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveTimeOfService.setStatus("current")


class _SessionStatusActiveTerminatingComponent_Type(Integer32):
    """Custom type sessionStatusActiveTerminatingComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("atmp", 32),
          ("atmptunnel", 33),
          ("chdlc", 9),
          ("cleartcp", 13),
          ("df", 3),
          ("ds0", 4),
          ("dvs", 28),
          ("dvstunnel", 29),
          ("ether", 15),
          ("fax", 30),
          ("fepdf", 17),
          ("fr", 10),
          ("hdlc", 6),
          ("hssi", 22),
          ("ip", 11),
          ("iptest", 34),
          ("l2f", 26),
          ("l2ftunnel", 27),
          ("l2tp", 14),
          ("l2tproute", 31),
          ("lineip", 18),
          ("loopback", 19),
          ("modem", 5),
          ("none", 1),
          ("other", 2),
          ("ppp", 7),
          ("rlogin", 21),
          ("shell", 20),
          ("slip", 8),
          ("sm", 23),
          ("telnet", 12),
          ("trunkip", 16),
          ("unknown", 0),
          ("vl", 24),
          ("voip", 25))
    )


_SessionStatusActiveTerminatingComponent_Type.__name__ = "Integer32"
_SessionStatusActiveTerminatingComponent_Object = MibTableColumn
sessionStatusActiveTerminatingComponent = _SessionStatusActiveTerminatingComponent_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 23),
    _SessionStatusActiveTerminatingComponent_Type()
)
sessionStatusActiveTerminatingComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveTerminatingComponent.setStatus("current")
_SessionStatusActiveTerminationCause_Type = Integer32
_SessionStatusActiveTerminationCause_Object = MibTableColumn
sessionStatusActiveTerminationCause = _SessionStatusActiveTerminationCause_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 24),
    _SessionStatusActiveTerminationCause_Type()
)
sessionStatusActiveTerminationCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveTerminationCause.setStatus("current")


class _SessionStatusActiveLastComponent_Type(Integer32):
    """Custom type sessionStatusActiveLastComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("atmp", 32),
          ("atmptunnel", 33),
          ("chdlc", 9),
          ("cleartcp", 13),
          ("df", 3),
          ("ds0", 4),
          ("dvs", 28),
          ("dvstunnel", 29),
          ("ether", 15),
          ("fax", 30),
          ("fepdf", 17),
          ("fr", 10),
          ("hdlc", 6),
          ("hssi", 22),
          ("ip", 11),
          ("iptest", 34),
          ("l2f", 26),
          ("l2ftunnel", 27),
          ("l2tp", 14),
          ("l2tproute", 31),
          ("lineip", 18),
          ("loopback", 19),
          ("modem", 5),
          ("none", 1),
          ("other", 2),
          ("ppp", 7),
          ("rlogin", 21),
          ("shell", 20),
          ("slip", 8),
          ("sm", 23),
          ("telnet", 12),
          ("trunkip", 16),
          ("unknown", 0),
          ("vl", 24),
          ("voip", 25))
    )


_SessionStatusActiveLastComponent_Type.__name__ = "Integer32"
_SessionStatusActiveLastComponent_Object = MibTableColumn
sessionStatusActiveLastComponent = _SessionStatusActiveLastComponent_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 25),
    _SessionStatusActiveLastComponent_Type()
)
sessionStatusActiveLastComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveLastComponent.setStatus("current")


class _SessionStatusActiveLayer1Slot_Type(Integer32):
    """Custom type sessionStatusActiveLayer1Slot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_SessionStatusActiveLayer1Slot_Type.__name__ = "Integer32"
_SessionStatusActiveLayer1Slot_Object = MibTableColumn
sessionStatusActiveLayer1Slot = _SessionStatusActiveLayer1Slot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 26),
    _SessionStatusActiveLayer1Slot_Type()
)
sessionStatusActiveLayer1Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveLayer1Slot.setStatus("current")


class _SessionStatusActiveLayer2Slot_Type(Integer32):
    """Custom type sessionStatusActiveLayer2Slot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_SessionStatusActiveLayer2Slot_Type.__name__ = "Integer32"
_SessionStatusActiveLayer2Slot_Object = MibTableColumn
sessionStatusActiveLayer2Slot = _SessionStatusActiveLayer2Slot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 27),
    _SessionStatusActiveLayer2Slot_Type()
)
sessionStatusActiveLayer2Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveLayer2Slot.setStatus("current")


class _SessionStatusActiveCalledNumber_Type(DisplayString):
    """Custom type sessionStatusActiveCalledNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SessionStatusActiveCalledNumber_Type.__name__ = "DisplayString"
_SessionStatusActiveCalledNumber_Object = MibTableColumn
sessionStatusActiveCalledNumber = _SessionStatusActiveCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 28),
    _SessionStatusActiveCalledNumber_Type()
)
sessionStatusActiveCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveCalledNumber.setStatus("current")


class _SessionStatusActiveCallingNumber_Type(DisplayString):
    """Custom type sessionStatusActiveCallingNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SessionStatusActiveCallingNumber_Type.__name__ = "DisplayString"
_SessionStatusActiveCallingNumber_Object = MibTableColumn
sessionStatusActiveCallingNumber = _SessionStatusActiveCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 29),
    _SessionStatusActiveCallingNumber_Type()
)
sessionStatusActiveCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveCallingNumber.setStatus("current")


class _SessionStatusActiveOriginateMode_Type(Integer32):
    """Custom type sessionStatusActiveOriginateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("answer", 0),
          ("originate", 1))
    )


_SessionStatusActiveOriginateMode_Type.__name__ = "Integer32"
_SessionStatusActiveOriginateMode_Object = MibTableColumn
sessionStatusActiveOriginateMode = _SessionStatusActiveOriginateMode_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 30),
    _SessionStatusActiveOriginateMode_Type()
)
sessionStatusActiveOriginateMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveOriginateMode.setStatus("current")
_SessionStatusActiveOctetsIn_Type = Integer32
_SessionStatusActiveOctetsIn_Object = MibTableColumn
sessionStatusActiveOctetsIn = _SessionStatusActiveOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 31),
    _SessionStatusActiveOctetsIn_Type()
)
sessionStatusActiveOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveOctetsIn.setStatus("current")
_SessionStatusActiveOctetsOut_Type = Integer32
_SessionStatusActiveOctetsOut_Object = MibTableColumn
sessionStatusActiveOctetsOut = _SessionStatusActiveOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 32),
    _SessionStatusActiveOctetsOut_Type()
)
sessionStatusActiveOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveOctetsOut.setStatus("current")
_SessionStatusActivePacketsIn_Type = Integer32
_SessionStatusActivePacketsIn_Object = MibTableColumn
sessionStatusActivePacketsIn = _SessionStatusActivePacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 33),
    _SessionStatusActivePacketsIn_Type()
)
sessionStatusActivePacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActivePacketsIn.setStatus("current")
_SessionStatusActivePacketsOut_Type = Integer32
_SessionStatusActivePacketsOut_Object = MibTableColumn
sessionStatusActivePacketsOut = _SessionStatusActivePacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 34),
    _SessionStatusActivePacketsOut_Type()
)
sessionStatusActivePacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActivePacketsOut.setStatus("current")
_SessionStatusActiveMultiLinkId_Type = Integer32
_SessionStatusActiveMultiLinkId_Object = MibTableColumn
sessionStatusActiveMultiLinkId = _SessionStatusActiveMultiLinkId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 35),
    _SessionStatusActiveMultiLinkId_Type()
)
sessionStatusActiveMultiLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveMultiLinkId.setStatus("current")
_SessionStatusActivePort_Type = Integer32
_SessionStatusActivePort_Object = MibTableColumn
sessionStatusActivePort = _SessionStatusActivePort_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 36),
    _SessionStatusActivePort_Type()
)
sessionStatusActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActivePort.setStatus("current")
_SessionStatusActiveTimeslot_Type = Integer32
_SessionStatusActiveTimeslot_Object = MibTableColumn
sessionStatusActiveTimeslot = _SessionStatusActiveTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 37),
    _SessionStatusActiveTimeslot_Type()
)
sessionStatusActiveTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveTimeslot.setStatus("current")
_SessionStatusActiveLinkCount_Type = Integer32
_SessionStatusActiveLinkCount_Object = MibTableColumn
sessionStatusActiveLinkCount = _SessionStatusActiveLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 38),
    _SessionStatusActiveLinkCount_Type()
)
sessionStatusActiveLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveLinkCount.setStatus("current")
_SessionStatusActiveTxStartDataRate_Type = Integer32
_SessionStatusActiveTxStartDataRate_Object = MibTableColumn
sessionStatusActiveTxStartDataRate = _SessionStatusActiveTxStartDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 39),
    _SessionStatusActiveTxStartDataRate_Type()
)
sessionStatusActiveTxStartDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveTxStartDataRate.setStatus("current")
_SessionStatusActiveRxStartDataRate_Type = Integer32
_SessionStatusActiveRxStartDataRate_Object = MibTableColumn
sessionStatusActiveRxStartDataRate = _SessionStatusActiveRxStartDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 40),
    _SessionStatusActiveRxStartDataRate_Type()
)
sessionStatusActiveRxStartDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveRxStartDataRate.setStatus("current")
_SessionStatusActiveTxEndDataRate_Type = Integer32
_SessionStatusActiveTxEndDataRate_Object = MibTableColumn
sessionStatusActiveTxEndDataRate = _SessionStatusActiveTxEndDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 41),
    _SessionStatusActiveTxEndDataRate_Type()
)
sessionStatusActiveTxEndDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveTxEndDataRate.setStatus("current")
_SessionStatusActiveRxEndDataRate_Type = Integer32
_SessionStatusActiveRxEndDataRate_Object = MibTableColumn
sessionStatusActiveRxEndDataRate = _SessionStatusActiveRxEndDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 42),
    _SessionStatusActiveRxEndDataRate_Type()
)
sessionStatusActiveRxEndDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveRxEndDataRate.setStatus("current")
_SessionStatusActiveTxMinDataRate_Type = Integer32
_SessionStatusActiveTxMinDataRate_Object = MibTableColumn
sessionStatusActiveTxMinDataRate = _SessionStatusActiveTxMinDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 43),
    _SessionStatusActiveTxMinDataRate_Type()
)
sessionStatusActiveTxMinDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveTxMinDataRate.setStatus("current")
_SessionStatusActiveRxMinDataRate_Type = Integer32
_SessionStatusActiveRxMinDataRate_Object = MibTableColumn
sessionStatusActiveRxMinDataRate = _SessionStatusActiveRxMinDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 44),
    _SessionStatusActiveRxMinDataRate_Type()
)
sessionStatusActiveRxMinDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveRxMinDataRate.setStatus("current")
_SessionStatusActiveTxMaxDataRate_Type = Integer32
_SessionStatusActiveTxMaxDataRate_Object = MibTableColumn
sessionStatusActiveTxMaxDataRate = _SessionStatusActiveTxMaxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 45),
    _SessionStatusActiveTxMaxDataRate_Type()
)
sessionStatusActiveTxMaxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveTxMaxDataRate.setStatus("current")
_SessionStatusActiveRxMaxDataRate_Type = Integer32
_SessionStatusActiveRxMaxDataRate_Object = MibTableColumn
sessionStatusActiveRxMaxDataRate = _SessionStatusActiveRxMaxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 46),
    _SessionStatusActiveRxMaxDataRate_Type()
)
sessionStatusActiveRxMaxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveRxMaxDataRate.setStatus("current")
_SessionStatusActiveIop_Type = Integer32
_SessionStatusActiveIop_Object = MibTableColumn
sessionStatusActiveIop = _SessionStatusActiveIop_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 47),
    _SessionStatusActiveIop_Type()
)
sessionStatusActiveIop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveIop.setStatus("current")
_SessionStatusActiveDmm_Type = Integer32
_SessionStatusActiveDmm_Object = MibTableColumn
sessionStatusActiveDmm = _SessionStatusActiveDmm_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 48),
    _SessionStatusActiveDmm_Type()
)
sessionStatusActiveDmm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveDmm.setStatus("current")
_SessionStatusActivePack_Type = Integer32
_SessionStatusActivePack_Object = MibTableColumn
sessionStatusActivePack = _SessionStatusActivePack_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 49),
    _SessionStatusActivePack_Type()
)
sessionStatusActivePack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActivePack.setStatus("current")
_SessionStatusActiveDevice_Type = Integer32
_SessionStatusActiveDevice_Object = MibTableColumn
sessionStatusActiveDevice = _SessionStatusActiveDevice_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 50),
    _SessionStatusActiveDevice_Type()
)
sessionStatusActiveDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveDevice.setStatus("current")
_SessionStatusActiveTdmStream_Type = Integer32
_SessionStatusActiveTdmStream_Object = MibTableColumn
sessionStatusActiveTdmStream = _SessionStatusActiveTdmStream_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 51),
    _SessionStatusActiveTdmStream_Type()
)
sessionStatusActiveTdmStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveTdmStream.setStatus("current")
_SessionStatusActiveTdmTimeSlot_Type = Integer32
_SessionStatusActiveTdmTimeSlot_Object = MibTableColumn
sessionStatusActiveTdmTimeSlot = _SessionStatusActiveTdmTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 52),
    _SessionStatusActiveTdmTimeSlot_Type()
)
sessionStatusActiveTdmTimeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveTdmTimeSlot.setStatus("current")


class _SessionStatusActiveTerminationReason_Type(DisplayString):
    """Custom type sessionStatusActiveTerminationReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SessionStatusActiveTerminationReason_Type.__name__ = "DisplayString"
_SessionStatusActiveTerminationReason_Object = MibTableColumn
sessionStatusActiveTerminationReason = _SessionStatusActiveTerminationReason_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 53),
    _SessionStatusActiveTerminationReason_Type()
)
sessionStatusActiveTerminationReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveTerminationReason.setStatus("current")
_SessionStatusActiveDuration_Type = Integer32
_SessionStatusActiveDuration_Object = MibTableColumn
sessionStatusActiveDuration = _SessionStatusActiveDuration_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 54),
    _SessionStatusActiveDuration_Type()
)
sessionStatusActiveDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveDuration.setStatus("current")


class _SessionStatusActiveDurationHMS_Type(DisplayString):
    """Custom type sessionStatusActiveDurationHMS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SessionStatusActiveDurationHMS_Type.__name__ = "DisplayString"
_SessionStatusActiveDurationHMS_Object = MibTableColumn
sessionStatusActiveDurationHMS = _SessionStatusActiveDurationHMS_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 55),
    _SessionStatusActiveDurationHMS_Type()
)
sessionStatusActiveDurationHMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveDurationHMS.setStatus("current")


class _SessionStatusActiveSs7SessionId_Type(DisplayString):
    """Custom type sessionStatusActiveSs7SessionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 41),
    )


_SessionStatusActiveSs7SessionId_Type.__name__ = "DisplayString"
_SessionStatusActiveSs7SessionId_Object = MibTableColumn
sessionStatusActiveSs7SessionId = _SessionStatusActiveSs7SessionId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 56),
    _SessionStatusActiveSs7SessionId_Type()
)
sessionStatusActiveSs7SessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveSs7SessionId.setStatus("current")
_SessionStatusActiveModemNumber_Type = Integer32
_SessionStatusActiveModemNumber_Object = MibTableColumn
sessionStatusActiveModemNumber = _SessionStatusActiveModemNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 57),
    _SessionStatusActiveModemNumber_Type()
)
sessionStatusActiveModemNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveModemNumber.setStatus("current")


class _SessionStatusActiveTunnelType_Type(Integer32):
    """Custom type sessionStatusActiveTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("atmp", 6),
          ("dvs", 5),
          ("l2f", 3),
          ("l2tp", 4),
          ("none", 1),
          ("other", 2),
          ("unknown", 0))
    )


_SessionStatusActiveTunnelType_Type.__name__ = "Integer32"
_SessionStatusActiveTunnelType_Object = MibTableColumn
sessionStatusActiveTunnelType = _SessionStatusActiveTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 58),
    _SessionStatusActiveTunnelType_Type()
)
sessionStatusActiveTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveTunnelType.setStatus("current")


class _SessionStatusActiveTunnelMediumType_Type(Integer32):
    """Custom type sessionStatusActiveTunnelMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 3),
          ("none", 1),
          ("other", 2),
          ("unknown", 0))
    )


_SessionStatusActiveTunnelMediumType_Type.__name__ = "Integer32"
_SessionStatusActiveTunnelMediumType_Object = MibTableColumn
sessionStatusActiveTunnelMediumType = _SessionStatusActiveTunnelMediumType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 59),
    _SessionStatusActiveTunnelMediumType_Type()
)
sessionStatusActiveTunnelMediumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveTunnelMediumType.setStatus("current")
_SessionStatusActiveTunnelServerAddress_Type = IpAddress
_SessionStatusActiveTunnelServerAddress_Object = MibTableColumn
sessionStatusActiveTunnelServerAddress = _SessionStatusActiveTunnelServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 60),
    _SessionStatusActiveTunnelServerAddress_Type()
)
sessionStatusActiveTunnelServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveTunnelServerAddress.setStatus("current")
_SessionStatusActiveCallClass_Type = Integer32
_SessionStatusActiveCallClass_Object = MibTableColumn
sessionStatusActiveCallClass = _SessionStatusActiveCallClass_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 61),
    _SessionStatusActiveCallClass_Type()
)
sessionStatusActiveCallClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveCallClass.setStatus("current")
_SessionStatusActiveTandemPort_Type = Integer32
_SessionStatusActiveTandemPort_Object = MibTableColumn
sessionStatusActiveTandemPort = _SessionStatusActiveTandemPort_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 62),
    _SessionStatusActiveTandemPort_Type()
)
sessionStatusActiveTandemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveTandemPort.setStatus("current")
_SessionStatusActiveTandemTimeslot_Type = Integer32
_SessionStatusActiveTandemTimeslot_Object = MibTableColumn
sessionStatusActiveTandemTimeslot = _SessionStatusActiveTandemTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 63),
    _SessionStatusActiveTandemTimeslot_Type()
)
sessionStatusActiveTandemTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveTandemTimeslot.setStatus("current")


class _SessionStatusActiveCallClassArray_Type(OctetString):
    """Custom type sessionStatusActiveCallClassArray based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SessionStatusActiveCallClassArray_Type.__name__ = "OctetString"
_SessionStatusActiveCallClassArray_Object = MibTableColumn
sessionStatusActiveCallClassArray = _SessionStatusActiveCallClassArray_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 64),
    _SessionStatusActiveCallClassArray_Type()
)
sessionStatusActiveCallClassArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveCallClassArray.setStatus("current")
_SessionStatusActiveCallClassLen_Type = Integer32
_SessionStatusActiveCallClassLen_Object = MibTableColumn
sessionStatusActiveCallClassLen = _SessionStatusActiveCallClassLen_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 65),
    _SessionStatusActiveCallClassLen_Type()
)
sessionStatusActiveCallClassLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveCallClassLen.setStatus("current")


class _SessionStatusActiveActualAuthMethod_Type(Integer32):
    """Custom type sessionStatusActiveActualAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("radius", 1),
          ("remote", 3))
    )


_SessionStatusActiveActualAuthMethod_Type.__name__ = "Integer32"
_SessionStatusActiveActualAuthMethod_Object = MibTableColumn
sessionStatusActiveActualAuthMethod = _SessionStatusActiveActualAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 66),
    _SessionStatusActiveActualAuthMethod_Type()
)
sessionStatusActiveActualAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveActualAuthMethod.setStatus("current")


class _SessionStatusActiveModemModulation_Type(Integer32):
    """Custom type sessionStatusActiveModemModulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("bell103", 2),
          ("bell208", 3),
          ("bell212", 4),
          ("k56", 17),
          ("none", 0),
          ("unknown", 1),
          ("v17", 5),
          ("v21", 6),
          ("v22", 7),
          ("v22bis", 8),
          ("v23", 9),
          ("v27", 10),
          ("v29", 11),
          ("v32", 12),
          ("v32bis", 13),
          ("v33", 14),
          ("v34", 15),
          ("v90", 18),
          ("vFC", 16))
    )


_SessionStatusActiveModemModulation_Type.__name__ = "Integer32"
_SessionStatusActiveModemModulation_Object = MibTableColumn
sessionStatusActiveModemModulation = _SessionStatusActiveModemModulation_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 67),
    _SessionStatusActiveModemModulation_Type()
)
sessionStatusActiveModemModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveModemModulation.setStatus("current")


class _SessionStatusActiveModemErrorCorrection_Type(Integer32):
    """Custom type sessionStatusActiveModemErrorCorrection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mNP", 2),
          ("none", 0),
          ("unknown", 1),
          ("v42", 3))
    )


_SessionStatusActiveModemErrorCorrection_Type.__name__ = "Integer32"
_SessionStatusActiveModemErrorCorrection_Object = MibTableColumn
sessionStatusActiveModemErrorCorrection = _SessionStatusActiveModemErrorCorrection_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 68),
    _SessionStatusActiveModemErrorCorrection_Type()
)
sessionStatusActiveModemErrorCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveModemErrorCorrection.setStatus("current")


class _SessionStatusActiveModemDataCompression_Type(Integer32):
    """Custom type sessionStatusActiveModemDataCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mNP5", 2),
          ("none", 0),
          ("unknown", 1),
          ("v42bis", 3))
    )


_SessionStatusActiveModemDataCompression_Type.__name__ = "Integer32"
_SessionStatusActiveModemDataCompression_Object = MibTableColumn
sessionStatusActiveModemDataCompression = _SessionStatusActiveModemDataCompression_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 69),
    _SessionStatusActiveModemDataCompression_Type()
)
sessionStatusActiveModemDataCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveModemDataCompression.setStatus("current")
_SessionStatusActiveModemTxBlocks_Type = Integer32
_SessionStatusActiveModemTxBlocks_Object = MibTableColumn
sessionStatusActiveModemTxBlocks = _SessionStatusActiveModemTxBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 70),
    _SessionStatusActiveModemTxBlocks_Type()
)
sessionStatusActiveModemTxBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveModemTxBlocks.setStatus("current")
_SessionStatusActiveModemRetransmits_Type = Integer32
_SessionStatusActiveModemRetransmits_Object = MibTableColumn
sessionStatusActiveModemRetransmits = _SessionStatusActiveModemRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 71),
    _SessionStatusActiveModemRetransmits_Type()
)
sessionStatusActiveModemRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveModemRetransmits.setStatus("current")
_SessionStatusActiveModemSNR_Type = Integer32
_SessionStatusActiveModemSNR_Object = MibTableColumn
sessionStatusActiveModemSNR = _SessionStatusActiveModemSNR_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 72),
    _SessionStatusActiveModemSNR_Type()
)
sessionStatusActiveModemSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveModemSNR.setStatus("current")
_SessionStatusActiveModemLocalRetrains_Type = Integer32
_SessionStatusActiveModemLocalRetrains_Object = MibTableColumn
sessionStatusActiveModemLocalRetrains = _SessionStatusActiveModemLocalRetrains_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 73),
    _SessionStatusActiveModemLocalRetrains_Type()
)
sessionStatusActiveModemLocalRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveModemLocalRetrains.setStatus("current")
_SessionStatusActiveModemRemoteRetrains_Type = Integer32
_SessionStatusActiveModemRemoteRetrains_Object = MibTableColumn
sessionStatusActiveModemRemoteRetrains = _SessionStatusActiveModemRemoteRetrains_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 74),
    _SessionStatusActiveModemRemoteRetrains_Type()
)
sessionStatusActiveModemRemoteRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveModemRemoteRetrains.setStatus("current")
_SessionStatusActiveModemLocalRenegotiations_Type = Integer32
_SessionStatusActiveModemLocalRenegotiations_Object = MibTableColumn
sessionStatusActiveModemLocalRenegotiations = _SessionStatusActiveModemLocalRenegotiations_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 75),
    _SessionStatusActiveModemLocalRenegotiations_Type()
)
sessionStatusActiveModemLocalRenegotiations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveModemLocalRenegotiations.setStatus("current")
_SessionStatusActiveModemRemoteRenegotiations_Type = Integer32
_SessionStatusActiveModemRemoteRenegotiations_Object = MibTableColumn
sessionStatusActiveModemRemoteRenegotiations = _SessionStatusActiveModemRemoteRenegotiations_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 76),
    _SessionStatusActiveModemRemoteRenegotiations_Type()
)
sessionStatusActiveModemRemoteRenegotiations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveModemRemoteRenegotiations.setStatus("current")
_SessionStatusActiveModemReceiveLineLevel_Type = Integer32
_SessionStatusActiveModemReceiveLineLevel_Object = MibTableColumn
sessionStatusActiveModemReceiveLineLevel = _SessionStatusActiveModemReceiveLineLevel_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 77),
    _SessionStatusActiveModemReceiveLineLevel_Type()
)
sessionStatusActiveModemReceiveLineLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveModemReceiveLineLevel.setStatus("current")
_SessionStatusActiveRemoteIPXNetwork_Type = Integer32
_SessionStatusActiveRemoteIPXNetwork_Object = MibTableColumn
sessionStatusActiveRemoteIPXNetwork = _SessionStatusActiveRemoteIPXNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 78),
    _SessionStatusActiveRemoteIPXNetwork_Type()
)
sessionStatusActiveRemoteIPXNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveRemoteIPXNetwork.setStatus("current")


class _SessionStatusActiveRemoteIPXNode_Type(DisplayString):
    """Custom type sessionStatusActiveRemoteIPXNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SessionStatusActiveRemoteIPXNode_Type.__name__ = "DisplayString"
_SessionStatusActiveRemoteIPXNode_Object = MibTableColumn
sessionStatusActiveRemoteIPXNode = _SessionStatusActiveRemoteIPXNode_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 79),
    _SessionStatusActiveRemoteIPXNode_Type()
)
sessionStatusActiveRemoteIPXNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveRemoteIPXNode.setStatus("current")
_SessionStatusActiveCleartcpRemoteIP_Type = IpAddress
_SessionStatusActiveCleartcpRemoteIP_Object = MibTableColumn
sessionStatusActiveCleartcpRemoteIP = _SessionStatusActiveCleartcpRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 80),
    _SessionStatusActiveCleartcpRemoteIP_Type()
)
sessionStatusActiveCleartcpRemoteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveCleartcpRemoteIP.setStatus("current")
_SessionStatusActiveCleartcpRemotePort_Type = Integer32
_SessionStatusActiveCleartcpRemotePort_Object = MibTableColumn
sessionStatusActiveCleartcpRemotePort = _SessionStatusActiveCleartcpRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 81),
    _SessionStatusActiveCleartcpRemotePort_Type()
)
sessionStatusActiveCleartcpRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveCleartcpRemotePort.setStatus("current")
_SessionStatusActiveTunnelId_Type = Integer32
_SessionStatusActiveTunnelId_Object = MibTableColumn
sessionStatusActiveTunnelId = _SessionStatusActiveTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 82),
    _SessionStatusActiveTunnelId_Type()
)
sessionStatusActiveTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveTunnelId.setStatus("current")
_SessionStatusActiveLinkId_Type = Integer32
_SessionStatusActiveLinkId_Object = MibTableColumn
sessionStatusActiveLinkId = _SessionStatusActiveLinkId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 102, 1, 83),
    _SessionStatusActiveLinkId_Type()
)
sessionStatusActiveLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusActiveLinkId.setStatus("current")
_SessionStatusInactiveTable_Object = MibTable
sessionStatusInactiveTable = _SessionStatusInactiveTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103)
)
if mibBuilder.loadTexts:
    sessionStatusInactiveTable.setStatus("current")
_SessionStatusInactiveEntry_Object = MibTableRow
sessionStatusInactiveEntry = _SessionStatusInactiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1)
)
sessionStatusInactiveEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "sessionStatusInactiveSessionID"),
)
if mibBuilder.loadTexts:
    sessionStatusInactiveEntry.setStatus("current")
_SessionStatusInactiveSessionID_Type = Integer32
_SessionStatusInactiveSessionID_Object = MibTableColumn
sessionStatusInactiveSessionID = _SessionStatusInactiveSessionID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 2),
    _SessionStatusInactiveSessionID_Type()
)
sessionStatusInactiveSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveSessionID.setStatus("current")


class _SessionStatusInactiveState_Type(Integer32):
    """Custom type sessionStatusInactiveState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_SessionStatusInactiveState_Type.__name__ = "Integer32"
_SessionStatusInactiveState_Object = MibTableColumn
sessionStatusInactiveState = _SessionStatusInactiveState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 3),
    _SessionStatusInactiveState_Type()
)
sessionStatusInactiveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveState.setStatus("current")


class _SessionStatusInactivePermanentFlag_Type(Integer32):
    """Custom type sessionStatusInactivePermanentFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permanent", 2),
          ("switched", 1),
          ("unknown", 0))
    )


_SessionStatusInactivePermanentFlag_Type.__name__ = "Integer32"
_SessionStatusInactivePermanentFlag_Object = MibTableColumn
sessionStatusInactivePermanentFlag = _SessionStatusInactivePermanentFlag_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 10),
    _SessionStatusInactivePermanentFlag_Type()
)
sessionStatusInactivePermanentFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactivePermanentFlag.setStatus("current")
_SessionStatusInactiveVpopId_Type = Integer32
_SessionStatusInactiveVpopId_Object = MibTableColumn
sessionStatusInactiveVpopId = _SessionStatusInactiveVpopId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 11),
    _SessionStatusInactiveVpopId_Type()
)
sessionStatusInactiveVpopId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveVpopId.setStatus("current")


class _SessionStatusInactiveName_Type(DisplayString):
    """Custom type sessionStatusInactiveName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 68),
    )


_SessionStatusInactiveName_Type.__name__ = "DisplayString"
_SessionStatusInactiveName_Object = MibTableColumn
sessionStatusInactiveName = _SessionStatusInactiveName_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 12),
    _SessionStatusInactiveName_Type()
)
sessionStatusInactiveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveName.setStatus("current")
_SessionStatusInactiveRemoteIP_Type = IpAddress
_SessionStatusInactiveRemoteIP_Object = MibTableColumn
sessionStatusInactiveRemoteIP = _SessionStatusInactiveRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 13),
    _SessionStatusInactiveRemoteIP_Type()
)
sessionStatusInactiveRemoteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveRemoteIP.setStatus("current")
_SessionStatusInactiveRemoteIPMask_Type = IpAddress
_SessionStatusInactiveRemoteIPMask_Object = MibTableColumn
sessionStatusInactiveRemoteIPMask = _SessionStatusInactiveRemoteIPMask_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 14),
    _SessionStatusInactiveRemoteIPMask_Type()
)
sessionStatusInactiveRemoteIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveRemoteIPMask.setStatus("current")
_SessionStatusInactiveLocalIP_Type = IpAddress
_SessionStatusInactiveLocalIP_Object = MibTableColumn
sessionStatusInactiveLocalIP = _SessionStatusInactiveLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 15),
    _SessionStatusInactiveLocalIP_Type()
)
sessionStatusInactiveLocalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveLocalIP.setStatus("current")
_SessionStatusInactiveLocalIPMask_Type = IpAddress
_SessionStatusInactiveLocalIPMask_Object = MibTableColumn
sessionStatusInactiveLocalIPMask = _SessionStatusInactiveLocalIPMask_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 16),
    _SessionStatusInactiveLocalIPMask_Type()
)
sessionStatusInactiveLocalIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveLocalIPMask.setStatus("current")


class _SessionStatusInactiveLinkService_Type(Integer32):
    """Custom type sessionStatusInactiveLinkService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 11),
          ("hssi", 14),
          ("hub", 15),
          ("isdn56K", 3),
          ("isdn64K", 4),
          ("isdnV110", 6),
          ("isdnV120", 5),
          ("loopback", 13),
          ("modemK56", 9),
          ("modemV32", 7),
          ("modemV34", 8),
          ("modemV90", 10),
          ("none", 1),
          ("other", 2),
          ("t1Trunk", 12),
          ("unknown", 0),
          ("voice", 16))
    )


_SessionStatusInactiveLinkService_Type.__name__ = "Integer32"
_SessionStatusInactiveLinkService_Object = MibTableColumn
sessionStatusInactiveLinkService = _SessionStatusInactiveLinkService_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 17),
    _SessionStatusInactiveLinkService_Type()
)
sessionStatusInactiveLinkService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveLinkService.setStatus("current")


class _SessionStatusInactiveServiceMode_Type(Integer32):
    """Custom type sessionStatusInactiveServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("atmp", 20),
          ("ciscoHDLC", 6),
          ("dvs", 18),
          ("fax", 19),
          ("frameRelay", 5),
          ("ftp", 17),
          ("hub", 16),
          ("iptest", 21),
          ("l2f", 12),
          ("l2tp", 11),
          ("none", 1),
          ("other", 2),
          ("ppp", 3),
          ("rawTCP", 9),
          ("rlogin", 10),
          ("slip", 4),
          ("tandem", 15),
          ("telnet", 8),
          ("terminalServer", 7),
          ("trunk", 13),
          ("unknown", 0),
          ("voice", 14))
    )


_SessionStatusInactiveServiceMode_Type.__name__ = "Integer32"
_SessionStatusInactiveServiceMode_Object = MibTableColumn
sessionStatusInactiveServiceMode = _SessionStatusInactiveServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 18),
    _SessionStatusInactiveServiceMode_Type()
)
sessionStatusInactiveServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveServiceMode.setStatus("current")
_SessionStatusInactiveStartTime_Type = Integer32
_SessionStatusInactiveStartTime_Object = MibTableColumn
sessionStatusInactiveStartTime = _SessionStatusInactiveStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 19),
    _SessionStatusInactiveStartTime_Type()
)
sessionStatusInactiveStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveStartTime.setStatus("current")
_SessionStatusInactiveStopTime_Type = Integer32
_SessionStatusInactiveStopTime_Object = MibTableColumn
sessionStatusInactiveStopTime = _SessionStatusInactiveStopTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 20),
    _SessionStatusInactiveStopTime_Type()
)
sessionStatusInactiveStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveStopTime.setStatus("current")
_SessionStatusInactiveTimeOfModemSync_Type = Integer32
_SessionStatusInactiveTimeOfModemSync_Object = MibTableColumn
sessionStatusInactiveTimeOfModemSync = _SessionStatusInactiveTimeOfModemSync_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 21),
    _SessionStatusInactiveTimeOfModemSync_Type()
)
sessionStatusInactiveTimeOfModemSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveTimeOfModemSync.setStatus("current")
_SessionStatusInactiveTimeOfService_Type = Integer32
_SessionStatusInactiveTimeOfService_Object = MibTableColumn
sessionStatusInactiveTimeOfService = _SessionStatusInactiveTimeOfService_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 22),
    _SessionStatusInactiveTimeOfService_Type()
)
sessionStatusInactiveTimeOfService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveTimeOfService.setStatus("current")


class _SessionStatusInactiveTerminatingComponent_Type(Integer32):
    """Custom type sessionStatusInactiveTerminatingComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("atmp", 32),
          ("atmptunnel", 33),
          ("chdlc", 9),
          ("cleartcp", 13),
          ("df", 3),
          ("ds0", 4),
          ("dvs", 28),
          ("dvstunnel", 29),
          ("ether", 15),
          ("fax", 30),
          ("fepdf", 17),
          ("fr", 10),
          ("hdlc", 6),
          ("hssi", 22),
          ("ip", 11),
          ("iptest", 34),
          ("l2f", 26),
          ("l2ftunnel", 27),
          ("l2tp", 14),
          ("l2tproute", 31),
          ("lineip", 18),
          ("loopback", 19),
          ("modem", 5),
          ("none", 1),
          ("other", 2),
          ("ppp", 7),
          ("rlogin", 21),
          ("shell", 20),
          ("slip", 8),
          ("sm", 23),
          ("telnet", 12),
          ("trunkip", 16),
          ("unknown", 0),
          ("vl", 24),
          ("voip", 25))
    )


_SessionStatusInactiveTerminatingComponent_Type.__name__ = "Integer32"
_SessionStatusInactiveTerminatingComponent_Object = MibTableColumn
sessionStatusInactiveTerminatingComponent = _SessionStatusInactiveTerminatingComponent_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 23),
    _SessionStatusInactiveTerminatingComponent_Type()
)
sessionStatusInactiveTerminatingComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveTerminatingComponent.setStatus("current")
_SessionStatusInactiveTerminationCause_Type = Integer32
_SessionStatusInactiveTerminationCause_Object = MibTableColumn
sessionStatusInactiveTerminationCause = _SessionStatusInactiveTerminationCause_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 24),
    _SessionStatusInactiveTerminationCause_Type()
)
sessionStatusInactiveTerminationCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveTerminationCause.setStatus("current")


class _SessionStatusInactiveLastComponent_Type(Integer32):
    """Custom type sessionStatusInactiveLastComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("atmp", 32),
          ("atmptunnel", 33),
          ("chdlc", 9),
          ("cleartcp", 13),
          ("df", 3),
          ("ds0", 4),
          ("dvs", 28),
          ("dvstunnel", 29),
          ("ether", 15),
          ("fax", 30),
          ("fepdf", 17),
          ("fr", 10),
          ("hdlc", 6),
          ("hssi", 22),
          ("ip", 11),
          ("iptest", 34),
          ("l2f", 26),
          ("l2ftunnel", 27),
          ("l2tp", 14),
          ("l2tproute", 31),
          ("lineip", 18),
          ("loopback", 19),
          ("modem", 5),
          ("none", 1),
          ("other", 2),
          ("ppp", 7),
          ("rlogin", 21),
          ("shell", 20),
          ("slip", 8),
          ("sm", 23),
          ("telnet", 12),
          ("trunkip", 16),
          ("unknown", 0),
          ("vl", 24),
          ("voip", 25))
    )


_SessionStatusInactiveLastComponent_Type.__name__ = "Integer32"
_SessionStatusInactiveLastComponent_Object = MibTableColumn
sessionStatusInactiveLastComponent = _SessionStatusInactiveLastComponent_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 25),
    _SessionStatusInactiveLastComponent_Type()
)
sessionStatusInactiveLastComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveLastComponent.setStatus("current")


class _SessionStatusInactiveLayer1Slot_Type(Integer32):
    """Custom type sessionStatusInactiveLayer1Slot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_SessionStatusInactiveLayer1Slot_Type.__name__ = "Integer32"
_SessionStatusInactiveLayer1Slot_Object = MibTableColumn
sessionStatusInactiveLayer1Slot = _SessionStatusInactiveLayer1Slot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 26),
    _SessionStatusInactiveLayer1Slot_Type()
)
sessionStatusInactiveLayer1Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveLayer1Slot.setStatus("current")


class _SessionStatusInactiveLayer2Slot_Type(Integer32):
    """Custom type sessionStatusInactiveLayer2Slot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_SessionStatusInactiveLayer2Slot_Type.__name__ = "Integer32"
_SessionStatusInactiveLayer2Slot_Object = MibTableColumn
sessionStatusInactiveLayer2Slot = _SessionStatusInactiveLayer2Slot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 27),
    _SessionStatusInactiveLayer2Slot_Type()
)
sessionStatusInactiveLayer2Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveLayer2Slot.setStatus("current")


class _SessionStatusInactiveCalledNumber_Type(DisplayString):
    """Custom type sessionStatusInactiveCalledNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SessionStatusInactiveCalledNumber_Type.__name__ = "DisplayString"
_SessionStatusInactiveCalledNumber_Object = MibTableColumn
sessionStatusInactiveCalledNumber = _SessionStatusInactiveCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 28),
    _SessionStatusInactiveCalledNumber_Type()
)
sessionStatusInactiveCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveCalledNumber.setStatus("current")


class _SessionStatusInactiveCallingNumber_Type(DisplayString):
    """Custom type sessionStatusInactiveCallingNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SessionStatusInactiveCallingNumber_Type.__name__ = "DisplayString"
_SessionStatusInactiveCallingNumber_Object = MibTableColumn
sessionStatusInactiveCallingNumber = _SessionStatusInactiveCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 29),
    _SessionStatusInactiveCallingNumber_Type()
)
sessionStatusInactiveCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveCallingNumber.setStatus("current")


class _SessionStatusInactiveOriginateMode_Type(Integer32):
    """Custom type sessionStatusInactiveOriginateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("answer", 0),
          ("originate", 1))
    )


_SessionStatusInactiveOriginateMode_Type.__name__ = "Integer32"
_SessionStatusInactiveOriginateMode_Object = MibTableColumn
sessionStatusInactiveOriginateMode = _SessionStatusInactiveOriginateMode_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 30),
    _SessionStatusInactiveOriginateMode_Type()
)
sessionStatusInactiveOriginateMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveOriginateMode.setStatus("current")
_SessionStatusInactiveOctetsIn_Type = Integer32
_SessionStatusInactiveOctetsIn_Object = MibTableColumn
sessionStatusInactiveOctetsIn = _SessionStatusInactiveOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 31),
    _SessionStatusInactiveOctetsIn_Type()
)
sessionStatusInactiveOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveOctetsIn.setStatus("current")
_SessionStatusInactiveOctetsOut_Type = Integer32
_SessionStatusInactiveOctetsOut_Object = MibTableColumn
sessionStatusInactiveOctetsOut = _SessionStatusInactiveOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 32),
    _SessionStatusInactiveOctetsOut_Type()
)
sessionStatusInactiveOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveOctetsOut.setStatus("current")
_SessionStatusInactivePacketsIn_Type = Integer32
_SessionStatusInactivePacketsIn_Object = MibTableColumn
sessionStatusInactivePacketsIn = _SessionStatusInactivePacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 33),
    _SessionStatusInactivePacketsIn_Type()
)
sessionStatusInactivePacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactivePacketsIn.setStatus("current")
_SessionStatusInactivePacketsOut_Type = Integer32
_SessionStatusInactivePacketsOut_Object = MibTableColumn
sessionStatusInactivePacketsOut = _SessionStatusInactivePacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 34),
    _SessionStatusInactivePacketsOut_Type()
)
sessionStatusInactivePacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactivePacketsOut.setStatus("current")
_SessionStatusInactiveMultiLinkId_Type = Integer32
_SessionStatusInactiveMultiLinkId_Object = MibTableColumn
sessionStatusInactiveMultiLinkId = _SessionStatusInactiveMultiLinkId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 35),
    _SessionStatusInactiveMultiLinkId_Type()
)
sessionStatusInactiveMultiLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveMultiLinkId.setStatus("current")
_SessionStatusInactivePort_Type = Integer32
_SessionStatusInactivePort_Object = MibTableColumn
sessionStatusInactivePort = _SessionStatusInactivePort_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 36),
    _SessionStatusInactivePort_Type()
)
sessionStatusInactivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactivePort.setStatus("current")
_SessionStatusInactiveTimeslot_Type = Integer32
_SessionStatusInactiveTimeslot_Object = MibTableColumn
sessionStatusInactiveTimeslot = _SessionStatusInactiveTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 37),
    _SessionStatusInactiveTimeslot_Type()
)
sessionStatusInactiveTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveTimeslot.setStatus("current")
_SessionStatusInactiveLinkCount_Type = Integer32
_SessionStatusInactiveLinkCount_Object = MibTableColumn
sessionStatusInactiveLinkCount = _SessionStatusInactiveLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 38),
    _SessionStatusInactiveLinkCount_Type()
)
sessionStatusInactiveLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveLinkCount.setStatus("current")
_SessionStatusInactiveTxStartDataRate_Type = Integer32
_SessionStatusInactiveTxStartDataRate_Object = MibTableColumn
sessionStatusInactiveTxStartDataRate = _SessionStatusInactiveTxStartDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 39),
    _SessionStatusInactiveTxStartDataRate_Type()
)
sessionStatusInactiveTxStartDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveTxStartDataRate.setStatus("current")
_SessionStatusInactiveRxStartDataRate_Type = Integer32
_SessionStatusInactiveRxStartDataRate_Object = MibTableColumn
sessionStatusInactiveRxStartDataRate = _SessionStatusInactiveRxStartDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 40),
    _SessionStatusInactiveRxStartDataRate_Type()
)
sessionStatusInactiveRxStartDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveRxStartDataRate.setStatus("current")
_SessionStatusInactiveTxEndDataRate_Type = Integer32
_SessionStatusInactiveTxEndDataRate_Object = MibTableColumn
sessionStatusInactiveTxEndDataRate = _SessionStatusInactiveTxEndDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 41),
    _SessionStatusInactiveTxEndDataRate_Type()
)
sessionStatusInactiveTxEndDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveTxEndDataRate.setStatus("current")
_SessionStatusInactiveRxEndDataRate_Type = Integer32
_SessionStatusInactiveRxEndDataRate_Object = MibTableColumn
sessionStatusInactiveRxEndDataRate = _SessionStatusInactiveRxEndDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 42),
    _SessionStatusInactiveRxEndDataRate_Type()
)
sessionStatusInactiveRxEndDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveRxEndDataRate.setStatus("current")
_SessionStatusInactiveTxMinDataRate_Type = Integer32
_SessionStatusInactiveTxMinDataRate_Object = MibTableColumn
sessionStatusInactiveTxMinDataRate = _SessionStatusInactiveTxMinDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 43),
    _SessionStatusInactiveTxMinDataRate_Type()
)
sessionStatusInactiveTxMinDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveTxMinDataRate.setStatus("current")
_SessionStatusInactiveRxMinDataRate_Type = Integer32
_SessionStatusInactiveRxMinDataRate_Object = MibTableColumn
sessionStatusInactiveRxMinDataRate = _SessionStatusInactiveRxMinDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 44),
    _SessionStatusInactiveRxMinDataRate_Type()
)
sessionStatusInactiveRxMinDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveRxMinDataRate.setStatus("current")
_SessionStatusInactiveTxMaxDataRate_Type = Integer32
_SessionStatusInactiveTxMaxDataRate_Object = MibTableColumn
sessionStatusInactiveTxMaxDataRate = _SessionStatusInactiveTxMaxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 45),
    _SessionStatusInactiveTxMaxDataRate_Type()
)
sessionStatusInactiveTxMaxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveTxMaxDataRate.setStatus("current")
_SessionStatusInactiveRxMaxDataRate_Type = Integer32
_SessionStatusInactiveRxMaxDataRate_Object = MibTableColumn
sessionStatusInactiveRxMaxDataRate = _SessionStatusInactiveRxMaxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 46),
    _SessionStatusInactiveRxMaxDataRate_Type()
)
sessionStatusInactiveRxMaxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveRxMaxDataRate.setStatus("current")
_SessionStatusInactiveIop_Type = Integer32
_SessionStatusInactiveIop_Object = MibTableColumn
sessionStatusInactiveIop = _SessionStatusInactiveIop_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 47),
    _SessionStatusInactiveIop_Type()
)
sessionStatusInactiveIop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveIop.setStatus("current")
_SessionStatusInactiveDmm_Type = Integer32
_SessionStatusInactiveDmm_Object = MibTableColumn
sessionStatusInactiveDmm = _SessionStatusInactiveDmm_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 48),
    _SessionStatusInactiveDmm_Type()
)
sessionStatusInactiveDmm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveDmm.setStatus("current")
_SessionStatusInactivePack_Type = Integer32
_SessionStatusInactivePack_Object = MibTableColumn
sessionStatusInactivePack = _SessionStatusInactivePack_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 49),
    _SessionStatusInactivePack_Type()
)
sessionStatusInactivePack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactivePack.setStatus("current")
_SessionStatusInactiveDevice_Type = Integer32
_SessionStatusInactiveDevice_Object = MibTableColumn
sessionStatusInactiveDevice = _SessionStatusInactiveDevice_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 50),
    _SessionStatusInactiveDevice_Type()
)
sessionStatusInactiveDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveDevice.setStatus("current")
_SessionStatusInactiveTdmStream_Type = Integer32
_SessionStatusInactiveTdmStream_Object = MibTableColumn
sessionStatusInactiveTdmStream = _SessionStatusInactiveTdmStream_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 51),
    _SessionStatusInactiveTdmStream_Type()
)
sessionStatusInactiveTdmStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveTdmStream.setStatus("current")
_SessionStatusInactiveTdmTimeSlot_Type = Integer32
_SessionStatusInactiveTdmTimeSlot_Object = MibTableColumn
sessionStatusInactiveTdmTimeSlot = _SessionStatusInactiveTdmTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 52),
    _SessionStatusInactiveTdmTimeSlot_Type()
)
sessionStatusInactiveTdmTimeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveTdmTimeSlot.setStatus("current")


class _SessionStatusInactiveTerminationReason_Type(DisplayString):
    """Custom type sessionStatusInactiveTerminationReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SessionStatusInactiveTerminationReason_Type.__name__ = "DisplayString"
_SessionStatusInactiveTerminationReason_Object = MibTableColumn
sessionStatusInactiveTerminationReason = _SessionStatusInactiveTerminationReason_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 53),
    _SessionStatusInactiveTerminationReason_Type()
)
sessionStatusInactiveTerminationReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveTerminationReason.setStatus("current")
_SessionStatusInactiveDuration_Type = Integer32
_SessionStatusInactiveDuration_Object = MibTableColumn
sessionStatusInactiveDuration = _SessionStatusInactiveDuration_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 54),
    _SessionStatusInactiveDuration_Type()
)
sessionStatusInactiveDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveDuration.setStatus("current")


class _SessionStatusInactiveDurationHMS_Type(DisplayString):
    """Custom type sessionStatusInactiveDurationHMS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SessionStatusInactiveDurationHMS_Type.__name__ = "DisplayString"
_SessionStatusInactiveDurationHMS_Object = MibTableColumn
sessionStatusInactiveDurationHMS = _SessionStatusInactiveDurationHMS_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 55),
    _SessionStatusInactiveDurationHMS_Type()
)
sessionStatusInactiveDurationHMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveDurationHMS.setStatus("current")


class _SessionStatusInactiveSs7SessionId_Type(DisplayString):
    """Custom type sessionStatusInactiveSs7SessionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 41),
    )


_SessionStatusInactiveSs7SessionId_Type.__name__ = "DisplayString"
_SessionStatusInactiveSs7SessionId_Object = MibTableColumn
sessionStatusInactiveSs7SessionId = _SessionStatusInactiveSs7SessionId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 56),
    _SessionStatusInactiveSs7SessionId_Type()
)
sessionStatusInactiveSs7SessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveSs7SessionId.setStatus("current")
_SessionStatusInactiveModemNumber_Type = Integer32
_SessionStatusInactiveModemNumber_Object = MibTableColumn
sessionStatusInactiveModemNumber = _SessionStatusInactiveModemNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 57),
    _SessionStatusInactiveModemNumber_Type()
)
sessionStatusInactiveModemNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveModemNumber.setStatus("current")


class _SessionStatusInactiveTunnelType_Type(Integer32):
    """Custom type sessionStatusInactiveTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("atmp", 6),
          ("dvs", 5),
          ("l2f", 3),
          ("l2tp", 4),
          ("none", 1),
          ("other", 2),
          ("unknown", 0))
    )


_SessionStatusInactiveTunnelType_Type.__name__ = "Integer32"
_SessionStatusInactiveTunnelType_Object = MibTableColumn
sessionStatusInactiveTunnelType = _SessionStatusInactiveTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 58),
    _SessionStatusInactiveTunnelType_Type()
)
sessionStatusInactiveTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveTunnelType.setStatus("current")


class _SessionStatusInactiveTunnelMediumType_Type(Integer32):
    """Custom type sessionStatusInactiveTunnelMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 3),
          ("none", 1),
          ("other", 2),
          ("unknown", 0))
    )


_SessionStatusInactiveTunnelMediumType_Type.__name__ = "Integer32"
_SessionStatusInactiveTunnelMediumType_Object = MibTableColumn
sessionStatusInactiveTunnelMediumType = _SessionStatusInactiveTunnelMediumType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 59),
    _SessionStatusInactiveTunnelMediumType_Type()
)
sessionStatusInactiveTunnelMediumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveTunnelMediumType.setStatus("current")
_SessionStatusInactiveTunnelServerAddress_Type = IpAddress
_SessionStatusInactiveTunnelServerAddress_Object = MibTableColumn
sessionStatusInactiveTunnelServerAddress = _SessionStatusInactiveTunnelServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 60),
    _SessionStatusInactiveTunnelServerAddress_Type()
)
sessionStatusInactiveTunnelServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveTunnelServerAddress.setStatus("current")
_SessionStatusInactiveCallClass_Type = Integer32
_SessionStatusInactiveCallClass_Object = MibTableColumn
sessionStatusInactiveCallClass = _SessionStatusInactiveCallClass_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 61),
    _SessionStatusInactiveCallClass_Type()
)
sessionStatusInactiveCallClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveCallClass.setStatus("current")
_SessionStatusInactiveTandemPort_Type = Integer32
_SessionStatusInactiveTandemPort_Object = MibTableColumn
sessionStatusInactiveTandemPort = _SessionStatusInactiveTandemPort_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 62),
    _SessionStatusInactiveTandemPort_Type()
)
sessionStatusInactiveTandemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveTandemPort.setStatus("current")
_SessionStatusInactiveTandemTimeslot_Type = Integer32
_SessionStatusInactiveTandemTimeslot_Object = MibTableColumn
sessionStatusInactiveTandemTimeslot = _SessionStatusInactiveTandemTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 63),
    _SessionStatusInactiveTandemTimeslot_Type()
)
sessionStatusInactiveTandemTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveTandemTimeslot.setStatus("current")


class _SessionStatusInactiveCallClassArray_Type(OctetString):
    """Custom type sessionStatusInactiveCallClassArray based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SessionStatusInactiveCallClassArray_Type.__name__ = "OctetString"
_SessionStatusInactiveCallClassArray_Object = MibTableColumn
sessionStatusInactiveCallClassArray = _SessionStatusInactiveCallClassArray_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 64),
    _SessionStatusInactiveCallClassArray_Type()
)
sessionStatusInactiveCallClassArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveCallClassArray.setStatus("current")
_SessionStatusInactiveCallClassLen_Type = Integer32
_SessionStatusInactiveCallClassLen_Object = MibTableColumn
sessionStatusInactiveCallClassLen = _SessionStatusInactiveCallClassLen_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 65),
    _SessionStatusInactiveCallClassLen_Type()
)
sessionStatusInactiveCallClassLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveCallClassLen.setStatus("current")


class _SessionStatusInactiveActualAuthMethod_Type(Integer32):
    """Custom type sessionStatusInactiveActualAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("radius", 1),
          ("remote", 3))
    )


_SessionStatusInactiveActualAuthMethod_Type.__name__ = "Integer32"
_SessionStatusInactiveActualAuthMethod_Object = MibTableColumn
sessionStatusInactiveActualAuthMethod = _SessionStatusInactiveActualAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 66),
    _SessionStatusInactiveActualAuthMethod_Type()
)
sessionStatusInactiveActualAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveActualAuthMethod.setStatus("current")


class _SessionStatusInactiveModemModulation_Type(Integer32):
    """Custom type sessionStatusInactiveModemModulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("bell103", 2),
          ("bell208", 3),
          ("bell212", 4),
          ("k56", 17),
          ("none", 0),
          ("unknown", 1),
          ("v17", 5),
          ("v21", 6),
          ("v22", 7),
          ("v22bis", 8),
          ("v23", 9),
          ("v27", 10),
          ("v29", 11),
          ("v32", 12),
          ("v32bis", 13),
          ("v33", 14),
          ("v34", 15),
          ("v90", 18),
          ("vFC", 16))
    )


_SessionStatusInactiveModemModulation_Type.__name__ = "Integer32"
_SessionStatusInactiveModemModulation_Object = MibTableColumn
sessionStatusInactiveModemModulation = _SessionStatusInactiveModemModulation_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 67),
    _SessionStatusInactiveModemModulation_Type()
)
sessionStatusInactiveModemModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveModemModulation.setStatus("current")


class _SessionStatusInactiveModemErrorCorrection_Type(Integer32):
    """Custom type sessionStatusInactiveModemErrorCorrection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mNP", 2),
          ("none", 0),
          ("unknown", 1),
          ("v42", 3))
    )


_SessionStatusInactiveModemErrorCorrection_Type.__name__ = "Integer32"
_SessionStatusInactiveModemErrorCorrection_Object = MibTableColumn
sessionStatusInactiveModemErrorCorrection = _SessionStatusInactiveModemErrorCorrection_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 68),
    _SessionStatusInactiveModemErrorCorrection_Type()
)
sessionStatusInactiveModemErrorCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveModemErrorCorrection.setStatus("current")


class _SessionStatusInactiveModemDataCompression_Type(Integer32):
    """Custom type sessionStatusInactiveModemDataCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mNP5", 2),
          ("none", 0),
          ("unknown", 1),
          ("v42bis", 3))
    )


_SessionStatusInactiveModemDataCompression_Type.__name__ = "Integer32"
_SessionStatusInactiveModemDataCompression_Object = MibTableColumn
sessionStatusInactiveModemDataCompression = _SessionStatusInactiveModemDataCompression_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 69),
    _SessionStatusInactiveModemDataCompression_Type()
)
sessionStatusInactiveModemDataCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveModemDataCompression.setStatus("current")
_SessionStatusInactiveModemTxBlocks_Type = Integer32
_SessionStatusInactiveModemTxBlocks_Object = MibTableColumn
sessionStatusInactiveModemTxBlocks = _SessionStatusInactiveModemTxBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 70),
    _SessionStatusInactiveModemTxBlocks_Type()
)
sessionStatusInactiveModemTxBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveModemTxBlocks.setStatus("current")
_SessionStatusInactiveModemRetransmits_Type = Integer32
_SessionStatusInactiveModemRetransmits_Object = MibTableColumn
sessionStatusInactiveModemRetransmits = _SessionStatusInactiveModemRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 71),
    _SessionStatusInactiveModemRetransmits_Type()
)
sessionStatusInactiveModemRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveModemRetransmits.setStatus("current")
_SessionStatusInactiveModemSNR_Type = Integer32
_SessionStatusInactiveModemSNR_Object = MibTableColumn
sessionStatusInactiveModemSNR = _SessionStatusInactiveModemSNR_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 72),
    _SessionStatusInactiveModemSNR_Type()
)
sessionStatusInactiveModemSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveModemSNR.setStatus("current")
_SessionStatusInactiveModemLocalRetrains_Type = Integer32
_SessionStatusInactiveModemLocalRetrains_Object = MibTableColumn
sessionStatusInactiveModemLocalRetrains = _SessionStatusInactiveModemLocalRetrains_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 73),
    _SessionStatusInactiveModemLocalRetrains_Type()
)
sessionStatusInactiveModemLocalRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveModemLocalRetrains.setStatus("current")
_SessionStatusInactiveModemRemoteRetrains_Type = Integer32
_SessionStatusInactiveModemRemoteRetrains_Object = MibTableColumn
sessionStatusInactiveModemRemoteRetrains = _SessionStatusInactiveModemRemoteRetrains_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 74),
    _SessionStatusInactiveModemRemoteRetrains_Type()
)
sessionStatusInactiveModemRemoteRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveModemRemoteRetrains.setStatus("current")
_SessionStatusInactiveModemLocalRenegotiations_Type = Integer32
_SessionStatusInactiveModemLocalRenegotiations_Object = MibTableColumn
sessionStatusInactiveModemLocalRenegotiations = _SessionStatusInactiveModemLocalRenegotiations_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 75),
    _SessionStatusInactiveModemLocalRenegotiations_Type()
)
sessionStatusInactiveModemLocalRenegotiations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveModemLocalRenegotiations.setStatus("current")
_SessionStatusInactiveModemRemoteRenegotiations_Type = Integer32
_SessionStatusInactiveModemRemoteRenegotiations_Object = MibTableColumn
sessionStatusInactiveModemRemoteRenegotiations = _SessionStatusInactiveModemRemoteRenegotiations_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 76),
    _SessionStatusInactiveModemRemoteRenegotiations_Type()
)
sessionStatusInactiveModemRemoteRenegotiations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveModemRemoteRenegotiations.setStatus("current")
_SessionStatusInactiveModemReceiveLineLevel_Type = Integer32
_SessionStatusInactiveModemReceiveLineLevel_Object = MibTableColumn
sessionStatusInactiveModemReceiveLineLevel = _SessionStatusInactiveModemReceiveLineLevel_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 77),
    _SessionStatusInactiveModemReceiveLineLevel_Type()
)
sessionStatusInactiveModemReceiveLineLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveModemReceiveLineLevel.setStatus("current")
_SessionStatusInactiveRemoteIPXNetwork_Type = Integer32
_SessionStatusInactiveRemoteIPXNetwork_Object = MibTableColumn
sessionStatusInactiveRemoteIPXNetwork = _SessionStatusInactiveRemoteIPXNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 78),
    _SessionStatusInactiveRemoteIPXNetwork_Type()
)
sessionStatusInactiveRemoteIPXNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveRemoteIPXNetwork.setStatus("current")


class _SessionStatusInactiveRemoteIPXNode_Type(DisplayString):
    """Custom type sessionStatusInactiveRemoteIPXNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SessionStatusInactiveRemoteIPXNode_Type.__name__ = "DisplayString"
_SessionStatusInactiveRemoteIPXNode_Object = MibTableColumn
sessionStatusInactiveRemoteIPXNode = _SessionStatusInactiveRemoteIPXNode_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 79),
    _SessionStatusInactiveRemoteIPXNode_Type()
)
sessionStatusInactiveRemoteIPXNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveRemoteIPXNode.setStatus("current")
_SessionStatusInactiveCleartcpRemoteIP_Type = IpAddress
_SessionStatusInactiveCleartcpRemoteIP_Object = MibTableColumn
sessionStatusInactiveCleartcpRemoteIP = _SessionStatusInactiveCleartcpRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 80),
    _SessionStatusInactiveCleartcpRemoteIP_Type()
)
sessionStatusInactiveCleartcpRemoteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveCleartcpRemoteIP.setStatus("current")
_SessionStatusInactiveCleartcpRemotePort_Type = Integer32
_SessionStatusInactiveCleartcpRemotePort_Object = MibTableColumn
sessionStatusInactiveCleartcpRemotePort = _SessionStatusInactiveCleartcpRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 81),
    _SessionStatusInactiveCleartcpRemotePort_Type()
)
sessionStatusInactiveCleartcpRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveCleartcpRemotePort.setStatus("current")
_SessionStatusInactiveTunnelId_Type = Integer32
_SessionStatusInactiveTunnelId_Object = MibTableColumn
sessionStatusInactiveTunnelId = _SessionStatusInactiveTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 82),
    _SessionStatusInactiveTunnelId_Type()
)
sessionStatusInactiveTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveTunnelId.setStatus("current")
_SessionStatusInactiveLinkId_Type = Integer32
_SessionStatusInactiveLinkId_Object = MibTableColumn
sessionStatusInactiveLinkId = _SessionStatusInactiveLinkId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 103, 1, 83),
    _SessionStatusInactiveLinkId_Type()
)
sessionStatusInactiveLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusInactiveLinkId.setStatus("current")
_SessionDiscCauseTable_Object = MibTable
sessionDiscCauseTable = _SessionDiscCauseTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 104)
)
if mibBuilder.loadTexts:
    sessionDiscCauseTable.setStatus("current")
_SessionDiscCauseEntry_Object = MibTableRow
sessionDiscCauseEntry = _SessionDiscCauseEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 104, 1)
)
sessionDiscCauseEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "sessionDiscCauseIndex"),
)
if mibBuilder.loadTexts:
    sessionDiscCauseEntry.setStatus("current")
_SessionDiscCauseIndex_Type = Integer32
_SessionDiscCauseIndex_Object = MibTableColumn
sessionDiscCauseIndex = _SessionDiscCauseIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 104, 1, 1),
    _SessionDiscCauseIndex_Type()
)
sessionDiscCauseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionDiscCauseIndex.setStatus("current")


class _SessionDiscCauseComponent_Type(Integer32):
    """Custom type sessionDiscCauseComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("atmp", 32),
          ("atmptunnel", 33),
          ("chdlc", 9),
          ("cleartcp", 13),
          ("df", 3),
          ("ds0", 4),
          ("dvs", 28),
          ("dvstunnel", 29),
          ("ether", 15),
          ("fax", 30),
          ("fepdf", 17),
          ("fr", 10),
          ("hdlc", 6),
          ("hssi", 22),
          ("ip", 11),
          ("iptest", 34),
          ("l2f", 26),
          ("l2ftunnel", 27),
          ("l2tp", 14),
          ("l2tproute", 31),
          ("lineip", 18),
          ("loopback", 19),
          ("modem", 5),
          ("none", 1),
          ("other", 2),
          ("ppp", 7),
          ("rlogin", 21),
          ("shell", 20),
          ("slip", 8),
          ("sm", 23),
          ("telnet", 12),
          ("trunkip", 16),
          ("unknown", 0),
          ("vl", 24),
          ("voip", 25))
    )


_SessionDiscCauseComponent_Type.__name__ = "Integer32"
_SessionDiscCauseComponent_Object = MibTableColumn
sessionDiscCauseComponent = _SessionDiscCauseComponent_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 104, 1, 2),
    _SessionDiscCauseComponent_Type()
)
sessionDiscCauseComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionDiscCauseComponent.setStatus("current")
_SessionDiscCauseCause_Type = Integer32
_SessionDiscCauseCause_Object = MibTableColumn
sessionDiscCauseCause = _SessionDiscCauseCause_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 104, 1, 3),
    _SessionDiscCauseCause_Type()
)
sessionDiscCauseCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionDiscCauseCause.setStatus("current")


class _SessionDiscCauseReason_Type(DisplayString):
    """Custom type sessionDiscCauseReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SessionDiscCauseReason_Type.__name__ = "DisplayString"
_SessionDiscCauseReason_Object = MibTableColumn
sessionDiscCauseReason = _SessionDiscCauseReason_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 104, 1, 4),
    _SessionDiscCauseReason_Type()
)
sessionDiscCauseReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionDiscCauseReason.setStatus("current")
_SessionDiscCauseCount_Type = Integer32
_SessionDiscCauseCount_Object = MibTableColumn
sessionDiscCauseCount = _SessionDiscCauseCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 104, 1, 5),
    _SessionDiscCauseCount_Type()
)
sessionDiscCauseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionDiscCauseCount.setStatus("current")
_SessionStatusReverseTable_Object = MibTable
sessionStatusReverseTable = _SessionStatusReverseTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106)
)
if mibBuilder.loadTexts:
    sessionStatusReverseTable.setStatus("current")
_SessionStatusReverseEntry_Object = MibTableRow
sessionStatusReverseEntry = _SessionStatusReverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1)
)
sessionStatusReverseEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "sessionStatusReverseSessionID"),
)
if mibBuilder.loadTexts:
    sessionStatusReverseEntry.setStatus("current")
_SessionStatusReverseSessionID_Type = Integer32
_SessionStatusReverseSessionID_Object = MibTableColumn
sessionStatusReverseSessionID = _SessionStatusReverseSessionID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 2),
    _SessionStatusReverseSessionID_Type()
)
sessionStatusReverseSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseSessionID.setStatus("current")


class _SessionStatusReverseState_Type(Integer32):
    """Custom type sessionStatusReverseState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_SessionStatusReverseState_Type.__name__ = "Integer32"
_SessionStatusReverseState_Object = MibTableColumn
sessionStatusReverseState = _SessionStatusReverseState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 3),
    _SessionStatusReverseState_Type()
)
sessionStatusReverseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseState.setStatus("current")


class _SessionStatusReversePermanentFlag_Type(Integer32):
    """Custom type sessionStatusReversePermanentFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permanent", 2),
          ("switched", 1),
          ("unknown", 0))
    )


_SessionStatusReversePermanentFlag_Type.__name__ = "Integer32"
_SessionStatusReversePermanentFlag_Object = MibTableColumn
sessionStatusReversePermanentFlag = _SessionStatusReversePermanentFlag_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 10),
    _SessionStatusReversePermanentFlag_Type()
)
sessionStatusReversePermanentFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReversePermanentFlag.setStatus("current")
_SessionStatusReverseVpopId_Type = Integer32
_SessionStatusReverseVpopId_Object = MibTableColumn
sessionStatusReverseVpopId = _SessionStatusReverseVpopId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 11),
    _SessionStatusReverseVpopId_Type()
)
sessionStatusReverseVpopId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseVpopId.setStatus("current")


class _SessionStatusReverseName_Type(DisplayString):
    """Custom type sessionStatusReverseName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 68),
    )


_SessionStatusReverseName_Type.__name__ = "DisplayString"
_SessionStatusReverseName_Object = MibTableColumn
sessionStatusReverseName = _SessionStatusReverseName_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 12),
    _SessionStatusReverseName_Type()
)
sessionStatusReverseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseName.setStatus("current")
_SessionStatusReverseRemoteIP_Type = IpAddress
_SessionStatusReverseRemoteIP_Object = MibTableColumn
sessionStatusReverseRemoteIP = _SessionStatusReverseRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 13),
    _SessionStatusReverseRemoteIP_Type()
)
sessionStatusReverseRemoteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseRemoteIP.setStatus("current")
_SessionStatusReverseRemoteIPMask_Type = IpAddress
_SessionStatusReverseRemoteIPMask_Object = MibTableColumn
sessionStatusReverseRemoteIPMask = _SessionStatusReverseRemoteIPMask_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 14),
    _SessionStatusReverseRemoteIPMask_Type()
)
sessionStatusReverseRemoteIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseRemoteIPMask.setStatus("current")
_SessionStatusReverseLocalIP_Type = IpAddress
_SessionStatusReverseLocalIP_Object = MibTableColumn
sessionStatusReverseLocalIP = _SessionStatusReverseLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 15),
    _SessionStatusReverseLocalIP_Type()
)
sessionStatusReverseLocalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseLocalIP.setStatus("current")
_SessionStatusReverseLocalIPMask_Type = IpAddress
_SessionStatusReverseLocalIPMask_Object = MibTableColumn
sessionStatusReverseLocalIPMask = _SessionStatusReverseLocalIPMask_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 16),
    _SessionStatusReverseLocalIPMask_Type()
)
sessionStatusReverseLocalIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseLocalIPMask.setStatus("current")


class _SessionStatusReverseLinkService_Type(Integer32):
    """Custom type sessionStatusReverseLinkService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 11),
          ("hssi", 14),
          ("hub", 15),
          ("isdn56K", 3),
          ("isdn64K", 4),
          ("isdnV110", 6),
          ("isdnV120", 5),
          ("loopback", 13),
          ("modemK56", 9),
          ("modemV32", 7),
          ("modemV34", 8),
          ("modemV90", 10),
          ("none", 1),
          ("other", 2),
          ("t1Trunk", 12),
          ("unknown", 0),
          ("voice", 16))
    )


_SessionStatusReverseLinkService_Type.__name__ = "Integer32"
_SessionStatusReverseLinkService_Object = MibTableColumn
sessionStatusReverseLinkService = _SessionStatusReverseLinkService_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 17),
    _SessionStatusReverseLinkService_Type()
)
sessionStatusReverseLinkService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseLinkService.setStatus("current")


class _SessionStatusReverseServiceMode_Type(Integer32):
    """Custom type sessionStatusReverseServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("atmp", 20),
          ("ciscoHDLC", 6),
          ("dvs", 18),
          ("fax", 19),
          ("frameRelay", 5),
          ("ftp", 17),
          ("hub", 16),
          ("iptest", 21),
          ("l2f", 12),
          ("l2tp", 11),
          ("none", 1),
          ("other", 2),
          ("ppp", 3),
          ("rawTCP", 9),
          ("rlogin", 10),
          ("slip", 4),
          ("tandem", 15),
          ("telnet", 8),
          ("terminalServer", 7),
          ("trunk", 13),
          ("unknown", 0),
          ("voice", 14))
    )


_SessionStatusReverseServiceMode_Type.__name__ = "Integer32"
_SessionStatusReverseServiceMode_Object = MibTableColumn
sessionStatusReverseServiceMode = _SessionStatusReverseServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 18),
    _SessionStatusReverseServiceMode_Type()
)
sessionStatusReverseServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseServiceMode.setStatus("current")
_SessionStatusReverseStartTime_Type = Integer32
_SessionStatusReverseStartTime_Object = MibTableColumn
sessionStatusReverseStartTime = _SessionStatusReverseStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 19),
    _SessionStatusReverseStartTime_Type()
)
sessionStatusReverseStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseStartTime.setStatus("current")
_SessionStatusReverseStopTime_Type = Integer32
_SessionStatusReverseStopTime_Object = MibTableColumn
sessionStatusReverseStopTime = _SessionStatusReverseStopTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 20),
    _SessionStatusReverseStopTime_Type()
)
sessionStatusReverseStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseStopTime.setStatus("current")
_SessionStatusReverseTimeOfModemSync_Type = Integer32
_SessionStatusReverseTimeOfModemSync_Object = MibTableColumn
sessionStatusReverseTimeOfModemSync = _SessionStatusReverseTimeOfModemSync_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 21),
    _SessionStatusReverseTimeOfModemSync_Type()
)
sessionStatusReverseTimeOfModemSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseTimeOfModemSync.setStatus("current")
_SessionStatusReverseTimeOfService_Type = Integer32
_SessionStatusReverseTimeOfService_Object = MibTableColumn
sessionStatusReverseTimeOfService = _SessionStatusReverseTimeOfService_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 22),
    _SessionStatusReverseTimeOfService_Type()
)
sessionStatusReverseTimeOfService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseTimeOfService.setStatus("current")


class _SessionStatusReverseTerminatingComponent_Type(Integer32):
    """Custom type sessionStatusReverseTerminatingComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("atmp", 32),
          ("atmptunnel", 33),
          ("chdlc", 9),
          ("cleartcp", 13),
          ("df", 3),
          ("ds0", 4),
          ("dvs", 28),
          ("dvstunnel", 29),
          ("ether", 15),
          ("fax", 30),
          ("fepdf", 17),
          ("fr", 10),
          ("hdlc", 6),
          ("hssi", 22),
          ("ip", 11),
          ("iptest", 34),
          ("l2f", 26),
          ("l2ftunnel", 27),
          ("l2tp", 14),
          ("l2tproute", 31),
          ("lineip", 18),
          ("loopback", 19),
          ("modem", 5),
          ("none", 1),
          ("other", 2),
          ("ppp", 7),
          ("rlogin", 21),
          ("shell", 20),
          ("slip", 8),
          ("sm", 23),
          ("telnet", 12),
          ("trunkip", 16),
          ("unknown", 0),
          ("vl", 24),
          ("voip", 25))
    )


_SessionStatusReverseTerminatingComponent_Type.__name__ = "Integer32"
_SessionStatusReverseTerminatingComponent_Object = MibTableColumn
sessionStatusReverseTerminatingComponent = _SessionStatusReverseTerminatingComponent_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 23),
    _SessionStatusReverseTerminatingComponent_Type()
)
sessionStatusReverseTerminatingComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseTerminatingComponent.setStatus("current")
_SessionStatusReverseTerminationCause_Type = Integer32
_SessionStatusReverseTerminationCause_Object = MibTableColumn
sessionStatusReverseTerminationCause = _SessionStatusReverseTerminationCause_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 24),
    _SessionStatusReverseTerminationCause_Type()
)
sessionStatusReverseTerminationCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseTerminationCause.setStatus("current")


class _SessionStatusReverseLastComponent_Type(Integer32):
    """Custom type sessionStatusReverseLastComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("atmp", 32),
          ("atmptunnel", 33),
          ("chdlc", 9),
          ("cleartcp", 13),
          ("df", 3),
          ("ds0", 4),
          ("dvs", 28),
          ("dvstunnel", 29),
          ("ether", 15),
          ("fax", 30),
          ("fepdf", 17),
          ("fr", 10),
          ("hdlc", 6),
          ("hssi", 22),
          ("ip", 11),
          ("iptest", 34),
          ("l2f", 26),
          ("l2ftunnel", 27),
          ("l2tp", 14),
          ("l2tproute", 31),
          ("lineip", 18),
          ("loopback", 19),
          ("modem", 5),
          ("none", 1),
          ("other", 2),
          ("ppp", 7),
          ("rlogin", 21),
          ("shell", 20),
          ("slip", 8),
          ("sm", 23),
          ("telnet", 12),
          ("trunkip", 16),
          ("unknown", 0),
          ("vl", 24),
          ("voip", 25))
    )


_SessionStatusReverseLastComponent_Type.__name__ = "Integer32"
_SessionStatusReverseLastComponent_Object = MibTableColumn
sessionStatusReverseLastComponent = _SessionStatusReverseLastComponent_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 25),
    _SessionStatusReverseLastComponent_Type()
)
sessionStatusReverseLastComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseLastComponent.setStatus("current")


class _SessionStatusReverseLayer1Slot_Type(Integer32):
    """Custom type sessionStatusReverseLayer1Slot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_SessionStatusReverseLayer1Slot_Type.__name__ = "Integer32"
_SessionStatusReverseLayer1Slot_Object = MibTableColumn
sessionStatusReverseLayer1Slot = _SessionStatusReverseLayer1Slot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 26),
    _SessionStatusReverseLayer1Slot_Type()
)
sessionStatusReverseLayer1Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseLayer1Slot.setStatus("current")


class _SessionStatusReverseLayer2Slot_Type(Integer32):
    """Custom type sessionStatusReverseLayer2Slot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_SessionStatusReverseLayer2Slot_Type.__name__ = "Integer32"
_SessionStatusReverseLayer2Slot_Object = MibTableColumn
sessionStatusReverseLayer2Slot = _SessionStatusReverseLayer2Slot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 27),
    _SessionStatusReverseLayer2Slot_Type()
)
sessionStatusReverseLayer2Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseLayer2Slot.setStatus("current")


class _SessionStatusReverseCalledNumber_Type(DisplayString):
    """Custom type sessionStatusReverseCalledNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SessionStatusReverseCalledNumber_Type.__name__ = "DisplayString"
_SessionStatusReverseCalledNumber_Object = MibTableColumn
sessionStatusReverseCalledNumber = _SessionStatusReverseCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 28),
    _SessionStatusReverseCalledNumber_Type()
)
sessionStatusReverseCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseCalledNumber.setStatus("current")


class _SessionStatusReverseCallingNumber_Type(DisplayString):
    """Custom type sessionStatusReverseCallingNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SessionStatusReverseCallingNumber_Type.__name__ = "DisplayString"
_SessionStatusReverseCallingNumber_Object = MibTableColumn
sessionStatusReverseCallingNumber = _SessionStatusReverseCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 29),
    _SessionStatusReverseCallingNumber_Type()
)
sessionStatusReverseCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseCallingNumber.setStatus("current")


class _SessionStatusReverseOriginateMode_Type(Integer32):
    """Custom type sessionStatusReverseOriginateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("answer", 0),
          ("originate", 1))
    )


_SessionStatusReverseOriginateMode_Type.__name__ = "Integer32"
_SessionStatusReverseOriginateMode_Object = MibTableColumn
sessionStatusReverseOriginateMode = _SessionStatusReverseOriginateMode_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 30),
    _SessionStatusReverseOriginateMode_Type()
)
sessionStatusReverseOriginateMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseOriginateMode.setStatus("current")
_SessionStatusReverseOctetsIn_Type = Integer32
_SessionStatusReverseOctetsIn_Object = MibTableColumn
sessionStatusReverseOctetsIn = _SessionStatusReverseOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 31),
    _SessionStatusReverseOctetsIn_Type()
)
sessionStatusReverseOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseOctetsIn.setStatus("current")
_SessionStatusReverseOctetsOut_Type = Integer32
_SessionStatusReverseOctetsOut_Object = MibTableColumn
sessionStatusReverseOctetsOut = _SessionStatusReverseOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 32),
    _SessionStatusReverseOctetsOut_Type()
)
sessionStatusReverseOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseOctetsOut.setStatus("current")
_SessionStatusReversePacketsIn_Type = Integer32
_SessionStatusReversePacketsIn_Object = MibTableColumn
sessionStatusReversePacketsIn = _SessionStatusReversePacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 33),
    _SessionStatusReversePacketsIn_Type()
)
sessionStatusReversePacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReversePacketsIn.setStatus("current")
_SessionStatusReversePacketsOut_Type = Integer32
_SessionStatusReversePacketsOut_Object = MibTableColumn
sessionStatusReversePacketsOut = _SessionStatusReversePacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 34),
    _SessionStatusReversePacketsOut_Type()
)
sessionStatusReversePacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReversePacketsOut.setStatus("current")
_SessionStatusReverseMultiLinkId_Type = Integer32
_SessionStatusReverseMultiLinkId_Object = MibTableColumn
sessionStatusReverseMultiLinkId = _SessionStatusReverseMultiLinkId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 35),
    _SessionStatusReverseMultiLinkId_Type()
)
sessionStatusReverseMultiLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseMultiLinkId.setStatus("current")
_SessionStatusReversePort_Type = Integer32
_SessionStatusReversePort_Object = MibTableColumn
sessionStatusReversePort = _SessionStatusReversePort_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 36),
    _SessionStatusReversePort_Type()
)
sessionStatusReversePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReversePort.setStatus("current")
_SessionStatusReverseTimeslot_Type = Integer32
_SessionStatusReverseTimeslot_Object = MibTableColumn
sessionStatusReverseTimeslot = _SessionStatusReverseTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 37),
    _SessionStatusReverseTimeslot_Type()
)
sessionStatusReverseTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseTimeslot.setStatus("current")
_SessionStatusReverseLinkCount_Type = Integer32
_SessionStatusReverseLinkCount_Object = MibTableColumn
sessionStatusReverseLinkCount = _SessionStatusReverseLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 38),
    _SessionStatusReverseLinkCount_Type()
)
sessionStatusReverseLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseLinkCount.setStatus("current")
_SessionStatusReverseTxStartDataRate_Type = Integer32
_SessionStatusReverseTxStartDataRate_Object = MibTableColumn
sessionStatusReverseTxStartDataRate = _SessionStatusReverseTxStartDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 39),
    _SessionStatusReverseTxStartDataRate_Type()
)
sessionStatusReverseTxStartDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseTxStartDataRate.setStatus("current")
_SessionStatusReverseRxStartDataRate_Type = Integer32
_SessionStatusReverseRxStartDataRate_Object = MibTableColumn
sessionStatusReverseRxStartDataRate = _SessionStatusReverseRxStartDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 40),
    _SessionStatusReverseRxStartDataRate_Type()
)
sessionStatusReverseRxStartDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseRxStartDataRate.setStatus("current")
_SessionStatusReverseTxEndDataRate_Type = Integer32
_SessionStatusReverseTxEndDataRate_Object = MibTableColumn
sessionStatusReverseTxEndDataRate = _SessionStatusReverseTxEndDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 41),
    _SessionStatusReverseTxEndDataRate_Type()
)
sessionStatusReverseTxEndDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseTxEndDataRate.setStatus("current")
_SessionStatusReverseRxEndDataRate_Type = Integer32
_SessionStatusReverseRxEndDataRate_Object = MibTableColumn
sessionStatusReverseRxEndDataRate = _SessionStatusReverseRxEndDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 42),
    _SessionStatusReverseRxEndDataRate_Type()
)
sessionStatusReverseRxEndDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseRxEndDataRate.setStatus("current")
_SessionStatusReverseTxMinDataRate_Type = Integer32
_SessionStatusReverseTxMinDataRate_Object = MibTableColumn
sessionStatusReverseTxMinDataRate = _SessionStatusReverseTxMinDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 43),
    _SessionStatusReverseTxMinDataRate_Type()
)
sessionStatusReverseTxMinDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseTxMinDataRate.setStatus("current")
_SessionStatusReverseRxMinDataRate_Type = Integer32
_SessionStatusReverseRxMinDataRate_Object = MibTableColumn
sessionStatusReverseRxMinDataRate = _SessionStatusReverseRxMinDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 44),
    _SessionStatusReverseRxMinDataRate_Type()
)
sessionStatusReverseRxMinDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseRxMinDataRate.setStatus("current")
_SessionStatusReverseTxMaxDataRate_Type = Integer32
_SessionStatusReverseTxMaxDataRate_Object = MibTableColumn
sessionStatusReverseTxMaxDataRate = _SessionStatusReverseTxMaxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 45),
    _SessionStatusReverseTxMaxDataRate_Type()
)
sessionStatusReverseTxMaxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseTxMaxDataRate.setStatus("current")
_SessionStatusReverseRxMaxDataRate_Type = Integer32
_SessionStatusReverseRxMaxDataRate_Object = MibTableColumn
sessionStatusReverseRxMaxDataRate = _SessionStatusReverseRxMaxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 46),
    _SessionStatusReverseRxMaxDataRate_Type()
)
sessionStatusReverseRxMaxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseRxMaxDataRate.setStatus("current")
_SessionStatusReverseIop_Type = Integer32
_SessionStatusReverseIop_Object = MibTableColumn
sessionStatusReverseIop = _SessionStatusReverseIop_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 47),
    _SessionStatusReverseIop_Type()
)
sessionStatusReverseIop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseIop.setStatus("current")
_SessionStatusReverseDmm_Type = Integer32
_SessionStatusReverseDmm_Object = MibTableColumn
sessionStatusReverseDmm = _SessionStatusReverseDmm_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 48),
    _SessionStatusReverseDmm_Type()
)
sessionStatusReverseDmm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseDmm.setStatus("current")
_SessionStatusReversePack_Type = Integer32
_SessionStatusReversePack_Object = MibTableColumn
sessionStatusReversePack = _SessionStatusReversePack_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 49),
    _SessionStatusReversePack_Type()
)
sessionStatusReversePack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReversePack.setStatus("current")
_SessionStatusReverseDevice_Type = Integer32
_SessionStatusReverseDevice_Object = MibTableColumn
sessionStatusReverseDevice = _SessionStatusReverseDevice_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 50),
    _SessionStatusReverseDevice_Type()
)
sessionStatusReverseDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseDevice.setStatus("current")
_SessionStatusReverseTdmStream_Type = Integer32
_SessionStatusReverseTdmStream_Object = MibTableColumn
sessionStatusReverseTdmStream = _SessionStatusReverseTdmStream_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 51),
    _SessionStatusReverseTdmStream_Type()
)
sessionStatusReverseTdmStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseTdmStream.setStatus("current")
_SessionStatusReverseTdmTimeSlot_Type = Integer32
_SessionStatusReverseTdmTimeSlot_Object = MibTableColumn
sessionStatusReverseTdmTimeSlot = _SessionStatusReverseTdmTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 52),
    _SessionStatusReverseTdmTimeSlot_Type()
)
sessionStatusReverseTdmTimeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseTdmTimeSlot.setStatus("current")


class _SessionStatusReverseTerminationReason_Type(DisplayString):
    """Custom type sessionStatusReverseTerminationReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SessionStatusReverseTerminationReason_Type.__name__ = "DisplayString"
_SessionStatusReverseTerminationReason_Object = MibTableColumn
sessionStatusReverseTerminationReason = _SessionStatusReverseTerminationReason_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 53),
    _SessionStatusReverseTerminationReason_Type()
)
sessionStatusReverseTerminationReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseTerminationReason.setStatus("current")
_SessionStatusReverseDuration_Type = Integer32
_SessionStatusReverseDuration_Object = MibTableColumn
sessionStatusReverseDuration = _SessionStatusReverseDuration_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 54),
    _SessionStatusReverseDuration_Type()
)
sessionStatusReverseDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseDuration.setStatus("current")


class _SessionStatusReverseDurationHMS_Type(DisplayString):
    """Custom type sessionStatusReverseDurationHMS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SessionStatusReverseDurationHMS_Type.__name__ = "DisplayString"
_SessionStatusReverseDurationHMS_Object = MibTableColumn
sessionStatusReverseDurationHMS = _SessionStatusReverseDurationHMS_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 55),
    _SessionStatusReverseDurationHMS_Type()
)
sessionStatusReverseDurationHMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseDurationHMS.setStatus("current")


class _SessionStatusReverseSs7SessionId_Type(DisplayString):
    """Custom type sessionStatusReverseSs7SessionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 41),
    )


_SessionStatusReverseSs7SessionId_Type.__name__ = "DisplayString"
_SessionStatusReverseSs7SessionId_Object = MibTableColumn
sessionStatusReverseSs7SessionId = _SessionStatusReverseSs7SessionId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 56),
    _SessionStatusReverseSs7SessionId_Type()
)
sessionStatusReverseSs7SessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseSs7SessionId.setStatus("current")
_SessionStatusReverseModemNumber_Type = Integer32
_SessionStatusReverseModemNumber_Object = MibTableColumn
sessionStatusReverseModemNumber = _SessionStatusReverseModemNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 57),
    _SessionStatusReverseModemNumber_Type()
)
sessionStatusReverseModemNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseModemNumber.setStatus("current")


class _SessionStatusReverseTunnelType_Type(Integer32):
    """Custom type sessionStatusReverseTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("atmp", 6),
          ("dvs", 5),
          ("l2f", 3),
          ("l2tp", 4),
          ("none", 1),
          ("other", 2),
          ("unknown", 0))
    )


_SessionStatusReverseTunnelType_Type.__name__ = "Integer32"
_SessionStatusReverseTunnelType_Object = MibTableColumn
sessionStatusReverseTunnelType = _SessionStatusReverseTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 58),
    _SessionStatusReverseTunnelType_Type()
)
sessionStatusReverseTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseTunnelType.setStatus("current")


class _SessionStatusReverseTunnelMediumType_Type(Integer32):
    """Custom type sessionStatusReverseTunnelMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 3),
          ("none", 1),
          ("other", 2),
          ("unknown", 0))
    )


_SessionStatusReverseTunnelMediumType_Type.__name__ = "Integer32"
_SessionStatusReverseTunnelMediumType_Object = MibTableColumn
sessionStatusReverseTunnelMediumType = _SessionStatusReverseTunnelMediumType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 59),
    _SessionStatusReverseTunnelMediumType_Type()
)
sessionStatusReverseTunnelMediumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseTunnelMediumType.setStatus("current")
_SessionStatusReverseTunnelServerAddress_Type = IpAddress
_SessionStatusReverseTunnelServerAddress_Object = MibTableColumn
sessionStatusReverseTunnelServerAddress = _SessionStatusReverseTunnelServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 60),
    _SessionStatusReverseTunnelServerAddress_Type()
)
sessionStatusReverseTunnelServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseTunnelServerAddress.setStatus("current")
_SessionStatusReverseCallClass_Type = Integer32
_SessionStatusReverseCallClass_Object = MibTableColumn
sessionStatusReverseCallClass = _SessionStatusReverseCallClass_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 61),
    _SessionStatusReverseCallClass_Type()
)
sessionStatusReverseCallClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseCallClass.setStatus("current")
_SessionStatusReverseTandemPort_Type = Integer32
_SessionStatusReverseTandemPort_Object = MibTableColumn
sessionStatusReverseTandemPort = _SessionStatusReverseTandemPort_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 62),
    _SessionStatusReverseTandemPort_Type()
)
sessionStatusReverseTandemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseTandemPort.setStatus("current")
_SessionStatusReverseTandemTimeslot_Type = Integer32
_SessionStatusReverseTandemTimeslot_Object = MibTableColumn
sessionStatusReverseTandemTimeslot = _SessionStatusReverseTandemTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 63),
    _SessionStatusReverseTandemTimeslot_Type()
)
sessionStatusReverseTandemTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseTandemTimeslot.setStatus("current")


class _SessionStatusReverseCallClassArray_Type(OctetString):
    """Custom type sessionStatusReverseCallClassArray based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SessionStatusReverseCallClassArray_Type.__name__ = "OctetString"
_SessionStatusReverseCallClassArray_Object = MibTableColumn
sessionStatusReverseCallClassArray = _SessionStatusReverseCallClassArray_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 64),
    _SessionStatusReverseCallClassArray_Type()
)
sessionStatusReverseCallClassArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseCallClassArray.setStatus("current")
_SessionStatusReverseCallClassLen_Type = Integer32
_SessionStatusReverseCallClassLen_Object = MibTableColumn
sessionStatusReverseCallClassLen = _SessionStatusReverseCallClassLen_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 65),
    _SessionStatusReverseCallClassLen_Type()
)
sessionStatusReverseCallClassLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseCallClassLen.setStatus("current")


class _SessionStatusReverseActualAuthMethod_Type(Integer32):
    """Custom type sessionStatusReverseActualAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("radius", 1),
          ("remote", 3))
    )


_SessionStatusReverseActualAuthMethod_Type.__name__ = "Integer32"
_SessionStatusReverseActualAuthMethod_Object = MibTableColumn
sessionStatusReverseActualAuthMethod = _SessionStatusReverseActualAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 66),
    _SessionStatusReverseActualAuthMethod_Type()
)
sessionStatusReverseActualAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseActualAuthMethod.setStatus("current")


class _SessionStatusReverseModemModulation_Type(Integer32):
    """Custom type sessionStatusReverseModemModulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("bell103", 2),
          ("bell208", 3),
          ("bell212", 4),
          ("k56", 17),
          ("none", 0),
          ("unknown", 1),
          ("v17", 5),
          ("v21", 6),
          ("v22", 7),
          ("v22bis", 8),
          ("v23", 9),
          ("v27", 10),
          ("v29", 11),
          ("v32", 12),
          ("v32bis", 13),
          ("v33", 14),
          ("v34", 15),
          ("v90", 18),
          ("vFC", 16))
    )


_SessionStatusReverseModemModulation_Type.__name__ = "Integer32"
_SessionStatusReverseModemModulation_Object = MibTableColumn
sessionStatusReverseModemModulation = _SessionStatusReverseModemModulation_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 67),
    _SessionStatusReverseModemModulation_Type()
)
sessionStatusReverseModemModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseModemModulation.setStatus("current")


class _SessionStatusReverseModemErrorCorrection_Type(Integer32):
    """Custom type sessionStatusReverseModemErrorCorrection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mNP", 2),
          ("none", 0),
          ("unknown", 1),
          ("v42", 3))
    )


_SessionStatusReverseModemErrorCorrection_Type.__name__ = "Integer32"
_SessionStatusReverseModemErrorCorrection_Object = MibTableColumn
sessionStatusReverseModemErrorCorrection = _SessionStatusReverseModemErrorCorrection_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 68),
    _SessionStatusReverseModemErrorCorrection_Type()
)
sessionStatusReverseModemErrorCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseModemErrorCorrection.setStatus("current")


class _SessionStatusReverseModemDataCompression_Type(Integer32):
    """Custom type sessionStatusReverseModemDataCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mNP5", 2),
          ("none", 0),
          ("unknown", 1),
          ("v42bis", 3))
    )


_SessionStatusReverseModemDataCompression_Type.__name__ = "Integer32"
_SessionStatusReverseModemDataCompression_Object = MibTableColumn
sessionStatusReverseModemDataCompression = _SessionStatusReverseModemDataCompression_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 69),
    _SessionStatusReverseModemDataCompression_Type()
)
sessionStatusReverseModemDataCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseModemDataCompression.setStatus("current")
_SessionStatusReverseModemTxBlocks_Type = Integer32
_SessionStatusReverseModemTxBlocks_Object = MibTableColumn
sessionStatusReverseModemTxBlocks = _SessionStatusReverseModemTxBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 70),
    _SessionStatusReverseModemTxBlocks_Type()
)
sessionStatusReverseModemTxBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseModemTxBlocks.setStatus("current")
_SessionStatusReverseModemRetransmits_Type = Integer32
_SessionStatusReverseModemRetransmits_Object = MibTableColumn
sessionStatusReverseModemRetransmits = _SessionStatusReverseModemRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 71),
    _SessionStatusReverseModemRetransmits_Type()
)
sessionStatusReverseModemRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseModemRetransmits.setStatus("current")
_SessionStatusReverseModemSNR_Type = Integer32
_SessionStatusReverseModemSNR_Object = MibTableColumn
sessionStatusReverseModemSNR = _SessionStatusReverseModemSNR_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 72),
    _SessionStatusReverseModemSNR_Type()
)
sessionStatusReverseModemSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseModemSNR.setStatus("current")
_SessionStatusReverseModemLocalRetrains_Type = Integer32
_SessionStatusReverseModemLocalRetrains_Object = MibTableColumn
sessionStatusReverseModemLocalRetrains = _SessionStatusReverseModemLocalRetrains_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 73),
    _SessionStatusReverseModemLocalRetrains_Type()
)
sessionStatusReverseModemLocalRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseModemLocalRetrains.setStatus("current")
_SessionStatusReverseModemRemoteRetrains_Type = Integer32
_SessionStatusReverseModemRemoteRetrains_Object = MibTableColumn
sessionStatusReverseModemRemoteRetrains = _SessionStatusReverseModemRemoteRetrains_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 74),
    _SessionStatusReverseModemRemoteRetrains_Type()
)
sessionStatusReverseModemRemoteRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseModemRemoteRetrains.setStatus("current")
_SessionStatusReverseModemLocalRenegotiations_Type = Integer32
_SessionStatusReverseModemLocalRenegotiations_Object = MibTableColumn
sessionStatusReverseModemLocalRenegotiations = _SessionStatusReverseModemLocalRenegotiations_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 75),
    _SessionStatusReverseModemLocalRenegotiations_Type()
)
sessionStatusReverseModemLocalRenegotiations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseModemLocalRenegotiations.setStatus("current")
_SessionStatusReverseModemRemoteRenegotiations_Type = Integer32
_SessionStatusReverseModemRemoteRenegotiations_Object = MibTableColumn
sessionStatusReverseModemRemoteRenegotiations = _SessionStatusReverseModemRemoteRenegotiations_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 76),
    _SessionStatusReverseModemRemoteRenegotiations_Type()
)
sessionStatusReverseModemRemoteRenegotiations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseModemRemoteRenegotiations.setStatus("current")
_SessionStatusReverseModemReceiveLineLevel_Type = Integer32
_SessionStatusReverseModemReceiveLineLevel_Object = MibTableColumn
sessionStatusReverseModemReceiveLineLevel = _SessionStatusReverseModemReceiveLineLevel_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 77),
    _SessionStatusReverseModemReceiveLineLevel_Type()
)
sessionStatusReverseModemReceiveLineLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseModemReceiveLineLevel.setStatus("current")
_SessionStatusReverseRemoteIPXNetwork_Type = Integer32
_SessionStatusReverseRemoteIPXNetwork_Object = MibTableColumn
sessionStatusReverseRemoteIPXNetwork = _SessionStatusReverseRemoteIPXNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 78),
    _SessionStatusReverseRemoteIPXNetwork_Type()
)
sessionStatusReverseRemoteIPXNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseRemoteIPXNetwork.setStatus("current")


class _SessionStatusReverseRemoteIPXNode_Type(DisplayString):
    """Custom type sessionStatusReverseRemoteIPXNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SessionStatusReverseRemoteIPXNode_Type.__name__ = "DisplayString"
_SessionStatusReverseRemoteIPXNode_Object = MibTableColumn
sessionStatusReverseRemoteIPXNode = _SessionStatusReverseRemoteIPXNode_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 79),
    _SessionStatusReverseRemoteIPXNode_Type()
)
sessionStatusReverseRemoteIPXNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseRemoteIPXNode.setStatus("current")
_SessionStatusReverseCleartcpRemoteIP_Type = IpAddress
_SessionStatusReverseCleartcpRemoteIP_Object = MibTableColumn
sessionStatusReverseCleartcpRemoteIP = _SessionStatusReverseCleartcpRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 80),
    _SessionStatusReverseCleartcpRemoteIP_Type()
)
sessionStatusReverseCleartcpRemoteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseCleartcpRemoteIP.setStatus("current")
_SessionStatusReverseCleartcpRemotePort_Type = Integer32
_SessionStatusReverseCleartcpRemotePort_Object = MibTableColumn
sessionStatusReverseCleartcpRemotePort = _SessionStatusReverseCleartcpRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 81),
    _SessionStatusReverseCleartcpRemotePort_Type()
)
sessionStatusReverseCleartcpRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseCleartcpRemotePort.setStatus("current")
_SessionStatusReverseTunnelId_Type = Integer32
_SessionStatusReverseTunnelId_Object = MibTableColumn
sessionStatusReverseTunnelId = _SessionStatusReverseTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 82),
    _SessionStatusReverseTunnelId_Type()
)
sessionStatusReverseTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseTunnelId.setStatus("current")
_SessionStatusReverseLinkId_Type = Integer32
_SessionStatusReverseLinkId_Object = MibTableColumn
sessionStatusReverseLinkId = _SessionStatusReverseLinkId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 106, 1, 83),
    _SessionStatusReverseLinkId_Type()
)
sessionStatusReverseLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusReverseLinkId.setStatus("current")
_SessionStatusHistoryTable_Object = MibTable
sessionStatusHistoryTable = _SessionStatusHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107)
)
if mibBuilder.loadTexts:
    sessionStatusHistoryTable.setStatus("current")
_SessionStatusHistoryEntry_Object = MibTableRow
sessionStatusHistoryEntry = _SessionStatusHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1)
)
sessionStatusHistoryEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "sessionStatusHistoryIndex"),
)
if mibBuilder.loadTexts:
    sessionStatusHistoryEntry.setStatus("current")


class _SessionStatusHistoryIndex_Type(Integer32):
    """Custom type sessionStatusHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_SessionStatusHistoryIndex_Type.__name__ = "Integer32"
_SessionStatusHistoryIndex_Object = MibTableColumn
sessionStatusHistoryIndex = _SessionStatusHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 1),
    _SessionStatusHistoryIndex_Type()
)
sessionStatusHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryIndex.setStatus("current")
_SessionStatusHistorySessionID_Type = Integer32
_SessionStatusHistorySessionID_Object = MibTableColumn
sessionStatusHistorySessionID = _SessionStatusHistorySessionID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 2),
    _SessionStatusHistorySessionID_Type()
)
sessionStatusHistorySessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistorySessionID.setStatus("current")


class _SessionStatusHistoryState_Type(Integer32):
    """Custom type sessionStatusHistoryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_SessionStatusHistoryState_Type.__name__ = "Integer32"
_SessionStatusHistoryState_Object = MibTableColumn
sessionStatusHistoryState = _SessionStatusHistoryState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 3),
    _SessionStatusHistoryState_Type()
)
sessionStatusHistoryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryState.setStatus("current")


class _SessionStatusHistoryPermanentFlag_Type(Integer32):
    """Custom type sessionStatusHistoryPermanentFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permanent", 2),
          ("switched", 1),
          ("unknown", 0))
    )


_SessionStatusHistoryPermanentFlag_Type.__name__ = "Integer32"
_SessionStatusHistoryPermanentFlag_Object = MibTableColumn
sessionStatusHistoryPermanentFlag = _SessionStatusHistoryPermanentFlag_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 10),
    _SessionStatusHistoryPermanentFlag_Type()
)
sessionStatusHistoryPermanentFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryPermanentFlag.setStatus("current")
_SessionStatusHistoryVpopId_Type = Integer32
_SessionStatusHistoryVpopId_Object = MibTableColumn
sessionStatusHistoryVpopId = _SessionStatusHistoryVpopId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 11),
    _SessionStatusHistoryVpopId_Type()
)
sessionStatusHistoryVpopId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryVpopId.setStatus("current")


class _SessionStatusHistoryName_Type(DisplayString):
    """Custom type sessionStatusHistoryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 68),
    )


_SessionStatusHistoryName_Type.__name__ = "DisplayString"
_SessionStatusHistoryName_Object = MibTableColumn
sessionStatusHistoryName = _SessionStatusHistoryName_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 12),
    _SessionStatusHistoryName_Type()
)
sessionStatusHistoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryName.setStatus("current")
_SessionStatusHistoryRemoteIP_Type = IpAddress
_SessionStatusHistoryRemoteIP_Object = MibTableColumn
sessionStatusHistoryRemoteIP = _SessionStatusHistoryRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 13),
    _SessionStatusHistoryRemoteIP_Type()
)
sessionStatusHistoryRemoteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryRemoteIP.setStatus("current")
_SessionStatusHistoryRemoteIPMask_Type = IpAddress
_SessionStatusHistoryRemoteIPMask_Object = MibTableColumn
sessionStatusHistoryRemoteIPMask = _SessionStatusHistoryRemoteIPMask_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 14),
    _SessionStatusHistoryRemoteIPMask_Type()
)
sessionStatusHistoryRemoteIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryRemoteIPMask.setStatus("current")
_SessionStatusHistoryLocalIP_Type = IpAddress
_SessionStatusHistoryLocalIP_Object = MibTableColumn
sessionStatusHistoryLocalIP = _SessionStatusHistoryLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 15),
    _SessionStatusHistoryLocalIP_Type()
)
sessionStatusHistoryLocalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryLocalIP.setStatus("current")
_SessionStatusHistoryLocalIPMask_Type = IpAddress
_SessionStatusHistoryLocalIPMask_Object = MibTableColumn
sessionStatusHistoryLocalIPMask = _SessionStatusHistoryLocalIPMask_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 16),
    _SessionStatusHistoryLocalIPMask_Type()
)
sessionStatusHistoryLocalIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryLocalIPMask.setStatus("current")


class _SessionStatusHistoryLinkService_Type(Integer32):
    """Custom type sessionStatusHistoryLinkService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 11),
          ("hssi", 14),
          ("hub", 15),
          ("isdn56K", 3),
          ("isdn64K", 4),
          ("isdnV110", 6),
          ("isdnV120", 5),
          ("loopback", 13),
          ("modemK56", 9),
          ("modemV32", 7),
          ("modemV34", 8),
          ("modemV90", 10),
          ("none", 1),
          ("other", 2),
          ("t1Trunk", 12),
          ("unknown", 0),
          ("voice", 16))
    )


_SessionStatusHistoryLinkService_Type.__name__ = "Integer32"
_SessionStatusHistoryLinkService_Object = MibTableColumn
sessionStatusHistoryLinkService = _SessionStatusHistoryLinkService_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 17),
    _SessionStatusHistoryLinkService_Type()
)
sessionStatusHistoryLinkService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryLinkService.setStatus("current")


class _SessionStatusHistoryServiceMode_Type(Integer32):
    """Custom type sessionStatusHistoryServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("atmp", 20),
          ("ciscoHDLC", 6),
          ("dvs", 18),
          ("fax", 19),
          ("frameRelay", 5),
          ("ftp", 17),
          ("hub", 16),
          ("iptest", 21),
          ("l2f", 12),
          ("l2tp", 11),
          ("none", 1),
          ("other", 2),
          ("ppp", 3),
          ("rawTCP", 9),
          ("rlogin", 10),
          ("slip", 4),
          ("tandem", 15),
          ("telnet", 8),
          ("terminalServer", 7),
          ("trunk", 13),
          ("unknown", 0),
          ("voice", 14))
    )


_SessionStatusHistoryServiceMode_Type.__name__ = "Integer32"
_SessionStatusHistoryServiceMode_Object = MibTableColumn
sessionStatusHistoryServiceMode = _SessionStatusHistoryServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 18),
    _SessionStatusHistoryServiceMode_Type()
)
sessionStatusHistoryServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryServiceMode.setStatus("current")
_SessionStatusHistoryStartTime_Type = Integer32
_SessionStatusHistoryStartTime_Object = MibTableColumn
sessionStatusHistoryStartTime = _SessionStatusHistoryStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 19),
    _SessionStatusHistoryStartTime_Type()
)
sessionStatusHistoryStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryStartTime.setStatus("current")
_SessionStatusHistoryStopTime_Type = Integer32
_SessionStatusHistoryStopTime_Object = MibTableColumn
sessionStatusHistoryStopTime = _SessionStatusHistoryStopTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 20),
    _SessionStatusHistoryStopTime_Type()
)
sessionStatusHistoryStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryStopTime.setStatus("current")
_SessionStatusHistoryTimeOfModemSync_Type = Integer32
_SessionStatusHistoryTimeOfModemSync_Object = MibTableColumn
sessionStatusHistoryTimeOfModemSync = _SessionStatusHistoryTimeOfModemSync_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 21),
    _SessionStatusHistoryTimeOfModemSync_Type()
)
sessionStatusHistoryTimeOfModemSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryTimeOfModemSync.setStatus("current")
_SessionStatusHistoryTimeOfService_Type = Integer32
_SessionStatusHistoryTimeOfService_Object = MibTableColumn
sessionStatusHistoryTimeOfService = _SessionStatusHistoryTimeOfService_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 22),
    _SessionStatusHistoryTimeOfService_Type()
)
sessionStatusHistoryTimeOfService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryTimeOfService.setStatus("current")


class _SessionStatusHistoryTerminatingComponent_Type(Integer32):
    """Custom type sessionStatusHistoryTerminatingComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("atmp", 32),
          ("atmptunnel", 33),
          ("chdlc", 9),
          ("cleartcp", 13),
          ("df", 3),
          ("ds0", 4),
          ("dvs", 28),
          ("dvstunnel", 29),
          ("ether", 15),
          ("fax", 30),
          ("fepdf", 17),
          ("fr", 10),
          ("hdlc", 6),
          ("hssi", 22),
          ("ip", 11),
          ("iptest", 34),
          ("l2f", 26),
          ("l2ftunnel", 27),
          ("l2tp", 14),
          ("l2tproute", 31),
          ("lineip", 18),
          ("loopback", 19),
          ("modem", 5),
          ("none", 1),
          ("other", 2),
          ("ppp", 7),
          ("rlogin", 21),
          ("shell", 20),
          ("slip", 8),
          ("sm", 23),
          ("telnet", 12),
          ("trunkip", 16),
          ("unknown", 0),
          ("vl", 24),
          ("voip", 25))
    )


_SessionStatusHistoryTerminatingComponent_Type.__name__ = "Integer32"
_SessionStatusHistoryTerminatingComponent_Object = MibTableColumn
sessionStatusHistoryTerminatingComponent = _SessionStatusHistoryTerminatingComponent_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 23),
    _SessionStatusHistoryTerminatingComponent_Type()
)
sessionStatusHistoryTerminatingComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryTerminatingComponent.setStatus("current")
_SessionStatusHistoryTerminationCause_Type = Integer32
_SessionStatusHistoryTerminationCause_Object = MibTableColumn
sessionStatusHistoryTerminationCause = _SessionStatusHistoryTerminationCause_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 24),
    _SessionStatusHistoryTerminationCause_Type()
)
sessionStatusHistoryTerminationCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryTerminationCause.setStatus("current")


class _SessionStatusHistoryLastComponent_Type(Integer32):
    """Custom type sessionStatusHistoryLastComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("atmp", 32),
          ("atmptunnel", 33),
          ("chdlc", 9),
          ("cleartcp", 13),
          ("df", 3),
          ("ds0", 4),
          ("dvs", 28),
          ("dvstunnel", 29),
          ("ether", 15),
          ("fax", 30),
          ("fepdf", 17),
          ("fr", 10),
          ("hdlc", 6),
          ("hssi", 22),
          ("ip", 11),
          ("iptest", 34),
          ("l2f", 26),
          ("l2ftunnel", 27),
          ("l2tp", 14),
          ("l2tproute", 31),
          ("lineip", 18),
          ("loopback", 19),
          ("modem", 5),
          ("none", 1),
          ("other", 2),
          ("ppp", 7),
          ("rlogin", 21),
          ("shell", 20),
          ("slip", 8),
          ("sm", 23),
          ("telnet", 12),
          ("trunkip", 16),
          ("unknown", 0),
          ("vl", 24),
          ("voip", 25))
    )


_SessionStatusHistoryLastComponent_Type.__name__ = "Integer32"
_SessionStatusHistoryLastComponent_Object = MibTableColumn
sessionStatusHistoryLastComponent = _SessionStatusHistoryLastComponent_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 25),
    _SessionStatusHistoryLastComponent_Type()
)
sessionStatusHistoryLastComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryLastComponent.setStatus("current")


class _SessionStatusHistoryLayer1Slot_Type(Integer32):
    """Custom type sessionStatusHistoryLayer1Slot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_SessionStatusHistoryLayer1Slot_Type.__name__ = "Integer32"
_SessionStatusHistoryLayer1Slot_Object = MibTableColumn
sessionStatusHistoryLayer1Slot = _SessionStatusHistoryLayer1Slot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 26),
    _SessionStatusHistoryLayer1Slot_Type()
)
sessionStatusHistoryLayer1Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryLayer1Slot.setStatus("current")


class _SessionStatusHistoryLayer2Slot_Type(Integer32):
    """Custom type sessionStatusHistoryLayer2Slot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_SessionStatusHistoryLayer2Slot_Type.__name__ = "Integer32"
_SessionStatusHistoryLayer2Slot_Object = MibTableColumn
sessionStatusHistoryLayer2Slot = _SessionStatusHistoryLayer2Slot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 27),
    _SessionStatusHistoryLayer2Slot_Type()
)
sessionStatusHistoryLayer2Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryLayer2Slot.setStatus("current")


class _SessionStatusHistoryCalledNumber_Type(DisplayString):
    """Custom type sessionStatusHistoryCalledNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SessionStatusHistoryCalledNumber_Type.__name__ = "DisplayString"
_SessionStatusHistoryCalledNumber_Object = MibTableColumn
sessionStatusHistoryCalledNumber = _SessionStatusHistoryCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 28),
    _SessionStatusHistoryCalledNumber_Type()
)
sessionStatusHistoryCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryCalledNumber.setStatus("current")


class _SessionStatusHistoryCallingNumber_Type(DisplayString):
    """Custom type sessionStatusHistoryCallingNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SessionStatusHistoryCallingNumber_Type.__name__ = "DisplayString"
_SessionStatusHistoryCallingNumber_Object = MibTableColumn
sessionStatusHistoryCallingNumber = _SessionStatusHistoryCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 29),
    _SessionStatusHistoryCallingNumber_Type()
)
sessionStatusHistoryCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryCallingNumber.setStatus("current")


class _SessionStatusHistoryOriginateMode_Type(Integer32):
    """Custom type sessionStatusHistoryOriginateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("answer", 0),
          ("originate", 1))
    )


_SessionStatusHistoryOriginateMode_Type.__name__ = "Integer32"
_SessionStatusHistoryOriginateMode_Object = MibTableColumn
sessionStatusHistoryOriginateMode = _SessionStatusHistoryOriginateMode_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 30),
    _SessionStatusHistoryOriginateMode_Type()
)
sessionStatusHistoryOriginateMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryOriginateMode.setStatus("current")
_SessionStatusHistoryOctetsIn_Type = Integer32
_SessionStatusHistoryOctetsIn_Object = MibTableColumn
sessionStatusHistoryOctetsIn = _SessionStatusHistoryOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 31),
    _SessionStatusHistoryOctetsIn_Type()
)
sessionStatusHistoryOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryOctetsIn.setStatus("current")
_SessionStatusHistoryOctetsOut_Type = Integer32
_SessionStatusHistoryOctetsOut_Object = MibTableColumn
sessionStatusHistoryOctetsOut = _SessionStatusHistoryOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 32),
    _SessionStatusHistoryOctetsOut_Type()
)
sessionStatusHistoryOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryOctetsOut.setStatus("current")
_SessionStatusHistoryPacketsIn_Type = Integer32
_SessionStatusHistoryPacketsIn_Object = MibTableColumn
sessionStatusHistoryPacketsIn = _SessionStatusHistoryPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 33),
    _SessionStatusHistoryPacketsIn_Type()
)
sessionStatusHistoryPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryPacketsIn.setStatus("current")
_SessionStatusHistoryPacketsOut_Type = Integer32
_SessionStatusHistoryPacketsOut_Object = MibTableColumn
sessionStatusHistoryPacketsOut = _SessionStatusHistoryPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 34),
    _SessionStatusHistoryPacketsOut_Type()
)
sessionStatusHistoryPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryPacketsOut.setStatus("current")
_SessionStatusHistoryMultiLinkId_Type = Integer32
_SessionStatusHistoryMultiLinkId_Object = MibTableColumn
sessionStatusHistoryMultiLinkId = _SessionStatusHistoryMultiLinkId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 35),
    _SessionStatusHistoryMultiLinkId_Type()
)
sessionStatusHistoryMultiLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryMultiLinkId.setStatus("current")
_SessionStatusHistoryPort_Type = Integer32
_SessionStatusHistoryPort_Object = MibTableColumn
sessionStatusHistoryPort = _SessionStatusHistoryPort_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 36),
    _SessionStatusHistoryPort_Type()
)
sessionStatusHistoryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryPort.setStatus("current")
_SessionStatusHistoryTimeslot_Type = Integer32
_SessionStatusHistoryTimeslot_Object = MibTableColumn
sessionStatusHistoryTimeslot = _SessionStatusHistoryTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 37),
    _SessionStatusHistoryTimeslot_Type()
)
sessionStatusHistoryTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryTimeslot.setStatus("current")
_SessionStatusHistoryLinkCount_Type = Integer32
_SessionStatusHistoryLinkCount_Object = MibTableColumn
sessionStatusHistoryLinkCount = _SessionStatusHistoryLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 38),
    _SessionStatusHistoryLinkCount_Type()
)
sessionStatusHistoryLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryLinkCount.setStatus("current")
_SessionStatusHistoryTxStartDataRate_Type = Integer32
_SessionStatusHistoryTxStartDataRate_Object = MibTableColumn
sessionStatusHistoryTxStartDataRate = _SessionStatusHistoryTxStartDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 39),
    _SessionStatusHistoryTxStartDataRate_Type()
)
sessionStatusHistoryTxStartDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryTxStartDataRate.setStatus("current")
_SessionStatusHistoryRxStartDataRate_Type = Integer32
_SessionStatusHistoryRxStartDataRate_Object = MibTableColumn
sessionStatusHistoryRxStartDataRate = _SessionStatusHistoryRxStartDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 40),
    _SessionStatusHistoryRxStartDataRate_Type()
)
sessionStatusHistoryRxStartDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryRxStartDataRate.setStatus("current")
_SessionStatusHistoryTxEndDataRate_Type = Integer32
_SessionStatusHistoryTxEndDataRate_Object = MibTableColumn
sessionStatusHistoryTxEndDataRate = _SessionStatusHistoryTxEndDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 41),
    _SessionStatusHistoryTxEndDataRate_Type()
)
sessionStatusHistoryTxEndDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryTxEndDataRate.setStatus("current")
_SessionStatusHistoryRxEndDataRate_Type = Integer32
_SessionStatusHistoryRxEndDataRate_Object = MibTableColumn
sessionStatusHistoryRxEndDataRate = _SessionStatusHistoryRxEndDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 42),
    _SessionStatusHistoryRxEndDataRate_Type()
)
sessionStatusHistoryRxEndDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryRxEndDataRate.setStatus("current")
_SessionStatusHistoryTxMinDataRate_Type = Integer32
_SessionStatusHistoryTxMinDataRate_Object = MibTableColumn
sessionStatusHistoryTxMinDataRate = _SessionStatusHistoryTxMinDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 43),
    _SessionStatusHistoryTxMinDataRate_Type()
)
sessionStatusHistoryTxMinDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryTxMinDataRate.setStatus("current")
_SessionStatusHistoryRxMinDataRate_Type = Integer32
_SessionStatusHistoryRxMinDataRate_Object = MibTableColumn
sessionStatusHistoryRxMinDataRate = _SessionStatusHistoryRxMinDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 44),
    _SessionStatusHistoryRxMinDataRate_Type()
)
sessionStatusHistoryRxMinDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryRxMinDataRate.setStatus("current")
_SessionStatusHistoryTxMaxDataRate_Type = Integer32
_SessionStatusHistoryTxMaxDataRate_Object = MibTableColumn
sessionStatusHistoryTxMaxDataRate = _SessionStatusHistoryTxMaxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 45),
    _SessionStatusHistoryTxMaxDataRate_Type()
)
sessionStatusHistoryTxMaxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryTxMaxDataRate.setStatus("current")
_SessionStatusHistoryRxMaxDataRate_Type = Integer32
_SessionStatusHistoryRxMaxDataRate_Object = MibTableColumn
sessionStatusHistoryRxMaxDataRate = _SessionStatusHistoryRxMaxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 46),
    _SessionStatusHistoryRxMaxDataRate_Type()
)
sessionStatusHistoryRxMaxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryRxMaxDataRate.setStatus("current")
_SessionStatusHistoryIop_Type = Integer32
_SessionStatusHistoryIop_Object = MibTableColumn
sessionStatusHistoryIop = _SessionStatusHistoryIop_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 47),
    _SessionStatusHistoryIop_Type()
)
sessionStatusHistoryIop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryIop.setStatus("current")
_SessionStatusHistoryDmm_Type = Integer32
_SessionStatusHistoryDmm_Object = MibTableColumn
sessionStatusHistoryDmm = _SessionStatusHistoryDmm_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 48),
    _SessionStatusHistoryDmm_Type()
)
sessionStatusHistoryDmm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryDmm.setStatus("current")
_SessionStatusHistoryPack_Type = Integer32
_SessionStatusHistoryPack_Object = MibTableColumn
sessionStatusHistoryPack = _SessionStatusHistoryPack_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 49),
    _SessionStatusHistoryPack_Type()
)
sessionStatusHistoryPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryPack.setStatus("current")
_SessionStatusHistoryDevice_Type = Integer32
_SessionStatusHistoryDevice_Object = MibTableColumn
sessionStatusHistoryDevice = _SessionStatusHistoryDevice_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 50),
    _SessionStatusHistoryDevice_Type()
)
sessionStatusHistoryDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryDevice.setStatus("current")
_SessionStatusHistoryTdmStream_Type = Integer32
_SessionStatusHistoryTdmStream_Object = MibTableColumn
sessionStatusHistoryTdmStream = _SessionStatusHistoryTdmStream_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 51),
    _SessionStatusHistoryTdmStream_Type()
)
sessionStatusHistoryTdmStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryTdmStream.setStatus("current")
_SessionStatusHistoryTdmTimeSlot_Type = Integer32
_SessionStatusHistoryTdmTimeSlot_Object = MibTableColumn
sessionStatusHistoryTdmTimeSlot = _SessionStatusHistoryTdmTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 52),
    _SessionStatusHistoryTdmTimeSlot_Type()
)
sessionStatusHistoryTdmTimeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryTdmTimeSlot.setStatus("current")


class _SessionStatusHistoryTerminationReason_Type(DisplayString):
    """Custom type sessionStatusHistoryTerminationReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SessionStatusHistoryTerminationReason_Type.__name__ = "DisplayString"
_SessionStatusHistoryTerminationReason_Object = MibTableColumn
sessionStatusHistoryTerminationReason = _SessionStatusHistoryTerminationReason_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 53),
    _SessionStatusHistoryTerminationReason_Type()
)
sessionStatusHistoryTerminationReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryTerminationReason.setStatus("current")
_SessionStatusHistoryDuration_Type = Integer32
_SessionStatusHistoryDuration_Object = MibTableColumn
sessionStatusHistoryDuration = _SessionStatusHistoryDuration_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 54),
    _SessionStatusHistoryDuration_Type()
)
sessionStatusHistoryDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryDuration.setStatus("current")


class _SessionStatusHistoryDurationHMS_Type(DisplayString):
    """Custom type sessionStatusHistoryDurationHMS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SessionStatusHistoryDurationHMS_Type.__name__ = "DisplayString"
_SessionStatusHistoryDurationHMS_Object = MibTableColumn
sessionStatusHistoryDurationHMS = _SessionStatusHistoryDurationHMS_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 55),
    _SessionStatusHistoryDurationHMS_Type()
)
sessionStatusHistoryDurationHMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryDurationHMS.setStatus("current")


class _SessionStatusHistorySs7SessionId_Type(DisplayString):
    """Custom type sessionStatusHistorySs7SessionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 41),
    )


_SessionStatusHistorySs7SessionId_Type.__name__ = "DisplayString"
_SessionStatusHistorySs7SessionId_Object = MibTableColumn
sessionStatusHistorySs7SessionId = _SessionStatusHistorySs7SessionId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 56),
    _SessionStatusHistorySs7SessionId_Type()
)
sessionStatusHistorySs7SessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistorySs7SessionId.setStatus("current")
_SessionStatusHistoryModemNumber_Type = Integer32
_SessionStatusHistoryModemNumber_Object = MibTableColumn
sessionStatusHistoryModemNumber = _SessionStatusHistoryModemNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 57),
    _SessionStatusHistoryModemNumber_Type()
)
sessionStatusHistoryModemNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryModemNumber.setStatus("current")


class _SessionStatusHistoryTunnelType_Type(Integer32):
    """Custom type sessionStatusHistoryTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("atmp", 6),
          ("dvs", 5),
          ("l2f", 3),
          ("l2tp", 4),
          ("none", 1),
          ("other", 2),
          ("unknown", 0))
    )


_SessionStatusHistoryTunnelType_Type.__name__ = "Integer32"
_SessionStatusHistoryTunnelType_Object = MibTableColumn
sessionStatusHistoryTunnelType = _SessionStatusHistoryTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 58),
    _SessionStatusHistoryTunnelType_Type()
)
sessionStatusHistoryTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryTunnelType.setStatus("current")


class _SessionStatusHistoryTunnelMediumType_Type(Integer32):
    """Custom type sessionStatusHistoryTunnelMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 3),
          ("none", 1),
          ("other", 2),
          ("unknown", 0))
    )


_SessionStatusHistoryTunnelMediumType_Type.__name__ = "Integer32"
_SessionStatusHistoryTunnelMediumType_Object = MibTableColumn
sessionStatusHistoryTunnelMediumType = _SessionStatusHistoryTunnelMediumType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 59),
    _SessionStatusHistoryTunnelMediumType_Type()
)
sessionStatusHistoryTunnelMediumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryTunnelMediumType.setStatus("current")
_SessionStatusHistoryTunnelServerAddress_Type = IpAddress
_SessionStatusHistoryTunnelServerAddress_Object = MibTableColumn
sessionStatusHistoryTunnelServerAddress = _SessionStatusHistoryTunnelServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 60),
    _SessionStatusHistoryTunnelServerAddress_Type()
)
sessionStatusHistoryTunnelServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryTunnelServerAddress.setStatus("current")
_SessionStatusHistoryCallClass_Type = Integer32
_SessionStatusHistoryCallClass_Object = MibTableColumn
sessionStatusHistoryCallClass = _SessionStatusHistoryCallClass_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 61),
    _SessionStatusHistoryCallClass_Type()
)
sessionStatusHistoryCallClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryCallClass.setStatus("current")
_SessionStatusHistoryTandemPort_Type = Integer32
_SessionStatusHistoryTandemPort_Object = MibTableColumn
sessionStatusHistoryTandemPort = _SessionStatusHistoryTandemPort_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 62),
    _SessionStatusHistoryTandemPort_Type()
)
sessionStatusHistoryTandemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryTandemPort.setStatus("current")
_SessionStatusHistoryTandemTimeslot_Type = Integer32
_SessionStatusHistoryTandemTimeslot_Object = MibTableColumn
sessionStatusHistoryTandemTimeslot = _SessionStatusHistoryTandemTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 63),
    _SessionStatusHistoryTandemTimeslot_Type()
)
sessionStatusHistoryTandemTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryTandemTimeslot.setStatus("current")


class _SessionStatusHistoryCallClassArray_Type(OctetString):
    """Custom type sessionStatusHistoryCallClassArray based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SessionStatusHistoryCallClassArray_Type.__name__ = "OctetString"
_SessionStatusHistoryCallClassArray_Object = MibTableColumn
sessionStatusHistoryCallClassArray = _SessionStatusHistoryCallClassArray_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 64),
    _SessionStatusHistoryCallClassArray_Type()
)
sessionStatusHistoryCallClassArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryCallClassArray.setStatus("current")
_SessionStatusHistoryCallClassLen_Type = Integer32
_SessionStatusHistoryCallClassLen_Object = MibTableColumn
sessionStatusHistoryCallClassLen = _SessionStatusHistoryCallClassLen_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 65),
    _SessionStatusHistoryCallClassLen_Type()
)
sessionStatusHistoryCallClassLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryCallClassLen.setStatus("current")


class _SessionStatusHistoryActualAuthMethod_Type(Integer32):
    """Custom type sessionStatusHistoryActualAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("radius", 1),
          ("remote", 3))
    )


_SessionStatusHistoryActualAuthMethod_Type.__name__ = "Integer32"
_SessionStatusHistoryActualAuthMethod_Object = MibTableColumn
sessionStatusHistoryActualAuthMethod = _SessionStatusHistoryActualAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 66),
    _SessionStatusHistoryActualAuthMethod_Type()
)
sessionStatusHistoryActualAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryActualAuthMethod.setStatus("current")


class _SessionStatusHistoryModemModulation_Type(Integer32):
    """Custom type sessionStatusHistoryModemModulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("bell103", 2),
          ("bell208", 3),
          ("bell212", 4),
          ("k56", 17),
          ("none", 0),
          ("unknown", 1),
          ("v17", 5),
          ("v21", 6),
          ("v22", 7),
          ("v22bis", 8),
          ("v23", 9),
          ("v27", 10),
          ("v29", 11),
          ("v32", 12),
          ("v32bis", 13),
          ("v33", 14),
          ("v34", 15),
          ("v90", 18),
          ("vFC", 16))
    )


_SessionStatusHistoryModemModulation_Type.__name__ = "Integer32"
_SessionStatusHistoryModemModulation_Object = MibTableColumn
sessionStatusHistoryModemModulation = _SessionStatusHistoryModemModulation_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 67),
    _SessionStatusHistoryModemModulation_Type()
)
sessionStatusHistoryModemModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryModemModulation.setStatus("current")


class _SessionStatusHistoryModemErrorCorrection_Type(Integer32):
    """Custom type sessionStatusHistoryModemErrorCorrection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mNP", 2),
          ("none", 0),
          ("unknown", 1),
          ("v42", 3))
    )


_SessionStatusHistoryModemErrorCorrection_Type.__name__ = "Integer32"
_SessionStatusHistoryModemErrorCorrection_Object = MibTableColumn
sessionStatusHistoryModemErrorCorrection = _SessionStatusHistoryModemErrorCorrection_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 68),
    _SessionStatusHistoryModemErrorCorrection_Type()
)
sessionStatusHistoryModemErrorCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryModemErrorCorrection.setStatus("current")


class _SessionStatusHistoryModemDataCompression_Type(Integer32):
    """Custom type sessionStatusHistoryModemDataCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mNP5", 2),
          ("none", 0),
          ("unknown", 1),
          ("v42bis", 3))
    )


_SessionStatusHistoryModemDataCompression_Type.__name__ = "Integer32"
_SessionStatusHistoryModemDataCompression_Object = MibTableColumn
sessionStatusHistoryModemDataCompression = _SessionStatusHistoryModemDataCompression_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 69),
    _SessionStatusHistoryModemDataCompression_Type()
)
sessionStatusHistoryModemDataCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryModemDataCompression.setStatus("current")
_SessionStatusHistoryModemTxBlocks_Type = Integer32
_SessionStatusHistoryModemTxBlocks_Object = MibTableColumn
sessionStatusHistoryModemTxBlocks = _SessionStatusHistoryModemTxBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 70),
    _SessionStatusHistoryModemTxBlocks_Type()
)
sessionStatusHistoryModemTxBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryModemTxBlocks.setStatus("current")
_SessionStatusHistoryModemRetransmits_Type = Integer32
_SessionStatusHistoryModemRetransmits_Object = MibTableColumn
sessionStatusHistoryModemRetransmits = _SessionStatusHistoryModemRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 71),
    _SessionStatusHistoryModemRetransmits_Type()
)
sessionStatusHistoryModemRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryModemRetransmits.setStatus("current")
_SessionStatusHistoryModemSNR_Type = Integer32
_SessionStatusHistoryModemSNR_Object = MibTableColumn
sessionStatusHistoryModemSNR = _SessionStatusHistoryModemSNR_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 72),
    _SessionStatusHistoryModemSNR_Type()
)
sessionStatusHistoryModemSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryModemSNR.setStatus("current")
_SessionStatusHistoryModemLocalRetrains_Type = Integer32
_SessionStatusHistoryModemLocalRetrains_Object = MibTableColumn
sessionStatusHistoryModemLocalRetrains = _SessionStatusHistoryModemLocalRetrains_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 73),
    _SessionStatusHistoryModemLocalRetrains_Type()
)
sessionStatusHistoryModemLocalRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryModemLocalRetrains.setStatus("current")
_SessionStatusHistoryModemRemoteRetrains_Type = Integer32
_SessionStatusHistoryModemRemoteRetrains_Object = MibTableColumn
sessionStatusHistoryModemRemoteRetrains = _SessionStatusHistoryModemRemoteRetrains_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 74),
    _SessionStatusHistoryModemRemoteRetrains_Type()
)
sessionStatusHistoryModemRemoteRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryModemRemoteRetrains.setStatus("current")
_SessionStatusHistoryModemLocalRenegotiations_Type = Integer32
_SessionStatusHistoryModemLocalRenegotiations_Object = MibTableColumn
sessionStatusHistoryModemLocalRenegotiations = _SessionStatusHistoryModemLocalRenegotiations_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 75),
    _SessionStatusHistoryModemLocalRenegotiations_Type()
)
sessionStatusHistoryModemLocalRenegotiations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryModemLocalRenegotiations.setStatus("current")
_SessionStatusHistoryModemRemoteRenegotiations_Type = Integer32
_SessionStatusHistoryModemRemoteRenegotiations_Object = MibTableColumn
sessionStatusHistoryModemRemoteRenegotiations = _SessionStatusHistoryModemRemoteRenegotiations_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 76),
    _SessionStatusHistoryModemRemoteRenegotiations_Type()
)
sessionStatusHistoryModemRemoteRenegotiations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryModemRemoteRenegotiations.setStatus("current")
_SessionStatusHistoryModemReceiveLineLevel_Type = Integer32
_SessionStatusHistoryModemReceiveLineLevel_Object = MibTableColumn
sessionStatusHistoryModemReceiveLineLevel = _SessionStatusHistoryModemReceiveLineLevel_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 77),
    _SessionStatusHistoryModemReceiveLineLevel_Type()
)
sessionStatusHistoryModemReceiveLineLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryModemReceiveLineLevel.setStatus("current")
_SessionStatusHistoryRemoteIPXNetwork_Type = Integer32
_SessionStatusHistoryRemoteIPXNetwork_Object = MibTableColumn
sessionStatusHistoryRemoteIPXNetwork = _SessionStatusHistoryRemoteIPXNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 78),
    _SessionStatusHistoryRemoteIPXNetwork_Type()
)
sessionStatusHistoryRemoteIPXNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryRemoteIPXNetwork.setStatus("current")


class _SessionStatusHistoryRemoteIPXNode_Type(DisplayString):
    """Custom type sessionStatusHistoryRemoteIPXNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SessionStatusHistoryRemoteIPXNode_Type.__name__ = "DisplayString"
_SessionStatusHistoryRemoteIPXNode_Object = MibTableColumn
sessionStatusHistoryRemoteIPXNode = _SessionStatusHistoryRemoteIPXNode_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 79),
    _SessionStatusHistoryRemoteIPXNode_Type()
)
sessionStatusHistoryRemoteIPXNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryRemoteIPXNode.setStatus("current")
_SessionStatusHistoryCleartcpRemoteIP_Type = IpAddress
_SessionStatusHistoryCleartcpRemoteIP_Object = MibTableColumn
sessionStatusHistoryCleartcpRemoteIP = _SessionStatusHistoryCleartcpRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 80),
    _SessionStatusHistoryCleartcpRemoteIP_Type()
)
sessionStatusHistoryCleartcpRemoteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryCleartcpRemoteIP.setStatus("current")
_SessionStatusHistoryCleartcpRemotePort_Type = Integer32
_SessionStatusHistoryCleartcpRemotePort_Object = MibTableColumn
sessionStatusHistoryCleartcpRemotePort = _SessionStatusHistoryCleartcpRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 81),
    _SessionStatusHistoryCleartcpRemotePort_Type()
)
sessionStatusHistoryCleartcpRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryCleartcpRemotePort.setStatus("current")
_SessionStatusHistoryTunnelId_Type = Integer32
_SessionStatusHistoryTunnelId_Object = MibTableColumn
sessionStatusHistoryTunnelId = _SessionStatusHistoryTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 82),
    _SessionStatusHistoryTunnelId_Type()
)
sessionStatusHistoryTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryTunnelId.setStatus("current")
_SessionStatusHistoryLinkId_Type = Integer32
_SessionStatusHistoryLinkId_Object = MibTableColumn
sessionStatusHistoryLinkId = _SessionStatusHistoryLinkId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 107, 1, 83),
    _SessionStatusHistoryLinkId_Type()
)
sessionStatusHistoryLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatusHistoryLinkId.setStatus("current")
_SlotStatusTable_Object = MibTable
slotStatusTable = _SlotStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 201)
)
if mibBuilder.loadTexts:
    slotStatusTable.setStatus("obsolete")
_SlotStatusEntry_Object = MibTableRow
slotStatusEntry = _SlotStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 201, 1)
)
slotStatusEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "slotStatusShelfNumber"),
    (0, "APTIS-MONITOR-MIB", "slotStatusSlotIndex"),
)
if mibBuilder.loadTexts:
    slotStatusEntry.setStatus("current")
_SlotStatusShelfNumber_Type = Integer32
_SlotStatusShelfNumber_Object = MibTableColumn
slotStatusShelfNumber = _SlotStatusShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 201, 1, 1),
    _SlotStatusShelfNumber_Type()
)
slotStatusShelfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusShelfNumber.setStatus("current")


class _SlotStatusSlotIndex_Type(Integer32):
    """Custom type slotStatusSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SlotStatusSlotIndex_Type.__name__ = "Integer32"
_SlotStatusSlotIndex_Object = MibTableColumn
slotStatusSlotIndex = _SlotStatusSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 201, 1, 2),
    _SlotStatusSlotIndex_Type()
)
slotStatusSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusSlotIndex.setStatus("current")


class _SlotStatusSlotStatus_Type(Integer32):
    """Custom type slotStatusSlotStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("slotStatusBadCard", 12),
          ("slotStatusDown", 8),
          ("slotStatusEmpty", 0),
          ("slotStatusFailed", 11),
          ("slotStatusIniting", 6),
          ("slotStatusLoading", 4),
          ("slotStatusNoPower", 1),
          ("slotStatusPresent", 2),
          ("slotStatusPulled", 10),
          ("slotStatusReady", 3),
          ("slotStatusStandby", 13),
          ("slotStatusStarted", 5),
          ("slotStatusUnknown", 9),
          ("slotStatusUp", 7))
    )


_SlotStatusSlotStatus_Type.__name__ = "Integer32"
_SlotStatusSlotStatus_Object = MibTableColumn
slotStatusSlotStatus = _SlotStatusSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 201, 1, 3),
    _SlotStatusSlotStatus_Type()
)
slotStatusSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusSlotStatus.setStatus("current")
_SlotStatusPartNumber_Type = Integer32
_SlotStatusPartNumber_Object = MibTableColumn
slotStatusPartNumber = _SlotStatusPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 201, 1, 4),
    _SlotStatusPartNumber_Type()
)
slotStatusPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusPartNumber.setStatus("current")
_SlotStatusSerialNumber_Type = Integer32
_SlotStatusSerialNumber_Object = MibTableColumn
slotStatusSerialNumber = _SlotStatusSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 201, 1, 5),
    _SlotStatusSerialNumber_Type()
)
slotStatusSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusSerialNumber.setStatus("current")


class _SlotStatusHardwareRev_Type(DisplayString):
    """Custom type slotStatusHardwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SlotStatusHardwareRev_Type.__name__ = "DisplayString"
_SlotStatusHardwareRev_Object = MibTableColumn
slotStatusHardwareRev = _SlotStatusHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 201, 1, 6),
    _SlotStatusHardwareRev_Type()
)
slotStatusHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusHardwareRev.setStatus("current")


class _SlotStatusStiffwareRev_Type(DisplayString):
    """Custom type slotStatusStiffwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SlotStatusStiffwareRev_Type.__name__ = "DisplayString"
_SlotStatusStiffwareRev_Object = MibTableColumn
slotStatusStiffwareRev = _SlotStatusStiffwareRev_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 201, 1, 7),
    _SlotStatusStiffwareRev_Type()
)
slotStatusStiffwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusStiffwareRev.setStatus("current")


class _SlotStatusFirmwareRev_Type(DisplayString):
    """Custom type slotStatusFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SlotStatusFirmwareRev_Type.__name__ = "DisplayString"
_SlotStatusFirmwareRev_Object = MibTableColumn
slotStatusFirmwareRev = _SlotStatusFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 201, 1, 8),
    _SlotStatusFirmwareRev_Type()
)
slotStatusFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusFirmwareRev.setStatus("current")
_SlotStatusSystemMem_Type = Integer32
_SlotStatusSystemMem_Object = MibTableColumn
slotStatusSystemMem = _SlotStatusSystemMem_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 201, 1, 9),
    _SlotStatusSystemMem_Type()
)
slotStatusSystemMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusSystemMem.setStatus("current")
_SlotStatusOtherMem_Type = Integer32
_SlotStatusOtherMem_Object = MibTableColumn
slotStatusOtherMem = _SlotStatusOtherMem_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 201, 1, 10),
    _SlotStatusOtherMem_Type()
)
slotStatusOtherMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusOtherMem.setStatus("current")
_SlotStatusTemperature_Type = Integer32
_SlotStatusTemperature_Object = MibTableColumn
slotStatusTemperature = _SlotStatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 201, 1, 11),
    _SlotStatusTemperature_Type()
)
slotStatusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusTemperature.setStatus("current")


class _SlotStatusSlotType_Type(Integer32):
    """Custom type slotStatusSlotType based on Integer32"""
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
        *(("slotDac", 3),
          ("slotEmpty", 0),
          ("slotMac", 2),
          ("slotScc", 1),
          ("slotUnknown", 4))
    )


_SlotStatusSlotType_Type.__name__ = "Integer32"
_SlotStatusSlotType_Object = MibTableColumn
slotStatusSlotType = _SlotStatusSlotType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 201, 1, 12),
    _SlotStatusSlotType_Type()
)
slotStatusSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusSlotType.setStatus("current")
_SlotStatusSlotOos_Type = Integer32
_SlotStatusSlotOos_Object = MibTableColumn
slotStatusSlotOos = _SlotStatusSlotOos_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 201, 1, 13),
    _SlotStatusSlotOos_Type()
)
slotStatusSlotOos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusSlotOos.setStatus("current")
_SlotStatusServiceModule_Type = Integer32
_SlotStatusServiceModule_Object = MibTableColumn
slotStatusServiceModule = _SlotStatusServiceModule_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 201, 1, 14),
    _SlotStatusServiceModule_Type()
)
slotStatusServiceModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusServiceModule.setStatus("current")


class _SlotStatusLineTerminationModule_Type(Integer32):
    """Custom type slotStatusLineTerminationModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              820121,
              820131,
              820141,
              820151,
              820322,
              820323)
        )
    )
    namedValues = NamedValues(
        *(("dS3", 820121),
          ("dS3P", 820141),
          ("dS3PR", 820151),
          ("dS3R", 820131),
          ("e1", 820323),
          ("ltmEmpty", 0),
          ("t1", 820322))
    )


_SlotStatusLineTerminationModule_Type.__name__ = "Integer32"
_SlotStatusLineTerminationModule_Object = MibTableColumn
slotStatusLineTerminationModule = _SlotStatusLineTerminationModule_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 201, 1, 15),
    _SlotStatusLineTerminationModule_Type()
)
slotStatusLineTerminationModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusLineTerminationModule.setStatus("current")
_SlotStatusNewTable_Object = MibTable
slotStatusNewTable = _SlotStatusNewTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 205)
)
if mibBuilder.loadTexts:
    slotStatusNewTable.setStatus("current")
_SlotStatusNewEntry_Object = MibTableRow
slotStatusNewEntry = _SlotStatusNewEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 205, 1)
)
slotStatusNewEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "slotStatusNewShelfNumber"),
    (0, "APTIS-MONITOR-MIB", "slotStatusNewSlotIndex"),
)
if mibBuilder.loadTexts:
    slotStatusNewEntry.setStatus("current")
_SlotStatusNewShelfNumber_Type = Integer32
_SlotStatusNewShelfNumber_Object = MibTableColumn
slotStatusNewShelfNumber = _SlotStatusNewShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 205, 1, 1),
    _SlotStatusNewShelfNumber_Type()
)
slotStatusNewShelfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusNewShelfNumber.setStatus("current")


class _SlotStatusNewSlotIndex_Type(Integer32):
    """Custom type slotStatusNewSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SlotStatusNewSlotIndex_Type.__name__ = "Integer32"
_SlotStatusNewSlotIndex_Object = MibTableColumn
slotStatusNewSlotIndex = _SlotStatusNewSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 205, 1, 2),
    _SlotStatusNewSlotIndex_Type()
)
slotStatusNewSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusNewSlotIndex.setStatus("current")


class _SlotStatusNewSlotStatus_Type(Integer32):
    """Custom type slotStatusNewSlotStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("slotStatusBadCard", 12),
          ("slotStatusDown", 8),
          ("slotStatusEmpty", 0),
          ("slotStatusFailed", 11),
          ("slotStatusIniting", 6),
          ("slotStatusLoading", 4),
          ("slotStatusNoPower", 1),
          ("slotStatusPresent", 2),
          ("slotStatusPulled", 10),
          ("slotStatusReady", 3),
          ("slotStatusStandby", 13),
          ("slotStatusStarted", 5),
          ("slotStatusUnknown", 9),
          ("slotStatusUp", 7))
    )


_SlotStatusNewSlotStatus_Type.__name__ = "Integer32"
_SlotStatusNewSlotStatus_Object = MibTableColumn
slotStatusNewSlotStatus = _SlotStatusNewSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 205, 1, 3),
    _SlotStatusNewSlotStatus_Type()
)
slotStatusNewSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusNewSlotStatus.setStatus("current")


class _SlotStatusNewSlotType_Type(Integer32):
    """Custom type slotStatusNewSlotType based on Integer32"""
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
        *(("slotDac", 3),
          ("slotEmpty", 0),
          ("slotMac", 2),
          ("slotScc", 1),
          ("slotUnknown", 4))
    )


_SlotStatusNewSlotType_Type.__name__ = "Integer32"
_SlotStatusNewSlotType_Object = MibTableColumn
slotStatusNewSlotType = _SlotStatusNewSlotType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 205, 1, 4),
    _SlotStatusNewSlotType_Type()
)
slotStatusNewSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusNewSlotType.setStatus("current")


class _SlotStatusNewProductCode_Type(DisplayString):
    """Custom type slotStatusNewProductCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_SlotStatusNewProductCode_Type.__name__ = "DisplayString"
_SlotStatusNewProductCode_Object = MibTableColumn
slotStatusNewProductCode = _SlotStatusNewProductCode_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 205, 1, 5),
    _SlotStatusNewProductCode_Type()
)
slotStatusNewProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusNewProductCode.setStatus("current")


class _SlotStatusNewSlotSerialNumber_Type(DisplayString):
    """Custom type slotStatusNewSlotSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SlotStatusNewSlotSerialNumber_Type.__name__ = "DisplayString"
_SlotStatusNewSlotSerialNumber_Object = MibTableColumn
slotStatusNewSlotSerialNumber = _SlotStatusNewSlotSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 205, 1, 6),
    _SlotStatusNewSlotSerialNumber_Type()
)
slotStatusNewSlotSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusNewSlotSerialNumber.setStatus("current")


class _SlotStatusNewFabricationRev_Type(DisplayString):
    """Custom type slotStatusNewFabricationRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_SlotStatusNewFabricationRev_Type.__name__ = "DisplayString"
_SlotStatusNewFabricationRev_Object = MibTableColumn
slotStatusNewFabricationRev = _SlotStatusNewFabricationRev_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 205, 1, 7),
    _SlotStatusNewFabricationRev_Type()
)
slotStatusNewFabricationRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusNewFabricationRev.setStatus("current")


class _SlotStatusNewPalRev_Type(DisplayString):
    """Custom type slotStatusNewPalRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_SlotStatusNewPalRev_Type.__name__ = "DisplayString"
_SlotStatusNewPalRev_Object = MibTableColumn
slotStatusNewPalRev = _SlotStatusNewPalRev_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 205, 1, 8),
    _SlotStatusNewPalRev_Type()
)
slotStatusNewPalRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusNewPalRev.setStatus("current")
_SlotStatusNewReworkRev_Type = Integer32
_SlotStatusNewReworkRev_Object = MibTableColumn
slotStatusNewReworkRev = _SlotStatusNewReworkRev_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 205, 1, 9),
    _SlotStatusNewReworkRev_Type()
)
slotStatusNewReworkRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusNewReworkRev.setStatus("current")


class _SlotStatusNewFirmwareRev_Type(DisplayString):
    """Custom type slotStatusNewFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SlotStatusNewFirmwareRev_Type.__name__ = "DisplayString"
_SlotStatusNewFirmwareRev_Object = MibTableColumn
slotStatusNewFirmwareRev = _SlotStatusNewFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 205, 1, 10),
    _SlotStatusNewFirmwareRev_Type()
)
slotStatusNewFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusNewFirmwareRev.setStatus("current")
_SlotStatusNewTemperature_Type = Integer32
_SlotStatusNewTemperature_Object = MibTableColumn
slotStatusNewTemperature = _SlotStatusNewTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 205, 1, 11),
    _SlotStatusNewTemperature_Type()
)
slotStatusNewTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusNewTemperature.setStatus("current")
_SlotStatusNewSlotOos_Type = Integer32
_SlotStatusNewSlotOos_Object = MibTableColumn
slotStatusNewSlotOos = _SlotStatusNewSlotOos_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 205, 1, 12),
    _SlotStatusNewSlotOos_Type()
)
slotStatusNewSlotOos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusNewSlotOos.setStatus("current")


class _SlotStatusNewLineTerminationModuleType_Type(Integer32):
    """Custom type slotStatusNewLineTerminationModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              820121,
              820131,
              820141,
              820151,
              820322,
              820323,
              820324,
              820325,
              820326,
              820327,
              820328,
              820329)
        )
    )
    namedValues = NamedValues(
        *(("dS3", 820121),
          ("dS3P", 820141),
          ("dS3PR", 820151),
          ("dS3R", 820131),
          ("dS3x2", 820326),
          ("dS3x2P", 820328),
          ("dS3x2PR", 820329),
          ("dS3x2R", 820327),
          ("e1", 820323),
          ("e1x24", 820325),
          ("ltmEmpty", 0),
          ("t1", 820322),
          ("t1x24", 820324))
    )


_SlotStatusNewLineTerminationModuleType_Type.__name__ = "Integer32"
_SlotStatusNewLineTerminationModuleType_Object = MibTableColumn
slotStatusNewLineTerminationModuleType = _SlotStatusNewLineTerminationModuleType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 205, 1, 13),
    _SlotStatusNewLineTerminationModuleType_Type()
)
slotStatusNewLineTerminationModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatusNewLineTerminationModuleType.setStatus("current")
_SessionComponentsTable_Object = MibTable
sessionComponentsTable = _SessionComponentsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 213)
)
if mibBuilder.loadTexts:
    sessionComponentsTable.setStatus("current")
_SessionComponentsEntry_Object = MibTableRow
sessionComponentsEntry = _SessionComponentsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 213, 1)
)
sessionComponentsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "sessionComponentsSessionIndex"),
    (0, "APTIS-MONITOR-MIB", "sessionComponentsIndex"),
)
if mibBuilder.loadTexts:
    sessionComponentsEntry.setStatus("current")
_SessionComponentsSessionIndex_Type = Integer32
_SessionComponentsSessionIndex_Object = MibTableColumn
sessionComponentsSessionIndex = _SessionComponentsSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 213, 1, 1),
    _SessionComponentsSessionIndex_Type()
)
sessionComponentsSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionComponentsSessionIndex.setStatus("current")
_SessionComponentsIndex_Type = Integer32
_SessionComponentsIndex_Object = MibTableColumn
sessionComponentsIndex = _SessionComponentsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 213, 1, 2),
    _SessionComponentsIndex_Type()
)
sessionComponentsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionComponentsIndex.setStatus("current")


class _SessionComponentsComponentType_Type(Integer32):
    """Custom type sessionComponentsComponentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("atmp", 32),
          ("atmptunnel", 33),
          ("chdlc", 9),
          ("cleartcp", 13),
          ("df", 3),
          ("ds0", 4),
          ("dvs", 28),
          ("dvstunnel", 29),
          ("ether", 15),
          ("fax", 30),
          ("fepdf", 17),
          ("fr", 10),
          ("hdlc", 6),
          ("hssi", 22),
          ("ip", 11),
          ("iptest", 34),
          ("l2f", 26),
          ("l2ftunnel", 27),
          ("l2tp", 14),
          ("l2tproute", 31),
          ("lineip", 18),
          ("loopback", 19),
          ("modem", 5),
          ("none", 1),
          ("other", 2),
          ("ppp", 7),
          ("rlogin", 21),
          ("shell", 20),
          ("slip", 8),
          ("sm", 23),
          ("telnet", 12),
          ("trunkip", 16),
          ("unknown", 0),
          ("vl", 24),
          ("voip", 25))
    )


_SessionComponentsComponentType_Type.__name__ = "Integer32"
_SessionComponentsComponentType_Object = MibTableColumn
sessionComponentsComponentType = _SessionComponentsComponentType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 213, 1, 3),
    _SessionComponentsComponentType_Type()
)
sessionComponentsComponentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionComponentsComponentType.setStatus("current")
_SessionComponentsComponentState_Type = Integer32
_SessionComponentsComponentState_Object = MibTableColumn
sessionComponentsComponentState = _SessionComponentsComponentState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 213, 1, 4),
    _SessionComponentsComponentState_Type()
)
sessionComponentsComponentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionComponentsComponentState.setStatus("current")
_SessionComponentsStatHandle_Type = Integer32
_SessionComponentsStatHandle_Object = MibTableColumn
sessionComponentsStatHandle = _SessionComponentsStatHandle_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 213, 1, 5),
    _SessionComponentsStatHandle_Type()
)
sessionComponentsStatHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionComponentsStatHandle.setStatus("current")
_SessionTraceTable_Object = MibTable
sessionTraceTable = _SessionTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 214)
)
if mibBuilder.loadTexts:
    sessionTraceTable.setStatus("current")
_SessionTraceEntry_Object = MibTableRow
sessionTraceEntry = _SessionTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 214, 1)
)
sessionTraceEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "sessionTraceSessionIndex"),
    (0, "APTIS-MONITOR-MIB", "sessionTraceIndex"),
)
if mibBuilder.loadTexts:
    sessionTraceEntry.setStatus("current")
_SessionTraceSessionIndex_Type = Integer32
_SessionTraceSessionIndex_Object = MibTableColumn
sessionTraceSessionIndex = _SessionTraceSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 214, 1, 1),
    _SessionTraceSessionIndex_Type()
)
sessionTraceSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionTraceSessionIndex.setStatus("current")
_SessionTraceIndex_Type = Integer32
_SessionTraceIndex_Object = MibTableColumn
sessionTraceIndex = _SessionTraceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 214, 1, 2),
    _SessionTraceIndex_Type()
)
sessionTraceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionTraceIndex.setStatus("current")
_SessionTraceAbsoluteTimeStamp_Type = Integer32
_SessionTraceAbsoluteTimeStamp_Object = MibTableColumn
sessionTraceAbsoluteTimeStamp = _SessionTraceAbsoluteTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 214, 1, 3),
    _SessionTraceAbsoluteTimeStamp_Type()
)
sessionTraceAbsoluteTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionTraceAbsoluteTimeStamp.setStatus("current")
_SessionTraceRelativeTimeStamp_Type = Integer32
_SessionTraceRelativeTimeStamp_Object = MibTableColumn
sessionTraceRelativeTimeStamp = _SessionTraceRelativeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 214, 1, 4),
    _SessionTraceRelativeTimeStamp_Type()
)
sessionTraceRelativeTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionTraceRelativeTimeStamp.setStatus("current")


class _SessionTraceLogEntry_Type(DisplayString):
    """Custom type sessionTraceLogEntry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SessionTraceLogEntry_Type.__name__ = "DisplayString"
_SessionTraceLogEntry_Object = MibTableColumn
sessionTraceLogEntry = _SessionTraceLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 214, 1, 5),
    _SessionTraceLogEntry_Type()
)
sessionTraceLogEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionTraceLogEntry.setStatus("current")
_SessionSlotsTable_Object = MibTable
sessionSlotsTable = _SessionSlotsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 215)
)
if mibBuilder.loadTexts:
    sessionSlotsTable.setStatus("current")
_SessionSlotsEntry_Object = MibTableRow
sessionSlotsEntry = _SessionSlotsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 215, 1)
)
sessionSlotsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "sessionSlotsTrunkCount"),
)
if mibBuilder.loadTexts:
    sessionSlotsEntry.setStatus("current")
_SessionSlotsTrunkCount_Type = Integer32
_SessionSlotsTrunkCount_Object = MibTableColumn
sessionSlotsTrunkCount = _SessionSlotsTrunkCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 215, 1, 1),
    _SessionSlotsTrunkCount_Type()
)
sessionSlotsTrunkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSlotsTrunkCount.setStatus("current")
_SessionSlotsSlot1Count_Type = Integer32
_SessionSlotsSlot1Count_Object = MibTableColumn
sessionSlotsSlot1Count = _SessionSlotsSlot1Count_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 215, 1, 2),
    _SessionSlotsSlot1Count_Type()
)
sessionSlotsSlot1Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSlotsSlot1Count.setStatus("current")
_SessionSlotsSlot2Count_Type = Integer32
_SessionSlotsSlot2Count_Object = MibTableColumn
sessionSlotsSlot2Count = _SessionSlotsSlot2Count_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 215, 1, 3),
    _SessionSlotsSlot2Count_Type()
)
sessionSlotsSlot2Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSlotsSlot2Count.setStatus("current")
_SessionSlotsSlot3Count_Type = Integer32
_SessionSlotsSlot3Count_Object = MibTableColumn
sessionSlotsSlot3Count = _SessionSlotsSlot3Count_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 215, 1, 4),
    _SessionSlotsSlot3Count_Type()
)
sessionSlotsSlot3Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSlotsSlot3Count.setStatus("current")
_SessionSlotsSlot4Count_Type = Integer32
_SessionSlotsSlot4Count_Object = MibTableColumn
sessionSlotsSlot4Count = _SessionSlotsSlot4Count_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 215, 1, 5),
    _SessionSlotsSlot4Count_Type()
)
sessionSlotsSlot4Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSlotsSlot4Count.setStatus("current")
_SessionSlotsSlot5Count_Type = Integer32
_SessionSlotsSlot5Count_Object = MibTableColumn
sessionSlotsSlot5Count = _SessionSlotsSlot5Count_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 215, 1, 6),
    _SessionSlotsSlot5Count_Type()
)
sessionSlotsSlot5Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSlotsSlot5Count.setStatus("current")
_SessionSlotsSlot6Count_Type = Integer32
_SessionSlotsSlot6Count_Object = MibTableColumn
sessionSlotsSlot6Count = _SessionSlotsSlot6Count_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 215, 1, 7),
    _SessionSlotsSlot6Count_Type()
)
sessionSlotsSlot6Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSlotsSlot6Count.setStatus("current")
_SessionSlotsSlot7Count_Type = Integer32
_SessionSlotsSlot7Count_Object = MibTableColumn
sessionSlotsSlot7Count = _SessionSlotsSlot7Count_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 215, 1, 8),
    _SessionSlotsSlot7Count_Type()
)
sessionSlotsSlot7Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSlotsSlot7Count.setStatus("current")
_SessionSlotsSlot8Count_Type = Integer32
_SessionSlotsSlot8Count_Object = MibTableColumn
sessionSlotsSlot8Count = _SessionSlotsSlot8Count_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 215, 1, 9),
    _SessionSlotsSlot8Count_Type()
)
sessionSlotsSlot8Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSlotsSlot8Count.setStatus("current")
_SessionSlotsSlot9Count_Type = Integer32
_SessionSlotsSlot9Count_Object = MibTableColumn
sessionSlotsSlot9Count = _SessionSlotsSlot9Count_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 215, 1, 10),
    _SessionSlotsSlot9Count_Type()
)
sessionSlotsSlot9Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSlotsSlot9Count.setStatus("current")
_SessionSlotsSlot10Count_Type = Integer32
_SessionSlotsSlot10Count_Object = MibTableColumn
sessionSlotsSlot10Count = _SessionSlotsSlot10Count_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 215, 1, 11),
    _SessionSlotsSlot10Count_Type()
)
sessionSlotsSlot10Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSlotsSlot10Count.setStatus("current")
_SessionSlotsSlot11Count_Type = Integer32
_SessionSlotsSlot11Count_Object = MibTableColumn
sessionSlotsSlot11Count = _SessionSlotsSlot11Count_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 215, 1, 12),
    _SessionSlotsSlot11Count_Type()
)
sessionSlotsSlot11Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSlotsSlot11Count.setStatus("current")
_SessionSlotsSlot12Count_Type = Integer32
_SessionSlotsSlot12Count_Object = MibTableColumn
sessionSlotsSlot12Count = _SessionSlotsSlot12Count_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 215, 1, 13),
    _SessionSlotsSlot12Count_Type()
)
sessionSlotsSlot12Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSlotsSlot12Count.setStatus("current")
_SessionSlotsSlot13Count_Type = Integer32
_SessionSlotsSlot13Count_Object = MibTableColumn
sessionSlotsSlot13Count = _SessionSlotsSlot13Count_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 215, 1, 14),
    _SessionSlotsSlot13Count_Type()
)
sessionSlotsSlot13Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSlotsSlot13Count.setStatus("current")
_SessionSlotsSlot14Count_Type = Integer32
_SessionSlotsSlot14Count_Object = MibTableColumn
sessionSlotsSlot14Count = _SessionSlotsSlot14Count_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 215, 1, 15),
    _SessionSlotsSlot14Count_Type()
)
sessionSlotsSlot14Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSlotsSlot14Count.setStatus("current")
_SessionSlotsSlot15Count_Type = Integer32
_SessionSlotsSlot15Count_Object = MibTableColumn
sessionSlotsSlot15Count = _SessionSlotsSlot15Count_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 215, 1, 16),
    _SessionSlotsSlot15Count_Type()
)
sessionSlotsSlot15Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSlotsSlot15Count.setStatus("current")
_SessionSlotsSlot16Count_Type = Integer32
_SessionSlotsSlot16Count_Object = MibTableColumn
sessionSlotsSlot16Count = _SessionSlotsSlot16Count_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 215, 1, 17),
    _SessionSlotsSlot16Count_Type()
)
sessionSlotsSlot16Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSlotsSlot16Count.setStatus("current")
_SessionSlotsSlot17Count_Type = Integer32
_SessionSlotsSlot17Count_Object = MibTableColumn
sessionSlotsSlot17Count = _SessionSlotsSlot17Count_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 215, 1, 18),
    _SessionSlotsSlot17Count_Type()
)
sessionSlotsSlot17Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSlotsSlot17Count.setStatus("current")
_SessionSlotsSlot18Count_Type = Integer32
_SessionSlotsSlot18Count_Object = MibTableColumn
sessionSlotsSlot18Count = _SessionSlotsSlot18Count_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 215, 1, 19),
    _SessionSlotsSlot18Count_Type()
)
sessionSlotsSlot18Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSlotsSlot18Count.setStatus("current")
_SessionSummaryTable_Object = MibTable
sessionSummaryTable = _SessionSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216)
)
if mibBuilder.loadTexts:
    sessionSummaryTable.setStatus("current")
_SessionSummaryEntry_Object = MibTableRow
sessionSummaryEntry = _SessionSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1)
)
sessionSummaryEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "sessionSummaryActiveUnknown"),
)
if mibBuilder.loadTexts:
    sessionSummaryEntry.setStatus("current")
_SessionSummaryActiveUnknown_Type = Integer32
_SessionSummaryActiveUnknown_Object = MibTableColumn
sessionSummaryActiveUnknown = _SessionSummaryActiveUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 1),
    _SessionSummaryActiveUnknown_Type()
)
sessionSummaryActiveUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryActiveUnknown.setStatus("current")
_SessionSummaryMaximumUnknown_Type = Integer32
_SessionSummaryMaximumUnknown_Object = MibTableColumn
sessionSummaryMaximumUnknown = _SessionSummaryMaximumUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 2),
    _SessionSummaryMaximumUnknown_Type()
)
sessionSummaryMaximumUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryMaximumUnknown.setStatus("current")
_SessionSummaryInactiveUnknown_Type = Integer32
_SessionSummaryInactiveUnknown_Object = MibTableColumn
sessionSummaryInactiveUnknown = _SessionSummaryInactiveUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 3),
    _SessionSummaryInactiveUnknown_Type()
)
sessionSummaryInactiveUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryInactiveUnknown.setStatus("current")
_SessionSummaryActiveNone_Type = Integer32
_SessionSummaryActiveNone_Object = MibTableColumn
sessionSummaryActiveNone = _SessionSummaryActiveNone_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 4),
    _SessionSummaryActiveNone_Type()
)
sessionSummaryActiveNone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryActiveNone.setStatus("current")
_SessionSummaryMaximumNone_Type = Integer32
_SessionSummaryMaximumNone_Object = MibTableColumn
sessionSummaryMaximumNone = _SessionSummaryMaximumNone_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 5),
    _SessionSummaryMaximumNone_Type()
)
sessionSummaryMaximumNone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryMaximumNone.setStatus("current")
_SessionSummaryInactiveNone_Type = Integer32
_SessionSummaryInactiveNone_Object = MibTableColumn
sessionSummaryInactiveNone = _SessionSummaryInactiveNone_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 6),
    _SessionSummaryInactiveNone_Type()
)
sessionSummaryInactiveNone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryInactiveNone.setStatus("current")
_SessionSummaryActiveOther_Type = Integer32
_SessionSummaryActiveOther_Object = MibTableColumn
sessionSummaryActiveOther = _SessionSummaryActiveOther_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 7),
    _SessionSummaryActiveOther_Type()
)
sessionSummaryActiveOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryActiveOther.setStatus("current")
_SessionSummaryMaximumOther_Type = Integer32
_SessionSummaryMaximumOther_Object = MibTableColumn
sessionSummaryMaximumOther = _SessionSummaryMaximumOther_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 8),
    _SessionSummaryMaximumOther_Type()
)
sessionSummaryMaximumOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryMaximumOther.setStatus("current")
_SessionSummaryInactiveOther_Type = Integer32
_SessionSummaryInactiveOther_Object = MibTableColumn
sessionSummaryInactiveOther = _SessionSummaryInactiveOther_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 9),
    _SessionSummaryInactiveOther_Type()
)
sessionSummaryInactiveOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryInactiveOther.setStatus("current")
_SessionSummaryActivePpp_Type = Integer32
_SessionSummaryActivePpp_Object = MibTableColumn
sessionSummaryActivePpp = _SessionSummaryActivePpp_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 10),
    _SessionSummaryActivePpp_Type()
)
sessionSummaryActivePpp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryActivePpp.setStatus("current")
_SessionSummaryMaximumPpp_Type = Integer32
_SessionSummaryMaximumPpp_Object = MibTableColumn
sessionSummaryMaximumPpp = _SessionSummaryMaximumPpp_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 11),
    _SessionSummaryMaximumPpp_Type()
)
sessionSummaryMaximumPpp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryMaximumPpp.setStatus("current")
_SessionSummaryInactivePpp_Type = Integer32
_SessionSummaryInactivePpp_Object = MibTableColumn
sessionSummaryInactivePpp = _SessionSummaryInactivePpp_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 12),
    _SessionSummaryInactivePpp_Type()
)
sessionSummaryInactivePpp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryInactivePpp.setStatus("current")
_SessionSummaryActiveSlip_Type = Integer32
_SessionSummaryActiveSlip_Object = MibTableColumn
sessionSummaryActiveSlip = _SessionSummaryActiveSlip_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 13),
    _SessionSummaryActiveSlip_Type()
)
sessionSummaryActiveSlip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryActiveSlip.setStatus("current")
_SessionSummaryMaximumSlip_Type = Integer32
_SessionSummaryMaximumSlip_Object = MibTableColumn
sessionSummaryMaximumSlip = _SessionSummaryMaximumSlip_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 14),
    _SessionSummaryMaximumSlip_Type()
)
sessionSummaryMaximumSlip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryMaximumSlip.setStatus("current")
_SessionSummaryInactiveSlip_Type = Integer32
_SessionSummaryInactiveSlip_Object = MibTableColumn
sessionSummaryInactiveSlip = _SessionSummaryInactiveSlip_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 15),
    _SessionSummaryInactiveSlip_Type()
)
sessionSummaryInactiveSlip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryInactiveSlip.setStatus("current")
_SessionSummaryActiveFrameRelay_Type = Integer32
_SessionSummaryActiveFrameRelay_Object = MibTableColumn
sessionSummaryActiveFrameRelay = _SessionSummaryActiveFrameRelay_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 16),
    _SessionSummaryActiveFrameRelay_Type()
)
sessionSummaryActiveFrameRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryActiveFrameRelay.setStatus("current")
_SessionSummaryMaximumFrameRelay_Type = Integer32
_SessionSummaryMaximumFrameRelay_Object = MibTableColumn
sessionSummaryMaximumFrameRelay = _SessionSummaryMaximumFrameRelay_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 17),
    _SessionSummaryMaximumFrameRelay_Type()
)
sessionSummaryMaximumFrameRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryMaximumFrameRelay.setStatus("current")
_SessionSummaryInactiveFrameRelay_Type = Integer32
_SessionSummaryInactiveFrameRelay_Object = MibTableColumn
sessionSummaryInactiveFrameRelay = _SessionSummaryInactiveFrameRelay_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 18),
    _SessionSummaryInactiveFrameRelay_Type()
)
sessionSummaryInactiveFrameRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryInactiveFrameRelay.setStatus("current")
_SessionSummaryActiveCiscoHDLC_Type = Integer32
_SessionSummaryActiveCiscoHDLC_Object = MibTableColumn
sessionSummaryActiveCiscoHDLC = _SessionSummaryActiveCiscoHDLC_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 19),
    _SessionSummaryActiveCiscoHDLC_Type()
)
sessionSummaryActiveCiscoHDLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryActiveCiscoHDLC.setStatus("current")
_SessionSummaryMaximumCiscoHDLC_Type = Integer32
_SessionSummaryMaximumCiscoHDLC_Object = MibTableColumn
sessionSummaryMaximumCiscoHDLC = _SessionSummaryMaximumCiscoHDLC_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 20),
    _SessionSummaryMaximumCiscoHDLC_Type()
)
sessionSummaryMaximumCiscoHDLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryMaximumCiscoHDLC.setStatus("current")
_SessionSummaryInactiveCiscoHDLC_Type = Integer32
_SessionSummaryInactiveCiscoHDLC_Object = MibTableColumn
sessionSummaryInactiveCiscoHDLC = _SessionSummaryInactiveCiscoHDLC_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 21),
    _SessionSummaryInactiveCiscoHDLC_Type()
)
sessionSummaryInactiveCiscoHDLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryInactiveCiscoHDLC.setStatus("current")
_SessionSummaryActiveTerminalServer_Type = Integer32
_SessionSummaryActiveTerminalServer_Object = MibTableColumn
sessionSummaryActiveTerminalServer = _SessionSummaryActiveTerminalServer_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 22),
    _SessionSummaryActiveTerminalServer_Type()
)
sessionSummaryActiveTerminalServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryActiveTerminalServer.setStatus("current")
_SessionSummaryMaximumTerminalServer_Type = Integer32
_SessionSummaryMaximumTerminalServer_Object = MibTableColumn
sessionSummaryMaximumTerminalServer = _SessionSummaryMaximumTerminalServer_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 23),
    _SessionSummaryMaximumTerminalServer_Type()
)
sessionSummaryMaximumTerminalServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryMaximumTerminalServer.setStatus("current")
_SessionSummaryInactiveTerminalServer_Type = Integer32
_SessionSummaryInactiveTerminalServer_Object = MibTableColumn
sessionSummaryInactiveTerminalServer = _SessionSummaryInactiveTerminalServer_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 24),
    _SessionSummaryInactiveTerminalServer_Type()
)
sessionSummaryInactiveTerminalServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryInactiveTerminalServer.setStatus("current")
_SessionSummaryActiveTelnet_Type = Integer32
_SessionSummaryActiveTelnet_Object = MibTableColumn
sessionSummaryActiveTelnet = _SessionSummaryActiveTelnet_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 25),
    _SessionSummaryActiveTelnet_Type()
)
sessionSummaryActiveTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryActiveTelnet.setStatus("current")
_SessionSummaryMaximumTelnet_Type = Integer32
_SessionSummaryMaximumTelnet_Object = MibTableColumn
sessionSummaryMaximumTelnet = _SessionSummaryMaximumTelnet_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 26),
    _SessionSummaryMaximumTelnet_Type()
)
sessionSummaryMaximumTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryMaximumTelnet.setStatus("current")
_SessionSummaryInactiveTelnet_Type = Integer32
_SessionSummaryInactiveTelnet_Object = MibTableColumn
sessionSummaryInactiveTelnet = _SessionSummaryInactiveTelnet_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 27),
    _SessionSummaryInactiveTelnet_Type()
)
sessionSummaryInactiveTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryInactiveTelnet.setStatus("current")
_SessionSummaryActiveRawTCP_Type = Integer32
_SessionSummaryActiveRawTCP_Object = MibTableColumn
sessionSummaryActiveRawTCP = _SessionSummaryActiveRawTCP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 28),
    _SessionSummaryActiveRawTCP_Type()
)
sessionSummaryActiveRawTCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryActiveRawTCP.setStatus("current")
_SessionSummaryMaximumRawTCP_Type = Integer32
_SessionSummaryMaximumRawTCP_Object = MibTableColumn
sessionSummaryMaximumRawTCP = _SessionSummaryMaximumRawTCP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 29),
    _SessionSummaryMaximumRawTCP_Type()
)
sessionSummaryMaximumRawTCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryMaximumRawTCP.setStatus("current")
_SessionSummaryInactiveRawTCP_Type = Integer32
_SessionSummaryInactiveRawTCP_Object = MibTableColumn
sessionSummaryInactiveRawTCP = _SessionSummaryInactiveRawTCP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 30),
    _SessionSummaryInactiveRawTCP_Type()
)
sessionSummaryInactiveRawTCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryInactiveRawTCP.setStatus("current")
_SessionSummaryActiveRlogin_Type = Integer32
_SessionSummaryActiveRlogin_Object = MibTableColumn
sessionSummaryActiveRlogin = _SessionSummaryActiveRlogin_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 31),
    _SessionSummaryActiveRlogin_Type()
)
sessionSummaryActiveRlogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryActiveRlogin.setStatus("current")
_SessionSummaryMaximumRlogin_Type = Integer32
_SessionSummaryMaximumRlogin_Object = MibTableColumn
sessionSummaryMaximumRlogin = _SessionSummaryMaximumRlogin_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 32),
    _SessionSummaryMaximumRlogin_Type()
)
sessionSummaryMaximumRlogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryMaximumRlogin.setStatus("current")
_SessionSummaryInactiveRlogin_Type = Integer32
_SessionSummaryInactiveRlogin_Object = MibTableColumn
sessionSummaryInactiveRlogin = _SessionSummaryInactiveRlogin_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 33),
    _SessionSummaryInactiveRlogin_Type()
)
sessionSummaryInactiveRlogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryInactiveRlogin.setStatus("current")
_SessionSummaryActiveL2tp_Type = Integer32
_SessionSummaryActiveL2tp_Object = MibTableColumn
sessionSummaryActiveL2tp = _SessionSummaryActiveL2tp_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 34),
    _SessionSummaryActiveL2tp_Type()
)
sessionSummaryActiveL2tp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryActiveL2tp.setStatus("current")
_SessionSummaryMaximumL2tp_Type = Integer32
_SessionSummaryMaximumL2tp_Object = MibTableColumn
sessionSummaryMaximumL2tp = _SessionSummaryMaximumL2tp_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 35),
    _SessionSummaryMaximumL2tp_Type()
)
sessionSummaryMaximumL2tp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryMaximumL2tp.setStatus("current")
_SessionSummaryInactiveL2tp_Type = Integer32
_SessionSummaryInactiveL2tp_Object = MibTableColumn
sessionSummaryInactiveL2tp = _SessionSummaryInactiveL2tp_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 36),
    _SessionSummaryInactiveL2tp_Type()
)
sessionSummaryInactiveL2tp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryInactiveL2tp.setStatus("current")
_SessionSummaryActiveL2f_Type = Integer32
_SessionSummaryActiveL2f_Object = MibTableColumn
sessionSummaryActiveL2f = _SessionSummaryActiveL2f_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 37),
    _SessionSummaryActiveL2f_Type()
)
sessionSummaryActiveL2f.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryActiveL2f.setStatus("current")
_SessionSummaryMaximumL2f_Type = Integer32
_SessionSummaryMaximumL2f_Object = MibTableColumn
sessionSummaryMaximumL2f = _SessionSummaryMaximumL2f_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 38),
    _SessionSummaryMaximumL2f_Type()
)
sessionSummaryMaximumL2f.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryMaximumL2f.setStatus("current")
_SessionSummaryInactiveL2f_Type = Integer32
_SessionSummaryInactiveL2f_Object = MibTableColumn
sessionSummaryInactiveL2f = _SessionSummaryInactiveL2f_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 39),
    _SessionSummaryInactiveL2f_Type()
)
sessionSummaryInactiveL2f.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryInactiveL2f.setStatus("current")
_SessionSummaryActiveTrunk_Type = Integer32
_SessionSummaryActiveTrunk_Object = MibTableColumn
sessionSummaryActiveTrunk = _SessionSummaryActiveTrunk_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 40),
    _SessionSummaryActiveTrunk_Type()
)
sessionSummaryActiveTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryActiveTrunk.setStatus("current")
_SessionSummaryMaximumTrunk_Type = Integer32
_SessionSummaryMaximumTrunk_Object = MibTableColumn
sessionSummaryMaximumTrunk = _SessionSummaryMaximumTrunk_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 41),
    _SessionSummaryMaximumTrunk_Type()
)
sessionSummaryMaximumTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryMaximumTrunk.setStatus("current")
_SessionSummaryInactiveTrunk_Type = Integer32
_SessionSummaryInactiveTrunk_Object = MibTableColumn
sessionSummaryInactiveTrunk = _SessionSummaryInactiveTrunk_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 42),
    _SessionSummaryInactiveTrunk_Type()
)
sessionSummaryInactiveTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryInactiveTrunk.setStatus("current")
_SessionSummaryActiveVoice_Type = Integer32
_SessionSummaryActiveVoice_Object = MibTableColumn
sessionSummaryActiveVoice = _SessionSummaryActiveVoice_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 43),
    _SessionSummaryActiveVoice_Type()
)
sessionSummaryActiveVoice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryActiveVoice.setStatus("current")
_SessionSummaryMaximumVoice_Type = Integer32
_SessionSummaryMaximumVoice_Object = MibTableColumn
sessionSummaryMaximumVoice = _SessionSummaryMaximumVoice_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 44),
    _SessionSummaryMaximumVoice_Type()
)
sessionSummaryMaximumVoice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryMaximumVoice.setStatus("current")
_SessionSummaryInactiveVoice_Type = Integer32
_SessionSummaryInactiveVoice_Object = MibTableColumn
sessionSummaryInactiveVoice = _SessionSummaryInactiveVoice_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 45),
    _SessionSummaryInactiveVoice_Type()
)
sessionSummaryInactiveVoice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryInactiveVoice.setStatus("current")
_SessionSummaryActiveTandem_Type = Integer32
_SessionSummaryActiveTandem_Object = MibTableColumn
sessionSummaryActiveTandem = _SessionSummaryActiveTandem_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 46),
    _SessionSummaryActiveTandem_Type()
)
sessionSummaryActiveTandem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryActiveTandem.setStatus("current")
_SessionSummaryMaximumTandem_Type = Integer32
_SessionSummaryMaximumTandem_Object = MibTableColumn
sessionSummaryMaximumTandem = _SessionSummaryMaximumTandem_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 47),
    _SessionSummaryMaximumTandem_Type()
)
sessionSummaryMaximumTandem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryMaximumTandem.setStatus("current")
_SessionSummaryInactiveTandem_Type = Integer32
_SessionSummaryInactiveTandem_Object = MibTableColumn
sessionSummaryInactiveTandem = _SessionSummaryInactiveTandem_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 48),
    _SessionSummaryInactiveTandem_Type()
)
sessionSummaryInactiveTandem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryInactiveTandem.setStatus("current")
_SessionSummaryActiveFtp_Type = Integer32
_SessionSummaryActiveFtp_Object = MibTableColumn
sessionSummaryActiveFtp = _SessionSummaryActiveFtp_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 49),
    _SessionSummaryActiveFtp_Type()
)
sessionSummaryActiveFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryActiveFtp.setStatus("current")
_SessionSummaryMaximumFtp_Type = Integer32
_SessionSummaryMaximumFtp_Object = MibTableColumn
sessionSummaryMaximumFtp = _SessionSummaryMaximumFtp_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 50),
    _SessionSummaryMaximumFtp_Type()
)
sessionSummaryMaximumFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryMaximumFtp.setStatus("current")
_SessionSummaryInactiveFtp_Type = Integer32
_SessionSummaryInactiveFtp_Object = MibTableColumn
sessionSummaryInactiveFtp = _SessionSummaryInactiveFtp_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 51),
    _SessionSummaryInactiveFtp_Type()
)
sessionSummaryInactiveFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryInactiveFtp.setStatus("current")
_SessionSummaryActiveDvs_Type = Integer32
_SessionSummaryActiveDvs_Object = MibTableColumn
sessionSummaryActiveDvs = _SessionSummaryActiveDvs_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 52),
    _SessionSummaryActiveDvs_Type()
)
sessionSummaryActiveDvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryActiveDvs.setStatus("current")
_SessionSummaryMaximumDvs_Type = Integer32
_SessionSummaryMaximumDvs_Object = MibTableColumn
sessionSummaryMaximumDvs = _SessionSummaryMaximumDvs_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 53),
    _SessionSummaryMaximumDvs_Type()
)
sessionSummaryMaximumDvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryMaximumDvs.setStatus("current")
_SessionSummaryInactiveDvs_Type = Integer32
_SessionSummaryInactiveDvs_Object = MibTableColumn
sessionSummaryInactiveDvs = _SessionSummaryInactiveDvs_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 54),
    _SessionSummaryInactiveDvs_Type()
)
sessionSummaryInactiveDvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryInactiveDvs.setStatus("current")
_SessionSummaryActiveAtmp_Type = Integer32
_SessionSummaryActiveAtmp_Object = MibTableColumn
sessionSummaryActiveAtmp = _SessionSummaryActiveAtmp_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 55),
    _SessionSummaryActiveAtmp_Type()
)
sessionSummaryActiveAtmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryActiveAtmp.setStatus("current")
_SessionSummaryMaximumAtmp_Type = Integer32
_SessionSummaryMaximumAtmp_Object = MibTableColumn
sessionSummaryMaximumAtmp = _SessionSummaryMaximumAtmp_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 56),
    _SessionSummaryMaximumAtmp_Type()
)
sessionSummaryMaximumAtmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryMaximumAtmp.setStatus("current")
_SessionSummaryInactiveAtmp_Type = Integer32
_SessionSummaryInactiveAtmp_Object = MibTableColumn
sessionSummaryInactiveAtmp = _SessionSummaryInactiveAtmp_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 57),
    _SessionSummaryInactiveAtmp_Type()
)
sessionSummaryInactiveAtmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryInactiveAtmp.setStatus("current")
_SessionSummaryActiveFax_Type = Integer32
_SessionSummaryActiveFax_Object = MibTableColumn
sessionSummaryActiveFax = _SessionSummaryActiveFax_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 58),
    _SessionSummaryActiveFax_Type()
)
sessionSummaryActiveFax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryActiveFax.setStatus("current")
_SessionSummaryMaximumFax_Type = Integer32
_SessionSummaryMaximumFax_Object = MibTableColumn
sessionSummaryMaximumFax = _SessionSummaryMaximumFax_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 59),
    _SessionSummaryMaximumFax_Type()
)
sessionSummaryMaximumFax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryMaximumFax.setStatus("current")
_SessionSummaryInactiveFax_Type = Integer32
_SessionSummaryInactiveFax_Object = MibTableColumn
sessionSummaryInactiveFax = _SessionSummaryInactiveFax_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 60),
    _SessionSummaryInactiveFax_Type()
)
sessionSummaryInactiveFax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryInactiveFax.setStatus("current")
_SessionSummaryActiveHub_Type = Integer32
_SessionSummaryActiveHub_Object = MibTableColumn
sessionSummaryActiveHub = _SessionSummaryActiveHub_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 61),
    _SessionSummaryActiveHub_Type()
)
sessionSummaryActiveHub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryActiveHub.setStatus("current")
_SessionSummaryMaximumHub_Type = Integer32
_SessionSummaryMaximumHub_Object = MibTableColumn
sessionSummaryMaximumHub = _SessionSummaryMaximumHub_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 62),
    _SessionSummaryMaximumHub_Type()
)
sessionSummaryMaximumHub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryMaximumHub.setStatus("current")
_SessionSummaryInactiveHub_Type = Integer32
_SessionSummaryInactiveHub_Object = MibTableColumn
sessionSummaryInactiveHub = _SessionSummaryInactiveHub_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 63),
    _SessionSummaryInactiveHub_Type()
)
sessionSummaryInactiveHub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryInactiveHub.setStatus("current")
_SessionSummaryActiveTest_Type = Integer32
_SessionSummaryActiveTest_Object = MibTableColumn
sessionSummaryActiveTest = _SessionSummaryActiveTest_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 64),
    _SessionSummaryActiveTest_Type()
)
sessionSummaryActiveTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryActiveTest.setStatus("current")
_SessionSummaryMaximumTest_Type = Integer32
_SessionSummaryMaximumTest_Object = MibTableColumn
sessionSummaryMaximumTest = _SessionSummaryMaximumTest_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 65),
    _SessionSummaryMaximumTest_Type()
)
sessionSummaryMaximumTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryMaximumTest.setStatus("current")
_SessionSummaryInactiveTest_Type = Integer32
_SessionSummaryInactiveTest_Object = MibTableColumn
sessionSummaryInactiveTest = _SessionSummaryInactiveTest_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 66),
    _SessionSummaryInactiveTest_Type()
)
sessionSummaryInactiveTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryInactiveTest.setStatus("current")
_SessionSummaryMaximumTotal_Type = Integer32
_SessionSummaryMaximumTotal_Object = MibTableColumn
sessionSummaryMaximumTotal = _SessionSummaryMaximumTotal_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 216, 1, 67),
    _SessionSummaryMaximumTotal_Type()
)
sessionSummaryMaximumTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionSummaryMaximumTotal.setStatus("current")
_SessionMultilinkTable_Object = MibTable
sessionMultilinkTable = _SessionMultilinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 217)
)
if mibBuilder.loadTexts:
    sessionMultilinkTable.setStatus("current")
_SessionMultilinkEntry_Object = MibTableRow
sessionMultilinkEntry = _SessionMultilinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 217, 1)
)
sessionMultilinkEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "sessionMultilinkSessionId"),
)
if mibBuilder.loadTexts:
    sessionMultilinkEntry.setStatus("current")
_SessionMultilinkNegotiated_Type = Integer32
_SessionMultilinkNegotiated_Object = MibTableColumn
sessionMultilinkNegotiated = _SessionMultilinkNegotiated_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 217, 1, 1),
    _SessionMultilinkNegotiated_Type()
)
sessionMultilinkNegotiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionMultilinkNegotiated.setStatus("current")
_SessionMultilinkSessionId_Type = Integer32
_SessionMultilinkSessionId_Object = MibTableColumn
sessionMultilinkSessionId = _SessionMultilinkSessionId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 217, 1, 2),
    _SessionMultilinkSessionId_Type()
)
sessionMultilinkSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionMultilinkSessionId.setStatus("current")
_SessionMultilinkNameLength_Type = Integer32
_SessionMultilinkNameLength_Object = MibTableColumn
sessionMultilinkNameLength = _SessionMultilinkNameLength_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 217, 1, 3),
    _SessionMultilinkNameLength_Type()
)
sessionMultilinkNameLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionMultilinkNameLength.setStatus("current")


class _SessionMultilinkUserName_Type(DisplayString):
    """Custom type sessionMultilinkUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SessionMultilinkUserName_Type.__name__ = "DisplayString"
_SessionMultilinkUserName_Object = MibTableColumn
sessionMultilinkUserName = _SessionMultilinkUserName_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 217, 1, 4),
    _SessionMultilinkUserName_Type()
)
sessionMultilinkUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionMultilinkUserName.setStatus("current")
_SessionMultilinkMyMRRU_Type = Integer32
_SessionMultilinkMyMRRU_Object = MibTableColumn
sessionMultilinkMyMRRU = _SessionMultilinkMyMRRU_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 217, 1, 5),
    _SessionMultilinkMyMRRU_Type()
)
sessionMultilinkMyMRRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionMultilinkMyMRRU.setStatus("current")
_SessionMultilinkPeerMRRU_Type = Integer32
_SessionMultilinkPeerMRRU_Object = MibTableColumn
sessionMultilinkPeerMRRU = _SessionMultilinkPeerMRRU_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 217, 1, 6),
    _SessionMultilinkPeerMRRU_Type()
)
sessionMultilinkPeerMRRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionMultilinkPeerMRRU.setStatus("current")
_SessionMultilinkMyShortSequence_Type = Integer32
_SessionMultilinkMyShortSequence_Object = MibTableColumn
sessionMultilinkMyShortSequence = _SessionMultilinkMyShortSequence_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 217, 1, 7),
    _SessionMultilinkMyShortSequence_Type()
)
sessionMultilinkMyShortSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionMultilinkMyShortSequence.setStatus("current")
_SessionMultilinkPeerShortSequence_Type = Integer32
_SessionMultilinkPeerShortSequence_Object = MibTableColumn
sessionMultilinkPeerShortSequence = _SessionMultilinkPeerShortSequence_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 217, 1, 8),
    _SessionMultilinkPeerShortSequence_Type()
)
sessionMultilinkPeerShortSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionMultilinkPeerShortSequence.setStatus("current")
_SessionMultilinkMyEIDType_Type = Integer32
_SessionMultilinkMyEIDType_Object = MibTableColumn
sessionMultilinkMyEIDType = _SessionMultilinkMyEIDType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 217, 1, 9),
    _SessionMultilinkMyEIDType_Type()
)
sessionMultilinkMyEIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionMultilinkMyEIDType.setStatus("current")
_SessionMultilinkPeerEIDType_Type = Integer32
_SessionMultilinkPeerEIDType_Object = MibTableColumn
sessionMultilinkPeerEIDType = _SessionMultilinkPeerEIDType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 217, 1, 10),
    _SessionMultilinkPeerEIDType_Type()
)
sessionMultilinkPeerEIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionMultilinkPeerEIDType.setStatus("current")
_SessionMultilinkMyEIDLength_Type = Integer32
_SessionMultilinkMyEIDLength_Object = MibTableColumn
sessionMultilinkMyEIDLength = _SessionMultilinkMyEIDLength_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 217, 1, 11),
    _SessionMultilinkMyEIDLength_Type()
)
sessionMultilinkMyEIDLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionMultilinkMyEIDLength.setStatus("current")
_SessionMultilinkPeerEIDLength_Type = Integer32
_SessionMultilinkPeerEIDLength_Object = MibTableColumn
sessionMultilinkPeerEIDLength = _SessionMultilinkPeerEIDLength_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 217, 1, 12),
    _SessionMultilinkPeerEIDLength_Type()
)
sessionMultilinkPeerEIDLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionMultilinkPeerEIDLength.setStatus("current")


class _SessionMultilinkMyEIDData_Type(DisplayString):
    """Custom type sessionMultilinkMyEIDData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SessionMultilinkMyEIDData_Type.__name__ = "DisplayString"
_SessionMultilinkMyEIDData_Object = MibTableColumn
sessionMultilinkMyEIDData = _SessionMultilinkMyEIDData_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 217, 1, 13),
    _SessionMultilinkMyEIDData_Type()
)
sessionMultilinkMyEIDData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionMultilinkMyEIDData.setStatus("current")


class _SessionMultilinkPeerEIDData_Type(DisplayString):
    """Custom type sessionMultilinkPeerEIDData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SessionMultilinkPeerEIDData_Type.__name__ = "DisplayString"
_SessionMultilinkPeerEIDData_Object = MibTableColumn
sessionMultilinkPeerEIDData = _SessionMultilinkPeerEIDData_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 217, 1, 14),
    _SessionMultilinkPeerEIDData_Type()
)
sessionMultilinkPeerEIDData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionMultilinkPeerEIDData.setStatus("current")
_SessionVpopTable_Object = MibTable
sessionVpopTable = _SessionVpopTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 218)
)
if mibBuilder.loadTexts:
    sessionVpopTable.setStatus("current")
_SessionVpopEntry_Object = MibTableRow
sessionVpopEntry = _SessionVpopEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 218, 1)
)
sessionVpopEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "sessionVpopVpopIndex"),
    (0, "APTIS-MONITOR-MIB", "sessionVpopCallType"),
    (0, "APTIS-MONITOR-MIB", "sessionVpopProtocol"),
)
if mibBuilder.loadTexts:
    sessionVpopEntry.setStatus("current")
_SessionVpopVpopIndex_Type = Integer32
_SessionVpopVpopIndex_Object = MibTableColumn
sessionVpopVpopIndex = _SessionVpopVpopIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 218, 1, 1),
    _SessionVpopVpopIndex_Type()
)
sessionVpopVpopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionVpopVpopIndex.setStatus("current")
_SessionVpopVpopId_Type = Integer32
_SessionVpopVpopId_Object = MibTableColumn
sessionVpopVpopId = _SessionVpopVpopId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 218, 1, 2),
    _SessionVpopVpopId_Type()
)
sessionVpopVpopId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionVpopVpopId.setStatus("current")


class _SessionVpopCallType_Type(Integer32):
    """Custom type sessionVpopCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("isdn", 4),
          ("modem", 3),
          ("other", 1),
          ("trunk", 2),
          ("v110", 5),
          ("v120", 6))
    )


_SessionVpopCallType_Type.__name__ = "Integer32"
_SessionVpopCallType_Object = MibTableColumn
sessionVpopCallType = _SessionVpopCallType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 218, 1, 3),
    _SessionVpopCallType_Type()
)
sessionVpopCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionVpopCallType.setStatus("current")


class _SessionVpopProtocol_Type(Integer32):
    """Custom type sessionVpopProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cleartcp", 5),
          ("other", 2),
          ("ppp", 4),
          ("setup", 1),
          ("trunk", 3),
          ("tunnelled", 6))
    )


_SessionVpopProtocol_Type.__name__ = "Integer32"
_SessionVpopProtocol_Object = MibTableColumn
sessionVpopProtocol = _SessionVpopProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 218, 1, 4),
    _SessionVpopProtocol_Type()
)
sessionVpopProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionVpopProtocol.setStatus("current")
_SessionVpopCurrentCount_Type = Integer32
_SessionVpopCurrentCount_Object = MibTableColumn
sessionVpopCurrentCount = _SessionVpopCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 218, 1, 5),
    _SessionVpopCurrentCount_Type()
)
sessionVpopCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionVpopCurrentCount.setStatus("current")
_SessionVpopCurrentDuration_Type = Integer32
_SessionVpopCurrentDuration_Object = MibTableColumn
sessionVpopCurrentDuration = _SessionVpopCurrentDuration_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 218, 1, 6),
    _SessionVpopCurrentDuration_Type()
)
sessionVpopCurrentDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionVpopCurrentDuration.setStatus("current")
_SessionVpopCumulativeCount_Type = Integer32
_SessionVpopCumulativeCount_Object = MibTableColumn
sessionVpopCumulativeCount = _SessionVpopCumulativeCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 218, 1, 7),
    _SessionVpopCumulativeCount_Type()
)
sessionVpopCumulativeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionVpopCumulativeCount.setStatus("current")
_SessionVpopCumulativeDuration_Type = Integer32
_SessionVpopCumulativeDuration_Object = MibTableColumn
sessionVpopCumulativeDuration = _SessionVpopCumulativeDuration_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 218, 1, 8),
    _SessionVpopCumulativeDuration_Type()
)
sessionVpopCumulativeDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionVpopCumulativeDuration.setStatus("current")
_Ss7StatusTable_Object = MibTable
ss7StatusTable = _Ss7StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 500)
)
if mibBuilder.loadTexts:
    ss7StatusTable.setStatus("current")
_Ss7StatusEntry_Object = MibTableRow
ss7StatusEntry = _Ss7StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 500, 1)
)
ss7StatusEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "ss7StatusIndex"),
)
if mibBuilder.loadTexts:
    ss7StatusEntry.setStatus("current")
_Ss7StatusIndex_Type = Integer32
_Ss7StatusIndex_Object = MibTableColumn
ss7StatusIndex = _Ss7StatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 500, 1, 1),
    _Ss7StatusIndex_Type()
)
ss7StatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7StatusIndex.setStatus("current")


class _Ss7StatusState_Type(DisplayString):
    """Custom type ss7StatusState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Ss7StatusState_Type.__name__ = "DisplayString"
_Ss7StatusState_Object = MibTableColumn
ss7StatusState = _Ss7StatusState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 500, 1, 2),
    _Ss7StatusState_Type()
)
ss7StatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7StatusState.setStatus("current")


class _Ss7StatusNetworkId_Type(DisplayString):
    """Custom type ss7StatusNetworkId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_Ss7StatusNetworkId_Type.__name__ = "DisplayString"
_Ss7StatusNetworkId_Object = MibTableColumn
ss7StatusNetworkId = _Ss7StatusNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 500, 1, 3),
    _Ss7StatusNetworkId_Type()
)
ss7StatusNetworkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7StatusNetworkId.setStatus("current")


class _Ss7StatusCalledId_Type(DisplayString):
    """Custom type ss7StatusCalledId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Ss7StatusCalledId_Type.__name__ = "DisplayString"
_Ss7StatusCalledId_Object = MibTableColumn
ss7StatusCalledId = _Ss7StatusCalledId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 500, 1, 4),
    _Ss7StatusCalledId_Type()
)
ss7StatusCalledId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7StatusCalledId.setStatus("current")


class _Ss7StatusCallingId_Type(DisplayString):
    """Custom type ss7StatusCallingId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Ss7StatusCallingId_Type.__name__ = "DisplayString"
_Ss7StatusCallingId_Object = MibTableColumn
ss7StatusCallingId = _Ss7StatusCallingId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 500, 1, 5),
    _Ss7StatusCallingId_Type()
)
ss7StatusCallingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7StatusCallingId.setStatus("current")


class _Ss7StatusCallType_Type(Integer32):
    """Custom type ss7StatusCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("analog", 0),
          ("cotegress", 3),
          ("cotingress", 4),
          ("isdn", 1),
          ("loopback", 2),
          ("t102detect", 7),
          ("t102generate", 6),
          ("t108egress", 8),
          ("tandem", 5))
    )


_Ss7StatusCallType_Type.__name__ = "Integer32"
_Ss7StatusCallType_Object = MibTableColumn
ss7StatusCallType = _Ss7StatusCallType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 500, 1, 6),
    _Ss7StatusCallType_Type()
)
ss7StatusCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7StatusCallType.setStatus("current")
_Ss7StatusSlot_Type = Integer32
_Ss7StatusSlot_Object = MibTableColumn
ss7StatusSlot = _Ss7StatusSlot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 500, 1, 7),
    _Ss7StatusSlot_Type()
)
ss7StatusSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7StatusSlot.setStatus("current")
_Ss7StatusPort_Type = Integer32
_Ss7StatusPort_Object = MibTableColumn
ss7StatusPort = _Ss7StatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 500, 1, 8),
    _Ss7StatusPort_Type()
)
ss7StatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7StatusPort.setStatus("current")
_Ss7StatusTimeSlot_Type = Integer32
_Ss7StatusTimeSlot_Object = MibTableColumn
ss7StatusTimeSlot = _Ss7StatusTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 500, 1, 9),
    _Ss7StatusTimeSlot_Type()
)
ss7StatusTimeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7StatusTimeSlot.setStatus("current")
_Ss7StatusSessionId_Type = Integer32
_Ss7StatusSessionId_Object = MibTableColumn
ss7StatusSessionId = _Ss7StatusSessionId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 500, 1, 10),
    _Ss7StatusSessionId_Type()
)
ss7StatusSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7StatusSessionId.setStatus("current")


class _Ss7StatusServerId_Type(DisplayString):
    """Custom type ss7StatusServerId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 41),
    )


_Ss7StatusServerId_Type.__name__ = "DisplayString"
_Ss7StatusServerId_Object = MibTableColumn
ss7StatusServerId = _Ss7StatusServerId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 500, 1, 11),
    _Ss7StatusServerId_Type()
)
ss7StatusServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7StatusServerId.setStatus("current")
_Ss7StatusStartTime_Type = Integer32
_Ss7StatusStartTime_Object = MibTableColumn
ss7StatusStartTime = _Ss7StatusStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 500, 1, 12),
    _Ss7StatusStartTime_Type()
)
ss7StatusStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7StatusStartTime.setStatus("current")
_Ss7TraceTable_Object = MibTable
ss7TraceTable = _Ss7TraceTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 501)
)
if mibBuilder.loadTexts:
    ss7TraceTable.setStatus("current")
_Ss7TraceEntry_Object = MibTableRow
ss7TraceEntry = _Ss7TraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 501, 1)
)
ss7TraceEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "ss7TraceSs7Index"),
    (0, "APTIS-MONITOR-MIB", "ss7TraceIndex"),
)
if mibBuilder.loadTexts:
    ss7TraceEntry.setStatus("current")
_Ss7TraceSs7Index_Type = Integer32
_Ss7TraceSs7Index_Object = MibTableColumn
ss7TraceSs7Index = _Ss7TraceSs7Index_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 501, 1, 1),
    _Ss7TraceSs7Index_Type()
)
ss7TraceSs7Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7TraceSs7Index.setStatus("current")
_Ss7TraceIndex_Type = Integer32
_Ss7TraceIndex_Object = MibTableColumn
ss7TraceIndex = _Ss7TraceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 501, 1, 2),
    _Ss7TraceIndex_Type()
)
ss7TraceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7TraceIndex.setStatus("current")
_Ss7TraceAbsoluteTimeStamp_Type = Integer32
_Ss7TraceAbsoluteTimeStamp_Object = MibTableColumn
ss7TraceAbsoluteTimeStamp = _Ss7TraceAbsoluteTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 501, 1, 3),
    _Ss7TraceAbsoluteTimeStamp_Type()
)
ss7TraceAbsoluteTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7TraceAbsoluteTimeStamp.setStatus("current")
_Ss7TraceRelativeTimeStamp_Type = Integer32
_Ss7TraceRelativeTimeStamp_Object = MibTableColumn
ss7TraceRelativeTimeStamp = _Ss7TraceRelativeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 501, 1, 4),
    _Ss7TraceRelativeTimeStamp_Type()
)
ss7TraceRelativeTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7TraceRelativeTimeStamp.setStatus("current")


class _Ss7TraceLogEntry_Type(DisplayString):
    """Custom type ss7TraceLogEntry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Ss7TraceLogEntry_Type.__name__ = "DisplayString"
_Ss7TraceLogEntry_Object = MibTableColumn
ss7TraceLogEntry = _Ss7TraceLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 501, 1, 5),
    _Ss7TraceLogEntry_Type()
)
ss7TraceLogEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7TraceLogEntry.setStatus("current")
_Ss7StatusReverseTable_Object = MibTable
ss7StatusReverseTable = _Ss7StatusReverseTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 502)
)
if mibBuilder.loadTexts:
    ss7StatusReverseTable.setStatus("current")
_Ss7StatusReverseEntry_Object = MibTableRow
ss7StatusReverseEntry = _Ss7StatusReverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 502, 1)
)
ss7StatusReverseEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "ss7StatusReverseIndex"),
)
if mibBuilder.loadTexts:
    ss7StatusReverseEntry.setStatus("current")
_Ss7StatusReverseIndex_Type = Integer32
_Ss7StatusReverseIndex_Object = MibTableColumn
ss7StatusReverseIndex = _Ss7StatusReverseIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 502, 1, 1),
    _Ss7StatusReverseIndex_Type()
)
ss7StatusReverseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7StatusReverseIndex.setStatus("current")


class _Ss7StatusReverseState_Type(DisplayString):
    """Custom type ss7StatusReverseState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Ss7StatusReverseState_Type.__name__ = "DisplayString"
_Ss7StatusReverseState_Object = MibTableColumn
ss7StatusReverseState = _Ss7StatusReverseState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 502, 1, 2),
    _Ss7StatusReverseState_Type()
)
ss7StatusReverseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7StatusReverseState.setStatus("current")


class _Ss7StatusReverseNetworkId_Type(DisplayString):
    """Custom type ss7StatusReverseNetworkId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_Ss7StatusReverseNetworkId_Type.__name__ = "DisplayString"
_Ss7StatusReverseNetworkId_Object = MibTableColumn
ss7StatusReverseNetworkId = _Ss7StatusReverseNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 502, 1, 3),
    _Ss7StatusReverseNetworkId_Type()
)
ss7StatusReverseNetworkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7StatusReverseNetworkId.setStatus("current")


class _Ss7StatusReverseCalledId_Type(DisplayString):
    """Custom type ss7StatusReverseCalledId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Ss7StatusReverseCalledId_Type.__name__ = "DisplayString"
_Ss7StatusReverseCalledId_Object = MibTableColumn
ss7StatusReverseCalledId = _Ss7StatusReverseCalledId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 502, 1, 4),
    _Ss7StatusReverseCalledId_Type()
)
ss7StatusReverseCalledId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7StatusReverseCalledId.setStatus("current")


class _Ss7StatusReverseCallingId_Type(DisplayString):
    """Custom type ss7StatusReverseCallingId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Ss7StatusReverseCallingId_Type.__name__ = "DisplayString"
_Ss7StatusReverseCallingId_Object = MibTableColumn
ss7StatusReverseCallingId = _Ss7StatusReverseCallingId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 502, 1, 5),
    _Ss7StatusReverseCallingId_Type()
)
ss7StatusReverseCallingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7StatusReverseCallingId.setStatus("current")


class _Ss7StatusReverseCallType_Type(Integer32):
    """Custom type ss7StatusReverseCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("analog", 0),
          ("cotegress", 3),
          ("cotingress", 4),
          ("isdn", 1),
          ("loopback", 2),
          ("t102detect", 7),
          ("t102generate", 6),
          ("t108egress", 8),
          ("tandem", 5))
    )


_Ss7StatusReverseCallType_Type.__name__ = "Integer32"
_Ss7StatusReverseCallType_Object = MibTableColumn
ss7StatusReverseCallType = _Ss7StatusReverseCallType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 502, 1, 6),
    _Ss7StatusReverseCallType_Type()
)
ss7StatusReverseCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7StatusReverseCallType.setStatus("current")
_Ss7StatusReverseSlot_Type = Integer32
_Ss7StatusReverseSlot_Object = MibTableColumn
ss7StatusReverseSlot = _Ss7StatusReverseSlot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 502, 1, 7),
    _Ss7StatusReverseSlot_Type()
)
ss7StatusReverseSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7StatusReverseSlot.setStatus("current")
_Ss7StatusReversePort_Type = Integer32
_Ss7StatusReversePort_Object = MibTableColumn
ss7StatusReversePort = _Ss7StatusReversePort_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 502, 1, 8),
    _Ss7StatusReversePort_Type()
)
ss7StatusReversePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7StatusReversePort.setStatus("current")
_Ss7StatusReverseTimeSlot_Type = Integer32
_Ss7StatusReverseTimeSlot_Object = MibTableColumn
ss7StatusReverseTimeSlot = _Ss7StatusReverseTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 502, 1, 9),
    _Ss7StatusReverseTimeSlot_Type()
)
ss7StatusReverseTimeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7StatusReverseTimeSlot.setStatus("current")
_Ss7StatusReverseSessionId_Type = Integer32
_Ss7StatusReverseSessionId_Object = MibTableColumn
ss7StatusReverseSessionId = _Ss7StatusReverseSessionId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 502, 1, 10),
    _Ss7StatusReverseSessionId_Type()
)
ss7StatusReverseSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7StatusReverseSessionId.setStatus("current")


class _Ss7StatusReverseServerId_Type(DisplayString):
    """Custom type ss7StatusReverseServerId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 41),
    )


_Ss7StatusReverseServerId_Type.__name__ = "DisplayString"
_Ss7StatusReverseServerId_Object = MibTableColumn
ss7StatusReverseServerId = _Ss7StatusReverseServerId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 502, 1, 11),
    _Ss7StatusReverseServerId_Type()
)
ss7StatusReverseServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7StatusReverseServerId.setStatus("current")
_Ss7StatusReverseStartTime_Type = Integer32
_Ss7StatusReverseStartTime_Object = MibTableColumn
ss7StatusReverseStartTime = _Ss7StatusReverseStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 502, 1, 12),
    _Ss7StatusReverseStartTime_Type()
)
ss7StatusReverseStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7StatusReverseStartTime.setStatus("current")
_Ss7CountersTable_Object = MibTable
ss7CountersTable = _Ss7CountersTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 503)
)
if mibBuilder.loadTexts:
    ss7CountersTable.setStatus("current")
_Ss7CountersEntry_Object = MibTableRow
ss7CountersEntry = _Ss7CountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 503, 1)
)
ss7CountersEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "ss7CountersNumActive"),
)
if mibBuilder.loadTexts:
    ss7CountersEntry.setStatus("current")
_Ss7CountersNumActive_Type = Integer32
_Ss7CountersNumActive_Object = MibTableColumn
ss7CountersNumActive = _Ss7CountersNumActive_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 503, 1, 1),
    _Ss7CountersNumActive_Type()
)
ss7CountersNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7CountersNumActive.setStatus("current")
_Ss7CountersNumInactive_Type = Integer32
_Ss7CountersNumInactive_Object = MibTableColumn
ss7CountersNumInactive = _Ss7CountersNumInactive_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 503, 1, 2),
    _Ss7CountersNumInactive_Type()
)
ss7CountersNumInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7CountersNumInactive.setStatus("current")
_Ss7CountersRetainedFree_Type = Integer32
_Ss7CountersRetainedFree_Object = MibTableColumn
ss7CountersRetainedFree = _Ss7CountersRetainedFree_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 503, 1, 3),
    _Ss7CountersRetainedFree_Type()
)
ss7CountersRetainedFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7CountersRetainedFree.setStatus("current")
_Ss7CountersRetainedFull_Type = Integer32
_Ss7CountersRetainedFull_Object = MibTableColumn
ss7CountersRetainedFull = _Ss7CountersRetainedFull_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 503, 1, 4),
    _Ss7CountersRetainedFull_Type()
)
ss7CountersRetainedFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7CountersRetainedFull.setStatus("current")
_Ss7CountersOneshotFree_Type = Integer32
_Ss7CountersOneshotFree_Object = MibTableColumn
ss7CountersOneshotFree = _Ss7CountersOneshotFree_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 503, 1, 5),
    _Ss7CountersOneshotFree_Type()
)
ss7CountersOneshotFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7CountersOneshotFree.setStatus("current")
_Ss7CountersOneshotFull_Type = Integer32
_Ss7CountersOneshotFull_Object = MibTableColumn
ss7CountersOneshotFull = _Ss7CountersOneshotFull_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 503, 1, 6),
    _Ss7CountersOneshotFull_Type()
)
ss7CountersOneshotFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7CountersOneshotFull.setStatus("current")
_Ss7CountersDsmccFree_Type = Integer32
_Ss7CountersDsmccFree_Object = MibTableColumn
ss7CountersDsmccFree = _Ss7CountersDsmccFree_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 503, 1, 7),
    _Ss7CountersDsmccFree_Type()
)
ss7CountersDsmccFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7CountersDsmccFree.setStatus("current")
_Ss7CountersDsmccFull_Type = Integer32
_Ss7CountersDsmccFull_Object = MibTableColumn
ss7CountersDsmccFull = _Ss7CountersDsmccFull_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 503, 1, 8),
    _Ss7CountersDsmccFull_Type()
)
ss7CountersDsmccFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7CountersDsmccFull.setStatus("current")
_IpdcTraceTable_Object = MibTable
ipdcTraceTable = _IpdcTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 504)
)
if mibBuilder.loadTexts:
    ipdcTraceTable.setStatus("current")
_IpdcTraceEntry_Object = MibTableRow
ipdcTraceEntry = _IpdcTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 504, 1)
)
ipdcTraceEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "ipdcTraceIndex"),
)
if mibBuilder.loadTexts:
    ipdcTraceEntry.setStatus("current")
_IpdcTraceIndex_Type = Integer32
_IpdcTraceIndex_Object = MibTableColumn
ipdcTraceIndex = _IpdcTraceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 504, 1, 1),
    _IpdcTraceIndex_Type()
)
ipdcTraceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipdcTraceIndex.setStatus("current")
_IpdcTraceTimeStamp_Type = Integer32
_IpdcTraceTimeStamp_Object = MibTableColumn
ipdcTraceTimeStamp = _IpdcTraceTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 504, 1, 2),
    _IpdcTraceTimeStamp_Type()
)
ipdcTraceTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipdcTraceTimeStamp.setStatus("current")


class _IpdcTraceDirection_Type(Integer32):
    """Custom type ipdcTraceDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("receive", 1),
          ("transmit", 0))
    )


_IpdcTraceDirection_Type.__name__ = "Integer32"
_IpdcTraceDirection_Object = MibTableColumn
ipdcTraceDirection = _IpdcTraceDirection_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 504, 1, 3),
    _IpdcTraceDirection_Type()
)
ipdcTraceDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipdcTraceDirection.setStatus("current")
_IpdcTraceMsgSize_Type = Integer32
_IpdcTraceMsgSize_Object = MibTableColumn
ipdcTraceMsgSize = _IpdcTraceMsgSize_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 504, 1, 4),
    _IpdcTraceMsgSize_Type()
)
ipdcTraceMsgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipdcTraceMsgSize.setStatus("current")


class _IpdcTraceIpdcMsg_Type(OctetString):
    """Custom type ipdcTraceIpdcMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_IpdcTraceIpdcMsg_Type.__name__ = "OctetString"
_IpdcTraceIpdcMsg_Object = MibTableColumn
ipdcTraceIpdcMsg = _IpdcTraceIpdcMsg_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 504, 1, 5),
    _IpdcTraceIpdcMsg_Type()
)
ipdcTraceIpdcMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipdcTraceIpdcMsg.setStatus("current")
_IpSvcMonitoringTable_Object = MibTable
ipSvcMonitoringTable = _IpSvcMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1102)
)
if mibBuilder.loadTexts:
    ipSvcMonitoringTable.setStatus("current")
_IpSvcMonitoringEntry_Object = MibTableRow
ipSvcMonitoringEntry = _IpSvcMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1102, 1)
)
ipSvcMonitoringEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "ipSvcMonitoringServiceName"),
)
if mibBuilder.loadTexts:
    ipSvcMonitoringEntry.setStatus("current")


class _IpSvcMonitoringServiceName_Type(DisplayString):
    """Custom type ipSvcMonitoringServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpSvcMonitoringServiceName_Type.__name__ = "DisplayString"
_IpSvcMonitoringServiceName_Object = MibTableColumn
ipSvcMonitoringServiceName = _IpSvcMonitoringServiceName_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1102, 1, 1),
    _IpSvcMonitoringServiceName_Type()
)
ipSvcMonitoringServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSvcMonitoringServiceName.setStatus("current")


class _IpSvcMonitoringState_Type(Integer32):
    """Custom type ipSvcMonitoringState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("running", 4),
          ("starting", 3),
          ("stopped", 1),
          ("stopping", 2))
    )


_IpSvcMonitoringState_Type.__name__ = "Integer32"
_IpSvcMonitoringState_Object = MibTableColumn
ipSvcMonitoringState = _IpSvcMonitoringState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1102, 1, 2),
    _IpSvcMonitoringState_Type()
)
ipSvcMonitoringState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSvcMonitoringState.setStatus("current")
_IpSvcMonitoringUptime_Type = Integer32
_IpSvcMonitoringUptime_Object = MibTableColumn
ipSvcMonitoringUptime = _IpSvcMonitoringUptime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1102, 1, 3),
    _IpSvcMonitoringUptime_Type()
)
ipSvcMonitoringUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSvcMonitoringUptime.setStatus("current")
_IpSvcMonitoringRequestsIn_Type = Integer32
_IpSvcMonitoringRequestsIn_Object = MibTableColumn
ipSvcMonitoringRequestsIn = _IpSvcMonitoringRequestsIn_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1102, 1, 10),
    _IpSvcMonitoringRequestsIn_Type()
)
ipSvcMonitoringRequestsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSvcMonitoringRequestsIn.setStatus("current")
_IpSvcMonitoringResponsesOut_Type = Integer32
_IpSvcMonitoringResponsesOut_Object = MibTableColumn
ipSvcMonitoringResponsesOut = _IpSvcMonitoringResponsesOut_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1102, 1, 11),
    _IpSvcMonitoringResponsesOut_Type()
)
ipSvcMonitoringResponsesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSvcMonitoringResponsesOut.setStatus("current")
_IpSvcMonitoringRequestsOut_Type = Integer32
_IpSvcMonitoringRequestsOut_Object = MibTableColumn
ipSvcMonitoringRequestsOut = _IpSvcMonitoringRequestsOut_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1102, 1, 12),
    _IpSvcMonitoringRequestsOut_Type()
)
ipSvcMonitoringRequestsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSvcMonitoringRequestsOut.setStatus("current")
_IpSvcMonitoringResponsesIn_Type = Integer32
_IpSvcMonitoringResponsesIn_Object = MibTableColumn
ipSvcMonitoringResponsesIn = _IpSvcMonitoringResponsesIn_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1102, 1, 13),
    _IpSvcMonitoringResponsesIn_Type()
)
ipSvcMonitoringResponsesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSvcMonitoringResponsesIn.setStatus("current")
_IpSvcMonitoringRequestsInProgress_Type = Integer32
_IpSvcMonitoringRequestsInProgress_Object = MibTableColumn
ipSvcMonitoringRequestsInProgress = _IpSvcMonitoringRequestsInProgress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1102, 1, 14),
    _IpSvcMonitoringRequestsInProgress_Type()
)
ipSvcMonitoringRequestsInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSvcMonitoringRequestsInProgress.setStatus("current")
_IpSvcMonitoringRequestsInError_Type = Integer32
_IpSvcMonitoringRequestsInError_Object = MibTableColumn
ipSvcMonitoringRequestsInError = _IpSvcMonitoringRequestsInError_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1102, 1, 15),
    _IpSvcMonitoringRequestsInError_Type()
)
ipSvcMonitoringRequestsInError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSvcMonitoringRequestsInError.setStatus("current")
_IpSvcMonitoringResponsesInError_Type = Integer32
_IpSvcMonitoringResponsesInError_Object = MibTableColumn
ipSvcMonitoringResponsesInError = _IpSvcMonitoringResponsesInError_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1102, 1, 16),
    _IpSvcMonitoringResponsesInError_Type()
)
ipSvcMonitoringResponsesInError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSvcMonitoringResponsesInError.setStatus("current")
_IpAlarmEntryTable_Object = MibTable
ipAlarmEntryTable = _IpAlarmEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1196)
)
if mibBuilder.loadTexts:
    ipAlarmEntryTable.setStatus("current")
_IpAlarmEntryEntry_Object = MibTableRow
ipAlarmEntryEntry = _IpAlarmEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1196, 1)
)
ipAlarmEntryEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "ipAlarmEntryTrapGenNum"),
)
if mibBuilder.loadTexts:
    ipAlarmEntryEntry.setStatus("current")


class _IpAlarmEntryAlarmType_Type(Integer32):
    """Custom type ipAlarmEntryAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("dhcpAlarm", 16),
          ("ds1Alarm", 3),
          ("ds3Alarm", 4),
          ("enetPortAlarm", 8),
          ("fanAlarm", 14),
          ("flashAlarm", 2),
          ("hssiPortAlarm", 7),
          ("isdnLinkAlarm", 6),
          ("linkAlarm", 5),
          ("macModemsAlarm", 11),
          ("other", 1),
          ("powerAlarm", 15),
          ("slaveSccAlarm", 19),
          ("slaveSccFlashAlarm", 18),
          ("slotAlarm", 13),
          ("slotTempAlarm", 17),
          ("ss7Alarm", 10),
          ("totalModemsAlarm", 12),
          ("tunnelAlarm", 9))
    )


_IpAlarmEntryAlarmType_Type.__name__ = "Integer32"
_IpAlarmEntryAlarmType_Object = MibTableColumn
ipAlarmEntryAlarmType = _IpAlarmEntryAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1196, 1, 1),
    _IpAlarmEntryAlarmType_Type()
)
ipAlarmEntryAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAlarmEntryAlarmType.setStatus("current")


class _IpAlarmEntryTrapGenNum_Type(Integer32):
    """Custom type ipAlarmEntryTrapGenNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpAlarmEntryTrapGenNum_Type.__name__ = "Integer32"
_IpAlarmEntryTrapGenNum_Object = MibTableColumn
ipAlarmEntryTrapGenNum = _IpAlarmEntryTrapGenNum_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1196, 1, 2),
    _IpAlarmEntryTrapGenNum_Type()
)
ipAlarmEntryTrapGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAlarmEntryTrapGenNum.setStatus("current")
_IpAlarmEntryTrapType_Type = Integer32
_IpAlarmEntryTrapType_Object = MibTableColumn
ipAlarmEntryTrapType = _IpAlarmEntryTrapType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1196, 1, 3),
    _IpAlarmEntryTrapType_Type()
)
ipAlarmEntryTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAlarmEntryTrapType.setStatus("current")


class _IpAlarmEntryTrapOID_Type(OctetString):
    """Custom type ipAlarmEntryTrapOID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_IpAlarmEntryTrapOID_Type.__name__ = "OctetString"
_IpAlarmEntryTrapOID_Object = MibTableColumn
ipAlarmEntryTrapOID = _IpAlarmEntryTrapOID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1196, 1, 4),
    _IpAlarmEntryTrapOID_Type()
)
ipAlarmEntryTrapOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAlarmEntryTrapOID.setStatus("current")
_IpAlarmEntryTrapOIDLen_Type = Integer32
_IpAlarmEntryTrapOIDLen_Object = MibTableColumn
ipAlarmEntryTrapOIDLen = _IpAlarmEntryTrapOIDLen_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1196, 1, 5),
    _IpAlarmEntryTrapOIDLen_Type()
)
ipAlarmEntryTrapOIDLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAlarmEntryTrapOIDLen.setStatus("current")


class _IpAlarmEntryTrapSeverity_Type(Integer32):
    """Custom type ipAlarmEntryTrapSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 5),
          ("crit", 4),
          ("emerg", 6),
          ("err", 3),
          ("fatal", 7),
          ("info", 0),
          ("notice", 1),
          ("warning", 2))
    )


_IpAlarmEntryTrapSeverity_Type.__name__ = "Integer32"
_IpAlarmEntryTrapSeverity_Object = MibTableColumn
ipAlarmEntryTrapSeverity = _IpAlarmEntryTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1196, 1, 6),
    _IpAlarmEntryTrapSeverity_Type()
)
ipAlarmEntryTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAlarmEntryTrapSeverity.setStatus("current")
_IpAlarmEntryTrapTimeticks_Type = Integer32
_IpAlarmEntryTrapTimeticks_Object = MibTableColumn
ipAlarmEntryTrapTimeticks = _IpAlarmEntryTrapTimeticks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1196, 1, 7),
    _IpAlarmEntryTrapTimeticks_Type()
)
ipAlarmEntryTrapTimeticks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAlarmEntryTrapTimeticks.setStatus("current")


class _IpAlarmEntryTrapPath_Type(DisplayString):
    """Custom type ipAlarmEntryTrapPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_IpAlarmEntryTrapPath_Type.__name__ = "DisplayString"
_IpAlarmEntryTrapPath_Object = MibTableColumn
ipAlarmEntryTrapPath = _IpAlarmEntryTrapPath_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1196, 1, 8),
    _IpAlarmEntryTrapPath_Type()
)
ipAlarmEntryTrapPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAlarmEntryTrapPath.setStatus("current")


class _IpAlarmEntryTrapArg1_Type(DisplayString):
    """Custom type ipAlarmEntryTrapArg1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_IpAlarmEntryTrapArg1_Type.__name__ = "DisplayString"
_IpAlarmEntryTrapArg1_Object = MibTableColumn
ipAlarmEntryTrapArg1 = _IpAlarmEntryTrapArg1_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1196, 1, 11),
    _IpAlarmEntryTrapArg1_Type()
)
ipAlarmEntryTrapArg1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAlarmEntryTrapArg1.setStatus("current")


class _IpAlarmEntryTrapArg2_Type(DisplayString):
    """Custom type ipAlarmEntryTrapArg2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_IpAlarmEntryTrapArg2_Type.__name__ = "DisplayString"
_IpAlarmEntryTrapArg2_Object = MibTableColumn
ipAlarmEntryTrapArg2 = _IpAlarmEntryTrapArg2_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1196, 1, 12),
    _IpAlarmEntryTrapArg2_Type()
)
ipAlarmEntryTrapArg2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAlarmEntryTrapArg2.setStatus("current")


class _IpAlarmEntryTrapArg3_Type(DisplayString):
    """Custom type ipAlarmEntryTrapArg3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_IpAlarmEntryTrapArg3_Type.__name__ = "DisplayString"
_IpAlarmEntryTrapArg3_Object = MibTableColumn
ipAlarmEntryTrapArg3 = _IpAlarmEntryTrapArg3_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1196, 1, 13),
    _IpAlarmEntryTrapArg3_Type()
)
ipAlarmEntryTrapArg3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAlarmEntryTrapArg3.setStatus("current")


class _IpAlarmEntryTrapGroup_Type(Integer32):
    """Custom type ipAlarmEntryTrapGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cvx", 1),
          ("mib2", 2))
    )


_IpAlarmEntryTrapGroup_Type.__name__ = "Integer32"
_IpAlarmEntryTrapGroup_Object = MibTableColumn
ipAlarmEntryTrapGroup = _IpAlarmEntryTrapGroup_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1196, 1, 14),
    _IpAlarmEntryTrapGroup_Type()
)
ipAlarmEntryTrapGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAlarmEntryTrapGroup.setStatus("current")
_CHdlcStatsTable_Object = MibTable
cHdlcStatsTable = _CHdlcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1211)
)
if mibBuilder.loadTexts:
    cHdlcStatsTable.setStatus("current")
_CHdlcStatsEntry_Object = MibTableRow
cHdlcStatsEntry = _CHdlcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1211, 1)
)
cHdlcStatsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "cHdlcStatsNohdrspaceOut"),
)
if mibBuilder.loadTexts:
    cHdlcStatsEntry.setStatus("current")
_CHdlcStatsNohdrspaceOut_Type = Integer32
_CHdlcStatsNohdrspaceOut_Object = MibTableColumn
cHdlcStatsNohdrspaceOut = _CHdlcStatsNohdrspaceOut_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1211, 1, 1),
    _CHdlcStatsNohdrspaceOut_Type()
)
cHdlcStatsNohdrspaceOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHdlcStatsNohdrspaceOut.setStatus("current")
_CHdlcStatsNomemoryOut_Type = Integer32
_CHdlcStatsNomemoryOut_Object = MibTableColumn
cHdlcStatsNomemoryOut = _CHdlcStatsNomemoryOut_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1211, 1, 2),
    _CHdlcStatsNomemoryOut_Type()
)
cHdlcStatsNomemoryOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHdlcStatsNomemoryOut.setStatus("current")
_CHdlcStatsCiscoFramesOut_Type = Integer32
_CHdlcStatsCiscoFramesOut_Object = MibTableColumn
cHdlcStatsCiscoFramesOut = _CHdlcStatsCiscoFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1211, 1, 3),
    _CHdlcStatsCiscoFramesOut_Type()
)
cHdlcStatsCiscoFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHdlcStatsCiscoFramesOut.setStatus("current")
_CHdlcStatsKeepalivesIn_Type = Integer32
_CHdlcStatsKeepalivesIn_Object = MibTableColumn
cHdlcStatsKeepalivesIn = _CHdlcStatsKeepalivesIn_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1211, 1, 4),
    _CHdlcStatsKeepalivesIn_Type()
)
cHdlcStatsKeepalivesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHdlcStatsKeepalivesIn.setStatus("current")
_CHdlcStatsUnknownProtocolIn_Type = Integer32
_CHdlcStatsUnknownProtocolIn_Object = MibTableColumn
cHdlcStatsUnknownProtocolIn = _CHdlcStatsUnknownProtocolIn_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1211, 1, 5),
    _CHdlcStatsUnknownProtocolIn_Type()
)
cHdlcStatsUnknownProtocolIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHdlcStatsUnknownProtocolIn.setStatus("current")
_CHdlcStatsShortFramesIn_Type = Integer32
_CHdlcStatsShortFramesIn_Object = MibTableColumn
cHdlcStatsShortFramesIn = _CHdlcStatsShortFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1211, 1, 6),
    _CHdlcStatsShortFramesIn_Type()
)
cHdlcStatsShortFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHdlcStatsShortFramesIn.setStatus("current")
_CHdlcStatsPppFramesIn_Type = Integer32
_CHdlcStatsPppFramesIn_Object = MibTableColumn
cHdlcStatsPppFramesIn = _CHdlcStatsPppFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1211, 1, 7),
    _CHdlcStatsPppFramesIn_Type()
)
cHdlcStatsPppFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHdlcStatsPppFramesIn.setStatus("current")
_CHdlcStatsUnknownFramesIn_Type = Integer32
_CHdlcStatsUnknownFramesIn_Object = MibTableColumn
cHdlcStatsUnknownFramesIn = _CHdlcStatsUnknownFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1211, 1, 8),
    _CHdlcStatsUnknownFramesIn_Type()
)
cHdlcStatsUnknownFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHdlcStatsUnknownFramesIn.setStatus("current")
_CHdlcStatsUnknownCiscoTypeIn_Type = Integer32
_CHdlcStatsUnknownCiscoTypeIn_Object = MibTableColumn
cHdlcStatsUnknownCiscoTypeIn = _CHdlcStatsUnknownCiscoTypeIn_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1211, 1, 9),
    _CHdlcStatsUnknownCiscoTypeIn_Type()
)
cHdlcStatsUnknownCiscoTypeIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHdlcStatsUnknownCiscoTypeIn.setStatus("current")
_CHdlcStatsCiscoFramesIn_Type = Integer32
_CHdlcStatsCiscoFramesIn_Object = MibTableColumn
cHdlcStatsCiscoFramesIn = _CHdlcStatsCiscoFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1211, 1, 10),
    _CHdlcStatsCiscoFramesIn_Type()
)
cHdlcStatsCiscoFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHdlcStatsCiscoFramesIn.setStatus("current")
_IpStubStatsTable_Object = MibTable
ipStubStatsTable = _IpStubStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1221)
)
if mibBuilder.loadTexts:
    ipStubStatsTable.setStatus("current")
_IpStubStatsEntry_Object = MibTableRow
ipStubStatsEntry = _IpStubStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1221, 1)
)
ipStubStatsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "ipStubStatsIgmpInMsgs"),
)
if mibBuilder.loadTexts:
    ipStubStatsEntry.setStatus("current")
_IpStubStatsIgmpInMsgs_Type = Integer32
_IpStubStatsIgmpInMsgs_Object = MibTableColumn
ipStubStatsIgmpInMsgs = _IpStubStatsIgmpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1221, 1, 1),
    _IpStubStatsIgmpInMsgs_Type()
)
ipStubStatsIgmpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStubStatsIgmpInMsgs.setStatus("current")
_IpStubStatsIgmpInErrors_Type = Integer32
_IpStubStatsIgmpInErrors_Object = MibTableColumn
ipStubStatsIgmpInErrors = _IpStubStatsIgmpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1221, 1, 2),
    _IpStubStatsIgmpInErrors_Type()
)
ipStubStatsIgmpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStubStatsIgmpInErrors.setStatus("current")
_IpStubStatsIgmpInReports_Type = Integer32
_IpStubStatsIgmpInReports_Object = MibTableColumn
ipStubStatsIgmpInReports = _IpStubStatsIgmpInReports_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1221, 1, 3),
    _IpStubStatsIgmpInReports_Type()
)
ipStubStatsIgmpInReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStubStatsIgmpInReports.setStatus("current")
_IpStubStatsIgmpInQueries_Type = Integer32
_IpStubStatsIgmpInQueries_Object = MibTableColumn
ipStubStatsIgmpInQueries = _IpStubStatsIgmpInQueries_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1221, 1, 4),
    _IpStubStatsIgmpInQueries_Type()
)
ipStubStatsIgmpInQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStubStatsIgmpInQueries.setStatus("current")
_IpStubStatsIgmpUnknownType_Type = Integer32
_IpStubStatsIgmpUnknownType_Object = MibTableColumn
ipStubStatsIgmpUnknownType = _IpStubStatsIgmpUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1221, 1, 5),
    _IpStubStatsIgmpUnknownType_Type()
)
ipStubStatsIgmpUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStubStatsIgmpUnknownType.setStatus("current")
_IpStubStatsIgmpOutMsgs_Type = Integer32
_IpStubStatsIgmpOutMsgs_Object = MibTableColumn
ipStubStatsIgmpOutMsgs = _IpStubStatsIgmpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1221, 1, 6),
    _IpStubStatsIgmpOutMsgs_Type()
)
ipStubStatsIgmpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStubStatsIgmpOutMsgs.setStatus("current")
_IpStubStatsNomemoryOut_Type = Integer32
_IpStubStatsNomemoryOut_Object = MibTableColumn
ipStubStatsNomemoryOut = _IpStubStatsNomemoryOut_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1221, 1, 7),
    _IpStubStatsNomemoryOut_Type()
)
ipStubStatsNomemoryOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStubStatsNomemoryOut.setStatus("current")
_IpCleartcpStatsTable_Object = MibTable
ipCleartcpStatsTable = _IpCleartcpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1231)
)
if mibBuilder.loadTexts:
    ipCleartcpStatsTable.setStatus("current")
_IpCleartcpStatsEntry_Object = MibTableRow
ipCleartcpStatsEntry = _IpCleartcpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1231, 1)
)
ipCleartcpStatsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "ipCleartcpStatsInputQfull"),
)
if mibBuilder.loadTexts:
    ipCleartcpStatsEntry.setStatus("current")
_IpCleartcpStatsInputQfull_Type = Integer32
_IpCleartcpStatsInputQfull_Object = MibTableColumn
ipCleartcpStatsInputQfull = _IpCleartcpStatsInputQfull_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1231, 1, 1),
    _IpCleartcpStatsInputQfull_Type()
)
ipCleartcpStatsInputQfull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCleartcpStatsInputQfull.setStatus("current")
_IpCleartcpStatsInputTcpfull_Type = Integer32
_IpCleartcpStatsInputTcpfull_Object = MibTableColumn
ipCleartcpStatsInputTcpfull = _IpCleartcpStatsInputTcpfull_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1231, 1, 2),
    _IpCleartcpStatsInputTcpfull_Type()
)
ipCleartcpStatsInputTcpfull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCleartcpStatsInputTcpfull.setStatus("current")
_IpCleartcpStatsInputDroppedBytes_Type = Integer32
_IpCleartcpStatsInputDroppedBytes_Object = MibTableColumn
ipCleartcpStatsInputDroppedBytes = _IpCleartcpStatsInputDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1231, 1, 3),
    _IpCleartcpStatsInputDroppedBytes_Type()
)
ipCleartcpStatsInputDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCleartcpStatsInputDroppedBytes.setStatus("current")
_IpCleartcpStatsInputBytes_Type = Integer32
_IpCleartcpStatsInputBytes_Object = MibTableColumn
ipCleartcpStatsInputBytes = _IpCleartcpStatsInputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1231, 1, 4),
    _IpCleartcpStatsInputBytes_Type()
)
ipCleartcpStatsInputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCleartcpStatsInputBytes.setStatus("current")
_IpCleartcpStatsOutputQfull_Type = Integer32
_IpCleartcpStatsOutputQfull_Object = MibTableColumn
ipCleartcpStatsOutputQfull = _IpCleartcpStatsOutputQfull_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1231, 1, 5),
    _IpCleartcpStatsOutputQfull_Type()
)
ipCleartcpStatsOutputQfull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCleartcpStatsOutputQfull.setStatus("current")
_IpCleartcpStatsOutputDroppedBytes_Type = Integer32
_IpCleartcpStatsOutputDroppedBytes_Object = MibTableColumn
ipCleartcpStatsOutputDroppedBytes = _IpCleartcpStatsOutputDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1231, 1, 6),
    _IpCleartcpStatsOutputDroppedBytes_Type()
)
ipCleartcpStatsOutputDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCleartcpStatsOutputDroppedBytes.setStatus("current")
_IpCleartcpStatsOutputBytes_Type = Integer32
_IpCleartcpStatsOutputBytes_Object = MibTableColumn
ipCleartcpStatsOutputBytes = _IpCleartcpStatsOutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1231, 1, 7),
    _IpCleartcpStatsOutputBytes_Type()
)
ipCleartcpStatsOutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCleartcpStatsOutputBytes.setStatus("current")
_PppLogEntryTable_Object = MibTable
pppLogEntryTable = _PppLogEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1316)
)
if mibBuilder.loadTexts:
    pppLogEntryTable.setStatus("current")
_PppLogEntryEntry_Object = MibTableRow
pppLogEntryEntry = _PppLogEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1316, 1)
)
pppLogEntryEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "pppLogEntrySessionId"),
    (0, "APTIS-MONITOR-MIB", "pppLogEntryIndex"),
)
if mibBuilder.loadTexts:
    pppLogEntryEntry.setStatus("current")
_PppLogEntrySessionId_Type = Integer32
_PppLogEntrySessionId_Object = MibTableColumn
pppLogEntrySessionId = _PppLogEntrySessionId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1316, 1, 1),
    _PppLogEntrySessionId_Type()
)
pppLogEntrySessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLogEntrySessionId.setStatus("current")
_PppLogEntryIndex_Type = Integer32
_PppLogEntryIndex_Object = MibTableColumn
pppLogEntryIndex = _PppLogEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1316, 1, 2),
    _PppLogEntryIndex_Type()
)
pppLogEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLogEntryIndex.setStatus("current")
_PppLogEntryMinIndex_Type = Integer32
_PppLogEntryMinIndex_Object = MibTableColumn
pppLogEntryMinIndex = _PppLogEntryMinIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1316, 1, 3),
    _PppLogEntryMinIndex_Type()
)
pppLogEntryMinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLogEntryMinIndex.setStatus("current")
_PppLogEntryMaxIndex_Type = Integer32
_PppLogEntryMaxIndex_Object = MibTableColumn
pppLogEntryMaxIndex = _PppLogEntryMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1316, 1, 4),
    _PppLogEntryMaxIndex_Type()
)
pppLogEntryMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLogEntryMaxIndex.setStatus("current")


class _PppLogEntryEntryText_Type(OctetString):
    """Custom type pppLogEntryEntryText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_PppLogEntryEntryText_Type.__name__ = "OctetString"
_PppLogEntryEntryText_Object = MibTableColumn
pppLogEntryEntryText = _PppLogEntryEntryText_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1316, 1, 5),
    _PppLogEntryEntryText_Type()
)
pppLogEntryEntryText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLogEntryEntryText.setStatus("current")


class _PppLogEntryRawEntryText_Type(OctetString):
    """Custom type pppLogEntryRawEntryText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_PppLogEntryRawEntryText_Type.__name__ = "OctetString"
_PppLogEntryRawEntryText_Object = MibTableColumn
pppLogEntryRawEntryText = _PppLogEntryRawEntryText_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1316, 1, 6),
    _PppLogEntryRawEntryText_Type()
)
pppLogEntryRawEntryText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLogEntryRawEntryText.setStatus("current")
_PppDeadLogEntryTable_Object = MibTable
pppDeadLogEntryTable = _PppDeadLogEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1317)
)
if mibBuilder.loadTexts:
    pppDeadLogEntryTable.setStatus("current")
_PppDeadLogEntryEntry_Object = MibTableRow
pppDeadLogEntryEntry = _PppDeadLogEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1317, 1)
)
pppDeadLogEntryEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "pppDeadLogEntryIndex"),
)
if mibBuilder.loadTexts:
    pppDeadLogEntryEntry.setStatus("current")
_PppDeadLogEntrySessionId_Type = Integer32
_PppDeadLogEntrySessionId_Object = MibTableColumn
pppDeadLogEntrySessionId = _PppDeadLogEntrySessionId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1317, 1, 1),
    _PppDeadLogEntrySessionId_Type()
)
pppDeadLogEntrySessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadLogEntrySessionId.setStatus("current")
_PppDeadLogEntryIndex_Type = Integer32
_PppDeadLogEntryIndex_Object = MibTableColumn
pppDeadLogEntryIndex = _PppDeadLogEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1317, 1, 2),
    _PppDeadLogEntryIndex_Type()
)
pppDeadLogEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadLogEntryIndex.setStatus("current")
_PppDeadLogEntryMinIndex_Type = Integer32
_PppDeadLogEntryMinIndex_Object = MibTableColumn
pppDeadLogEntryMinIndex = _PppDeadLogEntryMinIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1317, 1, 3),
    _PppDeadLogEntryMinIndex_Type()
)
pppDeadLogEntryMinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadLogEntryMinIndex.setStatus("current")
_PppDeadLogEntryMaxIndex_Type = Integer32
_PppDeadLogEntryMaxIndex_Object = MibTableColumn
pppDeadLogEntryMaxIndex = _PppDeadLogEntryMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1317, 1, 4),
    _PppDeadLogEntryMaxIndex_Type()
)
pppDeadLogEntryMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadLogEntryMaxIndex.setStatus("current")


class _PppDeadLogEntryEntryText_Type(OctetString):
    """Custom type pppDeadLogEntryEntryText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_PppDeadLogEntryEntryText_Type.__name__ = "OctetString"
_PppDeadLogEntryEntryText_Object = MibTableColumn
pppDeadLogEntryEntryText = _PppDeadLogEntryEntryText_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1317, 1, 5),
    _PppDeadLogEntryEntryText_Type()
)
pppDeadLogEntryEntryText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadLogEntryEntryText.setStatus("current")


class _PppDeadLogEntryRawEntryText_Type(OctetString):
    """Custom type pppDeadLogEntryRawEntryText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_PppDeadLogEntryRawEntryText_Type.__name__ = "OctetString"
_PppDeadLogEntryRawEntryText_Object = MibTableColumn
pppDeadLogEntryRawEntryText = _PppDeadLogEntryRawEntryText_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1317, 1, 6),
    _PppDeadLogEntryRawEntryText_Type()
)
pppDeadLogEntryRawEntryText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadLogEntryRawEntryText.setStatus("current")
_PppSessionStatsTable_Object = MibTable
pppSessionStatsTable = _PppSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318)
)
if mibBuilder.loadTexts:
    pppSessionStatsTable.setStatus("current")
_PppSessionStatsEntry_Object = MibTableRow
pppSessionStatsEntry = _PppSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1)
)
pppSessionStatsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "pppSessionStatsSessionID"),
)
if mibBuilder.loadTexts:
    pppSessionStatsEntry.setStatus("current")
_PppSessionStatsSessionID_Type = Integer32
_PppSessionStatsSessionID_Object = MibTableColumn
pppSessionStatsSessionID = _PppSessionStatsSessionID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1),
    _PppSessionStatsSessionID_Type()
)
pppSessionStatsSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsSessionID.setStatus("current")


class _PppSessionStatsPhase_Type(Integer32):
    """Custom type pppSessionStatsPhase based on Integer32"""
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
        *(("auth", 2),
          ("establish", 1),
          ("idle", 0),
          ("network", 3),
          ("terminate", 4))
    )


_PppSessionStatsPhase_Type.__name__ = "Integer32"
_PppSessionStatsPhase_Object = MibTableColumn
pppSessionStatsPhase = _PppSessionStatsPhase_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 2),
    _PppSessionStatsPhase_Type()
)
pppSessionStatsPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsPhase.setStatus("current")


class _PppSessionStatsUserName_Type(DisplayString):
    """Custom type pppSessionStatsUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PppSessionStatsUserName_Type.__name__ = "DisplayString"
_PppSessionStatsUserName_Object = MibTableColumn
pppSessionStatsUserName = _PppSessionStatsUserName_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 3),
    _PppSessionStatsUserName_Type()
)
pppSessionStatsUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsUserName.setStatus("current")
_PppSessionStatsUpTime_Type = Integer32
_PppSessionStatsUpTime_Object = MibTableColumn
pppSessionStatsUpTime = _PppSessionStatsUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 4),
    _PppSessionStatsUpTime_Type()
)
pppSessionStatsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsUpTime.setStatus("current")
_PppSessionStatsConnectLimit_Type = Integer32
_PppSessionStatsConnectLimit_Object = MibTableColumn
pppSessionStatsConnectLimit = _PppSessionStatsConnectLimit_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 5),
    _PppSessionStatsConnectLimit_Type()
)
pppSessionStatsConnectLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsConnectLimit.setStatus("current")
_PppSessionStatsRemainingTime_Type = Integer32
_PppSessionStatsRemainingTime_Object = MibTableColumn
pppSessionStatsRemainingTime = _PppSessionStatsRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 6),
    _PppSessionStatsRemainingTime_Type()
)
pppSessionStatsRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRemainingTime.setStatus("current")
_PppSessionStatsInactivityLimit_Type = Integer32
_PppSessionStatsInactivityLimit_Object = MibTableColumn
pppSessionStatsInactivityLimit = _PppSessionStatsInactivityLimit_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 7),
    _PppSessionStatsInactivityLimit_Type()
)
pppSessionStatsInactivityLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsInactivityLimit.setStatus("current")
_PppSessionStatsInactivityRemaining_Type = Integer32
_PppSessionStatsInactivityRemaining_Object = MibTableColumn
pppSessionStatsInactivityRemaining = _PppSessionStatsInactivityRemaining_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 8),
    _PppSessionStatsInactivityRemaining_Type()
)
pppSessionStatsInactivityRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsInactivityRemaining.setStatus("current")
_PppSessionStatsDeadSession_Type = Boolean
_PppSessionStatsDeadSession_Object = MibTableColumn
pppSessionStatsDeadSession = _PppSessionStatsDeadSession_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 9),
    _PppSessionStatsDeadSession_Type()
)
pppSessionStatsDeadSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsDeadSession.setStatus("current")


class _PppSessionStatsInterfaceType_Type(Integer32):
    """Custom type pppSessionStatsInterfaceType based on Integer32"""
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
        *(("hssi", 4),
          ("isdn", 2),
          ("leased", 3),
          ("modem", 1),
          ("unknown", 0))
    )


_PppSessionStatsInterfaceType_Type.__name__ = "Integer32"
_PppSessionStatsInterfaceType_Object = MibTableColumn
pppSessionStatsInterfaceType = _PppSessionStatsInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 101),
    _PppSessionStatsInterfaceType_Type()
)
pppSessionStatsInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsInterfaceType.setStatus("current")
_PppSessionStatsTxSpeed_Type = Integer32
_PppSessionStatsTxSpeed_Object = MibTableColumn
pppSessionStatsTxSpeed = _PppSessionStatsTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 102),
    _PppSessionStatsTxSpeed_Type()
)
pppSessionStatsTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsTxSpeed.setStatus("current")
_PppSessionStatsRxSpeed_Type = Integer32
_PppSessionStatsRxSpeed_Object = MibTableColumn
pppSessionStatsRxSpeed = _PppSessionStatsRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 103),
    _PppSessionStatsRxSpeed_Type()
)
pppSessionStatsRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRxSpeed.setStatus("current")


class _PppSessionStatsLCPState_Type(Integer32):
    """Custom type pppSessionStatsLCPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ackRcvd", 7),
          ("ackSent", 8),
          ("closed", 2),
          ("closing", 4),
          ("initial", 0),
          ("opened", 9),
          ("reqSent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_PppSessionStatsLCPState_Type.__name__ = "Integer32"
_PppSessionStatsLCPState_Object = MibTableColumn
pppSessionStatsLCPState = _PppSessionStatsLCPState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 201),
    _PppSessionStatsLCPState_Type()
)
pppSessionStatsLCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsLCPState.setStatus("current")
_PppSessionStatsLocalMRU_Type = Integer32
_PppSessionStatsLocalMRU_Object = MibTableColumn
pppSessionStatsLocalMRU = _PppSessionStatsLocalMRU_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 202),
    _PppSessionStatsLocalMRU_Type()
)
pppSessionStatsLocalMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsLocalMRU.setStatus("current")
_PppSessionStatsRemoteMRU_Type = Integer32
_PppSessionStatsRemoteMRU_Object = MibTableColumn
pppSessionStatsRemoteMRU = _PppSessionStatsRemoteMRU_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 203),
    _PppSessionStatsRemoteMRU_Type()
)
pppSessionStatsRemoteMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRemoteMRU.setStatus("current")


class _PppSessionStatsLocalAuthProtocol_Type(Integer32):
    """Custom type pppSessionStatsLocalAuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              49187,
              49699)
        )
    )
    namedValues = NamedValues(
        *(("chap", 49699),
          ("none", 0),
          ("pap", 49187))
    )


_PppSessionStatsLocalAuthProtocol_Type.__name__ = "Integer32"
_PppSessionStatsLocalAuthProtocol_Object = MibTableColumn
pppSessionStatsLocalAuthProtocol = _PppSessionStatsLocalAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 204),
    _PppSessionStatsLocalAuthProtocol_Type()
)
pppSessionStatsLocalAuthProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsLocalAuthProtocol.setStatus("current")


class _PppSessionStatsRemoteAuthProtocol_Type(Integer32):
    """Custom type pppSessionStatsRemoteAuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              49187,
              49699)
        )
    )
    namedValues = NamedValues(
        *(("chap", 49699),
          ("none", 0),
          ("pap", 49187))
    )


_PppSessionStatsRemoteAuthProtocol_Type.__name__ = "Integer32"
_PppSessionStatsRemoteAuthProtocol_Object = MibTableColumn
pppSessionStatsRemoteAuthProtocol = _PppSessionStatsRemoteAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 205),
    _PppSessionStatsRemoteAuthProtocol_Type()
)
pppSessionStatsRemoteAuthProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRemoteAuthProtocol.setStatus("current")
_PppSessionStatsLocalPFC_Type = Boolean
_PppSessionStatsLocalPFC_Object = MibTableColumn
pppSessionStatsLocalPFC = _PppSessionStatsLocalPFC_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 206),
    _PppSessionStatsLocalPFC_Type()
)
pppSessionStatsLocalPFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsLocalPFC.setStatus("current")
_PppSessionStatsRemotePFC_Type = Boolean
_PppSessionStatsRemotePFC_Object = MibTableColumn
pppSessionStatsRemotePFC = _PppSessionStatsRemotePFC_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 207),
    _PppSessionStatsRemotePFC_Type()
)
pppSessionStatsRemotePFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRemotePFC.setStatus("current")
_PppSessionStatsLocalACFC_Type = Boolean
_PppSessionStatsLocalACFC_Object = MibTableColumn
pppSessionStatsLocalACFC = _PppSessionStatsLocalACFC_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 208),
    _PppSessionStatsLocalACFC_Type()
)
pppSessionStatsLocalACFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsLocalACFC.setStatus("current")
_PppSessionStatsRemoteACFC_Type = Boolean
_PppSessionStatsRemoteACFC_Object = MibTableColumn
pppSessionStatsRemoteACFC = _PppSessionStatsRemoteACFC_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 209),
    _PppSessionStatsRemoteACFC_Type()
)
pppSessionStatsRemoteACFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRemoteACFC.setStatus("current")
_PppSessionStatsLocalACCM_Type = Integer32
_PppSessionStatsLocalACCM_Object = MibTableColumn
pppSessionStatsLocalACCM = _PppSessionStatsLocalACCM_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 210),
    _PppSessionStatsLocalACCM_Type()
)
pppSessionStatsLocalACCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsLocalACCM.setStatus("current")
_PppSessionStatsRemoteACCM_Type = Integer32
_PppSessionStatsRemoteACCM_Object = MibTableColumn
pppSessionStatsRemoteACCM = _PppSessionStatsRemoteACCM_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 211),
    _PppSessionStatsRemoteACCM_Type()
)
pppSessionStatsRemoteACCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRemoteACCM.setStatus("current")
_PppSessionStatsLocalMRRU_Type = Integer32
_PppSessionStatsLocalMRRU_Object = MibTableColumn
pppSessionStatsLocalMRRU = _PppSessionStatsLocalMRRU_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 212),
    _PppSessionStatsLocalMRRU_Type()
)
pppSessionStatsLocalMRRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsLocalMRRU.setStatus("current")
_PppSessionStatsRemoteMRRU_Type = Integer32
_PppSessionStatsRemoteMRRU_Object = MibTableColumn
pppSessionStatsRemoteMRRU = _PppSessionStatsRemoteMRRU_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 213),
    _PppSessionStatsRemoteMRRU_Type()
)
pppSessionStatsRemoteMRRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRemoteMRRU.setStatus("current")
_PppSessionStatsLocalShortSeq_Type = Boolean
_PppSessionStatsLocalShortSeq_Object = MibTableColumn
pppSessionStatsLocalShortSeq = _PppSessionStatsLocalShortSeq_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 214),
    _PppSessionStatsLocalShortSeq_Type()
)
pppSessionStatsLocalShortSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsLocalShortSeq.setStatus("current")
_PppSessionStatsRemoteShortSeq_Type = Boolean
_PppSessionStatsRemoteShortSeq_Object = MibTableColumn
pppSessionStatsRemoteShortSeq = _PppSessionStatsRemoteShortSeq_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 215),
    _PppSessionStatsRemoteShortSeq_Type()
)
pppSessionStatsRemoteShortSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRemoteShortSeq.setStatus("current")
_PppSessionStatsRemoteAuthenticated_Type = Boolean
_PppSessionStatsRemoteAuthenticated_Object = MibTableColumn
pppSessionStatsRemoteAuthenticated = _PppSessionStatsRemoteAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 301),
    _PppSessionStatsRemoteAuthenticated_Type()
)
pppSessionStatsRemoteAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRemoteAuthenticated.setStatus("current")


class _PppSessionStatsIPCPState_Type(Integer32):
    """Custom type pppSessionStatsIPCPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ackRcvd", 7),
          ("ackSent", 8),
          ("closed", 2),
          ("closing", 4),
          ("initial", 0),
          ("opened", 9),
          ("reqSent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_PppSessionStatsIPCPState_Type.__name__ = "Integer32"
_PppSessionStatsIPCPState_Object = MibTableColumn
pppSessionStatsIPCPState = _PppSessionStatsIPCPState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 401),
    _PppSessionStatsIPCPState_Type()
)
pppSessionStatsIPCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsIPCPState.setStatus("current")
_PppSessionStatsLocalIPAddress_Type = Integer32
_PppSessionStatsLocalIPAddress_Object = MibTableColumn
pppSessionStatsLocalIPAddress = _PppSessionStatsLocalIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 402),
    _PppSessionStatsLocalIPAddress_Type()
)
pppSessionStatsLocalIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsLocalIPAddress.setStatus("current")
_PppSessionStatsRemoteIPAddress_Type = Integer32
_PppSessionStatsRemoteIPAddress_Object = MibTableColumn
pppSessionStatsRemoteIPAddress = _PppSessionStatsRemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 403),
    _PppSessionStatsRemoteIPAddress_Type()
)
pppSessionStatsRemoteIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRemoteIPAddress.setStatus("current")
_PppSessionStatsDNSAddress1_Type = Integer32
_PppSessionStatsDNSAddress1_Object = MibTableColumn
pppSessionStatsDNSAddress1 = _PppSessionStatsDNSAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 404),
    _PppSessionStatsDNSAddress1_Type()
)
pppSessionStatsDNSAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsDNSAddress1.setStatus("current")
_PppSessionStatsDNSAddress2_Type = Integer32
_PppSessionStatsDNSAddress2_Object = MibTableColumn
pppSessionStatsDNSAddress2 = _PppSessionStatsDNSAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 405),
    _PppSessionStatsDNSAddress2_Type()
)
pppSessionStatsDNSAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsDNSAddress2.setStatus("current")
_PppSessionStatsNBNSAddress1_Type = Integer32
_PppSessionStatsNBNSAddress1_Object = MibTableColumn
pppSessionStatsNBNSAddress1 = _PppSessionStatsNBNSAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 406),
    _PppSessionStatsNBNSAddress1_Type()
)
pppSessionStatsNBNSAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsNBNSAddress1.setStatus("current")
_PppSessionStatsNBNSAddress2_Type = Integer32
_PppSessionStatsNBNSAddress2_Object = MibTableColumn
pppSessionStatsNBNSAddress2 = _PppSessionStatsNBNSAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 407),
    _PppSessionStatsNBNSAddress2_Type()
)
pppSessionStatsNBNSAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsNBNSAddress2.setStatus("current")
_PppSessionStatsLocalVJ_Type = Boolean
_PppSessionStatsLocalVJ_Object = MibTableColumn
pppSessionStatsLocalVJ = _PppSessionStatsLocalVJ_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 408),
    _PppSessionStatsLocalVJ_Type()
)
pppSessionStatsLocalVJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsLocalVJ.setStatus("current")
_PppSessionStatsLocalVJSlots_Type = Integer32
_PppSessionStatsLocalVJSlots_Object = MibTableColumn
pppSessionStatsLocalVJSlots = _PppSessionStatsLocalVJSlots_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 409),
    _PppSessionStatsLocalVJSlots_Type()
)
pppSessionStatsLocalVJSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsLocalVJSlots.setStatus("current")
_PppSessionStatsRemoteVJ_Type = Boolean
_PppSessionStatsRemoteVJ_Object = MibTableColumn
pppSessionStatsRemoteVJ = _PppSessionStatsRemoteVJ_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 410),
    _PppSessionStatsRemoteVJ_Type()
)
pppSessionStatsRemoteVJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRemoteVJ.setStatus("current")
_PppSessionStatsRemoteVJSlots_Type = Integer32
_PppSessionStatsRemoteVJSlots_Object = MibTableColumn
pppSessionStatsRemoteVJSlots = _PppSessionStatsRemoteVJSlots_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 411),
    _PppSessionStatsRemoteVJSlots_Type()
)
pppSessionStatsRemoteVJSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRemoteVJSlots.setStatus("current")


class _PppSessionStatsIPXCPState_Type(Integer32):
    """Custom type pppSessionStatsIPXCPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ackRcvd", 7),
          ("ackSent", 8),
          ("closed", 2),
          ("closing", 4),
          ("initial", 0),
          ("opened", 9),
          ("reqSent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_PppSessionStatsIPXCPState_Type.__name__ = "Integer32"
_PppSessionStatsIPXCPState_Object = MibTableColumn
pppSessionStatsIPXCPState = _PppSessionStatsIPXCPState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 451),
    _PppSessionStatsIPXCPState_Type()
)
pppSessionStatsIPXCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsIPXCPState.setStatus("current")
_PppSessionStatsRemoteIPXNetwork_Type = Integer32
_PppSessionStatsRemoteIPXNetwork_Object = MibTableColumn
pppSessionStatsRemoteIPXNetwork = _PppSessionStatsRemoteIPXNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 452),
    _PppSessionStatsRemoteIPXNetwork_Type()
)
pppSessionStatsRemoteIPXNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRemoteIPXNetwork.setStatus("current")


class _PppSessionStatsRemoteIPXNode_Type(DisplayString):
    """Custom type pppSessionStatsRemoteIPXNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_PppSessionStatsRemoteIPXNode_Type.__name__ = "DisplayString"
_PppSessionStatsRemoteIPXNode_Object = MibTableColumn
pppSessionStatsRemoteIPXNode = _PppSessionStatsRemoteIPXNode_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 453),
    _PppSessionStatsRemoteIPXNode_Type()
)
pppSessionStatsRemoteIPXNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRemoteIPXNode.setStatus("current")


class _PppSessionStatsCCPState_Type(Integer32):
    """Custom type pppSessionStatsCCPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ackRcvd", 7),
          ("ackSent", 8),
          ("closed", 2),
          ("closing", 4),
          ("initial", 0),
          ("opened", 9),
          ("reqSent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_PppSessionStatsCCPState_Type.__name__ = "Integer32"
_PppSessionStatsCCPState_Object = MibTableColumn
pppSessionStatsCCPState = _PppSessionStatsCCPState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 501),
    _PppSessionStatsCCPState_Type()
)
pppSessionStatsCCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsCCPState.setStatus("current")


class _PppSessionStatsLocalCompressAlgorithm_Type(Integer32):
    """Custom type pppSessionStatsLocalCompressAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mppc", 2),
          ("none", 0),
          ("stac3", 3),
          ("stac4", 1))
    )


_PppSessionStatsLocalCompressAlgorithm_Type.__name__ = "Integer32"
_PppSessionStatsLocalCompressAlgorithm_Object = MibTableColumn
pppSessionStatsLocalCompressAlgorithm = _PppSessionStatsLocalCompressAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 502),
    _PppSessionStatsLocalCompressAlgorithm_Type()
)
pppSessionStatsLocalCompressAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsLocalCompressAlgorithm.setStatus("current")
_PppSessionStatsLocalCompressHistories_Type = Integer32
_PppSessionStatsLocalCompressHistories_Object = MibTableColumn
pppSessionStatsLocalCompressHistories = _PppSessionStatsLocalCompressHistories_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 503),
    _PppSessionStatsLocalCompressHistories_Type()
)
pppSessionStatsLocalCompressHistories.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsLocalCompressHistories.setStatus("current")


class _PppSessionStatsRemoteCompressAlgorithm_Type(Integer32):
    """Custom type pppSessionStatsRemoteCompressAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mppc", 2),
          ("none", 0),
          ("stac3", 3),
          ("stac4", 1))
    )


_PppSessionStatsRemoteCompressAlgorithm_Type.__name__ = "Integer32"
_PppSessionStatsRemoteCompressAlgorithm_Object = MibTableColumn
pppSessionStatsRemoteCompressAlgorithm = _PppSessionStatsRemoteCompressAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 504),
    _PppSessionStatsRemoteCompressAlgorithm_Type()
)
pppSessionStatsRemoteCompressAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRemoteCompressAlgorithm.setStatus("current")
_PppSessionStatsRemoteCompressHistories_Type = Integer32
_PppSessionStatsRemoteCompressHistories_Object = MibTableColumn
pppSessionStatsRemoteCompressHistories = _PppSessionStatsRemoteCompressHistories_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 505),
    _PppSessionStatsRemoteCompressHistories_Type()
)
pppSessionStatsRemoteCompressHistories.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRemoteCompressHistories.setStatus("current")
_PppSessionStatsMultilinkActive_Type = Boolean
_PppSessionStatsMultilinkActive_Object = MibTableColumn
pppSessionStatsMultilinkActive = _PppSessionStatsMultilinkActive_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 601),
    _PppSessionStatsMultilinkActive_Type()
)
pppSessionStatsMultilinkActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsMultilinkActive.setStatus("current")
_PppSessionStatsMultilinkLinks_Type = Integer32
_PppSessionStatsMultilinkLinks_Object = MibTableColumn
pppSessionStatsMultilinkLinks = _PppSessionStatsMultilinkLinks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 602),
    _PppSessionStatsMultilinkLinks_Type()
)
pppSessionStatsMultilinkLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsMultilinkLinks.setStatus("current")
_PppSessionStatsTotalTxSpeed_Type = Integer32
_PppSessionStatsTotalTxSpeed_Object = MibTableColumn
pppSessionStatsTotalTxSpeed = _PppSessionStatsTotalTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 603),
    _PppSessionStatsTotalTxSpeed_Type()
)
pppSessionStatsTotalTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsTotalTxSpeed.setStatus("current")
_PppSessionStatsTotalRxSpeed_Type = Integer32
_PppSessionStatsTotalRxSpeed_Object = MibTableColumn
pppSessionStatsTotalRxSpeed = _PppSessionStatsTotalRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 604),
    _PppSessionStatsTotalRxSpeed_Type()
)
pppSessionStatsTotalRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsTotalRxSpeed.setStatus("current")
_PppSessionStatsMLPFragmentsReceived_Type = Integer32
_PppSessionStatsMLPFragmentsReceived_Object = MibTableColumn
pppSessionStatsMLPFragmentsReceived = _PppSessionStatsMLPFragmentsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 605),
    _PppSessionStatsMLPFragmentsReceived_Type()
)
pppSessionStatsMLPFragmentsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsMLPFragmentsReceived.setStatus("current")
_PppSessionStatsMLPFragmentsMissing_Type = Integer32
_PppSessionStatsMLPFragmentsMissing_Object = MibTableColumn
pppSessionStatsMLPFragmentsMissing = _PppSessionStatsMLPFragmentsMissing_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 606),
    _PppSessionStatsMLPFragmentsMissing_Type()
)
pppSessionStatsMLPFragmentsMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsMLPFragmentsMissing.setStatus("current")
_PppSessionStatsMLPFragmentsDropped_Type = Integer32
_PppSessionStatsMLPFragmentsDropped_Object = MibTableColumn
pppSessionStatsMLPFragmentsDropped = _PppSessionStatsMLPFragmentsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 607),
    _PppSessionStatsMLPFragmentsDropped_Type()
)
pppSessionStatsMLPFragmentsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsMLPFragmentsDropped.setStatus("current")
_PppSessionStatsMLPPacketsReassembled_Type = Integer32
_PppSessionStatsMLPPacketsReassembled_Object = MibTableColumn
pppSessionStatsMLPPacketsReassembled = _PppSessionStatsMLPPacketsReassembled_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 608),
    _PppSessionStatsMLPPacketsReassembled_Type()
)
pppSessionStatsMLPPacketsReassembled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsMLPPacketsReassembled.setStatus("current")
_PppSessionStatsMLPPacketsNull_Type = Integer32
_PppSessionStatsMLPPacketsNull_Object = MibTableColumn
pppSessionStatsMLPPacketsNull = _PppSessionStatsMLPPacketsNull_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 609),
    _PppSessionStatsMLPPacketsNull_Type()
)
pppSessionStatsMLPPacketsNull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsMLPPacketsNull.setStatus("current")
_PppSessionStatsMultilinkLinksAdded_Type = Integer32
_PppSessionStatsMultilinkLinksAdded_Object = MibTableColumn
pppSessionStatsMultilinkLinksAdded = _PppSessionStatsMultilinkLinksAdded_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 610),
    _PppSessionStatsMultilinkLinksAdded_Type()
)
pppSessionStatsMultilinkLinksAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsMultilinkLinksAdded.setStatus("current")
_PppSessionStatsMultilinkLinksRemoved_Type = Integer32
_PppSessionStatsMultilinkLinksRemoved_Object = MibTableColumn
pppSessionStatsMultilinkLinksRemoved = _PppSessionStatsMultilinkLinksRemoved_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 611),
    _PppSessionStatsMultilinkLinksRemoved_Type()
)
pppSessionStatsMultilinkLinksRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsMultilinkLinksRemoved.setStatus("current")
_PppSessionStatsMultilinkLinksMax_Type = Integer32
_PppSessionStatsMultilinkLinksMax_Object = MibTableColumn
pppSessionStatsMultilinkLinksMax = _PppSessionStatsMultilinkLinksMax_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 612),
    _PppSessionStatsMultilinkLinksMax_Type()
)
pppSessionStatsMultilinkLinksMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsMultilinkLinksMax.setStatus("current")
_PppSessionStatsMultilinkLinksMaxConfig_Type = Integer32
_PppSessionStatsMultilinkLinksMaxConfig_Object = MibTableColumn
pppSessionStatsMultilinkLinksMaxConfig = _PppSessionStatsMultilinkLinksMaxConfig_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 613),
    _PppSessionStatsMultilinkLinksMaxConfig_Type()
)
pppSessionStatsMultilinkLinksMaxConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsMultilinkLinksMaxConfig.setStatus("current")
_PppSessionStatsTxPackets_Type = Integer32
_PppSessionStatsTxPackets_Object = MibTableColumn
pppSessionStatsTxPackets = _PppSessionStatsTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1001),
    _PppSessionStatsTxPackets_Type()
)
pppSessionStatsTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsTxPackets.setStatus("current")
_PppSessionStatsTxPacketsDropped_Type = Integer32
_PppSessionStatsTxPacketsDropped_Object = MibTableColumn
pppSessionStatsTxPacketsDropped = _PppSessionStatsTxPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1002),
    _PppSessionStatsTxPacketsDropped_Type()
)
pppSessionStatsTxPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsTxPacketsDropped.setStatus("current")
_PppSessionStatsTxBytes_Type = Integer32
_PppSessionStatsTxBytes_Object = MibTableColumn
pppSessionStatsTxBytes = _PppSessionStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1003),
    _PppSessionStatsTxBytes_Type()
)
pppSessionStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsTxBytes.setStatus("current")
_PppSessionStatsRxPackets_Type = Integer32
_PppSessionStatsRxPackets_Object = MibTableColumn
pppSessionStatsRxPackets = _PppSessionStatsRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1004),
    _PppSessionStatsRxPackets_Type()
)
pppSessionStatsRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRxPackets.setStatus("current")
_PppSessionStatsRxPacketsDropped_Type = Integer32
_PppSessionStatsRxPacketsDropped_Object = MibTableColumn
pppSessionStatsRxPacketsDropped = _PppSessionStatsRxPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1005),
    _PppSessionStatsRxPacketsDropped_Type()
)
pppSessionStatsRxPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRxPacketsDropped.setStatus("current")
_PppSessionStatsRxBytes_Type = Integer32
_PppSessionStatsRxBytes_Object = MibTableColumn
pppSessionStatsRxBytes = _PppSessionStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1006),
    _PppSessionStatsRxBytes_Type()
)
pppSessionStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRxBytes.setStatus("current")
_PppSessionStatsTxCompressing_Type = Boolean
_PppSessionStatsTxCompressing_Object = MibTableColumn
pppSessionStatsTxCompressing = _PppSessionStatsTxCompressing_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1101),
    _PppSessionStatsTxCompressing_Type()
)
pppSessionStatsTxCompressing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsTxCompressing.setStatus("current")
_PppSessionStatsTxBytesBeforeCompress_Type = Integer32
_PppSessionStatsTxBytesBeforeCompress_Object = MibTableColumn
pppSessionStatsTxBytesBeforeCompress = _PppSessionStatsTxBytesBeforeCompress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1102),
    _PppSessionStatsTxBytesBeforeCompress_Type()
)
pppSessionStatsTxBytesBeforeCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsTxBytesBeforeCompress.setStatus("current")
_PppSessionStatsTxBytesAfterCompress_Type = Integer32
_PppSessionStatsTxBytesAfterCompress_Object = MibTableColumn
pppSessionStatsTxBytesAfterCompress = _PppSessionStatsTxBytesAfterCompress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1103),
    _PppSessionStatsTxBytesAfterCompress_Type()
)
pppSessionStatsTxBytesAfterCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsTxBytesAfterCompress.setStatus("current")
_PppSessionStatsTxBytesUncompressed_Type = Integer32
_PppSessionStatsTxBytesUncompressed_Object = MibTableColumn
pppSessionStatsTxBytesUncompressed = _PppSessionStatsTxBytesUncompressed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1104),
    _PppSessionStatsTxBytesUncompressed_Type()
)
pppSessionStatsTxBytesUncompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsTxBytesUncompressed.setStatus("current")
_PppSessionStatsRxBytesBeforeCompress_Type = Integer32
_PppSessionStatsRxBytesBeforeCompress_Object = MibTableColumn
pppSessionStatsRxBytesBeforeCompress = _PppSessionStatsRxBytesBeforeCompress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1105),
    _PppSessionStatsRxBytesBeforeCompress_Type()
)
pppSessionStatsRxBytesBeforeCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRxBytesBeforeCompress.setStatus("current")
_PppSessionStatsRxBytesAfterCompress_Type = Integer32
_PppSessionStatsRxBytesAfterCompress_Object = MibTableColumn
pppSessionStatsRxBytesAfterCompress = _PppSessionStatsRxBytesAfterCompress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1106),
    _PppSessionStatsRxBytesAfterCompress_Type()
)
pppSessionStatsRxBytesAfterCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRxBytesAfterCompress.setStatus("current")
_PppSessionStatsRxBytesUncompressed_Type = Integer32
_PppSessionStatsRxBytesUncompressed_Object = MibTableColumn
pppSessionStatsRxBytesUncompressed = _PppSessionStatsRxBytesUncompressed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1107),
    _PppSessionStatsRxBytesUncompressed_Type()
)
pppSessionStatsRxBytesUncompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRxBytesUncompressed.setStatus("current")
_PppSessionStatsRxCompPacketsDropped_Type = Integer32
_PppSessionStatsRxCompPacketsDropped_Object = MibTableColumn
pppSessionStatsRxCompPacketsDropped = _PppSessionStatsRxCompPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1108),
    _PppSessionStatsRxCompPacketsDropped_Type()
)
pppSessionStatsRxCompPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRxCompPacketsDropped.setStatus("current")
_PppSessionStatsCCPResetsSent_Type = Integer32
_PppSessionStatsCCPResetsSent_Object = MibTableColumn
pppSessionStatsCCPResetsSent = _PppSessionStatsCCPResetsSent_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1109),
    _PppSessionStatsCCPResetsSent_Type()
)
pppSessionStatsCCPResetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsCCPResetsSent.setStatus("current")
_PppSessionStatsCCPResetsReceived_Type = Integer32
_PppSessionStatsCCPResetsReceived_Object = MibTableColumn
pppSessionStatsCCPResetsReceived = _PppSessionStatsCCPResetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1110),
    _PppSessionStatsCCPResetsReceived_Type()
)
pppSessionStatsCCPResetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsCCPResetsReceived.setStatus("current")
_PppSessionStatsRxResourceErrors_Type = Integer32
_PppSessionStatsRxResourceErrors_Object = MibTableColumn
pppSessionStatsRxResourceErrors = _PppSessionStatsRxResourceErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1201),
    _PppSessionStatsRxResourceErrors_Type()
)
pppSessionStatsRxResourceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRxResourceErrors.setStatus("current")
_PppSessionStatsRxQueueErrors_Type = Integer32
_PppSessionStatsRxQueueErrors_Object = MibTableColumn
pppSessionStatsRxQueueErrors = _PppSessionStatsRxQueueErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1202),
    _PppSessionStatsRxQueueErrors_Type()
)
pppSessionStatsRxQueueErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRxQueueErrors.setStatus("current")
_PppSessionStatsRxCRCErrors_Type = Integer32
_PppSessionStatsRxCRCErrors_Object = MibTableColumn
pppSessionStatsRxCRCErrors = _PppSessionStatsRxCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1203),
    _PppSessionStatsRxCRCErrors_Type()
)
pppSessionStatsRxCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRxCRCErrors.setStatus("current")
_PppSessionStatsRxAbortErrors_Type = Integer32
_PppSessionStatsRxAbortErrors_Object = MibTableColumn
pppSessionStatsRxAbortErrors = _PppSessionStatsRxAbortErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1204),
    _PppSessionStatsRxAbortErrors_Type()
)
pppSessionStatsRxAbortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRxAbortErrors.setStatus("current")
_PppSessionStatsRxOverrunErrors_Type = Integer32
_PppSessionStatsRxOverrunErrors_Object = MibTableColumn
pppSessionStatsRxOverrunErrors = _PppSessionStatsRxOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1205),
    _PppSessionStatsRxOverrunErrors_Type()
)
pppSessionStatsRxOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRxOverrunErrors.setStatus("current")
_PppSessionStatsRxBigErrors_Type = Integer32
_PppSessionStatsRxBigErrors_Object = MibTableColumn
pppSessionStatsRxBigErrors = _PppSessionStatsRxBigErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1206),
    _PppSessionStatsRxBigErrors_Type()
)
pppSessionStatsRxBigErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRxBigErrors.setStatus("current")
_PppSessionStatsRxSmallErrors_Type = Integer32
_PppSessionStatsRxSmallErrors_Object = MibTableColumn
pppSessionStatsRxSmallErrors = _PppSessionStatsRxSmallErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1207),
    _PppSessionStatsRxSmallErrors_Type()
)
pppSessionStatsRxSmallErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRxSmallErrors.setStatus("current")
_PppSessionStatsRxAlignErrors_Type = Integer32
_PppSessionStatsRxAlignErrors_Object = MibTableColumn
pppSessionStatsRxAlignErrors = _PppSessionStatsRxAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1208),
    _PppSessionStatsRxAlignErrors_Type()
)
pppSessionStatsRxAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsRxAlignErrors.setStatus("current")
_PppSessionStatsTxResourceErrors_Type = Integer32
_PppSessionStatsTxResourceErrors_Object = MibTableColumn
pppSessionStatsTxResourceErrors = _PppSessionStatsTxResourceErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1209),
    _PppSessionStatsTxResourceErrors_Type()
)
pppSessionStatsTxResourceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsTxResourceErrors.setStatus("current")
_PppSessionStatsTxQueueErrors_Type = Integer32
_PppSessionStatsTxQueueErrors_Object = MibTableColumn
pppSessionStatsTxQueueErrors = _PppSessionStatsTxQueueErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1210),
    _PppSessionStatsTxQueueErrors_Type()
)
pppSessionStatsTxQueueErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsTxQueueErrors.setStatus("current")
_PppSessionStatsTxBigErrors_Type = Integer32
_PppSessionStatsTxBigErrors_Object = MibTableColumn
pppSessionStatsTxBigErrors = _PppSessionStatsTxBigErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1211),
    _PppSessionStatsTxBigErrors_Type()
)
pppSessionStatsTxBigErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsTxBigErrors.setStatus("current")
_PppSessionStatsTxUnderrunErrors_Type = Integer32
_PppSessionStatsTxUnderrunErrors_Object = MibTableColumn
pppSessionStatsTxUnderrunErrors = _PppSessionStatsTxUnderrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1318, 1, 1212),
    _PppSessionStatsTxUnderrunErrors_Type()
)
pppSessionStatsTxUnderrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionStatsTxUnderrunErrors.setStatus("current")
_PppSummaryStatsTable_Object = MibTable
pppSummaryStatsTable = _PppSummaryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1319)
)
if mibBuilder.loadTexts:
    pppSummaryStatsTable.setStatus("current")
_PppSummaryStatsEntry_Object = MibTableRow
pppSummaryStatsEntry = _PppSummaryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1319, 1)
)
pppSummaryStatsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "pppSummaryStatsSlotNumber"),
)
if mibBuilder.loadTexts:
    pppSummaryStatsEntry.setStatus("current")
_PppSummaryStatsSlotNumber_Type = Integer32
_PppSummaryStatsSlotNumber_Object = MibTableColumn
pppSummaryStatsSlotNumber = _PppSummaryStatsSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1319, 1, 1),
    _PppSummaryStatsSlotNumber_Type()
)
pppSummaryStatsSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSummaryStatsSlotNumber.setStatus("current")
_PppSummaryStatsMaxLinks_Type = Integer32
_PppSummaryStatsMaxLinks_Object = MibTableColumn
pppSummaryStatsMaxLinks = _PppSummaryStatsMaxLinks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1319, 1, 2),
    _PppSummaryStatsMaxLinks_Type()
)
pppSummaryStatsMaxLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSummaryStatsMaxLinks.setStatus("current")
_PppSummaryStatsActiveLinks_Type = Integer32
_PppSummaryStatsActiveLinks_Object = MibTableColumn
pppSummaryStatsActiveLinks = _PppSummaryStatsActiveLinks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1319, 1, 3),
    _PppSummaryStatsActiveLinks_Type()
)
pppSummaryStatsActiveLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSummaryStatsActiveLinks.setStatus("current")
_PppSummaryStatsMaxActiveLinks_Type = Integer32
_PppSummaryStatsMaxActiveLinks_Object = MibTableColumn
pppSummaryStatsMaxActiveLinks = _PppSummaryStatsMaxActiveLinks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1319, 1, 4),
    _PppSummaryStatsMaxActiveLinks_Type()
)
pppSummaryStatsMaxActiveLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSummaryStatsMaxActiveLinks.setStatus("current")
_PppSummaryStatsFreeLinks_Type = Integer32
_PppSummaryStatsFreeLinks_Object = MibTableColumn
pppSummaryStatsFreeLinks = _PppSummaryStatsFreeLinks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1319, 1, 5),
    _PppSummaryStatsFreeLinks_Type()
)
pppSummaryStatsFreeLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSummaryStatsFreeLinks.setStatus("current")
_PppSummaryStatsLinksStarted_Type = Integer32
_PppSummaryStatsLinksStarted_Object = MibTableColumn
pppSummaryStatsLinksStarted = _PppSummaryStatsLinksStarted_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1319, 1, 6),
    _PppSummaryStatsLinksStarted_Type()
)
pppSummaryStatsLinksStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSummaryStatsLinksStarted.setStatus("current")
_PppSummaryStatsLinksStopped_Type = Integer32
_PppSummaryStatsLinksStopped_Object = MibTableColumn
pppSummaryStatsLinksStopped = _PppSummaryStatsLinksStopped_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1319, 1, 7),
    _PppSummaryStatsLinksStopped_Type()
)
pppSummaryStatsLinksStopped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSummaryStatsLinksStopped.setStatus("current")
_PppSummaryStatsLinksModem_Type = Integer32
_PppSummaryStatsLinksModem_Object = MibTableColumn
pppSummaryStatsLinksModem = _PppSummaryStatsLinksModem_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1319, 1, 101),
    _PppSummaryStatsLinksModem_Type()
)
pppSummaryStatsLinksModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSummaryStatsLinksModem.setStatus("current")
_PppSummaryStatsLinksHDLC_Type = Integer32
_PppSummaryStatsLinksHDLC_Object = MibTableColumn
pppSummaryStatsLinksHDLC = _PppSummaryStatsLinksHDLC_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1319, 1, 102),
    _PppSummaryStatsLinksHDLC_Type()
)
pppSummaryStatsLinksHDLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSummaryStatsLinksHDLC.setStatus("current")
_PppSummaryStatsLinksLeased_Type = Integer32
_PppSummaryStatsLinksLeased_Object = MibTableColumn
pppSummaryStatsLinksLeased = _PppSummaryStatsLinksLeased_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1319, 1, 103),
    _PppSummaryStatsLinksLeased_Type()
)
pppSummaryStatsLinksLeased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSummaryStatsLinksLeased.setStatus("current")
_PppSummaryStatsLinksNegotiatedLCP_Type = Integer32
_PppSummaryStatsLinksNegotiatedLCP_Object = MibTableColumn
pppSummaryStatsLinksNegotiatedLCP = _PppSummaryStatsLinksNegotiatedLCP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1319, 1, 201),
    _PppSummaryStatsLinksNegotiatedLCP_Type()
)
pppSummaryStatsLinksNegotiatedLCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSummaryStatsLinksNegotiatedLCP.setStatus("current")
_PppSummaryStatsLinksAuthenticated_Type = Integer32
_PppSummaryStatsLinksAuthenticated_Object = MibTableColumn
pppSummaryStatsLinksAuthenticated = _PppSummaryStatsLinksAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1319, 1, 202),
    _PppSummaryStatsLinksAuthenticated_Type()
)
pppSummaryStatsLinksAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSummaryStatsLinksAuthenticated.setStatus("current")
_PppSummaryStatsLinksNegotiatedIPCP_Type = Integer32
_PppSummaryStatsLinksNegotiatedIPCP_Object = MibTableColumn
pppSummaryStatsLinksNegotiatedIPCP = _PppSummaryStatsLinksNegotiatedIPCP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1319, 1, 203),
    _PppSummaryStatsLinksNegotiatedIPCP_Type()
)
pppSummaryStatsLinksNegotiatedIPCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSummaryStatsLinksNegotiatedIPCP.setStatus("current")
_PppSummaryStatsLinksNegotiatedMLP_Type = Integer32
_PppSummaryStatsLinksNegotiatedMLP_Object = MibTableColumn
pppSummaryStatsLinksNegotiatedMLP = _PppSummaryStatsLinksNegotiatedMLP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1319, 1, 204),
    _PppSummaryStatsLinksNegotiatedMLP_Type()
)
pppSummaryStatsLinksNegotiatedMLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSummaryStatsLinksNegotiatedMLP.setStatus("current")
_PppSummaryStatsLinksNegotiatedCCP_Type = Integer32
_PppSummaryStatsLinksNegotiatedCCP_Object = MibTableColumn
pppSummaryStatsLinksNegotiatedCCP = _PppSummaryStatsLinksNegotiatedCCP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1319, 1, 205),
    _PppSummaryStatsLinksNegotiatedCCP_Type()
)
pppSummaryStatsLinksNegotiatedCCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSummaryStatsLinksNegotiatedCCP.setStatus("current")
_PppSummaryStatsLinksNegotiatedIPXCP_Type = Integer32
_PppSummaryStatsLinksNegotiatedIPXCP_Object = MibTableColumn
pppSummaryStatsLinksNegotiatedIPXCP = _PppSummaryStatsLinksNegotiatedIPXCP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1319, 1, 206),
    _PppSummaryStatsLinksNegotiatedIPXCP_Type()
)
pppSummaryStatsLinksNegotiatedIPXCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSummaryStatsLinksNegotiatedIPXCP.setStatus("current")
_PppDeadSessionStatsTable_Object = MibTable
pppDeadSessionStatsTable = _PppDeadSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320)
)
if mibBuilder.loadTexts:
    pppDeadSessionStatsTable.setStatus("current")
_PppDeadSessionStatsEntry_Object = MibTableRow
pppDeadSessionStatsEntry = _PppDeadSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1)
)
pppDeadSessionStatsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "pppDeadSessionStatsSessionID"),
)
if mibBuilder.loadTexts:
    pppDeadSessionStatsEntry.setStatus("current")
_PppDeadSessionStatsSessionID_Type = Integer32
_PppDeadSessionStatsSessionID_Object = MibTableColumn
pppDeadSessionStatsSessionID = _PppDeadSessionStatsSessionID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1),
    _PppDeadSessionStatsSessionID_Type()
)
pppDeadSessionStatsSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsSessionID.setStatus("current")


class _PppDeadSessionStatsPhase_Type(Integer32):
    """Custom type pppDeadSessionStatsPhase based on Integer32"""
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
        *(("auth", 2),
          ("establish", 1),
          ("idle", 0),
          ("network", 3),
          ("terminate", 4))
    )


_PppDeadSessionStatsPhase_Type.__name__ = "Integer32"
_PppDeadSessionStatsPhase_Object = MibTableColumn
pppDeadSessionStatsPhase = _PppDeadSessionStatsPhase_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 2),
    _PppDeadSessionStatsPhase_Type()
)
pppDeadSessionStatsPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsPhase.setStatus("current")


class _PppDeadSessionStatsUserName_Type(DisplayString):
    """Custom type pppDeadSessionStatsUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PppDeadSessionStatsUserName_Type.__name__ = "DisplayString"
_PppDeadSessionStatsUserName_Object = MibTableColumn
pppDeadSessionStatsUserName = _PppDeadSessionStatsUserName_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 3),
    _PppDeadSessionStatsUserName_Type()
)
pppDeadSessionStatsUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsUserName.setStatus("current")
_PppDeadSessionStatsUpTime_Type = Integer32
_PppDeadSessionStatsUpTime_Object = MibTableColumn
pppDeadSessionStatsUpTime = _PppDeadSessionStatsUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 4),
    _PppDeadSessionStatsUpTime_Type()
)
pppDeadSessionStatsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsUpTime.setStatus("current")
_PppDeadSessionStatsConnectLimit_Type = Integer32
_PppDeadSessionStatsConnectLimit_Object = MibTableColumn
pppDeadSessionStatsConnectLimit = _PppDeadSessionStatsConnectLimit_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 5),
    _PppDeadSessionStatsConnectLimit_Type()
)
pppDeadSessionStatsConnectLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsConnectLimit.setStatus("current")
_PppDeadSessionStatsRemainingTime_Type = Integer32
_PppDeadSessionStatsRemainingTime_Object = MibTableColumn
pppDeadSessionStatsRemainingTime = _PppDeadSessionStatsRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 6),
    _PppDeadSessionStatsRemainingTime_Type()
)
pppDeadSessionStatsRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRemainingTime.setStatus("current")
_PppDeadSessionStatsInactivityLimit_Type = Integer32
_PppDeadSessionStatsInactivityLimit_Object = MibTableColumn
pppDeadSessionStatsInactivityLimit = _PppDeadSessionStatsInactivityLimit_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 7),
    _PppDeadSessionStatsInactivityLimit_Type()
)
pppDeadSessionStatsInactivityLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsInactivityLimit.setStatus("current")
_PppDeadSessionStatsInactivityRemaining_Type = Integer32
_PppDeadSessionStatsInactivityRemaining_Object = MibTableColumn
pppDeadSessionStatsInactivityRemaining = _PppDeadSessionStatsInactivityRemaining_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 8),
    _PppDeadSessionStatsInactivityRemaining_Type()
)
pppDeadSessionStatsInactivityRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsInactivityRemaining.setStatus("current")
_PppDeadSessionStatsDeadSession_Type = Boolean
_PppDeadSessionStatsDeadSession_Object = MibTableColumn
pppDeadSessionStatsDeadSession = _PppDeadSessionStatsDeadSession_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 9),
    _PppDeadSessionStatsDeadSession_Type()
)
pppDeadSessionStatsDeadSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsDeadSession.setStatus("current")


class _PppDeadSessionStatsInterfaceType_Type(Integer32):
    """Custom type pppDeadSessionStatsInterfaceType based on Integer32"""
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
        *(("hssi", 4),
          ("isdn", 2),
          ("leased", 3),
          ("modem", 1),
          ("unknown", 0))
    )


_PppDeadSessionStatsInterfaceType_Type.__name__ = "Integer32"
_PppDeadSessionStatsInterfaceType_Object = MibTableColumn
pppDeadSessionStatsInterfaceType = _PppDeadSessionStatsInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 101),
    _PppDeadSessionStatsInterfaceType_Type()
)
pppDeadSessionStatsInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsInterfaceType.setStatus("current")
_PppDeadSessionStatsTxSpeed_Type = Integer32
_PppDeadSessionStatsTxSpeed_Object = MibTableColumn
pppDeadSessionStatsTxSpeed = _PppDeadSessionStatsTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 102),
    _PppDeadSessionStatsTxSpeed_Type()
)
pppDeadSessionStatsTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsTxSpeed.setStatus("current")
_PppDeadSessionStatsRxSpeed_Type = Integer32
_PppDeadSessionStatsRxSpeed_Object = MibTableColumn
pppDeadSessionStatsRxSpeed = _PppDeadSessionStatsRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 103),
    _PppDeadSessionStatsRxSpeed_Type()
)
pppDeadSessionStatsRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRxSpeed.setStatus("current")


class _PppDeadSessionStatsLCPState_Type(Integer32):
    """Custom type pppDeadSessionStatsLCPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ackRcvd", 7),
          ("ackSent", 8),
          ("closed", 2),
          ("closing", 4),
          ("initial", 0),
          ("opened", 9),
          ("reqSent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_PppDeadSessionStatsLCPState_Type.__name__ = "Integer32"
_PppDeadSessionStatsLCPState_Object = MibTableColumn
pppDeadSessionStatsLCPState = _PppDeadSessionStatsLCPState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 201),
    _PppDeadSessionStatsLCPState_Type()
)
pppDeadSessionStatsLCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsLCPState.setStatus("current")
_PppDeadSessionStatsLocalMRU_Type = Integer32
_PppDeadSessionStatsLocalMRU_Object = MibTableColumn
pppDeadSessionStatsLocalMRU = _PppDeadSessionStatsLocalMRU_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 202),
    _PppDeadSessionStatsLocalMRU_Type()
)
pppDeadSessionStatsLocalMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsLocalMRU.setStatus("current")
_PppDeadSessionStatsRemoteMRU_Type = Integer32
_PppDeadSessionStatsRemoteMRU_Object = MibTableColumn
pppDeadSessionStatsRemoteMRU = _PppDeadSessionStatsRemoteMRU_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 203),
    _PppDeadSessionStatsRemoteMRU_Type()
)
pppDeadSessionStatsRemoteMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRemoteMRU.setStatus("current")


class _PppDeadSessionStatsLocalAuthProtocol_Type(Integer32):
    """Custom type pppDeadSessionStatsLocalAuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              49187,
              49699)
        )
    )
    namedValues = NamedValues(
        *(("chap", 49699),
          ("none", 0),
          ("pap", 49187))
    )


_PppDeadSessionStatsLocalAuthProtocol_Type.__name__ = "Integer32"
_PppDeadSessionStatsLocalAuthProtocol_Object = MibTableColumn
pppDeadSessionStatsLocalAuthProtocol = _PppDeadSessionStatsLocalAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 204),
    _PppDeadSessionStatsLocalAuthProtocol_Type()
)
pppDeadSessionStatsLocalAuthProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsLocalAuthProtocol.setStatus("current")


class _PppDeadSessionStatsRemoteAuthProtocol_Type(Integer32):
    """Custom type pppDeadSessionStatsRemoteAuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              49187,
              49699)
        )
    )
    namedValues = NamedValues(
        *(("chap", 49699),
          ("none", 0),
          ("pap", 49187))
    )


_PppDeadSessionStatsRemoteAuthProtocol_Type.__name__ = "Integer32"
_PppDeadSessionStatsRemoteAuthProtocol_Object = MibTableColumn
pppDeadSessionStatsRemoteAuthProtocol = _PppDeadSessionStatsRemoteAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 205),
    _PppDeadSessionStatsRemoteAuthProtocol_Type()
)
pppDeadSessionStatsRemoteAuthProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRemoteAuthProtocol.setStatus("current")
_PppDeadSessionStatsLocalPFC_Type = Boolean
_PppDeadSessionStatsLocalPFC_Object = MibTableColumn
pppDeadSessionStatsLocalPFC = _PppDeadSessionStatsLocalPFC_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 206),
    _PppDeadSessionStatsLocalPFC_Type()
)
pppDeadSessionStatsLocalPFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsLocalPFC.setStatus("current")
_PppDeadSessionStatsRemotePFC_Type = Boolean
_PppDeadSessionStatsRemotePFC_Object = MibTableColumn
pppDeadSessionStatsRemotePFC = _PppDeadSessionStatsRemotePFC_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 207),
    _PppDeadSessionStatsRemotePFC_Type()
)
pppDeadSessionStatsRemotePFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRemotePFC.setStatus("current")
_PppDeadSessionStatsLocalACFC_Type = Boolean
_PppDeadSessionStatsLocalACFC_Object = MibTableColumn
pppDeadSessionStatsLocalACFC = _PppDeadSessionStatsLocalACFC_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 208),
    _PppDeadSessionStatsLocalACFC_Type()
)
pppDeadSessionStatsLocalACFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsLocalACFC.setStatus("current")
_PppDeadSessionStatsRemoteACFC_Type = Boolean
_PppDeadSessionStatsRemoteACFC_Object = MibTableColumn
pppDeadSessionStatsRemoteACFC = _PppDeadSessionStatsRemoteACFC_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 209),
    _PppDeadSessionStatsRemoteACFC_Type()
)
pppDeadSessionStatsRemoteACFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRemoteACFC.setStatus("current")
_PppDeadSessionStatsLocalACCM_Type = Integer32
_PppDeadSessionStatsLocalACCM_Object = MibTableColumn
pppDeadSessionStatsLocalACCM = _PppDeadSessionStatsLocalACCM_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 210),
    _PppDeadSessionStatsLocalACCM_Type()
)
pppDeadSessionStatsLocalACCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsLocalACCM.setStatus("current")
_PppDeadSessionStatsRemoteACCM_Type = Integer32
_PppDeadSessionStatsRemoteACCM_Object = MibTableColumn
pppDeadSessionStatsRemoteACCM = _PppDeadSessionStatsRemoteACCM_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 211),
    _PppDeadSessionStatsRemoteACCM_Type()
)
pppDeadSessionStatsRemoteACCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRemoteACCM.setStatus("current")
_PppDeadSessionStatsLocalMRRU_Type = Integer32
_PppDeadSessionStatsLocalMRRU_Object = MibTableColumn
pppDeadSessionStatsLocalMRRU = _PppDeadSessionStatsLocalMRRU_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 212),
    _PppDeadSessionStatsLocalMRRU_Type()
)
pppDeadSessionStatsLocalMRRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsLocalMRRU.setStatus("current")
_PppDeadSessionStatsRemoteMRRU_Type = Integer32
_PppDeadSessionStatsRemoteMRRU_Object = MibTableColumn
pppDeadSessionStatsRemoteMRRU = _PppDeadSessionStatsRemoteMRRU_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 213),
    _PppDeadSessionStatsRemoteMRRU_Type()
)
pppDeadSessionStatsRemoteMRRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRemoteMRRU.setStatus("current")
_PppDeadSessionStatsLocalShortSeq_Type = Boolean
_PppDeadSessionStatsLocalShortSeq_Object = MibTableColumn
pppDeadSessionStatsLocalShortSeq = _PppDeadSessionStatsLocalShortSeq_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 214),
    _PppDeadSessionStatsLocalShortSeq_Type()
)
pppDeadSessionStatsLocalShortSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsLocalShortSeq.setStatus("current")
_PppDeadSessionStatsRemoteShortSeq_Type = Boolean
_PppDeadSessionStatsRemoteShortSeq_Object = MibTableColumn
pppDeadSessionStatsRemoteShortSeq = _PppDeadSessionStatsRemoteShortSeq_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 215),
    _PppDeadSessionStatsRemoteShortSeq_Type()
)
pppDeadSessionStatsRemoteShortSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRemoteShortSeq.setStatus("current")
_PppDeadSessionStatsRemoteAuthenticated_Type = Boolean
_PppDeadSessionStatsRemoteAuthenticated_Object = MibTableColumn
pppDeadSessionStatsRemoteAuthenticated = _PppDeadSessionStatsRemoteAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 301),
    _PppDeadSessionStatsRemoteAuthenticated_Type()
)
pppDeadSessionStatsRemoteAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRemoteAuthenticated.setStatus("current")


class _PppDeadSessionStatsIPCPState_Type(Integer32):
    """Custom type pppDeadSessionStatsIPCPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ackRcvd", 7),
          ("ackSent", 8),
          ("closed", 2),
          ("closing", 4),
          ("initial", 0),
          ("opened", 9),
          ("reqSent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_PppDeadSessionStatsIPCPState_Type.__name__ = "Integer32"
_PppDeadSessionStatsIPCPState_Object = MibTableColumn
pppDeadSessionStatsIPCPState = _PppDeadSessionStatsIPCPState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 401),
    _PppDeadSessionStatsIPCPState_Type()
)
pppDeadSessionStatsIPCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsIPCPState.setStatus("current")
_PppDeadSessionStatsLocalIPAddress_Type = Integer32
_PppDeadSessionStatsLocalIPAddress_Object = MibTableColumn
pppDeadSessionStatsLocalIPAddress = _PppDeadSessionStatsLocalIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 402),
    _PppDeadSessionStatsLocalIPAddress_Type()
)
pppDeadSessionStatsLocalIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsLocalIPAddress.setStatus("current")
_PppDeadSessionStatsRemoteIPAddress_Type = Integer32
_PppDeadSessionStatsRemoteIPAddress_Object = MibTableColumn
pppDeadSessionStatsRemoteIPAddress = _PppDeadSessionStatsRemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 403),
    _PppDeadSessionStatsRemoteIPAddress_Type()
)
pppDeadSessionStatsRemoteIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRemoteIPAddress.setStatus("current")
_PppDeadSessionStatsDNSAddress1_Type = Integer32
_PppDeadSessionStatsDNSAddress1_Object = MibTableColumn
pppDeadSessionStatsDNSAddress1 = _PppDeadSessionStatsDNSAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 404),
    _PppDeadSessionStatsDNSAddress1_Type()
)
pppDeadSessionStatsDNSAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsDNSAddress1.setStatus("current")
_PppDeadSessionStatsDNSAddress2_Type = Integer32
_PppDeadSessionStatsDNSAddress2_Object = MibTableColumn
pppDeadSessionStatsDNSAddress2 = _PppDeadSessionStatsDNSAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 405),
    _PppDeadSessionStatsDNSAddress2_Type()
)
pppDeadSessionStatsDNSAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsDNSAddress2.setStatus("current")
_PppDeadSessionStatsNBNSAddress1_Type = Integer32
_PppDeadSessionStatsNBNSAddress1_Object = MibTableColumn
pppDeadSessionStatsNBNSAddress1 = _PppDeadSessionStatsNBNSAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 406),
    _PppDeadSessionStatsNBNSAddress1_Type()
)
pppDeadSessionStatsNBNSAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsNBNSAddress1.setStatus("current")
_PppDeadSessionStatsNBNSAddress2_Type = Integer32
_PppDeadSessionStatsNBNSAddress2_Object = MibTableColumn
pppDeadSessionStatsNBNSAddress2 = _PppDeadSessionStatsNBNSAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 407),
    _PppDeadSessionStatsNBNSAddress2_Type()
)
pppDeadSessionStatsNBNSAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsNBNSAddress2.setStatus("current")
_PppDeadSessionStatsLocalVJ_Type = Boolean
_PppDeadSessionStatsLocalVJ_Object = MibTableColumn
pppDeadSessionStatsLocalVJ = _PppDeadSessionStatsLocalVJ_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 408),
    _PppDeadSessionStatsLocalVJ_Type()
)
pppDeadSessionStatsLocalVJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsLocalVJ.setStatus("current")
_PppDeadSessionStatsLocalVJSlots_Type = Integer32
_PppDeadSessionStatsLocalVJSlots_Object = MibTableColumn
pppDeadSessionStatsLocalVJSlots = _PppDeadSessionStatsLocalVJSlots_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 409),
    _PppDeadSessionStatsLocalVJSlots_Type()
)
pppDeadSessionStatsLocalVJSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsLocalVJSlots.setStatus("current")
_PppDeadSessionStatsRemoteVJ_Type = Boolean
_PppDeadSessionStatsRemoteVJ_Object = MibTableColumn
pppDeadSessionStatsRemoteVJ = _PppDeadSessionStatsRemoteVJ_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 410),
    _PppDeadSessionStatsRemoteVJ_Type()
)
pppDeadSessionStatsRemoteVJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRemoteVJ.setStatus("current")
_PppDeadSessionStatsRemoteVJSlots_Type = Integer32
_PppDeadSessionStatsRemoteVJSlots_Object = MibTableColumn
pppDeadSessionStatsRemoteVJSlots = _PppDeadSessionStatsRemoteVJSlots_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 411),
    _PppDeadSessionStatsRemoteVJSlots_Type()
)
pppDeadSessionStatsRemoteVJSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRemoteVJSlots.setStatus("current")


class _PppDeadSessionStatsIPXCPState_Type(Integer32):
    """Custom type pppDeadSessionStatsIPXCPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ackRcvd", 7),
          ("ackSent", 8),
          ("closed", 2),
          ("closing", 4),
          ("initial", 0),
          ("opened", 9),
          ("reqSent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_PppDeadSessionStatsIPXCPState_Type.__name__ = "Integer32"
_PppDeadSessionStatsIPXCPState_Object = MibTableColumn
pppDeadSessionStatsIPXCPState = _PppDeadSessionStatsIPXCPState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 451),
    _PppDeadSessionStatsIPXCPState_Type()
)
pppDeadSessionStatsIPXCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsIPXCPState.setStatus("current")
_PppDeadSessionStatsRemoteIPXNetwork_Type = Integer32
_PppDeadSessionStatsRemoteIPXNetwork_Object = MibTableColumn
pppDeadSessionStatsRemoteIPXNetwork = _PppDeadSessionStatsRemoteIPXNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 452),
    _PppDeadSessionStatsRemoteIPXNetwork_Type()
)
pppDeadSessionStatsRemoteIPXNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRemoteIPXNetwork.setStatus("current")


class _PppDeadSessionStatsRemoteIPXNode_Type(DisplayString):
    """Custom type pppDeadSessionStatsRemoteIPXNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_PppDeadSessionStatsRemoteIPXNode_Type.__name__ = "DisplayString"
_PppDeadSessionStatsRemoteIPXNode_Object = MibTableColumn
pppDeadSessionStatsRemoteIPXNode = _PppDeadSessionStatsRemoteIPXNode_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 453),
    _PppDeadSessionStatsRemoteIPXNode_Type()
)
pppDeadSessionStatsRemoteIPXNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRemoteIPXNode.setStatus("current")


class _PppDeadSessionStatsCCPState_Type(Integer32):
    """Custom type pppDeadSessionStatsCCPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ackRcvd", 7),
          ("ackSent", 8),
          ("closed", 2),
          ("closing", 4),
          ("initial", 0),
          ("opened", 9),
          ("reqSent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_PppDeadSessionStatsCCPState_Type.__name__ = "Integer32"
_PppDeadSessionStatsCCPState_Object = MibTableColumn
pppDeadSessionStatsCCPState = _PppDeadSessionStatsCCPState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 501),
    _PppDeadSessionStatsCCPState_Type()
)
pppDeadSessionStatsCCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsCCPState.setStatus("current")


class _PppDeadSessionStatsLocalCompressAlgorithm_Type(Integer32):
    """Custom type pppDeadSessionStatsLocalCompressAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mppc", 2),
          ("none", 0),
          ("stac3", 3),
          ("stac4", 1))
    )


_PppDeadSessionStatsLocalCompressAlgorithm_Type.__name__ = "Integer32"
_PppDeadSessionStatsLocalCompressAlgorithm_Object = MibTableColumn
pppDeadSessionStatsLocalCompressAlgorithm = _PppDeadSessionStatsLocalCompressAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 502),
    _PppDeadSessionStatsLocalCompressAlgorithm_Type()
)
pppDeadSessionStatsLocalCompressAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsLocalCompressAlgorithm.setStatus("current")
_PppDeadSessionStatsLocalCompressHistories_Type = Integer32
_PppDeadSessionStatsLocalCompressHistories_Object = MibTableColumn
pppDeadSessionStatsLocalCompressHistories = _PppDeadSessionStatsLocalCompressHistories_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 503),
    _PppDeadSessionStatsLocalCompressHistories_Type()
)
pppDeadSessionStatsLocalCompressHistories.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsLocalCompressHistories.setStatus("current")


class _PppDeadSessionStatsRemoteCompressAlgorithm_Type(Integer32):
    """Custom type pppDeadSessionStatsRemoteCompressAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mppc", 2),
          ("none", 0),
          ("stac3", 3),
          ("stac4", 1))
    )


_PppDeadSessionStatsRemoteCompressAlgorithm_Type.__name__ = "Integer32"
_PppDeadSessionStatsRemoteCompressAlgorithm_Object = MibTableColumn
pppDeadSessionStatsRemoteCompressAlgorithm = _PppDeadSessionStatsRemoteCompressAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 504),
    _PppDeadSessionStatsRemoteCompressAlgorithm_Type()
)
pppDeadSessionStatsRemoteCompressAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRemoteCompressAlgorithm.setStatus("current")
_PppDeadSessionStatsRemoteCompressHistories_Type = Integer32
_PppDeadSessionStatsRemoteCompressHistories_Object = MibTableColumn
pppDeadSessionStatsRemoteCompressHistories = _PppDeadSessionStatsRemoteCompressHistories_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 505),
    _PppDeadSessionStatsRemoteCompressHistories_Type()
)
pppDeadSessionStatsRemoteCompressHistories.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRemoteCompressHistories.setStatus("current")
_PppDeadSessionStatsMultilinkActive_Type = Boolean
_PppDeadSessionStatsMultilinkActive_Object = MibTableColumn
pppDeadSessionStatsMultilinkActive = _PppDeadSessionStatsMultilinkActive_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 601),
    _PppDeadSessionStatsMultilinkActive_Type()
)
pppDeadSessionStatsMultilinkActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsMultilinkActive.setStatus("current")
_PppDeadSessionStatsMultilinkLinks_Type = Integer32
_PppDeadSessionStatsMultilinkLinks_Object = MibTableColumn
pppDeadSessionStatsMultilinkLinks = _PppDeadSessionStatsMultilinkLinks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 602),
    _PppDeadSessionStatsMultilinkLinks_Type()
)
pppDeadSessionStatsMultilinkLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsMultilinkLinks.setStatus("current")
_PppDeadSessionStatsTotalTxSpeed_Type = Integer32
_PppDeadSessionStatsTotalTxSpeed_Object = MibTableColumn
pppDeadSessionStatsTotalTxSpeed = _PppDeadSessionStatsTotalTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 603),
    _PppDeadSessionStatsTotalTxSpeed_Type()
)
pppDeadSessionStatsTotalTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsTotalTxSpeed.setStatus("current")
_PppDeadSessionStatsTotalRxSpeed_Type = Integer32
_PppDeadSessionStatsTotalRxSpeed_Object = MibTableColumn
pppDeadSessionStatsTotalRxSpeed = _PppDeadSessionStatsTotalRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 604),
    _PppDeadSessionStatsTotalRxSpeed_Type()
)
pppDeadSessionStatsTotalRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsTotalRxSpeed.setStatus("current")
_PppDeadSessionStatsMLPFragmentsReceived_Type = Integer32
_PppDeadSessionStatsMLPFragmentsReceived_Object = MibTableColumn
pppDeadSessionStatsMLPFragmentsReceived = _PppDeadSessionStatsMLPFragmentsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 605),
    _PppDeadSessionStatsMLPFragmentsReceived_Type()
)
pppDeadSessionStatsMLPFragmentsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsMLPFragmentsReceived.setStatus("current")
_PppDeadSessionStatsMLPFragmentsMissing_Type = Integer32
_PppDeadSessionStatsMLPFragmentsMissing_Object = MibTableColumn
pppDeadSessionStatsMLPFragmentsMissing = _PppDeadSessionStatsMLPFragmentsMissing_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 606),
    _PppDeadSessionStatsMLPFragmentsMissing_Type()
)
pppDeadSessionStatsMLPFragmentsMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsMLPFragmentsMissing.setStatus("current")
_PppDeadSessionStatsMLPFragmentsDropped_Type = Integer32
_PppDeadSessionStatsMLPFragmentsDropped_Object = MibTableColumn
pppDeadSessionStatsMLPFragmentsDropped = _PppDeadSessionStatsMLPFragmentsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 607),
    _PppDeadSessionStatsMLPFragmentsDropped_Type()
)
pppDeadSessionStatsMLPFragmentsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsMLPFragmentsDropped.setStatus("current")
_PppDeadSessionStatsMLPPacketsReassembled_Type = Integer32
_PppDeadSessionStatsMLPPacketsReassembled_Object = MibTableColumn
pppDeadSessionStatsMLPPacketsReassembled = _PppDeadSessionStatsMLPPacketsReassembled_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 608),
    _PppDeadSessionStatsMLPPacketsReassembled_Type()
)
pppDeadSessionStatsMLPPacketsReassembled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsMLPPacketsReassembled.setStatus("current")
_PppDeadSessionStatsMLPPacketsNull_Type = Integer32
_PppDeadSessionStatsMLPPacketsNull_Object = MibTableColumn
pppDeadSessionStatsMLPPacketsNull = _PppDeadSessionStatsMLPPacketsNull_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 609),
    _PppDeadSessionStatsMLPPacketsNull_Type()
)
pppDeadSessionStatsMLPPacketsNull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsMLPPacketsNull.setStatus("current")
_PppDeadSessionStatsMultilinkLinksAdded_Type = Integer32
_PppDeadSessionStatsMultilinkLinksAdded_Object = MibTableColumn
pppDeadSessionStatsMultilinkLinksAdded = _PppDeadSessionStatsMultilinkLinksAdded_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 610),
    _PppDeadSessionStatsMultilinkLinksAdded_Type()
)
pppDeadSessionStatsMultilinkLinksAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsMultilinkLinksAdded.setStatus("current")
_PppDeadSessionStatsMultilinkLinksRemoved_Type = Integer32
_PppDeadSessionStatsMultilinkLinksRemoved_Object = MibTableColumn
pppDeadSessionStatsMultilinkLinksRemoved = _PppDeadSessionStatsMultilinkLinksRemoved_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 611),
    _PppDeadSessionStatsMultilinkLinksRemoved_Type()
)
pppDeadSessionStatsMultilinkLinksRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsMultilinkLinksRemoved.setStatus("current")
_PppDeadSessionStatsMultilinkLinksMax_Type = Integer32
_PppDeadSessionStatsMultilinkLinksMax_Object = MibTableColumn
pppDeadSessionStatsMultilinkLinksMax = _PppDeadSessionStatsMultilinkLinksMax_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 612),
    _PppDeadSessionStatsMultilinkLinksMax_Type()
)
pppDeadSessionStatsMultilinkLinksMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsMultilinkLinksMax.setStatus("current")
_PppDeadSessionStatsMultilinkLinksMaxConfig_Type = Integer32
_PppDeadSessionStatsMultilinkLinksMaxConfig_Object = MibTableColumn
pppDeadSessionStatsMultilinkLinksMaxConfig = _PppDeadSessionStatsMultilinkLinksMaxConfig_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 613),
    _PppDeadSessionStatsMultilinkLinksMaxConfig_Type()
)
pppDeadSessionStatsMultilinkLinksMaxConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsMultilinkLinksMaxConfig.setStatus("current")
_PppDeadSessionStatsTxPackets_Type = Integer32
_PppDeadSessionStatsTxPackets_Object = MibTableColumn
pppDeadSessionStatsTxPackets = _PppDeadSessionStatsTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1001),
    _PppDeadSessionStatsTxPackets_Type()
)
pppDeadSessionStatsTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsTxPackets.setStatus("current")
_PppDeadSessionStatsTxPacketsDropped_Type = Integer32
_PppDeadSessionStatsTxPacketsDropped_Object = MibTableColumn
pppDeadSessionStatsTxPacketsDropped = _PppDeadSessionStatsTxPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1002),
    _PppDeadSessionStatsTxPacketsDropped_Type()
)
pppDeadSessionStatsTxPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsTxPacketsDropped.setStatus("current")
_PppDeadSessionStatsTxBytes_Type = Integer32
_PppDeadSessionStatsTxBytes_Object = MibTableColumn
pppDeadSessionStatsTxBytes = _PppDeadSessionStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1003),
    _PppDeadSessionStatsTxBytes_Type()
)
pppDeadSessionStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsTxBytes.setStatus("current")
_PppDeadSessionStatsRxPackets_Type = Integer32
_PppDeadSessionStatsRxPackets_Object = MibTableColumn
pppDeadSessionStatsRxPackets = _PppDeadSessionStatsRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1004),
    _PppDeadSessionStatsRxPackets_Type()
)
pppDeadSessionStatsRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRxPackets.setStatus("current")
_PppDeadSessionStatsRxPacketsDropped_Type = Integer32
_PppDeadSessionStatsRxPacketsDropped_Object = MibTableColumn
pppDeadSessionStatsRxPacketsDropped = _PppDeadSessionStatsRxPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1005),
    _PppDeadSessionStatsRxPacketsDropped_Type()
)
pppDeadSessionStatsRxPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRxPacketsDropped.setStatus("current")
_PppDeadSessionStatsRxBytes_Type = Integer32
_PppDeadSessionStatsRxBytes_Object = MibTableColumn
pppDeadSessionStatsRxBytes = _PppDeadSessionStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1006),
    _PppDeadSessionStatsRxBytes_Type()
)
pppDeadSessionStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRxBytes.setStatus("current")
_PppDeadSessionStatsTxCompressing_Type = Boolean
_PppDeadSessionStatsTxCompressing_Object = MibTableColumn
pppDeadSessionStatsTxCompressing = _PppDeadSessionStatsTxCompressing_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1101),
    _PppDeadSessionStatsTxCompressing_Type()
)
pppDeadSessionStatsTxCompressing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsTxCompressing.setStatus("current")
_PppDeadSessionStatsTxBytesBeforeCompress_Type = Integer32
_PppDeadSessionStatsTxBytesBeforeCompress_Object = MibTableColumn
pppDeadSessionStatsTxBytesBeforeCompress = _PppDeadSessionStatsTxBytesBeforeCompress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1102),
    _PppDeadSessionStatsTxBytesBeforeCompress_Type()
)
pppDeadSessionStatsTxBytesBeforeCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsTxBytesBeforeCompress.setStatus("current")
_PppDeadSessionStatsTxBytesAfterCompress_Type = Integer32
_PppDeadSessionStatsTxBytesAfterCompress_Object = MibTableColumn
pppDeadSessionStatsTxBytesAfterCompress = _PppDeadSessionStatsTxBytesAfterCompress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1103),
    _PppDeadSessionStatsTxBytesAfterCompress_Type()
)
pppDeadSessionStatsTxBytesAfterCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsTxBytesAfterCompress.setStatus("current")
_PppDeadSessionStatsTxBytesUncompressed_Type = Integer32
_PppDeadSessionStatsTxBytesUncompressed_Object = MibTableColumn
pppDeadSessionStatsTxBytesUncompressed = _PppDeadSessionStatsTxBytesUncompressed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1104),
    _PppDeadSessionStatsTxBytesUncompressed_Type()
)
pppDeadSessionStatsTxBytesUncompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsTxBytesUncompressed.setStatus("current")
_PppDeadSessionStatsRxBytesBeforeCompress_Type = Integer32
_PppDeadSessionStatsRxBytesBeforeCompress_Object = MibTableColumn
pppDeadSessionStatsRxBytesBeforeCompress = _PppDeadSessionStatsRxBytesBeforeCompress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1105),
    _PppDeadSessionStatsRxBytesBeforeCompress_Type()
)
pppDeadSessionStatsRxBytesBeforeCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRxBytesBeforeCompress.setStatus("current")
_PppDeadSessionStatsRxBytesAfterCompress_Type = Integer32
_PppDeadSessionStatsRxBytesAfterCompress_Object = MibTableColumn
pppDeadSessionStatsRxBytesAfterCompress = _PppDeadSessionStatsRxBytesAfterCompress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1106),
    _PppDeadSessionStatsRxBytesAfterCompress_Type()
)
pppDeadSessionStatsRxBytesAfterCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRxBytesAfterCompress.setStatus("current")
_PppDeadSessionStatsRxBytesUncompressed_Type = Integer32
_PppDeadSessionStatsRxBytesUncompressed_Object = MibTableColumn
pppDeadSessionStatsRxBytesUncompressed = _PppDeadSessionStatsRxBytesUncompressed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1107),
    _PppDeadSessionStatsRxBytesUncompressed_Type()
)
pppDeadSessionStatsRxBytesUncompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRxBytesUncompressed.setStatus("current")
_PppDeadSessionStatsRxCompPacketsDropped_Type = Integer32
_PppDeadSessionStatsRxCompPacketsDropped_Object = MibTableColumn
pppDeadSessionStatsRxCompPacketsDropped = _PppDeadSessionStatsRxCompPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1108),
    _PppDeadSessionStatsRxCompPacketsDropped_Type()
)
pppDeadSessionStatsRxCompPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRxCompPacketsDropped.setStatus("current")
_PppDeadSessionStatsCCPResetsSent_Type = Integer32
_PppDeadSessionStatsCCPResetsSent_Object = MibTableColumn
pppDeadSessionStatsCCPResetsSent = _PppDeadSessionStatsCCPResetsSent_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1109),
    _PppDeadSessionStatsCCPResetsSent_Type()
)
pppDeadSessionStatsCCPResetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsCCPResetsSent.setStatus("current")
_PppDeadSessionStatsCCPResetsReceived_Type = Integer32
_PppDeadSessionStatsCCPResetsReceived_Object = MibTableColumn
pppDeadSessionStatsCCPResetsReceived = _PppDeadSessionStatsCCPResetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1110),
    _PppDeadSessionStatsCCPResetsReceived_Type()
)
pppDeadSessionStatsCCPResetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsCCPResetsReceived.setStatus("current")
_PppDeadSessionStatsRxResourceErrors_Type = Integer32
_PppDeadSessionStatsRxResourceErrors_Object = MibTableColumn
pppDeadSessionStatsRxResourceErrors = _PppDeadSessionStatsRxResourceErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1201),
    _PppDeadSessionStatsRxResourceErrors_Type()
)
pppDeadSessionStatsRxResourceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRxResourceErrors.setStatus("current")
_PppDeadSessionStatsRxQueueErrors_Type = Integer32
_PppDeadSessionStatsRxQueueErrors_Object = MibTableColumn
pppDeadSessionStatsRxQueueErrors = _PppDeadSessionStatsRxQueueErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1202),
    _PppDeadSessionStatsRxQueueErrors_Type()
)
pppDeadSessionStatsRxQueueErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRxQueueErrors.setStatus("current")
_PppDeadSessionStatsRxCRCErrors_Type = Integer32
_PppDeadSessionStatsRxCRCErrors_Object = MibTableColumn
pppDeadSessionStatsRxCRCErrors = _PppDeadSessionStatsRxCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1203),
    _PppDeadSessionStatsRxCRCErrors_Type()
)
pppDeadSessionStatsRxCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRxCRCErrors.setStatus("current")
_PppDeadSessionStatsRxAbortErrors_Type = Integer32
_PppDeadSessionStatsRxAbortErrors_Object = MibTableColumn
pppDeadSessionStatsRxAbortErrors = _PppDeadSessionStatsRxAbortErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1204),
    _PppDeadSessionStatsRxAbortErrors_Type()
)
pppDeadSessionStatsRxAbortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRxAbortErrors.setStatus("current")
_PppDeadSessionStatsRxOverrunErrors_Type = Integer32
_PppDeadSessionStatsRxOverrunErrors_Object = MibTableColumn
pppDeadSessionStatsRxOverrunErrors = _PppDeadSessionStatsRxOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1205),
    _PppDeadSessionStatsRxOverrunErrors_Type()
)
pppDeadSessionStatsRxOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRxOverrunErrors.setStatus("current")
_PppDeadSessionStatsRxBigErrors_Type = Integer32
_PppDeadSessionStatsRxBigErrors_Object = MibTableColumn
pppDeadSessionStatsRxBigErrors = _PppDeadSessionStatsRxBigErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1206),
    _PppDeadSessionStatsRxBigErrors_Type()
)
pppDeadSessionStatsRxBigErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRxBigErrors.setStatus("current")
_PppDeadSessionStatsRxSmallErrors_Type = Integer32
_PppDeadSessionStatsRxSmallErrors_Object = MibTableColumn
pppDeadSessionStatsRxSmallErrors = _PppDeadSessionStatsRxSmallErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1207),
    _PppDeadSessionStatsRxSmallErrors_Type()
)
pppDeadSessionStatsRxSmallErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRxSmallErrors.setStatus("current")
_PppDeadSessionStatsRxAlignErrors_Type = Integer32
_PppDeadSessionStatsRxAlignErrors_Object = MibTableColumn
pppDeadSessionStatsRxAlignErrors = _PppDeadSessionStatsRxAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1208),
    _PppDeadSessionStatsRxAlignErrors_Type()
)
pppDeadSessionStatsRxAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsRxAlignErrors.setStatus("current")
_PppDeadSessionStatsTxResourceErrors_Type = Integer32
_PppDeadSessionStatsTxResourceErrors_Object = MibTableColumn
pppDeadSessionStatsTxResourceErrors = _PppDeadSessionStatsTxResourceErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1209),
    _PppDeadSessionStatsTxResourceErrors_Type()
)
pppDeadSessionStatsTxResourceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsTxResourceErrors.setStatus("current")
_PppDeadSessionStatsTxQueueErrors_Type = Integer32
_PppDeadSessionStatsTxQueueErrors_Object = MibTableColumn
pppDeadSessionStatsTxQueueErrors = _PppDeadSessionStatsTxQueueErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1210),
    _PppDeadSessionStatsTxQueueErrors_Type()
)
pppDeadSessionStatsTxQueueErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsTxQueueErrors.setStatus("current")
_PppDeadSessionStatsTxBigErrors_Type = Integer32
_PppDeadSessionStatsTxBigErrors_Object = MibTableColumn
pppDeadSessionStatsTxBigErrors = _PppDeadSessionStatsTxBigErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1211),
    _PppDeadSessionStatsTxBigErrors_Type()
)
pppDeadSessionStatsTxBigErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsTxBigErrors.setStatus("current")
_PppDeadSessionStatsTxUnderrunErrors_Type = Integer32
_PppDeadSessionStatsTxUnderrunErrors_Object = MibTableColumn
pppDeadSessionStatsTxUnderrunErrors = _PppDeadSessionStatsTxUnderrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1320, 1, 1212),
    _PppDeadSessionStatsTxUnderrunErrors_Type()
)
pppDeadSessionStatsTxUnderrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppDeadSessionStatsTxUnderrunErrors.setStatus("current")
_L2FTunnelStatusActiveTable_Object = MibTable
l2FTunnelStatusActiveTable = _L2FTunnelStatusActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1351)
)
if mibBuilder.loadTexts:
    l2FTunnelStatusActiveTable.setStatus("current")
_L2FTunnelStatusActiveEntry_Object = MibTableRow
l2FTunnelStatusActiveEntry = _L2FTunnelStatusActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1351, 1)
)
l2FTunnelStatusActiveEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "l2FTunnelStatusActiveLocalCLID"),
)
if mibBuilder.loadTexts:
    l2FTunnelStatusActiveEntry.setStatus("current")
_L2FTunnelStatusActiveLocalCLID_Type = Integer32
_L2FTunnelStatusActiveLocalCLID_Object = MibTableColumn
l2FTunnelStatusActiveLocalCLID = _L2FTunnelStatusActiveLocalCLID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1351, 1, 1),
    _L2FTunnelStatusActiveLocalCLID_Type()
)
l2FTunnelStatusActiveLocalCLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusActiveLocalCLID.setStatus("current")
_L2FTunnelStatusActiveRemoteCLID_Type = Integer32
_L2FTunnelStatusActiveRemoteCLID_Object = MibTableColumn
l2FTunnelStatusActiveRemoteCLID = _L2FTunnelStatusActiveRemoteCLID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1351, 1, 2),
    _L2FTunnelStatusActiveRemoteCLID_Type()
)
l2FTunnelStatusActiveRemoteCLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusActiveRemoteCLID.setStatus("current")
_L2FTunnelStatusActiveLocalAddress_Type = IpAddress
_L2FTunnelStatusActiveLocalAddress_Object = MibTableColumn
l2FTunnelStatusActiveLocalAddress = _L2FTunnelStatusActiveLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1351, 1, 3),
    _L2FTunnelStatusActiveLocalAddress_Type()
)
l2FTunnelStatusActiveLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusActiveLocalAddress.setStatus("current")
_L2FTunnelStatusActiveRemoteAddress_Type = IpAddress
_L2FTunnelStatusActiveRemoteAddress_Object = MibTableColumn
l2FTunnelStatusActiveRemoteAddress = _L2FTunnelStatusActiveRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1351, 1, 4),
    _L2FTunnelStatusActiveRemoteAddress_Type()
)
l2FTunnelStatusActiveRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusActiveRemoteAddress.setStatus("current")


class _L2FTunnelStatusActiveState_Type(Integer32):
    """Custom type l2FTunnelStatusActiveState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("close1", 4),
          ("close2", 5),
          ("idle", 0),
          ("opened", 3),
          ("start1", 1),
          ("start2", 2))
    )


_L2FTunnelStatusActiveState_Type.__name__ = "Integer32"
_L2FTunnelStatusActiveState_Object = MibTableColumn
l2FTunnelStatusActiveState = _L2FTunnelStatusActiveState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1351, 1, 5),
    _L2FTunnelStatusActiveState_Type()
)
l2FTunnelStatusActiveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusActiveState.setStatus("current")
_L2FTunnelStatusActiveUpTime_Type = Integer32
_L2FTunnelStatusActiveUpTime_Object = MibTableColumn
l2FTunnelStatusActiveUpTime = _L2FTunnelStatusActiveUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1351, 1, 6),
    _L2FTunnelStatusActiveUpTime_Type()
)
l2FTunnelStatusActiveUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusActiveUpTime.setStatus("current")
_L2FTunnelStatusActiveActiveLinks_Type = Integer32
_L2FTunnelStatusActiveActiveLinks_Object = MibTableColumn
l2FTunnelStatusActiveActiveLinks = _L2FTunnelStatusActiveActiveLinks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1351, 1, 7),
    _L2FTunnelStatusActiveActiveLinks_Type()
)
l2FTunnelStatusActiveActiveLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusActiveActiveLinks.setStatus("current")
_L2FTunnelStatusActiveMaxActiveLinks_Type = Integer32
_L2FTunnelStatusActiveMaxActiveLinks_Object = MibTableColumn
l2FTunnelStatusActiveMaxActiveLinks = _L2FTunnelStatusActiveMaxActiveLinks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1351, 1, 8),
    _L2FTunnelStatusActiveMaxActiveLinks_Type()
)
l2FTunnelStatusActiveMaxActiveLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusActiveMaxActiveLinks.setStatus("current")
_L2FTunnelStatusActivePendingLinks_Type = Integer32
_L2FTunnelStatusActivePendingLinks_Object = MibTableColumn
l2FTunnelStatusActivePendingLinks = _L2FTunnelStatusActivePendingLinks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1351, 1, 9),
    _L2FTunnelStatusActivePendingLinks_Type()
)
l2FTunnelStatusActivePendingLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusActivePendingLinks.setStatus("current")
_L2FTunnelStatusActiveLinksAdded_Type = Integer32
_L2FTunnelStatusActiveLinksAdded_Object = MibTableColumn
l2FTunnelStatusActiveLinksAdded = _L2FTunnelStatusActiveLinksAdded_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1351, 1, 10),
    _L2FTunnelStatusActiveLinksAdded_Type()
)
l2FTunnelStatusActiveLinksAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusActiveLinksAdded.setStatus("current")
_L2FTunnelStatusActiveLinksAddedSuccessfully_Type = Integer32
_L2FTunnelStatusActiveLinksAddedSuccessfully_Object = MibTableColumn
l2FTunnelStatusActiveLinksAddedSuccessfully = _L2FTunnelStatusActiveLinksAddedSuccessfully_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1351, 1, 11),
    _L2FTunnelStatusActiveLinksAddedSuccessfully_Type()
)
l2FTunnelStatusActiveLinksAddedSuccessfully.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusActiveLinksAddedSuccessfully.setStatus("current")
_L2FTunnelStatusActiveLinksAddedUnsuccessfully_Type = Integer32
_L2FTunnelStatusActiveLinksAddedUnsuccessfully_Object = MibTableColumn
l2FTunnelStatusActiveLinksAddedUnsuccessfully = _L2FTunnelStatusActiveLinksAddedUnsuccessfully_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1351, 1, 12),
    _L2FTunnelStatusActiveLinksAddedUnsuccessfully_Type()
)
l2FTunnelStatusActiveLinksAddedUnsuccessfully.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusActiveLinksAddedUnsuccessfully.setStatus("current")
_L2FTunnelStatusActiveLinksRemoved_Type = Integer32
_L2FTunnelStatusActiveLinksRemoved_Object = MibTableColumn
l2FTunnelStatusActiveLinksRemoved = _L2FTunnelStatusActiveLinksRemoved_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1351, 1, 13),
    _L2FTunnelStatusActiveLinksRemoved_Type()
)
l2FTunnelStatusActiveLinksRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusActiveLinksRemoved.setStatus("current")
_L2FTunnelStatusActiveGotOpened_Type = Boolean
_L2FTunnelStatusActiveGotOpened_Object = MibTableColumn
l2FTunnelStatusActiveGotOpened = _L2FTunnelStatusActiveGotOpened_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1351, 1, 14),
    _L2FTunnelStatusActiveGotOpened_Type()
)
l2FTunnelStatusActiveGotOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusActiveGotOpened.setStatus("current")
_L2FTunnelStatusActiveVPOP_Type = Integer32
_L2FTunnelStatusActiveVPOP_Object = MibTableColumn
l2FTunnelStatusActiveVPOP = _L2FTunnelStatusActiveVPOP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1351, 1, 15),
    _L2FTunnelStatusActiveVPOP_Type()
)
l2FTunnelStatusActiveVPOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusActiveVPOP.setStatus("current")
_L2FTunnelStatusActiveL2FTermationCause_Type = Integer32
_L2FTunnelStatusActiveL2FTermationCause_Object = MibTableColumn
l2FTunnelStatusActiveL2FTermationCause = _L2FTunnelStatusActiveL2FTermationCause_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1351, 1, 16),
    _L2FTunnelStatusActiveL2FTermationCause_Type()
)
l2FTunnelStatusActiveL2FTermationCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusActiveL2FTermationCause.setStatus("current")
_L2FTunnelStatusInactiveTable_Object = MibTable
l2FTunnelStatusInactiveTable = _L2FTunnelStatusInactiveTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1352)
)
if mibBuilder.loadTexts:
    l2FTunnelStatusInactiveTable.setStatus("current")
_L2FTunnelStatusInactiveEntry_Object = MibTableRow
l2FTunnelStatusInactiveEntry = _L2FTunnelStatusInactiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1352, 1)
)
l2FTunnelStatusInactiveEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "l2FTunnelStatusInactiveLocalCLID"),
)
if mibBuilder.loadTexts:
    l2FTunnelStatusInactiveEntry.setStatus("current")
_L2FTunnelStatusInactiveLocalCLID_Type = Integer32
_L2FTunnelStatusInactiveLocalCLID_Object = MibTableColumn
l2FTunnelStatusInactiveLocalCLID = _L2FTunnelStatusInactiveLocalCLID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1352, 1, 1),
    _L2FTunnelStatusInactiveLocalCLID_Type()
)
l2FTunnelStatusInactiveLocalCLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusInactiveLocalCLID.setStatus("current")
_L2FTunnelStatusInactiveRemoteCLID_Type = Integer32
_L2FTunnelStatusInactiveRemoteCLID_Object = MibTableColumn
l2FTunnelStatusInactiveRemoteCLID = _L2FTunnelStatusInactiveRemoteCLID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1352, 1, 2),
    _L2FTunnelStatusInactiveRemoteCLID_Type()
)
l2FTunnelStatusInactiveRemoteCLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusInactiveRemoteCLID.setStatus("current")
_L2FTunnelStatusInactiveLocalAddress_Type = IpAddress
_L2FTunnelStatusInactiveLocalAddress_Object = MibTableColumn
l2FTunnelStatusInactiveLocalAddress = _L2FTunnelStatusInactiveLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1352, 1, 3),
    _L2FTunnelStatusInactiveLocalAddress_Type()
)
l2FTunnelStatusInactiveLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusInactiveLocalAddress.setStatus("current")
_L2FTunnelStatusInactiveRemoteAddress_Type = IpAddress
_L2FTunnelStatusInactiveRemoteAddress_Object = MibTableColumn
l2FTunnelStatusInactiveRemoteAddress = _L2FTunnelStatusInactiveRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1352, 1, 4),
    _L2FTunnelStatusInactiveRemoteAddress_Type()
)
l2FTunnelStatusInactiveRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusInactiveRemoteAddress.setStatus("current")


class _L2FTunnelStatusInactiveState_Type(Integer32):
    """Custom type l2FTunnelStatusInactiveState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("close1", 4),
          ("close2", 5),
          ("idle", 0),
          ("opened", 3),
          ("start1", 1),
          ("start2", 2))
    )


_L2FTunnelStatusInactiveState_Type.__name__ = "Integer32"
_L2FTunnelStatusInactiveState_Object = MibTableColumn
l2FTunnelStatusInactiveState = _L2FTunnelStatusInactiveState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1352, 1, 5),
    _L2FTunnelStatusInactiveState_Type()
)
l2FTunnelStatusInactiveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusInactiveState.setStatus("current")
_L2FTunnelStatusInactiveUpTime_Type = Integer32
_L2FTunnelStatusInactiveUpTime_Object = MibTableColumn
l2FTunnelStatusInactiveUpTime = _L2FTunnelStatusInactiveUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1352, 1, 6),
    _L2FTunnelStatusInactiveUpTime_Type()
)
l2FTunnelStatusInactiveUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusInactiveUpTime.setStatus("current")
_L2FTunnelStatusInactiveActiveLinks_Type = Integer32
_L2FTunnelStatusInactiveActiveLinks_Object = MibTableColumn
l2FTunnelStatusInactiveActiveLinks = _L2FTunnelStatusInactiveActiveLinks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1352, 1, 7),
    _L2FTunnelStatusInactiveActiveLinks_Type()
)
l2FTunnelStatusInactiveActiveLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusInactiveActiveLinks.setStatus("current")
_L2FTunnelStatusInactiveMaxActiveLinks_Type = Integer32
_L2FTunnelStatusInactiveMaxActiveLinks_Object = MibTableColumn
l2FTunnelStatusInactiveMaxActiveLinks = _L2FTunnelStatusInactiveMaxActiveLinks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1352, 1, 8),
    _L2FTunnelStatusInactiveMaxActiveLinks_Type()
)
l2FTunnelStatusInactiveMaxActiveLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusInactiveMaxActiveLinks.setStatus("current")
_L2FTunnelStatusInactivePendingLinks_Type = Integer32
_L2FTunnelStatusInactivePendingLinks_Object = MibTableColumn
l2FTunnelStatusInactivePendingLinks = _L2FTunnelStatusInactivePendingLinks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1352, 1, 9),
    _L2FTunnelStatusInactivePendingLinks_Type()
)
l2FTunnelStatusInactivePendingLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusInactivePendingLinks.setStatus("current")
_L2FTunnelStatusInactiveLinksAdded_Type = Integer32
_L2FTunnelStatusInactiveLinksAdded_Object = MibTableColumn
l2FTunnelStatusInactiveLinksAdded = _L2FTunnelStatusInactiveLinksAdded_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1352, 1, 10),
    _L2FTunnelStatusInactiveLinksAdded_Type()
)
l2FTunnelStatusInactiveLinksAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusInactiveLinksAdded.setStatus("current")
_L2FTunnelStatusInactiveLinksAddedSuccessfully_Type = Integer32
_L2FTunnelStatusInactiveLinksAddedSuccessfully_Object = MibTableColumn
l2FTunnelStatusInactiveLinksAddedSuccessfully = _L2FTunnelStatusInactiveLinksAddedSuccessfully_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1352, 1, 11),
    _L2FTunnelStatusInactiveLinksAddedSuccessfully_Type()
)
l2FTunnelStatusInactiveLinksAddedSuccessfully.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusInactiveLinksAddedSuccessfully.setStatus("current")
_L2FTunnelStatusInactiveLinksAddedUnsuccessfully_Type = Integer32
_L2FTunnelStatusInactiveLinksAddedUnsuccessfully_Object = MibTableColumn
l2FTunnelStatusInactiveLinksAddedUnsuccessfully = _L2FTunnelStatusInactiveLinksAddedUnsuccessfully_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1352, 1, 12),
    _L2FTunnelStatusInactiveLinksAddedUnsuccessfully_Type()
)
l2FTunnelStatusInactiveLinksAddedUnsuccessfully.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusInactiveLinksAddedUnsuccessfully.setStatus("current")
_L2FTunnelStatusInactiveLinksRemoved_Type = Integer32
_L2FTunnelStatusInactiveLinksRemoved_Object = MibTableColumn
l2FTunnelStatusInactiveLinksRemoved = _L2FTunnelStatusInactiveLinksRemoved_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1352, 1, 13),
    _L2FTunnelStatusInactiveLinksRemoved_Type()
)
l2FTunnelStatusInactiveLinksRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusInactiveLinksRemoved.setStatus("current")
_L2FTunnelStatusInactiveGotOpened_Type = Boolean
_L2FTunnelStatusInactiveGotOpened_Object = MibTableColumn
l2FTunnelStatusInactiveGotOpened = _L2FTunnelStatusInactiveGotOpened_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1352, 1, 14),
    _L2FTunnelStatusInactiveGotOpened_Type()
)
l2FTunnelStatusInactiveGotOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusInactiveGotOpened.setStatus("current")
_L2FTunnelStatusInactiveVPOP_Type = Integer32
_L2FTunnelStatusInactiveVPOP_Object = MibTableColumn
l2FTunnelStatusInactiveVPOP = _L2FTunnelStatusInactiveVPOP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1352, 1, 15),
    _L2FTunnelStatusInactiveVPOP_Type()
)
l2FTunnelStatusInactiveVPOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusInactiveVPOP.setStatus("current")
_L2FTunnelStatusInactiveL2FTermationCause_Type = Integer32
_L2FTunnelStatusInactiveL2FTermationCause_Object = MibTableColumn
l2FTunnelStatusInactiveL2FTermationCause = _L2FTunnelStatusInactiveL2FTermationCause_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1352, 1, 16),
    _L2FTunnelStatusInactiveL2FTermationCause_Type()
)
l2FTunnelStatusInactiveL2FTermationCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FTunnelStatusInactiveL2FTermationCause.setStatus("current")
_L2FLinkStatusTable_Object = MibTable
l2FLinkStatusTable = _L2FLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1353)
)
if mibBuilder.loadTexts:
    l2FLinkStatusTable.setStatus("current")
_L2FLinkStatusEntry_Object = MibTableRow
l2FLinkStatusEntry = _L2FLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1353, 1)
)
l2FLinkStatusEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "l2FLinkStatusLocalCLID"),
    (0, "APTIS-MONITOR-MIB", "l2FLinkStatusIndex"),
)
if mibBuilder.loadTexts:
    l2FLinkStatusEntry.setStatus("current")
_L2FLinkStatusLocalCLID_Type = Integer32
_L2FLinkStatusLocalCLID_Object = MibTableColumn
l2FLinkStatusLocalCLID = _L2FLinkStatusLocalCLID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1353, 1, 1),
    _L2FLinkStatusLocalCLID_Type()
)
l2FLinkStatusLocalCLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FLinkStatusLocalCLID.setStatus("current")
_L2FLinkStatusIndex_Type = Integer32
_L2FLinkStatusIndex_Object = MibTableColumn
l2FLinkStatusIndex = _L2FLinkStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1353, 1, 2),
    _L2FLinkStatusIndex_Type()
)
l2FLinkStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FLinkStatusIndex.setStatus("current")
_L2FLinkStatusSessionID_Type = Integer32
_L2FLinkStatusSessionID_Object = MibTableColumn
l2FLinkStatusSessionID = _L2FLinkStatusSessionID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1353, 1, 3),
    _L2FLinkStatusSessionID_Type()
)
l2FLinkStatusSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FLinkStatusSessionID.setStatus("current")
_L2FLinkStatusVPOP_Type = Integer32
_L2FLinkStatusVPOP_Object = MibTableColumn
l2FLinkStatusVPOP = _L2FLinkStatusVPOP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1353, 1, 4),
    _L2FLinkStatusVPOP_Type()
)
l2FLinkStatusVPOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FLinkStatusVPOP.setStatus("current")
_L2FLinkStatusMIDValue_Type = Integer32
_L2FLinkStatusMIDValue_Object = MibTableColumn
l2FLinkStatusMIDValue = _L2FLinkStatusMIDValue_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1353, 1, 11),
    _L2FLinkStatusMIDValue_Type()
)
l2FLinkStatusMIDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FLinkStatusMIDValue.setStatus("current")


class _L2FLinkStatusState_Type(Integer32):
    """Custom type l2FLinkStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("close1", 4),
          ("close2", 5),
          ("idle", 0),
          ("opened", 3),
          ("pending", 1),
          ("start1", 2))
    )


_L2FLinkStatusState_Type.__name__ = "Integer32"
_L2FLinkStatusState_Object = MibTableColumn
l2FLinkStatusState = _L2FLinkStatusState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1353, 1, 12),
    _L2FLinkStatusState_Type()
)
l2FLinkStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FLinkStatusState.setStatus("current")
_L2FLinkStatusUpTime_Type = Integer32
_L2FLinkStatusUpTime_Object = MibTableColumn
l2FLinkStatusUpTime = _L2FLinkStatusUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1353, 1, 13),
    _L2FLinkStatusUpTime_Type()
)
l2FLinkStatusUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FLinkStatusUpTime.setStatus("current")


class _L2FLinkStatusUserName_Type(DisplayString):
    """Custom type l2FLinkStatusUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_L2FLinkStatusUserName_Type.__name__ = "DisplayString"
_L2FLinkStatusUserName_Object = MibTableColumn
l2FLinkStatusUserName = _L2FLinkStatusUserName_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1353, 1, 14),
    _L2FLinkStatusUserName_Type()
)
l2FLinkStatusUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FLinkStatusUserName.setStatus("current")
_L2FLinkStatusTxPackets_Type = Integer32
_L2FLinkStatusTxPackets_Object = MibTableColumn
l2FLinkStatusTxPackets = _L2FLinkStatusTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1353, 1, 21),
    _L2FLinkStatusTxPackets_Type()
)
l2FLinkStatusTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FLinkStatusTxPackets.setStatus("current")
_L2FLinkStatusTxBytes_Type = Integer32
_L2FLinkStatusTxBytes_Object = MibTableColumn
l2FLinkStatusTxBytes = _L2FLinkStatusTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1353, 1, 22),
    _L2FLinkStatusTxBytes_Type()
)
l2FLinkStatusTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FLinkStatusTxBytes.setStatus("current")
_L2FLinkStatusRxPackets_Type = Integer32
_L2FLinkStatusRxPackets_Object = MibTableColumn
l2FLinkStatusRxPackets = _L2FLinkStatusRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1353, 1, 23),
    _L2FLinkStatusRxPackets_Type()
)
l2FLinkStatusRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FLinkStatusRxPackets.setStatus("current")
_L2FLinkStatusRxBytes_Type = Integer32
_L2FLinkStatusRxBytes_Object = MibTableColumn
l2FLinkStatusRxBytes = _L2FLinkStatusRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1353, 1, 24),
    _L2FLinkStatusRxBytes_Type()
)
l2FLinkStatusRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FLinkStatusRxBytes.setStatus("current")
_L2FLinkStatusL2FTermationCause_Type = Integer32
_L2FLinkStatusL2FTermationCause_Object = MibTableColumn
l2FLinkStatusL2FTermationCause = _L2FLinkStatusL2FTermationCause_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1353, 1, 31),
    _L2FLinkStatusL2FTermationCause_Type()
)
l2FLinkStatusL2FTermationCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FLinkStatusL2FTermationCause.setStatus("current")
_L2FLogEntryTable_Object = MibTable
l2FLogEntryTable = _L2FLogEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1354)
)
if mibBuilder.loadTexts:
    l2FLogEntryTable.setStatus("current")
_L2FLogEntryEntry_Object = MibTableRow
l2FLogEntryEntry = _L2FLogEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1354, 1)
)
l2FLogEntryEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "l2FLogEntryLocalCLID"),
    (0, "APTIS-MONITOR-MIB", "l2FLogEntryIndex"),
)
if mibBuilder.loadTexts:
    l2FLogEntryEntry.setStatus("current")
_L2FLogEntryLocalCLID_Type = Integer32
_L2FLogEntryLocalCLID_Object = MibTableColumn
l2FLogEntryLocalCLID = _L2FLogEntryLocalCLID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1354, 1, 1),
    _L2FLogEntryLocalCLID_Type()
)
l2FLogEntryLocalCLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FLogEntryLocalCLID.setStatus("current")
_L2FLogEntryIndex_Type = Integer32
_L2FLogEntryIndex_Object = MibTableColumn
l2FLogEntryIndex = _L2FLogEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1354, 1, 2),
    _L2FLogEntryIndex_Type()
)
l2FLogEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FLogEntryIndex.setStatus("current")
_L2FLogEntryMinIndex_Type = Integer32
_L2FLogEntryMinIndex_Object = MibTableColumn
l2FLogEntryMinIndex = _L2FLogEntryMinIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1354, 1, 11),
    _L2FLogEntryMinIndex_Type()
)
l2FLogEntryMinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FLogEntryMinIndex.setStatus("current")
_L2FLogEntryMaxIndex_Type = Integer32
_L2FLogEntryMaxIndex_Object = MibTableColumn
l2FLogEntryMaxIndex = _L2FLogEntryMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1354, 1, 12),
    _L2FLogEntryMaxIndex_Type()
)
l2FLogEntryMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FLogEntryMaxIndex.setStatus("current")
_L2FLogEntryUpTime_Type = Integer32
_L2FLogEntryUpTime_Object = MibTableColumn
l2FLogEntryUpTime = _L2FLogEntryUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1354, 1, 13),
    _L2FLogEntryUpTime_Type()
)
l2FLogEntryUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FLogEntryUpTime.setStatus("current")


class _L2FLogEntryEntryText_Type(OctetString):
    """Custom type l2FLogEntryEntryText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_L2FLogEntryEntryText_Type.__name__ = "OctetString"
_L2FLogEntryEntryText_Object = MibTableColumn
l2FLogEntryEntryText = _L2FLogEntryEntryText_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1354, 1, 21),
    _L2FLogEntryEntryText_Type()
)
l2FLogEntryEntryText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2FLogEntryEntryText.setStatus("current")
_MamLogEntryTable_Object = MibTable
mamLogEntryTable = _MamLogEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1402)
)
if mibBuilder.loadTexts:
    mamLogEntryTable.setStatus("current")
_MamLogEntryEntry_Object = MibTableRow
mamLogEntryEntry = _MamLogEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1402, 1)
)
mamLogEntryEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "mamLogEntryIndex"),
)
if mibBuilder.loadTexts:
    mamLogEntryEntry.setStatus("current")
_MamLogEntryIndex_Type = Integer32
_MamLogEntryIndex_Object = MibTableColumn
mamLogEntryIndex = _MamLogEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1402, 1, 1),
    _MamLogEntryIndex_Type()
)
mamLogEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mamLogEntryIndex.setStatus("current")
_MamLogEntryMinIndex_Type = Integer32
_MamLogEntryMinIndex_Object = MibTableColumn
mamLogEntryMinIndex = _MamLogEntryMinIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1402, 1, 2),
    _MamLogEntryMinIndex_Type()
)
mamLogEntryMinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mamLogEntryMinIndex.setStatus("current")
_MamLogEntryMaxIndex_Type = Integer32
_MamLogEntryMaxIndex_Object = MibTableColumn
mamLogEntryMaxIndex = _MamLogEntryMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1402, 1, 3),
    _MamLogEntryMaxIndex_Type()
)
mamLogEntryMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mamLogEntryMaxIndex.setStatus("current")


class _MamLogEntryEntryText_Type(OctetString):
    """Custom type mamLogEntryEntryText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_MamLogEntryEntryText_Type.__name__ = "OctetString"
_MamLogEntryEntryText_Object = MibTableColumn
mamLogEntryEntryText = _MamLogEntryEntryText_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1402, 1, 4),
    _MamLogEntryEntryText_Type()
)
mamLogEntryEntryText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mamLogEntryEntryText.setStatus("current")
_ModemStatsTable_Object = MibTable
modemStatsTable = _ModemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422)
)
if mibBuilder.loadTexts:
    modemStatsTable.setStatus("current")
_ModemStatsEntry_Object = MibTableRow
modemStatsEntry = _ModemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1)
)
modemStatsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "modemStatsSlot"),
    (0, "APTIS-MONITOR-MIB", "modemStatsModemIndex"),
)
if mibBuilder.loadTexts:
    modemStatsEntry.setStatus("current")


class _ModemStatsState_Type(Integer32):
    """Custom type modemStatsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("active", 6),
          ("dead", 3),
          ("disabled", 1),
          ("downloading", 7),
          ("idle", 5),
          ("noDownload", 2),
          ("takenOut", 4))
    )


_ModemStatsState_Type.__name__ = "Integer32"
_ModemStatsState_Object = MibTableColumn
modemStatsState = _ModemStatsState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 1),
    _ModemStatsState_Type()
)
modemStatsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsState.setStatus("current")


class _ModemStatsSlot_Type(Integer32):
    """Custom type modemStatsSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_ModemStatsSlot_Type.__name__ = "Integer32"
_ModemStatsSlot_Object = MibTableColumn
modemStatsSlot = _ModemStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 2),
    _ModemStatsSlot_Type()
)
modemStatsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsSlot.setStatus("current")


class _ModemStatsIOP_Type(Integer32):
    """Custom type modemStatsIOP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ModemStatsIOP_Type.__name__ = "Integer32"
_ModemStatsIOP_Object = MibTableColumn
modemStatsIOP = _ModemStatsIOP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 3),
    _ModemStatsIOP_Type()
)
modemStatsIOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsIOP.setStatus("current")


class _ModemStatsDMM_Type(Integer32):
    """Custom type modemStatsDMM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_ModemStatsDMM_Type.__name__ = "Integer32"
_ModemStatsDMM_Object = MibTableColumn
modemStatsDMM = _ModemStatsDMM_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 4),
    _ModemStatsDMM_Type()
)
modemStatsDMM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsDMM.setStatus("current")


class _ModemStatsPack_Type(Integer32):
    """Custom type modemStatsPack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ModemStatsPack_Type.__name__ = "Integer32"
_ModemStatsPack_Object = MibTableColumn
modemStatsPack = _ModemStatsPack_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 5),
    _ModemStatsPack_Type()
)
modemStatsPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsPack.setStatus("current")


class _ModemStatsModem_Type(Integer32):
    """Custom type modemStatsModem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_ModemStatsModem_Type.__name__ = "Integer32"
_ModemStatsModem_Object = MibTableColumn
modemStatsModem = _ModemStatsModem_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 6),
    _ModemStatsModem_Type()
)
modemStatsModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsModem.setStatus("current")
_ModemStatsCurrentSessionID_Type = Integer32
_ModemStatsCurrentSessionID_Object = MibTableColumn
modemStatsCurrentSessionID = _ModemStatsCurrentSessionID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 7),
    _ModemStatsCurrentSessionID_Type()
)
modemStatsCurrentSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsCurrentSessionID.setStatus("current")
_ModemStatsModemIndex_Type = Integer32
_ModemStatsModemIndex_Object = MibTableColumn
modemStatsModemIndex = _ModemStatsModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 8),
    _ModemStatsModemIndex_Type()
)
modemStatsModemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsModemIndex.setStatus("current")


class _ModemStatsRPI_Type(Integer32):
    """Custom type modemStatsRPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ModemStatsRPI_Type.__name__ = "Integer32"
_ModemStatsRPI_Object = MibTableColumn
modemStatsRPI = _ModemStatsRPI_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 101),
    _ModemStatsRPI_Type()
)
modemStatsRPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsRPI.setStatus("current")
_ModemStatsTotalCalls_Type = Integer32
_ModemStatsTotalCalls_Object = MibTableColumn
modemStatsTotalCalls = _ModemStatsTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 102),
    _ModemStatsTotalCalls_Type()
)
modemStatsTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsTotalCalls.setStatus("current")
_ModemStatsConnectedCalls_Type = Integer32
_ModemStatsConnectedCalls_Object = MibTableColumn
modemStatsConnectedCalls = _ModemStatsConnectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 201),
    _ModemStatsConnectedCalls_Type()
)
modemStatsConnectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsConnectedCalls.setStatus("current")
_ModemStatsLast32Calls_Type = Integer32
_ModemStatsLast32Calls_Object = MibTableColumn
modemStatsLast32Calls = _ModemStatsLast32Calls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 202),
    _ModemStatsLast32Calls_Type()
)
modemStatsLast32Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsLast32Calls.setStatus("current")
_ModemStatsConnectedWin_Type = Integer32
_ModemStatsConnectedWin_Object = MibTableColumn
modemStatsConnectedWin = _ModemStatsConnectedWin_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 203),
    _ModemStatsConnectedWin_Type()
)
modemStatsConnectedWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsConnectedWin.setStatus("current")
_ModemStatsConnectedLose_Type = Integer32
_ModemStatsConnectedLose_Object = MibTableColumn
modemStatsConnectedLose = _ModemStatsConnectedLose_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 204),
    _ModemStatsConnectedLose_Type()
)
modemStatsConnectedLose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsConnectedLose.setStatus("current")
_ModemStatsAuthCalls_Type = Integer32
_ModemStatsAuthCalls_Object = MibTableColumn
modemStatsAuthCalls = _ModemStatsAuthCalls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 301),
    _ModemStatsAuthCalls_Type()
)
modemStatsAuthCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsAuthCalls.setStatus("current")
_ModemStatsLast32Auth_Type = Integer32
_ModemStatsLast32Auth_Object = MibTableColumn
modemStatsLast32Auth = _ModemStatsLast32Auth_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 302),
    _ModemStatsLast32Auth_Type()
)
modemStatsLast32Auth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsLast32Auth.setStatus("current")
_ModemStatsAuthWin_Type = Integer32
_ModemStatsAuthWin_Object = MibTableColumn
modemStatsAuthWin = _ModemStatsAuthWin_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 303),
    _ModemStatsAuthWin_Type()
)
modemStatsAuthWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsAuthWin.setStatus("current")
_ModemStatsAuthLose_Type = Integer32
_ModemStatsAuthLose_Object = MibTableColumn
modemStatsAuthLose = _ModemStatsAuthLose_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 304),
    _ModemStatsAuthLose_Type()
)
modemStatsAuthLose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsAuthLose.setStatus("current")
_ModemStatsECCalls_Type = Integer32
_ModemStatsECCalls_Object = MibTableColumn
modemStatsECCalls = _ModemStatsECCalls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 401),
    _ModemStatsECCalls_Type()
)
modemStatsECCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsECCalls.setStatus("current")
_ModemStatsDCCalls_Type = Integer32
_ModemStatsDCCalls_Object = MibTableColumn
modemStatsDCCalls = _ModemStatsDCCalls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 402),
    _ModemStatsDCCalls_Type()
)
modemStatsDCCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsDCCalls.setStatus("current")
_ModemStatsK56Calls_Type = Integer32
_ModemStatsK56Calls_Object = MibTableColumn
modemStatsK56Calls = _ModemStatsK56Calls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 403),
    _ModemStatsK56Calls_Type()
)
modemStatsK56Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsK56Calls.setStatus("current")
_ModemStatsV90Calls_Type = Integer32
_ModemStatsV90Calls_Object = MibTableColumn
modemStatsV90Calls = _ModemStatsV90Calls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 404),
    _ModemStatsV90Calls_Type()
)
modemStatsV90Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsV90Calls.setStatus("current")
_ModemStatsV34Calls_Type = Integer32
_ModemStatsV34Calls_Object = MibTableColumn
modemStatsV34Calls = _ModemStatsV34Calls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 405),
    _ModemStatsV34Calls_Type()
)
modemStatsV34Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsV34Calls.setStatus("current")
_ModemStatsV32Calls_Type = Integer32
_ModemStatsV32Calls_Object = MibTableColumn
modemStatsV32Calls = _ModemStatsV32Calls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 406),
    _ModemStatsV32Calls_Type()
)
modemStatsV32Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsV32Calls.setStatus("current")
_ModemStatsStatsSamples_Type = Integer32
_ModemStatsStatsSamples_Object = MibTableColumn
modemStatsStatsSamples = _ModemStatsStatsSamples_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 501),
    _ModemStatsStatsSamples_Type()
)
modemStatsStatsSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsStatsSamples.setStatus("current")
_ModemStatsInitialTxSum_Type = Integer32
_ModemStatsInitialTxSum_Object = MibTableColumn
modemStatsInitialTxSum = _ModemStatsInitialTxSum_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 502),
    _ModemStatsInitialTxSum_Type()
)
modemStatsInitialTxSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsInitialTxSum.setStatus("current")
_ModemStatsMinTxSum_Type = Integer32
_ModemStatsMinTxSum_Object = MibTableColumn
modemStatsMinTxSum = _ModemStatsMinTxSum_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 503),
    _ModemStatsMinTxSum_Type()
)
modemStatsMinTxSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsMinTxSum.setStatus("current")
_ModemStatsMaxTxSum_Type = Integer32
_ModemStatsMaxTxSum_Object = MibTableColumn
modemStatsMaxTxSum = _ModemStatsMaxTxSum_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 504),
    _ModemStatsMaxTxSum_Type()
)
modemStatsMaxTxSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsMaxTxSum.setStatus("current")
_ModemStatsFinalTxSum_Type = Integer32
_ModemStatsFinalTxSum_Object = MibTableColumn
modemStatsFinalTxSum = _ModemStatsFinalTxSum_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 505),
    _ModemStatsFinalTxSum_Type()
)
modemStatsFinalTxSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsFinalTxSum.setStatus("current")
_ModemStatsMinTxSpeed_Type = Integer32
_ModemStatsMinTxSpeed_Object = MibTableColumn
modemStatsMinTxSpeed = _ModemStatsMinTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 506),
    _ModemStatsMinTxSpeed_Type()
)
modemStatsMinTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsMinTxSpeed.setStatus("current")
_ModemStatsMaxTxSpeed_Type = Integer32
_ModemStatsMaxTxSpeed_Object = MibTableColumn
modemStatsMaxTxSpeed = _ModemStatsMaxTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 507),
    _ModemStatsMaxTxSpeed_Type()
)
modemStatsMaxTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsMaxTxSpeed.setStatus("current")
_ModemStatsInitialRxSum_Type = Integer32
_ModemStatsInitialRxSum_Object = MibTableColumn
modemStatsInitialRxSum = _ModemStatsInitialRxSum_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 508),
    _ModemStatsInitialRxSum_Type()
)
modemStatsInitialRxSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsInitialRxSum.setStatus("current")
_ModemStatsMinRxSum_Type = Integer32
_ModemStatsMinRxSum_Object = MibTableColumn
modemStatsMinRxSum = _ModemStatsMinRxSum_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 509),
    _ModemStatsMinRxSum_Type()
)
modemStatsMinRxSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsMinRxSum.setStatus("current")
_ModemStatsMaxRxSum_Type = Integer32
_ModemStatsMaxRxSum_Object = MibTableColumn
modemStatsMaxRxSum = _ModemStatsMaxRxSum_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 510),
    _ModemStatsMaxRxSum_Type()
)
modemStatsMaxRxSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsMaxRxSum.setStatus("current")
_ModemStatsFinalRxSum_Type = Integer32
_ModemStatsFinalRxSum_Object = MibTableColumn
modemStatsFinalRxSum = _ModemStatsFinalRxSum_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 511),
    _ModemStatsFinalRxSum_Type()
)
modemStatsFinalRxSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsFinalRxSum.setStatus("current")
_ModemStatsMinRxSpeed_Type = Integer32
_ModemStatsMinRxSpeed_Object = MibTableColumn
modemStatsMinRxSpeed = _ModemStatsMinRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 512),
    _ModemStatsMinRxSpeed_Type()
)
modemStatsMinRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsMinRxSpeed.setStatus("current")
_ModemStatsMaxRxSpeed_Type = Integer32
_ModemStatsMaxRxSpeed_Object = MibTableColumn
modemStatsMaxRxSpeed = _ModemStatsMaxRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 513),
    _ModemStatsMaxRxSpeed_Type()
)
modemStatsMaxRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsMaxRxSpeed.setStatus("current")
_ModemStatsDownloadAttempts_Type = Integer32
_ModemStatsDownloadAttempts_Object = MibTableColumn
modemStatsDownloadAttempts = _ModemStatsDownloadAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 1001),
    _ModemStatsDownloadAttempts_Type()
)
modemStatsDownloadAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsDownloadAttempts.setStatus("current")
_ModemStatsDownloadSuccesses_Type = Integer32
_ModemStatsDownloadSuccesses_Object = MibTableColumn
modemStatsDownloadSuccesses = _ModemStatsDownloadSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 1002),
    _ModemStatsDownloadSuccesses_Type()
)
modemStatsDownloadSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsDownloadSuccesses.setStatus("current")
_ModemStatsResetFailures_Type = Integer32
_ModemStatsResetFailures_Object = MibTableColumn
modemStatsResetFailures = _ModemStatsResetFailures_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 1003),
    _ModemStatsResetFailures_Type()
)
modemStatsResetFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsResetFailures.setStatus("current")
_ModemStatsResetRevivals_Type = Integer32
_ModemStatsResetRevivals_Object = MibTableColumn
modemStatsResetRevivals = _ModemStatsResetRevivals_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 1004),
    _ModemStatsResetRevivals_Type()
)
modemStatsResetRevivals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsResetRevivals.setStatus("current")
_ModemStatsPackCrashes_Type = Integer32
_ModemStatsPackCrashes_Object = MibTableColumn
modemStatsPackCrashes = _ModemStatsPackCrashes_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 1005),
    _ModemStatsPackCrashes_Type()
)
modemStatsPackCrashes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsPackCrashes.setStatus("current")
_ModemStatsPackRevivals_Type = Integer32
_ModemStatsPackRevivals_Object = MibTableColumn
modemStatsPackRevivals = _ModemStatsPackRevivals_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1422, 1, 1006),
    _ModemStatsPackRevivals_Type()
)
modemStatsPackRevivals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatsPackRevivals.setStatus("current")
_ModemCallStatsTable_Object = MibTable
modemCallStatsTable = _ModemCallStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423)
)
if mibBuilder.loadTexts:
    modemCallStatsTable.setStatus("current")
_ModemCallStatsEntry_Object = MibTableRow
modemCallStatsEntry = _ModemCallStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1)
)
modemCallStatsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "modemCallStatsSlotIndex"),
    (0, "APTIS-MONITOR-MIB", "modemCallStatsModemIndex"),
)
if mibBuilder.loadTexts:
    modemCallStatsEntry.setStatus("current")
_ModemCallStatsTxInitialSpeed_Type = Integer32
_ModemCallStatsTxInitialSpeed_Object = MibTableColumn
modemCallStatsTxInitialSpeed = _ModemCallStatsTxInitialSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 1),
    _ModemCallStatsTxInitialSpeed_Type()
)
modemCallStatsTxInitialSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsTxInitialSpeed.setStatus("current")
_ModemCallStatsTxFinalSpeed_Type = Integer32
_ModemCallStatsTxFinalSpeed_Object = MibTableColumn
modemCallStatsTxFinalSpeed = _ModemCallStatsTxFinalSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 2),
    _ModemCallStatsTxFinalSpeed_Type()
)
modemCallStatsTxFinalSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsTxFinalSpeed.setStatus("current")
_ModemCallStatsTxMinSpeed_Type = Integer32
_ModemCallStatsTxMinSpeed_Object = MibTableColumn
modemCallStatsTxMinSpeed = _ModemCallStatsTxMinSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 3),
    _ModemCallStatsTxMinSpeed_Type()
)
modemCallStatsTxMinSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsTxMinSpeed.setStatus("current")
_ModemCallStatsTxMaxSpeed_Type = Integer32
_ModemCallStatsTxMaxSpeed_Object = MibTableColumn
modemCallStatsTxMaxSpeed = _ModemCallStatsTxMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 4),
    _ModemCallStatsTxMaxSpeed_Type()
)
modemCallStatsTxMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsTxMaxSpeed.setStatus("current")
_ModemCallStatsRxInitialSpeed_Type = Integer32
_ModemCallStatsRxInitialSpeed_Object = MibTableColumn
modemCallStatsRxInitialSpeed = _ModemCallStatsRxInitialSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 5),
    _ModemCallStatsRxInitialSpeed_Type()
)
modemCallStatsRxInitialSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsRxInitialSpeed.setStatus("current")
_ModemCallStatsRxFinalSpeed_Type = Integer32
_ModemCallStatsRxFinalSpeed_Object = MibTableColumn
modemCallStatsRxFinalSpeed = _ModemCallStatsRxFinalSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 6),
    _ModemCallStatsRxFinalSpeed_Type()
)
modemCallStatsRxFinalSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsRxFinalSpeed.setStatus("current")
_ModemCallStatsRxMinSpeed_Type = Integer32
_ModemCallStatsRxMinSpeed_Object = MibTableColumn
modemCallStatsRxMinSpeed = _ModemCallStatsRxMinSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 7),
    _ModemCallStatsRxMinSpeed_Type()
)
modemCallStatsRxMinSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsRxMinSpeed.setStatus("current")
_ModemCallStatsRxMaxSpeed_Type = Integer32
_ModemCallStatsRxMaxSpeed_Object = MibTableColumn
modemCallStatsRxMaxSpeed = _ModemCallStatsRxMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 8),
    _ModemCallStatsRxMaxSpeed_Type()
)
modemCallStatsRxMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsRxMaxSpeed.setStatus("current")


class _ModemCallStatsECProtocol_Type(DisplayString):
    """Custom type modemCallStatsECProtocol based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModemCallStatsECProtocol_Type.__name__ = "DisplayString"
_ModemCallStatsECProtocol_Object = MibTableColumn
modemCallStatsECProtocol = _ModemCallStatsECProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 9),
    _ModemCallStatsECProtocol_Type()
)
modemCallStatsECProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsECProtocol.setStatus("current")


class _ModemCallStatsDCProtocol_Type(DisplayString):
    """Custom type modemCallStatsDCProtocol based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModemCallStatsDCProtocol_Type.__name__ = "DisplayString"
_ModemCallStatsDCProtocol_Object = MibTableColumn
modemCallStatsDCProtocol = _ModemCallStatsDCProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 10),
    _ModemCallStatsDCProtocol_Type()
)
modemCallStatsDCProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsDCProtocol.setStatus("current")


class _ModemCallStatsModulationType_Type(DisplayString):
    """Custom type modemCallStatsModulationType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModemCallStatsModulationType_Type.__name__ = "DisplayString"
_ModemCallStatsModulationType_Object = MibTableColumn
modemCallStatsModulationType = _ModemCallStatsModulationType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 11),
    _ModemCallStatsModulationType_Type()
)
modemCallStatsModulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsModulationType.setStatus("current")


class _ModemCallStatsInitialModulationType_Type(DisplayString):
    """Custom type modemCallStatsInitialModulationType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModemCallStatsInitialModulationType_Type.__name__ = "DisplayString"
_ModemCallStatsInitialModulationType_Object = MibTableColumn
modemCallStatsInitialModulationType = _ModemCallStatsInitialModulationType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 12),
    _ModemCallStatsInitialModulationType_Type()
)
modemCallStatsInitialModulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsInitialModulationType.setStatus("current")
_ModemCallStatsSymbolRate_Type = Integer32
_ModemCallStatsSymbolRate_Object = MibTableColumn
modemCallStatsSymbolRate = _ModemCallStatsSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 13),
    _ModemCallStatsSymbolRate_Type()
)
modemCallStatsSymbolRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsSymbolRate.setStatus("current")
_ModemCallStatsTxCarrierFrequency_Type = Integer32
_ModemCallStatsTxCarrierFrequency_Object = MibTableColumn
modemCallStatsTxCarrierFrequency = _ModemCallStatsTxCarrierFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 14),
    _ModemCallStatsTxCarrierFrequency_Type()
)
modemCallStatsTxCarrierFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsTxCarrierFrequency.setStatus("current")
_ModemCallStatsRxCarrierFrequency_Type = Integer32
_ModemCallStatsRxCarrierFrequency_Object = MibTableColumn
modemCallStatsRxCarrierFrequency = _ModemCallStatsRxCarrierFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 15),
    _ModemCallStatsRxCarrierFrequency_Type()
)
modemCallStatsRxCarrierFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsRxCarrierFrequency.setStatus("current")


class _ModemCallStatsLastAGCGainValue_Type(DisplayString):
    """Custom type modemCallStatsLastAGCGainValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModemCallStatsLastAGCGainValue_Type.__name__ = "DisplayString"
_ModemCallStatsLastAGCGainValue_Object = MibTableColumn
modemCallStatsLastAGCGainValue = _ModemCallStatsLastAGCGainValue_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 16),
    _ModemCallStatsLastAGCGainValue_Type()
)
modemCallStatsLastAGCGainValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsLastAGCGainValue.setStatus("current")


class _ModemCallStatsMinAGCGainValue_Type(DisplayString):
    """Custom type modemCallStatsMinAGCGainValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModemCallStatsMinAGCGainValue_Type.__name__ = "DisplayString"
_ModemCallStatsMinAGCGainValue_Object = MibTableColumn
modemCallStatsMinAGCGainValue = _ModemCallStatsMinAGCGainValue_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 17),
    _ModemCallStatsMinAGCGainValue_Type()
)
modemCallStatsMinAGCGainValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsMinAGCGainValue.setStatus("current")


class _ModemCallStatsMaxAGCGainValue_Type(DisplayString):
    """Custom type modemCallStatsMaxAGCGainValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModemCallStatsMaxAGCGainValue_Type.__name__ = "DisplayString"
_ModemCallStatsMaxAGCGainValue_Object = MibTableColumn
modemCallStatsMaxAGCGainValue = _ModemCallStatsMaxAGCGainValue_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 18),
    _ModemCallStatsMaxAGCGainValue_Type()
)
modemCallStatsMaxAGCGainValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsMaxAGCGainValue.setStatus("current")
_ModemCallStatsTxLevel_Type = Integer32
_ModemCallStatsTxLevel_Object = MibTableColumn
modemCallStatsTxLevel = _ModemCallStatsTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 19),
    _ModemCallStatsTxLevel_Type()
)
modemCallStatsTxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsTxLevel.setStatus("current")
_ModemCallStatsTxLevelReduction_Type = Integer32
_ModemCallStatsTxLevelReduction_Object = MibTableColumn
modemCallStatsTxLevelReduction = _ModemCallStatsTxLevelReduction_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 20),
    _ModemCallStatsTxLevelReduction_Type()
)
modemCallStatsTxLevelReduction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsTxLevelReduction.setStatus("current")
_ModemCallStatsLastEQMValue_Type = Integer32
_ModemCallStatsLastEQMValue_Object = MibTableColumn
modemCallStatsLastEQMValue = _ModemCallStatsLastEQMValue_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 21),
    _ModemCallStatsLastEQMValue_Type()
)
modemCallStatsLastEQMValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsLastEQMValue.setStatus("current")
_ModemCallStatsMinEQMValue_Type = Integer32
_ModemCallStatsMinEQMValue_Object = MibTableColumn
modemCallStatsMinEQMValue = _ModemCallStatsMinEQMValue_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 22),
    _ModemCallStatsMinEQMValue_Type()
)
modemCallStatsMinEQMValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsMinEQMValue.setStatus("current")
_ModemCallStatsMaxEQMValue_Type = Integer32
_ModemCallStatsMaxEQMValue_Object = MibTableColumn
modemCallStatsMaxEQMValue = _ModemCallStatsMaxEQMValue_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 23),
    _ModemCallStatsMaxEQMValue_Type()
)
modemCallStatsMaxEQMValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsMaxEQMValue.setStatus("current")
_ModemCallStatsEQMHits_Type = Integer32
_ModemCallStatsEQMHits_Object = MibTableColumn
modemCallStatsEQMHits = _ModemCallStatsEQMHits_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 24),
    _ModemCallStatsEQMHits_Type()
)
modemCallStatsEQMHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsEQMHits.setStatus("current")
_ModemCallStatsEQMSumLow_Type = Integer32
_ModemCallStatsEQMSumLow_Object = MibTableColumn
modemCallStatsEQMSumLow = _ModemCallStatsEQMSumLow_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 25),
    _ModemCallStatsEQMSumLow_Type()
)
modemCallStatsEQMSumLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsEQMSumLow.setStatus("current")
_ModemCallStatsEQMSumMiddle_Type = Integer32
_ModemCallStatsEQMSumMiddle_Object = MibTableColumn
modemCallStatsEQMSumMiddle = _ModemCallStatsEQMSumMiddle_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 26),
    _ModemCallStatsEQMSumMiddle_Type()
)
modemCallStatsEQMSumMiddle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsEQMSumMiddle.setStatus("current")
_ModemCallStatsEQMSumHigh_Type = Integer32
_ModemCallStatsEQMSumHigh_Object = MibTableColumn
modemCallStatsEQMSumHigh = _ModemCallStatsEQMSumHigh_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 27),
    _ModemCallStatsEQMSumHigh_Type()
)
modemCallStatsEQMSumHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsEQMSumHigh.setStatus("current")
_ModemCallStatsEQM1Second_Type = Integer32
_ModemCallStatsEQM1Second_Object = MibTableColumn
modemCallStatsEQM1Second = _ModemCallStatsEQM1Second_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 28),
    _ModemCallStatsEQM1Second_Type()
)
modemCallStatsEQM1Second.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsEQM1Second.setStatus("current")
_ModemCallStatsEQM2Seconds_Type = Integer32
_ModemCallStatsEQM2Seconds_Object = MibTableColumn
modemCallStatsEQM2Seconds = _ModemCallStatsEQM2Seconds_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 29),
    _ModemCallStatsEQM2Seconds_Type()
)
modemCallStatsEQM2Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsEQM2Seconds.setStatus("current")
_ModemCallStatsEQM3Seconds_Type = Integer32
_ModemCallStatsEQM3Seconds_Object = MibTableColumn
modemCallStatsEQM3Seconds = _ModemCallStatsEQM3Seconds_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 30),
    _ModemCallStatsEQM3Seconds_Type()
)
modemCallStatsEQM3Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsEQM3Seconds.setStatus("current")
_ModemCallStatsEQM4Seconds_Type = Integer32
_ModemCallStatsEQM4Seconds_Object = MibTableColumn
modemCallStatsEQM4Seconds = _ModemCallStatsEQM4Seconds_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 31),
    _ModemCallStatsEQM4Seconds_Type()
)
modemCallStatsEQM4Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsEQM4Seconds.setStatus("current")
_ModemCallStatsEQM5Seconds_Type = Integer32
_ModemCallStatsEQM5Seconds_Object = MibTableColumn
modemCallStatsEQM5Seconds = _ModemCallStatsEQM5Seconds_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 32),
    _ModemCallStatsEQM5Seconds_Type()
)
modemCallStatsEQM5Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsEQM5Seconds.setStatus("current")
_ModemCallStatsEQM6Seconds_Type = Integer32
_ModemCallStatsEQM6Seconds_Object = MibTableColumn
modemCallStatsEQM6Seconds = _ModemCallStatsEQM6Seconds_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 33),
    _ModemCallStatsEQM6Seconds_Type()
)
modemCallStatsEQM6Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsEQM6Seconds.setStatus("current")
_ModemCallStatsEQM7Seconds_Type = Integer32
_ModemCallStatsEQM7Seconds_Object = MibTableColumn
modemCallStatsEQM7Seconds = _ModemCallStatsEQM7Seconds_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 34),
    _ModemCallStatsEQM7Seconds_Type()
)
modemCallStatsEQM7Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsEQM7Seconds.setStatus("current")
_ModemCallStatsEQM8Seconds_Type = Integer32
_ModemCallStatsEQM8Seconds_Object = MibTableColumn
modemCallStatsEQM8Seconds = _ModemCallStatsEQM8Seconds_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 35),
    _ModemCallStatsEQM8Seconds_Type()
)
modemCallStatsEQM8Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsEQM8Seconds.setStatus("current")
_ModemCallStatsEQM9Seconds_Type = Integer32
_ModemCallStatsEQM9Seconds_Object = MibTableColumn
modemCallStatsEQM9Seconds = _ModemCallStatsEQM9Seconds_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 36),
    _ModemCallStatsEQM9Seconds_Type()
)
modemCallStatsEQM9Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsEQM9Seconds.setStatus("current")
_ModemCallStatsEQM10Seconds_Type = Integer32
_ModemCallStatsEQM10Seconds_Object = MibTableColumn
modemCallStatsEQM10Seconds = _ModemCallStatsEQM10Seconds_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 37),
    _ModemCallStatsEQM10Seconds_Type()
)
modemCallStatsEQM10Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsEQM10Seconds.setStatus("current")


class _ModemCallStatsSNRRatio_Type(DisplayString):
    """Custom type modemCallStatsSNRRatio based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModemCallStatsSNRRatio_Type.__name__ = "DisplayString"
_ModemCallStatsSNRRatio_Object = MibTableColumn
modemCallStatsSNRRatio = _ModemCallStatsSNRRatio_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 38),
    _ModemCallStatsSNRRatio_Type()
)
modemCallStatsSNRRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsSNRRatio.setStatus("current")
_ModemCallStatsMinSNRValue_Type = Integer32
_ModemCallStatsMinSNRValue_Object = MibTableColumn
modemCallStatsMinSNRValue = _ModemCallStatsMinSNRValue_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 39),
    _ModemCallStatsMinSNRValue_Type()
)
modemCallStatsMinSNRValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsMinSNRValue.setStatus("current")
_ModemCallStatsMaxSNRValue_Type = Integer32
_ModemCallStatsMaxSNRValue_Object = MibTableColumn
modemCallStatsMaxSNRValue = _ModemCallStatsMaxSNRValue_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 40),
    _ModemCallStatsMaxSNRValue_Type()
)
modemCallStatsMaxSNRValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsMaxSNRValue.setStatus("current")
_ModemCallStatsLocalRetrains_Type = Integer32
_ModemCallStatsLocalRetrains_Object = MibTableColumn
modemCallStatsLocalRetrains = _ModemCallStatsLocalRetrains_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 41),
    _ModemCallStatsLocalRetrains_Type()
)
modemCallStatsLocalRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsLocalRetrains.setStatus("current")
_ModemCallStatsRemoteRetrains_Type = Integer32
_ModemCallStatsRemoteRetrains_Object = MibTableColumn
modemCallStatsRemoteRetrains = _ModemCallStatsRemoteRetrains_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 42),
    _ModemCallStatsRemoteRetrains_Type()
)
modemCallStatsRemoteRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsRemoteRetrains.setStatus("current")
_ModemCallStatsLocalRateRenegs_Type = Integer32
_ModemCallStatsLocalRateRenegs_Object = MibTableColumn
modemCallStatsLocalRateRenegs = _ModemCallStatsLocalRateRenegs_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 43),
    _ModemCallStatsLocalRateRenegs_Type()
)
modemCallStatsLocalRateRenegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsLocalRateRenegs.setStatus("current")
_ModemCallStatsRemoteRateRenegs_Type = Integer32
_ModemCallStatsRemoteRateRenegs_Object = MibTableColumn
modemCallStatsRemoteRateRenegs = _ModemCallStatsRemoteRateRenegs_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 44),
    _ModemCallStatsRemoteRateRenegs_Type()
)
modemCallStatsRemoteRateRenegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsRemoteRateRenegs.setStatus("current")
_ModemCallStatsTxNonlinearEncoding_Type = Integer32
_ModemCallStatsTxNonlinearEncoding_Object = MibTableColumn
modemCallStatsTxNonlinearEncoding = _ModemCallStatsTxNonlinearEncoding_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 45),
    _ModemCallStatsTxNonlinearEncoding_Type()
)
modemCallStatsTxNonlinearEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsTxNonlinearEncoding.setStatus("current")
_ModemCallStatsRxNonlinearEncoding_Type = Integer32
_ModemCallStatsRxNonlinearEncoding_Object = MibTableColumn
modemCallStatsRxNonlinearEncoding = _ModemCallStatsRxNonlinearEncoding_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 46),
    _ModemCallStatsRxNonlinearEncoding_Type()
)
modemCallStatsRxNonlinearEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsRxNonlinearEncoding.setStatus("current")
_ModemCallStatsTxPrecoding_Type = Integer32
_ModemCallStatsTxPrecoding_Object = MibTableColumn
modemCallStatsTxPrecoding = _ModemCallStatsTxPrecoding_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 47),
    _ModemCallStatsTxPrecoding_Type()
)
modemCallStatsTxPrecoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsTxPrecoding.setStatus("current")
_ModemCallStatsRxPrecoding_Type = Integer32
_ModemCallStatsRxPrecoding_Object = MibTableColumn
modemCallStatsRxPrecoding = _ModemCallStatsRxPrecoding_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 48),
    _ModemCallStatsRxPrecoding_Type()
)
modemCallStatsRxPrecoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsRxPrecoding.setStatus("current")
_ModemCallStatsTxShaping_Type = Integer32
_ModemCallStatsTxShaping_Object = MibTableColumn
modemCallStatsTxShaping = _ModemCallStatsTxShaping_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 49),
    _ModemCallStatsTxShaping_Type()
)
modemCallStatsTxShaping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsTxShaping.setStatus("current")
_ModemCallStatsRxShaping_Type = Integer32
_ModemCallStatsRxShaping_Object = MibTableColumn
modemCallStatsRxShaping = _ModemCallStatsRxShaping_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 50),
    _ModemCallStatsRxShaping_Type()
)
modemCallStatsRxShaping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsRxShaping.setStatus("current")


class _ModemCallStatsTrellisMapping_Type(DisplayString):
    """Custom type modemCallStatsTrellisMapping based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModemCallStatsTrellisMapping_Type.__name__ = "DisplayString"
_ModemCallStatsTrellisMapping_Object = MibTableColumn
modemCallStatsTrellisMapping = _ModemCallStatsTrellisMapping_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 51),
    _ModemCallStatsTrellisMapping_Type()
)
modemCallStatsTrellisMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsTrellisMapping.setStatus("current")
_ModemCallStatsPreEmphasis_Type = Integer32
_ModemCallStatsPreEmphasis_Object = MibTableColumn
modemCallStatsPreEmphasis = _ModemCallStatsPreEmphasis_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 52),
    _ModemCallStatsPreEmphasis_Type()
)
modemCallStatsPreEmphasis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsPreEmphasis.setStatus("current")


class _ModemCallStatsUpperBandEdge_Type(DisplayString):
    """Custom type modemCallStatsUpperBandEdge based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModemCallStatsUpperBandEdge_Type.__name__ = "DisplayString"
_ModemCallStatsUpperBandEdge_Object = MibTableColumn
modemCallStatsUpperBandEdge = _ModemCallStatsUpperBandEdge_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 53),
    _ModemCallStatsUpperBandEdge_Type()
)
modemCallStatsUpperBandEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsUpperBandEdge.setStatus("current")


class _ModemCallStatsLowerBandEdge_Type(DisplayString):
    """Custom type modemCallStatsLowerBandEdge based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModemCallStatsLowerBandEdge_Type.__name__ = "DisplayString"
_ModemCallStatsLowerBandEdge_Object = MibTableColumn
modemCallStatsLowerBandEdge = _ModemCallStatsLowerBandEdge_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 54),
    _ModemCallStatsLowerBandEdge_Type()
)
modemCallStatsLowerBandEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsLowerBandEdge.setStatus("current")
_ModemCallStatsRTTHigh_Type = Integer32
_ModemCallStatsRTTHigh_Object = MibTableColumn
modemCallStatsRTTHigh = _ModemCallStatsRTTHigh_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 55),
    _ModemCallStatsRTTHigh_Type()
)
modemCallStatsRTTHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsRTTHigh.setStatus("current")
_ModemCallStatsRTTLow_Type = Integer32
_ModemCallStatsRTTLow_Object = MibTableColumn
modemCallStatsRTTLow = _ModemCallStatsRTTLow_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 56),
    _ModemCallStatsRTTLow_Type()
)
modemCallStatsRTTLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsRTTLow.setStatus("current")
_ModemCallStatsInfo0SequenceHigh_Type = Integer32
_ModemCallStatsInfo0SequenceHigh_Object = MibTableColumn
modemCallStatsInfo0SequenceHigh = _ModemCallStatsInfo0SequenceHigh_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 57),
    _ModemCallStatsInfo0SequenceHigh_Type()
)
modemCallStatsInfo0SequenceHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsInfo0SequenceHigh.setStatus("current")
_ModemCallStatsInfo0SequenceLow_Type = Integer32
_ModemCallStatsInfo0SequenceLow_Object = MibTableColumn
modemCallStatsInfo0SequenceLow = _ModemCallStatsInfo0SequenceLow_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 58),
    _ModemCallStatsInfo0SequenceLow_Type()
)
modemCallStatsInfo0SequenceLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsInfo0SequenceLow.setStatus("current")
_ModemCallStatsRxMPSequenceByte1Low_Type = Integer32
_ModemCallStatsRxMPSequenceByte1Low_Object = MibTableColumn
modemCallStatsRxMPSequenceByte1Low = _ModemCallStatsRxMPSequenceByte1Low_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 59),
    _ModemCallStatsRxMPSequenceByte1Low_Type()
)
modemCallStatsRxMPSequenceByte1Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsRxMPSequenceByte1Low.setStatus("current")
_ModemCallStatsRxMPSequenceByte1High_Type = Integer32
_ModemCallStatsRxMPSequenceByte1High_Object = MibTableColumn
modemCallStatsRxMPSequenceByte1High = _ModemCallStatsRxMPSequenceByte1High_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 60),
    _ModemCallStatsRxMPSequenceByte1High_Type()
)
modemCallStatsRxMPSequenceByte1High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsRxMPSequenceByte1High.setStatus("current")
_ModemCallStatsRxMPSequenceByte2Low_Type = Integer32
_ModemCallStatsRxMPSequenceByte2Low_Object = MibTableColumn
modemCallStatsRxMPSequenceByte2Low = _ModemCallStatsRxMPSequenceByte2Low_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 61),
    _ModemCallStatsRxMPSequenceByte2Low_Type()
)
modemCallStatsRxMPSequenceByte2Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsRxMPSequenceByte2Low.setStatus("current")
_ModemCallStatsRxMPSequenceByte2High_Type = Integer32
_ModemCallStatsRxMPSequenceByte2High_Object = MibTableColumn
modemCallStatsRxMPSequenceByte2High = _ModemCallStatsRxMPSequenceByte2High_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 62),
    _ModemCallStatsRxMPSequenceByte2High_Type()
)
modemCallStatsRxMPSequenceByte2High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsRxMPSequenceByte2High.setStatus("current")
_ModemCallStatsHighestTxState_Type = Integer32
_ModemCallStatsHighestTxState_Object = MibTableColumn
modemCallStatsHighestTxState = _ModemCallStatsHighestTxState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 63),
    _ModemCallStatsHighestTxState_Type()
)
modemCallStatsHighestTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsHighestTxState.setStatus("current")
_ModemCallStatsHighestRxState_Type = Integer32
_ModemCallStatsHighestRxState_Object = MibTableColumn
modemCallStatsHighestRxState = _ModemCallStatsHighestRxState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 64),
    _ModemCallStatsHighestRxState_Type()
)
modemCallStatsHighestRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsHighestRxState.setStatus("current")
_ModemCallStatsLastTransmitState_Type = Integer32
_ModemCallStatsLastTransmitState_Object = MibTableColumn
modemCallStatsLastTransmitState = _ModemCallStatsLastTransmitState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 65),
    _ModemCallStatsLastTransmitState_Type()
)
modemCallStatsLastTransmitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsLastTransmitState.setStatus("current")
_ModemCallStatsLastReceiveState_Type = Integer32
_ModemCallStatsLastReceiveState_Object = MibTableColumn
modemCallStatsLastReceiveState = _ModemCallStatsLastReceiveState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 66),
    _ModemCallStatsLastReceiveState_Type()
)
modemCallStatsLastReceiveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsLastReceiveState.setStatus("current")
_ModemCallStatsConnectTimeHours_Type = Integer32
_ModemCallStatsConnectTimeHours_Object = MibTableColumn
modemCallStatsConnectTimeHours = _ModemCallStatsConnectTimeHours_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 67),
    _ModemCallStatsConnectTimeHours_Type()
)
modemCallStatsConnectTimeHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsConnectTimeHours.setStatus("current")
_ModemCallStatsConnectTimeMinutes_Type = Integer32
_ModemCallStatsConnectTimeMinutes_Object = MibTableColumn
modemCallStatsConnectTimeMinutes = _ModemCallStatsConnectTimeMinutes_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 68),
    _ModemCallStatsConnectTimeMinutes_Type()
)
modemCallStatsConnectTimeMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsConnectTimeMinutes.setStatus("current")
_ModemCallStatsConnectTimeSeconds_Type = Integer32
_ModemCallStatsConnectTimeSeconds_Object = MibTableColumn
modemCallStatsConnectTimeSeconds = _ModemCallStatsConnectTimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 69),
    _ModemCallStatsConnectTimeSeconds_Type()
)
modemCallStatsConnectTimeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsConnectTimeSeconds.setStatus("current")


class _ModemCallStatsAutoGainAmplitude_Type(DisplayString):
    """Custom type modemCallStatsAutoGainAmplitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModemCallStatsAutoGainAmplitude_Type.__name__ = "DisplayString"
_ModemCallStatsAutoGainAmplitude_Object = MibTableColumn
modemCallStatsAutoGainAmplitude = _ModemCallStatsAutoGainAmplitude_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 70),
    _ModemCallStatsAutoGainAmplitude_Type()
)
modemCallStatsAutoGainAmplitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsAutoGainAmplitude.setStatus("current")


class _ModemCallStatsAutoGainAttenuation_Type(DisplayString):
    """Custom type modemCallStatsAutoGainAttenuation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModemCallStatsAutoGainAttenuation_Type.__name__ = "DisplayString"
_ModemCallStatsAutoGainAttenuation_Object = MibTableColumn
modemCallStatsAutoGainAttenuation = _ModemCallStatsAutoGainAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 71),
    _ModemCallStatsAutoGainAttenuation_Type()
)
modemCallStatsAutoGainAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsAutoGainAttenuation.setStatus("current")


class _ModemCallStatsDigitalPadDetected_Type(DisplayString):
    """Custom type modemCallStatsDigitalPadDetected based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModemCallStatsDigitalPadDetected_Type.__name__ = "DisplayString"
_ModemCallStatsDigitalPadDetected_Object = MibTableColumn
modemCallStatsDigitalPadDetected = _ModemCallStatsDigitalPadDetected_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 72),
    _ModemCallStatsDigitalPadDetected_Type()
)
modemCallStatsDigitalPadDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsDigitalPadDetected.setStatus("current")
_ModemCallStatsRBSPattern_Type = Integer32
_ModemCallStatsRBSPattern_Object = MibTableColumn
modemCallStatsRBSPattern = _ModemCallStatsRBSPattern_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 73),
    _ModemCallStatsRBSPattern_Type()
)
modemCallStatsRBSPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsRBSPattern.setStatus("current")
_ModemCallStatsRBSRateDrop_Type = Integer32
_ModemCallStatsRBSRateDrop_Object = MibTableColumn
modemCallStatsRBSRateDrop = _ModemCallStatsRBSRateDrop_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 74),
    _ModemCallStatsRBSRateDrop_Type()
)
modemCallStatsRBSRateDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsRBSRateDrop.setStatus("current")
_ModemCallStatsMaxTxRetransmissions_Type = Integer32
_ModemCallStatsMaxTxRetransmissions_Object = MibTableColumn
modemCallStatsMaxTxRetransmissions = _ModemCallStatsMaxTxRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 75),
    _ModemCallStatsMaxTxRetransmissions_Type()
)
modemCallStatsMaxTxRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsMaxTxRetransmissions.setStatus("current")
_ModemCallStatsTotalTxRetransmissions_Type = Integer32
_ModemCallStatsTotalTxRetransmissions_Object = MibTableColumn
modemCallStatsTotalTxRetransmissions = _ModemCallStatsTotalTxRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 76),
    _ModemCallStatsTotalTxRetransmissions_Type()
)
modemCallStatsTotalTxRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsTotalTxRetransmissions.setStatus("current")
_ModemCallStatsNumberOfLAPMREJSReceived_Type = Integer32
_ModemCallStatsNumberOfLAPMREJSReceived_Object = MibTableColumn
modemCallStatsNumberOfLAPMREJSReceived = _ModemCallStatsNumberOfLAPMREJSReceived_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 77),
    _ModemCallStatsNumberOfLAPMREJSReceived_Type()
)
modemCallStatsNumberOfLAPMREJSReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsNumberOfLAPMREJSReceived.setStatus("current")
_ModemCallStatsNumberOfLAPMREJSTransmitted_Type = Integer32
_ModemCallStatsNumberOfLAPMREJSTransmitted_Object = MibTableColumn
modemCallStatsNumberOfLAPMREJSTransmitted = _ModemCallStatsNumberOfLAPMREJSTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 78),
    _ModemCallStatsNumberOfLAPMREJSTransmitted_Type()
)
modemCallStatsNumberOfLAPMREJSTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsNumberOfLAPMREJSTransmitted.setStatus("current")
_ModemCallStatsNumberOfTXBlocksHigh_Type = Integer32
_ModemCallStatsNumberOfTXBlocksHigh_Object = MibTableColumn
modemCallStatsNumberOfTXBlocksHigh = _ModemCallStatsNumberOfTXBlocksHigh_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 79),
    _ModemCallStatsNumberOfTXBlocksHigh_Type()
)
modemCallStatsNumberOfTXBlocksHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsNumberOfTXBlocksHigh.setStatus("current")
_ModemCallStatsNumberOfTXBlocksLow_Type = Integer32
_ModemCallStatsNumberOfTXBlocksLow_Object = MibTableColumn
modemCallStatsNumberOfTXBlocksLow = _ModemCallStatsNumberOfTXBlocksLow_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 80),
    _ModemCallStatsNumberOfTXBlocksLow_Type()
)
modemCallStatsNumberOfTXBlocksLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsNumberOfTXBlocksLow.setStatus("current")
_ModemCallStatsNumberOfRXBlocksHigh_Type = Integer32
_ModemCallStatsNumberOfRXBlocksHigh_Object = MibTableColumn
modemCallStatsNumberOfRXBlocksHigh = _ModemCallStatsNumberOfRXBlocksHigh_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 81),
    _ModemCallStatsNumberOfRXBlocksHigh_Type()
)
modemCallStatsNumberOfRXBlocksHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsNumberOfRXBlocksHigh.setStatus("current")
_ModemCallStatsNumberOfRXBlocksLow_Type = Integer32
_ModemCallStatsNumberOfRXBlocksLow_Object = MibTableColumn
modemCallStatsNumberOfRXBlocksLow = _ModemCallStatsNumberOfRXBlocksLow_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 82),
    _ModemCallStatsNumberOfRXBlocksLow_Type()
)
modemCallStatsNumberOfRXBlocksLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsNumberOfRXBlocksLow.setStatus("current")
_ModemCallStatsNumberOfTXCharsMSB_Type = Integer32
_ModemCallStatsNumberOfTXCharsMSB_Object = MibTableColumn
modemCallStatsNumberOfTXCharsMSB = _ModemCallStatsNumberOfTXCharsMSB_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 83),
    _ModemCallStatsNumberOfTXCharsMSB_Type()
)
modemCallStatsNumberOfTXCharsMSB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsNumberOfTXCharsMSB.setStatus("current")
_ModemCallStatsNumberOfTXChars2ndByte_Type = Integer32
_ModemCallStatsNumberOfTXChars2ndByte_Object = MibTableColumn
modemCallStatsNumberOfTXChars2ndByte = _ModemCallStatsNumberOfTXChars2ndByte_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 84),
    _ModemCallStatsNumberOfTXChars2ndByte_Type()
)
modemCallStatsNumberOfTXChars2ndByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsNumberOfTXChars2ndByte.setStatus("current")
_ModemCallStatsNumberOfTXChars3rdByte_Type = Integer32
_ModemCallStatsNumberOfTXChars3rdByte_Object = MibTableColumn
modemCallStatsNumberOfTXChars3rdByte = _ModemCallStatsNumberOfTXChars3rdByte_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 85),
    _ModemCallStatsNumberOfTXChars3rdByte_Type()
)
modemCallStatsNumberOfTXChars3rdByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsNumberOfTXChars3rdByte.setStatus("current")
_ModemCallStatsNumberOfTXCharsLSB_Type = Integer32
_ModemCallStatsNumberOfTXCharsLSB_Object = MibTableColumn
modemCallStatsNumberOfTXCharsLSB = _ModemCallStatsNumberOfTXCharsLSB_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 86),
    _ModemCallStatsNumberOfTXCharsLSB_Type()
)
modemCallStatsNumberOfTXCharsLSB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsNumberOfTXCharsLSB.setStatus("current")
_ModemCallStatsNumberOfRXCharsMSB_Type = Integer32
_ModemCallStatsNumberOfRXCharsMSB_Object = MibTableColumn
modemCallStatsNumberOfRXCharsMSB = _ModemCallStatsNumberOfRXCharsMSB_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 87),
    _ModemCallStatsNumberOfRXCharsMSB_Type()
)
modemCallStatsNumberOfRXCharsMSB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsNumberOfRXCharsMSB.setStatus("current")
_ModemCallStatsNumberOfRXChars2ndByte_Type = Integer32
_ModemCallStatsNumberOfRXChars2ndByte_Object = MibTableColumn
modemCallStatsNumberOfRXChars2ndByte = _ModemCallStatsNumberOfRXChars2ndByte_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 88),
    _ModemCallStatsNumberOfRXChars2ndByte_Type()
)
modemCallStatsNumberOfRXChars2ndByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsNumberOfRXChars2ndByte.setStatus("current")
_ModemCallStatsNumberOfRXChars3rdByte_Type = Integer32
_ModemCallStatsNumberOfRXChars3rdByte_Object = MibTableColumn
modemCallStatsNumberOfRXChars3rdByte = _ModemCallStatsNumberOfRXChars3rdByte_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 89),
    _ModemCallStatsNumberOfRXChars3rdByte_Type()
)
modemCallStatsNumberOfRXChars3rdByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsNumberOfRXChars3rdByte.setStatus("current")
_ModemCallStatsNumberOfRXCharsLSB_Type = Integer32
_ModemCallStatsNumberOfRXCharsLSB_Object = MibTableColumn
modemCallStatsNumberOfRXCharsLSB = _ModemCallStatsNumberOfRXCharsLSB_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 90),
    _ModemCallStatsNumberOfRXCharsLSB_Type()
)
modemCallStatsNumberOfRXCharsLSB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsNumberOfRXCharsLSB.setStatus("current")


class _ModemCallStatsDisconnectReason_Type(DisplayString):
    """Custom type modemCallStatsDisconnectReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ModemCallStatsDisconnectReason_Type.__name__ = "DisplayString"
_ModemCallStatsDisconnectReason_Object = MibTableColumn
modemCallStatsDisconnectReason = _ModemCallStatsDisconnectReason_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 91),
    _ModemCallStatsDisconnectReason_Type()
)
modemCallStatsDisconnectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsDisconnectReason.setStatus("current")


class _ModemCallStatsRetrainReason_Type(DisplayString):
    """Custom type modemCallStatsRetrainReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ModemCallStatsRetrainReason_Type.__name__ = "DisplayString"
_ModemCallStatsRetrainReason_Object = MibTableColumn
modemCallStatsRetrainReason = _ModemCallStatsRetrainReason_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 92),
    _ModemCallStatsRetrainReason_Type()
)
modemCallStatsRetrainReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsRetrainReason.setStatus("current")


class _ModemCallStatsAbortCode_Type(DisplayString):
    """Custom type modemCallStatsAbortCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ModemCallStatsAbortCode_Type.__name__ = "DisplayString"
_ModemCallStatsAbortCode_Object = MibTableColumn
modemCallStatsAbortCode = _ModemCallStatsAbortCode_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 93),
    _ModemCallStatsAbortCode_Type()
)
modemCallStatsAbortCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsAbortCode.setStatus("current")


class _ModemCallStatsK56Status_Type(DisplayString):
    """Custom type modemCallStatsK56Status based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ModemCallStatsK56Status_Type.__name__ = "DisplayString"
_ModemCallStatsK56Status_Object = MibTableColumn
modemCallStatsK56Status = _ModemCallStatsK56Status_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 94),
    _ModemCallStatsK56Status_Type()
)
modemCallStatsK56Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsK56Status.setStatus("current")


class _ModemCallStatsV8ManufacturerID_Type(DisplayString):
    """Custom type modemCallStatsV8ManufacturerID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModemCallStatsV8ManufacturerID_Type.__name__ = "DisplayString"
_ModemCallStatsV8ManufacturerID_Object = MibTableColumn
modemCallStatsV8ManufacturerID = _ModemCallStatsV8ManufacturerID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 95),
    _ModemCallStatsV8ManufacturerID_Type()
)
modemCallStatsV8ManufacturerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsV8ManufacturerID.setStatus("current")


class _ModemCallStatsV8LicenseeCode_Type(DisplayString):
    """Custom type modemCallStatsV8LicenseeCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModemCallStatsV8LicenseeCode_Type.__name__ = "DisplayString"
_ModemCallStatsV8LicenseeCode_Object = MibTableColumn
modemCallStatsV8LicenseeCode = _ModemCallStatsV8LicenseeCode_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 96),
    _ModemCallStatsV8LicenseeCode_Type()
)
modemCallStatsV8LicenseeCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsV8LicenseeCode.setStatus("current")


class _ModemCallStatsV8Capabilities_Type(DisplayString):
    """Custom type modemCallStatsV8Capabilities based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModemCallStatsV8Capabilities_Type.__name__ = "DisplayString"
_ModemCallStatsV8Capabilities_Object = MibTableColumn
modemCallStatsV8Capabilities = _ModemCallStatsV8Capabilities_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 97),
    _ModemCallStatsV8Capabilities_Type()
)
modemCallStatsV8Capabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsV8Capabilities.setStatus("current")


class _ModemCallStatsV8FlexVersion_Type(DisplayString):
    """Custom type modemCallStatsV8FlexVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ModemCallStatsV8FlexVersion_Type.__name__ = "DisplayString"
_ModemCallStatsV8FlexVersion_Object = MibTableColumn
modemCallStatsV8FlexVersion = _ModemCallStatsV8FlexVersion_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 98),
    _ModemCallStatsV8FlexVersion_Type()
)
modemCallStatsV8FlexVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsV8FlexVersion.setStatus("current")


class _ModemCallStatsV8DataPumpRev_Type(DisplayString):
    """Custom type modemCallStatsV8DataPumpRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModemCallStatsV8DataPumpRev_Type.__name__ = "DisplayString"
_ModemCallStatsV8DataPumpRev_Object = MibTableColumn
modemCallStatsV8DataPumpRev = _ModemCallStatsV8DataPumpRev_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 99),
    _ModemCallStatsV8DataPumpRev_Type()
)
modemCallStatsV8DataPumpRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsV8DataPumpRev.setStatus("current")


class _ModemCallStatsV8ControllerRev_Type(DisplayString):
    """Custom type modemCallStatsV8ControllerRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModemCallStatsV8ControllerRev_Type.__name__ = "DisplayString"
_ModemCallStatsV8ControllerRev_Object = MibTableColumn
modemCallStatsV8ControllerRev = _ModemCallStatsV8ControllerRev_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 100),
    _ModemCallStatsV8ControllerRev_Type()
)
modemCallStatsV8ControllerRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsV8ControllerRev.setStatus("current")


class _ModemCallStatsV8Progress_Type(DisplayString):
    """Custom type modemCallStatsV8Progress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ModemCallStatsV8Progress_Type.__name__ = "DisplayString"
_ModemCallStatsV8Progress_Object = MibTableColumn
modemCallStatsV8Progress = _ModemCallStatsV8Progress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 101),
    _ModemCallStatsV8Progress_Type()
)
modemCallStatsV8Progress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsV8Progress.setStatus("current")
_ModemCallStatsV90DigitalPadHigh_Type = Integer32
_ModemCallStatsV90DigitalPadHigh_Object = MibTableColumn
modemCallStatsV90DigitalPadHigh = _ModemCallStatsV90DigitalPadHigh_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 102),
    _ModemCallStatsV90DigitalPadHigh_Type()
)
modemCallStatsV90DigitalPadHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsV90DigitalPadHigh.setStatus("current")
_ModemCallStatsV90DigitalPadLow_Type = Integer32
_ModemCallStatsV90DigitalPadLow_Object = MibTableColumn
modemCallStatsV90DigitalPadLow = _ModemCallStatsV90DigitalPadLow_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 103),
    _ModemCallStatsV90DigitalPadLow_Type()
)
modemCallStatsV90DigitalPadLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsV90DigitalPadLow.setStatus("current")
_ModemCallStatsV90IMDRatio_Type = Integer32
_ModemCallStatsV90IMDRatio_Object = MibTableColumn
modemCallStatsV90IMDRatio = _ModemCallStatsV90IMDRatio_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 104),
    _ModemCallStatsV90IMDRatio_Type()
)
modemCallStatsV90IMDRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsV90IMDRatio.setStatus("current")
_ModemCallStatsHandshakeTime_Type = Integer32
_ModemCallStatsHandshakeTime_Object = MibTableColumn
modemCallStatsHandshakeTime = _ModemCallStatsHandshakeTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 105),
    _ModemCallStatsHandshakeTime_Type()
)
modemCallStatsHandshakeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsHandshakeTime.setStatus("current")
_ModemCallStatsNumberOfHandshakeRetries_Type = Integer32
_ModemCallStatsNumberOfHandshakeRetries_Object = MibTableColumn
modemCallStatsNumberOfHandshakeRetries = _ModemCallStatsNumberOfHandshakeRetries_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 106),
    _ModemCallStatsNumberOfHandshakeRetries_Type()
)
modemCallStatsNumberOfHandshakeRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsNumberOfHandshakeRetries.setStatus("current")
_ModemCallStatsECState1_Type = Integer32
_ModemCallStatsECState1_Object = MibTableColumn
modemCallStatsECState1 = _ModemCallStatsECState1_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 107),
    _ModemCallStatsECState1_Type()
)
modemCallStatsECState1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsECState1.setStatus("current")
_ModemCallStatsECState2_Type = Integer32
_ModemCallStatsECState2_Object = MibTableColumn
modemCallStatsECState2 = _ModemCallStatsECState2_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 108),
    _ModemCallStatsECState2_Type()
)
modemCallStatsECState2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsECState2.setStatus("current")
_ModemCallStatsFirmwareState_Type = Integer32
_ModemCallStatsFirmwareState_Object = MibTableColumn
modemCallStatsFirmwareState = _ModemCallStatsFirmwareState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 109),
    _ModemCallStatsFirmwareState_Type()
)
modemCallStatsFirmwareState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsFirmwareState.setStatus("current")
_ModemCallStatsHighAddrOfMEMACCFailure_Type = Integer32
_ModemCallStatsHighAddrOfMEMACCFailure_Object = MibTableColumn
modemCallStatsHighAddrOfMEMACCFailure = _ModemCallStatsHighAddrOfMEMACCFailure_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 110),
    _ModemCallStatsHighAddrOfMEMACCFailure_Type()
)
modemCallStatsHighAddrOfMEMACCFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsHighAddrOfMEMACCFailure.setStatus("current")
_ModemCallStatsLowAddrOfMEMACCFailure_Type = Integer32
_ModemCallStatsLowAddrOfMEMACCFailure_Object = MibTableColumn
modemCallStatsLowAddrOfMEMACCFailure = _ModemCallStatsLowAddrOfMEMACCFailure_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 111),
    _ModemCallStatsLowAddrOfMEMACCFailure_Type()
)
modemCallStatsLowAddrOfMEMACCFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsLowAddrOfMEMACCFailure.setStatus("current")
_ModemCallStatsMinutesSinceRetrain_Type = Integer32
_ModemCallStatsMinutesSinceRetrain_Object = MibTableColumn
modemCallStatsMinutesSinceRetrain = _ModemCallStatsMinutesSinceRetrain_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 112),
    _ModemCallStatsMinutesSinceRetrain_Type()
)
modemCallStatsMinutesSinceRetrain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsMinutesSinceRetrain.setStatus("current")
_ModemCallStatsWAStatus_Type = Integer32
_ModemCallStatsWAStatus_Object = MibTableColumn
modemCallStatsWAStatus = _ModemCallStatsWAStatus_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 113),
    _ModemCallStatsWAStatus_Type()
)
modemCallStatsWAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsWAStatus.setStatus("current")


class _ModemCallStatsRoundTripTime_Type(DisplayString):
    """Custom type modemCallStatsRoundTripTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModemCallStatsRoundTripTime_Type.__name__ = "DisplayString"
_ModemCallStatsRoundTripTime_Object = MibTableColumn
modemCallStatsRoundTripTime = _ModemCallStatsRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 114),
    _ModemCallStatsRoundTripTime_Type()
)
modemCallStatsRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsRoundTripTime.setStatus("current")
_ModemCallStatsDataIsValid_Type = Integer32
_ModemCallStatsDataIsValid_Object = MibTableColumn
modemCallStatsDataIsValid = _ModemCallStatsDataIsValid_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 201),
    _ModemCallStatsDataIsValid_Type()
)
modemCallStatsDataIsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsDataIsValid.setStatus("current")
_ModemCallStatsSessionID_Type = Integer32
_ModemCallStatsSessionID_Object = MibTableColumn
modemCallStatsSessionID = _ModemCallStatsSessionID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 202),
    _ModemCallStatsSessionID_Type()
)
modemCallStatsSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsSessionID.setStatus("current")
_ModemCallStatsSlotIndex_Type = Integer32
_ModemCallStatsSlotIndex_Object = MibTableColumn
modemCallStatsSlotIndex = _ModemCallStatsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 203),
    _ModemCallStatsSlotIndex_Type()
)
modemCallStatsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsSlotIndex.setStatus("current")
_ModemCallStatsModemIndex_Type = Integer32
_ModemCallStatsModemIndex_Object = MibTableColumn
modemCallStatsModemIndex = _ModemCallStatsModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1423, 1, 204),
    _ModemCallStatsModemIndex_Type()
)
modemCallStatsModemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCallStatsModemIndex.setStatus("current")
_ModemSummaryStatsTable_Object = MibTable
modemSummaryStatsTable = _ModemSummaryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1424)
)
if mibBuilder.loadTexts:
    modemSummaryStatsTable.setStatus("current")
_ModemSummaryStatsEntry_Object = MibTableRow
modemSummaryStatsEntry = _ModemSummaryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1424, 1)
)
modemSummaryStatsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "modemSummaryStatsSlotNumber"),
)
if mibBuilder.loadTexts:
    modemSummaryStatsEntry.setStatus("current")
_ModemSummaryStatsSlotNumber_Type = Integer32
_ModemSummaryStatsSlotNumber_Object = MibTableColumn
modemSummaryStatsSlotNumber = _ModemSummaryStatsSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1424, 1, 1),
    _ModemSummaryStatsSlotNumber_Type()
)
modemSummaryStatsSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSummaryStatsSlotNumber.setStatus("current")
_ModemSummaryStatsModemCount_Type = Integer32
_ModemSummaryStatsModemCount_Object = MibTableColumn
modemSummaryStatsModemCount = _ModemSummaryStatsModemCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1424, 1, 2),
    _ModemSummaryStatsModemCount_Type()
)
modemSummaryStatsModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSummaryStatsModemCount.setStatus("current")
_ModemSummaryStatsDisabledCount_Type = Integer32
_ModemSummaryStatsDisabledCount_Object = MibTableColumn
modemSummaryStatsDisabledCount = _ModemSummaryStatsDisabledCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1424, 1, 3),
    _ModemSummaryStatsDisabledCount_Type()
)
modemSummaryStatsDisabledCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSummaryStatsDisabledCount.setStatus("current")
_ModemSummaryStatsNoDownloadCount_Type = Integer32
_ModemSummaryStatsNoDownloadCount_Object = MibTableColumn
modemSummaryStatsNoDownloadCount = _ModemSummaryStatsNoDownloadCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1424, 1, 4),
    _ModemSummaryStatsNoDownloadCount_Type()
)
modemSummaryStatsNoDownloadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSummaryStatsNoDownloadCount.setStatus("current")
_ModemSummaryStatsDeadCount_Type = Integer32
_ModemSummaryStatsDeadCount_Object = MibTableColumn
modemSummaryStatsDeadCount = _ModemSummaryStatsDeadCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1424, 1, 5),
    _ModemSummaryStatsDeadCount_Type()
)
modemSummaryStatsDeadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSummaryStatsDeadCount.setStatus("current")
_ModemSummaryStatsRemovedCount_Type = Integer32
_ModemSummaryStatsRemovedCount_Object = MibTableColumn
modemSummaryStatsRemovedCount = _ModemSummaryStatsRemovedCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1424, 1, 6),
    _ModemSummaryStatsRemovedCount_Type()
)
modemSummaryStatsRemovedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSummaryStatsRemovedCount.setStatus("current")
_ModemSummaryStatsIdleCount_Type = Integer32
_ModemSummaryStatsIdleCount_Object = MibTableColumn
modemSummaryStatsIdleCount = _ModemSummaryStatsIdleCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1424, 1, 7),
    _ModemSummaryStatsIdleCount_Type()
)
modemSummaryStatsIdleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSummaryStatsIdleCount.setStatus("current")
_ModemSummaryStatsActiveCount_Type = Integer32
_ModemSummaryStatsActiveCount_Object = MibTableColumn
modemSummaryStatsActiveCount = _ModemSummaryStatsActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1424, 1, 8),
    _ModemSummaryStatsActiveCount_Type()
)
modemSummaryStatsActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSummaryStatsActiveCount.setStatus("current")
_ModemSummaryStatsDownloadingCount_Type = Integer32
_ModemSummaryStatsDownloadingCount_Object = MibTableColumn
modemSummaryStatsDownloadingCount = _ModemSummaryStatsDownloadingCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1424, 1, 9),
    _ModemSummaryStatsDownloadingCount_Type()
)
modemSummaryStatsDownloadingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSummaryStatsDownloadingCount.setStatus("current")
_ModemSummaryStatsTotalCalls_Type = Integer32
_ModemSummaryStatsTotalCalls_Object = MibTableColumn
modemSummaryStatsTotalCalls = _ModemSummaryStatsTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1424, 1, 101),
    _ModemSummaryStatsTotalCalls_Type()
)
modemSummaryStatsTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSummaryStatsTotalCalls.setStatus("current")
_ModemSummaryStatsConnectedCalls_Type = Integer32
_ModemSummaryStatsConnectedCalls_Object = MibTableColumn
modemSummaryStatsConnectedCalls = _ModemSummaryStatsConnectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1424, 1, 102),
    _ModemSummaryStatsConnectedCalls_Type()
)
modemSummaryStatsConnectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSummaryStatsConnectedCalls.setStatus("current")
_ModemSummaryStatsAuthCalls_Type = Integer32
_ModemSummaryStatsAuthCalls_Object = MibTableColumn
modemSummaryStatsAuthCalls = _ModemSummaryStatsAuthCalls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1424, 1, 103),
    _ModemSummaryStatsAuthCalls_Type()
)
modemSummaryStatsAuthCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSummaryStatsAuthCalls.setStatus("current")
_ModemSummaryStatsECCalls_Type = Integer32
_ModemSummaryStatsECCalls_Object = MibTableColumn
modemSummaryStatsECCalls = _ModemSummaryStatsECCalls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1424, 1, 104),
    _ModemSummaryStatsECCalls_Type()
)
modemSummaryStatsECCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSummaryStatsECCalls.setStatus("current")
_ModemSummaryStatsDCCalls_Type = Integer32
_ModemSummaryStatsDCCalls_Object = MibTableColumn
modemSummaryStatsDCCalls = _ModemSummaryStatsDCCalls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1424, 1, 105),
    _ModemSummaryStatsDCCalls_Type()
)
modemSummaryStatsDCCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSummaryStatsDCCalls.setStatus("current")
_ModemSummaryStatsK56Calls_Type = Integer32
_ModemSummaryStatsK56Calls_Object = MibTableColumn
modemSummaryStatsK56Calls = _ModemSummaryStatsK56Calls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1424, 1, 106),
    _ModemSummaryStatsK56Calls_Type()
)
modemSummaryStatsK56Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSummaryStatsK56Calls.setStatus("current")
_ModemSummaryStatsV90Calls_Type = Integer32
_ModemSummaryStatsV90Calls_Object = MibTableColumn
modemSummaryStatsV90Calls = _ModemSummaryStatsV90Calls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1424, 1, 107),
    _ModemSummaryStatsV90Calls_Type()
)
modemSummaryStatsV90Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSummaryStatsV90Calls.setStatus("current")
_ModemSummaryStatsV34Calls_Type = Integer32
_ModemSummaryStatsV34Calls_Object = MibTableColumn
modemSummaryStatsV34Calls = _ModemSummaryStatsV34Calls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1424, 1, 108),
    _ModemSummaryStatsV34Calls_Type()
)
modemSummaryStatsV34Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSummaryStatsV34Calls.setStatus("current")
_ModemSummaryStatsV32Calls_Type = Integer32
_ModemSummaryStatsV32Calls_Object = MibTableColumn
modemSummaryStatsV32Calls = _ModemSummaryStatsV32Calls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1424, 1, 109),
    _ModemSummaryStatsV32Calls_Type()
)
modemSummaryStatsV32Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSummaryStatsV32Calls.setStatus("current")
_ModemSummaryStatsReuseSuspectModems_Type = Boolean
_ModemSummaryStatsReuseSuspectModems_Object = MibTableColumn
modemSummaryStatsReuseSuspectModems = _ModemSummaryStatsReuseSuspectModems_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1424, 1, 201),
    _ModemSummaryStatsReuseSuspectModems_Type()
)
modemSummaryStatsReuseSuspectModems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSummaryStatsReuseSuspectModems.setStatus("current")
_ModemSummaryStatsUpTime_Type = Integer32
_ModemSummaryStatsUpTime_Object = MibTableColumn
modemSummaryStatsUpTime = _ModemSummaryStatsUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1424, 1, 301),
    _ModemSummaryStatsUpTime_Type()
)
modemSummaryStatsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSummaryStatsUpTime.setStatus("current")
_ModemSummaryStatsMaximumCalls_Type = Integer32
_ModemSummaryStatsMaximumCalls_Object = MibTableColumn
modemSummaryStatsMaximumCalls = _ModemSummaryStatsMaximumCalls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1424, 1, 401),
    _ModemSummaryStatsMaximumCalls_Type()
)
modemSummaryStatsMaximumCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSummaryStatsMaximumCalls.setStatus("current")
_ModemIntervalStatsTable_Object = MibTable
modemIntervalStatsTable = _ModemIntervalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425)
)
if mibBuilder.loadTexts:
    modemIntervalStatsTable.setStatus("current")
_ModemIntervalStatsEntry_Object = MibTableRow
modemIntervalStatsEntry = _ModemIntervalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425, 1)
)
modemIntervalStatsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "modemIntervalStatsIndex"),
)
if mibBuilder.loadTexts:
    modemIntervalStatsEntry.setStatus("current")
_ModemIntervalStatsIndex_Type = Integer32
_ModemIntervalStatsIndex_Object = MibTableColumn
modemIntervalStatsIndex = _ModemIntervalStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425, 1, 1),
    _ModemIntervalStatsIndex_Type()
)
modemIntervalStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIntervalStatsIndex.setStatus("current")
_ModemIntervalStatsStartTime_Type = Integer32
_ModemIntervalStatsStartTime_Object = MibTableColumn
modemIntervalStatsStartTime = _ModemIntervalStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425, 1, 2),
    _ModemIntervalStatsStartTime_Type()
)
modemIntervalStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIntervalStatsStartTime.setStatus("current")
_ModemIntervalStatsStopTime_Type = Integer32
_ModemIntervalStatsStopTime_Object = MibTableColumn
modemIntervalStatsStopTime = _ModemIntervalStatsStopTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425, 1, 3),
    _ModemIntervalStatsStopTime_Type()
)
modemIntervalStatsStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIntervalStatsStopTime.setStatus("current")
_ModemIntervalStatsModemCount_Type = Integer32
_ModemIntervalStatsModemCount_Object = MibTableColumn
modemIntervalStatsModemCount = _ModemIntervalStatsModemCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425, 1, 4),
    _ModemIntervalStatsModemCount_Type()
)
modemIntervalStatsModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIntervalStatsModemCount.setStatus("current")
_ModemIntervalStatsDisabledCount_Type = Integer32
_ModemIntervalStatsDisabledCount_Object = MibTableColumn
modemIntervalStatsDisabledCount = _ModemIntervalStatsDisabledCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425, 1, 5),
    _ModemIntervalStatsDisabledCount_Type()
)
modemIntervalStatsDisabledCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIntervalStatsDisabledCount.setStatus("current")
_ModemIntervalStatsNoDownloadCount_Type = Integer32
_ModemIntervalStatsNoDownloadCount_Object = MibTableColumn
modemIntervalStatsNoDownloadCount = _ModemIntervalStatsNoDownloadCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425, 1, 6),
    _ModemIntervalStatsNoDownloadCount_Type()
)
modemIntervalStatsNoDownloadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIntervalStatsNoDownloadCount.setStatus("current")
_ModemIntervalStatsDeadCount_Type = Integer32
_ModemIntervalStatsDeadCount_Object = MibTableColumn
modemIntervalStatsDeadCount = _ModemIntervalStatsDeadCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425, 1, 7),
    _ModemIntervalStatsDeadCount_Type()
)
modemIntervalStatsDeadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIntervalStatsDeadCount.setStatus("current")
_ModemIntervalStatsRemovedCount_Type = Integer32
_ModemIntervalStatsRemovedCount_Object = MibTableColumn
modemIntervalStatsRemovedCount = _ModemIntervalStatsRemovedCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425, 1, 8),
    _ModemIntervalStatsRemovedCount_Type()
)
modemIntervalStatsRemovedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIntervalStatsRemovedCount.setStatus("current")
_ModemIntervalStatsIdleCount_Type = Integer32
_ModemIntervalStatsIdleCount_Object = MibTableColumn
modemIntervalStatsIdleCount = _ModemIntervalStatsIdleCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425, 1, 9),
    _ModemIntervalStatsIdleCount_Type()
)
modemIntervalStatsIdleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIntervalStatsIdleCount.setStatus("current")
_ModemIntervalStatsActiveCount_Type = Integer32
_ModemIntervalStatsActiveCount_Object = MibTableColumn
modemIntervalStatsActiveCount = _ModemIntervalStatsActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425, 1, 10),
    _ModemIntervalStatsActiveCount_Type()
)
modemIntervalStatsActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIntervalStatsActiveCount.setStatus("current")
_ModemIntervalStatsDownloadingCount_Type = Integer32
_ModemIntervalStatsDownloadingCount_Object = MibTableColumn
modemIntervalStatsDownloadingCount = _ModemIntervalStatsDownloadingCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425, 1, 11),
    _ModemIntervalStatsDownloadingCount_Type()
)
modemIntervalStatsDownloadingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIntervalStatsDownloadingCount.setStatus("current")
_ModemIntervalStatsTotalCalls_Type = Integer32
_ModemIntervalStatsTotalCalls_Object = MibTableColumn
modemIntervalStatsTotalCalls = _ModemIntervalStatsTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425, 1, 101),
    _ModemIntervalStatsTotalCalls_Type()
)
modemIntervalStatsTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIntervalStatsTotalCalls.setStatus("current")
_ModemIntervalStatsConnectedCalls_Type = Integer32
_ModemIntervalStatsConnectedCalls_Object = MibTableColumn
modemIntervalStatsConnectedCalls = _ModemIntervalStatsConnectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425, 1, 102),
    _ModemIntervalStatsConnectedCalls_Type()
)
modemIntervalStatsConnectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIntervalStatsConnectedCalls.setStatus("current")
_ModemIntervalStatsAuthCalls_Type = Integer32
_ModemIntervalStatsAuthCalls_Object = MibTableColumn
modemIntervalStatsAuthCalls = _ModemIntervalStatsAuthCalls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425, 1, 103),
    _ModemIntervalStatsAuthCalls_Type()
)
modemIntervalStatsAuthCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIntervalStatsAuthCalls.setStatus("current")
_ModemIntervalStatsECCalls_Type = Integer32
_ModemIntervalStatsECCalls_Object = MibTableColumn
modemIntervalStatsECCalls = _ModemIntervalStatsECCalls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425, 1, 104),
    _ModemIntervalStatsECCalls_Type()
)
modemIntervalStatsECCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIntervalStatsECCalls.setStatus("current")
_ModemIntervalStatsDCCalls_Type = Integer32
_ModemIntervalStatsDCCalls_Object = MibTableColumn
modemIntervalStatsDCCalls = _ModemIntervalStatsDCCalls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425, 1, 105),
    _ModemIntervalStatsDCCalls_Type()
)
modemIntervalStatsDCCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIntervalStatsDCCalls.setStatus("current")
_ModemIntervalStatsK56Calls_Type = Integer32
_ModemIntervalStatsK56Calls_Object = MibTableColumn
modemIntervalStatsK56Calls = _ModemIntervalStatsK56Calls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425, 1, 106),
    _ModemIntervalStatsK56Calls_Type()
)
modemIntervalStatsK56Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIntervalStatsK56Calls.setStatus("current")
_ModemIntervalStatsV90Calls_Type = Integer32
_ModemIntervalStatsV90Calls_Object = MibTableColumn
modemIntervalStatsV90Calls = _ModemIntervalStatsV90Calls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425, 1, 107),
    _ModemIntervalStatsV90Calls_Type()
)
modemIntervalStatsV90Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIntervalStatsV90Calls.setStatus("current")
_ModemIntervalStatsV34Calls_Type = Integer32
_ModemIntervalStatsV34Calls_Object = MibTableColumn
modemIntervalStatsV34Calls = _ModemIntervalStatsV34Calls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425, 1, 108),
    _ModemIntervalStatsV34Calls_Type()
)
modemIntervalStatsV34Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIntervalStatsV34Calls.setStatus("current")
_ModemIntervalStatsV32Calls_Type = Integer32
_ModemIntervalStatsV32Calls_Object = MibTableColumn
modemIntervalStatsV32Calls = _ModemIntervalStatsV32Calls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425, 1, 109),
    _ModemIntervalStatsV32Calls_Type()
)
modemIntervalStatsV32Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIntervalStatsV32Calls.setStatus("current")
_ModemIntervalStatsOverallTotalCalls_Type = Integer32
_ModemIntervalStatsOverallTotalCalls_Object = MibTableColumn
modemIntervalStatsOverallTotalCalls = _ModemIntervalStatsOverallTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425, 1, 201),
    _ModemIntervalStatsOverallTotalCalls_Type()
)
modemIntervalStatsOverallTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIntervalStatsOverallTotalCalls.setStatus("current")
_ModemIntervalStatsOverallConnectedCalls_Type = Integer32
_ModemIntervalStatsOverallConnectedCalls_Object = MibTableColumn
modemIntervalStatsOverallConnectedCalls = _ModemIntervalStatsOverallConnectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425, 1, 202),
    _ModemIntervalStatsOverallConnectedCalls_Type()
)
modemIntervalStatsOverallConnectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIntervalStatsOverallConnectedCalls.setStatus("current")
_ModemIntervalStatsOverallAuthCalls_Type = Integer32
_ModemIntervalStatsOverallAuthCalls_Object = MibTableColumn
modemIntervalStatsOverallAuthCalls = _ModemIntervalStatsOverallAuthCalls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1425, 1, 203),
    _ModemIntervalStatsOverallAuthCalls_Type()
)
modemIntervalStatsOverallAuthCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIntervalStatsOverallAuthCalls.setStatus("current")
_ModemSessionStatsTable_Object = MibTable
modemSessionStatsTable = _ModemSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1426)
)
if mibBuilder.loadTexts:
    modemSessionStatsTable.setStatus("current")
_ModemSessionStatsEntry_Object = MibTableRow
modemSessionStatsEntry = _ModemSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1426, 1)
)
modemSessionStatsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "modemSessionStatsSlotNumber"),
    (0, "APTIS-MONITOR-MIB", "modemSessionStatsModemIndex"),
)
if mibBuilder.loadTexts:
    modemSessionStatsEntry.setStatus("current")


class _ModemSessionStatsDataValidity_Type(Integer32):
    """Custom type modemSessionStatsDataValidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notCaptured", 1),
          ("valid", 0))
    )


_ModemSessionStatsDataValidity_Type.__name__ = "Integer32"
_ModemSessionStatsDataValidity_Object = MibTableColumn
modemSessionStatsDataValidity = _ModemSessionStatsDataValidity_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1426, 1, 1),
    _ModemSessionStatsDataValidity_Type()
)
modemSessionStatsDataValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStatsDataValidity.setStatus("current")
_ModemSessionStatsSessionID_Type = Integer32
_ModemSessionStatsSessionID_Object = MibTableColumn
modemSessionStatsSessionID = _ModemSessionStatsSessionID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1426, 1, 2),
    _ModemSessionStatsSessionID_Type()
)
modemSessionStatsSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStatsSessionID.setStatus("current")
_ModemSessionStatsSlotNumber_Type = Integer32
_ModemSessionStatsSlotNumber_Object = MibTableColumn
modemSessionStatsSlotNumber = _ModemSessionStatsSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1426, 1, 3),
    _ModemSessionStatsSlotNumber_Type()
)
modemSessionStatsSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStatsSlotNumber.setStatus("current")
_ModemSessionStatsIOPNumber_Type = Integer32
_ModemSessionStatsIOPNumber_Object = MibTableColumn
modemSessionStatsIOPNumber = _ModemSessionStatsIOPNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1426, 1, 4),
    _ModemSessionStatsIOPNumber_Type()
)
modemSessionStatsIOPNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStatsIOPNumber.setStatus("current")
_ModemSessionStatsDMMNumber_Type = Integer32
_ModemSessionStatsDMMNumber_Object = MibTableColumn
modemSessionStatsDMMNumber = _ModemSessionStatsDMMNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1426, 1, 5),
    _ModemSessionStatsDMMNumber_Type()
)
modemSessionStatsDMMNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStatsDMMNumber.setStatus("current")
_ModemSessionStatsPackNumber_Type = Integer32
_ModemSessionStatsPackNumber_Object = MibTableColumn
modemSessionStatsPackNumber = _ModemSessionStatsPackNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1426, 1, 6),
    _ModemSessionStatsPackNumber_Type()
)
modemSessionStatsPackNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStatsPackNumber.setStatus("current")
_ModemSessionStatsModemNumber_Type = Integer32
_ModemSessionStatsModemNumber_Object = MibTableColumn
modemSessionStatsModemNumber = _ModemSessionStatsModemNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1426, 1, 7),
    _ModemSessionStatsModemNumber_Type()
)
modemSessionStatsModemNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStatsModemNumber.setStatus("current")
_ModemSessionStatsModemIndex_Type = Integer32
_ModemSessionStatsModemIndex_Object = MibTableColumn
modemSessionStatsModemIndex = _ModemSessionStatsModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1426, 1, 8),
    _ModemSessionStatsModemIndex_Type()
)
modemSessionStatsModemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStatsModemIndex.setStatus("current")
_ModemSessionStatsTDMStream_Type = Integer32
_ModemSessionStatsTDMStream_Object = MibTableColumn
modemSessionStatsTDMStream = _ModemSessionStatsTDMStream_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1426, 1, 101),
    _ModemSessionStatsTDMStream_Type()
)
modemSessionStatsTDMStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStatsTDMStream.setStatus("current")
_ModemSessionStatsTDMSlot_Type = Integer32
_ModemSessionStatsTDMSlot_Object = MibTableColumn
modemSessionStatsTDMSlot = _ModemSessionStatsTDMSlot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1426, 1, 102),
    _ModemSessionStatsTDMSlot_Type()
)
modemSessionStatsTDMSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStatsTDMSlot.setStatus("current")
_ModemSessionStatsInitialTxSpeed_Type = Integer32
_ModemSessionStatsInitialTxSpeed_Object = MibTableColumn
modemSessionStatsInitialTxSpeed = _ModemSessionStatsInitialTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1426, 1, 201),
    _ModemSessionStatsInitialTxSpeed_Type()
)
modemSessionStatsInitialTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStatsInitialTxSpeed.setStatus("current")
_ModemSessionStatsInitialRxSpeed_Type = Integer32
_ModemSessionStatsInitialRxSpeed_Object = MibTableColumn
modemSessionStatsInitialRxSpeed = _ModemSessionStatsInitialRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1426, 1, 202),
    _ModemSessionStatsInitialRxSpeed_Type()
)
modemSessionStatsInitialRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStatsInitialRxSpeed.setStatus("current")


class _ModemSessionStatsConnectString_Type(DisplayString):
    """Custom type modemSessionStatsConnectString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ModemSessionStatsConnectString_Type.__name__ = "DisplayString"
_ModemSessionStatsConnectString_Object = MibTableColumn
modemSessionStatsConnectString = _ModemSessionStatsConnectString_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1426, 1, 301),
    _ModemSessionStatsConnectString_Type()
)
modemSessionStatsConnectString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStatsConnectString.setStatus("current")


class _ModemSessionStatsAmpV2String_Type(OctetString):
    """Custom type modemSessionStatsAmpV2String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_ModemSessionStatsAmpV2String_Type.__name__ = "OctetString"
_ModemSessionStatsAmpV2String_Object = MibTableColumn
modemSessionStatsAmpV2String = _ModemSessionStatsAmpV2String_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1426, 1, 401),
    _ModemSessionStatsAmpV2String_Type()
)
modemSessionStatsAmpV2String.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStatsAmpV2String.setStatus("current")
_ModemSessionStats2Table_Object = MibTable
modemSessionStats2Table = _ModemSessionStats2Table_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1427)
)
if mibBuilder.loadTexts:
    modemSessionStats2Table.setStatus("current")
_ModemSessionStats2Entry_Object = MibTableRow
modemSessionStats2Entry = _ModemSessionStats2Entry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1427, 1)
)
modemSessionStats2Entry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "modemSessionStats2SessionID"),
)
if mibBuilder.loadTexts:
    modemSessionStats2Entry.setStatus("current")


class _ModemSessionStats2DataValidity_Type(Integer32):
    """Custom type modemSessionStats2DataValidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notCaptured", 1),
          ("valid", 0))
    )


_ModemSessionStats2DataValidity_Type.__name__ = "Integer32"
_ModemSessionStats2DataValidity_Object = MibTableColumn
modemSessionStats2DataValidity = _ModemSessionStats2DataValidity_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1427, 1, 1),
    _ModemSessionStats2DataValidity_Type()
)
modemSessionStats2DataValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStats2DataValidity.setStatus("current")
_ModemSessionStats2SessionID_Type = Integer32
_ModemSessionStats2SessionID_Object = MibTableColumn
modemSessionStats2SessionID = _ModemSessionStats2SessionID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1427, 1, 2),
    _ModemSessionStats2SessionID_Type()
)
modemSessionStats2SessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStats2SessionID.setStatus("current")
_ModemSessionStats2SlotNumber_Type = Integer32
_ModemSessionStats2SlotNumber_Object = MibTableColumn
modemSessionStats2SlotNumber = _ModemSessionStats2SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1427, 1, 3),
    _ModemSessionStats2SlotNumber_Type()
)
modemSessionStats2SlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStats2SlotNumber.setStatus("current")
_ModemSessionStats2IOPNumber_Type = Integer32
_ModemSessionStats2IOPNumber_Object = MibTableColumn
modemSessionStats2IOPNumber = _ModemSessionStats2IOPNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1427, 1, 4),
    _ModemSessionStats2IOPNumber_Type()
)
modemSessionStats2IOPNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStats2IOPNumber.setStatus("current")
_ModemSessionStats2DMMNumber_Type = Integer32
_ModemSessionStats2DMMNumber_Object = MibTableColumn
modemSessionStats2DMMNumber = _ModemSessionStats2DMMNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1427, 1, 5),
    _ModemSessionStats2DMMNumber_Type()
)
modemSessionStats2DMMNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStats2DMMNumber.setStatus("current")
_ModemSessionStats2PackNumber_Type = Integer32
_ModemSessionStats2PackNumber_Object = MibTableColumn
modemSessionStats2PackNumber = _ModemSessionStats2PackNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1427, 1, 6),
    _ModemSessionStats2PackNumber_Type()
)
modemSessionStats2PackNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStats2PackNumber.setStatus("current")
_ModemSessionStats2ModemNumber_Type = Integer32
_ModemSessionStats2ModemNumber_Object = MibTableColumn
modemSessionStats2ModemNumber = _ModemSessionStats2ModemNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1427, 1, 7),
    _ModemSessionStats2ModemNumber_Type()
)
modemSessionStats2ModemNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStats2ModemNumber.setStatus("current")
_ModemSessionStats2ModemIndex_Type = Integer32
_ModemSessionStats2ModemIndex_Object = MibTableColumn
modemSessionStats2ModemIndex = _ModemSessionStats2ModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1427, 1, 8),
    _ModemSessionStats2ModemIndex_Type()
)
modemSessionStats2ModemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStats2ModemIndex.setStatus("current")
_ModemSessionStats2TDMStream_Type = Integer32
_ModemSessionStats2TDMStream_Object = MibTableColumn
modemSessionStats2TDMStream = _ModemSessionStats2TDMStream_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1427, 1, 101),
    _ModemSessionStats2TDMStream_Type()
)
modemSessionStats2TDMStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStats2TDMStream.setStatus("current")
_ModemSessionStats2TDMSlot_Type = Integer32
_ModemSessionStats2TDMSlot_Object = MibTableColumn
modemSessionStats2TDMSlot = _ModemSessionStats2TDMSlot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1427, 1, 102),
    _ModemSessionStats2TDMSlot_Type()
)
modemSessionStats2TDMSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStats2TDMSlot.setStatus("current")
_ModemSessionStats2InitialTxSpeed_Type = Integer32
_ModemSessionStats2InitialTxSpeed_Object = MibTableColumn
modemSessionStats2InitialTxSpeed = _ModemSessionStats2InitialTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1427, 1, 201),
    _ModemSessionStats2InitialTxSpeed_Type()
)
modemSessionStats2InitialTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStats2InitialTxSpeed.setStatus("current")
_ModemSessionStats2InitialRxSpeed_Type = Integer32
_ModemSessionStats2InitialRxSpeed_Object = MibTableColumn
modemSessionStats2InitialRxSpeed = _ModemSessionStats2InitialRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1427, 1, 202),
    _ModemSessionStats2InitialRxSpeed_Type()
)
modemSessionStats2InitialRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStats2InitialRxSpeed.setStatus("current")


class _ModemSessionStats2ConnectString_Type(DisplayString):
    """Custom type modemSessionStats2ConnectString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ModemSessionStats2ConnectString_Type.__name__ = "DisplayString"
_ModemSessionStats2ConnectString_Object = MibTableColumn
modemSessionStats2ConnectString = _ModemSessionStats2ConnectString_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1427, 1, 301),
    _ModemSessionStats2ConnectString_Type()
)
modemSessionStats2ConnectString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStats2ConnectString.setStatus("current")


class _ModemSessionStats2AmpV2String_Type(OctetString):
    """Custom type modemSessionStats2AmpV2String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_ModemSessionStats2AmpV2String_Type.__name__ = "OctetString"
_ModemSessionStats2AmpV2String_Object = MibTableColumn
modemSessionStats2AmpV2String = _ModemSessionStats2AmpV2String_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1427, 1, 401),
    _ModemSessionStats2AmpV2String_Type()
)
modemSessionStats2AmpV2String.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSessionStats2AmpV2String.setStatus("current")
_DvsStatusTable_Object = MibTable
dvsStatusTable = _DvsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1505)
)
if mibBuilder.loadTexts:
    dvsStatusTable.setStatus("current")
_DvsStatusEntry_Object = MibTableRow
dvsStatusEntry = _DvsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1505, 1)
)
dvsStatusEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "dvsStatusLocalCLID"),
)
if mibBuilder.loadTexts:
    dvsStatusEntry.setStatus("current")
_DvsStatusLocalCLID_Type = Integer32
_DvsStatusLocalCLID_Object = MibTableColumn
dvsStatusLocalCLID = _DvsStatusLocalCLID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1505, 1, 1),
    _DvsStatusLocalCLID_Type()
)
dvsStatusLocalCLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusLocalCLID.setStatus("current")
_DvsStatusRemoteCLID_Type = Integer32
_DvsStatusRemoteCLID_Object = MibTableColumn
dvsStatusRemoteCLID = _DvsStatusRemoteCLID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1505, 1, 2),
    _DvsStatusRemoteCLID_Type()
)
dvsStatusRemoteCLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusRemoteCLID.setStatus("current")
_DvsStatusLocalAddress_Type = IpAddress
_DvsStatusLocalAddress_Object = MibTableColumn
dvsStatusLocalAddress = _DvsStatusLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1505, 1, 3),
    _DvsStatusLocalAddress_Type()
)
dvsStatusLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusLocalAddress.setStatus("current")
_DvsStatusRemoteAddress_Type = IpAddress
_DvsStatusRemoteAddress_Object = MibTableColumn
dvsStatusRemoteAddress = _DvsStatusRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1505, 1, 4),
    _DvsStatusRemoteAddress_Type()
)
dvsStatusRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusRemoteAddress.setStatus("current")


class _DvsStatusTunnelState_Type(Integer32):
    """Custom type dvsStatusTunnelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("aUTHREPLY", 2),
          ("aWGWCFG", 1),
          ("dHCP", 5),
          ("dISC", 8),
          ("iDLE", 0),
          ("mIP", 6),
          ("mODPPPCFG", 4),
          ("oPEN", 7),
          ("pRIMGWTO", 3))
    )


_DvsStatusTunnelState_Type.__name__ = "Integer32"
_DvsStatusTunnelState_Object = MibTableColumn
dvsStatusTunnelState = _DvsStatusTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1505, 1, 5),
    _DvsStatusTunnelState_Type()
)
dvsStatusTunnelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusTunnelState.setStatus("current")
_DvsStatusUpTime_Type = Integer32
_DvsStatusUpTime_Object = MibTableColumn
dvsStatusUpTime = _DvsStatusUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1505, 1, 6),
    _DvsStatusUpTime_Type()
)
dvsStatusUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusUpTime.setStatus("current")
_DvsStatusMacSlotNumber_Type = Integer32
_DvsStatusMacSlotNumber_Object = MibTableColumn
dvsStatusMacSlotNumber = _DvsStatusMacSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1505, 1, 7),
    _DvsStatusMacSlotNumber_Type()
)
dvsStatusMacSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusMacSlotNumber.setStatus("current")
_DvsStatusVPOP_Type = Integer32
_DvsStatusVPOP_Object = MibTableColumn
dvsStatusVPOP = _DvsStatusVPOP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1505, 1, 8),
    _DvsStatusVPOP_Type()
)
dvsStatusVPOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusVPOP.setStatus("current")
_DvsStatusGreInPackets_Type = Integer32
_DvsStatusGreInPackets_Object = MibTableColumn
dvsStatusGreInPackets = _DvsStatusGreInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1505, 1, 9),
    _DvsStatusGreInPackets_Type()
)
dvsStatusGreInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusGreInPackets.setStatus("current")
_DvsStatusGreOutPackets_Type = Integer32
_DvsStatusGreOutPackets_Object = MibTableColumn
dvsStatusGreOutPackets = _DvsStatusGreOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1505, 1, 10),
    _DvsStatusGreOutPackets_Type()
)
dvsStatusGreOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusGreOutPackets.setStatus("current")
_DvsStatusGreChecksumError_Type = Integer32
_DvsStatusGreChecksumError_Object = MibTableColumn
dvsStatusGreChecksumError = _DvsStatusGreChecksumError_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1505, 1, 11),
    _DvsStatusGreChecksumError_Type()
)
dvsStatusGreChecksumError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusGreChecksumError.setStatus("current")
_DvsStatusGreInDropped_Type = Integer32
_DvsStatusGreInDropped_Object = MibTableColumn
dvsStatusGreInDropped = _DvsStatusGreInDropped_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1505, 1, 12),
    _DvsStatusGreInDropped_Type()
)
dvsStatusGreInDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusGreInDropped.setStatus("current")
_DvsStatusGreOutDropped_Type = Integer32
_DvsStatusGreOutDropped_Object = MibTableColumn
dvsStatusGreOutDropped = _DvsStatusGreOutDropped_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1505, 1, 13),
    _DvsStatusGreOutDropped_Type()
)
dvsStatusGreOutDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusGreOutDropped.setStatus("current")
_DvsStatusDeadSession_Type = Boolean
_DvsStatusDeadSession_Object = MibTableColumn
dvsStatusDeadSession = _DvsStatusDeadSession_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1505, 1, 14),
    _DvsStatusDeadSession_Type()
)
dvsStatusDeadSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusDeadSession.setStatus("current")
_DvsStatusRemoteIPXNetwork_Type = Integer32
_DvsStatusRemoteIPXNetwork_Object = MibTableColumn
dvsStatusRemoteIPXNetwork = _DvsStatusRemoteIPXNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1505, 1, 15),
    _DvsStatusRemoteIPXNetwork_Type()
)
dvsStatusRemoteIPXNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusRemoteIPXNetwork.setStatus("current")


class _DvsStatusRemoteIPXNode_Type(DisplayString):
    """Custom type dvsStatusRemoteIPXNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DvsStatusRemoteIPXNode_Type.__name__ = "DisplayString"
_DvsStatusRemoteIPXNode_Object = MibTableColumn
dvsStatusRemoteIPXNode = _DvsStatusRemoteIPXNode_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1505, 1, 16),
    _DvsStatusRemoteIPXNode_Type()
)
dvsStatusRemoteIPXNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusRemoteIPXNode.setStatus("current")
_DvsStatusIPInPackets_Type = Integer32
_DvsStatusIPInPackets_Object = MibTableColumn
dvsStatusIPInPackets = _DvsStatusIPInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1505, 1, 17),
    _DvsStatusIPInPackets_Type()
)
dvsStatusIPInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusIPInPackets.setStatus("current")
_DvsStatusIPOutPackets_Type = Integer32
_DvsStatusIPOutPackets_Object = MibTableColumn
dvsStatusIPOutPackets = _DvsStatusIPOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1505, 1, 18),
    _DvsStatusIPOutPackets_Type()
)
dvsStatusIPOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusIPOutPackets.setStatus("current")
_DvsStatusIPXInPackets_Type = Integer32
_DvsStatusIPXInPackets_Object = MibTableColumn
dvsStatusIPXInPackets = _DvsStatusIPXInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1505, 1, 19),
    _DvsStatusIPXInPackets_Type()
)
dvsStatusIPXInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusIPXInPackets.setStatus("current")
_DvsStatusIPXOutPackets_Type = Integer32
_DvsStatusIPXOutPackets_Object = MibTableColumn
dvsStatusIPXOutPackets = _DvsStatusIPXOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1505, 1, 20),
    _DvsStatusIPXOutPackets_Type()
)
dvsStatusIPXOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusIPXOutPackets.setStatus("current")
_DvsLogEntryTable_Object = MibTable
dvsLogEntryTable = _DvsLogEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1506)
)
if mibBuilder.loadTexts:
    dvsLogEntryTable.setStatus("current")
_DvsLogEntryEntry_Object = MibTableRow
dvsLogEntryEntry = _DvsLogEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1506, 1)
)
dvsLogEntryEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "dvsLogEntryIndex"),
)
if mibBuilder.loadTexts:
    dvsLogEntryEntry.setStatus("current")
_DvsLogEntryIndex_Type = Integer32
_DvsLogEntryIndex_Object = MibTableColumn
dvsLogEntryIndex = _DvsLogEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1506, 1, 1),
    _DvsLogEntryIndex_Type()
)
dvsLogEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsLogEntryIndex.setStatus("current")
_DvsLogEntryMinIndex_Type = Integer32
_DvsLogEntryMinIndex_Object = MibTableColumn
dvsLogEntryMinIndex = _DvsLogEntryMinIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1506, 1, 2),
    _DvsLogEntryMinIndex_Type()
)
dvsLogEntryMinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsLogEntryMinIndex.setStatus("current")
_DvsLogEntryMaxIndex_Type = Integer32
_DvsLogEntryMaxIndex_Object = MibTableColumn
dvsLogEntryMaxIndex = _DvsLogEntryMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1506, 1, 3),
    _DvsLogEntryMaxIndex_Type()
)
dvsLogEntryMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsLogEntryMaxIndex.setStatus("current")


class _DvsLogEntryEntryText_Type(OctetString):
    """Custom type dvsLogEntryEntryText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_DvsLogEntryEntryText_Type.__name__ = "OctetString"
_DvsLogEntryEntryText_Object = MibTableColumn
dvsLogEntryEntryText = _DvsLogEntryEntryText_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1506, 1, 4),
    _DvsLogEntryEntryText_Type()
)
dvsLogEntryEntryText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsLogEntryEntryText.setStatus("current")
_DvsLogEntryTunnelCLID_Type = Integer32
_DvsLogEntryTunnelCLID_Object = MibTableColumn
dvsLogEntryTunnelCLID = _DvsLogEntryTunnelCLID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1506, 1, 5),
    _DvsLogEntryTunnelCLID_Type()
)
dvsLogEntryTunnelCLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsLogEntryTunnelCLID.setStatus("current")
_DvsLogEntryUpTime_Type = Integer32
_DvsLogEntryUpTime_Object = MibTableColumn
dvsLogEntryUpTime = _DvsLogEntryUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1506, 1, 6),
    _DvsLogEntryUpTime_Type()
)
dvsLogEntryUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsLogEntryUpTime.setStatus("current")
_L2TPTunnelStatusActiveTable_Object = MibTable
l2TPTunnelStatusActiveTable = _L2TPTunnelStatusActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1507)
)
if mibBuilder.loadTexts:
    l2TPTunnelStatusActiveTable.setStatus("current")
_L2TPTunnelStatusActiveEntry_Object = MibTableRow
l2TPTunnelStatusActiveEntry = _L2TPTunnelStatusActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1507, 1)
)
l2TPTunnelStatusActiveEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "l2TPTunnelStatusActiveLocalID"),
)
if mibBuilder.loadTexts:
    l2TPTunnelStatusActiveEntry.setStatus("current")
_L2TPTunnelStatusActiveSlot_Type = Integer32
_L2TPTunnelStatusActiveSlot_Object = MibTableColumn
l2TPTunnelStatusActiveSlot = _L2TPTunnelStatusActiveSlot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1507, 1, 1),
    _L2TPTunnelStatusActiveSlot_Type()
)
l2TPTunnelStatusActiveSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusActiveSlot.setStatus("current")
_L2TPTunnelStatusActiveLocalID_Type = Integer32
_L2TPTunnelStatusActiveLocalID_Object = MibTableColumn
l2TPTunnelStatusActiveLocalID = _L2TPTunnelStatusActiveLocalID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1507, 1, 2),
    _L2TPTunnelStatusActiveLocalID_Type()
)
l2TPTunnelStatusActiveLocalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusActiveLocalID.setStatus("current")
_L2TPTunnelStatusActiveRemoteID_Type = Integer32
_L2TPTunnelStatusActiveRemoteID_Object = MibTableColumn
l2TPTunnelStatusActiveRemoteID = _L2TPTunnelStatusActiveRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1507, 1, 3),
    _L2TPTunnelStatusActiveRemoteID_Type()
)
l2TPTunnelStatusActiveRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusActiveRemoteID.setStatus("current")
_L2TPTunnelStatusActiveLocalAddress_Type = IpAddress
_L2TPTunnelStatusActiveLocalAddress_Object = MibTableColumn
l2TPTunnelStatusActiveLocalAddress = _L2TPTunnelStatusActiveLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1507, 1, 4),
    _L2TPTunnelStatusActiveLocalAddress_Type()
)
l2TPTunnelStatusActiveLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusActiveLocalAddress.setStatus("current")
_L2TPTunnelStatusActiveRemoteAddress_Type = IpAddress
_L2TPTunnelStatusActiveRemoteAddress_Object = MibTableColumn
l2TPTunnelStatusActiveRemoteAddress = _L2TPTunnelStatusActiveRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1507, 1, 5),
    _L2TPTunnelStatusActiveRemoteAddress_Type()
)
l2TPTunnelStatusActiveRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusActiveRemoteAddress.setStatus("current")


class _L2TPTunnelStatusActiveState_Type(Integer32):
    """Custom type l2TPTunnelStatusActiveState based on Integer32"""
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
        *(("closed", 4),
          ("established", 3),
          ("idle", 0),
          ("waitCtrlConn", 2),
          ("waitCtrlReply", 1))
    )


_L2TPTunnelStatusActiveState_Type.__name__ = "Integer32"
_L2TPTunnelStatusActiveState_Object = MibTableColumn
l2TPTunnelStatusActiveState = _L2TPTunnelStatusActiveState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1507, 1, 6),
    _L2TPTunnelStatusActiveState_Type()
)
l2TPTunnelStatusActiveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusActiveState.setStatus("current")
_L2TPTunnelStatusActiveUpTime_Type = Integer32
_L2TPTunnelStatusActiveUpTime_Object = MibTableColumn
l2TPTunnelStatusActiveUpTime = _L2TPTunnelStatusActiveUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1507, 1, 7),
    _L2TPTunnelStatusActiveUpTime_Type()
)
l2TPTunnelStatusActiveUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusActiveUpTime.setStatus("current")
_L2TPTunnelStatusActiveActiveLinks_Type = Integer32
_L2TPTunnelStatusActiveActiveLinks_Object = MibTableColumn
l2TPTunnelStatusActiveActiveLinks = _L2TPTunnelStatusActiveActiveLinks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1507, 1, 8),
    _L2TPTunnelStatusActiveActiveLinks_Type()
)
l2TPTunnelStatusActiveActiveLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusActiveActiveLinks.setStatus("current")
_L2TPTunnelStatusActiveMaxActiveLinks_Type = Integer32
_L2TPTunnelStatusActiveMaxActiveLinks_Object = MibTableColumn
l2TPTunnelStatusActiveMaxActiveLinks = _L2TPTunnelStatusActiveMaxActiveLinks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1507, 1, 9),
    _L2TPTunnelStatusActiveMaxActiveLinks_Type()
)
l2TPTunnelStatusActiveMaxActiveLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusActiveMaxActiveLinks.setStatus("current")
_L2TPTunnelStatusActivePendingLinks_Type = Integer32
_L2TPTunnelStatusActivePendingLinks_Object = MibTableColumn
l2TPTunnelStatusActivePendingLinks = _L2TPTunnelStatusActivePendingLinks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1507, 1, 10),
    _L2TPTunnelStatusActivePendingLinks_Type()
)
l2TPTunnelStatusActivePendingLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusActivePendingLinks.setStatus("current")
_L2TPTunnelStatusActiveLinksAdded_Type = Integer32
_L2TPTunnelStatusActiveLinksAdded_Object = MibTableColumn
l2TPTunnelStatusActiveLinksAdded = _L2TPTunnelStatusActiveLinksAdded_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1507, 1, 11),
    _L2TPTunnelStatusActiveLinksAdded_Type()
)
l2TPTunnelStatusActiveLinksAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusActiveLinksAdded.setStatus("current")
_L2TPTunnelStatusActiveLinksAddedSuccessfully_Type = Integer32
_L2TPTunnelStatusActiveLinksAddedSuccessfully_Object = MibTableColumn
l2TPTunnelStatusActiveLinksAddedSuccessfully = _L2TPTunnelStatusActiveLinksAddedSuccessfully_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1507, 1, 12),
    _L2TPTunnelStatusActiveLinksAddedSuccessfully_Type()
)
l2TPTunnelStatusActiveLinksAddedSuccessfully.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusActiveLinksAddedSuccessfully.setStatus("current")
_L2TPTunnelStatusActiveLinksAddedUnsuccessfully_Type = Integer32
_L2TPTunnelStatusActiveLinksAddedUnsuccessfully_Object = MibTableColumn
l2TPTunnelStatusActiveLinksAddedUnsuccessfully = _L2TPTunnelStatusActiveLinksAddedUnsuccessfully_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1507, 1, 13),
    _L2TPTunnelStatusActiveLinksAddedUnsuccessfully_Type()
)
l2TPTunnelStatusActiveLinksAddedUnsuccessfully.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusActiveLinksAddedUnsuccessfully.setStatus("current")
_L2TPTunnelStatusActiveLinksRemoved_Type = Integer32
_L2TPTunnelStatusActiveLinksRemoved_Object = MibTableColumn
l2TPTunnelStatusActiveLinksRemoved = _L2TPTunnelStatusActiveLinksRemoved_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1507, 1, 14),
    _L2TPTunnelStatusActiveLinksRemoved_Type()
)
l2TPTunnelStatusActiveLinksRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusActiveLinksRemoved.setStatus("current")
_L2TPTunnelStatusActiveGotOpened_Type = Boolean
_L2TPTunnelStatusActiveGotOpened_Object = MibTableColumn
l2TPTunnelStatusActiveGotOpened = _L2TPTunnelStatusActiveGotOpened_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1507, 1, 15),
    _L2TPTunnelStatusActiveGotOpened_Type()
)
l2TPTunnelStatusActiveGotOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusActiveGotOpened.setStatus("current")
_L2TPTunnelStatusActiveVPOP_Type = Integer32
_L2TPTunnelStatusActiveVPOP_Object = MibTableColumn
l2TPTunnelStatusActiveVPOP = _L2TPTunnelStatusActiveVPOP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1507, 1, 16),
    _L2TPTunnelStatusActiveVPOP_Type()
)
l2TPTunnelStatusActiveVPOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusActiveVPOP.setStatus("current")
_L2TPTunnelStatusActiveL2TPTermationCause_Type = Integer32
_L2TPTunnelStatusActiveL2TPTermationCause_Object = MibTableColumn
l2TPTunnelStatusActiveL2TPTermationCause = _L2TPTunnelStatusActiveL2TPTermationCause_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1507, 1, 17),
    _L2TPTunnelStatusActiveL2TPTermationCause_Type()
)
l2TPTunnelStatusActiveL2TPTermationCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusActiveL2TPTermationCause.setStatus("current")
_L2TPTunnelStatusInactiveTable_Object = MibTable
l2TPTunnelStatusInactiveTable = _L2TPTunnelStatusInactiveTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1508)
)
if mibBuilder.loadTexts:
    l2TPTunnelStatusInactiveTable.setStatus("current")
_L2TPTunnelStatusInactiveEntry_Object = MibTableRow
l2TPTunnelStatusInactiveEntry = _L2TPTunnelStatusInactiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1508, 1)
)
l2TPTunnelStatusInactiveEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "l2TPTunnelStatusInactiveLocalID"),
)
if mibBuilder.loadTexts:
    l2TPTunnelStatusInactiveEntry.setStatus("current")
_L2TPTunnelStatusInactiveSlot_Type = Integer32
_L2TPTunnelStatusInactiveSlot_Object = MibTableColumn
l2TPTunnelStatusInactiveSlot = _L2TPTunnelStatusInactiveSlot_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1508, 1, 1),
    _L2TPTunnelStatusInactiveSlot_Type()
)
l2TPTunnelStatusInactiveSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusInactiveSlot.setStatus("current")
_L2TPTunnelStatusInactiveLocalID_Type = Integer32
_L2TPTunnelStatusInactiveLocalID_Object = MibTableColumn
l2TPTunnelStatusInactiveLocalID = _L2TPTunnelStatusInactiveLocalID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1508, 1, 2),
    _L2TPTunnelStatusInactiveLocalID_Type()
)
l2TPTunnelStatusInactiveLocalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusInactiveLocalID.setStatus("current")
_L2TPTunnelStatusInactiveRemoteID_Type = Integer32
_L2TPTunnelStatusInactiveRemoteID_Object = MibTableColumn
l2TPTunnelStatusInactiveRemoteID = _L2TPTunnelStatusInactiveRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1508, 1, 3),
    _L2TPTunnelStatusInactiveRemoteID_Type()
)
l2TPTunnelStatusInactiveRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusInactiveRemoteID.setStatus("current")
_L2TPTunnelStatusInactiveLocalAddress_Type = IpAddress
_L2TPTunnelStatusInactiveLocalAddress_Object = MibTableColumn
l2TPTunnelStatusInactiveLocalAddress = _L2TPTunnelStatusInactiveLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1508, 1, 4),
    _L2TPTunnelStatusInactiveLocalAddress_Type()
)
l2TPTunnelStatusInactiveLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusInactiveLocalAddress.setStatus("current")
_L2TPTunnelStatusInactiveRemoteAddress_Type = IpAddress
_L2TPTunnelStatusInactiveRemoteAddress_Object = MibTableColumn
l2TPTunnelStatusInactiveRemoteAddress = _L2TPTunnelStatusInactiveRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1508, 1, 5),
    _L2TPTunnelStatusInactiveRemoteAddress_Type()
)
l2TPTunnelStatusInactiveRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusInactiveRemoteAddress.setStatus("current")


class _L2TPTunnelStatusInactiveState_Type(Integer32):
    """Custom type l2TPTunnelStatusInactiveState based on Integer32"""
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
        *(("closed", 4),
          ("established", 3),
          ("idle", 0),
          ("waitCtrlConn", 2),
          ("waitCtrlReply", 1))
    )


_L2TPTunnelStatusInactiveState_Type.__name__ = "Integer32"
_L2TPTunnelStatusInactiveState_Object = MibTableColumn
l2TPTunnelStatusInactiveState = _L2TPTunnelStatusInactiveState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1508, 1, 6),
    _L2TPTunnelStatusInactiveState_Type()
)
l2TPTunnelStatusInactiveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusInactiveState.setStatus("current")
_L2TPTunnelStatusInactiveUpTime_Type = Integer32
_L2TPTunnelStatusInactiveUpTime_Object = MibTableColumn
l2TPTunnelStatusInactiveUpTime = _L2TPTunnelStatusInactiveUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1508, 1, 7),
    _L2TPTunnelStatusInactiveUpTime_Type()
)
l2TPTunnelStatusInactiveUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusInactiveUpTime.setStatus("current")
_L2TPTunnelStatusInactiveActiveLinks_Type = Integer32
_L2TPTunnelStatusInactiveActiveLinks_Object = MibTableColumn
l2TPTunnelStatusInactiveActiveLinks = _L2TPTunnelStatusInactiveActiveLinks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1508, 1, 8),
    _L2TPTunnelStatusInactiveActiveLinks_Type()
)
l2TPTunnelStatusInactiveActiveLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusInactiveActiveLinks.setStatus("current")
_L2TPTunnelStatusInactiveMaxActiveLinks_Type = Integer32
_L2TPTunnelStatusInactiveMaxActiveLinks_Object = MibTableColumn
l2TPTunnelStatusInactiveMaxActiveLinks = _L2TPTunnelStatusInactiveMaxActiveLinks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1508, 1, 9),
    _L2TPTunnelStatusInactiveMaxActiveLinks_Type()
)
l2TPTunnelStatusInactiveMaxActiveLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusInactiveMaxActiveLinks.setStatus("current")
_L2TPTunnelStatusInactivePendingLinks_Type = Integer32
_L2TPTunnelStatusInactivePendingLinks_Object = MibTableColumn
l2TPTunnelStatusInactivePendingLinks = _L2TPTunnelStatusInactivePendingLinks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1508, 1, 10),
    _L2TPTunnelStatusInactivePendingLinks_Type()
)
l2TPTunnelStatusInactivePendingLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusInactivePendingLinks.setStatus("current")
_L2TPTunnelStatusInactiveLinksAdded_Type = Integer32
_L2TPTunnelStatusInactiveLinksAdded_Object = MibTableColumn
l2TPTunnelStatusInactiveLinksAdded = _L2TPTunnelStatusInactiveLinksAdded_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1508, 1, 11),
    _L2TPTunnelStatusInactiveLinksAdded_Type()
)
l2TPTunnelStatusInactiveLinksAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusInactiveLinksAdded.setStatus("current")
_L2TPTunnelStatusInactiveLinksAddedSuccessfully_Type = Integer32
_L2TPTunnelStatusInactiveLinksAddedSuccessfully_Object = MibTableColumn
l2TPTunnelStatusInactiveLinksAddedSuccessfully = _L2TPTunnelStatusInactiveLinksAddedSuccessfully_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1508, 1, 12),
    _L2TPTunnelStatusInactiveLinksAddedSuccessfully_Type()
)
l2TPTunnelStatusInactiveLinksAddedSuccessfully.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusInactiveLinksAddedSuccessfully.setStatus("current")
_L2TPTunnelStatusInactiveLinksAddedUnsuccessfully_Type = Integer32
_L2TPTunnelStatusInactiveLinksAddedUnsuccessfully_Object = MibTableColumn
l2TPTunnelStatusInactiveLinksAddedUnsuccessfully = _L2TPTunnelStatusInactiveLinksAddedUnsuccessfully_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1508, 1, 13),
    _L2TPTunnelStatusInactiveLinksAddedUnsuccessfully_Type()
)
l2TPTunnelStatusInactiveLinksAddedUnsuccessfully.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusInactiveLinksAddedUnsuccessfully.setStatus("current")
_L2TPTunnelStatusInactiveLinksRemoved_Type = Integer32
_L2TPTunnelStatusInactiveLinksRemoved_Object = MibTableColumn
l2TPTunnelStatusInactiveLinksRemoved = _L2TPTunnelStatusInactiveLinksRemoved_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1508, 1, 14),
    _L2TPTunnelStatusInactiveLinksRemoved_Type()
)
l2TPTunnelStatusInactiveLinksRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusInactiveLinksRemoved.setStatus("current")
_L2TPTunnelStatusInactiveGotOpened_Type = Boolean
_L2TPTunnelStatusInactiveGotOpened_Object = MibTableColumn
l2TPTunnelStatusInactiveGotOpened = _L2TPTunnelStatusInactiveGotOpened_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1508, 1, 15),
    _L2TPTunnelStatusInactiveGotOpened_Type()
)
l2TPTunnelStatusInactiveGotOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusInactiveGotOpened.setStatus("current")
_L2TPTunnelStatusInactiveVPOP_Type = Integer32
_L2TPTunnelStatusInactiveVPOP_Object = MibTableColumn
l2TPTunnelStatusInactiveVPOP = _L2TPTunnelStatusInactiveVPOP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1508, 1, 16),
    _L2TPTunnelStatusInactiveVPOP_Type()
)
l2TPTunnelStatusInactiveVPOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusInactiveVPOP.setStatus("current")
_L2TPTunnelStatusInactiveL2TPTermationCause_Type = Integer32
_L2TPTunnelStatusInactiveL2TPTermationCause_Object = MibTableColumn
l2TPTunnelStatusInactiveL2TPTermationCause = _L2TPTunnelStatusInactiveL2TPTermationCause_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1508, 1, 17),
    _L2TPTunnelStatusInactiveL2TPTermationCause_Type()
)
l2TPTunnelStatusInactiveL2TPTermationCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPTunnelStatusInactiveL2TPTermationCause.setStatus("current")
_L2TPLinkStatusTable_Object = MibTable
l2TPLinkStatusTable = _L2TPLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1509)
)
if mibBuilder.loadTexts:
    l2TPLinkStatusTable.setStatus("current")
_L2TPLinkStatusEntry_Object = MibTableRow
l2TPLinkStatusEntry = _L2TPLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1509, 1)
)
l2TPLinkStatusEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "l2TPLinkStatusLocalID"),
    (0, "APTIS-MONITOR-MIB", "l2TPLinkStatusIndex"),
)
if mibBuilder.loadTexts:
    l2TPLinkStatusEntry.setStatus("current")
_L2TPLinkStatusLocalID_Type = Integer32
_L2TPLinkStatusLocalID_Object = MibTableColumn
l2TPLinkStatusLocalID = _L2TPLinkStatusLocalID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1509, 1, 1),
    _L2TPLinkStatusLocalID_Type()
)
l2TPLinkStatusLocalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPLinkStatusLocalID.setStatus("current")
_L2TPLinkStatusRemoteID_Type = Integer32
_L2TPLinkStatusRemoteID_Object = MibTableColumn
l2TPLinkStatusRemoteID = _L2TPLinkStatusRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1509, 1, 2),
    _L2TPLinkStatusRemoteID_Type()
)
l2TPLinkStatusRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPLinkStatusRemoteID.setStatus("current")
_L2TPLinkStatusIndex_Type = Integer32
_L2TPLinkStatusIndex_Object = MibTableColumn
l2TPLinkStatusIndex = _L2TPLinkStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1509, 1, 3),
    _L2TPLinkStatusIndex_Type()
)
l2TPLinkStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPLinkStatusIndex.setStatus("current")
_L2TPLinkStatusSessionID_Type = Integer32
_L2TPLinkStatusSessionID_Object = MibTableColumn
l2TPLinkStatusSessionID = _L2TPLinkStatusSessionID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1509, 1, 4),
    _L2TPLinkStatusSessionID_Type()
)
l2TPLinkStatusSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPLinkStatusSessionID.setStatus("current")
_L2TPLinkStatusVPOP_Type = Integer32
_L2TPLinkStatusVPOP_Object = MibTableColumn
l2TPLinkStatusVPOP = _L2TPLinkStatusVPOP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1509, 1, 5),
    _L2TPLinkStatusVPOP_Type()
)
l2TPLinkStatusVPOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPLinkStatusVPOP.setStatus("current")


class _L2TPLinkStatusState_Type(Integer32):
    """Custom type l2TPLinkStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 3),
          ("connected", 2),
          ("idle", 0),
          ("waitReply", 1))
    )


_L2TPLinkStatusState_Type.__name__ = "Integer32"
_L2TPLinkStatusState_Object = MibTableColumn
l2TPLinkStatusState = _L2TPLinkStatusState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1509, 1, 11),
    _L2TPLinkStatusState_Type()
)
l2TPLinkStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPLinkStatusState.setStatus("current")
_L2TPLinkStatusUpTime_Type = Integer32
_L2TPLinkStatusUpTime_Object = MibTableColumn
l2TPLinkStatusUpTime = _L2TPLinkStatusUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1509, 1, 12),
    _L2TPLinkStatusUpTime_Type()
)
l2TPLinkStatusUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPLinkStatusUpTime.setStatus("current")


class _L2TPLinkStatusUserName_Type(DisplayString):
    """Custom type l2TPLinkStatusUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_L2TPLinkStatusUserName_Type.__name__ = "DisplayString"
_L2TPLinkStatusUserName_Object = MibTableColumn
l2TPLinkStatusUserName = _L2TPLinkStatusUserName_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1509, 1, 13),
    _L2TPLinkStatusUserName_Type()
)
l2TPLinkStatusUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPLinkStatusUserName.setStatus("current")
_L2TPLinkStatusTxPackets_Type = Integer32
_L2TPLinkStatusTxPackets_Object = MibTableColumn
l2TPLinkStatusTxPackets = _L2TPLinkStatusTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1509, 1, 21),
    _L2TPLinkStatusTxPackets_Type()
)
l2TPLinkStatusTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPLinkStatusTxPackets.setStatus("current")
_L2TPLinkStatusTxBytes_Type = Integer32
_L2TPLinkStatusTxBytes_Object = MibTableColumn
l2TPLinkStatusTxBytes = _L2TPLinkStatusTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1509, 1, 22),
    _L2TPLinkStatusTxBytes_Type()
)
l2TPLinkStatusTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPLinkStatusTxBytes.setStatus("current")
_L2TPLinkStatusRxPackets_Type = Integer32
_L2TPLinkStatusRxPackets_Object = MibTableColumn
l2TPLinkStatusRxPackets = _L2TPLinkStatusRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1509, 1, 23),
    _L2TPLinkStatusRxPackets_Type()
)
l2TPLinkStatusRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPLinkStatusRxPackets.setStatus("current")
_L2TPLinkStatusRxBytes_Type = Integer32
_L2TPLinkStatusRxBytes_Object = MibTableColumn
l2TPLinkStatusRxBytes = _L2TPLinkStatusRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1509, 1, 24),
    _L2TPLinkStatusRxBytes_Type()
)
l2TPLinkStatusRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPLinkStatusRxBytes.setStatus("current")
_L2TPLinkStatusL2TPTermationCause_Type = Integer32
_L2TPLinkStatusL2TPTermationCause_Object = MibTableColumn
l2TPLinkStatusL2TPTermationCause = _L2TPLinkStatusL2TPTermationCause_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1509, 1, 31),
    _L2TPLinkStatusL2TPTermationCause_Type()
)
l2TPLinkStatusL2TPTermationCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPLinkStatusL2TPTermationCause.setStatus("current")
_L2TPLogEntryTable_Object = MibTable
l2TPLogEntryTable = _L2TPLogEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1510)
)
if mibBuilder.loadTexts:
    l2TPLogEntryTable.setStatus("current")
_L2TPLogEntryEntry_Object = MibTableRow
l2TPLogEntryEntry = _L2TPLogEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1510, 1)
)
l2TPLogEntryEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "l2TPLogEntryLocalID"),
    (0, "APTIS-MONITOR-MIB", "l2TPLogEntryIndex"),
)
if mibBuilder.loadTexts:
    l2TPLogEntryEntry.setStatus("current")
_L2TPLogEntryLocalID_Type = Integer32
_L2TPLogEntryLocalID_Object = MibTableColumn
l2TPLogEntryLocalID = _L2TPLogEntryLocalID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1510, 1, 1),
    _L2TPLogEntryLocalID_Type()
)
l2TPLogEntryLocalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPLogEntryLocalID.setStatus("current")
_L2TPLogEntryIndex_Type = Integer32
_L2TPLogEntryIndex_Object = MibTableColumn
l2TPLogEntryIndex = _L2TPLogEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1510, 1, 2),
    _L2TPLogEntryIndex_Type()
)
l2TPLogEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPLogEntryIndex.setStatus("current")
_L2TPLogEntryMinIndex_Type = Integer32
_L2TPLogEntryMinIndex_Object = MibTableColumn
l2TPLogEntryMinIndex = _L2TPLogEntryMinIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1510, 1, 11),
    _L2TPLogEntryMinIndex_Type()
)
l2TPLogEntryMinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPLogEntryMinIndex.setStatus("current")
_L2TPLogEntryMaxIndex_Type = Integer32
_L2TPLogEntryMaxIndex_Object = MibTableColumn
l2TPLogEntryMaxIndex = _L2TPLogEntryMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1510, 1, 12),
    _L2TPLogEntryMaxIndex_Type()
)
l2TPLogEntryMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPLogEntryMaxIndex.setStatus("current")
_L2TPLogEntryUpTime_Type = Integer32
_L2TPLogEntryUpTime_Object = MibTableColumn
l2TPLogEntryUpTime = _L2TPLogEntryUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1510, 1, 13),
    _L2TPLogEntryUpTime_Type()
)
l2TPLogEntryUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPLogEntryUpTime.setStatus("current")


class _L2TPLogEntryEntryText_Type(OctetString):
    """Custom type l2TPLogEntryEntryText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_L2TPLogEntryEntryText_Type.__name__ = "OctetString"
_L2TPLogEntryEntryText_Object = MibTableColumn
l2TPLogEntryEntryText = _L2TPLogEntryEntryText_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1510, 1, 21),
    _L2TPLogEntryEntryText_Type()
)
l2TPLogEntryEntryText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TPLogEntryEntryText.setStatus("current")
_DvsDeadLogEntryTable_Object = MibTable
dvsDeadLogEntryTable = _DvsDeadLogEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1520)
)
if mibBuilder.loadTexts:
    dvsDeadLogEntryTable.setStatus("current")
_DvsDeadLogEntryEntry_Object = MibTableRow
dvsDeadLogEntryEntry = _DvsDeadLogEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1520, 1)
)
dvsDeadLogEntryEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "dvsDeadLogEntryIndex"),
)
if mibBuilder.loadTexts:
    dvsDeadLogEntryEntry.setStatus("current")
_DvsDeadLogEntryIndex_Type = Integer32
_DvsDeadLogEntryIndex_Object = MibTableColumn
dvsDeadLogEntryIndex = _DvsDeadLogEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1520, 1, 1),
    _DvsDeadLogEntryIndex_Type()
)
dvsDeadLogEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsDeadLogEntryIndex.setStatus("current")
_DvsDeadLogEntryMinIndex_Type = Integer32
_DvsDeadLogEntryMinIndex_Object = MibTableColumn
dvsDeadLogEntryMinIndex = _DvsDeadLogEntryMinIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1520, 1, 2),
    _DvsDeadLogEntryMinIndex_Type()
)
dvsDeadLogEntryMinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsDeadLogEntryMinIndex.setStatus("current")
_DvsDeadLogEntryMaxIndex_Type = Integer32
_DvsDeadLogEntryMaxIndex_Object = MibTableColumn
dvsDeadLogEntryMaxIndex = _DvsDeadLogEntryMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1520, 1, 3),
    _DvsDeadLogEntryMaxIndex_Type()
)
dvsDeadLogEntryMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsDeadLogEntryMaxIndex.setStatus("current")


class _DvsDeadLogEntryEntryText_Type(OctetString):
    """Custom type dvsDeadLogEntryEntryText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_DvsDeadLogEntryEntryText_Type.__name__ = "OctetString"
_DvsDeadLogEntryEntryText_Object = MibTableColumn
dvsDeadLogEntryEntryText = _DvsDeadLogEntryEntryText_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1520, 1, 4),
    _DvsDeadLogEntryEntryText_Type()
)
dvsDeadLogEntryEntryText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsDeadLogEntryEntryText.setStatus("current")
_DvsDeadLogEntryTunnelCLID_Type = Integer32
_DvsDeadLogEntryTunnelCLID_Object = MibTableColumn
dvsDeadLogEntryTunnelCLID = _DvsDeadLogEntryTunnelCLID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1520, 1, 5),
    _DvsDeadLogEntryTunnelCLID_Type()
)
dvsDeadLogEntryTunnelCLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsDeadLogEntryTunnelCLID.setStatus("current")
_DvsDeadLogEntryUpTime_Type = Integer32
_DvsDeadLogEntryUpTime_Object = MibTableColumn
dvsDeadLogEntryUpTime = _DvsDeadLogEntryUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1520, 1, 6),
    _DvsDeadLogEntryUpTime_Type()
)
dvsDeadLogEntryUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsDeadLogEntryUpTime.setStatus("current")
_DvsStatusDeadTable_Object = MibTable
dvsStatusDeadTable = _DvsStatusDeadTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1521)
)
if mibBuilder.loadTexts:
    dvsStatusDeadTable.setStatus("current")
_DvsStatusDeadEntry_Object = MibTableRow
dvsStatusDeadEntry = _DvsStatusDeadEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1521, 1)
)
dvsStatusDeadEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "dvsStatusDeadTunnelCLID"),
)
if mibBuilder.loadTexts:
    dvsStatusDeadEntry.setStatus("current")
_DvsStatusDeadTunnelCLID_Type = Integer32
_DvsStatusDeadTunnelCLID_Object = MibTableColumn
dvsStatusDeadTunnelCLID = _DvsStatusDeadTunnelCLID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1521, 1, 1),
    _DvsStatusDeadTunnelCLID_Type()
)
dvsStatusDeadTunnelCLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusDeadTunnelCLID.setStatus("current")
_DvsStatusDeadRemoteCLID_Type = Integer32
_DvsStatusDeadRemoteCLID_Object = MibTableColumn
dvsStatusDeadRemoteCLID = _DvsStatusDeadRemoteCLID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1521, 1, 2),
    _DvsStatusDeadRemoteCLID_Type()
)
dvsStatusDeadRemoteCLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusDeadRemoteCLID.setStatus("current")
_DvsStatusDeadRemoteAddress_Type = IpAddress
_DvsStatusDeadRemoteAddress_Object = MibTableColumn
dvsStatusDeadRemoteAddress = _DvsStatusDeadRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1521, 1, 3),
    _DvsStatusDeadRemoteAddress_Type()
)
dvsStatusDeadRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusDeadRemoteAddress.setStatus("current")


class _DvsStatusDeadTunnelState_Type(Integer32):
    """Custom type dvsStatusDeadTunnelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("aUTHREPLY", 2),
          ("aWGWCFG", 1),
          ("dHCP", 5),
          ("dISC", 8),
          ("iDLE", 0),
          ("mIP", 6),
          ("mODPPPCFG", 4),
          ("oPEN", 7),
          ("pRIMGWTO", 3))
    )


_DvsStatusDeadTunnelState_Type.__name__ = "Integer32"
_DvsStatusDeadTunnelState_Object = MibTableColumn
dvsStatusDeadTunnelState = _DvsStatusDeadTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1521, 1, 4),
    _DvsStatusDeadTunnelState_Type()
)
dvsStatusDeadTunnelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusDeadTunnelState.setStatus("current")
_DvsStatusDeadUpTime_Type = Integer32
_DvsStatusDeadUpTime_Object = MibTableColumn
dvsStatusDeadUpTime = _DvsStatusDeadUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1521, 1, 5),
    _DvsStatusDeadUpTime_Type()
)
dvsStatusDeadUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusDeadUpTime.setStatus("current")
_DvsStatusDeadMacSlotNumber_Type = Integer32
_DvsStatusDeadMacSlotNumber_Object = MibTableColumn
dvsStatusDeadMacSlotNumber = _DvsStatusDeadMacSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1521, 1, 6),
    _DvsStatusDeadMacSlotNumber_Type()
)
dvsStatusDeadMacSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusDeadMacSlotNumber.setStatus("current")
_DvsStatusDeadVPOP_Type = Integer32
_DvsStatusDeadVPOP_Object = MibTableColumn
dvsStatusDeadVPOP = _DvsStatusDeadVPOP_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1521, 1, 7),
    _DvsStatusDeadVPOP_Type()
)
dvsStatusDeadVPOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusDeadVPOP.setStatus("current")
_DvsStatusDeadGreInPackets_Type = Integer32
_DvsStatusDeadGreInPackets_Object = MibTableColumn
dvsStatusDeadGreInPackets = _DvsStatusDeadGreInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1521, 1, 8),
    _DvsStatusDeadGreInPackets_Type()
)
dvsStatusDeadGreInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusDeadGreInPackets.setStatus("current")
_DvsStatusDeadGreOutPackets_Type = Integer32
_DvsStatusDeadGreOutPackets_Object = MibTableColumn
dvsStatusDeadGreOutPackets = _DvsStatusDeadGreOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1521, 1, 9),
    _DvsStatusDeadGreOutPackets_Type()
)
dvsStatusDeadGreOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusDeadGreOutPackets.setStatus("current")
_DvsStatusDeadGreChecksumError_Type = Integer32
_DvsStatusDeadGreChecksumError_Object = MibTableColumn
dvsStatusDeadGreChecksumError = _DvsStatusDeadGreChecksumError_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1521, 1, 10),
    _DvsStatusDeadGreChecksumError_Type()
)
dvsStatusDeadGreChecksumError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusDeadGreChecksumError.setStatus("current")
_DvsStatusDeadGreInDropped_Type = Integer32
_DvsStatusDeadGreInDropped_Object = MibTableColumn
dvsStatusDeadGreInDropped = _DvsStatusDeadGreInDropped_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1521, 1, 11),
    _DvsStatusDeadGreInDropped_Type()
)
dvsStatusDeadGreInDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusDeadGreInDropped.setStatus("current")
_DvsStatusDeadGreOutDropped_Type = Integer32
_DvsStatusDeadGreOutDropped_Object = MibTableColumn
dvsStatusDeadGreOutDropped = _DvsStatusDeadGreOutDropped_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1521, 1, 12),
    _DvsStatusDeadGreOutDropped_Type()
)
dvsStatusDeadGreOutDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusDeadGreOutDropped.setStatus("current")
_DvsStatusDeadDeadSession_Type = Boolean
_DvsStatusDeadDeadSession_Object = MibTableColumn
dvsStatusDeadDeadSession = _DvsStatusDeadDeadSession_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1521, 1, 13),
    _DvsStatusDeadDeadSession_Type()
)
dvsStatusDeadDeadSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvsStatusDeadDeadSession.setStatus("current")
_IpsecCountersTable_Object = MibTable
ipsecCountersTable = _IpsecCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1612)
)
if mibBuilder.loadTexts:
    ipsecCountersTable.setStatus("current")
_IpsecCountersEntry_Object = MibTableRow
ipsecCountersEntry = _IpsecCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1612, 1)
)
ipsecCountersEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "ipsecCountersOutboundCounter"),
)
if mibBuilder.loadTexts:
    ipsecCountersEntry.setStatus("current")
_IpsecCountersOutboundCounter_Type = Integer32
_IpsecCountersOutboundCounter_Object = MibTableColumn
ipsecCountersOutboundCounter = _IpsecCountersOutboundCounter_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1612, 1, 1),
    _IpsecCountersOutboundCounter_Type()
)
ipsecCountersOutboundCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecCountersOutboundCounter.setStatus("current")
_IpsecCountersInboundCounter_Type = Integer32
_IpsecCountersInboundCounter_Object = MibTableColumn
ipsecCountersInboundCounter = _IpsecCountersInboundCounter_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1612, 1, 2),
    _IpsecCountersInboundCounter_Type()
)
ipsecCountersInboundCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecCountersInboundCounter.setStatus("current")
_IpsecCountersOutboundDropCounter_Type = Integer32
_IpsecCountersOutboundDropCounter_Object = MibTableColumn
ipsecCountersOutboundDropCounter = _IpsecCountersOutboundDropCounter_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1612, 1, 3),
    _IpsecCountersOutboundDropCounter_Type()
)
ipsecCountersOutboundDropCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecCountersOutboundDropCounter.setStatus("current")
_IpsecCountersInboundDropCounter_Type = Integer32
_IpsecCountersInboundDropCounter_Object = MibTableColumn
ipsecCountersInboundDropCounter = _IpsecCountersInboundDropCounter_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 1612, 1, 4),
    _IpsecCountersInboundDropCounter_Type()
)
ipsecCountersInboundDropCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecCountersInboundDropCounter.setStatus("current")
_DacStatusTable_Object = MibTable
dacStatusTable = _DacStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2002)
)
if mibBuilder.loadTexts:
    dacStatusTable.setStatus("current")
_DacStatusEntry_Object = MibTableRow
dacStatusEntry = _DacStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2002, 1)
)
dacStatusEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "dacStatusClockSourcePrimary"),
)
if mibBuilder.loadTexts:
    dacStatusEntry.setStatus("current")
_DacStatusClockSourcePrimary_Type = Integer32
_DacStatusClockSourcePrimary_Object = MibTableColumn
dacStatusClockSourcePrimary = _DacStatusClockSourcePrimary_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2002, 1, 1),
    _DacStatusClockSourcePrimary_Type()
)
dacStatusClockSourcePrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dacStatusClockSourcePrimary.setStatus("current")
_DacStatusClockSourceSecondary_Type = Integer32
_DacStatusClockSourceSecondary_Object = MibTableColumn
dacStatusClockSourceSecondary = _DacStatusClockSourceSecondary_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2002, 1, 2),
    _DacStatusClockSourceSecondary_Type()
)
dacStatusClockSourceSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dacStatusClockSourceSecondary.setStatus("current")


class _DacStatusLTMType_Type(Integer32):
    """Custom type dacStatusLTMType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              17)
        )
    )
    namedValues = NamedValues(
        *(("e1by12", 2),
          ("e1by24", 6),
          ("redundant", 17),
          ("t1by12", 1),
          ("t1by24", 5),
          ("t3by1", 3),
          ("t3by2", 4),
          ("t3by4", 7))
    )


_DacStatusLTMType_Type.__name__ = "Integer32"
_DacStatusLTMType_Object = MibTableColumn
dacStatusLTMType = _DacStatusLTMType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2002, 1, 3),
    _DacStatusLTMType_Type()
)
dacStatusLTMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dacStatusLTMType.setStatus("current")
_DacTraceTable_Object = MibTable
dacTraceTable = _DacTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2003)
)
if mibBuilder.loadTexts:
    dacTraceTable.setStatus("current")
_DacTraceEntry_Object = MibTableRow
dacTraceEntry = _DacTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2003, 1)
)
dacTraceEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "dacTraceIndex"),
)
if mibBuilder.loadTexts:
    dacTraceEntry.setStatus("current")
_DacTraceIndex_Type = Integer32
_DacTraceIndex_Object = MibTableColumn
dacTraceIndex = _DacTraceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2003, 1, 1),
    _DacTraceIndex_Type()
)
dacTraceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dacTraceIndex.setStatus("current")


class _DacTraceLocation_Type(Integer32):
    """Custom type dacTraceLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("hDLC", 3),
          ("sM", 1),
          ("tN", 2),
          ("uSFSM", 4))
    )


_DacTraceLocation_Type.__name__ = "Integer32"
_DacTraceLocation_Object = MibTableColumn
dacTraceLocation = _DacTraceLocation_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2003, 1, 2),
    _DacTraceLocation_Type()
)
dacTraceLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dacTraceLocation.setStatus("current")


class _DacTraceDirection_Type(Integer32):
    """Custom type dacTraceDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("receive", 2),
          ("transmit", 1))
    )


_DacTraceDirection_Type.__name__ = "Integer32"
_DacTraceDirection_Object = MibTableColumn
dacTraceDirection = _DacTraceDirection_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2003, 1, 3),
    _DacTraceDirection_Type()
)
dacTraceDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dacTraceDirection.setStatus("current")


class _DacTraceType_Type(Integer32):
    """Custom type dacTraceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("ccAlloc", 18),
          ("ccClear", 19),
          ("ccConnect", 16),
          ("ccDisconnect", 17),
          ("ccRestart", 20),
          ("ccSetup", 15),
          ("smAbort", 7),
          ("smActivated", 8),
          ("smConnect", 4),
          ("smConnected", 9),
          ("smCreate", 1),
          ("smDisconnect", 6),
          ("smDisconnected", 13),
          ("smLinkFailed", 12),
          ("smMove", 5),
          ("smMoved", 11),
          ("smReady", 10),
          ("smResource", 2),
          ("smResourceSet", 14),
          ("smSetup", 3),
          ("tnAlertingInd", 25),
          ("tnAlertingReq", 24),
          ("tnCallProcInd", 27),
          ("tnCallProcReq", 26),
          ("tnClearConf", 35),
          ("tnClearInd", 34),
          ("tnClearReq", 33),
          ("tnClearResp", 36),
          ("tnConnectConf", 30),
          ("tnConnectInd", 29),
          ("tnConnectReq", 28),
          ("tnDiscInd", 32),
          ("tnDiscReq", 31),
          ("tnSetupConf", 23),
          ("tnSetupInd", 21),
          ("tnSetupReq", 22),
          ("tnSetupResp", 37))
    )


_DacTraceType_Type.__name__ = "Integer32"
_DacTraceType_Object = MibTableColumn
dacTraceType = _DacTraceType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2003, 1, 4),
    _DacTraceType_Type()
)
dacTraceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dacTraceType.setStatus("current")
_DacTraceTimestamp_Type = Integer32
_DacTraceTimestamp_Object = MibTableColumn
dacTraceTimestamp = _DacTraceTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2003, 1, 5),
    _DacTraceTimestamp_Type()
)
dacTraceTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dacTraceTimestamp.setStatus("current")


class _DacTraceLen_Type(Integer32):
    """Custom type dacTraceLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_DacTraceLen_Type.__name__ = "Integer32"
_DacTraceLen_Object = MibTableColumn
dacTraceLen = _DacTraceLen_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2003, 1, 6),
    _DacTraceLen_Type()
)
dacTraceLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dacTraceLen.setStatus("current")


class _DacTraceData_Type(OctetString):
    """Custom type dacTraceData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 300),
    )


_DacTraceData_Type.__name__ = "OctetString"
_DacTraceData_Object = MibTableColumn
dacTraceData = _DacTraceData_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2003, 1, 7),
    _DacTraceData_Type()
)
dacTraceData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dacTraceData.setStatus("current")
_T3StatsTable_Object = MibTable
t3StatsTable = _T3StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2008)
)
if mibBuilder.loadTexts:
    t3StatsTable.setStatus("current")
_T3StatsEntry_Object = MibTableRow
t3StatsEntry = _T3StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2008, 1)
)
t3StatsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "t3StatsSlotIndex"),
    (0, "APTIS-MONITOR-MIB", "t3StatsLineNumber"),
)
if mibBuilder.loadTexts:
    t3StatsEntry.setStatus("current")


class _T3StatsLineState_Type(Integer32):
    """Custom type t3StatsLineState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bluealarm", 3),
          ("noalarm", 0),
          ("redalarm", 2),
          ("yellowalarm", 1))
    )


_T3StatsLineState_Type.__name__ = "Integer32"
_T3StatsLineState_Object = MibTableColumn
t3StatsLineState = _T3StatsLineState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2008, 1, 1),
    _T3StatsLineState_Type()
)
t3StatsLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3StatsLineState.setStatus("current")


class _T3StatsSlotIndex_Type(Integer32):
    """Custom type t3StatsSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_T3StatsSlotIndex_Type.__name__ = "Integer32"
_T3StatsSlotIndex_Object = MibTableColumn
t3StatsSlotIndex = _T3StatsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2008, 1, 2),
    _T3StatsSlotIndex_Type()
)
t3StatsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3StatsSlotIndex.setStatus("current")


class _T3StatsLineNumber_Type(Integer32):
    """Custom type t3StatsLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_T3StatsLineNumber_Type.__name__ = "Integer32"
_T3StatsLineNumber_Object = MibTableColumn
t3StatsLineNumber = _T3StatsLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2008, 1, 3),
    _T3StatsLineNumber_Type()
)
t3StatsLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3StatsLineNumber.setStatus("current")
_T3StatsRedundant_Type = Boolean
_T3StatsRedundant_Object = MibTableColumn
t3StatsRedundant = _T3StatsRedundant_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2008, 1, 4),
    _T3StatsRedundant_Type()
)
t3StatsRedundant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3StatsRedundant.setStatus("current")


class _T3StatsDs1Count_Type(Integer32):
    """Custom type t3StatsDs1Count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 56),
    )


_T3StatsDs1Count_Type.__name__ = "Integer32"
_T3StatsDs1Count_Object = MibTableColumn
t3StatsDs1Count = _T3StatsDs1Count_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2008, 1, 5),
    _T3StatsDs1Count_Type()
)
t3StatsDs1Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3StatsDs1Count.setStatus("current")


class _T3StatsActiveDs1Count_Type(Integer32):
    """Custom type t3StatsActiveDs1Count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 56),
    )


_T3StatsActiveDs1Count_Type.__name__ = "Integer32"
_T3StatsActiveDs1Count_Object = MibTableColumn
t3StatsActiveDs1Count = _T3StatsActiveDs1Count_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2008, 1, 6),
    _T3StatsActiveDs1Count_Type()
)
t3StatsActiveDs1Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3StatsActiveDs1Count.setStatus("current")
_T3StatsExternalClockPort_Type = Boolean
_T3StatsExternalClockPort_Object = MibTableColumn
t3StatsExternalClockPort = _T3StatsExternalClockPort_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2008, 1, 7),
    _T3StatsExternalClockPort_Type()
)
t3StatsExternalClockPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3StatsExternalClockPort.setStatus("current")
_DacClockingTable_Object = MibTable
dacClockingTable = _DacClockingTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2050)
)
if mibBuilder.loadTexts:
    dacClockingTable.setStatus("current")
_DacClockingEntry_Object = MibTableRow
dacClockingEntry = _DacClockingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2050, 1)
)
dacClockingEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "dacClockingIndex"),
)
if mibBuilder.loadTexts:
    dacClockingEntry.setStatus("current")
_DacClockingIndex_Type = Integer32
_DacClockingIndex_Object = MibTableColumn
dacClockingIndex = _DacClockingIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2050, 1, 1),
    _DacClockingIndex_Type()
)
dacClockingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dacClockingIndex.setStatus("current")


class _DacClockingClockSourcePrimary_Type(Integer32):
    """Custom type dacClockingClockSourcePrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              200,
              201,
              202,
              255)
        )
    )
    namedValues = NamedValues(
        *(("auto1", 201),
          ("auto2", 202),
          ("disabled", 255),
          ("external", 200),
          ("if0", 0),
          ("if1", 1),
          ("if10", 10),
          ("if11", 11),
          ("if12", 12),
          ("if13", 13),
          ("if14", 14),
          ("if15", 15),
          ("if16", 16),
          ("if17", 17),
          ("if18", 18),
          ("if19", 19),
          ("if2", 2),
          ("if20", 20),
          ("if21", 21),
          ("if22", 22),
          ("if23", 23),
          ("if24", 24),
          ("if25", 25),
          ("if26", 26),
          ("if27", 27),
          ("if28", 28),
          ("if29", 29),
          ("if3", 3),
          ("if30", 30),
          ("if31", 31),
          ("if32", 32),
          ("if33", 33),
          ("if34", 34),
          ("if35", 35),
          ("if36", 36),
          ("if37", 37),
          ("if38", 38),
          ("if39", 39),
          ("if4", 4),
          ("if40", 40),
          ("if41", 41),
          ("if42", 42),
          ("if43", 43),
          ("if44", 44),
          ("if45", 45),
          ("if46", 46),
          ("if47", 47),
          ("if48", 48),
          ("if49", 49),
          ("if5", 5),
          ("if50", 50),
          ("if51", 51),
          ("if52", 52),
          ("if53", 53),
          ("if54", 54),
          ("if55", 55),
          ("if6", 6),
          ("if7", 7),
          ("if8", 8),
          ("if9", 9))
    )


_DacClockingClockSourcePrimary_Type.__name__ = "Integer32"
_DacClockingClockSourcePrimary_Object = MibTableColumn
dacClockingClockSourcePrimary = _DacClockingClockSourcePrimary_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2050, 1, 2),
    _DacClockingClockSourcePrimary_Type()
)
dacClockingClockSourcePrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dacClockingClockSourcePrimary.setStatus("current")


class _DacClockingClockSourceSecondary_Type(Integer32):
    """Custom type dacClockingClockSourceSecondary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              200,
              201,
              202,
              255)
        )
    )
    namedValues = NamedValues(
        *(("auto1", 201),
          ("auto2", 202),
          ("disabled", 255),
          ("external", 200),
          ("if0", 0),
          ("if1", 1),
          ("if10", 10),
          ("if11", 11),
          ("if12", 12),
          ("if13", 13),
          ("if14", 14),
          ("if15", 15),
          ("if16", 16),
          ("if17", 17),
          ("if18", 18),
          ("if19", 19),
          ("if2", 2),
          ("if20", 20),
          ("if21", 21),
          ("if22", 22),
          ("if23", 23),
          ("if24", 24),
          ("if25", 25),
          ("if26", 26),
          ("if27", 27),
          ("if28", 28),
          ("if29", 29),
          ("if3", 3),
          ("if30", 30),
          ("if31", 31),
          ("if32", 32),
          ("if33", 33),
          ("if34", 34),
          ("if35", 35),
          ("if36", 36),
          ("if37", 37),
          ("if38", 38),
          ("if39", 39),
          ("if4", 4),
          ("if40", 40),
          ("if41", 41),
          ("if42", 42),
          ("if43", 43),
          ("if44", 44),
          ("if45", 45),
          ("if46", 46),
          ("if47", 47),
          ("if48", 48),
          ("if49", 49),
          ("if5", 5),
          ("if50", 50),
          ("if51", 51),
          ("if52", 52),
          ("if53", 53),
          ("if54", 54),
          ("if55", 55),
          ("if6", 6),
          ("if7", 7),
          ("if8", 8),
          ("if9", 9))
    )


_DacClockingClockSourceSecondary_Type.__name__ = "Integer32"
_DacClockingClockSourceSecondary_Object = MibTableColumn
dacClockingClockSourceSecondary = _DacClockingClockSourceSecondary_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2050, 1, 3),
    _DacClockingClockSourceSecondary_Type()
)
dacClockingClockSourceSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dacClockingClockSourceSecondary.setStatus("current")
_DacClockingForce_Type = Boolean
_DacClockingForce_Object = MibTableColumn
dacClockingForce = _DacClockingForce_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2050, 1, 4),
    _DacClockingForce_Type()
)
dacClockingForce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dacClockingForce.setStatus("current")
_T1StatsTable_Object = MibTable
t1StatsTable = _T1StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2102)
)
if mibBuilder.loadTexts:
    t1StatsTable.setStatus("current")
_T1StatsEntry_Object = MibTableRow
t1StatsEntry = _T1StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2102, 1)
)
t1StatsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "t1StatsSlotIndex"),
    (0, "APTIS-MONITOR-MIB", "t1StatsLineNumber"),
)
if mibBuilder.loadTexts:
    t1StatsEntry.setStatus("current")


class _T1StatsAlarmStatus_Type(Integer32):
    """Custom type t1StatsAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bluealarm", 3),
          ("noalarm", 0),
          ("redalarm", 2),
          ("yellowalarm", 1))
    )


_T1StatsAlarmStatus_Type.__name__ = "Integer32"
_T1StatsAlarmStatus_Object = MibTableColumn
t1StatsAlarmStatus = _T1StatsAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2102, 1, 1),
    _T1StatsAlarmStatus_Type()
)
t1StatsAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1StatsAlarmStatus.setStatus("current")


class _T1StatsSlotIndex_Type(Integer32):
    """Custom type t1StatsSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_T1StatsSlotIndex_Type.__name__ = "Integer32"
_T1StatsSlotIndex_Object = MibTableColumn
t1StatsSlotIndex = _T1StatsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2102, 1, 2),
    _T1StatsSlotIndex_Type()
)
t1StatsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1StatsSlotIndex.setStatus("current")


class _T1StatsLineNumber_Type(Integer32):
    """Custom type t1StatsLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 56),
    )


_T1StatsLineNumber_Type.__name__ = "Integer32"
_T1StatsLineNumber_Object = MibTableColumn
t1StatsLineNumber = _T1StatsLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2102, 1, 3),
    _T1StatsLineNumber_Type()
)
t1StatsLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1StatsLineNumber.setStatus("current")
_T1CountsTable_Object = MibTable
t1CountsTable = _T1CountsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2103)
)
if mibBuilder.loadTexts:
    t1CountsTable.setStatus("current")
_T1CountsEntry_Object = MibTableRow
t1CountsEntry = _T1CountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2103, 1)
)
t1CountsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "t1CountsSlotIndex"),
    (0, "APTIS-MONITOR-MIB", "t1CountsLineNumber"),
)
if mibBuilder.loadTexts:
    t1CountsEntry.setStatus("current")
_T1CountsChannelCount_Type = Integer32
_T1CountsChannelCount_Object = MibTableColumn
t1CountsChannelCount = _T1CountsChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2103, 1, 1),
    _T1CountsChannelCount_Type()
)
t1CountsChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1CountsChannelCount.setStatus("current")
_T1CountsChannelsInUse_Type = Integer32
_T1CountsChannelsInUse_Object = MibTableColumn
t1CountsChannelsInUse = _T1CountsChannelsInUse_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2103, 1, 2),
    _T1CountsChannelsInUse_Type()
)
t1CountsChannelsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1CountsChannelsInUse.setStatus("current")
_T1CountsIncomingCallAttempts_Type = Integer32
_T1CountsIncomingCallAttempts_Object = MibTableColumn
t1CountsIncomingCallAttempts = _T1CountsIncomingCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2103, 1, 3),
    _T1CountsIncomingCallAttempts_Type()
)
t1CountsIncomingCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1CountsIncomingCallAttempts.setStatus("current")
_T1CountsIncomingConnects_Type = Integer32
_T1CountsIncomingConnects_Object = MibTableColumn
t1CountsIncomingConnects = _T1CountsIncomingConnects_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2103, 1, 4),
    _T1CountsIncomingConnects_Type()
)
t1CountsIncomingConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1CountsIncomingConnects.setStatus("current")
_T1CountsIncomingDisconnects_Type = Integer32
_T1CountsIncomingDisconnects_Object = MibTableColumn
t1CountsIncomingDisconnects = _T1CountsIncomingDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2103, 1, 5),
    _T1CountsIncomingDisconnects_Type()
)
t1CountsIncomingDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1CountsIncomingDisconnects.setStatus("current")
_T1CountsOutgoingCallAttempts_Type = Integer32
_T1CountsOutgoingCallAttempts_Object = MibTableColumn
t1CountsOutgoingCallAttempts = _T1CountsOutgoingCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2103, 1, 6),
    _T1CountsOutgoingCallAttempts_Type()
)
t1CountsOutgoingCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1CountsOutgoingCallAttempts.setStatus("current")
_T1CountsOutgoingConnects_Type = Integer32
_T1CountsOutgoingConnects_Object = MibTableColumn
t1CountsOutgoingConnects = _T1CountsOutgoingConnects_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2103, 1, 7),
    _T1CountsOutgoingConnects_Type()
)
t1CountsOutgoingConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1CountsOutgoingConnects.setStatus("current")
_T1CountsOutgoingDisconnects_Type = Integer32
_T1CountsOutgoingDisconnects_Object = MibTableColumn
t1CountsOutgoingDisconnects = _T1CountsOutgoingDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2103, 1, 8),
    _T1CountsOutgoingDisconnects_Type()
)
t1CountsOutgoingDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1CountsOutgoingDisconnects.setStatus("current")
_T1CountsSessionAbortMessages_Type = Integer32
_T1CountsSessionAbortMessages_Object = MibTableColumn
t1CountsSessionAbortMessages = _T1CountsSessionAbortMessages_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2103, 1, 9),
    _T1CountsSessionAbortMessages_Type()
)
t1CountsSessionAbortMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1CountsSessionAbortMessages.setStatus("current")


class _T1CountsSlotIndex_Type(Integer32):
    """Custom type t1CountsSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_T1CountsSlotIndex_Type.__name__ = "Integer32"
_T1CountsSlotIndex_Object = MibTableColumn
t1CountsSlotIndex = _T1CountsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2103, 1, 10),
    _T1CountsSlotIndex_Type()
)
t1CountsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1CountsSlotIndex.setStatus("current")


class _T1CountsLineNumber_Type(Integer32):
    """Custom type t1CountsLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 56),
    )


_T1CountsLineNumber_Type.__name__ = "Integer32"
_T1CountsLineNumber_Object = MibTableColumn
t1CountsLineNumber = _T1CountsLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2103, 1, 11),
    _T1CountsLineNumber_Type()
)
t1CountsLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1CountsLineNumber.setStatus("current")
_T1SummaryStatsTable_Object = MibTable
t1SummaryStatsTable = _T1SummaryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2104)
)
if mibBuilder.loadTexts:
    t1SummaryStatsTable.setStatus("current")
_T1SummaryStatsEntry_Object = MibTableRow
t1SummaryStatsEntry = _T1SummaryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2104, 1)
)
t1SummaryStatsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "t1SummaryStatsSlotIndex"),
    (0, "APTIS-MONITOR-MIB", "t1SummaryStatsLineNumber"),
)
if mibBuilder.loadTexts:
    t1SummaryStatsEntry.setStatus("current")
_T1SummaryStatsRingingChannels_Type = Integer32
_T1SummaryStatsRingingChannels_Object = MibTableColumn
t1SummaryStatsRingingChannels = _T1SummaryStatsRingingChannels_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2104, 1, 1),
    _T1SummaryStatsRingingChannels_Type()
)
t1SummaryStatsRingingChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1SummaryStatsRingingChannels.setStatus("current")
_T1SummaryStatsConnectedChannels_Type = Integer32
_T1SummaryStatsConnectedChannels_Object = MibTableColumn
t1SummaryStatsConnectedChannels = _T1SummaryStatsConnectedChannels_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2104, 1, 2),
    _T1SummaryStatsConnectedChannels_Type()
)
t1SummaryStatsConnectedChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1SummaryStatsConnectedChannels.setStatus("current")
_T1SummaryStatsClearingChannels_Type = Integer32
_T1SummaryStatsClearingChannels_Object = MibTableColumn
t1SummaryStatsClearingChannels = _T1SummaryStatsClearingChannels_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2104, 1, 3),
    _T1SummaryStatsClearingChannels_Type()
)
t1SummaryStatsClearingChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1SummaryStatsClearingChannels.setStatus("current")


class _T1SummaryStatsSlotIndex_Type(Integer32):
    """Custom type t1SummaryStatsSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_T1SummaryStatsSlotIndex_Type.__name__ = "Integer32"
_T1SummaryStatsSlotIndex_Object = MibTableColumn
t1SummaryStatsSlotIndex = _T1SummaryStatsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2104, 1, 4),
    _T1SummaryStatsSlotIndex_Type()
)
t1SummaryStatsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1SummaryStatsSlotIndex.setStatus("current")


class _T1SummaryStatsLineNumber_Type(Integer32):
    """Custom type t1SummaryStatsLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 56),
    )


_T1SummaryStatsLineNumber_Type.__name__ = "Integer32"
_T1SummaryStatsLineNumber_Object = MibTableColumn
t1SummaryStatsLineNumber = _T1SummaryStatsLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2104, 1, 5),
    _T1SummaryStatsLineNumber_Type()
)
t1SummaryStatsLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1SummaryStatsLineNumber.setStatus("current")
_T1SummaryStatsFunctionalChannels_Type = Integer32
_T1SummaryStatsFunctionalChannels_Object = MibTableColumn
t1SummaryStatsFunctionalChannels = _T1SummaryStatsFunctionalChannels_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2104, 1, 6),
    _T1SummaryStatsFunctionalChannels_Type()
)
t1SummaryStatsFunctionalChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1SummaryStatsFunctionalChannels.setStatus("current")
_T1SummaryStatsIdleChannels_Type = Integer32
_T1SummaryStatsIdleChannels_Object = MibTableColumn
t1SummaryStatsIdleChannels = _T1SummaryStatsIdleChannels_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2104, 1, 7),
    _T1SummaryStatsIdleChannels_Type()
)
t1SummaryStatsIdleChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1SummaryStatsIdleChannels.setStatus("current")
_Ds0StatsTable_Object = MibTable
ds0StatsTable = _Ds0StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2112)
)
if mibBuilder.loadTexts:
    ds0StatsTable.setStatus("current")
_Ds0StatsEntry_Object = MibTableRow
ds0StatsEntry = _Ds0StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2112, 1)
)
ds0StatsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "ds0StatsSlotIndex"),
    (0, "APTIS-MONITOR-MIB", "ds0StatsLineNumber"),
    (0, "APTIS-MONITOR-MIB", "ds0StatsDs0Index"),
)
if mibBuilder.loadTexts:
    ds0StatsEntry.setStatus("current")
_Ds0StatsInCalls_Type = Integer32
_Ds0StatsInCalls_Object = MibTableColumn
ds0StatsInCalls = _Ds0StatsInCalls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2112, 1, 1),
    _Ds0StatsInCalls_Type()
)
ds0StatsInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0StatsInCalls.setStatus("current")
_Ds0StatsInConnected_Type = Integer32
_Ds0StatsInConnected_Object = MibTableColumn
ds0StatsInConnected = _Ds0StatsInConnected_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2112, 1, 2),
    _Ds0StatsInConnected_Type()
)
ds0StatsInConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0StatsInConnected.setStatus("current")
_Ds0StatsOutCalls_Type = Integer32
_Ds0StatsOutCalls_Object = MibTableColumn
ds0StatsOutCalls = _Ds0StatsOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2112, 1, 3),
    _Ds0StatsOutCalls_Type()
)
ds0StatsOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0StatsOutCalls.setStatus("current")
_Ds0StatsOutConnected_Type = Integer32
_Ds0StatsOutConnected_Object = MibTableColumn
ds0StatsOutConnected = _Ds0StatsOutConnected_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2112, 1, 4),
    _Ds0StatsOutConnected_Type()
)
ds0StatsOutConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0StatsOutConnected.setStatus("current")
_Ds0StatsInCleared_Type = Integer32
_Ds0StatsInCleared_Object = MibTableColumn
ds0StatsInCleared = _Ds0StatsInCleared_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2112, 1, 5),
    _Ds0StatsInCleared_Type()
)
ds0StatsInCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0StatsInCleared.setStatus("current")
_Ds0StatsOutCleared_Type = Integer32
_Ds0StatsOutCleared_Object = MibTableColumn
ds0StatsOutCleared = _Ds0StatsOutCleared_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2112, 1, 6),
    _Ds0StatsOutCleared_Type()
)
ds0StatsOutCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0StatsOutCleared.setStatus("current")


class _Ds0StatsSlotIndex_Type(Integer32):
    """Custom type ds0StatsSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Ds0StatsSlotIndex_Type.__name__ = "Integer32"
_Ds0StatsSlotIndex_Object = MibTableColumn
ds0StatsSlotIndex = _Ds0StatsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2112, 1, 7),
    _Ds0StatsSlotIndex_Type()
)
ds0StatsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0StatsSlotIndex.setStatus("current")


class _Ds0StatsLineNumber_Type(Integer32):
    """Custom type ds0StatsLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 56),
    )


_Ds0StatsLineNumber_Type.__name__ = "Integer32"
_Ds0StatsLineNumber_Object = MibTableColumn
ds0StatsLineNumber = _Ds0StatsLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2112, 1, 8),
    _Ds0StatsLineNumber_Type()
)
ds0StatsLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0StatsLineNumber.setStatus("current")


class _Ds0StatsDs0Index_Type(Integer32):
    """Custom type ds0StatsDs0Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Ds0StatsDs0Index_Type.__name__ = "Integer32"
_Ds0StatsDs0Index_Object = MibTableColumn
ds0StatsDs0Index = _Ds0StatsDs0Index_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2112, 1, 9),
    _Ds0StatsDs0Index_Type()
)
ds0StatsDs0Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0StatsDs0Index.setStatus("current")
_ISDNStatsTable_Object = MibTable
iSDNStatsTable = _ISDNStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2208)
)
if mibBuilder.loadTexts:
    iSDNStatsTable.setStatus("current")
_ISDNStatsEntry_Object = MibTableRow
iSDNStatsEntry = _ISDNStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2208, 1)
)
iSDNStatsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "iSDNStatsInCalls"),
)
if mibBuilder.loadTexts:
    iSDNStatsEntry.setStatus("current")
_ISDNStatsInCalls_Type = Integer32
_ISDNStatsInCalls_Object = MibTableColumn
iSDNStatsInCalls = _ISDNStatsInCalls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2208, 1, 1),
    _ISDNStatsInCalls_Type()
)
iSDNStatsInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSDNStatsInCalls.setStatus("current")
_ISDNStatsInConnected_Type = Integer32
_ISDNStatsInConnected_Object = MibTableColumn
iSDNStatsInConnected = _ISDNStatsInConnected_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2208, 1, 2),
    _ISDNStatsInConnected_Type()
)
iSDNStatsInConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSDNStatsInConnected.setStatus("current")
_ISDNStatsOutCalls_Type = Integer32
_ISDNStatsOutCalls_Object = MibTableColumn
iSDNStatsOutCalls = _ISDNStatsOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2208, 1, 3),
    _ISDNStatsOutCalls_Type()
)
iSDNStatsOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSDNStatsOutCalls.setStatus("current")
_ISDNStatsOutConnected_Type = Integer32
_ISDNStatsOutConnected_Object = MibTableColumn
iSDNStatsOutConnected = _ISDNStatsOutConnected_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2208, 1, 4),
    _ISDNStatsOutConnected_Type()
)
iSDNStatsOutConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSDNStatsOutConnected.setStatus("current")
_ISDNStatsChargedUnits_Type = Integer32
_ISDNStatsChargedUnits_Object = MibTableColumn
iSDNStatsChargedUnits = _ISDNStatsChargedUnits_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2208, 1, 5),
    _ISDNStatsChargedUnits_Type()
)
iSDNStatsChargedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSDNStatsChargedUnits.setStatus("current")
_ISDNLayer2StatsTable_Object = MibTable
iSDNLayer2StatsTable = _ISDNLayer2StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2209)
)
if mibBuilder.loadTexts:
    iSDNLayer2StatsTable.setStatus("current")
_ISDNLayer2StatsEntry_Object = MibTableRow
iSDNLayer2StatsEntry = _ISDNLayer2StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2209, 1)
)
iSDNLayer2StatsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "iSDNLayer2StatsLapdPeerSabme"),
)
if mibBuilder.loadTexts:
    iSDNLayer2StatsEntry.setStatus("current")
_ISDNLayer2StatsLapdPeerSabme_Type = Integer32
_ISDNLayer2StatsLapdPeerSabme_Object = MibTableColumn
iSDNLayer2StatsLapdPeerSabme = _ISDNLayer2StatsLapdPeerSabme_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2209, 1, 1),
    _ISDNLayer2StatsLapdPeerSabme_Type()
)
iSDNLayer2StatsLapdPeerSabme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSDNLayer2StatsLapdPeerSabme.setStatus("current")
_ISDNLayer2StatsLapdRcvdFrmr_Type = Integer32
_ISDNLayer2StatsLapdRcvdFrmr_Object = MibTableColumn
iSDNLayer2StatsLapdRcvdFrmr = _ISDNLayer2StatsLapdRcvdFrmr_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2209, 1, 2),
    _ISDNLayer2StatsLapdRcvdFrmr_Type()
)
iSDNLayer2StatsLapdRcvdFrmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSDNLayer2StatsLapdRcvdFrmr.setStatus("current")


class _ISDNLayer2StatsLapdState_Type(Integer32):
    """Custom type iSDNLayer2StatsLapdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_ISDNLayer2StatsLapdState_Type.__name__ = "Integer32"
_ISDNLayer2StatsLapdState_Object = MibTableColumn
iSDNLayer2StatsLapdState = _ISDNLayer2StatsLapdState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2209, 1, 3),
    _ISDNLayer2StatsLapdState_Type()
)
iSDNLayer2StatsLapdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSDNLayer2StatsLapdState.setStatus("current")
_ISDNHDLCFrameTable_Object = MibTable
iSDNHDLCFrameTable = _ISDNHDLCFrameTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2210)
)
if mibBuilder.loadTexts:
    iSDNHDLCFrameTable.setStatus("current")
_ISDNHDLCFrameEntry_Object = MibTableRow
iSDNHDLCFrameEntry = _ISDNHDLCFrameEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2210, 1)
)
iSDNHDLCFrameEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "iSDNHDLCFrameIndex"),
)
if mibBuilder.loadTexts:
    iSDNHDLCFrameEntry.setStatus("current")
_ISDNHDLCFrameIndex_Type = Integer32
_ISDNHDLCFrameIndex_Object = MibTableColumn
iSDNHDLCFrameIndex = _ISDNHDLCFrameIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2210, 1, 1),
    _ISDNHDLCFrameIndex_Type()
)
iSDNHDLCFrameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSDNHDLCFrameIndex.setStatus("current")
_ISDNHDLCFrameNextIndex_Type = Integer32
_ISDNHDLCFrameNextIndex_Object = MibTableColumn
iSDNHDLCFrameNextIndex = _ISDNHDLCFrameNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2210, 1, 2),
    _ISDNHDLCFrameNextIndex_Type()
)
iSDNHDLCFrameNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSDNHDLCFrameNextIndex.setStatus("current")
_ISDNHDLCFrameMaxIndex_Type = Integer32
_ISDNHDLCFrameMaxIndex_Object = MibTableColumn
iSDNHDLCFrameMaxIndex = _ISDNHDLCFrameMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2210, 1, 3),
    _ISDNHDLCFrameMaxIndex_Type()
)
iSDNHDLCFrameMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSDNHDLCFrameMaxIndex.setStatus("current")
_ISDNHDLCFrameTimestamp_Type = Integer32
_ISDNHDLCFrameTimestamp_Object = MibTableColumn
iSDNHDLCFrameTimestamp = _ISDNHDLCFrameTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2210, 1, 4),
    _ISDNHDLCFrameTimestamp_Type()
)
iSDNHDLCFrameTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSDNHDLCFrameTimestamp.setStatus("current")


class _ISDNHDLCFrameDirection_Type(Integer32):
    """Custom type iSDNHDLCFrameDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("receive", 2),
          ("transmit", 1))
    )


_ISDNHDLCFrameDirection_Type.__name__ = "Integer32"
_ISDNHDLCFrameDirection_Object = MibTableColumn
iSDNHDLCFrameDirection = _ISDNHDLCFrameDirection_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2210, 1, 5),
    _ISDNHDLCFrameDirection_Type()
)
iSDNHDLCFrameDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSDNHDLCFrameDirection.setStatus("current")
_ISDNHDLCFrameLength_Type = Integer32
_ISDNHDLCFrameLength_Object = MibTableColumn
iSDNHDLCFrameLength = _ISDNHDLCFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2210, 1, 6),
    _ISDNHDLCFrameLength_Type()
)
iSDNHDLCFrameLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSDNHDLCFrameLength.setStatus("current")


class _ISDNHDLCFrameMessage_Type(OctetString):
    """Custom type iSDNHDLCFrameMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 260),
    )


_ISDNHDLCFrameMessage_Type.__name__ = "OctetString"
_ISDNHDLCFrameMessage_Object = MibTableColumn
iSDNHDLCFrameMessage = _ISDNHDLCFrameMessage_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2210, 1, 7),
    _ISDNHDLCFrameMessage_Type()
)
iSDNHDLCFrameMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSDNHDLCFrameMessage.setStatus("current")
_E1StatsTable_Object = MibTable
e1StatsTable = _E1StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2502)
)
if mibBuilder.loadTexts:
    e1StatsTable.setStatus("current")
_E1StatsEntry_Object = MibTableRow
e1StatsEntry = _E1StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2502, 1)
)
e1StatsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "e1StatsSlotIndex"),
    (0, "APTIS-MONITOR-MIB", "e1StatsLineNumber"),
)
if mibBuilder.loadTexts:
    e1StatsEntry.setStatus("current")


class _E1StatsAlarmStatus_Type(Integer32):
    """Custom type e1StatsAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("f1", 0),
          ("f2", 1),
          ("f3", 2),
          ("f4", 3),
          ("f5", 4),
          ("f6", 5))
    )


_E1StatsAlarmStatus_Type.__name__ = "Integer32"
_E1StatsAlarmStatus_Object = MibTableColumn
e1StatsAlarmStatus = _E1StatsAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2502, 1, 1),
    _E1StatsAlarmStatus_Type()
)
e1StatsAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1StatsAlarmStatus.setStatus("current")


class _E1StatsSlotIndex_Type(Integer32):
    """Custom type e1StatsSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_E1StatsSlotIndex_Type.__name__ = "Integer32"
_E1StatsSlotIndex_Object = MibTableColumn
e1StatsSlotIndex = _E1StatsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2502, 1, 2),
    _E1StatsSlotIndex_Type()
)
e1StatsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1StatsSlotIndex.setStatus("current")


class _E1StatsLineNumber_Type(Integer32):
    """Custom type e1StatsLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_E1StatsLineNumber_Type.__name__ = "Integer32"
_E1StatsLineNumber_Object = MibTableColumn
e1StatsLineNumber = _E1StatsLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2502, 1, 3),
    _E1StatsLineNumber_Type()
)
e1StatsLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1StatsLineNumber.setStatus("current")
_E1CountsTable_Object = MibTable
e1CountsTable = _E1CountsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2503)
)
if mibBuilder.loadTexts:
    e1CountsTable.setStatus("current")
_E1CountsEntry_Object = MibTableRow
e1CountsEntry = _E1CountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2503, 1)
)
e1CountsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "e1CountsSlotIndex"),
    (0, "APTIS-MONITOR-MIB", "e1CountsLineNumber"),
)
if mibBuilder.loadTexts:
    e1CountsEntry.setStatus("current")
_E1CountsChannelCount_Type = Integer32
_E1CountsChannelCount_Object = MibTableColumn
e1CountsChannelCount = _E1CountsChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2503, 1, 1),
    _E1CountsChannelCount_Type()
)
e1CountsChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1CountsChannelCount.setStatus("current")
_E1CountsChannelsInUse_Type = Integer32
_E1CountsChannelsInUse_Object = MibTableColumn
e1CountsChannelsInUse = _E1CountsChannelsInUse_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2503, 1, 2),
    _E1CountsChannelsInUse_Type()
)
e1CountsChannelsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1CountsChannelsInUse.setStatus("current")
_E1CountsIncomingCallAttempts_Type = Integer32
_E1CountsIncomingCallAttempts_Object = MibTableColumn
e1CountsIncomingCallAttempts = _E1CountsIncomingCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2503, 1, 3),
    _E1CountsIncomingCallAttempts_Type()
)
e1CountsIncomingCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1CountsIncomingCallAttempts.setStatus("current")
_E1CountsIncomingConnects_Type = Integer32
_E1CountsIncomingConnects_Object = MibTableColumn
e1CountsIncomingConnects = _E1CountsIncomingConnects_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2503, 1, 4),
    _E1CountsIncomingConnects_Type()
)
e1CountsIncomingConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1CountsIncomingConnects.setStatus("current")
_E1CountsIncomingDisconnects_Type = Integer32
_E1CountsIncomingDisconnects_Object = MibTableColumn
e1CountsIncomingDisconnects = _E1CountsIncomingDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2503, 1, 5),
    _E1CountsIncomingDisconnects_Type()
)
e1CountsIncomingDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1CountsIncomingDisconnects.setStatus("current")
_E1CountsOutgoingCallAttempts_Type = Integer32
_E1CountsOutgoingCallAttempts_Object = MibTableColumn
e1CountsOutgoingCallAttempts = _E1CountsOutgoingCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2503, 1, 6),
    _E1CountsOutgoingCallAttempts_Type()
)
e1CountsOutgoingCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1CountsOutgoingCallAttempts.setStatus("current")
_E1CountsOutgoingConnects_Type = Integer32
_E1CountsOutgoingConnects_Object = MibTableColumn
e1CountsOutgoingConnects = _E1CountsOutgoingConnects_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2503, 1, 7),
    _E1CountsOutgoingConnects_Type()
)
e1CountsOutgoingConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1CountsOutgoingConnects.setStatus("current")
_E1CountsOutgoingDisconnects_Type = Integer32
_E1CountsOutgoingDisconnects_Object = MibTableColumn
e1CountsOutgoingDisconnects = _E1CountsOutgoingDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2503, 1, 8),
    _E1CountsOutgoingDisconnects_Type()
)
e1CountsOutgoingDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1CountsOutgoingDisconnects.setStatus("current")
_E1CountsSessionAbortMessages_Type = Integer32
_E1CountsSessionAbortMessages_Object = MibTableColumn
e1CountsSessionAbortMessages = _E1CountsSessionAbortMessages_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2503, 1, 9),
    _E1CountsSessionAbortMessages_Type()
)
e1CountsSessionAbortMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1CountsSessionAbortMessages.setStatus("current")


class _E1CountsSlotIndex_Type(Integer32):
    """Custom type e1CountsSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_E1CountsSlotIndex_Type.__name__ = "Integer32"
_E1CountsSlotIndex_Object = MibTableColumn
e1CountsSlotIndex = _E1CountsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2503, 1, 10),
    _E1CountsSlotIndex_Type()
)
e1CountsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1CountsSlotIndex.setStatus("current")


class _E1CountsLineNumber_Type(Integer32):
    """Custom type e1CountsLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_E1CountsLineNumber_Type.__name__ = "Integer32"
_E1CountsLineNumber_Object = MibTableColumn
e1CountsLineNumber = _E1CountsLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2503, 1, 11),
    _E1CountsLineNumber_Type()
)
e1CountsLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1CountsLineNumber.setStatus("current")
_E1SummaryStatsTable_Object = MibTable
e1SummaryStatsTable = _E1SummaryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2504)
)
if mibBuilder.loadTexts:
    e1SummaryStatsTable.setStatus("current")
_E1SummaryStatsEntry_Object = MibTableRow
e1SummaryStatsEntry = _E1SummaryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2504, 1)
)
e1SummaryStatsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "e1SummaryStatsSlotIndex"),
    (0, "APTIS-MONITOR-MIB", "e1SummaryStatsLineNumber"),
)
if mibBuilder.loadTexts:
    e1SummaryStatsEntry.setStatus("current")
_E1SummaryStatsRingingChannels_Type = Integer32
_E1SummaryStatsRingingChannels_Object = MibTableColumn
e1SummaryStatsRingingChannels = _E1SummaryStatsRingingChannels_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2504, 1, 1),
    _E1SummaryStatsRingingChannels_Type()
)
e1SummaryStatsRingingChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1SummaryStatsRingingChannels.setStatus("current")
_E1SummaryStatsConnectedChannels_Type = Integer32
_E1SummaryStatsConnectedChannels_Object = MibTableColumn
e1SummaryStatsConnectedChannels = _E1SummaryStatsConnectedChannels_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2504, 1, 2),
    _E1SummaryStatsConnectedChannels_Type()
)
e1SummaryStatsConnectedChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1SummaryStatsConnectedChannels.setStatus("current")
_E1SummaryStatsClearingChannels_Type = Integer32
_E1SummaryStatsClearingChannels_Object = MibTableColumn
e1SummaryStatsClearingChannels = _E1SummaryStatsClearingChannels_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2504, 1, 3),
    _E1SummaryStatsClearingChannels_Type()
)
e1SummaryStatsClearingChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1SummaryStatsClearingChannels.setStatus("current")


class _E1SummaryStatsSlotIndex_Type(Integer32):
    """Custom type e1SummaryStatsSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_E1SummaryStatsSlotIndex_Type.__name__ = "Integer32"
_E1SummaryStatsSlotIndex_Object = MibTableColumn
e1SummaryStatsSlotIndex = _E1SummaryStatsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2504, 1, 4),
    _E1SummaryStatsSlotIndex_Type()
)
e1SummaryStatsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1SummaryStatsSlotIndex.setStatus("current")


class _E1SummaryStatsLineNumber_Type(Integer32):
    """Custom type e1SummaryStatsLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_E1SummaryStatsLineNumber_Type.__name__ = "Integer32"
_E1SummaryStatsLineNumber_Object = MibTableColumn
e1SummaryStatsLineNumber = _E1SummaryStatsLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2504, 1, 5),
    _E1SummaryStatsLineNumber_Type()
)
e1SummaryStatsLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1SummaryStatsLineNumber.setStatus("current")
_E1SummaryStatsFunctionalChannels_Type = Integer32
_E1SummaryStatsFunctionalChannels_Object = MibTableColumn
e1SummaryStatsFunctionalChannels = _E1SummaryStatsFunctionalChannels_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2504, 1, 6),
    _E1SummaryStatsFunctionalChannels_Type()
)
e1SummaryStatsFunctionalChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1SummaryStatsFunctionalChannels.setStatus("current")
_E1SummaryStatsIdleChannels_Type = Integer32
_E1SummaryStatsIdleChannels_Object = MibTableColumn
e1SummaryStatsIdleChannels = _E1SummaryStatsIdleChannels_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2504, 1, 7),
    _E1SummaryStatsIdleChannels_Type()
)
e1SummaryStatsIdleChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1SummaryStatsIdleChannels.setStatus("current")
_ClockStatusTable_Object = MibTable
clockStatusTable = _ClockStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2901)
)
if mibBuilder.loadTexts:
    clockStatusTable.setStatus("current")
_ClockStatusEntry_Object = MibTableRow
clockStatusEntry = _ClockStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2901, 1)
)
clockStatusEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "clockStatusCurrentSource"),
)
if mibBuilder.loadTexts:
    clockStatusEntry.setStatus("current")


class _ClockStatusCurrentSource_Type(Integer32):
    """Custom type clockStatusCurrentSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 0),
          ("primary", 1),
          ("secondary", 2))
    )


_ClockStatusCurrentSource_Type.__name__ = "Integer32"
_ClockStatusCurrentSource_Object = MibTableColumn
clockStatusCurrentSource = _ClockStatusCurrentSource_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 2901, 1, 1),
    _ClockStatusCurrentSource_Type()
)
clockStatusCurrentSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clockStatusCurrentSource.setStatus("current")
_TimerStatsTable_Object = MibTable
timerStatsTable = _TimerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3601)
)
if mibBuilder.loadTexts:
    timerStatsTable.setStatus("current")
_TimerStatsEntry_Object = MibTableRow
timerStatsEntry = _TimerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3601, 1)
)
timerStatsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "timerStatsSlotNumber"),
)
if mibBuilder.loadTexts:
    timerStatsEntry.setStatus("current")
_TimerStatsSlotNumber_Type = Integer32
_TimerStatsSlotNumber_Object = MibTableColumn
timerStatsSlotNumber = _TimerStatsSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3601, 1, 1),
    _TimerStatsSlotNumber_Type()
)
timerStatsSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timerStatsSlotNumber.setStatus("current")


class _TimerStatsCardType_Type(Integer32):
    """Custom type timerStatsCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dAC", 2),
          ("mAC", 3),
          ("sCC", 1),
          ("unknown", 0))
    )


_TimerStatsCardType_Type.__name__ = "Integer32"
_TimerStatsCardType_Object = MibTableColumn
timerStatsCardType = _TimerStatsCardType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3601, 1, 2),
    _TimerStatsCardType_Type()
)
timerStatsCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timerStatsCardType.setStatus("current")
_TimerStatsCPUNumber_Type = Integer32
_TimerStatsCPUNumber_Object = MibTableColumn
timerStatsCPUNumber = _TimerStatsCPUNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3601, 1, 3),
    _TimerStatsCPUNumber_Type()
)
timerStatsCPUNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timerStatsCPUNumber.setStatus("current")
_TimerStatsTimerEntrySize_Type = Integer32
_TimerStatsTimerEntrySize_Object = MibTableColumn
timerStatsTimerEntrySize = _TimerStatsTimerEntrySize_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3601, 1, 101),
    _TimerStatsTimerEntrySize_Type()
)
timerStatsTimerEntrySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timerStatsTimerEntrySize.setStatus("current")
_TimerStatsTimerMemorySize_Type = Integer32
_TimerStatsTimerMemorySize_Object = MibTableColumn
timerStatsTimerMemorySize = _TimerStatsTimerMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3601, 1, 102),
    _TimerStatsTimerMemorySize_Type()
)
timerStatsTimerMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timerStatsTimerMemorySize.setStatus("current")
_TimerStatsTotalCount_Type = Integer32
_TimerStatsTotalCount_Object = MibTableColumn
timerStatsTotalCount = _TimerStatsTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3601, 1, 201),
    _TimerStatsTotalCount_Type()
)
timerStatsTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timerStatsTotalCount.setStatus("current")
_TimerStatsFreeCount_Type = Integer32
_TimerStatsFreeCount_Object = MibTableColumn
timerStatsFreeCount = _TimerStatsFreeCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3601, 1, 202),
    _TimerStatsFreeCount_Type()
)
timerStatsFreeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timerStatsFreeCount.setStatus("current")
_TimerStatsFreeMin_Type = Integer32
_TimerStatsFreeMin_Object = MibTableColumn
timerStatsFreeMin = _TimerStatsFreeMin_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3601, 1, 203),
    _TimerStatsFreeMin_Type()
)
timerStatsFreeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timerStatsFreeMin.setStatus("current")
_TimerStatsActiveCount_Type = Integer32
_TimerStatsActiveCount_Object = MibTableColumn
timerStatsActiveCount = _TimerStatsActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3601, 1, 204),
    _TimerStatsActiveCount_Type()
)
timerStatsActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timerStatsActiveCount.setStatus("current")
_TimerStatsActiveMax_Type = Integer32
_TimerStatsActiveMax_Object = MibTableColumn
timerStatsActiveMax = _TimerStatsActiveMax_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3601, 1, 205),
    _TimerStatsActiveMax_Type()
)
timerStatsActiveMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timerStatsActiveMax.setStatus("current")
_TimerStatsAllocSuccesses_Type = Integer32
_TimerStatsAllocSuccesses_Object = MibTableColumn
timerStatsAllocSuccesses = _TimerStatsAllocSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3601, 1, 301),
    _TimerStatsAllocSuccesses_Type()
)
timerStatsAllocSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timerStatsAllocSuccesses.setStatus("current")
_TimerStatsAllocFails_Type = Integer32
_TimerStatsAllocFails_Object = MibTableColumn
timerStatsAllocFails = _TimerStatsAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3601, 1, 302),
    _TimerStatsAllocFails_Type()
)
timerStatsAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timerStatsAllocFails.setStatus("current")
_TimerStatsFreeSuccesses_Type = Integer32
_TimerStatsFreeSuccesses_Object = MibTableColumn
timerStatsFreeSuccesses = _TimerStatsFreeSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3601, 1, 303),
    _TimerStatsFreeSuccesses_Type()
)
timerStatsFreeSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timerStatsFreeSuccesses.setStatus("current")
_TimerStatsFreeFails_Type = Integer32
_TimerStatsFreeFails_Object = MibTableColumn
timerStatsFreeFails = _TimerStatsFreeFails_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3601, 1, 304),
    _TimerStatsFreeFails_Type()
)
timerStatsFreeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timerStatsFreeFails.setStatus("current")
_PbufStatsTable_Object = MibTable
pbufStatsTable = _PbufStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603)
)
if mibBuilder.loadTexts:
    pbufStatsTable.setStatus("current")
_PbufStatsEntry_Object = MibTableRow
pbufStatsEntry = _PbufStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1)
)
pbufStatsEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "pbufStatsSlotNumber"),
)
if mibBuilder.loadTexts:
    pbufStatsEntry.setStatus("current")
_PbufStatsSlotNumber_Type = Integer32
_PbufStatsSlotNumber_Object = MibTableColumn
pbufStatsSlotNumber = _PbufStatsSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 1),
    _PbufStatsSlotNumber_Type()
)
pbufStatsSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsSlotNumber.setStatus("current")


class _PbufStatsCardType_Type(Integer32):
    """Custom type pbufStatsCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mAC", 3),
          ("sCC", 1),
          ("tSC", 2),
          ("unknown", 0))
    )


_PbufStatsCardType_Type.__name__ = "Integer32"
_PbufStatsCardType_Object = MibTableColumn
pbufStatsCardType = _PbufStatsCardType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 2),
    _PbufStatsCardType_Type()
)
pbufStatsCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsCardType.setStatus("current")
_PbufStatsCPUNumber_Type = Integer32
_PbufStatsCPUNumber_Object = MibTableColumn
pbufStatsCPUNumber = _PbufStatsCPUNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 3),
    _PbufStatsCPUNumber_Type()
)
pbufStatsCPUNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsCPUNumber.setStatus("current")
_PbufStatsDataSize0_Type = Integer32
_PbufStatsDataSize0_Object = MibTableColumn
pbufStatsDataSize0 = _PbufStatsDataSize0_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 101),
    _PbufStatsDataSize0_Type()
)
pbufStatsDataSize0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsDataSize0.setStatus("current")
_PbufStatsTotalCount0_Type = Integer32
_PbufStatsTotalCount0_Object = MibTableColumn
pbufStatsTotalCount0 = _PbufStatsTotalCount0_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 102),
    _PbufStatsTotalCount0_Type()
)
pbufStatsTotalCount0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsTotalCount0.setStatus("current")
_PbufStatsAllocatedCount0_Type = Integer32
_PbufStatsAllocatedCount0_Object = MibTableColumn
pbufStatsAllocatedCount0 = _PbufStatsAllocatedCount0_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 103),
    _PbufStatsAllocatedCount0_Type()
)
pbufStatsAllocatedCount0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsAllocatedCount0.setStatus("current")
_PbufStatsPermAllocatedCount0_Type = Integer32
_PbufStatsPermAllocatedCount0_Object = MibTableColumn
pbufStatsPermAllocatedCount0 = _PbufStatsPermAllocatedCount0_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 104),
    _PbufStatsPermAllocatedCount0_Type()
)
pbufStatsPermAllocatedCount0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsPermAllocatedCount0.setStatus("current")
_PbufStatsAllocatedMax0_Type = Integer32
_PbufStatsAllocatedMax0_Object = MibTableColumn
pbufStatsAllocatedMax0 = _PbufStatsAllocatedMax0_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 105),
    _PbufStatsAllocatedMax0_Type()
)
pbufStatsAllocatedMax0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsAllocatedMax0.setStatus("current")
_PbufStatsFreeCount0_Type = Integer32
_PbufStatsFreeCount0_Object = MibTableColumn
pbufStatsFreeCount0 = _PbufStatsFreeCount0_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 106),
    _PbufStatsFreeCount0_Type()
)
pbufStatsFreeCount0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsFreeCount0.setStatus("current")
_PbufStatsFreeMin0_Type = Integer32
_PbufStatsFreeMin0_Object = MibTableColumn
pbufStatsFreeMin0 = _PbufStatsFreeMin0_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 107),
    _PbufStatsFreeMin0_Type()
)
pbufStatsFreeMin0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsFreeMin0.setStatus("current")
_PbufStatsAllocSuccesses0_Type = Integer32
_PbufStatsAllocSuccesses0_Object = MibTableColumn
pbufStatsAllocSuccesses0 = _PbufStatsAllocSuccesses0_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 108),
    _PbufStatsAllocSuccesses0_Type()
)
pbufStatsAllocSuccesses0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsAllocSuccesses0.setStatus("current")
_PbufStatsAllocFails0_Type = Integer32
_PbufStatsAllocFails0_Object = MibTableColumn
pbufStatsAllocFails0 = _PbufStatsAllocFails0_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 109),
    _PbufStatsAllocFails0_Type()
)
pbufStatsAllocFails0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsAllocFails0.setStatus("current")
_PbufStatsFreeSuccesses0_Type = Integer32
_PbufStatsFreeSuccesses0_Object = MibTableColumn
pbufStatsFreeSuccesses0 = _PbufStatsFreeSuccesses0_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 110),
    _PbufStatsFreeSuccesses0_Type()
)
pbufStatsFreeSuccesses0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsFreeSuccesses0.setStatus("current")
_PbufStatsFreeFails0_Type = Integer32
_PbufStatsFreeFails0_Object = MibTableColumn
pbufStatsFreeFails0 = _PbufStatsFreeFails0_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 111),
    _PbufStatsFreeFails0_Type()
)
pbufStatsFreeFails0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsFreeFails0.setStatus("current")
_PbufStatsDataSize1_Type = Integer32
_PbufStatsDataSize1_Object = MibTableColumn
pbufStatsDataSize1 = _PbufStatsDataSize1_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 201),
    _PbufStatsDataSize1_Type()
)
pbufStatsDataSize1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsDataSize1.setStatus("current")
_PbufStatsTotalCount1_Type = Integer32
_PbufStatsTotalCount1_Object = MibTableColumn
pbufStatsTotalCount1 = _PbufStatsTotalCount1_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 202),
    _PbufStatsTotalCount1_Type()
)
pbufStatsTotalCount1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsTotalCount1.setStatus("current")
_PbufStatsAllocatedCount1_Type = Integer32
_PbufStatsAllocatedCount1_Object = MibTableColumn
pbufStatsAllocatedCount1 = _PbufStatsAllocatedCount1_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 203),
    _PbufStatsAllocatedCount1_Type()
)
pbufStatsAllocatedCount1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsAllocatedCount1.setStatus("current")
_PbufStatsPermAllocatedCount1_Type = Integer32
_PbufStatsPermAllocatedCount1_Object = MibTableColumn
pbufStatsPermAllocatedCount1 = _PbufStatsPermAllocatedCount1_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 204),
    _PbufStatsPermAllocatedCount1_Type()
)
pbufStatsPermAllocatedCount1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsPermAllocatedCount1.setStatus("current")
_PbufStatsAllocatedMax1_Type = Integer32
_PbufStatsAllocatedMax1_Object = MibTableColumn
pbufStatsAllocatedMax1 = _PbufStatsAllocatedMax1_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 205),
    _PbufStatsAllocatedMax1_Type()
)
pbufStatsAllocatedMax1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsAllocatedMax1.setStatus("current")
_PbufStatsFreeCount1_Type = Integer32
_PbufStatsFreeCount1_Object = MibTableColumn
pbufStatsFreeCount1 = _PbufStatsFreeCount1_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 206),
    _PbufStatsFreeCount1_Type()
)
pbufStatsFreeCount1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsFreeCount1.setStatus("current")
_PbufStatsFreeMin1_Type = Integer32
_PbufStatsFreeMin1_Object = MibTableColumn
pbufStatsFreeMin1 = _PbufStatsFreeMin1_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 207),
    _PbufStatsFreeMin1_Type()
)
pbufStatsFreeMin1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsFreeMin1.setStatus("current")
_PbufStatsAllocSuccesses1_Type = Integer32
_PbufStatsAllocSuccesses1_Object = MibTableColumn
pbufStatsAllocSuccesses1 = _PbufStatsAllocSuccesses1_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 208),
    _PbufStatsAllocSuccesses1_Type()
)
pbufStatsAllocSuccesses1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsAllocSuccesses1.setStatus("current")
_PbufStatsAllocFails1_Type = Integer32
_PbufStatsAllocFails1_Object = MibTableColumn
pbufStatsAllocFails1 = _PbufStatsAllocFails1_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 209),
    _PbufStatsAllocFails1_Type()
)
pbufStatsAllocFails1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsAllocFails1.setStatus("current")
_PbufStatsFreeSuccesses1_Type = Integer32
_PbufStatsFreeSuccesses1_Object = MibTableColumn
pbufStatsFreeSuccesses1 = _PbufStatsFreeSuccesses1_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 210),
    _PbufStatsFreeSuccesses1_Type()
)
pbufStatsFreeSuccesses1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsFreeSuccesses1.setStatus("current")
_PbufStatsFreeFails1_Type = Integer32
_PbufStatsFreeFails1_Object = MibTableColumn
pbufStatsFreeFails1 = _PbufStatsFreeFails1_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 211),
    _PbufStatsFreeFails1_Type()
)
pbufStatsFreeFails1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsFreeFails1.setStatus("current")
_PbufStatsDataSize2_Type = Integer32
_PbufStatsDataSize2_Object = MibTableColumn
pbufStatsDataSize2 = _PbufStatsDataSize2_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 301),
    _PbufStatsDataSize2_Type()
)
pbufStatsDataSize2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsDataSize2.setStatus("current")
_PbufStatsTotalCount2_Type = Integer32
_PbufStatsTotalCount2_Object = MibTableColumn
pbufStatsTotalCount2 = _PbufStatsTotalCount2_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 302),
    _PbufStatsTotalCount2_Type()
)
pbufStatsTotalCount2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsTotalCount2.setStatus("current")
_PbufStatsAllocatedCount2_Type = Integer32
_PbufStatsAllocatedCount2_Object = MibTableColumn
pbufStatsAllocatedCount2 = _PbufStatsAllocatedCount2_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 303),
    _PbufStatsAllocatedCount2_Type()
)
pbufStatsAllocatedCount2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsAllocatedCount2.setStatus("current")
_PbufStatsPermAllocatedCount2_Type = Integer32
_PbufStatsPermAllocatedCount2_Object = MibTableColumn
pbufStatsPermAllocatedCount2 = _PbufStatsPermAllocatedCount2_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 304),
    _PbufStatsPermAllocatedCount2_Type()
)
pbufStatsPermAllocatedCount2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsPermAllocatedCount2.setStatus("current")
_PbufStatsAllocatedMax2_Type = Integer32
_PbufStatsAllocatedMax2_Object = MibTableColumn
pbufStatsAllocatedMax2 = _PbufStatsAllocatedMax2_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 305),
    _PbufStatsAllocatedMax2_Type()
)
pbufStatsAllocatedMax2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsAllocatedMax2.setStatus("current")
_PbufStatsFreeCount2_Type = Integer32
_PbufStatsFreeCount2_Object = MibTableColumn
pbufStatsFreeCount2 = _PbufStatsFreeCount2_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 306),
    _PbufStatsFreeCount2_Type()
)
pbufStatsFreeCount2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsFreeCount2.setStatus("current")
_PbufStatsFreeMin2_Type = Integer32
_PbufStatsFreeMin2_Object = MibTableColumn
pbufStatsFreeMin2 = _PbufStatsFreeMin2_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 307),
    _PbufStatsFreeMin2_Type()
)
pbufStatsFreeMin2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsFreeMin2.setStatus("current")
_PbufStatsAllocSuccesses2_Type = Integer32
_PbufStatsAllocSuccesses2_Object = MibTableColumn
pbufStatsAllocSuccesses2 = _PbufStatsAllocSuccesses2_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 308),
    _PbufStatsAllocSuccesses2_Type()
)
pbufStatsAllocSuccesses2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsAllocSuccesses2.setStatus("current")
_PbufStatsAllocFails2_Type = Integer32
_PbufStatsAllocFails2_Object = MibTableColumn
pbufStatsAllocFails2 = _PbufStatsAllocFails2_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 309),
    _PbufStatsAllocFails2_Type()
)
pbufStatsAllocFails2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsAllocFails2.setStatus("current")
_PbufStatsFreeSuccesses2_Type = Integer32
_PbufStatsFreeSuccesses2_Object = MibTableColumn
pbufStatsFreeSuccesses2 = _PbufStatsFreeSuccesses2_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 310),
    _PbufStatsFreeSuccesses2_Type()
)
pbufStatsFreeSuccesses2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsFreeSuccesses2.setStatus("current")
_PbufStatsFreeFails2_Type = Integer32
_PbufStatsFreeFails2_Object = MibTableColumn
pbufStatsFreeFails2 = _PbufStatsFreeFails2_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 311),
    _PbufStatsFreeFails2_Type()
)
pbufStatsFreeFails2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsFreeFails2.setStatus("current")
_PbufStatsDataSize3_Type = Integer32
_PbufStatsDataSize3_Object = MibTableColumn
pbufStatsDataSize3 = _PbufStatsDataSize3_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 401),
    _PbufStatsDataSize3_Type()
)
pbufStatsDataSize3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsDataSize3.setStatus("current")
_PbufStatsTotalCount3_Type = Integer32
_PbufStatsTotalCount3_Object = MibTableColumn
pbufStatsTotalCount3 = _PbufStatsTotalCount3_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 402),
    _PbufStatsTotalCount3_Type()
)
pbufStatsTotalCount3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsTotalCount3.setStatus("current")
_PbufStatsAllocatedCount3_Type = Integer32
_PbufStatsAllocatedCount3_Object = MibTableColumn
pbufStatsAllocatedCount3 = _PbufStatsAllocatedCount3_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 403),
    _PbufStatsAllocatedCount3_Type()
)
pbufStatsAllocatedCount3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsAllocatedCount3.setStatus("current")
_PbufStatsPermAllocatedCount3_Type = Integer32
_PbufStatsPermAllocatedCount3_Object = MibTableColumn
pbufStatsPermAllocatedCount3 = _PbufStatsPermAllocatedCount3_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 404),
    _PbufStatsPermAllocatedCount3_Type()
)
pbufStatsPermAllocatedCount3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsPermAllocatedCount3.setStatus("current")
_PbufStatsAllocatedMax3_Type = Integer32
_PbufStatsAllocatedMax3_Object = MibTableColumn
pbufStatsAllocatedMax3 = _PbufStatsAllocatedMax3_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 405),
    _PbufStatsAllocatedMax3_Type()
)
pbufStatsAllocatedMax3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsAllocatedMax3.setStatus("current")
_PbufStatsFreeCount3_Type = Integer32
_PbufStatsFreeCount3_Object = MibTableColumn
pbufStatsFreeCount3 = _PbufStatsFreeCount3_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 406),
    _PbufStatsFreeCount3_Type()
)
pbufStatsFreeCount3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsFreeCount3.setStatus("current")
_PbufStatsFreeMin3_Type = Integer32
_PbufStatsFreeMin3_Object = MibTableColumn
pbufStatsFreeMin3 = _PbufStatsFreeMin3_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 407),
    _PbufStatsFreeMin3_Type()
)
pbufStatsFreeMin3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsFreeMin3.setStatus("current")
_PbufStatsAllocSuccesses3_Type = Integer32
_PbufStatsAllocSuccesses3_Object = MibTableColumn
pbufStatsAllocSuccesses3 = _PbufStatsAllocSuccesses3_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 408),
    _PbufStatsAllocSuccesses3_Type()
)
pbufStatsAllocSuccesses3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsAllocSuccesses3.setStatus("current")
_PbufStatsAllocFails3_Type = Integer32
_PbufStatsAllocFails3_Object = MibTableColumn
pbufStatsAllocFails3 = _PbufStatsAllocFails3_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 409),
    _PbufStatsAllocFails3_Type()
)
pbufStatsAllocFails3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsAllocFails3.setStatus("current")
_PbufStatsFreeSuccesses3_Type = Integer32
_PbufStatsFreeSuccesses3_Object = MibTableColumn
pbufStatsFreeSuccesses3 = _PbufStatsFreeSuccesses3_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 410),
    _PbufStatsFreeSuccesses3_Type()
)
pbufStatsFreeSuccesses3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsFreeSuccesses3.setStatus("current")
_PbufStatsFreeFails3_Type = Integer32
_PbufStatsFreeFails3_Object = MibTableColumn
pbufStatsFreeFails3 = _PbufStatsFreeFails3_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 411),
    _PbufStatsFreeFails3_Type()
)
pbufStatsFreeFails3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsFreeFails3.setStatus("current")
_PbufStatsDataSize4_Type = Integer32
_PbufStatsDataSize4_Object = MibTableColumn
pbufStatsDataSize4 = _PbufStatsDataSize4_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 501),
    _PbufStatsDataSize4_Type()
)
pbufStatsDataSize4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsDataSize4.setStatus("current")
_PbufStatsTotalCount4_Type = Integer32
_PbufStatsTotalCount4_Object = MibTableColumn
pbufStatsTotalCount4 = _PbufStatsTotalCount4_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 502),
    _PbufStatsTotalCount4_Type()
)
pbufStatsTotalCount4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsTotalCount4.setStatus("current")
_PbufStatsAllocatedCount4_Type = Integer32
_PbufStatsAllocatedCount4_Object = MibTableColumn
pbufStatsAllocatedCount4 = _PbufStatsAllocatedCount4_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 503),
    _PbufStatsAllocatedCount4_Type()
)
pbufStatsAllocatedCount4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsAllocatedCount4.setStatus("current")
_PbufStatsPermAllocatedCount4_Type = Integer32
_PbufStatsPermAllocatedCount4_Object = MibTableColumn
pbufStatsPermAllocatedCount4 = _PbufStatsPermAllocatedCount4_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 504),
    _PbufStatsPermAllocatedCount4_Type()
)
pbufStatsPermAllocatedCount4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsPermAllocatedCount4.setStatus("current")
_PbufStatsAllocatedMax4_Type = Integer32
_PbufStatsAllocatedMax4_Object = MibTableColumn
pbufStatsAllocatedMax4 = _PbufStatsAllocatedMax4_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 505),
    _PbufStatsAllocatedMax4_Type()
)
pbufStatsAllocatedMax4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsAllocatedMax4.setStatus("current")
_PbufStatsFreeCount4_Type = Integer32
_PbufStatsFreeCount4_Object = MibTableColumn
pbufStatsFreeCount4 = _PbufStatsFreeCount4_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 506),
    _PbufStatsFreeCount4_Type()
)
pbufStatsFreeCount4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsFreeCount4.setStatus("current")
_PbufStatsFreeMin4_Type = Integer32
_PbufStatsFreeMin4_Object = MibTableColumn
pbufStatsFreeMin4 = _PbufStatsFreeMin4_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 507),
    _PbufStatsFreeMin4_Type()
)
pbufStatsFreeMin4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsFreeMin4.setStatus("current")
_PbufStatsAllocSuccesses4_Type = Integer32
_PbufStatsAllocSuccesses4_Object = MibTableColumn
pbufStatsAllocSuccesses4 = _PbufStatsAllocSuccesses4_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 508),
    _PbufStatsAllocSuccesses4_Type()
)
pbufStatsAllocSuccesses4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsAllocSuccesses4.setStatus("current")
_PbufStatsAllocFails4_Type = Integer32
_PbufStatsAllocFails4_Object = MibTableColumn
pbufStatsAllocFails4 = _PbufStatsAllocFails4_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 509),
    _PbufStatsAllocFails4_Type()
)
pbufStatsAllocFails4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsAllocFails4.setStatus("current")
_PbufStatsFreeSuccesses4_Type = Integer32
_PbufStatsFreeSuccesses4_Object = MibTableColumn
pbufStatsFreeSuccesses4 = _PbufStatsFreeSuccesses4_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 510),
    _PbufStatsFreeSuccesses4_Type()
)
pbufStatsFreeSuccesses4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsFreeSuccesses4.setStatus("current")
_PbufStatsFreeFails4_Type = Integer32
_PbufStatsFreeFails4_Object = MibTableColumn
pbufStatsFreeFails4 = _PbufStatsFreeFails4_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 511),
    _PbufStatsFreeFails4_Type()
)
pbufStatsFreeFails4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsFreeFails4.setStatus("current")
_PbufStatsDataSize5_Type = Integer32
_PbufStatsDataSize5_Object = MibTableColumn
pbufStatsDataSize5 = _PbufStatsDataSize5_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 601),
    _PbufStatsDataSize5_Type()
)
pbufStatsDataSize5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsDataSize5.setStatus("current")
_PbufStatsTotalCount5_Type = Integer32
_PbufStatsTotalCount5_Object = MibTableColumn
pbufStatsTotalCount5 = _PbufStatsTotalCount5_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 602),
    _PbufStatsTotalCount5_Type()
)
pbufStatsTotalCount5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsTotalCount5.setStatus("current")
_PbufStatsAllocatedCount5_Type = Integer32
_PbufStatsAllocatedCount5_Object = MibTableColumn
pbufStatsAllocatedCount5 = _PbufStatsAllocatedCount5_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 603),
    _PbufStatsAllocatedCount5_Type()
)
pbufStatsAllocatedCount5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsAllocatedCount5.setStatus("current")
_PbufStatsPermAllocatedCount5_Type = Integer32
_PbufStatsPermAllocatedCount5_Object = MibTableColumn
pbufStatsPermAllocatedCount5 = _PbufStatsPermAllocatedCount5_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 604),
    _PbufStatsPermAllocatedCount5_Type()
)
pbufStatsPermAllocatedCount5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsPermAllocatedCount5.setStatus("current")
_PbufStatsAllocatedMax5_Type = Integer32
_PbufStatsAllocatedMax5_Object = MibTableColumn
pbufStatsAllocatedMax5 = _PbufStatsAllocatedMax5_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 605),
    _PbufStatsAllocatedMax5_Type()
)
pbufStatsAllocatedMax5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsAllocatedMax5.setStatus("current")
_PbufStatsFreeCount5_Type = Integer32
_PbufStatsFreeCount5_Object = MibTableColumn
pbufStatsFreeCount5 = _PbufStatsFreeCount5_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 606),
    _PbufStatsFreeCount5_Type()
)
pbufStatsFreeCount5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsFreeCount5.setStatus("current")
_PbufStatsFreeMin5_Type = Integer32
_PbufStatsFreeMin5_Object = MibTableColumn
pbufStatsFreeMin5 = _PbufStatsFreeMin5_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 607),
    _PbufStatsFreeMin5_Type()
)
pbufStatsFreeMin5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsFreeMin5.setStatus("current")
_PbufStatsAllocSuccesses5_Type = Integer32
_PbufStatsAllocSuccesses5_Object = MibTableColumn
pbufStatsAllocSuccesses5 = _PbufStatsAllocSuccesses5_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 608),
    _PbufStatsAllocSuccesses5_Type()
)
pbufStatsAllocSuccesses5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsAllocSuccesses5.setStatus("current")
_PbufStatsAllocFails5_Type = Integer32
_PbufStatsAllocFails5_Object = MibTableColumn
pbufStatsAllocFails5 = _PbufStatsAllocFails5_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 609),
    _PbufStatsAllocFails5_Type()
)
pbufStatsAllocFails5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsAllocFails5.setStatus("current")
_PbufStatsFreeSuccesses5_Type = Integer32
_PbufStatsFreeSuccesses5_Object = MibTableColumn
pbufStatsFreeSuccesses5 = _PbufStatsFreeSuccesses5_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 610),
    _PbufStatsFreeSuccesses5_Type()
)
pbufStatsFreeSuccesses5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsFreeSuccesses5.setStatus("current")
_PbufStatsFreeFails5_Type = Integer32
_PbufStatsFreeFails5_Object = MibTableColumn
pbufStatsFreeFails5 = _PbufStatsFreeFails5_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3603, 1, 611),
    _PbufStatsFreeFails5_Type()
)
pbufStatsFreeFails5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbufStatsFreeFails5.setStatus("current")
_MemoryStatsTableTable_Object = MibTable
memoryStatsTableTable = _MemoryStatsTableTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3605)
)
if mibBuilder.loadTexts:
    memoryStatsTableTable.setStatus("current")
_MemoryStatsTableEntry_Object = MibTableRow
memoryStatsTableEntry = _MemoryStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3605, 1)
)
memoryStatsTableEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "memoryStatsTableSlotNumber"),
)
if mibBuilder.loadTexts:
    memoryStatsTableEntry.setStatus("current")


class _MemoryStatsTableSlotNumber_Type(Integer32):
    """Custom type memoryStatsTableSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("bep", 1),
          ("fep", 2),
          ("slot1", 3),
          ("slot11", 11),
          ("slot12", 12),
          ("slot13", 13),
          ("slot14", 14),
          ("slot15", 15),
          ("slot16", 16),
          ("slot17", 17),
          ("slot18", 18),
          ("slot2", 4),
          ("slot3", 5),
          ("slot4", 6),
          ("slot5", 7),
          ("slot6", 8),
          ("slot7", 9),
          ("slot8", 10))
    )


_MemoryStatsTableSlotNumber_Type.__name__ = "Integer32"
_MemoryStatsTableSlotNumber_Object = MibTableColumn
memoryStatsTableSlotNumber = _MemoryStatsTableSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3605, 1, 1),
    _MemoryStatsTableSlotNumber_Type()
)
memoryStatsTableSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryStatsTableSlotNumber.setStatus("current")


class _MemoryStatsTableCardType_Type(Integer32):
    """Custom type memoryStatsTableCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dAC", 2),
          ("mAC", 3),
          ("sCC", 1),
          ("unk", 0))
    )


_MemoryStatsTableCardType_Type.__name__ = "Integer32"
_MemoryStatsTableCardType_Object = MibTableColumn
memoryStatsTableCardType = _MemoryStatsTableCardType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3605, 1, 2),
    _MemoryStatsTableCardType_Type()
)
memoryStatsTableCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryStatsTableCardType.setStatus("current")
_MemoryStatsTableCPUNumber_Type = Integer32
_MemoryStatsTableCPUNumber_Object = MibTableColumn
memoryStatsTableCPUNumber = _MemoryStatsTableCPUNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3605, 1, 3),
    _MemoryStatsTableCPUNumber_Type()
)
memoryStatsTableCPUNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryStatsTableCPUNumber.setStatus("current")
_MemoryStatsTableTotalSize_Type = Integer32
_MemoryStatsTableTotalSize_Object = MibTableColumn
memoryStatsTableTotalSize = _MemoryStatsTableTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3605, 1, 101),
    _MemoryStatsTableTotalSize_Type()
)
memoryStatsTableTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryStatsTableTotalSize.setStatus("current")
_MemoryStatsTableManagedSize_Type = Integer32
_MemoryStatsTableManagedSize_Object = MibTableColumn
memoryStatsTableManagedSize = _MemoryStatsTableManagedSize_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3605, 1, 102),
    _MemoryStatsTableManagedSize_Type()
)
memoryStatsTableManagedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryStatsTableManagedSize.setStatus("current")
_MemoryStatsTableFreeSize_Type = Integer32
_MemoryStatsTableFreeSize_Object = MibTableColumn
memoryStatsTableFreeSize = _MemoryStatsTableFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3605, 1, 201),
    _MemoryStatsTableFreeSize_Type()
)
memoryStatsTableFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryStatsTableFreeSize.setStatus("current")
_MemoryStatsTableFreeBlockCount_Type = Integer32
_MemoryStatsTableFreeBlockCount_Object = MibTableColumn
memoryStatsTableFreeBlockCount = _MemoryStatsTableFreeBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3605, 1, 202),
    _MemoryStatsTableFreeBlockCount_Type()
)
memoryStatsTableFreeBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryStatsTableFreeBlockCount.setStatus("current")
_MemoryStatsTableFreeLargestBlock_Type = Integer32
_MemoryStatsTableFreeLargestBlock_Object = MibTableColumn
memoryStatsTableFreeLargestBlock = _MemoryStatsTableFreeLargestBlock_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3605, 1, 203),
    _MemoryStatsTableFreeLargestBlock_Type()
)
memoryStatsTableFreeLargestBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryStatsTableFreeLargestBlock.setStatus("current")
_MemoryStatsTableFreeSmallestBlock_Type = Integer32
_MemoryStatsTableFreeSmallestBlock_Object = MibTableColumn
memoryStatsTableFreeSmallestBlock = _MemoryStatsTableFreeSmallestBlock_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3605, 1, 204),
    _MemoryStatsTableFreeSmallestBlock_Type()
)
memoryStatsTableFreeSmallestBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryStatsTableFreeSmallestBlock.setStatus("current")
_MemoryStatsTableUsedSize_Type = Integer32
_MemoryStatsTableUsedSize_Object = MibTableColumn
memoryStatsTableUsedSize = _MemoryStatsTableUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3605, 1, 301),
    _MemoryStatsTableUsedSize_Type()
)
memoryStatsTableUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryStatsTableUsedSize.setStatus("current")
_MemoryStatsTableUsedBlockCount_Type = Integer32
_MemoryStatsTableUsedBlockCount_Object = MibTableColumn
memoryStatsTableUsedBlockCount = _MemoryStatsTableUsedBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3605, 1, 302),
    _MemoryStatsTableUsedBlockCount_Type()
)
memoryStatsTableUsedBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryStatsTableUsedBlockCount.setStatus("current")
_MemoryStatsTableUsedLargestBlock_Type = Integer32
_MemoryStatsTableUsedLargestBlock_Object = MibTableColumn
memoryStatsTableUsedLargestBlock = _MemoryStatsTableUsedLargestBlock_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3605, 1, 303),
    _MemoryStatsTableUsedLargestBlock_Type()
)
memoryStatsTableUsedLargestBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryStatsTableUsedLargestBlock.setStatus("current")
_MemoryStatsTableUsedSmallestBlock_Type = Integer32
_MemoryStatsTableUsedSmallestBlock_Object = MibTableColumn
memoryStatsTableUsedSmallestBlock = _MemoryStatsTableUsedSmallestBlock_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3605, 1, 304),
    _MemoryStatsTableUsedSmallestBlock_Type()
)
memoryStatsTableUsedSmallestBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryStatsTableUsedSmallestBlock.setStatus("current")
_MemoryStatsTableAllocSuccesses_Type = Integer32
_MemoryStatsTableAllocSuccesses_Object = MibTableColumn
memoryStatsTableAllocSuccesses = _MemoryStatsTableAllocSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3605, 1, 401),
    _MemoryStatsTableAllocSuccesses_Type()
)
memoryStatsTableAllocSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryStatsTableAllocSuccesses.setStatus("current")
_MemoryStatsTableAllocFails_Type = Integer32
_MemoryStatsTableAllocFails_Object = MibTableColumn
memoryStatsTableAllocFails = _MemoryStatsTableAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3605, 1, 402),
    _MemoryStatsTableAllocFails_Type()
)
memoryStatsTableAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryStatsTableAllocFails.setStatus("current")
_MemoryStatsTableFreeSuccesses_Type = Integer32
_MemoryStatsTableFreeSuccesses_Object = MibTableColumn
memoryStatsTableFreeSuccesses = _MemoryStatsTableFreeSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3605, 1, 403),
    _MemoryStatsTableFreeSuccesses_Type()
)
memoryStatsTableFreeSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryStatsTableFreeSuccesses.setStatus("current")
_MemoryStatsTableFreeFails_Type = Integer32
_MemoryStatsTableFreeFails_Object = MibTableColumn
memoryStatsTableFreeFails = _MemoryStatsTableFreeFails_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3605, 1, 404),
    _MemoryStatsTableFreeFails_Type()
)
memoryStatsTableFreeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryStatsTableFreeFails.setStatus("current")
_TaskStatsTableTable_Object = MibTable
taskStatsTableTable = _TaskStatsTableTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606)
)
if mibBuilder.loadTexts:
    taskStatsTableTable.setStatus("current")
_TaskStatsTableEntry_Object = MibTableRow
taskStatsTableEntry = _TaskStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1)
)
taskStatsTableEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "taskStatsTableSlotNumber"),
    (0, "APTIS-MONITOR-MIB", "taskStatsTableTaskIndex"),
)
if mibBuilder.loadTexts:
    taskStatsTableEntry.setStatus("current")


class _TaskStatsTableSlotNumber_Type(Integer32):
    """Custom type taskStatsTableSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("bep", 1),
          ("fep", 2),
          ("slot1", 3),
          ("slot11", 11),
          ("slot12", 12),
          ("slot13", 13),
          ("slot14", 14),
          ("slot15", 15),
          ("slot16", 16),
          ("slot17", 17),
          ("slot18", 18),
          ("slot2", 4),
          ("slot3", 5),
          ("slot4", 6),
          ("slot5", 7),
          ("slot6", 8),
          ("slot7", 9),
          ("slot8", 10))
    )


_TaskStatsTableSlotNumber_Type.__name__ = "Integer32"
_TaskStatsTableSlotNumber_Object = MibTableColumn
taskStatsTableSlotNumber = _TaskStatsTableSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 1),
    _TaskStatsTableSlotNumber_Type()
)
taskStatsTableSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableSlotNumber.setStatus("current")
_TaskStatsTableTaskIndex_Type = Integer32
_TaskStatsTableTaskIndex_Object = MibTableColumn
taskStatsTableTaskIndex = _TaskStatsTableTaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 2),
    _TaskStatsTableTaskIndex_Type()
)
taskStatsTableTaskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableTaskIndex.setStatus("current")
_TaskStatsTableTaskID_Type = Integer32
_TaskStatsTableTaskID_Object = MibTableColumn
taskStatsTableTaskID = _TaskStatsTableTaskID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 3),
    _TaskStatsTableTaskID_Type()
)
taskStatsTableTaskID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableTaskID.setStatus("current")


class _TaskStatsTableTaskName_Type(DisplayString):
    """Custom type taskStatsTableTaskName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TaskStatsTableTaskName_Type.__name__ = "DisplayString"
_TaskStatsTableTaskName_Object = MibTableColumn
taskStatsTableTaskName = _TaskStatsTableTaskName_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 4),
    _TaskStatsTableTaskName_Type()
)
taskStatsTableTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableTaskName.setStatus("current")
_TaskStatsTableTCBSize_Type = Integer32
_TaskStatsTableTCBSize_Object = MibTableColumn
taskStatsTableTCBSize = _TaskStatsTableTCBSize_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 11),
    _TaskStatsTableTCBSize_Type()
)
taskStatsTableTCBSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableTCBSize.setStatus("current")


class _TaskStatsTableTCB_Type(OctetString):
    """Custom type taskStatsTableTCB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_TaskStatsTableTCB_Type.__name__ = "OctetString"
_TaskStatsTableTCB_Object = MibTableColumn
taskStatsTableTCB = _TaskStatsTableTCB_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 12),
    _TaskStatsTableTCB_Type()
)
taskStatsTableTCB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableTCB.setStatus("current")


class _TaskStatsTableWaitObjectName_Type(DisplayString):
    """Custom type taskStatsTableWaitObjectName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TaskStatsTableWaitObjectName_Type.__name__ = "DisplayString"
_TaskStatsTableWaitObjectName_Object = MibTableColumn
taskStatsTableWaitObjectName = _TaskStatsTableWaitObjectName_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 21),
    _TaskStatsTableWaitObjectName_Type()
)
taskStatsTableWaitObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableWaitObjectName.setStatus("current")
_TaskStatsTableTicksPerSecond_Type = Integer32
_TaskStatsTableTicksPerSecond_Object = MibTableColumn
taskStatsTableTicksPerSecond = _TaskStatsTableTicksPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 22),
    _TaskStatsTableTicksPerSecond_Type()
)
taskStatsTableTicksPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableTicksPerSecond.setStatus("current")
_TaskStatsTableTicksElapsed_Type = Integer32
_TaskStatsTableTicksElapsed_Object = MibTableColumn
taskStatsTableTicksElapsed = _TaskStatsTableTicksElapsed_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 23),
    _TaskStatsTableTicksElapsed_Type()
)
taskStatsTableTicksElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableTicksElapsed.setStatus("current")
_TaskStatsTableStackAddress1_Type = Integer32
_TaskStatsTableStackAddress1_Object = MibTableColumn
taskStatsTableStackAddress1 = _TaskStatsTableStackAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 31),
    _TaskStatsTableStackAddress1_Type()
)
taskStatsTableStackAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableStackAddress1.setStatus("current")
_TaskStatsTableStackAddress2_Type = Integer32
_TaskStatsTableStackAddress2_Object = MibTableColumn
taskStatsTableStackAddress2 = _TaskStatsTableStackAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 32),
    _TaskStatsTableStackAddress2_Type()
)
taskStatsTableStackAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableStackAddress2.setStatus("current")
_TaskStatsTableStackAddress3_Type = Integer32
_TaskStatsTableStackAddress3_Object = MibTableColumn
taskStatsTableStackAddress3 = _TaskStatsTableStackAddress3_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 33),
    _TaskStatsTableStackAddress3_Type()
)
taskStatsTableStackAddress3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableStackAddress3.setStatus("current")
_TaskStatsTableStackAddress4_Type = Integer32
_TaskStatsTableStackAddress4_Object = MibTableColumn
taskStatsTableStackAddress4 = _TaskStatsTableStackAddress4_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 34),
    _TaskStatsTableStackAddress4_Type()
)
taskStatsTableStackAddress4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableStackAddress4.setStatus("current")
_TaskStatsTableStackAddress5_Type = Integer32
_TaskStatsTableStackAddress5_Object = MibTableColumn
taskStatsTableStackAddress5 = _TaskStatsTableStackAddress5_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 35),
    _TaskStatsTableStackAddress5_Type()
)
taskStatsTableStackAddress5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableStackAddress5.setStatus("current")
_TaskStatsTableStackAddress6_Type = Integer32
_TaskStatsTableStackAddress6_Object = MibTableColumn
taskStatsTableStackAddress6 = _TaskStatsTableStackAddress6_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 36),
    _TaskStatsTableStackAddress6_Type()
)
taskStatsTableStackAddress6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableStackAddress6.setStatus("current")
_TaskStatsTableStackAddress7_Type = Integer32
_TaskStatsTableStackAddress7_Object = MibTableColumn
taskStatsTableStackAddress7 = _TaskStatsTableStackAddress7_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 37),
    _TaskStatsTableStackAddress7_Type()
)
taskStatsTableStackAddress7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableStackAddress7.setStatus("current")
_TaskStatsTableStackAddress8_Type = Integer32
_TaskStatsTableStackAddress8_Object = MibTableColumn
taskStatsTableStackAddress8 = _TaskStatsTableStackAddress8_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 38),
    _TaskStatsTableStackAddress8_Type()
)
taskStatsTableStackAddress8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableStackAddress8.setStatus("current")
_TaskStatsTableStackAddress9_Type = Integer32
_TaskStatsTableStackAddress9_Object = MibTableColumn
taskStatsTableStackAddress9 = _TaskStatsTableStackAddress9_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 39),
    _TaskStatsTableStackAddress9_Type()
)
taskStatsTableStackAddress9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableStackAddress9.setStatus("current")
_TaskStatsTableStackAddress10_Type = Integer32
_TaskStatsTableStackAddress10_Object = MibTableColumn
taskStatsTableStackAddress10 = _TaskStatsTableStackAddress10_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 40),
    _TaskStatsTableStackAddress10_Type()
)
taskStatsTableStackAddress10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableStackAddress10.setStatus("current")
_TaskStatsTableRunTime_Type = Integer32
_TaskStatsTableRunTime_Object = MibTableColumn
taskStatsTableRunTime = _TaskStatsTableRunTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 41),
    _TaskStatsTableRunTime_Type()
)
taskStatsTableRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableRunTime.setStatus("current")
_TaskStatsTableContextSwitches_Type = Integer32
_TaskStatsTableContextSwitches_Object = MibTableColumn
taskStatsTableContextSwitches = _TaskStatsTableContextSwitches_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 42),
    _TaskStatsTableContextSwitches_Type()
)
taskStatsTableContextSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableContextSwitches.setStatus("current")
_TaskStatsTableGlobalPool_Type = Integer32
_TaskStatsTableGlobalPool_Object = MibTableColumn
taskStatsTableGlobalPool = _TaskStatsTableGlobalPool_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 43),
    _TaskStatsTableGlobalPool_Type()
)
taskStatsTableGlobalPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableGlobalPool.setStatus("current")
_TaskStatsTableIntervalTime_Type = Integer32
_TaskStatsTableIntervalTime_Object = MibTableColumn
taskStatsTableIntervalTime = _TaskStatsTableIntervalTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 44),
    _TaskStatsTableIntervalTime_Type()
)
taskStatsTableIntervalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableIntervalTime.setStatus("current")
_TaskStatsTableTotalTime_Type = Integer32
_TaskStatsTableTotalTime_Object = MibTableColumn
taskStatsTableTotalTime = _TaskStatsTableTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 45),
    _TaskStatsTableTotalTime_Type()
)
taskStatsTableTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableTotalTime.setStatus("current")
_TaskStatsTableIntervalSize_Type = Integer32
_TaskStatsTableIntervalSize_Object = MibTableColumn
taskStatsTableIntervalSize = _TaskStatsTableIntervalSize_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 46),
    _TaskStatsTableIntervalSize_Type()
)
taskStatsTableIntervalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableIntervalSize.setStatus("current")
_TaskStatsTableKernelPool_Type = Integer32
_TaskStatsTableKernelPool_Object = MibTableColumn
taskStatsTableKernelPool = _TaskStatsTableKernelPool_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 47),
    _TaskStatsTableKernelPool_Type()
)
taskStatsTableKernelPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableKernelPool.setStatus("current")
_TaskStatsTableTaskPool_Type = Integer32
_TaskStatsTableTaskPool_Object = MibTableColumn
taskStatsTableTaskPool = _TaskStatsTableTaskPool_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 48),
    _TaskStatsTableTaskPool_Type()
)
taskStatsTableTaskPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableTaskPool.setStatus("current")


class _TaskStatsTableIsrTimes_Type(DisplayString):
    """Custom type taskStatsTableIsrTimes based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TaskStatsTableIsrTimes_Type.__name__ = "DisplayString"
_TaskStatsTableIsrTimes_Object = MibTableColumn
taskStatsTableIsrTimes = _TaskStatsTableIsrTimes_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 49),
    _TaskStatsTableIsrTimes_Type()
)
taskStatsTableIsrTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableIsrTimes.setStatus("current")
_TaskStatsTableIdle5Seconds_Type = Integer32
_TaskStatsTableIdle5Seconds_Object = MibTableColumn
taskStatsTableIdle5Seconds = _TaskStatsTableIdle5Seconds_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 50),
    _TaskStatsTableIdle5Seconds_Type()
)
taskStatsTableIdle5Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableIdle5Seconds.setStatus("current")
_TaskStatsTableIdleMinute_Type = Integer32
_TaskStatsTableIdleMinute_Object = MibTableColumn
taskStatsTableIdleMinute = _TaskStatsTableIdleMinute_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 51),
    _TaskStatsTableIdleMinute_Type()
)
taskStatsTableIdleMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableIdleMinute.setStatus("current")
_TaskStatsTableIdle5Minute_Type = Integer32
_TaskStatsTableIdle5Minute_Object = MibTableColumn
taskStatsTableIdle5Minute = _TaskStatsTableIdle5Minute_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 52),
    _TaskStatsTableIdle5Minute_Type()
)
taskStatsTableIdle5Minute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableIdle5Minute.setStatus("current")
_TaskStatsTableIdleHour_Type = Integer32
_TaskStatsTableIdleHour_Object = MibTableColumn
taskStatsTableIdleHour = _TaskStatsTableIdleHour_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 53),
    _TaskStatsTableIdleHour_Type()
)
taskStatsTableIdleHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableIdleHour.setStatus("current")
_TaskStatsTableIdleDay_Type = Integer32
_TaskStatsTableIdleDay_Object = MibTableColumn
taskStatsTableIdleDay = _TaskStatsTableIdleDay_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3606, 1, 54),
    _TaskStatsTableIdleDay_Type()
)
taskStatsTableIdleDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatsTableIdleDay.setStatus("current")
_IpstatRouteEntryTable_Object = MibTable
ipstatRouteEntryTable = _IpstatRouteEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3701)
)
if mibBuilder.loadTexts:
    ipstatRouteEntryTable.setStatus("current")
_IpstatRouteEntryEntry_Object = MibTableRow
ipstatRouteEntryEntry = _IpstatRouteEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3701, 1)
)
ipstatRouteEntryEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "ipstatRouteEntryPrevXxrt"),
)
if mibBuilder.loadTexts:
    ipstatRouteEntryEntry.setStatus("current")
_IpstatRouteEntryPrevXxrt_Type = Integer32
_IpstatRouteEntryPrevXxrt_Object = MibTableColumn
ipstatRouteEntryPrevXxrt = _IpstatRouteEntryPrevXxrt_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3701, 1, 1),
    _IpstatRouteEntryPrevXxrt_Type()
)
ipstatRouteEntryPrevXxrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstatRouteEntryPrevXxrt.setStatus("current")
_IpstatRouteEntryNextIprt_Type = Integer32
_IpstatRouteEntryNextIprt_Object = MibTableColumn
ipstatRouteEntryNextIprt = _IpstatRouteEntryNextIprt_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3701, 1, 2),
    _IpstatRouteEntryNextIprt_Type()
)
ipstatRouteEntryNextIprt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstatRouteEntryNextIprt.setStatus("current")
_IpstatRouteEntryPrevIndex_Type = Integer32
_IpstatRouteEntryPrevIndex_Object = MibTableColumn
ipstatRouteEntryPrevIndex = _IpstatRouteEntryPrevIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3701, 1, 3),
    _IpstatRouteEntryPrevIndex_Type()
)
ipstatRouteEntryPrevIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstatRouteEntryPrevIndex.setStatus("current")
_IpstatRouteEntryGenNumber_Type = Integer32
_IpstatRouteEntryGenNumber_Object = MibTableColumn
ipstatRouteEntryGenNumber = _IpstatRouteEntryGenNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3701, 1, 4),
    _IpstatRouteEntryGenNumber_Type()
)
ipstatRouteEntryGenNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstatRouteEntryGenNumber.setStatus("current")
_IpstatRouteEntryNextIprtIndex_Type = Integer32
_IpstatRouteEntryNextIprtIndex_Object = MibTableColumn
ipstatRouteEntryNextIprtIndex = _IpstatRouteEntryNextIprtIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3701, 1, 5),
    _IpstatRouteEntryNextIprtIndex_Type()
)
ipstatRouteEntryNextIprtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstatRouteEntryNextIprtIndex.setStatus("current")
_IpstatRouteEntryIpAddress_Type = IpAddress
_IpstatRouteEntryIpAddress_Object = MibTableColumn
ipstatRouteEntryIpAddress = _IpstatRouteEntryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3701, 1, 6),
    _IpstatRouteEntryIpAddress_Type()
)
ipstatRouteEntryIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstatRouteEntryIpAddress.setStatus("current")
_IpstatRouteEntryIpMask_Type = Integer32
_IpstatRouteEntryIpMask_Object = MibTableColumn
ipstatRouteEntryIpMask = _IpstatRouteEntryIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3701, 1, 7),
    _IpstatRouteEntryIpMask_Type()
)
ipstatRouteEntryIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstatRouteEntryIpMask.setStatus("current")
_IpstatRouteEntryCircuitId_Type = Integer32
_IpstatRouteEntryCircuitId_Object = MibTableColumn
ipstatRouteEntryCircuitId = _IpstatRouteEntryCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3701, 1, 8),
    _IpstatRouteEntryCircuitId_Type()
)
ipstatRouteEntryCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstatRouteEntryCircuitId.setStatus("current")
_IpstatRouteEntryTYPE_Type = Integer32
_IpstatRouteEntryTYPE_Object = MibTableColumn
ipstatRouteEntryTYPE = _IpstatRouteEntryTYPE_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3701, 1, 9),
    _IpstatRouteEntryTYPE_Type()
)
ipstatRouteEntryTYPE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstatRouteEntryTYPE.setStatus("current")
_IpstatRouteEntryOwner_Type = Integer32
_IpstatRouteEntryOwner_Object = MibTableColumn
ipstatRouteEntryOwner = _IpstatRouteEntryOwner_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3701, 1, 10),
    _IpstatRouteEntryOwner_Type()
)
ipstatRouteEntryOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstatRouteEntryOwner.setStatus("current")


class _IpstatRouteEntryPathAndCost_Type(OctetString):
    """Custom type ipstatRouteEntryPathAndCost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_IpstatRouteEntryPathAndCost_Type.__name__ = "OctetString"
_IpstatRouteEntryPathAndCost_Object = MibTableColumn
ipstatRouteEntryPathAndCost = _IpstatRouteEntryPathAndCost_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3701, 1, 11),
    _IpstatRouteEntryPathAndCost_Type()
)
ipstatRouteEntryPathAndCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstatRouteEntryPathAndCost.setStatus("current")
_IpstatRouteEntryTrig_Type = Integer32
_IpstatRouteEntryTrig_Object = MibTableColumn
ipstatRouteEntryTrig = _IpstatRouteEntryTrig_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3701, 1, 12),
    _IpstatRouteEntryTrig_Type()
)
ipstatRouteEntryTrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstatRouteEntryTrig.setStatus("current")
_IpstatRouteEntryTag_Type = Integer32
_IpstatRouteEntryTag_Object = MibTableColumn
ipstatRouteEntryTag = _IpstatRouteEntryTag_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3701, 1, 13),
    _IpstatRouteEntryTag_Type()
)
ipstatRouteEntryTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstatRouteEntryTag.setStatus("current")
_IpstatRouteEntryPrivate_Type = Integer32
_IpstatRouteEntryPrivate_Object = MibTableColumn
ipstatRouteEntryPrivate = _IpstatRouteEntryPrivate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3701, 1, 14),
    _IpstatRouteEntryPrivate_Type()
)
ipstatRouteEntryPrivate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstatRouteEntryPrivate.setStatus("current")


class _IpstatRouteEntryPathType_Type(Integer32):
    """Custom type ipstatRouteEntryPathType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mpath", 1),
          ("simple", 2))
    )


_IpstatRouteEntryPathType_Type.__name__ = "Integer32"
_IpstatRouteEntryPathType_Object = MibTableColumn
ipstatRouteEntryPathType = _IpstatRouteEntryPathType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3701, 1, 15),
    _IpstatRouteEntryPathType_Type()
)
ipstatRouteEntryPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstatRouteEntryPathType.setStatus("current")
_IpstatRouteEntryCost_Type = Integer32
_IpstatRouteEntryCost_Object = MibTableColumn
ipstatRouteEntryCost = _IpstatRouteEntryCost_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3701, 1, 16),
    _IpstatRouteEntryCost_Type()
)
ipstatRouteEntryCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstatRouteEntryCost.setStatus("current")
_IpstatIgmpEntryTable_Object = MibTable
ipstatIgmpEntryTable = _IpstatIgmpEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3801)
)
if mibBuilder.loadTexts:
    ipstatIgmpEntryTable.setStatus("current")
_IpstatIgmpEntryEntry_Object = MibTableRow
ipstatIgmpEntryEntry = _IpstatIgmpEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3801, 1)
)
ipstatIgmpEntryEntry.setIndexNames(
    (0, "APTIS-MONITOR-MIB", "ipstatIgmpEntryIPAddress"),
)
if mibBuilder.loadTexts:
    ipstatIgmpEntryEntry.setStatus("current")
_IpstatIgmpEntryIPAddress_Type = IpAddress
_IpstatIgmpEntryIPAddress_Object = MibTableColumn
ipstatIgmpEntryIPAddress = _IpstatIgmpEntryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3801, 1, 1),
    _IpstatIgmpEntryIPAddress_Type()
)
ipstatIgmpEntryIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstatIgmpEntryIPAddress.setStatus("current")
_IpstatIgmpEntryIPAddrfrom_Type = IpAddress
_IpstatIgmpEntryIPAddrfrom_Object = MibTableColumn
ipstatIgmpEntryIPAddrfrom = _IpstatIgmpEntryIPAddrfrom_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3801, 1, 2),
    _IpstatIgmpEntryIPAddrfrom_Type()
)
ipstatIgmpEntryIPAddrfrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstatIgmpEntryIPAddrfrom.setStatus("current")
_IpstatIgmpEntryCliId_Type = Integer32
_IpstatIgmpEntryCliId_Object = MibTableColumn
ipstatIgmpEntryCliId = _IpstatIgmpEntryCliId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3801, 1, 3),
    _IpstatIgmpEntryCliId_Type()
)
ipstatIgmpEntryCliId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstatIgmpEntryCliId.setStatus("current")
_IpstatIgmpEntryTimeout_Type = Integer32
_IpstatIgmpEntryTimeout_Object = MibTableColumn
ipstatIgmpEntryTimeout = _IpstatIgmpEntryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3801, 1, 4),
    _IpstatIgmpEntryTimeout_Type()
)
ipstatIgmpEntryTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstatIgmpEntryTimeout.setStatus("current")
_IpstatIgmpEntryCount_Type = Integer32
_IpstatIgmpEntryCount_Object = MibTableColumn
ipstatIgmpEntryCount = _IpstatIgmpEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3801, 1, 5),
    _IpstatIgmpEntryCount_Type()
)
ipstatIgmpEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstatIgmpEntryCount.setStatus("current")


class _IpstatIgmpEntryState_Type(Integer32):
    """Custom type ipstatIgmpEntryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("check", 3),
          ("mem", 4),
          ("nomem", 1),
          ("v1mem", 2))
    )


_IpstatIgmpEntryState_Type.__name__ = "Integer32"
_IpstatIgmpEntryState_Object = MibTableColumn
ipstatIgmpEntryState = _IpstatIgmpEntryState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2, 3801, 1, 6),
    _IpstatIgmpEntryState_Type()
)
ipstatIgmpEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstatIgmpEntryState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APTIS-MONITOR-MIB",
    **{"aptisMonitorModule": aptisMonitorModule,
       "systemSummaryTable": systemSummaryTable,
       "systemSummaryEntry": systemSummaryEntry,
       "systemSummaryData": systemSummaryData,
       "powerStatusTable": powerStatusTable,
       "powerStatusEntry": powerStatusEntry,
       "powerStatusShelf": powerStatusShelf,
       "powerStatusFanStatus": powerStatusFanStatus,
       "powerStatusExternalDC1": powerStatusExternalDC1,
       "powerStatusExternalDC2": powerStatusExternalDC2,
       "powerStatusInternalAC1": powerStatusInternalAC1,
       "powerStatusInternalAC2": powerStatusInternalAC2,
       "powerStatusInternalACDC1": powerStatusInternalACDC1,
       "powerStatusInternalACDC2": powerStatusInternalACDC2,
       "powerStatusInternalACDC3": powerStatusInternalACDC3,
       "powerStatusCsr1Register": powerStatusCsr1Register,
       "softwareVersionTable": softwareVersionTable,
       "softwareVersionEntry": softwareVersionEntry,
       "softwareVersionMibVersion": softwareVersionMibVersion,
       "softwareVersionSoftwareRevision": softwareVersionSoftwareRevision,
       "softwareVersionProductId": softwareVersionProductId,
       "softwareVersionMibRevision": softwareVersionMibRevision,
       "systemTimeTable": systemTimeTable,
       "systemTimeEntry": systemTimeEntry,
       "systemTimeFixedBootTime": systemTimeFixedBootTime,
       "systemTimeUTCOffset": systemTimeUTCOffset,
       "systemTimeUpTime": systemTimeUpTime,
       "sessionCountersTable": sessionCountersTable,
       "sessionCountersEntry": sessionCountersEntry,
       "sessionCountersActiveLowest": sessionCountersActiveLowest,
       "sessionCountersActiveHighest": sessionCountersActiveHighest,
       "sessionCountersActiveCount": sessionCountersActiveCount,
       "sessionCountersInactiveLowest": sessionCountersInactiveLowest,
       "sessionCountersInactiveHighest": sessionCountersInactiveHighest,
       "sessionCountersInactiveCount": sessionCountersInactiveCount,
       "sessionCountersSessionTableSize": sessionCountersSessionTableSize,
       "sessionCountersHistoryLowest": sessionCountersHistoryLowest,
       "sessionCountersHistoryHighest": sessionCountersHistoryHighest,
       "sessionCountersBootEra": sessionCountersBootEra,
       "sessionCountersHistoryTableSize": sessionCountersHistoryTableSize,
       "sessionStatusTable": sessionStatusTable,
       "sessionStatusEntry": sessionStatusEntry,
       "sessionStatusSessionID": sessionStatusSessionID,
       "sessionStatusState": sessionStatusState,
       "sessionStatusPermanentFlag": sessionStatusPermanentFlag,
       "sessionStatusVpopId": sessionStatusVpopId,
       "sessionStatusName": sessionStatusName,
       "sessionStatusRemoteIP": sessionStatusRemoteIP,
       "sessionStatusRemoteIPMask": sessionStatusRemoteIPMask,
       "sessionStatusLocalIP": sessionStatusLocalIP,
       "sessionStatusLocalIPMask": sessionStatusLocalIPMask,
       "sessionStatusLinkService": sessionStatusLinkService,
       "sessionStatusServiceMode": sessionStatusServiceMode,
       "sessionStatusStartTime": sessionStatusStartTime,
       "sessionStatusStopTime": sessionStatusStopTime,
       "sessionStatusTimeOfModemSync": sessionStatusTimeOfModemSync,
       "sessionStatusTimeOfService": sessionStatusTimeOfService,
       "sessionStatusTerminatingComponent": sessionStatusTerminatingComponent,
       "sessionStatusTerminationCause": sessionStatusTerminationCause,
       "sessionStatusLastComponent": sessionStatusLastComponent,
       "sessionStatusLayer1Slot": sessionStatusLayer1Slot,
       "sessionStatusLayer2Slot": sessionStatusLayer2Slot,
       "sessionStatusCalledNumber": sessionStatusCalledNumber,
       "sessionStatusCallingNumber": sessionStatusCallingNumber,
       "sessionStatusOriginateMode": sessionStatusOriginateMode,
       "sessionStatusOctetsIn": sessionStatusOctetsIn,
       "sessionStatusOctetsOut": sessionStatusOctetsOut,
       "sessionStatusPacketsIn": sessionStatusPacketsIn,
       "sessionStatusPacketsOut": sessionStatusPacketsOut,
       "sessionStatusMultiLinkId": sessionStatusMultiLinkId,
       "sessionStatusPort": sessionStatusPort,
       "sessionStatusTimeslot": sessionStatusTimeslot,
       "sessionStatusLinkCount": sessionStatusLinkCount,
       "sessionStatusTxStartDataRate": sessionStatusTxStartDataRate,
       "sessionStatusRxStartDataRate": sessionStatusRxStartDataRate,
       "sessionStatusTxEndDataRate": sessionStatusTxEndDataRate,
       "sessionStatusRxEndDataRate": sessionStatusRxEndDataRate,
       "sessionStatusTxMinDataRate": sessionStatusTxMinDataRate,
       "sessionStatusRxMinDataRate": sessionStatusRxMinDataRate,
       "sessionStatusTxMaxDataRate": sessionStatusTxMaxDataRate,
       "sessionStatusRxMaxDataRate": sessionStatusRxMaxDataRate,
       "sessionStatusIop": sessionStatusIop,
       "sessionStatusDmm": sessionStatusDmm,
       "sessionStatusPack": sessionStatusPack,
       "sessionStatusDevice": sessionStatusDevice,
       "sessionStatusTdmStream": sessionStatusTdmStream,
       "sessionStatusTdmTimeSlot": sessionStatusTdmTimeSlot,
       "sessionStatusTerminationReason": sessionStatusTerminationReason,
       "sessionStatusDuration": sessionStatusDuration,
       "sessionStatusDurationHMS": sessionStatusDurationHMS,
       "sessionStatusSs7SessionId": sessionStatusSs7SessionId,
       "sessionStatusModemNumber": sessionStatusModemNumber,
       "sessionStatusTunnelType": sessionStatusTunnelType,
       "sessionStatusTunnelMediumType": sessionStatusTunnelMediumType,
       "sessionStatusTunnelServerAddress": sessionStatusTunnelServerAddress,
       "sessionStatusCallClass": sessionStatusCallClass,
       "sessionStatusTandemPort": sessionStatusTandemPort,
       "sessionStatusTandemTimeslot": sessionStatusTandemTimeslot,
       "sessionStatusCallClassArray": sessionStatusCallClassArray,
       "sessionStatusCallClassLen": sessionStatusCallClassLen,
       "sessionStatusActualAuthMethod": sessionStatusActualAuthMethod,
       "sessionStatusModemModulation": sessionStatusModemModulation,
       "sessionStatusModemErrorCorrection": sessionStatusModemErrorCorrection,
       "sessionStatusModemDataCompression": sessionStatusModemDataCompression,
       "sessionStatusModemTxBlocks": sessionStatusModemTxBlocks,
       "sessionStatusModemRetransmits": sessionStatusModemRetransmits,
       "sessionStatusModemSNR": sessionStatusModemSNR,
       "sessionStatusModemLocalRetrains": sessionStatusModemLocalRetrains,
       "sessionStatusModemRemoteRetrains": sessionStatusModemRemoteRetrains,
       "sessionStatusModemLocalRenegotiations": sessionStatusModemLocalRenegotiations,
       "sessionStatusModemRemoteRenegotiations": sessionStatusModemRemoteRenegotiations,
       "sessionStatusModemReceiveLineLevel": sessionStatusModemReceiveLineLevel,
       "sessionStatusRemoteIPXNetwork": sessionStatusRemoteIPXNetwork,
       "sessionStatusRemoteIPXNode": sessionStatusRemoteIPXNode,
       "sessionStatusCleartcpRemoteIP": sessionStatusCleartcpRemoteIP,
       "sessionStatusCleartcpRemotePort": sessionStatusCleartcpRemotePort,
       "sessionStatusTunnelId": sessionStatusTunnelId,
       "sessionStatusLinkId": sessionStatusLinkId,
       "sessionStatusActiveTable": sessionStatusActiveTable,
       "sessionStatusActiveEntry": sessionStatusActiveEntry,
       "sessionStatusActiveSessionID": sessionStatusActiveSessionID,
       "sessionStatusActiveState": sessionStatusActiveState,
       "sessionStatusActivePermanentFlag": sessionStatusActivePermanentFlag,
       "sessionStatusActiveVpopId": sessionStatusActiveVpopId,
       "sessionStatusActiveName": sessionStatusActiveName,
       "sessionStatusActiveRemoteIP": sessionStatusActiveRemoteIP,
       "sessionStatusActiveRemoteIPMask": sessionStatusActiveRemoteIPMask,
       "sessionStatusActiveLocalIP": sessionStatusActiveLocalIP,
       "sessionStatusActiveLocalIPMask": sessionStatusActiveLocalIPMask,
       "sessionStatusActiveLinkService": sessionStatusActiveLinkService,
       "sessionStatusActiveServiceMode": sessionStatusActiveServiceMode,
       "sessionStatusActiveStartTime": sessionStatusActiveStartTime,
       "sessionStatusActiveStopTime": sessionStatusActiveStopTime,
       "sessionStatusActiveTimeOfModemSync": sessionStatusActiveTimeOfModemSync,
       "sessionStatusActiveTimeOfService": sessionStatusActiveTimeOfService,
       "sessionStatusActiveTerminatingComponent": sessionStatusActiveTerminatingComponent,
       "sessionStatusActiveTerminationCause": sessionStatusActiveTerminationCause,
       "sessionStatusActiveLastComponent": sessionStatusActiveLastComponent,
       "sessionStatusActiveLayer1Slot": sessionStatusActiveLayer1Slot,
       "sessionStatusActiveLayer2Slot": sessionStatusActiveLayer2Slot,
       "sessionStatusActiveCalledNumber": sessionStatusActiveCalledNumber,
       "sessionStatusActiveCallingNumber": sessionStatusActiveCallingNumber,
       "sessionStatusActiveOriginateMode": sessionStatusActiveOriginateMode,
       "sessionStatusActiveOctetsIn": sessionStatusActiveOctetsIn,
       "sessionStatusActiveOctetsOut": sessionStatusActiveOctetsOut,
       "sessionStatusActivePacketsIn": sessionStatusActivePacketsIn,
       "sessionStatusActivePacketsOut": sessionStatusActivePacketsOut,
       "sessionStatusActiveMultiLinkId": sessionStatusActiveMultiLinkId,
       "sessionStatusActivePort": sessionStatusActivePort,
       "sessionStatusActiveTimeslot": sessionStatusActiveTimeslot,
       "sessionStatusActiveLinkCount": sessionStatusActiveLinkCount,
       "sessionStatusActiveTxStartDataRate": sessionStatusActiveTxStartDataRate,
       "sessionStatusActiveRxStartDataRate": sessionStatusActiveRxStartDataRate,
       "sessionStatusActiveTxEndDataRate": sessionStatusActiveTxEndDataRate,
       "sessionStatusActiveRxEndDataRate": sessionStatusActiveRxEndDataRate,
       "sessionStatusActiveTxMinDataRate": sessionStatusActiveTxMinDataRate,
       "sessionStatusActiveRxMinDataRate": sessionStatusActiveRxMinDataRate,
       "sessionStatusActiveTxMaxDataRate": sessionStatusActiveTxMaxDataRate,
       "sessionStatusActiveRxMaxDataRate": sessionStatusActiveRxMaxDataRate,
       "sessionStatusActiveIop": sessionStatusActiveIop,
       "sessionStatusActiveDmm": sessionStatusActiveDmm,
       "sessionStatusActivePack": sessionStatusActivePack,
       "sessionStatusActiveDevice": sessionStatusActiveDevice,
       "sessionStatusActiveTdmStream": sessionStatusActiveTdmStream,
       "sessionStatusActiveTdmTimeSlot": sessionStatusActiveTdmTimeSlot,
       "sessionStatusActiveTerminationReason": sessionStatusActiveTerminationReason,
       "sessionStatusActiveDuration": sessionStatusActiveDuration,
       "sessionStatusActiveDurationHMS": sessionStatusActiveDurationHMS,
       "sessionStatusActiveSs7SessionId": sessionStatusActiveSs7SessionId,
       "sessionStatusActiveModemNumber": sessionStatusActiveModemNumber,
       "sessionStatusActiveTunnelType": sessionStatusActiveTunnelType,
       "sessionStatusActiveTunnelMediumType": sessionStatusActiveTunnelMediumType,
       "sessionStatusActiveTunnelServerAddress": sessionStatusActiveTunnelServerAddress,
       "sessionStatusActiveCallClass": sessionStatusActiveCallClass,
       "sessionStatusActiveTandemPort": sessionStatusActiveTandemPort,
       "sessionStatusActiveTandemTimeslot": sessionStatusActiveTandemTimeslot,
       "sessionStatusActiveCallClassArray": sessionStatusActiveCallClassArray,
       "sessionStatusActiveCallClassLen": sessionStatusActiveCallClassLen,
       "sessionStatusActiveActualAuthMethod": sessionStatusActiveActualAuthMethod,
       "sessionStatusActiveModemModulation": sessionStatusActiveModemModulation,
       "sessionStatusActiveModemErrorCorrection": sessionStatusActiveModemErrorCorrection,
       "sessionStatusActiveModemDataCompression": sessionStatusActiveModemDataCompression,
       "sessionStatusActiveModemTxBlocks": sessionStatusActiveModemTxBlocks,
       "sessionStatusActiveModemRetransmits": sessionStatusActiveModemRetransmits,
       "sessionStatusActiveModemSNR": sessionStatusActiveModemSNR,
       "sessionStatusActiveModemLocalRetrains": sessionStatusActiveModemLocalRetrains,
       "sessionStatusActiveModemRemoteRetrains": sessionStatusActiveModemRemoteRetrains,
       "sessionStatusActiveModemLocalRenegotiations": sessionStatusActiveModemLocalRenegotiations,
       "sessionStatusActiveModemRemoteRenegotiations": sessionStatusActiveModemRemoteRenegotiations,
       "sessionStatusActiveModemReceiveLineLevel": sessionStatusActiveModemReceiveLineLevel,
       "sessionStatusActiveRemoteIPXNetwork": sessionStatusActiveRemoteIPXNetwork,
       "sessionStatusActiveRemoteIPXNode": sessionStatusActiveRemoteIPXNode,
       "sessionStatusActiveCleartcpRemoteIP": sessionStatusActiveCleartcpRemoteIP,
       "sessionStatusActiveCleartcpRemotePort": sessionStatusActiveCleartcpRemotePort,
       "sessionStatusActiveTunnelId": sessionStatusActiveTunnelId,
       "sessionStatusActiveLinkId": sessionStatusActiveLinkId,
       "sessionStatusInactiveTable": sessionStatusInactiveTable,
       "sessionStatusInactiveEntry": sessionStatusInactiveEntry,
       "sessionStatusInactiveSessionID": sessionStatusInactiveSessionID,
       "sessionStatusInactiveState": sessionStatusInactiveState,
       "sessionStatusInactivePermanentFlag": sessionStatusInactivePermanentFlag,
       "sessionStatusInactiveVpopId": sessionStatusInactiveVpopId,
       "sessionStatusInactiveName": sessionStatusInactiveName,
       "sessionStatusInactiveRemoteIP": sessionStatusInactiveRemoteIP,
       "sessionStatusInactiveRemoteIPMask": sessionStatusInactiveRemoteIPMask,
       "sessionStatusInactiveLocalIP": sessionStatusInactiveLocalIP,
       "sessionStatusInactiveLocalIPMask": sessionStatusInactiveLocalIPMask,
       "sessionStatusInactiveLinkService": sessionStatusInactiveLinkService,
       "sessionStatusInactiveServiceMode": sessionStatusInactiveServiceMode,
       "sessionStatusInactiveStartTime": sessionStatusInactiveStartTime,
       "sessionStatusInactiveStopTime": sessionStatusInactiveStopTime,
       "sessionStatusInactiveTimeOfModemSync": sessionStatusInactiveTimeOfModemSync,
       "sessionStatusInactiveTimeOfService": sessionStatusInactiveTimeOfService,
       "sessionStatusInactiveTerminatingComponent": sessionStatusInactiveTerminatingComponent,
       "sessionStatusInactiveTerminationCause": sessionStatusInactiveTerminationCause,
       "sessionStatusInactiveLastComponent": sessionStatusInactiveLastComponent,
       "sessionStatusInactiveLayer1Slot": sessionStatusInactiveLayer1Slot,
       "sessionStatusInactiveLayer2Slot": sessionStatusInactiveLayer2Slot,
       "sessionStatusInactiveCalledNumber": sessionStatusInactiveCalledNumber,
       "sessionStatusInactiveCallingNumber": sessionStatusInactiveCallingNumber,
       "sessionStatusInactiveOriginateMode": sessionStatusInactiveOriginateMode,
       "sessionStatusInactiveOctetsIn": sessionStatusInactiveOctetsIn,
       "sessionStatusInactiveOctetsOut": sessionStatusInactiveOctetsOut,
       "sessionStatusInactivePacketsIn": sessionStatusInactivePacketsIn,
       "sessionStatusInactivePacketsOut": sessionStatusInactivePacketsOut,
       "sessionStatusInactiveMultiLinkId": sessionStatusInactiveMultiLinkId,
       "sessionStatusInactivePort": sessionStatusInactivePort,
       "sessionStatusInactiveTimeslot": sessionStatusInactiveTimeslot,
       "sessionStatusInactiveLinkCount": sessionStatusInactiveLinkCount,
       "sessionStatusInactiveTxStartDataRate": sessionStatusInactiveTxStartDataRate,
       "sessionStatusInactiveRxStartDataRate": sessionStatusInactiveRxStartDataRate,
       "sessionStatusInactiveTxEndDataRate": sessionStatusInactiveTxEndDataRate,
       "sessionStatusInactiveRxEndDataRate": sessionStatusInactiveRxEndDataRate,
       "sessionStatusInactiveTxMinDataRate": sessionStatusInactiveTxMinDataRate,
       "sessionStatusInactiveRxMinDataRate": sessionStatusInactiveRxMinDataRate,
       "sessionStatusInactiveTxMaxDataRate": sessionStatusInactiveTxMaxDataRate,
       "sessionStatusInactiveRxMaxDataRate": sessionStatusInactiveRxMaxDataRate,
       "sessionStatusInactiveIop": sessionStatusInactiveIop,
       "sessionStatusInactiveDmm": sessionStatusInactiveDmm,
       "sessionStatusInactivePack": sessionStatusInactivePack,
       "sessionStatusInactiveDevice": sessionStatusInactiveDevice,
       "sessionStatusInactiveTdmStream": sessionStatusInactiveTdmStream,
       "sessionStatusInactiveTdmTimeSlot": sessionStatusInactiveTdmTimeSlot,
       "sessionStatusInactiveTerminationReason": sessionStatusInactiveTerminationReason,
       "sessionStatusInactiveDuration": sessionStatusInactiveDuration,
       "sessionStatusInactiveDurationHMS": sessionStatusInactiveDurationHMS,
       "sessionStatusInactiveSs7SessionId": sessionStatusInactiveSs7SessionId,
       "sessionStatusInactiveModemNumber": sessionStatusInactiveModemNumber,
       "sessionStatusInactiveTunnelType": sessionStatusInactiveTunnelType,
       "sessionStatusInactiveTunnelMediumType": sessionStatusInactiveTunnelMediumType,
       "sessionStatusInactiveTunnelServerAddress": sessionStatusInactiveTunnelServerAddress,
       "sessionStatusInactiveCallClass": sessionStatusInactiveCallClass,
       "sessionStatusInactiveTandemPort": sessionStatusInactiveTandemPort,
       "sessionStatusInactiveTandemTimeslot": sessionStatusInactiveTandemTimeslot,
       "sessionStatusInactiveCallClassArray": sessionStatusInactiveCallClassArray,
       "sessionStatusInactiveCallClassLen": sessionStatusInactiveCallClassLen,
       "sessionStatusInactiveActualAuthMethod": sessionStatusInactiveActualAuthMethod,
       "sessionStatusInactiveModemModulation": sessionStatusInactiveModemModulation,
       "sessionStatusInactiveModemErrorCorrection": sessionStatusInactiveModemErrorCorrection,
       "sessionStatusInactiveModemDataCompression": sessionStatusInactiveModemDataCompression,
       "sessionStatusInactiveModemTxBlocks": sessionStatusInactiveModemTxBlocks,
       "sessionStatusInactiveModemRetransmits": sessionStatusInactiveModemRetransmits,
       "sessionStatusInactiveModemSNR": sessionStatusInactiveModemSNR,
       "sessionStatusInactiveModemLocalRetrains": sessionStatusInactiveModemLocalRetrains,
       "sessionStatusInactiveModemRemoteRetrains": sessionStatusInactiveModemRemoteRetrains,
       "sessionStatusInactiveModemLocalRenegotiations": sessionStatusInactiveModemLocalRenegotiations,
       "sessionStatusInactiveModemRemoteRenegotiations": sessionStatusInactiveModemRemoteRenegotiations,
       "sessionStatusInactiveModemReceiveLineLevel": sessionStatusInactiveModemReceiveLineLevel,
       "sessionStatusInactiveRemoteIPXNetwork": sessionStatusInactiveRemoteIPXNetwork,
       "sessionStatusInactiveRemoteIPXNode": sessionStatusInactiveRemoteIPXNode,
       "sessionStatusInactiveCleartcpRemoteIP": sessionStatusInactiveCleartcpRemoteIP,
       "sessionStatusInactiveCleartcpRemotePort": sessionStatusInactiveCleartcpRemotePort,
       "sessionStatusInactiveTunnelId": sessionStatusInactiveTunnelId,
       "sessionStatusInactiveLinkId": sessionStatusInactiveLinkId,
       "sessionDiscCauseTable": sessionDiscCauseTable,
       "sessionDiscCauseEntry": sessionDiscCauseEntry,
       "sessionDiscCauseIndex": sessionDiscCauseIndex,
       "sessionDiscCauseComponent": sessionDiscCauseComponent,
       "sessionDiscCauseCause": sessionDiscCauseCause,
       "sessionDiscCauseReason": sessionDiscCauseReason,
       "sessionDiscCauseCount": sessionDiscCauseCount,
       "sessionStatusReverseTable": sessionStatusReverseTable,
       "sessionStatusReverseEntry": sessionStatusReverseEntry,
       "sessionStatusReverseSessionID": sessionStatusReverseSessionID,
       "sessionStatusReverseState": sessionStatusReverseState,
       "sessionStatusReversePermanentFlag": sessionStatusReversePermanentFlag,
       "sessionStatusReverseVpopId": sessionStatusReverseVpopId,
       "sessionStatusReverseName": sessionStatusReverseName,
       "sessionStatusReverseRemoteIP": sessionStatusReverseRemoteIP,
       "sessionStatusReverseRemoteIPMask": sessionStatusReverseRemoteIPMask,
       "sessionStatusReverseLocalIP": sessionStatusReverseLocalIP,
       "sessionStatusReverseLocalIPMask": sessionStatusReverseLocalIPMask,
       "sessionStatusReverseLinkService": sessionStatusReverseLinkService,
       "sessionStatusReverseServiceMode": sessionStatusReverseServiceMode,
       "sessionStatusReverseStartTime": sessionStatusReverseStartTime,
       "sessionStatusReverseStopTime": sessionStatusReverseStopTime,
       "sessionStatusReverseTimeOfModemSync": sessionStatusReverseTimeOfModemSync,
       "sessionStatusReverseTimeOfService": sessionStatusReverseTimeOfService,
       "sessionStatusReverseTerminatingComponent": sessionStatusReverseTerminatingComponent,
       "sessionStatusReverseTerminationCause": sessionStatusReverseTerminationCause,
       "sessionStatusReverseLastComponent": sessionStatusReverseLastComponent,
       "sessionStatusReverseLayer1Slot": sessionStatusReverseLayer1Slot,
       "sessionStatusReverseLayer2Slot": sessionStatusReverseLayer2Slot,
       "sessionStatusReverseCalledNumber": sessionStatusReverseCalledNumber,
       "sessionStatusReverseCallingNumber": sessionStatusReverseCallingNumber,
       "sessionStatusReverseOriginateMode": sessionStatusReverseOriginateMode,
       "sessionStatusReverseOctetsIn": sessionStatusReverseOctetsIn,
       "sessionStatusReverseOctetsOut": sessionStatusReverseOctetsOut,
       "sessionStatusReversePacketsIn": sessionStatusReversePacketsIn,
       "sessionStatusReversePacketsOut": sessionStatusReversePacketsOut,
       "sessionStatusReverseMultiLinkId": sessionStatusReverseMultiLinkId,
       "sessionStatusReversePort": sessionStatusReversePort,
       "sessionStatusReverseTimeslot": sessionStatusReverseTimeslot,
       "sessionStatusReverseLinkCount": sessionStatusReverseLinkCount,
       "sessionStatusReverseTxStartDataRate": sessionStatusReverseTxStartDataRate,
       "sessionStatusReverseRxStartDataRate": sessionStatusReverseRxStartDataRate,
       "sessionStatusReverseTxEndDataRate": sessionStatusReverseTxEndDataRate,
       "sessionStatusReverseRxEndDataRate": sessionStatusReverseRxEndDataRate,
       "sessionStatusReverseTxMinDataRate": sessionStatusReverseTxMinDataRate,
       "sessionStatusReverseRxMinDataRate": sessionStatusReverseRxMinDataRate,
       "sessionStatusReverseTxMaxDataRate": sessionStatusReverseTxMaxDataRate,
       "sessionStatusReverseRxMaxDataRate": sessionStatusReverseRxMaxDataRate,
       "sessionStatusReverseIop": sessionStatusReverseIop,
       "sessionStatusReverseDmm": sessionStatusReverseDmm,
       "sessionStatusReversePack": sessionStatusReversePack,
       "sessionStatusReverseDevice": sessionStatusReverseDevice,
       "sessionStatusReverseTdmStream": sessionStatusReverseTdmStream,
       "sessionStatusReverseTdmTimeSlot": sessionStatusReverseTdmTimeSlot,
       "sessionStatusReverseTerminationReason": sessionStatusReverseTerminationReason,
       "sessionStatusReverseDuration": sessionStatusReverseDuration,
       "sessionStatusReverseDurationHMS": sessionStatusReverseDurationHMS,
       "sessionStatusReverseSs7SessionId": sessionStatusReverseSs7SessionId,
       "sessionStatusReverseModemNumber": sessionStatusReverseModemNumber,
       "sessionStatusReverseTunnelType": sessionStatusReverseTunnelType,
       "sessionStatusReverseTunnelMediumType": sessionStatusReverseTunnelMediumType,
       "sessionStatusReverseTunnelServerAddress": sessionStatusReverseTunnelServerAddress,
       "sessionStatusReverseCallClass": sessionStatusReverseCallClass,
       "sessionStatusReverseTandemPort": sessionStatusReverseTandemPort,
       "sessionStatusReverseTandemTimeslot": sessionStatusReverseTandemTimeslot,
       "sessionStatusReverseCallClassArray": sessionStatusReverseCallClassArray,
       "sessionStatusReverseCallClassLen": sessionStatusReverseCallClassLen,
       "sessionStatusReverseActualAuthMethod": sessionStatusReverseActualAuthMethod,
       "sessionStatusReverseModemModulation": sessionStatusReverseModemModulation,
       "sessionStatusReverseModemErrorCorrection": sessionStatusReverseModemErrorCorrection,
       "sessionStatusReverseModemDataCompression": sessionStatusReverseModemDataCompression,
       "sessionStatusReverseModemTxBlocks": sessionStatusReverseModemTxBlocks,
       "sessionStatusReverseModemRetransmits": sessionStatusReverseModemRetransmits,
       "sessionStatusReverseModemSNR": sessionStatusReverseModemSNR,
       "sessionStatusReverseModemLocalRetrains": sessionStatusReverseModemLocalRetrains,
       "sessionStatusReverseModemRemoteRetrains": sessionStatusReverseModemRemoteRetrains,
       "sessionStatusReverseModemLocalRenegotiations": sessionStatusReverseModemLocalRenegotiations,
       "sessionStatusReverseModemRemoteRenegotiations": sessionStatusReverseModemRemoteRenegotiations,
       "sessionStatusReverseModemReceiveLineLevel": sessionStatusReverseModemReceiveLineLevel,
       "sessionStatusReverseRemoteIPXNetwork": sessionStatusReverseRemoteIPXNetwork,
       "sessionStatusReverseRemoteIPXNode": sessionStatusReverseRemoteIPXNode,
       "sessionStatusReverseCleartcpRemoteIP": sessionStatusReverseCleartcpRemoteIP,
       "sessionStatusReverseCleartcpRemotePort": sessionStatusReverseCleartcpRemotePort,
       "sessionStatusReverseTunnelId": sessionStatusReverseTunnelId,
       "sessionStatusReverseLinkId": sessionStatusReverseLinkId,
       "sessionStatusHistoryTable": sessionStatusHistoryTable,
       "sessionStatusHistoryEntry": sessionStatusHistoryEntry,
       "sessionStatusHistoryIndex": sessionStatusHistoryIndex,
       "sessionStatusHistorySessionID": sessionStatusHistorySessionID,
       "sessionStatusHistoryState": sessionStatusHistoryState,
       "sessionStatusHistoryPermanentFlag": sessionStatusHistoryPermanentFlag,
       "sessionStatusHistoryVpopId": sessionStatusHistoryVpopId,
       "sessionStatusHistoryName": sessionStatusHistoryName,
       "sessionStatusHistoryRemoteIP": sessionStatusHistoryRemoteIP,
       "sessionStatusHistoryRemoteIPMask": sessionStatusHistoryRemoteIPMask,
       "sessionStatusHistoryLocalIP": sessionStatusHistoryLocalIP,
       "sessionStatusHistoryLocalIPMask": sessionStatusHistoryLocalIPMask,
       "sessionStatusHistoryLinkService": sessionStatusHistoryLinkService,
       "sessionStatusHistoryServiceMode": sessionStatusHistoryServiceMode,
       "sessionStatusHistoryStartTime": sessionStatusHistoryStartTime,
       "sessionStatusHistoryStopTime": sessionStatusHistoryStopTime,
       "sessionStatusHistoryTimeOfModemSync": sessionStatusHistoryTimeOfModemSync,
       "sessionStatusHistoryTimeOfService": sessionStatusHistoryTimeOfService,
       "sessionStatusHistoryTerminatingComponent": sessionStatusHistoryTerminatingComponent,
       "sessionStatusHistoryTerminationCause": sessionStatusHistoryTerminationCause,
       "sessionStatusHistoryLastComponent": sessionStatusHistoryLastComponent,
       "sessionStatusHistoryLayer1Slot": sessionStatusHistoryLayer1Slot,
       "sessionStatusHistoryLayer2Slot": sessionStatusHistoryLayer2Slot,
       "sessionStatusHistoryCalledNumber": sessionStatusHistoryCalledNumber,
       "sessionStatusHistoryCallingNumber": sessionStatusHistoryCallingNumber,
       "sessionStatusHistoryOriginateMode": sessionStatusHistoryOriginateMode,
       "sessionStatusHistoryOctetsIn": sessionStatusHistoryOctetsIn,
       "sessionStatusHistoryOctetsOut": sessionStatusHistoryOctetsOut,
       "sessionStatusHistoryPacketsIn": sessionStatusHistoryPacketsIn,
       "sessionStatusHistoryPacketsOut": sessionStatusHistoryPacketsOut,
       "sessionStatusHistoryMultiLinkId": sessionStatusHistoryMultiLinkId,
       "sessionStatusHistoryPort": sessionStatusHistoryPort,
       "sessionStatusHistoryTimeslot": sessionStatusHistoryTimeslot,
       "sessionStatusHistoryLinkCount": sessionStatusHistoryLinkCount,
       "sessionStatusHistoryTxStartDataRate": sessionStatusHistoryTxStartDataRate,
       "sessionStatusHistoryRxStartDataRate": sessionStatusHistoryRxStartDataRate,
       "sessionStatusHistoryTxEndDataRate": sessionStatusHistoryTxEndDataRate,
       "sessionStatusHistoryRxEndDataRate": sessionStatusHistoryRxEndDataRate,
       "sessionStatusHistoryTxMinDataRate": sessionStatusHistoryTxMinDataRate,
       "sessionStatusHistoryRxMinDataRate": sessionStatusHistoryRxMinDataRate,
       "sessionStatusHistoryTxMaxDataRate": sessionStatusHistoryTxMaxDataRate,
       "sessionStatusHistoryRxMaxDataRate": sessionStatusHistoryRxMaxDataRate,
       "sessionStatusHistoryIop": sessionStatusHistoryIop,
       "sessionStatusHistoryDmm": sessionStatusHistoryDmm,
       "sessionStatusHistoryPack": sessionStatusHistoryPack,
       "sessionStatusHistoryDevice": sessionStatusHistoryDevice,
       "sessionStatusHistoryTdmStream": sessionStatusHistoryTdmStream,
       "sessionStatusHistoryTdmTimeSlot": sessionStatusHistoryTdmTimeSlot,
       "sessionStatusHistoryTerminationReason": sessionStatusHistoryTerminationReason,
       "sessionStatusHistoryDuration": sessionStatusHistoryDuration,
       "sessionStatusHistoryDurationHMS": sessionStatusHistoryDurationHMS,
       "sessionStatusHistorySs7SessionId": sessionStatusHistorySs7SessionId,
       "sessionStatusHistoryModemNumber": sessionStatusHistoryModemNumber,
       "sessionStatusHistoryTunnelType": sessionStatusHistoryTunnelType,
       "sessionStatusHistoryTunnelMediumType": sessionStatusHistoryTunnelMediumType,
       "sessionStatusHistoryTunnelServerAddress": sessionStatusHistoryTunnelServerAddress,
       "sessionStatusHistoryCallClass": sessionStatusHistoryCallClass,
       "sessionStatusHistoryTandemPort": sessionStatusHistoryTandemPort,
       "sessionStatusHistoryTandemTimeslot": sessionStatusHistoryTandemTimeslot,
       "sessionStatusHistoryCallClassArray": sessionStatusHistoryCallClassArray,
       "sessionStatusHistoryCallClassLen": sessionStatusHistoryCallClassLen,
       "sessionStatusHistoryActualAuthMethod": sessionStatusHistoryActualAuthMethod,
       "sessionStatusHistoryModemModulation": sessionStatusHistoryModemModulation,
       "sessionStatusHistoryModemErrorCorrection": sessionStatusHistoryModemErrorCorrection,
       "sessionStatusHistoryModemDataCompression": sessionStatusHistoryModemDataCompression,
       "sessionStatusHistoryModemTxBlocks": sessionStatusHistoryModemTxBlocks,
       "sessionStatusHistoryModemRetransmits": sessionStatusHistoryModemRetransmits,
       "sessionStatusHistoryModemSNR": sessionStatusHistoryModemSNR,
       "sessionStatusHistoryModemLocalRetrains": sessionStatusHistoryModemLocalRetrains,
       "sessionStatusHistoryModemRemoteRetrains": sessionStatusHistoryModemRemoteRetrains,
       "sessionStatusHistoryModemLocalRenegotiations": sessionStatusHistoryModemLocalRenegotiations,
       "sessionStatusHistoryModemRemoteRenegotiations": sessionStatusHistoryModemRemoteRenegotiations,
       "sessionStatusHistoryModemReceiveLineLevel": sessionStatusHistoryModemReceiveLineLevel,
       "sessionStatusHistoryRemoteIPXNetwork": sessionStatusHistoryRemoteIPXNetwork,
       "sessionStatusHistoryRemoteIPXNode": sessionStatusHistoryRemoteIPXNode,
       "sessionStatusHistoryCleartcpRemoteIP": sessionStatusHistoryCleartcpRemoteIP,
       "sessionStatusHistoryCleartcpRemotePort": sessionStatusHistoryCleartcpRemotePort,
       "sessionStatusHistoryTunnelId": sessionStatusHistoryTunnelId,
       "sessionStatusHistoryLinkId": sessionStatusHistoryLinkId,
       "slotStatusTable": slotStatusTable,
       "slotStatusEntry": slotStatusEntry,
       "slotStatusShelfNumber": slotStatusShelfNumber,
       "slotStatusSlotIndex": slotStatusSlotIndex,
       "slotStatusSlotStatus": slotStatusSlotStatus,
       "slotStatusPartNumber": slotStatusPartNumber,
       "slotStatusSerialNumber": slotStatusSerialNumber,
       "slotStatusHardwareRev": slotStatusHardwareRev,
       "slotStatusStiffwareRev": slotStatusStiffwareRev,
       "slotStatusFirmwareRev": slotStatusFirmwareRev,
       "slotStatusSystemMem": slotStatusSystemMem,
       "slotStatusOtherMem": slotStatusOtherMem,
       "slotStatusTemperature": slotStatusTemperature,
       "slotStatusSlotType": slotStatusSlotType,
       "slotStatusSlotOos": slotStatusSlotOos,
       "slotStatusServiceModule": slotStatusServiceModule,
       "slotStatusLineTerminationModule": slotStatusLineTerminationModule,
       "slotStatusNewTable": slotStatusNewTable,
       "slotStatusNewEntry": slotStatusNewEntry,
       "slotStatusNewShelfNumber": slotStatusNewShelfNumber,
       "slotStatusNewSlotIndex": slotStatusNewSlotIndex,
       "slotStatusNewSlotStatus": slotStatusNewSlotStatus,
       "slotStatusNewSlotType": slotStatusNewSlotType,
       "slotStatusNewProductCode": slotStatusNewProductCode,
       "slotStatusNewSlotSerialNumber": slotStatusNewSlotSerialNumber,
       "slotStatusNewFabricationRev": slotStatusNewFabricationRev,
       "slotStatusNewPalRev": slotStatusNewPalRev,
       "slotStatusNewReworkRev": slotStatusNewReworkRev,
       "slotStatusNewFirmwareRev": slotStatusNewFirmwareRev,
       "slotStatusNewTemperature": slotStatusNewTemperature,
       "slotStatusNewSlotOos": slotStatusNewSlotOos,
       "slotStatusNewLineTerminationModuleType": slotStatusNewLineTerminationModuleType,
       "sessionComponentsTable": sessionComponentsTable,
       "sessionComponentsEntry": sessionComponentsEntry,
       "sessionComponentsSessionIndex": sessionComponentsSessionIndex,
       "sessionComponentsIndex": sessionComponentsIndex,
       "sessionComponentsComponentType": sessionComponentsComponentType,
       "sessionComponentsComponentState": sessionComponentsComponentState,
       "sessionComponentsStatHandle": sessionComponentsStatHandle,
       "sessionTraceTable": sessionTraceTable,
       "sessionTraceEntry": sessionTraceEntry,
       "sessionTraceSessionIndex": sessionTraceSessionIndex,
       "sessionTraceIndex": sessionTraceIndex,
       "sessionTraceAbsoluteTimeStamp": sessionTraceAbsoluteTimeStamp,
       "sessionTraceRelativeTimeStamp": sessionTraceRelativeTimeStamp,
       "sessionTraceLogEntry": sessionTraceLogEntry,
       "sessionSlotsTable": sessionSlotsTable,
       "sessionSlotsEntry": sessionSlotsEntry,
       "sessionSlotsTrunkCount": sessionSlotsTrunkCount,
       "sessionSlotsSlot1Count": sessionSlotsSlot1Count,
       "sessionSlotsSlot2Count": sessionSlotsSlot2Count,
       "sessionSlotsSlot3Count": sessionSlotsSlot3Count,
       "sessionSlotsSlot4Count": sessionSlotsSlot4Count,
       "sessionSlotsSlot5Count": sessionSlotsSlot5Count,
       "sessionSlotsSlot6Count": sessionSlotsSlot6Count,
       "sessionSlotsSlot7Count": sessionSlotsSlot7Count,
       "sessionSlotsSlot8Count": sessionSlotsSlot8Count,
       "sessionSlotsSlot9Count": sessionSlotsSlot9Count,
       "sessionSlotsSlot10Count": sessionSlotsSlot10Count,
       "sessionSlotsSlot11Count": sessionSlotsSlot11Count,
       "sessionSlotsSlot12Count": sessionSlotsSlot12Count,
       "sessionSlotsSlot13Count": sessionSlotsSlot13Count,
       "sessionSlotsSlot14Count": sessionSlotsSlot14Count,
       "sessionSlotsSlot15Count": sessionSlotsSlot15Count,
       "sessionSlotsSlot16Count": sessionSlotsSlot16Count,
       "sessionSlotsSlot17Count": sessionSlotsSlot17Count,
       "sessionSlotsSlot18Count": sessionSlotsSlot18Count,
       "sessionSummaryTable": sessionSummaryTable,
       "sessionSummaryEntry": sessionSummaryEntry,
       "sessionSummaryActiveUnknown": sessionSummaryActiveUnknown,
       "sessionSummaryMaximumUnknown": sessionSummaryMaximumUnknown,
       "sessionSummaryInactiveUnknown": sessionSummaryInactiveUnknown,
       "sessionSummaryActiveNone": sessionSummaryActiveNone,
       "sessionSummaryMaximumNone": sessionSummaryMaximumNone,
       "sessionSummaryInactiveNone": sessionSummaryInactiveNone,
       "sessionSummaryActiveOther": sessionSummaryActiveOther,
       "sessionSummaryMaximumOther": sessionSummaryMaximumOther,
       "sessionSummaryInactiveOther": sessionSummaryInactiveOther,
       "sessionSummaryActivePpp": sessionSummaryActivePpp,
       "sessionSummaryMaximumPpp": sessionSummaryMaximumPpp,
       "sessionSummaryInactivePpp": sessionSummaryInactivePpp,
       "sessionSummaryActiveSlip": sessionSummaryActiveSlip,
       "sessionSummaryMaximumSlip": sessionSummaryMaximumSlip,
       "sessionSummaryInactiveSlip": sessionSummaryInactiveSlip,
       "sessionSummaryActiveFrameRelay": sessionSummaryActiveFrameRelay,
       "sessionSummaryMaximumFrameRelay": sessionSummaryMaximumFrameRelay,
       "sessionSummaryInactiveFrameRelay": sessionSummaryInactiveFrameRelay,
       "sessionSummaryActiveCiscoHDLC": sessionSummaryActiveCiscoHDLC,
       "sessionSummaryMaximumCiscoHDLC": sessionSummaryMaximumCiscoHDLC,
       "sessionSummaryInactiveCiscoHDLC": sessionSummaryInactiveCiscoHDLC,
       "sessionSummaryActiveTerminalServer": sessionSummaryActiveTerminalServer,
       "sessionSummaryMaximumTerminalServer": sessionSummaryMaximumTerminalServer,
       "sessionSummaryInactiveTerminalServer": sessionSummaryInactiveTerminalServer,
       "sessionSummaryActiveTelnet": sessionSummaryActiveTelnet,
       "sessionSummaryMaximumTelnet": sessionSummaryMaximumTelnet,
       "sessionSummaryInactiveTelnet": sessionSummaryInactiveTelnet,
       "sessionSummaryActiveRawTCP": sessionSummaryActiveRawTCP,
       "sessionSummaryMaximumRawTCP": sessionSummaryMaximumRawTCP,
       "sessionSummaryInactiveRawTCP": sessionSummaryInactiveRawTCP,
       "sessionSummaryActiveRlogin": sessionSummaryActiveRlogin,
       "sessionSummaryMaximumRlogin": sessionSummaryMaximumRlogin,
       "sessionSummaryInactiveRlogin": sessionSummaryInactiveRlogin,
       "sessionSummaryActiveL2tp": sessionSummaryActiveL2tp,
       "sessionSummaryMaximumL2tp": sessionSummaryMaximumL2tp,
       "sessionSummaryInactiveL2tp": sessionSummaryInactiveL2tp,
       "sessionSummaryActiveL2f": sessionSummaryActiveL2f,
       "sessionSummaryMaximumL2f": sessionSummaryMaximumL2f,
       "sessionSummaryInactiveL2f": sessionSummaryInactiveL2f,
       "sessionSummaryActiveTrunk": sessionSummaryActiveTrunk,
       "sessionSummaryMaximumTrunk": sessionSummaryMaximumTrunk,
       "sessionSummaryInactiveTrunk": sessionSummaryInactiveTrunk,
       "sessionSummaryActiveVoice": sessionSummaryActiveVoice,
       "sessionSummaryMaximumVoice": sessionSummaryMaximumVoice,
       "sessionSummaryInactiveVoice": sessionSummaryInactiveVoice,
       "sessionSummaryActiveTandem": sessionSummaryActiveTandem,
       "sessionSummaryMaximumTandem": sessionSummaryMaximumTandem,
       "sessionSummaryInactiveTandem": sessionSummaryInactiveTandem,
       "sessionSummaryActiveFtp": sessionSummaryActiveFtp,
       "sessionSummaryMaximumFtp": sessionSummaryMaximumFtp,
       "sessionSummaryInactiveFtp": sessionSummaryInactiveFtp,
       "sessionSummaryActiveDvs": sessionSummaryActiveDvs,
       "sessionSummaryMaximumDvs": sessionSummaryMaximumDvs,
       "sessionSummaryInactiveDvs": sessionSummaryInactiveDvs,
       "sessionSummaryActiveAtmp": sessionSummaryActiveAtmp,
       "sessionSummaryMaximumAtmp": sessionSummaryMaximumAtmp,
       "sessionSummaryInactiveAtmp": sessionSummaryInactiveAtmp,
       "sessionSummaryActiveFax": sessionSummaryActiveFax,
       "sessionSummaryMaximumFax": sessionSummaryMaximumFax,
       "sessionSummaryInactiveFax": sessionSummaryInactiveFax,
       "sessionSummaryActiveHub": sessionSummaryActiveHub,
       "sessionSummaryMaximumHub": sessionSummaryMaximumHub,
       "sessionSummaryInactiveHub": sessionSummaryInactiveHub,
       "sessionSummaryActiveTest": sessionSummaryActiveTest,
       "sessionSummaryMaximumTest": sessionSummaryMaximumTest,
       "sessionSummaryInactiveTest": sessionSummaryInactiveTest,
       "sessionSummaryMaximumTotal": sessionSummaryMaximumTotal,
       "sessionMultilinkTable": sessionMultilinkTable,
       "sessionMultilinkEntry": sessionMultilinkEntry,
       "sessionMultilinkNegotiated": sessionMultilinkNegotiated,
       "sessionMultilinkSessionId": sessionMultilinkSessionId,
       "sessionMultilinkNameLength": sessionMultilinkNameLength,
       "sessionMultilinkUserName": sessionMultilinkUserName,
       "sessionMultilinkMyMRRU": sessionMultilinkMyMRRU,
       "sessionMultilinkPeerMRRU": sessionMultilinkPeerMRRU,
       "sessionMultilinkMyShortSequence": sessionMultilinkMyShortSequence,
       "sessionMultilinkPeerShortSequence": sessionMultilinkPeerShortSequence,
       "sessionMultilinkMyEIDType": sessionMultilinkMyEIDType,
       "sessionMultilinkPeerEIDType": sessionMultilinkPeerEIDType,
       "sessionMultilinkMyEIDLength": sessionMultilinkMyEIDLength,
       "sessionMultilinkPeerEIDLength": sessionMultilinkPeerEIDLength,
       "sessionMultilinkMyEIDData": sessionMultilinkMyEIDData,
       "sessionMultilinkPeerEIDData": sessionMultilinkPeerEIDData,
       "sessionVpopTable": sessionVpopTable,
       "sessionVpopEntry": sessionVpopEntry,
       "sessionVpopVpopIndex": sessionVpopVpopIndex,
       "sessionVpopVpopId": sessionVpopVpopId,
       "sessionVpopCallType": sessionVpopCallType,
       "sessionVpopProtocol": sessionVpopProtocol,
       "sessionVpopCurrentCount": sessionVpopCurrentCount,
       "sessionVpopCurrentDuration": sessionVpopCurrentDuration,
       "sessionVpopCumulativeCount": sessionVpopCumulativeCount,
       "sessionVpopCumulativeDuration": sessionVpopCumulativeDuration,
       "ss7StatusTable": ss7StatusTable,
       "ss7StatusEntry": ss7StatusEntry,
       "ss7StatusIndex": ss7StatusIndex,
       "ss7StatusState": ss7StatusState,
       "ss7StatusNetworkId": ss7StatusNetworkId,
       "ss7StatusCalledId": ss7StatusCalledId,
       "ss7StatusCallingId": ss7StatusCallingId,
       "ss7StatusCallType": ss7StatusCallType,
       "ss7StatusSlot": ss7StatusSlot,
       "ss7StatusPort": ss7StatusPort,
       "ss7StatusTimeSlot": ss7StatusTimeSlot,
       "ss7StatusSessionId": ss7StatusSessionId,
       "ss7StatusServerId": ss7StatusServerId,
       "ss7StatusStartTime": ss7StatusStartTime,
       "ss7TraceTable": ss7TraceTable,
       "ss7TraceEntry": ss7TraceEntry,
       "ss7TraceSs7Index": ss7TraceSs7Index,
       "ss7TraceIndex": ss7TraceIndex,
       "ss7TraceAbsoluteTimeStamp": ss7TraceAbsoluteTimeStamp,
       "ss7TraceRelativeTimeStamp": ss7TraceRelativeTimeStamp,
       "ss7TraceLogEntry": ss7TraceLogEntry,
       "ss7StatusReverseTable": ss7StatusReverseTable,
       "ss7StatusReverseEntry": ss7StatusReverseEntry,
       "ss7StatusReverseIndex": ss7StatusReverseIndex,
       "ss7StatusReverseState": ss7StatusReverseState,
       "ss7StatusReverseNetworkId": ss7StatusReverseNetworkId,
       "ss7StatusReverseCalledId": ss7StatusReverseCalledId,
       "ss7StatusReverseCallingId": ss7StatusReverseCallingId,
       "ss7StatusReverseCallType": ss7StatusReverseCallType,
       "ss7StatusReverseSlot": ss7StatusReverseSlot,
       "ss7StatusReversePort": ss7StatusReversePort,
       "ss7StatusReverseTimeSlot": ss7StatusReverseTimeSlot,
       "ss7StatusReverseSessionId": ss7StatusReverseSessionId,
       "ss7StatusReverseServerId": ss7StatusReverseServerId,
       "ss7StatusReverseStartTime": ss7StatusReverseStartTime,
       "ss7CountersTable": ss7CountersTable,
       "ss7CountersEntry": ss7CountersEntry,
       "ss7CountersNumActive": ss7CountersNumActive,
       "ss7CountersNumInactive": ss7CountersNumInactive,
       "ss7CountersRetainedFree": ss7CountersRetainedFree,
       "ss7CountersRetainedFull": ss7CountersRetainedFull,
       "ss7CountersOneshotFree": ss7CountersOneshotFree,
       "ss7CountersOneshotFull": ss7CountersOneshotFull,
       "ss7CountersDsmccFree": ss7CountersDsmccFree,
       "ss7CountersDsmccFull": ss7CountersDsmccFull,
       "ipdcTraceTable": ipdcTraceTable,
       "ipdcTraceEntry": ipdcTraceEntry,
       "ipdcTraceIndex": ipdcTraceIndex,
       "ipdcTraceTimeStamp": ipdcTraceTimeStamp,
       "ipdcTraceDirection": ipdcTraceDirection,
       "ipdcTraceMsgSize": ipdcTraceMsgSize,
       "ipdcTraceIpdcMsg": ipdcTraceIpdcMsg,
       "ipSvcMonitoringTable": ipSvcMonitoringTable,
       "ipSvcMonitoringEntry": ipSvcMonitoringEntry,
       "ipSvcMonitoringServiceName": ipSvcMonitoringServiceName,
       "ipSvcMonitoringState": ipSvcMonitoringState,
       "ipSvcMonitoringUptime": ipSvcMonitoringUptime,
       "ipSvcMonitoringRequestsIn": ipSvcMonitoringRequestsIn,
       "ipSvcMonitoringResponsesOut": ipSvcMonitoringResponsesOut,
       "ipSvcMonitoringRequestsOut": ipSvcMonitoringRequestsOut,
       "ipSvcMonitoringResponsesIn": ipSvcMonitoringResponsesIn,
       "ipSvcMonitoringRequestsInProgress": ipSvcMonitoringRequestsInProgress,
       "ipSvcMonitoringRequestsInError": ipSvcMonitoringRequestsInError,
       "ipSvcMonitoringResponsesInError": ipSvcMonitoringResponsesInError,
       "ipAlarmEntryTable": ipAlarmEntryTable,
       "ipAlarmEntryEntry": ipAlarmEntryEntry,
       "ipAlarmEntryAlarmType": ipAlarmEntryAlarmType,
       "ipAlarmEntryTrapGenNum": ipAlarmEntryTrapGenNum,
       "ipAlarmEntryTrapType": ipAlarmEntryTrapType,
       "ipAlarmEntryTrapOID": ipAlarmEntryTrapOID,
       "ipAlarmEntryTrapOIDLen": ipAlarmEntryTrapOIDLen,
       "ipAlarmEntryTrapSeverity": ipAlarmEntryTrapSeverity,
       "ipAlarmEntryTrapTimeticks": ipAlarmEntryTrapTimeticks,
       "ipAlarmEntryTrapPath": ipAlarmEntryTrapPath,
       "ipAlarmEntryTrapArg1": ipAlarmEntryTrapArg1,
       "ipAlarmEntryTrapArg2": ipAlarmEntryTrapArg2,
       "ipAlarmEntryTrapArg3": ipAlarmEntryTrapArg3,
       "ipAlarmEntryTrapGroup": ipAlarmEntryTrapGroup,
       "cHdlcStatsTable": cHdlcStatsTable,
       "cHdlcStatsEntry": cHdlcStatsEntry,
       "cHdlcStatsNohdrspaceOut": cHdlcStatsNohdrspaceOut,
       "cHdlcStatsNomemoryOut": cHdlcStatsNomemoryOut,
       "cHdlcStatsCiscoFramesOut": cHdlcStatsCiscoFramesOut,
       "cHdlcStatsKeepalivesIn": cHdlcStatsKeepalivesIn,
       "cHdlcStatsUnknownProtocolIn": cHdlcStatsUnknownProtocolIn,
       "cHdlcStatsShortFramesIn": cHdlcStatsShortFramesIn,
       "cHdlcStatsPppFramesIn": cHdlcStatsPppFramesIn,
       "cHdlcStatsUnknownFramesIn": cHdlcStatsUnknownFramesIn,
       "cHdlcStatsUnknownCiscoTypeIn": cHdlcStatsUnknownCiscoTypeIn,
       "cHdlcStatsCiscoFramesIn": cHdlcStatsCiscoFramesIn,
       "ipStubStatsTable": ipStubStatsTable,
       "ipStubStatsEntry": ipStubStatsEntry,
       "ipStubStatsIgmpInMsgs": ipStubStatsIgmpInMsgs,
       "ipStubStatsIgmpInErrors": ipStubStatsIgmpInErrors,
       "ipStubStatsIgmpInReports": ipStubStatsIgmpInReports,
       "ipStubStatsIgmpInQueries": ipStubStatsIgmpInQueries,
       "ipStubStatsIgmpUnknownType": ipStubStatsIgmpUnknownType,
       "ipStubStatsIgmpOutMsgs": ipStubStatsIgmpOutMsgs,
       "ipStubStatsNomemoryOut": ipStubStatsNomemoryOut,
       "ipCleartcpStatsTable": ipCleartcpStatsTable,
       "ipCleartcpStatsEntry": ipCleartcpStatsEntry,
       "ipCleartcpStatsInputQfull": ipCleartcpStatsInputQfull,
       "ipCleartcpStatsInputTcpfull": ipCleartcpStatsInputTcpfull,
       "ipCleartcpStatsInputDroppedBytes": ipCleartcpStatsInputDroppedBytes,
       "ipCleartcpStatsInputBytes": ipCleartcpStatsInputBytes,
       "ipCleartcpStatsOutputQfull": ipCleartcpStatsOutputQfull,
       "ipCleartcpStatsOutputDroppedBytes": ipCleartcpStatsOutputDroppedBytes,
       "ipCleartcpStatsOutputBytes": ipCleartcpStatsOutputBytes,
       "pppLogEntryTable": pppLogEntryTable,
       "pppLogEntryEntry": pppLogEntryEntry,
       "pppLogEntrySessionId": pppLogEntrySessionId,
       "pppLogEntryIndex": pppLogEntryIndex,
       "pppLogEntryMinIndex": pppLogEntryMinIndex,
       "pppLogEntryMaxIndex": pppLogEntryMaxIndex,
       "pppLogEntryEntryText": pppLogEntryEntryText,
       "pppLogEntryRawEntryText": pppLogEntryRawEntryText,
       "pppDeadLogEntryTable": pppDeadLogEntryTable,
       "pppDeadLogEntryEntry": pppDeadLogEntryEntry,
       "pppDeadLogEntrySessionId": pppDeadLogEntrySessionId,
       "pppDeadLogEntryIndex": pppDeadLogEntryIndex,
       "pppDeadLogEntryMinIndex": pppDeadLogEntryMinIndex,
       "pppDeadLogEntryMaxIndex": pppDeadLogEntryMaxIndex,
       "pppDeadLogEntryEntryText": pppDeadLogEntryEntryText,
       "pppDeadLogEntryRawEntryText": pppDeadLogEntryRawEntryText,
       "pppSessionStatsTable": pppSessionStatsTable,
       "pppSessionStatsEntry": pppSessionStatsEntry,
       "pppSessionStatsSessionID": pppSessionStatsSessionID,
       "pppSessionStatsPhase": pppSessionStatsPhase,
       "pppSessionStatsUserName": pppSessionStatsUserName,
       "pppSessionStatsUpTime": pppSessionStatsUpTime,
       "pppSessionStatsConnectLimit": pppSessionStatsConnectLimit,
       "pppSessionStatsRemainingTime": pppSessionStatsRemainingTime,
       "pppSessionStatsInactivityLimit": pppSessionStatsInactivityLimit,
       "pppSessionStatsInactivityRemaining": pppSessionStatsInactivityRemaining,
       "pppSessionStatsDeadSession": pppSessionStatsDeadSession,
       "pppSessionStatsInterfaceType": pppSessionStatsInterfaceType,
       "pppSessionStatsTxSpeed": pppSessionStatsTxSpeed,
       "pppSessionStatsRxSpeed": pppSessionStatsRxSpeed,
       "pppSessionStatsLCPState": pppSessionStatsLCPState,
       "pppSessionStatsLocalMRU": pppSessionStatsLocalMRU,
       "pppSessionStatsRemoteMRU": pppSessionStatsRemoteMRU,
       "pppSessionStatsLocalAuthProtocol": pppSessionStatsLocalAuthProtocol,
       "pppSessionStatsRemoteAuthProtocol": pppSessionStatsRemoteAuthProtocol,
       "pppSessionStatsLocalPFC": pppSessionStatsLocalPFC,
       "pppSessionStatsRemotePFC": pppSessionStatsRemotePFC,
       "pppSessionStatsLocalACFC": pppSessionStatsLocalACFC,
       "pppSessionStatsRemoteACFC": pppSessionStatsRemoteACFC,
       "pppSessionStatsLocalACCM": pppSessionStatsLocalACCM,
       "pppSessionStatsRemoteACCM": pppSessionStatsRemoteACCM,
       "pppSessionStatsLocalMRRU": pppSessionStatsLocalMRRU,
       "pppSessionStatsRemoteMRRU": pppSessionStatsRemoteMRRU,
       "pppSessionStatsLocalShortSeq": pppSessionStatsLocalShortSeq,
       "pppSessionStatsRemoteShortSeq": pppSessionStatsRemoteShortSeq,
       "pppSessionStatsRemoteAuthenticated": pppSessionStatsRemoteAuthenticated,
       "pppSessionStatsIPCPState": pppSessionStatsIPCPState,
       "pppSessionStatsLocalIPAddress": pppSessionStatsLocalIPAddress,
       "pppSessionStatsRemoteIPAddress": pppSessionStatsRemoteIPAddress,
       "pppSessionStatsDNSAddress1": pppSessionStatsDNSAddress1,
       "pppSessionStatsDNSAddress2": pppSessionStatsDNSAddress2,
       "pppSessionStatsNBNSAddress1": pppSessionStatsNBNSAddress1,
       "pppSessionStatsNBNSAddress2": pppSessionStatsNBNSAddress2,
       "pppSessionStatsLocalVJ": pppSessionStatsLocalVJ,
       "pppSessionStatsLocalVJSlots": pppSessionStatsLocalVJSlots,
       "pppSessionStatsRemoteVJ": pppSessionStatsRemoteVJ,
       "pppSessionStatsRemoteVJSlots": pppSessionStatsRemoteVJSlots,
       "pppSessionStatsIPXCPState": pppSessionStatsIPXCPState,
       "pppSessionStatsRemoteIPXNetwork": pppSessionStatsRemoteIPXNetwork,
       "pppSessionStatsRemoteIPXNode": pppSessionStatsRemoteIPXNode,
       "pppSessionStatsCCPState": pppSessionStatsCCPState,
       "pppSessionStatsLocalCompressAlgorithm": pppSessionStatsLocalCompressAlgorithm,
       "pppSessionStatsLocalCompressHistories": pppSessionStatsLocalCompressHistories,
       "pppSessionStatsRemoteCompressAlgorithm": pppSessionStatsRemoteCompressAlgorithm,
       "pppSessionStatsRemoteCompressHistories": pppSessionStatsRemoteCompressHistories,
       "pppSessionStatsMultilinkActive": pppSessionStatsMultilinkActive,
       "pppSessionStatsMultilinkLinks": pppSessionStatsMultilinkLinks,
       "pppSessionStatsTotalTxSpeed": pppSessionStatsTotalTxSpeed,
       "pppSessionStatsTotalRxSpeed": pppSessionStatsTotalRxSpeed,
       "pppSessionStatsMLPFragmentsReceived": pppSessionStatsMLPFragmentsReceived,
       "pppSessionStatsMLPFragmentsMissing": pppSessionStatsMLPFragmentsMissing,
       "pppSessionStatsMLPFragmentsDropped": pppSessionStatsMLPFragmentsDropped,
       "pppSessionStatsMLPPacketsReassembled": pppSessionStatsMLPPacketsReassembled,
       "pppSessionStatsMLPPacketsNull": pppSessionStatsMLPPacketsNull,
       "pppSessionStatsMultilinkLinksAdded": pppSessionStatsMultilinkLinksAdded,
       "pppSessionStatsMultilinkLinksRemoved": pppSessionStatsMultilinkLinksRemoved,
       "pppSessionStatsMultilinkLinksMax": pppSessionStatsMultilinkLinksMax,
       "pppSessionStatsMultilinkLinksMaxConfig": pppSessionStatsMultilinkLinksMaxConfig,
       "pppSessionStatsTxPackets": pppSessionStatsTxPackets,
       "pppSessionStatsTxPacketsDropped": pppSessionStatsTxPacketsDropped,
       "pppSessionStatsTxBytes": pppSessionStatsTxBytes,
       "pppSessionStatsRxPackets": pppSessionStatsRxPackets,
       "pppSessionStatsRxPacketsDropped": pppSessionStatsRxPacketsDropped,
       "pppSessionStatsRxBytes": pppSessionStatsRxBytes,
       "pppSessionStatsTxCompressing": pppSessionStatsTxCompressing,
       "pppSessionStatsTxBytesBeforeCompress": pppSessionStatsTxBytesBeforeCompress,
       "pppSessionStatsTxBytesAfterCompress": pppSessionStatsTxBytesAfterCompress,
       "pppSessionStatsTxBytesUncompressed": pppSessionStatsTxBytesUncompressed,
       "pppSessionStatsRxBytesBeforeCompress": pppSessionStatsRxBytesBeforeCompress,
       "pppSessionStatsRxBytesAfterCompress": pppSessionStatsRxBytesAfterCompress,
       "pppSessionStatsRxBytesUncompressed": pppSessionStatsRxBytesUncompressed,
       "pppSessionStatsRxCompPacketsDropped": pppSessionStatsRxCompPacketsDropped,
       "pppSessionStatsCCPResetsSent": pppSessionStatsCCPResetsSent,
       "pppSessionStatsCCPResetsReceived": pppSessionStatsCCPResetsReceived,
       "pppSessionStatsRxResourceErrors": pppSessionStatsRxResourceErrors,
       "pppSessionStatsRxQueueErrors": pppSessionStatsRxQueueErrors,
       "pppSessionStatsRxCRCErrors": pppSessionStatsRxCRCErrors,
       "pppSessionStatsRxAbortErrors": pppSessionStatsRxAbortErrors,
       "pppSessionStatsRxOverrunErrors": pppSessionStatsRxOverrunErrors,
       "pppSessionStatsRxBigErrors": pppSessionStatsRxBigErrors,
       "pppSessionStatsRxSmallErrors": pppSessionStatsRxSmallErrors,
       "pppSessionStatsRxAlignErrors": pppSessionStatsRxAlignErrors,
       "pppSessionStatsTxResourceErrors": pppSessionStatsTxResourceErrors,
       "pppSessionStatsTxQueueErrors": pppSessionStatsTxQueueErrors,
       "pppSessionStatsTxBigErrors": pppSessionStatsTxBigErrors,
       "pppSessionStatsTxUnderrunErrors": pppSessionStatsTxUnderrunErrors,
       "pppSummaryStatsTable": pppSummaryStatsTable,
       "pppSummaryStatsEntry": pppSummaryStatsEntry,
       "pppSummaryStatsSlotNumber": pppSummaryStatsSlotNumber,
       "pppSummaryStatsMaxLinks": pppSummaryStatsMaxLinks,
       "pppSummaryStatsActiveLinks": pppSummaryStatsActiveLinks,
       "pppSummaryStatsMaxActiveLinks": pppSummaryStatsMaxActiveLinks,
       "pppSummaryStatsFreeLinks": pppSummaryStatsFreeLinks,
       "pppSummaryStatsLinksStarted": pppSummaryStatsLinksStarted,
       "pppSummaryStatsLinksStopped": pppSummaryStatsLinksStopped,
       "pppSummaryStatsLinksModem": pppSummaryStatsLinksModem,
       "pppSummaryStatsLinksHDLC": pppSummaryStatsLinksHDLC,
       "pppSummaryStatsLinksLeased": pppSummaryStatsLinksLeased,
       "pppSummaryStatsLinksNegotiatedLCP": pppSummaryStatsLinksNegotiatedLCP,
       "pppSummaryStatsLinksAuthenticated": pppSummaryStatsLinksAuthenticated,
       "pppSummaryStatsLinksNegotiatedIPCP": pppSummaryStatsLinksNegotiatedIPCP,
       "pppSummaryStatsLinksNegotiatedMLP": pppSummaryStatsLinksNegotiatedMLP,
       "pppSummaryStatsLinksNegotiatedCCP": pppSummaryStatsLinksNegotiatedCCP,
       "pppSummaryStatsLinksNegotiatedIPXCP": pppSummaryStatsLinksNegotiatedIPXCP,
       "pppDeadSessionStatsTable": pppDeadSessionStatsTable,
       "pppDeadSessionStatsEntry": pppDeadSessionStatsEntry,
       "pppDeadSessionStatsSessionID": pppDeadSessionStatsSessionID,
       "pppDeadSessionStatsPhase": pppDeadSessionStatsPhase,
       "pppDeadSessionStatsUserName": pppDeadSessionStatsUserName,
       "pppDeadSessionStatsUpTime": pppDeadSessionStatsUpTime,
       "pppDeadSessionStatsConnectLimit": pppDeadSessionStatsConnectLimit,
       "pppDeadSessionStatsRemainingTime": pppDeadSessionStatsRemainingTime,
       "pppDeadSessionStatsInactivityLimit": pppDeadSessionStatsInactivityLimit,
       "pppDeadSessionStatsInactivityRemaining": pppDeadSessionStatsInactivityRemaining,
       "pppDeadSessionStatsDeadSession": pppDeadSessionStatsDeadSession,
       "pppDeadSessionStatsInterfaceType": pppDeadSessionStatsInterfaceType,
       "pppDeadSessionStatsTxSpeed": pppDeadSessionStatsTxSpeed,
       "pppDeadSessionStatsRxSpeed": pppDeadSessionStatsRxSpeed,
       "pppDeadSessionStatsLCPState": pppDeadSessionStatsLCPState,
       "pppDeadSessionStatsLocalMRU": pppDeadSessionStatsLocalMRU,
       "pppDeadSessionStatsRemoteMRU": pppDeadSessionStatsRemoteMRU,
       "pppDeadSessionStatsLocalAuthProtocol": pppDeadSessionStatsLocalAuthProtocol,
       "pppDeadSessionStatsRemoteAuthProtocol": pppDeadSessionStatsRemoteAuthProtocol,
       "pppDeadSessionStatsLocalPFC": pppDeadSessionStatsLocalPFC,
       "pppDeadSessionStatsRemotePFC": pppDeadSessionStatsRemotePFC,
       "pppDeadSessionStatsLocalACFC": pppDeadSessionStatsLocalACFC,
       "pppDeadSessionStatsRemoteACFC": pppDeadSessionStatsRemoteACFC,
       "pppDeadSessionStatsLocalACCM": pppDeadSessionStatsLocalACCM,
       "pppDeadSessionStatsRemoteACCM": pppDeadSessionStatsRemoteACCM,
       "pppDeadSessionStatsLocalMRRU": pppDeadSessionStatsLocalMRRU,
       "pppDeadSessionStatsRemoteMRRU": pppDeadSessionStatsRemoteMRRU,
       "pppDeadSessionStatsLocalShortSeq": pppDeadSessionStatsLocalShortSeq,
       "pppDeadSessionStatsRemoteShortSeq": pppDeadSessionStatsRemoteShortSeq,
       "pppDeadSessionStatsRemoteAuthenticated": pppDeadSessionStatsRemoteAuthenticated,
       "pppDeadSessionStatsIPCPState": pppDeadSessionStatsIPCPState,
       "pppDeadSessionStatsLocalIPAddress": pppDeadSessionStatsLocalIPAddress,
       "pppDeadSessionStatsRemoteIPAddress": pppDeadSessionStatsRemoteIPAddress,
       "pppDeadSessionStatsDNSAddress1": pppDeadSessionStatsDNSAddress1,
       "pppDeadSessionStatsDNSAddress2": pppDeadSessionStatsDNSAddress2,
       "pppDeadSessionStatsNBNSAddress1": pppDeadSessionStatsNBNSAddress1,
       "pppDeadSessionStatsNBNSAddress2": pppDeadSessionStatsNBNSAddress2,
       "pppDeadSessionStatsLocalVJ": pppDeadSessionStatsLocalVJ,
       "pppDeadSessionStatsLocalVJSlots": pppDeadSessionStatsLocalVJSlots,
       "pppDeadSessionStatsRemoteVJ": pppDeadSessionStatsRemoteVJ,
       "pppDeadSessionStatsRemoteVJSlots": pppDeadSessionStatsRemoteVJSlots,
       "pppDeadSessionStatsIPXCPState": pppDeadSessionStatsIPXCPState,
       "pppDeadSessionStatsRemoteIPXNetwork": pppDeadSessionStatsRemoteIPXNetwork,
       "pppDeadSessionStatsRemoteIPXNode": pppDeadSessionStatsRemoteIPXNode,
       "pppDeadSessionStatsCCPState": pppDeadSessionStatsCCPState,
       "pppDeadSessionStatsLocalCompressAlgorithm": pppDeadSessionStatsLocalCompressAlgorithm,
       "pppDeadSessionStatsLocalCompressHistories": pppDeadSessionStatsLocalCompressHistories,
       "pppDeadSessionStatsRemoteCompressAlgorithm": pppDeadSessionStatsRemoteCompressAlgorithm,
       "pppDeadSessionStatsRemoteCompressHistories": pppDeadSessionStatsRemoteCompressHistories,
       "pppDeadSessionStatsMultilinkActive": pppDeadSessionStatsMultilinkActive,
       "pppDeadSessionStatsMultilinkLinks": pppDeadSessionStatsMultilinkLinks,
       "pppDeadSessionStatsTotalTxSpeed": pppDeadSessionStatsTotalTxSpeed,
       "pppDeadSessionStatsTotalRxSpeed": pppDeadSessionStatsTotalRxSpeed,
       "pppDeadSessionStatsMLPFragmentsReceived": pppDeadSessionStatsMLPFragmentsReceived,
       "pppDeadSessionStatsMLPFragmentsMissing": pppDeadSessionStatsMLPFragmentsMissing,
       "pppDeadSessionStatsMLPFragmentsDropped": pppDeadSessionStatsMLPFragmentsDropped,
       "pppDeadSessionStatsMLPPacketsReassembled": pppDeadSessionStatsMLPPacketsReassembled,
       "pppDeadSessionStatsMLPPacketsNull": pppDeadSessionStatsMLPPacketsNull,
       "pppDeadSessionStatsMultilinkLinksAdded": pppDeadSessionStatsMultilinkLinksAdded,
       "pppDeadSessionStatsMultilinkLinksRemoved": pppDeadSessionStatsMultilinkLinksRemoved,
       "pppDeadSessionStatsMultilinkLinksMax": pppDeadSessionStatsMultilinkLinksMax,
       "pppDeadSessionStatsMultilinkLinksMaxConfig": pppDeadSessionStatsMultilinkLinksMaxConfig,
       "pppDeadSessionStatsTxPackets": pppDeadSessionStatsTxPackets,
       "pppDeadSessionStatsTxPacketsDropped": pppDeadSessionStatsTxPacketsDropped,
       "pppDeadSessionStatsTxBytes": pppDeadSessionStatsTxBytes,
       "pppDeadSessionStatsRxPackets": pppDeadSessionStatsRxPackets,
       "pppDeadSessionStatsRxPacketsDropped": pppDeadSessionStatsRxPacketsDropped,
       "pppDeadSessionStatsRxBytes": pppDeadSessionStatsRxBytes,
       "pppDeadSessionStatsTxCompressing": pppDeadSessionStatsTxCompressing,
       "pppDeadSessionStatsTxBytesBeforeCompress": pppDeadSessionStatsTxBytesBeforeCompress,
       "pppDeadSessionStatsTxBytesAfterCompress": pppDeadSessionStatsTxBytesAfterCompress,
       "pppDeadSessionStatsTxBytesUncompressed": pppDeadSessionStatsTxBytesUncompressed,
       "pppDeadSessionStatsRxBytesBeforeCompress": pppDeadSessionStatsRxBytesBeforeCompress,
       "pppDeadSessionStatsRxBytesAfterCompress": pppDeadSessionStatsRxBytesAfterCompress,
       "pppDeadSessionStatsRxBytesUncompressed": pppDeadSessionStatsRxBytesUncompressed,
       "pppDeadSessionStatsRxCompPacketsDropped": pppDeadSessionStatsRxCompPacketsDropped,
       "pppDeadSessionStatsCCPResetsSent": pppDeadSessionStatsCCPResetsSent,
       "pppDeadSessionStatsCCPResetsReceived": pppDeadSessionStatsCCPResetsReceived,
       "pppDeadSessionStatsRxResourceErrors": pppDeadSessionStatsRxResourceErrors,
       "pppDeadSessionStatsRxQueueErrors": pppDeadSessionStatsRxQueueErrors,
       "pppDeadSessionStatsRxCRCErrors": pppDeadSessionStatsRxCRCErrors,
       "pppDeadSessionStatsRxAbortErrors": pppDeadSessionStatsRxAbortErrors,
       "pppDeadSessionStatsRxOverrunErrors": pppDeadSessionStatsRxOverrunErrors,
       "pppDeadSessionStatsRxBigErrors": pppDeadSessionStatsRxBigErrors,
       "pppDeadSessionStatsRxSmallErrors": pppDeadSessionStatsRxSmallErrors,
       "pppDeadSessionStatsRxAlignErrors": pppDeadSessionStatsRxAlignErrors,
       "pppDeadSessionStatsTxResourceErrors": pppDeadSessionStatsTxResourceErrors,
       "pppDeadSessionStatsTxQueueErrors": pppDeadSessionStatsTxQueueErrors,
       "pppDeadSessionStatsTxBigErrors": pppDeadSessionStatsTxBigErrors,
       "pppDeadSessionStatsTxUnderrunErrors": pppDeadSessionStatsTxUnderrunErrors,
       "l2FTunnelStatusActiveTable": l2FTunnelStatusActiveTable,
       "l2FTunnelStatusActiveEntry": l2FTunnelStatusActiveEntry,
       "l2FTunnelStatusActiveLocalCLID": l2FTunnelStatusActiveLocalCLID,
       "l2FTunnelStatusActiveRemoteCLID": l2FTunnelStatusActiveRemoteCLID,
       "l2FTunnelStatusActiveLocalAddress": l2FTunnelStatusActiveLocalAddress,
       "l2FTunnelStatusActiveRemoteAddress": l2FTunnelStatusActiveRemoteAddress,
       "l2FTunnelStatusActiveState": l2FTunnelStatusActiveState,
       "l2FTunnelStatusActiveUpTime": l2FTunnelStatusActiveUpTime,
       "l2FTunnelStatusActiveActiveLinks": l2FTunnelStatusActiveActiveLinks,
       "l2FTunnelStatusActiveMaxActiveLinks": l2FTunnelStatusActiveMaxActiveLinks,
       "l2FTunnelStatusActivePendingLinks": l2FTunnelStatusActivePendingLinks,
       "l2FTunnelStatusActiveLinksAdded": l2FTunnelStatusActiveLinksAdded,
       "l2FTunnelStatusActiveLinksAddedSuccessfully": l2FTunnelStatusActiveLinksAddedSuccessfully,
       "l2FTunnelStatusActiveLinksAddedUnsuccessfully": l2FTunnelStatusActiveLinksAddedUnsuccessfully,
       "l2FTunnelStatusActiveLinksRemoved": l2FTunnelStatusActiveLinksRemoved,
       "l2FTunnelStatusActiveGotOpened": l2FTunnelStatusActiveGotOpened,
       "l2FTunnelStatusActiveVPOP": l2FTunnelStatusActiveVPOP,
       "l2FTunnelStatusActiveL2FTermationCause": l2FTunnelStatusActiveL2FTermationCause,
       "l2FTunnelStatusInactiveTable": l2FTunnelStatusInactiveTable,
       "l2FTunnelStatusInactiveEntry": l2FTunnelStatusInactiveEntry,
       "l2FTunnelStatusInactiveLocalCLID": l2FTunnelStatusInactiveLocalCLID,
       "l2FTunnelStatusInactiveRemoteCLID": l2FTunnelStatusInactiveRemoteCLID,
       "l2FTunnelStatusInactiveLocalAddress": l2FTunnelStatusInactiveLocalAddress,
       "l2FTunnelStatusInactiveRemoteAddress": l2FTunnelStatusInactiveRemoteAddress,
       "l2FTunnelStatusInactiveState": l2FTunnelStatusInactiveState,
       "l2FTunnelStatusInactiveUpTime": l2FTunnelStatusInactiveUpTime,
       "l2FTunnelStatusInactiveActiveLinks": l2FTunnelStatusInactiveActiveLinks,
       "l2FTunnelStatusInactiveMaxActiveLinks": l2FTunnelStatusInactiveMaxActiveLinks,
       "l2FTunnelStatusInactivePendingLinks": l2FTunnelStatusInactivePendingLinks,
       "l2FTunnelStatusInactiveLinksAdded": l2FTunnelStatusInactiveLinksAdded,
       "l2FTunnelStatusInactiveLinksAddedSuccessfully": l2FTunnelStatusInactiveLinksAddedSuccessfully,
       "l2FTunnelStatusInactiveLinksAddedUnsuccessfully": l2FTunnelStatusInactiveLinksAddedUnsuccessfully,
       "l2FTunnelStatusInactiveLinksRemoved": l2FTunnelStatusInactiveLinksRemoved,
       "l2FTunnelStatusInactiveGotOpened": l2FTunnelStatusInactiveGotOpened,
       "l2FTunnelStatusInactiveVPOP": l2FTunnelStatusInactiveVPOP,
       "l2FTunnelStatusInactiveL2FTermationCause": l2FTunnelStatusInactiveL2FTermationCause,
       "l2FLinkStatusTable": l2FLinkStatusTable,
       "l2FLinkStatusEntry": l2FLinkStatusEntry,
       "l2FLinkStatusLocalCLID": l2FLinkStatusLocalCLID,
       "l2FLinkStatusIndex": l2FLinkStatusIndex,
       "l2FLinkStatusSessionID": l2FLinkStatusSessionID,
       "l2FLinkStatusVPOP": l2FLinkStatusVPOP,
       "l2FLinkStatusMIDValue": l2FLinkStatusMIDValue,
       "l2FLinkStatusState": l2FLinkStatusState,
       "l2FLinkStatusUpTime": l2FLinkStatusUpTime,
       "l2FLinkStatusUserName": l2FLinkStatusUserName,
       "l2FLinkStatusTxPackets": l2FLinkStatusTxPackets,
       "l2FLinkStatusTxBytes": l2FLinkStatusTxBytes,
       "l2FLinkStatusRxPackets": l2FLinkStatusRxPackets,
       "l2FLinkStatusRxBytes": l2FLinkStatusRxBytes,
       "l2FLinkStatusL2FTermationCause": l2FLinkStatusL2FTermationCause,
       "l2FLogEntryTable": l2FLogEntryTable,
       "l2FLogEntryEntry": l2FLogEntryEntry,
       "l2FLogEntryLocalCLID": l2FLogEntryLocalCLID,
       "l2FLogEntryIndex": l2FLogEntryIndex,
       "l2FLogEntryMinIndex": l2FLogEntryMinIndex,
       "l2FLogEntryMaxIndex": l2FLogEntryMaxIndex,
       "l2FLogEntryUpTime": l2FLogEntryUpTime,
       "l2FLogEntryEntryText": l2FLogEntryEntryText,
       "mamLogEntryTable": mamLogEntryTable,
       "mamLogEntryEntry": mamLogEntryEntry,
       "mamLogEntryIndex": mamLogEntryIndex,
       "mamLogEntryMinIndex": mamLogEntryMinIndex,
       "mamLogEntryMaxIndex": mamLogEntryMaxIndex,
       "mamLogEntryEntryText": mamLogEntryEntryText,
       "modemStatsTable": modemStatsTable,
       "modemStatsEntry": modemStatsEntry,
       "modemStatsState": modemStatsState,
       "modemStatsSlot": modemStatsSlot,
       "modemStatsIOP": modemStatsIOP,
       "modemStatsDMM": modemStatsDMM,
       "modemStatsPack": modemStatsPack,
       "modemStatsModem": modemStatsModem,
       "modemStatsCurrentSessionID": modemStatsCurrentSessionID,
       "modemStatsModemIndex": modemStatsModemIndex,
       "modemStatsRPI": modemStatsRPI,
       "modemStatsTotalCalls": modemStatsTotalCalls,
       "modemStatsConnectedCalls": modemStatsConnectedCalls,
       "modemStatsLast32Calls": modemStatsLast32Calls,
       "modemStatsConnectedWin": modemStatsConnectedWin,
       "modemStatsConnectedLose": modemStatsConnectedLose,
       "modemStatsAuthCalls": modemStatsAuthCalls,
       "modemStatsLast32Auth": modemStatsLast32Auth,
       "modemStatsAuthWin": modemStatsAuthWin,
       "modemStatsAuthLose": modemStatsAuthLose,
       "modemStatsECCalls": modemStatsECCalls,
       "modemStatsDCCalls": modemStatsDCCalls,
       "modemStatsK56Calls": modemStatsK56Calls,
       "modemStatsV90Calls": modemStatsV90Calls,
       "modemStatsV34Calls": modemStatsV34Calls,
       "modemStatsV32Calls": modemStatsV32Calls,
       "modemStatsStatsSamples": modemStatsStatsSamples,
       "modemStatsInitialTxSum": modemStatsInitialTxSum,
       "modemStatsMinTxSum": modemStatsMinTxSum,
       "modemStatsMaxTxSum": modemStatsMaxTxSum,
       "modemStatsFinalTxSum": modemStatsFinalTxSum,
       "modemStatsMinTxSpeed": modemStatsMinTxSpeed,
       "modemStatsMaxTxSpeed": modemStatsMaxTxSpeed,
       "modemStatsInitialRxSum": modemStatsInitialRxSum,
       "modemStatsMinRxSum": modemStatsMinRxSum,
       "modemStatsMaxRxSum": modemStatsMaxRxSum,
       "modemStatsFinalRxSum": modemStatsFinalRxSum,
       "modemStatsMinRxSpeed": modemStatsMinRxSpeed,
       "modemStatsMaxRxSpeed": modemStatsMaxRxSpeed,
       "modemStatsDownloadAttempts": modemStatsDownloadAttempts,
       "modemStatsDownloadSuccesses": modemStatsDownloadSuccesses,
       "modemStatsResetFailures": modemStatsResetFailures,
       "modemStatsResetRevivals": modemStatsResetRevivals,
       "modemStatsPackCrashes": modemStatsPackCrashes,
       "modemStatsPackRevivals": modemStatsPackRevivals,
       "modemCallStatsTable": modemCallStatsTable,
       "modemCallStatsEntry": modemCallStatsEntry,
       "modemCallStatsTxInitialSpeed": modemCallStatsTxInitialSpeed,
       "modemCallStatsTxFinalSpeed": modemCallStatsTxFinalSpeed,
       "modemCallStatsTxMinSpeed": modemCallStatsTxMinSpeed,
       "modemCallStatsTxMaxSpeed": modemCallStatsTxMaxSpeed,
       "modemCallStatsRxInitialSpeed": modemCallStatsRxInitialSpeed,
       "modemCallStatsRxFinalSpeed": modemCallStatsRxFinalSpeed,
       "modemCallStatsRxMinSpeed": modemCallStatsRxMinSpeed,
       "modemCallStatsRxMaxSpeed": modemCallStatsRxMaxSpeed,
       "modemCallStatsECProtocol": modemCallStatsECProtocol,
       "modemCallStatsDCProtocol": modemCallStatsDCProtocol,
       "modemCallStatsModulationType": modemCallStatsModulationType,
       "modemCallStatsInitialModulationType": modemCallStatsInitialModulationType,
       "modemCallStatsSymbolRate": modemCallStatsSymbolRate,
       "modemCallStatsTxCarrierFrequency": modemCallStatsTxCarrierFrequency,
       "modemCallStatsRxCarrierFrequency": modemCallStatsRxCarrierFrequency,
       "modemCallStatsLastAGCGainValue": modemCallStatsLastAGCGainValue,
       "modemCallStatsMinAGCGainValue": modemCallStatsMinAGCGainValue,
       "modemCallStatsMaxAGCGainValue": modemCallStatsMaxAGCGainValue,
       "modemCallStatsTxLevel": modemCallStatsTxLevel,
       "modemCallStatsTxLevelReduction": modemCallStatsTxLevelReduction,
       "modemCallStatsLastEQMValue": modemCallStatsLastEQMValue,
       "modemCallStatsMinEQMValue": modemCallStatsMinEQMValue,
       "modemCallStatsMaxEQMValue": modemCallStatsMaxEQMValue,
       "modemCallStatsEQMHits": modemCallStatsEQMHits,
       "modemCallStatsEQMSumLow": modemCallStatsEQMSumLow,
       "modemCallStatsEQMSumMiddle": modemCallStatsEQMSumMiddle,
       "modemCallStatsEQMSumHigh": modemCallStatsEQMSumHigh,
       "modemCallStatsEQM1Second": modemCallStatsEQM1Second,
       "modemCallStatsEQM2Seconds": modemCallStatsEQM2Seconds,
       "modemCallStatsEQM3Seconds": modemCallStatsEQM3Seconds,
       "modemCallStatsEQM4Seconds": modemCallStatsEQM4Seconds,
       "modemCallStatsEQM5Seconds": modemCallStatsEQM5Seconds,
       "modemCallStatsEQM6Seconds": modemCallStatsEQM6Seconds,
       "modemCallStatsEQM7Seconds": modemCallStatsEQM7Seconds,
       "modemCallStatsEQM8Seconds": modemCallStatsEQM8Seconds,
       "modemCallStatsEQM9Seconds": modemCallStatsEQM9Seconds,
       "modemCallStatsEQM10Seconds": modemCallStatsEQM10Seconds,
       "modemCallStatsSNRRatio": modemCallStatsSNRRatio,
       "modemCallStatsMinSNRValue": modemCallStatsMinSNRValue,
       "modemCallStatsMaxSNRValue": modemCallStatsMaxSNRValue,
       "modemCallStatsLocalRetrains": modemCallStatsLocalRetrains,
       "modemCallStatsRemoteRetrains": modemCallStatsRemoteRetrains,
       "modemCallStatsLocalRateRenegs": modemCallStatsLocalRateRenegs,
       "modemCallStatsRemoteRateRenegs": modemCallStatsRemoteRateRenegs,
       "modemCallStatsTxNonlinearEncoding": modemCallStatsTxNonlinearEncoding,
       "modemCallStatsRxNonlinearEncoding": modemCallStatsRxNonlinearEncoding,
       "modemCallStatsTxPrecoding": modemCallStatsTxPrecoding,
       "modemCallStatsRxPrecoding": modemCallStatsRxPrecoding,
       "modemCallStatsTxShaping": modemCallStatsTxShaping,
       "modemCallStatsRxShaping": modemCallStatsRxShaping,
       "modemCallStatsTrellisMapping": modemCallStatsTrellisMapping,
       "modemCallStatsPreEmphasis": modemCallStatsPreEmphasis,
       "modemCallStatsUpperBandEdge": modemCallStatsUpperBandEdge,
       "modemCallStatsLowerBandEdge": modemCallStatsLowerBandEdge,
       "modemCallStatsRTTHigh": modemCallStatsRTTHigh,
       "modemCallStatsRTTLow": modemCallStatsRTTLow,
       "modemCallStatsInfo0SequenceHigh": modemCallStatsInfo0SequenceHigh,
       "modemCallStatsInfo0SequenceLow": modemCallStatsInfo0SequenceLow,
       "modemCallStatsRxMPSequenceByte1Low": modemCallStatsRxMPSequenceByte1Low,
       "modemCallStatsRxMPSequenceByte1High": modemCallStatsRxMPSequenceByte1High,
       "modemCallStatsRxMPSequenceByte2Low": modemCallStatsRxMPSequenceByte2Low,
       "modemCallStatsRxMPSequenceByte2High": modemCallStatsRxMPSequenceByte2High,
       "modemCallStatsHighestTxState": modemCallStatsHighestTxState,
       "modemCallStatsHighestRxState": modemCallStatsHighestRxState,
       "modemCallStatsLastTransmitState": modemCallStatsLastTransmitState,
       "modemCallStatsLastReceiveState": modemCallStatsLastReceiveState,
       "modemCallStatsConnectTimeHours": modemCallStatsConnectTimeHours,
       "modemCallStatsConnectTimeMinutes": modemCallStatsConnectTimeMinutes,
       "modemCallStatsConnectTimeSeconds": modemCallStatsConnectTimeSeconds,
       "modemCallStatsAutoGainAmplitude": modemCallStatsAutoGainAmplitude,
       "modemCallStatsAutoGainAttenuation": modemCallStatsAutoGainAttenuation,
       "modemCallStatsDigitalPadDetected": modemCallStatsDigitalPadDetected,
       "modemCallStatsRBSPattern": modemCallStatsRBSPattern,
       "modemCallStatsRBSRateDrop": modemCallStatsRBSRateDrop,
       "modemCallStatsMaxTxRetransmissions": modemCallStatsMaxTxRetransmissions,
       "modemCallStatsTotalTxRetransmissions": modemCallStatsTotalTxRetransmissions,
       "modemCallStatsNumberOfLAPMREJSReceived": modemCallStatsNumberOfLAPMREJSReceived,
       "modemCallStatsNumberOfLAPMREJSTransmitted": modemCallStatsNumberOfLAPMREJSTransmitted,
       "modemCallStatsNumberOfTXBlocksHigh": modemCallStatsNumberOfTXBlocksHigh,
       "modemCallStatsNumberOfTXBlocksLow": modemCallStatsNumberOfTXBlocksLow,
       "modemCallStatsNumberOfRXBlocksHigh": modemCallStatsNumberOfRXBlocksHigh,
       "modemCallStatsNumberOfRXBlocksLow": modemCallStatsNumberOfRXBlocksLow,
       "modemCallStatsNumberOfTXCharsMSB": modemCallStatsNumberOfTXCharsMSB,
       "modemCallStatsNumberOfTXChars2ndByte": modemCallStatsNumberOfTXChars2ndByte,
       "modemCallStatsNumberOfTXChars3rdByte": modemCallStatsNumberOfTXChars3rdByte,
       "modemCallStatsNumberOfTXCharsLSB": modemCallStatsNumberOfTXCharsLSB,
       "modemCallStatsNumberOfRXCharsMSB": modemCallStatsNumberOfRXCharsMSB,
       "modemCallStatsNumberOfRXChars2ndByte": modemCallStatsNumberOfRXChars2ndByte,
       "modemCallStatsNumberOfRXChars3rdByte": modemCallStatsNumberOfRXChars3rdByte,
       "modemCallStatsNumberOfRXCharsLSB": modemCallStatsNumberOfRXCharsLSB,
       "modemCallStatsDisconnectReason": modemCallStatsDisconnectReason,
       "modemCallStatsRetrainReason": modemCallStatsRetrainReason,
       "modemCallStatsAbortCode": modemCallStatsAbortCode,
       "modemCallStatsK56Status": modemCallStatsK56Status,
       "modemCallStatsV8ManufacturerID": modemCallStatsV8ManufacturerID,
       "modemCallStatsV8LicenseeCode": modemCallStatsV8LicenseeCode,
       "modemCallStatsV8Capabilities": modemCallStatsV8Capabilities,
       "modemCallStatsV8FlexVersion": modemCallStatsV8FlexVersion,
       "modemCallStatsV8DataPumpRev": modemCallStatsV8DataPumpRev,
       "modemCallStatsV8ControllerRev": modemCallStatsV8ControllerRev,
       "modemCallStatsV8Progress": modemCallStatsV8Progress,
       "modemCallStatsV90DigitalPadHigh": modemCallStatsV90DigitalPadHigh,
       "modemCallStatsV90DigitalPadLow": modemCallStatsV90DigitalPadLow,
       "modemCallStatsV90IMDRatio": modemCallStatsV90IMDRatio,
       "modemCallStatsHandshakeTime": modemCallStatsHandshakeTime,
       "modemCallStatsNumberOfHandshakeRetries": modemCallStatsNumberOfHandshakeRetries,
       "modemCallStatsECState1": modemCallStatsECState1,
       "modemCallStatsECState2": modemCallStatsECState2,
       "modemCallStatsFirmwareState": modemCallStatsFirmwareState,
       "modemCallStatsHighAddrOfMEMACCFailure": modemCallStatsHighAddrOfMEMACCFailure,
       "modemCallStatsLowAddrOfMEMACCFailure": modemCallStatsLowAddrOfMEMACCFailure,
       "modemCallStatsMinutesSinceRetrain": modemCallStatsMinutesSinceRetrain,
       "modemCallStatsWAStatus": modemCallStatsWAStatus,
       "modemCallStatsRoundTripTime": modemCallStatsRoundTripTime,
       "modemCallStatsDataIsValid": modemCallStatsDataIsValid,
       "modemCallStatsSessionID": modemCallStatsSessionID,
       "modemCallStatsSlotIndex": modemCallStatsSlotIndex,
       "modemCallStatsModemIndex": modemCallStatsModemIndex,
       "modemSummaryStatsTable": modemSummaryStatsTable,
       "modemSummaryStatsEntry": modemSummaryStatsEntry,
       "modemSummaryStatsSlotNumber": modemSummaryStatsSlotNumber,
       "modemSummaryStatsModemCount": modemSummaryStatsModemCount,
       "modemSummaryStatsDisabledCount": modemSummaryStatsDisabledCount,
       "modemSummaryStatsNoDownloadCount": modemSummaryStatsNoDownloadCount,
       "modemSummaryStatsDeadCount": modemSummaryStatsDeadCount,
       "modemSummaryStatsRemovedCount": modemSummaryStatsRemovedCount,
       "modemSummaryStatsIdleCount": modemSummaryStatsIdleCount,
       "modemSummaryStatsActiveCount": modemSummaryStatsActiveCount,
       "modemSummaryStatsDownloadingCount": modemSummaryStatsDownloadingCount,
       "modemSummaryStatsTotalCalls": modemSummaryStatsTotalCalls,
       "modemSummaryStatsConnectedCalls": modemSummaryStatsConnectedCalls,
       "modemSummaryStatsAuthCalls": modemSummaryStatsAuthCalls,
       "modemSummaryStatsECCalls": modemSummaryStatsECCalls,
       "modemSummaryStatsDCCalls": modemSummaryStatsDCCalls,
       "modemSummaryStatsK56Calls": modemSummaryStatsK56Calls,
       "modemSummaryStatsV90Calls": modemSummaryStatsV90Calls,
       "modemSummaryStatsV34Calls": modemSummaryStatsV34Calls,
       "modemSummaryStatsV32Calls": modemSummaryStatsV32Calls,
       "modemSummaryStatsReuseSuspectModems": modemSummaryStatsReuseSuspectModems,
       "modemSummaryStatsUpTime": modemSummaryStatsUpTime,
       "modemSummaryStatsMaximumCalls": modemSummaryStatsMaximumCalls,
       "modemIntervalStatsTable": modemIntervalStatsTable,
       "modemIntervalStatsEntry": modemIntervalStatsEntry,
       "modemIntervalStatsIndex": modemIntervalStatsIndex,
       "modemIntervalStatsStartTime": modemIntervalStatsStartTime,
       "modemIntervalStatsStopTime": modemIntervalStatsStopTime,
       "modemIntervalStatsModemCount": modemIntervalStatsModemCount,
       "modemIntervalStatsDisabledCount": modemIntervalStatsDisabledCount,
       "modemIntervalStatsNoDownloadCount": modemIntervalStatsNoDownloadCount,
       "modemIntervalStatsDeadCount": modemIntervalStatsDeadCount,
       "modemIntervalStatsRemovedCount": modemIntervalStatsRemovedCount,
       "modemIntervalStatsIdleCount": modemIntervalStatsIdleCount,
       "modemIntervalStatsActiveCount": modemIntervalStatsActiveCount,
       "modemIntervalStatsDownloadingCount": modemIntervalStatsDownloadingCount,
       "modemIntervalStatsTotalCalls": modemIntervalStatsTotalCalls,
       "modemIntervalStatsConnectedCalls": modemIntervalStatsConnectedCalls,
       "modemIntervalStatsAuthCalls": modemIntervalStatsAuthCalls,
       "modemIntervalStatsECCalls": modemIntervalStatsECCalls,
       "modemIntervalStatsDCCalls": modemIntervalStatsDCCalls,
       "modemIntervalStatsK56Calls": modemIntervalStatsK56Calls,
       "modemIntervalStatsV90Calls": modemIntervalStatsV90Calls,
       "modemIntervalStatsV34Calls": modemIntervalStatsV34Calls,
       "modemIntervalStatsV32Calls": modemIntervalStatsV32Calls,
       "modemIntervalStatsOverallTotalCalls": modemIntervalStatsOverallTotalCalls,
       "modemIntervalStatsOverallConnectedCalls": modemIntervalStatsOverallConnectedCalls,
       "modemIntervalStatsOverallAuthCalls": modemIntervalStatsOverallAuthCalls,
       "modemSessionStatsTable": modemSessionStatsTable,
       "modemSessionStatsEntry": modemSessionStatsEntry,
       "modemSessionStatsDataValidity": modemSessionStatsDataValidity,
       "modemSessionStatsSessionID": modemSessionStatsSessionID,
       "modemSessionStatsSlotNumber": modemSessionStatsSlotNumber,
       "modemSessionStatsIOPNumber": modemSessionStatsIOPNumber,
       "modemSessionStatsDMMNumber": modemSessionStatsDMMNumber,
       "modemSessionStatsPackNumber": modemSessionStatsPackNumber,
       "modemSessionStatsModemNumber": modemSessionStatsModemNumber,
       "modemSessionStatsModemIndex": modemSessionStatsModemIndex,
       "modemSessionStatsTDMStream": modemSessionStatsTDMStream,
       "modemSessionStatsTDMSlot": modemSessionStatsTDMSlot,
       "modemSessionStatsInitialTxSpeed": modemSessionStatsInitialTxSpeed,
       "modemSessionStatsInitialRxSpeed": modemSessionStatsInitialRxSpeed,
       "modemSessionStatsConnectString": modemSessionStatsConnectString,
       "modemSessionStatsAmpV2String": modemSessionStatsAmpV2String,
       "modemSessionStats2Table": modemSessionStats2Table,
       "modemSessionStats2Entry": modemSessionStats2Entry,
       "modemSessionStats2DataValidity": modemSessionStats2DataValidity,
       "modemSessionStats2SessionID": modemSessionStats2SessionID,
       "modemSessionStats2SlotNumber": modemSessionStats2SlotNumber,
       "modemSessionStats2IOPNumber": modemSessionStats2IOPNumber,
       "modemSessionStats2DMMNumber": modemSessionStats2DMMNumber,
       "modemSessionStats2PackNumber": modemSessionStats2PackNumber,
       "modemSessionStats2ModemNumber": modemSessionStats2ModemNumber,
       "modemSessionStats2ModemIndex": modemSessionStats2ModemIndex,
       "modemSessionStats2TDMStream": modemSessionStats2TDMStream,
       "modemSessionStats2TDMSlot": modemSessionStats2TDMSlot,
       "modemSessionStats2InitialTxSpeed": modemSessionStats2InitialTxSpeed,
       "modemSessionStats2InitialRxSpeed": modemSessionStats2InitialRxSpeed,
       "modemSessionStats2ConnectString": modemSessionStats2ConnectString,
       "modemSessionStats2AmpV2String": modemSessionStats2AmpV2String,
       "dvsStatusTable": dvsStatusTable,
       "dvsStatusEntry": dvsStatusEntry,
       "dvsStatusLocalCLID": dvsStatusLocalCLID,
       "dvsStatusRemoteCLID": dvsStatusRemoteCLID,
       "dvsStatusLocalAddress": dvsStatusLocalAddress,
       "dvsStatusRemoteAddress": dvsStatusRemoteAddress,
       "dvsStatusTunnelState": dvsStatusTunnelState,
       "dvsStatusUpTime": dvsStatusUpTime,
       "dvsStatusMacSlotNumber": dvsStatusMacSlotNumber,
       "dvsStatusVPOP": dvsStatusVPOP,
       "dvsStatusGreInPackets": dvsStatusGreInPackets,
       "dvsStatusGreOutPackets": dvsStatusGreOutPackets,
       "dvsStatusGreChecksumError": dvsStatusGreChecksumError,
       "dvsStatusGreInDropped": dvsStatusGreInDropped,
       "dvsStatusGreOutDropped": dvsStatusGreOutDropped,
       "dvsStatusDeadSession": dvsStatusDeadSession,
       "dvsStatusRemoteIPXNetwork": dvsStatusRemoteIPXNetwork,
       "dvsStatusRemoteIPXNode": dvsStatusRemoteIPXNode,
       "dvsStatusIPInPackets": dvsStatusIPInPackets,
       "dvsStatusIPOutPackets": dvsStatusIPOutPackets,
       "dvsStatusIPXInPackets": dvsStatusIPXInPackets,
       "dvsStatusIPXOutPackets": dvsStatusIPXOutPackets,
       "dvsLogEntryTable": dvsLogEntryTable,
       "dvsLogEntryEntry": dvsLogEntryEntry,
       "dvsLogEntryIndex": dvsLogEntryIndex,
       "dvsLogEntryMinIndex": dvsLogEntryMinIndex,
       "dvsLogEntryMaxIndex": dvsLogEntryMaxIndex,
       "dvsLogEntryEntryText": dvsLogEntryEntryText,
       "dvsLogEntryTunnelCLID": dvsLogEntryTunnelCLID,
       "dvsLogEntryUpTime": dvsLogEntryUpTime,
       "l2TPTunnelStatusActiveTable": l2TPTunnelStatusActiveTable,
       "l2TPTunnelStatusActiveEntry": l2TPTunnelStatusActiveEntry,
       "l2TPTunnelStatusActiveSlot": l2TPTunnelStatusActiveSlot,
       "l2TPTunnelStatusActiveLocalID": l2TPTunnelStatusActiveLocalID,
       "l2TPTunnelStatusActiveRemoteID": l2TPTunnelStatusActiveRemoteID,
       "l2TPTunnelStatusActiveLocalAddress": l2TPTunnelStatusActiveLocalAddress,
       "l2TPTunnelStatusActiveRemoteAddress": l2TPTunnelStatusActiveRemoteAddress,
       "l2TPTunnelStatusActiveState": l2TPTunnelStatusActiveState,
       "l2TPTunnelStatusActiveUpTime": l2TPTunnelStatusActiveUpTime,
       "l2TPTunnelStatusActiveActiveLinks": l2TPTunnelStatusActiveActiveLinks,
       "l2TPTunnelStatusActiveMaxActiveLinks": l2TPTunnelStatusActiveMaxActiveLinks,
       "l2TPTunnelStatusActivePendingLinks": l2TPTunnelStatusActivePendingLinks,
       "l2TPTunnelStatusActiveLinksAdded": l2TPTunnelStatusActiveLinksAdded,
       "l2TPTunnelStatusActiveLinksAddedSuccessfully": l2TPTunnelStatusActiveLinksAddedSuccessfully,
       "l2TPTunnelStatusActiveLinksAddedUnsuccessfully": l2TPTunnelStatusActiveLinksAddedUnsuccessfully,
       "l2TPTunnelStatusActiveLinksRemoved": l2TPTunnelStatusActiveLinksRemoved,
       "l2TPTunnelStatusActiveGotOpened": l2TPTunnelStatusActiveGotOpened,
       "l2TPTunnelStatusActiveVPOP": l2TPTunnelStatusActiveVPOP,
       "l2TPTunnelStatusActiveL2TPTermationCause": l2TPTunnelStatusActiveL2TPTermationCause,
       "l2TPTunnelStatusInactiveTable": l2TPTunnelStatusInactiveTable,
       "l2TPTunnelStatusInactiveEntry": l2TPTunnelStatusInactiveEntry,
       "l2TPTunnelStatusInactiveSlot": l2TPTunnelStatusInactiveSlot,
       "l2TPTunnelStatusInactiveLocalID": l2TPTunnelStatusInactiveLocalID,
       "l2TPTunnelStatusInactiveRemoteID": l2TPTunnelStatusInactiveRemoteID,
       "l2TPTunnelStatusInactiveLocalAddress": l2TPTunnelStatusInactiveLocalAddress,
       "l2TPTunnelStatusInactiveRemoteAddress": l2TPTunnelStatusInactiveRemoteAddress,
       "l2TPTunnelStatusInactiveState": l2TPTunnelStatusInactiveState,
       "l2TPTunnelStatusInactiveUpTime": l2TPTunnelStatusInactiveUpTime,
       "l2TPTunnelStatusInactiveActiveLinks": l2TPTunnelStatusInactiveActiveLinks,
       "l2TPTunnelStatusInactiveMaxActiveLinks": l2TPTunnelStatusInactiveMaxActiveLinks,
       "l2TPTunnelStatusInactivePendingLinks": l2TPTunnelStatusInactivePendingLinks,
       "l2TPTunnelStatusInactiveLinksAdded": l2TPTunnelStatusInactiveLinksAdded,
       "l2TPTunnelStatusInactiveLinksAddedSuccessfully": l2TPTunnelStatusInactiveLinksAddedSuccessfully,
       "l2TPTunnelStatusInactiveLinksAddedUnsuccessfully": l2TPTunnelStatusInactiveLinksAddedUnsuccessfully,
       "l2TPTunnelStatusInactiveLinksRemoved": l2TPTunnelStatusInactiveLinksRemoved,
       "l2TPTunnelStatusInactiveGotOpened": l2TPTunnelStatusInactiveGotOpened,
       "l2TPTunnelStatusInactiveVPOP": l2TPTunnelStatusInactiveVPOP,
       "l2TPTunnelStatusInactiveL2TPTermationCause": l2TPTunnelStatusInactiveL2TPTermationCause,
       "l2TPLinkStatusTable": l2TPLinkStatusTable,
       "l2TPLinkStatusEntry": l2TPLinkStatusEntry,
       "l2TPLinkStatusLocalID": l2TPLinkStatusLocalID,
       "l2TPLinkStatusRemoteID": l2TPLinkStatusRemoteID,
       "l2TPLinkStatusIndex": l2TPLinkStatusIndex,
       "l2TPLinkStatusSessionID": l2TPLinkStatusSessionID,
       "l2TPLinkStatusVPOP": l2TPLinkStatusVPOP,
       "l2TPLinkStatusState": l2TPLinkStatusState,
       "l2TPLinkStatusUpTime": l2TPLinkStatusUpTime,
       "l2TPLinkStatusUserName": l2TPLinkStatusUserName,
       "l2TPLinkStatusTxPackets": l2TPLinkStatusTxPackets,
       "l2TPLinkStatusTxBytes": l2TPLinkStatusTxBytes,
       "l2TPLinkStatusRxPackets": l2TPLinkStatusRxPackets,
       "l2TPLinkStatusRxBytes": l2TPLinkStatusRxBytes,
       "l2TPLinkStatusL2TPTermationCause": l2TPLinkStatusL2TPTermationCause,
       "l2TPLogEntryTable": l2TPLogEntryTable,
       "l2TPLogEntryEntry": l2TPLogEntryEntry,
       "l2TPLogEntryLocalID": l2TPLogEntryLocalID,
       "l2TPLogEntryIndex": l2TPLogEntryIndex,
       "l2TPLogEntryMinIndex": l2TPLogEntryMinIndex,
       "l2TPLogEntryMaxIndex": l2TPLogEntryMaxIndex,
       "l2TPLogEntryUpTime": l2TPLogEntryUpTime,
       "l2TPLogEntryEntryText": l2TPLogEntryEntryText,
       "dvsDeadLogEntryTable": dvsDeadLogEntryTable,
       "dvsDeadLogEntryEntry": dvsDeadLogEntryEntry,
       "dvsDeadLogEntryIndex": dvsDeadLogEntryIndex,
       "dvsDeadLogEntryMinIndex": dvsDeadLogEntryMinIndex,
       "dvsDeadLogEntryMaxIndex": dvsDeadLogEntryMaxIndex,
       "dvsDeadLogEntryEntryText": dvsDeadLogEntryEntryText,
       "dvsDeadLogEntryTunnelCLID": dvsDeadLogEntryTunnelCLID,
       "dvsDeadLogEntryUpTime": dvsDeadLogEntryUpTime,
       "dvsStatusDeadTable": dvsStatusDeadTable,
       "dvsStatusDeadEntry": dvsStatusDeadEntry,
       "dvsStatusDeadTunnelCLID": dvsStatusDeadTunnelCLID,
       "dvsStatusDeadRemoteCLID": dvsStatusDeadRemoteCLID,
       "dvsStatusDeadRemoteAddress": dvsStatusDeadRemoteAddress,
       "dvsStatusDeadTunnelState": dvsStatusDeadTunnelState,
       "dvsStatusDeadUpTime": dvsStatusDeadUpTime,
       "dvsStatusDeadMacSlotNumber": dvsStatusDeadMacSlotNumber,
       "dvsStatusDeadVPOP": dvsStatusDeadVPOP,
       "dvsStatusDeadGreInPackets": dvsStatusDeadGreInPackets,
       "dvsStatusDeadGreOutPackets": dvsStatusDeadGreOutPackets,
       "dvsStatusDeadGreChecksumError": dvsStatusDeadGreChecksumError,
       "dvsStatusDeadGreInDropped": dvsStatusDeadGreInDropped,
       "dvsStatusDeadGreOutDropped": dvsStatusDeadGreOutDropped,
       "dvsStatusDeadDeadSession": dvsStatusDeadDeadSession,
       "ipsecCountersTable": ipsecCountersTable,
       "ipsecCountersEntry": ipsecCountersEntry,
       "ipsecCountersOutboundCounter": ipsecCountersOutboundCounter,
       "ipsecCountersInboundCounter": ipsecCountersInboundCounter,
       "ipsecCountersOutboundDropCounter": ipsecCountersOutboundDropCounter,
       "ipsecCountersInboundDropCounter": ipsecCountersInboundDropCounter,
       "dacStatusTable": dacStatusTable,
       "dacStatusEntry": dacStatusEntry,
       "dacStatusClockSourcePrimary": dacStatusClockSourcePrimary,
       "dacStatusClockSourceSecondary": dacStatusClockSourceSecondary,
       "dacStatusLTMType": dacStatusLTMType,
       "dacTraceTable": dacTraceTable,
       "dacTraceEntry": dacTraceEntry,
       "dacTraceIndex": dacTraceIndex,
       "dacTraceLocation": dacTraceLocation,
       "dacTraceDirection": dacTraceDirection,
       "dacTraceType": dacTraceType,
       "dacTraceTimestamp": dacTraceTimestamp,
       "dacTraceLen": dacTraceLen,
       "dacTraceData": dacTraceData,
       "t3StatsTable": t3StatsTable,
       "t3StatsEntry": t3StatsEntry,
       "t3StatsLineState": t3StatsLineState,
       "t3StatsSlotIndex": t3StatsSlotIndex,
       "t3StatsLineNumber": t3StatsLineNumber,
       "t3StatsRedundant": t3StatsRedundant,
       "t3StatsDs1Count": t3StatsDs1Count,
       "t3StatsActiveDs1Count": t3StatsActiveDs1Count,
       "t3StatsExternalClockPort": t3StatsExternalClockPort,
       "dacClockingTable": dacClockingTable,
       "dacClockingEntry": dacClockingEntry,
       "dacClockingIndex": dacClockingIndex,
       "dacClockingClockSourcePrimary": dacClockingClockSourcePrimary,
       "dacClockingClockSourceSecondary": dacClockingClockSourceSecondary,
       "dacClockingForce": dacClockingForce,
       "t1StatsTable": t1StatsTable,
       "t1StatsEntry": t1StatsEntry,
       "t1StatsAlarmStatus": t1StatsAlarmStatus,
       "t1StatsSlotIndex": t1StatsSlotIndex,
       "t1StatsLineNumber": t1StatsLineNumber,
       "t1CountsTable": t1CountsTable,
       "t1CountsEntry": t1CountsEntry,
       "t1CountsChannelCount": t1CountsChannelCount,
       "t1CountsChannelsInUse": t1CountsChannelsInUse,
       "t1CountsIncomingCallAttempts": t1CountsIncomingCallAttempts,
       "t1CountsIncomingConnects": t1CountsIncomingConnects,
       "t1CountsIncomingDisconnects": t1CountsIncomingDisconnects,
       "t1CountsOutgoingCallAttempts": t1CountsOutgoingCallAttempts,
       "t1CountsOutgoingConnects": t1CountsOutgoingConnects,
       "t1CountsOutgoingDisconnects": t1CountsOutgoingDisconnects,
       "t1CountsSessionAbortMessages": t1CountsSessionAbortMessages,
       "t1CountsSlotIndex": t1CountsSlotIndex,
       "t1CountsLineNumber": t1CountsLineNumber,
       "t1SummaryStatsTable": t1SummaryStatsTable,
       "t1SummaryStatsEntry": t1SummaryStatsEntry,
       "t1SummaryStatsRingingChannels": t1SummaryStatsRingingChannels,
       "t1SummaryStatsConnectedChannels": t1SummaryStatsConnectedChannels,
       "t1SummaryStatsClearingChannels": t1SummaryStatsClearingChannels,
       "t1SummaryStatsSlotIndex": t1SummaryStatsSlotIndex,
       "t1SummaryStatsLineNumber": t1SummaryStatsLineNumber,
       "t1SummaryStatsFunctionalChannels": t1SummaryStatsFunctionalChannels,
       "t1SummaryStatsIdleChannels": t1SummaryStatsIdleChannels,
       "ds0StatsTable": ds0StatsTable,
       "ds0StatsEntry": ds0StatsEntry,
       "ds0StatsInCalls": ds0StatsInCalls,
       "ds0StatsInConnected": ds0StatsInConnected,
       "ds0StatsOutCalls": ds0StatsOutCalls,
       "ds0StatsOutConnected": ds0StatsOutConnected,
       "ds0StatsInCleared": ds0StatsInCleared,
       "ds0StatsOutCleared": ds0StatsOutCleared,
       "ds0StatsSlotIndex": ds0StatsSlotIndex,
       "ds0StatsLineNumber": ds0StatsLineNumber,
       "ds0StatsDs0Index": ds0StatsDs0Index,
       "iSDNStatsTable": iSDNStatsTable,
       "iSDNStatsEntry": iSDNStatsEntry,
       "iSDNStatsInCalls": iSDNStatsInCalls,
       "iSDNStatsInConnected": iSDNStatsInConnected,
       "iSDNStatsOutCalls": iSDNStatsOutCalls,
       "iSDNStatsOutConnected": iSDNStatsOutConnected,
       "iSDNStatsChargedUnits": iSDNStatsChargedUnits,
       "iSDNLayer2StatsTable": iSDNLayer2StatsTable,
       "iSDNLayer2StatsEntry": iSDNLayer2StatsEntry,
       "iSDNLayer2StatsLapdPeerSabme": iSDNLayer2StatsLapdPeerSabme,
       "iSDNLayer2StatsLapdRcvdFrmr": iSDNLayer2StatsLapdRcvdFrmr,
       "iSDNLayer2StatsLapdState": iSDNLayer2StatsLapdState,
       "iSDNHDLCFrameTable": iSDNHDLCFrameTable,
       "iSDNHDLCFrameEntry": iSDNHDLCFrameEntry,
       "iSDNHDLCFrameIndex": iSDNHDLCFrameIndex,
       "iSDNHDLCFrameNextIndex": iSDNHDLCFrameNextIndex,
       "iSDNHDLCFrameMaxIndex": iSDNHDLCFrameMaxIndex,
       "iSDNHDLCFrameTimestamp": iSDNHDLCFrameTimestamp,
       "iSDNHDLCFrameDirection": iSDNHDLCFrameDirection,
       "iSDNHDLCFrameLength": iSDNHDLCFrameLength,
       "iSDNHDLCFrameMessage": iSDNHDLCFrameMessage,
       "e1StatsTable": e1StatsTable,
       "e1StatsEntry": e1StatsEntry,
       "e1StatsAlarmStatus": e1StatsAlarmStatus,
       "e1StatsSlotIndex": e1StatsSlotIndex,
       "e1StatsLineNumber": e1StatsLineNumber,
       "e1CountsTable": e1CountsTable,
       "e1CountsEntry": e1CountsEntry,
       "e1CountsChannelCount": e1CountsChannelCount,
       "e1CountsChannelsInUse": e1CountsChannelsInUse,
       "e1CountsIncomingCallAttempts": e1CountsIncomingCallAttempts,
       "e1CountsIncomingConnects": e1CountsIncomingConnects,
       "e1CountsIncomingDisconnects": e1CountsIncomingDisconnects,
       "e1CountsOutgoingCallAttempts": e1CountsOutgoingCallAttempts,
       "e1CountsOutgoingConnects": e1CountsOutgoingConnects,
       "e1CountsOutgoingDisconnects": e1CountsOutgoingDisconnects,
       "e1CountsSessionAbortMessages": e1CountsSessionAbortMessages,
       "e1CountsSlotIndex": e1CountsSlotIndex,
       "e1CountsLineNumber": e1CountsLineNumber,
       "e1SummaryStatsTable": e1SummaryStatsTable,
       "e1SummaryStatsEntry": e1SummaryStatsEntry,
       "e1SummaryStatsRingingChannels": e1SummaryStatsRingingChannels,
       "e1SummaryStatsConnectedChannels": e1SummaryStatsConnectedChannels,
       "e1SummaryStatsClearingChannels": e1SummaryStatsClearingChannels,
       "e1SummaryStatsSlotIndex": e1SummaryStatsSlotIndex,
       "e1SummaryStatsLineNumber": e1SummaryStatsLineNumber,
       "e1SummaryStatsFunctionalChannels": e1SummaryStatsFunctionalChannels,
       "e1SummaryStatsIdleChannels": e1SummaryStatsIdleChannels,
       "clockStatusTable": clockStatusTable,
       "clockStatusEntry": clockStatusEntry,
       "clockStatusCurrentSource": clockStatusCurrentSource,
       "timerStatsTable": timerStatsTable,
       "timerStatsEntry": timerStatsEntry,
       "timerStatsSlotNumber": timerStatsSlotNumber,
       "timerStatsCardType": timerStatsCardType,
       "timerStatsCPUNumber": timerStatsCPUNumber,
       "timerStatsTimerEntrySize": timerStatsTimerEntrySize,
       "timerStatsTimerMemorySize": timerStatsTimerMemorySize,
       "timerStatsTotalCount": timerStatsTotalCount,
       "timerStatsFreeCount": timerStatsFreeCount,
       "timerStatsFreeMin": timerStatsFreeMin,
       "timerStatsActiveCount": timerStatsActiveCount,
       "timerStatsActiveMax": timerStatsActiveMax,
       "timerStatsAllocSuccesses": timerStatsAllocSuccesses,
       "timerStatsAllocFails": timerStatsAllocFails,
       "timerStatsFreeSuccesses": timerStatsFreeSuccesses,
       "timerStatsFreeFails": timerStatsFreeFails,
       "pbufStatsTable": pbufStatsTable,
       "pbufStatsEntry": pbufStatsEntry,
       "pbufStatsSlotNumber": pbufStatsSlotNumber,
       "pbufStatsCardType": pbufStatsCardType,
       "pbufStatsCPUNumber": pbufStatsCPUNumber,
       "pbufStatsDataSize0": pbufStatsDataSize0,
       "pbufStatsTotalCount0": pbufStatsTotalCount0,
       "pbufStatsAllocatedCount0": pbufStatsAllocatedCount0,
       "pbufStatsPermAllocatedCount0": pbufStatsPermAllocatedCount0,
       "pbufStatsAllocatedMax0": pbufStatsAllocatedMax0,
       "pbufStatsFreeCount0": pbufStatsFreeCount0,
       "pbufStatsFreeMin0": pbufStatsFreeMin0,
       "pbufStatsAllocSuccesses0": pbufStatsAllocSuccesses0,
       "pbufStatsAllocFails0": pbufStatsAllocFails0,
       "pbufStatsFreeSuccesses0": pbufStatsFreeSuccesses0,
       "pbufStatsFreeFails0": pbufStatsFreeFails0,
       "pbufStatsDataSize1": pbufStatsDataSize1,
       "pbufStatsTotalCount1": pbufStatsTotalCount1,
       "pbufStatsAllocatedCount1": pbufStatsAllocatedCount1,
       "pbufStatsPermAllocatedCount1": pbufStatsPermAllocatedCount1,
       "pbufStatsAllocatedMax1": pbufStatsAllocatedMax1,
       "pbufStatsFreeCount1": pbufStatsFreeCount1,
       "pbufStatsFreeMin1": pbufStatsFreeMin1,
       "pbufStatsAllocSuccesses1": pbufStatsAllocSuccesses1,
       "pbufStatsAllocFails1": pbufStatsAllocFails1,
       "pbufStatsFreeSuccesses1": pbufStatsFreeSuccesses1,
       "pbufStatsFreeFails1": pbufStatsFreeFails1,
       "pbufStatsDataSize2": pbufStatsDataSize2,
       "pbufStatsTotalCount2": pbufStatsTotalCount2,
       "pbufStatsAllocatedCount2": pbufStatsAllocatedCount2,
       "pbufStatsPermAllocatedCount2": pbufStatsPermAllocatedCount2,
       "pbufStatsAllocatedMax2": pbufStatsAllocatedMax2,
       "pbufStatsFreeCount2": pbufStatsFreeCount2,
       "pbufStatsFreeMin2": pbufStatsFreeMin2,
       "pbufStatsAllocSuccesses2": pbufStatsAllocSuccesses2,
       "pbufStatsAllocFails2": pbufStatsAllocFails2,
       "pbufStatsFreeSuccesses2": pbufStatsFreeSuccesses2,
       "pbufStatsFreeFails2": pbufStatsFreeFails2,
       "pbufStatsDataSize3": pbufStatsDataSize3,
       "pbufStatsTotalCount3": pbufStatsTotalCount3,
       "pbufStatsAllocatedCount3": pbufStatsAllocatedCount3,
       "pbufStatsPermAllocatedCount3": pbufStatsPermAllocatedCount3,
       "pbufStatsAllocatedMax3": pbufStatsAllocatedMax3,
       "pbufStatsFreeCount3": pbufStatsFreeCount3,
       "pbufStatsFreeMin3": pbufStatsFreeMin3,
       "pbufStatsAllocSuccesses3": pbufStatsAllocSuccesses3,
       "pbufStatsAllocFails3": pbufStatsAllocFails3,
       "pbufStatsFreeSuccesses3": pbufStatsFreeSuccesses3,
       "pbufStatsFreeFails3": pbufStatsFreeFails3,
       "pbufStatsDataSize4": pbufStatsDataSize4,
       "pbufStatsTotalCount4": pbufStatsTotalCount4,
       "pbufStatsAllocatedCount4": pbufStatsAllocatedCount4,
       "pbufStatsPermAllocatedCount4": pbufStatsPermAllocatedCount4,
       "pbufStatsAllocatedMax4": pbufStatsAllocatedMax4,
       "pbufStatsFreeCount4": pbufStatsFreeCount4,
       "pbufStatsFreeMin4": pbufStatsFreeMin4,
       "pbufStatsAllocSuccesses4": pbufStatsAllocSuccesses4,
       "pbufStatsAllocFails4": pbufStatsAllocFails4,
       "pbufStatsFreeSuccesses4": pbufStatsFreeSuccesses4,
       "pbufStatsFreeFails4": pbufStatsFreeFails4,
       "pbufStatsDataSize5": pbufStatsDataSize5,
       "pbufStatsTotalCount5": pbufStatsTotalCount5,
       "pbufStatsAllocatedCount5": pbufStatsAllocatedCount5,
       "pbufStatsPermAllocatedCount5": pbufStatsPermAllocatedCount5,
       "pbufStatsAllocatedMax5": pbufStatsAllocatedMax5,
       "pbufStatsFreeCount5": pbufStatsFreeCount5,
       "pbufStatsFreeMin5": pbufStatsFreeMin5,
       "pbufStatsAllocSuccesses5": pbufStatsAllocSuccesses5,
       "pbufStatsAllocFails5": pbufStatsAllocFails5,
       "pbufStatsFreeSuccesses5": pbufStatsFreeSuccesses5,
       "pbufStatsFreeFails5": pbufStatsFreeFails5,
       "memoryStatsTableTable": memoryStatsTableTable,
       "memoryStatsTableEntry": memoryStatsTableEntry,
       "memoryStatsTableSlotNumber": memoryStatsTableSlotNumber,
       "memoryStatsTableCardType": memoryStatsTableCardType,
       "memoryStatsTableCPUNumber": memoryStatsTableCPUNumber,
       "memoryStatsTableTotalSize": memoryStatsTableTotalSize,
       "memoryStatsTableManagedSize": memoryStatsTableManagedSize,
       "memoryStatsTableFreeSize": memoryStatsTableFreeSize,
       "memoryStatsTableFreeBlockCount": memoryStatsTableFreeBlockCount,
       "memoryStatsTableFreeLargestBlock": memoryStatsTableFreeLargestBlock,
       "memoryStatsTableFreeSmallestBlock": memoryStatsTableFreeSmallestBlock,
       "memoryStatsTableUsedSize": memoryStatsTableUsedSize,
       "memoryStatsTableUsedBlockCount": memoryStatsTableUsedBlockCount,
       "memoryStatsTableUsedLargestBlock": memoryStatsTableUsedLargestBlock,
       "memoryStatsTableUsedSmallestBlock": memoryStatsTableUsedSmallestBlock,
       "memoryStatsTableAllocSuccesses": memoryStatsTableAllocSuccesses,
       "memoryStatsTableAllocFails": memoryStatsTableAllocFails,
       "memoryStatsTableFreeSuccesses": memoryStatsTableFreeSuccesses,
       "memoryStatsTableFreeFails": memoryStatsTableFreeFails,
       "taskStatsTableTable": taskStatsTableTable,
       "taskStatsTableEntry": taskStatsTableEntry,
       "taskStatsTableSlotNumber": taskStatsTableSlotNumber,
       "taskStatsTableTaskIndex": taskStatsTableTaskIndex,
       "taskStatsTableTaskID": taskStatsTableTaskID,
       "taskStatsTableTaskName": taskStatsTableTaskName,
       "taskStatsTableTCBSize": taskStatsTableTCBSize,
       "taskStatsTableTCB": taskStatsTableTCB,
       "taskStatsTableWaitObjectName": taskStatsTableWaitObjectName,
       "taskStatsTableTicksPerSecond": taskStatsTableTicksPerSecond,
       "taskStatsTableTicksElapsed": taskStatsTableTicksElapsed,
       "taskStatsTableStackAddress1": taskStatsTableStackAddress1,
       "taskStatsTableStackAddress2": taskStatsTableStackAddress2,
       "taskStatsTableStackAddress3": taskStatsTableStackAddress3,
       "taskStatsTableStackAddress4": taskStatsTableStackAddress4,
       "taskStatsTableStackAddress5": taskStatsTableStackAddress5,
       "taskStatsTableStackAddress6": taskStatsTableStackAddress6,
       "taskStatsTableStackAddress7": taskStatsTableStackAddress7,
       "taskStatsTableStackAddress8": taskStatsTableStackAddress8,
       "taskStatsTableStackAddress9": taskStatsTableStackAddress9,
       "taskStatsTableStackAddress10": taskStatsTableStackAddress10,
       "taskStatsTableRunTime": taskStatsTableRunTime,
       "taskStatsTableContextSwitches": taskStatsTableContextSwitches,
       "taskStatsTableGlobalPool": taskStatsTableGlobalPool,
       "taskStatsTableIntervalTime": taskStatsTableIntervalTime,
       "taskStatsTableTotalTime": taskStatsTableTotalTime,
       "taskStatsTableIntervalSize": taskStatsTableIntervalSize,
       "taskStatsTableKernelPool": taskStatsTableKernelPool,
       "taskStatsTableTaskPool": taskStatsTableTaskPool,
       "taskStatsTableIsrTimes": taskStatsTableIsrTimes,
       "taskStatsTableIdle5Seconds": taskStatsTableIdle5Seconds,
       "taskStatsTableIdleMinute": taskStatsTableIdleMinute,
       "taskStatsTableIdle5Minute": taskStatsTableIdle5Minute,
       "taskStatsTableIdleHour": taskStatsTableIdleHour,
       "taskStatsTableIdleDay": taskStatsTableIdleDay,
       "ipstatRouteEntryTable": ipstatRouteEntryTable,
       "ipstatRouteEntryEntry": ipstatRouteEntryEntry,
       "ipstatRouteEntryPrevXxrt": ipstatRouteEntryPrevXxrt,
       "ipstatRouteEntryNextIprt": ipstatRouteEntryNextIprt,
       "ipstatRouteEntryPrevIndex": ipstatRouteEntryPrevIndex,
       "ipstatRouteEntryGenNumber": ipstatRouteEntryGenNumber,
       "ipstatRouteEntryNextIprtIndex": ipstatRouteEntryNextIprtIndex,
       "ipstatRouteEntryIpAddress": ipstatRouteEntryIpAddress,
       "ipstatRouteEntryIpMask": ipstatRouteEntryIpMask,
       "ipstatRouteEntryCircuitId": ipstatRouteEntryCircuitId,
       "ipstatRouteEntryTYPE": ipstatRouteEntryTYPE,
       "ipstatRouteEntryOwner": ipstatRouteEntryOwner,
       "ipstatRouteEntryPathAndCost": ipstatRouteEntryPathAndCost,
       "ipstatRouteEntryTrig": ipstatRouteEntryTrig,
       "ipstatRouteEntryTag": ipstatRouteEntryTag,
       "ipstatRouteEntryPrivate": ipstatRouteEntryPrivate,
       "ipstatRouteEntryPathType": ipstatRouteEntryPathType,
       "ipstatRouteEntryCost": ipstatRouteEntryCost,
       "ipstatIgmpEntryTable": ipstatIgmpEntryTable,
       "ipstatIgmpEntryEntry": ipstatIgmpEntryEntry,
       "ipstatIgmpEntryIPAddress": ipstatIgmpEntryIPAddress,
       "ipstatIgmpEntryIPAddrfrom": ipstatIgmpEntryIPAddrfrom,
       "ipstatIgmpEntryCliId": ipstatIgmpEntryCliId,
       "ipstatIgmpEntryTimeout": ipstatIgmpEntryTimeout,
       "ipstatIgmpEntryCount": ipstatIgmpEntryCount,
       "ipstatIgmpEntryState": ipstatIgmpEntryState}
)
