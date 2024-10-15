# SNMP MIB module (HUAWEI-LOOPDETECT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-LOOPDETECT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:36 2024
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

(huawei,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "huawei")

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

hwLoopDetectMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 25, 180)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwDatacomm_ObjectIdentity = ObjectIdentity
hwDatacomm = _HwDatacomm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 25)
)
_HwLoopDetectCfgTable_Object = MibTable
hwLoopDetectCfgTable = _HwLoopDetectCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 25, 180, 1)
)
if mibBuilder.loadTexts:
    hwLoopDetectCfgTable.setStatus("current")
_HwLoopDetectCfgEntry_Object = MibTableRow
hwLoopDetectCfgEntry = _HwLoopDetectCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 25, 180, 1, 1)
)
hwLoopDetectCfgEntry.setIndexNames(
    (0, "HUAWEI-LOOPDETECT-MIB", "hwLoopDetectCfgPortIndex"),
)
if mibBuilder.loadTexts:
    hwLoopDetectCfgEntry.setStatus("current")


class _HwLoopDetectCfgPortIndex_Type(Integer32):
    """Custom type hwLoopDetectCfgPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwLoopDetectCfgPortIndex_Type.__name__ = "Integer32"
_HwLoopDetectCfgPortIndex_Object = MibTableColumn
hwLoopDetectCfgPortIndex = _HwLoopDetectCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 25, 180, 1, 1, 1),
    _HwLoopDetectCfgPortIndex_Type()
)
hwLoopDetectCfgPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwLoopDetectCfgPortIndex.setStatus("current")


class _HwLoopDetectCfgPortName_Type(OctetString):
    """Custom type hwLoopDetectCfgPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HwLoopDetectCfgPortName_Type.__name__ = "OctetString"
_HwLoopDetectCfgPortName_Object = MibTableColumn
hwLoopDetectCfgPortName = _HwLoopDetectCfgPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 25, 180, 1, 1, 2),
    _HwLoopDetectCfgPortName_Type()
)
hwLoopDetectCfgPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLoopDetectCfgPortName.setStatus("current")
_HwLoopDetectCfg_Type = Integer32
_HwLoopDetectCfg_Object = MibTableColumn
hwLoopDetectCfg = _HwLoopDetectCfg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 25, 180, 1, 1, 3),
    _HwLoopDetectCfg_Type()
)
hwLoopDetectCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLoopDetectCfg.setStatus("current")
_HwLoopDetectCfgBlock_Type = Integer32
_HwLoopDetectCfgBlock_Object = MibTableColumn
hwLoopDetectCfgBlock = _HwLoopDetectCfgBlock_Object(
    (1, 3, 6, 1, 4, 1, 2011, 25, 180, 1, 1, 4),
    _HwLoopDetectCfgBlock_Type()
)
hwLoopDetectCfgBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLoopDetectCfgBlock.setStatus("current")
_HwLoopDetectCfgBlockTime_Type = Integer32
_HwLoopDetectCfgBlockTime_Object = MibTableColumn
hwLoopDetectCfgBlockTime = _HwLoopDetectCfgBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 25, 180, 1, 1, 5),
    _HwLoopDetectCfgBlockTime_Type()
)
hwLoopDetectCfgBlockTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLoopDetectCfgBlockTime.setStatus("current")
_HwLoopDetectCfgPriority_Type = Integer32
_HwLoopDetectCfgPriority_Object = MibTableColumn
hwLoopDetectCfgPriority = _HwLoopDetectCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 25, 180, 1, 1, 6),
    _HwLoopDetectCfgPriority_Type()
)
hwLoopDetectCfgPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLoopDetectCfgPriority.setStatus("current")
_HwLoopDetectCfgTrigger_Type = Integer32
_HwLoopDetectCfgTrigger_Object = MibTableColumn
hwLoopDetectCfgTrigger = _HwLoopDetectCfgTrigger_Object(
    (1, 3, 6, 1, 4, 1, 2011, 25, 180, 1, 1, 7),
    _HwLoopDetectCfgTrigger_Type()
)
hwLoopDetectCfgTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLoopDetectCfgTrigger.setStatus("current")
_HwLoopDetectCfgSta_Type = Integer32
_HwLoopDetectCfgSta_Object = MibTableColumn
hwLoopDetectCfgSta = _HwLoopDetectCfgSta_Object(
    (1, 3, 6, 1, 4, 1, 2011, 25, 180, 1, 1, 8),
    _HwLoopDetectCfgSta_Type()
)
hwLoopDetectCfgSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLoopDetectCfgSta.setStatus("current")
_HwLoopDetectTraps_ObjectIdentity = ObjectIdentity
hwLoopDetectTraps = _HwLoopDetectTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 25, 180, 2)
)
_HwLoopDetectGroups_ObjectIdentity = ObjectIdentity
hwLoopDetectGroups = _HwLoopDetectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 25, 180, 3)
)

