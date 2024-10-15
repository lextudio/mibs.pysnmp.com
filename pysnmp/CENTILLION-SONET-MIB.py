# SNMP MIB module (CENTILLION-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CENTILLION-SONET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:13 2024
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

(atmSonet,) = mibBuilder.importSymbols(
    "CENTILLION-ROOT-MIB",
    "atmSonet")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmSonetConfig_ObjectIdentity = ObjectIdentity
atmSonetConfig = _AtmSonetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 4, 1)
)
_CnSonetSectionTable_Object = MibTable
cnSonetSectionTable = _CnSonetSectionTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cnSonetSectionTable.setStatus("mandatory")
_CnSonetSectionEntry_Object = MibTableRow
cnSonetSectionEntry = _CnSonetSectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 4, 1, 1, 1)
)
cnSonetSectionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cnSonetSectionEntry.setStatus("mandatory")
_CnSonetSectionBip8Errors_Type = Counter32
_CnSonetSectionBip8Errors_Object = MibTableColumn
cnSonetSectionBip8Errors = _CnSonetSectionBip8Errors_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 4, 1, 1, 1, 1),
    _CnSonetSectionBip8Errors_Type()
)
cnSonetSectionBip8Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnSonetSectionBip8Errors.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTILLION-SONET-MIB",
    **{"atmSonetConfig": atmSonetConfig,
       "cnSonetSectionTable": cnSonetSectionTable,
       "cnSonetSectionEntry": cnSonetSectionEntry,
       "cnSonetSectionBip8Errors": cnSonetSectionBip8Errors}
)
