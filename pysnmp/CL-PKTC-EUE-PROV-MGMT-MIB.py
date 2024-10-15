# SNMP MIB module (CL-PKTC-EUE-PROV-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CL-PKTC-EUE-PROV-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:32 2024
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

(pktcEUEMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "pktcEUEMibs")

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
 Bits,
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

pktcEUEProvMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PktcEUEProvMgmtNotifications_ObjectIdentity = ObjectIdentity
pktcEUEProvMgmtNotifications = _PktcEUEProvMgmtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 0)
)
_PktcEUEProvMgmtObjects_ObjectIdentity = ObjectIdentity
pktcEUEProvMgmtObjects = _PktcEUEProvMgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1)
)


class _PktcEUEProvMgmtVersion_Type(SnmpAdminString):
    """Custom type pktcEUEProvMgmtVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_PktcEUEProvMgmtVersion_Type.__name__ = "SnmpAdminString"
_PktcEUEProvMgmtVersion_Object = MibScalar
pktcEUEProvMgmtVersion = _PktcEUEProvMgmtVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1),
    _PktcEUEProvMgmtVersion_Type()
)
pktcEUEProvMgmtVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEProvMgmtVersion.setStatus("current")


class _PktcEUEDhcpv6ServerId1_Type(OctetString):
    """Custom type pktcEUEDhcpv6ServerId1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PktcEUEDhcpv6ServerId1_Type.__name__ = "OctetString"
_PktcEUEDhcpv6ServerId1_Object = MibScalar
pktcEUEDhcpv6ServerId1 = _PktcEUEDhcpv6ServerId1_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 2),
    _PktcEUEDhcpv6ServerId1_Type()
)
pktcEUEDhcpv6ServerId1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEDhcpv6ServerId1.setStatus("current")
_PktcEUEDhcpv6ServerId2_Type = InetAddress
_PktcEUEDhcpv6ServerId2_Object = MibScalar
pktcEUEDhcpv6ServerId2 = _PktcEUEDhcpv6ServerId2_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 3),
    _PktcEUEDhcpv6ServerId2_Type()
)
pktcEUEDhcpv6ServerId2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEDhcpv6ServerId2.setStatus("current")
_PktcEUEDhcpv6ServerAddressType_Type = InetAddressType
_PktcEUEDhcpv6ServerAddressType_Object = MibScalar
pktcEUEDhcpv6ServerAddressType = _PktcEUEDhcpv6ServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 4),
    _PktcEUEDhcpv6ServerAddressType_Type()
)
pktcEUEDhcpv6ServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEDhcpv6ServerAddressType.setStatus("current")
_PktcEUEDhcpv6ServerAddress_Type = InetAddress
_PktcEUEDhcpv6ServerAddress_Object = MibScalar
pktcEUEDhcpv6ServerAddress = _PktcEUEDhcpv6ServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 5),
    _PktcEUEDhcpv6ServerAddress_Type()
)
pktcEUEDhcpv6ServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEDhcpv6ServerAddress.setStatus("current")
_PktcEUEDnsv6ServerAddressType_Type = InetAddressType
_PktcEUEDnsv6ServerAddressType_Object = MibScalar
pktcEUEDnsv6ServerAddressType = _PktcEUEDnsv6ServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 6),
    _PktcEUEDnsv6ServerAddressType_Type()
)
pktcEUEDnsv6ServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEDnsv6ServerAddressType.setStatus("current")
_PktcEUEDnsv6ServerAddress1_Type = InetAddress
_PktcEUEDnsv6ServerAddress1_Object = MibScalar
pktcEUEDnsv6ServerAddress1 = _PktcEUEDnsv6ServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 7),
    _PktcEUEDnsv6ServerAddress1_Type()
)
pktcEUEDnsv6ServerAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUEDnsv6ServerAddress1.setStatus("current")
_PktcEUEDnsv6ServerAddress2_Type = InetAddress
_PktcEUEDnsv6ServerAddress2_Object = MibScalar
pktcEUEDnsv6ServerAddress2 = _PktcEUEDnsv6ServerAddress2_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 8),
    _PktcEUEDnsv6ServerAddress2_Type()
)
pktcEUEDnsv6ServerAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUEDnsv6ServerAddress2.setStatus("current")
_PktcEUEProvMgmtConformance_ObjectIdentity = ObjectIdentity
pktcEUEProvMgmtConformance = _PktcEUEProvMgmtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 2)
)
_PktcEUEProvMgmtCompliances_ObjectIdentity = ObjectIdentity
pktcEUEProvMgmtCompliances = _PktcEUEProvMgmtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 2, 1)
)
_PktcEUEProvMgmtGroups_ObjectIdentity = ObjectIdentity
pktcEUEProvMgmtGroups = _PktcEUEProvMgmtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 2, 2)
)

# Managed Objects groups

pktcEUEProvMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 2, 2, 1)
)
pktcEUEProvMgmtGroup.setObjects(
      *(("CL-PKTC-EUE-PROV-MGMT-MIB", "pktcEUEProvMgmtVersion"),
        ("CL-PKTC-EUE-PROV-MGMT-MIB", "pktcEUEDhcpv6ServerId1"),
        ("CL-PKTC-EUE-PROV-MGMT-MIB", "pktcEUEDhcpv6ServerId2"),
        ("CL-PKTC-EUE-PROV-MGMT-MIB", "pktcEUEDhcpv6ServerAddressType"),
        ("CL-PKTC-EUE-PROV-MGMT-MIB", "pktcEUEDhcpv6ServerAddress"),
        ("CL-PKTC-EUE-PROV-MGMT-MIB", "pktcEUEDnsv6ServerAddressType"),
        ("CL-PKTC-EUE-PROV-MGMT-MIB", "pktcEUEDnsv6ServerAddress1"),
        ("CL-PKTC-EUE-PROV-MGMT-MIB", "pktcEUEDnsv6ServerAddress2"))
)
if mibBuilder.loadTexts:
    pktcEUEProvMgmtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pktcEUEProvMgmtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pktcEUEProvMgmtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CL-PKTC-EUE-PROV-MGMT-MIB",
    **{"pktcEUEProvMgmtMIB": pktcEUEProvMgmtMIB,
       "pktcEUEProvMgmtNotifications": pktcEUEProvMgmtNotifications,
       "pktcEUEProvMgmtObjects": pktcEUEProvMgmtObjects,
       "pktcEUEProvMgmtVersion": pktcEUEProvMgmtVersion,
       "pktcEUEDhcpv6ServerId1": pktcEUEDhcpv6ServerId1,
       "pktcEUEDhcpv6ServerId2": pktcEUEDhcpv6ServerId2,
       "pktcEUEDhcpv6ServerAddressType": pktcEUEDhcpv6ServerAddressType,
       "pktcEUEDhcpv6ServerAddress": pktcEUEDhcpv6ServerAddress,
       "pktcEUEDnsv6ServerAddressType": pktcEUEDnsv6ServerAddressType,
       "pktcEUEDnsv6ServerAddress1": pktcEUEDnsv6ServerAddress1,
       "pktcEUEDnsv6ServerAddress2": pktcEUEDnsv6ServerAddress2,
       "pktcEUEProvMgmtConformance": pktcEUEProvMgmtConformance,
       "pktcEUEProvMgmtCompliances": pktcEUEProvMgmtCompliances,
       "pktcEUEProvMgmtCompliance": pktcEUEProvMgmtCompliance,
       "pktcEUEProvMgmtGroups": pktcEUEProvMgmtGroups,
       "pktcEUEProvMgmtGroup": pktcEUEProvMgmtGroup}
)
