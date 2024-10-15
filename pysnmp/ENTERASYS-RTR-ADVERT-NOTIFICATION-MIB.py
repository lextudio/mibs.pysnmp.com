# SNMP MIB module (ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:31 2024
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

(ifName,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifName")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

etsysRtrAdvertNotificationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 82)
)
etsysRtrAdvertNotificationMIB.setRevisions(
        ("2011-05-13 13:47",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysRtrAdvertNotificationObjects_ObjectIdentity = ObjectIdentity
etsysRtrAdvertNotificationObjects = _EtsysRtrAdvertNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1)
)
_EtsysRtrAdvertConfigBranch_ObjectIdentity = ObjectIdentity
etsysRtrAdvertConfigBranch = _EtsysRtrAdvertConfigBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1, 0)
)


class _EtsysRtrAdvertInconsistentEnabled_Type(TruthValue):
    """Custom type etsysRtrAdvertInconsistentEnabled based on TruthValue"""


_EtsysRtrAdvertInconsistentEnabled_Object = MibScalar
etsysRtrAdvertInconsistentEnabled = _EtsysRtrAdvertInconsistentEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1, 0, 1),
    _EtsysRtrAdvertInconsistentEnabled_Type()
)
etsysRtrAdvertInconsistentEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRtrAdvertInconsistentEnabled.setStatus("current")
_EtsysRtrAdvertInformationBranch_ObjectIdentity = ObjectIdentity
etsysRtrAdvertInformationBranch = _EtsysRtrAdvertInformationBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1, 1)
)
_EtsysRtrAdvertInetAddrType_Type = InetAddressType
_EtsysRtrAdvertInetAddrType_Object = MibScalar
etsysRtrAdvertInetAddrType = _EtsysRtrAdvertInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1, 1, 1),
    _EtsysRtrAdvertInetAddrType_Type()
)
etsysRtrAdvertInetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysRtrAdvertInetAddrType.setStatus("current")
_EtsysRtrAdvertInetAddress_Type = InetAddress
_EtsysRtrAdvertInetAddress_Object = MibScalar
etsysRtrAdvertInetAddress = _EtsysRtrAdvertInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1, 1, 2),
    _EtsysRtrAdvertInetAddress_Type()
)
etsysRtrAdvertInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysRtrAdvertInetAddress.setStatus("current")
_EtsysRtrAdvertUserData_Type = SnmpAdminString
_EtsysRtrAdvertUserData_Object = MibScalar
etsysRtrAdvertUserData = _EtsysRtrAdvertUserData_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1, 1, 3),
    _EtsysRtrAdvertUserData_Type()
)
etsysRtrAdvertUserData.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysRtrAdvertUserData.setStatus("current")
_EtsysRtrAdvertNotificationBranch_ObjectIdentity = ObjectIdentity
etsysRtrAdvertNotificationBranch = _EtsysRtrAdvertNotificationBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1, 2)
)
_EtsysRtrAdvertConformance_ObjectIdentity = ObjectIdentity
etsysRtrAdvertConformance = _EtsysRtrAdvertConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 2)
)
_EtsysRtrAdvertGroups_ObjectIdentity = ObjectIdentity
etsysRtrAdvertGroups = _EtsysRtrAdvertGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 2, 1)
)
_EtsysRtrAdvertCompliances_ObjectIdentity = ObjectIdentity
etsysRtrAdvertCompliances = _EtsysRtrAdvertCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 2, 2)
)

# Managed Objects groups

etsysRtrAdvertConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 2, 1, 1)
)
etsysRtrAdvertConfigGroup.setObjects(
    ("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertInconsistentEnabled")
)
if mibBuilder.loadTexts:
    etsysRtrAdvertConfigGroup.setStatus("current")

etsysRtrAdvertInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 2, 1, 2)
)
etsysRtrAdvertInformationGroup.setObjects(
      *(("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertInetAddrType"),
        ("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertInetAddress"),
        ("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertUserData"))
)
if mibBuilder.loadTexts:
    etsysRtrAdvertInformationGroup.setStatus("current")


# Notification objects

etsysRtrAdvertInconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1, 2, 1)
)
etsysRtrAdvertInconsistent.setObjects(
      *(("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertInetAddrType"),
        ("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertInetAddress"),
        ("IF-MIB", "ifName"),
        ("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertUserData"))
)
if mibBuilder.loadTexts:
    etsysRtrAdvertInconsistent.setStatus(
        "current"
    )


# Notifications groups

etsysRtrAdvertNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 2, 1, 3)
)
etsysRtrAdvertNotificationGroup.setObjects(
    ("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertInconsistent")
)
if mibBuilder.loadTexts:
    etsysRtrAdvertNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

etsysRtrAdvertCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysRtrAdvertCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB",
    **{"etsysRtrAdvertNotificationMIB": etsysRtrAdvertNotificationMIB,
       "etsysRtrAdvertNotificationObjects": etsysRtrAdvertNotificationObjects,
       "etsysRtrAdvertConfigBranch": etsysRtrAdvertConfigBranch,
       "etsysRtrAdvertInconsistentEnabled": etsysRtrAdvertInconsistentEnabled,
       "etsysRtrAdvertInformationBranch": etsysRtrAdvertInformationBranch,
       "etsysRtrAdvertInetAddrType": etsysRtrAdvertInetAddrType,
       "etsysRtrAdvertInetAddress": etsysRtrAdvertInetAddress,
       "etsysRtrAdvertUserData": etsysRtrAdvertUserData,
       "etsysRtrAdvertNotificationBranch": etsysRtrAdvertNotificationBranch,
       "etsysRtrAdvertInconsistent": etsysRtrAdvertInconsistent,
       "etsysRtrAdvertConformance": etsysRtrAdvertConformance,
       "etsysRtrAdvertGroups": etsysRtrAdvertGroups,
       "etsysRtrAdvertConfigGroup": etsysRtrAdvertConfigGroup,
       "etsysRtrAdvertInformationGroup": etsysRtrAdvertInformationGroup,
       "etsysRtrAdvertNotificationGroup": etsysRtrAdvertNotificationGroup,
       "etsysRtrAdvertCompliances": etsysRtrAdvertCompliances,
       "etsysRtrAdvertCompliance": etsysRtrAdvertCompliance}
)
