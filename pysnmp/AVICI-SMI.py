# SNMP MIB module (AVICI-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AVICI-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:40 2024
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

avici = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2474)
)
avici.setRevisions(
        ("1970-01-01 00:00",
         "1970-01-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AviciMibs_ObjectIdentity = ObjectIdentity
aviciMibs = _AviciMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1)
)
if mibBuilder.loadTexts:
    aviciMibs.setStatus("current")
_AviciProducts_ObjectIdentity = ObjectIdentity
aviciProducts = _AviciProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 2)
)
if mibBuilder.loadTexts:
    aviciProducts.setStatus("current")
_AviciExperimental_ObjectIdentity = ObjectIdentity
aviciExperimental = _AviciExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 3)
)
if mibBuilder.loadTexts:
    aviciExperimental.setStatus("current")
_AviciTypes_ObjectIdentity = ObjectIdentity
aviciTypes = _AviciTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 4)
)
if mibBuilder.loadTexts:
    aviciTypes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVICI-SMI",
    **{"avici": avici,
       "aviciMibs": aviciMibs,
       "aviciProducts": aviciProducts,
       "aviciExperimental": aviciExperimental,
       "aviciTypes": aviciTypes}
)
