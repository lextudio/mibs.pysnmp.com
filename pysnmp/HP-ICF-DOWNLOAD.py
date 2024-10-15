# SNMP MIB module (HP-ICF-DOWNLOAD) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-DOWNLOAD
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:24 2024
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

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(hpicfCommon,
 hpicfObjectModules) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpicfCommon",
    "hpicfObjectModules")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfDownloadMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4)
)
hpicfDownloadMib.setRevisions(
        ("2015-10-14 00:00",
         "2013-06-21 00:00",
         "2010-05-11 00:00",
         "2008-12-10 00:00",
         "2008-04-04 00:00",
         "2007-11-05 16:16",
         "2000-11-03 22:16",
         "1997-03-06 03:36",
         "1996-09-10 02:25",
         "1996-01-25 03:56",
         "1995-07-13 00:00",
         "1994-11-20 00:00",
         "1994-02-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfDownloadConformance_ObjectIdentity = ObjectIdentity
hpicfDownloadConformance = _HpicfDownloadConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1)
)
_HpicfDownloadCompliances_ObjectIdentity = ObjectIdentity
hpicfDownloadCompliances = _HpicfDownloadCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1, 1)
)
_HpicfDownloadGroups_ObjectIdentity = ObjectIdentity
hpicfDownloadGroups = _HpicfDownloadGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1, 2)
)
_HpicfDownload_ObjectIdentity = ObjectIdentity
hpicfDownload = _HpicfDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3)
)
_HpicfDownloadTable_Object = MibTable
hpicfDownloadTable = _HpicfDownloadTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpicfDownloadTable.setStatus("deprecated")
_HpicfDownloadEntry_Object = MibTableRow
hpicfDownloadEntry = _HpicfDownloadEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1)
)
hpicfDownloadEntry.setIndexNames(
    (0, "HP-ICF-DOWNLOAD", "hpicfDownloadIndex"),
)
if mibBuilder.loadTexts:
    hpicfDownloadEntry.setStatus("deprecated")


class _HpicfDownloadIndex_Type(Integer32):
    """Custom type hpicfDownloadIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("dlInstance", 1)
    )


_HpicfDownloadIndex_Type.__name__ = "Integer32"
_HpicfDownloadIndex_Object = MibTableColumn
hpicfDownloadIndex = _HpicfDownloadIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 1),
    _HpicfDownloadIndex_Type()
)
hpicfDownloadIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDownloadIndex.setStatus("deprecated")
_HpicfDownloadOwnerAddress_Type = TAddress
_HpicfDownloadOwnerAddress_Object = MibTableColumn
hpicfDownloadOwnerAddress = _HpicfDownloadOwnerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 2),
    _HpicfDownloadOwnerAddress_Type()
)
hpicfDownloadOwnerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDownloadOwnerAddress.setStatus("deprecated")
_HpicfDownloadOwnerDomain_Type = TDomain
_HpicfDownloadOwnerDomain_Object = MibTableColumn
hpicfDownloadOwnerDomain = _HpicfDownloadOwnerDomain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 3),
    _HpicfDownloadOwnerDomain_Type()
)
hpicfDownloadOwnerDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDownloadOwnerDomain.setStatus("deprecated")
_HpicfDownloadTAddress_Type = TAddress
_HpicfDownloadTAddress_Object = MibTableColumn
hpicfDownloadTAddress = _HpicfDownloadTAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 4),
    _HpicfDownloadTAddress_Type()
)
hpicfDownloadTAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDownloadTAddress.setStatus("deprecated")
_HpicfDownloadTDomain_Type = TDomain
_HpicfDownloadTDomain_Object = MibTableColumn
hpicfDownloadTDomain = _HpicfDownloadTDomain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 5),
    _HpicfDownloadTDomain_Type()
)
hpicfDownloadTDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDownloadTDomain.setStatus("deprecated")


class _HpicfDownloadFilename_Type(DisplayString):
    """Custom type hpicfDownloadFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpicfDownloadFilename_Type.__name__ = "DisplayString"
_HpicfDownloadFilename_Object = MibTableColumn
hpicfDownloadFilename = _HpicfDownloadFilename_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 6),
    _HpicfDownloadFilename_Type()
)
hpicfDownloadFilename.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDownloadFilename.setStatus("deprecated")


class _HpicfDownloadResetType_Type(Integer32):
    """Custom type hpicfDownloadResetType based on Integer32"""
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


_HpicfDownloadResetType_Type.__name__ = "Integer32"
_HpicfDownloadResetType_Object = MibTableColumn
hpicfDownloadResetType = _HpicfDownloadResetType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 7),
    _HpicfDownloadResetType_Type()
)
hpicfDownloadResetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDownloadResetType.setStatus("deprecated")


class _HpicfDownloadErrorStatus_Type(Integer32):
    """Custom type hpicfDownloadErrorStatus based on Integer32"""
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


_HpicfDownloadErrorStatus_Type.__name__ = "Integer32"
_HpicfDownloadErrorStatus_Object = MibTableColumn
hpicfDownloadErrorStatus = _HpicfDownloadErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 8),
    _HpicfDownloadErrorStatus_Type()
)
hpicfDownloadErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDownloadErrorStatus.setStatus("deprecated")


