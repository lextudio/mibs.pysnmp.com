# SNMP MIB module (CISCO-PNNI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PNNI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:49 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(pnniIfEntry,
 pnniNodeEntry,
 pnniRouteAddrEntry) = mibBuilder.importSymbols(
    "PNNI-MIB",
    "pnniIfEntry",
    "pnniNodeEntry",
    "pnniRouteAddrEntry")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoPnniMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 65)
)
ciscoPnniMIB.setRevisions(
        ("1996-10-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class E164Address(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoPnniMIBObjects_ObjectIdentity = ObjectIdentity
ciscoPnniMIBObjects = _CiscoPnniMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1)
)
_CiscoPnniBase_ObjectIdentity = ObjectIdentity
ciscoPnniBase = _CiscoPnniBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 1)
)


class _CiscoPnniBackgroundRoutes_Type(TruthValue):
    """Custom type ciscoPnniBackgroundRoutes based on TruthValue"""


_CiscoPnniBackgroundRoutes_Object = MibScalar
ciscoPnniBackgroundRoutes = _CiscoPnniBackgroundRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 1, 1),
    _CiscoPnniBackgroundRoutes_Type()
)
ciscoPnniBackgroundRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoPnniBackgroundRoutes.setStatus("current")


class _CiscoPnniBackgroundPollInterval_Type(Integer32):
    """Custom type ciscoPnniBackgroundPollInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CiscoPnniBackgroundPollInterval_Type.__name__ = "Integer32"
_CiscoPnniBackgroundPollInterval_Object = MibScalar
ciscoPnniBackgroundPollInterval = _CiscoPnniBackgroundPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 1, 2),
    _CiscoPnniBackgroundPollInterval_Type()
)
ciscoPnniBackgroundPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoPnniBackgroundPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    ciscoPnniBackgroundPollInterval.setUnits("seconds")


class _CiscoPnniBackgroundInsignificantThreshold_Type(Integer32):
    """Custom type ciscoPnniBackgroundInsignificantThreshold based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CiscoPnniBackgroundInsignificantThreshold_Type.__name__ = "Integer32"
_CiscoPnniBackgroundInsignificantThreshold_Object = MibScalar
ciscoPnniBackgroundInsignificantThreshold = _CiscoPnniBackgroundInsignificantThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 1, 3),
    _CiscoPnniBackgroundInsignificantThreshold_Type()
)
ciscoPnniBackgroundInsignificantThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoPnniBackgroundInsignificantThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ciscoPnniBackgroundInsignificantThreshold.setUnits("changes")


class _CiscoPnniResourceMgmtPollInterval_Type(Integer32):
    """Custom type ciscoPnniResourceMgmtPollInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CiscoPnniResourceMgmtPollInterval_Type.__name__ = "Integer32"
_CiscoPnniResourceMgmtPollInterval_Object = MibScalar
ciscoPnniResourceMgmtPollInterval = _CiscoPnniResourceMgmtPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 1, 4),
    _CiscoPnniResourceMgmtPollInterval_Type()
)
ciscoPnniResourceMgmtPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoPnniResourceMgmtPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    ciscoPnniResourceMgmtPollInterval.setUnits("seconds")


class _CiscoPnniAdminWeightMode_Type(Integer32):
    """Custom type ciscoPnniAdminWeightMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linespeed", 2),
          ("uniform", 1))
    )


_CiscoPnniAdminWeightMode_Type.__name__ = "Integer32"
_CiscoPnniAdminWeightMode_Object = MibScalar
ciscoPnniAdminWeightMode = _CiscoPnniAdminWeightMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 1, 5),
    _CiscoPnniAdminWeightMode_Type()
)
ciscoPnniAdminWeightMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoPnniAdminWeightMode.setStatus("current")


