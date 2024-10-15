# SNMP MIB module (H3C-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-ACL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:52 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cAcl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RuleAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deny", 3),
          ("invalid", 1),
          ("permit", 2))
    )



class CounterClear(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("nouse", 2))
    )



class PortOp(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eq", 2),
          ("gt", 3),
          ("invalid", 0),
          ("lt", 1),
          ("neq", 4),
          ("range", 5))
    )



class DSCPValue(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )



class TCPFlag(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("tcpack", 1),
          ("tcpfin", 2),
          ("tcppsh", 3),
          ("tcprst", 4),
          ("tcpsyn", 5),
          ("tcpurg", 6))
    )



class FragmentFlag(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fragment", 1),
          ("fragmentSubseq", 2),
          ("invalid", 0),
          ("nonFragment", 3),
          ("nonSubseq", 4))
    )



class AddressFlag(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("t128DestinationAddress", 6),
          ("t128SourceAddress", 5),
          ("t64SrcAddrPre64DestAddrPre", 1),
          ("t64SrcAddrPre64DestAddrSuf", 2),
          ("t64SrcAddrSuf64DestAddrPre", 3),
          ("t64SrcAddrSuf64DestAddrSuf", 4))
    )



class DirectionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )



# MIB Managed Objects in the order of their OIDs

_H3cAclMibObjects_ObjectIdentity = ObjectIdentity
h3cAclMibObjects = _H3cAclMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1)
)


class _H3cAclMode_Type(Integer32):
    """Custom type h3cAclMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipBased", 2),
          ("linkBased", 1))
    )


_H3cAclMode_Type.__name__ = "Integer32"
_H3cAclMode_Object = MibScalar
h3cAclMode = _H3cAclMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 1),
    _H3cAclMode_Type()
)
h3cAclMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cAclMode.setStatus("current")
_H3cAclNumGroupTable_Object = MibTable
h3cAclNumGroupTable = _H3cAclNumGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 2)
)
if mibBuilder.loadTexts:
    h3cAclNumGroupTable.setStatus("current")
_H3cAclNumGroupEntry_Object = MibTableRow
h3cAclNumGroupEntry = _H3cAclNumGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 2, 1)
)
h3cAclNumGroupEntry.setIndexNames(
    (0, "H3C-ACL-MIB", "h3cAclNumGroupAclNum"),
)
if mibBuilder.loadTexts:
    h3cAclNumGroupEntry.setStatus("current")


class _H3cAclNumGroupAclNum_Type(Integer32):
    """Custom type h3cAclNumGroupAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 5999),
    )


_H3cAclNumGroupAclNum_Type.__name__ = "Integer32"
_H3cAclNumGroupAclNum_Object = MibTableColumn
h3cAclNumGroupAclNum = _H3cAclNumGroupAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 2, 1, 1),
    _H3cAclNumGroupAclNum_Type()
)
h3cAclNumGroupAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclNumGroupAclNum.setStatus("current")


class _H3cAclNumGroupMatchOrder_Type(Integer32):
    """Custom type h3cAclNumGroupMatchOrder based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("config", 1))
    )


_H3cAclNumGroupMatchOrder_Type.__name__ = "Integer32"
_H3cAclNumGroupMatchOrder_Object = MibTableColumn
h3cAclNumGroupMatchOrder = _H3cAclNumGroupMatchOrder_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 2, 1, 2),
    _H3cAclNumGroupMatchOrder_Type()
)
h3cAclNumGroupMatchOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclNumGroupMatchOrder.setStatus("current")
_H3cAclNumGroupSubitemNum_Type = Integer32
_H3cAclNumGroupSubitemNum_Object = MibTableColumn
h3cAclNumGroupSubitemNum = _H3cAclNumGroupSubitemNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 2, 1, 3),
    _H3cAclNumGroupSubitemNum_Type()
)
h3cAclNumGroupSubitemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclNumGroupSubitemNum.setStatus("current")


class _H3cAclNumGroupDescription_Type(OctetString):
    """Custom type h3cAclNumGroupDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cAclNumGroupDescription_Type.__name__ = "OctetString"
_H3cAclNumGroupDescription_Object = MibTableColumn
h3cAclNumGroupDescription = _H3cAclNumGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 2, 1, 4),
    _H3cAclNumGroupDescription_Type()
)
h3cAclNumGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cAclNumGroupDescription.setStatus("current")


class _H3cAclNumGroupCountClear_Type(Integer32):
    """Custom type h3cAclNumGroupCountClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("nouse", 2))
    )


_H3cAclNumGroupCountClear_Type.__name__ = "Integer32"
_H3cAclNumGroupCountClear_Object = MibTableColumn
h3cAclNumGroupCountClear = _H3cAclNumGroupCountClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 2, 1, 5),
    _H3cAclNumGroupCountClear_Type()
)
h3cAclNumGroupCountClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclNumGroupCountClear.setStatus("current")
_H3cAclNumGroupRowStatus_Type = RowStatus
_H3cAclNumGroupRowStatus_Object = MibTableColumn
h3cAclNumGroupRowStatus = _H3cAclNumGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 2, 1, 6),
    _H3cAclNumGroupRowStatus_Type()
)
h3cAclNumGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclNumGroupRowStatus.setStatus("current")
_H3cAclNameGroupTable_Object = MibTable
h3cAclNameGroupTable = _H3cAclNameGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 3)
)
if mibBuilder.loadTexts:
    h3cAclNameGroupTable.setStatus("current")
_H3cAclNameGroupEntry_Object = MibTableRow
h3cAclNameGroupEntry = _H3cAclNameGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 3, 1)
)
h3cAclNameGroupEntry.setIndexNames(
    (0, "H3C-ACL-MIB", "h3cAclNameGroupIndex"),
)
if mibBuilder.loadTexts:
    h3cAclNameGroupEntry.setStatus("current")


class _H3cAclNameGroupIndex_Type(Integer32):
    """Custom type h3cAclNameGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 12999),
    )


_H3cAclNameGroupIndex_Type.__name__ = "Integer32"
_H3cAclNameGroupIndex_Object = MibTableColumn
h3cAclNameGroupIndex = _H3cAclNameGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 3, 1, 1),
    _H3cAclNameGroupIndex_Type()
)
h3cAclNameGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclNameGroupIndex.setStatus("current")


class _H3cAclNameGroupCreateName_Type(OctetString):
    """Custom type h3cAclNameGroupCreateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cAclNameGroupCreateName_Type.__name__ = "OctetString"
_H3cAclNameGroupCreateName_Object = MibTableColumn
h3cAclNameGroupCreateName = _H3cAclNameGroupCreateName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 3, 1, 2),
    _H3cAclNameGroupCreateName_Type()
)
h3cAclNameGroupCreateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclNameGroupCreateName.setStatus("current")


class _H3cAclNameGroupTypes_Type(Integer32):
    """Custom type h3cAclNameGroupTypes based on Integer32"""
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
        *(("advanced", 2),
          ("basic", 1),
          ("ifBased", 3),
          ("link", 4),
          ("user", 5))
    )


_H3cAclNameGroupTypes_Type.__name__ = "Integer32"
_H3cAclNameGroupTypes_Object = MibTableColumn
h3cAclNameGroupTypes = _H3cAclNameGroupTypes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 3, 1, 3),
    _H3cAclNameGroupTypes_Type()
)
h3cAclNameGroupTypes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclNameGroupTypes.setStatus("current")


class _H3cAclNameGroupMatchOrder_Type(Integer32):
    """Custom type h3cAclNameGroupMatchOrder based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("config", 1))
    )


_H3cAclNameGroupMatchOrder_Type.__name__ = "Integer32"
_H3cAclNameGroupMatchOrder_Object = MibTableColumn
h3cAclNameGroupMatchOrder = _H3cAclNameGroupMatchOrder_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 3, 1, 4),
    _H3cAclNameGroupMatchOrder_Type()
)
h3cAclNameGroupMatchOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclNameGroupMatchOrder.setStatus("current")


class _H3cAclNameGroupSubitemNum_Type(Integer32):
    """Custom type h3cAclNameGroupSubitemNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_H3cAclNameGroupSubitemNum_Type.__name__ = "Integer32"
_H3cAclNameGroupSubitemNum_Object = MibTableColumn
h3cAclNameGroupSubitemNum = _H3cAclNameGroupSubitemNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 3, 1, 5),
    _H3cAclNameGroupSubitemNum_Type()
)
h3cAclNameGroupSubitemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclNameGroupSubitemNum.setStatus("current")
_H3cAclNameGroupRowStatus_Type = RowStatus
_H3cAclNameGroupRowStatus_Object = MibTableColumn
h3cAclNameGroupRowStatus = _H3cAclNameGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 3, 1, 6),
    _H3cAclNameGroupRowStatus_Type()
)
h3cAclNameGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclNameGroupRowStatus.setStatus("current")
_H3cAclBasicRuleTable_Object = MibTable
h3cAclBasicRuleTable = _H3cAclBasicRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 4)
)
if mibBuilder.loadTexts:
    h3cAclBasicRuleTable.setStatus("current")
_H3cAclBasicRuleEntry_Object = MibTableRow
h3cAclBasicRuleEntry = _H3cAclBasicRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 4, 1)
)
h3cAclBasicRuleEntry.setIndexNames(
    (0, "H3C-ACL-MIB", "h3cAclBasicAclNum"),
    (0, "H3C-ACL-MIB", "h3cAclBasicSubitem"),
)
if mibBuilder.loadTexts:
    h3cAclBasicRuleEntry.setStatus("current")


class _H3cAclBasicAclNum_Type(Integer32):
    """Custom type h3cAclBasicAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2999),
        ValueRangeConstraint(10000, 12999),
    )


_H3cAclBasicAclNum_Type.__name__ = "Integer32"
_H3cAclBasicAclNum_Object = MibTableColumn
h3cAclBasicAclNum = _H3cAclBasicAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 4, 1, 1),
    _H3cAclBasicAclNum_Type()
)
h3cAclBasicAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclBasicAclNum.setStatus("current")


class _H3cAclBasicSubitem_Type(Integer32):
    """Custom type h3cAclBasicSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cAclBasicSubitem_Type.__name__ = "Integer32"
_H3cAclBasicSubitem_Object = MibTableColumn
h3cAclBasicSubitem = _H3cAclBasicSubitem_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 4, 1, 2),
    _H3cAclBasicSubitem_Type()
)
h3cAclBasicSubitem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclBasicSubitem.setStatus("current")


class _H3cAclBasicAct_Type(Integer32):
    """Custom type h3cAclBasicAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_H3cAclBasicAct_Type.__name__ = "Integer32"
_H3cAclBasicAct_Object = MibTableColumn
h3cAclBasicAct = _H3cAclBasicAct_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 4, 1, 3),
    _H3cAclBasicAct_Type()
)
h3cAclBasicAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclBasicAct.setStatus("current")
_H3cAclBasicSrcIp_Type = IpAddress
_H3cAclBasicSrcIp_Object = MibTableColumn
h3cAclBasicSrcIp = _H3cAclBasicSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 4, 1, 4),
    _H3cAclBasicSrcIp_Type()
)
h3cAclBasicSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclBasicSrcIp.setStatus("current")
_H3cAclBasicSrcWild_Type = IpAddress
_H3cAclBasicSrcWild_Object = MibTableColumn
h3cAclBasicSrcWild = _H3cAclBasicSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 4, 1, 5),
    _H3cAclBasicSrcWild_Type()
)
h3cAclBasicSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclBasicSrcWild.setStatus("current")


class _H3cAclBasicTimeRangeName_Type(OctetString):
    """Custom type h3cAclBasicTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cAclBasicTimeRangeName_Type.__name__ = "OctetString"
_H3cAclBasicTimeRangeName_Object = MibTableColumn
h3cAclBasicTimeRangeName = _H3cAclBasicTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 4, 1, 6),
    _H3cAclBasicTimeRangeName_Type()
)
h3cAclBasicTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclBasicTimeRangeName.setStatus("current")
_H3cAclBasicFragments_Type = TruthValue
_H3cAclBasicFragments_Object = MibTableColumn
h3cAclBasicFragments = _H3cAclBasicFragments_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 4, 1, 7),
    _H3cAclBasicFragments_Type()
)
h3cAclBasicFragments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclBasicFragments.setStatus("current")
_H3cAclBasicLog_Type = TruthValue
_H3cAclBasicLog_Object = MibTableColumn
h3cAclBasicLog = _H3cAclBasicLog_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 4, 1, 8),
    _H3cAclBasicLog_Type()
)
h3cAclBasicLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclBasicLog.setStatus("current")
_H3cAclBasicEnable_Type = TruthValue
_H3cAclBasicEnable_Object = MibTableColumn
h3cAclBasicEnable = _H3cAclBasicEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 4, 1, 9),
    _H3cAclBasicEnable_Type()
)
h3cAclBasicEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclBasicEnable.setStatus("current")
_H3cAclBasicCount_Type = Counter32
_H3cAclBasicCount_Object = MibTableColumn
h3cAclBasicCount = _H3cAclBasicCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 4, 1, 10),
    _H3cAclBasicCount_Type()
)
h3cAclBasicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclBasicCount.setStatus("current")


class _H3cAclBasicCountClear_Type(Integer32):
    """Custom type h3cAclBasicCountClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("nouse", 2))
    )


_H3cAclBasicCountClear_Type.__name__ = "Integer32"
_H3cAclBasicCountClear_Object = MibTableColumn
h3cAclBasicCountClear = _H3cAclBasicCountClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 4, 1, 11),
    _H3cAclBasicCountClear_Type()
)
h3cAclBasicCountClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclBasicCountClear.setStatus("current")
_H3cAclBasicRowStatus_Type = RowStatus
_H3cAclBasicRowStatus_Object = MibTableColumn
h3cAclBasicRowStatus = _H3cAclBasicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 4, 1, 12),
    _H3cAclBasicRowStatus_Type()
)
h3cAclBasicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclBasicRowStatus.setStatus("current")
_H3cAclAdvancedRuleTable_Object = MibTable
h3cAclAdvancedRuleTable = _H3cAclAdvancedRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5)
)
if mibBuilder.loadTexts:
    h3cAclAdvancedRuleTable.setStatus("current")
_H3cAclAdvancedRuleEntry_Object = MibTableRow
h3cAclAdvancedRuleEntry = _H3cAclAdvancedRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1)
)
h3cAclAdvancedRuleEntry.setIndexNames(
    (0, "H3C-ACL-MIB", "h3cAclAdvancedAclNum"),
    (0, "H3C-ACL-MIB", "h3cAclAdvancedSubitem"),
)
if mibBuilder.loadTexts:
    h3cAclAdvancedRuleEntry.setStatus("current")


class _H3cAclAdvancedAclNum_Type(Integer32):
    """Custom type h3cAclAdvancedAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_H3cAclAdvancedAclNum_Type.__name__ = "Integer32"
_H3cAclAdvancedAclNum_Object = MibTableColumn
h3cAclAdvancedAclNum = _H3cAclAdvancedAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 1),
    _H3cAclAdvancedAclNum_Type()
)
h3cAclAdvancedAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclAdvancedAclNum.setStatus("current")


class _H3cAclAdvancedSubitem_Type(Integer32):
    """Custom type h3cAclAdvancedSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cAclAdvancedSubitem_Type.__name__ = "Integer32"
_H3cAclAdvancedSubitem_Object = MibTableColumn
h3cAclAdvancedSubitem = _H3cAclAdvancedSubitem_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 2),
    _H3cAclAdvancedSubitem_Type()
)
h3cAclAdvancedSubitem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclAdvancedSubitem.setStatus("current")


class _H3cAclAdvancedAct_Type(Integer32):
    """Custom type h3cAclAdvancedAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_H3cAclAdvancedAct_Type.__name__ = "Integer32"
_H3cAclAdvancedAct_Object = MibTableColumn
h3cAclAdvancedAct = _H3cAclAdvancedAct_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 3),
    _H3cAclAdvancedAct_Type()
)
h3cAclAdvancedAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclAdvancedAct.setStatus("current")


class _H3cAclAdvancedProtocol_Type(Integer32):
    """Custom type h3cAclAdvancedProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cAclAdvancedProtocol_Type.__name__ = "Integer32"
_H3cAclAdvancedProtocol_Object = MibTableColumn
h3cAclAdvancedProtocol = _H3cAclAdvancedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 4),
    _H3cAclAdvancedProtocol_Type()
)
h3cAclAdvancedProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclAdvancedProtocol.setStatus("current")
_H3cAclAdvancedSrcIp_Type = IpAddress
_H3cAclAdvancedSrcIp_Object = MibTableColumn
h3cAclAdvancedSrcIp = _H3cAclAdvancedSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 5),
    _H3cAclAdvancedSrcIp_Type()
)
h3cAclAdvancedSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclAdvancedSrcIp.setStatus("current")
_H3cAclAdvancedSrcWild_Type = IpAddress
_H3cAclAdvancedSrcWild_Object = MibTableColumn
h3cAclAdvancedSrcWild = _H3cAclAdvancedSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 6),
    _H3cAclAdvancedSrcWild_Type()
)
h3cAclAdvancedSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclAdvancedSrcWild.setStatus("current")


class _H3cAclAdvancedSrcOp_Type(Integer32):
    """Custom type h3cAclAdvancedSrcOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eq", 2),
          ("gt", 3),
          ("invalid", 0),
          ("lt", 1),
          ("neq", 4),
          ("range", 5))
    )


_H3cAclAdvancedSrcOp_Type.__name__ = "Integer32"
_H3cAclAdvancedSrcOp_Object = MibTableColumn
h3cAclAdvancedSrcOp = _H3cAclAdvancedSrcOp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 7),
    _H3cAclAdvancedSrcOp_Type()
)
h3cAclAdvancedSrcOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclAdvancedSrcOp.setStatus("current")


class _H3cAclAdvancedSrcPort1_Type(Integer32):
    """Custom type h3cAclAdvancedSrcPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cAclAdvancedSrcPort1_Type.__name__ = "Integer32"
_H3cAclAdvancedSrcPort1_Object = MibTableColumn
h3cAclAdvancedSrcPort1 = _H3cAclAdvancedSrcPort1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 8),
    _H3cAclAdvancedSrcPort1_Type()
)
h3cAclAdvancedSrcPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclAdvancedSrcPort1.setStatus("current")


class _H3cAclAdvancedSrcPort2_Type(Integer32):
    """Custom type h3cAclAdvancedSrcPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cAclAdvancedSrcPort2_Type.__name__ = "Integer32"
_H3cAclAdvancedSrcPort2_Object = MibTableColumn
h3cAclAdvancedSrcPort2 = _H3cAclAdvancedSrcPort2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 9),
    _H3cAclAdvancedSrcPort2_Type()
)
h3cAclAdvancedSrcPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclAdvancedSrcPort2.setStatus("current")
_H3cAclAdvancedDestIp_Type = IpAddress
_H3cAclAdvancedDestIp_Object = MibTableColumn
h3cAclAdvancedDestIp = _H3cAclAdvancedDestIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 10),
    _H3cAclAdvancedDestIp_Type()
)
h3cAclAdvancedDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclAdvancedDestIp.setStatus("current")
_H3cAclAdvancedDestWild_Type = IpAddress
_H3cAclAdvancedDestWild_Object = MibTableColumn
h3cAclAdvancedDestWild = _H3cAclAdvancedDestWild_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 11),
    _H3cAclAdvancedDestWild_Type()
)
h3cAclAdvancedDestWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclAdvancedDestWild.setStatus("current")


class _H3cAclAdvancedDestOp_Type(Integer32):
    """Custom type h3cAclAdvancedDestOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eq", 2),
          ("gt", 3),
          ("invalid", 0),
          ("lt", 1),
          ("neq", 4),
          ("range", 5))
    )


_H3cAclAdvancedDestOp_Type.__name__ = "Integer32"
_H3cAclAdvancedDestOp_Object = MibTableColumn
h3cAclAdvancedDestOp = _H3cAclAdvancedDestOp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 12),
    _H3cAclAdvancedDestOp_Type()
)
h3cAclAdvancedDestOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclAdvancedDestOp.setStatus("current")


class _H3cAclAdvancedDestPort1_Type(Integer32):
    """Custom type h3cAclAdvancedDestPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cAclAdvancedDestPort1_Type.__name__ = "Integer32"
_H3cAclAdvancedDestPort1_Object = MibTableColumn
h3cAclAdvancedDestPort1 = _H3cAclAdvancedDestPort1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 13),
    _H3cAclAdvancedDestPort1_Type()
)
h3cAclAdvancedDestPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclAdvancedDestPort1.setStatus("current")


class _H3cAclAdvancedDestPort2_Type(Integer32):
    """Custom type h3cAclAdvancedDestPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cAclAdvancedDestPort2_Type.__name__ = "Integer32"
_H3cAclAdvancedDestPort2_Object = MibTableColumn
h3cAclAdvancedDestPort2 = _H3cAclAdvancedDestPort2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 14),
    _H3cAclAdvancedDestPort2_Type()
)
h3cAclAdvancedDestPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclAdvancedDestPort2.setStatus("current")


class _H3cAclAdvancedPrecedence_Type(Integer32):
    """Custom type h3cAclAdvancedPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_H3cAclAdvancedPrecedence_Type.__name__ = "Integer32"
_H3cAclAdvancedPrecedence_Object = MibTableColumn
h3cAclAdvancedPrecedence = _H3cAclAdvancedPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 15),
    _H3cAclAdvancedPrecedence_Type()
)
h3cAclAdvancedPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclAdvancedPrecedence.setStatus("current")


class _H3cAclAdvancedTos_Type(Integer32):
    """Custom type h3cAclAdvancedTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_H3cAclAdvancedTos_Type.__name__ = "Integer32"
