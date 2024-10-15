# SNMP MIB module (Nortel-MsCarrier-MscPassport-TdmaIwfMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-TdmaIwfMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:07 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
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
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "FixedPoint2",
    "Link",
    "NonReplicated")

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

_MscTdmaCs_ObjectIdentity = ObjectIdentity
mscTdmaCs = _MscTdmaCs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135)
)
_MscTdmaCsRowStatusTable_Object = MibTable
mscTdmaCsRowStatusTable = _MscTdmaCsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 1)
)
if mibBuilder.loadTexts:
    mscTdmaCsRowStatusTable.setStatus("mandatory")
_MscTdmaCsRowStatusEntry_Object = MibTableRow
mscTdmaCsRowStatusEntry = _MscTdmaCsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 1, 1)
)
mscTdmaCsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsCsIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaCsRowStatusEntry.setStatus("mandatory")
_MscTdmaCsRowStatus_Type = RowStatus
_MscTdmaCsRowStatus_Object = MibTableColumn
mscTdmaCsRowStatus = _MscTdmaCsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 1, 1, 1),
    _MscTdmaCsRowStatus_Type()
)
mscTdmaCsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsRowStatus.setStatus("mandatory")
_MscTdmaCsComponentName_Type = DisplayString
_MscTdmaCsComponentName_Object = MibTableColumn
mscTdmaCsComponentName = _MscTdmaCsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 1, 1, 2),
    _MscTdmaCsComponentName_Type()
)
mscTdmaCsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsComponentName.setStatus("mandatory")
_MscTdmaCsStorageType_Type = StorageType
_MscTdmaCsStorageType_Object = MibTableColumn
mscTdmaCsStorageType = _MscTdmaCsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 1, 1, 4),
    _MscTdmaCsStorageType_Type()
)
mscTdmaCsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsStorageType.setStatus("mandatory")


class _MscTdmaCsCsIndex_Type(Integer32):
    """Custom type mscTdmaCsCsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MscTdmaCsCsIndex_Type.__name__ = "Integer32"
_MscTdmaCsCsIndex_Object = MibTableColumn
mscTdmaCsCsIndex = _MscTdmaCsCsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 1, 1, 10),
    _MscTdmaCsCsIndex_Type()
)
mscTdmaCsCsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTdmaCsCsIndex.setStatus("mandatory")
_MscTdmaCsModem_ObjectIdentity = ObjectIdentity
mscTdmaCsModem = _MscTdmaCsModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 2)
)
_MscTdmaCsModemRowStatusTable_Object = MibTable
mscTdmaCsModemRowStatusTable = _MscTdmaCsModemRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 2, 1)
)
if mibBuilder.loadTexts:
    mscTdmaCsModemRowStatusTable.setStatus("mandatory")
_MscTdmaCsModemRowStatusEntry_Object = MibTableRow
mscTdmaCsModemRowStatusEntry = _MscTdmaCsModemRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 2, 1, 1)
)
mscTdmaCsModemRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsModemIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaCsModemRowStatusEntry.setStatus("mandatory")
_MscTdmaCsModemRowStatus_Type = RowStatus
_MscTdmaCsModemRowStatus_Object = MibTableColumn
mscTdmaCsModemRowStatus = _MscTdmaCsModemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 2, 1, 1, 1),
    _MscTdmaCsModemRowStatus_Type()
)
mscTdmaCsModemRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsModemRowStatus.setStatus("mandatory")
_MscTdmaCsModemComponentName_Type = DisplayString
_MscTdmaCsModemComponentName_Object = MibTableColumn
mscTdmaCsModemComponentName = _MscTdmaCsModemComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 2, 1, 1, 2),
    _MscTdmaCsModemComponentName_Type()
)
mscTdmaCsModemComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsModemComponentName.setStatus("mandatory")
_MscTdmaCsModemStorageType_Type = StorageType
_MscTdmaCsModemStorageType_Object = MibTableColumn
mscTdmaCsModemStorageType = _MscTdmaCsModemStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 2, 1, 1, 4),
    _MscTdmaCsModemStorageType_Type()
)
mscTdmaCsModemStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsModemStorageType.setStatus("mandatory")
_MscTdmaCsModemIndex_Type = NonReplicated
_MscTdmaCsModemIndex_Object = MibTableColumn
mscTdmaCsModemIndex = _MscTdmaCsModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 2, 1, 1, 10),
    _MscTdmaCsModemIndex_Type()
)
mscTdmaCsModemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTdmaCsModemIndex.setStatus("mandatory")
_MscTdmaCsFax_ObjectIdentity = ObjectIdentity
mscTdmaCsFax = _MscTdmaCsFax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 3)
)
_MscTdmaCsFaxRowStatusTable_Object = MibTable
mscTdmaCsFaxRowStatusTable = _MscTdmaCsFaxRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 3, 1)
)
if mibBuilder.loadTexts:
    mscTdmaCsFaxRowStatusTable.setStatus("mandatory")
_MscTdmaCsFaxRowStatusEntry_Object = MibTableRow
mscTdmaCsFaxRowStatusEntry = _MscTdmaCsFaxRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 3, 1, 1)
)
mscTdmaCsFaxRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsFaxIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaCsFaxRowStatusEntry.setStatus("mandatory")
_MscTdmaCsFaxRowStatus_Type = RowStatus
_MscTdmaCsFaxRowStatus_Object = MibTableColumn
mscTdmaCsFaxRowStatus = _MscTdmaCsFaxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 3, 1, 1, 1),
    _MscTdmaCsFaxRowStatus_Type()
)
mscTdmaCsFaxRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsFaxRowStatus.setStatus("mandatory")
_MscTdmaCsFaxComponentName_Type = DisplayString
_MscTdmaCsFaxComponentName_Object = MibTableColumn
mscTdmaCsFaxComponentName = _MscTdmaCsFaxComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 3, 1, 1, 2),
    _MscTdmaCsFaxComponentName_Type()
)
mscTdmaCsFaxComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsFaxComponentName.setStatus("mandatory")
_MscTdmaCsFaxStorageType_Type = StorageType
_MscTdmaCsFaxStorageType_Object = MibTableColumn
mscTdmaCsFaxStorageType = _MscTdmaCsFaxStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 3, 1, 1, 4),
    _MscTdmaCsFaxStorageType_Type()
)
mscTdmaCsFaxStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsFaxStorageType.setStatus("mandatory")
_MscTdmaCsFaxIndex_Type = NonReplicated
_MscTdmaCsFaxIndex_Object = MibTableColumn
mscTdmaCsFaxIndex = _MscTdmaCsFaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 3, 1, 1, 10),
    _MscTdmaCsFaxIndex_Type()
)
mscTdmaCsFaxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTdmaCsFaxIndex.setStatus("mandatory")
_MscTdmaCsDce_ObjectIdentity = ObjectIdentity
mscTdmaCsDce = _MscTdmaCsDce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 4)
)
_MscTdmaCsDceRowStatusTable_Object = MibTable
mscTdmaCsDceRowStatusTable = _MscTdmaCsDceRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 4, 1)
)
if mibBuilder.loadTexts:
    mscTdmaCsDceRowStatusTable.setStatus("mandatory")
_MscTdmaCsDceRowStatusEntry_Object = MibTableRow
mscTdmaCsDceRowStatusEntry = _MscTdmaCsDceRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 4, 1, 1)
)
mscTdmaCsDceRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsDceIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaCsDceRowStatusEntry.setStatus("mandatory")
_MscTdmaCsDceRowStatus_Type = RowStatus
_MscTdmaCsDceRowStatus_Object = MibTableColumn
mscTdmaCsDceRowStatus = _MscTdmaCsDceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 4, 1, 1, 1),
    _MscTdmaCsDceRowStatus_Type()
)
mscTdmaCsDceRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsDceRowStatus.setStatus("mandatory")
_MscTdmaCsDceComponentName_Type = DisplayString
_MscTdmaCsDceComponentName_Object = MibTableColumn
mscTdmaCsDceComponentName = _MscTdmaCsDceComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 4, 1, 1, 2),
    _MscTdmaCsDceComponentName_Type()
)
mscTdmaCsDceComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsDceComponentName.setStatus("mandatory")
_MscTdmaCsDceStorageType_Type = StorageType
_MscTdmaCsDceStorageType_Object = MibTableColumn
mscTdmaCsDceStorageType = _MscTdmaCsDceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 4, 1, 1, 4),
    _MscTdmaCsDceStorageType_Type()
)
mscTdmaCsDceStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsDceStorageType.setStatus("mandatory")
_MscTdmaCsDceIndex_Type = NonReplicated
_MscTdmaCsDceIndex_Object = MibTableColumn
mscTdmaCsDceIndex = _MscTdmaCsDceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 4, 1, 1, 10),
    _MscTdmaCsDceIndex_Type()
)
mscTdmaCsDceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTdmaCsDceIndex.setStatus("mandatory")
_MscTdmaCsDsc_ObjectIdentity = ObjectIdentity
mscTdmaCsDsc = _MscTdmaCsDsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 5)
)
_MscTdmaCsDscRowStatusTable_Object = MibTable
mscTdmaCsDscRowStatusTable = _MscTdmaCsDscRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 5, 1)
)
if mibBuilder.loadTexts:
    mscTdmaCsDscRowStatusTable.setStatus("mandatory")
_MscTdmaCsDscRowStatusEntry_Object = MibTableRow
mscTdmaCsDscRowStatusEntry = _MscTdmaCsDscRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 5, 1, 1)
)
mscTdmaCsDscRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsDscIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaCsDscRowStatusEntry.setStatus("mandatory")
_MscTdmaCsDscRowStatus_Type = RowStatus
_MscTdmaCsDscRowStatus_Object = MibTableColumn
mscTdmaCsDscRowStatus = _MscTdmaCsDscRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 5, 1, 1, 1),
    _MscTdmaCsDscRowStatus_Type()
)
mscTdmaCsDscRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsDscRowStatus.setStatus("mandatory")
_MscTdmaCsDscComponentName_Type = DisplayString
_MscTdmaCsDscComponentName_Object = MibTableColumn
mscTdmaCsDscComponentName = _MscTdmaCsDscComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 5, 1, 1, 2),
    _MscTdmaCsDscComponentName_Type()
)
mscTdmaCsDscComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsDscComponentName.setStatus("mandatory")
_MscTdmaCsDscStorageType_Type = StorageType
_MscTdmaCsDscStorageType_Object = MibTableColumn
mscTdmaCsDscStorageType = _MscTdmaCsDscStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 5, 1, 1, 4),
    _MscTdmaCsDscStorageType_Type()
)
mscTdmaCsDscStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsDscStorageType.setStatus("mandatory")
_MscTdmaCsDscIndex_Type = NonReplicated
_MscTdmaCsDscIndex_Object = MibTableColumn
mscTdmaCsDscIndex = _MscTdmaCsDscIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 5, 1, 1, 10),
    _MscTdmaCsDscIndex_Type()
)
mscTdmaCsDscIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTdmaCsDscIndex.setStatus("mandatory")
_MscTdmaCsDscProvTable_Object = MibTable
mscTdmaCsDscProvTable = _MscTdmaCsDscProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 5, 10)
)
if mibBuilder.loadTexts:
    mscTdmaCsDscProvTable.setStatus("mandatory")
_MscTdmaCsDscProvEntry_Object = MibTableRow
mscTdmaCsDscProvEntry = _MscTdmaCsDscProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 5, 10, 1)
)
mscTdmaCsDscProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsDscIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaCsDscProvEntry.setStatus("mandatory")


class _MscTdmaCsDscLl0BufferSize_Type(Unsigned32):
    """Custom type mscTdmaCsDscLl0BufferSize based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 65535),
    )


_MscTdmaCsDscLl0BufferSize_Type.__name__ = "Unsigned32"
_MscTdmaCsDscLl0BufferSize_Object = MibTableColumn
mscTdmaCsDscLl0BufferSize = _MscTdmaCsDscLl0BufferSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 5, 10, 1, 1),
    _MscTdmaCsDscLl0BufferSize_Type()
)
mscTdmaCsDscLl0BufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsDscLl0BufferSize.setStatus("obsolete")


class _MscTdmaCsDscLl1BufferSize_Type(Unsigned32):
    """Custom type mscTdmaCsDscLl1BufferSize based on Unsigned32"""
    defaultValue = 160

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(160, 65535),
    )


_MscTdmaCsDscLl1BufferSize_Type.__name__ = "Unsigned32"
_MscTdmaCsDscLl1BufferSize_Object = MibTableColumn
mscTdmaCsDscLl1BufferSize = _MscTdmaCsDscLl1BufferSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 5, 10, 1, 2),
    _MscTdmaCsDscLl1BufferSize_Type()
)
mscTdmaCsDscLl1BufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsDscLl1BufferSize.setStatus("obsolete")


class _MscTdmaCsDscK0Ll0WindowSize_Type(Unsigned32):
    """Custom type mscTdmaCsDscK0Ll0WindowSize based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_MscTdmaCsDscK0Ll0WindowSize_Type.__name__ = "Unsigned32"
_MscTdmaCsDscK0Ll0WindowSize_Object = MibTableColumn
mscTdmaCsDscK0Ll0WindowSize = _MscTdmaCsDscK0Ll0WindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 5, 10, 1, 3),
    _MscTdmaCsDscK0Ll0WindowSize_Type()
)
mscTdmaCsDscK0Ll0WindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsDscK0Ll0WindowSize.setStatus("mandatory")


class _MscTdmaCsDscK1Ll1WindowSize_Type(Unsigned32):
    """Custom type mscTdmaCsDscK1Ll1WindowSize based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_MscTdmaCsDscK1Ll1WindowSize_Type.__name__ = "Unsigned32"
_MscTdmaCsDscK1Ll1WindowSize_Object = MibTableColumn
mscTdmaCsDscK1Ll1WindowSize = _MscTdmaCsDscK1Ll1WindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 5, 10, 1, 4),
    _MscTdmaCsDscK1Ll1WindowSize_Type()
)
mscTdmaCsDscK1Ll1WindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsDscK1Ll1WindowSize.setStatus("mandatory")


class _MscTdmaCsDscP0CompressionDirection_Type(Integer32):
    """Custom type mscTdmaCsDscP0CompressionDirection based on Integer32"""
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


_MscTdmaCsDscP0CompressionDirection_Type.__name__ = "Integer32"
_MscTdmaCsDscP0CompressionDirection_Object = MibTableColumn
mscTdmaCsDscP0CompressionDirection = _MscTdmaCsDscP0CompressionDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 5, 10, 1, 5),
    _MscTdmaCsDscP0CompressionDirection_Type()
)
mscTdmaCsDscP0CompressionDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsDscP0CompressionDirection.setStatus("obsolete")


class _MscTdmaCsDscP1CompressionMaximumCodewords_Type(Unsigned32):
    """Custom type mscTdmaCsDscP1CompressionMaximumCodewords based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 4096),
    )


_MscTdmaCsDscP1CompressionMaximumCodewords_Type.__name__ = "Unsigned32"
_MscTdmaCsDscP1CompressionMaximumCodewords_Object = MibTableColumn
mscTdmaCsDscP1CompressionMaximumCodewords = _MscTdmaCsDscP1CompressionMaximumCodewords_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 5, 10, 1, 6),
    _MscTdmaCsDscP1CompressionMaximumCodewords_Type()
)
mscTdmaCsDscP1CompressionMaximumCodewords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsDscP1CompressionMaximumCodewords.setStatus("obsolete")


class _MscTdmaCsDscP2CompressionMaximumCharacters_Type(Unsigned32):
    """Custom type mscTdmaCsDscP2CompressionMaximumCharacters based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 150),
    )


_MscTdmaCsDscP2CompressionMaximumCharacters_Type.__name__ = "Unsigned32"
_MscTdmaCsDscP2CompressionMaximumCharacters_Object = MibTableColumn
mscTdmaCsDscP2CompressionMaximumCharacters = _MscTdmaCsDscP2CompressionMaximumCharacters_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 5, 10, 1, 7),
    _MscTdmaCsDscP2CompressionMaximumCharacters_Type()
)
mscTdmaCsDscP2CompressionMaximumCharacters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsDscP2CompressionMaximumCharacters.setStatus("obsolete")
_MscTdmaCsRlp1_ObjectIdentity = ObjectIdentity
mscTdmaCsRlp1 = _MscTdmaCsRlp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 6)
)
_MscTdmaCsRlp1RowStatusTable_Object = MibTable
mscTdmaCsRlp1RowStatusTable = _MscTdmaCsRlp1RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 6, 1)
)
if mibBuilder.loadTexts:
    mscTdmaCsRlp1RowStatusTable.setStatus("mandatory")
_MscTdmaCsRlp1RowStatusEntry_Object = MibTableRow
mscTdmaCsRlp1RowStatusEntry = _MscTdmaCsRlp1RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 6, 1, 1)
)
mscTdmaCsRlp1RowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsRlp1Index"),
)
if mibBuilder.loadTexts:
    mscTdmaCsRlp1RowStatusEntry.setStatus("mandatory")
_MscTdmaCsRlp1RowStatus_Type = RowStatus
_MscTdmaCsRlp1RowStatus_Object = MibTableColumn
mscTdmaCsRlp1RowStatus = _MscTdmaCsRlp1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 6, 1, 1, 1),
    _MscTdmaCsRlp1RowStatus_Type()
)
mscTdmaCsRlp1RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsRlp1RowStatus.setStatus("mandatory")
_MscTdmaCsRlp1ComponentName_Type = DisplayString
_MscTdmaCsRlp1ComponentName_Object = MibTableColumn
mscTdmaCsRlp1ComponentName = _MscTdmaCsRlp1ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 6, 1, 1, 2),
    _MscTdmaCsRlp1ComponentName_Type()
)
mscTdmaCsRlp1ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsRlp1ComponentName.setStatus("mandatory")
_MscTdmaCsRlp1StorageType_Type = StorageType
_MscTdmaCsRlp1StorageType_Object = MibTableColumn
mscTdmaCsRlp1StorageType = _MscTdmaCsRlp1StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 6, 1, 1, 4),
    _MscTdmaCsRlp1StorageType_Type()
)
mscTdmaCsRlp1StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsRlp1StorageType.setStatus("mandatory")


class _MscTdmaCsRlp1Index_Type(Integer32):
    """Custom type mscTdmaCsRlp1Index based on Integer32"""
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


_MscTdmaCsRlp1Index_Type.__name__ = "Integer32"
_MscTdmaCsRlp1Index_Object = MibTableColumn
mscTdmaCsRlp1Index = _MscTdmaCsRlp1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 6, 1, 1, 10),
    _MscTdmaCsRlp1Index_Type()
)
mscTdmaCsRlp1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTdmaCsRlp1Index.setStatus("mandatory")
_MscTdmaCsRlp1ProvTable_Object = MibTable
mscTdmaCsRlp1ProvTable = _MscTdmaCsRlp1ProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 6, 10)
)
if mibBuilder.loadTexts:
    mscTdmaCsRlp1ProvTable.setStatus("mandatory")
_MscTdmaCsRlp1ProvEntry_Object = MibTableRow
mscTdmaCsRlp1ProvEntry = _MscTdmaCsRlp1ProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 6, 10, 1)
)
mscTdmaCsRlp1ProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsRlp1Index"),
)
if mibBuilder.loadTexts:
    mscTdmaCsRlp1ProvEntry.setStatus("mandatory")


class _MscTdmaCsRlp1T1ResponseTimer_Type(Unsigned32):
    """Custom type mscTdmaCsRlp1T1ResponseTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_MscTdmaCsRlp1T1ResponseTimer_Type.__name__ = "Unsigned32"
_MscTdmaCsRlp1T1ResponseTimer_Object = MibTableColumn
mscTdmaCsRlp1T1ResponseTimer = _MscTdmaCsRlp1T1ResponseTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 6, 10, 1, 1),
    _MscTdmaCsRlp1T1ResponseTimer_Type()
)
mscTdmaCsRlp1T1ResponseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsRlp1T1ResponseTimer.setStatus("mandatory")


class _MscTdmaCsRlp1T2LinkActivityTimer_Type(Unsigned32):
    """Custom type mscTdmaCsRlp1T2LinkActivityTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_MscTdmaCsRlp1T2LinkActivityTimer_Type.__name__ = "Unsigned32"
_MscTdmaCsRlp1T2LinkActivityTimer_Object = MibTableColumn
mscTdmaCsRlp1T2LinkActivityTimer = _MscTdmaCsRlp1T2LinkActivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 6, 10, 1, 2),
    _MscTdmaCsRlp1T2LinkActivityTimer_Type()
)
mscTdmaCsRlp1T2LinkActivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsRlp1T2LinkActivityTimer.setStatus("mandatory")


