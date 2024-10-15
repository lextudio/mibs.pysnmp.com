# SNMP MIB module (Nortel-Magellan-Passport-SoftwareMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-SoftwareMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:22 2024
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
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 AsciiStringIndex,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
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

_Sw_ObjectIdentity = ObjectIdentity
sw = _Sw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14)
)
_SwRowStatusTable_Object = MibTable
swRowStatusTable = _SwRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 1)
)
if mibBuilder.loadTexts:
    swRowStatusTable.setStatus("mandatory")
_SwRowStatusEntry_Object = MibTableRow
swRowStatusEntry = _SwRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 1, 1)
)
swRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"),
)
if mibBuilder.loadTexts:
    swRowStatusEntry.setStatus("mandatory")
_SwRowStatus_Type = RowStatus
_SwRowStatus_Object = MibTableColumn
swRowStatus = _SwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 1, 1, 1),
    _SwRowStatus_Type()
)
swRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRowStatus.setStatus("mandatory")
_SwComponentName_Type = DisplayString
_SwComponentName_Object = MibTableColumn
swComponentName = _SwComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 1, 1, 2),
    _SwComponentName_Type()
)
swComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swComponentName.setStatus("mandatory")
_SwStorageType_Type = StorageType
_SwStorageType_Object = MibTableColumn
swStorageType = _SwStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 1, 1, 4),
    _SwStorageType_Type()
)
swStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStorageType.setStatus("mandatory")
_SwIndex_Type = NonReplicated
_SwIndex_Object = MibTableColumn
swIndex = _SwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 1, 1, 10),
    _SwIndex_Type()
)
swIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swIndex.setStatus("mandatory")
_SwDld_ObjectIdentity = ObjectIdentity
swDld = _SwDld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2)
)
_SwDldRowStatusTable_Object = MibTable
swDldRowStatusTable = _SwDldRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 1)
)
if mibBuilder.loadTexts:
    swDldRowStatusTable.setStatus("mandatory")
_SwDldRowStatusEntry_Object = MibTableRow
swDldRowStatusEntry = _SwDldRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 1, 1)
)
swDldRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swDldIndex"),
)
if mibBuilder.loadTexts:
    swDldRowStatusEntry.setStatus("mandatory")
_SwDldRowStatus_Type = RowStatus
_SwDldRowStatus_Object = MibTableColumn
swDldRowStatus = _SwDldRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 1, 1, 1),
    _SwDldRowStatus_Type()
)
swDldRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDldRowStatus.setStatus("mandatory")
_SwDldComponentName_Type = DisplayString
_SwDldComponentName_Object = MibTableColumn
swDldComponentName = _SwDldComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 1, 1, 2),
    _SwDldComponentName_Type()
)
swDldComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDldComponentName.setStatus("mandatory")
_SwDldStorageType_Type = StorageType
_SwDldStorageType_Object = MibTableColumn
swDldStorageType = _SwDldStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 1, 1, 4),
    _SwDldStorageType_Type()
)
swDldStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDldStorageType.setStatus("mandatory")
_SwDldIndex_Type = NonReplicated
_SwDldIndex_Object = MibTableColumn
swDldIndex = _SwDldIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 1, 1, 10),
    _SwDldIndex_Type()
)
swDldIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDldIndex.setStatus("mandatory")
_SwDldOperTable_Object = MibTable
swDldOperTable = _SwDldOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 10)
)
if mibBuilder.loadTexts:
    swDldOperTable.setStatus("mandatory")
_SwDldOperEntry_Object = MibTableRow
swDldOperEntry = _SwDldOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 10, 1)
)
swDldOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swDldIndex"),
)
if mibBuilder.loadTexts:
    swDldOperEntry.setStatus("mandatory")


class _SwDldAvBeingDownloaded_Type(AsciiString):
    """Custom type swDldAvBeingDownloaded based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SwDldAvBeingDownloaded_Type.__name__ = "AsciiString"
_SwDldAvBeingDownloaded_Object = MibTableColumn
swDldAvBeingDownloaded = _SwDldAvBeingDownloaded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 10, 1, 1),
    _SwDldAvBeingDownloaded_Type()
)
swDldAvBeingDownloaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDldAvBeingDownloaded.setStatus("mandatory")


class _SwDldStatus_Type(Integer32):
    """Custom type swDldStatus based on Integer32"""
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


_SwDldStatus_Type.__name__ = "Integer32"
_SwDldStatus_Object = MibTableColumn
swDldStatus = _SwDldStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 10, 1, 2),
    _SwDldStatus_Type()
)
swDldStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDldStatus.setStatus("mandatory")


class _SwDldFilesToTransfer_Type(Unsigned32):
    """Custom type swDldFilesToTransfer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SwDldFilesToTransfer_Type.__name__ = "Unsigned32"
