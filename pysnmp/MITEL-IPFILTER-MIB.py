# SNMP MIB module (MITEL-IPFILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MITEL-IPFILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:18 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

mitelIpGrpFilterGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1)
)
mitelIpGrpFilterGroup.setRevisions(
        ("2003-03-24 09:25",
         "1999-03-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mitel_ObjectIdentity = ObjectIdentity
mitel = _Mitel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027)
)
_MitelIdentification_ObjectIdentity = ObjectIdentity
mitelIdentification = _MitelIdentification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1)
)
_MitelIdCallServers_ObjectIdentity = ObjectIdentity
mitelIdCallServers = _MitelIdCallServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2)
)
_MitelIdCsIpera1000_ObjectIdentity = ObjectIdentity
mitelIdCsIpera1000 = _MitelIdCsIpera1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 4)
)
_MitelProprietary_ObjectIdentity = ObjectIdentity
mitelProprietary = _MitelProprietary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4)
)
_MitelPropIpNetworking_ObjectIdentity = ObjectIdentity
mitelPropIpNetworking = _MitelPropIpNetworking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8)
)
_MitelIpNetRouter_ObjectIdentity = ObjectIdentity
mitelIpNetRouter = _MitelIpNetRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1)
)
_MitelRouterIpGroup_ObjectIdentity = ObjectIdentity
mitelRouterIpGroup = _MitelRouterIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1)
)


class _MitelFltGrpAccessRestrictEnable_Type(Integer32):
    """Custom type mitelFltGrpAccessRestrictEnable based on Integer32"""
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


_MitelFltGrpAccessRestrictEnable_Type.__name__ = "Integer32"
_MitelFltGrpAccessRestrictEnable_Object = MibScalar
mitelFltGrpAccessRestrictEnable = _MitelFltGrpAccessRestrictEnable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 1),
    _MitelFltGrpAccessRestrictEnable_Type()
)
mitelFltGrpAccessRestrictEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelFltGrpAccessRestrictEnable.setStatus("current")
_MitelFltGrpLogicalTable_Object = MibTable
mitelFltGrpLogicalTable = _MitelFltGrpLogicalTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mitelFltGrpLogicalTable.setStatus("current")
_MitelFltGrpLogicalEntry_Object = MibTableRow
mitelFltGrpLogicalEntry = _MitelFltGrpLogicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 2, 1)
)
mitelFltGrpLogicalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mitelFltGrpLogicalEntry.setStatus("current")


class _MitelLogTableAccessDef_Type(Integer32):
    """Custom type mitelLogTableAccessDef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("forward", 2))
    )


_MitelLogTableAccessDef_Type.__name__ = "Integer32"
_MitelLogTableAccessDef_Object = MibTableColumn
mitelLogTableAccessDef = _MitelLogTableAccessDef_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 2, 1, 1),
    _MitelLogTableAccessDef_Type()
)
mitelLogTableAccessDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelLogTableAccessDef.setStatus("current")


class _MitelLogTableAllowSrcRouting_Type(Integer32):
    """Custom type mitelLogTableAllowSrcRouting based on Integer32"""
    defaultValue = 2

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


_MitelLogTableAllowSrcRouting_Type.__name__ = "Integer32"
_MitelLogTableAllowSrcRouting_Object = MibTableColumn
mitelLogTableAllowSrcRouting = _MitelLogTableAllowSrcRouting_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 2, 1, 2),
    _MitelLogTableAllowSrcRouting_Type()
)
mitelLogTableAllowSrcRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelLogTableAllowSrcRouting.setStatus("current")
_MitelFltGrpAccessRestrictTable_Object = MibTable
mitelFltGrpAccessRestrictTable = _MitelFltGrpAccessRestrictTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mitelFltGrpAccessRestrictTable.setStatus("current")
_MitelFltGrpAccessRestrictEntry_Object = MibTableRow
mitelFltGrpAccessRestrictEntry = _MitelFltGrpAccessRestrictEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1)
)
mitelFltGrpAccessRestrictEntry.setIndexNames(
    (0, "MITEL-IPFILTER-MIB", "mitelAccResTableIfIndex"),
    (0, "MITEL-IPFILTER-MIB", "mitelAccResTableOrder"),
)
if mibBuilder.loadTexts:
    mitelFltGrpAccessRestrictEntry.setStatus("current")
_MitelAccResTableIfIndex_Type = Integer32
_MitelAccResTableIfIndex_Object = MibTableColumn
mitelAccResTableIfIndex = _MitelAccResTableIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 1),
    _MitelAccResTableIfIndex_Type()
)
mitelAccResTableIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelAccResTableIfIndex.setStatus("current")
_MitelAccResTableOrder_Type = Integer32
_MitelAccResTableOrder_Object = MibTableColumn
mitelAccResTableOrder = _MitelAccResTableOrder_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 2),
    _MitelAccResTableOrder_Type()
)
mitelAccResTableOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelAccResTableOrder.setStatus("current")


class _MitelAccResTableType_Type(Integer32):
    """Custom type mitelAccResTableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("forward", 2),
          ("neither", 3))
    )


