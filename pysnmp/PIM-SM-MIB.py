# SNMP MIB module (PIM-SM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PIM-SM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:47 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

swPimSmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 52)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwPimSmCtrl_ObjectIdentity = ObjectIdentity
swPimSmCtrl = _SwPimSmCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 1)
)


class _SwPimSmGlobalState_Type(Integer32):
    """Custom type swPimSmGlobalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("other", 0))
    )


_SwPimSmGlobalState_Type.__name__ = "Integer32"
_SwPimSmGlobalState_Object = MibScalar
swPimSmGlobalState = _SwPimSmGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 1, 1),
    _SwPimSmGlobalState_Type()
)
swPimSmGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPimSmGlobalState.setStatus("current")
_SwPimSmInfo_ObjectIdentity = ObjectIdentity
swPimSmInfo = _SwPimSmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 2)
)


class _SwPimRegisterProbeTime_Type(Integer32):
    """Custom type swPimRegisterProbeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_SwPimRegisterProbeTime_Type.__name__ = "Integer32"
_SwPimRegisterProbeTime_Object = MibScalar
swPimRegisterProbeTime = _SwPimRegisterProbeTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 2, 1),
    _SwPimRegisterProbeTime_Type()
)
swPimRegisterProbeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPimRegisterProbeTime.setStatus("current")


class _SwPimRegisterSuppressionTime_Type(Integer32):
    """Custom type swPimRegisterSuppressionTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 255),
    )


_SwPimRegisterSuppressionTime_Type.__name__ = "Integer32"
_SwPimRegisterSuppressionTime_Object = MibScalar
swPimRegisterSuppressionTime = _SwPimRegisterSuppressionTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 2, 2),
    _SwPimRegisterSuppressionTime_Type()
)
swPimRegisterSuppressionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPimRegisterSuppressionTime.setStatus("current")
_SwPimInfoTable_Object = MibTable
swPimInfoTable = _SwPimInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 2, 3)
)
if mibBuilder.loadTexts:
    swPimInfoTable.setStatus("current")
_SwPimInfoEntry_Object = MibTableRow
swPimInfoEntry = _SwPimInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 2, 3, 1)
)
swPimInfoEntry.setIndexNames(
    (0, "PIM-SM-MIB", "swPimInfoInterface"),
)
if mibBuilder.loadTexts:
    swPimInfoEntry.setStatus("current")
_SwPimInfoInterface_Type = InterfaceIndex
_SwPimInfoInterface_Object = MibTableColumn
swPimInfoInterface = _SwPimInfoInterface_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 2, 3, 1, 1),
    _SwPimInfoInterface_Type()
)
swPimInfoInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPimInfoInterface.setStatus("current")
_SwPimInfoAddress_Type = IpAddress
_SwPimInfoAddress_Object = MibTableColumn
swPimInfoAddress = _SwPimInfoAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 2, 3, 1, 2),
    _SwPimInfoAddress_Type()
)
swPimInfoAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPimInfoAddress.setStatus("current")
_SwPimInfoNetMask_Type = IpAddress
_SwPimInfoNetMask_Object = MibTableColumn
swPimInfoNetMask = _SwPimInfoNetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 2, 3, 1, 3),
    _SwPimInfoNetMask_Type()
)
swPimInfoNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPimInfoNetMask.setStatus("current")
_SwPimInfoDesignatedRouter_Type = IpAddress
_SwPimInfoDesignatedRouter_Object = MibTableColumn
swPimInfoDesignatedRouter = _SwPimInfoDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 2, 3, 1, 4),
    _SwPimInfoDesignatedRouter_Type()
)
swPimInfoDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPimInfoDesignatedRouter.setStatus("current")


class _SwPimInfoHelloInterval_Type(Integer32):
    """Custom type swPimInfoHelloInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18724),
    )


_SwPimInfoHelloInterval_Type.__name__ = "Integer32"
_SwPimInfoHelloInterval_Object = MibTableColumn
swPimInfoHelloInterval = _SwPimInfoHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 2, 3, 1, 5),
    _SwPimInfoHelloInterval_Type()
)
swPimInfoHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPimInfoHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    swPimInfoHelloInterval.setUnits("seconds")


