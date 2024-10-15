# SNMP MIB module (Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:24 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
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
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "DigitString",
    "EnterpriseDateAndTime",
    "Hex",
    "HexString",
    "NonReplicated")

(mscTraceIndex,
 mscTraceRcvr,
 mscTraceRcvrIndex,
 mscTraceSession,
 mscTraceSessionIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TraceBaseMIB",
    "mscTraceIndex",
    "mscTraceRcvr",
    "mscTraceRcvrIndex",
    "mscTraceSession",
    "mscTraceSessionIndex")

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

_MscTraceRcvrX25_ObjectIdentity = ObjectIdentity
mscTraceRcvrX25 = _MscTraceRcvrX25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2)
)
_MscTraceRcvrX25RowStatusTable_Object = MibTable
mscTraceRcvrX25RowStatusTable = _MscTraceRcvrX25RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscTraceRcvrX25RowStatusTable.setStatus("mandatory")
_MscTraceRcvrX25RowStatusEntry_Object = MibTableRow
mscTraceRcvrX25RowStatusEntry = _MscTraceRcvrX25RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 1, 1)
)
mscTraceRcvrX25RowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceRcvrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceRcvrX25Index"),
)
if mibBuilder.loadTexts:
    mscTraceRcvrX25RowStatusEntry.setStatus("mandatory")
_MscTraceRcvrX25RowStatus_Type = RowStatus
_MscTraceRcvrX25RowStatus_Object = MibTableColumn
mscTraceRcvrX25RowStatus = _MscTraceRcvrX25RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 1, 1, 1),
    _MscTraceRcvrX25RowStatus_Type()
)
mscTraceRcvrX25RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrX25RowStatus.setStatus("mandatory")
_MscTraceRcvrX25ComponentName_Type = DisplayString
_MscTraceRcvrX25ComponentName_Object = MibTableColumn
mscTraceRcvrX25ComponentName = _MscTraceRcvrX25ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 1, 1, 2),
    _MscTraceRcvrX25ComponentName_Type()
)
mscTraceRcvrX25ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25ComponentName.setStatus("mandatory")
_MscTraceRcvrX25StorageType_Type = StorageType
_MscTraceRcvrX25StorageType_Object = MibTableColumn
mscTraceRcvrX25StorageType = _MscTraceRcvrX25StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 1, 1, 4),
    _MscTraceRcvrX25StorageType_Type()
)
mscTraceRcvrX25StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25StorageType.setStatus("mandatory")
_MscTraceRcvrX25Index_Type = NonReplicated
_MscTraceRcvrX25Index_Object = MibTableColumn
mscTraceRcvrX25Index = _MscTraceRcvrX25Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 1, 1, 10),
    _MscTraceRcvrX25Index_Type()
)
mscTraceRcvrX25Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTraceRcvrX25Index.setStatus("mandatory")
_MscTraceRcvrX25Dna_ObjectIdentity = ObjectIdentity
mscTraceRcvrX25Dna = _MscTraceRcvrX25Dna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2)
)
_MscTraceRcvrX25DnaRowStatusTable_Object = MibTable
mscTraceRcvrX25DnaRowStatusTable = _MscTraceRcvrX25DnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaRowStatusTable.setStatus("mandatory")
_MscTraceRcvrX25DnaRowStatusEntry_Object = MibTableRow
mscTraceRcvrX25DnaRowStatusEntry = _MscTraceRcvrX25DnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 1, 1)
)
mscTraceRcvrX25DnaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceRcvrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceRcvrX25Index"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceRcvrX25DnaIndex"),
)
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaRowStatusEntry.setStatus("mandatory")
_MscTraceRcvrX25DnaRowStatus_Type = RowStatus
_MscTraceRcvrX25DnaRowStatus_Object = MibTableColumn
mscTraceRcvrX25DnaRowStatus = _MscTraceRcvrX25DnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 1, 1, 1),
    _MscTraceRcvrX25DnaRowStatus_Type()
)
mscTraceRcvrX25DnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaRowStatus.setStatus("mandatory")
_MscTraceRcvrX25DnaComponentName_Type = DisplayString
_MscTraceRcvrX25DnaComponentName_Object = MibTableColumn
mscTraceRcvrX25DnaComponentName = _MscTraceRcvrX25DnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 1, 1, 2),
    _MscTraceRcvrX25DnaComponentName_Type()
)
mscTraceRcvrX25DnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaComponentName.setStatus("mandatory")
_MscTraceRcvrX25DnaStorageType_Type = StorageType
_MscTraceRcvrX25DnaStorageType_Object = MibTableColumn
mscTraceRcvrX25DnaStorageType = _MscTraceRcvrX25DnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 1, 1, 4),
    _MscTraceRcvrX25DnaStorageType_Type()
)
mscTraceRcvrX25DnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaStorageType.setStatus("mandatory")
_MscTraceRcvrX25DnaIndex_Type = NonReplicated
_MscTraceRcvrX25DnaIndex_Object = MibTableColumn
mscTraceRcvrX25DnaIndex = _MscTraceRcvrX25DnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 1, 1, 10),
    _MscTraceRcvrX25DnaIndex_Type()
)
mscTraceRcvrX25DnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaIndex.setStatus("mandatory")
_MscTraceRcvrX25DnaCug_ObjectIdentity = ObjectIdentity
mscTraceRcvrX25DnaCug = _MscTraceRcvrX25DnaCug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 2)
)
_MscTraceRcvrX25DnaCugRowStatusTable_Object = MibTable
mscTraceRcvrX25DnaCugRowStatusTable = _MscTraceRcvrX25DnaCugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaCugRowStatusTable.setStatus("mandatory")
_MscTraceRcvrX25DnaCugRowStatusEntry_Object = MibTableRow
mscTraceRcvrX25DnaCugRowStatusEntry = _MscTraceRcvrX25DnaCugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 2, 1, 1)
)
mscTraceRcvrX25DnaCugRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceRcvrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceRcvrX25Index"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceRcvrX25DnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceRcvrX25DnaCugIndex"),
)
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaCugRowStatusEntry.setStatus("mandatory")
_MscTraceRcvrX25DnaCugRowStatus_Type = RowStatus
_MscTraceRcvrX25DnaCugRowStatus_Object = MibTableColumn
mscTraceRcvrX25DnaCugRowStatus = _MscTraceRcvrX25DnaCugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 2, 1, 1, 1),
    _MscTraceRcvrX25DnaCugRowStatus_Type()
)
mscTraceRcvrX25DnaCugRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaCugRowStatus.setStatus("mandatory")
_MscTraceRcvrX25DnaCugComponentName_Type = DisplayString
_MscTraceRcvrX25DnaCugComponentName_Object = MibTableColumn
mscTraceRcvrX25DnaCugComponentName = _MscTraceRcvrX25DnaCugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 2, 1, 1, 2),
    _MscTraceRcvrX25DnaCugComponentName_Type()
)
mscTraceRcvrX25DnaCugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaCugComponentName.setStatus("mandatory")
_MscTraceRcvrX25DnaCugStorageType_Type = StorageType
_MscTraceRcvrX25DnaCugStorageType_Object = MibTableColumn
mscTraceRcvrX25DnaCugStorageType = _MscTraceRcvrX25DnaCugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 2, 1, 1, 4),
    _MscTraceRcvrX25DnaCugStorageType_Type()
)
mscTraceRcvrX25DnaCugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaCugStorageType.setStatus("mandatory")


class _MscTraceRcvrX25DnaCugIndex_Type(Integer32):
    """Custom type mscTraceRcvrX25DnaCugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MscTraceRcvrX25DnaCugIndex_Type.__name__ = "Integer32"
_MscTraceRcvrX25DnaCugIndex_Object = MibTableColumn
mscTraceRcvrX25DnaCugIndex = _MscTraceRcvrX25DnaCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 2, 1, 1, 10),
    _MscTraceRcvrX25DnaCugIndex_Type()
)
mscTraceRcvrX25DnaCugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaCugIndex.setStatus("mandatory")
_MscTraceRcvrX25DnaCugCugOptionsTable_Object = MibTable
mscTraceRcvrX25DnaCugCugOptionsTable = _MscTraceRcvrX25DnaCugCugOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaCugCugOptionsTable.setStatus("mandatory")
_MscTraceRcvrX25DnaCugCugOptionsEntry_Object = MibTableRow
mscTraceRcvrX25DnaCugCugOptionsEntry = _MscTraceRcvrX25DnaCugCugOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 2, 10, 1)
)
mscTraceRcvrX25DnaCugCugOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceRcvrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceRcvrX25Index"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceRcvrX25DnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceRcvrX25DnaCugIndex"),
)
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaCugCugOptionsEntry.setStatus("mandatory")


class _MscTraceRcvrX25DnaCugType_Type(Integer32):
    """Custom type mscTraceRcvrX25DnaCugType based on Integer32"""
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


_MscTraceRcvrX25DnaCugType_Type.__name__ = "Integer32"
_MscTraceRcvrX25DnaCugType_Object = MibTableColumn
mscTraceRcvrX25DnaCugType = _MscTraceRcvrX25DnaCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 2, 10, 1, 1),
    _MscTraceRcvrX25DnaCugType_Type()
)
mscTraceRcvrX25DnaCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaCugType.setStatus("mandatory")


class _MscTraceRcvrX25DnaCugDnic_Type(DigitString):
    """Custom type mscTraceRcvrX25DnaCugDnic based on DigitString"""
    defaultHexValue = "30303030"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MscTraceRcvrX25DnaCugDnic_Type.__name__ = "DigitString"
_MscTraceRcvrX25DnaCugDnic_Object = MibTableColumn
mscTraceRcvrX25DnaCugDnic = _MscTraceRcvrX25DnaCugDnic_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 2, 10, 1, 2),
    _MscTraceRcvrX25DnaCugDnic_Type()
)
mscTraceRcvrX25DnaCugDnic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaCugDnic.setStatus("mandatory")


class _MscTraceRcvrX25DnaCugInterlockCode_Type(Unsigned32):
    """Custom type mscTraceRcvrX25DnaCugInterlockCode based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscTraceRcvrX25DnaCugInterlockCode_Type.__name__ = "Unsigned32"
_MscTraceRcvrX25DnaCugInterlockCode_Object = MibTableColumn
mscTraceRcvrX25DnaCugInterlockCode = _MscTraceRcvrX25DnaCugInterlockCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 2, 10, 1, 3),
    _MscTraceRcvrX25DnaCugInterlockCode_Type()
)
mscTraceRcvrX25DnaCugInterlockCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaCugInterlockCode.setStatus("mandatory")


