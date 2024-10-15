# SNMP MIB module (CISCO-6400-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-6400-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:20 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cisco6400ChassisMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 27)
)
cisco6400ChassisMIB.setRevisions(
        ("2001-10-22 00:00",
         "2001-05-10 12:34",
         "2000-09-25 12:34",
         "1999-03-22 00:00",
         "1998-08-05 00:00",
         "1997-12-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class APSEventStatus(Integer32, TextualConvention):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("adminDown", 8),
          ("doNotRevert", 3),
          ("forceSwitch", 6),
          ("good", 1),
          ("lockOut", 7),
          ("manualSwitch", 4),
          ("noHardware", 2),
          ("signgalDegrade", 5))
    )



# MIB Managed Objects in the order of their OIDs

_Cisco6400ChassisMIBObjects_ObjectIdentity = ObjectIdentity
cisco6400ChassisMIBObjects = _Cisco6400ChassisMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1)
)
_C64RedundantGroup_ObjectIdentity = ObjectIdentity
c64RedundantGroup = _C64RedundantGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1)
)


class _C64MainCPUConfigAutoSync_Type(Integer32):
    """Custom type c64MainCPUConfigAutoSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_C64MainCPUConfigAutoSync_Type.__name__ = "Integer32"
_C64MainCPUConfigAutoSync_Object = MibScalar
c64MainCPUConfigAutoSync = _C64MainCPUConfigAutoSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 1),
    _C64MainCPUConfigAutoSync_Type()
)
c64MainCPUConfigAutoSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c64MainCPUConfigAutoSync.setStatus("current")


class _C64MainCPUSwitchOver_Type(Integer32):
    """Custom type c64MainCPUSwitchOver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceOver", 2),
          ("ok", 1))
    )


_C64MainCPUSwitchOver_Type.__name__ = "Integer32"
_C64MainCPUSwitchOver_Object = MibScalar
c64MainCPUSwitchOver = _C64MainCPUSwitchOver_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 2),
    _C64MainCPUSwitchOver_Type()
)
c64MainCPUSwitchOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c64MainCPUSwitchOver.setStatus("current")
_C64SlotConfigTable_Object = MibTable
c64SlotConfigTable = _C64SlotConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3)
)
if mibBuilder.loadTexts:
    c64SlotConfigTable.setStatus("current")
_C64SlotConfigEntry_Object = MibTableRow
c64SlotConfigEntry = _C64SlotConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3, 1)
)
c64SlotConfigEntry.setIndexNames(
    (0, "CISCO-6400-CHASSIS-MIB", "c64SlotConfigModule1Index"),
    (0, "CISCO-6400-CHASSIS-MIB", "c64SlotConfigModule2Index"),
)
if mibBuilder.loadTexts:
    c64SlotConfigEntry.setStatus("current")


class _C64SlotConfigModule1Index_Type(Integer32):
    """Custom type c64SlotConfigModule1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_C64SlotConfigModule1Index_Type.__name__ = "Integer32"
_C64SlotConfigModule1Index_Object = MibTableColumn
c64SlotConfigModule1Index = _C64SlotConfigModule1Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3, 1, 1),
    _C64SlotConfigModule1Index_Type()
)
c64SlotConfigModule1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c64SlotConfigModule1Index.setStatus("current")


class _C64SlotConfigModule2Index_Type(Integer32):
    """Custom type c64SlotConfigModule2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_C64SlotConfigModule2Index_Type.__name__ = "Integer32"
_C64SlotConfigModule2Index_Object = MibTableColumn
c64SlotConfigModule2Index = _C64SlotConfigModule2Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3, 1, 2),
    _C64SlotConfigModule2Index_Type()
)
c64SlotConfigModule2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c64SlotConfigModule2Index.setStatus("current")
_C64Slot1Name_Type = DisplayString
_C64Slot1Name_Object = MibTableColumn
c64Slot1Name = _C64Slot1Name_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3, 1, 3),
    _C64Slot1Name_Type()
)
c64Slot1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64Slot1Name.setStatus("current")
_C64Slot2Name_Type = DisplayString
_C64Slot2Name_Object = MibTableColumn
c64Slot2Name = _C64Slot2Name_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3, 1, 4),
    _C64Slot2Name_Type()
)
c64Slot2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64Slot2Name.setStatus("current")


class _C64SlotConfigPrefIndex_Type(Integer32):
    """Custom type c64SlotConfigPrefIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primarySlot", 1),
          ("secondarySlot", 2))
    )


_C64SlotConfigPrefIndex_Type.__name__ = "Integer32"
_C64SlotConfigPrefIndex_Object = MibTableColumn
c64SlotConfigPrefIndex = _C64SlotConfigPrefIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3, 1, 5),
    _C64SlotConfigPrefIndex_Type()
)
c64SlotConfigPrefIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c64SlotConfigPrefIndex.setStatus("deprecated")


class _C64SlotSwitchOver_Type(Integer32):
    """Custom type c64SlotSwitchOver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceOver", 2),
          ("ok", 1))
    )


_C64SlotSwitchOver_Type.__name__ = "Integer32"
_C64SlotSwitchOver_Object = MibTableColumn
c64SlotSwitchOver = _C64SlotSwitchOver_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3, 1, 6),
    _C64SlotSwitchOver_Type()
)
c64SlotSwitchOver.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c64SlotSwitchOver.setStatus("current")
_C64SlotConfigStatus_Type = RowStatus
_C64SlotConfigStatus_Object = MibTableColumn
c64SlotConfigStatus = _C64SlotConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3, 1, 7),
    _C64SlotConfigStatus_Type()
)
c64SlotConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c64SlotConfigStatus.setStatus("current")
_C64SubSlotConfigTable_Object = MibTable
c64SubSlotConfigTable = _C64SubSlotConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5)
)
if mibBuilder.loadTexts:
    c64SubSlotConfigTable.setStatus("current")
_C64SubSlotConfigEntry_Object = MibTableRow
c64SubSlotConfigEntry = _C64SubSlotConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1)
)
c64SubSlotConfigEntry.setIndexNames(
    (0, "CISCO-6400-CHASSIS-MIB", "c64SubSlotConfigModule1Index"),
    (0, "CISCO-6400-CHASSIS-MIB", "c64SubSlotConfigSubModule1Index"),
    (0, "CISCO-6400-CHASSIS-MIB", "c64SubSlotConfigModule2Index"),
    (0, "CISCO-6400-CHASSIS-MIB", "c64SubSlotConfigSubModule2Index"),
    (0, "CISCO-6400-CHASSIS-MIB", "c64SubSlotRedundantIndex"),
)
if mibBuilder.loadTexts:
    c64SubSlotConfigEntry.setStatus("current")


