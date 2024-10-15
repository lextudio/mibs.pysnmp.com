# SNMP MIB module (Nortel-MsCarrier-MscPassport-CallServerMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-CallServerMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:05 2024
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

(Counter32,
 DisplayString,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(NonReplicated,
 WildcardedDigitString) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "NonReplicated",
    "WildcardedDigitString")

(mscComponents,
 mscPassportMIBs) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscComponents",
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

_MscCR_ObjectIdentity = ObjectIdentity
mscCR = _MscCR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42)
)
_MscCRRowStatusTable_Object = MibTable
mscCRRowStatusTable = _MscCRRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 1)
)
if mibBuilder.loadTexts:
    mscCRRowStatusTable.setStatus("mandatory")
_MscCRRowStatusEntry_Object = MibTableRow
mscCRRowStatusEntry = _MscCRRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 1, 1)
)
mscCRRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CallServerMIB", "mscCRIndex"),
)
if mibBuilder.loadTexts:
    mscCRRowStatusEntry.setStatus("mandatory")
_MscCRRowStatus_Type = RowStatus
_MscCRRowStatus_Object = MibTableColumn
mscCRRowStatus = _MscCRRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 1, 1, 1),
    _MscCRRowStatus_Type()
)
mscCRRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscCRRowStatus.setStatus("mandatory")
_MscCRComponentName_Type = DisplayString
_MscCRComponentName_Object = MibTableColumn
mscCRComponentName = _MscCRComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 1, 1, 2),
    _MscCRComponentName_Type()
)
mscCRComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCRComponentName.setStatus("mandatory")
_MscCRStorageType_Type = StorageType
_MscCRStorageType_Object = MibTableColumn
mscCRStorageType = _MscCRStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 1, 1, 4),
    _MscCRStorageType_Type()
)
mscCRStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCRStorageType.setStatus("mandatory")
_MscCRIndex_Type = NonReplicated
_MscCRIndex_Object = MibTableColumn
mscCRIndex = _MscCRIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 1, 1, 10),
    _MscCRIndex_Type()
)
mscCRIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscCRIndex.setStatus("mandatory")
_MscCRNpi_ObjectIdentity = ObjectIdentity
mscCRNpi = _MscCRNpi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 2)
)
_MscCRNpiRowStatusTable_Object = MibTable
mscCRNpiRowStatusTable = _MscCRNpiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 2, 1)
)
if mibBuilder.loadTexts:
    mscCRNpiRowStatusTable.setStatus("mandatory")
_MscCRNpiRowStatusEntry_Object = MibTableRow
mscCRNpiRowStatusEntry = _MscCRNpiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 2, 1, 1)
)
mscCRNpiRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CallServerMIB", "mscCRIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CallServerMIB", "mscCRNpiIndex"),
)
if mibBuilder.loadTexts:
    mscCRNpiRowStatusEntry.setStatus("mandatory")
_MscCRNpiRowStatus_Type = RowStatus
_MscCRNpiRowStatus_Object = MibTableColumn
mscCRNpiRowStatus = _MscCRNpiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 2, 1, 1, 1),
    _MscCRNpiRowStatus_Type()
)
mscCRNpiRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscCRNpiRowStatus.setStatus("mandatory")
_MscCRNpiComponentName_Type = DisplayString
_MscCRNpiComponentName_Object = MibTableColumn
mscCRNpiComponentName = _MscCRNpiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 2, 1, 1, 2),
    _MscCRNpiComponentName_Type()
)
mscCRNpiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCRNpiComponentName.setStatus("mandatory")
_MscCRNpiStorageType_Type = StorageType
_MscCRNpiStorageType_Object = MibTableColumn
mscCRNpiStorageType = _MscCRNpiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 2, 1, 1, 4),
    _MscCRNpiStorageType_Type()
)
mscCRNpiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCRNpiStorageType.setStatus("mandatory")