class _MscTraceRcvrX25DnaCugPreferential_Type(Integer32):
    """Custom type mscTraceRcvrX25DnaCugPreferential based on Integer32"""
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


_MscTraceRcvrX25DnaCugPreferential_Type.__name__ = "Integer32"
_MscTraceRcvrX25DnaCugPreferential_Object = MibTableColumn
mscTraceRcvrX25DnaCugPreferential = _MscTraceRcvrX25DnaCugPreferential_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 2, 10, 1, 4),
    _MscTraceRcvrX25DnaCugPreferential_Type()
)
mscTraceRcvrX25DnaCugPreferential.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaCugPreferential.setStatus("mandatory")


class _MscTraceRcvrX25DnaCugOutCalls_Type(Integer32):
    """Custom type mscTraceRcvrX25DnaCugOutCalls based on Integer32"""
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


_MscTraceRcvrX25DnaCugOutCalls_Type.__name__ = "Integer32"
_MscTraceRcvrX25DnaCugOutCalls_Object = MibTableColumn
mscTraceRcvrX25DnaCugOutCalls = _MscTraceRcvrX25DnaCugOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 2, 10, 1, 5),
    _MscTraceRcvrX25DnaCugOutCalls_Type()
)
mscTraceRcvrX25DnaCugOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaCugOutCalls.setStatus("mandatory")


class _MscTraceRcvrX25DnaCugIncCalls_Type(Integer32):
    """Custom type mscTraceRcvrX25DnaCugIncCalls based on Integer32"""
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


_MscTraceRcvrX25DnaCugIncCalls_Type.__name__ = "Integer32"
_MscTraceRcvrX25DnaCugIncCalls_Object = MibTableColumn
mscTraceRcvrX25DnaCugIncCalls = _MscTraceRcvrX25DnaCugIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 2, 10, 1, 6),
    _MscTraceRcvrX25DnaCugIncCalls_Type()
)
mscTraceRcvrX25DnaCugIncCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaCugIncCalls.setStatus("mandatory")


class _MscTraceRcvrX25DnaCugPrivileged_Type(Integer32):
    """Custom type mscTraceRcvrX25DnaCugPrivileged based on Integer32"""
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


_MscTraceRcvrX25DnaCugPrivileged_Type.__name__ = "Integer32"
_MscTraceRcvrX25DnaCugPrivileged_Object = MibTableColumn
mscTraceRcvrX25DnaCugPrivileged = _MscTraceRcvrX25DnaCugPrivileged_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 2, 10, 1, 7),
    _MscTraceRcvrX25DnaCugPrivileged_Type()
)
mscTraceRcvrX25DnaCugPrivileged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaCugPrivileged.setStatus("mandatory")
_MscTraceRcvrX25DnaAddressTable_Object = MibTable
mscTraceRcvrX25DnaAddressTable = _MscTraceRcvrX25DnaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaAddressTable.setStatus("mandatory")
_MscTraceRcvrX25DnaAddressEntry_Object = MibTableRow
mscTraceRcvrX25DnaAddressEntry = _MscTraceRcvrX25DnaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 10, 1)
)
mscTraceRcvrX25DnaAddressEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceRcvrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceRcvrX25Index"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceRcvrX25DnaIndex"),
)
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaAddressEntry.setStatus("mandatory")


class _MscTraceRcvrX25DnaNumberingPlanIndicator_Type(Integer32):
    """Custom type mscTraceRcvrX25DnaNumberingPlanIndicator based on Integer32"""
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


_MscTraceRcvrX25DnaNumberingPlanIndicator_Type.__name__ = "Integer32"
_MscTraceRcvrX25DnaNumberingPlanIndicator_Object = MibTableColumn
mscTraceRcvrX25DnaNumberingPlanIndicator = _MscTraceRcvrX25DnaNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 10, 1, 1),
    _MscTraceRcvrX25DnaNumberingPlanIndicator_Type()
)
mscTraceRcvrX25DnaNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaNumberingPlanIndicator.setStatus("mandatory")


class _MscTraceRcvrX25DnaDataNetworkAddress_Type(DigitString):
    """Custom type mscTraceRcvrX25DnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscTraceRcvrX25DnaDataNetworkAddress_Type.__name__ = "DigitString"
_MscTraceRcvrX25DnaDataNetworkAddress_Object = MibTableColumn
mscTraceRcvrX25DnaDataNetworkAddress = _MscTraceRcvrX25DnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 10, 1, 2),
    _MscTraceRcvrX25DnaDataNetworkAddress_Type()
)
mscTraceRcvrX25DnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaDataNetworkAddress.setStatus("mandatory")
_MscTraceRcvrX25DnaOutgoingOptionsTable_Object = MibTable
mscTraceRcvrX25DnaOutgoingOptionsTable = _MscTraceRcvrX25DnaOutgoingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 11)
)
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaOutgoingOptionsTable.setStatus("mandatory")
_MscTraceRcvrX25DnaOutgoingOptionsEntry_Object = MibTableRow
mscTraceRcvrX25DnaOutgoingOptionsEntry = _MscTraceRcvrX25DnaOutgoingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 11, 1)
)
mscTraceRcvrX25DnaOutgoingOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceRcvrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceRcvrX25Index"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceRcvrX25DnaIndex"),
)
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaOutgoingOptionsEntry.setStatus("mandatory")


class _MscTraceRcvrX25DnaOutCalls_Type(Integer32):
    """Custom type mscTraceRcvrX25DnaOutCalls based on Integer32"""
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


_MscTraceRcvrX25DnaOutCalls_Type.__name__ = "Integer32"
_MscTraceRcvrX25DnaOutCalls_Object = MibTableColumn
mscTraceRcvrX25DnaOutCalls = _MscTraceRcvrX25DnaOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 11, 1, 1),
    _MscTraceRcvrX25DnaOutCalls_Type()
)
mscTraceRcvrX25DnaOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaOutCalls.setStatus("mandatory")


class _MscTraceRcvrX25DnaOutDefaultPriority_Type(Integer32):
    """Custom type mscTraceRcvrX25DnaOutDefaultPriority based on Integer32"""
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


_MscTraceRcvrX25DnaOutDefaultPriority_Type.__name__ = "Integer32"
_MscTraceRcvrX25DnaOutDefaultPriority_Object = MibTableColumn
mscTraceRcvrX25DnaOutDefaultPriority = _MscTraceRcvrX25DnaOutDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 11, 1, 7),
    _MscTraceRcvrX25DnaOutDefaultPriority_Type()
)
mscTraceRcvrX25DnaOutDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaOutDefaultPriority.setStatus("mandatory")


class _MscTraceRcvrX25DnaOutIntl_Type(Integer32):
    """Custom type mscTraceRcvrX25DnaOutIntl based on Integer32"""
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


_MscTraceRcvrX25DnaOutIntl_Type.__name__ = "Integer32"
_MscTraceRcvrX25DnaOutIntl_Object = MibTableColumn
mscTraceRcvrX25DnaOutIntl = _MscTraceRcvrX25DnaOutIntl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 11, 1, 8),
    _MscTraceRcvrX25DnaOutIntl_Type()
)
mscTraceRcvrX25DnaOutIntl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaOutIntl.setStatus("mandatory")


class _MscTraceRcvrX25DnaOutDefaultPathSensitivity_Type(Integer32):
    """Custom type mscTraceRcvrX25DnaOutDefaultPathSensitivity based on Integer32"""
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


_MscTraceRcvrX25DnaOutDefaultPathSensitivity_Type.__name__ = "Integer32"
_MscTraceRcvrX25DnaOutDefaultPathSensitivity_Object = MibTableColumn
mscTraceRcvrX25DnaOutDefaultPathSensitivity = _MscTraceRcvrX25DnaOutDefaultPathSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 11, 1, 11),
    _MscTraceRcvrX25DnaOutDefaultPathSensitivity_Type()
)
mscTraceRcvrX25DnaOutDefaultPathSensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaOutDefaultPathSensitivity.setStatus("obsolete")


class _MscTraceRcvrX25DnaOutDefaultPathReliability_Type(Integer32):
    """Custom type mscTraceRcvrX25DnaOutDefaultPathReliability based on Integer32"""
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


_MscTraceRcvrX25DnaOutDefaultPathReliability_Type.__name__ = "Integer32"
_MscTraceRcvrX25DnaOutDefaultPathReliability_Object = MibTableColumn
mscTraceRcvrX25DnaOutDefaultPathReliability = _MscTraceRcvrX25DnaOutDefaultPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 11, 1, 14),
    _MscTraceRcvrX25DnaOutDefaultPathReliability_Type()
)
mscTraceRcvrX25DnaOutDefaultPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaOutDefaultPathReliability.setStatus("mandatory")


class _MscTraceRcvrX25DnaOutPathReliabilityOverRide_Type(Integer32):
    """Custom type mscTraceRcvrX25DnaOutPathReliabilityOverRide based on Integer32"""
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


_MscTraceRcvrX25DnaOutPathReliabilityOverRide_Type.__name__ = "Integer32"
_MscTraceRcvrX25DnaOutPathReliabilityOverRide_Object = MibTableColumn
mscTraceRcvrX25DnaOutPathReliabilityOverRide = _MscTraceRcvrX25DnaOutPathReliabilityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 11, 1, 15),
    _MscTraceRcvrX25DnaOutPathReliabilityOverRide_Type()
)
mscTraceRcvrX25DnaOutPathReliabilityOverRide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaOutPathReliabilityOverRide.setStatus("mandatory")


class _MscTraceRcvrX25DnaOutPathReliabilitySignal_Type(Integer32):
    """Custom type mscTraceRcvrX25DnaOutPathReliabilitySignal based on Integer32"""
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


_MscTraceRcvrX25DnaOutPathReliabilitySignal_Type.__name__ = "Integer32"
_MscTraceRcvrX25DnaOutPathReliabilitySignal_Object = MibTableColumn
mscTraceRcvrX25DnaOutPathReliabilitySignal = _MscTraceRcvrX25DnaOutPathReliabilitySignal_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 11, 1, 16),
    _MscTraceRcvrX25DnaOutPathReliabilitySignal_Type()
)
mscTraceRcvrX25DnaOutPathReliabilitySignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaOutPathReliabilitySignal.setStatus("mandatory")


class _MscTraceRcvrX25DnaOutAccess_Type(Integer32):
    """Custom type mscTraceRcvrX25DnaOutAccess based on Integer32"""
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


_MscTraceRcvrX25DnaOutAccess_Type.__name__ = "Integer32"
_MscTraceRcvrX25DnaOutAccess_Object = MibTableColumn
mscTraceRcvrX25DnaOutAccess = _MscTraceRcvrX25DnaOutAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 11, 1, 17),
    _MscTraceRcvrX25DnaOutAccess_Type()
)
mscTraceRcvrX25DnaOutAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaOutAccess.setStatus("mandatory")
_MscTraceRcvrX25DnaIncomingOptionsTable_Object = MibTable
mscTraceRcvrX25DnaIncomingOptionsTable = _MscTraceRcvrX25DnaIncomingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 12)
)
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaIncomingOptionsTable.setStatus("mandatory")
_MscTraceRcvrX25DnaIncomingOptionsEntry_Object = MibTableRow
mscTraceRcvrX25DnaIncomingOptionsEntry = _MscTraceRcvrX25DnaIncomingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 12, 1)
)
mscTraceRcvrX25DnaIncomingOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceRcvrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceRcvrX25Index"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceRcvrX25DnaIndex"),
)
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaIncomingOptionsEntry.setStatus("mandatory")


class _MscTraceRcvrX25DnaIncCalls_Type(Integer32):
    """Custom type mscTraceRcvrX25DnaIncCalls based on Integer32"""
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


_MscTraceRcvrX25DnaIncCalls_Type.__name__ = "Integer32"
_MscTraceRcvrX25DnaIncCalls_Object = MibTableColumn
mscTraceRcvrX25DnaIncCalls = _MscTraceRcvrX25DnaIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 12, 1, 1),
    _MscTraceRcvrX25DnaIncCalls_Type()
)
mscTraceRcvrX25DnaIncCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaIncCalls.setStatus("mandatory")
_MscTraceRcvrX25DnaCallOptionsTable_Object = MibTable
mscTraceRcvrX25DnaCallOptionsTable = _MscTraceRcvrX25DnaCallOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 13)
)
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaCallOptionsTable.setStatus("mandatory")
_MscTraceRcvrX25DnaCallOptionsEntry_Object = MibTableRow
mscTraceRcvrX25DnaCallOptionsEntry = _MscTraceRcvrX25DnaCallOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 13, 1)
)
mscTraceRcvrX25DnaCallOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceRcvrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceRcvrX25Index"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceRcvrX25DnaIndex"),
)
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaCallOptionsEntry.setStatus("mandatory")


class _MscTraceRcvrX25DnaPacketSizes_Type(OctetString):
    """Custom type mscTraceRcvrX25DnaPacketSizes based on OctetString"""
    defaultHexValue = "0100"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscTraceRcvrX25DnaPacketSizes_Type.__name__ = "OctetString"
_MscTraceRcvrX25DnaPacketSizes_Object = MibTableColumn
mscTraceRcvrX25DnaPacketSizes = _MscTraceRcvrX25DnaPacketSizes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 13, 1, 2),
    _MscTraceRcvrX25DnaPacketSizes_Type()
)
mscTraceRcvrX25DnaPacketSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaPacketSizes.setStatus("mandatory")


class _MscTraceRcvrX25DnaDefaultRecvFrmNetworkPacketSize_Type(Integer32):
    """Custom type mscTraceRcvrX25DnaDefaultRecvFrmNetworkPacketSize based on Integer32"""
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


_MscTraceRcvrX25DnaDefaultRecvFrmNetworkPacketSize_Type.__name__ = "Integer32"
_MscTraceRcvrX25DnaDefaultRecvFrmNetworkPacketSize_Object = MibTableColumn
mscTraceRcvrX25DnaDefaultRecvFrmNetworkPacketSize = _MscTraceRcvrX25DnaDefaultRecvFrmNetworkPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 13, 1, 3),
    _MscTraceRcvrX25DnaDefaultRecvFrmNetworkPacketSize_Type()
)
mscTraceRcvrX25DnaDefaultRecvFrmNetworkPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaDefaultRecvFrmNetworkPacketSize.setStatus("mandatory")


class _MscTraceRcvrX25DnaDefaultSendToNetworkPacketSize_Type(Integer32):
    """Custom type mscTraceRcvrX25DnaDefaultSendToNetworkPacketSize based on Integer32"""
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


_MscTraceRcvrX25DnaDefaultSendToNetworkPacketSize_Type.__name__ = "Integer32"
_MscTraceRcvrX25DnaDefaultSendToNetworkPacketSize_Object = MibTableColumn
mscTraceRcvrX25DnaDefaultSendToNetworkPacketSize = _MscTraceRcvrX25DnaDefaultSendToNetworkPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 13, 1, 4),
    _MscTraceRcvrX25DnaDefaultSendToNetworkPacketSize_Type()
)
mscTraceRcvrX25DnaDefaultSendToNetworkPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaDefaultSendToNetworkPacketSize.setStatus("mandatory")


class _MscTraceRcvrX25DnaDefaultRecvFrmNetworkThruputClass_Type(Unsigned32):
    """Custom type mscTraceRcvrX25DnaDefaultRecvFrmNetworkThruputClass based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscTraceRcvrX25DnaDefaultRecvFrmNetworkThruputClass_Type.__name__ = "Unsigned32"
