# SNMP MIB module (NTWS-AP-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NTWS-AP-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:50 2024
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

(NtwsApAttachType,
 NtwsApBias,
 NtwsApFingerprint,
 NtwsApLedMode,
 NtwsApNum,
 NtwsApPowerMode,
 NtwsApRadioIndex,
 NtwsApSerialNum,
 NtwsChannelNum,
 NtwsPowerLevel,
 NtwsRadioAntennaLocation,
 NtwsRadioChannelWidth,
 NtwsRadioMode,
 NtwsRadioType) = mibBuilder.importSymbols(
    "NTWS-AP-TC",
    "NtwsApAttachType",
    "NtwsApBias",
    "NtwsApFingerprint",
    "NtwsApLedMode",
    "NtwsApNum",
    "NtwsApPowerMode",
    "NtwsApRadioIndex",
    "NtwsApSerialNum",
    "NtwsChannelNum",
    "NtwsPowerLevel",
    "NtwsRadioAntennaLocation",
    "NtwsRadioChannelWidth",
    "NtwsRadioMode",
    "NtwsRadioType")

(NtwsPhysPortNumberOrZero,) = mibBuilder.importSymbols(
    "NTWS-BASIC-TC",
    "NtwsPhysPortNumberOrZero")

(ntwsMibs,) = mibBuilder.importSymbols(
    "NTWS-ROOT-MIB",
    "ntwsMibs")

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


# MODULE-IDENTITY

ntwsApConfigMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14)
)
ntwsApConfigMib.setRevisions(
        ("2009-11-19 01:08",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NtwsApTemplateName(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class NtwsRadioProfileName(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class NtwsServiceProfileName(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class NtwsSnoopFilterName(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )



class NtwsServiceProfileSsidType(Integer32, TextualConvention):
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



class NtwsServiceProfile11nMode(Integer32, TextualConvention):
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



class NtwsServiceProfile11nFrameAggregationType(Integer32, TextualConvention):
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



class NtwsServiceProfile11nMsduMaxLength(Integer32, TextualConvention):
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



class NtwsServiceProfile11nMpduMaxLength(Integer32, TextualConvention):
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



class NtwsServiceProfileAuthFallthruType(Integer32, TextualConvention):
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



class NtwsServiceProfileCacMode(Integer32, TextualConvention):
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



class NtwsRadioProfileCountermeasuresMode(Integer32, TextualConvention):
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



class NtwsRadioProfileRFScanChannelScope(Integer32, TextualConvention):
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



class NtwsRadioProfileAutoTuneChannelRange(Integer32, TextualConvention):
    status = "current"
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



class NtwsRadioProfileRFScanMode(Integer32, TextualConvention):
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



# MIB Managed Objects in the order of their OIDs

_NtwsApConfigMibObjects_ObjectIdentity = ObjectIdentity
ntwsApConfigMibObjects = _NtwsApConfigMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1)
)
_NtwsApConfApConfigTable_Object = MibTable
ntwsApConfApConfigTable = _NtwsApConfApConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 2)
)
if mibBuilder.loadTexts:
    ntwsApConfApConfigTable.setStatus("current")
_NtwsApConfApConfigEntry_Object = MibTableRow
ntwsApConfApConfigEntry = _NtwsApConfApConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 2, 1)
)
ntwsApConfApConfigEntry.setIndexNames(
    (0, "NTWS-AP-CONFIG-MIB", "ntwsApConfApConfigApNum"),
)
if mibBuilder.loadTexts:
    ntwsApConfApConfigEntry.setStatus("current")
_NtwsApConfApConfigApNum_Type = NtwsApNum
_NtwsApConfApConfigApNum_Object = MibTableColumn
ntwsApConfApConfigApNum = _NtwsApConfApConfigApNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 2, 1, 1),
    _NtwsApConfApConfigApNum_Type()
)
ntwsApConfApConfigApNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApConfApConfigApNum.setStatus("current")
_NtwsApConfApConfigApAttachType_Type = NtwsApAttachType
_NtwsApConfApConfigApAttachType_Object = MibTableColumn
ntwsApConfApConfigApAttachType = _NtwsApConfApConfigApAttachType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 2, 1, 2),
    _NtwsApConfApConfigApAttachType_Type()
)
ntwsApConfApConfigApAttachType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApConfigApAttachType.setStatus("current")
_NtwsApConfApConfigPhysPortNum_Type = NtwsPhysPortNumberOrZero
_NtwsApConfApConfigPhysPortNum_Object = MibTableColumn
ntwsApConfApConfigPhysPortNum = _NtwsApConfApConfigPhysPortNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 2, 1, 3),
    _NtwsApConfApConfigPhysPortNum_Type()
)
ntwsApConfApConfigPhysPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApConfigPhysPortNum.setStatus("current")
_NtwsApConfApConfigApSerialNum_Type = NtwsApSerialNum
_NtwsApConfApConfigApSerialNum_Object = MibTableColumn
ntwsApConfApConfigApSerialNum = _NtwsApConfApConfigApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 2, 1, 4),
    _NtwsApConfApConfigApSerialNum_Type()
)
ntwsApConfApConfigApSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApConfigApSerialNum.setStatus("current")


class _NtwsApConfApConfigApModelName_Type(DisplayString):
    """Custom type ntwsApConfApConfigApModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_NtwsApConfApConfigApModelName_Type.__name__ = "DisplayString"
_NtwsApConfApConfigApModelName_Object = MibTableColumn
ntwsApConfApConfigApModelName = _NtwsApConfApConfigApModelName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 2, 1, 5),
    _NtwsApConfApConfigApModelName_Type()
)
ntwsApConfApConfigApModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApConfigApModelName.setStatus("current")
_NtwsApConfApConfigFingerprint_Type = NtwsApFingerprint
_NtwsApConfApConfigFingerprint_Object = MibTableColumn
ntwsApConfApConfigFingerprint = _NtwsApConfApConfigFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 2, 1, 6),
    _NtwsApConfApConfigFingerprint_Type()
)
ntwsApConfApConfigFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApConfigFingerprint.setStatus("current")
_NtwsApConfApConfigBias_Type = NtwsApBias
_NtwsApConfApConfigBias_Object = MibTableColumn
ntwsApConfApConfigBias = _NtwsApConfApConfigBias_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 2, 1, 7),
    _NtwsApConfApConfigBias_Type()
)
ntwsApConfApConfigBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApConfigBias.setStatus("current")
_NtwsApConfApConfigApTimeout_Type = Unsigned32
_NtwsApConfApConfigApTimeout_Object = MibTableColumn
ntwsApConfApConfigApTimeout = _NtwsApConfApConfigApTimeout_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 2, 1, 8),
    _NtwsApConfApConfigApTimeout_Type()
)
ntwsApConfApConfigApTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApConfigApTimeout.setStatus("current")


class _NtwsApConfApConfigApName_Type(DisplayString):
    """Custom type ntwsApConfApConfigApName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NtwsApConfApConfigApName_Type.__name__ = "DisplayString"
_NtwsApConfApConfigApName_Object = MibTableColumn
ntwsApConfApConfigApName = _NtwsApConfApConfigApName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 2, 1, 9),
    _NtwsApConfApConfigApName_Type()
)
ntwsApConfApConfigApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApConfigApName.setStatus("current")


class _NtwsApConfApConfigContact_Type(DisplayString):
    """Custom type ntwsApConfApConfigContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtwsApConfApConfigContact_Type.__name__ = "DisplayString"
_NtwsApConfApConfigContact_Object = MibTableColumn
ntwsApConfApConfigContact = _NtwsApConfApConfigContact_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 2, 1, 10),
    _NtwsApConfApConfigContact_Type()
)
ntwsApConfApConfigContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApConfigContact.setStatus("current")


class _NtwsApConfApConfigLocation_Type(DisplayString):
    """Custom type ntwsApConfApConfigLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtwsApConfApConfigLocation_Type.__name__ = "DisplayString"
_NtwsApConfApConfigLocation_Object = MibTableColumn
ntwsApConfApConfigLocation = _NtwsApConfApConfigLocation_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 2, 1, 11),
    _NtwsApConfApConfigLocation_Type()
)
ntwsApConfApConfigLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApConfigLocation.setStatus("current")
_NtwsApConfApConfigBlinkEnabled_Type = TruthValue
_NtwsApConfApConfigBlinkEnabled_Object = MibTableColumn
ntwsApConfApConfigBlinkEnabled = _NtwsApConfApConfigBlinkEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 2, 1, 12),
    _NtwsApConfApConfigBlinkEnabled_Type()
)
ntwsApConfApConfigBlinkEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApConfigBlinkEnabled.setStatus("current")
_NtwsApConfApConfigForceImageDownloadEnabled_Type = TruthValue
_NtwsApConfApConfigForceImageDownloadEnabled_Object = MibTableColumn
ntwsApConfApConfigForceImageDownloadEnabled = _NtwsApConfApConfigForceImageDownloadEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 2, 1, 13),
    _NtwsApConfApConfigForceImageDownloadEnabled_Type()
)
ntwsApConfApConfigForceImageDownloadEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApConfigForceImageDownloadEnabled.setStatus("current")
_NtwsApConfApConfigFirmwareUpgradeEnabled_Type = TruthValue
_NtwsApConfApConfigFirmwareUpgradeEnabled_Object = MibTableColumn
ntwsApConfApConfigFirmwareUpgradeEnabled = _NtwsApConfApConfigFirmwareUpgradeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 2, 1, 14),
    _NtwsApConfApConfigFirmwareUpgradeEnabled_Type()
)
ntwsApConfApConfigFirmwareUpgradeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApConfigFirmwareUpgradeEnabled.setStatus("current")
_NtwsApConfApConfigLocalSwitchingEnabled_Type = TruthValue
_NtwsApConfApConfigLocalSwitchingEnabled_Object = MibTableColumn
ntwsApConfApConfigLocalSwitchingEnabled = _NtwsApConfApConfigLocalSwitchingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 2, 1, 15),
    _NtwsApConfApConfigLocalSwitchingEnabled_Type()
)
ntwsApConfApConfigLocalSwitchingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApConfigLocalSwitchingEnabled.setStatus("current")
_NtwsApConfApConfigPowerMode_Type = NtwsApPowerMode
_NtwsApConfApConfigPowerMode_Object = MibTableColumn
ntwsApConfApConfigPowerMode = _NtwsApConfApConfigPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 2, 1, 16),
    _NtwsApConfApConfigPowerMode_Type()
)
ntwsApConfApConfigPowerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApConfigPowerMode.setStatus("current")
_NtwsApConfApConfigLedMode_Type = NtwsApLedMode
_NtwsApConfApConfigLedMode_Object = MibTableColumn
ntwsApConfApConfigLedMode = _NtwsApConfApConfigLedMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 2, 1, 17),
    _NtwsApConfApConfigLedMode_Type()
)
ntwsApConfApConfigLedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApConfigLedMode.setStatus("current")


class _NtwsApConfApConfigDescription_Type(DisplayString):
    """Custom type ntwsApConfApConfigDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_NtwsApConfApConfigDescription_Type.__name__ = "DisplayString"
_NtwsApConfApConfigDescription_Object = MibTableColumn
ntwsApConfApConfigDescription = _NtwsApConfApConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 2, 1, 18),
    _NtwsApConfApConfigDescription_Type()
)
ntwsApConfApConfigDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApConfigDescription.setStatus("current")
_NtwsApConfRadioConfigTable_Object = MibTable
ntwsApConfRadioConfigTable = _NtwsApConfRadioConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 3)
)
if mibBuilder.loadTexts:
    ntwsApConfRadioConfigTable.setStatus("current")
_NtwsApConfRadioConfigEntry_Object = MibTableRow
ntwsApConfRadioConfigEntry = _NtwsApConfRadioConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 3, 1)
)
ntwsApConfRadioConfigEntry.setIndexNames(
    (0, "NTWS-AP-CONFIG-MIB", "ntwsApConfRadioConfigApNum"),
    (0, "NTWS-AP-CONFIG-MIB", "ntwsApConfRadioConfigRadioIndex"),
)
if mibBuilder.loadTexts:
    ntwsApConfRadioConfigEntry.setStatus("current")
_NtwsApConfRadioConfigApNum_Type = NtwsApNum
_NtwsApConfRadioConfigApNum_Object = MibTableColumn
ntwsApConfRadioConfigApNum = _NtwsApConfRadioConfigApNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 3, 1, 1),
    _NtwsApConfRadioConfigApNum_Type()
)
ntwsApConfRadioConfigApNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApConfRadioConfigApNum.setStatus("current")
_NtwsApConfRadioConfigRadioIndex_Type = NtwsApRadioIndex
_NtwsApConfRadioConfigRadioIndex_Object = MibTableColumn
ntwsApConfRadioConfigRadioIndex = _NtwsApConfRadioConfigRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 3, 1, 2),
    _NtwsApConfRadioConfigRadioIndex_Type()
)
ntwsApConfRadioConfigRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApConfRadioConfigRadioIndex.setStatus("current")
_NtwsApConfRadioConfigRadioType_Type = NtwsRadioType
_NtwsApConfRadioConfigRadioType_Object = MibTableColumn
ntwsApConfRadioConfigRadioType = _NtwsApConfRadioConfigRadioType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 3, 1, 3),
    _NtwsApConfRadioConfigRadioType_Type()
)
ntwsApConfRadioConfigRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioConfigRadioType.setStatus("current")
_NtwsApConfRadioConfigRadioMode_Type = NtwsRadioMode
_NtwsApConfRadioConfigRadioMode_Object = MibTableColumn
ntwsApConfRadioConfigRadioMode = _NtwsApConfRadioConfigRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 3, 1, 4),
    _NtwsApConfRadioConfigRadioMode_Type()
)
ntwsApConfRadioConfigRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioConfigRadioMode.setStatus("current")
_NtwsApConfRadioConfigRadioProfileName_Type = NtwsRadioProfileName
_NtwsApConfRadioConfigRadioProfileName_Object = MibTableColumn
ntwsApConfRadioConfigRadioProfileName = _NtwsApConfRadioConfigRadioProfileName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 3, 1, 5),
    _NtwsApConfRadioConfigRadioProfileName_Type()
)
ntwsApConfRadioConfigRadioProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioConfigRadioProfileName.setStatus("current")
_NtwsApConfRadioConfigChannel_Type = NtwsChannelNum
_NtwsApConfRadioConfigChannel_Object = MibTableColumn
ntwsApConfRadioConfigChannel = _NtwsApConfRadioConfigChannel_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 3, 1, 6),
    _NtwsApConfRadioConfigChannel_Type()
)
ntwsApConfRadioConfigChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioConfigChannel.setStatus("current")
_NtwsApConfRadioConfigTxPower_Type = NtwsPowerLevel
_NtwsApConfRadioConfigTxPower_Object = MibTableColumn
ntwsApConfRadioConfigTxPower = _NtwsApConfRadioConfigTxPower_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 3, 1, 7),
    _NtwsApConfRadioConfigTxPower_Type()
)
ntwsApConfRadioConfigTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioConfigTxPower.setStatus("current")
_NtwsApConfRadioConfigAutoTuneMaxTxPower_Type = NtwsPowerLevel
_NtwsApConfRadioConfigAutoTuneMaxTxPower_Object = MibTableColumn
ntwsApConfRadioConfigAutoTuneMaxTxPower = _NtwsApConfRadioConfigAutoTuneMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 3, 1, 8),
    _NtwsApConfRadioConfigAutoTuneMaxTxPower_Type()
)
ntwsApConfRadioConfigAutoTuneMaxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioConfigAutoTuneMaxTxPower.setStatus("current")


class _NtwsApConfRadioConfigAntennaType_Type(DisplayString):
    """Custom type ntwsApConfRadioConfigAntennaType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NtwsApConfRadioConfigAntennaType_Type.__name__ = "DisplayString"
