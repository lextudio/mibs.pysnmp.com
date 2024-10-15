# SNMP MIB module (ACC-DN) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-DN
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:05 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccDn_ObjectIdentity = ObjectIdentity
accDn = _AccDn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19)
)
_AccDnNumber_Type = Integer32
_AccDnNumber_Object = MibScalar
accDnNumber = _AccDnNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 1),
    _AccDnNumber_Type()
)
accDnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnNumber.setStatus("mandatory")
_AccDnID_Type = Integer32
_AccDnID_Object = MibScalar
accDnID = _AccDnID_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 2),
    _AccDnID_Type()
)
accDnID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnID.setStatus("mandatory")


class _AccDnMaxNode_Type(Integer32):
    """Custom type accDnMaxNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_AccDnMaxNode_Type.__name__ = "Integer32"
_AccDnMaxNode_Object = MibScalar
accDnMaxNode = _AccDnMaxNode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 3),
    _AccDnMaxNode_Type()
)
accDnMaxNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnMaxNode.setStatus("mandatory")


class _AccDnMaxArea_Type(Integer32):
    """Custom type accDnMaxArea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_AccDnMaxArea_Type.__name__ = "Integer32"
_AccDnMaxArea_Object = MibScalar
accDnMaxArea = _AccDnMaxArea_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 4),
    _AccDnMaxArea_Type()
)
accDnMaxArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnMaxArea.setStatus("mandatory")


class _AccDnMaxAdjRtr_Type(Integer32):
    """Custom type accDnMaxAdjRtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AccDnMaxAdjRtr_Type.__name__ = "Integer32"
_AccDnMaxAdjRtr_Object = MibScalar
accDnMaxAdjRtr = _AccDnMaxAdjRtr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 5),
    _AccDnMaxAdjRtr_Type()
)
accDnMaxAdjRtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnMaxAdjRtr.setStatus("mandatory")


class _AccDnMaxEndNode_Type(Integer32):
    """Custom type accDnMaxEndNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_AccDnMaxEndNode_Type.__name__ = "Integer32"
_AccDnMaxEndNode_Object = MibScalar
accDnMaxEndNode = _AccDnMaxEndNode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 6),
    _AccDnMaxEndNode_Type()
)
accDnMaxEndNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnMaxEndNode.setStatus("mandatory")


class _AccDnMaxLocHop_Type(Integer32):
    """Custom type accDnMaxLocHop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AccDnMaxLocHop_Type.__name__ = "Integer32"
_AccDnMaxLocHop_Object = MibScalar
accDnMaxLocHop = _AccDnMaxLocHop_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 7),
    _AccDnMaxLocHop_Type()
)
accDnMaxLocHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnMaxLocHop.setStatus("mandatory")


class _AccDnMaxLocCost_Type(Integer32):
    """Custom type accDnMaxLocCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1022),
    )


_AccDnMaxLocCost_Type.__name__ = "Integer32"
_AccDnMaxLocCost_Object = MibScalar
accDnMaxLocCost = _AccDnMaxLocCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 8),
    _AccDnMaxLocCost_Type()
)
accDnMaxLocCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnMaxLocCost.setStatus("mandatory")


class _AccDnMaxVisit_Type(Integer32):
    """Custom type accDnMaxVisit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_AccDnMaxVisit_Type.__name__ = "Integer32"
_AccDnMaxVisit_Object = MibScalar
accDnMaxVisit = _AccDnMaxVisit_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 9),
    _AccDnMaxVisit_Type()
)
accDnMaxVisit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnMaxVisit.setStatus("mandatory")


class _AccDnMaxForHop_Type(Integer32):
    """Custom type accDnMaxForHop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AccDnMaxForHop_Type.__name__ = "Integer32"
_AccDnMaxForHop_Object = MibScalar
accDnMaxForHop = _AccDnMaxForHop_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 10),
    _AccDnMaxForHop_Type()
)
accDnMaxForHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnMaxForHop.setStatus("mandatory")


