# SNMP MIB module (CISCOSB-COPY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-COPY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:14:04 2024
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

(rndErrorDesc,
 rndErrorSeverity) = mibBuilder.importSymbols(
    "CISCOSB-DEVICEPARAMS-MIB",
    "rndErrorDesc",
    "rndErrorSeverity")

(rndNotifications,
 switch001) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "rndNotifications",
    "switch001")

(RlSecSdAccessType,) = mibBuilder.importSymbols(
    "CISCOSB-SECSD-MIB",
    "RlSecSdAccessType")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlCopy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87)
)
rlCopy.setRevisions(
        ("2010-07-25 00:00",
         "2010-05-11 00:00",
         "2010-02-17 00:00",
         "2009-08-10 00:00",
         "2006-02-02 00:00",
         "2003-09-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RlCopyApplicationType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cli", 2),
          ("ewb", 3),
          ("initerm", 5),
          ("mcli", 1),
          ("nms", 4),
          ("serial", 6))
    )



class RlCopyLocationType(Integer32, TextualConvention):
    status = "current"
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("anotherUnit", 2),
          ("http", 7),
          ("http-xml", 9),
          ("https", 8),
          ("https-xml", 10),
          ("local", 1),
          ("scp", 5),
          ("serial", 6),
          ("tftp", 3),
          ("xmodem", 4))
    )



class RlCopyFileType(Integer32, TextualConvention):
    status = "current"
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
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("backupConfig", 4),
          ("backupMibConfig", 7),
          ("boot", 9),
          ("image", 8),
          ("logging", 11),
          ("mirrorConfig", 12),
          ("null", 10),
          ("other", 1),
          ("runningConfig", 2),
          ("runningMibConfig", 5),
          ("startupConfig", 3),
          ("startupMibConfig", 6),
          ("usb", 13))
    )



class RlCopySecSdAccessType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("default", 4),
          ("exclude", 1),
          ("include-decrypted", 3),
          ("include-encrypted", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RlCopyMibVersion_Type = Integer32
_RlCopyMibVersion_Object = MibScalar
rlCopyMibVersion = _RlCopyMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 1),
    _RlCopyMibVersion_Type()
)
rlCopyMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyMibVersion.setStatus("current")
_RlCopyTable_Object = MibTable
rlCopyTable = _RlCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 2)
)
if mibBuilder.loadTexts:
    rlCopyTable.setStatus("current")
_RlCopyEntry_Object = MibTableRow
rlCopyEntry = _RlCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 2, 1)
)
rlCopyEntry.setIndexNames(
    (0, "CISCOSB-COPY-MIB", "rlCopyIndex"),
)
if mibBuilder.loadTexts:
    rlCopyEntry.setStatus("current")
_RlCopyIndex_Type = Integer32
_RlCopyIndex_Object = MibTableColumn
rlCopyIndex = _RlCopyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 2, 1, 1),
    _RlCopyIndex_Type()
)
rlCopyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyIndex.setStatus("current")
_RlCopyApplicationId_Type = RlCopyApplicationType
_RlCopyApplicationId_Object = MibTableColumn
rlCopyApplicationId = _RlCopyApplicationId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 2, 1, 2),
    _RlCopyApplicationId_Type()
)
rlCopyApplicationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyApplicationId.setStatus("current")
_RlCopySourceLocation_Type = RlCopyLocationType
_RlCopySourceLocation_Object = MibTableColumn
rlCopySourceLocation = _RlCopySourceLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 2, 1, 3),
    _RlCopySourceLocation_Type()
)
rlCopySourceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopySourceLocation.setStatus("current")
_RlCopySourceIpAddress_Type = IpAddress
_RlCopySourceIpAddress_Object = MibTableColumn
rlCopySourceIpAddress = _RlCopySourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 2, 1, 4),
    _RlCopySourceIpAddress_Type()
)
rlCopySourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopySourceIpAddress.setStatus("current")
_RlCopySourceUnitNumber_Type = Integer32
_RlCopySourceUnitNumber_Object = MibTableColumn
rlCopySourceUnitNumber = _RlCopySourceUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 2, 1, 5),
    _RlCopySourceUnitNumber_Type()
)
rlCopySourceUnitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopySourceUnitNumber.setStatus("current")
_RlCopySourceFileName_Type = DisplayString
_RlCopySourceFileName_Object = MibTableColumn
rlCopySourceFileName = _RlCopySourceFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 2, 1, 6),
    _RlCopySourceFileName_Type()
)
rlCopySourceFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopySourceFileName.setStatus("current")
_RlCopySourceFileType_Type = RlCopyFileType
_RlCopySourceFileType_Object = MibTableColumn
rlCopySourceFileType = _RlCopySourceFileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 2, 1, 7),
    _RlCopySourceFileType_Type()
)
rlCopySourceFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopySourceFileType.setStatus("current")
_RlCopyDestinationLocation_Type = RlCopyLocationType
_RlCopyDestinationLocation_Object = MibTableColumn
rlCopyDestinationLocation = _RlCopyDestinationLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 2, 1, 8),
    _RlCopyDestinationLocation_Type()
)
rlCopyDestinationLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyDestinationLocation.setStatus("current")
_RlCopyDestinationIpAddress_Type = IpAddress
_RlCopyDestinationIpAddress_Object = MibTableColumn
rlCopyDestinationIpAddress = _RlCopyDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 2, 1, 9),
    _RlCopyDestinationIpAddress_Type()
)
rlCopyDestinationIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyDestinationIpAddress.setStatus("current")
_RlCopyDestinationUnitNumber_Type = Integer32
_RlCopyDestinationUnitNumber_Object = MibTableColumn
rlCopyDestinationUnitNumber = _RlCopyDestinationUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 2, 1, 10),
    _RlCopyDestinationUnitNumber_Type()
)
rlCopyDestinationUnitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyDestinationUnitNumber.setStatus("current")
_RlCopyDestinationFileName_Type = DisplayString
_RlCopyDestinationFileName_Object = MibTableColumn
rlCopyDestinationFileName = _RlCopyDestinationFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 2, 1, 11),
    _RlCopyDestinationFileName_Type()
)
rlCopyDestinationFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyDestinationFileName.setStatus("current")
_RlCopyDestinationFileType_Type = RlCopyFileType
_RlCopyDestinationFileType_Object = MibTableColumn
rlCopyDestinationFileType = _RlCopyDestinationFileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 2, 1, 12),
    _RlCopyDestinationFileType_Type()
)
rlCopyDestinationFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyDestinationFileType.setStatus("current")
_RlCopyUpTime_Type = TimeTicks
_RlCopyUpTime_Object = MibTableColumn
rlCopyUpTime = _RlCopyUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 2, 1, 13),
    _RlCopyUpTime_Type()
)
rlCopyUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyUpTime.setStatus("current")


