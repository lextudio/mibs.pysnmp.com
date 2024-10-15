# SNMP MIB module (Nortel-MsCarrier-MscPassport-SoftwareMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-SoftwareMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:03 2024
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
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 AsciiStringIndex,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
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

_MscSw_ObjectIdentity = ObjectIdentity
mscSw = _MscSw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14)
)
_MscSwRowStatusTable_Object = MibTable
mscSwRowStatusTable = _MscSwRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 1)
)
if mibBuilder.loadTexts:
    mscSwRowStatusTable.setStatus("mandatory")
_MscSwRowStatusEntry_Object = MibTableRow
mscSwRowStatusEntry = _MscSwRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 1, 1)
)
mscSwRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"),
)
if mibBuilder.loadTexts:
    mscSwRowStatusEntry.setStatus("mandatory")
_MscSwRowStatus_Type = RowStatus
_MscSwRowStatus_Object = MibTableColumn
mscSwRowStatus = _MscSwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 1, 1, 1),
    _MscSwRowStatus_Type()
)
mscSwRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwRowStatus.setStatus("mandatory")
_MscSwComponentName_Type = DisplayString
_MscSwComponentName_Object = MibTableColumn
mscSwComponentName = _MscSwComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 1, 1, 2),
    _MscSwComponentName_Type()
)
mscSwComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwComponentName.setStatus("mandatory")
_MscSwStorageType_Type = StorageType
_MscSwStorageType_Object = MibTableColumn
mscSwStorageType = _MscSwStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 1, 1, 4),
    _MscSwStorageType_Type()
)
mscSwStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwStorageType.setStatus("mandatory")
_MscSwIndex_Type = NonReplicated
_MscSwIndex_Object = MibTableColumn
mscSwIndex = _MscSwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 1, 1, 10),
    _MscSwIndex_Type()
)
mscSwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscSwIndex.setStatus("mandatory")
_MscSwDld_ObjectIdentity = ObjectIdentity
mscSwDld = _MscSwDld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2)
)
_MscSwDldRowStatusTable_Object = MibTable
mscSwDldRowStatusTable = _MscSwDldRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 1)
)
if mibBuilder.loadTexts:
    mscSwDldRowStatusTable.setStatus("mandatory")
_MscSwDldRowStatusEntry_Object = MibTableRow
mscSwDldRowStatusEntry = _MscSwDldRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 1, 1)
)
mscSwDldRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwDldIndex"),
)
if mibBuilder.loadTexts:
    mscSwDldRowStatusEntry.setStatus("mandatory")
_MscSwDldRowStatus_Type = RowStatus
_MscSwDldRowStatus_Object = MibTableColumn
mscSwDldRowStatus = _MscSwDldRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 1, 1, 1),
    _MscSwDldRowStatus_Type()
)
mscSwDldRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwDldRowStatus.setStatus("mandatory")
_MscSwDldComponentName_Type = DisplayString
_MscSwDldComponentName_Object = MibTableColumn
mscSwDldComponentName = _MscSwDldComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 1, 1, 2),
    _MscSwDldComponentName_Type()
)
mscSwDldComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwDldComponentName.setStatus("mandatory")
_MscSwDldStorageType_Type = StorageType
_MscSwDldStorageType_Object = MibTableColumn
mscSwDldStorageType = _MscSwDldStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 1, 1, 4),
    _MscSwDldStorageType_Type()
)
mscSwDldStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwDldStorageType.setStatus("mandatory")
_MscSwDldIndex_Type = NonReplicated
_MscSwDldIndex_Object = MibTableColumn
mscSwDldIndex = _MscSwDldIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 1, 1, 10),
    _MscSwDldIndex_Type()
)
mscSwDldIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscSwDldIndex.setStatus("mandatory")
_MscSwDldOperTable_Object = MibTable
mscSwDldOperTable = _MscSwDldOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 10)
)
if mibBuilder.loadTexts:
    mscSwDldOperTable.setStatus("mandatory")
_MscSwDldOperEntry_Object = MibTableRow
mscSwDldOperEntry = _MscSwDldOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 10, 1)
)
mscSwDldOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwDldIndex"),
)
if mibBuilder.loadTexts:
    mscSwDldOperEntry.setStatus("mandatory")


class _MscSwDldAvBeingDownloaded_Type(AsciiString):
    """Custom type mscSwDldAvBeingDownloaded based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_MscSwDldAvBeingDownloaded_Type.__name__ = "AsciiString"
_MscSwDldAvBeingDownloaded_Object = MibTableColumn
mscSwDldAvBeingDownloaded = _MscSwDldAvBeingDownloaded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 10, 1, 1),
    _MscSwDldAvBeingDownloaded_Type()
)
mscSwDldAvBeingDownloaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwDldAvBeingDownloaded.setStatus("mandatory")


class _MscSwDldStatus_Type(Integer32):
    """Custom type mscSwDldStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 1),
          ("inactive", 0),
          ("stopping", 2))
    )


