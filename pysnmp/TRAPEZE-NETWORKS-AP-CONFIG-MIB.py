# SNMP MIB module (TRAPEZE-NETWORKS-AP-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRAPEZE-NETWORKS-AP-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:25 2024
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

(TrpzApAttachType,
 TrpzApBias,
 TrpzApFingerprint,
 TrpzApLedMode,
 TrpzApNum,
 TrpzApPowerMode,
 TrpzApRadioIndex,
 TrpzApSerialNum,
 TrpzChannelNum,
 TrpzPowerLevel,
 TrpzRadioAntennaLocation,
 TrpzRadioChannelWidth,
 TrpzRadioMode,
 TrpzRadioType) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-AP-TC",
    "TrpzApAttachType",
    "TrpzApBias",
    "TrpzApFingerprint",
    "TrpzApLedMode",
    "TrpzApNum",
    "TrpzApPowerMode",
    "TrpzApRadioIndex",
    "TrpzApSerialNum",
    "TrpzChannelNum",
    "TrpzPowerLevel",
    "TrpzRadioAntennaLocation",
    "TrpzRadioChannelWidth",
    "TrpzRadioMode",
    "TrpzRadioType")

(TrpzPhysPortNumberOrZero,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-BASIC-TC",
    "TrpzPhysPortNumberOrZero")

(TrpzSyslogSeverity,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-EXTERNAL-SERVER-TC",
    "TrpzSyslogSeverity")

(trpzMibs,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-ROOT-MIB",
    "trpzMibs")


# MODULE-IDENTITY

trpzApConfigMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14)
)
trpzApConfigMib.setRevisions(
        ("2013-06-21 03:24",
         "2012-12-21 03:23",
         "2012-10-16 03:22",
         "2012-08-06 03:13",
         "2012-08-05 03:02",
         "2012-03-08 03:01",
         "2011-02-03 02:00",
         "2010-03-05 01:21",
         "2009-11-19 01:08")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TrpzApTemplateName(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TrpzRadioProfileName(OctetString, TextualConvention):
    status = "deprecated"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class TrpzServiceProfileName(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TrpzSnoopFilterName(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )



class TrpzServiceProfileSsidType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("crypto", 2))
    )



class TrpzServiceProfile11nMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("required", 3))
    )



class TrpzServiceProfile11nFrameAggregationType(Integer32, TextualConvention):
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
        *(("all", 3),
          ("disable", 4),
          ("mpdu", 2),
          ("msdu", 1))
    )



class TrpzServiceProfile11nMsduMaxLength(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("msdu-4k", 1),
          ("msdu-8k", 2))
    )



class TrpzServiceProfile11nMpduMaxLength(Integer32, TextualConvention):
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
        *(("mpdu-16k", 2),
          ("mpdu-32k", 3),
          ("mpdu-64k", 4),
          ("mpdu-8k", 1))
    )



class TrpzServiceProfileAuthFallthruType(Integer32, TextualConvention):
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
        *(("last-resort", 4),
          ("none", 1),
          ("web-aaa-portal", 3),
          ("web-auth", 2))
    )



class TrpzServiceProfileCacMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("session", 2),
          ("vendor", 3))
    )



class TrpzRadioProfileCountermeasuresMode(Integer32, TextualConvention):
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
        *(("all", 2),
          ("configured", 4),
          ("none", 1),
          ("rogue", 3))
    )



class TrpzRadioProfileRFScanChannelScope(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("operating", 1),
          ("regulatory", 2))
    )



class TrpzRadioProfileAutoTuneChannelRange(Integer32, TextualConvention):
    status = "obsolete"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all-bands", 1),
          ("lower-bands", 2))
    )



class TrpzRadioProfileRFScanMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )



class TrpzApLldpMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("tx", 2))
    )



class TrpzRadioProfileRFSpectralScanPriority(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data-first", 1),
          ("scan-first", 2))
    )



class TrpzBackupSsidMode(Integer32, TextualConvention):
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
        *(("always-on", 4),
          ("disabled", 1),
          ("dual", 3),
          ("outage-only", 2))
    )



class TrpzSnoopObserverTxMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("batched-tzsp", 2),
          ("tzsp", 1))
    )



class TrpzRadioProfileName32(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TrpzApRadiusNasIdType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ap-name", 1),
          ("ap-serial-id", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TrpzApConfigMibObjects_ObjectIdentity = ObjectIdentity
trpzApConfigMibObjects = _TrpzApConfigMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1)
)
_TrpzApConfApConfigTable_Object = MibTable
trpzApConfApConfigTable = _TrpzApConfApConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2)
)
if mibBuilder.loadTexts:
    trpzApConfApConfigTable.setStatus("current")
_TrpzApConfApConfigEntry_Object = MibTableRow
trpzApConfApConfigEntry = _TrpzApConfApConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1)
)
trpzApConfApConfigEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigApNum"),
)
if mibBuilder.loadTexts:
    trpzApConfApConfigEntry.setStatus("current")
_TrpzApConfApConfigApNum_Type = TrpzApNum
_TrpzApConfApConfigApNum_Object = MibTableColumn
trpzApConfApConfigApNum = _TrpzApConfApConfigApNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 1),
    _TrpzApConfApConfigApNum_Type()
)
trpzApConfApConfigApNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApConfApConfigApNum.setStatus("current")
_TrpzApConfApConfigApAttachType_Type = TrpzApAttachType
_TrpzApConfApConfigApAttachType_Object = MibTableColumn
trpzApConfApConfigApAttachType = _TrpzApConfApConfigApAttachType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 2),
    _TrpzApConfApConfigApAttachType_Type()
)
trpzApConfApConfigApAttachType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigApAttachType.setStatus("current")
_TrpzApConfApConfigPhysPortNum_Type = TrpzPhysPortNumberOrZero
_TrpzApConfApConfigPhysPortNum_Object = MibTableColumn
trpzApConfApConfigPhysPortNum = _TrpzApConfApConfigPhysPortNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 3),
    _TrpzApConfApConfigPhysPortNum_Type()
)
trpzApConfApConfigPhysPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigPhysPortNum.setStatus("current")
_TrpzApConfApConfigApSerialNum_Type = TrpzApSerialNum
_TrpzApConfApConfigApSerialNum_Object = MibTableColumn
trpzApConfApConfigApSerialNum = _TrpzApConfApConfigApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 4),
    _TrpzApConfApConfigApSerialNum_Type()
)
trpzApConfApConfigApSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigApSerialNum.setStatus("current")


class _TrpzApConfApConfigApModelName_Type(DisplayString):
    """Custom type trpzApConfApConfigApModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_TrpzApConfApConfigApModelName_Type.__name__ = "DisplayString"
_TrpzApConfApConfigApModelName_Object = MibTableColumn
trpzApConfApConfigApModelName = _TrpzApConfApConfigApModelName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 5),
    _TrpzApConfApConfigApModelName_Type()
)
trpzApConfApConfigApModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigApModelName.setStatus("current")
_TrpzApConfApConfigFingerprint_Type = TrpzApFingerprint
_TrpzApConfApConfigFingerprint_Object = MibTableColumn
trpzApConfApConfigFingerprint = _TrpzApConfApConfigFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 6),
    _TrpzApConfApConfigFingerprint_Type()
)
trpzApConfApConfigFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigFingerprint.setStatus("current")
_TrpzApConfApConfigBias_Type = TrpzApBias
_TrpzApConfApConfigBias_Object = MibTableColumn
trpzApConfApConfigBias = _TrpzApConfApConfigBias_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 7),
    _TrpzApConfApConfigBias_Type()
)
trpzApConfApConfigBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigBias.setStatus("current")
_TrpzApConfApConfigApTimeout_Type = Unsigned32
_TrpzApConfApConfigApTimeout_Object = MibTableColumn
trpzApConfApConfigApTimeout = _TrpzApConfApConfigApTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 8),
    _TrpzApConfApConfigApTimeout_Type()
)
trpzApConfApConfigApTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigApTimeout.setStatus("current")


class _TrpzApConfApConfigApName_Type(DisplayString):
    """Custom type trpzApConfApConfigApName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TrpzApConfApConfigApName_Type.__name__ = "DisplayString"
_TrpzApConfApConfigApName_Object = MibTableColumn
trpzApConfApConfigApName = _TrpzApConfApConfigApName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 9),
    _TrpzApConfApConfigApName_Type()
)
trpzApConfApConfigApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigApName.setStatus("deprecated")


class _TrpzApConfApConfigContact_Type(DisplayString):
    """Custom type trpzApConfApConfigContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrpzApConfApConfigContact_Type.__name__ = "DisplayString"
_TrpzApConfApConfigContact_Object = MibTableColumn
trpzApConfApConfigContact = _TrpzApConfApConfigContact_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 10),
    _TrpzApConfApConfigContact_Type()
)
trpzApConfApConfigContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigContact.setStatus("current")


class _TrpzApConfApConfigLocation_Type(DisplayString):
    """Custom type trpzApConfApConfigLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrpzApConfApConfigLocation_Type.__name__ = "DisplayString"
_TrpzApConfApConfigLocation_Object = MibTableColumn
trpzApConfApConfigLocation = _TrpzApConfApConfigLocation_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 11),
    _TrpzApConfApConfigLocation_Type()
)
trpzApConfApConfigLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigLocation.setStatus("current")
_TrpzApConfApConfigBlinkEnabled_Type = TruthValue
_TrpzApConfApConfigBlinkEnabled_Object = MibTableColumn
trpzApConfApConfigBlinkEnabled = _TrpzApConfApConfigBlinkEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 12),
    _TrpzApConfApConfigBlinkEnabled_Type()
)
trpzApConfApConfigBlinkEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigBlinkEnabled.setStatus("current")
_TrpzApConfApConfigForceImageDownloadEnabled_Type = TruthValue
_TrpzApConfApConfigForceImageDownloadEnabled_Object = MibTableColumn
trpzApConfApConfigForceImageDownloadEnabled = _TrpzApConfApConfigForceImageDownloadEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 13),
    _TrpzApConfApConfigForceImageDownloadEnabled_Type()
)
trpzApConfApConfigForceImageDownloadEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigForceImageDownloadEnabled.setStatus("current")
_TrpzApConfApConfigFirmwareUpgradeEnabled_Type = TruthValue
_TrpzApConfApConfigFirmwareUpgradeEnabled_Object = MibTableColumn
trpzApConfApConfigFirmwareUpgradeEnabled = _TrpzApConfApConfigFirmwareUpgradeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 14),
    _TrpzApConfApConfigFirmwareUpgradeEnabled_Type()
)
trpzApConfApConfigFirmwareUpgradeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigFirmwareUpgradeEnabled.setStatus("current")
_TrpzApConfApConfigLocalSwitchingEnabled_Type = TruthValue
_TrpzApConfApConfigLocalSwitchingEnabled_Object = MibTableColumn
trpzApConfApConfigLocalSwitchingEnabled = _TrpzApConfApConfigLocalSwitchingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 15),
    _TrpzApConfApConfigLocalSwitchingEnabled_Type()
)
trpzApConfApConfigLocalSwitchingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigLocalSwitchingEnabled.setStatus("current")
_TrpzApConfApConfigPowerMode_Type = TrpzApPowerMode
_TrpzApConfApConfigPowerMode_Object = MibTableColumn
trpzApConfApConfigPowerMode = _TrpzApConfApConfigPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 16),
    _TrpzApConfApConfigPowerMode_Type()
)
trpzApConfApConfigPowerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigPowerMode.setStatus("current")
_TrpzApConfApConfigLedMode_Type = TrpzApLedMode
_TrpzApConfApConfigLedMode_Object = MibTableColumn
trpzApConfApConfigLedMode = _TrpzApConfApConfigLedMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 17),
    _TrpzApConfApConfigLedMode_Type()
)
trpzApConfApConfigLedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigLedMode.setStatus("current")


class _TrpzApConfApConfigDescription_Type(DisplayString):
    """Custom type trpzApConfApConfigDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TrpzApConfApConfigDescription_Type.__name__ = "DisplayString"
_TrpzApConfApConfigDescription_Object = MibTableColumn
trpzApConfApConfigDescription = _TrpzApConfApConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 18),
    _TrpzApConfApConfigDescription_Type()
)
trpzApConfApConfigDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigDescription.setStatus("current")
_TrpzApConfApConfigLldpMode_Type = TrpzApLldpMode
_TrpzApConfApConfigLldpMode_Object = MibTableColumn
trpzApConfApConfigLldpMode = _TrpzApConfApConfigLldpMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 19),
    _TrpzApConfApConfigLldpMode_Type()
)
trpzApConfApConfigLldpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigLldpMode.setStatus("current")
_TrpzApConfApConfigLldpMedEnabled_Type = TruthValue
_TrpzApConfApConfigLldpMedEnabled_Object = MibTableColumn
trpzApConfApConfigLldpMedEnabled = _TrpzApConfApConfigLldpMedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 20),
    _TrpzApConfApConfigLldpMedEnabled_Type()
)
trpzApConfApConfigLldpMedEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigLldpMedEnabled.setStatus("current")
_TrpzApConfApConfigLldpMedExtPowerViaMdiTlvSelected_Type = TruthValue
_TrpzApConfApConfigLldpMedExtPowerViaMdiTlvSelected_Object = MibTableColumn
trpzApConfApConfigLldpMedExtPowerViaMdiTlvSelected = _TrpzApConfApConfigLldpMedExtPowerViaMdiTlvSelected_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 21),
    _TrpzApConfApConfigLldpMedExtPowerViaMdiTlvSelected_Type()
)
trpzApConfApConfigLldpMedExtPowerViaMdiTlvSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigLldpMedExtPowerViaMdiTlvSelected.setStatus("current")
_TrpzApConfApConfigLldpMedInventoryTlvSelected_Type = TruthValue
_TrpzApConfApConfigLldpMedInventoryTlvSelected_Object = MibTableColumn
trpzApConfApConfigLldpMedInventoryTlvSelected = _TrpzApConfApConfigLldpMedInventoryTlvSelected_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 22),
    _TrpzApConfApConfigLldpMedInventoryTlvSelected_Type()
)
trpzApConfApConfigLldpMedInventoryTlvSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigLldpMedInventoryTlvSelected.setStatus("current")
_TrpzApConfApConfigApTunnelEnabled_Type = TruthValue
_TrpzApConfApConfigApTunnelEnabled_Object = MibTableColumn
trpzApConfApConfigApTunnelEnabled = _TrpzApConfApConfigApTunnelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 23),
    _TrpzApConfApConfigApTunnelEnabled_Type()
)
trpzApConfApConfigApTunnelEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigApTunnelEnabled.setStatus("current")
_TrpzApConfApConfigDataSecurityEnabled_Type = TruthValue
_TrpzApConfApConfigDataSecurityEnabled_Object = MibTableColumn
trpzApConfApConfigDataSecurityEnabled = _TrpzApConfApConfigDataSecurityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 24),
    _TrpzApConfApConfigDataSecurityEnabled_Type()
)
trpzApConfApConfigDataSecurityEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigDataSecurityEnabled.setStatus("current")
_TrpzApConfApConfigWanOutageModeEnabled_Type = TruthValue
_TrpzApConfApConfigWanOutageModeEnabled_Object = MibTableColumn
trpzApConfApConfigWanOutageModeEnabled = _TrpzApConfApConfigWanOutageModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 25),
    _TrpzApConfApConfigWanOutageModeEnabled_Type()
)
trpzApConfApConfigWanOutageModeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigWanOutageModeEnabled.setStatus("current")
_TrpzApConfApConfigWanOutageExtendedTimeout_Type = Unsigned32
_TrpzApConfApConfigWanOutageExtendedTimeout_Object = MibTableColumn
trpzApConfApConfigWanOutageExtendedTimeout = _TrpzApConfApConfigWanOutageExtendedTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 26),
    _TrpzApConfApConfigWanOutageExtendedTimeout_Type()
)
trpzApConfApConfigWanOutageExtendedTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigWanOutageExtendedTimeout.setStatus("current")
_TrpzApConfApConfigWanOutageEvaluationPeriod_Type = Unsigned32
_TrpzApConfApConfigWanOutageEvaluationPeriod_Object = MibTableColumn
trpzApConfApConfigWanOutageEvaluationPeriod = _TrpzApConfApConfigWanOutageEvaluationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 27),
    _TrpzApConfApConfigWanOutageEvaluationPeriod_Type()
)
trpzApConfApConfigWanOutageEvaluationPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigWanOutageEvaluationPeriod.setStatus("current")


class _TrpzApConfApConfigRemoteSiteName_Type(DisplayString):
    """Custom type trpzApConfApConfigRemoteSiteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrpzApConfApConfigRemoteSiteName_Type.__name__ = "DisplayString"
_TrpzApConfApConfigRemoteSiteName_Object = MibTableColumn
trpzApConfApConfigRemoteSiteName = _TrpzApConfApConfigRemoteSiteName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 28),
    _TrpzApConfApConfigRemoteSiteName_Type()
)
trpzApConfApConfigRemoteSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigRemoteSiteName.setStatus("current")
_TrpzApConfApConfigPathMtu_Type = Unsigned32
_TrpzApConfApConfigPathMtu_Object = MibTableColumn
trpzApConfApConfigPathMtu = _TrpzApConfApConfigPathMtu_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 29),
    _TrpzApConfApConfigPathMtu_Type()
)
trpzApConfApConfigPathMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigPathMtu.setStatus("current")
if mibBuilder.loadTexts:
    trpzApConfApConfigPathMtu.setUnits("bytes")
_TrpzApConfApConfigHighLatencyModeEnabled_Type = TruthValue
_TrpzApConfApConfigHighLatencyModeEnabled_Object = MibTableColumn
trpzApConfApConfigHighLatencyModeEnabled = _TrpzApConfApConfigHighLatencyModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 30),
    _TrpzApConfApConfigHighLatencyModeEnabled_Type()
)
trpzApConfApConfigHighLatencyModeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigHighLatencyModeEnabled.setStatus("current")
_TrpzApConfApConfigApName2_Type = DisplayString
_TrpzApConfApConfigApName2_Object = MibTableColumn
trpzApConfApConfigApName2 = _TrpzApConfApConfigApName2_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 31),
    _TrpzApConfApConfigApName2_Type()
)
trpzApConfApConfigApName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigApName2.setStatus("current")
_TrpzApConfApConfigCacheConfigEnabled_Type = TruthValue
_TrpzApConfApConfigCacheConfigEnabled_Object = MibTableColumn
trpzApConfApConfigCacheConfigEnabled = _TrpzApConfApConfigCacheConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 2, 1, 32),
    _TrpzApConfApConfigCacheConfigEnabled_Type()
)
trpzApConfApConfigCacheConfigEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApConfigCacheConfigEnabled.setStatus("current")
_TrpzApConfRadioConfigTable_Object = MibTable
trpzApConfRadioConfigTable = _TrpzApConfRadioConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 3)
)
if mibBuilder.loadTexts:
    trpzApConfRadioConfigTable.setStatus("current")
_TrpzApConfRadioConfigEntry_Object = MibTableRow
trpzApConfRadioConfigEntry = _TrpzApConfRadioConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 3, 1)
)
trpzApConfRadioConfigEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigApNum"),
    (0, "TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigRadioIndex"),
)
if mibBuilder.loadTexts:
    trpzApConfRadioConfigEntry.setStatus("current")
_TrpzApConfRadioConfigApNum_Type = TrpzApNum
_TrpzApConfRadioConfigApNum_Object = MibTableColumn
trpzApConfRadioConfigApNum = _TrpzApConfRadioConfigApNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 3, 1, 1),
    _TrpzApConfRadioConfigApNum_Type()
)
trpzApConfRadioConfigApNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApConfRadioConfigApNum.setStatus("current")
_TrpzApConfRadioConfigRadioIndex_Type = TrpzApRadioIndex
_TrpzApConfRadioConfigRadioIndex_Object = MibTableColumn
trpzApConfRadioConfigRadioIndex = _TrpzApConfRadioConfigRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 3, 1, 2),
    _TrpzApConfRadioConfigRadioIndex_Type()
)
trpzApConfRadioConfigRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApConfRadioConfigRadioIndex.setStatus("current")
_TrpzApConfRadioConfigRadioType_Type = TrpzRadioType
_TrpzApConfRadioConfigRadioType_Object = MibTableColumn
trpzApConfRadioConfigRadioType = _TrpzApConfRadioConfigRadioType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 3, 1, 3),
    _TrpzApConfRadioConfigRadioType_Type()
)
trpzApConfRadioConfigRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioConfigRadioType.setStatus("current")
_TrpzApConfRadioConfigRadioMode_Type = TrpzRadioMode
_TrpzApConfRadioConfigRadioMode_Object = MibTableColumn
trpzApConfRadioConfigRadioMode = _TrpzApConfRadioConfigRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 3, 1, 4),
    _TrpzApConfRadioConfigRadioMode_Type()
)
trpzApConfRadioConfigRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioConfigRadioMode.setStatus("current")
_TrpzApConfRadioConfigRadioProfileName_Type = TrpzRadioProfileName
_TrpzApConfRadioConfigRadioProfileName_Object = MibTableColumn
trpzApConfRadioConfigRadioProfileName = _TrpzApConfRadioConfigRadioProfileName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 3, 1, 5),
    _TrpzApConfRadioConfigRadioProfileName_Type()
)
trpzApConfRadioConfigRadioProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioConfigRadioProfileName.setStatus("deprecated")
_TrpzApConfRadioConfigChannel_Type = TrpzChannelNum
_TrpzApConfRadioConfigChannel_Object = MibTableColumn
trpzApConfRadioConfigChannel = _TrpzApConfRadioConfigChannel_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 3, 1, 6),
    _TrpzApConfRadioConfigChannel_Type()
)
trpzApConfRadioConfigChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioConfigChannel.setStatus("current")
_TrpzApConfRadioConfigTxPower_Type = TrpzPowerLevel
_TrpzApConfRadioConfigTxPower_Object = MibTableColumn
trpzApConfRadioConfigTxPower = _TrpzApConfRadioConfigTxPower_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 3, 1, 7),
    _TrpzApConfRadioConfigTxPower_Type()
)
trpzApConfRadioConfigTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioConfigTxPower.setStatus("current")
_TrpzApConfRadioConfigAutoTuneMaxTxPower_Type = TrpzPowerLevel
_TrpzApConfRadioConfigAutoTuneMaxTxPower_Object = MibTableColumn
trpzApConfRadioConfigAutoTuneMaxTxPower = _TrpzApConfRadioConfigAutoTuneMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 3, 1, 8),
    _TrpzApConfRadioConfigAutoTuneMaxTxPower_Type()
)
trpzApConfRadioConfigAutoTuneMaxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioConfigAutoTuneMaxTxPower.setStatus("obsolete")


