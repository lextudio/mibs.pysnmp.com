# SNMP MIB module (RADLAN-PIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-PIM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:42:39 2024
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

(IANAipRouteProtocol,) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipRouteProtocol")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetVersion) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetVersion")

(pimInterfaceEntry,
 pimInterfaceIPVersion,
 pimInterfaceIfIndex,
 pimNeighborAddress,
 pimNeighborAddressType,
 pimNeighborIfIndex) = mibBuilder.importSymbols(
    "PIM-STD-MIB",
    "pimInterfaceEntry",
    "pimInterfaceIPVersion",
    "pimInterfaceIfIndex",
    "pimNeighborAddress",
    "pimNeighborAddressType",
    "pimNeighborIfIndex")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlPim = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 211)
)
rlPim.setRevisions(
        ("2008-09-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AdminStatus(Integer32, TextualConvention):
    status = "current"
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



class OperStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("operStatusActFailed", 5),
          ("operStatusDown", 2),
          ("operStatusGoingDown", 4),
          ("operStatusGoingUp", 3),
          ("operStatusUp", 1))
    )



class Unsigned32NonZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class NumericIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class NumericIndexOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class EntityIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class EntityIndexOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class StdAccessListListIndexOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class StdAccessListRuleIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class ExtAccessListListIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class ExtAccessListListIndexOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class PimStatsCounter(Unsigned32, TextualConvention):
    status = "current"


class NpgOperStatus(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_RlPimInterfaceTable_Object = MibTable
rlPimInterfaceTable = _RlPimInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 1)
)
if mibBuilder.loadTexts:
    rlPimInterfaceTable.setStatus("current")
_RlPimInterfaceEntry_Object = MibTableRow
rlPimInterfaceEntry = _RlPimInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 1, 1)
)
if mibBuilder.loadTexts:
    rlPimInterfaceEntry.setStatus("current")


class _RlPimInterfaceAdminStatus_Type(AdminStatus):
    """Custom type rlPimInterfaceAdminStatus based on AdminStatus"""


_RlPimInterfaceAdminStatus_Object = MibTableColumn
rlPimInterfaceAdminStatus = _RlPimInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 1, 1, 3),
    _RlPimInterfaceAdminStatus_Type()
)
rlPimInterfaceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimInterfaceAdminStatus.setStatus("current")
_RlPimInterfaceOperStatus_Type = NpgOperStatus
_RlPimInterfaceOperStatus_Object = MibTableColumn
rlPimInterfaceOperStatus = _RlPimInterfaceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 1, 1, 4),
    _RlPimInterfaceOperStatus_Type()
)
rlPimInterfaceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimInterfaceOperStatus.setStatus("current")


class _RlPimInterfaceStubInterface_Type(TruthValue):
    """Custom type rlPimInterfaceStubInterface based on TruthValue"""


_RlPimInterfaceStubInterface_Object = MibTableColumn
rlPimInterfaceStubInterface = _RlPimInterfaceStubInterface_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 1, 1, 5),
    _RlPimInterfaceStubInterface_Type()
)
rlPimInterfaceStubInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimInterfaceStubInterface.setStatus("current")


class _RlPimInterfaceP2PNoHellos_Type(TruthValue):
    """Custom type rlPimInterfaceP2PNoHellos based on TruthValue"""


_RlPimInterfaceP2PNoHellos_Object = MibTableColumn
rlPimInterfaceP2PNoHellos = _RlPimInterfaceP2PNoHellos_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 1, 1, 6),
    _RlPimInterfaceP2PNoHellos_Type()
)
rlPimInterfaceP2PNoHellos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimInterfaceP2PNoHellos.setStatus("current")


class _RlPimInterfaceMgmdEntIndex_Type(NumericIndexOrZero):
    """Custom type rlPimInterfaceMgmdEntIndex based on NumericIndexOrZero"""
    defaultValue = 0


_RlPimInterfaceMgmdEntIndex_Object = MibTableColumn
rlPimInterfaceMgmdEntIndex = _RlPimInterfaceMgmdEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 1, 1, 7),
    _RlPimInterfaceMgmdEntIndex_Type()
)
rlPimInterfaceMgmdEntIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimInterfaceMgmdEntIndex.setStatus("current")
_RlPimInterfaceNeighborCount_Type = Gauge32
_RlPimInterfaceNeighborCount_Object = MibTableColumn
rlPimInterfaceNeighborCount = _RlPimInterfaceNeighborCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 1, 1, 8),
    _RlPimInterfaceNeighborCount_Type()
)
rlPimInterfaceNeighborCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimInterfaceNeighborCount.setStatus("current")


class _RlPimInterfaceStarGStateLimit_Type(Unsigned32):
    """Custom type rlPimInterfaceStarGStateLimit based on Unsigned32"""
    defaultValue = 0


_RlPimInterfaceStarGStateLimit_Object = MibTableColumn
rlPimInterfaceStarGStateLimit = _RlPimInterfaceStarGStateLimit_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 1, 1, 9),
    _RlPimInterfaceStarGStateLimit_Type()
)
rlPimInterfaceStarGStateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimInterfaceStarGStateLimit.setStatus("current")


class _RlPimInterfaceStarGStateWarnThold_Type(Unsigned32):
    """Custom type rlPimInterfaceStarGStateWarnThold based on Unsigned32"""
    defaultValue = 0


_RlPimInterfaceStarGStateWarnThold_Object = MibTableColumn
rlPimInterfaceStarGStateWarnThold = _RlPimInterfaceStarGStateWarnThold_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 1, 1, 10),
    _RlPimInterfaceStarGStateWarnThold_Type()
)
rlPimInterfaceStarGStateWarnThold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimInterfaceStarGStateWarnThold.setStatus("current")
_RlPimInterfaceStarGStateStored_Type = Gauge32
_RlPimInterfaceStarGStateStored_Object = MibTableColumn
rlPimInterfaceStarGStateStored = _RlPimInterfaceStarGStateStored_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 1, 1, 11),
    _RlPimInterfaceStarGStateStored_Type()
)
rlPimInterfaceStarGStateStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimInterfaceStarGStateStored.setStatus("current")


class _RlPimInterfaceSGStateLimit_Type(Unsigned32):
    """Custom type rlPimInterfaceSGStateLimit based on Unsigned32"""
    defaultValue = 0


_RlPimInterfaceSGStateLimit_Object = MibTableColumn
rlPimInterfaceSGStateLimit = _RlPimInterfaceSGStateLimit_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 1, 1, 12),
    _RlPimInterfaceSGStateLimit_Type()
)
rlPimInterfaceSGStateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimInterfaceSGStateLimit.setStatus("current")


class _RlPimInterfaceSGStateWarnThold_Type(Unsigned32):
    """Custom type rlPimInterfaceSGStateWarnThold based on Unsigned32"""
    defaultValue = 0