class _MscTdmaCsRlp1T3PeerAckTimer_Type(Unsigned32):
    """Custom type mscTdmaCsRlp1T3PeerAckTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_MscTdmaCsRlp1T3PeerAckTimer_Type.__name__ = "Unsigned32"
_MscTdmaCsRlp1T3PeerAckTimer_Object = MibTableColumn
mscTdmaCsRlp1T3PeerAckTimer = _MscTdmaCsRlp1T3PeerAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 6, 10, 1, 3),
    _MscTdmaCsRlp1T3PeerAckTimer_Type()
)
mscTdmaCsRlp1T3PeerAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsRlp1T3PeerAckTimer.setStatus("mandatory")
_MscTdmaCsV42_ObjectIdentity = ObjectIdentity
mscTdmaCsV42 = _MscTdmaCsV42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 7)
)
_MscTdmaCsV42RowStatusTable_Object = MibTable
mscTdmaCsV42RowStatusTable = _MscTdmaCsV42RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 7, 1)
)
if mibBuilder.loadTexts:
    mscTdmaCsV42RowStatusTable.setStatus("mandatory")
_MscTdmaCsV42RowStatusEntry_Object = MibTableRow
mscTdmaCsV42RowStatusEntry = _MscTdmaCsV42RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 7, 1, 1)
)
mscTdmaCsV42RowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsV42Index"),
)
if mibBuilder.loadTexts:
    mscTdmaCsV42RowStatusEntry.setStatus("mandatory")
_MscTdmaCsV42RowStatus_Type = RowStatus
_MscTdmaCsV42RowStatus_Object = MibTableColumn
mscTdmaCsV42RowStatus = _MscTdmaCsV42RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 7, 1, 1, 1),
    _MscTdmaCsV42RowStatus_Type()
)
mscTdmaCsV42RowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsV42RowStatus.setStatus("mandatory")
_MscTdmaCsV42ComponentName_Type = DisplayString
_MscTdmaCsV42ComponentName_Object = MibTableColumn
mscTdmaCsV42ComponentName = _MscTdmaCsV42ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 7, 1, 1, 2),
    _MscTdmaCsV42ComponentName_Type()
)
mscTdmaCsV42ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsV42ComponentName.setStatus("mandatory")
_MscTdmaCsV42StorageType_Type = StorageType
_MscTdmaCsV42StorageType_Object = MibTableColumn
mscTdmaCsV42StorageType = _MscTdmaCsV42StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 7, 1, 1, 4),
    _MscTdmaCsV42StorageType_Type()
)
mscTdmaCsV42StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsV42StorageType.setStatus("mandatory")
_MscTdmaCsV42Index_Type = NonReplicated
_MscTdmaCsV42Index_Object = MibTableColumn
mscTdmaCsV42Index = _MscTdmaCsV42Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 7, 1, 1, 10),
    _MscTdmaCsV42Index_Type()
)
mscTdmaCsV42Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTdmaCsV42Index.setStatus("mandatory")
_MscTdmaCsV42ProvTable_Object = MibTable
mscTdmaCsV42ProvTable = _MscTdmaCsV42ProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 7, 10)
)
if mibBuilder.loadTexts:
    mscTdmaCsV42ProvTable.setStatus("mandatory")
_MscTdmaCsV42ProvEntry_Object = MibTableRow
mscTdmaCsV42ProvEntry = _MscTdmaCsV42ProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 7, 10, 1)
)
mscTdmaCsV42ProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsV42Index"),
)
if mibBuilder.loadTexts:
    mscTdmaCsV42ProvEntry.setStatus("mandatory")


class _MscTdmaCsV42T400DetectTimer_Type(FixedPoint2):
    """Custom type mscTdmaCsV42T400DetectTimer based on FixedPoint2"""
    defaultValue = 75

    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(75, 254),
    )


_MscTdmaCsV42T400DetectTimer_Type.__name__ = "FixedPoint2"
_MscTdmaCsV42T400DetectTimer_Object = MibTableColumn
mscTdmaCsV42T400DetectTimer = _MscTdmaCsV42T400DetectTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 7, 10, 1, 1),
    _MscTdmaCsV42T400DetectTimer_Type()
)
mscTdmaCsV42T400DetectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsV42T400DetectTimer.setStatus("mandatory")


class _MscTdmaCsV42T401AckTimer_Type(FixedPoint2):
    """Custom type mscTdmaCsV42T401AckTimer based on FixedPoint2"""
    defaultValue = 400

    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 900),
    )


_MscTdmaCsV42T401AckTimer_Type.__name__ = "FixedPoint2"
_MscTdmaCsV42T401AckTimer_Object = MibTableColumn
mscTdmaCsV42T401AckTimer = _MscTdmaCsV42T401AckTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 7, 10, 1, 2),
    _MscTdmaCsV42T401AckTimer_Type()
)
mscTdmaCsV42T401AckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsV42T401AckTimer.setStatus("mandatory")


class _MscTdmaCsV42T402AckDelayTimer_Type(FixedPoint2):
    """Custom type mscTdmaCsV42T402AckDelayTimer based on FixedPoint2"""
    defaultValue = 200

    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 450),
    )


_MscTdmaCsV42T402AckDelayTimer_Type.__name__ = "FixedPoint2"
_MscTdmaCsV42T402AckDelayTimer_Object = MibTableColumn
mscTdmaCsV42T402AckDelayTimer = _MscTdmaCsV42T402AckDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 7, 10, 1, 3),
    _MscTdmaCsV42T402AckDelayTimer_Type()
)
mscTdmaCsV42T402AckDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsV42T402AckDelayTimer.setStatus("mandatory")


class _MscTdmaCsV42T403IdleProbeTimer_Type(Unsigned32):
    """Custom type mscTdmaCsV42T403IdleProbeTimer based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 90),
    )


_MscTdmaCsV42T403IdleProbeTimer_Type.__name__ = "Unsigned32"
_MscTdmaCsV42T403IdleProbeTimer_Object = MibTableColumn
mscTdmaCsV42T403IdleProbeTimer = _MscTdmaCsV42T403IdleProbeTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 7, 10, 1, 4),
    _MscTdmaCsV42T403IdleProbeTimer_Type()
)
mscTdmaCsV42T403IdleProbeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsV42T403IdleProbeTimer.setStatus("mandatory")


class _MscTdmaCsV42TxN401FrameSize_Type(Unsigned32):
    """Custom type mscTdmaCsV42TxN401FrameSize based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscTdmaCsV42TxN401FrameSize_Type.__name__ = "Unsigned32"
_MscTdmaCsV42TxN401FrameSize_Object = MibTableColumn
mscTdmaCsV42TxN401FrameSize = _MscTdmaCsV42TxN401FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 7, 10, 1, 5),
    _MscTdmaCsV42TxN401FrameSize_Type()
)
mscTdmaCsV42TxN401FrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsV42TxN401FrameSize.setStatus("mandatory")


class _MscTdmaCsV42RxN401FrameSize_Type(Unsigned32):
    """Custom type mscTdmaCsV42RxN401FrameSize based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscTdmaCsV42RxN401FrameSize_Type.__name__ = "Unsigned32"
_MscTdmaCsV42RxN401FrameSize_Object = MibTableColumn
mscTdmaCsV42RxN401FrameSize = _MscTdmaCsV42RxN401FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 7, 10, 1, 6),
    _MscTdmaCsV42RxN401FrameSize_Type()
)
mscTdmaCsV42RxN401FrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsV42RxN401FrameSize.setStatus("mandatory")


class _MscTdmaCsV42TxKWindowSize_Type(Unsigned32):
    """Custom type mscTdmaCsV42TxKWindowSize based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscTdmaCsV42TxKWindowSize_Type.__name__ = "Unsigned32"
_MscTdmaCsV42TxKWindowSize_Object = MibTableColumn
mscTdmaCsV42TxKWindowSize = _MscTdmaCsV42TxKWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 7, 10, 1, 7),
    _MscTdmaCsV42TxKWindowSize_Type()
)
mscTdmaCsV42TxKWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsV42TxKWindowSize.setStatus("mandatory")


class _MscTdmaCsV42RxKWindowSize_Type(Unsigned32):
    """Custom type mscTdmaCsV42RxKWindowSize based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscTdmaCsV42RxKWindowSize_Type.__name__ = "Unsigned32"
_MscTdmaCsV42RxKWindowSize_Object = MibTableColumn
mscTdmaCsV42RxKWindowSize = _MscTdmaCsV42RxKWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 7, 10, 1, 8),
    _MscTdmaCsV42RxKWindowSize_Type()
)
mscTdmaCsV42RxKWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsV42RxKWindowSize.setStatus("mandatory")


class _MscTdmaCsV42N400RetransLimit_Type(Unsigned32):
    """Custom type mscTdmaCsV42N400RetransLimit based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscTdmaCsV42N400RetransLimit_Type.__name__ = "Unsigned32"
_MscTdmaCsV42N400RetransLimit_Object = MibTableColumn
mscTdmaCsV42N400RetransLimit = _MscTdmaCsV42N400RetransLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 7, 10, 1, 9),
    _MscTdmaCsV42N400RetransLimit_Type()
)
mscTdmaCsV42N400RetransLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsV42N400RetransLimit.setStatus("mandatory")


class _MscTdmaCsV42FcsLength_Type(Integer32):
    """Custom type mscTdmaCsV42FcsLength based on Integer32"""
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


_MscTdmaCsV42FcsLength_Type.__name__ = "Integer32"
_MscTdmaCsV42FcsLength_Object = MibTableColumn
mscTdmaCsV42FcsLength = _MscTdmaCsV42FcsLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 7, 10, 1, 10),
    _MscTdmaCsV42FcsLength_Type()
)
mscTdmaCsV42FcsLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsV42FcsLength.setStatus("mandatory")
_MscTdmaCsV42Bis_ObjectIdentity = ObjectIdentity
mscTdmaCsV42Bis = _MscTdmaCsV42Bis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 8)
)
_MscTdmaCsV42BisRowStatusTable_Object = MibTable
mscTdmaCsV42BisRowStatusTable = _MscTdmaCsV42BisRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 8, 1)
)
if mibBuilder.loadTexts:
    mscTdmaCsV42BisRowStatusTable.setStatus("mandatory")
_MscTdmaCsV42BisRowStatusEntry_Object = MibTableRow
mscTdmaCsV42BisRowStatusEntry = _MscTdmaCsV42BisRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 8, 1, 1)
)
mscTdmaCsV42BisRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsV42BisIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaCsV42BisRowStatusEntry.setStatus("mandatory")
_MscTdmaCsV42BisRowStatus_Type = RowStatus
_MscTdmaCsV42BisRowStatus_Object = MibTableColumn
mscTdmaCsV42BisRowStatus = _MscTdmaCsV42BisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 8, 1, 1, 1),
    _MscTdmaCsV42BisRowStatus_Type()
)
mscTdmaCsV42BisRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsV42BisRowStatus.setStatus("mandatory")
_MscTdmaCsV42BisComponentName_Type = DisplayString
_MscTdmaCsV42BisComponentName_Object = MibTableColumn
mscTdmaCsV42BisComponentName = _MscTdmaCsV42BisComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 8, 1, 1, 2),
    _MscTdmaCsV42BisComponentName_Type()
)
mscTdmaCsV42BisComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsV42BisComponentName.setStatus("mandatory")
_MscTdmaCsV42BisStorageType_Type = StorageType
_MscTdmaCsV42BisStorageType_Object = MibTableColumn
mscTdmaCsV42BisStorageType = _MscTdmaCsV42BisStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 8, 1, 1, 4),
    _MscTdmaCsV42BisStorageType_Type()
)
mscTdmaCsV42BisStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsV42BisStorageType.setStatus("mandatory")
_MscTdmaCsV42BisIndex_Type = NonReplicated
_MscTdmaCsV42BisIndex_Object = MibTableColumn
mscTdmaCsV42BisIndex = _MscTdmaCsV42BisIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 8, 1, 1, 10),
    _MscTdmaCsV42BisIndex_Type()
)
mscTdmaCsV42BisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTdmaCsV42BisIndex.setStatus("mandatory")
_MscTdmaCsV42BisProvTable_Object = MibTable
mscTdmaCsV42BisProvTable = _MscTdmaCsV42BisProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 8, 10)
)
if mibBuilder.loadTexts:
    mscTdmaCsV42BisProvTable.setStatus("mandatory")
_MscTdmaCsV42BisProvEntry_Object = MibTableRow
mscTdmaCsV42BisProvEntry = _MscTdmaCsV42BisProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 8, 10, 1)
)
mscTdmaCsV42BisProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsV42BisIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaCsV42BisProvEntry.setStatus("mandatory")


class _MscTdmaCsV42BisP0CompressionDirection_Type(Integer32):
    """Custom type mscTdmaCsV42BisP0CompressionDirection based on Integer32"""
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


_MscTdmaCsV42BisP0CompressionDirection_Type.__name__ = "Integer32"
_MscTdmaCsV42BisP0CompressionDirection_Object = MibTableColumn
mscTdmaCsV42BisP0CompressionDirection = _MscTdmaCsV42BisP0CompressionDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 8, 10, 1, 1),
    _MscTdmaCsV42BisP0CompressionDirection_Type()
)
mscTdmaCsV42BisP0CompressionDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsV42BisP0CompressionDirection.setStatus("mandatory")


class _MscTdmaCsV42BisP1MaximumCodewords_Type(Unsigned32):
    """Custom type mscTdmaCsV42BisP1MaximumCodewords based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 4096),
    )


_MscTdmaCsV42BisP1MaximumCodewords_Type.__name__ = "Unsigned32"
_MscTdmaCsV42BisP1MaximumCodewords_Object = MibTableColumn
mscTdmaCsV42BisP1MaximumCodewords = _MscTdmaCsV42BisP1MaximumCodewords_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 8, 10, 1, 2),
    _MscTdmaCsV42BisP1MaximumCodewords_Type()
)
mscTdmaCsV42BisP1MaximumCodewords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsV42BisP1MaximumCodewords.setStatus("mandatory")


class _MscTdmaCsV42BisP2MaximumStringSize_Type(Unsigned32):
    """Custom type mscTdmaCsV42BisP2MaximumStringSize based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 250),
    )


_MscTdmaCsV42BisP2MaximumStringSize_Type.__name__ = "Unsigned32"
_MscTdmaCsV42BisP2MaximumStringSize_Object = MibTableColumn
mscTdmaCsV42BisP2MaximumStringSize = _MscTdmaCsV42BisP2MaximumStringSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 8, 10, 1, 3),
    _MscTdmaCsV42BisP2MaximumStringSize_Type()
)
mscTdmaCsV42BisP2MaximumStringSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsV42BisP2MaximumStringSize.setStatus("mandatory")


class _MscTdmaCsV42BisActionOnError_Type(Integer32):
    """Custom type mscTdmaCsV42BisActionOnError based on Integer32"""
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


_MscTdmaCsV42BisActionOnError_Type.__name__ = "Integer32"
_MscTdmaCsV42BisActionOnError_Object = MibTableColumn
mscTdmaCsV42BisActionOnError = _MscTdmaCsV42BisActionOnError_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 8, 10, 1, 4),
    _MscTdmaCsV42BisActionOnError_Type()
)
mscTdmaCsV42BisActionOnError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsV42BisActionOnError.setStatus("mandatory")
_MscTdmaCsLp_ObjectIdentity = ObjectIdentity
mscTdmaCsLp = _MscTdmaCsLp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 9)
)
_MscTdmaCsLpRowStatusTable_Object = MibTable
mscTdmaCsLpRowStatusTable = _MscTdmaCsLpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 9, 1)
)
if mibBuilder.loadTexts:
    mscTdmaCsLpRowStatusTable.setStatus("mandatory")
_MscTdmaCsLpRowStatusEntry_Object = MibTableRow
mscTdmaCsLpRowStatusEntry = _MscTdmaCsLpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 9, 1, 1)
)
mscTdmaCsLpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsLpIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaCsLpRowStatusEntry.setStatus("mandatory")
_MscTdmaCsLpRowStatus_Type = RowStatus
_MscTdmaCsLpRowStatus_Object = MibTableColumn
mscTdmaCsLpRowStatus = _MscTdmaCsLpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 9, 1, 1, 1),
    _MscTdmaCsLpRowStatus_Type()
)
mscTdmaCsLpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsLpRowStatus.setStatus("mandatory")
_MscTdmaCsLpComponentName_Type = DisplayString
_MscTdmaCsLpComponentName_Object = MibTableColumn
mscTdmaCsLpComponentName = _MscTdmaCsLpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 9, 1, 1, 2),
    _MscTdmaCsLpComponentName_Type()
)
mscTdmaCsLpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsLpComponentName.setStatus("mandatory")
_MscTdmaCsLpStorageType_Type = StorageType
_MscTdmaCsLpStorageType_Object = MibTableColumn
mscTdmaCsLpStorageType = _MscTdmaCsLpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 9, 1, 1, 4),
    _MscTdmaCsLpStorageType_Type()
)
mscTdmaCsLpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsLpStorageType.setStatus("mandatory")


class _MscTdmaCsLpIndex_Type(Integer32):
    """Custom type mscTdmaCsLpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscTdmaCsLpIndex_Type.__name__ = "Integer32"
_MscTdmaCsLpIndex_Object = MibTableColumn
mscTdmaCsLpIndex = _MscTdmaCsLpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 9, 1, 1, 10),
    _MscTdmaCsLpIndex_Type()
)
mscTdmaCsLpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTdmaCsLpIndex.setStatus("mandatory")
_MscTdmaCsLpOperTable_Object = MibTable
mscTdmaCsLpOperTable = _MscTdmaCsLpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 9, 10)
)
if mibBuilder.loadTexts:
    mscTdmaCsLpOperTable.setStatus("mandatory")
_MscTdmaCsLpOperEntry_Object = MibTableRow
mscTdmaCsLpOperEntry = _MscTdmaCsLpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 9, 10, 1)
)
mscTdmaCsLpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsLpIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaCsLpOperEntry.setStatus("mandatory")


class _MscTdmaCsLpConfiguredBearerChannels_Type(Unsigned32):
    """Custom type mscTdmaCsLpConfiguredBearerChannels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 124),
    )


_MscTdmaCsLpConfiguredBearerChannels_Type.__name__ = "Unsigned32"
_MscTdmaCsLpConfiguredBearerChannels_Object = MibTableColumn
mscTdmaCsLpConfiguredBearerChannels = _MscTdmaCsLpConfiguredBearerChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 9, 10, 1, 1),
    _MscTdmaCsLpConfiguredBearerChannels_Type()
)
mscTdmaCsLpConfiguredBearerChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsLpConfiguredBearerChannels.setStatus("mandatory")


class _MscTdmaCsLpActiveCalls_Type(Gauge32):
    """Custom type mscTdmaCsLpActiveCalls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 124),
    )


_MscTdmaCsLpActiveCalls_Type.__name__ = "Gauge32"
_MscTdmaCsLpActiveCalls_Object = MibTableColumn
mscTdmaCsLpActiveCalls = _MscTdmaCsLpActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 9, 10, 1, 2),
    _MscTdmaCsLpActiveCalls_Type()
)
mscTdmaCsLpActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsLpActiveCalls.setStatus("mandatory")


class _MscTdmaCsLpModemsSupported_Type(Integer32):
    """Custom type mscTdmaCsLpModemsSupported based on Integer32"""
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


_MscTdmaCsLpModemsSupported_Type.__name__ = "Integer32"
_MscTdmaCsLpModemsSupported_Object = MibTableColumn
mscTdmaCsLpModemsSupported = _MscTdmaCsLpModemsSupported_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 9, 10, 1, 3),
    _MscTdmaCsLpModemsSupported_Type()
)
mscTdmaCsLpModemsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsLpModemsSupported.setStatus("mandatory")
_MscTdmaCsServProvTable_Object = MibTable
mscTdmaCsServProvTable = _MscTdmaCsServProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 100)
)
if mibBuilder.loadTexts:
    mscTdmaCsServProvTable.setStatus("mandatory")
_MscTdmaCsServProvEntry_Object = MibTableRow
mscTdmaCsServProvEntry = _MscTdmaCsServProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 100, 1)
)
mscTdmaCsServProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsCsIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaCsServProvEntry.setStatus("mandatory")