class _SwPimInfoJoinPruneInterval_Type(Integer32):
    """Custom type swPimInfoJoinPruneInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18724),
    )


_SwPimInfoJoinPruneInterval_Type.__name__ = "Integer32"
_SwPimInfoJoinPruneInterval_Object = MibTableColumn
swPimInfoJoinPruneInterval = _SwPimInfoJoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 2, 3, 1, 6),
    _SwPimInfoJoinPruneInterval_Type()
)
swPimInfoJoinPruneInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPimInfoJoinPruneInterval.setStatus("current")
if mibBuilder.loadTexts:
    swPimInfoJoinPruneInterval.setUnits("seconds")


class _SwPimInfoDRPriority_Type(Unsigned32):
    """Custom type swPimInfoDRPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_SwPimInfoDRPriority_Type.__name__ = "Unsigned32"
_SwPimInfoDRPriority_Object = MibTableColumn
swPimInfoDRPriority = _SwPimInfoDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 2, 3, 1, 7),
    _SwPimInfoDRPriority_Type()
)
swPimInfoDRPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPimInfoDRPriority.setStatus("current")


class _SwPimInfoMode_Type(Integer32):
    """Custom type swPimInfoMode based on Integer32"""
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
        *(("dense", 1),
          ("sparse", 2),
          ("sparseDense", 3))
    )


_SwPimInfoMode_Type.__name__ = "Integer32"
_SwPimInfoMode_Object = MibTableColumn
swPimInfoMode = _SwPimInfoMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 2, 3, 1, 8),
    _SwPimInfoMode_Type()
)
swPimInfoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPimInfoMode.setStatus("current")


class _SwPimInfoState_Type(Integer32):
    """Custom type swPimInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwPimInfoState_Type.__name__ = "Integer32"
_SwPimInfoState_Object = MibTableColumn
swPimInfoState = _SwPimInfoState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 2, 3, 1, 9),
    _SwPimInfoState_Type()
)
swPimInfoState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPimInfoState.setStatus("current")
_SwPimSmMgmt_ObjectIdentity = ObjectIdentity
swPimSmMgmt = _SwPimSmMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3)
)
_SwPimCbsrInfoMgmt_ObjectIdentity = ObjectIdentity
swPimCbsrInfoMgmt = _SwPimCbsrInfoMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 1)
)


class _SwpimCbsrBootStrapPeriod_Type(Integer32):
    """Custom type swpimCbsrBootStrapPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwpimCbsrBootStrapPeriod_Type.__name__ = "Integer32"
_SwpimCbsrBootStrapPeriod_Object = MibScalar
swpimCbsrBootStrapPeriod = _SwpimCbsrBootStrapPeriod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 1, 1),
    _SwpimCbsrBootStrapPeriod_Type()
)
swpimCbsrBootStrapPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swpimCbsrBootStrapPeriod.setStatus("current")


class _SwPimCbsrHashMaskLen_Type(Integer32):
    """Custom type swPimCbsrHashMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SwPimCbsrHashMaskLen_Type.__name__ = "Integer32"
_SwPimCbsrHashMaskLen_Object = MibScalar
swPimCbsrHashMaskLen = _SwPimCbsrHashMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 1, 2),
    _SwPimCbsrHashMaskLen_Type()
)
swPimCbsrHashMaskLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPimCbsrHashMaskLen.setStatus("current")
_SwPimCbsrTable_Object = MibTable
swPimCbsrTable = _SwPimCbsrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 1, 3)
)
if mibBuilder.loadTexts:
    swPimCbsrTable.setStatus("current")
_SwPimCbsrEntry_Object = MibTableRow
swPimCbsrEntry = _SwPimCbsrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 1, 3, 1)
)
swPimCbsrEntry.setIndexNames(
    (0, "PIM-SM-MIB", "swPimCbsrInterface"),
)
if mibBuilder.loadTexts:
    swPimCbsrEntry.setStatus("current")
_SwPimCbsrInterface_Type = InterfaceIndex
_SwPimCbsrInterface_Object = MibTableColumn
swPimCbsrInterface = _SwPimCbsrInterface_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 1, 3, 1, 1),
    _SwPimCbsrInterface_Type()
)
swPimCbsrInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPimCbsrInterface.setStatus("current")
_SwPimCbsrIpAddress_Type = IpAddress
_SwPimCbsrIpAddress_Object = MibTableColumn
swPimCbsrIpAddress = _SwPimCbsrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 1, 3, 1, 2),
    _SwPimCbsrIpAddress_Type()
)
swPimCbsrIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPimCbsrIpAddress.setStatus("current")
_SwPimCbsrSubnetMask_Type = IpAddress
_SwPimCbsrSubnetMask_Object = MibTableColumn
swPimCbsrSubnetMask = _SwPimCbsrSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 1, 3, 1, 3),
    _SwPimCbsrSubnetMask_Type()
)
swPimCbsrSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPimCbsrSubnetMask.setStatus("current")


class _SwPimCbsrPriority_Type(Integer32):
    """Custom type swPimCbsrPriority based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_SwPimCbsrPriority_Type.__name__ = "Integer32"