_H3cAclAdvancedTos_Object = MibTableColumn
h3cAclAdvancedTos = _H3cAclAdvancedTos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 16),
    _H3cAclAdvancedTos_Type()
)
h3cAclAdvancedTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclAdvancedTos.setStatus("current")


class _H3cAclAdvancedDscp_Type(Integer32):
    """Custom type h3cAclAdvancedDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_H3cAclAdvancedDscp_Type.__name__ = "Integer32"
_H3cAclAdvancedDscp_Object = MibTableColumn
h3cAclAdvancedDscp = _H3cAclAdvancedDscp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 17),
    _H3cAclAdvancedDscp_Type()
)
h3cAclAdvancedDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclAdvancedDscp.setStatus("current")


class _H3cAclAdvancedEstablish_Type(TruthValue):
    """Custom type h3cAclAdvancedEstablish based on TruthValue"""


_H3cAclAdvancedEstablish_Object = MibTableColumn
h3cAclAdvancedEstablish = _H3cAclAdvancedEstablish_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 18),
    _H3cAclAdvancedEstablish_Type()
)
h3cAclAdvancedEstablish.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclAdvancedEstablish.setStatus("current")


class _H3cAclAdvancedTimeRangeName_Type(OctetString):
    """Custom type h3cAclAdvancedTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cAclAdvancedTimeRangeName_Type.__name__ = "OctetString"
_H3cAclAdvancedTimeRangeName_Object = MibTableColumn
h3cAclAdvancedTimeRangeName = _H3cAclAdvancedTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 19),
    _H3cAclAdvancedTimeRangeName_Type()
)
h3cAclAdvancedTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclAdvancedTimeRangeName.setStatus("current")


class _H3cAclAdvancedIcmpType_Type(Integer32):
    """Custom type h3cAclAdvancedIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_H3cAclAdvancedIcmpType_Type.__name__ = "Integer32"
_H3cAclAdvancedIcmpType_Object = MibTableColumn
h3cAclAdvancedIcmpType = _H3cAclAdvancedIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 20),
    _H3cAclAdvancedIcmpType_Type()
)
h3cAclAdvancedIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclAdvancedIcmpType.setStatus("current")


class _H3cAclAdvancedIcmpCode_Type(Integer32):
    """Custom type h3cAclAdvancedIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_H3cAclAdvancedIcmpCode_Type.__name__ = "Integer32"
_H3cAclAdvancedIcmpCode_Object = MibTableColumn
h3cAclAdvancedIcmpCode = _H3cAclAdvancedIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 21),
    _H3cAclAdvancedIcmpCode_Type()
)
h3cAclAdvancedIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclAdvancedIcmpCode.setStatus("current")
_H3cAclAdvancedFragments_Type = TruthValue
_H3cAclAdvancedFragments_Object = MibTableColumn
h3cAclAdvancedFragments = _H3cAclAdvancedFragments_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 22),
    _H3cAclAdvancedFragments_Type()
)
h3cAclAdvancedFragments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclAdvancedFragments.setStatus("current")
_H3cAclAdvancedLog_Type = TruthValue
_H3cAclAdvancedLog_Object = MibTableColumn
h3cAclAdvancedLog = _H3cAclAdvancedLog_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 23),
    _H3cAclAdvancedLog_Type()
)
h3cAclAdvancedLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclAdvancedLog.setStatus("current")
_H3cAclAdvancedEnable_Type = TruthValue
_H3cAclAdvancedEnable_Object = MibTableColumn
h3cAclAdvancedEnable = _H3cAclAdvancedEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 24),
    _H3cAclAdvancedEnable_Type()
)
h3cAclAdvancedEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclAdvancedEnable.setStatus("current")
_H3cAclAdvancedCount_Type = Counter32
_H3cAclAdvancedCount_Object = MibTableColumn
h3cAclAdvancedCount = _H3cAclAdvancedCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 25),
    _H3cAclAdvancedCount_Type()
)
h3cAclAdvancedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclAdvancedCount.setStatus("current")


class _H3cAclAdvancedCountClear_Type(Integer32):
    """Custom type h3cAclAdvancedCountClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("nouse", 2))
    )


_H3cAclAdvancedCountClear_Type.__name__ = "Integer32"
_H3cAclAdvancedCountClear_Object = MibTableColumn
h3cAclAdvancedCountClear = _H3cAclAdvancedCountClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 26),
    _H3cAclAdvancedCountClear_Type()
)
h3cAclAdvancedCountClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclAdvancedCountClear.setStatus("current")
_H3cAclAdvancedRowStatus_Type = RowStatus
_H3cAclAdvancedRowStatus_Object = MibTableColumn
h3cAclAdvancedRowStatus = _H3cAclAdvancedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 5, 1, 27),
    _H3cAclAdvancedRowStatus_Type()
)
h3cAclAdvancedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclAdvancedRowStatus.setStatus("current")
_H3cAclIfRuleTable_Object = MibTable
h3cAclIfRuleTable = _H3cAclIfRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 6)
)
if mibBuilder.loadTexts:
    h3cAclIfRuleTable.setStatus("current")
_H3cAclIfRuleEntry_Object = MibTableRow
h3cAclIfRuleEntry = _H3cAclIfRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 6, 1)
)
h3cAclIfRuleEntry.setIndexNames(
    (0, "H3C-ACL-MIB", "h3cAclIfAclNum"),
    (0, "H3C-ACL-MIB", "h3cAclIfSubitem"),
)
if mibBuilder.loadTexts:
    h3cAclIfRuleEntry.setStatus("current")


class _H3cAclIfAclNum_Type(Integer32):
    """Custom type h3cAclIfAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 1999),
        ValueRangeConstraint(10000, 12999),
    )


_H3cAclIfAclNum_Type.__name__ = "Integer32"
_H3cAclIfAclNum_Object = MibTableColumn
h3cAclIfAclNum = _H3cAclIfAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 6, 1, 1),
    _H3cAclIfAclNum_Type()
)
h3cAclIfAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclIfAclNum.setStatus("current")


class _H3cAclIfSubitem_Type(Integer32):
    """Custom type h3cAclIfSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cAclIfSubitem_Type.__name__ = "Integer32"
_H3cAclIfSubitem_Object = MibTableColumn
h3cAclIfSubitem = _H3cAclIfSubitem_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 6, 1, 2),
    _H3cAclIfSubitem_Type()
)
h3cAclIfSubitem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclIfSubitem.setStatus("current")


class _H3cAclIfAct_Type(Integer32):
    """Custom type h3cAclIfAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_H3cAclIfAct_Type.__name__ = "Integer32"
_H3cAclIfAct_Object = MibTableColumn
h3cAclIfAct = _H3cAclIfAct_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 6, 1, 3),
    _H3cAclIfAct_Type()
)
h3cAclIfAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIfAct.setStatus("current")


class _H3cAclIfIndex_Type(Integer32):
    """Custom type h3cAclIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cAclIfIndex_Type.__name__ = "Integer32"
_H3cAclIfIndex_Object = MibTableColumn
h3cAclIfIndex = _H3cAclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 6, 1, 4),
    _H3cAclIfIndex_Type()
)
h3cAclIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIfIndex.setStatus("current")
_H3cAclIfAny_Type = TruthValue
_H3cAclIfAny_Object = MibTableColumn
h3cAclIfAny = _H3cAclIfAny_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 6, 1, 5),
    _H3cAclIfAny_Type()
)
h3cAclIfAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIfAny.setStatus("current")


class _H3cAclIfTimeRangeName_Type(OctetString):
    """Custom type h3cAclIfTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cAclIfTimeRangeName_Type.__name__ = "OctetString"
_H3cAclIfTimeRangeName_Object = MibTableColumn
h3cAclIfTimeRangeName = _H3cAclIfTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 6, 1, 6),
    _H3cAclIfTimeRangeName_Type()
)
h3cAclIfTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIfTimeRangeName.setStatus("current")
_H3cAclIfLog_Type = TruthValue
_H3cAclIfLog_Object = MibTableColumn
h3cAclIfLog = _H3cAclIfLog_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 6, 1, 7),
    _H3cAclIfLog_Type()
)
h3cAclIfLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIfLog.setStatus("current")
_H3cAclIfEnable_Type = TruthValue
_H3cAclIfEnable_Object = MibTableColumn
h3cAclIfEnable = _H3cAclIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 6, 1, 8),
    _H3cAclIfEnable_Type()
)
h3cAclIfEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclIfEnable.setStatus("current")
_H3cAclIfCount_Type = Counter32
_H3cAclIfCount_Object = MibTableColumn
h3cAclIfCount = _H3cAclIfCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 6, 1, 9),
    _H3cAclIfCount_Type()
)
h3cAclIfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclIfCount.setStatus("current")


class _H3cAclIfCountClear_Type(Integer32):
    """Custom type h3cAclIfCountClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("nouse", 2))
    )


_H3cAclIfCountClear_Type.__name__ = "Integer32"
_H3cAclIfCountClear_Object = MibTableColumn
h3cAclIfCountClear = _H3cAclIfCountClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 6, 1, 10),
    _H3cAclIfCountClear_Type()
)
h3cAclIfCountClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIfCountClear.setStatus("current")
_H3cAclIfRowStatus_Type = RowStatus
_H3cAclIfRowStatus_Object = MibTableColumn
h3cAclIfRowStatus = _H3cAclIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 6, 1, 11),
    _H3cAclIfRowStatus_Type()
)
h3cAclIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIfRowStatus.setStatus("current")
_H3cAclLinkTable_Object = MibTable
h3cAclLinkTable = _H3cAclLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7)
)
if mibBuilder.loadTexts:
    h3cAclLinkTable.setStatus("current")
_H3cAclLinkEntry_Object = MibTableRow
h3cAclLinkEntry = _H3cAclLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1)
)
h3cAclLinkEntry.setIndexNames(
    (0, "H3C-ACL-MIB", "h3cAclLinkAclNum"),
    (0, "H3C-ACL-MIB", "h3cAclLinkSubitem"),
)
if mibBuilder.loadTexts:
    h3cAclLinkEntry.setStatus("current")


class _H3cAclLinkAclNum_Type(Integer32):
    """Custom type h3cAclLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_H3cAclLinkAclNum_Type.__name__ = "Integer32"
_H3cAclLinkAclNum_Object = MibTableColumn
h3cAclLinkAclNum = _H3cAclLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 1),
    _H3cAclLinkAclNum_Type()
)
h3cAclLinkAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclLinkAclNum.setStatus("current")


class _H3cAclLinkSubitem_Type(Integer32):
    """Custom type h3cAclLinkSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cAclLinkSubitem_Type.__name__ = "Integer32"
_H3cAclLinkSubitem_Object = MibTableColumn
h3cAclLinkSubitem = _H3cAclLinkSubitem_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 2),
    _H3cAclLinkSubitem_Type()
)
h3cAclLinkSubitem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclLinkSubitem.setStatus("current")


class _H3cAclLinkAct_Type(Integer32):
    """Custom type h3cAclLinkAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_H3cAclLinkAct_Type.__name__ = "Integer32"
_H3cAclLinkAct_Object = MibTableColumn
h3cAclLinkAct = _H3cAclLinkAct_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 3),
    _H3cAclLinkAct_Type()
)
h3cAclLinkAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkAct.setStatus("current")


class _H3cAclLinkProtocol_Type(Integer32):
    """Custom type h3cAclLinkProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2048,
              2054,
              32821,
              34887,
              34915,
              34916)
        )
    )
    namedValues = NamedValues(
        *(("arp", 2054),
          ("invalid", 0),
          ("ip", 2048),
          ("mpls", 34887),
          ("pppoeControl", 34915),
          ("pppoeData", 34916),
          ("rarp", 32821))
    )


_H3cAclLinkProtocol_Type.__name__ = "Integer32"
_H3cAclLinkProtocol_Object = MibTableColumn
h3cAclLinkProtocol = _H3cAclLinkProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 4),
    _H3cAclLinkProtocol_Type()
)
h3cAclLinkProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkProtocol.setStatus("current")


class _H3cAclLinkFormatType_Type(Integer32):
    """Custom type h3cAclLinkFormatType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ethernetII", 1),
          ("ieee802Dot3", 4),
          ("ieee802Dot3And2", 3),
          ("invalid", 0),
          ("snap", 2))
    )


_H3cAclLinkFormatType_Type.__name__ = "Integer32"
_H3cAclLinkFormatType_Object = MibTableColumn
h3cAclLinkFormatType = _H3cAclLinkFormatType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 5),
    _H3cAclLinkFormatType_Type()
)
h3cAclLinkFormatType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkFormatType.setStatus("current")


class _H3cAclLinkVlanTag_Type(Integer32):
    """Custom type h3cAclLinkVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("tagged", 1),
          ("untagged", 2))
    )


_H3cAclLinkVlanTag_Type.__name__ = "Integer32"
_H3cAclLinkVlanTag_Object = MibTableColumn
h3cAclLinkVlanTag = _H3cAclLinkVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 6),
    _H3cAclLinkVlanTag_Type()
)
h3cAclLinkVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkVlanTag.setStatus("current")


class _H3cAclLinkVlanPri_Type(Integer32):
    """Custom type h3cAclLinkVlanPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_H3cAclLinkVlanPri_Type.__name__ = "Integer32"
_H3cAclLinkVlanPri_Object = MibTableColumn
h3cAclLinkVlanPri = _H3cAclLinkVlanPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 7),
    _H3cAclLinkVlanPri_Type()
)
h3cAclLinkVlanPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkVlanPri.setStatus("current")


class _H3cAclLinkSrcVlanId_Type(Integer32):
    """Custom type h3cAclLinkSrcVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_H3cAclLinkSrcVlanId_Type.__name__ = "Integer32"
_H3cAclLinkSrcVlanId_Object = MibTableColumn
h3cAclLinkSrcVlanId = _H3cAclLinkSrcVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 8),
    _H3cAclLinkSrcVlanId_Type()
)
h3cAclLinkSrcVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkSrcVlanId.setStatus("current")
_H3cAclLinkSrcMac_Type = MacAddress
_H3cAclLinkSrcMac_Object = MibTableColumn
h3cAclLinkSrcMac = _H3cAclLinkSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 9),
    _H3cAclLinkSrcMac_Type()
)
h3cAclLinkSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkSrcMac.setStatus("current")
_H3cAclLinkSrcMacWild_Type = MacAddress
_H3cAclLinkSrcMacWild_Object = MibTableColumn
h3cAclLinkSrcMacWild = _H3cAclLinkSrcMacWild_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 10),
    _H3cAclLinkSrcMacWild_Type()
)
h3cAclLinkSrcMacWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkSrcMacWild.setStatus("current")


class _H3cAclLinkSrcIfIndex_Type(Integer32):
    """Custom type h3cAclLinkSrcIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cAclLinkSrcIfIndex_Type.__name__ = "Integer32"
_H3cAclLinkSrcIfIndex_Object = MibTableColumn
h3cAclLinkSrcIfIndex = _H3cAclLinkSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 11),
    _H3cAclLinkSrcIfIndex_Type()
)
h3cAclLinkSrcIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkSrcIfIndex.setStatus("current")
_H3cAclLinkSrcAny_Type = TruthValue
_H3cAclLinkSrcAny_Object = MibTableColumn
h3cAclLinkSrcAny = _H3cAclLinkSrcAny_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 12),
    _H3cAclLinkSrcAny_Type()
)
h3cAclLinkSrcAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkSrcAny.setStatus("current")


class _H3cAclLinkDestVlanId_Type(Integer32):
    """Custom type h3cAclLinkDestVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_H3cAclLinkDestVlanId_Type.__name__ = "Integer32"
_H3cAclLinkDestVlanId_Object = MibTableColumn
h3cAclLinkDestVlanId = _H3cAclLinkDestVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 13),
    _H3cAclLinkDestVlanId_Type()
)
h3cAclLinkDestVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkDestVlanId.setStatus("current")
_H3cAclLinkDestMac_Type = MacAddress
_H3cAclLinkDestMac_Object = MibTableColumn
h3cAclLinkDestMac = _H3cAclLinkDestMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 14),
    _H3cAclLinkDestMac_Type()
)
h3cAclLinkDestMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkDestMac.setStatus("current")
_H3cAclLinkDestMacWild_Type = MacAddress
_H3cAclLinkDestMacWild_Object = MibTableColumn
h3cAclLinkDestMacWild = _H3cAclLinkDestMacWild_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 15),
    _H3cAclLinkDestMacWild_Type()
)
h3cAclLinkDestMacWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkDestMacWild.setStatus("current")


class _H3cAclLinkDestIfIndex_Type(Integer32):
    """Custom type h3cAclLinkDestIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cAclLinkDestIfIndex_Type.__name__ = "Integer32"
_H3cAclLinkDestIfIndex_Object = MibTableColumn
h3cAclLinkDestIfIndex = _H3cAclLinkDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 16),
    _H3cAclLinkDestIfIndex_Type()
)
h3cAclLinkDestIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkDestIfIndex.setStatus("current")
_H3cAclLinkDestAny_Type = TruthValue
_H3cAclLinkDestAny_Object = MibTableColumn
h3cAclLinkDestAny = _H3cAclLinkDestAny_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 17),
    _H3cAclLinkDestAny_Type()
)
h3cAclLinkDestAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkDestAny.setStatus("current")


class _H3cAclLinkTimeRangeName_Type(OctetString):
    """Custom type h3cAclLinkTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cAclLinkTimeRangeName_Type.__name__ = "OctetString"
_H3cAclLinkTimeRangeName_Object = MibTableColumn
h3cAclLinkTimeRangeName = _H3cAclLinkTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 18),
    _H3cAclLinkTimeRangeName_Type()
)
h3cAclLinkTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkTimeRangeName.setStatus("current")
_H3cAclLinkEnable_Type = TruthValue
_H3cAclLinkEnable_Object = MibTableColumn
h3cAclLinkEnable = _H3cAclLinkEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 19),
    _H3cAclLinkEnable_Type()
)
h3cAclLinkEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclLinkEnable.setStatus("current")
_H3cAclLinkRowStatus_Type = RowStatus
_H3cAclLinkRowStatus_Object = MibTableColumn
h3cAclLinkRowStatus = _H3cAclLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 20),
    _H3cAclLinkRowStatus_Type()
)
h3cAclLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkRowStatus.setStatus("current")


class _H3cAclLinkTypeCode_Type(OctetString):
    """Custom type h3cAclLinkTypeCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cAclLinkTypeCode_Type.__name__ = "OctetString"
_H3cAclLinkTypeCode_Object = MibTableColumn
h3cAclLinkTypeCode = _H3cAclLinkTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 21),
    _H3cAclLinkTypeCode_Type()
)
h3cAclLinkTypeCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkTypeCode.setStatus("current")


class _H3cAclLinkTypeMask_Type(OctetString):
    """Custom type h3cAclLinkTypeMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cAclLinkTypeMask_Type.__name__ = "OctetString"
_H3cAclLinkTypeMask_Object = MibTableColumn
h3cAclLinkTypeMask = _H3cAclLinkTypeMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 22),
    _H3cAclLinkTypeMask_Type()
)
h3cAclLinkTypeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkTypeMask.setStatus("current")


class _H3cAclLinkLsapCode_Type(OctetString):
    """Custom type h3cAclLinkLsapCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cAclLinkLsapCode_Type.__name__ = "OctetString"
_H3cAclLinkLsapCode_Object = MibTableColumn
h3cAclLinkLsapCode = _H3cAclLinkLsapCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 23),
    _H3cAclLinkLsapCode_Type()
)
h3cAclLinkLsapCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkLsapCode.setStatus("current")


class _H3cAclLinkLsapMask_Type(OctetString):
    """Custom type h3cAclLinkLsapMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cAclLinkLsapMask_Type.__name__ = "OctetString"
_H3cAclLinkLsapMask_Object = MibTableColumn
h3cAclLinkLsapMask = _H3cAclLinkLsapMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 24),
    _H3cAclLinkLsapMask_Type()
)
h3cAclLinkLsapMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkLsapMask.setStatus("current")


class _H3cAclLinkL2LabelRangeOp_Type(Integer32):
    """Custom type h3cAclLinkL2LabelRangeOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eq", 2),
          ("gt", 3),
          ("invalid", 0),
          ("lt", 1),
          ("neq", 4),
          ("range", 5))
    )


_H3cAclLinkL2LabelRangeOp_Type.__name__ = "Integer32"
_H3cAclLinkL2LabelRangeOp_Object = MibTableColumn
h3cAclLinkL2LabelRangeOp = _H3cAclLinkL2LabelRangeOp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 25),
    _H3cAclLinkL2LabelRangeOp_Type()
)
h3cAclLinkL2LabelRangeOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkL2LabelRangeOp.setStatus("current")
_H3cAclLinkL2LabelRangeBegin_Type = Integer32
_H3cAclLinkL2LabelRangeBegin_Object = MibTableColumn
h3cAclLinkL2LabelRangeBegin = _H3cAclLinkL2LabelRangeBegin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 26),
    _H3cAclLinkL2LabelRangeBegin_Type()
)
h3cAclLinkL2LabelRangeBegin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkL2LabelRangeBegin.setStatus("current")
_H3cAclLinkL2LabelRangeEnd_Type = Integer32
_H3cAclLinkL2LabelRangeEnd_Object = MibTableColumn
h3cAclLinkL2LabelRangeEnd = _H3cAclLinkL2LabelRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 27),
    _H3cAclLinkL2LabelRangeEnd_Type()
)
h3cAclLinkL2LabelRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkL2LabelRangeEnd.setStatus("current")
_H3cAclLinkMplsExp_Type = Integer32
_H3cAclLinkMplsExp_Object = MibTableColumn
h3cAclLinkMplsExp = _H3cAclLinkMplsExp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 7, 1, 28),
    _H3cAclLinkMplsExp_Type()
)
h3cAclLinkMplsExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclLinkMplsExp.setStatus("current")
_H3cAclUserTable_Object = MibTable
h3cAclUserTable = _H3cAclUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 8)
)
if mibBuilder.loadTexts:
    h3cAclUserTable.setStatus("current")
