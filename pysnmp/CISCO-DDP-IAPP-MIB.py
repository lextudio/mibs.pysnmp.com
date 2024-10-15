# SNMP MIB module (CISCO-DDP-IAPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DDP-IAPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:54 2024
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

(CiscoPort,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoPort")

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

(DisplayString,
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoDdpIappMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 277)
)
ciscoDdpIappMIB.setRevisions(
        ("2002-07-31 00:00",
         "2002-07-17 00:00",
         "2002-03-19 00:00",
         "2002-03-07 00:00",
         "2001-09-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoDdpIappMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoDdpIappMIBNotifications = _CiscoDdpIappMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 277, 0)
)
_CiscoDdpIappMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDdpIappMIBObjects = _CiscoDdpIappMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 277, 1)
)
_CDdpIappGlobalConfig_ObjectIdentity = ObjectIdentity
cDdpIappGlobalConfig = _CDdpIappGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1)
)
_CDdpIappMcastIpAddrType_Type = InetAddressType
_CDdpIappMcastIpAddrType_Object = MibScalar
cDdpIappMcastIpAddrType = _CDdpIappMcastIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1, 1),
    _CDdpIappMcastIpAddrType_Type()
)
cDdpIappMcastIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDdpIappMcastIpAddrType.setStatus("current")


class _CDdpIappMcastIpAddr_Type(InetAddress):
    """Custom type cDdpIappMcastIpAddr based on InetAddress"""
    defaultHexValue = "e0000128"


_CDdpIappMcastIpAddr_Object = MibScalar
cDdpIappMcastIpAddr = _CDdpIappMcastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1, 2),
    _CDdpIappMcastIpAddr_Type()
)
cDdpIappMcastIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDdpIappMcastIpAddr.setStatus("current")


class _CDdpIappPort_Type(CiscoPort):
    """Custom type cDdpIappPort based on CiscoPort"""
    defaultValue = 2887


_CDdpIappPort_Object = MibScalar
cDdpIappPort = _CDdpIappPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1, 3),
    _CDdpIappPort_Type()
)
cDdpIappPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDdpIappPort.setStatus("current")


class _CDdpIappRogueApNotifEnabled_Type(TruthValue):
    """Custom type cDdpIappRogueApNotifEnabled based on TruthValue"""


_CDdpIappRogueApNotifEnabled_Object = MibScalar
cDdpIappRogueApNotifEnabled = _CDdpIappRogueApNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1, 4),
    _CDdpIappRogueApNotifEnabled_Type()
)
cDdpIappRogueApNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDdpIappRogueApNotifEnabled.setStatus("current")
_CDdpIappRogueApInfo_ObjectIdentity = ObjectIdentity
cDdpIappRogueApInfo = _CDdpIappRogueApInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 2)
)


class _CDdpIappLastRogueApMacAddr_Type(MacAddress):
    """Custom type cDdpIappLastRogueApMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_CDdpIappLastRogueApMacAddr_Object = MibScalar
cDdpIappLastRogueApMacAddr = _CDdpIappLastRogueApMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 2, 1),
    _CDdpIappLastRogueApMacAddr_Type()
)
cDdpIappLastRogueApMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDdpIappLastRogueApMacAddr.setStatus("current")
_CiscoDdpIappMIBConformance_ObjectIdentity = ObjectIdentity
ciscoDdpIappMIBConformance = _CiscoDdpIappMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 277, 2)
)
_CiscoDdpIappMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDdpIappMIBCompliances = _CiscoDdpIappMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 1)
)
_CiscoDdpIappMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDdpIappMIBGroups = _CiscoDdpIappMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 2)
)

# Managed Objects groups

ciscoDdpIappConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 2, 1)
)
ciscoDdpIappConfigGroup.setObjects(
      *(("CISCO-DDP-IAPP-MIB", "cDdpIappMcastIpAddrType"),
        ("CISCO-DDP-IAPP-MIB", "cDdpIappMcastIpAddr"),
        ("CISCO-DDP-IAPP-MIB", "cDdpIappPort"),
        ("CISCO-DDP-IAPP-MIB", "cDdpIappRogueApNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoDdpIappConfigGroup.setStatus("current")

ciscoDdpIappRogueApInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 2, 2)
)
ciscoDdpIappRogueApInfoGroup.setObjects(
    ("CISCO-DDP-IAPP-MIB", "cDdpIappLastRogueApMacAddr")
)
if mibBuilder.loadTexts:
    ciscoDdpIappRogueApInfoGroup.setStatus("current")


# Notification objects

cDdpIappLastRogueApNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 277, 0, 1)
)
cDdpIappLastRogueApNotif.setObjects(
    ("CISCO-DDP-IAPP-MIB", "cDdpIappLastRogueApMacAddr")
)
if mibBuilder.loadTexts:
    cDdpIappLastRogueApNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoDdpIappNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 2, 3)
)
ciscoDdpIappNotificationGroup.setObjects(
    ("CISCO-DDP-IAPP-MIB", "cDdpIappLastRogueApNotif")
)
if mibBuilder.loadTexts:
    ciscoDdpIappNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoDdpIappCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDdpIappCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DDP-IAPP-MIB",
    **{"ciscoDdpIappMIB": ciscoDdpIappMIB,
       "ciscoDdpIappMIBNotifications": ciscoDdpIappMIBNotifications,
       "cDdpIappLastRogueApNotif": cDdpIappLastRogueApNotif,
       "ciscoDdpIappMIBObjects": ciscoDdpIappMIBObjects,
       "cDdpIappGlobalConfig": cDdpIappGlobalConfig,
       "cDdpIappMcastIpAddrType": cDdpIappMcastIpAddrType,
       "cDdpIappMcastIpAddr": cDdpIappMcastIpAddr,
       "cDdpIappPort": cDdpIappPort,
       "cDdpIappRogueApNotifEnabled": cDdpIappRogueApNotifEnabled,
       "cDdpIappRogueApInfo": cDdpIappRogueApInfo,
       "cDdpIappLastRogueApMacAddr": cDdpIappLastRogueApMacAddr,
       "ciscoDdpIappMIBConformance": ciscoDdpIappMIBConformance,
       "ciscoDdpIappMIBCompliances": ciscoDdpIappMIBCompliances,
       "ciscoDdpIappCompliance": ciscoDdpIappCompliance,
       "ciscoDdpIappMIBGroups": ciscoDdpIappMIBGroups,
       "ciscoDdpIappConfigGroup": ciscoDdpIappConfigGroup,
       "ciscoDdpIappRogueApInfoGroup": ciscoDdpIappRogueApInfoGroup,
       "ciscoDdpIappNotificationGroup": ciscoDdpIappNotificationGroup}
)
