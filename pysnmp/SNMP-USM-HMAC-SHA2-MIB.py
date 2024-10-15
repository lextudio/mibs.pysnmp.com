# SNMP MIB module (SNMP-USM-HMAC-SHA2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNMP-USM-HMAC-SHA2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:10 2024
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

(snmpAuthProtocols,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "snmpAuthProtocols")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

snmpUsmHmacSha2MIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 235)
)
snmpUsmHmacSha2MIB.setRevisions(
        ("2016-04-18 00:00",
         "2015-10-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsmHMAC128SHA224AuthProtocol_ObjectIdentity = ObjectIdentity
usmHMAC128SHA224AuthProtocol = _UsmHMAC128SHA224AuthProtocol_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 10, 1, 1, 4)
)
if mibBuilder.loadTexts:
    usmHMAC128SHA224AuthProtocol.setStatus("current")
_UsmHMAC192SHA256AuthProtocol_ObjectIdentity = ObjectIdentity
usmHMAC192SHA256AuthProtocol = _UsmHMAC192SHA256AuthProtocol_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 10, 1, 1, 5)
)
if mibBuilder.loadTexts:
    usmHMAC192SHA256AuthProtocol.setStatus("current")
_UsmHMAC256SHA384AuthProtocol_ObjectIdentity = ObjectIdentity
usmHMAC256SHA384AuthProtocol = _UsmHMAC256SHA384AuthProtocol_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 10, 1, 1, 6)
)
if mibBuilder.loadTexts:
    usmHMAC256SHA384AuthProtocol.setStatus("current")
_UsmHMAC384SHA512AuthProtocol_ObjectIdentity = ObjectIdentity
usmHMAC384SHA512AuthProtocol = _UsmHMAC384SHA512AuthProtocol_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 10, 1, 1, 7)
)
if mibBuilder.loadTexts:
    usmHMAC384SHA512AuthProtocol.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP-USM-HMAC-SHA2-MIB",
    **{"snmpUsmHmacSha2MIB": snmpUsmHmacSha2MIB,
       "usmHMAC128SHA224AuthProtocol": usmHMAC128SHA224AuthProtocol,
       "usmHMAC192SHA256AuthProtocol": usmHMAC192SHA256AuthProtocol,
       "usmHMAC256SHA384AuthProtocol": usmHMAC256SHA384AuthProtocol,
       "usmHMAC384SHA512AuthProtocol": usmHMAC384SHA512AuthProtocol}
)
