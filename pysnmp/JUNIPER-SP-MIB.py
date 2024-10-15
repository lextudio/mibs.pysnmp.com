# SNMP MIB module (JUNIPER-SP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-SP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:39 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

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

jnxSpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32)
)
jnxSpMIB.setRevisions(
        ("2005-04-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxSpNotifications_ObjectIdentity = ObjectIdentity
jnxSpNotifications = _JnxSpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 0)
)
_JnxSpNotificationPrefix_ObjectIdentity = ObjectIdentity
jnxSpNotificationPrefix = _JnxSpNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 0, 0)
)
if mibBuilder.loadTexts:
    jnxSpNotificationPrefix.setStatus("current")
_JnxSpSvcSet_ObjectIdentity = ObjectIdentity
jnxSpSvcSet = _JnxSpSvcSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1)
)
if mibBuilder.loadTexts:
    jnxSpSvcSet.setStatus("current")
_JnxSpSvcSetTable_Object = MibTable
jnxSpSvcSetTable = _JnxSpSvcSetTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1)
)
if mibBuilder.loadTexts:
    jnxSpSvcSetTable.setStatus("current")
_JnxSpSvcSetEntry_Object = MibTableRow
jnxSpSvcSetEntry = _JnxSpSvcSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1)
)
jnxSpSvcSetEntry.setIndexNames(
    (0, "JUNIPER-SP-MIB", "jnxSpSvcSetName"),
)
if mibBuilder.loadTexts:
    jnxSpSvcSetEntry.setStatus("current")


class _JnxSpSvcSetName_Type(DisplayString):
    """Custom type jnxSpSvcSetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )


_JnxSpSvcSetName_Type.__name__ = "DisplayString"
_JnxSpSvcSetName_Object = MibTableColumn
jnxSpSvcSetName = _JnxSpSvcSetName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 1),
    _JnxSpSvcSetName_Type()
)
jnxSpSvcSetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSpSvcSetName.setStatus("current")
_JnxSpSvcSetSvcType_Type = DisplayString
_JnxSpSvcSetSvcType_Object = MibTableColumn
jnxSpSvcSetSvcType = _JnxSpSvcSetSvcType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 2),
    _JnxSpSvcSetSvcType_Type()
)
jnxSpSvcSetSvcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcType.setStatus("current")


class _JnxSpSvcSetTypeIndex_Type(Integer32):
    """Custom type jnxSpSvcSetTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxSpSvcSetTypeIndex_Type.__name__ = "Integer32"
_JnxSpSvcSetTypeIndex_Object = MibTableColumn
jnxSpSvcSetTypeIndex = _JnxSpSvcSetTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 3),
    _JnxSpSvcSetTypeIndex_Type()
)
jnxSpSvcSetTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetTypeIndex.setStatus("current")
_JnxSpSvcSetIfName_Type = DisplayString
_JnxSpSvcSetIfName_Object = MibTableColumn
jnxSpSvcSetIfName = _JnxSpSvcSetIfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 4),
    _JnxSpSvcSetIfName_Type()
)
jnxSpSvcSetIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfName.setStatus("current")
_JnxSpSvcSetIfIndex_Type = InterfaceIndex
_JnxSpSvcSetIfIndex_Object = MibTableColumn
jnxSpSvcSetIfIndex = _JnxSpSvcSetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 5),
    _JnxSpSvcSetIfIndex_Type()
)
jnxSpSvcSetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfIndex.setStatus("current")
_JnxSpSvcSetMemoryUsage_Type = Gauge32
_JnxSpSvcSetMemoryUsage_Object = MibTableColumn
jnxSpSvcSetMemoryUsage = _JnxSpSvcSetMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 6),
    _JnxSpSvcSetMemoryUsage_Type()
)
jnxSpSvcSetMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetMemoryUsage.setUnits("bytes")
_JnxSpSvcSetCpuUtil_Type = Gauge32
_JnxSpSvcSetCpuUtil_Object = MibTableColumn
jnxSpSvcSetCpuUtil = _JnxSpSvcSetCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 7),
    _JnxSpSvcSetCpuUtil_Type()
)
jnxSpSvcSetCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetCpuUtil.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetCpuUtil.setUnits("percent")


