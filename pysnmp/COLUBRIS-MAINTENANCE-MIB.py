# SNMP MIB module (COLUBRIS-MAINTENANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COLUBRIS-MAINTENANCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:19 2024
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

(colubrisMgmtV2,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisMgmtV2")

(systemConfigurationVersion,
 systemFirmwareRevision) = mibBuilder.importSymbols(
    "COLUBRIS-SYSTEM-MIB",
    "systemConfigurationVersion",
    "systemFirmwareRevision")

(ColubrisNotificationEnable,) = mibBuilder.importSymbols(
    "COLUBRIS-TC",
    "ColubrisNotificationEnable")

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

colubrisMaintenanceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisMaintenanceMIBObjects_ObjectIdentity = ObjectIdentity
colubrisMaintenanceMIBObjects = _ColubrisMaintenanceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1)
)
_FirmwareUpdate_ObjectIdentity = ObjectIdentity
firmwareUpdate = _FirmwareUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1)
)
_FirmwarePeriodicUpdate_Type = TruthValue
_FirmwarePeriodicUpdate_Object = MibScalar
firmwarePeriodicUpdate = _FirmwarePeriodicUpdate_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 1),
    _FirmwarePeriodicUpdate_Type()
)
firmwarePeriodicUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwarePeriodicUpdate.setStatus("current")


class _FirmwareUpdateDay_Type(Integer32):
    """Custom type firmwareUpdateDay based on Integer32"""
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
        *(("everyday", 8),
          ("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 7),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )


_FirmwareUpdateDay_Type.__name__ = "Integer32"
_FirmwareUpdateDay_Object = MibScalar
firmwareUpdateDay = _FirmwareUpdateDay_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 2),
    _FirmwareUpdateDay_Type()
)
firmwareUpdateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareUpdateDay.setStatus("current")


class _FirmwareUpdateTime_Type(OctetString):
    """Custom type firmwareUpdateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_FirmwareUpdateTime_Type.__name__ = "OctetString"
_FirmwareUpdateTime_Object = MibScalar
firmwareUpdateTime = _FirmwareUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 3),
    _FirmwareUpdateTime_Type()
)
firmwareUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareUpdateTime.setStatus("current")
_FirmwareUpdateLocation_Type = DisplayString
_FirmwareUpdateLocation_Object = MibScalar
firmwareUpdateLocation = _FirmwareUpdateLocation_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 4),
    _FirmwareUpdateLocation_Type()
)
firmwareUpdateLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareUpdateLocation.setStatus("current")


class _FirmwareUpdateInitiate_Type(Integer32):
    """Custom type firmwareUpdateInitiate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("update", 1))
    )


_FirmwareUpdateInitiate_Type.__name__ = "Integer32"
_FirmwareUpdateInitiate_Object = MibScalar
firmwareUpdateInitiate = _FirmwareUpdateInitiate_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 5),
    _FirmwareUpdateInitiate_Type()
)
firmwareUpdateInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareUpdateInitiate.setStatus("current")


class _FirmwareUpdateNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type firmwareUpdateNotificationEnabled based on ColubrisNotificationEnable"""


_FirmwareUpdateNotificationEnabled_Object = MibScalar
firmwareUpdateNotificationEnabled = _FirmwareUpdateNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 6),
    _FirmwareUpdateNotificationEnabled_Type()
)
firmwareUpdateNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareUpdateNotificationEnabled.setStatus("current")
_FirmwareUpdateInfo_Type = DisplayString
_FirmwareUpdateInfo_Object = MibScalar
firmwareUpdateInfo = _FirmwareUpdateInfo_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 7),
    _FirmwareUpdateInfo_Type()
)
firmwareUpdateInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareUpdateInfo.setStatus("current")


class _FirmwareUpdateStatus_Type(Integer32):
    """Custom type firmwareUpdateStatus based on Integer32"""
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
        *(("failure", 4),
          ("idle", 1),
          ("inprogress", 2),
          ("success", 3))
    )


_FirmwareUpdateStatus_Type.__name__ = "Integer32"
_FirmwareUpdateStatus_Object = MibScalar
firmwareUpdateStatus = _FirmwareUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 8),
    _FirmwareUpdateStatus_Type()
)
firmwareUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareUpdateStatus.setStatus("current")
_ConfigurationUpdate_ObjectIdentity = ObjectIdentity
configurationUpdate = _ConfigurationUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2)
)
_ConfigurationPeriodicUpdate_Type = TruthValue
_ConfigurationPeriodicUpdate_Object = MibScalar
configurationPeriodicUpdate = _ConfigurationPeriodicUpdate_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 1),
    _ConfigurationPeriodicUpdate_Type()
)
configurationPeriodicUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationPeriodicUpdate.setStatus("current")


class _ConfigurationUpdateDay_Type(Integer32):
    """Custom type configurationUpdateDay based on Integer32"""
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
        *(("everyday", 8),
          ("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 7),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )


_ConfigurationUpdateDay_Type.__name__ = "Integer32"
_ConfigurationUpdateDay_Object = MibScalar
configurationUpdateDay = _ConfigurationUpdateDay_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 2),
    _ConfigurationUpdateDay_Type()
)
configurationUpdateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationUpdateDay.setStatus("current")


class _ConfigurationUpdateTime_Type(OctetString):
    """Custom type configurationUpdateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_ConfigurationUpdateTime_Type.__name__ = "OctetString"
