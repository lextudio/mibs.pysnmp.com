# SNMP MIB module (Nortel-Magellan-Passport-CallServerMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-CallServerMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:29 2024
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
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(NonReplicated,
 WildcardedDigitString) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "NonReplicated",
    "WildcardedDigitString")

(components,
 passportMIBs) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "components",
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

_CR_ObjectIdentity = ObjectIdentity
cR = _CR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42)
)
_CRRowStatusTable_Object = MibTable
cRRowStatusTable = _CRRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 1)
)
if mibBuilder.loadTexts:
    cRRowStatusTable.setStatus("mandatory")
_CRRowStatusEntry_Object = MibTableRow
cRRowStatusEntry = _CRRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 1, 1)
)
cRRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CallServerMIB", "cRIndex"),
)
if mibBuilder.loadTexts:
    cRRowStatusEntry.setStatus("mandatory")
_CRRowStatus_Type = RowStatus
_CRRowStatus_Object = MibTableColumn
cRRowStatus = _CRRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 1, 1, 1),
    _CRRowStatus_Type()
)
cRRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRRowStatus.setStatus("mandatory")
_CRComponentName_Type = DisplayString
_CRComponentName_Object = MibTableColumn
cRComponentName = _CRComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 1, 1, 2),
    _CRComponentName_Type()
)
cRComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRComponentName.setStatus("mandatory")
_CRStorageType_Type = StorageType
_CRStorageType_Object = MibTableColumn
cRStorageType = _CRStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 1, 1, 4),
    _CRStorageType_Type()
)
cRStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRStorageType.setStatus("mandatory")
_CRIndex_Type = NonReplicated
_CRIndex_Object = MibTableColumn
cRIndex = _CRIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 1, 1, 10),
    _CRIndex_Type()
)
cRIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cRIndex.setStatus("mandatory")
_CRNpi_ObjectIdentity = ObjectIdentity
cRNpi = _CRNpi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 2)
)
_CRNpiRowStatusTable_Object = MibTable
cRNpiRowStatusTable = _CRNpiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 2, 1)
)
if mibBuilder.loadTexts:
    cRNpiRowStatusTable.setStatus("mandatory")
_CRNpiRowStatusEntry_Object = MibTableRow
cRNpiRowStatusEntry = _CRNpiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 2, 1, 1)
)
cRNpiRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CallServerMIB", "cRIndex"),
    (0, "Nortel-Magellan-Passport-CallServerMIB", "cRNpiIndex"),
)
if mibBuilder.loadTexts:
    cRNpiRowStatusEntry.setStatus("mandatory")
_CRNpiRowStatus_Type = RowStatus
_CRNpiRowStatus_Object = MibTableColumn
cRNpiRowStatus = _CRNpiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 2, 1, 1, 1),
    _CRNpiRowStatus_Type()
)
cRNpiRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRNpiRowStatus.setStatus("mandatory")
_CRNpiComponentName_Type = DisplayString
_CRNpiComponentName_Object = MibTableColumn
cRNpiComponentName = _CRNpiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 2, 1, 1, 2),
    _CRNpiComponentName_Type()
)
cRNpiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRNpiComponentName.setStatus("mandatory")
_CRNpiStorageType_Type = StorageType
_CRNpiStorageType_Object = MibTableColumn
cRNpiStorageType = _CRNpiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 2, 1, 1, 4),
    _CRNpiStorageType_Type()
)
cRNpiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRNpiStorageType.setStatus("mandatory")


class _CRNpiIndex_Type(Integer32):
    """Custom type cRNpiIndex based on Integer32"""
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


_CRNpiIndex_Type.__name__ = "Integer32"
_CRNpiIndex_Object = MibTableColumn
cRNpiIndex = _CRNpiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 2, 1, 1, 10),
    _CRNpiIndex_Type()
)
cRNpiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cRNpiIndex.setStatus("mandatory")
_CRNpiDna_ObjectIdentity = ObjectIdentity
cRNpiDna = _CRNpiDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 2, 2)
)
_CRNpiDnaRowStatusTable_Object = MibTable
cRNpiDnaRowStatusTable = _CRNpiDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cRNpiDnaRowStatusTable.setStatus("mandatory")
_CRNpiDnaRowStatusEntry_Object = MibTableRow
cRNpiDnaRowStatusEntry = _CRNpiDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 2, 2, 1, 1)
)
cRNpiDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CallServerMIB", "cRIndex"),
    (0, "Nortel-Magellan-Passport-CallServerMIB", "cRNpiIndex"),
    (0, "Nortel-Magellan-Passport-CallServerMIB", "cRNpiDnaIndex"),
)
if mibBuilder.loadTexts:
    cRNpiDnaRowStatusEntry.setStatus("mandatory")