class _RlCopyOperationState_Type(Integer32):
    """Custom type rlCopyOperationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("copyFailed", 3),
          ("copyFinished", 5),
          ("copyTimedout", 4),
          ("downloadInProgress", 2),
          ("uploadInProgress", 1))
    )


_RlCopyOperationState_Type.__name__ = "Integer32"
_RlCopyOperationState_Object = MibTableColumn
rlCopyOperationState = _RlCopyOperationState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 2, 1, 14),
    _RlCopyOperationState_Type()
)
rlCopyOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyOperationState.setStatus("current")
_RlCopyBytesTransferred_Type = Integer32
_RlCopyBytesTransferred_Object = MibTableColumn
rlCopyBytesTransferred = _RlCopyBytesTransferred_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 2, 1, 15),
    _RlCopyBytesTransferred_Type()
)
rlCopyBytesTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyBytesTransferred.setStatus("current")


class _RlCopyInBackground_Type(Integer32):
    """Custom type rlCopyInBackground based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RlCopyInBackground_Type.__name__ = "Integer32"
_RlCopyInBackground_Object = MibTableColumn
rlCopyInBackground = _RlCopyInBackground_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 2, 1, 16),
    _RlCopyInBackground_Type()
)
rlCopyInBackground.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyInBackground.setStatus("current")
_RlCopyRowStatus_Type = RowStatus
_RlCopyRowStatus_Object = MibTableColumn
rlCopyRowStatus = _RlCopyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 2, 1, 17),
    _RlCopyRowStatus_Type()
)
rlCopyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyRowStatus.setStatus("current")


class _RlCopyHistoryIndex_Type(Integer32):
    """Custom type rlCopyHistoryIndex based on Integer32"""
    defaultValue = 0


_RlCopyHistoryIndex_Object = MibTableColumn
rlCopyHistoryIndex = _RlCopyHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 2, 1, 18),
    _RlCopyHistoryIndex_Type()
)
rlCopyHistoryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryIndex.setStatus("current")
_RlCopyFreeHistoryIndex_Type = Integer32
_RlCopyFreeHistoryIndex_Object = MibScalar
rlCopyFreeHistoryIndex = _RlCopyFreeHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 3),
    _RlCopyFreeHistoryIndex_Type()
)
rlCopyFreeHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyFreeHistoryIndex.setStatus("current")
_RlCopyHistoryTable_Object = MibTable
rlCopyHistoryTable = _RlCopyHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 4)
)
if mibBuilder.loadTexts:
    rlCopyHistoryTable.setStatus("current")
_RlCopyHistoryEntry_Object = MibTableRow
rlCopyHistoryEntry = _RlCopyHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 4, 1)
)
rlCopyHistoryEntry.setIndexNames(
    (0, "CISCOSB-COPY-MIB", "rlCopyHistoryHistoryIndex"),
)
if mibBuilder.loadTexts:
    rlCopyHistoryEntry.setStatus("current")
_RlCopyHistoryHistoryIndex_Type = Integer32
_RlCopyHistoryHistoryIndex_Object = MibTableColumn
rlCopyHistoryHistoryIndex = _RlCopyHistoryHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 4, 1, 1),
    _RlCopyHistoryHistoryIndex_Type()
)
rlCopyHistoryHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyHistoryHistoryIndex.setStatus("current")
_RlCopyHistoryApplicationId_Type = RlCopyApplicationType
_RlCopyHistoryApplicationId_Object = MibTableColumn
rlCopyHistoryApplicationId = _RlCopyHistoryApplicationId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 4, 1, 2),
    _RlCopyHistoryApplicationId_Type()
)
rlCopyHistoryApplicationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyHistoryApplicationId.setStatus("current")
_RlCopyHistorySourceLocation_Type = RlCopyLocationType
_RlCopyHistorySourceLocation_Object = MibTableColumn
rlCopyHistorySourceLocation = _RlCopyHistorySourceLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 4, 1, 3),
    _RlCopyHistorySourceLocation_Type()
)
rlCopyHistorySourceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistorySourceLocation.setStatus("current")
_RlCopyHistorySourceIpAddress_Type = IpAddress
_RlCopyHistorySourceIpAddress_Object = MibTableColumn
rlCopyHistorySourceIpAddress = _RlCopyHistorySourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 4, 1, 4),
    _RlCopyHistorySourceIpAddress_Type()
)
rlCopyHistorySourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistorySourceIpAddress.setStatus("current")
_RlCopyHistorySourceUnitNumber_Type = Integer32
_RlCopyHistorySourceUnitNumber_Object = MibTableColumn
rlCopyHistorySourceUnitNumber = _RlCopyHistorySourceUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 4, 1, 5),
    _RlCopyHistorySourceUnitNumber_Type()
)
rlCopyHistorySourceUnitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistorySourceUnitNumber.setStatus("current")
_RlCopyHistorySourceFileName_Type = DisplayString
_RlCopyHistorySourceFileName_Object = MibTableColumn
rlCopyHistorySourceFileName = _RlCopyHistorySourceFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 4, 1, 6),
    _RlCopyHistorySourceFileName_Type()
)
rlCopyHistorySourceFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistorySourceFileName.setStatus("current")
_RlCopyHistorySourceFileType_Type = RlCopyFileType
_RlCopyHistorySourceFileType_Object = MibTableColumn
rlCopyHistorySourceFileType = _RlCopyHistorySourceFileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 4, 1, 7),
    _RlCopyHistorySourceFileType_Type()
)
rlCopyHistorySourceFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistorySourceFileType.setStatus("current")
_RlCopyHistoryDestinationLocation_Type = RlCopyLocationType
_RlCopyHistoryDestinationLocation_Object = MibTableColumn
rlCopyHistoryDestinationLocation = _RlCopyHistoryDestinationLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 4, 1, 8),
    _RlCopyHistoryDestinationLocation_Type()
)
rlCopyHistoryDestinationLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryDestinationLocation.setStatus("current")
_RlCopyHistoryDestinationIpAddress_Type = IpAddress
_RlCopyHistoryDestinationIpAddress_Object = MibTableColumn
rlCopyHistoryDestinationIpAddress = _RlCopyHistoryDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 4, 1, 9),
    _RlCopyHistoryDestinationIpAddress_Type()
)
rlCopyHistoryDestinationIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryDestinationIpAddress.setStatus("current")
_RlCopyHistoryDestinationUnitNumber_Type = Integer32
_RlCopyHistoryDestinationUnitNumber_Object = MibTableColumn
rlCopyHistoryDestinationUnitNumber = _RlCopyHistoryDestinationUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 4, 1, 10),
    _RlCopyHistoryDestinationUnitNumber_Type()
)
rlCopyHistoryDestinationUnitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryDestinationUnitNumber.setStatus("current")
_RlCopyHistoryDestinationFileName_Type = DisplayString
_RlCopyHistoryDestinationFileName_Object = MibTableColumn
rlCopyHistoryDestinationFileName = _RlCopyHistoryDestinationFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 4, 1, 11),
    _RlCopyHistoryDestinationFileName_Type()
)
rlCopyHistoryDestinationFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryDestinationFileName.setStatus("current")
_RlCopyHistoryDestinationFileType_Type = RlCopyFileType
_RlCopyHistoryDestinationFileType_Object = MibTableColumn
rlCopyHistoryDestinationFileType = _RlCopyHistoryDestinationFileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 4, 1, 12),
    _RlCopyHistoryDestinationFileType_Type()
)
rlCopyHistoryDestinationFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryDestinationFileType.setStatus("current")
_RlCopyHistoryUpTime_Type = TimeTicks
_RlCopyHistoryUpTime_Object = MibTableColumn
rlCopyHistoryUpTime = _RlCopyHistoryUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 4, 1, 13),
    _RlCopyHistoryUpTime_Type()
)
rlCopyHistoryUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyHistoryUpTime.setStatus("current")


