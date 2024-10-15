# SNMP MIB module (Nortel-MsCarrier-MscPassport-FrameRelayEngMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-FrameRelayEngMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:26 2024
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

(mscLpEng,
 mscLpEngIndex,
 mscLpIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB",
    "mscLpEng",
    "mscLpEngIndex",
    "mscLpIndex")

(DisplayString,
 Gauge32,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DisplayString",
    "Gauge32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

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

_MscLpEngFrs_ObjectIdentity = ObjectIdentity
mscLpEngFrs = _MscLpEngFrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 3)
)
_MscLpEngFrsRowStatusTable_Object = MibTable
mscLpEngFrsRowStatusTable = _MscLpEngFrsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 3, 1)
)
if mibBuilder.loadTexts:
    mscLpEngFrsRowStatusTable.setStatus("mandatory")
_MscLpEngFrsRowStatusEntry_Object = MibTableRow
mscLpEngFrsRowStatusEntry = _MscLpEngFrsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 3, 1, 1)
)
mscLpEngFrsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayEngMIB", "mscLpEngFrsIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngFrsRowStatusEntry.setStatus("mandatory")
_MscLpEngFrsRowStatus_Type = RowStatus
_MscLpEngFrsRowStatus_Object = MibTableColumn
mscLpEngFrsRowStatus = _MscLpEngFrsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 3, 1, 1, 1),
    _MscLpEngFrsRowStatus_Type()
)
mscLpEngFrsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngFrsRowStatus.setStatus("mandatory")
_MscLpEngFrsComponentName_Type = DisplayString
_MscLpEngFrsComponentName_Object = MibTableColumn
mscLpEngFrsComponentName = _MscLpEngFrsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 3, 1, 1, 2),
    _MscLpEngFrsComponentName_Type()
)
mscLpEngFrsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFrsComponentName.setStatus("mandatory")
_MscLpEngFrsStorageType_Type = StorageType
_MscLpEngFrsStorageType_Object = MibTableColumn
mscLpEngFrsStorageType = _MscLpEngFrsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 3, 1, 1, 4),
    _MscLpEngFrsStorageType_Type()
)
mscLpEngFrsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFrsStorageType.setStatus("mandatory")
_MscLpEngFrsIndex_Type = NonReplicated
_MscLpEngFrsIndex_Object = MibTableColumn
mscLpEngFrsIndex = _MscLpEngFrsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 3, 1, 1, 10),
    _MscLpEngFrsIndex_Type()
)
mscLpEngFrsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEngFrsIndex.setStatus("mandatory")
_MscLpEngFrsOv_ObjectIdentity = ObjectIdentity
mscLpEngFrsOv = _MscLpEngFrsOv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 3, 2)
)
_MscLpEngFrsOvRowStatusTable_Object = MibTable
mscLpEngFrsOvRowStatusTable = _MscLpEngFrsOvRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscLpEngFrsOvRowStatusTable.setStatus("mandatory")
_MscLpEngFrsOvRowStatusEntry_Object = MibTableRow
mscLpEngFrsOvRowStatusEntry = _MscLpEngFrsOvRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 3, 2, 1, 1)
)
mscLpEngFrsOvRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayEngMIB", "mscLpEngFrsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayEngMIB", "mscLpEngFrsOvIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngFrsOvRowStatusEntry.setStatus("mandatory")
_MscLpEngFrsOvRowStatus_Type = RowStatus
_MscLpEngFrsOvRowStatus_Object = MibTableColumn
mscLpEngFrsOvRowStatus = _MscLpEngFrsOvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 3, 2, 1, 1, 1),
    _MscLpEngFrsOvRowStatus_Type()
)
mscLpEngFrsOvRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngFrsOvRowStatus.setStatus("mandatory")
_MscLpEngFrsOvComponentName_Type = DisplayString
_MscLpEngFrsOvComponentName_Object = MibTableColumn
mscLpEngFrsOvComponentName = _MscLpEngFrsOvComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 3, 2, 1, 1, 2),
    _MscLpEngFrsOvComponentName_Type()
)
mscLpEngFrsOvComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFrsOvComponentName.setStatus("mandatory")
_MscLpEngFrsOvStorageType_Type = StorageType
_MscLpEngFrsOvStorageType_Object = MibTableColumn
mscLpEngFrsOvStorageType = _MscLpEngFrsOvStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 3, 2, 1, 1, 4),
    _MscLpEngFrsOvStorageType_Type()
)
mscLpEngFrsOvStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFrsOvStorageType.setStatus("mandatory")
_MscLpEngFrsOvIndex_Type = NonReplicated
_MscLpEngFrsOvIndex_Object = MibTableColumn
mscLpEngFrsOvIndex = _MscLpEngFrsOvIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 3, 2, 1, 1, 10),
    _MscLpEngFrsOvIndex_Type()
)
mscLpEngFrsOvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEngFrsOvIndex.setStatus("mandatory")
_MscLpEngFrsOvProvTable_Object = MibTable
mscLpEngFrsOvProvTable = _MscLpEngFrsOvProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscLpEngFrsOvProvTable.setStatus("mandatory")
_MscLpEngFrsOvProvEntry_Object = MibTableRow
mscLpEngFrsOvProvEntry = _MscLpEngFrsOvProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 3, 2, 10, 1)
)
mscLpEngFrsOvProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayEngMIB", "mscLpEngFrsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayEngMIB", "mscLpEngFrsOvIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngFrsOvProvEntry.setStatus("mandatory")