class _MscTdmaCsTIwf1_Type(Unsigned32):
    """Custom type mscTdmaCsTIwf1 based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MscTdmaCsTIwf1_Type.__name__ = "Unsigned32"
_MscTdmaCsTIwf1_Object = MibTableColumn
mscTdmaCsTIwf1 = _MscTdmaCsTIwf1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 100, 1, 1),
    _MscTdmaCsTIwf1_Type()
)
mscTdmaCsTIwf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsTIwf1.setStatus("mandatory")


class _MscTdmaCsTIwf2_Type(Unsigned32):
    """Custom type mscTdmaCsTIwf2 based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MscTdmaCsTIwf2_Type.__name__ = "Unsigned32"
_MscTdmaCsTIwf2_Object = MibTableColumn
mscTdmaCsTIwf2 = _MscTdmaCsTIwf2_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 100, 1, 2),
    _MscTdmaCsTIwf2_Type()
)
mscTdmaCsTIwf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsTIwf2.setStatus("mandatory")


class _MscTdmaCsT303_Type(Unsigned32):
    """Custom type mscTdmaCsT303 based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MscTdmaCsT303_Type.__name__ = "Unsigned32"
_MscTdmaCsT303_Object = MibTableColumn
mscTdmaCsT303 = _MscTdmaCsT303_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 100, 1, 3),
    _MscTdmaCsT303_Type()
)
mscTdmaCsT303.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsT303.setStatus("mandatory")


class _MscTdmaCsT305_Type(Unsigned32):
    """Custom type mscTdmaCsT305 based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MscTdmaCsT305_Type.__name__ = "Unsigned32"
_MscTdmaCsT305_Object = MibTableColumn
mscTdmaCsT305 = _MscTdmaCsT305_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 100, 1, 4),
    _MscTdmaCsT305_Type()
)
mscTdmaCsT305.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsT305.setStatus("mandatory")


class _MscTdmaCsT308_Type(Unsigned32):
    """Custom type mscTdmaCsT308 based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MscTdmaCsT308_Type.__name__ = "Unsigned32"
_MscTdmaCsT308_Object = MibTableColumn
mscTdmaCsT308 = _MscTdmaCsT308_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 100, 1, 5),
    _MscTdmaCsT308_Type()
)
mscTdmaCsT308.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsT308.setStatus("mandatory")


class _MscTdmaCsT313_Type(Unsigned32):
    """Custom type mscTdmaCsT313 based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MscTdmaCsT313_Type.__name__ = "Unsigned32"
_MscTdmaCsT313_Object = MibTableColumn
mscTdmaCsT313 = _MscTdmaCsT313_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 100, 1, 6),
    _MscTdmaCsT313_Type()
)
mscTdmaCsT313.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsT313.setStatus("mandatory")


class _MscTdmaCsT999_Type(Unsigned32):
    """Custom type mscTdmaCsT999 based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MscTdmaCsT999_Type.__name__ = "Unsigned32"
_MscTdmaCsT999_Object = MibTableColumn
mscTdmaCsT999 = _MscTdmaCsT999_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 100, 1, 7),
    _MscTdmaCsT999_Type()
)
mscTdmaCsT999.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsT999.setStatus("mandatory")


class _MscTdmaCsSupportedTechnology_Type(Integer32):
    """Custom type mscTdmaCsSupportedTechnology based on Integer32"""
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


_MscTdmaCsSupportedTechnology_Type.__name__ = "Integer32"
_MscTdmaCsSupportedTechnology_Object = MibTableColumn
mscTdmaCsSupportedTechnology = _MscTdmaCsSupportedTechnology_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 100, 1, 8),
    _MscTdmaCsSupportedTechnology_Type()
)
mscTdmaCsSupportedTechnology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsSupportedTechnology.setStatus("mandatory")


class _MscTdmaCsSupportedService_Type(Integer32):
    """Custom type mscTdmaCsSupportedService based on Integer32"""
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


_MscTdmaCsSupportedService_Type.__name__ = "Integer32"
_MscTdmaCsSupportedService_Object = MibTableColumn
mscTdmaCsSupportedService = _MscTdmaCsSupportedService_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 100, 1, 9),
    _MscTdmaCsSupportedService_Type()
)
mscTdmaCsSupportedService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsSupportedService.setStatus("mandatory")
_MscTdmaCsMiscProvTable_Object = MibTable
mscTdmaCsMiscProvTable = _MscTdmaCsMiscProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 101)
)
if mibBuilder.loadTexts:
    mscTdmaCsMiscProvTable.setStatus("mandatory")
_MscTdmaCsMiscProvEntry_Object = MibTableRow
mscTdmaCsMiscProvEntry = _MscTdmaCsMiscProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 101, 1)
)
mscTdmaCsMiscProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsCsIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaCsMiscProvEntry.setStatus("mandatory")


class _MscTdmaCsCommentText_Type(AsciiString):
    """Custom type mscTdmaCsCommentText based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscTdmaCsCommentText_Type.__name__ = "AsciiString"
_MscTdmaCsCommentText_Object = MibTableColumn
mscTdmaCsCommentText = _MscTdmaCsCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 101, 1, 1),
    _MscTdmaCsCommentText_Type()
)
mscTdmaCsCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsCommentText.setStatus("mandatory")


class _MscTdmaCsMscIpAddress_Type(IpAddress):
    """Custom type mscTdmaCsMscIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_MscTdmaCsMscIpAddress_Object = MibTableColumn
mscTdmaCsMscIpAddress = _MscTdmaCsMscIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 101, 1, 2),
    _MscTdmaCsMscIpAddress_Type()
)
mscTdmaCsMscIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsMscIpAddress.setStatus("mandatory")
_MscTdmaCsVirtualRouterName_Type = RowPointer
_MscTdmaCsVirtualRouterName_Object = MibTableColumn
mscTdmaCsVirtualRouterName = _MscTdmaCsVirtualRouterName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 101, 1, 3),
    _MscTdmaCsVirtualRouterName_Type()
)
mscTdmaCsVirtualRouterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsVirtualRouterName.setStatus("mandatory")


class _MscTdmaCsVoiceLaw_Type(Integer32):
    """Custom type mscTdmaCsVoiceLaw based on Integer32"""
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


_MscTdmaCsVoiceLaw_Type.__name__ = "Integer32"
_MscTdmaCsVoiceLaw_Object = MibTableColumn
mscTdmaCsVoiceLaw = _MscTdmaCsVoiceLaw_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 101, 1, 4),
    _MscTdmaCsVoiceLaw_Type()
)
mscTdmaCsVoiceLaw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsVoiceLaw.setStatus("mandatory")
_MscTdmaCsCidDataTable_Object = MibTable
mscTdmaCsCidDataTable = _MscTdmaCsCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 103)
)
if mibBuilder.loadTexts:
    mscTdmaCsCidDataTable.setStatus("mandatory")
_MscTdmaCsCidDataEntry_Object = MibTableRow
mscTdmaCsCidDataEntry = _MscTdmaCsCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 103, 1)
)
mscTdmaCsCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsCsIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaCsCidDataEntry.setStatus("mandatory")


class _MscTdmaCsCustomerIdentifier_Type(Unsigned32):
    """Custom type mscTdmaCsCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscTdmaCsCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscTdmaCsCustomerIdentifier_Object = MibTableColumn
mscTdmaCsCustomerIdentifier = _MscTdmaCsCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 103, 1, 1),
    _MscTdmaCsCustomerIdentifier_Type()
)
mscTdmaCsCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaCsCustomerIdentifier.setStatus("mandatory")
_MscTdmaCsStateTable_Object = MibTable
mscTdmaCsStateTable = _MscTdmaCsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 104)
)
if mibBuilder.loadTexts:
    mscTdmaCsStateTable.setStatus("mandatory")
_MscTdmaCsStateEntry_Object = MibTableRow
mscTdmaCsStateEntry = _MscTdmaCsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 104, 1)
)
mscTdmaCsStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsCsIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaCsStateEntry.setStatus("mandatory")


class _MscTdmaCsAdminState_Type(Integer32):
    """Custom type mscTdmaCsAdminState based on Integer32"""
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


_MscTdmaCsAdminState_Type.__name__ = "Integer32"
_MscTdmaCsAdminState_Object = MibTableColumn
mscTdmaCsAdminState = _MscTdmaCsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 104, 1, 1),
    _MscTdmaCsAdminState_Type()
)
mscTdmaCsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsAdminState.setStatus("mandatory")


class _MscTdmaCsOperationalState_Type(Integer32):
    """Custom type mscTdmaCsOperationalState based on Integer32"""
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


_MscTdmaCsOperationalState_Type.__name__ = "Integer32"
_MscTdmaCsOperationalState_Object = MibTableColumn
mscTdmaCsOperationalState = _MscTdmaCsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 104, 1, 2),
    _MscTdmaCsOperationalState_Type()
)
mscTdmaCsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsOperationalState.setStatus("mandatory")


class _MscTdmaCsUsageState_Type(Integer32):
    """Custom type mscTdmaCsUsageState based on Integer32"""
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


_MscTdmaCsUsageState_Type.__name__ = "Integer32"
_MscTdmaCsUsageState_Object = MibTableColumn
mscTdmaCsUsageState = _MscTdmaCsUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 104, 1, 3),
    _MscTdmaCsUsageState_Type()
)
mscTdmaCsUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsUsageState.setStatus("mandatory")
_MscTdmaCsStatsTable_Object = MibTable
mscTdmaCsStatsTable = _MscTdmaCsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 121)
)
if mibBuilder.loadTexts:
    mscTdmaCsStatsTable.setStatus("mandatory")
_MscTdmaCsStatsEntry_Object = MibTableRow
mscTdmaCsStatsEntry = _MscTdmaCsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 121, 1)
)
mscTdmaCsStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaCsCsIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaCsStatsEntry.setStatus("mandatory")


class _MscTdmaCsCurrentCalls_Type(Gauge32):
    """Custom type mscTdmaCsCurrentCalls based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_MscTdmaCsCurrentCalls_Type.__name__ = "Gauge32"
_MscTdmaCsCurrentCalls_Object = MibTableColumn
mscTdmaCsCurrentCalls = _MscTdmaCsCurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 121, 1, 1),
    _MscTdmaCsCurrentCalls_Type()
)
mscTdmaCsCurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsCurrentCalls.setStatus("mandatory")
_MscTdmaCsCallsRequested_Type = Counter32
_MscTdmaCsCallsRequested_Object = MibTableColumn
mscTdmaCsCallsRequested = _MscTdmaCsCallsRequested_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 121, 1, 2),
    _MscTdmaCsCallsRequested_Type()
)
mscTdmaCsCallsRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsCallsRequested.setStatus("mandatory")
_MscTdmaCsCallsSetUp_Type = Counter32
_MscTdmaCsCallsSetUp_Object = MibTableColumn
mscTdmaCsCallsSetUp = _MscTdmaCsCallsSetUp_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 121, 1, 3),
    _MscTdmaCsCallsSetUp_Type()
)
mscTdmaCsCallsSetUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsCallsSetUp.setStatus("mandatory")
_MscTdmaCsCallsReleasedNormal_Type = Counter32
_MscTdmaCsCallsReleasedNormal_Object = MibTableColumn
mscTdmaCsCallsReleasedNormal = _MscTdmaCsCallsReleasedNormal_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 121, 1, 4),
    _MscTdmaCsCallsReleasedNormal_Type()
)
mscTdmaCsCallsReleasedNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsCallsReleasedNormal.setStatus("mandatory")
_MscTdmaCsCallsReleasedAbnormal_Type = Counter32
_MscTdmaCsCallsReleasedAbnormal_Object = MibTableColumn
mscTdmaCsCallsReleasedAbnormal = _MscTdmaCsCallsReleasedAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 121, 1, 5),
    _MscTdmaCsCallsReleasedAbnormal_Type()
)
mscTdmaCsCallsReleasedAbnormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsCallsReleasedAbnormal.setStatus("mandatory")
_MscTdmaCsErroredLFrames_Type = Counter32
_MscTdmaCsErroredLFrames_Object = MibTableColumn
mscTdmaCsErroredLFrames = _MscTdmaCsErroredLFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 135, 121, 1, 6),
    _MscTdmaCsErroredLFrames_Type()
)
mscTdmaCsErroredLFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaCsErroredLFrames.setStatus("mandatory")
_MscTdmaBc_ObjectIdentity = ObjectIdentity
mscTdmaBc = _MscTdmaBc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136)
)
_MscTdmaBcRowStatusTable_Object = MibTable
mscTdmaBcRowStatusTable = _MscTdmaBcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 1)
)
if mibBuilder.loadTexts:
    mscTdmaBcRowStatusTable.setStatus("mandatory")
_MscTdmaBcRowStatusEntry_Object = MibTableRow
mscTdmaBcRowStatusEntry = _MscTdmaBcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 1, 1)
)
mscTdmaBcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcRowStatusEntry.setStatus("mandatory")
_MscTdmaBcRowStatus_Type = RowStatus
_MscTdmaBcRowStatus_Object = MibTableColumn
mscTdmaBcRowStatus = _MscTdmaBcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 1, 1, 1),
    _MscTdmaBcRowStatus_Type()
)
mscTdmaBcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaBcRowStatus.setStatus("mandatory")
_MscTdmaBcComponentName_Type = DisplayString
_MscTdmaBcComponentName_Object = MibTableColumn
mscTdmaBcComponentName = _MscTdmaBcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 1, 1, 2),
    _MscTdmaBcComponentName_Type()
)
mscTdmaBcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcComponentName.setStatus("mandatory")
_MscTdmaBcStorageType_Type = StorageType
_MscTdmaBcStorageType_Object = MibTableColumn
mscTdmaBcStorageType = _MscTdmaBcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 1, 1, 4),
    _MscTdmaBcStorageType_Type()
)
mscTdmaBcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcStorageType.setStatus("mandatory")


class _MscTdmaBcCsIndex_Type(Integer32):
    """Custom type mscTdmaBcCsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MscTdmaBcCsIndex_Type.__name__ = "Integer32"
_MscTdmaBcCsIndex_Object = MibTableColumn
mscTdmaBcCsIndex = _MscTdmaBcCsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 1, 1, 10),
    _MscTdmaBcCsIndex_Type()
)
mscTdmaBcCsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTdmaBcCsIndex.setStatus("mandatory")


class _MscTdmaBcBcIndex_Type(Integer32):
    """Custom type mscTdmaBcBcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_MscTdmaBcBcIndex_Type.__name__ = "Integer32"
_MscTdmaBcBcIndex_Object = MibTableColumn
mscTdmaBcBcIndex = _MscTdmaBcBcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 1, 1, 11),
    _MscTdmaBcBcIndex_Type()
)
mscTdmaBcBcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTdmaBcBcIndex.setStatus("mandatory")
_MscTdmaBcFramer_ObjectIdentity = ObjectIdentity
mscTdmaBcFramer = _MscTdmaBcFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 2)
)
_MscTdmaBcFramerRowStatusTable_Object = MibTable
mscTdmaBcFramerRowStatusTable = _MscTdmaBcFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 2, 1)
)
if mibBuilder.loadTexts:
    mscTdmaBcFramerRowStatusTable.setStatus("mandatory")
_MscTdmaBcFramerRowStatusEntry_Object = MibTableRow
mscTdmaBcFramerRowStatusEntry = _MscTdmaBcFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 2, 1, 1)
)
mscTdmaBcFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcFramerIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcFramerRowStatusEntry.setStatus("mandatory")
_MscTdmaBcFramerRowStatus_Type = RowStatus
_MscTdmaBcFramerRowStatus_Object = MibTableColumn
mscTdmaBcFramerRowStatus = _MscTdmaBcFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 2, 1, 1, 1),
    _MscTdmaBcFramerRowStatus_Type()
)
mscTdmaBcFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcFramerRowStatus.setStatus("mandatory")
_MscTdmaBcFramerComponentName_Type = DisplayString
_MscTdmaBcFramerComponentName_Object = MibTableColumn
mscTdmaBcFramerComponentName = _MscTdmaBcFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 2, 1, 1, 2),
    _MscTdmaBcFramerComponentName_Type()
)
mscTdmaBcFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcFramerComponentName.setStatus("mandatory")
_MscTdmaBcFramerStorageType_Type = StorageType
_MscTdmaBcFramerStorageType_Object = MibTableColumn
mscTdmaBcFramerStorageType = _MscTdmaBcFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 2, 1, 1, 4),
    _MscTdmaBcFramerStorageType_Type()
)
mscTdmaBcFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcFramerStorageType.setStatus("mandatory")
_MscTdmaBcFramerIndex_Type = NonReplicated
_MscTdmaBcFramerIndex_Object = MibTableColumn
mscTdmaBcFramerIndex = _MscTdmaBcFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 2, 1, 1, 10),
    _MscTdmaBcFramerIndex_Type()
)
mscTdmaBcFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTdmaBcFramerIndex.setStatus("mandatory")
_MscTdmaBcFramerProvTable_Object = MibTable
mscTdmaBcFramerProvTable = _MscTdmaBcFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 2, 10)
)
if mibBuilder.loadTexts:
    mscTdmaBcFramerProvTable.setStatus("mandatory")
_MscTdmaBcFramerProvEntry_Object = MibTableRow
mscTdmaBcFramerProvEntry = _MscTdmaBcFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 2, 10, 1)
)
mscTdmaBcFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcFramerIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcFramerProvEntry.setStatus("mandatory")
_MscTdmaBcFramerInterfaceName_Type = Link
_MscTdmaBcFramerInterfaceName_Object = MibTableColumn
mscTdmaBcFramerInterfaceName = _MscTdmaBcFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 2, 10, 1, 1),
    _MscTdmaBcFramerInterfaceName_Type()
)
mscTdmaBcFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaBcFramerInterfaceName.setStatus("mandatory")
_MscTdmaBcFramerStatsTable_Object = MibTable
mscTdmaBcFramerStatsTable = _MscTdmaBcFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 2, 11)
)
if mibBuilder.loadTexts:
    mscTdmaBcFramerStatsTable.setStatus("mandatory")
_MscTdmaBcFramerStatsEntry_Object = MibTableRow
mscTdmaBcFramerStatsEntry = _MscTdmaBcFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 2, 11, 1)
)
mscTdmaBcFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcFramerIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcFramerStatsEntry.setStatus("mandatory")
_MscTdmaBcFramerTxFrames_Type = Counter32
_MscTdmaBcFramerTxFrames_Object = MibTableColumn
mscTdmaBcFramerTxFrames = _MscTdmaBcFramerTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 2, 11, 1, 1),
    _MscTdmaBcFramerTxFrames_Type()
)
mscTdmaBcFramerTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcFramerTxFrames.setStatus("mandatory")
_MscTdmaBcFramerRxFrames_Type = Counter32
_MscTdmaBcFramerRxFrames_Object = MibTableColumn
mscTdmaBcFramerRxFrames = _MscTdmaBcFramerRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 2, 11, 1, 2),
    _MscTdmaBcFramerRxFrames_Type()
)
mscTdmaBcFramerRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcFramerRxFrames.setStatus("mandatory")
_MscTdmaBcFramerRxBytes_Type = Counter32
_MscTdmaBcFramerRxBytes_Object = MibTableColumn
mscTdmaBcFramerRxBytes = _MscTdmaBcFramerRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 2, 11, 1, 3),
    _MscTdmaBcFramerRxBytes_Type()
)
mscTdmaBcFramerRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcFramerRxBytes.setStatus("mandatory")
_MscTdmaBcFramerLinkTable_Object = MibTable
mscTdmaBcFramerLinkTable = _MscTdmaBcFramerLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 2, 12)
)
if mibBuilder.loadTexts:
    mscTdmaBcFramerLinkTable.setStatus("mandatory")
_MscTdmaBcFramerLinkEntry_Object = MibTableRow
mscTdmaBcFramerLinkEntry = _MscTdmaBcFramerLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 2, 12, 1)
)
mscTdmaBcFramerLinkEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcFramerIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcFramerLinkEntry.setStatus("mandatory")


class _MscTdmaBcFramerFramingType_Type(Integer32):
    """Custom type mscTdmaBcFramerFramingType based on Integer32"""
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


_MscTdmaBcFramerFramingType_Type.__name__ = "Integer32"
_MscTdmaBcFramerFramingType_Object = MibTableColumn
mscTdmaBcFramerFramingType = _MscTdmaBcFramerFramingType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 2, 12, 1, 1),
    _MscTdmaBcFramerFramingType_Type()
)
mscTdmaBcFramerFramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaBcFramerFramingType.setStatus("mandatory")
_MscTdmaBcFramerStateTable_Object = MibTable
mscTdmaBcFramerStateTable = _MscTdmaBcFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 2, 13)
)
if mibBuilder.loadTexts:
    mscTdmaBcFramerStateTable.setStatus("mandatory")
_MscTdmaBcFramerStateEntry_Object = MibTableRow
mscTdmaBcFramerStateEntry = _MscTdmaBcFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 2, 13, 1)
)
mscTdmaBcFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcFramerIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcFramerStateEntry.setStatus("mandatory")


class _MscTdmaBcFramerAdminState_Type(Integer32):
    """Custom type mscTdmaBcFramerAdminState based on Integer32"""
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


_MscTdmaBcFramerAdminState_Type.__name__ = "Integer32"
_MscTdmaBcFramerAdminState_Object = MibTableColumn
mscTdmaBcFramerAdminState = _MscTdmaBcFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 2, 13, 1, 1),
    _MscTdmaBcFramerAdminState_Type()
)
mscTdmaBcFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcFramerAdminState.setStatus("mandatory")


class _MscTdmaBcFramerOperationalState_Type(Integer32):
    """Custom type mscTdmaBcFramerOperationalState based on Integer32"""
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


_MscTdmaBcFramerOperationalState_Type.__name__ = "Integer32"
_MscTdmaBcFramerOperationalState_Object = MibTableColumn
mscTdmaBcFramerOperationalState = _MscTdmaBcFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 2, 13, 1, 2),
    _MscTdmaBcFramerOperationalState_Type()
)
mscTdmaBcFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcFramerOperationalState.setStatus("mandatory")


class _MscTdmaBcFramerUsageState_Type(Integer32):
    """Custom type mscTdmaBcFramerUsageState based on Integer32"""
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


_MscTdmaBcFramerUsageState_Type.__name__ = "Integer32"
_MscTdmaBcFramerUsageState_Object = MibTableColumn
mscTdmaBcFramerUsageState = _MscTdmaBcFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 2, 13, 1, 3),
    _MscTdmaBcFramerUsageState_Type()
)
mscTdmaBcFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcFramerUsageState.setStatus("mandatory")
_MscTdmaBcModem_ObjectIdentity = ObjectIdentity
mscTdmaBcModem = _MscTdmaBcModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 3)
)
_MscTdmaBcModemRowStatusTable_Object = MibTable
mscTdmaBcModemRowStatusTable = _MscTdmaBcModemRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 3, 1)
)
if mibBuilder.loadTexts:
    mscTdmaBcModemRowStatusTable.setStatus("mandatory")
_MscTdmaBcModemRowStatusEntry_Object = MibTableRow
mscTdmaBcModemRowStatusEntry = _MscTdmaBcModemRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 3, 1, 1)
)
mscTdmaBcModemRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcModemIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcModemRowStatusEntry.setStatus("mandatory")
_MscTdmaBcModemRowStatus_Type = RowStatus
_MscTdmaBcModemRowStatus_Object = MibTableColumn
mscTdmaBcModemRowStatus = _MscTdmaBcModemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 3, 1, 1, 1),
    _MscTdmaBcModemRowStatus_Type()
)
mscTdmaBcModemRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcModemRowStatus.setStatus("mandatory")
_MscTdmaBcModemComponentName_Type = DisplayString
_MscTdmaBcModemComponentName_Object = MibTableColumn
mscTdmaBcModemComponentName = _MscTdmaBcModemComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 3, 1, 1, 2),
    _MscTdmaBcModemComponentName_Type()
)
mscTdmaBcModemComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcModemComponentName.setStatus("mandatory")
_MscTdmaBcModemStorageType_Type = StorageType
_MscTdmaBcModemStorageType_Object = MibTableColumn
mscTdmaBcModemStorageType = _MscTdmaBcModemStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 3, 1, 1, 4),
    _MscTdmaBcModemStorageType_Type()
)
mscTdmaBcModemStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcModemStorageType.setStatus("mandatory")
_MscTdmaBcModemIndex_Type = NonReplicated
_MscTdmaBcModemIndex_Object = MibTableColumn
mscTdmaBcModemIndex = _MscTdmaBcModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 3, 1, 1, 10),
    _MscTdmaBcModemIndex_Type()
)
mscTdmaBcModemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTdmaBcModemIndex.setStatus("mandatory")
_MscTdmaBcModemOperTable_Object = MibTable
mscTdmaBcModemOperTable = _MscTdmaBcModemOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 3, 10)
)
if mibBuilder.loadTexts:
    mscTdmaBcModemOperTable.setStatus("mandatory")
_MscTdmaBcModemOperEntry_Object = MibTableRow
mscTdmaBcModemOperEntry = _MscTdmaBcModemOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 3, 10, 1)
)
mscTdmaBcModemOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcModemIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcModemOperEntry.setStatus("mandatory")


class _MscTdmaBcModemVoiceLaw_Type(Integer32):
    """Custom type mscTdmaBcModemVoiceLaw based on Integer32"""
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


_MscTdmaBcModemVoiceLaw_Type.__name__ = "Integer32"
_MscTdmaBcModemVoiceLaw_Object = MibTableColumn
mscTdmaBcModemVoiceLaw = _MscTdmaBcModemVoiceLaw_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 3, 10, 1, 1),
    _MscTdmaBcModemVoiceLaw_Type()
)
mscTdmaBcModemVoiceLaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcModemVoiceLaw.setStatus("mandatory")


class _MscTdmaBcModemRate_Type(Integer32):
    """Custom type mscTdmaBcModemRate based on Integer32"""
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


_MscTdmaBcModemRate_Type.__name__ = "Integer32"
_MscTdmaBcModemRate_Object = MibTableColumn
mscTdmaBcModemRate = _MscTdmaBcModemRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 3, 10, 1, 2),
    _MscTdmaBcModemRate_Type()
)
mscTdmaBcModemRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcModemRate.setStatus("mandatory")


class _MscTdmaBcModemModemAlgorithmInUse_Type(OctetString):
    """Custom type mscTdmaBcModemModemAlgorithmInUse based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscTdmaBcModemModemAlgorithmInUse_Type.__name__ = "OctetString"
