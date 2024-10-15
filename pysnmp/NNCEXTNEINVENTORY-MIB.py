# SNMP MIB module (NNCEXTNEINVENTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNCEXTNEINVENTORY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:19 2024
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

(entPhysicalEntry,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalEntry",
    "entPhysicalIndex")

(nncExtensions,) = mibBuilder.importSymbols(
    "NNCGNI0001-SMI",
    "nncExtensions")

(NncSwBank,
 NncSwStatus) = mibBuilder.importSymbols(
    "NNCGNI0006-MIB",
    "NncSwBank",
    "NncSwStatus")

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

nncExtNEInventory = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 69)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NncExtNEInventoryObjects_ObjectIdentity = ObjectIdentity
nncExtNEInventoryObjects = _NncExtNEInventoryObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 69, 1)
)
_NncNEInventoryTable_Object = MibTable
nncNEInventoryTable = _NncNEInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 69, 1, 1)
)
if mibBuilder.loadTexts:
    nncNEInventoryTable.setStatus("current")
_NncNEInventoryTableEntry_Object = MibTableRow
nncNEInventoryTableEntry = _NncNEInventoryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 69, 1, 1, 1)
)
if mibBuilder.loadTexts:
    nncNEInventoryTableEntry.setStatus("current")
_NncNEInvAssemblyName_Type = DisplayString
_NncNEInvAssemblyName_Object = MibTableColumn
nncNEInvAssemblyName = _NncNEInvAssemblyName_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 69, 1, 1, 1, 1),
    _NncNEInvAssemblyName_Type()
)
nncNEInvAssemblyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNEInvAssemblyName.setStatus("current")


class _NncNEInvSerialNumber_Type(DisplayString):
    """Custom type nncNEInvSerialNumber based on DisplayString"""
    defaultHexValue = ""


_NncNEInvSerialNumber_Object = MibTableColumn
nncNEInvSerialNumber = _NncNEInvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 69, 1, 1, 1, 2),
    _NncNEInvSerialNumber_Type()
)
nncNEInvSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNEInvSerialNumber.setStatus("current")


class _NncNEInvAssemblyIdentity_Type(DisplayString):
    """Custom type nncNEInvAssemblyIdentity based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_NncNEInvAssemblyIdentity_Type.__name__ = "DisplayString"
_NncNEInvAssemblyIdentity_Object = MibTableColumn
nncNEInvAssemblyIdentity = _NncNEInvAssemblyIdentity_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 69, 1, 1, 1, 3),
    _NncNEInvAssemblyIdentity_Type()
)
nncNEInvAssemblyIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNEInvAssemblyIdentity.setStatus("current")


class _NncNEInvMktgPartNo_Type(DisplayString):
    """Custom type nncNEInvMktgPartNo based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_NncNEInvMktgPartNo_Type.__name__ = "DisplayString"
_NncNEInvMktgPartNo_Object = MibTableColumn
nncNEInvMktgPartNo = _NncNEInvMktgPartNo_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 69, 1, 1, 1, 4),
    _NncNEInvMktgPartNo_Type()
)
nncNEInvMktgPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNEInvMktgPartNo.setStatus("current")


class _NncNEInvEnggPartNo_Type(DisplayString):
    """Custom type nncNEInvEnggPartNo based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_NncNEInvEnggPartNo_Type.__name__ = "DisplayString"
_NncNEInvEnggPartNo_Object = MibTableColumn
nncNEInvEnggPartNo = _NncNEInvEnggPartNo_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 69, 1, 1, 1, 5),
    _NncNEInvEnggPartNo_Type()
)
nncNEInvEnggPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNEInvEnggPartNo.setStatus("current")


class _NncNEInvRestartCause_Type(DisplayString):
    """Custom type nncNEInvRestartCause based on DisplayString"""
    defaultHexValue = ""


_NncNEInvRestartCause_Object = MibTableColumn
nncNEInvRestartCause = _NncNEInvRestartCause_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 69, 1, 1, 1, 6),
    _NncNEInvRestartCause_Type()
)
nncNEInvRestartCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNEInvRestartCause.setStatus("current")


class _NncNEInvAssemblyNoOfSwBanks_Type(Integer32):
    """Custom type nncNEInvAssemblyNoOfSwBanks based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_NncNEInvAssemblyNoOfSwBanks_Type.__name__ = "Integer32"