class _JnxSpSvcSetSvcStyle_Type(Integer32):
    """Custom type jnxSpSvcSetSvcStyle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interface-service", 2),
          ("next-hop-service", 3),
          ("unknown", 1))
    )


_JnxSpSvcSetSvcStyle_Type.__name__ = "Integer32"
_JnxSpSvcSetSvcStyle_Object = MibTableColumn
jnxSpSvcSetSvcStyle = _JnxSpSvcSetSvcStyle_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 8),
    _JnxSpSvcSetSvcStyle_Type()
)
jnxSpSvcSetSvcStyle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcStyle.setStatus("current")
_JnxSpSvcSetMemLimitPktDrops_Type = Counter32
_JnxSpSvcSetMemLimitPktDrops_Object = MibTableColumn
jnxSpSvcSetMemLimitPktDrops = _JnxSpSvcSetMemLimitPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 9),
    _JnxSpSvcSetMemLimitPktDrops_Type()
)
jnxSpSvcSetMemLimitPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetMemLimitPktDrops.setStatus("current")
_JnxSpSvcSetCpuLimitPktDrops_Type = Counter32
_JnxSpSvcSetCpuLimitPktDrops_Object = MibTableColumn
jnxSpSvcSetCpuLimitPktDrops = _JnxSpSvcSetCpuLimitPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 10),
    _JnxSpSvcSetCpuLimitPktDrops_Type()
)
jnxSpSvcSetCpuLimitPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetCpuLimitPktDrops.setStatus("current")
_JnxSpSvcSetFlowLimitPktDrops_Type = Counter32
_JnxSpSvcSetFlowLimitPktDrops_Object = MibTableColumn
jnxSpSvcSetFlowLimitPktDrops = _JnxSpSvcSetFlowLimitPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 11),
    _JnxSpSvcSetFlowLimitPktDrops_Type()
)
jnxSpSvcSetFlowLimitPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetFlowLimitPktDrops.setStatus("current")
_JnxSpSvcSetSvcTypeTable_Object = MibTable
jnxSpSvcSetSvcTypeTable = _JnxSpSvcSetSvcTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2)
)
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypeTable.setStatus("current")
_JnxSpSvcSetSvcTypeEntry_Object = MibTableRow
jnxSpSvcSetSvcTypeEntry = _JnxSpSvcSetSvcTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1)
)
jnxSpSvcSetSvcTypeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JUNIPER-SP-MIB", "jnxSpSvcSetSvcTypeIndex"),
)
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypeEntry.setStatus("current")


class _JnxSpSvcSetSvcTypeIndex_Type(Integer32):
    """Custom type jnxSpSvcSetSvcTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxSpSvcSetSvcTypeIndex_Type.__name__ = "Integer32"
