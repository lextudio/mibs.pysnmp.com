# SNMP MIB module (BULK-DATA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BULK-DATA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:57 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

bulkDataMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 999)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BulkDataAgentCapabilities_ObjectIdentity = ObjectIdentity
bulkDataAgentCapabilities = _BulkDataAgentCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 1)
)


class _AcFileEncoding_Type(Integer32):
    """Custom type acFileEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("xml", 2))
    )


_AcFileEncoding_Type.__name__ = "Integer32"
_AcFileEncoding_Object = MibScalar
acFileEncoding = _AcFileEncoding_Object(
    (1, 3, 6, 1, 3, 999, 1, 1),
    _AcFileEncoding_Type()
)
acFileEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFileEncoding.setStatus("current")


class _AcFileCompression_Type(Integer32):
    """Custom type acFileCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bzip", 2),
          ("gzip", 3),
          ("noCompression", 1))
    )


_AcFileCompression_Type.__name__ = "Integer32"
_AcFileCompression_Object = MibScalar
acFileCompression = _AcFileCompression_Object(
    (1, 3, 6, 1, 3, 999, 1, 2),
    _AcFileCompression_Type()
)
acFileCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFileCompression.setStatus("current")


class _AcXferProtocol_Type(Integer32):
    """Custom type acXferProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cp", 1),
          ("ftp", 2),
          ("scp", 3))
    )


_AcXferProtocol_Type.__name__ = "Integer32"
_AcXferProtocol_Object = MibScalar
acXferProtocol = _AcXferProtocol_Object(
    (1, 3, 6, 1, 3, 999, 1, 3),
    _AcXferProtocol_Type()
)
acXferProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acXferProtocol.setStatus("current")
_BulkDataObjects_ObjectIdentity = ObjectIdentity
bulkDataObjects = _BulkDataObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 2)
)
_SliceTable_Object = MibTable
sliceTable = _SliceTable_Object(
    (1, 3, 6, 1, 3, 999, 2, 1)
)
if mibBuilder.loadTexts:
    sliceTable.setStatus("current")
_SliceEntry_Object = MibTableRow
sliceEntry = _SliceEntry_Object(
    (1, 3, 6, 1, 3, 999, 2, 1, 1)
)
sliceEntry.setIndexNames(
    (0, "BULK-DATA-MIB", "sliceIndex"),
    (0, "BULK-DATA-MIB", "sliceSubId"),
)
if mibBuilder.loadTexts:
    sliceEntry.setStatus("current")


class _SliceIndex_Type(Unsigned32):
    """Custom type sliceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SliceIndex_Type.__name__ = "Unsigned32"
_SliceIndex_Object = MibTableColumn
sliceIndex = _SliceIndex_Object(
    (1, 3, 6, 1, 3, 999, 2, 1, 1, 1),
    _SliceIndex_Type()
)
sliceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sliceIndex.setStatus("current")


class _SliceSubId_Type(Unsigned32):
    """Custom type sliceSubId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SliceSubId_Type.__name__ = "Unsigned32"
_SliceSubId_Object = MibTableColumn
sliceSubId = _SliceSubId_Object(
    (1, 3, 6, 1, 3, 999, 2, 1, 1, 2),
    _SliceSubId_Type()
)
sliceSubId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sliceSubId.setStatus("current")
_SliceColumnOID_Type = ObjectIdentifier
_SliceColumnOID_Object = MibTableColumn
sliceColumnOID = _SliceColumnOID_Object(
    (1, 3, 6, 1, 3, 999, 2, 1, 1, 3),
    _SliceColumnOID_Type()
)
sliceColumnOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sliceColumnOID.setStatus("current")
_SliceSnmpContext_Type = DisplayString
_SliceSnmpContext_Object = MibTableColumn
sliceSnmpContext = _SliceSnmpContext_Object(
    (1, 3, 6, 1, 3, 999, 2, 1, 1, 4),
    _SliceSnmpContext_Type()
)
sliceSnmpContext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sliceSnmpContext.setStatus("current")
_SliceColumnDisplayHint_Type = DisplayString
_SliceColumnDisplayHint_Object = MibTableColumn
sliceColumnDisplayHint = _SliceColumnDisplayHint_Object(
    (1, 3, 6, 1, 3, 999, 2, 1, 1, 5),
    _SliceColumnDisplayHint_Type()
)
sliceColumnDisplayHint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sliceColumnDisplayHint.setStatus("current")


class _SliceAdminString_Type(DisplayString):
    """Custom type sliceAdminString based on DisplayString"""
    defaultHexValue = ""


_SliceAdminString_Object = MibTableColumn
sliceAdminString = _SliceAdminString_Object(
    (1, 3, 6, 1, 3, 999, 2, 1, 1, 6),
    _SliceAdminString_Type()
)
sliceAdminString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sliceAdminString.setStatus("current")
_SliceEntryStatus_Type = RowStatus
_SliceEntryStatus_Object = MibTableColumn
sliceEntryStatus = _SliceEntryStatus_Object(
    (1, 3, 6, 1, 3, 999, 2, 1, 1, 7),
    _SliceEntryStatus_Type()
)
sliceEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sliceEntryStatus.setStatus("current")
_XferTable_Object = MibTable
xferTable = _XferTable_Object(
    (1, 3, 6, 1, 3, 999, 2, 2)
)
if mibBuilder.loadTexts:
    xferTable.setStatus("current")
_XferEntry_Object = MibTableRow
xferEntry = _XferEntry_Object(
    (1, 3, 6, 1, 3, 999, 2, 2, 1)
)
xferEntry.setIndexNames(
    (0, "BULK-DATA-MIB", "xferIndex"),
    (0, "BULK-DATA-MIB", "xferSubId"),
)
if mibBuilder.loadTexts:
    xferEntry.setStatus("current")


class _XferIndex_Type(Unsigned32):
    """Custom type xferIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_XferIndex_Type.__name__ = "Unsigned32"
