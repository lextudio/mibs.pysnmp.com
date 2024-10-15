# SNMP MIB module (Nortel-Magellan-Passport-TdmaIwfMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-TdmaIwfMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:26 2024
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
 Gauge32,
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 FixedPoint2,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "FixedPoint2",
    "Link",
    "NonReplicated")

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

_TdmaCs_ObjectIdentity = ObjectIdentity
tdmaCs = _TdmaCs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135)
)
_TdmaCsRowStatusTable_Object = MibTable
tdmaCsRowStatusTable = _TdmaCsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 1)
)
if mibBuilder.loadTexts:
    tdmaCsRowStatusTable.setStatus("mandatory")
_TdmaCsRowStatusEntry_Object = MibTableRow
tdmaCsRowStatusEntry = _TdmaCsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 1, 1)
)
tdmaCsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsCsIndex"),
)
if mibBuilder.loadTexts:
    tdmaCsRowStatusEntry.setStatus("mandatory")
_TdmaCsRowStatus_Type = RowStatus
_TdmaCsRowStatus_Object = MibTableColumn
tdmaCsRowStatus = _TdmaCsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 1, 1, 1),
    _TdmaCsRowStatus_Type()
)
tdmaCsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsRowStatus.setStatus("mandatory")
_TdmaCsComponentName_Type = DisplayString
_TdmaCsComponentName_Object = MibTableColumn
tdmaCsComponentName = _TdmaCsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 1, 1, 2),
    _TdmaCsComponentName_Type()
)
tdmaCsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsComponentName.setStatus("mandatory")
_TdmaCsStorageType_Type = StorageType
_TdmaCsStorageType_Object = MibTableColumn
tdmaCsStorageType = _TdmaCsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 1, 1, 4),
    _TdmaCsStorageType_Type()
)
tdmaCsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsStorageType.setStatus("mandatory")


class _TdmaCsCsIndex_Type(Integer32):
    """Custom type tdmaCsCsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TdmaCsCsIndex_Type.__name__ = "Integer32"
_TdmaCsCsIndex_Object = MibTableColumn
tdmaCsCsIndex = _TdmaCsCsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 1, 1, 10),
    _TdmaCsCsIndex_Type()
)
tdmaCsCsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmaCsCsIndex.setStatus("mandatory")
_TdmaCsModem_ObjectIdentity = ObjectIdentity
tdmaCsModem = _TdmaCsModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 2)
)
_TdmaCsModemRowStatusTable_Object = MibTable
tdmaCsModemRowStatusTable = _TdmaCsModemRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 2, 1)
)
if mibBuilder.loadTexts:
    tdmaCsModemRowStatusTable.setStatus("mandatory")
_TdmaCsModemRowStatusEntry_Object = MibTableRow
tdmaCsModemRowStatusEntry = _TdmaCsModemRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 2, 1, 1)
)
tdmaCsModemRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsModemIndex"),
)
if mibBuilder.loadTexts:
    tdmaCsModemRowStatusEntry.setStatus("mandatory")
_TdmaCsModemRowStatus_Type = RowStatus
_TdmaCsModemRowStatus_Object = MibTableColumn
tdmaCsModemRowStatus = _TdmaCsModemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 2, 1, 1, 1),
    _TdmaCsModemRowStatus_Type()
)
tdmaCsModemRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsModemRowStatus.setStatus("mandatory")
_TdmaCsModemComponentName_Type = DisplayString
_TdmaCsModemComponentName_Object = MibTableColumn
tdmaCsModemComponentName = _TdmaCsModemComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 2, 1, 1, 2),
    _TdmaCsModemComponentName_Type()
)
tdmaCsModemComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsModemComponentName.setStatus("mandatory")
_TdmaCsModemStorageType_Type = StorageType
_TdmaCsModemStorageType_Object = MibTableColumn
tdmaCsModemStorageType = _TdmaCsModemStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 2, 1, 1, 4),
    _TdmaCsModemStorageType_Type()
)
tdmaCsModemStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsModemStorageType.setStatus("mandatory")
_TdmaCsModemIndex_Type = NonReplicated
_TdmaCsModemIndex_Object = MibTableColumn
tdmaCsModemIndex = _TdmaCsModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 2, 1, 1, 10),
    _TdmaCsModemIndex_Type()
)
tdmaCsModemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmaCsModemIndex.setStatus("mandatory")
_TdmaCsFax_ObjectIdentity = ObjectIdentity
tdmaCsFax = _TdmaCsFax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 3)
)
_TdmaCsFaxRowStatusTable_Object = MibTable
tdmaCsFaxRowStatusTable = _TdmaCsFaxRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 3, 1)
)
if mibBuilder.loadTexts:
    tdmaCsFaxRowStatusTable.setStatus("mandatory")
_TdmaCsFaxRowStatusEntry_Object = MibTableRow
tdmaCsFaxRowStatusEntry = _TdmaCsFaxRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 3, 1, 1)
)
tdmaCsFaxRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsFaxIndex"),
)
if mibBuilder.loadTexts:
    tdmaCsFaxRowStatusEntry.setStatus("mandatory")
_TdmaCsFaxRowStatus_Type = RowStatus
_TdmaCsFaxRowStatus_Object = MibTableColumn
tdmaCsFaxRowStatus = _TdmaCsFaxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 3, 1, 1, 1),
    _TdmaCsFaxRowStatus_Type()
)
tdmaCsFaxRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsFaxRowStatus.setStatus("mandatory")
_TdmaCsFaxComponentName_Type = DisplayString
_TdmaCsFaxComponentName_Object = MibTableColumn
tdmaCsFaxComponentName = _TdmaCsFaxComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 3, 1, 1, 2),
    _TdmaCsFaxComponentName_Type()
)
tdmaCsFaxComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsFaxComponentName.setStatus("mandatory")
_TdmaCsFaxStorageType_Type = StorageType
_TdmaCsFaxStorageType_Object = MibTableColumn
tdmaCsFaxStorageType = _TdmaCsFaxStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 3, 1, 1, 4),
    _TdmaCsFaxStorageType_Type()
)
tdmaCsFaxStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsFaxStorageType.setStatus("mandatory")
_TdmaCsFaxIndex_Type = NonReplicated
_TdmaCsFaxIndex_Object = MibTableColumn
tdmaCsFaxIndex = _TdmaCsFaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 3, 1, 1, 10),
    _TdmaCsFaxIndex_Type()
)
tdmaCsFaxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmaCsFaxIndex.setStatus("mandatory")
_TdmaCsDce_ObjectIdentity = ObjectIdentity
tdmaCsDce = _TdmaCsDce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 4)
)
_TdmaCsDceRowStatusTable_Object = MibTable
tdmaCsDceRowStatusTable = _TdmaCsDceRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 4, 1)
)
if mibBuilder.loadTexts:
    tdmaCsDceRowStatusTable.setStatus("mandatory")
_TdmaCsDceRowStatusEntry_Object = MibTableRow
tdmaCsDceRowStatusEntry = _TdmaCsDceRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 4, 1, 1)
)
tdmaCsDceRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsDceIndex"),
)
if mibBuilder.loadTexts:
    tdmaCsDceRowStatusEntry.setStatus("mandatory")
_TdmaCsDceRowStatus_Type = RowStatus
_TdmaCsDceRowStatus_Object = MibTableColumn
tdmaCsDceRowStatus = _TdmaCsDceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 4, 1, 1, 1),
    _TdmaCsDceRowStatus_Type()
)
tdmaCsDceRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsDceRowStatus.setStatus("mandatory")
_TdmaCsDceComponentName_Type = DisplayString
_TdmaCsDceComponentName_Object = MibTableColumn
tdmaCsDceComponentName = _TdmaCsDceComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 4, 1, 1, 2),
    _TdmaCsDceComponentName_Type()
)
tdmaCsDceComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsDceComponentName.setStatus("mandatory")
_TdmaCsDceStorageType_Type = StorageType
_TdmaCsDceStorageType_Object = MibTableColumn
tdmaCsDceStorageType = _TdmaCsDceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 4, 1, 1, 4),
    _TdmaCsDceStorageType_Type()
)
tdmaCsDceStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsDceStorageType.setStatus("mandatory")
_TdmaCsDceIndex_Type = NonReplicated
_TdmaCsDceIndex_Object = MibTableColumn
tdmaCsDceIndex = _TdmaCsDceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 4, 1, 1, 10),
    _TdmaCsDceIndex_Type()
)
tdmaCsDceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmaCsDceIndex.setStatus("mandatory")
_TdmaCsDsc_ObjectIdentity = ObjectIdentity
tdmaCsDsc = _TdmaCsDsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 5)
)
_TdmaCsDscRowStatusTable_Object = MibTable
tdmaCsDscRowStatusTable = _TdmaCsDscRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 5, 1)
)
if mibBuilder.loadTexts:
    tdmaCsDscRowStatusTable.setStatus("mandatory")
_TdmaCsDscRowStatusEntry_Object = MibTableRow
tdmaCsDscRowStatusEntry = _TdmaCsDscRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 5, 1, 1)
)
tdmaCsDscRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsDscIndex"),
)
if mibBuilder.loadTexts:
    tdmaCsDscRowStatusEntry.setStatus("mandatory")
_TdmaCsDscRowStatus_Type = RowStatus
_TdmaCsDscRowStatus_Object = MibTableColumn
tdmaCsDscRowStatus = _TdmaCsDscRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 5, 1, 1, 1),
    _TdmaCsDscRowStatus_Type()
)
tdmaCsDscRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsDscRowStatus.setStatus("mandatory")
_TdmaCsDscComponentName_Type = DisplayString
_TdmaCsDscComponentName_Object = MibTableColumn
tdmaCsDscComponentName = _TdmaCsDscComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 5, 1, 1, 2),
    _TdmaCsDscComponentName_Type()
)
tdmaCsDscComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsDscComponentName.setStatus("mandatory")
_TdmaCsDscStorageType_Type = StorageType
_TdmaCsDscStorageType_Object = MibTableColumn
tdmaCsDscStorageType = _TdmaCsDscStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 5, 1, 1, 4),
    _TdmaCsDscStorageType_Type()
)
tdmaCsDscStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsDscStorageType.setStatus("mandatory")
_TdmaCsDscIndex_Type = NonReplicated
_TdmaCsDscIndex_Object = MibTableColumn
tdmaCsDscIndex = _TdmaCsDscIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 5, 1, 1, 10),
    _TdmaCsDscIndex_Type()
)
tdmaCsDscIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmaCsDscIndex.setStatus("mandatory")
_TdmaCsDscProvTable_Object = MibTable
tdmaCsDscProvTable = _TdmaCsDscProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 5, 10)
)
if mibBuilder.loadTexts:
    tdmaCsDscProvTable.setStatus("mandatory")
_TdmaCsDscProvEntry_Object = MibTableRow
tdmaCsDscProvEntry = _TdmaCsDscProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 5, 10, 1)
)
tdmaCsDscProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsDscIndex"),
)
if mibBuilder.loadTexts:
    tdmaCsDscProvEntry.setStatus("mandatory")


class _TdmaCsDscLl0BufferSize_Type(Unsigned32):
    """Custom type tdmaCsDscLl0BufferSize based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 65535),
    )


_TdmaCsDscLl0BufferSize_Type.__name__ = "Unsigned32"
_TdmaCsDscLl0BufferSize_Object = MibTableColumn
tdmaCsDscLl0BufferSize = _TdmaCsDscLl0BufferSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 5, 10, 1, 1),
    _TdmaCsDscLl0BufferSize_Type()
)
tdmaCsDscLl0BufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsDscLl0BufferSize.setStatus("obsolete")


class _TdmaCsDscLl1BufferSize_Type(Unsigned32):
    """Custom type tdmaCsDscLl1BufferSize based on Unsigned32"""
    defaultValue = 160

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(160, 65535),
    )


_TdmaCsDscLl1BufferSize_Type.__name__ = "Unsigned32"
_TdmaCsDscLl1BufferSize_Object = MibTableColumn
tdmaCsDscLl1BufferSize = _TdmaCsDscLl1BufferSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 5, 10, 1, 2),
    _TdmaCsDscLl1BufferSize_Type()
)
tdmaCsDscLl1BufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsDscLl1BufferSize.setStatus("obsolete")


class _TdmaCsDscK0Ll0WindowSize_Type(Unsigned32):
    """Custom type tdmaCsDscK0Ll0WindowSize based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_TdmaCsDscK0Ll0WindowSize_Type.__name__ = "Unsigned32"
_TdmaCsDscK0Ll0WindowSize_Object = MibTableColumn
tdmaCsDscK0Ll0WindowSize = _TdmaCsDscK0Ll0WindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 5, 10, 1, 3),
    _TdmaCsDscK0Ll0WindowSize_Type()
)
tdmaCsDscK0Ll0WindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsDscK0Ll0WindowSize.setStatus("mandatory")


class _TdmaCsDscK1Ll1WindowSize_Type(Unsigned32):
    """Custom type tdmaCsDscK1Ll1WindowSize based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_TdmaCsDscK1Ll1WindowSize_Type.__name__ = "Unsigned32"
_TdmaCsDscK1Ll1WindowSize_Object = MibTableColumn
tdmaCsDscK1Ll1WindowSize = _TdmaCsDscK1Ll1WindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 5, 10, 1, 4),
    _TdmaCsDscK1Ll1WindowSize_Type()
)
tdmaCsDscK1Ll1WindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsDscK1Ll1WindowSize.setStatus("mandatory")


class _TdmaCsDscP0CompressionDirection_Type(Integer32):
    """Custom type tdmaCsDscP0CompressionDirection based on Integer32"""
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
        *(("compBoth", 3),
          ("compInitrResp", 1),
          ("compRespInitr", 2),
          ("noCompression", 0))
    )


_TdmaCsDscP0CompressionDirection_Type.__name__ = "Integer32"
_TdmaCsDscP0CompressionDirection_Object = MibTableColumn
tdmaCsDscP0CompressionDirection = _TdmaCsDscP0CompressionDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 5, 10, 1, 5),
    _TdmaCsDscP0CompressionDirection_Type()
)
tdmaCsDscP0CompressionDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsDscP0CompressionDirection.setStatus("obsolete")


class _TdmaCsDscP1CompressionMaximumCodewords_Type(Unsigned32):
    """Custom type tdmaCsDscP1CompressionMaximumCodewords based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 4096),
    )


_TdmaCsDscP1CompressionMaximumCodewords_Type.__name__ = "Unsigned32"
_TdmaCsDscP1CompressionMaximumCodewords_Object = MibTableColumn
tdmaCsDscP1CompressionMaximumCodewords = _TdmaCsDscP1CompressionMaximumCodewords_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 5, 10, 1, 6),
    _TdmaCsDscP1CompressionMaximumCodewords_Type()
)
tdmaCsDscP1CompressionMaximumCodewords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsDscP1CompressionMaximumCodewords.setStatus("obsolete")


class _TdmaCsDscP2CompressionMaximumCharacters_Type(Unsigned32):
    """Custom type tdmaCsDscP2CompressionMaximumCharacters based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 150),
    )


_TdmaCsDscP2CompressionMaximumCharacters_Type.__name__ = "Unsigned32"
_TdmaCsDscP2CompressionMaximumCharacters_Object = MibTableColumn
tdmaCsDscP2CompressionMaximumCharacters = _TdmaCsDscP2CompressionMaximumCharacters_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 5, 10, 1, 7),
    _TdmaCsDscP2CompressionMaximumCharacters_Type()
)
tdmaCsDscP2CompressionMaximumCharacters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsDscP2CompressionMaximumCharacters.setStatus("obsolete")
_TdmaCsRlp1_ObjectIdentity = ObjectIdentity
tdmaCsRlp1 = _TdmaCsRlp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 6)
)
_TdmaCsRlp1RowStatusTable_Object = MibTable
tdmaCsRlp1RowStatusTable = _TdmaCsRlp1RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 6, 1)
)
if mibBuilder.loadTexts:
    tdmaCsRlp1RowStatusTable.setStatus("mandatory")
_TdmaCsRlp1RowStatusEntry_Object = MibTableRow
tdmaCsRlp1RowStatusEntry = _TdmaCsRlp1RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 6, 1, 1)
)
tdmaCsRlp1RowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsRlp1Index"),
)
if mibBuilder.loadTexts:
    tdmaCsRlp1RowStatusEntry.setStatus("mandatory")
_TdmaCsRlp1RowStatus_Type = RowStatus
_TdmaCsRlp1RowStatus_Object = MibTableColumn
tdmaCsRlp1RowStatus = _TdmaCsRlp1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 6, 1, 1, 1),
    _TdmaCsRlp1RowStatus_Type()
)
tdmaCsRlp1RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsRlp1RowStatus.setStatus("mandatory")
_TdmaCsRlp1ComponentName_Type = DisplayString
_TdmaCsRlp1ComponentName_Object = MibTableColumn
tdmaCsRlp1ComponentName = _TdmaCsRlp1ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 6, 1, 1, 2),
    _TdmaCsRlp1ComponentName_Type()
)
tdmaCsRlp1ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsRlp1ComponentName.setStatus("mandatory")
_TdmaCsRlp1StorageType_Type = StorageType
_TdmaCsRlp1StorageType_Object = MibTableColumn
tdmaCsRlp1StorageType = _TdmaCsRlp1StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 6, 1, 1, 4),
    _TdmaCsRlp1StorageType_Type()
)
tdmaCsRlp1StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsRlp1StorageType.setStatus("mandatory")


class _TdmaCsRlp1Index_Type(Integer32):
    """Custom type tdmaCsRlp1Index based on Integer32"""
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
        *(("doubleRate", 2),
          ("fullRate", 1),
          ("halfRate", 0),
          ("tripleRate", 3))
    )


_TdmaCsRlp1Index_Type.__name__ = "Integer32"
_TdmaCsRlp1Index_Object = MibTableColumn
tdmaCsRlp1Index = _TdmaCsRlp1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 6, 1, 1, 10),
    _TdmaCsRlp1Index_Type()
)
tdmaCsRlp1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmaCsRlp1Index.setStatus("mandatory")
_TdmaCsRlp1ProvTable_Object = MibTable
tdmaCsRlp1ProvTable = _TdmaCsRlp1ProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 6, 10)
)
if mibBuilder.loadTexts:
    tdmaCsRlp1ProvTable.setStatus("mandatory")
_TdmaCsRlp1ProvEntry_Object = MibTableRow
tdmaCsRlp1ProvEntry = _TdmaCsRlp1ProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 6, 10, 1)
)
tdmaCsRlp1ProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsRlp1Index"),
)
if mibBuilder.loadTexts:
    tdmaCsRlp1ProvEntry.setStatus("mandatory")


class _TdmaCsRlp1T1ResponseTimer_Type(Unsigned32):
    """Custom type tdmaCsRlp1T1ResponseTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_TdmaCsRlp1T1ResponseTimer_Type.__name__ = "Unsigned32"
_TdmaCsRlp1T1ResponseTimer_Object = MibTableColumn
tdmaCsRlp1T1ResponseTimer = _TdmaCsRlp1T1ResponseTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 6, 10, 1, 1),
    _TdmaCsRlp1T1ResponseTimer_Type()
)
tdmaCsRlp1T1ResponseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsRlp1T1ResponseTimer.setStatus("mandatory")


class _TdmaCsRlp1T2LinkActivityTimer_Type(Unsigned32):
    """Custom type tdmaCsRlp1T2LinkActivityTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_TdmaCsRlp1T2LinkActivityTimer_Type.__name__ = "Unsigned32"
