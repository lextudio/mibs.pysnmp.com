# SNMP MIB module (WL400-DOT11EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WL400-DOT11EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:01 2024
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

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Bits,
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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wl400Modules,
 wl400Products) = mibBuilder.importSymbols(
    "WL400-GLOBAL-REG",
    "wl400Modules",
    "wl400Products")


# MODULE-IDENTITY

dot11ExtMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 232, 143, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dot11ExtMIB_ObjectIdentity = ObjectIdentity
dot11ExtMIB = _Dot11ExtMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 145, 1)
)
_Dot11ExtConf_ObjectIdentity = ObjectIdentity
dot11ExtConf = _Dot11ExtConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 1)
)
_Dot11ExtGroups_ObjectIdentity = ObjectIdentity
dot11ExtGroups = _Dot11ExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 1, 1)
)
_Dot11ExtCompl_ObjectIdentity = ObjectIdentity
dot11ExtCompl = _Dot11ExtCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 1, 2)
)
_Dot11ExtGenObjs_ObjectIdentity = ObjectIdentity
dot11ExtGenObjs = _Dot11ExtGenObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 2)
)
_Smt_ObjectIdentity = ObjectIdentity
smt = _Smt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 2, 1)
)


class _SmtAssociationID_Type(Integer32):
    """Custom type smtAssociationID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2007),
    )


_SmtAssociationID_Type.__name__ = "Integer32"
_SmtAssociationID_Object = MibScalar
smtAssociationID = _SmtAssociationID_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 2, 1, 1),
    _SmtAssociationID_Type()
)
smtAssociationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtAssociationID.setStatus("current")


class _SmtCapabilityInfo_Type(Bits):
    """Custom type smtCapabilityInfo based on Bits"""
    namedValues = NamedValues(
        *(("cfPollRequest", 1),
          ("cfPollable", 2),
          ("ess", 4),
          ("ibss", 3),
          ("privacy", 0))
    )

_SmtCapabilityInfo_Type.__name__ = "Bits"
_SmtCapabilityInfo_Object = MibScalar
smtCapabilityInfo = _SmtCapabilityInfo_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 2, 1, 2),
    _SmtCapabilityInfo_Type()
)
smtCapabilityInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtCapabilityInfo.setStatus("current")
_SmtPowerSaveInterval_Type = Integer32
_SmtPowerSaveInterval_Object = MibScalar
smtPowerSaveInterval = _SmtPowerSaveInterval_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 2, 1, 3),
    _SmtPowerSaveInterval_Type()
)
smtPowerSaveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtPowerSaveInterval.setStatus("current")
_SmtListenInterval_Type = Integer32
_SmtListenInterval_Object = MibScalar
smtListenInterval = _SmtListenInterval_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 2, 1, 4),
    _SmtListenInterval_Type()
)
smtListenInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtListenInterval.setStatus("current")
_SmtATIMWindow_Type = Integer32
_SmtATIMWindow_Object = MibScalar
smtATIMWindow = _SmtATIMWindow_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 2, 1, 5),
    _SmtATIMWindow_Type()
)
smtATIMWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtATIMWindow.setStatus("current")
_SmtOperationalChannels_Type = OctetString
_SmtOperationalChannels_Object = MibScalar
smtOperationalChannels = _SmtOperationalChannels_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 2, 1, 6),
    _SmtOperationalChannels_Type()
)
smtOperationalChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtOperationalChannels.setStatus("current")
_SmtCurrentBSSID_Type = OctetString
_SmtCurrentBSSID_Object = MibScalar
smtCurrentBSSID = _SmtCurrentBSSID_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 2, 1, 7),
    _SmtCurrentBSSID_Type()
)
smtCurrentBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtCurrentBSSID.setStatus("current")
_SmtCurrentSSID_Type = OctetString
_SmtCurrentSSID_Object = MibScalar
smtCurrentSSID = _SmtCurrentSSID_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 2, 1, 8),
    _SmtCurrentSSID_Type()
)
smtCurrentSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtCurrentSSID.setStatus("current")


class _SmtCurrentBSSType_Type(Integer32):
    """Custom type smtCurrentBSSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adhoc", 2),
          ("infrastructure", 1))
    )


_SmtCurrentBSSType_Type.__name__ = "Integer32"
_SmtCurrentBSSType_Object = MibScalar
smtCurrentBSSType = _SmtCurrentBSSType_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 2, 1, 9),
    _SmtCurrentBSSType_Type()
)
smtCurrentBSSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtCurrentBSSType.setStatus("current")