class _AccDnMaxForCost_Type(Integer32):
    """Custom type accDnMaxForCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1022),
    )


_AccDnMaxForCost_Type.__name__ = "Integer32"
_AccDnMaxForCost_Object = MibScalar
accDnMaxForCost = _AccDnMaxForCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 11),
    _AccDnMaxForCost_Type()
)
accDnMaxForCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnMaxForCost.setStatus("mandatory")
_AccDnBCT1_Type = TimeTicks
_AccDnBCT1_Object = MibScalar
accDnBCT1 = _AccDnBCT1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 12),
    _AccDnBCT1_Type()
)
accDnBCT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnBCT1.setStatus("mandatory")
_AccDnT1_Type = TimeTicks
_AccDnT1_Object = MibScalar
accDnT1 = _AccDnT1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 13),
    _AccDnT1_Type()
)
accDnT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnT1.setStatus("mandatory")


class _AccDnMsgLev_Type(Integer32):
    """Custom type accDnMsgLev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccDnMsgLev_Type.__name__ = "Integer32"
_AccDnMsgLev_Object = MibScalar
accDnMsgLev = _AccDnMsgLev_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 14),
    _AccDnMsgLev_Type()
)
accDnMsgLev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnMsgLev.setStatus("mandatory")


class _AccDnNodeState_Type(Integer32):
    """Custom type accDnNodeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1", 2),
          ("level2", 3),
          ("off", 1))
    )


_AccDnNodeState_Type.__name__ = "Integer32"
_AccDnNodeState_Object = MibScalar
accDnNodeState = _AccDnNodeState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 15),
    _AccDnNodeState_Type()
)
accDnNodeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnNodeState.setStatus("mandatory")
_AccDnUnreachs_Type = Counter32
_AccDnUnreachs_Object = MibScalar
accDnUnreachs = _AccDnUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 16),
    _AccDnUnreachs_Type()
)
accDnUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnUnreachs.setStatus("mandatory")
_AccDnVisitXcds_Type = Counter32
_AccDnVisitXcds_Object = MibScalar
accDnVisitXcds = _AccDnVisitXcds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 17),
    _AccDnVisitXcds_Type()
)
accDnVisitXcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnVisitXcds.setStatus("mandatory")
_AccDnBadNodes_Type = Counter32
_AccDnBadNodes_Object = MibScalar
accDnBadNodes = _AccDnBadNodes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 18),
    _AccDnBadNodes_Type()
)
accDnBadNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnBadNodes.setStatus("mandatory")
_AccDnPktOsizes_Type = Counter32
_AccDnPktOsizes_Object = MibScalar
accDnPktOsizes = _AccDnPktOsizes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 19),
    _AccDnPktOsizes_Type()
)
accDnPktOsizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnPktOsizes.setStatus("mandatory")
_AccDnFmtErrs_Type = Counter32
_AccDnFmtErrs_Object = MibScalar
accDnFmtErrs = _AccDnFmtErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 20),
    _AccDnFmtErrs_Type()
)
accDnFmtErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnFmtErrs.setStatus("mandatory")
_AccDnCktTable_Object = MibTable
accDnCktTable = _AccDnCktTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21)
)
if mibBuilder.loadTexts:
    accDnCktTable.setStatus("mandatory")
_AccDnCktEntry_Object = MibTableRow
accDnCktEntry = _AccDnCktEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1)
)
accDnCktEntry.setIndexNames(
    (0, "ACC-DN", "accDnCktIndex"),
)
if mibBuilder.loadTexts:
    accDnCktEntry.setStatus("mandatory")
_AccDnCktIndex_Type = Integer32
_AccDnCktIndex_Object = MibTableColumn
accDnCktIndex = _AccDnCktIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 1),
    _AccDnCktIndex_Type()
)
accDnCktIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnCktIndex.setStatus("mandatory")


class _AccDnCktStatus_Type(Integer32):
    """Custom type accDnCktStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccDnCktStatus_Type.__name__ = "Integer32"
