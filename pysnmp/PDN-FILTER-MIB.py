# SNMP MIB module (PDN-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-FILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:40 2024
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

(pdn_filter,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-filter")

(VnidRange,) = mibBuilder.importSymbols(
    "PDN-TC",
    "VnidRange")

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

_SysDevFilterMIBObjects_ObjectIdentity = ObjectIdentity
sysDevFilterMIBObjects = _SysDevFilterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1)
)
_SysDevFilter_ObjectIdentity = ObjectIdentity
sysDevFilter = _SysDevFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1)
)


class _SysDevSNInjectionType_Type(Integer32):
    """Custom type sysDevSNInjectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipFilter", 1)
    )


_SysDevSNInjectionType_Type.__name__ = "Integer32"
_SysDevSNInjectionType_Object = MibScalar
sysDevSNInjectionType = _SysDevSNInjectionType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 1),
    _SysDevSNInjectionType_Type()
)
sysDevSNInjectionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysDevSNInjectionType.setStatus("mandatory")
_SysDevSNInjectionVnid_Type = VnidRange
_SysDevSNInjectionVnid_Object = MibScalar
sysDevSNInjectionVnid = _SysDevSNInjectionVnid_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 1, 2),
    _SysDevSNInjectionVnid_Type()
)
sysDevSNInjectionVnid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysDevSNInjectionVnid.setStatus("mandatory")
_SysDevIpFilter_ObjectIdentity = ObjectIdentity
sysDevIpFilter = _SysDevIpFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2)
)
_SysDevIpFilterConfigTable_Object = MibTable
sysDevIpFilterConfigTable = _SysDevIpFilterConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sysDevIpFilterConfigTable.setStatus("mandatory")
_SysDevIpFilterConfigTableEntry_Object = MibTableRow
sysDevIpFilterConfigTableEntry = _SysDevIpFilterConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 1, 1)
)
sysDevIpFilterConfigTableEntry.setIndexNames(
    (0, "PDN-FILTER-MIB", "sysDevIpFilterName"),
)
if mibBuilder.loadTexts:
    sysDevIpFilterConfigTableEntry.setStatus("mandatory")


class _SysDevIpFilterName_Type(DisplayString):
    """Custom type sysDevIpFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SysDevIpFilterName_Type.__name__ = "DisplayString"
_SysDevIpFilterName_Object = MibTableColumn
sysDevIpFilterName = _SysDevIpFilterName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 1, 1, 1),
    _SysDevIpFilterName_Type()
)
sysDevIpFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevIpFilterName.setStatus("mandatory")


class _SysDevIpDefFilterAction_Type(Integer32):
    """Custom type sysDevIpDefFilterAction based on Integer32"""
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


_SysDevIpDefFilterAction_Type.__name__ = "Integer32"
_SysDevIpDefFilterAction_Object = MibTableColumn
sysDevIpDefFilterAction = _SysDevIpDefFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 1, 1, 2),
    _SysDevIpDefFilterAction_Type()
)
sysDevIpDefFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpDefFilterAction.setStatus("mandatory")
_SysDevIpFilterNumOfDynamicRules_Type = Integer32
_SysDevIpFilterNumOfDynamicRules_Object = MibTableColumn
sysDevIpFilterNumOfDynamicRules = _SysDevIpFilterNumOfDynamicRules_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 1, 1, 3),
    _SysDevIpFilterNumOfDynamicRules_Type()
)
sysDevIpFilterNumOfDynamicRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevIpFilterNumOfDynamicRules.setStatus("mandatory")
_SysDevIpFilterNumOfStaticRules_Type = Integer32
_SysDevIpFilterNumOfStaticRules_Object = MibTableColumn
sysDevIpFilterNumOfStaticRules = _SysDevIpFilterNumOfStaticRules_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 1, 1, 4),
    _SysDevIpFilterNumOfStaticRules_Type()
)
sysDevIpFilterNumOfStaticRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevIpFilterNumOfStaticRules.setStatus("mandatory")
_SysDevIpFilterRefCount_Type = Integer32
_SysDevIpFilterRefCount_Object = MibTableColumn
sysDevIpFilterRefCount = _SysDevIpFilterRefCount_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 1, 1, 5),
    _SysDevIpFilterRefCount_Type()
)
sysDevIpFilterRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevIpFilterRefCount.setStatus("mandatory")