_JnxSpSvcSetSvcTypeIndex_Object = MibTableColumn
jnxSpSvcSetSvcTypeIndex = _JnxSpSvcSetSvcTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 1),
    _JnxSpSvcSetSvcTypeIndex_Type()
)
jnxSpSvcSetSvcTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypeIndex.setStatus("current")
_JnxSpSvcSetSvcTypeIfName_Type = DisplayString
_JnxSpSvcSetSvcTypeIfName_Object = MibTableColumn
jnxSpSvcSetSvcTypeIfName = _JnxSpSvcSetSvcTypeIfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 2),
    _JnxSpSvcSetSvcTypeIfName_Type()
)
jnxSpSvcSetSvcTypeIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypeIfName.setStatus("current")
_JnxSpSvcSetSvcTypeName_Type = DisplayString
_JnxSpSvcSetSvcTypeName_Object = MibTableColumn
jnxSpSvcSetSvcTypeName = _JnxSpSvcSetSvcTypeName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 3),
    _JnxSpSvcSetSvcTypeName_Type()
)
jnxSpSvcSetSvcTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypeName.setStatus("current")
_JnxSpSvcSetSvcTypeSvcSets_Type = Gauge32
_JnxSpSvcSetSvcTypeSvcSets_Object = MibTableColumn
jnxSpSvcSetSvcTypeSvcSets = _JnxSpSvcSetSvcTypeSvcSets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 4),
    _JnxSpSvcSetSvcTypeSvcSets_Type()
)
jnxSpSvcSetSvcTypeSvcSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypeSvcSets.setStatus("current")
_JnxSpSvcSetSvcTypeMemoryUsage_Type = Gauge32
_JnxSpSvcSetSvcTypeMemoryUsage_Object = MibTableColumn
jnxSpSvcSetSvcTypeMemoryUsage = _JnxSpSvcSetSvcTypeMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 5),
    _JnxSpSvcSetSvcTypeMemoryUsage_Type()
)
jnxSpSvcSetSvcTypeMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypeMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypeMemoryUsage.setUnits("bytes")
_JnxSpSvcSetSvcTypePctMemoryUsage_Type = Gauge32
_JnxSpSvcSetSvcTypePctMemoryUsage_Object = MibTableColumn
jnxSpSvcSetSvcTypePctMemoryUsage = _JnxSpSvcSetSvcTypePctMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 6),
    _JnxSpSvcSetSvcTypePctMemoryUsage_Type()
)
jnxSpSvcSetSvcTypePctMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypePctMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypePctMemoryUsage.setUnits("percent")
_JnxSpSvcSetSvcTypeCpuUtil_Type = Gauge32
_JnxSpSvcSetSvcTypeCpuUtil_Object = MibTableColumn
jnxSpSvcSetSvcTypeCpuUtil = _JnxSpSvcSetSvcTypeCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 7),
    _JnxSpSvcSetSvcTypeCpuUtil_Type()
)
jnxSpSvcSetSvcTypeCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypeCpuUtil.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypeCpuUtil.setUnits("percent")
_JnxSpSvcSetSvcTypeMemoryUsage64_Type = CounterBasedGauge64
_JnxSpSvcSetSvcTypeMemoryUsage64_Object = MibTableColumn
jnxSpSvcSetSvcTypeMemoryUsage64 = _JnxSpSvcSetSvcTypeMemoryUsage64_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 8),
    _JnxSpSvcSetSvcTypeMemoryUsage64_Type()
)
jnxSpSvcSetSvcTypeMemoryUsage64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypeMemoryUsage64.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypeMemoryUsage64.setUnits("bytes")
_JnxSpSvcSetIfTable_Object = MibTable
jnxSpSvcSetIfTable = _JnxSpSvcSetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3)
)
if mibBuilder.loadTexts:
    jnxSpSvcSetIfTable.setStatus("current")