# Managed Objects groups

hwLoopDetectCfgEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 25, 180, 3, 1)
)
hwLoopDetectCfgEntryGroup.setObjects(
      *(("HUAWEI-LOOPDETECT-MIB", "hwLoopDetectCfgPortName"),
        ("HUAWEI-LOOPDETECT-MIB", "hwLoopDetectCfg"),
        ("HUAWEI-LOOPDETECT-MIB", "hwLoopDetectCfgBlock"),
        ("HUAWEI-LOOPDETECT-MIB", "hwLoopDetectCfgBlockTime"),
        ("HUAWEI-LOOPDETECT-MIB", "hwLoopDetectCfgPriority"),
        ("HUAWEI-LOOPDETECT-MIB", "hwLoopDetectCfgTrigger"),
        ("HUAWEI-LOOPDETECT-MIB", "hwLoopDetectCfgSta"))
)
if mibBuilder.loadTexts:
    hwLoopDetectCfgEntryGroup.setStatus("current")


# Notification objects

hwLoopDetectEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 25, 180, 2, 1)
)
hwLoopDetectEnabled.setObjects(
    ("HUAWEI-LOOPDETECT-MIB", "hwLoopDetectCfgPortName")
)
if mibBuilder.loadTexts:
    hwLoopDetectEnabled.setStatus(
        "current"
    )

hwLoopDetectDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 25, 180, 2, 2)
)
hwLoopDetectDisabled.setObjects(
    ("HUAWEI-LOOPDETECT-MIB", "hwLoopDetectCfgPortName")
)
if mibBuilder.loadTexts:
    hwLoopDetectDisabled.setStatus(
        "current"
    )

hwLoopDetectBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 25, 180, 2, 3)
)
hwLoopDetectBlocked.setObjects(
    ("HUAWEI-LOOPDETECT-MIB", "hwLoopDetectCfgPortName")
)
if mibBuilder.loadTexts:
    hwLoopDetectBlocked.setStatus(
        "current"
    )

hwLoopDetectUnBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 25, 180, 2, 4)
)
hwLoopDetectUnBlocked.setObjects(
    ("HUAWEI-LOOPDETECT-MIB", "hwLoopDetectCfgPortName")
)
if mibBuilder.loadTexts:
    hwLoopDetectUnBlocked.setStatus(
        "current"
    )


# Notifications groups

hwLoopDetectTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 25, 180, 3, 2)
)
hwLoopDetectTrapsGroup.setObjects(
      *(("HUAWEI-LOOPDETECT-MIB", "hwLoopDetectEnabled"),
        ("HUAWEI-LOOPDETECT-MIB", "hwLoopDetectDisabled"),
        ("HUAWEI-LOOPDETECT-MIB", "hwLoopDetectBlocked"),
        ("HUAWEI-LOOPDETECT-MIB", "hwLoopDetectUnBlocked"))
)
if mibBuilder.loadTexts:
    hwLoopDetectTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-LOOPDETECT-MIB",
    **{"hwDatacomm": hwDatacomm,
       "hwLoopDetectMIB": hwLoopDetectMIB,
       "hwLoopDetectCfgTable": hwLoopDetectCfgTable,
       "hwLoopDetectCfgEntry": hwLoopDetectCfgEntry,
       "hwLoopDetectCfgPortIndex": hwLoopDetectCfgPortIndex,
       "hwLoopDetectCfgPortName": hwLoopDetectCfgPortName,
       "hwLoopDetectCfg": hwLoopDetectCfg,
       "hwLoopDetectCfgBlock": hwLoopDetectCfgBlock,
       "hwLoopDetectCfgBlockTime": hwLoopDetectCfgBlockTime,
       "hwLoopDetectCfgPriority": hwLoopDetectCfgPriority,
       "hwLoopDetectCfgTrigger": hwLoopDetectCfgTrigger,
       "hwLoopDetectCfgSta": hwLoopDetectCfgSta,
       "hwLoopDetectTraps": hwLoopDetectTraps,
       "hwLoopDetectEnabled": hwLoopDetectEnabled,
       "hwLoopDetectDisabled": hwLoopDetectDisabled,
       "hwLoopDetectBlocked": hwLoopDetectBlocked,
       "hwLoopDetectUnBlocked": hwLoopDetectUnBlocked,
       "hwLoopDetectGroups": hwLoopDetectGroups,
       "hwLoopDetectCfgEntryGroup": hwLoopDetectCfgEntryGroup,
       "hwLoopDetectTrapsGroup": hwLoopDetectTrapsGroup}
)