class _SysDevIpFilterTcpAckFilterAction_Type(Integer32):
    """Custom type sysDevIpFilterTcpAckFilterAction based on Integer32"""
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


_SysDevIpFilterTcpAckFilterAction_Type.__name__ = "Integer32"
_SysDevIpFilterTcpAckFilterAction_Object = MibTableColumn
sysDevIpFilterTcpAckFilterAction = _SysDevIpFilterTcpAckFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 1, 1, 6),
    _SysDevIpFilterTcpAckFilterAction_Type()
)
sysDevIpFilterTcpAckFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterTcpAckFilterAction.setStatus("mandatory")


class _SysDevIpFilterDhcpFilterAction_Type(Integer32):
    """Custom type sysDevIpFilterDhcpFilterAction based on Integer32"""
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


_SysDevIpFilterDhcpFilterAction_Type.__name__ = "Integer32"
_SysDevIpFilterDhcpFilterAction_Object = MibTableColumn
sysDevIpFilterDhcpFilterAction = _SysDevIpFilterDhcpFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 1, 1, 7),
    _SysDevIpFilterDhcpFilterAction_Type()
)
sysDevIpFilterDhcpFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterDhcpFilterAction.setStatus("mandatory")
_SysDevIpFilterRowStatus_Type = RowStatus
_SysDevIpFilterRowStatus_Object = MibTableColumn
sysDevIpFilterRowStatus = _SysDevIpFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 1, 1, 8),
    _SysDevIpFilterRowStatus_Type()
)
sysDevIpFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRowStatus.setStatus("mandatory")
_SysDevIpFilterRuleConfigTable_Object = MibTable
sysDevIpFilterRuleConfigTable = _SysDevIpFilterRuleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sysDevIpFilterRuleConfigTable.setStatus("mandatory")
_SysDevIpFilterRuleConfigTableEntry_Object = MibTableRow
sysDevIpFilterRuleConfigTableEntry = _SysDevIpFilterRuleConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1)
)
sysDevIpFilterRuleConfigTableEntry.setIndexNames(
    (0, "PDN-FILTER-MIB", "sysDevIpRuleFilterName"),
    (0, "PDN-FILTER-MIB", "sysDevIpFilterRuleNumber"),
)
if mibBuilder.loadTexts:
    sysDevIpFilterRuleConfigTableEntry.setStatus("mandatory")


class _SysDevIpRuleFilterName_Type(DisplayString):
    """Custom type sysDevIpRuleFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SysDevIpRuleFilterName_Type.__name__ = "DisplayString"
_SysDevIpRuleFilterName_Object = MibTableColumn
sysDevIpRuleFilterName = _SysDevIpRuleFilterName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 1),
    _SysDevIpRuleFilterName_Type()
)
sysDevIpRuleFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevIpRuleFilterName.setStatus("mandatory")


class _SysDevIpFilterRuleNumber_Type(Integer32):
    """Custom type sysDevIpFilterRuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 33),
    )


_SysDevIpFilterRuleNumber_Type.__name__ = "Integer32"
_SysDevIpFilterRuleNumber_Object = MibTableColumn
sysDevIpFilterRuleNumber = _SysDevIpFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 2),
    _SysDevIpFilterRuleNumber_Type()
)
sysDevIpFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleNumber.setStatus("mandatory")
_SysDevIpFilterRuleSrcAddress_Type = IpAddress
_SysDevIpFilterRuleSrcAddress_Object = MibTableColumn
sysDevIpFilterRuleSrcAddress = _SysDevIpFilterRuleSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 3),
    _SysDevIpFilterRuleSrcAddress_Type()
)
sysDevIpFilterRuleSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleSrcAddress.setStatus("mandatory")
_SysDevIpFilterRuleSrcAddrMask_Type = IpAddress
_SysDevIpFilterRuleSrcAddrMask_Object = MibTableColumn
sysDevIpFilterRuleSrcAddrMask = _SysDevIpFilterRuleSrcAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 4),
    _SysDevIpFilterRuleSrcAddrMask_Type()
)
sysDevIpFilterRuleSrcAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleSrcAddrMask.setStatus("mandatory")