_JnxSpSvcSetIfEntry_Object = MibTableRow
jnxSpSvcSetIfEntry = _JnxSpSvcSetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1)
)
jnxSpSvcSetIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxSpSvcSetIfEntry.setStatus("current")
_JnxSpSvcSetIfTableName_Type = DisplayString
_JnxSpSvcSetIfTableName_Object = MibTableColumn
jnxSpSvcSetIfTableName = _JnxSpSvcSetIfTableName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 1),
    _JnxSpSvcSetIfTableName_Type()
)
jnxSpSvcSetIfTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfTableName.setStatus("current")
_JnxSpSvcSetIfSvcSets_Type = Gauge32
_JnxSpSvcSetIfSvcSets_Object = MibTableColumn
jnxSpSvcSetIfSvcSets = _JnxSpSvcSetIfSvcSets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 2),
    _JnxSpSvcSetIfSvcSets_Type()
)
jnxSpSvcSetIfSvcSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfSvcSets.setStatus("current")
_JnxSpSvcSetIfMemoryUsage_Type = Gauge32
_JnxSpSvcSetIfMemoryUsage_Object = MibTableColumn
jnxSpSvcSetIfMemoryUsage = _JnxSpSvcSetIfMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 3),
    _JnxSpSvcSetIfMemoryUsage_Type()
)
jnxSpSvcSetIfMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfMemoryUsage.setUnits("bytes")
_JnxSpSvcSetIfPctMemoryUsage_Type = Gauge32
_JnxSpSvcSetIfPctMemoryUsage_Object = MibTableColumn
jnxSpSvcSetIfPctMemoryUsage = _JnxSpSvcSetIfPctMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 4),
    _JnxSpSvcSetIfPctMemoryUsage_Type()
)
jnxSpSvcSetIfPctMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfPctMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfPctMemoryUsage.setUnits("percent")
_JnxSpSvcSetIfPolMemoryUsage_Type = Gauge32
_JnxSpSvcSetIfPolMemoryUsage_Object = MibTableColumn
jnxSpSvcSetIfPolMemoryUsage = _JnxSpSvcSetIfPolMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 5),
    _JnxSpSvcSetIfPolMemoryUsage_Type()
)
jnxSpSvcSetIfPolMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfPolMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfPolMemoryUsage.setUnits("bytes")
_JnxSpSvcSetIfPctPolMemoryUsage_Type = Gauge32
_JnxSpSvcSetIfPctPolMemoryUsage_Object = MibTableColumn
jnxSpSvcSetIfPctPolMemoryUsage = _JnxSpSvcSetIfPctPolMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 6),
    _JnxSpSvcSetIfPctPolMemoryUsage_Type()
)
jnxSpSvcSetIfPctPolMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfPctPolMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfPctPolMemoryUsage.setUnits("percent")


class _JnxSpSvcSetIfMemoryZone_Type(Integer32):
    """Custom type jnxSpSvcSetIfMemoryZone based on Integer32"""
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
        *(("green", 1),
          ("orange", 3),
          ("red", 4),
          ("yellow", 2))
    )


_JnxSpSvcSetIfMemoryZone_Type.__name__ = "Integer32"
_JnxSpSvcSetIfMemoryZone_Object = MibTableColumn
jnxSpSvcSetIfMemoryZone = _JnxSpSvcSetIfMemoryZone_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 7),
    _JnxSpSvcSetIfMemoryZone_Type()
)
jnxSpSvcSetIfMemoryZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfMemoryZone.setStatus("current")
_JnxSpSvcSetIfCpuUtil_Type = Gauge32
_JnxSpSvcSetIfCpuUtil_Object = MibTableColumn
jnxSpSvcSetIfCpuUtil = _JnxSpSvcSetIfCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 8),
    _JnxSpSvcSetIfCpuUtil_Type()
)
jnxSpSvcSetIfCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfCpuUtil.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfCpuUtil.setUnits("percent")
_JnxSpSvcSetIfMemoryUsage64_Type = CounterBasedGauge64
_JnxSpSvcSetIfMemoryUsage64_Object = MibTableColumn
jnxSpSvcSetIfMemoryUsage64 = _JnxSpSvcSetIfMemoryUsage64_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 9),
    _JnxSpSvcSetIfMemoryUsage64_Type()
)
jnxSpSvcSetIfMemoryUsage64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfMemoryUsage64.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfMemoryUsage64.setUnits("bytes")
_JnxSpSvcSetIfPolMemoryUsage64_Type = CounterBasedGauge64
_JnxSpSvcSetIfPolMemoryUsage64_Object = MibTableColumn
jnxSpSvcSetIfPolMemoryUsage64 = _JnxSpSvcSetIfPolMemoryUsage64_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 10),
    _JnxSpSvcSetIfPolMemoryUsage64_Type()
)
jnxSpSvcSetIfPolMemoryUsage64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfPolMemoryUsage64.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfPolMemoryUsage64.setUnits("bytes")
_JnxFlowLimitTrapVars_ObjectIdentity = ObjectIdentity
jnxFlowLimitTrapVars = _JnxFlowLimitTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 2)
)


