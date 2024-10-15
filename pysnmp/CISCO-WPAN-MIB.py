# SNMP MIB module (CISCO-WPAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WPAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:44 2024
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

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoWpanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 819)
)
ciscoWpanMIB.setRevisions(
        ("2013-11-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoWpanMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoWpanMIBNotifs = _CiscoWpanMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 0)
)
_CiscoWpanMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWpanMIBObjects = _CiscoWpanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1)
)
_CiscoWpanConfig_ObjectIdentity = ObjectIdentity
ciscoWpanConfig = _CiscoWpanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1, 1)
)
_CwpanInterfaceTable_Object = MibTable
cwpanInterfaceTable = _CwpanInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cwpanInterfaceTable.setStatus("current")
_CwpanInterfaceEntry_Object = MibTableRow
cwpanInterfaceEntry = _CwpanInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1, 1, 1, 1)
)
cwpanInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwpanInterfaceEntry.setStatus("current")


class _CwpanIfServiceStatus_Type(Integer32):
    """Custom type cwpanIfServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_CwpanIfServiceStatus_Type.__name__ = "Integer32"
_CwpanIfServiceStatus_Object = MibTableColumn
cwpanIfServiceStatus = _CwpanIfServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1, 1, 1, 1, 1),
    _CwpanIfServiceStatus_Type()
)
cwpanIfServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwpanIfServiceStatus.setStatus("current")


class _CwpanIfServiceStatusReason_Type(Integer32):
    """Custom type cwpanIfServiceStatusReason based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("driverStart", 7),
          ("driverStop", 6),
          ("firmwareReset", 9),
          ("firmwareUpgrade", 8),
          ("moduleReload", 5),
          ("moduleRemove", 4),
          ("powerDown", 2),
          ("powerUp", 3),
          ("unknown", 1),
          ("watchDog", 10))
    )


_CwpanIfServiceStatusReason_Type.__name__ = "Integer32"
_CwpanIfServiceStatusReason_Object = MibTableColumn
cwpanIfServiceStatusReason = _CwpanIfServiceStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1, 1, 1, 1, 2),
    _CwpanIfServiceStatusReason_Type()
)
cwpanIfServiceStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwpanIfServiceStatusReason.setStatus("current")


class _CwpanIfRplTableResetReason_Type(Integer32):
    """Custom type cwpanIfRplTableResetReason based on Integer32"""
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
        *(("configChange", 3),
          ("interfaceDown", 4),
          ("manuallyClear", 2),
          ("serviceStop", 6),
          ("timeout", 5),
          ("unknown", 1))
    )


_CwpanIfRplTableResetReason_Type.__name__ = "Integer32"
_CwpanIfRplTableResetReason_Object = MibTableColumn
cwpanIfRplTableResetReason = _CwpanIfRplTableResetReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1, 1, 1, 1, 3),
    _CwpanIfRplTableResetReason_Type()
)
cwpanIfRplTableResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwpanIfRplTableResetReason.setStatus("current")
_CwpanIfRplTableNodes_Type = Unsigned32
_CwpanIfRplTableNodes_Object = MibTableColumn
cwpanIfRplTableNodes = _CwpanIfRplTableNodes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1, 1, 1, 1, 4),
    _CwpanIfRplTableNodes_Type()
)
cwpanIfRplTableNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwpanIfRplTableNodes.setStatus("current")
_CwpanIfRplTableMajorThreshNodes_Type = Unsigned32
_CwpanIfRplTableMajorThreshNodes_Object = MibTableColumn
cwpanIfRplTableMajorThreshNodes = _CwpanIfRplTableMajorThreshNodes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1, 1, 1, 1, 5),
    _CwpanIfRplTableMajorThreshNodes_Type()
)
cwpanIfRplTableMajorThreshNodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwpanIfRplTableMajorThreshNodes.setStatus("current")
_CwpanIfRplTableMinorThreshNodes_Type = Unsigned32
_CwpanIfRplTableMinorThreshNodes_Object = MibTableColumn
cwpanIfRplTableMinorThreshNodes = _CwpanIfRplTableMinorThreshNodes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1, 1, 1, 1, 6),
    _CwpanIfRplTableMinorThreshNodes_Type()
)
cwpanIfRplTableMinorThreshNodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwpanIfRplTableMinorThreshNodes.setStatus("current")
_CwpanNotificationEnable_Type = TruthValue
_CwpanNotificationEnable_Object = MibScalar
cwpanNotificationEnable = _CwpanNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1, 1, 2),
    _CwpanNotificationEnable_Type()
)
cwpanNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwpanNotificationEnable.setStatus("current")
_CiscoWpanMIBConform_ObjectIdentity = ObjectIdentity
ciscoWpanMIBConform = _CiscoWpanMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 2)
)
_CiscoWpanMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWpanMIBCompliances = _CiscoWpanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 2, 1)
)
_CiscoWpanMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWpanMIBGroups = _CiscoWpanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 2, 2)
)

# Managed Objects groups

cwpanInterfaceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 2, 2, 1)
)
cwpanInterfaceInfoGroup.setObjects(
      *(("CISCO-WPAN-MIB", "cwpanIfServiceStatus"),
        ("CISCO-WPAN-MIB", "cwpanIfServiceStatusReason"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableResetReason"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableNodes"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableMajorThreshNodes"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableMinorThreshNodes"))
)
if mibBuilder.loadTexts:
    cwpanInterfaceInfoGroup.setStatus("current")

cwpanNotificationControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 2, 2, 2)
)
cwpanNotificationControlGroup.setObjects(
    ("CISCO-WPAN-MIB", "cwpanNotificationEnable")
)
if mibBuilder.loadTexts:
    cwpanNotificationControlGroup.setStatus("current")


# Notification objects

cwpanServiceStatusChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 0, 1)
)
cwpanServiceStatusChangeNotif.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-WPAN-MIB", "cwpanIfServiceStatusReason"))
)
if mibBuilder.loadTexts:
    cwpanServiceStatusChangeNotif.setStatus(
        "current"
    )

cwpanRplTableResetNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 0, 2)
)
cwpanRplTableResetNotif.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableResetReason"))
)
if mibBuilder.loadTexts:
    cwpanRplTableResetNotif.setStatus(
        "current"
    )

cwpanRisingIfRplTblMinorThreshNodesNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 0, 3)
)
cwpanRisingIfRplTblMinorThreshNodesNotif.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableNodes"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableMinorThreshNodes"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableMajorThreshNodes"))
)
if mibBuilder.loadTexts:
    cwpanRisingIfRplTblMinorThreshNodesNotif.setStatus(
        "current"
    )

cwpanFallingIfRplTblMinorThreshNodesNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 0, 4)
)
cwpanFallingIfRplTblMinorThreshNodesNotif.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableNodes"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableMinorThreshNodes"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableMajorThreshNodes"))
)
if mibBuilder.loadTexts:
    cwpanFallingIfRplTblMinorThreshNodesNotif.setStatus(
        "current"
    )

cwpanRisingIfRplTblMajorThreshNodesNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 0, 5)
)
cwpanRisingIfRplTblMajorThreshNodesNotif.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableNodes"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableMajorThreshNodes"))
)
if mibBuilder.loadTexts:
    cwpanRisingIfRplTblMajorThreshNodesNotif.setStatus(
        "current"
    )

cwpanFallingIfRplTblMajorThreshNodesNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 0, 6)
)
cwpanFallingIfRplTblMajorThreshNodesNotif.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableNodes"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableMajorThreshNodes"))
)
if mibBuilder.loadTexts:
    cwpanFallingIfRplTblMajorThreshNodesNotif.setStatus(
        "current"
    )


# Notifications groups

cwpanNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 2, 2, 3)
)
cwpanNotificationGroup.setObjects(
      *(("CISCO-WPAN-MIB", "cwpanServiceStatusChangeNotif"),
        ("CISCO-WPAN-MIB", "cwpanRplTableResetNotif"),
        ("CISCO-WPAN-MIB", "cwpanRisingIfRplTblMinorThreshNodesNotif"),
        ("CISCO-WPAN-MIB", "cwpanFallingIfRplTblMinorThreshNodesNotif"),
        ("CISCO-WPAN-MIB", "cwpanRisingIfRplTblMajorThreshNodesNotif"),
        ("CISCO-WPAN-MIB", "cwpanFallingIfRplTblMajorThreshNodesNotif"))
)
if mibBuilder.loadTexts:
    cwpanNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoWpanMIBModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoWpanMIBModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WPAN-MIB",
    **{"ciscoWpanMIB": ciscoWpanMIB,
       "ciscoWpanMIBNotifs": ciscoWpanMIBNotifs,
       "cwpanServiceStatusChangeNotif": cwpanServiceStatusChangeNotif,
       "cwpanRplTableResetNotif": cwpanRplTableResetNotif,
       "cwpanRisingIfRplTblMinorThreshNodesNotif": cwpanRisingIfRplTblMinorThreshNodesNotif,
       "cwpanFallingIfRplTblMinorThreshNodesNotif": cwpanFallingIfRplTblMinorThreshNodesNotif,
       "cwpanRisingIfRplTblMajorThreshNodesNotif": cwpanRisingIfRplTblMajorThreshNodesNotif,
       "cwpanFallingIfRplTblMajorThreshNodesNotif": cwpanFallingIfRplTblMajorThreshNodesNotif,
       "ciscoWpanMIBObjects": ciscoWpanMIBObjects,
       "ciscoWpanConfig": ciscoWpanConfig,
       "cwpanInterfaceTable": cwpanInterfaceTable,
       "cwpanInterfaceEntry": cwpanInterfaceEntry,
       "cwpanIfServiceStatus": cwpanIfServiceStatus,
       "cwpanIfServiceStatusReason": cwpanIfServiceStatusReason,
       "cwpanIfRplTableResetReason": cwpanIfRplTableResetReason,
       "cwpanIfRplTableNodes": cwpanIfRplTableNodes,
       "cwpanIfRplTableMajorThreshNodes": cwpanIfRplTableMajorThreshNodes,
       "cwpanIfRplTableMinorThreshNodes": cwpanIfRplTableMinorThreshNodes,
       "cwpanNotificationEnable": cwpanNotificationEnable,
       "ciscoWpanMIBConform": ciscoWpanMIBConform,
       "ciscoWpanMIBCompliances": ciscoWpanMIBCompliances,
       "ciscoWpanMIBModuleCompliance": ciscoWpanMIBModuleCompliance,
       "ciscoWpanMIBGroups": ciscoWpanMIBGroups,
       "cwpanInterfaceInfoGroup": cwpanInterfaceInfoGroup,
       "cwpanNotificationControlGroup": cwpanNotificationControlGroup,
       "cwpanNotificationGroup": cwpanNotificationGroup}
)
