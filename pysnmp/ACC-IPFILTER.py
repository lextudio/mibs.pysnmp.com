# SNMP MIB module (ACC-IPFILTER) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-IPFILTER
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:21 2024
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

_AccIpFilter_ObjectIdentity = ObjectIdentity
accIpFilter = _AccIpFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18)
)


class _AccIpSrcRouting_Type(Integer32):
    """Custom type accIpSrcRouting based on Integer32"""
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


_AccIpSrcRouting_Type.__name__ = "Integer32"
_AccIpSrcRouting_Object = MibScalar
accIpSrcRouting = _AccIpSrcRouting_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 1),
    _AccIpSrcRouting_Type()
)
accIpSrcRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpSrcRouting.setStatus("mandatory")
_AccIpFiltTable_Object = MibTable
accIpFiltTable = _AccIpFiltTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 2)
)
if mibBuilder.loadTexts:
    accIpFiltTable.setStatus("deprecated")
_AccIpFiltEntry_Object = MibTableRow
accIpFiltEntry = _AccIpFiltEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 2, 1)
)
accIpFiltEntry.setIndexNames(
    (0, "ACC-IPFILTER", "accIpFiltDAddr"),
    (0, "ACC-IPFILTER", "accIpFiltDNetMask"),
    (0, "ACC-IPFILTER", "accIpFiltSAddr"),
    (0, "ACC-IPFILTER", "accIpFiltSNetMask"),
    (0, "ACC-IPFILTER", "accIpFiltParm"),
    (0, "ACC-IPFILTER", "accIpFiltDisp"),
)
if mibBuilder.loadTexts:
    accIpFiltEntry.setStatus("deprecated")
_AccIpFiltDAddr_Type = IpAddress
_AccIpFiltDAddr_Object = MibTableColumn
accIpFiltDAddr = _AccIpFiltDAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 2, 1, 1),
    _AccIpFiltDAddr_Type()
)
accIpFiltDAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpFiltDAddr.setStatus("deprecated")
_AccIpFiltDNetMask_Type = IpAddress
_AccIpFiltDNetMask_Object = MibTableColumn
accIpFiltDNetMask = _AccIpFiltDNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 2, 1, 2),
    _AccIpFiltDNetMask_Type()
)
accIpFiltDNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpFiltDNetMask.setStatus("deprecated")
_AccIpFiltSAddr_Type = IpAddress
_AccIpFiltSAddr_Object = MibTableColumn
accIpFiltSAddr = _AccIpFiltSAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 2, 1, 3),
    _AccIpFiltSAddr_Type()
)
accIpFiltSAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpFiltSAddr.setStatus("deprecated")
_AccIpFiltSNetMask_Type = IpAddress
_AccIpFiltSNetMask_Object = MibTableColumn
accIpFiltSNetMask = _AccIpFiltSNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 2, 1, 4),
    _AccIpFiltSNetMask_Type()
)
accIpFiltSNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpFiltSNetMask.setStatus("deprecated")
_AccIpFiltParm_Type = OctetString
_AccIpFiltParm_Object = MibTableColumn
accIpFiltParm = _AccIpFiltParm_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 2, 1, 5),
    _AccIpFiltParm_Type()
)
accIpFiltParm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpFiltParm.setStatus("deprecated")


class _AccIpFiltDisp_Type(Integer32):
    """Custom type accIpFiltDisp based on Integer32"""
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
        *(("discard", 1),
          ("highPriority", 3),
          ("lowPriority", 2),
          ("normalPriority", 0))
    )


_AccIpFiltDisp_Type.__name__ = "Integer32"
_AccIpFiltDisp_Object = MibTableColumn
accIpFiltDisp = _AccIpFiltDisp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 2, 1, 6),
    _AccIpFiltDisp_Type()
)
accIpFiltDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpFiltDisp.setStatus("deprecated")
_AccIpSmdsAtTable_Object = MibTable
accIpSmdsAtTable = _AccIpSmdsAtTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 3)
)
if mibBuilder.loadTexts:
    accIpSmdsAtTable.setStatus("mandatory")
_AccIpSmdsAtEntry_Object = MibTableRow
accIpSmdsAtEntry = _AccIpSmdsAtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 3, 1)
)
accIpSmdsAtEntry.setIndexNames(
    (0, "ACC-IPFILTER", "accIpSmdsAtIpAddr"),
)
if mibBuilder.loadTexts:
    accIpSmdsAtEntry.setStatus("mandatory")