class _C64SubSlotRedundantIndex_Type(Integer32):
    """Custom type c64SubSlotRedundantIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_C64SubSlotRedundantIndex_Type.__name__ = "Integer32"
_C64SubSlotRedundantIndex_Object = MibTableColumn
c64SubSlotRedundantIndex = _C64SubSlotRedundantIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 1),
    _C64SubSlotRedundantIndex_Type()
)
c64SubSlotRedundantIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c64SubSlotRedundantIndex.setStatus("current")


class _C64SubSlotConfigModule1Index_Type(Integer32):
    """Custom type c64SubSlotConfigModule1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_C64SubSlotConfigModule1Index_Type.__name__ = "Integer32"
_C64SubSlotConfigModule1Index_Object = MibTableColumn
c64SubSlotConfigModule1Index = _C64SubSlotConfigModule1Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 2),
    _C64SubSlotConfigModule1Index_Type()
)
c64SubSlotConfigModule1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c64SubSlotConfigModule1Index.setStatus("current")


class _C64SubSlotConfigSubModule1Index_Type(Integer32):
    """Custom type c64SubSlotConfigSubModule1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_C64SubSlotConfigSubModule1Index_Type.__name__ = "Integer32"
_C64SubSlotConfigSubModule1Index_Object = MibTableColumn
c64SubSlotConfigSubModule1Index = _C64SubSlotConfigSubModule1Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 3),
    _C64SubSlotConfigSubModule1Index_Type()
)
c64SubSlotConfigSubModule1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c64SubSlotConfigSubModule1Index.setStatus("current")


class _C64SubSlotConfigModule2Index_Type(Integer32):
    """Custom type c64SubSlotConfigModule2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_C64SubSlotConfigModule2Index_Type.__name__ = "Integer32"
_C64SubSlotConfigModule2Index_Object = MibTableColumn
c64SubSlotConfigModule2Index = _C64SubSlotConfigModule2Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 4),
    _C64SubSlotConfigModule2Index_Type()
)
c64SubSlotConfigModule2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c64SubSlotConfigModule2Index.setStatus("current")


class _C64SubSlotConfigSubModule2Index_Type(Integer32):
    """Custom type c64SubSlotConfigSubModule2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_C64SubSlotConfigSubModule2Index_Type.__name__ = "Integer32"
_C64SubSlotConfigSubModule2Index_Object = MibTableColumn
c64SubSlotConfigSubModule2Index = _C64SubSlotConfigSubModule2Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 5),
    _C64SubSlotConfigSubModule2Index_Type()
)
c64SubSlotConfigSubModule2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c64SubSlotConfigSubModule2Index.setStatus("current")
_C64SubSlot1Name_Type = DisplayString
_C64SubSlot1Name_Object = MibTableColumn
c64SubSlot1Name = _C64SubSlot1Name_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 6),
    _C64SubSlot1Name_Type()
)
c64SubSlot1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64SubSlot1Name.setStatus("current")
_C64SubSlot2Name_Type = DisplayString
_C64SubSlot2Name_Object = MibTableColumn
c64SubSlot2Name = _C64SubSlot2Name_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 7),
    _C64SubSlot2Name_Type()
)
c64SubSlot2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64SubSlot2Name.setStatus("current")


class _C64SubSlotConfigPrefIndex_Type(Integer32):
    """Custom type c64SubSlotConfigPrefIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primarySubslot", 1),
          ("secondarySubslot", 2))
    )


_C64SubSlotConfigPrefIndex_Type.__name__ = "Integer32"
_C64SubSlotConfigPrefIndex_Object = MibTableColumn
c64SubSlotConfigPrefIndex = _C64SubSlotConfigPrefIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 8),
    _C64SubSlotConfigPrefIndex_Type()
)
c64SubSlotConfigPrefIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c64SubSlotConfigPrefIndex.setStatus("deprecated")


class _C64SubSlotSwitchOver_Type(Integer32):
    """Custom type c64SubSlotSwitchOver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceOver", 2),
          ("ok", 1))
    )


_C64SubSlotSwitchOver_Type.__name__ = "Integer32"
_C64SubSlotSwitchOver_Object = MibTableColumn
c64SubSlotSwitchOver = _C64SubSlotSwitchOver_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 9),
    _C64SubSlotSwitchOver_Type()
)
c64SubSlotSwitchOver.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c64SubSlotSwitchOver.setStatus("current")
_C64SubSlotConfigStatus_Type = RowStatus
_C64SubSlotConfigStatus_Object = MibTableColumn
c64SubSlotConfigStatus = _C64SubSlotConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 10),
    _C64SubSlotConfigStatus_Type()
)
c64SubSlotConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c64SubSlotConfigStatus.setStatus("current")
_C64PortConfigTable_Object = MibTable
c64PortConfigTable = _C64PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6)
)
if mibBuilder.loadTexts:
    c64PortConfigTable.setStatus("current")
_C64PortConfigEntry_Object = MibTableRow
c64PortConfigEntry = _C64PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1)
)
c64PortConfigEntry.setIndexNames(
    (0, "CISCO-6400-CHASSIS-MIB", "c64PortConfigModule1Index"),
    (0, "CISCO-6400-CHASSIS-MIB", "c64PortConfigSubModule1Index"),
    (0, "CISCO-6400-CHASSIS-MIB", "c64PortConfigPort1Index"),
    (0, "CISCO-6400-CHASSIS-MIB", "c64PortConfigModule2Index"),
    (0, "CISCO-6400-CHASSIS-MIB", "c64PortConfigSubModule2Index"),
    (0, "CISCO-6400-CHASSIS-MIB", "c64PortConfigPort2Index"),
    (0, "CISCO-6400-CHASSIS-MIB", "c64SubSlotRedundantIndex"),
)
if mibBuilder.loadTexts:
    c64PortConfigEntry.setStatus("current")


class _C64PortConfigModule1Index_Type(Integer32):
    """Custom type c64PortConfigModule1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_C64PortConfigModule1Index_Type.__name__ = "Integer32"
_C64PortConfigModule1Index_Object = MibTableColumn
c64PortConfigModule1Index = _C64PortConfigModule1Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 1),
    _C64PortConfigModule1Index_Type()
)
c64PortConfigModule1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c64PortConfigModule1Index.setStatus("current")


