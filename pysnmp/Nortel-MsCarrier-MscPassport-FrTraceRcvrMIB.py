# SNMP MIB module (Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:22 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
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
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
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

_MscTraceRcvrFr_ObjectIdentity = ObjectIdentity
mscTraceRcvrFr = _MscTraceRcvrFr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3)
)
_MscTraceRcvrFrRowStatusTable_Object = MibTable
mscTraceRcvrFrRowStatusTable = _MscTraceRcvrFrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mscTraceRcvrFrRowStatusTable.setStatus("mandatory")
_MscTraceRcvrFrRowStatusEntry_Object = MibTableRow
mscTraceRcvrFrRowStatusEntry = _MscTraceRcvrFrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 1, 1)
)
mscTraceRcvrFrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceRcvrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceRcvrFrIndex"),
)
if mibBuilder.loadTexts:
    mscTraceRcvrFrRowStatusEntry.setStatus("mandatory")
_MscTraceRcvrFrRowStatus_Type = RowStatus
_MscTraceRcvrFrRowStatus_Object = MibTableColumn
mscTraceRcvrFrRowStatus = _MscTraceRcvrFrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 1, 1, 1),
    _MscTraceRcvrFrRowStatus_Type()
)
mscTraceRcvrFrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrFrRowStatus.setStatus("mandatory")
_MscTraceRcvrFrComponentName_Type = DisplayString
_MscTraceRcvrFrComponentName_Object = MibTableColumn
mscTraceRcvrFrComponentName = _MscTraceRcvrFrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 1, 1, 2),
    _MscTraceRcvrFrComponentName_Type()
)
mscTraceRcvrFrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrComponentName.setStatus("mandatory")
_MscTraceRcvrFrStorageType_Type = StorageType
_MscTraceRcvrFrStorageType_Object = MibTableColumn
mscTraceRcvrFrStorageType = _MscTraceRcvrFrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 1, 1, 4),
    _MscTraceRcvrFrStorageType_Type()
)
mscTraceRcvrFrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrStorageType.setStatus("mandatory")
_MscTraceRcvrFrIndex_Type = NonReplicated
_MscTraceRcvrFrIndex_Object = MibTableColumn
mscTraceRcvrFrIndex = _MscTraceRcvrFrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 1, 1, 10),
    _MscTraceRcvrFrIndex_Type()
)
mscTraceRcvrFrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTraceRcvrFrIndex.setStatus("mandatory")
_MscTraceRcvrFrDna_ObjectIdentity = ObjectIdentity
mscTraceRcvrFrDna = _MscTraceRcvrFrDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2)
)
_MscTraceRcvrFrDnaRowStatusTable_Object = MibTable
mscTraceRcvrFrDnaRowStatusTable = _MscTraceRcvrFrDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaRowStatusTable.setStatus("mandatory")
_MscTraceRcvrFrDnaRowStatusEntry_Object = MibTableRow
mscTraceRcvrFrDnaRowStatusEntry = _MscTraceRcvrFrDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 1, 1)
)
mscTraceRcvrFrDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceRcvrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceRcvrFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceRcvrFrDnaIndex"),
)
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaRowStatusEntry.setStatus("mandatory")
_MscTraceRcvrFrDnaRowStatus_Type = RowStatus
_MscTraceRcvrFrDnaRowStatus_Object = MibTableColumn
mscTraceRcvrFrDnaRowStatus = _MscTraceRcvrFrDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 1, 1, 1),
    _MscTraceRcvrFrDnaRowStatus_Type()
)
mscTraceRcvrFrDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaRowStatus.setStatus("mandatory")
_MscTraceRcvrFrDnaComponentName_Type = DisplayString
_MscTraceRcvrFrDnaComponentName_Object = MibTableColumn
mscTraceRcvrFrDnaComponentName = _MscTraceRcvrFrDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 1, 1, 2),
    _MscTraceRcvrFrDnaComponentName_Type()
)
mscTraceRcvrFrDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaComponentName.setStatus("mandatory")
_MscTraceRcvrFrDnaStorageType_Type = StorageType
_MscTraceRcvrFrDnaStorageType_Object = MibTableColumn
mscTraceRcvrFrDnaStorageType = _MscTraceRcvrFrDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 1, 1, 4),
    _MscTraceRcvrFrDnaStorageType_Type()
)
mscTraceRcvrFrDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaStorageType.setStatus("mandatory")
_MscTraceRcvrFrDnaIndex_Type = NonReplicated
_MscTraceRcvrFrDnaIndex_Object = MibTableColumn
mscTraceRcvrFrDnaIndex = _MscTraceRcvrFrDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 1, 1, 10),
    _MscTraceRcvrFrDnaIndex_Type()
)
mscTraceRcvrFrDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaIndex.setStatus("mandatory")
_MscTraceRcvrFrDnaCug_ObjectIdentity = ObjectIdentity
mscTraceRcvrFrDnaCug = _MscTraceRcvrFrDnaCug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 2)
)
_MscTraceRcvrFrDnaCugRowStatusTable_Object = MibTable
mscTraceRcvrFrDnaCugRowStatusTable = _MscTraceRcvrFrDnaCugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaCugRowStatusTable.setStatus("mandatory")
_MscTraceRcvrFrDnaCugRowStatusEntry_Object = MibTableRow
mscTraceRcvrFrDnaCugRowStatusEntry = _MscTraceRcvrFrDnaCugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 2, 1, 1)
)
mscTraceRcvrFrDnaCugRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceRcvrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceRcvrFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceRcvrFrDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceRcvrFrDnaCugIndex"),
)
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaCugRowStatusEntry.setStatus("mandatory")
_MscTraceRcvrFrDnaCugRowStatus_Type = RowStatus
_MscTraceRcvrFrDnaCugRowStatus_Object = MibTableColumn
mscTraceRcvrFrDnaCugRowStatus = _MscTraceRcvrFrDnaCugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 2, 1, 1, 1),
    _MscTraceRcvrFrDnaCugRowStatus_Type()
)
mscTraceRcvrFrDnaCugRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaCugRowStatus.setStatus("mandatory")
_MscTraceRcvrFrDnaCugComponentName_Type = DisplayString
_MscTraceRcvrFrDnaCugComponentName_Object = MibTableColumn
mscTraceRcvrFrDnaCugComponentName = _MscTraceRcvrFrDnaCugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 2, 1, 1, 2),
    _MscTraceRcvrFrDnaCugComponentName_Type()
)
mscTraceRcvrFrDnaCugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaCugComponentName.setStatus("mandatory")
_MscTraceRcvrFrDnaCugStorageType_Type = StorageType
_MscTraceRcvrFrDnaCugStorageType_Object = MibTableColumn
mscTraceRcvrFrDnaCugStorageType = _MscTraceRcvrFrDnaCugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 2, 1, 1, 4),
    _MscTraceRcvrFrDnaCugStorageType_Type()
)
mscTraceRcvrFrDnaCugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaCugStorageType.setStatus("mandatory")


class _MscTraceRcvrFrDnaCugIndex_Type(Integer32):
    """Custom type mscTraceRcvrFrDnaCugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MscTraceRcvrFrDnaCugIndex_Type.__name__ = "Integer32"
_MscTraceRcvrFrDnaCugIndex_Object = MibTableColumn
mscTraceRcvrFrDnaCugIndex = _MscTraceRcvrFrDnaCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 2, 1, 1, 10),
    _MscTraceRcvrFrDnaCugIndex_Type()
)
mscTraceRcvrFrDnaCugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaCugIndex.setStatus("mandatory")
_MscTraceRcvrFrDnaCugCugOptionsTable_Object = MibTable
mscTraceRcvrFrDnaCugCugOptionsTable = _MscTraceRcvrFrDnaCugCugOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaCugCugOptionsTable.setStatus("mandatory")
_MscTraceRcvrFrDnaCugCugOptionsEntry_Object = MibTableRow
mscTraceRcvrFrDnaCugCugOptionsEntry = _MscTraceRcvrFrDnaCugCugOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 2, 10, 1)
)
mscTraceRcvrFrDnaCugCugOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceRcvrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceRcvrFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceRcvrFrDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceRcvrFrDnaCugIndex"),
)
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaCugCugOptionsEntry.setStatus("mandatory")


class _MscTraceRcvrFrDnaCugType_Type(Integer32):
    """Custom type mscTraceRcvrFrDnaCugType based on Integer32"""
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


_MscTraceRcvrFrDnaCugType_Type.__name__ = "Integer32"
_MscTraceRcvrFrDnaCugType_Object = MibTableColumn
mscTraceRcvrFrDnaCugType = _MscTraceRcvrFrDnaCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 2, 10, 1, 1),
    _MscTraceRcvrFrDnaCugType_Type()
)
mscTraceRcvrFrDnaCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaCugType.setStatus("mandatory")


class _MscTraceRcvrFrDnaCugDnic_Type(DigitString):
    """Custom type mscTraceRcvrFrDnaCugDnic based on DigitString"""
    defaultHexValue = "30303030"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MscTraceRcvrFrDnaCugDnic_Type.__name__ = "DigitString"
_MscTraceRcvrFrDnaCugDnic_Object = MibTableColumn
mscTraceRcvrFrDnaCugDnic = _MscTraceRcvrFrDnaCugDnic_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 2, 10, 1, 2),
    _MscTraceRcvrFrDnaCugDnic_Type()
)
mscTraceRcvrFrDnaCugDnic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaCugDnic.setStatus("mandatory")


class _MscTraceRcvrFrDnaCugInterlockCode_Type(Unsigned32):
    """Custom type mscTraceRcvrFrDnaCugInterlockCode based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscTraceRcvrFrDnaCugInterlockCode_Type.__name__ = "Unsigned32"
_MscTraceRcvrFrDnaCugInterlockCode_Object = MibTableColumn
mscTraceRcvrFrDnaCugInterlockCode = _MscTraceRcvrFrDnaCugInterlockCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 2, 10, 1, 3),
    _MscTraceRcvrFrDnaCugInterlockCode_Type()
)
mscTraceRcvrFrDnaCugInterlockCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaCugInterlockCode.setStatus("mandatory")


