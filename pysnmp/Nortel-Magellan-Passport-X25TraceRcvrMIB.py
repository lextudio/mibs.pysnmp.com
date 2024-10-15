# SNMP MIB module (Nortel-Magellan-Passport-X25TraceRcvrMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-X25TraceRcvrMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:42 2024
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
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(DigitString,
 EnterpriseDateAndTime,
 Hex,
 HexString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
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

_TraceRcvrX25_ObjectIdentity = ObjectIdentity
traceRcvrX25 = _TraceRcvrX25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2)
)
_TraceRcvrX25RowStatusTable_Object = MibTable
traceRcvrX25RowStatusTable = _TraceRcvrX25RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 1)
)
if mibBuilder.loadTexts:
    traceRcvrX25RowStatusTable.setStatus("mandatory")
_TraceRcvrX25RowStatusEntry_Object = MibTableRow
traceRcvrX25RowStatusEntry = _TraceRcvrX25RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 1, 1)
)
traceRcvrX25RowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceRcvrIndex"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceRcvrX25Index"),
)
if mibBuilder.loadTexts:
    traceRcvrX25RowStatusEntry.setStatus("mandatory")
_TraceRcvrX25RowStatus_Type = RowStatus
_TraceRcvrX25RowStatus_Object = MibTableColumn
traceRcvrX25RowStatus = _TraceRcvrX25RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 1, 1, 1),
    _TraceRcvrX25RowStatus_Type()
)
traceRcvrX25RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrX25RowStatus.setStatus("mandatory")
_TraceRcvrX25ComponentName_Type = DisplayString
_TraceRcvrX25ComponentName_Object = MibTableColumn
traceRcvrX25ComponentName = _TraceRcvrX25ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 1, 1, 2),
    _TraceRcvrX25ComponentName_Type()
)
traceRcvrX25ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25ComponentName.setStatus("mandatory")
_TraceRcvrX25StorageType_Type = StorageType
_TraceRcvrX25StorageType_Object = MibTableColumn
traceRcvrX25StorageType = _TraceRcvrX25StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 1, 1, 4),
    _TraceRcvrX25StorageType_Type()
)
traceRcvrX25StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25StorageType.setStatus("mandatory")
_TraceRcvrX25Index_Type = NonReplicated
_TraceRcvrX25Index_Object = MibTableColumn
traceRcvrX25Index = _TraceRcvrX25Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 1, 1, 10),
    _TraceRcvrX25Index_Type()
)
traceRcvrX25Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceRcvrX25Index.setStatus("mandatory")
_TraceRcvrX25Dna_ObjectIdentity = ObjectIdentity
traceRcvrX25Dna = _TraceRcvrX25Dna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2)
)
_TraceRcvrX25DnaRowStatusTable_Object = MibTable
traceRcvrX25DnaRowStatusTable = _TraceRcvrX25DnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    traceRcvrX25DnaRowStatusTable.setStatus("mandatory")
_TraceRcvrX25DnaRowStatusEntry_Object = MibTableRow
traceRcvrX25DnaRowStatusEntry = _TraceRcvrX25DnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 1, 1)
)
traceRcvrX25DnaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceRcvrIndex"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceRcvrX25Index"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceRcvrX25DnaIndex"),
)
if mibBuilder.loadTexts:
    traceRcvrX25DnaRowStatusEntry.setStatus("mandatory")
_TraceRcvrX25DnaRowStatus_Type = RowStatus
_TraceRcvrX25DnaRowStatus_Object = MibTableColumn
traceRcvrX25DnaRowStatus = _TraceRcvrX25DnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 1, 1, 1),
    _TraceRcvrX25DnaRowStatus_Type()
)
traceRcvrX25DnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DnaRowStatus.setStatus("mandatory")
_TraceRcvrX25DnaComponentName_Type = DisplayString
_TraceRcvrX25DnaComponentName_Object = MibTableColumn
traceRcvrX25DnaComponentName = _TraceRcvrX25DnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 1, 1, 2),
    _TraceRcvrX25DnaComponentName_Type()
)
traceRcvrX25DnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DnaComponentName.setStatus("mandatory")
_TraceRcvrX25DnaStorageType_Type = StorageType
_TraceRcvrX25DnaStorageType_Object = MibTableColumn
traceRcvrX25DnaStorageType = _TraceRcvrX25DnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 1, 1, 4),
    _TraceRcvrX25DnaStorageType_Type()
)
traceRcvrX25DnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DnaStorageType.setStatus("mandatory")
_TraceRcvrX25DnaIndex_Type = NonReplicated
_TraceRcvrX25DnaIndex_Object = MibTableColumn
traceRcvrX25DnaIndex = _TraceRcvrX25DnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 1, 1, 10),
    _TraceRcvrX25DnaIndex_Type()
)
traceRcvrX25DnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceRcvrX25DnaIndex.setStatus("mandatory")
_TraceRcvrX25DnaCug_ObjectIdentity = ObjectIdentity
traceRcvrX25DnaCug = _TraceRcvrX25DnaCug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 2)
)
_TraceRcvrX25DnaCugRowStatusTable_Object = MibTable
traceRcvrX25DnaCugRowStatusTable = _TraceRcvrX25DnaCugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    traceRcvrX25DnaCugRowStatusTable.setStatus("mandatory")
_TraceRcvrX25DnaCugRowStatusEntry_Object = MibTableRow
traceRcvrX25DnaCugRowStatusEntry = _TraceRcvrX25DnaCugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 2, 1, 1)
)
traceRcvrX25DnaCugRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceRcvrIndex"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceRcvrX25Index"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceRcvrX25DnaIndex"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceRcvrX25DnaCugIndex"),
)
if mibBuilder.loadTexts:
    traceRcvrX25DnaCugRowStatusEntry.setStatus("mandatory")
_TraceRcvrX25DnaCugRowStatus_Type = RowStatus
_TraceRcvrX25DnaCugRowStatus_Object = MibTableColumn
traceRcvrX25DnaCugRowStatus = _TraceRcvrX25DnaCugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 2, 1, 1, 1),
    _TraceRcvrX25DnaCugRowStatus_Type()
)
traceRcvrX25DnaCugRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrX25DnaCugRowStatus.setStatus("mandatory")
_TraceRcvrX25DnaCugComponentName_Type = DisplayString
_TraceRcvrX25DnaCugComponentName_Object = MibTableColumn
traceRcvrX25DnaCugComponentName = _TraceRcvrX25DnaCugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 2, 1, 1, 2),
    _TraceRcvrX25DnaCugComponentName_Type()
)
traceRcvrX25DnaCugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DnaCugComponentName.setStatus("mandatory")
_TraceRcvrX25DnaCugStorageType_Type = StorageType
_TraceRcvrX25DnaCugStorageType_Object = MibTableColumn
traceRcvrX25DnaCugStorageType = _TraceRcvrX25DnaCugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 2, 1, 1, 4),
    _TraceRcvrX25DnaCugStorageType_Type()
)
traceRcvrX25DnaCugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DnaCugStorageType.setStatus("mandatory")


class _TraceRcvrX25DnaCugIndex_Type(Integer32):
    """Custom type traceRcvrX25DnaCugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_TraceRcvrX25DnaCugIndex_Type.__name__ = "Integer32"
_TraceRcvrX25DnaCugIndex_Object = MibTableColumn
traceRcvrX25DnaCugIndex = _TraceRcvrX25DnaCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 2, 1, 1, 10),
    _TraceRcvrX25DnaCugIndex_Type()
)
traceRcvrX25DnaCugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceRcvrX25DnaCugIndex.setStatus("mandatory")
_TraceRcvrX25DnaCugCugOptionsTable_Object = MibTable
traceRcvrX25DnaCugCugOptionsTable = _TraceRcvrX25DnaCugCugOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 2, 10)
)
if mibBuilder.loadTexts:
    traceRcvrX25DnaCugCugOptionsTable.setStatus("mandatory")
_TraceRcvrX25DnaCugCugOptionsEntry_Object = MibTableRow
traceRcvrX25DnaCugCugOptionsEntry = _TraceRcvrX25DnaCugCugOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 2, 10, 1)
)
traceRcvrX25DnaCugCugOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceRcvrIndex"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceRcvrX25Index"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceRcvrX25DnaIndex"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceRcvrX25DnaCugIndex"),
)
if mibBuilder.loadTexts:
    traceRcvrX25DnaCugCugOptionsEntry.setStatus("mandatory")


class _TraceRcvrX25DnaCugType_Type(Integer32):
    """Custom type traceRcvrX25DnaCugType based on Integer32"""
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


_TraceRcvrX25DnaCugType_Type.__name__ = "Integer32"
_TraceRcvrX25DnaCugType_Object = MibTableColumn
traceRcvrX25DnaCugType = _TraceRcvrX25DnaCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 2, 10, 1, 1),
    _TraceRcvrX25DnaCugType_Type()
)
traceRcvrX25DnaCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrX25DnaCugType.setStatus("mandatory")


class _TraceRcvrX25DnaCugDnic_Type(DigitString):
    """Custom type traceRcvrX25DnaCugDnic based on DigitString"""
    defaultHexValue = "30303030"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_TraceRcvrX25DnaCugDnic_Type.__name__ = "DigitString"
_TraceRcvrX25DnaCugDnic_Object = MibTableColumn
traceRcvrX25DnaCugDnic = _TraceRcvrX25DnaCugDnic_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 2, 10, 1, 2),
    _TraceRcvrX25DnaCugDnic_Type()
)
traceRcvrX25DnaCugDnic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrX25DnaCugDnic.setStatus("mandatory")


class _TraceRcvrX25DnaCugInterlockCode_Type(Unsigned32):
    """Custom type traceRcvrX25DnaCugInterlockCode based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TraceRcvrX25DnaCugInterlockCode_Type.__name__ = "Unsigned32"
_TraceRcvrX25DnaCugInterlockCode_Object = MibTableColumn
traceRcvrX25DnaCugInterlockCode = _TraceRcvrX25DnaCugInterlockCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 2, 10, 1, 3),
    _TraceRcvrX25DnaCugInterlockCode_Type()
)
traceRcvrX25DnaCugInterlockCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrX25DnaCugInterlockCode.setStatus("mandatory")