_RlPimInterfaceSGStateWarnThold_Object = MibTableColumn
rlPimInterfaceSGStateWarnThold = _RlPimInterfaceSGStateWarnThold_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 1, 1, 13),
    _RlPimInterfaceSGStateWarnThold_Type()
)
rlPimInterfaceSGStateWarnThold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimInterfaceSGStateWarnThold.setStatus("current")
_RlPimInterfaceSGStateStored_Type = Gauge32
_RlPimInterfaceSGStateStored_Object = MibTableColumn
rlPimInterfaceSGStateStored = _RlPimInterfaceSGStateStored_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 1, 1, 14),
    _RlPimInterfaceSGStateStored_Type()
)
rlPimInterfaceSGStateStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimInterfaceSGStateStored.setStatus("current")
_RlPimInterfaceNeighborFilter_Type = DisplayString
_RlPimInterfaceNeighborFilter_Object = MibTableColumn
rlPimInterfaceNeighborFilter = _RlPimInterfaceNeighborFilter_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 1, 1, 15),
    _RlPimInterfaceNeighborFilter_Type()
)
rlPimInterfaceNeighborFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimInterfaceNeighborFilter.setStatus("current")


class _RlPimInterfaceAssertInterval_Type(Unsigned32):
    """Custom type rlPimInterfaceAssertInterval based on Unsigned32"""
    defaultValue = 177

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlPimInterfaceAssertInterval_Type.__name__ = "Unsigned32"
_RlPimInterfaceAssertInterval_Object = MibTableColumn
rlPimInterfaceAssertInterval = _RlPimInterfaceAssertInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 1, 1, 16),
    _RlPimInterfaceAssertInterval_Type()
)
rlPimInterfaceAssertInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimInterfaceAssertInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlPimInterfaceAssertInterval.setUnits("seconds")


