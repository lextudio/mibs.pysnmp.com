# SNMP MIB module (ADTRAN-AOSDOWNLOAD) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-AOSDOWNLOAD
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:18 2024
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

(adGenAOSCommon,
 adGenAOSConformance) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSCommon",
    "adGenAOSConformance")

(adIdentity,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity")

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
 TAddress,
 TDomain,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TAddress",
    "TDomain",
    "TextualConvention")


# MODULE-IDENTITY

adAOSDownloadMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 3)
)
adAOSDownloadMib.setRevisions(
        ("2004-09-21 22:16",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdAOSDownload_ObjectIdentity = ObjectIdentity
adAOSDownload = _AdAOSDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3)
)
_AdAOSDownloadTable_Object = MibTable
adAOSDownloadTable = _AdAOSDownloadTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1)
)
if mibBuilder.loadTexts:
    adAOSDownloadTable.setStatus("current")
_AdAOSDownloadEntry_Object = MibTableRow
adAOSDownloadEntry = _AdAOSDownloadEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1)
)
adAOSDownloadEntry.setIndexNames(
    (0, "ADTRAN-AOSDOWNLOAD", "adAOSDownloadIndex"),
)
if mibBuilder.loadTexts:
    adAOSDownloadEntry.setStatus("current")


class _AdAOSDownloadIndex_Type(Integer32):
    """Custom type adAOSDownloadIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("dlInstance", 1)
    )


_AdAOSDownloadIndex_Type.__name__ = "Integer32"
_AdAOSDownloadIndex_Object = MibTableColumn
adAOSDownloadIndex = _AdAOSDownloadIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 1),
    _AdAOSDownloadIndex_Type()
)
adAOSDownloadIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDownloadIndex.setStatus("current")
_AdAOSDownloadOwnerAddress_Type = TAddress
_AdAOSDownloadOwnerAddress_Object = MibTableColumn
adAOSDownloadOwnerAddress = _AdAOSDownloadOwnerAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 2),
    _AdAOSDownloadOwnerAddress_Type()
)
adAOSDownloadOwnerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDownloadOwnerAddress.setStatus("current")
_AdAOSDownloadOwnerDomain_Type = TDomain
_AdAOSDownloadOwnerDomain_Object = MibTableColumn
adAOSDownloadOwnerDomain = _AdAOSDownloadOwnerDomain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 3),
    _AdAOSDownloadOwnerDomain_Type()
)
adAOSDownloadOwnerDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDownloadOwnerDomain.setStatus("current")
_AdAOSDownloadTAddress_Type = TAddress
_AdAOSDownloadTAddress_Object = MibTableColumn
adAOSDownloadTAddress = _AdAOSDownloadTAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 4),
    _AdAOSDownloadTAddress_Type()
)
adAOSDownloadTAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adAOSDownloadTAddress.setStatus("current")
_AdAOSDownloadTDomain_Type = TDomain
_AdAOSDownloadTDomain_Object = MibTableColumn
adAOSDownloadTDomain = _AdAOSDownloadTDomain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 5),
    _AdAOSDownloadTDomain_Type()
)
adAOSDownloadTDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adAOSDownloadTDomain.setStatus("current")


class _AdAOSDownloadFilename_Type(DisplayString):
    """Custom type adAOSDownloadFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AdAOSDownloadFilename_Type.__name__ = "DisplayString"
_AdAOSDownloadFilename_Object = MibTableColumn
adAOSDownloadFilename = _AdAOSDownloadFilename_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 6),
    _AdAOSDownloadFilename_Type()
)
adAOSDownloadFilename.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adAOSDownloadFilename.setStatus("current")


class _AdAOSDownloadResetType_Type(Integer32):
    """Custom type adAOSDownloadResetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("factoryReset", 3),
          ("noReset", 1),
          ("warmReset", 2))
    )


_AdAOSDownloadResetType_Type.__name__ = "Integer32"
_AdAOSDownloadResetType_Object = MibTableColumn
adAOSDownloadResetType = _AdAOSDownloadResetType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 7),
    _AdAOSDownloadResetType_Type()
)
adAOSDownloadResetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adAOSDownloadResetType.setStatus("current")


class _AdAOSDownloadErrorStatus_Type(Integer32):
    """Custom type adAOSDownloadErrorStatus based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 14),
          ("accessViolation", 2),
          ("cannotDowngrade", 21),
          ("cannotUpgrade", 20),
          ("corruptFile", 9),
          ("diskFull", 3),
          ("erasingEeprom", 17),
          ("fileExists", 6),
          ("fileNotFound", 1),
          ("hardwareError", 12),
          ("idle", 16),
          ("illegalOperation", 4),
          ("inProgress", 15),
          ("incompleteFirmware", 18),
          ("noServer", 10),
          ("noSuchUser", 7),
          ("notDefined", 8),
          ("requirePowerCycle", 19),
          ("success", 13),
          ("tftpTimeout", 11),
          ("unknownTID", 5))
    )