_AccDnCktStatus_Object = MibTableColumn
accDnCktStatus = _AccDnCktStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 2),
    _AccDnCktStatus_Type()
)
accDnCktStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnCktStatus.setStatus("mandatory")


class _AccDnCktState_Type(Integer32):
    """Custom type accDnCktState based on Integer32"""
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
        *(("down", 2),
          ("shut", 3),
          ("start", 4),
          ("test", 5),
          ("up", 1))
    )


_AccDnCktState_Type.__name__ = "Integer32"
_AccDnCktState_Object = MibTableColumn
accDnCktState = _AccDnCktState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 3),
    _AccDnCktState_Type()
)
accDnCktState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnCktState.setStatus("mandatory")


class _AccDnCktCost_Type(Integer32):
    """Custom type accDnCktCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1022),
    )


_AccDnCktCost_Type.__name__ = "Integer32"
_AccDnCktCost_Object = MibTableColumn
accDnCktCost = _AccDnCktCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 4),
    _AccDnCktCost_Type()
)
accDnCktCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnCktCost.setStatus("mandatory")


class _AccDnMaxRtr_Type(Integer32):
    """Custom type accDnMaxRtr based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AccDnMaxRtr_Type.__name__ = "Integer32"
_AccDnMaxRtr_Object = MibTableColumn
accDnMaxRtr = _AccDnMaxRtr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 5),
    _AccDnMaxRtr_Type()
)
accDnMaxRtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnMaxRtr.setStatus("mandatory")


class _AccDnHelloInt_Type(TimeTicks):
    """Custom type accDnHelloInt based on TimeTicks"""
    defaultValue = 15


_AccDnHelloInt_Object = MibTableColumn
accDnHelloInt = _AccDnHelloInt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 6),
    _AccDnHelloInt_Type()
)
accDnHelloInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnHelloInt.setStatus("mandatory")


class _AccDnRtrPriority_Type(Integer32):
    """Custom type accDnRtrPriority based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccDnRtrPriority_Type.__name__ = "Integer32"
_AccDnRtrPriority_Object = MibTableColumn
accDnRtrPriority = _AccDnRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 7),
    _AccDnRtrPriority_Type()
)
accDnRtrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnRtrPriority.setStatus("mandatory")
_AccDnDesRtrId_Type = OctetString
_AccDnDesRtrId_Object = MibTableColumn
accDnDesRtrId = _AccDnDesRtrId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 8),
    _AccDnDesRtrId_Type()
)
accDnDesRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnDesRtrId.setStatus("mandatory")


class _AccDnDesRtrPrio_Type(Integer32):
    """Custom type accDnDesRtrPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccDnDesRtrPrio_Type.__name__ = "Integer32"
_AccDnDesRtrPrio_Object = MibTableColumn
accDnDesRtrPrio = _AccDnDesRtrPrio_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 9),
    _AccDnDesRtrPrio_Type()
)
accDnDesRtrPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnDesRtrPrio.setStatus("mandatory")
_AccDnTrnPktRecs_Type = Counter32
_AccDnTrnPktRecs_Object = MibTableColumn
accDnTrnPktRecs = _AccDnTrnPktRecs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 10),
    _AccDnTrnPktRecs_Type()
)
accDnTrnPktRecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnTrnPktRecs.setStatus("mandatory")
_AccDnTrnPktSnds_Type = Counter32
_AccDnTrnPktSnds_Object = MibTableColumn
accDnTrnPktSnds = _AccDnTrnPktSnds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 11),
    _AccDnTrnPktSnds_Type()
)
accDnTrnPktSnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnTrnPktSnds.setStatus("mandatory")
_AccDnEndNodePktRecs_Type = Counter32
_AccDnEndNodePktRecs_Object = MibTableColumn
accDnEndNodePktRecs = _AccDnEndNodePktRecs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 12),
    _AccDnEndNodePktRecs_Type()
)
accDnEndNodePktRecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnEndNodePktRecs.setStatus("mandatory")
_AccDnEndNodePktSnds_Type = Counter32
_AccDnEndNodePktSnds_Object = MibTableColumn
accDnEndNodePktSnds = _AccDnEndNodePktSnds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 13),
    _AccDnEndNodePktSnds_Type()
)
accDnEndNodePktSnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnEndNodePktSnds.setStatus("mandatory")
_AccDnCktDowns_Type = Counter32
_AccDnCktDowns_Object = MibTableColumn
accDnCktDowns = _AccDnCktDowns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 14),
    _AccDnCktDowns_Type()
)
accDnCktDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnCktDowns.setStatus("mandatory")