class _CiscoPnniMaxAdminWeightPercentage_Type(Integer32):
    """Custom type ciscoPnniMaxAdminWeightPercentage based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 2000),
    )


_CiscoPnniMaxAdminWeightPercentage_Type.__name__ = "Integer32"
_CiscoPnniMaxAdminWeightPercentage_Object = MibScalar
ciscoPnniMaxAdminWeightPercentage = _CiscoPnniMaxAdminWeightPercentage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 1, 6),
    _CiscoPnniMaxAdminWeightPercentage_Type()
)
ciscoPnniMaxAdminWeightPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoPnniMaxAdminWeightPercentage.setStatus("current")


class _CiscoPnniRouteOptimizationThreshold_Type(Integer32):
    """Custom type ciscoPnniRouteOptimizationThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 100),
    )


_CiscoPnniRouteOptimizationThreshold_Type.__name__ = "Integer32"
_CiscoPnniRouteOptimizationThreshold_Object = MibScalar
ciscoPnniRouteOptimizationThreshold = _CiscoPnniRouteOptimizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 1, 7),
    _CiscoPnniRouteOptimizationThreshold_Type()
)
ciscoPnniRouteOptimizationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoPnniRouteOptimizationThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ciscoPnniRouteOptimizationThreshold.setUnits("percent")
_CiscoPnniNode_ObjectIdentity = ObjectIdentity
ciscoPnniNode = _CiscoPnniNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 2)
)
_CiscoPnniNodeTable_Object = MibTable
ciscoPnniNodeTable = _CiscoPnniNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoPnniNodeTable.setStatus("current")
_CiscoPnniNodeEntry_Object = MibTableRow
ciscoPnniNodeEntry = _CiscoPnniNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoPnniNodeEntry.setStatus("current")


class _CiscoPnniNodeAutoSummary_Type(TruthValue):
    """Custom type ciscoPnniNodeAutoSummary based on TruthValue"""


_CiscoPnniNodeAutoSummary_Object = MibTableColumn
ciscoPnniNodeAutoSummary = _CiscoPnniNodeAutoSummary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 2, 1, 1, 1),
    _CiscoPnniNodeAutoSummary_Type()
)
ciscoPnniNodeAutoSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoPnniNodeAutoSummary.setStatus("current")


class _CiscoPnniNodeRedistributeStatic_Type(TruthValue):
    """Custom type ciscoPnniNodeRedistributeStatic based on TruthValue"""


_CiscoPnniNodeRedistributeStatic_Object = MibTableColumn
ciscoPnniNodeRedistributeStatic = _CiscoPnniNodeRedistributeStatic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 2, 1, 1, 2),
    _CiscoPnniNodeRedistributeStatic_Type()
)
ciscoPnniNodeRedistributeStatic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoPnniNodeRedistributeStatic.setStatus("current")


class _CiscoPnniNodePtseRequest_Type(Integer32):
    """Custom type ciscoPnniNodePtseRequest based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CiscoPnniNodePtseRequest_Type.__name__ = "Integer32"
_CiscoPnniNodePtseRequest_Object = MibTableColumn
ciscoPnniNodePtseRequest = _CiscoPnniNodePtseRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 2, 1, 1, 3),
    _CiscoPnniNodePtseRequest_Type()
)
ciscoPnniNodePtseRequest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoPnniNodePtseRequest.setStatus("current")
_CiscoPnniNodeName_Type = DisplayString
_CiscoPnniNodeName_Object = MibTableColumn
ciscoPnniNodeName = _CiscoPnniNodeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 2, 1, 1, 4),
    _CiscoPnniNodeName_Type()
)
ciscoPnniNodeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoPnniNodeName.setStatus("current")


class _CiscoPnniNodeScopeMappingMode_Type(Integer32):
    """Custom type ciscoPnniNodeScopeMappingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_CiscoPnniNodeScopeMappingMode_Type.__name__ = "Integer32"
_CiscoPnniNodeScopeMappingMode_Object = MibTableColumn
ciscoPnniNodeScopeMappingMode = _CiscoPnniNodeScopeMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 2, 1, 1, 5),
    _CiscoPnniNodeScopeMappingMode_Type()
)
ciscoPnniNodeScopeMappingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoPnniNodeScopeMappingMode.setStatus("current")
_CiscoPnniInterface_ObjectIdentity = ObjectIdentity
ciscoPnniInterface = _CiscoPnniInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 3)
)
_CiscoPnniIfTable_Object = MibTable
ciscoPnniIfTable = _CiscoPnniIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ciscoPnniIfTable.setStatus("current")
_CiscoPnniIfEntry_Object = MibTableRow
ciscoPnniIfEntry = _CiscoPnniIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoPnniIfEntry.setStatus("current")


