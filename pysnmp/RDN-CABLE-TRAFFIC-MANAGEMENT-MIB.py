# SNMP MIB module (RDN-CABLE-TRAFFIC-MANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RDN-CABLE-TRAFFIC-MANAGEMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:00 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(riverdelta,) = mibBuilder.importSymbols(
    "RDN-MIB",
    "riverdelta")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rdnCableTrafficManagementMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 10)
)
rdnCableTrafficManagementMib.setRevisions(
        ("2008-09-16 00:00",
         "2008-02-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RdnCtmScalar_ObjectIdentity = ObjectIdentity
rdnCtmScalar = _RdnCtmScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 10, 1)
)


class _RdnCtmEnforcedClear_Type(Integer32):
    """Custom type rdnCtmEnforcedClear based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noAction", 1))
    )


_RdnCtmEnforcedClear_Type.__name__ = "Integer32"
_RdnCtmEnforcedClear_Object = MibScalar
rdnCtmEnforcedClear = _RdnCtmEnforcedClear_Object(
    (1, 3, 6, 1, 4, 1, 4981, 10, 1, 1),
    _RdnCtmEnforcedClear_Type()
)
rdnCtmEnforcedClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCtmEnforcedClear.setStatus("current")
_RdnCtmEnforcedSince_Type = DateAndTime
_RdnCtmEnforcedSince_Object = MibScalar
rdnCtmEnforcedSince = _RdnCtmEnforcedSince_Object(
    (1, 3, 6, 1, 4, 1, 4981, 10, 1, 2),
    _RdnCtmEnforcedSince_Type()
)
rdnCtmEnforcedSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCtmEnforcedSince.setStatus("current")


class _RdnCtmClearHistory_Type(Integer32):
    """Custom type rdnCtmClearHistory based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noAction", 1))
    )


_RdnCtmClearHistory_Type.__name__ = "Integer32"
_RdnCtmClearHistory_Object = MibScalar
rdnCtmClearHistory = _RdnCtmClearHistory_Object(
    (1, 3, 6, 1, 4, 1, 4981, 10, 1, 3),
    _RdnCtmClearHistory_Type()
)
rdnCtmClearHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCtmClearHistory.setStatus("current")
_RdnCtmSummaryTable_Object = MibTable
rdnCtmSummaryTable = _RdnCtmSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 10, 2)
)
if mibBuilder.loadTexts:
    rdnCtmSummaryTable.setStatus("current")
_RdnCtmSummaryTableEntry_Object = MibTableRow
rdnCtmSummaryTableEntry = _RdnCtmSummaryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 10, 2, 1)
)
rdnCtmSummaryTableEntry.setIndexNames(
    (0, "RDN-CABLE-TRAFFIC-MANAGEMENT-MIB", "rdnCtmSummaryIfIndex"),
    (0, "RDN-CABLE-TRAFFIC-MANAGEMENT-MIB", "rdnCtmSummaryDirection"),
    (0, "RDN-CABLE-TRAFFIC-MANAGEMENT-MIB", "rdnCtmSummaryTrafficPolicy"),
)
if mibBuilder.loadTexts:
    rdnCtmSummaryTableEntry.setStatus("current")
_RdnCtmSummaryIfIndex_Type = InterfaceIndex
_RdnCtmSummaryIfIndex_Object = MibTableColumn
rdnCtmSummaryIfIndex = _RdnCtmSummaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 10, 2, 1, 1),
    _RdnCtmSummaryIfIndex_Type()
)
rdnCtmSummaryIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnCtmSummaryIfIndex.setStatus("current")