class _SysDevIpFilterRuleSrcAddrCompEnable_Type(Integer32):
    """Custom type sysDevIpFilterRuleSrcAddrCompEnable based on Integer32"""
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


_SysDevIpFilterRuleSrcAddrCompEnable_Type.__name__ = "Integer32"
_SysDevIpFilterRuleSrcAddrCompEnable_Object = MibTableColumn
sysDevIpFilterRuleSrcAddrCompEnable = _SysDevIpFilterRuleSrcAddrCompEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 5),
    _SysDevIpFilterRuleSrcAddrCompEnable_Type()
)
sysDevIpFilterRuleSrcAddrCompEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleSrcAddrCompEnable.setStatus("mandatory")


class _SysDevIpFilterRuleSrcPortNum_Type(Integer32):
    """Custom type sysDevIpFilterRuleSrcPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SysDevIpFilterRuleSrcPortNum_Type.__name__ = "Integer32"
_SysDevIpFilterRuleSrcPortNum_Object = MibTableColumn
sysDevIpFilterRuleSrcPortNum = _SysDevIpFilterRuleSrcPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 6),
    _SysDevIpFilterRuleSrcPortNum_Type()
)
sysDevIpFilterRuleSrcPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleSrcPortNum.setStatus("mandatory")


class _SysDevIpFilterRuleMaxSrcPortNum_Type(Integer32):
    """Custom type sysDevIpFilterRuleMaxSrcPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SysDevIpFilterRuleMaxSrcPortNum_Type.__name__ = "Integer32"
_SysDevIpFilterRuleMaxSrcPortNum_Object = MibTableColumn
sysDevIpFilterRuleMaxSrcPortNum = _SysDevIpFilterRuleMaxSrcPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 7),
    _SysDevIpFilterRuleMaxSrcPortNum_Type()
)
sysDevIpFilterRuleMaxSrcPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleMaxSrcPortNum.setStatus("mandatory")


class _SysDevIpFilterRuleSrcCompType_Type(Integer32):
    """Custom type sysDevIpFilterRuleSrcCompType based on Integer32"""
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


_SysDevIpFilterRuleSrcCompType_Type.__name__ = "Integer32"
_SysDevIpFilterRuleSrcCompType_Object = MibTableColumn
sysDevIpFilterRuleSrcCompType = _SysDevIpFilterRuleSrcCompType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 8),
    _SysDevIpFilterRuleSrcCompType_Type()
)
sysDevIpFilterRuleSrcCompType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleSrcCompType.setStatus("mandatory")
_SysDevIpFilterRuleDestAddress_Type = IpAddress
_SysDevIpFilterRuleDestAddress_Object = MibTableColumn
sysDevIpFilterRuleDestAddress = _SysDevIpFilterRuleDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 9),
    _SysDevIpFilterRuleDestAddress_Type()
)
sysDevIpFilterRuleDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleDestAddress.setStatus("mandatory")
_SysDevIpFilterRuleDestAddrMask_Type = IpAddress
_SysDevIpFilterRuleDestAddrMask_Object = MibTableColumn
sysDevIpFilterRuleDestAddrMask = _SysDevIpFilterRuleDestAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 10),
    _SysDevIpFilterRuleDestAddrMask_Type()
)
sysDevIpFilterRuleDestAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleDestAddrMask.setStatus("mandatory")


class _SysDevIpFilterRuleDestAddrCompEnable_Type(Integer32):
    """Custom type sysDevIpFilterRuleDestAddrCompEnable based on Integer32"""
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


_SysDevIpFilterRuleDestAddrCompEnable_Type.__name__ = "Integer32"
_SysDevIpFilterRuleDestAddrCompEnable_Object = MibTableColumn
sysDevIpFilterRuleDestAddrCompEnable = _SysDevIpFilterRuleDestAddrCompEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 11),
    _SysDevIpFilterRuleDestAddrCompEnable_Type()
)
sysDevIpFilterRuleDestAddrCompEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleDestAddrCompEnable.setStatus("mandatory")