class _AccDnCktType_Type(Integer32):
    """Custom type accDnCktType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              9,
              16,
              129,
              130,
              131)
        )
    )
    namedValues = NamedValues(
        *(("enet", 6),
          ("fr", 131),
          ("lapb", 16),
          ("mlink", 129),
          ("trn", 9),
          ("x25", 130))
    )


_AccDnCktType_Type.__name__ = "Integer32"
_AccDnCktType_Object = MibTableColumn
accDnCktType = _AccDnCktType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 15),
    _AccDnCktType_Type()
)
accDnCktType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnCktType.setStatus("mandatory")


class _AccDnCktPort_Type(Integer32):
    """Custom type accDnCktPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("j1", 1),
          ("j2", 2),
          ("j3", 3))
    )


_AccDnCktPort_Type.__name__ = "Integer32"
_AccDnCktPort_Object = MibTableColumn
accDnCktPort = _AccDnCktPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 16),
    _AccDnCktPort_Type()
)
accDnCktPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnCktPort.setStatus("mandatory")
_AccDnX25InOutAddr_Type = DisplayString
_AccDnX25InOutAddr_Object = MibTableColumn
accDnX25InOutAddr = _AccDnX25InOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 17),
    _AccDnX25InOutAddr_Type()
)
accDnX25InOutAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnX25InOutAddr.setStatus("mandatory")
_AccDnX25InAddr_Type = DisplayString
_AccDnX25InAddr_Object = MibTableColumn
accDnX25InAddr = _AccDnX25InAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 18),
    _AccDnX25InAddr_Type()
)
accDnX25InAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnX25InAddr.setStatus("mandatory")
_AccDnX25Idle_Type = TimeTicks
_AccDnX25Idle_Object = MibTableColumn
accDnX25Idle = _AccDnX25Idle_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 19),
    _AccDnX25Idle_Type()
)
accDnX25Idle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnX25Idle.setStatus("mandatory")


class _AccDnX25PktVal_Type(Integer32):
    """Custom type accDnX25PktVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_AccDnX25PktVal_Type.__name__ = "Integer32"
_AccDnX25PktVal_Object = MibTableColumn
accDnX25PktVal = _AccDnX25PktVal_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 20),
    _AccDnX25PktVal_Type()
)
accDnX25PktVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnX25PktVal.setStatus("mandatory")


class _AccDnX25PktWin_Type(Integer32):
    """Custom type accDnX25PktWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AccDnX25PktWin_Type.__name__ = "Integer32"
_AccDnX25PktWin_Object = MibTableColumn
accDnX25PktWin = _AccDnX25PktWin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 21),
    _AccDnX25PktWin_Type()
)
accDnX25PktWin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnX25PktWin.setStatus("mandatory")


class _AccDnEntryStatus_Type(Integer32):
    """Custom type accDnEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_AccDnEntryStatus_Type.__name__ = "Integer32"
_AccDnEntryStatus_Object = MibTableColumn
accDnEntryStatus = _AccDnEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 22),
    _AccDnEntryStatus_Type()
)
accDnEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnEntryStatus.setStatus("mandatory")


class _AccDnX25FacIndex_Type(Integer32):
    """Custom type accDnX25FacIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccDnX25FacIndex_Type.__name__ = "Integer32"
_AccDnX25FacIndex_Object = MibTableColumn
accDnX25FacIndex = _AccDnX25FacIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 23),
    _AccDnX25FacIndex_Type()
)
accDnX25FacIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnX25FacIndex.setStatus("mandatory")
_AccDnRtTable_Object = MibTable
accDnRtTable = _AccDnRtTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 22)
)
if mibBuilder.loadTexts:
    accDnRtTable.setStatus("mandatory")
