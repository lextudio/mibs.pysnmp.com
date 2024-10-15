# SNMP MIB module (NOKIA-RATESHAPE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOKIA-RATESHAPE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:44 2024
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

ntcRS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4)
)
ntcRS.setRevisions(
        ("1900-01-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PacketSource(Integer32, TextualConvention):
    status = "current"
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



class RateLimitAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("condition", 4),
          ("drop", 1),
          ("prioritize", 6),
          ("reject", 3),
          ("skip", 5))
    )



# MIB Managed Objects in the order of their OIDs

_Nokia_ObjectIdentity = ObjectIdentity
nokia = _Nokia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94)
)
_NokiaProducts_ObjectIdentity = ObjectIdentity
nokiaProducts = _NokiaProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1)
)
_NtcCommon_ObjectIdentity = ObjectIdentity
ntcCommon = _NtcCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16)
)
_RsAccessListTable_Object = MibTable
rsAccessListTable = _RsAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rsAccessListTable.setStatus("current")
_RsAccessListEntry_Object = MibTableRow
rsAccessListEntry = _RsAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 1, 1, 1)
)
rsAccessListEntry.setIndexNames(
    (0, "NOKIA-RATESHAPE-MIB", "rsAccessListIfIndex"),
    (0, "NOKIA-RATESHAPE-MIB", "rsAccessListIndex"),
    (0, "NOKIA-RATESHAPE-MIB", "rsAccessListDirection"),
)
if mibBuilder.loadTexts:
    rsAccessListEntry.setStatus("current")


class _RsAccessListIfIndex_Type(Integer32):
    """Custom type rsAccessListIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RsAccessListIfIndex_Type.__name__ = "Integer32"
_RsAccessListIfIndex_Object = MibTableColumn
rsAccessListIfIndex = _RsAccessListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 1, 1, 1, 1),
    _RsAccessListIfIndex_Type()
)
rsAccessListIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAccessListIfIndex.setStatus("current")


class _RsAccessListIndex_Type(Integer32):
    """Custom type rsAccessListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RsAccessListIndex_Type.__name__ = "Integer32"
_RsAccessListIndex_Object = MibTableColumn
rsAccessListIndex = _RsAccessListIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 1, 1, 1, 2),
    _RsAccessListIndex_Type()
)
rsAccessListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAccessListIndex.setStatus("current")
_RsAccessListDirection_Type = PacketSource
_RsAccessListDirection_Object = MibTableColumn
rsAccessListDirection = _RsAccessListDirection_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 1, 1, 1, 3),
    _RsAccessListDirection_Type()
)
rsAccessListDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAccessListDirection.setStatus("current")
_RsAccessListName_Type = DisplayString
_RsAccessListName_Object = MibTableColumn
rsAccessListName = _RsAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 1, 1, 1, 4),
    _RsAccessListName_Type()
)
rsAccessListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAccessListName.setStatus("current")
_RsAccessListRowStatus_Type = RowStatus
_RsAccessListRowStatus_Object = MibTableColumn
rsAccessListRowStatus = _RsAccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 1, 1, 1, 5),
    _RsAccessListRowStatus_Type()
)
rsAccessListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAccessListRowStatus.setStatus("current")
_RsRuleTable_Object = MibTable
rsRuleTable = _RsRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1)
)
if mibBuilder.loadTexts:
    rsRuleTable.setStatus("current")
_RsRuleEntry_Object = MibTableRow
rsRuleEntry = _RsRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1)
)
rsRuleEntry.setIndexNames(
    (0, "NOKIA-RATESHAPE-MIB", "rsRuleIfIndex"),
    (0, "NOKIA-RATESHAPE-MIB", "rsRuleIndex"),
    (0, "NOKIA-RATESHAPE-MIB", "rsRuleDirection"),
)
if mibBuilder.loadTexts:
    rsRuleEntry.setStatus("current")


class _RsRuleIfIndex_Type(Integer32):
    """Custom type rsRuleIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RsRuleIfIndex_Type.__name__ = "Integer32"
_RsRuleIfIndex_Object = MibTableColumn
rsRuleIfIndex = _RsRuleIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 1),
    _RsRuleIfIndex_Type()
)
rsRuleIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRuleIfIndex.setStatus("current")


class _RsRuleIndex_Type(Integer32):
    """Custom type rsRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RsRuleIndex_Type.__name__ = "Integer32"