_ConfigurationUpdateTime_Object = MibScalar
configurationUpdateTime = _ConfigurationUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 3),
    _ConfigurationUpdateTime_Type()
)
configurationUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationUpdateTime.setStatus("current")
_ConfigurationUpdateLocation_Type = DisplayString
_ConfigurationUpdateLocation_Object = MibScalar
configurationUpdateLocation = _ConfigurationUpdateLocation_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 4),
    _ConfigurationUpdateLocation_Type()
)
configurationUpdateLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationUpdateLocation.setStatus("current")


class _ConfigurationUpdateInitiate_Type(Integer32):
    """Custom type configurationUpdateInitiate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("update", 1))
    )


_ConfigurationUpdateInitiate_Type.__name__ = "Integer32"
_ConfigurationUpdateInitiate_Object = MibScalar
configurationUpdateInitiate = _ConfigurationUpdateInitiate_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 5),
    _ConfigurationUpdateInitiate_Type()
)
configurationUpdateInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationUpdateInitiate.setStatus("current")


class _ConfigurationUpdateOperation_Type(Integer32):
    """Custom type configurationUpdateOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("restore", 2))
    )


_ConfigurationUpdateOperation_Type.__name__ = "Integer32"
_ConfigurationUpdateOperation_Object = MibScalar
configurationUpdateOperation = _ConfigurationUpdateOperation_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 6),
    _ConfigurationUpdateOperation_Type()
)
configurationUpdateOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationUpdateOperation.setStatus("current")


class _ConfigurationUpdateNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type configurationUpdateNotificationEnabled based on ColubrisNotificationEnable"""


_ConfigurationUpdateNotificationEnabled_Object = MibScalar
configurationUpdateNotificationEnabled = _ConfigurationUpdateNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 7),
    _ConfigurationUpdateNotificationEnabled_Type()
)
configurationUpdateNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationUpdateNotificationEnabled.setStatus("current")


class _ConfigurationLocalUpdateNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type configurationLocalUpdateNotificationEnabled based on ColubrisNotificationEnable"""


_ConfigurationLocalUpdateNotificationEnabled_Object = MibScalar
configurationLocalUpdateNotificationEnabled = _ConfigurationLocalUpdateNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 8),
    _ConfigurationLocalUpdateNotificationEnabled_Type()
)
configurationLocalUpdateNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationLocalUpdateNotificationEnabled.setStatus("current")
_ConfigurationUpdateInfo_Type = DisplayString
_ConfigurationUpdateInfo_Object = MibScalar
configurationUpdateInfo = _ConfigurationUpdateInfo_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 9),
    _ConfigurationUpdateInfo_Type()
)
configurationUpdateInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurationUpdateInfo.setStatus("current")


class _ConfigurationFactoryDefaults_Type(Integer32):
    """Custom type configurationFactoryDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("resetToFactoryDefaults", 1))
    )


_ConfigurationFactoryDefaults_Type.__name__ = "Integer32"
_ConfigurationFactoryDefaults_Object = MibScalar
configurationFactoryDefaults = _ConfigurationFactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 10),
    _ConfigurationFactoryDefaults_Type()
)
configurationFactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationFactoryDefaults.setStatus("current")


class _ConfigurationRestart_Type(Integer32):
    """Custom type configurationRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("restart", 1))
    )


_ConfigurationRestart_Type.__name__ = "Integer32"
_ConfigurationRestart_Object = MibScalar
configurationRestart = _ConfigurationRestart_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 11),
    _ConfigurationRestart_Type()
)
configurationRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationRestart.setStatus("current")


class _ConfigurationUpdateStatus_Type(Integer32):
    """Custom type configurationUpdateStatus based on Integer32"""
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
        *(("failure", 4),
          ("idle", 1),
          ("inprogress", 2),
          ("success", 3))
    )


