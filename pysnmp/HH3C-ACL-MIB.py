# SNMP MIB module (HH3C-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-ACL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:27 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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

hh3cAcl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8)
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



# MIB Managed Objects in the order of their OIDs

_Hh3cAclMibObjects_ObjectIdentity = ObjectIdentity
hh3cAclMibObjects = _Hh3cAclMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1)
)


class _Hh3cAclMode_Type(Integer32):
    """Custom type hh3cAclMode based on Integer32"""
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


_Hh3cAclMode_Type.__name__ = "Integer32"
_Hh3cAclMode_Object = MibScalar
hh3cAclMode = _Hh3cAclMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 1),
    _Hh3cAclMode_Type()
)
hh3cAclMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAclMode.setStatus("current")
_Hh3cAclNumGroupTable_Object = MibTable
hh3cAclNumGroupTable = _Hh3cAclNumGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cAclNumGroupTable.setStatus("current")
_Hh3cAclNumGroupEntry_Object = MibTableRow
hh3cAclNumGroupEntry = _Hh3cAclNumGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 2, 1)
)
hh3cAclNumGroupEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclNumGroupAclNum"),
)
if mibBuilder.loadTexts:
    hh3cAclNumGroupEntry.setStatus("current")


class _Hh3cAclNumGroupAclNum_Type(Integer32):
    """Custom type hh3cAclNumGroupAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 5999),
    )


_Hh3cAclNumGroupAclNum_Type.__name__ = "Integer32"
_Hh3cAclNumGroupAclNum_Object = MibTableColumn
hh3cAclNumGroupAclNum = _Hh3cAclNumGroupAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 2, 1, 1),
    _Hh3cAclNumGroupAclNum_Type()
)
hh3cAclNumGroupAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclNumGroupAclNum.setStatus("current")


class _Hh3cAclNumGroupMatchOrder_Type(Integer32):
    """Custom type hh3cAclNumGroupMatchOrder based on Integer32"""
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


_Hh3cAclNumGroupMatchOrder_Type.__name__ = "Integer32"
_Hh3cAclNumGroupMatchOrder_Object = MibTableColumn
hh3cAclNumGroupMatchOrder = _Hh3cAclNumGroupMatchOrder_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 2, 1, 2),
    _Hh3cAclNumGroupMatchOrder_Type()
)
hh3cAclNumGroupMatchOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNumGroupMatchOrder.setStatus("current")
_Hh3cAclNumGroupSubitemNum_Type = Integer32
_Hh3cAclNumGroupSubitemNum_Object = MibTableColumn
hh3cAclNumGroupSubitemNum = _Hh3cAclNumGroupSubitemNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 2, 1, 3),
    _Hh3cAclNumGroupSubitemNum_Type()
)
hh3cAclNumGroupSubitemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclNumGroupSubitemNum.setStatus("current")


class _Hh3cAclNumGroupDescription_Type(OctetString):
    """Custom type hh3cAclNumGroupDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cAclNumGroupDescription_Type.__name__ = "OctetString"
_Hh3cAclNumGroupDescription_Object = MibTableColumn
hh3cAclNumGroupDescription = _Hh3cAclNumGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 2, 1, 4),
    _Hh3cAclNumGroupDescription_Type()
)
hh3cAclNumGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAclNumGroupDescription.setStatus("current")


class _Hh3cAclNumGroupCountClear_Type(Integer32):
    """Custom type hh3cAclNumGroupCountClear based on Integer32"""
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


_Hh3cAclNumGroupCountClear_Type.__name__ = "Integer32"
_Hh3cAclNumGroupCountClear_Object = MibTableColumn
hh3cAclNumGroupCountClear = _Hh3cAclNumGroupCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 2, 1, 5),
    _Hh3cAclNumGroupCountClear_Type()
)
hh3cAclNumGroupCountClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNumGroupCountClear.setStatus("current")
_Hh3cAclNumGroupRowStatus_Type = RowStatus
_Hh3cAclNumGroupRowStatus_Object = MibTableColumn
hh3cAclNumGroupRowStatus = _Hh3cAclNumGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 2, 1, 6),
    _Hh3cAclNumGroupRowStatus_Type()
)
hh3cAclNumGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNumGroupRowStatus.setStatus("current")
_Hh3cAclNameGroupTable_Object = MibTable
hh3cAclNameGroupTable = _Hh3cAclNameGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cAclNameGroupTable.setStatus("current")
_Hh3cAclNameGroupEntry_Object = MibTableRow
hh3cAclNameGroupEntry = _Hh3cAclNameGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 3, 1)
)
hh3cAclNameGroupEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclNameGroupIndex"),
)
if mibBuilder.loadTexts:
    hh3cAclNameGroupEntry.setStatus("current")


class _Hh3cAclNameGroupIndex_Type(Integer32):
    """Custom type hh3cAclNameGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cAclNameGroupIndex_Type.__name__ = "Integer32"
_Hh3cAclNameGroupIndex_Object = MibTableColumn
hh3cAclNameGroupIndex = _Hh3cAclNameGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 3, 1, 1),
    _Hh3cAclNameGroupIndex_Type()
)
hh3cAclNameGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclNameGroupIndex.setStatus("current")


class _Hh3cAclNameGroupCreateName_Type(OctetString):
    """Custom type hh3cAclNameGroupCreateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclNameGroupCreateName_Type.__name__ = "OctetString"
_Hh3cAclNameGroupCreateName_Object = MibTableColumn
hh3cAclNameGroupCreateName = _Hh3cAclNameGroupCreateName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 3, 1, 2),
    _Hh3cAclNameGroupCreateName_Type()
)
hh3cAclNameGroupCreateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNameGroupCreateName.setStatus("current")


class _Hh3cAclNameGroupTypes_Type(Integer32):
    """Custom type hh3cAclNameGroupTypes based on Integer32"""
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


_Hh3cAclNameGroupTypes_Type.__name__ = "Integer32"
_Hh3cAclNameGroupTypes_Object = MibTableColumn
hh3cAclNameGroupTypes = _Hh3cAclNameGroupTypes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 3, 1, 3),
    _Hh3cAclNameGroupTypes_Type()
)
hh3cAclNameGroupTypes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNameGroupTypes.setStatus("current")


class _Hh3cAclNameGroupMatchOrder_Type(Integer32):
    """Custom type hh3cAclNameGroupMatchOrder based on Integer32"""
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


_Hh3cAclNameGroupMatchOrder_Type.__name__ = "Integer32"
_Hh3cAclNameGroupMatchOrder_Object = MibTableColumn
hh3cAclNameGroupMatchOrder = _Hh3cAclNameGroupMatchOrder_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 3, 1, 4),
    _Hh3cAclNameGroupMatchOrder_Type()
)
hh3cAclNameGroupMatchOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNameGroupMatchOrder.setStatus("current")


class _Hh3cAclNameGroupSubitemNum_Type(Integer32):
    """Custom type hh3cAclNameGroupSubitemNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Hh3cAclNameGroupSubitemNum_Type.__name__ = "Integer32"
_Hh3cAclNameGroupSubitemNum_Object = MibTableColumn
hh3cAclNameGroupSubitemNum = _Hh3cAclNameGroupSubitemNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 3, 1, 5),
    _Hh3cAclNameGroupSubitemNum_Type()
)
hh3cAclNameGroupSubitemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclNameGroupSubitemNum.setStatus("current")
_Hh3cAclNameGroupRowStatus_Type = RowStatus
_Hh3cAclNameGroupRowStatus_Object = MibTableColumn
hh3cAclNameGroupRowStatus = _Hh3cAclNameGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 3, 1, 6),
    _Hh3cAclNameGroupRowStatus_Type()
)
hh3cAclNameGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNameGroupRowStatus.setStatus("current")
_Hh3cAclBasicRuleTable_Object = MibTable
hh3cAclBasicRuleTable = _Hh3cAclBasicRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cAclBasicRuleTable.setStatus("current")
_Hh3cAclBasicRuleEntry_Object = MibTableRow
hh3cAclBasicRuleEntry = _Hh3cAclBasicRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1)
)
hh3cAclBasicRuleEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclBasicAclNum"),
    (0, "HH3C-ACL-MIB", "hh3cAclBasicSubitem"),
)
if mibBuilder.loadTexts:
    hh3cAclBasicRuleEntry.setStatus("current")


class _Hh3cAclBasicAclNum_Type(Integer32):
    """Custom type hh3cAclBasicAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cAclBasicAclNum_Type.__name__ = "Integer32"
_Hh3cAclBasicAclNum_Object = MibTableColumn
hh3cAclBasicAclNum = _Hh3cAclBasicAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1, 1),
    _Hh3cAclBasicAclNum_Type()
)
hh3cAclBasicAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclBasicAclNum.setStatus("current")


class _Hh3cAclBasicSubitem_Type(Integer32):
    """Custom type hh3cAclBasicSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclBasicSubitem_Type.__name__ = "Integer32"
_Hh3cAclBasicSubitem_Object = MibTableColumn
hh3cAclBasicSubitem = _Hh3cAclBasicSubitem_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1, 2),
    _Hh3cAclBasicSubitem_Type()
)
hh3cAclBasicSubitem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclBasicSubitem.setStatus("current")


class _Hh3cAclBasicAct_Type(Integer32):
    """Custom type hh3cAclBasicAct based on Integer32"""
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


_Hh3cAclBasicAct_Type.__name__ = "Integer32"
_Hh3cAclBasicAct_Object = MibTableColumn
hh3cAclBasicAct = _Hh3cAclBasicAct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1, 3),
    _Hh3cAclBasicAct_Type()
)
hh3cAclBasicAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclBasicAct.setStatus("current")
_Hh3cAclBasicSrcIp_Type = IpAddress
_Hh3cAclBasicSrcIp_Object = MibTableColumn
hh3cAclBasicSrcIp = _Hh3cAclBasicSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1, 4),
    _Hh3cAclBasicSrcIp_Type()
)
hh3cAclBasicSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclBasicSrcIp.setStatus("current")
_Hh3cAclBasicSrcWild_Type = IpAddress
_Hh3cAclBasicSrcWild_Object = MibTableColumn
hh3cAclBasicSrcWild = _Hh3cAclBasicSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1, 5),
    _Hh3cAclBasicSrcWild_Type()
)
hh3cAclBasicSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclBasicSrcWild.setStatus("current")


class _Hh3cAclBasicTimeRangeName_Type(OctetString):
    """Custom type hh3cAclBasicTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclBasicTimeRangeName_Type.__name__ = "OctetString"
_Hh3cAclBasicTimeRangeName_Object = MibTableColumn
hh3cAclBasicTimeRangeName = _Hh3cAclBasicTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1, 6),
    _Hh3cAclBasicTimeRangeName_Type()
)
hh3cAclBasicTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclBasicTimeRangeName.setStatus("current")
_Hh3cAclBasicFragments_Type = TruthValue
_Hh3cAclBasicFragments_Object = MibTableColumn
hh3cAclBasicFragments = _Hh3cAclBasicFragments_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1, 7),
    _Hh3cAclBasicFragments_Type()
)
hh3cAclBasicFragments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclBasicFragments.setStatus("current")
_Hh3cAclBasicLog_Type = TruthValue
_Hh3cAclBasicLog_Object = MibTableColumn
hh3cAclBasicLog = _Hh3cAclBasicLog_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1, 8),
    _Hh3cAclBasicLog_Type()
)
hh3cAclBasicLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclBasicLog.setStatus("current")
_Hh3cAclBasicEnable_Type = TruthValue
_Hh3cAclBasicEnable_Object = MibTableColumn
hh3cAclBasicEnable = _Hh3cAclBasicEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1, 9),
    _Hh3cAclBasicEnable_Type()
)
hh3cAclBasicEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclBasicEnable.setStatus("current")
_Hh3cAclBasicCount_Type = Counter32
_Hh3cAclBasicCount_Object = MibTableColumn
hh3cAclBasicCount = _Hh3cAclBasicCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1, 10),
    _Hh3cAclBasicCount_Type()
)
hh3cAclBasicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclBasicCount.setStatus("current")


class _Hh3cAclBasicCountClear_Type(Integer32):
    """Custom type hh3cAclBasicCountClear based on Integer32"""
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


_Hh3cAclBasicCountClear_Type.__name__ = "Integer32"
_Hh3cAclBasicCountClear_Object = MibTableColumn
hh3cAclBasicCountClear = _Hh3cAclBasicCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1, 11),
    _Hh3cAclBasicCountClear_Type()
)
hh3cAclBasicCountClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclBasicCountClear.setStatus("current")
_Hh3cAclBasicRowStatus_Type = RowStatus
_Hh3cAclBasicRowStatus_Object = MibTableColumn
hh3cAclBasicRowStatus = _Hh3cAclBasicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1, 12),
    _Hh3cAclBasicRowStatus_Type()
)
hh3cAclBasicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclBasicRowStatus.setStatus("current")
_Hh3cAclAdvancedRuleTable_Object = MibTable
hh3cAclAdvancedRuleTable = _Hh3cAclAdvancedRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cAclAdvancedRuleTable.setStatus("current")
_Hh3cAclAdvancedRuleEntry_Object = MibTableRow
hh3cAclAdvancedRuleEntry = _Hh3cAclAdvancedRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1)
)
hh3cAclAdvancedRuleEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclAdvancedAclNum"),
    (0, "HH3C-ACL-MIB", "hh3cAclAdvancedSubitem"),
)
if mibBuilder.loadTexts:
    hh3cAclAdvancedRuleEntry.setStatus("current")


class _Hh3cAclAdvancedAclNum_Type(Integer32):
    """Custom type hh3cAclAdvancedAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cAclAdvancedAclNum_Type.__name__ = "Integer32"
_Hh3cAclAdvancedAclNum_Object = MibTableColumn
hh3cAclAdvancedAclNum = _Hh3cAclAdvancedAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 1),
    _Hh3cAclAdvancedAclNum_Type()
)
hh3cAclAdvancedAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclAdvancedAclNum.setStatus("current")


class _Hh3cAclAdvancedSubitem_Type(Integer32):
    """Custom type hh3cAclAdvancedSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclAdvancedSubitem_Type.__name__ = "Integer32"
_Hh3cAclAdvancedSubitem_Object = MibTableColumn
hh3cAclAdvancedSubitem = _Hh3cAclAdvancedSubitem_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 2),
    _Hh3cAclAdvancedSubitem_Type()
)
hh3cAclAdvancedSubitem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclAdvancedSubitem.setStatus("current")


class _Hh3cAclAdvancedAct_Type(Integer32):
    """Custom type hh3cAclAdvancedAct based on Integer32"""
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


_Hh3cAclAdvancedAct_Type.__name__ = "Integer32"
_Hh3cAclAdvancedAct_Object = MibTableColumn
hh3cAclAdvancedAct = _Hh3cAclAdvancedAct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 3),
    _Hh3cAclAdvancedAct_Type()
)
hh3cAclAdvancedAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedAct.setStatus("current")


class _Hh3cAclAdvancedProtocol_Type(Integer32):
    """Custom type hh3cAclAdvancedProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cAclAdvancedProtocol_Type.__name__ = "Integer32"
_Hh3cAclAdvancedProtocol_Object = MibTableColumn
hh3cAclAdvancedProtocol = _Hh3cAclAdvancedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 4),
    _Hh3cAclAdvancedProtocol_Type()
)
hh3cAclAdvancedProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedProtocol.setStatus("current")
_Hh3cAclAdvancedSrcIp_Type = IpAddress
_Hh3cAclAdvancedSrcIp_Object = MibTableColumn
hh3cAclAdvancedSrcIp = _Hh3cAclAdvancedSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 5),
    _Hh3cAclAdvancedSrcIp_Type()
)
hh3cAclAdvancedSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedSrcIp.setStatus("current")
_Hh3cAclAdvancedSrcWild_Type = IpAddress
_Hh3cAclAdvancedSrcWild_Object = MibTableColumn
hh3cAclAdvancedSrcWild = _Hh3cAclAdvancedSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 6),
    _Hh3cAclAdvancedSrcWild_Type()
)
hh3cAclAdvancedSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedSrcWild.setStatus("current")


class _Hh3cAclAdvancedSrcOp_Type(Integer32):
    """Custom type hh3cAclAdvancedSrcOp based on Integer32"""
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


_Hh3cAclAdvancedSrcOp_Type.__name__ = "Integer32"
_Hh3cAclAdvancedSrcOp_Object = MibTableColumn
hh3cAclAdvancedSrcOp = _Hh3cAclAdvancedSrcOp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 7),
    _Hh3cAclAdvancedSrcOp_Type()
)
hh3cAclAdvancedSrcOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedSrcOp.setStatus("current")


class _Hh3cAclAdvancedSrcPort1_Type(Integer32):
    """Custom type hh3cAclAdvancedSrcPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclAdvancedSrcPort1_Type.__name__ = "Integer32"
_Hh3cAclAdvancedSrcPort1_Object = MibTableColumn
hh3cAclAdvancedSrcPort1 = _Hh3cAclAdvancedSrcPort1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 8),
    _Hh3cAclAdvancedSrcPort1_Type()
)
hh3cAclAdvancedSrcPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedSrcPort1.setStatus("current")