class _JnxSpSvcSetFlowLimitUtil_Type(Integer32):
    """Custom type jnxSpSvcSetFlowLimitUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JnxSpSvcSetFlowLimitUtil_Type.__name__ = "Integer32"
_JnxSpSvcSetFlowLimitUtil_Object = MibScalar
jnxSpSvcSetFlowLimitUtil = _JnxSpSvcSetFlowLimitUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 2, 1),
    _JnxSpSvcSetFlowLimitUtil_Type()
)
jnxSpSvcSetFlowLimitUtil.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSpSvcSetFlowLimitUtil.setStatus("current")


class _JnxSpSvcSetNameUtil_Type(DisplayString):
    """Custom type jnxSpSvcSetNameUtil based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 96),
    )


_JnxSpSvcSetNameUtil_Type.__name__ = "DisplayString"
_JnxSpSvcSetNameUtil_Object = MibScalar
jnxSpSvcSetNameUtil = _JnxSpSvcSetNameUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 2, 2),
    _JnxSpSvcSetNameUtil_Type()
)
jnxSpSvcSetNameUtil.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSpSvcSetNameUtil.setStatus("current")

# Managed Objects groups


# Notification objects

jnxSpSvcSetZoneEntered = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 0, 0, 1)
)
jnxSpSvcSetZoneEntered.setObjects(
      *(("JUNIPER-SP-MIB", "jnxSpSvcSetIfMemoryZone"),
        ("JUNIPER-SP-MIB", "jnxSpSvcSetIfTableName"))
)
if mibBuilder.loadTexts:
    jnxSpSvcSetZoneEntered.setStatus(
        "current"
    )

jnxSpSvcSetZoneExited = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 0, 0, 2)
)
jnxSpSvcSetZoneExited.setObjects(
      *(("JUNIPER-SP-MIB", "jnxSpSvcSetIfMemoryZone"),
        ("JUNIPER-SP-MIB", "jnxSpSvcSetIfTableName"))
)
if mibBuilder.loadTexts:
    jnxSpSvcSetZoneExited.setStatus(
        "current"
    )

jnxSpSvcSetCpuExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 0, 0, 3)
)
jnxSpSvcSetCpuExceeded.setObjects(
      *(("JUNIPER-SP-MIB", "jnxSpSvcSetIfCpuUtil"),
        ("JUNIPER-SP-MIB", "jnxSpSvcSetIfTableName"))
)
if mibBuilder.loadTexts:
    jnxSpSvcSetCpuExceeded.setStatus(
        "current"
    )

jnxSpSvcSetCpuOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 0, 0, 4)
)
jnxSpSvcSetCpuOk.setObjects(
      *(("JUNIPER-SP-MIB", "jnxSpSvcSetIfCpuUtil"),
        ("JUNIPER-SP-MIB", "jnxSpSvcSetIfTableName"))
)
if mibBuilder.loadTexts:
    jnxSpSvcSetCpuOk.setStatus(
        "current"
    )

