# SNMP MIB module (Nortel-Magellan-Passport-FrTraceRcvrMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-FrTraceRcvrMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:42 2024
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

(DisplayString,
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 DigitString,
 EnterpriseDateAndTime,
 Hex,
 HexString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "DigitString",
    "EnterpriseDateAndTime",
    "Hex",
    "HexString",
    "NonReplicated")

(traceIndex,
 traceRcvr,
 traceRcvrIndex,
 traceSession,
 traceSessionIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TraceBaseMIB",
    "traceIndex",
    "traceRcvr",
    "traceRcvrIndex",
    "traceSession",
    "traceSessionIndex")

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

_TraceRcvrFr_ObjectIdentity = ObjectIdentity
traceRcvrFr = _TraceRcvrFr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3)
)
_TraceRcvrFrRowStatusTable_Object = MibTable
traceRcvrFrRowStatusTable = _TraceRcvrFrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 1)
)
if mibBuilder.loadTexts:
    traceRcvrFrRowStatusTable.setStatus("mandatory")
_TraceRcvrFrRowStatusEntry_Object = MibTableRow
traceRcvrFrRowStatusEntry = _TraceRcvrFrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 1, 1)
)
traceRcvrFrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceRcvrIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceRcvrFrIndex"),
)
if mibBuilder.loadTexts:
    traceRcvrFrRowStatusEntry.setStatus("mandatory")
_TraceRcvrFrRowStatus_Type = RowStatus
_TraceRcvrFrRowStatus_Object = MibTableColumn
traceRcvrFrRowStatus = _TraceRcvrFrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 1, 1, 1),
    _TraceRcvrFrRowStatus_Type()
)
traceRcvrFrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrFrRowStatus.setStatus("mandatory")
_TraceRcvrFrComponentName_Type = DisplayString
_TraceRcvrFrComponentName_Object = MibTableColumn
traceRcvrFrComponentName = _TraceRcvrFrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 1, 1, 2),
    _TraceRcvrFrComponentName_Type()
)
traceRcvrFrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrComponentName.setStatus("mandatory")
_TraceRcvrFrStorageType_Type = StorageType
_TraceRcvrFrStorageType_Object = MibTableColumn
traceRcvrFrStorageType = _TraceRcvrFrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 1, 1, 4),
    _TraceRcvrFrStorageType_Type()
)
traceRcvrFrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrStorageType.setStatus("mandatory")
_TraceRcvrFrIndex_Type = NonReplicated
_TraceRcvrFrIndex_Object = MibTableColumn
traceRcvrFrIndex = _TraceRcvrFrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 1, 1, 10),
    _TraceRcvrFrIndex_Type()
)
traceRcvrFrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceRcvrFrIndex.setStatus("mandatory")
_TraceRcvrFrDna_ObjectIdentity = ObjectIdentity
traceRcvrFrDna = _TraceRcvrFrDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2)
)
_TraceRcvrFrDnaRowStatusTable_Object = MibTable
traceRcvrFrDnaRowStatusTable = _TraceRcvrFrDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    traceRcvrFrDnaRowStatusTable.setStatus("mandatory")
_TraceRcvrFrDnaRowStatusEntry_Object = MibTableRow
traceRcvrFrDnaRowStatusEntry = _TraceRcvrFrDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 1, 1)
)
traceRcvrFrDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceRcvrIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceRcvrFrIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceRcvrFrDnaIndex"),
)
if mibBuilder.loadTexts:
    traceRcvrFrDnaRowStatusEntry.setStatus("mandatory")
_TraceRcvrFrDnaRowStatus_Type = RowStatus
_TraceRcvrFrDnaRowStatus_Object = MibTableColumn
traceRcvrFrDnaRowStatus = _TraceRcvrFrDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 1, 1, 1),
    _TraceRcvrFrDnaRowStatus_Type()
)
traceRcvrFrDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrDnaRowStatus.setStatus("mandatory")
_TraceRcvrFrDnaComponentName_Type = DisplayString
_TraceRcvrFrDnaComponentName_Object = MibTableColumn
traceRcvrFrDnaComponentName = _TraceRcvrFrDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 1, 1, 2),
    _TraceRcvrFrDnaComponentName_Type()
)
traceRcvrFrDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrDnaComponentName.setStatus("mandatory")
_TraceRcvrFrDnaStorageType_Type = StorageType
_TraceRcvrFrDnaStorageType_Object = MibTableColumn
traceRcvrFrDnaStorageType = _TraceRcvrFrDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 1, 1, 4),
    _TraceRcvrFrDnaStorageType_Type()
)
traceRcvrFrDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrDnaStorageType.setStatus("mandatory")
_TraceRcvrFrDnaIndex_Type = NonReplicated
_TraceRcvrFrDnaIndex_Object = MibTableColumn
traceRcvrFrDnaIndex = _TraceRcvrFrDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 1, 1, 10),
    _TraceRcvrFrDnaIndex_Type()
)
traceRcvrFrDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceRcvrFrDnaIndex.setStatus("mandatory")
_TraceRcvrFrDnaCug_ObjectIdentity = ObjectIdentity
traceRcvrFrDnaCug = _TraceRcvrFrDnaCug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 2)
)
_TraceRcvrFrDnaCugRowStatusTable_Object = MibTable
traceRcvrFrDnaCugRowStatusTable = _TraceRcvrFrDnaCugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    traceRcvrFrDnaCugRowStatusTable.setStatus("mandatory")
_TraceRcvrFrDnaCugRowStatusEntry_Object = MibTableRow
traceRcvrFrDnaCugRowStatusEntry = _TraceRcvrFrDnaCugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 2, 1, 1)
)
traceRcvrFrDnaCugRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceRcvrIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceRcvrFrIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceRcvrFrDnaIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceRcvrFrDnaCugIndex"),
)
if mibBuilder.loadTexts:
    traceRcvrFrDnaCugRowStatusEntry.setStatus("mandatory")
_TraceRcvrFrDnaCugRowStatus_Type = RowStatus
_TraceRcvrFrDnaCugRowStatus_Object = MibTableColumn
traceRcvrFrDnaCugRowStatus = _TraceRcvrFrDnaCugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 2, 1, 1, 1),
    _TraceRcvrFrDnaCugRowStatus_Type()
)
traceRcvrFrDnaCugRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrFrDnaCugRowStatus.setStatus("mandatory")
_TraceRcvrFrDnaCugComponentName_Type = DisplayString
_TraceRcvrFrDnaCugComponentName_Object = MibTableColumn
traceRcvrFrDnaCugComponentName = _TraceRcvrFrDnaCugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 2, 1, 1, 2),
    _TraceRcvrFrDnaCugComponentName_Type()
)
traceRcvrFrDnaCugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrDnaCugComponentName.setStatus("mandatory")
_TraceRcvrFrDnaCugStorageType_Type = StorageType
_TraceRcvrFrDnaCugStorageType_Object = MibTableColumn
traceRcvrFrDnaCugStorageType = _TraceRcvrFrDnaCugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 2, 1, 1, 4),
    _TraceRcvrFrDnaCugStorageType_Type()
)
traceRcvrFrDnaCugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrDnaCugStorageType.setStatus("mandatory")


class _TraceRcvrFrDnaCugIndex_Type(Integer32):
    """Custom type traceRcvrFrDnaCugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_TraceRcvrFrDnaCugIndex_Type.__name__ = "Integer32"
_TraceRcvrFrDnaCugIndex_Object = MibTableColumn
traceRcvrFrDnaCugIndex = _TraceRcvrFrDnaCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 2, 1, 1, 10),
    _TraceRcvrFrDnaCugIndex_Type()
)
traceRcvrFrDnaCugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceRcvrFrDnaCugIndex.setStatus("mandatory")
_TraceRcvrFrDnaCugCugOptionsTable_Object = MibTable
traceRcvrFrDnaCugCugOptionsTable = _TraceRcvrFrDnaCugCugOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 2, 10)
)
if mibBuilder.loadTexts:
    traceRcvrFrDnaCugCugOptionsTable.setStatus("mandatory")
_TraceRcvrFrDnaCugCugOptionsEntry_Object = MibTableRow
traceRcvrFrDnaCugCugOptionsEntry = _TraceRcvrFrDnaCugCugOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 2, 10, 1)
)
traceRcvrFrDnaCugCugOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceRcvrIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceRcvrFrIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceRcvrFrDnaIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceRcvrFrDnaCugIndex"),
)
if mibBuilder.loadTexts:
    traceRcvrFrDnaCugCugOptionsEntry.setStatus("mandatory")


class _TraceRcvrFrDnaCugType_Type(Integer32):
    """Custom type traceRcvrFrDnaCugType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("international", 1),
          ("national", 0))
    )


_TraceRcvrFrDnaCugType_Type.__name__ = "Integer32"
_TraceRcvrFrDnaCugType_Object = MibTableColumn
traceRcvrFrDnaCugType = _TraceRcvrFrDnaCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 2, 10, 1, 1),
    _TraceRcvrFrDnaCugType_Type()
)
traceRcvrFrDnaCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrFrDnaCugType.setStatus("mandatory")


class _TraceRcvrFrDnaCugDnic_Type(DigitString):
    """Custom type traceRcvrFrDnaCugDnic based on DigitString"""
    defaultHexValue = "30303030"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_TraceRcvrFrDnaCugDnic_Type.__name__ = "DigitString"
_TraceRcvrFrDnaCugDnic_Object = MibTableColumn
traceRcvrFrDnaCugDnic = _TraceRcvrFrDnaCugDnic_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 2, 10, 1, 2),
    _TraceRcvrFrDnaCugDnic_Type()
)
traceRcvrFrDnaCugDnic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrFrDnaCugDnic.setStatus("mandatory")


