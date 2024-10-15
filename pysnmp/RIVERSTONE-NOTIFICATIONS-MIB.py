# SNMP MIB module (RIVERSTONE-NOTIFICATIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RIVERSTONE-NOTIFICATIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:49 2024
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

(entPhysicalDescr,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalDescr")

(riverstoneMibs,) = mibBuilder.importSymbols(
    "RIVERSTONE-SMI-MIB",
    "riverstoneMibs")

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

rsNotificationsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33)
)
rsNotificationsMib.setRevisions(
        ("2006-01-26 00:00",
         "2005-02-01 00:00",
         "2003-07-23 00:00",
         "2003-06-10 00:00",
         "2002-03-12 00:00",
         "2001-12-07 00:00",
         "2001-05-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsNotifications_ObjectIdentity = ObjectIdentity
rsNotifications = _RsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 1)
)
_RsNotificationControl_ObjectIdentity = ObjectIdentity
rsNotificationControl = _RsNotificationControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 1)
)
_RsEnvNotificationGroup_ObjectIdentity = ObjectIdentity
rsEnvNotificationGroup = _RsEnvNotificationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2)
)
_RsEnvNotifications_ObjectIdentity = ObjectIdentity
rsEnvNotifications = _RsEnvNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0)
)
_RsSyslog2SNMPMapGroup_ObjectIdentity = ObjectIdentity
rsSyslog2SNMPMapGroup = _RsSyslog2SNMPMapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 3)
)
_RsSyslog2SNMPMapNotifications_ObjectIdentity = ObjectIdentity
rsSyslog2SNMPMapNotifications = _RsSyslog2SNMPMapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 3, 0)
)


class _RsS2SModuleId_Type(DisplayString):
    """Custom type rsS2SModuleId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RsS2SModuleId_Type.__name__ = "DisplayString"
_RsS2SModuleId_Object = MibScalar
rsS2SModuleId = _RsS2SModuleId_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 3, 1),
    _RsS2SModuleId_Type()
)
rsS2SModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsS2SModuleId.setStatus("current")


class _RsS2SSeverity_Type(Integer32):
    """Custom type rsS2SSeverity based on Integer32"""
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
        *(("error", 2),
          ("fatal", 1),
          ("information", 4),
          ("warning", 3))
    )


_RsS2SSeverity_Type.__name__ = "Integer32"
_RsS2SSeverity_Object = MibScalar
rsS2SSeverity = _RsS2SSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 3, 2),
    _RsS2SSeverity_Type()
)
rsS2SSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsS2SSeverity.setStatus("current")


class _RsS2SMessage_Type(DisplayString):
    """Custom type rsS2SMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_RsS2SMessage_Type.__name__ = "DisplayString"
_RsS2SMessage_Object = MibScalar
rsS2SMessage = _RsS2SMessage_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 3, 3),
    _RsS2SMessage_Type()
)
rsS2SMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsS2SMessage.setStatus("current")
_RsNotificationConformance_ObjectIdentity = ObjectIdentity
rsNotificationConformance = _RsNotificationConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 2)
)
_RsNotificationCompliances_ObjectIdentity = ObjectIdentity
rsNotificationCompliances = _RsNotificationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 2, 1)
)
_RsEnvNotificationConfGroup_ObjectIdentity = ObjectIdentity
rsEnvNotificationConfGroup = _RsEnvNotificationConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 2, 2)
)
_RsS2SNotificationConfGroup_ObjectIdentity = ObjectIdentity
rsS2SNotificationConfGroup = _RsS2SNotificationConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 2, 3)
)

# Managed Objects groups


# Notification objects

rsEnvirPowerSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0, 1)
)
rsEnvirPowerSupplyFailed.setObjects(
    ("ENTITY-MIB", "entPhysicalDescr")
)
if mibBuilder.loadTexts:
    rsEnvirPowerSupplyFailed.setStatus(
        "current"
    )

rsEnvirPowerSupplyRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0, 2)
)
rsEnvirPowerSupplyRecovered.setObjects(
    ("ENTITY-MIB", "entPhysicalDescr")
)
if mibBuilder.loadTexts:
    rsEnvirPowerSupplyRecovered.setStatus(
        "current"
    )

rsEnvirFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0, 3)
)
rsEnvirFanFailed.setObjects(
    ("ENTITY-MIB", "entPhysicalDescr")
)
if mibBuilder.loadTexts:
    rsEnvirFanFailed.setStatus(
        "current"
    )

rsEnvirFanRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0, 4)
)
rsEnvirFanRecovered.setObjects(
    ("ENTITY-MIB", "entPhysicalDescr")
)
if mibBuilder.loadTexts:
    rsEnvirFanRecovered.setStatus(
        "current"
    )

rsEnvirTempExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0, 5)
)
rsEnvirTempExceeded.setObjects(
    ("ENTITY-MIB", "entPhysicalDescr")
)
if mibBuilder.loadTexts:
    rsEnvirTempExceeded.setStatus(
        "current"
    )

rsEnvirTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0, 6)
)
rsEnvirTempNormal.setObjects(
    ("ENTITY-MIB", "entPhysicalDescr")
)
if mibBuilder.loadTexts:
    rsEnvirTempNormal.setStatus(
        "current"
    )

rsEnvirHotSwapIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0, 7)
)
rsEnvirHotSwapIn.setObjects(
    ("ENTITY-MIB", "entPhysicalDescr")
)
if mibBuilder.loadTexts:
    rsEnvirHotSwapIn.setStatus(
        "current"
    )

rsEnvirHotSwapOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0, 8)
)
rsEnvirHotSwapOut.setObjects(
    ("ENTITY-MIB", "entPhysicalDescr")
)
if mibBuilder.loadTexts:
    rsEnvirHotSwapOut.setStatus(
        "current"
    )

rsEnvirBackupControlModuleOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0, 9)
)
rsEnvirBackupControlModuleOnline.setObjects(
    ("ENTITY-MIB", "entPhysicalDescr")
)
if mibBuilder.loadTexts:
    rsEnvirBackupControlModuleOnline.setStatus(
        "current"
    )

rsEnvirSwitchingFabricFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0, 10)
)
rsEnvirSwitchingFabricFailure.setObjects(
    ("ENTITY-MIB", "entPhysicalDescr")
)
if mibBuilder.loadTexts:
    rsEnvirSwitchingFabricFailure.setStatus(
        "current"
    )

rsEnvirSwitchingFabricFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0, 11)
)
rsEnvirSwitchingFabricFailover.setObjects(
    ("ENTITY-MIB", "entPhysicalDescr")
)
if mibBuilder.loadTexts:
    rsEnvirSwitchingFabricFailover.setStatus(
        "current"
    )

rsEnvirTempTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0, 12)
)
rsEnvirTempTooLow.setObjects(
    ("ENTITY-MIB", "entPhysicalDescr")
)
if mibBuilder.loadTexts:
    rsEnvirTempTooLow.setStatus(
        "current"
    )

rsSyslog2SNMPMap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 3, 0, 1)
)
rsSyslog2SNMPMap.setObjects(
      *(("RIVERSTONE-NOTIFICATIONS-MIB", "rsS2SModuleId"),
        ("RIVERSTONE-NOTIFICATIONS-MIB", "rsS2SSeverity"),
        ("RIVERSTONE-NOTIFICATIONS-MIB", "rsS2SMessage"))
)
if mibBuilder.loadTexts:
    rsSyslog2SNMPMap.setStatus(
        "current"
    )


# Notifications groups

rsNotificationConfGroupV10 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 2, 2, 1)
)
rsNotificationConfGroupV10.setObjects(
      *(("RIVERSTONE-NOTIFICATIONS-MIB", "rsEnvirPowerSupplyFailed"),
        ("RIVERSTONE-NOTIFICATIONS-MIB", "rsEnvirPowerSupplyRecovered"),
        ("RIVERSTONE-NOTIFICATIONS-MIB", "rsEnvirFanFailed"),
        ("RIVERSTONE-NOTIFICATIONS-MIB", "rsEnvirFanRecovered"),
        ("RIVERSTONE-NOTIFICATIONS-MIB", "rsEnvirTempExceeded"),
        ("RIVERSTONE-NOTIFICATIONS-MIB", "rsEnvirTempNormal"),
        ("RIVERSTONE-NOTIFICATIONS-MIB", "rsEnvirHotSwapIn"),
        ("RIVERSTONE-NOTIFICATIONS-MIB", "rsEnvirHotSwapOut"),
        ("RIVERSTONE-NOTIFICATIONS-MIB", "rsEnvirBackupControlModuleOnline"))
)
if mibBuilder.loadTexts:
    rsNotificationConfGroupV10.setStatus(
        "current"
    )