_AccDnRtEntry_Object = MibTableRow
accDnRtEntry = _AccDnRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 22, 1)
)
accDnRtEntry.setIndexNames(
    (0, "ACC-DN", "accDnRtNode"),
)
if mibBuilder.loadTexts:
    accDnRtEntry.setStatus("mandatory")
_AccDnRtNode_Type = Integer32
_AccDnRtNode_Object = MibTableColumn
accDnRtNode = _AccDnRtNode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 22, 1, 1),
    _AccDnRtNode_Type()
)
accDnRtNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnRtNode.setStatus("mandatory")
_AccDnRtHops_Type = Integer32
_AccDnRtHops_Object = MibTableColumn
accDnRtHops = _AccDnRtHops_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 22, 1, 2),
    _AccDnRtHops_Type()
)
accDnRtHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnRtHops.setStatus("mandatory")
_AccDnRtCost_Type = Integer32
_AccDnRtCost_Object = MibTableColumn
accDnRtCost = _AccDnRtCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 22, 1, 3),
    _AccDnRtCost_Type()
)
accDnRtCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnRtCost.setStatus("mandatory")
_AccDnRtCkt_Type = Integer32
_AccDnRtCkt_Object = MibTableColumn
accDnRtCkt = _AccDnRtCkt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 22, 1, 4),
    _AccDnRtCkt_Type()
)
accDnRtCkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnRtCkt.setStatus("mandatory")
_AccDnRtNextHop_Type = Integer32
_AccDnRtNextHop_Object = MibTableColumn
accDnRtNextHop = _AccDnRtNextHop_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 22, 1, 5),
    _AccDnRtNextHop_Type()
)
accDnRtNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnRtNextHop.setStatus("mandatory")
_AccDnAreaTable_Object = MibTable
accDnAreaTable = _AccDnAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 23)
)
if mibBuilder.loadTexts:
    accDnAreaTable.setStatus("mandatory")
_AccDnAreaEntry_Object = MibTableRow
accDnAreaEntry = _AccDnAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 23, 1)
)
accDnAreaEntry.setIndexNames(
    (0, "ACC-DN", "accDnAreaArea"),
)
if mibBuilder.loadTexts:
    accDnAreaEntry.setStatus("mandatory")
_AccDnAreaArea_Type = Integer32
_AccDnAreaArea_Object = MibTableColumn
accDnAreaArea = _AccDnAreaArea_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 23, 1, 1),
    _AccDnAreaArea_Type()
)
accDnAreaArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnAreaArea.setStatus("mandatory")
_AccDnAreaHops_Type = Integer32
_AccDnAreaHops_Object = MibTableColumn
accDnAreaHops = _AccDnAreaHops_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 23, 1, 2),
    _AccDnAreaHops_Type()
)
accDnAreaHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnAreaHops.setStatus("mandatory")
_AccDnAreaCost_Type = Integer32
_AccDnAreaCost_Object = MibTableColumn
accDnAreaCost = _AccDnAreaCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 23, 1, 3),
    _AccDnAreaCost_Type()
)
accDnAreaCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnAreaCost.setStatus("mandatory")
_AccDnAreaCkt_Type = Integer32
_AccDnAreaCkt_Object = MibTableColumn
accDnAreaCkt = _AccDnAreaCkt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 23, 1, 4),
    _AccDnAreaCkt_Type()
)
accDnAreaCkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnAreaCkt.setStatus("mandatory")
_AccDnAreaNextHop_Type = Integer32
_AccDnAreaNextHop_Object = MibTableColumn
accDnAreaNextHop = _AccDnAreaNextHop_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 23, 1, 5),
    _AccDnAreaNextHop_Type()
)
accDnAreaNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnAreaNextHop.setStatus("mandatory")
_AccDnRouteFilterTable_Object = MibTable
accDnRouteFilterTable = _AccDnRouteFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 24)
)
if mibBuilder.loadTexts:
    accDnRouteFilterTable.setStatus("mandatory")