_XferIndex_Object = MibTableColumn
xferIndex = _XferIndex_Object(
    (1, 3, 6, 1, 3, 999, 2, 2, 1, 1),
    _XferIndex_Type()
)
xferIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xferIndex.setStatus("current")
_XferSubId_Type = Unsigned32
_XferSubId_Object = MibTableColumn
xferSubId = _XferSubId_Object(
    (1, 3, 6, 1, 3, 999, 2, 2, 1, 2),
    _XferSubId_Type()
)
xferSubId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xferSubId.setStatus("current")


class _XferHostIpType_Type(InetAddressType):
    """Custom type xferHostIpType based on InetAddressType"""


_XferHostIpType_Object = MibTableColumn
xferHostIpType = _XferHostIpType_Object(
    (1, 3, 6, 1, 3, 999, 2, 2, 1, 3),
    _XferHostIpType_Type()
)
xferHostIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xferHostIpType.setStatus("current")
_XferHostIpAddr_Type = InetAddress
_XferHostIpAddr_Object = MibTableColumn
xferHostIpAddr = _XferHostIpAddr_Object(
    (1, 3, 6, 1, 3, 999, 2, 2, 1, 4),
    _XferHostIpAddr_Type()
)
xferHostIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xferHostIpAddr.setStatus("current")


class _XferProtocol_Type(Integer32):
    """Custom type xferProtocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cp", 1),
          ("ftp", 2),
          ("scp", 3))
    )


_XferProtocol_Type.__name__ = "Integer32"
_XferProtocol_Object = MibTableColumn
xferProtocol = _XferProtocol_Object(
    (1, 3, 6, 1, 3, 999, 2, 2, 1, 5),
    _XferProtocol_Type()
)
xferProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xferProtocol.setStatus("current")


class _XferWriteControl_Type(Integer32):
    """Custom type xferWriteControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failIfExists", 1),
          ("overwrite", 2))
    )


_XferWriteControl_Type.__name__ = "Integer32"
_XferWriteControl_Object = MibTableColumn
xferWriteControl = _XferWriteControl_Object(
    (1, 3, 6, 1, 3, 999, 2, 2, 1, 6),
    _XferWriteControl_Type()
)
xferWriteControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xferWriteControl.setStatus("current")
_XferFilePath_Type = DisplayString
_XferFilePath_Object = MibTableColumn
xferFilePath = _XferFilePath_Object(
    (1, 3, 6, 1, 3, 999, 2, 2, 1, 7),
    _XferFilePath_Type()
)
xferFilePath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xferFilePath.setStatus("current")
_XferAuthUsername_Type = DisplayString
_XferAuthUsername_Object = MibTableColumn
xferAuthUsername = _XferAuthUsername_Object(
    (1, 3, 6, 1, 3, 999, 2, 2, 1, 8),
    _XferAuthUsername_Type()
)
xferAuthUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xferAuthUsername.setStatus("current")
_XferAuthPassword_Type = DisplayString
_XferAuthPassword_Object = MibTableColumn
xferAuthPassword = _XferAuthPassword_Object(
    (1, 3, 6, 1, 3, 999, 2, 2, 1, 9),
    _XferAuthPassword_Type()
)
xferAuthPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xferAuthPassword.setStatus("current")