_NncNEInvAssemblyNoOfSwBanks_Object = MibTableColumn
nncNEInvAssemblyNoOfSwBanks = _NncNEInvAssemblyNoOfSwBanks_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 69, 1, 1, 1, 7),
    _NncNEInvAssemblyNoOfSwBanks_Type()
)
nncNEInvAssemblyNoOfSwBanks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNEInvAssemblyNoOfSwBanks.setStatus("current")


class _NncNEInvAssemblyActiveSwBank_Type(NncSwBank):
    """Custom type nncNEInvAssemblyActiveSwBank based on NncSwBank"""
    defaultValue = 0


_NncNEInvAssemblyActiveSwBank_Object = MibTableColumn
nncNEInvAssemblyActiveSwBank = _NncNEInvAssemblyActiveSwBank_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 69, 1, 1, 1, 8),
    _NncNEInvAssemblyActiveSwBank_Type()
)
nncNEInvAssemblyActiveSwBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNEInvAssemblyActiveSwBank.setStatus("current")


class _NncNEInvAssemblyNextActiveSwBank_Type(NncSwBank):
    """Custom type nncNEInvAssemblyNextActiveSwBank based on NncSwBank"""
    defaultValue = 0


_NncNEInvAssemblyNextActiveSwBank_Object = MibTableColumn
nncNEInvAssemblyNextActiveSwBank = _NncNEInvAssemblyNextActiveSwBank_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 69, 1, 1, 1, 9),
    _NncNEInvAssemblyNextActiveSwBank_Type()
)
nncNEInvAssemblyNextActiveSwBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNEInvAssemblyNextActiveSwBank.setStatus("current")
_NncAssemblySwBanksTable_Object = MibTable
nncAssemblySwBanksTable = _NncAssemblySwBanksTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 69, 1, 2)
)
if mibBuilder.loadTexts:
    nncAssemblySwBanksTable.setStatus("current")
_NncAssemblySwBanksTableEntry_Object = MibTableRow
nncAssemblySwBanksTableEntry = _NncAssemblySwBanksTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 69, 1, 2, 1)
)
nncAssemblySwBanksTableEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "NNCEXTNEINVENTORY-MIB", "nncAssemblySwBankNumber"),
)
if mibBuilder.loadTexts:
    nncAssemblySwBanksTableEntry.setStatus("current")


class _NncAssemblySwBankNumber_Type(Integer32):
    """Custom type nncAssemblySwBankNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_NncAssemblySwBankNumber_Type.__name__ = "Integer32"
_NncAssemblySwBankNumber_Object = MibTableColumn
nncAssemblySwBankNumber = _NncAssemblySwBankNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 69, 1, 2, 1, 1),
    _NncAssemblySwBankNumber_Type()
)
nncAssemblySwBankNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAssemblySwBankNumber.setStatus("current")


class _NncAssemblySwBankGeneric_Type(DisplayString):
    """Custom type nncAssemblySwBankGeneric based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_NncAssemblySwBankGeneric_Type.__name__ = "DisplayString"
_NncAssemblySwBankGeneric_Object = MibTableColumn
nncAssemblySwBankGeneric = _NncAssemblySwBankGeneric_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 69, 1, 2, 1, 2),
    _NncAssemblySwBankGeneric_Type()
)
nncAssemblySwBankGeneric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAssemblySwBankGeneric.setStatus("current")
_NncAssemblySwBankStatus_Type = NncSwStatus
_NncAssemblySwBankStatus_Object = MibTableColumn
nncAssemblySwBankStatus = _NncAssemblySwBankStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 69, 1, 2, 1, 3),
    _NncAssemblySwBankStatus_Type()
)
nncAssemblySwBankStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAssemblySwBankStatus.setStatus("current")
_NncExtNEInventoryGroups_ObjectIdentity = ObjectIdentity
nncExtNEInventoryGroups = _NncExtNEInventoryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 69, 2)
)
_NncExtNEInventoryCompliances_ObjectIdentity = ObjectIdentity
nncExtNEInventoryCompliances = _NncExtNEInventoryCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 69, 3)
)
entPhysicalEntry.registerAugmentions(
    ("NNCEXTNEINVENTORY-MIB",
     "nncNEInventoryTableEntry")
)
nncNEInventoryTableEntry.setIndexNames(*entPhysicalEntry.getIndexNames())