class _MscTraceRcvrFrDnaCugPreferential_Type(Integer32):
    """Custom type mscTraceRcvrFrDnaCugPreferential based on Integer32"""
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


_MscTraceRcvrFrDnaCugPreferential_Type.__name__ = "Integer32"
_MscTraceRcvrFrDnaCugPreferential_Object = MibTableColumn
mscTraceRcvrFrDnaCugPreferential = _MscTraceRcvrFrDnaCugPreferential_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 2, 10, 1, 4),
    _MscTraceRcvrFrDnaCugPreferential_Type()
)
mscTraceRcvrFrDnaCugPreferential.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaCugPreferential.setStatus("mandatory")


class _MscTraceRcvrFrDnaCugOutCalls_Type(Integer32):
    """Custom type mscTraceRcvrFrDnaCugOutCalls based on Integer32"""
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


_MscTraceRcvrFrDnaCugOutCalls_Type.__name__ = "Integer32"
_MscTraceRcvrFrDnaCugOutCalls_Object = MibTableColumn
mscTraceRcvrFrDnaCugOutCalls = _MscTraceRcvrFrDnaCugOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 2, 10, 1, 5),
    _MscTraceRcvrFrDnaCugOutCalls_Type()
)
mscTraceRcvrFrDnaCugOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaCugOutCalls.setStatus("mandatory")


class _MscTraceRcvrFrDnaCugIncCalls_Type(Integer32):
    """Custom type mscTraceRcvrFrDnaCugIncCalls based on Integer32"""
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


_MscTraceRcvrFrDnaCugIncCalls_Type.__name__ = "Integer32"
_MscTraceRcvrFrDnaCugIncCalls_Object = MibTableColumn
mscTraceRcvrFrDnaCugIncCalls = _MscTraceRcvrFrDnaCugIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 2, 10, 1, 6),
    _MscTraceRcvrFrDnaCugIncCalls_Type()
)
mscTraceRcvrFrDnaCugIncCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaCugIncCalls.setStatus("mandatory")


class _MscTraceRcvrFrDnaCugPrivileged_Type(Integer32):
    """Custom type mscTraceRcvrFrDnaCugPrivileged based on Integer32"""
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


_MscTraceRcvrFrDnaCugPrivileged_Type.__name__ = "Integer32"
_MscTraceRcvrFrDnaCugPrivileged_Object = MibTableColumn
mscTraceRcvrFrDnaCugPrivileged = _MscTraceRcvrFrDnaCugPrivileged_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 2, 10, 1, 7),
    _MscTraceRcvrFrDnaCugPrivileged_Type()
)
mscTraceRcvrFrDnaCugPrivileged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaCugPrivileged.setStatus("mandatory")
_MscTraceRcvrFrDnaAddressTable_Object = MibTable
mscTraceRcvrFrDnaAddressTable = _MscTraceRcvrFrDnaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaAddressTable.setStatus("mandatory")
_MscTraceRcvrFrDnaAddressEntry_Object = MibTableRow
mscTraceRcvrFrDnaAddressEntry = _MscTraceRcvrFrDnaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 10, 1)
)
mscTraceRcvrFrDnaAddressEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceRcvrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceRcvrFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceRcvrFrDnaIndex"),
)
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaAddressEntry.setStatus("mandatory")


class _MscTraceRcvrFrDnaNumberingPlanIndicator_Type(Integer32):
    """Custom type mscTraceRcvrFrDnaNumberingPlanIndicator based on Integer32"""
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


_MscTraceRcvrFrDnaNumberingPlanIndicator_Type.__name__ = "Integer32"
_MscTraceRcvrFrDnaNumberingPlanIndicator_Object = MibTableColumn
mscTraceRcvrFrDnaNumberingPlanIndicator = _MscTraceRcvrFrDnaNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 10, 1, 1),
    _MscTraceRcvrFrDnaNumberingPlanIndicator_Type()
)
mscTraceRcvrFrDnaNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaNumberingPlanIndicator.setStatus("mandatory")


