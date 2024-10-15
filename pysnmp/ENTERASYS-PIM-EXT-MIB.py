# SNMP MIB module (ENTERASYS-PIM-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-PIM-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:20 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(InetVersion,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetVersion")

(pimAnycastRPSetEntry,
 pimGroupMappingEntry,
 pimInterfaceEntry,
 pimNeighborEntry,
 pimStaticRPEntry) = mibBuilder.importSymbols(
    "PIM-STD-MIB",
    "pimAnycastRPSetEntry",
    "pimGroupMappingEntry",
    "pimInterfaceEntry",
    "pimNeighborEntry",
    "pimStaticRPEntry")

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

etsysPimExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67)
)
etsysPimExtMIB.setRevisions(
        ("2009-02-24 22:32",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysPimExtObjects_ObjectIdentity = ObjectIdentity
etsysPimExtObjects = _EtsysPimExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1)
)
_EtsysPimExtGlobals_ObjectIdentity = ObjectIdentity
etsysPimExtGlobals = _EtsysPimExtGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 1)
)
_EtsysPimExtTables_ObjectIdentity = ObjectIdentity
etsysPimExtTables = _EtsysPimExtTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2)
)
_EtsysPimExtIfTable_Object = MibTable
etsysPimExtIfTable = _EtsysPimExtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysPimExtIfTable.setStatus("current")
_EtsysPimExtIfEntry_Object = MibTableRow
etsysPimExtIfEntry = _EtsysPimExtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    etsysPimExtIfEntry.setStatus("current")


class _EtsysPimExtIfAdminStatus_Type(Integer32):
    """Custom type etsysPimExtIfAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminStatusDown", 2),
          ("adminStatusUp", 1))
    )


_EtsysPimExtIfAdminStatus_Type.__name__ = "Integer32"
_EtsysPimExtIfAdminStatus_Object = MibTableColumn
etsysPimExtIfAdminStatus = _EtsysPimExtIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 1, 1, 1),
    _EtsysPimExtIfAdminStatus_Type()
)
etsysPimExtIfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPimExtIfAdminStatus.setStatus("current")


class _EtsysPimExtIfOperStatus_Type(Integer32):
    """Custom type etsysPimExtIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("operStatusActFailed", 5),
          ("operStatusDown", 2),
          ("operStatusFailed", 8),
          ("operStatusFailedPerm", 10),
          ("operStatusFailing", 11),
          ("operStatusGoingDown", 4),
          ("operStatusGoingUp", 3),
          ("operStatusUp", 1))
    )


_EtsysPimExtIfOperStatus_Type.__name__ = "Integer32"
_EtsysPimExtIfOperStatus_Object = MibTableColumn
etsysPimExtIfOperStatus = _EtsysPimExtIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 1, 1, 2),
    _EtsysPimExtIfOperStatus_Type()
)
etsysPimExtIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtIfOperStatus.setStatus("current")


class _EtsysPimExtIfP2PNoHellos_Type(TruthValue):
    """Custom type etsysPimExtIfP2PNoHellos based on TruthValue"""


_EtsysPimExtIfP2PNoHellos_Object = MibTableColumn
etsysPimExtIfP2PNoHellos = _EtsysPimExtIfP2PNoHellos_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 1, 1, 3),
    _EtsysPimExtIfP2PNoHellos_Type()
)
etsysPimExtIfP2PNoHellos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPimExtIfP2PNoHellos.setStatus("current")
_EtsysPimExtIfNeighborCount_Type = Gauge32
_EtsysPimExtIfNeighborCount_Object = MibTableColumn
etsysPimExtIfNeighborCount = _EtsysPimExtIfNeighborCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 1, 1, 4),
    _EtsysPimExtIfNeighborCount_Type()
)
etsysPimExtIfNeighborCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtIfNeighborCount.setStatus("current")


class _EtsysPimExtIfStarGStateLimit_Type(Unsigned32):
    """Custom type etsysPimExtIfStarGStateLimit based on Unsigned32"""
    defaultValue = 0


_EtsysPimExtIfStarGStateLimit_Object = MibTableColumn
etsysPimExtIfStarGStateLimit = _EtsysPimExtIfStarGStateLimit_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 1, 1, 5),
    _EtsysPimExtIfStarGStateLimit_Type()
)
etsysPimExtIfStarGStateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPimExtIfStarGStateLimit.setStatus("current")


class _EtsysPimExtIfStarGStateWarnThold_Type(Unsigned32):
    """Custom type etsysPimExtIfStarGStateWarnThold based on Unsigned32"""
    defaultValue = 0


_EtsysPimExtIfStarGStateWarnThold_Object = MibTableColumn
etsysPimExtIfStarGStateWarnThold = _EtsysPimExtIfStarGStateWarnThold_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 1, 1, 6),
    _EtsysPimExtIfStarGStateWarnThold_Type()
)
etsysPimExtIfStarGStateWarnThold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPimExtIfStarGStateWarnThold.setStatus("current")
_EtsysPimExtIfStarGStateStored_Type = Gauge32
_EtsysPimExtIfStarGStateStored_Object = MibTableColumn
etsysPimExtIfStarGStateStored = _EtsysPimExtIfStarGStateStored_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 1, 1, 7),
    _EtsysPimExtIfStarGStateStored_Type()
)
etsysPimExtIfStarGStateStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtIfStarGStateStored.setStatus("current")


class _EtsysPimExtIfSGStateLimit_Type(Unsigned32):
    """Custom type etsysPimExtIfSGStateLimit based on Unsigned32"""
    defaultValue = 0


_EtsysPimExtIfSGStateLimit_Object = MibTableColumn
etsysPimExtIfSGStateLimit = _EtsysPimExtIfSGStateLimit_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 1, 1, 8),
    _EtsysPimExtIfSGStateLimit_Type()
)
etsysPimExtIfSGStateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPimExtIfSGStateLimit.setStatus("current")


class _EtsysPimExtIfSGStateWarnThold_Type(Unsigned32):
    """Custom type etsysPimExtIfSGStateWarnThold based on Unsigned32"""
    defaultValue = 0


_EtsysPimExtIfSGStateWarnThold_Object = MibTableColumn
etsysPimExtIfSGStateWarnThold = _EtsysPimExtIfSGStateWarnThold_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 1, 1, 9),
    _EtsysPimExtIfSGStateWarnThold_Type()
)
etsysPimExtIfSGStateWarnThold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPimExtIfSGStateWarnThold.setStatus("current")
_EtsysPimExtIfSGStateStored_Type = Gauge32
_EtsysPimExtIfSGStateStored_Object = MibTableColumn
etsysPimExtIfSGStateStored = _EtsysPimExtIfSGStateStored_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 1, 1, 10),
    _EtsysPimExtIfSGStateStored_Type()
)
etsysPimExtIfSGStateStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtIfSGStateStored.setStatus("current")