class _RlCopyHistoryOperationState_Type(Integer32):
    """Custom type rlCopyHistoryOperationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("copyFailed", 3),
          ("copyFinished", 5),
          ("copyTimedout", 4),
          ("downloadInProgress", 2),
          ("uploadInProgress", 1))
    )


_RlCopyHistoryOperationState_Type.__name__ = "Integer32"
_RlCopyHistoryOperationState_Object = MibTableColumn
rlCopyHistoryOperationState = _RlCopyHistoryOperationState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 4, 1, 14),
    _RlCopyHistoryOperationState_Type()
)
rlCopyHistoryOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyHistoryOperationState.setStatus("current")
_RlCopyHistoryBytesTransferred_Type = Integer32
_RlCopyHistoryBytesTransferred_Object = MibTableColumn
rlCopyHistoryBytesTransferred = _RlCopyHistoryBytesTransferred_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 4, 1, 15),
    _RlCopyHistoryBytesTransferred_Type()
)
rlCopyHistoryBytesTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyHistoryBytesTransferred.setStatus("current")


class _RlCopyHistoryInBackground_Type(Integer32):
    """Custom type rlCopyHistoryInBackground based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RlCopyHistoryInBackground_Type.__name__ = "Integer32"
_RlCopyHistoryInBackground_Object = MibTableColumn
rlCopyHistoryInBackground = _RlCopyHistoryInBackground_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 4, 1, 16),
    _RlCopyHistoryInBackground_Type()
)
rlCopyHistoryInBackground.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryInBackground.setStatus("current")
_RlCopyHistoryRowStatus_Type = RowStatus
_RlCopyHistoryRowStatus_Object = MibTableColumn
rlCopyHistoryRowStatus = _RlCopyHistoryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 4, 1, 17),
    _RlCopyHistoryRowStatus_Type()
)
rlCopyHistoryRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryRowStatus.setStatus("current")
_RlCopyHistoryErrorMessage_Type = DisplayString
_RlCopyHistoryErrorMessage_Object = MibTableColumn
rlCopyHistoryErrorMessage = _RlCopyHistoryErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 4, 1, 18),
    _RlCopyHistoryErrorMessage_Type()
)
rlCopyHistoryErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyHistoryErrorMessage.setStatus("current")


class _RlCopyAuditingEnable_Type(TruthValue):
    """Custom type rlCopyAuditingEnable based on TruthValue"""


_RlCopyAuditingEnable_Object = MibScalar
rlCopyAuditingEnable = _RlCopyAuditingEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 5),
    _RlCopyAuditingEnable_Type()
)
rlCopyAuditingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyAuditingEnable.setStatus("current")
_RlCopyMessagesTable_Object = MibTable
rlCopyMessagesTable = _RlCopyMessagesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 6)
)
if mibBuilder.loadTexts:
    rlCopyMessagesTable.setStatus("current")
_RlCopyMessagesEntry_Object = MibTableRow
rlCopyMessagesEntry = _RlCopyMessagesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 6, 1)
)
rlCopyMessagesEntry.setIndexNames(
    (0, "CISCOSB-COPY-MIB", "rlCopyMessagesCopyIndex"),
    (0, "CISCOSB-COPY-MIB", "rlCopyMessagesMessageIndex"),
)
if mibBuilder.loadTexts:
    rlCopyMessagesEntry.setStatus("current")


class _RlCopyMessagesCopyIndex_Type(Integer32):
    """Custom type rlCopyMessagesCopyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlCopyMessagesCopyIndex_Type.__name__ = "Integer32"
_RlCopyMessagesCopyIndex_Object = MibTableColumn
rlCopyMessagesCopyIndex = _RlCopyMessagesCopyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 6, 1, 1),
    _RlCopyMessagesCopyIndex_Type()
)
rlCopyMessagesCopyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlCopyMessagesCopyIndex.setStatus("current")


class _RlCopyMessagesMessageIndex_Type(Integer32):
    """Custom type rlCopyMessagesMessageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlCopyMessagesMessageIndex_Type.__name__ = "Integer32"
_RlCopyMessagesMessageIndex_Object = MibTableColumn
rlCopyMessagesMessageIndex = _RlCopyMessagesMessageIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 6, 1, 2),
    _RlCopyMessagesMessageIndex_Type()
)
rlCopyMessagesMessageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlCopyMessagesMessageIndex.setStatus("current")