class _HpicfDownloadErrorText_Type(DisplayString):
    """Custom type hpicfDownloadErrorText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfDownloadErrorText_Type.__name__ = "DisplayString"
_HpicfDownloadErrorText_Object = MibTableColumn
hpicfDownloadErrorText = _HpicfDownloadErrorText_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 9),
    _HpicfDownloadErrorText_Type()
)
hpicfDownloadErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDownloadErrorText.setStatus("deprecated")
_HpicfDownloadStatus_Type = RowStatus
_HpicfDownloadStatus_Object = MibTableColumn
hpicfDownloadStatus = _HpicfDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 10),
    _HpicfDownloadStatus_Type()
)
hpicfDownloadStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDownloadStatus.setStatus("deprecated")
_HpicfDownloadPassesLeft_Type = Integer32
_HpicfDownloadPassesLeft_Object = MibTableColumn
hpicfDownloadPassesLeft = _HpicfDownloadPassesLeft_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 11),
    _HpicfDownloadPassesLeft_Type()
)
hpicfDownloadPassesLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDownloadPassesLeft.setStatus("deprecated")
_HpicfDownloadOctetCount_Type = Integer32
_HpicfDownloadOctetCount_Object = MibTableColumn
hpicfDownloadOctetCount = _HpicfDownloadOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 12),
    _HpicfDownloadOctetCount_Type()
)
hpicfDownloadOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDownloadOctetCount.setStatus("deprecated")


class _HpicfDownloadDestination_Type(DisplayString):
    """Custom type hpicfDownloadDestination based on DisplayString"""
    defaultValue = OctetString("/os/primary")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpicfDownloadDestination_Type.__name__ = "DisplayString"
_HpicfDownloadDestination_Object = MibTableColumn
hpicfDownloadDestination = _HpicfDownloadDestination_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 13),
    _HpicfDownloadDestination_Type()
)
hpicfDownloadDestination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDownloadDestination.setStatus("deprecated")


class _HpicfDownloadLogMaxSize_Type(Integer32):
    """Custom type hpicfDownloadLogMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfDownloadLogMaxSize_Type.__name__ = "Integer32"
_HpicfDownloadLogMaxSize_Object = MibScalar
hpicfDownloadLogMaxSize = _HpicfDownloadLogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 2),
    _HpicfDownloadLogMaxSize_Type()
)
hpicfDownloadLogMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDownloadLogMaxSize.setStatus("current")


class _HpicfDownloadLogSize_Type(Gauge32):
    """Custom type hpicfDownloadLogSize based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfDownloadLogSize_Type.__name__ = "Gauge32"
_HpicfDownloadLogSize_Object = MibScalar
hpicfDownloadLogSize = _HpicfDownloadLogSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 3),
    _HpicfDownloadLogSize_Type()
)
hpicfDownloadLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDownloadLogSize.setStatus("current")
_HpicfDownloadLogTable_Object = MibTable
hpicfDownloadLogTable = _HpicfDownloadLogTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4)
)
if mibBuilder.loadTexts:
    hpicfDownloadLogTable.setStatus("current")
_HpicfDownloadLogEntry_Object = MibTableRow
hpicfDownloadLogEntry = _HpicfDownloadLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1)
)
hpicfDownloadLogEntry.setIndexNames(
    (0, "HP-ICF-DOWNLOAD", "hpicfDlLogIndex"),
)
if mibBuilder.loadTexts:
    hpicfDownloadLogEntry.setStatus("current")


class _HpicfDlLogIndex_Type(Integer32):
    """Custom type hpicfDlLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfDlLogIndex_Type.__name__ = "Integer32"
_HpicfDlLogIndex_Object = MibTableColumn
hpicfDlLogIndex = _HpicfDlLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 1),
    _HpicfDlLogIndex_Type()
)
hpicfDlLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDlLogIndex.setStatus("current")
_HpicfDlLogOwnerAddress_Type = TAddress
_HpicfDlLogOwnerAddress_Object = MibTableColumn
hpicfDlLogOwnerAddress = _HpicfDlLogOwnerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 2),
    _HpicfDlLogOwnerAddress_Type()
)
hpicfDlLogOwnerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDlLogOwnerAddress.setStatus("current")
_HpicfDlLogOwnerDomain_Type = TDomain
_HpicfDlLogOwnerDomain_Object = MibTableColumn
hpicfDlLogOwnerDomain = _HpicfDlLogOwnerDomain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 3),
    _HpicfDlLogOwnerDomain_Type()
)
hpicfDlLogOwnerDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDlLogOwnerDomain.setStatus("current")
_HpicfDlLogTAddress_Type = TAddress
_HpicfDlLogTAddress_Object = MibTableColumn
hpicfDlLogTAddress = _HpicfDlLogTAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 4),
    _HpicfDlLogTAddress_Type()
)
hpicfDlLogTAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDlLogTAddress.setStatus("current")
_HpicfDlLogTDomain_Type = TDomain
_HpicfDlLogTDomain_Object = MibTableColumn
hpicfDlLogTDomain = _HpicfDlLogTDomain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 5),
    _HpicfDlLogTDomain_Type()
)
hpicfDlLogTDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDlLogTDomain.setStatus("current")