class _TrpzApConfRadioConfigAntennaType_Type(DisplayString):
    """Custom type trpzApConfRadioConfigAntennaType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TrpzApConfRadioConfigAntennaType_Type.__name__ = "DisplayString"
_TrpzApConfRadioConfigAntennaType_Object = MibTableColumn
trpzApConfRadioConfigAntennaType = _TrpzApConfRadioConfigAntennaType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 3, 1, 9),
    _TrpzApConfRadioConfigAntennaType_Type()
)
trpzApConfRadioConfigAntennaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioConfigAntennaType.setStatus("current")
_TrpzApConfRadioConfigAntennaLocation_Type = TrpzRadioAntennaLocation
_TrpzApConfRadioConfigAntennaLocation_Object = MibTableColumn
trpzApConfRadioConfigAntennaLocation = _TrpzApConfRadioConfigAntennaLocation_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 3, 1, 10),
    _TrpzApConfRadioConfigAntennaLocation_Type()
)
trpzApConfRadioConfigAntennaLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioConfigAntennaLocation.setStatus("current")
_TrpzApConfRadioConfigLoadBalancingEnabled_Type = TruthValue
_TrpzApConfRadioConfigLoadBalancingEnabled_Object = MibTableColumn
trpzApConfRadioConfigLoadBalancingEnabled = _TrpzApConfRadioConfigLoadBalancingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 3, 1, 11),
    _TrpzApConfRadioConfigLoadBalancingEnabled_Type()
)
trpzApConfRadioConfigLoadBalancingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioConfigLoadBalancingEnabled.setStatus("current")


class _TrpzApConfRadioConfigLoadBalancingGroup_Type(DisplayString):
    """Custom type trpzApConfRadioConfigLoadBalancingGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrpzApConfRadioConfigLoadBalancingGroup_Type.__name__ = "DisplayString"
_TrpzApConfRadioConfigLoadBalancingGroup_Object = MibTableColumn
trpzApConfRadioConfigLoadBalancingGroup = _TrpzApConfRadioConfigLoadBalancingGroup_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 3, 1, 12),
    _TrpzApConfRadioConfigLoadBalancingGroup_Type()
)
trpzApConfRadioConfigLoadBalancingGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioConfigLoadBalancingGroup.setStatus("current")
_TrpzApConfRadioConfigLoadRebalancingEnabled_Type = TruthValue
_TrpzApConfRadioConfigLoadRebalancingEnabled_Object = MibTableColumn
trpzApConfRadioConfigLoadRebalancingEnabled = _TrpzApConfRadioConfigLoadRebalancingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 3, 1, 13),
    _TrpzApConfRadioConfigLoadRebalancingEnabled_Type()
)
trpzApConfRadioConfigLoadRebalancingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioConfigLoadRebalancingEnabled.setStatus("current")
_TrpzApConfRadioConfigRadioProfileName2_Type = DisplayString
_TrpzApConfRadioConfigRadioProfileName2_Object = MibTableColumn
trpzApConfRadioConfigRadioProfileName2 = _TrpzApConfRadioConfigRadioProfileName2_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 3, 1, 14),
    _TrpzApConfRadioConfigRadioProfileName2_Type()
)
trpzApConfRadioConfigRadioProfileName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioConfigRadioProfileName2.setStatus("current")
_TrpzApConfApTemplateConfigTable_Object = MibTable
trpzApConfApTemplateConfigTable = _TrpzApConfApTemplateConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 4)
)
if mibBuilder.loadTexts:
    trpzApConfApTemplateConfigTable.setStatus("current")
_TrpzApConfApTemplateConfigEntry_Object = MibTableRow
trpzApConfApTemplateConfigEntry = _TrpzApConfApTemplateConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 4, 1)
)
trpzApConfApTemplateConfigEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApTemplConfApTemplateName"),
)
if mibBuilder.loadTexts:
    trpzApConfApTemplateConfigEntry.setStatus("current")
_TrpzApConfApTemplConfApTemplateName_Type = TrpzApTemplateName
_TrpzApConfApTemplConfApTemplateName_Object = MibTableColumn
trpzApConfApTemplConfApTemplateName = _TrpzApConfApTemplConfApTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 4, 1, 1),
    _TrpzApConfApTemplConfApTemplateName_Type()
)
trpzApConfApTemplConfApTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApConfApTemplConfApTemplateName.setStatus("current")
_TrpzApConfApTemplConfApTemplateEnabled_Type = TruthValue
_TrpzApConfApTemplConfApTemplateEnabled_Object = MibTableColumn
trpzApConfApTemplConfApTemplateEnabled = _TrpzApConfApTemplConfApTemplateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 4, 1, 2),
    _TrpzApConfApTemplConfApTemplateEnabled_Type()
)
trpzApConfApTemplConfApTemplateEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApTemplConfApTemplateEnabled.setStatus("current")
_TrpzApConfApTemplConfBias_Type = TrpzApBias
_TrpzApConfApTemplConfBias_Object = MibTableColumn
trpzApConfApTemplConfBias = _TrpzApConfApTemplConfBias_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 4, 1, 3),
    _TrpzApConfApTemplConfBias_Type()
)
trpzApConfApTemplConfBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApTemplConfBias.setStatus("current")
_TrpzApConfApTemplConfApTimeout_Type = Unsigned32
_TrpzApConfApTemplConfApTimeout_Object = MibTableColumn
trpzApConfApTemplConfApTimeout = _TrpzApConfApTemplConfApTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 4, 1, 4),
    _TrpzApConfApTemplConfApTimeout_Type()
)
trpzApConfApTemplConfApTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApTemplConfApTimeout.setStatus("current")
_TrpzApConfApTemplConfBlinkEnabled_Type = TruthValue
_TrpzApConfApTemplConfBlinkEnabled_Object = MibTableColumn
trpzApConfApTemplConfBlinkEnabled = _TrpzApConfApTemplConfBlinkEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 4, 1, 5),
    _TrpzApConfApTemplConfBlinkEnabled_Type()
)
trpzApConfApTemplConfBlinkEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApTemplConfBlinkEnabled.setStatus("current")
_TrpzApConfApTemplConfForceImageDownloadEnabled_Type = TruthValue
_TrpzApConfApTemplConfForceImageDownloadEnabled_Object = MibTableColumn
trpzApConfApTemplConfForceImageDownloadEnabled = _TrpzApConfApTemplConfForceImageDownloadEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 4, 1, 6),
    _TrpzApConfApTemplConfForceImageDownloadEnabled_Type()
)
trpzApConfApTemplConfForceImageDownloadEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApTemplConfForceImageDownloadEnabled.setStatus("current")
_TrpzApConfApTemplConfFirmwareUpgradeEnabled_Type = TruthValue
_TrpzApConfApTemplConfFirmwareUpgradeEnabled_Object = MibTableColumn
trpzApConfApTemplConfFirmwareUpgradeEnabled = _TrpzApConfApTemplConfFirmwareUpgradeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 4, 1, 7),
    _TrpzApConfApTemplConfFirmwareUpgradeEnabled_Type()
)
trpzApConfApTemplConfFirmwareUpgradeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApTemplConfFirmwareUpgradeEnabled.setStatus("current")
_TrpzApConfApTemplConfLocalSwitchingEnabled_Type = TruthValue
_TrpzApConfApTemplConfLocalSwitchingEnabled_Object = MibTableColumn
trpzApConfApTemplConfLocalSwitchingEnabled = _TrpzApConfApTemplConfLocalSwitchingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 4, 1, 8),
    _TrpzApConfApTemplConfLocalSwitchingEnabled_Type()
)
trpzApConfApTemplConfLocalSwitchingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApTemplConfLocalSwitchingEnabled.setStatus("current")
_TrpzApConfApTemplConfPowerMode_Type = TrpzApPowerMode
_TrpzApConfApTemplConfPowerMode_Object = MibTableColumn
trpzApConfApTemplConfPowerMode = _TrpzApConfApTemplConfPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 4, 1, 9),
    _TrpzApConfApTemplConfPowerMode_Type()
)
trpzApConfApTemplConfPowerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApTemplConfPowerMode.setStatus("current")
_TrpzApConfApTemplConfLedMode_Type = TrpzApLedMode
_TrpzApConfApTemplConfLedMode_Object = MibTableColumn
trpzApConfApTemplConfLedMode = _TrpzApConfApTemplConfLedMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 4, 1, 10),
    _TrpzApConfApTemplConfLedMode_Type()
)
trpzApConfApTemplConfLedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApTemplConfLedMode.setStatus("current")
_TrpzApConfApTemplateRadioConfigTable_Object = MibTable
trpzApConfApTemplateRadioConfigTable = _TrpzApConfApTemplateRadioConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 5)
)
if mibBuilder.loadTexts:
    trpzApConfApTemplateRadioConfigTable.setStatus("current")
_TrpzApConfApTemplateRadioConfigEntry_Object = MibTableRow
trpzApConfApTemplateRadioConfigEntry = _TrpzApConfApTemplateRadioConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 5, 1)
)
trpzApConfApTemplateRadioConfigEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApTemRadioConfApTemplateName"),
    (0, "TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApTemRadioConfRadioIndex"),
)
if mibBuilder.loadTexts:
    trpzApConfApTemplateRadioConfigEntry.setStatus("current")
_TrpzApConfApTemRadioConfApTemplateName_Type = TrpzApTemplateName
_TrpzApConfApTemRadioConfApTemplateName_Object = MibTableColumn
trpzApConfApTemRadioConfApTemplateName = _TrpzApConfApTemRadioConfApTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 5, 1, 1),
    _TrpzApConfApTemRadioConfApTemplateName_Type()
)
trpzApConfApTemRadioConfApTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApConfApTemRadioConfApTemplateName.setStatus("current")
_TrpzApConfApTemRadioConfRadioIndex_Type = TrpzApRadioIndex
_TrpzApConfApTemRadioConfRadioIndex_Object = MibTableColumn
trpzApConfApTemRadioConfRadioIndex = _TrpzApConfApTemRadioConfRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 5, 1, 2),
    _TrpzApConfApTemRadioConfRadioIndex_Type()
)
trpzApConfApTemRadioConfRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApConfApTemRadioConfRadioIndex.setStatus("current")
_TrpzApConfApTemRadioConfRadioMode_Type = TrpzRadioMode
_TrpzApConfApTemRadioConfRadioMode_Object = MibTableColumn
trpzApConfApTemRadioConfRadioMode = _TrpzApConfApTemRadioConfRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 5, 1, 3),
    _TrpzApConfApTemRadioConfRadioMode_Type()
)
trpzApConfApTemRadioConfRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApTemRadioConfRadioMode.setStatus("current")
_TrpzApConfApTemRadioConfRadioProfileName_Type = TrpzRadioProfileName
_TrpzApConfApTemRadioConfRadioProfileName_Object = MibTableColumn
trpzApConfApTemRadioConfRadioProfileName = _TrpzApConfApTemRadioConfRadioProfileName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 5, 1, 4),
    _TrpzApConfApTemRadioConfRadioProfileName_Type()
)
trpzApConfApTemRadioConfRadioProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApTemRadioConfRadioProfileName.setStatus("deprecated")
_TrpzApConfApTemRadioConfAutoTuneMaxTxPower_Type = TrpzPowerLevel
_TrpzApConfApTemRadioConfAutoTuneMaxTxPower_Object = MibTableColumn
trpzApConfApTemRadioConfAutoTuneMaxTxPower = _TrpzApConfApTemRadioConfAutoTuneMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 5, 1, 5),
    _TrpzApConfApTemRadioConfAutoTuneMaxTxPower_Type()
)
trpzApConfApTemRadioConfAutoTuneMaxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApTemRadioConfAutoTuneMaxTxPower.setStatus("obsolete")
_TrpzApConfApTemRadioConfLoadBalancingEnabled_Type = TruthValue
_TrpzApConfApTemRadioConfLoadBalancingEnabled_Object = MibTableColumn
trpzApConfApTemRadioConfLoadBalancingEnabled = _TrpzApConfApTemRadioConfLoadBalancingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 5, 1, 6),
    _TrpzApConfApTemRadioConfLoadBalancingEnabled_Type()
)
trpzApConfApTemRadioConfLoadBalancingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApTemRadioConfLoadBalancingEnabled.setStatus("current")