class _MscTraceRcvrFrDnaDataNetworkAddress_Type(DigitString):
    """Custom type mscTraceRcvrFrDnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscTraceRcvrFrDnaDataNetworkAddress_Type.__name__ = "DigitString"
_MscTraceRcvrFrDnaDataNetworkAddress_Object = MibTableColumn
mscTraceRcvrFrDnaDataNetworkAddress = _MscTraceRcvrFrDnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 10, 1, 2),
    _MscTraceRcvrFrDnaDataNetworkAddress_Type()
)
mscTraceRcvrFrDnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaDataNetworkAddress.setStatus("mandatory")
_MscTraceRcvrFrDnaOutgoingOptionsTable_Object = MibTable
mscTraceRcvrFrDnaOutgoingOptionsTable = _MscTraceRcvrFrDnaOutgoingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 11)
)
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaOutgoingOptionsTable.setStatus("mandatory")
_MscTraceRcvrFrDnaOutgoingOptionsEntry_Object = MibTableRow
mscTraceRcvrFrDnaOutgoingOptionsEntry = _MscTraceRcvrFrDnaOutgoingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 11, 1)
)
mscTraceRcvrFrDnaOutgoingOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceRcvrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceRcvrFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceRcvrFrDnaIndex"),
)
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaOutgoingOptionsEntry.setStatus("mandatory")


class _MscTraceRcvrFrDnaOutCalls_Type(Integer32):
    """Custom type mscTraceRcvrFrDnaOutCalls based on Integer32"""
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


_MscTraceRcvrFrDnaOutCalls_Type.__name__ = "Integer32"
_MscTraceRcvrFrDnaOutCalls_Object = MibTableColumn
mscTraceRcvrFrDnaOutCalls = _MscTraceRcvrFrDnaOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 11, 1, 1),
    _MscTraceRcvrFrDnaOutCalls_Type()
)
mscTraceRcvrFrDnaOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaOutCalls.setStatus("mandatory")


class _MscTraceRcvrFrDnaOutDefaultPriority_Type(Integer32):
    """Custom type mscTraceRcvrFrDnaOutDefaultPriority based on Integer32"""
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


_MscTraceRcvrFrDnaOutDefaultPriority_Type.__name__ = "Integer32"
_MscTraceRcvrFrDnaOutDefaultPriority_Object = MibTableColumn
mscTraceRcvrFrDnaOutDefaultPriority = _MscTraceRcvrFrDnaOutDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 11, 1, 7),
    _MscTraceRcvrFrDnaOutDefaultPriority_Type()
)
mscTraceRcvrFrDnaOutDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaOutDefaultPriority.setStatus("mandatory")


class _MscTraceRcvrFrDnaOutIntl_Type(Integer32):
    """Custom type mscTraceRcvrFrDnaOutIntl based on Integer32"""
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


_MscTraceRcvrFrDnaOutIntl_Type.__name__ = "Integer32"
_MscTraceRcvrFrDnaOutIntl_Object = MibTableColumn
mscTraceRcvrFrDnaOutIntl = _MscTraceRcvrFrDnaOutIntl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 11, 1, 8),
    _MscTraceRcvrFrDnaOutIntl_Type()
)
mscTraceRcvrFrDnaOutIntl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaOutIntl.setStatus("mandatory")


class _MscTraceRcvrFrDnaOutDefaultPathReliability_Type(Integer32):
    """Custom type mscTraceRcvrFrDnaOutDefaultPathReliability based on Integer32"""
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


_MscTraceRcvrFrDnaOutDefaultPathReliability_Type.__name__ = "Integer32"
_MscTraceRcvrFrDnaOutDefaultPathReliability_Object = MibTableColumn
mscTraceRcvrFrDnaOutDefaultPathReliability = _MscTraceRcvrFrDnaOutDefaultPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 11, 1, 14),
    _MscTraceRcvrFrDnaOutDefaultPathReliability_Type()
)
mscTraceRcvrFrDnaOutDefaultPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaOutDefaultPathReliability.setStatus("mandatory")


class _MscTraceRcvrFrDnaOutPathReliabilityOverRide_Type(Integer32):
    """Custom type mscTraceRcvrFrDnaOutPathReliabilityOverRide based on Integer32"""
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


_MscTraceRcvrFrDnaOutPathReliabilityOverRide_Type.__name__ = "Integer32"
_MscTraceRcvrFrDnaOutPathReliabilityOverRide_Object = MibTableColumn
mscTraceRcvrFrDnaOutPathReliabilityOverRide = _MscTraceRcvrFrDnaOutPathReliabilityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 11, 1, 15),
    _MscTraceRcvrFrDnaOutPathReliabilityOverRide_Type()
)
mscTraceRcvrFrDnaOutPathReliabilityOverRide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaOutPathReliabilityOverRide.setStatus("mandatory")


class _MscTraceRcvrFrDnaOutPathReliabilitySignal_Type(Integer32):
    """Custom type mscTraceRcvrFrDnaOutPathReliabilitySignal based on Integer32"""
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


_MscTraceRcvrFrDnaOutPathReliabilitySignal_Type.__name__ = "Integer32"
_MscTraceRcvrFrDnaOutPathReliabilitySignal_Object = MibTableColumn
mscTraceRcvrFrDnaOutPathReliabilitySignal = _MscTraceRcvrFrDnaOutPathReliabilitySignal_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 11, 1, 16),
    _MscTraceRcvrFrDnaOutPathReliabilitySignal_Type()
)
mscTraceRcvrFrDnaOutPathReliabilitySignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaOutPathReliabilitySignal.setStatus("mandatory")


class _MscTraceRcvrFrDnaOutAccess_Type(Integer32):
    """Custom type mscTraceRcvrFrDnaOutAccess based on Integer32"""
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


_MscTraceRcvrFrDnaOutAccess_Type.__name__ = "Integer32"
_MscTraceRcvrFrDnaOutAccess_Object = MibTableColumn
mscTraceRcvrFrDnaOutAccess = _MscTraceRcvrFrDnaOutAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 11, 1, 17),
    _MscTraceRcvrFrDnaOutAccess_Type()
)
mscTraceRcvrFrDnaOutAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaOutAccess.setStatus("mandatory")
_MscTraceRcvrFrDnaIncomingOptionsTable_Object = MibTable
mscTraceRcvrFrDnaIncomingOptionsTable = _MscTraceRcvrFrDnaIncomingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 12)
)
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaIncomingOptionsTable.setStatus("mandatory")
_MscTraceRcvrFrDnaIncomingOptionsEntry_Object = MibTableRow
mscTraceRcvrFrDnaIncomingOptionsEntry = _MscTraceRcvrFrDnaIncomingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 12, 1)
)
mscTraceRcvrFrDnaIncomingOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceRcvrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceRcvrFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceRcvrFrDnaIndex"),
)
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaIncomingOptionsEntry.setStatus("mandatory")


class _MscTraceRcvrFrDnaIncCalls_Type(Integer32):
    """Custom type mscTraceRcvrFrDnaIncCalls based on Integer32"""
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


_MscTraceRcvrFrDnaIncCalls_Type.__name__ = "Integer32"
_MscTraceRcvrFrDnaIncCalls_Object = MibTableColumn
mscTraceRcvrFrDnaIncCalls = _MscTraceRcvrFrDnaIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 12, 1, 1),
    _MscTraceRcvrFrDnaIncCalls_Type()
)
mscTraceRcvrFrDnaIncCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaIncCalls.setStatus("mandatory")
_MscTraceRcvrFrDnaCallOptionsTable_Object = MibTable
mscTraceRcvrFrDnaCallOptionsTable = _MscTraceRcvrFrDnaCallOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 13)
)
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaCallOptionsTable.setStatus("mandatory")
_MscTraceRcvrFrDnaCallOptionsEntry_Object = MibTableRow
mscTraceRcvrFrDnaCallOptionsEntry = _MscTraceRcvrFrDnaCallOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 13, 1)
)
mscTraceRcvrFrDnaCallOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceRcvrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceRcvrFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceRcvrFrDnaIndex"),
)
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaCallOptionsEntry.setStatus("mandatory")


class _MscTraceRcvrFrDnaPacketSizes_Type(OctetString):
    """Custom type mscTraceRcvrFrDnaPacketSizes based on OctetString"""
    defaultHexValue = "0100"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscTraceRcvrFrDnaPacketSizes_Type.__name__ = "OctetString"
_MscTraceRcvrFrDnaPacketSizes_Object = MibTableColumn
mscTraceRcvrFrDnaPacketSizes = _MscTraceRcvrFrDnaPacketSizes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 13, 1, 2),
    _MscTraceRcvrFrDnaPacketSizes_Type()
)
mscTraceRcvrFrDnaPacketSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaPacketSizes.setStatus("mandatory")


class _MscTraceRcvrFrDnaDefaultRecvFrmNetworkPacketSize_Type(Integer32):
    """Custom type mscTraceRcvrFrDnaDefaultRecvFrmNetworkPacketSize based on Integer32"""
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


_MscTraceRcvrFrDnaDefaultRecvFrmNetworkPacketSize_Type.__name__ = "Integer32"
_MscTraceRcvrFrDnaDefaultRecvFrmNetworkPacketSize_Object = MibTableColumn
mscTraceRcvrFrDnaDefaultRecvFrmNetworkPacketSize = _MscTraceRcvrFrDnaDefaultRecvFrmNetworkPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 13, 1, 3),
    _MscTraceRcvrFrDnaDefaultRecvFrmNetworkPacketSize_Type()
)
mscTraceRcvrFrDnaDefaultRecvFrmNetworkPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaDefaultRecvFrmNetworkPacketSize.setStatus("mandatory")


class _MscTraceRcvrFrDnaDefaultSendToNetworkPacketSize_Type(Integer32):
    """Custom type mscTraceRcvrFrDnaDefaultSendToNetworkPacketSize based on Integer32"""
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


_MscTraceRcvrFrDnaDefaultSendToNetworkPacketSize_Type.__name__ = "Integer32"
_MscTraceRcvrFrDnaDefaultSendToNetworkPacketSize_Object = MibTableColumn
mscTraceRcvrFrDnaDefaultSendToNetworkPacketSize = _MscTraceRcvrFrDnaDefaultSendToNetworkPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 13, 1, 4),
    _MscTraceRcvrFrDnaDefaultSendToNetworkPacketSize_Type()
)
mscTraceRcvrFrDnaDefaultSendToNetworkPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaDefaultSendToNetworkPacketSize.setStatus("mandatory")


class _MscTraceRcvrFrDnaCugFormat_Type(Integer32):
    """Custom type mscTraceRcvrFrDnaCugFormat based on Integer32"""
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


_MscTraceRcvrFrDnaCugFormat_Type.__name__ = "Integer32"
_MscTraceRcvrFrDnaCugFormat_Object = MibTableColumn
mscTraceRcvrFrDnaCugFormat = _MscTraceRcvrFrDnaCugFormat_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 2, 13, 1, 10),
    _MscTraceRcvrFrDnaCugFormat_Type()
)
mscTraceRcvrFrDnaCugFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDnaCugFormat.setStatus("mandatory")
_MscTraceRcvrFrDc_ObjectIdentity = ObjectIdentity
mscTraceRcvrFrDc = _MscTraceRcvrFrDc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 3)
)
_MscTraceRcvrFrDcRowStatusTable_Object = MibTable
mscTraceRcvrFrDcRowStatusTable = _MscTraceRcvrFrDcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    mscTraceRcvrFrDcRowStatusTable.setStatus("mandatory")
_MscTraceRcvrFrDcRowStatusEntry_Object = MibTableRow
mscTraceRcvrFrDcRowStatusEntry = _MscTraceRcvrFrDcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 3, 1, 1)
)
mscTraceRcvrFrDcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceRcvrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceRcvrFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceRcvrFrDcIndex"),
)
if mibBuilder.loadTexts:
    mscTraceRcvrFrDcRowStatusEntry.setStatus("mandatory")
_MscTraceRcvrFrDcRowStatus_Type = RowStatus
_MscTraceRcvrFrDcRowStatus_Object = MibTableColumn
mscTraceRcvrFrDcRowStatus = _MscTraceRcvrFrDcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 3, 1, 1, 1),
    _MscTraceRcvrFrDcRowStatus_Type()
)
mscTraceRcvrFrDcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDcRowStatus.setStatus("mandatory")
_MscTraceRcvrFrDcComponentName_Type = DisplayString
_MscTraceRcvrFrDcComponentName_Object = MibTableColumn
mscTraceRcvrFrDcComponentName = _MscTraceRcvrFrDcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 3, 1, 1, 2),
    _MscTraceRcvrFrDcComponentName_Type()
)
mscTraceRcvrFrDcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDcComponentName.setStatus("mandatory")
_MscTraceRcvrFrDcStorageType_Type = StorageType
_MscTraceRcvrFrDcStorageType_Object = MibTableColumn
mscTraceRcvrFrDcStorageType = _MscTraceRcvrFrDcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 3, 1, 1, 4),
    _MscTraceRcvrFrDcStorageType_Type()
)
mscTraceRcvrFrDcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDcStorageType.setStatus("mandatory")
_MscTraceRcvrFrDcIndex_Type = NonReplicated
_MscTraceRcvrFrDcIndex_Object = MibTableColumn
mscTraceRcvrFrDcIndex = _MscTraceRcvrFrDcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 3, 1, 1, 10),
    _MscTraceRcvrFrDcIndex_Type()
)
mscTraceRcvrFrDcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDcIndex.setStatus("mandatory")
_MscTraceRcvrFrDcOptionsTable_Object = MibTable
mscTraceRcvrFrDcOptionsTable = _MscTraceRcvrFrDcOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 3, 10)
)
if mibBuilder.loadTexts:
    mscTraceRcvrFrDcOptionsTable.setStatus("mandatory")
_MscTraceRcvrFrDcOptionsEntry_Object = MibTableRow
mscTraceRcvrFrDcOptionsEntry = _MscTraceRcvrFrDcOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 3, 10, 1)
)
mscTraceRcvrFrDcOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceRcvrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceRcvrFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceRcvrFrDcIndex"),
)
if mibBuilder.loadTexts:
    mscTraceRcvrFrDcOptionsEntry.setStatus("mandatory")


class _MscTraceRcvrFrDcRemoteNpi_Type(Integer32):
    """Custom type mscTraceRcvrFrDcRemoteNpi based on Integer32"""
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


_MscTraceRcvrFrDcRemoteNpi_Type.__name__ = "Integer32"
_MscTraceRcvrFrDcRemoteNpi_Object = MibTableColumn
mscTraceRcvrFrDcRemoteNpi = _MscTraceRcvrFrDcRemoteNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 3, 10, 1, 3),
    _MscTraceRcvrFrDcRemoteNpi_Type()
)
mscTraceRcvrFrDcRemoteNpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDcRemoteNpi.setStatus("mandatory")


class _MscTraceRcvrFrDcRemoteDna_Type(DigitString):
    """Custom type mscTraceRcvrFrDcRemoteDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscTraceRcvrFrDcRemoteDna_Type.__name__ = "DigitString"
_MscTraceRcvrFrDcRemoteDna_Object = MibTableColumn
mscTraceRcvrFrDcRemoteDna = _MscTraceRcvrFrDcRemoteDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 3, 10, 1, 4),
    _MscTraceRcvrFrDcRemoteDna_Type()
)
mscTraceRcvrFrDcRemoteDna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDcRemoteDna.setStatus("mandatory")


class _MscTraceRcvrFrDcType_Type(Integer32):
    """Custom type mscTraceRcvrFrDcType based on Integer32"""
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