class _SmtPublicKeyEnable_Type(Integer32):
    """Custom type smtPublicKeyEnable based on Integer32"""
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


_SmtPublicKeyEnable_Type.__name__ = "Integer32"
_SmtPublicKeyEnable_Object = MibScalar
smtPublicKeyEnable = _SmtPublicKeyEnable_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 2, 1, 10),
    _SmtPublicKeyEnable_Type()
)
smtPublicKeyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtPublicKeyEnable.setStatus("current")
_SmtQualityLevel0_Type = Integer32
_SmtQualityLevel0_Object = MibScalar
smtQualityLevel0 = _SmtQualityLevel0_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 2, 1, 11),
    _SmtQualityLevel0_Type()
)
smtQualityLevel0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtQualityLevel0.setStatus("current")
_SmtQualityLevel1_Type = Integer32
_SmtQualityLevel1_Object = MibScalar
smtQualityLevel1 = _SmtQualityLevel1_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 2, 1, 12),
    _SmtQualityLevel1_Type()
)
smtQualityLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtQualityLevel1.setStatus("current")
_SmtQualityLevel2_Type = Integer32
_SmtQualityLevel2_Object = MibScalar
smtQualityLevel2 = _SmtQualityLevel2_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 2, 1, 13),
    _SmtQualityLevel2_Type()
)
smtQualityLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtQualityLevel2.setStatus("current")
_SmtQualityPenalty_Type = Integer32
_SmtQualityPenalty_Object = MibScalar
smtQualityPenalty = _SmtQualityPenalty_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 2, 1, 14),
    _SmtQualityPenalty_Type()
)
smtQualityPenalty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtQualityPenalty.setStatus("current")
_SmtStationDBTimeout_Type = Integer32
_SmtStationDBTimeout_Object = MibScalar
smtStationDBTimeout = _SmtStationDBTimeout_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 2, 1, 15),
    _SmtStationDBTimeout_Type()
)
smtStationDBTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtStationDBTimeout.setStatus("current")


class _SmtQualityIndicator_Type(Integer32):
    """Custom type smtQualityIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SmtQualityIndicator_Type.__name__ = "Integer32"
_SmtQualityIndicator_Object = MibScalar
smtQualityIndicator = _SmtQualityIndicator_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 2, 1, 16),
    _SmtQualityIndicator_Type()
)
smtQualityIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtQualityIndicator.setStatus("current")
_SmtQualityUpperLimit_Type = Integer32
_SmtQualityUpperLimit_Object = MibScalar
smtQualityUpperLimit = _SmtQualityUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 2, 1, 17),
    _SmtQualityUpperLimit_Type()
)
smtQualityUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtQualityUpperLimit.setStatus("current")
_SmtQualityLowerLimit_Type = Integer32
_SmtQualityLowerLimit_Object = MibScalar
smtQualityLowerLimit = _SmtQualityLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 2, 1, 18),
    _SmtQualityLowerLimit_Type()
)
smtQualityLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtQualityLowerLimit.setStatus("current")
_SmtOEMCapabilityInformation_Type = Integer32
_SmtOEMCapabilityInformation_Object = MibScalar
smtOEMCapabilityInformation = _SmtOEMCapabilityInformation_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 2, 1, 19),
    _SmtOEMCapabilityInformation_Type()
)
smtOEMCapabilityInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtOEMCapabilityInformation.setStatus("current")
_SmtCWMin_Type = Integer32
_SmtCWMin_Object = MibScalar
smtCWMin = _SmtCWMin_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 2, 1, 20),
    _SmtCWMin_Type()
)
smtCWMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtCWMin.setStatus("current")
_SmtCWMax_Type = Integer32
_SmtCWMax_Object = MibScalar
smtCWMax = _SmtCWMax_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 2, 1, 21),
    _SmtCWMax_Type()
)
smtCWMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtCWMax.setStatus("current")
_SmtACKWindow_Type = Integer32
_SmtACKWindow_Object = MibScalar
smtACKWindow = _SmtACKWindow_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 2, 1, 22),
    _SmtACKWindow_Type()
)
smtACKWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtACKWindow.setStatus("current")
_Dot11ExtAPObjs_ObjectIdentity = ObjectIdentity
dot11ExtAPObjs = _Dot11ExtAPObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 3)
)
_Assoc_ObjectIdentity = ObjectIdentity
assoc = _Assoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 3, 1)
)
_AssocTableMaxLength_Type = Integer32
_AssocTableMaxLength_Object = MibScalar
assocTableMaxLength = _AssocTableMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 3, 1, 1),
    _AssocTableMaxLength_Type()
)
assocTableMaxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocTableMaxLength.setStatus("current")
_AssocTable_Object = MibTable
assocTable = _AssocTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    assocTable.setStatus("current")
_AssocEntry_Object = MibTableRow
assocEntry = _AssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 3, 1, 2, 1)
)
assocEntry.setIndexNames(
    (0, "WL400-DOT11EXT-MIB", "assocIndex"),
)
if mibBuilder.loadTexts:
    assocEntry.setStatus("current")


class _AssocIndex_Type(Integer32):
    """Custom type assocIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2007),
    )