class _Hh3cAclAdvancedSrcPort2_Type(Integer32):
    """Custom type hh3cAclAdvancedSrcPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclAdvancedSrcPort2_Type.__name__ = "Integer32"
_Hh3cAclAdvancedSrcPort2_Object = MibTableColumn
hh3cAclAdvancedSrcPort2 = _Hh3cAclAdvancedSrcPort2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 9),
    _Hh3cAclAdvancedSrcPort2_Type()
)
hh3cAclAdvancedSrcPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedSrcPort2.setStatus("current")
_Hh3cAclAdvancedDestIp_Type = IpAddress
_Hh3cAclAdvancedDestIp_Object = MibTableColumn
hh3cAclAdvancedDestIp = _Hh3cAclAdvancedDestIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 10),
    _Hh3cAclAdvancedDestIp_Type()
)
hh3cAclAdvancedDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedDestIp.setStatus("current")
_Hh3cAclAdvancedDestWild_Type = IpAddress
_Hh3cAclAdvancedDestWild_Object = MibTableColumn
hh3cAclAdvancedDestWild = _Hh3cAclAdvancedDestWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 11),
    _Hh3cAclAdvancedDestWild_Type()
)
hh3cAclAdvancedDestWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedDestWild.setStatus("current")


class _Hh3cAclAdvancedDestOp_Type(Integer32):
    """Custom type hh3cAclAdvancedDestOp based on Integer32"""
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


_Hh3cAclAdvancedDestOp_Type.__name__ = "Integer32"
_Hh3cAclAdvancedDestOp_Object = MibTableColumn
hh3cAclAdvancedDestOp = _Hh3cAclAdvancedDestOp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 12),
    _Hh3cAclAdvancedDestOp_Type()
)
hh3cAclAdvancedDestOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedDestOp.setStatus("current")


class _Hh3cAclAdvancedDestPort1_Type(Integer32):
    """Custom type hh3cAclAdvancedDestPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclAdvancedDestPort1_Type.__name__ = "Integer32"
_Hh3cAclAdvancedDestPort1_Object = MibTableColumn
hh3cAclAdvancedDestPort1 = _Hh3cAclAdvancedDestPort1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 13),
    _Hh3cAclAdvancedDestPort1_Type()
)
hh3cAclAdvancedDestPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedDestPort1.setStatus("current")


class _Hh3cAclAdvancedDestPort2_Type(Integer32):
    """Custom type hh3cAclAdvancedDestPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclAdvancedDestPort2_Type.__name__ = "Integer32"
_Hh3cAclAdvancedDestPort2_Object = MibTableColumn
hh3cAclAdvancedDestPort2 = _Hh3cAclAdvancedDestPort2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 14),
    _Hh3cAclAdvancedDestPort2_Type()
)
hh3cAclAdvancedDestPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedDestPort2.setStatus("current")


class _Hh3cAclAdvancedPrecedence_Type(Integer32):
    """Custom type hh3cAclAdvancedPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cAclAdvancedPrecedence_Type.__name__ = "Integer32"
_Hh3cAclAdvancedPrecedence_Object = MibTableColumn
hh3cAclAdvancedPrecedence = _Hh3cAclAdvancedPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 15),
    _Hh3cAclAdvancedPrecedence_Type()
)
hh3cAclAdvancedPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedPrecedence.setStatus("current")


class _Hh3cAclAdvancedTos_Type(Integer32):
    """Custom type hh3cAclAdvancedTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_Hh3cAclAdvancedTos_Type.__name__ = "Integer32"
_Hh3cAclAdvancedTos_Object = MibTableColumn
hh3cAclAdvancedTos = _Hh3cAclAdvancedTos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 16),
    _Hh3cAclAdvancedTos_Type()
)
hh3cAclAdvancedTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedTos.setStatus("current")


class _Hh3cAclAdvancedDscp_Type(Integer32):
    """Custom type hh3cAclAdvancedDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_Hh3cAclAdvancedDscp_Type.__name__ = "Integer32"
_Hh3cAclAdvancedDscp_Object = MibTableColumn
hh3cAclAdvancedDscp = _Hh3cAclAdvancedDscp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 17),
    _Hh3cAclAdvancedDscp_Type()
)
hh3cAclAdvancedDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedDscp.setStatus("current")


class _Hh3cAclAdvancedEstablish_Type(TruthValue):
    """Custom type hh3cAclAdvancedEstablish based on TruthValue"""


_Hh3cAclAdvancedEstablish_Object = MibTableColumn
hh3cAclAdvancedEstablish = _Hh3cAclAdvancedEstablish_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 18),
    _Hh3cAclAdvancedEstablish_Type()
)
hh3cAclAdvancedEstablish.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedEstablish.setStatus("current")


class _Hh3cAclAdvancedTimeRangeName_Type(OctetString):
    """Custom type hh3cAclAdvancedTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclAdvancedTimeRangeName_Type.__name__ = "OctetString"
_Hh3cAclAdvancedTimeRangeName_Object = MibTableColumn
hh3cAclAdvancedTimeRangeName = _Hh3cAclAdvancedTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 19),
    _Hh3cAclAdvancedTimeRangeName_Type()
)
hh3cAclAdvancedTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedTimeRangeName.setStatus("current")


class _Hh3cAclAdvancedIcmpType_Type(Integer32):
    """Custom type hh3cAclAdvancedIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cAclAdvancedIcmpType_Type.__name__ = "Integer32"
_Hh3cAclAdvancedIcmpType_Object = MibTableColumn
hh3cAclAdvancedIcmpType = _Hh3cAclAdvancedIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 20),
    _Hh3cAclAdvancedIcmpType_Type()
)
hh3cAclAdvancedIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedIcmpType.setStatus("current")


class _Hh3cAclAdvancedIcmpCode_Type(Integer32):
    """Custom type hh3cAclAdvancedIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cAclAdvancedIcmpCode_Type.__name__ = "Integer32"
_Hh3cAclAdvancedIcmpCode_Object = MibTableColumn
hh3cAclAdvancedIcmpCode = _Hh3cAclAdvancedIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 21),
    _Hh3cAclAdvancedIcmpCode_Type()
)
hh3cAclAdvancedIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedIcmpCode.setStatus("current")
_Hh3cAclAdvancedFragments_Type = TruthValue
_Hh3cAclAdvancedFragments_Object = MibTableColumn
hh3cAclAdvancedFragments = _Hh3cAclAdvancedFragments_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 22),
    _Hh3cAclAdvancedFragments_Type()
)
hh3cAclAdvancedFragments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedFragments.setStatus("current")
_Hh3cAclAdvancedLog_Type = TruthValue
_Hh3cAclAdvancedLog_Object = MibTableColumn
hh3cAclAdvancedLog = _Hh3cAclAdvancedLog_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 23),
    _Hh3cAclAdvancedLog_Type()
)
hh3cAclAdvancedLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedLog.setStatus("current")
_Hh3cAclAdvancedEnable_Type = TruthValue
_Hh3cAclAdvancedEnable_Object = MibTableColumn
hh3cAclAdvancedEnable = _Hh3cAclAdvancedEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 24),
    _Hh3cAclAdvancedEnable_Type()
)
hh3cAclAdvancedEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclAdvancedEnable.setStatus("current")
_Hh3cAclAdvancedCount_Type = Counter32
_Hh3cAclAdvancedCount_Object = MibTableColumn
hh3cAclAdvancedCount = _Hh3cAclAdvancedCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 25),
    _Hh3cAclAdvancedCount_Type()
)
hh3cAclAdvancedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclAdvancedCount.setStatus("current")


class _Hh3cAclAdvancedCountClear_Type(Integer32):
    """Custom type hh3cAclAdvancedCountClear based on Integer32"""
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


_Hh3cAclAdvancedCountClear_Type.__name__ = "Integer32"
_Hh3cAclAdvancedCountClear_Object = MibTableColumn
hh3cAclAdvancedCountClear = _Hh3cAclAdvancedCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 26),
    _Hh3cAclAdvancedCountClear_Type()
)
hh3cAclAdvancedCountClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedCountClear.setStatus("current")
_Hh3cAclAdvancedRowStatus_Type = RowStatus
_Hh3cAclAdvancedRowStatus_Object = MibTableColumn
hh3cAclAdvancedRowStatus = _Hh3cAclAdvancedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 27),
    _Hh3cAclAdvancedRowStatus_Type()
)
hh3cAclAdvancedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedRowStatus.setStatus("current")
_Hh3cAclIfRuleTable_Object = MibTable
hh3cAclIfRuleTable = _Hh3cAclIfRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cAclIfRuleTable.setStatus("current")
_Hh3cAclIfRuleEntry_Object = MibTableRow
hh3cAclIfRuleEntry = _Hh3cAclIfRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6, 1)
)
hh3cAclIfRuleEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclIfAclNum"),
    (0, "HH3C-ACL-MIB", "hh3cAclIfSubitem"),
)
if mibBuilder.loadTexts:
    hh3cAclIfRuleEntry.setStatus("current")


class _Hh3cAclIfAclNum_Type(Integer32):
    """Custom type hh3cAclIfAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 1999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cAclIfAclNum_Type.__name__ = "Integer32"
_Hh3cAclIfAclNum_Object = MibTableColumn
hh3cAclIfAclNum = _Hh3cAclIfAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6, 1, 1),
    _Hh3cAclIfAclNum_Type()
)
hh3cAclIfAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclIfAclNum.setStatus("current")


class _Hh3cAclIfSubitem_Type(Integer32):
    """Custom type hh3cAclIfSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclIfSubitem_Type.__name__ = "Integer32"
_Hh3cAclIfSubitem_Object = MibTableColumn
hh3cAclIfSubitem = _Hh3cAclIfSubitem_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6, 1, 2),
    _Hh3cAclIfSubitem_Type()
)
hh3cAclIfSubitem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclIfSubitem.setStatus("current")


class _Hh3cAclIfAct_Type(Integer32):
    """Custom type hh3cAclIfAct based on Integer32"""
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


_Hh3cAclIfAct_Type.__name__ = "Integer32"
_Hh3cAclIfAct_Object = MibTableColumn
hh3cAclIfAct = _Hh3cAclIfAct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6, 1, 3),
    _Hh3cAclIfAct_Type()
)
hh3cAclIfAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIfAct.setStatus("current")


class _Hh3cAclIfIndex_Type(Integer32):
    """Custom type hh3cAclIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cAclIfIndex_Type.__name__ = "Integer32"
_Hh3cAclIfIndex_Object = MibTableColumn
hh3cAclIfIndex = _Hh3cAclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6, 1, 4),
    _Hh3cAclIfIndex_Type()
)
hh3cAclIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIfIndex.setStatus("current")
_Hh3cAclIfAny_Type = TruthValue
_Hh3cAclIfAny_Object = MibTableColumn
hh3cAclIfAny = _Hh3cAclIfAny_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6, 1, 5),
    _Hh3cAclIfAny_Type()
)
hh3cAclIfAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIfAny.setStatus("current")


class _Hh3cAclIfTimeRangeName_Type(OctetString):
    """Custom type hh3cAclIfTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclIfTimeRangeName_Type.__name__ = "OctetString"
_Hh3cAclIfTimeRangeName_Object = MibTableColumn
hh3cAclIfTimeRangeName = _Hh3cAclIfTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6, 1, 6),
    _Hh3cAclIfTimeRangeName_Type()
)
hh3cAclIfTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIfTimeRangeName.setStatus("current")
_Hh3cAclIfLog_Type = TruthValue
_Hh3cAclIfLog_Object = MibTableColumn
hh3cAclIfLog = _Hh3cAclIfLog_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6, 1, 7),
    _Hh3cAclIfLog_Type()
)
hh3cAclIfLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIfLog.setStatus("current")
_Hh3cAclIfEnable_Type = TruthValue
_Hh3cAclIfEnable_Object = MibTableColumn
hh3cAclIfEnable = _Hh3cAclIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6, 1, 8),
    _Hh3cAclIfEnable_Type()
)
hh3cAclIfEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclIfEnable.setStatus("current")
_Hh3cAclIfCount_Type = Counter32
_Hh3cAclIfCount_Object = MibTableColumn
hh3cAclIfCount = _Hh3cAclIfCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6, 1, 9),
    _Hh3cAclIfCount_Type()
)
hh3cAclIfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclIfCount.setStatus("current")


class _Hh3cAclIfCountClear_Type(Integer32):
    """Custom type hh3cAclIfCountClear based on Integer32"""
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


_Hh3cAclIfCountClear_Type.__name__ = "Integer32"
_Hh3cAclIfCountClear_Object = MibTableColumn
hh3cAclIfCountClear = _Hh3cAclIfCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6, 1, 10),
    _Hh3cAclIfCountClear_Type()
)
hh3cAclIfCountClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIfCountClear.setStatus("current")
_Hh3cAclIfRowStatus_Type = RowStatus
_Hh3cAclIfRowStatus_Object = MibTableColumn
hh3cAclIfRowStatus = _Hh3cAclIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6, 1, 11),
    _Hh3cAclIfRowStatus_Type()
)
hh3cAclIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIfRowStatus.setStatus("current")
_Hh3cAclLinkTable_Object = MibTable
hh3cAclLinkTable = _Hh3cAclLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cAclLinkTable.setStatus("current")
_Hh3cAclLinkEntry_Object = MibTableRow
hh3cAclLinkEntry = _Hh3cAclLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1)
)
hh3cAclLinkEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclLinkAclNum"),
    (0, "HH3C-ACL-MIB", "hh3cAclLinkSubitem"),
)
if mibBuilder.loadTexts:
    hh3cAclLinkEntry.setStatus("current")


class _Hh3cAclLinkAclNum_Type(Integer32):
    """Custom type hh3cAclLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cAclLinkAclNum_Type.__name__ = "Integer32"
_Hh3cAclLinkAclNum_Object = MibTableColumn
hh3cAclLinkAclNum = _Hh3cAclLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 1),
    _Hh3cAclLinkAclNum_Type()
)
hh3cAclLinkAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclLinkAclNum.setStatus("current")


class _Hh3cAclLinkSubitem_Type(Integer32):
    """Custom type hh3cAclLinkSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclLinkSubitem_Type.__name__ = "Integer32"
_Hh3cAclLinkSubitem_Object = MibTableColumn
hh3cAclLinkSubitem = _Hh3cAclLinkSubitem_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 2),
    _Hh3cAclLinkSubitem_Type()
)
hh3cAclLinkSubitem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclLinkSubitem.setStatus("current")


class _Hh3cAclLinkAct_Type(Integer32):
    """Custom type hh3cAclLinkAct based on Integer32"""
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


_Hh3cAclLinkAct_Type.__name__ = "Integer32"
_Hh3cAclLinkAct_Object = MibTableColumn
hh3cAclLinkAct = _Hh3cAclLinkAct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 3),
    _Hh3cAclLinkAct_Type()
)
hh3cAclLinkAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkAct.setStatus("current")


class _Hh3cAclLinkProtocol_Type(Integer32):
    """Custom type hh3cAclLinkProtocol based on Integer32"""
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


_Hh3cAclLinkProtocol_Type.__name__ = "Integer32"
_Hh3cAclLinkProtocol_Object = MibTableColumn
hh3cAclLinkProtocol = _Hh3cAclLinkProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 4),
    _Hh3cAclLinkProtocol_Type()
)
hh3cAclLinkProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkProtocol.setStatus("current")


class _Hh3cAclLinkFormatType_Type(Integer32):
    """Custom type hh3cAclLinkFormatType based on Integer32"""
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


_Hh3cAclLinkFormatType_Type.__name__ = "Integer32"
_Hh3cAclLinkFormatType_Object = MibTableColumn
hh3cAclLinkFormatType = _Hh3cAclLinkFormatType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 5),
    _Hh3cAclLinkFormatType_Type()
)
hh3cAclLinkFormatType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkFormatType.setStatus("current")


class _Hh3cAclLinkVlanTag_Type(Integer32):
    """Custom type hh3cAclLinkVlanTag based on Integer32"""
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


_Hh3cAclLinkVlanTag_Type.__name__ = "Integer32"
_Hh3cAclLinkVlanTag_Object = MibTableColumn
hh3cAclLinkVlanTag = _Hh3cAclLinkVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 6),
    _Hh3cAclLinkVlanTag_Type()
)
hh3cAclLinkVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkVlanTag.setStatus("current")


class _Hh3cAclLinkVlanPri_Type(Integer32):
    """Custom type hh3cAclLinkVlanPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cAclLinkVlanPri_Type.__name__ = "Integer32"
_Hh3cAclLinkVlanPri_Object = MibTableColumn
hh3cAclLinkVlanPri = _Hh3cAclLinkVlanPri_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 7),
    _Hh3cAclLinkVlanPri_Type()
)
hh3cAclLinkVlanPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkVlanPri.setStatus("current")


class _Hh3cAclLinkSrcVlanId_Type(Integer32):
    """Custom type hh3cAclLinkSrcVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cAclLinkSrcVlanId_Type.__name__ = "Integer32"
_Hh3cAclLinkSrcVlanId_Object = MibTableColumn
hh3cAclLinkSrcVlanId = _Hh3cAclLinkSrcVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 8),
    _Hh3cAclLinkSrcVlanId_Type()
)
hh3cAclLinkSrcVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkSrcVlanId.setStatus("current")
_Hh3cAclLinkSrcMac_Type = MacAddress
_Hh3cAclLinkSrcMac_Object = MibTableColumn
hh3cAclLinkSrcMac = _Hh3cAclLinkSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 9),
    _Hh3cAclLinkSrcMac_Type()
)
hh3cAclLinkSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkSrcMac.setStatus("current")
_Hh3cAclLinkSrcMacWild_Type = MacAddress
_Hh3cAclLinkSrcMacWild_Object = MibTableColumn
hh3cAclLinkSrcMacWild = _Hh3cAclLinkSrcMacWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 10),
    _Hh3cAclLinkSrcMacWild_Type()
)
hh3cAclLinkSrcMacWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkSrcMacWild.setStatus("current")


class _Hh3cAclLinkSrcIfIndex_Type(Integer32):
    """Custom type hh3cAclLinkSrcIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cAclLinkSrcIfIndex_Type.__name__ = "Integer32"
