# SNMP MIB module (CISCO-HW-MODULE-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-HW-MODULE-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:18 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoInterfaceIndexList,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoInterfaceIndexList")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

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

ciscoHwModuleControlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 714)
)
ciscoHwModuleControlMIB.setRevisions(
        ("2010-08-09 00:00",
         "2009-11-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoHwModuleControlMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoHwModuleControlMIBNotifs = _CiscoHwModuleControlMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 0)
)
_CiscoHwModuleControlMIBObjects_ObjectIdentity = ObjectIdentity
ciscoHwModuleControlMIBObjects = _CiscoHwModuleControlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 1)
)
_ChmcOversubscription_ObjectIdentity = ObjectIdentity
chmcOversubscription = _ChmcOversubscription_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 1, 1)
)
_ChmcOversubModuleTable_Object = MibTable
chmcOversubModuleTable = _ChmcOversubModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 1, 1, 1)
)
if mibBuilder.loadTexts:
    chmcOversubModuleTable.setStatus("current")
_ChmcOversubModuleEntry_Object = MibTableRow
chmcOversubModuleEntry = _ChmcOversubModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 1, 1, 1, 1)
)
chmcOversubModuleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    chmcOversubModuleEntry.setStatus("current")


class _ChmcOversubModuleCapabilities_Type(Bits):
    """Custom type chmcOversubModuleCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("clearblockConfigPortGroupLevel", 2),
          ("oversubConfigModuleLevel", 0),
          ("oversubConfigPortGroupLevel", 1))
    )

_ChmcOversubModuleCapabilities_Type.__name__ = "Bits"
_ChmcOversubModuleCapabilities_Object = MibTableColumn
chmcOversubModuleCapabilities = _ChmcOversubModuleCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 1, 1, 1, 1, 1),
    _ChmcOversubModuleCapabilities_Type()
)
chmcOversubModuleCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmcOversubModuleCapabilities.setStatus("current")


class _ChmcOversubModOversubStatus_Type(Integer32):
    """Custom type chmcOversubModOversubStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabledOnAllPortGroups", 2),
          ("enabledOnAllPortGroups", 1),
          ("portGroupSpecific", 3))
    )


_ChmcOversubModOversubStatus_Type.__name__ = "Integer32"
_ChmcOversubModOversubStatus_Object = MibTableColumn
chmcOversubModOversubStatus = _ChmcOversubModOversubStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 1, 1, 1, 1, 2),
    _ChmcOversubModOversubStatus_Type()
)
chmcOversubModOversubStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chmcOversubModOversubStatus.setStatus("current")
_ChmcOversubPortGroupTable_Object = MibTable
chmcOversubPortGroupTable = _ChmcOversubPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 1, 1, 2)
)
if mibBuilder.loadTexts:
    chmcOversubPortGroupTable.setStatus("current")
_ChmcOversubPortGroupEntry_Object = MibTableRow
chmcOversubPortGroupEntry = _ChmcOversubPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 1, 1, 2, 1)
)
chmcOversubPortGroupEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-HW-MODULE-CONTROL-MIB", "chmcOversubPortGrpIndex"),
)
if mibBuilder.loadTexts:
    chmcOversubPortGroupEntry.setStatus("current")


class _ChmcOversubPortGrpIndex_Type(Unsigned32):
    """Custom type chmcOversubPortGrpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ChmcOversubPortGrpIndex_Type.__name__ = "Unsigned32"
_ChmcOversubPortGrpIndex_Object = MibTableColumn
chmcOversubPortGrpIndex = _ChmcOversubPortGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 1, 1, 2, 1, 1),
    _ChmcOversubPortGrpIndex_Type()
)
chmcOversubPortGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chmcOversubPortGrpIndex.setStatus("current")
_ChmcOversubPortGrpIfIndexList_Type = CiscoInterfaceIndexList
_ChmcOversubPortGrpIfIndexList_Object = MibTableColumn
chmcOversubPortGrpIfIndexList = _ChmcOversubPortGrpIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 1, 1, 2, 1, 2),
    _ChmcOversubPortGrpIfIndexList_Type()
)
chmcOversubPortGrpIfIndexList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmcOversubPortGrpIfIndexList.setStatus("current")


class _ChmcOversubPortGrpOversubStatus_Type(Integer32):
    """Custom type chmcOversubPortGrpOversubStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_ChmcOversubPortGrpOversubStatus_Type.__name__ = "Integer32"
