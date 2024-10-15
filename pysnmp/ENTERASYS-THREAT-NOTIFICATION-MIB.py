# SNMP MIB module (ENTERASYS-THREAT-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-THREAT-NOTIFICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:39 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

etsysThreatNotificationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45)
)
etsysThreatNotificationMIB.setRevisions(
        ("2005-09-14 13:14",
         "2005-02-11 15:14",
         "2004-07-19 17:58",
         "2004-03-10 15:47")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysThreatNotificationObjects_ObjectIdentity = ObjectIdentity
etsysThreatNotificationObjects = _EtsysThreatNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1)
)
_EtsysThreatNotificationNotificationBranch_ObjectIdentity = ObjectIdentity
etsysThreatNotificationNotificationBranch = _EtsysThreatNotificationNotificationBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 0)
)
_EtsysThreatNotificationSystemBranch_ObjectIdentity = ObjectIdentity
etsysThreatNotificationSystemBranch = _EtsysThreatNotificationSystemBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 1)
)


class _EtsysThreatNotificationSenderID_Type(DisplayString):
    """Custom type etsysThreatNotificationSenderID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EtsysThreatNotificationSenderID_Type.__name__ = "DisplayString"
_EtsysThreatNotificationSenderID_Object = MibScalar
etsysThreatNotificationSenderID = _EtsysThreatNotificationSenderID_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 1, 1),
    _EtsysThreatNotificationSenderID_Type()
)
etsysThreatNotificationSenderID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysThreatNotificationSenderID.setStatus("current")


class _EtsysThreatNotificationSenderName_Type(DisplayString):
    """Custom type etsysThreatNotificationSenderName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EtsysThreatNotificationSenderName_Type.__name__ = "DisplayString"
_EtsysThreatNotificationSenderName_Object = MibScalar
etsysThreatNotificationSenderName = _EtsysThreatNotificationSenderName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 1, 2),
    _EtsysThreatNotificationSenderName_Type()
)
etsysThreatNotificationSenderName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysThreatNotificationSenderName.setStatus("current")


class _EtsysThreatNotificationThreatCategory_Type(DisplayString):
    """Custom type etsysThreatNotificationThreatCategory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EtsysThreatNotificationThreatCategory_Type.__name__ = "DisplayString"
_EtsysThreatNotificationThreatCategory_Object = MibScalar
etsysThreatNotificationThreatCategory = _EtsysThreatNotificationThreatCategory_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 1, 3),
    _EtsysThreatNotificationThreatCategory_Type()
)
etsysThreatNotificationThreatCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysThreatNotificationThreatCategory.setStatus("current")


class _EtsysThreatNotificationThreatName_Type(DisplayString):
    """Custom type etsysThreatNotificationThreatName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysThreatNotificationThreatName_Type.__name__ = "DisplayString"
_EtsysThreatNotificationThreatName_Object = MibScalar
etsysThreatNotificationThreatName = _EtsysThreatNotificationThreatName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 1, 4),
    _EtsysThreatNotificationThreatName_Type()
)
etsysThreatNotificationThreatName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysThreatNotificationThreatName.setStatus("current")
_EtsysThreatNotificationDeviceAddressType_Type = InetAddressType
_EtsysThreatNotificationDeviceAddressType_Object = MibScalar
etsysThreatNotificationDeviceAddressType = _EtsysThreatNotificationDeviceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 1, 5),
    _EtsysThreatNotificationDeviceAddressType_Type()
)
etsysThreatNotificationDeviceAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysThreatNotificationDeviceAddressType.setStatus("current")
_EtsysThreatNotificationDeviceAddress_Type = InetAddress
_EtsysThreatNotificationDeviceAddress_Object = MibScalar
etsysThreatNotificationDeviceAddress = _EtsysThreatNotificationDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 1, 6),
    _EtsysThreatNotificationDeviceAddress_Type()
)
etsysThreatNotificationDeviceAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysThreatNotificationDeviceAddress.setStatus("current")
_EtsysThreatNotificationDeviceIfIndex_Type = InterfaceIndex
_EtsysThreatNotificationDeviceIfIndex_Object = MibScalar
etsysThreatNotificationDeviceIfIndex = _EtsysThreatNotificationDeviceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 1, 7),
    _EtsysThreatNotificationDeviceIfIndex_Type()
)
etsysThreatNotificationDeviceIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysThreatNotificationDeviceIfIndex.setStatus("current")
_EtsysThreatNotificationInitiatorAddressType_Type = InetAddressType
_EtsysThreatNotificationInitiatorAddressType_Object = MibScalar
etsysThreatNotificationInitiatorAddressType = _EtsysThreatNotificationInitiatorAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 1, 8),
    _EtsysThreatNotificationInitiatorAddressType_Type()
)
etsysThreatNotificationInitiatorAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysThreatNotificationInitiatorAddressType.setStatus("current")
_EtsysThreatNotificationInitiatorAddress_Type = InetAddress
_EtsysThreatNotificationInitiatorAddress_Object = MibScalar
etsysThreatNotificationInitiatorAddress = _EtsysThreatNotificationInitiatorAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 1, 9),
    _EtsysThreatNotificationInitiatorAddress_Type()
)
etsysThreatNotificationInitiatorAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysThreatNotificationInitiatorAddress.setStatus("current")
_EtsysThreatNotificationTargetAddressType_Type = InetAddressType
_EtsysThreatNotificationTargetAddressType_Object = MibScalar
etsysThreatNotificationTargetAddressType = _EtsysThreatNotificationTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 1, 10),
    _EtsysThreatNotificationTargetAddressType_Type()
)
etsysThreatNotificationTargetAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysThreatNotificationTargetAddressType.setStatus("current")
_EtsysThreatNotificationTargetAddress_Type = InetAddress
_EtsysThreatNotificationTargetAddress_Object = MibScalar
etsysThreatNotificationTargetAddress = _EtsysThreatNotificationTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 1, 11),
    _EtsysThreatNotificationTargetAddress_Type()
)
etsysThreatNotificationTargetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysThreatNotificationTargetAddress.setStatus("current")