class _RdnCtmSummaryDirection_Type(Integer32):
    """Custom type rdnCtmSummaryDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 1),
          ("upstream", 2))
    )


_RdnCtmSummaryDirection_Type.__name__ = "Integer32"
_RdnCtmSummaryDirection_Object = MibTableColumn
rdnCtmSummaryDirection = _RdnCtmSummaryDirection_Object(
    (1, 3, 6, 1, 4, 1, 4981, 10, 2, 1, 2),
    _RdnCtmSummaryDirection_Type()
)
rdnCtmSummaryDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnCtmSummaryDirection.setStatus("current")
_RdnCtmSummaryTrafficPolicy_Type = DisplayString
_RdnCtmSummaryTrafficPolicy_Object = MibTableColumn
rdnCtmSummaryTrafficPolicy = _RdnCtmSummaryTrafficPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4981, 10, 2, 1, 3),
    _RdnCtmSummaryTrafficPolicy_Type()
)
rdnCtmSummaryTrafficPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnCtmSummaryTrafficPolicy.setStatus("current")
_RdnCtmSummaryMonitoredCount_Type = Integer32
_RdnCtmSummaryMonitoredCount_Object = MibTableColumn
rdnCtmSummaryMonitoredCount = _RdnCtmSummaryMonitoredCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 10, 2, 1, 4),
    _RdnCtmSummaryMonitoredCount_Type()
)
rdnCtmSummaryMonitoredCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCtmSummaryMonitoredCount.setStatus("current")
_RdnCtmSummaryTotalFlows_Type = Integer32
_RdnCtmSummaryTotalFlows_Object = MibTableColumn
rdnCtmSummaryTotalFlows = _RdnCtmSummaryTotalFlows_Object(
    (1, 3, 6, 1, 4, 1, 4981, 10, 2, 1, 5),
    _RdnCtmSummaryTotalFlows_Type()
)
rdnCtmSummaryTotalFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCtmSummaryTotalFlows.setStatus("current")
_RdnCtmSummaryEnforcedFlows_Type = Integer32
_RdnCtmSummaryEnforcedFlows_Object = MibTableColumn
rdnCtmSummaryEnforcedFlows = _RdnCtmSummaryEnforcedFlows_Object(
    (1, 3, 6, 1, 4, 1, 4981, 10, 2, 1, 6),
    _RdnCtmSummaryEnforcedFlows_Type()
)
rdnCtmSummaryEnforcedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCtmSummaryEnforcedFlows.setStatus("current")
_RdnCtmEnforcedTable_Object = MibTable
rdnCtmEnforcedTable = _RdnCtmEnforcedTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 10, 3)
)
if mibBuilder.loadTexts:
    rdnCtmEnforcedTable.setStatus("current")
_RdnCtmEnforcedTableEntry_Object = MibTableRow
rdnCtmEnforcedTableEntry = _RdnCtmEnforcedTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 10, 3, 1)
)
rdnCtmEnforcedTableEntry.setIndexNames(
    (0, "RDN-CABLE-TRAFFIC-MANAGEMENT-MIB", "rdnCtmEnforcedIfIndex"),
    (0, "RDN-CABLE-TRAFFIC-MANAGEMENT-MIB", "rdnCtmEnforcedDirection"),
    (0, "RDN-CABLE-TRAFFIC-MANAGEMENT-MIB", "rdnCtmEnforcedServiceFlowId"),
)
if mibBuilder.loadTexts:
    rdnCtmEnforcedTableEntry.setStatus("current")
_RdnCtmEnforcedIfIndex_Type = InterfaceIndex
_RdnCtmEnforcedIfIndex_Object = MibTableColumn
rdnCtmEnforcedIfIndex = _RdnCtmEnforcedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 10, 3, 1, 1),
    _RdnCtmEnforcedIfIndex_Type()
)
rdnCtmEnforcedIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnCtmEnforcedIfIndex.setStatus("current")


class _RdnCtmEnforcedDirection_Type(Integer32):
    """Custom type rdnCtmEnforcedDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 1),
          ("upstream", 2))
    )


_RdnCtmEnforcedDirection_Type.__name__ = "Integer32"
_RdnCtmEnforcedDirection_Object = MibTableColumn
rdnCtmEnforcedDirection = _RdnCtmEnforcedDirection_Object(
    (1, 3, 6, 1, 4, 1, 4981, 10, 3, 1, 2),
    _RdnCtmEnforcedDirection_Type()
)
rdnCtmEnforcedDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnCtmEnforcedDirection.setStatus("current")
_RdnCtmEnforcedServiceFlowId_Type = Integer32
_RdnCtmEnforcedServiceFlowId_Object = MibTableColumn
rdnCtmEnforcedServiceFlowId = _RdnCtmEnforcedServiceFlowId_Object(
    (1, 3, 6, 1, 4, 1, 4981, 10, 3, 1, 3),
    _RdnCtmEnforcedServiceFlowId_Type()
)
rdnCtmEnforcedServiceFlowId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnCtmEnforcedServiceFlowId.setStatus("current")
_RdnCtmEnforcedCmMacAddr_Type = MacAddress
_RdnCtmEnforcedCmMacAddr_Object = MibTableColumn
rdnCtmEnforcedCmMacAddr = _RdnCtmEnforcedCmMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4981, 10, 3, 1, 4),
    _RdnCtmEnforcedCmMacAddr_Type()
)
rdnCtmEnforcedCmMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCtmEnforcedCmMacAddr.setStatus("current")
_RdnCtmEnforcedTrafficPolicy_Type = DisplayString
_RdnCtmEnforcedTrafficPolicy_Object = MibTableColumn
rdnCtmEnforcedTrafficPolicy = _RdnCtmEnforcedTrafficPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4981, 10, 3, 1, 5),
    _RdnCtmEnforcedTrafficPolicy_Type()
)
rdnCtmEnforcedTrafficPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCtmEnforcedTrafficPolicy.setStatus("current")
_RdnCtmEnforcedMonitoredCount_Type = Counter32
_RdnCtmEnforcedMonitoredCount_Object = MibTableColumn
rdnCtmEnforcedMonitoredCount = _RdnCtmEnforcedMonitoredCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 10, 3, 1, 6),
    _RdnCtmEnforcedMonitoredCount_Type()
)
rdnCtmEnforcedMonitoredCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCtmEnforcedMonitoredCount.setStatus("current")
_RdnCtmEnforcedLast_Type = OctetString
_RdnCtmEnforcedLast_Object = MibTableColumn
rdnCtmEnforcedLast = _RdnCtmEnforcedLast_Object(
    (1, 3, 6, 1, 4, 1, 4981, 10, 3, 1, 7),
    _RdnCtmEnforcedLast_Type()
)
rdnCtmEnforcedLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCtmEnforcedLast.setStatus("current")
_RdnCtmEnforcedRemain_Type = OctetString
_RdnCtmEnforcedRemain_Object = MibTableColumn
rdnCtmEnforcedRemain = _RdnCtmEnforcedRemain_Object(
    (1, 3, 6, 1, 4, 1, 4981, 10, 3, 1, 8),
    _RdnCtmEnforcedRemain_Type()
)
rdnCtmEnforcedRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCtmEnforcedRemain.setStatus("current")
_RdnCtmEnforcedLimitRate_Type = Integer32
_RdnCtmEnforcedLimitRate_Object = MibTableColumn
rdnCtmEnforcedLimitRate = _RdnCtmEnforcedLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 4981, 10, 3, 1, 9),
    _RdnCtmEnforcedLimitRate_Type()
)
rdnCtmEnforcedLimitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCtmEnforcedLimitRate.setStatus("current")