_NtwsApConfRadioConfigAntennaType_Object = MibTableColumn
ntwsApConfRadioConfigAntennaType = _NtwsApConfRadioConfigAntennaType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 3, 1, 9),
    _NtwsApConfRadioConfigAntennaType_Type()
)
ntwsApConfRadioConfigAntennaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioConfigAntennaType.setStatus("current")
_NtwsApConfRadioConfigAntennaLocation_Type = NtwsRadioAntennaLocation
_NtwsApConfRadioConfigAntennaLocation_Object = MibTableColumn
ntwsApConfRadioConfigAntennaLocation = _NtwsApConfRadioConfigAntennaLocation_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 3, 1, 10),
    _NtwsApConfRadioConfigAntennaLocation_Type()
)
ntwsApConfRadioConfigAntennaLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioConfigAntennaLocation.setStatus("current")
_NtwsApConfRadioConfigLoadBalancingEnabled_Type = TruthValue
_NtwsApConfRadioConfigLoadBalancingEnabled_Object = MibTableColumn
ntwsApConfRadioConfigLoadBalancingEnabled = _NtwsApConfRadioConfigLoadBalancingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 3, 1, 11),
    _NtwsApConfRadioConfigLoadBalancingEnabled_Type()
)
ntwsApConfRadioConfigLoadBalancingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioConfigLoadBalancingEnabled.setStatus("current")


class _NtwsApConfRadioConfigLoadBalancingGroup_Type(DisplayString):
    """Custom type ntwsApConfRadioConfigLoadBalancingGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtwsApConfRadioConfigLoadBalancingGroup_Type.__name__ = "DisplayString"
_NtwsApConfRadioConfigLoadBalancingGroup_Object = MibTableColumn
ntwsApConfRadioConfigLoadBalancingGroup = _NtwsApConfRadioConfigLoadBalancingGroup_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 3, 1, 12),
    _NtwsApConfRadioConfigLoadBalancingGroup_Type()
)
ntwsApConfRadioConfigLoadBalancingGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioConfigLoadBalancingGroup.setStatus("current")
_NtwsApConfRadioConfigLoadRebalancingEnabled_Type = TruthValue
_NtwsApConfRadioConfigLoadRebalancingEnabled_Object = MibTableColumn
ntwsApConfRadioConfigLoadRebalancingEnabled = _NtwsApConfRadioConfigLoadRebalancingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 3, 1, 13),
    _NtwsApConfRadioConfigLoadRebalancingEnabled_Type()
)
ntwsApConfRadioConfigLoadRebalancingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioConfigLoadRebalancingEnabled.setStatus("current")
_NtwsApConfApTemplateConfigTable_Object = MibTable
ntwsApConfApTemplateConfigTable = _NtwsApConfApTemplateConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 4)
)
if mibBuilder.loadTexts:
    ntwsApConfApTemplateConfigTable.setStatus("current")
_NtwsApConfApTemplateConfigEntry_Object = MibTableRow
ntwsApConfApTemplateConfigEntry = _NtwsApConfApTemplateConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 4, 1)
)
ntwsApConfApTemplateConfigEntry.setIndexNames(
    (0, "NTWS-AP-CONFIG-MIB", "ntwsApConfApTemplConfApTemplateName"),
)
if mibBuilder.loadTexts:
    ntwsApConfApTemplateConfigEntry.setStatus("current")
_NtwsApConfApTemplConfApTemplateName_Type = NtwsApTemplateName
_NtwsApConfApTemplConfApTemplateName_Object = MibTableColumn
ntwsApConfApTemplConfApTemplateName = _NtwsApConfApTemplConfApTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 4, 1, 1),
    _NtwsApConfApTemplConfApTemplateName_Type()
)
ntwsApConfApTemplConfApTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApConfApTemplConfApTemplateName.setStatus("current")
_NtwsApConfApTemplConfApTemplateEnabled_Type = TruthValue
_NtwsApConfApTemplConfApTemplateEnabled_Object = MibTableColumn
ntwsApConfApTemplConfApTemplateEnabled = _NtwsApConfApTemplConfApTemplateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 4, 1, 2),
    _NtwsApConfApTemplConfApTemplateEnabled_Type()
)
ntwsApConfApTemplConfApTemplateEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApTemplConfApTemplateEnabled.setStatus("current")
_NtwsApConfApTemplConfBias_Type = NtwsApBias
_NtwsApConfApTemplConfBias_Object = MibTableColumn
ntwsApConfApTemplConfBias = _NtwsApConfApTemplConfBias_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 4, 1, 3),
    _NtwsApConfApTemplConfBias_Type()
)
ntwsApConfApTemplConfBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApTemplConfBias.setStatus("current")
_NtwsApConfApTemplConfApTimeout_Type = Unsigned32
_NtwsApConfApTemplConfApTimeout_Object = MibTableColumn
ntwsApConfApTemplConfApTimeout = _NtwsApConfApTemplConfApTimeout_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 4, 1, 4),
    _NtwsApConfApTemplConfApTimeout_Type()
)
ntwsApConfApTemplConfApTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApTemplConfApTimeout.setStatus("current")
_NtwsApConfApTemplConfBlinkEnabled_Type = TruthValue
_NtwsApConfApTemplConfBlinkEnabled_Object = MibTableColumn
ntwsApConfApTemplConfBlinkEnabled = _NtwsApConfApTemplConfBlinkEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 4, 1, 5),
    _NtwsApConfApTemplConfBlinkEnabled_Type()
)
ntwsApConfApTemplConfBlinkEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApTemplConfBlinkEnabled.setStatus("current")
_NtwsApConfApTemplConfForceImageDownloadEnabled_Type = TruthValue
_NtwsApConfApTemplConfForceImageDownloadEnabled_Object = MibTableColumn
ntwsApConfApTemplConfForceImageDownloadEnabled = _NtwsApConfApTemplConfForceImageDownloadEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 4, 1, 6),
    _NtwsApConfApTemplConfForceImageDownloadEnabled_Type()
)
ntwsApConfApTemplConfForceImageDownloadEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApTemplConfForceImageDownloadEnabled.setStatus("current")
_NtwsApConfApTemplConfFirmwareUpgradeEnabled_Type = TruthValue
_NtwsApConfApTemplConfFirmwareUpgradeEnabled_Object = MibTableColumn
ntwsApConfApTemplConfFirmwareUpgradeEnabled = _NtwsApConfApTemplConfFirmwareUpgradeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 4, 1, 7),
    _NtwsApConfApTemplConfFirmwareUpgradeEnabled_Type()
)
ntwsApConfApTemplConfFirmwareUpgradeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApTemplConfFirmwareUpgradeEnabled.setStatus("current")
_NtwsApConfApTemplConfLocalSwitchingEnabled_Type = TruthValue
_NtwsApConfApTemplConfLocalSwitchingEnabled_Object = MibTableColumn
ntwsApConfApTemplConfLocalSwitchingEnabled = _NtwsApConfApTemplConfLocalSwitchingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 4, 1, 8),
    _NtwsApConfApTemplConfLocalSwitchingEnabled_Type()
)
ntwsApConfApTemplConfLocalSwitchingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApTemplConfLocalSwitchingEnabled.setStatus("current")
_NtwsApConfApTemplConfPowerMode_Type = NtwsApPowerMode
_NtwsApConfApTemplConfPowerMode_Object = MibTableColumn
ntwsApConfApTemplConfPowerMode = _NtwsApConfApTemplConfPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 4, 1, 9),
    _NtwsApConfApTemplConfPowerMode_Type()
)
ntwsApConfApTemplConfPowerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApTemplConfPowerMode.setStatus("current")
_NtwsApConfApTemplConfLedMode_Type = NtwsApLedMode
_NtwsApConfApTemplConfLedMode_Object = MibTableColumn
ntwsApConfApTemplConfLedMode = _NtwsApConfApTemplConfLedMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 4, 1, 10),
    _NtwsApConfApTemplConfLedMode_Type()
)
ntwsApConfApTemplConfLedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApTemplConfLedMode.setStatus("current")
_NtwsApConfApTemplateRadioConfigTable_Object = MibTable
ntwsApConfApTemplateRadioConfigTable = _NtwsApConfApTemplateRadioConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 5)
)
if mibBuilder.loadTexts:
    ntwsApConfApTemplateRadioConfigTable.setStatus("current")
_NtwsApConfApTemplateRadioConfigEntry_Object = MibTableRow
ntwsApConfApTemplateRadioConfigEntry = _NtwsApConfApTemplateRadioConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 5, 1)
)
ntwsApConfApTemplateRadioConfigEntry.setIndexNames(
    (0, "NTWS-AP-CONFIG-MIB", "ntwsApConfApTemRadioConfApTemplateName"),
    (0, "NTWS-AP-CONFIG-MIB", "ntwsApConfApTemRadioConfRadioIndex"),
)
if mibBuilder.loadTexts:
    ntwsApConfApTemplateRadioConfigEntry.setStatus("current")
_NtwsApConfApTemRadioConfApTemplateName_Type = NtwsApTemplateName
_NtwsApConfApTemRadioConfApTemplateName_Object = MibTableColumn
ntwsApConfApTemRadioConfApTemplateName = _NtwsApConfApTemRadioConfApTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 5, 1, 1),
    _NtwsApConfApTemRadioConfApTemplateName_Type()
)
ntwsApConfApTemRadioConfApTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApConfApTemRadioConfApTemplateName.setStatus("current")
_NtwsApConfApTemRadioConfRadioIndex_Type = NtwsApRadioIndex
_NtwsApConfApTemRadioConfRadioIndex_Object = MibTableColumn
ntwsApConfApTemRadioConfRadioIndex = _NtwsApConfApTemRadioConfRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 5, 1, 2),
    _NtwsApConfApTemRadioConfRadioIndex_Type()
)
ntwsApConfApTemRadioConfRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApConfApTemRadioConfRadioIndex.setStatus("current")
_NtwsApConfApTemRadioConfRadioMode_Type = NtwsRadioMode
_NtwsApConfApTemRadioConfRadioMode_Object = MibTableColumn
ntwsApConfApTemRadioConfRadioMode = _NtwsApConfApTemRadioConfRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 5, 1, 3),
    _NtwsApConfApTemRadioConfRadioMode_Type()
)
ntwsApConfApTemRadioConfRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApTemRadioConfRadioMode.setStatus("current")
_NtwsApConfApTemRadioConfRadioProfileName_Type = NtwsRadioProfileName
_NtwsApConfApTemRadioConfRadioProfileName_Object = MibTableColumn
ntwsApConfApTemRadioConfRadioProfileName = _NtwsApConfApTemRadioConfRadioProfileName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 5, 1, 4),
    _NtwsApConfApTemRadioConfRadioProfileName_Type()
)
ntwsApConfApTemRadioConfRadioProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApTemRadioConfRadioProfileName.setStatus("current")
_NtwsApConfApTemRadioConfAutoTuneMaxTxPower_Type = NtwsPowerLevel
_NtwsApConfApTemRadioConfAutoTuneMaxTxPower_Object = MibTableColumn
ntwsApConfApTemRadioConfAutoTuneMaxTxPower = _NtwsApConfApTemRadioConfAutoTuneMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 5, 1, 5),
    _NtwsApConfApTemRadioConfAutoTuneMaxTxPower_Type()
)
ntwsApConfApTemRadioConfAutoTuneMaxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApTemRadioConfAutoTuneMaxTxPower.setStatus("current")
_NtwsApConfApTemRadioConfLoadBalancingEnabled_Type = TruthValue
_NtwsApConfApTemRadioConfLoadBalancingEnabled_Object = MibTableColumn
ntwsApConfApTemRadioConfLoadBalancingEnabled = _NtwsApConfApTemRadioConfLoadBalancingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 5, 1, 6),
    _NtwsApConfApTemRadioConfLoadBalancingEnabled_Type()
)
ntwsApConfApTemRadioConfLoadBalancingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApTemRadioConfLoadBalancingEnabled.setStatus("current")


class _NtwsApConfApTemRadioConfLoadBalancingGroup_Type(DisplayString):
    """Custom type ntwsApConfApTemRadioConfLoadBalancingGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtwsApConfApTemRadioConfLoadBalancingGroup_Type.__name__ = "DisplayString"