class _TrpzApConfApTemRadioConfLoadBalancingGroup_Type(DisplayString):
    """Custom type trpzApConfApTemRadioConfLoadBalancingGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrpzApConfApTemRadioConfLoadBalancingGroup_Type.__name__ = "DisplayString"
_TrpzApConfApTemRadioConfLoadBalancingGroup_Object = MibTableColumn
trpzApConfApTemRadioConfLoadBalancingGroup = _TrpzApConfApTemRadioConfLoadBalancingGroup_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 5, 1, 7),
    _TrpzApConfApTemRadioConfLoadBalancingGroup_Type()
)
trpzApConfApTemRadioConfLoadBalancingGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApTemRadioConfLoadBalancingGroup.setStatus("current")
_TrpzApConfApTemRadioConfLoadRebalancingEnabled_Type = TruthValue
_TrpzApConfApTemRadioConfLoadRebalancingEnabled_Object = MibTableColumn
trpzApConfApTemRadioConfLoadRebalancingEnabled = _TrpzApConfApTemRadioConfLoadRebalancingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 5, 1, 8),
    _TrpzApConfApTemRadioConfLoadRebalancingEnabled_Type()
)
trpzApConfApTemRadioConfLoadRebalancingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApTemRadioConfLoadRebalancingEnabled.setStatus("current")
_TrpzApConfApTemRadioConfRadioProfileName2_Type = DisplayString
_TrpzApConfApTemRadioConfRadioProfileName2_Object = MibTableColumn
trpzApConfApTemRadioConfRadioProfileName2 = _TrpzApConfApTemRadioConfRadioProfileName2_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 5, 1, 9),
    _TrpzApConfApTemRadioConfRadioProfileName2_Type()
)
trpzApConfApTemRadioConfRadioProfileName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfApTemRadioConfRadioProfileName2.setStatus("current")
_TrpzApConfRadioProfileTable_Object = MibTable
trpzApConfRadioProfileTable = _TrpzApConfRadioProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6)
)
if mibBuilder.loadTexts:
    trpzApConfRadioProfileTable.setStatus("deprecated")
_TrpzApConfRadioProfileEntry_Object = MibTableRow
trpzApConfRadioProfileEntry = _TrpzApConfRadioProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1)
)
trpzApConfRadioProfileEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfRadioProfileName"),
)
if mibBuilder.loadTexts:
    trpzApConfRadioProfileEntry.setStatus("deprecated")
_TrpzApConfRadioProfRadioProfileName_Type = TrpzRadioProfileName
_TrpzApConfRadioProfRadioProfileName_Object = MibTableColumn
trpzApConfRadioProfRadioProfileName = _TrpzApConfRadioProfRadioProfileName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 1),
    _TrpzApConfRadioProfRadioProfileName_Type()
)
trpzApConfRadioProfRadioProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApConfRadioProfRadioProfileName.setStatus("deprecated")
_TrpzApConfRadioProfBeaconInterval_Type = Unsigned32
_TrpzApConfRadioProfBeaconInterval_Object = MibTableColumn
trpzApConfRadioProfBeaconInterval = _TrpzApConfRadioProfBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 2),
    _TrpzApConfRadioProfBeaconInterval_Type()
)
trpzApConfRadioProfBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trpzApConfRadioProfBeaconInterval.setStatus("deprecated")
_TrpzApConfRadioProfDtimInterval_Type = Unsigned32
_TrpzApConfRadioProfDtimInterval_Object = MibTableColumn
trpzApConfRadioProfDtimInterval = _TrpzApConfRadioProfDtimInterval_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 3),
    _TrpzApConfRadioProfDtimInterval_Type()
)
trpzApConfRadioProfDtimInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfDtimInterval.setStatus("deprecated")
_TrpzApConfRadioProfChannelWidth11na_Type = TrpzRadioChannelWidth
_TrpzApConfRadioProfChannelWidth11na_Object = MibTableColumn
trpzApConfRadioProfChannelWidth11na = _TrpzApConfRadioProfChannelWidth11na_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 4),
    _TrpzApConfRadioProfChannelWidth11na_Type()
)
trpzApConfRadioProfChannelWidth11na.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfChannelWidth11na.setStatus("deprecated")
_TrpzApConfRadioProfMaxTxLifetime_Type = Unsigned32
_TrpzApConfRadioProfMaxTxLifetime_Object = MibTableColumn
trpzApConfRadioProfMaxTxLifetime = _TrpzApConfRadioProfMaxTxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 5),
    _TrpzApConfRadioProfMaxTxLifetime_Type()
)
trpzApConfRadioProfMaxTxLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfMaxTxLifetime.setStatus("deprecated")
_TrpzApConfRadioProfMaxRxLifetime_Type = Unsigned32
_TrpzApConfRadioProfMaxRxLifetime_Object = MibTableColumn
trpzApConfRadioProfMaxRxLifetime = _TrpzApConfRadioProfMaxRxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 6),
    _TrpzApConfRadioProfMaxRxLifetime_Type()
)
trpzApConfRadioProfMaxRxLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfMaxRxLifetime.setStatus("deprecated")
_TrpzApConfRadioProfRtsThreshold_Type = Unsigned32
_TrpzApConfRadioProfRtsThreshold_Object = MibTableColumn
trpzApConfRadioProfRtsThreshold = _TrpzApConfRadioProfRtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 7),
    _TrpzApConfRadioProfRtsThreshold_Type()
)
trpzApConfRadioProfRtsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trpzApConfRadioProfRtsThreshold.setStatus("deprecated")
_TrpzApConfRadioProfFragThreshold_Type = Unsigned32
_TrpzApConfRadioProfFragThreshold_Object = MibTableColumn
trpzApConfRadioProfFragThreshold = _TrpzApConfRadioProfFragThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 8),
    _TrpzApConfRadioProfFragThreshold_Type()
)
trpzApConfRadioProfFragThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trpzApConfRadioProfFragThreshold.setStatus("deprecated")
_TrpzApConfRadioProfLongXmitPreambleEnabled_Type = TruthValue
_TrpzApConfRadioProfLongXmitPreambleEnabled_Object = MibTableColumn
trpzApConfRadioProfLongXmitPreambleEnabled = _TrpzApConfRadioProfLongXmitPreambleEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 9),
    _TrpzApConfRadioProfLongXmitPreambleEnabled_Type()
)
trpzApConfRadioProfLongXmitPreambleEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfLongXmitPreambleEnabled.setStatus("deprecated")
_TrpzApConfRadioProfCountermeasuresMode_Type = TrpzRadioProfileCountermeasuresMode
_TrpzApConfRadioProfCountermeasuresMode_Object = MibTableColumn
trpzApConfRadioProfCountermeasuresMode = _TrpzApConfRadioProfCountermeasuresMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 10),
    _TrpzApConfRadioProfCountermeasuresMode_Type()
)
trpzApConfRadioProfCountermeasuresMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfCountermeasuresMode.setStatus("deprecated")
_TrpzApConfRadioProfRFScanMode_Type = TrpzRadioProfileRFScanMode
_TrpzApConfRadioProfRFScanMode_Object = MibTableColumn
trpzApConfRadioProfRFScanMode = _TrpzApConfRadioProfRFScanMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 11),
    _TrpzApConfRadioProfRFScanMode_Type()
)
trpzApConfRadioProfRFScanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfRFScanMode.setStatus("deprecated")
_TrpzApConfRadioProfRFScanChannelScope_Type = TrpzRadioProfileRFScanChannelScope
_TrpzApConfRadioProfRFScanChannelScope_Object = MibTableColumn
trpzApConfRadioProfRFScanChannelScope = _TrpzApConfRadioProfRFScanChannelScope_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 12),
    _TrpzApConfRadioProfRFScanChannelScope_Type()
)
trpzApConfRadioProfRFScanChannelScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfRFScanChannelScope.setStatus("deprecated")
_TrpzApConfRadioProfRFScanCTSEnabled_Type = TruthValue
_TrpzApConfRadioProfRFScanCTSEnabled_Object = MibTableColumn
trpzApConfRadioProfRFScanCTSEnabled = _TrpzApConfRadioProfRFScanCTSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 13),
    _TrpzApConfRadioProfRFScanCTSEnabled_Type()
)
trpzApConfRadioProfRFScanCTSEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfRFScanCTSEnabled.setStatus("deprecated")
_TrpzApConfRadioProfAutoTune11aChannelRange_Type = TrpzRadioProfileAutoTuneChannelRange
_TrpzApConfRadioProfAutoTune11aChannelRange_Object = MibTableColumn
trpzApConfRadioProfAutoTune11aChannelRange = _TrpzApConfRadioProfAutoTune11aChannelRange_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 14),
    _TrpzApConfRadioProfAutoTune11aChannelRange_Type()
)
trpzApConfRadioProfAutoTune11aChannelRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfAutoTune11aChannelRange.setStatus("obsolete")
_TrpzApConfRadioProfAutoTuneIgnoreClientsEnabled_Type = TruthValue
_TrpzApConfRadioProfAutoTuneIgnoreClientsEnabled_Object = MibTableColumn
trpzApConfRadioProfAutoTuneIgnoreClientsEnabled = _TrpzApConfRadioProfAutoTuneIgnoreClientsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 15),
    _TrpzApConfRadioProfAutoTuneIgnoreClientsEnabled_Type()
)
trpzApConfRadioProfAutoTuneIgnoreClientsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfAutoTuneIgnoreClientsEnabled.setStatus("obsolete")
_TrpzApConfRadioProfAutoTuneChannelEnabled_Type = TruthValue
_TrpzApConfRadioProfAutoTuneChannelEnabled_Object = MibTableColumn
trpzApConfRadioProfAutoTuneChannelEnabled = _TrpzApConfRadioProfAutoTuneChannelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 16),
    _TrpzApConfRadioProfAutoTuneChannelEnabled_Type()
)
trpzApConfRadioProfAutoTuneChannelEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfAutoTuneChannelEnabled.setStatus("obsolete")
_TrpzApConfRadioProfAutoTuneChannelHolddownInterval_Type = Unsigned32
_TrpzApConfRadioProfAutoTuneChannelHolddownInterval_Object = MibTableColumn
trpzApConfRadioProfAutoTuneChannelHolddownInterval = _TrpzApConfRadioProfAutoTuneChannelHolddownInterval_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 17),
    _TrpzApConfRadioProfAutoTuneChannelHolddownInterval_Type()
)
trpzApConfRadioProfAutoTuneChannelHolddownInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfAutoTuneChannelHolddownInterval.setStatus("obsolete")
_TrpzApConfRadioProfAutoTuneChannelChangeInterval_Type = Unsigned32
_TrpzApConfRadioProfAutoTuneChannelChangeInterval_Object = MibTableColumn
trpzApConfRadioProfAutoTuneChannelChangeInterval = _TrpzApConfRadioProfAutoTuneChannelChangeInterval_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 18),
    _TrpzApConfRadioProfAutoTuneChannelChangeInterval_Type()
)
trpzApConfRadioProfAutoTuneChannelChangeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfAutoTuneChannelChangeInterval.setStatus("obsolete")
_TrpzApConfRadioProfAutoTunePowerEnabled_Type = TruthValue
_TrpzApConfRadioProfAutoTunePowerEnabled_Object = MibTableColumn
trpzApConfRadioProfAutoTunePowerEnabled = _TrpzApConfRadioProfAutoTunePowerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 19),
    _TrpzApConfRadioProfAutoTunePowerEnabled_Type()
)
trpzApConfRadioProfAutoTunePowerEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfAutoTunePowerEnabled.setStatus("deprecated")
_TrpzApConfRadioProfAutoTunePowerRampInterval_Type = Unsigned32
_TrpzApConfRadioProfAutoTunePowerRampInterval_Object = MibTableColumn
trpzApConfRadioProfAutoTunePowerRampInterval = _TrpzApConfRadioProfAutoTunePowerRampInterval_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 20),
    _TrpzApConfRadioProfAutoTunePowerRampInterval_Type()
)
trpzApConfRadioProfAutoTunePowerRampInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfAutoTunePowerRampInterval.setStatus("deprecated")
_TrpzApConfRadioProfAutoTunePowerChangeInterval_Type = Unsigned32
_TrpzApConfRadioProfAutoTunePowerChangeInterval_Object = MibTableColumn
trpzApConfRadioProfAutoTunePowerChangeInterval = _TrpzApConfRadioProfAutoTunePowerChangeInterval_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 21),
    _TrpzApConfRadioProfAutoTunePowerChangeInterval_Type()
)
trpzApConfRadioProfAutoTunePowerChangeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfAutoTunePowerChangeInterval.setStatus("deprecated")
_TrpzApConfRadioProfFairQueuingEnabled_Type = TruthValue
_TrpzApConfRadioProfFairQueuingEnabled_Object = MibTableColumn
trpzApConfRadioProfFairQueuingEnabled = _TrpzApConfRadioProfFairQueuingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 22),
    _TrpzApConfRadioProfFairQueuingEnabled_Type()
)
trpzApConfRadioProfFairQueuingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfFairQueuingEnabled.setStatus("deprecated")
_TrpzApConfRadioProfCacBackgroundACMandatory_Type = TruthValue
_TrpzApConfRadioProfCacBackgroundACMandatory_Object = MibTableColumn
trpzApConfRadioProfCacBackgroundACMandatory = _TrpzApConfRadioProfCacBackgroundACMandatory_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 23),
    _TrpzApConfRadioProfCacBackgroundACMandatory_Type()
)
trpzApConfRadioProfCacBackgroundACMandatory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfCacBackgroundACMandatory.setStatus("deprecated")
_TrpzApConfRadioProfCacBackgroundMaxUtilization_Type = Unsigned32
_TrpzApConfRadioProfCacBackgroundMaxUtilization_Object = MibTableColumn
trpzApConfRadioProfCacBackgroundMaxUtilization = _TrpzApConfRadioProfCacBackgroundMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 24),
    _TrpzApConfRadioProfCacBackgroundMaxUtilization_Type()
)
trpzApConfRadioProfCacBackgroundMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfCacBackgroundMaxUtilization.setStatus("deprecated")
_TrpzApConfRadioProfCacBackgroundPolicingEnabled_Type = TruthValue
_TrpzApConfRadioProfCacBackgroundPolicingEnabled_Object = MibTableColumn
trpzApConfRadioProfCacBackgroundPolicingEnabled = _TrpzApConfRadioProfCacBackgroundPolicingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 25),
    _TrpzApConfRadioProfCacBackgroundPolicingEnabled_Type()
)
trpzApConfRadioProfCacBackgroundPolicingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfCacBackgroundPolicingEnabled.setStatus("deprecated")
_TrpzApConfRadioProfCacBestEffortACMandatory_Type = TruthValue
_TrpzApConfRadioProfCacBestEffortACMandatory_Object = MibTableColumn
trpzApConfRadioProfCacBestEffortACMandatory = _TrpzApConfRadioProfCacBestEffortACMandatory_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 26),
    _TrpzApConfRadioProfCacBestEffortACMandatory_Type()
)
trpzApConfRadioProfCacBestEffortACMandatory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfCacBestEffortACMandatory.setStatus("deprecated")
_TrpzApConfRadioProfCacBestEffortMaxUtilization_Type = Unsigned32
_TrpzApConfRadioProfCacBestEffortMaxUtilization_Object = MibTableColumn
trpzApConfRadioProfCacBestEffortMaxUtilization = _TrpzApConfRadioProfCacBestEffortMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 27),
    _TrpzApConfRadioProfCacBestEffortMaxUtilization_Type()
)
trpzApConfRadioProfCacBestEffortMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfCacBestEffortMaxUtilization.setStatus("deprecated")
_TrpzApConfRadioProfCacBestEffortPolicingEnabled_Type = TruthValue
_TrpzApConfRadioProfCacBestEffortPolicingEnabled_Object = MibTableColumn
trpzApConfRadioProfCacBestEffortPolicingEnabled = _TrpzApConfRadioProfCacBestEffortPolicingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 28),
    _TrpzApConfRadioProfCacBestEffortPolicingEnabled_Type()
)
trpzApConfRadioProfCacBestEffortPolicingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfCacBestEffortPolicingEnabled.setStatus("deprecated")
_TrpzApConfRadioProfCacVideoACMandatory_Type = TruthValue
_TrpzApConfRadioProfCacVideoACMandatory_Object = MibTableColumn
trpzApConfRadioProfCacVideoACMandatory = _TrpzApConfRadioProfCacVideoACMandatory_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 29),
    _TrpzApConfRadioProfCacVideoACMandatory_Type()
)
trpzApConfRadioProfCacVideoACMandatory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfCacVideoACMandatory.setStatus("deprecated")
_TrpzApConfRadioProfCacVideoMaxUtilization_Type = Unsigned32
_TrpzApConfRadioProfCacVideoMaxUtilization_Object = MibTableColumn
trpzApConfRadioProfCacVideoMaxUtilization = _TrpzApConfRadioProfCacVideoMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 30),
    _TrpzApConfRadioProfCacVideoMaxUtilization_Type()
)
trpzApConfRadioProfCacVideoMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfCacVideoMaxUtilization.setStatus("deprecated")
_TrpzApConfRadioProfCacVideoPolicingEnabled_Type = TruthValue
_TrpzApConfRadioProfCacVideoPolicingEnabled_Object = MibTableColumn
trpzApConfRadioProfCacVideoPolicingEnabled = _TrpzApConfRadioProfCacVideoPolicingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 31),
    _TrpzApConfRadioProfCacVideoPolicingEnabled_Type()
)
trpzApConfRadioProfCacVideoPolicingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfCacVideoPolicingEnabled.setStatus("deprecated")
_TrpzApConfRadioProfCacVoiceACMandatory_Type = TruthValue
_TrpzApConfRadioProfCacVoiceACMandatory_Object = MibTableColumn
trpzApConfRadioProfCacVoiceACMandatory = _TrpzApConfRadioProfCacVoiceACMandatory_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 32),
    _TrpzApConfRadioProfCacVoiceACMandatory_Type()
)
trpzApConfRadioProfCacVoiceACMandatory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfCacVoiceACMandatory.setStatus("deprecated")
_TrpzApConfRadioProfCacVoiceMaxUtilization_Type = Unsigned32
_TrpzApConfRadioProfCacVoiceMaxUtilization_Object = MibTableColumn
trpzApConfRadioProfCacVoiceMaxUtilization = _TrpzApConfRadioProfCacVoiceMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 33),
    _TrpzApConfRadioProfCacVoiceMaxUtilization_Type()
)
trpzApConfRadioProfCacVoiceMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfCacVoiceMaxUtilization.setStatus("deprecated")
_TrpzApConfRadioProfCacVoicePolicingEnabled_Type = TruthValue
_TrpzApConfRadioProfCacVoicePolicingEnabled_Object = MibTableColumn
trpzApConfRadioProfCacVoicePolicingEnabled = _TrpzApConfRadioProfCacVoicePolicingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 34),
    _TrpzApConfRadioProfCacVoicePolicingEnabled_Type()
)
trpzApConfRadioProfCacVoicePolicingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfCacVoicePolicingEnabled.setStatus("deprecated")
_TrpzApConfRadioProfRfidTagEnabled_Type = TruthValue
_TrpzApConfRadioProfRfidTagEnabled_Object = MibTableColumn
trpzApConfRadioProfRfidTagEnabled = _TrpzApConfRadioProfRfidTagEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 35),
    _TrpzApConfRadioProfRfidTagEnabled_Type()
)
trpzApConfRadioProfRfidTagEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfRfidTagEnabled.setStatus("deprecated")
_TrpzApConfRadioProfWmmPowerSaveEnabled_Type = TruthValue
_TrpzApConfRadioProfWmmPowerSaveEnabled_Object = MibTableColumn
trpzApConfRadioProfWmmPowerSaveEnabled = _TrpzApConfRadioProfWmmPowerSaveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 36),
    _TrpzApConfRadioProfWmmPowerSaveEnabled_Type()
)
trpzApConfRadioProfWmmPowerSaveEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfWmmPowerSaveEnabled.setStatus("deprecated")
_TrpzApConfRadioProfRateEnforcementEnabled_Type = TruthValue
_TrpzApConfRadioProfRateEnforcementEnabled_Object = MibTableColumn
trpzApConfRadioProfRateEnforcementEnabled = _TrpzApConfRadioProfRateEnforcementEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 37),
    _TrpzApConfRadioProfRateEnforcementEnabled_Type()
)
trpzApConfRadioProfRateEnforcementEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfRateEnforcementEnabled.setStatus("deprecated")
_TrpzApConfRadioProfDfsChannelsEnabled_Type = TruthValue
_TrpzApConfRadioProfDfsChannelsEnabled_Object = MibTableColumn
trpzApConfRadioProfDfsChannelsEnabled = _TrpzApConfRadioProfDfsChannelsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 38),
    _TrpzApConfRadioProfDfsChannelsEnabled_Type()
)
trpzApConfRadioProfDfsChannelsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfDfsChannelsEnabled.setStatus("deprecated")
_TrpzApConfRadioProfRFSpectralScanModeEnabled_Type = TruthValue
_TrpzApConfRadioProfRFSpectralScanModeEnabled_Object = MibTableColumn
trpzApConfRadioProfRFSpectralScanModeEnabled = _TrpzApConfRadioProfRFSpectralScanModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 39),
    _TrpzApConfRadioProfRFSpectralScanModeEnabled_Type()
)
trpzApConfRadioProfRFSpectralScanModeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfRFSpectralScanModeEnabled.setStatus("deprecated")
_TrpzApConfRadioProfRFSpectralScanPriority_Type = TrpzRadioProfileRFSpectralScanPriority
_TrpzApConfRadioProfRFSpectralScanPriority_Object = MibTableColumn
trpzApConfRadioProfRFSpectralScanPriority = _TrpzApConfRadioProfRFSpectralScanPriority_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 40),
    _TrpzApConfRadioProfRFSpectralScanPriority_Type()
)
trpzApConfRadioProfRFSpectralScanPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfRFSpectralScanPriority.setStatus("deprecated")
_TrpzApConfRadioProfRadioProfileFullName_Type = DisplayString
_TrpzApConfRadioProfRadioProfileFullName_Object = MibTableColumn
trpzApConfRadioProfRadioProfileFullName = _TrpzApConfRadioProfRadioProfileFullName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 6, 1, 41),
    _TrpzApConfRadioProfRadioProfileFullName_Type()
)
trpzApConfRadioProfRadioProfileFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProfRadioProfileFullName.setStatus("deprecated")
_TrpzApConfRadioProfServiceProfileTable_Object = MibTable
trpzApConfRadioProfServiceProfileTable = _TrpzApConfRadioProfServiceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 7)
)
if mibBuilder.loadTexts:
    trpzApConfRadioProfServiceProfileTable.setStatus("deprecated")
_TrpzApConfRadioProfServiceProfileEntry_Object = MibTableRow
trpzApConfRadioProfServiceProfileEntry = _TrpzApConfRadioProfServiceProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 7, 1)
)
trpzApConfRadioProfServiceProfileEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRpServpRadioProfileName"),
    (0, "TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRpServpServiceProfileName"),
)
if mibBuilder.loadTexts:
    trpzApConfRadioProfServiceProfileEntry.setStatus("deprecated")
_TrpzApConfRpServpRadioProfileName_Type = TrpzRadioProfileName
_TrpzApConfRpServpRadioProfileName_Object = MibTableColumn
trpzApConfRpServpRadioProfileName = _TrpzApConfRpServpRadioProfileName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 7, 1, 1),
    _TrpzApConfRpServpRadioProfileName_Type()
)
trpzApConfRpServpRadioProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApConfRpServpRadioProfileName.setStatus("deprecated")
_TrpzApConfRpServpServiceProfileName_Type = TrpzServiceProfileName
_TrpzApConfRpServpServiceProfileName_Object = MibTableColumn
trpzApConfRpServpServiceProfileName = _TrpzApConfRpServpServiceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 7, 1, 2),
    _TrpzApConfRpServpServiceProfileName_Type()
)
trpzApConfRpServpServiceProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApConfRpServpServiceProfileName.setStatus("deprecated")
_TrpzApConfRpServpRowStatus_Type = RowStatus
_TrpzApConfRpServpRowStatus_Object = MibTableColumn
trpzApConfRpServpRowStatus = _TrpzApConfRpServpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 7, 1, 3),
    _TrpzApConfRpServpRowStatus_Type()
)
trpzApConfRpServpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trpzApConfRpServpRowStatus.setStatus("deprecated")
_TrpzApConfRadioProfSnoopFilterTable_Object = MibTable
trpzApConfRadioProfSnoopFilterTable = _TrpzApConfRadioProfSnoopFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 8)
)
if mibBuilder.loadTexts:
    trpzApConfRadioProfSnoopFilterTable.setStatus("deprecated")
_TrpzApConfRadioProfSnoopFilterEntry_Object = MibTableRow
trpzApConfRadioProfSnoopFilterEntry = _TrpzApConfRadioProfSnoopFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 8, 1)
)
trpzApConfRadioProfSnoopFilterEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRpSnoopfRadioProfileName"),
    (0, "TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRpSnoopfSnoopFilterName"),
)
if mibBuilder.loadTexts:
    trpzApConfRadioProfSnoopFilterEntry.setStatus("deprecated")
_TrpzApConfRpSnoopfRadioProfileName_Type = TrpzRadioProfileName
_TrpzApConfRpSnoopfRadioProfileName_Object = MibTableColumn
trpzApConfRpSnoopfRadioProfileName = _TrpzApConfRpSnoopfRadioProfileName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 8, 1, 1),
    _TrpzApConfRpSnoopfRadioProfileName_Type()
)
trpzApConfRpSnoopfRadioProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApConfRpSnoopfRadioProfileName.setStatus("deprecated")
_TrpzApConfRpSnoopfSnoopFilterName_Type = TrpzSnoopFilterName
_TrpzApConfRpSnoopfSnoopFilterName_Object = MibTableColumn
trpzApConfRpSnoopfSnoopFilterName = _TrpzApConfRpSnoopfSnoopFilterName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 8, 1, 2),
    _TrpzApConfRpSnoopfSnoopFilterName_Type()
)
trpzApConfRpSnoopfSnoopFilterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApConfRpSnoopfSnoopFilterName.setStatus("deprecated")
_TrpzApConfRpSnoopfRowStatus_Type = RowStatus
_TrpzApConfRpSnoopfRowStatus_Object = MibTableColumn
trpzApConfRpSnoopfRowStatus = _TrpzApConfRpSnoopfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 8, 1, 3),
    _TrpzApConfRpSnoopfRowStatus_Type()
)
trpzApConfRpSnoopfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trpzApConfRpSnoopfRowStatus.setStatus("deprecated")
_TrpzApConfServiceProfileTable_Object = MibTable
trpzApConfServiceProfileTable = _TrpzApConfServiceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9)
)
if mibBuilder.loadTexts:
    trpzApConfServiceProfileTable.setStatus("current")
_TrpzApConfServiceProfileEntry_Object = MibTableRow
trpzApConfServiceProfileEntry = _TrpzApConfServiceProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1)
)
trpzApConfServiceProfileEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfServiceProfileName"),
)
if mibBuilder.loadTexts:
    trpzApConfServiceProfileEntry.setStatus("current")
_TrpzApConfServProfServiceProfileName_Type = TrpzServiceProfileName
_TrpzApConfServProfServiceProfileName_Object = MibTableColumn
trpzApConfServProfServiceProfileName = _TrpzApConfServProfServiceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 1),
    _TrpzApConfServProfServiceProfileName_Type()
)
trpzApConfServProfServiceProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApConfServProfServiceProfileName.setStatus("current")
_TrpzApConfServProfSsidType_Type = TrpzServiceProfileSsidType
_TrpzApConfServProfSsidType_Object = MibTableColumn
trpzApConfServProfSsidType = _TrpzApConfServProfSsidType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 2),
    _TrpzApConfServProfSsidType_Type()
)
trpzApConfServProfSsidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfSsidType.setStatus("current")
_TrpzApConfServProfBeaconEnabled_Type = TruthValue
_TrpzApConfServProfBeaconEnabled_Object = MibTableColumn
trpzApConfServProfBeaconEnabled = _TrpzApConfServProfBeaconEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 3),
    _TrpzApConfServProfBeaconEnabled_Type()
)
trpzApConfServProfBeaconEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfBeaconEnabled.setStatus("current")
_TrpzApConfServProf11naMode_Type = TrpzServiceProfile11nMode
_TrpzApConfServProf11naMode_Object = MibTableColumn
trpzApConfServProf11naMode = _TrpzApConfServProf11naMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 4),
    _TrpzApConfServProf11naMode_Type()
)
trpzApConfServProf11naMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProf11naMode.setStatus("current")
_TrpzApConfServProf11ngMode_Type = TrpzServiceProfile11nMode
_TrpzApConfServProf11ngMode_Object = MibTableColumn
trpzApConfServProf11ngMode = _TrpzApConfServProf11ngMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 5),
    _TrpzApConfServProf11ngMode_Type()
)
trpzApConfServProf11ngMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProf11ngMode.setStatus("current")
_TrpzApConfServProf11nShortGuardIntervalEnabled_Type = TruthValue
_TrpzApConfServProf11nShortGuardIntervalEnabled_Object = MibTableColumn
trpzApConfServProf11nShortGuardIntervalEnabled = _TrpzApConfServProf11nShortGuardIntervalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 6),
    _TrpzApConfServProf11nShortGuardIntervalEnabled_Type()
)
trpzApConfServProf11nShortGuardIntervalEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProf11nShortGuardIntervalEnabled.setStatus("current")
_TrpzApConfServProf11nFrameAggregation_Type = TrpzServiceProfile11nFrameAggregationType
_TrpzApConfServProf11nFrameAggregation_Object = MibTableColumn
trpzApConfServProf11nFrameAggregation = _TrpzApConfServProf11nFrameAggregation_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 7),
    _TrpzApConfServProf11nFrameAggregation_Type()
)
trpzApConfServProf11nFrameAggregation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProf11nFrameAggregation.setStatus("current")
_TrpzApConfServProf11nMsduMaxLength_Type = TrpzServiceProfile11nMsduMaxLength
_TrpzApConfServProf11nMsduMaxLength_Object = MibTableColumn
trpzApConfServProf11nMsduMaxLength = _TrpzApConfServProf11nMsduMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 8),
    _TrpzApConfServProf11nMsduMaxLength_Type()
)
trpzApConfServProf11nMsduMaxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProf11nMsduMaxLength.setStatus("current")
_TrpzApConfServProf11nMpduMaxLength_Type = TrpzServiceProfile11nMpduMaxLength
_TrpzApConfServProf11nMpduMaxLength_Object = MibTableColumn
trpzApConfServProf11nMpduMaxLength = _TrpzApConfServProf11nMpduMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 9),
    _TrpzApConfServProf11nMpduMaxLength_Type()
)
trpzApConfServProf11nMpduMaxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProf11nMpduMaxLength.setStatus("current")
_TrpzApConfServProfAuthFallthru_Type = TrpzServiceProfileAuthFallthruType
_TrpzApConfServProfAuthFallthru_Object = MibTableColumn
trpzApConfServProfAuthFallthru = _TrpzApConfServProfAuthFallthru_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 10),
    _TrpzApConfServProfAuthFallthru_Type()
)
trpzApConfServProfAuthFallthru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfAuthFallthru.setStatus("current")


class _TrpzApConfServProfWebAAAForm_Type(DisplayString):
    """Custom type trpzApConfServProfWebAAAForm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TrpzApConfServProfWebAAAForm_Type.__name__ = "DisplayString"
