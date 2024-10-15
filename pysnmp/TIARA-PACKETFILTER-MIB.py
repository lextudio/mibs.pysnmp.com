# SNMP MIB module (TIARA-PACKETFILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIARA-PACKETFILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:43 2024
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

(tiaraIpIfIndex,) = mibBuilder.importSymbols(
    "TIARA-IP-MIB",
    "tiaraIpIfIndex")

(tiaraMgmt,) = mibBuilder.importSymbols(
    "TIARA-NETWORKS-SMI",
    "tiaraMgmt")


# MODULE-IDENTITY

tiaraPacketFilterMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FilterRuleClearCounters_Type = DisplayString
_FilterRuleClearCounters_Object = MibScalar
filterRuleClearCounters = _FilterRuleClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 1),
    _FilterRuleClearCounters_Type()
)
filterRuleClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterRuleClearCounters.setStatus("current")
_FilterNameIndexTable_Object = MibTable
filterNameIndexTable = _FilterNameIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 2)
)
if mibBuilder.loadTexts:
    filterNameIndexTable.setStatus("current")
_FilterNameIndexEntry_Object = MibTableRow
filterNameIndexEntry = _FilterNameIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 2, 1)
)
filterNameIndexEntry.setIndexNames(
    (0, "TIARA-PACKETFILTER-MIB", "filterNameIndex"),
)
if mibBuilder.loadTexts:
    filterNameIndexEntry.setStatus("current")
_FilterEntryName_Type = DisplayString
_FilterEntryName_Object = MibTableColumn
filterEntryName = _FilterEntryName_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 2, 1, 1),
    _FilterEntryName_Type()
)
filterEntryName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterEntryName.setStatus("current")
_FilterNameIndex_Type = Integer32
_FilterNameIndex_Object = MibTableColumn
filterNameIndex = _FilterNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 2, 1, 2),
    _FilterNameIndex_Type()
)
filterNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    filterNameIndex.setStatus("current")
_FilterEntryRowStatus_Type = RowStatus
_FilterEntryRowStatus_Object = MibTableColumn
filterEntryRowStatus = _FilterEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 2, 1, 3),
    _FilterEntryRowStatus_Type()
)
filterEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterEntryRowStatus.setStatus("current")
_FilterRuleAssignTable_Object = MibTable
filterRuleAssignTable = _FilterRuleAssignTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 3)
)
if mibBuilder.loadTexts:
    filterRuleAssignTable.setStatus("current")
_FilterRuleAssignTableEntry_Object = MibTableRow
filterRuleAssignTableEntry = _FilterRuleAssignTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 3, 1)
)
filterRuleAssignTableEntry.setIndexNames(
    (0, "TIARA-IP-MIB", "tiaraIpIfIndex"),
)
if mibBuilder.loadTexts:
    filterRuleAssignTableEntry.setStatus("current")
_FilterRuleSetNameIn_Type = DisplayString
_FilterRuleSetNameIn_Object = MibTableColumn
filterRuleSetNameIn = _FilterRuleSetNameIn_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 3, 1, 1),
    _FilterRuleSetNameIn_Type()
)
filterRuleSetNameIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRuleSetNameIn.setStatus("current")
_FilterRuleSetNameOut_Type = DisplayString
_FilterRuleSetNameOut_Object = MibTableColumn
filterRuleSetNameOut = _FilterRuleSetNameOut_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 3, 1, 2),
    _FilterRuleSetNameOut_Type()
)
filterRuleSetNameOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRuleSetNameOut.setStatus("current")
_FilterRuleAssignTableRowStatus_Type = RowStatus
_FilterRuleAssignTableRowStatus_Object = MibTableColumn
filterRuleAssignTableRowStatus = _FilterRuleAssignTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 3, 1, 3),
    _FilterRuleAssignTableRowStatus_Type()
)
filterRuleAssignTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRuleAssignTableRowStatus.setStatus("current")
_FilterRuleSetTable_Object = MibTable
filterRuleSetTable = _FilterRuleSetTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 4)
)
if mibBuilder.loadTexts:
    filterRuleSetTable.setStatus("current")