class _RlPimInterfaceAssertHoldtime_Type(Unsigned32):
    """Custom type rlPimInterfaceAssertHoldtime based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlPimInterfaceAssertHoldtime_Type.__name__ = "Unsigned32"
_RlPimInterfaceAssertHoldtime_Object = MibTableColumn
rlPimInterfaceAssertHoldtime = _RlPimInterfaceAssertHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 1, 1, 17),
    _RlPimInterfaceAssertHoldtime_Type()
)
rlPimInterfaceAssertHoldtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimInterfaceAssertHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    rlPimInterfaceAssertHoldtime.setUnits("seconds")
_RlPimInterfaceAsmGrpFilter_Type = DisplayString
_RlPimInterfaceAsmGrpFilter_Object = MibTableColumn
rlPimInterfaceAsmGrpFilter = _RlPimInterfaceAsmGrpFilter_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 1, 1, 18),
    _RlPimInterfaceAsmGrpFilter_Type()
)
rlPimInterfaceAsmGrpFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimInterfaceAsmGrpFilter.setStatus("current")
_RlPimInterfaceSsmSrcAndGrpFilter_Type = DisplayString
_RlPimInterfaceSsmSrcAndGrpFilter_Object = MibTableColumn
rlPimInterfaceSsmSrcAndGrpFilter = _RlPimInterfaceSsmSrcAndGrpFilter_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 1, 1, 19),
    _RlPimInterfaceSsmSrcAndGrpFilter_Type()
)
rlPimInterfaceSsmSrcAndGrpFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimInterfaceSsmSrcAndGrpFilter.setStatus("current")
_RlPimIfStatsTable_Object = MibTable
rlPimIfStatsTable = _RlPimIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 2)
)
if mibBuilder.loadTexts:
    rlPimIfStatsTable.setStatus("current")
_RlPimIfStatsEntry_Object = MibTableRow
rlPimIfStatsEntry = _RlPimIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 2, 1)
)
rlPimIfStatsEntry.setIndexNames(
    (0, "PIM-STD-MIB", "pimInterfaceIfIndex"),
    (0, "PIM-STD-MIB", "pimInterfaceIPVersion"),
)
if mibBuilder.loadTexts:
    rlPimIfStatsEntry.setStatus("current")
_RlPimIfStatsNumSentHello_Type = PimStatsCounter
_RlPimIfStatsNumSentHello_Object = MibTableColumn
rlPimIfStatsNumSentHello = _RlPimIfStatsNumSentHello_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 2, 1, 1),
    _RlPimIfStatsNumSentHello_Type()
)
rlPimIfStatsNumSentHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimIfStatsNumSentHello.setStatus("current")
_RlPimIfStatsNumSentJoinPrune_Type = PimStatsCounter
_RlPimIfStatsNumSentJoinPrune_Object = MibTableColumn
rlPimIfStatsNumSentJoinPrune = _RlPimIfStatsNumSentJoinPrune_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 2, 1, 2),
    _RlPimIfStatsNumSentJoinPrune_Type()
)
rlPimIfStatsNumSentJoinPrune.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimIfStatsNumSentJoinPrune.setStatus("current")
_RlPimIfStatsNumSentAssert_Type = PimStatsCounter
_RlPimIfStatsNumSentAssert_Object = MibTableColumn
rlPimIfStatsNumSentAssert = _RlPimIfStatsNumSentAssert_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 2, 1, 3),
    _RlPimIfStatsNumSentAssert_Type()
)
rlPimIfStatsNumSentAssert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimIfStatsNumSentAssert.setStatus("current")
_RlPimIfStatsNumSentBsm_Type = PimStatsCounter
_RlPimIfStatsNumSentBsm_Object = MibTableColumn
rlPimIfStatsNumSentBsm = _RlPimIfStatsNumSentBsm_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 2, 1, 4),
    _RlPimIfStatsNumSentBsm_Type()
)
rlPimIfStatsNumSentBsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimIfStatsNumSentBsm.setStatus("current")
_RlPimIfStatsNumErrHello_Type = PimStatsCounter
_RlPimIfStatsNumErrHello_Object = MibTableColumn
rlPimIfStatsNumErrHello = _RlPimIfStatsNumErrHello_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 2, 1, 5),
    _RlPimIfStatsNumErrHello_Type()
)
rlPimIfStatsNumErrHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimIfStatsNumErrHello.setStatus("current")
_RlPimIfStatsNumRecvUnknownNbr_Type = PimStatsCounter
_RlPimIfStatsNumRecvUnknownNbr_Object = MibTableColumn
rlPimIfStatsNumRecvUnknownNbr = _RlPimIfStatsNumRecvUnknownNbr_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 2, 1, 6),
    _RlPimIfStatsNumRecvUnknownNbr_Type()
)
rlPimIfStatsNumRecvUnknownNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimIfStatsNumRecvUnknownNbr.setStatus("current")
_RlPimIfStatsNumUnknownHelloOpt_Type = PimStatsCounter
_RlPimIfStatsNumUnknownHelloOpt_Object = MibTableColumn
rlPimIfStatsNumUnknownHelloOpt = _RlPimIfStatsNumUnknownHelloOpt_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 2, 1, 7),
    _RlPimIfStatsNumUnknownHelloOpt_Type()
)
rlPimIfStatsNumUnknownHelloOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimIfStatsNumUnknownHelloOpt.setStatus("current")
_RlPimIfStatsNumFilteredOut_Type = PimStatsCounter
_RlPimIfStatsNumFilteredOut_Object = MibTableColumn
rlPimIfStatsNumFilteredOut = _RlPimIfStatsNumFilteredOut_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 2, 1, 8),
    _RlPimIfStatsNumFilteredOut_Type()
)
rlPimIfStatsNumFilteredOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimIfStatsNumFilteredOut.setStatus("current")
_RlPimNmEntTable_Object = MibTable
rlPimNmEntTable = _RlPimNmEntTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 3)
)
if mibBuilder.loadTexts:
    rlPimNmEntTable.setStatus("current")
_RlPimNmEntEntry_Object = MibTableRow
rlPimNmEntEntry = _RlPimNmEntEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 3, 1)
)
rlPimNmEntEntry.setIndexNames(
    (0, "RADLAN-PIM-MIB", "rlPimNmEntIndex"),
)
if mibBuilder.loadTexts:
    rlPimNmEntEntry.setStatus("current")
_RlPimNmEntIndex_Type = NumericIndex
_RlPimNmEntIndex_Object = MibTableColumn
rlPimNmEntIndex = _RlPimNmEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 3, 1, 1),
    _RlPimNmEntIndex_Type()
)
rlPimNmEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPimNmEntIndex.setStatus("current")
_RlPimNmEntRowStatus_Type = RowStatus
_RlPimNmEntRowStatus_Object = MibTableColumn
rlPimNmEntRowStatus = _RlPimNmEntRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 3, 1, 2),
    _RlPimNmEntRowStatus_Type()
)
rlPimNmEntRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimNmEntRowStatus.setStatus("current")


class _RlPimNmEntAdminStatus_Type(AdminStatus):
    """Custom type rlPimNmEntAdminStatus based on AdminStatus"""


_RlPimNmEntAdminStatus_Object = MibTableColumn
rlPimNmEntAdminStatus = _RlPimNmEntAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 3, 1, 3),
    _RlPimNmEntAdminStatus_Type()
)
rlPimNmEntAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimNmEntAdminStatus.setStatus("current")
_RlPimNmEntOperStatus_Type = NpgOperStatus
_RlPimNmEntOperStatus_Object = MibTableColumn
rlPimNmEntOperStatus = _RlPimNmEntOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 3, 1, 4),
    _RlPimNmEntOperStatus_Type()
)
rlPimNmEntOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNmEntOperStatus.setStatus("current")
_RlPimNmEntTmEntIndex_Type = NumericIndex
_RlPimNmEntTmEntIndex_Object = MibTableColumn
rlPimNmEntTmEntIndex = _RlPimNmEntTmEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 3, 1, 5),
    _RlPimNmEntTmEntIndex_Type()
)
rlPimNmEntTmEntIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimNmEntTmEntIndex.setStatus("current")
_RlPimNmEntI3JoinOperStatus_Type = NpgOperStatus
_RlPimNmEntI3JoinOperStatus_Object = MibTableColumn
rlPimNmEntI3JoinOperStatus = _RlPimNmEntI3JoinOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 3, 1, 6),
    _RlPimNmEntI3JoinOperStatus_Type()
)
rlPimNmEntI3JoinOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNmEntI3JoinOperStatus.setStatus("current")
_RlPimNmEntNmiJoinOperStatus_Type = NpgOperStatus
_RlPimNmEntNmiJoinOperStatus_Object = MibTableColumn
rlPimNmEntNmiJoinOperStatus = _RlPimNmEntNmiJoinOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 3, 1, 7),
    _RlPimNmEntNmiJoinOperStatus_Type()
)
rlPimNmEntNmiJoinOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNmEntNmiJoinOperStatus.setStatus("current")
_RlPimNmEntSckJoinOperStatus_Type = NpgOperStatus
_RlPimNmEntSckJoinOperStatus_Object = MibTableColumn
rlPimNmEntSckJoinOperStatus = _RlPimNmEntSckJoinOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 3, 1, 8),
    _RlPimNmEntSckJoinOperStatus_Type()
)
rlPimNmEntSckJoinOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNmEntSckJoinOperStatus.setStatus("current")


class _RlPimNmEntClearStatsCounters_Type(TruthValue):
    """Custom type rlPimNmEntClearStatsCounters based on TruthValue"""


_RlPimNmEntClearStatsCounters_Object = MibTableColumn
rlPimNmEntClearStatsCounters = _RlPimNmEntClearStatsCounters_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 3, 1, 9),
    _RlPimNmEntClearStatsCounters_Type()
)
rlPimNmEntClearStatsCounters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimNmEntClearStatsCounters.setStatus("current")
_RlPimNmEntStatsUpTime_Type = TimeTicks
_RlPimNmEntStatsUpTime_Object = MibTableColumn
rlPimNmEntStatsUpTime = _RlPimNmEntStatsUpTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 3, 1, 10),
    _RlPimNmEntStatsUpTime_Type()
)
rlPimNmEntStatsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNmEntStatsUpTime.setStatus("current")


class _RlPimNmEntEnableUnicastMessages_Type(TruthValue):
    """Custom type rlPimNmEntEnableUnicastMessages based on TruthValue"""


_RlPimNmEntEnableUnicastMessages_Object = MibTableColumn
rlPimNmEntEnableUnicastMessages = _RlPimNmEntEnableUnicastMessages_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 3, 1, 11),
    _RlPimNmEntEnableUnicastMessages_Type()
)
rlPimNmEntEnableUnicastMessages.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimNmEntEnableUnicastMessages.setStatus("current")


class _RlPimNmEntAcceptUnicastBsms_Type(TruthValue):
    """Custom type rlPimNmEntAcceptUnicastBsms based on TruthValue"""


_RlPimNmEntAcceptUnicastBsms_Object = MibTableColumn
rlPimNmEntAcceptUnicastBsms = _RlPimNmEntAcceptUnicastBsms_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 3, 1, 12),
    _RlPimNmEntAcceptUnicastBsms_Type()
)
rlPimNmEntAcceptUnicastBsms.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimNmEntAcceptUnicastBsms.setStatus("current")


class _RlPimNmEntCrpAdvFilterIndex_Type(StdAccessListListIndexOrZero):
    """Custom type rlPimNmEntCrpAdvFilterIndex based on StdAccessListListIndexOrZero"""
    defaultValue = 0


_RlPimNmEntCrpAdvFilterIndex_Object = MibTableColumn
rlPimNmEntCrpAdvFilterIndex = _RlPimNmEntCrpAdvFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 3, 1, 13),
    _RlPimNmEntCrpAdvFilterIndex_Type()
)
rlPimNmEntCrpAdvFilterIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimNmEntCrpAdvFilterIndex.setStatus("current")
_RlPimNmEntStatsTable_Object = MibTable
rlPimNmEntStatsTable = _RlPimNmEntStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 4)
)
if mibBuilder.loadTexts:
    rlPimNmEntStatsTable.setStatus("current")
_RlPimNmEntStatsEntry_Object = MibTableRow
rlPimNmEntStatsEntry = _RlPimNmEntStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 4, 1)
)
rlPimNmEntStatsEntry.setIndexNames(
    (0, "RADLAN-PIM-MIB", "rlPimNmEntIndex"),
)
if mibBuilder.loadTexts:
    rlPimNmEntStatsEntry.setStatus("current")
_RlPimNmEntStatsNumSentCRPAdvert_Type = PimStatsCounter
_RlPimNmEntStatsNumSentCRPAdvert_Object = MibTableColumn
rlPimNmEntStatsNumSentCRPAdvert = _RlPimNmEntStatsNumSentCRPAdvert_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 4, 1, 1),
    _RlPimNmEntStatsNumSentCRPAdvert_Type()
)
rlPimNmEntStatsNumSentCRPAdvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNmEntStatsNumSentCRPAdvert.setStatus("current")
_RlPimNmEntStatsNumSentRegister_Type = PimStatsCounter
_RlPimNmEntStatsNumSentRegister_Object = MibTableColumn
rlPimNmEntStatsNumSentRegister = _RlPimNmEntStatsNumSentRegister_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 4, 1, 2),
    _RlPimNmEntStatsNumSentRegister_Type()
)
rlPimNmEntStatsNumSentRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNmEntStatsNumSentRegister.setStatus("current")
_RlPimNmEntStatsNumSentRegisterStop_Type = PimStatsCounter
_RlPimNmEntStatsNumSentRegisterStop_Object = MibTableColumn
rlPimNmEntStatsNumSentRegisterStop = _RlPimNmEntStatsNumSentRegisterStop_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 4, 1, 3),
    _RlPimNmEntStatsNumSentRegisterStop_Type()
)
rlPimNmEntStatsNumSentRegisterStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNmEntStatsNumSentRegisterStop.setStatus("current")
_RlPimNmEntStatsNumRecvCRPAdvert_Type = PimStatsCounter
_RlPimNmEntStatsNumRecvCRPAdvert_Object = MibTableColumn
rlPimNmEntStatsNumRecvCRPAdvert = _RlPimNmEntStatsNumRecvCRPAdvert_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 4, 1, 4),
    _RlPimNmEntStatsNumRecvCRPAdvert_Type()
)
rlPimNmEntStatsNumRecvCRPAdvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNmEntStatsNumRecvCRPAdvert.setStatus("current")
_RlPimNmEntStatsNumRecvRegister_Type = PimStatsCounter
_RlPimNmEntStatsNumRecvRegister_Object = MibTableColumn
rlPimNmEntStatsNumRecvRegister = _RlPimNmEntStatsNumRecvRegister_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 4, 1, 5),
    _RlPimNmEntStatsNumRecvRegister_Type()
)
rlPimNmEntStatsNumRecvRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNmEntStatsNumRecvRegister.setStatus("current")
_RlPimNmEntStatsNumRecvRegisterStop_Type = PimStatsCounter
_RlPimNmEntStatsNumRecvRegisterStop_Object = MibTableColumn
rlPimNmEntStatsNumRecvRegisterStop = _RlPimNmEntStatsNumRecvRegisterStop_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 4, 1, 6),
    _RlPimNmEntStatsNumRecvRegisterStop_Type()
)
rlPimNmEntStatsNumRecvRegisterStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNmEntStatsNumRecvRegisterStop.setStatus("current")
_RlPimNmEntStatsNumErrCRPAdvert_Type = PimStatsCounter
_RlPimNmEntStatsNumErrCRPAdvert_Object = MibTableColumn
rlPimNmEntStatsNumErrCRPAdvert = _RlPimNmEntStatsNumErrCRPAdvert_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 4, 1, 7),
    _RlPimNmEntStatsNumErrCRPAdvert_Type()
)
rlPimNmEntStatsNumErrCRPAdvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNmEntStatsNumErrCRPAdvert.setStatus("current")
_RlPimNmEntStatsNumErrRegister_Type = PimStatsCounter
_RlPimNmEntStatsNumErrRegister_Object = MibTableColumn
rlPimNmEntStatsNumErrRegister = _RlPimNmEntStatsNumErrRegister_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 4, 1, 8),
    _RlPimNmEntStatsNumErrRegister_Type()
)
rlPimNmEntStatsNumErrRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNmEntStatsNumErrRegister.setStatus("current")
_RlPimNmEntStatsNumErrRegisterStop_Type = PimStatsCounter
_RlPimNmEntStatsNumErrRegisterStop_Object = MibTableColumn
rlPimNmEntStatsNumErrRegisterStop = _RlPimNmEntStatsNumErrRegisterStop_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 4, 1, 9),
    _RlPimNmEntStatsNumErrRegisterStop_Type()
)
rlPimNmEntStatsNumErrRegisterStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNmEntStatsNumErrRegisterStop.setStatus("current")
_RlPimNmEntStatsNumRecvIgnoredType_Type = PimStatsCounter
_RlPimNmEntStatsNumRecvIgnoredType_Object = MibTableColumn
rlPimNmEntStatsNumRecvIgnoredType = _RlPimNmEntStatsNumRecvIgnoredType_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 4, 1, 10),
    _RlPimNmEntStatsNumRecvIgnoredType_Type()
)
rlPimNmEntStatsNumRecvIgnoredType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNmEntStatsNumRecvIgnoredType.setStatus("current")
_RlPimNmEntStatsNumRecvUnknownType_Type = PimStatsCounter
_RlPimNmEntStatsNumRecvUnknownType_Object = MibTableColumn
rlPimNmEntStatsNumRecvUnknownType = _RlPimNmEntStatsNumRecvUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 4, 1, 11),
    _RlPimNmEntStatsNumRecvUnknownType_Type()
)
rlPimNmEntStatsNumRecvUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNmEntStatsNumRecvUnknownType.setStatus("current")
_RlPimNmEntStatsNumRecvUnknownVer_Type = PimStatsCounter
_RlPimNmEntStatsNumRecvUnknownVer_Object = MibTableColumn
rlPimNmEntStatsNumRecvUnknownVer = _RlPimNmEntStatsNumRecvUnknownVer_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 4, 1, 12),
    _RlPimNmEntStatsNumRecvUnknownVer_Type()
)
rlPimNmEntStatsNumRecvUnknownVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNmEntStatsNumRecvUnknownVer.setStatus("current")
_RlPimNmEntStatsNumRecvBadChecksum_Type = PimStatsCounter
_RlPimNmEntStatsNumRecvBadChecksum_Object = MibTableColumn
rlPimNmEntStatsNumRecvBadChecksum = _RlPimNmEntStatsNumRecvBadChecksum_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 4, 1, 13),
    _RlPimNmEntStatsNumRecvBadChecksum_Type()
)
rlPimNmEntStatsNumRecvBadChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNmEntStatsNumRecvBadChecksum.setStatus("current")
_RlPimNmEntStatsNumRecvBadLength_Type = PimStatsCounter
_RlPimNmEntStatsNumRecvBadLength_Object = MibTableColumn
rlPimNmEntStatsNumRecvBadLength = _RlPimNmEntStatsNumRecvBadLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 4, 1, 14),
    _RlPimNmEntStatsNumRecvBadLength_Type()
)
rlPimNmEntStatsNumRecvBadLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNmEntStatsNumRecvBadLength.setStatus("current")
_RlPimNmEntStatsNumCRPAdvfiltered_Type = PimStatsCounter
_RlPimNmEntStatsNumCRPAdvfiltered_Object = MibTableColumn
rlPimNmEntStatsNumCRPAdvfiltered = _RlPimNmEntStatsNumCRPAdvfiltered_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 4, 1, 15),
    _RlPimNmEntStatsNumCRPAdvfiltered_Type()
)
rlPimNmEntStatsNumCRPAdvfiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNmEntStatsNumCRPAdvfiltered.setStatus("current")
_RlPimNbrStatsTable_Object = MibTable
rlPimNbrStatsTable = _RlPimNbrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 5)
)
if mibBuilder.loadTexts:
    rlPimNbrStatsTable.setStatus("current")
_RlPimNbrStatsEntry_Object = MibTableRow
rlPimNbrStatsEntry = _RlPimNbrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 5, 1)
)
rlPimNbrStatsEntry.setIndexNames(
    (0, "PIM-STD-MIB", "pimNeighborIfIndex"),
    (0, "PIM-STD-MIB", "pimNeighborAddressType"),
    (0, "PIM-STD-MIB", "pimNeighborAddress"),
)
if mibBuilder.loadTexts:
    rlPimNbrStatsEntry.setStatus("current")
_RlPimNbrStatsNumRecvHello_Type = PimStatsCounter
_RlPimNbrStatsNumRecvHello_Object = MibTableColumn
rlPimNbrStatsNumRecvHello = _RlPimNbrStatsNumRecvHello_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 5, 1, 1),
    _RlPimNbrStatsNumRecvHello_Type()
)
rlPimNbrStatsNumRecvHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNbrStatsNumRecvHello.setStatus("current")
_RlPimNbrStatsNumRecvJoinPrune_Type = PimStatsCounter
_RlPimNbrStatsNumRecvJoinPrune_Object = MibTableColumn
rlPimNbrStatsNumRecvJoinPrune = _RlPimNbrStatsNumRecvJoinPrune_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 5, 1, 2),
    _RlPimNbrStatsNumRecvJoinPrune_Type()
)
rlPimNbrStatsNumRecvJoinPrune.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNbrStatsNumRecvJoinPrune.setStatus("current")
_RlPimNbrStatsNumRecvAssert_Type = PimStatsCounter
_RlPimNbrStatsNumRecvAssert_Object = MibTableColumn
rlPimNbrStatsNumRecvAssert = _RlPimNbrStatsNumRecvAssert_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 5, 1, 3),
    _RlPimNbrStatsNumRecvAssert_Type()
)
rlPimNbrStatsNumRecvAssert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNbrStatsNumRecvAssert.setStatus("current")
_RlPimNbrStatsNumRecvBSM_Type = PimStatsCounter
_RlPimNbrStatsNumRecvBSM_Object = MibTableColumn
rlPimNbrStatsNumRecvBSM = _RlPimNbrStatsNumRecvBSM_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 5, 1, 4),
    _RlPimNbrStatsNumRecvBSM_Type()
)
rlPimNbrStatsNumRecvBSM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNbrStatsNumRecvBSM.setStatus("current")
_RlPimNbrStatsNumErrJoinPrune_Type = PimStatsCounter
_RlPimNbrStatsNumErrJoinPrune_Object = MibTableColumn
rlPimNbrStatsNumErrJoinPrune = _RlPimNbrStatsNumErrJoinPrune_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 5, 1, 5),
    _RlPimNbrStatsNumErrJoinPrune_Type()
)
rlPimNbrStatsNumErrJoinPrune.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNbrStatsNumErrJoinPrune.setStatus("current")
_RlPimNbrStatsNumErrAssert_Type = PimStatsCounter
_RlPimNbrStatsNumErrAssert_Object = MibTableColumn
rlPimNbrStatsNumErrAssert = _RlPimNbrStatsNumErrAssert_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 5, 1, 6),
    _RlPimNbrStatsNumErrAssert_Type()
)
rlPimNbrStatsNumErrAssert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNbrStatsNumErrAssert.setStatus("current")
_RlPimNbrStatsNumErrBSM_Type = PimStatsCounter
_RlPimNbrStatsNumErrBSM_Object = MibTableColumn
rlPimNbrStatsNumErrBSM = _RlPimNbrStatsNumErrBSM_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 5, 1, 7),
    _RlPimNbrStatsNumErrBSM_Type()
)
rlPimNbrStatsNumErrBSM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimNbrStatsNumErrBSM.setStatus("current")
_RlPimTmEntTable_Object = MibTable
rlPimTmEntTable = _RlPimTmEntTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6)
)
if mibBuilder.loadTexts:
    rlPimTmEntTable.setStatus("current")
_RlPimTmEntEntry_Object = MibTableRow
rlPimTmEntEntry = _RlPimTmEntEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1)
)
rlPimTmEntEntry.setIndexNames(
    (0, "RADLAN-PIM-MIB", "rlPimTmEntIndex"),
)
if mibBuilder.loadTexts:
    rlPimTmEntEntry.setStatus("current")
_RlPimTmEntIndex_Type = NumericIndex
_RlPimTmEntIndex_Object = MibTableColumn
rlPimTmEntIndex = _RlPimTmEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1, 1),
    _RlPimTmEntIndex_Type()
)
rlPimTmEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPimTmEntIndex.setStatus("current")
_RlPimTmEntRowStatus_Type = RowStatus
_RlPimTmEntRowStatus_Object = MibTableColumn
rlPimTmEntRowStatus = _RlPimTmEntRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1, 2),
    _RlPimTmEntRowStatus_Type()
)
rlPimTmEntRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimTmEntRowStatus.setStatus("current")


class _RlPimTmEntAdminStatus_Type(AdminStatus):
    """Custom type rlPimTmEntAdminStatus based on AdminStatus"""


_RlPimTmEntAdminStatus_Object = MibTableColumn
rlPimTmEntAdminStatus = _RlPimTmEntAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1, 3),
    _RlPimTmEntAdminStatus_Type()
)
rlPimTmEntAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimTmEntAdminStatus.setStatus("current")
_RlPimTmEntOperStatus_Type = NpgOperStatus
_RlPimTmEntOperStatus_Object = MibTableColumn
rlPimTmEntOperStatus = _RlPimTmEntOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1, 4),
    _RlPimTmEntOperStatus_Type()
)
rlPimTmEntOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimTmEntOperStatus.setStatus("current")


class _RlPimTmEntGStateLimit_Type(Unsigned32):
    """Custom type rlPimTmEntGStateLimit based on Unsigned32"""
    defaultValue = 0


_RlPimTmEntGStateLimit_Object = MibTableColumn
rlPimTmEntGStateLimit = _RlPimTmEntGStateLimit_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1, 5),
    _RlPimTmEntGStateLimit_Type()
)
rlPimTmEntGStateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimTmEntGStateLimit.setStatus("current")


class _RlPimTmEntGStateWarnThold_Type(Unsigned32):
    """Custom type rlPimTmEntGStateWarnThold based on Unsigned32"""
    defaultValue = 0


_RlPimTmEntGStateWarnThold_Object = MibTableColumn
rlPimTmEntGStateWarnThold = _RlPimTmEntGStateWarnThold_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1, 6),
    _RlPimTmEntGStateWarnThold_Type()
)
rlPimTmEntGStateWarnThold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimTmEntGStateWarnThold.setStatus("current")
_RlPimTmEntGStateStored_Type = Gauge32
_RlPimTmEntGStateStored_Object = MibTableColumn
rlPimTmEntGStateStored = _RlPimTmEntGStateStored_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1, 7),
    _RlPimTmEntGStateStored_Type()
)
rlPimTmEntGStateStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimTmEntGStateStored.setStatus("current")


class _RlPimTmEntSGStateLimit_Type(Unsigned32):
    """Custom type rlPimTmEntSGStateLimit based on Unsigned32"""
    defaultValue = 0


_RlPimTmEntSGStateLimit_Object = MibTableColumn
rlPimTmEntSGStateLimit = _RlPimTmEntSGStateLimit_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1, 8),
    _RlPimTmEntSGStateLimit_Type()
)
rlPimTmEntSGStateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimTmEntSGStateLimit.setStatus("current")


class _RlPimTmEntSGStateWarnThold_Type(Unsigned32):
    """Custom type rlPimTmEntSGStateWarnThold based on Unsigned32"""
    defaultValue = 0


_RlPimTmEntSGStateWarnThold_Object = MibTableColumn
rlPimTmEntSGStateWarnThold = _RlPimTmEntSGStateWarnThold_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1, 9),
    _RlPimTmEntSGStateWarnThold_Type()
)
rlPimTmEntSGStateWarnThold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimTmEntSGStateWarnThold.setStatus("current")
_RlPimTmEntSGStateStored_Type = Gauge32
_RlPimTmEntSGStateStored_Object = MibTableColumn
rlPimTmEntSGStateStored = _RlPimTmEntSGStateStored_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1, 10),
    _RlPimTmEntSGStateStored_Type()
)
rlPimTmEntSGStateStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimTmEntSGStateStored.setStatus("current")


class _RlPimTmEntStarGIStateLimit_Type(Unsigned32):
    """Custom type rlPimTmEntStarGIStateLimit based on Unsigned32"""
    defaultValue = 0


_RlPimTmEntStarGIStateLimit_Object = MibTableColumn
rlPimTmEntStarGIStateLimit = _RlPimTmEntStarGIStateLimit_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1, 11),
    _RlPimTmEntStarGIStateLimit_Type()
)
rlPimTmEntStarGIStateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimTmEntStarGIStateLimit.setStatus("current")


class _RlPimTmEntStarGIStateWarnThold_Type(Unsigned32):
    """Custom type rlPimTmEntStarGIStateWarnThold based on Unsigned32"""
    defaultValue = 0


_RlPimTmEntStarGIStateWarnThold_Object = MibTableColumn
rlPimTmEntStarGIStateWarnThold = _RlPimTmEntStarGIStateWarnThold_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1, 12),
    _RlPimTmEntStarGIStateWarnThold_Type()
)
rlPimTmEntStarGIStateWarnThold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimTmEntStarGIStateWarnThold.setStatus("current")
_RlPimTmEntStarGIStateStored_Type = Gauge32
_RlPimTmEntStarGIStateStored_Object = MibTableColumn
rlPimTmEntStarGIStateStored = _RlPimTmEntStarGIStateStored_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1, 13),
    _RlPimTmEntStarGIStateStored_Type()
)
rlPimTmEntStarGIStateStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimTmEntStarGIStateStored.setStatus("current")


class _RlPimTmEntSGIStateLimit_Type(Unsigned32):
    """Custom type rlPimTmEntSGIStateLimit based on Unsigned32"""
    defaultValue = 0


_RlPimTmEntSGIStateLimit_Object = MibTableColumn
rlPimTmEntSGIStateLimit = _RlPimTmEntSGIStateLimit_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1, 14),
    _RlPimTmEntSGIStateLimit_Type()
)
rlPimTmEntSGIStateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimTmEntSGIStateLimit.setStatus("current")


class _RlPimTmEntSGIStateWarnThold_Type(Unsigned32):
    """Custom type rlPimTmEntSGIStateWarnThold based on Unsigned32"""
    defaultValue = 0


_RlPimTmEntSGIStateWarnThold_Object = MibTableColumn
rlPimTmEntSGIStateWarnThold = _RlPimTmEntSGIStateWarnThold_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1, 15),
    _RlPimTmEntSGIStateWarnThold_Type()
)
rlPimTmEntSGIStateWarnThold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimTmEntSGIStateWarnThold.setStatus("current")
_RlPimTmEntSGIStateStored_Type = Gauge32
_RlPimTmEntSGIStateStored_Object = MibTableColumn
rlPimTmEntSGIStateStored = _RlPimTmEntSGIStateStored_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1, 16),
    _RlPimTmEntSGIStateStored_Type()
)
rlPimTmEntSGIStateStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimTmEntSGIStateStored.setStatus("current")
_RlPimTmEntAsmGrpFilter_Type = DisplayString
_RlPimTmEntAsmGrpFilter_Object = MibTableColumn
rlPimTmEntAsmGrpFilter = _RlPimTmEntAsmGrpFilter_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1, 17),
    _RlPimTmEntAsmGrpFilter_Type()
)
rlPimTmEntAsmGrpFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimTmEntAsmGrpFilter.setStatus("current")
_RlPimTmEntSsmSrcAndGrpFilter_Type = DisplayString
_RlPimTmEntSsmSrcAndGrpFilter_Object = MibTableColumn
rlPimTmEntSsmSrcAndGrpFilter = _RlPimTmEntSsmSrcAndGrpFilter_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1, 18),
    _RlPimTmEntSsmSrcAndGrpFilter_Type()
)
rlPimTmEntSsmSrcAndGrpFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimTmEntSsmSrcAndGrpFilter.setStatus("current")
_RlPimTmEntRegSrcAndGrpFilter_Type = DisplayString
_RlPimTmEntRegSrcAndGrpFilter_Object = MibTableColumn
rlPimTmEntRegSrcAndGrpFilter = _RlPimTmEntRegSrcAndGrpFilter_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1, 19),
    _RlPimTmEntRegSrcAndGrpFilter_Type()
)
rlPimTmEntRegSrcAndGrpFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimTmEntRegSrcAndGrpFilter.setStatus("current")


class _RlPimTmEntRegSuppressionTime_Type(Unsigned32):
    """Custom type rlPimTmEntRegSuppressionTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlPimTmEntRegSuppressionTime_Type.__name__ = "Unsigned32"