class _RlCopyMessagesMessageText_Type(DisplayString):
    """Custom type rlCopyMessagesMessageText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RlCopyMessagesMessageText_Type.__name__ = "DisplayString"
_RlCopyMessagesMessageText_Object = MibTableColumn
rlCopyMessagesMessageText = _RlCopyMessagesMessageText_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 6, 1, 3),
    _RlCopyMessagesMessageText_Type()
)
rlCopyMessagesMessageText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyMessagesMessageText.setStatus("current")
_RlCopyMessagesStatus_Type = RowStatus
_RlCopyMessagesStatus_Object = MibTableColumn
rlCopyMessagesStatus = _RlCopyMessagesStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 6, 1, 4),
    _RlCopyMessagesStatus_Type()
)
rlCopyMessagesStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyMessagesStatus.setStatus("current")
_RlCopyMessagesTableRemoveEntries_Type = Integer32
_RlCopyMessagesTableRemoveEntries_Object = MibScalar
rlCopyMessagesTableRemoveEntries = _RlCopyMessagesTableRemoveEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 7),
    _RlCopyMessagesTableRemoveEntries_Type()
)
rlCopyMessagesTableRemoveEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyMessagesTableRemoveEntries.setStatus("current")
_RlCopyInetTable_Object = MibTable
rlCopyInetTable = _RlCopyInetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8)
)
if mibBuilder.loadTexts:
    rlCopyInetTable.setStatus("current")
_RlCopyInetEntry_Object = MibTableRow
rlCopyInetEntry = _RlCopyInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8, 1)
)
rlCopyInetEntry.setIndexNames(
    (0, "CISCOSB-COPY-MIB", "rlCopyInetIndex"),
)
if mibBuilder.loadTexts:
    rlCopyInetEntry.setStatus("current")
_RlCopyInetIndex_Type = Integer32
_RlCopyInetIndex_Object = MibTableColumn
rlCopyInetIndex = _RlCopyInetIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8, 1, 1),
    _RlCopyInetIndex_Type()
)
rlCopyInetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyInetIndex.setStatus("current")
_RlCopyInetApplicationId_Type = RlCopyApplicationType
_RlCopyInetApplicationId_Object = MibTableColumn
rlCopyInetApplicationId = _RlCopyInetApplicationId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8, 1, 2),
    _RlCopyInetApplicationId_Type()
)
rlCopyInetApplicationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyInetApplicationId.setStatus("current")
_RlCopyInetSourceLocation_Type = RlCopyLocationType
_RlCopyInetSourceLocation_Object = MibTableColumn
rlCopyInetSourceLocation = _RlCopyInetSourceLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8, 1, 3),
    _RlCopyInetSourceLocation_Type()
)
rlCopyInetSourceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyInetSourceLocation.setStatus("current")
_RlCopyInetSourceIpAddressType_Type = InetAddressType
_RlCopyInetSourceIpAddressType_Object = MibTableColumn
rlCopyInetSourceIpAddressType = _RlCopyInetSourceIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8, 1, 4),
    _RlCopyInetSourceIpAddressType_Type()
)
rlCopyInetSourceIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyInetSourceIpAddressType.setStatus("current")
_RlCopyInetSourceIpAddress_Type = InetAddress
_RlCopyInetSourceIpAddress_Object = MibTableColumn
rlCopyInetSourceIpAddress = _RlCopyInetSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8, 1, 5),
    _RlCopyInetSourceIpAddress_Type()
)
rlCopyInetSourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyInetSourceIpAddress.setStatus("current")
_RlCopyInetSourceUnitNumber_Type = Integer32
_RlCopyInetSourceUnitNumber_Object = MibTableColumn
rlCopyInetSourceUnitNumber = _RlCopyInetSourceUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8, 1, 6),
    _RlCopyInetSourceUnitNumber_Type()
)
rlCopyInetSourceUnitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyInetSourceUnitNumber.setStatus("current")
_RlCopyInetSourceFileName_Type = DisplayString
_RlCopyInetSourceFileName_Object = MibTableColumn
rlCopyInetSourceFileName = _RlCopyInetSourceFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8, 1, 7),
    _RlCopyInetSourceFileName_Type()
)
rlCopyInetSourceFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyInetSourceFileName.setStatus("current")
_RlCopyInetSourceFileType_Type = RlCopyFileType
_RlCopyInetSourceFileType_Object = MibTableColumn
rlCopyInetSourceFileType = _RlCopyInetSourceFileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8, 1, 8),
    _RlCopyInetSourceFileType_Type()
)
rlCopyInetSourceFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyInetSourceFileType.setStatus("current")
_RlCopyInetDestinationLocation_Type = RlCopyLocationType
_RlCopyInetDestinationLocation_Object = MibTableColumn
rlCopyInetDestinationLocation = _RlCopyInetDestinationLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8, 1, 9),
    _RlCopyInetDestinationLocation_Type()
)
rlCopyInetDestinationLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyInetDestinationLocation.setStatus("current")
_RlCopyInetDestinationIpAddressType_Type = InetAddressType
_RlCopyInetDestinationIpAddressType_Object = MibTableColumn
rlCopyInetDestinationIpAddressType = _RlCopyInetDestinationIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8, 1, 10),
    _RlCopyInetDestinationIpAddressType_Type()
)
rlCopyInetDestinationIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyInetDestinationIpAddressType.setStatus("current")
_RlCopyInetDestinationIpAddress_Type = InetAddress
_RlCopyInetDestinationIpAddress_Object = MibTableColumn
rlCopyInetDestinationIpAddress = _RlCopyInetDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8, 1, 11),
    _RlCopyInetDestinationIpAddress_Type()
)
rlCopyInetDestinationIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyInetDestinationIpAddress.setStatus("current")
_RlCopyInetDestinationUnitNumber_Type = Integer32
_RlCopyInetDestinationUnitNumber_Object = MibTableColumn
rlCopyInetDestinationUnitNumber = _RlCopyInetDestinationUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8, 1, 12),
    _RlCopyInetDestinationUnitNumber_Type()
)
rlCopyInetDestinationUnitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyInetDestinationUnitNumber.setStatus("current")
_RlCopyInetDestinationFileName_Type = DisplayString
_RlCopyInetDestinationFileName_Object = MibTableColumn
rlCopyInetDestinationFileName = _RlCopyInetDestinationFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8, 1, 13),
    _RlCopyInetDestinationFileName_Type()
)
rlCopyInetDestinationFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyInetDestinationFileName.setStatus("current")
_RlCopyInetDestinationFileType_Type = RlCopyFileType
_RlCopyInetDestinationFileType_Object = MibTableColumn
rlCopyInetDestinationFileType = _RlCopyInetDestinationFileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8, 1, 14),
    _RlCopyInetDestinationFileType_Type()
)
rlCopyInetDestinationFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyInetDestinationFileType.setStatus("current")
_RlCopyInetUpTime_Type = TimeTicks
_RlCopyInetUpTime_Object = MibTableColumn
rlCopyInetUpTime = _RlCopyInetUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8, 1, 15),
    _RlCopyInetUpTime_Type()
)
rlCopyInetUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyInetUpTime.setStatus("current")


class _RlCopyInetOperationState_Type(Integer32):
    """Custom type rlCopyInetOperationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("copyFailed", 3),
          ("copyFinished", 5),
          ("copyTimedout", 4),
          ("downloadInProgress", 2),
          ("uploadInProgress", 1))
    )


_RlCopyInetOperationState_Type.__name__ = "Integer32"
_RlCopyInetOperationState_Object = MibTableColumn
rlCopyInetOperationState = _RlCopyInetOperationState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8, 1, 16),
    _RlCopyInetOperationState_Type()
)
rlCopyInetOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyInetOperationState.setStatus("current")
_RlCopyInetBytesTransferred_Type = Integer32
_RlCopyInetBytesTransferred_Object = MibTableColumn
rlCopyInetBytesTransferred = _RlCopyInetBytesTransferred_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8, 1, 17),
    _RlCopyInetBytesTransferred_Type()
)
rlCopyInetBytesTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyInetBytesTransferred.setStatus("current")