_AccIpSmdsAtIpAddr_Type = IpAddress
_AccIpSmdsAtIpAddr_Object = MibTableColumn
accIpSmdsAtIpAddr = _AccIpSmdsAtIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 3, 1, 1),
    _AccIpSmdsAtIpAddr_Type()
)
accIpSmdsAtIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpSmdsAtIpAddr.setStatus("mandatory")
_AccIpSmdsAtSmdsAddr_Type = SmdsAddress
_AccIpSmdsAtSmdsAddr_Object = MibTableColumn
accIpSmdsAtSmdsAddr = _AccIpSmdsAtSmdsAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 3, 1, 2),
    _AccIpSmdsAtSmdsAddr_Type()
)
accIpSmdsAtSmdsAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpSmdsAtSmdsAddr.setStatus("mandatory")
_AccIpSmdsAtIpMcast_Type = SmdsAddress
_AccIpSmdsAtIpMcast_Object = MibTableColumn
accIpSmdsAtIpMcast = _AccIpSmdsAtIpMcast_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 3, 1, 3),
    _AccIpSmdsAtIpMcast_Type()
)
accIpSmdsAtIpMcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpSmdsAtIpMcast.setStatus("mandatory")
_AccIpSmdsAtArpMcast_Type = SmdsAddress
_AccIpSmdsAtArpMcast_Object = MibTableColumn
accIpSmdsAtArpMcast = _AccIpSmdsAtArpMcast_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 3, 1, 4),
    _AccIpSmdsAtArpMcast_Type()
)
accIpSmdsAtArpMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpSmdsAtArpMcast.setStatus("mandatory")


class _AccIpSubDirBcast_Type(Integer32):
    """Custom type accIpSubDirBcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bcast", 1),
          ("nobcast", 2))
    )


_AccIpSubDirBcast_Type.__name__ = "Integer32"
_AccIpSubDirBcast_Object = MibScalar
accIpSubDirBcast = _AccIpSubDirBcast_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 4),
    _AccIpSubDirBcast_Type()
)
accIpSubDirBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpSubDirBcast.setStatus("mandatory")
_AccIpIfFiltDispTable_Object = MibTable
accIpIfFiltDispTable = _AccIpIfFiltDispTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5)
)
if mibBuilder.loadTexts:
    accIpIfFiltDispTable.setStatus("mandatory")
_AccIpIfFiltDispEntry_Object = MibTableRow
accIpIfFiltDispEntry = _AccIpIfFiltDispEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1)
)
accIpIfFiltDispEntry.setIndexNames(
    (0, "ACC-IPFILTER", "accIpIfFiltDispIfIndex"),
    (0, "ACC-IPFILTER", "accIpIfFiltDispPktDir"),
    (0, "ACC-IPFILTER", "accIpIfFiltDispSeqNum"),
)
if mibBuilder.loadTexts:
    accIpIfFiltDispEntry.setStatus("mandatory")
_AccIpIfFiltDispIfIndex_Type = Integer32
_AccIpIfFiltDispIfIndex_Object = MibTableColumn
accIpIfFiltDispIfIndex = _AccIpIfFiltDispIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 1),
    _AccIpIfFiltDispIfIndex_Type()
)
accIpIfFiltDispIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispIfIndex.setStatus("mandatory")


class _AccIpIfFiltDispPktDir_Type(Integer32):
    """Custom type accIpIfFiltDispPktDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("global", 3),
          ("input", 1),
          ("output", 2))
    )


_AccIpIfFiltDispPktDir_Type.__name__ = "Integer32"
_AccIpIfFiltDispPktDir_Object = MibTableColumn
accIpIfFiltDispPktDir = _AccIpIfFiltDispPktDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 2),
    _AccIpIfFiltDispPktDir_Type()
)
accIpIfFiltDispPktDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispPktDir.setStatus("mandatory")
_AccIpIfFiltDispSeqNum_Type = Integer32
_AccIpIfFiltDispSeqNum_Object = MibTableColumn
accIpIfFiltDispSeqNum = _AccIpIfFiltDispSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 3),
    _AccIpIfFiltDispSeqNum_Type()
)
accIpIfFiltDispSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispSeqNum.setStatus("mandatory")
_AccIpIfFiltDispDAddr_Type = IpAddress
_AccIpIfFiltDispDAddr_Object = MibTableColumn
accIpIfFiltDispDAddr = _AccIpIfFiltDispDAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 4),
    _AccIpIfFiltDispDAddr_Type()
)
accIpIfFiltDispDAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispDAddr.setStatus("mandatory")
_AccIpIfFiltDispDNetMask_Type = IpAddress
_AccIpIfFiltDispDNetMask_Object = MibTableColumn
accIpIfFiltDispDNetMask = _AccIpIfFiltDispDNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 5),
    _AccIpIfFiltDispDNetMask_Type()
)
accIpIfFiltDispDNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispDNetMask.setStatus("mandatory")
_AccIpIfFiltDispSAddr_Type = IpAddress
_AccIpIfFiltDispSAddr_Object = MibTableColumn
accIpIfFiltDispSAddr = _AccIpIfFiltDispSAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 6),
    _AccIpIfFiltDispSAddr_Type()
)
accIpIfFiltDispSAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispSAddr.setStatus("mandatory")
_AccIpIfFiltDispSNetMask_Type = IpAddress
_AccIpIfFiltDispSNetMask_Object = MibTableColumn
accIpIfFiltDispSNetMask = _AccIpIfFiltDispSNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 7),
    _AccIpIfFiltDispSNetMask_Type()
)
accIpIfFiltDispSNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispSNetMask.setStatus("mandatory")