_TrpzApConfServProfWebAAAForm_Object = MibTableColumn
trpzApConfServProfWebAAAForm = _TrpzApConfServProfWebAAAForm_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 11),
    _TrpzApConfServProfWebAAAForm_Type()
)
trpzApConfServProfWebAAAForm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfWebAAAForm.setStatus("current")
_TrpzApConfServProfSharedKeyAuthEnabled_Type = TruthValue
_TrpzApConfServProfSharedKeyAuthEnabled_Object = MibTableColumn
trpzApConfServProfSharedKeyAuthEnabled = _TrpzApConfServProfSharedKeyAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 12),
    _TrpzApConfServProfSharedKeyAuthEnabled_Type()
)
trpzApConfServProfSharedKeyAuthEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfSharedKeyAuthEnabled.setStatus("current")
_TrpzApConfServProfWpaIeEnabled_Type = TruthValue
_TrpzApConfServProfWpaIeEnabled_Object = MibTableColumn
trpzApConfServProfWpaIeEnabled = _TrpzApConfServProfWpaIeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 13),
    _TrpzApConfServProfWpaIeEnabled_Type()
)
trpzApConfServProfWpaIeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfWpaIeEnabled.setStatus("current")
_TrpzApConfServProfWpaIeCipherTkipEnabled_Type = TruthValue
_TrpzApConfServProfWpaIeCipherTkipEnabled_Object = MibTableColumn
trpzApConfServProfWpaIeCipherTkipEnabled = _TrpzApConfServProfWpaIeCipherTkipEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 14),
    _TrpzApConfServProfWpaIeCipherTkipEnabled_Type()
)
trpzApConfServProfWpaIeCipherTkipEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfWpaIeCipherTkipEnabled.setStatus("current")
_TrpzApConfServProfWpaIeCipherCcmpEnabled_Type = TruthValue
_TrpzApConfServProfWpaIeCipherCcmpEnabled_Object = MibTableColumn
trpzApConfServProfWpaIeCipherCcmpEnabled = _TrpzApConfServProfWpaIeCipherCcmpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 15),
    _TrpzApConfServProfWpaIeCipherCcmpEnabled_Type()
)
trpzApConfServProfWpaIeCipherCcmpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfWpaIeCipherCcmpEnabled.setStatus("current")
_TrpzApConfServProfWpaIeCipherWep40Enabled_Type = TruthValue
_TrpzApConfServProfWpaIeCipherWep40Enabled_Object = MibTableColumn
trpzApConfServProfWpaIeCipherWep40Enabled = _TrpzApConfServProfWpaIeCipherWep40Enabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 16),
    _TrpzApConfServProfWpaIeCipherWep40Enabled_Type()
)
trpzApConfServProfWpaIeCipherWep40Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfWpaIeCipherWep40Enabled.setStatus("obsolete")
_TrpzApConfServProfWpaIeCipherWep104Enabled_Type = TruthValue
_TrpzApConfServProfWpaIeCipherWep104Enabled_Object = MibTableColumn
trpzApConfServProfWpaIeCipherWep104Enabled = _TrpzApConfServProfWpaIeCipherWep104Enabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 17),
    _TrpzApConfServProfWpaIeCipherWep104Enabled_Type()
)
trpzApConfServProfWpaIeCipherWep104Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfWpaIeCipherWep104Enabled.setStatus("obsolete")
_TrpzApConfServProfWpaIeAuthDot1xEnabled_Type = TruthValue
_TrpzApConfServProfWpaIeAuthDot1xEnabled_Object = MibTableColumn
trpzApConfServProfWpaIeAuthDot1xEnabled = _TrpzApConfServProfWpaIeAuthDot1xEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 18),
    _TrpzApConfServProfWpaIeAuthDot1xEnabled_Type()
)
trpzApConfServProfWpaIeAuthDot1xEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfWpaIeAuthDot1xEnabled.setStatus("current")
_TrpzApConfServProfWpaIeAuthPskEnabled_Type = TruthValue
_TrpzApConfServProfWpaIeAuthPskEnabled_Object = MibTableColumn
trpzApConfServProfWpaIeAuthPskEnabled = _TrpzApConfServProfWpaIeAuthPskEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 19),
    _TrpzApConfServProfWpaIeAuthPskEnabled_Type()
)
trpzApConfServProfWpaIeAuthPskEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfWpaIeAuthPskEnabled.setStatus("current")
_TrpzApConfServProfRsnIeEnabled_Type = TruthValue
_TrpzApConfServProfRsnIeEnabled_Object = MibTableColumn
trpzApConfServProfRsnIeEnabled = _TrpzApConfServProfRsnIeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 20),
    _TrpzApConfServProfRsnIeEnabled_Type()
)
trpzApConfServProfRsnIeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfRsnIeEnabled.setStatus("current")
_TrpzApConfServProfRsnIeCipherTkipEnabled_Type = TruthValue
_TrpzApConfServProfRsnIeCipherTkipEnabled_Object = MibTableColumn
trpzApConfServProfRsnIeCipherTkipEnabled = _TrpzApConfServProfRsnIeCipherTkipEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 21),
    _TrpzApConfServProfRsnIeCipherTkipEnabled_Type()
)
trpzApConfServProfRsnIeCipherTkipEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfRsnIeCipherTkipEnabled.setStatus("current")
_TrpzApConfServProfRsnIeCipherCcmpEnabled_Type = TruthValue
_TrpzApConfServProfRsnIeCipherCcmpEnabled_Object = MibTableColumn
trpzApConfServProfRsnIeCipherCcmpEnabled = _TrpzApConfServProfRsnIeCipherCcmpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 22),
    _TrpzApConfServProfRsnIeCipherCcmpEnabled_Type()
)
trpzApConfServProfRsnIeCipherCcmpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfRsnIeCipherCcmpEnabled.setStatus("current")
_TrpzApConfServProfRsnIeCipherWep40Enabled_Type = TruthValue
_TrpzApConfServProfRsnIeCipherWep40Enabled_Object = MibTableColumn
trpzApConfServProfRsnIeCipherWep40Enabled = _TrpzApConfServProfRsnIeCipherWep40Enabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 23),
    _TrpzApConfServProfRsnIeCipherWep40Enabled_Type()
)
trpzApConfServProfRsnIeCipherWep40Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfRsnIeCipherWep40Enabled.setStatus("obsolete")
_TrpzApConfServProfRsnIeCipherWep104Enabled_Type = TruthValue
_TrpzApConfServProfRsnIeCipherWep104Enabled_Object = MibTableColumn
trpzApConfServProfRsnIeCipherWep104Enabled = _TrpzApConfServProfRsnIeCipherWep104Enabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 24),
    _TrpzApConfServProfRsnIeCipherWep104Enabled_Type()
)
trpzApConfServProfRsnIeCipherWep104Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfRsnIeCipherWep104Enabled.setStatus("obsolete")
_TrpzApConfServProfRsnIeAuthDot1xEnabled_Type = TruthValue
_TrpzApConfServProfRsnIeAuthDot1xEnabled_Object = MibTableColumn
trpzApConfServProfRsnIeAuthDot1xEnabled = _TrpzApConfServProfRsnIeAuthDot1xEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 25),
    _TrpzApConfServProfRsnIeAuthDot1xEnabled_Type()
)
trpzApConfServProfRsnIeAuthDot1xEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfRsnIeAuthDot1xEnabled.setStatus("current")
_TrpzApConfServProfRsnIeAuthPskEnabled_Type = TruthValue
_TrpzApConfServProfRsnIeAuthPskEnabled_Object = MibTableColumn
trpzApConfServProfRsnIeAuthPskEnabled = _TrpzApConfServProfRsnIeAuthPskEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 26),
    _TrpzApConfServProfRsnIeAuthPskEnabled_Type()
)
trpzApConfServProfRsnIeAuthPskEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfRsnIeAuthPskEnabled.setStatus("current")
_TrpzApConfServProfTkipMicCountermeasuresTime_Type = Unsigned32
_TrpzApConfServProfTkipMicCountermeasuresTime_Object = MibTableColumn
trpzApConfServProfTkipMicCountermeasuresTime = _TrpzApConfServProfTkipMicCountermeasuresTime_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 27),
    _TrpzApConfServProfTkipMicCountermeasuresTime_Type()
)
trpzApConfServProfTkipMicCountermeasuresTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfTkipMicCountermeasuresTime.setStatus("current")
_TrpzApConfServProfMaxBandwidthKbps_Type = Unsigned32
_TrpzApConfServProfMaxBandwidthKbps_Object = MibTableColumn
trpzApConfServProfMaxBandwidthKbps = _TrpzApConfServProfMaxBandwidthKbps_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 28),
    _TrpzApConfServProfMaxBandwidthKbps_Type()
)
trpzApConfServProfMaxBandwidthKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfMaxBandwidthKbps.setStatus("current")
_TrpzApConfServProfCacMode_Type = TrpzServiceProfileCacMode
_TrpzApConfServProfCacMode_Object = MibTableColumn
trpzApConfServProfCacMode = _TrpzApConfServProfCacMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 29),
    _TrpzApConfServProfCacMode_Type()
)
trpzApConfServProfCacMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfCacMode.setStatus("current")
_TrpzApConfServProfCacSessCount_Type = Unsigned32
_TrpzApConfServProfCacSessCount_Object = MibTableColumn
trpzApConfServProfCacSessCount = _TrpzApConfServProfCacSessCount_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 30),
    _TrpzApConfServProfCacSessCount_Type()
)
trpzApConfServProfCacSessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfCacSessCount.setStatus("current")
_TrpzApConfServProfUserIdleTimeout_Type = Unsigned32
_TrpzApConfServProfUserIdleTimeout_Object = MibTableColumn
trpzApConfServProfUserIdleTimeout = _TrpzApConfServProfUserIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 31),
    _TrpzApConfServProfUserIdleTimeout_Type()
)
trpzApConfServProfUserIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfUserIdleTimeout.setStatus("current")
_TrpzApConfServProfIdleClientProbingEnabled_Type = TruthValue
_TrpzApConfServProfIdleClientProbingEnabled_Object = MibTableColumn
trpzApConfServProfIdleClientProbingEnabled = _TrpzApConfServProfIdleClientProbingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 32),
    _TrpzApConfServProfIdleClientProbingEnabled_Type()
)
trpzApConfServProfIdleClientProbingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfIdleClientProbingEnabled.setStatus("current")
_TrpzApConfServProfShortRetryCount_Type = Unsigned32
_TrpzApConfServProfShortRetryCount_Object = MibTableColumn
trpzApConfServProfShortRetryCount = _TrpzApConfServProfShortRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 33),
    _TrpzApConfServProfShortRetryCount_Type()
)
trpzApConfServProfShortRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfShortRetryCount.setStatus("current")
_TrpzApConfServProfLongRetryCount_Type = Unsigned32
_TrpzApConfServProfLongRetryCount_Object = MibTableColumn
trpzApConfServProfLongRetryCount = _TrpzApConfServProfLongRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 34),
    _TrpzApConfServProfLongRetryCount_Type()
)
trpzApConfServProfLongRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfLongRetryCount.setStatus("current")
_TrpzApConfServProfProxyArpEnabled_Type = TruthValue
_TrpzApConfServProfProxyArpEnabled_Object = MibTableColumn
trpzApConfServProfProxyArpEnabled = _TrpzApConfServProfProxyArpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 35),
    _TrpzApConfServProfProxyArpEnabled_Type()
)
trpzApConfServProfProxyArpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfProxyArpEnabled.setStatus("current")
_TrpzApConfServProfDhcpRestrictEnabled_Type = TruthValue
_TrpzApConfServProfDhcpRestrictEnabled_Object = MibTableColumn
trpzApConfServProfDhcpRestrictEnabled = _TrpzApConfServProfDhcpRestrictEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 36),
    _TrpzApConfServProfDhcpRestrictEnabled_Type()
)
trpzApConfServProfDhcpRestrictEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfDhcpRestrictEnabled.setStatus("current")
_TrpzApConfServProfNoBroadcastEnabled_Type = TruthValue
_TrpzApConfServProfNoBroadcastEnabled_Object = MibTableColumn
trpzApConfServProfNoBroadcastEnabled = _TrpzApConfServProfNoBroadcastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 37),
    _TrpzApConfServProfNoBroadcastEnabled_Type()
)
trpzApConfServProfNoBroadcastEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfNoBroadcastEnabled.setStatus("current")
_TrpzApConfServProfSygateOnDemandEnabled_Type = TruthValue
_TrpzApConfServProfSygateOnDemandEnabled_Object = MibTableColumn
trpzApConfServProfSygateOnDemandEnabled = _TrpzApConfServProfSygateOnDemandEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 38),
    _TrpzApConfServProfSygateOnDemandEnabled_Type()
)
trpzApConfServProfSygateOnDemandEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfSygateOnDemandEnabled.setStatus("current")
_TrpzApConfServProfEnforceChecksEnabled_Type = TruthValue
_TrpzApConfServProfEnforceChecksEnabled_Object = MibTableColumn
trpzApConfServProfEnforceChecksEnabled = _TrpzApConfServProfEnforceChecksEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 39),
    _TrpzApConfServProfEnforceChecksEnabled_Type()
)
trpzApConfServProfEnforceChecksEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfEnforceChecksEnabled.setStatus("current")


class _TrpzApConfServProfSodaRemediationAcl_Type(DisplayString):
    """Custom type trpzApConfServProfSodaRemediationAcl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrpzApConfServProfSodaRemediationAcl_Type.__name__ = "DisplayString"
_TrpzApConfServProfSodaRemediationAcl_Object = MibTableColumn
trpzApConfServProfSodaRemediationAcl = _TrpzApConfServProfSodaRemediationAcl_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 40),
    _TrpzApConfServProfSodaRemediationAcl_Type()
)
trpzApConfServProfSodaRemediationAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfSodaRemediationAcl.setStatus("current")


class _TrpzApConfServProfSodaSuccessPage_Type(DisplayString):
    """Custom type trpzApConfServProfSodaSuccessPage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrpzApConfServProfSodaSuccessPage_Type.__name__ = "DisplayString"
_TrpzApConfServProfSodaSuccessPage_Object = MibTableColumn
trpzApConfServProfSodaSuccessPage = _TrpzApConfServProfSodaSuccessPage_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 41),
    _TrpzApConfServProfSodaSuccessPage_Type()
)
trpzApConfServProfSodaSuccessPage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfSodaSuccessPage.setStatus("current")


class _TrpzApConfServProfSodaFailurePage_Type(DisplayString):
    """Custom type trpzApConfServProfSodaFailurePage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrpzApConfServProfSodaFailurePage_Type.__name__ = "DisplayString"
_TrpzApConfServProfSodaFailurePage_Object = MibTableColumn
trpzApConfServProfSodaFailurePage = _TrpzApConfServProfSodaFailurePage_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 42),
    _TrpzApConfServProfSodaFailurePage_Type()
)
trpzApConfServProfSodaFailurePage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfSodaFailurePage.setStatus("current")


class _TrpzApConfServProfSodaLogoutPage_Type(DisplayString):
    """Custom type trpzApConfServProfSodaLogoutPage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrpzApConfServProfSodaLogoutPage_Type.__name__ = "DisplayString"
_TrpzApConfServProfSodaLogoutPage_Object = MibTableColumn
trpzApConfServProfSodaLogoutPage = _TrpzApConfServProfSodaLogoutPage_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 43),
    _TrpzApConfServProfSodaLogoutPage_Type()
)
trpzApConfServProfSodaLogoutPage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfSodaLogoutPage.setStatus("current")


class _TrpzApConfServProfSodaAgentDirectory_Type(DisplayString):
    """Custom type trpzApConfServProfSodaAgentDirectory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrpzApConfServProfSodaAgentDirectory_Type.__name__ = "DisplayString"
_TrpzApConfServProfSodaAgentDirectory_Object = MibTableColumn
trpzApConfServProfSodaAgentDirectory = _TrpzApConfServProfSodaAgentDirectory_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 44),
    _TrpzApConfServProfSodaAgentDirectory_Type()
)
trpzApConfServProfSodaAgentDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfSodaAgentDirectory.setStatus("current")
_TrpzApConfServProfWebPortalSessionTimeout_Type = Unsigned32
_TrpzApConfServProfWebPortalSessionTimeout_Object = MibTableColumn
trpzApConfServProfWebPortalSessionTimeout = _TrpzApConfServProfWebPortalSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 45),
    _TrpzApConfServProfWebPortalSessionTimeout_Type()
)
trpzApConfServProfWebPortalSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfWebPortalSessionTimeout.setStatus("current")


class _TrpzApConfServProfWebPortalAcl_Type(DisplayString):
    """Custom type trpzApConfServProfWebPortalAcl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrpzApConfServProfWebPortalAcl_Type.__name__ = "DisplayString"
_TrpzApConfServProfWebPortalAcl_Object = MibTableColumn
trpzApConfServProfWebPortalAcl = _TrpzApConfServProfWebPortalAcl_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 46),
    _TrpzApConfServProfWebPortalAcl_Type()
)
trpzApConfServProfWebPortalAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfWebPortalAcl.setStatus("current")
_TrpzApConfServProfWebPortalLogoutEnabled_Type = TruthValue
_TrpzApConfServProfWebPortalLogoutEnabled_Object = MibTableColumn
trpzApConfServProfWebPortalLogoutEnabled = _TrpzApConfServProfWebPortalLogoutEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 47),
    _TrpzApConfServProfWebPortalLogoutEnabled_Type()
)
trpzApConfServProfWebPortalLogoutEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfWebPortalLogoutEnabled.setStatus("current")


class _TrpzApConfServProfWebPortalLogoutUrl_Type(DisplayString):
    """Custom type trpzApConfServProfWebPortalLogoutUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TrpzApConfServProfWebPortalLogoutUrl_Type.__name__ = "DisplayString"
_TrpzApConfServProfWebPortalLogoutUrl_Object = MibTableColumn
trpzApConfServProfWebPortalLogoutUrl = _TrpzApConfServProfWebPortalLogoutUrl_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 48),
    _TrpzApConfServProfWebPortalLogoutUrl_Type()
)
trpzApConfServProfWebPortalLogoutUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfWebPortalLogoutUrl.setStatus("current")
_TrpzApConfServProfKeepInitialVlanEnabled_Type = TruthValue
_TrpzApConfServProfKeepInitialVlanEnabled_Object = MibTableColumn
trpzApConfServProfKeepInitialVlanEnabled = _TrpzApConfServProfKeepInitialVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 49),
    _TrpzApConfServProfKeepInitialVlanEnabled_Type()
)
trpzApConfServProfKeepInitialVlanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfKeepInitialVlanEnabled.setStatus("current")
_TrpzApConfServProfMeshModeEnabled_Type = TruthValue
_TrpzApConfServProfMeshModeEnabled_Object = MibTableColumn
trpzApConfServProfMeshModeEnabled = _TrpzApConfServProfMeshModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 50),
    _TrpzApConfServProfMeshModeEnabled_Type()
)
trpzApConfServProfMeshModeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfMeshModeEnabled.setStatus("current")
_TrpzApConfServProfBridgingEnabled_Type = TruthValue
_TrpzApConfServProfBridgingEnabled_Object = MibTableColumn
trpzApConfServProfBridgingEnabled = _TrpzApConfServProfBridgingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 51),
    _TrpzApConfServProfBridgingEnabled_Type()
)
trpzApConfServProfBridgingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfBridgingEnabled.setStatus("current")
_TrpzApConfServProfLoadBalanceExemptEnabled_Type = TruthValue
_TrpzApConfServProfLoadBalanceExemptEnabled_Object = MibTableColumn
trpzApConfServProfLoadBalanceExemptEnabled = _TrpzApConfServProfLoadBalanceExemptEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 52),
    _TrpzApConfServProfLoadBalanceExemptEnabled_Type()
)
trpzApConfServProfLoadBalanceExemptEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfLoadBalanceExemptEnabled.setStatus("current")
_TrpzApConfServProfM2UConversionEnabled_Type = TruthValue
_TrpzApConfServProfM2UConversionEnabled_Object = MibTableColumn
trpzApConfServProfM2UConversionEnabled = _TrpzApConfServProfM2UConversionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 53),
    _TrpzApConfServProfM2UConversionEnabled_Type()
)
trpzApConfServProfM2UConversionEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfM2UConversionEnabled.setStatus("current")
_TrpzApConfServProfBackupSsidMode_Type = TrpzBackupSsidMode
_TrpzApConfServProfBackupSsidMode_Object = MibTableColumn
trpzApConfServProfBackupSsidMode = _TrpzApConfServProfBackupSsidMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 54),
    _TrpzApConfServProfBackupSsidMode_Type()
)
trpzApConfServProfBackupSsidMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfBackupSsidMode.setStatus("current")
_TrpzApConfServProfBackupSsidTimeout_Type = Unsigned32
_TrpzApConfServProfBackupSsidTimeout_Object = MibTableColumn
trpzApConfServProfBackupSsidTimeout = _TrpzApConfServProfBackupSsidTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 55),
    _TrpzApConfServProfBackupSsidTimeout_Type()
)
trpzApConfServProfBackupSsidTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfBackupSsidTimeout.setStatus("current")
if mibBuilder.loadTexts:
    trpzApConfServProfBackupSsidTimeout.setUnits("seconds")
_TrpzApConfServProfBackupSsidKeepClients_Type = TruthValue
_TrpzApConfServProfBackupSsidKeepClients_Object = MibTableColumn
trpzApConfServProfBackupSsidKeepClients = _TrpzApConfServProfBackupSsidKeepClients_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 56),
    _TrpzApConfServProfBackupSsidKeepClients_Type()
)
trpzApConfServProfBackupSsidKeepClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfBackupSsidKeepClients.setStatus("current")


class _TrpzApConfServProfWebPortalLogoutForm_Type(DisplayString):
    """Custom type trpzApConfServProfWebPortalLogoutForm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TrpzApConfServProfWebPortalLogoutForm_Type.__name__ = "DisplayString"
_TrpzApConfServProfWebPortalLogoutForm_Object = MibTableColumn
trpzApConfServProfWebPortalLogoutForm = _TrpzApConfServProfWebPortalLogoutForm_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 9, 1, 57),
    _TrpzApConfServProfWebPortalLogoutForm_Type()
)
trpzApConfServProfWebPortalLogoutForm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfServProfWebPortalLogoutForm.setStatus("current")
_TrpzApConfSnoopFilterTable_Object = MibTable
trpzApConfSnoopFilterTable = _TrpzApConfSnoopFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 10)
)
if mibBuilder.loadTexts:
    trpzApConfSnoopFilterTable.setStatus("current")
_TrpzApConfSnoopFilterEntry_Object = MibTableRow
trpzApConfSnoopFilterEntry = _TrpzApConfSnoopFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 10, 1)
)
trpzApConfSnoopFilterEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfSnoopFilterName"),
)
if mibBuilder.loadTexts:
    trpzApConfSnoopFilterEntry.setStatus("current")