_ConfigurationUpdateStatus_Type.__name__ = "Integer32"
_ConfigurationUpdateStatus_Object = MibScalar
configurationUpdateStatus = _ConfigurationUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 12),
    _ConfigurationUpdateStatus_Type()
)
configurationUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurationUpdateStatus.setStatus("current")
_Certificate_ObjectIdentity = ObjectIdentity
certificate = _Certificate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 3)
)


class _CertificateAboutToExpireNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type certificateAboutToExpireNotificationEnabled based on ColubrisNotificationEnable"""


_CertificateAboutToExpireNotificationEnabled_Object = MibScalar
certificateAboutToExpireNotificationEnabled = _CertificateAboutToExpireNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 3, 1),
    _CertificateAboutToExpireNotificationEnabled_Type()
)
certificateAboutToExpireNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certificateAboutToExpireNotificationEnabled.setStatus("current")


class _CertificateExpiredNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type certificateExpiredNotificationEnabled based on ColubrisNotificationEnable"""


_CertificateExpiredNotificationEnabled_Object = MibScalar
certificateExpiredNotificationEnabled = _CertificateExpiredNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 3, 2),
    _CertificateExpiredNotificationEnabled_Type()
)
certificateExpiredNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certificateExpiredNotificationEnabled.setStatus("current")
_CertificateExpiryDate_Type = DisplayString
_CertificateExpiryDate_Object = MibScalar
certificateExpiryDate = _CertificateExpiryDate_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 3, 3),
    _CertificateExpiryDate_Type()
)
certificateExpiryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateExpiryDate.setStatus("current")
_ColubrisMaintenanceMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
colubrisMaintenanceMIBNotificationPrefix = _ColubrisMaintenanceMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 2)
)
_ColubrisMaintenanceMIBNotifications_ObjectIdentity = ObjectIdentity
colubrisMaintenanceMIBNotifications = _ColubrisMaintenanceMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 2, 0)
)
_ColubrisMaintenanceMIBConformance_ObjectIdentity = ObjectIdentity
colubrisMaintenanceMIBConformance = _ColubrisMaintenanceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 3)
)
_ColubrisMaintenanceMIBCompliances_ObjectIdentity = ObjectIdentity
colubrisMaintenanceMIBCompliances = _ColubrisMaintenanceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 3, 1)
)
_ColubrisMaintenanceMIBGroups_ObjectIdentity = ObjectIdentity
colubrisMaintenanceMIBGroups = _ColubrisMaintenanceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 3, 2)
)

# Managed Objects groups

colubrisMaintenanceMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 3, 2, 1)
)
colubrisMaintenanceMIBGroup.setObjects(
      *(("COLUBRIS-MAINTENANCE-MIB", "firmwarePeriodicUpdate"),
        ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateDay"),
        ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateTime"),
        ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateLocation"),
        ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateInitiate"),
        ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateNotificationEnabled"),
        ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateInfo"),
        ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateStatus"),
        ("COLUBRIS-MAINTENANCE-MIB", "configurationPeriodicUpdate"),
        ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateDay"),
        ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateTime"),
        ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateLocation"),
        ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateInitiate"),
        ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateOperation"),
        ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateNotificationEnabled"),
        ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateInfo"),
        ("COLUBRIS-MAINTENANCE-MIB", "configurationFactoryDefaults"),
        ("COLUBRIS-MAINTENANCE-MIB", "configurationRestart"),
        ("COLUBRIS-MAINTENANCE-MIB", "configurationLocalUpdateNotificationEnabled"),
        ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateStatus"),
        ("COLUBRIS-MAINTENANCE-MIB", "certificateAboutToExpireNotificationEnabled"),
        ("COLUBRIS-MAINTENANCE-MIB", "certificateExpiredNotificationEnabled"),
        ("COLUBRIS-MAINTENANCE-MIB", "certificateExpiryDate"))
)
if mibBuilder.loadTexts:
    colubrisMaintenanceMIBGroup.setStatus("current")


# Notification objects

configurationUpdateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 2, 0, 1)
)
configurationUpdateNotification.setObjects(
      *(("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateInfo"),
        ("COLUBRIS-SYSTEM-MIB", "systemConfigurationVersion"))
)
if mibBuilder.loadTexts:
    configurationUpdateNotification.setStatus(
        "current"
    )

configurationLocalUpdateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 2, 0, 2)
)
configurationLocalUpdateNotification.setObjects(
    ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateInfo")
)
if mibBuilder.loadTexts:
    configurationLocalUpdateNotification.setStatus(
        "current"
    )

certificateAboutToExpireNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 2, 0, 3)
)
certificateAboutToExpireNotification.setObjects(
    ("COLUBRIS-MAINTENANCE-MIB", "certificateExpiryDate")
)
if mibBuilder.loadTexts:
    certificateAboutToExpireNotification.setStatus(
        "current"
    )

certificateExpiredNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 2, 0, 4)
)
certificateExpiredNotification.setObjects(
    ("COLUBRIS-MAINTENANCE-MIB", "certificateExpiryDate")
)
if mibBuilder.loadTexts:
    certificateExpiredNotification.setStatus(
        "current"
    )

firmwareUpdateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 2, 0, 5)
)
firmwareUpdateNotification.setObjects(
      *(("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateInfo"),
        ("COLUBRIS-SYSTEM-MIB", "systemFirmwareRevision"))
)
if mibBuilder.loadTexts:
    firmwareUpdateNotification.setStatus(
        "current"
    )


# Notifications groups

colubrisMaintenanceNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 3, 2, 2)
)
colubrisMaintenanceNotificationGroup.setObjects(
      *(("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateNotification"),
        ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateNotification"),
        ("COLUBRIS-MAINTENANCE-MIB", "configurationLocalUpdateNotification"),
        ("COLUBRIS-MAINTENANCE-MIB", "certificateAboutToExpireNotification"),
        ("COLUBRIS-MAINTENANCE-MIB", "certificateExpiredNotification"))
)
if mibBuilder.loadTexts:
    colubrisMaintenanceNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

colubrisMaintenanceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    colubrisMaintenanceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-MAINTENANCE-MIB",
    **{"colubrisMaintenanceMIB": colubrisMaintenanceMIB,
       "colubrisMaintenanceMIBObjects": colubrisMaintenanceMIBObjects,
       "firmwareUpdate": firmwareUpdate,
       "firmwarePeriodicUpdate": firmwarePeriodicUpdate,
       "firmwareUpdateDay": firmwareUpdateDay,
       "firmwareUpdateTime": firmwareUpdateTime,
       "firmwareUpdateLocation": firmwareUpdateLocation,
       "firmwareUpdateInitiate": firmwareUpdateInitiate,
       "firmwareUpdateNotificationEnabled": firmwareUpdateNotificationEnabled,
       "firmwareUpdateInfo": firmwareUpdateInfo,
       "firmwareUpdateStatus": firmwareUpdateStatus,
       "configurationUpdate": configurationUpdate,
       "configurationPeriodicUpdate": configurationPeriodicUpdate,
       "configurationUpdateDay": configurationUpdateDay,
       "configurationUpdateTime": configurationUpdateTime,
       "configurationUpdateLocation": configurationUpdateLocation,
       "configurationUpdateInitiate": configurationUpdateInitiate,
       "configurationUpdateOperation": configurationUpdateOperation,
       "configurationUpdateNotificationEnabled": configurationUpdateNotificationEnabled,
       "configurationLocalUpdateNotificationEnabled": configurationLocalUpdateNotificationEnabled,
       "configurationUpdateInfo": configurationUpdateInfo,
       "configurationFactoryDefaults": configurationFactoryDefaults,
       "configurationRestart": configurationRestart,
       "configurationUpdateStatus": configurationUpdateStatus,
       "certificate": certificate,
       "certificateAboutToExpireNotificationEnabled": certificateAboutToExpireNotificationEnabled,
       "certificateExpiredNotificationEnabled": certificateExpiredNotificationEnabled,
       "certificateExpiryDate": certificateExpiryDate,
       "colubrisMaintenanceMIBNotificationPrefix": colubrisMaintenanceMIBNotificationPrefix,
       "colubrisMaintenanceMIBNotifications": colubrisMaintenanceMIBNotifications,
       "configurationUpdateNotification": configurationUpdateNotification,
       "configurationLocalUpdateNotification": configurationLocalUpdateNotification,
       "certificateAboutToExpireNotification": certificateAboutToExpireNotification,
       "certificateExpiredNotification": certificateExpiredNotification,
       "firmwareUpdateNotification": firmwareUpdateNotification,
       "colubrisMaintenanceMIBConformance": colubrisMaintenanceMIBConformance,
       "colubrisMaintenanceMIBCompliances": colubrisMaintenanceMIBCompliances,
       "colubrisMaintenanceMIBCompliance": colubrisMaintenanceMIBCompliance,
       "colubrisMaintenanceMIBGroups": colubrisMaintenanceMIBGroups,
       "colubrisMaintenanceMIBGroup": colubrisMaintenanceMIBGroup,
       "colubrisMaintenanceNotificationGroup": colubrisMaintenanceNotificationGroup}
)