_CRNpiDnaRowStatus_Type = RowStatus
_CRNpiDnaRowStatus_Object = MibTableColumn
cRNpiDnaRowStatus = _CRNpiDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 2, 2, 1, 1, 1),
    _CRNpiDnaRowStatus_Type()
)
cRNpiDnaRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRNpiDnaRowStatus.setStatus("mandatory")
_CRNpiDnaComponentName_Type = DisplayString
_CRNpiDnaComponentName_Object = MibTableColumn
cRNpiDnaComponentName = _CRNpiDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 2, 2, 1, 1, 2),
    _CRNpiDnaComponentName_Type()
)
cRNpiDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRNpiDnaComponentName.setStatus("mandatory")
_CRNpiDnaStorageType_Type = StorageType
_CRNpiDnaStorageType_Object = MibTableColumn
cRNpiDnaStorageType = _CRNpiDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 2, 2, 1, 1, 4),
    _CRNpiDnaStorageType_Type()
)
cRNpiDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRNpiDnaStorageType.setStatus("mandatory")


class _CRNpiDnaIndex_Type(WildcardedDigitString):
    """Custom type cRNpiDnaIndex based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_CRNpiDnaIndex_Type.__name__ = "WildcardedDigitString"
_CRNpiDnaIndex_Object = MibTableColumn
cRNpiDnaIndex = _CRNpiDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 2, 2, 1, 1, 10),
    _CRNpiDnaIndex_Type()
)
cRNpiDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cRNpiDnaIndex.setStatus("mandatory")
_CRNpiDnaProvTable_Object = MibTable
cRNpiDnaProvTable = _CRNpiDnaProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 2, 2, 10)
)
if mibBuilder.loadTexts:
    cRNpiDnaProvTable.setStatus("mandatory")
_CRNpiDnaProvEntry_Object = MibTableRow
cRNpiDnaProvEntry = _CRNpiDnaProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 2, 2, 10, 1)
)
cRNpiDnaProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CallServerMIB", "cRIndex"),
    (0, "Nortel-Magellan-Passport-CallServerMIB", "cRNpiIndex"),
    (0, "Nortel-Magellan-Passport-CallServerMIB", "cRNpiDnaIndex"),
)
if mibBuilder.loadTexts:
    cRNpiDnaProvEntry.setStatus("mandatory")


class _CRNpiDnaRoutingId_Type(Unsigned32):
    """Custom type cRNpiDnaRoutingId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_CRNpiDnaRoutingId_Type.__name__ = "Unsigned32"
_CRNpiDnaRoutingId_Object = MibTableColumn
cRNpiDnaRoutingId = _CRNpiDnaRoutingId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 2, 2, 10, 1, 1),
    _CRNpiDnaRoutingId_Type()
)
cRNpiDnaRoutingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRNpiDnaRoutingId.setStatus("mandatory")


class _CRNpiDnaModuleId_Type(Unsigned32):
    """Custom type cRNpiDnaModuleId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1909),
    )


_CRNpiDnaModuleId_Type.__name__ = "Unsigned32"
_CRNpiDnaModuleId_Object = MibTableColumn
cRNpiDnaModuleId = _CRNpiDnaModuleId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 2, 2, 10, 1, 2),
    _CRNpiDnaModuleId_Type()
)
cRNpiDnaModuleId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRNpiDnaModuleId.setStatus("mandatory")
_CRNpiStatsTable_Object = MibTable
cRNpiStatsTable = _CRNpiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 2, 10)
)
if mibBuilder.loadTexts:
    cRNpiStatsTable.setStatus("mandatory")
_CRNpiStatsEntry_Object = MibTableRow
cRNpiStatsEntry = _CRNpiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 2, 10, 1)
)
cRNpiStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CallServerMIB", "cRIndex"),
    (0, "Nortel-Magellan-Passport-CallServerMIB", "cRNpiIndex"),
)
if mibBuilder.loadTexts:
    cRNpiStatsEntry.setStatus("mandatory")


class _CRNpiTotalDnas_Type(Unsigned32):
    """Custom type cRNpiTotalDnas based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CRNpiTotalDnas_Type.__name__ = "Unsigned32"