class _RdnCtmEnforcedReason_Type(Integer32):
    """Custom type rdnCtmEnforcedReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 2),
          ("configured", 1),
          ("enforced", 3))
    )


_RdnCtmEnforcedReason_Type.__name__ = "Integer32"
_RdnCtmEnforcedReason_Object = MibTableColumn
rdnCtmEnforcedReason = _RdnCtmEnforcedReason_Object(
    (1, 3, 6, 1, 4, 1, 4981, 10, 3, 1, 10),
    _RdnCtmEnforcedReason_Type()
)
rdnCtmEnforcedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCtmEnforcedReason.setStatus("current")
_RdnCtmEnforcedMonitored_Type = TruthValue
_RdnCtmEnforcedMonitored_Object = MibTableColumn
rdnCtmEnforcedMonitored = _RdnCtmEnforcedMonitored_Object(
    (1, 3, 6, 1, 4, 1, 4981, 10, 3, 1, 11),
    _RdnCtmEnforcedMonitored_Type()
)
rdnCtmEnforcedMonitored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCtmEnforcedMonitored.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RDN-CABLE-TRAFFIC-MANAGEMENT-MIB",
    **{"rdnCableTrafficManagementMib": rdnCableTrafficManagementMib,
       "rdnCtmScalar": rdnCtmScalar,
       "rdnCtmEnforcedClear": rdnCtmEnforcedClear,
       "rdnCtmEnforcedSince": rdnCtmEnforcedSince,
       "rdnCtmClearHistory": rdnCtmClearHistory,
       "rdnCtmSummaryTable": rdnCtmSummaryTable,
       "rdnCtmSummaryTableEntry": rdnCtmSummaryTableEntry,
       "rdnCtmSummaryIfIndex": rdnCtmSummaryIfIndex,
       "rdnCtmSummaryDirection": rdnCtmSummaryDirection,
       "rdnCtmSummaryTrafficPolicy": rdnCtmSummaryTrafficPolicy,
       "rdnCtmSummaryMonitoredCount": rdnCtmSummaryMonitoredCount,
       "rdnCtmSummaryTotalFlows": rdnCtmSummaryTotalFlows,
       "rdnCtmSummaryEnforcedFlows": rdnCtmSummaryEnforcedFlows,
       "rdnCtmEnforcedTable": rdnCtmEnforcedTable,
       "rdnCtmEnforcedTableEntry": rdnCtmEnforcedTableEntry,
       "rdnCtmEnforcedIfIndex": rdnCtmEnforcedIfIndex,
       "rdnCtmEnforcedDirection": rdnCtmEnforcedDirection,
       "rdnCtmEnforcedServiceFlowId": rdnCtmEnforcedServiceFlowId,
       "rdnCtmEnforcedCmMacAddr": rdnCtmEnforcedCmMacAddr,
       "rdnCtmEnforcedTrafficPolicy": rdnCtmEnforcedTrafficPolicy,
       "rdnCtmEnforcedMonitoredCount": rdnCtmEnforcedMonitoredCount,
       "rdnCtmEnforcedLast": rdnCtmEnforcedLast,
       "rdnCtmEnforcedRemain": rdnCtmEnforcedRemain,
       "rdnCtmEnforcedLimitRate": rdnCtmEnforcedLimitRate,
       "rdnCtmEnforcedReason": rdnCtmEnforcedReason,
       "rdnCtmEnforcedMonitored": rdnCtmEnforcedMonitored}
)