_SwDldFilesToTransfer_Object = MibTableColumn
swDldFilesToTransfer = _SwDldFilesToTransfer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 10, 1, 3),
    _SwDldFilesToTransfer_Type()
)
swDldFilesToTransfer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDldFilesToTransfer.setStatus("mandatory")


class _SwDldProcessorTargets_Type(OctetString):
    """Custom type swDldProcessorTargets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SwDldProcessorTargets_Type.__name__ = "OctetString"
_SwDldProcessorTargets_Object = MibTableColumn
swDldProcessorTargets = _SwDldProcessorTargets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 10, 1, 4),
    _SwDldProcessorTargets_Type()
)
swDldProcessorTargets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDldProcessorTargets.setStatus("mandatory")
_SwDldDldListTable_Object = MibTable
swDldDldListTable = _SwDldDldListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 260)
)
if mibBuilder.loadTexts:
    swDldDldListTable.setStatus("mandatory")
_SwDldDldListEntry_Object = MibTableRow
swDldDldListEntry = _SwDldDldListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 260, 1)
)
swDldDldListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swDldIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swDldDldListValue"),
)
if mibBuilder.loadTexts:
    swDldDldListEntry.setStatus("mandatory")


class _SwDldDldListValue_Type(AsciiString):
    """Custom type swDldDldListValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_SwDldDldListValue_Type.__name__ = "AsciiString"
_SwDldDldListValue_Object = MibTableColumn
swDldDldListValue = _SwDldDldListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 260, 1, 1),
    _SwDldDldListValue_Type()
)
swDldDldListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDldDldListValue.setStatus("mandatory")
_SwDldDldListRowStatus_Type = RowStatus
_SwDldDldListRowStatus_Object = MibTableColumn
swDldDldListRowStatus = _SwDldDldListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 260, 1, 2),
    _SwDldDldListRowStatus_Type()
)
swDldDldListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    swDldDldListRowStatus.setStatus("mandatory")
_SwDldDownloadedAvListTable_Object = MibTable
swDldDownloadedAvListTable = _SwDldDownloadedAvListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 261)
)
if mibBuilder.loadTexts:
    swDldDownloadedAvListTable.setStatus("mandatory")
_SwDldDownloadedAvListEntry_Object = MibTableRow
swDldDownloadedAvListEntry = _SwDldDownloadedAvListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 261, 1)
)
swDldDownloadedAvListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swDldIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swDldDownloadedAvListValue"),
)
if mibBuilder.loadTexts:
    swDldDownloadedAvListEntry.setStatus("mandatory")


class _SwDldDownloadedAvListValue_Type(AsciiString):
    """Custom type swDldDownloadedAvListValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_SwDldDownloadedAvListValue_Type.__name__ = "AsciiString"
_SwDldDownloadedAvListValue_Object = MibTableColumn
swDldDownloadedAvListValue = _SwDldDownloadedAvListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 261, 1, 1),
    _SwDldDownloadedAvListValue_Type()
)
swDldDownloadedAvListValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDldDownloadedAvListValue.setStatus("mandatory")
_SwAv_ObjectIdentity = ObjectIdentity
swAv = _SwAv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3)
)
_SwAvRowStatusTable_Object = MibTable
swAvRowStatusTable = _SwAvRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 1)
)
if mibBuilder.loadTexts:
    swAvRowStatusTable.setStatus("mandatory")
_SwAvRowStatusEntry_Object = MibTableRow
swAvRowStatusEntry = _SwAvRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 1, 1)
)
swAvRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvIndex"),
)
if mibBuilder.loadTexts:
    swAvRowStatusEntry.setStatus("mandatory")
_SwAvRowStatus_Type = RowStatus
_SwAvRowStatus_Object = MibTableColumn
swAvRowStatus = _SwAvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 1, 1, 1),
    _SwAvRowStatus_Type()
)
swAvRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAvRowStatus.setStatus("mandatory")
_SwAvComponentName_Type = DisplayString
_SwAvComponentName_Object = MibTableColumn
swAvComponentName = _SwAvComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 1, 1, 2),
    _SwAvComponentName_Type()
)
swAvComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAvComponentName.setStatus("mandatory")
_SwAvStorageType_Type = StorageType
_SwAvStorageType_Object = MibTableColumn
swAvStorageType = _SwAvStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 1, 1, 4),
    _SwAvStorageType_Type()
)
swAvStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAvStorageType.setStatus("mandatory")


class _SwAvIndex_Type(AsciiStringIndex):
    """Custom type swAvIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_SwAvIndex_Type.__name__ = "AsciiStringIndex"