_H3cAclUserEntry_Object = MibTableRow
h3cAclUserEntry = _H3cAclUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 8, 1)
)
h3cAclUserEntry.setIndexNames(
    (0, "H3C-ACL-MIB", "h3cAclUserAclNum"),
    (0, "H3C-ACL-MIB", "h3cAclUserSubitem"),
)
if mibBuilder.loadTexts:
    h3cAclUserEntry.setStatus("current")


class _H3cAclUserAclNum_Type(Integer32):
    """Custom type h3cAclUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_H3cAclUserAclNum_Type.__name__ = "Integer32"
_H3cAclUserAclNum_Object = MibTableColumn
h3cAclUserAclNum = _H3cAclUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 8, 1, 1),
    _H3cAclUserAclNum_Type()
)
h3cAclUserAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclUserAclNum.setStatus("current")


class _H3cAclUserSubitem_Type(Integer32):
    """Custom type h3cAclUserSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cAclUserSubitem_Type.__name__ = "Integer32"
_H3cAclUserSubitem_Object = MibTableColumn
h3cAclUserSubitem = _H3cAclUserSubitem_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 8, 1, 2),
    _H3cAclUserSubitem_Type()
)
h3cAclUserSubitem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclUserSubitem.setStatus("current")


class _H3cAclUserAct_Type(Integer32):
    """Custom type h3cAclUserAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_H3cAclUserAct_Type.__name__ = "Integer32"
_H3cAclUserAct_Object = MibTableColumn
h3cAclUserAct = _H3cAclUserAct_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 8, 1, 3),
    _H3cAclUserAct_Type()
)
h3cAclUserAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclUserAct.setStatus("current")


class _H3cAclUserFormatType_Type(Integer32):
    """Custom type h3cAclUserFormatType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ethernetII", 1),
          ("ieee802Dot2And3", 3),
          ("ieee802Dot4", 4),
          ("invalid", 0),
          ("snap", 2))
    )


_H3cAclUserFormatType_Type.__name__ = "Integer32"
_H3cAclUserFormatType_Object = MibTableColumn
h3cAclUserFormatType = _H3cAclUserFormatType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 8, 1, 4),
    _H3cAclUserFormatType_Type()
)
h3cAclUserFormatType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclUserFormatType.setStatus("current")


class _H3cAclUserVlanTag_Type(Integer32):
    """Custom type h3cAclUserVlanTag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("tagged", 1),
          ("untagged", 2))
    )


_H3cAclUserVlanTag_Type.__name__ = "Integer32"
_H3cAclUserVlanTag_Object = MibTableColumn
h3cAclUserVlanTag = _H3cAclUserVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 8, 1, 5),
    _H3cAclUserVlanTag_Type()
)
h3cAclUserVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclUserVlanTag.setStatus("current")


class _H3cAclUserRuleStr_Type(OctetString):
    """Custom type h3cAclUserRuleStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_H3cAclUserRuleStr_Type.__name__ = "OctetString"
_H3cAclUserRuleStr_Object = MibTableColumn
h3cAclUserRuleStr = _H3cAclUserRuleStr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 8, 1, 6),
    _H3cAclUserRuleStr_Type()
)
h3cAclUserRuleStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclUserRuleStr.setStatus("current")


class _H3cAclUserRuleMask_Type(OctetString):
    """Custom type h3cAclUserRuleMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_H3cAclUserRuleMask_Type.__name__ = "OctetString"
_H3cAclUserRuleMask_Object = MibTableColumn
h3cAclUserRuleMask = _H3cAclUserRuleMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 8, 1, 7),
    _H3cAclUserRuleMask_Type()
)
h3cAclUserRuleMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclUserRuleMask.setStatus("current")


class _H3cAclUserTimeRangeName_Type(OctetString):
    """Custom type h3cAclUserTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cAclUserTimeRangeName_Type.__name__ = "OctetString"
_H3cAclUserTimeRangeName_Object = MibTableColumn
h3cAclUserTimeRangeName = _H3cAclUserTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 8, 1, 8),
    _H3cAclUserTimeRangeName_Type()
)
h3cAclUserTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclUserTimeRangeName.setStatus("current")
_H3cAclUserEnable_Type = TruthValue
_H3cAclUserEnable_Object = MibTableColumn
h3cAclUserEnable = _H3cAclUserEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 8, 1, 9),
    _H3cAclUserEnable_Type()
)
h3cAclUserEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclUserEnable.setStatus("current")
_H3cAclUserRowStatus_Type = RowStatus
_H3cAclUserRowStatus_Object = MibTableColumn
h3cAclUserRowStatus = _H3cAclUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 8, 1, 10),
    _H3cAclUserRowStatus_Type()
)
h3cAclUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclUserRowStatus.setStatus("current")
_H3cAclActiveTable_Object = MibTable
h3cAclActiveTable = _H3cAclActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 9)
)
if mibBuilder.loadTexts:
    h3cAclActiveTable.setStatus("current")
_H3cAclActiveEntry_Object = MibTableRow
h3cAclActiveEntry = _H3cAclActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 9, 1)
)
h3cAclActiveEntry.setIndexNames(
    (0, "H3C-ACL-MIB", "h3cAclActiveAclIndex"),
    (0, "H3C-ACL-MIB", "h3cAclActiveIfIndex"),
    (0, "H3C-ACL-MIB", "h3cAclActiveVlanID"),
    (0, "H3C-ACL-MIB", "h3cAclActiveDirection"),
)
if mibBuilder.loadTexts:
    h3cAclActiveEntry.setStatus("current")


class _H3cAclActiveAclIndex_Type(Integer32):
    """Custom type h3cAclActiveAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_H3cAclActiveAclIndex_Type.__name__ = "Integer32"
_H3cAclActiveAclIndex_Object = MibTableColumn
h3cAclActiveAclIndex = _H3cAclActiveAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 9, 1, 1),
    _H3cAclActiveAclIndex_Type()
)
h3cAclActiveAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclActiveAclIndex.setStatus("current")


class _H3cAclActiveIfIndex_Type(Integer32):
    """Custom type h3cAclActiveIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cAclActiveIfIndex_Type.__name__ = "Integer32"
_H3cAclActiveIfIndex_Object = MibTableColumn
h3cAclActiveIfIndex = _H3cAclActiveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 9, 1, 2),
    _H3cAclActiveIfIndex_Type()
)
h3cAclActiveIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclActiveIfIndex.setStatus("current")
_H3cAclActiveVlanID_Type = Integer32
_H3cAclActiveVlanID_Object = MibTableColumn
h3cAclActiveVlanID = _H3cAclActiveVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 9, 1, 3),
    _H3cAclActiveVlanID_Type()
)
h3cAclActiveVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclActiveVlanID.setStatus("current")


class _H3cAclActiveDirection_Type(Integer32):
    """Custom type h3cAclActiveDirection based on Integer32"""
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
        *(("both", 3),
          ("input", 1),
          ("invalid", 0),
          ("output", 2))
    )


_H3cAclActiveDirection_Type.__name__ = "Integer32"
_H3cAclActiveDirection_Object = MibTableColumn
h3cAclActiveDirection = _H3cAclActiveDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 9, 1, 4),
    _H3cAclActiveDirection_Type()
)
h3cAclActiveDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclActiveDirection.setStatus("current")


class _H3cAclActiveUserAclNum_Type(Integer32):
    """Custom type h3cAclActiveUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_H3cAclActiveUserAclNum_Type.__name__ = "Integer32"
_H3cAclActiveUserAclNum_Object = MibTableColumn
h3cAclActiveUserAclNum = _H3cAclActiveUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 9, 1, 5),
    _H3cAclActiveUserAclNum_Type()
)
h3cAclActiveUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclActiveUserAclNum.setStatus("current")


class _H3cAclActiveUserAclSubitem_Type(Integer32):
    """Custom type h3cAclActiveUserAclSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cAclActiveUserAclSubitem_Type.__name__ = "Integer32"
_H3cAclActiveUserAclSubitem_Object = MibTableColumn
h3cAclActiveUserAclSubitem = _H3cAclActiveUserAclSubitem_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 9, 1, 6),
    _H3cAclActiveUserAclSubitem_Type()
)
h3cAclActiveUserAclSubitem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclActiveUserAclSubitem.setStatus("current")


class _H3cAclActiveIpAclNum_Type(Integer32):
    """Custom type h3cAclActiveIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_H3cAclActiveIpAclNum_Type.__name__ = "Integer32"
_H3cAclActiveIpAclNum_Object = MibTableColumn
h3cAclActiveIpAclNum = _H3cAclActiveIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 9, 1, 7),
    _H3cAclActiveIpAclNum_Type()
)
h3cAclActiveIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclActiveIpAclNum.setStatus("current")


class _H3cAclActiveIpAclSubitem_Type(Integer32):
    """Custom type h3cAclActiveIpAclSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cAclActiveIpAclSubitem_Type.__name__ = "Integer32"
_H3cAclActiveIpAclSubitem_Object = MibTableColumn
h3cAclActiveIpAclSubitem = _H3cAclActiveIpAclSubitem_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 9, 1, 8),
    _H3cAclActiveIpAclSubitem_Type()
)
h3cAclActiveIpAclSubitem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclActiveIpAclSubitem.setStatus("current")


class _H3cAclActiveLinkAclNum_Type(Integer32):
    """Custom type h3cAclActiveLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_H3cAclActiveLinkAclNum_Type.__name__ = "Integer32"
_H3cAclActiveLinkAclNum_Object = MibTableColumn
h3cAclActiveLinkAclNum = _H3cAclActiveLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 9, 1, 9),
    _H3cAclActiveLinkAclNum_Type()
)
h3cAclActiveLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclActiveLinkAclNum.setStatus("current")


class _H3cAclActiveLinkAclSubitem_Type(Integer32):
    """Custom type h3cAclActiveLinkAclSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cAclActiveLinkAclSubitem_Type.__name__ = "Integer32"
_H3cAclActiveLinkAclSubitem_Object = MibTableColumn
h3cAclActiveLinkAclSubitem = _H3cAclActiveLinkAclSubitem_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 9, 1, 10),
    _H3cAclActiveLinkAclSubitem_Type()
)
h3cAclActiveLinkAclSubitem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclActiveLinkAclSubitem.setStatus("current")
_H3cAclActiveRuntime_Type = TruthValue
_H3cAclActiveRuntime_Object = MibTableColumn
h3cAclActiveRuntime = _H3cAclActiveRuntime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 9, 1, 11),
    _H3cAclActiveRuntime_Type()
)
h3cAclActiveRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclActiveRuntime.setStatus("current")
_H3cAclActiveRowStatus_Type = RowStatus
_H3cAclActiveRowStatus_Object = MibTableColumn
h3cAclActiveRowStatus = _H3cAclActiveRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 9, 1, 12),
    _H3cAclActiveRowStatus_Type()
)
h3cAclActiveRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclActiveRowStatus.setStatus("current")
_H3cAclIDSTable_Object = MibTable
h3cAclIDSTable = _H3cAclIDSTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 10)
)
if mibBuilder.loadTexts:
    h3cAclIDSTable.setStatus("current")
_H3cAclIDSEntry_Object = MibTableRow
h3cAclIDSEntry = _H3cAclIDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 10, 1)
)
h3cAclIDSEntry.setIndexNames(
    (1, "H3C-ACL-MIB", "h3cAclIDSName"),
)
if mibBuilder.loadTexts:
    h3cAclIDSEntry.setStatus("current")


class _H3cAclIDSName_Type(OctetString):
    """Custom type h3cAclIDSName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_H3cAclIDSName_Type.__name__ = "OctetString"
_H3cAclIDSName_Object = MibTableColumn
h3cAclIDSName = _H3cAclIDSName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 10, 1, 1),
    _H3cAclIDSName_Type()
)
h3cAclIDSName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclIDSName.setStatus("current")
_H3cAclIDSSrcMac_Type = MacAddress
_H3cAclIDSSrcMac_Object = MibTableColumn
h3cAclIDSSrcMac = _H3cAclIDSSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 10, 1, 2),
    _H3cAclIDSSrcMac_Type()
)
h3cAclIDSSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIDSSrcMac.setStatus("current")
_H3cAclIDSDestMac_Type = MacAddress
_H3cAclIDSDestMac_Object = MibTableColumn
h3cAclIDSDestMac = _H3cAclIDSDestMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 10, 1, 3),
    _H3cAclIDSDestMac_Type()
)
h3cAclIDSDestMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIDSDestMac.setStatus("current")
_H3cAclIDSSrcIp_Type = IpAddress
_H3cAclIDSSrcIp_Object = MibTableColumn
h3cAclIDSSrcIp = _H3cAclIDSSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 10, 1, 4),
    _H3cAclIDSSrcIp_Type()
)
h3cAclIDSSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIDSSrcIp.setStatus("current")
_H3cAclIDSSrcWild_Type = IpAddress
_H3cAclIDSSrcWild_Object = MibTableColumn
h3cAclIDSSrcWild = _H3cAclIDSSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 10, 1, 5),
    _H3cAclIDSSrcWild_Type()
)
h3cAclIDSSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIDSSrcWild.setStatus("current")
_H3cAclIDSDestIp_Type = IpAddress
_H3cAclIDSDestIp_Object = MibTableColumn
h3cAclIDSDestIp = _H3cAclIDSDestIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 10, 1, 6),
    _H3cAclIDSDestIp_Type()
)
h3cAclIDSDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIDSDestIp.setStatus("current")
_H3cAclIDSDestWild_Type = IpAddress
_H3cAclIDSDestWild_Object = MibTableColumn
h3cAclIDSDestWild = _H3cAclIDSDestWild_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 10, 1, 7),
    _H3cAclIDSDestWild_Type()
)
h3cAclIDSDestWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIDSDestWild.setStatus("current")


class _H3cAclIDSSrcPort_Type(Integer32):
    """Custom type h3cAclIDSSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cAclIDSSrcPort_Type.__name__ = "Integer32"
_H3cAclIDSSrcPort_Object = MibTableColumn
h3cAclIDSSrcPort = _H3cAclIDSSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 10, 1, 8),
    _H3cAclIDSSrcPort_Type()
)
h3cAclIDSSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIDSSrcPort.setStatus("current")


class _H3cAclIDSDestPort_Type(Integer32):
    """Custom type h3cAclIDSDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cAclIDSDestPort_Type.__name__ = "Integer32"
_H3cAclIDSDestPort_Object = MibTableColumn
h3cAclIDSDestPort = _H3cAclIDSDestPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 10, 1, 9),
    _H3cAclIDSDestPort_Type()
)
h3cAclIDSDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIDSDestPort.setStatus("current")


class _H3cAclIDSProtocol_Type(Integer32):
    """Custom type h3cAclIDSProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cAclIDSProtocol_Type.__name__ = "Integer32"
_H3cAclIDSProtocol_Object = MibTableColumn
h3cAclIDSProtocol = _H3cAclIDSProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 10, 1, 10),
    _H3cAclIDSProtocol_Type()
)
h3cAclIDSProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIDSProtocol.setStatus("current")


class _H3cAclIDSDenyTime_Type(Unsigned32):
    """Custom type h3cAclIDSDenyTime based on Unsigned32"""
    defaultValue = 0


_H3cAclIDSDenyTime_Object = MibTableColumn
h3cAclIDSDenyTime = _H3cAclIDSDenyTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 10, 1, 11),
    _H3cAclIDSDenyTime_Type()
)
h3cAclIDSDenyTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIDSDenyTime.setStatus("current")


class _H3cAclIDSAct_Type(Integer32):
    """Custom type h3cAclIDSAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_H3cAclIDSAct_Type.__name__ = "Integer32"
_H3cAclIDSAct_Object = MibTableColumn
h3cAclIDSAct = _H3cAclIDSAct_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 10, 1, 12),
    _H3cAclIDSAct_Type()
)
h3cAclIDSAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIDSAct.setStatus("current")
_H3cAclIDSRowStatus_Type = RowStatus
_H3cAclIDSRowStatus_Object = MibTableColumn
h3cAclIDSRowStatus = _H3cAclIDSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 1, 10, 1, 13),
    _H3cAclIDSRowStatus_Type()
)
h3cAclIDSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIDSRowStatus.setStatus("current")
_H3cAclMib2Objects_ObjectIdentity = ObjectIdentity
h3cAclMib2Objects = _H3cAclMib2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2)
)
_H3cAclMib2GlobalGroup_ObjectIdentity = ObjectIdentity
h3cAclMib2GlobalGroup = _H3cAclMib2GlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1)
)
_H3cAclMib2NodesGroup_ObjectIdentity = ObjectIdentity
h3cAclMib2NodesGroup = _H3cAclMib2NodesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1, 1)
)


class _H3cAclMib2Mode_Type(Integer32):
    """Custom type h3cAclMib2Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipBased", 2),
          ("linkBased", 1))
    )


_H3cAclMib2Mode_Type.__name__ = "Integer32"
_H3cAclMib2Mode_Object = MibScalar
h3cAclMib2Mode = _H3cAclMib2Mode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1, 1, 1),
    _H3cAclMib2Mode_Type()
)
h3cAclMib2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cAclMib2Mode.setStatus("current")
_H3cAclMib2Version_Type = Integer32
_H3cAclMib2Version_Object = MibScalar
h3cAclMib2Version = _H3cAclMib2Version_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1, 1, 2),
    _H3cAclMib2Version_Type()
)
h3cAclMib2Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclMib2Version.setStatus("current")


class _H3cAclMib2ObjectsCapabilities_Type(Bits):
    """Custom type h3cAclMib2ObjectsCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("h3cAclEnUserTable", 8),
          ("h3cAclIPAclAdvancedTable", 6),
          ("h3cAclIPAclBasicTable", 5),
          ("h3cAclMACTable", 7),
          ("h3cAclMib2CapabilityTable", 3),
          ("h3cAclMib2Mode", 0),
          ("h3cAclMib2ObjectsCapabilities", 2),
          ("h3cAclMib2ProcessingStatus", 9),
          ("h3cAclNumberGroupTable", 4),
          ("h3cAclVersion", 1))
    )

_H3cAclMib2ObjectsCapabilities_Type.__name__ = "Bits"
_H3cAclMib2ObjectsCapabilities_Object = MibScalar
h3cAclMib2ObjectsCapabilities = _H3cAclMib2ObjectsCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1, 1, 3),
    _H3cAclMib2ObjectsCapabilities_Type()
)
h3cAclMib2ObjectsCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclMib2ObjectsCapabilities.setStatus("current")


class _H3cAclMib2ProcessingStatus_Type(Integer32):
    """Custom type h3cAclMib2ProcessingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("done", 2),
          ("processing", 1))
    )


_H3cAclMib2ProcessingStatus_Type.__name__ = "Integer32"
_H3cAclMib2ProcessingStatus_Object = MibScalar
h3cAclMib2ProcessingStatus = _H3cAclMib2ProcessingStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1, 1, 4),
    _H3cAclMib2ProcessingStatus_Type()
)
h3cAclMib2ProcessingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclMib2ProcessingStatus.setStatus("current")
_H3cAclMib2CapabilityTable_Object = MibTable
h3cAclMib2CapabilityTable = _H3cAclMib2CapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1, 2)
)
if mibBuilder.loadTexts:
    h3cAclMib2CapabilityTable.setStatus("current")
_H3cAclMib2CapabilityEntry_Object = MibTableRow
h3cAclMib2CapabilityEntry = _H3cAclMib2CapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1, 2, 1)
)
h3cAclMib2CapabilityEntry.setIndexNames(
    (0, "H3C-ACL-MIB", "h3cAclMib2EntityType"),
    (0, "H3C-ACL-MIB", "h3cAclMib2EntityIndex"),
    (0, "H3C-ACL-MIB", "h3cAclMib2ModuleIndex"),
    (0, "H3C-ACL-MIB", "h3cAclMib2CharacteristicsIndex"),
)
if mibBuilder.loadTexts:
    h3cAclMib2CapabilityEntry.setStatus("current")


class _H3cAclMib2EntityType_Type(Integer32):
    """Custom type h3cAclMib2EntityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 2),
          ("system", 1))
    )


_H3cAclMib2EntityType_Type.__name__ = "Integer32"
_H3cAclMib2EntityType_Object = MibTableColumn
h3cAclMib2EntityType = _H3cAclMib2EntityType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1, 2, 1, 1),
    _H3cAclMib2EntityType_Type()
)
h3cAclMib2EntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclMib2EntityType.setStatus("current")
_H3cAclMib2EntityIndex_Type = Integer32
_H3cAclMib2EntityIndex_Object = MibTableColumn
h3cAclMib2EntityIndex = _H3cAclMib2EntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1, 2, 1, 2),
    _H3cAclMib2EntityIndex_Type()
)
h3cAclMib2EntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclMib2EntityIndex.setStatus("current")


class _H3cAclMib2ModuleIndex_Type(Integer32):
    """Custom type h3cAclMib2ModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("layer2", 2),
          ("layer3", 1),
          ("userDefined", 3))
    )