class _TraceRcvrFrDnaCugInterlockCode_Type(Unsigned32):
    """Custom type traceRcvrFrDnaCugInterlockCode based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TraceRcvrFrDnaCugInterlockCode_Type.__name__ = "Unsigned32"
_TraceRcvrFrDnaCugInterlockCode_Object = MibTableColumn
traceRcvrFrDnaCugInterlockCode = _TraceRcvrFrDnaCugInterlockCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 2, 10, 1, 3),
    _TraceRcvrFrDnaCugInterlockCode_Type()
)
traceRcvrFrDnaCugInterlockCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrFrDnaCugInterlockCode.setStatus("mandatory")


class _TraceRcvrFrDnaCugPreferential_Type(Integer32):
    """Custom type traceRcvrFrDnaCugPreferential based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TraceRcvrFrDnaCugPreferential_Type.__name__ = "Integer32"
_TraceRcvrFrDnaCugPreferential_Object = MibTableColumn
traceRcvrFrDnaCugPreferential = _TraceRcvrFrDnaCugPreferential_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 2, 10, 1, 4),
    _TraceRcvrFrDnaCugPreferential_Type()
)
traceRcvrFrDnaCugPreferential.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrDnaCugPreferential.setStatus("mandatory")


class _TraceRcvrFrDnaCugOutCalls_Type(Integer32):
    """Custom type traceRcvrFrDnaCugOutCalls based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_TraceRcvrFrDnaCugOutCalls_Type.__name__ = "Integer32"
_TraceRcvrFrDnaCugOutCalls_Object = MibTableColumn
traceRcvrFrDnaCugOutCalls = _TraceRcvrFrDnaCugOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 2, 10, 1, 5),
    _TraceRcvrFrDnaCugOutCalls_Type()
)
traceRcvrFrDnaCugOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrDnaCugOutCalls.setStatus("mandatory")


class _TraceRcvrFrDnaCugIncCalls_Type(Integer32):
    """Custom type traceRcvrFrDnaCugIncCalls based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_TraceRcvrFrDnaCugIncCalls_Type.__name__ = "Integer32"
_TraceRcvrFrDnaCugIncCalls_Object = MibTableColumn
traceRcvrFrDnaCugIncCalls = _TraceRcvrFrDnaCugIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 2, 10, 1, 6),
    _TraceRcvrFrDnaCugIncCalls_Type()
)
traceRcvrFrDnaCugIncCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrDnaCugIncCalls.setStatus("mandatory")


class _TraceRcvrFrDnaCugPrivileged_Type(Integer32):
    """Custom type traceRcvrFrDnaCugPrivileged based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TraceRcvrFrDnaCugPrivileged_Type.__name__ = "Integer32"
_TraceRcvrFrDnaCugPrivileged_Object = MibTableColumn
traceRcvrFrDnaCugPrivileged = _TraceRcvrFrDnaCugPrivileged_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 2, 10, 1, 7),
    _TraceRcvrFrDnaCugPrivileged_Type()
)
traceRcvrFrDnaCugPrivileged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrDnaCugPrivileged.setStatus("mandatory")
_TraceRcvrFrDnaAddressTable_Object = MibTable
traceRcvrFrDnaAddressTable = _TraceRcvrFrDnaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 10)
)
if mibBuilder.loadTexts:
    traceRcvrFrDnaAddressTable.setStatus("mandatory")
_TraceRcvrFrDnaAddressEntry_Object = MibTableRow
traceRcvrFrDnaAddressEntry = _TraceRcvrFrDnaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 10, 1)
)
traceRcvrFrDnaAddressEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceRcvrIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceRcvrFrIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceRcvrFrDnaIndex"),
)
if mibBuilder.loadTexts:
    traceRcvrFrDnaAddressEntry.setStatus("mandatory")


class _TraceRcvrFrDnaNumberingPlanIndicator_Type(Integer32):
    """Custom type traceRcvrFrDnaNumberingPlanIndicator based on Integer32"""
    defaultValue = 0

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


_TraceRcvrFrDnaNumberingPlanIndicator_Type.__name__ = "Integer32"
_TraceRcvrFrDnaNumberingPlanIndicator_Object = MibTableColumn
traceRcvrFrDnaNumberingPlanIndicator = _TraceRcvrFrDnaNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 10, 1, 1),
    _TraceRcvrFrDnaNumberingPlanIndicator_Type()
)
traceRcvrFrDnaNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrFrDnaNumberingPlanIndicator.setStatus("mandatory")


class _TraceRcvrFrDnaDataNetworkAddress_Type(DigitString):
    """Custom type traceRcvrFrDnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_TraceRcvrFrDnaDataNetworkAddress_Type.__name__ = "DigitString"
_TraceRcvrFrDnaDataNetworkAddress_Object = MibTableColumn
traceRcvrFrDnaDataNetworkAddress = _TraceRcvrFrDnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 10, 1, 2),
    _TraceRcvrFrDnaDataNetworkAddress_Type()
)
traceRcvrFrDnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrFrDnaDataNetworkAddress.setStatus("mandatory")
_TraceRcvrFrDnaOutgoingOptionsTable_Object = MibTable
traceRcvrFrDnaOutgoingOptionsTable = _TraceRcvrFrDnaOutgoingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 11)
)
if mibBuilder.loadTexts:
    traceRcvrFrDnaOutgoingOptionsTable.setStatus("mandatory")
_TraceRcvrFrDnaOutgoingOptionsEntry_Object = MibTableRow
traceRcvrFrDnaOutgoingOptionsEntry = _TraceRcvrFrDnaOutgoingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 11, 1)
)
traceRcvrFrDnaOutgoingOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceRcvrIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceRcvrFrIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceRcvrFrDnaIndex"),
)
if mibBuilder.loadTexts:
    traceRcvrFrDnaOutgoingOptionsEntry.setStatus("mandatory")


class _TraceRcvrFrDnaOutCalls_Type(Integer32):
    """Custom type traceRcvrFrDnaOutCalls based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_TraceRcvrFrDnaOutCalls_Type.__name__ = "Integer32"
_TraceRcvrFrDnaOutCalls_Object = MibTableColumn
traceRcvrFrDnaOutCalls = _TraceRcvrFrDnaOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 11, 1, 1),
    _TraceRcvrFrDnaOutCalls_Type()
)
traceRcvrFrDnaOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrDnaOutCalls.setStatus("mandatory")


class _TraceRcvrFrDnaOutDefaultPriority_Type(Integer32):
    """Custom type traceRcvrFrDnaOutDefaultPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("normal", 0))
    )


_TraceRcvrFrDnaOutDefaultPriority_Type.__name__ = "Integer32"
_TraceRcvrFrDnaOutDefaultPriority_Object = MibTableColumn
traceRcvrFrDnaOutDefaultPriority = _TraceRcvrFrDnaOutDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 11, 1, 7),
    _TraceRcvrFrDnaOutDefaultPriority_Type()
)
traceRcvrFrDnaOutDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrFrDnaOutDefaultPriority.setStatus("mandatory")


class _TraceRcvrFrDnaOutIntl_Type(Integer32):
    """Custom type traceRcvrFrDnaOutIntl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_TraceRcvrFrDnaOutIntl_Type.__name__ = "Integer32"
_TraceRcvrFrDnaOutIntl_Object = MibTableColumn
traceRcvrFrDnaOutIntl = _TraceRcvrFrDnaOutIntl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 11, 1, 8),
    _TraceRcvrFrDnaOutIntl_Type()
)
traceRcvrFrDnaOutIntl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrDnaOutIntl.setStatus("mandatory")


class _TraceRcvrFrDnaOutDefaultPathReliability_Type(Integer32):
    """Custom type traceRcvrFrDnaOutDefaultPathReliability based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 0),
          ("normal", 1))
    )


_TraceRcvrFrDnaOutDefaultPathReliability_Type.__name__ = "Integer32"
_TraceRcvrFrDnaOutDefaultPathReliability_Object = MibTableColumn
traceRcvrFrDnaOutDefaultPathReliability = _TraceRcvrFrDnaOutDefaultPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 11, 1, 14),
    _TraceRcvrFrDnaOutDefaultPathReliability_Type()
)
traceRcvrFrDnaOutDefaultPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrDnaOutDefaultPathReliability.setStatus("mandatory")


class _TraceRcvrFrDnaOutPathReliabilityOverRide_Type(Integer32):
    """Custom type traceRcvrFrDnaOutPathReliabilityOverRide based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TraceRcvrFrDnaOutPathReliabilityOverRide_Type.__name__ = "Integer32"
_TraceRcvrFrDnaOutPathReliabilityOverRide_Object = MibTableColumn
traceRcvrFrDnaOutPathReliabilityOverRide = _TraceRcvrFrDnaOutPathReliabilityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 11, 1, 15),
    _TraceRcvrFrDnaOutPathReliabilityOverRide_Type()
)
traceRcvrFrDnaOutPathReliabilityOverRide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrDnaOutPathReliabilityOverRide.setStatus("mandatory")


class _TraceRcvrFrDnaOutPathReliabilitySignal_Type(Integer32):
    """Custom type traceRcvrFrDnaOutPathReliabilitySignal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_TraceRcvrFrDnaOutPathReliabilitySignal_Type.__name__ = "Integer32"
_TraceRcvrFrDnaOutPathReliabilitySignal_Object = MibTableColumn
traceRcvrFrDnaOutPathReliabilitySignal = _TraceRcvrFrDnaOutPathReliabilitySignal_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 11, 1, 16),
    _TraceRcvrFrDnaOutPathReliabilitySignal_Type()
)
traceRcvrFrDnaOutPathReliabilitySignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrDnaOutPathReliabilitySignal.setStatus("mandatory")