_SwAvIndex_Object = MibTableColumn
swAvIndex = _SwAvIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 1, 1, 10),
    _SwAvIndex_Type()
)
swAvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swAvIndex.setStatus("mandatory")
_SwAvFeat_ObjectIdentity = ObjectIdentity
swAvFeat = _SwAvFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 2)
)
_SwAvFeatRowStatusTable_Object = MibTable
swAvFeatRowStatusTable = _SwAvFeatRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 2, 1)
)
if mibBuilder.loadTexts:
    swAvFeatRowStatusTable.setStatus("mandatory")
_SwAvFeatRowStatusEntry_Object = MibTableRow
swAvFeatRowStatusEntry = _SwAvFeatRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 2, 1, 1)
)
swAvFeatRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvFeatIndex"),
)
if mibBuilder.loadTexts:
    swAvFeatRowStatusEntry.setStatus("mandatory")
_SwAvFeatRowStatus_Type = RowStatus
_SwAvFeatRowStatus_Object = MibTableColumn
swAvFeatRowStatus = _SwAvFeatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 2, 1, 1, 1),
    _SwAvFeatRowStatus_Type()
)
swAvFeatRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAvFeatRowStatus.setStatus("mandatory")
_SwAvFeatComponentName_Type = DisplayString
_SwAvFeatComponentName_Object = MibTableColumn
swAvFeatComponentName = _SwAvFeatComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 2, 1, 1, 2),
    _SwAvFeatComponentName_Type()
)
swAvFeatComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAvFeatComponentName.setStatus("mandatory")
_SwAvFeatStorageType_Type = StorageType
_SwAvFeatStorageType_Object = MibTableColumn
swAvFeatStorageType = _SwAvFeatStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 2, 1, 1, 4),
    _SwAvFeatStorageType_Type()
)
swAvFeatStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAvFeatStorageType.setStatus("mandatory")


class _SwAvFeatIndex_Type(AsciiStringIndex):
    """Custom type swAvFeatIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_SwAvFeatIndex_Type.__name__ = "AsciiStringIndex"
_SwAvFeatIndex_Object = MibTableColumn
swAvFeatIndex = _SwAvFeatIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 2, 1, 1, 10),
    _SwAvFeatIndex_Type()
)
swAvFeatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swAvFeatIndex.setStatus("mandatory")
_SwAvPatch_ObjectIdentity = ObjectIdentity
swAvPatch = _SwAvPatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 3)
)
_SwAvPatchRowStatusTable_Object = MibTable
swAvPatchRowStatusTable = _SwAvPatchRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 3, 1)
)
if mibBuilder.loadTexts:
    swAvPatchRowStatusTable.setStatus("mandatory")
_SwAvPatchRowStatusEntry_Object = MibTableRow
swAvPatchRowStatusEntry = _SwAvPatchRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 3, 1, 1)
)
swAvPatchRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvPatchIndex"),
)
if mibBuilder.loadTexts:
    swAvPatchRowStatusEntry.setStatus("mandatory")
_SwAvPatchRowStatus_Type = RowStatus
_SwAvPatchRowStatus_Object = MibTableColumn
swAvPatchRowStatus = _SwAvPatchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 3, 1, 1, 1),
    _SwAvPatchRowStatus_Type()
)
swAvPatchRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAvPatchRowStatus.setStatus("mandatory")
_SwAvPatchComponentName_Type = DisplayString
_SwAvPatchComponentName_Object = MibTableColumn
swAvPatchComponentName = _SwAvPatchComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 3, 1, 1, 2),
    _SwAvPatchComponentName_Type()
)
swAvPatchComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAvPatchComponentName.setStatus("mandatory")
_SwAvPatchStorageType_Type = StorageType
_SwAvPatchStorageType_Object = MibTableColumn
swAvPatchStorageType = _SwAvPatchStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 3, 1, 1, 4),
    _SwAvPatchStorageType_Type()
)
swAvPatchStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAvPatchStorageType.setStatus("mandatory")


class _SwAvPatchIndex_Type(AsciiStringIndex):
    """Custom type swAvPatchIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_SwAvPatchIndex_Type.__name__ = "AsciiStringIndex"