_H3cAclMib2ModuleIndex_Type.__name__ = "Integer32"
_H3cAclMib2ModuleIndex_Object = MibTableColumn
h3cAclMib2ModuleIndex = _H3cAclMib2ModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1, 2, 1, 3),
    _H3cAclMib2ModuleIndex_Type()
)
h3cAclMib2ModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclMib2ModuleIndex.setStatus("current")
_H3cAclMib2CharacteristicsIndex_Type = Integer32
_H3cAclMib2CharacteristicsIndex_Object = MibTableColumn
h3cAclMib2CharacteristicsIndex = _H3cAclMib2CharacteristicsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1, 2, 1, 4),
    _H3cAclMib2CharacteristicsIndex_Type()
)
h3cAclMib2CharacteristicsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclMib2CharacteristicsIndex.setStatus("current")


class _H3cAclMib2CharacteristicsDesc_Type(OctetString):
    """Custom type h3cAclMib2CharacteristicsDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cAclMib2CharacteristicsDesc_Type.__name__ = "OctetString"
_H3cAclMib2CharacteristicsDesc_Object = MibTableColumn
h3cAclMib2CharacteristicsDesc = _H3cAclMib2CharacteristicsDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1, 2, 1, 5),
    _H3cAclMib2CharacteristicsDesc_Type()
)
h3cAclMib2CharacteristicsDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclMib2CharacteristicsDesc.setStatus("current")
_H3cAclMib2CharacteristicsValue_Type = Unsigned32
_H3cAclMib2CharacteristicsValue_Object = MibTableColumn
h3cAclMib2CharacteristicsValue = _H3cAclMib2CharacteristicsValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1, 2, 1, 6),
    _H3cAclMib2CharacteristicsValue_Type()
)
h3cAclMib2CharacteristicsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclMib2CharacteristicsValue.setStatus("current")
_H3cAclNumberGroupTable_Object = MibTable
h3cAclNumberGroupTable = _H3cAclNumberGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1, 3)
)
if mibBuilder.loadTexts:
    h3cAclNumberGroupTable.setStatus("current")
_H3cAclNumberGroupEntry_Object = MibTableRow
h3cAclNumberGroupEntry = _H3cAclNumberGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1, 3, 1)
)
h3cAclNumberGroupEntry.setIndexNames(
    (0, "H3C-ACL-MIB", "h3cAclNumberGroupType"),
    (0, "H3C-ACL-MIB", "h3cAclNumberGroupIndex"),
)
if mibBuilder.loadTexts:
    h3cAclNumberGroupEntry.setStatus("current")


class _H3cAclNumberGroupType_Type(Integer32):
    """Custom type h3cAclNumberGroupType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_H3cAclNumberGroupType_Type.__name__ = "Integer32"
_H3cAclNumberGroupType_Object = MibTableColumn
h3cAclNumberGroupType = _H3cAclNumberGroupType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1, 3, 1, 1),
    _H3cAclNumberGroupType_Type()
)
h3cAclNumberGroupType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclNumberGroupType.setStatus("current")


class _H3cAclNumberGroupIndex_Type(Integer32):
    """Custom type h3cAclNumberGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 5999),
        ValueRangeConstraint(10000, 42767),
    )


_H3cAclNumberGroupIndex_Type.__name__ = "Integer32"
_H3cAclNumberGroupIndex_Object = MibTableColumn
h3cAclNumberGroupIndex = _H3cAclNumberGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1, 3, 1, 2),
    _H3cAclNumberGroupIndex_Type()
)
h3cAclNumberGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclNumberGroupIndex.setStatus("current")
_H3cAclNumberGroupRowStatus_Type = RowStatus
_H3cAclNumberGroupRowStatus_Object = MibTableColumn
h3cAclNumberGroupRowStatus = _H3cAclNumberGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1, 3, 1, 3),
    _H3cAclNumberGroupRowStatus_Type()
)
h3cAclNumberGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclNumberGroupRowStatus.setStatus("current")


class _H3cAclNumberGroupMatchOrder_Type(Integer32):
    """Custom type h3cAclNumberGroupMatchOrder based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("config", 1))
    )


_H3cAclNumberGroupMatchOrder_Type.__name__ = "Integer32"
_H3cAclNumberGroupMatchOrder_Object = MibTableColumn
h3cAclNumberGroupMatchOrder = _H3cAclNumberGroupMatchOrder_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1, 3, 1, 4),
    _H3cAclNumberGroupMatchOrder_Type()
)
h3cAclNumberGroupMatchOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclNumberGroupMatchOrder.setStatus("current")


class _H3cAclNumberGroupStep_Type(Integer32):
    """Custom type h3cAclNumberGroupStep based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_H3cAclNumberGroupStep_Type.__name__ = "Integer32"
_H3cAclNumberGroupStep_Object = MibTableColumn
h3cAclNumberGroupStep = _H3cAclNumberGroupStep_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1, 3, 1, 5),
    _H3cAclNumberGroupStep_Type()
)
h3cAclNumberGroupStep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclNumberGroupStep.setStatus("current")


class _H3cAclNumberGroupDescription_Type(OctetString):
    """Custom type h3cAclNumberGroupDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cAclNumberGroupDescription_Type.__name__ = "OctetString"
_H3cAclNumberGroupDescription_Object = MibTableColumn
h3cAclNumberGroupDescription = _H3cAclNumberGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1, 3, 1, 6),
    _H3cAclNumberGroupDescription_Type()
)
h3cAclNumberGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclNumberGroupDescription.setStatus("current")


class _H3cAclNumberGroupCountClear_Type(CounterClear):
    """Custom type h3cAclNumberGroupCountClear based on CounterClear"""


_H3cAclNumberGroupCountClear_Object = MibTableColumn
h3cAclNumberGroupCountClear = _H3cAclNumberGroupCountClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1, 3, 1, 7),
    _H3cAclNumberGroupCountClear_Type()
)
h3cAclNumberGroupCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cAclNumberGroupCountClear.setStatus("current")
_H3cAclNumberGroupRuleCounter_Type = Counter32
_H3cAclNumberGroupRuleCounter_Object = MibTableColumn
h3cAclNumberGroupRuleCounter = _H3cAclNumberGroupRuleCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1, 3, 1, 8),
    _H3cAclNumberGroupRuleCounter_Type()
)
h3cAclNumberGroupRuleCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclNumberGroupRuleCounter.setStatus("current")


class _H3cAclNumberGroupName_Type(OctetString):
    """Custom type h3cAclNumberGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_H3cAclNumberGroupName_Type.__name__ = "OctetString"
_H3cAclNumberGroupName_Object = MibTableColumn
h3cAclNumberGroupName = _H3cAclNumberGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 1, 3, 1, 9),
    _H3cAclNumberGroupName_Type()
)
h3cAclNumberGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclNumberGroupName.setStatus("current")
_H3cAclIPAclGroup_ObjectIdentity = ObjectIdentity
h3cAclIPAclGroup = _H3cAclIPAclGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2)
)
_H3cAclIPAclBasicTable_Object = MibTable
h3cAclIPAclBasicTable = _H3cAclIPAclBasicTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 2)
)
if mibBuilder.loadTexts:
    h3cAclIPAclBasicTable.setStatus("current")
_H3cAclIPAclBasicEntry_Object = MibTableRow
h3cAclIPAclBasicEntry = _H3cAclIPAclBasicEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 2, 1)
)
h3cAclIPAclBasicEntry.setIndexNames(
    (0, "H3C-ACL-MIB", "h3cAclNumberGroupType"),
    (0, "H3C-ACL-MIB", "h3cAclNumberGroupIndex"),
    (0, "H3C-ACL-MIB", "h3cAclIPAclBasicRuleIndex"),
)
if mibBuilder.loadTexts:
    h3cAclIPAclBasicEntry.setStatus("current")


class _H3cAclIPAclBasicRuleIndex_Type(Integer32):
    """Custom type h3cAclIPAclBasicRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_H3cAclIPAclBasicRuleIndex_Type.__name__ = "Integer32"
_H3cAclIPAclBasicRuleIndex_Object = MibTableColumn
h3cAclIPAclBasicRuleIndex = _H3cAclIPAclBasicRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 2, 1, 1),
    _H3cAclIPAclBasicRuleIndex_Type()
)
h3cAclIPAclBasicRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclIPAclBasicRuleIndex.setStatus("current")
_H3cAclIPAclBasicRowStatus_Type = RowStatus
_H3cAclIPAclBasicRowStatus_Object = MibTableColumn
h3cAclIPAclBasicRowStatus = _H3cAclIPAclBasicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 2, 1, 2),
    _H3cAclIPAclBasicRowStatus_Type()
)
h3cAclIPAclBasicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclBasicRowStatus.setStatus("current")
_H3cAclIPAclBasicAct_Type = RuleAction
_H3cAclIPAclBasicAct_Object = MibTableColumn
h3cAclIPAclBasicAct = _H3cAclIPAclBasicAct_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 2, 1, 3),
    _H3cAclIPAclBasicAct_Type()
)
h3cAclIPAclBasicAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclBasicAct.setStatus("current")
_H3cAclIPAclBasicSrcAddrType_Type = InetAddressType
_H3cAclIPAclBasicSrcAddrType_Object = MibTableColumn
h3cAclIPAclBasicSrcAddrType = _H3cAclIPAclBasicSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 2, 1, 4),
    _H3cAclIPAclBasicSrcAddrType_Type()
)
h3cAclIPAclBasicSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclBasicSrcAddrType.setStatus("current")
_H3cAclIPAclBasicSrcAddr_Type = InetAddress
_H3cAclIPAclBasicSrcAddr_Object = MibTableColumn
h3cAclIPAclBasicSrcAddr = _H3cAclIPAclBasicSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 2, 1, 5),
    _H3cAclIPAclBasicSrcAddr_Type()
)
h3cAclIPAclBasicSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclBasicSrcAddr.setStatus("current")
_H3cAclIPAclBasicSrcPrefix_Type = InetAddressPrefixLength
_H3cAclIPAclBasicSrcPrefix_Object = MibTableColumn
h3cAclIPAclBasicSrcPrefix = _H3cAclIPAclBasicSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 2, 1, 6),
    _H3cAclIPAclBasicSrcPrefix_Type()
)
h3cAclIPAclBasicSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclBasicSrcPrefix.setStatus("current")
_H3cAclIPAclBasicSrcAny_Type = TruthValue
_H3cAclIPAclBasicSrcAny_Object = MibTableColumn
h3cAclIPAclBasicSrcAny = _H3cAclIPAclBasicSrcAny_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 2, 1, 7),
    _H3cAclIPAclBasicSrcAny_Type()
)
h3cAclIPAclBasicSrcAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclBasicSrcAny.setStatus("current")
_H3cAclIPAclBasicSrcWild_Type = IpAddress
_H3cAclIPAclBasicSrcWild_Object = MibTableColumn
h3cAclIPAclBasicSrcWild = _H3cAclIPAclBasicSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 2, 1, 8),
    _H3cAclIPAclBasicSrcWild_Type()
)
h3cAclIPAclBasicSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclBasicSrcWild.setStatus("current")


class _H3cAclIPAclBasicTimeRangeName_Type(OctetString):
    """Custom type h3cAclIPAclBasicTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cAclIPAclBasicTimeRangeName_Type.__name__ = "OctetString"
_H3cAclIPAclBasicTimeRangeName_Object = MibTableColumn
h3cAclIPAclBasicTimeRangeName = _H3cAclIPAclBasicTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 2, 1, 9),
    _H3cAclIPAclBasicTimeRangeName_Type()
)
h3cAclIPAclBasicTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclBasicTimeRangeName.setStatus("current")
_H3cAclIPAclBasicFragmentFlag_Type = FragmentFlag
_H3cAclIPAclBasicFragmentFlag_Object = MibTableColumn
h3cAclIPAclBasicFragmentFlag = _H3cAclIPAclBasicFragmentFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 2, 1, 10),
    _H3cAclIPAclBasicFragmentFlag_Type()
)
h3cAclIPAclBasicFragmentFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclBasicFragmentFlag.setStatus("current")
_H3cAclIPAclBasicLog_Type = TruthValue
_H3cAclIPAclBasicLog_Object = MibTableColumn
h3cAclIPAclBasicLog = _H3cAclIPAclBasicLog_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 2, 1, 11),
    _H3cAclIPAclBasicLog_Type()
)
h3cAclIPAclBasicLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclBasicLog.setStatus("current")
_H3cAclIPAclBasicCount_Type = Unsigned32
_H3cAclIPAclBasicCount_Object = MibTableColumn
h3cAclIPAclBasicCount = _H3cAclIPAclBasicCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 2, 1, 12),
    _H3cAclIPAclBasicCount_Type()
)
h3cAclIPAclBasicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclIPAclBasicCount.setStatus("current")
_H3cAclIPAclBasicCountClear_Type = CounterClear
_H3cAclIPAclBasicCountClear_Object = MibTableColumn
h3cAclIPAclBasicCountClear = _H3cAclIPAclBasicCountClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 2, 1, 13),
    _H3cAclIPAclBasicCountClear_Type()
)
h3cAclIPAclBasicCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cAclIPAclBasicCountClear.setStatus("current")
_H3cAclIPAclBasicEnable_Type = TruthValue
_H3cAclIPAclBasicEnable_Object = MibTableColumn
h3cAclIPAclBasicEnable = _H3cAclIPAclBasicEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 2, 1, 14),
    _H3cAclIPAclBasicEnable_Type()
)
h3cAclIPAclBasicEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclIPAclBasicEnable.setStatus("current")


class _H3cAclIPAclBasicVpnInstanceName_Type(OctetString):
    """Custom type h3cAclIPAclBasicVpnInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cAclIPAclBasicVpnInstanceName_Type.__name__ = "OctetString"
_H3cAclIPAclBasicVpnInstanceName_Object = MibTableColumn
h3cAclIPAclBasicVpnInstanceName = _H3cAclIPAclBasicVpnInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 2, 1, 15),
    _H3cAclIPAclBasicVpnInstanceName_Type()
)
h3cAclIPAclBasicVpnInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclBasicVpnInstanceName.setStatus("current")


class _H3cAclIPAclBasicComment_Type(OctetString):
    """Custom type h3cAclIPAclBasicComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cAclIPAclBasicComment_Type.__name__ = "OctetString"
_H3cAclIPAclBasicComment_Object = MibTableColumn
h3cAclIPAclBasicComment = _H3cAclIPAclBasicComment_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 2, 1, 16),
    _H3cAclIPAclBasicComment_Type()
)
h3cAclIPAclBasicComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclBasicComment.setStatus("current")


class _H3cAclIPAclBasicCounting_Type(TruthValue):
    """Custom type h3cAclIPAclBasicCounting based on TruthValue"""


_H3cAclIPAclBasicCounting_Object = MibTableColumn
h3cAclIPAclBasicCounting = _H3cAclIPAclBasicCounting_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 2, 1, 17),
    _H3cAclIPAclBasicCounting_Type()
)
h3cAclIPAclBasicCounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclBasicCounting.setStatus("current")


class _H3cAclIPAclBasicRouteTypeAny_Type(TruthValue):
    """Custom type h3cAclIPAclBasicRouteTypeAny based on TruthValue"""


_H3cAclIPAclBasicRouteTypeAny_Object = MibTableColumn
h3cAclIPAclBasicRouteTypeAny = _H3cAclIPAclBasicRouteTypeAny_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 2, 1, 18),
    _H3cAclIPAclBasicRouteTypeAny_Type()
)
h3cAclIPAclBasicRouteTypeAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclBasicRouteTypeAny.setStatus("current")


class _H3cAclIPAclBasicRouteTypeValue_Type(Integer32):
    """Custom type h3cAclIPAclBasicRouteTypeValue based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_H3cAclIPAclBasicRouteTypeValue_Type.__name__ = "Integer32"
_H3cAclIPAclBasicRouteTypeValue_Object = MibTableColumn
h3cAclIPAclBasicRouteTypeValue = _H3cAclIPAclBasicRouteTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 2, 1, 19),
    _H3cAclIPAclBasicRouteTypeValue_Type()
)
h3cAclIPAclBasicRouteTypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclBasicRouteTypeValue.setStatus("current")
_H3cAclIPAclAdvancedTable_Object = MibTable
h3cAclIPAclAdvancedTable = _H3cAclIPAclAdvancedTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3)
)
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedTable.setStatus("current")
_H3cAclIPAclAdvancedEntry_Object = MibTableRow
h3cAclIPAclAdvancedEntry = _H3cAclIPAclAdvancedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1)
)
h3cAclIPAclAdvancedEntry.setIndexNames(
    (0, "H3C-ACL-MIB", "h3cAclNumberGroupType"),
    (0, "H3C-ACL-MIB", "h3cAclNumberGroupIndex"),
    (0, "H3C-ACL-MIB", "h3cAclIPAclAdvancedRuleIndex"),
)
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedEntry.setStatus("current")


class _H3cAclIPAclAdvancedRuleIndex_Type(Integer32):
    """Custom type h3cAclIPAclAdvancedRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_H3cAclIPAclAdvancedRuleIndex_Type.__name__ = "Integer32"
_H3cAclIPAclAdvancedRuleIndex_Object = MibTableColumn
h3cAclIPAclAdvancedRuleIndex = _H3cAclIPAclAdvancedRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 1),
    _H3cAclIPAclAdvancedRuleIndex_Type()
)
h3cAclIPAclAdvancedRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedRuleIndex.setStatus("current")
_H3cAclIPAclAdvancedRowStatus_Type = RowStatus
_H3cAclIPAclAdvancedRowStatus_Object = MibTableColumn
h3cAclIPAclAdvancedRowStatus = _H3cAclIPAclAdvancedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 2),
    _H3cAclIPAclAdvancedRowStatus_Type()
)
h3cAclIPAclAdvancedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedRowStatus.setStatus("current")
_H3cAclIPAclAdvancedAct_Type = RuleAction
_H3cAclIPAclAdvancedAct_Object = MibTableColumn
h3cAclIPAclAdvancedAct = _H3cAclIPAclAdvancedAct_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 3),
    _H3cAclIPAclAdvancedAct_Type()
)
h3cAclIPAclAdvancedAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedAct.setStatus("current")


class _H3cAclIPAclAdvancedProtocol_Type(Integer32):
    """Custom type h3cAclIPAclAdvancedProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cAclIPAclAdvancedProtocol_Type.__name__ = "Integer32"
_H3cAclIPAclAdvancedProtocol_Object = MibTableColumn
h3cAclIPAclAdvancedProtocol = _H3cAclIPAclAdvancedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 4),
    _H3cAclIPAclAdvancedProtocol_Type()
)
h3cAclIPAclAdvancedProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedProtocol.setStatus("current")


class _H3cAclIPAclAdvancedAddrFlag_Type(AddressFlag):
    """Custom type h3cAclIPAclAdvancedAddrFlag based on AddressFlag"""


_H3cAclIPAclAdvancedAddrFlag_Object = MibTableColumn
h3cAclIPAclAdvancedAddrFlag = _H3cAclIPAclAdvancedAddrFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 5),
    _H3cAclIPAclAdvancedAddrFlag_Type()
)
h3cAclIPAclAdvancedAddrFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedAddrFlag.setStatus("current")
_H3cAclIPAclAdvancedSrcAddrType_Type = InetAddressType
_H3cAclIPAclAdvancedSrcAddrType_Object = MibTableColumn
h3cAclIPAclAdvancedSrcAddrType = _H3cAclIPAclAdvancedSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 6),
    _H3cAclIPAclAdvancedSrcAddrType_Type()
)
h3cAclIPAclAdvancedSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedSrcAddrType.setStatus("current")
_H3cAclIPAclAdvancedSrcAddr_Type = InetAddress
_H3cAclIPAclAdvancedSrcAddr_Object = MibTableColumn
h3cAclIPAclAdvancedSrcAddr = _H3cAclIPAclAdvancedSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 7),
    _H3cAclIPAclAdvancedSrcAddr_Type()
)
h3cAclIPAclAdvancedSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedSrcAddr.setStatus("current")
_H3cAclIPAclAdvancedSrcPrefix_Type = InetAddressPrefixLength
_H3cAclIPAclAdvancedSrcPrefix_Object = MibTableColumn
h3cAclIPAclAdvancedSrcPrefix = _H3cAclIPAclAdvancedSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 8),
    _H3cAclIPAclAdvancedSrcPrefix_Type()
)
h3cAclIPAclAdvancedSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedSrcPrefix.setStatus("current")


class _H3cAclIPAclAdvancedSrcAny_Type(TruthValue):
    """Custom type h3cAclIPAclAdvancedSrcAny based on TruthValue"""


_H3cAclIPAclAdvancedSrcAny_Object = MibTableColumn
h3cAclIPAclAdvancedSrcAny = _H3cAclIPAclAdvancedSrcAny_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 9),
    _H3cAclIPAclAdvancedSrcAny_Type()
)
h3cAclIPAclAdvancedSrcAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedSrcAny.setStatus("current")
_H3cAclIPAclAdvancedSrcWild_Type = IpAddress
_H3cAclIPAclAdvancedSrcWild_Object = MibTableColumn
h3cAclIPAclAdvancedSrcWild = _H3cAclIPAclAdvancedSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 10),
    _H3cAclIPAclAdvancedSrcWild_Type()
)
h3cAclIPAclAdvancedSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedSrcWild.setStatus("current")
_H3cAclIPAclAdvancedSrcOp_Type = PortOp
_H3cAclIPAclAdvancedSrcOp_Object = MibTableColumn
h3cAclIPAclAdvancedSrcOp = _H3cAclIPAclAdvancedSrcOp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 11),
    _H3cAclIPAclAdvancedSrcOp_Type()
)
h3cAclIPAclAdvancedSrcOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedSrcOp.setStatus("current")