class _EtsysThreatNotificationConsolidatedData_Type(DisplayString):
    """Custom type etsysThreatNotificationConsolidatedData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_EtsysThreatNotificationConsolidatedData_Type.__name__ = "DisplayString"
_EtsysThreatNotificationConsolidatedData_Object = MibScalar
etsysThreatNotificationConsolidatedData = _EtsysThreatNotificationConsolidatedData_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 1, 12),
    _EtsysThreatNotificationConsolidatedData_Type()
)
etsysThreatNotificationConsolidatedData.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysThreatNotificationConsolidatedData.setStatus("current")
_EtsysThreatNotificationInitiatorMacAddress_Type = MacAddress
_EtsysThreatNotificationInitiatorMacAddress_Object = MibScalar
etsysThreatNotificationInitiatorMacAddress = _EtsysThreatNotificationInitiatorMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 1, 13),
    _EtsysThreatNotificationInitiatorMacAddress_Type()
)
etsysThreatNotificationInitiatorMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysThreatNotificationInitiatorMacAddress.setStatus("current")
_EtsysThreatNotificationIncidentID_Type = Integer32
_EtsysThreatNotificationIncidentID_Object = MibScalar
etsysThreatNotificationIncidentID = _EtsysThreatNotificationIncidentID_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 1, 14),
    _EtsysThreatNotificationIncidentID_Type()
)
etsysThreatNotificationIncidentID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysThreatNotificationIncidentID.setStatus("current")


class _EtsysThreatNotificationStatus_Type(DisplayString):
    """Custom type etsysThreatNotificationStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EtsysThreatNotificationStatus_Type.__name__ = "DisplayString"
_EtsysThreatNotificationStatus_Object = MibScalar
etsysThreatNotificationStatus = _EtsysThreatNotificationStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 1, 15),
    _EtsysThreatNotificationStatus_Type()
)
etsysThreatNotificationStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysThreatNotificationStatus.setStatus("current")


class _EtsysThreatNotificationDetails_Type(DisplayString):
    """Custom type etsysThreatNotificationDetails based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysThreatNotificationDetails_Type.__name__ = "DisplayString"
_EtsysThreatNotificationDetails_Object = MibScalar
etsysThreatNotificationDetails = _EtsysThreatNotificationDetails_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 1, 16),
    _EtsysThreatNotificationDetails_Type()
)
etsysThreatNotificationDetails.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysThreatNotificationDetails.setStatus("current")


class _EtsysThreatNotificationAction_Type(DisplayString):
    """Custom type etsysThreatNotificationAction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EtsysThreatNotificationAction_Type.__name__ = "DisplayString"
_EtsysThreatNotificationAction_Object = MibScalar
etsysThreatNotificationAction = _EtsysThreatNotificationAction_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 1, 17),
    _EtsysThreatNotificationAction_Type()
)
etsysThreatNotificationAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysThreatNotificationAction.setStatus("current")


