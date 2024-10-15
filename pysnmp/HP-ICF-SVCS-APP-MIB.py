# SNMP MIB module (HP-ICF-SVCS-APP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-SVCS-APP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:16 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

(AutonomousType,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfSvcsAppMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86)
)
hpicfSvcsAppMIB.setRevisions(
        ("2011-05-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AppStatus(Integer32, TextualConvention):
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
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("appError", 10),
          ("appInit", 9),
          ("appRunning", 11),
          ("bootFailure", 5),
          ("bootInit", 3),
          ("booting", 4),
          ("halted", 6),
          ("other", 1),
          ("ready", 8),
          ("rebooting", 7),
          ("shuttingDown", 12),
          ("unknown", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HpicfSvcsAppNotifications_ObjectIdentity = ObjectIdentity
hpicfSvcsAppNotifications = _HpicfSvcsAppNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 0)
)
_HpicfSvcsAppObjects_ObjectIdentity = ObjectIdentity
hpicfSvcsAppObjects = _HpicfSvcsAppObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1)
)
_HpicfSvcsInstalledAppTable_Object = MibTable
hpicfSvcsInstalledAppTable = _HpicfSvcsInstalledAppTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfSvcsInstalledAppTable.setStatus("current")
_HpicfSvcsInstalledAppEntry_Object = MibTableRow
hpicfSvcsInstalledAppEntry = _HpicfSvcsInstalledAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 1, 1)
)
hpicfSvcsInstalledAppEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpicfSvcsInstalledAppEntry.setStatus("current")
_HpicfSvcsInstalledAppPlatformType_Type = AutonomousType
_HpicfSvcsInstalledAppPlatformType_Object = MibTableColumn
hpicfSvcsInstalledAppPlatformType = _HpicfSvcsInstalledAppPlatformType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 1, 1, 1),
    _HpicfSvcsInstalledAppPlatformType_Type()
)
hpicfSvcsInstalledAppPlatformType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSvcsInstalledAppPlatformType.setStatus("current")


class _HpicfSvcsInstalledAppDescription_Type(SnmpAdminString):
    """Custom type hpicfSvcsInstalledAppDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpicfSvcsInstalledAppDescription_Type.__name__ = "SnmpAdminString"
_HpicfSvcsInstalledAppDescription_Object = MibTableColumn
hpicfSvcsInstalledAppDescription = _HpicfSvcsInstalledAppDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 1, 1, 2),
    _HpicfSvcsInstalledAppDescription_Type()
)
hpicfSvcsInstalledAppDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSvcsInstalledAppDescription.setStatus("current")


class _HpicfSvcsInstalledAppVersion_Type(SnmpAdminString):
    """Custom type hpicfSvcsInstalledAppVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpicfSvcsInstalledAppVersion_Type.__name__ = "SnmpAdminString"
_HpicfSvcsInstalledAppVersion_Object = MibTableColumn
hpicfSvcsInstalledAppVersion = _HpicfSvcsInstalledAppVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 1, 1, 3),
    _HpicfSvcsInstalledAppVersion_Type()
)
hpicfSvcsInstalledAppVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSvcsInstalledAppVersion.setStatus("current")
_HpicfSvcsInstalledAppStatus_Type = AppStatus
_HpicfSvcsInstalledAppStatus_Object = MibTableColumn
hpicfSvcsInstalledAppStatus = _HpicfSvcsInstalledAppStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 1, 1, 4),
    _HpicfSvcsInstalledAppStatus_Type()
)
hpicfSvcsInstalledAppStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSvcsInstalledAppStatus.setStatus("current")


class _HpicfSvcsInstalledAppJNumber_Type(SnmpAdminString):
    """Custom type hpicfSvcsInstalledAppJNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpicfSvcsInstalledAppJNumber_Type.__name__ = "SnmpAdminString"
_HpicfSvcsInstalledAppJNumber_Object = MibTableColumn
hpicfSvcsInstalledAppJNumber = _HpicfSvcsInstalledAppJNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 1, 1, 5),
    _HpicfSvcsInstalledAppJNumber_Type()
)
hpicfSvcsInstalledAppJNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSvcsInstalledAppJNumber.setStatus("current")


class _HpicfSvcsInstalledAppLicensingStatus_Type(Integer32):
    """Custom type hpicfSvcsInstalledAppLicensingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("expired", 2),
          ("unknown", 3))
    )