_SwAvPatchIndex_Object = MibTableColumn
swAvPatchIndex = _SwAvPatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 3, 1, 1, 10),
    _SwAvPatchIndex_Type()
)
swAvPatchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swAvPatchIndex.setStatus("mandatory")
_SwAvPatchOperTable_Object = MibTable
swAvPatchOperTable = _SwAvPatchOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 3, 10)
)
if mibBuilder.loadTexts:
    swAvPatchOperTable.setStatus("mandatory")
_SwAvPatchOperEntry_Object = MibTableRow
swAvPatchOperEntry = _SwAvPatchOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 3, 10, 1)
)
swAvPatchOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvPatchIndex"),
)
if mibBuilder.loadTexts:
    swAvPatchOperEntry.setStatus("mandatory")


class _SwAvPatchDescription_Type(AsciiString):
    """Custom type swAvPatchDescription based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SwAvPatchDescription_Type.__name__ = "AsciiString"
_SwAvPatchDescription_Object = MibTableColumn
swAvPatchDescription = _SwAvPatchDescription_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 3, 10, 1, 1),
    _SwAvPatchDescription_Type()
)
swAvPatchDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAvPatchDescription.setStatus("mandatory")
_SwAvOperTable_Object = MibTable
swAvOperTable = _SwAvOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 10)
)
if mibBuilder.loadTexts:
    swAvOperTable.setStatus("mandatory")
_SwAvOperEntry_Object = MibTableRow
swAvOperEntry = _SwAvOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 10, 1)
)
swAvOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvIndex"),
)
if mibBuilder.loadTexts:
    swAvOperEntry.setStatus("mandatory")


class _SwAvProcessorTargets_Type(OctetString):
    """Custom type swAvProcessorTargets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SwAvProcessorTargets_Type.__name__ = "OctetString"
_SwAvProcessorTargets_Object = MibTableColumn
swAvProcessorTargets = _SwAvProcessorTargets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 10, 1, 1),
    _SwAvProcessorTargets_Type()
)
swAvProcessorTargets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAvProcessorTargets.setStatus("mandatory")
_SwAvCompatibleAvListTable_Object = MibTable
swAvCompatibleAvListTable = _SwAvCompatibleAvListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 259)
)
if mibBuilder.loadTexts:
    swAvCompatibleAvListTable.setStatus("mandatory")
_SwAvCompatibleAvListEntry_Object = MibTableRow
swAvCompatibleAvListEntry = _SwAvCompatibleAvListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 259, 1)
)
swAvCompatibleAvListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvCompatibleAvListValue"),
)
if mibBuilder.loadTexts:
    swAvCompatibleAvListEntry.setStatus("mandatory")