class _TraceRcvrX25DnaCugPreferential_Type(Integer32):
    """Custom type traceRcvrX25DnaCugPreferential based on Integer32"""
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


_TraceRcvrX25DnaCugPreferential_Type.__name__ = "Integer32"
_TraceRcvrX25DnaCugPreferential_Object = MibTableColumn
traceRcvrX25DnaCugPreferential = _TraceRcvrX25DnaCugPreferential_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 2, 10, 1, 4),
    _TraceRcvrX25DnaCugPreferential_Type()
)
traceRcvrX25DnaCugPreferential.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DnaCugPreferential.setStatus("mandatory")


class _TraceRcvrX25DnaCugOutCalls_Type(Integer32):
    """Custom type traceRcvrX25DnaCugOutCalls based on Integer32"""
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


_TraceRcvrX25DnaCugOutCalls_Type.__name__ = "Integer32"
_TraceRcvrX25DnaCugOutCalls_Object = MibTableColumn
traceRcvrX25DnaCugOutCalls = _TraceRcvrX25DnaCugOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 2, 10, 1, 5),
    _TraceRcvrX25DnaCugOutCalls_Type()
)
traceRcvrX25DnaCugOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DnaCugOutCalls.setStatus("mandatory")


class _TraceRcvrX25DnaCugIncCalls_Type(Integer32):
    """Custom type traceRcvrX25DnaCugIncCalls based on Integer32"""
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


_TraceRcvrX25DnaCugIncCalls_Type.__name__ = "Integer32"
_TraceRcvrX25DnaCugIncCalls_Object = MibTableColumn
traceRcvrX25DnaCugIncCalls = _TraceRcvrX25DnaCugIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 2, 10, 1, 6),
    _TraceRcvrX25DnaCugIncCalls_Type()
)
traceRcvrX25DnaCugIncCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DnaCugIncCalls.setStatus("mandatory")


class _TraceRcvrX25DnaCugPrivileged_Type(Integer32):
    """Custom type traceRcvrX25DnaCugPrivileged based on Integer32"""
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


_TraceRcvrX25DnaCugPrivileged_Type.__name__ = "Integer32"
_TraceRcvrX25DnaCugPrivileged_Object = MibTableColumn
traceRcvrX25DnaCugPrivileged = _TraceRcvrX25DnaCugPrivileged_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 2, 10, 1, 7),
    _TraceRcvrX25DnaCugPrivileged_Type()
)
traceRcvrX25DnaCugPrivileged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrX25DnaCugPrivileged.setStatus("mandatory")
_TraceRcvrX25DnaAddressTable_Object = MibTable
traceRcvrX25DnaAddressTable = _TraceRcvrX25DnaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 10)
)
if mibBuilder.loadTexts:
    traceRcvrX25DnaAddressTable.setStatus("mandatory")
_TraceRcvrX25DnaAddressEntry_Object = MibTableRow
traceRcvrX25DnaAddressEntry = _TraceRcvrX25DnaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 10, 1)
)
traceRcvrX25DnaAddressEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceRcvrIndex"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceRcvrX25Index"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceRcvrX25DnaIndex"),
)
if mibBuilder.loadTexts:
    traceRcvrX25DnaAddressEntry.setStatus("mandatory")


class _TraceRcvrX25DnaNumberingPlanIndicator_Type(Integer32):
    """Custom type traceRcvrX25DnaNumberingPlanIndicator based on Integer32"""
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


_TraceRcvrX25DnaNumberingPlanIndicator_Type.__name__ = "Integer32"
_TraceRcvrX25DnaNumberingPlanIndicator_Object = MibTableColumn
traceRcvrX25DnaNumberingPlanIndicator = _TraceRcvrX25DnaNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 10, 1, 1),
    _TraceRcvrX25DnaNumberingPlanIndicator_Type()
)
traceRcvrX25DnaNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrX25DnaNumberingPlanIndicator.setStatus("mandatory")


class _TraceRcvrX25DnaDataNetworkAddress_Type(DigitString):
    """Custom type traceRcvrX25DnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_TraceRcvrX25DnaDataNetworkAddress_Type.__name__ = "DigitString"
_TraceRcvrX25DnaDataNetworkAddress_Object = MibTableColumn
traceRcvrX25DnaDataNetworkAddress = _TraceRcvrX25DnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 10, 1, 2),
    _TraceRcvrX25DnaDataNetworkAddress_Type()
)
traceRcvrX25DnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrX25DnaDataNetworkAddress.setStatus("mandatory")
_TraceRcvrX25DnaOutgoingOptionsTable_Object = MibTable
traceRcvrX25DnaOutgoingOptionsTable = _TraceRcvrX25DnaOutgoingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 11)
)
if mibBuilder.loadTexts:
    traceRcvrX25DnaOutgoingOptionsTable.setStatus("mandatory")
_TraceRcvrX25DnaOutgoingOptionsEntry_Object = MibTableRow
traceRcvrX25DnaOutgoingOptionsEntry = _TraceRcvrX25DnaOutgoingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 11, 1)
)
traceRcvrX25DnaOutgoingOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceRcvrIndex"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceRcvrX25Index"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceRcvrX25DnaIndex"),
)
if mibBuilder.loadTexts:
    traceRcvrX25DnaOutgoingOptionsEntry.setStatus("mandatory")


class _TraceRcvrX25DnaOutCalls_Type(Integer32):
    """Custom type traceRcvrX25DnaOutCalls based on Integer32"""
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


_TraceRcvrX25DnaOutCalls_Type.__name__ = "Integer32"
_TraceRcvrX25DnaOutCalls_Object = MibTableColumn
traceRcvrX25DnaOutCalls = _TraceRcvrX25DnaOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 11, 1, 1),
    _TraceRcvrX25DnaOutCalls_Type()
)
traceRcvrX25DnaOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DnaOutCalls.setStatus("mandatory")


class _TraceRcvrX25DnaOutDefaultPriority_Type(Integer32):
    """Custom type traceRcvrX25DnaOutDefaultPriority based on Integer32"""
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


_TraceRcvrX25DnaOutDefaultPriority_Type.__name__ = "Integer32"
_TraceRcvrX25DnaOutDefaultPriority_Object = MibTableColumn
traceRcvrX25DnaOutDefaultPriority = _TraceRcvrX25DnaOutDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 11, 1, 7),
    _TraceRcvrX25DnaOutDefaultPriority_Type()
)
traceRcvrX25DnaOutDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrX25DnaOutDefaultPriority.setStatus("mandatory")


class _TraceRcvrX25DnaOutIntl_Type(Integer32):
    """Custom type traceRcvrX25DnaOutIntl based on Integer32"""
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


_TraceRcvrX25DnaOutIntl_Type.__name__ = "Integer32"
_TraceRcvrX25DnaOutIntl_Object = MibTableColumn
traceRcvrX25DnaOutIntl = _TraceRcvrX25DnaOutIntl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 11, 1, 8),
    _TraceRcvrX25DnaOutIntl_Type()
)
traceRcvrX25DnaOutIntl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DnaOutIntl.setStatus("mandatory")


class _TraceRcvrX25DnaOutDefaultPathSensitivity_Type(Integer32):
    """Custom type traceRcvrX25DnaOutDefaultPathSensitivity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delay", 1),
          ("throughput", 0))
    )


_TraceRcvrX25DnaOutDefaultPathSensitivity_Type.__name__ = "Integer32"
_TraceRcvrX25DnaOutDefaultPathSensitivity_Object = MibTableColumn
traceRcvrX25DnaOutDefaultPathSensitivity = _TraceRcvrX25DnaOutDefaultPathSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 11, 1, 11),
    _TraceRcvrX25DnaOutDefaultPathSensitivity_Type()
)
traceRcvrX25DnaOutDefaultPathSensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DnaOutDefaultPathSensitivity.setStatus("obsolete")


class _TraceRcvrX25DnaOutDefaultPathReliability_Type(Integer32):
    """Custom type traceRcvrX25DnaOutDefaultPathReliability based on Integer32"""
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


_TraceRcvrX25DnaOutDefaultPathReliability_Type.__name__ = "Integer32"
_TraceRcvrX25DnaOutDefaultPathReliability_Object = MibTableColumn
traceRcvrX25DnaOutDefaultPathReliability = _TraceRcvrX25DnaOutDefaultPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 11, 1, 14),
    _TraceRcvrX25DnaOutDefaultPathReliability_Type()
)
traceRcvrX25DnaOutDefaultPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DnaOutDefaultPathReliability.setStatus("mandatory")


class _TraceRcvrX25DnaOutPathReliabilityOverRide_Type(Integer32):
    """Custom type traceRcvrX25DnaOutPathReliabilityOverRide based on Integer32"""
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


_TraceRcvrX25DnaOutPathReliabilityOverRide_Type.__name__ = "Integer32"
_TraceRcvrX25DnaOutPathReliabilityOverRide_Object = MibTableColumn
traceRcvrX25DnaOutPathReliabilityOverRide = _TraceRcvrX25DnaOutPathReliabilityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 11, 1, 15),
    _TraceRcvrX25DnaOutPathReliabilityOverRide_Type()
)
traceRcvrX25DnaOutPathReliabilityOverRide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DnaOutPathReliabilityOverRide.setStatus("mandatory")


class _TraceRcvrX25DnaOutPathReliabilitySignal_Type(Integer32):
    """Custom type traceRcvrX25DnaOutPathReliabilitySignal based on Integer32"""
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


_TraceRcvrX25DnaOutPathReliabilitySignal_Type.__name__ = "Integer32"
_TraceRcvrX25DnaOutPathReliabilitySignal_Object = MibTableColumn
traceRcvrX25DnaOutPathReliabilitySignal = _TraceRcvrX25DnaOutPathReliabilitySignal_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 11, 1, 16),
    _TraceRcvrX25DnaOutPathReliabilitySignal_Type()
)
traceRcvrX25DnaOutPathReliabilitySignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DnaOutPathReliabilitySignal.setStatus("mandatory")


class _TraceRcvrX25DnaOutAccess_Type(Integer32):
    """Custom type traceRcvrX25DnaOutAccess based on Integer32"""
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