_FilterRuleSetTableEntry_Object = MibTableRow
filterRuleSetTableEntry = _FilterRuleSetTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1)
)
filterRuleSetTableEntry.setIndexNames(
    (0, "TIARA-PACKETFILTER-MIB", "filterNameIndex"),
    (0, "TIARA-PACKETFILTER-MIB", "filterRuleSetLineNo"),
)
if mibBuilder.loadTexts:
    filterRuleSetTableEntry.setStatus("current")
_FilterRuleSetLineNo_Type = Integer32
_FilterRuleSetLineNo_Object = MibTableColumn
filterRuleSetLineNo = _FilterRuleSetLineNo_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 1),
    _FilterRuleSetLineNo_Type()
)
filterRuleSetLineNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    filterRuleSetLineNo.setStatus("current")
_FilterRuleName_Type = DisplayString
_FilterRuleName_Object = MibTableColumn
filterRuleName = _FilterRuleName_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 2),
    _FilterRuleName_Type()
)
filterRuleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRuleName.setStatus("current")


class _FilterRuleSetAction_Type(Integer32):
    """Custom type filterRuleSetAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1),
          ("reject", 3))
    )


_FilterRuleSetAction_Type.__name__ = "Integer32"
_FilterRuleSetAction_Object = MibTableColumn
filterRuleSetAction = _FilterRuleSetAction_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 3),
    _FilterRuleSetAction_Type()
)
filterRuleSetAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRuleSetAction.setStatus("current")


class _FilterRuleSetProtocolType_Type(Integer32):
    """Custom type filterRuleSetProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("ip", 0),
          ("tcp", 6),
          ("udp", 17))
    )


_FilterRuleSetProtocolType_Type.__name__ = "Integer32"
_FilterRuleSetProtocolType_Object = MibTableColumn
filterRuleSetProtocolType = _FilterRuleSetProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 4),
    _FilterRuleSetProtocolType_Type()
)
filterRuleSetProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRuleSetProtocolType.setStatus("current")
_FilterRuleSetSrcIpAddr_Type = IpAddress
_FilterRuleSetSrcIpAddr_Object = MibTableColumn
filterRuleSetSrcIpAddr = _FilterRuleSetSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 5),
    _FilterRuleSetSrcIpAddr_Type()
)
filterRuleSetSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRuleSetSrcIpAddr.setStatus("current")


class _FilterRuleSetSrcMask_Type(IpAddress):
    """Custom type filterRuleSetSrcMask based on IpAddress"""
    defaultValue = 0


_FilterRuleSetSrcMask_Object = MibTableColumn
filterRuleSetSrcMask = _FilterRuleSetSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 6),
    _FilterRuleSetSrcMask_Type()
)
filterRuleSetSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRuleSetSrcMask.setStatus("current")
_FilterRuleSetDestIpAddr_Type = IpAddress
_FilterRuleSetDestIpAddr_Object = MibTableColumn
filterRuleSetDestIpAddr = _FilterRuleSetDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 7),
    _FilterRuleSetDestIpAddr_Type()
)
filterRuleSetDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRuleSetDestIpAddr.setStatus("current")


class _FilterRuleSetDestMask_Type(IpAddress):
    """Custom type filterRuleSetDestMask based on IpAddress"""
    defaultValue = 0


_FilterRuleSetDestMask_Object = MibTableColumn
filterRuleSetDestMask = _FilterRuleSetDestMask_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 8),
    _FilterRuleSetDestMask_Type()
)
filterRuleSetDestMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRuleSetDestMask.setStatus("current")


class _FilterRuleSetPrecedence_Type(Integer32):
    """Custom type filterRuleSetPrecedence based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FilterRuleSetPrecedence_Type.__name__ = "Integer32"
_FilterRuleSetPrecedence_Object = MibTableColumn
filterRuleSetPrecedence = _FilterRuleSetPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 9),
    _FilterRuleSetPrecedence_Type()
)
filterRuleSetPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRuleSetPrecedence.setStatus("current")


class _FilterRuleSetTos_Type(Integer32):
    """Custom type filterRuleSetTos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FilterRuleSetTos_Type.__name__ = "Integer32"