_AccDnRouteFilterEntry_Object = MibTableRow
accDnRouteFilterEntry = _AccDnRouteFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 24, 1)
)
accDnRouteFilterEntry.setIndexNames(
    (0, "ACC-DN", "accDnRouteFilterAdj"),
    (0, "ACC-DN", "accDnRouteFilterNode"),
)
if mibBuilder.loadTexts:
    accDnRouteFilterEntry.setStatus("mandatory")


class _AccDnRouteFilterAdj_Type(Integer32):
    """Custom type accDnRouteFilterAdj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccDnRouteFilterAdj_Type.__name__ = "Integer32"
_AccDnRouteFilterAdj_Object = MibTableColumn
accDnRouteFilterAdj = _AccDnRouteFilterAdj_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 24, 1, 1),
    _AccDnRouteFilterAdj_Type()
)
accDnRouteFilterAdj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnRouteFilterAdj.setStatus("mandatory")


class _AccDnRouteFilterNode_Type(Integer32):
    """Custom type accDnRouteFilterNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccDnRouteFilterNode_Type.__name__ = "Integer32"
_AccDnRouteFilterNode_Object = MibTableColumn
accDnRouteFilterNode = _AccDnRouteFilterNode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 24, 1, 2),
    _AccDnRouteFilterNode_Type()
)
accDnRouteFilterNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnRouteFilterNode.setStatus("mandatory")


class _AccDnRouteFilterDisposition_Type(Integer32):
    """Custom type accDnRouteFilterDisposition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_AccDnRouteFilterDisposition_Type.__name__ = "Integer32"
_AccDnRouteFilterDisposition_Object = MibTableColumn
accDnRouteFilterDisposition = _AccDnRouteFilterDisposition_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 24, 1, 3),
    _AccDnRouteFilterDisposition_Type()
)
accDnRouteFilterDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnRouteFilterDisposition.setStatus("mandatory")


class _AccDnRouteFilterEntStat_Type(Integer32):
    """Custom type accDnRouteFilterEntStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccDnRouteFilterEntStat_Type.__name__ = "Integer32"
_AccDnRouteFilterEntStat_Object = MibTableColumn
accDnRouteFilterEntStat = _AccDnRouteFilterEntStat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 24, 1, 4),
    _AccDnRouteFilterEntStat_Type()
)
accDnRouteFilterEntStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnRouteFilterEntStat.setStatus("mandatory")
_AccDnForwardFilterTable_Object = MibTable
accDnForwardFilterTable = _AccDnForwardFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 25)
)
if mibBuilder.loadTexts:
    accDnForwardFilterTable.setStatus("mandatory")
_AccDnForwardFilterEntry_Object = MibTableRow
accDnForwardFilterEntry = _AccDnForwardFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 25, 1)
)
accDnForwardFilterEntry.setIndexNames(
    (0, "ACC-DN", "accDnForwardFilterDest"),
    (0, "ACC-DN", "accDnForwardFilterSource"),
)
if mibBuilder.loadTexts:
    accDnForwardFilterEntry.setStatus("mandatory")


class _AccDnForwardFilterDest_Type(Integer32):
    """Custom type accDnForwardFilterDest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccDnForwardFilterDest_Type.__name__ = "Integer32"
_AccDnForwardFilterDest_Object = MibTableColumn
accDnForwardFilterDest = _AccDnForwardFilterDest_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 25, 1, 1),
    _AccDnForwardFilterDest_Type()
)
accDnForwardFilterDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnForwardFilterDest.setStatus("mandatory")


class _AccDnForwardFilterSource_Type(Integer32):
    """Custom type accDnForwardFilterSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccDnForwardFilterSource_Type.__name__ = "Integer32"
_AccDnForwardFilterSource_Object = MibTableColumn
accDnForwardFilterSource = _AccDnForwardFilterSource_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 25, 1, 2),
    _AccDnForwardFilterSource_Type()
)
accDnForwardFilterSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnForwardFilterSource.setStatus("mandatory")