class _EtsysPimExtIfAssertInterval_Type(Unsigned32):
    """Custom type etsysPimExtIfAssertInterval based on Unsigned32"""
    defaultValue = 177

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EtsysPimExtIfAssertInterval_Type.__name__ = "Unsigned32"
_EtsysPimExtIfAssertInterval_Object = MibTableColumn
etsysPimExtIfAssertInterval = _EtsysPimExtIfAssertInterval_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 1, 1, 11),
    _EtsysPimExtIfAssertInterval_Type()
)
etsysPimExtIfAssertInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPimExtIfAssertInterval.setStatus("current")
if mibBuilder.loadTexts:
    etsysPimExtIfAssertInterval.setUnits("seconds")


class _EtsysPimExtIfAssertHoldtime_Type(Unsigned32):
    """Custom type etsysPimExtIfAssertHoldtime based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EtsysPimExtIfAssertHoldtime_Type.__name__ = "Unsigned32"
_EtsysPimExtIfAssertHoldtime_Object = MibTableColumn
etsysPimExtIfAssertHoldtime = _EtsysPimExtIfAssertHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 1, 1, 12),
    _EtsysPimExtIfAssertHoldtime_Type()
)
etsysPimExtIfAssertHoldtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPimExtIfAssertHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    etsysPimExtIfAssertHoldtime.setUnits("seconds")
_EtsysPimExtStaticRPTable_Object = MibTable
etsysPimExtStaticRPTable = _EtsysPimExtStaticRPTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 2)
)
if mibBuilder.loadTexts:
    etsysPimExtStaticRPTable.setStatus("current")
_EtsysPimExtStaticRPEntry_Object = MibTableRow
etsysPimExtStaticRPEntry = _EtsysPimExtStaticRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysPimExtStaticRPEntry.setStatus("current")


class _EtsysPimExtStaticRPAdminStatus_Type(Integer32):
    """Custom type etsysPimExtStaticRPAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminStatusDown", 2),
          ("adminStatusUp", 1))
    )


_EtsysPimExtStaticRPAdminStatus_Type.__name__ = "Integer32"
_EtsysPimExtStaticRPAdminStatus_Object = MibTableColumn
etsysPimExtStaticRPAdminStatus = _EtsysPimExtStaticRPAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 2, 1, 1),
    _EtsysPimExtStaticRPAdminStatus_Type()
)
etsysPimExtStaticRPAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPimExtStaticRPAdminStatus.setStatus("current")
_EtsysPimExtAnycastRPSetTable_Object = MibTable
etsysPimExtAnycastRPSetTable = _EtsysPimExtAnycastRPSetTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 3)
)
if mibBuilder.loadTexts:
    etsysPimExtAnycastRPSetTable.setStatus("current")
_EtsysPimExtAnycastRPSetEntry_Object = MibTableRow
etsysPimExtAnycastRPSetEntry = _EtsysPimExtAnycastRPSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    etsysPimExtAnycastRPSetEntry.setStatus("current")