class _MscLpEngFrsOvMaxCalls_Type(Unsigned32):
    """Custom type mscLpEngFrsOvMaxCalls based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_MscLpEngFrsOvMaxCalls_Type.__name__ = "Unsigned32"
_MscLpEngFrsOvMaxCalls_Object = MibTableColumn
mscLpEngFrsOvMaxCalls = _MscLpEngFrsOvMaxCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 3, 2, 10, 1, 1),
    _MscLpEngFrsOvMaxCalls_Type()
)
mscLpEngFrsOvMaxCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngFrsOvMaxCalls.setStatus("mandatory")


class _MscLpEngFrsOvHeadroomCalls_Type(Unsigned32):
    """Custom type mscLpEngFrsOvHeadroomCalls based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_MscLpEngFrsOvHeadroomCalls_Type.__name__ = "Unsigned32"
_MscLpEngFrsOvHeadroomCalls_Object = MibTableColumn
mscLpEngFrsOvHeadroomCalls = _MscLpEngFrsOvHeadroomCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 3, 2, 10, 1, 2),
    _MscLpEngFrsOvHeadroomCalls_Type()
)
mscLpEngFrsOvHeadroomCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngFrsOvHeadroomCalls.setStatus("mandatory")
_MscLpEngFrsOperTable_Object = MibTable
mscLpEngFrsOperTable = _MscLpEngFrsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 3, 10)
)
if mibBuilder.loadTexts:
    mscLpEngFrsOperTable.setStatus("mandatory")
_MscLpEngFrsOperEntry_Object = MibTableRow
mscLpEngFrsOperEntry = _MscLpEngFrsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 3, 10, 1)
)
mscLpEngFrsOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayEngMIB", "mscLpEngFrsIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngFrsOperEntry.setStatus("mandatory")


class _MscLpEngFrsMaxCalls_Type(Unsigned32):
    """Custom type mscLpEngFrsMaxCalls based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_MscLpEngFrsMaxCalls_Type.__name__ = "Unsigned32"
_MscLpEngFrsMaxCalls_Object = MibTableColumn
mscLpEngFrsMaxCalls = _MscLpEngFrsMaxCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 3, 10, 1, 1),
    _MscLpEngFrsMaxCalls_Type()
)
mscLpEngFrsMaxCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFrsMaxCalls.setStatus("mandatory")


class _MscLpEngFrsHeadroomCalls_Type(Unsigned32):
    """Custom type mscLpEngFrsHeadroomCalls based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_MscLpEngFrsHeadroomCalls_Type.__name__ = "Unsigned32"
_MscLpEngFrsHeadroomCalls_Object = MibTableColumn
mscLpEngFrsHeadroomCalls = _MscLpEngFrsHeadroomCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 3, 10, 1, 2),
    _MscLpEngFrsHeadroomCalls_Type()
)
mscLpEngFrsHeadroomCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFrsHeadroomCalls.setStatus("mandatory")


class _MscLpEngFrsCurrentCalls_Type(Gauge32):
    """Custom type mscLpEngFrsCurrentCalls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpEngFrsCurrentCalls_Type.__name__ = "Gauge32"
_MscLpEngFrsCurrentCalls_Object = MibTableColumn
mscLpEngFrsCurrentCalls = _MscLpEngFrsCurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 3, 10, 1, 3),
    _MscLpEngFrsCurrentCalls_Type()
)
mscLpEngFrsCurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFrsCurrentCalls.setStatus("mandatory")


class _MscLpEngFrsCallsRefused_Type(Unsigned32):
    """Custom type mscLpEngFrsCallsRefused based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpEngFrsCallsRefused_Type.__name__ = "Unsigned32"
