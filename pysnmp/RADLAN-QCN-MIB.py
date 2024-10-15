# SNMP MIB module (RADLAN-QCN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-QCN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:43:04 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(Percents,
 rnd) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "Percents",
    "rnd")

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
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlQcnMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 202)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RlQcnFeatureStatus_Type(TruthValue):
    """Custom type rlQcnFeatureStatus based on TruthValue"""


_RlQcnFeatureStatus_Object = MibScalar
rlQcnFeatureStatus = _RlQcnFeatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 202, 1),
    _RlQcnFeatureStatus_Type()
)
rlQcnFeatureStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQcnFeatureStatus.setStatus("current")
_RlQcnPriorityStateTable_Object = MibTable
rlQcnPriorityStateTable = _RlQcnPriorityStateTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 202, 2)
)
if mibBuilder.loadTexts:
    rlQcnPriorityStateTable.setStatus("current")
_RlQcnPriorityStateEntry_Object = MibTableRow
rlQcnPriorityStateEntry = _RlQcnPriorityStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 202, 2, 1)
)
rlQcnPriorityStateEntry.setIndexNames(
    (0, "RADLAN-QCN-MIB", "rlQcnPriorityStatePriority"),
)
if mibBuilder.loadTexts:
    rlQcnPriorityStateEntry.setStatus("current")


class _RlQcnPriorityStatePriority_Type(Integer32):
    """Custom type rlQcnPriorityStatePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlQcnPriorityStatePriority_Type.__name__ = "Integer32"
_RlQcnPriorityStatePriority_Object = MibTableColumn
rlQcnPriorityStatePriority = _RlQcnPriorityStatePriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 202, 2, 1, 1),
    _RlQcnPriorityStatePriority_Type()
)
rlQcnPriorityStatePriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQcnPriorityStatePriority.setStatus("current")


class _RlQcnPriorityAdminStateEnable_Type(TruthValue):
    """Custom type rlQcnPriorityAdminStateEnable based on TruthValue"""


_RlQcnPriorityAdminStateEnable_Object = MibTableColumn
rlQcnPriorityAdminStateEnable = _RlQcnPriorityAdminStateEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 202, 2, 1, 2),
    _RlQcnPriorityAdminStateEnable_Type()
)
rlQcnPriorityAdminStateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQcnPriorityAdminStateEnable.setStatus("current")


class _RlQcnPriorityOperStateEnable_Type(TruthValue):
    """Custom type rlQcnPriorityOperStateEnable based on TruthValue"""


_RlQcnPriorityOperStateEnable_Object = MibTableColumn
rlQcnPriorityOperStateEnable = _RlQcnPriorityOperStateEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 202, 2, 1, 3),
    _RlQcnPriorityOperStateEnable_Type()
)
rlQcnPriorityOperStateEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQcnPriorityOperStateEnable.setStatus("current")


class _RlQcnPriorityAdminStateReason_Type(Integer32):
    """Custom type rlQcnPriorityAdminStateReason based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("queue0", 2),
          ("sharedQueue", 3))
    )


_RlQcnPriorityAdminStateReason_Type.__name__ = "Integer32"
_RlQcnPriorityAdminStateReason_Object = MibTableColumn
rlQcnPriorityAdminStateReason = _RlQcnPriorityAdminStateReason_Object(
    (1, 3, 6, 1, 4, 1, 89, 202, 2, 1, 4),
    _RlQcnPriorityAdminStateReason_Type()
)
rlQcnPriorityAdminStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQcnPriorityAdminStateReason.setStatus("current")
_RlQcnPriorityStateStatus_Type = RowStatus
_RlQcnPriorityStateStatus_Object = MibTableColumn
rlQcnPriorityStateStatus = _RlQcnPriorityStateStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 202, 2, 1, 5),
    _RlQcnPriorityStateStatus_Type()
)
rlQcnPriorityStateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQcnPriorityStateStatus.setStatus("current")
_RlQcnIfStateTable_Object = MibTable
rlQcnIfStateTable = _RlQcnIfStateTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 202, 3)
)
if mibBuilder.loadTexts:
    rlQcnIfStateTable.setStatus("current")
_RlQcnIfStateEntry_Object = MibTableRow
rlQcnIfStateEntry = _RlQcnIfStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 202, 3, 1)
)
rlQcnIfStateEntry.setIndexNames(
    (0, "RADLAN-QCN-MIB", "rlQcnIfStateIfIndex"),
)
if mibBuilder.loadTexts:
    rlQcnIfStateEntry.setStatus("current")
_RlQcnIfStateIfIndex_Type = Integer32
_RlQcnIfStateIfIndex_Object = MibTableColumn
rlQcnIfStateIfIndex = _RlQcnIfStateIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 202, 3, 1, 1),
    _RlQcnIfStateIfIndex_Type()
)
rlQcnIfStateIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQcnIfStateIfIndex.setStatus("current")


class _RlQcnIfStateCpCreationEn_Type(TruthValue):
    """Custom type rlQcnIfStateCpCreationEn based on TruthValue"""