_SwPimCbsrPriority_Object = MibTableColumn
swPimCbsrPriority = _SwPimCbsrPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 1, 3, 1, 4),
    _SwPimCbsrPriority_Type()
)
swPimCbsrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPimCbsrPriority.setStatus("current")
_SwPimCandidateRPMgmt_ObjectIdentity = ObjectIdentity
swPimCandidateRPMgmt = _SwPimCandidateRPMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 2)
)


class _SwPimCandidateRPHoldtime_Type(Integer32):
    """Custom type swPimCandidateRPHoldtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwPimCandidateRPHoldtime_Type.__name__ = "Integer32"
_SwPimCandidateRPHoldtime_Object = MibScalar
swPimCandidateRPHoldtime = _SwPimCandidateRPHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 2, 1),
    _SwPimCandidateRPHoldtime_Type()
)
swPimCandidateRPHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPimCandidateRPHoldtime.setStatus("current")


class _SwPimCandidateRPPriority_Type(Integer32):
    """Custom type swPimCandidateRPPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwPimCandidateRPPriority_Type.__name__ = "Integer32"
_SwPimCandidateRPPriority_Object = MibScalar
swPimCandidateRPPriority = _SwPimCandidateRPPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 2, 2),
    _SwPimCandidateRPPriority_Type()
)
swPimCandidateRPPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPimCandidateRPPriority.setStatus("current")


class _SwPimCandidateRPWildcardPrefixCnt_Type(Integer32):
    """Custom type swPimCandidateRPWildcardPrefixCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SwPimCandidateRPWildcardPrefixCnt_Type.__name__ = "Integer32"
_SwPimCandidateRPWildcardPrefixCnt_Object = MibScalar
swPimCandidateRPWildcardPrefixCnt = _SwPimCandidateRPWildcardPrefixCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 2, 3),
    _SwPimCandidateRPWildcardPrefixCnt_Type()
)
swPimCandidateRPWildcardPrefixCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPimCandidateRPWildcardPrefixCnt.setStatus("current")
_SwPimCandidateRPTable_Object = MibTable
swPimCandidateRPTable = _SwPimCandidateRPTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 2, 4)
)
if mibBuilder.loadTexts:
    swPimCandidateRPTable.setStatus("current")
_SwPimCandidateRPEntry_Object = MibTableRow
swPimCandidateRPEntry = _SwPimCandidateRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 2, 4, 1)
)
swPimCandidateRPEntry.setIndexNames(
    (0, "PIM-SM-MIB", "swPimCandidateRPGroupAddress"),
    (0, "PIM-SM-MIB", "swPimCandidateRPGroupMask"),
)
if mibBuilder.loadTexts:
    swPimCandidateRPEntry.setStatus("current")
_SwPimCandidateRPGroupAddress_Type = IpAddress
_SwPimCandidateRPGroupAddress_Object = MibTableColumn
swPimCandidateRPGroupAddress = _SwPimCandidateRPGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 2, 4, 1, 1),
    _SwPimCandidateRPGroupAddress_Type()
)
swPimCandidateRPGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPimCandidateRPGroupAddress.setStatus("current")
_SwPimCandidateRPGroupMask_Type = IpAddress
_SwPimCandidateRPGroupMask_Object = MibTableColumn
swPimCandidateRPGroupMask = _SwPimCandidateRPGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 2, 4, 1, 2),
    _SwPimCandidateRPGroupMask_Type()
)
swPimCandidateRPGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPimCandidateRPGroupMask.setStatus("current")


class _SwPimCandidateRPInterface_Type(DisplayString):
    """Custom type swPimCandidateRPInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwPimCandidateRPInterface_Type.__name__ = "DisplayString"