_MscTdmaBcModemModemAlgorithmInUse_Object = MibTableColumn
mscTdmaBcModemModemAlgorithmInUse = _MscTdmaBcModemModemAlgorithmInUse_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 3, 10, 1, 3),
    _MscTdmaBcModemModemAlgorithmInUse_Type()
)
mscTdmaBcModemModemAlgorithmInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcModemModemAlgorithmInUse.setStatus("mandatory")


class _MscTdmaBcModemProtocolState_Type(Integer32):
    """Custom type mscTdmaBcModemProtocolState based on Integer32"""
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


_MscTdmaBcModemProtocolState_Type.__name__ = "Integer32"
_MscTdmaBcModemProtocolState_Object = MibTableColumn
mscTdmaBcModemProtocolState = _MscTdmaBcModemProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 3, 10, 1, 4),
    _MscTdmaBcModemProtocolState_Type()
)
mscTdmaBcModemProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcModemProtocolState.setStatus("mandatory")


class _MscTdmaBcModemMobileSideFlowControlState_Type(Integer32):
    """Custom type mscTdmaBcModemMobileSideFlowControlState based on Integer32"""
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


_MscTdmaBcModemMobileSideFlowControlState_Type.__name__ = "Integer32"
_MscTdmaBcModemMobileSideFlowControlState_Object = MibTableColumn
mscTdmaBcModemMobileSideFlowControlState = _MscTdmaBcModemMobileSideFlowControlState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 3, 10, 1, 5),
    _MscTdmaBcModemMobileSideFlowControlState_Type()
)
mscTdmaBcModemMobileSideFlowControlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcModemMobileSideFlowControlState.setStatus("mandatory")


class _MscTdmaBcModemPstnSideFlowControlState_Type(Integer32):
    """Custom type mscTdmaBcModemPstnSideFlowControlState based on Integer32"""
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


_MscTdmaBcModemPstnSideFlowControlState_Type.__name__ = "Integer32"
_MscTdmaBcModemPstnSideFlowControlState_Object = MibTableColumn
mscTdmaBcModemPstnSideFlowControlState = _MscTdmaBcModemPstnSideFlowControlState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 3, 10, 1, 6),
    _MscTdmaBcModemPstnSideFlowControlState_Type()
)
mscTdmaBcModemPstnSideFlowControlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcModemPstnSideFlowControlState.setStatus("mandatory")


class _MscTdmaBcModemAsyncMode_Type(Integer32):
    """Custom type mscTdmaBcModemAsyncMode based on Integer32"""
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


_MscTdmaBcModemAsyncMode_Type.__name__ = "Integer32"
_MscTdmaBcModemAsyncMode_Object = MibTableColumn
mscTdmaBcModemAsyncMode = _MscTdmaBcModemAsyncMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 3, 10, 1, 7),
    _MscTdmaBcModemAsyncMode_Type()
)
mscTdmaBcModemAsyncMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcModemAsyncMode.setStatus("mandatory")


class _MscTdmaBcModemOutbandFlowControl_Type(Integer32):
    """Custom type mscTdmaBcModemOutbandFlowControl based on Integer32"""
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


_MscTdmaBcModemOutbandFlowControl_Type.__name__ = "Integer32"
_MscTdmaBcModemOutbandFlowControl_Object = MibTableColumn
mscTdmaBcModemOutbandFlowControl = _MscTdmaBcModemOutbandFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 3, 10, 1, 8),
    _MscTdmaBcModemOutbandFlowControl_Type()
)
mscTdmaBcModemOutbandFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcModemOutbandFlowControl.setStatus("mandatory")


class _MscTdmaBcModemOutbandBreak_Type(Integer32):
    """Custom type mscTdmaBcModemOutbandBreak based on Integer32"""
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


_MscTdmaBcModemOutbandBreak_Type.__name__ = "Integer32"
_MscTdmaBcModemOutbandBreak_Object = MibTableColumn
mscTdmaBcModemOutbandBreak = _MscTdmaBcModemOutbandBreak_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 3, 10, 1, 9),
    _MscTdmaBcModemOutbandBreak_Type()
)
mscTdmaBcModemOutbandBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcModemOutbandBreak.setStatus("mandatory")


class _MscTdmaBcModemAutobaud_Type(Integer32):
    """Custom type mscTdmaBcModemAutobaud based on Integer32"""
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


_MscTdmaBcModemAutobaud_Type.__name__ = "Integer32"
_MscTdmaBcModemAutobaud_Object = MibTableColumn
mscTdmaBcModemAutobaud = _MscTdmaBcModemAutobaud_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 3, 10, 1, 10),
    _MscTdmaBcModemAutobaud_Type()
)
mscTdmaBcModemAutobaud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcModemAutobaud.setStatus("mandatory")
_MscTdmaBcModemStatsTable_Object = MibTable
mscTdmaBcModemStatsTable = _MscTdmaBcModemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 3, 11)
)
if mibBuilder.loadTexts:
    mscTdmaBcModemStatsTable.setStatus("mandatory")
_MscTdmaBcModemStatsEntry_Object = MibTableRow
mscTdmaBcModemStatsEntry = _MscTdmaBcModemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 3, 11, 1)
)
mscTdmaBcModemStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcModemIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcModemStatsEntry.setStatus("mandatory")
_MscTdmaBcModemTxBytes_Type = Counter32
_MscTdmaBcModemTxBytes_Object = MibTableColumn
mscTdmaBcModemTxBytes = _MscTdmaBcModemTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 3, 11, 1, 1),
    _MscTdmaBcModemTxBytes_Type()
)
mscTdmaBcModemTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcModemTxBytes.setStatus("mandatory")
_MscTdmaBcModemRxBytes_Type = Counter32
_MscTdmaBcModemRxBytes_Object = MibTableColumn
mscTdmaBcModemRxBytes = _MscTdmaBcModemRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 3, 11, 1, 2),
    _MscTdmaBcModemRxBytes_Type()
)
mscTdmaBcModemRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcModemRxBytes.setStatus("mandatory")
_MscTdmaBcModemFramingErrors_Type = Counter32
_MscTdmaBcModemFramingErrors_Object = MibTableColumn
mscTdmaBcModemFramingErrors = _MscTdmaBcModemFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 3, 11, 1, 3),
    _MscTdmaBcModemFramingErrors_Type()
)
mscTdmaBcModemFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcModemFramingErrors.setStatus("mandatory")
_MscTdmaBcFax_ObjectIdentity = ObjectIdentity
mscTdmaBcFax = _MscTdmaBcFax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 4)
)
_MscTdmaBcFaxRowStatusTable_Object = MibTable
mscTdmaBcFaxRowStatusTable = _MscTdmaBcFaxRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 4, 1)
)
if mibBuilder.loadTexts:
    mscTdmaBcFaxRowStatusTable.setStatus("mandatory")
_MscTdmaBcFaxRowStatusEntry_Object = MibTableRow
mscTdmaBcFaxRowStatusEntry = _MscTdmaBcFaxRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 4, 1, 1)
)
mscTdmaBcFaxRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcFaxIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcFaxRowStatusEntry.setStatus("mandatory")
_MscTdmaBcFaxRowStatus_Type = RowStatus
_MscTdmaBcFaxRowStatus_Object = MibTableColumn
mscTdmaBcFaxRowStatus = _MscTdmaBcFaxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 4, 1, 1, 1),
    _MscTdmaBcFaxRowStatus_Type()
)
mscTdmaBcFaxRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcFaxRowStatus.setStatus("mandatory")
_MscTdmaBcFaxComponentName_Type = DisplayString
_MscTdmaBcFaxComponentName_Object = MibTableColumn
mscTdmaBcFaxComponentName = _MscTdmaBcFaxComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 4, 1, 1, 2),
    _MscTdmaBcFaxComponentName_Type()
)
mscTdmaBcFaxComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcFaxComponentName.setStatus("mandatory")
_MscTdmaBcFaxStorageType_Type = StorageType
_MscTdmaBcFaxStorageType_Object = MibTableColumn
mscTdmaBcFaxStorageType = _MscTdmaBcFaxStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 4, 1, 1, 4),
    _MscTdmaBcFaxStorageType_Type()
)
mscTdmaBcFaxStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcFaxStorageType.setStatus("mandatory")
_MscTdmaBcFaxIndex_Type = NonReplicated
_MscTdmaBcFaxIndex_Object = MibTableColumn
mscTdmaBcFaxIndex = _MscTdmaBcFaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 4, 1, 1, 10),
    _MscTdmaBcFaxIndex_Type()
)
mscTdmaBcFaxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTdmaBcFaxIndex.setStatus("mandatory")
_MscTdmaBcFaxOperTable_Object = MibTable
mscTdmaBcFaxOperTable = _MscTdmaBcFaxOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 4, 10)
)
if mibBuilder.loadTexts:
    mscTdmaBcFaxOperTable.setStatus("mandatory")
_MscTdmaBcFaxOperEntry_Object = MibTableRow
mscTdmaBcFaxOperEntry = _MscTdmaBcFaxOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 4, 10, 1)
)
mscTdmaBcFaxOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcFaxIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcFaxOperEntry.setStatus("mandatory")


class _MscTdmaBcFaxActiveMode_Type(Integer32):
    """Custom type mscTdmaBcFaxActiveMode based on Integer32"""
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


_MscTdmaBcFaxActiveMode_Type.__name__ = "Integer32"
_MscTdmaBcFaxActiveMode_Object = MibTableColumn
mscTdmaBcFaxActiveMode = _MscTdmaBcFaxActiveMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 4, 10, 1, 1),
    _MscTdmaBcFaxActiveMode_Type()
)
mscTdmaBcFaxActiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcFaxActiveMode.setStatus("mandatory")


class _MscTdmaBcFaxProtocolState_Type(Integer32):
    """Custom type mscTdmaBcFaxProtocolState based on Integer32"""
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


_MscTdmaBcFaxProtocolState_Type.__name__ = "Integer32"
_MscTdmaBcFaxProtocolState_Object = MibTableColumn
mscTdmaBcFaxProtocolState = _MscTdmaBcFaxProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 4, 10, 1, 2),
    _MscTdmaBcFaxProtocolState_Type()
)
mscTdmaBcFaxProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcFaxProtocolState.setStatus("mandatory")


class _MscTdmaBcFaxMessageRate_Type(Unsigned32):
    """Custom type mscTdmaBcFaxMessageRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_MscTdmaBcFaxMessageRate_Type.__name__ = "Unsigned32"
_MscTdmaBcFaxMessageRate_Object = MibTableColumn
mscTdmaBcFaxMessageRate = _MscTdmaBcFaxMessageRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 4, 10, 1, 3),
    _MscTdmaBcFaxMessageRate_Type()
)
mscTdmaBcFaxMessageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcFaxMessageRate.setStatus("mandatory")
_MscTdmaBcFaxStatsTable_Object = MibTable
mscTdmaBcFaxStatsTable = _MscTdmaBcFaxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 4, 11)
)
if mibBuilder.loadTexts:
    mscTdmaBcFaxStatsTable.setStatus("mandatory")
_MscTdmaBcFaxStatsEntry_Object = MibTableRow
mscTdmaBcFaxStatsEntry = _MscTdmaBcFaxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 4, 11, 1)
)
mscTdmaBcFaxStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcFaxIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcFaxStatsEntry.setStatus("mandatory")
_MscTdmaBcFaxTxPagesToMobile_Type = Counter32
_MscTdmaBcFaxTxPagesToMobile_Object = MibTableColumn
mscTdmaBcFaxTxPagesToMobile = _MscTdmaBcFaxTxPagesToMobile_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 4, 11, 1, 1),
    _MscTdmaBcFaxTxPagesToMobile_Type()
)
mscTdmaBcFaxTxPagesToMobile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcFaxTxPagesToMobile.setStatus("mandatory")
_MscTdmaBcFaxRxPagesFromMobile_Type = Counter32
_MscTdmaBcFaxRxPagesFromMobile_Object = MibTableColumn
mscTdmaBcFaxRxPagesFromMobile = _MscTdmaBcFaxRxPagesFromMobile_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 4, 11, 1, 2),
    _MscTdmaBcFaxRxPagesFromMobile_Type()
)
mscTdmaBcFaxRxPagesFromMobile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcFaxRxPagesFromMobile.setStatus("mandatory")
_MscTdmaBcDce_ObjectIdentity = ObjectIdentity
mscTdmaBcDce = _MscTdmaBcDce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 5)
)
_MscTdmaBcDceRowStatusTable_Object = MibTable
mscTdmaBcDceRowStatusTable = _MscTdmaBcDceRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 5, 1)
)
if mibBuilder.loadTexts:
    mscTdmaBcDceRowStatusTable.setStatus("mandatory")
_MscTdmaBcDceRowStatusEntry_Object = MibTableRow
mscTdmaBcDceRowStatusEntry = _MscTdmaBcDceRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 5, 1, 1)
)
mscTdmaBcDceRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcDceIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcDceRowStatusEntry.setStatus("mandatory")
_MscTdmaBcDceRowStatus_Type = RowStatus
_MscTdmaBcDceRowStatus_Object = MibTableColumn
mscTdmaBcDceRowStatus = _MscTdmaBcDceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 5, 1, 1, 1),
    _MscTdmaBcDceRowStatus_Type()
)
mscTdmaBcDceRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcDceRowStatus.setStatus("mandatory")
_MscTdmaBcDceComponentName_Type = DisplayString
_MscTdmaBcDceComponentName_Object = MibTableColumn
mscTdmaBcDceComponentName = _MscTdmaBcDceComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 5, 1, 1, 2),
    _MscTdmaBcDceComponentName_Type()
)
mscTdmaBcDceComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcDceComponentName.setStatus("mandatory")
_MscTdmaBcDceStorageType_Type = StorageType
_MscTdmaBcDceStorageType_Object = MibTableColumn
mscTdmaBcDceStorageType = _MscTdmaBcDceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 5, 1, 1, 4),
    _MscTdmaBcDceStorageType_Type()
)
mscTdmaBcDceStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcDceStorageType.setStatus("mandatory")
_MscTdmaBcDceIndex_Type = NonReplicated
_MscTdmaBcDceIndex_Object = MibTableColumn
mscTdmaBcDceIndex = _MscTdmaBcDceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 5, 1, 1, 10),
    _MscTdmaBcDceIndex_Type()
)
mscTdmaBcDceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTdmaBcDceIndex.setStatus("mandatory")
_MscTdmaBcDsc_ObjectIdentity = ObjectIdentity
mscTdmaBcDsc = _MscTdmaBcDsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 6)
)
_MscTdmaBcDscRowStatusTable_Object = MibTable
mscTdmaBcDscRowStatusTable = _MscTdmaBcDscRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 6, 1)
)
if mibBuilder.loadTexts:
    mscTdmaBcDscRowStatusTable.setStatus("mandatory")
_MscTdmaBcDscRowStatusEntry_Object = MibTableRow
mscTdmaBcDscRowStatusEntry = _MscTdmaBcDscRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 6, 1, 1)
)
mscTdmaBcDscRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcDscIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcDscRowStatusEntry.setStatus("mandatory")
_MscTdmaBcDscRowStatus_Type = RowStatus
_MscTdmaBcDscRowStatus_Object = MibTableColumn
mscTdmaBcDscRowStatus = _MscTdmaBcDscRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 6, 1, 1, 1),
    _MscTdmaBcDscRowStatus_Type()
)
mscTdmaBcDscRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcDscRowStatus.setStatus("mandatory")
_MscTdmaBcDscComponentName_Type = DisplayString
_MscTdmaBcDscComponentName_Object = MibTableColumn
mscTdmaBcDscComponentName = _MscTdmaBcDscComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 6, 1, 1, 2),
    _MscTdmaBcDscComponentName_Type()
)
mscTdmaBcDscComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcDscComponentName.setStatus("mandatory")
_MscTdmaBcDscStorageType_Type = StorageType
_MscTdmaBcDscStorageType_Object = MibTableColumn
mscTdmaBcDscStorageType = _MscTdmaBcDscStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 6, 1, 1, 4),
    _MscTdmaBcDscStorageType_Type()
)
mscTdmaBcDscStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcDscStorageType.setStatus("mandatory")
_MscTdmaBcDscIndex_Type = NonReplicated
_MscTdmaBcDscIndex_Object = MibTableColumn
mscTdmaBcDscIndex = _MscTdmaBcDscIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 6, 1, 1, 10),
    _MscTdmaBcDscIndex_Type()
)
mscTdmaBcDscIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTdmaBcDscIndex.setStatus("mandatory")
_MscTdmaBcDscOperTable_Object = MibTable
mscTdmaBcDscOperTable = _MscTdmaBcDscOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 6, 10)
)
if mibBuilder.loadTexts:
    mscTdmaBcDscOperTable.setStatus("mandatory")
_MscTdmaBcDscOperEntry_Object = MibTableRow
mscTdmaBcDscOperEntry = _MscTdmaBcDscOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 6, 10, 1)
)
mscTdmaBcDscOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcDscIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcDscOperEntry.setStatus("mandatory")


class _MscTdmaBcDscP0CompressionDirection_Type(Integer32):
    """Custom type mscTdmaBcDscP0CompressionDirection based on Integer32"""
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


_MscTdmaBcDscP0CompressionDirection_Type.__name__ = "Integer32"
_MscTdmaBcDscP0CompressionDirection_Object = MibTableColumn
mscTdmaBcDscP0CompressionDirection = _MscTdmaBcDscP0CompressionDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 6, 10, 1, 1),
    _MscTdmaBcDscP0CompressionDirection_Type()
)
mscTdmaBcDscP0CompressionDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcDscP0CompressionDirection.setStatus("mandatory")


class _MscTdmaBcDscP1CompressionMaximumCodewords_Type(Unsigned32):
    """Custom type mscTdmaBcDscP1CompressionMaximumCodewords based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 65535),
    )