_MscTraceRcvrFrDcType_Type.__name__ = "Integer32"
_MscTraceRcvrFrDcType_Object = MibTableColumn
mscTraceRcvrFrDcType = _MscTraceRcvrFrDcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 3, 10, 1, 6),
    _MscTraceRcvrFrDcType_Type()
)
mscTraceRcvrFrDcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDcType.setStatus("mandatory")


class _MscTraceRcvrFrDcUserData_Type(HexString):
    """Custom type mscTraceRcvrFrDcUserData based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscTraceRcvrFrDcUserData_Type.__name__ = "HexString"
_MscTraceRcvrFrDcUserData_Object = MibTableColumn
mscTraceRcvrFrDcUserData = _MscTraceRcvrFrDcUserData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 3, 3, 10, 1, 8),
    _MscTraceRcvrFrDcUserData_Type()
)
mscTraceRcvrFrDcUserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrFrDcUserData.setStatus("mandatory")
_MscTraceSessionFr_ObjectIdentity = ObjectIdentity
mscTraceSessionFr = _MscTraceSessionFr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3)
)
_MscTraceSessionFrRowStatusTable_Object = MibTable
mscTraceSessionFrRowStatusTable = _MscTraceSessionFrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 1)
)
if mibBuilder.loadTexts:
    mscTraceSessionFrRowStatusTable.setStatus("mandatory")
_MscTraceSessionFrRowStatusEntry_Object = MibTableRow
mscTraceSessionFrRowStatusEntry = _MscTraceSessionFrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 1, 1)
)
mscTraceSessionFrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceSessionIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceSessionFrIndex"),
)
if mibBuilder.loadTexts:
    mscTraceSessionFrRowStatusEntry.setStatus("mandatory")
_MscTraceSessionFrRowStatus_Type = RowStatus
_MscTraceSessionFrRowStatus_Object = MibTableColumn
mscTraceSessionFrRowStatus = _MscTraceSessionFrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 1, 1, 1),
    _MscTraceSessionFrRowStatus_Type()
)
mscTraceSessionFrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrRowStatus.setStatus("mandatory")
_MscTraceSessionFrComponentName_Type = DisplayString
_MscTraceSessionFrComponentName_Object = MibTableColumn
mscTraceSessionFrComponentName = _MscTraceSessionFrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 1, 1, 2),
    _MscTraceSessionFrComponentName_Type()
)
mscTraceSessionFrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrComponentName.setStatus("mandatory")
_MscTraceSessionFrStorageType_Type = StorageType
_MscTraceSessionFrStorageType_Object = MibTableColumn
mscTraceSessionFrStorageType = _MscTraceSessionFrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 1, 1, 4),
    _MscTraceSessionFrStorageType_Type()
)
mscTraceSessionFrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrStorageType.setStatus("mandatory")
_MscTraceSessionFrIndex_Type = NonReplicated
_MscTraceSessionFrIndex_Object = MibTableColumn
mscTraceSessionFrIndex = _MscTraceSessionFrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 1, 1, 10),
    _MscTraceSessionFrIndex_Type()
)
mscTraceSessionFrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTraceSessionFrIndex.setStatus("mandatory")
_MscTraceSessionFrVc_ObjectIdentity = ObjectIdentity
mscTraceSessionFrVc = _MscTraceSessionFrVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2)
)
_MscTraceSessionFrVcRowStatusTable_Object = MibTable
mscTraceSessionFrVcRowStatusTable = _MscTraceSessionFrVcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscTraceSessionFrVcRowStatusTable.setStatus("mandatory")
_MscTraceSessionFrVcRowStatusEntry_Object = MibTableRow
mscTraceSessionFrVcRowStatusEntry = _MscTraceSessionFrVcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 1, 1)
)
mscTraceSessionFrVcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceSessionIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceSessionFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceSessionFrVcIndex"),
)
if mibBuilder.loadTexts:
    mscTraceSessionFrVcRowStatusEntry.setStatus("mandatory")
_MscTraceSessionFrVcRowStatus_Type = RowStatus
_MscTraceSessionFrVcRowStatus_Object = MibTableColumn
mscTraceSessionFrVcRowStatus = _MscTraceSessionFrVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 1, 1, 1),
    _MscTraceSessionFrVcRowStatus_Type()
)
mscTraceSessionFrVcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcRowStatus.setStatus("mandatory")
_MscTraceSessionFrVcComponentName_Type = DisplayString
_MscTraceSessionFrVcComponentName_Object = MibTableColumn
mscTraceSessionFrVcComponentName = _MscTraceSessionFrVcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 1, 1, 2),
    _MscTraceSessionFrVcComponentName_Type()
)
mscTraceSessionFrVcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcComponentName.setStatus("mandatory")
_MscTraceSessionFrVcStorageType_Type = StorageType
_MscTraceSessionFrVcStorageType_Object = MibTableColumn
mscTraceSessionFrVcStorageType = _MscTraceSessionFrVcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 1, 1, 4),
    _MscTraceSessionFrVcStorageType_Type()
)
mscTraceSessionFrVcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcStorageType.setStatus("mandatory")
_MscTraceSessionFrVcIndex_Type = NonReplicated
_MscTraceSessionFrVcIndex_Object = MibTableColumn
mscTraceSessionFrVcIndex = _MscTraceSessionFrVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 1, 1, 10),
    _MscTraceSessionFrVcIndex_Type()
)
mscTraceSessionFrVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcIndex.setStatus("mandatory")
_MscTraceSessionFrVcCadTable_Object = MibTable
mscTraceSessionFrVcCadTable = _MscTraceSessionFrVcCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscTraceSessionFrVcCadTable.setStatus("mandatory")
_MscTraceSessionFrVcCadEntry_Object = MibTableRow
mscTraceSessionFrVcCadEntry = _MscTraceSessionFrVcCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10, 1)
)
mscTraceSessionFrVcCadEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceSessionIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceSessionFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceSessionFrVcIndex"),
)
if mibBuilder.loadTexts:
    mscTraceSessionFrVcCadEntry.setStatus("mandatory")


class _MscTraceSessionFrVcType_Type(Integer32):
    """Custom type mscTraceSessionFrVcType based on Integer32"""
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
        *(("frf10spvc", 3),
          ("pvc", 1),
          ("spvc", 2),
          ("svc", 0))
    )


_MscTraceSessionFrVcType_Type.__name__ = "Integer32"
_MscTraceSessionFrVcType_Object = MibTableColumn
mscTraceSessionFrVcType = _MscTraceSessionFrVcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10, 1, 1),
    _MscTraceSessionFrVcType_Type()
)
mscTraceSessionFrVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcType.setStatus("mandatory")


class _MscTraceSessionFrVcState_Type(Integer32):
    """Custom type mscTraceSessionFrVcState based on Integer32"""
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


_MscTraceSessionFrVcState_Type.__name__ = "Integer32"
_MscTraceSessionFrVcState_Object = MibTableColumn
mscTraceSessionFrVcState = _MscTraceSessionFrVcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10, 1, 2),
    _MscTraceSessionFrVcState_Type()
)
mscTraceSessionFrVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcState.setStatus("mandatory")


class _MscTraceSessionFrVcPreviousState_Type(Integer32):
    """Custom type mscTraceSessionFrVcPreviousState based on Integer32"""
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


_MscTraceSessionFrVcPreviousState_Type.__name__ = "Integer32"
_MscTraceSessionFrVcPreviousState_Object = MibTableColumn
mscTraceSessionFrVcPreviousState = _MscTraceSessionFrVcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10, 1, 3),
    _MscTraceSessionFrVcPreviousState_Type()
)
mscTraceSessionFrVcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcPreviousState.setStatus("mandatory")


class _MscTraceSessionFrVcDiagnosticCode_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscTraceSessionFrVcDiagnosticCode_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcDiagnosticCode_Object = MibTableColumn
mscTraceSessionFrVcDiagnosticCode = _MscTraceSessionFrVcDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10, 1, 4),
    _MscTraceSessionFrVcDiagnosticCode_Type()
)
mscTraceSessionFrVcDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcDiagnosticCode.setStatus("mandatory")


class _MscTraceSessionFrVcPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscTraceSessionFrVcPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcPreviousDiagnosticCode_Object = MibTableColumn
mscTraceSessionFrVcPreviousDiagnosticCode = _MscTraceSessionFrVcPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10, 1, 5),
    _MscTraceSessionFrVcPreviousDiagnosticCode_Type()
)
mscTraceSessionFrVcPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcPreviousDiagnosticCode.setStatus("mandatory")


class _MscTraceSessionFrVcCalledNpi_Type(Integer32):
    """Custom type mscTraceSessionFrVcCalledNpi based on Integer32"""
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


_MscTraceSessionFrVcCalledNpi_Type.__name__ = "Integer32"
_MscTraceSessionFrVcCalledNpi_Object = MibTableColumn
mscTraceSessionFrVcCalledNpi = _MscTraceSessionFrVcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10, 1, 6),
    _MscTraceSessionFrVcCalledNpi_Type()
)
mscTraceSessionFrVcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcCalledNpi.setStatus("mandatory")


class _MscTraceSessionFrVcCalledDna_Type(DigitString):
    """Custom type mscTraceSessionFrVcCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscTraceSessionFrVcCalledDna_Type.__name__ = "DigitString"
_MscTraceSessionFrVcCalledDna_Object = MibTableColumn
mscTraceSessionFrVcCalledDna = _MscTraceSessionFrVcCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10, 1, 7),
    _MscTraceSessionFrVcCalledDna_Type()
)
mscTraceSessionFrVcCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcCalledDna.setStatus("mandatory")


class _MscTraceSessionFrVcCalledLcn_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscTraceSessionFrVcCalledLcn_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcCalledLcn_Object = MibTableColumn
mscTraceSessionFrVcCalledLcn = _MscTraceSessionFrVcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10, 1, 8),
    _MscTraceSessionFrVcCalledLcn_Type()
)
mscTraceSessionFrVcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcCalledLcn.setStatus("mandatory")