_RlQcnIfStateCpCreationEn_Object = MibTableColumn
rlQcnIfStateCpCreationEn = _RlQcnIfStateCpCreationEn_Object(
    (1, 3, 6, 1, 4, 1, 89, 202, 3, 1, 2),
    _RlQcnIfStateCpCreationEn_Type()
)
rlQcnIfStateCpCreationEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQcnIfStateCpCreationEn.setStatus("current")
_RlQcnIfStateStatus_Type = RowStatus
_RlQcnIfStateStatus_Object = MibTableColumn
rlQcnIfStateStatus = _RlQcnIfStateStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 202, 3, 1, 3),
    _RlQcnIfStateStatus_Type()
)
rlQcnIfStateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQcnIfStateStatus.setStatus("current")


class _RlQcnCmnPriority_Type(Integer32):
    """Custom type rlQcnCmnPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlQcnCmnPriority_Type.__name__ = "Integer32"
_RlQcnCmnPriority_Object = MibScalar
rlQcnCmnPriority = _RlQcnCmnPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 202, 4),
    _RlQcnCmnPriority_Type()
)
rlQcnCmnPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQcnCmnPriority.setStatus("current")


class _RlQcnCpPfcSetPoint_Type(Integer32):
    """Custom type rlQcnCpPfcSetPoint based on Integer32"""
    defaultValue = 26112


_RlQcnCpPfcSetPoint_Object = MibScalar
rlQcnCpPfcSetPoint = _RlQcnCpPfcSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 89, 202, 5),
    _RlQcnCpPfcSetPoint_Type()
)
rlQcnCpPfcSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQcnCpPfcSetPoint.setStatus("obsolete")


class _RlQcnCpNonPfcSetPoint_Type(Integer32):
    """Custom type rlQcnCpNonPfcSetPoint based on Integer32"""
    defaultValue = 26112


_RlQcnCpNonPfcSetPoint_Object = MibScalar
rlQcnCpNonPfcSetPoint = _RlQcnCpNonPfcSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 89, 202, 6),
    _RlQcnCpNonPfcSetPoint_Type()
)
rlQcnCpNonPfcSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQcnCpNonPfcSetPoint.setStatus("obsolete")


class _RlQcnCpFeedbackWeight_Type(Integer32):
    """Custom type rlQcnCpFeedbackWeight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 10),
    )


_RlQcnCpFeedbackWeight_Type.__name__ = "Integer32"
_RlQcnCpFeedbackWeight_Object = MibScalar
rlQcnCpFeedbackWeight = _RlQcnCpFeedbackWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 202, 7),
    _RlQcnCpFeedbackWeight_Type()
)
rlQcnCpFeedbackWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQcnCpFeedbackWeight.setStatus("current")


class _RlQcnCpMinSampleBase_Type(Integer32):
    """Custom type rlQcnCpMinSampleBase based on Integer32"""
    defaultValue = 150000


_RlQcnCpMinSampleBase_Object = MibScalar
rlQcnCpMinSampleBase = _RlQcnCpMinSampleBase_Object(
    (1, 3, 6, 1, 4, 1, 89, 202, 8),
    _RlQcnCpMinSampleBase_Type()
)
rlQcnCpMinSampleBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQcnCpMinSampleBase.setStatus("current")


class _RlQcnCpSetPoint_Type(Integer32):
    """Custom type rlQcnCpSetPoint based on Integer32"""
    defaultValue = 26112


_RlQcnCpSetPoint_Object = MibScalar
rlQcnCpSetPoint = _RlQcnCpSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 89, 202, 9),
    _RlQcnCpSetPoint_Type()
)
rlQcnCpSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQcnCpSetPoint.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-QCN-MIB",
    **{"rlQcnMib": rlQcnMib,
       "rlQcnFeatureStatus": rlQcnFeatureStatus,
       "rlQcnPriorityStateTable": rlQcnPriorityStateTable,
       "rlQcnPriorityStateEntry": rlQcnPriorityStateEntry,
       "rlQcnPriorityStatePriority": rlQcnPriorityStatePriority,
       "rlQcnPriorityAdminStateEnable": rlQcnPriorityAdminStateEnable,
       "rlQcnPriorityOperStateEnable": rlQcnPriorityOperStateEnable,
       "rlQcnPriorityAdminStateReason": rlQcnPriorityAdminStateReason,
       "rlQcnPriorityStateStatus": rlQcnPriorityStateStatus,
       "rlQcnIfStateTable": rlQcnIfStateTable,
       "rlQcnIfStateEntry": rlQcnIfStateEntry,
       "rlQcnIfStateIfIndex": rlQcnIfStateIfIndex,
       "rlQcnIfStateCpCreationEn": rlQcnIfStateCpCreationEn,
       "rlQcnIfStateStatus": rlQcnIfStateStatus,
       "rlQcnCmnPriority": rlQcnCmnPriority,
       "rlQcnCpPfcSetPoint": rlQcnCpPfcSetPoint,
       "rlQcnCpNonPfcSetPoint": rlQcnCpNonPfcSetPoint,
       "rlQcnCpFeedbackWeight": rlQcnCpFeedbackWeight,
       "rlQcnCpMinSampleBase": rlQcnCpMinSampleBase,
       "rlQcnCpSetPoint": rlQcnCpSetPoint}
)