_MitelAccResTableType_Type.__name__ = "Integer32"
_MitelAccResTableType_Object = MibTableColumn
mitelAccResTableType = _MitelAccResTableType_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 3),
    _MitelAccResTableType_Type()
)
mitelAccResTableType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelAccResTableType.setStatus("current")
_MitelAccResTableSrcAddrFrom_Type = IpAddress
_MitelAccResTableSrcAddrFrom_Object = MibTableColumn
mitelAccResTableSrcAddrFrom = _MitelAccResTableSrcAddrFrom_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 4),
    _MitelAccResTableSrcAddrFrom_Type()
)
mitelAccResTableSrcAddrFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelAccResTableSrcAddrFrom.setStatus("current")
_MitelAccResTableSrcAddrTo_Type = IpAddress
_MitelAccResTableSrcAddrTo_Object = MibTableColumn
mitelAccResTableSrcAddrTo = _MitelAccResTableSrcAddrTo_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 5),
    _MitelAccResTableSrcAddrTo_Type()
)
mitelAccResTableSrcAddrTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelAccResTableSrcAddrTo.setStatus("current")


class _MitelAccResTableSrcAddrOutsideRange_Type(Integer32):
    """Custom type mitelAccResTableSrcAddrOutsideRange based on Integer32"""
    defaultValue = 2

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


_MitelAccResTableSrcAddrOutsideRange_Type.__name__ = "Integer32"
_MitelAccResTableSrcAddrOutsideRange_Object = MibTableColumn
mitelAccResTableSrcAddrOutsideRange = _MitelAccResTableSrcAddrOutsideRange_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 6),
    _MitelAccResTableSrcAddrOutsideRange_Type()
)
mitelAccResTableSrcAddrOutsideRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelAccResTableSrcAddrOutsideRange.setStatus("current")
_MitelAccResTableDstAddrFrom_Type = IpAddress
_MitelAccResTableDstAddrFrom_Object = MibTableColumn
mitelAccResTableDstAddrFrom = _MitelAccResTableDstAddrFrom_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 7),
    _MitelAccResTableDstAddrFrom_Type()
)
mitelAccResTableDstAddrFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelAccResTableDstAddrFrom.setStatus("current")
_MitelAccResTableDstAddrTo_Type = IpAddress
_MitelAccResTableDstAddrTo_Object = MibTableColumn
mitelAccResTableDstAddrTo = _MitelAccResTableDstAddrTo_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 8),
    _MitelAccResTableDstAddrTo_Type()
)
mitelAccResTableDstAddrTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelAccResTableDstAddrTo.setStatus("current")


class _MitelAccResTableDstAddrOutsideRange_Type(Integer32):
    """Custom type mitelAccResTableDstAddrOutsideRange based on Integer32"""
    defaultValue = 2

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


_MitelAccResTableDstAddrOutsideRange_Type.__name__ = "Integer32"
_MitelAccResTableDstAddrOutsideRange_Object = MibTableColumn
mitelAccResTableDstAddrOutsideRange = _MitelAccResTableDstAddrOutsideRange_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 9),
    _MitelAccResTableDstAddrOutsideRange_Type()
)
mitelAccResTableDstAddrOutsideRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelAccResTableDstAddrOutsideRange.setStatus("current")


class _MitelAccResTableProtocolFrom_Type(Integer32):
    """Custom type mitelAccResTableProtocolFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MitelAccResTableProtocolFrom_Type.__name__ = "Integer32"
_MitelAccResTableProtocolFrom_Object = MibTableColumn
mitelAccResTableProtocolFrom = _MitelAccResTableProtocolFrom_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 10),
    _MitelAccResTableProtocolFrom_Type()
)
mitelAccResTableProtocolFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelAccResTableProtocolFrom.setStatus("current")


class _MitelAccResTableProtocolTo_Type(Integer32):
    """Custom type mitelAccResTableProtocolTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MitelAccResTableProtocolTo_Type.__name__ = "Integer32"
