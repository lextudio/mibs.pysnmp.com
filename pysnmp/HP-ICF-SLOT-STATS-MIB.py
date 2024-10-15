# SNMP MIB module (HP-ICF-SLOT-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-SLOT-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:10 2024
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

(hpSwitchStatistics,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitchStatistics")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hpicfSlotStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20)
)
hpicfSlotStatsMIB.setRevisions(
        ("2012-01-05 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfSlotStatsObjects_ObjectIdentity = ObjectIdentity
hpicfSlotStatsObjects = _HpicfSlotStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1)
)
_HpicfSlotStatsModuleCpuStatTable_Object = MibTable
hpicfSlotStatsModuleCpuStatTable = _HpicfSlotStatsModuleCpuStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfSlotStatsModuleCpuStatTable.setStatus("current")
_HpicfSlotStatsModuleCpuStatEntry_Object = MibTableRow
hpicfSlotStatsModuleCpuStatEntry = _HpicfSlotStatsModuleCpuStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 1, 1)
)
hpicfSlotStatsModuleCpuStatEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpicfSlotStatsModuleCpuStatEntry.setStatus("current")
_HpicfSlotStatsModuleHwModel_Type = SnmpAdminString
_HpicfSlotStatsModuleHwModel_Object = MibTableColumn
hpicfSlotStatsModuleHwModel = _HpicfSlotStatsModuleHwModel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 1, 1, 1),
    _HpicfSlotStatsModuleHwModel_Type()
)
hpicfSlotStatsModuleHwModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSlotStatsModuleHwModel.setStatus("current")
_HpicfSlotStatsModuleSerialNum_Type = SnmpAdminString
_HpicfSlotStatsModuleSerialNum_Object = MibTableColumn
hpicfSlotStatsModuleSerialNum = _HpicfSlotStatsModuleSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 1, 1, 2),
    _HpicfSlotStatsModuleSerialNum_Type()
)
hpicfSlotStatsModuleSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSlotStatsModuleSerialNum.setStatus("current")


class _HpicfSlotStatsModuleCpuStatCurrentPercent_Type(Integer32):
    """Custom type hpicfSlotStatsModuleCpuStatCurrentPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpicfSlotStatsModuleCpuStatCurrentPercent_Type.__name__ = "Integer32"
_HpicfSlotStatsModuleCpuStatCurrentPercent_Object = MibTableColumn
hpicfSlotStatsModuleCpuStatCurrentPercent = _HpicfSlotStatsModuleCpuStatCurrentPercent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 1, 1, 3),
    _HpicfSlotStatsModuleCpuStatCurrentPercent_Type()
)
hpicfSlotStatsModuleCpuStatCurrentPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSlotStatsModuleCpuStatCurrentPercent.setStatus("current")


class _HpicfSlotStatsModuleCpuStatAveragePercent_Type(Integer32):
    """Custom type hpicfSlotStatsModuleCpuStatAveragePercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpicfSlotStatsModuleCpuStatAveragePercent_Type.__name__ = "Integer32"
_HpicfSlotStatsModuleCpuStatAveragePercent_Object = MibTableColumn
hpicfSlotStatsModuleCpuStatAveragePercent = _HpicfSlotStatsModuleCpuStatAveragePercent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 1, 1, 4),
    _HpicfSlotStatsModuleCpuStatAveragePercent_Type()
)
hpicfSlotStatsModuleCpuStatAveragePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSlotStatsModuleCpuStatAveragePercent.setStatus("current")
_HpicfSlotStatsModuleCpuStatUpdateFrequency_Type = Integer32
_HpicfSlotStatsModuleCpuStatUpdateFrequency_Object = MibScalar
hpicfSlotStatsModuleCpuStatUpdateFrequency = _HpicfSlotStatsModuleCpuStatUpdateFrequency_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 2),
    _HpicfSlotStatsModuleCpuStatUpdateFrequency_Type()
)
hpicfSlotStatsModuleCpuStatUpdateFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSlotStatsModuleCpuStatUpdateFrequency.setStatus("current")
_HpicfSlotStatsConformance_ObjectIdentity = ObjectIdentity
hpicfSlotStatsConformance = _HpicfSlotStatsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 2)
)
_HpicfSlotStatsGroups_ObjectIdentity = ObjectIdentity
hpicfSlotStatsGroups = _HpicfSlotStatsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 2, 1)
)
_HpicfSlotStatsCompliances_ObjectIdentity = ObjectIdentity
hpicfSlotStatsCompliances = _HpicfSlotStatsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 2, 2)
)

# Managed Objects groups

hpicfSlotStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 2, 1, 1)
)
hpicfSlotStatsGroup.setObjects(
      *(("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsModuleHwModel"),
        ("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsModuleSerialNum"),
        ("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsModuleCpuStatCurrentPercent"),
        ("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsModuleCpuStatAveragePercent"),
        ("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsModuleCpuStatUpdateFrequency"))
)
if mibBuilder.loadTexts:
    hpicfSlotStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfSlotStatsFullCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfSlotStatsFullCompliance1.setStatus(
        "current"
    )

hpicfModuleSlotStatsReadOnlyCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfModuleSlotStatsReadOnlyCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-SLOT-STATS-MIB",
    **{"hpicfSlotStatsMIB": hpicfSlotStatsMIB,
       "hpicfSlotStatsObjects": hpicfSlotStatsObjects,
       "hpicfSlotStatsModuleCpuStatTable": hpicfSlotStatsModuleCpuStatTable,
       "hpicfSlotStatsModuleCpuStatEntry": hpicfSlotStatsModuleCpuStatEntry,
       "hpicfSlotStatsModuleHwModel": hpicfSlotStatsModuleHwModel,
       "hpicfSlotStatsModuleSerialNum": hpicfSlotStatsModuleSerialNum,
       "hpicfSlotStatsModuleCpuStatCurrentPercent": hpicfSlotStatsModuleCpuStatCurrentPercent,
       "hpicfSlotStatsModuleCpuStatAveragePercent": hpicfSlotStatsModuleCpuStatAveragePercent,
       "hpicfSlotStatsModuleCpuStatUpdateFrequency": hpicfSlotStatsModuleCpuStatUpdateFrequency,
       "hpicfSlotStatsConformance": hpicfSlotStatsConformance,
       "hpicfSlotStatsGroups": hpicfSlotStatsGroups,
       "hpicfSlotStatsGroup": hpicfSlotStatsGroup,
       "hpicfSlotStatsCompliances": hpicfSlotStatsCompliances,
       "hpicfSlotStatsFullCompliance1": hpicfSlotStatsFullCompliance1,
       "hpicfModuleSlotStatsReadOnlyCompliance1": hpicfModuleSlotStatsReadOnlyCompliance1}
)