class _TraceRcvrFrDnaOutAccess_Type(Integer32):
    """Custom type traceRcvrFrDnaOutAccess based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_TraceRcvrFrDnaOutAccess_Type.__name__ = "Integer32"
_TraceRcvrFrDnaOutAccess_Object = MibTableColumn
traceRcvrFrDnaOutAccess = _TraceRcvrFrDnaOutAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 11, 1, 17),
    _TraceRcvrFrDnaOutAccess_Type()
)
traceRcvrFrDnaOutAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrFrDnaOutAccess.setStatus("mandatory")
_TraceRcvrFrDnaIncomingOptionsTable_Object = MibTable
traceRcvrFrDnaIncomingOptionsTable = _TraceRcvrFrDnaIncomingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 12)
)
if mibBuilder.loadTexts:
    traceRcvrFrDnaIncomingOptionsTable.setStatus("mandatory")
_TraceRcvrFrDnaIncomingOptionsEntry_Object = MibTableRow
traceRcvrFrDnaIncomingOptionsEntry = _TraceRcvrFrDnaIncomingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 12, 1)
)
traceRcvrFrDnaIncomingOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceRcvrIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceRcvrFrIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceRcvrFrDnaIndex"),
)
if mibBuilder.loadTexts:
    traceRcvrFrDnaIncomingOptionsEntry.setStatus("mandatory")


class _TraceRcvrFrDnaIncCalls_Type(Integer32):
    """Custom type traceRcvrFrDnaIncCalls based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_TraceRcvrFrDnaIncCalls_Type.__name__ = "Integer32"
_TraceRcvrFrDnaIncCalls_Object = MibTableColumn
traceRcvrFrDnaIncCalls = _TraceRcvrFrDnaIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 12, 1, 1),
    _TraceRcvrFrDnaIncCalls_Type()
)
traceRcvrFrDnaIncCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrDnaIncCalls.setStatus("mandatory")
_TraceRcvrFrDnaCallOptionsTable_Object = MibTable
traceRcvrFrDnaCallOptionsTable = _TraceRcvrFrDnaCallOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 13)
)
if mibBuilder.loadTexts:
    traceRcvrFrDnaCallOptionsTable.setStatus("mandatory")
_TraceRcvrFrDnaCallOptionsEntry_Object = MibTableRow
traceRcvrFrDnaCallOptionsEntry = _TraceRcvrFrDnaCallOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 13, 1)
)
traceRcvrFrDnaCallOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceRcvrIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceRcvrFrIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceRcvrFrDnaIndex"),
)
if mibBuilder.loadTexts:
    traceRcvrFrDnaCallOptionsEntry.setStatus("mandatory")


class _TraceRcvrFrDnaPacketSizes_Type(OctetString):
    """Custom type traceRcvrFrDnaPacketSizes based on OctetString"""
    defaultHexValue = "0100"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_TraceRcvrFrDnaPacketSizes_Type.__name__ = "OctetString"
_TraceRcvrFrDnaPacketSizes_Object = MibTableColumn
traceRcvrFrDnaPacketSizes = _TraceRcvrFrDnaPacketSizes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 13, 1, 2),
    _TraceRcvrFrDnaPacketSizes_Type()
)
traceRcvrFrDnaPacketSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrDnaPacketSizes.setStatus("mandatory")


class _TraceRcvrFrDnaDefaultRecvFrmNetworkPacketSize_Type(Integer32):
    """Custom type traceRcvrFrDnaDefaultRecvFrmNetworkPacketSize based on Integer32"""
    defaultValue = 11

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("n1024", 10),
          ("n128", 7),
          ("n16", 4),
          ("n2048", 11),
          ("n256", 8),
          ("n32", 5),
          ("n4096", 12),
          ("n512", 9),
          ("n64", 6))
    )


_TraceRcvrFrDnaDefaultRecvFrmNetworkPacketSize_Type.__name__ = "Integer32"
_TraceRcvrFrDnaDefaultRecvFrmNetworkPacketSize_Object = MibTableColumn
traceRcvrFrDnaDefaultRecvFrmNetworkPacketSize = _TraceRcvrFrDnaDefaultRecvFrmNetworkPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 13, 1, 3),
    _TraceRcvrFrDnaDefaultRecvFrmNetworkPacketSize_Type()
)
traceRcvrFrDnaDefaultRecvFrmNetworkPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrDnaDefaultRecvFrmNetworkPacketSize.setStatus("mandatory")


class _TraceRcvrFrDnaDefaultSendToNetworkPacketSize_Type(Integer32):
    """Custom type traceRcvrFrDnaDefaultSendToNetworkPacketSize based on Integer32"""
    defaultValue = 11

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("n1024", 10),
          ("n128", 7),
          ("n16", 4),
          ("n2048", 11),
          ("n256", 8),
          ("n32", 5),
          ("n4096", 12),
          ("n512", 9),
          ("n64", 6))
    )


_TraceRcvrFrDnaDefaultSendToNetworkPacketSize_Type.__name__ = "Integer32"
_TraceRcvrFrDnaDefaultSendToNetworkPacketSize_Object = MibTableColumn
traceRcvrFrDnaDefaultSendToNetworkPacketSize = _TraceRcvrFrDnaDefaultSendToNetworkPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 13, 1, 4),
    _TraceRcvrFrDnaDefaultSendToNetworkPacketSize_Type()
)
traceRcvrFrDnaDefaultSendToNetworkPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrDnaDefaultSendToNetworkPacketSize.setStatus("mandatory")


class _TraceRcvrFrDnaCugFormat_Type(Integer32):
    """Custom type traceRcvrFrDnaCugFormat based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("basic", 0),
          ("extended", 1))
    )


_TraceRcvrFrDnaCugFormat_Type.__name__ = "Integer32"
_TraceRcvrFrDnaCugFormat_Object = MibTableColumn
traceRcvrFrDnaCugFormat = _TraceRcvrFrDnaCugFormat_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 2, 13, 1, 10),
    _TraceRcvrFrDnaCugFormat_Type()
)
traceRcvrFrDnaCugFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrDnaCugFormat.setStatus("mandatory")
_TraceRcvrFrDc_ObjectIdentity = ObjectIdentity
traceRcvrFrDc = _TraceRcvrFrDc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 3)
)
_TraceRcvrFrDcRowStatusTable_Object = MibTable
traceRcvrFrDcRowStatusTable = _TraceRcvrFrDcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    traceRcvrFrDcRowStatusTable.setStatus("mandatory")
_TraceRcvrFrDcRowStatusEntry_Object = MibTableRow
traceRcvrFrDcRowStatusEntry = _TraceRcvrFrDcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 3, 1, 1)
)
traceRcvrFrDcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceRcvrIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceRcvrFrIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceRcvrFrDcIndex"),
)
if mibBuilder.loadTexts:
    traceRcvrFrDcRowStatusEntry.setStatus("mandatory")
_TraceRcvrFrDcRowStatus_Type = RowStatus
_TraceRcvrFrDcRowStatus_Object = MibTableColumn
traceRcvrFrDcRowStatus = _TraceRcvrFrDcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 3, 1, 1, 1),
    _TraceRcvrFrDcRowStatus_Type()
)
traceRcvrFrDcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrDcRowStatus.setStatus("mandatory")
_TraceRcvrFrDcComponentName_Type = DisplayString
_TraceRcvrFrDcComponentName_Object = MibTableColumn
traceRcvrFrDcComponentName = _TraceRcvrFrDcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 3, 1, 1, 2),
    _TraceRcvrFrDcComponentName_Type()
)
traceRcvrFrDcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrDcComponentName.setStatus("mandatory")
_TraceRcvrFrDcStorageType_Type = StorageType
_TraceRcvrFrDcStorageType_Object = MibTableColumn
traceRcvrFrDcStorageType = _TraceRcvrFrDcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 3, 1, 1, 4),
    _TraceRcvrFrDcStorageType_Type()
)
traceRcvrFrDcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrDcStorageType.setStatus("mandatory")
_TraceRcvrFrDcIndex_Type = NonReplicated
_TraceRcvrFrDcIndex_Object = MibTableColumn
traceRcvrFrDcIndex = _TraceRcvrFrDcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 3, 1, 1, 10),
    _TraceRcvrFrDcIndex_Type()
)
traceRcvrFrDcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceRcvrFrDcIndex.setStatus("mandatory")
_TraceRcvrFrDcOptionsTable_Object = MibTable
traceRcvrFrDcOptionsTable = _TraceRcvrFrDcOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 3, 10)
)
if mibBuilder.loadTexts:
    traceRcvrFrDcOptionsTable.setStatus("mandatory")
_TraceRcvrFrDcOptionsEntry_Object = MibTableRow
traceRcvrFrDcOptionsEntry = _TraceRcvrFrDcOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 3, 10, 1)
)
traceRcvrFrDcOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceRcvrIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceRcvrFrIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceRcvrFrDcIndex"),
)
if mibBuilder.loadTexts:
    traceRcvrFrDcOptionsEntry.setStatus("mandatory")


class _TraceRcvrFrDcRemoteNpi_Type(Integer32):
    """Custom type traceRcvrFrDcRemoteNpi based on Integer32"""
    defaultValue = 0

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


_TraceRcvrFrDcRemoteNpi_Type.__name__ = "Integer32"
_TraceRcvrFrDcRemoteNpi_Object = MibTableColumn
traceRcvrFrDcRemoteNpi = _TraceRcvrFrDcRemoteNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 3, 10, 1, 3),
    _TraceRcvrFrDcRemoteNpi_Type()
)
traceRcvrFrDcRemoteNpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrFrDcRemoteNpi.setStatus("mandatory")


class _TraceRcvrFrDcRemoteDna_Type(DigitString):
    """Custom type traceRcvrFrDcRemoteDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_TraceRcvrFrDcRemoteDna_Type.__name__ = "DigitString"