_MitelAccResTableProtocolTo_Object = MibTableColumn
mitelAccResTableProtocolTo = _MitelAccResTableProtocolTo_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 11),
    _MitelAccResTableProtocolTo_Type()
)
mitelAccResTableProtocolTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelAccResTableProtocolTo.setStatus("current")


class _MitelAccResTableProtocolOutsideRange_Type(Integer32):
    """Custom type mitelAccResTableProtocolOutsideRange based on Integer32"""
    defaultValue = 2

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


_MitelAccResTableProtocolOutsideRange_Type.__name__ = "Integer32"
_MitelAccResTableProtocolOutsideRange_Object = MibTableColumn
mitelAccResTableProtocolOutsideRange = _MitelAccResTableProtocolOutsideRange_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 12),
    _MitelAccResTableProtocolOutsideRange_Type()
)
mitelAccResTableProtocolOutsideRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelAccResTableProtocolOutsideRange.setStatus("current")


class _MitelAccResTableSrcPortFrom_Type(Integer32):
    """Custom type mitelAccResTableSrcPortFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MitelAccResTableSrcPortFrom_Type.__name__ = "Integer32"
_MitelAccResTableSrcPortFrom_Object = MibTableColumn
mitelAccResTableSrcPortFrom = _MitelAccResTableSrcPortFrom_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 13),
    _MitelAccResTableSrcPortFrom_Type()
)
mitelAccResTableSrcPortFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelAccResTableSrcPortFrom.setStatus("current")


class _MitelAccResTableSrcPortTo_Type(Integer32):
    """Custom type mitelAccResTableSrcPortTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MitelAccResTableSrcPortTo_Type.__name__ = "Integer32"
_MitelAccResTableSrcPortTo_Object = MibTableColumn
mitelAccResTableSrcPortTo = _MitelAccResTableSrcPortTo_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 14),
    _MitelAccResTableSrcPortTo_Type()
)
mitelAccResTableSrcPortTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelAccResTableSrcPortTo.setStatus("current")


class _MitelAccResTableSrcPortOutsideRange_Type(Integer32):
    """Custom type mitelAccResTableSrcPortOutsideRange based on Integer32"""
    defaultValue = 2

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


_MitelAccResTableSrcPortOutsideRange_Type.__name__ = "Integer32"
_MitelAccResTableSrcPortOutsideRange_Object = MibTableColumn
mitelAccResTableSrcPortOutsideRange = _MitelAccResTableSrcPortOutsideRange_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 15),
    _MitelAccResTableSrcPortOutsideRange_Type()
)
mitelAccResTableSrcPortOutsideRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelAccResTableSrcPortOutsideRange.setStatus("current")


class _MitelAccResTableDstPortFrom_Type(Integer32):
    """Custom type mitelAccResTableDstPortFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MitelAccResTableDstPortFrom_Type.__name__ = "Integer32"
_MitelAccResTableDstPortFrom_Object = MibTableColumn
mitelAccResTableDstPortFrom = _MitelAccResTableDstPortFrom_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 16),
    _MitelAccResTableDstPortFrom_Type()
)
mitelAccResTableDstPortFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelAccResTableDstPortFrom.setStatus("current")


class _MitelAccResTableDstPortTo_Type(Integer32):
    """Custom type mitelAccResTableDstPortTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MitelAccResTableDstPortTo_Type.__name__ = "Integer32"
_MitelAccResTableDstPortTo_Object = MibTableColumn
mitelAccResTableDstPortTo = _MitelAccResTableDstPortTo_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 17),
    _MitelAccResTableDstPortTo_Type()
)
mitelAccResTableDstPortTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelAccResTableDstPortTo.setStatus("current")


class _MitelAccResTableDstPortOutsideRange_Type(Integer32):
    """Custom type mitelAccResTableDstPortOutsideRange based on Integer32"""
    defaultValue = 2

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


_MitelAccResTableDstPortOutsideRange_Type.__name__ = "Integer32"
_MitelAccResTableDstPortOutsideRange_Object = MibTableColumn
mitelAccResTableDstPortOutsideRange = _MitelAccResTableDstPortOutsideRange_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 18),
    _MitelAccResTableDstPortOutsideRange_Type()
)
mitelAccResTableDstPortOutsideRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelAccResTableDstPortOutsideRange.setStatus("current")