_Hh3cAclLinkSrcIfIndex_Object = MibTableColumn
hh3cAclLinkSrcIfIndex = _Hh3cAclLinkSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 11),
    _Hh3cAclLinkSrcIfIndex_Type()
)
hh3cAclLinkSrcIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkSrcIfIndex.setStatus("current")
_Hh3cAclLinkSrcAny_Type = TruthValue
_Hh3cAclLinkSrcAny_Object = MibTableColumn
hh3cAclLinkSrcAny = _Hh3cAclLinkSrcAny_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 12),
    _Hh3cAclLinkSrcAny_Type()
)
hh3cAclLinkSrcAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkSrcAny.setStatus("current")


class _Hh3cAclLinkDestVlanId_Type(Integer32):
    """Custom type hh3cAclLinkDestVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cAclLinkDestVlanId_Type.__name__ = "Integer32"
_Hh3cAclLinkDestVlanId_Object = MibTableColumn
hh3cAclLinkDestVlanId = _Hh3cAclLinkDestVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 13),
    _Hh3cAclLinkDestVlanId_Type()
)
hh3cAclLinkDestVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkDestVlanId.setStatus("current")
_Hh3cAclLinkDestMac_Type = MacAddress
_Hh3cAclLinkDestMac_Object = MibTableColumn
hh3cAclLinkDestMac = _Hh3cAclLinkDestMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 14),
    _Hh3cAclLinkDestMac_Type()
)
hh3cAclLinkDestMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkDestMac.setStatus("current")
_Hh3cAclLinkDestMacWild_Type = MacAddress
_Hh3cAclLinkDestMacWild_Object = MibTableColumn
hh3cAclLinkDestMacWild = _Hh3cAclLinkDestMacWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 15),
    _Hh3cAclLinkDestMacWild_Type()
)
hh3cAclLinkDestMacWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkDestMacWild.setStatus("current")


class _Hh3cAclLinkDestIfIndex_Type(Integer32):
    """Custom type hh3cAclLinkDestIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cAclLinkDestIfIndex_Type.__name__ = "Integer32"
_Hh3cAclLinkDestIfIndex_Object = MibTableColumn
hh3cAclLinkDestIfIndex = _Hh3cAclLinkDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 16),
    _Hh3cAclLinkDestIfIndex_Type()
)
hh3cAclLinkDestIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkDestIfIndex.setStatus("current")
_Hh3cAclLinkDestAny_Type = TruthValue
_Hh3cAclLinkDestAny_Object = MibTableColumn
hh3cAclLinkDestAny = _Hh3cAclLinkDestAny_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 17),
    _Hh3cAclLinkDestAny_Type()
)
hh3cAclLinkDestAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkDestAny.setStatus("current")


class _Hh3cAclLinkTimeRangeName_Type(OctetString):
    """Custom type hh3cAclLinkTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclLinkTimeRangeName_Type.__name__ = "OctetString"
_Hh3cAclLinkTimeRangeName_Object = MibTableColumn
hh3cAclLinkTimeRangeName = _Hh3cAclLinkTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 18),
    _Hh3cAclLinkTimeRangeName_Type()
)
hh3cAclLinkTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkTimeRangeName.setStatus("current")
_Hh3cAclLinkEnable_Type = TruthValue
_Hh3cAclLinkEnable_Object = MibTableColumn
hh3cAclLinkEnable = _Hh3cAclLinkEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 19),
    _Hh3cAclLinkEnable_Type()
)
hh3cAclLinkEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclLinkEnable.setStatus("current")
_Hh3cAclLinkRowStatus_Type = RowStatus
_Hh3cAclLinkRowStatus_Object = MibTableColumn
hh3cAclLinkRowStatus = _Hh3cAclLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 20),
    _Hh3cAclLinkRowStatus_Type()
)
hh3cAclLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkRowStatus.setStatus("current")


class _Hh3cAclLinkTypeCode_Type(OctetString):
    """Custom type hh3cAclLinkTypeCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclLinkTypeCode_Type.__name__ = "OctetString"
_Hh3cAclLinkTypeCode_Object = MibTableColumn
hh3cAclLinkTypeCode = _Hh3cAclLinkTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 21),
    _Hh3cAclLinkTypeCode_Type()
)
hh3cAclLinkTypeCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkTypeCode.setStatus("current")


class _Hh3cAclLinkTypeMask_Type(OctetString):
    """Custom type hh3cAclLinkTypeMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclLinkTypeMask_Type.__name__ = "OctetString"
_Hh3cAclLinkTypeMask_Object = MibTableColumn
hh3cAclLinkTypeMask = _Hh3cAclLinkTypeMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 22),
    _Hh3cAclLinkTypeMask_Type()
)
hh3cAclLinkTypeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkTypeMask.setStatus("current")


class _Hh3cAclLinkLsapCode_Type(OctetString):
    """Custom type hh3cAclLinkLsapCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclLinkLsapCode_Type.__name__ = "OctetString"
_Hh3cAclLinkLsapCode_Object = MibTableColumn
hh3cAclLinkLsapCode = _Hh3cAclLinkLsapCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 23),
    _Hh3cAclLinkLsapCode_Type()
)
hh3cAclLinkLsapCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkLsapCode.setStatus("current")


class _Hh3cAclLinkLsapMask_Type(OctetString):
    """Custom type hh3cAclLinkLsapMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclLinkLsapMask_Type.__name__ = "OctetString"
_Hh3cAclLinkLsapMask_Object = MibTableColumn
hh3cAclLinkLsapMask = _Hh3cAclLinkLsapMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 24),
    _Hh3cAclLinkLsapMask_Type()
)
hh3cAclLinkLsapMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkLsapMask.setStatus("current")


class _Hh3cAclLinkL2LabelRangeOp_Type(Integer32):
    """Custom type hh3cAclLinkL2LabelRangeOp based on Integer32"""
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


_Hh3cAclLinkL2LabelRangeOp_Type.__name__ = "Integer32"
_Hh3cAclLinkL2LabelRangeOp_Object = MibTableColumn
hh3cAclLinkL2LabelRangeOp = _Hh3cAclLinkL2LabelRangeOp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 25),
    _Hh3cAclLinkL2LabelRangeOp_Type()
)
hh3cAclLinkL2LabelRangeOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkL2LabelRangeOp.setStatus("current")
_Hh3cAclLinkL2LabelRangeBegin_Type = Integer32
_Hh3cAclLinkL2LabelRangeBegin_Object = MibTableColumn
hh3cAclLinkL2LabelRangeBegin = _Hh3cAclLinkL2LabelRangeBegin_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 26),
    _Hh3cAclLinkL2LabelRangeBegin_Type()
)
hh3cAclLinkL2LabelRangeBegin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkL2LabelRangeBegin.setStatus("current")
_Hh3cAclLinkL2LabelRangeEnd_Type = Integer32
_Hh3cAclLinkL2LabelRangeEnd_Object = MibTableColumn
hh3cAclLinkL2LabelRangeEnd = _Hh3cAclLinkL2LabelRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 27),
    _Hh3cAclLinkL2LabelRangeEnd_Type()
)
hh3cAclLinkL2LabelRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkL2LabelRangeEnd.setStatus("current")
_Hh3cAclLinkMplsExp_Type = Integer32
_Hh3cAclLinkMplsExp_Object = MibTableColumn
hh3cAclLinkMplsExp = _Hh3cAclLinkMplsExp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 28),
    _Hh3cAclLinkMplsExp_Type()
)
hh3cAclLinkMplsExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkMplsExp.setStatus("current")
_Hh3cAclUserTable_Object = MibTable
hh3cAclUserTable = _Hh3cAclUserTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 8)
)
if mibBuilder.loadTexts:
    hh3cAclUserTable.setStatus("current")
_Hh3cAclUserEntry_Object = MibTableRow
hh3cAclUserEntry = _Hh3cAclUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 8, 1)
)
hh3cAclUserEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclUserAclNum"),
    (0, "HH3C-ACL-MIB", "hh3cAclUserSubitem"),
)
if mibBuilder.loadTexts:
    hh3cAclUserEntry.setStatus("current")


class _Hh3cAclUserAclNum_Type(Integer32):
    """Custom type hh3cAclUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cAclUserAclNum_Type.__name__ = "Integer32"
_Hh3cAclUserAclNum_Object = MibTableColumn
hh3cAclUserAclNum = _Hh3cAclUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 8, 1, 1),
    _Hh3cAclUserAclNum_Type()
)
hh3cAclUserAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclUserAclNum.setStatus("current")


class _Hh3cAclUserSubitem_Type(Integer32):
    """Custom type hh3cAclUserSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclUserSubitem_Type.__name__ = "Integer32"
_Hh3cAclUserSubitem_Object = MibTableColumn
hh3cAclUserSubitem = _Hh3cAclUserSubitem_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 8, 1, 2),
    _Hh3cAclUserSubitem_Type()
)
hh3cAclUserSubitem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclUserSubitem.setStatus("current")


class _Hh3cAclUserAct_Type(Integer32):
    """Custom type hh3cAclUserAct based on Integer32"""
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


_Hh3cAclUserAct_Type.__name__ = "Integer32"
_Hh3cAclUserAct_Object = MibTableColumn
hh3cAclUserAct = _Hh3cAclUserAct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 8, 1, 3),
    _Hh3cAclUserAct_Type()
)
hh3cAclUserAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclUserAct.setStatus("current")


class _Hh3cAclUserFormatType_Type(Integer32):
    """Custom type hh3cAclUserFormatType based on Integer32"""
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


_Hh3cAclUserFormatType_Type.__name__ = "Integer32"
_Hh3cAclUserFormatType_Object = MibTableColumn
hh3cAclUserFormatType = _Hh3cAclUserFormatType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 8, 1, 4),
    _Hh3cAclUserFormatType_Type()
)
hh3cAclUserFormatType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclUserFormatType.setStatus("current")


class _Hh3cAclUserVlanTag_Type(Integer32):
    """Custom type hh3cAclUserVlanTag based on Integer32"""
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


_Hh3cAclUserVlanTag_Type.__name__ = "Integer32"
_Hh3cAclUserVlanTag_Object = MibTableColumn
hh3cAclUserVlanTag = _Hh3cAclUserVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 8, 1, 5),
    _Hh3cAclUserVlanTag_Type()
)
hh3cAclUserVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclUserVlanTag.setStatus("current")


class _Hh3cAclUserRuleStr_Type(OctetString):
    """Custom type hh3cAclUserRuleStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Hh3cAclUserRuleStr_Type.__name__ = "OctetString"
_Hh3cAclUserRuleStr_Object = MibTableColumn
hh3cAclUserRuleStr = _Hh3cAclUserRuleStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 8, 1, 6),
    _Hh3cAclUserRuleStr_Type()
)
hh3cAclUserRuleStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclUserRuleStr.setStatus("current")


class _Hh3cAclUserRuleMask_Type(OctetString):
    """Custom type hh3cAclUserRuleMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Hh3cAclUserRuleMask_Type.__name__ = "OctetString"
_Hh3cAclUserRuleMask_Object = MibTableColumn
hh3cAclUserRuleMask = _Hh3cAclUserRuleMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 8, 1, 7),
    _Hh3cAclUserRuleMask_Type()
)
hh3cAclUserRuleMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclUserRuleMask.setStatus("current")


class _Hh3cAclUserTimeRangeName_Type(OctetString):
    """Custom type hh3cAclUserTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclUserTimeRangeName_Type.__name__ = "OctetString"
_Hh3cAclUserTimeRangeName_Object = MibTableColumn
hh3cAclUserTimeRangeName = _Hh3cAclUserTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 8, 1, 8),
    _Hh3cAclUserTimeRangeName_Type()
)
hh3cAclUserTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclUserTimeRangeName.setStatus("current")
_Hh3cAclUserEnable_Type = TruthValue
_Hh3cAclUserEnable_Object = MibTableColumn
hh3cAclUserEnable = _Hh3cAclUserEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 8, 1, 9),
    _Hh3cAclUserEnable_Type()
)
hh3cAclUserEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclUserEnable.setStatus("current")
_Hh3cAclUserRowStatus_Type = RowStatus
_Hh3cAclUserRowStatus_Object = MibTableColumn
hh3cAclUserRowStatus = _Hh3cAclUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 8, 1, 10),
    _Hh3cAclUserRowStatus_Type()
)
hh3cAclUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclUserRowStatus.setStatus("current")
_Hh3cAclActiveTable_Object = MibTable
hh3cAclActiveTable = _Hh3cAclActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9)
)
if mibBuilder.loadTexts:
    hh3cAclActiveTable.setStatus("current")
_Hh3cAclActiveEntry_Object = MibTableRow
hh3cAclActiveEntry = _Hh3cAclActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1)
)
hh3cAclActiveEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclActiveAclIndex"),
    (0, "HH3C-ACL-MIB", "hh3cAclActiveIfIndex"),
    (0, "HH3C-ACL-MIB", "hh3cAclActiveVlanID"),
    (0, "HH3C-ACL-MIB", "hh3cAclActiveDirection"),
)
if mibBuilder.loadTexts:
    hh3cAclActiveEntry.setStatus("current")


class _Hh3cAclActiveAclIndex_Type(Integer32):
    """Custom type hh3cAclActiveAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cAclActiveAclIndex_Type.__name__ = "Integer32"
_Hh3cAclActiveAclIndex_Object = MibTableColumn
hh3cAclActiveAclIndex = _Hh3cAclActiveAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1, 1),
    _Hh3cAclActiveAclIndex_Type()
)
hh3cAclActiveAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclActiveAclIndex.setStatus("current")


class _Hh3cAclActiveIfIndex_Type(Integer32):
    """Custom type hh3cAclActiveIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cAclActiveIfIndex_Type.__name__ = "Integer32"
_Hh3cAclActiveIfIndex_Object = MibTableColumn
hh3cAclActiveIfIndex = _Hh3cAclActiveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1, 2),
    _Hh3cAclActiveIfIndex_Type()
)
hh3cAclActiveIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclActiveIfIndex.setStatus("current")
_Hh3cAclActiveVlanID_Type = Integer32
_Hh3cAclActiveVlanID_Object = MibTableColumn
hh3cAclActiveVlanID = _Hh3cAclActiveVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1, 3),
    _Hh3cAclActiveVlanID_Type()
)
hh3cAclActiveVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclActiveVlanID.setStatus("current")


class _Hh3cAclActiveDirection_Type(Integer32):
    """Custom type hh3cAclActiveDirection based on Integer32"""
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


_Hh3cAclActiveDirection_Type.__name__ = "Integer32"
_Hh3cAclActiveDirection_Object = MibTableColumn
hh3cAclActiveDirection = _Hh3cAclActiveDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1, 4),
    _Hh3cAclActiveDirection_Type()
)
hh3cAclActiveDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclActiveDirection.setStatus("current")


class _Hh3cAclActiveUserAclNum_Type(Integer32):
    """Custom type hh3cAclActiveUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cAclActiveUserAclNum_Type.__name__ = "Integer32"
_Hh3cAclActiveUserAclNum_Object = MibTableColumn
hh3cAclActiveUserAclNum = _Hh3cAclActiveUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1, 5),
    _Hh3cAclActiveUserAclNum_Type()
)
hh3cAclActiveUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclActiveUserAclNum.setStatus("current")


class _Hh3cAclActiveUserAclSubitem_Type(Integer32):
    """Custom type hh3cAclActiveUserAclSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclActiveUserAclSubitem_Type.__name__ = "Integer32"
_Hh3cAclActiveUserAclSubitem_Object = MibTableColumn
hh3cAclActiveUserAclSubitem = _Hh3cAclActiveUserAclSubitem_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1, 6),
    _Hh3cAclActiveUserAclSubitem_Type()
)
hh3cAclActiveUserAclSubitem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclActiveUserAclSubitem.setStatus("current")


class _Hh3cAclActiveIpAclNum_Type(Integer32):
    """Custom type hh3cAclActiveIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cAclActiveIpAclNum_Type.__name__ = "Integer32"
_Hh3cAclActiveIpAclNum_Object = MibTableColumn
hh3cAclActiveIpAclNum = _Hh3cAclActiveIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1, 7),
    _Hh3cAclActiveIpAclNum_Type()
)
hh3cAclActiveIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclActiveIpAclNum.setStatus("current")


class _Hh3cAclActiveIpAclSubitem_Type(Integer32):
    """Custom type hh3cAclActiveIpAclSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclActiveIpAclSubitem_Type.__name__ = "Integer32"
_Hh3cAclActiveIpAclSubitem_Object = MibTableColumn
hh3cAclActiveIpAclSubitem = _Hh3cAclActiveIpAclSubitem_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1, 8),
    _Hh3cAclActiveIpAclSubitem_Type()
)
hh3cAclActiveIpAclSubitem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclActiveIpAclSubitem.setStatus("current")