class _MscCRNpiIndex_Type(Integer32):
    """Custom type mscCRNpiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_MscCRNpiIndex_Type.__name__ = "Integer32"
_MscCRNpiIndex_Object = MibTableColumn
mscCRNpiIndex = _MscCRNpiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 2, 1, 1, 10),
    _MscCRNpiIndex_Type()
)
mscCRNpiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscCRNpiIndex.setStatus("mandatory")
_MscCRNpiDna_ObjectIdentity = ObjectIdentity
mscCRNpiDna = _MscCRNpiDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 2, 2)
)
_MscCRNpiDnaRowStatusTable_Object = MibTable
mscCRNpiDnaRowStatusTable = _MscCRNpiDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscCRNpiDnaRowStatusTable.setStatus("mandatory")
_MscCRNpiDnaRowStatusEntry_Object = MibTableRow
mscCRNpiDnaRowStatusEntry = _MscCRNpiDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 2, 2, 1, 1)
)
mscCRNpiDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CallServerMIB", "mscCRIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CallServerMIB", "mscCRNpiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CallServerMIB", "mscCRNpiDnaIndex"),
)
if mibBuilder.loadTexts:
    mscCRNpiDnaRowStatusEntry.setStatus("mandatory")
_MscCRNpiDnaRowStatus_Type = RowStatus
_MscCRNpiDnaRowStatus_Object = MibTableColumn
mscCRNpiDnaRowStatus = _MscCRNpiDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 2, 2, 1, 1, 1),
    _MscCRNpiDnaRowStatus_Type()
)
mscCRNpiDnaRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscCRNpiDnaRowStatus.setStatus("mandatory")
_MscCRNpiDnaComponentName_Type = DisplayString
_MscCRNpiDnaComponentName_Object = MibTableColumn
mscCRNpiDnaComponentName = _MscCRNpiDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 2, 2, 1, 1, 2),
    _MscCRNpiDnaComponentName_Type()
)
mscCRNpiDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCRNpiDnaComponentName.setStatus("mandatory")
_MscCRNpiDnaStorageType_Type = StorageType
_MscCRNpiDnaStorageType_Object = MibTableColumn
mscCRNpiDnaStorageType = _MscCRNpiDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 2, 2, 1, 1, 4),
    _MscCRNpiDnaStorageType_Type()
)
mscCRNpiDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCRNpiDnaStorageType.setStatus("mandatory")


class _MscCRNpiDnaIndex_Type(WildcardedDigitString):
    """Custom type mscCRNpiDnaIndex based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscCRNpiDnaIndex_Type.__name__ = "WildcardedDigitString"
_MscCRNpiDnaIndex_Object = MibTableColumn
mscCRNpiDnaIndex = _MscCRNpiDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 2, 2, 1, 1, 10),
    _MscCRNpiDnaIndex_Type()
)
mscCRNpiDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscCRNpiDnaIndex.setStatus("mandatory")
_MscCRNpiDnaProvTable_Object = MibTable
mscCRNpiDnaProvTable = _MscCRNpiDnaProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscCRNpiDnaProvTable.setStatus("mandatory")
_MscCRNpiDnaProvEntry_Object = MibTableRow
mscCRNpiDnaProvEntry = _MscCRNpiDnaProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 2, 2, 10, 1)
)
mscCRNpiDnaProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CallServerMIB", "mscCRIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CallServerMIB", "mscCRNpiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CallServerMIB", "mscCRNpiDnaIndex"),
)
if mibBuilder.loadTexts:
    mscCRNpiDnaProvEntry.setStatus("mandatory")


class _MscCRNpiDnaRoutingId_Type(Unsigned32):
    """Custom type mscCRNpiDnaRoutingId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_MscCRNpiDnaRoutingId_Type.__name__ = "Unsigned32"
_MscCRNpiDnaRoutingId_Object = MibTableColumn
mscCRNpiDnaRoutingId = _MscCRNpiDnaRoutingId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 2, 2, 10, 1, 1),
    _MscCRNpiDnaRoutingId_Type()
)
mscCRNpiDnaRoutingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscCRNpiDnaRoutingId.setStatus("mandatory")


class _MscCRNpiDnaModuleId_Type(Unsigned32):
    """Custom type mscCRNpiDnaModuleId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1909),
    )


_MscCRNpiDnaModuleId_Type.__name__ = "Unsigned32"
_MscCRNpiDnaModuleId_Object = MibTableColumn
mscCRNpiDnaModuleId = _MscCRNpiDnaModuleId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 2, 2, 10, 1, 2),
    _MscCRNpiDnaModuleId_Type()
)
mscCRNpiDnaModuleId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscCRNpiDnaModuleId.setStatus("mandatory")
_MscCRNpiStatsTable_Object = MibTable
mscCRNpiStatsTable = _MscCRNpiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 2, 10)
)
if mibBuilder.loadTexts:
    mscCRNpiStatsTable.setStatus("mandatory")
_MscCRNpiStatsEntry_Object = MibTableRow
mscCRNpiStatsEntry = _MscCRNpiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 2, 10, 1)
)
mscCRNpiStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CallServerMIB", "mscCRIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CallServerMIB", "mscCRNpiIndex"),
)
if mibBuilder.loadTexts:
    mscCRNpiStatsEntry.setStatus("mandatory")