class _MscTraceSessionFrVcCallingNpi_Type(Integer32):
    """Custom type mscTraceSessionFrVcCallingNpi based on Integer32"""
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


_MscTraceSessionFrVcCallingNpi_Type.__name__ = "Integer32"
_MscTraceSessionFrVcCallingNpi_Object = MibTableColumn
mscTraceSessionFrVcCallingNpi = _MscTraceSessionFrVcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10, 1, 9),
    _MscTraceSessionFrVcCallingNpi_Type()
)
mscTraceSessionFrVcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcCallingNpi.setStatus("mandatory")


class _MscTraceSessionFrVcCallingDna_Type(DigitString):
    """Custom type mscTraceSessionFrVcCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscTraceSessionFrVcCallingDna_Type.__name__ = "DigitString"
_MscTraceSessionFrVcCallingDna_Object = MibTableColumn
mscTraceSessionFrVcCallingDna = _MscTraceSessionFrVcCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10, 1, 10),
    _MscTraceSessionFrVcCallingDna_Type()
)
mscTraceSessionFrVcCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcCallingDna.setStatus("mandatory")


class _MscTraceSessionFrVcCallingLcn_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscTraceSessionFrVcCallingLcn_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcCallingLcn_Object = MibTableColumn
mscTraceSessionFrVcCallingLcn = _MscTraceSessionFrVcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10, 1, 11),
    _MscTraceSessionFrVcCallingLcn_Type()
)
mscTraceSessionFrVcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcCallingLcn.setStatus("mandatory")


class _MscTraceSessionFrVcAccountingEnabled_Type(Integer32):
    """Custom type mscTraceSessionFrVcAccountingEnabled based on Integer32"""
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


_MscTraceSessionFrVcAccountingEnabled_Type.__name__ = "Integer32"
_MscTraceSessionFrVcAccountingEnabled_Object = MibTableColumn
mscTraceSessionFrVcAccountingEnabled = _MscTraceSessionFrVcAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10, 1, 12),
    _MscTraceSessionFrVcAccountingEnabled_Type()
)
mscTraceSessionFrVcAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcAccountingEnabled.setStatus("mandatory")


class _MscTraceSessionFrVcFastSelectCall_Type(Integer32):
    """Custom type mscTraceSessionFrVcFastSelectCall based on Integer32"""
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


_MscTraceSessionFrVcFastSelectCall_Type.__name__ = "Integer32"
_MscTraceSessionFrVcFastSelectCall_Object = MibTableColumn
mscTraceSessionFrVcFastSelectCall = _MscTraceSessionFrVcFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10, 1, 13),
    _MscTraceSessionFrVcFastSelectCall_Type()
)
mscTraceSessionFrVcFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcFastSelectCall.setStatus("mandatory")


class _MscTraceSessionFrVcPathReliability_Type(Integer32):
    """Custom type mscTraceSessionFrVcPathReliability based on Integer32"""
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


_MscTraceSessionFrVcPathReliability_Type.__name__ = "Integer32"
_MscTraceSessionFrVcPathReliability_Object = MibTableColumn
mscTraceSessionFrVcPathReliability = _MscTraceSessionFrVcPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10, 1, 19),
    _MscTraceSessionFrVcPathReliability_Type()
)
mscTraceSessionFrVcPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcPathReliability.setStatus("mandatory")


class _MscTraceSessionFrVcAccountingEnd_Type(Integer32):
    """Custom type mscTraceSessionFrVcAccountingEnd based on Integer32"""
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


_MscTraceSessionFrVcAccountingEnd_Type.__name__ = "Integer32"
_MscTraceSessionFrVcAccountingEnd_Object = MibTableColumn
mscTraceSessionFrVcAccountingEnd = _MscTraceSessionFrVcAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10, 1, 20),
    _MscTraceSessionFrVcAccountingEnd_Type()
)
mscTraceSessionFrVcAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcAccountingEnd.setStatus("mandatory")


class _MscTraceSessionFrVcPriority_Type(Integer32):
    """Custom type mscTraceSessionFrVcPriority based on Integer32"""
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


_MscTraceSessionFrVcPriority_Type.__name__ = "Integer32"
_MscTraceSessionFrVcPriority_Object = MibTableColumn
mscTraceSessionFrVcPriority = _MscTraceSessionFrVcPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10, 1, 21),
    _MscTraceSessionFrVcPriority_Type()
)
mscTraceSessionFrVcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcPriority.setStatus("mandatory")


class _MscTraceSessionFrVcSegmentSize_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscTraceSessionFrVcSegmentSize_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcSegmentSize_Object = MibTableColumn
mscTraceSessionFrVcSegmentSize = _MscTraceSessionFrVcSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10, 1, 22),
    _MscTraceSessionFrVcSegmentSize_Type()
)
mscTraceSessionFrVcSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcSegmentSize.setStatus("mandatory")


class _MscTraceSessionFrVcMaxSubnetPktSize_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscTraceSessionFrVcMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcMaxSubnetPktSize_Object = MibTableColumn
mscTraceSessionFrVcMaxSubnetPktSize = _MscTraceSessionFrVcMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10, 1, 27),
    _MscTraceSessionFrVcMaxSubnetPktSize_Type()
)
mscTraceSessionFrVcMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcMaxSubnetPktSize.setStatus("mandatory")


class _MscTraceSessionFrVcRcosToNetwork_Type(Integer32):
    """Custom type mscTraceSessionFrVcRcosToNetwork based on Integer32"""
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


_MscTraceSessionFrVcRcosToNetwork_Type.__name__ = "Integer32"
_MscTraceSessionFrVcRcosToNetwork_Object = MibTableColumn
mscTraceSessionFrVcRcosToNetwork = _MscTraceSessionFrVcRcosToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10, 1, 28),
    _MscTraceSessionFrVcRcosToNetwork_Type()
)
mscTraceSessionFrVcRcosToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcRcosToNetwork.setStatus("mandatory")


class _MscTraceSessionFrVcRcosFromNetwork_Type(Integer32):
    """Custom type mscTraceSessionFrVcRcosFromNetwork based on Integer32"""
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


_MscTraceSessionFrVcRcosFromNetwork_Type.__name__ = "Integer32"
_MscTraceSessionFrVcRcosFromNetwork_Object = MibTableColumn
mscTraceSessionFrVcRcosFromNetwork = _MscTraceSessionFrVcRcosFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10, 1, 29),
    _MscTraceSessionFrVcRcosFromNetwork_Type()
)
mscTraceSessionFrVcRcosFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcRcosFromNetwork.setStatus("mandatory")


class _MscTraceSessionFrVcEmissionPriorityToNetwork_Type(Integer32):
    """Custom type mscTraceSessionFrVcEmissionPriorityToNetwork based on Integer32"""
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


_MscTraceSessionFrVcEmissionPriorityToNetwork_Type.__name__ = "Integer32"
_MscTraceSessionFrVcEmissionPriorityToNetwork_Object = MibTableColumn
mscTraceSessionFrVcEmissionPriorityToNetwork = _MscTraceSessionFrVcEmissionPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10, 1, 30),
    _MscTraceSessionFrVcEmissionPriorityToNetwork_Type()
)
mscTraceSessionFrVcEmissionPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcEmissionPriorityToNetwork.setStatus("mandatory")


class _MscTraceSessionFrVcEmissionPriorityFromNetwork_Type(Integer32):
    """Custom type mscTraceSessionFrVcEmissionPriorityFromNetwork based on Integer32"""
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


_MscTraceSessionFrVcEmissionPriorityFromNetwork_Type.__name__ = "Integer32"
_MscTraceSessionFrVcEmissionPriorityFromNetwork_Object = MibTableColumn
mscTraceSessionFrVcEmissionPriorityFromNetwork = _MscTraceSessionFrVcEmissionPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10, 1, 31),
    _MscTraceSessionFrVcEmissionPriorityFromNetwork_Type()
)
mscTraceSessionFrVcEmissionPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcEmissionPriorityFromNetwork.setStatus("mandatory")


class _MscTraceSessionFrVcDataPath_Type(AsciiString):
    """Custom type mscTraceSessionFrVcDataPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscTraceSessionFrVcDataPath_Type.__name__ = "AsciiString"
_MscTraceSessionFrVcDataPath_Object = MibTableColumn
mscTraceSessionFrVcDataPath = _MscTraceSessionFrVcDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 10, 1, 32),
    _MscTraceSessionFrVcDataPath_Type()
)
mscTraceSessionFrVcDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcDataPath.setStatus("mandatory")
_MscTraceSessionFrVcIntdTable_Object = MibTable
mscTraceSessionFrVcIntdTable = _MscTraceSessionFrVcIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 11)
)
if mibBuilder.loadTexts:
    mscTraceSessionFrVcIntdTable.setStatus("mandatory")
_MscTraceSessionFrVcIntdEntry_Object = MibTableRow
mscTraceSessionFrVcIntdEntry = _MscTraceSessionFrVcIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 11, 1)
)
mscTraceSessionFrVcIntdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceSessionIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceSessionFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceSessionFrVcIndex"),
)
if mibBuilder.loadTexts:
    mscTraceSessionFrVcIntdEntry.setStatus("mandatory")