class _C64PortConfigSubModule1Index_Type(Integer32):
    """Custom type c64PortConfigSubModule1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_C64PortConfigSubModule1Index_Type.__name__ = "Integer32"
_C64PortConfigSubModule1Index_Object = MibTableColumn
c64PortConfigSubModule1Index = _C64PortConfigSubModule1Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 2),
    _C64PortConfigSubModule1Index_Type()
)
c64PortConfigSubModule1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c64PortConfigSubModule1Index.setStatus("current")


class _C64PortConfigPort1Index_Type(Integer32):
    """Custom type c64PortConfigPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_C64PortConfigPort1Index_Type.__name__ = "Integer32"
_C64PortConfigPort1Index_Object = MibTableColumn
c64PortConfigPort1Index = _C64PortConfigPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 3),
    _C64PortConfigPort1Index_Type()
)
c64PortConfigPort1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c64PortConfigPort1Index.setStatus("current")


class _C64PortConfigModule2Index_Type(Integer32):
    """Custom type c64PortConfigModule2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_C64PortConfigModule2Index_Type.__name__ = "Integer32"
_C64PortConfigModule2Index_Object = MibTableColumn
c64PortConfigModule2Index = _C64PortConfigModule2Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 4),
    _C64PortConfigModule2Index_Type()
)
c64PortConfigModule2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c64PortConfigModule2Index.setStatus("current")


class _C64PortConfigSubModule2Index_Type(Integer32):
    """Custom type c64PortConfigSubModule2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_C64PortConfigSubModule2Index_Type.__name__ = "Integer32"
_C64PortConfigSubModule2Index_Object = MibTableColumn
c64PortConfigSubModule2Index = _C64PortConfigSubModule2Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 5),
    _C64PortConfigSubModule2Index_Type()
)
c64PortConfigSubModule2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c64PortConfigSubModule2Index.setStatus("current")


class _C64PortConfigPort2Index_Type(Integer32):
    """Custom type c64PortConfigPort2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_C64PortConfigPort2Index_Type.__name__ = "Integer32"
_C64PortConfigPort2Index_Object = MibTableColumn
c64PortConfigPort2Index = _C64PortConfigPort2Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 6),
    _C64PortConfigPort2Index_Type()
)
c64PortConfigPort2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c64PortConfigPort2Index.setStatus("current")
_C64Port1Name_Type = DisplayString
_C64Port1Name_Object = MibTableColumn
c64Port1Name = _C64Port1Name_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 7),
    _C64Port1Name_Type()
)
c64Port1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64Port1Name.setStatus("current")
_C64Port2Name_Type = DisplayString
_C64Port2Name_Object = MibTableColumn
c64Port2Name = _C64Port2Name_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 8),
    _C64Port2Name_Type()
)
c64Port2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64Port2Name.setStatus("current")


class _C64PortConfigPrefIndex_Type(Integer32):
    """Custom type c64PortConfigPrefIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primaryPort", 1),
          ("secondaryPort", 2))
    )


_C64PortConfigPrefIndex_Type.__name__ = "Integer32"
_C64PortConfigPrefIndex_Object = MibTableColumn
c64PortConfigPrefIndex = _C64PortConfigPrefIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 9),
    _C64PortConfigPrefIndex_Type()
)
c64PortConfigPrefIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c64PortConfigPrefIndex.setStatus("current")


class _C64PortSwitchOver_Type(Integer32):
    """Custom type c64PortSwitchOver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceOver", 2),
          ("ok", 1))
    )


_C64PortSwitchOver_Type.__name__ = "Integer32"
_C64PortSwitchOver_Object = MibTableColumn
c64PortSwitchOver = _C64PortSwitchOver_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 10),
    _C64PortSwitchOver_Type()
)
c64PortSwitchOver.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c64PortSwitchOver.setStatus("current")
_C64PortConfigStatus_Type = RowStatus
_C64PortConfigStatus_Object = MibTableColumn
c64PortConfigStatus = _C64PortConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 11),
    _C64PortConfigStatus_Type()
)
c64PortConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c64PortConfigStatus.setStatus("current")
_C64SonetAPSConfigTable_Object = MibTable
c64SonetAPSConfigTable = _C64SonetAPSConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 7)
)
if mibBuilder.loadTexts:
    c64SonetAPSConfigTable.setStatus("current")
_C64SonetAPSConfigEntry_Object = MibTableRow
c64SonetAPSConfigEntry = _C64SonetAPSConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 7, 1)
)
c64SonetAPSConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    c64SonetAPSConfigEntry.setStatus("current")


class _C64SonetAPSMode_Type(Integer32):
    """Custom type c64SonetAPSMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("linear", 1),
          ("yCable", 2))
    )


_C64SonetAPSMode_Type.__name__ = "Integer32"
_C64SonetAPSMode_Object = MibTableColumn
c64SonetAPSMode = _C64SonetAPSMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 7, 1, 1),
    _C64SonetAPSMode_Type()
)
c64SonetAPSMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c64SonetAPSMode.setStatus("current")


class _C64SonetAPSBERThreshold_Type(Integer32):
    """Custom type c64SonetAPSBERThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150000),
    )


_C64SonetAPSBERThreshold_Type.__name__ = "Integer32"
_C64SonetAPSBERThreshold_Object = MibTableColumn
c64SonetAPSBERThreshold = _C64SonetAPSBERThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 7, 1, 2),
    _C64SonetAPSBERThreshold_Type()
)
c64SonetAPSBERThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c64SonetAPSBERThreshold.setStatus("current")


class _C64SonetAPSSwitchCmd_Type(Integer32):
    """Custom type c64SonetAPSSwitchCmd based on Integer32"""
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
        *(("clear", 6),
          ("forceProtect", 3),
          ("forceWorking", 2),
          ("lockOut", 1),
          ("manualProtect", 5),
          ("manualWorking", 4))
    )


_C64SonetAPSSwitchCmd_Type.__name__ = "Integer32"
_C64SonetAPSSwitchCmd_Object = MibTableColumn
c64SonetAPSSwitchCmd = _C64SonetAPSSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 7, 1, 3),
    _C64SonetAPSSwitchCmd_Type()
)
c64SonetAPSSwitchCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c64SonetAPSSwitchCmd.setStatus("current")


class _C64SonetAPSSFBERThreshold_Type(Integer32):
    """Custom type c64SonetAPSSFBERThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 5),
    )