_ChmcOversubPortGrpOversubStatus_Object = MibTableColumn
chmcOversubPortGrpOversubStatus = _ChmcOversubPortGrpOversubStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 1, 1, 2, 1, 3),
    _ChmcOversubPortGrpOversubStatus_Type()
)
chmcOversubPortGrpOversubStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chmcOversubPortGrpOversubStatus.setStatus("current")


class _ChmcOversubPortGrpClearBlkStatus_Type(Integer32):
    """Custom type chmcOversubPortGrpClearBlkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_ChmcOversubPortGrpClearBlkStatus_Type.__name__ = "Integer32"
_ChmcOversubPortGrpClearBlkStatus_Object = MibTableColumn
chmcOversubPortGrpClearBlkStatus = _ChmcOversubPortGrpClearBlkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 1, 1, 2, 1, 4),
    _ChmcOversubPortGrpClearBlkStatus_Type()
)
chmcOversubPortGrpClearBlkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chmcOversubPortGrpClearBlkStatus.setStatus("current")
_ChmcOperationalMode_ObjectIdentity = ObjectIdentity
chmcOperationalMode = _ChmcOperationalMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 1, 2)
)
_ChmcOperModePortGroupTable_Object = MibTable
chmcOperModePortGroupTable = _ChmcOperModePortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 1, 2, 1)
)
if mibBuilder.loadTexts:
    chmcOperModePortGroupTable.setStatus("current")
_ChmcOperModePortGroupEntry_Object = MibTableRow
chmcOperModePortGroupEntry = _ChmcOperModePortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 1, 2, 1, 1)
)
chmcOperModePortGroupEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-HW-MODULE-CONTROL-MIB", "chmcOperModePortGrpIndex"),
)
if mibBuilder.loadTexts:
    chmcOperModePortGroupEntry.setStatus("current")


class _ChmcOperModePortGrpIndex_Type(Unsigned32):
    """Custom type chmcOperModePortGrpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ChmcOperModePortGrpIndex_Type.__name__ = "Unsigned32"
_ChmcOperModePortGrpIndex_Object = MibTableColumn
chmcOperModePortGrpIndex = _ChmcOperModePortGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 1, 2, 1, 1, 1),
    _ChmcOperModePortGrpIndex_Type()
)
chmcOperModePortGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chmcOperModePortGrpIndex.setStatus("current")