class _RlCopyInetInBackground_Type(Integer32):
    """Custom type rlCopyInetInBackground based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RlCopyInetInBackground_Type.__name__ = "Integer32"
_RlCopyInetInBackground_Object = MibTableColumn
rlCopyInetInBackground = _RlCopyInetInBackground_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8, 1, 18),
    _RlCopyInetInBackground_Type()
)
rlCopyInetInBackground.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyInetInBackground.setStatus("current")
_RlCopyInetRowStatus_Type = RowStatus
_RlCopyInetRowStatus_Object = MibTableColumn
rlCopyInetRowStatus = _RlCopyInetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8, 1, 19),
    _RlCopyInetRowStatus_Type()
)
rlCopyInetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyInetRowStatus.setStatus("current")


class _RlCopyInetHistoryIndex_Type(Integer32):
    """Custom type rlCopyInetHistoryIndex based on Integer32"""
    defaultValue = 0


_RlCopyInetHistoryIndex_Object = MibTableColumn
rlCopyInetHistoryIndex = _RlCopyInetHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8, 1, 20),
    _RlCopyInetHistoryIndex_Type()
)
rlCopyInetHistoryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyInetHistoryIndex.setStatus("current")


class _RlCopyInetDestinationUnitList_Type(Integer32):
    """Custom type rlCopyInetDestinationUnitList based on Integer32"""
    defaultValue = 0


_RlCopyInetDestinationUnitList_Object = MibTableColumn
rlCopyInetDestinationUnitList = _RlCopyInetDestinationUnitList_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8, 1, 21),
    _RlCopyInetDestinationUnitList_Type()
)
rlCopyInetDestinationUnitList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyInetDestinationUnitList.setStatus("current")
_RlCopyInetUnitStatusList_Type = Integer32
_RlCopyInetUnitStatusList_Object = MibTableColumn
rlCopyInetUnitStatusList = _RlCopyInetUnitStatusList_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8, 1, 22),
    _RlCopyInetUnitStatusList_Type()
)
rlCopyInetUnitStatusList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyInetUnitStatusList.setStatus("current")
_RlCopyInetSpecificCopyInfo_Type = DisplayString
_RlCopyInetSpecificCopyInfo_Object = MibTableColumn
rlCopyInetSpecificCopyInfo = _RlCopyInetSpecificCopyInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 8, 1, 23),
    _RlCopyInetSpecificCopyInfo_Type()
)
rlCopyInetSpecificCopyInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyInetSpecificCopyInfo.setStatus("current")
_RlCopyHistoryInetTable_Object = MibTable
rlCopyHistoryInetTable = _RlCopyHistoryInetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 9)
)
if mibBuilder.loadTexts:
    rlCopyHistoryInetTable.setStatus("current")
_RlCopyHistoryInetEntry_Object = MibTableRow
rlCopyHistoryInetEntry = _RlCopyHistoryInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 9, 1)
)
rlCopyHistoryInetEntry.setIndexNames(
    (0, "CISCOSB-COPY-MIB", "rlCopyHistoryInetHistoryIndex"),
)
if mibBuilder.loadTexts:
    rlCopyHistoryInetEntry.setStatus("current")
_RlCopyHistoryInetHistoryIndex_Type = Integer32
_RlCopyHistoryInetHistoryIndex_Object = MibTableColumn
rlCopyHistoryInetHistoryIndex = _RlCopyHistoryInetHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 9, 1, 1),
    _RlCopyHistoryInetHistoryIndex_Type()
)
rlCopyHistoryInetHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyHistoryInetHistoryIndex.setStatus("current")
_RlCopyHistoryInetApplicationId_Type = RlCopyApplicationType
_RlCopyHistoryInetApplicationId_Object = MibTableColumn
rlCopyHistoryInetApplicationId = _RlCopyHistoryInetApplicationId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 9, 1, 2),
    _RlCopyHistoryInetApplicationId_Type()
)
rlCopyHistoryInetApplicationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyHistoryInetApplicationId.setStatus("current")
_RlCopyHistoryInetSourceLocation_Type = RlCopyLocationType
_RlCopyHistoryInetSourceLocation_Object = MibTableColumn
rlCopyHistoryInetSourceLocation = _RlCopyHistoryInetSourceLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 9, 1, 3),
    _RlCopyHistoryInetSourceLocation_Type()
)
rlCopyHistoryInetSourceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryInetSourceLocation.setStatus("current")
_RlCopyHistoryInetSourceIpAddressType_Type = InetAddressType
_RlCopyHistoryInetSourceIpAddressType_Object = MibTableColumn
rlCopyHistoryInetSourceIpAddressType = _RlCopyHistoryInetSourceIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 9, 1, 4),
    _RlCopyHistoryInetSourceIpAddressType_Type()
)
rlCopyHistoryInetSourceIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryInetSourceIpAddressType.setStatus("current")
_RlCopyHistoryInetSourceIpAddress_Type = InetAddress
_RlCopyHistoryInetSourceIpAddress_Object = MibTableColumn
rlCopyHistoryInetSourceIpAddress = _RlCopyHistoryInetSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 9, 1, 5),
    _RlCopyHistoryInetSourceIpAddress_Type()
)
rlCopyHistoryInetSourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryInetSourceIpAddress.setStatus("current")
_RlCopyHistoryInetSourceUnitNumber_Type = Integer32
_RlCopyHistoryInetSourceUnitNumber_Object = MibTableColumn
rlCopyHistoryInetSourceUnitNumber = _RlCopyHistoryInetSourceUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 9, 1, 6),
    _RlCopyHistoryInetSourceUnitNumber_Type()
)
rlCopyHistoryInetSourceUnitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryInetSourceUnitNumber.setStatus("current")
_RlCopyHistoryInetSourceFileName_Type = DisplayString
_RlCopyHistoryInetSourceFileName_Object = MibTableColumn
rlCopyHistoryInetSourceFileName = _RlCopyHistoryInetSourceFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 9, 1, 7),
    _RlCopyHistoryInetSourceFileName_Type()
)
rlCopyHistoryInetSourceFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryInetSourceFileName.setStatus("current")
_RlCopyHistoryInetSourceFileType_Type = RlCopyFileType
_RlCopyHistoryInetSourceFileType_Object = MibTableColumn
rlCopyHistoryInetSourceFileType = _RlCopyHistoryInetSourceFileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 9, 1, 8),
    _RlCopyHistoryInetSourceFileType_Type()
)
rlCopyHistoryInetSourceFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryInetSourceFileType.setStatus("current")
_RlCopyHistoryInetDestinationLocation_Type = RlCopyLocationType
_RlCopyHistoryInetDestinationLocation_Object = MibTableColumn
rlCopyHistoryInetDestinationLocation = _RlCopyHistoryInetDestinationLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 9, 1, 9),
    _RlCopyHistoryInetDestinationLocation_Type()
)
rlCopyHistoryInetDestinationLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryInetDestinationLocation.setStatus("current")
_RlCopyHistoryInetDestinationIpAddressType_Type = InetAddressType
_RlCopyHistoryInetDestinationIpAddressType_Object = MibTableColumn
rlCopyHistoryInetDestinationIpAddressType = _RlCopyHistoryInetDestinationIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 9, 1, 10),
    _RlCopyHistoryInetDestinationIpAddressType_Type()
)
rlCopyHistoryInetDestinationIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryInetDestinationIpAddressType.setStatus("current")
_RlCopyHistoryInetDestinationIpAddress_Type = InetAddress
_RlCopyHistoryInetDestinationIpAddress_Object = MibTableColumn
rlCopyHistoryInetDestinationIpAddress = _RlCopyHistoryInetDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 9, 1, 11),
    _RlCopyHistoryInetDestinationIpAddress_Type()
)
rlCopyHistoryInetDestinationIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryInetDestinationIpAddress.setStatus("current")
_RlCopyHistoryInetDestinationUnitNumber_Type = Integer32
_RlCopyHistoryInetDestinationUnitNumber_Object = MibTableColumn
rlCopyHistoryInetDestinationUnitNumber = _RlCopyHistoryInetDestinationUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 9, 1, 12),
    _RlCopyHistoryInetDestinationUnitNumber_Type()
)
rlCopyHistoryInetDestinationUnitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryInetDestinationUnitNumber.setStatus("current")
_RlCopyHistoryInetDestinationFileName_Type = DisplayString
_RlCopyHistoryInetDestinationFileName_Object = MibTableColumn
rlCopyHistoryInetDestinationFileName = _RlCopyHistoryInetDestinationFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 9, 1, 13),
    _RlCopyHistoryInetDestinationFileName_Type()
)
rlCopyHistoryInetDestinationFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryInetDestinationFileName.setStatus("current")
_RlCopyHistoryInetDestinationFileType_Type = RlCopyFileType
_RlCopyHistoryInetDestinationFileType_Object = MibTableColumn
rlCopyHistoryInetDestinationFileType = _RlCopyHistoryInetDestinationFileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 9, 1, 14),
    _RlCopyHistoryInetDestinationFileType_Type()
)
rlCopyHistoryInetDestinationFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryInetDestinationFileType.setStatus("current")
_RlCopyHistoryInetUpTime_Type = TimeTicks
_RlCopyHistoryInetUpTime_Object = MibTableColumn
rlCopyHistoryInetUpTime = _RlCopyHistoryInetUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 9, 1, 15),
    _RlCopyHistoryInetUpTime_Type()
)
rlCopyHistoryInetUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyHistoryInetUpTime.setStatus("current")


class _RlCopyHistoryInetOperationState_Type(Integer32):
    """Custom type rlCopyHistoryInetOperationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("copyFailed", 3),
          ("copyFinished", 5),
          ("copyTimedout", 4),
          ("downloadInProgress", 2),
          ("uploadInProgress", 1))
    )


