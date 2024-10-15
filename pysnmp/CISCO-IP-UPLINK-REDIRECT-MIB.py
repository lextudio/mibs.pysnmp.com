# SNMP MIB module (CISCO-IP-UPLINK-REDIRECT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IP-UPLINK-REDIRECT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:47 2024
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

ciscoIpUplinkRedirectMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 191)
)
ciscoIpUplinkRedirectMIB.setRevisions(
        ("2001-01-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIpUplinkRedirectMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIpUplinkRedirectMIBObjects = _CiscoIpUplinkRedirectMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 191, 1)
)
_CiurStartupStatus_Type = TruthValue
_CiurStartupStatus_Object = MibScalar
ciurStartupStatus = _CiurStartupStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 191, 1, 1),
    _CiurStartupStatus_Type()
)
ciurStartupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciurStartupStatus.setStatus("current")
_CiurOperStatus_Type = TruthValue
_CiurOperStatus_Object = MibScalar
ciurOperStatus = _CiurOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 191, 1, 2),
    _CiurOperStatus_Type()
)
ciurOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciurOperStatus.setStatus("current")
_CiscoIpUplinkRedirectMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoIpUplinkRedirectMIBNotificationPrefix = _CiscoIpUplinkRedirectMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 191, 2)
)
_CiscoIpUplinkRedirectMIBConformance_ObjectIdentity = ObjectIdentity
ciscoIpUplinkRedirectMIBConformance = _CiscoIpUplinkRedirectMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 191, 3)
)
_CiscoIpUplinkRedirectMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIpUplinkRedirectMIBCompliances = _CiscoIpUplinkRedirectMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 191, 3, 1)
)
_CiscoIpUplinkRedirectMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIpUplinkRedirectMIBGroups = _CiscoIpUplinkRedirectMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 191, 3, 2)
)

# Managed Objects groups

ciscoIpUplinkRedirectMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 191, 3, 2, 1)
)
ciscoIpUplinkRedirectMIBGroup.setObjects(
      *(("CISCO-IP-UPLINK-REDIRECT-MIB", "ciurStartupStatus"),
        ("CISCO-IP-UPLINK-REDIRECT-MIB", "ciurOperStatus"))
)
if mibBuilder.loadTexts:
    ciscoIpUplinkRedirectMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIpUplinkRedirectMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 191, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIpUplinkRedirectMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IP-UPLINK-REDIRECT-MIB",
    **{"ciscoIpUplinkRedirectMIB": ciscoIpUplinkRedirectMIB,
       "ciscoIpUplinkRedirectMIBObjects": ciscoIpUplinkRedirectMIBObjects,
       "ciurStartupStatus": ciurStartupStatus,
       "ciurOperStatus": ciurOperStatus,
       "ciscoIpUplinkRedirectMIBNotificationPrefix": ciscoIpUplinkRedirectMIBNotificationPrefix,
       "ciscoIpUplinkRedirectMIBConformance": ciscoIpUplinkRedirectMIBConformance,
       "ciscoIpUplinkRedirectMIBCompliances": ciscoIpUplinkRedirectMIBCompliances,
       "ciscoIpUplinkRedirectMIBCompliance": ciscoIpUplinkRedirectMIBCompliance,
       "ciscoIpUplinkRedirectMIBGroups": ciscoIpUplinkRedirectMIBGroups,
       "ciscoIpUplinkRedirectMIBGroup": ciscoIpUplinkRedirectMIBGroup}
)