class _H3cAclIPAclAdvancedSrcPort1_Type(Integer32):
    """Custom type h3cAclIPAclAdvancedSrcPort1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cAclIPAclAdvancedSrcPort1_Type.__name__ = "Integer32"
_H3cAclIPAclAdvancedSrcPort1_Object = MibTableColumn
h3cAclIPAclAdvancedSrcPort1 = _H3cAclIPAclAdvancedSrcPort1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 12),
    _H3cAclIPAclAdvancedSrcPort1_Type()
)
h3cAclIPAclAdvancedSrcPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedSrcPort1.setStatus("current")


class _H3cAclIPAclAdvancedSrcPort2_Type(Integer32):
    """Custom type h3cAclIPAclAdvancedSrcPort2 based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cAclIPAclAdvancedSrcPort2_Type.__name__ = "Integer32"
_H3cAclIPAclAdvancedSrcPort2_Object = MibTableColumn
h3cAclIPAclAdvancedSrcPort2 = _H3cAclIPAclAdvancedSrcPort2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 13),
    _H3cAclIPAclAdvancedSrcPort2_Type()
)
h3cAclIPAclAdvancedSrcPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedSrcPort2.setStatus("current")
_H3cAclIPAclAdvancedDestAddrType_Type = InetAddressType
_H3cAclIPAclAdvancedDestAddrType_Object = MibTableColumn
h3cAclIPAclAdvancedDestAddrType = _H3cAclIPAclAdvancedDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 14),
    _H3cAclIPAclAdvancedDestAddrType_Type()
)
h3cAclIPAclAdvancedDestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedDestAddrType.setStatus("current")
_H3cAclIPAclAdvancedDestAddr_Type = InetAddress
_H3cAclIPAclAdvancedDestAddr_Object = MibTableColumn
h3cAclIPAclAdvancedDestAddr = _H3cAclIPAclAdvancedDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 15),
    _H3cAclIPAclAdvancedDestAddr_Type()
)
h3cAclIPAclAdvancedDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedDestAddr.setStatus("current")
_H3cAclIPAclAdvancedDestPrefix_Type = InetAddressPrefixLength
_H3cAclIPAclAdvancedDestPrefix_Object = MibTableColumn
h3cAclIPAclAdvancedDestPrefix = _H3cAclIPAclAdvancedDestPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 16),
    _H3cAclIPAclAdvancedDestPrefix_Type()
)
h3cAclIPAclAdvancedDestPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedDestPrefix.setStatus("current")


class _H3cAclIPAclAdvancedDestAny_Type(TruthValue):
    """Custom type h3cAclIPAclAdvancedDestAny based on TruthValue"""


_H3cAclIPAclAdvancedDestAny_Object = MibTableColumn
h3cAclIPAclAdvancedDestAny = _H3cAclIPAclAdvancedDestAny_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 17),
    _H3cAclIPAclAdvancedDestAny_Type()
)
h3cAclIPAclAdvancedDestAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedDestAny.setStatus("current")
_H3cAclIPAclAdvancedDestWild_Type = IpAddress
_H3cAclIPAclAdvancedDestWild_Object = MibTableColumn
h3cAclIPAclAdvancedDestWild = _H3cAclIPAclAdvancedDestWild_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 18),
    _H3cAclIPAclAdvancedDestWild_Type()
)
h3cAclIPAclAdvancedDestWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedDestWild.setStatus("current")
_H3cAclIPAclAdvancedDestOp_Type = PortOp
_H3cAclIPAclAdvancedDestOp_Object = MibTableColumn
h3cAclIPAclAdvancedDestOp = _H3cAclIPAclAdvancedDestOp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 19),
    _H3cAclIPAclAdvancedDestOp_Type()
)
h3cAclIPAclAdvancedDestOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedDestOp.setStatus("current")


class _H3cAclIPAclAdvancedDestPort1_Type(Integer32):
    """Custom type h3cAclIPAclAdvancedDestPort1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cAclIPAclAdvancedDestPort1_Type.__name__ = "Integer32"
_H3cAclIPAclAdvancedDestPort1_Object = MibTableColumn
h3cAclIPAclAdvancedDestPort1 = _H3cAclIPAclAdvancedDestPort1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 20),
    _H3cAclIPAclAdvancedDestPort1_Type()
)
h3cAclIPAclAdvancedDestPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedDestPort1.setStatus("current")


class _H3cAclIPAclAdvancedDestPort2_Type(Integer32):
    """Custom type h3cAclIPAclAdvancedDestPort2 based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cAclIPAclAdvancedDestPort2_Type.__name__ = "Integer32"
_H3cAclIPAclAdvancedDestPort2_Object = MibTableColumn
h3cAclIPAclAdvancedDestPort2 = _H3cAclIPAclAdvancedDestPort2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 21),
    _H3cAclIPAclAdvancedDestPort2_Type()
)
h3cAclIPAclAdvancedDestPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedDestPort2.setStatus("current")


class _H3cAclIPAclAdvancedIcmpType_Type(Integer32):
    """Custom type h3cAclIPAclAdvancedIcmpType based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_H3cAclIPAclAdvancedIcmpType_Type.__name__ = "Integer32"
_H3cAclIPAclAdvancedIcmpType_Object = MibTableColumn
h3cAclIPAclAdvancedIcmpType = _H3cAclIPAclAdvancedIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 22),
    _H3cAclIPAclAdvancedIcmpType_Type()
)
h3cAclIPAclAdvancedIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedIcmpType.setStatus("current")


class _H3cAclIPAclAdvancedIcmpCode_Type(Integer32):
    """Custom type h3cAclIPAclAdvancedIcmpCode based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_H3cAclIPAclAdvancedIcmpCode_Type.__name__ = "Integer32"
_H3cAclIPAclAdvancedIcmpCode_Object = MibTableColumn
h3cAclIPAclAdvancedIcmpCode = _H3cAclIPAclAdvancedIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 23),
    _H3cAclIPAclAdvancedIcmpCode_Type()
)
h3cAclIPAclAdvancedIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedIcmpCode.setStatus("current")


class _H3cAclIPAclAdvancedPrecedence_Type(Integer32):
    """Custom type h3cAclIPAclAdvancedPrecedence based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_H3cAclIPAclAdvancedPrecedence_Type.__name__ = "Integer32"
_H3cAclIPAclAdvancedPrecedence_Object = MibTableColumn
h3cAclIPAclAdvancedPrecedence = _H3cAclIPAclAdvancedPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 24),
    _H3cAclIPAclAdvancedPrecedence_Type()
)
h3cAclIPAclAdvancedPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedPrecedence.setStatus("current")


class _H3cAclIPAclAdvancedTos_Type(Integer32):
    """Custom type h3cAclIPAclAdvancedTos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_H3cAclIPAclAdvancedTos_Type.__name__ = "Integer32"
_H3cAclIPAclAdvancedTos_Object = MibTableColumn
h3cAclIPAclAdvancedTos = _H3cAclIPAclAdvancedTos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 25),
    _H3cAclIPAclAdvancedTos_Type()
)
h3cAclIPAclAdvancedTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedTos.setStatus("current")


class _H3cAclIPAclAdvancedDscp_Type(DSCPValue):
    """Custom type h3cAclIPAclAdvancedDscp based on DSCPValue"""
    defaultValue = 255


_H3cAclIPAclAdvancedDscp_Object = MibTableColumn
h3cAclIPAclAdvancedDscp = _H3cAclIPAclAdvancedDscp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 26),
    _H3cAclIPAclAdvancedDscp_Type()
)
h3cAclIPAclAdvancedDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedDscp.setStatus("current")


class _H3cAclIPAclAdvancedTimeRangeName_Type(OctetString):
    """Custom type h3cAclIPAclAdvancedTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cAclIPAclAdvancedTimeRangeName_Type.__name__ = "OctetString"
_H3cAclIPAclAdvancedTimeRangeName_Object = MibTableColumn
h3cAclIPAclAdvancedTimeRangeName = _H3cAclIPAclAdvancedTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 27),
    _H3cAclIPAclAdvancedTimeRangeName_Type()
)
h3cAclIPAclAdvancedTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedTimeRangeName.setStatus("current")


class _H3cAclIPAclAdvancedTCPFlag_Type(TCPFlag):
    """Custom type h3cAclIPAclAdvancedTCPFlag based on TCPFlag"""


_H3cAclIPAclAdvancedTCPFlag_Object = MibTableColumn
h3cAclIPAclAdvancedTCPFlag = _H3cAclIPAclAdvancedTCPFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 28),
    _H3cAclIPAclAdvancedTCPFlag_Type()
)
h3cAclIPAclAdvancedTCPFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedTCPFlag.setStatus("current")


class _H3cAclIPAclAdvancedFragmentFlag_Type(FragmentFlag):
    """Custom type h3cAclIPAclAdvancedFragmentFlag based on FragmentFlag"""


_H3cAclIPAclAdvancedFragmentFlag_Object = MibTableColumn
h3cAclIPAclAdvancedFragmentFlag = _H3cAclIPAclAdvancedFragmentFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 29),
    _H3cAclIPAclAdvancedFragmentFlag_Type()
)
h3cAclIPAclAdvancedFragmentFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedFragmentFlag.setStatus("current")


class _H3cAclIPAclAdvancedLog_Type(TruthValue):
    """Custom type h3cAclIPAclAdvancedLog based on TruthValue"""


_H3cAclIPAclAdvancedLog_Object = MibTableColumn
h3cAclIPAclAdvancedLog = _H3cAclIPAclAdvancedLog_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 30),
    _H3cAclIPAclAdvancedLog_Type()
)
h3cAclIPAclAdvancedLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedLog.setStatus("current")
_H3cAclIPAclAdvancedCount_Type = Unsigned32
_H3cAclIPAclAdvancedCount_Object = MibTableColumn
h3cAclIPAclAdvancedCount = _H3cAclIPAclAdvancedCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 31),
    _H3cAclIPAclAdvancedCount_Type()
)
h3cAclIPAclAdvancedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedCount.setStatus("current")


class _H3cAclIPAclAdvancedCountClear_Type(CounterClear):
    """Custom type h3cAclIPAclAdvancedCountClear based on CounterClear"""


_H3cAclIPAclAdvancedCountClear_Object = MibTableColumn
h3cAclIPAclAdvancedCountClear = _H3cAclIPAclAdvancedCountClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 32),
    _H3cAclIPAclAdvancedCountClear_Type()
)
h3cAclIPAclAdvancedCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedCountClear.setStatus("current")


class _H3cAclIPAclAdvancedEnable_Type(TruthValue):
    """Custom type h3cAclIPAclAdvancedEnable based on TruthValue"""


_H3cAclIPAclAdvancedEnable_Object = MibTableColumn
h3cAclIPAclAdvancedEnable = _H3cAclIPAclAdvancedEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 33),
    _H3cAclIPAclAdvancedEnable_Type()
)
h3cAclIPAclAdvancedEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedEnable.setStatus("current")


class _H3cAclIPAclAdvancedVpnInstanceName_Type(OctetString):
    """Custom type h3cAclIPAclAdvancedVpnInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cAclIPAclAdvancedVpnInstanceName_Type.__name__ = "OctetString"
_H3cAclIPAclAdvancedVpnInstanceName_Object = MibTableColumn
h3cAclIPAclAdvancedVpnInstanceName = _H3cAclIPAclAdvancedVpnInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 34),
    _H3cAclIPAclAdvancedVpnInstanceName_Type()
)
h3cAclIPAclAdvancedVpnInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedVpnInstanceName.setStatus("current")


class _H3cAclIPAclAdvancedComment_Type(OctetString):
    """Custom type h3cAclIPAclAdvancedComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cAclIPAclAdvancedComment_Type.__name__ = "OctetString"
_H3cAclIPAclAdvancedComment_Object = MibTableColumn
h3cAclIPAclAdvancedComment = _H3cAclIPAclAdvancedComment_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 35),
    _H3cAclIPAclAdvancedComment_Type()
)
h3cAclIPAclAdvancedComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedComment.setStatus("current")
_H3cAclIPAclAdvancedReflective_Type = TruthValue
_H3cAclIPAclAdvancedReflective_Object = MibTableColumn
h3cAclIPAclAdvancedReflective = _H3cAclIPAclAdvancedReflective_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 36),
    _H3cAclIPAclAdvancedReflective_Type()
)
h3cAclIPAclAdvancedReflective.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedReflective.setStatus("current")


class _H3cAclIPAclAdvancedCounting_Type(TruthValue):
    """Custom type h3cAclIPAclAdvancedCounting based on TruthValue"""


_H3cAclIPAclAdvancedCounting_Object = MibTableColumn
h3cAclIPAclAdvancedCounting = _H3cAclIPAclAdvancedCounting_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 37),
    _H3cAclIPAclAdvancedCounting_Type()
)
h3cAclIPAclAdvancedCounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedCounting.setStatus("current")


class _H3cAclIPAclAdvancedTCPFlagMask_Type(Bits):
    """Custom type h3cAclIPAclAdvancedTCPFlagMask based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("tcpack", 0),
          ("tcpfin", 1),
          ("tcppsh", 2),
          ("tcprst", 3),
          ("tcpsyn", 4),
          ("tcpurg", 5))
    )

_H3cAclIPAclAdvancedTCPFlagMask_Type.__name__ = "Bits"
_H3cAclIPAclAdvancedTCPFlagMask_Object = MibTableColumn
h3cAclIPAclAdvancedTCPFlagMask = _H3cAclIPAclAdvancedTCPFlagMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 38),
    _H3cAclIPAclAdvancedTCPFlagMask_Type()
)
h3cAclIPAclAdvancedTCPFlagMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedTCPFlagMask.setStatus("current")


class _H3cAclIPAclAdvancedTCPFlagValue_Type(Bits):
    """Custom type h3cAclIPAclAdvancedTCPFlagValue based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("tcpack", 0),
          ("tcpfin", 1),
          ("tcppsh", 2),
          ("tcprst", 3),
          ("tcpsyn", 4),
          ("tcpurg", 5))
    )

_H3cAclIPAclAdvancedTCPFlagValue_Type.__name__ = "Bits"
_H3cAclIPAclAdvancedTCPFlagValue_Object = MibTableColumn
h3cAclIPAclAdvancedTCPFlagValue = _H3cAclIPAclAdvancedTCPFlagValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 39),
    _H3cAclIPAclAdvancedTCPFlagValue_Type()
)
h3cAclIPAclAdvancedTCPFlagValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedTCPFlagValue.setStatus("current")


class _H3cAclIPAclAdvancedRouteTypeAny_Type(TruthValue):
    """Custom type h3cAclIPAclAdvancedRouteTypeAny based on TruthValue"""


_H3cAclIPAclAdvancedRouteTypeAny_Object = MibTableColumn
h3cAclIPAclAdvancedRouteTypeAny = _H3cAclIPAclAdvancedRouteTypeAny_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 40),
    _H3cAclIPAclAdvancedRouteTypeAny_Type()
)
h3cAclIPAclAdvancedRouteTypeAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedRouteTypeAny.setStatus("current")


class _H3cAclIPAclAdvancedRouteTypeValue_Type(Integer32):
    """Custom type h3cAclIPAclAdvancedRouteTypeValue based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_H3cAclIPAclAdvancedRouteTypeValue_Type.__name__ = "Integer32"
_H3cAclIPAclAdvancedRouteTypeValue_Object = MibTableColumn
h3cAclIPAclAdvancedRouteTypeValue = _H3cAclIPAclAdvancedRouteTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 41),
    _H3cAclIPAclAdvancedRouteTypeValue_Type()
)
h3cAclIPAclAdvancedRouteTypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedRouteTypeValue.setStatus("current")


class _H3cAclIPAclAdvancedFlowLabel_Type(Unsigned32):
    """Custom type h3cAclIPAclAdvancedFlowLabel based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_H3cAclIPAclAdvancedFlowLabel_Type.__name__ = "Unsigned32"
_H3cAclIPAclAdvancedFlowLabel_Object = MibTableColumn
h3cAclIPAclAdvancedFlowLabel = _H3cAclIPAclAdvancedFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 2, 3, 1, 42),
    _H3cAclIPAclAdvancedFlowLabel_Type()
)
h3cAclIPAclAdvancedFlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclIPAclAdvancedFlowLabel.setStatus("current")
_H3cAclMACAclGroup_ObjectIdentity = ObjectIdentity
h3cAclMACAclGroup = _H3cAclMACAclGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 3)
)
_H3cAclMACTable_Object = MibTable
h3cAclMACTable = _H3cAclMACTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 3, 1)
)
if mibBuilder.loadTexts:
    h3cAclMACTable.setStatus("current")
_H3cAclMACEntry_Object = MibTableRow
h3cAclMACEntry = _H3cAclMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 3, 1, 1)
)
h3cAclMACEntry.setIndexNames(
    (0, "H3C-ACL-MIB", "h3cAclNumberGroupType"),
    (0, "H3C-ACL-MIB", "h3cAclNumberGroupIndex"),
    (0, "H3C-ACL-MIB", "h3cAclMACRuleIndex"),
)
if mibBuilder.loadTexts:
    h3cAclMACEntry.setStatus("current")


class _H3cAclMACRuleIndex_Type(Integer32):
    """Custom type h3cAclMACRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_H3cAclMACRuleIndex_Type.__name__ = "Integer32"
_H3cAclMACRuleIndex_Object = MibTableColumn
h3cAclMACRuleIndex = _H3cAclMACRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 3, 1, 1, 1),
    _H3cAclMACRuleIndex_Type()
)
h3cAclMACRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclMACRuleIndex.setStatus("current")
_H3cAclMACRowStatus_Type = RowStatus
_H3cAclMACRowStatus_Object = MibTableColumn
h3cAclMACRowStatus = _H3cAclMACRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 3, 1, 1, 2),
    _H3cAclMACRowStatus_Type()
)
h3cAclMACRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclMACRowStatus.setStatus("current")
_H3cAclMACAct_Type = RuleAction
_H3cAclMACAct_Object = MibTableColumn
h3cAclMACAct = _H3cAclMACAct_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 3, 1, 1, 3),
    _H3cAclMACAct_Type()
)
h3cAclMACAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclMACAct.setStatus("current")


class _H3cAclMACTypeCode_Type(OctetString):
    """Custom type h3cAclMACTypeCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cAclMACTypeCode_Type.__name__ = "OctetString"
_H3cAclMACTypeCode_Object = MibTableColumn
h3cAclMACTypeCode = _H3cAclMACTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 3, 1, 1, 4),
    _H3cAclMACTypeCode_Type()
)
h3cAclMACTypeCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclMACTypeCode.setStatus("current")


class _H3cAclMACTypeMask_Type(OctetString):
    """Custom type h3cAclMACTypeMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cAclMACTypeMask_Type.__name__ = "OctetString"
_H3cAclMACTypeMask_Object = MibTableColumn
h3cAclMACTypeMask = _H3cAclMACTypeMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 3, 1, 1, 5),
    _H3cAclMACTypeMask_Type()
)
h3cAclMACTypeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclMACTypeMask.setStatus("current")
_H3cAclMACSrcMac_Type = MacAddress
_H3cAclMACSrcMac_Object = MibTableColumn
h3cAclMACSrcMac = _H3cAclMACSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 3, 1, 1, 6),
    _H3cAclMACSrcMac_Type()
)
h3cAclMACSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclMACSrcMac.setStatus("current")
_H3cAclMACSrcMacWild_Type = MacAddress
_H3cAclMACSrcMacWild_Object = MibTableColumn
h3cAclMACSrcMacWild = _H3cAclMACSrcMacWild_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 3, 1, 1, 7),
    _H3cAclMACSrcMacWild_Type()
)
h3cAclMACSrcMacWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclMACSrcMacWild.setStatus("current")
_H3cAclMACDestMac_Type = MacAddress
_H3cAclMACDestMac_Object = MibTableColumn
h3cAclMACDestMac = _H3cAclMACDestMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 3, 1, 1, 8),
    _H3cAclMACDestMac_Type()
)
h3cAclMACDestMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclMACDestMac.setStatus("current")
_H3cAclMACDestMacWild_Type = MacAddress
_H3cAclMACDestMacWild_Object = MibTableColumn
h3cAclMACDestMacWild = _H3cAclMACDestMacWild_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 3, 1, 1, 9),
    _H3cAclMACDestMacWild_Type()
)
h3cAclMACDestMacWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclMACDestMacWild.setStatus("current")


class _H3cAclMACLsapCode_Type(OctetString):
    """Custom type h3cAclMACLsapCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cAclMACLsapCode_Type.__name__ = "OctetString"
_H3cAclMACLsapCode_Object = MibTableColumn
h3cAclMACLsapCode = _H3cAclMACLsapCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 3, 1, 1, 10),
    _H3cAclMACLsapCode_Type()
)
h3cAclMACLsapCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclMACLsapCode.setStatus("current")


class _H3cAclMACLsapMask_Type(OctetString):
    """Custom type h3cAclMACLsapMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cAclMACLsapMask_Type.__name__ = "OctetString"