_MscTraceRcvrX25DnaDefaultRecvFrmNetworkThruputClass_Object = MibTableColumn
mscTraceRcvrX25DnaDefaultRecvFrmNetworkThruputClass = _MscTraceRcvrX25DnaDefaultRecvFrmNetworkThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 13, 1, 5),
    _MscTraceRcvrX25DnaDefaultRecvFrmNetworkThruputClass_Type()
)
mscTraceRcvrX25DnaDefaultRecvFrmNetworkThruputClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaDefaultRecvFrmNetworkThruputClass.setStatus("mandatory")


class _MscTraceRcvrX25DnaDefaultSendToNetworkThruputClass_Type(Unsigned32):
    """Custom type mscTraceRcvrX25DnaDefaultSendToNetworkThruputClass based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscTraceRcvrX25DnaDefaultSendToNetworkThruputClass_Type.__name__ = "Unsigned32"
_MscTraceRcvrX25DnaDefaultSendToNetworkThruputClass_Object = MibTableColumn
mscTraceRcvrX25DnaDefaultSendToNetworkThruputClass = _MscTraceRcvrX25DnaDefaultSendToNetworkThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 13, 1, 6),
    _MscTraceRcvrX25DnaDefaultSendToNetworkThruputClass_Type()
)
mscTraceRcvrX25DnaDefaultSendToNetworkThruputClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaDefaultSendToNetworkThruputClass.setStatus("mandatory")


class _MscTraceRcvrX25DnaDefaultRecvFrmNetworkWindowSize_Type(Unsigned32):
    """Custom type mscTraceRcvrX25DnaDefaultRecvFrmNetworkWindowSize based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_MscTraceRcvrX25DnaDefaultRecvFrmNetworkWindowSize_Type.__name__ = "Unsigned32"
_MscTraceRcvrX25DnaDefaultRecvFrmNetworkWindowSize_Object = MibTableColumn
mscTraceRcvrX25DnaDefaultRecvFrmNetworkWindowSize = _MscTraceRcvrX25DnaDefaultRecvFrmNetworkWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 13, 1, 7),
    _MscTraceRcvrX25DnaDefaultRecvFrmNetworkWindowSize_Type()
)
mscTraceRcvrX25DnaDefaultRecvFrmNetworkWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaDefaultRecvFrmNetworkWindowSize.setStatus("mandatory")