_C64SonetAPSSFBERThreshold_Type.__name__ = "Integer32"
_C64SonetAPSSFBERThreshold_Object = MibTableColumn
c64SonetAPSSFBERThreshold = _C64SonetAPSSFBERThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 7, 1, 4),
    _C64SonetAPSSFBERThreshold_Type()
)
c64SonetAPSSFBERThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c64SonetAPSSFBERThreshold.setStatus("current")
_C64SonetAPSStatsTable_Object = MibTable
c64SonetAPSStatsTable = _C64SonetAPSStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8)
)
if mibBuilder.loadTexts:
    c64SonetAPSStatsTable.setStatus("current")
_C64SonetAPSStatsEntry_Object = MibTableRow
c64SonetAPSStatsEntry = _C64SonetAPSStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1)
)
c64SonetAPSStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    c64SonetAPSStatsEntry.setStatus("current")


class _C64SonetAPSWorkSectionStatus_Type(Integer32):
    """Custom type c64SonetAPSWorkSectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_C64SonetAPSWorkSectionStatus_Type.__name__ = "Integer32"
_C64SonetAPSWorkSectionStatus_Object = MibTableColumn
c64SonetAPSWorkSectionStatus = _C64SonetAPSWorkSectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 1),
    _C64SonetAPSWorkSectionStatus_Type()
)
c64SonetAPSWorkSectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64SonetAPSWorkSectionStatus.setStatus("current")


class _C64SonetAPSWorkLineStatus_Type(Integer32):
    """Custom type c64SonetAPSWorkLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_C64SonetAPSWorkLineStatus_Type.__name__ = "Integer32"
_C64SonetAPSWorkLineStatus_Object = MibTableColumn
c64SonetAPSWorkLineStatus = _C64SonetAPSWorkLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 2),
    _C64SonetAPSWorkLineStatus_Type()
)
c64SonetAPSWorkLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64SonetAPSWorkLineStatus.setStatus("current")


class _C64SonetAPSWorkPathStatus_Type(Integer32):
    """Custom type c64SonetAPSWorkPathStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_C64SonetAPSWorkPathStatus_Type.__name__ = "Integer32"
_C64SonetAPSWorkPathStatus_Object = MibTableColumn
c64SonetAPSWorkPathStatus = _C64SonetAPSWorkPathStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 3),
    _C64SonetAPSWorkPathStatus_Type()
)
c64SonetAPSWorkPathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64SonetAPSWorkPathStatus.setStatus("current")
_C64SonetAPSWorkSectionBIPE_Type = Counter32
_C64SonetAPSWorkSectionBIPE_Object = MibTableColumn
c64SonetAPSWorkSectionBIPE = _C64SonetAPSWorkSectionBIPE_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 4),
    _C64SonetAPSWorkSectionBIPE_Type()
)
c64SonetAPSWorkSectionBIPE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64SonetAPSWorkSectionBIPE.setStatus("current")
_C64SonetAPSWorkLineBIPE_Type = Counter32
_C64SonetAPSWorkLineBIPE_Object = MibTableColumn
c64SonetAPSWorkLineBIPE = _C64SonetAPSWorkLineBIPE_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 5),
    _C64SonetAPSWorkLineBIPE_Type()
)
c64SonetAPSWorkLineBIPE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64SonetAPSWorkLineBIPE.setStatus("current")
_C64SonetAPSWorkLineFEBE_Type = Counter32
_C64SonetAPSWorkLineFEBE_Object = MibTableColumn
c64SonetAPSWorkLineFEBE = _C64SonetAPSWorkLineFEBE_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 6),
    _C64SonetAPSWorkLineFEBE_Type()
)
c64SonetAPSWorkLineFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64SonetAPSWorkLineFEBE.setStatus("current")
_C64SonetAPSWorkPathBIPE_Type = Counter32
_C64SonetAPSWorkPathBIPE_Object = MibTableColumn
c64SonetAPSWorkPathBIPE = _C64SonetAPSWorkPathBIPE_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 7),
    _C64SonetAPSWorkPathBIPE_Type()
)
c64SonetAPSWorkPathBIPE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64SonetAPSWorkPathBIPE.setStatus("current")
_C64SonetAPSWorkPathFEBE_Type = Counter32
_C64SonetAPSWorkPathFEBE_Object = MibTableColumn
c64SonetAPSWorkPathFEBE = _C64SonetAPSWorkPathFEBE_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 8),
    _C64SonetAPSWorkPathFEBE_Type()
)
c64SonetAPSWorkPathFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64SonetAPSWorkPathFEBE.setStatus("current")
_C64SonetAPSWorkPortStatus_Type = APSEventStatus
_C64SonetAPSWorkPortStatus_Object = MibTableColumn
c64SonetAPSWorkPortStatus = _C64SonetAPSWorkPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 9),
    _C64SonetAPSWorkPortStatus_Type()
)
c64SonetAPSWorkPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64SonetAPSWorkPortStatus.setStatus("current")


class _C64SonetAPSProtectSectionStatus_Type(Integer32):
    """Custom type c64SonetAPSProtectSectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_C64SonetAPSProtectSectionStatus_Type.__name__ = "Integer32"
_C64SonetAPSProtectSectionStatus_Object = MibTableColumn
c64SonetAPSProtectSectionStatus = _C64SonetAPSProtectSectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 10),
    _C64SonetAPSProtectSectionStatus_Type()
)
c64SonetAPSProtectSectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64SonetAPSProtectSectionStatus.setStatus("current")


class _C64SonetAPSProtectLineStatus_Type(Integer32):
    """Custom type c64SonetAPSProtectLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_C64SonetAPSProtectLineStatus_Type.__name__ = "Integer32"
_C64SonetAPSProtectLineStatus_Object = MibTableColumn
c64SonetAPSProtectLineStatus = _C64SonetAPSProtectLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 11),
    _C64SonetAPSProtectLineStatus_Type()
)
c64SonetAPSProtectLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64SonetAPSProtectLineStatus.setStatus("current")


class _C64SonetAPSProtectPathStatus_Type(Integer32):
    """Custom type c64SonetAPSProtectPathStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_C64SonetAPSProtectPathStatus_Type.__name__ = "Integer32"
