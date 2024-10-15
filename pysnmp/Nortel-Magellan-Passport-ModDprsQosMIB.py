# SNMP MIB module (Nortel-Magellan-Passport-ModDprsQosMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-ModDprsQosMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:12 2024
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

(modFrs,
 modFrsIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-ModCommonMIB",
    "modFrs",
    "modFrsIndex")

(modIndex,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-ShelfMIB",
    "modIndex")

(DisplayString,
 Integer32,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

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

_ModFrsDprsNet_ObjectIdentity = ObjectIdentity
modFrsDprsNet = _ModFrsDprsNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 3)
)
_ModFrsDprsNetRowStatusTable_Object = MibTable
modFrsDprsNetRowStatusTable = _ModFrsDprsNetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 3, 1)
)
if mibBuilder.loadTexts:
    modFrsDprsNetRowStatusTable.setStatus("mandatory")
_ModFrsDprsNetRowStatusEntry_Object = MibTableRow
modFrsDprsNetRowStatusEntry = _ModFrsDprsNetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 3, 1, 1)
)
modFrsDprsNetRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "modIndex"),
    (0, "Nortel-Magellan-Passport-ModCommonMIB", "modFrsIndex"),
    (0, "Nortel-Magellan-Passport-ModDprsQosMIB", "modFrsDprsNetIndex"),
)
if mibBuilder.loadTexts:
    modFrsDprsNetRowStatusEntry.setStatus("mandatory")
_ModFrsDprsNetRowStatus_Type = RowStatus
_ModFrsDprsNetRowStatus_Object = MibTableColumn
modFrsDprsNetRowStatus = _ModFrsDprsNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 3, 1, 1, 1),
    _ModFrsDprsNetRowStatus_Type()
)
modFrsDprsNetRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modFrsDprsNetRowStatus.setStatus("mandatory")
_ModFrsDprsNetComponentName_Type = DisplayString
_ModFrsDprsNetComponentName_Object = MibTableColumn
modFrsDprsNetComponentName = _ModFrsDprsNetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 3, 1, 1, 2),
    _ModFrsDprsNetComponentName_Type()
)
modFrsDprsNetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modFrsDprsNetComponentName.setStatus("mandatory")
_ModFrsDprsNetStorageType_Type = StorageType
_ModFrsDprsNetStorageType_Object = MibTableColumn
modFrsDprsNetStorageType = _ModFrsDprsNetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 3, 1, 1, 4),
    _ModFrsDprsNetStorageType_Type()
)
modFrsDprsNetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modFrsDprsNetStorageType.setStatus("mandatory")
_ModFrsDprsNetIndex_Type = NonReplicated
_ModFrsDprsNetIndex_Object = MibTableColumn
modFrsDprsNetIndex = _ModFrsDprsNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 3, 1, 1, 10),
    _ModFrsDprsNetIndex_Type()
)
modFrsDprsNetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modFrsDprsNetIndex.setStatus("mandatory")
_ModFrsDprsNetTpm_ObjectIdentity = ObjectIdentity
modFrsDprsNetTpm = _ModFrsDprsNetTpm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 3, 2)
)
_ModFrsDprsNetTpmRowStatusTable_Object = MibTable
modFrsDprsNetTpmRowStatusTable = _ModFrsDprsNetTpmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    modFrsDprsNetTpmRowStatusTable.setStatus("mandatory")
_ModFrsDprsNetTpmRowStatusEntry_Object = MibTableRow
modFrsDprsNetTpmRowStatusEntry = _ModFrsDprsNetTpmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 3, 2, 1, 1)
)
modFrsDprsNetTpmRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "modIndex"),
    (0, "Nortel-Magellan-Passport-ModCommonMIB", "modFrsIndex"),
    (0, "Nortel-Magellan-Passport-ModDprsQosMIB", "modFrsDprsNetIndex"),
    (0, "Nortel-Magellan-Passport-ModDprsQosMIB", "modFrsDprsNetTpmIndex"),
)
if mibBuilder.loadTexts:
    modFrsDprsNetTpmRowStatusEntry.setStatus("mandatory")