class _MscTraceRcvrX25DnaDefaultSendToNetworkWindowSize_Type(Unsigned32):
    """Custom type mscTraceRcvrX25DnaDefaultSendToNetworkWindowSize based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_MscTraceRcvrX25DnaDefaultSendToNetworkWindowSize_Type.__name__ = "Unsigned32"
_MscTraceRcvrX25DnaDefaultSendToNetworkWindowSize_Object = MibTableColumn
mscTraceRcvrX25DnaDefaultSendToNetworkWindowSize = _MscTraceRcvrX25DnaDefaultSendToNetworkWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 13, 1, 8),
    _MscTraceRcvrX25DnaDefaultSendToNetworkWindowSize_Type()
)
mscTraceRcvrX25DnaDefaultSendToNetworkWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaDefaultSendToNetworkWindowSize.setStatus("mandatory")


class _MscTraceRcvrX25DnaPacketSizeNegotiation_Type(Integer32):
    """Custom type mscTraceRcvrX25DnaPacketSizeNegotiation based on Integer32"""
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


_MscTraceRcvrX25DnaPacketSizeNegotiation_Type.__name__ = "Integer32"
_MscTraceRcvrX25DnaPacketSizeNegotiation_Object = MibTableColumn
mscTraceRcvrX25DnaPacketSizeNegotiation = _MscTraceRcvrX25DnaPacketSizeNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 13, 1, 9),
    _MscTraceRcvrX25DnaPacketSizeNegotiation_Type()
)
mscTraceRcvrX25DnaPacketSizeNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaPacketSizeNegotiation.setStatus("mandatory")


class _MscTraceRcvrX25DnaCugFormat_Type(Integer32):
    """Custom type mscTraceRcvrX25DnaCugFormat based on Integer32"""
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


_MscTraceRcvrX25DnaCugFormat_Type.__name__ = "Integer32"
_MscTraceRcvrX25DnaCugFormat_Object = MibTableColumn
mscTraceRcvrX25DnaCugFormat = _MscTraceRcvrX25DnaCugFormat_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 2, 13, 1, 10),
    _MscTraceRcvrX25DnaCugFormat_Type()
)
mscTraceRcvrX25DnaCugFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DnaCugFormat.setStatus("mandatory")
_MscTraceRcvrX25Dc_ObjectIdentity = ObjectIdentity
mscTraceRcvrX25Dc = _MscTraceRcvrX25Dc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 3)
)
_MscTraceRcvrX25DcRowStatusTable_Object = MibTable
mscTraceRcvrX25DcRowStatusTable = _MscTraceRcvrX25DcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mscTraceRcvrX25DcRowStatusTable.setStatus("mandatory")
_MscTraceRcvrX25DcRowStatusEntry_Object = MibTableRow
mscTraceRcvrX25DcRowStatusEntry = _MscTraceRcvrX25DcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 3, 1, 1)
)
mscTraceRcvrX25DcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceRcvrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceRcvrX25Index"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceRcvrX25DcIndex"),
)
if mibBuilder.loadTexts:
    mscTraceRcvrX25DcRowStatusEntry.setStatus("mandatory")
_MscTraceRcvrX25DcRowStatus_Type = RowStatus
_MscTraceRcvrX25DcRowStatus_Object = MibTableColumn
mscTraceRcvrX25DcRowStatus = _MscTraceRcvrX25DcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 3, 1, 1, 1),
    _MscTraceRcvrX25DcRowStatus_Type()
)
mscTraceRcvrX25DcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DcRowStatus.setStatus("mandatory")
_MscTraceRcvrX25DcComponentName_Type = DisplayString
_MscTraceRcvrX25DcComponentName_Object = MibTableColumn
mscTraceRcvrX25DcComponentName = _MscTraceRcvrX25DcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 3, 1, 1, 2),
    _MscTraceRcvrX25DcComponentName_Type()
)
mscTraceRcvrX25DcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DcComponentName.setStatus("mandatory")
_MscTraceRcvrX25DcStorageType_Type = StorageType
_MscTraceRcvrX25DcStorageType_Object = MibTableColumn
mscTraceRcvrX25DcStorageType = _MscTraceRcvrX25DcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 3, 1, 1, 4),
    _MscTraceRcvrX25DcStorageType_Type()
)
mscTraceRcvrX25DcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DcStorageType.setStatus("mandatory")
_MscTraceRcvrX25DcIndex_Type = NonReplicated
_MscTraceRcvrX25DcIndex_Object = MibTableColumn
mscTraceRcvrX25DcIndex = _MscTraceRcvrX25DcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 3, 1, 1, 10),
    _MscTraceRcvrX25DcIndex_Type()
)
mscTraceRcvrX25DcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DcIndex.setStatus("mandatory")
_MscTraceRcvrX25DcOptionsTable_Object = MibTable
mscTraceRcvrX25DcOptionsTable = _MscTraceRcvrX25DcOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 3, 10)
)
if mibBuilder.loadTexts:
    mscTraceRcvrX25DcOptionsTable.setStatus("mandatory")
_MscTraceRcvrX25DcOptionsEntry_Object = MibTableRow
mscTraceRcvrX25DcOptionsEntry = _MscTraceRcvrX25DcOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 3, 10, 1)
)
mscTraceRcvrX25DcOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceRcvrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceRcvrX25Index"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceRcvrX25DcIndex"),
)
if mibBuilder.loadTexts:
    mscTraceRcvrX25DcOptionsEntry.setStatus("mandatory")


class _MscTraceRcvrX25DcRemoteNpi_Type(Integer32):
    """Custom type mscTraceRcvrX25DcRemoteNpi based on Integer32"""
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


_MscTraceRcvrX25DcRemoteNpi_Type.__name__ = "Integer32"
_MscTraceRcvrX25DcRemoteNpi_Object = MibTableColumn
mscTraceRcvrX25DcRemoteNpi = _MscTraceRcvrX25DcRemoteNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 3, 10, 1, 3),
    _MscTraceRcvrX25DcRemoteNpi_Type()
)
mscTraceRcvrX25DcRemoteNpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DcRemoteNpi.setStatus("mandatory")


class _MscTraceRcvrX25DcRemoteDna_Type(DigitString):
    """Custom type mscTraceRcvrX25DcRemoteDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscTraceRcvrX25DcRemoteDna_Type.__name__ = "DigitString"
_MscTraceRcvrX25DcRemoteDna_Object = MibTableColumn
mscTraceRcvrX25DcRemoteDna = _MscTraceRcvrX25DcRemoteDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 3, 10, 1, 4),
    _MscTraceRcvrX25DcRemoteDna_Type()
)
mscTraceRcvrX25DcRemoteDna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DcRemoteDna.setStatus("mandatory")


class _MscTraceRcvrX25DcType_Type(Integer32):
    """Custom type mscTraceRcvrX25DcType based on Integer32"""
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


_MscTraceRcvrX25DcType_Type.__name__ = "Integer32"
_MscTraceRcvrX25DcType_Object = MibTableColumn
mscTraceRcvrX25DcType = _MscTraceRcvrX25DcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 3, 10, 1, 6),
    _MscTraceRcvrX25DcType_Type()
)
mscTraceRcvrX25DcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DcType.setStatus("mandatory")


class _MscTraceRcvrX25DcUserData_Type(HexString):
    """Custom type mscTraceRcvrX25DcUserData based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscTraceRcvrX25DcUserData_Type.__name__ = "HexString"
_MscTraceRcvrX25DcUserData_Object = MibTableColumn
mscTraceRcvrX25DcUserData = _MscTraceRcvrX25DcUserData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 2, 3, 10, 1, 8),
    _MscTraceRcvrX25DcUserData_Type()
)
mscTraceRcvrX25DcUserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrX25DcUserData.setStatus("mandatory")
_MscTraceSessionX25_ObjectIdentity = ObjectIdentity
mscTraceSessionX25 = _MscTraceSessionX25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2)
)
_MscTraceSessionX25RowStatusTable_Object = MibTable
mscTraceSessionX25RowStatusTable = _MscTraceSessionX25RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscTraceSessionX25RowStatusTable.setStatus("mandatory")
_MscTraceSessionX25RowStatusEntry_Object = MibTableRow
mscTraceSessionX25RowStatusEntry = _MscTraceSessionX25RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 1, 1)
)
mscTraceSessionX25RowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceSessionIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceSessionX25Index"),
)
if mibBuilder.loadTexts:
    mscTraceSessionX25RowStatusEntry.setStatus("mandatory")
_MscTraceSessionX25RowStatus_Type = RowStatus
_MscTraceSessionX25RowStatus_Object = MibTableColumn
mscTraceSessionX25RowStatus = _MscTraceSessionX25RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 1, 1, 1),
    _MscTraceSessionX25RowStatus_Type()
)
mscTraceSessionX25RowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25RowStatus.setStatus("mandatory")
_MscTraceSessionX25ComponentName_Type = DisplayString
_MscTraceSessionX25ComponentName_Object = MibTableColumn
mscTraceSessionX25ComponentName = _MscTraceSessionX25ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 1, 1, 2),
    _MscTraceSessionX25ComponentName_Type()
)
mscTraceSessionX25ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25ComponentName.setStatus("mandatory")
_MscTraceSessionX25StorageType_Type = StorageType
_MscTraceSessionX25StorageType_Object = MibTableColumn
mscTraceSessionX25StorageType = _MscTraceSessionX25StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 1, 1, 4),
    _MscTraceSessionX25StorageType_Type()
)
mscTraceSessionX25StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25StorageType.setStatus("mandatory")
_MscTraceSessionX25Index_Type = NonReplicated
_MscTraceSessionX25Index_Object = MibTableColumn
mscTraceSessionX25Index = _MscTraceSessionX25Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 1, 1, 10),
    _MscTraceSessionX25Index_Type()
)
mscTraceSessionX25Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTraceSessionX25Index.setStatus("mandatory")
_MscTraceSessionX25Vc_ObjectIdentity = ObjectIdentity
mscTraceSessionX25Vc = _MscTraceSessionX25Vc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2)
)
_MscTraceSessionX25VcRowStatusTable_Object = MibTable
mscTraceSessionX25VcRowStatusTable = _MscTraceSessionX25VcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscTraceSessionX25VcRowStatusTable.setStatus("mandatory")
_MscTraceSessionX25VcRowStatusEntry_Object = MibTableRow
mscTraceSessionX25VcRowStatusEntry = _MscTraceSessionX25VcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 1, 1)
)
mscTraceSessionX25VcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceSessionIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceSessionX25Index"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceSessionX25VcIndex"),
)
if mibBuilder.loadTexts:
    mscTraceSessionX25VcRowStatusEntry.setStatus("mandatory")
_MscTraceSessionX25VcRowStatus_Type = RowStatus
_MscTraceSessionX25VcRowStatus_Object = MibTableColumn
mscTraceSessionX25VcRowStatus = _MscTraceSessionX25VcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 1, 1, 1),
    _MscTraceSessionX25VcRowStatus_Type()
)
mscTraceSessionX25VcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcRowStatus.setStatus("mandatory")
_MscTraceSessionX25VcComponentName_Type = DisplayString
_MscTraceSessionX25VcComponentName_Object = MibTableColumn
mscTraceSessionX25VcComponentName = _MscTraceSessionX25VcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 1, 1, 2),
    _MscTraceSessionX25VcComponentName_Type()
)
mscTraceSessionX25VcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcComponentName.setStatus("mandatory")
_MscTraceSessionX25VcStorageType_Type = StorageType
_MscTraceSessionX25VcStorageType_Object = MibTableColumn
mscTraceSessionX25VcStorageType = _MscTraceSessionX25VcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 1, 1, 4),
    _MscTraceSessionX25VcStorageType_Type()
)
mscTraceSessionX25VcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcStorageType.setStatus("mandatory")
_MscTraceSessionX25VcIndex_Type = NonReplicated
_MscTraceSessionX25VcIndex_Object = MibTableColumn
mscTraceSessionX25VcIndex = _MscTraceSessionX25VcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 1, 1, 10),
    _MscTraceSessionX25VcIndex_Type()
)
mscTraceSessionX25VcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcIndex.setStatus("mandatory")
_MscTraceSessionX25VcCadTable_Object = MibTable
mscTraceSessionX25VcCadTable = _MscTraceSessionX25VcCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscTraceSessionX25VcCadTable.setStatus("mandatory")
_MscTraceSessionX25VcCadEntry_Object = MibTableRow
mscTraceSessionX25VcCadEntry = _MscTraceSessionX25VcCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1)
)
mscTraceSessionX25VcCadEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceSessionIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceSessionX25Index"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceSessionX25VcIndex"),
)
if mibBuilder.loadTexts:
    mscTraceSessionX25VcCadEntry.setStatus("mandatory")


class _MscTraceSessionX25VcType_Type(Integer32):
    """Custom type mscTraceSessionX25VcType based on Integer32"""
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


_MscTraceSessionX25VcType_Type.__name__ = "Integer32"
_MscTraceSessionX25VcType_Object = MibTableColumn
mscTraceSessionX25VcType = _MscTraceSessionX25VcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 1),
    _MscTraceSessionX25VcType_Type()
)
mscTraceSessionX25VcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcType.setStatus("mandatory")


class _MscTraceSessionX25VcState_Type(Integer32):
    """Custom type mscTraceSessionX25VcState based on Integer32"""
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


_MscTraceSessionX25VcState_Type.__name__ = "Integer32"
_MscTraceSessionX25VcState_Object = MibTableColumn
mscTraceSessionX25VcState = _MscTraceSessionX25VcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 2),
    _MscTraceSessionX25VcState_Type()
)
mscTraceSessionX25VcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcState.setStatus("mandatory")


class _MscTraceSessionX25VcPreviousState_Type(Integer32):
    """Custom type mscTraceSessionX25VcPreviousState based on Integer32"""
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


_MscTraceSessionX25VcPreviousState_Type.__name__ = "Integer32"
_MscTraceSessionX25VcPreviousState_Object = MibTableColumn
mscTraceSessionX25VcPreviousState = _MscTraceSessionX25VcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 3),
    _MscTraceSessionX25VcPreviousState_Type()
)
mscTraceSessionX25VcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcPreviousState.setStatus("mandatory")


class _MscTraceSessionX25VcDiagnosticCode_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscTraceSessionX25VcDiagnosticCode_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcDiagnosticCode_Object = MibTableColumn
mscTraceSessionX25VcDiagnosticCode = _MscTraceSessionX25VcDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 4),
    _MscTraceSessionX25VcDiagnosticCode_Type()
)
mscTraceSessionX25VcDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcDiagnosticCode.setStatus("mandatory")


class _MscTraceSessionX25VcPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscTraceSessionX25VcPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcPreviousDiagnosticCode_Object = MibTableColumn
mscTraceSessionX25VcPreviousDiagnosticCode = _MscTraceSessionX25VcPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 5),
    _MscTraceSessionX25VcPreviousDiagnosticCode_Type()
)
mscTraceSessionX25VcPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcPreviousDiagnosticCode.setStatus("mandatory")


class _MscTraceSessionX25VcCalledNpi_Type(Integer32):
    """Custom type mscTraceSessionX25VcCalledNpi based on Integer32"""
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


_MscTraceSessionX25VcCalledNpi_Type.__name__ = "Integer32"
_MscTraceSessionX25VcCalledNpi_Object = MibTableColumn
mscTraceSessionX25VcCalledNpi = _MscTraceSessionX25VcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 6),
    _MscTraceSessionX25VcCalledNpi_Type()
)
mscTraceSessionX25VcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcCalledNpi.setStatus("mandatory")


class _MscTraceSessionX25VcCalledDna_Type(DigitString):
    """Custom type mscTraceSessionX25VcCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscTraceSessionX25VcCalledDna_Type.__name__ = "DigitString"