_C64SonetAPSProtectPathStatus_Object = MibTableColumn
c64SonetAPSProtectPathStatus = _C64SonetAPSProtectPathStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 12),
    _C64SonetAPSProtectPathStatus_Type()
)
c64SonetAPSProtectPathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64SonetAPSProtectPathStatus.setStatus("current")
_C64SonetAPSProtectSectionBIPE_Type = Counter32
_C64SonetAPSProtectSectionBIPE_Object = MibTableColumn
c64SonetAPSProtectSectionBIPE = _C64SonetAPSProtectSectionBIPE_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 13),
    _C64SonetAPSProtectSectionBIPE_Type()
)
c64SonetAPSProtectSectionBIPE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64SonetAPSProtectSectionBIPE.setStatus("current")
_C64SonetAPSProtectLineBIPE_Type = Counter32
_C64SonetAPSProtectLineBIPE_Object = MibTableColumn
c64SonetAPSProtectLineBIPE = _C64SonetAPSProtectLineBIPE_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 14),
    _C64SonetAPSProtectLineBIPE_Type()
)
c64SonetAPSProtectLineBIPE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64SonetAPSProtectLineBIPE.setStatus("current")
_C64SonetAPSProtectLineFEBE_Type = Counter32
_C64SonetAPSProtectLineFEBE_Object = MibTableColumn
c64SonetAPSProtectLineFEBE = _C64SonetAPSProtectLineFEBE_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 15),
    _C64SonetAPSProtectLineFEBE_Type()
)
c64SonetAPSProtectLineFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64SonetAPSProtectLineFEBE.setStatus("current")
_C64SonetAPSProtectPathBIPE_Type = Counter32
_C64SonetAPSProtectPathBIPE_Object = MibTableColumn
c64SonetAPSProtectPathBIPE = _C64SonetAPSProtectPathBIPE_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 16),
    _C64SonetAPSProtectPathBIPE_Type()
)
c64SonetAPSProtectPathBIPE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64SonetAPSProtectPathBIPE.setStatus("current")
_C64SonetAPSProtectPathFEBE_Type = Counter32
_C64SonetAPSProtectPathFEBE_Object = MibTableColumn
c64SonetAPSProtectPathFEBE = _C64SonetAPSProtectPathFEBE_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 17),
    _C64SonetAPSProtectPathFEBE_Type()
)
c64SonetAPSProtectPathFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64SonetAPSProtectPathFEBE.setStatus("current")
_C64SonetAPSProtectPortStatus_Type = APSEventStatus
_C64SonetAPSProtectPortStatus_Object = MibTableColumn
c64SonetAPSProtectPortStatus = _C64SonetAPSProtectPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 18),
    _C64SonetAPSProtectPortStatus_Type()
)
c64SonetAPSProtectPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64SonetAPSProtectPortStatus.setStatus("current")
_C64SonetAPSChannelStatus_Type = APSEventStatus
_C64SonetAPSChannelStatus_Object = MibTableColumn
c64SonetAPSChannelStatus = _C64SonetAPSChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 19),
    _C64SonetAPSChannelStatus_Type()
)
c64SonetAPSChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64SonetAPSChannelStatus.setStatus("current")
_C64ChassisGroup_ObjectIdentity = ObjectIdentity
c64ChassisGroup = _C64ChassisGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2)
)
_C64TelcoAlarmMgmt_ObjectIdentity = ObjectIdentity
c64TelcoAlarmMgmt = _C64TelcoAlarmMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 1)
)


class _C64ChassisFacilityAlarmStatus_Type(Integer32):
    """Custom type c64ChassisFacilityAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_C64ChassisFacilityAlarmStatus_Type.__name__ = "Integer32"
_C64ChassisFacilityAlarmStatus_Object = MibScalar
c64ChassisFacilityAlarmStatus = _C64ChassisFacilityAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 1, 1),
    _C64ChassisFacilityAlarmStatus_Type()
)
c64ChassisFacilityAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64ChassisFacilityAlarmStatus.setStatus("current")


class _C64ChassisClearAlarms_Type(Integer32):
    """Custom type c64ChassisClearAlarms based on Integer32"""
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
        *(("all", 1),
          ("critical", 4),
          ("done", 0),
          ("major", 3),
          ("minor", 2))
    )


_C64ChassisClearAlarms_Type.__name__ = "Integer32"
_C64ChassisClearAlarms_Object = MibScalar
c64ChassisClearAlarms = _C64ChassisClearAlarms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 1, 2),
    _C64ChassisClearAlarms_Type()
)
c64ChassisClearAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c64ChassisClearAlarms.setStatus("current")


class _C64ChassisTempIntakeMinorThreshold_Type(Integer32):
    """Custom type c64ChassisTempIntakeMinorThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 57),
    )


_C64ChassisTempIntakeMinorThreshold_Type.__name__ = "Integer32"
_C64ChassisTempIntakeMinorThreshold_Object = MibScalar
c64ChassisTempIntakeMinorThreshold = _C64ChassisTempIntakeMinorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 1, 3),
    _C64ChassisTempIntakeMinorThreshold_Type()
)
c64ChassisTempIntakeMinorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c64ChassisTempIntakeMinorThreshold.setStatus("current")


class _C64ChassisTempIntakeMajorThreshold_Type(Integer32):
    """Custom type c64ChassisTempIntakeMajorThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 57),
    )


_C64ChassisTempIntakeMajorThreshold_Type.__name__ = "Integer32"
_C64ChassisTempIntakeMajorThreshold_Object = MibScalar
c64ChassisTempIntakeMajorThreshold = _C64ChassisTempIntakeMajorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 1, 4),
    _C64ChassisTempIntakeMajorThreshold_Type()
)
c64ChassisTempIntakeMajorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c64ChassisTempIntakeMajorThreshold.setStatus("current")


class _C64ChassisTempCoreMinorThreshold_Type(Integer32):
    """Custom type c64ChassisTempCoreMinorThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 60),
    )


_C64ChassisTempCoreMinorThreshold_Type.__name__ = "Integer32"
_C64ChassisTempCoreMinorThreshold_Object = MibScalar
c64ChassisTempCoreMinorThreshold = _C64ChassisTempCoreMinorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 1, 5),
    _C64ChassisTempCoreMinorThreshold_Type()
)
c64ChassisTempCoreMinorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c64ChassisTempCoreMinorThreshold.setStatus("current")


class _C64ChassisTempCoreMajorThreshold_Type(Integer32):
    """Custom type c64ChassisTempCoreMajorThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 60),
    )


_C64ChassisTempCoreMajorThreshold_Type.__name__ = "Integer32"
_C64ChassisTempCoreMajorThreshold_Object = MibScalar
c64ChassisTempCoreMajorThreshold = _C64ChassisTempCoreMajorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 1, 6),
    _C64ChassisTempCoreMajorThreshold_Type()
)
c64ChassisTempCoreMajorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c64ChassisTempCoreMajorThreshold.setStatus("current")


class _C64ChassisTempThresholdAdmin_Type(Integer32):
    """Custom type c64ChassisTempThresholdAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_C64ChassisTempThresholdAdmin_Type.__name__ = "Integer32"