_AssocIndex_Type.__name__ = "Integer32"
_AssocIndex_Object = MibTableColumn
assocIndex = _AssocIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 3, 1, 2, 1, 1),
    _AssocIndex_Type()
)
assocIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    assocIndex.setStatus("current")
_AssocAddress_Type = MacAddress
_AssocAddress_Object = MibTableColumn
assocAddress = _AssocAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 3, 1, 2, 1, 2),
    _AssocAddress_Type()
)
assocAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocAddress.setStatus("current")
_AssocQuality_Type = Integer32
_AssocQuality_Object = MibTableColumn
assocQuality = _AssocQuality_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 3, 1, 2, 1, 3),
    _AssocQuality_Type()
)
assocQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocQuality.setStatus("current")
_AssocAge_Type = Integer32
_AssocAge_Object = MibTableColumn
assocAge = _AssocAge_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 3, 1, 2, 1, 4),
    _AssocAge_Type()
)
assocAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocAge.setStatus("current")
_AssocRSSI_Type = Integer32
_AssocRSSI_Object = MibTableColumn
assocRSSI = _AssocRSSI_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 3, 1, 2, 1, 5),
    _AssocRSSI_Type()
)
assocRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocRSSI.setStatus("current")
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 3, 2)
)
_SecMACAclMaxTableLength_Type = Integer32
_SecMACAclMaxTableLength_Object = MibScalar
secMACAclMaxTableLength = _SecMACAclMaxTableLength_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 3, 2, 1),
    _SecMACAclMaxTableLength_Type()
)
secMACAclMaxTableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secMACAclMaxTableLength.setStatus("current")
_SecMACAclTable_Object = MibTable
secMACAclTable = _SecMACAclTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    secMACAclTable.setStatus("current")
_SecMACAclEntry_Object = MibTableRow
secMACAclEntry = _SecMACAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 3, 2, 2, 1)
)
secMACAclEntry.setIndexNames(
    (0, "WL400-DOT11EXT-MIB", "secMACAclIndex"),
)
if mibBuilder.loadTexts:
    secMACAclEntry.setStatus("current")


class _SecMACAclIndex_Type(Integer32):
    """Custom type secMACAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2007),
    )


_SecMACAclIndex_Type.__name__ = "Integer32"
_SecMACAclIndex_Object = MibTableColumn
secMACAclIndex = _SecMACAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 3, 2, 2, 1, 1),
    _SecMACAclIndex_Type()
)
secMACAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    secMACAclIndex.setStatus("current")
_SecMACAclAddress_Type = MacAddress
_SecMACAclAddress_Object = MibTableColumn
secMACAclAddress = _SecMACAclAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 3, 2, 2, 1, 2),
    _SecMACAclAddress_Type()
)
secMACAclAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secMACAclAddress.setStatus("current")
_SecMACAclAllowed_Type = TruthValue
_SecMACAclAllowed_Object = MibTableColumn
secMACAclAllowed = _SecMACAclAllowed_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 3, 2, 2, 1, 3),
    _SecMACAclAllowed_Type()
)
secMACAclAllowed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secMACAclAllowed.setStatus("current")
_SecMACAclRowStatus_Type = RowStatus
_SecMACAclRowStatus_Object = MibTableColumn
secMACAclRowStatus = _SecMACAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 3, 2, 2, 1, 4),
    _SecMACAclRowStatus_Type()
)
secMACAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secMACAclRowStatus.setStatus("current")


class _SecLastError_Type(OctetString):
    """Custom type secLastError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SecLastError_Type.__name__ = "OctetString"