_MscSwDldStatus_Type.__name__ = "Integer32"
_MscSwDldStatus_Object = MibTableColumn
mscSwDldStatus = _MscSwDldStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 10, 1, 2),
    _MscSwDldStatus_Type()
)
mscSwDldStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwDldStatus.setStatus("mandatory")


class _MscSwDldFilesToTransfer_Type(Unsigned32):
    """Custom type mscSwDldFilesToTransfer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MscSwDldFilesToTransfer_Type.__name__ = "Unsigned32"
_MscSwDldFilesToTransfer_Object = MibTableColumn
mscSwDldFilesToTransfer = _MscSwDldFilesToTransfer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 10, 1, 3),
    _MscSwDldFilesToTransfer_Type()
)
mscSwDldFilesToTransfer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwDldFilesToTransfer.setStatus("mandatory")


class _MscSwDldProcessorTargets_Type(OctetString):
    """Custom type mscSwDldProcessorTargets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscSwDldProcessorTargets_Type.__name__ = "OctetString"
_MscSwDldProcessorTargets_Object = MibTableColumn
mscSwDldProcessorTargets = _MscSwDldProcessorTargets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 10, 1, 4),
    _MscSwDldProcessorTargets_Type()
)
mscSwDldProcessorTargets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSwDldProcessorTargets.setStatus("mandatory")
_MscSwDldDldListTable_Object = MibTable
mscSwDldDldListTable = _MscSwDldDldListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 260)
)
if mibBuilder.loadTexts:
    mscSwDldDldListTable.setStatus("mandatory")
_MscSwDldDldListEntry_Object = MibTableRow
mscSwDldDldListEntry = _MscSwDldDldListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 260, 1)
)
mscSwDldDldListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwDldIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwDldDldListValue"),
)
if mibBuilder.loadTexts:
    mscSwDldDldListEntry.setStatus("mandatory")


class _MscSwDldDldListValue_Type(AsciiString):
    """Custom type mscSwDldDldListValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_MscSwDldDldListValue_Type.__name__ = "AsciiString"
_MscSwDldDldListValue_Object = MibTableColumn
mscSwDldDldListValue = _MscSwDldDldListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 260, 1, 1),
    _MscSwDldDldListValue_Type()
)
mscSwDldDldListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSwDldDldListValue.setStatus("mandatory")
_MscSwDldDldListRowStatus_Type = RowStatus
_MscSwDldDldListRowStatus_Object = MibTableColumn
mscSwDldDldListRowStatus = _MscSwDldDldListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 260, 1, 2),
    _MscSwDldDldListRowStatus_Type()
)
mscSwDldDldListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscSwDldDldListRowStatus.setStatus("mandatory")
_MscSwDldDownloadedAvListTable_Object = MibTable
mscSwDldDownloadedAvListTable = _MscSwDldDownloadedAvListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 261)
)
if mibBuilder.loadTexts:
    mscSwDldDownloadedAvListTable.setStatus("mandatory")
_MscSwDldDownloadedAvListEntry_Object = MibTableRow
mscSwDldDownloadedAvListEntry = _MscSwDldDownloadedAvListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 261, 1)
)
mscSwDldDownloadedAvListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwDldIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwDldDownloadedAvListValue"),
)
if mibBuilder.loadTexts:
    mscSwDldDownloadedAvListEntry.setStatus("mandatory")


class _MscSwDldDownloadedAvListValue_Type(AsciiString):
    """Custom type mscSwDldDownloadedAvListValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_MscSwDldDownloadedAvListValue_Type.__name__ = "AsciiString"
_MscSwDldDownloadedAvListValue_Object = MibTableColumn
mscSwDldDownloadedAvListValue = _MscSwDldDownloadedAvListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 261, 1, 1),
    _MscSwDldDownloadedAvListValue_Type()
)
mscSwDldDownloadedAvListValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwDldDownloadedAvListValue.setStatus("mandatory")
_MscSwAv_ObjectIdentity = ObjectIdentity
mscSwAv = _MscSwAv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3)
)
_MscSwAvRowStatusTable_Object = MibTable
mscSwAvRowStatusTable = _MscSwAvRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 1)
)
if mibBuilder.loadTexts:
    mscSwAvRowStatusTable.setStatus("mandatory")
_MscSwAvRowStatusEntry_Object = MibTableRow
mscSwAvRowStatusEntry = _MscSwAvRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 1, 1)
)
mscSwAvRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvIndex"),
)
if mibBuilder.loadTexts:
    mscSwAvRowStatusEntry.setStatus("mandatory")