class _Hh3cAclActiveLinkAclNum_Type(Integer32):
    """Custom type hh3cAclActiveLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cAclActiveLinkAclNum_Type.__name__ = "Integer32"
_Hh3cAclActiveLinkAclNum_Object = MibTableColumn
hh3cAclActiveLinkAclNum = _Hh3cAclActiveLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1, 9),
    _Hh3cAclActiveLinkAclNum_Type()
)
hh3cAclActiveLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclActiveLinkAclNum.setStatus("current")


class _Hh3cAclActiveLinkAclSubitem_Type(Integer32):
    """Custom type hh3cAclActiveLinkAclSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclActiveLinkAclSubitem_Type.__name__ = "Integer32"
_Hh3cAclActiveLinkAclSubitem_Object = MibTableColumn
hh3cAclActiveLinkAclSubitem = _Hh3cAclActiveLinkAclSubitem_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1, 10),
    _Hh3cAclActiveLinkAclSubitem_Type()
)
hh3cAclActiveLinkAclSubitem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclActiveLinkAclSubitem.setStatus("current")
_Hh3cAclActiveRuntime_Type = TruthValue
_Hh3cAclActiveRuntime_Object = MibTableColumn
hh3cAclActiveRuntime = _Hh3cAclActiveRuntime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1, 11),
    _Hh3cAclActiveRuntime_Type()
)
hh3cAclActiveRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclActiveRuntime.setStatus("current")
_Hh3cAclActiveRowStatus_Type = RowStatus
_Hh3cAclActiveRowStatus_Object = MibTableColumn
hh3cAclActiveRowStatus = _Hh3cAclActiveRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1, 12),
    _Hh3cAclActiveRowStatus_Type()
)
hh3cAclActiveRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclActiveRowStatus.setStatus("current")
_Hh3cAclIDSTable_Object = MibTable
hh3cAclIDSTable = _Hh3cAclIDSTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10)
)
if mibBuilder.loadTexts:
    hh3cAclIDSTable.setStatus("current")
_Hh3cAclIDSEntry_Object = MibTableRow
hh3cAclIDSEntry = _Hh3cAclIDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1)
)
hh3cAclIDSEntry.setIndexNames(
    (1, "HH3C-ACL-MIB", "hh3cAclIDSName"),
)
if mibBuilder.loadTexts:
    hh3cAclIDSEntry.setStatus("current")


class _Hh3cAclIDSName_Type(OctetString):
    """Custom type hh3cAclIDSName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cAclIDSName_Type.__name__ = "OctetString"
_Hh3cAclIDSName_Object = MibTableColumn
hh3cAclIDSName = _Hh3cAclIDSName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 1),
    _Hh3cAclIDSName_Type()
)
hh3cAclIDSName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclIDSName.setStatus("current")
_Hh3cAclIDSSrcMac_Type = MacAddress
_Hh3cAclIDSSrcMac_Object = MibTableColumn
hh3cAclIDSSrcMac = _Hh3cAclIDSSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 2),
    _Hh3cAclIDSSrcMac_Type()
)
hh3cAclIDSSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIDSSrcMac.setStatus("current")
_Hh3cAclIDSDestMac_Type = MacAddress
_Hh3cAclIDSDestMac_Object = MibTableColumn
hh3cAclIDSDestMac = _Hh3cAclIDSDestMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 3),
    _Hh3cAclIDSDestMac_Type()
)
hh3cAclIDSDestMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIDSDestMac.setStatus("current")
_Hh3cAclIDSSrcIp_Type = IpAddress
_Hh3cAclIDSSrcIp_Object = MibTableColumn
hh3cAclIDSSrcIp = _Hh3cAclIDSSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 4),
    _Hh3cAclIDSSrcIp_Type()
)
hh3cAclIDSSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIDSSrcIp.setStatus("current")
_Hh3cAclIDSSrcWild_Type = IpAddress
_Hh3cAclIDSSrcWild_Object = MibTableColumn
hh3cAclIDSSrcWild = _Hh3cAclIDSSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 5),
    _Hh3cAclIDSSrcWild_Type()
)
hh3cAclIDSSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIDSSrcWild.setStatus("current")
_Hh3cAclIDSDestIp_Type = IpAddress
_Hh3cAclIDSDestIp_Object = MibTableColumn
hh3cAclIDSDestIp = _Hh3cAclIDSDestIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 6),
    _Hh3cAclIDSDestIp_Type()
)
hh3cAclIDSDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIDSDestIp.setStatus("current")
_Hh3cAclIDSDestWild_Type = IpAddress
_Hh3cAclIDSDestWild_Object = MibTableColumn
hh3cAclIDSDestWild = _Hh3cAclIDSDestWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 7),
    _Hh3cAclIDSDestWild_Type()
)
hh3cAclIDSDestWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIDSDestWild.setStatus("current")


class _Hh3cAclIDSSrcPort_Type(Integer32):
    """Custom type hh3cAclIDSSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclIDSSrcPort_Type.__name__ = "Integer32"
_Hh3cAclIDSSrcPort_Object = MibTableColumn
hh3cAclIDSSrcPort = _Hh3cAclIDSSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 8),
    _Hh3cAclIDSSrcPort_Type()
)
hh3cAclIDSSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIDSSrcPort.setStatus("current")


class _Hh3cAclIDSDestPort_Type(Integer32):
    """Custom type hh3cAclIDSDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclIDSDestPort_Type.__name__ = "Integer32"
_Hh3cAclIDSDestPort_Object = MibTableColumn
hh3cAclIDSDestPort = _Hh3cAclIDSDestPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 9),
    _Hh3cAclIDSDestPort_Type()
)
hh3cAclIDSDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIDSDestPort.setStatus("current")


class _Hh3cAclIDSProtocol_Type(Integer32):
    """Custom type hh3cAclIDSProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cAclIDSProtocol_Type.__name__ = "Integer32"
_Hh3cAclIDSProtocol_Object = MibTableColumn
hh3cAclIDSProtocol = _Hh3cAclIDSProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 10),
    _Hh3cAclIDSProtocol_Type()
)
hh3cAclIDSProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIDSProtocol.setStatus("current")


class _Hh3cAclIDSDenyTime_Type(Unsigned32):
    """Custom type hh3cAclIDSDenyTime based on Unsigned32"""
    defaultValue = 0


_Hh3cAclIDSDenyTime_Object = MibTableColumn
hh3cAclIDSDenyTime = _Hh3cAclIDSDenyTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 11),
    _Hh3cAclIDSDenyTime_Type()
)
hh3cAclIDSDenyTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIDSDenyTime.setStatus("current")


class _Hh3cAclIDSAct_Type(Integer32):
    """Custom type hh3cAclIDSAct based on Integer32"""
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


_Hh3cAclIDSAct_Type.__name__ = "Integer32"
_Hh3cAclIDSAct_Object = MibTableColumn
hh3cAclIDSAct = _Hh3cAclIDSAct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 12),
    _Hh3cAclIDSAct_Type()
)
hh3cAclIDSAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIDSAct.setStatus("current")
_Hh3cAclIDSRowStatus_Type = RowStatus
_Hh3cAclIDSRowStatus_Object = MibTableColumn
hh3cAclIDSRowStatus = _Hh3cAclIDSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 13),
    _Hh3cAclIDSRowStatus_Type()
)
hh3cAclIDSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIDSRowStatus.setStatus("current")
_Hh3cAclMib2Objects_ObjectIdentity = ObjectIdentity
hh3cAclMib2Objects = _Hh3cAclMib2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2)
)
_Hh3cAclMib2GlobalGroup_ObjectIdentity = ObjectIdentity
hh3cAclMib2GlobalGroup = _Hh3cAclMib2GlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1)
)
_Hh3cAclMib2NodesGroup_ObjectIdentity = ObjectIdentity
hh3cAclMib2NodesGroup = _Hh3cAclMib2NodesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 1)
)


class _Hh3cAclMib2Mode_Type(Integer32):
    """Custom type hh3cAclMib2Mode based on Integer32"""
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


_Hh3cAclMib2Mode_Type.__name__ = "Integer32"
_Hh3cAclMib2Mode_Object = MibScalar
hh3cAclMib2Mode = _Hh3cAclMib2Mode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 1, 1),
    _Hh3cAclMib2Mode_Type()
)
hh3cAclMib2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAclMib2Mode.setStatus("current")
_Hh3cAclMib2Version_Type = Integer32
_Hh3cAclMib2Version_Object = MibScalar
hh3cAclMib2Version = _Hh3cAclMib2Version_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 1, 2),
    _Hh3cAclMib2Version_Type()
)
hh3cAclMib2Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclMib2Version.setStatus("current")


class _Hh3cAclMib2ObjectsCapabilities_Type(Bits):
    """Custom type hh3cAclMib2ObjectsCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("hh3cAclEnUserTable", 8),
          ("hh3cAclIPAclAdvancedTable", 6),
          ("hh3cAclIPAclBasicTable", 5),
          ("hh3cAclMACTable", 7),
          ("hh3cAclMib2CapabilityTable", 3),
          ("hh3cAclMib2Mode", 0),
          ("hh3cAclMib2ObjectsCapabilities", 2),
          ("hh3cAclNumberGroupTable", 4),
          ("hh3cAclVersion", 1))
    )

_Hh3cAclMib2ObjectsCapabilities_Type.__name__ = "Bits"
_Hh3cAclMib2ObjectsCapabilities_Object = MibScalar
hh3cAclMib2ObjectsCapabilities = _Hh3cAclMib2ObjectsCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 1, 3),
    _Hh3cAclMib2ObjectsCapabilities_Type()
)
hh3cAclMib2ObjectsCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclMib2ObjectsCapabilities.setStatus("current")
_Hh3cAclMib2CapabilityTable_Object = MibTable
hh3cAclMib2CapabilityTable = _Hh3cAclMib2CapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cAclMib2CapabilityTable.setStatus("current")
_Hh3cAclMib2CapabilityEntry_Object = MibTableRow
hh3cAclMib2CapabilityEntry = _Hh3cAclMib2CapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 2, 1)
)
hh3cAclMib2CapabilityEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclMib2EntityType"),
    (0, "HH3C-ACL-MIB", "hh3cAclMib2EntityIndex"),
    (0, "HH3C-ACL-MIB", "hh3cAclMib2ModuleIndex"),
    (0, "HH3C-ACL-MIB", "hh3cAclMib2CharacteristicsIndex"),
)
if mibBuilder.loadTexts:
    hh3cAclMib2CapabilityEntry.setStatus("current")


class _Hh3cAclMib2EntityType_Type(Integer32):
    """Custom type hh3cAclMib2EntityType based on Integer32"""
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


_Hh3cAclMib2EntityType_Type.__name__ = "Integer32"
_Hh3cAclMib2EntityType_Object = MibTableColumn
hh3cAclMib2EntityType = _Hh3cAclMib2EntityType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 2, 1, 1),
    _Hh3cAclMib2EntityType_Type()
)
hh3cAclMib2EntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclMib2EntityType.setStatus("current")
_Hh3cAclMib2EntityIndex_Type = Integer32
_Hh3cAclMib2EntityIndex_Object = MibTableColumn
hh3cAclMib2EntityIndex = _Hh3cAclMib2EntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 2, 1, 2),
    _Hh3cAclMib2EntityIndex_Type()
)
hh3cAclMib2EntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclMib2EntityIndex.setStatus("current")


class _Hh3cAclMib2ModuleIndex_Type(Integer32):
    """Custom type hh3cAclMib2ModuleIndex based on Integer32"""
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


_Hh3cAclMib2ModuleIndex_Type.__name__ = "Integer32"
_Hh3cAclMib2ModuleIndex_Object = MibTableColumn
hh3cAclMib2ModuleIndex = _Hh3cAclMib2ModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 2, 1, 3),
    _Hh3cAclMib2ModuleIndex_Type()
)
hh3cAclMib2ModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclMib2ModuleIndex.setStatus("current")
_Hh3cAclMib2CharacteristicsIndex_Type = Integer32
_Hh3cAclMib2CharacteristicsIndex_Object = MibTableColumn
hh3cAclMib2CharacteristicsIndex = _Hh3cAclMib2CharacteristicsIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 2, 1, 4),
    _Hh3cAclMib2CharacteristicsIndex_Type()
)
hh3cAclMib2CharacteristicsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclMib2CharacteristicsIndex.setStatus("current")


class _Hh3cAclMib2CharacteristicsDesc_Type(OctetString):
    """Custom type hh3cAclMib2CharacteristicsDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclMib2CharacteristicsDesc_Type.__name__ = "OctetString"
_Hh3cAclMib2CharacteristicsDesc_Object = MibTableColumn
hh3cAclMib2CharacteristicsDesc = _Hh3cAclMib2CharacteristicsDesc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 2, 1, 5),
    _Hh3cAclMib2CharacteristicsDesc_Type()
)
hh3cAclMib2CharacteristicsDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclMib2CharacteristicsDesc.setStatus("current")
_Hh3cAclMib2CharacteristicsValue_Type = Unsigned32
_Hh3cAclMib2CharacteristicsValue_Object = MibTableColumn
hh3cAclMib2CharacteristicsValue = _Hh3cAclMib2CharacteristicsValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 2, 1, 6),
    _Hh3cAclMib2CharacteristicsValue_Type()
)
hh3cAclMib2CharacteristicsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclMib2CharacteristicsValue.setStatus("current")
_Hh3cAclNumberGroupTable_Object = MibTable
hh3cAclNumberGroupTable = _Hh3cAclNumberGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cAclNumberGroupTable.setStatus("current")
_Hh3cAclNumberGroupEntry_Object = MibTableRow
hh3cAclNumberGroupEntry = _Hh3cAclNumberGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 3, 1)
)
hh3cAclNumberGroupEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupType"),
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupIndex"),
)
if mibBuilder.loadTexts:
    hh3cAclNumberGroupEntry.setStatus("current")


class _Hh3cAclNumberGroupType_Type(Integer32):
    """Custom type hh3cAclNumberGroupType based on Integer32"""
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


_Hh3cAclNumberGroupType_Type.__name__ = "Integer32"
_Hh3cAclNumberGroupType_Object = MibTableColumn
hh3cAclNumberGroupType = _Hh3cAclNumberGroupType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 3, 1, 1),
    _Hh3cAclNumberGroupType_Type()
)
hh3cAclNumberGroupType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclNumberGroupType.setStatus("current")


class _Hh3cAclNumberGroupIndex_Type(Integer32):
    """Custom type hh3cAclNumberGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 5999),
        ValueRangeConstraint(10000, 42767),
    )


_Hh3cAclNumberGroupIndex_Type.__name__ = "Integer32"
_Hh3cAclNumberGroupIndex_Object = MibTableColumn
hh3cAclNumberGroupIndex = _Hh3cAclNumberGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 3, 1, 2),
    _Hh3cAclNumberGroupIndex_Type()
)
hh3cAclNumberGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclNumberGroupIndex.setStatus("current")
_Hh3cAclNumberGroupRowStatus_Type = RowStatus
_Hh3cAclNumberGroupRowStatus_Object = MibTableColumn
hh3cAclNumberGroupRowStatus = _Hh3cAclNumberGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 3, 1, 3),
    _Hh3cAclNumberGroupRowStatus_Type()
)
hh3cAclNumberGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNumberGroupRowStatus.setStatus("current")


class _Hh3cAclNumberGroupMatchOrder_Type(Integer32):
    """Custom type hh3cAclNumberGroupMatchOrder based on Integer32"""
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


_Hh3cAclNumberGroupMatchOrder_Type.__name__ = "Integer32"
_Hh3cAclNumberGroupMatchOrder_Object = MibTableColumn
hh3cAclNumberGroupMatchOrder = _Hh3cAclNumberGroupMatchOrder_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 3, 1, 4),
    _Hh3cAclNumberGroupMatchOrder_Type()
)
hh3cAclNumberGroupMatchOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNumberGroupMatchOrder.setStatus("current")


class _Hh3cAclNumberGroupStep_Type(Integer32):
    """Custom type hh3cAclNumberGroupStep based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Hh3cAclNumberGroupStep_Type.__name__ = "Integer32"
_Hh3cAclNumberGroupStep_Object = MibTableColumn
hh3cAclNumberGroupStep = _Hh3cAclNumberGroupStep_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 3, 1, 5),
    _Hh3cAclNumberGroupStep_Type()
)
hh3cAclNumberGroupStep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNumberGroupStep.setStatus("current")