rsNotificationSwitchingFabric = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 2, 2, 2)
)
rsNotificationSwitchingFabric.setObjects(
      *(("RIVERSTONE-NOTIFICATIONS-MIB", "rsEnvirSwitchingFabricFailure"),
        ("RIVERSTONE-NOTIFICATIONS-MIB", "rsEnvirSwitchingFabricFailover"))
)
if mibBuilder.loadTexts:
    rsNotificationSwitchingFabric.setStatus(
        "current"
    )

rsNotificationSyslog2SNMPMap = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 2, 3, 1)
)
rsNotificationSyslog2SNMPMap.setObjects(
    ("RIVERSTONE-NOTIFICATIONS-MIB", "rsSyslog2SNMPMap")
)
if mibBuilder.loadTexts:
    rsNotificationSyslog2SNMPMap.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rsNotificationComplianceV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rsNotificationComplianceV10.setStatus(
        "obsolete"
    )

rsNotificationComplianceV11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 2, 1, 2)
)
if mibBuilder.loadTexts:
    rsNotificationComplianceV11.setStatus(
        "current"
    )

rsNotificationComplianceV12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5567, 2, 33, 2, 1, 3)
)
if mibBuilder.loadTexts:
    rsNotificationComplianceV12.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RIVERSTONE-NOTIFICATIONS-MIB",
    **{"rsNotificationsMib": rsNotificationsMib,
       "rsNotifications": rsNotifications,
       "rsNotificationControl": rsNotificationControl,
       "rsEnvNotificationGroup": rsEnvNotificationGroup,
       "rsEnvNotifications": rsEnvNotifications,
       "rsEnvirPowerSupplyFailed": rsEnvirPowerSupplyFailed,
       "rsEnvirPowerSupplyRecovered": rsEnvirPowerSupplyRecovered,
       "rsEnvirFanFailed": rsEnvirFanFailed,
       "rsEnvirFanRecovered": rsEnvirFanRecovered,
       "rsEnvirTempExceeded": rsEnvirTempExceeded,
       "rsEnvirTempNormal": rsEnvirTempNormal,
       "rsEnvirHotSwapIn": rsEnvirHotSwapIn,
       "rsEnvirHotSwapOut": rsEnvirHotSwapOut,
       "rsEnvirBackupControlModuleOnline": rsEnvirBackupControlModuleOnline,
       "rsEnvirSwitchingFabricFailure": rsEnvirSwitchingFabricFailure,
       "rsEnvirSwitchingFabricFailover": rsEnvirSwitchingFabricFailover,
       "rsEnvirTempTooLow": rsEnvirTempTooLow,
       "rsSyslog2SNMPMapGroup": rsSyslog2SNMPMapGroup,
       "rsSyslog2SNMPMapNotifications": rsSyslog2SNMPMapNotifications,
       "rsSyslog2SNMPMap": rsSyslog2SNMPMap,
       "rsS2SModuleId": rsS2SModuleId,
       "rsS2SSeverity": rsS2SSeverity,
       "rsS2SMessage": rsS2SMessage,
       "rsNotificationConformance": rsNotificationConformance,
       "rsNotificationCompliances": rsNotificationCompliances,
       "rsNotificationComplianceV10": rsNotificationComplianceV10,
       "rsNotificationComplianceV11": rsNotificationComplianceV11,
       "rsNotificationComplianceV12": rsNotificationComplianceV12,
       "rsEnvNotificationConfGroup": rsEnvNotificationConfGroup,
       "rsNotificationConfGroupV10": rsNotificationConfGroupV10,
       "rsNotificationSwitchingFabric": rsNotificationSwitchingFabric,
       "rsS2SNotificationConfGroup": rsS2SNotificationConfGroup,
       "rsNotificationSyslog2SNMPMap": rsNotificationSyslog2SNMPMap}
)