_RlCopyHistoryInetOperationState_Type.__name__ = "Integer32"
_RlCopyHistoryInetOperationState_Object = MibTableColumn
rlCopyHistoryInetOperationState = _RlCopyHistoryInetOperationState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 9, 1, 16),
    _RlCopyHistoryInetOperationState_Type()
)
rlCopyHistoryInetOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyHistoryInetOperationState.setStatus("current")
_RlCopyHistoryInetBytesTransferred_Type = Integer32
_RlCopyHistoryInetBytesTransferred_Object = MibTableColumn
rlCopyHistoryInetBytesTransferred = _RlCopyHistoryInetBytesTransferred_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 9, 1, 17),
    _RlCopyHistoryInetBytesTransferred_Type()
)
rlCopyHistoryInetBytesTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyHistoryInetBytesTransferred.setStatus("current")


class _RlCopyHistoryInetInBackground_Type(Integer32):
    """Custom type rlCopyHistoryInetInBackground based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RlCopyHistoryInetInBackground_Type.__name__ = "Integer32"
_RlCopyHistoryInetInBackground_Object = MibTableColumn
rlCopyHistoryInetInBackground = _RlCopyHistoryInetInBackground_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 9, 1, 18),
    _RlCopyHistoryInetInBackground_Type()
)
rlCopyHistoryInetInBackground.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryInetInBackground.setStatus("current")
_RlCopyHistoryInetRowStatus_Type = RowStatus
_RlCopyHistoryInetRowStatus_Object = MibTableColumn
rlCopyHistoryInetRowStatus = _RlCopyHistoryInetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 9, 1, 19),
    _RlCopyHistoryInetRowStatus_Type()
)
rlCopyHistoryInetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryInetRowStatus.setStatus("current")
_RlCopyHistoryInetErrorMessage_Type = DisplayString
_RlCopyHistoryInetErrorMessage_Object = MibTableColumn
rlCopyHistoryInetErrorMessage = _RlCopyHistoryInetErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 9, 1, 20),
    _RlCopyHistoryInetErrorMessage_Type()
)
rlCopyHistoryInetErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyHistoryInetErrorMessage.setStatus("current")


class _RlCopyHistoryInetDestinationUnitList_Type(Integer32):
    """Custom type rlCopyHistoryInetDestinationUnitList based on Integer32"""
    defaultValue = 0


_RlCopyHistoryInetDestinationUnitList_Object = MibTableColumn
rlCopyHistoryInetDestinationUnitList = _RlCopyHistoryInetDestinationUnitList_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 9, 1, 21),
    _RlCopyHistoryInetDestinationUnitList_Type()
)
rlCopyHistoryInetDestinationUnitList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryInetDestinationUnitList.setStatus("current")
_RlCopyHistoryInetUnitStatusList_Type = Integer32
_RlCopyHistoryInetUnitStatusList_Object = MibTableColumn
rlCopyHistoryInetUnitStatusList = _RlCopyHistoryInetUnitStatusList_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 9, 1, 22),
    _RlCopyHistoryInetUnitStatusList_Type()
)
rlCopyHistoryInetUnitStatusList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyHistoryInetUnitStatusList.setStatus("current")
_RlCopyUnitsList_Type = Integer32
_RlCopyUnitsList_Object = MibScalar
rlCopyUnitsList = _RlCopyUnitsList_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 10),
    _RlCopyUnitsList_Type()
)
rlCopyUnitsList.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rlCopyUnitsList.setStatus("current")
_RlCopyMirrorTimeout_Type = Integer32
_RlCopyMirrorTimeout_Object = MibScalar
rlCopyMirrorTimeout = _RlCopyMirrorTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 11),
    _RlCopyMirrorTimeout_Type()
)
rlCopyMirrorTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyMirrorTimeout.setStatus("current")
_RlCopyOptionsTable_Object = MibTable
rlCopyOptionsTable = _RlCopyOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 12)
)
if mibBuilder.loadTexts:
    rlCopyOptionsTable.setStatus("current")
_RlCopyOptionsEntry_Object = MibTableRow
rlCopyOptionsEntry = _RlCopyOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 12, 1)
)
rlCopyOptionsEntry.setIndexNames(
    (0, "CISCOSB-COPY-MIB", "rlCopyOptionsIndex"),
)
if mibBuilder.loadTexts:
    rlCopyOptionsEntry.setStatus("current")
_RlCopyOptionsIndex_Type = Unsigned32
_RlCopyOptionsIndex_Object = MibTableColumn
rlCopyOptionsIndex = _RlCopyOptionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 12, 1, 1),
    _RlCopyOptionsIndex_Type()
)
rlCopyOptionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlCopyOptionsIndex.setStatus("current")


class _RlCopyOptionsRequestedSsdAccess_Type(RlCopySecSdAccessType):
    """Custom type rlCopyOptionsRequestedSsdAccess based on RlCopySecSdAccessType"""


_RlCopyOptionsRequestedSsdAccess_Object = MibTableColumn
rlCopyOptionsRequestedSsdAccess = _RlCopyOptionsRequestedSsdAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 12, 1, 2),
    _RlCopyOptionsRequestedSsdAccess_Type()
)
rlCopyOptionsRequestedSsdAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlCopyOptionsRequestedSsdAccess.setStatus("current")
_RlCopyMirror_ObjectIdentity = ObjectIdentity
rlCopyMirror = _RlCopyMirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 13)
)


class _RlCopyMirrorEnable_Type(Integer32):
    """Custom type rlCopyMirrorEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RlCopyMirrorEnable_Type.__name__ = "Integer32"