class _Hh3cAclNumberGroupDescription_Type(OctetString):
    """Custom type hh3cAclNumberGroupDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cAclNumberGroupDescription_Type.__name__ = "OctetString"
_Hh3cAclNumberGroupDescription_Object = MibTableColumn
hh3cAclNumberGroupDescription = _Hh3cAclNumberGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 3, 1, 6),
    _Hh3cAclNumberGroupDescription_Type()
)
hh3cAclNumberGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNumberGroupDescription.setStatus("current")


class _Hh3cAclNumberGroupCountClear_Type(CounterClear):
    """Custom type hh3cAclNumberGroupCountClear based on CounterClear"""


_Hh3cAclNumberGroupCountClear_Object = MibTableColumn
hh3cAclNumberGroupCountClear = _Hh3cAclNumberGroupCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 3, 1, 7),
    _Hh3cAclNumberGroupCountClear_Type()
)
hh3cAclNumberGroupCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAclNumberGroupCountClear.setStatus("current")
_Hh3cAclNumberGroupRuleCounter_Type = Counter32
_Hh3cAclNumberGroupRuleCounter_Object = MibTableColumn
hh3cAclNumberGroupRuleCounter = _Hh3cAclNumberGroupRuleCounter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 3, 1, 8),
    _Hh3cAclNumberGroupRuleCounter_Type()
)
hh3cAclNumberGroupRuleCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclNumberGroupRuleCounter.setStatus("current")
_Hh3cAclIPAclGroup_ObjectIdentity = ObjectIdentity
hh3cAclIPAclGroup = _Hh3cAclIPAclGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2)
)
_Hh3cAclIPAclBasicTable_Object = MibTable
hh3cAclIPAclBasicTable = _Hh3cAclIPAclBasicTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicTable.setStatus("current")
_Hh3cAclIPAclBasicEntry_Object = MibTableRow
hh3cAclIPAclBasicEntry = _Hh3cAclIPAclBasicEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1)
)
hh3cAclIPAclBasicEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupType"),
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupIndex"),
    (0, "HH3C-ACL-MIB", "hh3cAclIPAclBasicRuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicEntry.setStatus("current")


class _Hh3cAclIPAclBasicRuleIndex_Type(Integer32):
    """Custom type hh3cAclIPAclBasicRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cAclIPAclBasicRuleIndex_Type.__name__ = "Integer32"
_Hh3cAclIPAclBasicRuleIndex_Object = MibTableColumn
hh3cAclIPAclBasicRuleIndex = _Hh3cAclIPAclBasicRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 1),
    _Hh3cAclIPAclBasicRuleIndex_Type()
)
hh3cAclIPAclBasicRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicRuleIndex.setStatus("current")
_Hh3cAclIPAclBasicRowStatus_Type = RowStatus
_Hh3cAclIPAclBasicRowStatus_Object = MibTableColumn
hh3cAclIPAclBasicRowStatus = _Hh3cAclIPAclBasicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 2),
    _Hh3cAclIPAclBasicRowStatus_Type()
)
hh3cAclIPAclBasicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicRowStatus.setStatus("current")
_Hh3cAclIPAclBasicAct_Type = RuleAction
_Hh3cAclIPAclBasicAct_Object = MibTableColumn
hh3cAclIPAclBasicAct = _Hh3cAclIPAclBasicAct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 3),
    _Hh3cAclIPAclBasicAct_Type()
)
hh3cAclIPAclBasicAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicAct.setStatus("current")
_Hh3cAclIPAclBasicSrcAddrType_Type = InetAddressType
_Hh3cAclIPAclBasicSrcAddrType_Object = MibTableColumn
hh3cAclIPAclBasicSrcAddrType = _Hh3cAclIPAclBasicSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 4),
    _Hh3cAclIPAclBasicSrcAddrType_Type()
)
hh3cAclIPAclBasicSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicSrcAddrType.setStatus("current")
_Hh3cAclIPAclBasicSrcAddr_Type = InetAddress
_Hh3cAclIPAclBasicSrcAddr_Object = MibTableColumn
hh3cAclIPAclBasicSrcAddr = _Hh3cAclIPAclBasicSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 5),
    _Hh3cAclIPAclBasicSrcAddr_Type()
)
hh3cAclIPAclBasicSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicSrcAddr.setStatus("current")
_Hh3cAclIPAclBasicSrcPrefix_Type = InetAddressPrefixLength
_Hh3cAclIPAclBasicSrcPrefix_Object = MibTableColumn
hh3cAclIPAclBasicSrcPrefix = _Hh3cAclIPAclBasicSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 6),
    _Hh3cAclIPAclBasicSrcPrefix_Type()
)
hh3cAclIPAclBasicSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicSrcPrefix.setStatus("current")
_Hh3cAclIPAclBasicSrcAny_Type = TruthValue
_Hh3cAclIPAclBasicSrcAny_Object = MibTableColumn
hh3cAclIPAclBasicSrcAny = _Hh3cAclIPAclBasicSrcAny_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 7),
    _Hh3cAclIPAclBasicSrcAny_Type()
)
hh3cAclIPAclBasicSrcAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicSrcAny.setStatus("current")
_Hh3cAclIPAclBasicSrcWild_Type = IpAddress
_Hh3cAclIPAclBasicSrcWild_Object = MibTableColumn
hh3cAclIPAclBasicSrcWild = _Hh3cAclIPAclBasicSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 8),
    _Hh3cAclIPAclBasicSrcWild_Type()
)
hh3cAclIPAclBasicSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicSrcWild.setStatus("current")


class _Hh3cAclIPAclBasicTimeRangeName_Type(OctetString):
    """Custom type hh3cAclIPAclBasicTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclIPAclBasicTimeRangeName_Type.__name__ = "OctetString"
_Hh3cAclIPAclBasicTimeRangeName_Object = MibTableColumn
hh3cAclIPAclBasicTimeRangeName = _Hh3cAclIPAclBasicTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 9),
    _Hh3cAclIPAclBasicTimeRangeName_Type()
)
hh3cAclIPAclBasicTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicTimeRangeName.setStatus("current")
_Hh3cAclIPAclBasicFragmentFlag_Type = FragmentFlag
_Hh3cAclIPAclBasicFragmentFlag_Object = MibTableColumn
hh3cAclIPAclBasicFragmentFlag = _Hh3cAclIPAclBasicFragmentFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 10),
    _Hh3cAclIPAclBasicFragmentFlag_Type()
)
hh3cAclIPAclBasicFragmentFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicFragmentFlag.setStatus("current")
_Hh3cAclIPAclBasicLog_Type = TruthValue
_Hh3cAclIPAclBasicLog_Object = MibTableColumn
hh3cAclIPAclBasicLog = _Hh3cAclIPAclBasicLog_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 11),
    _Hh3cAclIPAclBasicLog_Type()
)
hh3cAclIPAclBasicLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicLog.setStatus("current")
_Hh3cAclIPAclBasicCount_Type = Unsigned32
_Hh3cAclIPAclBasicCount_Object = MibTableColumn
hh3cAclIPAclBasicCount = _Hh3cAclIPAclBasicCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 12),
    _Hh3cAclIPAclBasicCount_Type()
)
hh3cAclIPAclBasicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicCount.setStatus("current")
_Hh3cAclIPAclBasicCountClear_Type = CounterClear
_Hh3cAclIPAclBasicCountClear_Object = MibTableColumn
hh3cAclIPAclBasicCountClear = _Hh3cAclIPAclBasicCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 13),
    _Hh3cAclIPAclBasicCountClear_Type()
)
hh3cAclIPAclBasicCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicCountClear.setStatus("current")
_Hh3cAclIPAclBasicEnable_Type = TruthValue
_Hh3cAclIPAclBasicEnable_Object = MibTableColumn
hh3cAclIPAclBasicEnable = _Hh3cAclIPAclBasicEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 14),
    _Hh3cAclIPAclBasicEnable_Type()
)
hh3cAclIPAclBasicEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicEnable.setStatus("current")


class _Hh3cAclIPAclBasicVpnInstanceName_Type(OctetString):
    """Custom type hh3cAclIPAclBasicVpnInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclIPAclBasicVpnInstanceName_Type.__name__ = "OctetString"
_Hh3cAclIPAclBasicVpnInstanceName_Object = MibTableColumn
hh3cAclIPAclBasicVpnInstanceName = _Hh3cAclIPAclBasicVpnInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 15),
    _Hh3cAclIPAclBasicVpnInstanceName_Type()
)
hh3cAclIPAclBasicVpnInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicVpnInstanceName.setStatus("current")


class _Hh3cAclIPAclBasicComment_Type(OctetString):
    """Custom type hh3cAclIPAclBasicComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cAclIPAclBasicComment_Type.__name__ = "OctetString"
_Hh3cAclIPAclBasicComment_Object = MibTableColumn
hh3cAclIPAclBasicComment = _Hh3cAclIPAclBasicComment_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 16),
    _Hh3cAclIPAclBasicComment_Type()
)
hh3cAclIPAclBasicComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicComment.setStatus("current")
_Hh3cAclIPAclAdvancedTable_Object = MibTable
hh3cAclIPAclAdvancedTable = _Hh3cAclIPAclAdvancedTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedTable.setStatus("current")
_Hh3cAclIPAclAdvancedEntry_Object = MibTableRow
hh3cAclIPAclAdvancedEntry = _Hh3cAclIPAclAdvancedEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1)
)
hh3cAclIPAclAdvancedEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupType"),
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupIndex"),
    (0, "HH3C-ACL-MIB", "hh3cAclIPAclAdvancedRuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedEntry.setStatus("current")


class _Hh3cAclIPAclAdvancedRuleIndex_Type(Integer32):
    """Custom type hh3cAclIPAclAdvancedRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cAclIPAclAdvancedRuleIndex_Type.__name__ = "Integer32"
_Hh3cAclIPAclAdvancedRuleIndex_Object = MibTableColumn
hh3cAclIPAclAdvancedRuleIndex = _Hh3cAclIPAclAdvancedRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 1),
    _Hh3cAclIPAclAdvancedRuleIndex_Type()
)
hh3cAclIPAclAdvancedRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedRuleIndex.setStatus("current")
_Hh3cAclIPAclAdvancedRowStatus_Type = RowStatus
_Hh3cAclIPAclAdvancedRowStatus_Object = MibTableColumn
hh3cAclIPAclAdvancedRowStatus = _Hh3cAclIPAclAdvancedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 2),
    _Hh3cAclIPAclAdvancedRowStatus_Type()
)
hh3cAclIPAclAdvancedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedRowStatus.setStatus("current")
_Hh3cAclIPAclAdvancedAct_Type = RuleAction
_Hh3cAclIPAclAdvancedAct_Object = MibTableColumn
hh3cAclIPAclAdvancedAct = _Hh3cAclIPAclAdvancedAct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 3),
    _Hh3cAclIPAclAdvancedAct_Type()
)
hh3cAclIPAclAdvancedAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedAct.setStatus("current")


class _Hh3cAclIPAclAdvancedProtocol_Type(Integer32):
    """Custom type hh3cAclIPAclAdvancedProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cAclIPAclAdvancedProtocol_Type.__name__ = "Integer32"
_Hh3cAclIPAclAdvancedProtocol_Object = MibTableColumn
hh3cAclIPAclAdvancedProtocol = _Hh3cAclIPAclAdvancedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 4),
    _Hh3cAclIPAclAdvancedProtocol_Type()
)
hh3cAclIPAclAdvancedProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedProtocol.setStatus("current")


class _Hh3cAclIPAclAdvancedAddrFlag_Type(AddressFlag):
    """Custom type hh3cAclIPAclAdvancedAddrFlag based on AddressFlag"""


_Hh3cAclIPAclAdvancedAddrFlag_Object = MibTableColumn
hh3cAclIPAclAdvancedAddrFlag = _Hh3cAclIPAclAdvancedAddrFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 5),
    _Hh3cAclIPAclAdvancedAddrFlag_Type()
)
hh3cAclIPAclAdvancedAddrFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedAddrFlag.setStatus("current")
_Hh3cAclIPAclAdvancedSrcAddrType_Type = InetAddressType
_Hh3cAclIPAclAdvancedSrcAddrType_Object = MibTableColumn
hh3cAclIPAclAdvancedSrcAddrType = _Hh3cAclIPAclAdvancedSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 6),
    _Hh3cAclIPAclAdvancedSrcAddrType_Type()
)
hh3cAclIPAclAdvancedSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedSrcAddrType.setStatus("current")
_Hh3cAclIPAclAdvancedSrcAddr_Type = InetAddress
_Hh3cAclIPAclAdvancedSrcAddr_Object = MibTableColumn
hh3cAclIPAclAdvancedSrcAddr = _Hh3cAclIPAclAdvancedSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 7),
    _Hh3cAclIPAclAdvancedSrcAddr_Type()
)
hh3cAclIPAclAdvancedSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedSrcAddr.setStatus("current")
_Hh3cAclIPAclAdvancedSrcPrefix_Type = InetAddressPrefixLength
_Hh3cAclIPAclAdvancedSrcPrefix_Object = MibTableColumn
hh3cAclIPAclAdvancedSrcPrefix = _Hh3cAclIPAclAdvancedSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 8),
    _Hh3cAclIPAclAdvancedSrcPrefix_Type()
)
hh3cAclIPAclAdvancedSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedSrcPrefix.setStatus("current")


class _Hh3cAclIPAclAdvancedSrcAny_Type(TruthValue):
    """Custom type hh3cAclIPAclAdvancedSrcAny based on TruthValue"""


_Hh3cAclIPAclAdvancedSrcAny_Object = MibTableColumn
hh3cAclIPAclAdvancedSrcAny = _Hh3cAclIPAclAdvancedSrcAny_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 9),
    _Hh3cAclIPAclAdvancedSrcAny_Type()
)
hh3cAclIPAclAdvancedSrcAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedSrcAny.setStatus("current")
_Hh3cAclIPAclAdvancedSrcWild_Type = IpAddress
_Hh3cAclIPAclAdvancedSrcWild_Object = MibTableColumn
hh3cAclIPAclAdvancedSrcWild = _Hh3cAclIPAclAdvancedSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 10),
    _Hh3cAclIPAclAdvancedSrcWild_Type()
)
hh3cAclIPAclAdvancedSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedSrcWild.setStatus("current")
_Hh3cAclIPAclAdvancedSrcOp_Type = PortOp
_Hh3cAclIPAclAdvancedSrcOp_Object = MibTableColumn
hh3cAclIPAclAdvancedSrcOp = _Hh3cAclIPAclAdvancedSrcOp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 11),
    _Hh3cAclIPAclAdvancedSrcOp_Type()
)
hh3cAclIPAclAdvancedSrcOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedSrcOp.setStatus("current")


class _Hh3cAclIPAclAdvancedSrcPort1_Type(Integer32):
    """Custom type hh3cAclIPAclAdvancedSrcPort1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclIPAclAdvancedSrcPort1_Type.__name__ = "Integer32"
_Hh3cAclIPAclAdvancedSrcPort1_Object = MibTableColumn
hh3cAclIPAclAdvancedSrcPort1 = _Hh3cAclIPAclAdvancedSrcPort1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 12),
    _Hh3cAclIPAclAdvancedSrcPort1_Type()
)
hh3cAclIPAclAdvancedSrcPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedSrcPort1.setStatus("current")


class _Hh3cAclIPAclAdvancedSrcPort2_Type(Integer32):
    """Custom type hh3cAclIPAclAdvancedSrcPort2 based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclIPAclAdvancedSrcPort2_Type.__name__ = "Integer32"
_Hh3cAclIPAclAdvancedSrcPort2_Object = MibTableColumn
hh3cAclIPAclAdvancedSrcPort2 = _Hh3cAclIPAclAdvancedSrcPort2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 13),
    _Hh3cAclIPAclAdvancedSrcPort2_Type()
)
hh3cAclIPAclAdvancedSrcPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedSrcPort2.setStatus("current")
_Hh3cAclIPAclAdvancedDestAddrType_Type = InetAddressType
_Hh3cAclIPAclAdvancedDestAddrType_Object = MibTableColumn
hh3cAclIPAclAdvancedDestAddrType = _Hh3cAclIPAclAdvancedDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 14),
    _Hh3cAclIPAclAdvancedDestAddrType_Type()
)
hh3cAclIPAclAdvancedDestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedDestAddrType.setStatus("current")
_Hh3cAclIPAclAdvancedDestAddr_Type = InetAddress
_Hh3cAclIPAclAdvancedDestAddr_Object = MibTableColumn
hh3cAclIPAclAdvancedDestAddr = _Hh3cAclIPAclAdvancedDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 15),
    _Hh3cAclIPAclAdvancedDestAddr_Type()
)
hh3cAclIPAclAdvancedDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedDestAddr.setStatus("current")
_Hh3cAclIPAclAdvancedDestPrefix_Type = InetAddressPrefixLength
_Hh3cAclIPAclAdvancedDestPrefix_Object = MibTableColumn
hh3cAclIPAclAdvancedDestPrefix = _Hh3cAclIPAclAdvancedDestPrefix_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 16),
    _Hh3cAclIPAclAdvancedDestPrefix_Type()
)
hh3cAclIPAclAdvancedDestPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedDestPrefix.setStatus("current")


class _Hh3cAclIPAclAdvancedDestAny_Type(TruthValue):
    """Custom type hh3cAclIPAclAdvancedDestAny based on TruthValue"""


_Hh3cAclIPAclAdvancedDestAny_Object = MibTableColumn
hh3cAclIPAclAdvancedDestAny = _Hh3cAclIPAclAdvancedDestAny_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 17),
    _Hh3cAclIPAclAdvancedDestAny_Type()
)
hh3cAclIPAclAdvancedDestAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedDestAny.setStatus("current")
_Hh3cAclIPAclAdvancedDestWild_Type = IpAddress
_Hh3cAclIPAclAdvancedDestWild_Object = MibTableColumn
hh3cAclIPAclAdvancedDestWild = _Hh3cAclIPAclAdvancedDestWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 18),
    _Hh3cAclIPAclAdvancedDestWild_Type()
)
hh3cAclIPAclAdvancedDestWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedDestWild.setStatus("current")
_Hh3cAclIPAclAdvancedDestOp_Type = PortOp
_Hh3cAclIPAclAdvancedDestOp_Object = MibTableColumn
hh3cAclIPAclAdvancedDestOp = _Hh3cAclIPAclAdvancedDestOp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 19),
    _Hh3cAclIPAclAdvancedDestOp_Type()
)
hh3cAclIPAclAdvancedDestOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedDestOp.setStatus("current")


class _Hh3cAclIPAclAdvancedDestPort1_Type(Integer32):
    """Custom type hh3cAclIPAclAdvancedDestPort1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclIPAclAdvancedDestPort1_Type.__name__ = "Integer32"