_NtwsApConfApTemRadioConfLoadBalancingGroup_Object = MibTableColumn
ntwsApConfApTemRadioConfLoadBalancingGroup = _NtwsApConfApTemRadioConfLoadBalancingGroup_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 5, 1, 7),
    _NtwsApConfApTemRadioConfLoadBalancingGroup_Type()
)
ntwsApConfApTemRadioConfLoadBalancingGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApTemRadioConfLoadBalancingGroup.setStatus("current")
_NtwsApConfApTemRadioConfLoadRebalancingEnabled_Type = TruthValue
_NtwsApConfApTemRadioConfLoadRebalancingEnabled_Object = MibTableColumn
ntwsApConfApTemRadioConfLoadRebalancingEnabled = _NtwsApConfApTemRadioConfLoadRebalancingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 5, 1, 8),
    _NtwsApConfApTemRadioConfLoadRebalancingEnabled_Type()
)
ntwsApConfApTemRadioConfLoadRebalancingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfApTemRadioConfLoadRebalancingEnabled.setStatus("current")
_NtwsApConfRadioProfileTable_Object = MibTable
ntwsApConfRadioProfileTable = _NtwsApConfRadioProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6)
)
if mibBuilder.loadTexts:
    ntwsApConfRadioProfileTable.setStatus("current")
_NtwsApConfRadioProfileEntry_Object = MibTableRow
ntwsApConfRadioProfileEntry = _NtwsApConfRadioProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1)
)
ntwsApConfRadioProfileEntry.setIndexNames(
    (0, "NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfRadioProfileName"),
)
if mibBuilder.loadTexts:
    ntwsApConfRadioProfileEntry.setStatus("current")
_NtwsApConfRadioProfRadioProfileName_Type = NtwsRadioProfileName
_NtwsApConfRadioProfRadioProfileName_Object = MibTableColumn
ntwsApConfRadioProfRadioProfileName = _NtwsApConfRadioProfRadioProfileName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 1),
    _NtwsApConfRadioProfRadioProfileName_Type()
)
ntwsApConfRadioProfRadioProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfRadioProfileName.setStatus("current")
_NtwsApConfRadioProfBeaconInterval_Type = Unsigned32
_NtwsApConfRadioProfBeaconInterval_Object = MibTableColumn
ntwsApConfRadioProfBeaconInterval = _NtwsApConfRadioProfBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 2),
    _NtwsApConfRadioProfBeaconInterval_Type()
)
ntwsApConfRadioProfBeaconInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfBeaconInterval.setStatus("current")
_NtwsApConfRadioProfDtimInterval_Type = Unsigned32
_NtwsApConfRadioProfDtimInterval_Object = MibTableColumn
ntwsApConfRadioProfDtimInterval = _NtwsApConfRadioProfDtimInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 3),
    _NtwsApConfRadioProfDtimInterval_Type()
)
ntwsApConfRadioProfDtimInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfDtimInterval.setStatus("current")
_NtwsApConfRadioProfChannelWidth11na_Type = NtwsRadioChannelWidth
_NtwsApConfRadioProfChannelWidth11na_Object = MibTableColumn
ntwsApConfRadioProfChannelWidth11na = _NtwsApConfRadioProfChannelWidth11na_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 4),
    _NtwsApConfRadioProfChannelWidth11na_Type()
)
ntwsApConfRadioProfChannelWidth11na.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfChannelWidth11na.setStatus("current")
_NtwsApConfRadioProfMaxTxLifetime_Type = Unsigned32
_NtwsApConfRadioProfMaxTxLifetime_Object = MibTableColumn
ntwsApConfRadioProfMaxTxLifetime = _NtwsApConfRadioProfMaxTxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 5),
    _NtwsApConfRadioProfMaxTxLifetime_Type()
)
ntwsApConfRadioProfMaxTxLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfMaxTxLifetime.setStatus("current")
_NtwsApConfRadioProfMaxRxLifetime_Type = Unsigned32
_NtwsApConfRadioProfMaxRxLifetime_Object = MibTableColumn
ntwsApConfRadioProfMaxRxLifetime = _NtwsApConfRadioProfMaxRxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 6),
    _NtwsApConfRadioProfMaxRxLifetime_Type()
)
ntwsApConfRadioProfMaxRxLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfMaxRxLifetime.setStatus("current")
_NtwsApConfRadioProfRtsThreshold_Type = Unsigned32
_NtwsApConfRadioProfRtsThreshold_Object = MibTableColumn
ntwsApConfRadioProfRtsThreshold = _NtwsApConfRadioProfRtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 7),
    _NtwsApConfRadioProfRtsThreshold_Type()
)
ntwsApConfRadioProfRtsThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfRtsThreshold.setStatus("current")
_NtwsApConfRadioProfFragThreshold_Type = Unsigned32
_NtwsApConfRadioProfFragThreshold_Object = MibTableColumn
ntwsApConfRadioProfFragThreshold = _NtwsApConfRadioProfFragThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 8),
    _NtwsApConfRadioProfFragThreshold_Type()
)
ntwsApConfRadioProfFragThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfFragThreshold.setStatus("current")
_NtwsApConfRadioProfLongXmitPreambleEnabled_Type = TruthValue
_NtwsApConfRadioProfLongXmitPreambleEnabled_Object = MibTableColumn
ntwsApConfRadioProfLongXmitPreambleEnabled = _NtwsApConfRadioProfLongXmitPreambleEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 9),
    _NtwsApConfRadioProfLongXmitPreambleEnabled_Type()
)
ntwsApConfRadioProfLongXmitPreambleEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfLongXmitPreambleEnabled.setStatus("current")
_NtwsApConfRadioProfCountermeasuresMode_Type = NtwsRadioProfileCountermeasuresMode
_NtwsApConfRadioProfCountermeasuresMode_Object = MibTableColumn
ntwsApConfRadioProfCountermeasuresMode = _NtwsApConfRadioProfCountermeasuresMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 10),
    _NtwsApConfRadioProfCountermeasuresMode_Type()
)
ntwsApConfRadioProfCountermeasuresMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfCountermeasuresMode.setStatus("current")
_NtwsApConfRadioProfRFScanMode_Type = NtwsRadioProfileRFScanMode
_NtwsApConfRadioProfRFScanMode_Object = MibTableColumn
ntwsApConfRadioProfRFScanMode = _NtwsApConfRadioProfRFScanMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 11),
    _NtwsApConfRadioProfRFScanMode_Type()
)
ntwsApConfRadioProfRFScanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfRFScanMode.setStatus("current")
_NtwsApConfRadioProfRFScanChannelScope_Type = NtwsRadioProfileRFScanChannelScope
_NtwsApConfRadioProfRFScanChannelScope_Object = MibTableColumn
ntwsApConfRadioProfRFScanChannelScope = _NtwsApConfRadioProfRFScanChannelScope_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 12),
    _NtwsApConfRadioProfRFScanChannelScope_Type()
)
ntwsApConfRadioProfRFScanChannelScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfRFScanChannelScope.setStatus("current")
_NtwsApConfRadioProfRFScanCTSEnabled_Type = TruthValue
_NtwsApConfRadioProfRFScanCTSEnabled_Object = MibTableColumn
ntwsApConfRadioProfRFScanCTSEnabled = _NtwsApConfRadioProfRFScanCTSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 13),
    _NtwsApConfRadioProfRFScanCTSEnabled_Type()
)
ntwsApConfRadioProfRFScanCTSEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfRFScanCTSEnabled.setStatus("current")
_NtwsApConfRadioProfAutoTune11aChannelRange_Type = NtwsRadioProfileAutoTuneChannelRange
_NtwsApConfRadioProfAutoTune11aChannelRange_Object = MibTableColumn
ntwsApConfRadioProfAutoTune11aChannelRange = _NtwsApConfRadioProfAutoTune11aChannelRange_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 14),
    _NtwsApConfRadioProfAutoTune11aChannelRange_Type()
)
ntwsApConfRadioProfAutoTune11aChannelRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfAutoTune11aChannelRange.setStatus("current")
_NtwsApConfRadioProfAutoTuneIgnoreClientsEnabled_Type = TruthValue
_NtwsApConfRadioProfAutoTuneIgnoreClientsEnabled_Object = MibTableColumn
ntwsApConfRadioProfAutoTuneIgnoreClientsEnabled = _NtwsApConfRadioProfAutoTuneIgnoreClientsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 15),
    _NtwsApConfRadioProfAutoTuneIgnoreClientsEnabled_Type()
)
ntwsApConfRadioProfAutoTuneIgnoreClientsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfAutoTuneIgnoreClientsEnabled.setStatus("current")
_NtwsApConfRadioProfAutoTuneChannelEnabled_Type = TruthValue
_NtwsApConfRadioProfAutoTuneChannelEnabled_Object = MibTableColumn
ntwsApConfRadioProfAutoTuneChannelEnabled = _NtwsApConfRadioProfAutoTuneChannelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 16),
    _NtwsApConfRadioProfAutoTuneChannelEnabled_Type()
)
ntwsApConfRadioProfAutoTuneChannelEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfAutoTuneChannelEnabled.setStatus("current")
_NtwsApConfRadioProfAutoTuneChannelHolddownInterval_Type = Unsigned32
_NtwsApConfRadioProfAutoTuneChannelHolddownInterval_Object = MibTableColumn
ntwsApConfRadioProfAutoTuneChannelHolddownInterval = _NtwsApConfRadioProfAutoTuneChannelHolddownInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 17),
    _NtwsApConfRadioProfAutoTuneChannelHolddownInterval_Type()
)
ntwsApConfRadioProfAutoTuneChannelHolddownInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfAutoTuneChannelHolddownInterval.setStatus("current")
_NtwsApConfRadioProfAutoTuneChannelChangeInterval_Type = Unsigned32
_NtwsApConfRadioProfAutoTuneChannelChangeInterval_Object = MibTableColumn
ntwsApConfRadioProfAutoTuneChannelChangeInterval = _NtwsApConfRadioProfAutoTuneChannelChangeInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 18),
    _NtwsApConfRadioProfAutoTuneChannelChangeInterval_Type()
)
ntwsApConfRadioProfAutoTuneChannelChangeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfAutoTuneChannelChangeInterval.setStatus("current")
_NtwsApConfRadioProfAutoTunePowerEnabled_Type = TruthValue
_NtwsApConfRadioProfAutoTunePowerEnabled_Object = MibTableColumn
ntwsApConfRadioProfAutoTunePowerEnabled = _NtwsApConfRadioProfAutoTunePowerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 19),
    _NtwsApConfRadioProfAutoTunePowerEnabled_Type()
)
ntwsApConfRadioProfAutoTunePowerEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfAutoTunePowerEnabled.setStatus("current")
_NtwsApConfRadioProfAutoTunePowerRampInterval_Type = Unsigned32
_NtwsApConfRadioProfAutoTunePowerRampInterval_Object = MibTableColumn
ntwsApConfRadioProfAutoTunePowerRampInterval = _NtwsApConfRadioProfAutoTunePowerRampInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 20),
    _NtwsApConfRadioProfAutoTunePowerRampInterval_Type()
)
ntwsApConfRadioProfAutoTunePowerRampInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfAutoTunePowerRampInterval.setStatus("current")
_NtwsApConfRadioProfAutoTunePowerChangeInterval_Type = Unsigned32
_NtwsApConfRadioProfAutoTunePowerChangeInterval_Object = MibTableColumn
ntwsApConfRadioProfAutoTunePowerChangeInterval = _NtwsApConfRadioProfAutoTunePowerChangeInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 21),
    _NtwsApConfRadioProfAutoTunePowerChangeInterval_Type()
)
ntwsApConfRadioProfAutoTunePowerChangeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfAutoTunePowerChangeInterval.setStatus("current")
_NtwsApConfRadioProfFairQueuingEnabled_Type = TruthValue
_NtwsApConfRadioProfFairQueuingEnabled_Object = MibTableColumn
ntwsApConfRadioProfFairQueuingEnabled = _NtwsApConfRadioProfFairQueuingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 22),
    _NtwsApConfRadioProfFairQueuingEnabled_Type()
)
ntwsApConfRadioProfFairQueuingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfFairQueuingEnabled.setStatus("current")
_NtwsApConfRadioProfCacBackgroundACMandatory_Type = TruthValue
_NtwsApConfRadioProfCacBackgroundACMandatory_Object = MibTableColumn
ntwsApConfRadioProfCacBackgroundACMandatory = _NtwsApConfRadioProfCacBackgroundACMandatory_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 23),
    _NtwsApConfRadioProfCacBackgroundACMandatory_Type()
)
ntwsApConfRadioProfCacBackgroundACMandatory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfCacBackgroundACMandatory.setStatus("current")
_NtwsApConfRadioProfCacBackgroundMaxUtilization_Type = Unsigned32
_NtwsApConfRadioProfCacBackgroundMaxUtilization_Object = MibTableColumn
ntwsApConfRadioProfCacBackgroundMaxUtilization = _NtwsApConfRadioProfCacBackgroundMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 24),
    _NtwsApConfRadioProfCacBackgroundMaxUtilization_Type()
)
ntwsApConfRadioProfCacBackgroundMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfCacBackgroundMaxUtilization.setStatus("current")
_NtwsApConfRadioProfCacBackgroundPolicingEnabled_Type = TruthValue
_NtwsApConfRadioProfCacBackgroundPolicingEnabled_Object = MibTableColumn
ntwsApConfRadioProfCacBackgroundPolicingEnabled = _NtwsApConfRadioProfCacBackgroundPolicingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 25),
    _NtwsApConfRadioProfCacBackgroundPolicingEnabled_Type()
)
ntwsApConfRadioProfCacBackgroundPolicingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfCacBackgroundPolicingEnabled.setStatus("current")
_NtwsApConfRadioProfCacBestEffortACMandatory_Type = TruthValue
_NtwsApConfRadioProfCacBestEffortACMandatory_Object = MibTableColumn
ntwsApConfRadioProfCacBestEffortACMandatory = _NtwsApConfRadioProfCacBestEffortACMandatory_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 26),
    _NtwsApConfRadioProfCacBestEffortACMandatory_Type()
)
ntwsApConfRadioProfCacBestEffortACMandatory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfCacBestEffortACMandatory.setStatus("current")
_NtwsApConfRadioProfCacBestEffortMaxUtilization_Type = Unsigned32
_NtwsApConfRadioProfCacBestEffortMaxUtilization_Object = MibTableColumn
ntwsApConfRadioProfCacBestEffortMaxUtilization = _NtwsApConfRadioProfCacBestEffortMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 27),
    _NtwsApConfRadioProfCacBestEffortMaxUtilization_Type()
)
ntwsApConfRadioProfCacBestEffortMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfCacBestEffortMaxUtilization.setStatus("current")
_NtwsApConfRadioProfCacBestEffortPolicingEnabled_Type = TruthValue
_NtwsApConfRadioProfCacBestEffortPolicingEnabled_Object = MibTableColumn
ntwsApConfRadioProfCacBestEffortPolicingEnabled = _NtwsApConfRadioProfCacBestEffortPolicingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 28),
    _NtwsApConfRadioProfCacBestEffortPolicingEnabled_Type()
)
ntwsApConfRadioProfCacBestEffortPolicingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfCacBestEffortPolicingEnabled.setStatus("current")
_NtwsApConfRadioProfCacVideoACMandatory_Type = TruthValue
_NtwsApConfRadioProfCacVideoACMandatory_Object = MibTableColumn
ntwsApConfRadioProfCacVideoACMandatory = _NtwsApConfRadioProfCacVideoACMandatory_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 29),
    _NtwsApConfRadioProfCacVideoACMandatory_Type()
)
ntwsApConfRadioProfCacVideoACMandatory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfCacVideoACMandatory.setStatus("current")
_NtwsApConfRadioProfCacVideoMaxUtilization_Type = Unsigned32
_NtwsApConfRadioProfCacVideoMaxUtilization_Object = MibTableColumn
ntwsApConfRadioProfCacVideoMaxUtilization = _NtwsApConfRadioProfCacVideoMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 30),
    _NtwsApConfRadioProfCacVideoMaxUtilization_Type()
)
ntwsApConfRadioProfCacVideoMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfCacVideoMaxUtilization.setStatus("current")
_NtwsApConfRadioProfCacVideoPolicingEnabled_Type = TruthValue
_NtwsApConfRadioProfCacVideoPolicingEnabled_Object = MibTableColumn
ntwsApConfRadioProfCacVideoPolicingEnabled = _NtwsApConfRadioProfCacVideoPolicingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 31),
    _NtwsApConfRadioProfCacVideoPolicingEnabled_Type()
)
ntwsApConfRadioProfCacVideoPolicingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfCacVideoPolicingEnabled.setStatus("current")
_NtwsApConfRadioProfCacVoiceACMandatory_Type = TruthValue
_NtwsApConfRadioProfCacVoiceACMandatory_Object = MibTableColumn
ntwsApConfRadioProfCacVoiceACMandatory = _NtwsApConfRadioProfCacVoiceACMandatory_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 32),
    _NtwsApConfRadioProfCacVoiceACMandatory_Type()
)
ntwsApConfRadioProfCacVoiceACMandatory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfCacVoiceACMandatory.setStatus("current")
_NtwsApConfRadioProfCacVoiceMaxUtilization_Type = Unsigned32
_NtwsApConfRadioProfCacVoiceMaxUtilization_Object = MibTableColumn
ntwsApConfRadioProfCacVoiceMaxUtilization = _NtwsApConfRadioProfCacVoiceMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 33),
    _NtwsApConfRadioProfCacVoiceMaxUtilization_Type()
)
ntwsApConfRadioProfCacVoiceMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfCacVoiceMaxUtilization.setStatus("current")
_NtwsApConfRadioProfCacVoicePolicingEnabled_Type = TruthValue
_NtwsApConfRadioProfCacVoicePolicingEnabled_Object = MibTableColumn
ntwsApConfRadioProfCacVoicePolicingEnabled = _NtwsApConfRadioProfCacVoicePolicingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 34),
    _NtwsApConfRadioProfCacVoicePolicingEnabled_Type()
)
ntwsApConfRadioProfCacVoicePolicingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfCacVoicePolicingEnabled.setStatus("current")
_NtwsApConfRadioProfRfidTagEnabled_Type = TruthValue
_NtwsApConfRadioProfRfidTagEnabled_Object = MibTableColumn
ntwsApConfRadioProfRfidTagEnabled = _NtwsApConfRadioProfRfidTagEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 35),
    _NtwsApConfRadioProfRfidTagEnabled_Type()
)
ntwsApConfRadioProfRfidTagEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfRfidTagEnabled.setStatus("current")
_NtwsApConfRadioProfWmmPowerSaveEnabled_Type = TruthValue
_NtwsApConfRadioProfWmmPowerSaveEnabled_Object = MibTableColumn
ntwsApConfRadioProfWmmPowerSaveEnabled = _NtwsApConfRadioProfWmmPowerSaveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 36),
    _NtwsApConfRadioProfWmmPowerSaveEnabled_Type()
)
ntwsApConfRadioProfWmmPowerSaveEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfWmmPowerSaveEnabled.setStatus("current")
_NtwsApConfRadioProfRateEnforcementEnabled_Type = TruthValue
_NtwsApConfRadioProfRateEnforcementEnabled_Object = MibTableColumn
ntwsApConfRadioProfRateEnforcementEnabled = _NtwsApConfRadioProfRateEnforcementEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 37),
    _NtwsApConfRadioProfRateEnforcementEnabled_Type()
)
ntwsApConfRadioProfRateEnforcementEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfRateEnforcementEnabled.setStatus("current")
_NtwsApConfRadioProfDfsChannelsEnabled_Type = TruthValue
_NtwsApConfRadioProfDfsChannelsEnabled_Object = MibTableColumn
ntwsApConfRadioProfDfsChannelsEnabled = _NtwsApConfRadioProfDfsChannelsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 6, 1, 38),
    _NtwsApConfRadioProfDfsChannelsEnabled_Type()
)
ntwsApConfRadioProfDfsChannelsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfRadioProfDfsChannelsEnabled.setStatus("current")
_NtwsApConfRadioProfServiceProfileTable_Object = MibTable
ntwsApConfRadioProfServiceProfileTable = _NtwsApConfRadioProfServiceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 7)
)
if mibBuilder.loadTexts:
    ntwsApConfRadioProfServiceProfileTable.setStatus("current")