_TdmaCsRlp1T2LinkActivityTimer_Object = MibTableColumn
tdmaCsRlp1T2LinkActivityTimer = _TdmaCsRlp1T2LinkActivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 6, 10, 1, 2),
    _TdmaCsRlp1T2LinkActivityTimer_Type()
)
tdmaCsRlp1T2LinkActivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsRlp1T2LinkActivityTimer.setStatus("mandatory")


class _TdmaCsRlp1T3PeerAckTimer_Type(Unsigned32):
    """Custom type tdmaCsRlp1T3PeerAckTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_TdmaCsRlp1T3PeerAckTimer_Type.__name__ = "Unsigned32"
_TdmaCsRlp1T3PeerAckTimer_Object = MibTableColumn
tdmaCsRlp1T3PeerAckTimer = _TdmaCsRlp1T3PeerAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 6, 10, 1, 3),
    _TdmaCsRlp1T3PeerAckTimer_Type()
)
tdmaCsRlp1T3PeerAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsRlp1T3PeerAckTimer.setStatus("mandatory")
_TdmaCsV42_ObjectIdentity = ObjectIdentity
tdmaCsV42 = _TdmaCsV42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 7)
)
_TdmaCsV42RowStatusTable_Object = MibTable
tdmaCsV42RowStatusTable = _TdmaCsV42RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 7, 1)
)
if mibBuilder.loadTexts:
    tdmaCsV42RowStatusTable.setStatus("mandatory")
_TdmaCsV42RowStatusEntry_Object = MibTableRow
tdmaCsV42RowStatusEntry = _TdmaCsV42RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 7, 1, 1)
)
tdmaCsV42RowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsV42Index"),
)
if mibBuilder.loadTexts:
    tdmaCsV42RowStatusEntry.setStatus("mandatory")
_TdmaCsV42RowStatus_Type = RowStatus
_TdmaCsV42RowStatus_Object = MibTableColumn
tdmaCsV42RowStatus = _TdmaCsV42RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 7, 1, 1, 1),
    _TdmaCsV42RowStatus_Type()
)
tdmaCsV42RowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsV42RowStatus.setStatus("mandatory")
_TdmaCsV42ComponentName_Type = DisplayString
_TdmaCsV42ComponentName_Object = MibTableColumn
tdmaCsV42ComponentName = _TdmaCsV42ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 7, 1, 1, 2),
    _TdmaCsV42ComponentName_Type()
)
tdmaCsV42ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsV42ComponentName.setStatus("mandatory")
_TdmaCsV42StorageType_Type = StorageType
_TdmaCsV42StorageType_Object = MibTableColumn
tdmaCsV42StorageType = _TdmaCsV42StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 7, 1, 1, 4),
    _TdmaCsV42StorageType_Type()
)
tdmaCsV42StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsV42StorageType.setStatus("mandatory")
_TdmaCsV42Index_Type = NonReplicated
_TdmaCsV42Index_Object = MibTableColumn
tdmaCsV42Index = _TdmaCsV42Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 7, 1, 1, 10),
    _TdmaCsV42Index_Type()
)
tdmaCsV42Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmaCsV42Index.setStatus("mandatory")
_TdmaCsV42ProvTable_Object = MibTable
tdmaCsV42ProvTable = _TdmaCsV42ProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 7, 10)
)
if mibBuilder.loadTexts:
    tdmaCsV42ProvTable.setStatus("mandatory")
_TdmaCsV42ProvEntry_Object = MibTableRow
tdmaCsV42ProvEntry = _TdmaCsV42ProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 7, 10, 1)
)
tdmaCsV42ProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsV42Index"),
)
if mibBuilder.loadTexts:
    tdmaCsV42ProvEntry.setStatus("mandatory")


class _TdmaCsV42T400DetectTimer_Type(FixedPoint2):
    """Custom type tdmaCsV42T400DetectTimer based on FixedPoint2"""
    defaultValue = 75

    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(75, 254),
    )


_TdmaCsV42T400DetectTimer_Type.__name__ = "FixedPoint2"
_TdmaCsV42T400DetectTimer_Object = MibTableColumn
tdmaCsV42T400DetectTimer = _TdmaCsV42T400DetectTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 7, 10, 1, 1),
    _TdmaCsV42T400DetectTimer_Type()
)
tdmaCsV42T400DetectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsV42T400DetectTimer.setStatus("mandatory")


class _TdmaCsV42T401AckTimer_Type(FixedPoint2):
    """Custom type tdmaCsV42T401AckTimer based on FixedPoint2"""
    defaultValue = 400

    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 900),
    )


_TdmaCsV42T401AckTimer_Type.__name__ = "FixedPoint2"
_TdmaCsV42T401AckTimer_Object = MibTableColumn
tdmaCsV42T401AckTimer = _TdmaCsV42T401AckTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 7, 10, 1, 2),
    _TdmaCsV42T401AckTimer_Type()
)
tdmaCsV42T401AckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsV42T401AckTimer.setStatus("mandatory")


class _TdmaCsV42T402AckDelayTimer_Type(FixedPoint2):
    """Custom type tdmaCsV42T402AckDelayTimer based on FixedPoint2"""
    defaultValue = 200

    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 450),
    )


_TdmaCsV42T402AckDelayTimer_Type.__name__ = "FixedPoint2"
_TdmaCsV42T402AckDelayTimer_Object = MibTableColumn
tdmaCsV42T402AckDelayTimer = _TdmaCsV42T402AckDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 7, 10, 1, 3),
    _TdmaCsV42T402AckDelayTimer_Type()
)
tdmaCsV42T402AckDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsV42T402AckDelayTimer.setStatus("mandatory")


class _TdmaCsV42T403IdleProbeTimer_Type(Unsigned32):
    """Custom type tdmaCsV42T403IdleProbeTimer based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 90),
    )


_TdmaCsV42T403IdleProbeTimer_Type.__name__ = "Unsigned32"
_TdmaCsV42T403IdleProbeTimer_Object = MibTableColumn
tdmaCsV42T403IdleProbeTimer = _TdmaCsV42T403IdleProbeTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 7, 10, 1, 4),
    _TdmaCsV42T403IdleProbeTimer_Type()
)
tdmaCsV42T403IdleProbeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsV42T403IdleProbeTimer.setStatus("mandatory")


class _TdmaCsV42TxN401FrameSize_Type(Unsigned32):
    """Custom type tdmaCsV42TxN401FrameSize based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TdmaCsV42TxN401FrameSize_Type.__name__ = "Unsigned32"
_TdmaCsV42TxN401FrameSize_Object = MibTableColumn
tdmaCsV42TxN401FrameSize = _TdmaCsV42TxN401FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 7, 10, 1, 5),
    _TdmaCsV42TxN401FrameSize_Type()
)
tdmaCsV42TxN401FrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsV42TxN401FrameSize.setStatus("mandatory")


class _TdmaCsV42RxN401FrameSize_Type(Unsigned32):
    """Custom type tdmaCsV42RxN401FrameSize based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TdmaCsV42RxN401FrameSize_Type.__name__ = "Unsigned32"
_TdmaCsV42RxN401FrameSize_Object = MibTableColumn
tdmaCsV42RxN401FrameSize = _TdmaCsV42RxN401FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 7, 10, 1, 6),
    _TdmaCsV42RxN401FrameSize_Type()
)
tdmaCsV42RxN401FrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsV42RxN401FrameSize.setStatus("mandatory")


class _TdmaCsV42TxKWindowSize_Type(Unsigned32):
    """Custom type tdmaCsV42TxKWindowSize based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TdmaCsV42TxKWindowSize_Type.__name__ = "Unsigned32"
_TdmaCsV42TxKWindowSize_Object = MibTableColumn
tdmaCsV42TxKWindowSize = _TdmaCsV42TxKWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 7, 10, 1, 7),
    _TdmaCsV42TxKWindowSize_Type()
)
tdmaCsV42TxKWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsV42TxKWindowSize.setStatus("mandatory")


class _TdmaCsV42RxKWindowSize_Type(Unsigned32):
    """Custom type tdmaCsV42RxKWindowSize based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TdmaCsV42RxKWindowSize_Type.__name__ = "Unsigned32"
_TdmaCsV42RxKWindowSize_Object = MibTableColumn
tdmaCsV42RxKWindowSize = _TdmaCsV42RxKWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 7, 10, 1, 8),
    _TdmaCsV42RxKWindowSize_Type()
)
tdmaCsV42RxKWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsV42RxKWindowSize.setStatus("mandatory")


class _TdmaCsV42N400RetransLimit_Type(Unsigned32):
    """Custom type tdmaCsV42N400RetransLimit based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TdmaCsV42N400RetransLimit_Type.__name__ = "Unsigned32"
_TdmaCsV42N400RetransLimit_Object = MibTableColumn
tdmaCsV42N400RetransLimit = _TdmaCsV42N400RetransLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 7, 10, 1, 9),
    _TdmaCsV42N400RetransLimit_Type()
)
tdmaCsV42N400RetransLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsV42N400RetransLimit.setStatus("mandatory")


class _TdmaCsV42FcsLength_Type(Integer32):
    """Custom type tdmaCsV42FcsLength based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fcs16", 0),
          ("fcs32", 2),
          ("fcs32Or16", 1))
    )


_TdmaCsV42FcsLength_Type.__name__ = "Integer32"
_TdmaCsV42FcsLength_Object = MibTableColumn
tdmaCsV42FcsLength = _TdmaCsV42FcsLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 7, 10, 1, 10),
    _TdmaCsV42FcsLength_Type()
)
tdmaCsV42FcsLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsV42FcsLength.setStatus("mandatory")
_TdmaCsV42Bis_ObjectIdentity = ObjectIdentity
tdmaCsV42Bis = _TdmaCsV42Bis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 8)
)
_TdmaCsV42BisRowStatusTable_Object = MibTable
tdmaCsV42BisRowStatusTable = _TdmaCsV42BisRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 8, 1)
)
if mibBuilder.loadTexts:
    tdmaCsV42BisRowStatusTable.setStatus("mandatory")
_TdmaCsV42BisRowStatusEntry_Object = MibTableRow
tdmaCsV42BisRowStatusEntry = _TdmaCsV42BisRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 8, 1, 1)
)
tdmaCsV42BisRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsV42BisIndex"),
)
if mibBuilder.loadTexts:
    tdmaCsV42BisRowStatusEntry.setStatus("mandatory")
_TdmaCsV42BisRowStatus_Type = RowStatus
_TdmaCsV42BisRowStatus_Object = MibTableColumn
tdmaCsV42BisRowStatus = _TdmaCsV42BisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 8, 1, 1, 1),
    _TdmaCsV42BisRowStatus_Type()
)
tdmaCsV42BisRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsV42BisRowStatus.setStatus("mandatory")
_TdmaCsV42BisComponentName_Type = DisplayString
_TdmaCsV42BisComponentName_Object = MibTableColumn
tdmaCsV42BisComponentName = _TdmaCsV42BisComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 8, 1, 1, 2),
    _TdmaCsV42BisComponentName_Type()
)
tdmaCsV42BisComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsV42BisComponentName.setStatus("mandatory")
_TdmaCsV42BisStorageType_Type = StorageType
_TdmaCsV42BisStorageType_Object = MibTableColumn
tdmaCsV42BisStorageType = _TdmaCsV42BisStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 8, 1, 1, 4),
    _TdmaCsV42BisStorageType_Type()
)
tdmaCsV42BisStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsV42BisStorageType.setStatus("mandatory")
_TdmaCsV42BisIndex_Type = NonReplicated
_TdmaCsV42BisIndex_Object = MibTableColumn
tdmaCsV42BisIndex = _TdmaCsV42BisIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 8, 1, 1, 10),
    _TdmaCsV42BisIndex_Type()
)
tdmaCsV42BisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmaCsV42BisIndex.setStatus("mandatory")
_TdmaCsV42BisProvTable_Object = MibTable
tdmaCsV42BisProvTable = _TdmaCsV42BisProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 8, 10)
)
if mibBuilder.loadTexts:
    tdmaCsV42BisProvTable.setStatus("mandatory")
_TdmaCsV42BisProvEntry_Object = MibTableRow
tdmaCsV42BisProvEntry = _TdmaCsV42BisProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 8, 10, 1)
)
tdmaCsV42BisProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsV42BisIndex"),
)
if mibBuilder.loadTexts:
    tdmaCsV42BisProvEntry.setStatus("mandatory")


class _TdmaCsV42BisP0CompressionDirection_Type(Integer32):
    """Custom type tdmaCsV42BisP0CompressionDirection based on Integer32"""
    defaultValue = 3

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
        *(("compBoth", 3),
          ("compInitrResp", 1),
          ("compRespInitr", 2),
          ("noCompression", 0))
    )


_TdmaCsV42BisP0CompressionDirection_Type.__name__ = "Integer32"
_TdmaCsV42BisP0CompressionDirection_Object = MibTableColumn
tdmaCsV42BisP0CompressionDirection = _TdmaCsV42BisP0CompressionDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 8, 10, 1, 1),
    _TdmaCsV42BisP0CompressionDirection_Type()
)
tdmaCsV42BisP0CompressionDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsV42BisP0CompressionDirection.setStatus("mandatory")


class _TdmaCsV42BisP1MaximumCodewords_Type(Unsigned32):
    """Custom type tdmaCsV42BisP1MaximumCodewords based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 4096),
    )


_TdmaCsV42BisP1MaximumCodewords_Type.__name__ = "Unsigned32"
_TdmaCsV42BisP1MaximumCodewords_Object = MibTableColumn
tdmaCsV42BisP1MaximumCodewords = _TdmaCsV42BisP1MaximumCodewords_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 8, 10, 1, 2),
    _TdmaCsV42BisP1MaximumCodewords_Type()
)
tdmaCsV42BisP1MaximumCodewords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsV42BisP1MaximumCodewords.setStatus("mandatory")


class _TdmaCsV42BisP2MaximumStringSize_Type(Unsigned32):
    """Custom type tdmaCsV42BisP2MaximumStringSize based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 250),
    )


_TdmaCsV42BisP2MaximumStringSize_Type.__name__ = "Unsigned32"
_TdmaCsV42BisP2MaximumStringSize_Object = MibTableColumn
tdmaCsV42BisP2MaximumStringSize = _TdmaCsV42BisP2MaximumStringSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 8, 10, 1, 3),
    _TdmaCsV42BisP2MaximumStringSize_Type()
)
tdmaCsV42BisP2MaximumStringSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsV42BisP2MaximumStringSize.setStatus("mandatory")


class _TdmaCsV42BisActionOnError_Type(Integer32):
    """Custom type tdmaCsV42BisActionOnError based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("resetLink", 0),
          ("takeDownCall", 1))
    )


_TdmaCsV42BisActionOnError_Type.__name__ = "Integer32"
_TdmaCsV42BisActionOnError_Object = MibTableColumn
tdmaCsV42BisActionOnError = _TdmaCsV42BisActionOnError_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 8, 10, 1, 4),
    _TdmaCsV42BisActionOnError_Type()
)
tdmaCsV42BisActionOnError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsV42BisActionOnError.setStatus("mandatory")
_TdmaCsLp_ObjectIdentity = ObjectIdentity
tdmaCsLp = _TdmaCsLp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 9)
)
_TdmaCsLpRowStatusTable_Object = MibTable
tdmaCsLpRowStatusTable = _TdmaCsLpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 9, 1)
)
if mibBuilder.loadTexts:
    tdmaCsLpRowStatusTable.setStatus("mandatory")
_TdmaCsLpRowStatusEntry_Object = MibTableRow
tdmaCsLpRowStatusEntry = _TdmaCsLpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 9, 1, 1)
)
tdmaCsLpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsLpIndex"),
)
if mibBuilder.loadTexts:
    tdmaCsLpRowStatusEntry.setStatus("mandatory")
_TdmaCsLpRowStatus_Type = RowStatus
_TdmaCsLpRowStatus_Object = MibTableColumn
tdmaCsLpRowStatus = _TdmaCsLpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 9, 1, 1, 1),
    _TdmaCsLpRowStatus_Type()
)
tdmaCsLpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsLpRowStatus.setStatus("mandatory")
_TdmaCsLpComponentName_Type = DisplayString
_TdmaCsLpComponentName_Object = MibTableColumn
tdmaCsLpComponentName = _TdmaCsLpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 9, 1, 1, 2),
    _TdmaCsLpComponentName_Type()
)
tdmaCsLpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsLpComponentName.setStatus("mandatory")
_TdmaCsLpStorageType_Type = StorageType
_TdmaCsLpStorageType_Object = MibTableColumn
tdmaCsLpStorageType = _TdmaCsLpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 9, 1, 1, 4),
    _TdmaCsLpStorageType_Type()
)
tdmaCsLpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsLpStorageType.setStatus("mandatory")


class _TdmaCsLpIndex_Type(Integer32):
    """Custom type tdmaCsLpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TdmaCsLpIndex_Type.__name__ = "Integer32"
_TdmaCsLpIndex_Object = MibTableColumn
tdmaCsLpIndex = _TdmaCsLpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 9, 1, 1, 10),
    _TdmaCsLpIndex_Type()
)
tdmaCsLpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmaCsLpIndex.setStatus("mandatory")
_TdmaCsLpOperTable_Object = MibTable
tdmaCsLpOperTable = _TdmaCsLpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 9, 10)
)
if mibBuilder.loadTexts:
    tdmaCsLpOperTable.setStatus("mandatory")
_TdmaCsLpOperEntry_Object = MibTableRow
tdmaCsLpOperEntry = _TdmaCsLpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 9, 10, 1)
)
tdmaCsLpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsLpIndex"),
)
if mibBuilder.loadTexts:
    tdmaCsLpOperEntry.setStatus("mandatory")


class _TdmaCsLpConfiguredBearerChannels_Type(Unsigned32):
    """Custom type tdmaCsLpConfiguredBearerChannels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 124),
    )


_TdmaCsLpConfiguredBearerChannels_Type.__name__ = "Unsigned32"
_TdmaCsLpConfiguredBearerChannels_Object = MibTableColumn
tdmaCsLpConfiguredBearerChannels = _TdmaCsLpConfiguredBearerChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 9, 10, 1, 1),
    _TdmaCsLpConfiguredBearerChannels_Type()
)
tdmaCsLpConfiguredBearerChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsLpConfiguredBearerChannels.setStatus("mandatory")


class _TdmaCsLpActiveCalls_Type(Gauge32):
    """Custom type tdmaCsLpActiveCalls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 124),
    )


_TdmaCsLpActiveCalls_Type.__name__ = "Gauge32"
_TdmaCsLpActiveCalls_Object = MibTableColumn
tdmaCsLpActiveCalls = _TdmaCsLpActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 9, 10, 1, 2),
    _TdmaCsLpActiveCalls_Type()
)
tdmaCsLpActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsLpActiveCalls.setStatus("mandatory")


class _TdmaCsLpModemsSupported_Type(Integer32):
    """Custom type tdmaCsLpModemsSupported based on Integer32"""
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


_TdmaCsLpModemsSupported_Type.__name__ = "Integer32"
_TdmaCsLpModemsSupported_Object = MibTableColumn
tdmaCsLpModemsSupported = _TdmaCsLpModemsSupported_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 9, 10, 1, 3),
    _TdmaCsLpModemsSupported_Type()
)
tdmaCsLpModemsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsLpModemsSupported.setStatus("mandatory")
_TdmaCsServProvTable_Object = MibTable
tdmaCsServProvTable = _TdmaCsServProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 100)
)
if mibBuilder.loadTexts:
    tdmaCsServProvTable.setStatus("mandatory")