_RlCopyMirrorEnable_Object = MibScalar
rlCopyMirrorEnable = _RlCopyMirrorEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 13, 1),
    _RlCopyMirrorEnable_Type()
)
rlCopyMirrorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyMirrorEnable.setStatus("current")


class _RlCopyStaticDowngradeStatus_Type(TruthValue):
    """Custom type rlCopyStaticDowngradeStatus based on TruthValue"""


_RlCopyStaticDowngradeStatus_Object = MibScalar
rlCopyStaticDowngradeStatus = _RlCopyStaticDowngradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87, 14),
    _RlCopyStaticDowngradeStatus_Type()
)
rlCopyStaticDowngradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyStaticDowngradeStatus.setStatus("current")

# Managed Objects groups


# Notification objects

rlCopyFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 180)
)
rlCopyFinished.setObjects(
      *(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlCopyFinished.setStatus(
        "current"
    )

rlCopyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 181)
)
rlCopyFailed.setObjects(
      *(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlCopyFailed.setStatus(
        "current"
    )

rlCopySWFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 211)
)
rlCopySWFinished.setObjects(
      *(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlCopySWFinished.setStatus(
        "current"
    )

rlCopySWToUnits = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 212)
)
rlCopySWToUnits.setObjects(
      *(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"),
        ("CISCOSB-COPY-MIB", "rlCopyUnitsList"))
)
if mibBuilder.loadTexts:
    rlCopySWToUnits.setStatus(
        "current"
    )