_FilterRuleSetTos_Object = MibTableColumn
filterRuleSetTos = _FilterRuleSetTos_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 10),
    _FilterRuleSetTos_Type()
)
filterRuleSetTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRuleSetTos.setStatus("current")


class _FilterRuleSetIcmpType_Type(Integer32):
    """Custom type filterRuleSetIcmpType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FilterRuleSetIcmpType_Type.__name__ = "Integer32"
_FilterRuleSetIcmpType_Object = MibTableColumn
filterRuleSetIcmpType = _FilterRuleSetIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 11),
    _FilterRuleSetIcmpType_Type()
)
filterRuleSetIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRuleSetIcmpType.setStatus("current")


class _FilterRuleSetIcmpCode_Type(Integer32):
    """Custom type filterRuleSetIcmpCode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FilterRuleSetIcmpCode_Type.__name__ = "Integer32"
_FilterRuleSetIcmpCode_Object = MibTableColumn
filterRuleSetIcmpCode = _FilterRuleSetIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 12),
    _FilterRuleSetIcmpCode_Type()
)
filterRuleSetIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRuleSetIcmpCode.setStatus("current")


class _FilterRuleSetSrcPortOne_Type(Integer32):
    """Custom type filterRuleSetSrcPortOne based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FilterRuleSetSrcPortOne_Type.__name__ = "Integer32"
_FilterRuleSetSrcPortOne_Object = MibTableColumn
filterRuleSetSrcPortOne = _FilterRuleSetSrcPortOne_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 13),
    _FilterRuleSetSrcPortOne_Type()
)
filterRuleSetSrcPortOne.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRuleSetSrcPortOne.setStatus("current")


class _FilterRuleSetSrcPortTwo_Type(Integer32):
    """Custom type filterRuleSetSrcPortTwo based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FilterRuleSetSrcPortTwo_Type.__name__ = "Integer32"
_FilterRuleSetSrcPortTwo_Object = MibTableColumn
filterRuleSetSrcPortTwo = _FilterRuleSetSrcPortTwo_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 14),
    _FilterRuleSetSrcPortTwo_Type()
)
filterRuleSetSrcPortTwo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRuleSetSrcPortTwo.setStatus("current")


class _FilterRuleSetDestPortOne_Type(Integer32):
    """Custom type filterRuleSetDestPortOne based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FilterRuleSetDestPortOne_Type.__name__ = "Integer32"
_FilterRuleSetDestPortOne_Object = MibTableColumn
filterRuleSetDestPortOne = _FilterRuleSetDestPortOne_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 15),
    _FilterRuleSetDestPortOne_Type()
)
filterRuleSetDestPortOne.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRuleSetDestPortOne.setStatus("current")


class _FilterRuleSetDestPortTwo_Type(Integer32):
    """Custom type filterRuleSetDestPortTwo based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FilterRuleSetDestPortTwo_Type.__name__ = "Integer32"
_FilterRuleSetDestPortTwo_Object = MibTableColumn
filterRuleSetDestPortTwo = _FilterRuleSetDestPortTwo_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 16),
    _FilterRuleSetDestPortTwo_Type()
)
filterRuleSetDestPortTwo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRuleSetDestPortTwo.setStatus("current")


class _FilterRuleSetSrcRelationBetnPorts_Type(Integer32):
    """Custom type filterRuleSetSrcRelationBetnPorts based on Integer32"""
    defaultValue = 8

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("equalto", 1),
          ("greaterthan", 4),
          ("greaterthanorequalto", 6),
          ("lessthan", 3),
          ("lessthanorequalto", 5),
          ("none", 8),
          ("notequalto", 2),
          ("range", 7))
    )


_FilterRuleSetSrcRelationBetnPorts_Type.__name__ = "Integer32"
_FilterRuleSetSrcRelationBetnPorts_Object = MibTableColumn
filterRuleSetSrcRelationBetnPorts = _FilterRuleSetSrcRelationBetnPorts_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 17),
    _FilterRuleSetSrcRelationBetnPorts_Type()
)
filterRuleSetSrcRelationBetnPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRuleSetSrcRelationBetnPorts.setStatus("current")