_TdmaCsServProvEntry_Object = MibTableRow
tdmaCsServProvEntry = _TdmaCsServProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 100, 1)
)
tdmaCsServProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsCsIndex"),
)
if mibBuilder.loadTexts:
    tdmaCsServProvEntry.setStatus("mandatory")


class _TdmaCsTIwf1_Type(Unsigned32):
    """Custom type tdmaCsTIwf1 based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_TdmaCsTIwf1_Type.__name__ = "Unsigned32"
_TdmaCsTIwf1_Object = MibTableColumn
tdmaCsTIwf1 = _TdmaCsTIwf1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 100, 1, 1),
    _TdmaCsTIwf1_Type()
)
tdmaCsTIwf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsTIwf1.setStatus("mandatory")


class _TdmaCsTIwf2_Type(Unsigned32):
    """Custom type tdmaCsTIwf2 based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_TdmaCsTIwf2_Type.__name__ = "Unsigned32"
_TdmaCsTIwf2_Object = MibTableColumn
tdmaCsTIwf2 = _TdmaCsTIwf2_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 100, 1, 2),
    _TdmaCsTIwf2_Type()
)
tdmaCsTIwf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsTIwf2.setStatus("mandatory")


class _TdmaCsT303_Type(Unsigned32):
    """Custom type tdmaCsT303 based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_TdmaCsT303_Type.__name__ = "Unsigned32"
_TdmaCsT303_Object = MibTableColumn
tdmaCsT303 = _TdmaCsT303_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 100, 1, 3),
    _TdmaCsT303_Type()
)
tdmaCsT303.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsT303.setStatus("mandatory")


class _TdmaCsT305_Type(Unsigned32):
    """Custom type tdmaCsT305 based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_TdmaCsT305_Type.__name__ = "Unsigned32"
_TdmaCsT305_Object = MibTableColumn
tdmaCsT305 = _TdmaCsT305_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 100, 1, 4),
    _TdmaCsT305_Type()
)
tdmaCsT305.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsT305.setStatus("mandatory")


class _TdmaCsT308_Type(Unsigned32):
    """Custom type tdmaCsT308 based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_TdmaCsT308_Type.__name__ = "Unsigned32"
_TdmaCsT308_Object = MibTableColumn
tdmaCsT308 = _TdmaCsT308_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 100, 1, 5),
    _TdmaCsT308_Type()
)
tdmaCsT308.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsT308.setStatus("mandatory")


class _TdmaCsT313_Type(Unsigned32):
    """Custom type tdmaCsT313 based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_TdmaCsT313_Type.__name__ = "Unsigned32"
_TdmaCsT313_Object = MibTableColumn
tdmaCsT313 = _TdmaCsT313_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 100, 1, 6),
    _TdmaCsT313_Type()
)
tdmaCsT313.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsT313.setStatus("mandatory")


class _TdmaCsT999_Type(Unsigned32):
    """Custom type tdmaCsT999 based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_TdmaCsT999_Type.__name__ = "Unsigned32"
_TdmaCsT999_Object = MibTableColumn
tdmaCsT999 = _TdmaCsT999_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 100, 1, 7),
    _TdmaCsT999_Type()
)
tdmaCsT999.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsT999.setStatus("mandatory")


class _TdmaCsSupportedTechnology_Type(Integer32):
    """Custom type tdmaCsSupportedTechnology based on Integer32"""
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
        *(("cdmaOnly", 1),
          ("tdmaAndCdma", 2),
          ("tdmaOnly", 0))
    )


_TdmaCsSupportedTechnology_Type.__name__ = "Integer32"
_TdmaCsSupportedTechnology_Object = MibTableColumn
tdmaCsSupportedTechnology = _TdmaCsSupportedTechnology_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 100, 1, 8),
    _TdmaCsSupportedTechnology_Type()
)
tdmaCsSupportedTechnology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsSupportedTechnology.setStatus("mandatory")


class _TdmaCsSupportedService_Type(Integer32):
    """Custom type tdmaCsSupportedService based on Integer32"""
    defaultValue = 0

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
        *(("analogFaxOnly", 2),
          ("asyncDataAFaxAndPacket", 8),
          ("asyncDataAndAnalogFax", 5),
          ("asyncDataAndG3Fax", 4),
          ("asyncDataAndPacket", 6),
          ("asyncDataG3FaxAndPacket", 7),
          ("asyncDataOnly", 0),
          ("g3FaxOnly", 1),
          ("packetOnly", 3))
    )


_TdmaCsSupportedService_Type.__name__ = "Integer32"
_TdmaCsSupportedService_Object = MibTableColumn
tdmaCsSupportedService = _TdmaCsSupportedService_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 100, 1, 9),
    _TdmaCsSupportedService_Type()
)
tdmaCsSupportedService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsSupportedService.setStatus("mandatory")
_TdmaCsMiscProvTable_Object = MibTable
tdmaCsMiscProvTable = _TdmaCsMiscProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 101)
)
if mibBuilder.loadTexts:
    tdmaCsMiscProvTable.setStatus("mandatory")
_TdmaCsMiscProvEntry_Object = MibTableRow
tdmaCsMiscProvEntry = _TdmaCsMiscProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 101, 1)
)
tdmaCsMiscProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsCsIndex"),
)
if mibBuilder.loadTexts:
    tdmaCsMiscProvEntry.setStatus("mandatory")


class _TdmaCsCommentText_Type(AsciiString):
    """Custom type tdmaCsCommentText based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TdmaCsCommentText_Type.__name__ = "AsciiString"
_TdmaCsCommentText_Object = MibTableColumn
tdmaCsCommentText = _TdmaCsCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 101, 1, 1),
    _TdmaCsCommentText_Type()
)
tdmaCsCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsCommentText.setStatus("mandatory")


class _TdmaCsMscIpAddress_Type(IpAddress):
    """Custom type tdmaCsMscIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TdmaCsMscIpAddress_Object = MibTableColumn
tdmaCsMscIpAddress = _TdmaCsMscIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 101, 1, 2),
    _TdmaCsMscIpAddress_Type()
)
tdmaCsMscIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsMscIpAddress.setStatus("mandatory")
_TdmaCsVirtualRouterName_Type = RowPointer
_TdmaCsVirtualRouterName_Object = MibTableColumn
tdmaCsVirtualRouterName = _TdmaCsVirtualRouterName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 101, 1, 3),
    _TdmaCsVirtualRouterName_Type()
)
tdmaCsVirtualRouterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsVirtualRouterName.setStatus("mandatory")


class _TdmaCsVoiceLaw_Type(Integer32):
    """Custom type tdmaCsVoiceLaw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aLaw", 0),
          ("muLaw", 1))
    )


_TdmaCsVoiceLaw_Type.__name__ = "Integer32"
_TdmaCsVoiceLaw_Object = MibTableColumn
tdmaCsVoiceLaw = _TdmaCsVoiceLaw_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 101, 1, 4),
    _TdmaCsVoiceLaw_Type()
)
tdmaCsVoiceLaw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsVoiceLaw.setStatus("mandatory")
_TdmaCsCidDataTable_Object = MibTable
tdmaCsCidDataTable = _TdmaCsCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 103)
)
if mibBuilder.loadTexts:
    tdmaCsCidDataTable.setStatus("mandatory")
_TdmaCsCidDataEntry_Object = MibTableRow
tdmaCsCidDataEntry = _TdmaCsCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 103, 1)
)
tdmaCsCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsCsIndex"),
)
if mibBuilder.loadTexts:
    tdmaCsCidDataEntry.setStatus("mandatory")


class _TdmaCsCustomerIdentifier_Type(Unsigned32):
    """Custom type tdmaCsCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_TdmaCsCustomerIdentifier_Type.__name__ = "Unsigned32"
_TdmaCsCustomerIdentifier_Object = MibTableColumn
tdmaCsCustomerIdentifier = _TdmaCsCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 103, 1, 1),
    _TdmaCsCustomerIdentifier_Type()
)
tdmaCsCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaCsCustomerIdentifier.setStatus("mandatory")
_TdmaCsStateTable_Object = MibTable
tdmaCsStateTable = _TdmaCsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 104)
)
if mibBuilder.loadTexts:
    tdmaCsStateTable.setStatus("mandatory")
_TdmaCsStateEntry_Object = MibTableRow
tdmaCsStateEntry = _TdmaCsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 104, 1)
)
tdmaCsStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsCsIndex"),
)
if mibBuilder.loadTexts:
    tdmaCsStateEntry.setStatus("mandatory")


class _TdmaCsAdminState_Type(Integer32):
    """Custom type tdmaCsAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_TdmaCsAdminState_Type.__name__ = "Integer32"
_TdmaCsAdminState_Object = MibTableColumn
tdmaCsAdminState = _TdmaCsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 104, 1, 1),
    _TdmaCsAdminState_Type()
)
tdmaCsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsAdminState.setStatus("mandatory")


class _TdmaCsOperationalState_Type(Integer32):
    """Custom type tdmaCsOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TdmaCsOperationalState_Type.__name__ = "Integer32"
_TdmaCsOperationalState_Object = MibTableColumn
tdmaCsOperationalState = _TdmaCsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 104, 1, 2),
    _TdmaCsOperationalState_Type()
)
tdmaCsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsOperationalState.setStatus("mandatory")


class _TdmaCsUsageState_Type(Integer32):
    """Custom type tdmaCsUsageState based on Integer32"""
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
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_TdmaCsUsageState_Type.__name__ = "Integer32"
_TdmaCsUsageState_Object = MibTableColumn
tdmaCsUsageState = _TdmaCsUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 104, 1, 3),
    _TdmaCsUsageState_Type()
)
tdmaCsUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsUsageState.setStatus("mandatory")
_TdmaCsStatsTable_Object = MibTable
tdmaCsStatsTable = _TdmaCsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 121)
)
if mibBuilder.loadTexts:
    tdmaCsStatsTable.setStatus("mandatory")
_TdmaCsStatsEntry_Object = MibTableRow
tdmaCsStatsEntry = _TdmaCsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 121, 1)
)
tdmaCsStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaCsCsIndex"),
)
if mibBuilder.loadTexts:
    tdmaCsStatsEntry.setStatus("mandatory")


class _TdmaCsCurrentCalls_Type(Gauge32):
    """Custom type tdmaCsCurrentCalls based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_TdmaCsCurrentCalls_Type.__name__ = "Gauge32"
_TdmaCsCurrentCalls_Object = MibTableColumn
tdmaCsCurrentCalls = _TdmaCsCurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 121, 1, 1),
    _TdmaCsCurrentCalls_Type()
)
tdmaCsCurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsCurrentCalls.setStatus("mandatory")
_TdmaCsCallsRequested_Type = Counter32
_TdmaCsCallsRequested_Object = MibTableColumn
tdmaCsCallsRequested = _TdmaCsCallsRequested_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 121, 1, 2),
    _TdmaCsCallsRequested_Type()
)
tdmaCsCallsRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsCallsRequested.setStatus("mandatory")
_TdmaCsCallsSetUp_Type = Counter32
_TdmaCsCallsSetUp_Object = MibTableColumn
tdmaCsCallsSetUp = _TdmaCsCallsSetUp_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 121, 1, 3),
    _TdmaCsCallsSetUp_Type()
)
tdmaCsCallsSetUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsCallsSetUp.setStatus("mandatory")
_TdmaCsCallsReleasedNormal_Type = Counter32
_TdmaCsCallsReleasedNormal_Object = MibTableColumn
tdmaCsCallsReleasedNormal = _TdmaCsCallsReleasedNormal_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 121, 1, 4),
    _TdmaCsCallsReleasedNormal_Type()
)
tdmaCsCallsReleasedNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsCallsReleasedNormal.setStatus("mandatory")
_TdmaCsCallsReleasedAbnormal_Type = Counter32
_TdmaCsCallsReleasedAbnormal_Object = MibTableColumn
tdmaCsCallsReleasedAbnormal = _TdmaCsCallsReleasedAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 121, 1, 5),
    _TdmaCsCallsReleasedAbnormal_Type()
)
tdmaCsCallsReleasedAbnormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsCallsReleasedAbnormal.setStatus("mandatory")
_TdmaCsErroredLFrames_Type = Counter32
_TdmaCsErroredLFrames_Object = MibTableColumn
tdmaCsErroredLFrames = _TdmaCsErroredLFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 135, 121, 1, 6),
    _TdmaCsErroredLFrames_Type()
)
tdmaCsErroredLFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaCsErroredLFrames.setStatus("mandatory")
_TdmaBc_ObjectIdentity = ObjectIdentity
tdmaBc = _TdmaBc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136)
)
_TdmaBcRowStatusTable_Object = MibTable
tdmaBcRowStatusTable = _TdmaBcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 1)
)
if mibBuilder.loadTexts:
    tdmaBcRowStatusTable.setStatus("mandatory")
_TdmaBcRowStatusEntry_Object = MibTableRow
tdmaBcRowStatusEntry = _TdmaBcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 1, 1)
)
tdmaBcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcRowStatusEntry.setStatus("mandatory")
_TdmaBcRowStatus_Type = RowStatus
_TdmaBcRowStatus_Object = MibTableColumn
tdmaBcRowStatus = _TdmaBcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 1, 1, 1),
    _TdmaBcRowStatus_Type()
)
tdmaBcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaBcRowStatus.setStatus("mandatory")
_TdmaBcComponentName_Type = DisplayString
_TdmaBcComponentName_Object = MibTableColumn
tdmaBcComponentName = _TdmaBcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 1, 1, 2),
    _TdmaBcComponentName_Type()
)
tdmaBcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcComponentName.setStatus("mandatory")
_TdmaBcStorageType_Type = StorageType
_TdmaBcStorageType_Object = MibTableColumn
tdmaBcStorageType = _TdmaBcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 1, 1, 4),
    _TdmaBcStorageType_Type()
)
tdmaBcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcStorageType.setStatus("mandatory")


class _TdmaBcCsIndex_Type(Integer32):
    """Custom type tdmaBcCsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TdmaBcCsIndex_Type.__name__ = "Integer32"
_TdmaBcCsIndex_Object = MibTableColumn
tdmaBcCsIndex = _TdmaBcCsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 1, 1, 10),
    _TdmaBcCsIndex_Type()
)
tdmaBcCsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmaBcCsIndex.setStatus("mandatory")


class _TdmaBcBcIndex_Type(Integer32):
    """Custom type tdmaBcBcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_TdmaBcBcIndex_Type.__name__ = "Integer32"
_TdmaBcBcIndex_Object = MibTableColumn
tdmaBcBcIndex = _TdmaBcBcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 1, 1, 11),
    _TdmaBcBcIndex_Type()
)
tdmaBcBcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmaBcBcIndex.setStatus("mandatory")
_TdmaBcFramer_ObjectIdentity = ObjectIdentity
tdmaBcFramer = _TdmaBcFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 2)
)
_TdmaBcFramerRowStatusTable_Object = MibTable
tdmaBcFramerRowStatusTable = _TdmaBcFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 2, 1)
)
if mibBuilder.loadTexts:
    tdmaBcFramerRowStatusTable.setStatus("mandatory")
_TdmaBcFramerRowStatusEntry_Object = MibTableRow
tdmaBcFramerRowStatusEntry = _TdmaBcFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 2, 1, 1)
)
tdmaBcFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcFramerIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcFramerRowStatusEntry.setStatus("mandatory")
_TdmaBcFramerRowStatus_Type = RowStatus
_TdmaBcFramerRowStatus_Object = MibTableColumn
tdmaBcFramerRowStatus = _TdmaBcFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 2, 1, 1, 1),
    _TdmaBcFramerRowStatus_Type()
)
tdmaBcFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcFramerRowStatus.setStatus("mandatory")
_TdmaBcFramerComponentName_Type = DisplayString
_TdmaBcFramerComponentName_Object = MibTableColumn
tdmaBcFramerComponentName = _TdmaBcFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 2, 1, 1, 2),
    _TdmaBcFramerComponentName_Type()
)
tdmaBcFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcFramerComponentName.setStatus("mandatory")
_TdmaBcFramerStorageType_Type = StorageType
_TdmaBcFramerStorageType_Object = MibTableColumn
tdmaBcFramerStorageType = _TdmaBcFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 2, 1, 1, 4),
    _TdmaBcFramerStorageType_Type()
)
tdmaBcFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcFramerStorageType.setStatus("mandatory")
_TdmaBcFramerIndex_Type = NonReplicated
_TdmaBcFramerIndex_Object = MibTableColumn
tdmaBcFramerIndex = _TdmaBcFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 2, 1, 1, 10),
    _TdmaBcFramerIndex_Type()
)
tdmaBcFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmaBcFramerIndex.setStatus("mandatory")
_TdmaBcFramerProvTable_Object = MibTable
tdmaBcFramerProvTable = _TdmaBcFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 2, 10)
)
if mibBuilder.loadTexts:
    tdmaBcFramerProvTable.setStatus("mandatory")
_TdmaBcFramerProvEntry_Object = MibTableRow
tdmaBcFramerProvEntry = _TdmaBcFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 2, 10, 1)
)
tdmaBcFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcFramerIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcFramerProvEntry.setStatus("mandatory")
_TdmaBcFramerInterfaceName_Type = Link
_TdmaBcFramerInterfaceName_Object = MibTableColumn
tdmaBcFramerInterfaceName = _TdmaBcFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 2, 10, 1, 1),
    _TdmaBcFramerInterfaceName_Type()
)
tdmaBcFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaBcFramerInterfaceName.setStatus("mandatory")
_TdmaBcFramerStatsTable_Object = MibTable
tdmaBcFramerStatsTable = _TdmaBcFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 2, 11)
)
if mibBuilder.loadTexts:
    tdmaBcFramerStatsTable.setStatus("mandatory")
_TdmaBcFramerStatsEntry_Object = MibTableRow
tdmaBcFramerStatsEntry = _TdmaBcFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 2, 11, 1)
)
tdmaBcFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcFramerIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcFramerStatsEntry.setStatus("mandatory")
_TdmaBcFramerTxFrames_Type = Counter32
_TdmaBcFramerTxFrames_Object = MibTableColumn
tdmaBcFramerTxFrames = _TdmaBcFramerTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 2, 11, 1, 1),
    _TdmaBcFramerTxFrames_Type()
)
tdmaBcFramerTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcFramerTxFrames.setStatus("mandatory")
_TdmaBcFramerRxFrames_Type = Counter32
_TdmaBcFramerRxFrames_Object = MibTableColumn
tdmaBcFramerRxFrames = _TdmaBcFramerRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 2, 11, 1, 2),
    _TdmaBcFramerRxFrames_Type()
)
tdmaBcFramerRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcFramerRxFrames.setStatus("mandatory")
_TdmaBcFramerRxBytes_Type = Counter32
_TdmaBcFramerRxBytes_Object = MibTableColumn
tdmaBcFramerRxBytes = _TdmaBcFramerRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 2, 11, 1, 3),
    _TdmaBcFramerRxBytes_Type()
)
tdmaBcFramerRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcFramerRxBytes.setStatus("mandatory")
_TdmaBcFramerLinkTable_Object = MibTable
tdmaBcFramerLinkTable = _TdmaBcFramerLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 2, 12)
)
if mibBuilder.loadTexts:
    tdmaBcFramerLinkTable.setStatus("mandatory")
