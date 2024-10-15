# SNMP MIB module (PCUBE-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PCUBE-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:57 2024
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

pcube = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5655)
)
pcube.setRevisions(
        ("2002-01-14 20:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PcubeProducts_ObjectIdentity = ObjectIdentity
pcubeProducts = _PcubeProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 1)
)
if mibBuilder.loadTexts:
    pcubeProducts.setStatus("current")
_PcubeModules_ObjectIdentity = ObjectIdentity
pcubeModules = _PcubeModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 2)
)
if mibBuilder.loadTexts:
    pcubeModules.setStatus("current")
_PcubeMgmt_ObjectIdentity = ObjectIdentity
pcubeMgmt = _PcubeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 3)
)
if mibBuilder.loadTexts:
    pcubeMgmt.setStatus("current")
_PcubeWorkgroup_ObjectIdentity = ObjectIdentity
pcubeWorkgroup = _PcubeWorkgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4)
)
if mibBuilder.loadTexts:
    pcubeWorkgroup.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PCUBE-SMI",
    **{"pcube": pcube,
       "pcubeProducts": pcubeProducts,
       "pcubeModules": pcubeModules,
       "pcubeMgmt": pcubeMgmt,
       "pcubeWorkgroup": pcubeWorkgroup}
)