# Managed Objects groups

nncNEPhysInventoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 69, 2, 1)
)
nncNEPhysInventoryGroup.setObjects(
      *(("NNCEXTNEINVENTORY-MIB", "nncNEInvAssemblyName"),
        ("NNCEXTNEINVENTORY-MIB", "nncNEInvSerialNumber"),
        ("NNCEXTNEINVENTORY-MIB", "nncNEInvAssemblyIdentity"),
        ("NNCEXTNEINVENTORY-MIB", "nncNEInvMktgPartNo"),
        ("NNCEXTNEINVENTORY-MIB", "nncNEInvEnggPartNo"),
        ("NNCEXTNEINVENTORY-MIB", "nncNEInvRestartCause"),
        ("NNCEXTNEINVENTORY-MIB", "nncNEInvAssemblyNoOfSwBanks"),
        ("NNCEXTNEINVENTORY-MIB", "nncNEInvAssemblyActiveSwBank"),
        ("NNCEXTNEINVENTORY-MIB", "nncNEInvAssemblyNextActiveSwBank"))
)
if mibBuilder.loadTexts:
    nncNEPhysInventoryGroup.setStatus("current")

nncNEPhysAssemblySwBankGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 69, 2, 2)
)
nncNEPhysAssemblySwBankGroup.setObjects(
      *(("NNCEXTNEINVENTORY-MIB", "nncAssemblySwBankNumber"),
        ("NNCEXTNEINVENTORY-MIB", "nncAssemblySwBankGeneric"),
        ("NNCEXTNEINVENTORY-MIB", "nncAssemblySwBankStatus"))
)
if mibBuilder.loadTexts:
    nncNEPhysAssemblySwBankGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nncNEInvCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 123, 3, 69, 3, 1)
)
if mibBuilder.loadTexts:
    nncNEInvCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNCEXTNEINVENTORY-MIB",
    **{"nncExtNEInventory": nncExtNEInventory,
       "nncExtNEInventoryObjects": nncExtNEInventoryObjects,
       "nncNEInventoryTable": nncNEInventoryTable,
       "nncNEInventoryTableEntry": nncNEInventoryTableEntry,
       "nncNEInvAssemblyName": nncNEInvAssemblyName,
       "nncNEInvSerialNumber": nncNEInvSerialNumber,
       "nncNEInvAssemblyIdentity": nncNEInvAssemblyIdentity,
       "nncNEInvMktgPartNo": nncNEInvMktgPartNo,
       "nncNEInvEnggPartNo": nncNEInvEnggPartNo,
       "nncNEInvRestartCause": nncNEInvRestartCause,
       "nncNEInvAssemblyNoOfSwBanks": nncNEInvAssemblyNoOfSwBanks,
       "nncNEInvAssemblyActiveSwBank": nncNEInvAssemblyActiveSwBank,
       "nncNEInvAssemblyNextActiveSwBank": nncNEInvAssemblyNextActiveSwBank,
       "nncAssemblySwBanksTable": nncAssemblySwBanksTable,
       "nncAssemblySwBanksTableEntry": nncAssemblySwBanksTableEntry,
       "nncAssemblySwBankNumber": nncAssemblySwBankNumber,
       "nncAssemblySwBankGeneric": nncAssemblySwBankGeneric,
       "nncAssemblySwBankStatus": nncAssemblySwBankStatus,
       "nncExtNEInventoryGroups": nncExtNEInventoryGroups,
       "nncNEPhysInventoryGroup": nncNEPhysInventoryGroup,
       "nncNEPhysAssemblySwBankGroup": nncNEPhysAssemblySwBankGroup,
       "nncExtNEInventoryCompliances": nncExtNEInventoryCompliances,
       "nncNEInvCompliance": nncNEInvCompliance}
)