class _AccDnForwardFilterDisposition_Type(Integer32):
    """Custom type accDnForwardFilterDisposition based on Integer32"""
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
        *(("discard", 0),
          ("highPriority", 3),
          ("lowPriority", 1),
          ("normalPriority", 2))
    )


_AccDnForwardFilterDisposition_Type.__name__ = "Integer32"
_AccDnForwardFilterDisposition_Object = MibTableColumn
accDnForwardFilterDisposition = _AccDnForwardFilterDisposition_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 25, 1, 3),
    _AccDnForwardFilterDisposition_Type()
)
accDnForwardFilterDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnForwardFilterDisposition.setStatus("mandatory")


class _AccDnForwardFilterEntStat_Type(Integer32):
    """Custom type accDnForwardFilterEntStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccDnForwardFilterEntStat_Type.__name__ = "Integer32"
_AccDnForwardFilterEntStat_Object = MibTableColumn
accDnForwardFilterEntStat = _AccDnForwardFilterEntStat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 25, 1, 4),
    _AccDnForwardFilterEntStat_Type()
)
accDnForwardFilterEntStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnForwardFilterEntStat.setStatus("mandatory")
_AccDnAdjTable_Object = MibTable
accDnAdjTable = _AccDnAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 26)
)
if mibBuilder.loadTexts:
    accDnAdjTable.setStatus("mandatory")
_AccDnAdjEntry_Object = MibTableRow
accDnAdjEntry = _AccDnAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 26, 1)
)
accDnAdjEntry.setIndexNames(
    (0, "ACC-DN", "accDnAdjNode"),
)
if mibBuilder.loadTexts:
    accDnAdjEntry.setStatus("mandatory")


class _AccDnAdjNode_Type(Integer32):
    """Custom type accDnAdjNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccDnAdjNode_Type.__name__ = "Integer32"
_AccDnAdjNode_Object = MibTableColumn
accDnAdjNode = _AccDnAdjNode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 26, 1, 1),
    _AccDnAdjNode_Type()
)
accDnAdjNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnAdjNode.setStatus("mandatory")


class _AccDnAdjType_Type(Integer32):
    """Custom type accDnAdjType based on Integer32"""
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
        *(("endNode", 4),
          ("level1", 3),
          ("level2", 2),
          ("level2Only", 1))
    )


_AccDnAdjType_Type.__name__ = "Integer32"
_AccDnAdjType_Object = MibTableColumn
accDnAdjType = _AccDnAdjType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 26, 1, 2),
    _AccDnAdjType_Type()
)
accDnAdjType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnAdjType.setStatus("mandatory")
_AccDnAdjCircuit_Type = Integer32
_AccDnAdjCircuit_Object = MibTableColumn
accDnAdjCircuit = _AccDnAdjCircuit_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 26, 1, 3),
    _AccDnAdjCircuit_Type()
)
accDnAdjCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnAdjCircuit.setStatus("mandatory")


class _AccDnAdjState_Type(Integer32):
    """Custom type accDnAdjState based on Integer32"""
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
        *(("circuitFailed", 3),
          ("initializing", 2),
          ("timedOut", 4),
          ("up", 1))
    )