_RsRuleIndex_Object = MibTableColumn
rsRuleIndex = _RsRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 2),
    _RsRuleIndex_Type()
)
rsRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRuleIndex.setStatus("current")
_RsRuleDirection_Type = PacketSource
_RsRuleDirection_Object = MibTableColumn
rsRuleDirection = _RsRuleDirection_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 3),
    _RsRuleDirection_Type()
)
rsRuleDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRuleDirection.setStatus("current")


class _RsRuleTOS_Type(Integer32):
    """Custom type rsRuleTOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RsRuleTOS_Type.__name__ = "Integer32"
_RsRuleTOS_Object = MibTableColumn
rsRuleTOS = _RsRuleTOS_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 4),
    _RsRuleTOS_Type()
)
rsRuleTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRuleTOS.setStatus("current")
_RsRuleAction_Type = RateLimitAction
_RsRuleAction_Object = MibTableColumn
rsRuleAction = _RsRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 5),
    _RsRuleAction_Type()
)
rsRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRuleAction.setStatus("current")
_RsRuleSrcAddress_Type = IpAddress
_RsRuleSrcAddress_Object = MibTableColumn
rsRuleSrcAddress = _RsRuleSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 6),
    _RsRuleSrcAddress_Type()
)
rsRuleSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRuleSrcAddress.setStatus("current")
_RsRuleSrcAddrMask_Type = IpAddress
_RsRuleSrcAddrMask_Object = MibTableColumn
rsRuleSrcAddrMask = _RsRuleSrcAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 7),
    _RsRuleSrcAddrMask_Type()
)
rsRuleSrcAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRuleSrcAddrMask.setStatus("current")
_RsRuleDestAddress_Type = IpAddress
_RsRuleDestAddress_Object = MibTableColumn
rsRuleDestAddress = _RsRuleDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 8),
    _RsRuleDestAddress_Type()
)
rsRuleDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRuleDestAddress.setStatus("current")
_RsRuleDestAddrMask_Type = IpAddress
_RsRuleDestAddrMask_Object = MibTableColumn
rsRuleDestAddrMask = _RsRuleDestAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 9),
    _RsRuleDestAddrMask_Type()
)
rsRuleDestAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRuleDestAddrMask.setStatus("current")
_RsRuleIpProtocol_Type = Integer32
_RsRuleIpProtocol_Object = MibTableColumn
rsRuleIpProtocol = _RsRuleIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 10),
    _RsRuleIpProtocol_Type()
)
rsRuleIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRuleIpProtocol.setStatus("current")
_RsRuleSrcStartingPort_Type = Integer32
_RsRuleSrcStartingPort_Object = MibTableColumn
rsRuleSrcStartingPort = _RsRuleSrcStartingPort_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 11),
    _RsRuleSrcStartingPort_Type()
)
rsRuleSrcStartingPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRuleSrcStartingPort.setStatus("current")
_RsRuleSrcEndingPort_Type = Integer32
_RsRuleSrcEndingPort_Object = MibTableColumn
rsRuleSrcEndingPort = _RsRuleSrcEndingPort_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 12),
    _RsRuleSrcEndingPort_Type()
)
rsRuleSrcEndingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRuleSrcEndingPort.setStatus("current")
_RsRuleDestStartingPort_Type = Integer32
_RsRuleDestStartingPort_Object = MibTableColumn
rsRuleDestStartingPort = _RsRuleDestStartingPort_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 13),
    _RsRuleDestStartingPort_Type()
)
rsRuleDestStartingPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRuleDestStartingPort.setStatus("current")
_RsRuleDestEndingPort_Type = Integer32
_RsRuleDestEndingPort_Object = MibTableColumn
rsRuleDestEndingPort = _RsRuleDestEndingPort_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 14),
    _RsRuleDestEndingPort_Type()
)
rsRuleDestEndingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRuleDestEndingPort.setStatus("current")
_RsRuleAggregationClassIndex_Type = Integer32
_RsRuleAggregationClassIndex_Object = MibTableColumn
rsRuleAggregationClassIndex = _RsRuleAggregationClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 15),
    _RsRuleAggregationClassIndex_Type()
)
rsRuleAggregationClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRuleAggregationClassIndex.setStatus("current")


class _RsRuleEstablished_Type(Integer32):
    """Custom type rsRuleEstablished based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("established", 1),
          ("notEstablished", 2))
    )


