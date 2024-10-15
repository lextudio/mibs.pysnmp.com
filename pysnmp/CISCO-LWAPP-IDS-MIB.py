# SNMP MIB module (CISCO-LWAPP-IDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-IDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:35 2024
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
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappIdsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 519)
)
ciscoLwappIdsMIB.setRevisions(
        ("2006-04-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappIdsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappIdsMIBNotifs = _CiscoLwappIdsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 0)
)
_CiscoLwappIdsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappIdsMIBObjects = _CiscoLwappIdsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 1)
)
_CiscoLwappIdsConfig_ObjectIdentity = ObjectIdentity
ciscoLwappIdsConfig = _CiscoLwappIdsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 1, 1)
)
_CLIdsIpsSensorConfigTable_Object = MibTable
cLIdsIpsSensorConfigTable = _CLIdsIpsSensorConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLIdsIpsSensorConfigTable.setStatus("current")
_CLIdsIpsSensorConfigEntry_Object = MibTableRow
cLIdsIpsSensorConfigEntry = _CLIdsIpsSensorConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 1, 1, 1, 1)
)
cLIdsIpsSensorConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-IDS-MIB", "cLIdsIpsSensorAddressType"),
    (0, "CISCO-LWAPP-IDS-MIB", "cLIdsIpsSensorAddress"),
)
if mibBuilder.loadTexts:
    cLIdsIpsSensorConfigEntry.setStatus("current")
_CLIdsIpsSensorAddressType_Type = InetAddressType
_CLIdsIpsSensorAddressType_Object = MibTableColumn
cLIdsIpsSensorAddressType = _CLIdsIpsSensorAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 1, 1, 1, 1, 1),
    _CLIdsIpsSensorAddressType_Type()
)
cLIdsIpsSensorAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLIdsIpsSensorAddressType.setStatus("current")
_CLIdsIpsSensorAddress_Type = InetAddress
_CLIdsIpsSensorAddress_Object = MibTableColumn
cLIdsIpsSensorAddress = _CLIdsIpsSensorAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 1, 1, 1, 1, 2),
    _CLIdsIpsSensorAddress_Type()
)
cLIdsIpsSensorAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLIdsIpsSensorAddress.setStatus("current")
_CLIdsIpsSensorUserName_Type = SnmpAdminString
_CLIdsIpsSensorUserName_Object = MibTableColumn
cLIdsIpsSensorUserName = _CLIdsIpsSensorUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 1, 1, 1, 1, 3),
    _CLIdsIpsSensorUserName_Type()
)
cLIdsIpsSensorUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIdsIpsSensorUserName.setStatus("current")
_CLIdsIpsSensorPassword_Type = SnmpAdminString
_CLIdsIpsSensorPassword_Object = MibTableColumn
cLIdsIpsSensorPassword = _CLIdsIpsSensorPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 1, 1, 1, 1, 4),
    _CLIdsIpsSensorPassword_Type()
)
cLIdsIpsSensorPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIdsIpsSensorPassword.setStatus("current")


class _CLIdsIpsSensorQueryInterval_Type(TimeInterval):
    """Custom type cLIdsIpsSensorQueryInterval based on TimeInterval"""
    defaultValue = 3000

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 360000),
    )


_CLIdsIpsSensorQueryInterval_Type.__name__ = "TimeInterval"
_CLIdsIpsSensorQueryInterval_Object = MibTableColumn
cLIdsIpsSensorQueryInterval = _CLIdsIpsSensorQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 1, 1, 1, 1, 5),
    _CLIdsIpsSensorQueryInterval_Type()
)
cLIdsIpsSensorQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIdsIpsSensorQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLIdsIpsSensorQueryInterval.setUnits("Hundredths-seconds")


class _CLIdsIpsSensorEnabled_Type(TruthValue):
    """Custom type cLIdsIpsSensorEnabled based on TruthValue"""


_CLIdsIpsSensorEnabled_Object = MibTableColumn
cLIdsIpsSensorEnabled = _CLIdsIpsSensorEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 1, 1, 1, 1, 6),
    _CLIdsIpsSensorEnabled_Type()
)
cLIdsIpsSensorEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIdsIpsSensorEnabled.setStatus("current")