_Hh3cAclIPAclAdvancedDestPort1_Object = MibTableColumn
hh3cAclIPAclAdvancedDestPort1 = _Hh3cAclIPAclAdvancedDestPort1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 20),
    _Hh3cAclIPAclAdvancedDestPort1_Type()
)
hh3cAclIPAclAdvancedDestPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedDestPort1.setStatus("current")


class _Hh3cAclIPAclAdvancedDestPort2_Type(Integer32):
    """Custom type hh3cAclIPAclAdvancedDestPort2 based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclIPAclAdvancedDestPort2_Type.__name__ = "Integer32"
_Hh3cAclIPAclAdvancedDestPort2_Object = MibTableColumn
hh3cAclIPAclAdvancedDestPort2 = _Hh3cAclIPAclAdvancedDestPort2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 21),
    _Hh3cAclIPAclAdvancedDestPort2_Type()
)
hh3cAclIPAclAdvancedDestPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedDestPort2.setStatus("current")


class _Hh3cAclIPAclAdvancedIcmpType_Type(Integer32):
    """Custom type hh3cAclIPAclAdvancedIcmpType based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cAclIPAclAdvancedIcmpType_Type.__name__ = "Integer32"
_Hh3cAclIPAclAdvancedIcmpType_Object = MibTableColumn
hh3cAclIPAclAdvancedIcmpType = _Hh3cAclIPAclAdvancedIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 22),
    _Hh3cAclIPAclAdvancedIcmpType_Type()
)
hh3cAclIPAclAdvancedIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedIcmpType.setStatus("current")


class _Hh3cAclIPAclAdvancedIcmpCode_Type(Integer32):
    """Custom type hh3cAclIPAclAdvancedIcmpCode based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cAclIPAclAdvancedIcmpCode_Type.__name__ = "Integer32"
_Hh3cAclIPAclAdvancedIcmpCode_Object = MibTableColumn
hh3cAclIPAclAdvancedIcmpCode = _Hh3cAclIPAclAdvancedIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 23),
    _Hh3cAclIPAclAdvancedIcmpCode_Type()
)
hh3cAclIPAclAdvancedIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedIcmpCode.setStatus("current")


class _Hh3cAclIPAclAdvancedPrecedence_Type(Integer32):
    """Custom type hh3cAclIPAclAdvancedPrecedence based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cAclIPAclAdvancedPrecedence_Type.__name__ = "Integer32"
_Hh3cAclIPAclAdvancedPrecedence_Object = MibTableColumn
hh3cAclIPAclAdvancedPrecedence = _Hh3cAclIPAclAdvancedPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 24),
    _Hh3cAclIPAclAdvancedPrecedence_Type()
)
hh3cAclIPAclAdvancedPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedPrecedence.setStatus("current")


class _Hh3cAclIPAclAdvancedTos_Type(Integer32):
    """Custom type hh3cAclIPAclAdvancedTos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_Hh3cAclIPAclAdvancedTos_Type.__name__ = "Integer32"
_Hh3cAclIPAclAdvancedTos_Object = MibTableColumn
hh3cAclIPAclAdvancedTos = _Hh3cAclIPAclAdvancedTos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 25),
    _Hh3cAclIPAclAdvancedTos_Type()
)
hh3cAclIPAclAdvancedTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedTos.setStatus("current")


class _Hh3cAclIPAclAdvancedDscp_Type(DSCPValue):
    """Custom type hh3cAclIPAclAdvancedDscp based on DSCPValue"""
    defaultValue = 255


_Hh3cAclIPAclAdvancedDscp_Object = MibTableColumn
hh3cAclIPAclAdvancedDscp = _Hh3cAclIPAclAdvancedDscp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 26),
    _Hh3cAclIPAclAdvancedDscp_Type()
)
hh3cAclIPAclAdvancedDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedDscp.setStatus("current")


class _Hh3cAclIPAclAdvancedTimeRangeName_Type(OctetString):
    """Custom type hh3cAclIPAclAdvancedTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclIPAclAdvancedTimeRangeName_Type.__name__ = "OctetString"
_Hh3cAclIPAclAdvancedTimeRangeName_Object = MibTableColumn
hh3cAclIPAclAdvancedTimeRangeName = _Hh3cAclIPAclAdvancedTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 27),
    _Hh3cAclIPAclAdvancedTimeRangeName_Type()
)
hh3cAclIPAclAdvancedTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedTimeRangeName.setStatus("current")


class _Hh3cAclIPAclAdvancedTCPFlag_Type(TCPFlag):
    """Custom type hh3cAclIPAclAdvancedTCPFlag based on TCPFlag"""


_Hh3cAclIPAclAdvancedTCPFlag_Object = MibTableColumn
hh3cAclIPAclAdvancedTCPFlag = _Hh3cAclIPAclAdvancedTCPFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 28),
    _Hh3cAclIPAclAdvancedTCPFlag_Type()
)
hh3cAclIPAclAdvancedTCPFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedTCPFlag.setStatus("current")


class _Hh3cAclIPAclAdvancedFragmentFlag_Type(FragmentFlag):
    """Custom type hh3cAclIPAclAdvancedFragmentFlag based on FragmentFlag"""


_Hh3cAclIPAclAdvancedFragmentFlag_Object = MibTableColumn
hh3cAclIPAclAdvancedFragmentFlag = _Hh3cAclIPAclAdvancedFragmentFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 29),
    _Hh3cAclIPAclAdvancedFragmentFlag_Type()
)
hh3cAclIPAclAdvancedFragmentFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedFragmentFlag.setStatus("current")


class _Hh3cAclIPAclAdvancedLog_Type(TruthValue):
    """Custom type hh3cAclIPAclAdvancedLog based on TruthValue"""


_Hh3cAclIPAclAdvancedLog_Object = MibTableColumn
hh3cAclIPAclAdvancedLog = _Hh3cAclIPAclAdvancedLog_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 30),
    _Hh3cAclIPAclAdvancedLog_Type()
)
hh3cAclIPAclAdvancedLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedLog.setStatus("current")
_Hh3cAclIPAclAdvancedCount_Type = Unsigned32
_Hh3cAclIPAclAdvancedCount_Object = MibTableColumn
hh3cAclIPAclAdvancedCount = _Hh3cAclIPAclAdvancedCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 31),
    _Hh3cAclIPAclAdvancedCount_Type()
)
hh3cAclIPAclAdvancedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedCount.setStatus("current")


class _Hh3cAclIPAclAdvancedCountClear_Type(CounterClear):
    """Custom type hh3cAclIPAclAdvancedCountClear based on CounterClear"""


_Hh3cAclIPAclAdvancedCountClear_Object = MibTableColumn
hh3cAclIPAclAdvancedCountClear = _Hh3cAclIPAclAdvancedCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 32),
    _Hh3cAclIPAclAdvancedCountClear_Type()
)
hh3cAclIPAclAdvancedCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedCountClear.setStatus("current")


class _Hh3cAclIPAclAdvancedEnable_Type(TruthValue):
    """Custom type hh3cAclIPAclAdvancedEnable based on TruthValue"""


_Hh3cAclIPAclAdvancedEnable_Object = MibTableColumn
hh3cAclIPAclAdvancedEnable = _Hh3cAclIPAclAdvancedEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 33),
    _Hh3cAclIPAclAdvancedEnable_Type()
)
hh3cAclIPAclAdvancedEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedEnable.setStatus("current")


class _Hh3cAclIPAclAdvancedVpnInstanceName_Type(OctetString):
    """Custom type hh3cAclIPAclAdvancedVpnInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclIPAclAdvancedVpnInstanceName_Type.__name__ = "OctetString"
_Hh3cAclIPAclAdvancedVpnInstanceName_Object = MibTableColumn
hh3cAclIPAclAdvancedVpnInstanceName = _Hh3cAclIPAclAdvancedVpnInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 34),
    _Hh3cAclIPAclAdvancedVpnInstanceName_Type()
)
hh3cAclIPAclAdvancedVpnInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedVpnInstanceName.setStatus("current")


class _Hh3cAclIPAclAdvancedComment_Type(OctetString):
    """Custom type hh3cAclIPAclAdvancedComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cAclIPAclAdvancedComment_Type.__name__ = "OctetString"
_Hh3cAclIPAclAdvancedComment_Object = MibTableColumn
hh3cAclIPAclAdvancedComment = _Hh3cAclIPAclAdvancedComment_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 35),
    _Hh3cAclIPAclAdvancedComment_Type()
)
hh3cAclIPAclAdvancedComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedComment.setStatus("current")
_Hh3cAclIPAclAdvancedReflective_Type = TruthValue
_Hh3cAclIPAclAdvancedReflective_Object = MibTableColumn
hh3cAclIPAclAdvancedReflective = _Hh3cAclIPAclAdvancedReflective_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 36),
    _Hh3cAclIPAclAdvancedReflective_Type()
)
hh3cAclIPAclAdvancedReflective.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedReflective.setStatus("current")
_Hh3cAclMACAclGroup_ObjectIdentity = ObjectIdentity
hh3cAclMACAclGroup = _Hh3cAclMACAclGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3)
)
_Hh3cAclMACTable_Object = MibTable
hh3cAclMACTable = _Hh3cAclMACTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cAclMACTable.setStatus("current")
_Hh3cAclMACEntry_Object = MibTableRow
hh3cAclMACEntry = _Hh3cAclMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1)
)
hh3cAclMACEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupType"),
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupIndex"),
    (0, "HH3C-ACL-MIB", "hh3cAclMACRuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cAclMACEntry.setStatus("current")


class _Hh3cAclMACRuleIndex_Type(Integer32):
    """Custom type hh3cAclMACRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cAclMACRuleIndex_Type.__name__ = "Integer32"
_Hh3cAclMACRuleIndex_Object = MibTableColumn
hh3cAclMACRuleIndex = _Hh3cAclMACRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 1),
    _Hh3cAclMACRuleIndex_Type()
)
hh3cAclMACRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclMACRuleIndex.setStatus("current")
_Hh3cAclMACRowStatus_Type = RowStatus
_Hh3cAclMACRowStatus_Object = MibTableColumn
hh3cAclMACRowStatus = _Hh3cAclMACRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 2),
    _Hh3cAclMACRowStatus_Type()
)
hh3cAclMACRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACRowStatus.setStatus("current")
_Hh3cAclMACAct_Type = RuleAction
_Hh3cAclMACAct_Object = MibTableColumn
hh3cAclMACAct = _Hh3cAclMACAct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 3),
    _Hh3cAclMACAct_Type()
)
hh3cAclMACAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACAct.setStatus("current")


class _Hh3cAclMACTypeCode_Type(OctetString):
    """Custom type hh3cAclMACTypeCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclMACTypeCode_Type.__name__ = "OctetString"
_Hh3cAclMACTypeCode_Object = MibTableColumn
hh3cAclMACTypeCode = _Hh3cAclMACTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 4),
    _Hh3cAclMACTypeCode_Type()
)
hh3cAclMACTypeCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACTypeCode.setStatus("current")


class _Hh3cAclMACTypeMask_Type(OctetString):
    """Custom type hh3cAclMACTypeMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclMACTypeMask_Type.__name__ = "OctetString"
_Hh3cAclMACTypeMask_Object = MibTableColumn
hh3cAclMACTypeMask = _Hh3cAclMACTypeMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 5),
    _Hh3cAclMACTypeMask_Type()
)
hh3cAclMACTypeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACTypeMask.setStatus("current")
_Hh3cAclMACSrcMac_Type = MacAddress
_Hh3cAclMACSrcMac_Object = MibTableColumn
hh3cAclMACSrcMac = _Hh3cAclMACSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 6),
    _Hh3cAclMACSrcMac_Type()
)
hh3cAclMACSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACSrcMac.setStatus("current")
_Hh3cAclMACSrcMacWild_Type = MacAddress
_Hh3cAclMACSrcMacWild_Object = MibTableColumn
hh3cAclMACSrcMacWild = _Hh3cAclMACSrcMacWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 7),
    _Hh3cAclMACSrcMacWild_Type()
)
hh3cAclMACSrcMacWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACSrcMacWild.setStatus("current")
_Hh3cAclMACDestMac_Type = MacAddress
_Hh3cAclMACDestMac_Object = MibTableColumn
hh3cAclMACDestMac = _Hh3cAclMACDestMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 8),
    _Hh3cAclMACDestMac_Type()
)
hh3cAclMACDestMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACDestMac.setStatus("current")
_Hh3cAclMACDestMacWild_Type = MacAddress
_Hh3cAclMACDestMacWild_Object = MibTableColumn
hh3cAclMACDestMacWild = _Hh3cAclMACDestMacWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 9),
    _Hh3cAclMACDestMacWild_Type()
)
hh3cAclMACDestMacWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACDestMacWild.setStatus("current")


class _Hh3cAclMACLsapCode_Type(OctetString):
    """Custom type hh3cAclMACLsapCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclMACLsapCode_Type.__name__ = "OctetString"
_Hh3cAclMACLsapCode_Object = MibTableColumn
hh3cAclMACLsapCode = _Hh3cAclMACLsapCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 10),
    _Hh3cAclMACLsapCode_Type()
)
hh3cAclMACLsapCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACLsapCode.setStatus("current")


class _Hh3cAclMACLsapMask_Type(OctetString):
    """Custom type hh3cAclMACLsapMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclMACLsapMask_Type.__name__ = "OctetString"
_Hh3cAclMACLsapMask_Object = MibTableColumn
hh3cAclMACLsapMask = _Hh3cAclMACLsapMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 11),
    _Hh3cAclMACLsapMask_Type()
)
hh3cAclMACLsapMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACLsapMask.setStatus("current")
_Hh3cAclMACCos_Type = Integer32
_Hh3cAclMACCos_Object = MibTableColumn
hh3cAclMACCos = _Hh3cAclMACCos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 12),
    _Hh3cAclMACCos_Type()
)
hh3cAclMACCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACCos.setStatus("current")


class _Hh3cAclMACTimeRangeName_Type(OctetString):
    """Custom type hh3cAclMACTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclMACTimeRangeName_Type.__name__ = "OctetString"
_Hh3cAclMACTimeRangeName_Object = MibTableColumn
hh3cAclMACTimeRangeName = _Hh3cAclMACTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 13),
    _Hh3cAclMACTimeRangeName_Type()
)
hh3cAclMACTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACTimeRangeName.setStatus("current")
_Hh3cAclMACCount_Type = Unsigned32
_Hh3cAclMACCount_Object = MibTableColumn
hh3cAclMACCount = _Hh3cAclMACCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 14),
    _Hh3cAclMACCount_Type()
)
hh3cAclMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclMACCount.setStatus("current")
_Hh3cAclMACCountClear_Type = CounterClear
_Hh3cAclMACCountClear_Object = MibTableColumn
hh3cAclMACCountClear = _Hh3cAclMACCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 15),
    _Hh3cAclMACCountClear_Type()
)
hh3cAclMACCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAclMACCountClear.setStatus("current")


class _Hh3cAclMACEnable_Type(TruthValue):
    """Custom type hh3cAclMACEnable based on TruthValue"""


_Hh3cAclMACEnable_Object = MibTableColumn
hh3cAclMACEnable = _Hh3cAclMACEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 16),
    _Hh3cAclMACEnable_Type()
)
hh3cAclMACEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclMACEnable.setStatus("current")


class _Hh3cAclMACComment_Type(OctetString):
    """Custom type hh3cAclMACComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cAclMACComment_Type.__name__ = "OctetString"
_Hh3cAclMACComment_Object = MibTableColumn
hh3cAclMACComment = _Hh3cAclMACComment_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 17),
    _Hh3cAclMACComment_Type()
)
hh3cAclMACComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACComment.setStatus("current")
_Hh3cAclEnUserAclGroup_ObjectIdentity = ObjectIdentity
hh3cAclEnUserAclGroup = _Hh3cAclEnUserAclGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4)
)
_Hh3cAclEnUserTable_Object = MibTable
hh3cAclEnUserTable = _Hh3cAclEnUserTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3)
)
if mibBuilder.loadTexts:
    hh3cAclEnUserTable.setStatus("current")
_Hh3cAclEnUserEntry_Object = MibTableRow
hh3cAclEnUserEntry = _Hh3cAclEnUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1)
)
hh3cAclEnUserEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupType"),
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupIndex"),
    (0, "HH3C-ACL-MIB", "hh3cAclEnUserRuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cAclEnUserEntry.setStatus("current")


class _Hh3cAclEnUserRuleIndex_Type(Integer32):
    """Custom type hh3cAclEnUserRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cAclEnUserRuleIndex_Type.__name__ = "Integer32"