class _CiscoPnniIfLinkSelection_Type(Integer32):
    """Custom type ciscoPnniIfLinkSelection based on Integer32"""
    defaultValue = 2

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
        *(("adminWeightMinimize", 1),
          ("blockingMinimize", 2),
          ("loadBalance", 4),
          ("transmitSpeedMaximize", 3))
    )


_CiscoPnniIfLinkSelection_Type.__name__ = "Integer32"
_CiscoPnniIfLinkSelection_Object = MibTableColumn
ciscoPnniIfLinkSelection = _CiscoPnniIfLinkSelection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 3, 1, 1, 1),
    _CiscoPnniIfLinkSelection_Type()
)
ciscoPnniIfLinkSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoPnniIfLinkSelection.setStatus("current")


class _CiscoPnniIfRouteOptimization_Type(Integer32):
    """Custom type ciscoPnniIfRouteOptimization based on Integer32"""
    defaultValue = 1

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
        *(("disable", 1),
          ("soft", 2),
          ("switched", 3),
          ("switchedAndSoft", 4))
    )


_CiscoPnniIfRouteOptimization_Type.__name__ = "Integer32"
_CiscoPnniIfRouteOptimization_Object = MibTableColumn
ciscoPnniIfRouteOptimization = _CiscoPnniIfRouteOptimization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 3, 1, 1, 2),
    _CiscoPnniIfRouteOptimization_Type()
)
ciscoPnniIfRouteOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoPnniIfRouteOptimization.setStatus("current")


class _CiscoPnniIfRouteOptimInterval_Type(Integer32):
    """Custom type ciscoPnniIfRouteOptimInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_CiscoPnniIfRouteOptimInterval_Type.__name__ = "Integer32"
_CiscoPnniIfRouteOptimInterval_Object = MibTableColumn
ciscoPnniIfRouteOptimInterval = _CiscoPnniIfRouteOptimInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 3, 1, 1, 3),
    _CiscoPnniIfRouteOptimInterval_Type()
)
ciscoPnniIfRouteOptimInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoPnniIfRouteOptimInterval.setStatus("current")
if mibBuilder.loadTexts:
    ciscoPnniIfRouteOptimInterval.setUnits("minutes")


class _CiscoPnniIfRouteOptimStartHour_Type(Integer32):
    """Custom type ciscoPnniIfRouteOptimStartHour based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_CiscoPnniIfRouteOptimStartHour_Type.__name__ = "Integer32"
_CiscoPnniIfRouteOptimStartHour_Object = MibTableColumn
ciscoPnniIfRouteOptimStartHour = _CiscoPnniIfRouteOptimStartHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 3, 1, 1, 4),
    _CiscoPnniIfRouteOptimStartHour_Type()
)
ciscoPnniIfRouteOptimStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoPnniIfRouteOptimStartHour.setStatus("current")
if mibBuilder.loadTexts:
    ciscoPnniIfRouteOptimStartHour.setUnits("hour")


class _CiscoPnniIfRouteOptimStartMinute_Type(Integer32):
    """Custom type ciscoPnniIfRouteOptimStartMinute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_CiscoPnniIfRouteOptimStartMinute_Type.__name__ = "Integer32"
_CiscoPnniIfRouteOptimStartMinute_Object = MibTableColumn
ciscoPnniIfRouteOptimStartMinute = _CiscoPnniIfRouteOptimStartMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 3, 1, 1, 5),
    _CiscoPnniIfRouteOptimStartMinute_Type()
)
ciscoPnniIfRouteOptimStartMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoPnniIfRouteOptimStartMinute.setStatus("current")
if mibBuilder.loadTexts:
    ciscoPnniIfRouteOptimStartMinute.setUnits("minutes")


class _CiscoPnniIfRouteOptimEndHour_Type(Integer32):
    """Custom type ciscoPnniIfRouteOptimEndHour based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_CiscoPnniIfRouteOptimEndHour_Type.__name__ = "Integer32"