_NtwsApConfRadioProfServiceProfileEntry_Object = MibTableRow
ntwsApConfRadioProfServiceProfileEntry = _NtwsApConfRadioProfServiceProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 7, 1)
)
ntwsApConfRadioProfServiceProfileEntry.setIndexNames(
    (0, "NTWS-AP-CONFIG-MIB", "ntwsApConfRpServpRadioProfileName"),
    (0, "NTWS-AP-CONFIG-MIB", "ntwsApConfRpServpServiceProfileName"),
)
if mibBuilder.loadTexts:
    ntwsApConfRadioProfServiceProfileEntry.setStatus("current")
_NtwsApConfRpServpRadioProfileName_Type = NtwsRadioProfileName
_NtwsApConfRpServpRadioProfileName_Object = MibTableColumn
ntwsApConfRpServpRadioProfileName = _NtwsApConfRpServpRadioProfileName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 7, 1, 1),
    _NtwsApConfRpServpRadioProfileName_Type()
)
ntwsApConfRpServpRadioProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApConfRpServpRadioProfileName.setStatus("current")
_NtwsApConfRpServpServiceProfileName_Type = NtwsServiceProfileName
_NtwsApConfRpServpServiceProfileName_Object = MibTableColumn
ntwsApConfRpServpServiceProfileName = _NtwsApConfRpServpServiceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 7, 1, 2),
    _NtwsApConfRpServpServiceProfileName_Type()
)
ntwsApConfRpServpServiceProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApConfRpServpServiceProfileName.setStatus("current")
_NtwsApConfRpServpRowStatus_Type = RowStatus
_NtwsApConfRpServpRowStatus_Object = MibTableColumn
ntwsApConfRpServpRowStatus = _NtwsApConfRpServpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 7, 1, 3),
    _NtwsApConfRpServpRowStatus_Type()
)
ntwsApConfRpServpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntwsApConfRpServpRowStatus.setStatus("current")
_NtwsApConfRadioProfSnoopFilterTable_Object = MibTable
ntwsApConfRadioProfSnoopFilterTable = _NtwsApConfRadioProfSnoopFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 8)
)
if mibBuilder.loadTexts:
    ntwsApConfRadioProfSnoopFilterTable.setStatus("current")
_NtwsApConfRadioProfSnoopFilterEntry_Object = MibTableRow
ntwsApConfRadioProfSnoopFilterEntry = _NtwsApConfRadioProfSnoopFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 8, 1)
)
ntwsApConfRadioProfSnoopFilterEntry.setIndexNames(
    (0, "NTWS-AP-CONFIG-MIB", "ntwsApConfRpSnoopfRadioProfileName"),
    (0, "NTWS-AP-CONFIG-MIB", "ntwsApConfRpSnoopfSnoopFilterName"),
)
if mibBuilder.loadTexts:
    ntwsApConfRadioProfSnoopFilterEntry.setStatus("current")
_NtwsApConfRpSnoopfRadioProfileName_Type = NtwsRadioProfileName
_NtwsApConfRpSnoopfRadioProfileName_Object = MibTableColumn
ntwsApConfRpSnoopfRadioProfileName = _NtwsApConfRpSnoopfRadioProfileName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 8, 1, 1),
    _NtwsApConfRpSnoopfRadioProfileName_Type()
)
ntwsApConfRpSnoopfRadioProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApConfRpSnoopfRadioProfileName.setStatus("current")
_NtwsApConfRpSnoopfSnoopFilterName_Type = NtwsSnoopFilterName
_NtwsApConfRpSnoopfSnoopFilterName_Object = MibTableColumn
ntwsApConfRpSnoopfSnoopFilterName = _NtwsApConfRpSnoopfSnoopFilterName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 8, 1, 2),
    _NtwsApConfRpSnoopfSnoopFilterName_Type()
)
ntwsApConfRpSnoopfSnoopFilterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApConfRpSnoopfSnoopFilterName.setStatus("current")
_NtwsApConfRpSnoopfRowStatus_Type = RowStatus
_NtwsApConfRpSnoopfRowStatus_Object = MibTableColumn
ntwsApConfRpSnoopfRowStatus = _NtwsApConfRpSnoopfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 8, 1, 3),
    _NtwsApConfRpSnoopfRowStatus_Type()
)
ntwsApConfRpSnoopfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntwsApConfRpSnoopfRowStatus.setStatus("current")
_NtwsApConfServiceProfileTable_Object = MibTable
ntwsApConfServiceProfileTable = _NtwsApConfServiceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9)
)
if mibBuilder.loadTexts:
    ntwsApConfServiceProfileTable.setStatus("current")
_NtwsApConfServiceProfileEntry_Object = MibTableRow
ntwsApConfServiceProfileEntry = _NtwsApConfServiceProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1)
)
ntwsApConfServiceProfileEntry.setIndexNames(
    (0, "NTWS-AP-CONFIG-MIB", "ntwsApConfServProfServiceProfileName"),
)
if mibBuilder.loadTexts:
    ntwsApConfServiceProfileEntry.setStatus("current")