class _SwAvCompatibleAvListValue_Type(AsciiString):
    """Custom type swAvCompatibleAvListValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_SwAvCompatibleAvListValue_Type.__name__ = "AsciiString"
_SwAvCompatibleAvListValue_Object = MibTableColumn
swAvCompatibleAvListValue = _SwAvCompatibleAvListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 259, 1, 1),
    _SwAvCompatibleAvListValue_Type()
)
swAvCompatibleAvListValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAvCompatibleAvListValue.setStatus("mandatory")
_SwLpt_ObjectIdentity = ObjectIdentity
swLpt = _SwLpt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4)
)
_SwLptRowStatusTable_Object = MibTable
swLptRowStatusTable = _SwLptRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 1)
)
if mibBuilder.loadTexts:
    swLptRowStatusTable.setStatus("mandatory")
_SwLptRowStatusEntry_Object = MibTableRow
swLptRowStatusEntry = _SwLptRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 1, 1)
)
swLptRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swLptIndex"),
)
if mibBuilder.loadTexts:
    swLptRowStatusEntry.setStatus("mandatory")
_SwLptRowStatus_Type = RowStatus
_SwLptRowStatus_Object = MibTableColumn
swLptRowStatus = _SwLptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 1, 1, 1),
    _SwLptRowStatus_Type()
)
swLptRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swLptRowStatus.setStatus("mandatory")
_SwLptComponentName_Type = DisplayString
_SwLptComponentName_Object = MibTableColumn
swLptComponentName = _SwLptComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 1, 1, 2),
    _SwLptComponentName_Type()
)
swLptComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLptComponentName.setStatus("mandatory")
_SwLptStorageType_Type = StorageType
_SwLptStorageType_Object = MibTableColumn
swLptStorageType = _SwLptStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 1, 1, 4),
    _SwLptStorageType_Type()
)
swLptStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLptStorageType.setStatus("mandatory")


class _SwLptIndex_Type(AsciiStringIndex):
    """Custom type swLptIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_SwLptIndex_Type.__name__ = "AsciiStringIndex"
_SwLptIndex_Object = MibTableColumn
swLptIndex = _SwLptIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 1, 1, 10),
    _SwLptIndex_Type()
)
swLptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swLptIndex.setStatus("mandatory")
_SwLptProvTable_Object = MibTable
swLptProvTable = _SwLptProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 10)
)
if mibBuilder.loadTexts:
    swLptProvTable.setStatus("mandatory")
_SwLptProvEntry_Object = MibTableRow
swLptProvEntry = _SwLptProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 10, 1)
)
swLptProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swLptIndex"),
)
if mibBuilder.loadTexts:
    swLptProvEntry.setStatus("mandatory")


class _SwLptCommentText_Type(AsciiString):
    """Custom type swLptCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwLptCommentText_Type.__name__ = "AsciiString"
_SwLptCommentText_Object = MibTableColumn
swLptCommentText = _SwLptCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 10, 1, 1),
    _SwLptCommentText_Type()
)
swLptCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swLptCommentText.setStatus("mandatory")


class _SwLptSystemConfig_Type(Integer32):
    """Custom type swLptSystemConfig based on Integer32"""
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


_SwLptSystemConfig_Type.__name__ = "Integer32"
_SwLptSystemConfig_Object = MibTableColumn
swLptSystemConfig = _SwLptSystemConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 10, 1, 2),
    _SwLptSystemConfig_Type()
)
swLptSystemConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swLptSystemConfig.setStatus("mandatory")
_SwLptFlTable_Object = MibTable
swLptFlTable = _SwLptFlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 257)
)
if mibBuilder.loadTexts:
    swLptFlTable.setStatus("mandatory")
_SwLptFlEntry_Object = MibTableRow
swLptFlEntry = _SwLptFlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 257, 1)
)
swLptFlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swLptIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swLptFlValue"),
)
if mibBuilder.loadTexts:
    swLptFlEntry.setStatus("mandatory")


class _SwLptFlValue_Type(AsciiString):
    """Custom type swLptFlValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_SwLptFlValue_Type.__name__ = "AsciiString"
_SwLptFlValue_Object = MibTableColumn
swLptFlValue = _SwLptFlValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 257, 1, 1),
    _SwLptFlValue_Type()
)
swLptFlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swLptFlValue.setStatus("mandatory")
_SwLptFlRowStatus_Type = RowStatus
_SwLptFlRowStatus_Object = MibTableColumn
swLptFlRowStatus = _SwLptFlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 257, 1, 2),
    _SwLptFlRowStatus_Type()
)
swLptFlRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    swLptFlRowStatus.setStatus("mandatory")
_SwLptLogicalProcessorsTable_Object = MibTable
swLptLogicalProcessorsTable = _SwLptLogicalProcessorsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 258)
)
if mibBuilder.loadTexts:
    swLptLogicalProcessorsTable.setStatus("mandatory")
_SwLptLogicalProcessorsEntry_Object = MibTableRow
swLptLogicalProcessorsEntry = _SwLptLogicalProcessorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 258, 1)
)
swLptLogicalProcessorsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swLptIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swLptLogicalProcessorsValue"),
)
if mibBuilder.loadTexts:
    swLptLogicalProcessorsEntry.setStatus("mandatory")