_CiscoPnniIfRouteOptimEndHour_Object = MibTableColumn
ciscoPnniIfRouteOptimEndHour = _CiscoPnniIfRouteOptimEndHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 3, 1, 1, 6),
    _CiscoPnniIfRouteOptimEndHour_Type()
)
ciscoPnniIfRouteOptimEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoPnniIfRouteOptimEndHour.setStatus("current")
if mibBuilder.loadTexts:
    ciscoPnniIfRouteOptimEndHour.setUnits("hour")


class _CiscoPnniIfRouteOptimEndMinute_Type(Integer32):
    """Custom type ciscoPnniIfRouteOptimEndMinute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_CiscoPnniIfRouteOptimEndMinute_Type.__name__ = "Integer32"
_CiscoPnniIfRouteOptimEndMinute_Object = MibTableColumn
ciscoPnniIfRouteOptimEndMinute = _CiscoPnniIfRouteOptimEndMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 3, 1, 1, 7),
    _CiscoPnniIfRouteOptimEndMinute_Type()
)
ciscoPnniIfRouteOptimEndMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoPnniIfRouteOptimEndMinute.setStatus("current")
if mibBuilder.loadTexts:
    ciscoPnniIfRouteOptimEndMinute.setUnits("minutes")
_CiscoPnniPrecedence_ObjectIdentity = ObjectIdentity
ciscoPnniPrecedence = _CiscoPnniPrecedence_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 4)
)
_CiscoPnniPrecedenceTable_Object = MibTable
ciscoPnniPrecedenceTable = _CiscoPnniPrecedenceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ciscoPnniPrecedenceTable.setStatus("current")
_CiscoPnniPrecedenceEntry_Object = MibTableRow
ciscoPnniPrecedenceEntry = _CiscoPnniPrecedenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 4, 1, 1)
)
ciscoPnniPrecedenceEntry.setIndexNames(
    (0, "CISCO-PNNI-MIB", "ciscoPnniPrecedenceAddressType"),
)
if mibBuilder.loadTexts:
    ciscoPnniPrecedenceEntry.setStatus("current")


class _CiscoPnniPrecedenceAddressType_Type(Integer32):
    """Custom type ciscoPnniPrecedenceAddressType based on Integer32"""
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
        *(("pnniRemoteExterior", 6),
          ("pnniRemoteExteriorWithMetrics", 7),
          ("pnniRemoteInternal", 4),
          ("pnniRemoteInternalWithMetrics", 5),
          ("staticLocalExterior", 2),
          ("staticLocalExteriorWithMetrics", 3),
          ("staticLocalInternalWithMetrics", 1))
    )


_CiscoPnniPrecedenceAddressType_Type.__name__ = "Integer32"
_CiscoPnniPrecedenceAddressType_Object = MibTableColumn
ciscoPnniPrecedenceAddressType = _CiscoPnniPrecedenceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 4, 1, 1, 1),
    _CiscoPnniPrecedenceAddressType_Type()
)
ciscoPnniPrecedenceAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoPnniPrecedenceAddressType.setStatus("current")


class _CiscoPnniPrecedenceValue_Type(Integer32):
    """Custom type ciscoPnniPrecedenceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4),
    )


_CiscoPnniPrecedenceValue_Type.__name__ = "Integer32"
_CiscoPnniPrecedenceValue_Object = MibTableColumn
ciscoPnniPrecedenceValue = _CiscoPnniPrecedenceValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 4, 1, 1, 2),
    _CiscoPnniPrecedenceValue_Type()
)
ciscoPnniPrecedenceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoPnniPrecedenceValue.setStatus("current")
_CiscoPnniRouteAddr_ObjectIdentity = ObjectIdentity
ciscoPnniRouteAddr = _CiscoPnniRouteAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 5)
)
_CiscoPnniRouteAddrTable_Object = MibTable
ciscoPnniRouteAddrTable = _CiscoPnniRouteAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ciscoPnniRouteAddrTable.setStatus("current")
_CiscoPnniRouteAddrEntry_Object = MibTableRow
ciscoPnniRouteAddrEntry = _CiscoPnniRouteAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoPnniRouteAddrEntry.setStatus("current")


