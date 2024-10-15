# SNMP MIB module (Nortel-Magellan-Passport-ModCommonMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-ModCommonMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:10 2024
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

(mod,
 modIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-ShelfMIB",
    "mod",
    "modIndex")

(DisplayString,
 RowStatus,
 StorageType) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "RowStatus",
    "StorageType")

(NonReplicated,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "NonReplicated")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "passportMIBs")

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

_ModFrs_ObjectIdentity = ObjectIdentity
modFrs = _ModFrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3)
)
_ModFrsRowStatusTable_Object = MibTable
modFrsRowStatusTable = _ModFrsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 1)
)
if mibBuilder.loadTexts:
    modFrsRowStatusTable.setStatus("mandatory")
_ModFrsRowStatusEntry_Object = MibTableRow
modFrsRowStatusEntry = _ModFrsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 1, 1)
)
modFrsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "modIndex"),
    (0, "Nortel-Magellan-Passport-ModCommonMIB", "modFrsIndex"),
)
if mibBuilder.loadTexts:
    modFrsRowStatusEntry.setStatus("mandatory")
_ModFrsRowStatus_Type = RowStatus
_ModFrsRowStatus_Object = MibTableColumn
modFrsRowStatus = _ModFrsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 1, 1, 1),
    _ModFrsRowStatus_Type()
)
modFrsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modFrsRowStatus.setStatus("mandatory")
_ModFrsComponentName_Type = DisplayString
_ModFrsComponentName_Object = MibTableColumn
modFrsComponentName = _ModFrsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 1, 1, 2),
    _ModFrsComponentName_Type()
)
modFrsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modFrsComponentName.setStatus("mandatory")
_ModFrsStorageType_Type = StorageType
_ModFrsStorageType_Object = MibTableColumn
modFrsStorageType = _ModFrsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 1, 1, 4),
    _ModFrsStorageType_Type()
)
modFrsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modFrsStorageType.setStatus("mandatory")
_ModFrsIndex_Type = NonReplicated
_ModFrsIndex_Object = MibTableColumn
modFrsIndex = _ModFrsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 1, 1, 10),
    _ModFrsIndex_Type()
)
modFrsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modFrsIndex.setStatus("mandatory")
_ModCommonMIB_ObjectIdentity = ObjectIdentity
modCommonMIB = _ModCommonMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 74)
)
_ModCommonGroup_ObjectIdentity = ObjectIdentity
modCommonGroup = _ModCommonGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 74, 1)
)
_ModCommonGroupBE_ObjectIdentity = ObjectIdentity
modCommonGroupBE = _ModCommonGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 74, 1, 5)
)
_ModCommonGroupBE01_ObjectIdentity = ObjectIdentity
modCommonGroupBE01 = _ModCommonGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 74, 1, 5, 2)
)
_ModCommonGroupBE01A_ObjectIdentity = ObjectIdentity
modCommonGroupBE01A = _ModCommonGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 74, 1, 5, 2, 2)
)
_ModCommonCapabilities_ObjectIdentity = ObjectIdentity
modCommonCapabilities = _ModCommonCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 74, 3)
)
_ModCommonCapabilitiesBE_ObjectIdentity = ObjectIdentity
modCommonCapabilitiesBE = _ModCommonCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 74, 3, 5)
)
_ModCommonCapabilitiesBE01_ObjectIdentity = ObjectIdentity
modCommonCapabilitiesBE01 = _ModCommonCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 74, 3, 5, 2)
)
_ModCommonCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
modCommonCapabilitiesBE01A = _ModCommonCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 74, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-ModCommonMIB",
    **{"modFrs": modFrs,
       "modFrsRowStatusTable": modFrsRowStatusTable,
       "modFrsRowStatusEntry": modFrsRowStatusEntry,
       "modFrsRowStatus": modFrsRowStatus,
       "modFrsComponentName": modFrsComponentName,
       "modFrsStorageType": modFrsStorageType,
       "modFrsIndex": modFrsIndex,
       "modCommonMIB": modCommonMIB,
       "modCommonGroup": modCommonGroup,
       "modCommonGroupBE": modCommonGroupBE,
       "modCommonGroupBE01": modCommonGroupBE01,
       "modCommonGroupBE01A": modCommonGroupBE01A,
       "modCommonCapabilities": modCommonCapabilities,
       "modCommonCapabilitiesBE": modCommonCapabilitiesBE,
       "modCommonCapabilitiesBE01": modCommonCapabilitiesBE01,
       "modCommonCapabilitiesBE01A": modCommonCapabilitiesBE01A}
)