class _MscCRNpiTotalDnas_Type(Unsigned32):
    """Custom type mscCRNpiTotalDnas based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscCRNpiTotalDnas_Type.__name__ = "Unsigned32"
_MscCRNpiTotalDnas_Object = MibTableColumn
mscCRNpiTotalDnas = _MscCRNpiTotalDnas_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 2, 10, 1, 1),
    _MscCRNpiTotalDnas_Type()
)
mscCRNpiTotalDnas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCRNpiTotalDnas.setStatus("mandatory")
_MscCRNpiCallsRouted_Type = Counter32
_MscCRNpiCallsRouted_Object = MibTableColumn
mscCRNpiCallsRouted = _MscCRNpiCallsRouted_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 2, 10, 1, 2),
    _MscCRNpiCallsRouted_Type()
)
mscCRNpiCallsRouted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCRNpiCallsRouted.setStatus("mandatory")
_MscCRNpiCallsFailed_Type = Counter32
_MscCRNpiCallsFailed_Object = MibTableColumn
mscCRNpiCallsFailed = _MscCRNpiCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 42, 2, 10, 1, 3),
    _MscCRNpiCallsFailed_Type()
)
mscCRNpiCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCRNpiCallsFailed.setStatus("mandatory")
_CallServerMIB_ObjectIdentity = ObjectIdentity
callServerMIB = _CallServerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 41)
)
_CallServerGroup_ObjectIdentity = ObjectIdentity
callServerGroup = _CallServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 41, 1)
)
_CallServerGroupCA_ObjectIdentity = ObjectIdentity
callServerGroupCA = _CallServerGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 41, 1, 1)
)
_CallServerGroupCA02_ObjectIdentity = ObjectIdentity
callServerGroupCA02 = _CallServerGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 41, 1, 1, 3)
)
_CallServerGroupCA02A_ObjectIdentity = ObjectIdentity
callServerGroupCA02A = _CallServerGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 41, 1, 1, 3, 2)
)
_CallServerCapabilities_ObjectIdentity = ObjectIdentity
callServerCapabilities = _CallServerCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 41, 3)
)
_CallServerCapabilitiesCA_ObjectIdentity = ObjectIdentity
callServerCapabilitiesCA = _CallServerCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 41, 3, 1)
)
_CallServerCapabilitiesCA02_ObjectIdentity = ObjectIdentity
callServerCapabilitiesCA02 = _CallServerCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 41, 3, 1, 3)
)
_CallServerCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
callServerCapabilitiesCA02A = _CallServerCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 41, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-CallServerMIB",
    **{"mscCR": mscCR,
       "mscCRRowStatusTable": mscCRRowStatusTable,
       "mscCRRowStatusEntry": mscCRRowStatusEntry,
       "mscCRRowStatus": mscCRRowStatus,
       "mscCRComponentName": mscCRComponentName,
       "mscCRStorageType": mscCRStorageType,
       "mscCRIndex": mscCRIndex,
       "mscCRNpi": mscCRNpi,
       "mscCRNpiRowStatusTable": mscCRNpiRowStatusTable,
       "mscCRNpiRowStatusEntry": mscCRNpiRowStatusEntry,
       "mscCRNpiRowStatus": mscCRNpiRowStatus,
       "mscCRNpiComponentName": mscCRNpiComponentName,
       "mscCRNpiStorageType": mscCRNpiStorageType,
       "mscCRNpiIndex": mscCRNpiIndex,
       "mscCRNpiDna": mscCRNpiDna,
       "mscCRNpiDnaRowStatusTable": mscCRNpiDnaRowStatusTable,
       "mscCRNpiDnaRowStatusEntry": mscCRNpiDnaRowStatusEntry,
       "mscCRNpiDnaRowStatus": mscCRNpiDnaRowStatus,
       "mscCRNpiDnaComponentName": mscCRNpiDnaComponentName,
       "mscCRNpiDnaStorageType": mscCRNpiDnaStorageType,
       "mscCRNpiDnaIndex": mscCRNpiDnaIndex,
       "mscCRNpiDnaProvTable": mscCRNpiDnaProvTable,
       "mscCRNpiDnaProvEntry": mscCRNpiDnaProvEntry,
       "mscCRNpiDnaRoutingId": mscCRNpiDnaRoutingId,
       "mscCRNpiDnaModuleId": mscCRNpiDnaModuleId,
       "mscCRNpiStatsTable": mscCRNpiStatsTable,
       "mscCRNpiStatsEntry": mscCRNpiStatsEntry,
       "mscCRNpiTotalDnas": mscCRNpiTotalDnas,
       "mscCRNpiCallsRouted": mscCRNpiCallsRouted,
       "mscCRNpiCallsFailed": mscCRNpiCallsFailed,
       "callServerMIB": callServerMIB,
       "callServerGroup": callServerGroup,
       "callServerGroupCA": callServerGroupCA,
       "callServerGroupCA02": callServerGroupCA02,
       "callServerGroupCA02A": callServerGroupCA02A,
       "callServerCapabilities": callServerCapabilities,
       "callServerCapabilitiesCA": callServerCapabilitiesCA,
       "callServerCapabilitiesCA02": callServerCapabilitiesCA02,
       "callServerCapabilitiesCA02A": callServerCapabilitiesCA02A}
)
