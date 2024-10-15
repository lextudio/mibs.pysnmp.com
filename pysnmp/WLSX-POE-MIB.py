# SNMP MIB module (WLSX-POE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WLSX-POE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:09 2024
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

(wlsxEnterpriseMibModules,) = mibBuilder.importSymbols(
    "ARUBA-MIB",
    "wlsxEnterpriseMibModules")

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

wlsxPoEMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18)
)
wlsxPoEMIB.setRevisions(
        ("2011-05-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlsxPoEMIBNotifications_ObjectIdentity = ObjectIdentity
wlsxPoEMIBNotifications = _WlsxPoEMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 0)
)
_WlsxPoEMIBObjects_ObjectIdentity = ObjectIdentity
wlsxPoEMIBObjects = _WlsxPoEMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 1)
)
_WlsxPsePortTable_Object = MibTable
wlsxPsePortTable = _WlsxPsePortTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 1, 1)
)
if mibBuilder.loadTexts:
    wlsxPsePortTable.setStatus("current")
_WlsxPsePortEntry_Object = MibTableRow
wlsxPsePortEntry = _WlsxPsePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 1, 1, 1)
)
wlsxPsePortEntry.setIndexNames(
    (0, "WLSX-POE-MIB", "wlsxPsePortIndex"),
)
if mibBuilder.loadTexts:
    wlsxPsePortEntry.setStatus("current")
_WlsxPsePortIndex_Type = Integer32
_WlsxPsePortIndex_Object = MibTableColumn
wlsxPsePortIndex = _WlsxPsePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 1, 1, 1, 1),
    _WlsxPsePortIndex_Type()
)
wlsxPsePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlsxPsePortIndex.setStatus("current")


class _WlsxPsePortAdminStatus_Type(Integer32):
    """Custom type wlsxPsePortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WlsxPsePortAdminStatus_Type.__name__ = "Integer32"
_WlsxPsePortAdminStatus_Object = MibTableColumn
wlsxPsePortAdminStatus = _WlsxPsePortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 1, 1, 1, 2),
    _WlsxPsePortAdminStatus_Type()
)
wlsxPsePortAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxPsePortAdminStatus.setStatus("current")


class _WlsxPsePortState_Type(Integer32):
    """Custom type wlsxPsePortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WlsxPsePortState_Type.__name__ = "Integer32"
_WlsxPsePortState_Object = MibTableColumn
wlsxPsePortState = _WlsxPsePortState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 1, 1, 1, 3),
    _WlsxPsePortState_Type()
)
wlsxPsePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxPsePortState.setStatus("current")


class _WlsxPsePortStatus_Type(Integer32):
    """Custom type wlsxPsePortStatus based on Integer32"""
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
        *(("offAdmin", 2),
          ("offDetectionProgress", 5),
          ("offHardwareError", 6),
          ("offIllegalClass", 4),
          ("offNonStandardPd", 7),
          ("offPowerManagement", 3),
          ("unknown", 1))
    )


_WlsxPsePortStatus_Type.__name__ = "Integer32"
_WlsxPsePortStatus_Object = MibTableColumn
wlsxPsePortStatus = _WlsxPsePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 1, 1, 1, 4),
    _WlsxPsePortStatus_Type()
)
wlsxPsePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxPsePortStatus.setStatus("current")


class _WlsxPsePortDiscoveryMode_Type(Integer32):
    """Custom type wlsxPsePortDiscoveryMode based on Integer32"""
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
        *(("cisco", 3),
          ("ieee", 2),
          ("off", 1),
          ("unknown", 0))
    )


_WlsxPsePortDiscoveryMode_Type.__name__ = "Integer32"
_WlsxPsePortDiscoveryMode_Object = MibTableColumn
wlsxPsePortDiscoveryMode = _WlsxPsePortDiscoveryMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 1, 1, 1, 5),
    _WlsxPsePortDiscoveryMode_Type()
)
wlsxPsePortDiscoveryMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxPsePortDiscoveryMode.setStatus("current")
_WlsxPsePortIsPdDetected_Type = TruthValue
_WlsxPsePortIsPdDetected_Object = MibTableColumn
wlsxPsePortIsPdDetected = _WlsxPsePortIsPdDetected_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 1, 1, 1, 6),
    _WlsxPsePortIsPdDetected_Type()
)
wlsxPsePortIsPdDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxPsePortIsPdDetected.setStatus("current")
_WlsxPsePortIsIeeePd_Type = TruthValue
_WlsxPsePortIsIeeePd_Object = MibTableColumn
wlsxPsePortIsIeeePd = _WlsxPsePortIsIeeePd_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 1, 1, 1, 7),
    _WlsxPsePortIsIeeePd_Type()
)
wlsxPsePortIsIeeePd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxPsePortIsIeeePd.setStatus("current")