_NtwsApConfServProfServiceProfileName_Type = NtwsServiceProfileName
_NtwsApConfServProfServiceProfileName_Object = MibTableColumn
ntwsApConfServProfServiceProfileName = _NtwsApConfServProfServiceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 1),
    _NtwsApConfServProfServiceProfileName_Type()
)
ntwsApConfServProfServiceProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApConfServProfServiceProfileName.setStatus("current")
_NtwsApConfServProfSsidType_Type = NtwsServiceProfileSsidType
_NtwsApConfServProfSsidType_Object = MibTableColumn
ntwsApConfServProfSsidType = _NtwsApConfServProfSsidType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 2),
    _NtwsApConfServProfSsidType_Type()
)
ntwsApConfServProfSsidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfSsidType.setStatus("current")
_NtwsApConfServProfBeaconEnabled_Type = TruthValue
_NtwsApConfServProfBeaconEnabled_Object = MibTableColumn
ntwsApConfServProfBeaconEnabled = _NtwsApConfServProfBeaconEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 3),
    _NtwsApConfServProfBeaconEnabled_Type()
)
ntwsApConfServProfBeaconEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfBeaconEnabled.setStatus("current")
_NtwsApConfServProf11naMode_Type = NtwsServiceProfile11nMode
_NtwsApConfServProf11naMode_Object = MibTableColumn
ntwsApConfServProf11naMode = _NtwsApConfServProf11naMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 4),
    _NtwsApConfServProf11naMode_Type()
)
ntwsApConfServProf11naMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProf11naMode.setStatus("current")
_NtwsApConfServProf11ngMode_Type = NtwsServiceProfile11nMode
_NtwsApConfServProf11ngMode_Object = MibTableColumn
ntwsApConfServProf11ngMode = _NtwsApConfServProf11ngMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 5),
    _NtwsApConfServProf11ngMode_Type()
)
ntwsApConfServProf11ngMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProf11ngMode.setStatus("current")
_NtwsApConfServProf11nShortGuardIntervalEnabled_Type = TruthValue
_NtwsApConfServProf11nShortGuardIntervalEnabled_Object = MibTableColumn
ntwsApConfServProf11nShortGuardIntervalEnabled = _NtwsApConfServProf11nShortGuardIntervalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 6),
    _NtwsApConfServProf11nShortGuardIntervalEnabled_Type()
)
ntwsApConfServProf11nShortGuardIntervalEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProf11nShortGuardIntervalEnabled.setStatus("current")
_NtwsApConfServProf11nFrameAggregation_Type = NtwsServiceProfile11nFrameAggregationType
_NtwsApConfServProf11nFrameAggregation_Object = MibTableColumn
ntwsApConfServProf11nFrameAggregation = _NtwsApConfServProf11nFrameAggregation_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 7),
    _NtwsApConfServProf11nFrameAggregation_Type()
)
ntwsApConfServProf11nFrameAggregation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProf11nFrameAggregation.setStatus("current")
_NtwsApConfServProf11nMsduMaxLength_Type = NtwsServiceProfile11nMsduMaxLength
_NtwsApConfServProf11nMsduMaxLength_Object = MibTableColumn
ntwsApConfServProf11nMsduMaxLength = _NtwsApConfServProf11nMsduMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 8),
    _NtwsApConfServProf11nMsduMaxLength_Type()
)
ntwsApConfServProf11nMsduMaxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProf11nMsduMaxLength.setStatus("current")
_NtwsApConfServProf11nMpduMaxLength_Type = NtwsServiceProfile11nMpduMaxLength
_NtwsApConfServProf11nMpduMaxLength_Object = MibTableColumn
ntwsApConfServProf11nMpduMaxLength = _NtwsApConfServProf11nMpduMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 9),
    _NtwsApConfServProf11nMpduMaxLength_Type()
)
ntwsApConfServProf11nMpduMaxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProf11nMpduMaxLength.setStatus("current")
_NtwsApConfServProfAuthFallthru_Type = NtwsServiceProfileAuthFallthruType
_NtwsApConfServProfAuthFallthru_Object = MibTableColumn
ntwsApConfServProfAuthFallthru = _NtwsApConfServProfAuthFallthru_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 10),
    _NtwsApConfServProfAuthFallthru_Type()
)
ntwsApConfServProfAuthFallthru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfAuthFallthru.setStatus("current")


class _NtwsApConfServProfWebAAAForm_Type(DisplayString):
    """Custom type ntwsApConfServProfWebAAAForm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NtwsApConfServProfWebAAAForm_Type.__name__ = "DisplayString"
_NtwsApConfServProfWebAAAForm_Object = MibTableColumn
ntwsApConfServProfWebAAAForm = _NtwsApConfServProfWebAAAForm_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 11),
    _NtwsApConfServProfWebAAAForm_Type()
)
ntwsApConfServProfWebAAAForm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfWebAAAForm.setStatus("current")
_NtwsApConfServProfSharedKeyAuthEnabled_Type = TruthValue
_NtwsApConfServProfSharedKeyAuthEnabled_Object = MibTableColumn
ntwsApConfServProfSharedKeyAuthEnabled = _NtwsApConfServProfSharedKeyAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 12),
    _NtwsApConfServProfSharedKeyAuthEnabled_Type()
)
ntwsApConfServProfSharedKeyAuthEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfSharedKeyAuthEnabled.setStatus("current")
_NtwsApConfServProfWpaIeEnabled_Type = TruthValue
_NtwsApConfServProfWpaIeEnabled_Object = MibTableColumn
ntwsApConfServProfWpaIeEnabled = _NtwsApConfServProfWpaIeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 13),
    _NtwsApConfServProfWpaIeEnabled_Type()
)
ntwsApConfServProfWpaIeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfWpaIeEnabled.setStatus("current")
_NtwsApConfServProfWpaIeCipherTkipEnabled_Type = TruthValue
_NtwsApConfServProfWpaIeCipherTkipEnabled_Object = MibTableColumn
ntwsApConfServProfWpaIeCipherTkipEnabled = _NtwsApConfServProfWpaIeCipherTkipEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 14),
    _NtwsApConfServProfWpaIeCipherTkipEnabled_Type()
)
ntwsApConfServProfWpaIeCipherTkipEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfWpaIeCipherTkipEnabled.setStatus("current")
_NtwsApConfServProfWpaIeCipherCcmpEnabled_Type = TruthValue
_NtwsApConfServProfWpaIeCipherCcmpEnabled_Object = MibTableColumn
ntwsApConfServProfWpaIeCipherCcmpEnabled = _NtwsApConfServProfWpaIeCipherCcmpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 15),
    _NtwsApConfServProfWpaIeCipherCcmpEnabled_Type()
)
ntwsApConfServProfWpaIeCipherCcmpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfWpaIeCipherCcmpEnabled.setStatus("current")
_NtwsApConfServProfWpaIeCipherWep40Enabled_Type = TruthValue
_NtwsApConfServProfWpaIeCipherWep40Enabled_Object = MibTableColumn
ntwsApConfServProfWpaIeCipherWep40Enabled = _NtwsApConfServProfWpaIeCipherWep40Enabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 16),
    _NtwsApConfServProfWpaIeCipherWep40Enabled_Type()
)
ntwsApConfServProfWpaIeCipherWep40Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfWpaIeCipherWep40Enabled.setStatus("current")
_NtwsApConfServProfWpaIeCipherWep104Enabled_Type = TruthValue
_NtwsApConfServProfWpaIeCipherWep104Enabled_Object = MibTableColumn
ntwsApConfServProfWpaIeCipherWep104Enabled = _NtwsApConfServProfWpaIeCipherWep104Enabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 17),
    _NtwsApConfServProfWpaIeCipherWep104Enabled_Type()
)
ntwsApConfServProfWpaIeCipherWep104Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfWpaIeCipherWep104Enabled.setStatus("current")
_NtwsApConfServProfWpaIeAuthDot1xEnabled_Type = TruthValue
_NtwsApConfServProfWpaIeAuthDot1xEnabled_Object = MibTableColumn
ntwsApConfServProfWpaIeAuthDot1xEnabled = _NtwsApConfServProfWpaIeAuthDot1xEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 18),
    _NtwsApConfServProfWpaIeAuthDot1xEnabled_Type()
)
ntwsApConfServProfWpaIeAuthDot1xEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfWpaIeAuthDot1xEnabled.setStatus("current")
_NtwsApConfServProfWpaIeAuthPskEnabled_Type = TruthValue
_NtwsApConfServProfWpaIeAuthPskEnabled_Object = MibTableColumn
ntwsApConfServProfWpaIeAuthPskEnabled = _NtwsApConfServProfWpaIeAuthPskEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 19),
    _NtwsApConfServProfWpaIeAuthPskEnabled_Type()
)
ntwsApConfServProfWpaIeAuthPskEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfWpaIeAuthPskEnabled.setStatus("current")
_NtwsApConfServProfRsnIeEnabled_Type = TruthValue
_NtwsApConfServProfRsnIeEnabled_Object = MibTableColumn
ntwsApConfServProfRsnIeEnabled = _NtwsApConfServProfRsnIeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 20),
    _NtwsApConfServProfRsnIeEnabled_Type()
)
ntwsApConfServProfRsnIeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfRsnIeEnabled.setStatus("current")
_NtwsApConfServProfRsnIeCipherTkipEnabled_Type = TruthValue
_NtwsApConfServProfRsnIeCipherTkipEnabled_Object = MibTableColumn
ntwsApConfServProfRsnIeCipherTkipEnabled = _NtwsApConfServProfRsnIeCipherTkipEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 21),
    _NtwsApConfServProfRsnIeCipherTkipEnabled_Type()
)
ntwsApConfServProfRsnIeCipherTkipEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfRsnIeCipherTkipEnabled.setStatus("current")
_NtwsApConfServProfRsnIeCipherCcmpEnabled_Type = TruthValue
_NtwsApConfServProfRsnIeCipherCcmpEnabled_Object = MibTableColumn
ntwsApConfServProfRsnIeCipherCcmpEnabled = _NtwsApConfServProfRsnIeCipherCcmpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 22),
    _NtwsApConfServProfRsnIeCipherCcmpEnabled_Type()
)
ntwsApConfServProfRsnIeCipherCcmpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfRsnIeCipherCcmpEnabled.setStatus("current")
_NtwsApConfServProfRsnIeCipherWep40Enabled_Type = TruthValue
_NtwsApConfServProfRsnIeCipherWep40Enabled_Object = MibTableColumn
ntwsApConfServProfRsnIeCipherWep40Enabled = _NtwsApConfServProfRsnIeCipherWep40Enabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 23),
    _NtwsApConfServProfRsnIeCipherWep40Enabled_Type()
)
ntwsApConfServProfRsnIeCipherWep40Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfRsnIeCipherWep40Enabled.setStatus("current")
_NtwsApConfServProfRsnIeCipherWep104Enabled_Type = TruthValue
_NtwsApConfServProfRsnIeCipherWep104Enabled_Object = MibTableColumn
ntwsApConfServProfRsnIeCipherWep104Enabled = _NtwsApConfServProfRsnIeCipherWep104Enabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 24),
    _NtwsApConfServProfRsnIeCipherWep104Enabled_Type()
)
ntwsApConfServProfRsnIeCipherWep104Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfRsnIeCipherWep104Enabled.setStatus("current")
_NtwsApConfServProfRsnIeAuthDot1xEnabled_Type = TruthValue
_NtwsApConfServProfRsnIeAuthDot1xEnabled_Object = MibTableColumn
ntwsApConfServProfRsnIeAuthDot1xEnabled = _NtwsApConfServProfRsnIeAuthDot1xEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 25),
    _NtwsApConfServProfRsnIeAuthDot1xEnabled_Type()
)
ntwsApConfServProfRsnIeAuthDot1xEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfRsnIeAuthDot1xEnabled.setStatus("current")
_NtwsApConfServProfRsnIeAuthPskEnabled_Type = TruthValue
_NtwsApConfServProfRsnIeAuthPskEnabled_Object = MibTableColumn
ntwsApConfServProfRsnIeAuthPskEnabled = _NtwsApConfServProfRsnIeAuthPskEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 26),
    _NtwsApConfServProfRsnIeAuthPskEnabled_Type()
)
ntwsApConfServProfRsnIeAuthPskEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfRsnIeAuthPskEnabled.setStatus("current")
_NtwsApConfServProfTkipMicCountermeasuresTime_Type = Unsigned32
_NtwsApConfServProfTkipMicCountermeasuresTime_Object = MibTableColumn
ntwsApConfServProfTkipMicCountermeasuresTime = _NtwsApConfServProfTkipMicCountermeasuresTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 27),
    _NtwsApConfServProfTkipMicCountermeasuresTime_Type()
)
ntwsApConfServProfTkipMicCountermeasuresTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfTkipMicCountermeasuresTime.setStatus("current")
_NtwsApConfServProfMaxBandwidthKbps_Type = Unsigned32
_NtwsApConfServProfMaxBandwidthKbps_Object = MibTableColumn
ntwsApConfServProfMaxBandwidthKbps = _NtwsApConfServProfMaxBandwidthKbps_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 28),
    _NtwsApConfServProfMaxBandwidthKbps_Type()
)
ntwsApConfServProfMaxBandwidthKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfMaxBandwidthKbps.setStatus("current")
_NtwsApConfServProfCacMode_Type = NtwsServiceProfileCacMode
_NtwsApConfServProfCacMode_Object = MibTableColumn
ntwsApConfServProfCacMode = _NtwsApConfServProfCacMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 29),
    _NtwsApConfServProfCacMode_Type()
)
ntwsApConfServProfCacMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfCacMode.setStatus("current")
_NtwsApConfServProfCacSessCount_Type = Unsigned32
_NtwsApConfServProfCacSessCount_Object = MibTableColumn
ntwsApConfServProfCacSessCount = _NtwsApConfServProfCacSessCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 30),
    _NtwsApConfServProfCacSessCount_Type()
)
ntwsApConfServProfCacSessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfCacSessCount.setStatus("current")
_NtwsApConfServProfUserIdleTimeout_Type = Unsigned32
_NtwsApConfServProfUserIdleTimeout_Object = MibTableColumn
ntwsApConfServProfUserIdleTimeout = _NtwsApConfServProfUserIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 31),
    _NtwsApConfServProfUserIdleTimeout_Type()
)
ntwsApConfServProfUserIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfUserIdleTimeout.setStatus("current")
_NtwsApConfServProfIdleClientProbingEnabled_Type = TruthValue
_NtwsApConfServProfIdleClientProbingEnabled_Object = MibTableColumn
ntwsApConfServProfIdleClientProbingEnabled = _NtwsApConfServProfIdleClientProbingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 32),
    _NtwsApConfServProfIdleClientProbingEnabled_Type()
)
ntwsApConfServProfIdleClientProbingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfIdleClientProbingEnabled.setStatus("current")
_NtwsApConfServProfShortRetryCount_Type = Unsigned32
_NtwsApConfServProfShortRetryCount_Object = MibTableColumn
ntwsApConfServProfShortRetryCount = _NtwsApConfServProfShortRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 33),
    _NtwsApConfServProfShortRetryCount_Type()
)
ntwsApConfServProfShortRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfShortRetryCount.setStatus("current")
_NtwsApConfServProfLongRetryCount_Type = Unsigned32
_NtwsApConfServProfLongRetryCount_Object = MibTableColumn
ntwsApConfServProfLongRetryCount = _NtwsApConfServProfLongRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 34),
    _NtwsApConfServProfLongRetryCount_Type()
)
ntwsApConfServProfLongRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfLongRetryCount.setStatus("current")
_NtwsApConfServProfProxyArpEnabled_Type = TruthValue
_NtwsApConfServProfProxyArpEnabled_Object = MibTableColumn
ntwsApConfServProfProxyArpEnabled = _NtwsApConfServProfProxyArpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 35),
    _NtwsApConfServProfProxyArpEnabled_Type()
)
ntwsApConfServProfProxyArpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfProxyArpEnabled.setStatus("current")
_NtwsApConfServProfDhcpRestrictEnabled_Type = TruthValue
_NtwsApConfServProfDhcpRestrictEnabled_Object = MibTableColumn
ntwsApConfServProfDhcpRestrictEnabled = _NtwsApConfServProfDhcpRestrictEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 36),
    _NtwsApConfServProfDhcpRestrictEnabled_Type()
)
ntwsApConfServProfDhcpRestrictEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfDhcpRestrictEnabled.setStatus("current")
_NtwsApConfServProfNoBroadcastEnabled_Type = TruthValue
_NtwsApConfServProfNoBroadcastEnabled_Object = MibTableColumn
ntwsApConfServProfNoBroadcastEnabled = _NtwsApConfServProfNoBroadcastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 37),
    _NtwsApConfServProfNoBroadcastEnabled_Type()
)
ntwsApConfServProfNoBroadcastEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfNoBroadcastEnabled.setStatus("current")
_NtwsApConfServProfSygateOnDemandEnabled_Type = TruthValue
_NtwsApConfServProfSygateOnDemandEnabled_Object = MibTableColumn
ntwsApConfServProfSygateOnDemandEnabled = _NtwsApConfServProfSygateOnDemandEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 38),
    _NtwsApConfServProfSygateOnDemandEnabled_Type()
)
ntwsApConfServProfSygateOnDemandEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfSygateOnDemandEnabled.setStatus("current")
_NtwsApConfServProfEnforceChecksEnabled_Type = TruthValue
_NtwsApConfServProfEnforceChecksEnabled_Object = MibTableColumn
ntwsApConfServProfEnforceChecksEnabled = _NtwsApConfServProfEnforceChecksEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 39),
    _NtwsApConfServProfEnforceChecksEnabled_Type()
)
ntwsApConfServProfEnforceChecksEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfEnforceChecksEnabled.setStatus("current")


class _NtwsApConfServProfSodaRemediationAcl_Type(DisplayString):
    """Custom type ntwsApConfServProfSodaRemediationAcl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtwsApConfServProfSodaRemediationAcl_Type.__name__ = "DisplayString"