_SwPimCandidateRPInterface_Object = MibTableColumn
swPimCandidateRPInterface = _SwPimCandidateRPInterface_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 2, 4, 1, 3),
    _SwPimCandidateRPInterface_Type()
)
swPimCandidateRPInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPimCandidateRPInterface.setStatus("current")
_SwPimCandidateRPRowStatus_Type = RowStatus
_SwPimCandidateRPRowStatus_Object = MibTableColumn
swPimCandidateRPRowStatus = _SwPimCandidateRPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 2, 4, 1, 4),
    _SwPimCandidateRPRowStatus_Type()
)
swPimCandidateRPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPimCandidateRPRowStatus.setStatus("current")
_SwPimNeighborTable_Object = MibTable
swPimNeighborTable = _SwPimNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 3)
)
if mibBuilder.loadTexts:
    swPimNeighborTable.setStatus("current")
_SwPimNeighborEntry_Object = MibTableRow
swPimNeighborEntry = _SwPimNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 3, 1)
)
swPimNeighborEntry.setIndexNames(
    (0, "PIM-SM-MIB", "swPimNeighborAddress"),
)
if mibBuilder.loadTexts:
    swPimNeighborEntry.setStatus("current")
_SwPimNeighborAddress_Type = IpAddress
_SwPimNeighborAddress_Object = MibTableColumn
swPimNeighborAddress = _SwPimNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 3, 1, 1),
    _SwPimNeighborAddress_Type()
)
swPimNeighborAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPimNeighborAddress.setStatus("current")
_SwPimNeighborIfIndex_Type = InterfaceIndex
_SwPimNeighborIfIndex_Object = MibTableColumn
swPimNeighborIfIndex = _SwPimNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 3, 1, 2),
    _SwPimNeighborIfIndex_Type()
)
swPimNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPimNeighborIfIndex.setStatus("current")
_SwPimNeighborExpiryTime_Type = TimeTicks
_SwPimNeighborExpiryTime_Object = MibTableColumn
swPimNeighborExpiryTime = _SwPimNeighborExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 3, 1, 3),
    _SwPimNeighborExpiryTime_Type()
)
swPimNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPimNeighborExpiryTime.setStatus("current")
_SwPimSptMgmt_ObjectIdentity = ObjectIdentity
swPimSptMgmt = _SwPimSptMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 4)
)