_MscTraceSessionX25VcCalledDna_Object = MibTableColumn
mscTraceSessionX25VcCalledDna = _MscTraceSessionX25VcCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 7),
    _MscTraceSessionX25VcCalledDna_Type()
)
mscTraceSessionX25VcCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcCalledDna.setStatus("mandatory")


class _MscTraceSessionX25VcCalledLcn_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscTraceSessionX25VcCalledLcn_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcCalledLcn_Object = MibTableColumn
mscTraceSessionX25VcCalledLcn = _MscTraceSessionX25VcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 8),
    _MscTraceSessionX25VcCalledLcn_Type()
)
mscTraceSessionX25VcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcCalledLcn.setStatus("mandatory")


class _MscTraceSessionX25VcCallingNpi_Type(Integer32):
    """Custom type mscTraceSessionX25VcCallingNpi based on Integer32"""
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


_MscTraceSessionX25VcCallingNpi_Type.__name__ = "Integer32"
_MscTraceSessionX25VcCallingNpi_Object = MibTableColumn
mscTraceSessionX25VcCallingNpi = _MscTraceSessionX25VcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 9),
    _MscTraceSessionX25VcCallingNpi_Type()
)
mscTraceSessionX25VcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcCallingNpi.setStatus("mandatory")


class _MscTraceSessionX25VcCallingDna_Type(DigitString):
    """Custom type mscTraceSessionX25VcCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscTraceSessionX25VcCallingDna_Type.__name__ = "DigitString"
_MscTraceSessionX25VcCallingDna_Object = MibTableColumn
mscTraceSessionX25VcCallingDna = _MscTraceSessionX25VcCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 10),
    _MscTraceSessionX25VcCallingDna_Type()
)
mscTraceSessionX25VcCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcCallingDna.setStatus("mandatory")


class _MscTraceSessionX25VcCallingLcn_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscTraceSessionX25VcCallingLcn_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcCallingLcn_Object = MibTableColumn
mscTraceSessionX25VcCallingLcn = _MscTraceSessionX25VcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 11),
    _MscTraceSessionX25VcCallingLcn_Type()
)
mscTraceSessionX25VcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcCallingLcn.setStatus("mandatory")


class _MscTraceSessionX25VcAccountingEnabled_Type(Integer32):
    """Custom type mscTraceSessionX25VcAccountingEnabled based on Integer32"""
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


_MscTraceSessionX25VcAccountingEnabled_Type.__name__ = "Integer32"
_MscTraceSessionX25VcAccountingEnabled_Object = MibTableColumn
mscTraceSessionX25VcAccountingEnabled = _MscTraceSessionX25VcAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 12),
    _MscTraceSessionX25VcAccountingEnabled_Type()
)
mscTraceSessionX25VcAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcAccountingEnabled.setStatus("mandatory")


class _MscTraceSessionX25VcFastSelectCall_Type(Integer32):
    """Custom type mscTraceSessionX25VcFastSelectCall based on Integer32"""
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


_MscTraceSessionX25VcFastSelectCall_Type.__name__ = "Integer32"
_MscTraceSessionX25VcFastSelectCall_Object = MibTableColumn
mscTraceSessionX25VcFastSelectCall = _MscTraceSessionX25VcFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 13),
    _MscTraceSessionX25VcFastSelectCall_Type()
)
mscTraceSessionX25VcFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcFastSelectCall.setStatus("mandatory")


class _MscTraceSessionX25VcLocalRxPktSize_Type(Integer32):
    """Custom type mscTraceSessionX25VcLocalRxPktSize based on Integer32"""
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


_MscTraceSessionX25VcLocalRxPktSize_Type.__name__ = "Integer32"
_MscTraceSessionX25VcLocalRxPktSize_Object = MibTableColumn
mscTraceSessionX25VcLocalRxPktSize = _MscTraceSessionX25VcLocalRxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 14),
    _MscTraceSessionX25VcLocalRxPktSize_Type()
)
mscTraceSessionX25VcLocalRxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcLocalRxPktSize.setStatus("mandatory")


class _MscTraceSessionX25VcLocalTxPktSize_Type(Integer32):
    """Custom type mscTraceSessionX25VcLocalTxPktSize based on Integer32"""
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


_MscTraceSessionX25VcLocalTxPktSize_Type.__name__ = "Integer32"
_MscTraceSessionX25VcLocalTxPktSize_Object = MibTableColumn
mscTraceSessionX25VcLocalTxPktSize = _MscTraceSessionX25VcLocalTxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 15),
    _MscTraceSessionX25VcLocalTxPktSize_Type()
)
mscTraceSessionX25VcLocalTxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcLocalTxPktSize.setStatus("mandatory")


class _MscTraceSessionX25VcLocalTxWindowSize_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcLocalTxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MscTraceSessionX25VcLocalTxWindowSize_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcLocalTxWindowSize_Object = MibTableColumn
mscTraceSessionX25VcLocalTxWindowSize = _MscTraceSessionX25VcLocalTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 16),
    _MscTraceSessionX25VcLocalTxWindowSize_Type()
)
mscTraceSessionX25VcLocalTxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcLocalTxWindowSize.setStatus("mandatory")


class _MscTraceSessionX25VcLocalRxWindowSize_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcLocalRxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MscTraceSessionX25VcLocalRxWindowSize_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcLocalRxWindowSize_Object = MibTableColumn
mscTraceSessionX25VcLocalRxWindowSize = _MscTraceSessionX25VcLocalRxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 17),
    _MscTraceSessionX25VcLocalRxWindowSize_Type()
)
mscTraceSessionX25VcLocalRxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcLocalRxWindowSize.setStatus("mandatory")


class _MscTraceSessionX25VcPathReliability_Type(Integer32):
    """Custom type mscTraceSessionX25VcPathReliability based on Integer32"""
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


_MscTraceSessionX25VcPathReliability_Type.__name__ = "Integer32"
_MscTraceSessionX25VcPathReliability_Object = MibTableColumn
mscTraceSessionX25VcPathReliability = _MscTraceSessionX25VcPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 19),
    _MscTraceSessionX25VcPathReliability_Type()
)
mscTraceSessionX25VcPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcPathReliability.setStatus("mandatory")


class _MscTraceSessionX25VcAccountingEnd_Type(Integer32):
    """Custom type mscTraceSessionX25VcAccountingEnd based on Integer32"""
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


_MscTraceSessionX25VcAccountingEnd_Type.__name__ = "Integer32"
_MscTraceSessionX25VcAccountingEnd_Object = MibTableColumn
mscTraceSessionX25VcAccountingEnd = _MscTraceSessionX25VcAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 20),
    _MscTraceSessionX25VcAccountingEnd_Type()
)
mscTraceSessionX25VcAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcAccountingEnd.setStatus("mandatory")


class _MscTraceSessionX25VcPriority_Type(Integer32):
    """Custom type mscTraceSessionX25VcPriority based on Integer32"""
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


_MscTraceSessionX25VcPriority_Type.__name__ = "Integer32"
_MscTraceSessionX25VcPriority_Object = MibTableColumn
mscTraceSessionX25VcPriority = _MscTraceSessionX25VcPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 21),
    _MscTraceSessionX25VcPriority_Type()
)
mscTraceSessionX25VcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcPriority.setStatus("mandatory")


class _MscTraceSessionX25VcSegmentSize_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscTraceSessionX25VcSegmentSize_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcSegmentSize_Object = MibTableColumn
mscTraceSessionX25VcSegmentSize = _MscTraceSessionX25VcSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 22),
    _MscTraceSessionX25VcSegmentSize_Type()
)
mscTraceSessionX25VcSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcSegmentSize.setStatus("mandatory")


class _MscTraceSessionX25VcSubnetTxPktSize_Type(Integer32):
    """Custom type mscTraceSessionX25VcSubnetTxPktSize based on Integer32"""
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


_MscTraceSessionX25VcSubnetTxPktSize_Type.__name__ = "Integer32"
_MscTraceSessionX25VcSubnetTxPktSize_Object = MibTableColumn
mscTraceSessionX25VcSubnetTxPktSize = _MscTraceSessionX25VcSubnetTxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 23),
    _MscTraceSessionX25VcSubnetTxPktSize_Type()
)
mscTraceSessionX25VcSubnetTxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcSubnetTxPktSize.setStatus("mandatory")


class _MscTraceSessionX25VcSubnetTxWindowSize_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcSubnetTxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscTraceSessionX25VcSubnetTxWindowSize_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcSubnetTxWindowSize_Object = MibTableColumn
mscTraceSessionX25VcSubnetTxWindowSize = _MscTraceSessionX25VcSubnetTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 24),
    _MscTraceSessionX25VcSubnetTxWindowSize_Type()
)
mscTraceSessionX25VcSubnetTxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcSubnetTxWindowSize.setStatus("mandatory")


class _MscTraceSessionX25VcSubnetRxPktSize_Type(Integer32):
    """Custom type mscTraceSessionX25VcSubnetRxPktSize based on Integer32"""
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


_MscTraceSessionX25VcSubnetRxPktSize_Type.__name__ = "Integer32"
_MscTraceSessionX25VcSubnetRxPktSize_Object = MibTableColumn
mscTraceSessionX25VcSubnetRxPktSize = _MscTraceSessionX25VcSubnetRxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 25),
    _MscTraceSessionX25VcSubnetRxPktSize_Type()
)
mscTraceSessionX25VcSubnetRxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcSubnetRxPktSize.setStatus("mandatory")


class _MscTraceSessionX25VcSubnetRxWindowSize_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcSubnetRxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscTraceSessionX25VcSubnetRxWindowSize_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcSubnetRxWindowSize_Object = MibTableColumn
mscTraceSessionX25VcSubnetRxWindowSize = _MscTraceSessionX25VcSubnetRxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 26),
    _MscTraceSessionX25VcSubnetRxWindowSize_Type()
)
mscTraceSessionX25VcSubnetRxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcSubnetRxWindowSize.setStatus("mandatory")


class _MscTraceSessionX25VcMaxSubnetPktSize_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscTraceSessionX25VcMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcMaxSubnetPktSize_Object = MibTableColumn
mscTraceSessionX25VcMaxSubnetPktSize = _MscTraceSessionX25VcMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 27),
    _MscTraceSessionX25VcMaxSubnetPktSize_Type()
)
mscTraceSessionX25VcMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcMaxSubnetPktSize.setStatus("mandatory")


class _MscTraceSessionX25VcTransferPriorityToNetwork_Type(Integer32):
    """Custom type mscTraceSessionX25VcTransferPriorityToNetwork based on Integer32"""
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


_MscTraceSessionX25VcTransferPriorityToNetwork_Type.__name__ = "Integer32"
_MscTraceSessionX25VcTransferPriorityToNetwork_Object = MibTableColumn
mscTraceSessionX25VcTransferPriorityToNetwork = _MscTraceSessionX25VcTransferPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 28),
    _MscTraceSessionX25VcTransferPriorityToNetwork_Type()
)
mscTraceSessionX25VcTransferPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcTransferPriorityToNetwork.setStatus("mandatory")


class _MscTraceSessionX25VcTransferPriorityFromNetwork_Type(Integer32):
    """Custom type mscTraceSessionX25VcTransferPriorityFromNetwork based on Integer32"""
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


_MscTraceSessionX25VcTransferPriorityFromNetwork_Type.__name__ = "Integer32"
_MscTraceSessionX25VcTransferPriorityFromNetwork_Object = MibTableColumn
mscTraceSessionX25VcTransferPriorityFromNetwork = _MscTraceSessionX25VcTransferPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 10, 1, 29),
    _MscTraceSessionX25VcTransferPriorityFromNetwork_Type()
)
mscTraceSessionX25VcTransferPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcTransferPriorityFromNetwork.setStatus("mandatory")
_MscTraceSessionX25VcIntdTable_Object = MibTable
mscTraceSessionX25VcIntdTable = _MscTraceSessionX25VcIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 11)
)
if mibBuilder.loadTexts:
    mscTraceSessionX25VcIntdTable.setStatus("mandatory")
_MscTraceSessionX25VcIntdEntry_Object = MibTableRow
mscTraceSessionX25VcIntdEntry = _MscTraceSessionX25VcIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 11, 1)
)
mscTraceSessionX25VcIntdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceSessionIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceSessionX25Index"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceSessionX25VcIndex"),
)
if mibBuilder.loadTexts:
    mscTraceSessionX25VcIntdEntry.setStatus("mandatory")


class _MscTraceSessionX25VcCallReferenceNumber_Type(Hex):
    """Custom type mscTraceSessionX25VcCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscTraceSessionX25VcCallReferenceNumber_Type.__name__ = "Hex"