_RsRuleEstablished_Type.__name__ = "Integer32"
_RsRuleEstablished_Object = MibTableColumn
rsRuleEstablished = _RsRuleEstablished_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 16),
    _RsRuleEstablished_Type()
)
rsRuleEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRuleEstablished.setStatus("current")
_RsRuleRowStatus_Type = RowStatus
_RsRuleRowStatus_Object = MibTableColumn
rsRuleRowStatus = _RsRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 17),
    _RsRuleRowStatus_Type()
)
rsRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRuleRowStatus.setStatus("current")
_RsAggregationClassTable_Object = MibTable
rsAggregationClassTable = _RsAggregationClassTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1)
)
if mibBuilder.loadTexts:
    rsAggregationClassTable.setStatus("current")
_RsAggregationClassEntry_Object = MibTableRow
rsAggregationClassEntry = _RsAggregationClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1, 1)
)
rsAggregationClassEntry.setIndexNames(
    (0, "NOKIA-RATESHAPE-MIB", "rsAggregationClassIfIndex"),
    (0, "NOKIA-RATESHAPE-MIB", "rsAggregationClassIndex"),
    (0, "NOKIA-RATESHAPE-MIB", "rsAggregationClassDirection"),
)
if mibBuilder.loadTexts:
    rsAggregationClassEntry.setStatus("current")


class _RsAggregationClassIfIndex_Type(Integer32):
    """Custom type rsAggregationClassIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RsAggregationClassIfIndex_Type.__name__ = "Integer32"
_RsAggregationClassIfIndex_Object = MibTableColumn
rsAggregationClassIfIndex = _RsAggregationClassIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1, 1, 1),
    _RsAggregationClassIfIndex_Type()
)
rsAggregationClassIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAggregationClassIfIndex.setStatus("current")


class _RsAggregationClassIndex_Type(Integer32):
    """Custom type rsAggregationClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RsAggregationClassIndex_Type.__name__ = "Integer32"
_RsAggregationClassIndex_Object = MibTableColumn
rsAggregationClassIndex = _RsAggregationClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1, 1, 2),
    _RsAggregationClassIndex_Type()
)
rsAggregationClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAggregationClassIndex.setStatus("current")
_RsAggregationClassDirection_Type = PacketSource
_RsAggregationClassDirection_Object = MibTableColumn
rsAggregationClassDirection = _RsAggregationClassDirection_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1, 1, 3),
    _RsAggregationClassDirection_Type()
)
rsAggregationClassDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAggregationClassDirection.setStatus("current")
_RsAggregationClassName_Type = DisplayString
_RsAggregationClassName_Object = MibTableColumn
rsAggregationClassName = _RsAggregationClassName_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1, 1, 4),
    _RsAggregationClassName_Type()
)
rsAggregationClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAggregationClassName.setStatus("current")


class _RsAggregationClassMeanRate_Type(Integer32):
    """Custom type rsAggregationClassMeanRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_RsAggregationClassMeanRate_Type.__name__ = "Integer32"
_RsAggregationClassMeanRate_Object = MibTableColumn
rsAggregationClassMeanRate = _RsAggregationClassMeanRate_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1, 1, 5),
    _RsAggregationClassMeanRate_Type()
)
rsAggregationClassMeanRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAggregationClassMeanRate.setStatus("current")


class _RsAggregationClassBurstSize_Type(Integer32):
    """Custom type rsAggregationClassBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 150000),
    )


_RsAggregationClassBurstSize_Type.__name__ = "Integer32"
_RsAggregationClassBurstSize_Object = MibTableColumn
rsAggregationClassBurstSize = _RsAggregationClassBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1, 1, 7),
    _RsAggregationClassBurstSize_Type()
)
rsAggregationClassBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAggregationClassBurstSize.setStatus("current")
_RsAggregationClassRowStatus_Type = RowStatus
_RsAggregationClassRowStatus_Object = MibTableColumn
rsAggregationClassRowStatus = _RsAggregationClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1, 1, 8),
    _RsAggregationClassRowStatus_Type()
)
rsAggregationClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAggregationClassRowStatus.setStatus("current")
_RsAccessListStatTable_Object = MibTable
rsAccessListStatTable = _RsAccessListStatTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 4, 1)
)
if mibBuilder.loadTexts:
    rsAccessListStatTable.setStatus("current")
_RsAccessListStatEntry_Object = MibTableRow
rsAccessListStatEntry = _RsAccessListStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 4, 1, 1)
)
rsAccessListStatEntry.setIndexNames(
    (0, "NOKIA-RATESHAPE-MIB", "rsAccessListStatIfIndex"),
    (0, "NOKIA-RATESHAPE-MIB", "rsAccessListStatIndex"),
    (0, "NOKIA-RATESHAPE-MIB", "rsAccessListStatDirection"),
)
if mibBuilder.loadTexts:
    rsAccessListStatEntry.setStatus("current")