_NtwsApConfServProfSodaRemediationAcl_Object = MibTableColumn
ntwsApConfServProfSodaRemediationAcl = _NtwsApConfServProfSodaRemediationAcl_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 40),
    _NtwsApConfServProfSodaRemediationAcl_Type()
)
ntwsApConfServProfSodaRemediationAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfSodaRemediationAcl.setStatus("current")


class _NtwsApConfServProfSodaSuccessPage_Type(DisplayString):
    """Custom type ntwsApConfServProfSodaSuccessPage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtwsApConfServProfSodaSuccessPage_Type.__name__ = "DisplayString"
_NtwsApConfServProfSodaSuccessPage_Object = MibTableColumn
ntwsApConfServProfSodaSuccessPage = _NtwsApConfServProfSodaSuccessPage_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 41),
    _NtwsApConfServProfSodaSuccessPage_Type()
)
ntwsApConfServProfSodaSuccessPage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfSodaSuccessPage.setStatus("current")


class _NtwsApConfServProfSodaFailurePage_Type(DisplayString):
    """Custom type ntwsApConfServProfSodaFailurePage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtwsApConfServProfSodaFailurePage_Type.__name__ = "DisplayString"
_NtwsApConfServProfSodaFailurePage_Object = MibTableColumn
ntwsApConfServProfSodaFailurePage = _NtwsApConfServProfSodaFailurePage_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 42),
    _NtwsApConfServProfSodaFailurePage_Type()
)
ntwsApConfServProfSodaFailurePage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfSodaFailurePage.setStatus("current")


class _NtwsApConfServProfSodaLogoutPage_Type(DisplayString):
    """Custom type ntwsApConfServProfSodaLogoutPage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtwsApConfServProfSodaLogoutPage_Type.__name__ = "DisplayString"
_NtwsApConfServProfSodaLogoutPage_Object = MibTableColumn
ntwsApConfServProfSodaLogoutPage = _NtwsApConfServProfSodaLogoutPage_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 43),
    _NtwsApConfServProfSodaLogoutPage_Type()
)
ntwsApConfServProfSodaLogoutPage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfSodaLogoutPage.setStatus("current")


class _NtwsApConfServProfSodaAgentDirectory_Type(DisplayString):
    """Custom type ntwsApConfServProfSodaAgentDirectory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtwsApConfServProfSodaAgentDirectory_Type.__name__ = "DisplayString"
_NtwsApConfServProfSodaAgentDirectory_Object = MibTableColumn
ntwsApConfServProfSodaAgentDirectory = _NtwsApConfServProfSodaAgentDirectory_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 44),
    _NtwsApConfServProfSodaAgentDirectory_Type()
)
ntwsApConfServProfSodaAgentDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfSodaAgentDirectory.setStatus("current")
_NtwsApConfServProfWebPortalSessionTimeout_Type = Unsigned32
_NtwsApConfServProfWebPortalSessionTimeout_Object = MibTableColumn
ntwsApConfServProfWebPortalSessionTimeout = _NtwsApConfServProfWebPortalSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 45),
    _NtwsApConfServProfWebPortalSessionTimeout_Type()
)
ntwsApConfServProfWebPortalSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfWebPortalSessionTimeout.setStatus("current")


class _NtwsApConfServProfWebPortalAcl_Type(DisplayString):
    """Custom type ntwsApConfServProfWebPortalAcl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtwsApConfServProfWebPortalAcl_Type.__name__ = "DisplayString"
_NtwsApConfServProfWebPortalAcl_Object = MibTableColumn
ntwsApConfServProfWebPortalAcl = _NtwsApConfServProfWebPortalAcl_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 46),
    _NtwsApConfServProfWebPortalAcl_Type()
)
ntwsApConfServProfWebPortalAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfWebPortalAcl.setStatus("current")
_NtwsApConfServProfWebPortalLogoutEnabled_Type = TruthValue
_NtwsApConfServProfWebPortalLogoutEnabled_Object = MibTableColumn
ntwsApConfServProfWebPortalLogoutEnabled = _NtwsApConfServProfWebPortalLogoutEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 47),
    _NtwsApConfServProfWebPortalLogoutEnabled_Type()
)
ntwsApConfServProfWebPortalLogoutEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfWebPortalLogoutEnabled.setStatus("current")


class _NtwsApConfServProfWebPortalLogoutUrl_Type(DisplayString):
    """Custom type ntwsApConfServProfWebPortalLogoutUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NtwsApConfServProfWebPortalLogoutUrl_Type.__name__ = "DisplayString"
_NtwsApConfServProfWebPortalLogoutUrl_Object = MibTableColumn
ntwsApConfServProfWebPortalLogoutUrl = _NtwsApConfServProfWebPortalLogoutUrl_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 48),
    _NtwsApConfServProfWebPortalLogoutUrl_Type()
)
ntwsApConfServProfWebPortalLogoutUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfWebPortalLogoutUrl.setStatus("current")
_NtwsApConfServProfKeepInitialVlanEnabled_Type = TruthValue
_NtwsApConfServProfKeepInitialVlanEnabled_Object = MibTableColumn
ntwsApConfServProfKeepInitialVlanEnabled = _NtwsApConfServProfKeepInitialVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 49),
    _NtwsApConfServProfKeepInitialVlanEnabled_Type()
)
ntwsApConfServProfKeepInitialVlanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfKeepInitialVlanEnabled.setStatus("current")
_NtwsApConfServProfMeshModeEnabled_Type = TruthValue
_NtwsApConfServProfMeshModeEnabled_Object = MibTableColumn
ntwsApConfServProfMeshModeEnabled = _NtwsApConfServProfMeshModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 50),
    _NtwsApConfServProfMeshModeEnabled_Type()
)
ntwsApConfServProfMeshModeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfMeshModeEnabled.setStatus("current")
_NtwsApConfServProfBridgingEnabled_Type = TruthValue
_NtwsApConfServProfBridgingEnabled_Object = MibTableColumn
ntwsApConfServProfBridgingEnabled = _NtwsApConfServProfBridgingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 51),
    _NtwsApConfServProfBridgingEnabled_Type()
)
ntwsApConfServProfBridgingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfBridgingEnabled.setStatus("current")
_NtwsApConfServProfLoadBalanceExemptEnabled_Type = TruthValue
_NtwsApConfServProfLoadBalanceExemptEnabled_Object = MibTableColumn
ntwsApConfServProfLoadBalanceExemptEnabled = _NtwsApConfServProfLoadBalanceExemptEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 9, 1, 52),
    _NtwsApConfServProfLoadBalanceExemptEnabled_Type()
)
ntwsApConfServProfLoadBalanceExemptEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfServProfLoadBalanceExemptEnabled.setStatus("current")
_NtwsApConfSnoopFilterTable_Object = MibTable
ntwsApConfSnoopFilterTable = _NtwsApConfSnoopFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 10)
)
if mibBuilder.loadTexts:
    ntwsApConfSnoopFilterTable.setStatus("current")
_NtwsApConfSnoopFilterEntry_Object = MibTableRow
ntwsApConfSnoopFilterEntry = _NtwsApConfSnoopFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 10, 1)
)
ntwsApConfSnoopFilterEntry.setIndexNames(
    (0, "NTWS-AP-CONFIG-MIB", "ntwsApConfSnoopFilterName"),
)
if mibBuilder.loadTexts:
    ntwsApConfSnoopFilterEntry.setStatus("current")
_NtwsApConfSnoopFilterName_Type = NtwsSnoopFilterName
_NtwsApConfSnoopFilterName_Object = MibTableColumn
ntwsApConfSnoopFilterName = _NtwsApConfSnoopFilterName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 10, 1, 1),
    _NtwsApConfSnoopFilterName_Type()
)
ntwsApConfSnoopFilterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApConfSnoopFilterName.setStatus("current")
_NtwsApConfSnoopFilterEnabled_Type = TruthValue
_NtwsApConfSnoopFilterEnabled_Object = MibTableColumn
ntwsApConfSnoopFilterEnabled = _NtwsApConfSnoopFilterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 1, 10, 1, 2),
    _NtwsApConfSnoopFilterEnabled_Type()
)
ntwsApConfSnoopFilterEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApConfSnoopFilterEnabled.setStatus("current")
_NtwsApConfigConformance_ObjectIdentity = ObjectIdentity
ntwsApConfigConformance = _NtwsApConfigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 2)
)
_NtwsApConfigCompliances_ObjectIdentity = ObjectIdentity
ntwsApConfigCompliances = _NtwsApConfigCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 2, 1)
)
_NtwsApConfigGroups_ObjectIdentity = ObjectIdentity
ntwsApConfigGroups = _NtwsApConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 2, 2)
)

# Managed Objects groups

ntwsApConfApConfigTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 2, 2, 1)
)
ntwsApConfApConfigTableGroup.setObjects(
      *(("NTWS-AP-CONFIG-MIB", "ntwsApConfApConfigApAttachType"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApConfigPhysPortNum"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApConfigApSerialNum"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApConfigApModelName"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApConfigFingerprint"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApConfigBias"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApConfigApTimeout"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApConfigApName"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApConfigContact"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApConfigLocation"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApConfigBlinkEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApConfigForceImageDownloadEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApConfigFirmwareUpgradeEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApConfigLocalSwitchingEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApConfigPowerMode"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApConfigLedMode"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApConfigDescription"))
)
if mibBuilder.loadTexts:
    ntwsApConfApConfigTableGroup.setStatus("current")

ntwsApConfRadioConfigTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 2, 2, 2)
)
ntwsApConfRadioConfigTableGroup.setObjects(
      *(("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioConfigRadioType"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioConfigRadioMode"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioConfigRadioProfileName"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioConfigChannel"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioConfigTxPower"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioConfigAutoTuneMaxTxPower"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioConfigAntennaType"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioConfigAntennaLocation"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioConfigLoadBalancingEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioConfigLoadBalancingGroup"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioConfigLoadRebalancingEnabled"))
)
if mibBuilder.loadTexts:
    ntwsApConfRadioConfigTableGroup.setStatus("current")

ntwsApConfApTemplateConfigTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 2, 2, 3)
)
ntwsApConfApTemplateConfigTableGroup.setObjects(
      *(("NTWS-AP-CONFIG-MIB", "ntwsApConfApTemplConfApTemplateEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApTemplConfBias"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApTemplConfApTimeout"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApTemplConfBlinkEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApTemplConfForceImageDownloadEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApTemplConfFirmwareUpgradeEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApTemplConfLocalSwitchingEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApTemplConfPowerMode"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApTemplConfLedMode"))
)
if mibBuilder.loadTexts:
    ntwsApConfApTemplateConfigTableGroup.setStatus("current")

ntwsApConfApTemplateRadioConfigTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 2, 2, 4)
)
ntwsApConfApTemplateRadioConfigTableGroup.setObjects(
      *(("NTWS-AP-CONFIG-MIB", "ntwsApConfApTemRadioConfRadioMode"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApTemRadioConfRadioProfileName"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApTemRadioConfAutoTuneMaxTxPower"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApTemRadioConfLoadBalancingEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApTemRadioConfLoadBalancingGroup"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfApTemRadioConfLoadRebalancingEnabled"))
)
if mibBuilder.loadTexts:
    ntwsApConfApTemplateRadioConfigTableGroup.setStatus("current")

ntwsApConfRadioProfileTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 2, 2, 5)
)
ntwsApConfRadioProfileTableGroup.setObjects(
      *(("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfBeaconInterval"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfDtimInterval"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfChannelWidth11na"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfMaxTxLifetime"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfMaxRxLifetime"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfRtsThreshold"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfFragThreshold"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfLongXmitPreambleEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfCountermeasuresMode"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfRFScanMode"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfRFScanChannelScope"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfRFScanCTSEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfAutoTune11aChannelRange"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfAutoTuneIgnoreClientsEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfAutoTuneChannelEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfAutoTuneChannelHolddownInterval"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfAutoTuneChannelChangeInterval"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfAutoTunePowerEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfAutoTunePowerRampInterval"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfAutoTunePowerChangeInterval"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfFairQueuingEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfCacBackgroundACMandatory"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfCacBackgroundMaxUtilization"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfCacBackgroundPolicingEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfCacBestEffortACMandatory"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfCacBestEffortMaxUtilization"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfCacBestEffortPolicingEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfCacVideoACMandatory"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfCacVideoMaxUtilization"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfCacVideoPolicingEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfCacVoiceACMandatory"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfCacVoiceMaxUtilization"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfCacVoicePolicingEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfRfidTagEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfWmmPowerSaveEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfRateEnforcementEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfRadioProfDfsChannelsEnabled"))
)
if mibBuilder.loadTexts:
    ntwsApConfRadioProfileTableGroup.setStatus("current")

ntwsApConfRadioProfServiceProfileTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 2, 2, 6)
)
ntwsApConfRadioProfServiceProfileTableGroup.setObjects(
    ("NTWS-AP-CONFIG-MIB", "ntwsApConfRpServpRowStatus")
)
if mibBuilder.loadTexts:
    ntwsApConfRadioProfServiceProfileTableGroup.setStatus("current")

ntwsApConfRadioProfSnoopFilterTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 2, 2, 7)
)
ntwsApConfRadioProfSnoopFilterTableGroup.setObjects(
    ("NTWS-AP-CONFIG-MIB", "ntwsApConfRpSnoopfRowStatus")
)
if mibBuilder.loadTexts:
    ntwsApConfRadioProfSnoopFilterTableGroup.setStatus("current")

ntwsApConfServiceProfileTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 2, 2, 8)
)
ntwsApConfServiceProfileTableGroup.setObjects(
      *(("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfSsidType"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfBeaconEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProf11naMode"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProf11ngMode"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProf11nShortGuardIntervalEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProf11nFrameAggregation"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProf11nMsduMaxLength"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProf11nMpduMaxLength"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfAuthFallthru"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfWebAAAForm"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfSharedKeyAuthEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfWpaIeEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfWpaIeCipherTkipEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfWpaIeCipherCcmpEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfWpaIeCipherWep40Enabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfWpaIeCipherWep104Enabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfWpaIeAuthDot1xEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfWpaIeAuthPskEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfRsnIeEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfRsnIeCipherTkipEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfRsnIeCipherCcmpEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfRsnIeCipherWep40Enabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfRsnIeCipherWep104Enabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfRsnIeAuthDot1xEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfRsnIeAuthPskEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfTkipMicCountermeasuresTime"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfMaxBandwidthKbps"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfCacMode"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfCacSessCount"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfUserIdleTimeout"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfIdleClientProbingEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfShortRetryCount"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfLongRetryCount"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfProxyArpEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfDhcpRestrictEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfNoBroadcastEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfSygateOnDemandEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfEnforceChecksEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfSodaRemediationAcl"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfSodaSuccessPage"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfSodaFailurePage"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfSodaLogoutPage"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfSodaAgentDirectory"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfWebPortalSessionTimeout"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfWebPortalAcl"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfWebPortalLogoutEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfWebPortalLogoutUrl"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfKeepInitialVlanEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfMeshModeEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfBridgingEnabled"),
        ("NTWS-AP-CONFIG-MIB", "ntwsApConfServProfLoadBalanceExemptEnabled"))
)
if mibBuilder.loadTexts:
    ntwsApConfServiceProfileTableGroup.setStatus("current")

ntwsApConfSnoopFilterTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 2, 2, 9)
)
ntwsApConfSnoopFilterTableGroup.setObjects(
    ("NTWS-AP-CONFIG-MIB", "ntwsApConfSnoopFilterEnabled")
)
if mibBuilder.loadTexts:
    ntwsApConfSnoopFilterTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntwsApConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 14, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ntwsApConfigCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTWS-AP-CONFIG-MIB",
    **{"NtwsApTemplateName": NtwsApTemplateName,
       "NtwsRadioProfileName": NtwsRadioProfileName,
       "NtwsServiceProfileName": NtwsServiceProfileName,
       "NtwsSnoopFilterName": NtwsSnoopFilterName,
       "NtwsServiceProfileSsidType": NtwsServiceProfileSsidType,
       "NtwsServiceProfile11nMode": NtwsServiceProfile11nMode,
       "NtwsServiceProfile11nFrameAggregationType": NtwsServiceProfile11nFrameAggregationType,
       "NtwsServiceProfile11nMsduMaxLength": NtwsServiceProfile11nMsduMaxLength,
       "NtwsServiceProfile11nMpduMaxLength": NtwsServiceProfile11nMpduMaxLength,
       "NtwsServiceProfileAuthFallthruType": NtwsServiceProfileAuthFallthruType,
       "NtwsServiceProfileCacMode": NtwsServiceProfileCacMode,
       "NtwsRadioProfileCountermeasuresMode": NtwsRadioProfileCountermeasuresMode,
       "NtwsRadioProfileRFScanChannelScope": NtwsRadioProfileRFScanChannelScope,
       "NtwsRadioProfileAutoTuneChannelRange": NtwsRadioProfileAutoTuneChannelRange,
       "NtwsRadioProfileRFScanMode": NtwsRadioProfileRFScanMode,
       "ntwsApConfigMib": ntwsApConfigMib,
       "ntwsApConfigMibObjects": ntwsApConfigMibObjects,
       "ntwsApConfApConfigTable": ntwsApConfApConfigTable,
       "ntwsApConfApConfigEntry": ntwsApConfApConfigEntry,
       "ntwsApConfApConfigApNum": ntwsApConfApConfigApNum,
       "ntwsApConfApConfigApAttachType": ntwsApConfApConfigApAttachType,
       "ntwsApConfApConfigPhysPortNum": ntwsApConfApConfigPhysPortNum,
       "ntwsApConfApConfigApSerialNum": ntwsApConfApConfigApSerialNum,
       "ntwsApConfApConfigApModelName": ntwsApConfApConfigApModelName,
       "ntwsApConfApConfigFingerprint": ntwsApConfApConfigFingerprint,
       "ntwsApConfApConfigBias": ntwsApConfApConfigBias,
       "ntwsApConfApConfigApTimeout": ntwsApConfApConfigApTimeout,
       "ntwsApConfApConfigApName": ntwsApConfApConfigApName,
       "ntwsApConfApConfigContact": ntwsApConfApConfigContact,
       "ntwsApConfApConfigLocation": ntwsApConfApConfigLocation,
       "ntwsApConfApConfigBlinkEnabled": ntwsApConfApConfigBlinkEnabled,
       "ntwsApConfApConfigForceImageDownloadEnabled": ntwsApConfApConfigForceImageDownloadEnabled,
       "ntwsApConfApConfigFirmwareUpgradeEnabled": ntwsApConfApConfigFirmwareUpgradeEnabled,
       "ntwsApConfApConfigLocalSwitchingEnabled": ntwsApConfApConfigLocalSwitchingEnabled,
       "ntwsApConfApConfigPowerMode": ntwsApConfApConfigPowerMode,
       "ntwsApConfApConfigLedMode": ntwsApConfApConfigLedMode,
       "ntwsApConfApConfigDescription": ntwsApConfApConfigDescription,
       "ntwsApConfRadioConfigTable": ntwsApConfRadioConfigTable,
       "ntwsApConfRadioConfigEntry": ntwsApConfRadioConfigEntry,
       "ntwsApConfRadioConfigApNum": ntwsApConfRadioConfigApNum,
       "ntwsApConfRadioConfigRadioIndex": ntwsApConfRadioConfigRadioIndex,
       "ntwsApConfRadioConfigRadioType": ntwsApConfRadioConfigRadioType,
       "ntwsApConfRadioConfigRadioMode": ntwsApConfRadioConfigRadioMode,
       "ntwsApConfRadioConfigRadioProfileName": ntwsApConfRadioConfigRadioProfileName,
       "ntwsApConfRadioConfigChannel": ntwsApConfRadioConfigChannel,
       "ntwsApConfRadioConfigTxPower": ntwsApConfRadioConfigTxPower,
       "ntwsApConfRadioConfigAutoTuneMaxTxPower": ntwsApConfRadioConfigAutoTuneMaxTxPower,
       "ntwsApConfRadioConfigAntennaType": ntwsApConfRadioConfigAntennaType,
       "ntwsApConfRadioConfigAntennaLocation": ntwsApConfRadioConfigAntennaLocation,
       "ntwsApConfRadioConfigLoadBalancingEnabled": ntwsApConfRadioConfigLoadBalancingEnabled,
       "ntwsApConfRadioConfigLoadBalancingGroup": ntwsApConfRadioConfigLoadBalancingGroup,
       "ntwsApConfRadioConfigLoadRebalancingEnabled": ntwsApConfRadioConfigLoadRebalancingEnabled,
       "ntwsApConfApTemplateConfigTable": ntwsApConfApTemplateConfigTable,
       "ntwsApConfApTemplateConfigEntry": ntwsApConfApTemplateConfigEntry,
       "ntwsApConfApTemplConfApTemplateName": ntwsApConfApTemplConfApTemplateName,
       "ntwsApConfApTemplConfApTemplateEnabled": ntwsApConfApTemplConfApTemplateEnabled,
       "ntwsApConfApTemplConfBias": ntwsApConfApTemplConfBias,
       "ntwsApConfApTemplConfApTimeout": ntwsApConfApTemplConfApTimeout,
       "ntwsApConfApTemplConfBlinkEnabled": ntwsApConfApTemplConfBlinkEnabled,
       "ntwsApConfApTemplConfForceImageDownloadEnabled": ntwsApConfApTemplConfForceImageDownloadEnabled,
       "ntwsApConfApTemplConfFirmwareUpgradeEnabled": ntwsApConfApTemplConfFirmwareUpgradeEnabled,
       "ntwsApConfApTemplConfLocalSwitchingEnabled": ntwsApConfApTemplConfLocalSwitchingEnabled,
       "ntwsApConfApTemplConfPowerMode": ntwsApConfApTemplConfPowerMode,
       "ntwsApConfApTemplConfLedMode": ntwsApConfApTemplConfLedMode,
       "ntwsApConfApTemplateRadioConfigTable": ntwsApConfApTemplateRadioConfigTable,
       "ntwsApConfApTemplateRadioConfigEntry": ntwsApConfApTemplateRadioConfigEntry,
       "ntwsApConfApTemRadioConfApTemplateName": ntwsApConfApTemRadioConfApTemplateName,
       "ntwsApConfApTemRadioConfRadioIndex": ntwsApConfApTemRadioConfRadioIndex,
       "ntwsApConfApTemRadioConfRadioMode": ntwsApConfApTemRadioConfRadioMode,
       "ntwsApConfApTemRadioConfRadioProfileName": ntwsApConfApTemRadioConfRadioProfileName,
       "ntwsApConfApTemRadioConfAutoTuneMaxTxPower": ntwsApConfApTemRadioConfAutoTuneMaxTxPower,
       "ntwsApConfApTemRadioConfLoadBalancingEnabled": ntwsApConfApTemRadioConfLoadBalancingEnabled,
       "ntwsApConfApTemRadioConfLoadBalancingGroup": ntwsApConfApTemRadioConfLoadBalancingGroup,
       "ntwsApConfApTemRadioConfLoadRebalancingEnabled": ntwsApConfApTemRadioConfLoadRebalancingEnabled,
       "ntwsApConfRadioProfileTable": ntwsApConfRadioProfileTable,
       "ntwsApConfRadioProfileEntry": ntwsApConfRadioProfileEntry,
       "ntwsApConfRadioProfRadioProfileName": ntwsApConfRadioProfRadioProfileName,
       "ntwsApConfRadioProfBeaconInterval": ntwsApConfRadioProfBeaconInterval,
       "ntwsApConfRadioProfDtimInterval": ntwsApConfRadioProfDtimInterval,
       "ntwsApConfRadioProfChannelWidth11na": ntwsApConfRadioProfChannelWidth11na,
       "ntwsApConfRadioProfMaxTxLifetime": ntwsApConfRadioProfMaxTxLifetime,
       "ntwsApConfRadioProfMaxRxLifetime": ntwsApConfRadioProfMaxRxLifetime,
       "ntwsApConfRadioProfRtsThreshold": ntwsApConfRadioProfRtsThreshold,
       "ntwsApConfRadioProfFragThreshold": ntwsApConfRadioProfFragThreshold,
       "ntwsApConfRadioProfLongXmitPreambleEnabled": ntwsApConfRadioProfLongXmitPreambleEnabled,
       "ntwsApConfRadioProfCountermeasuresMode": ntwsApConfRadioProfCountermeasuresMode,
       "ntwsApConfRadioProfRFScanMode": ntwsApConfRadioProfRFScanMode,
       "ntwsApConfRadioProfRFScanChannelScope": ntwsApConfRadioProfRFScanChannelScope,
       "ntwsApConfRadioProfRFScanCTSEnabled": ntwsApConfRadioProfRFScanCTSEnabled,
       "ntwsApConfRadioProfAutoTune11aChannelRange": ntwsApConfRadioProfAutoTune11aChannelRange,
       "ntwsApConfRadioProfAutoTuneIgnoreClientsEnabled": ntwsApConfRadioProfAutoTuneIgnoreClientsEnabled,
       "ntwsApConfRadioProfAutoTuneChannelEnabled": ntwsApConfRadioProfAutoTuneChannelEnabled,
       "ntwsApConfRadioProfAutoTuneChannelHolddownInterval": ntwsApConfRadioProfAutoTuneChannelHolddownInterval,
       "ntwsApConfRadioProfAutoTuneChannelChangeInterval": ntwsApConfRadioProfAutoTuneChannelChangeInterval,
       "ntwsApConfRadioProfAutoTunePowerEnabled": ntwsApConfRadioProfAutoTunePowerEnabled,
       "ntwsApConfRadioProfAutoTunePowerRampInterval": ntwsApConfRadioProfAutoTunePowerRampInterval,
       "ntwsApConfRadioProfAutoTunePowerChangeInterval": ntwsApConfRadioProfAutoTunePowerChangeInterval,
       "ntwsApConfRadioProfFairQueuingEnabled": ntwsApConfRadioProfFairQueuingEnabled,
       "ntwsApConfRadioProfCacBackgroundACMandatory": ntwsApConfRadioProfCacBackgroundACMandatory,
       "ntwsApConfRadioProfCacBackgroundMaxUtilization": ntwsApConfRadioProfCacBackgroundMaxUtilization,
       "ntwsApConfRadioProfCacBackgroundPolicingEnabled": ntwsApConfRadioProfCacBackgroundPolicingEnabled,
       "ntwsApConfRadioProfCacBestEffortACMandatory": ntwsApConfRadioProfCacBestEffortACMandatory,
       "ntwsApConfRadioProfCacBestEffortMaxUtilization": ntwsApConfRadioProfCacBestEffortMaxUtilization,
       "ntwsApConfRadioProfCacBestEffortPolicingEnabled": ntwsApConfRadioProfCacBestEffortPolicingEnabled,
       "ntwsApConfRadioProfCacVideoACMandatory": ntwsApConfRadioProfCacVideoACMandatory,
       "ntwsApConfRadioProfCacVideoMaxUtilization": ntwsApConfRadioProfCacVideoMaxUtilization,
       "ntwsApConfRadioProfCacVideoPolicingEnabled": ntwsApConfRadioProfCacVideoPolicingEnabled,
       "ntwsApConfRadioProfCacVoiceACMandatory": ntwsApConfRadioProfCacVoiceACMandatory,
       "ntwsApConfRadioProfCacVoiceMaxUtilization": ntwsApConfRadioProfCacVoiceMaxUtilization,
       "ntwsApConfRadioProfCacVoicePolicingEnabled": ntwsApConfRadioProfCacVoicePolicingEnabled,
       "ntwsApConfRadioProfRfidTagEnabled": ntwsApConfRadioProfRfidTagEnabled,
       "ntwsApConfRadioProfWmmPowerSaveEnabled": ntwsApConfRadioProfWmmPowerSaveEnabled,
       "ntwsApConfRadioProfRateEnforcementEnabled": ntwsApConfRadioProfRateEnforcementEnabled,
       "ntwsApConfRadioProfDfsChannelsEnabled": ntwsApConfRadioProfDfsChannelsEnabled,
       "ntwsApConfRadioProfServiceProfileTable": ntwsApConfRadioProfServiceProfileTable,
       "ntwsApConfRadioProfServiceProfileEntry": ntwsApConfRadioProfServiceProfileEntry,
       "ntwsApConfRpServpRadioProfileName": ntwsApConfRpServpRadioProfileName,
       "ntwsApConfRpServpServiceProfileName": ntwsApConfRpServpServiceProfileName,
       "ntwsApConfRpServpRowStatus": ntwsApConfRpServpRowStatus,
       "ntwsApConfRadioProfSnoopFilterTable": ntwsApConfRadioProfSnoopFilterTable,
       "ntwsApConfRadioProfSnoopFilterEntry": ntwsApConfRadioProfSnoopFilterEntry,
       "ntwsApConfRpSnoopfRadioProfileName": ntwsApConfRpSnoopfRadioProfileName,
       "ntwsApConfRpSnoopfSnoopFilterName": ntwsApConfRpSnoopfSnoopFilterName,
       "ntwsApConfRpSnoopfRowStatus": ntwsApConfRpSnoopfRowStatus,
       "ntwsApConfServiceProfileTable": ntwsApConfServiceProfileTable,
       "ntwsApConfServiceProfileEntry": ntwsApConfServiceProfileEntry,
       "ntwsApConfServProfServiceProfileName": ntwsApConfServProfServiceProfileName,
       "ntwsApConfServProfSsidType": ntwsApConfServProfSsidType,
       "ntwsApConfServProfBeaconEnabled": ntwsApConfServProfBeaconEnabled,
       "ntwsApConfServProf11naMode": ntwsApConfServProf11naMode,
       "ntwsApConfServProf11ngMode": ntwsApConfServProf11ngMode,
       "ntwsApConfServProf11nShortGuardIntervalEnabled": ntwsApConfServProf11nShortGuardIntervalEnabled,
       "ntwsApConfServProf11nFrameAggregation": ntwsApConfServProf11nFrameAggregation,
       "ntwsApConfServProf11nMsduMaxLength": ntwsApConfServProf11nMsduMaxLength,
       "ntwsApConfServProf11nMpduMaxLength": ntwsApConfServProf11nMpduMaxLength,
       "ntwsApConfServProfAuthFallthru": ntwsApConfServProfAuthFallthru,
       "ntwsApConfServProfWebAAAForm": ntwsApConfServProfWebAAAForm,
       "ntwsApConfServProfSharedKeyAuthEnabled": ntwsApConfServProfSharedKeyAuthEnabled,
       "ntwsApConfServProfWpaIeEnabled": ntwsApConfServProfWpaIeEnabled,
       "ntwsApConfServProfWpaIeCipherTkipEnabled": ntwsApConfServProfWpaIeCipherTkipEnabled,
       "ntwsApConfServProfWpaIeCipherCcmpEnabled": ntwsApConfServProfWpaIeCipherCcmpEnabled,
       "ntwsApConfServProfWpaIeCipherWep40Enabled": ntwsApConfServProfWpaIeCipherWep40Enabled,
       "ntwsApConfServProfWpaIeCipherWep104Enabled": ntwsApConfServProfWpaIeCipherWep104Enabled,
       "ntwsApConfServProfWpaIeAuthDot1xEnabled": ntwsApConfServProfWpaIeAuthDot1xEnabled,
       "ntwsApConfServProfWpaIeAuthPskEnabled": ntwsApConfServProfWpaIeAuthPskEnabled,
       "ntwsApConfServProfRsnIeEnabled": ntwsApConfServProfRsnIeEnabled,
       "ntwsApConfServProfRsnIeCipherTkipEnabled": ntwsApConfServProfRsnIeCipherTkipEnabled,
       "ntwsApConfServProfRsnIeCipherCcmpEnabled": ntwsApConfServProfRsnIeCipherCcmpEnabled,
       "ntwsApConfServProfRsnIeCipherWep40Enabled": ntwsApConfServProfRsnIeCipherWep40Enabled,
       "ntwsApConfServProfRsnIeCipherWep104Enabled": ntwsApConfServProfRsnIeCipherWep104Enabled,
       "ntwsApConfServProfRsnIeAuthDot1xEnabled": ntwsApConfServProfRsnIeAuthDot1xEnabled,
       "ntwsApConfServProfRsnIeAuthPskEnabled": ntwsApConfServProfRsnIeAuthPskEnabled,
       "ntwsApConfServProfTkipMicCountermeasuresTime": ntwsApConfServProfTkipMicCountermeasuresTime,
       "ntwsApConfServProfMaxBandwidthKbps": ntwsApConfServProfMaxBandwidthKbps,
       "ntwsApConfServProfCacMode": ntwsApConfServProfCacMode,
       "ntwsApConfServProfCacSessCount": ntwsApConfServProfCacSessCount,
       "ntwsApConfServProfUserIdleTimeout": ntwsApConfServProfUserIdleTimeout,
       "ntwsApConfServProfIdleClientProbingEnabled": ntwsApConfServProfIdleClientProbingEnabled,
       "ntwsApConfServProfShortRetryCount": ntwsApConfServProfShortRetryCount,
       "ntwsApConfServProfLongRetryCount": ntwsApConfServProfLongRetryCount,
       "ntwsApConfServProfProxyArpEnabled": ntwsApConfServProfProxyArpEnabled,
       "ntwsApConfServProfDhcpRestrictEnabled": ntwsApConfServProfDhcpRestrictEnabled,
       "ntwsApConfServProfNoBroadcastEnabled": ntwsApConfServProfNoBroadcastEnabled,
       "ntwsApConfServProfSygateOnDemandEnabled": ntwsApConfServProfSygateOnDemandEnabled,
       "ntwsApConfServProfEnforceChecksEnabled": ntwsApConfServProfEnforceChecksEnabled,
       "ntwsApConfServProfSodaRemediationAcl": ntwsApConfServProfSodaRemediationAcl,
       "ntwsApConfServProfSodaSuccessPage": ntwsApConfServProfSodaSuccessPage,
       "ntwsApConfServProfSodaFailurePage": ntwsApConfServProfSodaFailurePage,
       "ntwsApConfServProfSodaLogoutPage": ntwsApConfServProfSodaLogoutPage,
       "ntwsApConfServProfSodaAgentDirectory": ntwsApConfServProfSodaAgentDirectory,
       "ntwsApConfServProfWebPortalSessionTimeout": ntwsApConfServProfWebPortalSessionTimeout,
       "ntwsApConfServProfWebPortalAcl": ntwsApConfServProfWebPortalAcl,
       "ntwsApConfServProfWebPortalLogoutEnabled": ntwsApConfServProfWebPortalLogoutEnabled,
       "ntwsApConfServProfWebPortalLogoutUrl": ntwsApConfServProfWebPortalLogoutUrl,
       "ntwsApConfServProfKeepInitialVlanEnabled": ntwsApConfServProfKeepInitialVlanEnabled,
       "ntwsApConfServProfMeshModeEnabled": ntwsApConfServProfMeshModeEnabled,
       "ntwsApConfServProfBridgingEnabled": ntwsApConfServProfBridgingEnabled,
       "ntwsApConfServProfLoadBalanceExemptEnabled": ntwsApConfServProfLoadBalanceExemptEnabled,
       "ntwsApConfSnoopFilterTable": ntwsApConfSnoopFilterTable,
       "ntwsApConfSnoopFilterEntry": ntwsApConfSnoopFilterEntry,
       "ntwsApConfSnoopFilterName": ntwsApConfSnoopFilterName,
       "ntwsApConfSnoopFilterEnabled": ntwsApConfSnoopFilterEnabled,
       "ntwsApConfigConformance": ntwsApConfigConformance,
       "ntwsApConfigCompliances": ntwsApConfigCompliances,
       "ntwsApConfigCompliance": ntwsApConfigCompliance,
       "ntwsApConfigGroups": ntwsApConfigGroups,
       "ntwsApConfApConfigTableGroup": ntwsApConfApConfigTableGroup,
       "ntwsApConfRadioConfigTableGroup": ntwsApConfRadioConfigTableGroup,
       "ntwsApConfApTemplateConfigTableGroup": ntwsApConfApTemplateConfigTableGroup,
       "ntwsApConfApTemplateRadioConfigTableGroup": ntwsApConfApTemplateRadioConfigTableGroup,
       "ntwsApConfRadioProfileTableGroup": ntwsApConfRadioProfileTableGroup,
       "ntwsApConfRadioProfServiceProfileTableGroup": ntwsApConfRadioProfServiceProfileTableGroup,
       "ntwsApConfRadioProfSnoopFilterTableGroup": ntwsApConfRadioProfSnoopFilterTableGroup,
       "ntwsApConfServiceProfileTableGroup": ntwsApConfServiceProfileTableGroup,
       "ntwsApConfSnoopFilterTableGroup": ntwsApConfSnoopFilterTableGroup}
)