_MscTdmaBcDscP1CompressionMaximumCodewords_Type.__name__ = "Unsigned32"
_MscTdmaBcDscP1CompressionMaximumCodewords_Object = MibTableColumn
mscTdmaBcDscP1CompressionMaximumCodewords = _MscTdmaBcDscP1CompressionMaximumCodewords_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 6, 10, 1, 2),
    _MscTdmaBcDscP1CompressionMaximumCodewords_Type()
)
mscTdmaBcDscP1CompressionMaximumCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcDscP1CompressionMaximumCodewords.setStatus("mandatory")


class _MscTdmaBcDscP2CompressionMaximumCharacters_Type(Unsigned32):
    """Custom type mscTdmaBcDscP2CompressionMaximumCharacters based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 250),
    )


_MscTdmaBcDscP2CompressionMaximumCharacters_Type.__name__ = "Unsigned32"
_MscTdmaBcDscP2CompressionMaximumCharacters_Object = MibTableColumn
mscTdmaBcDscP2CompressionMaximumCharacters = _MscTdmaBcDscP2CompressionMaximumCharacters_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 6, 10, 1, 3),
    _MscTdmaBcDscP2CompressionMaximumCharacters_Type()
)
mscTdmaBcDscP2CompressionMaximumCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcDscP2CompressionMaximumCharacters.setStatus("mandatory")
_MscTdmaBcDscStatsTable_Object = MibTable
mscTdmaBcDscStatsTable = _MscTdmaBcDscStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 6, 11)
)
if mibBuilder.loadTexts:
    mscTdmaBcDscStatsTable.setStatus("mandatory")
_MscTdmaBcDscStatsEntry_Object = MibTableRow
mscTdmaBcDscStatsEntry = _MscTdmaBcDscStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 6, 11, 1)
)
mscTdmaBcDscStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcDscIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcDscStatsEntry.setStatus("mandatory")
_MscTdmaBcDscTxBytes_Type = Counter32
_MscTdmaBcDscTxBytes_Object = MibTableColumn
mscTdmaBcDscTxBytes = _MscTdmaBcDscTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 6, 11, 1, 1),
    _MscTdmaBcDscTxBytes_Type()
)
mscTdmaBcDscTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcDscTxBytes.setStatus("mandatory")
_MscTdmaBcDscRxBytes_Type = Counter32
_MscTdmaBcDscRxBytes_Object = MibTableColumn
mscTdmaBcDscRxBytes = _MscTdmaBcDscRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 6, 11, 1, 2),
    _MscTdmaBcDscRxBytes_Type()
)
mscTdmaBcDscRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcDscRxBytes.setStatus("mandatory")
_MscTdmaBcRlp1_ObjectIdentity = ObjectIdentity
mscTdmaBcRlp1 = _MscTdmaBcRlp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 7)
)
_MscTdmaBcRlp1RowStatusTable_Object = MibTable
mscTdmaBcRlp1RowStatusTable = _MscTdmaBcRlp1RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 7, 1)
)
if mibBuilder.loadTexts:
    mscTdmaBcRlp1RowStatusTable.setStatus("mandatory")
_MscTdmaBcRlp1RowStatusEntry_Object = MibTableRow
mscTdmaBcRlp1RowStatusEntry = _MscTdmaBcRlp1RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 7, 1, 1)
)
mscTdmaBcRlp1RowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcRlp1Index"),
)
if mibBuilder.loadTexts:
    mscTdmaBcRlp1RowStatusEntry.setStatus("mandatory")
_MscTdmaBcRlp1RowStatus_Type = RowStatus
_MscTdmaBcRlp1RowStatus_Object = MibTableColumn
mscTdmaBcRlp1RowStatus = _MscTdmaBcRlp1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 7, 1, 1, 1),
    _MscTdmaBcRlp1RowStatus_Type()
)
mscTdmaBcRlp1RowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcRlp1RowStatus.setStatus("mandatory")
_MscTdmaBcRlp1ComponentName_Type = DisplayString
_MscTdmaBcRlp1ComponentName_Object = MibTableColumn
mscTdmaBcRlp1ComponentName = _MscTdmaBcRlp1ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 7, 1, 1, 2),
    _MscTdmaBcRlp1ComponentName_Type()
)
mscTdmaBcRlp1ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcRlp1ComponentName.setStatus("mandatory")
_MscTdmaBcRlp1StorageType_Type = StorageType
_MscTdmaBcRlp1StorageType_Object = MibTableColumn
mscTdmaBcRlp1StorageType = _MscTdmaBcRlp1StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 7, 1, 1, 4),
    _MscTdmaBcRlp1StorageType_Type()
)
mscTdmaBcRlp1StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcRlp1StorageType.setStatus("mandatory")
_MscTdmaBcRlp1Index_Type = NonReplicated
_MscTdmaBcRlp1Index_Object = MibTableColumn
mscTdmaBcRlp1Index = _MscTdmaBcRlp1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 7, 1, 1, 10),
    _MscTdmaBcRlp1Index_Type()
)
mscTdmaBcRlp1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTdmaBcRlp1Index.setStatus("mandatory")
_MscTdmaBcRlp1OperTable_Object = MibTable
mscTdmaBcRlp1OperTable = _MscTdmaBcRlp1OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 7, 10)
)
if mibBuilder.loadTexts:
    mscTdmaBcRlp1OperTable.setStatus("mandatory")
_MscTdmaBcRlp1OperEntry_Object = MibTableRow
mscTdmaBcRlp1OperEntry = _MscTdmaBcRlp1OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 7, 10, 1)
)
mscTdmaBcRlp1OperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcRlp1Index"),
)
if mibBuilder.loadTexts:
    mscTdmaBcRlp1OperEntry.setStatus("mandatory")


class _MscTdmaBcRlp1Layer3L0ReqWinSize_Type(Unsigned32):
    """Custom type mscTdmaBcRlp1Layer3L0ReqWinSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_MscTdmaBcRlp1Layer3L0ReqWinSize_Type.__name__ = "Unsigned32"
_MscTdmaBcRlp1Layer3L0ReqWinSize_Object = MibTableColumn
mscTdmaBcRlp1Layer3L0ReqWinSize = _MscTdmaBcRlp1Layer3L0ReqWinSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 7, 10, 1, 1),
    _MscTdmaBcRlp1Layer3L0ReqWinSize_Type()
)
mscTdmaBcRlp1Layer3L0ReqWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcRlp1Layer3L0ReqWinSize.setStatus("mandatory")


class _MscTdmaBcRlp1Layer3L1ReqWinSize1_Type(Unsigned32):
    """Custom type mscTdmaBcRlp1Layer3L1ReqWinSize1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_MscTdmaBcRlp1Layer3L1ReqWinSize1_Type.__name__ = "Unsigned32"
_MscTdmaBcRlp1Layer3L1ReqWinSize1_Object = MibTableColumn
mscTdmaBcRlp1Layer3L1ReqWinSize1 = _MscTdmaBcRlp1Layer3L1ReqWinSize1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 7, 10, 1, 2),
    _MscTdmaBcRlp1Layer3L1ReqWinSize1_Type()
)
mscTdmaBcRlp1Layer3L1ReqWinSize1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcRlp1Layer3L1ReqWinSize1.setStatus("mandatory")


class _MscTdmaBcRlp1T1ResponseTimer_Type(Unsigned32):
    """Custom type mscTdmaBcRlp1T1ResponseTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_MscTdmaBcRlp1T1ResponseTimer_Type.__name__ = "Unsigned32"
_MscTdmaBcRlp1T1ResponseTimer_Object = MibTableColumn
mscTdmaBcRlp1T1ResponseTimer = _MscTdmaBcRlp1T1ResponseTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 7, 10, 1, 3),
    _MscTdmaBcRlp1T1ResponseTimer_Type()
)
mscTdmaBcRlp1T1ResponseTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcRlp1T1ResponseTimer.setStatus("mandatory")


class _MscTdmaBcRlp1T2LinkActivityTimer_Type(Unsigned32):
    """Custom type mscTdmaBcRlp1T2LinkActivityTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_MscTdmaBcRlp1T2LinkActivityTimer_Type.__name__ = "Unsigned32"
_MscTdmaBcRlp1T2LinkActivityTimer_Object = MibTableColumn
mscTdmaBcRlp1T2LinkActivityTimer = _MscTdmaBcRlp1T2LinkActivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 7, 10, 1, 4),
    _MscTdmaBcRlp1T2LinkActivityTimer_Type()
)
mscTdmaBcRlp1T2LinkActivityTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcRlp1T2LinkActivityTimer.setStatus("mandatory")


class _MscTdmaBcRlp1T3PeerAckTimer_Type(Unsigned32):
    """Custom type mscTdmaBcRlp1T3PeerAckTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_MscTdmaBcRlp1T3PeerAckTimer_Type.__name__ = "Unsigned32"
_MscTdmaBcRlp1T3PeerAckTimer_Object = MibTableColumn
mscTdmaBcRlp1T3PeerAckTimer = _MscTdmaBcRlp1T3PeerAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 7, 10, 1, 5),
    _MscTdmaBcRlp1T3PeerAckTimer_Type()
)
mscTdmaBcRlp1T3PeerAckTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcRlp1T3PeerAckTimer.setStatus("mandatory")
_MscTdmaBcRlp1StatsTable_Object = MibTable
mscTdmaBcRlp1StatsTable = _MscTdmaBcRlp1StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 7, 11)
)
if mibBuilder.loadTexts:
    mscTdmaBcRlp1StatsTable.setStatus("mandatory")
_MscTdmaBcRlp1StatsEntry_Object = MibTableRow
mscTdmaBcRlp1StatsEntry = _MscTdmaBcRlp1StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 7, 11, 1)
)
mscTdmaBcRlp1StatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcRlp1Index"),
)
if mibBuilder.loadTexts:
    mscTdmaBcRlp1StatsEntry.setStatus("mandatory")
_MscTdmaBcRlp1TxFrames_Type = Counter32
_MscTdmaBcRlp1TxFrames_Object = MibTableColumn
mscTdmaBcRlp1TxFrames = _MscTdmaBcRlp1TxFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 7, 11, 1, 1),
    _MscTdmaBcRlp1TxFrames_Type()
)
mscTdmaBcRlp1TxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcRlp1TxFrames.setStatus("mandatory")
_MscTdmaBcRlp1RxFrames_Type = Counter32
_MscTdmaBcRlp1RxFrames_Object = MibTableColumn
mscTdmaBcRlp1RxFrames = _MscTdmaBcRlp1RxFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 7, 11, 1, 2),
    _MscTdmaBcRlp1RxFrames_Type()
)
mscTdmaBcRlp1RxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcRlp1RxFrames.setStatus("mandatory")
_MscTdmaBcRlp1BadRxFrames_Type = Counter32
_MscTdmaBcRlp1BadRxFrames_Object = MibTableColumn
mscTdmaBcRlp1BadRxFrames = _MscTdmaBcRlp1BadRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 7, 11, 1, 3),
    _MscTdmaBcRlp1BadRxFrames_Type()
)
mscTdmaBcRlp1BadRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcRlp1BadRxFrames.setStatus("mandatory")
_MscTdmaBcV42_ObjectIdentity = ObjectIdentity
mscTdmaBcV42 = _MscTdmaBcV42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8)
)
_MscTdmaBcV42RowStatusTable_Object = MibTable
mscTdmaBcV42RowStatusTable = _MscTdmaBcV42RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 1)
)
if mibBuilder.loadTexts:
    mscTdmaBcV42RowStatusTable.setStatus("mandatory")
_MscTdmaBcV42RowStatusEntry_Object = MibTableRow
mscTdmaBcV42RowStatusEntry = _MscTdmaBcV42RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 1, 1)
)
mscTdmaBcV42RowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcV42Index"),
)
if mibBuilder.loadTexts:
    mscTdmaBcV42RowStatusEntry.setStatus("mandatory")
_MscTdmaBcV42RowStatus_Type = RowStatus
_MscTdmaBcV42RowStatus_Object = MibTableColumn
mscTdmaBcV42RowStatus = _MscTdmaBcV42RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 1, 1, 1),
    _MscTdmaBcV42RowStatus_Type()
)
mscTdmaBcV42RowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42RowStatus.setStatus("mandatory")
_MscTdmaBcV42ComponentName_Type = DisplayString
_MscTdmaBcV42ComponentName_Object = MibTableColumn
mscTdmaBcV42ComponentName = _MscTdmaBcV42ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 1, 1, 2),
    _MscTdmaBcV42ComponentName_Type()
)
mscTdmaBcV42ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42ComponentName.setStatus("mandatory")
_MscTdmaBcV42StorageType_Type = StorageType
_MscTdmaBcV42StorageType_Object = MibTableColumn
mscTdmaBcV42StorageType = _MscTdmaBcV42StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 1, 1, 4),
    _MscTdmaBcV42StorageType_Type()
)
mscTdmaBcV42StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42StorageType.setStatus("mandatory")
_MscTdmaBcV42Index_Type = NonReplicated
_MscTdmaBcV42Index_Object = MibTableColumn
mscTdmaBcV42Index = _MscTdmaBcV42Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 1, 1, 10),
    _MscTdmaBcV42Index_Type()
)
mscTdmaBcV42Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTdmaBcV42Index.setStatus("mandatory")
_MscTdmaBcV42OperTable_Object = MibTable
mscTdmaBcV42OperTable = _MscTdmaBcV42OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 10)
)
if mibBuilder.loadTexts:
    mscTdmaBcV42OperTable.setStatus("mandatory")
_MscTdmaBcV42OperEntry_Object = MibTableRow
mscTdmaBcV42OperEntry = _MscTdmaBcV42OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 10, 1)
)
mscTdmaBcV42OperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcV42Index"),
)
if mibBuilder.loadTexts:
    mscTdmaBcV42OperEntry.setStatus("mandatory")


class _MscTdmaBcV42ProtocolState_Type(Integer32):
    """Custom type mscTdmaBcV42ProtocolState based on Integer32"""
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


_MscTdmaBcV42ProtocolState_Type.__name__ = "Integer32"
_MscTdmaBcV42ProtocolState_Object = MibTableColumn
mscTdmaBcV42ProtocolState = _MscTdmaBcV42ProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 10, 1, 1),
    _MscTdmaBcV42ProtocolState_Type()
)
mscTdmaBcV42ProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42ProtocolState.setStatus("mandatory")


class _MscTdmaBcV42TxN401FrameSize_Type(Unsigned32):
    """Custom type mscTdmaBcV42TxN401FrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65355),
    )


_MscTdmaBcV42TxN401FrameSize_Type.__name__ = "Unsigned32"
_MscTdmaBcV42TxN401FrameSize_Object = MibTableColumn
mscTdmaBcV42TxN401FrameSize = _MscTdmaBcV42TxN401FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 10, 1, 2),
    _MscTdmaBcV42TxN401FrameSize_Type()
)
mscTdmaBcV42TxN401FrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42TxN401FrameSize.setStatus("mandatory")


class _MscTdmaBcV42RxN401FrameSize_Type(Unsigned32):
    """Custom type mscTdmaBcV42RxN401FrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscTdmaBcV42RxN401FrameSize_Type.__name__ = "Unsigned32"
_MscTdmaBcV42RxN401FrameSize_Object = MibTableColumn
mscTdmaBcV42RxN401FrameSize = _MscTdmaBcV42RxN401FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 10, 1, 3),
    _MscTdmaBcV42RxN401FrameSize_Type()
)
mscTdmaBcV42RxN401FrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42RxN401FrameSize.setStatus("mandatory")


class _MscTdmaBcV42TxKWindowSize_Type(Unsigned32):
    """Custom type mscTdmaBcV42TxKWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MscTdmaBcV42TxKWindowSize_Type.__name__ = "Unsigned32"
_MscTdmaBcV42TxKWindowSize_Object = MibTableColumn
mscTdmaBcV42TxKWindowSize = _MscTdmaBcV42TxKWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 10, 1, 4),
    _MscTdmaBcV42TxKWindowSize_Type()
)
mscTdmaBcV42TxKWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42TxKWindowSize.setStatus("mandatory")


class _MscTdmaBcV42RxKWindowSize_Type(Unsigned32):
    """Custom type mscTdmaBcV42RxKWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MscTdmaBcV42RxKWindowSize_Type.__name__ = "Unsigned32"
_MscTdmaBcV42RxKWindowSize_Object = MibTableColumn
mscTdmaBcV42RxKWindowSize = _MscTdmaBcV42RxKWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 10, 1, 5),
    _MscTdmaBcV42RxKWindowSize_Type()
)
mscTdmaBcV42RxKWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42RxKWindowSize.setStatus("mandatory")


class _MscTdmaBcV42V42ActiveInCall_Type(Integer32):
    """Custom type mscTdmaBcV42V42ActiveInCall based on Integer32"""
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


_MscTdmaBcV42V42ActiveInCall_Type.__name__ = "Integer32"
_MscTdmaBcV42V42ActiveInCall_Object = MibTableColumn
mscTdmaBcV42V42ActiveInCall = _MscTdmaBcV42V42ActiveInCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 10, 1, 6),
    _MscTdmaBcV42V42ActiveInCall_Type()
)
mscTdmaBcV42V42ActiveInCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42V42ActiveInCall.setStatus("mandatory")


class _MscTdmaBcV42V42BisActiveInCall_Type(Integer32):
    """Custom type mscTdmaBcV42V42BisActiveInCall based on Integer32"""
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