_SwLptLogicalProcessorsValue_Type = Link
_SwLptLogicalProcessorsValue_Object = MibTableColumn
swLptLogicalProcessorsValue = _SwLptLogicalProcessorsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 258, 1, 1),
    _SwLptLogicalProcessorsValue_Type()
)
swLptLogicalProcessorsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLptLogicalProcessorsValue.setStatus("mandatory")
_SwOperTable_Object = MibTable
swOperTable = _SwOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 11)
)
if mibBuilder.loadTexts:
    swOperTable.setStatus("mandatory")
_SwOperEntry_Object = MibTableRow
swOperEntry = _SwOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 11, 1)
)
swOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"),
)
if mibBuilder.loadTexts:
    swOperEntry.setStatus("mandatory")


class _SwTidyStatus_Type(Integer32):
    """Custom type swTidyStatus based on Integer32"""
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


_SwTidyStatus_Type.__name__ = "Integer32"
_SwTidyStatus_Object = MibTableColumn
swTidyStatus = _SwTidyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 11, 1, 1),
    _SwTidyStatus_Type()
)
swTidyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTidyStatus.setStatus("mandatory")


class _SwAvBeingTidied_Type(AsciiString):
    """Custom type swAvBeingTidied based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_SwAvBeingTidied_Type.__name__ = "AsciiString"
_SwAvBeingTidied_Object = MibTableColumn
swAvBeingTidied = _SwAvBeingTidied_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 11, 1, 421),
    _SwAvBeingTidied_Type()
)
swAvBeingTidied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAvBeingTidied.setStatus("mandatory")
_SwAvlTable_Object = MibTable
swAvlTable = _SwAvlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 256)
)
if mibBuilder.loadTexts:
    swAvlTable.setStatus("mandatory")
_SwAvlEntry_Object = MibTableRow
swAvlEntry = _SwAvlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 256, 1)
)
swAvlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvlValue"),
)
if mibBuilder.loadTexts:
    swAvlEntry.setStatus("mandatory")


class _SwAvlValue_Type(AsciiString):
    """Custom type swAvlValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_SwAvlValue_Type.__name__ = "AsciiString"
_SwAvlValue_Object = MibTableColumn
swAvlValue = _SwAvlValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 256, 1, 1),
    _SwAvlValue_Type()
)
swAvlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAvlValue.setStatus("mandatory")
_SwAvlRowStatus_Type = RowStatus
_SwAvlRowStatus_Object = MibTableColumn
swAvlRowStatus = _SwAvlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 256, 1, 2),
    _SwAvlRowStatus_Type()
)
swAvlRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    swAvlRowStatus.setStatus("mandatory")
_SwAvListToTidyTable_Object = MibTable
swAvListToTidyTable = _SwAvListToTidyTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 422)
)
if mibBuilder.loadTexts:
    swAvListToTidyTable.setStatus("mandatory")
_SwAvListToTidyEntry_Object = MibTableRow
swAvListToTidyEntry = _SwAvListToTidyEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 422, 1)
)
swAvListToTidyEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvListToTidyValue"),
)
if mibBuilder.loadTexts:
    swAvListToTidyEntry.setStatus("mandatory")


class _SwAvListToTidyValue_Type(AsciiString):
    """Custom type swAvListToTidyValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_SwAvListToTidyValue_Type.__name__ = "AsciiString"
_SwAvListToTidyValue_Object = MibTableColumn
swAvListToTidyValue = _SwAvListToTidyValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 422, 1, 1),
    _SwAvListToTidyValue_Type()
)
swAvListToTidyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAvListToTidyValue.setStatus("mandatory")
_SwAvListTidiedTable_Object = MibTable
swAvListTidiedTable = _SwAvListTidiedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 423)
)
if mibBuilder.loadTexts:
    swAvListTidiedTable.setStatus("mandatory")
_SwAvListTidiedEntry_Object = MibTableRow
swAvListTidiedEntry = _SwAvListTidiedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 423, 1)
)
swAvListTidiedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvListTidiedValue"),
)
if mibBuilder.loadTexts:
    swAvListTidiedEntry.setStatus("mandatory")


class _SwAvListTidiedValue_Type(AsciiString):
    """Custom type swAvListTidiedValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_SwAvListTidiedValue_Type.__name__ = "AsciiString"