_TdmaBcFramerLinkEntry_Object = MibTableRow
tdmaBcFramerLinkEntry = _TdmaBcFramerLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 2, 12, 1)
)
tdmaBcFramerLinkEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcFramerIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcFramerLinkEntry.setStatus("mandatory")


class _TdmaBcFramerFramingType_Type(Integer32):
    """Custom type tdmaBcFramerFramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              8)
        )
    )
    namedValues = NamedValues(
        *(("btdsFraming", 2),
          ("mtxFraming", 8))
    )


_TdmaBcFramerFramingType_Type.__name__ = "Integer32"
_TdmaBcFramerFramingType_Object = MibTableColumn
tdmaBcFramerFramingType = _TdmaBcFramerFramingType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 2, 12, 1, 1),
    _TdmaBcFramerFramingType_Type()
)
tdmaBcFramerFramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaBcFramerFramingType.setStatus("mandatory")
_TdmaBcFramerStateTable_Object = MibTable
tdmaBcFramerStateTable = _TdmaBcFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 2, 13)
)
if mibBuilder.loadTexts:
    tdmaBcFramerStateTable.setStatus("mandatory")
_TdmaBcFramerStateEntry_Object = MibTableRow
tdmaBcFramerStateEntry = _TdmaBcFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 2, 13, 1)
)
tdmaBcFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcFramerIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcFramerStateEntry.setStatus("mandatory")


class _TdmaBcFramerAdminState_Type(Integer32):
    """Custom type tdmaBcFramerAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_TdmaBcFramerAdminState_Type.__name__ = "Integer32"
_TdmaBcFramerAdminState_Object = MibTableColumn
tdmaBcFramerAdminState = _TdmaBcFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 2, 13, 1, 1),
    _TdmaBcFramerAdminState_Type()
)
tdmaBcFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcFramerAdminState.setStatus("mandatory")


class _TdmaBcFramerOperationalState_Type(Integer32):
    """Custom type tdmaBcFramerOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TdmaBcFramerOperationalState_Type.__name__ = "Integer32"
_TdmaBcFramerOperationalState_Object = MibTableColumn
tdmaBcFramerOperationalState = _TdmaBcFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 2, 13, 1, 2),
    _TdmaBcFramerOperationalState_Type()
)
tdmaBcFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcFramerOperationalState.setStatus("mandatory")


class _TdmaBcFramerUsageState_Type(Integer32):
    """Custom type tdmaBcFramerUsageState based on Integer32"""
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
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_TdmaBcFramerUsageState_Type.__name__ = "Integer32"
_TdmaBcFramerUsageState_Object = MibTableColumn
tdmaBcFramerUsageState = _TdmaBcFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 2, 13, 1, 3),
    _TdmaBcFramerUsageState_Type()
)
tdmaBcFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcFramerUsageState.setStatus("mandatory")
_TdmaBcModem_ObjectIdentity = ObjectIdentity
tdmaBcModem = _TdmaBcModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 3)
)
_TdmaBcModemRowStatusTable_Object = MibTable
tdmaBcModemRowStatusTable = _TdmaBcModemRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 3, 1)
)
if mibBuilder.loadTexts:
    tdmaBcModemRowStatusTable.setStatus("mandatory")
_TdmaBcModemRowStatusEntry_Object = MibTableRow
tdmaBcModemRowStatusEntry = _TdmaBcModemRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 3, 1, 1)
)
tdmaBcModemRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcModemIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcModemRowStatusEntry.setStatus("mandatory")
_TdmaBcModemRowStatus_Type = RowStatus
_TdmaBcModemRowStatus_Object = MibTableColumn
tdmaBcModemRowStatus = _TdmaBcModemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 3, 1, 1, 1),
    _TdmaBcModemRowStatus_Type()
)
tdmaBcModemRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcModemRowStatus.setStatus("mandatory")
_TdmaBcModemComponentName_Type = DisplayString
_TdmaBcModemComponentName_Object = MibTableColumn
tdmaBcModemComponentName = _TdmaBcModemComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 3, 1, 1, 2),
    _TdmaBcModemComponentName_Type()
)
tdmaBcModemComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcModemComponentName.setStatus("mandatory")
_TdmaBcModemStorageType_Type = StorageType
_TdmaBcModemStorageType_Object = MibTableColumn
tdmaBcModemStorageType = _TdmaBcModemStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 3, 1, 1, 4),
    _TdmaBcModemStorageType_Type()
)
tdmaBcModemStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcModemStorageType.setStatus("mandatory")
_TdmaBcModemIndex_Type = NonReplicated
_TdmaBcModemIndex_Object = MibTableColumn
tdmaBcModemIndex = _TdmaBcModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 3, 1, 1, 10),
    _TdmaBcModemIndex_Type()
)
tdmaBcModemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmaBcModemIndex.setStatus("mandatory")
_TdmaBcModemOperTable_Object = MibTable
tdmaBcModemOperTable = _TdmaBcModemOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 3, 10)
)
if mibBuilder.loadTexts:
    tdmaBcModemOperTable.setStatus("mandatory")
_TdmaBcModemOperEntry_Object = MibTableRow
tdmaBcModemOperEntry = _TdmaBcModemOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 3, 10, 1)
)
tdmaBcModemOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcModemIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcModemOperEntry.setStatus("mandatory")


class _TdmaBcModemVoiceLaw_Type(Integer32):
    """Custom type tdmaBcModemVoiceLaw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aLaw", 0),
          ("muLaw", 1))
    )


_TdmaBcModemVoiceLaw_Type.__name__ = "Integer32"
_TdmaBcModemVoiceLaw_Object = MibTableColumn
tdmaBcModemVoiceLaw = _TdmaBcModemVoiceLaw_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 3, 10, 1, 1),
    _TdmaBcModemVoiceLaw_Type()
)
tdmaBcModemVoiceLaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcModemVoiceLaw.setStatus("mandatory")


class _TdmaBcModemRate_Type(Integer32):
    """Custom type tdmaBcModemRate based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("n1200", 3),
          ("n12000", 8),
          ("n14400", 9),
          ("n16800", 10),
          ("n19200", 11),
          ("n21600", 12),
          ("n2400", 4),
          ("n24000", 13),
          ("n26400", 14),
          ("n28800", 15),
          ("n300", 1),
          ("n31200", 16),
          ("n32000", 17),
          ("n33600", 18),
          ("n38400", 19),
          ("n43200", 20),
          ("n4800", 5),
          ("n48000", 21),
          ("n50", 0),
          ("n56000", 22),
          ("n57600", 23),
          ("n600", 2),
          ("n64000", 24),
          ("n7200", 6),
          ("n9600", 7))
    )


_TdmaBcModemRate_Type.__name__ = "Integer32"
_TdmaBcModemRate_Object = MibTableColumn
tdmaBcModemRate = _TdmaBcModemRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 3, 10, 1, 2),
    _TdmaBcModemRate_Type()
)
tdmaBcModemRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcModemRate.setStatus("mandatory")


class _TdmaBcModemModemAlgorithmInUse_Type(OctetString):
    """Custom type tdmaBcModemModemAlgorithmInUse based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_TdmaBcModemModemAlgorithmInUse_Type.__name__ = "OctetString"
_TdmaBcModemModemAlgorithmInUse_Object = MibTableColumn
tdmaBcModemModemAlgorithmInUse = _TdmaBcModemModemAlgorithmInUse_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 3, 10, 1, 3),
    _TdmaBcModemModemAlgorithmInUse_Type()
)
tdmaBcModemModemAlgorithmInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcModemModemAlgorithmInUse.setStatus("mandatory")


class _TdmaBcModemProtocolState_Type(Integer32):
    """Custom type tdmaBcModemProtocolState based on Integer32"""
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
        *(("connected", 2),
          ("idle", 0),
          ("releasing", 3),
          ("training", 1))
    )


_TdmaBcModemProtocolState_Type.__name__ = "Integer32"
_TdmaBcModemProtocolState_Object = MibTableColumn
tdmaBcModemProtocolState = _TdmaBcModemProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 3, 10, 1, 4),
    _TdmaBcModemProtocolState_Type()
)
tdmaBcModemProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcModemProtocolState.setStatus("mandatory")


class _TdmaBcModemMobileSideFlowControlState_Type(Integer32):
    """Custom type tdmaBcModemMobileSideFlowControlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_TdmaBcModemMobileSideFlowControlState_Type.__name__ = "Integer32"
_TdmaBcModemMobileSideFlowControlState_Object = MibTableColumn
tdmaBcModemMobileSideFlowControlState = _TdmaBcModemMobileSideFlowControlState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 3, 10, 1, 5),
    _TdmaBcModemMobileSideFlowControlState_Type()
)
tdmaBcModemMobileSideFlowControlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcModemMobileSideFlowControlState.setStatus("mandatory")


class _TdmaBcModemPstnSideFlowControlState_Type(Integer32):
    """Custom type tdmaBcModemPstnSideFlowControlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_TdmaBcModemPstnSideFlowControlState_Type.__name__ = "Integer32"
_TdmaBcModemPstnSideFlowControlState_Object = MibTableColumn
tdmaBcModemPstnSideFlowControlState = _TdmaBcModemPstnSideFlowControlState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 3, 10, 1, 6),
    _TdmaBcModemPstnSideFlowControlState_Type()
)
tdmaBcModemPstnSideFlowControlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcModemPstnSideFlowControlState.setStatus("mandatory")


class _TdmaBcModemAsyncMode_Type(Integer32):
    """Custom type tdmaBcModemAsyncMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_TdmaBcModemAsyncMode_Type.__name__ = "Integer32"
_TdmaBcModemAsyncMode_Object = MibTableColumn
tdmaBcModemAsyncMode = _TdmaBcModemAsyncMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 3, 10, 1, 7),
    _TdmaBcModemAsyncMode_Type()
)
tdmaBcModemAsyncMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcModemAsyncMode.setStatus("mandatory")


class _TdmaBcModemOutbandFlowControl_Type(Integer32):
    """Custom type tdmaBcModemOutbandFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_TdmaBcModemOutbandFlowControl_Type.__name__ = "Integer32"
_TdmaBcModemOutbandFlowControl_Object = MibTableColumn
tdmaBcModemOutbandFlowControl = _TdmaBcModemOutbandFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 3, 10, 1, 8),
    _TdmaBcModemOutbandFlowControl_Type()
)
tdmaBcModemOutbandFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcModemOutbandFlowControl.setStatus("mandatory")


class _TdmaBcModemOutbandBreak_Type(Integer32):
    """Custom type tdmaBcModemOutbandBreak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_TdmaBcModemOutbandBreak_Type.__name__ = "Integer32"
_TdmaBcModemOutbandBreak_Object = MibTableColumn
tdmaBcModemOutbandBreak = _TdmaBcModemOutbandBreak_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 3, 10, 1, 9),
    _TdmaBcModemOutbandBreak_Type()
)
tdmaBcModemOutbandBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcModemOutbandBreak.setStatus("mandatory")


class _TdmaBcModemAutobaud_Type(Integer32):
    """Custom type tdmaBcModemAutobaud based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_TdmaBcModemAutobaud_Type.__name__ = "Integer32"
_TdmaBcModemAutobaud_Object = MibTableColumn
tdmaBcModemAutobaud = _TdmaBcModemAutobaud_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 3, 10, 1, 10),
    _TdmaBcModemAutobaud_Type()
)
tdmaBcModemAutobaud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcModemAutobaud.setStatus("mandatory")
_TdmaBcModemStatsTable_Object = MibTable
tdmaBcModemStatsTable = _TdmaBcModemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 3, 11)
)
if mibBuilder.loadTexts:
    tdmaBcModemStatsTable.setStatus("mandatory")
_TdmaBcModemStatsEntry_Object = MibTableRow
tdmaBcModemStatsEntry = _TdmaBcModemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 3, 11, 1)
)
tdmaBcModemStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcModemIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcModemStatsEntry.setStatus("mandatory")
_TdmaBcModemTxBytes_Type = Counter32
_TdmaBcModemTxBytes_Object = MibTableColumn
tdmaBcModemTxBytes = _TdmaBcModemTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 3, 11, 1, 1),
    _TdmaBcModemTxBytes_Type()
)
tdmaBcModemTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcModemTxBytes.setStatus("mandatory")
_TdmaBcModemRxBytes_Type = Counter32
_TdmaBcModemRxBytes_Object = MibTableColumn
tdmaBcModemRxBytes = _TdmaBcModemRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 3, 11, 1, 2),
    _TdmaBcModemRxBytes_Type()
)
tdmaBcModemRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcModemRxBytes.setStatus("mandatory")
_TdmaBcModemFramingErrors_Type = Counter32
_TdmaBcModemFramingErrors_Object = MibTableColumn
tdmaBcModemFramingErrors = _TdmaBcModemFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 3, 11, 1, 3),
    _TdmaBcModemFramingErrors_Type()
)
tdmaBcModemFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcModemFramingErrors.setStatus("mandatory")
_TdmaBcFax_ObjectIdentity = ObjectIdentity
tdmaBcFax = _TdmaBcFax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 4)
)
_TdmaBcFaxRowStatusTable_Object = MibTable
tdmaBcFaxRowStatusTable = _TdmaBcFaxRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 4, 1)
)
if mibBuilder.loadTexts:
    tdmaBcFaxRowStatusTable.setStatus("mandatory")
_TdmaBcFaxRowStatusEntry_Object = MibTableRow
tdmaBcFaxRowStatusEntry = _TdmaBcFaxRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 4, 1, 1)
)
tdmaBcFaxRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcFaxIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcFaxRowStatusEntry.setStatus("mandatory")
_TdmaBcFaxRowStatus_Type = RowStatus
_TdmaBcFaxRowStatus_Object = MibTableColumn
tdmaBcFaxRowStatus = _TdmaBcFaxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 4, 1, 1, 1),
    _TdmaBcFaxRowStatus_Type()
)
tdmaBcFaxRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcFaxRowStatus.setStatus("mandatory")
_TdmaBcFaxComponentName_Type = DisplayString
_TdmaBcFaxComponentName_Object = MibTableColumn
tdmaBcFaxComponentName = _TdmaBcFaxComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 4, 1, 1, 2),
    _TdmaBcFaxComponentName_Type()
)
tdmaBcFaxComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcFaxComponentName.setStatus("mandatory")
_TdmaBcFaxStorageType_Type = StorageType
_TdmaBcFaxStorageType_Object = MibTableColumn
tdmaBcFaxStorageType = _TdmaBcFaxStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 4, 1, 1, 4),
    _TdmaBcFaxStorageType_Type()
)
tdmaBcFaxStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcFaxStorageType.setStatus("mandatory")
_TdmaBcFaxIndex_Type = NonReplicated
_TdmaBcFaxIndex_Object = MibTableColumn
tdmaBcFaxIndex = _TdmaBcFaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 4, 1, 1, 10),
    _TdmaBcFaxIndex_Type()
)
tdmaBcFaxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmaBcFaxIndex.setStatus("mandatory")
_TdmaBcFaxOperTable_Object = MibTable
tdmaBcFaxOperTable = _TdmaBcFaxOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 4, 10)
)
if mibBuilder.loadTexts:
    tdmaBcFaxOperTable.setStatus("mandatory")
_TdmaBcFaxOperEntry_Object = MibTableRow
tdmaBcFaxOperEntry = _TdmaBcFaxOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 4, 10, 1)
)
tdmaBcFaxOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcFaxIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcFaxOperEntry.setStatus("mandatory")


class _TdmaBcFaxActiveMode_Type(Integer32):
    """Custom type tdmaBcFaxActiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ecm", 1),
          ("normal", 0))
    )


_TdmaBcFaxActiveMode_Type.__name__ = "Integer32"
_TdmaBcFaxActiveMode_Object = MibTableColumn
tdmaBcFaxActiveMode = _TdmaBcFaxActiveMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 4, 10, 1, 1),
    _TdmaBcFaxActiveMode_Type()
)
tdmaBcFaxActiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcFaxActiveMode.setStatus("mandatory")


class _TdmaBcFaxProtocolState_Type(Integer32):
    """Custom type tdmaBcFaxProtocolState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bcsRx", 2),
          ("bcsTx", 3),
          ("idle", 1),
          ("msgRx", 4),
          ("msgTx", 5),
          ("setup", 0))
    )


_TdmaBcFaxProtocolState_Type.__name__ = "Integer32"
_TdmaBcFaxProtocolState_Object = MibTableColumn
tdmaBcFaxProtocolState = _TdmaBcFaxProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 4, 10, 1, 2),
    _TdmaBcFaxProtocolState_Type()
)
tdmaBcFaxProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcFaxProtocolState.setStatus("mandatory")