_TrpzApConfSnoopFilterName_Type = TrpzSnoopFilterName
_TrpzApConfSnoopFilterName_Object = MibTableColumn
trpzApConfSnoopFilterName = _TrpzApConfSnoopFilterName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 10, 1, 1),
    _TrpzApConfSnoopFilterName_Type()
)
trpzApConfSnoopFilterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApConfSnoopFilterName.setStatus("current")
_TrpzApConfSnoopFilterEnabled_Type = TruthValue
_TrpzApConfSnoopFilterEnabled_Object = MibTableColumn
trpzApConfSnoopFilterEnabled = _TrpzApConfSnoopFilterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 10, 1, 2),
    _TrpzApConfSnoopFilterEnabled_Type()
)
trpzApConfSnoopFilterEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfSnoopFilterEnabled.setStatus("current")
_TrpzApConfSnoopFilterObserverAddrType_Type = InetAddressType
_TrpzApConfSnoopFilterObserverAddrType_Object = MibTableColumn
trpzApConfSnoopFilterObserverAddrType = _TrpzApConfSnoopFilterObserverAddrType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 10, 1, 3),
    _TrpzApConfSnoopFilterObserverAddrType_Type()
)
trpzApConfSnoopFilterObserverAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfSnoopFilterObserverAddrType.setStatus("current")
_TrpzApConfSnoopFilterObserverAddr_Type = InetAddress
_TrpzApConfSnoopFilterObserverAddr_Object = MibTableColumn
trpzApConfSnoopFilterObserverAddr = _TrpzApConfSnoopFilterObserverAddr_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 10, 1, 4),
    _TrpzApConfSnoopFilterObserverAddr_Type()
)
trpzApConfSnoopFilterObserverAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfSnoopFilterObserverAddr.setStatus("current")
_TrpzApConfRadioSnoopFilterTable_Object = MibTable
trpzApConfRadioSnoopFilterTable = _TrpzApConfRadioSnoopFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 11)
)
if mibBuilder.loadTexts:
    trpzApConfRadioSnoopFilterTable.setStatus("current")
_TrpzApConfRadioSnoopFilterEntry_Object = MibTableRow
trpzApConfRadioSnoopFilterEntry = _TrpzApConfRadioSnoopFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 11, 1)
)
trpzApConfRadioSnoopFilterEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigApNum"),
    (0, "TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigRadioIndex"),
    (0, "TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfSnoopFilterName"),
)
if mibBuilder.loadTexts:
    trpzApConfRadioSnoopFilterEntry.setStatus("current")
_TrpzApConfRadioSnoopFilterRowStatus_Type = RowStatus
_TrpzApConfRadioSnoopFilterRowStatus_Object = MibTableColumn
trpzApConfRadioSnoopFilterRowStatus = _TrpzApConfRadioSnoopFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 11, 1, 1),
    _TrpzApConfRadioSnoopFilterRowStatus_Type()
)
trpzApConfRadioSnoopFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trpzApConfRadioSnoopFilterRowStatus.setStatus("current")
_TrpzApConfSnoopObserverTable_Object = MibTable
trpzApConfSnoopObserverTable = _TrpzApConfSnoopObserverTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 12)
)
if mibBuilder.loadTexts:
    trpzApConfSnoopObserverTable.setStatus("current")
_TrpzApConfSnoopObserverEntry_Object = MibTableRow
trpzApConfSnoopObserverEntry = _TrpzApConfSnoopObserverEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 12, 1)
)
trpzApConfSnoopObserverEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfSnoopObserverTargetAddrType"),
    (0, "TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfSnoopObserverTargetAddr"),
)
if mibBuilder.loadTexts:
    trpzApConfSnoopObserverEntry.setStatus("current")
_TrpzApConfSnoopObserverTargetAddrType_Type = InetAddressType
_TrpzApConfSnoopObserverTargetAddrType_Object = MibTableColumn
trpzApConfSnoopObserverTargetAddrType = _TrpzApConfSnoopObserverTargetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 12, 1, 1),
    _TrpzApConfSnoopObserverTargetAddrType_Type()
)
trpzApConfSnoopObserverTargetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApConfSnoopObserverTargetAddrType.setStatus("current")


class _TrpzApConfSnoopObserverTargetAddr_Type(InetAddress):
    """Custom type trpzApConfSnoopObserverTargetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TrpzApConfSnoopObserverTargetAddr_Type.__name__ = "InetAddress"
_TrpzApConfSnoopObserverTargetAddr_Object = MibTableColumn
trpzApConfSnoopObserverTargetAddr = _TrpzApConfSnoopObserverTargetAddr_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 12, 1, 2),
    _TrpzApConfSnoopObserverTargetAddr_Type()
)
trpzApConfSnoopObserverTargetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApConfSnoopObserverTargetAddr.setStatus("current")
_TrpzApConfSnoopObserverSnapLength_Type = Unsigned32
_TrpzApConfSnoopObserverSnapLength_Object = MibTableColumn
trpzApConfSnoopObserverSnapLength = _TrpzApConfSnoopObserverSnapLength_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 12, 1, 3),
    _TrpzApConfSnoopObserverSnapLength_Type()
)
trpzApConfSnoopObserverSnapLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfSnoopObserverSnapLength.setStatus("current")
_TrpzApConfSnoopObserverInterval_Type = Unsigned32
_TrpzApConfSnoopObserverInterval_Object = MibTableColumn
trpzApConfSnoopObserverInterval = _TrpzApConfSnoopObserverInterval_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 12, 1, 4),
    _TrpzApConfSnoopObserverInterval_Type()
)
trpzApConfSnoopObserverInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfSnoopObserverInterval.setStatus("current")
_TrpzApConfSnoopObserverTxMode_Type = TrpzSnoopObserverTxMode
_TrpzApConfSnoopObserverTxMode_Object = MibTableColumn
trpzApConfSnoopObserverTxMode = _TrpzApConfSnoopObserverTxMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 12, 1, 5),
    _TrpzApConfSnoopObserverTxMode_Type()
)
trpzApConfSnoopObserverTxMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfSnoopObserverTxMode.setStatus("current")
_TrpzApConfRemoteSiteTable_Object = MibTable
trpzApConfRemoteSiteTable = _TrpzApConfRemoteSiteTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 13)
)
if mibBuilder.loadTexts:
    trpzApConfRemoteSiteTable.setStatus("current")
_TrpzApConfRemoteSiteEntry_Object = MibTableRow
trpzApConfRemoteSiteEntry = _TrpzApConfRemoteSiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 13, 1)
)
trpzApConfRemoteSiteEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRemoteSiteName"),
)
if mibBuilder.loadTexts:
    trpzApConfRemoteSiteEntry.setStatus("current")


class _TrpzApConfRemoteSiteName_Type(DisplayString):
    """Custom type trpzApConfRemoteSiteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TrpzApConfRemoteSiteName_Type.__name__ = "DisplayString"
_TrpzApConfRemoteSiteName_Object = MibTableColumn
trpzApConfRemoteSiteName = _TrpzApConfRemoteSiteName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 13, 1, 1),
    _TrpzApConfRemoteSiteName_Type()
)
trpzApConfRemoteSiteName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApConfRemoteSiteName.setStatus("current")


class _TrpzApConfRemoteSiteCountryCode_Type(DisplayString):
    """Custom type trpzApConfRemoteSiteCountryCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
        ValueSizeConstraint(4, 4),
    )


_TrpzApConfRemoteSiteCountryCode_Type.__name__ = "DisplayString"
_TrpzApConfRemoteSiteCountryCode_Object = MibTableColumn
trpzApConfRemoteSiteCountryCode = _TrpzApConfRemoteSiteCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 13, 1, 2),
    _TrpzApConfRemoteSiteCountryCode_Type()
)
trpzApConfRemoteSiteCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRemoteSiteCountryCode.setStatus("current")
_TrpzApConfRemoteSitePathMtu_Type = Unsigned32
_TrpzApConfRemoteSitePathMtu_Object = MibTableColumn
trpzApConfRemoteSitePathMtu = _TrpzApConfRemoteSitePathMtu_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 13, 1, 3),
    _TrpzApConfRemoteSitePathMtu_Type()
)
trpzApConfRemoteSitePathMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRemoteSitePathMtu.setStatus("current")
if mibBuilder.loadTexts:
    trpzApConfRemoteSitePathMtu.setUnits("bytes")
_TrpzApConfRemoteSiteBackupSsidsEnabled_Type = TruthValue
_TrpzApConfRemoteSiteBackupSsidsEnabled_Object = MibTableColumn
trpzApConfRemoteSiteBackupSsidsEnabled = _TrpzApConfRemoteSiteBackupSsidsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 13, 1, 4),
    _TrpzApConfRemoteSiteBackupSsidsEnabled_Type()
)
trpzApConfRemoteSiteBackupSsidsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRemoteSiteBackupSsidsEnabled.setStatus("current")
_TrpzApConfRemoteSiteLogServerEnabled_Type = TruthValue
_TrpzApConfRemoteSiteLogServerEnabled_Object = MibTableColumn
trpzApConfRemoteSiteLogServerEnabled = _TrpzApConfRemoteSiteLogServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 13, 1, 5),
    _TrpzApConfRemoteSiteLogServerEnabled_Type()
)
trpzApConfRemoteSiteLogServerEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRemoteSiteLogServerEnabled.setStatus("current")
_TrpzApConfRemoteSiteLogServerAddrType_Type = InetAddressType
_TrpzApConfRemoteSiteLogServerAddrType_Object = MibTableColumn
trpzApConfRemoteSiteLogServerAddrType = _TrpzApConfRemoteSiteLogServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 13, 1, 6),
    _TrpzApConfRemoteSiteLogServerAddrType_Type()
)
trpzApConfRemoteSiteLogServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRemoteSiteLogServerAddrType.setStatus("current")
_TrpzApConfRemoteSiteLogServerAddr_Type = InetAddress
_TrpzApConfRemoteSiteLogServerAddr_Object = MibTableColumn
trpzApConfRemoteSiteLogServerAddr = _TrpzApConfRemoteSiteLogServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 13, 1, 7),
    _TrpzApConfRemoteSiteLogServerAddr_Type()
)
trpzApConfRemoteSiteLogServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRemoteSiteLogServerAddr.setStatus("current")


class _TrpzApConfRemoteSiteLogServerPort_Type(Unsigned32):
    """Custom type trpzApConfRemoteSiteLogServerPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TrpzApConfRemoteSiteLogServerPort_Type.__name__ = "Unsigned32"
_TrpzApConfRemoteSiteLogServerPort_Object = MibTableColumn
trpzApConfRemoteSiteLogServerPort = _TrpzApConfRemoteSiteLogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 13, 1, 8),
    _TrpzApConfRemoteSiteLogServerPort_Type()
)
trpzApConfRemoteSiteLogServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRemoteSiteLogServerPort.setStatus("current")
_TrpzApConfRemoteSiteLogServerSeverity_Type = TrpzSyslogSeverity
_TrpzApConfRemoteSiteLogServerSeverity_Object = MibTableColumn
trpzApConfRemoteSiteLogServerSeverity = _TrpzApConfRemoteSiteLogServerSeverity_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 13, 1, 9),
    _TrpzApConfRemoteSiteLogServerSeverity_Type()
)
trpzApConfRemoteSiteLogServerSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRemoteSiteLogServerSeverity.setStatus("current")
_TrpzApConfRemoteSiteAcPollingEnabled_Type = TruthValue
_TrpzApConfRemoteSiteAcPollingEnabled_Object = MibTableColumn
trpzApConfRemoteSiteAcPollingEnabled = _TrpzApConfRemoteSiteAcPollingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 13, 1, 10),
    _TrpzApConfRemoteSiteAcPollingEnabled_Type()
)
trpzApConfRemoteSiteAcPollingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRemoteSiteAcPollingEnabled.setStatus("current")
_TrpzApConfRemoteSiteRadiusServerGroupName_Type = DisplayString
_TrpzApConfRemoteSiteRadiusServerGroupName_Object = MibTableColumn
trpzApConfRemoteSiteRadiusServerGroupName = _TrpzApConfRemoteSiteRadiusServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 13, 1, 11),
    _TrpzApConfRemoteSiteRadiusServerGroupName_Type()
)
trpzApConfRemoteSiteRadiusServerGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRemoteSiteRadiusServerGroupName.setStatus("current")
_TrpzApConfRemoteSiteRadiusDeadtime_Type = Unsigned32
_TrpzApConfRemoteSiteRadiusDeadtime_Object = MibTableColumn
trpzApConfRemoteSiteRadiusDeadtime = _TrpzApConfRemoteSiteRadiusDeadtime_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 13, 1, 12),
    _TrpzApConfRemoteSiteRadiusDeadtime_Type()
)
trpzApConfRemoteSiteRadiusDeadtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRemoteSiteRadiusDeadtime.setStatus("current")
_TrpzApConfRemoteSiteRadiusTimeout_Type = Unsigned32
_TrpzApConfRemoteSiteRadiusTimeout_Object = MibTableColumn
trpzApConfRemoteSiteRadiusTimeout = _TrpzApConfRemoteSiteRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 13, 1, 13),
    _TrpzApConfRemoteSiteRadiusTimeout_Type()
)
trpzApConfRemoteSiteRadiusTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRemoteSiteRadiusTimeout.setStatus("current")
_TrpzApConfRemoteSiteRadiusRetransmit_Type = Unsigned32
_TrpzApConfRemoteSiteRadiusRetransmit_Object = MibTableColumn
trpzApConfRemoteSiteRadiusRetransmit = _TrpzApConfRemoteSiteRadiusRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 13, 1, 14),
    _TrpzApConfRemoteSiteRadiusRetransmit_Type()
)
trpzApConfRemoteSiteRadiusRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRemoteSiteRadiusRetransmit.setStatus("current")
_TrpzApConfRemoteSiteRadiusNasIdType_Type = TrpzApRadiusNasIdType
_TrpzApConfRemoteSiteRadiusNasIdType_Object = MibTableColumn
trpzApConfRemoteSiteRadiusNasIdType = _TrpzApConfRemoteSiteRadiusNasIdType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 13, 1, 15),
    _TrpzApConfRemoteSiteRadiusNasIdType_Type()
)
trpzApConfRemoteSiteRadiusNasIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRemoteSiteRadiusNasIdType.setStatus("current")
_TrpzApConfRadioProfile32Table_Object = MibTable
trpzApConfRadioProfile32Table = _TrpzApConfRadioProfile32Table_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14)
)
if mibBuilder.loadTexts:
    trpzApConfRadioProfile32Table.setStatus("current")
_TrpzApConfRadioProfile32Entry_Object = MibTableRow
trpzApConfRadioProfile32Entry = _TrpzApConfRadioProfile32Entry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1)
)
trpzApConfRadioProfile32Entry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32RadioProfileName"),
)
if mibBuilder.loadTexts:
    trpzApConfRadioProfile32Entry.setStatus("current")