_TraceRcvrFrDcRemoteDna_Object = MibTableColumn
traceRcvrFrDcRemoteDna = _TraceRcvrFrDcRemoteDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 3, 10, 1, 4),
    _TraceRcvrFrDcRemoteDna_Type()
)
traceRcvrFrDcRemoteDna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrFrDcRemoteDna.setStatus("mandatory")


class _TraceRcvrFrDcType_Type(Integer32):
    """Custom type traceRcvrFrDcType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("permanentBackupSlave", 3),
          ("permanentMaster", 1),
          ("permanentSlave", 2),
          ("switched", 0))
    )


_TraceRcvrFrDcType_Type.__name__ = "Integer32"
_TraceRcvrFrDcType_Object = MibTableColumn
traceRcvrFrDcType = _TraceRcvrFrDcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 3, 10, 1, 6),
    _TraceRcvrFrDcType_Type()
)
traceRcvrFrDcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrFrDcType.setStatus("mandatory")


class _TraceRcvrFrDcUserData_Type(HexString):
    """Custom type traceRcvrFrDcUserData based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TraceRcvrFrDcUserData_Type.__name__ = "HexString"
_TraceRcvrFrDcUserData_Object = MibTableColumn
traceRcvrFrDcUserData = _TraceRcvrFrDcUserData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 3, 3, 10, 1, 8),
    _TraceRcvrFrDcUserData_Type()
)
traceRcvrFrDcUserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrFrDcUserData.setStatus("mandatory")
_TraceSessionFr_ObjectIdentity = ObjectIdentity
traceSessionFr = _TraceSessionFr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3)
)
_TraceSessionFrRowStatusTable_Object = MibTable
traceSessionFrRowStatusTable = _TraceSessionFrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 1)
)
if mibBuilder.loadTexts:
    traceSessionFrRowStatusTable.setStatus("mandatory")
_TraceSessionFrRowStatusEntry_Object = MibTableRow
traceSessionFrRowStatusEntry = _TraceSessionFrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 1, 1)
)
traceSessionFrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceSessionIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceSessionFrIndex"),
)
if mibBuilder.loadTexts:
    traceSessionFrRowStatusEntry.setStatus("mandatory")
_TraceSessionFrRowStatus_Type = RowStatus
_TraceSessionFrRowStatus_Object = MibTableColumn
traceSessionFrRowStatus = _TraceSessionFrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 1, 1, 1),
    _TraceSessionFrRowStatus_Type()
)
traceSessionFrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrRowStatus.setStatus("mandatory")
_TraceSessionFrComponentName_Type = DisplayString
_TraceSessionFrComponentName_Object = MibTableColumn
traceSessionFrComponentName = _TraceSessionFrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 1, 1, 2),
    _TraceSessionFrComponentName_Type()
)
traceSessionFrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrComponentName.setStatus("mandatory")
_TraceSessionFrStorageType_Type = StorageType
_TraceSessionFrStorageType_Object = MibTableColumn
traceSessionFrStorageType = _TraceSessionFrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 1, 1, 4),
    _TraceSessionFrStorageType_Type()
)
traceSessionFrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrStorageType.setStatus("mandatory")
_TraceSessionFrIndex_Type = NonReplicated
_TraceSessionFrIndex_Object = MibTableColumn
traceSessionFrIndex = _TraceSessionFrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 1, 1, 10),
    _TraceSessionFrIndex_Type()
)
traceSessionFrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceSessionFrIndex.setStatus("mandatory")
_TraceSessionFrVc_ObjectIdentity = ObjectIdentity
traceSessionFrVc = _TraceSessionFrVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2)
)
_TraceSessionFrVcRowStatusTable_Object = MibTable
traceSessionFrVcRowStatusTable = _TraceSessionFrVcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    traceSessionFrVcRowStatusTable.setStatus("mandatory")
_TraceSessionFrVcRowStatusEntry_Object = MibTableRow
traceSessionFrVcRowStatusEntry = _TraceSessionFrVcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 1, 1)
)
traceSessionFrVcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceSessionIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceSessionFrIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceSessionFrVcIndex"),
)
if mibBuilder.loadTexts:
    traceSessionFrVcRowStatusEntry.setStatus("mandatory")
_TraceSessionFrVcRowStatus_Type = RowStatus
_TraceSessionFrVcRowStatus_Object = MibTableColumn
traceSessionFrVcRowStatus = _TraceSessionFrVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 1, 1, 1),
    _TraceSessionFrVcRowStatus_Type()
)
traceSessionFrVcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcRowStatus.setStatus("mandatory")
_TraceSessionFrVcComponentName_Type = DisplayString
_TraceSessionFrVcComponentName_Object = MibTableColumn
traceSessionFrVcComponentName = _TraceSessionFrVcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 1, 1, 2),
    _TraceSessionFrVcComponentName_Type()
)
traceSessionFrVcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcComponentName.setStatus("mandatory")
_TraceSessionFrVcStorageType_Type = StorageType
_TraceSessionFrVcStorageType_Object = MibTableColumn
traceSessionFrVcStorageType = _TraceSessionFrVcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 1, 1, 4),
    _TraceSessionFrVcStorageType_Type()
)
traceSessionFrVcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcStorageType.setStatus("mandatory")
_TraceSessionFrVcIndex_Type = NonReplicated
_TraceSessionFrVcIndex_Object = MibTableColumn
traceSessionFrVcIndex = _TraceSessionFrVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 1, 1, 10),
    _TraceSessionFrVcIndex_Type()
)
traceSessionFrVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceSessionFrVcIndex.setStatus("mandatory")
_TraceSessionFrVcCadTable_Object = MibTable
traceSessionFrVcCadTable = _TraceSessionFrVcCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10)
)
if mibBuilder.loadTexts:
    traceSessionFrVcCadTable.setStatus("mandatory")
_TraceSessionFrVcCadEntry_Object = MibTableRow
traceSessionFrVcCadEntry = _TraceSessionFrVcCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10, 1)
)
traceSessionFrVcCadEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceSessionIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceSessionFrIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceSessionFrVcIndex"),
)
if mibBuilder.loadTexts:
    traceSessionFrVcCadEntry.setStatus("mandatory")


class _TraceSessionFrVcType_Type(Integer32):
    """Custom type traceSessionFrVcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("spvc", 2),
          ("svc", 0))
    )


_TraceSessionFrVcType_Type.__name__ = "Integer32"
_TraceSessionFrVcType_Object = MibTableColumn
traceSessionFrVcType = _TraceSessionFrVcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10, 1, 1),
    _TraceSessionFrVcType_Type()
)
traceSessionFrVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcType.setStatus("mandatory")


class _TraceSessionFrVcState_Type(Integer32):
    """Custom type traceSessionFrVcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("creating", 0),
          ("dataTransferP4", 4),
          ("dceClearIndicationP7", 7),
          ("dceWaitingP3", 3),
          ("dteClearRequestP6", 6),
          ("dteWaitingP2", 2),
          ("readyP1", 1),
          ("termination", 8),
          ("unsupportedP5", 5))
    )


_TraceSessionFrVcState_Type.__name__ = "Integer32"
_TraceSessionFrVcState_Object = MibTableColumn
traceSessionFrVcState = _TraceSessionFrVcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10, 1, 2),
    _TraceSessionFrVcState_Type()
)
traceSessionFrVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcState.setStatus("mandatory")


class _TraceSessionFrVcPreviousState_Type(Integer32):
    """Custom type traceSessionFrVcPreviousState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("creating", 0),
          ("dataTransferP4", 4),
          ("dceClearIndicationP7", 7),
          ("dceWaitingP3", 3),
          ("dteClearRequestP6", 6),
          ("dteWaitingP2", 2),
          ("readyP1", 1),
          ("termination", 8),
          ("unsupportedP5", 5))
    )


_TraceSessionFrVcPreviousState_Type.__name__ = "Integer32"
_TraceSessionFrVcPreviousState_Object = MibTableColumn
traceSessionFrVcPreviousState = _TraceSessionFrVcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10, 1, 3),
    _TraceSessionFrVcPreviousState_Type()
)
traceSessionFrVcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcPreviousState.setStatus("mandatory")


class _TraceSessionFrVcDiagnosticCode_Type(Unsigned32):
    """Custom type traceSessionFrVcDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TraceSessionFrVcDiagnosticCode_Type.__name__ = "Unsigned32"
_TraceSessionFrVcDiagnosticCode_Object = MibTableColumn
traceSessionFrVcDiagnosticCode = _TraceSessionFrVcDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10, 1, 4),
    _TraceSessionFrVcDiagnosticCode_Type()
)
traceSessionFrVcDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcDiagnosticCode.setStatus("mandatory")


class _TraceSessionFrVcPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type traceSessionFrVcPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TraceSessionFrVcPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_TraceSessionFrVcPreviousDiagnosticCode_Object = MibTableColumn
traceSessionFrVcPreviousDiagnosticCode = _TraceSessionFrVcPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10, 1, 5),
    _TraceSessionFrVcPreviousDiagnosticCode_Type()
)
traceSessionFrVcPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcPreviousDiagnosticCode.setStatus("mandatory")


class _TraceSessionFrVcCalledNpi_Type(Integer32):
    """Custom type traceSessionFrVcCalledNpi based on Integer32"""
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


_TraceSessionFrVcCalledNpi_Type.__name__ = "Integer32"
_TraceSessionFrVcCalledNpi_Object = MibTableColumn
traceSessionFrVcCalledNpi = _TraceSessionFrVcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10, 1, 6),
    _TraceSessionFrVcCalledNpi_Type()
)
traceSessionFrVcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcCalledNpi.setStatus("mandatory")