class _EtsysPimExtAnycastRPSetAdminStatus_Type(Integer32):
    """Custom type etsysPimExtAnycastRPSetAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminStatusDown", 2),
          ("adminStatusUp", 1))
    )


_EtsysPimExtAnycastRPSetAdminStatus_Type.__name__ = "Integer32"
_EtsysPimExtAnycastRPSetAdminStatus_Object = MibTableColumn
etsysPimExtAnycastRPSetAdminStatus = _EtsysPimExtAnycastRPSetAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 3, 1, 1),
    _EtsysPimExtAnycastRPSetAdminStatus_Type()
)
etsysPimExtAnycastRPSetAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPimExtAnycastRPSetAdminStatus.setStatus("current")
_EtsysPimExtGroupMappingTable_Object = MibTable
etsysPimExtGroupMappingTable = _EtsysPimExtGroupMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 4)
)
if mibBuilder.loadTexts:
    etsysPimExtGroupMappingTable.setStatus("current")
_EtsysPimExtGroupMappingEntry_Object = MibTableRow
etsysPimExtGroupMappingEntry = _EtsysPimExtGroupMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    etsysPimExtGroupMappingEntry.setStatus("current")
_EtsysPimExtGroupMappingIsInactive_Type = TruthValue
_EtsysPimExtGroupMappingIsInactive_Object = MibTableColumn
etsysPimExtGroupMappingIsInactive = _EtsysPimExtGroupMappingIsInactive_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 4, 1, 1),
    _EtsysPimExtGroupMappingIsInactive_Type()
)
etsysPimExtGroupMappingIsInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtGroupMappingIsInactive.setStatus("current")
_EtsysPimExtNbrStatsTable_Object = MibTable
etsysPimExtNbrStatsTable = _EtsysPimExtNbrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 5)
)
if mibBuilder.loadTexts:
    etsysPimExtNbrStatsTable.setStatus("current")
_EtsysPimExtNbrStatsEntry_Object = MibTableRow
etsysPimExtNbrStatsEntry = _EtsysPimExtNbrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    etsysPimExtNbrStatsEntry.setStatus("current")
_EtsysPimExtNbrStatsNumRecvHello_Type = Counter32
_EtsysPimExtNbrStatsNumRecvHello_Object = MibTableColumn
etsysPimExtNbrStatsNumRecvHello = _EtsysPimExtNbrStatsNumRecvHello_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 5, 1, 1),
    _EtsysPimExtNbrStatsNumRecvHello_Type()
)
etsysPimExtNbrStatsNumRecvHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtNbrStatsNumRecvHello.setStatus("current")
_EtsysPimExtNbrStatsNumRecvJoinPrune_Type = Counter32
_EtsysPimExtNbrStatsNumRecvJoinPrune_Object = MibTableColumn
etsysPimExtNbrStatsNumRecvJoinPrune = _EtsysPimExtNbrStatsNumRecvJoinPrune_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 5, 1, 2),
    _EtsysPimExtNbrStatsNumRecvJoinPrune_Type()
)
etsysPimExtNbrStatsNumRecvJoinPrune.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtNbrStatsNumRecvJoinPrune.setStatus("current")
_EtsysPimExtNbrStatsNumRecvAssert_Type = Counter32
_EtsysPimExtNbrStatsNumRecvAssert_Object = MibTableColumn
etsysPimExtNbrStatsNumRecvAssert = _EtsysPimExtNbrStatsNumRecvAssert_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 5, 1, 3),
    _EtsysPimExtNbrStatsNumRecvAssert_Type()
)
etsysPimExtNbrStatsNumRecvAssert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtNbrStatsNumRecvAssert.setStatus("current")
_EtsysPimExtNbrStatsNumRecvBSM_Type = Counter32
_EtsysPimExtNbrStatsNumRecvBSM_Object = MibTableColumn
etsysPimExtNbrStatsNumRecvBSM = _EtsysPimExtNbrStatsNumRecvBSM_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 5, 1, 4),
    _EtsysPimExtNbrStatsNumRecvBSM_Type()
)
etsysPimExtNbrStatsNumRecvBSM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtNbrStatsNumRecvBSM.setStatus("current")
_EtsysPimExtNbrStatsNumErrJoinPrune_Type = Counter32
_EtsysPimExtNbrStatsNumErrJoinPrune_Object = MibTableColumn
etsysPimExtNbrStatsNumErrJoinPrune = _EtsysPimExtNbrStatsNumErrJoinPrune_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 5, 1, 5),
    _EtsysPimExtNbrStatsNumErrJoinPrune_Type()
)
etsysPimExtNbrStatsNumErrJoinPrune.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtNbrStatsNumErrJoinPrune.setStatus("current")
_EtsysPimExtNbrStatsNumErrAssert_Type = Counter32
_EtsysPimExtNbrStatsNumErrAssert_Object = MibTableColumn
etsysPimExtNbrStatsNumErrAssert = _EtsysPimExtNbrStatsNumErrAssert_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 5, 1, 6),
    _EtsysPimExtNbrStatsNumErrAssert_Type()
)
etsysPimExtNbrStatsNumErrAssert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtNbrStatsNumErrAssert.setStatus("current")
_EtsysPimExtNbrStatsNumErrBSM_Type = Counter32
_EtsysPimExtNbrStatsNumErrBSM_Object = MibTableColumn
etsysPimExtNbrStatsNumErrBSM = _EtsysPimExtNbrStatsNumErrBSM_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 5, 1, 7),
    _EtsysPimExtNbrStatsNumErrBSM_Type()
)
etsysPimExtNbrStatsNumErrBSM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtNbrStatsNumErrBSM.setStatus("current")
_EtsysPimExtIfStatsTable_Object = MibTable
etsysPimExtIfStatsTable = _EtsysPimExtIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 6)
)
if mibBuilder.loadTexts:
    etsysPimExtIfStatsTable.setStatus("current")
_EtsysPimExtIfStatsEntry_Object = MibTableRow
etsysPimExtIfStatsEntry = _EtsysPimExtIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    etsysPimExtIfStatsEntry.setStatus("current")
_EtsysPimExtIfStatsNumSentHello_Type = Counter32
_EtsysPimExtIfStatsNumSentHello_Object = MibTableColumn
etsysPimExtIfStatsNumSentHello = _EtsysPimExtIfStatsNumSentHello_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 6, 1, 1),
    _EtsysPimExtIfStatsNumSentHello_Type()
)
etsysPimExtIfStatsNumSentHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtIfStatsNumSentHello.setStatus("current")
_EtsysPimExtIfStatsNumSentJoinPrune_Type = Counter32
_EtsysPimExtIfStatsNumSentJoinPrune_Object = MibTableColumn
etsysPimExtIfStatsNumSentJoinPrune = _EtsysPimExtIfStatsNumSentJoinPrune_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 6, 1, 2),
    _EtsysPimExtIfStatsNumSentJoinPrune_Type()
)
etsysPimExtIfStatsNumSentJoinPrune.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtIfStatsNumSentJoinPrune.setStatus("current")
_EtsysPimExtIfStatsNumSentAssert_Type = Counter32
_EtsysPimExtIfStatsNumSentAssert_Object = MibTableColumn
etsysPimExtIfStatsNumSentAssert = _EtsysPimExtIfStatsNumSentAssert_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 6, 1, 3),
    _EtsysPimExtIfStatsNumSentAssert_Type()
)
etsysPimExtIfStatsNumSentAssert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtIfStatsNumSentAssert.setStatus("current")
_EtsysPimExtIfStatsNumSentBsm_Type = Counter32
_EtsysPimExtIfStatsNumSentBsm_Object = MibTableColumn
etsysPimExtIfStatsNumSentBsm = _EtsysPimExtIfStatsNumSentBsm_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 6, 1, 4),
    _EtsysPimExtIfStatsNumSentBsm_Type()
)
etsysPimExtIfStatsNumSentBsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtIfStatsNumSentBsm.setStatus("current")
_EtsysPimExtIfStatsNumErrHello_Type = Counter32
_EtsysPimExtIfStatsNumErrHello_Object = MibTableColumn
etsysPimExtIfStatsNumErrHello = _EtsysPimExtIfStatsNumErrHello_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 6, 1, 5),
    _EtsysPimExtIfStatsNumErrHello_Type()
)
etsysPimExtIfStatsNumErrHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtIfStatsNumErrHello.setStatus("current")
_EtsysPimExtIfStatsNumRecvUnknownNbr_Type = Counter32
_EtsysPimExtIfStatsNumRecvUnknownNbr_Object = MibTableColumn
etsysPimExtIfStatsNumRecvUnknownNbr = _EtsysPimExtIfStatsNumRecvUnknownNbr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 6, 1, 6),
    _EtsysPimExtIfStatsNumRecvUnknownNbr_Type()
)
etsysPimExtIfStatsNumRecvUnknownNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtIfStatsNumRecvUnknownNbr.setStatus("current")
_EtsysPimExtIfStatsNumUnknownHelloOpt_Type = Counter32
_EtsysPimExtIfStatsNumUnknownHelloOpt_Object = MibTableColumn
etsysPimExtIfStatsNumUnknownHelloOpt = _EtsysPimExtIfStatsNumUnknownHelloOpt_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 6, 1, 7),
    _EtsysPimExtIfStatsNumUnknownHelloOpt_Type()
)
etsysPimExtIfStatsNumUnknownHelloOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtIfStatsNumUnknownHelloOpt.setStatus("current")
_EtsysPimExtNbrMgrTable_Object = MibTable
etsysPimExtNbrMgrTable = _EtsysPimExtNbrMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 7)
)
if mibBuilder.loadTexts:
    etsysPimExtNbrMgrTable.setStatus("current")
_EtsysPimExtNbrMgrEntry_Object = MibTableRow
etsysPimExtNbrMgrEntry = _EtsysPimExtNbrMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 7, 1)
)
etsysPimExtNbrMgrEntry.setIndexNames(
    (0, "ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrMgrIndex"),
)
if mibBuilder.loadTexts:
    etsysPimExtNbrMgrEntry.setStatus("current")
_EtsysPimExtNbrMgrIndex_Type = InetVersion
_EtsysPimExtNbrMgrIndex_Object = MibTableColumn
etsysPimExtNbrMgrIndex = _EtsysPimExtNbrMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 7, 1, 1),
    _EtsysPimExtNbrMgrIndex_Type()
)
etsysPimExtNbrMgrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysPimExtNbrMgrIndex.setStatus("current")


class _EtsysPimExtNbrMgrEnableUnicastMessages_Type(TruthValue):
    """Custom type etsysPimExtNbrMgrEnableUnicastMessages based on TruthValue"""


_EtsysPimExtNbrMgrEnableUnicastMessages_Object = MibTableColumn
etsysPimExtNbrMgrEnableUnicastMessages = _EtsysPimExtNbrMgrEnableUnicastMessages_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 7, 1, 2),
    _EtsysPimExtNbrMgrEnableUnicastMessages_Type()
)
etsysPimExtNbrMgrEnableUnicastMessages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPimExtNbrMgrEnableUnicastMessages.setStatus("current")


class _EtsysPimExtNbrMgrAcceptUnicastBsms_Type(TruthValue):
    """Custom type etsysPimExtNbrMgrAcceptUnicastBsms based on TruthValue"""


_EtsysPimExtNbrMgrAcceptUnicastBsms_Object = MibTableColumn
etsysPimExtNbrMgrAcceptUnicastBsms = _EtsysPimExtNbrMgrAcceptUnicastBsms_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 7, 1, 3),
    _EtsysPimExtNbrMgrAcceptUnicastBsms_Type()
)
etsysPimExtNbrMgrAcceptUnicastBsms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPimExtNbrMgrAcceptUnicastBsms.setStatus("current")
_EtsysPimExtNbrMgrNumSentCRPAdvert_Type = Counter32
_EtsysPimExtNbrMgrNumSentCRPAdvert_Object = MibTableColumn
etsysPimExtNbrMgrNumSentCRPAdvert = _EtsysPimExtNbrMgrNumSentCRPAdvert_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 7, 1, 4),
    _EtsysPimExtNbrMgrNumSentCRPAdvert_Type()
)
etsysPimExtNbrMgrNumSentCRPAdvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtNbrMgrNumSentCRPAdvert.setStatus("current")
_EtsysPimExtNbrMgrNumSentRegister_Type = Counter32
_EtsysPimExtNbrMgrNumSentRegister_Object = MibTableColumn
etsysPimExtNbrMgrNumSentRegister = _EtsysPimExtNbrMgrNumSentRegister_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 7, 1, 5),
    _EtsysPimExtNbrMgrNumSentRegister_Type()
)
etsysPimExtNbrMgrNumSentRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtNbrMgrNumSentRegister.setStatus("current")
_EtsysPimExtNbrMgrNumSentRegisterStop_Type = Counter32
_EtsysPimExtNbrMgrNumSentRegisterStop_Object = MibTableColumn
etsysPimExtNbrMgrNumSentRegisterStop = _EtsysPimExtNbrMgrNumSentRegisterStop_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 7, 1, 6),
    _EtsysPimExtNbrMgrNumSentRegisterStop_Type()
)
etsysPimExtNbrMgrNumSentRegisterStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtNbrMgrNumSentRegisterStop.setStatus("current")
_EtsysPimExtNbrMgrNumRecvCRPAdvert_Type = Counter32
_EtsysPimExtNbrMgrNumRecvCRPAdvert_Object = MibTableColumn
etsysPimExtNbrMgrNumRecvCRPAdvert = _EtsysPimExtNbrMgrNumRecvCRPAdvert_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 7, 1, 7),
    _EtsysPimExtNbrMgrNumRecvCRPAdvert_Type()
)
etsysPimExtNbrMgrNumRecvCRPAdvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtNbrMgrNumRecvCRPAdvert.setStatus("current")
_EtsysPimExtNbrMgrNumRecvRegister_Type = Counter32
_EtsysPimExtNbrMgrNumRecvRegister_Object = MibTableColumn
etsysPimExtNbrMgrNumRecvRegister = _EtsysPimExtNbrMgrNumRecvRegister_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 7, 1, 8),
    _EtsysPimExtNbrMgrNumRecvRegister_Type()
)
etsysPimExtNbrMgrNumRecvRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtNbrMgrNumRecvRegister.setStatus("current")
_EtsysPimExtNbrMgrNumRecvRegisterStop_Type = Counter32
_EtsysPimExtNbrMgrNumRecvRegisterStop_Object = MibTableColumn
etsysPimExtNbrMgrNumRecvRegisterStop = _EtsysPimExtNbrMgrNumRecvRegisterStop_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 7, 1, 9),
    _EtsysPimExtNbrMgrNumRecvRegisterStop_Type()
)
etsysPimExtNbrMgrNumRecvRegisterStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtNbrMgrNumRecvRegisterStop.setStatus("current")
_EtsysPimExtNbrMgrNumErrCRPAdvert_Type = Counter32
_EtsysPimExtNbrMgrNumErrCRPAdvert_Object = MibTableColumn
etsysPimExtNbrMgrNumErrCRPAdvert = _EtsysPimExtNbrMgrNumErrCRPAdvert_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 7, 1, 10),
    _EtsysPimExtNbrMgrNumErrCRPAdvert_Type()
)
etsysPimExtNbrMgrNumErrCRPAdvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtNbrMgrNumErrCRPAdvert.setStatus("current")
_EtsysPimExtNbrMgrNumErrRegister_Type = Counter32
_EtsysPimExtNbrMgrNumErrRegister_Object = MibTableColumn
etsysPimExtNbrMgrNumErrRegister = _EtsysPimExtNbrMgrNumErrRegister_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 7, 1, 11),
    _EtsysPimExtNbrMgrNumErrRegister_Type()
)
etsysPimExtNbrMgrNumErrRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtNbrMgrNumErrRegister.setStatus("current")
_EtsysPimExtNbrMgrNumErrRegisterStop_Type = Counter32
_EtsysPimExtNbrMgrNumErrRegisterStop_Object = MibTableColumn
etsysPimExtNbrMgrNumErrRegisterStop = _EtsysPimExtNbrMgrNumErrRegisterStop_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 7, 1, 12),
    _EtsysPimExtNbrMgrNumErrRegisterStop_Type()
)
etsysPimExtNbrMgrNumErrRegisterStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtNbrMgrNumErrRegisterStop.setStatus("current")
_EtsysPimExtNbrMgrNumRecvIgnoredType_Type = Counter32
_EtsysPimExtNbrMgrNumRecvIgnoredType_Object = MibTableColumn
etsysPimExtNbrMgrNumRecvIgnoredType = _EtsysPimExtNbrMgrNumRecvIgnoredType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 7, 1, 13),
    _EtsysPimExtNbrMgrNumRecvIgnoredType_Type()
)
etsysPimExtNbrMgrNumRecvIgnoredType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtNbrMgrNumRecvIgnoredType.setStatus("current")
_EtsysPimExtNbrMgrNumRecvUnknownType_Type = Counter32
_EtsysPimExtNbrMgrNumRecvUnknownType_Object = MibTableColumn
etsysPimExtNbrMgrNumRecvUnknownType = _EtsysPimExtNbrMgrNumRecvUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 7, 1, 14),
    _EtsysPimExtNbrMgrNumRecvUnknownType_Type()
)
etsysPimExtNbrMgrNumRecvUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtNbrMgrNumRecvUnknownType.setStatus("current")
_EtsysPimExtNbrMgrNumRecvUnknownVer_Type = Counter32
_EtsysPimExtNbrMgrNumRecvUnknownVer_Object = MibTableColumn
etsysPimExtNbrMgrNumRecvUnknownVer = _EtsysPimExtNbrMgrNumRecvUnknownVer_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 7, 1, 15),
    _EtsysPimExtNbrMgrNumRecvUnknownVer_Type()
)
etsysPimExtNbrMgrNumRecvUnknownVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtNbrMgrNumRecvUnknownVer.setStatus("current")
_EtsysPimExtNbrMgrNumRecvBadChecksum_Type = Counter32
_EtsysPimExtNbrMgrNumRecvBadChecksum_Object = MibTableColumn
etsysPimExtNbrMgrNumRecvBadChecksum = _EtsysPimExtNbrMgrNumRecvBadChecksum_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 7, 1, 16),
    _EtsysPimExtNbrMgrNumRecvBadChecksum_Type()
)
etsysPimExtNbrMgrNumRecvBadChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtNbrMgrNumRecvBadChecksum.setStatus("current")
_EtsysPimExtNbrMgrNumRecvBadLength_Type = Counter32
_EtsysPimExtNbrMgrNumRecvBadLength_Object = MibTableColumn
etsysPimExtNbrMgrNumRecvBadLength = _EtsysPimExtNbrMgrNumRecvBadLength_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 7, 1, 17),
    _EtsysPimExtNbrMgrNumRecvBadLength_Type()
)
etsysPimExtNbrMgrNumRecvBadLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtNbrMgrNumRecvBadLength.setStatus("current")
_EtsysPimExtTibMgrTable_Object = MibTable
etsysPimExtTibMgrTable = _EtsysPimExtTibMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 8)
)
if mibBuilder.loadTexts:
    etsysPimExtTibMgrTable.setStatus("current")
_EtsysPimExtTibMgrEntry_Object = MibTableRow
etsysPimExtTibMgrEntry = _EtsysPimExtTibMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 8, 1)
)
etsysPimExtTibMgrEntry.setIndexNames(
    (0, "ENTERASYS-PIM-EXT-MIB", "etsysPimExtTibMgrIndex"),
)
if mibBuilder.loadTexts:
    etsysPimExtTibMgrEntry.setStatus("current")
_EtsysPimExtTibMgrIndex_Type = InetVersion
_EtsysPimExtTibMgrIndex_Object = MibTableColumn
etsysPimExtTibMgrIndex = _EtsysPimExtTibMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 8, 1, 1),
    _EtsysPimExtTibMgrIndex_Type()
)
etsysPimExtTibMgrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysPimExtTibMgrIndex.setStatus("current")


class _EtsysPimExtTibMgrGStateLimit_Type(Unsigned32):
    """Custom type etsysPimExtTibMgrGStateLimit based on Unsigned32"""
    defaultValue = 0


_EtsysPimExtTibMgrGStateLimit_Object = MibTableColumn
etsysPimExtTibMgrGStateLimit = _EtsysPimExtTibMgrGStateLimit_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 8, 1, 2),
    _EtsysPimExtTibMgrGStateLimit_Type()
)
etsysPimExtTibMgrGStateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPimExtTibMgrGStateLimit.setStatus("current")


class _EtsysPimExtTibMgrGStateWarnThold_Type(Unsigned32):
    """Custom type etsysPimExtTibMgrGStateWarnThold based on Unsigned32"""
    defaultValue = 0


_EtsysPimExtTibMgrGStateWarnThold_Object = MibTableColumn
etsysPimExtTibMgrGStateWarnThold = _EtsysPimExtTibMgrGStateWarnThold_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 8, 1, 3),
    _EtsysPimExtTibMgrGStateWarnThold_Type()
)
etsysPimExtTibMgrGStateWarnThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPimExtTibMgrGStateWarnThold.setStatus("current")
_EtsysPimExtTibMgrGStateStored_Type = Gauge32
_EtsysPimExtTibMgrGStateStored_Object = MibTableColumn
etsysPimExtTibMgrGStateStored = _EtsysPimExtTibMgrGStateStored_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 8, 1, 4),
    _EtsysPimExtTibMgrGStateStored_Type()
)
etsysPimExtTibMgrGStateStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtTibMgrGStateStored.setStatus("current")


class _EtsysPimExtTibMgrSGStateLimit_Type(Unsigned32):
    """Custom type etsysPimExtTibMgrSGStateLimit based on Unsigned32"""
    defaultValue = 0


_EtsysPimExtTibMgrSGStateLimit_Object = MibTableColumn
etsysPimExtTibMgrSGStateLimit = _EtsysPimExtTibMgrSGStateLimit_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 8, 1, 5),
    _EtsysPimExtTibMgrSGStateLimit_Type()
)
etsysPimExtTibMgrSGStateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPimExtTibMgrSGStateLimit.setStatus("current")


class _EtsysPimExtTibMgrSGStateWarnThold_Type(Unsigned32):
    """Custom type etsysPimExtTibMgrSGStateWarnThold based on Unsigned32"""
    defaultValue = 0


_EtsysPimExtTibMgrSGStateWarnThold_Object = MibTableColumn
etsysPimExtTibMgrSGStateWarnThold = _EtsysPimExtTibMgrSGStateWarnThold_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 8, 1, 6),
    _EtsysPimExtTibMgrSGStateWarnThold_Type()
)
etsysPimExtTibMgrSGStateWarnThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPimExtTibMgrSGStateWarnThold.setStatus("current")
_EtsysPimExtTibMgrSGStateStored_Type = Gauge32
_EtsysPimExtTibMgrSGStateStored_Object = MibTableColumn
etsysPimExtTibMgrSGStateStored = _EtsysPimExtTibMgrSGStateStored_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 8, 1, 7),
    _EtsysPimExtTibMgrSGStateStored_Type()
)
etsysPimExtTibMgrSGStateStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtTibMgrSGStateStored.setStatus("current")


class _EtsysPimExtTibMgrStarGIStateLimit_Type(Unsigned32):
    """Custom type etsysPimExtTibMgrStarGIStateLimit based on Unsigned32"""
    defaultValue = 0


_EtsysPimExtTibMgrStarGIStateLimit_Object = MibTableColumn
etsysPimExtTibMgrStarGIStateLimit = _EtsysPimExtTibMgrStarGIStateLimit_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 8, 1, 8),
    _EtsysPimExtTibMgrStarGIStateLimit_Type()
)
etsysPimExtTibMgrStarGIStateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPimExtTibMgrStarGIStateLimit.setStatus("current")


class _EtsysPimExtTibMgrStarGIStateWarnThold_Type(Unsigned32):
    """Custom type etsysPimExtTibMgrStarGIStateWarnThold based on Unsigned32"""
    defaultValue = 0


_EtsysPimExtTibMgrStarGIStateWarnThold_Object = MibTableColumn
etsysPimExtTibMgrStarGIStateWarnThold = _EtsysPimExtTibMgrStarGIStateWarnThold_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 8, 1, 9),
    _EtsysPimExtTibMgrStarGIStateWarnThold_Type()
)
etsysPimExtTibMgrStarGIStateWarnThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPimExtTibMgrStarGIStateWarnThold.setStatus("current")
_EtsysPimExtTibMgrStarGIStateStored_Type = Gauge32
_EtsysPimExtTibMgrStarGIStateStored_Object = MibTableColumn
etsysPimExtTibMgrStarGIStateStored = _EtsysPimExtTibMgrStarGIStateStored_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 8, 1, 10),
    _EtsysPimExtTibMgrStarGIStateStored_Type()
)
etsysPimExtTibMgrStarGIStateStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtTibMgrStarGIStateStored.setStatus("current")


class _EtsysPimExtTibMgrSGIStateLimit_Type(Unsigned32):
    """Custom type etsysPimExtTibMgrSGIStateLimit based on Unsigned32"""
    defaultValue = 0


_EtsysPimExtTibMgrSGIStateLimit_Object = MibTableColumn
etsysPimExtTibMgrSGIStateLimit = _EtsysPimExtTibMgrSGIStateLimit_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 8, 1, 11),
    _EtsysPimExtTibMgrSGIStateLimit_Type()
)
etsysPimExtTibMgrSGIStateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPimExtTibMgrSGIStateLimit.setStatus("current")


class _EtsysPimExtTibMgrSGIStateWarnThold_Type(Unsigned32):
    """Custom type etsysPimExtTibMgrSGIStateWarnThold based on Unsigned32"""
    defaultValue = 0


_EtsysPimExtTibMgrSGIStateWarnThold_Object = MibTableColumn
etsysPimExtTibMgrSGIStateWarnThold = _EtsysPimExtTibMgrSGIStateWarnThold_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 8, 1, 12),
    _EtsysPimExtTibMgrSGIStateWarnThold_Type()
)
etsysPimExtTibMgrSGIStateWarnThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPimExtTibMgrSGIStateWarnThold.setStatus("current")
_EtsysPimExtTibMgrSGIStateStored_Type = Gauge32
_EtsysPimExtTibMgrSGIStateStored_Object = MibTableColumn
etsysPimExtTibMgrSGIStateStored = _EtsysPimExtTibMgrSGIStateStored_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 8, 1, 13),
    _EtsysPimExtTibMgrSGIStateStored_Type()
)
etsysPimExtTibMgrSGIStateStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPimExtTibMgrSGIStateStored.setStatus("current")


class _EtsysPimExtTibMgrRegSuppressionTime_Type(Unsigned32):
    """Custom type etsysPimExtTibMgrRegSuppressionTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EtsysPimExtTibMgrRegSuppressionTime_Type.__name__ = "Unsigned32"