class _MscTraceSessionFrVcCallReferenceNumber_Type(Hex):
    """Custom type mscTraceSessionFrVcCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscTraceSessionFrVcCallReferenceNumber_Type.__name__ = "Hex"
_MscTraceSessionFrVcCallReferenceNumber_Object = MibTableColumn
mscTraceSessionFrVcCallReferenceNumber = _MscTraceSessionFrVcCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 11, 1, 1),
    _MscTraceSessionFrVcCallReferenceNumber_Type()
)
mscTraceSessionFrVcCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcCallReferenceNumber.setStatus("obsolete")


class _MscTraceSessionFrVcElapsedTimeTillNow_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscTraceSessionFrVcElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcElapsedTimeTillNow_Object = MibTableColumn
mscTraceSessionFrVcElapsedTimeTillNow = _MscTraceSessionFrVcElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 11, 1, 2),
    _MscTraceSessionFrVcElapsedTimeTillNow_Type()
)
mscTraceSessionFrVcElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcElapsedTimeTillNow.setStatus("mandatory")


class _MscTraceSessionFrVcSegmentsRx_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscTraceSessionFrVcSegmentsRx_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcSegmentsRx_Object = MibTableColumn
mscTraceSessionFrVcSegmentsRx = _MscTraceSessionFrVcSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 11, 1, 3),
    _MscTraceSessionFrVcSegmentsRx_Type()
)
mscTraceSessionFrVcSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcSegmentsRx.setStatus("mandatory")


class _MscTraceSessionFrVcSegmentsSent_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscTraceSessionFrVcSegmentsSent_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcSegmentsSent_Object = MibTableColumn
mscTraceSessionFrVcSegmentsSent = _MscTraceSessionFrVcSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 11, 1, 4),
    _MscTraceSessionFrVcSegmentsSent_Type()
)
mscTraceSessionFrVcSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcSegmentsSent.setStatus("mandatory")


class _MscTraceSessionFrVcStartTime_Type(EnterpriseDateAndTime):
    """Custom type mscTraceSessionFrVcStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscTraceSessionFrVcStartTime_Type.__name__ = "EnterpriseDateAndTime"
_MscTraceSessionFrVcStartTime_Object = MibTableColumn
mscTraceSessionFrVcStartTime = _MscTraceSessionFrVcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 11, 1, 5),
    _MscTraceSessionFrVcStartTime_Type()
)
mscTraceSessionFrVcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcStartTime.setStatus("mandatory")


class _MscTraceSessionFrVcCallReferenceNumberDecimal_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcCallReferenceNumberDecimal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscTraceSessionFrVcCallReferenceNumberDecimal_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcCallReferenceNumberDecimal_Object = MibTableColumn
mscTraceSessionFrVcCallReferenceNumberDecimal = _MscTraceSessionFrVcCallReferenceNumberDecimal_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 11, 1, 7),
    _MscTraceSessionFrVcCallReferenceNumberDecimal_Type()
)
mscTraceSessionFrVcCallReferenceNumberDecimal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcCallReferenceNumberDecimal.setStatus("mandatory")
_MscTraceSessionFrVcFrdTable_Object = MibTable
mscTraceSessionFrVcFrdTable = _MscTraceSessionFrVcFrdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 12)
)
if mibBuilder.loadTexts:
    mscTraceSessionFrVcFrdTable.setStatus("mandatory")
_MscTraceSessionFrVcFrdEntry_Object = MibTableRow
mscTraceSessionFrVcFrdEntry = _MscTraceSessionFrVcFrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 12, 1)
)
mscTraceSessionFrVcFrdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceSessionIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceSessionFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceSessionFrVcIndex"),
)
if mibBuilder.loadTexts:
    mscTraceSessionFrVcFrdEntry.setStatus("mandatory")


class _MscTraceSessionFrVcFrmCongestedToSubnet_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcFrmCongestedToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionFrVcFrmCongestedToSubnet_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcFrmCongestedToSubnet_Object = MibTableColumn
mscTraceSessionFrVcFrmCongestedToSubnet = _MscTraceSessionFrVcFrmCongestedToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 12, 1, 2),
    _MscTraceSessionFrVcFrmCongestedToSubnet_Type()
)
mscTraceSessionFrVcFrmCongestedToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcFrmCongestedToSubnet.setStatus("mandatory")


class _MscTraceSessionFrVcCannotForwardToSubnet_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcCannotForwardToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionFrVcCannotForwardToSubnet_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcCannotForwardToSubnet_Object = MibTableColumn
mscTraceSessionFrVcCannotForwardToSubnet = _MscTraceSessionFrVcCannotForwardToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 12, 1, 3),
    _MscTraceSessionFrVcCannotForwardToSubnet_Type()
)
mscTraceSessionFrVcCannotForwardToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcCannotForwardToSubnet.setStatus("mandatory")


class _MscTraceSessionFrVcNotDataXferToSubnet_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcNotDataXferToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionFrVcNotDataXferToSubnet_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcNotDataXferToSubnet_Object = MibTableColumn
mscTraceSessionFrVcNotDataXferToSubnet = _MscTraceSessionFrVcNotDataXferToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 12, 1, 4),
    _MscTraceSessionFrVcNotDataXferToSubnet_Type()
)
mscTraceSessionFrVcNotDataXferToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcNotDataXferToSubnet.setStatus("mandatory")


class _MscTraceSessionFrVcOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionFrVcOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcOutOfRangeFrmFromSubnet_Object = MibTableColumn
mscTraceSessionFrVcOutOfRangeFrmFromSubnet = _MscTraceSessionFrVcOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 12, 1, 5),
    _MscTraceSessionFrVcOutOfRangeFrmFromSubnet_Type()
)
mscTraceSessionFrVcOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _MscTraceSessionFrVcCombErrorsFromSubnet_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcCombErrorsFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionFrVcCombErrorsFromSubnet_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcCombErrorsFromSubnet_Object = MibTableColumn
mscTraceSessionFrVcCombErrorsFromSubnet = _MscTraceSessionFrVcCombErrorsFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 12, 1, 6),
    _MscTraceSessionFrVcCombErrorsFromSubnet_Type()
)
mscTraceSessionFrVcCombErrorsFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcCombErrorsFromSubnet.setStatus("mandatory")


class _MscTraceSessionFrVcDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionFrVcDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcDuplicatesFromSubnet_Object = MibTableColumn
mscTraceSessionFrVcDuplicatesFromSubnet = _MscTraceSessionFrVcDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 12, 1, 7),
    _MscTraceSessionFrVcDuplicatesFromSubnet_Type()
)
mscTraceSessionFrVcDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcDuplicatesFromSubnet.setStatus("mandatory")


class _MscTraceSessionFrVcNotDataXferFromSubnet_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcNotDataXferFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionFrVcNotDataXferFromSubnet_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcNotDataXferFromSubnet_Object = MibTableColumn
mscTraceSessionFrVcNotDataXferFromSubnet = _MscTraceSessionFrVcNotDataXferFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 12, 1, 8),
    _MscTraceSessionFrVcNotDataXferFromSubnet_Type()
)
mscTraceSessionFrVcNotDataXferFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcNotDataXferFromSubnet.setStatus("mandatory")


class _MscTraceSessionFrVcFrmLossTimeouts_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcFrmLossTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionFrVcFrmLossTimeouts_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcFrmLossTimeouts_Object = MibTableColumn
mscTraceSessionFrVcFrmLossTimeouts = _MscTraceSessionFrVcFrmLossTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 12, 1, 9),
    _MscTraceSessionFrVcFrmLossTimeouts_Type()
)
mscTraceSessionFrVcFrmLossTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcFrmLossTimeouts.setStatus("mandatory")


class _MscTraceSessionFrVcOoSeqByteCntExceeded_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcOoSeqByteCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionFrVcOoSeqByteCntExceeded_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcOoSeqByteCntExceeded_Object = MibTableColumn
mscTraceSessionFrVcOoSeqByteCntExceeded = _MscTraceSessionFrVcOoSeqByteCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 12, 1, 10),
    _MscTraceSessionFrVcOoSeqByteCntExceeded_Type()
)
mscTraceSessionFrVcOoSeqByteCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcOoSeqByteCntExceeded.setStatus("mandatory")


class _MscTraceSessionFrVcPeakOoSeqPktCount_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcPeakOoSeqPktCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionFrVcPeakOoSeqPktCount_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcPeakOoSeqPktCount_Object = MibTableColumn
mscTraceSessionFrVcPeakOoSeqPktCount = _MscTraceSessionFrVcPeakOoSeqPktCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 12, 1, 11),
    _MscTraceSessionFrVcPeakOoSeqPktCount_Type()
)
mscTraceSessionFrVcPeakOoSeqPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcPeakOoSeqPktCount.setStatus("mandatory")


class _MscTraceSessionFrVcPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionFrVcPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcPeakOoSeqFrmForwarded_Object = MibTableColumn
mscTraceSessionFrVcPeakOoSeqFrmForwarded = _MscTraceSessionFrVcPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 12, 1, 12),
    _MscTraceSessionFrVcPeakOoSeqFrmForwarded_Type()
)
mscTraceSessionFrVcPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcPeakOoSeqFrmForwarded.setStatus("mandatory")


class _MscTraceSessionFrVcSendSequenceNumber_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcSendSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionFrVcSendSequenceNumber_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcSendSequenceNumber_Object = MibTableColumn
mscTraceSessionFrVcSendSequenceNumber = _MscTraceSessionFrVcSendSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 12, 1, 13),
    _MscTraceSessionFrVcSendSequenceNumber_Type()
)
mscTraceSessionFrVcSendSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcSendSequenceNumber.setStatus("mandatory")


class _MscTraceSessionFrVcPktRetryTimeouts_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcPktRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionFrVcPktRetryTimeouts_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcPktRetryTimeouts_Object = MibTableColumn
mscTraceSessionFrVcPktRetryTimeouts = _MscTraceSessionFrVcPktRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 12, 1, 15),
    _MscTraceSessionFrVcPktRetryTimeouts_Type()
)
mscTraceSessionFrVcPktRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcPktRetryTimeouts.setStatus("mandatory")


class _MscTraceSessionFrVcPeakRetryQueueSize_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionFrVcPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcPeakRetryQueueSize_Object = MibTableColumn
mscTraceSessionFrVcPeakRetryQueueSize = _MscTraceSessionFrVcPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 12, 1, 16),
    _MscTraceSessionFrVcPeakRetryQueueSize_Type()
)
mscTraceSessionFrVcPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcPeakRetryQueueSize.setStatus("mandatory")