class _CiscoPnniRouteAddrForwardingE164Address_Type(E164Address):
    """Custom type ciscoPnniRouteAddrForwardingE164Address based on E164Address"""
    defaultHexValue = ""


_CiscoPnniRouteAddrForwardingE164Address_Object = MibTableColumn
ciscoPnniRouteAddrForwardingE164Address = _CiscoPnniRouteAddrForwardingE164Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 1, 5, 1, 1, 1),
    _CiscoPnniRouteAddrForwardingE164Address_Type()
)
ciscoPnniRouteAddrForwardingE164Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoPnniRouteAddrForwardingE164Address.setStatus("current")
_CiscoPnniMIBConformance_ObjectIdentity = ObjectIdentity
ciscoPnniMIBConformance = _CiscoPnniMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 3)
)
_CiscoPnniMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoPnniMIBCompliances = _CiscoPnniMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 3, 1)
)
_CiscoPnniMIBGroups_ObjectIdentity = ObjectIdentity
ciscoPnniMIBGroups = _CiscoPnniMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 3, 2)
)
pnniNodeEntry.registerAugmentions(
    ("CISCO-PNNI-MIB",
     "ciscoPnniNodeEntry")
)
ciscoPnniNodeEntry.setIndexNames(*pnniNodeEntry.getIndexNames())
pnniIfEntry.registerAugmentions(
    ("CISCO-PNNI-MIB",
     "ciscoPnniIfEntry")
)
ciscoPnniIfEntry.setIndexNames(*pnniIfEntry.getIndexNames())
pnniRouteAddrEntry.registerAugmentions(
    ("CISCO-PNNI-MIB",
     "ciscoPnniRouteAddrEntry")
)
ciscoPnniRouteAddrEntry.setIndexNames(*pnniRouteAddrEntry.getIndexNames())

# Managed Objects groups

ciscoPnniBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 3, 2, 1)
)
ciscoPnniBasicGroup.setObjects(
      *(("CISCO-PNNI-MIB", "ciscoPnniBackgroundRoutes"),
        ("CISCO-PNNI-MIB", "ciscoPnniBackgroundPollInterval"),
        ("CISCO-PNNI-MIB", "ciscoPnniBackgroundInsignificantThreshold"),
        ("CISCO-PNNI-MIB", "ciscoPnniResourceMgmtPollInterval"),
        ("CISCO-PNNI-MIB", "ciscoPnniAdminWeightMode"),
        ("CISCO-PNNI-MIB", "ciscoPnniMaxAdminWeightPercentage"),
        ("CISCO-PNNI-MIB", "ciscoPnniNodeAutoSummary"),
        ("CISCO-PNNI-MIB", "ciscoPnniNodeRedistributeStatic"),
        ("CISCO-PNNI-MIB", "ciscoPnniNodePtseRequest"),
        ("CISCO-PNNI-MIB", "ciscoPnniNodeName"),
        ("CISCO-PNNI-MIB", "ciscoPnniNodeScopeMappingMode"),
        ("CISCO-PNNI-MIB", "ciscoPnniIfLinkSelection"),
        ("CISCO-PNNI-MIB", "ciscoPnniPrecedenceValue"),
        ("CISCO-PNNI-MIB", "ciscoPnniRouteAddrForwardingE164Address"))
)
if mibBuilder.loadTexts:
    ciscoPnniBasicGroup.setStatus("current")

ciscoPnniRouteOptimizationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 3, 2, 2)
)
ciscoPnniRouteOptimizationGroup.setObjects(
      *(("CISCO-PNNI-MIB", "ciscoPnniRouteOptimizationThreshold"),
        ("CISCO-PNNI-MIB", "ciscoPnniIfRouteOptimization"),
        ("CISCO-PNNI-MIB", "ciscoPnniIfRouteOptimInterval"),
        ("CISCO-PNNI-MIB", "ciscoPnniIfRouteOptimStartHour"),
        ("CISCO-PNNI-MIB", "ciscoPnniIfRouteOptimStartMinute"),
        ("CISCO-PNNI-MIB", "ciscoPnniIfRouteOptimEndHour"),
        ("CISCO-PNNI-MIB", "ciscoPnniIfRouteOptimEndMinute"))
)
if mibBuilder.loadTexts:
    ciscoPnniRouteOptimizationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoPnniMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 65, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoPnniMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PNNI-MIB",
    **{"E164Address": E164Address,
       "ciscoPnniMIB": ciscoPnniMIB,
       "ciscoPnniMIBObjects": ciscoPnniMIBObjects,
       "ciscoPnniBase": ciscoPnniBase,
       "ciscoPnniBackgroundRoutes": ciscoPnniBackgroundRoutes,
       "ciscoPnniBackgroundPollInterval": ciscoPnniBackgroundPollInterval,
       "ciscoPnniBackgroundInsignificantThreshold": ciscoPnniBackgroundInsignificantThreshold,
       "ciscoPnniResourceMgmtPollInterval": ciscoPnniResourceMgmtPollInterval,
       "ciscoPnniAdminWeightMode": ciscoPnniAdminWeightMode,
       "ciscoPnniMaxAdminWeightPercentage": ciscoPnniMaxAdminWeightPercentage,
       "ciscoPnniRouteOptimizationThreshold": ciscoPnniRouteOptimizationThreshold,
       "ciscoPnniNode": ciscoPnniNode,
       "ciscoPnniNodeTable": ciscoPnniNodeTable,
       "ciscoPnniNodeEntry": ciscoPnniNodeEntry,
       "ciscoPnniNodeAutoSummary": ciscoPnniNodeAutoSummary,
       "ciscoPnniNodeRedistributeStatic": ciscoPnniNodeRedistributeStatic,
       "ciscoPnniNodePtseRequest": ciscoPnniNodePtseRequest,
       "ciscoPnniNodeName": ciscoPnniNodeName,
       "ciscoPnniNodeScopeMappingMode": ciscoPnniNodeScopeMappingMode,
       "ciscoPnniInterface": ciscoPnniInterface,
       "ciscoPnniIfTable": ciscoPnniIfTable,
       "ciscoPnniIfEntry": ciscoPnniIfEntry,
       "ciscoPnniIfLinkSelection": ciscoPnniIfLinkSelection,
       "ciscoPnniIfRouteOptimization": ciscoPnniIfRouteOptimization,
       "ciscoPnniIfRouteOptimInterval": ciscoPnniIfRouteOptimInterval,
       "ciscoPnniIfRouteOptimStartHour": ciscoPnniIfRouteOptimStartHour,
       "ciscoPnniIfRouteOptimStartMinute": ciscoPnniIfRouteOptimStartMinute,
       "ciscoPnniIfRouteOptimEndHour": ciscoPnniIfRouteOptimEndHour,
       "ciscoPnniIfRouteOptimEndMinute": ciscoPnniIfRouteOptimEndMinute,
       "ciscoPnniPrecedence": ciscoPnniPrecedence,
       "ciscoPnniPrecedenceTable": ciscoPnniPrecedenceTable,
       "ciscoPnniPrecedenceEntry": ciscoPnniPrecedenceEntry,
       "ciscoPnniPrecedenceAddressType": ciscoPnniPrecedenceAddressType,
       "ciscoPnniPrecedenceValue": ciscoPnniPrecedenceValue,
       "ciscoPnniRouteAddr": ciscoPnniRouteAddr,
       "ciscoPnniRouteAddrTable": ciscoPnniRouteAddrTable,
       "ciscoPnniRouteAddrEntry": ciscoPnniRouteAddrEntry,
       "ciscoPnniRouteAddrForwardingE164Address": ciscoPnniRouteAddrForwardingE164Address,
       "ciscoPnniMIBConformance": ciscoPnniMIBConformance,
       "ciscoPnniMIBCompliances": ciscoPnniMIBCompliances,
       "ciscoPnniMIBCompliance": ciscoPnniMIBCompliance,
       "ciscoPnniMIBGroups": ciscoPnniMIBGroups,
       "ciscoPnniBasicGroup": ciscoPnniBasicGroup,
       "ciscoPnniRouteOptimizationGroup": ciscoPnniRouteOptimizationGroup}
)