_MscTraceSessionX25VcCallReferenceNumber_Object = MibTableColumn
mscTraceSessionX25VcCallReferenceNumber = _MscTraceSessionX25VcCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 11, 1, 1),
    _MscTraceSessionX25VcCallReferenceNumber_Type()
)
mscTraceSessionX25VcCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcCallReferenceNumber.setStatus("obsolete")


class _MscTraceSessionX25VcElapsedTimeTillNow_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscTraceSessionX25VcElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcElapsedTimeTillNow_Object = MibTableColumn
mscTraceSessionX25VcElapsedTimeTillNow = _MscTraceSessionX25VcElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 11, 1, 2),
    _MscTraceSessionX25VcElapsedTimeTillNow_Type()
)
mscTraceSessionX25VcElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcElapsedTimeTillNow.setStatus("mandatory")


class _MscTraceSessionX25VcSegmentsRx_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscTraceSessionX25VcSegmentsRx_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcSegmentsRx_Object = MibTableColumn
mscTraceSessionX25VcSegmentsRx = _MscTraceSessionX25VcSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 11, 1, 3),
    _MscTraceSessionX25VcSegmentsRx_Type()
)
mscTraceSessionX25VcSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcSegmentsRx.setStatus("mandatory")


class _MscTraceSessionX25VcSegmentsSent_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscTraceSessionX25VcSegmentsSent_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcSegmentsSent_Object = MibTableColumn
mscTraceSessionX25VcSegmentsSent = _MscTraceSessionX25VcSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 11, 1, 4),
    _MscTraceSessionX25VcSegmentsSent_Type()
)
mscTraceSessionX25VcSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcSegmentsSent.setStatus("mandatory")


class _MscTraceSessionX25VcStartTime_Type(EnterpriseDateAndTime):
    """Custom type mscTraceSessionX25VcStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscTraceSessionX25VcStartTime_Type.__name__ = "EnterpriseDateAndTime"
_MscTraceSessionX25VcStartTime_Object = MibTableColumn
mscTraceSessionX25VcStartTime = _MscTraceSessionX25VcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 11, 1, 5),
    _MscTraceSessionX25VcStartTime_Type()
)
mscTraceSessionX25VcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcStartTime.setStatus("mandatory")


class _MscTraceSessionX25VcCallReferenceNumberDecimal_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcCallReferenceNumberDecimal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscTraceSessionX25VcCallReferenceNumberDecimal_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcCallReferenceNumberDecimal_Object = MibTableColumn
mscTraceSessionX25VcCallReferenceNumberDecimal = _MscTraceSessionX25VcCallReferenceNumberDecimal_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 11, 1, 7),
    _MscTraceSessionX25VcCallReferenceNumberDecimal_Type()
)
mscTraceSessionX25VcCallReferenceNumberDecimal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcCallReferenceNumberDecimal.setStatus("mandatory")
_MscTraceSessionX25VcStatsTable_Object = MibTable
mscTraceSessionX25VcStatsTable = _MscTraceSessionX25VcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 12)
)
if mibBuilder.loadTexts:
    mscTraceSessionX25VcStatsTable.setStatus("mandatory")
_MscTraceSessionX25VcStatsEntry_Object = MibTableRow
mscTraceSessionX25VcStatsEntry = _MscTraceSessionX25VcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 12, 1)
)
mscTraceSessionX25VcStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceSessionIndex"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceSessionX25Index"),
    (0, "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB", "mscTraceSessionX25VcIndex"),
)
if mibBuilder.loadTexts:
    mscTraceSessionX25VcStatsEntry.setStatus("mandatory")


class _MscTraceSessionX25VcAckStackingTimeouts_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcAckStackingTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionX25VcAckStackingTimeouts_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcAckStackingTimeouts_Object = MibTableColumn
mscTraceSessionX25VcAckStackingTimeouts = _MscTraceSessionX25VcAckStackingTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 12, 1, 1),
    _MscTraceSessionX25VcAckStackingTimeouts_Type()
)
mscTraceSessionX25VcAckStackingTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcAckStackingTimeouts.setStatus("mandatory")


class _MscTraceSessionX25VcOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionX25VcOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcOutOfRangeFrmFromSubnet_Object = MibTableColumn
mscTraceSessionX25VcOutOfRangeFrmFromSubnet = _MscTraceSessionX25VcOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 12, 1, 2),
    _MscTraceSessionX25VcOutOfRangeFrmFromSubnet_Type()
)
mscTraceSessionX25VcOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _MscTraceSessionX25VcDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionX25VcDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcDuplicatesFromSubnet_Object = MibTableColumn
mscTraceSessionX25VcDuplicatesFromSubnet = _MscTraceSessionX25VcDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 12, 1, 3),
    _MscTraceSessionX25VcDuplicatesFromSubnet_Type()
)
mscTraceSessionX25VcDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcDuplicatesFromSubnet.setStatus("mandatory")


class _MscTraceSessionX25VcFrmRetryTimeouts_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcFrmRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionX25VcFrmRetryTimeouts_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcFrmRetryTimeouts_Object = MibTableColumn
mscTraceSessionX25VcFrmRetryTimeouts = _MscTraceSessionX25VcFrmRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 12, 1, 4),
    _MscTraceSessionX25VcFrmRetryTimeouts_Type()
)
mscTraceSessionX25VcFrmRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcFrmRetryTimeouts.setStatus("mandatory")


class _MscTraceSessionX25VcPeakRetryQueueSize_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionX25VcPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcPeakRetryQueueSize_Object = MibTableColumn
mscTraceSessionX25VcPeakRetryQueueSize = _MscTraceSessionX25VcPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 12, 1, 5),
    _MscTraceSessionX25VcPeakRetryQueueSize_Type()
)
mscTraceSessionX25VcPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcPeakRetryQueueSize.setStatus("mandatory")


class _MscTraceSessionX25VcPeakOoSeqQueueSize_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcPeakOoSeqQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionX25VcPeakOoSeqQueueSize_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcPeakOoSeqQueueSize_Object = MibTableColumn
mscTraceSessionX25VcPeakOoSeqQueueSize = _MscTraceSessionX25VcPeakOoSeqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 12, 1, 6),
    _MscTraceSessionX25VcPeakOoSeqQueueSize_Type()
)
mscTraceSessionX25VcPeakOoSeqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcPeakOoSeqQueueSize.setStatus("mandatory")


class _MscTraceSessionX25VcPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionX25VcPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcPeakOoSeqFrmForwarded_Object = MibTableColumn
mscTraceSessionX25VcPeakOoSeqFrmForwarded = _MscTraceSessionX25VcPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 12, 1, 7),
    _MscTraceSessionX25VcPeakOoSeqFrmForwarded_Type()
)
mscTraceSessionX25VcPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcPeakOoSeqFrmForwarded.setStatus("mandatory")


class _MscTraceSessionX25VcPeakStackedAcksRx_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcPeakStackedAcksRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionX25VcPeakStackedAcksRx_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcPeakStackedAcksRx_Object = MibTableColumn
mscTraceSessionX25VcPeakStackedAcksRx = _MscTraceSessionX25VcPeakStackedAcksRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 12, 1, 8),
    _MscTraceSessionX25VcPeakStackedAcksRx_Type()
)
mscTraceSessionX25VcPeakStackedAcksRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcPeakStackedAcksRx.setStatus("mandatory")


class _MscTraceSessionX25VcSubnetRecoveries_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionX25VcSubnetRecoveries_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcSubnetRecoveries_Object = MibTableColumn
mscTraceSessionX25VcSubnetRecoveries = _MscTraceSessionX25VcSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 12, 1, 9),
    _MscTraceSessionX25VcSubnetRecoveries_Type()
)
mscTraceSessionX25VcSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcSubnetRecoveries.setStatus("mandatory")


class _MscTraceSessionX25VcWindowClosuresToSubnet_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcWindowClosuresToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionX25VcWindowClosuresToSubnet_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcWindowClosuresToSubnet_Object = MibTableColumn
mscTraceSessionX25VcWindowClosuresToSubnet = _MscTraceSessionX25VcWindowClosuresToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 12, 1, 10),
    _MscTraceSessionX25VcWindowClosuresToSubnet_Type()
)
mscTraceSessionX25VcWindowClosuresToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcWindowClosuresToSubnet.setStatus("mandatory")


class _MscTraceSessionX25VcWindowClosuresFromSubnet_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcWindowClosuresFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionX25VcWindowClosuresFromSubnet_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcWindowClosuresFromSubnet_Object = MibTableColumn
mscTraceSessionX25VcWindowClosuresFromSubnet = _MscTraceSessionX25VcWindowClosuresFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 12, 1, 11),
    _MscTraceSessionX25VcWindowClosuresFromSubnet_Type()
)
mscTraceSessionX25VcWindowClosuresFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcWindowClosuresFromSubnet.setStatus("mandatory")


class _MscTraceSessionX25VcWrTriggers_Type(Unsigned32):
    """Custom type mscTraceSessionX25VcWrTriggers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionX25VcWrTriggers_Type.__name__ = "Unsigned32"