_Hh3cAclEnUserRuleIndex_Object = MibTableColumn
hh3cAclEnUserRuleIndex = _Hh3cAclEnUserRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 1),
    _Hh3cAclEnUserRuleIndex_Type()
)
hh3cAclEnUserRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclEnUserRuleIndex.setStatus("current")
_Hh3cAclEnUserRowStatus_Type = RowStatus
_Hh3cAclEnUserRowStatus_Object = MibTableColumn
hh3cAclEnUserRowStatus = _Hh3cAclEnUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 2),
    _Hh3cAclEnUserRowStatus_Type()
)
hh3cAclEnUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclEnUserRowStatus.setStatus("current")
_Hh3cAclEnUserAct_Type = RuleAction
_Hh3cAclEnUserAct_Object = MibTableColumn
hh3cAclEnUserAct = _Hh3cAclEnUserAct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 3),
    _Hh3cAclEnUserAct_Type()
)
hh3cAclEnUserAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclEnUserAct.setStatus("current")


class _Hh3cAclEnUserStartString_Type(OctetString):
    """Custom type hh3cAclEnUserStartString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclEnUserStartString_Type.__name__ = "OctetString"
_Hh3cAclEnUserStartString_Object = MibTableColumn
hh3cAclEnUserStartString = _Hh3cAclEnUserStartString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 4),
    _Hh3cAclEnUserStartString_Type()
)
hh3cAclEnUserStartString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclEnUserStartString.setStatus("current")


class _Hh3cAclEnUserL2String_Type(OctetString):
    """Custom type hh3cAclEnUserL2String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclEnUserL2String_Type.__name__ = "OctetString"
_Hh3cAclEnUserL2String_Object = MibTableColumn
hh3cAclEnUserL2String = _Hh3cAclEnUserL2String_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 5),
    _Hh3cAclEnUserL2String_Type()
)
hh3cAclEnUserL2String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclEnUserL2String.setStatus("current")


class _Hh3cAclEnUserMplsString_Type(OctetString):
    """Custom type hh3cAclEnUserMplsString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclEnUserMplsString_Type.__name__ = "OctetString"
_Hh3cAclEnUserMplsString_Object = MibTableColumn
hh3cAclEnUserMplsString = _Hh3cAclEnUserMplsString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 6),
    _Hh3cAclEnUserMplsString_Type()
)
hh3cAclEnUserMplsString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclEnUserMplsString.setStatus("current")


class _Hh3cAclEnUserIPv4String_Type(OctetString):
    """Custom type hh3cAclEnUserIPv4String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclEnUserIPv4String_Type.__name__ = "OctetString"
_Hh3cAclEnUserIPv4String_Object = MibTableColumn
hh3cAclEnUserIPv4String = _Hh3cAclEnUserIPv4String_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 7),
    _Hh3cAclEnUserIPv4String_Type()
)
hh3cAclEnUserIPv4String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclEnUserIPv4String.setStatus("current")


class _Hh3cAclEnUserIPv6String_Type(OctetString):
    """Custom type hh3cAclEnUserIPv6String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclEnUserIPv6String_Type.__name__ = "OctetString"
_Hh3cAclEnUserIPv6String_Object = MibTableColumn
hh3cAclEnUserIPv6String = _Hh3cAclEnUserIPv6String_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 8),
    _Hh3cAclEnUserIPv6String_Type()
)
hh3cAclEnUserIPv6String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclEnUserIPv6String.setStatus("current")


class _Hh3cAclEnUserL4String_Type(OctetString):
    """Custom type hh3cAclEnUserL4String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclEnUserL4String_Type.__name__ = "OctetString"
_Hh3cAclEnUserL4String_Object = MibTableColumn
hh3cAclEnUserL4String = _Hh3cAclEnUserL4String_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 9),
    _Hh3cAclEnUserL4String_Type()
)
hh3cAclEnUserL4String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclEnUserL4String.setStatus("current")


class _Hh3cAclEnUserL5String_Type(OctetString):
    """Custom type hh3cAclEnUserL5String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclEnUserL5String_Type.__name__ = "OctetString"
_Hh3cAclEnUserL5String_Object = MibTableColumn
hh3cAclEnUserL5String = _Hh3cAclEnUserL5String_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 10),
    _Hh3cAclEnUserL5String_Type()
)
hh3cAclEnUserL5String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclEnUserL5String.setStatus("current")


class _Hh3cAclEnUserTimeRangeName_Type(OctetString):
    """Custom type hh3cAclEnUserTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclEnUserTimeRangeName_Type.__name__ = "OctetString"
_Hh3cAclEnUserTimeRangeName_Object = MibTableColumn
hh3cAclEnUserTimeRangeName = _Hh3cAclEnUserTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 11),
    _Hh3cAclEnUserTimeRangeName_Type()
)
hh3cAclEnUserTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclEnUserTimeRangeName.setStatus("current")
_Hh3cAclEnUserCount_Type = Unsigned32
_Hh3cAclEnUserCount_Object = MibTableColumn
hh3cAclEnUserCount = _Hh3cAclEnUserCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 12),
    _Hh3cAclEnUserCount_Type()
)
hh3cAclEnUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclEnUserCount.setStatus("current")
_Hh3cAclEnUserCountClear_Type = CounterClear
_Hh3cAclEnUserCountClear_Object = MibTableColumn
hh3cAclEnUserCountClear = _Hh3cAclEnUserCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 13),
    _Hh3cAclEnUserCountClear_Type()
)
hh3cAclEnUserCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAclEnUserCountClear.setStatus("current")


class _Hh3cAclEnUserEnable_Type(TruthValue):
    """Custom type hh3cAclEnUserEnable based on TruthValue"""


_Hh3cAclEnUserEnable_Object = MibTableColumn
hh3cAclEnUserEnable = _Hh3cAclEnUserEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 14),
    _Hh3cAclEnUserEnable_Type()
)
hh3cAclEnUserEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclEnUserEnable.setStatus("current")