class _SysDevIpFilterRuleDestPortNum_Type(Integer32):
    """Custom type sysDevIpFilterRuleDestPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SysDevIpFilterRuleDestPortNum_Type.__name__ = "Integer32"
_SysDevIpFilterRuleDestPortNum_Object = MibTableColumn
sysDevIpFilterRuleDestPortNum = _SysDevIpFilterRuleDestPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 12),
    _SysDevIpFilterRuleDestPortNum_Type()
)
sysDevIpFilterRuleDestPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleDestPortNum.setStatus("mandatory")


class _SysDevIpFilterRuleMaxDestPortNum_Type(Integer32):
    """Custom type sysDevIpFilterRuleMaxDestPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SysDevIpFilterRuleMaxDestPortNum_Type.__name__ = "Integer32"
_SysDevIpFilterRuleMaxDestPortNum_Object = MibTableColumn
sysDevIpFilterRuleMaxDestPortNum = _SysDevIpFilterRuleMaxDestPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 13),
    _SysDevIpFilterRuleMaxDestPortNum_Type()
)
sysDevIpFilterRuleMaxDestPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleMaxDestPortNum.setStatus("mandatory")


class _SysDevIpFilterRuleDestCompType_Type(Integer32):
    """Custom type sysDevIpFilterRuleDestCompType based on Integer32"""
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


_SysDevIpFilterRuleDestCompType_Type.__name__ = "Integer32"
_SysDevIpFilterRuleDestCompType_Object = MibTableColumn
sysDevIpFilterRuleDestCompType = _SysDevIpFilterRuleDestCompType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 14),
    _SysDevIpFilterRuleDestCompType_Type()
)
sysDevIpFilterRuleDestCompType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleDestCompType.setStatus("mandatory")


class _SysDevIpFilterRuleType_Type(Integer32):
    """Custom type sysDevIpFilterRuleType based on Integer32"""
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


_SysDevIpFilterRuleType_Type.__name__ = "Integer32"
_SysDevIpFilterRuleType_Object = MibTableColumn
sysDevIpFilterRuleType = _SysDevIpFilterRuleType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 15),
    _SysDevIpFilterRuleType_Type()
)
sysDevIpFilterRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleType.setStatus("mandatory")


class _SysDevIpFilterRuleProtocolTypeUdp_Type(Integer32):
    """Custom type sysDevIpFilterRuleProtocolTypeUdp based on Integer32"""
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


_SysDevIpFilterRuleProtocolTypeUdp_Type.__name__ = "Integer32"
_SysDevIpFilterRuleProtocolTypeUdp_Object = MibTableColumn
sysDevIpFilterRuleProtocolTypeUdp = _SysDevIpFilterRuleProtocolTypeUdp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 16),
    _SysDevIpFilterRuleProtocolTypeUdp_Type()
)
sysDevIpFilterRuleProtocolTypeUdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleProtocolTypeUdp.setStatus("mandatory")


class _SysDevIpFilterRuleProtocolTypeTcp_Type(Integer32):
    """Custom type sysDevIpFilterRuleProtocolTypeTcp based on Integer32"""
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


_SysDevIpFilterRuleProtocolTypeTcp_Type.__name__ = "Integer32"
_SysDevIpFilterRuleProtocolTypeTcp_Object = MibTableColumn
sysDevIpFilterRuleProtocolTypeTcp = _SysDevIpFilterRuleProtocolTypeTcp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 17),
    _SysDevIpFilterRuleProtocolTypeTcp_Type()
)
sysDevIpFilterRuleProtocolTypeTcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleProtocolTypeTcp.setStatus("mandatory")


class _SysDevIpFilterRuleProtocolTypeIcmp_Type(Integer32):
    """Custom type sysDevIpFilterRuleProtocolTypeIcmp based on Integer32"""
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