_SecLastError_Object = MibScalar
secLastError = _SecLastError_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 3, 2, 3),
    _SecLastError_Type()
)
secLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secLastError.setStatus("current")
_SecLastErrorAddress_Type = MacAddress
_SecLastErrorAddress_Object = MibScalar
secLastErrorAddress = _SecLastErrorAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 3, 2, 4),
    _SecLastErrorAddress_Type()
)
secLastErrorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secLastErrorAddress.setStatus("current")
_Dot11ExtEvents_ObjectIdentity = ObjectIdentity
dot11ExtEvents = _Dot11ExtEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 4)
)
_Dot11ExtEventsV2_ObjectIdentity = ObjectIdentity
dot11ExtEventsV2 = _Dot11ExtEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 4, 0)
)
_Dot11ExtWBUObjs_ObjectIdentity = ObjectIdentity
dot11ExtWBUObjs = _Dot11ExtWBUObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5)
)
_Roam_ObjectIdentity = ObjectIdentity
roam = _Roam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1)
)


class _RoamScanType_Type(Integer32):
    """Custom type roamScanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 0))
    )


_RoamScanType_Type.__name__ = "Integer32"
_RoamScanType_Object = MibScalar
roamScanType = _RoamScanType_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 1),
    _RoamScanType_Type()
)
roamScanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamScanType.setStatus("current")
_RoamScanInterval_Type = Integer32
_RoamScanInterval_Object = MibScalar
roamScanInterval = _RoamScanInterval_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 2),
    _RoamScanInterval_Type()
)
roamScanInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamScanInterval.setStatus("current")
_RoamProbeDelay_Type = Integer32
_RoamProbeDelay_Object = MibScalar
roamProbeDelay = _RoamProbeDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 3),
    _RoamProbeDelay_Type()
)
roamProbeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamProbeDelay.setStatus("current")
_RoamMinChannelTime_Type = Integer32
_RoamMinChannelTime_Object = MibScalar
roamMinChannelTime = _RoamMinChannelTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 4),
    _RoamMinChannelTime_Type()
)
roamMinChannelTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamMinChannelTime.setStatus("current")
_RoamMaxChannelTime_Type = Integer32
_RoamMaxChannelTime_Object = MibScalar
roamMaxChannelTime = _RoamMaxChannelTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 5),
    _RoamMaxChannelTime_Type()
)
roamMaxChannelTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamMaxChannelTime.setStatus("current")
_RoamJoinTimeout_Type = Integer32
_RoamJoinTimeout_Object = MibScalar
roamJoinTimeout = _RoamJoinTimeout_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 6),
    _RoamJoinTimeout_Type()
)
roamJoinTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamJoinTimeout.setStatus("current")
_RoamBeaconPeriodTimeout_Type = Integer32
_RoamBeaconPeriodTimeout_Object = MibScalar
roamBeaconPeriodTimeout = _RoamBeaconPeriodTimeout_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 7),
    _RoamBeaconPeriodTimeout_Type()
)
roamBeaconPeriodTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamBeaconPeriodTimeout.setStatus("current")
_RoamDontSwitch_Type = Integer32
_RoamDontSwitch_Object = MibScalar
roamDontSwitch = _RoamDontSwitch_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 8),
    _RoamDontSwitch_Type()
)
roamDontSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamDontSwitch.setStatus("current")
_RoamBlackout_Type = Integer32
_RoamBlackout_Object = MibScalar
roamBlackout = _RoamBlackout_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 9),
    _RoamBlackout_Type()
)
roamBlackout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamBlackout.setStatus("current")
_RoamDisassociateTime_Type = Integer32
_RoamDisassociateTime_Object = MibScalar
roamDisassociateTime = _RoamDisassociateTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 10),
    _RoamDisassociateTime_Type()
)
roamDisassociateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamDisassociateTime.setStatus("current")
_RoamHandoffTime_Type = Integer32
_RoamHandoffTime_Object = MibScalar
roamHandoffTime = _RoamHandoffTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 11),
    _RoamHandoffTime_Type()
)
roamHandoffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamHandoffTime.setStatus("current")
_RoamWeightMetric1_Type = Integer32
_RoamWeightMetric1_Object = MibScalar
roamWeightMetric1 = _RoamWeightMetric1_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 12),
    _RoamWeightMetric1_Type()
)
roamWeightMetric1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamWeightMetric1.setStatus("current")
_RoamWeightMetric2_Type = Integer32
_RoamWeightMetric2_Object = MibScalar
roamWeightMetric2 = _RoamWeightMetric2_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 13),
    _RoamWeightMetric2_Type()
)
roamWeightMetric2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamWeightMetric2.setStatus("current")
_RoamWeightMetric3_Type = Integer32
_RoamWeightMetric3_Object = MibScalar
roamWeightMetric3 = _RoamWeightMetric3_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 14),
    _RoamWeightMetric3_Type()
)
roamWeightMetric3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamWeightMetric3.setStatus("current")
_RoamWeightMetric4_Type = Integer32
_RoamWeightMetric4_Object = MibScalar
roamWeightMetric4 = _RoamWeightMetric4_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 15),
    _RoamWeightMetric4_Type()
)
roamWeightMetric4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamWeightMetric4.setStatus("current")
_RoamWeightMetric5_Type = Integer32
_RoamWeightMetric5_Object = MibScalar
roamWeightMetric5 = _RoamWeightMetric5_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 16),
    _RoamWeightMetric5_Type()
)
roamWeightMetric5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamWeightMetric5.setStatus("current")
_RoamWeightMetric6_Type = Integer32
_RoamWeightMetric6_Object = MibScalar
roamWeightMetric6 = _RoamWeightMetric6_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 17),
    _RoamWeightMetric6_Type()
)
roamWeightMetric6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamWeightMetric6.setStatus("current")
_RoamWeightMetric7_Type = Integer32
_RoamWeightMetric7_Object = MibScalar
roamWeightMetric7 = _RoamWeightMetric7_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 18),
    _RoamWeightMetric7_Type()
)
roamWeightMetric7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamWeightMetric7.setStatus("current")
_RoamWeightMetric8_Type = Integer32
_RoamWeightMetric8_Object = MibScalar
roamWeightMetric8 = _RoamWeightMetric8_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 19),
    _RoamWeightMetric8_Type()
)
roamWeightMetric8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamWeightMetric8.setStatus("current")
_RoamMisc1_Type = Integer32
_RoamMisc1_Object = MibScalar
roamMisc1 = _RoamMisc1_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 20),
    _RoamMisc1_Type()
)
roamMisc1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamMisc1.setStatus("current")
_RoamMisc2_Type = Integer32
_RoamMisc2_Object = MibScalar
roamMisc2 = _RoamMisc2_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 21),
    _RoamMisc2_Type()
)
roamMisc2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roamMisc2.setStatus("current")
_RoamTableLength_Type = Integer32
_RoamTableLength_Object = MibScalar
roamTableLength = _RoamTableLength_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 22),
    _RoamTableLength_Type()
)
roamTableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roamTableLength.setStatus("current")
_RoamTable_Object = MibTable
roamTable = _RoamTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 23)
)
if mibBuilder.loadTexts:
    roamTable.setStatus("current")
_RoamEntry_Object = MibTableRow
roamEntry = _RoamEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 23, 1)
)
roamEntry.setIndexNames(
    (0, "WL400-DOT11EXT-MIB", "roamIndex"),
)
if mibBuilder.loadTexts:
    roamEntry.setStatus("current")
_RoamIndex_Type = Integer32
_RoamIndex_Object = MibTableColumn
roamIndex = _RoamIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 23, 1, 1),
    _RoamIndex_Type()
)
roamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    roamIndex.setStatus("current")
_RoamBSSID_Type = MacAddress
_RoamBSSID_Object = MibTableColumn
roamBSSID = _RoamBSSID_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 23, 1, 2),
    _RoamBSSID_Type()
)
roamBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roamBSSID.setStatus("current")
_RoamSSID_Type = OctetString
_RoamSSID_Object = MibTableColumn
roamSSID = _RoamSSID_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 23, 1, 3),
    _RoamSSID_Type()
)
roamSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roamSSID.setStatus("current")


class _RoamBSSType_Type(Integer32):
    """Custom type roamBSSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("independent", 2),
          ("infrastructure", 1))
    )