_C64ChassisTempThresholdAdmin_Object = MibScalar
c64ChassisTempThresholdAdmin = _C64ChassisTempThresholdAdmin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 1, 7),
    _C64ChassisTempThresholdAdmin_Type()
)
c64ChassisTempThresholdAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c64ChassisTempThresholdAdmin.setStatus("current")
_C64ChassisAlarmTable_Object = MibTable
c64ChassisAlarmTable = _C64ChassisAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 2)
)
if mibBuilder.loadTexts:
    c64ChassisAlarmTable.setStatus("current")
_C64ChassisAlarmEntry_Object = MibTableRow
c64ChassisAlarmEntry = _C64ChassisAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 2, 1)
)
c64ChassisAlarmEntry.setIndexNames(
    (0, "CISCO-6400-CHASSIS-MIB", "c64ChassisAlarmIndex"),
)
if mibBuilder.loadTexts:
    c64ChassisAlarmEntry.setStatus("current")


class _C64ChassisAlarmIndex_Type(Integer32):
    """Custom type c64ChassisAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_C64ChassisAlarmIndex_Type.__name__ = "Integer32"
_C64ChassisAlarmIndex_Object = MibTableColumn
c64ChassisAlarmIndex = _C64ChassisAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 2, 1, 1),
    _C64ChassisAlarmIndex_Type()
)
c64ChassisAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64ChassisAlarmIndex.setStatus("current")
_C64ChassisAlarmSource_Type = DisplayString
_C64ChassisAlarmSource_Object = MibTableColumn
c64ChassisAlarmSource = _C64ChassisAlarmSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 2, 1, 2),
    _C64ChassisAlarmSource_Type()
)
c64ChassisAlarmSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64ChassisAlarmSource.setStatus("current")


class _C64ChassisAlarmType_Type(Integer32):
    """Custom type c64ChassisAlarmType based on Integer32"""
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("cardFail", 10),
          ("cardOIRAlarm", 9),
          ("cardPartialFail", 11),
          ("coreTemp", 1),
          ("diskAlarm", 16),
          ("fanMissing", 5),
          ("imageAlarm", 17),
          ("inletTemp", 2),
          ("linkDownAlarm", 12),
          ("networkClockAlarm", 13),
          ("nrpBootUpAlarm", 18),
          ("nrpMismatchAlarm", 22),
          ("nrpPAMDataError", 15),
          ("nrpSARFail", 14),
          ("nrpSecondaryFailureAlarm", 20),
          ("nrpSecondaryRemovedAlarm", 21),
          ("nrpSwitchoverAlarm", 19),
          ("partialFanFail", 4),
          ("pem0Fail", 6),
          ("pem1Fail", 7),
          ("sonetLineFail", 8),
          ("totalFanFail", 3))
    )


_C64ChassisAlarmType_Type.__name__ = "Integer32"
_C64ChassisAlarmType_Object = MibTableColumn
c64ChassisAlarmType = _C64ChassisAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 2, 1, 3),
    _C64ChassisAlarmType_Type()
)
c64ChassisAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64ChassisAlarmType.setStatus("current")


class _C64ChassisAlarmSeverity_Type(Integer32):
    """Custom type c64ChassisAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("major", 2),
          ("minor", 1))
    )


_C64ChassisAlarmSeverity_Type.__name__ = "Integer32"
_C64ChassisAlarmSeverity_Object = MibTableColumn
c64ChassisAlarmSeverity = _C64ChassisAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 2, 1, 4),
    _C64ChassisAlarmSeverity_Type()
)
c64ChassisAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64ChassisAlarmSeverity.setStatus("current")