_SysDevIpFilterRuleProtocolTypeIcmp_Type.__name__ = "Integer32"
_SysDevIpFilterRuleProtocolTypeIcmp_Object = MibTableColumn
sysDevIpFilterRuleProtocolTypeIcmp = _SysDevIpFilterRuleProtocolTypeIcmp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 18),
    _SysDevIpFilterRuleProtocolTypeIcmp_Type()
)
sysDevIpFilterRuleProtocolTypeIcmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleProtocolTypeIcmp.setStatus("mandatory")
_SysDevIpFilterRuleRowStatus_Type = RowStatus
_SysDevIpFilterRuleRowStatus_Object = MibTableColumn
sysDevIpFilterRuleRowStatus = _SysDevIpFilterRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 2, 1, 19),
    _SysDevIpFilterRuleRowStatus_Type()
)
sysDevIpFilterRuleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpFilterRuleRowStatus.setStatus("mandatory")
_SysDevMaxNumOfInputIpFilters_Type = Integer32
_SysDevMaxNumOfInputIpFilters_Object = MibScalar
sysDevMaxNumOfInputIpFilters = _SysDevMaxNumOfInputIpFilters_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 3),
    _SysDevMaxNumOfInputIpFilters_Type()
)
sysDevMaxNumOfInputIpFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevMaxNumOfInputIpFilters.setStatus("mandatory")
_SysDevMaxNumOfOutputIpFilters_Type = Integer32
_SysDevMaxNumOfOutputIpFilters_Object = MibScalar
sysDevMaxNumOfOutputIpFilters = _SysDevMaxNumOfOutputIpFilters_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 4),
    _SysDevMaxNumOfOutputIpFilters_Type()
)
sysDevMaxNumOfOutputIpFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevMaxNumOfOutputIpFilters.setStatus("mandatory")
_SysDevIpFilterBindingTable_Object = MibTable
sysDevIpFilterBindingTable = _SysDevIpFilterBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 5)
)
if mibBuilder.loadTexts:
    sysDevIpFilterBindingTable.setStatus("mandatory")
_SysDevIpFilterBindingTableEntry_Object = MibTableRow
sysDevIpFilterBindingTableEntry = _SysDevIpFilterBindingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 5, 1)
)
sysDevIpFilterBindingTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PDN-FILTER-MIB", "sysDevIpBindingFilterName"),
)
if mibBuilder.loadTexts:
    sysDevIpFilterBindingTableEntry.setStatus("mandatory")


class _SysDevIpBindingFilterName_Type(DisplayString):
    """Custom type sysDevIpBindingFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SysDevIpBindingFilterName_Type.__name__ = "DisplayString"
_SysDevIpBindingFilterName_Object = MibTableColumn
sysDevIpBindingFilterName = _SysDevIpBindingFilterName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 5, 1, 1),
    _SysDevIpBindingFilterName_Type()
)
sysDevIpBindingFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevIpBindingFilterName.setStatus("mandatory")


class _SysDevIpBindingFilterType_Type(Integer32):
    """Custom type sysDevIpBindingFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inputFilter", 1),
          ("inputOutputFilter", 3),
          ("outputFilter", 2))
    )


_SysDevIpBindingFilterType_Type.__name__ = "Integer32"
_SysDevIpBindingFilterType_Object = MibTableColumn
sysDevIpBindingFilterType = _SysDevIpBindingFilterType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 5, 1, 2),
    _SysDevIpBindingFilterType_Type()
)
sysDevIpBindingFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpBindingFilterType.setStatus("mandatory")
_SysDevIpBindingFilterRowStatus_Type = RowStatus
_SysDevIpBindingFilterRowStatus_Object = MibTableColumn
sysDevIpBindingFilterRowStatus = _SysDevIpBindingFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 5, 1, 3),
    _SysDevIpBindingFilterRowStatus_Type()
)
sysDevIpBindingFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpBindingFilterRowStatus.setStatus("mandatory")
_SysDevIpFilterSNBindingTable_Object = MibTable
sysDevIpFilterSNBindingTable = _SysDevIpFilterSNBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 6)
)
if mibBuilder.loadTexts:
    sysDevIpFilterSNBindingTable.setStatus("mandatory")
_SysDevIpFilterSNBindingTableEntry_Object = MibTableRow
sysDevIpFilterSNBindingTableEntry = _SysDevIpFilterSNBindingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 6, 1)
)
sysDevIpFilterSNBindingTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PDN-FILTER-MIB", "sysDevIpSNBindingVnidId"),
    (0, "PDN-FILTER-MIB", "sysDevIpSNBindingFilterName"),
)
if mibBuilder.loadTexts:
    sysDevIpFilterSNBindingTableEntry.setStatus("mandatory")
_SysDevIpSNBindingVnidId_Type = VnidRange
_SysDevIpSNBindingVnidId_Object = MibTableColumn
sysDevIpSNBindingVnidId = _SysDevIpSNBindingVnidId_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 6, 1, 1),
    _SysDevIpSNBindingVnidId_Type()
)
sysDevIpSNBindingVnidId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevIpSNBindingVnidId.setStatus("mandatory")