class _FilterRuleSetDestRelationBetnPorts_Type(Integer32):
    """Custom type filterRuleSetDestRelationBetnPorts based on Integer32"""
    defaultValue = 8

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("equalto", 1),
          ("greaterthan", 4),
          ("greaterthanorequalto", 6),
          ("lessthan", 3),
          ("lessthanorequalto", 5),
          ("none", 8),
          ("notequalto", 2),
          ("range", 7))
    )


_FilterRuleSetDestRelationBetnPorts_Type.__name__ = "Integer32"
_FilterRuleSetDestRelationBetnPorts_Object = MibTableColumn
filterRuleSetDestRelationBetnPorts = _FilterRuleSetDestRelationBetnPorts_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 18),
    _FilterRuleSetDestRelationBetnPorts_Type()
)
filterRuleSetDestRelationBetnPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRuleSetDestRelationBetnPorts.setStatus("current")


class _FilterRuleSetTcpFlags_Type(Bits):
    """Custom type filterRuleSetTcpFlags based on Bits"""
    namedValues = NamedValues(
        *(("ack", 4),
          ("estaslished", 6),
          ("fin", 0),
          ("psh", 3),
          ("rst", 2),
          ("syn", 1),
          ("urg", 5))
    )

_FilterRuleSetTcpFlags_Type.__name__ = "Bits"
_FilterRuleSetTcpFlags_Object = MibTableColumn
filterRuleSetTcpFlags = _FilterRuleSetTcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 19),
    _FilterRuleSetTcpFlags_Type()
)
filterRuleSetTcpFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRuleSetTcpFlags.setStatus("current")


class _FilterRuleSetLogAction_Type(TruthValue):
    """Custom type filterRuleSetLogAction based on TruthValue"""


_FilterRuleSetLogAction_Object = MibTableColumn
filterRuleSetLogAction = _FilterRuleSetLogAction_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 20),
    _FilterRuleSetLogAction_Type()
)
filterRuleSetLogAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRuleSetLogAction.setStatus("current")