class _RsAccessListStatIfIndex_Type(Integer32):
    """Custom type rsAccessListStatIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RsAccessListStatIfIndex_Type.__name__ = "Integer32"
_RsAccessListStatIfIndex_Object = MibTableColumn
rsAccessListStatIfIndex = _RsAccessListStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 4, 1, 1, 1),
    _RsAccessListStatIfIndex_Type()
)
rsAccessListStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAccessListStatIfIndex.setStatus("current")


class _RsAccessListStatIndex_Type(Integer32):
    """Custom type rsAccessListStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RsAccessListStatIndex_Type.__name__ = "Integer32"
_RsAccessListStatIndex_Object = MibTableColumn
rsAccessListStatIndex = _RsAccessListStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 4, 1, 1, 2),
    _RsAccessListStatIndex_Type()
)
rsAccessListStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAccessListStatIndex.setStatus("current")
_RsAccessListStatDirection_Type = PacketSource
_RsAccessListStatDirection_Object = MibTableColumn
rsAccessListStatDirection = _RsAccessListStatDirection_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 4, 1, 1, 3),
    _RsAccessListStatDirection_Type()
)
rsAccessListStatDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAccessListStatDirection.setStatus("current")
_RsAccessListStatPktsPassed_Type = Counter32
_RsAccessListStatPktsPassed_Object = MibTableColumn
rsAccessListStatPktsPassed = _RsAccessListStatPktsPassed_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 4, 1, 1, 4),
    _RsAccessListStatPktsPassed_Type()
)
rsAccessListStatPktsPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAccessListStatPktsPassed.setStatus("current")
_RsAccessListStatBytesPassed_Type = Counter32
_RsAccessListStatBytesPassed_Object = MibTableColumn
rsAccessListStatBytesPassed = _RsAccessListStatBytesPassed_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 4, 1, 1, 5),
    _RsAccessListStatBytesPassed_Type()
)
rsAccessListStatBytesPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAccessListStatBytesPassed.setStatus("current")
_RsAggregationClassStatTable_Object = MibTable
rsAggregationClassStatTable = _RsAggregationClassStatTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1)
)
if mibBuilder.loadTexts:
    rsAggregationClassStatTable.setStatus("current")
_RsAggregationClassStatEntry_Object = MibTableRow
rsAggregationClassStatEntry = _RsAggregationClassStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1)
)
rsAggregationClassStatEntry.setIndexNames(
    (0, "NOKIA-RATESHAPE-MIB", "rsAggregationClassStatIfIndex"),
    (0, "NOKIA-RATESHAPE-MIB", "rsAggregationClassStatIndex"),
    (0, "NOKIA-RATESHAPE-MIB", "rsAggregationClassStatDirection"),
)
if mibBuilder.loadTexts:
    rsAggregationClassStatEntry.setStatus("current")


class _RsAggregationClassStatIfIndex_Type(Integer32):
    """Custom type rsAggregationClassStatIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RsAggregationClassStatIfIndex_Type.__name__ = "Integer32"
_RsAggregationClassStatIfIndex_Object = MibTableColumn
rsAggregationClassStatIfIndex = _RsAggregationClassStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 1),
    _RsAggregationClassStatIfIndex_Type()
)
rsAggregationClassStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAggregationClassStatIfIndex.setStatus("current")


class _RsAggregationClassStatIndex_Type(Integer32):
    """Custom type rsAggregationClassStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RsAggregationClassStatIndex_Type.__name__ = "Integer32"