class _MscTraceSessionFrVcSubnetRecoveries_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscTraceSessionFrVcSubnetRecoveries_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcSubnetRecoveries_Object = MibTableColumn
mscTraceSessionFrVcSubnetRecoveries = _MscTraceSessionFrVcSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 12, 1, 17),
    _MscTraceSessionFrVcSubnetRecoveries_Type()
)
mscTraceSessionFrVcSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcSubnetRecoveries.setStatus("mandatory")


class _MscTraceSessionFrVcOoSeqPktCntExceeded_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcOoSeqPktCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscTraceSessionFrVcOoSeqPktCntExceeded_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcOoSeqPktCntExceeded_Object = MibTableColumn
mscTraceSessionFrVcOoSeqPktCntExceeded = _MscTraceSessionFrVcOoSeqPktCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 12, 1, 19),
    _MscTraceSessionFrVcOoSeqPktCntExceeded_Type()
)
mscTraceSessionFrVcOoSeqPktCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcOoSeqPktCntExceeded.setStatus("mandatory")


class _MscTraceSessionFrVcPeakOoSeqByteCount_Type(Unsigned32):
    """Custom type mscTraceSessionFrVcPeakOoSeqByteCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_MscTraceSessionFrVcPeakOoSeqByteCount_Type.__name__ = "Unsigned32"
_MscTraceSessionFrVcPeakOoSeqByteCount_Object = MibTableColumn
mscTraceSessionFrVcPeakOoSeqByteCount = _MscTraceSessionFrVcPeakOoSeqByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 12, 1, 20),
    _MscTraceSessionFrVcPeakOoSeqByteCount_Type()
)
mscTraceSessionFrVcPeakOoSeqByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcPeakOoSeqByteCount.setStatus("mandatory")
_MscTraceSessionFrVcDmepTable_Object = MibTable
mscTraceSessionFrVcDmepTable = _MscTraceSessionFrVcDmepTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 417)
)
if mibBuilder.loadTexts:
    mscTraceSessionFrVcDmepTable.setStatus("mandatory")
_MscTraceSessionFrVcDmepEntry_Object = MibTableRow
mscTraceSessionFrVcDmepEntry = _MscTraceSessionFrVcDmepEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 417, 1)
)
mscTraceSessionFrVcDmepEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceSessionIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceSessionFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceSessionFrVcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB", "mscTraceSessionFrVcDmepValue"),
)
if mibBuilder.loadTexts:
    mscTraceSessionFrVcDmepEntry.setStatus("mandatory")
_MscTraceSessionFrVcDmepValue_Type = RowPointer
_MscTraceSessionFrVcDmepValue_Object = MibTableColumn
mscTraceSessionFrVcDmepValue = _MscTraceSessionFrVcDmepValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 3, 2, 417, 1, 1),
    _MscTraceSessionFrVcDmepValue_Type()
)
mscTraceSessionFrVcDmepValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFrVcDmepValue.setStatus("mandatory")
_FrTraceRcvrMIB_ObjectIdentity = ObjectIdentity
frTraceRcvrMIB = _FrTraceRcvrMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 139)
)
_FrTraceRcvrGroup_ObjectIdentity = ObjectIdentity
frTraceRcvrGroup = _FrTraceRcvrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 139, 1)
)
_FrTraceRcvrGroupCA_ObjectIdentity = ObjectIdentity
frTraceRcvrGroupCA = _FrTraceRcvrGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 139, 1, 1)
)
_FrTraceRcvrGroupCA02_ObjectIdentity = ObjectIdentity
frTraceRcvrGroupCA02 = _FrTraceRcvrGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 139, 1, 1, 3)
)
_FrTraceRcvrGroupCA02A_ObjectIdentity = ObjectIdentity
frTraceRcvrGroupCA02A = _FrTraceRcvrGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 139, 1, 1, 3, 2)
)
_FrTraceRcvrCapabilities_ObjectIdentity = ObjectIdentity
frTraceRcvrCapabilities = _FrTraceRcvrCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 139, 3)
)
_FrTraceRcvrCapabilitiesCA_ObjectIdentity = ObjectIdentity
frTraceRcvrCapabilitiesCA = _FrTraceRcvrCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 139, 3, 1)
)
_FrTraceRcvrCapabilitiesCA02_ObjectIdentity = ObjectIdentity
frTraceRcvrCapabilitiesCA02 = _FrTraceRcvrCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 139, 3, 1, 3)
)
_FrTraceRcvrCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
frTraceRcvrCapabilitiesCA02A = _FrTraceRcvrCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 139, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-FrTraceRcvrMIB",
    **{"mscTraceRcvrFr": mscTraceRcvrFr,
       "mscTraceRcvrFrRowStatusTable": mscTraceRcvrFrRowStatusTable,
       "mscTraceRcvrFrRowStatusEntry": mscTraceRcvrFrRowStatusEntry,
       "mscTraceRcvrFrRowStatus": mscTraceRcvrFrRowStatus,
       "mscTraceRcvrFrComponentName": mscTraceRcvrFrComponentName,
       "mscTraceRcvrFrStorageType": mscTraceRcvrFrStorageType,
       "mscTraceRcvrFrIndex": mscTraceRcvrFrIndex,
       "mscTraceRcvrFrDna": mscTraceRcvrFrDna,
       "mscTraceRcvrFrDnaRowStatusTable": mscTraceRcvrFrDnaRowStatusTable,
       "mscTraceRcvrFrDnaRowStatusEntry": mscTraceRcvrFrDnaRowStatusEntry,
       "mscTraceRcvrFrDnaRowStatus": mscTraceRcvrFrDnaRowStatus,
       "mscTraceRcvrFrDnaComponentName": mscTraceRcvrFrDnaComponentName,
       "mscTraceRcvrFrDnaStorageType": mscTraceRcvrFrDnaStorageType,
       "mscTraceRcvrFrDnaIndex": mscTraceRcvrFrDnaIndex,
       "mscTraceRcvrFrDnaCug": mscTraceRcvrFrDnaCug,
       "mscTraceRcvrFrDnaCugRowStatusTable": mscTraceRcvrFrDnaCugRowStatusTable,
       "mscTraceRcvrFrDnaCugRowStatusEntry": mscTraceRcvrFrDnaCugRowStatusEntry,
       "mscTraceRcvrFrDnaCugRowStatus": mscTraceRcvrFrDnaCugRowStatus,
       "mscTraceRcvrFrDnaCugComponentName": mscTraceRcvrFrDnaCugComponentName,
       "mscTraceRcvrFrDnaCugStorageType": mscTraceRcvrFrDnaCugStorageType,
       "mscTraceRcvrFrDnaCugIndex": mscTraceRcvrFrDnaCugIndex,
       "mscTraceRcvrFrDnaCugCugOptionsTable": mscTraceRcvrFrDnaCugCugOptionsTable,
       "mscTraceRcvrFrDnaCugCugOptionsEntry": mscTraceRcvrFrDnaCugCugOptionsEntry,
       "mscTraceRcvrFrDnaCugType": mscTraceRcvrFrDnaCugType,
       "mscTraceRcvrFrDnaCugDnic": mscTraceRcvrFrDnaCugDnic,
       "mscTraceRcvrFrDnaCugInterlockCode": mscTraceRcvrFrDnaCugInterlockCode,
       "mscTraceRcvrFrDnaCugPreferential": mscTraceRcvrFrDnaCugPreferential,
       "mscTraceRcvrFrDnaCugOutCalls": mscTraceRcvrFrDnaCugOutCalls,
       "mscTraceRcvrFrDnaCugIncCalls": mscTraceRcvrFrDnaCugIncCalls,
       "mscTraceRcvrFrDnaCugPrivileged": mscTraceRcvrFrDnaCugPrivileged,
       "mscTraceRcvrFrDnaAddressTable": mscTraceRcvrFrDnaAddressTable,
       "mscTraceRcvrFrDnaAddressEntry": mscTraceRcvrFrDnaAddressEntry,
       "mscTraceRcvrFrDnaNumberingPlanIndicator": mscTraceRcvrFrDnaNumberingPlanIndicator,
       "mscTraceRcvrFrDnaDataNetworkAddress": mscTraceRcvrFrDnaDataNetworkAddress,
       "mscTraceRcvrFrDnaOutgoingOptionsTable": mscTraceRcvrFrDnaOutgoingOptionsTable,
       "mscTraceRcvrFrDnaOutgoingOptionsEntry": mscTraceRcvrFrDnaOutgoingOptionsEntry,
       "mscTraceRcvrFrDnaOutCalls": mscTraceRcvrFrDnaOutCalls,
       "mscTraceRcvrFrDnaOutDefaultPriority": mscTraceRcvrFrDnaOutDefaultPriority,
       "mscTraceRcvrFrDnaOutIntl": mscTraceRcvrFrDnaOutIntl,
       "mscTraceRcvrFrDnaOutDefaultPathReliability": mscTraceRcvrFrDnaOutDefaultPathReliability,
       "mscTraceRcvrFrDnaOutPathReliabilityOverRide": mscTraceRcvrFrDnaOutPathReliabilityOverRide,
       "mscTraceRcvrFrDnaOutPathReliabilitySignal": mscTraceRcvrFrDnaOutPathReliabilitySignal,
       "mscTraceRcvrFrDnaOutAccess": mscTraceRcvrFrDnaOutAccess,
       "mscTraceRcvrFrDnaIncomingOptionsTable": mscTraceRcvrFrDnaIncomingOptionsTable,
       "mscTraceRcvrFrDnaIncomingOptionsEntry": mscTraceRcvrFrDnaIncomingOptionsEntry,
       "mscTraceRcvrFrDnaIncCalls": mscTraceRcvrFrDnaIncCalls,
       "mscTraceRcvrFrDnaCallOptionsTable": mscTraceRcvrFrDnaCallOptionsTable,
       "mscTraceRcvrFrDnaCallOptionsEntry": mscTraceRcvrFrDnaCallOptionsEntry,
       "mscTraceRcvrFrDnaPacketSizes": mscTraceRcvrFrDnaPacketSizes,
       "mscTraceRcvrFrDnaDefaultRecvFrmNetworkPacketSize": mscTraceRcvrFrDnaDefaultRecvFrmNetworkPacketSize,
       "mscTraceRcvrFrDnaDefaultSendToNetworkPacketSize": mscTraceRcvrFrDnaDefaultSendToNetworkPacketSize,
       "mscTraceRcvrFrDnaCugFormat": mscTraceRcvrFrDnaCugFormat,
       "mscTraceRcvrFrDc": mscTraceRcvrFrDc,
       "mscTraceRcvrFrDcRowStatusTable": mscTraceRcvrFrDcRowStatusTable,
       "mscTraceRcvrFrDcRowStatusEntry": mscTraceRcvrFrDcRowStatusEntry,
       "mscTraceRcvrFrDcRowStatus": mscTraceRcvrFrDcRowStatus,
       "mscTraceRcvrFrDcComponentName": mscTraceRcvrFrDcComponentName,
       "mscTraceRcvrFrDcStorageType": mscTraceRcvrFrDcStorageType,
       "mscTraceRcvrFrDcIndex": mscTraceRcvrFrDcIndex,
       "mscTraceRcvrFrDcOptionsTable": mscTraceRcvrFrDcOptionsTable,
       "mscTraceRcvrFrDcOptionsEntry": mscTraceRcvrFrDcOptionsEntry,
       "mscTraceRcvrFrDcRemoteNpi": mscTraceRcvrFrDcRemoteNpi,
       "mscTraceRcvrFrDcRemoteDna": mscTraceRcvrFrDcRemoteDna,
       "mscTraceRcvrFrDcType": mscTraceRcvrFrDcType,
       "mscTraceRcvrFrDcUserData": mscTraceRcvrFrDcUserData,
       "mscTraceSessionFr": mscTraceSessionFr,
       "mscTraceSessionFrRowStatusTable": mscTraceSessionFrRowStatusTable,
       "mscTraceSessionFrRowStatusEntry": mscTraceSessionFrRowStatusEntry,
       "mscTraceSessionFrRowStatus": mscTraceSessionFrRowStatus,
       "mscTraceSessionFrComponentName": mscTraceSessionFrComponentName,
       "mscTraceSessionFrStorageType": mscTraceSessionFrStorageType,
       "mscTraceSessionFrIndex": mscTraceSessionFrIndex,
       "mscTraceSessionFrVc": mscTraceSessionFrVc,
       "mscTraceSessionFrVcRowStatusTable": mscTraceSessionFrVcRowStatusTable,
       "mscTraceSessionFrVcRowStatusEntry": mscTraceSessionFrVcRowStatusEntry,
       "mscTraceSessionFrVcRowStatus": mscTraceSessionFrVcRowStatus,
       "mscTraceSessionFrVcComponentName": mscTraceSessionFrVcComponentName,
       "mscTraceSessionFrVcStorageType": mscTraceSessionFrVcStorageType,
       "mscTraceSessionFrVcIndex": mscTraceSessionFrVcIndex,
       "mscTraceSessionFrVcCadTable": mscTraceSessionFrVcCadTable,
       "mscTraceSessionFrVcCadEntry": mscTraceSessionFrVcCadEntry,
       "mscTraceSessionFrVcType": mscTraceSessionFrVcType,
       "mscTraceSessionFrVcState": mscTraceSessionFrVcState,
       "mscTraceSessionFrVcPreviousState": mscTraceSessionFrVcPreviousState,
       "mscTraceSessionFrVcDiagnosticCode": mscTraceSessionFrVcDiagnosticCode,
       "mscTraceSessionFrVcPreviousDiagnosticCode": mscTraceSessionFrVcPreviousDiagnosticCode,
       "mscTraceSessionFrVcCalledNpi": mscTraceSessionFrVcCalledNpi,
       "mscTraceSessionFrVcCalledDna": mscTraceSessionFrVcCalledDna,
       "mscTraceSessionFrVcCalledLcn": mscTraceSessionFrVcCalledLcn,
       "mscTraceSessionFrVcCallingNpi": mscTraceSessionFrVcCallingNpi,
       "mscTraceSessionFrVcCallingDna": mscTraceSessionFrVcCallingDna,
       "mscTraceSessionFrVcCallingLcn": mscTraceSessionFrVcCallingLcn,
       "mscTraceSessionFrVcAccountingEnabled": mscTraceSessionFrVcAccountingEnabled,
       "mscTraceSessionFrVcFastSelectCall": mscTraceSessionFrVcFastSelectCall,
       "mscTraceSessionFrVcPathReliability": mscTraceSessionFrVcPathReliability,
       "mscTraceSessionFrVcAccountingEnd": mscTraceSessionFrVcAccountingEnd,
       "mscTraceSessionFrVcPriority": mscTraceSessionFrVcPriority,
       "mscTraceSessionFrVcSegmentSize": mscTraceSessionFrVcSegmentSize,
       "mscTraceSessionFrVcMaxSubnetPktSize": mscTraceSessionFrVcMaxSubnetPktSize,
       "mscTraceSessionFrVcRcosToNetwork": mscTraceSessionFrVcRcosToNetwork,
       "mscTraceSessionFrVcRcosFromNetwork": mscTraceSessionFrVcRcosFromNetwork,
       "mscTraceSessionFrVcEmissionPriorityToNetwork": mscTraceSessionFrVcEmissionPriorityToNetwork,
       "mscTraceSessionFrVcEmissionPriorityFromNetwork": mscTraceSessionFrVcEmissionPriorityFromNetwork,
       "mscTraceSessionFrVcDataPath": mscTraceSessionFrVcDataPath,
       "mscTraceSessionFrVcIntdTable": mscTraceSessionFrVcIntdTable,
       "mscTraceSessionFrVcIntdEntry": mscTraceSessionFrVcIntdEntry,
       "mscTraceSessionFrVcCallReferenceNumber": mscTraceSessionFrVcCallReferenceNumber,
       "mscTraceSessionFrVcElapsedTimeTillNow": mscTraceSessionFrVcElapsedTimeTillNow,
       "mscTraceSessionFrVcSegmentsRx": mscTraceSessionFrVcSegmentsRx,
       "mscTraceSessionFrVcSegmentsSent": mscTraceSessionFrVcSegmentsSent,
       "mscTraceSessionFrVcStartTime": mscTraceSessionFrVcStartTime,
       "mscTraceSessionFrVcCallReferenceNumberDecimal": mscTraceSessionFrVcCallReferenceNumberDecimal,
       "mscTraceSessionFrVcFrdTable": mscTraceSessionFrVcFrdTable,
       "mscTraceSessionFrVcFrdEntry": mscTraceSessionFrVcFrdEntry,
       "mscTraceSessionFrVcFrmCongestedToSubnet": mscTraceSessionFrVcFrmCongestedToSubnet,
       "mscTraceSessionFrVcCannotForwardToSubnet": mscTraceSessionFrVcCannotForwardToSubnet,
       "mscTraceSessionFrVcNotDataXferToSubnet": mscTraceSessionFrVcNotDataXferToSubnet,
       "mscTraceSessionFrVcOutOfRangeFrmFromSubnet": mscTraceSessionFrVcOutOfRangeFrmFromSubnet,
       "mscTraceSessionFrVcCombErrorsFromSubnet": mscTraceSessionFrVcCombErrorsFromSubnet,
       "mscTraceSessionFrVcDuplicatesFromSubnet": mscTraceSessionFrVcDuplicatesFromSubnet,
       "mscTraceSessionFrVcNotDataXferFromSubnet": mscTraceSessionFrVcNotDataXferFromSubnet,
       "mscTraceSessionFrVcFrmLossTimeouts": mscTraceSessionFrVcFrmLossTimeouts,
       "mscTraceSessionFrVcOoSeqByteCntExceeded": mscTraceSessionFrVcOoSeqByteCntExceeded,
       "mscTraceSessionFrVcPeakOoSeqPktCount": mscTraceSessionFrVcPeakOoSeqPktCount,
       "mscTraceSessionFrVcPeakOoSeqFrmForwarded": mscTraceSessionFrVcPeakOoSeqFrmForwarded,
       "mscTraceSessionFrVcSendSequenceNumber": mscTraceSessionFrVcSendSequenceNumber,
       "mscTraceSessionFrVcPktRetryTimeouts": mscTraceSessionFrVcPktRetryTimeouts,
       "mscTraceSessionFrVcPeakRetryQueueSize": mscTraceSessionFrVcPeakRetryQueueSize,
       "mscTraceSessionFrVcSubnetRecoveries": mscTraceSessionFrVcSubnetRecoveries,
       "mscTraceSessionFrVcOoSeqPktCntExceeded": mscTraceSessionFrVcOoSeqPktCntExceeded,
       "mscTraceSessionFrVcPeakOoSeqByteCount": mscTraceSessionFrVcPeakOoSeqByteCount,
       "mscTraceSessionFrVcDmepTable": mscTraceSessionFrVcDmepTable,
       "mscTraceSessionFrVcDmepEntry": mscTraceSessionFrVcDmepEntry,
       "mscTraceSessionFrVcDmepValue": mscTraceSessionFrVcDmepValue,
       "frTraceRcvrMIB": frTraceRcvrMIB,
       "frTraceRcvrGroup": frTraceRcvrGroup,
       "frTraceRcvrGroupCA": frTraceRcvrGroupCA,
       "frTraceRcvrGroupCA02": frTraceRcvrGroupCA02,
       "frTraceRcvrGroupCA02A": frTraceRcvrGroupCA02A,
       "frTraceRcvrCapabilities": frTraceRcvrCapabilities,
       "frTraceRcvrCapabilitiesCA": frTraceRcvrCapabilitiesCA,
       "frTraceRcvrCapabilitiesCA02": frTraceRcvrCapabilitiesCA02,
       "frTraceRcvrCapabilitiesCA02A": frTraceRcvrCapabilitiesCA02A}
)