rlCopyMirrorFileIllegal = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 220)
)
rlCopyMirrorFileIllegal.setObjects(
      *(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlCopyMirrorFileIllegal.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-COPY-MIB",
    **{"RlCopyApplicationType": RlCopyApplicationType,
       "RlCopyLocationType": RlCopyLocationType,
       "RlCopyFileType": RlCopyFileType,
       "RlCopySecSdAccessType": RlCopySecSdAccessType,
       "rlCopyFinished": rlCopyFinished,
       "rlCopyFailed": rlCopyFailed,
       "rlCopySWFinished": rlCopySWFinished,
       "rlCopySWToUnits": rlCopySWToUnits,
       "rlCopyMirrorFileIllegal": rlCopyMirrorFileIllegal,
       "rlCopy": rlCopy,
       "rlCopyMibVersion": rlCopyMibVersion,
       "rlCopyTable": rlCopyTable,
       "rlCopyEntry": rlCopyEntry,
       "rlCopyIndex": rlCopyIndex,
       "rlCopyApplicationId": rlCopyApplicationId,
       "rlCopySourceLocation": rlCopySourceLocation,
       "rlCopySourceIpAddress": rlCopySourceIpAddress,
       "rlCopySourceUnitNumber": rlCopySourceUnitNumber,
       "rlCopySourceFileName": rlCopySourceFileName,
       "rlCopySourceFileType": rlCopySourceFileType,
       "rlCopyDestinationLocation": rlCopyDestinationLocation,
       "rlCopyDestinationIpAddress": rlCopyDestinationIpAddress,
       "rlCopyDestinationUnitNumber": rlCopyDestinationUnitNumber,
       "rlCopyDestinationFileName": rlCopyDestinationFileName,
       "rlCopyDestinationFileType": rlCopyDestinationFileType,
       "rlCopyUpTime": rlCopyUpTime,
       "rlCopyOperationState": rlCopyOperationState,
       "rlCopyBytesTransferred": rlCopyBytesTransferred,
       "rlCopyInBackground": rlCopyInBackground,
       "rlCopyRowStatus": rlCopyRowStatus,
       "rlCopyHistoryIndex": rlCopyHistoryIndex,
       "rlCopyFreeHistoryIndex": rlCopyFreeHistoryIndex,
       "rlCopyHistoryTable": rlCopyHistoryTable,
       "rlCopyHistoryEntry": rlCopyHistoryEntry,
       "rlCopyHistoryHistoryIndex": rlCopyHistoryHistoryIndex,
       "rlCopyHistoryApplicationId": rlCopyHistoryApplicationId,
       "rlCopyHistorySourceLocation": rlCopyHistorySourceLocation,
       "rlCopyHistorySourceIpAddress": rlCopyHistorySourceIpAddress,
       "rlCopyHistorySourceUnitNumber": rlCopyHistorySourceUnitNumber,
       "rlCopyHistorySourceFileName": rlCopyHistorySourceFileName,
       "rlCopyHistorySourceFileType": rlCopyHistorySourceFileType,
       "rlCopyHistoryDestinationLocation": rlCopyHistoryDestinationLocation,
       "rlCopyHistoryDestinationIpAddress": rlCopyHistoryDestinationIpAddress,
       "rlCopyHistoryDestinationUnitNumber": rlCopyHistoryDestinationUnitNumber,
       "rlCopyHistoryDestinationFileName": rlCopyHistoryDestinationFileName,
       "rlCopyHistoryDestinationFileType": rlCopyHistoryDestinationFileType,
       "rlCopyHistoryUpTime": rlCopyHistoryUpTime,
       "rlCopyHistoryOperationState": rlCopyHistoryOperationState,
       "rlCopyHistoryBytesTransferred": rlCopyHistoryBytesTransferred,
       "rlCopyHistoryInBackground": rlCopyHistoryInBackground,
       "rlCopyHistoryRowStatus": rlCopyHistoryRowStatus,
       "rlCopyHistoryErrorMessage": rlCopyHistoryErrorMessage,
       "rlCopyAuditingEnable": rlCopyAuditingEnable,
       "rlCopyMessagesTable": rlCopyMessagesTable,
       "rlCopyMessagesEntry": rlCopyMessagesEntry,
       "rlCopyMessagesCopyIndex": rlCopyMessagesCopyIndex,
       "rlCopyMessagesMessageIndex": rlCopyMessagesMessageIndex,
       "rlCopyMessagesMessageText": rlCopyMessagesMessageText,
       "rlCopyMessagesStatus": rlCopyMessagesStatus,
       "rlCopyMessagesTableRemoveEntries": rlCopyMessagesTableRemoveEntries,
       "rlCopyInetTable": rlCopyInetTable,
       "rlCopyInetEntry": rlCopyInetEntry,
       "rlCopyInetIndex": rlCopyInetIndex,
       "rlCopyInetApplicationId": rlCopyInetApplicationId,
       "rlCopyInetSourceLocation": rlCopyInetSourceLocation,
       "rlCopyInetSourceIpAddressType": rlCopyInetSourceIpAddressType,
       "rlCopyInetSourceIpAddress": rlCopyInetSourceIpAddress,
       "rlCopyInetSourceUnitNumber": rlCopyInetSourceUnitNumber,
       "rlCopyInetSourceFileName": rlCopyInetSourceFileName,
       "rlCopyInetSourceFileType": rlCopyInetSourceFileType,
       "rlCopyInetDestinationLocation": rlCopyInetDestinationLocation,
       "rlCopyInetDestinationIpAddressType": rlCopyInetDestinationIpAddressType,
       "rlCopyInetDestinationIpAddress": rlCopyInetDestinationIpAddress,
       "rlCopyInetDestinationUnitNumber": rlCopyInetDestinationUnitNumber,
       "rlCopyInetDestinationFileName": rlCopyInetDestinationFileName,
       "rlCopyInetDestinationFileType": rlCopyInetDestinationFileType,
       "rlCopyInetUpTime": rlCopyInetUpTime,
       "rlCopyInetOperationState": rlCopyInetOperationState,
       "rlCopyInetBytesTransferred": rlCopyInetBytesTransferred,
       "rlCopyInetInBackground": rlCopyInetInBackground,
       "rlCopyInetRowStatus": rlCopyInetRowStatus,
       "rlCopyInetHistoryIndex": rlCopyInetHistoryIndex,
       "rlCopyInetDestinationUnitList": rlCopyInetDestinationUnitList,
       "rlCopyInetUnitStatusList": rlCopyInetUnitStatusList,
       "rlCopyInetSpecificCopyInfo": rlCopyInetSpecificCopyInfo,
       "rlCopyHistoryInetTable": rlCopyHistoryInetTable,
       "rlCopyHistoryInetEntry": rlCopyHistoryInetEntry,
       "rlCopyHistoryInetHistoryIndex": rlCopyHistoryInetHistoryIndex,
       "rlCopyHistoryInetApplicationId": rlCopyHistoryInetApplicationId,
       "rlCopyHistoryInetSourceLocation": rlCopyHistoryInetSourceLocation,
       "rlCopyHistoryInetSourceIpAddressType": rlCopyHistoryInetSourceIpAddressType,
       "rlCopyHistoryInetSourceIpAddress": rlCopyHistoryInetSourceIpAddress,
       "rlCopyHistoryInetSourceUnitNumber": rlCopyHistoryInetSourceUnitNumber,
       "rlCopyHistoryInetSourceFileName": rlCopyHistoryInetSourceFileName,
       "rlCopyHistoryInetSourceFileType": rlCopyHistoryInetSourceFileType,
       "rlCopyHistoryInetDestinationLocation": rlCopyHistoryInetDestinationLocation,
       "rlCopyHistoryInetDestinationIpAddressType": rlCopyHistoryInetDestinationIpAddressType,
       "rlCopyHistoryInetDestinationIpAddress": rlCopyHistoryInetDestinationIpAddress,
       "rlCopyHistoryInetDestinationUnitNumber": rlCopyHistoryInetDestinationUnitNumber,
       "rlCopyHistoryInetDestinationFileName": rlCopyHistoryInetDestinationFileName,
       "rlCopyHistoryInetDestinationFileType": rlCopyHistoryInetDestinationFileType,
       "rlCopyHistoryInetUpTime": rlCopyHistoryInetUpTime,
       "rlCopyHistoryInetOperationState": rlCopyHistoryInetOperationState,
       "rlCopyHistoryInetBytesTransferred": rlCopyHistoryInetBytesTransferred,
       "rlCopyHistoryInetInBackground": rlCopyHistoryInetInBackground,
       "rlCopyHistoryInetRowStatus": rlCopyHistoryInetRowStatus,
       "rlCopyHistoryInetErrorMessage": rlCopyHistoryInetErrorMessage,
       "rlCopyHistoryInetDestinationUnitList": rlCopyHistoryInetDestinationUnitList,
       "rlCopyHistoryInetUnitStatusList": rlCopyHistoryInetUnitStatusList,
       "rlCopyUnitsList": rlCopyUnitsList,
       "rlCopyMirrorTimeout": rlCopyMirrorTimeout,
       "rlCopyOptionsTable": rlCopyOptionsTable,
       "rlCopyOptionsEntry": rlCopyOptionsEntry,
       "rlCopyOptionsIndex": rlCopyOptionsIndex,
       "rlCopyOptionsRequestedSsdAccess": rlCopyOptionsRequestedSsdAccess,
       "rlCopyMirror": rlCopyMirror,
       "rlCopyMirrorEnable": rlCopyMirrorEnable,
       "rlCopyStaticDowngradeStatus": rlCopyStaticDowngradeStatus}
)