_HpicfSvcsInstalledAppLicensingStatus_Type.__name__ = "Integer32"
_HpicfSvcsInstalledAppLicensingStatus_Object = MibTableColumn
hpicfSvcsInstalledAppLicensingStatus = _HpicfSvcsInstalledAppLicensingStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 1, 1, 6),
    _HpicfSvcsInstalledAppLicensingStatus_Type()
)
hpicfSvcsInstalledAppLicensingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSvcsInstalledAppLicensingStatus.setStatus("current")
_HpicfSvcsInstalledAppRowStatus_Type = RowStatus
_HpicfSvcsInstalledAppRowStatus_Object = MibTableColumn
hpicfSvcsInstalledAppRowStatus = _HpicfSvcsInstalledAppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 1, 1, 7),
    _HpicfSvcsInstalledAppRowStatus_Type()
)
hpicfSvcsInstalledAppRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSvcsInstalledAppRowStatus.setStatus("current")
_HpicfSvcsV1AppTable_Object = MibTable
hpicfSvcsV1AppTable = _HpicfSvcsV1AppTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfSvcsV1AppTable.setStatus("current")
_HpicfSvcsV1AppEntry_Object = MibTableRow
hpicfSvcsV1AppEntry = _HpicfSvcsV1AppEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 2, 1)
)
hpicfSvcsV1AppEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpicfSvcsV1AppEntry.setStatus("current")


class _HpicfSvcsV1AppIndex_Type(Integer32):
    """Custom type hpicfSvcsV1AppIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfSvcsV1AppIndex_Type.__name__ = "Integer32"
_HpicfSvcsV1AppIndex_Object = MibTableColumn
hpicfSvcsV1AppIndex = _HpicfSvcsV1AppIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 2, 1, 1),
    _HpicfSvcsV1AppIndex_Type()
)
hpicfSvcsV1AppIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSvcsV1AppIndex.setStatus("current")
_HpicfSvcsV1AppCLIAvailable_Type = TruthValue
_HpicfSvcsV1AppCLIAvailable_Object = MibTableColumn
hpicfSvcsV1AppCLIAvailable = _HpicfSvcsV1AppCLIAvailable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 2, 1, 2),
    _HpicfSvcsV1AppCLIAvailable_Type()
)
hpicfSvcsV1AppCLIAvailable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSvcsV1AppCLIAvailable.setStatus("current")


class _HpicfSvcsV1AppName_Type(SnmpAdminString):
    """Custom type hpicfSvcsV1AppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpicfSvcsV1AppName_Type.__name__ = "SnmpAdminString"
_HpicfSvcsV1AppName_Object = MibTableColumn
hpicfSvcsV1AppName = _HpicfSvcsV1AppName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 2, 1, 3),
    _HpicfSvcsV1AppName_Type()
)
hpicfSvcsV1AppName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSvcsV1AppName.setStatus("current")


class _HpicfSvcsV1AppDescription_Type(SnmpAdminString):
    """Custom type hpicfSvcsV1AppDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpicfSvcsV1AppDescription_Type.__name__ = "SnmpAdminString"
_HpicfSvcsV1AppDescription_Object = MibTableColumn
hpicfSvcsV1AppDescription = _HpicfSvcsV1AppDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 2, 1, 4),
    _HpicfSvcsV1AppDescription_Type()
)
hpicfSvcsV1AppDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSvcsV1AppDescription.setStatus("current")


class _HpicfSvcsV1AppVersion_Type(SnmpAdminString):
    """Custom type hpicfSvcsV1AppVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpicfSvcsV1AppVersion_Type.__name__ = "SnmpAdminString"
_HpicfSvcsV1AppVersion_Object = MibTableColumn
hpicfSvcsV1AppVersion = _HpicfSvcsV1AppVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 2, 1, 5),
    _HpicfSvcsV1AppVersion_Type()
)
hpicfSvcsV1AppVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSvcsV1AppVersion.setStatus("current")
_HpicfSvcsV1AppStatus_Type = AppStatus
_HpicfSvcsV1AppStatus_Object = MibTableColumn
hpicfSvcsV1AppStatus = _HpicfSvcsV1AppStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 2, 1, 6),
    _HpicfSvcsV1AppStatus_Type()
)
hpicfSvcsV1AppStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSvcsV1AppStatus.setStatus("current")


class _HpicfSvcsV1AppJNumber_Type(SnmpAdminString):
    """Custom type hpicfSvcsV1AppJNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpicfSvcsV1AppJNumber_Type.__name__ = "SnmpAdminString"
_HpicfSvcsV1AppJNumber_Object = MibTableColumn
hpicfSvcsV1AppJNumber = _HpicfSvcsV1AppJNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 2, 1, 7),
    _HpicfSvcsV1AppJNumber_Type()
)
hpicfSvcsV1AppJNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSvcsV1AppJNumber.setStatus("current")


class _HpicfSvcsV1AppURL_Type(SnmpAdminString):
    """Custom type hpicfSvcsV1AppURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfSvcsV1AppURL_Type.__name__ = "SnmpAdminString"