_RsAggregationClassStatIndex_Object = MibTableColumn
rsAggregationClassStatIndex = _RsAggregationClassStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 2),
    _RsAggregationClassStatIndex_Type()
)
rsAggregationClassStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAggregationClassStatIndex.setStatus("current")
_RsAggregationClassStatDirection_Type = PacketSource
_RsAggregationClassStatDirection_Object = MibTableColumn
rsAggregationClassStatDirection = _RsAggregationClassStatDirection_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 3),
    _RsAggregationClassStatDirection_Type()
)
rsAggregationClassStatDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAggregationClassStatDirection.setStatus("current")
_RsAggregationClassStatShapedPkts_Type = Counter32
_RsAggregationClassStatShapedPkts_Object = MibTableColumn
rsAggregationClassStatShapedPkts = _RsAggregationClassStatShapedPkts_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 4),
    _RsAggregationClassStatShapedPkts_Type()
)
rsAggregationClassStatShapedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAggregationClassStatShapedPkts.setStatus("current")
_RsAggregationClassStatShapedOctets_Type = Counter32
_RsAggregationClassStatShapedOctets_Object = MibTableColumn
rsAggregationClassStatShapedOctets = _RsAggregationClassStatShapedOctets_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 5),
    _RsAggregationClassStatShapedOctets_Type()
)
rsAggregationClassStatShapedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAggregationClassStatShapedOctets.setStatus("current")
_RsAggregationClassStatEnqueuedPkts_Type = Counter32
_RsAggregationClassStatEnqueuedPkts_Object = MibTableColumn
rsAggregationClassStatEnqueuedPkts = _RsAggregationClassStatEnqueuedPkts_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 6),
    _RsAggregationClassStatEnqueuedPkts_Type()
)
rsAggregationClassStatEnqueuedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAggregationClassStatEnqueuedPkts.setStatus("current")
_RsAggregationClassStatEnqueuedOctets_Type = Counter32
_RsAggregationClassStatEnqueuedOctets_Object = MibTableColumn
rsAggregationClassStatEnqueuedOctets = _RsAggregationClassStatEnqueuedOctets_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 7),
    _RsAggregationClassStatEnqueuedOctets_Type()
)
rsAggregationClassStatEnqueuedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAggregationClassStatEnqueuedOctets.setStatus("current")
_RsAggregationClassStatDroppedPkts_Type = Counter32
_RsAggregationClassStatDroppedPkts_Object = MibTableColumn
rsAggregationClassStatDroppedPkts = _RsAggregationClassStatDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 8),
    _RsAggregationClassStatDroppedPkts_Type()
)
rsAggregationClassStatDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAggregationClassStatDroppedPkts.setStatus("current")
_RsAggregationClassStatDroppedOctets_Type = Counter32
_RsAggregationClassStatDroppedOctets_Object = MibTableColumn
rsAggregationClassStatDroppedOctets = _RsAggregationClassStatDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 9),
    _RsAggregationClassStatDroppedOctets_Type()
)
rsAggregationClassStatDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAggregationClassStatDroppedOctets.setStatus("current")
_RsAggregationClassStatInputPktsPassed_Type = Counter32
_RsAggregationClassStatInputPktsPassed_Object = MibTableColumn
rsAggregationClassStatInputPktsPassed = _RsAggregationClassStatInputPktsPassed_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 10),
    _RsAggregationClassStatInputPktsPassed_Type()
)
rsAggregationClassStatInputPktsPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAggregationClassStatInputPktsPassed.setStatus("current")
_RsAggregationClassStatOutputPktsPassed_Type = Counter32
_RsAggregationClassStatOutputPktsPassed_Object = MibTableColumn
rsAggregationClassStatOutputPktsPassed = _RsAggregationClassStatOutputPktsPassed_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 11),
    _RsAggregationClassStatOutputPktsPassed_Type()
)
rsAggregationClassStatOutputPktsPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAggregationClassStatOutputPktsPassed.setStatus("current")
_RsAggregationClassStatInputBytesPassed_Type = Counter32
_RsAggregationClassStatInputBytesPassed_Object = MibTableColumn
rsAggregationClassStatInputBytesPassed = _RsAggregationClassStatInputBytesPassed_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 12),
    _RsAggregationClassStatInputBytesPassed_Type()
)
rsAggregationClassStatInputBytesPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAggregationClassStatInputBytesPassed.setStatus("current")
_RsAggregationClassStatOutputBytesPassed_Type = Counter32
_RsAggregationClassStatOutputBytesPassed_Object = MibTableColumn
rsAggregationClassStatOutputBytesPassed = _RsAggregationClassStatOutputBytesPassed_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 13),
    _RsAggregationClassStatOutputBytesPassed_Type()
)
rsAggregationClassStatOutputBytesPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAggregationClassStatOutputBytesPassed.setStatus("current")
_RsRuleStatTable_Object = MibTable
rsRuleStatTable = _RsRuleStatTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1)
)
if mibBuilder.loadTexts:
    rsRuleStatTable.setStatus("current")
