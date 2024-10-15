# SNMP MIB module (ARISTA-SNMP-TRANSPORTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARISTA-SNMP-TRANSPORTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:27 2024
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

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
 TAddress,
 TDomain,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TAddress",
    "TDomain",
    "TextualConvention")


# MODULE-IDENTITY

aristaSnmpTransportMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 10)
)
aristaSnmpTransportMIB.setRevisions(
        ("2014-08-15 00:00",
         "2012-01-09 13:00",
         "2012-01-05 18:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TransportAddressIPv4NS(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d.1d.1d.1d:2d@*1t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 255),
    )



class TransportAddressIPv6NS(OctetString, TextualConvention):
    status = "current"
    displayHint = "0a[2x:2x:2x:2x:2x:2x:2x:2x]0a:2d@*1t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 255),
    )



# MIB Managed Objects in the order of their OIDs

_AristaUDPNSDomain_ObjectIdentity = ObjectIdentity
aristaUDPNSDomain = _AristaUDPNSDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 10, 1)
)
if mibBuilder.loadTexts:
    aristaUDPNSDomain.setStatus("current")
_AristaTCPNSDomain_ObjectIdentity = ObjectIdentity
aristaTCPNSDomain = _AristaTCPNSDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 10, 2)
)
if mibBuilder.loadTexts:
    aristaTCPNSDomain.setStatus("current")
_AristaUDPNS6Domain_ObjectIdentity = ObjectIdentity
aristaUDPNS6Domain = _AristaUDPNS6Domain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 10, 3)
)
if mibBuilder.loadTexts:
    aristaUDPNS6Domain.setStatus("current")
_AristaTCPNS6Domain_ObjectIdentity = ObjectIdentity
aristaTCPNS6Domain = _AristaTCPNS6Domain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 10, 4)
)
if mibBuilder.loadTexts:
    aristaTCPNS6Domain.setStatus("current")
_AristaAuthFailTrapObjects_ObjectIdentity = ObjectIdentity
aristaAuthFailTrapObjects = _AristaAuthFailTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 10, 5)
)
_AristaAuthFailTrapTDomain_Type = TDomain
_AristaAuthFailTrapTDomain_Object = MibScalar
aristaAuthFailTrapTDomain = _AristaAuthFailTrapTDomain_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 10, 5, 1),
    _AristaAuthFailTrapTDomain_Type()
)
aristaAuthFailTrapTDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaAuthFailTrapTDomain.setStatus("current")
_AristaAuthFailTrapSrcTAddress_Type = TAddress
_AristaAuthFailTrapSrcTAddress_Object = MibScalar
aristaAuthFailTrapSrcTAddress = _AristaAuthFailTrapSrcTAddress_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 10, 5, 2),
    _AristaAuthFailTrapSrcTAddress_Type()
)
aristaAuthFailTrapSrcTAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaAuthFailTrapSrcTAddress.setStatus("current")
_AristaTransportConformance_ObjectIdentity = ObjectIdentity
aristaTransportConformance = _AristaTransportConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 10, 6)
)
_AristaAuthFailTrapGroups_ObjectIdentity = ObjectIdentity
aristaAuthFailTrapGroups = _AristaAuthFailTrapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 10, 6, 1)
)
_AristaAuthFailCompliances_ObjectIdentity = ObjectIdentity
aristaAuthFailCompliances = _AristaAuthFailCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 10, 6, 2)
)

# Managed Objects groups

aristaAuthFailTrapObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 10, 6, 1, 1)
)
aristaAuthFailTrapObjectsGroup.setObjects(
      *(("ARISTA-SNMP-TRANSPORTS-MIB", "aristaAuthFailTrapTDomain"),
        ("ARISTA-SNMP-TRANSPORTS-MIB", "aristaAuthFailTrapSrcTAddress"))
)
if mibBuilder.loadTexts:
    aristaAuthFailTrapObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aristaAuthFailCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 10, 6, 2, 1)
)
if mibBuilder.loadTexts:
    aristaAuthFailCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-SNMP-TRANSPORTS-MIB",
    **{"TransportAddressIPv4NS": TransportAddressIPv4NS,
       "TransportAddressIPv6NS": TransportAddressIPv6NS,
       "aristaSnmpTransportMIB": aristaSnmpTransportMIB,
       "aristaUDPNSDomain": aristaUDPNSDomain,
       "aristaTCPNSDomain": aristaTCPNSDomain,
       "aristaUDPNS6Domain": aristaUDPNS6Domain,
       "aristaTCPNS6Domain": aristaTCPNS6Domain,
       "aristaAuthFailTrapObjects": aristaAuthFailTrapObjects,
       "aristaAuthFailTrapTDomain": aristaAuthFailTrapTDomain,
       "aristaAuthFailTrapSrcTAddress": aristaAuthFailTrapSrcTAddress,
       "aristaTransportConformance": aristaTransportConformance,
       "aristaAuthFailTrapGroups": aristaAuthFailTrapGroups,
       "aristaAuthFailTrapObjectsGroup": aristaAuthFailTrapObjectsGroup,
       "aristaAuthFailCompliances": aristaAuthFailCompliances,
       "aristaAuthFailCompliance": aristaAuthFailCompliance}
)
