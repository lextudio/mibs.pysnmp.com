# SNMP MIB module (CISCO-SIBU-FLASH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SIBU-FLASH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:14 2024
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

ciscoSibuFlashMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 45)
)
ciscoSibuFlashMIB.setRevisions(
        ("1998-10-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSibuFlashMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSibuFlashMIBObjects = _CiscoSibuFlashMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 1)
)
_CsfUpgrade_ObjectIdentity = ObjectIdentity
csfUpgrade = _CsfUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1)
)


class _CsfUpgradeFirmwareVersion_Type(DisplayString):
    """Custom type csfUpgradeFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CsfUpgradeFirmwareVersion_Type.__name__ = "DisplayString"
_CsfUpgradeFirmwareVersion_Object = MibScalar
csfUpgradeFirmwareVersion = _CsfUpgradeFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 1),
    _CsfUpgradeFirmwareVersion_Type()
)
csfUpgradeFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfUpgradeFirmwareVersion.setStatus("current")


class _CsfUpgradeFlashSize_Type(Integer32):
    """Custom type csfUpgradeFlashSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CsfUpgradeFlashSize_Type.__name__ = "Integer32"
_CsfUpgradeFlashSize_Object = MibScalar
csfUpgradeFlashSize = _CsfUpgradeFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 2),
    _CsfUpgradeFlashSize_Type()
)
csfUpgradeFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfUpgradeFlashSize.setStatus("current")
if mibBuilder.loadTexts:
    csfUpgradeFlashSize.setUnits("kbytes")


class _CsfUpgradeTFTPServerAddress_Type(IpAddress):
    """Custom type csfUpgradeTFTPServerAddress based on IpAddress"""
    defaultHexValue = "00000000"


_CsfUpgradeTFTPServerAddress_Object = MibScalar
csfUpgradeTFTPServerAddress = _CsfUpgradeTFTPServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 3),
    _CsfUpgradeTFTPServerAddress_Type()
)
csfUpgradeTFTPServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csfUpgradeTFTPServerAddress.setStatus("current")


class _CsfUpgradeTFTPLoadFilename_Type(DisplayString):
    """Custom type csfUpgradeTFTPLoadFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CsfUpgradeTFTPLoadFilename_Type.__name__ = "DisplayString"
_CsfUpgradeTFTPLoadFilename_Object = MibScalar
csfUpgradeTFTPLoadFilename = _CsfUpgradeTFTPLoadFilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 4),
    _CsfUpgradeTFTPLoadFilename_Type()
)
csfUpgradeTFTPLoadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csfUpgradeTFTPLoadFilename.setStatus("current")


class _CsfUpgradeTFTPInitiate_Type(Integer32):
    """Custom type csfUpgradeTFTPInitiate based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noUpgrade", 2),
          ("upgrade", 1))
    )


_CsfUpgradeTFTPInitiate_Type.__name__ = "Integer32"
_CsfUpgradeTFTPInitiate_Object = MibScalar
csfUpgradeTFTPInitiate = _CsfUpgradeTFTPInitiate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 5),
    _CsfUpgradeTFTPInitiate_Type()
)
csfUpgradeTFTPInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csfUpgradeTFTPInitiate.setStatus("current")


class _CsfUpgradeFlashMode_Type(Integer32):
    """Custom type csfUpgradeFlashMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permanent", 1),
          ("temporary", 2))
    )


_CsfUpgradeFlashMode_Type.__name__ = "Integer32"
_CsfUpgradeFlashMode_Object = MibScalar
csfUpgradeFlashMode = _CsfUpgradeFlashMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 6),
    _CsfUpgradeFlashMode_Type()
)
csfUpgradeFlashMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csfUpgradeFlashMode.setStatus("current")


class _CsfUpgradeFirmwareStatus_Type(Integer32):
    """Custom type csfUpgradeFirmwareStatus based on Integer32"""
    defaultValue = 1

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
        *(("failed", 4),
          ("inProgress", 2),
          ("none", 1),
          ("succeeded", 3))
    )


_CsfUpgradeFirmwareStatus_Type.__name__ = "Integer32"
_CsfUpgradeFirmwareStatus_Object = MibScalar
csfUpgradeFirmwareStatus = _CsfUpgradeFirmwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 7),
    _CsfUpgradeFirmwareStatus_Type()
)
csfUpgradeFirmwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfUpgradeFirmwareStatus.setStatus("current")
_CiscoSibuFlashMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
ciscoSibuFlashMIBNotificationsPrefix = _CiscoSibuFlashMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 2)
)
_CiscoSibuFlashMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoSibuFlashMIBNotifications = _CiscoSibuFlashMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 2, 0)
)
_CiscoSibuFlashMIBComformance_ObjectIdentity = ObjectIdentity
ciscoSibuFlashMIBComformance = _CiscoSibuFlashMIBComformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 3)
)
_CiscoSibuFlashMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSibuFlashMIBCompliances = _CiscoSibuFlashMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 3, 1)
)
_CiscoSibuFlashMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSibuFlashMIBGroups = _CiscoSibuFlashMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 3, 2)
)

# Managed Objects groups

ciscoSibuFlashMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 3, 2, 1)
)
ciscoSibuFlashMIBGroup.setObjects(
      *(("CISCO-SIBU-FLASH-MIB", "csfUpgradeFirmwareVersion"),
        ("CISCO-SIBU-FLASH-MIB", "csfUpgradeFlashSize"),
        ("CISCO-SIBU-FLASH-MIB", "csfUpgradeTFTPServerAddress"),
        ("CISCO-SIBU-FLASH-MIB", "csfUpgradeTFTPLoadFilename"),
        ("CISCO-SIBU-FLASH-MIB", "csfUpgradeTFTPInitiate"),
        ("CISCO-SIBU-FLASH-MIB", "csfUpgradeFlashMode"),
        ("CISCO-SIBU-FLASH-MIB", "csfUpgradeFirmwareStatus"))
)
if mibBuilder.loadTexts:
    ciscoSibuFlashMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoSibuFlashCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSibuFlashCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SIBU-FLASH-MIB",
    **{"ciscoSibuFlashMIB": ciscoSibuFlashMIB,
       "ciscoSibuFlashMIBObjects": ciscoSibuFlashMIBObjects,
       "csfUpgrade": csfUpgrade,
       "csfUpgradeFirmwareVersion": csfUpgradeFirmwareVersion,
       "csfUpgradeFlashSize": csfUpgradeFlashSize,
       "csfUpgradeTFTPServerAddress": csfUpgradeTFTPServerAddress,
       "csfUpgradeTFTPLoadFilename": csfUpgradeTFTPLoadFilename,
       "csfUpgradeTFTPInitiate": csfUpgradeTFTPInitiate,
       "csfUpgradeFlashMode": csfUpgradeFlashMode,
       "csfUpgradeFirmwareStatus": csfUpgradeFirmwareStatus,
       "ciscoSibuFlashMIBNotificationsPrefix": ciscoSibuFlashMIBNotificationsPrefix,
       "ciscoSibuFlashMIBNotifications": ciscoSibuFlashMIBNotifications,
       "ciscoSibuFlashMIBComformance": ciscoSibuFlashMIBComformance,
       "ciscoSibuFlashMIBCompliances": ciscoSibuFlashMIBCompliances,
       "ciscoSibuFlashCompliance": ciscoSibuFlashCompliance,
       "ciscoSibuFlashMIBGroups": ciscoSibuFlashMIBGroups,
       "ciscoSibuFlashMIBGroup": ciscoSibuFlashMIBGroup}
)