_MscTdmaBcV42V42BisActiveInCall_Type.__name__ = "Integer32"
_MscTdmaBcV42V42BisActiveInCall_Object = MibTableColumn
mscTdmaBcV42V42BisActiveInCall = _MscTdmaBcV42V42BisActiveInCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 10, 1, 7),
    _MscTdmaBcV42V42BisActiveInCall_Type()
)
mscTdmaBcV42V42BisActiveInCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42V42BisActiveInCall.setStatus("mandatory")
_MscTdmaBcV42StatsTable_Object = MibTable
mscTdmaBcV42StatsTable = _MscTdmaBcV42StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 11)
)
if mibBuilder.loadTexts:
    mscTdmaBcV42StatsTable.setStatus("mandatory")
_MscTdmaBcV42StatsEntry_Object = MibTableRow
mscTdmaBcV42StatsEntry = _MscTdmaBcV42StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 11, 1)
)
mscTdmaBcV42StatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcV42Index"),
)
if mibBuilder.loadTexts:
    mscTdmaBcV42StatsEntry.setStatus("mandatory")
_MscTdmaBcV42RxIBytes_Type = Counter32
_MscTdmaBcV42RxIBytes_Object = MibTableColumn
mscTdmaBcV42RxIBytes = _MscTdmaBcV42RxIBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 11, 1, 1),
    _MscTdmaBcV42RxIBytes_Type()
)
mscTdmaBcV42RxIBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42RxIBytes.setStatus("mandatory")
_MscTdmaBcV42TxIBytes_Type = Counter32
_MscTdmaBcV42TxIBytes_Object = MibTableColumn
mscTdmaBcV42TxIBytes = _MscTdmaBcV42TxIBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 11, 1, 2),
    _MscTdmaBcV42TxIBytes_Type()
)
mscTdmaBcV42TxIBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42TxIBytes.setStatus("mandatory")
_MscTdmaBcV42RxIFrames_Type = Counter32
_MscTdmaBcV42RxIFrames_Object = MibTableColumn
mscTdmaBcV42RxIFrames = _MscTdmaBcV42RxIFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 11, 1, 3),
    _MscTdmaBcV42RxIFrames_Type()
)
mscTdmaBcV42RxIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42RxIFrames.setStatus("mandatory")
_MscTdmaBcV42TxIFrames_Type = Counter32
_MscTdmaBcV42TxIFrames_Object = MibTableColumn
mscTdmaBcV42TxIFrames = _MscTdmaBcV42TxIFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 11, 1, 4),
    _MscTdmaBcV42TxIFrames_Type()
)
mscTdmaBcV42TxIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42TxIFrames.setStatus("mandatory")
_MscTdmaBcV42RetransmittedFrames_Type = Counter32
_MscTdmaBcV42RetransmittedFrames_Object = MibTableColumn
mscTdmaBcV42RetransmittedFrames = _MscTdmaBcV42RetransmittedFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 11, 1, 5),
    _MscTdmaBcV42RetransmittedFrames_Type()
)
mscTdmaBcV42RetransmittedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42RetransmittedFrames.setStatus("mandatory")
_MscTdmaBcV42T1AckTimeouts_Type = Counter32
_MscTdmaBcV42T1AckTimeouts_Object = MibTableColumn
mscTdmaBcV42T1AckTimeouts = _MscTdmaBcV42T1AckTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 11, 1, 6),
    _MscTdmaBcV42T1AckTimeouts_Type()
)
mscTdmaBcV42T1AckTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42T1AckTimeouts.setStatus("mandatory")
_MscTdmaBcV42RemoteBusyIndications_Type = Counter32
_MscTdmaBcV42RemoteBusyIndications_Object = MibTableColumn
mscTdmaBcV42RemoteBusyIndications = _MscTdmaBcV42RemoteBusyIndications_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 11, 1, 7),
    _MscTdmaBcV42RemoteBusyIndications_Type()
)
mscTdmaBcV42RemoteBusyIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42RemoteBusyIndications.setStatus("mandatory")
_MscTdmaBcV42LocalBusyIndications_Type = Counter32
_MscTdmaBcV42LocalBusyIndications_Object = MibTableColumn
mscTdmaBcV42LocalBusyIndications = _MscTdmaBcV42LocalBusyIndications_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 11, 1, 8),
    _MscTdmaBcV42LocalBusyIndications_Type()
)
mscTdmaBcV42LocalBusyIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42LocalBusyIndications.setStatus("mandatory")
_MscTdmaBcV42BadFramesRx_Type = Counter32
_MscTdmaBcV42BadFramesRx_Object = MibTableColumn
mscTdmaBcV42BadFramesRx = _MscTdmaBcV42BadFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 11, 1, 9),
    _MscTdmaBcV42BadFramesRx_Type()
)
mscTdmaBcV42BadFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42BadFramesRx.setStatus("mandatory")
_MscTdmaBcV42CrcErrorsRx_Type = Counter32
_MscTdmaBcV42CrcErrorsRx_Object = MibTableColumn
mscTdmaBcV42CrcErrorsRx = _MscTdmaBcV42CrcErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 8, 11, 1, 10),
    _MscTdmaBcV42CrcErrorsRx_Type()
)
mscTdmaBcV42CrcErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42CrcErrorsRx.setStatus("mandatory")
_MscTdmaBcV42Bis_ObjectIdentity = ObjectIdentity
mscTdmaBcV42Bis = _MscTdmaBcV42Bis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9)
)
_MscTdmaBcV42BisRowStatusTable_Object = MibTable
mscTdmaBcV42BisRowStatusTable = _MscTdmaBcV42BisRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9, 1)
)
if mibBuilder.loadTexts:
    mscTdmaBcV42BisRowStatusTable.setStatus("mandatory")
_MscTdmaBcV42BisRowStatusEntry_Object = MibTableRow
mscTdmaBcV42BisRowStatusEntry = _MscTdmaBcV42BisRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9, 1, 1)
)
mscTdmaBcV42BisRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcV42BisIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcV42BisRowStatusEntry.setStatus("mandatory")
_MscTdmaBcV42BisRowStatus_Type = RowStatus
_MscTdmaBcV42BisRowStatus_Object = MibTableColumn
mscTdmaBcV42BisRowStatus = _MscTdmaBcV42BisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9, 1, 1, 1),
    _MscTdmaBcV42BisRowStatus_Type()
)
mscTdmaBcV42BisRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42BisRowStatus.setStatus("mandatory")
_MscTdmaBcV42BisComponentName_Type = DisplayString
_MscTdmaBcV42BisComponentName_Object = MibTableColumn
mscTdmaBcV42BisComponentName = _MscTdmaBcV42BisComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9, 1, 1, 2),
    _MscTdmaBcV42BisComponentName_Type()
)
mscTdmaBcV42BisComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42BisComponentName.setStatus("mandatory")
_MscTdmaBcV42BisStorageType_Type = StorageType
_MscTdmaBcV42BisStorageType_Object = MibTableColumn
mscTdmaBcV42BisStorageType = _MscTdmaBcV42BisStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9, 1, 1, 4),
    _MscTdmaBcV42BisStorageType_Type()
)
mscTdmaBcV42BisStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42BisStorageType.setStatus("mandatory")
_MscTdmaBcV42BisIndex_Type = NonReplicated
_MscTdmaBcV42BisIndex_Object = MibTableColumn
mscTdmaBcV42BisIndex = _MscTdmaBcV42BisIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9, 1, 1, 10),
    _MscTdmaBcV42BisIndex_Type()
)
mscTdmaBcV42BisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTdmaBcV42BisIndex.setStatus("mandatory")
_MscTdmaBcV42BisOperTable_Object = MibTable
mscTdmaBcV42BisOperTable = _MscTdmaBcV42BisOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9, 10)
)
if mibBuilder.loadTexts:
    mscTdmaBcV42BisOperTable.setStatus("mandatory")
_MscTdmaBcV42BisOperEntry_Object = MibTableRow
mscTdmaBcV42BisOperEntry = _MscTdmaBcV42BisOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9, 10, 1)
)
mscTdmaBcV42BisOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcV42BisIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcV42BisOperEntry.setStatus("mandatory")


class _MscTdmaBcV42BisProtocolModeEncoder_Type(Integer32):
    """Custom type mscTdmaBcV42BisProtocolModeEncoder based on Integer32"""
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


_MscTdmaBcV42BisProtocolModeEncoder_Type.__name__ = "Integer32"
_MscTdmaBcV42BisProtocolModeEncoder_Object = MibTableColumn
mscTdmaBcV42BisProtocolModeEncoder = _MscTdmaBcV42BisProtocolModeEncoder_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9, 10, 1, 1),
    _MscTdmaBcV42BisProtocolModeEncoder_Type()
)
mscTdmaBcV42BisProtocolModeEncoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42BisProtocolModeEncoder.setStatus("mandatory")


class _MscTdmaBcV42BisProtocolModeDecoder_Type(Integer32):
    """Custom type mscTdmaBcV42BisProtocolModeDecoder based on Integer32"""
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


_MscTdmaBcV42BisProtocolModeDecoder_Type.__name__ = "Integer32"
_MscTdmaBcV42BisProtocolModeDecoder_Object = MibTableColumn
mscTdmaBcV42BisProtocolModeDecoder = _MscTdmaBcV42BisProtocolModeDecoder_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9, 10, 1, 2),
    _MscTdmaBcV42BisProtocolModeDecoder_Type()
)
mscTdmaBcV42BisProtocolModeDecoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42BisProtocolModeDecoder.setStatus("mandatory")


class _MscTdmaBcV42BisP0CompressionDirection_Type(Integer32):
    """Custom type mscTdmaBcV42BisP0CompressionDirection based on Integer32"""
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


_MscTdmaBcV42BisP0CompressionDirection_Type.__name__ = "Integer32"
_MscTdmaBcV42BisP0CompressionDirection_Object = MibTableColumn
mscTdmaBcV42BisP0CompressionDirection = _MscTdmaBcV42BisP0CompressionDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9, 10, 1, 3),
    _MscTdmaBcV42BisP0CompressionDirection_Type()
)
mscTdmaBcV42BisP0CompressionDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42BisP0CompressionDirection.setStatus("mandatory")


class _MscTdmaBcV42BisP1MaximumCodewords_Type(Unsigned32):
    """Custom type mscTdmaBcV42BisP1MaximumCodewords based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscTdmaBcV42BisP1MaximumCodewords_Type.__name__ = "Unsigned32"
_MscTdmaBcV42BisP1MaximumCodewords_Object = MibTableColumn
mscTdmaBcV42BisP1MaximumCodewords = _MscTdmaBcV42BisP1MaximumCodewords_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9, 10, 1, 4),
    _MscTdmaBcV42BisP1MaximumCodewords_Type()
)
mscTdmaBcV42BisP1MaximumCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42BisP1MaximumCodewords.setStatus("mandatory")


class _MscTdmaBcV42BisP2MaximumStringSize_Type(Unsigned32):
    """Custom type mscTdmaBcV42BisP2MaximumStringSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 250),
    )


_MscTdmaBcV42BisP2MaximumStringSize_Type.__name__ = "Unsigned32"
_MscTdmaBcV42BisP2MaximumStringSize_Object = MibTableColumn
mscTdmaBcV42BisP2MaximumStringSize = _MscTdmaBcV42BisP2MaximumStringSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9, 10, 1, 5),
    _MscTdmaBcV42BisP2MaximumStringSize_Type()
)
mscTdmaBcV42BisP2MaximumStringSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42BisP2MaximumStringSize.setStatus("mandatory")


class _MscTdmaBcV42BisLastDecodeError_Type(Integer32):
    """Custom type mscTdmaBcV42BisLastDecodeError based on Integer32"""
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


_MscTdmaBcV42BisLastDecodeError_Type.__name__ = "Integer32"
_MscTdmaBcV42BisLastDecodeError_Object = MibTableColumn
mscTdmaBcV42BisLastDecodeError = _MscTdmaBcV42BisLastDecodeError_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9, 10, 1, 6),
    _MscTdmaBcV42BisLastDecodeError_Type()
)
mscTdmaBcV42BisLastDecodeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42BisLastDecodeError.setStatus("mandatory")


class _MscTdmaBcV42BisCompRatioEncoder_Type(FixedPoint2):
    """Custom type mscTdmaBcV42BisCompRatioEncoder based on FixedPoint2"""
    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_MscTdmaBcV42BisCompRatioEncoder_Type.__name__ = "FixedPoint2"
_MscTdmaBcV42BisCompRatioEncoder_Object = MibTableColumn
mscTdmaBcV42BisCompRatioEncoder = _MscTdmaBcV42BisCompRatioEncoder_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9, 10, 1, 7),
    _MscTdmaBcV42BisCompRatioEncoder_Type()
)
mscTdmaBcV42BisCompRatioEncoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42BisCompRatioEncoder.setStatus("mandatory")


class _MscTdmaBcV42BisCompRatioDecoder_Type(FixedPoint2):
    """Custom type mscTdmaBcV42BisCompRatioDecoder based on FixedPoint2"""
    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_MscTdmaBcV42BisCompRatioDecoder_Type.__name__ = "FixedPoint2"
_MscTdmaBcV42BisCompRatioDecoder_Object = MibTableColumn
mscTdmaBcV42BisCompRatioDecoder = _MscTdmaBcV42BisCompRatioDecoder_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9, 10, 1, 8),
    _MscTdmaBcV42BisCompRatioDecoder_Type()
)
mscTdmaBcV42BisCompRatioDecoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42BisCompRatioDecoder.setStatus("mandatory")
_MscTdmaBcV42BisStatsTable_Object = MibTable
mscTdmaBcV42BisStatsTable = _MscTdmaBcV42BisStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9, 11)
)
if mibBuilder.loadTexts:
    mscTdmaBcV42BisStatsTable.setStatus("mandatory")
_MscTdmaBcV42BisStatsEntry_Object = MibTableRow
mscTdmaBcV42BisStatsEntry = _MscTdmaBcV42BisStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9, 11, 1)
)
mscTdmaBcV42BisStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcV42BisIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcV42BisStatsEntry.setStatus("mandatory")
_MscTdmaBcV42BisModeChangesEncode_Type = Counter32
_MscTdmaBcV42BisModeChangesEncode_Object = MibTableColumn
mscTdmaBcV42BisModeChangesEncode = _MscTdmaBcV42BisModeChangesEncode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9, 11, 1, 1),
    _MscTdmaBcV42BisModeChangesEncode_Type()
)
mscTdmaBcV42BisModeChangesEncode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42BisModeChangesEncode.setStatus("mandatory")
_MscTdmaBcV42BisModeChangesDecode_Type = Counter32
_MscTdmaBcV42BisModeChangesDecode_Object = MibTableColumn
mscTdmaBcV42BisModeChangesDecode = _MscTdmaBcV42BisModeChangesDecode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9, 11, 1, 2),
    _MscTdmaBcV42BisModeChangesDecode_Type()
)
mscTdmaBcV42BisModeChangesDecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42BisModeChangesDecode.setStatus("mandatory")
_MscTdmaBcV42BisResetsEncode_Type = Counter32
_MscTdmaBcV42BisResetsEncode_Object = MibTableColumn
mscTdmaBcV42BisResetsEncode = _MscTdmaBcV42BisResetsEncode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9, 11, 1, 3),
    _MscTdmaBcV42BisResetsEncode_Type()
)
mscTdmaBcV42BisResetsEncode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42BisResetsEncode.setStatus("mandatory")
_MscTdmaBcV42BisResetsDecode_Type = Counter32
_MscTdmaBcV42BisResetsDecode_Object = MibTableColumn
mscTdmaBcV42BisResetsDecode = _MscTdmaBcV42BisResetsDecode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9, 11, 1, 4),
    _MscTdmaBcV42BisResetsDecode_Type()
)
mscTdmaBcV42BisResetsDecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42BisResetsDecode.setStatus("mandatory")
_MscTdmaBcV42BisReinitializations_Type = Counter32
_MscTdmaBcV42BisReinitializations_Object = MibTableColumn
mscTdmaBcV42BisReinitializations = _MscTdmaBcV42BisReinitializations_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9, 11, 1, 5),
    _MscTdmaBcV42BisReinitializations_Type()
)
mscTdmaBcV42BisReinitializations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42BisReinitializations.setStatus("mandatory")
_MscTdmaBcV42BisErrorsInDecode_Type = Counter32
_MscTdmaBcV42BisErrorsInDecode_Object = MibTableColumn
mscTdmaBcV42BisErrorsInDecode = _MscTdmaBcV42BisErrorsInDecode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 9, 11, 1, 6),
    _MscTdmaBcV42BisErrorsInDecode_Type()
)
mscTdmaBcV42BisErrorsInDecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcV42BisErrorsInDecode.setStatus("mandatory")
_MscTdmaBcUr_ObjectIdentity = ObjectIdentity
mscTdmaBcUr = _MscTdmaBcUr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 10)
)
_MscTdmaBcUrRowStatusTable_Object = MibTable
mscTdmaBcUrRowStatusTable = _MscTdmaBcUrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 10, 1)
)
if mibBuilder.loadTexts:
    mscTdmaBcUrRowStatusTable.setStatus("mandatory")
_MscTdmaBcUrRowStatusEntry_Object = MibTableRow
mscTdmaBcUrRowStatusEntry = _MscTdmaBcUrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 10, 1, 1)
)
mscTdmaBcUrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcUrIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcUrRowStatusEntry.setStatus("mandatory")
_MscTdmaBcUrRowStatus_Type = RowStatus
_MscTdmaBcUrRowStatus_Object = MibTableColumn
mscTdmaBcUrRowStatus = _MscTdmaBcUrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 10, 1, 1, 1),
    _MscTdmaBcUrRowStatus_Type()
)
mscTdmaBcUrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcUrRowStatus.setStatus("mandatory")
_MscTdmaBcUrComponentName_Type = DisplayString
_MscTdmaBcUrComponentName_Object = MibTableColumn
mscTdmaBcUrComponentName = _MscTdmaBcUrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 10, 1, 1, 2),
    _MscTdmaBcUrComponentName_Type()
)
mscTdmaBcUrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcUrComponentName.setStatus("mandatory")
_MscTdmaBcUrStorageType_Type = StorageType
_MscTdmaBcUrStorageType_Object = MibTableColumn
mscTdmaBcUrStorageType = _MscTdmaBcUrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 10, 1, 1, 4),
    _MscTdmaBcUrStorageType_Type()
)
mscTdmaBcUrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcUrStorageType.setStatus("mandatory")
_MscTdmaBcUrIndex_Type = NonReplicated
_MscTdmaBcUrIndex_Object = MibTableColumn
mscTdmaBcUrIndex = _MscTdmaBcUrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 10, 1, 1, 10),
    _MscTdmaBcUrIndex_Type()
)
mscTdmaBcUrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTdmaBcUrIndex.setStatus("mandatory")
_MscTdmaBcUrOperTable_Object = MibTable
mscTdmaBcUrOperTable = _MscTdmaBcUrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 10, 10)
)
if mibBuilder.loadTexts:
    mscTdmaBcUrOperTable.setStatus("mandatory")
_MscTdmaBcUrOperEntry_Object = MibTableRow
mscTdmaBcUrOperEntry = _MscTdmaBcUrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 10, 10, 1)
)
mscTdmaBcUrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcUrIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcUrOperEntry.setStatus("mandatory")