_TraceRcvrX25DnaOutAccess_Type.__name__ = "Integer32"
_TraceRcvrX25DnaOutAccess_Object = MibTableColumn
traceRcvrX25DnaOutAccess = _TraceRcvrX25DnaOutAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 11, 1, 17),
    _TraceRcvrX25DnaOutAccess_Type()
)
traceRcvrX25DnaOutAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrX25DnaOutAccess.setStatus("mandatory")
_TraceRcvrX25DnaIncomingOptionsTable_Object = MibTable
traceRcvrX25DnaIncomingOptionsTable = _TraceRcvrX25DnaIncomingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 12)
)
if mibBuilder.loadTexts:
    traceRcvrX25DnaIncomingOptionsTable.setStatus("mandatory")
_TraceRcvrX25DnaIncomingOptionsEntry_Object = MibTableRow
traceRcvrX25DnaIncomingOptionsEntry = _TraceRcvrX25DnaIncomingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 12, 1)
)
traceRcvrX25DnaIncomingOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceRcvrIndex"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceRcvrX25Index"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceRcvrX25DnaIndex"),
)
if mibBuilder.loadTexts:
    traceRcvrX25DnaIncomingOptionsEntry.setStatus("mandatory")


class _TraceRcvrX25DnaIncCalls_Type(Integer32):
    """Custom type traceRcvrX25DnaIncCalls based on Integer32"""
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


_TraceRcvrX25DnaIncCalls_Type.__name__ = "Integer32"
_TraceRcvrX25DnaIncCalls_Object = MibTableColumn
traceRcvrX25DnaIncCalls = _TraceRcvrX25DnaIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 12, 1, 1),
    _TraceRcvrX25DnaIncCalls_Type()
)
traceRcvrX25DnaIncCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DnaIncCalls.setStatus("mandatory")
_TraceRcvrX25DnaCallOptionsTable_Object = MibTable
traceRcvrX25DnaCallOptionsTable = _TraceRcvrX25DnaCallOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 13)
)
if mibBuilder.loadTexts:
    traceRcvrX25DnaCallOptionsTable.setStatus("mandatory")
_TraceRcvrX25DnaCallOptionsEntry_Object = MibTableRow
traceRcvrX25DnaCallOptionsEntry = _TraceRcvrX25DnaCallOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 13, 1)
)
traceRcvrX25DnaCallOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceRcvrIndex"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceRcvrX25Index"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceRcvrX25DnaIndex"),
)
if mibBuilder.loadTexts:
    traceRcvrX25DnaCallOptionsEntry.setStatus("mandatory")


class _TraceRcvrX25DnaPacketSizes_Type(OctetString):
    """Custom type traceRcvrX25DnaPacketSizes based on OctetString"""
    defaultHexValue = "0100"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_TraceRcvrX25DnaPacketSizes_Type.__name__ = "OctetString"
_TraceRcvrX25DnaPacketSizes_Object = MibTableColumn
traceRcvrX25DnaPacketSizes = _TraceRcvrX25DnaPacketSizes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 13, 1, 2),
    _TraceRcvrX25DnaPacketSizes_Type()
)
traceRcvrX25DnaPacketSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DnaPacketSizes.setStatus("mandatory")


class _TraceRcvrX25DnaDefaultRecvFrmNetworkPacketSize_Type(Integer32):
    """Custom type traceRcvrX25DnaDefaultRecvFrmNetworkPacketSize based on Integer32"""
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


_TraceRcvrX25DnaDefaultRecvFrmNetworkPacketSize_Type.__name__ = "Integer32"
_TraceRcvrX25DnaDefaultRecvFrmNetworkPacketSize_Object = MibTableColumn
traceRcvrX25DnaDefaultRecvFrmNetworkPacketSize = _TraceRcvrX25DnaDefaultRecvFrmNetworkPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 13, 1, 3),
    _TraceRcvrX25DnaDefaultRecvFrmNetworkPacketSize_Type()
)
traceRcvrX25DnaDefaultRecvFrmNetworkPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DnaDefaultRecvFrmNetworkPacketSize.setStatus("mandatory")


class _TraceRcvrX25DnaDefaultSendToNetworkPacketSize_Type(Integer32):
    """Custom type traceRcvrX25DnaDefaultSendToNetworkPacketSize based on Integer32"""
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


_TraceRcvrX25DnaDefaultSendToNetworkPacketSize_Type.__name__ = "Integer32"
_TraceRcvrX25DnaDefaultSendToNetworkPacketSize_Object = MibTableColumn
traceRcvrX25DnaDefaultSendToNetworkPacketSize = _TraceRcvrX25DnaDefaultSendToNetworkPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 13, 1, 4),
    _TraceRcvrX25DnaDefaultSendToNetworkPacketSize_Type()
)
traceRcvrX25DnaDefaultSendToNetworkPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DnaDefaultSendToNetworkPacketSize.setStatus("mandatory")


class _TraceRcvrX25DnaDefaultRecvFrmNetworkThruputClass_Type(Unsigned32):
    """Custom type traceRcvrX25DnaDefaultRecvFrmNetworkThruputClass based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TraceRcvrX25DnaDefaultRecvFrmNetworkThruputClass_Type.__name__ = "Unsigned32"
_TraceRcvrX25DnaDefaultRecvFrmNetworkThruputClass_Object = MibTableColumn
traceRcvrX25DnaDefaultRecvFrmNetworkThruputClass = _TraceRcvrX25DnaDefaultRecvFrmNetworkThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 13, 1, 5),
    _TraceRcvrX25DnaDefaultRecvFrmNetworkThruputClass_Type()
)
traceRcvrX25DnaDefaultRecvFrmNetworkThruputClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrX25DnaDefaultRecvFrmNetworkThruputClass.setStatus("mandatory")


class _TraceRcvrX25DnaDefaultSendToNetworkThruputClass_Type(Unsigned32):
    """Custom type traceRcvrX25DnaDefaultSendToNetworkThruputClass based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TraceRcvrX25DnaDefaultSendToNetworkThruputClass_Type.__name__ = "Unsigned32"
_TraceRcvrX25DnaDefaultSendToNetworkThruputClass_Object = MibTableColumn
traceRcvrX25DnaDefaultSendToNetworkThruputClass = _TraceRcvrX25DnaDefaultSendToNetworkThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 13, 1, 6),
    _TraceRcvrX25DnaDefaultSendToNetworkThruputClass_Type()
)
traceRcvrX25DnaDefaultSendToNetworkThruputClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrX25DnaDefaultSendToNetworkThruputClass.setStatus("mandatory")


class _TraceRcvrX25DnaDefaultRecvFrmNetworkWindowSize_Type(Unsigned32):
    """Custom type traceRcvrX25DnaDefaultRecvFrmNetworkWindowSize based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TraceRcvrX25DnaDefaultRecvFrmNetworkWindowSize_Type.__name__ = "Unsigned32"
_TraceRcvrX25DnaDefaultRecvFrmNetworkWindowSize_Object = MibTableColumn
traceRcvrX25DnaDefaultRecvFrmNetworkWindowSize = _TraceRcvrX25DnaDefaultRecvFrmNetworkWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 13, 1, 7),
    _TraceRcvrX25DnaDefaultRecvFrmNetworkWindowSize_Type()
)
traceRcvrX25DnaDefaultRecvFrmNetworkWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DnaDefaultRecvFrmNetworkWindowSize.setStatus("mandatory")


class _TraceRcvrX25DnaDefaultSendToNetworkWindowSize_Type(Unsigned32):
    """Custom type traceRcvrX25DnaDefaultSendToNetworkWindowSize based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TraceRcvrX25DnaDefaultSendToNetworkWindowSize_Type.__name__ = "Unsigned32"
_TraceRcvrX25DnaDefaultSendToNetworkWindowSize_Object = MibTableColumn
traceRcvrX25DnaDefaultSendToNetworkWindowSize = _TraceRcvrX25DnaDefaultSendToNetworkWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 13, 1, 8),
    _TraceRcvrX25DnaDefaultSendToNetworkWindowSize_Type()
)
traceRcvrX25DnaDefaultSendToNetworkWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DnaDefaultSendToNetworkWindowSize.setStatus("mandatory")