class _TdmaBcFaxMessageRate_Type(Unsigned32):
    """Custom type tdmaBcFaxMessageRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_TdmaBcFaxMessageRate_Type.__name__ = "Unsigned32"
_TdmaBcFaxMessageRate_Object = MibTableColumn
tdmaBcFaxMessageRate = _TdmaBcFaxMessageRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 4, 10, 1, 3),
    _TdmaBcFaxMessageRate_Type()
)
tdmaBcFaxMessageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcFaxMessageRate.setStatus("mandatory")
_TdmaBcFaxStatsTable_Object = MibTable
tdmaBcFaxStatsTable = _TdmaBcFaxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 4, 11)
)
if mibBuilder.loadTexts:
    tdmaBcFaxStatsTable.setStatus("mandatory")
_TdmaBcFaxStatsEntry_Object = MibTableRow
tdmaBcFaxStatsEntry = _TdmaBcFaxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 4, 11, 1)
)
tdmaBcFaxStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcFaxIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcFaxStatsEntry.setStatus("mandatory")
_TdmaBcFaxTxPagesToMobile_Type = Counter32
_TdmaBcFaxTxPagesToMobile_Object = MibTableColumn
tdmaBcFaxTxPagesToMobile = _TdmaBcFaxTxPagesToMobile_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 4, 11, 1, 1),
    _TdmaBcFaxTxPagesToMobile_Type()
)
tdmaBcFaxTxPagesToMobile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcFaxTxPagesToMobile.setStatus("mandatory")
_TdmaBcFaxRxPagesFromMobile_Type = Counter32
_TdmaBcFaxRxPagesFromMobile_Object = MibTableColumn
tdmaBcFaxRxPagesFromMobile = _TdmaBcFaxRxPagesFromMobile_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 4, 11, 1, 2),
    _TdmaBcFaxRxPagesFromMobile_Type()
)
tdmaBcFaxRxPagesFromMobile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcFaxRxPagesFromMobile.setStatus("mandatory")
_TdmaBcDce_ObjectIdentity = ObjectIdentity
tdmaBcDce = _TdmaBcDce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 5)
)
_TdmaBcDceRowStatusTable_Object = MibTable
tdmaBcDceRowStatusTable = _TdmaBcDceRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 5, 1)
)
if mibBuilder.loadTexts:
    tdmaBcDceRowStatusTable.setStatus("obsolete")
_TdmaBcDceRowStatusEntry_Object = MibTableRow
tdmaBcDceRowStatusEntry = _TdmaBcDceRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 5, 1, 1)
)
tdmaBcDceRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcDceIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcDceRowStatusEntry.setStatus("obsolete")
_TdmaBcDceRowStatus_Type = RowStatus
_TdmaBcDceRowStatus_Object = MibTableColumn
tdmaBcDceRowStatus = _TdmaBcDceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 5, 1, 1, 1),
    _TdmaBcDceRowStatus_Type()
)
tdmaBcDceRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcDceRowStatus.setStatus("obsolete")
_TdmaBcDceComponentName_Type = DisplayString
_TdmaBcDceComponentName_Object = MibTableColumn
tdmaBcDceComponentName = _TdmaBcDceComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 5, 1, 1, 2),
    _TdmaBcDceComponentName_Type()
)
tdmaBcDceComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcDceComponentName.setStatus("obsolete")
_TdmaBcDceStorageType_Type = StorageType
_TdmaBcDceStorageType_Object = MibTableColumn
tdmaBcDceStorageType = _TdmaBcDceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 5, 1, 1, 4),
    _TdmaBcDceStorageType_Type()
)
tdmaBcDceStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcDceStorageType.setStatus("obsolete")
_TdmaBcDceIndex_Type = NonReplicated
_TdmaBcDceIndex_Object = MibTableColumn
tdmaBcDceIndex = _TdmaBcDceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 5, 1, 1, 10),
    _TdmaBcDceIndex_Type()
)
tdmaBcDceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmaBcDceIndex.setStatus("obsolete")
_TdmaBcDsc_ObjectIdentity = ObjectIdentity
tdmaBcDsc = _TdmaBcDsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 6)
)
_TdmaBcDscRowStatusTable_Object = MibTable
tdmaBcDscRowStatusTable = _TdmaBcDscRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 6, 1)
)
if mibBuilder.loadTexts:
    tdmaBcDscRowStatusTable.setStatus("mandatory")
_TdmaBcDscRowStatusEntry_Object = MibTableRow
tdmaBcDscRowStatusEntry = _TdmaBcDscRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 6, 1, 1)
)
tdmaBcDscRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcDscIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcDscRowStatusEntry.setStatus("mandatory")
_TdmaBcDscRowStatus_Type = RowStatus
_TdmaBcDscRowStatus_Object = MibTableColumn
tdmaBcDscRowStatus = _TdmaBcDscRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 6, 1, 1, 1),
    _TdmaBcDscRowStatus_Type()
)
tdmaBcDscRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcDscRowStatus.setStatus("mandatory")
_TdmaBcDscComponentName_Type = DisplayString
_TdmaBcDscComponentName_Object = MibTableColumn
tdmaBcDscComponentName = _TdmaBcDscComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 6, 1, 1, 2),
    _TdmaBcDscComponentName_Type()
)
tdmaBcDscComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcDscComponentName.setStatus("mandatory")
_TdmaBcDscStorageType_Type = StorageType
_TdmaBcDscStorageType_Object = MibTableColumn
tdmaBcDscStorageType = _TdmaBcDscStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 6, 1, 1, 4),
    _TdmaBcDscStorageType_Type()
)
tdmaBcDscStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcDscStorageType.setStatus("mandatory")
_TdmaBcDscIndex_Type = NonReplicated
_TdmaBcDscIndex_Object = MibTableColumn
tdmaBcDscIndex = _TdmaBcDscIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 6, 1, 1, 10),
    _TdmaBcDscIndex_Type()
)
tdmaBcDscIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmaBcDscIndex.setStatus("mandatory")
_TdmaBcDscOperTable_Object = MibTable
tdmaBcDscOperTable = _TdmaBcDscOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 6, 10)
)
if mibBuilder.loadTexts:
    tdmaBcDscOperTable.setStatus("mandatory")
_TdmaBcDscOperEntry_Object = MibTableRow
tdmaBcDscOperEntry = _TdmaBcDscOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 6, 10, 1)
)
tdmaBcDscOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcDscIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcDscOperEntry.setStatus("mandatory")


class _TdmaBcDscP0CompressionDirection_Type(Integer32):
    """Custom type tdmaBcDscP0CompressionDirection based on Integer32"""
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
        *(("compBoth", 3),
          ("compInitrResp", 1),
          ("compRespInitr", 2),
          ("noCompression", 0))
    )


_TdmaBcDscP0CompressionDirection_Type.__name__ = "Integer32"
_TdmaBcDscP0CompressionDirection_Object = MibTableColumn
tdmaBcDscP0CompressionDirection = _TdmaBcDscP0CompressionDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 6, 10, 1, 1),
    _TdmaBcDscP0CompressionDirection_Type()
)
tdmaBcDscP0CompressionDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcDscP0CompressionDirection.setStatus("mandatory")


class _TdmaBcDscP1CompressionMaximumCodewords_Type(Unsigned32):
    """Custom type tdmaBcDscP1CompressionMaximumCodewords based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 65535),
    )


_TdmaBcDscP1CompressionMaximumCodewords_Type.__name__ = "Unsigned32"
_TdmaBcDscP1CompressionMaximumCodewords_Object = MibTableColumn
tdmaBcDscP1CompressionMaximumCodewords = _TdmaBcDscP1CompressionMaximumCodewords_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 6, 10, 1, 2),
    _TdmaBcDscP1CompressionMaximumCodewords_Type()
)
tdmaBcDscP1CompressionMaximumCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcDscP1CompressionMaximumCodewords.setStatus("mandatory")


class _TdmaBcDscP2CompressionMaximumCharacters_Type(Unsigned32):
    """Custom type tdmaBcDscP2CompressionMaximumCharacters based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 250),
    )


_TdmaBcDscP2CompressionMaximumCharacters_Type.__name__ = "Unsigned32"
_TdmaBcDscP2CompressionMaximumCharacters_Object = MibTableColumn
tdmaBcDscP2CompressionMaximumCharacters = _TdmaBcDscP2CompressionMaximumCharacters_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 6, 10, 1, 3),
    _TdmaBcDscP2CompressionMaximumCharacters_Type()
)
tdmaBcDscP2CompressionMaximumCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcDscP2CompressionMaximumCharacters.setStatus("mandatory")
_TdmaBcDscStatsTable_Object = MibTable
tdmaBcDscStatsTable = _TdmaBcDscStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 6, 11)
)
if mibBuilder.loadTexts:
    tdmaBcDscStatsTable.setStatus("mandatory")
_TdmaBcDscStatsEntry_Object = MibTableRow
tdmaBcDscStatsEntry = _TdmaBcDscStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 6, 11, 1)
)
tdmaBcDscStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcDscIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcDscStatsEntry.setStatus("mandatory")
_TdmaBcDscTxBytes_Type = Counter32
_TdmaBcDscTxBytes_Object = MibTableColumn
tdmaBcDscTxBytes = _TdmaBcDscTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 6, 11, 1, 1),
    _TdmaBcDscTxBytes_Type()
)
tdmaBcDscTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcDscTxBytes.setStatus("mandatory")
_TdmaBcDscRxBytes_Type = Counter32
_TdmaBcDscRxBytes_Object = MibTableColumn
tdmaBcDscRxBytes = _TdmaBcDscRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 6, 11, 1, 2),
    _TdmaBcDscRxBytes_Type()
)
tdmaBcDscRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcDscRxBytes.setStatus("mandatory")
_TdmaBcRlp1_ObjectIdentity = ObjectIdentity
tdmaBcRlp1 = _TdmaBcRlp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 7)
)
_TdmaBcRlp1RowStatusTable_Object = MibTable
tdmaBcRlp1RowStatusTable = _TdmaBcRlp1RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 7, 1)
)
if mibBuilder.loadTexts:
    tdmaBcRlp1RowStatusTable.setStatus("mandatory")
_TdmaBcRlp1RowStatusEntry_Object = MibTableRow
tdmaBcRlp1RowStatusEntry = _TdmaBcRlp1RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 7, 1, 1)
)
tdmaBcRlp1RowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcRlp1Index"),
)
if mibBuilder.loadTexts:
    tdmaBcRlp1RowStatusEntry.setStatus("mandatory")
_TdmaBcRlp1RowStatus_Type = RowStatus
_TdmaBcRlp1RowStatus_Object = MibTableColumn
tdmaBcRlp1RowStatus = _TdmaBcRlp1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 7, 1, 1, 1),
    _TdmaBcRlp1RowStatus_Type()
)
tdmaBcRlp1RowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcRlp1RowStatus.setStatus("mandatory")
_TdmaBcRlp1ComponentName_Type = DisplayString
_TdmaBcRlp1ComponentName_Object = MibTableColumn
tdmaBcRlp1ComponentName = _TdmaBcRlp1ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 7, 1, 1, 2),
    _TdmaBcRlp1ComponentName_Type()
)
tdmaBcRlp1ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcRlp1ComponentName.setStatus("mandatory")
_TdmaBcRlp1StorageType_Type = StorageType
_TdmaBcRlp1StorageType_Object = MibTableColumn
tdmaBcRlp1StorageType = _TdmaBcRlp1StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 7, 1, 1, 4),
    _TdmaBcRlp1StorageType_Type()
)
tdmaBcRlp1StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcRlp1StorageType.setStatus("mandatory")
_TdmaBcRlp1Index_Type = NonReplicated
_TdmaBcRlp1Index_Object = MibTableColumn
tdmaBcRlp1Index = _TdmaBcRlp1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 7, 1, 1, 10),
    _TdmaBcRlp1Index_Type()
)
tdmaBcRlp1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmaBcRlp1Index.setStatus("mandatory")
_TdmaBcRlp1OperTable_Object = MibTable
tdmaBcRlp1OperTable = _TdmaBcRlp1OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 7, 10)
)
if mibBuilder.loadTexts:
    tdmaBcRlp1OperTable.setStatus("mandatory")
_TdmaBcRlp1OperEntry_Object = MibTableRow
tdmaBcRlp1OperEntry = _TdmaBcRlp1OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 7, 10, 1)
)
tdmaBcRlp1OperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcRlp1Index"),
)
if mibBuilder.loadTexts:
    tdmaBcRlp1OperEntry.setStatus("mandatory")


class _TdmaBcRlp1Layer3L0ReqWinSize_Type(Unsigned32):
    """Custom type tdmaBcRlp1Layer3L0ReqWinSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_TdmaBcRlp1Layer3L0ReqWinSize_Type.__name__ = "Unsigned32"
_TdmaBcRlp1Layer3L0ReqWinSize_Object = MibTableColumn
tdmaBcRlp1Layer3L0ReqWinSize = _TdmaBcRlp1Layer3L0ReqWinSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 7, 10, 1, 1),
    _TdmaBcRlp1Layer3L0ReqWinSize_Type()
)
tdmaBcRlp1Layer3L0ReqWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcRlp1Layer3L0ReqWinSize.setStatus("mandatory")


class _TdmaBcRlp1Layer3L1ReqWinSize1_Type(Unsigned32):
    """Custom type tdmaBcRlp1Layer3L1ReqWinSize1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_TdmaBcRlp1Layer3L1ReqWinSize1_Type.__name__ = "Unsigned32"
_TdmaBcRlp1Layer3L1ReqWinSize1_Object = MibTableColumn
tdmaBcRlp1Layer3L1ReqWinSize1 = _TdmaBcRlp1Layer3L1ReqWinSize1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 7, 10, 1, 2),
    _TdmaBcRlp1Layer3L1ReqWinSize1_Type()
)
tdmaBcRlp1Layer3L1ReqWinSize1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcRlp1Layer3L1ReqWinSize1.setStatus("mandatory")


class _TdmaBcRlp1T1ResponseTimer_Type(Unsigned32):
    """Custom type tdmaBcRlp1T1ResponseTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_TdmaBcRlp1T1ResponseTimer_Type.__name__ = "Unsigned32"
_TdmaBcRlp1T1ResponseTimer_Object = MibTableColumn
tdmaBcRlp1T1ResponseTimer = _TdmaBcRlp1T1ResponseTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 7, 10, 1, 3),
    _TdmaBcRlp1T1ResponseTimer_Type()
)
tdmaBcRlp1T1ResponseTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcRlp1T1ResponseTimer.setStatus("mandatory")


class _TdmaBcRlp1T2LinkActivityTimer_Type(Unsigned32):
    """Custom type tdmaBcRlp1T2LinkActivityTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_TdmaBcRlp1T2LinkActivityTimer_Type.__name__ = "Unsigned32"
_TdmaBcRlp1T2LinkActivityTimer_Object = MibTableColumn
tdmaBcRlp1T2LinkActivityTimer = _TdmaBcRlp1T2LinkActivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 7, 10, 1, 4),
    _TdmaBcRlp1T2LinkActivityTimer_Type()
)
tdmaBcRlp1T2LinkActivityTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcRlp1T2LinkActivityTimer.setStatus("mandatory")


class _TdmaBcRlp1T3PeerAckTimer_Type(Unsigned32):
    """Custom type tdmaBcRlp1T3PeerAckTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_TdmaBcRlp1T3PeerAckTimer_Type.__name__ = "Unsigned32"
_TdmaBcRlp1T3PeerAckTimer_Object = MibTableColumn
tdmaBcRlp1T3PeerAckTimer = _TdmaBcRlp1T3PeerAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 7, 10, 1, 5),
    _TdmaBcRlp1T3PeerAckTimer_Type()
)
tdmaBcRlp1T3PeerAckTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcRlp1T3PeerAckTimer.setStatus("mandatory")
_TdmaBcRlp1StatsTable_Object = MibTable
tdmaBcRlp1StatsTable = _TdmaBcRlp1StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 7, 11)
)
if mibBuilder.loadTexts:
    tdmaBcRlp1StatsTable.setStatus("mandatory")
_TdmaBcRlp1StatsEntry_Object = MibTableRow
tdmaBcRlp1StatsEntry = _TdmaBcRlp1StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 7, 11, 1)
)
tdmaBcRlp1StatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcRlp1Index"),
)
if mibBuilder.loadTexts:
    tdmaBcRlp1StatsEntry.setStatus("mandatory")
_TdmaBcRlp1TxFrames_Type = Counter32
_TdmaBcRlp1TxFrames_Object = MibTableColumn
tdmaBcRlp1TxFrames = _TdmaBcRlp1TxFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 7, 11, 1, 1),
    _TdmaBcRlp1TxFrames_Type()
)
tdmaBcRlp1TxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcRlp1TxFrames.setStatus("mandatory")
_TdmaBcRlp1RxFrames_Type = Counter32
_TdmaBcRlp1RxFrames_Object = MibTableColumn
tdmaBcRlp1RxFrames = _TdmaBcRlp1RxFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 7, 11, 1, 2),
    _TdmaBcRlp1RxFrames_Type()
)
tdmaBcRlp1RxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcRlp1RxFrames.setStatus("mandatory")
_TdmaBcRlp1BadRxFrames_Type = Counter32
_TdmaBcRlp1BadRxFrames_Object = MibTableColumn
tdmaBcRlp1BadRxFrames = _TdmaBcRlp1BadRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 7, 11, 1, 3),
    _TdmaBcRlp1BadRxFrames_Type()
)
tdmaBcRlp1BadRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcRlp1BadRxFrames.setStatus("mandatory")
_TdmaBcV42_ObjectIdentity = ObjectIdentity
tdmaBcV42 = _TdmaBcV42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8)
)
_TdmaBcV42RowStatusTable_Object = MibTable
tdmaBcV42RowStatusTable = _TdmaBcV42RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 1)
)
if mibBuilder.loadTexts:
    tdmaBcV42RowStatusTable.setStatus("mandatory")
_TdmaBcV42RowStatusEntry_Object = MibTableRow
tdmaBcV42RowStatusEntry = _TdmaBcV42RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 1, 1)
)
tdmaBcV42RowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcV42Index"),
)
if mibBuilder.loadTexts:
    tdmaBcV42RowStatusEntry.setStatus("mandatory")
_TdmaBcV42RowStatus_Type = RowStatus
_TdmaBcV42RowStatus_Object = MibTableColumn
tdmaBcV42RowStatus = _TdmaBcV42RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 1, 1, 1),
    _TdmaBcV42RowStatus_Type()
)
tdmaBcV42RowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42RowStatus.setStatus("mandatory")
_TdmaBcV42ComponentName_Type = DisplayString
_TdmaBcV42ComponentName_Object = MibTableColumn
tdmaBcV42ComponentName = _TdmaBcV42ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 1, 1, 2),
    _TdmaBcV42ComponentName_Type()
)
tdmaBcV42ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42ComponentName.setStatus("mandatory")
_TdmaBcV42StorageType_Type = StorageType
_TdmaBcV42StorageType_Object = MibTableColumn
tdmaBcV42StorageType = _TdmaBcV42StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 1, 1, 4),
    _TdmaBcV42StorageType_Type()
)
tdmaBcV42StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42StorageType.setStatus("mandatory")
_TdmaBcV42Index_Type = NonReplicated
_TdmaBcV42Index_Object = MibTableColumn
tdmaBcV42Index = _TdmaBcV42Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 1, 1, 10),
    _TdmaBcV42Index_Type()
)
tdmaBcV42Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmaBcV42Index.setStatus("mandatory")
_TdmaBcV42OperTable_Object = MibTable
tdmaBcV42OperTable = _TdmaBcV42OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 10)
)
if mibBuilder.loadTexts:
    tdmaBcV42OperTable.setStatus("mandatory")
_TdmaBcV42OperEntry_Object = MibTableRow
tdmaBcV42OperEntry = _TdmaBcV42OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 10, 1)
)
tdmaBcV42OperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcV42Index"),
)
if mibBuilder.loadTexts:
    tdmaBcV42OperEntry.setStatus("mandatory")


class _TdmaBcV42ProtocolState_Type(Integer32):
    """Custom type tdmaBcV42ProtocolState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disconnectRequest", 4),
          ("disconnected", 1),
          ("frameReject", 3),
          ("informationTransfer", 5),
          ("linkSetup", 2),
          ("notActive", 0),
          ("waitingAck", 6))
    )


_TdmaBcV42ProtocolState_Type.__name__ = "Integer32"
_TdmaBcV42ProtocolState_Object = MibTableColumn
tdmaBcV42ProtocolState = _TdmaBcV42ProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 10, 1, 1),
    _TdmaBcV42ProtocolState_Type()
)
tdmaBcV42ProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42ProtocolState.setStatus("mandatory")


class _TdmaBcV42TxN401FrameSize_Type(Unsigned32):
    """Custom type tdmaBcV42TxN401FrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65355),
    )


_TdmaBcV42TxN401FrameSize_Type.__name__ = "Unsigned32"
_TdmaBcV42TxN401FrameSize_Object = MibTableColumn
tdmaBcV42TxN401FrameSize = _TdmaBcV42TxN401FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 10, 1, 2),
    _TdmaBcV42TxN401FrameSize_Type()
)
tdmaBcV42TxN401FrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42TxN401FrameSize.setStatus("mandatory")


class _TdmaBcV42RxN401FrameSize_Type(Unsigned32):
    """Custom type tdmaBcV42RxN401FrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TdmaBcV42RxN401FrameSize_Type.__name__ = "Unsigned32"
_TdmaBcV42RxN401FrameSize_Object = MibTableColumn
tdmaBcV42RxN401FrameSize = _TdmaBcV42RxN401FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 10, 1, 3),
    _TdmaBcV42RxN401FrameSize_Type()
)
tdmaBcV42RxN401FrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42RxN401FrameSize.setStatus("mandatory")


class _TdmaBcV42TxKWindowSize_Type(Unsigned32):
    """Custom type tdmaBcV42TxKWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TdmaBcV42TxKWindowSize_Type.__name__ = "Unsigned32"
_TdmaBcV42TxKWindowSize_Object = MibTableColumn
tdmaBcV42TxKWindowSize = _TdmaBcV42TxKWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 10, 1, 4),
    _TdmaBcV42TxKWindowSize_Type()
)
tdmaBcV42TxKWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42TxKWindowSize.setStatus("mandatory")