class _ChmcOperModePortGrpOperMode_Type(Integer32):
    """Custom type chmcOperModePortGrpOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fortyGigabitEthernet", 3),
          ("other", 1),
          ("tenGigabitEthernet", 2))
    )


_ChmcOperModePortGrpOperMode_Type.__name__ = "Integer32"
_ChmcOperModePortGrpOperMode_Object = MibTableColumn
chmcOperModePortGrpOperMode = _ChmcOperModePortGrpOperMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 1, 2, 1, 1, 2),
    _ChmcOperModePortGrpOperMode_Type()
)
chmcOperModePortGrpOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chmcOperModePortGrpOperMode.setStatus("current")
_ChmcOperModePortGrpIfIndexList_Type = CiscoInterfaceIndexList
_ChmcOperModePortGrpIfIndexList_Object = MibTableColumn
chmcOperModePortGrpIfIndexList = _ChmcOperModePortGrpIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 1, 2, 1, 1, 3),
    _ChmcOperModePortGrpIfIndexList_Type()
)
chmcOperModePortGrpIfIndexList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmcOperModePortGrpIfIndexList.setStatus("current")
_CiscoHwModuleControlMIBConform_ObjectIdentity = ObjectIdentity
ciscoHwModuleControlMIBConform = _CiscoHwModuleControlMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 2)
)
_ChmcHwModuleControlMIBCompliances_ObjectIdentity = ObjectIdentity
chmcHwModuleControlMIBCompliances = _ChmcHwModuleControlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 2, 1)
)
_ChmcHwModuleControlMIBGroups_ObjectIdentity = ObjectIdentity
chmcHwModuleControlMIBGroups = _ChmcHwModuleControlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 2, 2)
)

# Managed Objects groups

ciscoHmcMIBOversubBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 2, 2, 1)
)
ciscoHmcMIBOversubBaseGroup.setObjects(
      *(("CISCO-HW-MODULE-CONTROL-MIB", "chmcOversubModuleCapabilities"),
        ("CISCO-HW-MODULE-CONTROL-MIB", "chmcOversubModOversubStatus"),
        ("CISCO-HW-MODULE-CONTROL-MIB", "chmcOversubPortGrpIfIndexList"),
        ("CISCO-HW-MODULE-CONTROL-MIB", "chmcOversubPortGrpOversubStatus"))
)
if mibBuilder.loadTexts:
    ciscoHmcMIBOversubBaseGroup.setStatus("current")

ciscoHmcMIBOversubPgClearBlkGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 2, 2, 2)
)
ciscoHmcMIBOversubPgClearBlkGrp.setObjects(
    ("CISCO-HW-MODULE-CONTROL-MIB", "chmcOversubPortGrpClearBlkStatus")
)
if mibBuilder.loadTexts:
    ciscoHmcMIBOversubPgClearBlkGrp.setStatus("current")

ciscoHmcMIBOperModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 2, 2, 3)
)
ciscoHmcMIBOperModeGroup.setObjects(
      *(("CISCO-HW-MODULE-CONTROL-MIB", "chmcOperModePortGrpOperMode"),
        ("CISCO-HW-MODULE-CONTROL-MIB", "chmcOperModePortGrpIfIndexList"))
)
if mibBuilder.loadTexts:
    ciscoHmcMIBOperModeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

chmcHwModuleControlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 2, 1, 1)
)
if mibBuilder.loadTexts:
    chmcHwModuleControlMIBCompliance.setStatus(
        "deprecated"
    )

chmcHwModuleControlMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 714, 2, 1, 2)
)
if mibBuilder.loadTexts:
    chmcHwModuleControlMIBCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-HW-MODULE-CONTROL-MIB",
    **{"ciscoHwModuleControlMIB": ciscoHwModuleControlMIB,
       "ciscoHwModuleControlMIBNotifs": ciscoHwModuleControlMIBNotifs,
       "ciscoHwModuleControlMIBObjects": ciscoHwModuleControlMIBObjects,
       "chmcOversubscription": chmcOversubscription,
       "chmcOversubModuleTable": chmcOversubModuleTable,
       "chmcOversubModuleEntry": chmcOversubModuleEntry,
       "chmcOversubModuleCapabilities": chmcOversubModuleCapabilities,
       "chmcOversubModOversubStatus": chmcOversubModOversubStatus,
       "chmcOversubPortGroupTable": chmcOversubPortGroupTable,
       "chmcOversubPortGroupEntry": chmcOversubPortGroupEntry,
       "chmcOversubPortGrpIndex": chmcOversubPortGrpIndex,
       "chmcOversubPortGrpIfIndexList": chmcOversubPortGrpIfIndexList,
       "chmcOversubPortGrpOversubStatus": chmcOversubPortGrpOversubStatus,
       "chmcOversubPortGrpClearBlkStatus": chmcOversubPortGrpClearBlkStatus,
       "chmcOperationalMode": chmcOperationalMode,
       "chmcOperModePortGroupTable": chmcOperModePortGroupTable,
       "chmcOperModePortGroupEntry": chmcOperModePortGroupEntry,
       "chmcOperModePortGrpIndex": chmcOperModePortGrpIndex,
       "chmcOperModePortGrpOperMode": chmcOperModePortGrpOperMode,
       "chmcOperModePortGrpIfIndexList": chmcOperModePortGrpIfIndexList,
       "ciscoHwModuleControlMIBConform": ciscoHwModuleControlMIBConform,
       "chmcHwModuleControlMIBCompliances": chmcHwModuleControlMIBCompliances,
       "chmcHwModuleControlMIBCompliance": chmcHwModuleControlMIBCompliance,
       "chmcHwModuleControlMIBCompliance1": chmcHwModuleControlMIBCompliance1,
       "chmcHwModuleControlMIBGroups": chmcHwModuleControlMIBGroups,
       "ciscoHmcMIBOversubBaseGroup": ciscoHmcMIBOversubBaseGroup,
       "ciscoHmcMIBOversubPgClearBlkGrp": ciscoHmcMIBOversubPgClearBlkGrp,
       "ciscoHmcMIBOperModeGroup": ciscoHmcMIBOperModeGroup}
)