class _TraceRcvrX25DnaPacketSizeNegotiation_Type(Integer32):
    """Custom type traceRcvrX25DnaPacketSizeNegotiation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("endToEnd", 0),
          ("local", 1))
    )


_TraceRcvrX25DnaPacketSizeNegotiation_Type.__name__ = "Integer32"
_TraceRcvrX25DnaPacketSizeNegotiation_Object = MibTableColumn
traceRcvrX25DnaPacketSizeNegotiation = _TraceRcvrX25DnaPacketSizeNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 13, 1, 9),
    _TraceRcvrX25DnaPacketSizeNegotiation_Type()
)
traceRcvrX25DnaPacketSizeNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DnaPacketSizeNegotiation.setStatus("mandatory")


class _TraceRcvrX25DnaCugFormat_Type(Integer32):
    """Custom type traceRcvrX25DnaCugFormat based on Integer32"""
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


_TraceRcvrX25DnaCugFormat_Type.__name__ = "Integer32"
_TraceRcvrX25DnaCugFormat_Object = MibTableColumn
traceRcvrX25DnaCugFormat = _TraceRcvrX25DnaCugFormat_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 2, 13, 1, 10),
    _TraceRcvrX25DnaCugFormat_Type()
)
traceRcvrX25DnaCugFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DnaCugFormat.setStatus("mandatory")
_TraceRcvrX25Dc_ObjectIdentity = ObjectIdentity
traceRcvrX25Dc = _TraceRcvrX25Dc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 3)
)
_TraceRcvrX25DcRowStatusTable_Object = MibTable
traceRcvrX25DcRowStatusTable = _TraceRcvrX25DcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    traceRcvrX25DcRowStatusTable.setStatus("mandatory")
_TraceRcvrX25DcRowStatusEntry_Object = MibTableRow
traceRcvrX25DcRowStatusEntry = _TraceRcvrX25DcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 3, 1, 1)
)
traceRcvrX25DcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceRcvrIndex"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceRcvrX25Index"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceRcvrX25DcIndex"),
)
if mibBuilder.loadTexts:
    traceRcvrX25DcRowStatusEntry.setStatus("mandatory")
_TraceRcvrX25DcRowStatus_Type = RowStatus
_TraceRcvrX25DcRowStatus_Object = MibTableColumn
traceRcvrX25DcRowStatus = _TraceRcvrX25DcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 3, 1, 1, 1),
    _TraceRcvrX25DcRowStatus_Type()
)
traceRcvrX25DcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DcRowStatus.setStatus("mandatory")
_TraceRcvrX25DcComponentName_Type = DisplayString
_TraceRcvrX25DcComponentName_Object = MibTableColumn
traceRcvrX25DcComponentName = _TraceRcvrX25DcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 3, 1, 1, 2),
    _TraceRcvrX25DcComponentName_Type()
)
traceRcvrX25DcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DcComponentName.setStatus("mandatory")
_TraceRcvrX25DcStorageType_Type = StorageType
_TraceRcvrX25DcStorageType_Object = MibTableColumn
traceRcvrX25DcStorageType = _TraceRcvrX25DcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 3, 1, 1, 4),
    _TraceRcvrX25DcStorageType_Type()
)
traceRcvrX25DcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DcStorageType.setStatus("mandatory")
_TraceRcvrX25DcIndex_Type = NonReplicated
_TraceRcvrX25DcIndex_Object = MibTableColumn
traceRcvrX25DcIndex = _TraceRcvrX25DcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 3, 1, 1, 10),
    _TraceRcvrX25DcIndex_Type()
)
traceRcvrX25DcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceRcvrX25DcIndex.setStatus("mandatory")
_TraceRcvrX25DcOptionsTable_Object = MibTable
traceRcvrX25DcOptionsTable = _TraceRcvrX25DcOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 3, 10)
)
if mibBuilder.loadTexts:
    traceRcvrX25DcOptionsTable.setStatus("mandatory")
_TraceRcvrX25DcOptionsEntry_Object = MibTableRow
traceRcvrX25DcOptionsEntry = _TraceRcvrX25DcOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 3, 10, 1)
)
traceRcvrX25DcOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceRcvrIndex"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceRcvrX25Index"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceRcvrX25DcIndex"),
)
if mibBuilder.loadTexts:
    traceRcvrX25DcOptionsEntry.setStatus("mandatory")


class _TraceRcvrX25DcRemoteNpi_Type(Integer32):
    """Custom type traceRcvrX25DcRemoteNpi based on Integer32"""
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


_TraceRcvrX25DcRemoteNpi_Type.__name__ = "Integer32"
_TraceRcvrX25DcRemoteNpi_Object = MibTableColumn
traceRcvrX25DcRemoteNpi = _TraceRcvrX25DcRemoteNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 3, 10, 1, 3),
    _TraceRcvrX25DcRemoteNpi_Type()
)
traceRcvrX25DcRemoteNpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrX25DcRemoteNpi.setStatus("mandatory")


class _TraceRcvrX25DcRemoteDna_Type(DigitString):
    """Custom type traceRcvrX25DcRemoteDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_TraceRcvrX25DcRemoteDna_Type.__name__ = "DigitString"
_TraceRcvrX25DcRemoteDna_Object = MibTableColumn
traceRcvrX25DcRemoteDna = _TraceRcvrX25DcRemoteDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 3, 10, 1, 4),
    _TraceRcvrX25DcRemoteDna_Type()
)
traceRcvrX25DcRemoteDna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrX25DcRemoteDna.setStatus("mandatory")


class _TraceRcvrX25DcType_Type(Integer32):
    """Custom type traceRcvrX25DcType based on Integer32"""
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


_TraceRcvrX25DcType_Type.__name__ = "Integer32"
_TraceRcvrX25DcType_Object = MibTableColumn
traceRcvrX25DcType = _TraceRcvrX25DcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 3, 10, 1, 6),
    _TraceRcvrX25DcType_Type()
)
traceRcvrX25DcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrX25DcType.setStatus("mandatory")


class _TraceRcvrX25DcUserData_Type(HexString):
    """Custom type traceRcvrX25DcUserData based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TraceRcvrX25DcUserData_Type.__name__ = "HexString"
_TraceRcvrX25DcUserData_Object = MibTableColumn
traceRcvrX25DcUserData = _TraceRcvrX25DcUserData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 2, 3, 10, 1, 8),
    _TraceRcvrX25DcUserData_Type()
)
traceRcvrX25DcUserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrX25DcUserData.setStatus("mandatory")
_TraceSessionX25_ObjectIdentity = ObjectIdentity
traceSessionX25 = _TraceSessionX25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2)
)
_TraceSessionX25RowStatusTable_Object = MibTable
traceSessionX25RowStatusTable = _TraceSessionX25RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 1)
)
if mibBuilder.loadTexts:
    traceSessionX25RowStatusTable.setStatus("mandatory")
_TraceSessionX25RowStatusEntry_Object = MibTableRow
traceSessionX25RowStatusEntry = _TraceSessionX25RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 1, 1)
)
traceSessionX25RowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceSessionIndex"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceSessionX25Index"),
)
if mibBuilder.loadTexts:
    traceSessionX25RowStatusEntry.setStatus("mandatory")
_TraceSessionX25RowStatus_Type = RowStatus
_TraceSessionX25RowStatus_Object = MibTableColumn
traceSessionX25RowStatus = _TraceSessionX25RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 1, 1, 1),
    _TraceSessionX25RowStatus_Type()
)
traceSessionX25RowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25RowStatus.setStatus("mandatory")
_TraceSessionX25ComponentName_Type = DisplayString
_TraceSessionX25ComponentName_Object = MibTableColumn
traceSessionX25ComponentName = _TraceSessionX25ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 1, 1, 2),
    _TraceSessionX25ComponentName_Type()
)
traceSessionX25ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25ComponentName.setStatus("mandatory")
_TraceSessionX25StorageType_Type = StorageType
_TraceSessionX25StorageType_Object = MibTableColumn
traceSessionX25StorageType = _TraceSessionX25StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 1, 1, 4),
    _TraceSessionX25StorageType_Type()
)
traceSessionX25StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25StorageType.setStatus("mandatory")
_TraceSessionX25Index_Type = NonReplicated
_TraceSessionX25Index_Object = MibTableColumn
traceSessionX25Index = _TraceSessionX25Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 1, 1, 10),
    _TraceSessionX25Index_Type()
)
traceSessionX25Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceSessionX25Index.setStatus("mandatory")
_TraceSessionX25Vc_ObjectIdentity = ObjectIdentity
traceSessionX25Vc = _TraceSessionX25Vc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2)
)
_TraceSessionX25VcRowStatusTable_Object = MibTable
traceSessionX25VcRowStatusTable = _TraceSessionX25VcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    traceSessionX25VcRowStatusTable.setStatus("mandatory")
_TraceSessionX25VcRowStatusEntry_Object = MibTableRow
traceSessionX25VcRowStatusEntry = _TraceSessionX25VcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 1, 1)
)
traceSessionX25VcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceSessionIndex"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceSessionX25Index"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceSessionX25VcIndex"),
)
if mibBuilder.loadTexts:
    traceSessionX25VcRowStatusEntry.setStatus("mandatory")
_TraceSessionX25VcRowStatus_Type = RowStatus
_TraceSessionX25VcRowStatus_Object = MibTableColumn
traceSessionX25VcRowStatus = _TraceSessionX25VcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 1, 1, 1),
    _TraceSessionX25VcRowStatus_Type()
)
traceSessionX25VcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcRowStatus.setStatus("mandatory")
_TraceSessionX25VcComponentName_Type = DisplayString
_TraceSessionX25VcComponentName_Object = MibTableColumn
traceSessionX25VcComponentName = _TraceSessionX25VcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 1, 1, 2),
    _TraceSessionX25VcComponentName_Type()
)
traceSessionX25VcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcComponentName.setStatus("mandatory")
_TraceSessionX25VcStorageType_Type = StorageType
_TraceSessionX25VcStorageType_Object = MibTableColumn
traceSessionX25VcStorageType = _TraceSessionX25VcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 1, 1, 4),
    _TraceSessionX25VcStorageType_Type()
)
traceSessionX25VcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcStorageType.setStatus("mandatory")
_TraceSessionX25VcIndex_Type = NonReplicated
_TraceSessionX25VcIndex_Object = MibTableColumn
traceSessionX25VcIndex = _TraceSessionX25VcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 1, 1, 10),
    _TraceSessionX25VcIndex_Type()
)
traceSessionX25VcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceSessionX25VcIndex.setStatus("mandatory")
_TraceSessionX25VcCadTable_Object = MibTable
traceSessionX25VcCadTable = _TraceSessionX25VcCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10)
)
if mibBuilder.loadTexts:
    traceSessionX25VcCadTable.setStatus("mandatory")
_TraceSessionX25VcCadEntry_Object = MibTableRow
traceSessionX25VcCadEntry = _TraceSessionX25VcCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1)
)
traceSessionX25VcCadEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceSessionIndex"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceSessionX25Index"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceSessionX25VcIndex"),
)
if mibBuilder.loadTexts:
    traceSessionX25VcCadEntry.setStatus("mandatory")


class _TraceSessionX25VcType_Type(Integer32):
    """Custom type traceSessionX25VcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 0))
    )


_TraceSessionX25VcType_Type.__name__ = "Integer32"
_TraceSessionX25VcType_Object = MibTableColumn
traceSessionX25VcType = _TraceSessionX25VcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 1),
    _TraceSessionX25VcType_Type()
)
traceSessionX25VcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcType.setStatus("mandatory")


class _TraceSessionX25VcState_Type(Integer32):
    """Custom type traceSessionX25VcState based on Integer32"""
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


_TraceSessionX25VcState_Type.__name__ = "Integer32"
_TraceSessionX25VcState_Object = MibTableColumn
traceSessionX25VcState = _TraceSessionX25VcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 2),
    _TraceSessionX25VcState_Type()
)
traceSessionX25VcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcState.setStatus("mandatory")


class _TraceSessionX25VcPreviousState_Type(Integer32):
    """Custom type traceSessionX25VcPreviousState based on Integer32"""
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