_RsRuleStatEntry_Object = MibTableRow
rsRuleStatEntry = _RsRuleStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1, 1)
)
rsRuleStatEntry.setIndexNames(
    (0, "NOKIA-RATESHAPE-MIB", "rsRuleStatIfIndex"),
    (0, "NOKIA-RATESHAPE-MIB", "rsRuleStatIndex"),
    (0, "NOKIA-RATESHAPE-MIB", "rsRuleStatDirection"),
)
if mibBuilder.loadTexts:
    rsRuleStatEntry.setStatus("current")


class _RsRuleStatIfIndex_Type(Integer32):
    """Custom type rsRuleStatIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RsRuleStatIfIndex_Type.__name__ = "Integer32"
_RsRuleStatIfIndex_Object = MibTableColumn
rsRuleStatIfIndex = _RsRuleStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1, 1, 1),
    _RsRuleStatIfIndex_Type()
)
rsRuleStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRuleStatIfIndex.setStatus("current")


class _RsRuleStatIndex_Type(Integer32):
    """Custom type rsRuleStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RsRuleStatIndex_Type.__name__ = "Integer32"
_RsRuleStatIndex_Object = MibTableColumn
rsRuleStatIndex = _RsRuleStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1, 1, 2),
    _RsRuleStatIndex_Type()
)
rsRuleStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRuleStatIndex.setStatus("current")
_RsRuleStatDirection_Type = PacketSource
_RsRuleStatDirection_Object = MibTableColumn
rsRuleStatDirection = _RsRuleStatDirection_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1, 1, 3),
    _RsRuleStatDirection_Type()
)
rsRuleStatDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRuleStatDirection.setStatus("current")
_RsRuleStatDropPkts_Type = Counter32
_RsRuleStatDropPkts_Object = MibTableColumn
rsRuleStatDropPkts = _RsRuleStatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1, 1, 4),
    _RsRuleStatDropPkts_Type()
)
rsRuleStatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRuleStatDropPkts.setStatus("current")
_RsRuleStatDropOctets_Type = Counter32
_RsRuleStatDropOctets_Object = MibTableColumn
rsRuleStatDropOctets = _RsRuleStatDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1, 1, 5),
    _RsRuleStatDropOctets_Type()
)
rsRuleStatDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRuleStatDropOctets.setStatus("current")
_RsRuleStatPktsPassed_Type = Counter32
_RsRuleStatPktsPassed_Object = MibTableColumn
rsRuleStatPktsPassed = _RsRuleStatPktsPassed_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1, 1, 6),
    _RsRuleStatPktsPassed_Type()
)
rsRuleStatPktsPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRuleStatPktsPassed.setStatus("current")
_RsRuleStatBytesPassed_Type = Counter32
_RsRuleStatBytesPassed_Object = MibTableColumn
rsRuleStatBytesPassed = _RsRuleStatBytesPassed_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1, 1, 7),
    _RsRuleStatBytesPassed_Type()
)
rsRuleStatBytesPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRuleStatBytesPassed.setStatus("current")

# Managed Objects groups

rsAccessLists = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 1)
)
rsAccessLists.setObjects(
      *(("NOKIA-RATESHAPE-MIB", "rsAccessListIfIndex"),
        ("NOKIA-RATESHAPE-MIB", "rsAccessListIndex"),
        ("NOKIA-RATESHAPE-MIB", "rsAccessListDirection"),
        ("NOKIA-RATESHAPE-MIB", "rsAccessListName"),
        ("NOKIA-RATESHAPE-MIB", "rsAccessListRowStatus"))
)
if mibBuilder.loadTexts:
    rsAccessLists.setStatus("current")

rsRules = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2)
)
rsRules.setObjects(
      *(("NOKIA-RATESHAPE-MIB", "rsRuleIfIndex"),
        ("NOKIA-RATESHAPE-MIB", "rsRuleIndex"),
        ("NOKIA-RATESHAPE-MIB", "rsRuleDirection"),
        ("NOKIA-RATESHAPE-MIB", "rsRuleTOS"),
        ("NOKIA-RATESHAPE-MIB", "rsRuleAction"),
        ("NOKIA-RATESHAPE-MIB", "rsRuleSrcAddress"),
        ("NOKIA-RATESHAPE-MIB", "rsRuleSrcAddrMask"),
        ("NOKIA-RATESHAPE-MIB", "rsRuleDestAddress"),
        ("NOKIA-RATESHAPE-MIB", "rsRuleDestAddrMask"),
        ("NOKIA-RATESHAPE-MIB", "rsRuleIpProtocol"),
        ("NOKIA-RATESHAPE-MIB", "rsRuleSrcStartingPort"),
        ("NOKIA-RATESHAPE-MIB", "rsRuleSrcEndingPort"),
        ("NOKIA-RATESHAPE-MIB", "rsRuleDestStartingPort"),
        ("NOKIA-RATESHAPE-MIB", "rsRuleDestEndingPort"),
        ("NOKIA-RATESHAPE-MIB", "rsRuleAggregationClassIndex"),
        ("NOKIA-RATESHAPE-MIB", "rsRuleEstablished"),
        ("NOKIA-RATESHAPE-MIB", "rsRuleRowStatus"))
)
if mibBuilder.loadTexts:
    rsRules.setStatus("current")