_MscSwAvRowStatus_Type = RowStatus
_MscSwAvRowStatus_Object = MibTableColumn
mscSwAvRowStatus = _MscSwAvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 1, 1, 1),
    _MscSwAvRowStatus_Type()
)
mscSwAvRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwAvRowStatus.setStatus("mandatory")
_MscSwAvComponentName_Type = DisplayString
_MscSwAvComponentName_Object = MibTableColumn
mscSwAvComponentName = _MscSwAvComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 1, 1, 2),
    _MscSwAvComponentName_Type()
)
mscSwAvComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwAvComponentName.setStatus("mandatory")
_MscSwAvStorageType_Type = StorageType
_MscSwAvStorageType_Object = MibTableColumn
mscSwAvStorageType = _MscSwAvStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 1, 1, 4),
    _MscSwAvStorageType_Type()
)
mscSwAvStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwAvStorageType.setStatus("mandatory")


class _MscSwAvIndex_Type(AsciiStringIndex):
    """Custom type mscSwAvIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_MscSwAvIndex_Type.__name__ = "AsciiStringIndex"
_MscSwAvIndex_Object = MibTableColumn
mscSwAvIndex = _MscSwAvIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 1, 1, 10),
    _MscSwAvIndex_Type()
)
mscSwAvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscSwAvIndex.setStatus("mandatory")
_MscSwAvFeat_ObjectIdentity = ObjectIdentity
mscSwAvFeat = _MscSwAvFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 2)
)
_MscSwAvFeatRowStatusTable_Object = MibTable
mscSwAvFeatRowStatusTable = _MscSwAvFeatRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscSwAvFeatRowStatusTable.setStatus("mandatory")
_MscSwAvFeatRowStatusEntry_Object = MibTableRow
mscSwAvFeatRowStatusEntry = _MscSwAvFeatRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 2, 1, 1)
)
mscSwAvFeatRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvFeatIndex"),
)
if mibBuilder.loadTexts:
    mscSwAvFeatRowStatusEntry.setStatus("mandatory")
_MscSwAvFeatRowStatus_Type = RowStatus
_MscSwAvFeatRowStatus_Object = MibTableColumn
mscSwAvFeatRowStatus = _MscSwAvFeatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 2, 1, 1, 1),
    _MscSwAvFeatRowStatus_Type()
)
mscSwAvFeatRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwAvFeatRowStatus.setStatus("mandatory")
_MscSwAvFeatComponentName_Type = DisplayString
_MscSwAvFeatComponentName_Object = MibTableColumn
mscSwAvFeatComponentName = _MscSwAvFeatComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 2, 1, 1, 2),
    _MscSwAvFeatComponentName_Type()
)
mscSwAvFeatComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwAvFeatComponentName.setStatus("mandatory")
_MscSwAvFeatStorageType_Type = StorageType
_MscSwAvFeatStorageType_Object = MibTableColumn
mscSwAvFeatStorageType = _MscSwAvFeatStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 2, 1, 1, 4),
    _MscSwAvFeatStorageType_Type()
)
mscSwAvFeatStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwAvFeatStorageType.setStatus("mandatory")


class _MscSwAvFeatIndex_Type(AsciiStringIndex):
    """Custom type mscSwAvFeatIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_MscSwAvFeatIndex_Type.__name__ = "AsciiStringIndex"
_MscSwAvFeatIndex_Object = MibTableColumn
mscSwAvFeatIndex = _MscSwAvFeatIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 2, 1, 1, 10),
    _MscSwAvFeatIndex_Type()
)
mscSwAvFeatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscSwAvFeatIndex.setStatus("mandatory")
_MscSwAvPatch_ObjectIdentity = ObjectIdentity
mscSwAvPatch = _MscSwAvPatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 3)
)
_MscSwAvPatchRowStatusTable_Object = MibTable
mscSwAvPatchRowStatusTable = _MscSwAvPatchRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 3, 1)
)
if mibBuilder.loadTexts:
    mscSwAvPatchRowStatusTable.setStatus("mandatory")
_MscSwAvPatchRowStatusEntry_Object = MibTableRow
mscSwAvPatchRowStatusEntry = _MscSwAvPatchRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 3, 1, 1)
)
mscSwAvPatchRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvPatchIndex"),
)
if mibBuilder.loadTexts:
    mscSwAvPatchRowStatusEntry.setStatus("mandatory")
_MscSwAvPatchRowStatus_Type = RowStatus
_MscSwAvPatchRowStatus_Object = MibTableColumn
mscSwAvPatchRowStatus = _MscSwAvPatchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 3, 1, 1, 1),
    _MscSwAvPatchRowStatus_Type()
)
mscSwAvPatchRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwAvPatchRowStatus.setStatus("mandatory")
_MscSwAvPatchComponentName_Type = DisplayString
_MscSwAvPatchComponentName_Object = MibTableColumn
mscSwAvPatchComponentName = _MscSwAvPatchComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 3, 1, 1, 2),
    _MscSwAvPatchComponentName_Type()
)
mscSwAvPatchComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwAvPatchComponentName.setStatus("mandatory")
_MscSwAvPatchStorageType_Type = StorageType
_MscSwAvPatchStorageType_Object = MibTableColumn
mscSwAvPatchStorageType = _MscSwAvPatchStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 3, 1, 1, 4),
    _MscSwAvPatchStorageType_Type()
)
mscSwAvPatchStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwAvPatchStorageType.setStatus("mandatory")