_MscLpEngFrsCallsRefused_Object = MibTableColumn
mscLpEngFrsCallsRefused = _MscLpEngFrsCallsRefused_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 3, 10, 1, 4),
    _MscLpEngFrsCallsRefused_Type()
)
mscLpEngFrsCallsRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFrsCallsRefused.setStatus("mandatory")
_FrameRelayEngMIB_ObjectIdentity = ObjectIdentity
frameRelayEngMIB = _FrameRelayEngMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 73)
)
_FrameRelayEngGroup_ObjectIdentity = ObjectIdentity
frameRelayEngGroup = _FrameRelayEngGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 73, 1)
)
_FrameRelayEngGroupCA_ObjectIdentity = ObjectIdentity
frameRelayEngGroupCA = _FrameRelayEngGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 73, 1, 1)
)
_FrameRelayEngGroupCA02_ObjectIdentity = ObjectIdentity
frameRelayEngGroupCA02 = _FrameRelayEngGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 73, 1, 1, 3)
)
_FrameRelayEngGroupCA02A_ObjectIdentity = ObjectIdentity
frameRelayEngGroupCA02A = _FrameRelayEngGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 73, 1, 1, 3, 2)
)
_FrameRelayEngCapabilities_ObjectIdentity = ObjectIdentity
frameRelayEngCapabilities = _FrameRelayEngCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 73, 3)
)
_FrameRelayEngCapabilitiesCA_ObjectIdentity = ObjectIdentity
frameRelayEngCapabilitiesCA = _FrameRelayEngCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 73, 3, 1)
)
_FrameRelayEngCapabilitiesCA02_ObjectIdentity = ObjectIdentity
frameRelayEngCapabilitiesCA02 = _FrameRelayEngCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 73, 3, 1, 3)
)
_FrameRelayEngCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
frameRelayEngCapabilitiesCA02A = _FrameRelayEngCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 73, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-FrameRelayEngMIB",
    **{"mscLpEngFrs": mscLpEngFrs,
       "mscLpEngFrsRowStatusTable": mscLpEngFrsRowStatusTable,
       "mscLpEngFrsRowStatusEntry": mscLpEngFrsRowStatusEntry,
       "mscLpEngFrsRowStatus": mscLpEngFrsRowStatus,
       "mscLpEngFrsComponentName": mscLpEngFrsComponentName,
       "mscLpEngFrsStorageType": mscLpEngFrsStorageType,
       "mscLpEngFrsIndex": mscLpEngFrsIndex,
       "mscLpEngFrsOv": mscLpEngFrsOv,
       "mscLpEngFrsOvRowStatusTable": mscLpEngFrsOvRowStatusTable,
       "mscLpEngFrsOvRowStatusEntry": mscLpEngFrsOvRowStatusEntry,
       "mscLpEngFrsOvRowStatus": mscLpEngFrsOvRowStatus,
       "mscLpEngFrsOvComponentName": mscLpEngFrsOvComponentName,
       "mscLpEngFrsOvStorageType": mscLpEngFrsOvStorageType,
       "mscLpEngFrsOvIndex": mscLpEngFrsOvIndex,
       "mscLpEngFrsOvProvTable": mscLpEngFrsOvProvTable,
       "mscLpEngFrsOvProvEntry": mscLpEngFrsOvProvEntry,
       "mscLpEngFrsOvMaxCalls": mscLpEngFrsOvMaxCalls,
       "mscLpEngFrsOvHeadroomCalls": mscLpEngFrsOvHeadroomCalls,
       "mscLpEngFrsOperTable": mscLpEngFrsOperTable,
       "mscLpEngFrsOperEntry": mscLpEngFrsOperEntry,
       "mscLpEngFrsMaxCalls": mscLpEngFrsMaxCalls,
       "mscLpEngFrsHeadroomCalls": mscLpEngFrsHeadroomCalls,
       "mscLpEngFrsCurrentCalls": mscLpEngFrsCurrentCalls,
       "mscLpEngFrsCallsRefused": mscLpEngFrsCallsRefused,
       "frameRelayEngMIB": frameRelayEngMIB,
       "frameRelayEngGroup": frameRelayEngGroup,
       "frameRelayEngGroupCA": frameRelayEngGroupCA,
       "frameRelayEngGroupCA02": frameRelayEngGroupCA02,
       "frameRelayEngGroupCA02A": frameRelayEngGroupCA02A,
       "frameRelayEngCapabilities": frameRelayEngCapabilities,
       "frameRelayEngCapabilitiesCA": frameRelayEngCapabilitiesCA,
       "frameRelayEngCapabilitiesCA02": frameRelayEngCapabilitiesCA02,
       "frameRelayEngCapabilitiesCA02A": frameRelayEngCapabilitiesCA02A}
)
