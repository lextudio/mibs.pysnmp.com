# SNMP MIB module (PDN-MPE-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-MPE-FILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:57 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(mpe_filter,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "mpe-filter")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MpeSysDevFilterMIBObjects_ObjectIdentity = ObjectIdentity
mpeSysDevFilterMIBObjects = _MpeSysDevFilterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1)
)
_MpeSysDevIpFilter_ObjectIdentity = ObjectIdentity
mpeSysDevIpFilter = _MpeSysDevIpFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1)
)
_MpeSysDevIpFilterConfigTable_Object = MibTable
mpeSysDevIpFilterConfigTable = _MpeSysDevIpFilterConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mpeSysDevIpFilterConfigTable.setStatus("mandatory")
_MpeSysDevIpFilterConfigTableEntry_Object = MibTableRow
mpeSysDevIpFilterConfigTableEntry = _MpeSysDevIpFilterConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 1, 1)
)
mpeSysDevIpFilterConfigTableEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "PDN-MPE-FILTER-MIB", "mpeSysDevIpFilterName"),
)
if mibBuilder.loadTexts:
    mpeSysDevIpFilterConfigTableEntry.setStatus("mandatory")


class _MpeSysDevIpFilterName_Type(DisplayString):
    """Custom type mpeSysDevIpFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_MpeSysDevIpFilterName_Type.__name__ = "DisplayString"
_MpeSysDevIpFilterName_Object = MibTableColumn
mpeSysDevIpFilterName = _MpeSysDevIpFilterName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 1, 1, 1),
    _MpeSysDevIpFilterName_Type()
)
mpeSysDevIpFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterName.setStatus("mandatory")


class _MpeSysDevIpDefFilterAction_Type(Integer32):
    """Custom type mpeSysDevIpDefFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("discard", 2),
          ("forward", 1))
    )


_MpeSysDevIpDefFilterAction_Type.__name__ = "Integer32"
_MpeSysDevIpDefFilterAction_Object = MibTableColumn
mpeSysDevIpDefFilterAction = _MpeSysDevIpDefFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 1, 1, 2),
    _MpeSysDevIpDefFilterAction_Type()
)
mpeSysDevIpDefFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeSysDevIpDefFilterAction.setStatus("mandatory")
_MpeSysDevIpFilterNumOfDynamicRules_Type = Integer32
_MpeSysDevIpFilterNumOfDynamicRules_Object = MibTableColumn
mpeSysDevIpFilterNumOfDynamicRules = _MpeSysDevIpFilterNumOfDynamicRules_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 1, 1, 3),
    _MpeSysDevIpFilterNumOfDynamicRules_Type()
)
mpeSysDevIpFilterNumOfDynamicRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterNumOfDynamicRules.setStatus("mandatory")
_MpeSysDevIpFilterNumOfStaticRules_Type = Integer32
_MpeSysDevIpFilterNumOfStaticRules_Object = MibTableColumn
mpeSysDevIpFilterNumOfStaticRules = _MpeSysDevIpFilterNumOfStaticRules_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 1, 1, 4),
    _MpeSysDevIpFilterNumOfStaticRules_Type()
)
mpeSysDevIpFilterNumOfStaticRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterNumOfStaticRules.setStatus("mandatory")
_MpeSysDevIpFilterRefCount_Type = Integer32
_MpeSysDevIpFilterRefCount_Object = MibTableColumn
mpeSysDevIpFilterRefCount = _MpeSysDevIpFilterRefCount_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 1, 1, 5),
    _MpeSysDevIpFilterRefCount_Type()
)
mpeSysDevIpFilterRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterRefCount.setStatus("mandatory")