_CRNpiTotalDnas_Object = MibTableColumn
cRNpiTotalDnas = _CRNpiTotalDnas_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 2, 10, 1, 1),
    _CRNpiTotalDnas_Type()
)
cRNpiTotalDnas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRNpiTotalDnas.setStatus("mandatory")
_CRNpiCallsRouted_Type = Counter32
_CRNpiCallsRouted_Object = MibTableColumn
cRNpiCallsRouted = _CRNpiCallsRouted_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 2, 10, 1, 2),
    _CRNpiCallsRouted_Type()
)
cRNpiCallsRouted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRNpiCallsRouted.setStatus("mandatory")
_CRNpiCallsFailed_Type = Counter32
_CRNpiCallsFailed_Object = MibTableColumn
cRNpiCallsFailed = _CRNpiCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 42, 2, 10, 1, 3),
    _CRNpiCallsFailed_Type()
)
cRNpiCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRNpiCallsFailed.setStatus("mandatory")
_CallServerMIB_ObjectIdentity = ObjectIdentity
callServerMIB = _CallServerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 41)
)
_CallServerGroup_ObjectIdentity = ObjectIdentity
callServerGroup = _CallServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 41, 1)
)
_CallServerGroupBC_ObjectIdentity = ObjectIdentity
callServerGroupBC = _CallServerGroupBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 41, 1, 3)
)
_CallServerGroupBC02_ObjectIdentity = ObjectIdentity
callServerGroupBC02 = _CallServerGroupBC02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 41, 1, 3, 3)
)
_CallServerGroupBC02A_ObjectIdentity = ObjectIdentity
callServerGroupBC02A = _CallServerGroupBC02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 41, 1, 3, 3, 2)
)
_CallServerCapabilities_ObjectIdentity = ObjectIdentity
callServerCapabilities = _CallServerCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 41, 3)
)
_CallServerCapabilitiesBC_ObjectIdentity = ObjectIdentity
callServerCapabilitiesBC = _CallServerCapabilitiesBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 41, 3, 3)
)
_CallServerCapabilitiesBC02_ObjectIdentity = ObjectIdentity
callServerCapabilitiesBC02 = _CallServerCapabilitiesBC02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 41, 3, 3, 3)
)
_CallServerCapabilitiesBC02A_ObjectIdentity = ObjectIdentity
callServerCapabilitiesBC02A = _CallServerCapabilitiesBC02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 41, 3, 3, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-CallServerMIB",
    **{"cR": cR,
       "cRRowStatusTable": cRRowStatusTable,
       "cRRowStatusEntry": cRRowStatusEntry,
       "cRRowStatus": cRRowStatus,
       "cRComponentName": cRComponentName,
       "cRStorageType": cRStorageType,
       "cRIndex": cRIndex,
       "cRNpi": cRNpi,
       "cRNpiRowStatusTable": cRNpiRowStatusTable,
       "cRNpiRowStatusEntry": cRNpiRowStatusEntry,
       "cRNpiRowStatus": cRNpiRowStatus,
       "cRNpiComponentName": cRNpiComponentName,
       "cRNpiStorageType": cRNpiStorageType,
       "cRNpiIndex": cRNpiIndex,
       "cRNpiDna": cRNpiDna,
       "cRNpiDnaRowStatusTable": cRNpiDnaRowStatusTable,
       "cRNpiDnaRowStatusEntry": cRNpiDnaRowStatusEntry,
       "cRNpiDnaRowStatus": cRNpiDnaRowStatus,
       "cRNpiDnaComponentName": cRNpiDnaComponentName,
       "cRNpiDnaStorageType": cRNpiDnaStorageType,
       "cRNpiDnaIndex": cRNpiDnaIndex,
       "cRNpiDnaProvTable": cRNpiDnaProvTable,
       "cRNpiDnaProvEntry": cRNpiDnaProvEntry,
       "cRNpiDnaRoutingId": cRNpiDnaRoutingId,
       "cRNpiDnaModuleId": cRNpiDnaModuleId,
       "cRNpiStatsTable": cRNpiStatsTable,
       "cRNpiStatsEntry": cRNpiStatsEntry,
       "cRNpiTotalDnas": cRNpiTotalDnas,
       "cRNpiCallsRouted": cRNpiCallsRouted,
       "cRNpiCallsFailed": cRNpiCallsFailed,
       "callServerMIB": callServerMIB,
       "callServerGroup": callServerGroup,
       "callServerGroupBC": callServerGroupBC,
       "callServerGroupBC02": callServerGroupBC02,
       "callServerGroupBC02A": callServerGroupBC02A,
       "callServerCapabilities": callServerCapabilities,
       "callServerCapabilitiesBC": callServerCapabilitiesBC,
       "callServerCapabilitiesBC02": callServerCapabilitiesBC02,
       "callServerCapabilitiesBC02A": callServerCapabilitiesBC02A}
)