class _MitelAccResTableTcpSyn_Type(Integer32):
    """Custom type mitelAccResTableTcpSyn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("one", 3),
          ("zero", 2))
    )


_MitelAccResTableTcpSyn_Type.__name__ = "Integer32"
_MitelAccResTableTcpSyn_Object = MibTableColumn
mitelAccResTableTcpSyn = _MitelAccResTableTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 19),
    _MitelAccResTableTcpSyn_Type()
)
mitelAccResTableTcpSyn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelAccResTableTcpSyn.setStatus("current")


class _MitelAccResTableTcpAck_Type(Integer32):
    """Custom type mitelAccResTableTcpAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("one", 3),
          ("zero", 2))
    )


_MitelAccResTableTcpAck_Type.__name__ = "Integer32"
_MitelAccResTableTcpAck_Object = MibTableColumn
mitelAccResTableTcpAck = _MitelAccResTableTcpAck_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 20),
    _MitelAccResTableTcpAck_Type()
)
mitelAccResTableTcpAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelAccResTableTcpAck.setStatus("current")


class _MitelAccResTableTcpFin_Type(Integer32):
    """Custom type mitelAccResTableTcpFin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("one", 3),
          ("zero", 2))
    )


_MitelAccResTableTcpFin_Type.__name__ = "Integer32"
_MitelAccResTableTcpFin_Object = MibTableColumn
mitelAccResTableTcpFin = _MitelAccResTableTcpFin_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 21),
    _MitelAccResTableTcpFin_Type()
)
mitelAccResTableTcpFin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelAccResTableTcpFin.setStatus("current")


class _MitelAccResTableTcpRst_Type(Integer32):
    """Custom type mitelAccResTableTcpRst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("one", 3),
          ("zero", 2))
    )


_MitelAccResTableTcpRst_Type.__name__ = "Integer32"
_MitelAccResTableTcpRst_Object = MibTableColumn
mitelAccResTableTcpRst = _MitelAccResTableTcpRst_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 22),
    _MitelAccResTableTcpRst_Type()
)
mitelAccResTableTcpRst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelAccResTableTcpRst.setStatus("current")


class _MitelAccResTableMatchIn_Type(Integer32):
    """Custom type mitelAccResTableMatchIn based on Integer32"""
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


_MitelAccResTableMatchIn_Type.__name__ = "Integer32"
_MitelAccResTableMatchIn_Object = MibTableColumn
mitelAccResTableMatchIn = _MitelAccResTableMatchIn_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 23),
    _MitelAccResTableMatchIn_Type()
)
mitelAccResTableMatchIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelAccResTableMatchIn.setStatus("current")


class _MitelAccResTableMatchOut_Type(Integer32):
    """Custom type mitelAccResTableMatchOut based on Integer32"""
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


_MitelAccResTableMatchOut_Type.__name__ = "Integer32"
_MitelAccResTableMatchOut_Object = MibTableColumn
mitelAccResTableMatchOut = _MitelAccResTableMatchOut_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 24),
    _MitelAccResTableMatchOut_Type()
)
mitelAccResTableMatchOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelAccResTableMatchOut.setStatus("current")


class _MitelAccResTableLog_Type(Integer32):
    """Custom type mitelAccResTableLog based on Integer32"""
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


_MitelAccResTableLog_Type.__name__ = "Integer32"
_MitelAccResTableLog_Object = MibTableColumn
mitelAccResTableLog = _MitelAccResTableLog_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 25),
    _MitelAccResTableLog_Type()
)
mitelAccResTableLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelAccResTableLog.setStatus("current")


class _MitelAccResTableTrap_Type(Integer32):
    """Custom type mitelAccResTableTrap based on Integer32"""
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


_MitelAccResTableTrap_Type.__name__ = "Integer32"
_MitelAccResTableTrap_Object = MibTableColumn
mitelAccResTableTrap = _MitelAccResTableTrap_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 26),
    _MitelAccResTableTrap_Type()
)
mitelAccResTableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelAccResTableTrap.setStatus("current")
_MitelAccResTableStatus_Type = RowStatus
_MitelAccResTableStatus_Object = MibTableColumn
mitelAccResTableStatus = _MitelAccResTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 27),
    _MitelAccResTableStatus_Type()
)
mitelAccResTableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mitelAccResTableStatus.setStatus("current")
_MitelAccResTableCount_Type = Integer32
_MitelAccResTableCount_Object = MibTableColumn
mitelAccResTableCount = _MitelAccResTableCount_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 28),
    _MitelAccResTableCount_Type()
)
mitelAccResTableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelAccResTableCount.setStatus("current")