class _TraceSessionFrVcCalledDna_Type(DigitString):
    """Custom type traceSessionFrVcCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_TraceSessionFrVcCalledDna_Type.__name__ = "DigitString"
_TraceSessionFrVcCalledDna_Object = MibTableColumn
traceSessionFrVcCalledDna = _TraceSessionFrVcCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10, 1, 7),
    _TraceSessionFrVcCalledDna_Type()
)
traceSessionFrVcCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcCalledDna.setStatus("mandatory")


class _TraceSessionFrVcCalledLcn_Type(Unsigned32):
    """Custom type traceSessionFrVcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TraceSessionFrVcCalledLcn_Type.__name__ = "Unsigned32"
_TraceSessionFrVcCalledLcn_Object = MibTableColumn
traceSessionFrVcCalledLcn = _TraceSessionFrVcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10, 1, 8),
    _TraceSessionFrVcCalledLcn_Type()
)
traceSessionFrVcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcCalledLcn.setStatus("mandatory")


class _TraceSessionFrVcCallingNpi_Type(Integer32):
    """Custom type traceSessionFrVcCallingNpi based on Integer32"""
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


_TraceSessionFrVcCallingNpi_Type.__name__ = "Integer32"
_TraceSessionFrVcCallingNpi_Object = MibTableColumn
traceSessionFrVcCallingNpi = _TraceSessionFrVcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10, 1, 9),
    _TraceSessionFrVcCallingNpi_Type()
)
traceSessionFrVcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcCallingNpi.setStatus("mandatory")


class _TraceSessionFrVcCallingDna_Type(DigitString):
    """Custom type traceSessionFrVcCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_TraceSessionFrVcCallingDna_Type.__name__ = "DigitString"
_TraceSessionFrVcCallingDna_Object = MibTableColumn
traceSessionFrVcCallingDna = _TraceSessionFrVcCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10, 1, 10),
    _TraceSessionFrVcCallingDna_Type()
)
traceSessionFrVcCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcCallingDna.setStatus("mandatory")


class _TraceSessionFrVcCallingLcn_Type(Unsigned32):
    """Custom type traceSessionFrVcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TraceSessionFrVcCallingLcn_Type.__name__ = "Unsigned32"
_TraceSessionFrVcCallingLcn_Object = MibTableColumn
traceSessionFrVcCallingLcn = _TraceSessionFrVcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10, 1, 11),
    _TraceSessionFrVcCallingLcn_Type()
)
traceSessionFrVcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcCallingLcn.setStatus("mandatory")


class _TraceSessionFrVcAccountingEnabled_Type(Integer32):
    """Custom type traceSessionFrVcAccountingEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 0))
    )


_TraceSessionFrVcAccountingEnabled_Type.__name__ = "Integer32"
_TraceSessionFrVcAccountingEnabled_Object = MibTableColumn
traceSessionFrVcAccountingEnabled = _TraceSessionFrVcAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10, 1, 12),
    _TraceSessionFrVcAccountingEnabled_Type()
)
traceSessionFrVcAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcAccountingEnabled.setStatus("mandatory")


class _TraceSessionFrVcFastSelectCall_Type(Integer32):
    """Custom type traceSessionFrVcFastSelectCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TraceSessionFrVcFastSelectCall_Type.__name__ = "Integer32"
_TraceSessionFrVcFastSelectCall_Object = MibTableColumn
traceSessionFrVcFastSelectCall = _TraceSessionFrVcFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10, 1, 13),
    _TraceSessionFrVcFastSelectCall_Type()
)
traceSessionFrVcFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcFastSelectCall.setStatus("mandatory")


class _TraceSessionFrVcPathReliability_Type(Integer32):
    """Custom type traceSessionFrVcPathReliability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 0),
          ("normal", 1))
    )


_TraceSessionFrVcPathReliability_Type.__name__ = "Integer32"
_TraceSessionFrVcPathReliability_Object = MibTableColumn
traceSessionFrVcPathReliability = _TraceSessionFrVcPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10, 1, 19),
    _TraceSessionFrVcPathReliability_Type()
)
traceSessionFrVcPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcPathReliability.setStatus("mandatory")


class _TraceSessionFrVcAccountingEnd_Type(Integer32):
    """Custom type traceSessionFrVcAccountingEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("calledEnd", 1),
          ("callingEnd", 0))
    )


_TraceSessionFrVcAccountingEnd_Type.__name__ = "Integer32"
_TraceSessionFrVcAccountingEnd_Object = MibTableColumn
traceSessionFrVcAccountingEnd = _TraceSessionFrVcAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10, 1, 20),
    _TraceSessionFrVcAccountingEnd_Type()
)
traceSessionFrVcAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcAccountingEnd.setStatus("mandatory")


class _TraceSessionFrVcPriority_Type(Integer32):
    """Custom type traceSessionFrVcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("normal", 0))
    )


_TraceSessionFrVcPriority_Type.__name__ = "Integer32"
_TraceSessionFrVcPriority_Object = MibTableColumn
traceSessionFrVcPriority = _TraceSessionFrVcPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10, 1, 21),
    _TraceSessionFrVcPriority_Type()
)
traceSessionFrVcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcPriority.setStatus("mandatory")


class _TraceSessionFrVcSegmentSize_Type(Unsigned32):
    """Custom type traceSessionFrVcSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TraceSessionFrVcSegmentSize_Type.__name__ = "Unsigned32"
_TraceSessionFrVcSegmentSize_Object = MibTableColumn
traceSessionFrVcSegmentSize = _TraceSessionFrVcSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10, 1, 22),
    _TraceSessionFrVcSegmentSize_Type()
)
traceSessionFrVcSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcSegmentSize.setStatus("mandatory")


class _TraceSessionFrVcMaxSubnetPktSize_Type(Unsigned32):
    """Custom type traceSessionFrVcMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TraceSessionFrVcMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_TraceSessionFrVcMaxSubnetPktSize_Object = MibTableColumn
traceSessionFrVcMaxSubnetPktSize = _TraceSessionFrVcMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10, 1, 27),
    _TraceSessionFrVcMaxSubnetPktSize_Type()
)
traceSessionFrVcMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcMaxSubnetPktSize.setStatus("mandatory")


class _TraceSessionFrVcRcosToNetwork_Type(Integer32):
    """Custom type traceSessionFrVcRcosToNetwork based on Integer32"""
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


_TraceSessionFrVcRcosToNetwork_Type.__name__ = "Integer32"
_TraceSessionFrVcRcosToNetwork_Object = MibTableColumn
traceSessionFrVcRcosToNetwork = _TraceSessionFrVcRcosToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10, 1, 28),
    _TraceSessionFrVcRcosToNetwork_Type()
)
traceSessionFrVcRcosToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcRcosToNetwork.setStatus("mandatory")


class _TraceSessionFrVcRcosFromNetwork_Type(Integer32):
    """Custom type traceSessionFrVcRcosFromNetwork based on Integer32"""
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


_TraceSessionFrVcRcosFromNetwork_Type.__name__ = "Integer32"
_TraceSessionFrVcRcosFromNetwork_Object = MibTableColumn
traceSessionFrVcRcosFromNetwork = _TraceSessionFrVcRcosFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10, 1, 29),
    _TraceSessionFrVcRcosFromNetwork_Type()
)
traceSessionFrVcRcosFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcRcosFromNetwork.setStatus("mandatory")


class _TraceSessionFrVcEmissionPriorityToNetwork_Type(Integer32):
    """Custom type traceSessionFrVcEmissionPriorityToNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("interrupting", 2),
          ("normal", 0))
    )


_TraceSessionFrVcEmissionPriorityToNetwork_Type.__name__ = "Integer32"
_TraceSessionFrVcEmissionPriorityToNetwork_Object = MibTableColumn
traceSessionFrVcEmissionPriorityToNetwork = _TraceSessionFrVcEmissionPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10, 1, 30),
    _TraceSessionFrVcEmissionPriorityToNetwork_Type()
)
traceSessionFrVcEmissionPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcEmissionPriorityToNetwork.setStatus("mandatory")


class _TraceSessionFrVcEmissionPriorityFromNetwork_Type(Integer32):
    """Custom type traceSessionFrVcEmissionPriorityFromNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("interrupting", 2),
          ("normal", 0))
    )


_TraceSessionFrVcEmissionPriorityFromNetwork_Type.__name__ = "Integer32"
_TraceSessionFrVcEmissionPriorityFromNetwork_Object = MibTableColumn
traceSessionFrVcEmissionPriorityFromNetwork = _TraceSessionFrVcEmissionPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10, 1, 31),
    _TraceSessionFrVcEmissionPriorityFromNetwork_Type()
)
traceSessionFrVcEmissionPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcEmissionPriorityFromNetwork.setStatus("mandatory")


class _TraceSessionFrVcDataPath_Type(AsciiString):
    """Custom type traceSessionFrVcDataPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TraceSessionFrVcDataPath_Type.__name__ = "AsciiString"
_TraceSessionFrVcDataPath_Object = MibTableColumn
traceSessionFrVcDataPath = _TraceSessionFrVcDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 10, 1, 32),
    _TraceSessionFrVcDataPath_Type()
)
traceSessionFrVcDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcDataPath.setStatus("mandatory")
_TraceSessionFrVcIntdTable_Object = MibTable
traceSessionFrVcIntdTable = _TraceSessionFrVcIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 11)
)
if mibBuilder.loadTexts:
    traceSessionFrVcIntdTable.setStatus("mandatory")
_TraceSessionFrVcIntdEntry_Object = MibTableRow
traceSessionFrVcIntdEntry = _TraceSessionFrVcIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 11, 1)
)
traceSessionFrVcIntdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceSessionIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceSessionFrIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceSessionFrVcIndex"),
)
if mibBuilder.loadTexts:
    traceSessionFrVcIntdEntry.setStatus("mandatory")