_RoamBSSType_Type.__name__ = "Integer32"
_RoamBSSType_Object = MibTableColumn
roamBSSType = _RoamBSSType_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 23, 1, 4),
    _RoamBSSType_Type()
)
roamBSSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roamBSSType.setStatus("current")
_RoamChannel_Type = Integer32
_RoamChannel_Object = MibTableColumn
roamChannel = _RoamChannel_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 23, 1, 5),
    _RoamChannel_Type()
)
roamChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roamChannel.setStatus("current")
_RoamAge_Type = Integer32
_RoamAge_Object = MibTableColumn
roamAge = _RoamAge_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 23, 1, 6),
    _RoamAge_Type()
)
roamAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roamAge.setStatus("current")
_RoamQuality_Type = Integer32
_RoamQuality_Object = MibTableColumn
roamQuality = _RoamQuality_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 23, 1, 7),
    _RoamQuality_Type()
)
roamQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roamQuality.setStatus("current")
_RoamLoad_Type = Integer32
_RoamLoad_Object = MibTableColumn
roamLoad = _RoamLoad_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 23, 1, 8),
    _RoamLoad_Type()
)
roamLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roamLoad.setStatus("current")
_RoamBeaconPeriod_Type = Integer32
_RoamBeaconPeriod_Object = MibTableColumn
roamBeaconPeriod = _RoamBeaconPeriod_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 23, 1, 9),
    _RoamBeaconPeriod_Type()
)
roamBeaconPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roamBeaconPeriod.setStatus("current")
_RoamDTIMPeriod_Type = Integer32
_RoamDTIMPeriod_Object = MibTableColumn
roamDTIMPeriod = _RoamDTIMPeriod_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 23, 1, 10),
    _RoamDTIMPeriod_Type()
)
roamDTIMPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roamDTIMPeriod.setStatus("current")