class _Hh3cAclEnUserComment_Type(OctetString):
    """Custom type hh3cAclEnUserComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cAclEnUserComment_Type.__name__ = "OctetString"
_Hh3cAclEnUserComment_Object = MibTableColumn
hh3cAclEnUserComment = _Hh3cAclEnUserComment_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 15),
    _Hh3cAclEnUserComment_Type()
)
hh3cAclEnUserComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclEnUserComment.setStatus("current")
_Hh3cAclResourceGroup_ObjectIdentity = ObjectIdentity
hh3cAclResourceGroup = _Hh3cAclResourceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5)
)
_Hh3cAclResourceUsageTable_Object = MibTable
hh3cAclResourceUsageTable = _Hh3cAclResourceUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5, 1)
)
if mibBuilder.loadTexts:
    hh3cAclResourceUsageTable.setStatus("current")
_Hh3cAclResourceUsageEntry_Object = MibTableRow
hh3cAclResourceUsageEntry = _Hh3cAclResourceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5, 1, 1)
)
hh3cAclResourceUsageEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclResourceChassis"),
    (0, "HH3C-ACL-MIB", "hh3cAclResourceSlot"),
    (0, "HH3C-ACL-MIB", "hh3cAclResourceChip"),
    (0, "HH3C-ACL-MIB", "hh3cAclResourceType"),
)
if mibBuilder.loadTexts:
    hh3cAclResourceUsageEntry.setStatus("current")
_Hh3cAclResourceChassis_Type = Unsigned32
_Hh3cAclResourceChassis_Object = MibTableColumn
hh3cAclResourceChassis = _Hh3cAclResourceChassis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5, 1, 1, 1),
    _Hh3cAclResourceChassis_Type()
)
hh3cAclResourceChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclResourceChassis.setStatus("current")
_Hh3cAclResourceSlot_Type = Unsigned32
_Hh3cAclResourceSlot_Object = MibTableColumn
hh3cAclResourceSlot = _Hh3cAclResourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5, 1, 1, 2),
    _Hh3cAclResourceSlot_Type()
)
hh3cAclResourceSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclResourceSlot.setStatus("current")
_Hh3cAclResourceChip_Type = Unsigned32
_Hh3cAclResourceChip_Object = MibTableColumn
hh3cAclResourceChip = _Hh3cAclResourceChip_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5, 1, 1, 3),
    _Hh3cAclResourceChip_Type()
)
hh3cAclResourceChip.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclResourceChip.setStatus("current")


class _Hh3cAclResourceType_Type(Integer32):
    """Custom type hh3cAclResourceType based on Integer32"""
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
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("aclRuleResource", 8),
          ("counterResource", 10),
          ("efpAclResource", 5),
          ("efpCounterResource", 7),
          ("efpMeterResource", 6),
          ("egressAclResource", 12),
          ("ifpAclResource", 2),
          ("ifpCounterResource", 4),
          ("ifpMeterResource", 3),
          ("ingressAclResource", 11),
          ("ipv4AclResource", 13),
          ("ipv6AclResource", 14),
          ("meterResource", 9),
          ("vfpAclResource", 1))
    )


_Hh3cAclResourceType_Type.__name__ = "Integer32"
_Hh3cAclResourceType_Object = MibTableColumn
hh3cAclResourceType = _Hh3cAclResourceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5, 1, 1, 4),
    _Hh3cAclResourceType_Type()
)
hh3cAclResourceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclResourceType.setStatus("current")
_Hh3cAclPortRange_Type = OctetString
_Hh3cAclPortRange_Object = MibTableColumn
hh3cAclPortRange = _Hh3cAclPortRange_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5, 1, 1, 5),
    _Hh3cAclPortRange_Type()
)
hh3cAclPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclPortRange.setStatus("current")
_Hh3cAclResourceTotal_Type = Unsigned32
_Hh3cAclResourceTotal_Object = MibTableColumn
hh3cAclResourceTotal = _Hh3cAclResourceTotal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5, 1, 1, 6),
    _Hh3cAclResourceTotal_Type()
)
hh3cAclResourceTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclResourceTotal.setStatus("current")
_Hh3cAclResourceReserved_Type = Unsigned32
_Hh3cAclResourceReserved_Object = MibTableColumn
hh3cAclResourceReserved = _Hh3cAclResourceReserved_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5, 1, 1, 7),
    _Hh3cAclResourceReserved_Type()
)
hh3cAclResourceReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclResourceReserved.setStatus("current")
_Hh3cAclResourceConfigured_Type = Unsigned32
_Hh3cAclResourceConfigured_Object = MibTableColumn
hh3cAclResourceConfigured = _Hh3cAclResourceConfigured_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5, 1, 1, 8),
    _Hh3cAclResourceConfigured_Type()
)
hh3cAclResourceConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclResourceConfigured.setStatus("current")
_Hh3cAclResourceUsagePercent_Type = Unsigned32
_Hh3cAclResourceUsagePercent_Object = MibTableColumn
hh3cAclResourceUsagePercent = _Hh3cAclResourceUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5, 1, 1, 9),
    _Hh3cAclResourceUsagePercent_Type()
)
hh3cAclResourceUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclResourceUsagePercent.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-ACL-MIB",
    **{"RuleAction": RuleAction,
       "CounterClear": CounterClear,
       "PortOp": PortOp,
       "DSCPValue": DSCPValue,
       "TCPFlag": TCPFlag,
       "FragmentFlag": FragmentFlag,
       "AddressFlag": AddressFlag,
       "hh3cAcl": hh3cAcl,
       "hh3cAclMibObjects": hh3cAclMibObjects,
       "hh3cAclMode": hh3cAclMode,
       "hh3cAclNumGroupTable": hh3cAclNumGroupTable,
       "hh3cAclNumGroupEntry": hh3cAclNumGroupEntry,
       "hh3cAclNumGroupAclNum": hh3cAclNumGroupAclNum,
       "hh3cAclNumGroupMatchOrder": hh3cAclNumGroupMatchOrder,
       "hh3cAclNumGroupSubitemNum": hh3cAclNumGroupSubitemNum,
       "hh3cAclNumGroupDescription": hh3cAclNumGroupDescription,
       "hh3cAclNumGroupCountClear": hh3cAclNumGroupCountClear,
       "hh3cAclNumGroupRowStatus": hh3cAclNumGroupRowStatus,
       "hh3cAclNameGroupTable": hh3cAclNameGroupTable,
       "hh3cAclNameGroupEntry": hh3cAclNameGroupEntry,
       "hh3cAclNameGroupIndex": hh3cAclNameGroupIndex,
       "hh3cAclNameGroupCreateName": hh3cAclNameGroupCreateName,
       "hh3cAclNameGroupTypes": hh3cAclNameGroupTypes,
       "hh3cAclNameGroupMatchOrder": hh3cAclNameGroupMatchOrder,
       "hh3cAclNameGroupSubitemNum": hh3cAclNameGroupSubitemNum,
       "hh3cAclNameGroupRowStatus": hh3cAclNameGroupRowStatus,
       "hh3cAclBasicRuleTable": hh3cAclBasicRuleTable,
       "hh3cAclBasicRuleEntry": hh3cAclBasicRuleEntry,
       "hh3cAclBasicAclNum": hh3cAclBasicAclNum,
       "hh3cAclBasicSubitem": hh3cAclBasicSubitem,
       "hh3cAclBasicAct": hh3cAclBasicAct,
       "hh3cAclBasicSrcIp": hh3cAclBasicSrcIp,
       "hh3cAclBasicSrcWild": hh3cAclBasicSrcWild,
       "hh3cAclBasicTimeRangeName": hh3cAclBasicTimeRangeName,
       "hh3cAclBasicFragments": hh3cAclBasicFragments,
       "hh3cAclBasicLog": hh3cAclBasicLog,
       "hh3cAclBasicEnable": hh3cAclBasicEnable,
       "hh3cAclBasicCount": hh3cAclBasicCount,
       "hh3cAclBasicCountClear": hh3cAclBasicCountClear,
       "hh3cAclBasicRowStatus": hh3cAclBasicRowStatus,
       "hh3cAclAdvancedRuleTable": hh3cAclAdvancedRuleTable,
       "hh3cAclAdvancedRuleEntry": hh3cAclAdvancedRuleEntry,
       "hh3cAclAdvancedAclNum": hh3cAclAdvancedAclNum,
       "hh3cAclAdvancedSubitem": hh3cAclAdvancedSubitem,
       "hh3cAclAdvancedAct": hh3cAclAdvancedAct,
       "hh3cAclAdvancedProtocol": hh3cAclAdvancedProtocol,
       "hh3cAclAdvancedSrcIp": hh3cAclAdvancedSrcIp,
       "hh3cAclAdvancedSrcWild": hh3cAclAdvancedSrcWild,
       "hh3cAclAdvancedSrcOp": hh3cAclAdvancedSrcOp,
       "hh3cAclAdvancedSrcPort1": hh3cAclAdvancedSrcPort1,
       "hh3cAclAdvancedSrcPort2": hh3cAclAdvancedSrcPort2,
       "hh3cAclAdvancedDestIp": hh3cAclAdvancedDestIp,
       "hh3cAclAdvancedDestWild": hh3cAclAdvancedDestWild,
       "hh3cAclAdvancedDestOp": hh3cAclAdvancedDestOp,
       "hh3cAclAdvancedDestPort1": hh3cAclAdvancedDestPort1,
       "hh3cAclAdvancedDestPort2": hh3cAclAdvancedDestPort2,
       "hh3cAclAdvancedPrecedence": hh3cAclAdvancedPrecedence,
       "hh3cAclAdvancedTos": hh3cAclAdvancedTos,
       "hh3cAclAdvancedDscp": hh3cAclAdvancedDscp,
       "hh3cAclAdvancedEstablish": hh3cAclAdvancedEstablish,
       "hh3cAclAdvancedTimeRangeName": hh3cAclAdvancedTimeRangeName,
       "hh3cAclAdvancedIcmpType": hh3cAclAdvancedIcmpType,
       "hh3cAclAdvancedIcmpCode": hh3cAclAdvancedIcmpCode,
       "hh3cAclAdvancedFragments": hh3cAclAdvancedFragments,
       "hh3cAclAdvancedLog": hh3cAclAdvancedLog,
       "hh3cAclAdvancedEnable": hh3cAclAdvancedEnable,
       "hh3cAclAdvancedCount": hh3cAclAdvancedCount,
       "hh3cAclAdvancedCountClear": hh3cAclAdvancedCountClear,
       "hh3cAclAdvancedRowStatus": hh3cAclAdvancedRowStatus,
       "hh3cAclIfRuleTable": hh3cAclIfRuleTable,
       "hh3cAclIfRuleEntry": hh3cAclIfRuleEntry,
       "hh3cAclIfAclNum": hh3cAclIfAclNum,
       "hh3cAclIfSubitem": hh3cAclIfSubitem,
       "hh3cAclIfAct": hh3cAclIfAct,
       "hh3cAclIfIndex": hh3cAclIfIndex,
       "hh3cAclIfAny": hh3cAclIfAny,
       "hh3cAclIfTimeRangeName": hh3cAclIfTimeRangeName,
       "hh3cAclIfLog": hh3cAclIfLog,
       "hh3cAclIfEnable": hh3cAclIfEnable,
       "hh3cAclIfCount": hh3cAclIfCount,
       "hh3cAclIfCountClear": hh3cAclIfCountClear,
       "hh3cAclIfRowStatus": hh3cAclIfRowStatus,
       "hh3cAclLinkTable": hh3cAclLinkTable,
       "hh3cAclLinkEntry": hh3cAclLinkEntry,
       "hh3cAclLinkAclNum": hh3cAclLinkAclNum,
       "hh3cAclLinkSubitem": hh3cAclLinkSubitem,
       "hh3cAclLinkAct": hh3cAclLinkAct,
       "hh3cAclLinkProtocol": hh3cAclLinkProtocol,
       "hh3cAclLinkFormatType": hh3cAclLinkFormatType,
       "hh3cAclLinkVlanTag": hh3cAclLinkVlanTag,
       "hh3cAclLinkVlanPri": hh3cAclLinkVlanPri,
       "hh3cAclLinkSrcVlanId": hh3cAclLinkSrcVlanId,
       "hh3cAclLinkSrcMac": hh3cAclLinkSrcMac,
       "hh3cAclLinkSrcMacWild": hh3cAclLinkSrcMacWild,
       "hh3cAclLinkSrcIfIndex": hh3cAclLinkSrcIfIndex,
       "hh3cAclLinkSrcAny": hh3cAclLinkSrcAny,
       "hh3cAclLinkDestVlanId": hh3cAclLinkDestVlanId,
       "hh3cAclLinkDestMac": hh3cAclLinkDestMac,
       "hh3cAclLinkDestMacWild": hh3cAclLinkDestMacWild,
       "hh3cAclLinkDestIfIndex": hh3cAclLinkDestIfIndex,
       "hh3cAclLinkDestAny": hh3cAclLinkDestAny,
       "hh3cAclLinkTimeRangeName": hh3cAclLinkTimeRangeName,
       "hh3cAclLinkEnable": hh3cAclLinkEnable,
       "hh3cAclLinkRowStatus": hh3cAclLinkRowStatus,
       "hh3cAclLinkTypeCode": hh3cAclLinkTypeCode,
       "hh3cAclLinkTypeMask": hh3cAclLinkTypeMask,
       "hh3cAclLinkLsapCode": hh3cAclLinkLsapCode,
       "hh3cAclLinkLsapMask": hh3cAclLinkLsapMask,
       "hh3cAclLinkL2LabelRangeOp": hh3cAclLinkL2LabelRangeOp,
       "hh3cAclLinkL2LabelRangeBegin": hh3cAclLinkL2LabelRangeBegin,
       "hh3cAclLinkL2LabelRangeEnd": hh3cAclLinkL2LabelRangeEnd,
       "hh3cAclLinkMplsExp": hh3cAclLinkMplsExp,
       "hh3cAclUserTable": hh3cAclUserTable,
       "hh3cAclUserEntry": hh3cAclUserEntry,
       "hh3cAclUserAclNum": hh3cAclUserAclNum,
       "hh3cAclUserSubitem": hh3cAclUserSubitem,
       "hh3cAclUserAct": hh3cAclUserAct,
       "hh3cAclUserFormatType": hh3cAclUserFormatType,
       "hh3cAclUserVlanTag": hh3cAclUserVlanTag,
       "hh3cAclUserRuleStr": hh3cAclUserRuleStr,
       "hh3cAclUserRuleMask": hh3cAclUserRuleMask,
       "hh3cAclUserTimeRangeName": hh3cAclUserTimeRangeName,
       "hh3cAclUserEnable": hh3cAclUserEnable,
       "hh3cAclUserRowStatus": hh3cAclUserRowStatus,
       "hh3cAclActiveTable": hh3cAclActiveTable,
       "hh3cAclActiveEntry": hh3cAclActiveEntry,
       "hh3cAclActiveAclIndex": hh3cAclActiveAclIndex,
       "hh3cAclActiveIfIndex": hh3cAclActiveIfIndex,
       "hh3cAclActiveVlanID": hh3cAclActiveVlanID,
       "hh3cAclActiveDirection": hh3cAclActiveDirection,
       "hh3cAclActiveUserAclNum": hh3cAclActiveUserAclNum,
       "hh3cAclActiveUserAclSubitem": hh3cAclActiveUserAclSubitem,
       "hh3cAclActiveIpAclNum": hh3cAclActiveIpAclNum,
       "hh3cAclActiveIpAclSubitem": hh3cAclActiveIpAclSubitem,
       "hh3cAclActiveLinkAclNum": hh3cAclActiveLinkAclNum,
       "hh3cAclActiveLinkAclSubitem": hh3cAclActiveLinkAclSubitem,
       "hh3cAclActiveRuntime": hh3cAclActiveRuntime,
       "hh3cAclActiveRowStatus": hh3cAclActiveRowStatus,
       "hh3cAclIDSTable": hh3cAclIDSTable,
       "hh3cAclIDSEntry": hh3cAclIDSEntry,
       "hh3cAclIDSName": hh3cAclIDSName,
       "hh3cAclIDSSrcMac": hh3cAclIDSSrcMac,
       "hh3cAclIDSDestMac": hh3cAclIDSDestMac,
       "hh3cAclIDSSrcIp": hh3cAclIDSSrcIp,
       "hh3cAclIDSSrcWild": hh3cAclIDSSrcWild,
       "hh3cAclIDSDestIp": hh3cAclIDSDestIp,
       "hh3cAclIDSDestWild": hh3cAclIDSDestWild,
       "hh3cAclIDSSrcPort": hh3cAclIDSSrcPort,
       "hh3cAclIDSDestPort": hh3cAclIDSDestPort,
       "hh3cAclIDSProtocol": hh3cAclIDSProtocol,
       "hh3cAclIDSDenyTime": hh3cAclIDSDenyTime,
       "hh3cAclIDSAct": hh3cAclIDSAct,
       "hh3cAclIDSRowStatus": hh3cAclIDSRowStatus,
       "hh3cAclMib2Objects": hh3cAclMib2Objects,
       "hh3cAclMib2GlobalGroup": hh3cAclMib2GlobalGroup,
       "hh3cAclMib2NodesGroup": hh3cAclMib2NodesGroup,
       "hh3cAclMib2Mode": hh3cAclMib2Mode,
       "hh3cAclMib2Version": hh3cAclMib2Version,
       "hh3cAclMib2ObjectsCapabilities": hh3cAclMib2ObjectsCapabilities,
       "hh3cAclMib2CapabilityTable": hh3cAclMib2CapabilityTable,
       "hh3cAclMib2CapabilityEntry": hh3cAclMib2CapabilityEntry,
       "hh3cAclMib2EntityType": hh3cAclMib2EntityType,
       "hh3cAclMib2EntityIndex": hh3cAclMib2EntityIndex,
       "hh3cAclMib2ModuleIndex": hh3cAclMib2ModuleIndex,
       "hh3cAclMib2CharacteristicsIndex": hh3cAclMib2CharacteristicsIndex,
       "hh3cAclMib2CharacteristicsDesc": hh3cAclMib2CharacteristicsDesc,
       "hh3cAclMib2CharacteristicsValue": hh3cAclMib2CharacteristicsValue,
       "hh3cAclNumberGroupTable": hh3cAclNumberGroupTable,
       "hh3cAclNumberGroupEntry": hh3cAclNumberGroupEntry,
       "hh3cAclNumberGroupType": hh3cAclNumberGroupType,
       "hh3cAclNumberGroupIndex": hh3cAclNumberGroupIndex,
       "hh3cAclNumberGroupRowStatus": hh3cAclNumberGroupRowStatus,
       "hh3cAclNumberGroupMatchOrder": hh3cAclNumberGroupMatchOrder,
       "hh3cAclNumberGroupStep": hh3cAclNumberGroupStep,
       "hh3cAclNumberGroupDescription": hh3cAclNumberGroupDescription,
       "hh3cAclNumberGroupCountClear": hh3cAclNumberGroupCountClear,
       "hh3cAclNumberGroupRuleCounter": hh3cAclNumberGroupRuleCounter,
       "hh3cAclIPAclGroup": hh3cAclIPAclGroup,
       "hh3cAclIPAclBasicTable": hh3cAclIPAclBasicTable,
       "hh3cAclIPAclBasicEntry": hh3cAclIPAclBasicEntry,
       "hh3cAclIPAclBasicRuleIndex": hh3cAclIPAclBasicRuleIndex,
       "hh3cAclIPAclBasicRowStatus": hh3cAclIPAclBasicRowStatus,
       "hh3cAclIPAclBasicAct": hh3cAclIPAclBasicAct,
       "hh3cAclIPAclBasicSrcAddrType": hh3cAclIPAclBasicSrcAddrType,
       "hh3cAclIPAclBasicSrcAddr": hh3cAclIPAclBasicSrcAddr,
       "hh3cAclIPAclBasicSrcPrefix": hh3cAclIPAclBasicSrcPrefix,
       "hh3cAclIPAclBasicSrcAny": hh3cAclIPAclBasicSrcAny,
       "hh3cAclIPAclBasicSrcWild": hh3cAclIPAclBasicSrcWild,
       "hh3cAclIPAclBasicTimeRangeName": hh3cAclIPAclBasicTimeRangeName,
       "hh3cAclIPAclBasicFragmentFlag": hh3cAclIPAclBasicFragmentFlag,
       "hh3cAclIPAclBasicLog": hh3cAclIPAclBasicLog,
       "hh3cAclIPAclBasicCount": hh3cAclIPAclBasicCount,
       "hh3cAclIPAclBasicCountClear": hh3cAclIPAclBasicCountClear,
       "hh3cAclIPAclBasicEnable": hh3cAclIPAclBasicEnable,
       "hh3cAclIPAclBasicVpnInstanceName": hh3cAclIPAclBasicVpnInstanceName,
       "hh3cAclIPAclBasicComment": hh3cAclIPAclBasicComment,
       "hh3cAclIPAclAdvancedTable": hh3cAclIPAclAdvancedTable,
       "hh3cAclIPAclAdvancedEntry": hh3cAclIPAclAdvancedEntry,
       "hh3cAclIPAclAdvancedRuleIndex": hh3cAclIPAclAdvancedRuleIndex,
       "hh3cAclIPAclAdvancedRowStatus": hh3cAclIPAclAdvancedRowStatus,
       "hh3cAclIPAclAdvancedAct": hh3cAclIPAclAdvancedAct,
       "hh3cAclIPAclAdvancedProtocol": hh3cAclIPAclAdvancedProtocol,
       "hh3cAclIPAclAdvancedAddrFlag": hh3cAclIPAclAdvancedAddrFlag,
       "hh3cAclIPAclAdvancedSrcAddrType": hh3cAclIPAclAdvancedSrcAddrType,
       "hh3cAclIPAclAdvancedSrcAddr": hh3cAclIPAclAdvancedSrcAddr,
       "hh3cAclIPAclAdvancedSrcPrefix": hh3cAclIPAclAdvancedSrcPrefix,
       "hh3cAclIPAclAdvancedSrcAny": hh3cAclIPAclAdvancedSrcAny,
       "hh3cAclIPAclAdvancedSrcWild": hh3cAclIPAclAdvancedSrcWild,
       "hh3cAclIPAclAdvancedSrcOp": hh3cAclIPAclAdvancedSrcOp,
       "hh3cAclIPAclAdvancedSrcPort1": hh3cAclIPAclAdvancedSrcPort1,
       "hh3cAclIPAclAdvancedSrcPort2": hh3cAclIPAclAdvancedSrcPort2,
       "hh3cAclIPAclAdvancedDestAddrType": hh3cAclIPAclAdvancedDestAddrType,
       "hh3cAclIPAclAdvancedDestAddr": hh3cAclIPAclAdvancedDestAddr,
       "hh3cAclIPAclAdvancedDestPrefix": hh3cAclIPAclAdvancedDestPrefix,
       "hh3cAclIPAclAdvancedDestAny": hh3cAclIPAclAdvancedDestAny,
       "hh3cAclIPAclAdvancedDestWild": hh3cAclIPAclAdvancedDestWild,
       "hh3cAclIPAclAdvancedDestOp": hh3cAclIPAclAdvancedDestOp,
       "hh3cAclIPAclAdvancedDestPort1": hh3cAclIPAclAdvancedDestPort1,
       "hh3cAclIPAclAdvancedDestPort2": hh3cAclIPAclAdvancedDestPort2,
       "hh3cAclIPAclAdvancedIcmpType": hh3cAclIPAclAdvancedIcmpType,
       "hh3cAclIPAclAdvancedIcmpCode": hh3cAclIPAclAdvancedIcmpCode,
       "hh3cAclIPAclAdvancedPrecedence": hh3cAclIPAclAdvancedPrecedence,
       "hh3cAclIPAclAdvancedTos": hh3cAclIPAclAdvancedTos,
       "hh3cAclIPAclAdvancedDscp": hh3cAclIPAclAdvancedDscp,
       "hh3cAclIPAclAdvancedTimeRangeName": hh3cAclIPAclAdvancedTimeRangeName,
       "hh3cAclIPAclAdvancedTCPFlag": hh3cAclIPAclAdvancedTCPFlag,
       "hh3cAclIPAclAdvancedFragmentFlag": hh3cAclIPAclAdvancedFragmentFlag,
       "hh3cAclIPAclAdvancedLog": hh3cAclIPAclAdvancedLog,
       "hh3cAclIPAclAdvancedCount": hh3cAclIPAclAdvancedCount,
       "hh3cAclIPAclAdvancedCountClear": hh3cAclIPAclAdvancedCountClear,
       "hh3cAclIPAclAdvancedEnable": hh3cAclIPAclAdvancedEnable,
       "hh3cAclIPAclAdvancedVpnInstanceName": hh3cAclIPAclAdvancedVpnInstanceName,
       "hh3cAclIPAclAdvancedComment": hh3cAclIPAclAdvancedComment,
       "hh3cAclIPAclAdvancedReflective": hh3cAclIPAclAdvancedReflective,
       "hh3cAclMACAclGroup": hh3cAclMACAclGroup,
       "hh3cAclMACTable": hh3cAclMACTable,
       "hh3cAclMACEntry": hh3cAclMACEntry,
       "hh3cAclMACRuleIndex": hh3cAclMACRuleIndex,
       "hh3cAclMACRowStatus": hh3cAclMACRowStatus,
       "hh3cAclMACAct": hh3cAclMACAct,
       "hh3cAclMACTypeCode": hh3cAclMACTypeCode,
       "hh3cAclMACTypeMask": hh3cAclMACTypeMask,
       "hh3cAclMACSrcMac": hh3cAclMACSrcMac,
       "hh3cAclMACSrcMacWild": hh3cAclMACSrcMacWild,
       "hh3cAclMACDestMac": hh3cAclMACDestMac,
       "hh3cAclMACDestMacWild": hh3cAclMACDestMacWild,
       "hh3cAclMACLsapCode": hh3cAclMACLsapCode,
       "hh3cAclMACLsapMask": hh3cAclMACLsapMask,
       "hh3cAclMACCos": hh3cAclMACCos,
       "hh3cAclMACTimeRangeName": hh3cAclMACTimeRangeName,
       "hh3cAclMACCount": hh3cAclMACCount,
       "hh3cAclMACCountClear": hh3cAclMACCountClear,
       "hh3cAclMACEnable": hh3cAclMACEnable,
       "hh3cAclMACComment": hh3cAclMACComment,
       "hh3cAclEnUserAclGroup": hh3cAclEnUserAclGroup,
       "hh3cAclEnUserTable": hh3cAclEnUserTable,
       "hh3cAclEnUserEntry": hh3cAclEnUserEntry,
       "hh3cAclEnUserRuleIndex": hh3cAclEnUserRuleIndex,
       "hh3cAclEnUserRowStatus": hh3cAclEnUserRowStatus,
       "hh3cAclEnUserAct": hh3cAclEnUserAct,
       "hh3cAclEnUserStartString": hh3cAclEnUserStartString,
       "hh3cAclEnUserL2String": hh3cAclEnUserL2String,
       "hh3cAclEnUserMplsString": hh3cAclEnUserMplsString,
       "hh3cAclEnUserIPv4String": hh3cAclEnUserIPv4String,
       "hh3cAclEnUserIPv6String": hh3cAclEnUserIPv6String,
       "hh3cAclEnUserL4String": hh3cAclEnUserL4String,
       "hh3cAclEnUserL5String": hh3cAclEnUserL5String,
       "hh3cAclEnUserTimeRangeName": hh3cAclEnUserTimeRangeName,
       "hh3cAclEnUserCount": hh3cAclEnUserCount,
       "hh3cAclEnUserCountClear": hh3cAclEnUserCountClear,
       "hh3cAclEnUserEnable": hh3cAclEnUserEnable,
       "hh3cAclEnUserComment": hh3cAclEnUserComment,
       "hh3cAclResourceGroup": hh3cAclResourceGroup,
       "hh3cAclResourceUsageTable": hh3cAclResourceUsageTable,
       "hh3cAclResourceUsageEntry": hh3cAclResourceUsageEntry,
       "hh3cAclResourceChassis": hh3cAclResourceChassis,
       "hh3cAclResourceSlot": hh3cAclResourceSlot,
       "hh3cAclResourceChip": hh3cAclResourceChip,
       "hh3cAclResourceType": hh3cAclResourceType,
       "hh3cAclPortRange": hh3cAclPortRange,
       "hh3cAclResourceTotal": hh3cAclResourceTotal,
       "hh3cAclResourceReserved": hh3cAclResourceReserved,
       "hh3cAclResourceConfigured": hh3cAclResourceConfigured,
       "hh3cAclResourceUsagePercent": hh3cAclResourceUsagePercent}
)