class _MpeSysDevIpFilterTcpAckFilterAction_Type(Integer32):
    """Custom type mpeSysDevIpFilterTcpAckFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1),
          ("noOp", 3))
    )


_MpeSysDevIpFilterTcpAckFilterAction_Type.__name__ = "Integer32"
_MpeSysDevIpFilterTcpAckFilterAction_Object = MibTableColumn
mpeSysDevIpFilterTcpAckFilterAction = _MpeSysDevIpFilterTcpAckFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 1, 1, 6),
    _MpeSysDevIpFilterTcpAckFilterAction_Type()
)
mpeSysDevIpFilterTcpAckFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterTcpAckFilterAction.setStatus("mandatory")


class _MpeSysDevIpFilterDhcpFilterAction_Type(Integer32):
    """Custom type mpeSysDevIpFilterDhcpFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1),
          ("noOp", 3))
    )


_MpeSysDevIpFilterDhcpFilterAction_Type.__name__ = "Integer32"
_MpeSysDevIpFilterDhcpFilterAction_Object = MibTableColumn
mpeSysDevIpFilterDhcpFilterAction = _MpeSysDevIpFilterDhcpFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 1, 1, 7),
    _MpeSysDevIpFilterDhcpFilterAction_Type()
)
mpeSysDevIpFilterDhcpFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterDhcpFilterAction.setStatus("mandatory")
_MpeSysDevIpFilterRowStatus_Type = RowStatus
_MpeSysDevIpFilterRowStatus_Object = MibTableColumn
mpeSysDevIpFilterRowStatus = _MpeSysDevIpFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 1, 1, 8),
    _MpeSysDevIpFilterRowStatus_Type()
)
mpeSysDevIpFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterRowStatus.setStatus("mandatory")
_MpeSysDevIpFilterRuleConfigTable_Object = MibTable
mpeSysDevIpFilterRuleConfigTable = _MpeSysDevIpFilterRuleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mpeSysDevIpFilterRuleConfigTable.setStatus("mandatory")
_MpeSysDevIpFilterRuleConfigTableEntry_Object = MibTableRow
mpeSysDevIpFilterRuleConfigTableEntry = _MpeSysDevIpFilterRuleConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1)
)
mpeSysDevIpFilterRuleConfigTableEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "PDN-MPE-FILTER-MIB", "mpeSysDevIpRuleFilterName"),
    (0, "PDN-MPE-FILTER-MIB", "mpeSysDevIpFilterRuleNumber"),
)
if mibBuilder.loadTexts:
    mpeSysDevIpFilterRuleConfigTableEntry.setStatus("mandatory")


class _MpeSysDevIpRuleFilterName_Type(DisplayString):
    """Custom type mpeSysDevIpRuleFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_MpeSysDevIpRuleFilterName_Type.__name__ = "DisplayString"
_MpeSysDevIpRuleFilterName_Object = MibTableColumn
mpeSysDevIpRuleFilterName = _MpeSysDevIpRuleFilterName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 1),
    _MpeSysDevIpRuleFilterName_Type()
)
mpeSysDevIpRuleFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeSysDevIpRuleFilterName.setStatus("mandatory")


class _MpeSysDevIpFilterRuleNumber_Type(Integer32):
    """Custom type mpeSysDevIpFilterRuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 33),
    )


_MpeSysDevIpFilterRuleNumber_Type.__name__ = "Integer32"
_MpeSysDevIpFilterRuleNumber_Object = MibTableColumn
mpeSysDevIpFilterRuleNumber = _MpeSysDevIpFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 2),
    _MpeSysDevIpFilterRuleNumber_Type()
)
mpeSysDevIpFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterRuleNumber.setStatus("mandatory")
_MpeSysDevIpFilterRuleSrcAddress_Type = IpAddress
_MpeSysDevIpFilterRuleSrcAddress_Object = MibTableColumn
mpeSysDevIpFilterRuleSrcAddress = _MpeSysDevIpFilterRuleSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 3),
    _MpeSysDevIpFilterRuleSrcAddress_Type()
)
mpeSysDevIpFilterRuleSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterRuleSrcAddress.setStatus("mandatory")
_MpeSysDevIpFilterRuleSrcAddrMask_Type = IpAddress
_MpeSysDevIpFilterRuleSrcAddrMask_Object = MibTableColumn
mpeSysDevIpFilterRuleSrcAddrMask = _MpeSysDevIpFilterRuleSrcAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 4),
    _MpeSysDevIpFilterRuleSrcAddrMask_Type()
)
mpeSysDevIpFilterRuleSrcAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterRuleSrcAddrMask.setStatus("mandatory")