class _CLIdsIpsSensorFingerPrintHex_Type(OctetString):
    """Custom type cLIdsIpsSensorFingerPrintHex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_CLIdsIpsSensorFingerPrintHex_Type.__name__ = "OctetString"
_CLIdsIpsSensorFingerPrintHex_Object = MibTableColumn
cLIdsIpsSensorFingerPrintHex = _CLIdsIpsSensorFingerPrintHex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 1, 1, 1, 1, 7),
    _CLIdsIpsSensorFingerPrintHex_Type()
)
cLIdsIpsSensorFingerPrintHex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIdsIpsSensorFingerPrintHex.setStatus("current")


class _CLIdsIpsSensorPort_Type(Unsigned32):
    """Custom type cLIdsIpsSensorPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CLIdsIpsSensorPort_Type.__name__ = "Unsigned32"
_CLIdsIpsSensorPort_Object = MibTableColumn
cLIdsIpsSensorPort = _CLIdsIpsSensorPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 1, 1, 1, 1, 8),
    _CLIdsIpsSensorPort_Type()
)
cLIdsIpsSensorPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIdsIpsSensorPort.setStatus("current")
_CLIdsIpsSensorRowStatus_Type = RowStatus
_CLIdsIpsSensorRowStatus_Object = MibTableColumn
cLIdsIpsSensorRowStatus = _CLIdsIpsSensorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 1, 1, 1, 1, 9),
    _CLIdsIpsSensorRowStatus_Type()
)
cLIdsIpsSensorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIdsIpsSensorRowStatus.setStatus("current")
_CiscoLwappIdsStatus_ObjectIdentity = ObjectIdentity
ciscoLwappIdsStatus = _CiscoLwappIdsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 1, 2)
)
_CLIdsClientExclTable_Object = MibTable
cLIdsClientExclTable = _CLIdsClientExclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cLIdsClientExclTable.setStatus("current")
_CLIdsClientExclEntry_Object = MibTableRow
cLIdsClientExclEntry = _CLIdsClientExclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 1, 2, 1, 1)
)
cLIdsClientExclEntry.setIndexNames(
    (0, "CISCO-LWAPP-IDS-MIB", "cLIdsIpsSensorAddressType"),
    (0, "CISCO-LWAPP-IDS-MIB", "cLIdsIpsSensorAddress"),
    (0, "CISCO-LWAPP-IDS-MIB", "cLIdsClientAddressType"),
    (0, "CISCO-LWAPP-IDS-MIB", "cLIdsClientAddress"),
)
if mibBuilder.loadTexts:
    cLIdsClientExclEntry.setStatus("current")
_CLIdsClientAddressType_Type = InetAddressType
_CLIdsClientAddressType_Object = MibTableColumn
cLIdsClientAddressType = _CLIdsClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 1, 2, 1, 1, 1),
    _CLIdsClientAddressType_Type()
)
cLIdsClientAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLIdsClientAddressType.setStatus("current")
_CLIdsClientAddress_Type = InetAddress
_CLIdsClientAddress_Object = MibTableColumn
cLIdsClientAddress = _CLIdsClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 1, 2, 1, 1, 2),
    _CLIdsClientAddress_Type()
)
cLIdsClientAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLIdsClientAddress.setStatus("current")
_CLIdsClientTimeRemaining_Type = TimeInterval
_CLIdsClientTimeRemaining_Object = MibTableColumn
cLIdsClientTimeRemaining = _CLIdsClientTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 1, 2, 1, 1, 3),
    _CLIdsClientTimeRemaining_Type()
)
cLIdsClientTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIdsClientTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    cLIdsClientTimeRemaining.setUnits("hundredths-seconds")
_CiscoLwappIdsMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappIdsMIBConform = _CiscoLwappIdsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 2)
)
_CiscoLwappIdsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappIdsMIBCompliances = _CiscoLwappIdsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 2, 1)
)
_CiscoLwappIdsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappIdsMIBGroups = _CiscoLwappIdsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 2, 2)
)

# Managed Objects groups

ciscoLwappIdsConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 2, 2, 1)
)
ciscoLwappIdsConfigGroup.setObjects(
      *(("CISCO-LWAPP-IDS-MIB", "cLIdsIpsSensorUserName"),
        ("CISCO-LWAPP-IDS-MIB", "cLIdsIpsSensorPassword"),
        ("CISCO-LWAPP-IDS-MIB", "cLIdsIpsSensorQueryInterval"),
        ("CISCO-LWAPP-IDS-MIB", "cLIdsIpsSensorEnabled"),
        ("CISCO-LWAPP-IDS-MIB", "cLIdsIpsSensorFingerPrintHex"),
        ("CISCO-LWAPP-IDS-MIB", "cLIdsIpsSensorPort"),
        ("CISCO-LWAPP-IDS-MIB", "cLIdsIpsSensorRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappIdsConfigGroup.setStatus("current")

ciscoLwappIdsStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 2, 2, 2)
)
ciscoLwappIdsStatusGroup.setObjects(
    ("CISCO-LWAPP-IDS-MIB", "cLIdsClientTimeRemaining")
)
if mibBuilder.loadTexts:
    ciscoLwappIdsStatusGroup.setStatus("current")


# Notification objects

ciscoLwappIdsShunClientUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 0, 1)
)
ciscoLwappIdsShunClientUpdate.setObjects(
    ("CISCO-LWAPP-IDS-MIB", "cLIdsClientTimeRemaining")
)
if mibBuilder.loadTexts:
    ciscoLwappIdsShunClientUpdate.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappIdsNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 2, 2, 3)
)
ciscoLwappIdsNotifsGroup.setObjects(
    ("CISCO-LWAPP-IDS-MIB", "ciscoLwappIdsShunClientUpdate")
)
if mibBuilder.loadTexts:
    ciscoLwappIdsNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappIdsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 519, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappIdsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-IDS-MIB",
    **{"ciscoLwappIdsMIB": ciscoLwappIdsMIB,
       "ciscoLwappIdsMIBNotifs": ciscoLwappIdsMIBNotifs,
       "ciscoLwappIdsShunClientUpdate": ciscoLwappIdsShunClientUpdate,
       "ciscoLwappIdsMIBObjects": ciscoLwappIdsMIBObjects,
       "ciscoLwappIdsConfig": ciscoLwappIdsConfig,
       "cLIdsIpsSensorConfigTable": cLIdsIpsSensorConfigTable,
       "cLIdsIpsSensorConfigEntry": cLIdsIpsSensorConfigEntry,
       "cLIdsIpsSensorAddressType": cLIdsIpsSensorAddressType,
       "cLIdsIpsSensorAddress": cLIdsIpsSensorAddress,
       "cLIdsIpsSensorUserName": cLIdsIpsSensorUserName,
       "cLIdsIpsSensorPassword": cLIdsIpsSensorPassword,
       "cLIdsIpsSensorQueryInterval": cLIdsIpsSensorQueryInterval,
       "cLIdsIpsSensorEnabled": cLIdsIpsSensorEnabled,
       "cLIdsIpsSensorFingerPrintHex": cLIdsIpsSensorFingerPrintHex,
       "cLIdsIpsSensorPort": cLIdsIpsSensorPort,
       "cLIdsIpsSensorRowStatus": cLIdsIpsSensorRowStatus,
       "ciscoLwappIdsStatus": ciscoLwappIdsStatus,
       "cLIdsClientExclTable": cLIdsClientExclTable,
       "cLIdsClientExclEntry": cLIdsClientExclEntry,
       "cLIdsClientAddressType": cLIdsClientAddressType,
       "cLIdsClientAddress": cLIdsClientAddress,
       "cLIdsClientTimeRemaining": cLIdsClientTimeRemaining,
       "ciscoLwappIdsMIBConform": ciscoLwappIdsMIBConform,
       "ciscoLwappIdsMIBCompliances": ciscoLwappIdsMIBCompliances,
       "ciscoLwappIdsMIBCompliance": ciscoLwappIdsMIBCompliance,
       "ciscoLwappIdsMIBGroups": ciscoLwappIdsMIBGroups,
       "ciscoLwappIdsConfigGroup": ciscoLwappIdsConfigGroup,
       "ciscoLwappIdsStatusGroup": ciscoLwappIdsStatusGroup,
       "ciscoLwappIdsNotifsGroup": ciscoLwappIdsNotifsGroup}
)