class _WlsxPsePortPdClass_Type(Integer32):
    """Custom type wlsxPsePortPdClass based on Integer32"""
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5),
          ("unknownClass", 0))
    )


_WlsxPsePortPdClass_Type.__name__ = "Integer32"
_WlsxPsePortPdClass_Object = MibTableColumn
wlsxPsePortPdClass = _WlsxPsePortPdClass_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 1, 1, 1, 8),
    _WlsxPsePortPdClass_Type()
)
wlsxPsePortPdClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxPsePortPdClass.setStatus("current")


class _WlsxPsePortPriority_Type(Integer32):
    """Custom type wlsxPsePortPriority based on Integer32"""
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
          ("high", 2),
          ("low", 1))
    )


_WlsxPsePortPriority_Type.__name__ = "Integer32"
_WlsxPsePortPriority_Object = MibTableColumn
wlsxPsePortPriority = _WlsxPsePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 1, 1, 1, 9),
    _WlsxPsePortPriority_Type()
)
wlsxPsePortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxPsePortPriority.setStatus("current")
_WlsxPsePortDefaultPowerMax_Type = Integer32
_WlsxPsePortDefaultPowerMax_Object = MibTableColumn
wlsxPsePortDefaultPowerMax = _WlsxPsePortDefaultPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 1, 1, 1, 10),
    _WlsxPsePortDefaultPowerMax_Type()
)
wlsxPsePortDefaultPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxPsePortDefaultPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    wlsxPsePortDefaultPowerMax.setUnits("milliwatts")
_WlsxPsePortPowerAllocated_Type = Integer32
_WlsxPsePortPowerAllocated_Object = MibTableColumn
wlsxPsePortPowerAllocated = _WlsxPsePortPowerAllocated_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 1, 1, 1, 11),
    _WlsxPsePortPowerAllocated_Type()
)
wlsxPsePortPowerAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxPsePortPowerAllocated.setStatus("current")
if mibBuilder.loadTexts:
    wlsxPsePortPowerAllocated.setUnits("milliwatts")
_WlsxPsePortPowerConsumed_Type = Integer32
_WlsxPsePortPowerConsumed_Object = MibTableColumn
wlsxPsePortPowerConsumed = _WlsxPsePortPowerConsumed_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 1, 1, 1, 12),
    _WlsxPsePortPowerConsumed_Type()
)
wlsxPsePortPowerConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxPsePortPowerConsumed.setStatus("current")
if mibBuilder.loadTexts:
    wlsxPsePortPowerConsumed.setUnits("milliwatts")
_WlsxPsePortVoltage_Type = Integer32
_WlsxPsePortVoltage_Object = MibTableColumn
wlsxPsePortVoltage = _WlsxPsePortVoltage_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 1, 1, 1, 13),
    _WlsxPsePortVoltage_Type()
)
wlsxPsePortVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxPsePortVoltage.setStatus("current")
if mibBuilder.loadTexts:
    wlsxPsePortVoltage.setUnits("milliVolts")
_WlsxPsePortCurrent_Type = Integer32
_WlsxPsePortCurrent_Object = MibTableColumn
wlsxPsePortCurrent = _WlsxPsePortCurrent_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 1, 1, 1, 14),
    _WlsxPsePortCurrent_Type()
)
wlsxPsePortCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxPsePortCurrent.setStatus("current")
if mibBuilder.loadTexts:
    wlsxPsePortCurrent.setUnits("milliAmps")
_WlsxPseSlotTable_Object = MibTable
wlsxPseSlotTable = _WlsxPseSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 1, 2)
)
if mibBuilder.loadTexts:
    wlsxPseSlotTable.setStatus("current")
_WlsxPseSlotEntry_Object = MibTableRow
wlsxPseSlotEntry = _WlsxPseSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 1, 2, 1)
)
wlsxPseSlotEntry.setIndexNames(
    (0, "WLSX-POE-MIB", "wlsxPseSlotIndex"),
)
if mibBuilder.loadTexts:
    wlsxPseSlotEntry.setStatus("current")
