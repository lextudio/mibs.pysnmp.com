# SNMP MIB module (HP-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:06 2024
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

(hpProcurveCommon,) = mibBuilder.importSymbols(
    "HP-BASE-MIB",
    "hpProcurveCommon")

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

hpProcurveSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1)
)
hpProcurveSystem.setRevisions(
        ("2005-02-01 14:55",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpSystemTraps_ObjectIdentity = ObjectIdentity
hpSystemTraps = _HpSystemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 0)
)
_HpProcurveSysMib_ObjectIdentity = ObjectIdentity
hpProcurveSysMib = _HpProcurveSysMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 1)
)
_HpProductDescription_Type = OctetString
_HpProductDescription_Object = MibScalar
hpProductDescription = _HpProductDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 1, 1),
    _HpProductDescription_Type()
)
hpProductDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpProductDescription.setStatus("current")
_HpProductHWVersion_Type = OctetString
_HpProductHWVersion_Object = MibScalar
hpProductHWVersion = _HpProductHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 1, 2),
    _HpProductHWVersion_Type()
)
hpProductHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpProductHWVersion.setStatus("current")
_HpProductSWVersion_Type = OctetString
_HpProductSWVersion_Object = MibScalar
hpProductSWVersion = _HpProductSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 1, 3),
    _HpProductSWVersion_Type()
)
hpProductSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpProductSWVersion.setStatus("current")
_HpProductSerialNumber_Type = OctetString
_HpProductSerialNumber_Object = MibScalar
hpProductSerialNumber = _HpProductSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 1, 4),
    _HpProductSerialNumber_Type()
)
hpProductSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpProductSerialNumber.setStatus("current")
_HpProductLastChange_Type = OctetString
_HpProductLastChange_Object = MibScalar
hpProductLastChange = _HpProductLastChange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 1, 5),
    _HpProductLastChange_Type()
)
hpProductLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpProductLastChange.setStatus("current")
_HpCpuTemperature_Type = OctetString
_HpCpuTemperature_Object = MibScalar
hpCpuTemperature = _HpCpuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 1, 6),
    _HpCpuTemperature_Type()
)
hpCpuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpCpuTemperature.setStatus("current")
_HpPowerSupplyTemperature_Type = OctetString
_HpPowerSupplyTemperature_Object = MibScalar
hpPowerSupplyTemperature = _HpPowerSupplyTemperature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 1, 7),
    _HpPowerSupplyTemperature_Type()
)
hpPowerSupplyTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpPowerSupplyTemperature.setStatus("deprecated")
_HpChassisTemperature_Type = OctetString
_HpChassisTemperature_Object = MibScalar
hpChassisTemperature = _HpChassisTemperature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 1, 8),
    _HpChassisTemperature_Type()
)
hpChassisTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpChassisTemperature.setStatus("current")
_HpFanStatusTable_Object = MibTable
hpFanStatusTable = _HpFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    hpFanStatusTable.setStatus("current")
_HpFanStatusEntry_Object = MibTableRow
hpFanStatusEntry = _HpFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 1, 9, 1)
)
hpFanStatusEntry.setIndexNames(
    (0, "HP-SYSTEM-MIB", "hpFanNumber"),
)
if mibBuilder.loadTexts:
    hpFanStatusEntry.setStatus("current")


class _HpFanNumber_Type(Integer32):
    """Custom type hpFanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cpu", 1),
          ("power", 2))
    )


_HpFanNumber_Type.__name__ = "Integer32"
_HpFanNumber_Object = MibTableColumn
hpFanNumber = _HpFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 1, 9, 1, 1),
    _HpFanNumber_Type()
)
hpFanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFanNumber.setStatus("current")


class _HpFanOperational_Type(Integer32):
    """Custom type hpFanOperational based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HpFanOperational_Type.__name__ = "Integer32"
_HpFanOperational_Object = MibTableColumn
hpFanOperational = _HpFanOperational_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 1, 9, 1, 2),
    _HpFanOperational_Type()
)
hpFanOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFanOperational.setStatus("current")
_HpFanSpeed_Type = Integer32
_HpFanSpeed_Object = MibTableColumn
hpFanSpeed = _HpFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 1, 9, 1, 3),
    _HpFanSpeed_Type()
)
hpFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFanSpeed.setStatus("current")
_HpSystemMIBObjects_ObjectIdentity = ObjectIdentity
hpSystemMIBObjects = _HpSystemMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 2)
)
_HpConfig_ObjectIdentity = ObjectIdentity
hpConfig = _HpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 2, 1)
)