_SwAvListTidiedValue_Object = MibTableColumn
swAvListTidiedValue = _SwAvListTidiedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 423, 1, 1),
    _SwAvListTidiedValue_Type()
)
swAvListTidiedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAvListTidiedValue.setStatus("mandatory")
_SwPatlTable_Object = MibTable
swPatlTable = _SwPatlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 436)
)
if mibBuilder.loadTexts:
    swPatlTable.setStatus("mandatory")
_SwPatlEntry_Object = MibTableRow
swPatlEntry = _SwPatlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 436, 1)
)
swPatlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"),
    (0, "Nortel-Magellan-Passport-SoftwareMIB", "swPatlValue"),
)
if mibBuilder.loadTexts:
    swPatlEntry.setStatus("mandatory")


class _SwPatlValue_Type(AsciiString):
    """Custom type swPatlValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_SwPatlValue_Type.__name__ = "AsciiString"
_SwPatlValue_Object = MibTableColumn
swPatlValue = _SwPatlValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 436, 1, 1),
    _SwPatlValue_Type()
)
swPatlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPatlValue.setStatus("mandatory")
_SwPatlRowStatus_Type = RowStatus
_SwPatlRowStatus_Object = MibTableColumn
swPatlRowStatus = _SwPatlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 436, 1, 2),
    _SwPatlRowStatus_Type()
)
swPatlRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    swPatlRowStatus.setStatus("mandatory")
_SoftwareMIB_ObjectIdentity = ObjectIdentity
softwareMIB = _SoftwareMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 17)
)
_SoftwareGroup_ObjectIdentity = ObjectIdentity
softwareGroup = _SoftwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 17, 1)
)
_SoftwareGroupBE_ObjectIdentity = ObjectIdentity
softwareGroupBE = _SoftwareGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 17, 1, 5)
)
_SoftwareGroupBE01_ObjectIdentity = ObjectIdentity
softwareGroupBE01 = _SoftwareGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 17, 1, 5, 2)
)
_SoftwareGroupBE01A_ObjectIdentity = ObjectIdentity
softwareGroupBE01A = _SoftwareGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 17, 1, 5, 2, 2)
)
_SoftwareCapabilities_ObjectIdentity = ObjectIdentity
softwareCapabilities = _SoftwareCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 17, 3)
)
_SoftwareCapabilitiesBE_ObjectIdentity = ObjectIdentity
softwareCapabilitiesBE = _SoftwareCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 17, 3, 5)
)
_SoftwareCapabilitiesBE01_ObjectIdentity = ObjectIdentity
softwareCapabilitiesBE01 = _SoftwareCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 17, 3, 5, 2)
)
_SoftwareCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
softwareCapabilitiesBE01A = _SoftwareCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 17, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-SoftwareMIB",
    **{"sw": sw,
       "swRowStatusTable": swRowStatusTable,
       "swRowStatusEntry": swRowStatusEntry,
       "swRowStatus": swRowStatus,
       "swComponentName": swComponentName,
       "swStorageType": swStorageType,
       "swIndex": swIndex,
       "swDld": swDld,
       "swDldRowStatusTable": swDldRowStatusTable,
       "swDldRowStatusEntry": swDldRowStatusEntry,
       "swDldRowStatus": swDldRowStatus,
       "swDldComponentName": swDldComponentName,
       "swDldStorageType": swDldStorageType,
       "swDldIndex": swDldIndex,
       "swDldOperTable": swDldOperTable,
       "swDldOperEntry": swDldOperEntry,
       "swDldAvBeingDownloaded": swDldAvBeingDownloaded,
       "swDldStatus": swDldStatus,
       "swDldFilesToTransfer": swDldFilesToTransfer,
       "swDldProcessorTargets": swDldProcessorTargets,
       "swDldDldListTable": swDldDldListTable,
       "swDldDldListEntry": swDldDldListEntry,
       "swDldDldListValue": swDldDldListValue,
       "swDldDldListRowStatus": swDldDldListRowStatus,
       "swDldDownloadedAvListTable": swDldDownloadedAvListTable,
       "swDldDownloadedAvListEntry": swDldDownloadedAvListEntry,
       "swDldDownloadedAvListValue": swDldDownloadedAvListValue,
       "swAv": swAv,
       "swAvRowStatusTable": swAvRowStatusTable,
       "swAvRowStatusEntry": swAvRowStatusEntry,
       "swAvRowStatus": swAvRowStatus,
       "swAvComponentName": swAvComponentName,
       "swAvStorageType": swAvStorageType,
       "swAvIndex": swAvIndex,
       "swAvFeat": swAvFeat,
       "swAvFeatRowStatusTable": swAvFeatRowStatusTable,
       "swAvFeatRowStatusEntry": swAvFeatRowStatusEntry,
       "swAvFeatRowStatus": swAvFeatRowStatus,
       "swAvFeatComponentName": swAvFeatComponentName,
       "swAvFeatStorageType": swAvFeatStorageType,
       "swAvFeatIndex": swAvFeatIndex,
       "swAvPatch": swAvPatch,
       "swAvPatchRowStatusTable": swAvPatchRowStatusTable,
       "swAvPatchRowStatusEntry": swAvPatchRowStatusEntry,
       "swAvPatchRowStatus": swAvPatchRowStatus,
       "swAvPatchComponentName": swAvPatchComponentName,
       "swAvPatchStorageType": swAvPatchStorageType,
       "swAvPatchIndex": swAvPatchIndex,
       "swAvPatchOperTable": swAvPatchOperTable,
       "swAvPatchOperEntry": swAvPatchOperEntry,
       "swAvPatchDescription": swAvPatchDescription,
       "swAvOperTable": swAvOperTable,
       "swAvOperEntry": swAvOperEntry,
       "swAvProcessorTargets": swAvProcessorTargets,
       "swAvCompatibleAvListTable": swAvCompatibleAvListTable,
       "swAvCompatibleAvListEntry": swAvCompatibleAvListEntry,
       "swAvCompatibleAvListValue": swAvCompatibleAvListValue,
       "swLpt": swLpt,
       "swLptRowStatusTable": swLptRowStatusTable,
       "swLptRowStatusEntry": swLptRowStatusEntry,
       "swLptRowStatus": swLptRowStatus,
       "swLptComponentName": swLptComponentName,
       "swLptStorageType": swLptStorageType,
       "swLptIndex": swLptIndex,
       "swLptProvTable": swLptProvTable,
       "swLptProvEntry": swLptProvEntry,
       "swLptCommentText": swLptCommentText,
       "swLptSystemConfig": swLptSystemConfig,
       "swLptFlTable": swLptFlTable,
       "swLptFlEntry": swLptFlEntry,
       "swLptFlValue": swLptFlValue,
       "swLptFlRowStatus": swLptFlRowStatus,
       "swLptLogicalProcessorsTable": swLptLogicalProcessorsTable,
       "swLptLogicalProcessorsEntry": swLptLogicalProcessorsEntry,
       "swLptLogicalProcessorsValue": swLptLogicalProcessorsValue,
       "swOperTable": swOperTable,
       "swOperEntry": swOperEntry,
       "swTidyStatus": swTidyStatus,
       "swAvBeingTidied": swAvBeingTidied,
       "swAvlTable": swAvlTable,
       "swAvlEntry": swAvlEntry,
       "swAvlValue": swAvlValue,
       "swAvlRowStatus": swAvlRowStatus,
       "swAvListToTidyTable": swAvListToTidyTable,
       "swAvListToTidyEntry": swAvListToTidyEntry,
       "swAvListToTidyValue": swAvListToTidyValue,
       "swAvListTidiedTable": swAvListTidiedTable,
       "swAvListTidiedEntry": swAvListTidiedEntry,
       "swAvListTidiedValue": swAvListTidiedValue,
       "swPatlTable": swPatlTable,
       "swPatlEntry": swPatlEntry,
       "swPatlValue": swPatlValue,
       "swPatlRowStatus": swPatlRowStatus,
       "softwareMIB": softwareMIB,
       "softwareGroup": softwareGroup,
       "softwareGroupBE": softwareGroupBE,
       "softwareGroupBE01": softwareGroupBE01,
       "softwareGroupBE01A": softwareGroupBE01A,
       "softwareCapabilities": softwareCapabilities,
       "softwareCapabilitiesBE": softwareCapabilitiesBE,
       "softwareCapabilitiesBE01": softwareCapabilitiesBE01,
       "softwareCapabilitiesBE01A": softwareCapabilitiesBE01A}
)
