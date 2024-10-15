# SNMP MIB module (Nortel-Magellan-Passport-FrameRelayEngMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-FrameRelayEngMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:46 2024
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

(lpEng,
 lpEngIndex,
 lpIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-LogicalProcessorMIB",
    "lpEng",
    "lpEngIndex",
    "lpIndex")

(DisplayString,
 Gauge32,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "Gauge32",
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

_LpEngFrs_ObjectIdentity = ObjectIdentity
lpEngFrs = _LpEngFrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 3)
)
_LpEngFrsRowStatusTable_Object = MibTable
lpEngFrsRowStatusTable = _LpEngFrsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 3, 1)
)
if mibBuilder.loadTexts:
    lpEngFrsRowStatusTable.setStatus("mandatory")
_LpEngFrsRowStatusEntry_Object = MibTableRow
lpEngFrsRowStatusEntry = _LpEngFrsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 3, 1, 1)
)
lpEngFrsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayEngMIB", "lpEngFrsIndex"),
)
if mibBuilder.loadTexts:
    lpEngFrsRowStatusEntry.setStatus("mandatory")
_LpEngFrsRowStatus_Type = RowStatus
_LpEngFrsRowStatus_Object = MibTableColumn
lpEngFrsRowStatus = _LpEngFrsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 3, 1, 1, 1),
    _LpEngFrsRowStatus_Type()
)
lpEngFrsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngFrsRowStatus.setStatus("mandatory")
_LpEngFrsComponentName_Type = DisplayString
_LpEngFrsComponentName_Object = MibTableColumn
lpEngFrsComponentName = _LpEngFrsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 3, 1, 1, 2),
    _LpEngFrsComponentName_Type()
)
lpEngFrsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFrsComponentName.setStatus("mandatory")
_LpEngFrsStorageType_Type = StorageType
_LpEngFrsStorageType_Object = MibTableColumn
lpEngFrsStorageType = _LpEngFrsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 3, 1, 1, 4),
    _LpEngFrsStorageType_Type()
)
lpEngFrsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFrsStorageType.setStatus("mandatory")
_LpEngFrsIndex_Type = NonReplicated
_LpEngFrsIndex_Object = MibTableColumn
lpEngFrsIndex = _LpEngFrsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 3, 1, 1, 10),
    _LpEngFrsIndex_Type()
)
lpEngFrsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEngFrsIndex.setStatus("mandatory")
_LpEngFrsOv_ObjectIdentity = ObjectIdentity
lpEngFrsOv = _LpEngFrsOv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 3, 2)
)
_LpEngFrsOvRowStatusTable_Object = MibTable
lpEngFrsOvRowStatusTable = _LpEngFrsOvRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 3, 2, 1)
)
if mibBuilder.loadTexts:
    lpEngFrsOvRowStatusTable.setStatus("mandatory")
_LpEngFrsOvRowStatusEntry_Object = MibTableRow
lpEngFrsOvRowStatusEntry = _LpEngFrsOvRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 3, 2, 1, 1)
)
lpEngFrsOvRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayEngMIB", "lpEngFrsIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayEngMIB", "lpEngFrsOvIndex"),
)
if mibBuilder.loadTexts:
    lpEngFrsOvRowStatusEntry.setStatus("mandatory")
_LpEngFrsOvRowStatus_Type = RowStatus
_LpEngFrsOvRowStatus_Object = MibTableColumn
lpEngFrsOvRowStatus = _LpEngFrsOvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 3, 2, 1, 1, 1),
    _LpEngFrsOvRowStatus_Type()
)
lpEngFrsOvRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngFrsOvRowStatus.setStatus("mandatory")
_LpEngFrsOvComponentName_Type = DisplayString
_LpEngFrsOvComponentName_Object = MibTableColumn
lpEngFrsOvComponentName = _LpEngFrsOvComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 3, 2, 1, 1, 2),
    _LpEngFrsOvComponentName_Type()
)
lpEngFrsOvComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFrsOvComponentName.setStatus("mandatory")
_LpEngFrsOvStorageType_Type = StorageType
_LpEngFrsOvStorageType_Object = MibTableColumn
lpEngFrsOvStorageType = _LpEngFrsOvStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 3, 2, 1, 1, 4),
    _LpEngFrsOvStorageType_Type()
)
lpEngFrsOvStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFrsOvStorageType.setStatus("mandatory")
_LpEngFrsOvIndex_Type = NonReplicated
_LpEngFrsOvIndex_Object = MibTableColumn
lpEngFrsOvIndex = _LpEngFrsOvIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 3, 2, 1, 1, 10),
    _LpEngFrsOvIndex_Type()
)
lpEngFrsOvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEngFrsOvIndex.setStatus("mandatory")
_LpEngFrsOvProvTable_Object = MibTable
lpEngFrsOvProvTable = _LpEngFrsOvProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 3, 2, 10)
)
if mibBuilder.loadTexts:
    lpEngFrsOvProvTable.setStatus("mandatory")