_AdAOSDownloadErrorStatus_Type.__name__ = "Integer32"
_AdAOSDownloadErrorStatus_Object = MibTableColumn
adAOSDownloadErrorStatus = _AdAOSDownloadErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 8),
    _AdAOSDownloadErrorStatus_Type()
)
adAOSDownloadErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDownloadErrorStatus.setStatus("current")


class _AdAOSDownloadErrorText_Type(DisplayString):
    """Custom type adAOSDownloadErrorText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdAOSDownloadErrorText_Type.__name__ = "DisplayString"
_AdAOSDownloadErrorText_Object = MibTableColumn
adAOSDownloadErrorText = _AdAOSDownloadErrorText_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 9),
    _AdAOSDownloadErrorText_Type()
)
adAOSDownloadErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDownloadErrorText.setStatus("current")
_AdAOSDownloadStatus_Type = RowStatus
_AdAOSDownloadStatus_Object = MibTableColumn
adAOSDownloadStatus = _AdAOSDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 10),
    _AdAOSDownloadStatus_Type()
)
adAOSDownloadStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adAOSDownloadStatus.setStatus("current")
_AdAOSDownloadPassesLeft_Type = Integer32
_AdAOSDownloadPassesLeft_Object = MibTableColumn
adAOSDownloadPassesLeft = _AdAOSDownloadPassesLeft_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 11),
    _AdAOSDownloadPassesLeft_Type()
)
adAOSDownloadPassesLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDownloadPassesLeft.setStatus("current")
_AdAOSDownloadOctetCount_Type = Integer32
_AdAOSDownloadOctetCount_Object = MibTableColumn
adAOSDownloadOctetCount = _AdAOSDownloadOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 12),
    _AdAOSDownloadOctetCount_Type()
)
adAOSDownloadOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDownloadOctetCount.setStatus("current")


class _AdAOSDownloadDestination_Type(DisplayString):
    """Custom type adAOSDownloadDestination based on DisplayString"""
    defaultValue = OctetString("/os/primary")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AdAOSDownloadDestination_Type.__name__ = "DisplayString"
_AdAOSDownloadDestination_Object = MibTableColumn
adAOSDownloadDestination = _AdAOSDownloadDestination_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 13),
    _AdAOSDownloadDestination_Type()
)
adAOSDownloadDestination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adAOSDownloadDestination.setStatus("deprecated")


class _AdAOSDownloadDestinationType_Type(Integer32):
    """Custom type adAOSDownloadDestinationType based on Integer32"""
    defaultValue = 1

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
        *(("config", 3),
          ("other", 5),
          ("primary", 1),
          ("remote", 4),
          ("secondary", 2))
    )


_AdAOSDownloadDestinationType_Type.__name__ = "Integer32"
_AdAOSDownloadDestinationType_Object = MibTableColumn
adAOSDownloadDestinationType = _AdAOSDownloadDestinationType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 14),
    _AdAOSDownloadDestinationType_Type()
)
adAOSDownloadDestinationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adAOSDownloadDestinationType.setStatus("current")


class _AdAOSDownloadLogMaxSize_Type(Integer32):
    """Custom type adAOSDownloadLogMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdAOSDownloadLogMaxSize_Type.__name__ = "Integer32"
_AdAOSDownloadLogMaxSize_Object = MibScalar
adAOSDownloadLogMaxSize = _AdAOSDownloadLogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 2),
    _AdAOSDownloadLogMaxSize_Type()
)
adAOSDownloadLogMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDownloadLogMaxSize.setStatus("current")


class _AdAOSDownloadLogSize_Type(Gauge32):
    """Custom type adAOSDownloadLogSize based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdAOSDownloadLogSize_Type.__name__ = "Gauge32"
_AdAOSDownloadLogSize_Object = MibScalar
adAOSDownloadLogSize = _AdAOSDownloadLogSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 3),
    _AdAOSDownloadLogSize_Type()
)
adAOSDownloadLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDownloadLogSize.setStatus("current")
_AdAOSDownloadLogTable_Object = MibTable
adAOSDownloadLogTable = _AdAOSDownloadLogTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4)
)
if mibBuilder.loadTexts:
    adAOSDownloadLogTable.setStatus("current")
_AdAOSDownloadLogEntry_Object = MibTableRow
adAOSDownloadLogEntry = _AdAOSDownloadLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1)
)
adAOSDownloadLogEntry.setIndexNames(
    (0, "ADTRAN-AOSDOWNLOAD", "adAOSDlLogIndex"),
)
if mibBuilder.loadTexts:
    adAOSDownloadLogEntry.setStatus("current")


class _AdAOSDlLogIndex_Type(Integer32):
    """Custom type adAOSDlLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AdAOSDlLogIndex_Type.__name__ = "Integer32"