class _MscSwAvPatchIndex_Type(AsciiStringIndex):
    """Custom type mscSwAvPatchIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_MscSwAvPatchIndex_Type.__name__ = "AsciiStringIndex"
_MscSwAvPatchIndex_Object = MibTableColumn
mscSwAvPatchIndex = _MscSwAvPatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 3, 1, 1, 10),
    _MscSwAvPatchIndex_Type()
)
mscSwAvPatchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscSwAvPatchIndex.setStatus("mandatory")
_MscSwAvPatchOperTable_Object = MibTable
mscSwAvPatchOperTable = _MscSwAvPatchOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 3, 10)
)
if mibBuilder.loadTexts:
    mscSwAvPatchOperTable.setStatus("mandatory")
_MscSwAvPatchOperEntry_Object = MibTableRow
mscSwAvPatchOperEntry = _MscSwAvPatchOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 3, 10, 1)
)
mscSwAvPatchOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvPatchIndex"),
)
if mibBuilder.loadTexts:
    mscSwAvPatchOperEntry.setStatus("mandatory")


class _MscSwAvPatchDescription_Type(AsciiString):
    """Custom type mscSwAvPatchDescription based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_MscSwAvPatchDescription_Type.__name__ = "AsciiString"
_MscSwAvPatchDescription_Object = MibTableColumn
mscSwAvPatchDescription = _MscSwAvPatchDescription_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 3, 10, 1, 1),
    _MscSwAvPatchDescription_Type()
)
mscSwAvPatchDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwAvPatchDescription.setStatus("mandatory")
_MscSwAvOperTable_Object = MibTable
mscSwAvOperTable = _MscSwAvOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 10)
)
if mibBuilder.loadTexts:
    mscSwAvOperTable.setStatus("mandatory")
_MscSwAvOperEntry_Object = MibTableRow
mscSwAvOperEntry = _MscSwAvOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 10, 1)
)
mscSwAvOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvIndex"),
)
if mibBuilder.loadTexts:
    mscSwAvOperEntry.setStatus("mandatory")


class _MscSwAvProcessorTargets_Type(OctetString):
    """Custom type mscSwAvProcessorTargets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscSwAvProcessorTargets_Type.__name__ = "OctetString"
_MscSwAvProcessorTargets_Object = MibTableColumn
mscSwAvProcessorTargets = _MscSwAvProcessorTargets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 10, 1, 1),
    _MscSwAvProcessorTargets_Type()
)
mscSwAvProcessorTargets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwAvProcessorTargets.setStatus("mandatory")
_MscSwAvCompatibleAvListTable_Object = MibTable
mscSwAvCompatibleAvListTable = _MscSwAvCompatibleAvListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 259)
)
if mibBuilder.loadTexts:
    mscSwAvCompatibleAvListTable.setStatus("mandatory")
_MscSwAvCompatibleAvListEntry_Object = MibTableRow
mscSwAvCompatibleAvListEntry = _MscSwAvCompatibleAvListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 259, 1)
)
mscSwAvCompatibleAvListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvCompatibleAvListValue"),
)
if mibBuilder.loadTexts:
    mscSwAvCompatibleAvListEntry.setStatus("mandatory")


class _MscSwAvCompatibleAvListValue_Type(AsciiString):
    """Custom type mscSwAvCompatibleAvListValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_MscSwAvCompatibleAvListValue_Type.__name__ = "AsciiString"
_MscSwAvCompatibleAvListValue_Object = MibTableColumn
mscSwAvCompatibleAvListValue = _MscSwAvCompatibleAvListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 259, 1, 1),
    _MscSwAvCompatibleAvListValue_Type()
)
mscSwAvCompatibleAvListValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwAvCompatibleAvListValue.setStatus("mandatory")
_MscSwLpt_ObjectIdentity = ObjectIdentity
mscSwLpt = _MscSwLpt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4)
)
_MscSwLptRowStatusTable_Object = MibTable
mscSwLptRowStatusTable = _MscSwLptRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 1)
)
if mibBuilder.loadTexts:
    mscSwLptRowStatusTable.setStatus("mandatory")
_MscSwLptRowStatusEntry_Object = MibTableRow
mscSwLptRowStatusEntry = _MscSwLptRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 1, 1)
)
mscSwLptRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwLptIndex"),
)
if mibBuilder.loadTexts:
    mscSwLptRowStatusEntry.setStatus("mandatory")