_LpEngFrsOvProvEntry_Object = MibTableRow
lpEngFrsOvProvEntry = _LpEngFrsOvProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 3, 2, 10, 1)
)
lpEngFrsOvProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayEngMIB", "lpEngFrsIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayEngMIB", "lpEngFrsOvIndex"),
)
if mibBuilder.loadTexts:
    lpEngFrsOvProvEntry.setStatus("mandatory")


class _LpEngFrsOvMaxCalls_Type(Unsigned32):
    """Custom type lpEngFrsOvMaxCalls based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_LpEngFrsOvMaxCalls_Type.__name__ = "Unsigned32"
_LpEngFrsOvMaxCalls_Object = MibTableColumn
lpEngFrsOvMaxCalls = _LpEngFrsOvMaxCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 3, 2, 10, 1, 1),
    _LpEngFrsOvMaxCalls_Type()
)
lpEngFrsOvMaxCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngFrsOvMaxCalls.setStatus("mandatory")


class _LpEngFrsOvHeadroomCalls_Type(Unsigned32):
    """Custom type lpEngFrsOvHeadroomCalls based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_LpEngFrsOvHeadroomCalls_Type.__name__ = "Unsigned32"
_LpEngFrsOvHeadroomCalls_Object = MibTableColumn
lpEngFrsOvHeadroomCalls = _LpEngFrsOvHeadroomCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 3, 2, 10, 1, 2),
    _LpEngFrsOvHeadroomCalls_Type()
)
lpEngFrsOvHeadroomCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngFrsOvHeadroomCalls.setStatus("mandatory")
_LpEngFrsOperTable_Object = MibTable
lpEngFrsOperTable = _LpEngFrsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 3, 10)
)
if mibBuilder.loadTexts:
    lpEngFrsOperTable.setStatus("mandatory")
_LpEngFrsOperEntry_Object = MibTableRow
lpEngFrsOperEntry = _LpEngFrsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 3, 10, 1)
)
lpEngFrsOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayEngMIB", "lpEngFrsIndex"),
)
if mibBuilder.loadTexts:
    lpEngFrsOperEntry.setStatus("mandatory")


class _LpEngFrsMaxCalls_Type(Unsigned32):
    """Custom type lpEngFrsMaxCalls based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_LpEngFrsMaxCalls_Type.__name__ = "Unsigned32"
_LpEngFrsMaxCalls_Object = MibTableColumn
lpEngFrsMaxCalls = _LpEngFrsMaxCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 3, 10, 1, 1),
    _LpEngFrsMaxCalls_Type()
)
lpEngFrsMaxCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFrsMaxCalls.setStatus("mandatory")


class _LpEngFrsHeadroomCalls_Type(Unsigned32):
    """Custom type lpEngFrsHeadroomCalls based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_LpEngFrsHeadroomCalls_Type.__name__ = "Unsigned32"
_LpEngFrsHeadroomCalls_Object = MibTableColumn
lpEngFrsHeadroomCalls = _LpEngFrsHeadroomCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 3, 10, 1, 2),
    _LpEngFrsHeadroomCalls_Type()
)
lpEngFrsHeadroomCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFrsHeadroomCalls.setStatus("mandatory")


class _LpEngFrsCurrentCalls_Type(Gauge32):
    """Custom type lpEngFrsCurrentCalls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpEngFrsCurrentCalls_Type.__name__ = "Gauge32"
_LpEngFrsCurrentCalls_Object = MibTableColumn
lpEngFrsCurrentCalls = _LpEngFrsCurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 3, 10, 1, 3),
    _LpEngFrsCurrentCalls_Type()
)
lpEngFrsCurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFrsCurrentCalls.setStatus("mandatory")


class _LpEngFrsCallsRefused_Type(Unsigned32):
    """Custom type lpEngFrsCallsRefused based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpEngFrsCallsRefused_Type.__name__ = "Unsigned32"
