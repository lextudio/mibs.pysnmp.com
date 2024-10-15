# SNMP MIB module (NNCEXTCALLROUTINGSTATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNCEXTCALLROUTINGSTATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:17 2024
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

(NncExtIntvlStateType,) = mibBuilder.importSymbols(
    "NNC-INTERVAL-STATISTICS-TC-MIB",
    "NncExtIntvlStateType")

(nncExtensions,) = mibBuilder.importSymbols(
    "NNCGNI0001-SMI",
    "nncExtensions")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

nncExtRoutingStats = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 78)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NncRoutingStatsObjects_ObjectIdentity = ObjectIdentity
nncRoutingStatsObjects = _NncRoutingStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1)
)
_NncRoutingStatsCommon15MinCurrentTable_Object = MibTable
nncRoutingStatsCommon15MinCurrentTable = _NncRoutingStatsCommon15MinCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 1)
)
if mibBuilder.loadTexts:
    nncRoutingStatsCommon15MinCurrentTable.setStatus("current")
_NncRoutingStatsCommon15MinCurrentEntry_Object = MibTableRow
nncRoutingStatsCommon15MinCurrentEntry = _NncRoutingStatsCommon15MinCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 1, 1)
)
nncRoutingStatsCommon15MinCurrentEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsCommon15MinCurrentEntry.setStatus("current")


class _NncCallControlGroupNumber_Type(Integer32):
    """Custom type nncCallControlGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_NncCallControlGroupNumber_Type.__name__ = "Integer32"
_NncCallControlGroupNumber_Object = MibTableColumn
nncCallControlGroupNumber = _NncCallControlGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 1, 1, 1),
    _NncCallControlGroupNumber_Type()
)
nncCallControlGroupNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncCallControlGroupNumber.setStatus("current")
_NncCommon15MinCurrentState_Type = NncExtIntvlStateType
_NncCommon15MinCurrentState_Object = MibTableColumn
nncCommon15MinCurrentState = _NncCommon15MinCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 1, 1, 2),
    _NncCommon15MinCurrentState_Type()
)
nncCommon15MinCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinCurrentState.setStatus("current")
_NncCommon15MinCurrentAbsoluteIntervalNumber_Type = Counter32
_NncCommon15MinCurrentAbsoluteIntervalNumber_Object = MibTableColumn
nncCommon15MinCurrentAbsoluteIntervalNumber = _NncCommon15MinCurrentAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 1, 1, 3),
    _NncCommon15MinCurrentAbsoluteIntervalNumber_Type()
)
nncCommon15MinCurrentAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinCurrentAbsoluteIntervalNumber.setStatus("current")
_NncCommon15MinCurrentSuccessRoutedCallsOrigFromLocalSubs_Type = Counter32
_NncCommon15MinCurrentSuccessRoutedCallsOrigFromLocalSubs_Object = MibTableColumn
nncCommon15MinCurrentSuccessRoutedCallsOrigFromLocalSubs = _NncCommon15MinCurrentSuccessRoutedCallsOrigFromLocalSubs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 1, 1, 4),
    _NncCommon15MinCurrentSuccessRoutedCallsOrigFromLocalSubs_Type()
)
nncCommon15MinCurrentSuccessRoutedCallsOrigFromLocalSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinCurrentSuccessRoutedCallsOrigFromLocalSubs.setStatus("current")
_NncCommon15MinCurrentSuccessRoutedCallsTransitedViaThisNode_Type = Counter32
_NncCommon15MinCurrentSuccessRoutedCallsTransitedViaThisNode_Object = MibTableColumn
nncCommon15MinCurrentSuccessRoutedCallsTransitedViaThisNode = _NncCommon15MinCurrentSuccessRoutedCallsTransitedViaThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 1, 1, 5),
    _NncCommon15MinCurrentSuccessRoutedCallsTransitedViaThisNode_Type()
)
nncCommon15MinCurrentSuccessRoutedCallsTransitedViaThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinCurrentSuccessRoutedCallsTransitedViaThisNode.setStatus("current")
_NncCommon15MinCurrentSuccessRoutedCallsTermToLocalSubs_Type = Counter32
_NncCommon15MinCurrentSuccessRoutedCallsTermToLocalSubs_Object = MibTableColumn
nncCommon15MinCurrentSuccessRoutedCallsTermToLocalSubs = _NncCommon15MinCurrentSuccessRoutedCallsTermToLocalSubs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 1, 1, 6),
    _NncCommon15MinCurrentSuccessRoutedCallsTermToLocalSubs_Type()
)
nncCommon15MinCurrentSuccessRoutedCallsTermToLocalSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinCurrentSuccessRoutedCallsTermToLocalSubs.setStatus("current")
_NncCommon15MinCurrentSuccessRoutedLocalCalls_Type = Counter32
_NncCommon15MinCurrentSuccessRoutedLocalCalls_Object = MibTableColumn
nncCommon15MinCurrentSuccessRoutedLocalCalls = _NncCommon15MinCurrentSuccessRoutedLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 1, 1, 7),
    _NncCommon15MinCurrentSuccessRoutedLocalCalls_Type()
)
nncCommon15MinCurrentSuccessRoutedLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinCurrentSuccessRoutedLocalCalls.setStatus("current")
_NncCommon15MinCurrentCallsOrigFromLocalCalls_Type = Counter32
_NncCommon15MinCurrentCallsOrigFromLocalCalls_Object = MibTableColumn
nncCommon15MinCurrentCallsOrigFromLocalCalls = _NncCommon15MinCurrentCallsOrigFromLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 1, 1, 8),
    _NncCommon15MinCurrentCallsOrigFromLocalCalls_Type()
)
nncCommon15MinCurrentCallsOrigFromLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinCurrentCallsOrigFromLocalCalls.setStatus("current")
_NncCommon15MinCurrentCallsTermToLocalCalls_Type = Counter32
_NncCommon15MinCurrentCallsTermToLocalCalls_Object = MibTableColumn
nncCommon15MinCurrentCallsTermToLocalCalls = _NncCommon15MinCurrentCallsTermToLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 1, 1, 9),
    _NncCommon15MinCurrentCallsTermToLocalCalls_Type()
)
nncCommon15MinCurrentCallsTermToLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinCurrentCallsTermToLocalCalls.setStatus("current")
_NncCommon15MinCurrentLocalCallAttempts_Type = Counter32
_NncCommon15MinCurrentLocalCallAttempts_Object = MibTableColumn
nncCommon15MinCurrentLocalCallAttempts = _NncCommon15MinCurrentLocalCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 1, 1, 10),
    _NncCommon15MinCurrentLocalCallAttempts_Type()
)
nncCommon15MinCurrentLocalCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinCurrentLocalCallAttempts.setStatus("current")
_NncCommon15MinCurrentCallsClearedDueToNoRoutingTabEntry_Type = Counter32
_NncCommon15MinCurrentCallsClearedDueToNoRoutingTabEntry_Object = MibTableColumn
nncCommon15MinCurrentCallsClearedDueToNoRoutingTabEntry = _NncCommon15MinCurrentCallsClearedDueToNoRoutingTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 1, 1, 11),
    _NncCommon15MinCurrentCallsClearedDueToNoRoutingTabEntry_Type()
)
nncCommon15MinCurrentCallsClearedDueToNoRoutingTabEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinCurrentCallsClearedDueToNoRoutingTabEntry.setStatus("current")
_NncCommon15MinCurrentCrankbacksGeneratedByThisNode_Type = Counter32
_NncCommon15MinCurrentCrankbacksGeneratedByThisNode_Object = MibTableColumn
nncCommon15MinCurrentCrankbacksGeneratedByThisNode = _NncCommon15MinCurrentCrankbacksGeneratedByThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 1, 1, 12),
    _NncCommon15MinCurrentCrankbacksGeneratedByThisNode_Type()
)
nncCommon15MinCurrentCrankbacksGeneratedByThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinCurrentCrankbacksGeneratedByThisNode.setStatus("current")
_NncCommon15MinCurrentFailedCallsAtLocalSubs_Type = Counter32
_NncCommon15MinCurrentFailedCallsAtLocalSubs_Object = MibTableColumn
nncCommon15MinCurrentFailedCallsAtLocalSubs = _NncCommon15MinCurrentFailedCallsAtLocalSubs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 1, 1, 13),
    _NncCommon15MinCurrentFailedCallsAtLocalSubs_Type()
)
nncCommon15MinCurrentFailedCallsAtLocalSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinCurrentFailedCallsAtLocalSubs.setStatus("current")
_NncCommon15MinCurrentCallsSuccessRerouted_Type = Counter32
_NncCommon15MinCurrentCallsSuccessRerouted_Object = MibTableColumn
nncCommon15MinCurrentCallsSuccessRerouted = _NncCommon15MinCurrentCallsSuccessRerouted_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 1, 1, 14),
    _NncCommon15MinCurrentCallsSuccessRerouted_Type()
)
nncCommon15MinCurrentCallsSuccessRerouted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinCurrentCallsSuccessRerouted.setStatus("current")
_NncCommon15MinCurrentCallsFailedInRerouting_Type = Counter32
_NncCommon15MinCurrentCallsFailedInRerouting_Object = MibTableColumn
nncCommon15MinCurrentCallsFailedInRerouting = _NncCommon15MinCurrentCallsFailedInRerouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 1, 1, 15),
    _NncCommon15MinCurrentCallsFailedInRerouting_Type()
)
nncCommon15MinCurrentCallsFailedInRerouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinCurrentCallsFailedInRerouting.setStatus("current")
_NncRoutingStatsCommon15MinIntervalTable_Object = MibTable
nncRoutingStatsCommon15MinIntervalTable = _NncRoutingStatsCommon15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 2)
)
if mibBuilder.loadTexts:
    nncRoutingStatsCommon15MinIntervalTable.setStatus("current")
_NncRoutingStatsCommon15MinIntervalEntry_Object = MibTableRow
nncRoutingStatsCommon15MinIntervalEntry = _NncRoutingStatsCommon15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 2, 1)
)
nncRoutingStatsCommon15MinIntervalEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsCommon15MinIntervalEntry.setStatus("current")


class _NncCommon15MinIntervalNumber_Type(Integer32):
    """Custom type nncCommon15MinIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NncCommon15MinIntervalNumber_Type.__name__ = "Integer32"
_NncCommon15MinIntervalNumber_Object = MibTableColumn
nncCommon15MinIntervalNumber = _NncCommon15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 2, 1, 2),
    _NncCommon15MinIntervalNumber_Type()
)
nncCommon15MinIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncCommon15MinIntervalNumber.setStatus("current")
_NncCommon15MinIntervalState_Type = NncExtIntvlStateType
_NncCommon15MinIntervalState_Object = MibTableColumn
nncCommon15MinIntervalState = _NncCommon15MinIntervalState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 2, 1, 3),
    _NncCommon15MinIntervalState_Type()
)
nncCommon15MinIntervalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinIntervalState.setStatus("current")
_NncCommon15MinIntervalAbsoluteIntervalNumber_Type = Integer32
_NncCommon15MinIntervalAbsoluteIntervalNumber_Object = MibTableColumn
nncCommon15MinIntervalAbsoluteIntervalNumber = _NncCommon15MinIntervalAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 2, 1, 4),
    _NncCommon15MinIntervalAbsoluteIntervalNumber_Type()
)
nncCommon15MinIntervalAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinIntervalAbsoluteIntervalNumber.setStatus("current")
_NncCommon15MinIntervalSuccessRoutedCallsOrigFromLocalSubs_Type = Counter32
_NncCommon15MinIntervalSuccessRoutedCallsOrigFromLocalSubs_Object = MibTableColumn
nncCommon15MinIntervalSuccessRoutedCallsOrigFromLocalSubs = _NncCommon15MinIntervalSuccessRoutedCallsOrigFromLocalSubs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 2, 1, 5),
    _NncCommon15MinIntervalSuccessRoutedCallsOrigFromLocalSubs_Type()
)
nncCommon15MinIntervalSuccessRoutedCallsOrigFromLocalSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinIntervalSuccessRoutedCallsOrigFromLocalSubs.setStatus("current")
_NncCommon15MinIntervalSuccessRoutedCallsTransitedViaThisNode_Type = Counter32
_NncCommon15MinIntervalSuccessRoutedCallsTransitedViaThisNode_Object = MibTableColumn
nncCommon15MinIntervalSuccessRoutedCallsTransitedViaThisNode = _NncCommon15MinIntervalSuccessRoutedCallsTransitedViaThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 2, 1, 6),
    _NncCommon15MinIntervalSuccessRoutedCallsTransitedViaThisNode_Type()
)
nncCommon15MinIntervalSuccessRoutedCallsTransitedViaThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinIntervalSuccessRoutedCallsTransitedViaThisNode.setStatus("current")
_NncCommon15MinIntervalSuccessRoutedCallsTermToLocalSubs_Type = Counter32
_NncCommon15MinIntervalSuccessRoutedCallsTermToLocalSubs_Object = MibTableColumn
nncCommon15MinIntervalSuccessRoutedCallsTermToLocalSubs = _NncCommon15MinIntervalSuccessRoutedCallsTermToLocalSubs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 2, 1, 7),
    _NncCommon15MinIntervalSuccessRoutedCallsTermToLocalSubs_Type()
)
nncCommon15MinIntervalSuccessRoutedCallsTermToLocalSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinIntervalSuccessRoutedCallsTermToLocalSubs.setStatus("current")
_NncCommon15MinIntervalSuccessRoutedLocalCalls_Type = Counter32
_NncCommon15MinIntervalSuccessRoutedLocalCalls_Object = MibTableColumn
nncCommon15MinIntervalSuccessRoutedLocalCalls = _NncCommon15MinIntervalSuccessRoutedLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 2, 1, 8),
    _NncCommon15MinIntervalSuccessRoutedLocalCalls_Type()
)
nncCommon15MinIntervalSuccessRoutedLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinIntervalSuccessRoutedLocalCalls.setStatus("current")
_NncCommon15MinIntervalCallsOrigFromLocalCalls_Type = Counter32
_NncCommon15MinIntervalCallsOrigFromLocalCalls_Object = MibTableColumn
nncCommon15MinIntervalCallsOrigFromLocalCalls = _NncCommon15MinIntervalCallsOrigFromLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 2, 1, 9),
    _NncCommon15MinIntervalCallsOrigFromLocalCalls_Type()
)
nncCommon15MinIntervalCallsOrigFromLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinIntervalCallsOrigFromLocalCalls.setStatus("current")
_NncCommon15MinIntervalCallsTermToLocalCalls_Type = Counter32
_NncCommon15MinIntervalCallsTermToLocalCalls_Object = MibTableColumn
nncCommon15MinIntervalCallsTermToLocalCalls = _NncCommon15MinIntervalCallsTermToLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 2, 1, 10),
    _NncCommon15MinIntervalCallsTermToLocalCalls_Type()
)
nncCommon15MinIntervalCallsTermToLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinIntervalCallsTermToLocalCalls.setStatus("current")
_NncCommon15MinIntervalLocalCallAttempts_Type = Counter32
_NncCommon15MinIntervalLocalCallAttempts_Object = MibTableColumn
nncCommon15MinIntervalLocalCallAttempts = _NncCommon15MinIntervalLocalCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 2, 1, 11),
    _NncCommon15MinIntervalLocalCallAttempts_Type()
)
nncCommon15MinIntervalLocalCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinIntervalLocalCallAttempts.setStatus("current")
_NncCommon15MinIntervalCallsClearedDueToNoRoutingTabEntry_Type = Counter32
_NncCommon15MinIntervalCallsClearedDueToNoRoutingTabEntry_Object = MibTableColumn
nncCommon15MinIntervalCallsClearedDueToNoRoutingTabEntry = _NncCommon15MinIntervalCallsClearedDueToNoRoutingTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 2, 1, 12),
    _NncCommon15MinIntervalCallsClearedDueToNoRoutingTabEntry_Type()
)
nncCommon15MinIntervalCallsClearedDueToNoRoutingTabEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinIntervalCallsClearedDueToNoRoutingTabEntry.setStatus("current")
_NncCommon15MinIntervalCrankbacksGeneratedByThisNode_Type = Counter32
_NncCommon15MinIntervalCrankbacksGeneratedByThisNode_Object = MibTableColumn
nncCommon15MinIntervalCrankbacksGeneratedByThisNode = _NncCommon15MinIntervalCrankbacksGeneratedByThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 2, 1, 13),
    _NncCommon15MinIntervalCrankbacksGeneratedByThisNode_Type()
)
nncCommon15MinIntervalCrankbacksGeneratedByThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinIntervalCrankbacksGeneratedByThisNode.setStatus("current")
_NncCommon15MinIntervalFailedCallsAtLocalSubs_Type = Counter32
_NncCommon15MinIntervalFailedCallsAtLocalSubs_Object = MibTableColumn
nncCommon15MinIntervalFailedCallsAtLocalSubs = _NncCommon15MinIntervalFailedCallsAtLocalSubs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 2, 1, 14),
    _NncCommon15MinIntervalFailedCallsAtLocalSubs_Type()
)
nncCommon15MinIntervalFailedCallsAtLocalSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinIntervalFailedCallsAtLocalSubs.setStatus("current")
_NncCommon15MinIntervalCallsSuccessRerouted_Type = Counter32
_NncCommon15MinIntervalCallsSuccessRerouted_Object = MibTableColumn
nncCommon15MinIntervalCallsSuccessRerouted = _NncCommon15MinIntervalCallsSuccessRerouted_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 2, 1, 15),
    _NncCommon15MinIntervalCallsSuccessRerouted_Type()
)
nncCommon15MinIntervalCallsSuccessRerouted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinIntervalCallsSuccessRerouted.setStatus("current")
_NncCommon15MinIntervalCallsFailedInRerouting_Type = Counter32
_NncCommon15MinIntervalCallsFailedInRerouting_Object = MibTableColumn
nncCommon15MinIntervalCallsFailedInRerouting = _NncCommon15MinIntervalCallsFailedInRerouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 2, 1, 16),
    _NncCommon15MinIntervalCallsFailedInRerouting_Type()
)
nncCommon15MinIntervalCallsFailedInRerouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon15MinIntervalCallsFailedInRerouting.setStatus("current")
_NncRoutingStatsCommon24HourCurrentTable_Object = MibTable
nncRoutingStatsCommon24HourCurrentTable = _NncRoutingStatsCommon24HourCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 3)
)
if mibBuilder.loadTexts:
    nncRoutingStatsCommon24HourCurrentTable.setStatus("current")
_NncRoutingStatsCommon24HourCurrentEntry_Object = MibTableRow
nncRoutingStatsCommon24HourCurrentEntry = _NncRoutingStatsCommon24HourCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 3, 1)
)
nncRoutingStatsCommon24HourCurrentEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsCommon24HourCurrentEntry.setStatus("current")
_NncCommon24HourCurrentState_Type = NncExtIntvlStateType
_NncCommon24HourCurrentState_Object = MibTableColumn
nncCommon24HourCurrentState = _NncCommon24HourCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 3, 1, 2),
    _NncCommon24HourCurrentState_Type()
)
nncCommon24HourCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourCurrentState.setStatus("current")
_NncCommon24HourCurrentAbsoluteIntervalNumber_Type = Integer32
_NncCommon24HourCurrentAbsoluteIntervalNumber_Object = MibTableColumn
nncCommon24HourCurrentAbsoluteIntervalNumber = _NncCommon24HourCurrentAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 3, 1, 3),
    _NncCommon24HourCurrentAbsoluteIntervalNumber_Type()
)
nncCommon24HourCurrentAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourCurrentAbsoluteIntervalNumber.setStatus("current")
_NncCommon24HourCurrentSuccessRoutedCallsOrigFromLocalSubs_Type = Counter32
_NncCommon24HourCurrentSuccessRoutedCallsOrigFromLocalSubs_Object = MibTableColumn
nncCommon24HourCurrentSuccessRoutedCallsOrigFromLocalSubs = _NncCommon24HourCurrentSuccessRoutedCallsOrigFromLocalSubs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 3, 1, 4),
    _NncCommon24HourCurrentSuccessRoutedCallsOrigFromLocalSubs_Type()
)
nncCommon24HourCurrentSuccessRoutedCallsOrigFromLocalSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourCurrentSuccessRoutedCallsOrigFromLocalSubs.setStatus("current")
_NncCommon24HourCurrentSuccessRoutedCallsTransitedViaThisNode_Type = Counter32
_NncCommon24HourCurrentSuccessRoutedCallsTransitedViaThisNode_Object = MibTableColumn
nncCommon24HourCurrentSuccessRoutedCallsTransitedViaThisNode = _NncCommon24HourCurrentSuccessRoutedCallsTransitedViaThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 3, 1, 5),
    _NncCommon24HourCurrentSuccessRoutedCallsTransitedViaThisNode_Type()
)
nncCommon24HourCurrentSuccessRoutedCallsTransitedViaThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourCurrentSuccessRoutedCallsTransitedViaThisNode.setStatus("current")
_NncCommon24HourCurrentSuccessRoutedCallsTermToLocalSubs_Type = Counter32
_NncCommon24HourCurrentSuccessRoutedCallsTermToLocalSubs_Object = MibTableColumn
nncCommon24HourCurrentSuccessRoutedCallsTermToLocalSubs = _NncCommon24HourCurrentSuccessRoutedCallsTermToLocalSubs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 3, 1, 6),
    _NncCommon24HourCurrentSuccessRoutedCallsTermToLocalSubs_Type()
)
nncCommon24HourCurrentSuccessRoutedCallsTermToLocalSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourCurrentSuccessRoutedCallsTermToLocalSubs.setStatus("current")
_NncCommon24HourCurrentSuccessRoutedLocalCalls_Type = Counter32
_NncCommon24HourCurrentSuccessRoutedLocalCalls_Object = MibTableColumn
nncCommon24HourCurrentSuccessRoutedLocalCalls = _NncCommon24HourCurrentSuccessRoutedLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 3, 1, 7),
    _NncCommon24HourCurrentSuccessRoutedLocalCalls_Type()
)
nncCommon24HourCurrentSuccessRoutedLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourCurrentSuccessRoutedLocalCalls.setStatus("current")
_NncCommon24HourCurrentCallsOrigFromLocalCalls_Type = Counter32
_NncCommon24HourCurrentCallsOrigFromLocalCalls_Object = MibTableColumn
nncCommon24HourCurrentCallsOrigFromLocalCalls = _NncCommon24HourCurrentCallsOrigFromLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 3, 1, 8),
    _NncCommon24HourCurrentCallsOrigFromLocalCalls_Type()
)
nncCommon24HourCurrentCallsOrigFromLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourCurrentCallsOrigFromLocalCalls.setStatus("current")
_NncCommon24HourCurrentCallsTermToLocalCalls_Type = Counter32
_NncCommon24HourCurrentCallsTermToLocalCalls_Object = MibTableColumn
nncCommon24HourCurrentCallsTermToLocalCalls = _NncCommon24HourCurrentCallsTermToLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 3, 1, 9),
    _NncCommon24HourCurrentCallsTermToLocalCalls_Type()
)
nncCommon24HourCurrentCallsTermToLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourCurrentCallsTermToLocalCalls.setStatus("current")
_NncCommon24HourCurrentLocalCallAttempts_Type = Counter32
_NncCommon24HourCurrentLocalCallAttempts_Object = MibTableColumn
nncCommon24HourCurrentLocalCallAttempts = _NncCommon24HourCurrentLocalCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 3, 1, 10),
    _NncCommon24HourCurrentLocalCallAttempts_Type()
)
nncCommon24HourCurrentLocalCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourCurrentLocalCallAttempts.setStatus("current")
_NncCommon24HourCurrentCallsClearedDueToNoRoutingTabEntry_Type = Counter32
_NncCommon24HourCurrentCallsClearedDueToNoRoutingTabEntry_Object = MibTableColumn
nncCommon24HourCurrentCallsClearedDueToNoRoutingTabEntry = _NncCommon24HourCurrentCallsClearedDueToNoRoutingTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 3, 1, 11),
    _NncCommon24HourCurrentCallsClearedDueToNoRoutingTabEntry_Type()
)
nncCommon24HourCurrentCallsClearedDueToNoRoutingTabEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourCurrentCallsClearedDueToNoRoutingTabEntry.setStatus("current")
_NncCommon24HourCurrentCrankbacksGeneratedByThisNode_Type = Counter32
_NncCommon24HourCurrentCrankbacksGeneratedByThisNode_Object = MibTableColumn
nncCommon24HourCurrentCrankbacksGeneratedByThisNode = _NncCommon24HourCurrentCrankbacksGeneratedByThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 3, 1, 12),
    _NncCommon24HourCurrentCrankbacksGeneratedByThisNode_Type()
)
nncCommon24HourCurrentCrankbacksGeneratedByThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourCurrentCrankbacksGeneratedByThisNode.setStatus("current")
_NncCommon24HourCurrentFailedCallsAtLocalSubs_Type = Counter32
_NncCommon24HourCurrentFailedCallsAtLocalSubs_Object = MibTableColumn
nncCommon24HourCurrentFailedCallsAtLocalSubs = _NncCommon24HourCurrentFailedCallsAtLocalSubs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 3, 1, 13),
    _NncCommon24HourCurrentFailedCallsAtLocalSubs_Type()
)
nncCommon24HourCurrentFailedCallsAtLocalSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourCurrentFailedCallsAtLocalSubs.setStatus("current")
_NncCommon24HourCurrentCallsSuccessRerouted_Type = Counter32
_NncCommon24HourCurrentCallsSuccessRerouted_Object = MibTableColumn
nncCommon24HourCurrentCallsSuccessRerouted = _NncCommon24HourCurrentCallsSuccessRerouted_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 3, 1, 14),
    _NncCommon24HourCurrentCallsSuccessRerouted_Type()
)
nncCommon24HourCurrentCallsSuccessRerouted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourCurrentCallsSuccessRerouted.setStatus("current")
_NncCommon24HourCurrentCallsFailedInRerouting_Type = Counter32
_NncCommon24HourCurrentCallsFailedInRerouting_Object = MibTableColumn
nncCommon24HourCurrentCallsFailedInRerouting = _NncCommon24HourCurrentCallsFailedInRerouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 3, 1, 15),
    _NncCommon24HourCurrentCallsFailedInRerouting_Type()
)
nncCommon24HourCurrentCallsFailedInRerouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourCurrentCallsFailedInRerouting.setStatus("current")
_NncRoutingStatsCommon24HourIntervalTable_Object = MibTable
nncRoutingStatsCommon24HourIntervalTable = _NncRoutingStatsCommon24HourIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 4)
)
if mibBuilder.loadTexts:
    nncRoutingStatsCommon24HourIntervalTable.setStatus("current")
_NncRoutingStatsCommon24HourIntervalEntry_Object = MibTableRow
nncRoutingStatsCommon24HourIntervalEntry = _NncRoutingStatsCommon24HourIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 4, 1)
)
nncRoutingStatsCommon24HourIntervalEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourIntervalNumber"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsCommon24HourIntervalEntry.setStatus("current")
_NncCommon24HourIntervalNumber_Type = Integer32
_NncCommon24HourIntervalNumber_Object = MibTableColumn
nncCommon24HourIntervalNumber = _NncCommon24HourIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 4, 1, 2),
    _NncCommon24HourIntervalNumber_Type()
)
nncCommon24HourIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncCommon24HourIntervalNumber.setStatus("current")
_NncCommon24HourIntervalState_Type = NncExtIntvlStateType
_NncCommon24HourIntervalState_Object = MibTableColumn
nncCommon24HourIntervalState = _NncCommon24HourIntervalState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 4, 1, 3),
    _NncCommon24HourIntervalState_Type()
)
nncCommon24HourIntervalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourIntervalState.setStatus("current")
_NncCommon24HourIntervalAbsoluteIntervalNumber_Type = Integer32
_NncCommon24HourIntervalAbsoluteIntervalNumber_Object = MibTableColumn
nncCommon24HourIntervalAbsoluteIntervalNumber = _NncCommon24HourIntervalAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 4, 1, 4),
    _NncCommon24HourIntervalAbsoluteIntervalNumber_Type()
)
nncCommon24HourIntervalAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourIntervalAbsoluteIntervalNumber.setStatus("current")
_NncCommon24HourIntervalSuccessRoutedCallsOrigFromLocalSubs_Type = Counter32
_NncCommon24HourIntervalSuccessRoutedCallsOrigFromLocalSubs_Object = MibTableColumn
nncCommon24HourIntervalSuccessRoutedCallsOrigFromLocalSubs = _NncCommon24HourIntervalSuccessRoutedCallsOrigFromLocalSubs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 4, 1, 5),
    _NncCommon24HourIntervalSuccessRoutedCallsOrigFromLocalSubs_Type()
)
nncCommon24HourIntervalSuccessRoutedCallsOrigFromLocalSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourIntervalSuccessRoutedCallsOrigFromLocalSubs.setStatus("current")
_NncCommon24HourIntervalSuccessRoutedCallsTransitedViaThisNode_Type = Counter32
_NncCommon24HourIntervalSuccessRoutedCallsTransitedViaThisNode_Object = MibTableColumn
nncCommon24HourIntervalSuccessRoutedCallsTransitedViaThisNode = _NncCommon24HourIntervalSuccessRoutedCallsTransitedViaThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 4, 1, 6),
    _NncCommon24HourIntervalSuccessRoutedCallsTransitedViaThisNode_Type()
)
nncCommon24HourIntervalSuccessRoutedCallsTransitedViaThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourIntervalSuccessRoutedCallsTransitedViaThisNode.setStatus("current")
_NncCommon24HourIntervalSuccessRoutedCallsTermToLocalSubs_Type = Counter32
_NncCommon24HourIntervalSuccessRoutedCallsTermToLocalSubs_Object = MibTableColumn
nncCommon24HourIntervalSuccessRoutedCallsTermToLocalSubs = _NncCommon24HourIntervalSuccessRoutedCallsTermToLocalSubs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 4, 1, 7),
    _NncCommon24HourIntervalSuccessRoutedCallsTermToLocalSubs_Type()
)
nncCommon24HourIntervalSuccessRoutedCallsTermToLocalSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourIntervalSuccessRoutedCallsTermToLocalSubs.setStatus("current")
_NncCommon24HourIntervalSuccessRoutedLocalCalls_Type = Counter32
_NncCommon24HourIntervalSuccessRoutedLocalCalls_Object = MibTableColumn
nncCommon24HourIntervalSuccessRoutedLocalCalls = _NncCommon24HourIntervalSuccessRoutedLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 4, 1, 8),
    _NncCommon24HourIntervalSuccessRoutedLocalCalls_Type()
)
nncCommon24HourIntervalSuccessRoutedLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourIntervalSuccessRoutedLocalCalls.setStatus("current")
_NncCommon24HourIntervalCallsOrigFromLocalCalls_Type = Counter32
_NncCommon24HourIntervalCallsOrigFromLocalCalls_Object = MibTableColumn
nncCommon24HourIntervalCallsOrigFromLocalCalls = _NncCommon24HourIntervalCallsOrigFromLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 4, 1, 9),
    _NncCommon24HourIntervalCallsOrigFromLocalCalls_Type()
)
nncCommon24HourIntervalCallsOrigFromLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourIntervalCallsOrigFromLocalCalls.setStatus("current")
_NncCommon24HourIntervalCallsTermToLocalCalls_Type = Counter32
_NncCommon24HourIntervalCallsTermToLocalCalls_Object = MibTableColumn
nncCommon24HourIntervalCallsTermToLocalCalls = _NncCommon24HourIntervalCallsTermToLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 4, 1, 10),
    _NncCommon24HourIntervalCallsTermToLocalCalls_Type()
)
nncCommon24HourIntervalCallsTermToLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourIntervalCallsTermToLocalCalls.setStatus("current")
_NncCommon24HourIntervalLocalCallAttempts_Type = Counter32
_NncCommon24HourIntervalLocalCallAttempts_Object = MibTableColumn
nncCommon24HourIntervalLocalCallAttempts = _NncCommon24HourIntervalLocalCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 4, 1, 11),
    _NncCommon24HourIntervalLocalCallAttempts_Type()
)
nncCommon24HourIntervalLocalCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourIntervalLocalCallAttempts.setStatus("current")
_NncCommon24HourIntervalCallsClearedDueToNoRoutingTabEntry_Type = Counter32
_NncCommon24HourIntervalCallsClearedDueToNoRoutingTabEntry_Object = MibTableColumn
nncCommon24HourIntervalCallsClearedDueToNoRoutingTabEntry = _NncCommon24HourIntervalCallsClearedDueToNoRoutingTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 4, 1, 12),
    _NncCommon24HourIntervalCallsClearedDueToNoRoutingTabEntry_Type()
)
nncCommon24HourIntervalCallsClearedDueToNoRoutingTabEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourIntervalCallsClearedDueToNoRoutingTabEntry.setStatus("current")
_NncCommon24HourIntervalCrankbacksGeneratedByThisNode_Type = Counter32
_NncCommon24HourIntervalCrankbacksGeneratedByThisNode_Object = MibTableColumn
nncCommon24HourIntervalCrankbacksGeneratedByThisNode = _NncCommon24HourIntervalCrankbacksGeneratedByThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 4, 1, 13),
    _NncCommon24HourIntervalCrankbacksGeneratedByThisNode_Type()
)
nncCommon24HourIntervalCrankbacksGeneratedByThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourIntervalCrankbacksGeneratedByThisNode.setStatus("current")
_NncCommon24HourIntervalFailedCallsAtLocalSubs_Type = Counter32
_NncCommon24HourIntervalFailedCallsAtLocalSubs_Object = MibTableColumn
nncCommon24HourIntervalFailedCallsAtLocalSubs = _NncCommon24HourIntervalFailedCallsAtLocalSubs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 4, 1, 14),
    _NncCommon24HourIntervalFailedCallsAtLocalSubs_Type()
)
nncCommon24HourIntervalFailedCallsAtLocalSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourIntervalFailedCallsAtLocalSubs.setStatus("current")
_NncCommon24HourIntervalCallsSuccessRerouted_Type = Counter32
_NncCommon24HourIntervalCallsSuccessRerouted_Object = MibTableColumn
nncCommon24HourIntervalCallsSuccessRerouted = _NncCommon24HourIntervalCallsSuccessRerouted_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 4, 1, 15),
    _NncCommon24HourIntervalCallsSuccessRerouted_Type()
)
nncCommon24HourIntervalCallsSuccessRerouted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourIntervalCallsSuccessRerouted.setStatus("current")
_NncCommon24HourIntervalCallsFailedInRerouting_Type = Counter32
_NncCommon24HourIntervalCallsFailedInRerouting_Object = MibTableColumn
nncCommon24HourIntervalCallsFailedInRerouting = _NncCommon24HourIntervalCallsFailedInRerouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 4, 1, 16),
    _NncCommon24HourIntervalCallsFailedInRerouting_Type()
)
nncCommon24HourIntervalCallsFailedInRerouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCommon24HourIntervalCallsFailedInRerouting.setStatus("current")
_NncRoutingStatsSpecific15MinCurrentTable_Object = MibTable
nncRoutingStatsSpecific15MinCurrentTable = _NncRoutingStatsSpecific15MinCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 5)
)
if mibBuilder.loadTexts:
    nncRoutingStatsSpecific15MinCurrentTable.setStatus("current")
_NncRoutingStatsSpecific15MinCurrentEntry_Object = MibTableRow
nncRoutingStatsSpecific15MinCurrentEntry = _NncRoutingStatsSpecific15MinCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 5, 1)
)
nncRoutingStatsSpecific15MinCurrentEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsSpecific15MinCurrentEntry.setStatus("current")
_NncSpecific15MinCurrentState_Type = NncExtIntvlStateType
_NncSpecific15MinCurrentState_Object = MibTableColumn
nncSpecific15MinCurrentState = _NncSpecific15MinCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 5, 1, 2),
    _NncSpecific15MinCurrentState_Type()
)
nncSpecific15MinCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSpecific15MinCurrentState.setStatus("current")
_NncSpecific15MinCurrentAbsoluteIntervalNumber_Type = Integer32
_NncSpecific15MinCurrentAbsoluteIntervalNumber_Object = MibTableColumn
nncSpecific15MinCurrentAbsoluteIntervalNumber = _NncSpecific15MinCurrentAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 5, 1, 3),
    _NncSpecific15MinCurrentAbsoluteIntervalNumber_Type()
)
nncSpecific15MinCurrentAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSpecific15MinCurrentAbsoluteIntervalNumber.setStatus("current")
_NncSpecific15MinCurrentCallsStaticallyRoutedByThisNode_Type = Counter32
_NncSpecific15MinCurrentCallsStaticallyRoutedByThisNode_Object = MibTableColumn
nncSpecific15MinCurrentCallsStaticallyRoutedByThisNode = _NncSpecific15MinCurrentCallsStaticallyRoutedByThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 5, 1, 4),
    _NncSpecific15MinCurrentCallsStaticallyRoutedByThisNode_Type()
)
nncSpecific15MinCurrentCallsStaticallyRoutedByThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSpecific15MinCurrentCallsStaticallyRoutedByThisNode.setStatus("current")
_NncSpecific15MinCurrentCrankbacksReceivedByThisNode_Type = Counter32
_NncSpecific15MinCurrentCrankbacksReceivedByThisNode_Object = MibTableColumn
nncSpecific15MinCurrentCrankbacksReceivedByThisNode = _NncSpecific15MinCurrentCrankbacksReceivedByThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 5, 1, 5),
    _NncSpecific15MinCurrentCrankbacksReceivedByThisNode_Type()
)
nncSpecific15MinCurrentCrankbacksReceivedByThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSpecific15MinCurrentCrankbacksReceivedByThisNode.setStatus("current")
_NncSpecific15MinCurrentRerouteAttempts_Type = Counter32
_NncSpecific15MinCurrentRerouteAttempts_Object = MibTableColumn
nncSpecific15MinCurrentRerouteAttempts = _NncSpecific15MinCurrentRerouteAttempts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 5, 1, 6),
    _NncSpecific15MinCurrentRerouteAttempts_Type()
)
nncSpecific15MinCurrentRerouteAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSpecific15MinCurrentRerouteAttempts.setStatus("current")
_NncSpecific15MinCurrentRoutingLoopsDetectedByThisNode_Type = Counter32
_NncSpecific15MinCurrentRoutingLoopsDetectedByThisNode_Object = MibTableColumn
nncSpecific15MinCurrentRoutingLoopsDetectedByThisNode = _NncSpecific15MinCurrentRoutingLoopsDetectedByThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 5, 1, 7),
    _NncSpecific15MinCurrentRoutingLoopsDetectedByThisNode_Type()
)
nncSpecific15MinCurrentRoutingLoopsDetectedByThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSpecific15MinCurrentRoutingLoopsDetectedByThisNode.setStatus("current")
_NncRoutingStatsSpecific15MinIntervalTable_Object = MibTable
nncRoutingStatsSpecific15MinIntervalTable = _NncRoutingStatsSpecific15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 6)
)
if mibBuilder.loadTexts:
    nncRoutingStatsSpecific15MinIntervalTable.setStatus("current")
_NncRoutingStatsSpecific15MinIntervalEntry_Object = MibTableRow
nncRoutingStatsSpecific15MinIntervalEntry = _NncRoutingStatsSpecific15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 6, 1)
)
nncRoutingStatsSpecific15MinIntervalEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncSpecific15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsSpecific15MinIntervalEntry.setStatus("current")


class _NncSpecific15MinIntervalNumber_Type(Integer32):
    """Custom type nncSpecific15MinIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NncSpecific15MinIntervalNumber_Type.__name__ = "Integer32"
_NncSpecific15MinIntervalNumber_Object = MibTableColumn
nncSpecific15MinIntervalNumber = _NncSpecific15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 6, 1, 2),
    _NncSpecific15MinIntervalNumber_Type()
)
nncSpecific15MinIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncSpecific15MinIntervalNumber.setStatus("current")
_NncSpecific15MinIntervalState_Type = NncExtIntvlStateType
_NncSpecific15MinIntervalState_Object = MibTableColumn
nncSpecific15MinIntervalState = _NncSpecific15MinIntervalState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 6, 1, 3),
    _NncSpecific15MinIntervalState_Type()
)
nncSpecific15MinIntervalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSpecific15MinIntervalState.setStatus("current")
_NncSpecific15MinIntervalAbsoluteIntervalNumber_Type = Integer32
_NncSpecific15MinIntervalAbsoluteIntervalNumber_Object = MibTableColumn
nncSpecific15MinIntervalAbsoluteIntervalNumber = _NncSpecific15MinIntervalAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 6, 1, 4),
    _NncSpecific15MinIntervalAbsoluteIntervalNumber_Type()
)
nncSpecific15MinIntervalAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSpecific15MinIntervalAbsoluteIntervalNumber.setStatus("current")
_NncSpecific15MinIntervalCallsStaticallyRoutedByThisNode_Type = Counter32
_NncSpecific15MinIntervalCallsStaticallyRoutedByThisNode_Object = MibTableColumn
nncSpecific15MinIntervalCallsStaticallyRoutedByThisNode = _NncSpecific15MinIntervalCallsStaticallyRoutedByThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 6, 1, 5),
    _NncSpecific15MinIntervalCallsStaticallyRoutedByThisNode_Type()
)
nncSpecific15MinIntervalCallsStaticallyRoutedByThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSpecific15MinIntervalCallsStaticallyRoutedByThisNode.setStatus("current")
_NncSpecific15MinIntervalCrankbacksReceivedByThisNode_Type = Counter32
_NncSpecific15MinIntervalCrankbacksReceivedByThisNode_Object = MibTableColumn
nncSpecific15MinIntervalCrankbacksReceivedByThisNode = _NncSpecific15MinIntervalCrankbacksReceivedByThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 6, 1, 6),
    _NncSpecific15MinIntervalCrankbacksReceivedByThisNode_Type()
)
nncSpecific15MinIntervalCrankbacksReceivedByThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSpecific15MinIntervalCrankbacksReceivedByThisNode.setStatus("current")
_NncSpecific15MinIntervalRerouteAttempts_Type = Counter32
_NncSpecific15MinIntervalRerouteAttempts_Object = MibTableColumn
nncSpecific15MinIntervalRerouteAttempts = _NncSpecific15MinIntervalRerouteAttempts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 6, 1, 7),
    _NncSpecific15MinIntervalRerouteAttempts_Type()
)
nncSpecific15MinIntervalRerouteAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSpecific15MinIntervalRerouteAttempts.setStatus("current")
_NncSpecific15MinIntervalRoutingLoopsDetectedByThisNode_Type = Counter32
_NncSpecific15MinIntervalRoutingLoopsDetectedByThisNode_Object = MibTableColumn
nncSpecific15MinIntervalRoutingLoopsDetectedByThisNode = _NncSpecific15MinIntervalRoutingLoopsDetectedByThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 6, 1, 8),
    _NncSpecific15MinIntervalRoutingLoopsDetectedByThisNode_Type()
)
nncSpecific15MinIntervalRoutingLoopsDetectedByThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSpecific15MinIntervalRoutingLoopsDetectedByThisNode.setStatus("current")
_NncRoutingStatsSpecific24HourCurrentTable_Object = MibTable
nncRoutingStatsSpecific24HourCurrentTable = _NncRoutingStatsSpecific24HourCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 7)
)
if mibBuilder.loadTexts:
    nncRoutingStatsSpecific24HourCurrentTable.setStatus("current")
_NncRoutingStatsSpecific24HourCurrentEntry_Object = MibTableRow
nncRoutingStatsSpecific24HourCurrentEntry = _NncRoutingStatsSpecific24HourCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 7, 1)
)
nncRoutingStatsSpecific24HourCurrentEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsSpecific24HourCurrentEntry.setStatus("current")
_NncSpecific24HourCurrentState_Type = NncExtIntvlStateType
_NncSpecific24HourCurrentState_Object = MibTableColumn
nncSpecific24HourCurrentState = _NncSpecific24HourCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 7, 1, 2),
    _NncSpecific24HourCurrentState_Type()
)
nncSpecific24HourCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSpecific24HourCurrentState.setStatus("current")
_NncSpecific24HourCurrentAbsoluteIntervalNumber_Type = Integer32
_NncSpecific24HourCurrentAbsoluteIntervalNumber_Object = MibTableColumn
nncSpecific24HourCurrentAbsoluteIntervalNumber = _NncSpecific24HourCurrentAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 7, 1, 3),
    _NncSpecific24HourCurrentAbsoluteIntervalNumber_Type()
)
nncSpecific24HourCurrentAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSpecific24HourCurrentAbsoluteIntervalNumber.setStatus("current")
_NncSpecific24HourCurrentCallsStaticallyRoutedByThisNode_Type = Counter32
_NncSpecific24HourCurrentCallsStaticallyRoutedByThisNode_Object = MibTableColumn
nncSpecific24HourCurrentCallsStaticallyRoutedByThisNode = _NncSpecific24HourCurrentCallsStaticallyRoutedByThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 7, 1, 4),
    _NncSpecific24HourCurrentCallsStaticallyRoutedByThisNode_Type()
)
nncSpecific24HourCurrentCallsStaticallyRoutedByThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSpecific24HourCurrentCallsStaticallyRoutedByThisNode.setStatus("current")
_NncSpecific24HourCurrentCrankbacksReceivedByThisNode_Type = Counter32
_NncSpecific24HourCurrentCrankbacksReceivedByThisNode_Object = MibTableColumn
nncSpecific24HourCurrentCrankbacksReceivedByThisNode = _NncSpecific24HourCurrentCrankbacksReceivedByThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 7, 1, 5),
    _NncSpecific24HourCurrentCrankbacksReceivedByThisNode_Type()
)
nncSpecific24HourCurrentCrankbacksReceivedByThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSpecific24HourCurrentCrankbacksReceivedByThisNode.setStatus("current")
_NncSpecific24HourCurrentRerouteAttempts_Type = Counter32
_NncSpecific24HourCurrentRerouteAttempts_Object = MibTableColumn
nncSpecific24HourCurrentRerouteAttempts = _NncSpecific24HourCurrentRerouteAttempts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 7, 1, 6),
    _NncSpecific24HourCurrentRerouteAttempts_Type()
)
nncSpecific24HourCurrentRerouteAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSpecific24HourCurrentRerouteAttempts.setStatus("current")
_NncSpecific24HourCurrentRoutingLoopsDetectedByThisNode_Type = Counter32
_NncSpecific24HourCurrentRoutingLoopsDetectedByThisNode_Object = MibTableColumn
nncSpecific24HourCurrentRoutingLoopsDetectedByThisNode = _NncSpecific24HourCurrentRoutingLoopsDetectedByThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 7, 1, 7),
    _NncSpecific24HourCurrentRoutingLoopsDetectedByThisNode_Type()
)
nncSpecific24HourCurrentRoutingLoopsDetectedByThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSpecific24HourCurrentRoutingLoopsDetectedByThisNode.setStatus("current")
_NncRoutingStatsSpecific24HourIntervalTable_Object = MibTable
nncRoutingStatsSpecific24HourIntervalTable = _NncRoutingStatsSpecific24HourIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 8)
)
if mibBuilder.loadTexts:
    nncRoutingStatsSpecific24HourIntervalTable.setStatus("current")
_NncRoutingStatsSpecific24HourIntervalEntry_Object = MibTableRow
nncRoutingStatsSpecific24HourIntervalEntry = _NncRoutingStatsSpecific24HourIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 8, 1)
)
nncRoutingStatsSpecific24HourIntervalEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncSpecific24HourIntervalNumber"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsSpecific24HourIntervalEntry.setStatus("current")
_NncSpecific24HourIntervalNumber_Type = Integer32
_NncSpecific24HourIntervalNumber_Object = MibTableColumn
nncSpecific24HourIntervalNumber = _NncSpecific24HourIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 8, 1, 2),
    _NncSpecific24HourIntervalNumber_Type()
)
nncSpecific24HourIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncSpecific24HourIntervalNumber.setStatus("current")
_NncSpecific24HourIntervalState_Type = NncExtIntvlStateType
_NncSpecific24HourIntervalState_Object = MibTableColumn
nncSpecific24HourIntervalState = _NncSpecific24HourIntervalState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 8, 1, 3),
    _NncSpecific24HourIntervalState_Type()
)
nncSpecific24HourIntervalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSpecific24HourIntervalState.setStatus("current")
_NncSpecific24HourIntervalAbsoluteIntervalNumber_Type = Integer32
_NncSpecific24HourIntervalAbsoluteIntervalNumber_Object = MibTableColumn
nncSpecific24HourIntervalAbsoluteIntervalNumber = _NncSpecific24HourIntervalAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 8, 1, 4),
    _NncSpecific24HourIntervalAbsoluteIntervalNumber_Type()
)
nncSpecific24HourIntervalAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSpecific24HourIntervalAbsoluteIntervalNumber.setStatus("current")
_NncSpecific24HourIntervalCallsStaticallyRoutedByThisNode_Type = Counter32
_NncSpecific24HourIntervalCallsStaticallyRoutedByThisNode_Object = MibTableColumn
nncSpecific24HourIntervalCallsStaticallyRoutedByThisNode = _NncSpecific24HourIntervalCallsStaticallyRoutedByThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 8, 1, 5),
    _NncSpecific24HourIntervalCallsStaticallyRoutedByThisNode_Type()
)
nncSpecific24HourIntervalCallsStaticallyRoutedByThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSpecific24HourIntervalCallsStaticallyRoutedByThisNode.setStatus("current")
_NncSpecific24HourIntervalCrankbacksReceivedByThisNode_Type = Counter32
_NncSpecific24HourIntervalCrankbacksReceivedByThisNode_Object = MibTableColumn
nncSpecific24HourIntervalCrankbacksReceivedByThisNode = _NncSpecific24HourIntervalCrankbacksReceivedByThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 8, 1, 6),
    _NncSpecific24HourIntervalCrankbacksReceivedByThisNode_Type()
)
nncSpecific24HourIntervalCrankbacksReceivedByThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSpecific24HourIntervalCrankbacksReceivedByThisNode.setStatus("current")
_NncSpecific24HourIntervalRerouteAttempts_Type = Counter32
_NncSpecific24HourIntervalRerouteAttempts_Object = MibTableColumn
nncSpecific24HourIntervalRerouteAttempts = _NncSpecific24HourIntervalRerouteAttempts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 8, 1, 7),
    _NncSpecific24HourIntervalRerouteAttempts_Type()
)
nncSpecific24HourIntervalRerouteAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSpecific24HourIntervalRerouteAttempts.setStatus("current")
_NncSpecific24HourIntervalRoutingLoopsDetectedByThisNode_Type = Counter32
_NncSpecific24HourIntervalRoutingLoopsDetectedByThisNode_Object = MibTableColumn
nncSpecific24HourIntervalRoutingLoopsDetectedByThisNode = _NncSpecific24HourIntervalRoutingLoopsDetectedByThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 8, 1, 8),
    _NncSpecific24HourIntervalRoutingLoopsDetectedByThisNode_Type()
)
nncSpecific24HourIntervalRoutingLoopsDetectedByThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSpecific24HourIntervalRoutingLoopsDetectedByThisNode.setStatus("current")
_NncRoutingStatsNonBorderPerTbl15MinCurrentTable_Object = MibTable
nncRoutingStatsNonBorderPerTbl15MinCurrentTable = _NncRoutingStatsNonBorderPerTbl15MinCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 9)
)
if mibBuilder.loadTexts:
    nncRoutingStatsNonBorderPerTbl15MinCurrentTable.setStatus("current")
_NncRoutingStatsNonBorderPerTbl15MinCurrentEntry_Object = MibTableRow
nncRoutingStatsNonBorderPerTbl15MinCurrentEntry = _NncRoutingStatsNonBorderPerTbl15MinCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 9, 1)
)
nncRoutingStatsNonBorderPerTbl15MinCurrentEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl15MinCurrentTableDescriptor"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsNonBorderPerTbl15MinCurrentEntry.setStatus("current")


class _NncNBPerTbl15MinCurrentTableDescriptor_Type(Integer32):
    """Custom type nncNBPerTbl15MinCurrentTableDescriptor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_NncNBPerTbl15MinCurrentTableDescriptor_Type.__name__ = "Integer32"
_NncNBPerTbl15MinCurrentTableDescriptor_Object = MibTableColumn
nncNBPerTbl15MinCurrentTableDescriptor = _NncNBPerTbl15MinCurrentTableDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 9, 1, 2),
    _NncNBPerTbl15MinCurrentTableDescriptor_Type()
)
nncNBPerTbl15MinCurrentTableDescriptor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncNBPerTbl15MinCurrentTableDescriptor.setStatus("current")
_NncNBPerTbl15MinCurrentState_Type = NncExtIntvlStateType
_NncNBPerTbl15MinCurrentState_Object = MibTableColumn
nncNBPerTbl15MinCurrentState = _NncNBPerTbl15MinCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 9, 1, 3),
    _NncNBPerTbl15MinCurrentState_Type()
)
nncNBPerTbl15MinCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl15MinCurrentState.setStatus("current")
_NncNBPerTbl15MinCurrentAbsoluteIntervalNumber_Type = Integer32
_NncNBPerTbl15MinCurrentAbsoluteIntervalNumber_Object = MibTableColumn
nncNBPerTbl15MinCurrentAbsoluteIntervalNumber = _NncNBPerTbl15MinCurrentAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 9, 1, 4),
    _NncNBPerTbl15MinCurrentAbsoluteIntervalNumber_Type()
)
nncNBPerTbl15MinCurrentAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl15MinCurrentAbsoluteIntervalNumber.setStatus("current")
_NncNBPerTbl15MinCurrentFailedCallsDueToInitDTLNotGenerated_Type = Counter32
_NncNBPerTbl15MinCurrentFailedCallsDueToInitDTLNotGenerated_Object = MibTableColumn
nncNBPerTbl15MinCurrentFailedCallsDueToInitDTLNotGenerated = _NncNBPerTbl15MinCurrentFailedCallsDueToInitDTLNotGenerated_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 9, 1, 5),
    _NncNBPerTbl15MinCurrentFailedCallsDueToInitDTLNotGenerated_Type()
)
nncNBPerTbl15MinCurrentFailedCallsDueToInitDTLNotGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl15MinCurrentFailedCallsDueToInitDTLNotGenerated.setStatus("current")
_NncNBPerTbl15MinCurrentCallsGeneratingAnInitDTL_Type = Counter32
_NncNBPerTbl15MinCurrentCallsGeneratingAnInitDTL_Object = MibTableColumn
nncNBPerTbl15MinCurrentCallsGeneratingAnInitDTL = _NncNBPerTbl15MinCurrentCallsGeneratingAnInitDTL_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 9, 1, 6),
    _NncNBPerTbl15MinCurrentCallsGeneratingAnInitDTL_Type()
)
nncNBPerTbl15MinCurrentCallsGeneratingAnInitDTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl15MinCurrentCallsGeneratingAnInitDTL.setStatus("current")
_NncNBPerTble15MinCurrentDTLOrigCallsSuccessEstWithoutReroute_Type = Counter32
_NncNBPerTble15MinCurrentDTLOrigCallsSuccessEstWithoutReroute_Object = MibTableColumn
nncNBPerTble15MinCurrentDTLOrigCallsSuccessEstWithoutReroute = _NncNBPerTble15MinCurrentDTLOrigCallsSuccessEstWithoutReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 9, 1, 7),
    _NncNBPerTble15MinCurrentDTLOrigCallsSuccessEstWithoutReroute_Type()
)
nncNBPerTble15MinCurrentDTLOrigCallsSuccessEstWithoutReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTble15MinCurrentDTLOrigCallsSuccessEstWithoutReroute.setStatus("current")
_NncNBPerTbl15MinCurrentDTLOrigCallsSuccessEstWithReroute_Type = Counter32
_NncNBPerTbl15MinCurrentDTLOrigCallsSuccessEstWithReroute_Object = MibTableColumn
nncNBPerTbl15MinCurrentDTLOrigCallsSuccessEstWithReroute = _NncNBPerTbl15MinCurrentDTLOrigCallsSuccessEstWithReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 9, 1, 8),
    _NncNBPerTbl15MinCurrentDTLOrigCallsSuccessEstWithReroute_Type()
)
nncNBPerTbl15MinCurrentDTLOrigCallsSuccessEstWithReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl15MinCurrentDTLOrigCallsSuccessEstWithReroute.setStatus("current")
_NncNBPerTbl15MinCurrentDTLOrigCallsFailedInReRouting_Type = Counter32
_NncNBPerTbl15MinCurrentDTLOrigCallsFailedInReRouting_Object = MibTableColumn
nncNBPerTbl15MinCurrentDTLOrigCallsFailedInReRouting = _NncNBPerTbl15MinCurrentDTLOrigCallsFailedInReRouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 9, 1, 9),
    _NncNBPerTbl15MinCurrentDTLOrigCallsFailedInReRouting_Type()
)
nncNBPerTbl15MinCurrentDTLOrigCallsFailedInReRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl15MinCurrentDTLOrigCallsFailedInReRouting.setStatus("current")
_NncNBPerTbl15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncNBPerTbl15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncNBPerTbl15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw = _NncNBPerTbl15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 9, 1, 10),
    _NncNBPerTbl15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Type()
)
nncNBPerTbl15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncNBPerTbl15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncNBPerTbl15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncNBPerTbl15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw = _NncNBPerTbl15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 9, 1, 11),
    _NncNBPerTbl15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw_Type()
)
nncNBPerTbl15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncNBPerTbl15MinCurrentCrankbackReceivedAsDTLOriginator_Type = Counter32
_NncNBPerTbl15MinCurrentCrankbackReceivedAsDTLOriginator_Object = MibTableColumn
nncNBPerTbl15MinCurrentCrankbackReceivedAsDTLOriginator = _NncNBPerTbl15MinCurrentCrankbackReceivedAsDTLOriginator_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 9, 1, 12),
    _NncNBPerTbl15MinCurrentCrankbackReceivedAsDTLOriginator_Type()
)
nncNBPerTbl15MinCurrentCrankbackReceivedAsDTLOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl15MinCurrentCrankbackReceivedAsDTLOriginator.setStatus("current")
_NncNBPerTbl15MinCurrentDTLsGeneratedDueToCrankback_Type = Counter32
_NncNBPerTbl15MinCurrentDTLsGeneratedDueToCrankback_Object = MibTableColumn
nncNBPerTbl15MinCurrentDTLsGeneratedDueToCrankback = _NncNBPerTbl15MinCurrentDTLsGeneratedDueToCrankback_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 9, 1, 13),
    _NncNBPerTbl15MinCurrentDTLsGeneratedDueToCrankback_Type()
)
nncNBPerTbl15MinCurrentDTLsGeneratedDueToCrankback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl15MinCurrentDTLsGeneratedDueToCrankback.setStatus("current")
_NncRoutingStatsNonBorderPerTbl15MinIntervalTable_Object = MibTable
nncRoutingStatsNonBorderPerTbl15MinIntervalTable = _NncRoutingStatsNonBorderPerTbl15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 10)
)
if mibBuilder.loadTexts:
    nncRoutingStatsNonBorderPerTbl15MinIntervalTable.setStatus("current")
_NncRoutingStatsNonBorderPerTbl15MinIntervalEntry_Object = MibTableRow
nncRoutingStatsNonBorderPerTbl15MinIntervalEntry = _NncRoutingStatsNonBorderPerTbl15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 10, 1)
)
nncRoutingStatsNonBorderPerTbl15MinIntervalEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl15MinIntervalNumber"),
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl15MinIntervalTableDescriptor"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsNonBorderPerTbl15MinIntervalEntry.setStatus("current")


class _NncNBPerTbl15MinIntervalNumber_Type(Integer32):
    """Custom type nncNBPerTbl15MinIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NncNBPerTbl15MinIntervalNumber_Type.__name__ = "Integer32"
_NncNBPerTbl15MinIntervalNumber_Object = MibTableColumn
nncNBPerTbl15MinIntervalNumber = _NncNBPerTbl15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 10, 1, 2),
    _NncNBPerTbl15MinIntervalNumber_Type()
)
nncNBPerTbl15MinIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncNBPerTbl15MinIntervalNumber.setStatus("current")


class _NncNBPerTbl15MinIntervalTableDescriptor_Type(Integer32):
    """Custom type nncNBPerTbl15MinIntervalTableDescriptor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_NncNBPerTbl15MinIntervalTableDescriptor_Type.__name__ = "Integer32"
_NncNBPerTbl15MinIntervalTableDescriptor_Object = MibTableColumn
nncNBPerTbl15MinIntervalTableDescriptor = _NncNBPerTbl15MinIntervalTableDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 10, 1, 3),
    _NncNBPerTbl15MinIntervalTableDescriptor_Type()
)
nncNBPerTbl15MinIntervalTableDescriptor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncNBPerTbl15MinIntervalTableDescriptor.setStatus("current")
_NncNBPerTbl15MinIntervalState_Type = NncExtIntvlStateType
_NncNBPerTbl15MinIntervalState_Object = MibTableColumn
nncNBPerTbl15MinIntervalState = _NncNBPerTbl15MinIntervalState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 10, 1, 4),
    _NncNBPerTbl15MinIntervalState_Type()
)
nncNBPerTbl15MinIntervalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl15MinIntervalState.setStatus("current")
_NncNBPerTbl15MinIntervalAbsoluteIntervalNumber_Type = Integer32
_NncNBPerTbl15MinIntervalAbsoluteIntervalNumber_Object = MibTableColumn
nncNBPerTbl15MinIntervalAbsoluteIntervalNumber = _NncNBPerTbl15MinIntervalAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 10, 1, 5),
    _NncNBPerTbl15MinIntervalAbsoluteIntervalNumber_Type()
)
nncNBPerTbl15MinIntervalAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl15MinIntervalAbsoluteIntervalNumber.setStatus("current")
_NncNBPerTbl15MinIntervalFailedCallsDueToInitDTLNotGenerated_Type = Counter32
_NncNBPerTbl15MinIntervalFailedCallsDueToInitDTLNotGenerated_Object = MibTableColumn
nncNBPerTbl15MinIntervalFailedCallsDueToInitDTLNotGenerated = _NncNBPerTbl15MinIntervalFailedCallsDueToInitDTLNotGenerated_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 10, 1, 6),
    _NncNBPerTbl15MinIntervalFailedCallsDueToInitDTLNotGenerated_Type()
)
nncNBPerTbl15MinIntervalFailedCallsDueToInitDTLNotGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl15MinIntervalFailedCallsDueToInitDTLNotGenerated.setStatus("current")
_NncNBPerTbl15MinIntervalCallsGeneratingAnInitDTL_Type = Counter32
_NncNBPerTbl15MinIntervalCallsGeneratingAnInitDTL_Object = MibTableColumn
nncNBPerTbl15MinIntervalCallsGeneratingAnInitDTL = _NncNBPerTbl15MinIntervalCallsGeneratingAnInitDTL_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 10, 1, 7),
    _NncNBPerTbl15MinIntervalCallsGeneratingAnInitDTL_Type()
)
nncNBPerTbl15MinIntervalCallsGeneratingAnInitDTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl15MinIntervalCallsGeneratingAnInitDTL.setStatus("current")
_NncNBPerTbl15MinIntervalDTLOrigCallsSuccessEstWithoutReroute_Type = Counter32
_NncNBPerTbl15MinIntervalDTLOrigCallsSuccessEstWithoutReroute_Object = MibTableColumn
nncNBPerTbl15MinIntervalDTLOrigCallsSuccessEstWithoutReroute = _NncNBPerTbl15MinIntervalDTLOrigCallsSuccessEstWithoutReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 10, 1, 8),
    _NncNBPerTbl15MinIntervalDTLOrigCallsSuccessEstWithoutReroute_Type()
)
nncNBPerTbl15MinIntervalDTLOrigCallsSuccessEstWithoutReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl15MinIntervalDTLOrigCallsSuccessEstWithoutReroute.setStatus("current")
_NncNBPerTbl15MinIntervalDTLOrigCallsSuccessEstWithReroute_Type = Counter32
_NncNBPerTbl15MinIntervalDTLOrigCallsSuccessEstWithReroute_Object = MibTableColumn
nncNBPerTbl15MinIntervalDTLOrigCallsSuccessEstWithReroute = _NncNBPerTbl15MinIntervalDTLOrigCallsSuccessEstWithReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 10, 1, 9),
    _NncNBPerTbl15MinIntervalDTLOrigCallsSuccessEstWithReroute_Type()
)
nncNBPerTbl15MinIntervalDTLOrigCallsSuccessEstWithReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl15MinIntervalDTLOrigCallsSuccessEstWithReroute.setStatus("current")
_NncNBPerTbl15MinIntervalDTLOrigCallsFailedInReRouting_Type = Counter32
_NncNBPerTbl15MinIntervalDTLOrigCallsFailedInReRouting_Object = MibTableColumn
nncNBPerTbl15MinIntervalDTLOrigCallsFailedInReRouting = _NncNBPerTbl15MinIntervalDTLOrigCallsFailedInReRouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 10, 1, 10),
    _NncNBPerTbl15MinIntervalDTLOrigCallsFailedInReRouting_Type()
)
nncNBPerTbl15MinIntervalDTLOrigCallsFailedInReRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl15MinIntervalDTLOrigCallsFailedInReRouting.setStatus("current")
_NncNBPerTbl15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncNBPerTbl15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncNBPerTbl15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw = _NncNBPerTbl15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 10, 1, 11),
    _NncNBPerTbl15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Type()
)
nncNBPerTbl15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncNBPerTbl15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncNBPerTbl15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncNBPerTbl15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw = _NncNBPerTbl15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 10, 1, 12),
    _NncNBPerTbl15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw_Type()
)
nncNBPerTbl15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncNBPerTbl15MinIntervalCrankbackReceivedAsDTLOriginator_Type = Counter32
_NncNBPerTbl15MinIntervalCrankbackReceivedAsDTLOriginator_Object = MibTableColumn
nncNBPerTbl15MinIntervalCrankbackReceivedAsDTLOriginator = _NncNBPerTbl15MinIntervalCrankbackReceivedAsDTLOriginator_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 10, 1, 13),
    _NncNBPerTbl15MinIntervalCrankbackReceivedAsDTLOriginator_Type()
)
nncNBPerTbl15MinIntervalCrankbackReceivedAsDTLOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl15MinIntervalCrankbackReceivedAsDTLOriginator.setStatus("current")
_NncNBPerTbl15MinIntervalDTLsGeneratedDueToCrankback_Type = Counter32
_NncNBPerTbl15MinIntervalDTLsGeneratedDueToCrankback_Object = MibTableColumn
nncNBPerTbl15MinIntervalDTLsGeneratedDueToCrankback = _NncNBPerTbl15MinIntervalDTLsGeneratedDueToCrankback_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 10, 1, 14),
    _NncNBPerTbl15MinIntervalDTLsGeneratedDueToCrankback_Type()
)
nncNBPerTbl15MinIntervalDTLsGeneratedDueToCrankback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl15MinIntervalDTLsGeneratedDueToCrankback.setStatus("current")
_NncRoutingStatsNonBorderPerTbl24HourCurrentTable_Object = MibTable
nncRoutingStatsNonBorderPerTbl24HourCurrentTable = _NncRoutingStatsNonBorderPerTbl24HourCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 11)
)
if mibBuilder.loadTexts:
    nncRoutingStatsNonBorderPerTbl24HourCurrentTable.setStatus("current")
_NncRoutingStatsNonBorderPerTbl24HourCurrentEntry_Object = MibTableRow
nncRoutingStatsNonBorderPerTbl24HourCurrentEntry = _NncRoutingStatsNonBorderPerTbl24HourCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 11, 1)
)
nncRoutingStatsNonBorderPerTbl24HourCurrentEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourCurrentTableDescriptor"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsNonBorderPerTbl24HourCurrentEntry.setStatus("current")


class _NncNBPerTbl24HourCurrentTableDescriptor_Type(Integer32):
    """Custom type nncNBPerTbl24HourCurrentTableDescriptor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_NncNBPerTbl24HourCurrentTableDescriptor_Type.__name__ = "Integer32"
_NncNBPerTbl24HourCurrentTableDescriptor_Object = MibTableColumn
nncNBPerTbl24HourCurrentTableDescriptor = _NncNBPerTbl24HourCurrentTableDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 11, 1, 2),
    _NncNBPerTbl24HourCurrentTableDescriptor_Type()
)
nncNBPerTbl24HourCurrentTableDescriptor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourCurrentTableDescriptor.setStatus("current")
_NncNBPerTbl24HourCurrentState_Type = NncExtIntvlStateType
_NncNBPerTbl24HourCurrentState_Object = MibTableColumn
nncNBPerTbl24HourCurrentState = _NncNBPerTbl24HourCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 11, 1, 3),
    _NncNBPerTbl24HourCurrentState_Type()
)
nncNBPerTbl24HourCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourCurrentState.setStatus("current")
_NncNBPerTbl24HourCurrentAbsoluteIntervalNumber_Type = Integer32
_NncNBPerTbl24HourCurrentAbsoluteIntervalNumber_Object = MibTableColumn
nncNBPerTbl24HourCurrentAbsoluteIntervalNumber = _NncNBPerTbl24HourCurrentAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 11, 1, 4),
    _NncNBPerTbl24HourCurrentAbsoluteIntervalNumber_Type()
)
nncNBPerTbl24HourCurrentAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourCurrentAbsoluteIntervalNumber.setStatus("current")
_NncNBPerTbl24HourCurrentFailedCallsDueToInitDTLNotGenerated_Type = Counter32
_NncNBPerTbl24HourCurrentFailedCallsDueToInitDTLNotGenerated_Object = MibTableColumn
nncNBPerTbl24HourCurrentFailedCallsDueToInitDTLNotGenerated = _NncNBPerTbl24HourCurrentFailedCallsDueToInitDTLNotGenerated_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 11, 1, 5),
    _NncNBPerTbl24HourCurrentFailedCallsDueToInitDTLNotGenerated_Type()
)
nncNBPerTbl24HourCurrentFailedCallsDueToInitDTLNotGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourCurrentFailedCallsDueToInitDTLNotGenerated.setStatus("current")
_NncNBPerTbl24HourCurrentCallsGeneratingAnInitDTL_Type = Counter32
_NncNBPerTbl24HourCurrentCallsGeneratingAnInitDTL_Object = MibTableColumn
nncNBPerTbl24HourCurrentCallsGeneratingAnInitDTL = _NncNBPerTbl24HourCurrentCallsGeneratingAnInitDTL_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 11, 1, 6),
    _NncNBPerTbl24HourCurrentCallsGeneratingAnInitDTL_Type()
)
nncNBPerTbl24HourCurrentCallsGeneratingAnInitDTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourCurrentCallsGeneratingAnInitDTL.setStatus("current")
_NncNBPerTbl24HourCurrentDTLOrigCallsSuccessEstWithoutReroute_Type = Counter32
_NncNBPerTbl24HourCurrentDTLOrigCallsSuccessEstWithoutReroute_Object = MibTableColumn
nncNBPerTbl24HourCurrentDTLOrigCallsSuccessEstWithoutReroute = _NncNBPerTbl24HourCurrentDTLOrigCallsSuccessEstWithoutReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 11, 1, 7),
    _NncNBPerTbl24HourCurrentDTLOrigCallsSuccessEstWithoutReroute_Type()
)
nncNBPerTbl24HourCurrentDTLOrigCallsSuccessEstWithoutReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourCurrentDTLOrigCallsSuccessEstWithoutReroute.setStatus("current")
_NncNBPerTbl24HourCurrentDTLOrigCallsSuccessEstWithReroute_Type = Counter32
_NncNBPerTbl24HourCurrentDTLOrigCallsSuccessEstWithReroute_Object = MibTableColumn
nncNBPerTbl24HourCurrentDTLOrigCallsSuccessEstWithReroute = _NncNBPerTbl24HourCurrentDTLOrigCallsSuccessEstWithReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 11, 1, 8),
    _NncNBPerTbl24HourCurrentDTLOrigCallsSuccessEstWithReroute_Type()
)
nncNBPerTbl24HourCurrentDTLOrigCallsSuccessEstWithReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourCurrentDTLOrigCallsSuccessEstWithReroute.setStatus("current")
_NncNBPerTbl24HourCurrentDTLOrigCallsFailedInReRouting_Type = Counter32
_NncNBPerTbl24HourCurrentDTLOrigCallsFailedInReRouting_Object = MibTableColumn
nncNBPerTbl24HourCurrentDTLOrigCallsFailedInReRouting = _NncNBPerTbl24HourCurrentDTLOrigCallsFailedInReRouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 11, 1, 9),
    _NncNBPerTbl24HourCurrentDTLOrigCallsFailedInReRouting_Type()
)
nncNBPerTbl24HourCurrentDTLOrigCallsFailedInReRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourCurrentDTLOrigCallsFailedInReRouting.setStatus("current")
_NncNBPerTbl24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncNBPerTbl24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncNBPerTbl24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw = _NncNBPerTbl24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 11, 1, 10),
    _NncNBPerTbl24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Type()
)
nncNBPerTbl24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncNBPerTbl24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncNBPerTbl24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncNBPerTbl24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw = _NncNBPerTbl24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 11, 1, 11),
    _NncNBPerTbl24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw_Type()
)
nncNBPerTbl24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncNBPerTbl24HourCurrentCrankbackReceivedAsDTLOriginator_Type = Counter32
_NncNBPerTbl24HourCurrentCrankbackReceivedAsDTLOriginator_Object = MibTableColumn
nncNBPerTbl24HourCurrentCrankbackReceivedAsDTLOriginator = _NncNBPerTbl24HourCurrentCrankbackReceivedAsDTLOriginator_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 11, 1, 12),
    _NncNBPerTbl24HourCurrentCrankbackReceivedAsDTLOriginator_Type()
)
nncNBPerTbl24HourCurrentCrankbackReceivedAsDTLOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourCurrentCrankbackReceivedAsDTLOriginator.setStatus("current")
_NncNBPerTbl24HourCurrentDTLsGeneratedDueToCrankback_Type = Counter32
_NncNBPerTbl24HourCurrentDTLsGeneratedDueToCrankback_Object = MibTableColumn
nncNBPerTbl24HourCurrentDTLsGeneratedDueToCrankback = _NncNBPerTbl24HourCurrentDTLsGeneratedDueToCrankback_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 11, 1, 13),
    _NncNBPerTbl24HourCurrentDTLsGeneratedDueToCrankback_Type()
)
nncNBPerTbl24HourCurrentDTLsGeneratedDueToCrankback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourCurrentDTLsGeneratedDueToCrankback.setStatus("current")
_NncRoutingStatsNonBorderPerTbl24HourIntervalTable_Object = MibTable
nncRoutingStatsNonBorderPerTbl24HourIntervalTable = _NncRoutingStatsNonBorderPerTbl24HourIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 12)
)
if mibBuilder.loadTexts:
    nncRoutingStatsNonBorderPerTbl24HourIntervalTable.setStatus("current")
_NncRoutingStatsNonBorderPerTbl24HourIntervalEntry_Object = MibTableRow
nncRoutingStatsNonBorderPerTbl24HourIntervalEntry = _NncRoutingStatsNonBorderPerTbl24HourIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 12, 1)
)
nncRoutingStatsNonBorderPerTbl24HourIntervalEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourIntervalNumber"),
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourIntervalTableDescriptor"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsNonBorderPerTbl24HourIntervalEntry.setStatus("current")
_NncNBPerTbl24HourIntervalNumber_Type = Integer32
_NncNBPerTbl24HourIntervalNumber_Object = MibTableColumn
nncNBPerTbl24HourIntervalNumber = _NncNBPerTbl24HourIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 12, 1, 2),
    _NncNBPerTbl24HourIntervalNumber_Type()
)
nncNBPerTbl24HourIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourIntervalNumber.setStatus("current")


class _NncNBPerTbl24HourIntervalTableDescriptor_Type(Integer32):
    """Custom type nncNBPerTbl24HourIntervalTableDescriptor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_NncNBPerTbl24HourIntervalTableDescriptor_Type.__name__ = "Integer32"
_NncNBPerTbl24HourIntervalTableDescriptor_Object = MibTableColumn
nncNBPerTbl24HourIntervalTableDescriptor = _NncNBPerTbl24HourIntervalTableDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 12, 1, 3),
    _NncNBPerTbl24HourIntervalTableDescriptor_Type()
)
nncNBPerTbl24HourIntervalTableDescriptor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourIntervalTableDescriptor.setStatus("current")
_NncNBPerTbl24HourIntervalState_Type = NncExtIntvlStateType
_NncNBPerTbl24HourIntervalState_Object = MibTableColumn
nncNBPerTbl24HourIntervalState = _NncNBPerTbl24HourIntervalState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 12, 1, 4),
    _NncNBPerTbl24HourIntervalState_Type()
)
nncNBPerTbl24HourIntervalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourIntervalState.setStatus("current")
_NncNBPerTbl24HourIntervalAbsoluteIntervalNumber_Type = Integer32
_NncNBPerTbl24HourIntervalAbsoluteIntervalNumber_Object = MibTableColumn
nncNBPerTbl24HourIntervalAbsoluteIntervalNumber = _NncNBPerTbl24HourIntervalAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 12, 1, 5),
    _NncNBPerTbl24HourIntervalAbsoluteIntervalNumber_Type()
)
nncNBPerTbl24HourIntervalAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourIntervalAbsoluteIntervalNumber.setStatus("current")
_NncNBPerTbl24HourIntervalFailedCallsDueToInitDTLNotGenerated_Type = Counter32
_NncNBPerTbl24HourIntervalFailedCallsDueToInitDTLNotGenerated_Object = MibTableColumn
nncNBPerTbl24HourIntervalFailedCallsDueToInitDTLNotGenerated = _NncNBPerTbl24HourIntervalFailedCallsDueToInitDTLNotGenerated_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 12, 1, 6),
    _NncNBPerTbl24HourIntervalFailedCallsDueToInitDTLNotGenerated_Type()
)
nncNBPerTbl24HourIntervalFailedCallsDueToInitDTLNotGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourIntervalFailedCallsDueToInitDTLNotGenerated.setStatus("current")
_NncNBPerTbl24HourIntervalCallsGeneratingAnInitDTL_Type = Counter32
_NncNBPerTbl24HourIntervalCallsGeneratingAnInitDTL_Object = MibTableColumn
nncNBPerTbl24HourIntervalCallsGeneratingAnInitDTL = _NncNBPerTbl24HourIntervalCallsGeneratingAnInitDTL_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 12, 1, 7),
    _NncNBPerTbl24HourIntervalCallsGeneratingAnInitDTL_Type()
)
nncNBPerTbl24HourIntervalCallsGeneratingAnInitDTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourIntervalCallsGeneratingAnInitDTL.setStatus("current")
_NncNBPerTbl24HourIntervalDTLOrigCallsSuccessEstWithoutReroute_Type = Counter32
_NncNBPerTbl24HourIntervalDTLOrigCallsSuccessEstWithoutReroute_Object = MibTableColumn
nncNBPerTbl24HourIntervalDTLOrigCallsSuccessEstWithoutReroute = _NncNBPerTbl24HourIntervalDTLOrigCallsSuccessEstWithoutReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 12, 1, 8),
    _NncNBPerTbl24HourIntervalDTLOrigCallsSuccessEstWithoutReroute_Type()
)
nncNBPerTbl24HourIntervalDTLOrigCallsSuccessEstWithoutReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourIntervalDTLOrigCallsSuccessEstWithoutReroute.setStatus("current")
_NncNBPerTbl24HourIntervalDTLOrigCallsSuccessEstWithReroute_Type = Counter32
_NncNBPerTbl24HourIntervalDTLOrigCallsSuccessEstWithReroute_Object = MibTableColumn
nncNBPerTbl24HourIntervalDTLOrigCallsSuccessEstWithReroute = _NncNBPerTbl24HourIntervalDTLOrigCallsSuccessEstWithReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 12, 1, 9),
    _NncNBPerTbl24HourIntervalDTLOrigCallsSuccessEstWithReroute_Type()
)
nncNBPerTbl24HourIntervalDTLOrigCallsSuccessEstWithReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourIntervalDTLOrigCallsSuccessEstWithReroute.setStatus("current")
_NncNBPerTbl24HourIntervalDTLOrigCallsFailedInReRouting_Type = Counter32
_NncNBPerTbl24HourIntervalDTLOrigCallsFailedInReRouting_Object = MibTableColumn
nncNBPerTbl24HourIntervalDTLOrigCallsFailedInReRouting = _NncNBPerTbl24HourIntervalDTLOrigCallsFailedInReRouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 12, 1, 10),
    _NncNBPerTbl24HourIntervalDTLOrigCallsFailedInReRouting_Type()
)
nncNBPerTbl24HourIntervalDTLOrigCallsFailedInReRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourIntervalDTLOrigCallsFailedInReRouting.setStatus("current")
_NncNBPerTbl24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncNBPerTbl24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncNBPerTbl24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw = _NncNBPerTbl24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 12, 1, 11),
    _NncNBPerTbl24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Type()
)
nncNBPerTbl24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncNBPerTbl24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncNBPerTbl24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncNBPerTbl24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw = _NncNBPerTbl24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 12, 1, 12),
    _NncNBPerTbl24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw_Type()
)
nncNBPerTbl24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncNBPerTbl24HourIntervalCrankbackReceivedAsDTLOriginator_Type = Counter32
_NncNBPerTbl24HourIntervalCrankbackReceivedAsDTLOriginator_Object = MibTableColumn
nncNBPerTbl24HourIntervalCrankbackReceivedAsDTLOriginator = _NncNBPerTbl24HourIntervalCrankbackReceivedAsDTLOriginator_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 12, 1, 13),
    _NncNBPerTbl24HourIntervalCrankbackReceivedAsDTLOriginator_Type()
)
nncNBPerTbl24HourIntervalCrankbackReceivedAsDTLOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourIntervalCrankbackReceivedAsDTLOriginator.setStatus("current")
_NncNBPerTbl24HourIntervalDTLsGeneratedDueToCrankback_Type = Counter32
_NncNBPerTbl24HourIntervalDTLsGeneratedDueToCrankback_Object = MibTableColumn
nncNBPerTbl24HourIntervalDTLsGeneratedDueToCrankback = _NncNBPerTbl24HourIntervalDTLsGeneratedDueToCrankback_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 12, 1, 14),
    _NncNBPerTbl24HourIntervalDTLsGeneratedDueToCrankback_Type()
)
nncNBPerTbl24HourIntervalDTLsGeneratedDueToCrankback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBPerTbl24HourIntervalDTLsGeneratedDueToCrankback.setStatus("current")
_NncRoutingStatsBorderPerTbl15MinCurrentTable_Object = MibTable
nncRoutingStatsBorderPerTbl15MinCurrentTable = _NncRoutingStatsBorderPerTbl15MinCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 13)
)
if mibBuilder.loadTexts:
    nncRoutingStatsBorderPerTbl15MinCurrentTable.setStatus("current")
_NncRoutingStatsBorderPerTbl15MinCurrentEntry_Object = MibTableRow
nncRoutingStatsBorderPerTbl15MinCurrentEntry = _NncRoutingStatsBorderPerTbl15MinCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 13, 1)
)
nncRoutingStatsBorderPerTbl15MinCurrentEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinCurrentTableDescriptor"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsBorderPerTbl15MinCurrentEntry.setStatus("current")


class _NncBPerTbl15MinCurrentTableDescriptor_Type(Integer32):
    """Custom type nncBPerTbl15MinCurrentTableDescriptor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_NncBPerTbl15MinCurrentTableDescriptor_Type.__name__ = "Integer32"
_NncBPerTbl15MinCurrentTableDescriptor_Object = MibTableColumn
nncBPerTbl15MinCurrentTableDescriptor = _NncBPerTbl15MinCurrentTableDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 13, 1, 2),
    _NncBPerTbl15MinCurrentTableDescriptor_Type()
)
nncBPerTbl15MinCurrentTableDescriptor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncBPerTbl15MinCurrentTableDescriptor.setStatus("current")
_NncBPerTbl15MinCurrentState_Type = NncExtIntvlStateType
_NncBPerTbl15MinCurrentState_Object = MibTableColumn
nncBPerTbl15MinCurrentState = _NncBPerTbl15MinCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 13, 1, 3),
    _NncBPerTbl15MinCurrentState_Type()
)
nncBPerTbl15MinCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl15MinCurrentState.setStatus("current")
_NncBPerTbl15MinCurrentAbsoluteIntervalNumber_Type = Integer32
_NncBPerTbl15MinCurrentAbsoluteIntervalNumber_Object = MibTableColumn
nncBPerTbl15MinCurrentAbsoluteIntervalNumber = _NncBPerTbl15MinCurrentAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 13, 1, 4),
    _NncBPerTbl15MinCurrentAbsoluteIntervalNumber_Type()
)
nncBPerTbl15MinCurrentAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl15MinCurrentAbsoluteIntervalNumber.setStatus("current")
_NncBPerTbl15MinCurrentFailedCallsDueInitLowerLvlDTLsNotGen_Type = Counter32
_NncBPerTbl15MinCurrentFailedCallsDueInitLowerLvlDTLsNotGen_Object = MibTableColumn
nncBPerTbl15MinCurrentFailedCallsDueInitLowerLvlDTLsNotGen = _NncBPerTbl15MinCurrentFailedCallsDueInitLowerLvlDTLsNotGen_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 13, 1, 5),
    _NncBPerTbl15MinCurrentFailedCallsDueInitLowerLvlDTLsNotGen_Type()
)
nncBPerTbl15MinCurrentFailedCallsDueInitLowerLvlDTLsNotGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl15MinCurrentFailedCallsDueInitLowerLvlDTLsNotGen.setStatus("current")
_NncBPerTbl15MinCurrentCallsGeneratingInitLowerLvlDTLs_Type = Counter32
_NncBPerTbl15MinCurrentCallsGeneratingInitLowerLvlDTLs_Object = MibTableColumn
nncBPerTbl15MinCurrentCallsGeneratingInitLowerLvlDTLs = _NncBPerTbl15MinCurrentCallsGeneratingInitLowerLvlDTLs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 13, 1, 6),
    _NncBPerTbl15MinCurrentCallsGeneratingInitLowerLvlDTLs_Type()
)
nncBPerTbl15MinCurrentCallsGeneratingInitLowerLvlDTLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl15MinCurrentCallsGeneratingInitLowerLvlDTLs.setStatus("current")
_NncBPerTbl15MinCurrentDTLGenCallsSuccessEstWithoutReroute_Type = Counter32
_NncBPerTbl15MinCurrentDTLGenCallsSuccessEstWithoutReroute_Object = MibTableColumn
nncBPerTbl15MinCurrentDTLGenCallsSuccessEstWithoutReroute = _NncBPerTbl15MinCurrentDTLGenCallsSuccessEstWithoutReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 13, 1, 7),
    _NncBPerTbl15MinCurrentDTLGenCallsSuccessEstWithoutReroute_Type()
)
nncBPerTbl15MinCurrentDTLGenCallsSuccessEstWithoutReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl15MinCurrentDTLGenCallsSuccessEstWithoutReroute.setStatus("current")
_NncBPerTbl15MinCurrentDTLGenCallsSuccessEstWithReroute_Type = Counter32
_NncBPerTbl15MinCurrentDTLGenCallsSuccessEstWithReroute_Object = MibTableColumn
nncBPerTbl15MinCurrentDTLGenCallsSuccessEstWithReroute = _NncBPerTbl15MinCurrentDTLGenCallsSuccessEstWithReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 13, 1, 8),
    _NncBPerTbl15MinCurrentDTLGenCallsSuccessEstWithReroute_Type()
)
nncBPerTbl15MinCurrentDTLGenCallsSuccessEstWithReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl15MinCurrentDTLGenCallsSuccessEstWithReroute.setStatus("current")
_NncBPerTbl15MinCurrentDTLGenCallsFailedInReRouting_Type = Counter32
_NncBPerTbl15MinCurrentDTLGenCallsFailedInReRouting_Object = MibTableColumn
nncBPerTbl15MinCurrentDTLGenCallsFailedInReRouting = _NncBPerTbl15MinCurrentDTLGenCallsFailedInReRouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 13, 1, 9),
    _NncBPerTbl15MinCurrentDTLGenCallsFailedInReRouting_Type()
)
nncBPerTbl15MinCurrentDTLGenCallsFailedInReRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl15MinCurrentDTLGenCallsFailedInReRouting.setStatus("current")
_NncBPerTbl15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncBPerTbl15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncBPerTbl15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw = _NncBPerTbl15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 13, 1, 10),
    _NncBPerTbl15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Type()
)
nncBPerTbl15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncBPerTbl15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncBPerTbl15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncBPerTbl15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw = _NncBPerTbl15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 13, 1, 11),
    _NncBPerTbl15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw_Type()
)
nncBPerTbl15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncBPerTbl15MinCurrentCrankbackReceivedAsAnEntryBorderNode_Type = Counter32
_NncBPerTbl15MinCurrentCrankbackReceivedAsAnEntryBorderNode_Object = MibTableColumn
nncBPerTbl15MinCurrentCrankbackReceivedAsAnEntryBorderNode = _NncBPerTbl15MinCurrentCrankbackReceivedAsAnEntryBorderNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 13, 1, 12),
    _NncBPerTbl15MinCurrentCrankbackReceivedAsAnEntryBorderNode_Type()
)
nncBPerTbl15MinCurrentCrankbackReceivedAsAnEntryBorderNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl15MinCurrentCrankbackReceivedAsAnEntryBorderNode.setStatus("current")
_NncBPerTbl15MinCurrentLowerLvlDTLsGenDueToRecdCrankback_Type = Counter32
_NncBPerTbl15MinCurrentLowerLvlDTLsGenDueToRecdCrankback_Object = MibTableColumn
nncBPerTbl15MinCurrentLowerLvlDTLsGenDueToRecdCrankback = _NncBPerTbl15MinCurrentLowerLvlDTLsGenDueToRecdCrankback_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 13, 1, 13),
    _NncBPerTbl15MinCurrentLowerLvlDTLsGenDueToRecdCrankback_Type()
)
nncBPerTbl15MinCurrentLowerLvlDTLsGenDueToRecdCrankback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl15MinCurrentLowerLvlDTLsGenDueToRecdCrankback.setStatus("current")
_NncRoutingStatsBorderPerTbl15MinIntervalTable_Object = MibTable
nncRoutingStatsBorderPerTbl15MinIntervalTable = _NncRoutingStatsBorderPerTbl15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 14)
)
if mibBuilder.loadTexts:
    nncRoutingStatsBorderPerTbl15MinIntervalTable.setStatus("current")
_NncRoutingStatsBorderPerTbl15MinIntervalEntry_Object = MibTableRow
nncRoutingStatsBorderPerTbl15MinIntervalEntry = _NncRoutingStatsBorderPerTbl15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 14, 1)
)
nncRoutingStatsBorderPerTbl15MinIntervalEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinIntervalNumber"),
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinIntervalTableDescriptor"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsBorderPerTbl15MinIntervalEntry.setStatus("current")


class _NncBPerTbl15MinIntervalNumber_Type(Integer32):
    """Custom type nncBPerTbl15MinIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NncBPerTbl15MinIntervalNumber_Type.__name__ = "Integer32"
_NncBPerTbl15MinIntervalNumber_Object = MibTableColumn
nncBPerTbl15MinIntervalNumber = _NncBPerTbl15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 14, 1, 2),
    _NncBPerTbl15MinIntervalNumber_Type()
)
nncBPerTbl15MinIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncBPerTbl15MinIntervalNumber.setStatus("current")


class _NncBPerTbl15MinIntervalTableDescriptor_Type(Integer32):
    """Custom type nncBPerTbl15MinIntervalTableDescriptor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_NncBPerTbl15MinIntervalTableDescriptor_Type.__name__ = "Integer32"
_NncBPerTbl15MinIntervalTableDescriptor_Object = MibTableColumn
nncBPerTbl15MinIntervalTableDescriptor = _NncBPerTbl15MinIntervalTableDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 14, 1, 3),
    _NncBPerTbl15MinIntervalTableDescriptor_Type()
)
nncBPerTbl15MinIntervalTableDescriptor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncBPerTbl15MinIntervalTableDescriptor.setStatus("current")
_NncBPerTbl15MinIntervalState_Type = NncExtIntvlStateType
_NncBPerTbl15MinIntervalState_Object = MibTableColumn
nncBPerTbl15MinIntervalState = _NncBPerTbl15MinIntervalState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 14, 1, 4),
    _NncBPerTbl15MinIntervalState_Type()
)
nncBPerTbl15MinIntervalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl15MinIntervalState.setStatus("current")
_NncBPerTbl15MinIntervalAbsoluteIntervalNumber_Type = Integer32
_NncBPerTbl15MinIntervalAbsoluteIntervalNumber_Object = MibTableColumn
nncBPerTbl15MinIntervalAbsoluteIntervalNumber = _NncBPerTbl15MinIntervalAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 14, 1, 5),
    _NncBPerTbl15MinIntervalAbsoluteIntervalNumber_Type()
)
nncBPerTbl15MinIntervalAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl15MinIntervalAbsoluteIntervalNumber.setStatus("current")
_NncBPerTbl15MinIntervalFailedCallsDueInitLowerLvlDTLsNotGen_Type = Counter32
_NncBPerTbl15MinIntervalFailedCallsDueInitLowerLvlDTLsNotGen_Object = MibTableColumn
nncBPerTbl15MinIntervalFailedCallsDueInitLowerLvlDTLsNotGen = _NncBPerTbl15MinIntervalFailedCallsDueInitLowerLvlDTLsNotGen_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 14, 1, 6),
    _NncBPerTbl15MinIntervalFailedCallsDueInitLowerLvlDTLsNotGen_Type()
)
nncBPerTbl15MinIntervalFailedCallsDueInitLowerLvlDTLsNotGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl15MinIntervalFailedCallsDueInitLowerLvlDTLsNotGen.setStatus("current")
_NncBPerTbl15MinIntervalCallsGeneratingInitLowerLvlDTLs_Type = Counter32
_NncBPerTbl15MinIntervalCallsGeneratingInitLowerLvlDTLs_Object = MibTableColumn
nncBPerTbl15MinIntervalCallsGeneratingInitLowerLvlDTLs = _NncBPerTbl15MinIntervalCallsGeneratingInitLowerLvlDTLs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 14, 1, 7),
    _NncBPerTbl15MinIntervalCallsGeneratingInitLowerLvlDTLs_Type()
)
nncBPerTbl15MinIntervalCallsGeneratingInitLowerLvlDTLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl15MinIntervalCallsGeneratingInitLowerLvlDTLs.setStatus("current")
_NncBPerTbl15MinIntervalDTLGenCallsSuccessEstWithoutReroute_Type = Counter32
_NncBPerTbl15MinIntervalDTLGenCallsSuccessEstWithoutReroute_Object = MibTableColumn
nncBPerTbl15MinIntervalDTLGenCallsSuccessEstWithoutReroute = _NncBPerTbl15MinIntervalDTLGenCallsSuccessEstWithoutReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 14, 1, 8),
    _NncBPerTbl15MinIntervalDTLGenCallsSuccessEstWithoutReroute_Type()
)
nncBPerTbl15MinIntervalDTLGenCallsSuccessEstWithoutReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl15MinIntervalDTLGenCallsSuccessEstWithoutReroute.setStatus("current")
_NncBPerTbl15MinIntervalDTLGenCallsSuccessEstWithReroute_Type = Counter32
_NncBPerTbl15MinIntervalDTLGenCallsSuccessEstWithReroute_Object = MibTableColumn
nncBPerTbl15MinIntervalDTLGenCallsSuccessEstWithReroute = _NncBPerTbl15MinIntervalDTLGenCallsSuccessEstWithReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 14, 1, 9),
    _NncBPerTbl15MinIntervalDTLGenCallsSuccessEstWithReroute_Type()
)
nncBPerTbl15MinIntervalDTLGenCallsSuccessEstWithReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl15MinIntervalDTLGenCallsSuccessEstWithReroute.setStatus("current")
_NncBPerTbl15MinIntervalDTLGenCallsFailedInReRouting_Type = Counter32
_NncBPerTbl15MinIntervalDTLGenCallsFailedInReRouting_Object = MibTableColumn
nncBPerTbl15MinIntervalDTLGenCallsFailedInReRouting = _NncBPerTbl15MinIntervalDTLGenCallsFailedInReRouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 14, 1, 10),
    _NncBPerTbl15MinIntervalDTLGenCallsFailedInReRouting_Type()
)
nncBPerTbl15MinIntervalDTLGenCallsFailedInReRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl15MinIntervalDTLGenCallsFailedInReRouting.setStatus("current")
_NncBPerTbl15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncBPerTbl15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncBPerTbl15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw = _NncBPerTbl15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 14, 1, 11),
    _NncBPerTbl15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Type()
)
nncBPerTbl15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncBPerTbl15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncBPerTbl15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncBPerTbl15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw = _NncBPerTbl15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 14, 1, 12),
    _NncBPerTbl15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw_Type()
)
nncBPerTbl15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncBPerTbl15MinIntervalCrankbackReceivedAsAnEntryBorderNode_Type = Counter32
_NncBPerTbl15MinIntervalCrankbackReceivedAsAnEntryBorderNode_Object = MibTableColumn
nncBPerTbl15MinIntervalCrankbackReceivedAsAnEntryBorderNode = _NncBPerTbl15MinIntervalCrankbackReceivedAsAnEntryBorderNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 14, 1, 13),
    _NncBPerTbl15MinIntervalCrankbackReceivedAsAnEntryBorderNode_Type()
)
nncBPerTbl15MinIntervalCrankbackReceivedAsAnEntryBorderNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl15MinIntervalCrankbackReceivedAsAnEntryBorderNode.setStatus("current")
_NncBPerTbl15MinIntervalLowerLvlDTLsGenDueToRecdCrankback_Type = Counter32
_NncBPerTbl15MinIntervalLowerLvlDTLsGenDueToRecdCrankback_Object = MibTableColumn
nncBPerTbl15MinIntervalLowerLvlDTLsGenDueToRecdCrankback = _NncBPerTbl15MinIntervalLowerLvlDTLsGenDueToRecdCrankback_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 14, 1, 14),
    _NncBPerTbl15MinIntervalLowerLvlDTLsGenDueToRecdCrankback_Type()
)
nncBPerTbl15MinIntervalLowerLvlDTLsGenDueToRecdCrankback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl15MinIntervalLowerLvlDTLsGenDueToRecdCrankback.setStatus("current")
_NncRoutingStatsBorderPerTbl24HourCurrentTable_Object = MibTable
nncRoutingStatsBorderPerTbl24HourCurrentTable = _NncRoutingStatsBorderPerTbl24HourCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 15)
)
if mibBuilder.loadTexts:
    nncRoutingStatsBorderPerTbl24HourCurrentTable.setStatus("current")
_NncRoutingStatsBorderPerTbl24HourCurrentEntry_Object = MibTableRow
nncRoutingStatsBorderPerTbl24HourCurrentEntry = _NncRoutingStatsBorderPerTbl24HourCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 15, 1)
)
nncRoutingStatsBorderPerTbl24HourCurrentEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourCurrentTableDescriptor"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsBorderPerTbl24HourCurrentEntry.setStatus("current")


class _NncBPerTbl24HourCurrentTableDescriptor_Type(Integer32):
    """Custom type nncBPerTbl24HourCurrentTableDescriptor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_NncBPerTbl24HourCurrentTableDescriptor_Type.__name__ = "Integer32"
_NncBPerTbl24HourCurrentTableDescriptor_Object = MibTableColumn
nncBPerTbl24HourCurrentTableDescriptor = _NncBPerTbl24HourCurrentTableDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 15, 1, 2),
    _NncBPerTbl24HourCurrentTableDescriptor_Type()
)
nncBPerTbl24HourCurrentTableDescriptor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncBPerTbl24HourCurrentTableDescriptor.setStatus("current")
_NncBPerTbl24HourCurrentState_Type = NncExtIntvlStateType
_NncBPerTbl24HourCurrentState_Object = MibTableColumn
nncBPerTbl24HourCurrentState = _NncBPerTbl24HourCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 15, 1, 3),
    _NncBPerTbl24HourCurrentState_Type()
)
nncBPerTbl24HourCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl24HourCurrentState.setStatus("current")
_NncBPerTbl24HourCurrentAbsoluteIntervalNumber_Type = Integer32
_NncBPerTbl24HourCurrentAbsoluteIntervalNumber_Object = MibTableColumn
nncBPerTbl24HourCurrentAbsoluteIntervalNumber = _NncBPerTbl24HourCurrentAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 15, 1, 4),
    _NncBPerTbl24HourCurrentAbsoluteIntervalNumber_Type()
)
nncBPerTbl24HourCurrentAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl24HourCurrentAbsoluteIntervalNumber.setStatus("current")
_NncBPerTbl24HourCurrentFailedCallsDueInitLowerLvlDTLsNotGen_Type = Counter32
_NncBPerTbl24HourCurrentFailedCallsDueInitLowerLvlDTLsNotGen_Object = MibTableColumn
nncBPerTbl24HourCurrentFailedCallsDueInitLowerLvlDTLsNotGen = _NncBPerTbl24HourCurrentFailedCallsDueInitLowerLvlDTLsNotGen_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 15, 1, 5),
    _NncBPerTbl24HourCurrentFailedCallsDueInitLowerLvlDTLsNotGen_Type()
)
nncBPerTbl24HourCurrentFailedCallsDueInitLowerLvlDTLsNotGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl24HourCurrentFailedCallsDueInitLowerLvlDTLsNotGen.setStatus("current")
_NncBPerTbl24HourCurrentCallsGeneratingInitLowerLvlDTLs_Type = Counter32
_NncBPerTbl24HourCurrentCallsGeneratingInitLowerLvlDTLs_Object = MibTableColumn
nncBPerTbl24HourCurrentCallsGeneratingInitLowerLvlDTLs = _NncBPerTbl24HourCurrentCallsGeneratingInitLowerLvlDTLs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 15, 1, 6),
    _NncBPerTbl24HourCurrentCallsGeneratingInitLowerLvlDTLs_Type()
)
nncBPerTbl24HourCurrentCallsGeneratingInitLowerLvlDTLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl24HourCurrentCallsGeneratingInitLowerLvlDTLs.setStatus("current")
_NncBPerTbl24HourCurrentDTLGenCallsSuccessEstWithoutReroute_Type = Counter32
_NncBPerTbl24HourCurrentDTLGenCallsSuccessEstWithoutReroute_Object = MibTableColumn
nncBPerTbl24HourCurrentDTLGenCallsSuccessEstWithoutReroute = _NncBPerTbl24HourCurrentDTLGenCallsSuccessEstWithoutReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 15, 1, 7),
    _NncBPerTbl24HourCurrentDTLGenCallsSuccessEstWithoutReroute_Type()
)
nncBPerTbl24HourCurrentDTLGenCallsSuccessEstWithoutReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl24HourCurrentDTLGenCallsSuccessEstWithoutReroute.setStatus("current")
_NncBPerTbl24HourCurrentDTLGenCallsSuccessEstWithReroute_Type = Counter32
_NncBPerTbl24HourCurrentDTLGenCallsSuccessEstWithReroute_Object = MibTableColumn
nncBPerTbl24HourCurrentDTLGenCallsSuccessEstWithReroute = _NncBPerTbl24HourCurrentDTLGenCallsSuccessEstWithReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 15, 1, 8),
    _NncBPerTbl24HourCurrentDTLGenCallsSuccessEstWithReroute_Type()
)
nncBPerTbl24HourCurrentDTLGenCallsSuccessEstWithReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl24HourCurrentDTLGenCallsSuccessEstWithReroute.setStatus("current")
_NncBPerTbl24HourCurrentDTLGenCallsFailedInReRouting_Type = Counter32
_NncBPerTbl24HourCurrentDTLGenCallsFailedInReRouting_Object = MibTableColumn
nncBPerTbl24HourCurrentDTLGenCallsFailedInReRouting = _NncBPerTbl24HourCurrentDTLGenCallsFailedInReRouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 15, 1, 9),
    _NncBPerTbl24HourCurrentDTLGenCallsFailedInReRouting_Type()
)
nncBPerTbl24HourCurrentDTLGenCallsFailedInReRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl24HourCurrentDTLGenCallsFailedInReRouting.setStatus("current")
_NncBPerTbl24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncBPerTbl24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncBPerTbl24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw = _NncBPerTbl24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 15, 1, 10),
    _NncBPerTbl24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Type()
)
nncBPerTbl24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncBPerTbl24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncBPerTbl24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncBPerTbl24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw = _NncBPerTbl24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 15, 1, 11),
    _NncBPerTbl24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw_Type()
)
nncBPerTbl24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncBPerTbl24HourCurrentCrankbackReceivedAsAnEntryBorderNode_Type = Counter32
_NncBPerTbl24HourCurrentCrankbackReceivedAsAnEntryBorderNode_Object = MibTableColumn
nncBPerTbl24HourCurrentCrankbackReceivedAsAnEntryBorderNode = _NncBPerTbl24HourCurrentCrankbackReceivedAsAnEntryBorderNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 15, 1, 12),
    _NncBPerTbl24HourCurrentCrankbackReceivedAsAnEntryBorderNode_Type()
)
nncBPerTbl24HourCurrentCrankbackReceivedAsAnEntryBorderNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl24HourCurrentCrankbackReceivedAsAnEntryBorderNode.setStatus("current")
_NncBPerTbl24HourCurrentLowerLvlDTLsGenDueToRecdCrankback_Type = Counter32
_NncBPerTbl24HourCurrentLowerLvlDTLsGenDueToRecdCrankback_Object = MibTableColumn
nncBPerTbl24HourCurrentLowerLvlDTLsGenDueToRecdCrankback = _NncBPerTbl24HourCurrentLowerLvlDTLsGenDueToRecdCrankback_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 15, 1, 13),
    _NncBPerTbl24HourCurrentLowerLvlDTLsGenDueToRecdCrankback_Type()
)
nncBPerTbl24HourCurrentLowerLvlDTLsGenDueToRecdCrankback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl24HourCurrentLowerLvlDTLsGenDueToRecdCrankback.setStatus("current")
_NncRoutingStatsBorderPerTbl24HourIntervalTable_Object = MibTable
nncRoutingStatsBorderPerTbl24HourIntervalTable = _NncRoutingStatsBorderPerTbl24HourIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 16)
)
if mibBuilder.loadTexts:
    nncRoutingStatsBorderPerTbl24HourIntervalTable.setStatus("current")
_NncRoutingStatsBorderPerTbl24HourIntervalEntry_Object = MibTableRow
nncRoutingStatsBorderPerTbl24HourIntervalEntry = _NncRoutingStatsBorderPerTbl24HourIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 16, 1)
)
nncRoutingStatsBorderPerTbl24HourIntervalEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourIntervalNumber"),
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourIntervalTableDescriptor"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsBorderPerTbl24HourIntervalEntry.setStatus("current")
_NncBPerTbl24HourIntervalNumber_Type = Integer32
_NncBPerTbl24HourIntervalNumber_Object = MibTableColumn
nncBPerTbl24HourIntervalNumber = _NncBPerTbl24HourIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 16, 1, 2),
    _NncBPerTbl24HourIntervalNumber_Type()
)
nncBPerTbl24HourIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncBPerTbl24HourIntervalNumber.setStatus("current")


class _NncBPerTbl24HourIntervalTableDescriptor_Type(Integer32):
    """Custom type nncBPerTbl24HourIntervalTableDescriptor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_NncBPerTbl24HourIntervalTableDescriptor_Type.__name__ = "Integer32"
_NncBPerTbl24HourIntervalTableDescriptor_Object = MibTableColumn
nncBPerTbl24HourIntervalTableDescriptor = _NncBPerTbl24HourIntervalTableDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 16, 1, 3),
    _NncBPerTbl24HourIntervalTableDescriptor_Type()
)
nncBPerTbl24HourIntervalTableDescriptor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncBPerTbl24HourIntervalTableDescriptor.setStatus("current")
_NncBPerTbl24HourIntervalState_Type = NncExtIntvlStateType
_NncBPerTbl24HourIntervalState_Object = MibTableColumn
nncBPerTbl24HourIntervalState = _NncBPerTbl24HourIntervalState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 16, 1, 4),
    _NncBPerTbl24HourIntervalState_Type()
)
nncBPerTbl24HourIntervalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl24HourIntervalState.setStatus("current")
_NncBPerTbl24HourIntervalAbsoluteIntervalNumber_Type = Integer32
_NncBPerTbl24HourIntervalAbsoluteIntervalNumber_Object = MibTableColumn
nncBPerTbl24HourIntervalAbsoluteIntervalNumber = _NncBPerTbl24HourIntervalAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 16, 1, 5),
    _NncBPerTbl24HourIntervalAbsoluteIntervalNumber_Type()
)
nncBPerTbl24HourIntervalAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl24HourIntervalAbsoluteIntervalNumber.setStatus("current")
_NncBPerTbl24HourIntervalFailedCallsDueInitLowerLvlDTLsNotGen_Type = Counter32
_NncBPerTbl24HourIntervalFailedCallsDueInitLowerLvlDTLsNotGen_Object = MibTableColumn
nncBPerTbl24HourIntervalFailedCallsDueInitLowerLvlDTLsNotGen = _NncBPerTbl24HourIntervalFailedCallsDueInitLowerLvlDTLsNotGen_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 16, 1, 6),
    _NncBPerTbl24HourIntervalFailedCallsDueInitLowerLvlDTLsNotGen_Type()
)
nncBPerTbl24HourIntervalFailedCallsDueInitLowerLvlDTLsNotGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl24HourIntervalFailedCallsDueInitLowerLvlDTLsNotGen.setStatus("current")
_NncBPerTbl24HourIntervalCallsGeneratingInitLowerLvlDTLs_Type = Counter32
_NncBPerTbl24HourIntervalCallsGeneratingInitLowerLvlDTLs_Object = MibTableColumn
nncBPerTbl24HourIntervalCallsGeneratingInitLowerLvlDTLs = _NncBPerTbl24HourIntervalCallsGeneratingInitLowerLvlDTLs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 16, 1, 7),
    _NncBPerTbl24HourIntervalCallsGeneratingInitLowerLvlDTLs_Type()
)
nncBPerTbl24HourIntervalCallsGeneratingInitLowerLvlDTLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl24HourIntervalCallsGeneratingInitLowerLvlDTLs.setStatus("current")
_NncBPerTbl24HourIntervalDTLGenCallsSuccessEstWithoutReroute_Type = Counter32
_NncBPerTbl24HourIntervalDTLGenCallsSuccessEstWithoutReroute_Object = MibTableColumn
nncBPerTbl24HourIntervalDTLGenCallsSuccessEstWithoutReroute = _NncBPerTbl24HourIntervalDTLGenCallsSuccessEstWithoutReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 16, 1, 8),
    _NncBPerTbl24HourIntervalDTLGenCallsSuccessEstWithoutReroute_Type()
)
nncBPerTbl24HourIntervalDTLGenCallsSuccessEstWithoutReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl24HourIntervalDTLGenCallsSuccessEstWithoutReroute.setStatus("current")
_NncBPerTbl24HourIntervalDTLGenCallsSuccessEstWithReroute_Type = Counter32
_NncBPerTbl24HourIntervalDTLGenCallsSuccessEstWithReroute_Object = MibTableColumn
nncBPerTbl24HourIntervalDTLGenCallsSuccessEstWithReroute = _NncBPerTbl24HourIntervalDTLGenCallsSuccessEstWithReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 16, 1, 9),
    _NncBPerTbl24HourIntervalDTLGenCallsSuccessEstWithReroute_Type()
)
nncBPerTbl24HourIntervalDTLGenCallsSuccessEstWithReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl24HourIntervalDTLGenCallsSuccessEstWithReroute.setStatus("current")
_NncBPerTbl24HourIntervalDTLGenCallsFailedInReRouting_Type = Counter32
_NncBPerTbl24HourIntervalDTLGenCallsFailedInReRouting_Object = MibTableColumn
nncBPerTbl24HourIntervalDTLGenCallsFailedInReRouting = _NncBPerTbl24HourIntervalDTLGenCallsFailedInReRouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 16, 1, 10),
    _NncBPerTbl24HourIntervalDTLGenCallsFailedInReRouting_Type()
)
nncBPerTbl24HourIntervalDTLGenCallsFailedInReRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl24HourIntervalDTLGenCallsFailedInReRouting.setStatus("current")
_NncBPerTbl24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncBPerTbl24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncBPerTbl24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw = _NncBPerTbl24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 16, 1, 11),
    _NncBPerTbl24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Type()
)
nncBPerTbl24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncBPerTbl24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncBPerTbl24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncBPerTbl24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw = _NncBPerTbl24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 16, 1, 12),
    _NncBPerTbl24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw_Type()
)
nncBPerTbl24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncBPerTbl24HourIntervalCrankbackReceivedAsAnEntryBorderNode_Type = Counter32
_NncBPerTbl24HourIntervalCrankbackReceivedAsAnEntryBorderNode_Object = MibTableColumn
nncBPerTbl24HourIntervalCrankbackReceivedAsAnEntryBorderNode = _NncBPerTbl24HourIntervalCrankbackReceivedAsAnEntryBorderNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 16, 1, 13),
    _NncBPerTbl24HourIntervalCrankbackReceivedAsAnEntryBorderNode_Type()
)
nncBPerTbl24HourIntervalCrankbackReceivedAsAnEntryBorderNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl24HourIntervalCrankbackReceivedAsAnEntryBorderNode.setStatus("current")
_NncBPerTbl24HourIntervalLowerLvlDTLsGenDueToRecdCrankback_Type = Counter32
_NncBPerTbl24HourIntervalLowerLvlDTLsGenDueToRecdCrankback_Object = MibTableColumn
nncBPerTbl24HourIntervalLowerLvlDTLsGenDueToRecdCrankback = _NncBPerTbl24HourIntervalLowerLvlDTLsGenDueToRecdCrankback_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 16, 1, 14),
    _NncBPerTbl24HourIntervalLowerLvlDTLsGenDueToRecdCrankback_Type()
)
nncBPerTbl24HourIntervalLowerLvlDTLsGenDueToRecdCrankback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBPerTbl24HourIntervalLowerLvlDTLsGenDueToRecdCrankback.setStatus("current")
_NncRoutingStatsNonBorderTotal15MinCurrentTable_Object = MibTable
nncRoutingStatsNonBorderTotal15MinCurrentTable = _NncRoutingStatsNonBorderTotal15MinCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 17)
)
if mibBuilder.loadTexts:
    nncRoutingStatsNonBorderTotal15MinCurrentTable.setStatus("current")
_NncRoutingStatsNonBorderTotal15MinCurrentEntry_Object = MibTableRow
nncRoutingStatsNonBorderTotal15MinCurrentEntry = _NncRoutingStatsNonBorderTotal15MinCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 17, 1)
)
nncRoutingStatsNonBorderTotal15MinCurrentEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsNonBorderTotal15MinCurrentEntry.setStatus("current")
_NncNBTotal15MinCurrentState_Type = NncExtIntvlStateType
_NncNBTotal15MinCurrentState_Object = MibTableColumn
nncNBTotal15MinCurrentState = _NncNBTotal15MinCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 17, 1, 2),
    _NncNBTotal15MinCurrentState_Type()
)
nncNBTotal15MinCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinCurrentState.setStatus("current")
_NncNBTotal15MinCurrentAbsoluteIntervalNumber_Type = Integer32
_NncNBTotal15MinCurrentAbsoluteIntervalNumber_Object = MibTableColumn
nncNBTotal15MinCurrentAbsoluteIntervalNumber = _NncNBTotal15MinCurrentAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 17, 1, 3),
    _NncNBTotal15MinCurrentAbsoluteIntervalNumber_Type()
)
nncNBTotal15MinCurrentAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinCurrentAbsoluteIntervalNumber.setStatus("current")
_NncNBTotal15MinCurrentFailedCallsDueToInitDTLNotGenerated_Type = Counter32
_NncNBTotal15MinCurrentFailedCallsDueToInitDTLNotGenerated_Object = MibTableColumn
nncNBTotal15MinCurrentFailedCallsDueToInitDTLNotGenerated = _NncNBTotal15MinCurrentFailedCallsDueToInitDTLNotGenerated_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 17, 1, 4),
    _NncNBTotal15MinCurrentFailedCallsDueToInitDTLNotGenerated_Type()
)
nncNBTotal15MinCurrentFailedCallsDueToInitDTLNotGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinCurrentFailedCallsDueToInitDTLNotGenerated.setStatus("current")
_NncNBTotal15MinCurrentCallsGeneratingAnInitDTL_Type = Counter32
_NncNBTotal15MinCurrentCallsGeneratingAnInitDTL_Object = MibTableColumn
nncNBTotal15MinCurrentCallsGeneratingAnInitDTL = _NncNBTotal15MinCurrentCallsGeneratingAnInitDTL_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 17, 1, 5),
    _NncNBTotal15MinCurrentCallsGeneratingAnInitDTL_Type()
)
nncNBTotal15MinCurrentCallsGeneratingAnInitDTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinCurrentCallsGeneratingAnInitDTL.setStatus("current")
_NncNBTotal15MinCurrentDTLOrigCallsSuccessEstWithoutReroute_Type = Counter32
_NncNBTotal15MinCurrentDTLOrigCallsSuccessEstWithoutReroute_Object = MibTableColumn
nncNBTotal15MinCurrentDTLOrigCallsSuccessEstWithoutReroute = _NncNBTotal15MinCurrentDTLOrigCallsSuccessEstWithoutReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 17, 1, 6),
    _NncNBTotal15MinCurrentDTLOrigCallsSuccessEstWithoutReroute_Type()
)
nncNBTotal15MinCurrentDTLOrigCallsSuccessEstWithoutReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinCurrentDTLOrigCallsSuccessEstWithoutReroute.setStatus("current")
_NncNBTotal15MinCurrentDTLOrigCallsSuccessEstWithReroute_Type = Counter32
_NncNBTotal15MinCurrentDTLOrigCallsSuccessEstWithReroute_Object = MibTableColumn
nncNBTotal15MinCurrentDTLOrigCallsSuccessEstWithReroute = _NncNBTotal15MinCurrentDTLOrigCallsSuccessEstWithReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 17, 1, 7),
    _NncNBTotal15MinCurrentDTLOrigCallsSuccessEstWithReroute_Type()
)
nncNBTotal15MinCurrentDTLOrigCallsSuccessEstWithReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinCurrentDTLOrigCallsSuccessEstWithReroute.setStatus("current")
_NncNBTotal15MinCurrentDTLOrigCallsFailedInReRouting_Type = Counter32
_NncNBTotal15MinCurrentDTLOrigCallsFailedInReRouting_Object = MibTableColumn
nncNBTotal15MinCurrentDTLOrigCallsFailedInReRouting = _NncNBTotal15MinCurrentDTLOrigCallsFailedInReRouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 17, 1, 8),
    _NncNBTotal15MinCurrentDTLOrigCallsFailedInReRouting_Type()
)
nncNBTotal15MinCurrentDTLOrigCallsFailedInReRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinCurrentDTLOrigCallsFailedInReRouting.setStatus("current")
_NncNBTotal15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncNBTotal15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncNBTotal15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw = _NncNBTotal15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 17, 1, 9),
    _NncNBTotal15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Type()
)
nncNBTotal15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncNBTotal15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncNBTotal15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncNBTotal15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw = _NncNBTotal15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 17, 1, 10),
    _NncNBTotal15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw_Type()
)
nncNBTotal15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncNBTotal15MinCurrentCrankbackReceivedAsDTLOriginator_Type = Counter32
_NncNBTotal15MinCurrentCrankbackReceivedAsDTLOriginator_Object = MibTableColumn
nncNBTotal15MinCurrentCrankbackReceivedAsDTLOriginator = _NncNBTotal15MinCurrentCrankbackReceivedAsDTLOriginator_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 17, 1, 11),
    _NncNBTotal15MinCurrentCrankbackReceivedAsDTLOriginator_Type()
)
nncNBTotal15MinCurrentCrankbackReceivedAsDTLOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinCurrentCrankbackReceivedAsDTLOriginator.setStatus("current")
_NncNBTotal15MinCurrentDTLsGeneratedDueToCrankback_Type = Counter32
_NncNBTotal15MinCurrentDTLsGeneratedDueToCrankback_Object = MibTableColumn
nncNBTotal15MinCurrentDTLsGeneratedDueToCrankback = _NncNBTotal15MinCurrentDTLsGeneratedDueToCrankback_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 17, 1, 12),
    _NncNBTotal15MinCurrentDTLsGeneratedDueToCrankback_Type()
)
nncNBTotal15MinCurrentDTLsGeneratedDueToCrankback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinCurrentDTLsGeneratedDueToCrankback.setStatus("current")
_NncNBTotal15MinCurrentCallsRecdAsTransitNodeOverInsideLinks_Type = Counter32
_NncNBTotal15MinCurrentCallsRecdAsTransitNodeOverInsideLinks_Object = MibTableColumn
nncNBTotal15MinCurrentCallsRecdAsTransitNodeOverInsideLinks = _NncNBTotal15MinCurrentCallsRecdAsTransitNodeOverInsideLinks_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 17, 1, 13),
    _NncNBTotal15MinCurrentCallsRecdAsTransitNodeOverInsideLinks_Type()
)
nncNBTotal15MinCurrentCallsRecdAsTransitNodeOverInsideLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinCurrentCallsRecdAsTransitNodeOverInsideLinks.setStatus("current")
_NncNBTotal15MinCurrentCrnkbksRecdAsTransitNodeOvInsideLnks_Type = Counter32
_NncNBTotal15MinCurrentCrnkbksRecdAsTransitNodeOvInsideLnks_Object = MibTableColumn
nncNBTotal15MinCurrentCrnkbksRecdAsTransitNodeOvInsideLnks = _NncNBTotal15MinCurrentCrnkbksRecdAsTransitNodeOvInsideLnks_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 17, 1, 14),
    _NncNBTotal15MinCurrentCrnkbksRecdAsTransitNodeOvInsideLnks_Type()
)
nncNBTotal15MinCurrentCrnkbksRecdAsTransitNodeOvInsideLnks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinCurrentCrnkbksRecdAsTransitNodeOvInsideLnks.setStatus("current")
_NncNBTotal15MinCurrentSucdEndBlocCrnkbksRecdOvInsideLnks_Type = Counter32
_NncNBTotal15MinCurrentSucdEndBlocCrnkbksRecdOvInsideLnks_Object = MibTableColumn
nncNBTotal15MinCurrentSucdEndBlocCrnkbksRecdOvInsideLnks = _NncNBTotal15MinCurrentSucdEndBlocCrnkbksRecdOvInsideLnks_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 17, 1, 15),
    _NncNBTotal15MinCurrentSucdEndBlocCrnkbksRecdOvInsideLnks_Type()
)
nncNBTotal15MinCurrentSucdEndBlocCrnkbksRecdOvInsideLnks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinCurrentSucdEndBlocCrnkbksRecdOvInsideLnks.setStatus("current")
_NncRoutingStatsNonBorderTotal15MinIntervalTable_Object = MibTable
nncRoutingStatsNonBorderTotal15MinIntervalTable = _NncRoutingStatsNonBorderTotal15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 18)
)
if mibBuilder.loadTexts:
    nncRoutingStatsNonBorderTotal15MinIntervalTable.setStatus("current")
_NncRoutingStatsNonBorderTotal15MinIntervalEntry_Object = MibTableRow
nncRoutingStatsNonBorderTotal15MinIntervalEntry = _NncRoutingStatsNonBorderTotal15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 18, 1)
)
nncRoutingStatsNonBorderTotal15MinIntervalEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsNonBorderTotal15MinIntervalEntry.setStatus("current")


class _NncNBTotal15MinIntervalNumber_Type(Integer32):
    """Custom type nncNBTotal15MinIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NncNBTotal15MinIntervalNumber_Type.__name__ = "Integer32"
_NncNBTotal15MinIntervalNumber_Object = MibTableColumn
nncNBTotal15MinIntervalNumber = _NncNBTotal15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 18, 1, 2),
    _NncNBTotal15MinIntervalNumber_Type()
)
nncNBTotal15MinIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncNBTotal15MinIntervalNumber.setStatus("current")
_NncNBTotal15MinIntervalState_Type = NncExtIntvlStateType
_NncNBTotal15MinIntervalState_Object = MibTableColumn
nncNBTotal15MinIntervalState = _NncNBTotal15MinIntervalState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 18, 1, 3),
    _NncNBTotal15MinIntervalState_Type()
)
nncNBTotal15MinIntervalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinIntervalState.setStatus("current")
_NncNBTotal15MinIntervalAbsoluteIntervalNumber_Type = Integer32
_NncNBTotal15MinIntervalAbsoluteIntervalNumber_Object = MibTableColumn
nncNBTotal15MinIntervalAbsoluteIntervalNumber = _NncNBTotal15MinIntervalAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 18, 1, 4),
    _NncNBTotal15MinIntervalAbsoluteIntervalNumber_Type()
)
nncNBTotal15MinIntervalAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinIntervalAbsoluteIntervalNumber.setStatus("current")
_NncNBTotal15MinIntervalFailedCallsDueToInitDTLNotGenerated_Type = Counter32
_NncNBTotal15MinIntervalFailedCallsDueToInitDTLNotGenerated_Object = MibTableColumn
nncNBTotal15MinIntervalFailedCallsDueToInitDTLNotGenerated = _NncNBTotal15MinIntervalFailedCallsDueToInitDTLNotGenerated_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 18, 1, 5),
    _NncNBTotal15MinIntervalFailedCallsDueToInitDTLNotGenerated_Type()
)
nncNBTotal15MinIntervalFailedCallsDueToInitDTLNotGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinIntervalFailedCallsDueToInitDTLNotGenerated.setStatus("current")
_NncNBTotal15MinIntervalCallsGeneratingAnInitDTL_Type = Counter32
_NncNBTotal15MinIntervalCallsGeneratingAnInitDTL_Object = MibTableColumn
nncNBTotal15MinIntervalCallsGeneratingAnInitDTL = _NncNBTotal15MinIntervalCallsGeneratingAnInitDTL_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 18, 1, 6),
    _NncNBTotal15MinIntervalCallsGeneratingAnInitDTL_Type()
)
nncNBTotal15MinIntervalCallsGeneratingAnInitDTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinIntervalCallsGeneratingAnInitDTL.setStatus("current")
_NncNBTotal15MinIntervalDTLOrigCallsSuccessEstWithoutReroute_Type = Counter32
_NncNBTotal15MinIntervalDTLOrigCallsSuccessEstWithoutReroute_Object = MibTableColumn
nncNBTotal15MinIntervalDTLOrigCallsSuccessEstWithoutReroute = _NncNBTotal15MinIntervalDTLOrigCallsSuccessEstWithoutReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 18, 1, 7),
    _NncNBTotal15MinIntervalDTLOrigCallsSuccessEstWithoutReroute_Type()
)
nncNBTotal15MinIntervalDTLOrigCallsSuccessEstWithoutReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinIntervalDTLOrigCallsSuccessEstWithoutReroute.setStatus("current")
_NncNBTotal15MinIntervalDTLOrigCallsSuccessEstWithReroute_Type = Counter32
_NncNBTotal15MinIntervalDTLOrigCallsSuccessEstWithReroute_Object = MibTableColumn
nncNBTotal15MinIntervalDTLOrigCallsSuccessEstWithReroute = _NncNBTotal15MinIntervalDTLOrigCallsSuccessEstWithReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 18, 1, 8),
    _NncNBTotal15MinIntervalDTLOrigCallsSuccessEstWithReroute_Type()
)
nncNBTotal15MinIntervalDTLOrigCallsSuccessEstWithReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinIntervalDTLOrigCallsSuccessEstWithReroute.setStatus("current")
_NncNBTotal15MinIntervalDTLOrigCallsFailedInReRouting_Type = Counter32
_NncNBTotal15MinIntervalDTLOrigCallsFailedInReRouting_Object = MibTableColumn
nncNBTotal15MinIntervalDTLOrigCallsFailedInReRouting = _NncNBTotal15MinIntervalDTLOrigCallsFailedInReRouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 18, 1, 9),
    _NncNBTotal15MinIntervalDTLOrigCallsFailedInReRouting_Type()
)
nncNBTotal15MinIntervalDTLOrigCallsFailedInReRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinIntervalDTLOrigCallsFailedInReRouting.setStatus("current")
_NncNBTotal15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncNBTotal15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncNBTotal15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw = _NncNBTotal15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 18, 1, 10),
    _NncNBTotal15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Type()
)
nncNBTotal15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncNBTotal15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncNBTotal15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncNBTotal15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw = _NncNBTotal15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 18, 1, 11),
    _NncNBTotal15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw_Type()
)
nncNBTotal15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncNBTotal15MinIntervalCrankbackReceivedAsDTLOriginator_Type = Counter32
_NncNBTotal15MinIntervalCrankbackReceivedAsDTLOriginator_Object = MibTableColumn
nncNBTotal15MinIntervalCrankbackReceivedAsDTLOriginator = _NncNBTotal15MinIntervalCrankbackReceivedAsDTLOriginator_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 18, 1, 12),
    _NncNBTotal15MinIntervalCrankbackReceivedAsDTLOriginator_Type()
)
nncNBTotal15MinIntervalCrankbackReceivedAsDTLOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinIntervalCrankbackReceivedAsDTLOriginator.setStatus("current")
_NncNBTotal15MinIntervalDTLsGeneratedDueToCrankback_Type = Counter32
_NncNBTotal15MinIntervalDTLsGeneratedDueToCrankback_Object = MibTableColumn
nncNBTotal15MinIntervalDTLsGeneratedDueToCrankback = _NncNBTotal15MinIntervalDTLsGeneratedDueToCrankback_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 18, 1, 13),
    _NncNBTotal15MinIntervalDTLsGeneratedDueToCrankback_Type()
)
nncNBTotal15MinIntervalDTLsGeneratedDueToCrankback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinIntervalDTLsGeneratedDueToCrankback.setStatus("current")
_NncNBTotal15MinIntervalCallsRecdAsTransitNodeOverInsideLinks_Type = Counter32
_NncNBTotal15MinIntervalCallsRecdAsTransitNodeOverInsideLinks_Object = MibTableColumn
nncNBTotal15MinIntervalCallsRecdAsTransitNodeOverInsideLinks = _NncNBTotal15MinIntervalCallsRecdAsTransitNodeOverInsideLinks_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 18, 1, 14),
    _NncNBTotal15MinIntervalCallsRecdAsTransitNodeOverInsideLinks_Type()
)
nncNBTotal15MinIntervalCallsRecdAsTransitNodeOverInsideLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinIntervalCallsRecdAsTransitNodeOverInsideLinks.setStatus("current")
_NncNBTotal15MinIntervalCrnkbksRecdAsTransitNodeOvInsideLnks_Type = Counter32
_NncNBTotal15MinIntervalCrnkbksRecdAsTransitNodeOvInsideLnks_Object = MibTableColumn
nncNBTotal15MinIntervalCrnkbksRecdAsTransitNodeOvInsideLnks = _NncNBTotal15MinIntervalCrnkbksRecdAsTransitNodeOvInsideLnks_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 18, 1, 15),
    _NncNBTotal15MinIntervalCrnkbksRecdAsTransitNodeOvInsideLnks_Type()
)
nncNBTotal15MinIntervalCrnkbksRecdAsTransitNodeOvInsideLnks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinIntervalCrnkbksRecdAsTransitNodeOvInsideLnks.setStatus("current")
_NncNBTotal15MinIntervalSucdEndBlocCrnkbksRecdOvInsideLnks_Type = Counter32
_NncNBTotal15MinIntervalSucdEndBlocCrnkbksRecdOvInsideLnks_Object = MibTableColumn
nncNBTotal15MinIntervalSucdEndBlocCrnkbksRecdOvInsideLnks = _NncNBTotal15MinIntervalSucdEndBlocCrnkbksRecdOvInsideLnks_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 18, 1, 16),
    _NncNBTotal15MinIntervalSucdEndBlocCrnkbksRecdOvInsideLnks_Type()
)
nncNBTotal15MinIntervalSucdEndBlocCrnkbksRecdOvInsideLnks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal15MinIntervalSucdEndBlocCrnkbksRecdOvInsideLnks.setStatus("current")
_NncRoutingStatsNonBorderTotal24HourCurrentTable_Object = MibTable
nncRoutingStatsNonBorderTotal24HourCurrentTable = _NncRoutingStatsNonBorderTotal24HourCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 19)
)
if mibBuilder.loadTexts:
    nncRoutingStatsNonBorderTotal24HourCurrentTable.setStatus("current")
_NncRoutingStatsNonBorderTotal24HourCurrentEntry_Object = MibTableRow
nncRoutingStatsNonBorderTotal24HourCurrentEntry = _NncRoutingStatsNonBorderTotal24HourCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 19, 1)
)
nncRoutingStatsNonBorderTotal24HourCurrentEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsNonBorderTotal24HourCurrentEntry.setStatus("current")
_NncNBTotal24HourCurrentState_Type = NncExtIntvlStateType
_NncNBTotal24HourCurrentState_Object = MibTableColumn
nncNBTotal24HourCurrentState = _NncNBTotal24HourCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 19, 1, 2),
    _NncNBTotal24HourCurrentState_Type()
)
nncNBTotal24HourCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourCurrentState.setStatus("current")
_NncNBTotal24HourCurrentAbsoluteIntervalNumber_Type = Integer32
_NncNBTotal24HourCurrentAbsoluteIntervalNumber_Object = MibTableColumn
nncNBTotal24HourCurrentAbsoluteIntervalNumber = _NncNBTotal24HourCurrentAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 19, 1, 3),
    _NncNBTotal24HourCurrentAbsoluteIntervalNumber_Type()
)
nncNBTotal24HourCurrentAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourCurrentAbsoluteIntervalNumber.setStatus("current")
_NncNBTotal24HourCurrentFailedCallsDueToInitDTLNotGenerated_Type = Counter32
_NncNBTotal24HourCurrentFailedCallsDueToInitDTLNotGenerated_Object = MibTableColumn
nncNBTotal24HourCurrentFailedCallsDueToInitDTLNotGenerated = _NncNBTotal24HourCurrentFailedCallsDueToInitDTLNotGenerated_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 19, 1, 4),
    _NncNBTotal24HourCurrentFailedCallsDueToInitDTLNotGenerated_Type()
)
nncNBTotal24HourCurrentFailedCallsDueToInitDTLNotGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourCurrentFailedCallsDueToInitDTLNotGenerated.setStatus("current")
_NncNBTotal24HourCurrentCallsGeneratingAnInitDTL_Type = Counter32
_NncNBTotal24HourCurrentCallsGeneratingAnInitDTL_Object = MibTableColumn
nncNBTotal24HourCurrentCallsGeneratingAnInitDTL = _NncNBTotal24HourCurrentCallsGeneratingAnInitDTL_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 19, 1, 5),
    _NncNBTotal24HourCurrentCallsGeneratingAnInitDTL_Type()
)
nncNBTotal24HourCurrentCallsGeneratingAnInitDTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourCurrentCallsGeneratingAnInitDTL.setStatus("current")
_NncNBTotal24HourCurrentDTLOrigCallsSuccessEstWithoutReroute_Type = Counter32
_NncNBTotal24HourCurrentDTLOrigCallsSuccessEstWithoutReroute_Object = MibTableColumn
nncNBTotal24HourCurrentDTLOrigCallsSuccessEstWithoutReroute = _NncNBTotal24HourCurrentDTLOrigCallsSuccessEstWithoutReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 19, 1, 6),
    _NncNBTotal24HourCurrentDTLOrigCallsSuccessEstWithoutReroute_Type()
)
nncNBTotal24HourCurrentDTLOrigCallsSuccessEstWithoutReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourCurrentDTLOrigCallsSuccessEstWithoutReroute.setStatus("current")
_NncNBTotal24HourCurrentDTLOrigCallsSuccessEstWithReroute_Type = Counter32
_NncNBTotal24HourCurrentDTLOrigCallsSuccessEstWithReroute_Object = MibTableColumn
nncNBTotal24HourCurrentDTLOrigCallsSuccessEstWithReroute = _NncNBTotal24HourCurrentDTLOrigCallsSuccessEstWithReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 19, 1, 7),
    _NncNBTotal24HourCurrentDTLOrigCallsSuccessEstWithReroute_Type()
)
nncNBTotal24HourCurrentDTLOrigCallsSuccessEstWithReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourCurrentDTLOrigCallsSuccessEstWithReroute.setStatus("current")
_NncNBTotal24HourCurrentDTLOrigCallsFailedInReRouting_Type = Counter32
_NncNBTotal24HourCurrentDTLOrigCallsFailedInReRouting_Object = MibTableColumn
nncNBTotal24HourCurrentDTLOrigCallsFailedInReRouting = _NncNBTotal24HourCurrentDTLOrigCallsFailedInReRouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 19, 1, 8),
    _NncNBTotal24HourCurrentDTLOrigCallsFailedInReRouting_Type()
)
nncNBTotal24HourCurrentDTLOrigCallsFailedInReRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourCurrentDTLOrigCallsFailedInReRouting.setStatus("current")
_NncNBTotal24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncNBTotal24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncNBTotal24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw = _NncNBTotal24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 19, 1, 9),
    _NncNBTotal24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Type()
)
nncNBTotal24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncNBTotal24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncNBTotal24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncNBTotal24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw = _NncNBTotal24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 19, 1, 10),
    _NncNBTotal24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw_Type()
)
nncNBTotal24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncNBTotal24HourCurrentCrankbackReceivedAsDTLOriginator_Type = Counter32
_NncNBTotal24HourCurrentCrankbackReceivedAsDTLOriginator_Object = MibTableColumn
nncNBTotal24HourCurrentCrankbackReceivedAsDTLOriginator = _NncNBTotal24HourCurrentCrankbackReceivedAsDTLOriginator_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 19, 1, 11),
    _NncNBTotal24HourCurrentCrankbackReceivedAsDTLOriginator_Type()
)
nncNBTotal24HourCurrentCrankbackReceivedAsDTLOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourCurrentCrankbackReceivedAsDTLOriginator.setStatus("current")
_NncNBTotal24HourCurrentDTLsGeneratedDueToCrankback_Type = Counter32
_NncNBTotal24HourCurrentDTLsGeneratedDueToCrankback_Object = MibTableColumn
nncNBTotal24HourCurrentDTLsGeneratedDueToCrankback = _NncNBTotal24HourCurrentDTLsGeneratedDueToCrankback_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 19, 1, 12),
    _NncNBTotal24HourCurrentDTLsGeneratedDueToCrankback_Type()
)
nncNBTotal24HourCurrentDTLsGeneratedDueToCrankback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourCurrentDTLsGeneratedDueToCrankback.setStatus("current")
_NncNBTotal24HourCurrentCallsRecdAsTransitNodeOverInsideLinks_Type = Counter32
_NncNBTotal24HourCurrentCallsRecdAsTransitNodeOverInsideLinks_Object = MibTableColumn
nncNBTotal24HourCurrentCallsRecdAsTransitNodeOverInsideLinks = _NncNBTotal24HourCurrentCallsRecdAsTransitNodeOverInsideLinks_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 19, 1, 13),
    _NncNBTotal24HourCurrentCallsRecdAsTransitNodeOverInsideLinks_Type()
)
nncNBTotal24HourCurrentCallsRecdAsTransitNodeOverInsideLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourCurrentCallsRecdAsTransitNodeOverInsideLinks.setStatus("current")
_NncNBTotal24HourCurrentCrnkbksRecdAsTransNodeOvInsideLnks_Type = Counter32
_NncNBTotal24HourCurrentCrnkbksRecdAsTransNodeOvInsideLnks_Object = MibTableColumn
nncNBTotal24HourCurrentCrnkbksRecdAsTransNodeOvInsideLnks = _NncNBTotal24HourCurrentCrnkbksRecdAsTransNodeOvInsideLnks_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 19, 1, 14),
    _NncNBTotal24HourCurrentCrnkbksRecdAsTransNodeOvInsideLnks_Type()
)
nncNBTotal24HourCurrentCrnkbksRecdAsTransNodeOvInsideLnks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourCurrentCrnkbksRecdAsTransNodeOvInsideLnks.setStatus("current")
_NncNBTotal24HourCurrentSucdEndBlocCrnkbksRecdOverInsideLinks_Type = Counter32
_NncNBTotal24HourCurrentSucdEndBlocCrnkbksRecdOverInsideLinks_Object = MibTableColumn
nncNBTotal24HourCurrentSucdEndBlocCrnkbksRecdOverInsideLinks = _NncNBTotal24HourCurrentSucdEndBlocCrnkbksRecdOverInsideLinks_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 19, 1, 15),
    _NncNBTotal24HourCurrentSucdEndBlocCrnkbksRecdOverInsideLinks_Type()
)
nncNBTotal24HourCurrentSucdEndBlocCrnkbksRecdOverInsideLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourCurrentSucdEndBlocCrnkbksRecdOverInsideLinks.setStatus("current")
_NncRoutingStatsNonBorderTotal24HourIntervalTable_Object = MibTable
nncRoutingStatsNonBorderTotal24HourIntervalTable = _NncRoutingStatsNonBorderTotal24HourIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 20)
)
if mibBuilder.loadTexts:
    nncRoutingStatsNonBorderTotal24HourIntervalTable.setStatus("current")
_NncRoutingStatsNonBorderTotal24HourIntervalEntry_Object = MibTableRow
nncRoutingStatsNonBorderTotal24HourIntervalEntry = _NncRoutingStatsNonBorderTotal24HourIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 20, 1)
)
nncRoutingStatsNonBorderTotal24HourIntervalEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourIntervalNumber"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsNonBorderTotal24HourIntervalEntry.setStatus("current")
_NncNBTotal24HourIntervalNumber_Type = Integer32
_NncNBTotal24HourIntervalNumber_Object = MibTableColumn
nncNBTotal24HourIntervalNumber = _NncNBTotal24HourIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 20, 1, 2),
    _NncNBTotal24HourIntervalNumber_Type()
)
nncNBTotal24HourIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncNBTotal24HourIntervalNumber.setStatus("current")
_NncNBTotal24HourIntervalState_Type = NncExtIntvlStateType
_NncNBTotal24HourIntervalState_Object = MibTableColumn
nncNBTotal24HourIntervalState = _NncNBTotal24HourIntervalState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 20, 1, 3),
    _NncNBTotal24HourIntervalState_Type()
)
nncNBTotal24HourIntervalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourIntervalState.setStatus("current")
_NncNBTotal24HourIntervalAbsoluteIntervalNumber_Type = Integer32
_NncNBTotal24HourIntervalAbsoluteIntervalNumber_Object = MibTableColumn
nncNBTotal24HourIntervalAbsoluteIntervalNumber = _NncNBTotal24HourIntervalAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 20, 1, 4),
    _NncNBTotal24HourIntervalAbsoluteIntervalNumber_Type()
)
nncNBTotal24HourIntervalAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourIntervalAbsoluteIntervalNumber.setStatus("current")
_NncNBTotal24HourIntervalFailedCallsDueToInitDTLNotGenerated_Type = Counter32
_NncNBTotal24HourIntervalFailedCallsDueToInitDTLNotGenerated_Object = MibTableColumn
nncNBTotal24HourIntervalFailedCallsDueToInitDTLNotGenerated = _NncNBTotal24HourIntervalFailedCallsDueToInitDTLNotGenerated_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 20, 1, 5),
    _NncNBTotal24HourIntervalFailedCallsDueToInitDTLNotGenerated_Type()
)
nncNBTotal24HourIntervalFailedCallsDueToInitDTLNotGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourIntervalFailedCallsDueToInitDTLNotGenerated.setStatus("current")
_NncNBTotal24HourIntervalCallsGeneratingAnInitDTL_Type = Counter32
_NncNBTotal24HourIntervalCallsGeneratingAnInitDTL_Object = MibTableColumn
nncNBTotal24HourIntervalCallsGeneratingAnInitDTL = _NncNBTotal24HourIntervalCallsGeneratingAnInitDTL_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 20, 1, 6),
    _NncNBTotal24HourIntervalCallsGeneratingAnInitDTL_Type()
)
nncNBTotal24HourIntervalCallsGeneratingAnInitDTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourIntervalCallsGeneratingAnInitDTL.setStatus("current")
_NncNBTotal24HourIntervalDTLOrigCallsSuccessEstWithoutReroute_Type = Counter32
_NncNBTotal24HourIntervalDTLOrigCallsSuccessEstWithoutReroute_Object = MibTableColumn
nncNBTotal24HourIntervalDTLOrigCallsSuccessEstWithoutReroute = _NncNBTotal24HourIntervalDTLOrigCallsSuccessEstWithoutReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 20, 1, 7),
    _NncNBTotal24HourIntervalDTLOrigCallsSuccessEstWithoutReroute_Type()
)
nncNBTotal24HourIntervalDTLOrigCallsSuccessEstWithoutReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourIntervalDTLOrigCallsSuccessEstWithoutReroute.setStatus("current")
_NncNBTotal24HourIntervalDTLOrigCallsSuccessEstWithReroute_Type = Counter32
_NncNBTotal24HourIntervalDTLOrigCallsSuccessEstWithReroute_Object = MibTableColumn
nncNBTotal24HourIntervalDTLOrigCallsSuccessEstWithReroute = _NncNBTotal24HourIntervalDTLOrigCallsSuccessEstWithReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 20, 1, 8),
    _NncNBTotal24HourIntervalDTLOrigCallsSuccessEstWithReroute_Type()
)
nncNBTotal24HourIntervalDTLOrigCallsSuccessEstWithReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourIntervalDTLOrigCallsSuccessEstWithReroute.setStatus("current")
_NncNBTotal24HourIntervalDTLOrigCallsFailedInReRouting_Type = Counter32
_NncNBTotal24HourIntervalDTLOrigCallsFailedInReRouting_Object = MibTableColumn
nncNBTotal24HourIntervalDTLOrigCallsFailedInReRouting = _NncNBTotal24HourIntervalDTLOrigCallsFailedInReRouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 20, 1, 9),
    _NncNBTotal24HourIntervalDTLOrigCallsFailedInReRouting_Type()
)
nncNBTotal24HourIntervalDTLOrigCallsFailedInReRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourIntervalDTLOrigCallsFailedInReRouting.setStatus("current")
_NncNBTotal24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncNBTotal24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncNBTotal24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw = _NncNBTotal24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 20, 1, 10),
    _NncNBTotal24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Type()
)
nncNBTotal24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncNBTotal24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncNBTotal24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncNBTotal24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw = _NncNBTotal24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 20, 1, 11),
    _NncNBTotal24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw_Type()
)
nncNBTotal24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncNBTotal24HourIntervalCrankbackReceivedAsDTLOriginator_Type = Counter32
_NncNBTotal24HourIntervalCrankbackReceivedAsDTLOriginator_Object = MibTableColumn
nncNBTotal24HourIntervalCrankbackReceivedAsDTLOriginator = _NncNBTotal24HourIntervalCrankbackReceivedAsDTLOriginator_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 20, 1, 12),
    _NncNBTotal24HourIntervalCrankbackReceivedAsDTLOriginator_Type()
)
nncNBTotal24HourIntervalCrankbackReceivedAsDTLOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourIntervalCrankbackReceivedAsDTLOriginator.setStatus("current")
_NncNBTotal24HourIntervalDTLsGeneratedDueToCrankback_Type = Counter32
_NncNBTotal24HourIntervalDTLsGeneratedDueToCrankback_Object = MibTableColumn
nncNBTotal24HourIntervalDTLsGeneratedDueToCrankback = _NncNBTotal24HourIntervalDTLsGeneratedDueToCrankback_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 20, 1, 13),
    _NncNBTotal24HourIntervalDTLsGeneratedDueToCrankback_Type()
)
nncNBTotal24HourIntervalDTLsGeneratedDueToCrankback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourIntervalDTLsGeneratedDueToCrankback.setStatus("current")
_NncNBTotal24HourIntervalCallsRecdAsTransitNodeOverInsideLinks_Type = Counter32
_NncNBTotal24HourIntervalCallsRecdAsTransitNodeOverInsideLinks_Object = MibTableColumn
nncNBTotal24HourIntervalCallsRecdAsTransitNodeOverInsideLinks = _NncNBTotal24HourIntervalCallsRecdAsTransitNodeOverInsideLinks_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 20, 1, 14),
    _NncNBTotal24HourIntervalCallsRecdAsTransitNodeOverInsideLinks_Type()
)
nncNBTotal24HourIntervalCallsRecdAsTransitNodeOverInsideLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourIntervalCallsRecdAsTransitNodeOverInsideLinks.setStatus("current")
_NncNBTotal24HourIntervalCrnkbksRecdAsTransNodeOverInsideLnks_Type = Counter32
_NncNBTotal24HourIntervalCrnkbksRecdAsTransNodeOverInsideLnks_Object = MibTableColumn
nncNBTotal24HourIntervalCrnkbksRecdAsTransNodeOverInsideLnks = _NncNBTotal24HourIntervalCrnkbksRecdAsTransNodeOverInsideLnks_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 20, 1, 15),
    _NncNBTotal24HourIntervalCrnkbksRecdAsTransNodeOverInsideLnks_Type()
)
nncNBTotal24HourIntervalCrnkbksRecdAsTransNodeOverInsideLnks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourIntervalCrnkbksRecdAsTransNodeOverInsideLnks.setStatus("current")
_NncNBTotal24HourIntervalSucdEndBlocCrnkbksRecdOverInsideLnks_Type = Counter32
_NncNBTotal24HourIntervalSucdEndBlocCrnkbksRecdOverInsideLnks_Object = MibTableColumn
nncNBTotal24HourIntervalSucdEndBlocCrnkbksRecdOverInsideLnks = _NncNBTotal24HourIntervalSucdEndBlocCrnkbksRecdOverInsideLnks_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 20, 1, 16),
    _NncNBTotal24HourIntervalSucdEndBlocCrnkbksRecdOverInsideLnks_Type()
)
nncNBTotal24HourIntervalSucdEndBlocCrnkbksRecdOverInsideLnks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNBTotal24HourIntervalSucdEndBlocCrnkbksRecdOverInsideLnks.setStatus("current")
_NncRoutingStatsBorderTotal15MinCurrentTable_Object = MibTable
nncRoutingStatsBorderTotal15MinCurrentTable = _NncRoutingStatsBorderTotal15MinCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 21)
)
if mibBuilder.loadTexts:
    nncRoutingStatsBorderTotal15MinCurrentTable.setStatus("current")
_NncRoutingStatsBorderTotal15MinCurrentEntry_Object = MibTableRow
nncRoutingStatsBorderTotal15MinCurrentEntry = _NncRoutingStatsBorderTotal15MinCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 21, 1)
)
nncRoutingStatsBorderTotal15MinCurrentEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsBorderTotal15MinCurrentEntry.setStatus("current")
_NncBTotal15MinCurrentState_Type = NncExtIntvlStateType
_NncBTotal15MinCurrentState_Object = MibTableColumn
nncBTotal15MinCurrentState = _NncBTotal15MinCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 21, 1, 2),
    _NncBTotal15MinCurrentState_Type()
)
nncBTotal15MinCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinCurrentState.setStatus("current")
_NncBTotal15MinCurrentAbsoluteIntervalNumber_Type = Integer32
_NncBTotal15MinCurrentAbsoluteIntervalNumber_Object = MibTableColumn
nncBTotal15MinCurrentAbsoluteIntervalNumber = _NncBTotal15MinCurrentAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 21, 1, 3),
    _NncBTotal15MinCurrentAbsoluteIntervalNumber_Type()
)
nncBTotal15MinCurrentAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinCurrentAbsoluteIntervalNumber.setStatus("current")
_NncBTotal15MinCurrentFailedCallsDueToInitLowerLvlDTLNotGen_Type = Counter32
_NncBTotal15MinCurrentFailedCallsDueToInitLowerLvlDTLNotGen_Object = MibTableColumn
nncBTotal15MinCurrentFailedCallsDueToInitLowerLvlDTLNotGen = _NncBTotal15MinCurrentFailedCallsDueToInitLowerLvlDTLNotGen_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 21, 1, 4),
    _NncBTotal15MinCurrentFailedCallsDueToInitLowerLvlDTLNotGen_Type()
)
nncBTotal15MinCurrentFailedCallsDueToInitLowerLvlDTLNotGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinCurrentFailedCallsDueToInitLowerLvlDTLNotGen.setStatus("current")
_NncBTotal15MinCurrentCallsGeneratingInitLowerLvlDTLs_Type = Counter32
_NncBTotal15MinCurrentCallsGeneratingInitLowerLvlDTLs_Object = MibTableColumn
nncBTotal15MinCurrentCallsGeneratingInitLowerLvlDTLs = _NncBTotal15MinCurrentCallsGeneratingInitLowerLvlDTLs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 21, 1, 5),
    _NncBTotal15MinCurrentCallsGeneratingInitLowerLvlDTLs_Type()
)
nncBTotal15MinCurrentCallsGeneratingInitLowerLvlDTLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinCurrentCallsGeneratingInitLowerLvlDTLs.setStatus("current")
_NncBTotal15MinCurrentDTLGenCallsSuccessEstWithoutReroute_Type = Counter32
_NncBTotal15MinCurrentDTLGenCallsSuccessEstWithoutReroute_Object = MibTableColumn
nncBTotal15MinCurrentDTLGenCallsSuccessEstWithoutReroute = _NncBTotal15MinCurrentDTLGenCallsSuccessEstWithoutReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 21, 1, 6),
    _NncBTotal15MinCurrentDTLGenCallsSuccessEstWithoutReroute_Type()
)
nncBTotal15MinCurrentDTLGenCallsSuccessEstWithoutReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinCurrentDTLGenCallsSuccessEstWithoutReroute.setStatus("current")
_NncBTotal15MinCurrentDTLGenCallsSuccessEstWithReroute_Type = Counter32
_NncBTotal15MinCurrentDTLGenCallsSuccessEstWithReroute_Object = MibTableColumn
nncBTotal15MinCurrentDTLGenCallsSuccessEstWithReroute = _NncBTotal15MinCurrentDTLGenCallsSuccessEstWithReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 21, 1, 7),
    _NncBTotal15MinCurrentDTLGenCallsSuccessEstWithReroute_Type()
)
nncBTotal15MinCurrentDTLGenCallsSuccessEstWithReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinCurrentDTLGenCallsSuccessEstWithReroute.setStatus("current")
_NncBTotal15MinCurrentDTLGenCallsFailedInReRouting_Type = Counter32
_NncBTotal15MinCurrentDTLGenCallsFailedInReRouting_Object = MibTableColumn
nncBTotal15MinCurrentDTLGenCallsFailedInReRouting = _NncBTotal15MinCurrentDTLGenCallsFailedInReRouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 21, 1, 8),
    _NncBTotal15MinCurrentDTLGenCallsFailedInReRouting_Type()
)
nncBTotal15MinCurrentDTLGenCallsFailedInReRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinCurrentDTLGenCallsFailedInReRouting.setStatus("current")
_NncBTotal15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncBTotal15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncBTotal15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw = _NncBTotal15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 21, 1, 9),
    _NncBTotal15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Type()
)
nncBTotal15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncBTotal15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncBTotal15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncBTotal15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw = _NncBTotal15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 21, 1, 10),
    _NncBTotal15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw_Type()
)
nncBTotal15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncBTotal15MinCurrentCrankbackReceivedAsAnEntryBorderNode_Type = Counter32
_NncBTotal15MinCurrentCrankbackReceivedAsAnEntryBorderNode_Object = MibTableColumn
nncBTotal15MinCurrentCrankbackReceivedAsAnEntryBorderNode = _NncBTotal15MinCurrentCrankbackReceivedAsAnEntryBorderNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 21, 1, 11),
    _NncBTotal15MinCurrentCrankbackReceivedAsAnEntryBorderNode_Type()
)
nncBTotal15MinCurrentCrankbackReceivedAsAnEntryBorderNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinCurrentCrankbackReceivedAsAnEntryBorderNode.setStatus("current")
_NncBTotal15MinCurrentLowerLvlDTLsGenDueToRecdCrankback_Type = Counter32
_NncBTotal15MinCurrentLowerLvlDTLsGenDueToRecdCrankback_Object = MibTableColumn
nncBTotal15MinCurrentLowerLvlDTLsGenDueToRecdCrankback = _NncBTotal15MinCurrentLowerLvlDTLsGenDueToRecdCrankback_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 21, 1, 12),
    _NncBTotal15MinCurrentLowerLvlDTLsGenDueToRecdCrankback_Type()
)
nncBTotal15MinCurrentLowerLvlDTLsGenDueToRecdCrankback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinCurrentLowerLvlDTLsGenDueToRecdCrankback.setStatus("current")
_NncBTotal15MinCurrentCallsRecdOverAnOutsideLink_Type = Counter32
_NncBTotal15MinCurrentCallsRecdOverAnOutsideLink_Object = MibTableColumn
nncBTotal15MinCurrentCallsRecdOverAnOutsideLink = _NncBTotal15MinCurrentCallsRecdOverAnOutsideLink_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 21, 1, 13),
    _NncBTotal15MinCurrentCallsRecdOverAnOutsideLink_Type()
)
nncBTotal15MinCurrentCallsRecdOverAnOutsideLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinCurrentCallsRecdOverAnOutsideLink.setStatus("current")
_NncBTotal15MinCurrentCallsTransmittedOverAnOutsideLink_Type = Counter32
_NncBTotal15MinCurrentCallsTransmittedOverAnOutsideLink_Object = MibTableColumn
nncBTotal15MinCurrentCallsTransmittedOverAnOutsideLink = _NncBTotal15MinCurrentCallsTransmittedOverAnOutsideLink_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 21, 1, 14),
    _NncBTotal15MinCurrentCallsTransmittedOverAnOutsideLink_Type()
)
nncBTotal15MinCurrentCallsTransmittedOverAnOutsideLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinCurrentCallsTransmittedOverAnOutsideLink.setStatus("current")
_NncBTotal15MinCurrentCrankbksRecdOverAnOutsideLink_Type = Counter32
_NncBTotal15MinCurrentCrankbksRecdOverAnOutsideLink_Object = MibTableColumn
nncBTotal15MinCurrentCrankbksRecdOverAnOutsideLink = _NncBTotal15MinCurrentCrankbksRecdOverAnOutsideLink_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 21, 1, 15),
    _NncBTotal15MinCurrentCrankbksRecdOverAnOutsideLink_Type()
)
nncBTotal15MinCurrentCrankbksRecdOverAnOutsideLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinCurrentCrankbksRecdOverAnOutsideLink.setStatus("current")
_NncBTotal15MinCurreSucdEndBlocCrankbksRecdOverOutsideLink_Type = Counter32
_NncBTotal15MinCurreSucdEndBlocCrankbksRecdOverOutsideLink_Object = MibTableColumn
nncBTotal15MinCurreSucdEndBlocCrankbksRecdOverOutsideLink = _NncBTotal15MinCurreSucdEndBlocCrankbksRecdOverOutsideLink_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 21, 1, 16),
    _NncBTotal15MinCurreSucdEndBlocCrankbksRecdOverOutsideLink_Type()
)
nncBTotal15MinCurreSucdEndBlocCrankbksRecdOverOutsideLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinCurreSucdEndBlocCrankbksRecdOverOutsideLink.setStatus("current")
_NncBTotal15MinCurrentCrankbkForwdedToPrevPGCrankbkLvlTooHigh_Type = Counter32
_NncBTotal15MinCurrentCrankbkForwdedToPrevPGCrankbkLvlTooHigh_Object = MibTableColumn
nncBTotal15MinCurrentCrankbkForwdedToPrevPGCrankbkLvlTooHigh = _NncBTotal15MinCurrentCrankbkForwdedToPrevPGCrankbkLvlTooHigh_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 21, 1, 17),
    _NncBTotal15MinCurrentCrankbkForwdedToPrevPGCrankbkLvlTooHigh_Type()
)
nncBTotal15MinCurrentCrankbkForwdedToPrevPGCrankbkLvlTooHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinCurrentCrankbkForwdedToPrevPGCrankbkLvlTooHigh.setStatus("current")
_NncRoutingStatsBorderTotal15MinIntervalTable_Object = MibTable
nncRoutingStatsBorderTotal15MinIntervalTable = _NncRoutingStatsBorderTotal15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 22)
)
if mibBuilder.loadTexts:
    nncRoutingStatsBorderTotal15MinIntervalTable.setStatus("current")
_NncRoutingStatsBorderTotal15MinIntervalEntry_Object = MibTableRow
nncRoutingStatsBorderTotal15MinIntervalEntry = _NncRoutingStatsBorderTotal15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 22, 1)
)
nncRoutingStatsBorderTotal15MinIntervalEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsBorderTotal15MinIntervalEntry.setStatus("current")


class _NncBTotal15MinIntervalNumber_Type(Integer32):
    """Custom type nncBTotal15MinIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NncBTotal15MinIntervalNumber_Type.__name__ = "Integer32"
_NncBTotal15MinIntervalNumber_Object = MibTableColumn
nncBTotal15MinIntervalNumber = _NncBTotal15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 22, 1, 2),
    _NncBTotal15MinIntervalNumber_Type()
)
nncBTotal15MinIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncBTotal15MinIntervalNumber.setStatus("current")
_NncBTotal15MinIntervalState_Type = NncExtIntvlStateType
_NncBTotal15MinIntervalState_Object = MibTableColumn
nncBTotal15MinIntervalState = _NncBTotal15MinIntervalState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 22, 1, 3),
    _NncBTotal15MinIntervalState_Type()
)
nncBTotal15MinIntervalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinIntervalState.setStatus("current")
_NncBTotal15MinIntervalAbsoluteIntervalNumber_Type = Integer32
_NncBTotal15MinIntervalAbsoluteIntervalNumber_Object = MibTableColumn
nncBTotal15MinIntervalAbsoluteIntervalNumber = _NncBTotal15MinIntervalAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 22, 1, 4),
    _NncBTotal15MinIntervalAbsoluteIntervalNumber_Type()
)
nncBTotal15MinIntervalAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinIntervalAbsoluteIntervalNumber.setStatus("current")
_NncBTotal15MinIntervalFailedCallsDueToInitLowerLvlDTLNotGen_Type = Counter32
_NncBTotal15MinIntervalFailedCallsDueToInitLowerLvlDTLNotGen_Object = MibTableColumn
nncBTotal15MinIntervalFailedCallsDueToInitLowerLvlDTLNotGen = _NncBTotal15MinIntervalFailedCallsDueToInitLowerLvlDTLNotGen_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 22, 1, 5),
    _NncBTotal15MinIntervalFailedCallsDueToInitLowerLvlDTLNotGen_Type()
)
nncBTotal15MinIntervalFailedCallsDueToInitLowerLvlDTLNotGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinIntervalFailedCallsDueToInitLowerLvlDTLNotGen.setStatus("current")
_NncBTotal15MinIntervalCallsGeneratingInitLowerLvlDTLs_Type = Counter32
_NncBTotal15MinIntervalCallsGeneratingInitLowerLvlDTLs_Object = MibTableColumn
nncBTotal15MinIntervalCallsGeneratingInitLowerLvlDTLs = _NncBTotal15MinIntervalCallsGeneratingInitLowerLvlDTLs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 22, 1, 6),
    _NncBTotal15MinIntervalCallsGeneratingInitLowerLvlDTLs_Type()
)
nncBTotal15MinIntervalCallsGeneratingInitLowerLvlDTLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinIntervalCallsGeneratingInitLowerLvlDTLs.setStatus("current")
_NncBTotal15MinIntervalDTLGenCallsSuccessEstWithoutReroute_Type = Counter32
_NncBTotal15MinIntervalDTLGenCallsSuccessEstWithoutReroute_Object = MibTableColumn
nncBTotal15MinIntervalDTLGenCallsSuccessEstWithoutReroute = _NncBTotal15MinIntervalDTLGenCallsSuccessEstWithoutReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 22, 1, 7),
    _NncBTotal15MinIntervalDTLGenCallsSuccessEstWithoutReroute_Type()
)
nncBTotal15MinIntervalDTLGenCallsSuccessEstWithoutReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinIntervalDTLGenCallsSuccessEstWithoutReroute.setStatus("current")
_NncBTotal15MinIntervalDTLGenCallsSuccessEstWithReroute_Type = Counter32
_NncBTotal15MinIntervalDTLGenCallsSuccessEstWithReroute_Object = MibTableColumn
nncBTotal15MinIntervalDTLGenCallsSuccessEstWithReroute = _NncBTotal15MinIntervalDTLGenCallsSuccessEstWithReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 22, 1, 8),
    _NncBTotal15MinIntervalDTLGenCallsSuccessEstWithReroute_Type()
)
nncBTotal15MinIntervalDTLGenCallsSuccessEstWithReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinIntervalDTLGenCallsSuccessEstWithReroute.setStatus("current")
_NncBTotal15MinIntervalDTLGenCallsFailedInReRouting_Type = Counter32
_NncBTotal15MinIntervalDTLGenCallsFailedInReRouting_Object = MibTableColumn
nncBTotal15MinIntervalDTLGenCallsFailedInReRouting = _NncBTotal15MinIntervalDTLGenCallsFailedInReRouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 22, 1, 9),
    _NncBTotal15MinIntervalDTLGenCallsFailedInReRouting_Type()
)
nncBTotal15MinIntervalDTLGenCallsFailedInReRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinIntervalDTLGenCallsFailedInReRouting.setStatus("current")
_NncBTotal15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncBTotal15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncBTotal15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw = _NncBTotal15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 22, 1, 10),
    _NncBTotal15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Type()
)
nncBTotal15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncBTotal15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncBTotal15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncBTotal15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw = _NncBTotal15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 22, 1, 11),
    _NncBTotal15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw_Type()
)
nncBTotal15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncBTotal15MinIntervalCrankbackReceivedAsAnEntryBorderNode_Type = Counter32
_NncBTotal15MinIntervalCrankbackReceivedAsAnEntryBorderNode_Object = MibTableColumn
nncBTotal15MinIntervalCrankbackReceivedAsAnEntryBorderNode = _NncBTotal15MinIntervalCrankbackReceivedAsAnEntryBorderNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 22, 1, 12),
    _NncBTotal15MinIntervalCrankbackReceivedAsAnEntryBorderNode_Type()
)
nncBTotal15MinIntervalCrankbackReceivedAsAnEntryBorderNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinIntervalCrankbackReceivedAsAnEntryBorderNode.setStatus("current")
_NncBTotal15MinIntervalLowerLvlDTLsGenDueToRecdCrankback_Type = Counter32
_NncBTotal15MinIntervalLowerLvlDTLsGenDueToRecdCrankback_Object = MibTableColumn
nncBTotal15MinIntervalLowerLvlDTLsGenDueToRecdCrankback = _NncBTotal15MinIntervalLowerLvlDTLsGenDueToRecdCrankback_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 22, 1, 13),
    _NncBTotal15MinIntervalLowerLvlDTLsGenDueToRecdCrankback_Type()
)
nncBTotal15MinIntervalLowerLvlDTLsGenDueToRecdCrankback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinIntervalLowerLvlDTLsGenDueToRecdCrankback.setStatus("current")
_NncBTotal15MinIntervalCallsRecdOverAnOutsideLink_Type = Counter32
_NncBTotal15MinIntervalCallsRecdOverAnOutsideLink_Object = MibTableColumn
nncBTotal15MinIntervalCallsRecdOverAnOutsideLink = _NncBTotal15MinIntervalCallsRecdOverAnOutsideLink_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 22, 1, 14),
    _NncBTotal15MinIntervalCallsRecdOverAnOutsideLink_Type()
)
nncBTotal15MinIntervalCallsRecdOverAnOutsideLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinIntervalCallsRecdOverAnOutsideLink.setStatus("current")
_NncBTotal15MinIntervalCallsTransmittedOverAnOutsideLink_Type = Counter32
_NncBTotal15MinIntervalCallsTransmittedOverAnOutsideLink_Object = MibTableColumn
nncBTotal15MinIntervalCallsTransmittedOverAnOutsideLink = _NncBTotal15MinIntervalCallsTransmittedOverAnOutsideLink_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 22, 1, 15),
    _NncBTotal15MinIntervalCallsTransmittedOverAnOutsideLink_Type()
)
nncBTotal15MinIntervalCallsTransmittedOverAnOutsideLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinIntervalCallsTransmittedOverAnOutsideLink.setStatus("current")
_NncBTotal15MinIntervalCrankbksRecdOverAnOutsideLink_Type = Counter32
_NncBTotal15MinIntervalCrankbksRecdOverAnOutsideLink_Object = MibTableColumn
nncBTotal15MinIntervalCrankbksRecdOverAnOutsideLink = _NncBTotal15MinIntervalCrankbksRecdOverAnOutsideLink_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 22, 1, 16),
    _NncBTotal15MinIntervalCrankbksRecdOverAnOutsideLink_Type()
)
nncBTotal15MinIntervalCrankbksRecdOverAnOutsideLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinIntervalCrankbksRecdOverAnOutsideLink.setStatus("current")
_NncBTotal15MinIntervalSucdEndBlocCrankbksRecdOverOutsideLink_Type = Counter32
_NncBTotal15MinIntervalSucdEndBlocCrankbksRecdOverOutsideLink_Object = MibTableColumn
nncBTotal15MinIntervalSucdEndBlocCrankbksRecdOverOutsideLink = _NncBTotal15MinIntervalSucdEndBlocCrankbksRecdOverOutsideLink_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 22, 1, 17),
    _NncBTotal15MinIntervalSucdEndBlocCrankbksRecdOverOutsideLink_Type()
)
nncBTotal15MinIntervalSucdEndBlocCrankbksRecdOverOutsideLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinIntervalSucdEndBlocCrankbksRecdOverOutsideLink.setStatus("current")
_NncBTotal15MinIntervalCrankbkForwdedToPrevPGCrankbkLvlTooHigh_Type = Counter32
_NncBTotal15MinIntervalCrankbkForwdedToPrevPGCrankbkLvlTooHigh_Object = MibTableColumn
nncBTotal15MinIntervalCrankbkForwdedToPrevPGCrankbkLvlTooHigh = _NncBTotal15MinIntervalCrankbkForwdedToPrevPGCrankbkLvlTooHigh_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 22, 1, 18),
    _NncBTotal15MinIntervalCrankbkForwdedToPrevPGCrankbkLvlTooHigh_Type()
)
nncBTotal15MinIntervalCrankbkForwdedToPrevPGCrankbkLvlTooHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal15MinIntervalCrankbkForwdedToPrevPGCrankbkLvlTooHigh.setStatus("current")
_NncRoutingStatsBorderTotal24HourCurrentTable_Object = MibTable
nncRoutingStatsBorderTotal24HourCurrentTable = _NncRoutingStatsBorderTotal24HourCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 23)
)
if mibBuilder.loadTexts:
    nncRoutingStatsBorderTotal24HourCurrentTable.setStatus("current")
_NncRoutingStatsBorderTotal24HourCurrentEntry_Object = MibTableRow
nncRoutingStatsBorderTotal24HourCurrentEntry = _NncRoutingStatsBorderTotal24HourCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 23, 1)
)
nncRoutingStatsBorderTotal24HourCurrentEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsBorderTotal24HourCurrentEntry.setStatus("current")
_NncBTotal24HourCurrentState_Type = NncExtIntvlStateType
_NncBTotal24HourCurrentState_Object = MibTableColumn
nncBTotal24HourCurrentState = _NncBTotal24HourCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 23, 1, 2),
    _NncBTotal24HourCurrentState_Type()
)
nncBTotal24HourCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourCurrentState.setStatus("current")
_NncBTotal24HourCurrentAbsoluteIntervalNumber_Type = Integer32
_NncBTotal24HourCurrentAbsoluteIntervalNumber_Object = MibTableColumn
nncBTotal24HourCurrentAbsoluteIntervalNumber = _NncBTotal24HourCurrentAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 23, 1, 3),
    _NncBTotal24HourCurrentAbsoluteIntervalNumber_Type()
)
nncBTotal24HourCurrentAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourCurrentAbsoluteIntervalNumber.setStatus("current")
_NncBTotal24HourCurrentFailedCallsDueToInitLowerLvlDTLNotGen_Type = Counter32
_NncBTotal24HourCurrentFailedCallsDueToInitLowerLvlDTLNotGen_Object = MibTableColumn
nncBTotal24HourCurrentFailedCallsDueToInitLowerLvlDTLNotGen = _NncBTotal24HourCurrentFailedCallsDueToInitLowerLvlDTLNotGen_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 23, 1, 4),
    _NncBTotal24HourCurrentFailedCallsDueToInitLowerLvlDTLNotGen_Type()
)
nncBTotal24HourCurrentFailedCallsDueToInitLowerLvlDTLNotGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourCurrentFailedCallsDueToInitLowerLvlDTLNotGen.setStatus("current")
_NncBTotal24HourCurrentCallsGeneratingInitLowerLvlDTLs_Type = Counter32
_NncBTotal24HourCurrentCallsGeneratingInitLowerLvlDTLs_Object = MibTableColumn
nncBTotal24HourCurrentCallsGeneratingInitLowerLvlDTLs = _NncBTotal24HourCurrentCallsGeneratingInitLowerLvlDTLs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 23, 1, 5),
    _NncBTotal24HourCurrentCallsGeneratingInitLowerLvlDTLs_Type()
)
nncBTotal24HourCurrentCallsGeneratingInitLowerLvlDTLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourCurrentCallsGeneratingInitLowerLvlDTLs.setStatus("current")
_NncBTotal24HourCurrentDTLGenCallsSuccessEstWithoutReroute_Type = Counter32
_NncBTotal24HourCurrentDTLGenCallsSuccessEstWithoutReroute_Object = MibTableColumn
nncBTotal24HourCurrentDTLGenCallsSuccessEstWithoutReroute = _NncBTotal24HourCurrentDTLGenCallsSuccessEstWithoutReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 23, 1, 6),
    _NncBTotal24HourCurrentDTLGenCallsSuccessEstWithoutReroute_Type()
)
nncBTotal24HourCurrentDTLGenCallsSuccessEstWithoutReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourCurrentDTLGenCallsSuccessEstWithoutReroute.setStatus("current")
_NncBTotal24HourCurrentDTLGenCallsSuccessEstWithReroute_Type = Counter32
_NncBTotal24HourCurrentDTLGenCallsSuccessEstWithReroute_Object = MibTableColumn
nncBTotal24HourCurrentDTLGenCallsSuccessEstWithReroute = _NncBTotal24HourCurrentDTLGenCallsSuccessEstWithReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 23, 1, 7),
    _NncBTotal24HourCurrentDTLGenCallsSuccessEstWithReroute_Type()
)
nncBTotal24HourCurrentDTLGenCallsSuccessEstWithReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourCurrentDTLGenCallsSuccessEstWithReroute.setStatus("current")
_NncBTotal24HourCurrentDTLGenCallsFailedInReRouting_Type = Counter32
_NncBTotal24HourCurrentDTLGenCallsFailedInReRouting_Object = MibTableColumn
nncBTotal24HourCurrentDTLGenCallsFailedInReRouting = _NncBTotal24HourCurrentDTLGenCallsFailedInReRouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 23, 1, 8),
    _NncBTotal24HourCurrentDTLGenCallsFailedInReRouting_Type()
)
nncBTotal24HourCurrentDTLGenCallsFailedInReRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourCurrentDTLGenCallsFailedInReRouting.setStatus("current")
_NncBTotal24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncBTotal24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncBTotal24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw = _NncBTotal24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 23, 1, 9),
    _NncBTotal24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw_Type()
)
nncBTotal24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncBTotal24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncBTotal24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncBTotal24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw = _NncBTotal24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 23, 1, 10),
    _NncBTotal24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw_Type()
)
nncBTotal24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncBTotal24HourCurrentCrankbackReceivedAsAnEntryBorderNode_Type = Counter32
_NncBTotal24HourCurrentCrankbackReceivedAsAnEntryBorderNode_Object = MibTableColumn
nncBTotal24HourCurrentCrankbackReceivedAsAnEntryBorderNode = _NncBTotal24HourCurrentCrankbackReceivedAsAnEntryBorderNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 23, 1, 11),
    _NncBTotal24HourCurrentCrankbackReceivedAsAnEntryBorderNode_Type()
)
nncBTotal24HourCurrentCrankbackReceivedAsAnEntryBorderNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourCurrentCrankbackReceivedAsAnEntryBorderNode.setStatus("current")
_NncBTotal24HourCurrentLowerLvlDTLsGenDueToRecdCrankback_Type = Counter32
_NncBTotal24HourCurrentLowerLvlDTLsGenDueToRecdCrankback_Object = MibTableColumn
nncBTotal24HourCurrentLowerLvlDTLsGenDueToRecdCrankback = _NncBTotal24HourCurrentLowerLvlDTLsGenDueToRecdCrankback_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 23, 1, 12),
    _NncBTotal24HourCurrentLowerLvlDTLsGenDueToRecdCrankback_Type()
)
nncBTotal24HourCurrentLowerLvlDTLsGenDueToRecdCrankback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourCurrentLowerLvlDTLsGenDueToRecdCrankback.setStatus("current")
_NncBTotal24HourCurrentCallsRecdOverAnOutsideLink_Type = Counter32
_NncBTotal24HourCurrentCallsRecdOverAnOutsideLink_Object = MibTableColumn
nncBTotal24HourCurrentCallsRecdOverAnOutsideLink = _NncBTotal24HourCurrentCallsRecdOverAnOutsideLink_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 23, 1, 13),
    _NncBTotal24HourCurrentCallsRecdOverAnOutsideLink_Type()
)
nncBTotal24HourCurrentCallsRecdOverAnOutsideLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourCurrentCallsRecdOverAnOutsideLink.setStatus("current")
_NncBTotal24HourCurrentCallsTransmittedOverAnOutsideLink_Type = Counter32
_NncBTotal24HourCurrentCallsTransmittedOverAnOutsideLink_Object = MibTableColumn
nncBTotal24HourCurrentCallsTransmittedOverAnOutsideLink = _NncBTotal24HourCurrentCallsTransmittedOverAnOutsideLink_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 23, 1, 14),
    _NncBTotal24HourCurrentCallsTransmittedOverAnOutsideLink_Type()
)
nncBTotal24HourCurrentCallsTransmittedOverAnOutsideLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourCurrentCallsTransmittedOverAnOutsideLink.setStatus("current")
_NncBTotal24HourCurrentCrankbksRecdOverAnOutsideLink_Type = Counter32
_NncBTotal24HourCurrentCrankbksRecdOverAnOutsideLink_Object = MibTableColumn
nncBTotal24HourCurrentCrankbksRecdOverAnOutsideLink = _NncBTotal24HourCurrentCrankbksRecdOverAnOutsideLink_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 23, 1, 15),
    _NncBTotal24HourCurrentCrankbksRecdOverAnOutsideLink_Type()
)
nncBTotal24HourCurrentCrankbksRecdOverAnOutsideLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourCurrentCrankbksRecdOverAnOutsideLink.setStatus("current")
_NncBTotal24HourCurrentSucdEndBlocCrankbksRecdOverOutsideLink_Type = Counter32
_NncBTotal24HourCurrentSucdEndBlocCrankbksRecdOverOutsideLink_Object = MibTableColumn
nncBTotal24HourCurrentSucdEndBlocCrankbksRecdOverOutsideLink = _NncBTotal24HourCurrentSucdEndBlocCrankbksRecdOverOutsideLink_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 23, 1, 16),
    _NncBTotal24HourCurrentSucdEndBlocCrankbksRecdOverOutsideLink_Type()
)
nncBTotal24HourCurrentSucdEndBlocCrankbksRecdOverOutsideLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourCurrentSucdEndBlocCrankbksRecdOverOutsideLink.setStatus("current")
_NncBTotal24HourCurrentCrankbkForwdedToPrevPGCrankbkLvlTooHigh_Type = Counter32
_NncBTotal24HourCurrentCrankbkForwdedToPrevPGCrankbkLvlTooHigh_Object = MibTableColumn
nncBTotal24HourCurrentCrankbkForwdedToPrevPGCrankbkLvlTooHigh = _NncBTotal24HourCurrentCrankbkForwdedToPrevPGCrankbkLvlTooHigh_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 23, 1, 17),
    _NncBTotal24HourCurrentCrankbkForwdedToPrevPGCrankbkLvlTooHigh_Type()
)
nncBTotal24HourCurrentCrankbkForwdedToPrevPGCrankbkLvlTooHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourCurrentCrankbkForwdedToPrevPGCrankbkLvlTooHigh.setStatus("current")
_NncRoutingStatsBorderTotal24HourIntervalTable_Object = MibTable
nncRoutingStatsBorderTotal24HourIntervalTable = _NncRoutingStatsBorderTotal24HourIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 24)
)
if mibBuilder.loadTexts:
    nncRoutingStatsBorderTotal24HourIntervalTable.setStatus("current")
_NncRoutingStatsBorderTotal24HourIntervalEntry_Object = MibTableRow
nncRoutingStatsBorderTotal24HourIntervalEntry = _NncRoutingStatsBorderTotal24HourIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 24, 1)
)
nncRoutingStatsBorderTotal24HourIntervalEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal24HourIntervalNumber"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsBorderTotal24HourIntervalEntry.setStatus("current")
_NncBTotal24HourIntervalNumber_Type = Integer32
_NncBTotal24HourIntervalNumber_Object = MibTableColumn
nncBTotal24HourIntervalNumber = _NncBTotal24HourIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 24, 1, 2),
    _NncBTotal24HourIntervalNumber_Type()
)
nncBTotal24HourIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncBTotal24HourIntervalNumber.setStatus("current")
_NncBTotal24HourIntervalState_Type = NncExtIntvlStateType
_NncBTotal24HourIntervalState_Object = MibTableColumn
nncBTotal24HourIntervalState = _NncBTotal24HourIntervalState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 24, 1, 3),
    _NncBTotal24HourIntervalState_Type()
)
nncBTotal24HourIntervalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourIntervalState.setStatus("current")
_NncBTotal24HourIntervalAbsoluteIntervalNumber_Type = Integer32
_NncBTotal24HourIntervalAbsoluteIntervalNumber_Object = MibTableColumn
nncBTotal24HourIntervalAbsoluteIntervalNumber = _NncBTotal24HourIntervalAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 24, 1, 4),
    _NncBTotal24HourIntervalAbsoluteIntervalNumber_Type()
)
nncBTotal24HourIntervalAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourIntervalAbsoluteIntervalNumber.setStatus("current")
_NncBTotal24HourIntervalFailedCallsDueToInitLowerLvlDTLNotGen_Type = Counter32
_NncBTotal24HourIntervalFailedCallsDueToInitLowerLvlDTLNotGen_Object = MibTableColumn
nncBTotal24HourIntervalFailedCallsDueToInitLowerLvlDTLNotGen = _NncBTotal24HourIntervalFailedCallsDueToInitLowerLvlDTLNotGen_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 24, 1, 5),
    _NncBTotal24HourIntervalFailedCallsDueToInitLowerLvlDTLNotGen_Type()
)
nncBTotal24HourIntervalFailedCallsDueToInitLowerLvlDTLNotGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourIntervalFailedCallsDueToInitLowerLvlDTLNotGen.setStatus("current")
_NncBTotal24HourIntervalCallsGeneratingInitLowerLvlDTLs_Type = Counter32
_NncBTotal24HourIntervalCallsGeneratingInitLowerLvlDTLs_Object = MibTableColumn
nncBTotal24HourIntervalCallsGeneratingInitLowerLvlDTLs = _NncBTotal24HourIntervalCallsGeneratingInitLowerLvlDTLs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 24, 1, 6),
    _NncBTotal24HourIntervalCallsGeneratingInitLowerLvlDTLs_Type()
)
nncBTotal24HourIntervalCallsGeneratingInitLowerLvlDTLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourIntervalCallsGeneratingInitLowerLvlDTLs.setStatus("current")
_NncBTotal24HourIntervalDTLGenCallsSuccessEstWithoutReroute_Type = Counter32
_NncBTotal24HourIntervalDTLGenCallsSuccessEstWithoutReroute_Object = MibTableColumn
nncBTotal24HourIntervalDTLGenCallsSuccessEstWithoutReroute = _NncBTotal24HourIntervalDTLGenCallsSuccessEstWithoutReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 24, 1, 7),
    _NncBTotal24HourIntervalDTLGenCallsSuccessEstWithoutReroute_Type()
)
nncBTotal24HourIntervalDTLGenCallsSuccessEstWithoutReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourIntervalDTLGenCallsSuccessEstWithoutReroute.setStatus("current")
_NncBTotal24HourIntervalDTLGenCallsSuccessEstWithReroute_Type = Counter32
_NncBTotal24HourIntervalDTLGenCallsSuccessEstWithReroute_Object = MibTableColumn
nncBTotal24HourIntervalDTLGenCallsSuccessEstWithReroute = _NncBTotal24HourIntervalDTLGenCallsSuccessEstWithReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 24, 1, 8),
    _NncBTotal24HourIntervalDTLGenCallsSuccessEstWithReroute_Type()
)
nncBTotal24HourIntervalDTLGenCallsSuccessEstWithReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourIntervalDTLGenCallsSuccessEstWithReroute.setStatus("current")
_NncBTotal24HourIntervalDTLGenCallsFailedInReRouting_Type = Counter32
_NncBTotal24HourIntervalDTLGenCallsFailedInReRouting_Object = MibTableColumn
nncBTotal24HourIntervalDTLGenCallsFailedInReRouting = _NncBTotal24HourIntervalDTLGenCallsFailedInReRouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 24, 1, 9),
    _NncBTotal24HourIntervalDTLGenCallsFailedInReRouting_Type()
)
nncBTotal24HourIntervalDTLGenCallsFailedInReRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourIntervalDTLGenCallsFailedInReRouting.setStatus("current")
_NncBTotal24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncBTotal24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncBTotal24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw = _NncBTotal24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 24, 1, 10),
    _NncBTotal24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw_Type()
)
nncBTotal24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncBTotal24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncBTotal24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncBTotal24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw = _NncBTotal24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 24, 1, 11),
    _NncBTotal24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw_Type()
)
nncBTotal24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncBTotal24HourIntervalCrankbackReceivedAsAnEntryBorderNode_Type = Counter32
_NncBTotal24HourIntervalCrankbackReceivedAsAnEntryBorderNode_Object = MibTableColumn
nncBTotal24HourIntervalCrankbackReceivedAsAnEntryBorderNode = _NncBTotal24HourIntervalCrankbackReceivedAsAnEntryBorderNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 24, 1, 12),
    _NncBTotal24HourIntervalCrankbackReceivedAsAnEntryBorderNode_Type()
)
nncBTotal24HourIntervalCrankbackReceivedAsAnEntryBorderNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourIntervalCrankbackReceivedAsAnEntryBorderNode.setStatus("current")
_NncBTotal24HourIntervalLowerLvlDTLsGenDueToRecdCrankback_Type = Counter32
_NncBTotal24HourIntervalLowerLvlDTLsGenDueToRecdCrankback_Object = MibTableColumn
nncBTotal24HourIntervalLowerLvlDTLsGenDueToRecdCrankback = _NncBTotal24HourIntervalLowerLvlDTLsGenDueToRecdCrankback_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 24, 1, 13),
    _NncBTotal24HourIntervalLowerLvlDTLsGenDueToRecdCrankback_Type()
)
nncBTotal24HourIntervalLowerLvlDTLsGenDueToRecdCrankback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourIntervalLowerLvlDTLsGenDueToRecdCrankback.setStatus("current")
_NncBTotal24HourIntervalCallsRecdOverAnOutsideLink_Type = Counter32
_NncBTotal24HourIntervalCallsRecdOverAnOutsideLink_Object = MibTableColumn
nncBTotal24HourIntervalCallsRecdOverAnOutsideLink = _NncBTotal24HourIntervalCallsRecdOverAnOutsideLink_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 24, 1, 14),
    _NncBTotal24HourIntervalCallsRecdOverAnOutsideLink_Type()
)
nncBTotal24HourIntervalCallsRecdOverAnOutsideLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourIntervalCallsRecdOverAnOutsideLink.setStatus("current")
_NncBTotal24HourIntervalCallsTransmittedOverAnOutsideLink_Type = Counter32
_NncBTotal24HourIntervalCallsTransmittedOverAnOutsideLink_Object = MibTableColumn
nncBTotal24HourIntervalCallsTransmittedOverAnOutsideLink = _NncBTotal24HourIntervalCallsTransmittedOverAnOutsideLink_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 24, 1, 15),
    _NncBTotal24HourIntervalCallsTransmittedOverAnOutsideLink_Type()
)
nncBTotal24HourIntervalCallsTransmittedOverAnOutsideLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourIntervalCallsTransmittedOverAnOutsideLink.setStatus("current")
_NncBTotal24HourIntervalCrankbksRecdOverAnOutsideLink_Type = Counter32
_NncBTotal24HourIntervalCrankbksRecdOverAnOutsideLink_Object = MibTableColumn
nncBTotal24HourIntervalCrankbksRecdOverAnOutsideLink = _NncBTotal24HourIntervalCrankbksRecdOverAnOutsideLink_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 24, 1, 16),
    _NncBTotal24HourIntervalCrankbksRecdOverAnOutsideLink_Type()
)
nncBTotal24HourIntervalCrankbksRecdOverAnOutsideLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourIntervalCrankbksRecdOverAnOutsideLink.setStatus("current")
_NncBTotal24HourIntervalSucdEndBlocCrankbksRecdOverOutsideLink_Type = Counter32
_NncBTotal24HourIntervalSucdEndBlocCrankbksRecdOverOutsideLink_Object = MibTableColumn
nncBTotal24HourIntervalSucdEndBlocCrankbksRecdOverOutsideLink = _NncBTotal24HourIntervalSucdEndBlocCrankbksRecdOverOutsideLink_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 24, 1, 17),
    _NncBTotal24HourIntervalSucdEndBlocCrankbksRecdOverOutsideLink_Type()
)
nncBTotal24HourIntervalSucdEndBlocCrankbksRecdOverOutsideLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourIntervalSucdEndBlocCrankbksRecdOverOutsideLink.setStatus("current")
_NncBTotal24HourIntervalCrankbkFwdToPrevPGCrankbkLvlTooHigh_Type = Counter32
_NncBTotal24HourIntervalCrankbkFwdToPrevPGCrankbkLvlTooHigh_Object = MibTableColumn
nncBTotal24HourIntervalCrankbkFwdToPrevPGCrankbkLvlTooHigh = _NncBTotal24HourIntervalCrankbkFwdToPrevPGCrankbkLvlTooHigh_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 24, 1, 18),
    _NncBTotal24HourIntervalCrankbkFwdToPrevPGCrankbkLvlTooHigh_Type()
)
nncBTotal24HourIntervalCrankbkFwdToPrevPGCrankbkLvlTooHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBTotal24HourIntervalCrankbkFwdToPrevPGCrankbkLvlTooHigh.setStatus("current")
_NncRoutingStatsRawCommonTable_Object = MibTable
nncRoutingStatsRawCommonTable = _NncRoutingStatsRawCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 25)
)
if mibBuilder.loadTexts:
    nncRoutingStatsRawCommonTable.setStatus("current")
_NncRoutingStatsRawCommonEntry_Object = MibTableRow
nncRoutingStatsRawCommonEntry = _NncRoutingStatsRawCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 25, 1)
)
nncRoutingStatsRawCommonEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsRawCommonEntry.setStatus("current")
_NncRoutingStatsRawCommonSuccessRoutedCallsOrigFromLocalSubs_Type = Counter32
_NncRoutingStatsRawCommonSuccessRoutedCallsOrigFromLocalSubs_Object = MibTableColumn
nncRoutingStatsRawCommonSuccessRoutedCallsOrigFromLocalSubs = _NncRoutingStatsRawCommonSuccessRoutedCallsOrigFromLocalSubs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 25, 1, 2),
    _NncRoutingStatsRawCommonSuccessRoutedCallsOrigFromLocalSubs_Type()
)
nncRoutingStatsRawCommonSuccessRoutedCallsOrigFromLocalSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRoutingStatsRawCommonSuccessRoutedCallsOrigFromLocalSubs.setStatus("current")
_NncRoutingStatsRawCommonSuccessRtedCallsTransitedViaThisNode_Type = Counter32
_NncRoutingStatsRawCommonSuccessRtedCallsTransitedViaThisNode_Object = MibTableColumn
nncRoutingStatsRawCommonSuccessRtedCallsTransitedViaThisNode = _NncRoutingStatsRawCommonSuccessRtedCallsTransitedViaThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 25, 1, 3),
    _NncRoutingStatsRawCommonSuccessRtedCallsTransitedViaThisNode_Type()
)
nncRoutingStatsRawCommonSuccessRtedCallsTransitedViaThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRoutingStatsRawCommonSuccessRtedCallsTransitedViaThisNode.setStatus("current")
_NncRoutingStatsRawCommonSuccessRoutedCallsTermToLocalSubs_Type = Counter32
_NncRoutingStatsRawCommonSuccessRoutedCallsTermToLocalSubs_Object = MibTableColumn
nncRoutingStatsRawCommonSuccessRoutedCallsTermToLocalSubs = _NncRoutingStatsRawCommonSuccessRoutedCallsTermToLocalSubs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 25, 1, 4),
    _NncRoutingStatsRawCommonSuccessRoutedCallsTermToLocalSubs_Type()
)
nncRoutingStatsRawCommonSuccessRoutedCallsTermToLocalSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRoutingStatsRawCommonSuccessRoutedCallsTermToLocalSubs.setStatus("current")
_NncRoutingStatsRawCommonSuccessRoutedLocalCalls_Type = Counter32
_NncRoutingStatsRawCommonSuccessRoutedLocalCalls_Object = MibTableColumn
nncRoutingStatsRawCommonSuccessRoutedLocalCalls = _NncRoutingStatsRawCommonSuccessRoutedLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 25, 1, 5),
    _NncRoutingStatsRawCommonSuccessRoutedLocalCalls_Type()
)
nncRoutingStatsRawCommonSuccessRoutedLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRoutingStatsRawCommonSuccessRoutedLocalCalls.setStatus("current")
_NncRoutingStatsRawCommonCallsOrigFromLocalCalls_Type = Counter32
_NncRoutingStatsRawCommonCallsOrigFromLocalCalls_Object = MibTableColumn
nncRoutingStatsRawCommonCallsOrigFromLocalCalls = _NncRoutingStatsRawCommonCallsOrigFromLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 25, 1, 6),
    _NncRoutingStatsRawCommonCallsOrigFromLocalCalls_Type()
)
nncRoutingStatsRawCommonCallsOrigFromLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRoutingStatsRawCommonCallsOrigFromLocalCalls.setStatus("current")
_NncRoutingStatsRawCommonCallsTermToLocalCalls_Type = Counter32
_NncRoutingStatsRawCommonCallsTermToLocalCalls_Object = MibTableColumn
nncRoutingStatsRawCommonCallsTermToLocalCalls = _NncRoutingStatsRawCommonCallsTermToLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 25, 1, 7),
    _NncRoutingStatsRawCommonCallsTermToLocalCalls_Type()
)
nncRoutingStatsRawCommonCallsTermToLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRoutingStatsRawCommonCallsTermToLocalCalls.setStatus("current")
_NncRoutingStatsRawCommonLocalCallAttempts_Type = Counter32
_NncRoutingStatsRawCommonLocalCallAttempts_Object = MibTableColumn
nncRoutingStatsRawCommonLocalCallAttempts = _NncRoutingStatsRawCommonLocalCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 25, 1, 8),
    _NncRoutingStatsRawCommonLocalCallAttempts_Type()
)
nncRoutingStatsRawCommonLocalCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRoutingStatsRawCommonLocalCallAttempts.setStatus("current")
_NncRoutingStatsRawCommonCallsClearedDueToNoRoutingTabEntry_Type = Counter32
_NncRoutingStatsRawCommonCallsClearedDueToNoRoutingTabEntry_Object = MibTableColumn
nncRoutingStatsRawCommonCallsClearedDueToNoRoutingTabEntry = _NncRoutingStatsRawCommonCallsClearedDueToNoRoutingTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 25, 1, 9),
    _NncRoutingStatsRawCommonCallsClearedDueToNoRoutingTabEntry_Type()
)
nncRoutingStatsRawCommonCallsClearedDueToNoRoutingTabEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRoutingStatsRawCommonCallsClearedDueToNoRoutingTabEntry.setStatus("current")
_NncRoutingStatsRawCommonCrankbacksGeneratedByThisNode_Type = Counter32
_NncRoutingStatsRawCommonCrankbacksGeneratedByThisNode_Object = MibTableColumn
nncRoutingStatsRawCommonCrankbacksGeneratedByThisNode = _NncRoutingStatsRawCommonCrankbacksGeneratedByThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 25, 1, 10),
    _NncRoutingStatsRawCommonCrankbacksGeneratedByThisNode_Type()
)
nncRoutingStatsRawCommonCrankbacksGeneratedByThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRoutingStatsRawCommonCrankbacksGeneratedByThisNode.setStatus("current")
_NncRoutingStatsRawCommonFailedCallsAtLocalSubs_Type = Counter32
_NncRoutingStatsRawCommonFailedCallsAtLocalSubs_Object = MibTableColumn
nncRoutingStatsRawCommonFailedCallsAtLocalSubs = _NncRoutingStatsRawCommonFailedCallsAtLocalSubs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 25, 1, 11),
    _NncRoutingStatsRawCommonFailedCallsAtLocalSubs_Type()
)
nncRoutingStatsRawCommonFailedCallsAtLocalSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRoutingStatsRawCommonFailedCallsAtLocalSubs.setStatus("current")
_NncRoutingStatsRawCommonCallsSuccessRerouted_Type = Counter32
_NncRoutingStatsRawCommonCallsSuccessRerouted_Object = MibTableColumn
nncRoutingStatsRawCommonCallsSuccessRerouted = _NncRoutingStatsRawCommonCallsSuccessRerouted_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 25, 1, 12),
    _NncRoutingStatsRawCommonCallsSuccessRerouted_Type()
)
nncRoutingStatsRawCommonCallsSuccessRerouted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRoutingStatsRawCommonCallsSuccessRerouted.setStatus("current")
_NncRoutingStatsRawCommonCallsFailedInRerouting_Type = Counter32
_NncRoutingStatsRawCommonCallsFailedInRerouting_Object = MibTableColumn
nncRoutingStatsRawCommonCallsFailedInRerouting = _NncRoutingStatsRawCommonCallsFailedInRerouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 25, 1, 13),
    _NncRoutingStatsRawCommonCallsFailedInRerouting_Type()
)
nncRoutingStatsRawCommonCallsFailedInRerouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRoutingStatsRawCommonCallsFailedInRerouting.setStatus("current")
_NncRoutingStatsRawSpecificTable_Object = MibTable
nncRoutingStatsRawSpecificTable = _NncRoutingStatsRawSpecificTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 26)
)
if mibBuilder.loadTexts:
    nncRoutingStatsRawSpecificTable.setStatus("current")
_NncRoutingStatsRawSpecificEntry_Object = MibTableRow
nncRoutingStatsRawSpecificEntry = _NncRoutingStatsRawSpecificEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 26, 1)
)
nncRoutingStatsRawSpecificEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsRawSpecificEntry.setStatus("current")
_NncRoutingStatsRawSpecificCallsStaticallyRoutedByThisNode_Type = Counter32
_NncRoutingStatsRawSpecificCallsStaticallyRoutedByThisNode_Object = MibTableColumn
nncRoutingStatsRawSpecificCallsStaticallyRoutedByThisNode = _NncRoutingStatsRawSpecificCallsStaticallyRoutedByThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 26, 1, 2),
    _NncRoutingStatsRawSpecificCallsStaticallyRoutedByThisNode_Type()
)
nncRoutingStatsRawSpecificCallsStaticallyRoutedByThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRoutingStatsRawSpecificCallsStaticallyRoutedByThisNode.setStatus("current")
_NncRoutingStatsRawSpecificCrankbacksReceivedByThisNode_Type = Counter32
_NncRoutingStatsRawSpecificCrankbacksReceivedByThisNode_Object = MibTableColumn
nncRoutingStatsRawSpecificCrankbacksReceivedByThisNode = _NncRoutingStatsRawSpecificCrankbacksReceivedByThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 26, 1, 3),
    _NncRoutingStatsRawSpecificCrankbacksReceivedByThisNode_Type()
)
nncRoutingStatsRawSpecificCrankbacksReceivedByThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRoutingStatsRawSpecificCrankbacksReceivedByThisNode.setStatus("current")
_NncRoutingStatsRawSpecificRerouteAttempts_Type = Counter32
_NncRoutingStatsRawSpecificRerouteAttempts_Object = MibTableColumn
nncRoutingStatsRawSpecificRerouteAttempts = _NncRoutingStatsRawSpecificRerouteAttempts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 26, 1, 4),
    _NncRoutingStatsRawSpecificRerouteAttempts_Type()
)
nncRoutingStatsRawSpecificRerouteAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRoutingStatsRawSpecificRerouteAttempts.setStatus("current")
_NncRoutingStatsRawSpecificRoutingLoopsDetectedByThisNode_Type = Counter32
_NncRoutingStatsRawSpecificRoutingLoopsDetectedByThisNode_Object = MibTableColumn
nncRoutingStatsRawSpecificRoutingLoopsDetectedByThisNode = _NncRoutingStatsRawSpecificRoutingLoopsDetectedByThisNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 26, 1, 5),
    _NncRoutingStatsRawSpecificRoutingLoopsDetectedByThisNode_Type()
)
nncRoutingStatsRawSpecificRoutingLoopsDetectedByThisNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRoutingStatsRawSpecificRoutingLoopsDetectedByThisNode.setStatus("current")
_NncRoutingStatsRawNonBorderPerTblTable_Object = MibTable
nncRoutingStatsRawNonBorderPerTblTable = _NncRoutingStatsRawNonBorderPerTblTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 27)
)
if mibBuilder.loadTexts:
    nncRoutingStatsRawNonBorderPerTblTable.setStatus("current")
_NncRoutingStatsRawNonBorderPerTblEntry_Object = MibTableRow
nncRoutingStatsRawNonBorderPerTblEntry = _NncRoutingStatsRawNonBorderPerTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 27, 1)
)
nncRoutingStatsRawNonBorderPerTblEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncRawNBPerTbleTableDescriptor"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsRawNonBorderPerTblEntry.setStatus("current")


class _NncRawNBPerTbleTableDescriptor_Type(Integer32):
    """Custom type nncRawNBPerTbleTableDescriptor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_NncRawNBPerTbleTableDescriptor_Type.__name__ = "Integer32"
_NncRawNBPerTbleTableDescriptor_Object = MibTableColumn
nncRawNBPerTbleTableDescriptor = _NncRawNBPerTbleTableDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 27, 1, 2),
    _NncRawNBPerTbleTableDescriptor_Type()
)
nncRawNBPerTbleTableDescriptor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncRawNBPerTbleTableDescriptor.setStatus("current")
_NncRawNBPerTbleFailedCallsDueToInitDTLNotGenerated_Type = Counter32
_NncRawNBPerTbleFailedCallsDueToInitDTLNotGenerated_Object = MibTableColumn
nncRawNBPerTbleFailedCallsDueToInitDTLNotGenerated = _NncRawNBPerTbleFailedCallsDueToInitDTLNotGenerated_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 27, 1, 3),
    _NncRawNBPerTbleFailedCallsDueToInitDTLNotGenerated_Type()
)
nncRawNBPerTbleFailedCallsDueToInitDTLNotGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawNBPerTbleFailedCallsDueToInitDTLNotGenerated.setStatus("current")
_NncRawNBPerTbleCallsGeneratingAnInitDTL_Type = Counter32
_NncRawNBPerTbleCallsGeneratingAnInitDTL_Object = MibTableColumn
nncRawNBPerTbleCallsGeneratingAnInitDTL = _NncRawNBPerTbleCallsGeneratingAnInitDTL_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 27, 1, 4),
    _NncRawNBPerTbleCallsGeneratingAnInitDTL_Type()
)
nncRawNBPerTbleCallsGeneratingAnInitDTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawNBPerTbleCallsGeneratingAnInitDTL.setStatus("current")
_NncRawNBPerTbleDTLOrigCallsSuccessEstWithoutReroute_Type = Counter32
_NncRawNBPerTbleDTLOrigCallsSuccessEstWithoutReroute_Object = MibTableColumn
nncRawNBPerTbleDTLOrigCallsSuccessEstWithoutReroute = _NncRawNBPerTbleDTLOrigCallsSuccessEstWithoutReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 27, 1, 5),
    _NncRawNBPerTbleDTLOrigCallsSuccessEstWithoutReroute_Type()
)
nncRawNBPerTbleDTLOrigCallsSuccessEstWithoutReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawNBPerTbleDTLOrigCallsSuccessEstWithoutReroute.setStatus("current")
_NncRawNBPerTbleDTLOrigCallsSuccessEstWithReroute_Type = Counter32
_NncRawNBPerTbleDTLOrigCallsSuccessEstWithReroute_Object = MibTableColumn
nncRawNBPerTbleDTLOrigCallsSuccessEstWithReroute = _NncRawNBPerTbleDTLOrigCallsSuccessEstWithReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 27, 1, 6),
    _NncRawNBPerTbleDTLOrigCallsSuccessEstWithReroute_Type()
)
nncRawNBPerTbleDTLOrigCallsSuccessEstWithReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawNBPerTbleDTLOrigCallsSuccessEstWithReroute.setStatus("current")
_NncRawNBPerTbleDTLOrigCallsFailedInReRouting_Type = Counter32
_NncRawNBPerTbleDTLOrigCallsFailedInReRouting_Object = MibTableColumn
nncRawNBPerTbleDTLOrigCallsFailedInReRouting = _NncRawNBPerTbleDTLOrigCallsFailedInReRouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 27, 1, 7),
    _NncRawNBPerTbleDTLOrigCallsFailedInReRouting_Type()
)
nncRawNBPerTbleDTLOrigCallsFailedInReRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawNBPerTbleDTLOrigCallsFailedInReRouting.setStatus("current")
_NncRawNBPerTbleSuccessCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncRawNBPerTbleSuccessCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncRawNBPerTbleSuccessCallsBdwGreaterThanRTDMinBdw = _NncRawNBPerTbleSuccessCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 27, 1, 8),
    _NncRawNBPerTbleSuccessCallsBdwGreaterThanRTDMinBdw_Type()
)
nncRawNBPerTbleSuccessCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawNBPerTbleSuccessCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncRawNBPerTbleFailedCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncRawNBPerTbleFailedCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncRawNBPerTbleFailedCallsBdwGreaterThanRTDMinBdw = _NncRawNBPerTbleFailedCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 27, 1, 9),
    _NncRawNBPerTbleFailedCallsBdwGreaterThanRTDMinBdw_Type()
)
nncRawNBPerTbleFailedCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawNBPerTbleFailedCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncRawNBPerTbleCrankbackReceivedAsDTLOriginator_Type = Counter32
_NncRawNBPerTbleCrankbackReceivedAsDTLOriginator_Object = MibTableColumn
nncRawNBPerTbleCrankbackReceivedAsDTLOriginator = _NncRawNBPerTbleCrankbackReceivedAsDTLOriginator_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 27, 1, 10),
    _NncRawNBPerTbleCrankbackReceivedAsDTLOriginator_Type()
)
nncRawNBPerTbleCrankbackReceivedAsDTLOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawNBPerTbleCrankbackReceivedAsDTLOriginator.setStatus("current")
_NncRawNBPerTbleDTLsGeneratedDueToCrankback_Type = Counter32
_NncRawNBPerTbleDTLsGeneratedDueToCrankback_Object = MibTableColumn
nncRawNBPerTbleDTLsGeneratedDueToCrankback = _NncRawNBPerTbleDTLsGeneratedDueToCrankback_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 27, 1, 11),
    _NncRawNBPerTbleDTLsGeneratedDueToCrankback_Type()
)
nncRawNBPerTbleDTLsGeneratedDueToCrankback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawNBPerTbleDTLsGeneratedDueToCrankback.setStatus("current")
_NncRoutingStatsRawBorderPerTblTable_Object = MibTable
nncRoutingStatsRawBorderPerTblTable = _NncRoutingStatsRawBorderPerTblTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 28)
)
if mibBuilder.loadTexts:
    nncRoutingStatsRawBorderPerTblTable.setStatus("current")
_NncRoutingStatsRawBorderPerTblEntry_Object = MibTableRow
nncRoutingStatsRawBorderPerTblEntry = _NncRoutingStatsRawBorderPerTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 28, 1)
)
nncRoutingStatsRawBorderPerTblEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncRawBPerTblTableDescriptor"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsRawBorderPerTblEntry.setStatus("current")


class _NncRawBPerTblTableDescriptor_Type(Integer32):
    """Custom type nncRawBPerTblTableDescriptor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_NncRawBPerTblTableDescriptor_Type.__name__ = "Integer32"
_NncRawBPerTblTableDescriptor_Object = MibTableColumn
nncRawBPerTblTableDescriptor = _NncRawBPerTblTableDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 28, 1, 2),
    _NncRawBPerTblTableDescriptor_Type()
)
nncRawBPerTblTableDescriptor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncRawBPerTblTableDescriptor.setStatus("current")
_NncRawBPerTblFailedCallsDueInitLowerLvlDTLsNotGen_Type = Counter32
_NncRawBPerTblFailedCallsDueInitLowerLvlDTLsNotGen_Object = MibTableColumn
nncRawBPerTblFailedCallsDueInitLowerLvlDTLsNotGen = _NncRawBPerTblFailedCallsDueInitLowerLvlDTLsNotGen_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 28, 1, 3),
    _NncRawBPerTblFailedCallsDueInitLowerLvlDTLsNotGen_Type()
)
nncRawBPerTblFailedCallsDueInitLowerLvlDTLsNotGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawBPerTblFailedCallsDueInitLowerLvlDTLsNotGen.setStatus("current")
_NncRawBPerTblCallsGeneratingInitLowerLvlDTLs_Type = Counter32
_NncRawBPerTblCallsGeneratingInitLowerLvlDTLs_Object = MibTableColumn
nncRawBPerTblCallsGeneratingInitLowerLvlDTLs = _NncRawBPerTblCallsGeneratingInitLowerLvlDTLs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 28, 1, 4),
    _NncRawBPerTblCallsGeneratingInitLowerLvlDTLs_Type()
)
nncRawBPerTblCallsGeneratingInitLowerLvlDTLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawBPerTblCallsGeneratingInitLowerLvlDTLs.setStatus("current")
_NncRawBPerTblDTLGenCallsSuccessEstWithoutReroute_Type = Counter32
_NncRawBPerTblDTLGenCallsSuccessEstWithoutReroute_Object = MibTableColumn
nncRawBPerTblDTLGenCallsSuccessEstWithoutReroute = _NncRawBPerTblDTLGenCallsSuccessEstWithoutReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 28, 1, 5),
    _NncRawBPerTblDTLGenCallsSuccessEstWithoutReroute_Type()
)
nncRawBPerTblDTLGenCallsSuccessEstWithoutReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawBPerTblDTLGenCallsSuccessEstWithoutReroute.setStatus("current")
_NncRawBPerTblDTLGenCallsSuccessEstWithReroute_Type = Counter32
_NncRawBPerTblDTLGenCallsSuccessEstWithReroute_Object = MibTableColumn
nncRawBPerTblDTLGenCallsSuccessEstWithReroute = _NncRawBPerTblDTLGenCallsSuccessEstWithReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 28, 1, 6),
    _NncRawBPerTblDTLGenCallsSuccessEstWithReroute_Type()
)
nncRawBPerTblDTLGenCallsSuccessEstWithReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawBPerTblDTLGenCallsSuccessEstWithReroute.setStatus("current")
_NncRawBPerTblDTLGenCallsFailedInReRouting_Type = Counter32
_NncRawBPerTblDTLGenCallsFailedInReRouting_Object = MibTableColumn
nncRawBPerTblDTLGenCallsFailedInReRouting = _NncRawBPerTblDTLGenCallsFailedInReRouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 28, 1, 7),
    _NncRawBPerTblDTLGenCallsFailedInReRouting_Type()
)
nncRawBPerTblDTLGenCallsFailedInReRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawBPerTblDTLGenCallsFailedInReRouting.setStatus("current")
_NncRawBPerTblSuccessCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncRawBPerTblSuccessCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncRawBPerTblSuccessCallsBdwGreaterThanRTDMinBdw = _NncRawBPerTblSuccessCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 28, 1, 8),
    _NncRawBPerTblSuccessCallsBdwGreaterThanRTDMinBdw_Type()
)
nncRawBPerTblSuccessCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawBPerTblSuccessCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncRawBPerTblFailedCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncRawBPerTblFailedCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncRawBPerTblFailedCallsBdwGreaterThanRTDMinBdw = _NncRawBPerTblFailedCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 28, 1, 9),
    _NncRawBPerTblFailedCallsBdwGreaterThanRTDMinBdw_Type()
)
nncRawBPerTblFailedCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawBPerTblFailedCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncRawBPerTblCrankbackReceivedAsAnEntryBorderNode_Type = Counter32
_NncRawBPerTblCrankbackReceivedAsAnEntryBorderNode_Object = MibTableColumn
nncRawBPerTblCrankbackReceivedAsAnEntryBorderNode = _NncRawBPerTblCrankbackReceivedAsAnEntryBorderNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 28, 1, 10),
    _NncRawBPerTblCrankbackReceivedAsAnEntryBorderNode_Type()
)
nncRawBPerTblCrankbackReceivedAsAnEntryBorderNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawBPerTblCrankbackReceivedAsAnEntryBorderNode.setStatus("current")
_NncRawBPerTblLowerLvlDTLsGenDueToRecdCrankback_Type = Counter32
_NncRawBPerTblLowerLvlDTLsGenDueToRecdCrankback_Object = MibTableColumn
nncRawBPerTblLowerLvlDTLsGenDueToRecdCrankback = _NncRawBPerTblLowerLvlDTLsGenDueToRecdCrankback_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 28, 1, 11),
    _NncRawBPerTblLowerLvlDTLsGenDueToRecdCrankback_Type()
)
nncRawBPerTblLowerLvlDTLsGenDueToRecdCrankback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawBPerTblLowerLvlDTLsGenDueToRecdCrankback.setStatus("current")
_NncRoutingStatsRawNonBorderTotalTable_Object = MibTable
nncRoutingStatsRawNonBorderTotalTable = _NncRoutingStatsRawNonBorderTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 29)
)
if mibBuilder.loadTexts:
    nncRoutingStatsRawNonBorderTotalTable.setStatus("current")
_NncRoutingStatsRawNonBorderTotalEntry_Object = MibTableRow
nncRoutingStatsRawNonBorderTotalEntry = _NncRoutingStatsRawNonBorderTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 29, 1)
)
nncRoutingStatsRawNonBorderTotalEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsRawNonBorderTotalEntry.setStatus("current")
_NncRawNBTotalFailedCallsDueToInitDTLNotGenerated_Type = Counter32
_NncRawNBTotalFailedCallsDueToInitDTLNotGenerated_Object = MibTableColumn
nncRawNBTotalFailedCallsDueToInitDTLNotGenerated = _NncRawNBTotalFailedCallsDueToInitDTLNotGenerated_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 29, 1, 2),
    _NncRawNBTotalFailedCallsDueToInitDTLNotGenerated_Type()
)
nncRawNBTotalFailedCallsDueToInitDTLNotGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawNBTotalFailedCallsDueToInitDTLNotGenerated.setStatus("current")
_NncRawNBTotalCallsGeneratingAnInitDTL_Type = Counter32
_NncRawNBTotalCallsGeneratingAnInitDTL_Object = MibTableColumn
nncRawNBTotalCallsGeneratingAnInitDTL = _NncRawNBTotalCallsGeneratingAnInitDTL_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 29, 1, 3),
    _NncRawNBTotalCallsGeneratingAnInitDTL_Type()
)
nncRawNBTotalCallsGeneratingAnInitDTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawNBTotalCallsGeneratingAnInitDTL.setStatus("current")
_NncRawNBTotalDTLOrigCallsSuccessEstWithoutReroute_Type = Counter32
_NncRawNBTotalDTLOrigCallsSuccessEstWithoutReroute_Object = MibTableColumn
nncRawNBTotalDTLOrigCallsSuccessEstWithoutReroute = _NncRawNBTotalDTLOrigCallsSuccessEstWithoutReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 29, 1, 4),
    _NncRawNBTotalDTLOrigCallsSuccessEstWithoutReroute_Type()
)
nncRawNBTotalDTLOrigCallsSuccessEstWithoutReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawNBTotalDTLOrigCallsSuccessEstWithoutReroute.setStatus("current")
_NncRawNBTotalDTLOrigCallsSuccessEstWithReroute_Type = Counter32
_NncRawNBTotalDTLOrigCallsSuccessEstWithReroute_Object = MibTableColumn
nncRawNBTotalDTLOrigCallsSuccessEstWithReroute = _NncRawNBTotalDTLOrigCallsSuccessEstWithReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 29, 1, 5),
    _NncRawNBTotalDTLOrigCallsSuccessEstWithReroute_Type()
)
nncRawNBTotalDTLOrigCallsSuccessEstWithReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawNBTotalDTLOrigCallsSuccessEstWithReroute.setStatus("current")
_NncRawNBTotalDTLOrigCallsFailedInReRouting_Type = Counter32
_NncRawNBTotalDTLOrigCallsFailedInReRouting_Object = MibTableColumn
nncRawNBTotalDTLOrigCallsFailedInReRouting = _NncRawNBTotalDTLOrigCallsFailedInReRouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 29, 1, 6),
    _NncRawNBTotalDTLOrigCallsFailedInReRouting_Type()
)
nncRawNBTotalDTLOrigCallsFailedInReRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawNBTotalDTLOrigCallsFailedInReRouting.setStatus("current")
_NncRawNBTotalSuccessCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncRawNBTotalSuccessCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncRawNBTotalSuccessCallsBdwGreaterThanRTDMinBdw = _NncRawNBTotalSuccessCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 29, 1, 7),
    _NncRawNBTotalSuccessCallsBdwGreaterThanRTDMinBdw_Type()
)
nncRawNBTotalSuccessCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawNBTotalSuccessCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncRawNBTotalFailedCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncRawNBTotalFailedCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncRawNBTotalFailedCallsBdwGreaterThanRTDMinBdw = _NncRawNBTotalFailedCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 29, 1, 8),
    _NncRawNBTotalFailedCallsBdwGreaterThanRTDMinBdw_Type()
)
nncRawNBTotalFailedCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawNBTotalFailedCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncRawNBTotalCrankbackReceivedAsDTLOriginator_Type = Counter32
_NncRawNBTotalCrankbackReceivedAsDTLOriginator_Object = MibTableColumn
nncRawNBTotalCrankbackReceivedAsDTLOriginator = _NncRawNBTotalCrankbackReceivedAsDTLOriginator_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 29, 1, 9),
    _NncRawNBTotalCrankbackReceivedAsDTLOriginator_Type()
)
nncRawNBTotalCrankbackReceivedAsDTLOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawNBTotalCrankbackReceivedAsDTLOriginator.setStatus("current")
_NncRawNBTotalDTLsGeneratedDueToCrankback_Type = Counter32
_NncRawNBTotalDTLsGeneratedDueToCrankback_Object = MibTableColumn
nncRawNBTotalDTLsGeneratedDueToCrankback = _NncRawNBTotalDTLsGeneratedDueToCrankback_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 29, 1, 10),
    _NncRawNBTotalDTLsGeneratedDueToCrankback_Type()
)
nncRawNBTotalDTLsGeneratedDueToCrankback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawNBTotalDTLsGeneratedDueToCrankback.setStatus("current")
_NncRawNBTotalCallsRecdAsTransitNodeOverInsideLinks_Type = Counter32
_NncRawNBTotalCallsRecdAsTransitNodeOverInsideLinks_Object = MibTableColumn
nncRawNBTotalCallsRecdAsTransitNodeOverInsideLinks = _NncRawNBTotalCallsRecdAsTransitNodeOverInsideLinks_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 29, 1, 11),
    _NncRawNBTotalCallsRecdAsTransitNodeOverInsideLinks_Type()
)
nncRawNBTotalCallsRecdAsTransitNodeOverInsideLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawNBTotalCallsRecdAsTransitNodeOverInsideLinks.setStatus("current")
_NncRawNBTotalCrnkbksRecdAsTransitNodeOvInsideLnks_Type = Counter32
_NncRawNBTotalCrnkbksRecdAsTransitNodeOvInsideLnks_Object = MibTableColumn
nncRawNBTotalCrnkbksRecdAsTransitNodeOvInsideLnks = _NncRawNBTotalCrnkbksRecdAsTransitNodeOvInsideLnks_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 29, 1, 12),
    _NncRawNBTotalCrnkbksRecdAsTransitNodeOvInsideLnks_Type()
)
nncRawNBTotalCrnkbksRecdAsTransitNodeOvInsideLnks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawNBTotalCrnkbksRecdAsTransitNodeOvInsideLnks.setStatus("current")
_NncRawNBTotalSucdEndBlocCrnkbksRecdOvInsideLnks_Type = Counter32
_NncRawNBTotalSucdEndBlocCrnkbksRecdOvInsideLnks_Object = MibTableColumn
nncRawNBTotalSucdEndBlocCrnkbksRecdOvInsideLnks = _NncRawNBTotalSucdEndBlocCrnkbksRecdOvInsideLnks_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 29, 1, 13),
    _NncRawNBTotalSucdEndBlocCrnkbksRecdOvInsideLnks_Type()
)
nncRawNBTotalSucdEndBlocCrnkbksRecdOvInsideLnks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawNBTotalSucdEndBlocCrnkbksRecdOvInsideLnks.setStatus("current")
_NncRoutingStatsRawBorderTotalTable_Object = MibTable
nncRoutingStatsRawBorderTotalTable = _NncRoutingStatsRawBorderTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 30)
)
if mibBuilder.loadTexts:
    nncRoutingStatsRawBorderTotalTable.setStatus("current")
_NncRoutingStatsRawBorderTotalEntry_Object = MibTableRow
nncRoutingStatsRawBorderTotalEntry = _NncRoutingStatsRawBorderTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 30, 1)
)
nncRoutingStatsRawBorderTotalEntry.setIndexNames(
    (0, "NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
)
if mibBuilder.loadTexts:
    nncRoutingStatsRawBorderTotalEntry.setStatus("current")
_NncRawBTotalFailedCallsDueToInitLowerLvlDTLNotGen_Type = Counter32
_NncRawBTotalFailedCallsDueToInitLowerLvlDTLNotGen_Object = MibTableColumn
nncRawBTotalFailedCallsDueToInitLowerLvlDTLNotGen = _NncRawBTotalFailedCallsDueToInitLowerLvlDTLNotGen_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 30, 1, 2),
    _NncRawBTotalFailedCallsDueToInitLowerLvlDTLNotGen_Type()
)
nncRawBTotalFailedCallsDueToInitLowerLvlDTLNotGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawBTotalFailedCallsDueToInitLowerLvlDTLNotGen.setStatus("current")
_NncRawBTotalCallsGeneratingInitLowerLvlDTLs_Type = Counter32
_NncRawBTotalCallsGeneratingInitLowerLvlDTLs_Object = MibTableColumn
nncRawBTotalCallsGeneratingInitLowerLvlDTLs = _NncRawBTotalCallsGeneratingInitLowerLvlDTLs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 30, 1, 3),
    _NncRawBTotalCallsGeneratingInitLowerLvlDTLs_Type()
)
nncRawBTotalCallsGeneratingInitLowerLvlDTLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawBTotalCallsGeneratingInitLowerLvlDTLs.setStatus("current")
_NncRawBTotalDTLGenCallsSuccessEstWithoutReroute_Type = Counter32
_NncRawBTotalDTLGenCallsSuccessEstWithoutReroute_Object = MibTableColumn
nncRawBTotalDTLGenCallsSuccessEstWithoutReroute = _NncRawBTotalDTLGenCallsSuccessEstWithoutReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 30, 1, 4),
    _NncRawBTotalDTLGenCallsSuccessEstWithoutReroute_Type()
)
nncRawBTotalDTLGenCallsSuccessEstWithoutReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawBTotalDTLGenCallsSuccessEstWithoutReroute.setStatus("current")
_NncRawBTotalDTLGenCallsSuccessEstWithReroute_Type = Counter32
_NncRawBTotalDTLGenCallsSuccessEstWithReroute_Object = MibTableColumn
nncRawBTotalDTLGenCallsSuccessEstWithReroute = _NncRawBTotalDTLGenCallsSuccessEstWithReroute_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 30, 1, 5),
    _NncRawBTotalDTLGenCallsSuccessEstWithReroute_Type()
)
nncRawBTotalDTLGenCallsSuccessEstWithReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawBTotalDTLGenCallsSuccessEstWithReroute.setStatus("current")
_NncRawBTotalDTLGenCallsFailedInReRouting_Type = Counter32
_NncRawBTotalDTLGenCallsFailedInReRouting_Object = MibTableColumn
nncRawBTotalDTLGenCallsFailedInReRouting = _NncRawBTotalDTLGenCallsFailedInReRouting_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 30, 1, 6),
    _NncRawBTotalDTLGenCallsFailedInReRouting_Type()
)
nncRawBTotalDTLGenCallsFailedInReRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawBTotalDTLGenCallsFailedInReRouting.setStatus("current")
_NncRawBTotalSuccessCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncRawBTotalSuccessCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncRawBTotalSuccessCallsBdwGreaterThanRTDMinBdw = _NncRawBTotalSuccessCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 30, 1, 7),
    _NncRawBTotalSuccessCallsBdwGreaterThanRTDMinBdw_Type()
)
nncRawBTotalSuccessCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawBTotalSuccessCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncRawBTotalFailedCallsBdwGreaterThanRTDMinBdw_Type = Counter32
_NncRawBTotalFailedCallsBdwGreaterThanRTDMinBdw_Object = MibTableColumn
nncRawBTotalFailedCallsBdwGreaterThanRTDMinBdw = _NncRawBTotalFailedCallsBdwGreaterThanRTDMinBdw_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 30, 1, 8),
    _NncRawBTotalFailedCallsBdwGreaterThanRTDMinBdw_Type()
)
nncRawBTotalFailedCallsBdwGreaterThanRTDMinBdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawBTotalFailedCallsBdwGreaterThanRTDMinBdw.setStatus("current")
_NncRawBTotalCrankbackReceivedAsAnEntryBorderNode_Type = Counter32
_NncRawBTotalCrankbackReceivedAsAnEntryBorderNode_Object = MibTableColumn
nncRawBTotalCrankbackReceivedAsAnEntryBorderNode = _NncRawBTotalCrankbackReceivedAsAnEntryBorderNode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 30, 1, 9),
    _NncRawBTotalCrankbackReceivedAsAnEntryBorderNode_Type()
)
nncRawBTotalCrankbackReceivedAsAnEntryBorderNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawBTotalCrankbackReceivedAsAnEntryBorderNode.setStatus("current")
_NncRawBTotalLowerLvlDTLsGenDueToRecdCrankback_Type = Counter32
_NncRawBTotalLowerLvlDTLsGenDueToRecdCrankback_Object = MibTableColumn
nncRawBTotalLowerLvlDTLsGenDueToRecdCrankback = _NncRawBTotalLowerLvlDTLsGenDueToRecdCrankback_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 30, 1, 10),
    _NncRawBTotalLowerLvlDTLsGenDueToRecdCrankback_Type()
)
nncRawBTotalLowerLvlDTLsGenDueToRecdCrankback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawBTotalLowerLvlDTLsGenDueToRecdCrankback.setStatus("current")
_NncRawBTotalCallsRecdOverAnOutsideLink_Type = Counter32
_NncRawBTotalCallsRecdOverAnOutsideLink_Object = MibTableColumn
nncRawBTotalCallsRecdOverAnOutsideLink = _NncRawBTotalCallsRecdOverAnOutsideLink_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 30, 1, 11),
    _NncRawBTotalCallsRecdOverAnOutsideLink_Type()
)
nncRawBTotalCallsRecdOverAnOutsideLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawBTotalCallsRecdOverAnOutsideLink.setStatus("current")
_NncRawBTotalCallsTransmittedOverAnOutsideLink_Type = Counter32
_NncRawBTotalCallsTransmittedOverAnOutsideLink_Object = MibTableColumn
nncRawBTotalCallsTransmittedOverAnOutsideLink = _NncRawBTotalCallsTransmittedOverAnOutsideLink_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 30, 1, 12),
    _NncRawBTotalCallsTransmittedOverAnOutsideLink_Type()
)
nncRawBTotalCallsTransmittedOverAnOutsideLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawBTotalCallsTransmittedOverAnOutsideLink.setStatus("current")
_NncRawBTotalCrankbksRecdOverAnOutsideLink_Type = Counter32
_NncRawBTotalCrankbksRecdOverAnOutsideLink_Object = MibTableColumn
nncRawBTotalCrankbksRecdOverAnOutsideLink = _NncRawBTotalCrankbksRecdOverAnOutsideLink_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 30, 1, 13),
    _NncRawBTotalCrankbksRecdOverAnOutsideLink_Type()
)
nncRawBTotalCrankbksRecdOverAnOutsideLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawBTotalCrankbksRecdOverAnOutsideLink.setStatus("current")
_NncRawBTotalSucdEndBlocCrankbksRecdOverOutsideLink_Type = Counter32
_NncRawBTotalSucdEndBlocCrankbksRecdOverOutsideLink_Object = MibTableColumn
nncRawBTotalSucdEndBlocCrankbksRecdOverOutsideLink = _NncRawBTotalSucdEndBlocCrankbksRecdOverOutsideLink_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 30, 1, 14),
    _NncRawBTotalSucdEndBlocCrankbksRecdOverOutsideLink_Type()
)
nncRawBTotalSucdEndBlocCrankbksRecdOverOutsideLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawBTotalSucdEndBlocCrankbksRecdOverOutsideLink.setStatus("current")
_NncRawBTotalCrankbkForwdedToPrevPGCrankbkLvlTooHigh_Type = Counter32
_NncRawBTotalCrankbkForwdedToPrevPGCrankbkLvlTooHigh_Object = MibTableColumn
nncRawBTotalCrankbkForwdedToPrevPGCrankbkLvlTooHigh = _NncRawBTotalCrankbkForwdedToPrevPGCrankbkLvlTooHigh_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 1, 30, 1, 15),
    _NncRawBTotalCrankbkForwdedToPrevPGCrankbkLvlTooHigh_Type()
)
nncRawBTotalCrankbkForwdedToPrevPGCrankbkLvlTooHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncRawBTotalCrankbkForwdedToPrevPGCrankbkLvlTooHigh.setStatus("current")
_NncRoutingStatsGroups_ObjectIdentity = ObjectIdentity
nncRoutingStatsGroups = _NncRoutingStatsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3)
)
_NncRoutingStatsCompliances_ObjectIdentity = ObjectIdentity
nncRoutingStatsCompliances = _NncRoutingStatsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 4)
)

# Managed Objects groups

nncRoutingStatsCommon15MinCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 1)
)
nncRoutingStatsCommon15MinCurrentGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncCallControlGroupNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinCurrentAbsoluteIntervalNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinCurrentSuccessRoutedCallsOrigFromLocalSubs"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinCurrentSuccessRoutedCallsTransitedViaThisNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinCurrentSuccessRoutedCallsTermToLocalSubs"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinCurrentSuccessRoutedLocalCalls"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinCurrentCallsOrigFromLocalCalls"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinCurrentCallsTermToLocalCalls"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinCurrentLocalCallAttempts"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinCurrentCallsClearedDueToNoRoutingTabEntry"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinCurrentCrankbacksGeneratedByThisNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinCurrentFailedCallsAtLocalSubs"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinCurrentCallsSuccessRerouted"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinCurrentCallsFailedInRerouting"))
)
if mibBuilder.loadTexts:
    nncRoutingStatsCommon15MinCurrentGroup.setStatus("current")

nncRoutingStatsCommon15MinIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 2)
)
nncRoutingStatsCommon15MinIntervalGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinIntervalAbsoluteIntervalNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinIntervalSuccessRoutedCallsOrigFromLocalSubs"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinIntervalSuccessRoutedCallsTransitedViaThisNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinIntervalSuccessRoutedCallsTermToLocalSubs"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinIntervalSuccessRoutedLocalCalls"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinIntervalCallsOrigFromLocalCalls"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinIntervalCallsTermToLocalCalls"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinIntervalLocalCallAttempts"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinIntervalCallsClearedDueToNoRoutingTabEntry"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinIntervalCrankbacksGeneratedByThisNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinIntervalFailedCallsAtLocalSubs"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinIntervalCallsSuccessRerouted"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon15MinIntervalCallsFailedInRerouting"))
)
if mibBuilder.loadTexts:
    nncRoutingStatsCommon15MinIntervalGroup.setStatus("current")

nncRoutingStatsCommon24HourCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 3)
)
nncRoutingStatsCommon24HourCurrentGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourCurrentAbsoluteIntervalNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourCurrentSuccessRoutedCallsOrigFromLocalSubs"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourCurrentSuccessRoutedCallsTransitedViaThisNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourCurrentSuccessRoutedCallsTermToLocalSubs"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourCurrentSuccessRoutedLocalCalls"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourCurrentCallsOrigFromLocalCalls"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourCurrentCallsTermToLocalCalls"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourCurrentLocalCallAttempts"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourCurrentCallsClearedDueToNoRoutingTabEntry"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourCurrentCrankbacksGeneratedByThisNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourCurrentFailedCallsAtLocalSubs"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourCurrentCallsSuccessRerouted"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourCurrentCallsFailedInRerouting"))
)
if mibBuilder.loadTexts:
    nncRoutingStatsCommon24HourCurrentGroup.setStatus("current")

nncRoutingStatsCommon24HourIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 4)
)
nncRoutingStatsCommon24HourIntervalGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourIntervalAbsoluteIntervalNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourIntervalSuccessRoutedCallsOrigFromLocalSubs"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourIntervalSuccessRoutedCallsTransitedViaThisNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourIntervalSuccessRoutedCallsTermToLocalSubs"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourIntervalSuccessRoutedLocalCalls"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourIntervalCallsOrigFromLocalCalls"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourIntervalCallsTermToLocalCalls"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourIntervalLocalCallAttempts"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourIntervalCallsClearedDueToNoRoutingTabEntry"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourIntervalCrankbacksGeneratedByThisNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourIntervalFailedCallsAtLocalSubs"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourIntervalCallsSuccessRerouted"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncCommon24HourIntervalCallsFailedInRerouting"))
)
if mibBuilder.loadTexts:
    nncRoutingStatsCommon24HourIntervalGroup.setStatus("current")

nncRoutingStatsSpecific15MinCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 5)
)
nncRoutingStatsSpecific15MinCurrentGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncSpecific15MinCurrentAbsoluteIntervalNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncSpecific15MinCurrentCallsStaticallyRoutedByThisNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncSpecific15MinCurrentCrankbacksReceivedByThisNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncSpecific15MinCurrentRerouteAttempts"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncSpecific15MinCurrentRoutingLoopsDetectedByThisNode"))
)
if mibBuilder.loadTexts:
    nncRoutingStatsSpecific15MinCurrentGroup.setStatus("current")

nncRoutingStatsSpecific15MinIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 6)
)
nncRoutingStatsSpecific15MinIntervalGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncSpecific15MinIntervalAbsoluteIntervalNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncSpecific15MinIntervalCallsStaticallyRoutedByThisNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncSpecific15MinIntervalCrankbacksReceivedByThisNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncSpecific15MinIntervalRerouteAttempts"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncSpecific15MinIntervalRoutingLoopsDetectedByThisNode"))
)
if mibBuilder.loadTexts:
    nncRoutingStatsSpecific15MinIntervalGroup.setStatus("current")

nncRoutingStatsSpecific24HourCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 7)
)
nncRoutingStatsSpecific24HourCurrentGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncSpecific24HourCurrentAbsoluteIntervalNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncSpecific24HourCurrentCallsStaticallyRoutedByThisNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncSpecific24HourCurrentCrankbacksReceivedByThisNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncSpecific24HourCurrentRerouteAttempts"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncSpecific24HourCurrentRoutingLoopsDetectedByThisNode"))
)
if mibBuilder.loadTexts:
    nncRoutingStatsSpecific24HourCurrentGroup.setStatus("current")

nncRoutingStatsSpecific24HourIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 8)
)
nncRoutingStatsSpecific24HourIntervalGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncSpecific24HourIntervalAbsoluteIntervalNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncSpecific24HourIntervalCallsStaticallyRoutedByThisNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncSpecific24HourIntervalCrankbacksReceivedByThisNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncSpecific24HourIntervalRerouteAttempts"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncSpecific24HourIntervalRoutingLoopsDetectedByThisNode"))
)
if mibBuilder.loadTexts:
    nncRoutingStatsSpecific24HourIntervalGroup.setStatus("current")

nncRoutingStatsNonBorderPerTbl15MinCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 9)
)
nncRoutingStatsNonBorderPerTbl15MinCurrentGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl15MinCurrentTableDescriptor"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl15MinCurrentAbsoluteIntervalNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl15MinCurrentFailedCallsDueToInitDTLNotGenerated"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl15MinCurrentCallsGeneratingAnInitDTL"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTble15MinCurrentDTLOrigCallsSuccessEstWithoutReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl15MinCurrentDTLOrigCallsSuccessEstWithReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl15MinCurrentDTLOrigCallsFailedInReRouting"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl15MinCurrentCrankbackReceivedAsDTLOriginator"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl15MinCurrentDTLsGeneratedDueToCrankback"))
)
if mibBuilder.loadTexts:
    nncRoutingStatsNonBorderPerTbl15MinCurrentGroup.setStatus("current")

nncRoutingStatsNonBorderPerTbl15MinIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 10)
)
nncRoutingStatsNonBorderPerTbl15MinIntervalGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl15MinIntervalTableDescriptor"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl15MinIntervalAbsoluteIntervalNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl15MinIntervalFailedCallsDueToInitDTLNotGenerated"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl15MinIntervalCallsGeneratingAnInitDTL"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl15MinIntervalDTLOrigCallsSuccessEstWithoutReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl15MinIntervalDTLOrigCallsSuccessEstWithReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl15MinIntervalDTLOrigCallsFailedInReRouting"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl15MinIntervalCrankbackReceivedAsDTLOriginator"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl15MinIntervalDTLsGeneratedDueToCrankback"))
)
if mibBuilder.loadTexts:
    nncRoutingStatsNonBorderPerTbl15MinIntervalGroup.setStatus("current")

nncRoutingStatsNonBorderPerTbl24HourCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 11)
)
nncRoutingStatsNonBorderPerTbl24HourCurrentGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourCurrentTableDescriptor"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourCurrentAbsoluteIntervalNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourCurrentFailedCallsDueToInitDTLNotGenerated"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourCurrentCallsGeneratingAnInitDTL"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourCurrentDTLOrigCallsSuccessEstWithoutReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourCurrentDTLOrigCallsSuccessEstWithReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourCurrentDTLOrigCallsFailedInReRouting"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourCurrentCrankbackReceivedAsDTLOriginator"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourCurrentDTLsGeneratedDueToCrankback"))
)
if mibBuilder.loadTexts:
    nncRoutingStatsNonBorderPerTbl24HourCurrentGroup.setStatus("current")

nncRoutingStatsNonBorderPerTbl24HourIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 12)
)
nncRoutingStatsNonBorderPerTbl24HourIntervalGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourIntervalTableDescriptor"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourIntervalAbsoluteIntervalNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourIntervalFailedCallsDueToInitDTLNotGenerated"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourIntervalCallsGeneratingAnInitDTL"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourIntervalDTLOrigCallsSuccessEstWithoutReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourIntervalDTLOrigCallsSuccessEstWithReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourIntervalDTLOrigCallsFailedInReRouting"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourIntervalCrankbackReceivedAsDTLOriginator"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBPerTbl24HourIntervalDTLsGeneratedDueToCrankback"))
)
if mibBuilder.loadTexts:
    nncRoutingStatsNonBorderPerTbl24HourIntervalGroup.setStatus("current")

nncRoutingStatsBorderPerTbl15MinCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 13)
)
nncRoutingStatsBorderPerTbl15MinCurrentGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinCurrentTableDescriptor"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinCurrentAbsoluteIntervalNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinCurrentFailedCallsDueInitLowerLvlDTLsNotGen"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinCurrentCallsGeneratingInitLowerLvlDTLs"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinCurrentDTLGenCallsSuccessEstWithoutReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinCurrentDTLGenCallsSuccessEstWithReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinCurrentDTLGenCallsFailedInReRouting"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinCurrentCrankbackReceivedAsAnEntryBorderNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinCurrentLowerLvlDTLsGenDueToRecdCrankback"))
)
if mibBuilder.loadTexts:
    nncRoutingStatsBorderPerTbl15MinCurrentGroup.setStatus("current")

nncRoutingStatsBorderPerTbl15MinIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 14)
)
nncRoutingStatsBorderPerTbl15MinIntervalGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinIntervalTableDescriptor"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinIntervalAbsoluteIntervalNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinIntervalFailedCallsDueInitLowerLvlDTLsNotGen"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinIntervalCallsGeneratingInitLowerLvlDTLs"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinIntervalDTLGenCallsSuccessEstWithoutReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinIntervalDTLGenCallsSuccessEstWithReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinIntervalDTLGenCallsFailedInReRouting"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinIntervalCrankbackReceivedAsAnEntryBorderNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl15MinIntervalLowerLvlDTLsGenDueToRecdCrankback"))
)
if mibBuilder.loadTexts:
    nncRoutingStatsBorderPerTbl15MinIntervalGroup.setStatus("current")

nncRoutingStatsBorderPerTbl24HourCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 15)
)
nncRoutingStatsBorderPerTbl24HourCurrentGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourCurrentTableDescriptor"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourCurrentState"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourCurrentAbsoluteIntervalNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourCurrentFailedCallsDueInitLowerLvlDTLsNotGen"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourCurrentCallsGeneratingInitLowerLvlDTLs"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourCurrentDTLGenCallsSuccessEstWithoutReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourCurrentDTLGenCallsSuccessEstWithReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourCurrentDTLGenCallsFailedInReRouting"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourCurrentCrankbackReceivedAsAnEntryBorderNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourCurrentLowerLvlDTLsGenDueToRecdCrankback"))
)
if mibBuilder.loadTexts:
    nncRoutingStatsBorderPerTbl24HourCurrentGroup.setStatus("current")

nncRoutingStatsBorderPerTbl24HourIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 16)
)
nncRoutingStatsBorderPerTbl24HourIntervalGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourIntervalTableDescriptor"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourIntervalAbsoluteIntervalNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourIntervalFailedCallsDueInitLowerLvlDTLsNotGen"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourIntervalCallsGeneratingInitLowerLvlDTLs"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourIntervalDTLGenCallsSuccessEstWithoutReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourIntervalDTLGenCallsSuccessEstWithReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourIntervalDTLGenCallsFailedInReRouting"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourIntervalCrankbackReceivedAsAnEntryBorderNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBPerTbl24HourIntervalLowerLvlDTLsGenDueToRecdCrankback"))
)
if mibBuilder.loadTexts:
    nncRoutingStatsBorderPerTbl24HourIntervalGroup.setStatus("current")

nncPNNIStatNonBorderTotal15MinCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 17)
)
nncPNNIStatNonBorderTotal15MinCurrentGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinCurrentAbsoluteIntervalNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinCurrentFailedCallsDueToInitDTLNotGenerated"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinCurrentCallsGeneratingAnInitDTL"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinCurrentDTLOrigCallsSuccessEstWithoutReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinCurrentDTLOrigCallsSuccessEstWithReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinCurrentDTLOrigCallsFailedInReRouting"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinCurrentCrankbackReceivedAsDTLOriginator"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinCurrentDTLsGeneratedDueToCrankback"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinCurrentCallsRecdAsTransitNodeOverInsideLinks"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinCurrentCrnkbksRecdAsTransitNodeOvInsideLnks"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinCurrentSucdEndBlocCrnkbksRecdOvInsideLnks"))
)
if mibBuilder.loadTexts:
    nncPNNIStatNonBorderTotal15MinCurrentGroup.setStatus("current")

nncPNNIStatNonBorderTotal15MinIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 18)
)
nncPNNIStatNonBorderTotal15MinIntervalGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinIntervalAbsoluteIntervalNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinIntervalFailedCallsDueToInitDTLNotGenerated"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinIntervalCallsGeneratingAnInitDTL"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinIntervalDTLOrigCallsSuccessEstWithoutReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinIntervalDTLOrigCallsSuccessEstWithReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinIntervalDTLOrigCallsFailedInReRouting"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinIntervalCrankbackReceivedAsDTLOriginator"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinIntervalDTLsGeneratedDueToCrankback"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinIntervalCallsRecdAsTransitNodeOverInsideLinks"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinIntervalCrnkbksRecdAsTransitNodeOvInsideLnks"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal15MinIntervalSucdEndBlocCrnkbksRecdOvInsideLnks"))
)
if mibBuilder.loadTexts:
    nncPNNIStatNonBorderTotal15MinIntervalGroup.setStatus("current")

nncPNNIStatNonBorderTotal24HourCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 19)
)
nncPNNIStatNonBorderTotal24HourCurrentGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentAbsoluteIntervalNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentFailedCallsDueToInitDTLNotGenerated"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentCallsGeneratingAnInitDTL"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentDTLOrigCallsSuccessEstWithoutReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentDTLOrigCallsSuccessEstWithReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentDTLOrigCallsFailedInReRouting"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentCrankbackReceivedAsDTLOriginator"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentDTLsGeneratedDueToCrankback"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentCallsRecdAsTransitNodeOverInsideLinks"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentCrnkbksRecdAsTransNodeOvInsideLnks"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentSucdEndBlocCrnkbksRecdOverInsideLinks"))
)
if mibBuilder.loadTexts:
    nncPNNIStatNonBorderTotal24HourCurrentGroup.setStatus("current")

nncPNNIStatNonBorderTotal24HourIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 20)
)
nncPNNIStatNonBorderTotal24HourIntervalGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourIntervalAbsoluteIntervalNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourIntervalFailedCallsDueToInitDTLNotGenerated"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourIntervalCallsGeneratingAnInitDTL"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourIntervalDTLOrigCallsSuccessEstWithoutReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourIntervalDTLOrigCallsSuccessEstWithReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourIntervalDTLOrigCallsFailedInReRouting"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourIntervalCrankbackReceivedAsDTLOriginator"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourIntervalDTLsGeneratedDueToCrankback"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourIntervalCallsRecdAsTransitNodeOverInsideLinks"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourIntervalCrnkbksRecdAsTransNodeOverInsideLnks"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourIntervalSucdEndBlocCrnkbksRecdOverInsideLnks"))
)
if mibBuilder.loadTexts:
    nncPNNIStatNonBorderTotal24HourIntervalGroup.setStatus("current")

nncPNNIStatBorderTotal15MinCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 21)
)
nncPNNIStatBorderTotal15MinCurrentGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinCurrentAbsoluteIntervalNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinCurrentFailedCallsDueToInitLowerLvlDTLNotGen"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinCurrentCallsGeneratingInitLowerLvlDTLs"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinCurrentDTLGenCallsSuccessEstWithoutReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinCurrentDTLGenCallsSuccessEstWithReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinCurrentDTLGenCallsFailedInReRouting"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinCurrentCrankbackReceivedAsAnEntryBorderNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinCurrentLowerLvlDTLsGenDueToRecdCrankback"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinCurrentCallsRecdOverAnOutsideLink"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinCurrentCallsTransmittedOverAnOutsideLink"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinCurrentCrankbksRecdOverAnOutsideLink"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinCurreSucdEndBlocCrankbksRecdOverOutsideLink"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinCurrentCrankbkForwdedToPrevPGCrankbkLvlTooHigh"))
)
if mibBuilder.loadTexts:
    nncPNNIStatBorderTotal15MinCurrentGroup.setStatus("current")

nncPNNIStatBorderTotal15MinIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 22)
)
nncPNNIStatBorderTotal15MinIntervalGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinIntervalAbsoluteIntervalNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinIntervalFailedCallsDueToInitLowerLvlDTLNotGen"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinIntervalCallsGeneratingInitLowerLvlDTLs"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinIntervalDTLGenCallsSuccessEstWithoutReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinIntervalDTLGenCallsSuccessEstWithReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinIntervalDTLGenCallsFailedInReRouting"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinIntervalCrankbackReceivedAsAnEntryBorderNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinIntervalLowerLvlDTLsGenDueToRecdCrankback"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinIntervalCallsRecdOverAnOutsideLink"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinIntervalCallsTransmittedOverAnOutsideLink"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinIntervalCrankbksRecdOverAnOutsideLink"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinIntervalSucdEndBlocCrankbksRecdOverOutsideLink"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal15MinIntervalCrankbkForwdedToPrevPGCrankbkLvlTooHigh"))
)
if mibBuilder.loadTexts:
    nncPNNIStatBorderTotal15MinIntervalGroup.setStatus("current")

nncPNNIStatBorderTotal24HourCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 23)
)
nncPNNIStatBorderTotal24HourCurrentGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentAbsoluteIntervalNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentFailedCallsDueToInitDTLNotGenerated"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentCallsGeneratingAnInitDTL"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentDTLOrigCallsSuccessEstWithoutReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentDTLOrigCallsSuccessEstWithReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentDTLOrigCallsFailedInReRouting"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentCrankbackReceivedAsDTLOriginator"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentDTLsGeneratedDueToCrankback"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentCallsRecdAsTransitNodeOverInsideLinks"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentCrnkbksRecdAsTransNodeOvInsideLnks"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncNBTotal24HourCurrentSucdEndBlocCrnkbksRecdOverInsideLinks"))
)
if mibBuilder.loadTexts:
    nncPNNIStatBorderTotal24HourCurrentGroup.setStatus("current")

nncPNNIStatBorderTotal24HourIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 24)
)
nncPNNIStatBorderTotal24HourIntervalGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal24HourIntervalAbsoluteIntervalNumber"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal24HourIntervalFailedCallsDueToInitLowerLvlDTLNotGen"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal24HourIntervalCallsGeneratingInitLowerLvlDTLs"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal24HourIntervalDTLGenCallsSuccessEstWithoutReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal24HourIntervalDTLGenCallsSuccessEstWithReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal24HourIntervalDTLGenCallsFailedInReRouting"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal24HourIntervalCrankbackReceivedAsAnEntryBorderNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal24HourIntervalLowerLvlDTLsGenDueToRecdCrankback"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal24HourIntervalCallsRecdOverAnOutsideLink"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal24HourIntervalCallsTransmittedOverAnOutsideLink"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal24HourIntervalCrankbksRecdOverAnOutsideLink"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal24HourCurrentSucdEndBlocCrankbksRecdOverOutsideLink"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncBTotal24HourIntervalCrankbkFwdToPrevPGCrankbkLvlTooHigh"))
)
if mibBuilder.loadTexts:
    nncPNNIStatBorderTotal24HourIntervalGroup.setStatus("current")

nncRoutingStatsRawCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 25)
)
nncRoutingStatsRawCommonGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncRoutingStatsRawCommonSuccessRoutedCallsOrigFromLocalSubs"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRoutingStatsRawCommonSuccessRtedCallsTransitedViaThisNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRoutingStatsRawCommonSuccessRoutedCallsTermToLocalSubs"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRoutingStatsRawCommonSuccessRoutedLocalCalls"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRoutingStatsRawCommonCallsOrigFromLocalCalls"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRoutingStatsRawCommonCallsTermToLocalCalls"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRoutingStatsRawCommonLocalCallAttempts"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRoutingStatsRawCommonCallsClearedDueToNoRoutingTabEntry"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRoutingStatsRawCommonCrankbacksGeneratedByThisNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRoutingStatsRawCommonFailedCallsAtLocalSubs"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRoutingStatsRawCommonCallsSuccessRerouted"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRoutingStatsRawCommonCallsFailedInRerouting"))
)
if mibBuilder.loadTexts:
    nncRoutingStatsRawCommonGroup.setStatus("current")

ncExtRoutingStatsRawSpecificGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 26)
)
ncExtRoutingStatsRawSpecificGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncRoutingStatsRawSpecificCallsStaticallyRoutedByThisNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRoutingStatsRawSpecificCrankbacksReceivedByThisNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRoutingStatsRawSpecificRerouteAttempts"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRoutingStatsRawSpecificRoutingLoopsDetectedByThisNode"))
)
if mibBuilder.loadTexts:
    ncExtRoutingStatsRawSpecificGroup.setStatus("current")

nncRoutingStatsRawNonBorderPerTblGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 27)
)
nncRoutingStatsRawNonBorderPerTblGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncRawNBPerTbleTableDescriptor"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawNBPerTbleFailedCallsDueToInitDTLNotGenerated"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawNBPerTbleCallsGeneratingAnInitDTL"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawNBPerTbleDTLOrigCallsSuccessEstWithoutReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawNBPerTbleDTLOrigCallsSuccessEstWithReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawNBPerTbleDTLOrigCallsFailedInReRouting"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawNBPerTbleSuccessCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawNBPerTbleFailedCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawNBPerTbleCrankbackReceivedAsDTLOriginator"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawNBPerTbleDTLsGeneratedDueToCrankback"))
)
if mibBuilder.loadTexts:
    nncRoutingStatsRawNonBorderPerTblGroup.setStatus("current")

nncRoutingStatsRawBorderPerTblGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 28)
)
nncRoutingStatsRawBorderPerTblGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncRawBPerTblTableDescriptor"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawBPerTblFailedCallsDueInitLowerLvlDTLsNotGen"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawBPerTblCallsGeneratingInitLowerLvlDTLs"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawBPerTblDTLGenCallsSuccessEstWithoutReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawBPerTblDTLGenCallsSuccessEstWithReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawBPerTblDTLGenCallsFailedInReRouting"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawBPerTblSuccessCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawBPerTblFailedCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawBPerTblCrankbackReceivedAsAnEntryBorderNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawBPerTblLowerLvlDTLsGenDueToRecdCrankback"))
)
if mibBuilder.loadTexts:
    nncRoutingStatsRawBorderPerTblGroup.setStatus("current")

nncPNNIStatRawNonBorderTotalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 29)
)
nncPNNIStatRawNonBorderTotalGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncRawNBTotalFailedCallsDueToInitDTLNotGenerated"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawNBTotalCallsGeneratingAnInitDTL"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawNBTotalDTLOrigCallsSuccessEstWithoutReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawNBTotalDTLOrigCallsSuccessEstWithReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawNBTotalDTLOrigCallsFailedInReRouting"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawNBTotalSuccessCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawNBTotalFailedCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawNBTotalCrankbackReceivedAsDTLOriginator"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawNBTotalDTLsGeneratedDueToCrankback"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawNBTotalCallsRecdAsTransitNodeOverInsideLinks"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawNBTotalCrnkbksRecdAsTransitNodeOvInsideLnks"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawNBTotalSucdEndBlocCrnkbksRecdOvInsideLnks"))
)
if mibBuilder.loadTexts:
    nncPNNIStatRawNonBorderTotalGroup.setStatus("current")

nncRoutingStatsRawBorderTotalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 3, 30)
)
nncRoutingStatsRawBorderTotalGroup.setObjects(
      *(("NNCEXTCALLROUTINGSTATS-MIB", "nncRawBTotalFailedCallsDueToInitLowerLvlDTLNotGen"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawBTotalCallsGeneratingInitLowerLvlDTLs"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawBTotalDTLGenCallsSuccessEstWithoutReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawBTotalDTLGenCallsSuccessEstWithReroute"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawBTotalDTLGenCallsFailedInReRouting"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawBTotalSuccessCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawBTotalFailedCallsBdwGreaterThanRTDMinBdw"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawBTotalCrankbackReceivedAsAnEntryBorderNode"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawBTotalLowerLvlDTLsGenDueToRecdCrankback"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawBTotalCallsRecdOverAnOutsideLink"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawBTotalCallsTransmittedOverAnOutsideLink"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawBTotalCrankbksRecdOverAnOutsideLink"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawBTotalSucdEndBlocCrankbksRecdOverOutsideLink"),
        ("NNCEXTCALLROUTINGSTATS-MIB", "nncRawBTotalCrankbkForwdedToPrevPGCrankbkLvlTooHigh"))
)
if mibBuilder.loadTexts:
    nncRoutingStatsRawBorderTotalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nncRoutingStatsCompliances1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 4, 1)
)
if mibBuilder.loadTexts:
    nncRoutingStatsCompliances1.setStatus(
        "current"
    )

nncRoutingStatsCompliances2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 4, 2)
)
if mibBuilder.loadTexts:
    nncRoutingStatsCompliances2.setStatus(
        "current"
    )

nncRoutingStatsCompliances3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 123, 3, 78, 4, 3)
)
if mibBuilder.loadTexts:
    nncRoutingStatsCompliances3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNCEXTCALLROUTINGSTATS-MIB",
    **{"nncExtRoutingStats": nncExtRoutingStats,
       "nncRoutingStatsObjects": nncRoutingStatsObjects,
       "nncRoutingStatsCommon15MinCurrentTable": nncRoutingStatsCommon15MinCurrentTable,
       "nncRoutingStatsCommon15MinCurrentEntry": nncRoutingStatsCommon15MinCurrentEntry,
       "nncCallControlGroupNumber": nncCallControlGroupNumber,
       "nncCommon15MinCurrentState": nncCommon15MinCurrentState,
       "nncCommon15MinCurrentAbsoluteIntervalNumber": nncCommon15MinCurrentAbsoluteIntervalNumber,
       "nncCommon15MinCurrentSuccessRoutedCallsOrigFromLocalSubs": nncCommon15MinCurrentSuccessRoutedCallsOrigFromLocalSubs,
       "nncCommon15MinCurrentSuccessRoutedCallsTransitedViaThisNode": nncCommon15MinCurrentSuccessRoutedCallsTransitedViaThisNode,
       "nncCommon15MinCurrentSuccessRoutedCallsTermToLocalSubs": nncCommon15MinCurrentSuccessRoutedCallsTermToLocalSubs,
       "nncCommon15MinCurrentSuccessRoutedLocalCalls": nncCommon15MinCurrentSuccessRoutedLocalCalls,
       "nncCommon15MinCurrentCallsOrigFromLocalCalls": nncCommon15MinCurrentCallsOrigFromLocalCalls,
       "nncCommon15MinCurrentCallsTermToLocalCalls": nncCommon15MinCurrentCallsTermToLocalCalls,
       "nncCommon15MinCurrentLocalCallAttempts": nncCommon15MinCurrentLocalCallAttempts,
       "nncCommon15MinCurrentCallsClearedDueToNoRoutingTabEntry": nncCommon15MinCurrentCallsClearedDueToNoRoutingTabEntry,
       "nncCommon15MinCurrentCrankbacksGeneratedByThisNode": nncCommon15MinCurrentCrankbacksGeneratedByThisNode,
       "nncCommon15MinCurrentFailedCallsAtLocalSubs": nncCommon15MinCurrentFailedCallsAtLocalSubs,
       "nncCommon15MinCurrentCallsSuccessRerouted": nncCommon15MinCurrentCallsSuccessRerouted,
       "nncCommon15MinCurrentCallsFailedInRerouting": nncCommon15MinCurrentCallsFailedInRerouting,
       "nncRoutingStatsCommon15MinIntervalTable": nncRoutingStatsCommon15MinIntervalTable,
       "nncRoutingStatsCommon15MinIntervalEntry": nncRoutingStatsCommon15MinIntervalEntry,
       "nncCommon15MinIntervalNumber": nncCommon15MinIntervalNumber,
       "nncCommon15MinIntervalState": nncCommon15MinIntervalState,
       "nncCommon15MinIntervalAbsoluteIntervalNumber": nncCommon15MinIntervalAbsoluteIntervalNumber,
       "nncCommon15MinIntervalSuccessRoutedCallsOrigFromLocalSubs": nncCommon15MinIntervalSuccessRoutedCallsOrigFromLocalSubs,
       "nncCommon15MinIntervalSuccessRoutedCallsTransitedViaThisNode": nncCommon15MinIntervalSuccessRoutedCallsTransitedViaThisNode,
       "nncCommon15MinIntervalSuccessRoutedCallsTermToLocalSubs": nncCommon15MinIntervalSuccessRoutedCallsTermToLocalSubs,
       "nncCommon15MinIntervalSuccessRoutedLocalCalls": nncCommon15MinIntervalSuccessRoutedLocalCalls,
       "nncCommon15MinIntervalCallsOrigFromLocalCalls": nncCommon15MinIntervalCallsOrigFromLocalCalls,
       "nncCommon15MinIntervalCallsTermToLocalCalls": nncCommon15MinIntervalCallsTermToLocalCalls,
       "nncCommon15MinIntervalLocalCallAttempts": nncCommon15MinIntervalLocalCallAttempts,
       "nncCommon15MinIntervalCallsClearedDueToNoRoutingTabEntry": nncCommon15MinIntervalCallsClearedDueToNoRoutingTabEntry,
       "nncCommon15MinIntervalCrankbacksGeneratedByThisNode": nncCommon15MinIntervalCrankbacksGeneratedByThisNode,
       "nncCommon15MinIntervalFailedCallsAtLocalSubs": nncCommon15MinIntervalFailedCallsAtLocalSubs,
       "nncCommon15MinIntervalCallsSuccessRerouted": nncCommon15MinIntervalCallsSuccessRerouted,
       "nncCommon15MinIntervalCallsFailedInRerouting": nncCommon15MinIntervalCallsFailedInRerouting,
       "nncRoutingStatsCommon24HourCurrentTable": nncRoutingStatsCommon24HourCurrentTable,
       "nncRoutingStatsCommon24HourCurrentEntry": nncRoutingStatsCommon24HourCurrentEntry,
       "nncCommon24HourCurrentState": nncCommon24HourCurrentState,
       "nncCommon24HourCurrentAbsoluteIntervalNumber": nncCommon24HourCurrentAbsoluteIntervalNumber,
       "nncCommon24HourCurrentSuccessRoutedCallsOrigFromLocalSubs": nncCommon24HourCurrentSuccessRoutedCallsOrigFromLocalSubs,
       "nncCommon24HourCurrentSuccessRoutedCallsTransitedViaThisNode": nncCommon24HourCurrentSuccessRoutedCallsTransitedViaThisNode,
       "nncCommon24HourCurrentSuccessRoutedCallsTermToLocalSubs": nncCommon24HourCurrentSuccessRoutedCallsTermToLocalSubs,
       "nncCommon24HourCurrentSuccessRoutedLocalCalls": nncCommon24HourCurrentSuccessRoutedLocalCalls,
       "nncCommon24HourCurrentCallsOrigFromLocalCalls": nncCommon24HourCurrentCallsOrigFromLocalCalls,
       "nncCommon24HourCurrentCallsTermToLocalCalls": nncCommon24HourCurrentCallsTermToLocalCalls,
       "nncCommon24HourCurrentLocalCallAttempts": nncCommon24HourCurrentLocalCallAttempts,
       "nncCommon24HourCurrentCallsClearedDueToNoRoutingTabEntry": nncCommon24HourCurrentCallsClearedDueToNoRoutingTabEntry,
       "nncCommon24HourCurrentCrankbacksGeneratedByThisNode": nncCommon24HourCurrentCrankbacksGeneratedByThisNode,
       "nncCommon24HourCurrentFailedCallsAtLocalSubs": nncCommon24HourCurrentFailedCallsAtLocalSubs,
       "nncCommon24HourCurrentCallsSuccessRerouted": nncCommon24HourCurrentCallsSuccessRerouted,
       "nncCommon24HourCurrentCallsFailedInRerouting": nncCommon24HourCurrentCallsFailedInRerouting,
       "nncRoutingStatsCommon24HourIntervalTable": nncRoutingStatsCommon24HourIntervalTable,
       "nncRoutingStatsCommon24HourIntervalEntry": nncRoutingStatsCommon24HourIntervalEntry,
       "nncCommon24HourIntervalNumber": nncCommon24HourIntervalNumber,
       "nncCommon24HourIntervalState": nncCommon24HourIntervalState,
       "nncCommon24HourIntervalAbsoluteIntervalNumber": nncCommon24HourIntervalAbsoluteIntervalNumber,
       "nncCommon24HourIntervalSuccessRoutedCallsOrigFromLocalSubs": nncCommon24HourIntervalSuccessRoutedCallsOrigFromLocalSubs,
       "nncCommon24HourIntervalSuccessRoutedCallsTransitedViaThisNode": nncCommon24HourIntervalSuccessRoutedCallsTransitedViaThisNode,
       "nncCommon24HourIntervalSuccessRoutedCallsTermToLocalSubs": nncCommon24HourIntervalSuccessRoutedCallsTermToLocalSubs,
       "nncCommon24HourIntervalSuccessRoutedLocalCalls": nncCommon24HourIntervalSuccessRoutedLocalCalls,
       "nncCommon24HourIntervalCallsOrigFromLocalCalls": nncCommon24HourIntervalCallsOrigFromLocalCalls,
       "nncCommon24HourIntervalCallsTermToLocalCalls": nncCommon24HourIntervalCallsTermToLocalCalls,
       "nncCommon24HourIntervalLocalCallAttempts": nncCommon24HourIntervalLocalCallAttempts,
       "nncCommon24HourIntervalCallsClearedDueToNoRoutingTabEntry": nncCommon24HourIntervalCallsClearedDueToNoRoutingTabEntry,
       "nncCommon24HourIntervalCrankbacksGeneratedByThisNode": nncCommon24HourIntervalCrankbacksGeneratedByThisNode,
       "nncCommon24HourIntervalFailedCallsAtLocalSubs": nncCommon24HourIntervalFailedCallsAtLocalSubs,
       "nncCommon24HourIntervalCallsSuccessRerouted": nncCommon24HourIntervalCallsSuccessRerouted,
       "nncCommon24HourIntervalCallsFailedInRerouting": nncCommon24HourIntervalCallsFailedInRerouting,
       "nncRoutingStatsSpecific15MinCurrentTable": nncRoutingStatsSpecific15MinCurrentTable,
       "nncRoutingStatsSpecific15MinCurrentEntry": nncRoutingStatsSpecific15MinCurrentEntry,
       "nncSpecific15MinCurrentState": nncSpecific15MinCurrentState,
       "nncSpecific15MinCurrentAbsoluteIntervalNumber": nncSpecific15MinCurrentAbsoluteIntervalNumber,
       "nncSpecific15MinCurrentCallsStaticallyRoutedByThisNode": nncSpecific15MinCurrentCallsStaticallyRoutedByThisNode,
       "nncSpecific15MinCurrentCrankbacksReceivedByThisNode": nncSpecific15MinCurrentCrankbacksReceivedByThisNode,
       "nncSpecific15MinCurrentRerouteAttempts": nncSpecific15MinCurrentRerouteAttempts,
       "nncSpecific15MinCurrentRoutingLoopsDetectedByThisNode": nncSpecific15MinCurrentRoutingLoopsDetectedByThisNode,
       "nncRoutingStatsSpecific15MinIntervalTable": nncRoutingStatsSpecific15MinIntervalTable,
       "nncRoutingStatsSpecific15MinIntervalEntry": nncRoutingStatsSpecific15MinIntervalEntry,
       "nncSpecific15MinIntervalNumber": nncSpecific15MinIntervalNumber,
       "nncSpecific15MinIntervalState": nncSpecific15MinIntervalState,
       "nncSpecific15MinIntervalAbsoluteIntervalNumber": nncSpecific15MinIntervalAbsoluteIntervalNumber,
       "nncSpecific15MinIntervalCallsStaticallyRoutedByThisNode": nncSpecific15MinIntervalCallsStaticallyRoutedByThisNode,
       "nncSpecific15MinIntervalCrankbacksReceivedByThisNode": nncSpecific15MinIntervalCrankbacksReceivedByThisNode,
       "nncSpecific15MinIntervalRerouteAttempts": nncSpecific15MinIntervalRerouteAttempts,
       "nncSpecific15MinIntervalRoutingLoopsDetectedByThisNode": nncSpecific15MinIntervalRoutingLoopsDetectedByThisNode,
       "nncRoutingStatsSpecific24HourCurrentTable": nncRoutingStatsSpecific24HourCurrentTable,
       "nncRoutingStatsSpecific24HourCurrentEntry": nncRoutingStatsSpecific24HourCurrentEntry,
       "nncSpecific24HourCurrentState": nncSpecific24HourCurrentState,
       "nncSpecific24HourCurrentAbsoluteIntervalNumber": nncSpecific24HourCurrentAbsoluteIntervalNumber,
       "nncSpecific24HourCurrentCallsStaticallyRoutedByThisNode": nncSpecific24HourCurrentCallsStaticallyRoutedByThisNode,
       "nncSpecific24HourCurrentCrankbacksReceivedByThisNode": nncSpecific24HourCurrentCrankbacksReceivedByThisNode,
       "nncSpecific24HourCurrentRerouteAttempts": nncSpecific24HourCurrentRerouteAttempts,
       "nncSpecific24HourCurrentRoutingLoopsDetectedByThisNode": nncSpecific24HourCurrentRoutingLoopsDetectedByThisNode,
       "nncRoutingStatsSpecific24HourIntervalTable": nncRoutingStatsSpecific24HourIntervalTable,
       "nncRoutingStatsSpecific24HourIntervalEntry": nncRoutingStatsSpecific24HourIntervalEntry,
       "nncSpecific24HourIntervalNumber": nncSpecific24HourIntervalNumber,
       "nncSpecific24HourIntervalState": nncSpecific24HourIntervalState,
       "nncSpecific24HourIntervalAbsoluteIntervalNumber": nncSpecific24HourIntervalAbsoluteIntervalNumber,
       "nncSpecific24HourIntervalCallsStaticallyRoutedByThisNode": nncSpecific24HourIntervalCallsStaticallyRoutedByThisNode,
       "nncSpecific24HourIntervalCrankbacksReceivedByThisNode": nncSpecific24HourIntervalCrankbacksReceivedByThisNode,
       "nncSpecific24HourIntervalRerouteAttempts": nncSpecific24HourIntervalRerouteAttempts,
       "nncSpecific24HourIntervalRoutingLoopsDetectedByThisNode": nncSpecific24HourIntervalRoutingLoopsDetectedByThisNode,
       "nncRoutingStatsNonBorderPerTbl15MinCurrentTable": nncRoutingStatsNonBorderPerTbl15MinCurrentTable,
       "nncRoutingStatsNonBorderPerTbl15MinCurrentEntry": nncRoutingStatsNonBorderPerTbl15MinCurrentEntry,
       "nncNBPerTbl15MinCurrentTableDescriptor": nncNBPerTbl15MinCurrentTableDescriptor,
       "nncNBPerTbl15MinCurrentState": nncNBPerTbl15MinCurrentState,
       "nncNBPerTbl15MinCurrentAbsoluteIntervalNumber": nncNBPerTbl15MinCurrentAbsoluteIntervalNumber,
       "nncNBPerTbl15MinCurrentFailedCallsDueToInitDTLNotGenerated": nncNBPerTbl15MinCurrentFailedCallsDueToInitDTLNotGenerated,
       "nncNBPerTbl15MinCurrentCallsGeneratingAnInitDTL": nncNBPerTbl15MinCurrentCallsGeneratingAnInitDTL,
       "nncNBPerTble15MinCurrentDTLOrigCallsSuccessEstWithoutReroute": nncNBPerTble15MinCurrentDTLOrigCallsSuccessEstWithoutReroute,
       "nncNBPerTbl15MinCurrentDTLOrigCallsSuccessEstWithReroute": nncNBPerTbl15MinCurrentDTLOrigCallsSuccessEstWithReroute,
       "nncNBPerTbl15MinCurrentDTLOrigCallsFailedInReRouting": nncNBPerTbl15MinCurrentDTLOrigCallsFailedInReRouting,
       "nncNBPerTbl15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw": nncNBPerTbl15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw,
       "nncNBPerTbl15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw": nncNBPerTbl15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw,
       "nncNBPerTbl15MinCurrentCrankbackReceivedAsDTLOriginator": nncNBPerTbl15MinCurrentCrankbackReceivedAsDTLOriginator,
       "nncNBPerTbl15MinCurrentDTLsGeneratedDueToCrankback": nncNBPerTbl15MinCurrentDTLsGeneratedDueToCrankback,
       "nncRoutingStatsNonBorderPerTbl15MinIntervalTable": nncRoutingStatsNonBorderPerTbl15MinIntervalTable,
       "nncRoutingStatsNonBorderPerTbl15MinIntervalEntry": nncRoutingStatsNonBorderPerTbl15MinIntervalEntry,
       "nncNBPerTbl15MinIntervalNumber": nncNBPerTbl15MinIntervalNumber,
       "nncNBPerTbl15MinIntervalTableDescriptor": nncNBPerTbl15MinIntervalTableDescriptor,
       "nncNBPerTbl15MinIntervalState": nncNBPerTbl15MinIntervalState,
       "nncNBPerTbl15MinIntervalAbsoluteIntervalNumber": nncNBPerTbl15MinIntervalAbsoluteIntervalNumber,
       "nncNBPerTbl15MinIntervalFailedCallsDueToInitDTLNotGenerated": nncNBPerTbl15MinIntervalFailedCallsDueToInitDTLNotGenerated,
       "nncNBPerTbl15MinIntervalCallsGeneratingAnInitDTL": nncNBPerTbl15MinIntervalCallsGeneratingAnInitDTL,
       "nncNBPerTbl15MinIntervalDTLOrigCallsSuccessEstWithoutReroute": nncNBPerTbl15MinIntervalDTLOrigCallsSuccessEstWithoutReroute,
       "nncNBPerTbl15MinIntervalDTLOrigCallsSuccessEstWithReroute": nncNBPerTbl15MinIntervalDTLOrigCallsSuccessEstWithReroute,
       "nncNBPerTbl15MinIntervalDTLOrigCallsFailedInReRouting": nncNBPerTbl15MinIntervalDTLOrigCallsFailedInReRouting,
       "nncNBPerTbl15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw": nncNBPerTbl15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw,
       "nncNBPerTbl15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw": nncNBPerTbl15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw,
       "nncNBPerTbl15MinIntervalCrankbackReceivedAsDTLOriginator": nncNBPerTbl15MinIntervalCrankbackReceivedAsDTLOriginator,
       "nncNBPerTbl15MinIntervalDTLsGeneratedDueToCrankback": nncNBPerTbl15MinIntervalDTLsGeneratedDueToCrankback,
       "nncRoutingStatsNonBorderPerTbl24HourCurrentTable": nncRoutingStatsNonBorderPerTbl24HourCurrentTable,
       "nncRoutingStatsNonBorderPerTbl24HourCurrentEntry": nncRoutingStatsNonBorderPerTbl24HourCurrentEntry,
       "nncNBPerTbl24HourCurrentTableDescriptor": nncNBPerTbl24HourCurrentTableDescriptor,
       "nncNBPerTbl24HourCurrentState": nncNBPerTbl24HourCurrentState,
       "nncNBPerTbl24HourCurrentAbsoluteIntervalNumber": nncNBPerTbl24HourCurrentAbsoluteIntervalNumber,
       "nncNBPerTbl24HourCurrentFailedCallsDueToInitDTLNotGenerated": nncNBPerTbl24HourCurrentFailedCallsDueToInitDTLNotGenerated,
       "nncNBPerTbl24HourCurrentCallsGeneratingAnInitDTL": nncNBPerTbl24HourCurrentCallsGeneratingAnInitDTL,
       "nncNBPerTbl24HourCurrentDTLOrigCallsSuccessEstWithoutReroute": nncNBPerTbl24HourCurrentDTLOrigCallsSuccessEstWithoutReroute,
       "nncNBPerTbl24HourCurrentDTLOrigCallsSuccessEstWithReroute": nncNBPerTbl24HourCurrentDTLOrigCallsSuccessEstWithReroute,
       "nncNBPerTbl24HourCurrentDTLOrigCallsFailedInReRouting": nncNBPerTbl24HourCurrentDTLOrigCallsFailedInReRouting,
       "nncNBPerTbl24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw": nncNBPerTbl24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw,
       "nncNBPerTbl24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw": nncNBPerTbl24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw,
       "nncNBPerTbl24HourCurrentCrankbackReceivedAsDTLOriginator": nncNBPerTbl24HourCurrentCrankbackReceivedAsDTLOriginator,
       "nncNBPerTbl24HourCurrentDTLsGeneratedDueToCrankback": nncNBPerTbl24HourCurrentDTLsGeneratedDueToCrankback,
       "nncRoutingStatsNonBorderPerTbl24HourIntervalTable": nncRoutingStatsNonBorderPerTbl24HourIntervalTable,
       "nncRoutingStatsNonBorderPerTbl24HourIntervalEntry": nncRoutingStatsNonBorderPerTbl24HourIntervalEntry,
       "nncNBPerTbl24HourIntervalNumber": nncNBPerTbl24HourIntervalNumber,
       "nncNBPerTbl24HourIntervalTableDescriptor": nncNBPerTbl24HourIntervalTableDescriptor,
       "nncNBPerTbl24HourIntervalState": nncNBPerTbl24HourIntervalState,
       "nncNBPerTbl24HourIntervalAbsoluteIntervalNumber": nncNBPerTbl24HourIntervalAbsoluteIntervalNumber,
       "nncNBPerTbl24HourIntervalFailedCallsDueToInitDTLNotGenerated": nncNBPerTbl24HourIntervalFailedCallsDueToInitDTLNotGenerated,
       "nncNBPerTbl24HourIntervalCallsGeneratingAnInitDTL": nncNBPerTbl24HourIntervalCallsGeneratingAnInitDTL,
       "nncNBPerTbl24HourIntervalDTLOrigCallsSuccessEstWithoutReroute": nncNBPerTbl24HourIntervalDTLOrigCallsSuccessEstWithoutReroute,
       "nncNBPerTbl24HourIntervalDTLOrigCallsSuccessEstWithReroute": nncNBPerTbl24HourIntervalDTLOrigCallsSuccessEstWithReroute,
       "nncNBPerTbl24HourIntervalDTLOrigCallsFailedInReRouting": nncNBPerTbl24HourIntervalDTLOrigCallsFailedInReRouting,
       "nncNBPerTbl24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw": nncNBPerTbl24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw,
       "nncNBPerTbl24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw": nncNBPerTbl24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw,
       "nncNBPerTbl24HourIntervalCrankbackReceivedAsDTLOriginator": nncNBPerTbl24HourIntervalCrankbackReceivedAsDTLOriginator,
       "nncNBPerTbl24HourIntervalDTLsGeneratedDueToCrankback": nncNBPerTbl24HourIntervalDTLsGeneratedDueToCrankback,
       "nncRoutingStatsBorderPerTbl15MinCurrentTable": nncRoutingStatsBorderPerTbl15MinCurrentTable,
       "nncRoutingStatsBorderPerTbl15MinCurrentEntry": nncRoutingStatsBorderPerTbl15MinCurrentEntry,
       "nncBPerTbl15MinCurrentTableDescriptor": nncBPerTbl15MinCurrentTableDescriptor,
       "nncBPerTbl15MinCurrentState": nncBPerTbl15MinCurrentState,
       "nncBPerTbl15MinCurrentAbsoluteIntervalNumber": nncBPerTbl15MinCurrentAbsoluteIntervalNumber,
       "nncBPerTbl15MinCurrentFailedCallsDueInitLowerLvlDTLsNotGen": nncBPerTbl15MinCurrentFailedCallsDueInitLowerLvlDTLsNotGen,
       "nncBPerTbl15MinCurrentCallsGeneratingInitLowerLvlDTLs": nncBPerTbl15MinCurrentCallsGeneratingInitLowerLvlDTLs,
       "nncBPerTbl15MinCurrentDTLGenCallsSuccessEstWithoutReroute": nncBPerTbl15MinCurrentDTLGenCallsSuccessEstWithoutReroute,
       "nncBPerTbl15MinCurrentDTLGenCallsSuccessEstWithReroute": nncBPerTbl15MinCurrentDTLGenCallsSuccessEstWithReroute,
       "nncBPerTbl15MinCurrentDTLGenCallsFailedInReRouting": nncBPerTbl15MinCurrentDTLGenCallsFailedInReRouting,
       "nncBPerTbl15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw": nncBPerTbl15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw,
       "nncBPerTbl15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw": nncBPerTbl15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw,
       "nncBPerTbl15MinCurrentCrankbackReceivedAsAnEntryBorderNode": nncBPerTbl15MinCurrentCrankbackReceivedAsAnEntryBorderNode,
       "nncBPerTbl15MinCurrentLowerLvlDTLsGenDueToRecdCrankback": nncBPerTbl15MinCurrentLowerLvlDTLsGenDueToRecdCrankback,
       "nncRoutingStatsBorderPerTbl15MinIntervalTable": nncRoutingStatsBorderPerTbl15MinIntervalTable,
       "nncRoutingStatsBorderPerTbl15MinIntervalEntry": nncRoutingStatsBorderPerTbl15MinIntervalEntry,
       "nncBPerTbl15MinIntervalNumber": nncBPerTbl15MinIntervalNumber,
       "nncBPerTbl15MinIntervalTableDescriptor": nncBPerTbl15MinIntervalTableDescriptor,
       "nncBPerTbl15MinIntervalState": nncBPerTbl15MinIntervalState,
       "nncBPerTbl15MinIntervalAbsoluteIntervalNumber": nncBPerTbl15MinIntervalAbsoluteIntervalNumber,
       "nncBPerTbl15MinIntervalFailedCallsDueInitLowerLvlDTLsNotGen": nncBPerTbl15MinIntervalFailedCallsDueInitLowerLvlDTLsNotGen,
       "nncBPerTbl15MinIntervalCallsGeneratingInitLowerLvlDTLs": nncBPerTbl15MinIntervalCallsGeneratingInitLowerLvlDTLs,
       "nncBPerTbl15MinIntervalDTLGenCallsSuccessEstWithoutReroute": nncBPerTbl15MinIntervalDTLGenCallsSuccessEstWithoutReroute,
       "nncBPerTbl15MinIntervalDTLGenCallsSuccessEstWithReroute": nncBPerTbl15MinIntervalDTLGenCallsSuccessEstWithReroute,
       "nncBPerTbl15MinIntervalDTLGenCallsFailedInReRouting": nncBPerTbl15MinIntervalDTLGenCallsFailedInReRouting,
       "nncBPerTbl15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw": nncBPerTbl15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw,
       "nncBPerTbl15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw": nncBPerTbl15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw,
       "nncBPerTbl15MinIntervalCrankbackReceivedAsAnEntryBorderNode": nncBPerTbl15MinIntervalCrankbackReceivedAsAnEntryBorderNode,
       "nncBPerTbl15MinIntervalLowerLvlDTLsGenDueToRecdCrankback": nncBPerTbl15MinIntervalLowerLvlDTLsGenDueToRecdCrankback,
       "nncRoutingStatsBorderPerTbl24HourCurrentTable": nncRoutingStatsBorderPerTbl24HourCurrentTable,
       "nncRoutingStatsBorderPerTbl24HourCurrentEntry": nncRoutingStatsBorderPerTbl24HourCurrentEntry,
       "nncBPerTbl24HourCurrentTableDescriptor": nncBPerTbl24HourCurrentTableDescriptor,
       "nncBPerTbl24HourCurrentState": nncBPerTbl24HourCurrentState,
       "nncBPerTbl24HourCurrentAbsoluteIntervalNumber": nncBPerTbl24HourCurrentAbsoluteIntervalNumber,
       "nncBPerTbl24HourCurrentFailedCallsDueInitLowerLvlDTLsNotGen": nncBPerTbl24HourCurrentFailedCallsDueInitLowerLvlDTLsNotGen,
       "nncBPerTbl24HourCurrentCallsGeneratingInitLowerLvlDTLs": nncBPerTbl24HourCurrentCallsGeneratingInitLowerLvlDTLs,
       "nncBPerTbl24HourCurrentDTLGenCallsSuccessEstWithoutReroute": nncBPerTbl24HourCurrentDTLGenCallsSuccessEstWithoutReroute,
       "nncBPerTbl24HourCurrentDTLGenCallsSuccessEstWithReroute": nncBPerTbl24HourCurrentDTLGenCallsSuccessEstWithReroute,
       "nncBPerTbl24HourCurrentDTLGenCallsFailedInReRouting": nncBPerTbl24HourCurrentDTLGenCallsFailedInReRouting,
       "nncBPerTbl24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw": nncBPerTbl24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw,
       "nncBPerTbl24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw": nncBPerTbl24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw,
       "nncBPerTbl24HourCurrentCrankbackReceivedAsAnEntryBorderNode": nncBPerTbl24HourCurrentCrankbackReceivedAsAnEntryBorderNode,
       "nncBPerTbl24HourCurrentLowerLvlDTLsGenDueToRecdCrankback": nncBPerTbl24HourCurrentLowerLvlDTLsGenDueToRecdCrankback,
       "nncRoutingStatsBorderPerTbl24HourIntervalTable": nncRoutingStatsBorderPerTbl24HourIntervalTable,
       "nncRoutingStatsBorderPerTbl24HourIntervalEntry": nncRoutingStatsBorderPerTbl24HourIntervalEntry,
       "nncBPerTbl24HourIntervalNumber": nncBPerTbl24HourIntervalNumber,
       "nncBPerTbl24HourIntervalTableDescriptor": nncBPerTbl24HourIntervalTableDescriptor,
       "nncBPerTbl24HourIntervalState": nncBPerTbl24HourIntervalState,
       "nncBPerTbl24HourIntervalAbsoluteIntervalNumber": nncBPerTbl24HourIntervalAbsoluteIntervalNumber,
       "nncBPerTbl24HourIntervalFailedCallsDueInitLowerLvlDTLsNotGen": nncBPerTbl24HourIntervalFailedCallsDueInitLowerLvlDTLsNotGen,
       "nncBPerTbl24HourIntervalCallsGeneratingInitLowerLvlDTLs": nncBPerTbl24HourIntervalCallsGeneratingInitLowerLvlDTLs,
       "nncBPerTbl24HourIntervalDTLGenCallsSuccessEstWithoutReroute": nncBPerTbl24HourIntervalDTLGenCallsSuccessEstWithoutReroute,
       "nncBPerTbl24HourIntervalDTLGenCallsSuccessEstWithReroute": nncBPerTbl24HourIntervalDTLGenCallsSuccessEstWithReroute,
       "nncBPerTbl24HourIntervalDTLGenCallsFailedInReRouting": nncBPerTbl24HourIntervalDTLGenCallsFailedInReRouting,
       "nncBPerTbl24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw": nncBPerTbl24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw,
       "nncBPerTbl24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw": nncBPerTbl24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw,
       "nncBPerTbl24HourIntervalCrankbackReceivedAsAnEntryBorderNode": nncBPerTbl24HourIntervalCrankbackReceivedAsAnEntryBorderNode,
       "nncBPerTbl24HourIntervalLowerLvlDTLsGenDueToRecdCrankback": nncBPerTbl24HourIntervalLowerLvlDTLsGenDueToRecdCrankback,
       "nncRoutingStatsNonBorderTotal15MinCurrentTable": nncRoutingStatsNonBorderTotal15MinCurrentTable,
       "nncRoutingStatsNonBorderTotal15MinCurrentEntry": nncRoutingStatsNonBorderTotal15MinCurrentEntry,
       "nncNBTotal15MinCurrentState": nncNBTotal15MinCurrentState,
       "nncNBTotal15MinCurrentAbsoluteIntervalNumber": nncNBTotal15MinCurrentAbsoluteIntervalNumber,
       "nncNBTotal15MinCurrentFailedCallsDueToInitDTLNotGenerated": nncNBTotal15MinCurrentFailedCallsDueToInitDTLNotGenerated,
       "nncNBTotal15MinCurrentCallsGeneratingAnInitDTL": nncNBTotal15MinCurrentCallsGeneratingAnInitDTL,
       "nncNBTotal15MinCurrentDTLOrigCallsSuccessEstWithoutReroute": nncNBTotal15MinCurrentDTLOrigCallsSuccessEstWithoutReroute,
       "nncNBTotal15MinCurrentDTLOrigCallsSuccessEstWithReroute": nncNBTotal15MinCurrentDTLOrigCallsSuccessEstWithReroute,
       "nncNBTotal15MinCurrentDTLOrigCallsFailedInReRouting": nncNBTotal15MinCurrentDTLOrigCallsFailedInReRouting,
       "nncNBTotal15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw": nncNBTotal15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw,
       "nncNBTotal15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw": nncNBTotal15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw,
       "nncNBTotal15MinCurrentCrankbackReceivedAsDTLOriginator": nncNBTotal15MinCurrentCrankbackReceivedAsDTLOriginator,
       "nncNBTotal15MinCurrentDTLsGeneratedDueToCrankback": nncNBTotal15MinCurrentDTLsGeneratedDueToCrankback,
       "nncNBTotal15MinCurrentCallsRecdAsTransitNodeOverInsideLinks": nncNBTotal15MinCurrentCallsRecdAsTransitNodeOverInsideLinks,
       "nncNBTotal15MinCurrentCrnkbksRecdAsTransitNodeOvInsideLnks": nncNBTotal15MinCurrentCrnkbksRecdAsTransitNodeOvInsideLnks,
       "nncNBTotal15MinCurrentSucdEndBlocCrnkbksRecdOvInsideLnks": nncNBTotal15MinCurrentSucdEndBlocCrnkbksRecdOvInsideLnks,
       "nncRoutingStatsNonBorderTotal15MinIntervalTable": nncRoutingStatsNonBorderTotal15MinIntervalTable,
       "nncRoutingStatsNonBorderTotal15MinIntervalEntry": nncRoutingStatsNonBorderTotal15MinIntervalEntry,
       "nncNBTotal15MinIntervalNumber": nncNBTotal15MinIntervalNumber,
       "nncNBTotal15MinIntervalState": nncNBTotal15MinIntervalState,
       "nncNBTotal15MinIntervalAbsoluteIntervalNumber": nncNBTotal15MinIntervalAbsoluteIntervalNumber,
       "nncNBTotal15MinIntervalFailedCallsDueToInitDTLNotGenerated": nncNBTotal15MinIntervalFailedCallsDueToInitDTLNotGenerated,
       "nncNBTotal15MinIntervalCallsGeneratingAnInitDTL": nncNBTotal15MinIntervalCallsGeneratingAnInitDTL,
       "nncNBTotal15MinIntervalDTLOrigCallsSuccessEstWithoutReroute": nncNBTotal15MinIntervalDTLOrigCallsSuccessEstWithoutReroute,
       "nncNBTotal15MinIntervalDTLOrigCallsSuccessEstWithReroute": nncNBTotal15MinIntervalDTLOrigCallsSuccessEstWithReroute,
       "nncNBTotal15MinIntervalDTLOrigCallsFailedInReRouting": nncNBTotal15MinIntervalDTLOrigCallsFailedInReRouting,
       "nncNBTotal15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw": nncNBTotal15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw,
       "nncNBTotal15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw": nncNBTotal15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw,
       "nncNBTotal15MinIntervalCrankbackReceivedAsDTLOriginator": nncNBTotal15MinIntervalCrankbackReceivedAsDTLOriginator,
       "nncNBTotal15MinIntervalDTLsGeneratedDueToCrankback": nncNBTotal15MinIntervalDTLsGeneratedDueToCrankback,
       "nncNBTotal15MinIntervalCallsRecdAsTransitNodeOverInsideLinks": nncNBTotal15MinIntervalCallsRecdAsTransitNodeOverInsideLinks,
       "nncNBTotal15MinIntervalCrnkbksRecdAsTransitNodeOvInsideLnks": nncNBTotal15MinIntervalCrnkbksRecdAsTransitNodeOvInsideLnks,
       "nncNBTotal15MinIntervalSucdEndBlocCrnkbksRecdOvInsideLnks": nncNBTotal15MinIntervalSucdEndBlocCrnkbksRecdOvInsideLnks,
       "nncRoutingStatsNonBorderTotal24HourCurrentTable": nncRoutingStatsNonBorderTotal24HourCurrentTable,
       "nncRoutingStatsNonBorderTotal24HourCurrentEntry": nncRoutingStatsNonBorderTotal24HourCurrentEntry,
       "nncNBTotal24HourCurrentState": nncNBTotal24HourCurrentState,
       "nncNBTotal24HourCurrentAbsoluteIntervalNumber": nncNBTotal24HourCurrentAbsoluteIntervalNumber,
       "nncNBTotal24HourCurrentFailedCallsDueToInitDTLNotGenerated": nncNBTotal24HourCurrentFailedCallsDueToInitDTLNotGenerated,
       "nncNBTotal24HourCurrentCallsGeneratingAnInitDTL": nncNBTotal24HourCurrentCallsGeneratingAnInitDTL,
       "nncNBTotal24HourCurrentDTLOrigCallsSuccessEstWithoutReroute": nncNBTotal24HourCurrentDTLOrigCallsSuccessEstWithoutReroute,
       "nncNBTotal24HourCurrentDTLOrigCallsSuccessEstWithReroute": nncNBTotal24HourCurrentDTLOrigCallsSuccessEstWithReroute,
       "nncNBTotal24HourCurrentDTLOrigCallsFailedInReRouting": nncNBTotal24HourCurrentDTLOrigCallsFailedInReRouting,
       "nncNBTotal24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw": nncNBTotal24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw,
       "nncNBTotal24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw": nncNBTotal24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw,
       "nncNBTotal24HourCurrentCrankbackReceivedAsDTLOriginator": nncNBTotal24HourCurrentCrankbackReceivedAsDTLOriginator,
       "nncNBTotal24HourCurrentDTLsGeneratedDueToCrankback": nncNBTotal24HourCurrentDTLsGeneratedDueToCrankback,
       "nncNBTotal24HourCurrentCallsRecdAsTransitNodeOverInsideLinks": nncNBTotal24HourCurrentCallsRecdAsTransitNodeOverInsideLinks,
       "nncNBTotal24HourCurrentCrnkbksRecdAsTransNodeOvInsideLnks": nncNBTotal24HourCurrentCrnkbksRecdAsTransNodeOvInsideLnks,
       "nncNBTotal24HourCurrentSucdEndBlocCrnkbksRecdOverInsideLinks": nncNBTotal24HourCurrentSucdEndBlocCrnkbksRecdOverInsideLinks,
       "nncRoutingStatsNonBorderTotal24HourIntervalTable": nncRoutingStatsNonBorderTotal24HourIntervalTable,
       "nncRoutingStatsNonBorderTotal24HourIntervalEntry": nncRoutingStatsNonBorderTotal24HourIntervalEntry,
       "nncNBTotal24HourIntervalNumber": nncNBTotal24HourIntervalNumber,
       "nncNBTotal24HourIntervalState": nncNBTotal24HourIntervalState,
       "nncNBTotal24HourIntervalAbsoluteIntervalNumber": nncNBTotal24HourIntervalAbsoluteIntervalNumber,
       "nncNBTotal24HourIntervalFailedCallsDueToInitDTLNotGenerated": nncNBTotal24HourIntervalFailedCallsDueToInitDTLNotGenerated,
       "nncNBTotal24HourIntervalCallsGeneratingAnInitDTL": nncNBTotal24HourIntervalCallsGeneratingAnInitDTL,
       "nncNBTotal24HourIntervalDTLOrigCallsSuccessEstWithoutReroute": nncNBTotal24HourIntervalDTLOrigCallsSuccessEstWithoutReroute,
       "nncNBTotal24HourIntervalDTLOrigCallsSuccessEstWithReroute": nncNBTotal24HourIntervalDTLOrigCallsSuccessEstWithReroute,
       "nncNBTotal24HourIntervalDTLOrigCallsFailedInReRouting": nncNBTotal24HourIntervalDTLOrigCallsFailedInReRouting,
       "nncNBTotal24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw": nncNBTotal24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw,
       "nncNBTotal24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw": nncNBTotal24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw,
       "nncNBTotal24HourIntervalCrankbackReceivedAsDTLOriginator": nncNBTotal24HourIntervalCrankbackReceivedAsDTLOriginator,
       "nncNBTotal24HourIntervalDTLsGeneratedDueToCrankback": nncNBTotal24HourIntervalDTLsGeneratedDueToCrankback,
       "nncNBTotal24HourIntervalCallsRecdAsTransitNodeOverInsideLinks": nncNBTotal24HourIntervalCallsRecdAsTransitNodeOverInsideLinks,
       "nncNBTotal24HourIntervalCrnkbksRecdAsTransNodeOverInsideLnks": nncNBTotal24HourIntervalCrnkbksRecdAsTransNodeOverInsideLnks,
       "nncNBTotal24HourIntervalSucdEndBlocCrnkbksRecdOverInsideLnks": nncNBTotal24HourIntervalSucdEndBlocCrnkbksRecdOverInsideLnks,
       "nncRoutingStatsBorderTotal15MinCurrentTable": nncRoutingStatsBorderTotal15MinCurrentTable,
       "nncRoutingStatsBorderTotal15MinCurrentEntry": nncRoutingStatsBorderTotal15MinCurrentEntry,
       "nncBTotal15MinCurrentState": nncBTotal15MinCurrentState,
       "nncBTotal15MinCurrentAbsoluteIntervalNumber": nncBTotal15MinCurrentAbsoluteIntervalNumber,
       "nncBTotal15MinCurrentFailedCallsDueToInitLowerLvlDTLNotGen": nncBTotal15MinCurrentFailedCallsDueToInitLowerLvlDTLNotGen,
       "nncBTotal15MinCurrentCallsGeneratingInitLowerLvlDTLs": nncBTotal15MinCurrentCallsGeneratingInitLowerLvlDTLs,
       "nncBTotal15MinCurrentDTLGenCallsSuccessEstWithoutReroute": nncBTotal15MinCurrentDTLGenCallsSuccessEstWithoutReroute,
       "nncBTotal15MinCurrentDTLGenCallsSuccessEstWithReroute": nncBTotal15MinCurrentDTLGenCallsSuccessEstWithReroute,
       "nncBTotal15MinCurrentDTLGenCallsFailedInReRouting": nncBTotal15MinCurrentDTLGenCallsFailedInReRouting,
       "nncBTotal15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw": nncBTotal15MinCurrentSuccessCallsBdwGreaterThanRTDMinBdw,
       "nncBTotal15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw": nncBTotal15MinCurrentFailedCallsBdwGreaterThanRTDMinBdw,
       "nncBTotal15MinCurrentCrankbackReceivedAsAnEntryBorderNode": nncBTotal15MinCurrentCrankbackReceivedAsAnEntryBorderNode,
       "nncBTotal15MinCurrentLowerLvlDTLsGenDueToRecdCrankback": nncBTotal15MinCurrentLowerLvlDTLsGenDueToRecdCrankback,
       "nncBTotal15MinCurrentCallsRecdOverAnOutsideLink": nncBTotal15MinCurrentCallsRecdOverAnOutsideLink,
       "nncBTotal15MinCurrentCallsTransmittedOverAnOutsideLink": nncBTotal15MinCurrentCallsTransmittedOverAnOutsideLink,
       "nncBTotal15MinCurrentCrankbksRecdOverAnOutsideLink": nncBTotal15MinCurrentCrankbksRecdOverAnOutsideLink,
       "nncBTotal15MinCurreSucdEndBlocCrankbksRecdOverOutsideLink": nncBTotal15MinCurreSucdEndBlocCrankbksRecdOverOutsideLink,
       "nncBTotal15MinCurrentCrankbkForwdedToPrevPGCrankbkLvlTooHigh": nncBTotal15MinCurrentCrankbkForwdedToPrevPGCrankbkLvlTooHigh,
       "nncRoutingStatsBorderTotal15MinIntervalTable": nncRoutingStatsBorderTotal15MinIntervalTable,
       "nncRoutingStatsBorderTotal15MinIntervalEntry": nncRoutingStatsBorderTotal15MinIntervalEntry,
       "nncBTotal15MinIntervalNumber": nncBTotal15MinIntervalNumber,
       "nncBTotal15MinIntervalState": nncBTotal15MinIntervalState,
       "nncBTotal15MinIntervalAbsoluteIntervalNumber": nncBTotal15MinIntervalAbsoluteIntervalNumber,
       "nncBTotal15MinIntervalFailedCallsDueToInitLowerLvlDTLNotGen": nncBTotal15MinIntervalFailedCallsDueToInitLowerLvlDTLNotGen,
       "nncBTotal15MinIntervalCallsGeneratingInitLowerLvlDTLs": nncBTotal15MinIntervalCallsGeneratingInitLowerLvlDTLs,
       "nncBTotal15MinIntervalDTLGenCallsSuccessEstWithoutReroute": nncBTotal15MinIntervalDTLGenCallsSuccessEstWithoutReroute,
       "nncBTotal15MinIntervalDTLGenCallsSuccessEstWithReroute": nncBTotal15MinIntervalDTLGenCallsSuccessEstWithReroute,
       "nncBTotal15MinIntervalDTLGenCallsFailedInReRouting": nncBTotal15MinIntervalDTLGenCallsFailedInReRouting,
       "nncBTotal15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw": nncBTotal15MinIntervalSuccessCallsBdwGreaterThanRTDMinBdw,
       "nncBTotal15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw": nncBTotal15MinIntervalFailedCallsBdwGreaterThanRTDMinBdw,
       "nncBTotal15MinIntervalCrankbackReceivedAsAnEntryBorderNode": nncBTotal15MinIntervalCrankbackReceivedAsAnEntryBorderNode,
       "nncBTotal15MinIntervalLowerLvlDTLsGenDueToRecdCrankback": nncBTotal15MinIntervalLowerLvlDTLsGenDueToRecdCrankback,
       "nncBTotal15MinIntervalCallsRecdOverAnOutsideLink": nncBTotal15MinIntervalCallsRecdOverAnOutsideLink,
       "nncBTotal15MinIntervalCallsTransmittedOverAnOutsideLink": nncBTotal15MinIntervalCallsTransmittedOverAnOutsideLink,
       "nncBTotal15MinIntervalCrankbksRecdOverAnOutsideLink": nncBTotal15MinIntervalCrankbksRecdOverAnOutsideLink,
       "nncBTotal15MinIntervalSucdEndBlocCrankbksRecdOverOutsideLink": nncBTotal15MinIntervalSucdEndBlocCrankbksRecdOverOutsideLink,
       "nncBTotal15MinIntervalCrankbkForwdedToPrevPGCrankbkLvlTooHigh": nncBTotal15MinIntervalCrankbkForwdedToPrevPGCrankbkLvlTooHigh,
       "nncRoutingStatsBorderTotal24HourCurrentTable": nncRoutingStatsBorderTotal24HourCurrentTable,
       "nncRoutingStatsBorderTotal24HourCurrentEntry": nncRoutingStatsBorderTotal24HourCurrentEntry,
       "nncBTotal24HourCurrentState": nncBTotal24HourCurrentState,
       "nncBTotal24HourCurrentAbsoluteIntervalNumber": nncBTotal24HourCurrentAbsoluteIntervalNumber,
       "nncBTotal24HourCurrentFailedCallsDueToInitLowerLvlDTLNotGen": nncBTotal24HourCurrentFailedCallsDueToInitLowerLvlDTLNotGen,
       "nncBTotal24HourCurrentCallsGeneratingInitLowerLvlDTLs": nncBTotal24HourCurrentCallsGeneratingInitLowerLvlDTLs,
       "nncBTotal24HourCurrentDTLGenCallsSuccessEstWithoutReroute": nncBTotal24HourCurrentDTLGenCallsSuccessEstWithoutReroute,
       "nncBTotal24HourCurrentDTLGenCallsSuccessEstWithReroute": nncBTotal24HourCurrentDTLGenCallsSuccessEstWithReroute,
       "nncBTotal24HourCurrentDTLGenCallsFailedInReRouting": nncBTotal24HourCurrentDTLGenCallsFailedInReRouting,
       "nncBTotal24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw": nncBTotal24HourCurrentSuccessCallsBdwGreaterThanRTDMinBdw,
       "nncBTotal24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw": nncBTotal24HourCurrentFailedCallsBdwGreaterThanRTDMinBdw,
       "nncBTotal24HourCurrentCrankbackReceivedAsAnEntryBorderNode": nncBTotal24HourCurrentCrankbackReceivedAsAnEntryBorderNode,
       "nncBTotal24HourCurrentLowerLvlDTLsGenDueToRecdCrankback": nncBTotal24HourCurrentLowerLvlDTLsGenDueToRecdCrankback,
       "nncBTotal24HourCurrentCallsRecdOverAnOutsideLink": nncBTotal24HourCurrentCallsRecdOverAnOutsideLink,
       "nncBTotal24HourCurrentCallsTransmittedOverAnOutsideLink": nncBTotal24HourCurrentCallsTransmittedOverAnOutsideLink,
       "nncBTotal24HourCurrentCrankbksRecdOverAnOutsideLink": nncBTotal24HourCurrentCrankbksRecdOverAnOutsideLink,
       "nncBTotal24HourCurrentSucdEndBlocCrankbksRecdOverOutsideLink": nncBTotal24HourCurrentSucdEndBlocCrankbksRecdOverOutsideLink,
       "nncBTotal24HourCurrentCrankbkForwdedToPrevPGCrankbkLvlTooHigh": nncBTotal24HourCurrentCrankbkForwdedToPrevPGCrankbkLvlTooHigh,
       "nncRoutingStatsBorderTotal24HourIntervalTable": nncRoutingStatsBorderTotal24HourIntervalTable,
       "nncRoutingStatsBorderTotal24HourIntervalEntry": nncRoutingStatsBorderTotal24HourIntervalEntry,
       "nncBTotal24HourIntervalNumber": nncBTotal24HourIntervalNumber,
       "nncBTotal24HourIntervalState": nncBTotal24HourIntervalState,
       "nncBTotal24HourIntervalAbsoluteIntervalNumber": nncBTotal24HourIntervalAbsoluteIntervalNumber,
       "nncBTotal24HourIntervalFailedCallsDueToInitLowerLvlDTLNotGen": nncBTotal24HourIntervalFailedCallsDueToInitLowerLvlDTLNotGen,
       "nncBTotal24HourIntervalCallsGeneratingInitLowerLvlDTLs": nncBTotal24HourIntervalCallsGeneratingInitLowerLvlDTLs,
       "nncBTotal24HourIntervalDTLGenCallsSuccessEstWithoutReroute": nncBTotal24HourIntervalDTLGenCallsSuccessEstWithoutReroute,
       "nncBTotal24HourIntervalDTLGenCallsSuccessEstWithReroute": nncBTotal24HourIntervalDTLGenCallsSuccessEstWithReroute,
       "nncBTotal24HourIntervalDTLGenCallsFailedInReRouting": nncBTotal24HourIntervalDTLGenCallsFailedInReRouting,
       "nncBTotal24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw": nncBTotal24HourIntervalSuccessCallsBdwGreaterThanRTDMinBdw,
       "nncBTotal24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw": nncBTotal24HourIntervalFailedCallsBdwGreaterThanRTDMinBdw,
       "nncBTotal24HourIntervalCrankbackReceivedAsAnEntryBorderNode": nncBTotal24HourIntervalCrankbackReceivedAsAnEntryBorderNode,
       "nncBTotal24HourIntervalLowerLvlDTLsGenDueToRecdCrankback": nncBTotal24HourIntervalLowerLvlDTLsGenDueToRecdCrankback,
       "nncBTotal24HourIntervalCallsRecdOverAnOutsideLink": nncBTotal24HourIntervalCallsRecdOverAnOutsideLink,
       "nncBTotal24HourIntervalCallsTransmittedOverAnOutsideLink": nncBTotal24HourIntervalCallsTransmittedOverAnOutsideLink,
       "nncBTotal24HourIntervalCrankbksRecdOverAnOutsideLink": nncBTotal24HourIntervalCrankbksRecdOverAnOutsideLink,
       "nncBTotal24HourIntervalSucdEndBlocCrankbksRecdOverOutsideLink": nncBTotal24HourIntervalSucdEndBlocCrankbksRecdOverOutsideLink,
       "nncBTotal24HourIntervalCrankbkFwdToPrevPGCrankbkLvlTooHigh": nncBTotal24HourIntervalCrankbkFwdToPrevPGCrankbkLvlTooHigh,
       "nncRoutingStatsRawCommonTable": nncRoutingStatsRawCommonTable,
       "nncRoutingStatsRawCommonEntry": nncRoutingStatsRawCommonEntry,
       "nncRoutingStatsRawCommonSuccessRoutedCallsOrigFromLocalSubs": nncRoutingStatsRawCommonSuccessRoutedCallsOrigFromLocalSubs,
       "nncRoutingStatsRawCommonSuccessRtedCallsTransitedViaThisNode": nncRoutingStatsRawCommonSuccessRtedCallsTransitedViaThisNode,
       "nncRoutingStatsRawCommonSuccessRoutedCallsTermToLocalSubs": nncRoutingStatsRawCommonSuccessRoutedCallsTermToLocalSubs,
       "nncRoutingStatsRawCommonSuccessRoutedLocalCalls": nncRoutingStatsRawCommonSuccessRoutedLocalCalls,
       "nncRoutingStatsRawCommonCallsOrigFromLocalCalls": nncRoutingStatsRawCommonCallsOrigFromLocalCalls,
       "nncRoutingStatsRawCommonCallsTermToLocalCalls": nncRoutingStatsRawCommonCallsTermToLocalCalls,
       "nncRoutingStatsRawCommonLocalCallAttempts": nncRoutingStatsRawCommonLocalCallAttempts,
       "nncRoutingStatsRawCommonCallsClearedDueToNoRoutingTabEntry": nncRoutingStatsRawCommonCallsClearedDueToNoRoutingTabEntry,
       "nncRoutingStatsRawCommonCrankbacksGeneratedByThisNode": nncRoutingStatsRawCommonCrankbacksGeneratedByThisNode,
       "nncRoutingStatsRawCommonFailedCallsAtLocalSubs": nncRoutingStatsRawCommonFailedCallsAtLocalSubs,
       "nncRoutingStatsRawCommonCallsSuccessRerouted": nncRoutingStatsRawCommonCallsSuccessRerouted,
       "nncRoutingStatsRawCommonCallsFailedInRerouting": nncRoutingStatsRawCommonCallsFailedInRerouting,
       "nncRoutingStatsRawSpecificTable": nncRoutingStatsRawSpecificTable,
       "nncRoutingStatsRawSpecificEntry": nncRoutingStatsRawSpecificEntry,
       "nncRoutingStatsRawSpecificCallsStaticallyRoutedByThisNode": nncRoutingStatsRawSpecificCallsStaticallyRoutedByThisNode,
       "nncRoutingStatsRawSpecificCrankbacksReceivedByThisNode": nncRoutingStatsRawSpecificCrankbacksReceivedByThisNode,
       "nncRoutingStatsRawSpecificRerouteAttempts": nncRoutingStatsRawSpecificRerouteAttempts,
       "nncRoutingStatsRawSpecificRoutingLoopsDetectedByThisNode": nncRoutingStatsRawSpecificRoutingLoopsDetectedByThisNode,
       "nncRoutingStatsRawNonBorderPerTblTable": nncRoutingStatsRawNonBorderPerTblTable,
       "nncRoutingStatsRawNonBorderPerTblEntry": nncRoutingStatsRawNonBorderPerTblEntry,
       "nncRawNBPerTbleTableDescriptor": nncRawNBPerTbleTableDescriptor,
       "nncRawNBPerTbleFailedCallsDueToInitDTLNotGenerated": nncRawNBPerTbleFailedCallsDueToInitDTLNotGenerated,
       "nncRawNBPerTbleCallsGeneratingAnInitDTL": nncRawNBPerTbleCallsGeneratingAnInitDTL,
       "nncRawNBPerTbleDTLOrigCallsSuccessEstWithoutReroute": nncRawNBPerTbleDTLOrigCallsSuccessEstWithoutReroute,
       "nncRawNBPerTbleDTLOrigCallsSuccessEstWithReroute": nncRawNBPerTbleDTLOrigCallsSuccessEstWithReroute,
       "nncRawNBPerTbleDTLOrigCallsFailedInReRouting": nncRawNBPerTbleDTLOrigCallsFailedInReRouting,
       "nncRawNBPerTbleSuccessCallsBdwGreaterThanRTDMinBdw": nncRawNBPerTbleSuccessCallsBdwGreaterThanRTDMinBdw,
       "nncRawNBPerTbleFailedCallsBdwGreaterThanRTDMinBdw": nncRawNBPerTbleFailedCallsBdwGreaterThanRTDMinBdw,
       "nncRawNBPerTbleCrankbackReceivedAsDTLOriginator": nncRawNBPerTbleCrankbackReceivedAsDTLOriginator,
       "nncRawNBPerTbleDTLsGeneratedDueToCrankback": nncRawNBPerTbleDTLsGeneratedDueToCrankback,
       "nncRoutingStatsRawBorderPerTblTable": nncRoutingStatsRawBorderPerTblTable,
       "nncRoutingStatsRawBorderPerTblEntry": nncRoutingStatsRawBorderPerTblEntry,
       "nncRawBPerTblTableDescriptor": nncRawBPerTblTableDescriptor,
       "nncRawBPerTblFailedCallsDueInitLowerLvlDTLsNotGen": nncRawBPerTblFailedCallsDueInitLowerLvlDTLsNotGen,
       "nncRawBPerTblCallsGeneratingInitLowerLvlDTLs": nncRawBPerTblCallsGeneratingInitLowerLvlDTLs,
       "nncRawBPerTblDTLGenCallsSuccessEstWithoutReroute": nncRawBPerTblDTLGenCallsSuccessEstWithoutReroute,
       "nncRawBPerTblDTLGenCallsSuccessEstWithReroute": nncRawBPerTblDTLGenCallsSuccessEstWithReroute,
       "nncRawBPerTblDTLGenCallsFailedInReRouting": nncRawBPerTblDTLGenCallsFailedInReRouting,
       "nncRawBPerTblSuccessCallsBdwGreaterThanRTDMinBdw": nncRawBPerTblSuccessCallsBdwGreaterThanRTDMinBdw,
       "nncRawBPerTblFailedCallsBdwGreaterThanRTDMinBdw": nncRawBPerTblFailedCallsBdwGreaterThanRTDMinBdw,
       "nncRawBPerTblCrankbackReceivedAsAnEntryBorderNode": nncRawBPerTblCrankbackReceivedAsAnEntryBorderNode,
       "nncRawBPerTblLowerLvlDTLsGenDueToRecdCrankback": nncRawBPerTblLowerLvlDTLsGenDueToRecdCrankback,
       "nncRoutingStatsRawNonBorderTotalTable": nncRoutingStatsRawNonBorderTotalTable,
       "nncRoutingStatsRawNonBorderTotalEntry": nncRoutingStatsRawNonBorderTotalEntry,
       "nncRawNBTotalFailedCallsDueToInitDTLNotGenerated": nncRawNBTotalFailedCallsDueToInitDTLNotGenerated,
       "nncRawNBTotalCallsGeneratingAnInitDTL": nncRawNBTotalCallsGeneratingAnInitDTL,
       "nncRawNBTotalDTLOrigCallsSuccessEstWithoutReroute": nncRawNBTotalDTLOrigCallsSuccessEstWithoutReroute,
       "nncRawNBTotalDTLOrigCallsSuccessEstWithReroute": nncRawNBTotalDTLOrigCallsSuccessEstWithReroute,
       "nncRawNBTotalDTLOrigCallsFailedInReRouting": nncRawNBTotalDTLOrigCallsFailedInReRouting,
       "nncRawNBTotalSuccessCallsBdwGreaterThanRTDMinBdw": nncRawNBTotalSuccessCallsBdwGreaterThanRTDMinBdw,
       "nncRawNBTotalFailedCallsBdwGreaterThanRTDMinBdw": nncRawNBTotalFailedCallsBdwGreaterThanRTDMinBdw,
       "nncRawNBTotalCrankbackReceivedAsDTLOriginator": nncRawNBTotalCrankbackReceivedAsDTLOriginator,
       "nncRawNBTotalDTLsGeneratedDueToCrankback": nncRawNBTotalDTLsGeneratedDueToCrankback,
       "nncRawNBTotalCallsRecdAsTransitNodeOverInsideLinks": nncRawNBTotalCallsRecdAsTransitNodeOverInsideLinks,
       "nncRawNBTotalCrnkbksRecdAsTransitNodeOvInsideLnks": nncRawNBTotalCrnkbksRecdAsTransitNodeOvInsideLnks,
       "nncRawNBTotalSucdEndBlocCrnkbksRecdOvInsideLnks": nncRawNBTotalSucdEndBlocCrnkbksRecdOvInsideLnks,
       "nncRoutingStatsRawBorderTotalTable": nncRoutingStatsRawBorderTotalTable,
       "nncRoutingStatsRawBorderTotalEntry": nncRoutingStatsRawBorderTotalEntry,
       "nncRawBTotalFailedCallsDueToInitLowerLvlDTLNotGen": nncRawBTotalFailedCallsDueToInitLowerLvlDTLNotGen,
       "nncRawBTotalCallsGeneratingInitLowerLvlDTLs": nncRawBTotalCallsGeneratingInitLowerLvlDTLs,
       "nncRawBTotalDTLGenCallsSuccessEstWithoutReroute": nncRawBTotalDTLGenCallsSuccessEstWithoutReroute,
       "nncRawBTotalDTLGenCallsSuccessEstWithReroute": nncRawBTotalDTLGenCallsSuccessEstWithReroute,
       "nncRawBTotalDTLGenCallsFailedInReRouting": nncRawBTotalDTLGenCallsFailedInReRouting,
       "nncRawBTotalSuccessCallsBdwGreaterThanRTDMinBdw": nncRawBTotalSuccessCallsBdwGreaterThanRTDMinBdw,
       "nncRawBTotalFailedCallsBdwGreaterThanRTDMinBdw": nncRawBTotalFailedCallsBdwGreaterThanRTDMinBdw,
       "nncRawBTotalCrankbackReceivedAsAnEntryBorderNode": nncRawBTotalCrankbackReceivedAsAnEntryBorderNode,
       "nncRawBTotalLowerLvlDTLsGenDueToRecdCrankback": nncRawBTotalLowerLvlDTLsGenDueToRecdCrankback,
       "nncRawBTotalCallsRecdOverAnOutsideLink": nncRawBTotalCallsRecdOverAnOutsideLink,
       "nncRawBTotalCallsTransmittedOverAnOutsideLink": nncRawBTotalCallsTransmittedOverAnOutsideLink,
       "nncRawBTotalCrankbksRecdOverAnOutsideLink": nncRawBTotalCrankbksRecdOverAnOutsideLink,
       "nncRawBTotalSucdEndBlocCrankbksRecdOverOutsideLink": nncRawBTotalSucdEndBlocCrankbksRecdOverOutsideLink,
       "nncRawBTotalCrankbkForwdedToPrevPGCrankbkLvlTooHigh": nncRawBTotalCrankbkForwdedToPrevPGCrankbkLvlTooHigh,
       "nncRoutingStatsGroups": nncRoutingStatsGroups,
       "nncRoutingStatsCommon15MinCurrentGroup": nncRoutingStatsCommon15MinCurrentGroup,
       "nncRoutingStatsCommon15MinIntervalGroup": nncRoutingStatsCommon15MinIntervalGroup,
       "nncRoutingStatsCommon24HourCurrentGroup": nncRoutingStatsCommon24HourCurrentGroup,
       "nncRoutingStatsCommon24HourIntervalGroup": nncRoutingStatsCommon24HourIntervalGroup,
       "nncRoutingStatsSpecific15MinCurrentGroup": nncRoutingStatsSpecific15MinCurrentGroup,
       "nncRoutingStatsSpecific15MinIntervalGroup": nncRoutingStatsSpecific15MinIntervalGroup,
       "nncRoutingStatsSpecific24HourCurrentGroup": nncRoutingStatsSpecific24HourCurrentGroup,
       "nncRoutingStatsSpecific24HourIntervalGroup": nncRoutingStatsSpecific24HourIntervalGroup,
       "nncRoutingStatsNonBorderPerTbl15MinCurrentGroup": nncRoutingStatsNonBorderPerTbl15MinCurrentGroup,
       "nncRoutingStatsNonBorderPerTbl15MinIntervalGroup": nncRoutingStatsNonBorderPerTbl15MinIntervalGroup,
       "nncRoutingStatsNonBorderPerTbl24HourCurrentGroup": nncRoutingStatsNonBorderPerTbl24HourCurrentGroup,
       "nncRoutingStatsNonBorderPerTbl24HourIntervalGroup": nncRoutingStatsNonBorderPerTbl24HourIntervalGroup,
       "nncRoutingStatsBorderPerTbl15MinCurrentGroup": nncRoutingStatsBorderPerTbl15MinCurrentGroup,
       "nncRoutingStatsBorderPerTbl15MinIntervalGroup": nncRoutingStatsBorderPerTbl15MinIntervalGroup,
       "nncRoutingStatsBorderPerTbl24HourCurrentGroup": nncRoutingStatsBorderPerTbl24HourCurrentGroup,
       "nncRoutingStatsBorderPerTbl24HourIntervalGroup": nncRoutingStatsBorderPerTbl24HourIntervalGroup,
       "nncPNNIStatNonBorderTotal15MinCurrentGroup": nncPNNIStatNonBorderTotal15MinCurrentGroup,
       "nncPNNIStatNonBorderTotal15MinIntervalGroup": nncPNNIStatNonBorderTotal15MinIntervalGroup,
       "nncPNNIStatNonBorderTotal24HourCurrentGroup": nncPNNIStatNonBorderTotal24HourCurrentGroup,
       "nncPNNIStatNonBorderTotal24HourIntervalGroup": nncPNNIStatNonBorderTotal24HourIntervalGroup,
       "nncPNNIStatBorderTotal15MinCurrentGroup": nncPNNIStatBorderTotal15MinCurrentGroup,
       "nncPNNIStatBorderTotal15MinIntervalGroup": nncPNNIStatBorderTotal15MinIntervalGroup,
       "nncPNNIStatBorderTotal24HourCurrentGroup": nncPNNIStatBorderTotal24HourCurrentGroup,
       "nncPNNIStatBorderTotal24HourIntervalGroup": nncPNNIStatBorderTotal24HourIntervalGroup,
       "nncRoutingStatsRawCommonGroup": nncRoutingStatsRawCommonGroup,
       "ncExtRoutingStatsRawSpecificGroup": ncExtRoutingStatsRawSpecificGroup,
       "nncRoutingStatsRawNonBorderPerTblGroup": nncRoutingStatsRawNonBorderPerTblGroup,
       "nncRoutingStatsRawBorderPerTblGroup": nncRoutingStatsRawBorderPerTblGroup,
       "nncPNNIStatRawNonBorderTotalGroup": nncPNNIStatRawNonBorderTotalGroup,
       "nncRoutingStatsRawBorderTotalGroup": nncRoutingStatsRawBorderTotalGroup,
       "nncRoutingStatsCompliances": nncRoutingStatsCompliances,
       "nncRoutingStatsCompliances1": nncRoutingStatsCompliances1,
       "nncRoutingStatsCompliances2": nncRoutingStatsCompliances2,
       "nncRoutingStatsCompliances3": nncRoutingStatsCompliances3}
)