class _AccIpIfFiltDispOp1_Type(Integer32):
    """Custom type accIpIfFiltDispOp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 3),
          ("none", 1),
          ("not-equal", 2))
    )


_AccIpIfFiltDispOp1_Type.__name__ = "Integer32"
_AccIpIfFiltDispOp1_Object = MibTableColumn
accIpIfFiltDispOp1 = _AccIpIfFiltDispOp1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 8),
    _AccIpIfFiltDispOp1_Type()
)
accIpIfFiltDispOp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispOp1.setStatus("mandatory")


class _AccIpIfFiltDispProtocol_Type(Integer32):
    """Custom type accIpIfFiltDispProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccIpIfFiltDispProtocol_Type.__name__ = "Integer32"
_AccIpIfFiltDispProtocol_Object = MibTableColumn
accIpIfFiltDispProtocol = _AccIpIfFiltDispProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 9),
    _AccIpIfFiltDispProtocol_Type()
)
accIpIfFiltDispProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispProtocol.setStatus("mandatory")


class _AccIpIfFiltDispOp2_Type(Integer32):
    """Custom type accIpIfFiltDispOp2 based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("dst-equal", 13),
          ("dst-greater-than", 12),
          ("dst-less-than", 11),
          ("dst-not-equal", 10),
          ("equal", 5),
          ("greater-than", 4),
          ("less-than", 3),
          ("none", 1),
          ("not-equal", 2),
          ("src-equal", 9),
          ("src-greater-than", 8),
          ("src-less-than", 7),
          ("src-not-equal", 6))
    )


_AccIpIfFiltDispOp2_Type.__name__ = "Integer32"
_AccIpIfFiltDispOp2_Object = MibTableColumn
accIpIfFiltDispOp2 = _AccIpIfFiltDispOp2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 10),
    _AccIpIfFiltDispOp2_Type()
)
accIpIfFiltDispOp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispOp2.setStatus("mandatory")


class _AccIpIfFiltDispUDPTCPPort_Type(Integer32):
    """Custom type accIpIfFiltDispUDPTCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccIpIfFiltDispUDPTCPPort_Type.__name__ = "Integer32"
_AccIpIfFiltDispUDPTCPPort_Object = MibTableColumn
accIpIfFiltDispUDPTCPPort = _AccIpIfFiltDispUDPTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 11),
    _AccIpIfFiltDispUDPTCPPort_Type()
)
accIpIfFiltDispUDPTCPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispUDPTCPPort.setStatus("mandatory")


class _AccIpIfFiltDispDispos_Type(Integer32):
    """Custom type accIpIfFiltDispDispos based on Integer32"""
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
        *(("discard", 1),
          ("highPriority", 5),
          ("log", 2),
          ("lowPriority", 3),
          ("normalPriority", 4))
    )


_AccIpIfFiltDispDispos_Type.__name__ = "Integer32"
_AccIpIfFiltDispDispos_Object = MibTableColumn
accIpIfFiltDispDispos = _AccIpIfFiltDispDispos_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 12),
    _AccIpIfFiltDispDispos_Type()
)
accIpIfFiltDispDispos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispDispos.setStatus("mandatory")
_AccIpIfFiltDispMatches_Type = Counter32
_AccIpIfFiltDispMatches_Object = MibTableColumn
accIpIfFiltDispMatches = _AccIpIfFiltDispMatches_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 13),
    _AccIpIfFiltDispMatches_Type()
)
accIpIfFiltDispMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispMatches.setStatus("mandatory")
_AccIpIfFiltDispLastMatchTime_Type = TimeTicks
_AccIpIfFiltDispLastMatchTime_Object = MibTableColumn
accIpIfFiltDispLastMatchTime = _AccIpIfFiltDispLastMatchTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 14),
    _AccIpIfFiltDispLastMatchTime_Type()
)
accIpIfFiltDispLastMatchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispLastMatchTime.setStatus("mandatory")
_AccIpIfFiltDispMatchPkt_Type = OctetString
_AccIpIfFiltDispMatchPkt_Object = MibTableColumn
accIpIfFiltDispMatchPkt = _AccIpIfFiltDispMatchPkt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 15),
    _AccIpIfFiltDispMatchPkt_Type()
)
accIpIfFiltDispMatchPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispMatchPkt.setStatus("mandatory")
_AccIpIfFiltEditTable_Object = MibTable
accIpIfFiltEditTable = _AccIpIfFiltEditTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6)
)
if mibBuilder.loadTexts:
    accIpIfFiltEditTable.setStatus("mandatory")