rsAggregationClasses = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3)
)
rsAggregationClasses.setObjects(
      *(("NOKIA-RATESHAPE-MIB", "rsAggregationClassIfIndex"),
        ("NOKIA-RATESHAPE-MIB", "rsAggregationClassIndex"),
        ("NOKIA-RATESHAPE-MIB", "rsAggregationClassDirection"),
        ("NOKIA-RATESHAPE-MIB", "rsAggregationClassName"),
        ("NOKIA-RATESHAPE-MIB", "rsAggregationClassMeanRate"),
        ("NOKIA-RATESHAPE-MIB", "rsAggregationClassBurstSize"),
        ("NOKIA-RATESHAPE-MIB", "rsAggregationClassRowStatus"))
)
if mibBuilder.loadTexts:
    rsAggregationClasses.setStatus("current")

rsAccessListStats = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 4)
)
rsAccessListStats.setObjects(
      *(("NOKIA-RATESHAPE-MIB", "rsAccessListStatIfIndex"),
        ("NOKIA-RATESHAPE-MIB", "rsAccessListStatIndex"),
        ("NOKIA-RATESHAPE-MIB", "rsAccessListStatDirection"),
        ("NOKIA-RATESHAPE-MIB", "rsAccessListStatPktsPassed"),
        ("NOKIA-RATESHAPE-MIB", "rsAccessListStatBytesPassed"))
)
if mibBuilder.loadTexts:
    rsAccessListStats.setStatus("current")

