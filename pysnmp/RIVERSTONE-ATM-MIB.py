# SNMP MIB module (RIVERSTONE-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RIVERSTONE-ATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:41 2024
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

(AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

(dot1dTpFdbAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dTpFdbAddress")

(riverstoneMibs,) = mibBuilder.importSymbols(
    "RSTONE-SMI-MIB",
    "riverstoneMibs")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

rsAtmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 16)
)
rsAtmMib.setRevisions(
        ("2001-01-31 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsAtmFdbObjects_ObjectIdentity = ObjectIdentity
rsAtmFdbObjects = _RsAtmFdbObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 16, 1)
)
_RsAtmFdbMacsLearned_Type = Gauge32
_RsAtmFdbMacsLearned_Object = MibScalar
rsAtmFdbMacsLearned = _RsAtmFdbMacsLearned_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 16, 1, 1),
    _RsAtmFdbMacsLearned_Type()
)
rsAtmFdbMacsLearned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAtmFdbMacsLearned.setStatus("current")
_RsAtmFdbTable_Object = MibTable
rsAtmFdbTable = _RsAtmFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 16, 1, 2)
)
if mibBuilder.loadTexts:
    rsAtmFdbTable.setStatus("current")
_RsAtmFdbEntry_Object = MibTableRow
rsAtmFdbEntry = _RsAtmFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 16, 1, 2, 1)
)
rsAtmFdbEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dTpFdbAddress"),
)
if mibBuilder.loadTexts:
    rsAtmFdbEntry.setStatus("current")
_RsAtmFdbVpi_Type = AtmVpIdentifier
_RsAtmFdbVpi_Object = MibTableColumn
rsAtmFdbVpi = _RsAtmFdbVpi_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 16, 1, 2, 1, 1),
    _RsAtmFdbVpi_Type()
)
rsAtmFdbVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAtmFdbVpi.setStatus("current")
_RsAtmFdbVci_Type = AtmVcIdentifier
_RsAtmFdbVci_Object = MibTableColumn
rsAtmFdbVci = _RsAtmFdbVci_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 16, 1, 2, 1, 2),
    _RsAtmFdbVci_Type()
)
rsAtmFdbVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAtmFdbVci.setStatus("current")
_RsAtmFdbConformance_ObjectIdentity = ObjectIdentity
rsAtmFdbConformance = _RsAtmFdbConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 16, 10)
)
_RsAtmFdbGroups_ObjectIdentity = ObjectIdentity
rsAtmFdbGroups = _RsAtmFdbGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 16, 10, 1)
)
_RsAtmFdbCompliances_ObjectIdentity = ObjectIdentity
rsAtmFdbCompliances = _RsAtmFdbCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 16, 10, 2)
)

# Managed Objects groups

rsAtmFdbBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 16, 10, 1, 1)
)
rsAtmFdbBaseGroup.setObjects(
      *(("RIVERSTONE-ATM-MIB", "rsAtmFdbMacsLearned"),
        ("RIVERSTONE-ATM-MIB", "rsAtmFdbVpi"),
        ("RIVERSTONE-ATM-MIB", "rsAtmFdbVci"))
)
if mibBuilder.loadTexts:
    rsAtmFdbBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsAtmFdbMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5567, 2, 16, 10, 2, 1)
)
if mibBuilder.loadTexts:
    rsAtmFdbMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RIVERSTONE-ATM-MIB",
    **{"rsAtmMib": rsAtmMib,
       "rsAtmFdbObjects": rsAtmFdbObjects,
       "rsAtmFdbMacsLearned": rsAtmFdbMacsLearned,
       "rsAtmFdbTable": rsAtmFdbTable,
       "rsAtmFdbEntry": rsAtmFdbEntry,
       "rsAtmFdbVpi": rsAtmFdbVpi,
       "rsAtmFdbVci": rsAtmFdbVci,
       "rsAtmFdbConformance": rsAtmFdbConformance,
       "rsAtmFdbGroups": rsAtmFdbGroups,
       "rsAtmFdbBaseGroup": rsAtmFdbBaseGroup,
       "rsAtmFdbCompliances": rsAtmFdbCompliances,
       "rsAtmFdbMibCompliance": rsAtmFdbMibCompliance}
)