class _MpeSysDevIpFilterRuleSrcAddrCompEnable_Type(Integer32):
    """Custom type mpeSysDevIpFilterRuleSrcAddrCompEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("noOp", 3))
    )


_MpeSysDevIpFilterRuleSrcAddrCompEnable_Type.__name__ = "Integer32"
_MpeSysDevIpFilterRuleSrcAddrCompEnable_Object = MibTableColumn
mpeSysDevIpFilterRuleSrcAddrCompEnable = _MpeSysDevIpFilterRuleSrcAddrCompEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 5),
    _MpeSysDevIpFilterRuleSrcAddrCompEnable_Type()
)
mpeSysDevIpFilterRuleSrcAddrCompEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterRuleSrcAddrCompEnable.setStatus("mandatory")


class _MpeSysDevIpFilterRuleSrcPortNum_Type(Integer32):
    """Custom type mpeSysDevIpFilterRuleSrcPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpeSysDevIpFilterRuleSrcPortNum_Type.__name__ = "Integer32"
_MpeSysDevIpFilterRuleSrcPortNum_Object = MibTableColumn
mpeSysDevIpFilterRuleSrcPortNum = _MpeSysDevIpFilterRuleSrcPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 6),
    _MpeSysDevIpFilterRuleSrcPortNum_Type()
)
mpeSysDevIpFilterRuleSrcPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterRuleSrcPortNum.setStatus("mandatory")


class _MpeSysDevIpFilterRuleMaxSrcPortNum_Type(Integer32):
    """Custom type mpeSysDevIpFilterRuleMaxSrcPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpeSysDevIpFilterRuleMaxSrcPortNum_Type.__name__ = "Integer32"
_MpeSysDevIpFilterRuleMaxSrcPortNum_Object = MibTableColumn
mpeSysDevIpFilterRuleMaxSrcPortNum = _MpeSysDevIpFilterRuleMaxSrcPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 7),
    _MpeSysDevIpFilterRuleMaxSrcPortNum_Type()
)
mpeSysDevIpFilterRuleMaxSrcPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterRuleMaxSrcPortNum.setStatus("mandatory")


class _MpeSysDevIpFilterRuleSrcCompType_Type(Integer32):
    """Custom type mpeSysDevIpFilterRuleSrcCompType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("eq", 2),
          ("gt", 4),
          ("inRange", 6),
          ("lt", 5),
          ("neq", 3),
          ("none", 1),
          ("outRange", 7))
    )


_MpeSysDevIpFilterRuleSrcCompType_Type.__name__ = "Integer32"
_MpeSysDevIpFilterRuleSrcCompType_Object = MibTableColumn
mpeSysDevIpFilterRuleSrcCompType = _MpeSysDevIpFilterRuleSrcCompType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 8),
    _MpeSysDevIpFilterRuleSrcCompType_Type()
)
mpeSysDevIpFilterRuleSrcCompType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterRuleSrcCompType.setStatus("mandatory")
_MpeSysDevIpFilterRuleDestAddress_Type = IpAddress
_MpeSysDevIpFilterRuleDestAddress_Object = MibTableColumn
mpeSysDevIpFilterRuleDestAddress = _MpeSysDevIpFilterRuleDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 9),
    _MpeSysDevIpFilterRuleDestAddress_Type()
)
mpeSysDevIpFilterRuleDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterRuleDestAddress.setStatus("mandatory")
_MpeSysDevIpFilterRuleDestAddrMask_Type = IpAddress
_MpeSysDevIpFilterRuleDestAddrMask_Object = MibTableColumn
mpeSysDevIpFilterRuleDestAddrMask = _MpeSysDevIpFilterRuleDestAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 10),
    _MpeSysDevIpFilterRuleDestAddrMask_Type()
)
mpeSysDevIpFilterRuleDestAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterRuleDestAddrMask.setStatus("mandatory")