class _HpicfDlLogFilename_Type(DisplayString):
    """Custom type hpicfDlLogFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpicfDlLogFilename_Type.__name__ = "DisplayString"
_HpicfDlLogFilename_Object = MibTableColumn
hpicfDlLogFilename = _HpicfDlLogFilename_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 6),
    _HpicfDlLogFilename_Type()
)
hpicfDlLogFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDlLogFilename.setStatus("current")


class _HpicfDlLogResetType_Type(Integer32):
    """Custom type hpicfDlLogResetType based on Integer32"""
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


_HpicfDlLogResetType_Type.__name__ = "Integer32"
_HpicfDlLogResetType_Object = MibTableColumn
hpicfDlLogResetType = _HpicfDlLogResetType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 7),
    _HpicfDlLogResetType_Type()
)
hpicfDlLogResetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDlLogResetType.setStatus("current")


class _HpicfDlLogErrorStatus_Type(Integer32):
    """Custom type hpicfDlLogErrorStatus based on Integer32"""
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


_HpicfDlLogErrorStatus_Type.__name__ = "Integer32"
_HpicfDlLogErrorStatus_Object = MibTableColumn
hpicfDlLogErrorStatus = _HpicfDlLogErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 8),
    _HpicfDlLogErrorStatus_Type()
)
hpicfDlLogErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDlLogErrorStatus.setStatus("current")


class _HpicfDlLogErrorText_Type(DisplayString):
    """Custom type hpicfDlLogErrorText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfDlLogErrorText_Type.__name__ = "DisplayString"
_HpicfDlLogErrorText_Object = MibTableColumn
hpicfDlLogErrorText = _HpicfDlLogErrorText_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 9),
    _HpicfDlLogErrorText_Type()
)
hpicfDlLogErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDlLogErrorText.setStatus("current")


class _HpicfDownloadTftpConfig_Type(Integer32):
    """Custom type hpicfDownloadTftpConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HpicfDownloadTftpConfig_Type.__name__ = "Integer32"
_HpicfDownloadTftpConfig_Object = MibScalar
hpicfDownloadTftpConfig = _HpicfDownloadTftpConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 5),
    _HpicfDownloadTftpConfig_Type()
)
hpicfDownloadTftpConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDownloadTftpConfig.setStatus("deprecated")
_HpicfDownloadTftpServerConfig_Type = TruthValue
_HpicfDownloadTftpServerConfig_Object = MibScalar
hpicfDownloadTftpServerConfig = _HpicfDownloadTftpServerConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 6),
    _HpicfDownloadTftpServerConfig_Type()
)
hpicfDownloadTftpServerConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDownloadTftpServerConfig.setStatus("current")


class _HpicfDownloadTftp6Config_Type(Integer32):
    """Custom type hpicfDownloadTftp6Config based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HpicfDownloadTftp6Config_Type.__name__ = "Integer32"
_HpicfDownloadTftp6Config_Object = MibScalar
hpicfDownloadTftp6Config = _HpicfDownloadTftp6Config_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 7),
    _HpicfDownloadTftp6Config_Type()
)
hpicfDownloadTftp6Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDownloadTftp6Config.setStatus("deprecated")
_HpicfDownloadTftp6ServerConfig_Type = TruthValue
_HpicfDownloadTftp6ServerConfig_Object = MibScalar
hpicfDownloadTftp6ServerConfig = _HpicfDownloadTftp6ServerConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 8),
    _HpicfDownloadTftp6ServerConfig_Type()
)
hpicfDownloadTftp6ServerConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDownloadTftp6ServerConfig.setStatus("deprecated")
_HpicfDownloadInetTable_Object = MibTable
hpicfDownloadInetTable = _HpicfDownloadInetTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 9)
)
if mibBuilder.loadTexts:
    hpicfDownloadInetTable.setStatus("current")
_HpicfDownloadInetEntry_Object = MibTableRow
hpicfDownloadInetEntry = _HpicfDownloadInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 9, 1)
)
hpicfDownloadInetEntry.setIndexNames(
    (0, "HP-ICF-DOWNLOAD", "hpicfDownloadInetIndex"),
)
if mibBuilder.loadTexts:
    hpicfDownloadInetEntry.setStatus("current")


class _HpicfDownloadInetIndex_Type(Integer32):
    """Custom type hpicfDownloadInetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpicfDownloadInetIndex_Type.__name__ = "Integer32"
_HpicfDownloadInetIndex_Object = MibTableColumn
hpicfDownloadInetIndex = _HpicfDownloadInetIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 9, 1, 1),
    _HpicfDownloadInetIndex_Type()
)
hpicfDownloadInetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDownloadInetIndex.setStatus("current")
_HpicfDownloadInetTAddressType_Type = InetAddressType
_HpicfDownloadInetTAddressType_Object = MibTableColumn
hpicfDownloadInetTAddressType = _HpicfDownloadInetTAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 9, 1, 2),
    _HpicfDownloadInetTAddressType_Type()
)
hpicfDownloadInetTAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDownloadInetTAddressType.setStatus("current")
_HpicfDownloadInetTAddress_Type = InetAddress
_HpicfDownloadInetTAddress_Object = MibTableColumn
hpicfDownloadInetTAddress = _HpicfDownloadInetTAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 9, 1, 3),
    _HpicfDownloadInetTAddress_Type()
)
hpicfDownloadInetTAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDownloadInetTAddress.setStatus("current")


class _HpicfDownloadInetFilename_Type(DisplayString):
    """Custom type hpicfDownloadInetFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpicfDownloadInetFilename_Type.__name__ = "DisplayString"