class _TraceSessionFrVcCallReferenceNumber_Type(Hex):
    """Custom type traceSessionFrVcCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TraceSessionFrVcCallReferenceNumber_Type.__name__ = "Hex"
_TraceSessionFrVcCallReferenceNumber_Object = MibTableColumn
traceSessionFrVcCallReferenceNumber = _TraceSessionFrVcCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 11, 1, 1),
    _TraceSessionFrVcCallReferenceNumber_Type()
)
traceSessionFrVcCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcCallReferenceNumber.setStatus("mandatory")


class _TraceSessionFrVcElapsedTimeTillNow_Type(Unsigned32):
    """Custom type traceSessionFrVcElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TraceSessionFrVcElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_TraceSessionFrVcElapsedTimeTillNow_Object = MibTableColumn
traceSessionFrVcElapsedTimeTillNow = _TraceSessionFrVcElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 11, 1, 2),
    _TraceSessionFrVcElapsedTimeTillNow_Type()
)
traceSessionFrVcElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcElapsedTimeTillNow.setStatus("mandatory")


class _TraceSessionFrVcSegmentsRx_Type(Unsigned32):
    """Custom type traceSessionFrVcSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TraceSessionFrVcSegmentsRx_Type.__name__ = "Unsigned32"
_TraceSessionFrVcSegmentsRx_Object = MibTableColumn
traceSessionFrVcSegmentsRx = _TraceSessionFrVcSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 11, 1, 3),
    _TraceSessionFrVcSegmentsRx_Type()
)
traceSessionFrVcSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcSegmentsRx.setStatus("mandatory")


class _TraceSessionFrVcSegmentsSent_Type(Unsigned32):
    """Custom type traceSessionFrVcSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TraceSessionFrVcSegmentsSent_Type.__name__ = "Unsigned32"
_TraceSessionFrVcSegmentsSent_Object = MibTableColumn
traceSessionFrVcSegmentsSent = _TraceSessionFrVcSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 11, 1, 4),
    _TraceSessionFrVcSegmentsSent_Type()
)
traceSessionFrVcSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcSegmentsSent.setStatus("mandatory")


class _TraceSessionFrVcStartTime_Type(EnterpriseDateAndTime):
    """Custom type traceSessionFrVcStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_TraceSessionFrVcStartTime_Type.__name__ = "EnterpriseDateAndTime"
_TraceSessionFrVcStartTime_Object = MibTableColumn
traceSessionFrVcStartTime = _TraceSessionFrVcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 11, 1, 5),
    _TraceSessionFrVcStartTime_Type()
)
traceSessionFrVcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcStartTime.setStatus("mandatory")
_TraceSessionFrVcFrdTable_Object = MibTable
traceSessionFrVcFrdTable = _TraceSessionFrVcFrdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 12)
)
if mibBuilder.loadTexts:
    traceSessionFrVcFrdTable.setStatus("mandatory")
_TraceSessionFrVcFrdEntry_Object = MibTableRow
traceSessionFrVcFrdEntry = _TraceSessionFrVcFrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 12, 1)
)
traceSessionFrVcFrdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceSessionIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceSessionFrIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceSessionFrVcIndex"),
)
if mibBuilder.loadTexts:
    traceSessionFrVcFrdEntry.setStatus("mandatory")


class _TraceSessionFrVcFrmCongestedToSubnet_Type(Unsigned32):
    """Custom type traceSessionFrVcFrmCongestedToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionFrVcFrmCongestedToSubnet_Type.__name__ = "Unsigned32"
_TraceSessionFrVcFrmCongestedToSubnet_Object = MibTableColumn
traceSessionFrVcFrmCongestedToSubnet = _TraceSessionFrVcFrmCongestedToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 12, 1, 2),
    _TraceSessionFrVcFrmCongestedToSubnet_Type()
)
traceSessionFrVcFrmCongestedToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcFrmCongestedToSubnet.setStatus("mandatory")


class _TraceSessionFrVcCannotForwardToSubnet_Type(Unsigned32):
    """Custom type traceSessionFrVcCannotForwardToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionFrVcCannotForwardToSubnet_Type.__name__ = "Unsigned32"
_TraceSessionFrVcCannotForwardToSubnet_Object = MibTableColumn
traceSessionFrVcCannotForwardToSubnet = _TraceSessionFrVcCannotForwardToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 12, 1, 3),
    _TraceSessionFrVcCannotForwardToSubnet_Type()
)
traceSessionFrVcCannotForwardToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcCannotForwardToSubnet.setStatus("mandatory")


class _TraceSessionFrVcNotDataXferToSubnet_Type(Unsigned32):
    """Custom type traceSessionFrVcNotDataXferToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionFrVcNotDataXferToSubnet_Type.__name__ = "Unsigned32"
_TraceSessionFrVcNotDataXferToSubnet_Object = MibTableColumn
traceSessionFrVcNotDataXferToSubnet = _TraceSessionFrVcNotDataXferToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 12, 1, 4),
    _TraceSessionFrVcNotDataXferToSubnet_Type()
)
traceSessionFrVcNotDataXferToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcNotDataXferToSubnet.setStatus("mandatory")


class _TraceSessionFrVcOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type traceSessionFrVcOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionFrVcOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_TraceSessionFrVcOutOfRangeFrmFromSubnet_Object = MibTableColumn
traceSessionFrVcOutOfRangeFrmFromSubnet = _TraceSessionFrVcOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 12, 1, 5),
    _TraceSessionFrVcOutOfRangeFrmFromSubnet_Type()
)
traceSessionFrVcOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _TraceSessionFrVcCombErrorsFromSubnet_Type(Unsigned32):
    """Custom type traceSessionFrVcCombErrorsFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionFrVcCombErrorsFromSubnet_Type.__name__ = "Unsigned32"
_TraceSessionFrVcCombErrorsFromSubnet_Object = MibTableColumn
traceSessionFrVcCombErrorsFromSubnet = _TraceSessionFrVcCombErrorsFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 12, 1, 6),
    _TraceSessionFrVcCombErrorsFromSubnet_Type()
)
traceSessionFrVcCombErrorsFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcCombErrorsFromSubnet.setStatus("mandatory")


class _TraceSessionFrVcDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type traceSessionFrVcDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionFrVcDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_TraceSessionFrVcDuplicatesFromSubnet_Object = MibTableColumn
traceSessionFrVcDuplicatesFromSubnet = _TraceSessionFrVcDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 12, 1, 7),
    _TraceSessionFrVcDuplicatesFromSubnet_Type()
)
traceSessionFrVcDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcDuplicatesFromSubnet.setStatus("mandatory")


class _TraceSessionFrVcNotDataXferFromSubnet_Type(Unsigned32):
    """Custom type traceSessionFrVcNotDataXferFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionFrVcNotDataXferFromSubnet_Type.__name__ = "Unsigned32"
_TraceSessionFrVcNotDataXferFromSubnet_Object = MibTableColumn
traceSessionFrVcNotDataXferFromSubnet = _TraceSessionFrVcNotDataXferFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 12, 1, 8),
    _TraceSessionFrVcNotDataXferFromSubnet_Type()
)
traceSessionFrVcNotDataXferFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcNotDataXferFromSubnet.setStatus("mandatory")


class _TraceSessionFrVcFrmLossTimeouts_Type(Unsigned32):
    """Custom type traceSessionFrVcFrmLossTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionFrVcFrmLossTimeouts_Type.__name__ = "Unsigned32"
_TraceSessionFrVcFrmLossTimeouts_Object = MibTableColumn
traceSessionFrVcFrmLossTimeouts = _TraceSessionFrVcFrmLossTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 12, 1, 9),
    _TraceSessionFrVcFrmLossTimeouts_Type()
)
traceSessionFrVcFrmLossTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcFrmLossTimeouts.setStatus("mandatory")


class _TraceSessionFrVcOoSeqByteCntExceeded_Type(Unsigned32):
    """Custom type traceSessionFrVcOoSeqByteCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionFrVcOoSeqByteCntExceeded_Type.__name__ = "Unsigned32"
_TraceSessionFrVcOoSeqByteCntExceeded_Object = MibTableColumn
traceSessionFrVcOoSeqByteCntExceeded = _TraceSessionFrVcOoSeqByteCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 12, 1, 10),
    _TraceSessionFrVcOoSeqByteCntExceeded_Type()
)
traceSessionFrVcOoSeqByteCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcOoSeqByteCntExceeded.setStatus("mandatory")


class _TraceSessionFrVcPeakOoSeqPktCount_Type(Unsigned32):
    """Custom type traceSessionFrVcPeakOoSeqPktCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionFrVcPeakOoSeqPktCount_Type.__name__ = "Unsigned32"
_TraceSessionFrVcPeakOoSeqPktCount_Object = MibTableColumn
traceSessionFrVcPeakOoSeqPktCount = _TraceSessionFrVcPeakOoSeqPktCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 12, 1, 11),
    _TraceSessionFrVcPeakOoSeqPktCount_Type()
)
traceSessionFrVcPeakOoSeqPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcPeakOoSeqPktCount.setStatus("mandatory")


class _TraceSessionFrVcPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type traceSessionFrVcPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionFrVcPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_TraceSessionFrVcPeakOoSeqFrmForwarded_Object = MibTableColumn
traceSessionFrVcPeakOoSeqFrmForwarded = _TraceSessionFrVcPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 12, 1, 12),
    _TraceSessionFrVcPeakOoSeqFrmForwarded_Type()
)
traceSessionFrVcPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcPeakOoSeqFrmForwarded.setStatus("mandatory")


class _TraceSessionFrVcSendSequenceNumber_Type(Unsigned32):
    """Custom type traceSessionFrVcSendSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionFrVcSendSequenceNumber_Type.__name__ = "Unsigned32"