class _EtsysThreatNotificationRuleName_Type(DisplayString):
    """Custom type etsysThreatNotificationRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EtsysThreatNotificationRuleName_Type.__name__ = "DisplayString"
_EtsysThreatNotificationRuleName_Object = MibScalar
etsysThreatNotificationRuleName = _EtsysThreatNotificationRuleName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 1, 18),
    _EtsysThreatNotificationRuleName_Type()
)
etsysThreatNotificationRuleName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysThreatNotificationRuleName.setStatus("current")
_EtsysThreatNotificationDateTime_Type = DateAndTime
_EtsysThreatNotificationDateTime_Object = MibScalar
etsysThreatNotificationDateTime = _EtsysThreatNotificationDateTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 1, 19),
    _EtsysThreatNotificationDateTime_Type()
)
etsysThreatNotificationDateTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysThreatNotificationDateTime.setStatus("current")
_EtsysThreatNotificationLastUpdated_Type = DateAndTime
_EtsysThreatNotificationLastUpdated_Object = MibScalar
etsysThreatNotificationLastUpdated = _EtsysThreatNotificationLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 1, 20),
    _EtsysThreatNotificationLastUpdated_Type()
)
etsysThreatNotificationLastUpdated.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysThreatNotificationLastUpdated.setStatus("current")
_EtsysThreatNotificationConformance_ObjectIdentity = ObjectIdentity
etsysThreatNotificationConformance = _EtsysThreatNotificationConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 2)
)
_EtsysThreatNotificationGroups_ObjectIdentity = ObjectIdentity
etsysThreatNotificationGroups = _EtsysThreatNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 2, 1)
)
_EtsysThreatNotificationCompliances_ObjectIdentity = ObjectIdentity
etsysThreatNotificationCompliances = _EtsysThreatNotificationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 2, 2)
)

# Managed Objects groups

etsysThreatNotificationMessage1SystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 2, 1, 1)
)
etsysThreatNotificationMessage1SystemGroup.setObjects(
      *(("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationSenderID"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationSenderName"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationThreatCategory"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationThreatName"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInitiatorAddressType"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInitiatorAddress"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationTargetAddressType"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationTargetAddress"))
)
if mibBuilder.loadTexts:
    etsysThreatNotificationMessage1SystemGroup.setStatus("current")

etsysThreatNotificationMessage2SystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 2, 1, 2)
)
etsysThreatNotificationMessage2SystemGroup.setObjects(
      *(("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDeviceAddressType"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDeviceAddress"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDeviceIfIndex"))
)
if mibBuilder.loadTexts:
    etsysThreatNotificationMessage2SystemGroup.setStatus("current")

etsysThreatNotificationMessage3SystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 2, 1, 3)
)
etsysThreatNotificationMessage3SystemGroup.setObjects(
    ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationConsolidatedData")
)
if mibBuilder.loadTexts:
    etsysThreatNotificationMessage3SystemGroup.setStatus("current")

etsysThreatNotificationMessage4SystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 2, 1, 7)
)
etsysThreatNotificationMessage4SystemGroup.setObjects(
      *(("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDeviceAddressType"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDeviceAddress"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDeviceIfIndex"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInitiatorMacAddress"))
)
if mibBuilder.loadTexts:
    etsysThreatNotificationMessage4SystemGroup.setStatus("current")

etsysThreatUndoNotificationMessageSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 2, 1, 9)
)
etsysThreatUndoNotificationMessageSystemGroup.setObjects(
      *(("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationIncidentID"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDeviceAddressType"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDeviceAddress"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDeviceIfIndex"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInitiatorAddressType"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInitiatorAddress"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInitiatorMacAddress"))
)
if mibBuilder.loadTexts:
    etsysThreatUndoNotificationMessageSystemGroup.setStatus("current")

etsysThreatResponseNotificationMessageSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 2, 1, 11)
)
etsysThreatResponseNotificationMessageSystemGroup.setObjects(
      *(("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationIncidentID"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationStatus"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDateTime"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationSenderID"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationSenderName"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationThreatCategory"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationThreatName"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInitiatorAddressType"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInitiatorAddress"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInitiatorMacAddress"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDeviceAddressType"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDeviceAddress"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDeviceIfIndex"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationRuleName"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationAction"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDetails"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationLastUpdated"))
)
if mibBuilder.loadTexts:
    etsysThreatResponseNotificationMessageSystemGroup.setStatus("current")


# Notification objects

etsysThreatNotificationInformationMessage1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 0, 1)
)
etsysThreatNotificationInformationMessage1.setObjects(
      *(("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationSenderID"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationSenderName"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationThreatCategory"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationThreatName"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInitiatorAddressType"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInitiatorAddress"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationTargetAddressType"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationTargetAddress"))
)
if mibBuilder.loadTexts:
    etsysThreatNotificationInformationMessage1.setStatus(
        "current"
    )

etsysThreatNotificationInformationMessage2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 0, 2)
)
etsysThreatNotificationInformationMessage2.setObjects(
      *(("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationSenderID"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationSenderName"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationThreatCategory"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationThreatName"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDeviceAddressType"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDeviceAddress"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDeviceIfIndex"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInitiatorAddressType"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInitiatorAddress"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationTargetAddressType"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationTargetAddress"))
)
if mibBuilder.loadTexts:
    etsysThreatNotificationInformationMessage2.setStatus(
        "current"
    )

etsysThreatNotificationInformationMessage3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 0, 3)
)
etsysThreatNotificationInformationMessage3.setObjects(
    ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationConsolidatedData")
)
if mibBuilder.loadTexts:
    etsysThreatNotificationInformationMessage3.setStatus(
        "current"
    )

etsysThreatNotificationInformationMessage4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 0, 4)
)
etsysThreatNotificationInformationMessage4.setObjects(
      *(("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationSenderID"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationSenderName"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationThreatCategory"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationThreatName"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDeviceAddressType"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDeviceAddress"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDeviceIfIndex"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInitiatorAddressType"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInitiatorAddress"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInitiatorMacAddress"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationTargetAddressType"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationTargetAddress"))
)
if mibBuilder.loadTexts:
    etsysThreatNotificationInformationMessage4.setStatus(
        "current"
    )

etsysThreatUndoNotificationMessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 0, 5)
)
etsysThreatUndoNotificationMessage.setObjects(
      *(("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationIncidentID"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDeviceAddressType"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDeviceAddress"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDeviceIfIndex"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInitiatorAddressType"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInitiatorAddress"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInitiatorMacAddress"))
)
if mibBuilder.loadTexts:
    etsysThreatUndoNotificationMessage.setStatus(
        "current"
    )

etsysThreatResponseNotificationMessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 1, 0, 6)
)
etsysThreatResponseNotificationMessage.setObjects(
      *(("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationIncidentID"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationStatus"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDateTime"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationSenderID"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationSenderName"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationThreatCategory"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationThreatName"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInitiatorAddressType"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInitiatorAddress"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInitiatorMacAddress"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDeviceAddressType"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDeviceAddress"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDeviceIfIndex"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationRuleName"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationAction"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationDetails"),
        ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationLastUpdated"))
)
if mibBuilder.loadTexts:
    etsysThreatResponseNotificationMessage.setStatus(
        "current"
    )


# Notifications groups

etsysThreatNotificationMessage1Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 2, 1, 4)
)
etsysThreatNotificationMessage1Group.setObjects(
    ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInformationMessage1")
)
if mibBuilder.loadTexts:
    etsysThreatNotificationMessage1Group.setStatus(
        "current"
    )

etsysThreatNotificationMessage2Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 2, 1, 5)
)
etsysThreatNotificationMessage2Group.setObjects(
    ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInformationMessage2")
)
if mibBuilder.loadTexts:
    etsysThreatNotificationMessage2Group.setStatus(
        "current"
    )

etsysThreatNotificationMessage3Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 2, 1, 6)
)
etsysThreatNotificationMessage3Group.setObjects(
    ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInformationMessage3")
)
if mibBuilder.loadTexts:
    etsysThreatNotificationMessage3Group.setStatus(
        "current"
    )

etsysThreatNotificationMessage4Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 2, 1, 8)
)
etsysThreatNotificationMessage4Group.setObjects(
    ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatNotificationInformationMessage4")
)
if mibBuilder.loadTexts:
    etsysThreatNotificationMessage4Group.setStatus(
        "current"
    )

etsysThreatUndoNotificationMessageGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 2, 1, 10)
)
etsysThreatUndoNotificationMessageGroup.setObjects(
    ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatUndoNotificationMessage")
)
if mibBuilder.loadTexts:
    etsysThreatUndoNotificationMessageGroup.setStatus(
        "current"
    )

etsysThreatResponseNotificationMessageGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 2, 1, 12)
)
etsysThreatResponseNotificationMessageGroup.setObjects(
    ("ENTERASYS-THREAT-NOTIFICATION-MIB", "etsysThreatResponseNotificationMessage")
)
if mibBuilder.loadTexts:
    etsysThreatResponseNotificationMessageGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

etsysThreatNotificationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 45, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysThreatNotificationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-THREAT-NOTIFICATION-MIB",
    **{"etsysThreatNotificationMIB": etsysThreatNotificationMIB,
       "etsysThreatNotificationObjects": etsysThreatNotificationObjects,
       "etsysThreatNotificationNotificationBranch": etsysThreatNotificationNotificationBranch,
       "etsysThreatNotificationInformationMessage1": etsysThreatNotificationInformationMessage1,
       "etsysThreatNotificationInformationMessage2": etsysThreatNotificationInformationMessage2,
       "etsysThreatNotificationInformationMessage3": etsysThreatNotificationInformationMessage3,
       "etsysThreatNotificationInformationMessage4": etsysThreatNotificationInformationMessage4,
       "etsysThreatUndoNotificationMessage": etsysThreatUndoNotificationMessage,
       "etsysThreatResponseNotificationMessage": etsysThreatResponseNotificationMessage,
       "etsysThreatNotificationSystemBranch": etsysThreatNotificationSystemBranch,
       "etsysThreatNotificationSenderID": etsysThreatNotificationSenderID,
       "etsysThreatNotificationSenderName": etsysThreatNotificationSenderName,
       "etsysThreatNotificationThreatCategory": etsysThreatNotificationThreatCategory,
       "etsysThreatNotificationThreatName": etsysThreatNotificationThreatName,
       "etsysThreatNotificationDeviceAddressType": etsysThreatNotificationDeviceAddressType,
       "etsysThreatNotificationDeviceAddress": etsysThreatNotificationDeviceAddress,
       "etsysThreatNotificationDeviceIfIndex": etsysThreatNotificationDeviceIfIndex,
       "etsysThreatNotificationInitiatorAddressType": etsysThreatNotificationInitiatorAddressType,
       "etsysThreatNotificationInitiatorAddress": etsysThreatNotificationInitiatorAddress,
       "etsysThreatNotificationTargetAddressType": etsysThreatNotificationTargetAddressType,
       "etsysThreatNotificationTargetAddress": etsysThreatNotificationTargetAddress,
       "etsysThreatNotificationConsolidatedData": etsysThreatNotificationConsolidatedData,
       "etsysThreatNotificationInitiatorMacAddress": etsysThreatNotificationInitiatorMacAddress,
       "etsysThreatNotificationIncidentID": etsysThreatNotificationIncidentID,
       "etsysThreatNotificationStatus": etsysThreatNotificationStatus,
       "etsysThreatNotificationDetails": etsysThreatNotificationDetails,
       "etsysThreatNotificationAction": etsysThreatNotificationAction,
       "etsysThreatNotificationRuleName": etsysThreatNotificationRuleName,
       "etsysThreatNotificationDateTime": etsysThreatNotificationDateTime,
       "etsysThreatNotificationLastUpdated": etsysThreatNotificationLastUpdated,
       "etsysThreatNotificationConformance": etsysThreatNotificationConformance,
       "etsysThreatNotificationGroups": etsysThreatNotificationGroups,
       "etsysThreatNotificationMessage1SystemGroup": etsysThreatNotificationMessage1SystemGroup,
       "etsysThreatNotificationMessage2SystemGroup": etsysThreatNotificationMessage2SystemGroup,
       "etsysThreatNotificationMessage3SystemGroup": etsysThreatNotificationMessage3SystemGroup,
       "etsysThreatNotificationMessage1Group": etsysThreatNotificationMessage1Group,
       "etsysThreatNotificationMessage2Group": etsysThreatNotificationMessage2Group,
       "etsysThreatNotificationMessage3Group": etsysThreatNotificationMessage3Group,
       "etsysThreatNotificationMessage4SystemGroup": etsysThreatNotificationMessage4SystemGroup,
       "etsysThreatNotificationMessage4Group": etsysThreatNotificationMessage4Group,
       "etsysThreatUndoNotificationMessageSystemGroup": etsysThreatUndoNotificationMessageSystemGroup,
       "etsysThreatUndoNotificationMessageGroup": etsysThreatUndoNotificationMessageGroup,
       "etsysThreatResponseNotificationMessageSystemGroup": etsysThreatResponseNotificationMessageSystemGroup,
       "etsysThreatResponseNotificationMessageGroup": etsysThreatResponseNotificationMessageGroup,
       "etsysThreatNotificationCompliances": etsysThreatNotificationCompliances,
       "etsysThreatNotificationCompliance": etsysThreatNotificationCompliance}
)
