# SNMP MIB module (GNOME-PRODUCT-ZEBRA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GNOME-PRODUCT-ZEBRA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:48 2024
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

(gnomeProducts,) = mibBuilder.importSymbols(
    "GNOME-SMI",
    "gnomeProducts")

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

zebra = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3319, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zserv_ObjectIdentity = ObjectIdentity
zserv = _Zserv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3319, 1, 2, 1)
)
if mibBuilder.loadTexts:
    zserv.setStatus("current")
_Bgpd_ObjectIdentity = ObjectIdentity
bgpd = _Bgpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3319, 1, 2, 2)
)
if mibBuilder.loadTexts:
    bgpd.setStatus("current")
_Ripd_ObjectIdentity = ObjectIdentity
ripd = _Ripd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3319, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ripd.setStatus("current")
_Ripngd_ObjectIdentity = ObjectIdentity
ripngd = _Ripngd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3319, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ripngd.setStatus("current")
_Ospfd_ObjectIdentity = ObjectIdentity
ospfd = _Ospfd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3319, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ospfd.setStatus("current")
_Ospf6d_ObjectIdentity = ObjectIdentity
ospf6d = _Ospf6d_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3319, 1, 2, 6)
)
if mibBuilder.loadTexts:
    ospf6d.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GNOME-PRODUCT-ZEBRA-MIB",
    **{"zebra": zebra,
       "zserv": zserv,
       "bgpd": bgpd,
       "ripd": ripd,
       "ripngd": ripngd,
       "ospfd": ospfd,
       "ospf6d": ospf6d}
)