_TraceSessionFrVcSendSequenceNumber_Object = MibTableColumn
traceSessionFrVcSendSequenceNumber = _TraceSessionFrVcSendSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 12, 1, 13),
    _TraceSessionFrVcSendSequenceNumber_Type()
)
traceSessionFrVcSendSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcSendSequenceNumber.setStatus("mandatory")


class _TraceSessionFrVcPktRetryTimeouts_Type(Unsigned32):
    """Custom type traceSessionFrVcPktRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionFrVcPktRetryTimeouts_Type.__name__ = "Unsigned32"
_TraceSessionFrVcPktRetryTimeouts_Object = MibTableColumn
traceSessionFrVcPktRetryTimeouts = _TraceSessionFrVcPktRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 12, 1, 15),
    _TraceSessionFrVcPktRetryTimeouts_Type()
)
traceSessionFrVcPktRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcPktRetryTimeouts.setStatus("mandatory")


class _TraceSessionFrVcPeakRetryQueueSize_Type(Unsigned32):
    """Custom type traceSessionFrVcPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionFrVcPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_TraceSessionFrVcPeakRetryQueueSize_Object = MibTableColumn
traceSessionFrVcPeakRetryQueueSize = _TraceSessionFrVcPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 12, 1, 16),
    _TraceSessionFrVcPeakRetryQueueSize_Type()
)
traceSessionFrVcPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcPeakRetryQueueSize.setStatus("mandatory")


class _TraceSessionFrVcSubnetRecoveries_Type(Unsigned32):
    """Custom type traceSessionFrVcSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionFrVcSubnetRecoveries_Type.__name__ = "Unsigned32"
_TraceSessionFrVcSubnetRecoveries_Object = MibTableColumn
traceSessionFrVcSubnetRecoveries = _TraceSessionFrVcSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 12, 1, 17),
    _TraceSessionFrVcSubnetRecoveries_Type()
)
traceSessionFrVcSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcSubnetRecoveries.setStatus("mandatory")


class _TraceSessionFrVcOoSeqPktCntExceeded_Type(Unsigned32):
    """Custom type traceSessionFrVcOoSeqPktCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TraceSessionFrVcOoSeqPktCntExceeded_Type.__name__ = "Unsigned32"
_TraceSessionFrVcOoSeqPktCntExceeded_Object = MibTableColumn
traceSessionFrVcOoSeqPktCntExceeded = _TraceSessionFrVcOoSeqPktCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 12, 1, 19),
    _TraceSessionFrVcOoSeqPktCntExceeded_Type()
)
traceSessionFrVcOoSeqPktCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcOoSeqPktCntExceeded.setStatus("mandatory")