_MscTraceSessionX25VcWrTriggers_Object = MibTableColumn
mscTraceSessionX25VcWrTriggers = _MscTraceSessionX25VcWrTriggers_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 2, 2, 12, 1, 12),
    _MscTraceSessionX25VcWrTriggers_Type()
)
mscTraceSessionX25VcWrTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionX25VcWrTriggers.setStatus("mandatory")
_X25TraceRcvrMIB_ObjectIdentity = ObjectIdentity
x25TraceRcvrMIB = _X25TraceRcvrMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 62)
)
_X25TraceRcvrGroup_ObjectIdentity = ObjectIdentity
x25TraceRcvrGroup = _X25TraceRcvrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 62, 1)
)
_X25TraceRcvrGroupCA_ObjectIdentity = ObjectIdentity
x25TraceRcvrGroupCA = _X25TraceRcvrGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 62, 1, 1)
)
_X25TraceRcvrGroupCA02_ObjectIdentity = ObjectIdentity
x25TraceRcvrGroupCA02 = _X25TraceRcvrGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 62, 1, 1, 3)
)
_X25TraceRcvrGroupCA02A_ObjectIdentity = ObjectIdentity
x25TraceRcvrGroupCA02A = _X25TraceRcvrGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 62, 1, 1, 3, 2)
)
_X25TraceRcvrCapabilities_ObjectIdentity = ObjectIdentity
x25TraceRcvrCapabilities = _X25TraceRcvrCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 62, 3)
)
_X25TraceRcvrCapabilitiesCA_ObjectIdentity = ObjectIdentity
x25TraceRcvrCapabilitiesCA = _X25TraceRcvrCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 62, 3, 1)
)
_X25TraceRcvrCapabilitiesCA02_ObjectIdentity = ObjectIdentity
x25TraceRcvrCapabilitiesCA02 = _X25TraceRcvrCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 62, 3, 1, 3)
)
_X25TraceRcvrCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
x25TraceRcvrCapabilitiesCA02A = _X25TraceRcvrCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 62, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-X25TraceRcvrMIB",
    **{"mscTraceRcvrX25": mscTraceRcvrX25,
       "mscTraceRcvrX25RowStatusTable": mscTraceRcvrX25RowStatusTable,
       "mscTraceRcvrX25RowStatusEntry": mscTraceRcvrX25RowStatusEntry,
       "mscTraceRcvrX25RowStatus": mscTraceRcvrX25RowStatus,
       "mscTraceRcvrX25ComponentName": mscTraceRcvrX25ComponentName,
       "mscTraceRcvrX25StorageType": mscTraceRcvrX25StorageType,
       "mscTraceRcvrX25Index": mscTraceRcvrX25Index,
       "mscTraceRcvrX25Dna": mscTraceRcvrX25Dna,
       "mscTraceRcvrX25DnaRowStatusTable": mscTraceRcvrX25DnaRowStatusTable,
       "mscTraceRcvrX25DnaRowStatusEntry": mscTraceRcvrX25DnaRowStatusEntry,
       "mscTraceRcvrX25DnaRowStatus": mscTraceRcvrX25DnaRowStatus,
       "mscTraceRcvrX25DnaComponentName": mscTraceRcvrX25DnaComponentName,
       "mscTraceRcvrX25DnaStorageType": mscTraceRcvrX25DnaStorageType,
       "mscTraceRcvrX25DnaIndex": mscTraceRcvrX25DnaIndex,
       "mscTraceRcvrX25DnaCug": mscTraceRcvrX25DnaCug,
       "mscTraceRcvrX25DnaCugRowStatusTable": mscTraceRcvrX25DnaCugRowStatusTable,
       "mscTraceRcvrX25DnaCugRowStatusEntry": mscTraceRcvrX25DnaCugRowStatusEntry,
       "mscTraceRcvrX25DnaCugRowStatus": mscTraceRcvrX25DnaCugRowStatus,
       "mscTraceRcvrX25DnaCugComponentName": mscTraceRcvrX25DnaCugComponentName,
       "mscTraceRcvrX25DnaCugStorageType": mscTraceRcvrX25DnaCugStorageType,
       "mscTraceRcvrX25DnaCugIndex": mscTraceRcvrX25DnaCugIndex,
       "mscTraceRcvrX25DnaCugCugOptionsTable": mscTraceRcvrX25DnaCugCugOptionsTable,
       "mscTraceRcvrX25DnaCugCugOptionsEntry": mscTraceRcvrX25DnaCugCugOptionsEntry,
       "mscTraceRcvrX25DnaCugType": mscTraceRcvrX25DnaCugType,
       "mscTraceRcvrX25DnaCugDnic": mscTraceRcvrX25DnaCugDnic,
       "mscTraceRcvrX25DnaCugInterlockCode": mscTraceRcvrX25DnaCugInterlockCode,
       "mscTraceRcvrX25DnaCugPreferential": mscTraceRcvrX25DnaCugPreferential,
       "mscTraceRcvrX25DnaCugOutCalls": mscTraceRcvrX25DnaCugOutCalls,
       "mscTraceRcvrX25DnaCugIncCalls": mscTraceRcvrX25DnaCugIncCalls,
       "mscTraceRcvrX25DnaCugPrivileged": mscTraceRcvrX25DnaCugPrivileged,
       "mscTraceRcvrX25DnaAddressTable": mscTraceRcvrX25DnaAddressTable,
       "mscTraceRcvrX25DnaAddressEntry": mscTraceRcvrX25DnaAddressEntry,
       "mscTraceRcvrX25DnaNumberingPlanIndicator": mscTraceRcvrX25DnaNumberingPlanIndicator,
       "mscTraceRcvrX25DnaDataNetworkAddress": mscTraceRcvrX25DnaDataNetworkAddress,
       "mscTraceRcvrX25DnaOutgoingOptionsTable": mscTraceRcvrX25DnaOutgoingOptionsTable,
       "mscTraceRcvrX25DnaOutgoingOptionsEntry": mscTraceRcvrX25DnaOutgoingOptionsEntry,
       "mscTraceRcvrX25DnaOutCalls": mscTraceRcvrX25DnaOutCalls,
       "mscTraceRcvrX25DnaOutDefaultPriority": mscTraceRcvrX25DnaOutDefaultPriority,
       "mscTraceRcvrX25DnaOutIntl": mscTraceRcvrX25DnaOutIntl,
       "mscTraceRcvrX25DnaOutDefaultPathSensitivity": mscTraceRcvrX25DnaOutDefaultPathSensitivity,
       "mscTraceRcvrX25DnaOutDefaultPathReliability": mscTraceRcvrX25DnaOutDefaultPathReliability,
       "mscTraceRcvrX25DnaOutPathReliabilityOverRide": mscTraceRcvrX25DnaOutPathReliabilityOverRide,
       "mscTraceRcvrX25DnaOutPathReliabilitySignal": mscTraceRcvrX25DnaOutPathReliabilitySignal,
       "mscTraceRcvrX25DnaOutAccess": mscTraceRcvrX25DnaOutAccess,
       "mscTraceRcvrX25DnaIncomingOptionsTable": mscTraceRcvrX25DnaIncomingOptionsTable,
       "mscTraceRcvrX25DnaIncomingOptionsEntry": mscTraceRcvrX25DnaIncomingOptionsEntry,
       "mscTraceRcvrX25DnaIncCalls": mscTraceRcvrX25DnaIncCalls,
       "mscTraceRcvrX25DnaCallOptionsTable": mscTraceRcvrX25DnaCallOptionsTable,
       "mscTraceRcvrX25DnaCallOptionsEntry": mscTraceRcvrX25DnaCallOptionsEntry,
       "mscTraceRcvrX25DnaPacketSizes": mscTraceRcvrX25DnaPacketSizes,
       "mscTraceRcvrX25DnaDefaultRecvFrmNetworkPacketSize": mscTraceRcvrX25DnaDefaultRecvFrmNetworkPacketSize,
       "mscTraceRcvrX25DnaDefaultSendToNetworkPacketSize": mscTraceRcvrX25DnaDefaultSendToNetworkPacketSize,
       "mscTraceRcvrX25DnaDefaultRecvFrmNetworkThruputClass": mscTraceRcvrX25DnaDefaultRecvFrmNetworkThruputClass,
       "mscTraceRcvrX25DnaDefaultSendToNetworkThruputClass": mscTraceRcvrX25DnaDefaultSendToNetworkThruputClass,
       "mscTraceRcvrX25DnaDefaultRecvFrmNetworkWindowSize": mscTraceRcvrX25DnaDefaultRecvFrmNetworkWindowSize,
       "mscTraceRcvrX25DnaDefaultSendToNetworkWindowSize": mscTraceRcvrX25DnaDefaultSendToNetworkWindowSize,
       "mscTraceRcvrX25DnaPacketSizeNegotiation": mscTraceRcvrX25DnaPacketSizeNegotiation,
       "mscTraceRcvrX25DnaCugFormat": mscTraceRcvrX25DnaCugFormat,
       "mscTraceRcvrX25Dc": mscTraceRcvrX25Dc,
       "mscTraceRcvrX25DcRowStatusTable": mscTraceRcvrX25DcRowStatusTable,
       "mscTraceRcvrX25DcRowStatusEntry": mscTraceRcvrX25DcRowStatusEntry,
       "mscTraceRcvrX25DcRowStatus": mscTraceRcvrX25DcRowStatus,
       "mscTraceRcvrX25DcComponentName": mscTraceRcvrX25DcComponentName,
       "mscTraceRcvrX25DcStorageType": mscTraceRcvrX25DcStorageType,
       "mscTraceRcvrX25DcIndex": mscTraceRcvrX25DcIndex,
       "mscTraceRcvrX25DcOptionsTable": mscTraceRcvrX25DcOptionsTable,
       "mscTraceRcvrX25DcOptionsEntry": mscTraceRcvrX25DcOptionsEntry,
       "mscTraceRcvrX25DcRemoteNpi": mscTraceRcvrX25DcRemoteNpi,
       "mscTraceRcvrX25DcRemoteDna": mscTraceRcvrX25DcRemoteDna,
       "mscTraceRcvrX25DcType": mscTraceRcvrX25DcType,
       "mscTraceRcvrX25DcUserData": mscTraceRcvrX25DcUserData,
       "mscTraceSessionX25": mscTraceSessionX25,
       "mscTraceSessionX25RowStatusTable": mscTraceSessionX25RowStatusTable,
       "mscTraceSessionX25RowStatusEntry": mscTraceSessionX25RowStatusEntry,
       "mscTraceSessionX25RowStatus": mscTraceSessionX25RowStatus,
       "mscTraceSessionX25ComponentName": mscTraceSessionX25ComponentName,
       "mscTraceSessionX25StorageType": mscTraceSessionX25StorageType,
       "mscTraceSessionX25Index": mscTraceSessionX25Index,
       "mscTraceSessionX25Vc": mscTraceSessionX25Vc,
       "mscTraceSessionX25VcRowStatusTable": mscTraceSessionX25VcRowStatusTable,
       "mscTraceSessionX25VcRowStatusEntry": mscTraceSessionX25VcRowStatusEntry,
       "mscTraceSessionX25VcRowStatus": mscTraceSessionX25VcRowStatus,
       "mscTraceSessionX25VcComponentName": mscTraceSessionX25VcComponentName,
       "mscTraceSessionX25VcStorageType": mscTraceSessionX25VcStorageType,
       "mscTraceSessionX25VcIndex": mscTraceSessionX25VcIndex,
       "mscTraceSessionX25VcCadTable": mscTraceSessionX25VcCadTable,
       "mscTraceSessionX25VcCadEntry": mscTraceSessionX25VcCadEntry,
       "mscTraceSessionX25VcType": mscTraceSessionX25VcType,
       "mscTraceSessionX25VcState": mscTraceSessionX25VcState,
       "mscTraceSessionX25VcPreviousState": mscTraceSessionX25VcPreviousState,
       "mscTraceSessionX25VcDiagnosticCode": mscTraceSessionX25VcDiagnosticCode,
       "mscTraceSessionX25VcPreviousDiagnosticCode": mscTraceSessionX25VcPreviousDiagnosticCode,
       "mscTraceSessionX25VcCalledNpi": mscTraceSessionX25VcCalledNpi,
       "mscTraceSessionX25VcCalledDna": mscTraceSessionX25VcCalledDna,
       "mscTraceSessionX25VcCalledLcn": mscTraceSessionX25VcCalledLcn,
       "mscTraceSessionX25VcCallingNpi": mscTraceSessionX25VcCallingNpi,
       "mscTraceSessionX25VcCallingDna": mscTraceSessionX25VcCallingDna,
       "mscTraceSessionX25VcCallingLcn": mscTraceSessionX25VcCallingLcn,
       "mscTraceSessionX25VcAccountingEnabled": mscTraceSessionX25VcAccountingEnabled,
       "mscTraceSessionX25VcFastSelectCall": mscTraceSessionX25VcFastSelectCall,
       "mscTraceSessionX25VcLocalRxPktSize": mscTraceSessionX25VcLocalRxPktSize,
       "mscTraceSessionX25VcLocalTxPktSize": mscTraceSessionX25VcLocalTxPktSize,
       "mscTraceSessionX25VcLocalTxWindowSize": mscTraceSessionX25VcLocalTxWindowSize,
       "mscTraceSessionX25VcLocalRxWindowSize": mscTraceSessionX25VcLocalRxWindowSize,
       "mscTraceSessionX25VcPathReliability": mscTraceSessionX25VcPathReliability,
       "mscTraceSessionX25VcAccountingEnd": mscTraceSessionX25VcAccountingEnd,
       "mscTraceSessionX25VcPriority": mscTraceSessionX25VcPriority,
       "mscTraceSessionX25VcSegmentSize": mscTraceSessionX25VcSegmentSize,
       "mscTraceSessionX25VcSubnetTxPktSize": mscTraceSessionX25VcSubnetTxPktSize,
       "mscTraceSessionX25VcSubnetTxWindowSize": mscTraceSessionX25VcSubnetTxWindowSize,
       "mscTraceSessionX25VcSubnetRxPktSize": mscTraceSessionX25VcSubnetRxPktSize,
       "mscTraceSessionX25VcSubnetRxWindowSize": mscTraceSessionX25VcSubnetRxWindowSize,
       "mscTraceSessionX25VcMaxSubnetPktSize": mscTraceSessionX25VcMaxSubnetPktSize,
       "mscTraceSessionX25VcTransferPriorityToNetwork": mscTraceSessionX25VcTransferPriorityToNetwork,
       "mscTraceSessionX25VcTransferPriorityFromNetwork": mscTraceSessionX25VcTransferPriorityFromNetwork,
       "mscTraceSessionX25VcIntdTable": mscTraceSessionX25VcIntdTable,
       "mscTraceSessionX25VcIntdEntry": mscTraceSessionX25VcIntdEntry,
       "mscTraceSessionX25VcCallReferenceNumber": mscTraceSessionX25VcCallReferenceNumber,
       "mscTraceSessionX25VcElapsedTimeTillNow": mscTraceSessionX25VcElapsedTimeTillNow,
       "mscTraceSessionX25VcSegmentsRx": mscTraceSessionX25VcSegmentsRx,
       "mscTraceSessionX25VcSegmentsSent": mscTraceSessionX25VcSegmentsSent,
       "mscTraceSessionX25VcStartTime": mscTraceSessionX25VcStartTime,
       "mscTraceSessionX25VcCallReferenceNumberDecimal": mscTraceSessionX25VcCallReferenceNumberDecimal,
       "mscTraceSessionX25VcStatsTable": mscTraceSessionX25VcStatsTable,
       "mscTraceSessionX25VcStatsEntry": mscTraceSessionX25VcStatsEntry,
       "mscTraceSessionX25VcAckStackingTimeouts": mscTraceSessionX25VcAckStackingTimeouts,
       "mscTraceSessionX25VcOutOfRangeFrmFromSubnet": mscTraceSessionX25VcOutOfRangeFrmFromSubnet,
       "mscTraceSessionX25VcDuplicatesFromSubnet": mscTraceSessionX25VcDuplicatesFromSubnet,
       "mscTraceSessionX25VcFrmRetryTimeouts": mscTraceSessionX25VcFrmRetryTimeouts,
       "mscTraceSessionX25VcPeakRetryQueueSize": mscTraceSessionX25VcPeakRetryQueueSize,
       "mscTraceSessionX25VcPeakOoSeqQueueSize": mscTraceSessionX25VcPeakOoSeqQueueSize,
       "mscTraceSessionX25VcPeakOoSeqFrmForwarded": mscTraceSessionX25VcPeakOoSeqFrmForwarded,
       "mscTraceSessionX25VcPeakStackedAcksRx": mscTraceSessionX25VcPeakStackedAcksRx,
       "mscTraceSessionX25VcSubnetRecoveries": mscTraceSessionX25VcSubnetRecoveries,
       "mscTraceSessionX25VcWindowClosuresToSubnet": mscTraceSessionX25VcWindowClosuresToSubnet,
       "mscTraceSessionX25VcWindowClosuresFromSubnet": mscTraceSessionX25VcWindowClosuresFromSubnet,
       "mscTraceSessionX25VcWrTriggers": mscTraceSessionX25VcWrTriggers,
       "x25TraceRcvrMIB": x25TraceRcvrMIB,
       "x25TraceRcvrGroup": x25TraceRcvrGroup,
       "x25TraceRcvrGroupCA": x25TraceRcvrGroupCA,
       "x25TraceRcvrGroupCA02": x25TraceRcvrGroupCA02,
       "x25TraceRcvrGroupCA02A": x25TraceRcvrGroupCA02A,
       "x25TraceRcvrCapabilities": x25TraceRcvrCapabilities,
       "x25TraceRcvrCapabilitiesCA": x25TraceRcvrCapabilitiesCA,
       "x25TraceRcvrCapabilitiesCA02": x25TraceRcvrCapabilitiesCA02,
       "x25TraceRcvrCapabilitiesCA02A": x25TraceRcvrCapabilitiesCA02A}
)