_AdAOSDlLogIndex_Object = MibTableColumn
adAOSDlLogIndex = _AdAOSDlLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 1),
    _AdAOSDlLogIndex_Type()
)
adAOSDlLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDlLogIndex.setStatus("current")
_AdAOSDlLogOwnerAddress_Type = TAddress
_AdAOSDlLogOwnerAddress_Object = MibTableColumn
adAOSDlLogOwnerAddress = _AdAOSDlLogOwnerAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 2),
    _AdAOSDlLogOwnerAddress_Type()
)
adAOSDlLogOwnerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDlLogOwnerAddress.setStatus("current")
_AdAOSDlLogOwnerDomain_Type = TDomain
_AdAOSDlLogOwnerDomain_Object = MibTableColumn
adAOSDlLogOwnerDomain = _AdAOSDlLogOwnerDomain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 3),
    _AdAOSDlLogOwnerDomain_Type()
)
adAOSDlLogOwnerDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDlLogOwnerDomain.setStatus("current")
_AdAOSDlLogTAddress_Type = TAddress
_AdAOSDlLogTAddress_Object = MibTableColumn
adAOSDlLogTAddress = _AdAOSDlLogTAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 4),
    _AdAOSDlLogTAddress_Type()
)
adAOSDlLogTAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDlLogTAddress.setStatus("current")
_AdAOSDlLogTDomain_Type = TDomain
_AdAOSDlLogTDomain_Object = MibTableColumn
adAOSDlLogTDomain = _AdAOSDlLogTDomain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 5),
    _AdAOSDlLogTDomain_Type()
)
adAOSDlLogTDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDlLogTDomain.setStatus("current")


class _AdAOSDlLogFilename_Type(DisplayString):
    """Custom type adAOSDlLogFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AdAOSDlLogFilename_Type.__name__ = "DisplayString"
_AdAOSDlLogFilename_Object = MibTableColumn
adAOSDlLogFilename = _AdAOSDlLogFilename_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 6),
    _AdAOSDlLogFilename_Type()
)
adAOSDlLogFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDlLogFilename.setStatus("current")


class _AdAOSDlLogResetType_Type(Integer32):
    """Custom type adAOSDlLogResetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("factoryReset", 3),
          ("noReset", 1),
          ("warmReset", 2))
    )


_AdAOSDlLogResetType_Type.__name__ = "Integer32"
_AdAOSDlLogResetType_Object = MibTableColumn
adAOSDlLogResetType = _AdAOSDlLogResetType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 7),
    _AdAOSDlLogResetType_Type()
)
adAOSDlLogResetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDlLogResetType.setStatus("current")


class _AdAOSDlLogErrorStatus_Type(Integer32):
    """Custom type adAOSDlLogErrorStatus based on Integer32"""
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
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 14),
          ("accessViolation", 2),
          ("corruptFile", 9),
          ("diskFull", 3),
          ("fileExists", 6),
          ("fileNotFound", 1),
          ("hardwareError", 12),
          ("illegalOperation", 4),
          ("noServer", 10),
          ("noSuchUser", 7),
          ("notDefined", 8),
          ("success", 13),
          ("tftpTimeout", 11),
          ("unknownTID", 5))
    )


_AdAOSDlLogErrorStatus_Type.__name__ = "Integer32"
_AdAOSDlLogErrorStatus_Object = MibTableColumn
adAOSDlLogErrorStatus = _AdAOSDlLogErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 8),
    _AdAOSDlLogErrorStatus_Type()
)
adAOSDlLogErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDlLogErrorStatus.setStatus("current")


