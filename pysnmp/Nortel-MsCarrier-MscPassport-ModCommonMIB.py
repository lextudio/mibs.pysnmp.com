# SNMP MIB module (Nortel-MsCarrier-MscPassport-ModCommonMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-ModCommonMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:49 2024
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

(mscMod,
 mscModIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-BaseShelfMIB",
    "mscMod",
    "mscModIndex")

(DisplayString,
 RowStatus,
 StorageType) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DisplayString",
    "RowStatus",
    "StorageType")

(NonReplicated,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "NonReplicated")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscPassportMIBs")

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

_MscModFrs_ObjectIdentity = ObjectIdentity
mscModFrs = _MscModFrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3)
)
_MscModFrsRowStatusTable_Object = MibTable
mscModFrsRowStatusTable = _MscModFrsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 1)
)
if mibBuilder.loadTexts:
    mscModFrsRowStatusTable.setStatus("mandatory")
_MscModFrsRowStatusEntry_Object = MibTableRow
mscModFrsRowStatusEntry = _MscModFrsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 1, 1)
)
mscModFrsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscModIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ModCommonMIB", "mscModFrsIndex"),
)
if mibBuilder.loadTexts:
    mscModFrsRowStatusEntry.setStatus("mandatory")
_MscModFrsRowStatus_Type = RowStatus
_MscModFrsRowStatus_Object = MibTableColumn
mscModFrsRowStatus = _MscModFrsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 1, 1, 1),
    _MscModFrsRowStatus_Type()
)
mscModFrsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscModFrsRowStatus.setStatus("mandatory")
_MscModFrsComponentName_Type = DisplayString
_MscModFrsComponentName_Object = MibTableColumn
mscModFrsComponentName = _MscModFrsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 1, 1, 2),
    _MscModFrsComponentName_Type()
)
mscModFrsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscModFrsComponentName.setStatus("mandatory")
_MscModFrsStorageType_Type = StorageType
_MscModFrsStorageType_Object = MibTableColumn
mscModFrsStorageType = _MscModFrsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 1, 1, 4),
    _MscModFrsStorageType_Type()
)
mscModFrsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscModFrsStorageType.setStatus("mandatory")
_MscModFrsIndex_Type = NonReplicated
_MscModFrsIndex_Object = MibTableColumn
mscModFrsIndex = _MscModFrsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 1, 1, 10),
    _MscModFrsIndex_Type()
)
mscModFrsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscModFrsIndex.setStatus("mandatory")
_ModCommonMIB_ObjectIdentity = ObjectIdentity
modCommonMIB = _ModCommonMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 74)
)
_ModCommonGroup_ObjectIdentity = ObjectIdentity
modCommonGroup = _ModCommonGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 74, 1)
)
_ModCommonGroupCA_ObjectIdentity = ObjectIdentity
modCommonGroupCA = _ModCommonGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 74, 1, 1)
)
_ModCommonGroupCA02_ObjectIdentity = ObjectIdentity
modCommonGroupCA02 = _ModCommonGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 74, 1, 1, 3)
)
_ModCommonGroupCA02A_ObjectIdentity = ObjectIdentity
modCommonGroupCA02A = _ModCommonGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 74, 1, 1, 3, 2)
)
_ModCommonCapabilities_ObjectIdentity = ObjectIdentity
modCommonCapabilities = _ModCommonCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 74, 3)
)
_ModCommonCapabilitiesCA_ObjectIdentity = ObjectIdentity
modCommonCapabilitiesCA = _ModCommonCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 74, 3, 1)
)
_ModCommonCapabilitiesCA02_ObjectIdentity = ObjectIdentity
modCommonCapabilitiesCA02 = _ModCommonCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 74, 3, 1, 3)
)
_ModCommonCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
modCommonCapabilitiesCA02A = _ModCommonCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 74, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-ModCommonMIB",
    **{"mscModFrs": mscModFrs,
       "mscModFrsRowStatusTable": mscModFrsRowStatusTable,
       "mscModFrsRowStatusEntry": mscModFrsRowStatusEntry,
       "mscModFrsRowStatus": mscModFrsRowStatus,
       "mscModFrsComponentName": mscModFrsComponentName,
       "mscModFrsStorageType": mscModFrsStorageType,
       "mscModFrsIndex": mscModFrsIndex,
       "modCommonMIB": modCommonMIB,
       "modCommonGroup": modCommonGroup,
       "modCommonGroupCA": modCommonGroupCA,
       "modCommonGroupCA02": modCommonGroupCA02,
       "modCommonGroupCA02A": modCommonGroupCA02A,
       "modCommonCapabilities": modCommonCapabilities,
       "modCommonCapabilitiesCA": modCommonCapabilitiesCA,
       "modCommonCapabilitiesCA02": modCommonCapabilitiesCA02,
       "modCommonCapabilitiesCA02A": modCommonCapabilitiesCA02A}
)
