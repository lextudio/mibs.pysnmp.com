# SNMP MIB module (CISCO-TM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-TM
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:43 2024
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

(ciscoDomains,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoDomains")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

ciscoTransportMappings = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 19, 1)
)
ciscoTransportMappings.setRevisions(
        ("2001-08-23 16:00",
         "2000-06-21 16:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SnmpUDPVPNAddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d.1d.1d.1d/2d/32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 38),
    )



class SnmpAAL5VCIdentifier(OctetString, TextualConvention):
    status = "current"
    displayHint = "4d/4d/4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )



class SnmpCNSIdentifier(OctetString, TextualConvention):
    status = "current"
    displayHint = "19a.255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 274),
    )



# MIB Managed Objects in the order of their OIDs

_SnmpUDPVPNDomain_ObjectIdentity = ObjectIdentity
snmpUDPVPNDomain = _SnmpUDPVPNDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 19, 1, 1)
)
if mibBuilder.loadTexts:
    snmpUDPVPNDomain.setStatus("current")
_SnmpAAL5Domain_ObjectIdentity = ObjectIdentity
snmpAAL5Domain = _SnmpAAL5Domain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 19, 1, 2)
)
if mibBuilder.loadTexts:
    snmpAAL5Domain.setStatus("current")
_SnmpCNSDomain_ObjectIdentity = ObjectIdentity
snmpCNSDomain = _SnmpCNSDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 19, 1, 3)
)
if mibBuilder.loadTexts:
    snmpCNSDomain.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TM",
    **{"SnmpUDPVPNAddress": SnmpUDPVPNAddress,
       "SnmpAAL5VCIdentifier": SnmpAAL5VCIdentifier,
       "SnmpCNSIdentifier": SnmpCNSIdentifier,
       "ciscoTransportMappings": ciscoTransportMappings,
       "snmpUDPVPNDomain": snmpUDPVPNDomain,
       "snmpAAL5Domain": snmpAAL5Domain,
       "snmpCNSDomain": snmpCNSDomain}
)