class _RoamCapabilityInfo_Type(Bits):
    """Custom type roamCapabilityInfo based on Bits"""
    namedValues = NamedValues(
        *(("cfPollRequest", 1),
          ("cfPollable", 2),
          ("ess", 4),
          ("ibss", 3),
          ("privacy", 0))
    )

_RoamCapabilityInfo_Type.__name__ = "Bits"
_RoamCapabilityInfo_Object = MibTableColumn
roamCapabilityInfo = _RoamCapabilityInfo_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 23, 1, 11),
    _RoamCapabilityInfo_Type()
)
roamCapabilityInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roamCapabilityInfo.setStatus("current")
_RoamRates_Type = OctetString
_RoamRates_Object = MibTableColumn
roamRates = _RoamRates_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 23, 1, 12),
    _RoamRates_Type()
)
roamRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roamRates.setStatus("current")
_RoamRSSI_Type = Integer32
_RoamRSSI_Object = MibTableColumn
roamRSSI = _RoamRSSI_Object(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 5, 1, 23, 1, 13),
    _RoamRSSI_Type()
)
roamRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roamRSSI.setStatus("current")

# Managed Objects groups

smtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 1, 1, 1)
)
smtGroup.setObjects(
      *(("WL400-DOT11EXT-MIB", "smtAssociationID"),
        ("WL400-DOT11EXT-MIB", "smtCapabilityInfo"),
        ("WL400-DOT11EXT-MIB", "smtPowerSaveInterval"),
        ("WL400-DOT11EXT-MIB", "smtListenInterval"),
        ("WL400-DOT11EXT-MIB", "smtATIMWindow"),
        ("WL400-DOT11EXT-MIB", "smtOperationalChannels"),
        ("WL400-DOT11EXT-MIB", "smtCurrentBSSID"),
        ("WL400-DOT11EXT-MIB", "smtCurrentSSID"),
        ("WL400-DOT11EXT-MIB", "smtCurrentBSSType"),
        ("WL400-DOT11EXT-MIB", "smtPublicKeyEnable"),
        ("WL400-DOT11EXT-MIB", "smtQualityLevel0"),
        ("WL400-DOT11EXT-MIB", "smtQualityLevel1"),
        ("WL400-DOT11EXT-MIB", "smtQualityLevel2"),
        ("WL400-DOT11EXT-MIB", "smtQualityPenalty"),
        ("WL400-DOT11EXT-MIB", "smtStationDBTimeout"),
        ("WL400-DOT11EXT-MIB", "smtQualityIndicator"),
        ("WL400-DOT11EXT-MIB", "smtQualityUpperLimit"),
        ("WL400-DOT11EXT-MIB", "smtQualityLowerLimit"),
        ("WL400-DOT11EXT-MIB", "smtOEMCapabilityInformation"),
        ("WL400-DOT11EXT-MIB", "smtCWMin"),
        ("WL400-DOT11EXT-MIB", "smtCWMax"),
        ("WL400-DOT11EXT-MIB", "smtACKWindow"))
)
if mibBuilder.loadTexts:
    smtGroup.setStatus("current")

assocGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 1, 1, 2)
)
assocGroup.setObjects(
      *(("WL400-DOT11EXT-MIB", "assocTableMaxLength"),
        ("WL400-DOT11EXT-MIB", "assocAddress"),
        ("WL400-DOT11EXT-MIB", "assocQuality"),
        ("WL400-DOT11EXT-MIB", "assocAge"),
        ("WL400-DOT11EXT-MIB", "assocRSSI"))
)
if mibBuilder.loadTexts:
    assocGroup.setStatus("current")

securityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 1, 1, 3)
)
securityGroup.setObjects(
      *(("WL400-DOT11EXT-MIB", "secMACAclMaxTableLength"),
        ("WL400-DOT11EXT-MIB", "secMACAclAddress"),
        ("WL400-DOT11EXT-MIB", "secMACAclAllowed"),
        ("WL400-DOT11EXT-MIB", "secMACAclRowStatus"),
        ("WL400-DOT11EXT-MIB", "secLastError"),
        ("WL400-DOT11EXT-MIB", "secLastErrorAddress"))
)
if mibBuilder.loadTexts:
    securityGroup.setStatus("current")

roamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 1, 1, 5)
)
roamGroup.setObjects(
      *(("WL400-DOT11EXT-MIB", "roamScanType"),
        ("WL400-DOT11EXT-MIB", "roamScanInterval"),
        ("WL400-DOT11EXT-MIB", "roamBeaconPeriodTimeout"),
        ("WL400-DOT11EXT-MIB", "roamBlackout"),
        ("WL400-DOT11EXT-MIB", "roamDisassociateTime"),
        ("WL400-DOT11EXT-MIB", "roamHandoffTime"),
        ("WL400-DOT11EXT-MIB", "roamWeightMetric1"),
        ("WL400-DOT11EXT-MIB", "roamWeightMetric2"),
        ("WL400-DOT11EXT-MIB", "roamWeightMetric3"),
        ("WL400-DOT11EXT-MIB", "roamWeightMetric4"),
        ("WL400-DOT11EXT-MIB", "roamWeightMetric5"),
        ("WL400-DOT11EXT-MIB", "roamWeightMetric6"),
        ("WL400-DOT11EXT-MIB", "roamWeightMetric7"),
        ("WL400-DOT11EXT-MIB", "roamWeightMetric8"),
        ("WL400-DOT11EXT-MIB", "roamMisc1"),
        ("WL400-DOT11EXT-MIB", "roamMisc2"),
        ("WL400-DOT11EXT-MIB", "roamProbeDelay"),
        ("WL400-DOT11EXT-MIB", "roamDontSwitch"),
        ("WL400-DOT11EXT-MIB", "roamMinChannelTime"),
        ("WL400-DOT11EXT-MIB", "roamMaxChannelTime"),
        ("WL400-DOT11EXT-MIB", "roamJoinTimeout"),
        ("WL400-DOT11EXT-MIB", "roamTableLength"),
        ("WL400-DOT11EXT-MIB", "roamSSID"),
        ("WL400-DOT11EXT-MIB", "roamBSSID"),
        ("WL400-DOT11EXT-MIB", "roamBSSType"),
        ("WL400-DOT11EXT-MIB", "roamChannel"),
        ("WL400-DOT11EXT-MIB", "roamAge"),
        ("WL400-DOT11EXT-MIB", "roamQuality"),
        ("WL400-DOT11EXT-MIB", "roamLoad"),
        ("WL400-DOT11EXT-MIB", "roamBeaconPeriod"),
        ("WL400-DOT11EXT-MIB", "roamDTIMPeriod"),
        ("WL400-DOT11EXT-MIB", "roamCapabilityInfo"),
        ("WL400-DOT11EXT-MIB", "roamRates"),
        ("WL400-DOT11EXT-MIB", "roamRSSI"))
)
if mibBuilder.loadTexts:
    roamGroup.setStatus("current")


# Notification objects

securityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 4, 0, 1)
)
securityViolation.setObjects(
      *(("WL400-DOT11EXT-MIB", "secLastError"),
        ("WL400-DOT11EXT-MIB", "secLastErrorAddress"))
)
if mibBuilder.loadTexts:
    securityViolation.setStatus(
        "current"
    )


# Notifications groups

secNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 1, 1, 4)
)
secNotificationGroup.setObjects(
    ("WL400-DOT11EXT-MIB", "securityViolation")
)
if mibBuilder.loadTexts:
    secNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dot11ExtBasicCompl = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dot11ExtBasicCompl.setStatus(
        "current"
    )

dot11ExtAPCompl = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dot11ExtAPCompl.setStatus(
        "current"
    )