class _TdmaBcV42RxKWindowSize_Type(Unsigned32):
    """Custom type tdmaBcV42RxKWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_TdmaBcV42RxKWindowSize_Type.__name__ = "Unsigned32"
_TdmaBcV42RxKWindowSize_Object = MibTableColumn
tdmaBcV42RxKWindowSize = _TdmaBcV42RxKWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 10, 1, 5),
    _TdmaBcV42RxKWindowSize_Type()
)
tdmaBcV42RxKWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42RxKWindowSize.setStatus("mandatory")


class _TdmaBcV42V42ActiveInCall_Type(Integer32):
    """Custom type tdmaBcV42V42ActiveInCall based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activeInCall", 1),
          ("notActiveInCall", 0))
    )


_TdmaBcV42V42ActiveInCall_Type.__name__ = "Integer32"
_TdmaBcV42V42ActiveInCall_Object = MibTableColumn
tdmaBcV42V42ActiveInCall = _TdmaBcV42V42ActiveInCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 10, 1, 6),
    _TdmaBcV42V42ActiveInCall_Type()
)
tdmaBcV42V42ActiveInCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42V42ActiveInCall.setStatus("mandatory")


class _TdmaBcV42V42BisActiveInCall_Type(Integer32):
    """Custom type tdmaBcV42V42BisActiveInCall based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activeInCall", 1),
          ("notActiveInCall", 0))
    )


_TdmaBcV42V42BisActiveInCall_Type.__name__ = "Integer32"
_TdmaBcV42V42BisActiveInCall_Object = MibTableColumn
tdmaBcV42V42BisActiveInCall = _TdmaBcV42V42BisActiveInCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 10, 1, 7),
    _TdmaBcV42V42BisActiveInCall_Type()
)
tdmaBcV42V42BisActiveInCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42V42BisActiveInCall.setStatus("mandatory")
_TdmaBcV42StatsTable_Object = MibTable
tdmaBcV42StatsTable = _TdmaBcV42StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 11)
)
if mibBuilder.loadTexts:
    tdmaBcV42StatsTable.setStatus("mandatory")
_TdmaBcV42StatsEntry_Object = MibTableRow
tdmaBcV42StatsEntry = _TdmaBcV42StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 11, 1)
)
tdmaBcV42StatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcV42Index"),
)
if mibBuilder.loadTexts:
    tdmaBcV42StatsEntry.setStatus("mandatory")
_TdmaBcV42RxIBytes_Type = Counter32
_TdmaBcV42RxIBytes_Object = MibTableColumn
tdmaBcV42RxIBytes = _TdmaBcV42RxIBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 11, 1, 1),
    _TdmaBcV42RxIBytes_Type()
)
tdmaBcV42RxIBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42RxIBytes.setStatus("mandatory")
_TdmaBcV42TxIBytes_Type = Counter32
_TdmaBcV42TxIBytes_Object = MibTableColumn
tdmaBcV42TxIBytes = _TdmaBcV42TxIBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 11, 1, 2),
    _TdmaBcV42TxIBytes_Type()
)
tdmaBcV42TxIBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42TxIBytes.setStatus("mandatory")
_TdmaBcV42RxIFrames_Type = Counter32
_TdmaBcV42RxIFrames_Object = MibTableColumn
tdmaBcV42RxIFrames = _TdmaBcV42RxIFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 11, 1, 3),
    _TdmaBcV42RxIFrames_Type()
)
tdmaBcV42RxIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42RxIFrames.setStatus("mandatory")
_TdmaBcV42TxIFrames_Type = Counter32
_TdmaBcV42TxIFrames_Object = MibTableColumn
tdmaBcV42TxIFrames = _TdmaBcV42TxIFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 11, 1, 4),
    _TdmaBcV42TxIFrames_Type()
)
tdmaBcV42TxIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42TxIFrames.setStatus("mandatory")
_TdmaBcV42RetransmittedFrames_Type = Counter32
_TdmaBcV42RetransmittedFrames_Object = MibTableColumn
tdmaBcV42RetransmittedFrames = _TdmaBcV42RetransmittedFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 11, 1, 5),
    _TdmaBcV42RetransmittedFrames_Type()
)
tdmaBcV42RetransmittedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42RetransmittedFrames.setStatus("mandatory")
_TdmaBcV42T1AckTimeouts_Type = Counter32
_TdmaBcV42T1AckTimeouts_Object = MibTableColumn
tdmaBcV42T1AckTimeouts = _TdmaBcV42T1AckTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 11, 1, 6),
    _TdmaBcV42T1AckTimeouts_Type()
)
tdmaBcV42T1AckTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42T1AckTimeouts.setStatus("mandatory")
_TdmaBcV42RemoteBusyIndications_Type = Counter32
_TdmaBcV42RemoteBusyIndications_Object = MibTableColumn
tdmaBcV42RemoteBusyIndications = _TdmaBcV42RemoteBusyIndications_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 11, 1, 7),
    _TdmaBcV42RemoteBusyIndications_Type()
)
tdmaBcV42RemoteBusyIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42RemoteBusyIndications.setStatus("mandatory")
_TdmaBcV42LocalBusyIndications_Type = Counter32
_TdmaBcV42LocalBusyIndications_Object = MibTableColumn
tdmaBcV42LocalBusyIndications = _TdmaBcV42LocalBusyIndications_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 11, 1, 8),
    _TdmaBcV42LocalBusyIndications_Type()
)
tdmaBcV42LocalBusyIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42LocalBusyIndications.setStatus("mandatory")
_TdmaBcV42BadFramesRx_Type = Counter32
_TdmaBcV42BadFramesRx_Object = MibTableColumn
tdmaBcV42BadFramesRx = _TdmaBcV42BadFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 11, 1, 9),
    _TdmaBcV42BadFramesRx_Type()
)
tdmaBcV42BadFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42BadFramesRx.setStatus("mandatory")
_TdmaBcV42CrcErrorsRx_Type = Counter32
_TdmaBcV42CrcErrorsRx_Object = MibTableColumn
tdmaBcV42CrcErrorsRx = _TdmaBcV42CrcErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 8, 11, 1, 10),
    _TdmaBcV42CrcErrorsRx_Type()
)
tdmaBcV42CrcErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42CrcErrorsRx.setStatus("mandatory")
_TdmaBcV42Bis_ObjectIdentity = ObjectIdentity
tdmaBcV42Bis = _TdmaBcV42Bis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9)
)
_TdmaBcV42BisRowStatusTable_Object = MibTable
tdmaBcV42BisRowStatusTable = _TdmaBcV42BisRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9, 1)
)
if mibBuilder.loadTexts:
    tdmaBcV42BisRowStatusTable.setStatus("mandatory")
_TdmaBcV42BisRowStatusEntry_Object = MibTableRow
tdmaBcV42BisRowStatusEntry = _TdmaBcV42BisRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9, 1, 1)
)
tdmaBcV42BisRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcV42BisIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcV42BisRowStatusEntry.setStatus("mandatory")
_TdmaBcV42BisRowStatus_Type = RowStatus
_TdmaBcV42BisRowStatus_Object = MibTableColumn
tdmaBcV42BisRowStatus = _TdmaBcV42BisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9, 1, 1, 1),
    _TdmaBcV42BisRowStatus_Type()
)
tdmaBcV42BisRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42BisRowStatus.setStatus("mandatory")
_TdmaBcV42BisComponentName_Type = DisplayString
_TdmaBcV42BisComponentName_Object = MibTableColumn
tdmaBcV42BisComponentName = _TdmaBcV42BisComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9, 1, 1, 2),
    _TdmaBcV42BisComponentName_Type()
)
tdmaBcV42BisComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42BisComponentName.setStatus("mandatory")
_TdmaBcV42BisStorageType_Type = StorageType
_TdmaBcV42BisStorageType_Object = MibTableColumn
tdmaBcV42BisStorageType = _TdmaBcV42BisStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9, 1, 1, 4),
    _TdmaBcV42BisStorageType_Type()
)
tdmaBcV42BisStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42BisStorageType.setStatus("mandatory")
_TdmaBcV42BisIndex_Type = NonReplicated
_TdmaBcV42BisIndex_Object = MibTableColumn
tdmaBcV42BisIndex = _TdmaBcV42BisIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9, 1, 1, 10),
    _TdmaBcV42BisIndex_Type()
)
tdmaBcV42BisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmaBcV42BisIndex.setStatus("mandatory")
_TdmaBcV42BisOperTable_Object = MibTable
tdmaBcV42BisOperTable = _TdmaBcV42BisOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9, 10)
)
if mibBuilder.loadTexts:
    tdmaBcV42BisOperTable.setStatus("mandatory")
_TdmaBcV42BisOperEntry_Object = MibTableRow
tdmaBcV42BisOperEntry = _TdmaBcV42BisOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9, 10, 1)
)
tdmaBcV42BisOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcV42BisIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcV42BisOperEntry.setStatus("mandatory")


class _TdmaBcV42BisProtocolModeEncoder_Type(Integer32):
    """Custom type tdmaBcV42BisProtocolModeEncoder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("compressed", 1),
          ("transparent", 0))
    )


_TdmaBcV42BisProtocolModeEncoder_Type.__name__ = "Integer32"
_TdmaBcV42BisProtocolModeEncoder_Object = MibTableColumn
tdmaBcV42BisProtocolModeEncoder = _TdmaBcV42BisProtocolModeEncoder_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9, 10, 1, 1),
    _TdmaBcV42BisProtocolModeEncoder_Type()
)
tdmaBcV42BisProtocolModeEncoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42BisProtocolModeEncoder.setStatus("mandatory")


class _TdmaBcV42BisProtocolModeDecoder_Type(Integer32):
    """Custom type tdmaBcV42BisProtocolModeDecoder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("compressed", 1),
          ("transparent", 0))
    )


_TdmaBcV42BisProtocolModeDecoder_Type.__name__ = "Integer32"
_TdmaBcV42BisProtocolModeDecoder_Object = MibTableColumn
tdmaBcV42BisProtocolModeDecoder = _TdmaBcV42BisProtocolModeDecoder_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9, 10, 1, 2),
    _TdmaBcV42BisProtocolModeDecoder_Type()
)
tdmaBcV42BisProtocolModeDecoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42BisProtocolModeDecoder.setStatus("mandatory")


class _TdmaBcV42BisP0CompressionDirection_Type(Integer32):
    """Custom type tdmaBcV42BisP0CompressionDirection based on Integer32"""
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
        *(("compBoth", 3),
          ("compInitrResp", 1),
          ("compRespInitr", 2),
          ("noCompression", 0))
    )


_TdmaBcV42BisP0CompressionDirection_Type.__name__ = "Integer32"
_TdmaBcV42BisP0CompressionDirection_Object = MibTableColumn
tdmaBcV42BisP0CompressionDirection = _TdmaBcV42BisP0CompressionDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9, 10, 1, 3),
    _TdmaBcV42BisP0CompressionDirection_Type()
)
tdmaBcV42BisP0CompressionDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42BisP0CompressionDirection.setStatus("mandatory")


class _TdmaBcV42BisP1MaximumCodewords_Type(Unsigned32):
    """Custom type tdmaBcV42BisP1MaximumCodewords based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TdmaBcV42BisP1MaximumCodewords_Type.__name__ = "Unsigned32"
_TdmaBcV42BisP1MaximumCodewords_Object = MibTableColumn
tdmaBcV42BisP1MaximumCodewords = _TdmaBcV42BisP1MaximumCodewords_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9, 10, 1, 4),
    _TdmaBcV42BisP1MaximumCodewords_Type()
)
tdmaBcV42BisP1MaximumCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42BisP1MaximumCodewords.setStatus("mandatory")


class _TdmaBcV42BisP2MaximumStringSize_Type(Unsigned32):
    """Custom type tdmaBcV42BisP2MaximumStringSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 250),
    )


_TdmaBcV42BisP2MaximumStringSize_Type.__name__ = "Unsigned32"
_TdmaBcV42BisP2MaximumStringSize_Object = MibTableColumn
tdmaBcV42BisP2MaximumStringSize = _TdmaBcV42BisP2MaximumStringSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9, 10, 1, 5),
    _TdmaBcV42BisP2MaximumStringSize_Type()
)
tdmaBcV42BisP2MaximumStringSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42BisP2MaximumStringSize.setStatus("mandatory")


class _TdmaBcV42BisLastDecodeError_Type(Integer32):
    """Custom type tdmaBcV42BisLastDecodeError based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("badStepup", 1),
          ("codewordEqC1", 2),
          ("emptyCodeword", 3),
          ("generalError", 5),
          ("none", 0),
          ("rsvdCommand", 4))
    )


_TdmaBcV42BisLastDecodeError_Type.__name__ = "Integer32"
_TdmaBcV42BisLastDecodeError_Object = MibTableColumn
tdmaBcV42BisLastDecodeError = _TdmaBcV42BisLastDecodeError_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9, 10, 1, 6),
    _TdmaBcV42BisLastDecodeError_Type()
)
tdmaBcV42BisLastDecodeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42BisLastDecodeError.setStatus("mandatory")


class _TdmaBcV42BisCompRatioEncoder_Type(FixedPoint2):
    """Custom type tdmaBcV42BisCompRatioEncoder based on FixedPoint2"""
    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_TdmaBcV42BisCompRatioEncoder_Type.__name__ = "FixedPoint2"
_TdmaBcV42BisCompRatioEncoder_Object = MibTableColumn
tdmaBcV42BisCompRatioEncoder = _TdmaBcV42BisCompRatioEncoder_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9, 10, 1, 7),
    _TdmaBcV42BisCompRatioEncoder_Type()
)
tdmaBcV42BisCompRatioEncoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42BisCompRatioEncoder.setStatus("mandatory")


class _TdmaBcV42BisCompRatioDecoder_Type(FixedPoint2):
    """Custom type tdmaBcV42BisCompRatioDecoder based on FixedPoint2"""
    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_TdmaBcV42BisCompRatioDecoder_Type.__name__ = "FixedPoint2"
_TdmaBcV42BisCompRatioDecoder_Object = MibTableColumn
tdmaBcV42BisCompRatioDecoder = _TdmaBcV42BisCompRatioDecoder_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9, 10, 1, 8),
    _TdmaBcV42BisCompRatioDecoder_Type()
)
tdmaBcV42BisCompRatioDecoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42BisCompRatioDecoder.setStatus("mandatory")
_TdmaBcV42BisStatsTable_Object = MibTable
tdmaBcV42BisStatsTable = _TdmaBcV42BisStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9, 11)
)
if mibBuilder.loadTexts:
    tdmaBcV42BisStatsTable.setStatus("mandatory")
_TdmaBcV42BisStatsEntry_Object = MibTableRow
tdmaBcV42BisStatsEntry = _TdmaBcV42BisStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9, 11, 1)
)
tdmaBcV42BisStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcV42BisIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcV42BisStatsEntry.setStatus("mandatory")
_TdmaBcV42BisModeChangesEncode_Type = Counter32
_TdmaBcV42BisModeChangesEncode_Object = MibTableColumn
tdmaBcV42BisModeChangesEncode = _TdmaBcV42BisModeChangesEncode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9, 11, 1, 1),
    _TdmaBcV42BisModeChangesEncode_Type()
)
tdmaBcV42BisModeChangesEncode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42BisModeChangesEncode.setStatus("mandatory")
_TdmaBcV42BisModeChangesDecode_Type = Counter32
_TdmaBcV42BisModeChangesDecode_Object = MibTableColumn
tdmaBcV42BisModeChangesDecode = _TdmaBcV42BisModeChangesDecode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9, 11, 1, 2),
    _TdmaBcV42BisModeChangesDecode_Type()
)
tdmaBcV42BisModeChangesDecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42BisModeChangesDecode.setStatus("mandatory")
_TdmaBcV42BisResetsEncode_Type = Counter32
_TdmaBcV42BisResetsEncode_Object = MibTableColumn
tdmaBcV42BisResetsEncode = _TdmaBcV42BisResetsEncode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9, 11, 1, 3),
    _TdmaBcV42BisResetsEncode_Type()
)
tdmaBcV42BisResetsEncode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42BisResetsEncode.setStatus("mandatory")
_TdmaBcV42BisResetsDecode_Type = Counter32
_TdmaBcV42BisResetsDecode_Object = MibTableColumn
tdmaBcV42BisResetsDecode = _TdmaBcV42BisResetsDecode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9, 11, 1, 4),
    _TdmaBcV42BisResetsDecode_Type()
)
tdmaBcV42BisResetsDecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42BisResetsDecode.setStatus("mandatory")
_TdmaBcV42BisReinitializations_Type = Counter32
_TdmaBcV42BisReinitializations_Object = MibTableColumn
tdmaBcV42BisReinitializations = _TdmaBcV42BisReinitializations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9, 11, 1, 5),
    _TdmaBcV42BisReinitializations_Type()
)
tdmaBcV42BisReinitializations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42BisReinitializations.setStatus("mandatory")
_TdmaBcV42BisErrorsInDecode_Type = Counter32
_TdmaBcV42BisErrorsInDecode_Object = MibTableColumn
tdmaBcV42BisErrorsInDecode = _TdmaBcV42BisErrorsInDecode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 9, 11, 1, 6),
    _TdmaBcV42BisErrorsInDecode_Type()
)
tdmaBcV42BisErrorsInDecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcV42BisErrorsInDecode.setStatus("mandatory")
_TdmaBcUr_ObjectIdentity = ObjectIdentity
tdmaBcUr = _TdmaBcUr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 10)
)
_TdmaBcUrRowStatusTable_Object = MibTable
tdmaBcUrRowStatusTable = _TdmaBcUrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 10, 1)
)
if mibBuilder.loadTexts:
    tdmaBcUrRowStatusTable.setStatus("mandatory")
_TdmaBcUrRowStatusEntry_Object = MibTableRow
tdmaBcUrRowStatusEntry = _TdmaBcUrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 10, 1, 1)
)
tdmaBcUrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcUrIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcUrRowStatusEntry.setStatus("mandatory")
_TdmaBcUrRowStatus_Type = RowStatus
_TdmaBcUrRowStatus_Object = MibTableColumn
tdmaBcUrRowStatus = _TdmaBcUrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 10, 1, 1, 1),
    _TdmaBcUrRowStatus_Type()
)
tdmaBcUrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcUrRowStatus.setStatus("mandatory")
_TdmaBcUrComponentName_Type = DisplayString
_TdmaBcUrComponentName_Object = MibTableColumn
tdmaBcUrComponentName = _TdmaBcUrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 10, 1, 1, 2),
    _TdmaBcUrComponentName_Type()
)
tdmaBcUrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcUrComponentName.setStatus("mandatory")
_TdmaBcUrStorageType_Type = StorageType
_TdmaBcUrStorageType_Object = MibTableColumn
tdmaBcUrStorageType = _TdmaBcUrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 10, 1, 1, 4),
    _TdmaBcUrStorageType_Type()
)
tdmaBcUrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcUrStorageType.setStatus("mandatory")
_TdmaBcUrIndex_Type = NonReplicated
_TdmaBcUrIndex_Object = MibTableColumn
tdmaBcUrIndex = _TdmaBcUrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 10, 1, 1, 10),
    _TdmaBcUrIndex_Type()
)
tdmaBcUrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmaBcUrIndex.setStatus("mandatory")
_TdmaBcUrOperTable_Object = MibTable
tdmaBcUrOperTable = _TdmaBcUrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 10, 10)
)
if mibBuilder.loadTexts:
    tdmaBcUrOperTable.setStatus("mandatory")