class _SwPimLastHopSptSwitchover_Type(Integer32):
    """Custom type swPimLastHopSptSwitchover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("immediately", 2),
          ("never", 1))
    )


_SwPimLastHopSptSwitchover_Type.__name__ = "Integer32"
_SwPimLastHopSptSwitchover_Object = MibScalar
swPimLastHopSptSwitchover = _SwPimLastHopSptSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 4, 3),
    _SwPimLastHopSptSwitchover_Type()
)
swPimLastHopSptSwitchover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPimLastHopSptSwitchover.setStatus("current")
_SwPimRegChksumIncDataTable_Object = MibTable
swPimRegChksumIncDataTable = _SwPimRegChksumIncDataTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 5)
)
if mibBuilder.loadTexts:
    swPimRegChksumIncDataTable.setStatus("current")
_SwPimRegChksumIncDataEntry_Object = MibTableRow
swPimRegChksumIncDataEntry = _SwPimRegChksumIncDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 5, 1)
)
swPimRegChksumIncDataEntry.setIndexNames(
    (0, "PIM-SM-MIB", "swL3SwPimRegChksumIncDataRpAddr"),
)
if mibBuilder.loadTexts:
    swPimRegChksumIncDataEntry.setStatus("current")
_SwL3SwPimRegChksumIncDataRpAddr_Type = IpAddress
_SwL3SwPimRegChksumIncDataRpAddr_Object = MibTableColumn
swL3SwPimRegChksumIncDataRpAddr = _SwL3SwPimRegChksumIncDataRpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 5, 1, 1),
    _SwL3SwPimRegChksumIncDataRpAddr_Type()
)
swL3SwPimRegChksumIncDataRpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swL3SwPimRegChksumIncDataRpAddr.setStatus("current")
_SwL3SwPimRegChksumIncDataState_Type = RowStatus
_SwL3SwPimRegChksumIncDataState_Object = MibTableColumn
swL3SwPimRegChksumIncDataState = _SwL3SwPimRegChksumIncDataState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 5, 1, 2),
    _SwL3SwPimRegChksumIncDataState_Type()
)
swL3SwPimRegChksumIncDataState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3SwPimRegChksumIncDataState.setStatus("current")
_SwPimStaticRPTable_Object = MibTable
swPimStaticRPTable = _SwPimStaticRPTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 6)
)
if mibBuilder.loadTexts:
    swPimStaticRPTable.setStatus("current")
_SwPimStaticRPEntry_Object = MibTableRow
swPimStaticRPEntry = _SwPimStaticRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 6, 1)
)
swPimStaticRPEntry.setIndexNames(
    (0, "PIM-SM-MIB", "swPimStaticRPGroupAddress"),
    (0, "PIM-SM-MIB", "swPimStaticRPGroupMask"),
    (0, "PIM-SM-MIB", "swPimStaticRPAddress"),
)
if mibBuilder.loadTexts:
    swPimStaticRPEntry.setStatus("current")
_SwPimStaticRPGroupAddress_Type = IpAddress
_SwPimStaticRPGroupAddress_Object = MibTableColumn
swPimStaticRPGroupAddress = _SwPimStaticRPGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 6, 1, 1),
    _SwPimStaticRPGroupAddress_Type()
)
swPimStaticRPGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPimStaticRPGroupAddress.setStatus("current")
_SwPimStaticRPGroupMask_Type = IpAddress
_SwPimStaticRPGroupMask_Object = MibTableColumn
swPimStaticRPGroupMask = _SwPimStaticRPGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 6, 1, 2),
    _SwPimStaticRPGroupMask_Type()
)
swPimStaticRPGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPimStaticRPGroupMask.setStatus("current")
_SwPimStaticRPAddress_Type = IpAddress
_SwPimStaticRPAddress_Object = MibTableColumn
swPimStaticRPAddress = _SwPimStaticRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 6, 1, 3),
    _SwPimStaticRPAddress_Type()
)
swPimStaticRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPimStaticRPAddress.setStatus("current")
_SwPimStaticRPRowStatus_Type = RowStatus
_SwPimStaticRPRowStatus_Object = MibTableColumn
swPimStaticRPRowStatus = _SwPimStaticRPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 6, 1, 4),
    _SwPimStaticRPRowStatus_Type()
)
swPimStaticRPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPimStaticRPRowStatus.setStatus("current")
_SwPimIpMRouteTable_Object = MibTable
swPimIpMRouteTable = _SwPimIpMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 7)
)
if mibBuilder.loadTexts:
    swPimIpMRouteTable.setStatus("current")
_SwPimIpMRouteEntry_Object = MibTableRow
swPimIpMRouteEntry = _SwPimIpMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 7, 1)
)
swPimIpMRouteEntry.setIndexNames(
    (0, "PIM-SM-MIB", "swPimIpMRouteGroup"),
    (0, "PIM-SM-MIB", "swPimIpMRouteSource"),
    (0, "PIM-SM-MIB", "swPimIpMRouteSourceMask"),
)
if mibBuilder.loadTexts:
    swPimIpMRouteEntry.setStatus("current")
_SwPimIpMRouteGroup_Type = IpAddress
_SwPimIpMRouteGroup_Object = MibTableColumn
swPimIpMRouteGroup = _SwPimIpMRouteGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 7, 1, 1),
    _SwPimIpMRouteGroup_Type()
)
swPimIpMRouteGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPimIpMRouteGroup.setStatus("current")
_SwPimIpMRouteSource_Type = IpAddress
_SwPimIpMRouteSource_Object = MibTableColumn
swPimIpMRouteSource = _SwPimIpMRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 7, 1, 2),
    _SwPimIpMRouteSource_Type()
)
swPimIpMRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPimIpMRouteSource.setStatus("current")
_SwPimIpMRouteSourceMask_Type = IpAddress
_SwPimIpMRouteSourceMask_Object = MibTableColumn
swPimIpMRouteSourceMask = _SwPimIpMRouteSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 7, 1, 3),
    _SwPimIpMRouteSourceMask_Type()
)
swPimIpMRouteSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPimIpMRouteSourceMask.setStatus("current")
_SwPimIpMRouteUpstreamAssertTimer_Type = TimeTicks
_SwPimIpMRouteUpstreamAssertTimer_Object = MibTableColumn
swPimIpMRouteUpstreamAssertTimer = _SwPimIpMRouteUpstreamAssertTimer_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 7, 1, 4),
    _SwPimIpMRouteUpstreamAssertTimer_Type()
)
swPimIpMRouteUpstreamAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPimIpMRouteUpstreamAssertTimer.setStatus("current")
_SwPimIpMRouteAssertMetric_Type = Integer32
_SwPimIpMRouteAssertMetric_Object = MibTableColumn
swPimIpMRouteAssertMetric = _SwPimIpMRouteAssertMetric_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 7, 1, 5),
    _SwPimIpMRouteAssertMetric_Type()
)
swPimIpMRouteAssertMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPimIpMRouteAssertMetric.setStatus("current")
_SwPimIpMRouteAssertMetricPref_Type = Integer32
_SwPimIpMRouteAssertMetricPref_Object = MibTableColumn
swPimIpMRouteAssertMetricPref = _SwPimIpMRouteAssertMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 7, 1, 6),
    _SwPimIpMRouteAssertMetricPref_Type()
)
swPimIpMRouteAssertMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPimIpMRouteAssertMetricPref.setStatus("current")
_SwPimIpMRouteAssertRPTBit_Type = TruthValue
_SwPimIpMRouteAssertRPTBit_Object = MibTableColumn
swPimIpMRouteAssertRPTBit = _SwPimIpMRouteAssertRPTBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 7, 1, 7),
    _SwPimIpMRouteAssertRPTBit_Type()
)
swPimIpMRouteAssertRPTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPimIpMRouteAssertRPTBit.setStatus("current")


class _SwPimIpMRouteFlags_Type(Bits):
    """Custom type swPimIpMRouteFlags based on Bits"""
    namedValues = NamedValues(
        *(("rpt", 0),
          ("spt", 1))
    )

_SwPimIpMRouteFlags_Type.__name__ = "Bits"
_SwPimIpMRouteFlags_Object = MibTableColumn
swPimIpMRouteFlags = _SwPimIpMRouteFlags_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 7, 1, 8),
    _SwPimIpMRouteFlags_Type()
)
swPimIpMRouteFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPimIpMRouteFlags.setStatus("current")
_SwPimIpMRouteType_Type = DisplayString
_SwPimIpMRouteType_Object = MibTableColumn
swPimIpMRouteType = _SwPimIpMRouteType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 7, 1, 9),
    _SwPimIpMRouteType_Type()
)
swPimIpMRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPimIpMRouteType.setStatus("current")
_SwPimRPSetMgmt_ObjectIdentity = ObjectIdentity
swPimRPSetMgmt = _SwPimRPSetMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 8)
)
_SwPimRPSetBootstrapRouter_Type = IpAddress
_SwPimRPSetBootstrapRouter_Object = MibScalar
swPimRPSetBootstrapRouter = _SwPimRPSetBootstrapRouter_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 8, 1),
    _SwPimRPSetBootstrapRouter_Type()
)
swPimRPSetBootstrapRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPimRPSetBootstrapRouter.setStatus("current")
_SwPimRPSetTable_Object = MibTable
swPimRPSetTable = _SwPimRPSetTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 8, 2)
)
if mibBuilder.loadTexts:
    swPimRPSetTable.setStatus("current")
_SwPimRPSetEntry_Object = MibTableRow
swPimRPSetEntry = _SwPimRPSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 8, 2, 1)
)
swPimRPSetEntry.setIndexNames(
    (0, "PIM-SM-MIB", "swPimRPSetComponent"),
    (0, "PIM-SM-MIB", "swPimRPSetGroupAddress"),
    (0, "PIM-SM-MIB", "swPimRPSetGroupMask"),
    (0, "PIM-SM-MIB", "swPimRPSetAddress"),
)
if mibBuilder.loadTexts:
    swPimRPSetEntry.setStatus("current")


class _SwPimRPSetComponent_Type(Integer32):
    """Custom type swPimRPSetComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwPimRPSetComponent_Type.__name__ = "Integer32"