_HpicfDownloadInetFilename_Object = MibTableColumn
hpicfDownloadInetFilename = _HpicfDownloadInetFilename_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 9, 1, 4),
    _HpicfDownloadInetFilename_Type()
)
hpicfDownloadInetFilename.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDownloadInetFilename.setStatus("current")
_HpicfDownloadInetOwnerAddressType_Type = InetAddressType
_HpicfDownloadInetOwnerAddressType_Object = MibTableColumn
hpicfDownloadInetOwnerAddressType = _HpicfDownloadInetOwnerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 9, 1, 5),
    _HpicfDownloadInetOwnerAddressType_Type()
)
hpicfDownloadInetOwnerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDownloadInetOwnerAddressType.setStatus("current")
_HpicfDownloadInetOwnerAddress_Type = InetAddress
_HpicfDownloadInetOwnerAddress_Object = MibTableColumn
hpicfDownloadInetOwnerAddress = _HpicfDownloadInetOwnerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 9, 1, 6),
    _HpicfDownloadInetOwnerAddress_Type()
)
hpicfDownloadInetOwnerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDownloadInetOwnerAddress.setStatus("current")


class _HpicfDownloadInetSourcePort_Type(Integer32):
    """Custom type hpicfDownloadInetSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfDownloadInetSourcePort_Type.__name__ = "Integer32"
_HpicfDownloadInetSourcePort_Object = MibTableColumn
hpicfDownloadInetSourcePort = _HpicfDownloadInetSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 9, 1, 7),
    _HpicfDownloadInetSourcePort_Type()
)
hpicfDownloadInetSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDownloadInetSourcePort.setStatus("current")


class _HpicfDownloadInetDestinationPort_Type(Integer32):
    """Custom type hpicfDownloadInetDestinationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfDownloadInetDestinationPort_Type.__name__ = "Integer32"
_HpicfDownloadInetDestinationPort_Object = MibTableColumn
hpicfDownloadInetDestinationPort = _HpicfDownloadInetDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 9, 1, 8),
    _HpicfDownloadInetDestinationPort_Type()
)
hpicfDownloadInetDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDownloadInetDestinationPort.setStatus("current")


class _HpicfDownloadInetFileTransferType_Type(Integer32):
    """Custom type hpicfDownloadInetFileTransferType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 2),
          ("usb", 1),
          ("xmodem", 3))
    )


_HpicfDownloadInetFileTransferType_Type.__name__ = "Integer32"
_HpicfDownloadInetFileTransferType_Object = MibTableColumn
hpicfDownloadInetFileTransferType = _HpicfDownloadInetFileTransferType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 9, 1, 9),
    _HpicfDownloadInetFileTransferType_Type()
)
hpicfDownloadInetFileTransferType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDownloadInetFileTransferType.setStatus("current")


class _HpicfDownloadInetResetType_Type(Integer32):
    """Custom type hpicfDownloadInetResetType based on Integer32"""
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


_HpicfDownloadInetResetType_Type.__name__ = "Integer32"
_HpicfDownloadInetResetType_Object = MibTableColumn
hpicfDownloadInetResetType = _HpicfDownloadInetResetType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 9, 1, 10),
    _HpicfDownloadInetResetType_Type()
)
hpicfDownloadInetResetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDownloadInetResetType.setStatus("current")


class _HpicfDownloadInetErrorStatus_Type(Integer32):
    """Custom type hpicfDownloadInetErrorStatus based on Integer32"""
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


_HpicfDownloadInetErrorStatus_Type.__name__ = "Integer32"
_HpicfDownloadInetErrorStatus_Object = MibTableColumn
hpicfDownloadInetErrorStatus = _HpicfDownloadInetErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 9, 1, 11),
    _HpicfDownloadInetErrorStatus_Type()
)
hpicfDownloadInetErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDownloadInetErrorStatus.setStatus("current")


class _HpicfDownloadInetErrorText_Type(DisplayString):
    """Custom type hpicfDownloadInetErrorText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfDownloadInetErrorText_Type.__name__ = "DisplayString"
_HpicfDownloadInetErrorText_Object = MibTableColumn
hpicfDownloadInetErrorText = _HpicfDownloadInetErrorText_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 9, 1, 12),
    _HpicfDownloadInetErrorText_Type()
)
hpicfDownloadInetErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDownloadInetErrorText.setStatus("current")
_HpicfDownloadInetStatus_Type = RowStatus
_HpicfDownloadInetStatus_Object = MibTableColumn
hpicfDownloadInetStatus = _HpicfDownloadInetStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 9, 1, 13),
    _HpicfDownloadInetStatus_Type()
)
hpicfDownloadInetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDownloadInetStatus.setStatus("current")
_HpicfDownloadInetPassesLeft_Type = Integer32
_HpicfDownloadInetPassesLeft_Object = MibTableColumn
hpicfDownloadInetPassesLeft = _HpicfDownloadInetPassesLeft_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 9, 1, 14),
    _HpicfDownloadInetPassesLeft_Type()
)
hpicfDownloadInetPassesLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDownloadInetPassesLeft.setStatus("current")
_HpicfDownloadInetOctetCount_Type = Integer32
_HpicfDownloadInetOctetCount_Object = MibTableColumn
hpicfDownloadInetOctetCount = _HpicfDownloadInetOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 9, 1, 15),
    _HpicfDownloadInetOctetCount_Type()
)
hpicfDownloadInetOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDownloadInetOctetCount.setStatus("current")