class _FilterRuleSetConfigure_Type(Integer32):
    """Custom type filterRuleSetConfigure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("insert", 2))
    )


_FilterRuleSetConfigure_Type.__name__ = "Integer32"
_FilterRuleSetConfigure_Object = MibTableColumn
filterRuleSetConfigure = _FilterRuleSetConfigure_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 21),
    _FilterRuleSetConfigure_Type()
)
filterRuleSetConfigure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRuleSetConfigure.setStatus("current")
_FilterRuleSetTableRowStatus_Type = RowStatus
_FilterRuleSetTableRowStatus_Object = MibTableColumn
filterRuleSetTableRowStatus = _FilterRuleSetTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 22),
    _FilterRuleSetTableRowStatus_Type()
)
filterRuleSetTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRuleSetTableRowStatus.setStatus("current")
_FilterRuleStatsTable_Object = MibTable
filterRuleStatsTable = _FilterRuleStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 5)
)
if mibBuilder.loadTexts:
    filterRuleStatsTable.setStatus("current")
_FilterRuleStatsTableEntry_Object = MibTableRow
filterRuleStatsTableEntry = _FilterRuleStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 5, 1)
)
filterRuleStatsTableEntry.setIndexNames(
    (0, "TIARA-IP-MIB", "tiaraIpIfIndex"),
)
if mibBuilder.loadTexts:
    filterRuleStatsTableEntry.setStatus("current")
_FilterRuleStatsInBoundPermittedPkts_Type = Counter32
_FilterRuleStatsInBoundPermittedPkts_Object = MibTableColumn
filterRuleStatsInBoundPermittedPkts = _FilterRuleStatsInBoundPermittedPkts_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 5, 1, 1),
    _FilterRuleStatsInBoundPermittedPkts_Type()
)
filterRuleStatsInBoundPermittedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterRuleStatsInBoundPermittedPkts.setStatus("current")
_FilterRuleStatsInBoundDeniedPkts_Type = Counter32
_FilterRuleStatsInBoundDeniedPkts_Object = MibTableColumn
filterRuleStatsInBoundDeniedPkts = _FilterRuleStatsInBoundDeniedPkts_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 5, 1, 2),
    _FilterRuleStatsInBoundDeniedPkts_Type()
)
filterRuleStatsInBoundDeniedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterRuleStatsInBoundDeniedPkts.setStatus("current")
_FilterRuleStatsInBoundUnMatchedPkts_Type = Counter32
_FilterRuleStatsInBoundUnMatchedPkts_Object = MibTableColumn
filterRuleStatsInBoundUnMatchedPkts = _FilterRuleStatsInBoundUnMatchedPkts_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 5, 1, 3),
    _FilterRuleStatsInBoundUnMatchedPkts_Type()
)
filterRuleStatsInBoundUnMatchedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterRuleStatsInBoundUnMatchedPkts.setStatus("current")
_FilterRuleStatsOutBoundPermittedPkts_Type = Counter32
_FilterRuleStatsOutBoundPermittedPkts_Object = MibTableColumn
filterRuleStatsOutBoundPermittedPkts = _FilterRuleStatsOutBoundPermittedPkts_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 5, 1, 4),
    _FilterRuleStatsOutBoundPermittedPkts_Type()
)
filterRuleStatsOutBoundPermittedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterRuleStatsOutBoundPermittedPkts.setStatus("current")
_FilterRuleStatsOutBoundDeniedPkts_Type = Counter32
_FilterRuleStatsOutBoundDeniedPkts_Object = MibTableColumn
filterRuleStatsOutBoundDeniedPkts = _FilterRuleStatsOutBoundDeniedPkts_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 5, 1, 5),
    _FilterRuleStatsOutBoundDeniedPkts_Type()
)
filterRuleStatsOutBoundDeniedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterRuleStatsOutBoundDeniedPkts.setStatus("current")
_FilterRuleStatsOutBoundUnMatchedPkts_Type = Counter32
_FilterRuleStatsOutBoundUnMatchedPkts_Object = MibTableColumn
filterRuleStatsOutBoundUnMatchedPkts = _FilterRuleStatsOutBoundUnMatchedPkts_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 5, 1, 6),
    _FilterRuleStatsOutBoundUnMatchedPkts_Type()
)
filterRuleStatsOutBoundUnMatchedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterRuleStatsOutBoundUnMatchedPkts.setStatus("current")
_FilterRuleStatsNonIpInBoundPkts_Type = Counter32
_FilterRuleStatsNonIpInBoundPkts_Object = MibTableColumn
filterRuleStatsNonIpInBoundPkts = _FilterRuleStatsNonIpInBoundPkts_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 5, 1, 7),
    _FilterRuleStatsNonIpInBoundPkts_Type()
)
filterRuleStatsNonIpInBoundPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterRuleStatsNonIpInBoundPkts.setStatus("current")
_FilterRuleStatsNonIpOutBoundPkts_Type = Counter32
_FilterRuleStatsNonIpOutBoundPkts_Object = MibTableColumn
filterRuleStatsNonIpOutBoundPkts = _FilterRuleStatsNonIpOutBoundPkts_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 5, 1, 8),
    _FilterRuleStatsNonIpOutBoundPkts_Type()
)
filterRuleStatsNonIpOutBoundPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterRuleStatsNonIpOutBoundPkts.setStatus("current")
_FilterRuleStatsBadIpInBoundPkts_Type = Counter32
_FilterRuleStatsBadIpInBoundPkts_Object = MibTableColumn
filterRuleStatsBadIpInBoundPkts = _FilterRuleStatsBadIpInBoundPkts_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 5, 1, 9),
    _FilterRuleStatsBadIpInBoundPkts_Type()
)
filterRuleStatsBadIpInBoundPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterRuleStatsBadIpInBoundPkts.setStatus("current")
_FilterRuleStatsBadIpOutBoundPkts_Type = Counter32
_FilterRuleStatsBadIpOutBoundPkts_Object = MibTableColumn
filterRuleStatsBadIpOutBoundPkts = _FilterRuleStatsBadIpOutBoundPkts_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 51, 5, 1, 10),
    _FilterRuleStatsBadIpOutBoundPkts_Type()
)
filterRuleStatsBadIpOutBoundPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterRuleStatsBadIpOutBoundPkts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIARA-PACKETFILTER-MIB",
    **{"tiaraPacketFilterMib": tiaraPacketFilterMib,
       "filterRuleClearCounters": filterRuleClearCounters,
       "filterNameIndexTable": filterNameIndexTable,
       "filterNameIndexEntry": filterNameIndexEntry,
       "filterEntryName": filterEntryName,
       "filterNameIndex": filterNameIndex,
       "filterEntryRowStatus": filterEntryRowStatus,
       "filterRuleAssignTable": filterRuleAssignTable,
       "filterRuleAssignTableEntry": filterRuleAssignTableEntry,
       "filterRuleSetNameIn": filterRuleSetNameIn,
       "filterRuleSetNameOut": filterRuleSetNameOut,
       "filterRuleAssignTableRowStatus": filterRuleAssignTableRowStatus,
       "filterRuleSetTable": filterRuleSetTable,
       "filterRuleSetTableEntry": filterRuleSetTableEntry,
       "filterRuleSetLineNo": filterRuleSetLineNo,
       "filterRuleName": filterRuleName,
       "filterRuleSetAction": filterRuleSetAction,
       "filterRuleSetProtocolType": filterRuleSetProtocolType,
       "filterRuleSetSrcIpAddr": filterRuleSetSrcIpAddr,
       "filterRuleSetSrcMask": filterRuleSetSrcMask,
       "filterRuleSetDestIpAddr": filterRuleSetDestIpAddr,
       "filterRuleSetDestMask": filterRuleSetDestMask,
       "filterRuleSetPrecedence": filterRuleSetPrecedence,
       "filterRuleSetTos": filterRuleSetTos,
       "filterRuleSetIcmpType": filterRuleSetIcmpType,
       "filterRuleSetIcmpCode": filterRuleSetIcmpCode,
       "filterRuleSetSrcPortOne": filterRuleSetSrcPortOne,
       "filterRuleSetSrcPortTwo": filterRuleSetSrcPortTwo,
       "filterRuleSetDestPortOne": filterRuleSetDestPortOne,
       "filterRuleSetDestPortTwo": filterRuleSetDestPortTwo,
       "filterRuleSetSrcRelationBetnPorts": filterRuleSetSrcRelationBetnPorts,
       "filterRuleSetDestRelationBetnPorts": filterRuleSetDestRelationBetnPorts,
       "filterRuleSetTcpFlags": filterRuleSetTcpFlags,
       "filterRuleSetLogAction": filterRuleSetLogAction,
       "filterRuleSetConfigure": filterRuleSetConfigure,
       "filterRuleSetTableRowStatus": filterRuleSetTableRowStatus,
       "filterRuleStatsTable": filterRuleStatsTable,
       "filterRuleStatsTableEntry": filterRuleStatsTableEntry,
       "filterRuleStatsInBoundPermittedPkts": filterRuleStatsInBoundPermittedPkts,
       "filterRuleStatsInBoundDeniedPkts": filterRuleStatsInBoundDeniedPkts,
       "filterRuleStatsInBoundUnMatchedPkts": filterRuleStatsInBoundUnMatchedPkts,
       "filterRuleStatsOutBoundPermittedPkts": filterRuleStatsOutBoundPermittedPkts,
       "filterRuleStatsOutBoundDeniedPkts": filterRuleStatsOutBoundDeniedPkts,
       "filterRuleStatsOutBoundUnMatchedPkts": filterRuleStatsOutBoundUnMatchedPkts,
       "filterRuleStatsNonIpInBoundPkts": filterRuleStatsNonIpInBoundPkts,
       "filterRuleStatsNonIpOutBoundPkts": filterRuleStatsNonIpOutBoundPkts,
       "filterRuleStatsBadIpInBoundPkts": filterRuleStatsBadIpInBoundPkts,
       "filterRuleStatsBadIpOutBoundPkts": filterRuleStatsBadIpOutBoundPkts}
)