_TraceSessionX25VcPreviousState_Type.__name__ = "Integer32"
_TraceSessionX25VcPreviousState_Object = MibTableColumn
traceSessionX25VcPreviousState = _TraceSessionX25VcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 3),
    _TraceSessionX25VcPreviousState_Type()
)
traceSessionX25VcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcPreviousState.setStatus("mandatory")


class _TraceSessionX25VcDiagnosticCode_Type(Unsigned32):
    """Custom type traceSessionX25VcDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TraceSessionX25VcDiagnosticCode_Type.__name__ = "Unsigned32"
_TraceSessionX25VcDiagnosticCode_Object = MibTableColumn
traceSessionX25VcDiagnosticCode = _TraceSessionX25VcDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 4),
    _TraceSessionX25VcDiagnosticCode_Type()
)
traceSessionX25VcDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcDiagnosticCode.setStatus("mandatory")


class _TraceSessionX25VcPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type traceSessionX25VcPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TraceSessionX25VcPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_TraceSessionX25VcPreviousDiagnosticCode_Object = MibTableColumn
traceSessionX25VcPreviousDiagnosticCode = _TraceSessionX25VcPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 5),
    _TraceSessionX25VcPreviousDiagnosticCode_Type()
)
traceSessionX25VcPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcPreviousDiagnosticCode.setStatus("mandatory")


class _TraceSessionX25VcCalledNpi_Type(Integer32):
    """Custom type traceSessionX25VcCalledNpi based on Integer32"""
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


_TraceSessionX25VcCalledNpi_Type.__name__ = "Integer32"
_TraceSessionX25VcCalledNpi_Object = MibTableColumn
traceSessionX25VcCalledNpi = _TraceSessionX25VcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 6),
    _TraceSessionX25VcCalledNpi_Type()
)
traceSessionX25VcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcCalledNpi.setStatus("mandatory")


class _TraceSessionX25VcCalledDna_Type(DigitString):
    """Custom type traceSessionX25VcCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_TraceSessionX25VcCalledDna_Type.__name__ = "DigitString"
_TraceSessionX25VcCalledDna_Object = MibTableColumn
traceSessionX25VcCalledDna = _TraceSessionX25VcCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 7),
    _TraceSessionX25VcCalledDna_Type()
)
traceSessionX25VcCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcCalledDna.setStatus("mandatory")


class _TraceSessionX25VcCalledLcn_Type(Unsigned32):
    """Custom type traceSessionX25VcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TraceSessionX25VcCalledLcn_Type.__name__ = "Unsigned32"
_TraceSessionX25VcCalledLcn_Object = MibTableColumn
traceSessionX25VcCalledLcn = _TraceSessionX25VcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 8),
    _TraceSessionX25VcCalledLcn_Type()
)
traceSessionX25VcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcCalledLcn.setStatus("mandatory")


class _TraceSessionX25VcCallingNpi_Type(Integer32):
    """Custom type traceSessionX25VcCallingNpi based on Integer32"""
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


_TraceSessionX25VcCallingNpi_Type.__name__ = "Integer32"
_TraceSessionX25VcCallingNpi_Object = MibTableColumn
traceSessionX25VcCallingNpi = _TraceSessionX25VcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 9),
    _TraceSessionX25VcCallingNpi_Type()
)
traceSessionX25VcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcCallingNpi.setStatus("mandatory")


class _TraceSessionX25VcCallingDna_Type(DigitString):
    """Custom type traceSessionX25VcCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_TraceSessionX25VcCallingDna_Type.__name__ = "DigitString"
_TraceSessionX25VcCallingDna_Object = MibTableColumn
traceSessionX25VcCallingDna = _TraceSessionX25VcCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 10),
    _TraceSessionX25VcCallingDna_Type()
)
traceSessionX25VcCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcCallingDna.setStatus("mandatory")


class _TraceSessionX25VcCallingLcn_Type(Unsigned32):
    """Custom type traceSessionX25VcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TraceSessionX25VcCallingLcn_Type.__name__ = "Unsigned32"
_TraceSessionX25VcCallingLcn_Object = MibTableColumn
traceSessionX25VcCallingLcn = _TraceSessionX25VcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 11),
    _TraceSessionX25VcCallingLcn_Type()
)
traceSessionX25VcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcCallingLcn.setStatus("mandatory")


class _TraceSessionX25VcAccountingEnabled_Type(Integer32):
    """Custom type traceSessionX25VcAccountingEnabled based on Integer32"""
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


_TraceSessionX25VcAccountingEnabled_Type.__name__ = "Integer32"
_TraceSessionX25VcAccountingEnabled_Object = MibTableColumn
traceSessionX25VcAccountingEnabled = _TraceSessionX25VcAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 12),
    _TraceSessionX25VcAccountingEnabled_Type()
)
traceSessionX25VcAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcAccountingEnabled.setStatus("mandatory")


class _TraceSessionX25VcFastSelectCall_Type(Integer32):
    """Custom type traceSessionX25VcFastSelectCall based on Integer32"""
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


_TraceSessionX25VcFastSelectCall_Type.__name__ = "Integer32"
_TraceSessionX25VcFastSelectCall_Object = MibTableColumn
traceSessionX25VcFastSelectCall = _TraceSessionX25VcFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 13),
    _TraceSessionX25VcFastSelectCall_Type()
)
traceSessionX25VcFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcFastSelectCall.setStatus("mandatory")


class _TraceSessionX25VcLocalRxPktSize_Type(Integer32):
    """Custom type traceSessionX25VcLocalRxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
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
          ("n64", 6),
          ("unknown", 0))
    )


_TraceSessionX25VcLocalRxPktSize_Type.__name__ = "Integer32"
_TraceSessionX25VcLocalRxPktSize_Object = MibTableColumn
traceSessionX25VcLocalRxPktSize = _TraceSessionX25VcLocalRxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 14),
    _TraceSessionX25VcLocalRxPktSize_Type()
)
traceSessionX25VcLocalRxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcLocalRxPktSize.setStatus("mandatory")


class _TraceSessionX25VcLocalTxPktSize_Type(Integer32):
    """Custom type traceSessionX25VcLocalTxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
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
          ("n64", 6),
          ("unknown", 0))
    )


_TraceSessionX25VcLocalTxPktSize_Type.__name__ = "Integer32"
_TraceSessionX25VcLocalTxPktSize_Object = MibTableColumn
traceSessionX25VcLocalTxPktSize = _TraceSessionX25VcLocalTxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 15),
    _TraceSessionX25VcLocalTxPktSize_Type()
)
traceSessionX25VcLocalTxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcLocalTxPktSize.setStatus("mandatory")


class _TraceSessionX25VcLocalTxWindowSize_Type(Unsigned32):
    """Custom type traceSessionX25VcLocalTxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TraceSessionX25VcLocalTxWindowSize_Type.__name__ = "Unsigned32"
_TraceSessionX25VcLocalTxWindowSize_Object = MibTableColumn
traceSessionX25VcLocalTxWindowSize = _TraceSessionX25VcLocalTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 16),
    _TraceSessionX25VcLocalTxWindowSize_Type()
)
traceSessionX25VcLocalTxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcLocalTxWindowSize.setStatus("mandatory")


class _TraceSessionX25VcLocalRxWindowSize_Type(Unsigned32):
    """Custom type traceSessionX25VcLocalRxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TraceSessionX25VcLocalRxWindowSize_Type.__name__ = "Unsigned32"
_TraceSessionX25VcLocalRxWindowSize_Object = MibTableColumn
traceSessionX25VcLocalRxWindowSize = _TraceSessionX25VcLocalRxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 17),
    _TraceSessionX25VcLocalRxWindowSize_Type()
)
traceSessionX25VcLocalRxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcLocalRxWindowSize.setStatus("mandatory")


class _TraceSessionX25VcPathReliability_Type(Integer32):
    """Custom type traceSessionX25VcPathReliability based on Integer32"""
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


_TraceSessionX25VcPathReliability_Type.__name__ = "Integer32"
_TraceSessionX25VcPathReliability_Object = MibTableColumn
traceSessionX25VcPathReliability = _TraceSessionX25VcPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 19),
    _TraceSessionX25VcPathReliability_Type()
)
traceSessionX25VcPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcPathReliability.setStatus("mandatory")


class _TraceSessionX25VcAccountingEnd_Type(Integer32):
    """Custom type traceSessionX25VcAccountingEnd based on Integer32"""
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


_TraceSessionX25VcAccountingEnd_Type.__name__ = "Integer32"
_TraceSessionX25VcAccountingEnd_Object = MibTableColumn
traceSessionX25VcAccountingEnd = _TraceSessionX25VcAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 20),
    _TraceSessionX25VcAccountingEnd_Type()
)
traceSessionX25VcAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcAccountingEnd.setStatus("mandatory")


class _TraceSessionX25VcPriority_Type(Integer32):
    """Custom type traceSessionX25VcPriority based on Integer32"""
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


_TraceSessionX25VcPriority_Type.__name__ = "Integer32"
_TraceSessionX25VcPriority_Object = MibTableColumn
traceSessionX25VcPriority = _TraceSessionX25VcPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 21),
    _TraceSessionX25VcPriority_Type()
)
traceSessionX25VcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcPriority.setStatus("mandatory")


class _TraceSessionX25VcSegmentSize_Type(Unsigned32):
    """Custom type traceSessionX25VcSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TraceSessionX25VcSegmentSize_Type.__name__ = "Unsigned32"
_TraceSessionX25VcSegmentSize_Object = MibTableColumn
traceSessionX25VcSegmentSize = _TraceSessionX25VcSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 22),
    _TraceSessionX25VcSegmentSize_Type()
)
traceSessionX25VcSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcSegmentSize.setStatus("mandatory")