_SwPimRPSetComponent_Object = MibTableColumn
swPimRPSetComponent = _SwPimRPSetComponent_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 8, 2, 1, 1),
    _SwPimRPSetComponent_Type()
)
swPimRPSetComponent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPimRPSetComponent.setStatus("current")
_SwPimRPSetGroupAddress_Type = IpAddress
_SwPimRPSetGroupAddress_Object = MibTableColumn
swPimRPSetGroupAddress = _SwPimRPSetGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 8, 2, 1, 2),
    _SwPimRPSetGroupAddress_Type()
)
swPimRPSetGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPimRPSetGroupAddress.setStatus("current")
_SwPimRPSetGroupMask_Type = IpAddress
_SwPimRPSetGroupMask_Object = MibTableColumn
swPimRPSetGroupMask = _SwPimRPSetGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 8, 2, 1, 3),
    _SwPimRPSetGroupMask_Type()
)
swPimRPSetGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPimRPSetGroupMask.setStatus("current")
_SwPimRPSetAddress_Type = IpAddress
_SwPimRPSetAddress_Object = MibTableColumn
swPimRPSetAddress = _SwPimRPSetAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 8, 2, 1, 4),
    _SwPimRPSetAddress_Type()
)
swPimRPSetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPimRPSetAddress.setStatus("current")