class _MpeSysDevIpFilterRuleDestAddrCompEnable_Type(Integer32):
    """Custom type mpeSysDevIpFilterRuleDestAddrCompEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("noOp", 3))
    )


_MpeSysDevIpFilterRuleDestAddrCompEnable_Type.__name__ = "Integer32"
_MpeSysDevIpFilterRuleDestAddrCompEnable_Object = MibTableColumn
mpeSysDevIpFilterRuleDestAddrCompEnable = _MpeSysDevIpFilterRuleDestAddrCompEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 11),
    _MpeSysDevIpFilterRuleDestAddrCompEnable_Type()
)
mpeSysDevIpFilterRuleDestAddrCompEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterRuleDestAddrCompEnable.setStatus("mandatory")


class _MpeSysDevIpFilterRuleDestPortNum_Type(Integer32):
    """Custom type mpeSysDevIpFilterRuleDestPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpeSysDevIpFilterRuleDestPortNum_Type.__name__ = "Integer32"
_MpeSysDevIpFilterRuleDestPortNum_Object = MibTableColumn
mpeSysDevIpFilterRuleDestPortNum = _MpeSysDevIpFilterRuleDestPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 12),
    _MpeSysDevIpFilterRuleDestPortNum_Type()
)
mpeSysDevIpFilterRuleDestPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterRuleDestPortNum.setStatus("mandatory")


class _MpeSysDevIpFilterRuleMaxDestPortNum_Type(Integer32):
    """Custom type mpeSysDevIpFilterRuleMaxDestPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpeSysDevIpFilterRuleMaxDestPortNum_Type.__name__ = "Integer32"
_MpeSysDevIpFilterRuleMaxDestPortNum_Object = MibTableColumn
mpeSysDevIpFilterRuleMaxDestPortNum = _MpeSysDevIpFilterRuleMaxDestPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 13),
    _MpeSysDevIpFilterRuleMaxDestPortNum_Type()
)
mpeSysDevIpFilterRuleMaxDestPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterRuleMaxDestPortNum.setStatus("mandatory")


class _MpeSysDevIpFilterRuleDestCompType_Type(Integer32):
    """Custom type mpeSysDevIpFilterRuleDestCompType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("eq", 2),
          ("gt", 4),
          ("inRange", 6),
          ("lt", 5),
          ("neq", 3),
          ("none", 1),
          ("outRange", 7))
    )


_MpeSysDevIpFilterRuleDestCompType_Type.__name__ = "Integer32"
_MpeSysDevIpFilterRuleDestCompType_Object = MibTableColumn
mpeSysDevIpFilterRuleDestCompType = _MpeSysDevIpFilterRuleDestCompType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 14),
    _MpeSysDevIpFilterRuleDestCompType_Type()
)
mpeSysDevIpFilterRuleDestCompType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterRuleDestCompType.setStatus("mandatory")


class _MpeSysDevIpFilterRuleType_Type(Integer32):
    """Custom type mpeSysDevIpFilterRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_MpeSysDevIpFilterRuleType_Type.__name__ = "Integer32"
_MpeSysDevIpFilterRuleType_Object = MibTableColumn
mpeSysDevIpFilterRuleType = _MpeSysDevIpFilterRuleType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 15),
    _MpeSysDevIpFilterRuleType_Type()
)
mpeSysDevIpFilterRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterRuleType.setStatus("mandatory")


class _MpeSysDevIpFilterRuleProtocolTypeUdp_Type(Integer32):
    """Custom type mpeSysDevIpFilterRuleProtocolTypeUdp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_MpeSysDevIpFilterRuleProtocolTypeUdp_Type.__name__ = "Integer32"
_MpeSysDevIpFilterRuleProtocolTypeUdp_Object = MibTableColumn
mpeSysDevIpFilterRuleProtocolTypeUdp = _MpeSysDevIpFilterRuleProtocolTypeUdp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 16),
    _MpeSysDevIpFilterRuleProtocolTypeUdp_Type()
)
mpeSysDevIpFilterRuleProtocolTypeUdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterRuleProtocolTypeUdp.setStatus("mandatory")