class _HpicfDownloadInetDestination_Type(DisplayString):
    """Custom type hpicfDownloadInetDestination based on DisplayString"""
    defaultValue = OctetString("/os/primary")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpicfDownloadInetDestination_Type.__name__ = "DisplayString"
_HpicfDownloadInetDestination_Object = MibTableColumn
hpicfDownloadInetDestination = _HpicfDownloadInetDestination_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 9, 1, 16),
    _HpicfDownloadInetDestination_Type()
)
hpicfDownloadInetDestination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDownloadInetDestination.setStatus("current")


class _HpicfDownloadInetOpType_Type(Integer32):
    """Custom type hpicfDownloadInetOpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftget", 1),
          ("ftput", 2))
    )


_HpicfDownloadInetOpType_Type.__name__ = "Integer32"
_HpicfDownloadInetOpType_Object = MibTableColumn
hpicfDownloadInetOpType = _HpicfDownloadInetOpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 9, 1, 17),
    _HpicfDownloadInetOpType_Type()
)
hpicfDownloadInetOpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDownloadInetOpType.setStatus("current")


class _HpicfDownloadInetFileType_Type(Integer32):
    """Custom type hpicfDownloadInetFileType based on Integer32"""
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
        *(("config", 4),
          ("coreDump", 5),
          ("flash", 1),
          ("runningConfig", 3),
          ("startUpConfig", 2))
    )


_HpicfDownloadInetFileType_Type.__name__ = "Integer32"
_HpicfDownloadInetFileType_Object = MibTableColumn
hpicfDownloadInetFileType = _HpicfDownloadInetFileType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 9, 1, 18),
    _HpicfDownloadInetFileType_Type()
)
hpicfDownloadInetFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDownloadInetFileType.setStatus("current")


class _HpicfDownloadInetFileModeType_Type(Integer32):
    """Custom type hpicfDownloadInetFileModeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pc", 2),
          ("unix", 1))
    )


_HpicfDownloadInetFileModeType_Type.__name__ = "Integer32"
_HpicfDownloadInetFileModeType_Object = MibTableColumn
hpicfDownloadInetFileModeType = _HpicfDownloadInetFileModeType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 9, 1, 19),
    _HpicfDownloadInetFileModeType_Type()
)
hpicfDownloadInetFileModeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDownloadInetFileModeType.setStatus("current")
_HpicfDownloadInetCoreDumpModule_Type = PhysicalIndex
_HpicfDownloadInetCoreDumpModule_Object = MibTableColumn
hpicfDownloadInetCoreDumpModule = _HpicfDownloadInetCoreDumpModule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 9, 1, 20),
    _HpicfDownloadInetCoreDumpModule_Type()
)
hpicfDownloadInetCoreDumpModule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDownloadInetCoreDumpModule.setStatus("current")
_HpicfDownloadConfigFileUpdateEnabled_Type = TruthValue
_HpicfDownloadConfigFileUpdateEnabled_Object = MibScalar
hpicfDownloadConfigFileUpdateEnabled = _HpicfDownloadConfigFileUpdateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 10),
    _HpicfDownloadConfigFileUpdateEnabled_Type()
)
hpicfDownloadConfigFileUpdateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDownloadConfigFileUpdateEnabled.setStatus("current")
_HpicfDownloadAutoTftpTable_Object = MibTable
hpicfDownloadAutoTftpTable = _HpicfDownloadAutoTftpTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 11)
)
if mibBuilder.loadTexts:
    hpicfDownloadAutoTftpTable.setStatus("current")
_HpicfDownloadAutoTftpEntry_Object = MibTableRow
hpicfDownloadAutoTftpEntry = _HpicfDownloadAutoTftpEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 11, 1)
)
hpicfDownloadAutoTftpEntry.setIndexNames(
    (0, "HP-ICF-DOWNLOAD", "hpicfDownloadAutoTftpIndex"),
)
if mibBuilder.loadTexts:
    hpicfDownloadAutoTftpEntry.setStatus("current")


class _HpicfDownloadAutoTftpIndex_Type(Integer32):
    """Custom type hpicfDownloadAutoTftpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfDownloadAutoTftpIndex_Type.__name__ = "Integer32"
_HpicfDownloadAutoTftpIndex_Object = MibTableColumn
hpicfDownloadAutoTftpIndex = _HpicfDownloadAutoTftpIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 11, 1, 1),
    _HpicfDownloadAutoTftpIndex_Type()
)
hpicfDownloadAutoTftpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDownloadAutoTftpIndex.setStatus("current")
_HpicfDownloadAutoTftpAddressType_Type = InetAddressType
_HpicfDownloadAutoTftpAddressType_Object = MibTableColumn
hpicfDownloadAutoTftpAddressType = _HpicfDownloadAutoTftpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 11, 1, 2),
    _HpicfDownloadAutoTftpAddressType_Type()
)
hpicfDownloadAutoTftpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDownloadAutoTftpAddressType.setStatus("current")
_HpicfDownloadAutoTftpAddress_Type = InetAddress
_HpicfDownloadAutoTftpAddress_Object = MibTableColumn
hpicfDownloadAutoTftpAddress = _HpicfDownloadAutoTftpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 11, 1, 3),
    _HpicfDownloadAutoTftpAddress_Type()
)
hpicfDownloadAutoTftpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDownloadAutoTftpAddress.setStatus("current")


class _HpicfDownloadAutoTftpRemoteFilename_Type(DisplayString):
    """Custom type hpicfDownloadAutoTftpRemoteFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfDownloadAutoTftpRemoteFilename_Type.__name__ = "DisplayString"