_H3cAclMACLsapMask_Object = MibTableColumn
h3cAclMACLsapMask = _H3cAclMACLsapMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 3, 1, 1, 11),
    _H3cAclMACLsapMask_Type()
)
h3cAclMACLsapMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclMACLsapMask.setStatus("current")
_H3cAclMACCos_Type = Integer32
_H3cAclMACCos_Object = MibTableColumn
h3cAclMACCos = _H3cAclMACCos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 3, 1, 1, 12),
    _H3cAclMACCos_Type()
)
h3cAclMACCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclMACCos.setStatus("current")


class _H3cAclMACTimeRangeName_Type(OctetString):
    """Custom type h3cAclMACTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cAclMACTimeRangeName_Type.__name__ = "OctetString"
_H3cAclMACTimeRangeName_Object = MibTableColumn
h3cAclMACTimeRangeName = _H3cAclMACTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 3, 1, 1, 13),
    _H3cAclMACTimeRangeName_Type()
)
h3cAclMACTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclMACTimeRangeName.setStatus("current")
_H3cAclMACCount_Type = Unsigned32
_H3cAclMACCount_Object = MibTableColumn
h3cAclMACCount = _H3cAclMACCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 3, 1, 1, 14),
    _H3cAclMACCount_Type()
)
h3cAclMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclMACCount.setStatus("current")
_H3cAclMACCountClear_Type = CounterClear
_H3cAclMACCountClear_Object = MibTableColumn
h3cAclMACCountClear = _H3cAclMACCountClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 3, 1, 1, 15),
    _H3cAclMACCountClear_Type()
)
h3cAclMACCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cAclMACCountClear.setStatus("current")


class _H3cAclMACEnable_Type(TruthValue):
    """Custom type h3cAclMACEnable based on TruthValue"""


_H3cAclMACEnable_Object = MibTableColumn
h3cAclMACEnable = _H3cAclMACEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 3, 1, 1, 16),
    _H3cAclMACEnable_Type()
)
h3cAclMACEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclMACEnable.setStatus("current")


class _H3cAclMACComment_Type(OctetString):
    """Custom type h3cAclMACComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cAclMACComment_Type.__name__ = "OctetString"
_H3cAclMACComment_Object = MibTableColumn
h3cAclMACComment = _H3cAclMACComment_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 3, 1, 1, 17),
    _H3cAclMACComment_Type()
)
h3cAclMACComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclMACComment.setStatus("current")


class _H3cAclMACLog_Type(TruthValue):
    """Custom type h3cAclMACLog based on TruthValue"""


_H3cAclMACLog_Object = MibTableColumn
h3cAclMACLog = _H3cAclMACLog_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 3, 1, 1, 18),
    _H3cAclMACLog_Type()
)
h3cAclMACLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclMACLog.setStatus("current")


class _H3cAclMACCounting_Type(TruthValue):
    """Custom type h3cAclMACCounting based on TruthValue"""


_H3cAclMACCounting_Object = MibTableColumn
h3cAclMACCounting = _H3cAclMACCounting_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 3, 1, 1, 19),
    _H3cAclMACCounting_Type()
)
h3cAclMACCounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclMACCounting.setStatus("current")
_H3cAclEnUserAclGroup_ObjectIdentity = ObjectIdentity
h3cAclEnUserAclGroup = _H3cAclEnUserAclGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 4)
)
_H3cAclEnUserTable_Object = MibTable
h3cAclEnUserTable = _H3cAclEnUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 4, 3)
)
if mibBuilder.loadTexts:
    h3cAclEnUserTable.setStatus("current")
_H3cAclEnUserEntry_Object = MibTableRow
h3cAclEnUserEntry = _H3cAclEnUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 4, 3, 1)
)
h3cAclEnUserEntry.setIndexNames(
    (0, "H3C-ACL-MIB", "h3cAclNumberGroupType"),
    (0, "H3C-ACL-MIB", "h3cAclNumberGroupIndex"),
    (0, "H3C-ACL-MIB", "h3cAclEnUserRuleIndex"),
)
if mibBuilder.loadTexts:
    h3cAclEnUserEntry.setStatus("current")


class _H3cAclEnUserRuleIndex_Type(Integer32):
    """Custom type h3cAclEnUserRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_H3cAclEnUserRuleIndex_Type.__name__ = "Integer32"
_H3cAclEnUserRuleIndex_Object = MibTableColumn
h3cAclEnUserRuleIndex = _H3cAclEnUserRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 4, 3, 1, 1),
    _H3cAclEnUserRuleIndex_Type()
)
h3cAclEnUserRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclEnUserRuleIndex.setStatus("current")
_H3cAclEnUserRowStatus_Type = RowStatus
_H3cAclEnUserRowStatus_Object = MibTableColumn
h3cAclEnUserRowStatus = _H3cAclEnUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 4, 3, 1, 2),
    _H3cAclEnUserRowStatus_Type()
)
h3cAclEnUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclEnUserRowStatus.setStatus("current")
_H3cAclEnUserAct_Type = RuleAction
_H3cAclEnUserAct_Object = MibTableColumn
h3cAclEnUserAct = _H3cAclEnUserAct_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 4, 3, 1, 3),
    _H3cAclEnUserAct_Type()
)
h3cAclEnUserAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclEnUserAct.setStatus("current")


class _H3cAclEnUserStartString_Type(OctetString):
    """Custom type h3cAclEnUserStartString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cAclEnUserStartString_Type.__name__ = "OctetString"
_H3cAclEnUserStartString_Object = MibTableColumn
h3cAclEnUserStartString = _H3cAclEnUserStartString_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 4, 3, 1, 4),
    _H3cAclEnUserStartString_Type()
)
h3cAclEnUserStartString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclEnUserStartString.setStatus("current")


class _H3cAclEnUserL2String_Type(OctetString):
    """Custom type h3cAclEnUserL2String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cAclEnUserL2String_Type.__name__ = "OctetString"
_H3cAclEnUserL2String_Object = MibTableColumn
h3cAclEnUserL2String = _H3cAclEnUserL2String_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 4, 3, 1, 5),
    _H3cAclEnUserL2String_Type()
)
h3cAclEnUserL2String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclEnUserL2String.setStatus("current")


class _H3cAclEnUserMplsString_Type(OctetString):
    """Custom type h3cAclEnUserMplsString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cAclEnUserMplsString_Type.__name__ = "OctetString"
_H3cAclEnUserMplsString_Object = MibTableColumn
h3cAclEnUserMplsString = _H3cAclEnUserMplsString_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 4, 3, 1, 6),
    _H3cAclEnUserMplsString_Type()
)
h3cAclEnUserMplsString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclEnUserMplsString.setStatus("current")


class _H3cAclEnUserIPv4String_Type(OctetString):
    """Custom type h3cAclEnUserIPv4String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cAclEnUserIPv4String_Type.__name__ = "OctetString"
_H3cAclEnUserIPv4String_Object = MibTableColumn
h3cAclEnUserIPv4String = _H3cAclEnUserIPv4String_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 4, 3, 1, 7),
    _H3cAclEnUserIPv4String_Type()
)
h3cAclEnUserIPv4String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclEnUserIPv4String.setStatus("current")


class _H3cAclEnUserIPv6String_Type(OctetString):
    """Custom type h3cAclEnUserIPv6String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cAclEnUserIPv6String_Type.__name__ = "OctetString"
_H3cAclEnUserIPv6String_Object = MibTableColumn
h3cAclEnUserIPv6String = _H3cAclEnUserIPv6String_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 4, 3, 1, 8),
    _H3cAclEnUserIPv6String_Type()
)
h3cAclEnUserIPv6String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclEnUserIPv6String.setStatus("current")


class _H3cAclEnUserL4String_Type(OctetString):
    """Custom type h3cAclEnUserL4String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cAclEnUserL4String_Type.__name__ = "OctetString"
_H3cAclEnUserL4String_Object = MibTableColumn
h3cAclEnUserL4String = _H3cAclEnUserL4String_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 4, 3, 1, 9),
    _H3cAclEnUserL4String_Type()
)
h3cAclEnUserL4String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclEnUserL4String.setStatus("current")


class _H3cAclEnUserL5String_Type(OctetString):
    """Custom type h3cAclEnUserL5String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cAclEnUserL5String_Type.__name__ = "OctetString"
_H3cAclEnUserL5String_Object = MibTableColumn
h3cAclEnUserL5String = _H3cAclEnUserL5String_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 4, 3, 1, 10),
    _H3cAclEnUserL5String_Type()
)
h3cAclEnUserL5String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclEnUserL5String.setStatus("current")


class _H3cAclEnUserTimeRangeName_Type(OctetString):
    """Custom type h3cAclEnUserTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cAclEnUserTimeRangeName_Type.__name__ = "OctetString"
_H3cAclEnUserTimeRangeName_Object = MibTableColumn
h3cAclEnUserTimeRangeName = _H3cAclEnUserTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 4, 3, 1, 11),
    _H3cAclEnUserTimeRangeName_Type()
)
h3cAclEnUserTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclEnUserTimeRangeName.setStatus("current")
_H3cAclEnUserCount_Type = Unsigned32
_H3cAclEnUserCount_Object = MibTableColumn
h3cAclEnUserCount = _H3cAclEnUserCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 4, 3, 1, 12),
    _H3cAclEnUserCount_Type()
)
h3cAclEnUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclEnUserCount.setStatus("current")
_H3cAclEnUserCountClear_Type = CounterClear
_H3cAclEnUserCountClear_Object = MibTableColumn
h3cAclEnUserCountClear = _H3cAclEnUserCountClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 4, 3, 1, 13),
    _H3cAclEnUserCountClear_Type()
)
h3cAclEnUserCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cAclEnUserCountClear.setStatus("current")


class _H3cAclEnUserEnable_Type(TruthValue):
    """Custom type h3cAclEnUserEnable based on TruthValue"""


_H3cAclEnUserEnable_Object = MibTableColumn
h3cAclEnUserEnable = _H3cAclEnUserEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 4, 3, 1, 14),
    _H3cAclEnUserEnable_Type()
)
h3cAclEnUserEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclEnUserEnable.setStatus("current")


class _H3cAclEnUserComment_Type(OctetString):
    """Custom type h3cAclEnUserComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cAclEnUserComment_Type.__name__ = "OctetString"
_H3cAclEnUserComment_Object = MibTableColumn
h3cAclEnUserComment = _H3cAclEnUserComment_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 4, 3, 1, 15),
    _H3cAclEnUserComment_Type()
)
h3cAclEnUserComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclEnUserComment.setStatus("current")


class _H3cAclEnUserLog_Type(TruthValue):
    """Custom type h3cAclEnUserLog based on TruthValue"""


_H3cAclEnUserLog_Object = MibTableColumn
h3cAclEnUserLog = _H3cAclEnUserLog_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 4, 3, 1, 16),
    _H3cAclEnUserLog_Type()
)
h3cAclEnUserLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclEnUserLog.setStatus("current")


class _H3cAclEnUserCounting_Type(TruthValue):
    """Custom type h3cAclEnUserCounting based on TruthValue"""


_H3cAclEnUserCounting_Object = MibTableColumn
h3cAclEnUserCounting = _H3cAclEnUserCounting_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 4, 3, 1, 17),
    _H3cAclEnUserCounting_Type()
)
h3cAclEnUserCounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAclEnUserCounting.setStatus("current")
_H3cAclResourceGroup_ObjectIdentity = ObjectIdentity
h3cAclResourceGroup = _H3cAclResourceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 5)
)
_H3cAclResourceUsageTable_Object = MibTable
h3cAclResourceUsageTable = _H3cAclResourceUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 5, 1)
)
if mibBuilder.loadTexts:
    h3cAclResourceUsageTable.setStatus("current")
_H3cAclResourceUsageEntry_Object = MibTableRow
h3cAclResourceUsageEntry = _H3cAclResourceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 5, 1, 1)
)
h3cAclResourceUsageEntry.setIndexNames(
    (0, "H3C-ACL-MIB", "h3cAclResourceChassis"),
    (0, "H3C-ACL-MIB", "h3cAclResourceSlot"),
    (0, "H3C-ACL-MIB", "h3cAclResourceChip"),
    (0, "H3C-ACL-MIB", "h3cAclResourceType"),
)
if mibBuilder.loadTexts:
    h3cAclResourceUsageEntry.setStatus("current")
_H3cAclResourceChassis_Type = Unsigned32
_H3cAclResourceChassis_Object = MibTableColumn
h3cAclResourceChassis = _H3cAclResourceChassis_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 5, 1, 1, 1),
    _H3cAclResourceChassis_Type()
)
h3cAclResourceChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclResourceChassis.setStatus("current")
_H3cAclResourceSlot_Type = Unsigned32
_H3cAclResourceSlot_Object = MibTableColumn
h3cAclResourceSlot = _H3cAclResourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 5, 1, 1, 2),
    _H3cAclResourceSlot_Type()
)
h3cAclResourceSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclResourceSlot.setStatus("current")
_H3cAclResourceChip_Type = Unsigned32
_H3cAclResourceChip_Object = MibTableColumn
h3cAclResourceChip = _H3cAclResourceChip_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 5, 1, 1, 3),
    _H3cAclResourceChip_Type()
)
h3cAclResourceChip.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclResourceChip.setStatus("current")


class _H3cAclResourceType_Type(Integer32):
    """Custom type h3cAclResourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_H3cAclResourceType_Type.__name__ = "Integer32"
_H3cAclResourceType_Object = MibTableColumn
h3cAclResourceType = _H3cAclResourceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 5, 1, 1, 4),
    _H3cAclResourceType_Type()
)
h3cAclResourceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAclResourceType.setStatus("current")
_H3cAclPortRange_Type = OctetString
_H3cAclPortRange_Object = MibTableColumn
h3cAclPortRange = _H3cAclPortRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 5, 1, 1, 5),
    _H3cAclPortRange_Type()
)
h3cAclPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclPortRange.setStatus("current")
_H3cAclResourceTotal_Type = Unsigned32
_H3cAclResourceTotal_Object = MibTableColumn
h3cAclResourceTotal = _H3cAclResourceTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 5, 1, 1, 6),
    _H3cAclResourceTotal_Type()
)
h3cAclResourceTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclResourceTotal.setStatus("current")
_H3cAclResourceReserved_Type = Unsigned32
_H3cAclResourceReserved_Object = MibTableColumn
h3cAclResourceReserved = _H3cAclResourceReserved_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 5, 1, 1, 7),
    _H3cAclResourceReserved_Type()
)
h3cAclResourceReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclResourceReserved.setStatus("current")
_H3cAclResourceConfigured_Type = Unsigned32
_H3cAclResourceConfigured_Object = MibTableColumn
h3cAclResourceConfigured = _H3cAclResourceConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 5, 1, 1, 8),
    _H3cAclResourceConfigured_Type()
)
h3cAclResourceConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclResourceConfigured.setStatus("current")
_H3cAclResourceUsagePercent_Type = Unsigned32
_H3cAclResourceUsagePercent_Object = MibTableColumn
h3cAclResourceUsagePercent = _H3cAclResourceUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 5, 1, 1, 9),
    _H3cAclResourceUsagePercent_Type()
)
h3cAclResourceUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclResourceUsagePercent.setStatus("current")


class _H3cAclResourceTypeDescription_Type(OctetString):
    """Custom type h3cAclResourceTypeDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_H3cAclResourceTypeDescription_Type.__name__ = "OctetString"
_H3cAclResourceTypeDescription_Object = MibTableColumn
h3cAclResourceTypeDescription = _H3cAclResourceTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 2, 5, 1, 1, 10),
    _H3cAclResourceTypeDescription_Type()
)
h3cAclResourceTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAclResourceTypeDescription.setStatus("current")
_H3cAclPacketFilterObjects_ObjectIdentity = ObjectIdentity
h3cAclPacketFilterObjects = _H3cAclPacketFilterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3)
)
_H3cPfilterScalarGroup_ObjectIdentity = ObjectIdentity
h3cPfilterScalarGroup = _H3cPfilterScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 1)
)


class _H3cPfilterDefaultAction_Type(Integer32):
    """Custom type h3cPfilterDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_H3cPfilterDefaultAction_Type.__name__ = "Integer32"
_H3cPfilterDefaultAction_Object = MibScalar
h3cPfilterDefaultAction = _H3cPfilterDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 1, 1),
    _H3cPfilterDefaultAction_Type()
)
h3cPfilterDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPfilterDefaultAction.setStatus("current")


class _H3cPfilterProcessingStatus_Type(Integer32):
    """Custom type h3cPfilterProcessingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("done", 2),
          ("processing", 1))
    )


_H3cPfilterProcessingStatus_Type.__name__ = "Integer32"
_H3cPfilterProcessingStatus_Object = MibScalar
h3cPfilterProcessingStatus = _H3cPfilterProcessingStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 1, 2),
    _H3cPfilterProcessingStatus_Type()
)
h3cPfilterProcessingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPfilterProcessingStatus.setStatus("current")
_H3cPfilterApplyTable_Object = MibTable
h3cPfilterApplyTable = _H3cPfilterApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 2)
)
if mibBuilder.loadTexts:
    h3cPfilterApplyTable.setStatus("current")
_H3cPfilterApplyEntry_Object = MibTableRow
h3cPfilterApplyEntry = _H3cPfilterApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 2, 1)
)
h3cPfilterApplyEntry.setIndexNames(
    (0, "H3C-ACL-MIB", "h3cPfilterApplyObjType"),
    (0, "H3C-ACL-MIB", "h3cPfilterApplyObjIndex"),
    (0, "H3C-ACL-MIB", "h3cPfilterApplyDirection"),
    (0, "H3C-ACL-MIB", "h3cPfilterApplyAclType"),
    (0, "H3C-ACL-MIB", "h3cPfilterApplyAclIndex"),
)
if mibBuilder.loadTexts:
    h3cPfilterApplyEntry.setStatus("current")


class _H3cPfilterApplyObjType_Type(Integer32):
    """Custom type h3cPfilterApplyObjType based on Integer32"""
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
          ("interface", 1),
          ("vlan", 2))
    )


_H3cPfilterApplyObjType_Type.__name__ = "Integer32"
_H3cPfilterApplyObjType_Object = MibTableColumn
h3cPfilterApplyObjType = _H3cPfilterApplyObjType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 2, 1, 1),
    _H3cPfilterApplyObjType_Type()
)
h3cPfilterApplyObjType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPfilterApplyObjType.setStatus("current")


class _H3cPfilterApplyObjIndex_Type(Integer32):
    """Custom type h3cPfilterApplyObjIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cPfilterApplyObjIndex_Type.__name__ = "Integer32"
_H3cPfilterApplyObjIndex_Object = MibTableColumn
h3cPfilterApplyObjIndex = _H3cPfilterApplyObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 2, 1, 2),
    _H3cPfilterApplyObjIndex_Type()
)
h3cPfilterApplyObjIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPfilterApplyObjIndex.setStatus("current")
_H3cPfilterApplyDirection_Type = DirectionType
_H3cPfilterApplyDirection_Object = MibTableColumn
h3cPfilterApplyDirection = _H3cPfilterApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 2, 1, 3),
    _H3cPfilterApplyDirection_Type()
)
h3cPfilterApplyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPfilterApplyDirection.setStatus("current")


class _H3cPfilterApplyAclType_Type(Integer32):
    """Custom type h3cPfilterApplyAclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("ipv4", 1),
          ("ipv6", 2))
    )


_H3cPfilterApplyAclType_Type.__name__ = "Integer32"
_H3cPfilterApplyAclType_Object = MibTableColumn
h3cPfilterApplyAclType = _H3cPfilterApplyAclType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 2, 1, 4),
    _H3cPfilterApplyAclType_Type()
)
h3cPfilterApplyAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPfilterApplyAclType.setStatus("current")


class _H3cPfilterApplyAclIndex_Type(Integer32):
    """Custom type h3cPfilterApplyAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 5999),
    )


_H3cPfilterApplyAclIndex_Type.__name__ = "Integer32"
_H3cPfilterApplyAclIndex_Object = MibTableColumn
h3cPfilterApplyAclIndex = _H3cPfilterApplyAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 2, 1, 5),
    _H3cPfilterApplyAclIndex_Type()
)
h3cPfilterApplyAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPfilterApplyAclIndex.setStatus("current")


class _H3cPfilterApplyHardCount_Type(TruthValue):
    """Custom type h3cPfilterApplyHardCount based on TruthValue"""


_H3cPfilterApplyHardCount_Object = MibTableColumn
h3cPfilterApplyHardCount = _H3cPfilterApplyHardCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 2, 1, 6),
    _H3cPfilterApplyHardCount_Type()
)
h3cPfilterApplyHardCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPfilterApplyHardCount.setStatus("current")
_H3cPfilterApplySequence_Type = Unsigned32
_H3cPfilterApplySequence_Object = MibTableColumn
h3cPfilterApplySequence = _H3cPfilterApplySequence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 2, 1, 7),
    _H3cPfilterApplySequence_Type()
)
h3cPfilterApplySequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPfilterApplySequence.setStatus("current")
_H3cPfilterApplyCountClear_Type = CounterClear
_H3cPfilterApplyCountClear_Object = MibTableColumn
h3cPfilterApplyCountClear = _H3cPfilterApplyCountClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 2, 1, 8),
    _H3cPfilterApplyCountClear_Type()
)
h3cPfilterApplyCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPfilterApplyCountClear.setStatus("current")
_H3cPfilterApplyRowStatus_Type = RowStatus
_H3cPfilterApplyRowStatus_Object = MibTableColumn
h3cPfilterApplyRowStatus = _H3cPfilterApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 2, 1, 9),
    _H3cPfilterApplyRowStatus_Type()
)
h3cPfilterApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPfilterApplyRowStatus.setStatus("current")
_H3cPfilterAclGroupRunInfoTable_Object = MibTable
h3cPfilterAclGroupRunInfoTable = _H3cPfilterAclGroupRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 3)
)
if mibBuilder.loadTexts:
    h3cPfilterAclGroupRunInfoTable.setStatus("current")
_H3cPfilterAclGroupRunInfoEntry_Object = MibTableRow
h3cPfilterAclGroupRunInfoEntry = _H3cPfilterAclGroupRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 3, 1)
)
h3cPfilterAclGroupRunInfoEntry.setIndexNames(
    (0, "H3C-ACL-MIB", "h3cPfilterApplyObjType"),
    (0, "H3C-ACL-MIB", "h3cPfilterApplyObjIndex"),
    (0, "H3C-ACL-MIB", "h3cPfilterApplyDirection"),
    (0, "H3C-ACL-MIB", "h3cPfilterApplyAclType"),
    (0, "H3C-ACL-MIB", "h3cPfilterApplyAclIndex"),
)
if mibBuilder.loadTexts:
    h3cPfilterAclGroupRunInfoEntry.setStatus("current")


class _H3cPfilterAclGroupStatus_Type(Integer32):
    """Custom type h3cPfilterAclGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("partialSuccess", 3),
          ("success", 1))
    )