# Managed Objects groups


# Notification objects

mitelAccResTableTrapped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0, 402)
)
mitelAccResTableTrapped.setObjects(
      *(("MITEL-IPFILTER-MIB", "mitelAccResTableIfIndex"),
        ("MITEL-IPFILTER-MIB", "mitelAccResTableOrder"))
)
if mibBuilder.loadTexts:
    mitelAccResTableTrapped.setStatus(
        "current"
    )


# Notifications groups

mitelIpera1000Notifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0)
)
mitelIpera1000Notifications.setObjects(
    ("MITEL-IPFILTER-MIB", "mitelAccResTableTrapped")
)
if mibBuilder.loadTexts:
    mitelIpera1000Notifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-IPFILTER-MIB",
    **{"mitel": mitel,
       "mitelIdentification": mitelIdentification,
       "mitelIdCallServers": mitelIdCallServers,
       "mitelIdCsIpera1000": mitelIdCsIpera1000,
       "mitelIpera1000Notifications": mitelIpera1000Notifications,
       "mitelAccResTableTrapped": mitelAccResTableTrapped,
       "mitelProprietary": mitelProprietary,
       "mitelPropIpNetworking": mitelPropIpNetworking,
       "mitelIpNetRouter": mitelIpNetRouter,
       "mitelRouterIpGroup": mitelRouterIpGroup,
       "mitelIpGrpFilterGroup": mitelIpGrpFilterGroup,
       "mitelFltGrpAccessRestrictEnable": mitelFltGrpAccessRestrictEnable,
       "mitelFltGrpLogicalTable": mitelFltGrpLogicalTable,
       "mitelFltGrpLogicalEntry": mitelFltGrpLogicalEntry,
       "mitelLogTableAccessDef": mitelLogTableAccessDef,
       "mitelLogTableAllowSrcRouting": mitelLogTableAllowSrcRouting,
       "mitelFltGrpAccessRestrictTable": mitelFltGrpAccessRestrictTable,
       "mitelFltGrpAccessRestrictEntry": mitelFltGrpAccessRestrictEntry,
       "mitelAccResTableIfIndex": mitelAccResTableIfIndex,
       "mitelAccResTableOrder": mitelAccResTableOrder,
       "mitelAccResTableType": mitelAccResTableType,
       "mitelAccResTableSrcAddrFrom": mitelAccResTableSrcAddrFrom,
       "mitelAccResTableSrcAddrTo": mitelAccResTableSrcAddrTo,
       "mitelAccResTableSrcAddrOutsideRange": mitelAccResTableSrcAddrOutsideRange,
       "mitelAccResTableDstAddrFrom": mitelAccResTableDstAddrFrom,
       "mitelAccResTableDstAddrTo": mitelAccResTableDstAddrTo,
       "mitelAccResTableDstAddrOutsideRange": mitelAccResTableDstAddrOutsideRange,
       "mitelAccResTableProtocolFrom": mitelAccResTableProtocolFrom,
       "mitelAccResTableProtocolTo": mitelAccResTableProtocolTo,
       "mitelAccResTableProtocolOutsideRange": mitelAccResTableProtocolOutsideRange,
       "mitelAccResTableSrcPortFrom": mitelAccResTableSrcPortFrom,
       "mitelAccResTableSrcPortTo": mitelAccResTableSrcPortTo,
       "mitelAccResTableSrcPortOutsideRange": mitelAccResTableSrcPortOutsideRange,
       "mitelAccResTableDstPortFrom": mitelAccResTableDstPortFrom,
       "mitelAccResTableDstPortTo": mitelAccResTableDstPortTo,
       "mitelAccResTableDstPortOutsideRange": mitelAccResTableDstPortOutsideRange,
       "mitelAccResTableTcpSyn": mitelAccResTableTcpSyn,
       "mitelAccResTableTcpAck": mitelAccResTableTcpAck,
       "mitelAccResTableTcpFin": mitelAccResTableTcpFin,
       "mitelAccResTableTcpRst": mitelAccResTableTcpRst,
       "mitelAccResTableMatchIn": mitelAccResTableMatchIn,
       "mitelAccResTableMatchOut": mitelAccResTableMatchOut,
       "mitelAccResTableLog": mitelAccResTableLog,
       "mitelAccResTableTrap": mitelAccResTableTrap,
       "mitelAccResTableStatus": mitelAccResTableStatus,
       "mitelAccResTableCount": mitelAccResTableCount}
)