dot11ExtWBUCompl = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 232, 145, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dot11ExtWBUCompl.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WL400-DOT11EXT-MIB",
    **{"dot11ExtMibModule": dot11ExtMibModule,
       "dot11ExtMIB": dot11ExtMIB,
       "dot11ExtConf": dot11ExtConf,
       "dot11ExtGroups": dot11ExtGroups,
       "smtGroup": smtGroup,
       "assocGroup": assocGroup,
       "securityGroup": securityGroup,
       "secNotificationGroup": secNotificationGroup,
       "roamGroup": roamGroup,
       "dot11ExtCompl": dot11ExtCompl,
       "dot11ExtBasicCompl": dot11ExtBasicCompl,
       "dot11ExtAPCompl": dot11ExtAPCompl,
       "dot11ExtWBUCompl": dot11ExtWBUCompl,
       "dot11ExtGenObjs": dot11ExtGenObjs,
       "smt": smt,
       "smtAssociationID": smtAssociationID,
       "smtCapabilityInfo": smtCapabilityInfo,
       "smtPowerSaveInterval": smtPowerSaveInterval,
       "smtListenInterval": smtListenInterval,
       "smtATIMWindow": smtATIMWindow,
       "smtOperationalChannels": smtOperationalChannels,
       "smtCurrentBSSID": smtCurrentBSSID,
       "smtCurrentSSID": smtCurrentSSID,
       "smtCurrentBSSType": smtCurrentBSSType,
       "smtPublicKeyEnable": smtPublicKeyEnable,
       "smtQualityLevel0": smtQualityLevel0,
       "smtQualityLevel1": smtQualityLevel1,
       "smtQualityLevel2": smtQualityLevel2,
       "smtQualityPenalty": smtQualityPenalty,
       "smtStationDBTimeout": smtStationDBTimeout,
       "smtQualityIndicator": smtQualityIndicator,
       "smtQualityUpperLimit": smtQualityUpperLimit,
       "smtQualityLowerLimit": smtQualityLowerLimit,
       "smtOEMCapabilityInformation": smtOEMCapabilityInformation,
       "smtCWMin": smtCWMin,
       "smtCWMax": smtCWMax,
       "smtACKWindow": smtACKWindow,
       "dot11ExtAPObjs": dot11ExtAPObjs,
       "assoc": assoc,
       "assocTableMaxLength": assocTableMaxLength,
       "assocTable": assocTable,
       "assocEntry": assocEntry,
       "assocIndex": assocIndex,
       "assocAddress": assocAddress,
       "assocQuality": assocQuality,
       "assocAge": assocAge,
       "assocRSSI": assocRSSI,
       "security": security,
       "secMACAclMaxTableLength": secMACAclMaxTableLength,
       "secMACAclTable": secMACAclTable,
       "secMACAclEntry": secMACAclEntry,
       "secMACAclIndex": secMACAclIndex,
       "secMACAclAddress": secMACAclAddress,
       "secMACAclAllowed": secMACAclAllowed,
       "secMACAclRowStatus": secMACAclRowStatus,
       "secLastError": secLastError,
       "secLastErrorAddress": secLastErrorAddress,
       "dot11ExtEvents": dot11ExtEvents,
       "dot11ExtEventsV2": dot11ExtEventsV2,
       "securityViolation": securityViolation,
       "dot11ExtWBUObjs": dot11ExtWBUObjs,
       "roam": roam,
       "roamScanType": roamScanType,
       "roamScanInterval": roamScanInterval,
       "roamProbeDelay": roamProbeDelay,
       "roamMinChannelTime": roamMinChannelTime,
       "roamMaxChannelTime": roamMaxChannelTime,
       "roamJoinTimeout": roamJoinTimeout,
       "roamBeaconPeriodTimeout": roamBeaconPeriodTimeout,
       "roamDontSwitch": roamDontSwitch,
       "roamBlackout": roamBlackout,
       "roamDisassociateTime": roamDisassociateTime,
       "roamHandoffTime": roamHandoffTime,
       "roamWeightMetric1": roamWeightMetric1,
       "roamWeightMetric2": roamWeightMetric2,
       "roamWeightMetric3": roamWeightMetric3,
       "roamWeightMetric4": roamWeightMetric4,
       "roamWeightMetric5": roamWeightMetric5,
       "roamWeightMetric6": roamWeightMetric6,
       "roamWeightMetric7": roamWeightMetric7,
       "roamWeightMetric8": roamWeightMetric8,
       "roamMisc1": roamMisc1,
       "roamMisc2": roamMisc2,
       "roamTableLength": roamTableLength,
       "roamTable": roamTable,
       "roamEntry": roamEntry,
       "roamIndex": roamIndex,
       "roamBSSID": roamBSSID,
       "roamSSID": roamSSID,
       "roamBSSType": roamBSSType,
       "roamChannel": roamChannel,
       "roamAge": roamAge,
       "roamQuality": roamQuality,
       "roamLoad": roamLoad,
       "roamBeaconPeriod": roamBeaconPeriod,
       "roamDTIMPeriod": roamDTIMPeriod,
       "roamCapabilityInfo": roamCapabilityInfo,
       "roamRates": roamRates,
       "roamRSSI": roamRSSI}
)