jnxSpSvcSetFlowLimitUtilized = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 0, 1)
)
jnxSpSvcSetFlowLimitUtilized.setObjects(
      *(("JUNIPER-SP-MIB", "jnxSpSvcSetFlowLimitUtil"),
        ("JUNIPER-SP-MIB", "jnxSpSvcSetNameUtil"))
)
if mibBuilder.loadTexts:
    jnxSpSvcSetFlowLimitUtilized.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-SP-MIB",
    **{"jnxSpMIB": jnxSpMIB,
       "jnxSpNotifications": jnxSpNotifications,
       "jnxSpNotificationPrefix": jnxSpNotificationPrefix,
       "jnxSpSvcSetZoneEntered": jnxSpSvcSetZoneEntered,
       "jnxSpSvcSetZoneExited": jnxSpSvcSetZoneExited,
       "jnxSpSvcSetCpuExceeded": jnxSpSvcSetCpuExceeded,
       "jnxSpSvcSetCpuOk": jnxSpSvcSetCpuOk,
       "jnxSpSvcSetFlowLimitUtilized": jnxSpSvcSetFlowLimitUtilized,
       "jnxSpSvcSet": jnxSpSvcSet,
       "jnxSpSvcSetTable": jnxSpSvcSetTable,
       "jnxSpSvcSetEntry": jnxSpSvcSetEntry,
       "jnxSpSvcSetName": jnxSpSvcSetName,
       "jnxSpSvcSetSvcType": jnxSpSvcSetSvcType,
       "jnxSpSvcSetTypeIndex": jnxSpSvcSetTypeIndex,
       "jnxSpSvcSetIfName": jnxSpSvcSetIfName,
       "jnxSpSvcSetIfIndex": jnxSpSvcSetIfIndex,
       "jnxSpSvcSetMemoryUsage": jnxSpSvcSetMemoryUsage,
       "jnxSpSvcSetCpuUtil": jnxSpSvcSetCpuUtil,
       "jnxSpSvcSetSvcStyle": jnxSpSvcSetSvcStyle,
       "jnxSpSvcSetMemLimitPktDrops": jnxSpSvcSetMemLimitPktDrops,
       "jnxSpSvcSetCpuLimitPktDrops": jnxSpSvcSetCpuLimitPktDrops,
       "jnxSpSvcSetFlowLimitPktDrops": jnxSpSvcSetFlowLimitPktDrops,
       "jnxSpSvcSetSvcTypeTable": jnxSpSvcSetSvcTypeTable,
       "jnxSpSvcSetSvcTypeEntry": jnxSpSvcSetSvcTypeEntry,
       "jnxSpSvcSetSvcTypeIndex": jnxSpSvcSetSvcTypeIndex,
       "jnxSpSvcSetSvcTypeIfName": jnxSpSvcSetSvcTypeIfName,
       "jnxSpSvcSetSvcTypeName": jnxSpSvcSetSvcTypeName,
       "jnxSpSvcSetSvcTypeSvcSets": jnxSpSvcSetSvcTypeSvcSets,
       "jnxSpSvcSetSvcTypeMemoryUsage": jnxSpSvcSetSvcTypeMemoryUsage,
       "jnxSpSvcSetSvcTypePctMemoryUsage": jnxSpSvcSetSvcTypePctMemoryUsage,
       "jnxSpSvcSetSvcTypeCpuUtil": jnxSpSvcSetSvcTypeCpuUtil,
       "jnxSpSvcSetSvcTypeMemoryUsage64": jnxSpSvcSetSvcTypeMemoryUsage64,
       "jnxSpSvcSetIfTable": jnxSpSvcSetIfTable,
       "jnxSpSvcSetIfEntry": jnxSpSvcSetIfEntry,
       "jnxSpSvcSetIfTableName": jnxSpSvcSetIfTableName,
       "jnxSpSvcSetIfSvcSets": jnxSpSvcSetIfSvcSets,
       "jnxSpSvcSetIfMemoryUsage": jnxSpSvcSetIfMemoryUsage,
       "jnxSpSvcSetIfPctMemoryUsage": jnxSpSvcSetIfPctMemoryUsage,
       "jnxSpSvcSetIfPolMemoryUsage": jnxSpSvcSetIfPolMemoryUsage,
       "jnxSpSvcSetIfPctPolMemoryUsage": jnxSpSvcSetIfPctPolMemoryUsage,
       "jnxSpSvcSetIfMemoryZone": jnxSpSvcSetIfMemoryZone,
       "jnxSpSvcSetIfCpuUtil": jnxSpSvcSetIfCpuUtil,
       "jnxSpSvcSetIfMemoryUsage64": jnxSpSvcSetIfMemoryUsage64,
       "jnxSpSvcSetIfPolMemoryUsage64": jnxSpSvcSetIfPolMemoryUsage64,
       "jnxFlowLimitTrapVars": jnxFlowLimitTrapVars,
       "jnxSpSvcSetFlowLimitUtil": jnxSpSvcSetFlowLimitUtil,
       "jnxSpSvcSetNameUtil": jnxSpSvcSetNameUtil}
)