class _MscTdmaBcUrRxBufferSize_Type(Unsigned32):
    """Custom type mscTdmaBcUrRxBufferSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscTdmaBcUrRxBufferSize_Type.__name__ = "Unsigned32"
_MscTdmaBcUrRxBufferSize_Object = MibTableColumn
mscTdmaBcUrRxBufferSize = _MscTdmaBcUrRxBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 10, 10, 1, 1),
    _MscTdmaBcUrRxBufferSize_Type()
)
mscTdmaBcUrRxBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcUrRxBufferSize.setStatus("mandatory")


class _MscTdmaBcUrTxFlowControlState_Type(Integer32):
    """Custom type mscTdmaBcUrTxFlowControlState based on Integer32"""
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


_MscTdmaBcUrTxFlowControlState_Type.__name__ = "Integer32"
_MscTdmaBcUrTxFlowControlState_Object = MibTableColumn
mscTdmaBcUrTxFlowControlState = _MscTdmaBcUrTxFlowControlState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 10, 10, 1, 2),
    _MscTdmaBcUrTxFlowControlState_Type()
)
mscTdmaBcUrTxFlowControlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcUrTxFlowControlState.setStatus("mandatory")


class _MscTdmaBcUrRxFlowControlState_Type(Integer32):
    """Custom type mscTdmaBcUrRxFlowControlState based on Integer32"""
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


_MscTdmaBcUrRxFlowControlState_Type.__name__ = "Integer32"
_MscTdmaBcUrRxFlowControlState_Object = MibTableColumn
mscTdmaBcUrRxFlowControlState = _MscTdmaBcUrRxFlowControlState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 10, 10, 1, 3),
    _MscTdmaBcUrRxFlowControlState_Type()
)
mscTdmaBcUrRxFlowControlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcUrRxFlowControlState.setStatus("mandatory")
_MscTdmaBcUrStatsTable_Object = MibTable
mscTdmaBcUrStatsTable = _MscTdmaBcUrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 10, 11)
)
if mibBuilder.loadTexts:
    mscTdmaBcUrStatsTable.setStatus("mandatory")
_MscTdmaBcUrStatsEntry_Object = MibTableRow
mscTdmaBcUrStatsEntry = _MscTdmaBcUrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 10, 11, 1)
)
mscTdmaBcUrStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcUrIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcUrStatsEntry.setStatus("mandatory")
_MscTdmaBcUrTxFrames_Type = Counter32
_MscTdmaBcUrTxFrames_Object = MibTableColumn
mscTdmaBcUrTxFrames = _MscTdmaBcUrTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 10, 11, 1, 1),
    _MscTdmaBcUrTxFrames_Type()
)
mscTdmaBcUrTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcUrTxFrames.setStatus("mandatory")
_MscTdmaBcUrRxFrames_Type = Counter32
_MscTdmaBcUrRxFrames_Object = MibTableColumn
mscTdmaBcUrRxFrames = _MscTdmaBcUrRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 10, 11, 1, 2),
    _MscTdmaBcUrRxFrames_Type()
)
mscTdmaBcUrRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcUrRxFrames.setStatus("mandatory")
_MscTdmaBcUrUnacknowledgedFrames_Type = Counter32
_MscTdmaBcUrUnacknowledgedFrames_Object = MibTableColumn
mscTdmaBcUrUnacknowledgedFrames = _MscTdmaBcUrUnacknowledgedFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 10, 11, 1, 3),
    _MscTdmaBcUrUnacknowledgedFrames_Type()
)
mscTdmaBcUrUnacknowledgedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcUrUnacknowledgedFrames.setStatus("mandatory")
_MscTdmaBcUrCumUnacknowledgedFrames_Type = Counter32
_MscTdmaBcUrCumUnacknowledgedFrames_Object = MibTableColumn
mscTdmaBcUrCumUnacknowledgedFrames = _MscTdmaBcUrCumUnacknowledgedFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 10, 11, 1, 4),
    _MscTdmaBcUrCumUnacknowledgedFrames_Type()
)
mscTdmaBcUrCumUnacknowledgedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcUrCumUnacknowledgedFrames.setStatus("mandatory")
_MscTdmaBcOperTable_Object = MibTable
mscTdmaBcOperTable = _MscTdmaBcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 101)
)
if mibBuilder.loadTexts:
    mscTdmaBcOperTable.setStatus("mandatory")
_MscTdmaBcOperEntry_Object = MibTableRow
mscTdmaBcOperEntry = _MscTdmaBcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 101, 1)
)
mscTdmaBcOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcOperEntry.setStatus("mandatory")


class _MscTdmaBcState_Type(Integer32):
    """Custom type mscTdmaBcState based on Integer32"""
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


_MscTdmaBcState_Type.__name__ = "Integer32"
_MscTdmaBcState_Object = MibTableColumn
mscTdmaBcState = _MscTdmaBcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 101, 1, 1),
    _MscTdmaBcState_Type()
)
mscTdmaBcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcState.setStatus("mandatory")


class _MscTdmaBcCallType_Type(Integer32):
    """Custom type mscTdmaBcCallType based on Integer32"""
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


_MscTdmaBcCallType_Type.__name__ = "Integer32"
_MscTdmaBcCallType_Object = MibTableColumn
mscTdmaBcCallType = _MscTdmaBcCallType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 101, 1, 2),
    _MscTdmaBcCallType_Type()
)
mscTdmaBcCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcCallType.setStatus("mandatory")


class _MscTdmaBcLastResponseCode_Type(Integer32):
    """Custom type mscTdmaBcLastResponseCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              16,
              17,
              18,
              19,
              28,
              31,
              41,
              44,
              47,
              49,
              63,
              79,
              81,
              82,
              95,
              96,
              97,
              98,
              102,
              111)
        )
    )
    namedValues = NamedValues(
        *(("channelUnavailable", 44),
          ("incompatibleMessage", 98),
          ("invalidCallRefValue", 81),
          ("invalidChannel", 82),
          ("invalidMessageType", 97),
          ("invalidNumberFormat", 28),
          ("missingMandatoryIe", 96),
          ("noCause", 0),
          ("noResponse", 18),
          ("noRouteToDest", 3),
          ("normalClearing", 16),
          ("qosUnavailable", 49),
          ("resourceUnavailable", 47),
          ("serviceUnavailable", 63),
          ("temporaryFailure", 41),
          ("timerRecovery", 102),
          ("unassignedNumber", 1),
          ("unimplementedOption", 79),
          ("unspecInvalidMessage", 95),
          ("unspecNormal", 31),
          ("unspecProtocolError", 111),
          ("userBusy", 17),
          ("userNoAnswer", 19))
    )


_MscTdmaBcLastResponseCode_Type.__name__ = "Integer32"
_MscTdmaBcLastResponseCode_Object = MibTableColumn
mscTdmaBcLastResponseCode = _MscTdmaBcLastResponseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 101, 1, 3),
    _MscTdmaBcLastResponseCode_Type()
)
mscTdmaBcLastResponseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcLastResponseCode.setStatus("mandatory")
_MscTdmaBcMateBearerChannel_Type = RowPointer
_MscTdmaBcMateBearerChannel_Object = MibTableColumn
mscTdmaBcMateBearerChannel = _MscTdmaBcMateBearerChannel_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 101, 1, 4),
    _MscTdmaBcMateBearerChannel_Type()
)
mscTdmaBcMateBearerChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcMateBearerChannel.setStatus("mandatory")
_MscTdmaBcCidDataTable_Object = MibTable
mscTdmaBcCidDataTable = _MscTdmaBcCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 103)
)
if mibBuilder.loadTexts:
    mscTdmaBcCidDataTable.setStatus("mandatory")
_MscTdmaBcCidDataEntry_Object = MibTableRow
mscTdmaBcCidDataEntry = _MscTdmaBcCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 103, 1)
)
mscTdmaBcCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcCidDataEntry.setStatus("mandatory")