_WlsxPseSlotIndex_Type = Integer32
_WlsxPseSlotIndex_Object = MibTableColumn
wlsxPseSlotIndex = _WlsxPseSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 1, 2, 1, 1),
    _WlsxPseSlotIndex_Type()
)
wlsxPseSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlsxPseSlotIndex.setStatus("current")
_WlsxPseSlotPowerAvailable_Type = Integer32
_WlsxPseSlotPowerAvailable_Object = MibTableColumn
wlsxPseSlotPowerAvailable = _WlsxPseSlotPowerAvailable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 1, 2, 1, 2),
    _WlsxPseSlotPowerAvailable_Type()
)
wlsxPseSlotPowerAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxPseSlotPowerAvailable.setStatus("current")
if mibBuilder.loadTexts:
    wlsxPseSlotPowerAvailable.setUnits("watts")
_WlsxPseSlotPowerConsumption_Type = Integer32
_WlsxPseSlotPowerConsumption_Object = MibTableColumn
wlsxPseSlotPowerConsumption = _WlsxPseSlotPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 1, 2, 1, 3),
    _WlsxPseSlotPowerConsumption_Type()
)
wlsxPseSlotPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxPseSlotPowerConsumption.setStatus("current")
if mibBuilder.loadTexts:
    wlsxPseSlotPowerConsumption.setUnits("watts")
_WlsxPseSlotGuardBand_Type = Integer32
_WlsxPseSlotGuardBand_Object = MibTableColumn
wlsxPseSlotGuardBand = _WlsxPseSlotGuardBand_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 1, 2, 1, 4),
    _WlsxPseSlotGuardBand_Type()
)
wlsxPseSlotGuardBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxPseSlotGuardBand.setStatus("current")