_MscSwLptRowStatus_Type = RowStatus
_MscSwLptRowStatus_Object = MibTableColumn
mscSwLptRowStatus = _MscSwLptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 1, 1, 1),
    _MscSwLptRowStatus_Type()
)
mscSwLptRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSwLptRowStatus.setStatus("mandatory")
_MscSwLptComponentName_Type = DisplayString
_MscSwLptComponentName_Object = MibTableColumn
mscSwLptComponentName = _MscSwLptComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 1, 1, 2),
    _MscSwLptComponentName_Type()
)
mscSwLptComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwLptComponentName.setStatus("mandatory")
_MscSwLptStorageType_Type = StorageType
_MscSwLptStorageType_Object = MibTableColumn
mscSwLptStorageType = _MscSwLptStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 1, 1, 4),
    _MscSwLptStorageType_Type()
)
mscSwLptStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwLptStorageType.setStatus("mandatory")


class _MscSwLptIndex_Type(AsciiStringIndex):
    """Custom type mscSwLptIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_MscSwLptIndex_Type.__name__ = "AsciiStringIndex"
_MscSwLptIndex_Object = MibTableColumn
mscSwLptIndex = _MscSwLptIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 1, 1, 10),
    _MscSwLptIndex_Type()
)
mscSwLptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscSwLptIndex.setStatus("mandatory")
_MscSwLptProvTable_Object = MibTable
mscSwLptProvTable = _MscSwLptProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 10)
)
if mibBuilder.loadTexts:
    mscSwLptProvTable.setStatus("mandatory")
_MscSwLptProvEntry_Object = MibTableRow
mscSwLptProvEntry = _MscSwLptProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 10, 1)
)
mscSwLptProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwLptIndex"),
)
if mibBuilder.loadTexts:
    mscSwLptProvEntry.setStatus("mandatory")


class _MscSwLptCommentText_Type(AsciiString):
    """Custom type mscSwLptCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MscSwLptCommentText_Type.__name__ = "AsciiString"
_MscSwLptCommentText_Object = MibTableColumn
mscSwLptCommentText = _MscSwLptCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 10, 1, 1),
    _MscSwLptCommentText_Type()
)
mscSwLptCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSwLptCommentText.setStatus("mandatory")


class _MscSwLptSystemConfig_Type(Integer32):
    """Custom type mscSwLptSystemConfig based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("default", 0)
    )


_MscSwLptSystemConfig_Type.__name__ = "Integer32"
_MscSwLptSystemConfig_Object = MibTableColumn
mscSwLptSystemConfig = _MscSwLptSystemConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 10, 1, 2),
    _MscSwLptSystemConfig_Type()
)
mscSwLptSystemConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSwLptSystemConfig.setStatus("mandatory")
_MscSwLptFlTable_Object = MibTable
mscSwLptFlTable = _MscSwLptFlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 257)
)
if mibBuilder.loadTexts:
    mscSwLptFlTable.setStatus("mandatory")
_MscSwLptFlEntry_Object = MibTableRow
mscSwLptFlEntry = _MscSwLptFlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 257, 1)
)
mscSwLptFlEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwLptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwLptFlValue"),
)
if mibBuilder.loadTexts:
    mscSwLptFlEntry.setStatus("mandatory")


class _MscSwLptFlValue_Type(AsciiString):
    """Custom type mscSwLptFlValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_MscSwLptFlValue_Type.__name__ = "AsciiString"
_MscSwLptFlValue_Object = MibTableColumn
mscSwLptFlValue = _MscSwLptFlValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 257, 1, 1),
    _MscSwLptFlValue_Type()
)
mscSwLptFlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSwLptFlValue.setStatus("mandatory")
_MscSwLptFlRowStatus_Type = RowStatus
_MscSwLptFlRowStatus_Object = MibTableColumn
mscSwLptFlRowStatus = _MscSwLptFlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 257, 1, 2),
    _MscSwLptFlRowStatus_Type()
)
mscSwLptFlRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscSwLptFlRowStatus.setStatus("mandatory")
_MscSwLptLogicalProcessorsTable_Object = MibTable
mscSwLptLogicalProcessorsTable = _MscSwLptLogicalProcessorsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 258)
)
if mibBuilder.loadTexts:
    mscSwLptLogicalProcessorsTable.setStatus("mandatory")
_MscSwLptLogicalProcessorsEntry_Object = MibTableRow
mscSwLptLogicalProcessorsEntry = _MscSwLptLogicalProcessorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 258, 1)
)
mscSwLptLogicalProcessorsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwLptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwLptLogicalProcessorsValue"),
)
if mibBuilder.loadTexts:
    mscSwLptLogicalProcessorsEntry.setStatus("mandatory")