_HpicfDownloadAutoTftpRemoteFilename_Object = MibTableColumn
hpicfDownloadAutoTftpRemoteFilename = _HpicfDownloadAutoTftpRemoteFilename_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 11, 1, 4),
    _HpicfDownloadAutoTftpRemoteFilename_Type()
)
hpicfDownloadAutoTftpRemoteFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDownloadAutoTftpRemoteFilename.setStatus("current")


class _HpicfDownloadAutoTftpAdminStatus_Type(Integer32):
    """Custom type hpicfDownloadAutoTftpAdminStatus based on Integer32"""
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


_HpicfDownloadAutoTftpAdminStatus_Type.__name__ = "Integer32"
_HpicfDownloadAutoTftpAdminStatus_Object = MibTableColumn
hpicfDownloadAutoTftpAdminStatus = _HpicfDownloadAutoTftpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 11, 1, 5),
    _HpicfDownloadAutoTftpAdminStatus_Type()
)
hpicfDownloadAutoTftpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDownloadAutoTftpAdminStatus.setStatus("current")


class _HpicfDownloadTftpClientConfig_Type(Integer32):
    """Custom type hpicfDownloadTftpClientConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfDownloadTftpClientConfig_Type.__name__ = "Integer32"
_HpicfDownloadTftpClientConfig_Object = MibScalar
hpicfDownloadTftpClientConfig = _HpicfDownloadTftpClientConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 12),
    _HpicfDownloadTftpClientConfig_Type()
)
hpicfDownloadTftpClientConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDownloadTftpClientConfig.setStatus("current")


class _HpicfDownloadTftpClientBlkSize_Type(Integer32):
    """Custom type hpicfDownloadTftpClientBlkSize based on Integer32"""
    defaultValue = 1416

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 8192),
    )


_HpicfDownloadTftpClientBlkSize_Type.__name__ = "Integer32"
_HpicfDownloadTftpClientBlkSize_Object = MibScalar
hpicfDownloadTftpClientBlkSize = _HpicfDownloadTftpClientBlkSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 13),
    _HpicfDownloadTftpClientBlkSize_Type()
)
hpicfDownloadTftpClientBlkSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDownloadTftpClientBlkSize.setStatus("current")

# Managed Objects groups

hpicfDownloadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1, 2, 1)
)
hpicfDownloadGroup.setObjects(
      *(("HP-ICF-DOWNLOAD", "hpicfDownloadIndex"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadOwnerAddress"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadOwnerDomain"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadTAddress"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadTDomain"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadFilename"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadResetType"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadErrorStatus"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadErrorText"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadStatus"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadLogMaxSize"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadLogSize"))
)
if mibBuilder.loadTexts:
    hpicfDownloadGroup.setStatus("deprecated")

hpicfDownloadLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1, 2, 2)
)
hpicfDownloadLogGroup.setObjects(
      *(("HP-ICF-DOWNLOAD", "hpicfDlLogIndex"),
        ("HP-ICF-DOWNLOAD", "hpicfDlLogOwnerAddress"),
        ("HP-ICF-DOWNLOAD", "hpicfDlLogOwnerDomain"),
        ("HP-ICF-DOWNLOAD", "hpicfDlLogTAddress"),
        ("HP-ICF-DOWNLOAD", "hpicfDlLogTDomain"),
        ("HP-ICF-DOWNLOAD", "hpicfDlLogFilename"),
        ("HP-ICF-DOWNLOAD", "hpicfDlLogResetType"),
        ("HP-ICF-DOWNLOAD", "hpicfDlLogErrorStatus"),
        ("HP-ICF-DOWNLOAD", "hpicfDlLogErrorText"))
)
if mibBuilder.loadTexts:
    hpicfDownloadLogGroup.setStatus("current")

hpicfDownloadConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1, 2, 3)
)
hpicfDownloadConfigGroup.setObjects(
      *(("HP-ICF-DOWNLOAD", "hpicfDownloadIndex"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadOwnerAddress"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadOwnerDomain"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadTAddress"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadTDomain"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadFilename"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadResetType"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadErrorStatus"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadErrorText"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadStatus"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadPassesLeft"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadOctetCount"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadDestination"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadLogMaxSize"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadLogSize"))
)
if mibBuilder.loadTexts:
    hpicfDownloadConfigGroup.setStatus("deprecated")

hpicfDownloadConfigInetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1, 2, 4)
)
hpicfDownloadConfigInetGroup.setObjects(
      *(("HP-ICF-DOWNLOAD", "hpicfDownloadLogMaxSize"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadLogSize"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadInetIndex"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadInetTAddressType"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadInetTAddress"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadInetFilename"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadInetOwnerAddressType"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadInetOwnerAddress"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadInetSourcePort"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadInetDestinationPort"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadInetFileTransferType"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadInetResetType"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadInetErrorStatus"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadInetErrorText"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadInetStatus"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadInetPassesLeft"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadInetOctetCount"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadInetDestination"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadInetOpType"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadInetFileType"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadInetFileModeType"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadInetCoreDumpModule"))
)
if mibBuilder.loadTexts:
    hpicfDownloadConfigInetGroup.setStatus("current")

hpicfDownloadAutoTftpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1, 2, 5)
)
hpicfDownloadAutoTftpGroup.setObjects(
      *(("HP-ICF-DOWNLOAD", "hpicfDownloadAutoTftpAddressType"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadAutoTftpAddress"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadAutoTftpRemoteFilename"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadAutoTftpAdminStatus"))
)
if mibBuilder.loadTexts:
    hpicfDownloadAutoTftpGroup.setStatus("current")

hpicfDownloadConfigOtherGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1, 2, 6)
)
hpicfDownloadConfigOtherGroup.setObjects(
      *(("HP-ICF-DOWNLOAD", "hpicfDownloadAutoTftpAdminStatus"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadTftpConfig"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadTftpServerConfig"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadConfigFileUpdateEnabled"))
)
if mibBuilder.loadTexts:
    hpicfDownloadConfigOtherGroup.setStatus("deprecated")

hpicfDownloadConfigOtherGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1, 2, 7)
)
hpicfDownloadConfigOtherGroup1.setObjects(
      *(("HP-ICF-DOWNLOAD", "hpicfDownloadTftp6Config"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadTftp6ServerConfig"))
)
if mibBuilder.loadTexts:
    hpicfDownloadConfigOtherGroup1.setStatus("deprecated")

hpicfDownloadConfigOtherGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1, 2, 8)
)
hpicfDownloadConfigOtherGroup2.setObjects(
      *(("HP-ICF-DOWNLOAD", "hpicfDownloadAutoTftpAdminStatus"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadTftpClientConfig"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadTftpServerConfig"),
        ("HP-ICF-DOWNLOAD", "hpicfDownloadConfigFileUpdateEnabled"))
)
if mibBuilder.loadTexts:
    hpicfDownloadConfigOtherGroup2.setStatus("current")

hpicfDownloadConfigOtherGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1, 2, 9)
)
hpicfDownloadConfigOtherGroup3.setObjects(
    ("HP-ICF-DOWNLOAD", "hpicfDownloadTftpClientBlkSize")
)
if mibBuilder.loadTexts:
    hpicfDownloadConfigOtherGroup3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfDownloadCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfDownloadCompliance.setStatus(
        "deprecated"
    )

hpicfDownloadConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfDownloadConfigCompliance.setStatus(
        "deprecated"
    )

hpicfDownloadConfigInetCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfDownloadConfigInetCompliance.setStatus(
        "current"
    )

hpicfDownloadAutoTftpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfDownloadAutoTftpCompliance.setStatus(
        "current"
    )

hpicfDownloadConfigInetCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfDownloadConfigInetCompliance1.setStatus(
        "deprecated"
    )

hpicfDownloadConfigInetCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hpicfDownloadConfigInetCompliance2.setStatus(
        "deprecated"
    )

hpicfDownloadConfigInetCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hpicfDownloadConfigInetCompliance3.setStatus(
        "current"
    )

hpicfDownloadConfigInetCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1, 1, 8)
)
if mibBuilder.loadTexts:
    hpicfDownloadConfigInetCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-DOWNLOAD",
    **{"hpicfDownloadMib": hpicfDownloadMib,
       "hpicfDownloadConformance": hpicfDownloadConformance,
       "hpicfDownloadCompliances": hpicfDownloadCompliances,
       "hpicfDownloadCompliance": hpicfDownloadCompliance,
       "hpicfDownloadConfigCompliance": hpicfDownloadConfigCompliance,
       "hpicfDownloadConfigInetCompliance": hpicfDownloadConfigInetCompliance,
       "hpicfDownloadAutoTftpCompliance": hpicfDownloadAutoTftpCompliance,
       "hpicfDownloadConfigInetCompliance1": hpicfDownloadConfigInetCompliance1,
       "hpicfDownloadConfigInetCompliance2": hpicfDownloadConfigInetCompliance2,
       "hpicfDownloadConfigInetCompliance3": hpicfDownloadConfigInetCompliance3,
       "hpicfDownloadConfigInetCompliance4": hpicfDownloadConfigInetCompliance4,
       "hpicfDownloadGroups": hpicfDownloadGroups,
       "hpicfDownloadGroup": hpicfDownloadGroup,
       "hpicfDownloadLogGroup": hpicfDownloadLogGroup,
       "hpicfDownloadConfigGroup": hpicfDownloadConfigGroup,
       "hpicfDownloadConfigInetGroup": hpicfDownloadConfigInetGroup,
       "hpicfDownloadAutoTftpGroup": hpicfDownloadAutoTftpGroup,
       "hpicfDownloadConfigOtherGroup": hpicfDownloadConfigOtherGroup,
       "hpicfDownloadConfigOtherGroup1": hpicfDownloadConfigOtherGroup1,
       "hpicfDownloadConfigOtherGroup2": hpicfDownloadConfigOtherGroup2,
       "hpicfDownloadConfigOtherGroup3": hpicfDownloadConfigOtherGroup3,
       "hpicfDownload": hpicfDownload,
       "hpicfDownloadTable": hpicfDownloadTable,
       "hpicfDownloadEntry": hpicfDownloadEntry,
       "hpicfDownloadIndex": hpicfDownloadIndex,
       "hpicfDownloadOwnerAddress": hpicfDownloadOwnerAddress,
       "hpicfDownloadOwnerDomain": hpicfDownloadOwnerDomain,
       "hpicfDownloadTAddress": hpicfDownloadTAddress,
       "hpicfDownloadTDomain": hpicfDownloadTDomain,
       "hpicfDownloadFilename": hpicfDownloadFilename,
       "hpicfDownloadResetType": hpicfDownloadResetType,
       "hpicfDownloadErrorStatus": hpicfDownloadErrorStatus,
       "hpicfDownloadErrorText": hpicfDownloadErrorText,
       "hpicfDownloadStatus": hpicfDownloadStatus,
       "hpicfDownloadPassesLeft": hpicfDownloadPassesLeft,
       "hpicfDownloadOctetCount": hpicfDownloadOctetCount,
       "hpicfDownloadDestination": hpicfDownloadDestination,
       "hpicfDownloadLogMaxSize": hpicfDownloadLogMaxSize,
       "hpicfDownloadLogSize": hpicfDownloadLogSize,
       "hpicfDownloadLogTable": hpicfDownloadLogTable,
       "hpicfDownloadLogEntry": hpicfDownloadLogEntry,
       "hpicfDlLogIndex": hpicfDlLogIndex,
       "hpicfDlLogOwnerAddress": hpicfDlLogOwnerAddress,
       "hpicfDlLogOwnerDomain": hpicfDlLogOwnerDomain,
       "hpicfDlLogTAddress": hpicfDlLogTAddress,
       "hpicfDlLogTDomain": hpicfDlLogTDomain,
       "hpicfDlLogFilename": hpicfDlLogFilename,
       "hpicfDlLogResetType": hpicfDlLogResetType,
       "hpicfDlLogErrorStatus": hpicfDlLogErrorStatus,
       "hpicfDlLogErrorText": hpicfDlLogErrorText,
       "hpicfDownloadTftpConfig": hpicfDownloadTftpConfig,
       "hpicfDownloadTftpServerConfig": hpicfDownloadTftpServerConfig,
       "hpicfDownloadTftp6Config": hpicfDownloadTftp6Config,
       "hpicfDownloadTftp6ServerConfig": hpicfDownloadTftp6ServerConfig,
       "hpicfDownloadInetTable": hpicfDownloadInetTable,
       "hpicfDownloadInetEntry": hpicfDownloadInetEntry,
       "hpicfDownloadInetIndex": hpicfDownloadInetIndex,
       "hpicfDownloadInetTAddressType": hpicfDownloadInetTAddressType,
       "hpicfDownloadInetTAddress": hpicfDownloadInetTAddress,
       "hpicfDownloadInetFilename": hpicfDownloadInetFilename,
       "hpicfDownloadInetOwnerAddressType": hpicfDownloadInetOwnerAddressType,
       "hpicfDownloadInetOwnerAddress": hpicfDownloadInetOwnerAddress,
       "hpicfDownloadInetSourcePort": hpicfDownloadInetSourcePort,
       "hpicfDownloadInetDestinationPort": hpicfDownloadInetDestinationPort,
       "hpicfDownloadInetFileTransferType": hpicfDownloadInetFileTransferType,
       "hpicfDownloadInetResetType": hpicfDownloadInetResetType,
       "hpicfDownloadInetErrorStatus": hpicfDownloadInetErrorStatus,
       "hpicfDownloadInetErrorText": hpicfDownloadInetErrorText,
       "hpicfDownloadInetStatus": hpicfDownloadInetStatus,
       "hpicfDownloadInetPassesLeft": hpicfDownloadInetPassesLeft,
       "hpicfDownloadInetOctetCount": hpicfDownloadInetOctetCount,
       "hpicfDownloadInetDestination": hpicfDownloadInetDestination,
       "hpicfDownloadInetOpType": hpicfDownloadInetOpType,
       "hpicfDownloadInetFileType": hpicfDownloadInetFileType,
       "hpicfDownloadInetFileModeType": hpicfDownloadInetFileModeType,
       "hpicfDownloadInetCoreDumpModule": hpicfDownloadInetCoreDumpModule,
       "hpicfDownloadConfigFileUpdateEnabled": hpicfDownloadConfigFileUpdateEnabled,
       "hpicfDownloadAutoTftpTable": hpicfDownloadAutoTftpTable,
       "hpicfDownloadAutoTftpEntry": hpicfDownloadAutoTftpEntry,
       "hpicfDownloadAutoTftpIndex": hpicfDownloadAutoTftpIndex,
       "hpicfDownloadAutoTftpAddressType": hpicfDownloadAutoTftpAddressType,
       "hpicfDownloadAutoTftpAddress": hpicfDownloadAutoTftpAddress,
       "hpicfDownloadAutoTftpRemoteFilename": hpicfDownloadAutoTftpRemoteFilename,
       "hpicfDownloadAutoTftpAdminStatus": hpicfDownloadAutoTftpAdminStatus,
       "hpicfDownloadTftpClientConfig": hpicfDownloadTftpClientConfig,
       "hpicfDownloadTftpClientBlkSize": hpicfDownloadTftpClientBlkSize}
)