_TdmaBcUrOperEntry_Object = MibTableRow
tdmaBcUrOperEntry = _TdmaBcUrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 10, 10, 1)
)
tdmaBcUrOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcUrIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcUrOperEntry.setStatus("mandatory")


class _TdmaBcUrRxBufferSize_Type(Unsigned32):
    """Custom type tdmaBcUrRxBufferSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TdmaBcUrRxBufferSize_Type.__name__ = "Unsigned32"
_TdmaBcUrRxBufferSize_Object = MibTableColumn
tdmaBcUrRxBufferSize = _TdmaBcUrRxBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 10, 10, 1, 1),
    _TdmaBcUrRxBufferSize_Type()
)
tdmaBcUrRxBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcUrRxBufferSize.setStatus("mandatory")


class _TdmaBcUrTxFlowControlState_Type(Integer32):
    """Custom type tdmaBcUrTxFlowControlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("inactive", 1))
    )


_TdmaBcUrTxFlowControlState_Type.__name__ = "Integer32"
_TdmaBcUrTxFlowControlState_Object = MibTableColumn
tdmaBcUrTxFlowControlState = _TdmaBcUrTxFlowControlState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 10, 10, 1, 2),
    _TdmaBcUrTxFlowControlState_Type()
)
tdmaBcUrTxFlowControlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcUrTxFlowControlState.setStatus("mandatory")


class _TdmaBcUrRxFlowControlState_Type(Integer32):
    """Custom type tdmaBcUrRxFlowControlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("inactive", 1))
    )


_TdmaBcUrRxFlowControlState_Type.__name__ = "Integer32"
_TdmaBcUrRxFlowControlState_Object = MibTableColumn
tdmaBcUrRxFlowControlState = _TdmaBcUrRxFlowControlState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 10, 10, 1, 3),
    _TdmaBcUrRxFlowControlState_Type()
)
tdmaBcUrRxFlowControlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcUrRxFlowControlState.setStatus("mandatory")
_TdmaBcUrStatsTable_Object = MibTable
tdmaBcUrStatsTable = _TdmaBcUrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 10, 11)
)
if mibBuilder.loadTexts:
    tdmaBcUrStatsTable.setStatus("mandatory")
_TdmaBcUrStatsEntry_Object = MibTableRow
tdmaBcUrStatsEntry = _TdmaBcUrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 10, 11, 1)
)
tdmaBcUrStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcUrIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcUrStatsEntry.setStatus("mandatory")
_TdmaBcUrTxFrames_Type = Counter32
_TdmaBcUrTxFrames_Object = MibTableColumn
tdmaBcUrTxFrames = _TdmaBcUrTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 10, 11, 1, 1),
    _TdmaBcUrTxFrames_Type()
)
tdmaBcUrTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcUrTxFrames.setStatus("mandatory")
_TdmaBcUrRxFrames_Type = Counter32
_TdmaBcUrRxFrames_Object = MibTableColumn
tdmaBcUrRxFrames = _TdmaBcUrRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 10, 11, 1, 2),
    _TdmaBcUrRxFrames_Type()
)
tdmaBcUrRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcUrRxFrames.setStatus("mandatory")
_TdmaBcUrUnacknowledgedFrames_Type = Counter32
_TdmaBcUrUnacknowledgedFrames_Object = MibTableColumn
tdmaBcUrUnacknowledgedFrames = _TdmaBcUrUnacknowledgedFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 10, 11, 1, 3),
    _TdmaBcUrUnacknowledgedFrames_Type()
)
tdmaBcUrUnacknowledgedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcUrUnacknowledgedFrames.setStatus("mandatory")
_TdmaBcUrCumUnacknowledgedFrames_Type = Counter32
_TdmaBcUrCumUnacknowledgedFrames_Object = MibTableColumn
tdmaBcUrCumUnacknowledgedFrames = _TdmaBcUrCumUnacknowledgedFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 10, 11, 1, 4),
    _TdmaBcUrCumUnacknowledgedFrames_Type()
)
tdmaBcUrCumUnacknowledgedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcUrCumUnacknowledgedFrames.setStatus("mandatory")
_TdmaBcOperTable_Object = MibTable
tdmaBcOperTable = _TdmaBcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 101)
)
if mibBuilder.loadTexts:
    tdmaBcOperTable.setStatus("mandatory")
_TdmaBcOperEntry_Object = MibTableRow
tdmaBcOperEntry = _TdmaBcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 101, 1)
)
tdmaBcOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcOperEntry.setStatus("mandatory")


class _TdmaBcState_Type(Integer32):
    """Custom type tdmaBcState based on Integer32"""
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
        *(("active", 2),
          ("idle", 0),
          ("release", 3),
          ("setup", 1))
    )


_TdmaBcState_Type.__name__ = "Integer32"
_TdmaBcState_Object = MibTableColumn
tdmaBcState = _TdmaBcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 101, 1, 1),
    _TdmaBcState_Type()
)
tdmaBcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcState.setStatus("mandatory")


class _TdmaBcCallType_Type(Integer32):
    """Custom type tdmaBcCallType based on Integer32"""
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
        *(("analogPrefSpeech", 2),
          ("analogSpeech", 0),
          ("asyncData", 4),
          ("digitalPrefSpeech", 3),
          ("digitalSpeech", 1),
          ("g3Fax", 5),
          ("notUsedYet", 8),
          ("rejected", 6),
          ("stuIII", 7))
    )


_TdmaBcCallType_Type.__name__ = "Integer32"
_TdmaBcCallType_Object = MibTableColumn
tdmaBcCallType = _TdmaBcCallType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 101, 1, 2),
    _TdmaBcCallType_Type()
)
tdmaBcCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcCallType.setStatus("mandatory")


class _TdmaBcLastResponseCode_Type(Integer32):
    """Custom type tdmaBcLastResponseCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              129,
              131,
              144,
              145,
              146,
              147,
              156,
              159,
              169,
              172,
              175,
              177,
              191,
              207,
              209,
              210,
              223,
              224,
              225,
              226,
              230,
              239)
        )
    )
    namedValues = NamedValues(
        *(("channelUnavailable", 172),
          ("incompatibleMessage", 226),
          ("invalidCallRefValue", 209),
          ("invalidChannel", 210),
          ("invalidMessageType", 225),
          ("invalidNumberFormat", 156),
          ("missingMandatoryIe", 224),
          ("noCause", 0),
          ("noResponse", 146),
          ("noRouteToDest", 131),
          ("normalClearing", 144),
          ("qosUnavailable", 177),
          ("resourceUnavailable", 175),
          ("serviceUnavailable", 191),
          ("temporaryFailure", 169),
          ("timerRecovery", 230),
          ("unassignedNumber", 129),
          ("unimplementedOption", 207),
          ("unspecInvalidMessage", 223),
          ("unspecNormal", 159),
          ("unspecProtocolError", 239),
          ("userBusy", 145),
          ("userNoAnswer", 147))
    )


_TdmaBcLastResponseCode_Type.__name__ = "Integer32"
_TdmaBcLastResponseCode_Object = MibTableColumn
tdmaBcLastResponseCode = _TdmaBcLastResponseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 101, 1, 3),
    _TdmaBcLastResponseCode_Type()
)
tdmaBcLastResponseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcLastResponseCode.setStatus("mandatory")
_TdmaBcMateBearerChannel_Type = RowPointer
_TdmaBcMateBearerChannel_Object = MibTableColumn
tdmaBcMateBearerChannel = _TdmaBcMateBearerChannel_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 101, 1, 4),
    _TdmaBcMateBearerChannel_Type()
)
tdmaBcMateBearerChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcMateBearerChannel.setStatus("mandatory")
_TdmaBcCidDataTable_Object = MibTable
tdmaBcCidDataTable = _TdmaBcCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 103)
)
if mibBuilder.loadTexts:
    tdmaBcCidDataTable.setStatus("mandatory")
_TdmaBcCidDataEntry_Object = MibTableRow
tdmaBcCidDataEntry = _TdmaBcCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 103, 1)
)
tdmaBcCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcCidDataEntry.setStatus("mandatory")


class _TdmaBcCustomerIdentifier_Type(Unsigned32):
    """Custom type tdmaBcCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_TdmaBcCustomerIdentifier_Type.__name__ = "Unsigned32"
_TdmaBcCustomerIdentifier_Object = MibTableColumn
tdmaBcCustomerIdentifier = _TdmaBcCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 103, 1, 1),
    _TdmaBcCustomerIdentifier_Type()
)
tdmaBcCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmaBcCustomerIdentifier.setStatus("mandatory")
_TdmaBcStateTable_Object = MibTable
tdmaBcStateTable = _TdmaBcStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 104)
)
if mibBuilder.loadTexts:
    tdmaBcStateTable.setStatus("mandatory")
_TdmaBcStateEntry_Object = MibTableRow
tdmaBcStateEntry = _TdmaBcStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 104, 1)
)
tdmaBcStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcCsIndex"),
    (0, "Nortel-Magellan-Passport-TdmaIwfMIB", "tdmaBcBcIndex"),
)
if mibBuilder.loadTexts:
    tdmaBcStateEntry.setStatus("mandatory")


class _TdmaBcAdminState_Type(Integer32):
    """Custom type tdmaBcAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_TdmaBcAdminState_Type.__name__ = "Integer32"
_TdmaBcAdminState_Object = MibTableColumn
tdmaBcAdminState = _TdmaBcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 104, 1, 1),
    _TdmaBcAdminState_Type()
)
tdmaBcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcAdminState.setStatus("mandatory")