class _MscTdmaBcCustomerIdentifier_Type(Unsigned32):
    """Custom type mscTdmaBcCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscTdmaBcCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscTdmaBcCustomerIdentifier_Object = MibTableColumn
mscTdmaBcCustomerIdentifier = _MscTdmaBcCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 103, 1, 1),
    _MscTdmaBcCustomerIdentifier_Type()
)
mscTdmaBcCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTdmaBcCustomerIdentifier.setStatus("mandatory")
_MscTdmaBcStateTable_Object = MibTable
mscTdmaBcStateTable = _MscTdmaBcStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 104)
)
if mibBuilder.loadTexts:
    mscTdmaBcStateTable.setStatus("mandatory")
_MscTdmaBcStateEntry_Object = MibTableRow
mscTdmaBcStateEntry = _MscTdmaBcStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 104, 1)
)
mscTdmaBcStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TdmaIwfMIB", "mscTdmaBcBcIndex"),
)
if mibBuilder.loadTexts:
    mscTdmaBcStateEntry.setStatus("mandatory")


class _MscTdmaBcAdminState_Type(Integer32):
    """Custom type mscTdmaBcAdminState based on Integer32"""
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


_MscTdmaBcAdminState_Type.__name__ = "Integer32"
_MscTdmaBcAdminState_Object = MibTableColumn
mscTdmaBcAdminState = _MscTdmaBcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 104, 1, 1),
    _MscTdmaBcAdminState_Type()
)
mscTdmaBcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcAdminState.setStatus("mandatory")


class _MscTdmaBcOperationalState_Type(Integer32):
    """Custom type mscTdmaBcOperationalState based on Integer32"""
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


_MscTdmaBcOperationalState_Type.__name__ = "Integer32"
_MscTdmaBcOperationalState_Object = MibTableColumn
mscTdmaBcOperationalState = _MscTdmaBcOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 104, 1, 2),
    _MscTdmaBcOperationalState_Type()
)
mscTdmaBcOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcOperationalState.setStatus("mandatory")


class _MscTdmaBcUsageState_Type(Integer32):
    """Custom type mscTdmaBcUsageState based on Integer32"""
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


_MscTdmaBcUsageState_Type.__name__ = "Integer32"
_MscTdmaBcUsageState_Object = MibTableColumn
mscTdmaBcUsageState = _MscTdmaBcUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 136, 104, 1, 3),
    _MscTdmaBcUsageState_Type()
)
mscTdmaBcUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTdmaBcUsageState.setStatus("mandatory")
_TdmaIwfMIB_ObjectIdentity = ObjectIdentity
tdmaIwfMIB = _TdmaIwfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 140)
)
_TdmaIwfGroup_ObjectIdentity = ObjectIdentity
tdmaIwfGroup = _TdmaIwfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 140, 1)
)
_TdmaIwfGroupCA_ObjectIdentity = ObjectIdentity
tdmaIwfGroupCA = _TdmaIwfGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 140, 1, 1)
)
_TdmaIwfGroupCA02_ObjectIdentity = ObjectIdentity
tdmaIwfGroupCA02 = _TdmaIwfGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 140, 1, 1, 3)
)
_TdmaIwfGroupCA02A_ObjectIdentity = ObjectIdentity
tdmaIwfGroupCA02A = _TdmaIwfGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 140, 1, 1, 3, 2)
)
_TdmaIwfCapabilities_ObjectIdentity = ObjectIdentity
tdmaIwfCapabilities = _TdmaIwfCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 140, 3)
)
_TdmaIwfCapabilitiesCA_ObjectIdentity = ObjectIdentity
tdmaIwfCapabilitiesCA = _TdmaIwfCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 140, 3, 1)
)
_TdmaIwfCapabilitiesCA02_ObjectIdentity = ObjectIdentity
tdmaIwfCapabilitiesCA02 = _TdmaIwfCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 140, 3, 1, 3)
)
_TdmaIwfCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
tdmaIwfCapabilitiesCA02A = _TdmaIwfCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 140, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-TdmaIwfMIB",
    **{"mscTdmaCs": mscTdmaCs,
       "mscTdmaCsRowStatusTable": mscTdmaCsRowStatusTable,
       "mscTdmaCsRowStatusEntry": mscTdmaCsRowStatusEntry,
       "mscTdmaCsRowStatus": mscTdmaCsRowStatus,
       "mscTdmaCsComponentName": mscTdmaCsComponentName,
       "mscTdmaCsStorageType": mscTdmaCsStorageType,
       "mscTdmaCsCsIndex": mscTdmaCsCsIndex,
       "mscTdmaCsModem": mscTdmaCsModem,
       "mscTdmaCsModemRowStatusTable": mscTdmaCsModemRowStatusTable,
       "mscTdmaCsModemRowStatusEntry": mscTdmaCsModemRowStatusEntry,
       "mscTdmaCsModemRowStatus": mscTdmaCsModemRowStatus,
       "mscTdmaCsModemComponentName": mscTdmaCsModemComponentName,
       "mscTdmaCsModemStorageType": mscTdmaCsModemStorageType,
       "mscTdmaCsModemIndex": mscTdmaCsModemIndex,
       "mscTdmaCsFax": mscTdmaCsFax,
       "mscTdmaCsFaxRowStatusTable": mscTdmaCsFaxRowStatusTable,
       "mscTdmaCsFaxRowStatusEntry": mscTdmaCsFaxRowStatusEntry,
       "mscTdmaCsFaxRowStatus": mscTdmaCsFaxRowStatus,
       "mscTdmaCsFaxComponentName": mscTdmaCsFaxComponentName,
       "mscTdmaCsFaxStorageType": mscTdmaCsFaxStorageType,
       "mscTdmaCsFaxIndex": mscTdmaCsFaxIndex,
       "mscTdmaCsDce": mscTdmaCsDce,
       "mscTdmaCsDceRowStatusTable": mscTdmaCsDceRowStatusTable,
       "mscTdmaCsDceRowStatusEntry": mscTdmaCsDceRowStatusEntry,
       "mscTdmaCsDceRowStatus": mscTdmaCsDceRowStatus,
       "mscTdmaCsDceComponentName": mscTdmaCsDceComponentName,
       "mscTdmaCsDceStorageType": mscTdmaCsDceStorageType,
       "mscTdmaCsDceIndex": mscTdmaCsDceIndex,
       "mscTdmaCsDsc": mscTdmaCsDsc,
       "mscTdmaCsDscRowStatusTable": mscTdmaCsDscRowStatusTable,
       "mscTdmaCsDscRowStatusEntry": mscTdmaCsDscRowStatusEntry,
       "mscTdmaCsDscRowStatus": mscTdmaCsDscRowStatus,
       "mscTdmaCsDscComponentName": mscTdmaCsDscComponentName,
       "mscTdmaCsDscStorageType": mscTdmaCsDscStorageType,
       "mscTdmaCsDscIndex": mscTdmaCsDscIndex,
       "mscTdmaCsDscProvTable": mscTdmaCsDscProvTable,
       "mscTdmaCsDscProvEntry": mscTdmaCsDscProvEntry,
       "mscTdmaCsDscLl0BufferSize": mscTdmaCsDscLl0BufferSize,
       "mscTdmaCsDscLl1BufferSize": mscTdmaCsDscLl1BufferSize,
       "mscTdmaCsDscK0Ll0WindowSize": mscTdmaCsDscK0Ll0WindowSize,
       "mscTdmaCsDscK1Ll1WindowSize": mscTdmaCsDscK1Ll1WindowSize,
       "mscTdmaCsDscP0CompressionDirection": mscTdmaCsDscP0CompressionDirection,
       "mscTdmaCsDscP1CompressionMaximumCodewords": mscTdmaCsDscP1CompressionMaximumCodewords,
       "mscTdmaCsDscP2CompressionMaximumCharacters": mscTdmaCsDscP2CompressionMaximumCharacters,
       "mscTdmaCsRlp1": mscTdmaCsRlp1,
       "mscTdmaCsRlp1RowStatusTable": mscTdmaCsRlp1RowStatusTable,
       "mscTdmaCsRlp1RowStatusEntry": mscTdmaCsRlp1RowStatusEntry,
       "mscTdmaCsRlp1RowStatus": mscTdmaCsRlp1RowStatus,
       "mscTdmaCsRlp1ComponentName": mscTdmaCsRlp1ComponentName,
       "mscTdmaCsRlp1StorageType": mscTdmaCsRlp1StorageType,
       "mscTdmaCsRlp1Index": mscTdmaCsRlp1Index,
       "mscTdmaCsRlp1ProvTable": mscTdmaCsRlp1ProvTable,
       "mscTdmaCsRlp1ProvEntry": mscTdmaCsRlp1ProvEntry,
       "mscTdmaCsRlp1T1ResponseTimer": mscTdmaCsRlp1T1ResponseTimer,
       "mscTdmaCsRlp1T2LinkActivityTimer": mscTdmaCsRlp1T2LinkActivityTimer,
       "mscTdmaCsRlp1T3PeerAckTimer": mscTdmaCsRlp1T3PeerAckTimer,
       "mscTdmaCsV42": mscTdmaCsV42,
       "mscTdmaCsV42RowStatusTable": mscTdmaCsV42RowStatusTable,
       "mscTdmaCsV42RowStatusEntry": mscTdmaCsV42RowStatusEntry,
       "mscTdmaCsV42RowStatus": mscTdmaCsV42RowStatus,
       "mscTdmaCsV42ComponentName": mscTdmaCsV42ComponentName,
       "mscTdmaCsV42StorageType": mscTdmaCsV42StorageType,
       "mscTdmaCsV42Index": mscTdmaCsV42Index,
       "mscTdmaCsV42ProvTable": mscTdmaCsV42ProvTable,
       "mscTdmaCsV42ProvEntry": mscTdmaCsV42ProvEntry,
       "mscTdmaCsV42T400DetectTimer": mscTdmaCsV42T400DetectTimer,
       "mscTdmaCsV42T401AckTimer": mscTdmaCsV42T401AckTimer,
       "mscTdmaCsV42T402AckDelayTimer": mscTdmaCsV42T402AckDelayTimer,
       "mscTdmaCsV42T403IdleProbeTimer": mscTdmaCsV42T403IdleProbeTimer,
       "mscTdmaCsV42TxN401FrameSize": mscTdmaCsV42TxN401FrameSize,
       "mscTdmaCsV42RxN401FrameSize": mscTdmaCsV42RxN401FrameSize,
       "mscTdmaCsV42TxKWindowSize": mscTdmaCsV42TxKWindowSize,
       "mscTdmaCsV42RxKWindowSize": mscTdmaCsV42RxKWindowSize,
       "mscTdmaCsV42N400RetransLimit": mscTdmaCsV42N400RetransLimit,
       "mscTdmaCsV42FcsLength": mscTdmaCsV42FcsLength,
       "mscTdmaCsV42Bis": mscTdmaCsV42Bis,
       "mscTdmaCsV42BisRowStatusTable": mscTdmaCsV42BisRowStatusTable,
       "mscTdmaCsV42BisRowStatusEntry": mscTdmaCsV42BisRowStatusEntry,
       "mscTdmaCsV42BisRowStatus": mscTdmaCsV42BisRowStatus,
       "mscTdmaCsV42BisComponentName": mscTdmaCsV42BisComponentName,
       "mscTdmaCsV42BisStorageType": mscTdmaCsV42BisStorageType,
       "mscTdmaCsV42BisIndex": mscTdmaCsV42BisIndex,
       "mscTdmaCsV42BisProvTable": mscTdmaCsV42BisProvTable,
       "mscTdmaCsV42BisProvEntry": mscTdmaCsV42BisProvEntry,
       "mscTdmaCsV42BisP0CompressionDirection": mscTdmaCsV42BisP0CompressionDirection,
       "mscTdmaCsV42BisP1MaximumCodewords": mscTdmaCsV42BisP1MaximumCodewords,
       "mscTdmaCsV42BisP2MaximumStringSize": mscTdmaCsV42BisP2MaximumStringSize,
       "mscTdmaCsV42BisActionOnError": mscTdmaCsV42BisActionOnError,
       "mscTdmaCsLp": mscTdmaCsLp,
       "mscTdmaCsLpRowStatusTable": mscTdmaCsLpRowStatusTable,
       "mscTdmaCsLpRowStatusEntry": mscTdmaCsLpRowStatusEntry,
       "mscTdmaCsLpRowStatus": mscTdmaCsLpRowStatus,
       "mscTdmaCsLpComponentName": mscTdmaCsLpComponentName,
       "mscTdmaCsLpStorageType": mscTdmaCsLpStorageType,
       "mscTdmaCsLpIndex": mscTdmaCsLpIndex,
       "mscTdmaCsLpOperTable": mscTdmaCsLpOperTable,
       "mscTdmaCsLpOperEntry": mscTdmaCsLpOperEntry,
       "mscTdmaCsLpConfiguredBearerChannels": mscTdmaCsLpConfiguredBearerChannels,
       "mscTdmaCsLpActiveCalls": mscTdmaCsLpActiveCalls,
       "mscTdmaCsLpModemsSupported": mscTdmaCsLpModemsSupported,
       "mscTdmaCsServProvTable": mscTdmaCsServProvTable,
       "mscTdmaCsServProvEntry": mscTdmaCsServProvEntry,
       "mscTdmaCsTIwf1": mscTdmaCsTIwf1,
       "mscTdmaCsTIwf2": mscTdmaCsTIwf2,
       "mscTdmaCsT303": mscTdmaCsT303,
       "mscTdmaCsT305": mscTdmaCsT305,
       "mscTdmaCsT308": mscTdmaCsT308,
       "mscTdmaCsT313": mscTdmaCsT313,
       "mscTdmaCsT999": mscTdmaCsT999,
       "mscTdmaCsSupportedTechnology": mscTdmaCsSupportedTechnology,
       "mscTdmaCsSupportedService": mscTdmaCsSupportedService,
       "mscTdmaCsMiscProvTable": mscTdmaCsMiscProvTable,
       "mscTdmaCsMiscProvEntry": mscTdmaCsMiscProvEntry,
       "mscTdmaCsCommentText": mscTdmaCsCommentText,
       "mscTdmaCsMscIpAddress": mscTdmaCsMscIpAddress,
       "mscTdmaCsVirtualRouterName": mscTdmaCsVirtualRouterName,
       "mscTdmaCsVoiceLaw": mscTdmaCsVoiceLaw,
       "mscTdmaCsCidDataTable": mscTdmaCsCidDataTable,
       "mscTdmaCsCidDataEntry": mscTdmaCsCidDataEntry,
       "mscTdmaCsCustomerIdentifier": mscTdmaCsCustomerIdentifier,
       "mscTdmaCsStateTable": mscTdmaCsStateTable,
       "mscTdmaCsStateEntry": mscTdmaCsStateEntry,
       "mscTdmaCsAdminState": mscTdmaCsAdminState,
       "mscTdmaCsOperationalState": mscTdmaCsOperationalState,
       "mscTdmaCsUsageState": mscTdmaCsUsageState,
       "mscTdmaCsStatsTable": mscTdmaCsStatsTable,
       "mscTdmaCsStatsEntry": mscTdmaCsStatsEntry,
       "mscTdmaCsCurrentCalls": mscTdmaCsCurrentCalls,
       "mscTdmaCsCallsRequested": mscTdmaCsCallsRequested,
       "mscTdmaCsCallsSetUp": mscTdmaCsCallsSetUp,
       "mscTdmaCsCallsReleasedNormal": mscTdmaCsCallsReleasedNormal,
       "mscTdmaCsCallsReleasedAbnormal": mscTdmaCsCallsReleasedAbnormal,
       "mscTdmaCsErroredLFrames": mscTdmaCsErroredLFrames,
       "mscTdmaBc": mscTdmaBc,
       "mscTdmaBcRowStatusTable": mscTdmaBcRowStatusTable,
       "mscTdmaBcRowStatusEntry": mscTdmaBcRowStatusEntry,
       "mscTdmaBcRowStatus": mscTdmaBcRowStatus,
       "mscTdmaBcComponentName": mscTdmaBcComponentName,
       "mscTdmaBcStorageType": mscTdmaBcStorageType,
       "mscTdmaBcCsIndex": mscTdmaBcCsIndex,
       "mscTdmaBcBcIndex": mscTdmaBcBcIndex,
       "mscTdmaBcFramer": mscTdmaBcFramer,
       "mscTdmaBcFramerRowStatusTable": mscTdmaBcFramerRowStatusTable,
       "mscTdmaBcFramerRowStatusEntry": mscTdmaBcFramerRowStatusEntry,
       "mscTdmaBcFramerRowStatus": mscTdmaBcFramerRowStatus,
       "mscTdmaBcFramerComponentName": mscTdmaBcFramerComponentName,
       "mscTdmaBcFramerStorageType": mscTdmaBcFramerStorageType,
       "mscTdmaBcFramerIndex": mscTdmaBcFramerIndex,
       "mscTdmaBcFramerProvTable": mscTdmaBcFramerProvTable,
       "mscTdmaBcFramerProvEntry": mscTdmaBcFramerProvEntry,
       "mscTdmaBcFramerInterfaceName": mscTdmaBcFramerInterfaceName,
       "mscTdmaBcFramerStatsTable": mscTdmaBcFramerStatsTable,
       "mscTdmaBcFramerStatsEntry": mscTdmaBcFramerStatsEntry,
       "mscTdmaBcFramerTxFrames": mscTdmaBcFramerTxFrames,
       "mscTdmaBcFramerRxFrames": mscTdmaBcFramerRxFrames,
       "mscTdmaBcFramerRxBytes": mscTdmaBcFramerRxBytes,
       "mscTdmaBcFramerLinkTable": mscTdmaBcFramerLinkTable,
       "mscTdmaBcFramerLinkEntry": mscTdmaBcFramerLinkEntry,
       "mscTdmaBcFramerFramingType": mscTdmaBcFramerFramingType,
       "mscTdmaBcFramerStateTable": mscTdmaBcFramerStateTable,
       "mscTdmaBcFramerStateEntry": mscTdmaBcFramerStateEntry,
       "mscTdmaBcFramerAdminState": mscTdmaBcFramerAdminState,
       "mscTdmaBcFramerOperationalState": mscTdmaBcFramerOperationalState,
       "mscTdmaBcFramerUsageState": mscTdmaBcFramerUsageState,
       "mscTdmaBcModem": mscTdmaBcModem,
       "mscTdmaBcModemRowStatusTable": mscTdmaBcModemRowStatusTable,
       "mscTdmaBcModemRowStatusEntry": mscTdmaBcModemRowStatusEntry,
       "mscTdmaBcModemRowStatus": mscTdmaBcModemRowStatus,
       "mscTdmaBcModemComponentName": mscTdmaBcModemComponentName,
       "mscTdmaBcModemStorageType": mscTdmaBcModemStorageType,
       "mscTdmaBcModemIndex": mscTdmaBcModemIndex,
       "mscTdmaBcModemOperTable": mscTdmaBcModemOperTable,
       "mscTdmaBcModemOperEntry": mscTdmaBcModemOperEntry,
       "mscTdmaBcModemVoiceLaw": mscTdmaBcModemVoiceLaw,
       "mscTdmaBcModemRate": mscTdmaBcModemRate,
       "mscTdmaBcModemModemAlgorithmInUse": mscTdmaBcModemModemAlgorithmInUse,
       "mscTdmaBcModemProtocolState": mscTdmaBcModemProtocolState,
       "mscTdmaBcModemMobileSideFlowControlState": mscTdmaBcModemMobileSideFlowControlState,
       "mscTdmaBcModemPstnSideFlowControlState": mscTdmaBcModemPstnSideFlowControlState,
       "mscTdmaBcModemAsyncMode": mscTdmaBcModemAsyncMode,
       "mscTdmaBcModemOutbandFlowControl": mscTdmaBcModemOutbandFlowControl,
       "mscTdmaBcModemOutbandBreak": mscTdmaBcModemOutbandBreak,
       "mscTdmaBcModemAutobaud": mscTdmaBcModemAutobaud,
       "mscTdmaBcModemStatsTable": mscTdmaBcModemStatsTable,
       "mscTdmaBcModemStatsEntry": mscTdmaBcModemStatsEntry,
       "mscTdmaBcModemTxBytes": mscTdmaBcModemTxBytes,
       "mscTdmaBcModemRxBytes": mscTdmaBcModemRxBytes,
       "mscTdmaBcModemFramingErrors": mscTdmaBcModemFramingErrors,
       "mscTdmaBcFax": mscTdmaBcFax,
       "mscTdmaBcFaxRowStatusTable": mscTdmaBcFaxRowStatusTable,
       "mscTdmaBcFaxRowStatusEntry": mscTdmaBcFaxRowStatusEntry,
       "mscTdmaBcFaxRowStatus": mscTdmaBcFaxRowStatus,
       "mscTdmaBcFaxComponentName": mscTdmaBcFaxComponentName,
       "mscTdmaBcFaxStorageType": mscTdmaBcFaxStorageType,
       "mscTdmaBcFaxIndex": mscTdmaBcFaxIndex,
       "mscTdmaBcFaxOperTable": mscTdmaBcFaxOperTable,
       "mscTdmaBcFaxOperEntry": mscTdmaBcFaxOperEntry,
       "mscTdmaBcFaxActiveMode": mscTdmaBcFaxActiveMode,
       "mscTdmaBcFaxProtocolState": mscTdmaBcFaxProtocolState,
       "mscTdmaBcFaxMessageRate": mscTdmaBcFaxMessageRate,
       "mscTdmaBcFaxStatsTable": mscTdmaBcFaxStatsTable,
       "mscTdmaBcFaxStatsEntry": mscTdmaBcFaxStatsEntry,
       "mscTdmaBcFaxTxPagesToMobile": mscTdmaBcFaxTxPagesToMobile,
       "mscTdmaBcFaxRxPagesFromMobile": mscTdmaBcFaxRxPagesFromMobile,
       "mscTdmaBcDce": mscTdmaBcDce,
       "mscTdmaBcDceRowStatusTable": mscTdmaBcDceRowStatusTable,
       "mscTdmaBcDceRowStatusEntry": mscTdmaBcDceRowStatusEntry,
       "mscTdmaBcDceRowStatus": mscTdmaBcDceRowStatus,
       "mscTdmaBcDceComponentName": mscTdmaBcDceComponentName,
       "mscTdmaBcDceStorageType": mscTdmaBcDceStorageType,
       "mscTdmaBcDceIndex": mscTdmaBcDceIndex,
       "mscTdmaBcDsc": mscTdmaBcDsc,
       "mscTdmaBcDscRowStatusTable": mscTdmaBcDscRowStatusTable,
       "mscTdmaBcDscRowStatusEntry": mscTdmaBcDscRowStatusEntry,
       "mscTdmaBcDscRowStatus": mscTdmaBcDscRowStatus,
       "mscTdmaBcDscComponentName": mscTdmaBcDscComponentName,
       "mscTdmaBcDscStorageType": mscTdmaBcDscStorageType,
       "mscTdmaBcDscIndex": mscTdmaBcDscIndex,
       "mscTdmaBcDscOperTable": mscTdmaBcDscOperTable,
       "mscTdmaBcDscOperEntry": mscTdmaBcDscOperEntry,
       "mscTdmaBcDscP0CompressionDirection": mscTdmaBcDscP0CompressionDirection,
       "mscTdmaBcDscP1CompressionMaximumCodewords": mscTdmaBcDscP1CompressionMaximumCodewords,
       "mscTdmaBcDscP2CompressionMaximumCharacters": mscTdmaBcDscP2CompressionMaximumCharacters,
       "mscTdmaBcDscStatsTable": mscTdmaBcDscStatsTable,
       "mscTdmaBcDscStatsEntry": mscTdmaBcDscStatsEntry,
       "mscTdmaBcDscTxBytes": mscTdmaBcDscTxBytes,
       "mscTdmaBcDscRxBytes": mscTdmaBcDscRxBytes,
       "mscTdmaBcRlp1": mscTdmaBcRlp1,
       "mscTdmaBcRlp1RowStatusTable": mscTdmaBcRlp1RowStatusTable,
       "mscTdmaBcRlp1RowStatusEntry": mscTdmaBcRlp1RowStatusEntry,
       "mscTdmaBcRlp1RowStatus": mscTdmaBcRlp1RowStatus,
       "mscTdmaBcRlp1ComponentName": mscTdmaBcRlp1ComponentName,
       "mscTdmaBcRlp1StorageType": mscTdmaBcRlp1StorageType,
       "mscTdmaBcRlp1Index": mscTdmaBcRlp1Index,
       "mscTdmaBcRlp1OperTable": mscTdmaBcRlp1OperTable,
       "mscTdmaBcRlp1OperEntry": mscTdmaBcRlp1OperEntry,
       "mscTdmaBcRlp1Layer3L0ReqWinSize": mscTdmaBcRlp1Layer3L0ReqWinSize,
       "mscTdmaBcRlp1Layer3L1ReqWinSize1": mscTdmaBcRlp1Layer3L1ReqWinSize1,
       "mscTdmaBcRlp1T1ResponseTimer": mscTdmaBcRlp1T1ResponseTimer,
       "mscTdmaBcRlp1T2LinkActivityTimer": mscTdmaBcRlp1T2LinkActivityTimer,
       "mscTdmaBcRlp1T3PeerAckTimer": mscTdmaBcRlp1T3PeerAckTimer,
       "mscTdmaBcRlp1StatsTable": mscTdmaBcRlp1StatsTable,
       "mscTdmaBcRlp1StatsEntry": mscTdmaBcRlp1StatsEntry,
       "mscTdmaBcRlp1TxFrames": mscTdmaBcRlp1TxFrames,
       "mscTdmaBcRlp1RxFrames": mscTdmaBcRlp1RxFrames,
       "mscTdmaBcRlp1BadRxFrames": mscTdmaBcRlp1BadRxFrames,
       "mscTdmaBcV42": mscTdmaBcV42,
       "mscTdmaBcV42RowStatusTable": mscTdmaBcV42RowStatusTable,
       "mscTdmaBcV42RowStatusEntry": mscTdmaBcV42RowStatusEntry,
       "mscTdmaBcV42RowStatus": mscTdmaBcV42RowStatus,
       "mscTdmaBcV42ComponentName": mscTdmaBcV42ComponentName,
       "mscTdmaBcV42StorageType": mscTdmaBcV42StorageType,
       "mscTdmaBcV42Index": mscTdmaBcV42Index,
       "mscTdmaBcV42OperTable": mscTdmaBcV42OperTable,
       "mscTdmaBcV42OperEntry": mscTdmaBcV42OperEntry,
       "mscTdmaBcV42ProtocolState": mscTdmaBcV42ProtocolState,
       "mscTdmaBcV42TxN401FrameSize": mscTdmaBcV42TxN401FrameSize,
       "mscTdmaBcV42RxN401FrameSize": mscTdmaBcV42RxN401FrameSize,
       "mscTdmaBcV42TxKWindowSize": mscTdmaBcV42TxKWindowSize,
       "mscTdmaBcV42RxKWindowSize": mscTdmaBcV42RxKWindowSize,
       "mscTdmaBcV42V42ActiveInCall": mscTdmaBcV42V42ActiveInCall,
       "mscTdmaBcV42V42BisActiveInCall": mscTdmaBcV42V42BisActiveInCall,
       "mscTdmaBcV42StatsTable": mscTdmaBcV42StatsTable,
       "mscTdmaBcV42StatsEntry": mscTdmaBcV42StatsEntry,
       "mscTdmaBcV42RxIBytes": mscTdmaBcV42RxIBytes,
       "mscTdmaBcV42TxIBytes": mscTdmaBcV42TxIBytes,
       "mscTdmaBcV42RxIFrames": mscTdmaBcV42RxIFrames,
       "mscTdmaBcV42TxIFrames": mscTdmaBcV42TxIFrames,
       "mscTdmaBcV42RetransmittedFrames": mscTdmaBcV42RetransmittedFrames,
       "mscTdmaBcV42T1AckTimeouts": mscTdmaBcV42T1AckTimeouts,
       "mscTdmaBcV42RemoteBusyIndications": mscTdmaBcV42RemoteBusyIndications,
       "mscTdmaBcV42LocalBusyIndications": mscTdmaBcV42LocalBusyIndications,
       "mscTdmaBcV42BadFramesRx": mscTdmaBcV42BadFramesRx,
       "mscTdmaBcV42CrcErrorsRx": mscTdmaBcV42CrcErrorsRx,
       "mscTdmaBcV42Bis": mscTdmaBcV42Bis,
       "mscTdmaBcV42BisRowStatusTable": mscTdmaBcV42BisRowStatusTable,
       "mscTdmaBcV42BisRowStatusEntry": mscTdmaBcV42BisRowStatusEntry,
       "mscTdmaBcV42BisRowStatus": mscTdmaBcV42BisRowStatus,
       "mscTdmaBcV42BisComponentName": mscTdmaBcV42BisComponentName,
       "mscTdmaBcV42BisStorageType": mscTdmaBcV42BisStorageType,
       "mscTdmaBcV42BisIndex": mscTdmaBcV42BisIndex,
       "mscTdmaBcV42BisOperTable": mscTdmaBcV42BisOperTable,
       "mscTdmaBcV42BisOperEntry": mscTdmaBcV42BisOperEntry,
       "mscTdmaBcV42BisProtocolModeEncoder": mscTdmaBcV42BisProtocolModeEncoder,
       "mscTdmaBcV42BisProtocolModeDecoder": mscTdmaBcV42BisProtocolModeDecoder,
       "mscTdmaBcV42BisP0CompressionDirection": mscTdmaBcV42BisP0CompressionDirection,
       "mscTdmaBcV42BisP1MaximumCodewords": mscTdmaBcV42BisP1MaximumCodewords,
       "mscTdmaBcV42BisP2MaximumStringSize": mscTdmaBcV42BisP2MaximumStringSize,
       "mscTdmaBcV42BisLastDecodeError": mscTdmaBcV42BisLastDecodeError,
       "mscTdmaBcV42BisCompRatioEncoder": mscTdmaBcV42BisCompRatioEncoder,
       "mscTdmaBcV42BisCompRatioDecoder": mscTdmaBcV42BisCompRatioDecoder,
       "mscTdmaBcV42BisStatsTable": mscTdmaBcV42BisStatsTable,
       "mscTdmaBcV42BisStatsEntry": mscTdmaBcV42BisStatsEntry,
       "mscTdmaBcV42BisModeChangesEncode": mscTdmaBcV42BisModeChangesEncode,
       "mscTdmaBcV42BisModeChangesDecode": mscTdmaBcV42BisModeChangesDecode,
       "mscTdmaBcV42BisResetsEncode": mscTdmaBcV42BisResetsEncode,
       "mscTdmaBcV42BisResetsDecode": mscTdmaBcV42BisResetsDecode,
       "mscTdmaBcV42BisReinitializations": mscTdmaBcV42BisReinitializations,
       "mscTdmaBcV42BisErrorsInDecode": mscTdmaBcV42BisErrorsInDecode,
       "mscTdmaBcUr": mscTdmaBcUr,
       "mscTdmaBcUrRowStatusTable": mscTdmaBcUrRowStatusTable,
       "mscTdmaBcUrRowStatusEntry": mscTdmaBcUrRowStatusEntry,
       "mscTdmaBcUrRowStatus": mscTdmaBcUrRowStatus,
       "mscTdmaBcUrComponentName": mscTdmaBcUrComponentName,
       "mscTdmaBcUrStorageType": mscTdmaBcUrStorageType,
       "mscTdmaBcUrIndex": mscTdmaBcUrIndex,
       "mscTdmaBcUrOperTable": mscTdmaBcUrOperTable,
       "mscTdmaBcUrOperEntry": mscTdmaBcUrOperEntry,
       "mscTdmaBcUrRxBufferSize": mscTdmaBcUrRxBufferSize,
       "mscTdmaBcUrTxFlowControlState": mscTdmaBcUrTxFlowControlState,
       "mscTdmaBcUrRxFlowControlState": mscTdmaBcUrRxFlowControlState,
       "mscTdmaBcUrStatsTable": mscTdmaBcUrStatsTable,
       "mscTdmaBcUrStatsEntry": mscTdmaBcUrStatsEntry,
       "mscTdmaBcUrTxFrames": mscTdmaBcUrTxFrames,
       "mscTdmaBcUrRxFrames": mscTdmaBcUrRxFrames,
       "mscTdmaBcUrUnacknowledgedFrames": mscTdmaBcUrUnacknowledgedFrames,
       "mscTdmaBcUrCumUnacknowledgedFrames": mscTdmaBcUrCumUnacknowledgedFrames,
       "mscTdmaBcOperTable": mscTdmaBcOperTable,
       "mscTdmaBcOperEntry": mscTdmaBcOperEntry,
       "mscTdmaBcState": mscTdmaBcState,
       "mscTdmaBcCallType": mscTdmaBcCallType,
       "mscTdmaBcLastResponseCode": mscTdmaBcLastResponseCode,
       "mscTdmaBcMateBearerChannel": mscTdmaBcMateBearerChannel,
       "mscTdmaBcCidDataTable": mscTdmaBcCidDataTable,
       "mscTdmaBcCidDataEntry": mscTdmaBcCidDataEntry,
       "mscTdmaBcCustomerIdentifier": mscTdmaBcCustomerIdentifier,
       "mscTdmaBcStateTable": mscTdmaBcStateTable,
       "mscTdmaBcStateEntry": mscTdmaBcStateEntry,
       "mscTdmaBcAdminState": mscTdmaBcAdminState,
       "mscTdmaBcOperationalState": mscTdmaBcOperationalState,
       "mscTdmaBcUsageState": mscTdmaBcUsageState,
       "tdmaIwfMIB": tdmaIwfMIB,
       "tdmaIwfGroup": tdmaIwfGroup,
       "tdmaIwfGroupCA": tdmaIwfGroupCA,
       "tdmaIwfGroupCA02": tdmaIwfGroupCA02,
       "tdmaIwfGroupCA02A": tdmaIwfGroupCA02A,
       "tdmaIwfCapabilities": tdmaIwfCapabilities,
       "tdmaIwfCapabilitiesCA": tdmaIwfCapabilitiesCA,
       "tdmaIwfCapabilitiesCA02": tdmaIwfCapabilitiesCA02,
       "tdmaIwfCapabilitiesCA02A": tdmaIwfCapabilitiesCA02A}
)