_AccIpIfFiltEditEntry_Object = MibTableRow
accIpIfFiltEditEntry = _AccIpIfFiltEditEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1)
)
accIpIfFiltEditEntry.setIndexNames(
    (0, "ACC-IPFILTER", "accIpIfFiltEditIndex"),
)
if mibBuilder.loadTexts:
    accIpIfFiltEditEntry.setStatus("mandatory")
_AccIpIfFiltEditIndex_Type = Integer32
_AccIpIfFiltEditIndex_Object = MibTableColumn
accIpIfFiltEditIndex = _AccIpIfFiltEditIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 1),
    _AccIpIfFiltEditIndex_Type()
)
accIpIfFiltEditIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltEditIndex.setStatus("mandatory")


class _AccIpIfFiltEditAction_Type(Integer32):
    """Custom type accIpIfFiltEditAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_AccIpIfFiltEditAction_Type.__name__ = "Integer32"
_AccIpIfFiltEditAction_Object = MibTableColumn
accIpIfFiltEditAction = _AccIpIfFiltEditAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 2),
    _AccIpIfFiltEditAction_Type()
)
accIpIfFiltEditAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpIfFiltEditAction.setStatus("mandatory")
_AccIpIfFiltEditIfIndex_Type = Integer32
_AccIpIfFiltEditIfIndex_Object = MibTableColumn
accIpIfFiltEditIfIndex = _AccIpIfFiltEditIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 3),
    _AccIpIfFiltEditIfIndex_Type()
)
accIpIfFiltEditIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpIfFiltEditIfIndex.setStatus("mandatory")


class _AccIpIfFiltEditPktDir_Type(Integer32):
    """Custom type accIpIfFiltEditPktDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("global", 3),
          ("input", 1),
          ("output", 2))
    )


_AccIpIfFiltEditPktDir_Type.__name__ = "Integer32"
_AccIpIfFiltEditPktDir_Object = MibTableColumn
accIpIfFiltEditPktDir = _AccIpIfFiltEditPktDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 4),
    _AccIpIfFiltEditPktDir_Type()
)
accIpIfFiltEditPktDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpIfFiltEditPktDir.setStatus("mandatory")
_AccIpIfFiltEditDAddr_Type = IpAddress
_AccIpIfFiltEditDAddr_Object = MibTableColumn
accIpIfFiltEditDAddr = _AccIpIfFiltEditDAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 5),
    _AccIpIfFiltEditDAddr_Type()
)
accIpIfFiltEditDAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpIfFiltEditDAddr.setStatus("mandatory")
_AccIpIfFiltEditDNetMask_Type = IpAddress
_AccIpIfFiltEditDNetMask_Object = MibTableColumn
accIpIfFiltEditDNetMask = _AccIpIfFiltEditDNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 6),
    _AccIpIfFiltEditDNetMask_Type()
)
accIpIfFiltEditDNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpIfFiltEditDNetMask.setStatus("mandatory")
_AccIpIfFiltEditSAddr_Type = IpAddress
_AccIpIfFiltEditSAddr_Object = MibTableColumn
accIpIfFiltEditSAddr = _AccIpIfFiltEditSAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 7),
    _AccIpIfFiltEditSAddr_Type()
)
accIpIfFiltEditSAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpIfFiltEditSAddr.setStatus("mandatory")
_AccIpIfFiltEditSNetMask_Type = IpAddress
_AccIpIfFiltEditSNetMask_Object = MibTableColumn
accIpIfFiltEditSNetMask = _AccIpIfFiltEditSNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 8),
    _AccIpIfFiltEditSNetMask_Type()
)
accIpIfFiltEditSNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpIfFiltEditSNetMask.setStatus("mandatory")


class _AccIpIfFiltEditOp1_Type(Integer32):
    """Custom type accIpIfFiltEditOp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 2),
          ("none", 1),
          ("not-equal", 3))
    )


_AccIpIfFiltEditOp1_Type.__name__ = "Integer32"
_AccIpIfFiltEditOp1_Object = MibTableColumn
accIpIfFiltEditOp1 = _AccIpIfFiltEditOp1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 9),
    _AccIpIfFiltEditOp1_Type()
)
accIpIfFiltEditOp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpIfFiltEditOp1.setStatus("mandatory")


class _AccIpIfFiltEditProtocol_Type(Integer32):
    """Custom type accIpIfFiltEditProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccIpIfFiltEditProtocol_Type.__name__ = "Integer32"
_AccIpIfFiltEditProtocol_Object = MibTableColumn
accIpIfFiltEditProtocol = _AccIpIfFiltEditProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 10),
    _AccIpIfFiltEditProtocol_Type()
)
accIpIfFiltEditProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpIfFiltEditProtocol.setStatus("mandatory")