class _HpName_Type(DisplayString):
    """Custom type hpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpName_Type.__name__ = "DisplayString"
_HpName_Object = MibScalar
hpName = _HpName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 2, 1, 2),
    _HpName_Type()
)
hpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpName.setStatus("current")


class _HpSystemID_Type(OctetString):
    """Custom type hpSystemID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpSystemID_Type.__name__ = "OctetString"
_HpSystemID_Object = MibScalar
hpSystemID = _HpSystemID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 2, 1, 3),
    _HpSystemID_Type()
)
hpSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSystemID.setStatus("current")


class _HpState_Type(Integer32):
    """Custom type hpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("primary", 4),
          ("secondary", 5),
          ("unknown", 1),
          ("up", 2))
    )


_HpState_Type.__name__ = "Integer32"
_HpState_Object = MibScalar
hpState = _HpState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 2, 1, 4),
    _HpState_Type()
)
hpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpState.setStatus("current")


class _HpDistributionType_Type(Integer32):
    """Custom type hpDistributionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rightsPush", 2),
          ("unknown", 1))
    )


_HpDistributionType_Type.__name__ = "Integer32"
_HpDistributionType_Object = MibScalar
hpDistributionType = _HpDistributionType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 2, 1, 5),
    _HpDistributionType_Type()
)
hpDistributionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDistributionType.setStatus("current")