_RlPimTmEntRegSuppressionTime_Object = MibTableColumn
rlPimTmEntRegSuppressionTime = _RlPimTmEntRegSuppressionTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1, 20),
    _RlPimTmEntRegSuppressionTime_Type()
)
rlPimTmEntRegSuppressionTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimTmEntRegSuppressionTime.setStatus("current")
if mibBuilder.loadTexts:
    rlPimTmEntRegSuppressionTime.setUnits("seconds")


class _RlPimTmEntRegProbeTime_Type(Unsigned32):
    """Custom type rlPimTmEntRegProbeTime based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlPimTmEntRegProbeTime_Type.__name__ = "Unsigned32"
_RlPimTmEntRegProbeTime_Object = MibTableColumn
rlPimTmEntRegProbeTime = _RlPimTmEntRegProbeTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1, 21),
    _RlPimTmEntRegProbeTime_Type()
)
rlPimTmEntRegProbeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimTmEntRegProbeTime.setStatus("current")
if mibBuilder.loadTexts:
    rlPimTmEntRegProbeTime.setUnits("seconds")


class _RlPimTmEntKeepalivePeriod_Type(Unsigned32):
    """Custom type rlPimTmEntKeepalivePeriod based on Unsigned32"""
    defaultValue = 210

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlPimTmEntKeepalivePeriod_Type.__name__ = "Unsigned32"
_RlPimTmEntKeepalivePeriod_Object = MibTableColumn
rlPimTmEntKeepalivePeriod = _RlPimTmEntKeepalivePeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1, 22),
    _RlPimTmEntKeepalivePeriod_Type()
)
rlPimTmEntKeepalivePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimTmEntKeepalivePeriod.setStatus("current")
if mibBuilder.loadTexts:
    rlPimTmEntKeepalivePeriod.setUnits("seconds")


class _RlPimTmEntSendIfStateChangeTraps_Type(TruthValue):
    """Custom type rlPimTmEntSendIfStateChangeTraps based on TruthValue"""


_RlPimTmEntSendIfStateChangeTraps_Object = MibTableColumn
rlPimTmEntSendIfStateChangeTraps = _RlPimTmEntSendIfStateChangeTraps_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1, 23),
    _RlPimTmEntSendIfStateChangeTraps_Type()
)
rlPimTmEntSendIfStateChangeTraps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimTmEntSendIfStateChangeTraps.setStatus("current")


class _RlPimTmEntSupportedAddrType_Type(InetAddressType):
    """Custom type rlPimTmEntSupportedAddrType based on InetAddressType"""


_RlPimTmEntSupportedAddrType_Object = MibTableColumn
rlPimTmEntSupportedAddrType = _RlPimTmEntSupportedAddrType_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 6, 1, 24),
    _RlPimTmEntSupportedAddrType_Type()
)
rlPimTmEntSupportedAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimTmEntSupportedAddrType.setStatus("current")


class _RlPimEmbeddedRpEnabled_Type(TruthValue):
    """Custom type rlPimEmbeddedRpEnabled based on TruthValue"""


_RlPimEmbeddedRpEnabled_Object = MibScalar
rlPimEmbeddedRpEnabled = _RlPimEmbeddedRpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 211, 7),
    _RlPimEmbeddedRpEnabled_Type()
)
rlPimEmbeddedRpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPimEmbeddedRpEnabled.setStatus("current")
pimInterfaceEntry.registerAugmentions(
    ("RADLAN-PIM-MIB",
     "rlPimInterfaceEntry")
)
rlPimInterfaceEntry.setIndexNames(*pimInterfaceEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-PIM-MIB",
    **{"AdminStatus": AdminStatus,
       "OperStatus": OperStatus,
       "Unsigned32NonZero": Unsigned32NonZero,
       "NumericIndex": NumericIndex,
       "NumericIndexOrZero": NumericIndexOrZero,
       "EntityIndex": EntityIndex,
       "EntityIndexOrZero": EntityIndexOrZero,
       "StdAccessListListIndexOrZero": StdAccessListListIndexOrZero,
       "StdAccessListRuleIndex": StdAccessListRuleIndex,
       "ExtAccessListListIndex": ExtAccessListListIndex,
       "ExtAccessListListIndexOrZero": ExtAccessListListIndexOrZero,
       "PimStatsCounter": PimStatsCounter,
       "NpgOperStatus": NpgOperStatus,
       "rlPim": rlPim,
       "rlPimInterfaceTable": rlPimInterfaceTable,
       "rlPimInterfaceEntry": rlPimInterfaceEntry,
       "rlPimInterfaceAdminStatus": rlPimInterfaceAdminStatus,
       "rlPimInterfaceOperStatus": rlPimInterfaceOperStatus,
       "rlPimInterfaceStubInterface": rlPimInterfaceStubInterface,
       "rlPimInterfaceP2PNoHellos": rlPimInterfaceP2PNoHellos,
       "rlPimInterfaceMgmdEntIndex": rlPimInterfaceMgmdEntIndex,
       "rlPimInterfaceNeighborCount": rlPimInterfaceNeighborCount,
       "rlPimInterfaceStarGStateLimit": rlPimInterfaceStarGStateLimit,
       "rlPimInterfaceStarGStateWarnThold": rlPimInterfaceStarGStateWarnThold,
       "rlPimInterfaceStarGStateStored": rlPimInterfaceStarGStateStored,
       "rlPimInterfaceSGStateLimit": rlPimInterfaceSGStateLimit,
       "rlPimInterfaceSGStateWarnThold": rlPimInterfaceSGStateWarnThold,
       "rlPimInterfaceSGStateStored": rlPimInterfaceSGStateStored,
       "rlPimInterfaceNeighborFilter": rlPimInterfaceNeighborFilter,
       "rlPimInterfaceAssertInterval": rlPimInterfaceAssertInterval,
       "rlPimInterfaceAssertHoldtime": rlPimInterfaceAssertHoldtime,
       "rlPimInterfaceAsmGrpFilter": rlPimInterfaceAsmGrpFilter,
       "rlPimInterfaceSsmSrcAndGrpFilter": rlPimInterfaceSsmSrcAndGrpFilter,
       "rlPimIfStatsTable": rlPimIfStatsTable,
       "rlPimIfStatsEntry": rlPimIfStatsEntry,
       "rlPimIfStatsNumSentHello": rlPimIfStatsNumSentHello,
       "rlPimIfStatsNumSentJoinPrune": rlPimIfStatsNumSentJoinPrune,
       "rlPimIfStatsNumSentAssert": rlPimIfStatsNumSentAssert,
       "rlPimIfStatsNumSentBsm": rlPimIfStatsNumSentBsm,
       "rlPimIfStatsNumErrHello": rlPimIfStatsNumErrHello,
       "rlPimIfStatsNumRecvUnknownNbr": rlPimIfStatsNumRecvUnknownNbr,
       "rlPimIfStatsNumUnknownHelloOpt": rlPimIfStatsNumUnknownHelloOpt,
       "rlPimIfStatsNumFilteredOut": rlPimIfStatsNumFilteredOut,
       "rlPimNmEntTable": rlPimNmEntTable,
       "rlPimNmEntEntry": rlPimNmEntEntry,
       "rlPimNmEntIndex": rlPimNmEntIndex,
       "rlPimNmEntRowStatus": rlPimNmEntRowStatus,
       "rlPimNmEntAdminStatus": rlPimNmEntAdminStatus,
       "rlPimNmEntOperStatus": rlPimNmEntOperStatus,
       "rlPimNmEntTmEntIndex": rlPimNmEntTmEntIndex,
       "rlPimNmEntI3JoinOperStatus": rlPimNmEntI3JoinOperStatus,
       "rlPimNmEntNmiJoinOperStatus": rlPimNmEntNmiJoinOperStatus,
       "rlPimNmEntSckJoinOperStatus": rlPimNmEntSckJoinOperStatus,
       "rlPimNmEntClearStatsCounters": rlPimNmEntClearStatsCounters,
       "rlPimNmEntStatsUpTime": rlPimNmEntStatsUpTime,
       "rlPimNmEntEnableUnicastMessages": rlPimNmEntEnableUnicastMessages,
       "rlPimNmEntAcceptUnicastBsms": rlPimNmEntAcceptUnicastBsms,
       "rlPimNmEntCrpAdvFilterIndex": rlPimNmEntCrpAdvFilterIndex,
       "rlPimNmEntStatsTable": rlPimNmEntStatsTable,
       "rlPimNmEntStatsEntry": rlPimNmEntStatsEntry,
       "rlPimNmEntStatsNumSentCRPAdvert": rlPimNmEntStatsNumSentCRPAdvert,
       "rlPimNmEntStatsNumSentRegister": rlPimNmEntStatsNumSentRegister,
       "rlPimNmEntStatsNumSentRegisterStop": rlPimNmEntStatsNumSentRegisterStop,
       "rlPimNmEntStatsNumRecvCRPAdvert": rlPimNmEntStatsNumRecvCRPAdvert,
       "rlPimNmEntStatsNumRecvRegister": rlPimNmEntStatsNumRecvRegister,
       "rlPimNmEntStatsNumRecvRegisterStop": rlPimNmEntStatsNumRecvRegisterStop,
       "rlPimNmEntStatsNumErrCRPAdvert": rlPimNmEntStatsNumErrCRPAdvert,
       "rlPimNmEntStatsNumErrRegister": rlPimNmEntStatsNumErrRegister,
       "rlPimNmEntStatsNumErrRegisterStop": rlPimNmEntStatsNumErrRegisterStop,
       "rlPimNmEntStatsNumRecvIgnoredType": rlPimNmEntStatsNumRecvIgnoredType,
       "rlPimNmEntStatsNumRecvUnknownType": rlPimNmEntStatsNumRecvUnknownType,
       "rlPimNmEntStatsNumRecvUnknownVer": rlPimNmEntStatsNumRecvUnknownVer,
       "rlPimNmEntStatsNumRecvBadChecksum": rlPimNmEntStatsNumRecvBadChecksum,
       "rlPimNmEntStatsNumRecvBadLength": rlPimNmEntStatsNumRecvBadLength,
       "rlPimNmEntStatsNumCRPAdvfiltered": rlPimNmEntStatsNumCRPAdvfiltered,
       "rlPimNbrStatsTable": rlPimNbrStatsTable,
       "rlPimNbrStatsEntry": rlPimNbrStatsEntry,
       "rlPimNbrStatsNumRecvHello": rlPimNbrStatsNumRecvHello,
       "rlPimNbrStatsNumRecvJoinPrune": rlPimNbrStatsNumRecvJoinPrune,
       "rlPimNbrStatsNumRecvAssert": rlPimNbrStatsNumRecvAssert,
       "rlPimNbrStatsNumRecvBSM": rlPimNbrStatsNumRecvBSM,
       "rlPimNbrStatsNumErrJoinPrune": rlPimNbrStatsNumErrJoinPrune,
       "rlPimNbrStatsNumErrAssert": rlPimNbrStatsNumErrAssert,
       "rlPimNbrStatsNumErrBSM": rlPimNbrStatsNumErrBSM,
       "rlPimTmEntTable": rlPimTmEntTable,
       "rlPimTmEntEntry": rlPimTmEntEntry,
       "rlPimTmEntIndex": rlPimTmEntIndex,
       "rlPimTmEntRowStatus": rlPimTmEntRowStatus,
       "rlPimTmEntAdminStatus": rlPimTmEntAdminStatus,
       "rlPimTmEntOperStatus": rlPimTmEntOperStatus,
       "rlPimTmEntGStateLimit": rlPimTmEntGStateLimit,
       "rlPimTmEntGStateWarnThold": rlPimTmEntGStateWarnThold,
       "rlPimTmEntGStateStored": rlPimTmEntGStateStored,
       "rlPimTmEntSGStateLimit": rlPimTmEntSGStateLimit,
       "rlPimTmEntSGStateWarnThold": rlPimTmEntSGStateWarnThold,
       "rlPimTmEntSGStateStored": rlPimTmEntSGStateStored,
       "rlPimTmEntStarGIStateLimit": rlPimTmEntStarGIStateLimit,
       "rlPimTmEntStarGIStateWarnThold": rlPimTmEntStarGIStateWarnThold,
       "rlPimTmEntStarGIStateStored": rlPimTmEntStarGIStateStored,
       "rlPimTmEntSGIStateLimit": rlPimTmEntSGIStateLimit,
       "rlPimTmEntSGIStateWarnThold": rlPimTmEntSGIStateWarnThold,
       "rlPimTmEntSGIStateStored": rlPimTmEntSGIStateStored,
       "rlPimTmEntAsmGrpFilter": rlPimTmEntAsmGrpFilter,
       "rlPimTmEntSsmSrcAndGrpFilter": rlPimTmEntSsmSrcAndGrpFilter,
       "rlPimTmEntRegSrcAndGrpFilter": rlPimTmEntRegSrcAndGrpFilter,
       "rlPimTmEntRegSuppressionTime": rlPimTmEntRegSuppressionTime,
       "rlPimTmEntRegProbeTime": rlPimTmEntRegProbeTime,
       "rlPimTmEntKeepalivePeriod": rlPimTmEntKeepalivePeriod,
       "rlPimTmEntSendIfStateChangeTraps": rlPimTmEntSendIfStateChangeTraps,
       "rlPimTmEntSupportedAddrType": rlPimTmEntSupportedAddrType,
       "rlPimEmbeddedRpEnabled": rlPimEmbeddedRpEnabled}
)