class _AccIpIfFiltEditOp2_Type(Integer32):
    """Custom type accIpIfFiltEditOp2 based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("dst-equal", 6),
          ("dst-greater-than", 9),
          ("dst-less-than", 8),
          ("dst-not-equal", 7),
          ("equal", 2),
          ("greater-than", 5),
          ("less-than", 4),
          ("none", 1),
          ("not-equal", 3),
          ("src-equal", 10),
          ("src-greater-than", 13),
          ("src-less-than", 12),
          ("src-not-equal", 11))
    )


_AccIpIfFiltEditOp2_Type.__name__ = "Integer32"
_AccIpIfFiltEditOp2_Object = MibTableColumn
accIpIfFiltEditOp2 = _AccIpIfFiltEditOp2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 11),
    _AccIpIfFiltEditOp2_Type()
)
accIpIfFiltEditOp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpIfFiltEditOp2.setStatus("mandatory")


class _AccIpIfFiltEditUDPTCPPort_Type(Integer32):
    """Custom type accIpIfFiltEditUDPTCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccIpIfFiltEditUDPTCPPort_Type.__name__ = "Integer32"
_AccIpIfFiltEditUDPTCPPort_Object = MibTableColumn
accIpIfFiltEditUDPTCPPort = _AccIpIfFiltEditUDPTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 12),
    _AccIpIfFiltEditUDPTCPPort_Type()
)
accIpIfFiltEditUDPTCPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpIfFiltEditUDPTCPPort.setStatus("mandatory")


class _AccIpIfFiltEditDispos_Type(Integer32):
    """Custom type accIpIfFiltEditDispos based on Integer32"""
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
        *(("discard", 1),
          ("highPriority", 5),
          ("log", 2),
          ("lowPriority", 4),
          ("normalPriority", 3))
    )


_AccIpIfFiltEditDispos_Type.__name__ = "Integer32"
_AccIpIfFiltEditDispos_Object = MibTableColumn
accIpIfFiltEditDispos = _AccIpIfFiltEditDispos_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 13),
    _AccIpIfFiltEditDispos_Type()
)
accIpIfFiltEditDispos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpIfFiltEditDispos.setStatus("mandatory")
_AccIpNamedFiltTable_Object = MibTable
accIpNamedFiltTable = _AccIpNamedFiltTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 7)
)
if mibBuilder.loadTexts:
    accIpNamedFiltTable.setStatus("mandatory")
_AccIpNamedFiltEntry_Object = MibTableRow
accIpNamedFiltEntry = _AccIpNamedFiltEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 7, 1)
)
accIpNamedFiltEntry.setIndexNames(
    (0, "ACC-IPFILTER", "pysmiFakeCol1"),
)
if mibBuilder.loadTexts:
    accIpNamedFiltEntry.setStatus("mandatory")
_AccIpNamedFiltName_Type = OctetString
_AccIpNamedFiltName_Object = MibTableColumn
accIpNamedFiltName = _AccIpNamedFiltName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 7, 1, 1),
    _AccIpNamedFiltName_Type()
)
accIpNamedFiltName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpNamedFiltName.setStatus("mandatory")


class _AccIpNamedFiltAction_Type(Integer32):
    """Custom type accIpNamedFiltAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_AccIpNamedFiltAction_Type.__name__ = "Integer32"
_AccIpNamedFiltAction_Object = MibTableColumn
accIpNamedFiltAction = _AccIpNamedFiltAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 7, 1, 2),
    _AccIpNamedFiltAction_Type()
)
accIpNamedFiltAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpNamedFiltAction.setStatus("mandatory")


class _AccIpNamedFiltPktDir_Type(Integer32):
    """Custom type accIpNamedFiltPktDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_AccIpNamedFiltPktDir_Type.__name__ = "Integer32"
_AccIpNamedFiltPktDir_Object = MibTableColumn
accIpNamedFiltPktDir = _AccIpNamedFiltPktDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 7, 1, 3),
    _AccIpNamedFiltPktDir_Type()
)
accIpNamedFiltPktDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpNamedFiltPktDir.setStatus("mandatory")
_AccIpNamedFiltDAddr_Type = IpAddress
_AccIpNamedFiltDAddr_Object = MibTableColumn
accIpNamedFiltDAddr = _AccIpNamedFiltDAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 7, 1, 4),
    _AccIpNamedFiltDAddr_Type()
)
accIpNamedFiltDAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpNamedFiltDAddr.setStatus("mandatory")
_AccIpNamedFiltDNetMask_Type = IpAddress
_AccIpNamedFiltDNetMask_Object = MibTableColumn
accIpNamedFiltDNetMask = _AccIpNamedFiltDNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 7, 1, 5),
    _AccIpNamedFiltDNetMask_Type()
)
accIpNamedFiltDNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpNamedFiltDNetMask.setStatus("mandatory")
_AccIpNamedFiltSAddr_Type = IpAddress
_AccIpNamedFiltSAddr_Object = MibTableColumn
accIpNamedFiltSAddr = _AccIpNamedFiltSAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 7, 1, 6),
    _AccIpNamedFiltSAddr_Type()
)
accIpNamedFiltSAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpNamedFiltSAddr.setStatus("mandatory")
_AccIpNamedFiltSNetMask_Type = IpAddress
_AccIpNamedFiltSNetMask_Object = MibTableColumn
accIpNamedFiltSNetMask = _AccIpNamedFiltSNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 7, 1, 7),
    _AccIpNamedFiltSNetMask_Type()
)
accIpNamedFiltSNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpNamedFiltSNetMask.setStatus("mandatory")