_EtsysPimExtTibMgrRegSuppressionTime_Object = MibTableColumn
etsysPimExtTibMgrRegSuppressionTime = _EtsysPimExtTibMgrRegSuppressionTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 8, 1, 14),
    _EtsysPimExtTibMgrRegSuppressionTime_Type()
)
etsysPimExtTibMgrRegSuppressionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPimExtTibMgrRegSuppressionTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysPimExtTibMgrRegSuppressionTime.setUnits("seconds")


class _EtsysPimExtTibMgrRegProbeTime_Type(Unsigned32):
    """Custom type etsysPimExtTibMgrRegProbeTime based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EtsysPimExtTibMgrRegProbeTime_Type.__name__ = "Unsigned32"
_EtsysPimExtTibMgrRegProbeTime_Object = MibTableColumn
etsysPimExtTibMgrRegProbeTime = _EtsysPimExtTibMgrRegProbeTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 8, 1, 15),
    _EtsysPimExtTibMgrRegProbeTime_Type()
)
etsysPimExtTibMgrRegProbeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPimExtTibMgrRegProbeTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysPimExtTibMgrRegProbeTime.setUnits("seconds")


class _EtsysPimExtTibMgrKeepalivePeriod_Type(Unsigned32):
    """Custom type etsysPimExtTibMgrKeepalivePeriod based on Unsigned32"""
    defaultValue = 210

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EtsysPimExtTibMgrKeepalivePeriod_Type.__name__ = "Unsigned32"
_EtsysPimExtTibMgrKeepalivePeriod_Object = MibTableColumn
etsysPimExtTibMgrKeepalivePeriod = _EtsysPimExtTibMgrKeepalivePeriod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 1, 2, 8, 1, 16),
    _EtsysPimExtTibMgrKeepalivePeriod_Type()
)
etsysPimExtTibMgrKeepalivePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPimExtTibMgrKeepalivePeriod.setStatus("current")
if mibBuilder.loadTexts:
    etsysPimExtTibMgrKeepalivePeriod.setUnits("seconds")
_EtsysPimExtConformance_ObjectIdentity = ObjectIdentity
etsysPimExtConformance = _EtsysPimExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 3)
)
_EtsysPimExtGroups_ObjectIdentity = ObjectIdentity
etsysPimExtGroups = _EtsysPimExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 3, 1)
)
_EtsysPimExtCompliances_ObjectIdentity = ObjectIdentity
etsysPimExtCompliances = _EtsysPimExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 3, 2)
)
pimInterfaceEntry.registerAugmentions(
    ("ENTERASYS-PIM-EXT-MIB",
     "etsysPimExtIfEntry")
)
etsysPimExtIfEntry.setIndexNames(*pimInterfaceEntry.getIndexNames())
pimStaticRPEntry.registerAugmentions(
    ("ENTERASYS-PIM-EXT-MIB",
     "etsysPimExtStaticRPEntry")
)
etsysPimExtStaticRPEntry.setIndexNames(*pimStaticRPEntry.getIndexNames())
pimAnycastRPSetEntry.registerAugmentions(
    ("ENTERASYS-PIM-EXT-MIB",
     "etsysPimExtAnycastRPSetEntry")
)
etsysPimExtAnycastRPSetEntry.setIndexNames(*pimAnycastRPSetEntry.getIndexNames())
pimGroupMappingEntry.registerAugmentions(
    ("ENTERASYS-PIM-EXT-MIB",
     "etsysPimExtGroupMappingEntry")
)
etsysPimExtGroupMappingEntry.setIndexNames(*pimGroupMappingEntry.getIndexNames())
pimNeighborEntry.registerAugmentions(
    ("ENTERASYS-PIM-EXT-MIB",
     "etsysPimExtNbrStatsEntry")
)
etsysPimExtNbrStatsEntry.setIndexNames(*pimNeighborEntry.getIndexNames())
pimInterfaceEntry.registerAugmentions(
    ("ENTERASYS-PIM-EXT-MIB",
     "etsysPimExtIfStatsEntry")
)
etsysPimExtIfStatsEntry.setIndexNames(*pimInterfaceEntry.getIndexNames())

# Managed Objects groups

etsysPimExtIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 3, 1, 1)
)
etsysPimExtIfGroup.setObjects(
      *(("ENTERASYS-PIM-EXT-MIB", "etsysPimExtIfAdminStatus"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtIfOperStatus"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtIfP2PNoHellos"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtIfNeighborCount"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtIfStarGStateLimit"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtIfStarGStateWarnThold"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtIfStarGStateStored"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtIfSGStateLimit"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtIfSGStateWarnThold"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtIfSGStateStored"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtIfAssertInterval"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtIfAssertHoldtime"))
)
if mibBuilder.loadTexts:
    etsysPimExtIfGroup.setStatus("current")

etsysPimExtStaticRPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 3, 1, 2)
)
etsysPimExtStaticRPGroup.setObjects(
    ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtStaticRPAdminStatus")
)
if mibBuilder.loadTexts:
    etsysPimExtStaticRPGroup.setStatus("current")

etsysPimExtAnycastRPSetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 3, 1, 3)
)
etsysPimExtAnycastRPSetGroup.setObjects(
    ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtAnycastRPSetAdminStatus")
)
if mibBuilder.loadTexts:
    etsysPimExtAnycastRPSetGroup.setStatus("current")

etsysPimExtGroupMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 3, 1, 4)
)
etsysPimExtGroupMappingGroup.setObjects(
    ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtGroupMappingIsInactive")
)
if mibBuilder.loadTexts:
    etsysPimExtGroupMappingGroup.setStatus("current")

etsysPimExtNbrStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 3, 1, 5)
)
etsysPimExtNbrStatsGroup.setObjects(
      *(("ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrStatsNumRecvHello"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrStatsNumRecvJoinPrune"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrStatsNumRecvAssert"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrStatsNumRecvBSM"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrStatsNumErrJoinPrune"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrStatsNumErrAssert"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrStatsNumErrBSM"))
)
if mibBuilder.loadTexts:
    etsysPimExtNbrStatsGroup.setStatus("current")

etsysPimExtIfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 3, 1, 6)
)
etsysPimExtIfStatsGroup.setObjects(
      *(("ENTERASYS-PIM-EXT-MIB", "etsysPimExtIfStatsNumSentHello"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtIfStatsNumSentJoinPrune"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtIfStatsNumSentAssert"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtIfStatsNumSentBsm"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtIfStatsNumErrHello"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtIfStatsNumRecvUnknownNbr"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtIfStatsNumUnknownHelloOpt"))
)
if mibBuilder.loadTexts:
    etsysPimExtIfStatsGroup.setStatus("current")

etsysPimExtNbrMgrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 3, 1, 7)
)
etsysPimExtNbrMgrGroup.setObjects(
      *(("ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrMgrIndex"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrMgrEnableUnicastMessages"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrMgrAcceptUnicastBsms"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrMgrNumSentCRPAdvert"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrMgrNumSentRegister"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrMgrNumSentRegisterStop"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrMgrNumRecvCRPAdvert"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrMgrNumRecvRegister"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrMgrNumRecvRegisterStop"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrMgrNumErrCRPAdvert"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrMgrNumErrRegister"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrMgrNumErrRegisterStop"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrMgrNumRecvIgnoredType"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrMgrNumRecvUnknownType"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrMgrNumRecvUnknownVer"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrMgrNumRecvBadChecksum"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtNbrMgrNumRecvBadLength"))
)
if mibBuilder.loadTexts:
    etsysPimExtNbrMgrGroup.setStatus("current")

etsysPimExtTibMgrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 3, 1, 8)
)
etsysPimExtTibMgrGroup.setObjects(
      *(("ENTERASYS-PIM-EXT-MIB", "etsysPimExtTibMgrIndex"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtTibMgrGStateLimit"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtTibMgrGStateWarnThold"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtTibMgrGStateStored"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtTibMgrSGStateLimit"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtTibMgrSGStateWarnThold"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtTibMgrSGStateStored"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtTibMgrStarGIStateLimit"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtTibMgrStarGIStateWarnThold"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtTibMgrStarGIStateStored"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtTibMgrSGIStateLimit"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtTibMgrSGIStateWarnThold"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtTibMgrSGIStateStored"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtTibMgrRegSuppressionTime"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtTibMgrRegProbeTime"),
        ("ENTERASYS-PIM-EXT-MIB", "etsysPimExtTibMgrKeepalivePeriod"))
)
if mibBuilder.loadTexts:
    etsysPimExtTibMgrGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysPimExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 67, 3, 2, 1)
)
if mibBuilder.loadTexts:
    etsysPimExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-PIM-EXT-MIB",
    **{"etsysPimExtMIB": etsysPimExtMIB,
       "etsysPimExtObjects": etsysPimExtObjects,
       "etsysPimExtGlobals": etsysPimExtGlobals,
       "etsysPimExtTables": etsysPimExtTables,
       "etsysPimExtIfTable": etsysPimExtIfTable,
       "etsysPimExtIfEntry": etsysPimExtIfEntry,
       "etsysPimExtIfAdminStatus": etsysPimExtIfAdminStatus,
       "etsysPimExtIfOperStatus": etsysPimExtIfOperStatus,
       "etsysPimExtIfP2PNoHellos": etsysPimExtIfP2PNoHellos,
       "etsysPimExtIfNeighborCount": etsysPimExtIfNeighborCount,
       "etsysPimExtIfStarGStateLimit": etsysPimExtIfStarGStateLimit,
       "etsysPimExtIfStarGStateWarnThold": etsysPimExtIfStarGStateWarnThold,
       "etsysPimExtIfStarGStateStored": etsysPimExtIfStarGStateStored,
       "etsysPimExtIfSGStateLimit": etsysPimExtIfSGStateLimit,
       "etsysPimExtIfSGStateWarnThold": etsysPimExtIfSGStateWarnThold,
       "etsysPimExtIfSGStateStored": etsysPimExtIfSGStateStored,
       "etsysPimExtIfAssertInterval": etsysPimExtIfAssertInterval,
       "etsysPimExtIfAssertHoldtime": etsysPimExtIfAssertHoldtime,
       "etsysPimExtStaticRPTable": etsysPimExtStaticRPTable,
       "etsysPimExtStaticRPEntry": etsysPimExtStaticRPEntry,
       "etsysPimExtStaticRPAdminStatus": etsysPimExtStaticRPAdminStatus,
       "etsysPimExtAnycastRPSetTable": etsysPimExtAnycastRPSetTable,
       "etsysPimExtAnycastRPSetEntry": etsysPimExtAnycastRPSetEntry,
       "etsysPimExtAnycastRPSetAdminStatus": etsysPimExtAnycastRPSetAdminStatus,
       "etsysPimExtGroupMappingTable": etsysPimExtGroupMappingTable,
       "etsysPimExtGroupMappingEntry": etsysPimExtGroupMappingEntry,
       "etsysPimExtGroupMappingIsInactive": etsysPimExtGroupMappingIsInactive,
       "etsysPimExtNbrStatsTable": etsysPimExtNbrStatsTable,
       "etsysPimExtNbrStatsEntry": etsysPimExtNbrStatsEntry,
       "etsysPimExtNbrStatsNumRecvHello": etsysPimExtNbrStatsNumRecvHello,
       "etsysPimExtNbrStatsNumRecvJoinPrune": etsysPimExtNbrStatsNumRecvJoinPrune,
       "etsysPimExtNbrStatsNumRecvAssert": etsysPimExtNbrStatsNumRecvAssert,
       "etsysPimExtNbrStatsNumRecvBSM": etsysPimExtNbrStatsNumRecvBSM,
       "etsysPimExtNbrStatsNumErrJoinPrune": etsysPimExtNbrStatsNumErrJoinPrune,
       "etsysPimExtNbrStatsNumErrAssert": etsysPimExtNbrStatsNumErrAssert,
       "etsysPimExtNbrStatsNumErrBSM": etsysPimExtNbrStatsNumErrBSM,
       "etsysPimExtIfStatsTable": etsysPimExtIfStatsTable,
       "etsysPimExtIfStatsEntry": etsysPimExtIfStatsEntry,
       "etsysPimExtIfStatsNumSentHello": etsysPimExtIfStatsNumSentHello,
       "etsysPimExtIfStatsNumSentJoinPrune": etsysPimExtIfStatsNumSentJoinPrune,
       "etsysPimExtIfStatsNumSentAssert": etsysPimExtIfStatsNumSentAssert,
       "etsysPimExtIfStatsNumSentBsm": etsysPimExtIfStatsNumSentBsm,
       "etsysPimExtIfStatsNumErrHello": etsysPimExtIfStatsNumErrHello,
       "etsysPimExtIfStatsNumRecvUnknownNbr": etsysPimExtIfStatsNumRecvUnknownNbr,
       "etsysPimExtIfStatsNumUnknownHelloOpt": etsysPimExtIfStatsNumUnknownHelloOpt,
       "etsysPimExtNbrMgrTable": etsysPimExtNbrMgrTable,
       "etsysPimExtNbrMgrEntry": etsysPimExtNbrMgrEntry,
       "etsysPimExtNbrMgrIndex": etsysPimExtNbrMgrIndex,
       "etsysPimExtNbrMgrEnableUnicastMessages": etsysPimExtNbrMgrEnableUnicastMessages,
       "etsysPimExtNbrMgrAcceptUnicastBsms": etsysPimExtNbrMgrAcceptUnicastBsms,
       "etsysPimExtNbrMgrNumSentCRPAdvert": etsysPimExtNbrMgrNumSentCRPAdvert,
       "etsysPimExtNbrMgrNumSentRegister": etsysPimExtNbrMgrNumSentRegister,
       "etsysPimExtNbrMgrNumSentRegisterStop": etsysPimExtNbrMgrNumSentRegisterStop,
       "etsysPimExtNbrMgrNumRecvCRPAdvert": etsysPimExtNbrMgrNumRecvCRPAdvert,
       "etsysPimExtNbrMgrNumRecvRegister": etsysPimExtNbrMgrNumRecvRegister,
       "etsysPimExtNbrMgrNumRecvRegisterStop": etsysPimExtNbrMgrNumRecvRegisterStop,
       "etsysPimExtNbrMgrNumErrCRPAdvert": etsysPimExtNbrMgrNumErrCRPAdvert,
       "etsysPimExtNbrMgrNumErrRegister": etsysPimExtNbrMgrNumErrRegister,
       "etsysPimExtNbrMgrNumErrRegisterStop": etsysPimExtNbrMgrNumErrRegisterStop,
       "etsysPimExtNbrMgrNumRecvIgnoredType": etsysPimExtNbrMgrNumRecvIgnoredType,
       "etsysPimExtNbrMgrNumRecvUnknownType": etsysPimExtNbrMgrNumRecvUnknownType,
       "etsysPimExtNbrMgrNumRecvUnknownVer": etsysPimExtNbrMgrNumRecvUnknownVer,
       "etsysPimExtNbrMgrNumRecvBadChecksum": etsysPimExtNbrMgrNumRecvBadChecksum,
       "etsysPimExtNbrMgrNumRecvBadLength": etsysPimExtNbrMgrNumRecvBadLength,
       "etsysPimExtTibMgrTable": etsysPimExtTibMgrTable,
       "etsysPimExtTibMgrEntry": etsysPimExtTibMgrEntry,
       "etsysPimExtTibMgrIndex": etsysPimExtTibMgrIndex,
       "etsysPimExtTibMgrGStateLimit": etsysPimExtTibMgrGStateLimit,
       "etsysPimExtTibMgrGStateWarnThold": etsysPimExtTibMgrGStateWarnThold,
       "etsysPimExtTibMgrGStateStored": etsysPimExtTibMgrGStateStored,
       "etsysPimExtTibMgrSGStateLimit": etsysPimExtTibMgrSGStateLimit,
       "etsysPimExtTibMgrSGStateWarnThold": etsysPimExtTibMgrSGStateWarnThold,
       "etsysPimExtTibMgrSGStateStored": etsysPimExtTibMgrSGStateStored,
       "etsysPimExtTibMgrStarGIStateLimit": etsysPimExtTibMgrStarGIStateLimit,
       "etsysPimExtTibMgrStarGIStateWarnThold": etsysPimExtTibMgrStarGIStateWarnThold,
       "etsysPimExtTibMgrStarGIStateStored": etsysPimExtTibMgrStarGIStateStored,
       "etsysPimExtTibMgrSGIStateLimit": etsysPimExtTibMgrSGIStateLimit,
       "etsysPimExtTibMgrSGIStateWarnThold": etsysPimExtTibMgrSGIStateWarnThold,
       "etsysPimExtTibMgrSGIStateStored": etsysPimExtTibMgrSGIStateStored,
       "etsysPimExtTibMgrRegSuppressionTime": etsysPimExtTibMgrRegSuppressionTime,
       "etsysPimExtTibMgrRegProbeTime": etsysPimExtTibMgrRegProbeTime,
       "etsysPimExtTibMgrKeepalivePeriod": etsysPimExtTibMgrKeepalivePeriod,
       "etsysPimExtConformance": etsysPimExtConformance,
       "etsysPimExtGroups": etsysPimExtGroups,
       "etsysPimExtIfGroup": etsysPimExtIfGroup,
       "etsysPimExtStaticRPGroup": etsysPimExtStaticRPGroup,
       "etsysPimExtAnycastRPSetGroup": etsysPimExtAnycastRPSetGroup,
       "etsysPimExtGroupMappingGroup": etsysPimExtGroupMappingGroup,
       "etsysPimExtNbrStatsGroup": etsysPimExtNbrStatsGroup,
       "etsysPimExtIfStatsGroup": etsysPimExtIfStatsGroup,
       "etsysPimExtNbrMgrGroup": etsysPimExtNbrMgrGroup,
       "etsysPimExtTibMgrGroup": etsysPimExtTibMgrGroup,
       "etsysPimExtCompliances": etsysPimExtCompliances,
       "etsysPimExtCompliance": etsysPimExtCompliance}
)