class _AdAOSDlLogErrorText_Type(DisplayString):
    """Custom type adAOSDlLogErrorText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdAOSDlLogErrorText_Type.__name__ = "DisplayString"
_AdAOSDlLogErrorText_Object = MibTableColumn
adAOSDlLogErrorText = _AdAOSDlLogErrorText_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 9),
    _AdAOSDlLogErrorText_Type()
)
adAOSDlLogErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDlLogErrorText.setStatus("current")
_AdAOSDownloadConformance_ObjectIdentity = ObjectIdentity
adAOSDownloadConformance = _AdAOSDownloadConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 3)
)
_AdAOSDownloadCompliances_ObjectIdentity = ObjectIdentity
adAOSDownloadCompliances = _AdAOSDownloadCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 3, 1)
)
_AdAOSDownloadGroups_ObjectIdentity = ObjectIdentity
adAOSDownloadGroups = _AdAOSDownloadGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 3, 2)
)

# Managed Objects groups

adAOSDownloadLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 3, 2, 1)
)
adAOSDownloadLogGroup.setObjects(
      *(("ADTRAN-AOSDOWNLOAD", "adAOSDlLogIndex"),
        ("ADTRAN-AOSDOWNLOAD", "adAOSDlLogOwnerAddress"),
        ("ADTRAN-AOSDOWNLOAD", "adAOSDlLogOwnerDomain"),
        ("ADTRAN-AOSDOWNLOAD", "adAOSDlLogTAddress"),
        ("ADTRAN-AOSDOWNLOAD", "adAOSDlLogTDomain"),
        ("ADTRAN-AOSDOWNLOAD", "adAOSDlLogFilename"),
        ("ADTRAN-AOSDOWNLOAD", "adAOSDlLogResetType"),
        ("ADTRAN-AOSDOWNLOAD", "adAOSDlLogErrorStatus"),
        ("ADTRAN-AOSDOWNLOAD", "adAOSDlLogErrorText"))
)
if mibBuilder.loadTexts:
    adAOSDownloadLogGroup.setStatus("current")

adAOSDownloadConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 3, 2, 2)
)
adAOSDownloadConfigGroup.setObjects(
      *(("ADTRAN-AOSDOWNLOAD", "adAOSDownloadIndex"),
        ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadOwnerAddress"),
        ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadOwnerDomain"),
        ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadTAddress"),
        ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadTDomain"),
        ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadFilename"),
        ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadResetType"),
        ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadErrorStatus"),
        ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadErrorText"),
        ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadStatus"),
        ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadPassesLeft"),
        ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadOctetCount"),
        ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadDestination"),
        ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadLogMaxSize"),
        ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadLogSize"))
)
if mibBuilder.loadTexts:
    adAOSDownloadConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adAOSDownloadConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 3, 1, 1)
)
if mibBuilder.loadTexts:
    adAOSDownloadConfigCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOSDOWNLOAD",
    **{"adAOSDownload": adAOSDownload,
       "adAOSDownloadTable": adAOSDownloadTable,
       "adAOSDownloadEntry": adAOSDownloadEntry,
       "adAOSDownloadIndex": adAOSDownloadIndex,
       "adAOSDownloadOwnerAddress": adAOSDownloadOwnerAddress,
       "adAOSDownloadOwnerDomain": adAOSDownloadOwnerDomain,
       "adAOSDownloadTAddress": adAOSDownloadTAddress,
       "adAOSDownloadTDomain": adAOSDownloadTDomain,
       "adAOSDownloadFilename": adAOSDownloadFilename,
       "adAOSDownloadResetType": adAOSDownloadResetType,
       "adAOSDownloadErrorStatus": adAOSDownloadErrorStatus,
       "adAOSDownloadErrorText": adAOSDownloadErrorText,
       "adAOSDownloadStatus": adAOSDownloadStatus,
       "adAOSDownloadPassesLeft": adAOSDownloadPassesLeft,
       "adAOSDownloadOctetCount": adAOSDownloadOctetCount,
       "adAOSDownloadDestination": adAOSDownloadDestination,
       "adAOSDownloadDestinationType": adAOSDownloadDestinationType,
       "adAOSDownloadLogMaxSize": adAOSDownloadLogMaxSize,
       "adAOSDownloadLogSize": adAOSDownloadLogSize,
       "adAOSDownloadLogTable": adAOSDownloadLogTable,
       "adAOSDownloadLogEntry": adAOSDownloadLogEntry,
       "adAOSDlLogIndex": adAOSDlLogIndex,
       "adAOSDlLogOwnerAddress": adAOSDlLogOwnerAddress,
       "adAOSDlLogOwnerDomain": adAOSDlLogOwnerDomain,
       "adAOSDlLogTAddress": adAOSDlLogTAddress,
       "adAOSDlLogTDomain": adAOSDlLogTDomain,
       "adAOSDlLogFilename": adAOSDlLogFilename,
       "adAOSDlLogResetType": adAOSDlLogResetType,
       "adAOSDlLogErrorStatus": adAOSDlLogErrorStatus,
       "adAOSDlLogErrorText": adAOSDlLogErrorText,
       "adAOSDownloadConformance": adAOSDownloadConformance,
       "adAOSDownloadCompliances": adAOSDownloadCompliances,
       "adAOSDownloadConfigCompliance": adAOSDownloadConfigCompliance,
       "adAOSDownloadGroups": adAOSDownloadGroups,
       "adAOSDownloadLogGroup": adAOSDownloadLogGroup,
       "adAOSDownloadConfigGroup": adAOSDownloadConfigGroup,
       "adAOSDownloadMib": adAOSDownloadMib}
)