class _XferAdminString_Type(DisplayString):
    """Custom type xferAdminString based on DisplayString"""
    defaultHexValue = ""


_XferAdminString_Object = MibTableColumn
xferAdminString = _XferAdminString_Object(
    (1, 3, 6, 1, 3, 999, 2, 2, 1, 10),
    _XferAdminString_Type()
)
xferAdminString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xferAdminString.setStatus("current")
_XferEntryStatus_Type = RowStatus
_XferEntryStatus_Object = MibTableColumn
xferEntryStatus = _XferEntryStatus_Object(
    (1, 3, 6, 1, 3, 999, 2, 2, 1, 11),
    _XferEntryStatus_Type()
)
xferEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xferEntryStatus.setStatus("current")
_SnapshotTable_Object = MibTable
snapshotTable = _SnapshotTable_Object(
    (1, 3, 6, 1, 3, 999, 2, 3)
)
if mibBuilder.loadTexts:
    snapshotTable.setStatus("current")
_SnapshotEntry_Object = MibTableRow
snapshotEntry = _SnapshotEntry_Object(
    (1, 3, 6, 1, 3, 999, 2, 3, 1)
)
snapshotEntry.setIndexNames(
    (0, "BULK-DATA-MIB", "snapshotIndex"),
    (0, "BULK-DATA-MIB", "snapshotSliceIndex"),
    (0, "BULK-DATA-MIB", "snapshotXferId"),
)
if mibBuilder.loadTexts:
    snapshotEntry.setStatus("current")


class _SnapshotIndex_Type(Unsigned32):
    """Custom type snapshotIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SnapshotIndex_Type.__name__ = "Unsigned32"
_SnapshotIndex_Object = MibTableColumn
snapshotIndex = _SnapshotIndex_Object(
    (1, 3, 6, 1, 3, 999, 2, 3, 1, 1),
    _SnapshotIndex_Type()
)
snapshotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snapshotIndex.setStatus("current")
_SnapshotSliceIndex_Type = Unsigned32
_SnapshotSliceIndex_Object = MibTableColumn
snapshotSliceIndex = _SnapshotSliceIndex_Object(
    (1, 3, 6, 1, 3, 999, 2, 3, 1, 2),
    _SnapshotSliceIndex_Type()
)
snapshotSliceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snapshotSliceIndex.setStatus("current")
_SnapshotXferId_Type = Unsigned32
_SnapshotXferId_Object = MibTableColumn
snapshotXferId = _SnapshotXferId_Object(
    (1, 3, 6, 1, 3, 999, 2, 3, 1, 3),
    _SnapshotXferId_Type()
)
snapshotXferId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snapshotXferId.setStatus("current")
_SnapshotSnapFileName_Type = DisplayString
_SnapshotSnapFileName_Object = MibTableColumn
snapshotSnapFileName = _SnapshotSnapFileName_Object(
    (1, 3, 6, 1, 3, 999, 2, 3, 1, 4),
    _SnapshotSnapFileName_Type()
)
snapshotSnapFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snapshotSnapFileName.setStatus("current")


class _SnapshotFileEncoding_Type(Integer32):
    """Custom type snapshotFileEncoding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("xml", 2))
    )


_SnapshotFileEncoding_Type.__name__ = "Integer32"
_SnapshotFileEncoding_Object = MibTableColumn
snapshotFileEncoding = _SnapshotFileEncoding_Object(
    (1, 3, 6, 1, 3, 999, 2, 3, 1, 5),
    _SnapshotFileEncoding_Type()
)
snapshotFileEncoding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snapshotFileEncoding.setStatus("current")