_AccDnAdjState_Type.__name__ = "Integer32"
_AccDnAdjState_Object = MibTableColumn
accDnAdjState = _AccDnAdjState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 26, 1, 4),
    _AccDnAdjState_Type()
)
accDnAdjState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnAdjState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-DN",
    **{"accDn": accDn,
       "accDnNumber": accDnNumber,
       "accDnID": accDnID,
       "accDnMaxNode": accDnMaxNode,
       "accDnMaxArea": accDnMaxArea,
       "accDnMaxAdjRtr": accDnMaxAdjRtr,
       "accDnMaxEndNode": accDnMaxEndNode,
       "accDnMaxLocHop": accDnMaxLocHop,
       "accDnMaxLocCost": accDnMaxLocCost,
       "accDnMaxVisit": accDnMaxVisit,
       "accDnMaxForHop": accDnMaxForHop,
       "accDnMaxForCost": accDnMaxForCost,
       "accDnBCT1": accDnBCT1,
       "accDnT1": accDnT1,
       "accDnMsgLev": accDnMsgLev,
       "accDnNodeState": accDnNodeState,
       "accDnUnreachs": accDnUnreachs,
       "accDnVisitXcds": accDnVisitXcds,
       "accDnBadNodes": accDnBadNodes,
       "accDnPktOsizes": accDnPktOsizes,
       "accDnFmtErrs": accDnFmtErrs,
       "accDnCktTable": accDnCktTable,
       "accDnCktEntry": accDnCktEntry,
       "accDnCktIndex": accDnCktIndex,
       "accDnCktStatus": accDnCktStatus,
       "accDnCktState": accDnCktState,
       "accDnCktCost": accDnCktCost,
       "accDnMaxRtr": accDnMaxRtr,
       "accDnHelloInt": accDnHelloInt,
       "accDnRtrPriority": accDnRtrPriority,
       "accDnDesRtrId": accDnDesRtrId,
       "accDnDesRtrPrio": accDnDesRtrPrio,
       "accDnTrnPktRecs": accDnTrnPktRecs,
       "accDnTrnPktSnds": accDnTrnPktSnds,
       "accDnEndNodePktRecs": accDnEndNodePktRecs,
       "accDnEndNodePktSnds": accDnEndNodePktSnds,
       "accDnCktDowns": accDnCktDowns,
       "accDnCktType": accDnCktType,
       "accDnCktPort": accDnCktPort,
       "accDnX25InOutAddr": accDnX25InOutAddr,
       "accDnX25InAddr": accDnX25InAddr,
       "accDnX25Idle": accDnX25Idle,
       "accDnX25PktVal": accDnX25PktVal,
       "accDnX25PktWin": accDnX25PktWin,
       "accDnEntryStatus": accDnEntryStatus,
       "accDnX25FacIndex": accDnX25FacIndex,
       "accDnRtTable": accDnRtTable,
       "accDnRtEntry": accDnRtEntry,
       "accDnRtNode": accDnRtNode,
       "accDnRtHops": accDnRtHops,
       "accDnRtCost": accDnRtCost,
       "accDnRtCkt": accDnRtCkt,
       "accDnRtNextHop": accDnRtNextHop,
       "accDnAreaTable": accDnAreaTable,
       "accDnAreaEntry": accDnAreaEntry,
       "accDnAreaArea": accDnAreaArea,
       "accDnAreaHops": accDnAreaHops,
       "accDnAreaCost": accDnAreaCost,
       "accDnAreaCkt": accDnAreaCkt,
       "accDnAreaNextHop": accDnAreaNextHop,
       "accDnRouteFilterTable": accDnRouteFilterTable,
       "accDnRouteFilterEntry": accDnRouteFilterEntry,
       "accDnRouteFilterAdj": accDnRouteFilterAdj,
       "accDnRouteFilterNode": accDnRouteFilterNode,
       "accDnRouteFilterDisposition": accDnRouteFilterDisposition,
       "accDnRouteFilterEntStat": accDnRouteFilterEntStat,
       "accDnForwardFilterTable": accDnForwardFilterTable,
       "accDnForwardFilterEntry": accDnForwardFilterEntry,
       "accDnForwardFilterDest": accDnForwardFilterDest,
       "accDnForwardFilterSource": accDnForwardFilterSource,
       "accDnForwardFilterDisposition": accDnForwardFilterDisposition,
       "accDnForwardFilterEntStat": accDnForwardFilterEntStat,
       "accDnAdjTable": accDnAdjTable,
       "accDnAdjEntry": accDnAdjEntry,
       "accDnAdjNode": accDnAdjNode,
       "accDnAdjType": accDnAdjType,
       "accDnAdjCircuit": accDnAdjCircuit,
       "accDnAdjState": accDnAdjState}
)