_MscSwLptLogicalProcessorsValue_Type = Link
_MscSwLptLogicalProcessorsValue_Object = MibTableColumn
mscSwLptLogicalProcessorsValue = _MscSwLptLogicalProcessorsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 258, 1, 1),
    _MscSwLptLogicalProcessorsValue_Type()
)
mscSwLptLogicalProcessorsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwLptLogicalProcessorsValue.setStatus("mandatory")
_MscSwOperTable_Object = MibTable
mscSwOperTable = _MscSwOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 11)
)
if mibBuilder.loadTexts:
    mscSwOperTable.setStatus("mandatory")
_MscSwOperEntry_Object = MibTableRow
mscSwOperEntry = _MscSwOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 11, 1)
)
mscSwOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"),
)
if mibBuilder.loadTexts:
    mscSwOperEntry.setStatus("mandatory")


class _MscSwTidyStatus_Type(Integer32):
    """Custom type mscSwTidyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 1),
          ("inactive", 0),
          ("querying", 2))
    )


_MscSwTidyStatus_Type.__name__ = "Integer32"
_MscSwTidyStatus_Object = MibTableColumn
mscSwTidyStatus = _MscSwTidyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 11, 1, 1),
    _MscSwTidyStatus_Type()
)
mscSwTidyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwTidyStatus.setStatus("mandatory")


class _MscSwAvBeingTidied_Type(AsciiString):
    """Custom type mscSwAvBeingTidied based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_MscSwAvBeingTidied_Type.__name__ = "AsciiString"
_MscSwAvBeingTidied_Object = MibTableColumn
mscSwAvBeingTidied = _MscSwAvBeingTidied_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 11, 1, 421),
    _MscSwAvBeingTidied_Type()
)
mscSwAvBeingTidied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwAvBeingTidied.setStatus("mandatory")
_MscSwAvlTable_Object = MibTable
mscSwAvlTable = _MscSwAvlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 256)
)
if mibBuilder.loadTexts:
    mscSwAvlTable.setStatus("mandatory")
_MscSwAvlEntry_Object = MibTableRow
mscSwAvlEntry = _MscSwAvlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 256, 1)
)
mscSwAvlEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvlValue"),
)
if mibBuilder.loadTexts:
    mscSwAvlEntry.setStatus("mandatory")


class _MscSwAvlValue_Type(AsciiString):
    """Custom type mscSwAvlValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_MscSwAvlValue_Type.__name__ = "AsciiString"
_MscSwAvlValue_Object = MibTableColumn
mscSwAvlValue = _MscSwAvlValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 256, 1, 1),
    _MscSwAvlValue_Type()
)
mscSwAvlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSwAvlValue.setStatus("mandatory")
_MscSwAvlRowStatus_Type = RowStatus
_MscSwAvlRowStatus_Object = MibTableColumn
mscSwAvlRowStatus = _MscSwAvlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 256, 1, 2),
    _MscSwAvlRowStatus_Type()
)
mscSwAvlRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscSwAvlRowStatus.setStatus("mandatory")
_MscSwAvListToTidyTable_Object = MibTable
mscSwAvListToTidyTable = _MscSwAvListToTidyTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 422)
)
if mibBuilder.loadTexts:
    mscSwAvListToTidyTable.setStatus("mandatory")
_MscSwAvListToTidyEntry_Object = MibTableRow
mscSwAvListToTidyEntry = _MscSwAvListToTidyEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 422, 1)
)
mscSwAvListToTidyEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvListToTidyValue"),
)
if mibBuilder.loadTexts:
    mscSwAvListToTidyEntry.setStatus("mandatory")


class _MscSwAvListToTidyValue_Type(AsciiString):
    """Custom type mscSwAvListToTidyValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_MscSwAvListToTidyValue_Type.__name__ = "AsciiString"
_MscSwAvListToTidyValue_Object = MibTableColumn
mscSwAvListToTidyValue = _MscSwAvListToTidyValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 422, 1, 1),
    _MscSwAvListToTidyValue_Type()
)
mscSwAvListToTidyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwAvListToTidyValue.setStatus("mandatory")
_MscSwAvListTidiedTable_Object = MibTable
mscSwAvListTidiedTable = _MscSwAvListTidiedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 423)
)
if mibBuilder.loadTexts:
    mscSwAvListTidiedTable.setStatus("mandatory")
_MscSwAvListTidiedEntry_Object = MibTableRow
mscSwAvListTidiedEntry = _MscSwAvListTidiedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 423, 1)
)
mscSwAvListTidiedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvListTidiedValue"),
)
if mibBuilder.loadTexts:
    mscSwAvListTidiedEntry.setStatus("mandatory")


