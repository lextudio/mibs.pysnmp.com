# SNMP MIB module (NETAL-PRODUCTS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETAL-PRODUCTS
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:27 2024
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

(netalModules,
 netalProducts,
 networkAlchemy) = mibBuilder.importSymbols(
    "NETAL-SMI",
    "netalModules",
    "netalProducts",
    "networkAlchemy")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

netalProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 5, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NetalHardwareUnknown_ObjectIdentity = ObjectIdentity
netalHardwareUnknown = _NetalHardwareUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 1, 1)
)
if mibBuilder.loadTexts:
    netalHardwareUnknown.setStatus("current")
_NetalKiltlifterUnknown_ObjectIdentity = ObjectIdentity
netalKiltlifterUnknown = _NetalKiltlifterUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 1, 2)
)
if mibBuilder.loadTexts:
    netalKiltlifterUnknown.setStatus("current")
_NetalStingrayUnknown_ObjectIdentity = ObjectIdentity
netalStingrayUnknown = _NetalStingrayUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 1, 3)
)
if mibBuilder.loadTexts:
    netalStingrayUnknown.setStatus("current")
_NetalCryptoCluster500_ObjectIdentity = ObjectIdentity
netalCryptoCluster500 = _NetalCryptoCluster500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 1, 4)
)
if mibBuilder.loadTexts:
    netalCryptoCluster500.setStatus("current")
_NetalCryptoCluster5010_ObjectIdentity = ObjectIdentity
netalCryptoCluster5010 = _NetalCryptoCluster5010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 1, 5)
)
if mibBuilder.loadTexts:
    netalCryptoCluster5010.setStatus("current")
_NetalCryptoCluster501_ObjectIdentity = ObjectIdentity
netalCryptoCluster501 = _NetalCryptoCluster501_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 1, 8)
)
if mibBuilder.loadTexts:
    netalCryptoCluster501.setStatus("current")
_NetalCryptoCluster5000_ObjectIdentity = ObjectIdentity
netalCryptoCluster5000 = _NetalCryptoCluster5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 1, 10)
)
if mibBuilder.loadTexts:
    netalCryptoCluster5000.setStatus("current")
_NetalCryptoCluster2500_ObjectIdentity = ObjectIdentity
netalCryptoCluster2500 = _NetalCryptoCluster2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 1, 11)
)
if mibBuilder.loadTexts:
    netalCryptoCluster2500.setStatus("current")
_NetalCryptoCluster2501_ObjectIdentity = ObjectIdentity
netalCryptoCluster2501 = _NetalCryptoCluster2501_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 1, 12)
)
if mibBuilder.loadTexts:
    netalCryptoCluster2501.setStatus("current")
_NetalFreeBSDApplication_ObjectIdentity = ObjectIdentity
netalFreeBSDApplication = _NetalFreeBSDApplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 1, 13)
)
if mibBuilder.loadTexts:
    netalFreeBSDApplication.setStatus("current")
_NetalCryptoCluster5200_ObjectIdentity = ObjectIdentity
netalCryptoCluster5200 = _NetalCryptoCluster5200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 1, 15)
)
if mibBuilder.loadTexts:
    netalCryptoCluster5200.setStatus("current")
_NetalCryptoCluster5205_ObjectIdentity = ObjectIdentity
netalCryptoCluster5205 = _NetalCryptoCluster5205_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 1, 16)
)
if mibBuilder.loadTexts:
    netalCryptoCluster5205.setStatus("current")
_NetalCA200_ObjectIdentity = ObjectIdentity
netalCA200 = _NetalCA200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 1, 18)
)
if mibBuilder.loadTexts:
    netalCA200.setStatus("current")
_NetalCA600_ObjectIdentity = ObjectIdentity
netalCA600 = _NetalCA600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 1, 19)
)
if mibBuilder.loadTexts:
    netalCA600.setStatus("current")
_NetalChameleon100_ObjectIdentity = ObjectIdentity
netalChameleon100 = _NetalChameleon100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 1, 20)
)
if mibBuilder.loadTexts:
    netalChameleon100.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETAL-PRODUCTS",
    **{"netalHardwareUnknown": netalHardwareUnknown,
       "netalKiltlifterUnknown": netalKiltlifterUnknown,
       "netalStingrayUnknown": netalStingrayUnknown,
       "netalCryptoCluster500": netalCryptoCluster500,
       "netalCryptoCluster5010": netalCryptoCluster5010,
       "netalCryptoCluster501": netalCryptoCluster501,
       "netalCryptoCluster5000": netalCryptoCluster5000,
       "netalCryptoCluster2500": netalCryptoCluster2500,
       "netalCryptoCluster2501": netalCryptoCluster2501,
       "netalFreeBSDApplication": netalFreeBSDApplication,
       "netalCryptoCluster5200": netalCryptoCluster5200,
       "netalCryptoCluster5205": netalCryptoCluster5205,
       "netalCA200": netalCA200,
       "netalCA600": netalCA600,
       "netalChameleon100": netalChameleon100,
       "netalProductsMIB": netalProductsMIB}
)
