# SNMP MIB module (ACMEPACKET-PRODUCTS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACMEPACKET-PRODUCTS
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:34 2024
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

(acmepacket,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacket")

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

acmepacketProducts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1)
)
acmepacketProducts.setRevisions(
        ("2012-07-16 00:00",
         "2007-04-03 15:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApNetNet4000Series_ObjectIdentity = ObjectIdentity
apNetNet4000Series = _ApNetNet4000Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 1)
)
if mibBuilder.loadTexts:
    apNetNet4000Series.setStatus("current")
_ApNetNet4250_ObjectIdentity = ObjectIdentity
apNetNet4250 = _ApNetNet4250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 1, 1)
)
if mibBuilder.loadTexts:
    apNetNet4250.setStatus("current")
_ApNetNet4500_ObjectIdentity = ObjectIdentity
apNetNet4500 = _ApNetNet4500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 1, 2)
)
if mibBuilder.loadTexts:
    apNetNet4500.setStatus("current")
_ApNetNet9000Series_ObjectIdentity = ObjectIdentity
apNetNet9000Series = _ApNetNet9000Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 2)
)
if mibBuilder.loadTexts:
    apNetNet9000Series.setStatus("current")
_ApNetNet9200_ObjectIdentity = ObjectIdentity
apNetNet9200 = _ApNetNet9200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 2, 1)
)
if mibBuilder.loadTexts:
    apNetNet9200.setStatus("current")
_ApNetNet3000Series_ObjectIdentity = ObjectIdentity
apNetNet3000Series = _ApNetNet3000Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 3)
)
if mibBuilder.loadTexts:
    apNetNet3000Series.setStatus("current")
_ApNetNet3800_ObjectIdentity = ObjectIdentity
apNetNet3800 = _ApNetNet3800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 3, 1)
)
if mibBuilder.loadTexts:
    apNetNet3800.setStatus("current")
_ApNetNet3820_ObjectIdentity = ObjectIdentity
apNetNet3820 = _ApNetNet3820_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 3, 2)
)
if mibBuilder.loadTexts:
    apNetNet3820.setStatus("current")
_ApNetNetOSSeries_ObjectIdentity = ObjectIdentity
apNetNetOSSeries = _ApNetNetOSSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 4)
)
if mibBuilder.loadTexts:
    apNetNetOSSeries.setStatus("current")
_ApNetNetOS_ObjectIdentity = ObjectIdentity
apNetNetOS = _ApNetNetOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 4, 1)
)
if mibBuilder.loadTexts:
    apNetNetOS.setStatus("current")
_ApNetNetOSVM_ObjectIdentity = ObjectIdentity
apNetNetOSVM = _ApNetNetOSVM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 4, 2)
)
if mibBuilder.loadTexts:
    apNetNetOSVM.setStatus("current")
_ApNetNet6000Series_ObjectIdentity = ObjectIdentity
apNetNet6000Series = _ApNetNet6000Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 5)
)
if mibBuilder.loadTexts:
    apNetNet6000Series.setStatus("current")
_ApNetNet6300_ObjectIdentity = ObjectIdentity
apNetNet6300 = _ApNetNet6300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 5, 1)
)
if mibBuilder.loadTexts:
    apNetNet6300.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACMEPACKET-PRODUCTS",
    **{"acmepacketProducts": acmepacketProducts,
       "apNetNet4000Series": apNetNet4000Series,
       "apNetNet4250": apNetNet4250,
       "apNetNet4500": apNetNet4500,
       "apNetNet9000Series": apNetNet9000Series,
       "apNetNet9200": apNetNet9200,
       "apNetNet3000Series": apNetNet3000Series,
       "apNetNet3800": apNetNet3800,
       "apNetNet3820": apNetNet3820,
       "apNetNetOSSeries": apNetNetOSSeries,
       "apNetNetOS": apNetNetOS,
       "apNetNetOSVM": apNetNetOSVM,
       "apNetNet6000Series": apNetNet6000Series,
       "apNetNet6300": apNetNet6300}
)