class _MscSwAvListTidiedValue_Type(AsciiString):
    """Custom type mscSwAvListTidiedValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_MscSwAvListTidiedValue_Type.__name__ = "AsciiString"
_MscSwAvListTidiedValue_Object = MibTableColumn
mscSwAvListTidiedValue = _MscSwAvListTidiedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 423, 1, 1),
    _MscSwAvListTidiedValue_Type()
)
mscSwAvListTidiedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSwAvListTidiedValue.setStatus("mandatory")
_MscSwPatlTable_Object = MibTable
mscSwPatlTable = _MscSwPatlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 436)
)
if mibBuilder.loadTexts:
    mscSwPatlTable.setStatus("mandatory")
_MscSwPatlEntry_Object = MibTableRow
mscSwPatlEntry = _MscSwPatlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 436, 1)
)
mscSwPatlEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwPatlValue"),
)
if mibBuilder.loadTexts:
    mscSwPatlEntry.setStatus("mandatory")


class _MscSwPatlValue_Type(AsciiString):
    """Custom type mscSwPatlValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_MscSwPatlValue_Type.__name__ = "AsciiString"
_MscSwPatlValue_Object = MibTableColumn
mscSwPatlValue = _MscSwPatlValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 436, 1, 1),
    _MscSwPatlValue_Type()
)
mscSwPatlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSwPatlValue.setStatus("mandatory")
_MscSwPatlRowStatus_Type = RowStatus
_MscSwPatlRowStatus_Object = MibTableColumn
mscSwPatlRowStatus = _MscSwPatlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 436, 1, 2),
    _MscSwPatlRowStatus_Type()
)
mscSwPatlRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscSwPatlRowStatus.setStatus("mandatory")
_SoftwareMIB_ObjectIdentity = ObjectIdentity
softwareMIB = _SoftwareMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 17)
)
_SoftwareGroup_ObjectIdentity = ObjectIdentity
softwareGroup = _SoftwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 17, 1)
)
_SoftwareGroupCA_ObjectIdentity = ObjectIdentity
softwareGroupCA = _SoftwareGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 17, 1, 1)
)
_SoftwareGroupCA02_ObjectIdentity = ObjectIdentity
softwareGroupCA02 = _SoftwareGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 17, 1, 1, 3)
)
_SoftwareGroupCA02A_ObjectIdentity = ObjectIdentity
softwareGroupCA02A = _SoftwareGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 17, 1, 1, 3, 2)
)
_SoftwareCapabilities_ObjectIdentity = ObjectIdentity
softwareCapabilities = _SoftwareCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 17, 3)
)
_SoftwareCapabilitiesCA_ObjectIdentity = ObjectIdentity
softwareCapabilitiesCA = _SoftwareCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 17, 3, 1)
)
_SoftwareCapabilitiesCA02_ObjectIdentity = ObjectIdentity
softwareCapabilitiesCA02 = _SoftwareCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 17, 3, 1, 3)
)
_SoftwareCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
softwareCapabilitiesCA02A = _SoftwareCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 17, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-SoftwareMIB",
    **{"mscSw": mscSw,
       "mscSwRowStatusTable": mscSwRowStatusTable,
       "mscSwRowStatusEntry": mscSwRowStatusEntry,
       "mscSwRowStatus": mscSwRowStatus,
       "mscSwComponentName": mscSwComponentName,
       "mscSwStorageType": mscSwStorageType,
       "mscSwIndex": mscSwIndex,
       "mscSwDld": mscSwDld,
       "mscSwDldRowStatusTable": mscSwDldRowStatusTable,
       "mscSwDldRowStatusEntry": mscSwDldRowStatusEntry,
       "mscSwDldRowStatus": mscSwDldRowStatus,
       "mscSwDldComponentName": mscSwDldComponentName,
       "mscSwDldStorageType": mscSwDldStorageType,
       "mscSwDldIndex": mscSwDldIndex,
       "mscSwDldOperTable": mscSwDldOperTable,
       "mscSwDldOperEntry": mscSwDldOperEntry,
       "mscSwDldAvBeingDownloaded": mscSwDldAvBeingDownloaded,
       "mscSwDldStatus": mscSwDldStatus,
       "mscSwDldFilesToTransfer": mscSwDldFilesToTransfer,
       "mscSwDldProcessorTargets": mscSwDldProcessorTargets,
       "mscSwDldDldListTable": mscSwDldDldListTable,
       "mscSwDldDldListEntry": mscSwDldDldListEntry,
       "mscSwDldDldListValue": mscSwDldDldListValue,
       "mscSwDldDldListRowStatus": mscSwDldDldListRowStatus,
       "mscSwDldDownloadedAvListTable": mscSwDldDownloadedAvListTable,
       "mscSwDldDownloadedAvListEntry": mscSwDldDownloadedAvListEntry,
       "mscSwDldDownloadedAvListValue": mscSwDldDownloadedAvListValue,
       "mscSwAv": mscSwAv,
       "mscSwAvRowStatusTable": mscSwAvRowStatusTable,
       "mscSwAvRowStatusEntry": mscSwAvRowStatusEntry,
       "mscSwAvRowStatus": mscSwAvRowStatus,
       "mscSwAvComponentName": mscSwAvComponentName,
       "mscSwAvStorageType": mscSwAvStorageType,
       "mscSwAvIndex": mscSwAvIndex,
       "mscSwAvFeat": mscSwAvFeat,
       "mscSwAvFeatRowStatusTable": mscSwAvFeatRowStatusTable,
       "mscSwAvFeatRowStatusEntry": mscSwAvFeatRowStatusEntry,
       "mscSwAvFeatRowStatus": mscSwAvFeatRowStatus,
       "mscSwAvFeatComponentName": mscSwAvFeatComponentName,
       "mscSwAvFeatStorageType": mscSwAvFeatStorageType,
       "mscSwAvFeatIndex": mscSwAvFeatIndex,
       "mscSwAvPatch": mscSwAvPatch,
       "mscSwAvPatchRowStatusTable": mscSwAvPatchRowStatusTable,
       "mscSwAvPatchRowStatusEntry": mscSwAvPatchRowStatusEntry,
       "mscSwAvPatchRowStatus": mscSwAvPatchRowStatus,
       "mscSwAvPatchComponentName": mscSwAvPatchComponentName,
       "mscSwAvPatchStorageType": mscSwAvPatchStorageType,
       "mscSwAvPatchIndex": mscSwAvPatchIndex,
       "mscSwAvPatchOperTable": mscSwAvPatchOperTable,
       "mscSwAvPatchOperEntry": mscSwAvPatchOperEntry,
       "mscSwAvPatchDescription": mscSwAvPatchDescription,
       "mscSwAvOperTable": mscSwAvOperTable,
       "mscSwAvOperEntry": mscSwAvOperEntry,
       "mscSwAvProcessorTargets": mscSwAvProcessorTargets,
       "mscSwAvCompatibleAvListTable": mscSwAvCompatibleAvListTable,
       "mscSwAvCompatibleAvListEntry": mscSwAvCompatibleAvListEntry,
       "mscSwAvCompatibleAvListValue": mscSwAvCompatibleAvListValue,
       "mscSwLpt": mscSwLpt,
       "mscSwLptRowStatusTable": mscSwLptRowStatusTable,
       "mscSwLptRowStatusEntry": mscSwLptRowStatusEntry,
       "mscSwLptRowStatus": mscSwLptRowStatus,
       "mscSwLptComponentName": mscSwLptComponentName,
       "mscSwLptStorageType": mscSwLptStorageType,
       "mscSwLptIndex": mscSwLptIndex,
       "mscSwLptProvTable": mscSwLptProvTable,
       "mscSwLptProvEntry": mscSwLptProvEntry,
       "mscSwLptCommentText": mscSwLptCommentText,
       "mscSwLptSystemConfig": mscSwLptSystemConfig,
       "mscSwLptFlTable": mscSwLptFlTable,
       "mscSwLptFlEntry": mscSwLptFlEntry,
       "mscSwLptFlValue": mscSwLptFlValue,
       "mscSwLptFlRowStatus": mscSwLptFlRowStatus,
       "mscSwLptLogicalProcessorsTable": mscSwLptLogicalProcessorsTable,
       "mscSwLptLogicalProcessorsEntry": mscSwLptLogicalProcessorsEntry,
       "mscSwLptLogicalProcessorsValue": mscSwLptLogicalProcessorsValue,
       "mscSwOperTable": mscSwOperTable,
       "mscSwOperEntry": mscSwOperEntry,
       "mscSwTidyStatus": mscSwTidyStatus,
       "mscSwAvBeingTidied": mscSwAvBeingTidied,
       "mscSwAvlTable": mscSwAvlTable,
       "mscSwAvlEntry": mscSwAvlEntry,
       "mscSwAvlValue": mscSwAvlValue,
       "mscSwAvlRowStatus": mscSwAvlRowStatus,
       "mscSwAvListToTidyTable": mscSwAvListToTidyTable,
       "mscSwAvListToTidyEntry": mscSwAvListToTidyEntry,
       "mscSwAvListToTidyValue": mscSwAvListToTidyValue,
       "mscSwAvListTidiedTable": mscSwAvListTidiedTable,
       "mscSwAvListTidiedEntry": mscSwAvListTidiedEntry,
       "mscSwAvListTidiedValue": mscSwAvListTidiedValue,
       "mscSwPatlTable": mscSwPatlTable,
       "mscSwPatlEntry": mscSwPatlEntry,
       "mscSwPatlValue": mscSwPatlValue,
       "mscSwPatlRowStatus": mscSwPatlRowStatus,
       "softwareMIB": softwareMIB,
       "softwareGroup": softwareGroup,
       "softwareGroupCA": softwareGroupCA,
       "softwareGroupCA02": softwareGroupCA02,
       "softwareGroupCA02A": softwareGroupCA02A,
       "softwareCapabilities": softwareCapabilities,
       "softwareCapabilitiesCA": softwareCapabilitiesCA,
       "softwareCapabilitiesCA02": softwareCapabilitiesCA02,
       "softwareCapabilitiesCA02A": softwareCapabilitiesCA02A}
)