class _SnapshotFileCompression_Type(Integer32):
    """Custom type snapshotFileCompression based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bzip", 2),
          ("gzip", 3),
          ("noCompression", 1))
    )


_SnapshotFileCompression_Type.__name__ = "Integer32"
_SnapshotFileCompression_Object = MibTableColumn
snapshotFileCompression = _SnapshotFileCompression_Object(
    (1, 3, 6, 1, 3, 999, 2, 3, 1, 6),
    _SnapshotFileCompression_Type()
)
snapshotFileCompression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snapshotFileCompression.setStatus("current")
_SnapshotStartTime_Type = TimeStamp
_SnapshotStartTime_Object = MibTableColumn
snapshotStartTime = _SnapshotStartTime_Object(
    (1, 3, 6, 1, 3, 999, 2, 3, 1, 7),
    _SnapshotStartTime_Type()
)
snapshotStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotStartTime.setStatus("current")
_SnapshotCompletionTime_Type = TimeStamp
_SnapshotCompletionTime_Object = MibTableColumn
snapshotCompletionTime = _SnapshotCompletionTime_Object(
    (1, 3, 6, 1, 3, 999, 2, 3, 1, 8),
    _SnapshotCompletionTime_Type()
)
snapshotCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotCompletionTime.setStatus("current")
_SnapshotFileSize_Type = Unsigned32
_SnapshotFileSize_Object = MibTableColumn
snapshotFileSize = _SnapshotFileSize_Object(
    (1, 3, 6, 1, 3, 999, 2, 3, 1, 9),
    _SnapshotFileSize_Type()
)
snapshotFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotFileSize.setStatus("current")


class _SnapshotState_Type(Integer32):
    """Custom type snapshotState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 7),
          ("badName", 4),
          ("noMem", 6),
          ("noSpace", 3),
          ("ready", 2),
          ("running", 1),
          ("writeErr", 5))
    )


_SnapshotState_Type.__name__ = "Integer32"
_SnapshotState_Object = MibTableColumn
snapshotState = _SnapshotState_Object(
    (1, 3, 6, 1, 3, 999, 2, 3, 1, 10),
    _SnapshotState_Type()
)
snapshotState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotState.setStatus("current")


class _SnapshotAdminString_Type(DisplayString):
    """Custom type snapshotAdminString based on DisplayString"""
    defaultHexValue = ""


_SnapshotAdminString_Object = MibTableColumn
snapshotAdminString = _SnapshotAdminString_Object(
    (1, 3, 6, 1, 3, 999, 2, 3, 1, 11),
    _SnapshotAdminString_Type()
)
snapshotAdminString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snapshotAdminString.setStatus("current")
_SnapshotEntryStatus_Type = RowStatus
_SnapshotEntryStatus_Object = MibTableColumn
snapshotEntryStatus = _SnapshotEntryStatus_Object(
    (1, 3, 6, 1, 3, 999, 2, 3, 1, 12),
    _SnapshotEntryStatus_Type()
)
snapshotEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snapshotEntryStatus.setStatus("current")
_XferCtlTable_Object = MibTable
xferCtlTable = _XferCtlTable_Object(
    (1, 3, 6, 1, 3, 999, 2, 4)
)
if mibBuilder.loadTexts:
    xferCtlTable.setStatus("current")
_XferCtlEntry_Object = MibTableRow
xferCtlEntry = _XferCtlEntry_Object(
    (1, 3, 6, 1, 3, 999, 2, 4, 1)
)
xferCtlEntry.setIndexNames(
    (0, "BULK-DATA-MIB", "xferCtlIndex"),
    (0, "BULK-DATA-MIB", "sliceIndex"),
    (0, "BULK-DATA-MIB", "xferIndex"),
    (0, "BULK-DATA-MIB", "xferSubId"),
)
if mibBuilder.loadTexts:
    xferCtlEntry.setStatus("current")


class _XferCtlIndex_Type(Unsigned32):
    """Custom type xferCtlIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_XferCtlIndex_Type.__name__ = "Unsigned32"
_XferCtlIndex_Object = MibTableColumn
xferCtlIndex = _XferCtlIndex_Object(
    (1, 3, 6, 1, 3, 999, 2, 4, 1, 1),
    _XferCtlIndex_Type()
)
xferCtlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xferCtlIndex.setStatus("current")
_XferCtlStartTime_Type = TimeStamp
_XferCtlStartTime_Object = MibTableColumn
xferCtlStartTime = _XferCtlStartTime_Object(
    (1, 3, 6, 1, 3, 999, 2, 4, 1, 2),
    _XferCtlStartTime_Type()
)
xferCtlStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xferCtlStartTime.setStatus("current")
_XferCtlCompletionTime_Type = TimeStamp
_XferCtlCompletionTime_Object = MibTableColumn
xferCtlCompletionTime = _XferCtlCompletionTime_Object(
    (1, 3, 6, 1, 3, 999, 2, 4, 1, 3),
    _XferCtlCompletionTime_Type()
)
xferCtlCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xferCtlCompletionTime.setStatus("current")


class _XferCtlPercentXferred_Type(Unsigned32):
    """Custom type xferCtlPercentXferred based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XferCtlPercentXferred_Type.__name__ = "Unsigned32"