class _C64ChassisAlarmACOStatus_Type(Integer32):
    """Custom type c64ChassisAlarmACOStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cutoff", 2),
          ("normal", 1))
    )


_C64ChassisAlarmACOStatus_Type.__name__ = "Integer32"
_C64ChassisAlarmACOStatus_Object = MibTableColumn
c64ChassisAlarmACOStatus = _C64ChassisAlarmACOStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 2, 1, 5),
    _C64ChassisAlarmACOStatus_Type()
)
c64ChassisAlarmACOStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c64ChassisAlarmACOStatus.setStatus("current")
_Cisco6400ChassisMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cisco6400ChassisMIBNotificationPrefix = _Cisco6400ChassisMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 2)
)
_Cisco6400ChassisMIBNotification_ObjectIdentity = ObjectIdentity
cisco6400ChassisMIBNotification = _Cisco6400ChassisMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 2, 0)
)
_Cisco6400ChassisMIBConformance_ObjectIdentity = ObjectIdentity
cisco6400ChassisMIBConformance = _Cisco6400ChassisMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 3)
)
_Cisco6400ChassisMIBCompliances_ObjectIdentity = ObjectIdentity
cisco6400ChassisMIBCompliances = _Cisco6400ChassisMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 3, 1)
)
_Cisco6400ChassisMIBGroups_ObjectIdentity = ObjectIdentity
cisco6400ChassisMIBGroups = _Cisco6400ChassisMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 3, 2)
)

# Managed Objects groups

cisco6400RedundantGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 3, 2, 1)
)
cisco6400RedundantGroup.setObjects(
      *(("CISCO-6400-CHASSIS-MIB", "c64MainCPUConfigAutoSync"),
        ("CISCO-6400-CHASSIS-MIB", "c64MainCPUSwitchOver"),
        ("CISCO-6400-CHASSIS-MIB", "c64Slot1Name"),
        ("CISCO-6400-CHASSIS-MIB", "c64Slot2Name"),
        ("CISCO-6400-CHASSIS-MIB", "c64SlotConfigPrefIndex"),
        ("CISCO-6400-CHASSIS-MIB", "c64SlotSwitchOver"),
        ("CISCO-6400-CHASSIS-MIB", "c64SlotConfigStatus"),
        ("CISCO-6400-CHASSIS-MIB", "c64SubSlot1Name"),
        ("CISCO-6400-CHASSIS-MIB", "c64SubSlot2Name"),
        ("CISCO-6400-CHASSIS-MIB", "c64SubSlotConfigPrefIndex"),
        ("CISCO-6400-CHASSIS-MIB", "c64SubSlotSwitchOver"),
        ("CISCO-6400-CHASSIS-MIB", "c64SubSlotConfigStatus"),
        ("CISCO-6400-CHASSIS-MIB", "c64Port1Name"),
        ("CISCO-6400-CHASSIS-MIB", "c64Port2Name"),
        ("CISCO-6400-CHASSIS-MIB", "c64PortConfigPrefIndex"),
        ("CISCO-6400-CHASSIS-MIB", "c64PortSwitchOver"),
        ("CISCO-6400-CHASSIS-MIB", "c64PortConfigStatus"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSMode"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSBERThreshold"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSSwitchCmd"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSSFBERThreshold"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkSectionStatus"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkLineStatus"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkPathStatus"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkSectionBIPE"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkLineBIPE"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkLineFEBE"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkPathBIPE"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkPathFEBE"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkPortStatus"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectSectionStatus"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectLineStatus"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectPathStatus"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectSectionBIPE"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectLineBIPE"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectLineFEBE"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectPathBIPE"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectPathFEBE"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectPortStatus"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSChannelStatus"))
)
if mibBuilder.loadTexts:
    cisco6400RedundantGroup.setStatus("deprecated")

cisco6400ChassisMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 3, 2, 2)
)
cisco6400ChassisMIBGroup.setObjects(
      *(("CISCO-6400-CHASSIS-MIB", "c64ChassisFacilityAlarmStatus"),
        ("CISCO-6400-CHASSIS-MIB", "c64ChassisClearAlarms"),
        ("CISCO-6400-CHASSIS-MIB", "c64ChassisTempIntakeMinorThreshold"),
        ("CISCO-6400-CHASSIS-MIB", "c64ChassisTempIntakeMajorThreshold"),
        ("CISCO-6400-CHASSIS-MIB", "c64ChassisTempCoreMinorThreshold"),
        ("CISCO-6400-CHASSIS-MIB", "c64ChassisTempCoreMajorThreshold"),
        ("CISCO-6400-CHASSIS-MIB", "c64ChassisTempThresholdAdmin"),
        ("CISCO-6400-CHASSIS-MIB", "c64ChassisAlarmIndex"),
        ("CISCO-6400-CHASSIS-MIB", "c64ChassisAlarmSource"),
        ("CISCO-6400-CHASSIS-MIB", "c64ChassisAlarmType"),
        ("CISCO-6400-CHASSIS-MIB", "c64ChassisAlarmSeverity"),
        ("CISCO-6400-CHASSIS-MIB", "c64ChassisAlarmACOStatus"))
)
if mibBuilder.loadTexts:
    cisco6400ChassisMIBGroup.setStatus("current")

cisco6400RedundantGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 3, 2, 3)
)
cisco6400RedundantGroup2.setObjects(
      *(("CISCO-6400-CHASSIS-MIB", "c64MainCPUConfigAutoSync"),
        ("CISCO-6400-CHASSIS-MIB", "c64MainCPUSwitchOver"),
        ("CISCO-6400-CHASSIS-MIB", "c64Slot1Name"),
        ("CISCO-6400-CHASSIS-MIB", "c64Slot2Name"),
        ("CISCO-6400-CHASSIS-MIB", "c64SlotSwitchOver"),
        ("CISCO-6400-CHASSIS-MIB", "c64SlotConfigStatus"),
        ("CISCO-6400-CHASSIS-MIB", "c64SubSlot1Name"),
        ("CISCO-6400-CHASSIS-MIB", "c64SubSlot2Name"),
        ("CISCO-6400-CHASSIS-MIB", "c64SubSlotSwitchOver"),
        ("CISCO-6400-CHASSIS-MIB", "c64SubSlotConfigStatus"),
        ("CISCO-6400-CHASSIS-MIB", "c64Port1Name"),
        ("CISCO-6400-CHASSIS-MIB", "c64Port2Name"),
        ("CISCO-6400-CHASSIS-MIB", "c64PortConfigPrefIndex"),
        ("CISCO-6400-CHASSIS-MIB", "c64PortSwitchOver"),
        ("CISCO-6400-CHASSIS-MIB", "c64PortConfigStatus"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSMode"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSBERThreshold"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSSwitchCmd"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSSFBERThreshold"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkSectionStatus"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkLineStatus"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkPathStatus"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkSectionBIPE"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkLineBIPE"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkLineFEBE"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkPathBIPE"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkPathFEBE"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkPortStatus"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectSectionStatus"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectLineStatus"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectPathStatus"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectSectionBIPE"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectLineBIPE"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectLineFEBE"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectPathBIPE"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectPathFEBE"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectPortStatus"),
        ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSChannelStatus"))
)
if mibBuilder.loadTexts:
    cisco6400RedundantGroup2.setStatus("current")


# Notification objects

cisco6400ChassisFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 2, 0, 1)
)
cisco6400ChassisFailureNotification.setObjects(
    ("CISCO-6400-CHASSIS-MIB", "c64ChassisFacilityAlarmStatus")
)
if mibBuilder.loadTexts:
    cisco6400ChassisFailureNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

cisco6400ChassisMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cisco6400ChassisMIBCompliance.setStatus(
        "deprecated"
    )

cisco6400ChassisMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 27, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cisco6400ChassisMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-6400-CHASSIS-MIB",
    **{"APSEventStatus": APSEventStatus,
       "cisco6400ChassisMIB": cisco6400ChassisMIB,
       "cisco6400ChassisMIBObjects": cisco6400ChassisMIBObjects,
       "c64RedundantGroup": c64RedundantGroup,
       "c64MainCPUConfigAutoSync": c64MainCPUConfigAutoSync,
       "c64MainCPUSwitchOver": c64MainCPUSwitchOver,
       "c64SlotConfigTable": c64SlotConfigTable,
       "c64SlotConfigEntry": c64SlotConfigEntry,
       "c64SlotConfigModule1Index": c64SlotConfigModule1Index,
       "c64SlotConfigModule2Index": c64SlotConfigModule2Index,
       "c64Slot1Name": c64Slot1Name,
       "c64Slot2Name": c64Slot2Name,
       "c64SlotConfigPrefIndex": c64SlotConfigPrefIndex,
       "c64SlotSwitchOver": c64SlotSwitchOver,
       "c64SlotConfigStatus": c64SlotConfigStatus,
       "c64SubSlotConfigTable": c64SubSlotConfigTable,
       "c64SubSlotConfigEntry": c64SubSlotConfigEntry,
       "c64SubSlotRedundantIndex": c64SubSlotRedundantIndex,
       "c64SubSlotConfigModule1Index": c64SubSlotConfigModule1Index,
       "c64SubSlotConfigSubModule1Index": c64SubSlotConfigSubModule1Index,
       "c64SubSlotConfigModule2Index": c64SubSlotConfigModule2Index,
       "c64SubSlotConfigSubModule2Index": c64SubSlotConfigSubModule2Index,
       "c64SubSlot1Name": c64SubSlot1Name,
       "c64SubSlot2Name": c64SubSlot2Name,
       "c64SubSlotConfigPrefIndex": c64SubSlotConfigPrefIndex,
       "c64SubSlotSwitchOver": c64SubSlotSwitchOver,
       "c64SubSlotConfigStatus": c64SubSlotConfigStatus,
       "c64PortConfigTable": c64PortConfigTable,
       "c64PortConfigEntry": c64PortConfigEntry,
       "c64PortConfigModule1Index": c64PortConfigModule1Index,
       "c64PortConfigSubModule1Index": c64PortConfigSubModule1Index,
       "c64PortConfigPort1Index": c64PortConfigPort1Index,
       "c64PortConfigModule2Index": c64PortConfigModule2Index,
       "c64PortConfigSubModule2Index": c64PortConfigSubModule2Index,
       "c64PortConfigPort2Index": c64PortConfigPort2Index,
       "c64Port1Name": c64Port1Name,
       "c64Port2Name": c64Port2Name,
       "c64PortConfigPrefIndex": c64PortConfigPrefIndex,
       "c64PortSwitchOver": c64PortSwitchOver,
       "c64PortConfigStatus": c64PortConfigStatus,
       "c64SonetAPSConfigTable": c64SonetAPSConfigTable,
       "c64SonetAPSConfigEntry": c64SonetAPSConfigEntry,
       "c64SonetAPSMode": c64SonetAPSMode,
       "c64SonetAPSBERThreshold": c64SonetAPSBERThreshold,
       "c64SonetAPSSwitchCmd": c64SonetAPSSwitchCmd,
       "c64SonetAPSSFBERThreshold": c64SonetAPSSFBERThreshold,
       "c64SonetAPSStatsTable": c64SonetAPSStatsTable,
       "c64SonetAPSStatsEntry": c64SonetAPSStatsEntry,
       "c64SonetAPSWorkSectionStatus": c64SonetAPSWorkSectionStatus,
       "c64SonetAPSWorkLineStatus": c64SonetAPSWorkLineStatus,
       "c64SonetAPSWorkPathStatus": c64SonetAPSWorkPathStatus,
       "c64SonetAPSWorkSectionBIPE": c64SonetAPSWorkSectionBIPE,
       "c64SonetAPSWorkLineBIPE": c64SonetAPSWorkLineBIPE,
       "c64SonetAPSWorkLineFEBE": c64SonetAPSWorkLineFEBE,
       "c64SonetAPSWorkPathBIPE": c64SonetAPSWorkPathBIPE,
       "c64SonetAPSWorkPathFEBE": c64SonetAPSWorkPathFEBE,
       "c64SonetAPSWorkPortStatus": c64SonetAPSWorkPortStatus,
       "c64SonetAPSProtectSectionStatus": c64SonetAPSProtectSectionStatus,
       "c64SonetAPSProtectLineStatus": c64SonetAPSProtectLineStatus,
       "c64SonetAPSProtectPathStatus": c64SonetAPSProtectPathStatus,
       "c64SonetAPSProtectSectionBIPE": c64SonetAPSProtectSectionBIPE,
       "c64SonetAPSProtectLineBIPE": c64SonetAPSProtectLineBIPE,
       "c64SonetAPSProtectLineFEBE": c64SonetAPSProtectLineFEBE,
       "c64SonetAPSProtectPathBIPE": c64SonetAPSProtectPathBIPE,
       "c64SonetAPSProtectPathFEBE": c64SonetAPSProtectPathFEBE,
       "c64SonetAPSProtectPortStatus": c64SonetAPSProtectPortStatus,
       "c64SonetAPSChannelStatus": c64SonetAPSChannelStatus,
       "c64ChassisGroup": c64ChassisGroup,
       "c64TelcoAlarmMgmt": c64TelcoAlarmMgmt,
       "c64ChassisFacilityAlarmStatus": c64ChassisFacilityAlarmStatus,
       "c64ChassisClearAlarms": c64ChassisClearAlarms,
       "c64ChassisTempIntakeMinorThreshold": c64ChassisTempIntakeMinorThreshold,
       "c64ChassisTempIntakeMajorThreshold": c64ChassisTempIntakeMajorThreshold,
       "c64ChassisTempCoreMinorThreshold": c64ChassisTempCoreMinorThreshold,
       "c64ChassisTempCoreMajorThreshold": c64ChassisTempCoreMajorThreshold,
       "c64ChassisTempThresholdAdmin": c64ChassisTempThresholdAdmin,
       "c64ChassisAlarmTable": c64ChassisAlarmTable,
       "c64ChassisAlarmEntry": c64ChassisAlarmEntry,
       "c64ChassisAlarmIndex": c64ChassisAlarmIndex,
       "c64ChassisAlarmSource": c64ChassisAlarmSource,
       "c64ChassisAlarmType": c64ChassisAlarmType,
       "c64ChassisAlarmSeverity": c64ChassisAlarmSeverity,
       "c64ChassisAlarmACOStatus": c64ChassisAlarmACOStatus,
       "cisco6400ChassisMIBNotificationPrefix": cisco6400ChassisMIBNotificationPrefix,
       "cisco6400ChassisMIBNotification": cisco6400ChassisMIBNotification,
       "cisco6400ChassisFailureNotification": cisco6400ChassisFailureNotification,
       "cisco6400ChassisMIBConformance": cisco6400ChassisMIBConformance,
       "cisco6400ChassisMIBCompliances": cisco6400ChassisMIBCompliances,
       "cisco6400ChassisMIBCompliance": cisco6400ChassisMIBCompliance,
       "cisco6400ChassisMIBCompliance2": cisco6400ChassisMIBCompliance2,
       "cisco6400ChassisMIBGroups": cisco6400ChassisMIBGroups,
       "cisco6400RedundantGroup": cisco6400RedundantGroup,
       "cisco6400ChassisMIBGroup": cisco6400ChassisMIBGroup,
       "cisco6400RedundantGroup2": cisco6400RedundantGroup2}
)