_ModFrsDprsNetTpmRowStatus_Type = RowStatus
_ModFrsDprsNetTpmRowStatus_Object = MibTableColumn
modFrsDprsNetTpmRowStatus = _ModFrsDprsNetTpmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 3, 2, 1, 1, 1),
    _ModFrsDprsNetTpmRowStatus_Type()
)
modFrsDprsNetTpmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modFrsDprsNetTpmRowStatus.setStatus("mandatory")
_ModFrsDprsNetTpmComponentName_Type = DisplayString
_ModFrsDprsNetTpmComponentName_Object = MibTableColumn
modFrsDprsNetTpmComponentName = _ModFrsDprsNetTpmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 3, 2, 1, 1, 2),
    _ModFrsDprsNetTpmComponentName_Type()
)
modFrsDprsNetTpmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modFrsDprsNetTpmComponentName.setStatus("mandatory")
_ModFrsDprsNetTpmStorageType_Type = StorageType
_ModFrsDprsNetTpmStorageType_Object = MibTableColumn
modFrsDprsNetTpmStorageType = _ModFrsDprsNetTpmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 3, 2, 1, 1, 4),
    _ModFrsDprsNetTpmStorageType_Type()
)
modFrsDprsNetTpmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modFrsDprsNetTpmStorageType.setStatus("mandatory")


class _ModFrsDprsNetTpmIndex_Type(Integer32):
    """Custom type modFrsDprsNetTpmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ModFrsDprsNetTpmIndex_Type.__name__ = "Integer32"
_ModFrsDprsNetTpmIndex_Object = MibTableColumn
modFrsDprsNetTpmIndex = _ModFrsDprsNetTpmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 3, 2, 1, 1, 10),
    _ModFrsDprsNetTpmIndex_Type()
)
modFrsDprsNetTpmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modFrsDprsNetTpmIndex.setStatus("mandatory")
_ModFrsDprsNetTpmProvTable_Object = MibTable
modFrsDprsNetTpmProvTable = _ModFrsDprsNetTpmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 3, 2, 10)
)
if mibBuilder.loadTexts:
    modFrsDprsNetTpmProvTable.setStatus("mandatory")
_ModFrsDprsNetTpmProvEntry_Object = MibTableRow
modFrsDprsNetTpmProvEntry = _ModFrsDprsNetTpmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 3, 2, 10, 1)
)
modFrsDprsNetTpmProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "modIndex"),
    (0, "Nortel-Magellan-Passport-ModCommonMIB", "modFrsIndex"),
    (0, "Nortel-Magellan-Passport-ModDprsQosMIB", "modFrsDprsNetIndex"),
    (0, "Nortel-Magellan-Passport-ModDprsQosMIB", "modFrsDprsNetTpmIndex"),
)
if mibBuilder.loadTexts:
    modFrsDprsNetTpmProvEntry.setStatus("mandatory")


class _ModFrsDprsNetTpmEmissionPriority_Type(Unsigned32):
    """Custom type modFrsDprsNetTpmEmissionPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ModFrsDprsNetTpmEmissionPriority_Type.__name__ = "Unsigned32"
_ModFrsDprsNetTpmEmissionPriority_Object = MibTableColumn
modFrsDprsNetTpmEmissionPriority = _ModFrsDprsNetTpmEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 3, 2, 10, 1, 1),
    _ModFrsDprsNetTpmEmissionPriority_Type()
)
modFrsDprsNetTpmEmissionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modFrsDprsNetTpmEmissionPriority.setStatus("mandatory")