class _WlsxPseSlotPoEManagementMode_Type(Integer32):
    """Custom type wlsxPseSlotPoEManagementMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("class", 3),
          ("dynamic", 1),
          ("static", 2))
    )


_WlsxPseSlotPoEManagementMode_Type.__name__ = "Integer32"
_WlsxPseSlotPoEManagementMode_Object = MibTableColumn
wlsxPseSlotPoEManagementMode = _WlsxPseSlotPoEManagementMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 1, 2, 1, 5),
    _WlsxPseSlotPoEManagementMode_Type()
)
wlsxPseSlotPoEManagementMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxPseSlotPoEManagementMode.setStatus("current")
_WlsxPoEMIBConformance_ObjectIdentity = ObjectIdentity
wlsxPoEMIBConformance = _WlsxPoEMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 2)
)
_WlsxPoEMIBCompliances_ObjectIdentity = ObjectIdentity
wlsxPoEMIBCompliances = _WlsxPoEMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 2, 1)
)
_WlsxPoEMIBGroups_ObjectIdentity = ObjectIdentity
wlsxPoEMIBGroups = _WlsxPoEMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 2, 2)
)

# Managed Objects groups

wlsxPoEMIBPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 2, 2, 1)
)
wlsxPoEMIBPortGroup.setObjects(
      *(("WLSX-POE-MIB", "wlsxPsePortAdminStatus"),
        ("WLSX-POE-MIB", "wlsxPsePortState"),
        ("WLSX-POE-MIB", "wlsxPsePortStatus"),
        ("WLSX-POE-MIB", "wlsxPsePortDiscoveryMode"),
        ("WLSX-POE-MIB", "wlsxPsePortIsPdDetected"),
        ("WLSX-POE-MIB", "wlsxPsePortIsIeeePd"),
        ("WLSX-POE-MIB", "wlsxPsePortPdClass"),
        ("WLSX-POE-MIB", "wlsxPsePortPriority"),
        ("WLSX-POE-MIB", "wlsxPsePortDefaultPowerMax"),
        ("WLSX-POE-MIB", "wlsxPsePortPowerAllocated"),
        ("WLSX-POE-MIB", "wlsxPsePortPowerConsumed"),
        ("WLSX-POE-MIB", "wlsxPsePortVoltage"),
        ("WLSX-POE-MIB", "wlsxPsePortCurrent"))
)
if mibBuilder.loadTexts:
    wlsxPoEMIBPortGroup.setStatus("current")

wlsxPoEMIBMainPseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 2, 2, 2)
)
wlsxPoEMIBMainPseGroup.setObjects(
      *(("WLSX-POE-MIB", "wlsxPseSlotPowerAvailable"),
        ("WLSX-POE-MIB", "wlsxPseSlotPowerConsumption"),
        ("WLSX-POE-MIB", "wlsxPseSlotGuardBand"),
        ("WLSX-POE-MIB", "wlsxPseSlotPoEManagementMode"))
)
if mibBuilder.loadTexts:
    wlsxPoEMIBMainPseGroup.setStatus("current")


# Notification objects

wlsxTrapInterfacePoEState = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 0, 1)
)
wlsxTrapInterfacePoEState.setObjects(
      *(("WLSX-POE-MIB", "wlsxPsePortIndex"),
        ("WLSX-POE-MIB", "wlsxPsePortState"),
        ("WLSX-POE-MIB", "wlsxPsePortStatus"))
)
if mibBuilder.loadTexts:
    wlsxTrapInterfacePoEState.setStatus(
        "current"
    )


# Notifications groups

wlsxPoEMIBNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 2, 2, 3)
)
wlsxPoEMIBNotificationsGroup.setObjects(
    ("WLSX-POE-MIB", "wlsxTrapInterfacePoEState")
)
if mibBuilder.loadTexts:
    wlsxPoEMIBNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

wlsxPoEMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 18, 2, 1, 1)
)
if mibBuilder.loadTexts:
    wlsxPoEMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WLSX-POE-MIB",
    **{"wlsxPoEMIB": wlsxPoEMIB,
       "wlsxPoEMIBNotifications": wlsxPoEMIBNotifications,
       "wlsxTrapInterfacePoEState": wlsxTrapInterfacePoEState,
       "wlsxPoEMIBObjects": wlsxPoEMIBObjects,
       "wlsxPsePortTable": wlsxPsePortTable,
       "wlsxPsePortEntry": wlsxPsePortEntry,
       "wlsxPsePortIndex": wlsxPsePortIndex,
       "wlsxPsePortAdminStatus": wlsxPsePortAdminStatus,
       "wlsxPsePortState": wlsxPsePortState,
       "wlsxPsePortStatus": wlsxPsePortStatus,
       "wlsxPsePortDiscoveryMode": wlsxPsePortDiscoveryMode,
       "wlsxPsePortIsPdDetected": wlsxPsePortIsPdDetected,
       "wlsxPsePortIsIeeePd": wlsxPsePortIsIeeePd,
       "wlsxPsePortPdClass": wlsxPsePortPdClass,
       "wlsxPsePortPriority": wlsxPsePortPriority,
       "wlsxPsePortDefaultPowerMax": wlsxPsePortDefaultPowerMax,
       "wlsxPsePortPowerAllocated": wlsxPsePortPowerAllocated,
       "wlsxPsePortPowerConsumed": wlsxPsePortPowerConsumed,
       "wlsxPsePortVoltage": wlsxPsePortVoltage,
       "wlsxPsePortCurrent": wlsxPsePortCurrent,
       "wlsxPseSlotTable": wlsxPseSlotTable,
       "wlsxPseSlotEntry": wlsxPseSlotEntry,
       "wlsxPseSlotIndex": wlsxPseSlotIndex,
       "wlsxPseSlotPowerAvailable": wlsxPseSlotPowerAvailable,
       "wlsxPseSlotPowerConsumption": wlsxPseSlotPowerConsumption,
       "wlsxPseSlotGuardBand": wlsxPseSlotGuardBand,
       "wlsxPseSlotPoEManagementMode": wlsxPseSlotPoEManagementMode,
       "wlsxPoEMIBConformance": wlsxPoEMIBConformance,
       "wlsxPoEMIBCompliances": wlsxPoEMIBCompliances,
       "wlsxPoEMIBCompliance": wlsxPoEMIBCompliance,
       "wlsxPoEMIBGroups": wlsxPoEMIBGroups,
       "wlsxPoEMIBPortGroup": wlsxPoEMIBPortGroup,
       "wlsxPoEMIBMainPseGroup": wlsxPoEMIBMainPseGroup,
       "wlsxPoEMIBNotificationsGroup": wlsxPoEMIBNotificationsGroup}
)