class _MpeSysDevIpFilterRuleProtocolTypeTcp_Type(Integer32):
    """Custom type mpeSysDevIpFilterRuleProtocolTypeTcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_MpeSysDevIpFilterRuleProtocolTypeTcp_Type.__name__ = "Integer32"
_MpeSysDevIpFilterRuleProtocolTypeTcp_Object = MibTableColumn
mpeSysDevIpFilterRuleProtocolTypeTcp = _MpeSysDevIpFilterRuleProtocolTypeTcp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 17),
    _MpeSysDevIpFilterRuleProtocolTypeTcp_Type()
)
mpeSysDevIpFilterRuleProtocolTypeTcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterRuleProtocolTypeTcp.setStatus("mandatory")


class _MpeSysDevIpFilterRuleProtocolTypeIcmp_Type(Integer32):
    """Custom type mpeSysDevIpFilterRuleProtocolTypeIcmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_MpeSysDevIpFilterRuleProtocolTypeIcmp_Type.__name__ = "Integer32"
_MpeSysDevIpFilterRuleProtocolTypeIcmp_Object = MibTableColumn
mpeSysDevIpFilterRuleProtocolTypeIcmp = _MpeSysDevIpFilterRuleProtocolTypeIcmp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 18),
    _MpeSysDevIpFilterRuleProtocolTypeIcmp_Type()
)
mpeSysDevIpFilterRuleProtocolTypeIcmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterRuleProtocolTypeIcmp.setStatus("mandatory")
_MpeSysDevIpFilterRuleRowStatus_Type = RowStatus
_MpeSysDevIpFilterRuleRowStatus_Object = MibTableColumn
mpeSysDevIpFilterRuleRowStatus = _MpeSysDevIpFilterRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 19),
    _MpeSysDevIpFilterRuleRowStatus_Type()
)
mpeSysDevIpFilterRuleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeSysDevIpFilterRuleRowStatus.setStatus("mandatory")
_MpeSysDevMaxNumOfIpFiltersTable_Object = MibTable
mpeSysDevMaxNumOfIpFiltersTable = _MpeSysDevMaxNumOfIpFiltersTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mpeSysDevMaxNumOfIpFiltersTable.setStatus("mandatory")
_MpeSysDevMaxNumOfIpFiltersTableEntry_Object = MibTableRow
mpeSysDevMaxNumOfIpFiltersTableEntry = _MpeSysDevMaxNumOfIpFiltersTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 3, 1)
)
mpeSysDevMaxNumOfIpFiltersTableEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    mpeSysDevMaxNumOfIpFiltersTableEntry.setStatus("mandatory")
_MpeSysDevMaxNumOfInputIpFilters_Type = Integer32
_MpeSysDevMaxNumOfInputIpFilters_Object = MibTableColumn
mpeSysDevMaxNumOfInputIpFilters = _MpeSysDevMaxNumOfInputIpFilters_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 3, 1, 1),
    _MpeSysDevMaxNumOfInputIpFilters_Type()
)
mpeSysDevMaxNumOfInputIpFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeSysDevMaxNumOfInputIpFilters.setStatus("mandatory")
_MpeSysDevMaxNumOfOutputIpFilters_Type = Integer32
_MpeSysDevMaxNumOfOutputIpFilters_Object = MibTableColumn
mpeSysDevMaxNumOfOutputIpFilters = _MpeSysDevMaxNumOfOutputIpFilters_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 3, 1, 2),
    _MpeSysDevMaxNumOfOutputIpFilters_Type()
)
mpeSysDevMaxNumOfOutputIpFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeSysDevMaxNumOfOutputIpFilters.setStatus("mandatory")
_MpeSysDevFilterMIBTraps_ObjectIdentity = ObjectIdentity
mpeSysDevFilterMIBTraps = _MpeSysDevFilterMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-MPE-FILTER-MIB",
    **{"mpeSysDevFilterMIBObjects": mpeSysDevFilterMIBObjects,
       "mpeSysDevIpFilter": mpeSysDevIpFilter,
       "mpeSysDevIpFilterConfigTable": mpeSysDevIpFilterConfigTable,
       "mpeSysDevIpFilterConfigTableEntry": mpeSysDevIpFilterConfigTableEntry,
       "mpeSysDevIpFilterName": mpeSysDevIpFilterName,
       "mpeSysDevIpDefFilterAction": mpeSysDevIpDefFilterAction,
       "mpeSysDevIpFilterNumOfDynamicRules": mpeSysDevIpFilterNumOfDynamicRules,
       "mpeSysDevIpFilterNumOfStaticRules": mpeSysDevIpFilterNumOfStaticRules,
       "mpeSysDevIpFilterRefCount": mpeSysDevIpFilterRefCount,
       "mpeSysDevIpFilterTcpAckFilterAction": mpeSysDevIpFilterTcpAckFilterAction,
       "mpeSysDevIpFilterDhcpFilterAction": mpeSysDevIpFilterDhcpFilterAction,
       "mpeSysDevIpFilterRowStatus": mpeSysDevIpFilterRowStatus,
       "mpeSysDevIpFilterRuleConfigTable": mpeSysDevIpFilterRuleConfigTable,
       "mpeSysDevIpFilterRuleConfigTableEntry": mpeSysDevIpFilterRuleConfigTableEntry,
       "mpeSysDevIpRuleFilterName": mpeSysDevIpRuleFilterName,
       "mpeSysDevIpFilterRuleNumber": mpeSysDevIpFilterRuleNumber,
       "mpeSysDevIpFilterRuleSrcAddress": mpeSysDevIpFilterRuleSrcAddress,
       "mpeSysDevIpFilterRuleSrcAddrMask": mpeSysDevIpFilterRuleSrcAddrMask,
       "mpeSysDevIpFilterRuleSrcAddrCompEnable": mpeSysDevIpFilterRuleSrcAddrCompEnable,
       "mpeSysDevIpFilterRuleSrcPortNum": mpeSysDevIpFilterRuleSrcPortNum,
       "mpeSysDevIpFilterRuleMaxSrcPortNum": mpeSysDevIpFilterRuleMaxSrcPortNum,
       "mpeSysDevIpFilterRuleSrcCompType": mpeSysDevIpFilterRuleSrcCompType,
       "mpeSysDevIpFilterRuleDestAddress": mpeSysDevIpFilterRuleDestAddress,
       "mpeSysDevIpFilterRuleDestAddrMask": mpeSysDevIpFilterRuleDestAddrMask,
       "mpeSysDevIpFilterRuleDestAddrCompEnable": mpeSysDevIpFilterRuleDestAddrCompEnable,
       "mpeSysDevIpFilterRuleDestPortNum": mpeSysDevIpFilterRuleDestPortNum,
       "mpeSysDevIpFilterRuleMaxDestPortNum": mpeSysDevIpFilterRuleMaxDestPortNum,
       "mpeSysDevIpFilterRuleDestCompType": mpeSysDevIpFilterRuleDestCompType,
       "mpeSysDevIpFilterRuleType": mpeSysDevIpFilterRuleType,
       "mpeSysDevIpFilterRuleProtocolTypeUdp": mpeSysDevIpFilterRuleProtocolTypeUdp,
       "mpeSysDevIpFilterRuleProtocolTypeTcp": mpeSysDevIpFilterRuleProtocolTypeTcp,
       "mpeSysDevIpFilterRuleProtocolTypeIcmp": mpeSysDevIpFilterRuleProtocolTypeIcmp,
       "mpeSysDevIpFilterRuleRowStatus": mpeSysDevIpFilterRuleRowStatus,
       "mpeSysDevMaxNumOfIpFiltersTable": mpeSysDevMaxNumOfIpFiltersTable,
       "mpeSysDevMaxNumOfIpFiltersTableEntry": mpeSysDevMaxNumOfIpFiltersTableEntry,
       "mpeSysDevMaxNumOfInputIpFilters": mpeSysDevMaxNumOfInputIpFilters,
       "mpeSysDevMaxNumOfOutputIpFilters": mpeSysDevMaxNumOfOutputIpFilters,
       "mpeSysDevFilterMIBTraps": mpeSysDevFilterMIBTraps}
)