class _TraceSessionX25VcSubnetTxPktSize_Type(Integer32):
    """Custom type traceSessionX25VcSubnetTxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
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
          ("n64", 6),
          ("unknown", 0))
    )


_TraceSessionX25VcSubnetTxPktSize_Type.__name__ = "Integer32"
_TraceSessionX25VcSubnetTxPktSize_Object = MibTableColumn
traceSessionX25VcSubnetTxPktSize = _TraceSessionX25VcSubnetTxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 23),
    _TraceSessionX25VcSubnetTxPktSize_Type()
)
traceSessionX25VcSubnetTxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcSubnetTxPktSize.setStatus("mandatory")


class _TraceSessionX25VcSubnetTxWindowSize_Type(Unsigned32):
    """Custom type traceSessionX25VcSubnetTxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TraceSessionX25VcSubnetTxWindowSize_Type.__name__ = "Unsigned32"
_TraceSessionX25VcSubnetTxWindowSize_Object = MibTableColumn
traceSessionX25VcSubnetTxWindowSize = _TraceSessionX25VcSubnetTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 24),
    _TraceSessionX25VcSubnetTxWindowSize_Type()
)
traceSessionX25VcSubnetTxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcSubnetTxWindowSize.setStatus("mandatory")


class _TraceSessionX25VcSubnetRxPktSize_Type(Integer32):
    """Custom type traceSessionX25VcSubnetRxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
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
          ("n64", 6),
          ("unknown", 0))
    )


_TraceSessionX25VcSubnetRxPktSize_Type.__name__ = "Integer32"
_TraceSessionX25VcSubnetRxPktSize_Object = MibTableColumn
traceSessionX25VcSubnetRxPktSize = _TraceSessionX25VcSubnetRxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 25),
    _TraceSessionX25VcSubnetRxPktSize_Type()
)
traceSessionX25VcSubnetRxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcSubnetRxPktSize.setStatus("mandatory")


class _TraceSessionX25VcSubnetRxWindowSize_Type(Unsigned32):
    """Custom type traceSessionX25VcSubnetRxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TraceSessionX25VcSubnetRxWindowSize_Type.__name__ = "Unsigned32"
_TraceSessionX25VcSubnetRxWindowSize_Object = MibTableColumn
traceSessionX25VcSubnetRxWindowSize = _TraceSessionX25VcSubnetRxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 26),
    _TraceSessionX25VcSubnetRxWindowSize_Type()
)
traceSessionX25VcSubnetRxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcSubnetRxWindowSize.setStatus("mandatory")


class _TraceSessionX25VcMaxSubnetPktSize_Type(Unsigned32):
    """Custom type traceSessionX25VcMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TraceSessionX25VcMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_TraceSessionX25VcMaxSubnetPktSize_Object = MibTableColumn
traceSessionX25VcMaxSubnetPktSize = _TraceSessionX25VcMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 27),
    _TraceSessionX25VcMaxSubnetPktSize_Type()
)
traceSessionX25VcMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcMaxSubnetPktSize.setStatus("mandatory")


class _TraceSessionX25VcTransferPriorityToNetwork_Type(Integer32):
    """Custom type traceSessionX25VcTransferPriorityToNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9)
        )
    )
    namedValues = NamedValues(
        *(("high", 9),
          ("normal", 0))
    )


_TraceSessionX25VcTransferPriorityToNetwork_Type.__name__ = "Integer32"
_TraceSessionX25VcTransferPriorityToNetwork_Object = MibTableColumn
traceSessionX25VcTransferPriorityToNetwork = _TraceSessionX25VcTransferPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 28),
    _TraceSessionX25VcTransferPriorityToNetwork_Type()
)
traceSessionX25VcTransferPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcTransferPriorityToNetwork.setStatus("mandatory")


class _TraceSessionX25VcTransferPriorityFromNetwork_Type(Integer32):
    """Custom type traceSessionX25VcTransferPriorityFromNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9)
        )
    )
    namedValues = NamedValues(
        *(("high", 9),
          ("normal", 0))
    )


_TraceSessionX25VcTransferPriorityFromNetwork_Type.__name__ = "Integer32"
_TraceSessionX25VcTransferPriorityFromNetwork_Object = MibTableColumn
traceSessionX25VcTransferPriorityFromNetwork = _TraceSessionX25VcTransferPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 10, 1, 29),
    _TraceSessionX25VcTransferPriorityFromNetwork_Type()
)
traceSessionX25VcTransferPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcTransferPriorityFromNetwork.setStatus("mandatory")
_TraceSessionX25VcIntdTable_Object = MibTable
traceSessionX25VcIntdTable = _TraceSessionX25VcIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 11)
)
if mibBuilder.loadTexts:
    traceSessionX25VcIntdTable.setStatus("mandatory")
_TraceSessionX25VcIntdEntry_Object = MibTableRow
traceSessionX25VcIntdEntry = _TraceSessionX25VcIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 11, 1)
)
traceSessionX25VcIntdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceSessionIndex"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceSessionX25Index"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceSessionX25VcIndex"),
)
if mibBuilder.loadTexts:
    traceSessionX25VcIntdEntry.setStatus("mandatory")


class _TraceSessionX25VcCallReferenceNumber_Type(Hex):
    """Custom type traceSessionX25VcCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TraceSessionX25VcCallReferenceNumber_Type.__name__ = "Hex"
_TraceSessionX25VcCallReferenceNumber_Object = MibTableColumn
traceSessionX25VcCallReferenceNumber = _TraceSessionX25VcCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 11, 1, 1),
    _TraceSessionX25VcCallReferenceNumber_Type()
)
traceSessionX25VcCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcCallReferenceNumber.setStatus("mandatory")


class _TraceSessionX25VcElapsedTimeTillNow_Type(Unsigned32):
    """Custom type traceSessionX25VcElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TraceSessionX25VcElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_TraceSessionX25VcElapsedTimeTillNow_Object = MibTableColumn
traceSessionX25VcElapsedTimeTillNow = _TraceSessionX25VcElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 11, 1, 2),
    _TraceSessionX25VcElapsedTimeTillNow_Type()
)
traceSessionX25VcElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcElapsedTimeTillNow.setStatus("mandatory")


class _TraceSessionX25VcSegmentsRx_Type(Unsigned32):
    """Custom type traceSessionX25VcSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TraceSessionX25VcSegmentsRx_Type.__name__ = "Unsigned32"
_TraceSessionX25VcSegmentsRx_Object = MibTableColumn
traceSessionX25VcSegmentsRx = _TraceSessionX25VcSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 11, 1, 3),
    _TraceSessionX25VcSegmentsRx_Type()
)
traceSessionX25VcSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcSegmentsRx.setStatus("mandatory")


class _TraceSessionX25VcSegmentsSent_Type(Unsigned32):
    """Custom type traceSessionX25VcSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TraceSessionX25VcSegmentsSent_Type.__name__ = "Unsigned32"
_TraceSessionX25VcSegmentsSent_Object = MibTableColumn
traceSessionX25VcSegmentsSent = _TraceSessionX25VcSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 11, 1, 4),
    _TraceSessionX25VcSegmentsSent_Type()
)
traceSessionX25VcSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcSegmentsSent.setStatus("mandatory")


class _TraceSessionX25VcStartTime_Type(EnterpriseDateAndTime):
    """Custom type traceSessionX25VcStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_TraceSessionX25VcStartTime_Type.__name__ = "EnterpriseDateAndTime"
_TraceSessionX25VcStartTime_Object = MibTableColumn
traceSessionX25VcStartTime = _TraceSessionX25VcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 11, 1, 5),
    _TraceSessionX25VcStartTime_Type()
)
traceSessionX25VcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcStartTime.setStatus("mandatory")
_TraceSessionX25VcStatsTable_Object = MibTable
traceSessionX25VcStatsTable = _TraceSessionX25VcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 12)
)
if mibBuilder.loadTexts:
    traceSessionX25VcStatsTable.setStatus("mandatory")
_TraceSessionX25VcStatsEntry_Object = MibTableRow
traceSessionX25VcStatsEntry = _TraceSessionX25VcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 12, 1)
)
traceSessionX25VcStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceSessionIndex"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceSessionX25Index"),
    (0, "Nortel-Magellan-Passport-X25TraceRcvrMIB", "traceSessionX25VcIndex"),
)
if mibBuilder.loadTexts:
    traceSessionX25VcStatsEntry.setStatus("mandatory")


class _TraceSessionX25VcAckStackingTimeouts_Type(Unsigned32):
    """Custom type traceSessionX25VcAckStackingTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionX25VcAckStackingTimeouts_Type.__name__ = "Unsigned32"
_TraceSessionX25VcAckStackingTimeouts_Object = MibTableColumn
traceSessionX25VcAckStackingTimeouts = _TraceSessionX25VcAckStackingTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 12, 1, 1),
    _TraceSessionX25VcAckStackingTimeouts_Type()
)
traceSessionX25VcAckStackingTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcAckStackingTimeouts.setStatus("mandatory")


class _TraceSessionX25VcOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type traceSessionX25VcOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionX25VcOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_TraceSessionX25VcOutOfRangeFrmFromSubnet_Object = MibTableColumn
traceSessionX25VcOutOfRangeFrmFromSubnet = _TraceSessionX25VcOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 12, 1, 2),
    _TraceSessionX25VcOutOfRangeFrmFromSubnet_Type()
)
traceSessionX25VcOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _TraceSessionX25VcDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type traceSessionX25VcDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionX25VcDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_TraceSessionX25VcDuplicatesFromSubnet_Object = MibTableColumn
traceSessionX25VcDuplicatesFromSubnet = _TraceSessionX25VcDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 12, 1, 3),
    _TraceSessionX25VcDuplicatesFromSubnet_Type()
)
traceSessionX25VcDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcDuplicatesFromSubnet.setStatus("mandatory")


class _TraceSessionX25VcFrmRetryTimeouts_Type(Unsigned32):
    """Custom type traceSessionX25VcFrmRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionX25VcFrmRetryTimeouts_Type.__name__ = "Unsigned32"
_TraceSessionX25VcFrmRetryTimeouts_Object = MibTableColumn
traceSessionX25VcFrmRetryTimeouts = _TraceSessionX25VcFrmRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 12, 1, 4),
    _TraceSessionX25VcFrmRetryTimeouts_Type()
)
traceSessionX25VcFrmRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcFrmRetryTimeouts.setStatus("mandatory")