class _AccIpNamedFiltOp1_Type(Integer32):
    """Custom type accIpNamedFiltOp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 3),
          ("none", 1),
          ("not-equal", 2))
    )


_AccIpNamedFiltOp1_Type.__name__ = "Integer32"
_AccIpNamedFiltOp1_Object = MibTableColumn
accIpNamedFiltOp1 = _AccIpNamedFiltOp1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 7, 1, 8),
    _AccIpNamedFiltOp1_Type()
)
accIpNamedFiltOp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpNamedFiltOp1.setStatus("mandatory")


class _AccIpNamedFiltProtocol_Type(Integer32):
    """Custom type accIpNamedFiltProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccIpNamedFiltProtocol_Type.__name__ = "Integer32"
_AccIpNamedFiltProtocol_Object = MibTableColumn
accIpNamedFiltProtocol = _AccIpNamedFiltProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 7, 1, 9),
    _AccIpNamedFiltProtocol_Type()
)
accIpNamedFiltProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpNamedFiltProtocol.setStatus("mandatory")


class _AccIpNamedFiltOp2_Type(Integer32):
    """Custom type accIpNamedFiltOp2 based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("dst-equal", 13),
          ("dst-greater-than", 12),
          ("dst-less-than", 11),
          ("dst-not-equal", 10),
          ("equal", 5),
          ("greater-than", 4),
          ("less-than", 3),
          ("none", 1),
          ("not-equal", 2),
          ("src-equal", 9),
          ("src-greater-than", 8),
          ("src-less-than", 7),
          ("src-not-equal", 6))
    )


_AccIpNamedFiltOp2_Type.__name__ = "Integer32"
_AccIpNamedFiltOp2_Object = MibTableColumn
accIpNamedFiltOp2 = _AccIpNamedFiltOp2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 7, 1, 10),
    _AccIpNamedFiltOp2_Type()
)
accIpNamedFiltOp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpNamedFiltOp2.setStatus("mandatory")


class _AccIpNamedFiltUDPTCPPort_Type(Integer32):
    """Custom type accIpNamedFiltUDPTCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccIpNamedFiltUDPTCPPort_Type.__name__ = "Integer32"
_AccIpNamedFiltUDPTCPPort_Object = MibTableColumn
accIpNamedFiltUDPTCPPort = _AccIpNamedFiltUDPTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 7, 1, 11),
    _AccIpNamedFiltUDPTCPPort_Type()
)
accIpNamedFiltUDPTCPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpNamedFiltUDPTCPPort.setStatus("mandatory")


class _AccIpNamedFiltDisp_Type(Integer32):
    """Custom type accIpNamedFiltDisp based on Integer32"""
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
        *(("discard", 1),
          ("highPriority", 5),
          ("log", 2),
          ("lowPriority", 4),
          ("normalPriority", 3))
    )


_AccIpNamedFiltDisp_Type.__name__ = "Integer32"
_AccIpNamedFiltDisp_Object = MibTableColumn
accIpNamedFiltDisp = _AccIpNamedFiltDisp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 7, 1, 12),
    _AccIpNamedFiltDisp_Type()
)
accIpNamedFiltDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpNamedFiltDisp.setStatus("mandatory")
_AccIpNamedFiltMatches_Type = Counter32
_AccIpNamedFiltMatches_Object = MibTableColumn
accIpNamedFiltMatches = _AccIpNamedFiltMatches_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 7, 1, 13),
    _AccIpNamedFiltMatches_Type()
)
accIpNamedFiltMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpNamedFiltMatches.setStatus("mandatory")
_AccIpNamedFiltLastMatch_Type = TimeTicks
_AccIpNamedFiltLastMatch_Object = MibTableColumn
accIpNamedFiltLastMatch = _AccIpNamedFiltLastMatch_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 7, 1, 14),
    _AccIpNamedFiltLastMatch_Type()
)
accIpNamedFiltLastMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpNamedFiltLastMatch.setStatus("mandatory")
_AccIpNamedFiltApplId_Type = Integer32
_AccIpNamedFiltApplId_Object = MibTableColumn
accIpNamedFiltApplId = _AccIpNamedFiltApplId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 7, 1, 15),
    _AccIpNamedFiltApplId_Type()
)
accIpNamedFiltApplId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpNamedFiltApplId.setStatus("mandatory")
_AccIpNamedFiltSAIndex_Type = OctetString
_AccIpNamedFiltSAIndex_Object = MibTableColumn
accIpNamedFiltSAIndex = _AccIpNamedFiltSAIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 7, 1, 16),
    _AccIpNamedFiltSAIndex_Type()
)
accIpNamedFiltSAIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpNamedFiltSAIndex.setStatus("mandatory")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 7, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")
_AccIpFiltApplTable_Object = MibTable
accIpFiltApplTable = _AccIpFiltApplTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 8)
)
if mibBuilder.loadTexts:
    accIpFiltApplTable.setStatus("mandatory")