_H3cPfilterAclGroupStatus_Type.__name__ = "Integer32"
_H3cPfilterAclGroupStatus_Object = MibTableColumn
h3cPfilterAclGroupStatus = _H3cPfilterAclGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 3, 1, 1),
    _H3cPfilterAclGroupStatus_Type()
)
h3cPfilterAclGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPfilterAclGroupStatus.setStatus("current")


class _H3cPfilterAclGroupCountStatus_Type(Integer32):
    """Custom type h3cPfilterAclGroupCountStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("partialSuccess", 3),
          ("success", 1))
    )


_H3cPfilterAclGroupCountStatus_Type.__name__ = "Integer32"
_H3cPfilterAclGroupCountStatus_Object = MibTableColumn
h3cPfilterAclGroupCountStatus = _H3cPfilterAclGroupCountStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 3, 1, 2),
    _H3cPfilterAclGroupCountStatus_Type()
)
h3cPfilterAclGroupCountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPfilterAclGroupCountStatus.setStatus("current")
_H3cPfilterAclGroupPermitPkts_Type = Counter64
_H3cPfilterAclGroupPermitPkts_Object = MibTableColumn
h3cPfilterAclGroupPermitPkts = _H3cPfilterAclGroupPermitPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 3, 1, 3),
    _H3cPfilterAclGroupPermitPkts_Type()
)
h3cPfilterAclGroupPermitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPfilterAclGroupPermitPkts.setStatus("current")
_H3cPfilterAclGroupPermitBytes_Type = Counter64
_H3cPfilterAclGroupPermitBytes_Object = MibTableColumn
h3cPfilterAclGroupPermitBytes = _H3cPfilterAclGroupPermitBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 3, 1, 4),
    _H3cPfilterAclGroupPermitBytes_Type()
)
h3cPfilterAclGroupPermitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPfilterAclGroupPermitBytes.setStatus("current")
_H3cPfilterAclGroupDenyPkts_Type = Counter64
_H3cPfilterAclGroupDenyPkts_Object = MibTableColumn
h3cPfilterAclGroupDenyPkts = _H3cPfilterAclGroupDenyPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 3, 1, 5),
    _H3cPfilterAclGroupDenyPkts_Type()
)
h3cPfilterAclGroupDenyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPfilterAclGroupDenyPkts.setStatus("current")
_H3cPfilterAclGroupDenyBytes_Type = Counter64
_H3cPfilterAclGroupDenyBytes_Object = MibTableColumn
h3cPfilterAclGroupDenyBytes = _H3cPfilterAclGroupDenyBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 3, 1, 6),
    _H3cPfilterAclGroupDenyBytes_Type()
)
h3cPfilterAclGroupDenyBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPfilterAclGroupDenyBytes.setStatus("current")
_H3cPfilterAclRuleRunInfoTable_Object = MibTable
h3cPfilterAclRuleRunInfoTable = _H3cPfilterAclRuleRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 4)
)
if mibBuilder.loadTexts:
    h3cPfilterAclRuleRunInfoTable.setStatus("current")
_H3cPfilterAclRuleRunInfoEntry_Object = MibTableRow
h3cPfilterAclRuleRunInfoEntry = _H3cPfilterAclRuleRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 4, 1)
)
h3cPfilterAclRuleRunInfoEntry.setIndexNames(
    (0, "H3C-ACL-MIB", "h3cPfilterApplyObjType"),
    (0, "H3C-ACL-MIB", "h3cPfilterApplyObjIndex"),
    (0, "H3C-ACL-MIB", "h3cPfilterApplyDirection"),
    (0, "H3C-ACL-MIB", "h3cPfilterApplyAclType"),
    (0, "H3C-ACL-MIB", "h3cPfilterApplyAclIndex"),
    (0, "H3C-ACL-MIB", "h3cPfilterAclRuleIndex"),
)
if mibBuilder.loadTexts:
    h3cPfilterAclRuleRunInfoEntry.setStatus("current")


class _H3cPfilterAclRuleIndex_Type(Integer32):
    """Custom type h3cPfilterAclRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_H3cPfilterAclRuleIndex_Type.__name__ = "Integer32"
_H3cPfilterAclRuleIndex_Object = MibTableColumn
h3cPfilterAclRuleIndex = _H3cPfilterAclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 4, 1, 1),
    _H3cPfilterAclRuleIndex_Type()
)
h3cPfilterAclRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPfilterAclRuleIndex.setStatus("current")


class _H3cPfilterAclRuleStatus_Type(Integer32):
    """Custom type h3cPfilterAclRuleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("partialSuccess", 3),
          ("success", 1))
    )


_H3cPfilterAclRuleStatus_Type.__name__ = "Integer32"
_H3cPfilterAclRuleStatus_Object = MibTableColumn
h3cPfilterAclRuleStatus = _H3cPfilterAclRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 4, 1, 2),
    _H3cPfilterAclRuleStatus_Type()
)
h3cPfilterAclRuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPfilterAclRuleStatus.setStatus("current")


class _H3cPfilterAclRuleCountStatus_Type(Integer32):
    """Custom type h3cPfilterAclRuleCountStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("partialSuccess", 3),
          ("success", 1))
    )


_H3cPfilterAclRuleCountStatus_Type.__name__ = "Integer32"
_H3cPfilterAclRuleCountStatus_Object = MibTableColumn
h3cPfilterAclRuleCountStatus = _H3cPfilterAclRuleCountStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 4, 1, 3),
    _H3cPfilterAclRuleCountStatus_Type()
)
h3cPfilterAclRuleCountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPfilterAclRuleCountStatus.setStatus("current")
_H3cPfilterAclRuleMatchPackets_Type = Counter64
_H3cPfilterAclRuleMatchPackets_Object = MibTableColumn
h3cPfilterAclRuleMatchPackets = _H3cPfilterAclRuleMatchPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 4, 1, 4),
    _H3cPfilterAclRuleMatchPackets_Type()
)
h3cPfilterAclRuleMatchPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPfilterAclRuleMatchPackets.setStatus("current")
_H3cPfilterAclRuleMatchBytes_Type = Counter64
_H3cPfilterAclRuleMatchBytes_Object = MibTableColumn
h3cPfilterAclRuleMatchBytes = _H3cPfilterAclRuleMatchBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 4, 1, 5),
    _H3cPfilterAclRuleMatchBytes_Type()
)
h3cPfilterAclRuleMatchBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPfilterAclRuleMatchBytes.setStatus("current")
_H3cPfilterStatisticSumTable_Object = MibTable
h3cPfilterStatisticSumTable = _H3cPfilterStatisticSumTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 5)
)
if mibBuilder.loadTexts:
    h3cPfilterStatisticSumTable.setStatus("current")
_H3cPfilterStatisticSumEntry_Object = MibTableRow
h3cPfilterStatisticSumEntry = _H3cPfilterStatisticSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 5, 1)
)
h3cPfilterStatisticSumEntry.setIndexNames(
    (0, "H3C-ACL-MIB", "h3cPfilterSumDirection"),
    (0, "H3C-ACL-MIB", "h3cPfilterSumAclType"),
    (0, "H3C-ACL-MIB", "h3cPfilterSumAclIndex"),
    (0, "H3C-ACL-MIB", "h3cPfilterSumRuleIndex"),
)
if mibBuilder.loadTexts:
    h3cPfilterStatisticSumEntry.setStatus("current")
_H3cPfilterSumDirection_Type = DirectionType
_H3cPfilterSumDirection_Object = MibTableColumn
h3cPfilterSumDirection = _H3cPfilterSumDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 5, 1, 1),
    _H3cPfilterSumDirection_Type()
)
h3cPfilterSumDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPfilterSumDirection.setStatus("current")


class _H3cPfilterSumAclType_Type(Integer32):
    """Custom type h3cPfilterSumAclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_H3cPfilterSumAclType_Type.__name__ = "Integer32"
_H3cPfilterSumAclType_Object = MibTableColumn
h3cPfilterSumAclType = _H3cPfilterSumAclType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 5, 1, 2),
    _H3cPfilterSumAclType_Type()
)
h3cPfilterSumAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPfilterSumAclType.setStatus("current")


class _H3cPfilterSumAclIndex_Type(Integer32):
    """Custom type h3cPfilterSumAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 5999),
    )


_H3cPfilterSumAclIndex_Type.__name__ = "Integer32"
_H3cPfilterSumAclIndex_Object = MibTableColumn
h3cPfilterSumAclIndex = _H3cPfilterSumAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 5, 1, 3),
    _H3cPfilterSumAclIndex_Type()
)
h3cPfilterSumAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPfilterSumAclIndex.setStatus("current")