class _SwPimRPSetType_Type(Integer32):
    """Custom type swPimRPSetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("static", 2))
    )


_SwPimRPSetType_Type.__name__ = "Integer32"
_SwPimRPSetType_Object = MibTableColumn
swPimRPSetType = _SwPimRPSetType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 52, 3, 8, 2, 1, 5),
    _SwPimRPSetType_Type()
)
swPimRPSetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPimRPSetType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PIM-SM-MIB",
    **{"swPimSmMIB": swPimSmMIB,
       "swPimSmCtrl": swPimSmCtrl,
       "swPimSmGlobalState": swPimSmGlobalState,
       "swPimSmInfo": swPimSmInfo,
       "swPimRegisterProbeTime": swPimRegisterProbeTime,
       "swPimRegisterSuppressionTime": swPimRegisterSuppressionTime,
       "swPimInfoTable": swPimInfoTable,
       "swPimInfoEntry": swPimInfoEntry,
       "swPimInfoInterface": swPimInfoInterface,
       "swPimInfoAddress": swPimInfoAddress,
       "swPimInfoNetMask": swPimInfoNetMask,
       "swPimInfoDesignatedRouter": swPimInfoDesignatedRouter,
       "swPimInfoHelloInterval": swPimInfoHelloInterval,
       "swPimInfoJoinPruneInterval": swPimInfoJoinPruneInterval,
       "swPimInfoDRPriority": swPimInfoDRPriority,
       "swPimInfoMode": swPimInfoMode,
       "swPimInfoState": swPimInfoState,
       "swPimSmMgmt": swPimSmMgmt,
       "swPimCbsrInfoMgmt": swPimCbsrInfoMgmt,
       "swpimCbsrBootStrapPeriod": swpimCbsrBootStrapPeriod,
       "swPimCbsrHashMaskLen": swPimCbsrHashMaskLen,
       "swPimCbsrTable": swPimCbsrTable,
       "swPimCbsrEntry": swPimCbsrEntry,
       "swPimCbsrInterface": swPimCbsrInterface,
       "swPimCbsrIpAddress": swPimCbsrIpAddress,
       "swPimCbsrSubnetMask": swPimCbsrSubnetMask,
       "swPimCbsrPriority": swPimCbsrPriority,
       "swPimCandidateRPMgmt": swPimCandidateRPMgmt,
       "swPimCandidateRPHoldtime": swPimCandidateRPHoldtime,
       "swPimCandidateRPPriority": swPimCandidateRPPriority,
       "swPimCandidateRPWildcardPrefixCnt": swPimCandidateRPWildcardPrefixCnt,
       "swPimCandidateRPTable": swPimCandidateRPTable,
       "swPimCandidateRPEntry": swPimCandidateRPEntry,
       "swPimCandidateRPGroupAddress": swPimCandidateRPGroupAddress,
       "swPimCandidateRPGroupMask": swPimCandidateRPGroupMask,
       "swPimCandidateRPInterface": swPimCandidateRPInterface,
       "swPimCandidateRPRowStatus": swPimCandidateRPRowStatus,
       "swPimNeighborTable": swPimNeighborTable,
       "swPimNeighborEntry": swPimNeighborEntry,
       "swPimNeighborAddress": swPimNeighborAddress,
       "swPimNeighborIfIndex": swPimNeighborIfIndex,
       "swPimNeighborExpiryTime": swPimNeighborExpiryTime,
       "swPimSptMgmt": swPimSptMgmt,
       "swPimLastHopSptSwitchover": swPimLastHopSptSwitchover,
       "swPimRegChksumIncDataTable": swPimRegChksumIncDataTable,
       "swPimRegChksumIncDataEntry": swPimRegChksumIncDataEntry,
       "swL3SwPimRegChksumIncDataRpAddr": swL3SwPimRegChksumIncDataRpAddr,
       "swL3SwPimRegChksumIncDataState": swL3SwPimRegChksumIncDataState,
       "swPimStaticRPTable": swPimStaticRPTable,
       "swPimStaticRPEntry": swPimStaticRPEntry,
       "swPimStaticRPGroupAddress": swPimStaticRPGroupAddress,
       "swPimStaticRPGroupMask": swPimStaticRPGroupMask,
       "swPimStaticRPAddress": swPimStaticRPAddress,
       "swPimStaticRPRowStatus": swPimStaticRPRowStatus,
       "swPimIpMRouteTable": swPimIpMRouteTable,
       "swPimIpMRouteEntry": swPimIpMRouteEntry,
       "swPimIpMRouteGroup": swPimIpMRouteGroup,
       "swPimIpMRouteSource": swPimIpMRouteSource,
       "swPimIpMRouteSourceMask": swPimIpMRouteSourceMask,
       "swPimIpMRouteUpstreamAssertTimer": swPimIpMRouteUpstreamAssertTimer,
       "swPimIpMRouteAssertMetric": swPimIpMRouteAssertMetric,
       "swPimIpMRouteAssertMetricPref": swPimIpMRouteAssertMetricPref,
       "swPimIpMRouteAssertRPTBit": swPimIpMRouteAssertRPTBit,
       "swPimIpMRouteFlags": swPimIpMRouteFlags,
       "swPimIpMRouteType": swPimIpMRouteType,
       "swPimRPSetMgmt": swPimRPSetMgmt,
       "swPimRPSetBootstrapRouter": swPimRPSetBootstrapRouter,
       "swPimRPSetTable": swPimRPSetTable,
       "swPimRPSetEntry": swPimRPSetEntry,
       "swPimRPSetComponent": swPimRPSetComponent,
       "swPimRPSetGroupAddress": swPimRPSetGroupAddress,
       "swPimRPSetGroupMask": swPimRPSetGroupMask,
       "swPimRPSetAddress": swPimRPSetAddress,
       "swPimRPSetType": swPimRPSetType}
)