class _SysDevIpSNBindingFilterName_Type(DisplayString):
    """Custom type sysDevIpSNBindingFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SysDevIpSNBindingFilterName_Type.__name__ = "DisplayString"
_SysDevIpSNBindingFilterName_Object = MibTableColumn
sysDevIpSNBindingFilterName = _SysDevIpSNBindingFilterName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 6, 1, 2),
    _SysDevIpSNBindingFilterName_Type()
)
sysDevIpSNBindingFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevIpSNBindingFilterName.setStatus("mandatory")


class _SysDevIpSNBindingFilterType_Type(Integer32):
    """Custom type sysDevIpSNBindingFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inputFilter", 1),
          ("inputOutputFilter", 3),
          ("outputFilter", 2))
    )


_SysDevIpSNBindingFilterType_Type.__name__ = "Integer32"
_SysDevIpSNBindingFilterType_Object = MibTableColumn
sysDevIpSNBindingFilterType = _SysDevIpSNBindingFilterType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 6, 1, 3),
    _SysDevIpSNBindingFilterType_Type()
)
sysDevIpSNBindingFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpSNBindingFilterType.setStatus("mandatory")
_SysDevIpSNBindingFilterRowStatus_Type = RowStatus
_SysDevIpSNBindingFilterRowStatus_Object = MibTableColumn
sysDevIpSNBindingFilterRowStatus = _SysDevIpSNBindingFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 6, 1, 4),
    _SysDevIpSNBindingFilterRowStatus_Type()
)
sysDevIpSNBindingFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIpSNBindingFilterRowStatus.setStatus("mandatory")
_SysDevIpInputPacketsFiltered_Type = Counter32
_SysDevIpInputPacketsFiltered_Object = MibScalar
sysDevIpInputPacketsFiltered = _SysDevIpInputPacketsFiltered_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 7),
    _SysDevIpInputPacketsFiltered_Type()
)
sysDevIpInputPacketsFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevIpInputPacketsFiltered.setStatus("mandatory")
_SysDevIpOutputPacketsFiltered_Type = Counter32
_SysDevIpOutputPacketsFiltered_Object = MibScalar
sysDevIpOutputPacketsFiltered = _SysDevIpOutputPacketsFiltered_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 1, 2, 8),
    _SysDevIpOutputPacketsFiltered_Type()
)
sysDevIpOutputPacketsFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevIpOutputPacketsFiltered.setStatus("mandatory")
_SysDevFilterMIBTraps_ObjectIdentity = ObjectIdentity
sysDevFilterMIBTraps = _SysDevFilterMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 2)
)

# Managed Objects groups


# Notification objects

sysDevSNInjectionFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 2, 0, 22)
)
sysDevSNInjectionFailureTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PDN-FILTER-MIB", "sysDevSNInjectionVnid"),
        ("PDN-FILTER-MIB", "sysDevSNInjectionType"))
)
if mibBuilder.loadTexts:
    sysDevSNInjectionFailureTrap.setStatus(
        ""
    )

sysDevSNInjectionIncompatibleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23, 2, 0, 23)
)
sysDevSNInjectionIncompatibleTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PDN-FILTER-MIB", "sysDevSNInjectionVnid"),
        ("PDN-FILTER-MIB", "sysDevSNInjectionType"))
)
if mibBuilder.loadTexts:
    sysDevSNInjectionIncompatibleTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-FILTER-MIB",
    **{"sysDevFilterMIBObjects": sysDevFilterMIBObjects,
       "sysDevFilter": sysDevFilter,
       "sysDevSNInjectionType": sysDevSNInjectionType,
       "sysDevSNInjectionVnid": sysDevSNInjectionVnid,
       "sysDevIpFilter": sysDevIpFilter,
       "sysDevIpFilterConfigTable": sysDevIpFilterConfigTable,
       "sysDevIpFilterConfigTableEntry": sysDevIpFilterConfigTableEntry,
       "sysDevIpFilterName": sysDevIpFilterName,
       "sysDevIpDefFilterAction": sysDevIpDefFilterAction,
       "sysDevIpFilterNumOfDynamicRules": sysDevIpFilterNumOfDynamicRules,
       "sysDevIpFilterNumOfStaticRules": sysDevIpFilterNumOfStaticRules,
       "sysDevIpFilterRefCount": sysDevIpFilterRefCount,
       "sysDevIpFilterTcpAckFilterAction": sysDevIpFilterTcpAckFilterAction,
       "sysDevIpFilterDhcpFilterAction": sysDevIpFilterDhcpFilterAction,
       "sysDevIpFilterRowStatus": sysDevIpFilterRowStatus,
       "sysDevIpFilterRuleConfigTable": sysDevIpFilterRuleConfigTable,
       "sysDevIpFilterRuleConfigTableEntry": sysDevIpFilterRuleConfigTableEntry,
       "sysDevIpRuleFilterName": sysDevIpRuleFilterName,
       "sysDevIpFilterRuleNumber": sysDevIpFilterRuleNumber,
       "sysDevIpFilterRuleSrcAddress": sysDevIpFilterRuleSrcAddress,
       "sysDevIpFilterRuleSrcAddrMask": sysDevIpFilterRuleSrcAddrMask,
       "sysDevIpFilterRuleSrcAddrCompEnable": sysDevIpFilterRuleSrcAddrCompEnable,
       "sysDevIpFilterRuleSrcPortNum": sysDevIpFilterRuleSrcPortNum,
       "sysDevIpFilterRuleMaxSrcPortNum": sysDevIpFilterRuleMaxSrcPortNum,
       "sysDevIpFilterRuleSrcCompType": sysDevIpFilterRuleSrcCompType,
       "sysDevIpFilterRuleDestAddress": sysDevIpFilterRuleDestAddress,
       "sysDevIpFilterRuleDestAddrMask": sysDevIpFilterRuleDestAddrMask,
       "sysDevIpFilterRuleDestAddrCompEnable": sysDevIpFilterRuleDestAddrCompEnable,
       "sysDevIpFilterRuleDestPortNum": sysDevIpFilterRuleDestPortNum,
       "sysDevIpFilterRuleMaxDestPortNum": sysDevIpFilterRuleMaxDestPortNum,
       "sysDevIpFilterRuleDestCompType": sysDevIpFilterRuleDestCompType,
       "sysDevIpFilterRuleType": sysDevIpFilterRuleType,
       "sysDevIpFilterRuleProtocolTypeUdp": sysDevIpFilterRuleProtocolTypeUdp,
       "sysDevIpFilterRuleProtocolTypeTcp": sysDevIpFilterRuleProtocolTypeTcp,
       "sysDevIpFilterRuleProtocolTypeIcmp": sysDevIpFilterRuleProtocolTypeIcmp,
       "sysDevIpFilterRuleRowStatus": sysDevIpFilterRuleRowStatus,
       "sysDevMaxNumOfInputIpFilters": sysDevMaxNumOfInputIpFilters,
       "sysDevMaxNumOfOutputIpFilters": sysDevMaxNumOfOutputIpFilters,
       "sysDevIpFilterBindingTable": sysDevIpFilterBindingTable,
       "sysDevIpFilterBindingTableEntry": sysDevIpFilterBindingTableEntry,
       "sysDevIpBindingFilterName": sysDevIpBindingFilterName,
       "sysDevIpBindingFilterType": sysDevIpBindingFilterType,
       "sysDevIpBindingFilterRowStatus": sysDevIpBindingFilterRowStatus,
       "sysDevIpFilterSNBindingTable": sysDevIpFilterSNBindingTable,
       "sysDevIpFilterSNBindingTableEntry": sysDevIpFilterSNBindingTableEntry,
       "sysDevIpSNBindingVnidId": sysDevIpSNBindingVnidId,
       "sysDevIpSNBindingFilterName": sysDevIpSNBindingFilterName,
       "sysDevIpSNBindingFilterType": sysDevIpSNBindingFilterType,
       "sysDevIpSNBindingFilterRowStatus": sysDevIpSNBindingFilterRowStatus,
       "sysDevIpInputPacketsFiltered": sysDevIpInputPacketsFiltered,
       "sysDevIpOutputPacketsFiltered": sysDevIpOutputPacketsFiltered,
       "sysDevFilterMIBTraps": sysDevFilterMIBTraps,
       "sysDevSNInjectionFailureTrap": sysDevSNInjectionFailureTrap,
       "sysDevSNInjectionIncompatibleTrap": sysDevSNInjectionIncompatibleTrap}
)