_TrpzApConfRadioProf32RadioProfileName_Type = TrpzRadioProfileName32
_TrpzApConfRadioProf32RadioProfileName_Object = MibTableColumn
trpzApConfRadioProf32RadioProfileName = _TrpzApConfRadioProf32RadioProfileName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 1),
    _TrpzApConfRadioProf32RadioProfileName_Type()
)
trpzApConfRadioProf32RadioProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32RadioProfileName.setStatus("current")
_TrpzApConfRadioProf32BeaconInterval_Type = Unsigned32
_TrpzApConfRadioProf32BeaconInterval_Object = MibTableColumn
trpzApConfRadioProf32BeaconInterval = _TrpzApConfRadioProf32BeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 2),
    _TrpzApConfRadioProf32BeaconInterval_Type()
)
trpzApConfRadioProf32BeaconInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32BeaconInterval.setStatus("current")
_TrpzApConfRadioProf32DtimInterval_Type = Unsigned32
_TrpzApConfRadioProf32DtimInterval_Object = MibTableColumn
trpzApConfRadioProf32DtimInterval = _TrpzApConfRadioProf32DtimInterval_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 3),
    _TrpzApConfRadioProf32DtimInterval_Type()
)
trpzApConfRadioProf32DtimInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32DtimInterval.setStatus("current")
_TrpzApConfRadioProf32ChannelWidth11na_Type = TrpzRadioChannelWidth
_TrpzApConfRadioProf32ChannelWidth11na_Object = MibTableColumn
trpzApConfRadioProf32ChannelWidth11na = _TrpzApConfRadioProf32ChannelWidth11na_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 4),
    _TrpzApConfRadioProf32ChannelWidth11na_Type()
)
trpzApConfRadioProf32ChannelWidth11na.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32ChannelWidth11na.setStatus("current")
_TrpzApConfRadioProf32MaxTxLifetime_Type = Unsigned32
_TrpzApConfRadioProf32MaxTxLifetime_Object = MibTableColumn
trpzApConfRadioProf32MaxTxLifetime = _TrpzApConfRadioProf32MaxTxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 5),
    _TrpzApConfRadioProf32MaxTxLifetime_Type()
)
trpzApConfRadioProf32MaxTxLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32MaxTxLifetime.setStatus("current")
_TrpzApConfRadioProf32MaxRxLifetime_Type = Unsigned32
_TrpzApConfRadioProf32MaxRxLifetime_Object = MibTableColumn
trpzApConfRadioProf32MaxRxLifetime = _TrpzApConfRadioProf32MaxRxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 6),
    _TrpzApConfRadioProf32MaxRxLifetime_Type()
)
trpzApConfRadioProf32MaxRxLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32MaxRxLifetime.setStatus("current")
_TrpzApConfRadioProf32RtsThreshold_Type = Unsigned32
_TrpzApConfRadioProf32RtsThreshold_Object = MibTableColumn
trpzApConfRadioProf32RtsThreshold = _TrpzApConfRadioProf32RtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 7),
    _TrpzApConfRadioProf32RtsThreshold_Type()
)
trpzApConfRadioProf32RtsThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32RtsThreshold.setStatus("current")
_TrpzApConfRadioProf32FragThreshold_Type = Unsigned32
_TrpzApConfRadioProf32FragThreshold_Object = MibTableColumn
trpzApConfRadioProf32FragThreshold = _TrpzApConfRadioProf32FragThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 8),
    _TrpzApConfRadioProf32FragThreshold_Type()
)
trpzApConfRadioProf32FragThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32FragThreshold.setStatus("current")
_TrpzApConfRadioProf32LongXmitPreambleEnabled_Type = TruthValue
_TrpzApConfRadioProf32LongXmitPreambleEnabled_Object = MibTableColumn
trpzApConfRadioProf32LongXmitPreambleEnabled = _TrpzApConfRadioProf32LongXmitPreambleEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 9),
    _TrpzApConfRadioProf32LongXmitPreambleEnabled_Type()
)
trpzApConfRadioProf32LongXmitPreambleEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32LongXmitPreambleEnabled.setStatus("current")
_TrpzApConfRadioProf32CountermeasuresMode_Type = TrpzRadioProfileCountermeasuresMode
_TrpzApConfRadioProf32CountermeasuresMode_Object = MibTableColumn
trpzApConfRadioProf32CountermeasuresMode = _TrpzApConfRadioProf32CountermeasuresMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 10),
    _TrpzApConfRadioProf32CountermeasuresMode_Type()
)
trpzApConfRadioProf32CountermeasuresMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32CountermeasuresMode.setStatus("current")
_TrpzApConfRadioProf32RFScanMode_Type = TrpzRadioProfileRFScanMode
_TrpzApConfRadioProf32RFScanMode_Object = MibTableColumn
trpzApConfRadioProf32RFScanMode = _TrpzApConfRadioProf32RFScanMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 11),
    _TrpzApConfRadioProf32RFScanMode_Type()
)
trpzApConfRadioProf32RFScanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32RFScanMode.setStatus("current")
_TrpzApConfRadioProf32RFScanChannelScope_Type = TrpzRadioProfileRFScanChannelScope
_TrpzApConfRadioProf32RFScanChannelScope_Object = MibTableColumn
trpzApConfRadioProf32RFScanChannelScope = _TrpzApConfRadioProf32RFScanChannelScope_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 12),
    _TrpzApConfRadioProf32RFScanChannelScope_Type()
)
trpzApConfRadioProf32RFScanChannelScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32RFScanChannelScope.setStatus("current")
_TrpzApConfRadioProf32RFScanCTSEnabled_Type = TruthValue
_TrpzApConfRadioProf32RFScanCTSEnabled_Object = MibTableColumn
trpzApConfRadioProf32RFScanCTSEnabled = _TrpzApConfRadioProf32RFScanCTSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 13),
    _TrpzApConfRadioProf32RFScanCTSEnabled_Type()
)
trpzApConfRadioProf32RFScanCTSEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32RFScanCTSEnabled.setStatus("current")
_TrpzApConfRadioProf32AutoTunePowerEnabled_Type = TruthValue
_TrpzApConfRadioProf32AutoTunePowerEnabled_Object = MibTableColumn
trpzApConfRadioProf32AutoTunePowerEnabled = _TrpzApConfRadioProf32AutoTunePowerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 14),
    _TrpzApConfRadioProf32AutoTunePowerEnabled_Type()
)
trpzApConfRadioProf32AutoTunePowerEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32AutoTunePowerEnabled.setStatus("current")
_TrpzApConfRadioProf32AutoTunePowerRampInterval_Type = Unsigned32
_TrpzApConfRadioProf32AutoTunePowerRampInterval_Object = MibTableColumn
trpzApConfRadioProf32AutoTunePowerRampInterval = _TrpzApConfRadioProf32AutoTunePowerRampInterval_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 15),
    _TrpzApConfRadioProf32AutoTunePowerRampInterval_Type()
)
trpzApConfRadioProf32AutoTunePowerRampInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32AutoTunePowerRampInterval.setStatus("current")
_TrpzApConfRadioProf32AutoTunePowerChangeInterval_Type = Unsigned32
_TrpzApConfRadioProf32AutoTunePowerChangeInterval_Object = MibTableColumn
trpzApConfRadioProf32AutoTunePowerChangeInterval = _TrpzApConfRadioProf32AutoTunePowerChangeInterval_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 16),
    _TrpzApConfRadioProf32AutoTunePowerChangeInterval_Type()
)
trpzApConfRadioProf32AutoTunePowerChangeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32AutoTunePowerChangeInterval.setStatus("current")
_TrpzApConfRadioProf32FairQueuingEnabled_Type = TruthValue
_TrpzApConfRadioProf32FairQueuingEnabled_Object = MibTableColumn
trpzApConfRadioProf32FairQueuingEnabled = _TrpzApConfRadioProf32FairQueuingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 17),
    _TrpzApConfRadioProf32FairQueuingEnabled_Type()
)
trpzApConfRadioProf32FairQueuingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32FairQueuingEnabled.setStatus("current")
_TrpzApConfRadioProf32CacBackgroundACMandatory_Type = TruthValue
_TrpzApConfRadioProf32CacBackgroundACMandatory_Object = MibTableColumn
trpzApConfRadioProf32CacBackgroundACMandatory = _TrpzApConfRadioProf32CacBackgroundACMandatory_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 18),
    _TrpzApConfRadioProf32CacBackgroundACMandatory_Type()
)
trpzApConfRadioProf32CacBackgroundACMandatory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32CacBackgroundACMandatory.setStatus("current")
_TrpzApConfRadioProf32CacBackgroundMaxUtilization_Type = Unsigned32
_TrpzApConfRadioProf32CacBackgroundMaxUtilization_Object = MibTableColumn
trpzApConfRadioProf32CacBackgroundMaxUtilization = _TrpzApConfRadioProf32CacBackgroundMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 19),
    _TrpzApConfRadioProf32CacBackgroundMaxUtilization_Type()
)
trpzApConfRadioProf32CacBackgroundMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32CacBackgroundMaxUtilization.setStatus("current")
_TrpzApConfRadioProf32CacBackgroundPolicingEnabled_Type = TruthValue
_TrpzApConfRadioProf32CacBackgroundPolicingEnabled_Object = MibTableColumn
trpzApConfRadioProf32CacBackgroundPolicingEnabled = _TrpzApConfRadioProf32CacBackgroundPolicingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 20),
    _TrpzApConfRadioProf32CacBackgroundPolicingEnabled_Type()
)
trpzApConfRadioProf32CacBackgroundPolicingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32CacBackgroundPolicingEnabled.setStatus("current")
_TrpzApConfRadioProf32CacBestEffortACMandatory_Type = TruthValue
_TrpzApConfRadioProf32CacBestEffortACMandatory_Object = MibTableColumn
trpzApConfRadioProf32CacBestEffortACMandatory = _TrpzApConfRadioProf32CacBestEffortACMandatory_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 21),
    _TrpzApConfRadioProf32CacBestEffortACMandatory_Type()
)
trpzApConfRadioProf32CacBestEffortACMandatory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32CacBestEffortACMandatory.setStatus("current")
_TrpzApConfRadioProf32CacBestEffortMaxUtilization_Type = Unsigned32
_TrpzApConfRadioProf32CacBestEffortMaxUtilization_Object = MibTableColumn
trpzApConfRadioProf32CacBestEffortMaxUtilization = _TrpzApConfRadioProf32CacBestEffortMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 22),
    _TrpzApConfRadioProf32CacBestEffortMaxUtilization_Type()
)
trpzApConfRadioProf32CacBestEffortMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32CacBestEffortMaxUtilization.setStatus("current")
_TrpzApConfRadioProf32CacBestEffortPolicingEnabled_Type = TruthValue
_TrpzApConfRadioProf32CacBestEffortPolicingEnabled_Object = MibTableColumn
trpzApConfRadioProf32CacBestEffortPolicingEnabled = _TrpzApConfRadioProf32CacBestEffortPolicingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 23),
    _TrpzApConfRadioProf32CacBestEffortPolicingEnabled_Type()
)
trpzApConfRadioProf32CacBestEffortPolicingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32CacBestEffortPolicingEnabled.setStatus("current")
_TrpzApConfRadioProf32CacVideoACMandatory_Type = TruthValue
_TrpzApConfRadioProf32CacVideoACMandatory_Object = MibTableColumn
trpzApConfRadioProf32CacVideoACMandatory = _TrpzApConfRadioProf32CacVideoACMandatory_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 24),
    _TrpzApConfRadioProf32CacVideoACMandatory_Type()
)
trpzApConfRadioProf32CacVideoACMandatory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32CacVideoACMandatory.setStatus("current")
_TrpzApConfRadioProf32CacVideoMaxUtilization_Type = Unsigned32
_TrpzApConfRadioProf32CacVideoMaxUtilization_Object = MibTableColumn
trpzApConfRadioProf32CacVideoMaxUtilization = _TrpzApConfRadioProf32CacVideoMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 25),
    _TrpzApConfRadioProf32CacVideoMaxUtilization_Type()
)
trpzApConfRadioProf32CacVideoMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32CacVideoMaxUtilization.setStatus("current")
_TrpzApConfRadioProf32CacVideoPolicingEnabled_Type = TruthValue
_TrpzApConfRadioProf32CacVideoPolicingEnabled_Object = MibTableColumn
trpzApConfRadioProf32CacVideoPolicingEnabled = _TrpzApConfRadioProf32CacVideoPolicingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 26),
    _TrpzApConfRadioProf32CacVideoPolicingEnabled_Type()
)
trpzApConfRadioProf32CacVideoPolicingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32CacVideoPolicingEnabled.setStatus("current")
_TrpzApConfRadioProf32CacVoiceACMandatory_Type = TruthValue
_TrpzApConfRadioProf32CacVoiceACMandatory_Object = MibTableColumn
trpzApConfRadioProf32CacVoiceACMandatory = _TrpzApConfRadioProf32CacVoiceACMandatory_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 27),
    _TrpzApConfRadioProf32CacVoiceACMandatory_Type()
)
trpzApConfRadioProf32CacVoiceACMandatory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32CacVoiceACMandatory.setStatus("current")
_TrpzApConfRadioProf32CacVoiceMaxUtilization_Type = Unsigned32
_TrpzApConfRadioProf32CacVoiceMaxUtilization_Object = MibTableColumn
trpzApConfRadioProf32CacVoiceMaxUtilization = _TrpzApConfRadioProf32CacVoiceMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 28),
    _TrpzApConfRadioProf32CacVoiceMaxUtilization_Type()
)
trpzApConfRadioProf32CacVoiceMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32CacVoiceMaxUtilization.setStatus("current")
_TrpzApConfRadioProf32CacVoicePolicingEnabled_Type = TruthValue
_TrpzApConfRadioProf32CacVoicePolicingEnabled_Object = MibTableColumn
trpzApConfRadioProf32CacVoicePolicingEnabled = _TrpzApConfRadioProf32CacVoicePolicingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 29),
    _TrpzApConfRadioProf32CacVoicePolicingEnabled_Type()
)
trpzApConfRadioProf32CacVoicePolicingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32CacVoicePolicingEnabled.setStatus("current")
_TrpzApConfRadioProf32RfidTagEnabled_Type = TruthValue
_TrpzApConfRadioProf32RfidTagEnabled_Object = MibTableColumn
trpzApConfRadioProf32RfidTagEnabled = _TrpzApConfRadioProf32RfidTagEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 30),
    _TrpzApConfRadioProf32RfidTagEnabled_Type()
)
trpzApConfRadioProf32RfidTagEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32RfidTagEnabled.setStatus("current")
_TrpzApConfRadioProf32WmmPowerSaveEnabled_Type = TruthValue
_TrpzApConfRadioProf32WmmPowerSaveEnabled_Object = MibTableColumn
trpzApConfRadioProf32WmmPowerSaveEnabled = _TrpzApConfRadioProf32WmmPowerSaveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 31),
    _TrpzApConfRadioProf32WmmPowerSaveEnabled_Type()
)
trpzApConfRadioProf32WmmPowerSaveEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32WmmPowerSaveEnabled.setStatus("current")
_TrpzApConfRadioProf32RateEnforcementEnabled_Type = TruthValue
_TrpzApConfRadioProf32RateEnforcementEnabled_Object = MibTableColumn
trpzApConfRadioProf32RateEnforcementEnabled = _TrpzApConfRadioProf32RateEnforcementEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 32),
    _TrpzApConfRadioProf32RateEnforcementEnabled_Type()
)
trpzApConfRadioProf32RateEnforcementEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32RateEnforcementEnabled.setStatus("current")
_TrpzApConfRadioProf32DfsChannelsEnabled_Type = TruthValue
_TrpzApConfRadioProf32DfsChannelsEnabled_Object = MibTableColumn
trpzApConfRadioProf32DfsChannelsEnabled = _TrpzApConfRadioProf32DfsChannelsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 33),
    _TrpzApConfRadioProf32DfsChannelsEnabled_Type()
)
trpzApConfRadioProf32DfsChannelsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32DfsChannelsEnabled.setStatus("current")
_TrpzApConfRadioProf32RFSpectralScanModeEnabled_Type = TruthValue
_TrpzApConfRadioProf32RFSpectralScanModeEnabled_Object = MibTableColumn
trpzApConfRadioProf32RFSpectralScanModeEnabled = _TrpzApConfRadioProf32RFSpectralScanModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 34),
    _TrpzApConfRadioProf32RFSpectralScanModeEnabled_Type()
)
trpzApConfRadioProf32RFSpectralScanModeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32RFSpectralScanModeEnabled.setStatus("current")
_TrpzApConfRadioProf32RFSpectralScanPriority_Type = TrpzRadioProfileRFSpectralScanPriority
_TrpzApConfRadioProf32RFSpectralScanPriority_Object = MibTableColumn
trpzApConfRadioProf32RFSpectralScanPriority = _TrpzApConfRadioProf32RFSpectralScanPriority_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 14, 1, 35),
    _TrpzApConfRadioProf32RFSpectralScanPriority_Type()
)
trpzApConfRadioProf32RFSpectralScanPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApConfRadioProf32RFSpectralScanPriority.setStatus("current")
_TrpzApConfRadioProf32ServiceProfileTable_Object = MibTable
trpzApConfRadioProf32ServiceProfileTable = _TrpzApConfRadioProf32ServiceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 15)
)
if mibBuilder.loadTexts:
    trpzApConfRadioProf32ServiceProfileTable.setStatus("current")
_TrpzApConfRadioProf32ServiceProfileEntry_Object = MibTableRow
trpzApConfRadioProf32ServiceProfileEntry = _TrpzApConfRadioProf32ServiceProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 15, 1)
)
trpzApConfRadioProf32ServiceProfileEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRp32ServpRadioProfileName"),
    (0, "TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRp32ServpServiceProfileName"),
)
if mibBuilder.loadTexts:
    trpzApConfRadioProf32ServiceProfileEntry.setStatus("current")
_TrpzApConfRp32ServpRadioProfileName_Type = TrpzRadioProfileName32
_TrpzApConfRp32ServpRadioProfileName_Object = MibTableColumn
trpzApConfRp32ServpRadioProfileName = _TrpzApConfRp32ServpRadioProfileName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 15, 1, 1),
    _TrpzApConfRp32ServpRadioProfileName_Type()
)
trpzApConfRp32ServpRadioProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApConfRp32ServpRadioProfileName.setStatus("current")
_TrpzApConfRp32ServpServiceProfileName_Type = TrpzServiceProfileName
_TrpzApConfRp32ServpServiceProfileName_Object = MibTableColumn
trpzApConfRp32ServpServiceProfileName = _TrpzApConfRp32ServpServiceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 15, 1, 2),
    _TrpzApConfRp32ServpServiceProfileName_Type()
)
trpzApConfRp32ServpServiceProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApConfRp32ServpServiceProfileName.setStatus("current")
_TrpzApConfRp32ServpRowStatus_Type = RowStatus
_TrpzApConfRp32ServpRowStatus_Object = MibTableColumn
trpzApConfRp32ServpRowStatus = _TrpzApConfRp32ServpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 15, 1, 3),
    _TrpzApConfRp32ServpRowStatus_Type()
)
trpzApConfRp32ServpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trpzApConfRp32ServpRowStatus.setStatus("current")
_TrpzApConfRadioProf32SnoopFilterTable_Object = MibTable
trpzApConfRadioProf32SnoopFilterTable = _TrpzApConfRadioProf32SnoopFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 16)
)
if mibBuilder.loadTexts:
    trpzApConfRadioProf32SnoopFilterTable.setStatus("current")
_TrpzApConfRadioProf32SnoopFilterEntry_Object = MibTableRow
trpzApConfRadioProf32SnoopFilterEntry = _TrpzApConfRadioProf32SnoopFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 16, 1)
)
trpzApConfRadioProf32SnoopFilterEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRp32SnoopfRadioProfileName"),
    (0, "TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRp32SnoopfSnoopFilterName"),
)
if mibBuilder.loadTexts:
    trpzApConfRadioProf32SnoopFilterEntry.setStatus("current")
_TrpzApConfRp32SnoopfRadioProfileName_Type = TrpzRadioProfileName32
_TrpzApConfRp32SnoopfRadioProfileName_Object = MibTableColumn
trpzApConfRp32SnoopfRadioProfileName = _TrpzApConfRp32SnoopfRadioProfileName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 16, 1, 1),
    _TrpzApConfRp32SnoopfRadioProfileName_Type()
)
trpzApConfRp32SnoopfRadioProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApConfRp32SnoopfRadioProfileName.setStatus("current")
_TrpzApConfRp32SnoopfSnoopFilterName_Type = TrpzSnoopFilterName
_TrpzApConfRp32SnoopfSnoopFilterName_Object = MibTableColumn
trpzApConfRp32SnoopfSnoopFilterName = _TrpzApConfRp32SnoopfSnoopFilterName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 16, 1, 2),
    _TrpzApConfRp32SnoopfSnoopFilterName_Type()
)
trpzApConfRp32SnoopfSnoopFilterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApConfRp32SnoopfSnoopFilterName.setStatus("current")
_TrpzApConfRp32SnoopfRowStatus_Type = RowStatus
_TrpzApConfRp32SnoopfRowStatus_Object = MibTableColumn
trpzApConfRp32SnoopfRowStatus = _TrpzApConfRp32SnoopfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 1, 16, 1, 3),
    _TrpzApConfRp32SnoopfRowStatus_Type()
)
trpzApConfRp32SnoopfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trpzApConfRp32SnoopfRowStatus.setStatus("current")
_TrpzApConfigConformance_ObjectIdentity = ObjectIdentity
trpzApConfigConformance = _TrpzApConfigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2)
)
_TrpzApConfigCompliances_ObjectIdentity = ObjectIdentity
trpzApConfigCompliances = _TrpzApConfigCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 1)
)
_TrpzApConfigGroups_ObjectIdentity = ObjectIdentity
trpzApConfigGroups = _TrpzApConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2)
)

# Managed Objects groups

trpzApConfApConfigTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 1)
)
trpzApConfApConfigTableGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigApAttachType"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigPhysPortNum"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigApSerialNum"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigApModelName"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigFingerprint"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigBias"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigApTimeout"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigApName"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigContact"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigLocation"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigBlinkEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigForceImageDownloadEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigFirmwareUpgradeEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigLocalSwitchingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigPowerMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigLedMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigDescription"))
)
if mibBuilder.loadTexts:
    trpzApConfApConfigTableGroup.setStatus("obsolete")

trpzApConfRadioConfigTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 2)
)
trpzApConfRadioConfigTableGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigRadioType"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigRadioMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigRadioProfileName"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigChannel"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigTxPower"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigAutoTuneMaxTxPower"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigAntennaType"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigAntennaLocation"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigLoadBalancingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigLoadBalancingGroup"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigLoadRebalancingEnabled"))
)
if mibBuilder.loadTexts:
    trpzApConfRadioConfigTableGroup.setStatus("obsolete")

trpzApConfApTemplateConfigTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 3)
)
trpzApConfApTemplateConfigTableGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApTemplConfApTemplateEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApTemplConfBias"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApTemplConfApTimeout"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApTemplConfBlinkEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApTemplConfForceImageDownloadEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApTemplConfFirmwareUpgradeEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApTemplConfLocalSwitchingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApTemplConfPowerMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApTemplConfLedMode"))
)
if mibBuilder.loadTexts:
    trpzApConfApTemplateConfigTableGroup.setStatus("current")

trpzApConfApTemplateRadioConfigTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 4)
)
trpzApConfApTemplateRadioConfigTableGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApTemRadioConfRadioMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApTemRadioConfRadioProfileName"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApTemRadioConfAutoTuneMaxTxPower"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApTemRadioConfLoadBalancingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApTemRadioConfLoadBalancingGroup"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApTemRadioConfLoadRebalancingEnabled"))
)
if mibBuilder.loadTexts:
    trpzApConfApTemplateRadioConfigTableGroup.setStatus("obsolete")

trpzApConfRadioProfileTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 5)
)
trpzApConfRadioProfileTableGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfBeaconInterval"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfDtimInterval"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfChannelWidth11na"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfMaxTxLifetime"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfMaxRxLifetime"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfRtsThreshold"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfFragThreshold"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfLongXmitPreambleEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCountermeasuresMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfRFScanMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfRFScanChannelScope"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfRFScanCTSEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfAutoTune11aChannelRange"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfAutoTuneIgnoreClientsEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfAutoTuneChannelEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfAutoTuneChannelHolddownInterval"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfAutoTuneChannelChangeInterval"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfAutoTunePowerEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfAutoTunePowerRampInterval"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfAutoTunePowerChangeInterval"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfFairQueuingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCacBackgroundACMandatory"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCacBackgroundMaxUtilization"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCacBackgroundPolicingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCacBestEffortACMandatory"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCacBestEffortMaxUtilization"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCacBestEffortPolicingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCacVideoACMandatory"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCacVideoMaxUtilization"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCacVideoPolicingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCacVoiceACMandatory"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCacVoiceMaxUtilization"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCacVoicePolicingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfRfidTagEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfWmmPowerSaveEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfRateEnforcementEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfDfsChannelsEnabled"))
)
if mibBuilder.loadTexts:
    trpzApConfRadioProfileTableGroup.setStatus("obsolete")

trpzApConfRadioProfServiceProfileTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 6)
)
trpzApConfRadioProfServiceProfileTableGroup.setObjects(
    ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRpServpRowStatus")
)
if mibBuilder.loadTexts:
    trpzApConfRadioProfServiceProfileTableGroup.setStatus("obsolete")

trpzApConfRadioProfSnoopFilterTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 7)
)
trpzApConfRadioProfSnoopFilterTableGroup.setObjects(
    ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRpSnoopfRowStatus")
)
if mibBuilder.loadTexts:
    trpzApConfRadioProfSnoopFilterTableGroup.setStatus("obsolete")

trpzApConfServiceProfileTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 8)
)
trpzApConfServiceProfileTableGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfSsidType"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfBeaconEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProf11naMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProf11ngMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProf11nShortGuardIntervalEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProf11nFrameAggregation"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProf11nMsduMaxLength"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProf11nMpduMaxLength"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfAuthFallthru"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWebAAAForm"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfSharedKeyAuthEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWpaIeEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWpaIeCipherTkipEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWpaIeCipherCcmpEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWpaIeCipherWep40Enabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWpaIeCipherWep104Enabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWpaIeAuthDot1xEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWpaIeAuthPskEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfRsnIeEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfRsnIeCipherTkipEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfRsnIeCipherCcmpEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfRsnIeCipherWep40Enabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfRsnIeCipherWep104Enabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfRsnIeAuthDot1xEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfRsnIeAuthPskEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfTkipMicCountermeasuresTime"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfMaxBandwidthKbps"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfCacMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfCacSessCount"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfUserIdleTimeout"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfIdleClientProbingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfShortRetryCount"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfLongRetryCount"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfProxyArpEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfDhcpRestrictEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfNoBroadcastEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfSygateOnDemandEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfEnforceChecksEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfSodaRemediationAcl"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfSodaSuccessPage"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfSodaFailurePage"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfSodaLogoutPage"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfSodaAgentDirectory"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWebPortalSessionTimeout"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWebPortalAcl"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWebPortalLogoutEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWebPortalLogoutUrl"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfKeepInitialVlanEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfMeshModeEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfBridgingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfLoadBalanceExemptEnabled"))
)
if mibBuilder.loadTexts:
    trpzApConfServiceProfileTableGroup.setStatus("obsolete")

trpzApConfSnoopFilterTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 9)
)
trpzApConfSnoopFilterTableGroup.setObjects(
    ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfSnoopFilterEnabled")
)
if mibBuilder.loadTexts:
    trpzApConfSnoopFilterTableGroup.setStatus("obsolete")

trpzApConfServiceProfileTableGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 10)
)
trpzApConfServiceProfileTableGroupRev2.setObjects(
      *(("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfSsidType"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfBeaconEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProf11naMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProf11ngMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProf11nShortGuardIntervalEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProf11nFrameAggregation"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProf11nMsduMaxLength"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProf11nMpduMaxLength"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfAuthFallthru"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWebAAAForm"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfSharedKeyAuthEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWpaIeEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWpaIeCipherTkipEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWpaIeCipherCcmpEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWpaIeAuthDot1xEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWpaIeAuthPskEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfRsnIeEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfRsnIeCipherTkipEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfRsnIeCipherCcmpEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfRsnIeAuthDot1xEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfRsnIeAuthPskEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfTkipMicCountermeasuresTime"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfMaxBandwidthKbps"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfCacMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfCacSessCount"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfUserIdleTimeout"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfIdleClientProbingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfShortRetryCount"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfLongRetryCount"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfProxyArpEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfDhcpRestrictEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfNoBroadcastEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfSygateOnDemandEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfEnforceChecksEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfSodaRemediationAcl"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfSodaSuccessPage"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfSodaFailurePage"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfSodaLogoutPage"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfSodaAgentDirectory"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWebPortalSessionTimeout"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWebPortalAcl"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWebPortalLogoutEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWebPortalLogoutUrl"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfKeepInitialVlanEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfMeshModeEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfBridgingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfLoadBalanceExemptEnabled"))
)
if mibBuilder.loadTexts:
    trpzApConfServiceProfileTableGroupRev2.setStatus("obsolete")

trpzApConfApConfigLldpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 11)
)
trpzApConfApConfigLldpGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigLldpMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigLldpMedEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigLldpMedExtPowerViaMdiTlvSelected"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigLldpMedInventoryTlvSelected"))
)
if mibBuilder.loadTexts:
    trpzApConfApConfigLldpGroup.setStatus("current")

trpzApConfApConfigTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 12)
)
trpzApConfApConfigTunnelGroup.setObjects(
    ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigApTunnelEnabled")
)
if mibBuilder.loadTexts:
    trpzApConfApConfigTunnelGroup.setStatus("current")

trpzApConfApConfigRemoteApGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 13)
)
trpzApConfApConfigRemoteApGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigDataSecurityEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigWanOutageModeEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigWanOutageExtendedTimeout"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigWanOutageEvaluationPeriod"))
)
if mibBuilder.loadTexts:
    trpzApConfApConfigRemoteApGroup.setStatus("current")

trpzApConfRadioProfileRFSpectralScanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 14)
)
trpzApConfRadioProfileRFSpectralScanGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfRFSpectralScanModeEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfRFSpectralScanPriority"))
)
if mibBuilder.loadTexts:
    trpzApConfRadioProfileRFSpectralScanGroup.setStatus("obsolete")

trpzApConfApConfigTableGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 15)
)
trpzApConfApConfigTableGroupRev2.setObjects(
      *(("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigApAttachType"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigPhysPortNum"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigApSerialNum"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigApModelName"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigFingerprint"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigBias"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigApTimeout"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigApName"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigContact"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigLocation"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigBlinkEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigForceImageDownloadEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigFirmwareUpgradeEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigLocalSwitchingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigPowerMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigLedMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigDescription"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigRemoteSiteName"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigPathMtu"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigHighLatencyModeEnabled"))
)
if mibBuilder.loadTexts:
    trpzApConfApConfigTableGroupRev2.setStatus("obsolete")

trpzApConfSnoopFilterTableGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 16)
)
trpzApConfSnoopFilterTableGroupRev2.setObjects(
      *(("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfSnoopFilterEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfSnoopFilterObserverAddrType"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfSnoopFilterObserverAddr"))
)
if mibBuilder.loadTexts:
    trpzApConfSnoopFilterTableGroupRev2.setStatus("current")

trpzApConfSnoopObserverTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 17)
)
trpzApConfSnoopObserverTableGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfSnoopObserverSnapLength"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfSnoopObserverInterval"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfSnoopObserverTxMode"))
)
if mibBuilder.loadTexts:
    trpzApConfSnoopObserverTableGroup.setStatus("current")

trpzApConfRadioSnoopFilterTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 18)
)
trpzApConfRadioSnoopFilterTableGroup.setObjects(
    ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioSnoopFilterRowStatus")
)
if mibBuilder.loadTexts:
    trpzApConfRadioSnoopFilterTableGroup.setStatus("current")

trpzApConfServiceProfileTableGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 19)
)
trpzApConfServiceProfileTableGroupRev3.setObjects(
      *(("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfSsidType"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfBeaconEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProf11naMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProf11ngMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProf11nShortGuardIntervalEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProf11nFrameAggregation"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProf11nMsduMaxLength"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProf11nMpduMaxLength"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfAuthFallthru"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWebAAAForm"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWebPortalLogoutForm"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfSharedKeyAuthEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWpaIeEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWpaIeCipherTkipEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWpaIeCipherCcmpEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWpaIeAuthDot1xEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWpaIeAuthPskEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfRsnIeEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfRsnIeCipherTkipEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfRsnIeCipherCcmpEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfRsnIeAuthDot1xEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfRsnIeAuthPskEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfTkipMicCountermeasuresTime"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfMaxBandwidthKbps"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfCacMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfCacSessCount"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfUserIdleTimeout"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfIdleClientProbingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfShortRetryCount"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfLongRetryCount"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfProxyArpEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfDhcpRestrictEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfNoBroadcastEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfSygateOnDemandEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfEnforceChecksEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfSodaRemediationAcl"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfSodaSuccessPage"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfSodaFailurePage"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfSodaLogoutPage"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfSodaAgentDirectory"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWebPortalSessionTimeout"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWebPortalAcl"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWebPortalLogoutEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfWebPortalLogoutUrl"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfKeepInitialVlanEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfMeshModeEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfBridgingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfLoadBalanceExemptEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfM2UConversionEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfBackupSsidMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfBackupSsidTimeout"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfServProfBackupSsidKeepClients"))
)
if mibBuilder.loadTexts:
    trpzApConfServiceProfileTableGroupRev3.setStatus("current")

trpzApConfRemoteSiteTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 20)
)
trpzApConfRemoteSiteTableGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRemoteSiteCountryCode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRemoteSitePathMtu"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRemoteSiteBackupSsidsEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRemoteSiteLogServerEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRemoteSiteLogServerAddrType"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRemoteSiteLogServerAddr"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRemoteSiteLogServerPort"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRemoteSiteLogServerSeverity"))
)
if mibBuilder.loadTexts:
    trpzApConfRemoteSiteTableGroup.setStatus("obsolete")

trpzApConfRadioProfileTableGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 21)
)
trpzApConfRadioProfileTableGroupRev2.setObjects(
      *(("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfBeaconInterval"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfDtimInterval"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfChannelWidth11na"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfMaxTxLifetime"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfMaxRxLifetime"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfRtsThreshold"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfFragThreshold"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfLongXmitPreambleEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCountermeasuresMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfRFScanMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfRFScanChannelScope"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfRFScanCTSEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfAutoTunePowerEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfAutoTunePowerRampInterval"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfAutoTunePowerChangeInterval"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfFairQueuingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCacBackgroundACMandatory"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCacBackgroundMaxUtilization"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCacBackgroundPolicingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCacBestEffortACMandatory"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCacBestEffortMaxUtilization"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCacBestEffortPolicingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCacVideoACMandatory"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCacVideoMaxUtilization"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCacVideoPolicingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCacVoiceACMandatory"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCacVoiceMaxUtilization"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfCacVoicePolicingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfRfidTagEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfWmmPowerSaveEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfRateEnforcementEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProfDfsChannelsEnabled"))
)
if mibBuilder.loadTexts:
    trpzApConfRadioProfileTableGroupRev2.setStatus("obsolete")

trpzApConfApConfigTableGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 22)
)
trpzApConfApConfigTableGroupRev3.setObjects(
      *(("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigApAttachType"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigPhysPortNum"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigApSerialNum"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigApModelName"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigFingerprint"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigBias"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigApTimeout"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigContact"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigLocation"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigBlinkEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigForceImageDownloadEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigFirmwareUpgradeEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigLocalSwitchingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigPowerMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigLedMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigDescription"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigRemoteSiteName"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigPathMtu"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigHighLatencyModeEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigApName2"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApConfigCacheConfigEnabled"))
)
if mibBuilder.loadTexts:
    trpzApConfApConfigTableGroupRev3.setStatus("current")

trpzApConfRadioConfigTableGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 23)
)
trpzApConfRadioConfigTableGroupRev2.setObjects(
      *(("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigRadioType"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigRadioMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigChannel"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigTxPower"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigAntennaType"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigAntennaLocation"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigLoadBalancingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigLoadBalancingGroup"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigLoadRebalancingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioConfigRadioProfileName2"))
)
if mibBuilder.loadTexts:
    trpzApConfRadioConfigTableGroupRev2.setStatus("current")

trpzApConfApTemplateRadioConfigTableGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 24)
)
trpzApConfApTemplateRadioConfigTableGroupRev2.setObjects(
      *(("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApTemRadioConfRadioMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApTemRadioConfLoadBalancingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApTemRadioConfLoadBalancingGroup"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApTemRadioConfLoadRebalancingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfApTemRadioConfRadioProfileName2"))
)
if mibBuilder.loadTexts:
    trpzApConfApTemplateRadioConfigTableGroupRev2.setStatus("current")

trpzApConfRadioProfile32TableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 25)
)
trpzApConfRadioProfile32TableGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32BeaconInterval"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32DtimInterval"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32ChannelWidth11na"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32MaxTxLifetime"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32MaxRxLifetime"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32RtsThreshold"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32FragThreshold"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32LongXmitPreambleEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32CountermeasuresMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32RFScanMode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32RFScanChannelScope"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32RFScanCTSEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32AutoTunePowerEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32AutoTunePowerRampInterval"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32AutoTunePowerChangeInterval"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32FairQueuingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32CacBackgroundACMandatory"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32CacBackgroundMaxUtilization"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32CacBackgroundPolicingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32CacBestEffortACMandatory"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32CacBestEffortMaxUtilization"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32CacBestEffortPolicingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32CacVideoACMandatory"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32CacVideoMaxUtilization"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32CacVideoPolicingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32CacVoiceACMandatory"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32CacVoiceMaxUtilization"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32CacVoicePolicingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32RfidTagEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32WmmPowerSaveEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32RateEnforcementEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32DfsChannelsEnabled"))
)
if mibBuilder.loadTexts:
    trpzApConfRadioProfile32TableGroup.setStatus("current")

trpzApConfRadioProfileRFSpectralScanGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 26)
)
trpzApConfRadioProfileRFSpectralScanGroupRev2.setObjects(
      *(("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32RFSpectralScanModeEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRadioProf32RFSpectralScanPriority"))
)
if mibBuilder.loadTexts:
    trpzApConfRadioProfileRFSpectralScanGroupRev2.setStatus("current")

trpzApConfRadioProf32ServiceProfileTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 27)
)
trpzApConfRadioProf32ServiceProfileTableGroup.setObjects(
    ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRp32ServpRowStatus")
)
if mibBuilder.loadTexts:
    trpzApConfRadioProf32ServiceProfileTableGroup.setStatus("current")

trpzApConfRadioProf32SnoopFilterTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 28)
)
trpzApConfRadioProf32SnoopFilterTableGroup.setObjects(
    ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRp32SnoopfRowStatus")
)
if mibBuilder.loadTexts:
    trpzApConfRadioProf32SnoopFilterTableGroup.setStatus("current")

trpzApConfRemoteSiteTableGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 2, 29)
)
trpzApConfRemoteSiteTableGroupRev2.setObjects(
      *(("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRemoteSiteCountryCode"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRemoteSitePathMtu"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRemoteSiteBackupSsidsEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRemoteSiteLogServerEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRemoteSiteLogServerAddrType"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRemoteSiteLogServerAddr"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRemoteSiteLogServerPort"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRemoteSiteLogServerSeverity"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRemoteSiteAcPollingEnabled"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRemoteSiteRadiusServerGroupName"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRemoteSiteRadiusDeadtime"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRemoteSiteRadiusTimeout"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRemoteSiteRadiusRetransmit"),
        ("TRAPEZE-NETWORKS-AP-CONFIG-MIB", "trpzApConfRemoteSiteRadiusNasIdType"))
)
if mibBuilder.loadTexts:
    trpzApConfRemoteSiteTableGroupRev2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

trpzApConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 1, 1)
)
if mibBuilder.loadTexts:
    trpzApConfigCompliance.setStatus(
        "obsolete"
    )

trpzApConfigComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 1, 2)
)
if mibBuilder.loadTexts:
    trpzApConfigComplianceRev2.setStatus(
        "obsolete"
    )

trpzApConfigComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 1, 3)
)
if mibBuilder.loadTexts:
    trpzApConfigComplianceRev3.setStatus(
        "obsolete"
    )

trpzApConfigComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 1, 4)
)
if mibBuilder.loadTexts:
    trpzApConfigComplianceRev4.setStatus(
        "obsolete"
    )

trpzApConfigComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 14, 2, 1, 5)
)
if mibBuilder.loadTexts:
    trpzApConfigComplianceRev5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAPEZE-NETWORKS-AP-CONFIG-MIB",
    **{"TrpzApTemplateName": TrpzApTemplateName,
       "TrpzRadioProfileName": TrpzRadioProfileName,
       "TrpzServiceProfileName": TrpzServiceProfileName,
       "TrpzSnoopFilterName": TrpzSnoopFilterName,
       "TrpzServiceProfileSsidType": TrpzServiceProfileSsidType,
       "TrpzServiceProfile11nMode": TrpzServiceProfile11nMode,
       "TrpzServiceProfile11nFrameAggregationType": TrpzServiceProfile11nFrameAggregationType,
       "TrpzServiceProfile11nMsduMaxLength": TrpzServiceProfile11nMsduMaxLength,
       "TrpzServiceProfile11nMpduMaxLength": TrpzServiceProfile11nMpduMaxLength,
       "TrpzServiceProfileAuthFallthruType": TrpzServiceProfileAuthFallthruType,
       "TrpzServiceProfileCacMode": TrpzServiceProfileCacMode,
       "TrpzRadioProfileCountermeasuresMode": TrpzRadioProfileCountermeasuresMode,
       "TrpzRadioProfileRFScanChannelScope": TrpzRadioProfileRFScanChannelScope,
       "TrpzRadioProfileAutoTuneChannelRange": TrpzRadioProfileAutoTuneChannelRange,
       "TrpzRadioProfileRFScanMode": TrpzRadioProfileRFScanMode,
       "TrpzApLldpMode": TrpzApLldpMode,
       "TrpzRadioProfileRFSpectralScanPriority": TrpzRadioProfileRFSpectralScanPriority,
       "TrpzBackupSsidMode": TrpzBackupSsidMode,
       "TrpzSnoopObserverTxMode": TrpzSnoopObserverTxMode,
       "TrpzRadioProfileName32": TrpzRadioProfileName32,
       "TrpzApRadiusNasIdType": TrpzApRadiusNasIdType,
       "trpzApConfigMib": trpzApConfigMib,
       "trpzApConfigMibObjects": trpzApConfigMibObjects,
       "trpzApConfApConfigTable": trpzApConfApConfigTable,
       "trpzApConfApConfigEntry": trpzApConfApConfigEntry,
       "trpzApConfApConfigApNum": trpzApConfApConfigApNum,
       "trpzApConfApConfigApAttachType": trpzApConfApConfigApAttachType,
       "trpzApConfApConfigPhysPortNum": trpzApConfApConfigPhysPortNum,
       "trpzApConfApConfigApSerialNum": trpzApConfApConfigApSerialNum,
       "trpzApConfApConfigApModelName": trpzApConfApConfigApModelName,
       "trpzApConfApConfigFingerprint": trpzApConfApConfigFingerprint,
       "trpzApConfApConfigBias": trpzApConfApConfigBias,
       "trpzApConfApConfigApTimeout": trpzApConfApConfigApTimeout,
       "trpzApConfApConfigApName": trpzApConfApConfigApName,
       "trpzApConfApConfigContact": trpzApConfApConfigContact,
       "trpzApConfApConfigLocation": trpzApConfApConfigLocation,
       "trpzApConfApConfigBlinkEnabled": trpzApConfApConfigBlinkEnabled,
       "trpzApConfApConfigForceImageDownloadEnabled": trpzApConfApConfigForceImageDownloadEnabled,
       "trpzApConfApConfigFirmwareUpgradeEnabled": trpzApConfApConfigFirmwareUpgradeEnabled,
       "trpzApConfApConfigLocalSwitchingEnabled": trpzApConfApConfigLocalSwitchingEnabled,
       "trpzApConfApConfigPowerMode": trpzApConfApConfigPowerMode,
       "trpzApConfApConfigLedMode": trpzApConfApConfigLedMode,
       "trpzApConfApConfigDescription": trpzApConfApConfigDescription,
       "trpzApConfApConfigLldpMode": trpzApConfApConfigLldpMode,
       "trpzApConfApConfigLldpMedEnabled": trpzApConfApConfigLldpMedEnabled,
       "trpzApConfApConfigLldpMedExtPowerViaMdiTlvSelected": trpzApConfApConfigLldpMedExtPowerViaMdiTlvSelected,
       "trpzApConfApConfigLldpMedInventoryTlvSelected": trpzApConfApConfigLldpMedInventoryTlvSelected,
       "trpzApConfApConfigApTunnelEnabled": trpzApConfApConfigApTunnelEnabled,
       "trpzApConfApConfigDataSecurityEnabled": trpzApConfApConfigDataSecurityEnabled,
       "trpzApConfApConfigWanOutageModeEnabled": trpzApConfApConfigWanOutageModeEnabled,
       "trpzApConfApConfigWanOutageExtendedTimeout": trpzApConfApConfigWanOutageExtendedTimeout,
       "trpzApConfApConfigWanOutageEvaluationPeriod": trpzApConfApConfigWanOutageEvaluationPeriod,
       "trpzApConfApConfigRemoteSiteName": trpzApConfApConfigRemoteSiteName,
       "trpzApConfApConfigPathMtu": trpzApConfApConfigPathMtu,
       "trpzApConfApConfigHighLatencyModeEnabled": trpzApConfApConfigHighLatencyModeEnabled,
       "trpzApConfApConfigApName2": trpzApConfApConfigApName2,
       "trpzApConfApConfigCacheConfigEnabled": trpzApConfApConfigCacheConfigEnabled,
       "trpzApConfRadioConfigTable": trpzApConfRadioConfigTable,
       "trpzApConfRadioConfigEntry": trpzApConfRadioConfigEntry,
       "trpzApConfRadioConfigApNum": trpzApConfRadioConfigApNum,
       "trpzApConfRadioConfigRadioIndex": trpzApConfRadioConfigRadioIndex,
       "trpzApConfRadioConfigRadioType": trpzApConfRadioConfigRadioType,
       "trpzApConfRadioConfigRadioMode": trpzApConfRadioConfigRadioMode,
       "trpzApConfRadioConfigRadioProfileName": trpzApConfRadioConfigRadioProfileName,
       "trpzApConfRadioConfigChannel": trpzApConfRadioConfigChannel,
       "trpzApConfRadioConfigTxPower": trpzApConfRadioConfigTxPower,
       "trpzApConfRadioConfigAutoTuneMaxTxPower": trpzApConfRadioConfigAutoTuneMaxTxPower,
       "trpzApConfRadioConfigAntennaType": trpzApConfRadioConfigAntennaType,
       "trpzApConfRadioConfigAntennaLocation": trpzApConfRadioConfigAntennaLocation,
       "trpzApConfRadioConfigLoadBalancingEnabled": trpzApConfRadioConfigLoadBalancingEnabled,
       "trpzApConfRadioConfigLoadBalancingGroup": trpzApConfRadioConfigLoadBalancingGroup,
       "trpzApConfRadioConfigLoadRebalancingEnabled": trpzApConfRadioConfigLoadRebalancingEnabled,
       "trpzApConfRadioConfigRadioProfileName2": trpzApConfRadioConfigRadioProfileName2,
       "trpzApConfApTemplateConfigTable": trpzApConfApTemplateConfigTable,
       "trpzApConfApTemplateConfigEntry": trpzApConfApTemplateConfigEntry,
       "trpzApConfApTemplConfApTemplateName": trpzApConfApTemplConfApTemplateName,
       "trpzApConfApTemplConfApTemplateEnabled": trpzApConfApTemplConfApTemplateEnabled,
       "trpzApConfApTemplConfBias": trpzApConfApTemplConfBias,
       "trpzApConfApTemplConfApTimeout": trpzApConfApTemplConfApTimeout,
       "trpzApConfApTemplConfBlinkEnabled": trpzApConfApTemplConfBlinkEnabled,
       "trpzApConfApTemplConfForceImageDownloadEnabled": trpzApConfApTemplConfForceImageDownloadEnabled,
       "trpzApConfApTemplConfFirmwareUpgradeEnabled": trpzApConfApTemplConfFirmwareUpgradeEnabled,
       "trpzApConfApTemplConfLocalSwitchingEnabled": trpzApConfApTemplConfLocalSwitchingEnabled,
       "trpzApConfApTemplConfPowerMode": trpzApConfApTemplConfPowerMode,
       "trpzApConfApTemplConfLedMode": trpzApConfApTemplConfLedMode,
       "trpzApConfApTemplateRadioConfigTable": trpzApConfApTemplateRadioConfigTable,
       "trpzApConfApTemplateRadioConfigEntry": trpzApConfApTemplateRadioConfigEntry,
       "trpzApConfApTemRadioConfApTemplateName": trpzApConfApTemRadioConfApTemplateName,
       "trpzApConfApTemRadioConfRadioIndex": trpzApConfApTemRadioConfRadioIndex,
       "trpzApConfApTemRadioConfRadioMode": trpzApConfApTemRadioConfRadioMode,
       "trpzApConfApTemRadioConfRadioProfileName": trpzApConfApTemRadioConfRadioProfileName,
       "trpzApConfApTemRadioConfAutoTuneMaxTxPower": trpzApConfApTemRadioConfAutoTuneMaxTxPower,
       "trpzApConfApTemRadioConfLoadBalancingEnabled": trpzApConfApTemRadioConfLoadBalancingEnabled,
       "trpzApConfApTemRadioConfLoadBalancingGroup": trpzApConfApTemRadioConfLoadBalancingGroup,
       "trpzApConfApTemRadioConfLoadRebalancingEnabled": trpzApConfApTemRadioConfLoadRebalancingEnabled,
       "trpzApConfApTemRadioConfRadioProfileName2": trpzApConfApTemRadioConfRadioProfileName2,
       "trpzApConfRadioProfileTable": trpzApConfRadioProfileTable,
       "trpzApConfRadioProfileEntry": trpzApConfRadioProfileEntry,
       "trpzApConfRadioProfRadioProfileName": trpzApConfRadioProfRadioProfileName,
       "trpzApConfRadioProfBeaconInterval": trpzApConfRadioProfBeaconInterval,
       "trpzApConfRadioProfDtimInterval": trpzApConfRadioProfDtimInterval,
       "trpzApConfRadioProfChannelWidth11na": trpzApConfRadioProfChannelWidth11na,
       "trpzApConfRadioProfMaxTxLifetime": trpzApConfRadioProfMaxTxLifetime,
       "trpzApConfRadioProfMaxRxLifetime": trpzApConfRadioProfMaxRxLifetime,
       "trpzApConfRadioProfRtsThreshold": trpzApConfRadioProfRtsThreshold,
       "trpzApConfRadioProfFragThreshold": trpzApConfRadioProfFragThreshold,
       "trpzApConfRadioProfLongXmitPreambleEnabled": trpzApConfRadioProfLongXmitPreambleEnabled,
       "trpzApConfRadioProfCountermeasuresMode": trpzApConfRadioProfCountermeasuresMode,
       "trpzApConfRadioProfRFScanMode": trpzApConfRadioProfRFScanMode,
       "trpzApConfRadioProfRFScanChannelScope": trpzApConfRadioProfRFScanChannelScope,
       "trpzApConfRadioProfRFScanCTSEnabled": trpzApConfRadioProfRFScanCTSEnabled,
       "trpzApConfRadioProfAutoTune11aChannelRange": trpzApConfRadioProfAutoTune11aChannelRange,
       "trpzApConfRadioProfAutoTuneIgnoreClientsEnabled": trpzApConfRadioProfAutoTuneIgnoreClientsEnabled,
       "trpzApConfRadioProfAutoTuneChannelEnabled": trpzApConfRadioProfAutoTuneChannelEnabled,
       "trpzApConfRadioProfAutoTuneChannelHolddownInterval": trpzApConfRadioProfAutoTuneChannelHolddownInterval,
       "trpzApConfRadioProfAutoTuneChannelChangeInterval": trpzApConfRadioProfAutoTuneChannelChangeInterval,
       "trpzApConfRadioProfAutoTunePowerEnabled": trpzApConfRadioProfAutoTunePowerEnabled,
       "trpzApConfRadioProfAutoTunePowerRampInterval": trpzApConfRadioProfAutoTunePowerRampInterval,
       "trpzApConfRadioProfAutoTunePowerChangeInterval": trpzApConfRadioProfAutoTunePowerChangeInterval,
       "trpzApConfRadioProfFairQueuingEnabled": trpzApConfRadioProfFairQueuingEnabled,
       "trpzApConfRadioProfCacBackgroundACMandatory": trpzApConfRadioProfCacBackgroundACMandatory,
       "trpzApConfRadioProfCacBackgroundMaxUtilization": trpzApConfRadioProfCacBackgroundMaxUtilization,
       "trpzApConfRadioProfCacBackgroundPolicingEnabled": trpzApConfRadioProfCacBackgroundPolicingEnabled,
       "trpzApConfRadioProfCacBestEffortACMandatory": trpzApConfRadioProfCacBestEffortACMandatory,
       "trpzApConfRadioProfCacBestEffortMaxUtilization": trpzApConfRadioProfCacBestEffortMaxUtilization,
       "trpzApConfRadioProfCacBestEffortPolicingEnabled": trpzApConfRadioProfCacBestEffortPolicingEnabled,
       "trpzApConfRadioProfCacVideoACMandatory": trpzApConfRadioProfCacVideoACMandatory,
       "trpzApConfRadioProfCacVideoMaxUtilization": trpzApConfRadioProfCacVideoMaxUtilization,
       "trpzApConfRadioProfCacVideoPolicingEnabled": trpzApConfRadioProfCacVideoPolicingEnabled,
       "trpzApConfRadioProfCacVoiceACMandatory": trpzApConfRadioProfCacVoiceACMandatory,
       "trpzApConfRadioProfCacVoiceMaxUtilization": trpzApConfRadioProfCacVoiceMaxUtilization,
       "trpzApConfRadioProfCacVoicePolicingEnabled": trpzApConfRadioProfCacVoicePolicingEnabled,
       "trpzApConfRadioProfRfidTagEnabled": trpzApConfRadioProfRfidTagEnabled,
       "trpzApConfRadioProfWmmPowerSaveEnabled": trpzApConfRadioProfWmmPowerSaveEnabled,
       "trpzApConfRadioProfRateEnforcementEnabled": trpzApConfRadioProfRateEnforcementEnabled,
       "trpzApConfRadioProfDfsChannelsEnabled": trpzApConfRadioProfDfsChannelsEnabled,
       "trpzApConfRadioProfRFSpectralScanModeEnabled": trpzApConfRadioProfRFSpectralScanModeEnabled,
       "trpzApConfRadioProfRFSpectralScanPriority": trpzApConfRadioProfRFSpectralScanPriority,
       "trpzApConfRadioProfRadioProfileFullName": trpzApConfRadioProfRadioProfileFullName,
       "trpzApConfRadioProfServiceProfileTable": trpzApConfRadioProfServiceProfileTable,
       "trpzApConfRadioProfServiceProfileEntry": trpzApConfRadioProfServiceProfileEntry,
       "trpzApConfRpServpRadioProfileName": trpzApConfRpServpRadioProfileName,
       "trpzApConfRpServpServiceProfileName": trpzApConfRpServpServiceProfileName,
       "trpzApConfRpServpRowStatus": trpzApConfRpServpRowStatus,
       "trpzApConfRadioProfSnoopFilterTable": trpzApConfRadioProfSnoopFilterTable,
       "trpzApConfRadioProfSnoopFilterEntry": trpzApConfRadioProfSnoopFilterEntry,
       "trpzApConfRpSnoopfRadioProfileName": trpzApConfRpSnoopfRadioProfileName,
       "trpzApConfRpSnoopfSnoopFilterName": trpzApConfRpSnoopfSnoopFilterName,
       "trpzApConfRpSnoopfRowStatus": trpzApConfRpSnoopfRowStatus,
       "trpzApConfServiceProfileTable": trpzApConfServiceProfileTable,
       "trpzApConfServiceProfileEntry": trpzApConfServiceProfileEntry,
       "trpzApConfServProfServiceProfileName": trpzApConfServProfServiceProfileName,
       "trpzApConfServProfSsidType": trpzApConfServProfSsidType,
       "trpzApConfServProfBeaconEnabled": trpzApConfServProfBeaconEnabled,
       "trpzApConfServProf11naMode": trpzApConfServProf11naMode,
       "trpzApConfServProf11ngMode": trpzApConfServProf11ngMode,
       "trpzApConfServProf11nShortGuardIntervalEnabled": trpzApConfServProf11nShortGuardIntervalEnabled,
       "trpzApConfServProf11nFrameAggregation": trpzApConfServProf11nFrameAggregation,
       "trpzApConfServProf11nMsduMaxLength": trpzApConfServProf11nMsduMaxLength,
       "trpzApConfServProf11nMpduMaxLength": trpzApConfServProf11nMpduMaxLength,
       "trpzApConfServProfAuthFallthru": trpzApConfServProfAuthFallthru,
       "trpzApConfServProfWebAAAForm": trpzApConfServProfWebAAAForm,
       "trpzApConfServProfSharedKeyAuthEnabled": trpzApConfServProfSharedKeyAuthEnabled,
       "trpzApConfServProfWpaIeEnabled": trpzApConfServProfWpaIeEnabled,
       "trpzApConfServProfWpaIeCipherTkipEnabled": trpzApConfServProfWpaIeCipherTkipEnabled,
       "trpzApConfServProfWpaIeCipherCcmpEnabled": trpzApConfServProfWpaIeCipherCcmpEnabled,
       "trpzApConfServProfWpaIeCipherWep40Enabled": trpzApConfServProfWpaIeCipherWep40Enabled,
       "trpzApConfServProfWpaIeCipherWep104Enabled": trpzApConfServProfWpaIeCipherWep104Enabled,
       "trpzApConfServProfWpaIeAuthDot1xEnabled": trpzApConfServProfWpaIeAuthDot1xEnabled,
       "trpzApConfServProfWpaIeAuthPskEnabled": trpzApConfServProfWpaIeAuthPskEnabled,
       "trpzApConfServProfRsnIeEnabled": trpzApConfServProfRsnIeEnabled,
       "trpzApConfServProfRsnIeCipherTkipEnabled": trpzApConfServProfRsnIeCipherTkipEnabled,
       "trpzApConfServProfRsnIeCipherCcmpEnabled": trpzApConfServProfRsnIeCipherCcmpEnabled,
       "trpzApConfServProfRsnIeCipherWep40Enabled": trpzApConfServProfRsnIeCipherWep40Enabled,
       "trpzApConfServProfRsnIeCipherWep104Enabled": trpzApConfServProfRsnIeCipherWep104Enabled,
       "trpzApConfServProfRsnIeAuthDot1xEnabled": trpzApConfServProfRsnIeAuthDot1xEnabled,
       "trpzApConfServProfRsnIeAuthPskEnabled": trpzApConfServProfRsnIeAuthPskEnabled,
       "trpzApConfServProfTkipMicCountermeasuresTime": trpzApConfServProfTkipMicCountermeasuresTime,
       "trpzApConfServProfMaxBandwidthKbps": trpzApConfServProfMaxBandwidthKbps,
       "trpzApConfServProfCacMode": trpzApConfServProfCacMode,
       "trpzApConfServProfCacSessCount": trpzApConfServProfCacSessCount,
       "trpzApConfServProfUserIdleTimeout": trpzApConfServProfUserIdleTimeout,
       "trpzApConfServProfIdleClientProbingEnabled": trpzApConfServProfIdleClientProbingEnabled,
       "trpzApConfServProfShortRetryCount": trpzApConfServProfShortRetryCount,
       "trpzApConfServProfLongRetryCount": trpzApConfServProfLongRetryCount,
       "trpzApConfServProfProxyArpEnabled": trpzApConfServProfProxyArpEnabled,
       "trpzApConfServProfDhcpRestrictEnabled": trpzApConfServProfDhcpRestrictEnabled,
       "trpzApConfServProfNoBroadcastEnabled": trpzApConfServProfNoBroadcastEnabled,
       "trpzApConfServProfSygateOnDemandEnabled": trpzApConfServProfSygateOnDemandEnabled,
       "trpzApConfServProfEnforceChecksEnabled": trpzApConfServProfEnforceChecksEnabled,
       "trpzApConfServProfSodaRemediationAcl": trpzApConfServProfSodaRemediationAcl,
       "trpzApConfServProfSodaSuccessPage": trpzApConfServProfSodaSuccessPage,
       "trpzApConfServProfSodaFailurePage": trpzApConfServProfSodaFailurePage,
       "trpzApConfServProfSodaLogoutPage": trpzApConfServProfSodaLogoutPage,
       "trpzApConfServProfSodaAgentDirectory": trpzApConfServProfSodaAgentDirectory,
       "trpzApConfServProfWebPortalSessionTimeout": trpzApConfServProfWebPortalSessionTimeout,
       "trpzApConfServProfWebPortalAcl": trpzApConfServProfWebPortalAcl,
       "trpzApConfServProfWebPortalLogoutEnabled": trpzApConfServProfWebPortalLogoutEnabled,
       "trpzApConfServProfWebPortalLogoutUrl": trpzApConfServProfWebPortalLogoutUrl,
       "trpzApConfServProfKeepInitialVlanEnabled": trpzApConfServProfKeepInitialVlanEnabled,
       "trpzApConfServProfMeshModeEnabled": trpzApConfServProfMeshModeEnabled,
       "trpzApConfServProfBridgingEnabled": trpzApConfServProfBridgingEnabled,
       "trpzApConfServProfLoadBalanceExemptEnabled": trpzApConfServProfLoadBalanceExemptEnabled,
       "trpzApConfServProfM2UConversionEnabled": trpzApConfServProfM2UConversionEnabled,
       "trpzApConfServProfBackupSsidMode": trpzApConfServProfBackupSsidMode,
       "trpzApConfServProfBackupSsidTimeout": trpzApConfServProfBackupSsidTimeout,
       "trpzApConfServProfBackupSsidKeepClients": trpzApConfServProfBackupSsidKeepClients,
       "trpzApConfServProfWebPortalLogoutForm": trpzApConfServProfWebPortalLogoutForm,
       "trpzApConfSnoopFilterTable": trpzApConfSnoopFilterTable,
       "trpzApConfSnoopFilterEntry": trpzApConfSnoopFilterEntry,
       "trpzApConfSnoopFilterName": trpzApConfSnoopFilterName,
       "trpzApConfSnoopFilterEnabled": trpzApConfSnoopFilterEnabled,
       "trpzApConfSnoopFilterObserverAddrType": trpzApConfSnoopFilterObserverAddrType,
       "trpzApConfSnoopFilterObserverAddr": trpzApConfSnoopFilterObserverAddr,
       "trpzApConfRadioSnoopFilterTable": trpzApConfRadioSnoopFilterTable,
       "trpzApConfRadioSnoopFilterEntry": trpzApConfRadioSnoopFilterEntry,
       "trpzApConfRadioSnoopFilterRowStatus": trpzApConfRadioSnoopFilterRowStatus,
       "trpzApConfSnoopObserverTable": trpzApConfSnoopObserverTable,
       "trpzApConfSnoopObserverEntry": trpzApConfSnoopObserverEntry,
       "trpzApConfSnoopObserverTargetAddrType": trpzApConfSnoopObserverTargetAddrType,
       "trpzApConfSnoopObserverTargetAddr": trpzApConfSnoopObserverTargetAddr,
       "trpzApConfSnoopObserverSnapLength": trpzApConfSnoopObserverSnapLength,
       "trpzApConfSnoopObserverInterval": trpzApConfSnoopObserverInterval,
       "trpzApConfSnoopObserverTxMode": trpzApConfSnoopObserverTxMode,
       "trpzApConfRemoteSiteTable": trpzApConfRemoteSiteTable,
       "trpzApConfRemoteSiteEntry": trpzApConfRemoteSiteEntry,
       "trpzApConfRemoteSiteName": trpzApConfRemoteSiteName,
       "trpzApConfRemoteSiteCountryCode": trpzApConfRemoteSiteCountryCode,
       "trpzApConfRemoteSitePathMtu": trpzApConfRemoteSitePathMtu,
       "trpzApConfRemoteSiteBackupSsidsEnabled": trpzApConfRemoteSiteBackupSsidsEnabled,
       "trpzApConfRemoteSiteLogServerEnabled": trpzApConfRemoteSiteLogServerEnabled,
       "trpzApConfRemoteSiteLogServerAddrType": trpzApConfRemoteSiteLogServerAddrType,
       "trpzApConfRemoteSiteLogServerAddr": trpzApConfRemoteSiteLogServerAddr,
       "trpzApConfRemoteSiteLogServerPort": trpzApConfRemoteSiteLogServerPort,
       "trpzApConfRemoteSiteLogServerSeverity": trpzApConfRemoteSiteLogServerSeverity,
       "trpzApConfRemoteSiteAcPollingEnabled": trpzApConfRemoteSiteAcPollingEnabled,
       "trpzApConfRemoteSiteRadiusServerGroupName": trpzApConfRemoteSiteRadiusServerGroupName,
       "trpzApConfRemoteSiteRadiusDeadtime": trpzApConfRemoteSiteRadiusDeadtime,
       "trpzApConfRemoteSiteRadiusTimeout": trpzApConfRemoteSiteRadiusTimeout,
       "trpzApConfRemoteSiteRadiusRetransmit": trpzApConfRemoteSiteRadiusRetransmit,
       "trpzApConfRemoteSiteRadiusNasIdType": trpzApConfRemoteSiteRadiusNasIdType,
       "trpzApConfRadioProfile32Table": trpzApConfRadioProfile32Table,
       "trpzApConfRadioProfile32Entry": trpzApConfRadioProfile32Entry,
       "trpzApConfRadioProf32RadioProfileName": trpzApConfRadioProf32RadioProfileName,
       "trpzApConfRadioProf32BeaconInterval": trpzApConfRadioProf32BeaconInterval,
       "trpzApConfRadioProf32DtimInterval": trpzApConfRadioProf32DtimInterval,
       "trpzApConfRadioProf32ChannelWidth11na": trpzApConfRadioProf32ChannelWidth11na,
       "trpzApConfRadioProf32MaxTxLifetime": trpzApConfRadioProf32MaxTxLifetime,
       "trpzApConfRadioProf32MaxRxLifetime": trpzApConfRadioProf32MaxRxLifetime,
       "trpzApConfRadioProf32RtsThreshold": trpzApConfRadioProf32RtsThreshold,
       "trpzApConfRadioProf32FragThreshold": trpzApConfRadioProf32FragThreshold,
       "trpzApConfRadioProf32LongXmitPreambleEnabled": trpzApConfRadioProf32LongXmitPreambleEnabled,
       "trpzApConfRadioProf32CountermeasuresMode": trpzApConfRadioProf32CountermeasuresMode,
       "trpzApConfRadioProf32RFScanMode": trpzApConfRadioProf32RFScanMode,
       "trpzApConfRadioProf32RFScanChannelScope": trpzApConfRadioProf32RFScanChannelScope,
       "trpzApConfRadioProf32RFScanCTSEnabled": trpzApConfRadioProf32RFScanCTSEnabled,
       "trpzApConfRadioProf32AutoTunePowerEnabled": trpzApConfRadioProf32AutoTunePowerEnabled,
       "trpzApConfRadioProf32AutoTunePowerRampInterval": trpzApConfRadioProf32AutoTunePowerRampInterval,
       "trpzApConfRadioProf32AutoTunePowerChangeInterval": trpzApConfRadioProf32AutoTunePowerChangeInterval,
       "trpzApConfRadioProf32FairQueuingEnabled": trpzApConfRadioProf32FairQueuingEnabled,
       "trpzApConfRadioProf32CacBackgroundACMandatory": trpzApConfRadioProf32CacBackgroundACMandatory,
       "trpzApConfRadioProf32CacBackgroundMaxUtilization": trpzApConfRadioProf32CacBackgroundMaxUtilization,
       "trpzApConfRadioProf32CacBackgroundPolicingEnabled": trpzApConfRadioProf32CacBackgroundPolicingEnabled,
       "trpzApConfRadioProf32CacBestEffortACMandatory": trpzApConfRadioProf32CacBestEffortACMandatory,
       "trpzApConfRadioProf32CacBestEffortMaxUtilization": trpzApConfRadioProf32CacBestEffortMaxUtilization,
       "trpzApConfRadioProf32CacBestEffortPolicingEnabled": trpzApConfRadioProf32CacBestEffortPolicingEnabled,
       "trpzApConfRadioProf32CacVideoACMandatory": trpzApConfRadioProf32CacVideoACMandatory,
       "trpzApConfRadioProf32CacVideoMaxUtilization": trpzApConfRadioProf32CacVideoMaxUtilization,
       "trpzApConfRadioProf32CacVideoPolicingEnabled": trpzApConfRadioProf32CacVideoPolicingEnabled,
       "trpzApConfRadioProf32CacVoiceACMandatory": trpzApConfRadioProf32CacVoiceACMandatory,
       "trpzApConfRadioProf32CacVoiceMaxUtilization": trpzApConfRadioProf32CacVoiceMaxUtilization,
       "trpzApConfRadioProf32CacVoicePolicingEnabled": trpzApConfRadioProf32CacVoicePolicingEnabled,
       "trpzApConfRadioProf32RfidTagEnabled": trpzApConfRadioProf32RfidTagEnabled,
       "trpzApConfRadioProf32WmmPowerSaveEnabled": trpzApConfRadioProf32WmmPowerSaveEnabled,
       "trpzApConfRadioProf32RateEnforcementEnabled": trpzApConfRadioProf32RateEnforcementEnabled,
       "trpzApConfRadioProf32DfsChannelsEnabled": trpzApConfRadioProf32DfsChannelsEnabled,
       "trpzApConfRadioProf32RFSpectralScanModeEnabled": trpzApConfRadioProf32RFSpectralScanModeEnabled,
       "trpzApConfRadioProf32RFSpectralScanPriority": trpzApConfRadioProf32RFSpectralScanPriority,
       "trpzApConfRadioProf32ServiceProfileTable": trpzApConfRadioProf32ServiceProfileTable,
       "trpzApConfRadioProf32ServiceProfileEntry": trpzApConfRadioProf32ServiceProfileEntry,
       "trpzApConfRp32ServpRadioProfileName": trpzApConfRp32ServpRadioProfileName,
       "trpzApConfRp32ServpServiceProfileName": trpzApConfRp32ServpServiceProfileName,
       "trpzApConfRp32ServpRowStatus": trpzApConfRp32ServpRowStatus,
       "trpzApConfRadioProf32SnoopFilterTable": trpzApConfRadioProf32SnoopFilterTable,
       "trpzApConfRadioProf32SnoopFilterEntry": trpzApConfRadioProf32SnoopFilterEntry,
       "trpzApConfRp32SnoopfRadioProfileName": trpzApConfRp32SnoopfRadioProfileName,
       "trpzApConfRp32SnoopfSnoopFilterName": trpzApConfRp32SnoopfSnoopFilterName,
       "trpzApConfRp32SnoopfRowStatus": trpzApConfRp32SnoopfRowStatus,
       "trpzApConfigConformance": trpzApConfigConformance,
       "trpzApConfigCompliances": trpzApConfigCompliances,
       "trpzApConfigCompliance": trpzApConfigCompliance,
       "trpzApConfigComplianceRev2": trpzApConfigComplianceRev2,
       "trpzApConfigComplianceRev3": trpzApConfigComplianceRev3,
       "trpzApConfigComplianceRev4": trpzApConfigComplianceRev4,
       "trpzApConfigComplianceRev5": trpzApConfigComplianceRev5,
       "trpzApConfigGroups": trpzApConfigGroups,
       "trpzApConfApConfigTableGroup": trpzApConfApConfigTableGroup,
       "trpzApConfRadioConfigTableGroup": trpzApConfRadioConfigTableGroup,
       "trpzApConfApTemplateConfigTableGroup": trpzApConfApTemplateConfigTableGroup,
       "trpzApConfApTemplateRadioConfigTableGroup": trpzApConfApTemplateRadioConfigTableGroup,
       "trpzApConfRadioProfileTableGroup": trpzApConfRadioProfileTableGroup,
       "trpzApConfRadioProfServiceProfileTableGroup": trpzApConfRadioProfServiceProfileTableGroup,
       "trpzApConfRadioProfSnoopFilterTableGroup": trpzApConfRadioProfSnoopFilterTableGroup,
       "trpzApConfServiceProfileTableGroup": trpzApConfServiceProfileTableGroup,
       "trpzApConfSnoopFilterTableGroup": trpzApConfSnoopFilterTableGroup,
       "trpzApConfServiceProfileTableGroupRev2": trpzApConfServiceProfileTableGroupRev2,
       "trpzApConfApConfigLldpGroup": trpzApConfApConfigLldpGroup,
       "trpzApConfApConfigTunnelGroup": trpzApConfApConfigTunnelGroup,
       "trpzApConfApConfigRemoteApGroup": trpzApConfApConfigRemoteApGroup,
       "trpzApConfRadioProfileRFSpectralScanGroup": trpzApConfRadioProfileRFSpectralScanGroup,
       "trpzApConfApConfigTableGroupRev2": trpzApConfApConfigTableGroupRev2,
       "trpzApConfSnoopFilterTableGroupRev2": trpzApConfSnoopFilterTableGroupRev2,
       "trpzApConfSnoopObserverTableGroup": trpzApConfSnoopObserverTableGroup,
       "trpzApConfRadioSnoopFilterTableGroup": trpzApConfRadioSnoopFilterTableGroup,
       "trpzApConfServiceProfileTableGroupRev3": trpzApConfServiceProfileTableGroupRev3,
       "trpzApConfRemoteSiteTableGroup": trpzApConfRemoteSiteTableGroup,
       "trpzApConfRadioProfileTableGroupRev2": trpzApConfRadioProfileTableGroupRev2,
       "trpzApConfApConfigTableGroupRev3": trpzApConfApConfigTableGroupRev3,
       "trpzApConfRadioConfigTableGroupRev2": trpzApConfRadioConfigTableGroupRev2,
       "trpzApConfApTemplateRadioConfigTableGroupRev2": trpzApConfApTemplateRadioConfigTableGroupRev2,
       "trpzApConfRadioProfile32TableGroup": trpzApConfRadioProfile32TableGroup,
       "trpzApConfRadioProfileRFSpectralScanGroupRev2": trpzApConfRadioProfileRFSpectralScanGroupRev2,
       "trpzApConfRadioProf32ServiceProfileTableGroup": trpzApConfRadioProf32ServiceProfileTableGroup,
       "trpzApConfRadioProf32SnoopFilterTableGroup": trpzApConfRadioProf32SnoopFilterTableGroup,
       "trpzApConfRemoteSiteTableGroupRev2": trpzApConfRemoteSiteTableGroupRev2}
)