class _TraceSessionX25VcPeakRetryQueueSize_Type(Unsigned32):
    """Custom type traceSessionX25VcPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionX25VcPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_TraceSessionX25VcPeakRetryQueueSize_Object = MibTableColumn
traceSessionX25VcPeakRetryQueueSize = _TraceSessionX25VcPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 12, 1, 5),
    _TraceSessionX25VcPeakRetryQueueSize_Type()
)
traceSessionX25VcPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcPeakRetryQueueSize.setStatus("mandatory")


class _TraceSessionX25VcPeakOoSeqQueueSize_Type(Unsigned32):
    """Custom type traceSessionX25VcPeakOoSeqQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionX25VcPeakOoSeqQueueSize_Type.__name__ = "Unsigned32"
_TraceSessionX25VcPeakOoSeqQueueSize_Object = MibTableColumn
traceSessionX25VcPeakOoSeqQueueSize = _TraceSessionX25VcPeakOoSeqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 12, 1, 6),
    _TraceSessionX25VcPeakOoSeqQueueSize_Type()
)
traceSessionX25VcPeakOoSeqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcPeakOoSeqQueueSize.setStatus("mandatory")


class _TraceSessionX25VcPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type traceSessionX25VcPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionX25VcPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_TraceSessionX25VcPeakOoSeqFrmForwarded_Object = MibTableColumn
traceSessionX25VcPeakOoSeqFrmForwarded = _TraceSessionX25VcPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 12, 1, 7),
    _TraceSessionX25VcPeakOoSeqFrmForwarded_Type()
)
traceSessionX25VcPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcPeakOoSeqFrmForwarded.setStatus("mandatory")


class _TraceSessionX25VcPeakStackedAcksRx_Type(Unsigned32):
    """Custom type traceSessionX25VcPeakStackedAcksRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionX25VcPeakStackedAcksRx_Type.__name__ = "Unsigned32"
_TraceSessionX25VcPeakStackedAcksRx_Object = MibTableColumn
traceSessionX25VcPeakStackedAcksRx = _TraceSessionX25VcPeakStackedAcksRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 12, 1, 8),
    _TraceSessionX25VcPeakStackedAcksRx_Type()
)
traceSessionX25VcPeakStackedAcksRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcPeakStackedAcksRx.setStatus("mandatory")


class _TraceSessionX25VcSubnetRecoveries_Type(Unsigned32):
    """Custom type traceSessionX25VcSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionX25VcSubnetRecoveries_Type.__name__ = "Unsigned32"
_TraceSessionX25VcSubnetRecoveries_Object = MibTableColumn
traceSessionX25VcSubnetRecoveries = _TraceSessionX25VcSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 12, 1, 9),
    _TraceSessionX25VcSubnetRecoveries_Type()
)
traceSessionX25VcSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcSubnetRecoveries.setStatus("mandatory")


class _TraceSessionX25VcWindowClosuresToSubnet_Type(Unsigned32):
    """Custom type traceSessionX25VcWindowClosuresToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionX25VcWindowClosuresToSubnet_Type.__name__ = "Unsigned32"
_TraceSessionX25VcWindowClosuresToSubnet_Object = MibTableColumn
traceSessionX25VcWindowClosuresToSubnet = _TraceSessionX25VcWindowClosuresToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 12, 1, 10),
    _TraceSessionX25VcWindowClosuresToSubnet_Type()
)
traceSessionX25VcWindowClosuresToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcWindowClosuresToSubnet.setStatus("mandatory")


class _TraceSessionX25VcWindowClosuresFromSubnet_Type(Unsigned32):
    """Custom type traceSessionX25VcWindowClosuresFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionX25VcWindowClosuresFromSubnet_Type.__name__ = "Unsigned32"
_TraceSessionX25VcWindowClosuresFromSubnet_Object = MibTableColumn
traceSessionX25VcWindowClosuresFromSubnet = _TraceSessionX25VcWindowClosuresFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 12, 1, 11),
    _TraceSessionX25VcWindowClosuresFromSubnet_Type()
)
traceSessionX25VcWindowClosuresFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcWindowClosuresFromSubnet.setStatus("mandatory")