rsAggregationClassStats = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5)
)
rsAggregationClassStats.setObjects(
      *(("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatIfIndex"),
        ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatIndex"),
        ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatDirection"),
        ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatShapedPkts"),
        ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatShapedOctets"),
        ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatEnqueuedPkts"),
        ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatEnqueuedOctets"),
        ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatDroppedPkts"),
        ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatDroppedOctets"),
        ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatInputPktsPassed"),
        ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatOutputPktsPassed"),
        ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatInputBytesPassed"),
        ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatOutputBytesPassed"))
)
if mibBuilder.loadTexts:
    rsAggregationClassStats.setStatus("current")

rsRuleStats = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6)
)
rsRuleStats.setObjects(
      *(("NOKIA-RATESHAPE-MIB", "rsRuleStatIfIndex"),
        ("NOKIA-RATESHAPE-MIB", "rsRuleStatIndex"),
        ("NOKIA-RATESHAPE-MIB", "rsRuleStatDirection"),
        ("NOKIA-RATESHAPE-MIB", "rsRuleStatDropPkts"),
        ("NOKIA-RATESHAPE-MIB", "rsRuleStatDropOctets"),
        ("NOKIA-RATESHAPE-MIB", "rsRuleStatPktsPassed"),
        ("NOKIA-RATESHAPE-MIB", "rsRuleStatBytesPassed"))
)
if mibBuilder.loadTexts:
    rsRuleStats.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOKIA-RATESHAPE-MIB",
    **{"PacketSource": PacketSource,
       "RateLimitAction": RateLimitAction,
       "nokia": nokia,
       "nokiaProducts": nokiaProducts,
       "ntcCommon": ntcCommon,
       "ntcRS": ntcRS,
       "rsAccessLists": rsAccessLists,
       "rsAccessListTable": rsAccessListTable,
       "rsAccessListEntry": rsAccessListEntry,
       "rsAccessListIfIndex": rsAccessListIfIndex,
       "rsAccessListIndex": rsAccessListIndex,
       "rsAccessListDirection": rsAccessListDirection,
       "rsAccessListName": rsAccessListName,
       "rsAccessListRowStatus": rsAccessListRowStatus,
       "rsRules": rsRules,
       "rsRuleTable": rsRuleTable,
       "rsRuleEntry": rsRuleEntry,
       "rsRuleIfIndex": rsRuleIfIndex,
       "rsRuleIndex": rsRuleIndex,
       "rsRuleDirection": rsRuleDirection,
       "rsRuleTOS": rsRuleTOS,
       "rsRuleAction": rsRuleAction,
       "rsRuleSrcAddress": rsRuleSrcAddress,
       "rsRuleSrcAddrMask": rsRuleSrcAddrMask,
       "rsRuleDestAddress": rsRuleDestAddress,
       "rsRuleDestAddrMask": rsRuleDestAddrMask,
       "rsRuleIpProtocol": rsRuleIpProtocol,
       "rsRuleSrcStartingPort": rsRuleSrcStartingPort,
       "rsRuleSrcEndingPort": rsRuleSrcEndingPort,
       "rsRuleDestStartingPort": rsRuleDestStartingPort,
       "rsRuleDestEndingPort": rsRuleDestEndingPort,
       "rsRuleAggregationClassIndex": rsRuleAggregationClassIndex,
       "rsRuleEstablished": rsRuleEstablished,
       "rsRuleRowStatus": rsRuleRowStatus,
       "rsAggregationClasses": rsAggregationClasses,
       "rsAggregationClassTable": rsAggregationClassTable,
       "rsAggregationClassEntry": rsAggregationClassEntry,
       "rsAggregationClassIfIndex": rsAggregationClassIfIndex,
       "rsAggregationClassIndex": rsAggregationClassIndex,
       "rsAggregationClassDirection": rsAggregationClassDirection,
       "rsAggregationClassName": rsAggregationClassName,
       "rsAggregationClassMeanRate": rsAggregationClassMeanRate,
       "rsAggregationClassBurstSize": rsAggregationClassBurstSize,
       "rsAggregationClassRowStatus": rsAggregationClassRowStatus,
       "rsAccessListStats": rsAccessListStats,
       "rsAccessListStatTable": rsAccessListStatTable,
       "rsAccessListStatEntry": rsAccessListStatEntry,
       "rsAccessListStatIfIndex": rsAccessListStatIfIndex,
       "rsAccessListStatIndex": rsAccessListStatIndex,
       "rsAccessListStatDirection": rsAccessListStatDirection,
       "rsAccessListStatPktsPassed": rsAccessListStatPktsPassed,
       "rsAccessListStatBytesPassed": rsAccessListStatBytesPassed,
       "rsAggregationClassStats": rsAggregationClassStats,
       "rsAggregationClassStatTable": rsAggregationClassStatTable,
       "rsAggregationClassStatEntry": rsAggregationClassStatEntry,
       "rsAggregationClassStatIfIndex": rsAggregationClassStatIfIndex,
       "rsAggregationClassStatIndex": rsAggregationClassStatIndex,
       "rsAggregationClassStatDirection": rsAggregationClassStatDirection,
       "rsAggregationClassStatShapedPkts": rsAggregationClassStatShapedPkts,
       "rsAggregationClassStatShapedOctets": rsAggregationClassStatShapedOctets,
       "rsAggregationClassStatEnqueuedPkts": rsAggregationClassStatEnqueuedPkts,
       "rsAggregationClassStatEnqueuedOctets": rsAggregationClassStatEnqueuedOctets,
       "rsAggregationClassStatDroppedPkts": rsAggregationClassStatDroppedPkts,
       "rsAggregationClassStatDroppedOctets": rsAggregationClassStatDroppedOctets,
       "rsAggregationClassStatInputPktsPassed": rsAggregationClassStatInputPktsPassed,
       "rsAggregationClassStatOutputPktsPassed": rsAggregationClassStatOutputPktsPassed,
       "rsAggregationClassStatInputBytesPassed": rsAggregationClassStatInputBytesPassed,
       "rsAggregationClassStatOutputBytesPassed": rsAggregationClassStatOutputBytesPassed,
       "rsRuleStats": rsRuleStats,
       "rsRuleStatTable": rsRuleStatTable,
       "rsRuleStatEntry": rsRuleStatEntry,
       "rsRuleStatIfIndex": rsRuleStatIfIndex,
       "rsRuleStatIndex": rsRuleStatIndex,
       "rsRuleStatDirection": rsRuleStatDirection,
       "rsRuleStatDropPkts": rsRuleStatDropPkts,
       "rsRuleStatDropOctets": rsRuleStatDropOctets,
       "rsRuleStatPktsPassed": rsRuleStatPktsPassed,
       "rsRuleStatBytesPassed": rsRuleStatBytesPassed}
)