class _H3cPfilterSumRuleIndex_Type(Integer32):
    """Custom type h3cPfilterSumRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_H3cPfilterSumRuleIndex_Type.__name__ = "Integer32"
_H3cPfilterSumRuleIndex_Object = MibTableColumn
h3cPfilterSumRuleIndex = _H3cPfilterSumRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 5, 1, 4),
    _H3cPfilterSumRuleIndex_Type()
)
h3cPfilterSumRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPfilterSumRuleIndex.setStatus("current")
_H3cPfilterSumRuleMatchPackets_Type = Counter64
_H3cPfilterSumRuleMatchPackets_Object = MibTableColumn
h3cPfilterSumRuleMatchPackets = _H3cPfilterSumRuleMatchPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 5, 1, 5),
    _H3cPfilterSumRuleMatchPackets_Type()
)
h3cPfilterSumRuleMatchPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPfilterSumRuleMatchPackets.setStatus("current")
_H3cPfilterSumRuleMatchBytes_Type = Counter64
_H3cPfilterSumRuleMatchBytes_Object = MibTableColumn
h3cPfilterSumRuleMatchBytes = _H3cPfilterSumRuleMatchBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 3, 5, 1, 6),
    _H3cPfilterSumRuleMatchBytes_Type()
)
h3cPfilterSumRuleMatchBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPfilterSumRuleMatchBytes.setStatus("current")
_H3cAclPacketfilterTrapObjects_ObjectIdentity = ObjectIdentity
h3cAclPacketfilterTrapObjects = _H3cAclPacketfilterTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 4)
)
_H3cPfilterInterface_Type = OctetString
_H3cPfilterInterface_Object = MibScalar
h3cPfilterInterface = _H3cPfilterInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 4, 1),
    _H3cPfilterInterface_Type()
)
h3cPfilterInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPfilterInterface.setStatus("current")
_H3cPfilterDirection_Type = OctetString
_H3cPfilterDirection_Object = MibScalar
h3cPfilterDirection = _H3cPfilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 4, 2),
    _H3cPfilterDirection_Type()
)
h3cPfilterDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPfilterDirection.setStatus("current")
_H3cPfilterACLNumber_Type = Integer32
_H3cPfilterACLNumber_Object = MibScalar
h3cPfilterACLNumber = _H3cPfilterACLNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 4, 3),
    _H3cPfilterACLNumber_Type()
)
h3cPfilterACLNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPfilterACLNumber.setStatus("current")
_H3cPfilterAction_Type = OctetString
_H3cPfilterAction_Object = MibScalar
h3cPfilterAction = _H3cPfilterAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 4, 4),
    _H3cPfilterAction_Type()
)
h3cPfilterAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPfilterAction.setStatus("current")
_H3cMACfilterSourceMac_Type = OctetString
_H3cMACfilterSourceMac_Object = MibScalar
h3cMACfilterSourceMac = _H3cMACfilterSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 4, 5),
    _H3cMACfilterSourceMac_Type()
)
h3cMACfilterSourceMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cMACfilterSourceMac.setStatus("current")
_H3cMACfilterDestinationMac_Type = OctetString
_H3cMACfilterDestinationMac_Object = MibScalar
h3cMACfilterDestinationMac = _H3cMACfilterDestinationMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 4, 6),
    _H3cMACfilterDestinationMac_Type()
)
h3cMACfilterDestinationMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cMACfilterDestinationMac.setStatus("current")
_H3cPfilterPacketNumber_Type = Integer32
_H3cPfilterPacketNumber_Object = MibScalar
h3cPfilterPacketNumber = _H3cPfilterPacketNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 4, 7),
    _H3cPfilterPacketNumber_Type()
)
h3cPfilterPacketNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPfilterPacketNumber.setStatus("current")
_H3cPfilterReceiveInterface_Type = OctetString
_H3cPfilterReceiveInterface_Object = MibScalar
h3cPfilterReceiveInterface = _H3cPfilterReceiveInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 4, 8),
    _H3cPfilterReceiveInterface_Type()
)
h3cPfilterReceiveInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPfilterReceiveInterface.setStatus("current")
_H3cAclPacketfilterTrap_ObjectIdentity = ObjectIdentity
h3cAclPacketfilterTrap = _H3cAclPacketfilterTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 5)
)
_H3cPfilterTrapPrefix_ObjectIdentity = ObjectIdentity
h3cPfilterTrapPrefix = _H3cPfilterTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 5, 0)
)

# Managed Objects groups


# Notification objects

h3cMACfilterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 8, 5, 0, 1)
)
h3cMACfilterTrap.setObjects(
      *(("H3C-ACL-MIB", "h3cPfilterInterface"),
        ("H3C-ACL-MIB", "h3cPfilterDirection"),
        ("H3C-ACL-MIB", "h3cPfilterACLNumber"),
        ("H3C-ACL-MIB", "h3cPfilterAction"),
        ("H3C-ACL-MIB", "h3cMACfilterSourceMac"),
        ("H3C-ACL-MIB", "h3cMACfilterDestinationMac"),
        ("H3C-ACL-MIB", "h3cPfilterPacketNumber"),
        ("H3C-ACL-MIB", "h3cPfilterReceiveInterface"))
)
if mibBuilder.loadTexts:
    h3cMACfilterTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-ACL-MIB",
    **{"RuleAction": RuleAction,
       "CounterClear": CounterClear,
       "PortOp": PortOp,
       "DSCPValue": DSCPValue,
       "TCPFlag": TCPFlag,
       "FragmentFlag": FragmentFlag,
       "AddressFlag": AddressFlag,
       "DirectionType": DirectionType,
       "h3cAcl": h3cAcl,
       "h3cAclMibObjects": h3cAclMibObjects,
       "h3cAclMode": h3cAclMode,
       "h3cAclNumGroupTable": h3cAclNumGroupTable,
       "h3cAclNumGroupEntry": h3cAclNumGroupEntry,
       "h3cAclNumGroupAclNum": h3cAclNumGroupAclNum,
       "h3cAclNumGroupMatchOrder": h3cAclNumGroupMatchOrder,
       "h3cAclNumGroupSubitemNum": h3cAclNumGroupSubitemNum,
       "h3cAclNumGroupDescription": h3cAclNumGroupDescription,
       "h3cAclNumGroupCountClear": h3cAclNumGroupCountClear,
       "h3cAclNumGroupRowStatus": h3cAclNumGroupRowStatus,
       "h3cAclNameGroupTable": h3cAclNameGroupTable,
       "h3cAclNameGroupEntry": h3cAclNameGroupEntry,
       "h3cAclNameGroupIndex": h3cAclNameGroupIndex,
       "h3cAclNameGroupCreateName": h3cAclNameGroupCreateName,
       "h3cAclNameGroupTypes": h3cAclNameGroupTypes,
       "h3cAclNameGroupMatchOrder": h3cAclNameGroupMatchOrder,
       "h3cAclNameGroupSubitemNum": h3cAclNameGroupSubitemNum,
       "h3cAclNameGroupRowStatus": h3cAclNameGroupRowStatus,
       "h3cAclBasicRuleTable": h3cAclBasicRuleTable,
       "h3cAclBasicRuleEntry": h3cAclBasicRuleEntry,
       "h3cAclBasicAclNum": h3cAclBasicAclNum,
       "h3cAclBasicSubitem": h3cAclBasicSubitem,
       "h3cAclBasicAct": h3cAclBasicAct,
       "h3cAclBasicSrcIp": h3cAclBasicSrcIp,
       "h3cAclBasicSrcWild": h3cAclBasicSrcWild,
       "h3cAclBasicTimeRangeName": h3cAclBasicTimeRangeName,
       "h3cAclBasicFragments": h3cAclBasicFragments,
       "h3cAclBasicLog": h3cAclBasicLog,
       "h3cAclBasicEnable": h3cAclBasicEnable,
       "h3cAclBasicCount": h3cAclBasicCount,
       "h3cAclBasicCountClear": h3cAclBasicCountClear,
       "h3cAclBasicRowStatus": h3cAclBasicRowStatus,
       "h3cAclAdvancedRuleTable": h3cAclAdvancedRuleTable,
       "h3cAclAdvancedRuleEntry": h3cAclAdvancedRuleEntry,
       "h3cAclAdvancedAclNum": h3cAclAdvancedAclNum,
       "h3cAclAdvancedSubitem": h3cAclAdvancedSubitem,
       "h3cAclAdvancedAct": h3cAclAdvancedAct,
       "h3cAclAdvancedProtocol": h3cAclAdvancedProtocol,
       "h3cAclAdvancedSrcIp": h3cAclAdvancedSrcIp,
       "h3cAclAdvancedSrcWild": h3cAclAdvancedSrcWild,
       "h3cAclAdvancedSrcOp": h3cAclAdvancedSrcOp,
       "h3cAclAdvancedSrcPort1": h3cAclAdvancedSrcPort1,
       "h3cAclAdvancedSrcPort2": h3cAclAdvancedSrcPort2,
       "h3cAclAdvancedDestIp": h3cAclAdvancedDestIp,
       "h3cAclAdvancedDestWild": h3cAclAdvancedDestWild,
       "h3cAclAdvancedDestOp": h3cAclAdvancedDestOp,
       "h3cAclAdvancedDestPort1": h3cAclAdvancedDestPort1,
       "h3cAclAdvancedDestPort2": h3cAclAdvancedDestPort2,
       "h3cAclAdvancedPrecedence": h3cAclAdvancedPrecedence,
       "h3cAclAdvancedTos": h3cAclAdvancedTos,
       "h3cAclAdvancedDscp": h3cAclAdvancedDscp,
       "h3cAclAdvancedEstablish": h3cAclAdvancedEstablish,
       "h3cAclAdvancedTimeRangeName": h3cAclAdvancedTimeRangeName,
       "h3cAclAdvancedIcmpType": h3cAclAdvancedIcmpType,
       "h3cAclAdvancedIcmpCode": h3cAclAdvancedIcmpCode,
       "h3cAclAdvancedFragments": h3cAclAdvancedFragments,
       "h3cAclAdvancedLog": h3cAclAdvancedLog,
       "h3cAclAdvancedEnable": h3cAclAdvancedEnable,
       "h3cAclAdvancedCount": h3cAclAdvancedCount,
       "h3cAclAdvancedCountClear": h3cAclAdvancedCountClear,
       "h3cAclAdvancedRowStatus": h3cAclAdvancedRowStatus,
       "h3cAclIfRuleTable": h3cAclIfRuleTable,
       "h3cAclIfRuleEntry": h3cAclIfRuleEntry,
       "h3cAclIfAclNum": h3cAclIfAclNum,
       "h3cAclIfSubitem": h3cAclIfSubitem,
       "h3cAclIfAct": h3cAclIfAct,
       "h3cAclIfIndex": h3cAclIfIndex,
       "h3cAclIfAny": h3cAclIfAny,
       "h3cAclIfTimeRangeName": h3cAclIfTimeRangeName,
       "h3cAclIfLog": h3cAclIfLog,
       "h3cAclIfEnable": h3cAclIfEnable,
       "h3cAclIfCount": h3cAclIfCount,
       "h3cAclIfCountClear": h3cAclIfCountClear,
       "h3cAclIfRowStatus": h3cAclIfRowStatus,
       "h3cAclLinkTable": h3cAclLinkTable,
       "h3cAclLinkEntry": h3cAclLinkEntry,
       "h3cAclLinkAclNum": h3cAclLinkAclNum,
       "h3cAclLinkSubitem": h3cAclLinkSubitem,
       "h3cAclLinkAct": h3cAclLinkAct,
       "h3cAclLinkProtocol": h3cAclLinkProtocol,
       "h3cAclLinkFormatType": h3cAclLinkFormatType,
       "h3cAclLinkVlanTag": h3cAclLinkVlanTag,
       "h3cAclLinkVlanPri": h3cAclLinkVlanPri,
       "h3cAclLinkSrcVlanId": h3cAclLinkSrcVlanId,
       "h3cAclLinkSrcMac": h3cAclLinkSrcMac,
       "h3cAclLinkSrcMacWild": h3cAclLinkSrcMacWild,
       "h3cAclLinkSrcIfIndex": h3cAclLinkSrcIfIndex,
       "h3cAclLinkSrcAny": h3cAclLinkSrcAny,
       "h3cAclLinkDestVlanId": h3cAclLinkDestVlanId,
       "h3cAclLinkDestMac": h3cAclLinkDestMac,
       "h3cAclLinkDestMacWild": h3cAclLinkDestMacWild,
       "h3cAclLinkDestIfIndex": h3cAclLinkDestIfIndex,
       "h3cAclLinkDestAny": h3cAclLinkDestAny,
       "h3cAclLinkTimeRangeName": h3cAclLinkTimeRangeName,
       "h3cAclLinkEnable": h3cAclLinkEnable,
       "h3cAclLinkRowStatus": h3cAclLinkRowStatus,
       "h3cAclLinkTypeCode": h3cAclLinkTypeCode,
       "h3cAclLinkTypeMask": h3cAclLinkTypeMask,
       "h3cAclLinkLsapCode": h3cAclLinkLsapCode,
       "h3cAclLinkLsapMask": h3cAclLinkLsapMask,
       "h3cAclLinkL2LabelRangeOp": h3cAclLinkL2LabelRangeOp,
       "h3cAclLinkL2LabelRangeBegin": h3cAclLinkL2LabelRangeBegin,
       "h3cAclLinkL2LabelRangeEnd": h3cAclLinkL2LabelRangeEnd,
       "h3cAclLinkMplsExp": h3cAclLinkMplsExp,
       "h3cAclUserTable": h3cAclUserTable,
       "h3cAclUserEntry": h3cAclUserEntry,
       "h3cAclUserAclNum": h3cAclUserAclNum,
       "h3cAclUserSubitem": h3cAclUserSubitem,
       "h3cAclUserAct": h3cAclUserAct,
       "h3cAclUserFormatType": h3cAclUserFormatType,
       "h3cAclUserVlanTag": h3cAclUserVlanTag,
       "h3cAclUserRuleStr": h3cAclUserRuleStr,
       "h3cAclUserRuleMask": h3cAclUserRuleMask,
       "h3cAclUserTimeRangeName": h3cAclUserTimeRangeName,
       "h3cAclUserEnable": h3cAclUserEnable,
       "h3cAclUserRowStatus": h3cAclUserRowStatus,
       "h3cAclActiveTable": h3cAclActiveTable,
       "h3cAclActiveEntry": h3cAclActiveEntry,
       "h3cAclActiveAclIndex": h3cAclActiveAclIndex,
       "h3cAclActiveIfIndex": h3cAclActiveIfIndex,
       "h3cAclActiveVlanID": h3cAclActiveVlanID,
       "h3cAclActiveDirection": h3cAclActiveDirection,
       "h3cAclActiveUserAclNum": h3cAclActiveUserAclNum,
       "h3cAclActiveUserAclSubitem": h3cAclActiveUserAclSubitem,
       "h3cAclActiveIpAclNum": h3cAclActiveIpAclNum,
       "h3cAclActiveIpAclSubitem": h3cAclActiveIpAclSubitem,
       "h3cAclActiveLinkAclNum": h3cAclActiveLinkAclNum,
       "h3cAclActiveLinkAclSubitem": h3cAclActiveLinkAclSubitem,
       "h3cAclActiveRuntime": h3cAclActiveRuntime,
       "h3cAclActiveRowStatus": h3cAclActiveRowStatus,
       "h3cAclIDSTable": h3cAclIDSTable,
       "h3cAclIDSEntry": h3cAclIDSEntry,
       "h3cAclIDSName": h3cAclIDSName,
       "h3cAclIDSSrcMac": h3cAclIDSSrcMac,
       "h3cAclIDSDestMac": h3cAclIDSDestMac,
       "h3cAclIDSSrcIp": h3cAclIDSSrcIp,
       "h3cAclIDSSrcWild": h3cAclIDSSrcWild,
       "h3cAclIDSDestIp": h3cAclIDSDestIp,
       "h3cAclIDSDestWild": h3cAclIDSDestWild,
       "h3cAclIDSSrcPort": h3cAclIDSSrcPort,
       "h3cAclIDSDestPort": h3cAclIDSDestPort,
       "h3cAclIDSProtocol": h3cAclIDSProtocol,
       "h3cAclIDSDenyTime": h3cAclIDSDenyTime,
       "h3cAclIDSAct": h3cAclIDSAct,
       "h3cAclIDSRowStatus": h3cAclIDSRowStatus,
       "h3cAclMib2Objects": h3cAclMib2Objects,
       "h3cAclMib2GlobalGroup": h3cAclMib2GlobalGroup,
       "h3cAclMib2NodesGroup": h3cAclMib2NodesGroup,
       "h3cAclMib2Mode": h3cAclMib2Mode,
       "h3cAclMib2Version": h3cAclMib2Version,
       "h3cAclMib2ObjectsCapabilities": h3cAclMib2ObjectsCapabilities,
       "h3cAclMib2ProcessingStatus": h3cAclMib2ProcessingStatus,
       "h3cAclMib2CapabilityTable": h3cAclMib2CapabilityTable,
       "h3cAclMib2CapabilityEntry": h3cAclMib2CapabilityEntry,
       "h3cAclMib2EntityType": h3cAclMib2EntityType,
       "h3cAclMib2EntityIndex": h3cAclMib2EntityIndex,
       "h3cAclMib2ModuleIndex": h3cAclMib2ModuleIndex,
       "h3cAclMib2CharacteristicsIndex": h3cAclMib2CharacteristicsIndex,
       "h3cAclMib2CharacteristicsDesc": h3cAclMib2CharacteristicsDesc,
       "h3cAclMib2CharacteristicsValue": h3cAclMib2CharacteristicsValue,
       "h3cAclNumberGroupTable": h3cAclNumberGroupTable,
       "h3cAclNumberGroupEntry": h3cAclNumberGroupEntry,
       "h3cAclNumberGroupType": h3cAclNumberGroupType,
       "h3cAclNumberGroupIndex": h3cAclNumberGroupIndex,
       "h3cAclNumberGroupRowStatus": h3cAclNumberGroupRowStatus,
       "h3cAclNumberGroupMatchOrder": h3cAclNumberGroupMatchOrder,
       "h3cAclNumberGroupStep": h3cAclNumberGroupStep,
       "h3cAclNumberGroupDescription": h3cAclNumberGroupDescription,
       "h3cAclNumberGroupCountClear": h3cAclNumberGroupCountClear,
       "h3cAclNumberGroupRuleCounter": h3cAclNumberGroupRuleCounter,
       "h3cAclNumberGroupName": h3cAclNumberGroupName,
       "h3cAclIPAclGroup": h3cAclIPAclGroup,
       "h3cAclIPAclBasicTable": h3cAclIPAclBasicTable,
       "h3cAclIPAclBasicEntry": h3cAclIPAclBasicEntry,
       "h3cAclIPAclBasicRuleIndex": h3cAclIPAclBasicRuleIndex,
       "h3cAclIPAclBasicRowStatus": h3cAclIPAclBasicRowStatus,
       "h3cAclIPAclBasicAct": h3cAclIPAclBasicAct,
       "h3cAclIPAclBasicSrcAddrType": h3cAclIPAclBasicSrcAddrType,
       "h3cAclIPAclBasicSrcAddr": h3cAclIPAclBasicSrcAddr,
       "h3cAclIPAclBasicSrcPrefix": h3cAclIPAclBasicSrcPrefix,
       "h3cAclIPAclBasicSrcAny": h3cAclIPAclBasicSrcAny,
       "h3cAclIPAclBasicSrcWild": h3cAclIPAclBasicSrcWild,
       "h3cAclIPAclBasicTimeRangeName": h3cAclIPAclBasicTimeRangeName,
       "h3cAclIPAclBasicFragmentFlag": h3cAclIPAclBasicFragmentFlag,
       "h3cAclIPAclBasicLog": h3cAclIPAclBasicLog,
       "h3cAclIPAclBasicCount": h3cAclIPAclBasicCount,
       "h3cAclIPAclBasicCountClear": h3cAclIPAclBasicCountClear,
       "h3cAclIPAclBasicEnable": h3cAclIPAclBasicEnable,
       "h3cAclIPAclBasicVpnInstanceName": h3cAclIPAclBasicVpnInstanceName,
       "h3cAclIPAclBasicComment": h3cAclIPAclBasicComment,
       "h3cAclIPAclBasicCounting": h3cAclIPAclBasicCounting,
       "h3cAclIPAclBasicRouteTypeAny": h3cAclIPAclBasicRouteTypeAny,
       "h3cAclIPAclBasicRouteTypeValue": h3cAclIPAclBasicRouteTypeValue,
       "h3cAclIPAclAdvancedTable": h3cAclIPAclAdvancedTable,
       "h3cAclIPAclAdvancedEntry": h3cAclIPAclAdvancedEntry,
       "h3cAclIPAclAdvancedRuleIndex": h3cAclIPAclAdvancedRuleIndex,
       "h3cAclIPAclAdvancedRowStatus": h3cAclIPAclAdvancedRowStatus,
       "h3cAclIPAclAdvancedAct": h3cAclIPAclAdvancedAct,
       "h3cAclIPAclAdvancedProtocol": h3cAclIPAclAdvancedProtocol,
       "h3cAclIPAclAdvancedAddrFlag": h3cAclIPAclAdvancedAddrFlag,
       "h3cAclIPAclAdvancedSrcAddrType": h3cAclIPAclAdvancedSrcAddrType,
       "h3cAclIPAclAdvancedSrcAddr": h3cAclIPAclAdvancedSrcAddr,
       "h3cAclIPAclAdvancedSrcPrefix": h3cAclIPAclAdvancedSrcPrefix,
       "h3cAclIPAclAdvancedSrcAny": h3cAclIPAclAdvancedSrcAny,
       "h3cAclIPAclAdvancedSrcWild": h3cAclIPAclAdvancedSrcWild,
       "h3cAclIPAclAdvancedSrcOp": h3cAclIPAclAdvancedSrcOp,
       "h3cAclIPAclAdvancedSrcPort1": h3cAclIPAclAdvancedSrcPort1,
       "h3cAclIPAclAdvancedSrcPort2": h3cAclIPAclAdvancedSrcPort2,
       "h3cAclIPAclAdvancedDestAddrType": h3cAclIPAclAdvancedDestAddrType,
       "h3cAclIPAclAdvancedDestAddr": h3cAclIPAclAdvancedDestAddr,
       "h3cAclIPAclAdvancedDestPrefix": h3cAclIPAclAdvancedDestPrefix,
       "h3cAclIPAclAdvancedDestAny": h3cAclIPAclAdvancedDestAny,
       "h3cAclIPAclAdvancedDestWild": h3cAclIPAclAdvancedDestWild,
       "h3cAclIPAclAdvancedDestOp": h3cAclIPAclAdvancedDestOp,
       "h3cAclIPAclAdvancedDestPort1": h3cAclIPAclAdvancedDestPort1,
       "h3cAclIPAclAdvancedDestPort2": h3cAclIPAclAdvancedDestPort2,
       "h3cAclIPAclAdvancedIcmpType": h3cAclIPAclAdvancedIcmpType,
       "h3cAclIPAclAdvancedIcmpCode": h3cAclIPAclAdvancedIcmpCode,
       "h3cAclIPAclAdvancedPrecedence": h3cAclIPAclAdvancedPrecedence,
       "h3cAclIPAclAdvancedTos": h3cAclIPAclAdvancedTos,
       "h3cAclIPAclAdvancedDscp": h3cAclIPAclAdvancedDscp,
       "h3cAclIPAclAdvancedTimeRangeName": h3cAclIPAclAdvancedTimeRangeName,
       "h3cAclIPAclAdvancedTCPFlag": h3cAclIPAclAdvancedTCPFlag,
       "h3cAclIPAclAdvancedFragmentFlag": h3cAclIPAclAdvancedFragmentFlag,
       "h3cAclIPAclAdvancedLog": h3cAclIPAclAdvancedLog,
       "h3cAclIPAclAdvancedCount": h3cAclIPAclAdvancedCount,
       "h3cAclIPAclAdvancedCountClear": h3cAclIPAclAdvancedCountClear,
       "h3cAclIPAclAdvancedEnable": h3cAclIPAclAdvancedEnable,
       "h3cAclIPAclAdvancedVpnInstanceName": h3cAclIPAclAdvancedVpnInstanceName,
       "h3cAclIPAclAdvancedComment": h3cAclIPAclAdvancedComment,
       "h3cAclIPAclAdvancedReflective": h3cAclIPAclAdvancedReflective,
       "h3cAclIPAclAdvancedCounting": h3cAclIPAclAdvancedCounting,
       "h3cAclIPAclAdvancedTCPFlagMask": h3cAclIPAclAdvancedTCPFlagMask,
       "h3cAclIPAclAdvancedTCPFlagValue": h3cAclIPAclAdvancedTCPFlagValue,
       "h3cAclIPAclAdvancedRouteTypeAny": h3cAclIPAclAdvancedRouteTypeAny,
       "h3cAclIPAclAdvancedRouteTypeValue": h3cAclIPAclAdvancedRouteTypeValue,
       "h3cAclIPAclAdvancedFlowLabel": h3cAclIPAclAdvancedFlowLabel,
       "h3cAclMACAclGroup": h3cAclMACAclGroup,
       "h3cAclMACTable": h3cAclMACTable,
       "h3cAclMACEntry": h3cAclMACEntry,
       "h3cAclMACRuleIndex": h3cAclMACRuleIndex,
       "h3cAclMACRowStatus": h3cAclMACRowStatus,
       "h3cAclMACAct": h3cAclMACAct,
       "h3cAclMACTypeCode": h3cAclMACTypeCode,
       "h3cAclMACTypeMask": h3cAclMACTypeMask,
       "h3cAclMACSrcMac": h3cAclMACSrcMac,
       "h3cAclMACSrcMacWild": h3cAclMACSrcMacWild,
       "h3cAclMACDestMac": h3cAclMACDestMac,
       "h3cAclMACDestMacWild": h3cAclMACDestMacWild,
       "h3cAclMACLsapCode": h3cAclMACLsapCode,
       "h3cAclMACLsapMask": h3cAclMACLsapMask,
       "h3cAclMACCos": h3cAclMACCos,
       "h3cAclMACTimeRangeName": h3cAclMACTimeRangeName,
       "h3cAclMACCount": h3cAclMACCount,
       "h3cAclMACCountClear": h3cAclMACCountClear,
       "h3cAclMACEnable": h3cAclMACEnable,
       "h3cAclMACComment": h3cAclMACComment,
       "h3cAclMACLog": h3cAclMACLog,
       "h3cAclMACCounting": h3cAclMACCounting,
       "h3cAclEnUserAclGroup": h3cAclEnUserAclGroup,
       "h3cAclEnUserTable": h3cAclEnUserTable,
       "h3cAclEnUserEntry": h3cAclEnUserEntry,
       "h3cAclEnUserRuleIndex": h3cAclEnUserRuleIndex,
       "h3cAclEnUserRowStatus": h3cAclEnUserRowStatus,
       "h3cAclEnUserAct": h3cAclEnUserAct,
       "h3cAclEnUserStartString": h3cAclEnUserStartString,
       "h3cAclEnUserL2String": h3cAclEnUserL2String,
       "h3cAclEnUserMplsString": h3cAclEnUserMplsString,
       "h3cAclEnUserIPv4String": h3cAclEnUserIPv4String,
       "h3cAclEnUserIPv6String": h3cAclEnUserIPv6String,
       "h3cAclEnUserL4String": h3cAclEnUserL4String,
       "h3cAclEnUserL5String": h3cAclEnUserL5String,
       "h3cAclEnUserTimeRangeName": h3cAclEnUserTimeRangeName,
       "h3cAclEnUserCount": h3cAclEnUserCount,
       "h3cAclEnUserCountClear": h3cAclEnUserCountClear,
       "h3cAclEnUserEnable": h3cAclEnUserEnable,
       "h3cAclEnUserComment": h3cAclEnUserComment,
       "h3cAclEnUserLog": h3cAclEnUserLog,
       "h3cAclEnUserCounting": h3cAclEnUserCounting,
       "h3cAclResourceGroup": h3cAclResourceGroup,
       "h3cAclResourceUsageTable": h3cAclResourceUsageTable,
       "h3cAclResourceUsageEntry": h3cAclResourceUsageEntry,
       "h3cAclResourceChassis": h3cAclResourceChassis,
       "h3cAclResourceSlot": h3cAclResourceSlot,
       "h3cAclResourceChip": h3cAclResourceChip,
       "h3cAclResourceType": h3cAclResourceType,
       "h3cAclPortRange": h3cAclPortRange,
       "h3cAclResourceTotal": h3cAclResourceTotal,
       "h3cAclResourceReserved": h3cAclResourceReserved,
       "h3cAclResourceConfigured": h3cAclResourceConfigured,
       "h3cAclResourceUsagePercent": h3cAclResourceUsagePercent,
       "h3cAclResourceTypeDescription": h3cAclResourceTypeDescription,
       "h3cAclPacketFilterObjects": h3cAclPacketFilterObjects,
       "h3cPfilterScalarGroup": h3cPfilterScalarGroup,
       "h3cPfilterDefaultAction": h3cPfilterDefaultAction,
       "h3cPfilterProcessingStatus": h3cPfilterProcessingStatus,
       "h3cPfilterApplyTable": h3cPfilterApplyTable,
       "h3cPfilterApplyEntry": h3cPfilterApplyEntry,
       "h3cPfilterApplyObjType": h3cPfilterApplyObjType,
       "h3cPfilterApplyObjIndex": h3cPfilterApplyObjIndex,
       "h3cPfilterApplyDirection": h3cPfilterApplyDirection,
       "h3cPfilterApplyAclType": h3cPfilterApplyAclType,
       "h3cPfilterApplyAclIndex": h3cPfilterApplyAclIndex,
       "h3cPfilterApplyHardCount": h3cPfilterApplyHardCount,
       "h3cPfilterApplySequence": h3cPfilterApplySequence,
       "h3cPfilterApplyCountClear": h3cPfilterApplyCountClear,
       "h3cPfilterApplyRowStatus": h3cPfilterApplyRowStatus,
       "h3cPfilterAclGroupRunInfoTable": h3cPfilterAclGroupRunInfoTable,
       "h3cPfilterAclGroupRunInfoEntry": h3cPfilterAclGroupRunInfoEntry,
       "h3cPfilterAclGroupStatus": h3cPfilterAclGroupStatus,
       "h3cPfilterAclGroupCountStatus": h3cPfilterAclGroupCountStatus,
       "h3cPfilterAclGroupPermitPkts": h3cPfilterAclGroupPermitPkts,
       "h3cPfilterAclGroupPermitBytes": h3cPfilterAclGroupPermitBytes,
       "h3cPfilterAclGroupDenyPkts": h3cPfilterAclGroupDenyPkts,
       "h3cPfilterAclGroupDenyBytes": h3cPfilterAclGroupDenyBytes,
       "h3cPfilterAclRuleRunInfoTable": h3cPfilterAclRuleRunInfoTable,
       "h3cPfilterAclRuleRunInfoEntry": h3cPfilterAclRuleRunInfoEntry,
       "h3cPfilterAclRuleIndex": h3cPfilterAclRuleIndex,
       "h3cPfilterAclRuleStatus": h3cPfilterAclRuleStatus,
       "h3cPfilterAclRuleCountStatus": h3cPfilterAclRuleCountStatus,
       "h3cPfilterAclRuleMatchPackets": h3cPfilterAclRuleMatchPackets,
       "h3cPfilterAclRuleMatchBytes": h3cPfilterAclRuleMatchBytes,
       "h3cPfilterStatisticSumTable": h3cPfilterStatisticSumTable,
       "h3cPfilterStatisticSumEntry": h3cPfilterStatisticSumEntry,
       "h3cPfilterSumDirection": h3cPfilterSumDirection,
       "h3cPfilterSumAclType": h3cPfilterSumAclType,
       "h3cPfilterSumAclIndex": h3cPfilterSumAclIndex,
       "h3cPfilterSumRuleIndex": h3cPfilterSumRuleIndex,
       "h3cPfilterSumRuleMatchPackets": h3cPfilterSumRuleMatchPackets,
       "h3cPfilterSumRuleMatchBytes": h3cPfilterSumRuleMatchBytes,
       "h3cAclPacketfilterTrapObjects": h3cAclPacketfilterTrapObjects,
       "h3cPfilterInterface": h3cPfilterInterface,
       "h3cPfilterDirection": h3cPfilterDirection,
       "h3cPfilterACLNumber": h3cPfilterACLNumber,
       "h3cPfilterAction": h3cPfilterAction,
       "h3cMACfilterSourceMac": h3cMACfilterSourceMac,
       "h3cMACfilterDestinationMac": h3cMACfilterDestinationMac,
       "h3cPfilterPacketNumber": h3cPfilterPacketNumber,
       "h3cPfilterReceiveInterface": h3cPfilterReceiveInterface,
       "h3cAclPacketfilterTrap": h3cAclPacketfilterTrap,
       "h3cPfilterTrapPrefix": h3cPfilterTrapPrefix,
       "h3cMACfilterTrap": h3cMACfilterTrap}
)