class _ModFrsDprsNetTpmRoutingClassOfService_Type(Integer32):
    """Custom type modFrsDprsNetTpmRoutingClassOfService based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delay", 1),
          ("multimedia", 2),
          ("throughput", 0))
    )


_ModFrsDprsNetTpmRoutingClassOfService_Type.__name__ = "Integer32"
_ModFrsDprsNetTpmRoutingClassOfService_Object = MibTableColumn
modFrsDprsNetTpmRoutingClassOfService = _ModFrsDprsNetTpmRoutingClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 3, 2, 10, 1, 2),
    _ModFrsDprsNetTpmRoutingClassOfService_Type()
)
modFrsDprsNetTpmRoutingClassOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modFrsDprsNetTpmRoutingClassOfService.setStatus("mandatory")
_ModDprsQosMIB_ObjectIdentity = ObjectIdentity
modDprsQosMIB = _ModDprsQosMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 76)
)
_ModDprsQosGroup_ObjectIdentity = ObjectIdentity
modDprsQosGroup = _ModDprsQosGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 76, 1)
)
_ModDprsQosGroupBE_ObjectIdentity = ObjectIdentity
modDprsQosGroupBE = _ModDprsQosGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 76, 1, 5)
)
_ModDprsQosGroupBE01_ObjectIdentity = ObjectIdentity
modDprsQosGroupBE01 = _ModDprsQosGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 76, 1, 5, 2)
)
_ModDprsQosGroupBE01A_ObjectIdentity = ObjectIdentity
modDprsQosGroupBE01A = _ModDprsQosGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 76, 1, 5, 2, 2)
)
_ModDprsQosCapabilities_ObjectIdentity = ObjectIdentity
modDprsQosCapabilities = _ModDprsQosCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 76, 3)
)
_ModDprsQosCapabilitiesBE_ObjectIdentity = ObjectIdentity
modDprsQosCapabilitiesBE = _ModDprsQosCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 76, 3, 5)
)
_ModDprsQosCapabilitiesBE01_ObjectIdentity = ObjectIdentity
modDprsQosCapabilitiesBE01 = _ModDprsQosCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 76, 3, 5, 2)
)
_ModDprsQosCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
modDprsQosCapabilitiesBE01A = _ModDprsQosCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 76, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-ModDprsQosMIB",
    **{"modFrsDprsNet": modFrsDprsNet,
       "modFrsDprsNetRowStatusTable": modFrsDprsNetRowStatusTable,
       "modFrsDprsNetRowStatusEntry": modFrsDprsNetRowStatusEntry,
       "modFrsDprsNetRowStatus": modFrsDprsNetRowStatus,
       "modFrsDprsNetComponentName": modFrsDprsNetComponentName,
       "modFrsDprsNetStorageType": modFrsDprsNetStorageType,
       "modFrsDprsNetIndex": modFrsDprsNetIndex,
       "modFrsDprsNetTpm": modFrsDprsNetTpm,
       "modFrsDprsNetTpmRowStatusTable": modFrsDprsNetTpmRowStatusTable,
       "modFrsDprsNetTpmRowStatusEntry": modFrsDprsNetTpmRowStatusEntry,
       "modFrsDprsNetTpmRowStatus": modFrsDprsNetTpmRowStatus,
       "modFrsDprsNetTpmComponentName": modFrsDprsNetTpmComponentName,
       "modFrsDprsNetTpmStorageType": modFrsDprsNetTpmStorageType,
       "modFrsDprsNetTpmIndex": modFrsDprsNetTpmIndex,
       "modFrsDprsNetTpmProvTable": modFrsDprsNetTpmProvTable,
       "modFrsDprsNetTpmProvEntry": modFrsDprsNetTpmProvEntry,
       "modFrsDprsNetTpmEmissionPriority": modFrsDprsNetTpmEmissionPriority,
       "modFrsDprsNetTpmRoutingClassOfService": modFrsDprsNetTpmRoutingClassOfService,
       "modDprsQosMIB": modDprsQosMIB,
       "modDprsQosGroup": modDprsQosGroup,
       "modDprsQosGroupBE": modDprsQosGroupBE,
       "modDprsQosGroupBE01": modDprsQosGroupBE01,
       "modDprsQosGroupBE01A": modDprsQosGroupBE01A,
       "modDprsQosCapabilities": modDprsQosCapabilities,
       "modDprsQosCapabilitiesBE": modDprsQosCapabilitiesBE,
       "modDprsQosCapabilitiesBE01": modDprsQosCapabilitiesBE01,
       "modDprsQosCapabilitiesBE01A": modDprsQosCapabilitiesBE01A}
)