_AccIpFiltApplEntry_Object = MibTableRow
accIpFiltApplEntry = _AccIpFiltApplEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 8, 1)
)
accIpFiltApplEntry.setIndexNames(
    (0, "ACC-IPFILTER", "accIpFiltApplIfIndex"),
    (0, "ACC-IPFILTER", "accIpFiltApplPktDir"),
    (0, "ACC-IPFILTER", "accIpFiltApplSeqNum"),
)
if mibBuilder.loadTexts:
    accIpFiltApplEntry.setStatus("mandatory")
_AccIpFiltApplIfIndex_Type = Integer32
_AccIpFiltApplIfIndex_Object = MibTableColumn
accIpFiltApplIfIndex = _AccIpFiltApplIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 8, 1, 1),
    _AccIpFiltApplIfIndex_Type()
)
accIpFiltApplIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpFiltApplIfIndex.setStatus("mandatory")


class _AccIpFiltApplPktDir_Type(Integer32):
    """Custom type accIpFiltApplPktDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("global", 3),
          ("input", 1),
          ("output", 2))
    )


_AccIpFiltApplPktDir_Type.__name__ = "Integer32"
_AccIpFiltApplPktDir_Object = MibTableColumn
accIpFiltApplPktDir = _AccIpFiltApplPktDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 8, 1, 2),
    _AccIpFiltApplPktDir_Type()
)
accIpFiltApplPktDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpFiltApplPktDir.setStatus("mandatory")
_AccIpFiltApplSeqNum_Type = Integer32
_AccIpFiltApplSeqNum_Object = MibTableColumn
accIpFiltApplSeqNum = _AccIpFiltApplSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 8, 1, 3),
    _AccIpFiltApplSeqNum_Type()
)
accIpFiltApplSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpFiltApplSeqNum.setStatus("mandatory")
_AccIpFiltApplName_Type = DisplayString
_AccIpFiltApplName_Object = MibTableColumn
accIpFiltApplName = _AccIpFiltApplName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 8, 1, 4),
    _AccIpFiltApplName_Type()
)
accIpFiltApplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpFiltApplName.setStatus("mandatory")
_AccIpFiltApplMatches_Type = Counter32
_AccIpFiltApplMatches_Object = MibTableColumn
accIpFiltApplMatches = _AccIpFiltApplMatches_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 8, 1, 5),
    _AccIpFiltApplMatches_Type()
)
accIpFiltApplMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpFiltApplMatches.setStatus("mandatory")
_AccIpFiltApplLastMatch_Type = TimeTicks
_AccIpFiltApplLastMatch_Object = MibTableColumn
accIpFiltApplLastMatch = _AccIpFiltApplLastMatch_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 8, 1, 6),
    _AccIpFiltApplLastMatch_Type()
)
accIpFiltApplLastMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpFiltApplLastMatch.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-IPFILTER",
    **{"accIpFilter": accIpFilter,
       "accIpSrcRouting": accIpSrcRouting,
       "accIpFiltTable": accIpFiltTable,
       "accIpFiltEntry": accIpFiltEntry,
       "accIpFiltDAddr": accIpFiltDAddr,
       "accIpFiltDNetMask": accIpFiltDNetMask,
       "accIpFiltSAddr": accIpFiltSAddr,
       "accIpFiltSNetMask": accIpFiltSNetMask,
       "accIpFiltParm": accIpFiltParm,
       "accIpFiltDisp": accIpFiltDisp,
       "accIpSmdsAtTable": accIpSmdsAtTable,
       "accIpSmdsAtEntry": accIpSmdsAtEntry,
       "accIpSmdsAtIpAddr": accIpSmdsAtIpAddr,
       "accIpSmdsAtSmdsAddr": accIpSmdsAtSmdsAddr,
       "accIpSmdsAtIpMcast": accIpSmdsAtIpMcast,
       "accIpSmdsAtArpMcast": accIpSmdsAtArpMcast,
       "accIpSubDirBcast": accIpSubDirBcast,
       "accIpIfFiltDispTable": accIpIfFiltDispTable,
       "accIpIfFiltDispEntry": accIpIfFiltDispEntry,
       "accIpIfFiltDispIfIndex": accIpIfFiltDispIfIndex,
       "accIpIfFiltDispPktDir": accIpIfFiltDispPktDir,
       "accIpIfFiltDispSeqNum": accIpIfFiltDispSeqNum,
       "accIpIfFiltDispDAddr": accIpIfFiltDispDAddr,
       "accIpIfFiltDispDNetMask": accIpIfFiltDispDNetMask,
       "accIpIfFiltDispSAddr": accIpIfFiltDispSAddr,
       "accIpIfFiltDispSNetMask": accIpIfFiltDispSNetMask,
       "accIpIfFiltDispOp1": accIpIfFiltDispOp1,
       "accIpIfFiltDispProtocol": accIpIfFiltDispProtocol,
       "accIpIfFiltDispOp2": accIpIfFiltDispOp2,
       "accIpIfFiltDispUDPTCPPort": accIpIfFiltDispUDPTCPPort,
       "accIpIfFiltDispDispos": accIpIfFiltDispDispos,
       "accIpIfFiltDispMatches": accIpIfFiltDispMatches,
       "accIpIfFiltDispLastMatchTime": accIpIfFiltDispLastMatchTime,
       "accIpIfFiltDispMatchPkt": accIpIfFiltDispMatchPkt,
       "accIpIfFiltEditTable": accIpIfFiltEditTable,
       "accIpIfFiltEditEntry": accIpIfFiltEditEntry,
       "accIpIfFiltEditIndex": accIpIfFiltEditIndex,
       "accIpIfFiltEditAction": accIpIfFiltEditAction,
       "accIpIfFiltEditIfIndex": accIpIfFiltEditIfIndex,
       "accIpIfFiltEditPktDir": accIpIfFiltEditPktDir,
       "accIpIfFiltEditDAddr": accIpIfFiltEditDAddr,
       "accIpIfFiltEditDNetMask": accIpIfFiltEditDNetMask,
       "accIpIfFiltEditSAddr": accIpIfFiltEditSAddr,
       "accIpIfFiltEditSNetMask": accIpIfFiltEditSNetMask,
       "accIpIfFiltEditOp1": accIpIfFiltEditOp1,
       "accIpIfFiltEditProtocol": accIpIfFiltEditProtocol,
       "accIpIfFiltEditOp2": accIpIfFiltEditOp2,
       "accIpIfFiltEditUDPTCPPort": accIpIfFiltEditUDPTCPPort,
       "accIpIfFiltEditDispos": accIpIfFiltEditDispos,
       "accIpNamedFiltTable": accIpNamedFiltTable,
       "accIpNamedFiltEntry": accIpNamedFiltEntry,
       "accIpNamedFiltName": accIpNamedFiltName,
       "accIpNamedFiltAction": accIpNamedFiltAction,
       "accIpNamedFiltPktDir": accIpNamedFiltPktDir,
       "accIpNamedFiltDAddr": accIpNamedFiltDAddr,
       "accIpNamedFiltDNetMask": accIpNamedFiltDNetMask,
       "accIpNamedFiltSAddr": accIpNamedFiltSAddr,
       "accIpNamedFiltSNetMask": accIpNamedFiltSNetMask,
       "accIpNamedFiltOp1": accIpNamedFiltOp1,
       "accIpNamedFiltProtocol": accIpNamedFiltProtocol,
       "accIpNamedFiltOp2": accIpNamedFiltOp2,
       "accIpNamedFiltUDPTCPPort": accIpNamedFiltUDPTCPPort,
       "accIpNamedFiltDisp": accIpNamedFiltDisp,
       "accIpNamedFiltMatches": accIpNamedFiltMatches,
       "accIpNamedFiltLastMatch": accIpNamedFiltLastMatch,
       "accIpNamedFiltApplId": accIpNamedFiltApplId,
       "accIpNamedFiltSAIndex": accIpNamedFiltSAIndex,
       "pysmiFakeCol1": pysmiFakeCol1,
       "accIpFiltApplTable": accIpFiltApplTable,
       "accIpFiltApplEntry": accIpFiltApplEntry,
       "accIpFiltApplIfIndex": accIpFiltApplIfIndex,
       "accIpFiltApplPktDir": accIpFiltApplPktDir,
       "accIpFiltApplSeqNum": accIpFiltApplSeqNum,
       "accIpFiltApplName": accIpFiltApplName,
       "accIpFiltApplMatches": accIpFiltApplMatches,
       "accIpFiltApplLastMatch": accIpFiltApplLastMatch}
)