_LpEngFrsCallsRefused_Object = MibTableColumn
lpEngFrsCallsRefused = _LpEngFrsCallsRefused_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 3, 10, 1, 4),
    _LpEngFrsCallsRefused_Type()
)
lpEngFrsCallsRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFrsCallsRefused.setStatus("mandatory")
_FrameRelayEngMIB_ObjectIdentity = ObjectIdentity
frameRelayEngMIB = _FrameRelayEngMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 73)
)
_FrameRelayEngGroup_ObjectIdentity = ObjectIdentity
frameRelayEngGroup = _FrameRelayEngGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 73, 1)
)
_FrameRelayEngGroupBE_ObjectIdentity = ObjectIdentity
frameRelayEngGroupBE = _FrameRelayEngGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 73, 1, 5)
)
_FrameRelayEngGroupBE00_ObjectIdentity = ObjectIdentity
frameRelayEngGroupBE00 = _FrameRelayEngGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 73, 1, 5, 1)
)
_FrameRelayEngGroupBE00A_ObjectIdentity = ObjectIdentity
frameRelayEngGroupBE00A = _FrameRelayEngGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 73, 1, 5, 1, 2)
)
_FrameRelayEngCapabilities_ObjectIdentity = ObjectIdentity
frameRelayEngCapabilities = _FrameRelayEngCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 73, 3)
)
_FrameRelayEngCapabilitiesBE_ObjectIdentity = ObjectIdentity
frameRelayEngCapabilitiesBE = _FrameRelayEngCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 73, 3, 5)
)
_FrameRelayEngCapabilitiesBE00_ObjectIdentity = ObjectIdentity
frameRelayEngCapabilitiesBE00 = _FrameRelayEngCapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 73, 3, 5, 1)
)
_FrameRelayEngCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
frameRelayEngCapabilitiesBE00A = _FrameRelayEngCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 73, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-FrameRelayEngMIB",
    **{"lpEngFrs": lpEngFrs,
       "lpEngFrsRowStatusTable": lpEngFrsRowStatusTable,
       "lpEngFrsRowStatusEntry": lpEngFrsRowStatusEntry,
       "lpEngFrsRowStatus": lpEngFrsRowStatus,
       "lpEngFrsComponentName": lpEngFrsComponentName,
       "lpEngFrsStorageType": lpEngFrsStorageType,
       "lpEngFrsIndex": lpEngFrsIndex,
       "lpEngFrsOv": lpEngFrsOv,
       "lpEngFrsOvRowStatusTable": lpEngFrsOvRowStatusTable,
       "lpEngFrsOvRowStatusEntry": lpEngFrsOvRowStatusEntry,
       "lpEngFrsOvRowStatus": lpEngFrsOvRowStatus,
       "lpEngFrsOvComponentName": lpEngFrsOvComponentName,
       "lpEngFrsOvStorageType": lpEngFrsOvStorageType,
       "lpEngFrsOvIndex": lpEngFrsOvIndex,
       "lpEngFrsOvProvTable": lpEngFrsOvProvTable,
       "lpEngFrsOvProvEntry": lpEngFrsOvProvEntry,
       "lpEngFrsOvMaxCalls": lpEngFrsOvMaxCalls,
       "lpEngFrsOvHeadroomCalls": lpEngFrsOvHeadroomCalls,
       "lpEngFrsOperTable": lpEngFrsOperTable,
       "lpEngFrsOperEntry": lpEngFrsOperEntry,
       "lpEngFrsMaxCalls": lpEngFrsMaxCalls,
       "lpEngFrsHeadroomCalls": lpEngFrsHeadroomCalls,
       "lpEngFrsCurrentCalls": lpEngFrsCurrentCalls,
       "lpEngFrsCallsRefused": lpEngFrsCallsRefused,
       "frameRelayEngMIB": frameRelayEngMIB,
       "frameRelayEngGroup": frameRelayEngGroup,
       "frameRelayEngGroupBE": frameRelayEngGroupBE,
       "frameRelayEngGroupBE00": frameRelayEngGroupBE00,
       "frameRelayEngGroupBE00A": frameRelayEngGroupBE00A,
       "frameRelayEngCapabilities": frameRelayEngCapabilities,
       "frameRelayEngCapabilitiesBE": frameRelayEngCapabilitiesBE,
       "frameRelayEngCapabilitiesBE00": frameRelayEngCapabilitiesBE00,
       "frameRelayEngCapabilitiesBE00A": frameRelayEngCapabilitiesBE00A}
)