class _TraceSessionFrVcPeakOoSeqByteCount_Type(Unsigned32):
    """Custom type traceSessionFrVcPeakOoSeqByteCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_TraceSessionFrVcPeakOoSeqByteCount_Type.__name__ = "Unsigned32"
_TraceSessionFrVcPeakOoSeqByteCount_Object = MibTableColumn
traceSessionFrVcPeakOoSeqByteCount = _TraceSessionFrVcPeakOoSeqByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 12, 1, 20),
    _TraceSessionFrVcPeakOoSeqByteCount_Type()
)
traceSessionFrVcPeakOoSeqByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcPeakOoSeqByteCount.setStatus("mandatory")
_TraceSessionFrVcDmepTable_Object = MibTable
traceSessionFrVcDmepTable = _TraceSessionFrVcDmepTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 417)
)
if mibBuilder.loadTexts:
    traceSessionFrVcDmepTable.setStatus("mandatory")
_TraceSessionFrVcDmepEntry_Object = MibTableRow
traceSessionFrVcDmepEntry = _TraceSessionFrVcDmepEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 417, 1)
)
traceSessionFrVcDmepEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceSessionIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceSessionFrIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceSessionFrVcIndex"),
    (0, "Nortel-Magellan-Passport-FrTraceRcvrMIB", "traceSessionFrVcDmepValue"),
)
if mibBuilder.loadTexts:
    traceSessionFrVcDmepEntry.setStatus("mandatory")
_TraceSessionFrVcDmepValue_Type = RowPointer
_TraceSessionFrVcDmepValue_Object = MibTableColumn
traceSessionFrVcDmepValue = _TraceSessionFrVcDmepValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 3, 2, 417, 1, 1),
    _TraceSessionFrVcDmepValue_Type()
)
traceSessionFrVcDmepValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFrVcDmepValue.setStatus("mandatory")
_FrTraceRcvrMIB_ObjectIdentity = ObjectIdentity
frTraceRcvrMIB = _FrTraceRcvrMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 139)
)
_FrTraceRcvrGroup_ObjectIdentity = ObjectIdentity
frTraceRcvrGroup = _FrTraceRcvrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 139, 1)
)
_FrTraceRcvrGroupBE_ObjectIdentity = ObjectIdentity
frTraceRcvrGroupBE = _FrTraceRcvrGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 139, 1, 5)
)
_FrTraceRcvrGroupBE01_ObjectIdentity = ObjectIdentity
frTraceRcvrGroupBE01 = _FrTraceRcvrGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 139, 1, 5, 2)
)
_FrTraceRcvrGroupBE01A_ObjectIdentity = ObjectIdentity
frTraceRcvrGroupBE01A = _FrTraceRcvrGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 139, 1, 5, 2, 2)
)
_FrTraceRcvrCapabilities_ObjectIdentity = ObjectIdentity
frTraceRcvrCapabilities = _FrTraceRcvrCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 139, 3)
)
_FrTraceRcvrCapabilitiesBE_ObjectIdentity = ObjectIdentity
frTraceRcvrCapabilitiesBE = _FrTraceRcvrCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 139, 3, 5)
)
_FrTraceRcvrCapabilitiesBE01_ObjectIdentity = ObjectIdentity
frTraceRcvrCapabilitiesBE01 = _FrTraceRcvrCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 139, 3, 5, 2)
)
_FrTraceRcvrCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
frTraceRcvrCapabilitiesBE01A = _FrTraceRcvrCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 139, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-FrTraceRcvrMIB",
    **{"traceRcvrFr": traceRcvrFr,
       "traceRcvrFrRowStatusTable": traceRcvrFrRowStatusTable,
       "traceRcvrFrRowStatusEntry": traceRcvrFrRowStatusEntry,
       "traceRcvrFrRowStatus": traceRcvrFrRowStatus,
       "traceRcvrFrComponentName": traceRcvrFrComponentName,
       "traceRcvrFrStorageType": traceRcvrFrStorageType,
       "traceRcvrFrIndex": traceRcvrFrIndex,
       "traceRcvrFrDna": traceRcvrFrDna,
       "traceRcvrFrDnaRowStatusTable": traceRcvrFrDnaRowStatusTable,
       "traceRcvrFrDnaRowStatusEntry": traceRcvrFrDnaRowStatusEntry,
       "traceRcvrFrDnaRowStatus": traceRcvrFrDnaRowStatus,
       "traceRcvrFrDnaComponentName": traceRcvrFrDnaComponentName,
       "traceRcvrFrDnaStorageType": traceRcvrFrDnaStorageType,
       "traceRcvrFrDnaIndex": traceRcvrFrDnaIndex,
       "traceRcvrFrDnaCug": traceRcvrFrDnaCug,
       "traceRcvrFrDnaCugRowStatusTable": traceRcvrFrDnaCugRowStatusTable,
       "traceRcvrFrDnaCugRowStatusEntry": traceRcvrFrDnaCugRowStatusEntry,
       "traceRcvrFrDnaCugRowStatus": traceRcvrFrDnaCugRowStatus,
       "traceRcvrFrDnaCugComponentName": traceRcvrFrDnaCugComponentName,
       "traceRcvrFrDnaCugStorageType": traceRcvrFrDnaCugStorageType,
       "traceRcvrFrDnaCugIndex": traceRcvrFrDnaCugIndex,
       "traceRcvrFrDnaCugCugOptionsTable": traceRcvrFrDnaCugCugOptionsTable,
       "traceRcvrFrDnaCugCugOptionsEntry": traceRcvrFrDnaCugCugOptionsEntry,
       "traceRcvrFrDnaCugType": traceRcvrFrDnaCugType,
       "traceRcvrFrDnaCugDnic": traceRcvrFrDnaCugDnic,
       "traceRcvrFrDnaCugInterlockCode": traceRcvrFrDnaCugInterlockCode,
       "traceRcvrFrDnaCugPreferential": traceRcvrFrDnaCugPreferential,
       "traceRcvrFrDnaCugOutCalls": traceRcvrFrDnaCugOutCalls,
       "traceRcvrFrDnaCugIncCalls": traceRcvrFrDnaCugIncCalls,
       "traceRcvrFrDnaCugPrivileged": traceRcvrFrDnaCugPrivileged,
       "traceRcvrFrDnaAddressTable": traceRcvrFrDnaAddressTable,
       "traceRcvrFrDnaAddressEntry": traceRcvrFrDnaAddressEntry,
       "traceRcvrFrDnaNumberingPlanIndicator": traceRcvrFrDnaNumberingPlanIndicator,
       "traceRcvrFrDnaDataNetworkAddress": traceRcvrFrDnaDataNetworkAddress,
       "traceRcvrFrDnaOutgoingOptionsTable": traceRcvrFrDnaOutgoingOptionsTable,
       "traceRcvrFrDnaOutgoingOptionsEntry": traceRcvrFrDnaOutgoingOptionsEntry,
       "traceRcvrFrDnaOutCalls": traceRcvrFrDnaOutCalls,
       "traceRcvrFrDnaOutDefaultPriority": traceRcvrFrDnaOutDefaultPriority,
       "traceRcvrFrDnaOutIntl": traceRcvrFrDnaOutIntl,
       "traceRcvrFrDnaOutDefaultPathReliability": traceRcvrFrDnaOutDefaultPathReliability,
       "traceRcvrFrDnaOutPathReliabilityOverRide": traceRcvrFrDnaOutPathReliabilityOverRide,
       "traceRcvrFrDnaOutPathReliabilitySignal": traceRcvrFrDnaOutPathReliabilitySignal,
       "traceRcvrFrDnaOutAccess": traceRcvrFrDnaOutAccess,
       "traceRcvrFrDnaIncomingOptionsTable": traceRcvrFrDnaIncomingOptionsTable,
       "traceRcvrFrDnaIncomingOptionsEntry": traceRcvrFrDnaIncomingOptionsEntry,
       "traceRcvrFrDnaIncCalls": traceRcvrFrDnaIncCalls,
       "traceRcvrFrDnaCallOptionsTable": traceRcvrFrDnaCallOptionsTable,
       "traceRcvrFrDnaCallOptionsEntry": traceRcvrFrDnaCallOptionsEntry,
       "traceRcvrFrDnaPacketSizes": traceRcvrFrDnaPacketSizes,
       "traceRcvrFrDnaDefaultRecvFrmNetworkPacketSize": traceRcvrFrDnaDefaultRecvFrmNetworkPacketSize,
       "traceRcvrFrDnaDefaultSendToNetworkPacketSize": traceRcvrFrDnaDefaultSendToNetworkPacketSize,
       "traceRcvrFrDnaCugFormat": traceRcvrFrDnaCugFormat,
       "traceRcvrFrDc": traceRcvrFrDc,
       "traceRcvrFrDcRowStatusTable": traceRcvrFrDcRowStatusTable,
       "traceRcvrFrDcRowStatusEntry": traceRcvrFrDcRowStatusEntry,
       "traceRcvrFrDcRowStatus": traceRcvrFrDcRowStatus,
       "traceRcvrFrDcComponentName": traceRcvrFrDcComponentName,
       "traceRcvrFrDcStorageType": traceRcvrFrDcStorageType,
       "traceRcvrFrDcIndex": traceRcvrFrDcIndex,
       "traceRcvrFrDcOptionsTable": traceRcvrFrDcOptionsTable,
       "traceRcvrFrDcOptionsEntry": traceRcvrFrDcOptionsEntry,
       "traceRcvrFrDcRemoteNpi": traceRcvrFrDcRemoteNpi,
       "traceRcvrFrDcRemoteDna": traceRcvrFrDcRemoteDna,
       "traceRcvrFrDcType": traceRcvrFrDcType,
       "traceRcvrFrDcUserData": traceRcvrFrDcUserData,
       "traceSessionFr": traceSessionFr,
       "traceSessionFrRowStatusTable": traceSessionFrRowStatusTable,
       "traceSessionFrRowStatusEntry": traceSessionFrRowStatusEntry,
       "traceSessionFrRowStatus": traceSessionFrRowStatus,
       "traceSessionFrComponentName": traceSessionFrComponentName,
       "traceSessionFrStorageType": traceSessionFrStorageType,
       "traceSessionFrIndex": traceSessionFrIndex,
       "traceSessionFrVc": traceSessionFrVc,
       "traceSessionFrVcRowStatusTable": traceSessionFrVcRowStatusTable,
       "traceSessionFrVcRowStatusEntry": traceSessionFrVcRowStatusEntry,
       "traceSessionFrVcRowStatus": traceSessionFrVcRowStatus,
       "traceSessionFrVcComponentName": traceSessionFrVcComponentName,
       "traceSessionFrVcStorageType": traceSessionFrVcStorageType,
       "traceSessionFrVcIndex": traceSessionFrVcIndex,
       "traceSessionFrVcCadTable": traceSessionFrVcCadTable,
       "traceSessionFrVcCadEntry": traceSessionFrVcCadEntry,
       "traceSessionFrVcType": traceSessionFrVcType,
       "traceSessionFrVcState": traceSessionFrVcState,
       "traceSessionFrVcPreviousState": traceSessionFrVcPreviousState,
       "traceSessionFrVcDiagnosticCode": traceSessionFrVcDiagnosticCode,
       "traceSessionFrVcPreviousDiagnosticCode": traceSessionFrVcPreviousDiagnosticCode,
       "traceSessionFrVcCalledNpi": traceSessionFrVcCalledNpi,
       "traceSessionFrVcCalledDna": traceSessionFrVcCalledDna,
       "traceSessionFrVcCalledLcn": traceSessionFrVcCalledLcn,
       "traceSessionFrVcCallingNpi": traceSessionFrVcCallingNpi,
       "traceSessionFrVcCallingDna": traceSessionFrVcCallingDna,
       "traceSessionFrVcCallingLcn": traceSessionFrVcCallingLcn,
       "traceSessionFrVcAccountingEnabled": traceSessionFrVcAccountingEnabled,
       "traceSessionFrVcFastSelectCall": traceSessionFrVcFastSelectCall,
       "traceSessionFrVcPathReliability": traceSessionFrVcPathReliability,
       "traceSessionFrVcAccountingEnd": traceSessionFrVcAccountingEnd,
       "traceSessionFrVcPriority": traceSessionFrVcPriority,
       "traceSessionFrVcSegmentSize": traceSessionFrVcSegmentSize,
       "traceSessionFrVcMaxSubnetPktSize": traceSessionFrVcMaxSubnetPktSize,
       "traceSessionFrVcRcosToNetwork": traceSessionFrVcRcosToNetwork,
       "traceSessionFrVcRcosFromNetwork": traceSessionFrVcRcosFromNetwork,
       "traceSessionFrVcEmissionPriorityToNetwork": traceSessionFrVcEmissionPriorityToNetwork,
       "traceSessionFrVcEmissionPriorityFromNetwork": traceSessionFrVcEmissionPriorityFromNetwork,
       "traceSessionFrVcDataPath": traceSessionFrVcDataPath,
       "traceSessionFrVcIntdTable": traceSessionFrVcIntdTable,
       "traceSessionFrVcIntdEntry": traceSessionFrVcIntdEntry,
       "traceSessionFrVcCallReferenceNumber": traceSessionFrVcCallReferenceNumber,
       "traceSessionFrVcElapsedTimeTillNow": traceSessionFrVcElapsedTimeTillNow,
       "traceSessionFrVcSegmentsRx": traceSessionFrVcSegmentsRx,
       "traceSessionFrVcSegmentsSent": traceSessionFrVcSegmentsSent,
       "traceSessionFrVcStartTime": traceSessionFrVcStartTime,
       "traceSessionFrVcFrdTable": traceSessionFrVcFrdTable,
       "traceSessionFrVcFrdEntry": traceSessionFrVcFrdEntry,
       "traceSessionFrVcFrmCongestedToSubnet": traceSessionFrVcFrmCongestedToSubnet,
       "traceSessionFrVcCannotForwardToSubnet": traceSessionFrVcCannotForwardToSubnet,
       "traceSessionFrVcNotDataXferToSubnet": traceSessionFrVcNotDataXferToSubnet,
       "traceSessionFrVcOutOfRangeFrmFromSubnet": traceSessionFrVcOutOfRangeFrmFromSubnet,
       "traceSessionFrVcCombErrorsFromSubnet": traceSessionFrVcCombErrorsFromSubnet,
       "traceSessionFrVcDuplicatesFromSubnet": traceSessionFrVcDuplicatesFromSubnet,
       "traceSessionFrVcNotDataXferFromSubnet": traceSessionFrVcNotDataXferFromSubnet,
       "traceSessionFrVcFrmLossTimeouts": traceSessionFrVcFrmLossTimeouts,
       "traceSessionFrVcOoSeqByteCntExceeded": traceSessionFrVcOoSeqByteCntExceeded,
       "traceSessionFrVcPeakOoSeqPktCount": traceSessionFrVcPeakOoSeqPktCount,
       "traceSessionFrVcPeakOoSeqFrmForwarded": traceSessionFrVcPeakOoSeqFrmForwarded,
       "traceSessionFrVcSendSequenceNumber": traceSessionFrVcSendSequenceNumber,
       "traceSessionFrVcPktRetryTimeouts": traceSessionFrVcPktRetryTimeouts,
       "traceSessionFrVcPeakRetryQueueSize": traceSessionFrVcPeakRetryQueueSize,
       "traceSessionFrVcSubnetRecoveries": traceSessionFrVcSubnetRecoveries,
       "traceSessionFrVcOoSeqPktCntExceeded": traceSessionFrVcOoSeqPktCntExceeded,
       "traceSessionFrVcPeakOoSeqByteCount": traceSessionFrVcPeakOoSeqByteCount,
       "traceSessionFrVcDmepTable": traceSessionFrVcDmepTable,
       "traceSessionFrVcDmepEntry": traceSessionFrVcDmepEntry,
       "traceSessionFrVcDmepValue": traceSessionFrVcDmepValue,
       "frTraceRcvrMIB": frTraceRcvrMIB,
       "frTraceRcvrGroup": frTraceRcvrGroup,
       "frTraceRcvrGroupBE": frTraceRcvrGroupBE,
       "frTraceRcvrGroupBE01": frTraceRcvrGroupBE01,
       "frTraceRcvrGroupBE01A": frTraceRcvrGroupBE01A,
       "frTraceRcvrCapabilities": frTraceRcvrCapabilities,
       "frTraceRcvrCapabilitiesBE": frTraceRcvrCapabilitiesBE,
       "frTraceRcvrCapabilitiesBE01": frTraceRcvrCapabilitiesBE01,
       "frTraceRcvrCapabilitiesBE01A": frTraceRcvrCapabilitiesBE01A}
)