_XferCtlPercentXferred_Object = MibTableColumn
xferCtlPercentXferred = _XferCtlPercentXferred_Object(
    (1, 3, 6, 1, 3, 999, 2, 4, 1, 4),
    _XferCtlPercentXferred_Type()
)
xferCtlPercentXferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xferCtlPercentXferred.setStatus("current")


class _XferCtlStatus_Type(Integer32):
    """Custom type xferCtlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("abortXfer", 7),
          ("badLogin", 6),
          ("badName", 4),
          ("complete", 2),
          ("deleteRow", 9),
          ("inProgress", 1),
          ("noSpace", 3),
          ("retryXfer", 8),
          ("writeErr", 5))
    )


_XferCtlStatus_Type.__name__ = "Integer32"
_XferCtlStatus_Object = MibTableColumn
xferCtlStatus = _XferCtlStatus_Object(
    (1, 3, 6, 1, 3, 999, 2, 4, 1, 5),
    _XferCtlStatus_Type()
)
xferCtlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xferCtlStatus.setStatus("current")
_BulkDataTraps_ObjectIdentity = ObjectIdentity
bulkDataTraps = _BulkDataTraps_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 3)
)
_BulkMIBConformance_ObjectIdentity = ObjectIdentity
bulkMIBConformance = _BulkMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 4)
)
_BulkMIBCompliances_ObjectIdentity = ObjectIdentity
bulkMIBCompliances = _BulkMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 4, 1)
)
_BulkMIBGroups_ObjectIdentity = ObjectIdentity
bulkMIBGroups = _BulkMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 4, 2)
)

# Managed Objects groups

bulkCapabilitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 999, 4, 2, 1)
)
bulkCapabilitiesGroup.setObjects(
      *(("BULK-DATA-MIB", "acFileEncoding"),
        ("BULK-DATA-MIB", "acFileCompression"),
        ("BULK-DATA-MIB", "acXferProtocol"))
)
if mibBuilder.loadTexts:
    bulkCapabilitiesGroup.setStatus("current")

bulkSliceGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 999, 4, 2, 2)
)
bulkSliceGroup.setObjects(
      *(("BULK-DATA-MIB", "sliceColumnOID"),
        ("BULK-DATA-MIB", "sliceSnmpContext"),
        ("BULK-DATA-MIB", "sliceColumnDisplayHint"),
        ("BULK-DATA-MIB", "sliceAdminString"),
        ("BULK-DATA-MIB", "sliceEntryStatus"))
)
if mibBuilder.loadTexts:
    bulkSliceGroup.setStatus("current")

bulkFileTransferGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 999, 4, 2, 3)
)
bulkFileTransferGroup.setObjects(
      *(("BULK-DATA-MIB", "xferHostIpType"),
        ("BULK-DATA-MIB", "xferHostIpAddr"),
        ("BULK-DATA-MIB", "xferProtocol"),
        ("BULK-DATA-MIB", "xferWriteControl"),
        ("BULK-DATA-MIB", "xferFilePath"),
        ("BULK-DATA-MIB", "xferAuthUsername"),
        ("BULK-DATA-MIB", "xferAuthPassword"),
        ("BULK-DATA-MIB", "xferAdminString"),
        ("BULK-DATA-MIB", "xferEntryStatus"))
)
if mibBuilder.loadTexts:
    bulkFileTransferGroup.setStatus("current")

bulkSnapshotGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 999, 4, 2, 4)
)
bulkSnapshotGroup.setObjects(
      *(("BULK-DATA-MIB", "snapshotSnapFileName"),
        ("BULK-DATA-MIB", "snapshotFileEncoding"),
        ("BULK-DATA-MIB", "snapshotFileCompression"),
        ("BULK-DATA-MIB", "snapshotStartTime"),
        ("BULK-DATA-MIB", "snapshotCompletionTime"),
        ("BULK-DATA-MIB", "snapshotFileSize"),
        ("BULK-DATA-MIB", "snapshotState"),
        ("BULK-DATA-MIB", "snapshotAdminString"),
        ("BULK-DATA-MIB", "snapshotEntryStatus"))
)
if mibBuilder.loadTexts:
    bulkSnapshotGroup.setStatus("current")

bulkXferCtlGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 999, 4, 2, 5)
)
bulkXferCtlGroup.setObjects(
      *(("BULK-DATA-MIB", "xferCtlStartTime"),
        ("BULK-DATA-MIB", "xferCtlCompletionTime"),
        ("BULK-DATA-MIB", "xferCtlPercentXferred"),
        ("BULK-DATA-MIB", "xferCtlStatus"))
)
if mibBuilder.loadTexts:
    bulkXferCtlGroup.setStatus("current")


# Notification objects

bulkDataXfer = NotificationType(
    (1, 3, 6, 1, 3, 999, 3, 1)
)
bulkDataXfer.setObjects(
    ("BULK-DATA-MIB", "xferCtlStatus")
)
if mibBuilder.loadTexts:
    bulkDataXfer.setStatus(
        "current"
    )


# Notifications groups

bulkTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 3, 999, 4, 2, 6)
)
bulkTrapGroup.setObjects(
    ("BULK-DATA-MIB", "bulkDataXfer")
)
if mibBuilder.loadTexts:
    bulkTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

bulkMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 999, 4, 1, 1)
)
if mibBuilder.loadTexts:
    bulkMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BULK-DATA-MIB",
    **{"bulkDataMIB": bulkDataMIB,
       "bulkDataAgentCapabilities": bulkDataAgentCapabilities,
       "acFileEncoding": acFileEncoding,
       "acFileCompression": acFileCompression,
       "acXferProtocol": acXferProtocol,
       "bulkDataObjects": bulkDataObjects,
       "sliceTable": sliceTable,
       "sliceEntry": sliceEntry,
       "sliceIndex": sliceIndex,
       "sliceSubId": sliceSubId,
       "sliceColumnOID": sliceColumnOID,
       "sliceSnmpContext": sliceSnmpContext,
       "sliceColumnDisplayHint": sliceColumnDisplayHint,
       "sliceAdminString": sliceAdminString,
       "sliceEntryStatus": sliceEntryStatus,
       "xferTable": xferTable,
       "xferEntry": xferEntry,
       "xferIndex": xferIndex,
       "xferSubId": xferSubId,
       "xferHostIpType": xferHostIpType,
       "xferHostIpAddr": xferHostIpAddr,
       "xferProtocol": xferProtocol,
       "xferWriteControl": xferWriteControl,
       "xferFilePath": xferFilePath,
       "xferAuthUsername": xferAuthUsername,
       "xferAuthPassword": xferAuthPassword,
       "xferAdminString": xferAdminString,
       "xferEntryStatus": xferEntryStatus,
       "snapshotTable": snapshotTable,
       "snapshotEntry": snapshotEntry,
       "snapshotIndex": snapshotIndex,
       "snapshotSliceIndex": snapshotSliceIndex,
       "snapshotXferId": snapshotXferId,
       "snapshotSnapFileName": snapshotSnapFileName,
       "snapshotFileEncoding": snapshotFileEncoding,
       "snapshotFileCompression": snapshotFileCompression,
       "snapshotStartTime": snapshotStartTime,
       "snapshotCompletionTime": snapshotCompletionTime,
       "snapshotFileSize": snapshotFileSize,
       "snapshotState": snapshotState,
       "snapshotAdminString": snapshotAdminString,
       "snapshotEntryStatus": snapshotEntryStatus,
       "xferCtlTable": xferCtlTable,
       "xferCtlEntry": xferCtlEntry,
       "xferCtlIndex": xferCtlIndex,
       "xferCtlStartTime": xferCtlStartTime,
       "xferCtlCompletionTime": xferCtlCompletionTime,
       "xferCtlPercentXferred": xferCtlPercentXferred,
       "xferCtlStatus": xferCtlStatus,
       "bulkDataTraps": bulkDataTraps,
       "bulkDataXfer": bulkDataXfer,
       "bulkMIBConformance": bulkMIBConformance,
       "bulkMIBCompliances": bulkMIBCompliances,
       "bulkMIBCompliance": bulkMIBCompliance,
       "bulkMIBGroups": bulkMIBGroups,
       "bulkCapabilitiesGroup": bulkCapabilitiesGroup,
       "bulkSliceGroup": bulkSliceGroup,
       "bulkFileTransferGroup": bulkFileTransferGroup,
       "bulkSnapshotGroup": bulkSnapshotGroup,
       "bulkXferCtlGroup": bulkXferCtlGroup,
       "bulkTrapGroup": bulkTrapGroup}
)
