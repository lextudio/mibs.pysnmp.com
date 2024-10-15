# SNMP MIB module (GNOME-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GNOME-SMI
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

gnome = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3319)
)
gnome.setRevisions(
        ("2007-09-07 00:00",
         "2005-05-07 00:00",
         "2003-12-07 00:00",
         "1998-09-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GnomeProducts_ObjectIdentity = ObjectIdentity
gnomeProducts = _GnomeProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3319, 1)
)
if mibBuilder.loadTexts:
    gnomeProducts.setStatus("current")
_GnomeMgmt_ObjectIdentity = ObjectIdentity
gnomeMgmt = _GnomeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3319, 2)
)
if mibBuilder.loadTexts:
    gnomeMgmt.setStatus("current")
_GnomeTest_ObjectIdentity = ObjectIdentity
gnomeTest = _GnomeTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3319, 3)
)
if mibBuilder.loadTexts:
    gnomeTest.setStatus("current")
_GnomeSysadmin_ObjectIdentity = ObjectIdentity
gnomeSysadmin = _GnomeSysadmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3319, 4)
)
if mibBuilder.loadTexts:
    gnomeSysadmin.setStatus("current")
_GnomeLDAP_ObjectIdentity = ObjectIdentity
gnomeLDAP = _GnomeLDAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3319, 5)
)
if mibBuilder.loadTexts:
    gnomeLDAP.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GNOME-SMI",
    **{"gnome": gnome,
       "gnomeProducts": gnomeProducts,
       "gnomeMgmt": gnomeMgmt,
       "gnomeTest": gnomeTest,
       "gnomeSysadmin": gnomeSysadmin,
       "gnomeLDAP": gnomeLDAP}
)