_HpicfSvcsV1AppURL_Object = MibTableColumn
hpicfSvcsV1AppURL = _HpicfSvcsV1AppURL_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 2, 1, 8),
    _HpicfSvcsV1AppURL_Type()
)
hpicfSvcsV1AppURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSvcsV1AppURL.setStatus("current")
_HpicfSvcsV1AppRowStatus_Type = RowStatus
_HpicfSvcsV1AppRowStatus_Object = MibTableColumn
hpicfSvcsV1AppRowStatus = _HpicfSvcsV1AppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 1, 2, 1, 9),
    _HpicfSvcsV1AppRowStatus_Type()
)
hpicfSvcsV1AppRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSvcsV1AppRowStatus.setStatus("current")
_HpicfSvcsAppConformance_ObjectIdentity = ObjectIdentity
hpicfSvcsAppConformance = _HpicfSvcsAppConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 2)
)
_HpicfSvcsAppCompliances_ObjectIdentity = ObjectIdentity
hpicfSvcsAppCompliances = _HpicfSvcsAppCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 2, 1)
)
_HpicfSvcsAppGroups_ObjectIdentity = ObjectIdentity
hpicfSvcsAppGroups = _HpicfSvcsAppGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 2, 2)
)

# Managed Objects groups

hpicfSvcsInstalledAppGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 2, 2, 1)
)
hpicfSvcsInstalledAppGroup.setObjects(
      *(("HP-ICF-SVCS-APP-MIB", "hpicfSvcsInstalledAppPlatformType"),
        ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsInstalledAppDescription"),
        ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsInstalledAppVersion"),
        ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsInstalledAppStatus"),
        ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsInstalledAppJNumber"),
        ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsInstalledAppLicensingStatus"),
        ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsInstalledAppRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfSvcsInstalledAppGroup.setStatus("current")

hpicfSvcsV1AppGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 2, 2, 2)
)
hpicfSvcsV1AppGroup.setObjects(
      *(("HP-ICF-SVCS-APP-MIB", "hpicfSvcsV1AppIndex"),
        ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsV1AppCLIAvailable"),
        ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsV1AppName"),
        ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsV1AppDescription"),
        ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsV1AppVersion"),
        ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsV1AppStatus"),
        ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsV1AppJNumber"),
        ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsV1AppURL"),
        ("HP-ICF-SVCS-APP-MIB", "hpicfSvcsV1AppRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfSvcsV1AppGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfSvcsAppCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfSvcsAppCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-SVCS-APP-MIB",
    **{"AppStatus": AppStatus,
       "hpicfSvcsAppMIB": hpicfSvcsAppMIB,
       "hpicfSvcsAppNotifications": hpicfSvcsAppNotifications,
       "hpicfSvcsAppObjects": hpicfSvcsAppObjects,
       "hpicfSvcsInstalledAppTable": hpicfSvcsInstalledAppTable,
       "hpicfSvcsInstalledAppEntry": hpicfSvcsInstalledAppEntry,
       "hpicfSvcsInstalledAppPlatformType": hpicfSvcsInstalledAppPlatformType,
       "hpicfSvcsInstalledAppDescription": hpicfSvcsInstalledAppDescription,
       "hpicfSvcsInstalledAppVersion": hpicfSvcsInstalledAppVersion,
       "hpicfSvcsInstalledAppStatus": hpicfSvcsInstalledAppStatus,
       "hpicfSvcsInstalledAppJNumber": hpicfSvcsInstalledAppJNumber,
       "hpicfSvcsInstalledAppLicensingStatus": hpicfSvcsInstalledAppLicensingStatus,
       "hpicfSvcsInstalledAppRowStatus": hpicfSvcsInstalledAppRowStatus,
       "hpicfSvcsV1AppTable": hpicfSvcsV1AppTable,
       "hpicfSvcsV1AppEntry": hpicfSvcsV1AppEntry,
       "hpicfSvcsV1AppIndex": hpicfSvcsV1AppIndex,
       "hpicfSvcsV1AppCLIAvailable": hpicfSvcsV1AppCLIAvailable,
       "hpicfSvcsV1AppName": hpicfSvcsV1AppName,
       "hpicfSvcsV1AppDescription": hpicfSvcsV1AppDescription,
       "hpicfSvcsV1AppVersion": hpicfSvcsV1AppVersion,
       "hpicfSvcsV1AppStatus": hpicfSvcsV1AppStatus,
       "hpicfSvcsV1AppJNumber": hpicfSvcsV1AppJNumber,
       "hpicfSvcsV1AppURL": hpicfSvcsV1AppURL,
       "hpicfSvcsV1AppRowStatus": hpicfSvcsV1AppRowStatus,
       "hpicfSvcsAppConformance": hpicfSvcsAppConformance,
       "hpicfSvcsAppCompliances": hpicfSvcsAppCompliances,
       "hpicfSvcsAppCompliance": hpicfSvcsAppCompliance,
       "hpicfSvcsAppGroups": hpicfSvcsAppGroups,
       "hpicfSvcsInstalledAppGroup": hpicfSvcsInstalledAppGroup,
       "hpicfSvcsV1AppGroup": hpicfSvcsV1AppGroup}
)