class _HpDistributionStatus_Type(Integer32):
    """Custom type hpDistributionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("succeeded", 2),
          ("unknown", 1))
    )


_HpDistributionStatus_Type.__name__ = "Integer32"
_HpDistributionStatus_Object = MibScalar
hpDistributionStatus = _HpDistributionStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 2, 1, 6),
    _HpDistributionStatus_Type()
)
hpDistributionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDistributionStatus.setStatus("current")
_HpIpAddress_Type = IpAddress
_HpIpAddress_Object = MibScalar
hpIpAddress = _HpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 2, 1, 7),
    _HpIpAddress_Type()
)
hpIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpIpAddress.setStatus("current")
_HpPeerIpAddress_Type = IpAddress
_HpPeerIpAddress_Object = MibScalar
hpPeerIpAddress = _HpPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 2, 1, 8),
    _HpPeerIpAddress_Type()
)
hpPeerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpPeerIpAddress.setStatus("current")


class _HpTechSupportEnabled_Type(TruthValue):
    """Custom type hpTechSupportEnabled based on TruthValue"""


_HpTechSupportEnabled_Object = MibScalar
hpTechSupportEnabled = _HpTechSupportEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 2, 1, 9),
    _HpTechSupportEnabled_Type()
)
hpTechSupportEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpTechSupportEnabled.setStatus("current")
_HpFailedAdminIpAddress_Type = IpAddress
_HpFailedAdminIpAddress_Object = MibScalar
hpFailedAdminIpAddress = _HpFailedAdminIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 2, 1, 10),
    _HpFailedAdminIpAddress_Type()
)
hpFailedAdminIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFailedAdminIpAddress.setStatus("current")
_HpStatus_ObjectIdentity = ObjectIdentity
hpStatus = _HpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 2, 2)
)
_HpNumAccessControllers_Type = Unsigned32
_HpNumAccessControllers_Object = MibScalar
hpNumAccessControllers = _HpNumAccessControllers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 2, 2, 1),
    _HpNumAccessControllers_Type()
)
hpNumAccessControllers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpNumAccessControllers.setStatus("current")
_HpNumClients_Type = Gauge32
_HpNumClients_Object = MibScalar
hpNumClients = _HpNumClients_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 2, 2, 2),
    _HpNumClients_Type()
)
hpNumClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpNumClients.setStatus("current")
_HpNotificationsConfig_ObjectIdentity = ObjectIdentity
hpNotificationsConfig = _HpNotificationsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 2, 3)
)
_HpFailoverNotificationEnabled_Type = TruthValue
_HpFailoverNotificationEnabled_Object = MibScalar
hpFailoverNotificationEnabled = _HpFailoverNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 2, 3, 1),
    _HpFailoverNotificationEnabled_Type()
)
hpFailoverNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpFailoverNotificationEnabled.setStatus("current")


class _HpDistributionNotificationEnabled_Type(TruthValue):
    """Custom type hpDistributionNotificationEnabled based on TruthValue"""


_HpDistributionNotificationEnabled_Object = MibScalar
hpDistributionNotificationEnabled = _HpDistributionNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 2, 3, 2),
    _HpDistributionNotificationEnabled_Type()
)
hpDistributionNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpDistributionNotificationEnabled.setStatus("current")


class _HpAdminAuthFailureNotificationEnabled_Type(TruthValue):
    """Custom type hpAdminAuthFailureNotificationEnabled based on TruthValue"""


_HpAdminAuthFailureNotificationEnabled_Object = MibScalar
hpAdminAuthFailureNotificationEnabled = _HpAdminAuthFailureNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 2, 3, 3),
    _HpAdminAuthFailureNotificationEnabled_Type()
)
hpAdminAuthFailureNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpAdminAuthFailureNotificationEnabled.setStatus("current")
_HpSystemMIBConformance_ObjectIdentity = ObjectIdentity
hpSystemMIBConformance = _HpSystemMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 3)
)
_HpCompliances_ObjectIdentity = ObjectIdentity
hpCompliances = _HpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 3, 1)
)
_HpGroups_ObjectIdentity = ObjectIdentity
hpGroups = _HpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 3, 2)
)

# Managed Objects groups

hpSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 3, 2, 1)
)
hpSystemGroup.setObjects(
      *(("HP-SYSTEM-MIB", "hpProductDescription"),
        ("HP-SYSTEM-MIB", "hpProductHWVersion"),
        ("HP-SYSTEM-MIB", "hpProductSWVersion"),
        ("HP-SYSTEM-MIB", "hpProductSerialNumber"),
        ("HP-SYSTEM-MIB", "hpProductLastChange"))
)
if mibBuilder.loadTexts:
    hpSystemGroup.setStatus("current")

hpEnvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 3, 2, 2)
)
hpEnvGroup.setObjects(
      *(("HP-SYSTEM-MIB", "hpCpuTemperature"),
        ("HP-SYSTEM-MIB", "hpPowerSupplyTemperature"),
        ("HP-SYSTEM-MIB", "hpChassisTemperature"),
        ("HP-SYSTEM-MIB", "hpFanNumber"),
        ("HP-SYSTEM-MIB", "hpFanOperational"),
        ("HP-SYSTEM-MIB", "hpFanSpeed"))
)
if mibBuilder.loadTexts:
    hpEnvGroup.setStatus("current")

hpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 3, 2, 3)
)
hpConfigGroup.setObjects(
      *(("HP-SYSTEM-MIB", "hpName"),
        ("HP-SYSTEM-MIB", "hpSystemID"),
        ("HP-SYSTEM-MIB", "hpState"),
        ("HP-SYSTEM-MIB", "hpIpAddress"),
        ("HP-SYSTEM-MIB", "hpPeerIpAddress"),
        ("HP-SYSTEM-MIB", "hpTechSupportEnabled"),
        ("HP-SYSTEM-MIB", "hpDistributionType"),
        ("HP-SYSTEM-MIB", "hpDistributionStatus"),
        ("HP-SYSTEM-MIB", "hpFailedAdminIpAddress"))
)
if mibBuilder.loadTexts:
    hpConfigGroup.setStatus("current")

hpStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 3, 2, 4)
)
hpStatusGroup.setObjects(
      *(("HP-SYSTEM-MIB", "hpNumAccessControllers"),
        ("HP-SYSTEM-MIB", "hpNumClients"))
)
if mibBuilder.loadTexts:
    hpStatusGroup.setStatus("current")

hpNotificationsConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 3, 2, 5)
)
hpNotificationsConfigGroup.setObjects(
      *(("HP-SYSTEM-MIB", "hpFailoverNotificationEnabled"),
        ("HP-SYSTEM-MIB", "hpDistributionNotificationEnabled"),
        ("HP-SYSTEM-MIB", "hpAdminAuthFailureNotificationEnabled"))
)
if mibBuilder.loadTexts:
    hpNotificationsConfigGroup.setStatus("current")


# Notification objects

fanDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 0, 1)
)
fanDown.setObjects(
    ("HP-SYSTEM-MIB", "hpFanNumber")
)
if mibBuilder.loadTexts:
    fanDown.setStatus(
        "current"
    )

fanUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 0, 2)
)
fanUp.setObjects(
    ("HP-SYSTEM-MIB", "hpFanNumber")
)
if mibBuilder.loadTexts:
    fanUp.setStatus(
        "current"
    )

temperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 0, 3)
)
temperatureAlarm.setObjects(
    ("HP-SYSTEM-MIB", "hpCpuTemperature")
)
if mibBuilder.loadTexts:
    temperatureAlarm.setStatus(
        "current"
    )

hpFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 0, 4)
)
hpFailover.setObjects(
    ("HP-SYSTEM-MIB", "hpIpAddress")
)
if mibBuilder.loadTexts:
    hpFailover.setStatus(
        "current"
    )

hpDistributionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 0, 5)
)
hpDistributionEvent.setObjects(
      *(("HP-SYSTEM-MIB", "hpDistributionType"),
        ("HP-SYSTEM-MIB", "hpDistributionStatus"))
)
if mibBuilder.loadTexts:
    hpDistributionEvent.setStatus(
        "current"
    )

hpAdminAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 0, 6)
)
hpAdminAuthFailure.setObjects(
    ("HP-SYSTEM-MIB", "hpFailedAdminIpAddress")
)
if mibBuilder.loadTexts:
    hpAdminAuthFailure.setStatus(
        "current"
    )


# Notifications groups

hpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 3, 2, 6)
)
hpNotificationsGroup.setObjects(
      *(("HP-SYSTEM-MIB", "fanDown"),
        ("HP-SYSTEM-MIB", "fanUp"),
        ("HP-SYSTEM-MIB", "temperatureAlarm"),
        ("HP-SYSTEM-MIB", "hpFailover"),
        ("HP-SYSTEM-MIB", "hpDistributionEvent"),
        ("HP-SYSTEM-MIB", "hpAdminAuthFailure"))
)
if mibBuilder.loadTexts:
    hpNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpSystemMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpSystemMIBCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-SYSTEM-MIB",
    **{"hpProcurveSystem": hpProcurveSystem,
       "hpSystemTraps": hpSystemTraps,
       "fanDown": fanDown,
       "fanUp": fanUp,
       "temperatureAlarm": temperatureAlarm,
       "hpFailover": hpFailover,
       "hpDistributionEvent": hpDistributionEvent,
       "hpAdminAuthFailure": hpAdminAuthFailure,
       "hpProcurveSysMib": hpProcurveSysMib,
       "hpProductDescription": hpProductDescription,
       "hpProductHWVersion": hpProductHWVersion,
       "hpProductSWVersion": hpProductSWVersion,
       "hpProductSerialNumber": hpProductSerialNumber,
       "hpProductLastChange": hpProductLastChange,
       "hpCpuTemperature": hpCpuTemperature,
       "hpPowerSupplyTemperature": hpPowerSupplyTemperature,
       "hpChassisTemperature": hpChassisTemperature,
       "hpFanStatusTable": hpFanStatusTable,
       "hpFanStatusEntry": hpFanStatusEntry,
       "hpFanNumber": hpFanNumber,
       "hpFanOperational": hpFanOperational,
       "hpFanSpeed": hpFanSpeed,
       "hpSystemMIBObjects": hpSystemMIBObjects,
       "hpConfig": hpConfig,
       "hpName": hpName,
       "hpSystemID": hpSystemID,
       "hpState": hpState,
       "hpDistributionType": hpDistributionType,
       "hpDistributionStatus": hpDistributionStatus,
       "hpIpAddress": hpIpAddress,
       "hpPeerIpAddress": hpPeerIpAddress,
       "hpTechSupportEnabled": hpTechSupportEnabled,
       "hpFailedAdminIpAddress": hpFailedAdminIpAddress,
       "hpStatus": hpStatus,
       "hpNumAccessControllers": hpNumAccessControllers,
       "hpNumClients": hpNumClients,
       "hpNotificationsConfig": hpNotificationsConfig,
       "hpFailoverNotificationEnabled": hpFailoverNotificationEnabled,
       "hpDistributionNotificationEnabled": hpDistributionNotificationEnabled,
       "hpAdminAuthFailureNotificationEnabled": hpAdminAuthFailureNotificationEnabled,
       "hpSystemMIBConformance": hpSystemMIBConformance,
       "hpCompliances": hpCompliances,
       "hpSystemMIBCompliance1": hpSystemMIBCompliance1,
       "hpGroups": hpGroups,
       "hpSystemGroup": hpSystemGroup,
       "hpEnvGroup": hpEnvGroup,
       "hpConfigGroup": hpConfigGroup,
       "hpStatusGroup": hpStatusGroup,
       "hpNotificationsConfigGroup": hpNotificationsConfigGroup,
       "hpNotificationsGroup": hpNotificationsGroup}
)