class _TraceSessionX25VcWrTriggers_Type(Unsigned32):
    """Custom type traceSessionX25VcWrTriggers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TraceSessionX25VcWrTriggers_Type.__name__ = "Unsigned32"
_TraceSessionX25VcWrTriggers_Object = MibTableColumn
traceSessionX25VcWrTriggers = _TraceSessionX25VcWrTriggers_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 2, 2, 12, 1, 12),
    _TraceSessionX25VcWrTriggers_Type()
)
traceSessionX25VcWrTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionX25VcWrTriggers.setStatus("mandatory")
_X25TraceRcvrMIB_ObjectIdentity = ObjectIdentity
x25TraceRcvrMIB = _X25TraceRcvrMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 62)
)
_X25TraceRcvrGroup_ObjectIdentity = ObjectIdentity
x25TraceRcvrGroup = _X25TraceRcvrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 62, 1)
)
_X25TraceRcvrGroupBD_ObjectIdentity = ObjectIdentity
x25TraceRcvrGroupBD = _X25TraceRcvrGroupBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 62, 1, 4)
)
_X25TraceRcvrGroupBD00_ObjectIdentity = ObjectIdentity
x25TraceRcvrGroupBD00 = _X25TraceRcvrGroupBD00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 62, 1, 4, 1)
)
_X25TraceRcvrGroupBD00A_ObjectIdentity = ObjectIdentity
x25TraceRcvrGroupBD00A = _X25TraceRcvrGroupBD00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 62, 1, 4, 1, 2)
)
_X25TraceRcvrCapabilities_ObjectIdentity = ObjectIdentity
x25TraceRcvrCapabilities = _X25TraceRcvrCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 62, 3)
)
_X25TraceRcvrCapabilitiesBD_ObjectIdentity = ObjectIdentity
x25TraceRcvrCapabilitiesBD = _X25TraceRcvrCapabilitiesBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 62, 3, 4)
)
_X25TraceRcvrCapabilitiesBD00_ObjectIdentity = ObjectIdentity
x25TraceRcvrCapabilitiesBD00 = _X25TraceRcvrCapabilitiesBD00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 62, 3, 4, 1)
)
_X25TraceRcvrCapabilitiesBD00A_ObjectIdentity = ObjectIdentity
x25TraceRcvrCapabilitiesBD00A = _X25TraceRcvrCapabilitiesBD00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 62, 3, 4, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-X25TraceRcvrMIB",
    **{"traceRcvrX25": traceRcvrX25,
       "traceRcvrX25RowStatusTable": traceRcvrX25RowStatusTable,
       "traceRcvrX25RowStatusEntry": traceRcvrX25RowStatusEntry,
       "traceRcvrX25RowStatus": traceRcvrX25RowStatus,
       "traceRcvrX25ComponentName": traceRcvrX25ComponentName,
       "traceRcvrX25StorageType": traceRcvrX25StorageType,
       "traceRcvrX25Index": traceRcvrX25Index,
       "traceRcvrX25Dna": traceRcvrX25Dna,
       "traceRcvrX25DnaRowStatusTable": traceRcvrX25DnaRowStatusTable,
       "traceRcvrX25DnaRowStatusEntry": traceRcvrX25DnaRowStatusEntry,
       "traceRcvrX25DnaRowStatus": traceRcvrX25DnaRowStatus,
       "traceRcvrX25DnaComponentName": traceRcvrX25DnaComponentName,
       "traceRcvrX25DnaStorageType": traceRcvrX25DnaStorageType,
       "traceRcvrX25DnaIndex": traceRcvrX25DnaIndex,
       "traceRcvrX25DnaCug": traceRcvrX25DnaCug,
       "traceRcvrX25DnaCugRowStatusTable": traceRcvrX25DnaCugRowStatusTable,
       "traceRcvrX25DnaCugRowStatusEntry": traceRcvrX25DnaCugRowStatusEntry,
       "traceRcvrX25DnaCugRowStatus": traceRcvrX25DnaCugRowStatus,
       "traceRcvrX25DnaCugComponentName": traceRcvrX25DnaCugComponentName,
       "traceRcvrX25DnaCugStorageType": traceRcvrX25DnaCugStorageType,
       "traceRcvrX25DnaCugIndex": traceRcvrX25DnaCugIndex,
       "traceRcvrX25DnaCugCugOptionsTable": traceRcvrX25DnaCugCugOptionsTable,
       "traceRcvrX25DnaCugCugOptionsEntry": traceRcvrX25DnaCugCugOptionsEntry,
       "traceRcvrX25DnaCugType": traceRcvrX25DnaCugType,
       "traceRcvrX25DnaCugDnic": traceRcvrX25DnaCugDnic,
       "traceRcvrX25DnaCugInterlockCode": traceRcvrX25DnaCugInterlockCode,
       "traceRcvrX25DnaCugPreferential": traceRcvrX25DnaCugPreferential,
       "traceRcvrX25DnaCugOutCalls": traceRcvrX25DnaCugOutCalls,
       "traceRcvrX25DnaCugIncCalls": traceRcvrX25DnaCugIncCalls,
       "traceRcvrX25DnaCugPrivileged": traceRcvrX25DnaCugPrivileged,
       "traceRcvrX25DnaAddressTable": traceRcvrX25DnaAddressTable,
       "traceRcvrX25DnaAddressEntry": traceRcvrX25DnaAddressEntry,
       "traceRcvrX25DnaNumberingPlanIndicator": traceRcvrX25DnaNumberingPlanIndicator,
       "traceRcvrX25DnaDataNetworkAddress": traceRcvrX25DnaDataNetworkAddress,
       "traceRcvrX25DnaOutgoingOptionsTable": traceRcvrX25DnaOutgoingOptionsTable,
       "traceRcvrX25DnaOutgoingOptionsEntry": traceRcvrX25DnaOutgoingOptionsEntry,
       "traceRcvrX25DnaOutCalls": traceRcvrX25DnaOutCalls,
       "traceRcvrX25DnaOutDefaultPriority": traceRcvrX25DnaOutDefaultPriority,
       "traceRcvrX25DnaOutIntl": traceRcvrX25DnaOutIntl,
       "traceRcvrX25DnaOutDefaultPathSensitivity": traceRcvrX25DnaOutDefaultPathSensitivity,
       "traceRcvrX25DnaOutDefaultPathReliability": traceRcvrX25DnaOutDefaultPathReliability,
       "traceRcvrX25DnaOutPathReliabilityOverRide": traceRcvrX25DnaOutPathReliabilityOverRide,
       "traceRcvrX25DnaOutPathReliabilitySignal": traceRcvrX25DnaOutPathReliabilitySignal,
       "traceRcvrX25DnaOutAccess": traceRcvrX25DnaOutAccess,
       "traceRcvrX25DnaIncomingOptionsTable": traceRcvrX25DnaIncomingOptionsTable,
       "traceRcvrX25DnaIncomingOptionsEntry": traceRcvrX25DnaIncomingOptionsEntry,
       "traceRcvrX25DnaIncCalls": traceRcvrX25DnaIncCalls,
       "traceRcvrX25DnaCallOptionsTable": traceRcvrX25DnaCallOptionsTable,
       "traceRcvrX25DnaCallOptionsEntry": traceRcvrX25DnaCallOptionsEntry,
       "traceRcvrX25DnaPacketSizes": traceRcvrX25DnaPacketSizes,
       "traceRcvrX25DnaDefaultRecvFrmNetworkPacketSize": traceRcvrX25DnaDefaultRecvFrmNetworkPacketSize,
       "traceRcvrX25DnaDefaultSendToNetworkPacketSize": traceRcvrX25DnaDefaultSendToNetworkPacketSize,
       "traceRcvrX25DnaDefaultRecvFrmNetworkThruputClass": traceRcvrX25DnaDefaultRecvFrmNetworkThruputClass,
       "traceRcvrX25DnaDefaultSendToNetworkThruputClass": traceRcvrX25DnaDefaultSendToNetworkThruputClass,
       "traceRcvrX25DnaDefaultRecvFrmNetworkWindowSize": traceRcvrX25DnaDefaultRecvFrmNetworkWindowSize,
       "traceRcvrX25DnaDefaultSendToNetworkWindowSize": traceRcvrX25DnaDefaultSendToNetworkWindowSize,
       "traceRcvrX25DnaPacketSizeNegotiation": traceRcvrX25DnaPacketSizeNegotiation,
       "traceRcvrX25DnaCugFormat": traceRcvrX25DnaCugFormat,
       "traceRcvrX25Dc": traceRcvrX25Dc,
       "traceRcvrX25DcRowStatusTable": traceRcvrX25DcRowStatusTable,
       "traceRcvrX25DcRowStatusEntry": traceRcvrX25DcRowStatusEntry,
       "traceRcvrX25DcRowStatus": traceRcvrX25DcRowStatus,
       "traceRcvrX25DcComponentName": traceRcvrX25DcComponentName,
       "traceRcvrX25DcStorageType": traceRcvrX25DcStorageType,
       "traceRcvrX25DcIndex": traceRcvrX25DcIndex,
       "traceRcvrX25DcOptionsTable": traceRcvrX25DcOptionsTable,
       "traceRcvrX25DcOptionsEntry": traceRcvrX25DcOptionsEntry,
       "traceRcvrX25DcRemoteNpi": traceRcvrX25DcRemoteNpi,
       "traceRcvrX25DcRemoteDna": traceRcvrX25DcRemoteDna,
       "traceRcvrX25DcType": traceRcvrX25DcType,
       "traceRcvrX25DcUserData": traceRcvrX25DcUserData,
       "traceSessionX25": traceSessionX25,
       "traceSessionX25RowStatusTable": traceSessionX25RowStatusTable,
       "traceSessionX25RowStatusEntry": traceSessionX25RowStatusEntry,
       "traceSessionX25RowStatus": traceSessionX25RowStatus,
       "traceSessionX25ComponentName": traceSessionX25ComponentName,
       "traceSessionX25StorageType": traceSessionX25StorageType,
       "traceSessionX25Index": traceSessionX25Index,
       "traceSessionX25Vc": traceSessionX25Vc,
       "traceSessionX25VcRowStatusTable": traceSessionX25VcRowStatusTable,
       "traceSessionX25VcRowStatusEntry": traceSessionX25VcRowStatusEntry,
       "traceSessionX25VcRowStatus": traceSessionX25VcRowStatus,
       "traceSessionX25VcComponentName": traceSessionX25VcComponentName,
       "traceSessionX25VcStorageType": traceSessionX25VcStorageType,
       "traceSessionX25VcIndex": traceSessionX25VcIndex,
       "traceSessionX25VcCadTable": traceSessionX25VcCadTable,
       "traceSessionX25VcCadEntry": traceSessionX25VcCadEntry,
       "traceSessionX25VcType": traceSessionX25VcType,
       "traceSessionX25VcState": traceSessionX25VcState,
       "traceSessionX25VcPreviousState": traceSessionX25VcPreviousState,
       "traceSessionX25VcDiagnosticCode": traceSessionX25VcDiagnosticCode,
       "traceSessionX25VcPreviousDiagnosticCode": traceSessionX25VcPreviousDiagnosticCode,
       "traceSessionX25VcCalledNpi": traceSessionX25VcCalledNpi,
       "traceSessionX25VcCalledDna": traceSessionX25VcCalledDna,
       "traceSessionX25VcCalledLcn": traceSessionX25VcCalledLcn,
       "traceSessionX25VcCallingNpi": traceSessionX25VcCallingNpi,
       "traceSessionX25VcCallingDna": traceSessionX25VcCallingDna,
       "traceSessionX25VcCallingLcn": traceSessionX25VcCallingLcn,
       "traceSessionX25VcAccountingEnabled": traceSessionX25VcAccountingEnabled,
       "traceSessionX25VcFastSelectCall": traceSessionX25VcFastSelectCall,
       "traceSessionX25VcLocalRxPktSize": traceSessionX25VcLocalRxPktSize,
       "traceSessionX25VcLocalTxPktSize": traceSessionX25VcLocalTxPktSize,
       "traceSessionX25VcLocalTxWindowSize": traceSessionX25VcLocalTxWindowSize,
       "traceSessionX25VcLocalRxWindowSize": traceSessionX25VcLocalRxWindowSize,
       "traceSessionX25VcPathReliability": traceSessionX25VcPathReliability,
       "traceSessionX25VcAccountingEnd": traceSessionX25VcAccountingEnd,
       "traceSessionX25VcPriority": traceSessionX25VcPriority,
       "traceSessionX25VcSegmentSize": traceSessionX25VcSegmentSize,
       "traceSessionX25VcSubnetTxPktSize": traceSessionX25VcSubnetTxPktSize,
       "traceSessionX25VcSubnetTxWindowSize": traceSessionX25VcSubnetTxWindowSize,
       "traceSessionX25VcSubnetRxPktSize": traceSessionX25VcSubnetRxPktSize,
       "traceSessionX25VcSubnetRxWindowSize": traceSessionX25VcSubnetRxWindowSize,
       "traceSessionX25VcMaxSubnetPktSize": traceSessionX25VcMaxSubnetPktSize,
       "traceSessionX25VcTransferPriorityToNetwork": traceSessionX25VcTransferPriorityToNetwork,
       "traceSessionX25VcTransferPriorityFromNetwork": traceSessionX25VcTransferPriorityFromNetwork,
       "traceSessionX25VcIntdTable": traceSessionX25VcIntdTable,
       "traceSessionX25VcIntdEntry": traceSessionX25VcIntdEntry,
       "traceSessionX25VcCallReferenceNumber": traceSessionX25VcCallReferenceNumber,
       "traceSessionX25VcElapsedTimeTillNow": traceSessionX25VcElapsedTimeTillNow,
       "traceSessionX25VcSegmentsRx": traceSessionX25VcSegmentsRx,
       "traceSessionX25VcSegmentsSent": traceSessionX25VcSegmentsSent,
       "traceSessionX25VcStartTime": traceSessionX25VcStartTime,
       "traceSessionX25VcStatsTable": traceSessionX25VcStatsTable,
       "traceSessionX25VcStatsEntry": traceSessionX25VcStatsEntry,
       "traceSessionX25VcAckStackingTimeouts": traceSessionX25VcAckStackingTimeouts,
       "traceSessionX25VcOutOfRangeFrmFromSubnet": traceSessionX25VcOutOfRangeFrmFromSubnet,
       "traceSessionX25VcDuplicatesFromSubnet": traceSessionX25VcDuplicatesFromSubnet,
       "traceSessionX25VcFrmRetryTimeouts": traceSessionX25VcFrmRetryTimeouts,
       "traceSessionX25VcPeakRetryQueueSize": traceSessionX25VcPeakRetryQueueSize,
       "traceSessionX25VcPeakOoSeqQueueSize": traceSessionX25VcPeakOoSeqQueueSize,
       "traceSessionX25VcPeakOoSeqFrmForwarded": traceSessionX25VcPeakOoSeqFrmForwarded,
       "traceSessionX25VcPeakStackedAcksRx": traceSessionX25VcPeakStackedAcksRx,
       "traceSessionX25VcSubnetRecoveries": traceSessionX25VcSubnetRecoveries,
       "traceSessionX25VcWindowClosuresToSubnet": traceSessionX25VcWindowClosuresToSubnet,
       "traceSessionX25VcWindowClosuresFromSubnet": traceSessionX25VcWindowClosuresFromSubnet,
       "traceSessionX25VcWrTriggers": traceSessionX25VcWrTriggers,
       "x25TraceRcvrMIB": x25TraceRcvrMIB,
       "x25TraceRcvrGroup": x25TraceRcvrGroup,
       "x25TraceRcvrGroupBD": x25TraceRcvrGroupBD,
       "x25TraceRcvrGroupBD00": x25TraceRcvrGroupBD00,
       "x25TraceRcvrGroupBD00A": x25TraceRcvrGroupBD00A,
       "x25TraceRcvrCapabilities": x25TraceRcvrCapabilities,
       "x25TraceRcvrCapabilitiesBD": x25TraceRcvrCapabilitiesBD,
       "x25TraceRcvrCapabilitiesBD00": x25TraceRcvrCapabilitiesBD00,
       "x25TraceRcvrCapabilitiesBD00A": x25TraceRcvrCapabilitiesBD00A}
)