class _TdmaBcOperationalState_Type(Integer32):
    """Custom type tdmaBcOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TdmaBcOperationalState_Type.__name__ = "Integer32"
_TdmaBcOperationalState_Object = MibTableColumn
tdmaBcOperationalState = _TdmaBcOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 104, 1, 2),
    _TdmaBcOperationalState_Type()
)
tdmaBcOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcOperationalState.setStatus("mandatory")


class _TdmaBcUsageState_Type(Integer32):
    """Custom type tdmaBcUsageState based on Integer32"""
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
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_TdmaBcUsageState_Type.__name__ = "Integer32"
_TdmaBcUsageState_Object = MibTableColumn
tdmaBcUsageState = _TdmaBcUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 136, 104, 1, 3),
    _TdmaBcUsageState_Type()
)
tdmaBcUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaBcUsageState.setStatus("mandatory")
_TdmaIwfMIB_ObjectIdentity = ObjectIdentity
tdmaIwfMIB = _TdmaIwfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 140)
)
_TdmaIwfGroup_ObjectIdentity = ObjectIdentity
tdmaIwfGroup = _TdmaIwfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 140, 1)
)
_TdmaIwfGroupBE_ObjectIdentity = ObjectIdentity
tdmaIwfGroupBE = _TdmaIwfGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 140, 1, 5)
)
_TdmaIwfGroupBE01_ObjectIdentity = ObjectIdentity
tdmaIwfGroupBE01 = _TdmaIwfGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 140, 1, 5, 2)
)
_TdmaIwfGroupBE01A_ObjectIdentity = ObjectIdentity
tdmaIwfGroupBE01A = _TdmaIwfGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 140, 1, 5, 2, 2)
)
_TdmaIwfCapabilities_ObjectIdentity = ObjectIdentity
tdmaIwfCapabilities = _TdmaIwfCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 140, 3)
)
_TdmaIwfCapabilitiesBE_ObjectIdentity = ObjectIdentity
tdmaIwfCapabilitiesBE = _TdmaIwfCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 140, 3, 5)
)
_TdmaIwfCapabilitiesBE01_ObjectIdentity = ObjectIdentity
tdmaIwfCapabilitiesBE01 = _TdmaIwfCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 140, 3, 5, 2)
)
_TdmaIwfCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
tdmaIwfCapabilitiesBE01A = _TdmaIwfCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 140, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-TdmaIwfMIB",
    **{"tdmaCs": tdmaCs,
       "tdmaCsRowStatusTable": tdmaCsRowStatusTable,
       "tdmaCsRowStatusEntry": tdmaCsRowStatusEntry,
       "tdmaCsRowStatus": tdmaCsRowStatus,
       "tdmaCsComponentName": tdmaCsComponentName,
       "tdmaCsStorageType": tdmaCsStorageType,
       "tdmaCsCsIndex": tdmaCsCsIndex,
       "tdmaCsModem": tdmaCsModem,
       "tdmaCsModemRowStatusTable": tdmaCsModemRowStatusTable,
       "tdmaCsModemRowStatusEntry": tdmaCsModemRowStatusEntry,
       "tdmaCsModemRowStatus": tdmaCsModemRowStatus,
       "tdmaCsModemComponentName": tdmaCsModemComponentName,
       "tdmaCsModemStorageType": tdmaCsModemStorageType,
       "tdmaCsModemIndex": tdmaCsModemIndex,
       "tdmaCsFax": tdmaCsFax,
       "tdmaCsFaxRowStatusTable": tdmaCsFaxRowStatusTable,
       "tdmaCsFaxRowStatusEntry": tdmaCsFaxRowStatusEntry,
       "tdmaCsFaxRowStatus": tdmaCsFaxRowStatus,
       "tdmaCsFaxComponentName": tdmaCsFaxComponentName,
       "tdmaCsFaxStorageType": tdmaCsFaxStorageType,
       "tdmaCsFaxIndex": tdmaCsFaxIndex,
       "tdmaCsDce": tdmaCsDce,
       "tdmaCsDceRowStatusTable": tdmaCsDceRowStatusTable,
       "tdmaCsDceRowStatusEntry": tdmaCsDceRowStatusEntry,
       "tdmaCsDceRowStatus": tdmaCsDceRowStatus,
       "tdmaCsDceComponentName": tdmaCsDceComponentName,
       "tdmaCsDceStorageType": tdmaCsDceStorageType,
       "tdmaCsDceIndex": tdmaCsDceIndex,
       "tdmaCsDsc": tdmaCsDsc,
       "tdmaCsDscRowStatusTable": tdmaCsDscRowStatusTable,
       "tdmaCsDscRowStatusEntry": tdmaCsDscRowStatusEntry,
       "tdmaCsDscRowStatus": tdmaCsDscRowStatus,
       "tdmaCsDscComponentName": tdmaCsDscComponentName,
       "tdmaCsDscStorageType": tdmaCsDscStorageType,
       "tdmaCsDscIndex": tdmaCsDscIndex,
       "tdmaCsDscProvTable": tdmaCsDscProvTable,
       "tdmaCsDscProvEntry": tdmaCsDscProvEntry,
       "tdmaCsDscLl0BufferSize": tdmaCsDscLl0BufferSize,
       "tdmaCsDscLl1BufferSize": tdmaCsDscLl1BufferSize,
       "tdmaCsDscK0Ll0WindowSize": tdmaCsDscK0Ll0WindowSize,
       "tdmaCsDscK1Ll1WindowSize": tdmaCsDscK1Ll1WindowSize,
       "tdmaCsDscP0CompressionDirection": tdmaCsDscP0CompressionDirection,
       "tdmaCsDscP1CompressionMaximumCodewords": tdmaCsDscP1CompressionMaximumCodewords,
       "tdmaCsDscP2CompressionMaximumCharacters": tdmaCsDscP2CompressionMaximumCharacters,
       "tdmaCsRlp1": tdmaCsRlp1,
       "tdmaCsRlp1RowStatusTable": tdmaCsRlp1RowStatusTable,
       "tdmaCsRlp1RowStatusEntry": tdmaCsRlp1RowStatusEntry,
       "tdmaCsRlp1RowStatus": tdmaCsRlp1RowStatus,
       "tdmaCsRlp1ComponentName": tdmaCsRlp1ComponentName,
       "tdmaCsRlp1StorageType": tdmaCsRlp1StorageType,
       "tdmaCsRlp1Index": tdmaCsRlp1Index,
       "tdmaCsRlp1ProvTable": tdmaCsRlp1ProvTable,
       "tdmaCsRlp1ProvEntry": tdmaCsRlp1ProvEntry,
       "tdmaCsRlp1T1ResponseTimer": tdmaCsRlp1T1ResponseTimer,
       "tdmaCsRlp1T2LinkActivityTimer": tdmaCsRlp1T2LinkActivityTimer,
       "tdmaCsRlp1T3PeerAckTimer": tdmaCsRlp1T3PeerAckTimer,
       "tdmaCsV42": tdmaCsV42,
       "tdmaCsV42RowStatusTable": tdmaCsV42RowStatusTable,
       "tdmaCsV42RowStatusEntry": tdmaCsV42RowStatusEntry,
       "tdmaCsV42RowStatus": tdmaCsV42RowStatus,
       "tdmaCsV42ComponentName": tdmaCsV42ComponentName,
       "tdmaCsV42StorageType": tdmaCsV42StorageType,
       "tdmaCsV42Index": tdmaCsV42Index,
       "tdmaCsV42ProvTable": tdmaCsV42ProvTable,
       "tdmaCsV42ProvEntry": tdmaCsV42ProvEntry,
       "tdmaCsV42T400DetectTimer": tdmaCsV42T400DetectTimer,
       "tdmaCsV42T401AckTimer": tdmaCsV42T401AckTimer,
       "tdmaCsV42T402AckDelayTimer": tdmaCsV42T402AckDelayTimer,
       "tdmaCsV42T403IdleProbeTimer": tdmaCsV42T403IdleProbeTimer,
       "tdmaCsV42TxN401FrameSize": tdmaCsV42TxN401FrameSize,
       "tdmaCsV42RxN401FrameSize": tdmaCsV42RxN401FrameSize,
       "tdmaCsV42TxKWindowSize": tdmaCsV42TxKWindowSize,
       "tdmaCsV42RxKWindowSize": tdmaCsV42RxKWindowSize,
       "tdmaCsV42N400RetransLimit": tdmaCsV42N400RetransLimit,
       "tdmaCsV42FcsLength": tdmaCsV42FcsLength,
       "tdmaCsV42Bis": tdmaCsV42Bis,
       "tdmaCsV42BisRowStatusTable": tdmaCsV42BisRowStatusTable,
       "tdmaCsV42BisRowStatusEntry": tdmaCsV42BisRowStatusEntry,
       "tdmaCsV42BisRowStatus": tdmaCsV42BisRowStatus,
       "tdmaCsV42BisComponentName": tdmaCsV42BisComponentName,
       "tdmaCsV42BisStorageType": tdmaCsV42BisStorageType,
       "tdmaCsV42BisIndex": tdmaCsV42BisIndex,
       "tdmaCsV42BisProvTable": tdmaCsV42BisProvTable,
       "tdmaCsV42BisProvEntry": tdmaCsV42BisProvEntry,
       "tdmaCsV42BisP0CompressionDirection": tdmaCsV42BisP0CompressionDirection,
       "tdmaCsV42BisP1MaximumCodewords": tdmaCsV42BisP1MaximumCodewords,
       "tdmaCsV42BisP2MaximumStringSize": tdmaCsV42BisP2MaximumStringSize,
       "tdmaCsV42BisActionOnError": tdmaCsV42BisActionOnError,
       "tdmaCsLp": tdmaCsLp,
       "tdmaCsLpRowStatusTable": tdmaCsLpRowStatusTable,
       "tdmaCsLpRowStatusEntry": tdmaCsLpRowStatusEntry,
       "tdmaCsLpRowStatus": tdmaCsLpRowStatus,
       "tdmaCsLpComponentName": tdmaCsLpComponentName,
       "tdmaCsLpStorageType": tdmaCsLpStorageType,
       "tdmaCsLpIndex": tdmaCsLpIndex,
       "tdmaCsLpOperTable": tdmaCsLpOperTable,
       "tdmaCsLpOperEntry": tdmaCsLpOperEntry,
       "tdmaCsLpConfiguredBearerChannels": tdmaCsLpConfiguredBearerChannels,
       "tdmaCsLpActiveCalls": tdmaCsLpActiveCalls,
       "tdmaCsLpModemsSupported": tdmaCsLpModemsSupported,
       "tdmaCsServProvTable": tdmaCsServProvTable,
       "tdmaCsServProvEntry": tdmaCsServProvEntry,
       "tdmaCsTIwf1": tdmaCsTIwf1,
       "tdmaCsTIwf2": tdmaCsTIwf2,
       "tdmaCsT303": tdmaCsT303,
       "tdmaCsT305": tdmaCsT305,
       "tdmaCsT308": tdmaCsT308,
       "tdmaCsT313": tdmaCsT313,
       "tdmaCsT999": tdmaCsT999,
       "tdmaCsSupportedTechnology": tdmaCsSupportedTechnology,
       "tdmaCsSupportedService": tdmaCsSupportedService,
       "tdmaCsMiscProvTable": tdmaCsMiscProvTable,
       "tdmaCsMiscProvEntry": tdmaCsMiscProvEntry,
       "tdmaCsCommentText": tdmaCsCommentText,
       "tdmaCsMscIpAddress": tdmaCsMscIpAddress,
       "tdmaCsVirtualRouterName": tdmaCsVirtualRouterName,
       "tdmaCsVoiceLaw": tdmaCsVoiceLaw,
       "tdmaCsCidDataTable": tdmaCsCidDataTable,
       "tdmaCsCidDataEntry": tdmaCsCidDataEntry,
       "tdmaCsCustomerIdentifier": tdmaCsCustomerIdentifier,
       "tdmaCsStateTable": tdmaCsStateTable,
       "tdmaCsStateEntry": tdmaCsStateEntry,
       "tdmaCsAdminState": tdmaCsAdminState,
       "tdmaCsOperationalState": tdmaCsOperationalState,
       "tdmaCsUsageState": tdmaCsUsageState,
       "tdmaCsStatsTable": tdmaCsStatsTable,
       "tdmaCsStatsEntry": tdmaCsStatsEntry,
       "tdmaCsCurrentCalls": tdmaCsCurrentCalls,
       "tdmaCsCallsRequested": tdmaCsCallsRequested,
       "tdmaCsCallsSetUp": tdmaCsCallsSetUp,
       "tdmaCsCallsReleasedNormal": tdmaCsCallsReleasedNormal,
       "tdmaCsCallsReleasedAbnormal": tdmaCsCallsReleasedAbnormal,
       "tdmaCsErroredLFrames": tdmaCsErroredLFrames,
       "tdmaBc": tdmaBc,
       "tdmaBcRowStatusTable": tdmaBcRowStatusTable,
       "tdmaBcRowStatusEntry": tdmaBcRowStatusEntry,
       "tdmaBcRowStatus": tdmaBcRowStatus,
       "tdmaBcComponentName": tdmaBcComponentName,
       "tdmaBcStorageType": tdmaBcStorageType,
       "tdmaBcCsIndex": tdmaBcCsIndex,
       "tdmaBcBcIndex": tdmaBcBcIndex,
       "tdmaBcFramer": tdmaBcFramer,
       "tdmaBcFramerRowStatusTable": tdmaBcFramerRowStatusTable,
       "tdmaBcFramerRowStatusEntry": tdmaBcFramerRowStatusEntry,
       "tdmaBcFramerRowStatus": tdmaBcFramerRowStatus,
       "tdmaBcFramerComponentName": tdmaBcFramerComponentName,
       "tdmaBcFramerStorageType": tdmaBcFramerStorageType,
       "tdmaBcFramerIndex": tdmaBcFramerIndex,
       "tdmaBcFramerProvTable": tdmaBcFramerProvTable,
       "tdmaBcFramerProvEntry": tdmaBcFramerProvEntry,
       "tdmaBcFramerInterfaceName": tdmaBcFramerInterfaceName,
       "tdmaBcFramerStatsTable": tdmaBcFramerStatsTable,
       "tdmaBcFramerStatsEntry": tdmaBcFramerStatsEntry,
       "tdmaBcFramerTxFrames": tdmaBcFramerTxFrames,
       "tdmaBcFramerRxFrames": tdmaBcFramerRxFrames,
       "tdmaBcFramerRxBytes": tdmaBcFramerRxBytes,
       "tdmaBcFramerLinkTable": tdmaBcFramerLinkTable,
       "tdmaBcFramerLinkEntry": tdmaBcFramerLinkEntry,
       "tdmaBcFramerFramingType": tdmaBcFramerFramingType,
       "tdmaBcFramerStateTable": tdmaBcFramerStateTable,
       "tdmaBcFramerStateEntry": tdmaBcFramerStateEntry,
       "tdmaBcFramerAdminState": tdmaBcFramerAdminState,
       "tdmaBcFramerOperationalState": tdmaBcFramerOperationalState,
       "tdmaBcFramerUsageState": tdmaBcFramerUsageState,
       "tdmaBcModem": tdmaBcModem,
       "tdmaBcModemRowStatusTable": tdmaBcModemRowStatusTable,
       "tdmaBcModemRowStatusEntry": tdmaBcModemRowStatusEntry,
       "tdmaBcModemRowStatus": tdmaBcModemRowStatus,
       "tdmaBcModemComponentName": tdmaBcModemComponentName,
       "tdmaBcModemStorageType": tdmaBcModemStorageType,
       "tdmaBcModemIndex": tdmaBcModemIndex,
       "tdmaBcModemOperTable": tdmaBcModemOperTable,
       "tdmaBcModemOperEntry": tdmaBcModemOperEntry,
       "tdmaBcModemVoiceLaw": tdmaBcModemVoiceLaw,
       "tdmaBcModemRate": tdmaBcModemRate,
       "tdmaBcModemModemAlgorithmInUse": tdmaBcModemModemAlgorithmInUse,
       "tdmaBcModemProtocolState": tdmaBcModemProtocolState,
       "tdmaBcModemMobileSideFlowControlState": tdmaBcModemMobileSideFlowControlState,
       "tdmaBcModemPstnSideFlowControlState": tdmaBcModemPstnSideFlowControlState,
       "tdmaBcModemAsyncMode": tdmaBcModemAsyncMode,
       "tdmaBcModemOutbandFlowControl": tdmaBcModemOutbandFlowControl,
       "tdmaBcModemOutbandBreak": tdmaBcModemOutbandBreak,
       "tdmaBcModemAutobaud": tdmaBcModemAutobaud,
       "tdmaBcModemStatsTable": tdmaBcModemStatsTable,
       "tdmaBcModemStatsEntry": tdmaBcModemStatsEntry,
       "tdmaBcModemTxBytes": tdmaBcModemTxBytes,
       "tdmaBcModemRxBytes": tdmaBcModemRxBytes,
       "tdmaBcModemFramingErrors": tdmaBcModemFramingErrors,
       "tdmaBcFax": tdmaBcFax,
       "tdmaBcFaxRowStatusTable": tdmaBcFaxRowStatusTable,
       "tdmaBcFaxRowStatusEntry": tdmaBcFaxRowStatusEntry,
       "tdmaBcFaxRowStatus": tdmaBcFaxRowStatus,
       "tdmaBcFaxComponentName": tdmaBcFaxComponentName,
       "tdmaBcFaxStorageType": tdmaBcFaxStorageType,
       "tdmaBcFaxIndex": tdmaBcFaxIndex,
       "tdmaBcFaxOperTable": tdmaBcFaxOperTable,
       "tdmaBcFaxOperEntry": tdmaBcFaxOperEntry,
       "tdmaBcFaxActiveMode": tdmaBcFaxActiveMode,
       "tdmaBcFaxProtocolState": tdmaBcFaxProtocolState,
       "tdmaBcFaxMessageRate": tdmaBcFaxMessageRate,
       "tdmaBcFaxStatsTable": tdmaBcFaxStatsTable,
       "tdmaBcFaxStatsEntry": tdmaBcFaxStatsEntry,
       "tdmaBcFaxTxPagesToMobile": tdmaBcFaxTxPagesToMobile,
       "tdmaBcFaxRxPagesFromMobile": tdmaBcFaxRxPagesFromMobile,
       "tdmaBcDce": tdmaBcDce,
       "tdmaBcDceRowStatusTable": tdmaBcDceRowStatusTable,
       "tdmaBcDceRowStatusEntry": tdmaBcDceRowStatusEntry,
       "tdmaBcDceRowStatus": tdmaBcDceRowStatus,
       "tdmaBcDceComponentName": tdmaBcDceComponentName,
       "tdmaBcDceStorageType": tdmaBcDceStorageType,
       "tdmaBcDceIndex": tdmaBcDceIndex,
       "tdmaBcDsc": tdmaBcDsc,
       "tdmaBcDscRowStatusTable": tdmaBcDscRowStatusTable,
       "tdmaBcDscRowStatusEntry": tdmaBcDscRowStatusEntry,
       "tdmaBcDscRowStatus": tdmaBcDscRowStatus,
       "tdmaBcDscComponentName": tdmaBcDscComponentName,
       "tdmaBcDscStorageType": tdmaBcDscStorageType,
       "tdmaBcDscIndex": tdmaBcDscIndex,
       "tdmaBcDscOperTable": tdmaBcDscOperTable,
       "tdmaBcDscOperEntry": tdmaBcDscOperEntry,
       "tdmaBcDscP0CompressionDirection": tdmaBcDscP0CompressionDirection,
       "tdmaBcDscP1CompressionMaximumCodewords": tdmaBcDscP1CompressionMaximumCodewords,
       "tdmaBcDscP2CompressionMaximumCharacters": tdmaBcDscP2CompressionMaximumCharacters,
       "tdmaBcDscStatsTable": tdmaBcDscStatsTable,
       "tdmaBcDscStatsEntry": tdmaBcDscStatsEntry,
       "tdmaBcDscTxBytes": tdmaBcDscTxBytes,
       "tdmaBcDscRxBytes": tdmaBcDscRxBytes,
       "tdmaBcRlp1": tdmaBcRlp1,
       "tdmaBcRlp1RowStatusTable": tdmaBcRlp1RowStatusTable,
       "tdmaBcRlp1RowStatusEntry": tdmaBcRlp1RowStatusEntry,
       "tdmaBcRlp1RowStatus": tdmaBcRlp1RowStatus,
       "tdmaBcRlp1ComponentName": tdmaBcRlp1ComponentName,
       "tdmaBcRlp1StorageType": tdmaBcRlp1StorageType,
       "tdmaBcRlp1Index": tdmaBcRlp1Index,
       "tdmaBcRlp1OperTable": tdmaBcRlp1OperTable,
       "tdmaBcRlp1OperEntry": tdmaBcRlp1OperEntry,
       "tdmaBcRlp1Layer3L0ReqWinSize": tdmaBcRlp1Layer3L0ReqWinSize,
       "tdmaBcRlp1Layer3L1ReqWinSize1": tdmaBcRlp1Layer3L1ReqWinSize1,
       "tdmaBcRlp1T1ResponseTimer": tdmaBcRlp1T1ResponseTimer,
       "tdmaBcRlp1T2LinkActivityTimer": tdmaBcRlp1T2LinkActivityTimer,
       "tdmaBcRlp1T3PeerAckTimer": tdmaBcRlp1T3PeerAckTimer,
       "tdmaBcRlp1StatsTable": tdmaBcRlp1StatsTable,
       "tdmaBcRlp1StatsEntry": tdmaBcRlp1StatsEntry,
       "tdmaBcRlp1TxFrames": tdmaBcRlp1TxFrames,
       "tdmaBcRlp1RxFrames": tdmaBcRlp1RxFrames,
       "tdmaBcRlp1BadRxFrames": tdmaBcRlp1BadRxFrames,
       "tdmaBcV42": tdmaBcV42,
       "tdmaBcV42RowStatusTable": tdmaBcV42RowStatusTable,
       "tdmaBcV42RowStatusEntry": tdmaBcV42RowStatusEntry,
       "tdmaBcV42RowStatus": tdmaBcV42RowStatus,
       "tdmaBcV42ComponentName": tdmaBcV42ComponentName,
       "tdmaBcV42StorageType": tdmaBcV42StorageType,
       "tdmaBcV42Index": tdmaBcV42Index,
       "tdmaBcV42OperTable": tdmaBcV42OperTable,
       "tdmaBcV42OperEntry": tdmaBcV42OperEntry,
       "tdmaBcV42ProtocolState": tdmaBcV42ProtocolState,
       "tdmaBcV42TxN401FrameSize": tdmaBcV42TxN401FrameSize,
       "tdmaBcV42RxN401FrameSize": tdmaBcV42RxN401FrameSize,
       "tdmaBcV42TxKWindowSize": tdmaBcV42TxKWindowSize,
       "tdmaBcV42RxKWindowSize": tdmaBcV42RxKWindowSize,
       "tdmaBcV42V42ActiveInCall": tdmaBcV42V42ActiveInCall,
       "tdmaBcV42V42BisActiveInCall": tdmaBcV42V42BisActiveInCall,
       "tdmaBcV42StatsTable": tdmaBcV42StatsTable,
       "tdmaBcV42StatsEntry": tdmaBcV42StatsEntry,
       "tdmaBcV42RxIBytes": tdmaBcV42RxIBytes,
       "tdmaBcV42TxIBytes": tdmaBcV42TxIBytes,
       "tdmaBcV42RxIFrames": tdmaBcV42RxIFrames,
       "tdmaBcV42TxIFrames": tdmaBcV42TxIFrames,
       "tdmaBcV42RetransmittedFrames": tdmaBcV42RetransmittedFrames,
       "tdmaBcV42T1AckTimeouts": tdmaBcV42T1AckTimeouts,
       "tdmaBcV42RemoteBusyIndications": tdmaBcV42RemoteBusyIndications,
       "tdmaBcV42LocalBusyIndications": tdmaBcV42LocalBusyIndications,
       "tdmaBcV42BadFramesRx": tdmaBcV42BadFramesRx,
       "tdmaBcV42CrcErrorsRx": tdmaBcV42CrcErrorsRx,
       "tdmaBcV42Bis": tdmaBcV42Bis,
       "tdmaBcV42BisRowStatusTable": tdmaBcV42BisRowStatusTable,
       "tdmaBcV42BisRowStatusEntry": tdmaBcV42BisRowStatusEntry,
       "tdmaBcV42BisRowStatus": tdmaBcV42BisRowStatus,
       "tdmaBcV42BisComponentName": tdmaBcV42BisComponentName,
       "tdmaBcV42BisStorageType": tdmaBcV42BisStorageType,
       "tdmaBcV42BisIndex": tdmaBcV42BisIndex,
       "tdmaBcV42BisOperTable": tdmaBcV42BisOperTable,
       "tdmaBcV42BisOperEntry": tdmaBcV42BisOperEntry,
       "tdmaBcV42BisProtocolModeEncoder": tdmaBcV42BisProtocolModeEncoder,
       "tdmaBcV42BisProtocolModeDecoder": tdmaBcV42BisProtocolModeDecoder,
       "tdmaBcV42BisP0CompressionDirection": tdmaBcV42BisP0CompressionDirection,
       "tdmaBcV42BisP1MaximumCodewords": tdmaBcV42BisP1MaximumCodewords,
       "tdmaBcV42BisP2MaximumStringSize": tdmaBcV42BisP2MaximumStringSize,
       "tdmaBcV42BisLastDecodeError": tdmaBcV42BisLastDecodeError,
       "tdmaBcV42BisCompRatioEncoder": tdmaBcV42BisCompRatioEncoder,
       "tdmaBcV42BisCompRatioDecoder": tdmaBcV42BisCompRatioDecoder,
       "tdmaBcV42BisStatsTable": tdmaBcV42BisStatsTable,
       "tdmaBcV42BisStatsEntry": tdmaBcV42BisStatsEntry,
       "tdmaBcV42BisModeChangesEncode": tdmaBcV42BisModeChangesEncode,
       "tdmaBcV42BisModeChangesDecode": tdmaBcV42BisModeChangesDecode,
       "tdmaBcV42BisResetsEncode": tdmaBcV42BisResetsEncode,
       "tdmaBcV42BisResetsDecode": tdmaBcV42BisResetsDecode,
       "tdmaBcV42BisReinitializations": tdmaBcV42BisReinitializations,
       "tdmaBcV42BisErrorsInDecode": tdmaBcV42BisErrorsInDecode,
       "tdmaBcUr": tdmaBcUr,
       "tdmaBcUrRowStatusTable": tdmaBcUrRowStatusTable,
       "tdmaBcUrRowStatusEntry": tdmaBcUrRowStatusEntry,
       "tdmaBcUrRowStatus": tdmaBcUrRowStatus,
       "tdmaBcUrComponentName": tdmaBcUrComponentName,
       "tdmaBcUrStorageType": tdmaBcUrStorageType,
       "tdmaBcUrIndex": tdmaBcUrIndex,
       "tdmaBcUrOperTable": tdmaBcUrOperTable,
       "tdmaBcUrOperEntry": tdmaBcUrOperEntry,
       "tdmaBcUrRxBufferSize": tdmaBcUrRxBufferSize,
       "tdmaBcUrTxFlowControlState": tdmaBcUrTxFlowControlState,
       "tdmaBcUrRxFlowControlState": tdmaBcUrRxFlowControlState,
       "tdmaBcUrStatsTable": tdmaBcUrStatsTable,
       "tdmaBcUrStatsEntry": tdmaBcUrStatsEntry,
       "tdmaBcUrTxFrames": tdmaBcUrTxFrames,
       "tdmaBcUrRxFrames": tdmaBcUrRxFrames,
       "tdmaBcUrUnacknowledgedFrames": tdmaBcUrUnacknowledgedFrames,
       "tdmaBcUrCumUnacknowledgedFrames": tdmaBcUrCumUnacknowledgedFrames,
       "tdmaBcOperTable": tdmaBcOperTable,
       "tdmaBcOperEntry": tdmaBcOperEntry,
       "tdmaBcState": tdmaBcState,
       "tdmaBcCallType": tdmaBcCallType,
       "tdmaBcLastResponseCode": tdmaBcLastResponseCode,
       "tdmaBcMateBearerChannel": tdmaBcMateBearerChannel,
       "tdmaBcCidDataTable": tdmaBcCidDataTable,
       "tdmaBcCidDataEntry": tdmaBcCidDataEntry,
       "tdmaBcCustomerIdentifier": tdmaBcCustomerIdentifier,
       "tdmaBcStateTable": tdmaBcStateTable,
       "tdmaBcStateEntry": tdmaBcStateEntry,
       "tdmaBcAdminState": tdmaBcAdminState,
       "tdmaBcOperationalState": tdmaBcOperationalState,
       "tdmaBcUsageState": tdmaBcUsageState,
       "tdmaIwfMIB": tdmaIwfMIB,
       "tdmaIwfGroup": tdmaIwfGroup,
       "tdmaIwfGroupBE": tdmaIwfGroupBE,
       "tdmaIwfGroupBE01": tdmaIwfGroupBE01,
       "tdmaIwfGroupBE01A": tdmaIwfGroupBE01A,
       "tdmaIwfCapabilities": tdmaIwfCapabilities,
       "tdmaIwfCapabilitiesBE": tdmaIwfCapabilitiesBE,
       "tdmaIwfCapabilitiesBE01": tdmaIwfCapabilitiesBE01,
       "tdmaIwfCapabilitiesBE01A": tdmaIwfCapabilitiesBE01A}
)
