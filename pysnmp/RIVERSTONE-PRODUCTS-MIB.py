# SNMP MIB module (RIVERSTONE-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RIVERSTONE-PRODUCTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:49 2024
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

(riverstoneProducts,) = mibBuilder.importSymbols(
    "RSTONE-SMI-MIB",
    "riverstoneProducts")

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

rsFamilyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 1, 1)
)
rsFamilyMIB.setRevisions(
        ("2000-04-16 00:00",
         "2000-11-28 00:00",
         "2000-11-29 00:00",
         "2000-11-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rs8000_ObjectIdentity = ObjectIdentity
rs8000 = _Rs8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rs8000.setStatus("current")
_Rs8600_ObjectIdentity = ObjectIdentity
rs8600 = _Rs8600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rs8600.setStatus("current")
_Rs2000_ObjectIdentity = ObjectIdentity
rs2000 = _Rs2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 1, 1, 3)
)
if mibBuilder.loadTexts:
    rs2000.setStatus("current")
_Rs2100_ObjectIdentity = ObjectIdentity
rs2100 = _Rs2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 1, 1, 4)
)
if mibBuilder.loadTexts:
    rs2100.setStatus("current")
_Rs3000_ObjectIdentity = ObjectIdentity
rs3000 = _Rs3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 1, 1, 5)
)
if mibBuilder.loadTexts:
    rs3000.setStatus("current")
_Rs32000_ObjectIdentity = ObjectIdentity
rs32000 = _Rs32000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 1, 1, 6)
)
if mibBuilder.loadTexts:
    rs32000.setStatus("current")
_Rs1000_ObjectIdentity = ObjectIdentity
rs1000 = _Rs1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 1, 1, 8)
)
if mibBuilder.loadTexts:
    rs1000.setStatus("current")
_Rs38000_ObjectIdentity = ObjectIdentity
rs38000 = _Rs38000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 1, 1, 9)
)
if mibBuilder.loadTexts:
    rs38000.setStatus("current")
_RsIA1100_ObjectIdentity = ObjectIdentity
rsIA1100 = _RsIA1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 1, 1, 22)
)
if mibBuilder.loadTexts:
    rsIA1100.setStatus("current")
_RsIA1200_ObjectIdentity = ObjectIdentity
rsIA1200 = _RsIA1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 1, 1, 23)
)
if mibBuilder.loadTexts:
    rsIA1200.setStatus("current")
_RsIA1500_ObjectIdentity = ObjectIdentity
rsIA1500 = _RsIA1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 1, 1, 27)
)
if mibBuilder.loadTexts:
    rsIA1500.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RIVERSTONE-PRODUCTS-MIB",
    **{"rsFamilyMIB": rsFamilyMIB,
       "rs8000": rs8000,
       "rs8600": rs8600,
       "rs2000": rs2000,
       "rs2100": rs2100,
       "rs3000": rs3000,
       "rs32000": rs32000,
       "rs1000": rs1000,
       "rs38000": rs38000,
       "rsIA1100": rsIA1100,
       "rsIA1200": rsIA1200,
       "rsIA1500": rsIA1500}
)
