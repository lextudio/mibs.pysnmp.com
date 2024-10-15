# SNMP MIB module (ZhoneAPON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZhoneAPON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:23:18 2024
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

(ifAlias,
 ifCompliance,
 ifCompliance2,
 ifConnectorPresent,
 ifCounterDiscontinuityGroup,
 ifCounterDiscontinuityTime,
 ifFixedLengthGroup,
 ifGeneralGroup,
 ifGeneralInformationGroup,
 ifHCFixedLengthGroup,
 ifHCInBroadcastPkts,
 ifHCInMulticastPkts,
 ifHCInOctets,
 ifHCInUcastPkts,
 ifHCOutBroadcastPkts,
 ifHCOutMulticastPkts,
 ifHCOutOctets,
 ifHCOutUcastPkts,
 ifHCPacketGroup,
 ifHighSpeed,
 ifInBroadcastPkts,
 ifInMulticastPkts,
 ifIndex,
 ifLinkUpDownTrapEnable,
 ifName,
 ifNumber,
 ifOldObjectsGroup,
 ifOutBroadcastPkts,
 ifOutMulticastPkts,
 ifPacketGroup,
 ifPromiscuousMode,
 ifRcvAddressAddress,
 ifRcvAddressGroup,
 ifRcvAddressStatus,
 ifRcvAddressType,
 ifStackGroup,
 ifStackGroup2,
 ifStackHigherLayer,
 ifStackLastChange,
 ifStackLowerLayer,
 ifStackStatus,
 ifTableLastChange,
 ifTestCode,
 ifTestGroup,
 ifTestId,
 ifTestOwner,
 ifTestResult,
 ifTestStatus,
 ifTestType,
 ifVHCPacketGroup) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAlias",
    "ifCompliance",
    "ifCompliance2",
    "ifConnectorPresent",
    "ifCounterDiscontinuityGroup",
    "ifCounterDiscontinuityTime",
    "ifFixedLengthGroup",
    "ifGeneralGroup",
    "ifGeneralInformationGroup",
    "ifHCFixedLengthGroup",
    "ifHCInBroadcastPkts",
    "ifHCInMulticastPkts",
    "ifHCInOctets",
    "ifHCInUcastPkts",
    "ifHCOutBroadcastPkts",
    "ifHCOutMulticastPkts",
    "ifHCOutOctets",
    "ifHCOutUcastPkts",
    "ifHCPacketGroup",
    "ifHighSpeed",
    "ifInBroadcastPkts",
    "ifInMulticastPkts",
    "ifIndex",
    "ifLinkUpDownTrapEnable",
    "ifName",
    "ifNumber",
    "ifOldObjectsGroup",
    "ifOutBroadcastPkts",
    "ifOutMulticastPkts",
    "ifPacketGroup",
    "ifPromiscuousMode",
    "ifRcvAddressAddress",
    "ifRcvAddressGroup",
    "ifRcvAddressStatus",
    "ifRcvAddressType",
    "ifStackGroup",
    "ifStackGroup2",
    "ifStackHigherLayer",
    "ifStackLastChange",
    "ifStackLowerLayer",
    "ifStackStatus",
    "ifTableLastChange",
    "ifTestCode",
    "ifTestGroup",
    "ifTestId",
    "ifTestOwner",
    "ifTestResult",
    "ifTestStatus",
    "ifTestType",
    "ifVHCPacketGroup")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(apsMIB,
 sechtor100,
 sechtor300,
 sipCommonMIB,
 sipTC,
 sipUAMIB,
 zhoneAtm,
 zhoneBridge,
 zhoneCard,
 zhoneConsole,
 zhoneDrafts,
 zhoneDs3Ext,
 zhoneDsl,
 zhoneDsx,
 zhoneEnet,
 zhoneGenWtn,
 zhoneGroups,
 zhoneIma,
 zhoneInterfaceGroup,
 zhoneInterfaceTranslation,
 zhoneIp,
 zhoneLineTypes,
 zhoneMalc,
 zhoneMasterAgent,
 zhoneModules,
 zhoneOcx,
 zhonePhysical,
 zhonePls,
 zhonePpp,
 zhoneRadio,
 zhoneRegCpe,
 zhoneRegMalc,
 zhoneRegMux,
 zhoneRegPls,
 zhoneRegSechtor,
 zhoneRegWtn,
 zhoneShelf,
 zhoneShelfIndex,
 zhoneShelfSlotCompliance,
 zhoneShelfSlotGroup,
 zhoneSlotIndex,
 zhoneSonet,
 zhoneSubscriber,
 zhoneSystem,
 zhoneTrapModules,
 zhoneVoice,
 zhoneVoiceStats,
 zhoneVoip,
 zhoneWtn,
 zhoneZAP,
 zhoneZedge,
 zhoneZmsProduct,
 zhoneZplex) = mibBuilder.importSymbols(
    "Zhone",
    "apsMIB",
    "sechtor100",
    "sechtor300",
    "sipCommonMIB",
    "sipTC",
    "sipUAMIB",
    "zhoneAtm",
    "zhoneBridge",
    "zhoneCard",
    "zhoneConsole",
    "zhoneDrafts",
    "zhoneDs3Ext",
    "zhoneDsl",
    "zhoneDsx",
    "zhoneEnet",
    "zhoneGenWtn",
    "zhoneGroups",
    "zhoneIma",
    "zhoneInterfaceGroup",
    "zhoneInterfaceTranslation",
    "zhoneIp",
    "zhoneLineTypes",
    "zhoneMalc",
    "zhoneMasterAgent",
    "zhoneModules",
    "zhoneOcx",
    "zhonePhysical",
    "zhonePls",
    "zhonePpp",
    "zhoneRadio",
    "zhoneRegCpe",
    "zhoneRegMalc",
    "zhoneRegMux",
    "zhoneRegPls",
    "zhoneRegSechtor",
    "zhoneRegWtn",
    "zhoneShelf",
    "zhoneShelfIndex",
    "zhoneShelfSlotCompliance",
    "zhoneShelfSlotGroup",
    "zhoneSlotIndex",
    "zhoneSonet",
    "zhoneSubscriber",
    "zhoneSystem",
    "zhoneTrapModules",
    "zhoneVoice",
    "zhoneVoiceStats",
    "zhoneVoip",
    "zhoneWtn",
    "zhoneZAP",
    "zhoneZedge",
    "zhoneZmsProduct",
    "zhoneZplex")

(ZhoneAdminString,
 ZhoneRowStatus) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminString",
    "ZhoneRowStatus")


# MODULE-IDENTITY

zhoneAponMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1)
)
zhoneAponMIB.setRevisions(
        ("2006-04-25 11:03",
         "2005-04-18 14:42",
         "2004-06-09 11:56",
         "2004-03-25 16:27",
         "2003-12-08 15:29",
         "2003-11-19 12:49",
         "2003-08-18 15:59",
         "2003-08-12 11:25",
         "2003-08-05 10:12")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhoneApon_ObjectIdentity = ObjectIdentity
zhoneApon = _ZhoneApon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12)
)
if mibBuilder.loadTexts:
    zhoneApon.setStatus("current")
_ZhoneOltConfigTable_Object = MibTable
zhoneOltConfigTable = _ZhoneOltConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2)
)
if mibBuilder.loadTexts:
    zhoneOltConfigTable.setStatus("current")
_ZhoneOltConfigEntry_Object = MibTableRow
zhoneOltConfigEntry = _ZhoneOltConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2, 1)
)
zhoneOltConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zhoneOltConfigEntry.setStatus("current")


class _ZhoneOltConfigAutoLearn_Type(Integer32):
    """Custom type zhoneOltConfigAutoLearn based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oltAutolearnDisable", 2),
          ("oltAutolearnEnable", 1))
    )


_ZhoneOltConfigAutoLearn_Type.__name__ = "Integer32"
_ZhoneOltConfigAutoLearn_Object = MibTableColumn
zhoneOltConfigAutoLearn = _ZhoneOltConfigAutoLearn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2, 1, 1),
    _ZhoneOltConfigAutoLearn_Type()
)
zhoneOltConfigAutoLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltConfigAutoLearn.setStatus("current")


class _ZhoneOltConfigCellScrambling_Type(Integer32):
    """Custom type zhoneOltConfigCellScrambling based on Integer32"""
    defaultValue = 4

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
        *(("oltCellScramblingOff", 1),
          ("oltCellScramblingRxAndTx", 4),
          ("oltCellScramblingRxOnly", 2),
          ("oltCellScramblingTxOnly", 3))
    )


_ZhoneOltConfigCellScrambling_Type.__name__ = "Integer32"
_ZhoneOltConfigCellScrambling_Object = MibTableColumn
zhoneOltConfigCellScrambling = _ZhoneOltConfigCellScrambling_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2, 1, 2),
    _ZhoneOltConfigCellScrambling_Type()
)
zhoneOltConfigCellScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltConfigCellScrambling.setStatus("current")


class _ZhoneOltConfigBip8_Type(Integer32):
    """Custom type zhoneOltConfigBip8 based on Integer32"""
    defaultValue = 3

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
        *(("oltBip8Off", 1),
          ("oltBip8RxAndTx", 4),
          ("oltBip8RxCorrectionOnly", 2),
          ("oltBip8TxGenerationOnly", 3))
    )


_ZhoneOltConfigBip8_Type.__name__ = "Integer32"
_ZhoneOltConfigBip8_Object = MibTableColumn
zhoneOltConfigBip8 = _ZhoneOltConfigBip8_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2, 1, 3),
    _ZhoneOltConfigBip8_Type()
)
zhoneOltConfigBip8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltConfigBip8.setStatus("current")


class _ZhoneOltConfigHec_Type(Integer32):
    """Custom type zhoneOltConfigHec based on Integer32"""
    defaultValue = 2

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
        *(("oltHecOff", 1),
          ("oltHecRxAndTx", 4),
          ("oltHecRxCorrectionOnly", 2),
          ("oltHecTxGenerationOnly", 3))
    )


_ZhoneOltConfigHec_Type.__name__ = "Integer32"
_ZhoneOltConfigHec_Object = MibTableColumn
zhoneOltConfigHec = _ZhoneOltConfigHec_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2, 1, 4),
    _ZhoneOltConfigHec_Type()
)
zhoneOltConfigHec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltConfigHec.setStatus("current")


class _ZhoneOltConfigHecRxBypass_Type(TruthValue):
    """Custom type zhoneOltConfigHecRxBypass based on TruthValue"""


_ZhoneOltConfigHecRxBypass_Object = MibTableColumn
zhoneOltConfigHecRxBypass = _ZhoneOltConfigHecRxBypass_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2, 1, 5),
    _ZhoneOltConfigHecRxBypass_Type()
)
zhoneOltConfigHecRxBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltConfigHecRxBypass.setStatus("current")


class _ZhoneOltConfigCrcRx_Type(TruthValue):
    """Custom type zhoneOltConfigCrcRx based on TruthValue"""


_ZhoneOltConfigCrcRx_Object = MibTableColumn
zhoneOltConfigCrcRx = _ZhoneOltConfigCrcRx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2, 1, 6),
    _ZhoneOltConfigCrcRx_Type()
)
zhoneOltConfigCrcRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltConfigCrcRx.setStatus("current")


class _ZhoneOltConfigOverheadSize_Type(Integer32):
    """Custom type zhoneOltConfigOverheadSize based on Integer32"""
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
        *(("oltPonOverhead12Bytes", 3),
          ("oltPonOverhead3Bytes", 1),
          ("oltPonOverhead6Bytes", 2))
    )


_ZhoneOltConfigOverheadSize_Type.__name__ = "Integer32"
_ZhoneOltConfigOverheadSize_Object = MibTableColumn
zhoneOltConfigOverheadSize = _ZhoneOltConfigOverheadSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2, 1, 7),
    _ZhoneOltConfigOverheadSize_Type()
)
zhoneOltConfigOverheadSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltConfigOverheadSize.setStatus("current")


class _ZhoneOltConfigDelimiterPattern_Type(Integer32):
    """Custom type zhoneOltConfigDelimiterPattern based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneOltConfigDelimiterPattern_Type.__name__ = "Integer32"
_ZhoneOltConfigDelimiterPattern_Object = MibTableColumn
zhoneOltConfigDelimiterPattern = _ZhoneOltConfigDelimiterPattern_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2, 1, 8),
    _ZhoneOltConfigDelimiterPattern_Type()
)
zhoneOltConfigDelimiterPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltConfigDelimiterPattern.setStatus("current")


class _ZhoneOltConfigDelimiterSize_Type(Integer32):
    """Custom type zhoneOltConfigDelimiterSize based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 16),
    )


_ZhoneOltConfigDelimiterSize_Type.__name__ = "Integer32"
_ZhoneOltConfigDelimiterSize_Object = MibTableColumn
zhoneOltConfigDelimiterSize = _ZhoneOltConfigDelimiterSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2, 1, 9),
    _ZhoneOltConfigDelimiterSize_Type()
)
zhoneOltConfigDelimiterSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltConfigDelimiterSize.setStatus("current")
if mibBuilder.loadTexts:
    zhoneOltConfigDelimiterSize.setUnits("Number of bits")


class _ZhoneOltConfigCdrPattern_Type(Integer32):
    """Custom type zhoneOltConfigCdrPattern based on Integer32"""
    defaultValue = 192

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneOltConfigCdrPattern_Type.__name__ = "Integer32"
_ZhoneOltConfigCdrPattern_Object = MibTableColumn
zhoneOltConfigCdrPattern = _ZhoneOltConfigCdrPattern_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2, 1, 10),
    _ZhoneOltConfigCdrPattern_Type()
)
zhoneOltConfigCdrPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltConfigCdrPattern.setStatus("current")


class _ZhoneOltConfigCdrLocation_Type(Integer32):
    """Custom type zhoneOltConfigCdrLocation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_ZhoneOltConfigCdrLocation_Type.__name__ = "Integer32"
_ZhoneOltConfigCdrLocation_Object = MibTableColumn
zhoneOltConfigCdrLocation = _ZhoneOltConfigCdrLocation_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2, 1, 11),
    _ZhoneOltConfigCdrLocation_Type()
)
zhoneOltConfigCdrLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltConfigCdrLocation.setStatus("current")


class _ZhoneOltConfigCdrActiveHigh_Type(TruthValue):
    """Custom type zhoneOltConfigCdrActiveHigh based on TruthValue"""


_ZhoneOltConfigCdrActiveHigh_Object = MibTableColumn
zhoneOltConfigCdrActiveHigh = _ZhoneOltConfigCdrActiveHigh_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2, 1, 12),
    _ZhoneOltConfigCdrActiveHigh_Type()
)
zhoneOltConfigCdrActiveHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltConfigCdrActiveHigh.setStatus("current")


class _ZhoneOltConfigCpeLimit_Type(Integer32):
    """Custom type zhoneOltConfigCpeLimit based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ZhoneOltConfigCpeLimit_Type.__name__ = "Integer32"
_ZhoneOltConfigCpeLimit_Object = MibTableColumn
zhoneOltConfigCpeLimit = _ZhoneOltConfigCpeLimit_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2, 1, 13),
    _ZhoneOltConfigCpeLimit_Type()
)
zhoneOltConfigCpeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltConfigCpeLimit.setStatus("current")


class _ZhoneOltConfigLcdLimit_Type(Integer32):
    """Custom type zhoneOltConfigLcdLimit based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_ZhoneOltConfigLcdLimit_Type.__name__ = "Integer32"
_ZhoneOltConfigLcdLimit_Object = MibTableColumn
zhoneOltConfigLcdLimit = _ZhoneOltConfigLcdLimit_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2, 1, 14),
    _ZhoneOltConfigLcdLimit_Type()
)
zhoneOltConfigLcdLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltConfigLcdLimit.setStatus("current")


class _ZhoneOltConfigLcdAlpha_Type(Integer32):
    """Custom type zhoneOltConfigLcdAlpha based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ZhoneOltConfigLcdAlpha_Type.__name__ = "Integer32"
_ZhoneOltConfigLcdAlpha_Object = MibTableColumn
zhoneOltConfigLcdAlpha = _ZhoneOltConfigLcdAlpha_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2, 1, 15),
    _ZhoneOltConfigLcdAlpha_Type()
)
zhoneOltConfigLcdAlpha.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltConfigLcdAlpha.setStatus("current")


class _ZhoneOltConfigLcdDelta_Type(Integer32):
    """Custom type zhoneOltConfigLcdDelta based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ZhoneOltConfigLcdDelta_Type.__name__ = "Integer32"
_ZhoneOltConfigLcdDelta_Object = MibTableColumn
zhoneOltConfigLcdDelta = _ZhoneOltConfigLcdDelta_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2, 1, 16),
    _ZhoneOltConfigLcdDelta_Type()
)
zhoneOltConfigLcdDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltConfigLcdDelta.setStatus("current")


class _ZhoneOltConfigTxDiscardNonMatchingVpi_Type(TruthValue):
    """Custom type zhoneOltConfigTxDiscardNonMatchingVpi based on TruthValue"""


_ZhoneOltConfigTxDiscardNonMatchingVpi_Object = MibTableColumn
zhoneOltConfigTxDiscardNonMatchingVpi = _ZhoneOltConfigTxDiscardNonMatchingVpi_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2, 1, 17),
    _ZhoneOltConfigTxDiscardNonMatchingVpi_Type()
)
zhoneOltConfigTxDiscardNonMatchingVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltConfigTxDiscardNonMatchingVpi.setStatus("current")


class _ZhoneOltConfigUtopiaDiscard_Type(TruthValue):
    """Custom type zhoneOltConfigUtopiaDiscard based on TruthValue"""


_ZhoneOltConfigUtopiaDiscard_Object = MibTableColumn
zhoneOltConfigUtopiaDiscard = _ZhoneOltConfigUtopiaDiscard_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2, 1, 18),
    _ZhoneOltConfigUtopiaDiscard_Type()
)
zhoneOltConfigUtopiaDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltConfigUtopiaDiscard.setStatus("current")


class _ZhoneOltConfigSyncBytesClkDivisor_Type(Integer32):
    """Custom type zhoneOltConfigSyncBytesClkDivisor based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneOltConfigSyncBytesClkDivisor_Type.__name__ = "Integer32"
_ZhoneOltConfigSyncBytesClkDivisor_Object = MibTableColumn
zhoneOltConfigSyncBytesClkDivisor = _ZhoneOltConfigSyncBytesClkDivisor_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2, 1, 19),
    _ZhoneOltConfigSyncBytesClkDivisor_Type()
)
zhoneOltConfigSyncBytesClkDivisor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltConfigSyncBytesClkDivisor.setStatus("current")


class _ZhoneOltConfigTxSyncBytes_Type(Integer32):
    """Custom type zhoneOltConfigTxSyncBytes based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("txSyncBytesDisable", 2),
          ("txSyncBytesEnable", 1))
    )


_ZhoneOltConfigTxSyncBytes_Type.__name__ = "Integer32"
_ZhoneOltConfigTxSyncBytes_Object = MibTableColumn
zhoneOltConfigTxSyncBytes = _ZhoneOltConfigTxSyncBytes_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2, 1, 20),
    _ZhoneOltConfigTxSyncBytes_Type()
)
zhoneOltConfigTxSyncBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltConfigTxSyncBytes.setStatus("current")


class _ZhoneOltConfigLoopback_Type(Integer32):
    """Custom type zhoneOltConfigLoopback based on Integer32"""
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
        *(("loopbackInward", 2),
          ("loopbackLine", 3),
          ("loopbackNone", 1))
    )


_ZhoneOltConfigLoopback_Type.__name__ = "Integer32"
_ZhoneOltConfigLoopback_Object = MibTableColumn
zhoneOltConfigLoopback = _ZhoneOltConfigLoopback_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2, 1, 21),
    _ZhoneOltConfigLoopback_Type()
)
zhoneOltConfigLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltConfigLoopback.setStatus("current")


class _ZhoneOltConfigMaxPonDistance_Type(Integer32):
    """Custom type zhoneOltConfigMaxPonDistance based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneOltConfigMaxPonDistance_Type.__name__ = "Integer32"
_ZhoneOltConfigMaxPonDistance_Object = MibTableColumn
zhoneOltConfigMaxPonDistance = _ZhoneOltConfigMaxPonDistance_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2, 1, 22),
    _ZhoneOltConfigMaxPonDistance_Type()
)
zhoneOltConfigMaxPonDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltConfigMaxPonDistance.setStatus("current")
if mibBuilder.loadTexts:
    zhoneOltConfigMaxPonDistance.setUnits("Distance in microseconds, used in the ranging process.")


class _ZhoneOltConfigLineStatusChangeTrapEnable_Type(Integer32):
    """Custom type zhoneOltConfigLineStatusChangeTrapEnable based on Integer32"""
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


_ZhoneOltConfigLineStatusChangeTrapEnable_Type.__name__ = "Integer32"
_ZhoneOltConfigLineStatusChangeTrapEnable_Object = MibTableColumn
zhoneOltConfigLineStatusChangeTrapEnable = _ZhoneOltConfigLineStatusChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 2, 1, 23),
    _ZhoneOltConfigLineStatusChangeTrapEnable_Type()
)
zhoneOltConfigLineStatusChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltConfigLineStatusChangeTrapEnable.setStatus("current")
_ZhoneOltStatusTable_Object = MibTable
zhoneOltStatusTable = _ZhoneOltStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 3)
)
if mibBuilder.loadTexts:
    zhoneOltStatusTable.setStatus("current")
_ZhoneOltStatusEntry_Object = MibTableRow
zhoneOltStatusEntry = _ZhoneOltStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 3, 1)
)
zhoneOltStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zhoneOltStatusEntry.setStatus("current")


class _ZhoneOltStatusState_Type(Integer32):
    """Custom type zhoneOltStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oltStateDown", 1),
          ("oltStateUp", 2))
    )


_ZhoneOltStatusState_Type.__name__ = "Integer32"
_ZhoneOltStatusState_Object = MibTableColumn
zhoneOltStatusState = _ZhoneOltStatusState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 3, 1, 1),
    _ZhoneOltStatusState_Type()
)
zhoneOltStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOltStatusState.setStatus("current")


class _ZhoneOltStatusLoopback_Type(Integer32):
    """Custom type zhoneOltStatusLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oltLoopbackInward", 2),
          ("oltLoopbackLine", 3),
          ("oltLoopbackNone", 1))
    )


_ZhoneOltStatusLoopback_Type.__name__ = "Integer32"
_ZhoneOltStatusLoopback_Object = MibTableColumn
zhoneOltStatusLoopback = _ZhoneOltStatusLoopback_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 3, 1, 2),
    _ZhoneOltStatusLoopback_Type()
)
zhoneOltStatusLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOltStatusLoopback.setStatus("current")
_ZhoneOltStatusPonAlarmLPHY_Type = TruthValue
_ZhoneOltStatusPonAlarmLPHY_Object = MibTableColumn
zhoneOltStatusPonAlarmLPHY = _ZhoneOltStatusPonAlarmLPHY_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 3, 1, 3),
    _ZhoneOltStatusPonAlarmLPHY_Type()
)
zhoneOltStatusPonAlarmLPHY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOltStatusPonAlarmLPHY.setStatus("current")
_ZhoneOltStatusPonAlarmTF_Type = TruthValue
_ZhoneOltStatusPonAlarmTF_Object = MibTableColumn
zhoneOltStatusPonAlarmTF = _ZhoneOltStatusPonAlarmTF_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 3, 1, 4),
    _ZhoneOltStatusPonAlarmTF_Type()
)
zhoneOltStatusPonAlarmTF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOltStatusPonAlarmTF.setStatus("current")
_ZhoneOltStatusPonAlarmSUF_Type = TruthValue
_ZhoneOltStatusPonAlarmSUF_Object = MibTableColumn
zhoneOltStatusPonAlarmSUF = _ZhoneOltStatusPonAlarmSUF_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 3, 1, 5),
    _ZhoneOltStatusPonAlarmSUF_Type()
)
zhoneOltStatusPonAlarmSUF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOltStatusPonAlarmSUF.setStatus("current")
_ZhoneOltStatusPonAlarmPEE_Type = TruthValue
_ZhoneOltStatusPonAlarmPEE_Object = MibTableColumn
zhoneOltStatusPonAlarmPEE = _ZhoneOltStatusPonAlarmPEE_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 3, 1, 6),
    _ZhoneOltStatusPonAlarmPEE_Type()
)
zhoneOltStatusPonAlarmPEE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOltStatusPonAlarmPEE.setStatus("current")
_ZhoneOltStatusPonAlarmLCD_Type = TruthValue
_ZhoneOltStatusPonAlarmLCD_Object = MibTableColumn
zhoneOltStatusPonAlarmLCD = _ZhoneOltStatusPonAlarmLCD_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 3, 1, 7),
    _ZhoneOltStatusPonAlarmLCD_Type()
)
zhoneOltStatusPonAlarmLCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOltStatusPonAlarmLCD.setStatus("current")
_ZhoneOltStatusPonAlarmLOS_Type = TruthValue
_ZhoneOltStatusPonAlarmLOS_Object = MibTableColumn
zhoneOltStatusPonAlarmLOS = _ZhoneOltStatusPonAlarmLOS_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 3, 1, 8),
    _ZhoneOltStatusPonAlarmLOS_Type()
)
zhoneOltStatusPonAlarmLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOltStatusPonAlarmLOS.setStatus("current")
_ZhoneOltStatusPonAlarmOAML_Type = TruthValue
_ZhoneOltStatusPonAlarmOAML_Object = MibTableColumn
zhoneOltStatusPonAlarmOAML = _ZhoneOltStatusPonAlarmOAML_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 3, 1, 9),
    _ZhoneOltStatusPonAlarmOAML_Type()
)
zhoneOltStatusPonAlarmOAML.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOltStatusPonAlarmOAML.setStatus("current")
_ZhoneOltStatusPonAlarmCPE_Type = TruthValue
_ZhoneOltStatusPonAlarmCPE_Object = MibTableColumn
zhoneOltStatusPonAlarmCPE = _ZhoneOltStatusPonAlarmCPE_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 3, 1, 10),
    _ZhoneOltStatusPonAlarmCPE_Type()
)
zhoneOltStatusPonAlarmCPE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOltStatusPonAlarmCPE.setStatus("current")


class _ZhoneOltStatusLastChange_Type(TimeStamp):
    """Custom type zhoneOltStatusLastChange based on TimeStamp"""
    defaultValue = 0


_ZhoneOltStatusLastChange_Object = MibTableColumn
zhoneOltStatusLastChange = _ZhoneOltStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 3, 1, 11),
    _ZhoneOltStatusLastChange_Type()
)
zhoneOltStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOltStatusLastChange.setStatus("current")
_ZhoneOltOnuConfigTable_Object = MibTable
zhoneOltOnuConfigTable = _ZhoneOltOnuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 4)
)
if mibBuilder.loadTexts:
    zhoneOltOnuConfigTable.setStatus("current")
_ZhoneOltOnuConfigEntry_Object = MibTableRow
zhoneOltOnuConfigEntry = _ZhoneOltOnuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 4, 1)
)
zhoneOltOnuConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zhoneOltOnuConfigEntry.setStatus("current")


class _ZhoneOltOnuConfigPassword_Type(ZhoneAdminString):
    """Custom type zhoneOltOnuConfigPassword based on ZhoneAdminString"""
    subtypeSpec = ZhoneAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ZhoneOltOnuConfigPassword_Type.__name__ = "ZhoneAdminString"
_ZhoneOltOnuConfigPassword_Object = MibTableColumn
zhoneOltOnuConfigPassword = _ZhoneOltOnuConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 4, 1, 1),
    _ZhoneOltOnuConfigPassword_Type()
)
zhoneOltOnuConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltOnuConfigPassword.setStatus("current")


class _ZhoneOltOnuConfigSerialNum_Type(Integer32):
    """Custom type zhoneOltOnuConfigSerialNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneOltOnuConfigSerialNum_Type.__name__ = "Integer32"
_ZhoneOltOnuConfigSerialNum_Object = MibTableColumn
zhoneOltOnuConfigSerialNum = _ZhoneOltOnuConfigSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 4, 1, 2),
    _ZhoneOltOnuConfigSerialNum_Type()
)
zhoneOltOnuConfigSerialNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltOnuConfigSerialNum.setStatus("current")


class _ZhoneOltOnuConfigChurnkey_Type(Integer32):
    """Custom type zhoneOltOnuConfigChurnkey based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onuChurnkeyDisable", 2),
          ("onuChurnkeyEnable", 1))
    )


_ZhoneOltOnuConfigChurnkey_Type.__name__ = "Integer32"
_ZhoneOltOnuConfigChurnkey_Object = MibTableColumn
zhoneOltOnuConfigChurnkey = _ZhoneOltOnuConfigChurnkey_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 4, 1, 3),
    _ZhoneOltOnuConfigChurnkey_Type()
)
zhoneOltOnuConfigChurnkey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltOnuConfigChurnkey.setStatus("current")


class _ZhoneOltOnuConfigLineStatusChangeTrapEnable_Type(Integer32):
    """Custom type zhoneOltOnuConfigLineStatusChangeTrapEnable based on Integer32"""
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


_ZhoneOltOnuConfigLineStatusChangeTrapEnable_Type.__name__ = "Integer32"
_ZhoneOltOnuConfigLineStatusChangeTrapEnable_Object = MibTableColumn
zhoneOltOnuConfigLineStatusChangeTrapEnable = _ZhoneOltOnuConfigLineStatusChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 4, 1, 4),
    _ZhoneOltOnuConfigLineStatusChangeTrapEnable_Type()
)
zhoneOltOnuConfigLineStatusChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOltOnuConfigLineStatusChangeTrapEnable.setStatus("current")
_ZhoneOltOnuStatusTable_Object = MibTable
zhoneOltOnuStatusTable = _ZhoneOltOnuStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 5)
)
if mibBuilder.loadTexts:
    zhoneOltOnuStatusTable.setStatus("current")
_ZhoneOltOnuStatusEntry_Object = MibTableRow
zhoneOltOnuStatusEntry = _ZhoneOltOnuStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 5, 1)
)
zhoneOltOnuStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zhoneOltOnuStatusEntry.setStatus("current")
_ZhoneOltOnuStatusPonAlarmLOA_Type = TruthValue
_ZhoneOltOnuStatusPonAlarmLOA_Object = MibTableColumn
zhoneOltOnuStatusPonAlarmLOA = _ZhoneOltOnuStatusPonAlarmLOA_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 5, 1, 1),
    _ZhoneOltOnuStatusPonAlarmLOA_Type()
)
zhoneOltOnuStatusPonAlarmLOA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOltOnuStatusPonAlarmLOA.setStatus("current")
_ZhoneOltOnuStatusPonAlarmERR_Type = TruthValue
_ZhoneOltOnuStatusPonAlarmERR_Object = MibTableColumn
zhoneOltOnuStatusPonAlarmERR = _ZhoneOltOnuStatusPonAlarmERR_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 5, 1, 2),
    _ZhoneOltOnuStatusPonAlarmERR_Type()
)
zhoneOltOnuStatusPonAlarmERR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOltOnuStatusPonAlarmERR.setStatus("current")
_ZhoneOltOnuStatusPonAlarmSD_Type = TruthValue
_ZhoneOltOnuStatusPonAlarmSD_Object = MibTableColumn
zhoneOltOnuStatusPonAlarmSD = _ZhoneOltOnuStatusPonAlarmSD_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 5, 1, 3),
    _ZhoneOltOnuStatusPonAlarmSD_Type()
)
zhoneOltOnuStatusPonAlarmSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOltOnuStatusPonAlarmSD.setStatus("current")
_ZhoneOltOnuStatusPonAlarmREI_Type = TruthValue
_ZhoneOltOnuStatusPonAlarmREI_Object = MibTableColumn
zhoneOltOnuStatusPonAlarmREI = _ZhoneOltOnuStatusPonAlarmREI_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 5, 1, 4),
    _ZhoneOltOnuStatusPonAlarmREI_Type()
)
zhoneOltOnuStatusPonAlarmREI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOltOnuStatusPonAlarmREI.setStatus("current")
_ZhoneOltOnuStatusPonAlarmMEM_Type = TruthValue
_ZhoneOltOnuStatusPonAlarmMEM_Object = MibTableColumn
zhoneOltOnuStatusPonAlarmMEM = _ZhoneOltOnuStatusPonAlarmMEM_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 5, 1, 5),
    _ZhoneOltOnuStatusPonAlarmMEM_Type()
)
zhoneOltOnuStatusPonAlarmMEM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOltOnuStatusPonAlarmMEM.setStatus("current")
_ZhoneOltOnuStatusPonAlarmRXINH_Type = TruthValue
_ZhoneOltOnuStatusPonAlarmRXINH_Object = MibTableColumn
zhoneOltOnuStatusPonAlarmRXINH = _ZhoneOltOnuStatusPonAlarmRXINH_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 5, 1, 6),
    _ZhoneOltOnuStatusPonAlarmRXINH_Type()
)
zhoneOltOnuStatusPonAlarmRXINH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOltOnuStatusPonAlarmRXINH.setStatus("current")
_ZhoneOltOnuStatusPonAlarmLOS_Type = TruthValue
_ZhoneOltOnuStatusPonAlarmLOS_Object = MibTableColumn
zhoneOltOnuStatusPonAlarmLOS = _ZhoneOltOnuStatusPonAlarmLOS_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 5, 1, 7),
    _ZhoneOltOnuStatusPonAlarmLOS_Type()
)
zhoneOltOnuStatusPonAlarmLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOltOnuStatusPonAlarmLOS.setStatus("current")
_ZhoneOltOnuStatusPonAlarmPEE_Type = TruthValue
_ZhoneOltOnuStatusPonAlarmPEE_Object = MibTableColumn
zhoneOltOnuStatusPonAlarmPEE = _ZhoneOltOnuStatusPonAlarmPEE_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 5, 1, 8),
    _ZhoneOltOnuStatusPonAlarmPEE_Type()
)
zhoneOltOnuStatusPonAlarmPEE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOltOnuStatusPonAlarmPEE.setStatus("current")
_ZhoneOltOnuStatusPonAlarmSUF_Type = TruthValue
_ZhoneOltOnuStatusPonAlarmSUF_Object = MibTableColumn
zhoneOltOnuStatusPonAlarmSUF = _ZhoneOltOnuStatusPonAlarmSUF_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 5, 1, 9),
    _ZhoneOltOnuStatusPonAlarmSUF_Type()
)
zhoneOltOnuStatusPonAlarmSUF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOltOnuStatusPonAlarmSUF.setStatus("current")
_ZhoneOltOnuStatusPonAlarmOAML_Type = TruthValue
_ZhoneOltOnuStatusPonAlarmOAML_Object = MibTableColumn
zhoneOltOnuStatusPonAlarmOAML = _ZhoneOltOnuStatusPonAlarmOAML_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 5, 1, 10),
    _ZhoneOltOnuStatusPonAlarmOAML_Type()
)
zhoneOltOnuStatusPonAlarmOAML.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOltOnuStatusPonAlarmOAML.setStatus("current")
_ZhoneOltOnuStatusPonAlarmLCD_Type = TruthValue
_ZhoneOltOnuStatusPonAlarmLCD_Object = MibTableColumn
zhoneOltOnuStatusPonAlarmLCD = _ZhoneOltOnuStatusPonAlarmLCD_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 5, 1, 11),
    _ZhoneOltOnuStatusPonAlarmLCD_Type()
)
zhoneOltOnuStatusPonAlarmLCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOltOnuStatusPonAlarmLCD.setStatus("current")
_ZhoneOnuConfigTable_Object = MibTable
zhoneOnuConfigTable = _ZhoneOnuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 6)
)
if mibBuilder.loadTexts:
    zhoneOnuConfigTable.setStatus("current")
_ZhoneOnuConfigEntry_Object = MibTableRow
zhoneOnuConfigEntry = _ZhoneOnuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 6, 1)
)
zhoneOnuConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zhoneOnuConfigEntry.setStatus("current")


class _ZhoneOnuConfigSerialNumber_Type(Integer32):
    """Custom type zhoneOnuConfigSerialNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneOnuConfigSerialNumber_Type.__name__ = "Integer32"
_ZhoneOnuConfigSerialNumber_Object = MibTableColumn
zhoneOnuConfigSerialNumber = _ZhoneOnuConfigSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 6, 1, 1),
    _ZhoneOnuConfigSerialNumber_Type()
)
zhoneOnuConfigSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuConfigSerialNumber.setStatus("current")
_ZhoneOnuConfigPassword_Type = ZhoneAdminString
_ZhoneOnuConfigPassword_Object = MibTableColumn
zhoneOnuConfigPassword = _ZhoneOnuConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 6, 1, 2),
    _ZhoneOnuConfigPassword_Type()
)
zhoneOnuConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOnuConfigPassword.setStatus("current")


class _ZhoneOnuConfigNetworkRefClk_Type(TruthValue):
    """Custom type zhoneOnuConfigNetworkRefClk based on TruthValue"""


_ZhoneOnuConfigNetworkRefClk_Object = MibTableColumn
zhoneOnuConfigNetworkRefClk = _ZhoneOnuConfigNetworkRefClk_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 6, 1, 3),
    _ZhoneOnuConfigNetworkRefClk_Type()
)
zhoneOnuConfigNetworkRefClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOnuConfigNetworkRefClk.setStatus("current")


class _ZhoneOnuConfigHEC_Type(Integer32):
    """Custom type zhoneOnuConfigHEC based on Integer32"""
    defaultValue = 4

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
        *(("onuOff", 1),
          ("onuRxAndTx", 4),
          ("onuRxCorrectionOnly", 2),
          ("onuTxGenerationOnly", 3))
    )


_ZhoneOnuConfigHEC_Type.__name__ = "Integer32"
_ZhoneOnuConfigHEC_Object = MibTableColumn
zhoneOnuConfigHEC = _ZhoneOnuConfigHEC_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 6, 1, 4),
    _ZhoneOnuConfigHEC_Type()
)
zhoneOnuConfigHEC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOnuConfigHEC.setStatus("current")


class _ZhoneOnuConfigLoopback_Type(Integer32):
    """Custom type zhoneOnuConfigLoopback based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("onuInward", 2),
          ("onuLine", 3),
          ("onuNone", 1))
    )


_ZhoneOnuConfigLoopback_Type.__name__ = "Integer32"
_ZhoneOnuConfigLoopback_Object = MibTableColumn
zhoneOnuConfigLoopback = _ZhoneOnuConfigLoopback_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 6, 1, 5),
    _ZhoneOnuConfigLoopback_Type()
)
zhoneOnuConfigLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOnuConfigLoopback.setStatus("current")


class _ZhoneOnuConfigOverheadSize_Type(Integer32):
    """Custom type zhoneOnuConfigOverheadSize based on Integer32"""
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
        *(("onuOverheadSize12Bytes", 3),
          ("onuOverheadSize3Bytes", 1),
          ("onuOverheadSize6Bytes", 2))
    )


_ZhoneOnuConfigOverheadSize_Type.__name__ = "Integer32"
_ZhoneOnuConfigOverheadSize_Object = MibTableColumn
zhoneOnuConfigOverheadSize = _ZhoneOnuConfigOverheadSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 6, 1, 6),
    _ZhoneOnuConfigOverheadSize_Type()
)
zhoneOnuConfigOverheadSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOnuConfigOverheadSize.setStatus("current")


class _ZhoneOnuConfigRfVideo_Type(Integer32):
    """Custom type zhoneOnuConfigRfVideo based on Integer32"""
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


_ZhoneOnuConfigRfVideo_Type.__name__ = "Integer32"
_ZhoneOnuConfigRfVideo_Object = MibTableColumn
zhoneOnuConfigRfVideo = _ZhoneOnuConfigRfVideo_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 6, 1, 7),
    _ZhoneOnuConfigRfVideo_Type()
)
zhoneOnuConfigRfVideo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneOnuConfigRfVideo.setStatus("current")
_ZhoneOnuStatusTable_Object = MibTable
zhoneOnuStatusTable = _ZhoneOnuStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 7)
)
if mibBuilder.loadTexts:
    zhoneOnuStatusTable.setStatus("current")
_ZhoneOnuStatusEntry_Object = MibTableRow
zhoneOnuStatusEntry = _ZhoneOnuStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 7, 1)
)
zhoneOnuStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zhoneOnuStatusEntry.setStatus("current")


class _ZhoneOnuStatusOperStatus_Type(Integer32):
    """Custom type zhoneOnuStatusOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onuStateDown", 1),
          ("onuStateUp", 2))
    )


_ZhoneOnuStatusOperStatus_Type.__name__ = "Integer32"
_ZhoneOnuStatusOperStatus_Object = MibTableColumn
zhoneOnuStatusOperStatus = _ZhoneOnuStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 7, 1, 1),
    _ZhoneOnuStatusOperStatus_Type()
)
zhoneOnuStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuStatusOperStatus.setStatus("current")


class _ZhoneOnuStatusLoopback_Type(Integer32):
    """Custom type zhoneOnuStatusLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("onuInward", 2),
          ("onuLine", 3),
          ("onuNone", 1))
    )


_ZhoneOnuStatusLoopback_Type.__name__ = "Integer32"
_ZhoneOnuStatusLoopback_Object = MibTableColumn
zhoneOnuStatusLoopback = _ZhoneOnuStatusLoopback_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 7, 1, 2),
    _ZhoneOnuStatusLoopback_Type()
)
zhoneOnuStatusLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuStatusLoopback.setStatus("current")
_ZhoneOnuStatusAlarmTF_Type = TruthValue
_ZhoneOnuStatusAlarmTF_Object = MibTableColumn
zhoneOnuStatusAlarmTF = _ZhoneOnuStatusAlarmTF_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 7, 1, 3),
    _ZhoneOnuStatusAlarmTF_Type()
)
zhoneOnuStatusAlarmTF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuStatusAlarmTF.setStatus("current")
_ZhoneOnuStatusAlarmLOS_Type = TruthValue
_ZhoneOnuStatusAlarmLOS_Object = MibTableColumn
zhoneOnuStatusAlarmLOS = _ZhoneOnuStatusAlarmLOS_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 7, 1, 4),
    _ZhoneOnuStatusAlarmLOS_Type()
)
zhoneOnuStatusAlarmLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuStatusAlarmLOS.setStatus("current")
_ZhoneOnuStatusAlarmPEE_Type = TruthValue
_ZhoneOnuStatusAlarmPEE_Object = MibTableColumn
zhoneOnuStatusAlarmPEE = _ZhoneOnuStatusAlarmPEE_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 7, 1, 5),
    _ZhoneOnuStatusAlarmPEE_Type()
)
zhoneOnuStatusAlarmPEE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuStatusAlarmPEE.setStatus("current")
_ZhoneOnuStatusAlarmSUF_Type = TruthValue
_ZhoneOnuStatusAlarmSUF_Object = MibTableColumn
zhoneOnuStatusAlarmSUF = _ZhoneOnuStatusAlarmSUF_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 7, 1, 6),
    _ZhoneOnuStatusAlarmSUF_Type()
)
zhoneOnuStatusAlarmSUF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuStatusAlarmSUF.setStatus("current")
_ZhoneOnuStatusAlarmOAML_Type = TruthValue
_ZhoneOnuStatusAlarmOAML_Object = MibTableColumn
zhoneOnuStatusAlarmOAML = _ZhoneOnuStatusAlarmOAML_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 7, 1, 7),
    _ZhoneOnuStatusAlarmOAML_Type()
)
zhoneOnuStatusAlarmOAML.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuStatusAlarmOAML.setStatus("current")
_ZhoneOnuStatusAlarmLCD_Type = TruthValue
_ZhoneOnuStatusAlarmLCD_Object = MibTableColumn
zhoneOnuStatusAlarmLCD = _ZhoneOnuStatusAlarmLCD_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 7, 1, 8),
    _ZhoneOnuStatusAlarmLCD_Type()
)
zhoneOnuStatusAlarmLCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuStatusAlarmLCD.setStatus("current")
_ZhoneOnuStatusAlarmFRML_Type = TruthValue
_ZhoneOnuStatusAlarmFRML_Object = MibTableColumn
zhoneOnuStatusAlarmFRML = _ZhoneOnuStatusAlarmFRML_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 7, 1, 9),
    _ZhoneOnuStatusAlarmFRML_Type()
)
zhoneOnuStatusAlarmFRML.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuStatusAlarmFRML.setStatus("current")
_ZhoneOnuStatusAlarmERR_Type = TruthValue
_ZhoneOnuStatusAlarmERR_Object = MibTableColumn
zhoneOnuStatusAlarmERR = _ZhoneOnuStatusAlarmERR_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 7, 1, 10),
    _ZhoneOnuStatusAlarmERR_Type()
)
zhoneOnuStatusAlarmERR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuStatusAlarmERR.setStatus("current")
_ZhoneOnuStatusAlarmSD_Type = TruthValue
_ZhoneOnuStatusAlarmSD_Object = MibTableColumn
zhoneOnuStatusAlarmSD = _ZhoneOnuStatusAlarmSD_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 7, 1, 11),
    _ZhoneOnuStatusAlarmSD_Type()
)
zhoneOnuStatusAlarmSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuStatusAlarmSD.setStatus("current")
_ZhoneOnuStatusAlarmMEM_Type = TruthValue
_ZhoneOnuStatusAlarmMEM_Object = MibTableColumn
zhoneOnuStatusAlarmMEM = _ZhoneOnuStatusAlarmMEM_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 7, 1, 12),
    _ZhoneOnuStatusAlarmMEM_Type()
)
zhoneOnuStatusAlarmMEM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuStatusAlarmMEM.setStatus("current")
_ZhoneOnuStatusAlarmDACT_Type = TruthValue
_ZhoneOnuStatusAlarmDACT_Object = MibTableColumn
zhoneOnuStatusAlarmDACT = _ZhoneOnuStatusAlarmDACT_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 7, 1, 13),
    _ZhoneOnuStatusAlarmDACT_Type()
)
zhoneOnuStatusAlarmDACT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuStatusAlarmDACT.setStatus("current")
_ZhoneOnuStatusAlarmDIS_Type = TruthValue
_ZhoneOnuStatusAlarmDIS_Object = MibTableColumn
zhoneOnuStatusAlarmDIS = _ZhoneOnuStatusAlarmDIS_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 7, 1, 14),
    _ZhoneOnuStatusAlarmDIS_Type()
)
zhoneOnuStatusAlarmDIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuStatusAlarmDIS.setStatus("current")
_ZhoneOnuStatusAlarmMIS_Type = TruthValue
_ZhoneOnuStatusAlarmMIS_Object = MibTableColumn
zhoneOnuStatusAlarmMIS = _ZhoneOnuStatusAlarmMIS_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 7, 1, 15),
    _ZhoneOnuStatusAlarmMIS_Type()
)
zhoneOnuStatusAlarmMIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuStatusAlarmMIS.setStatus("current")


class _ZhoneOnuStatusLastChange_Type(TimeStamp):
    """Custom type zhoneOnuStatusLastChange based on TimeStamp"""
    defaultBinValue = 0


_ZhoneOnuStatusLastChange_Object = MibTableColumn
zhoneOnuStatusLastChange = _ZhoneOnuStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 7, 1, 16),
    _ZhoneOnuStatusLastChange_Type()
)
zhoneOnuStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuStatusLastChange.setStatus("current")


class _ZhoneOltTrafficContainerIndexNext_Type(Integer32):
    """Custom type zhoneOltTrafficContainerIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneOltTrafficContainerIndexNext_Type.__name__ = "Integer32"
_ZhoneOltTrafficContainerIndexNext_Object = MibScalar
zhoneOltTrafficContainerIndexNext = _ZhoneOltTrafficContainerIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 8),
    _ZhoneOltTrafficContainerIndexNext_Type()
)
zhoneOltTrafficContainerIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOltTrafficContainerIndexNext.setStatus("current")
_ZhoneOltTrafficContainerTable_Object = MibTable
zhoneOltTrafficContainerTable = _ZhoneOltTrafficContainerTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 9)
)
if mibBuilder.loadTexts:
    zhoneOltTrafficContainerTable.setStatus("current")
_ZhoneOltTrafficContainerEntry_Object = MibTableRow
zhoneOltTrafficContainerEntry = _ZhoneOltTrafficContainerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 9, 1)
)
zhoneOltTrafficContainerEntry.setIndexNames(
    (0, "ZhoneAPON-MIB", "zhoneOltTrafficContainerIndex"),
)
if mibBuilder.loadTexts:
    zhoneOltTrafficContainerEntry.setStatus("current")


class _ZhoneOltTrafficContainerIndex_Type(Integer32):
    """Custom type zhoneOltTrafficContainerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZhoneOltTrafficContainerIndex_Type.__name__ = "Integer32"
_ZhoneOltTrafficContainerIndex_Object = MibTableColumn
zhoneOltTrafficContainerIndex = _ZhoneOltTrafficContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 9, 1, 1),
    _ZhoneOltTrafficContainerIndex_Type()
)
zhoneOltTrafficContainerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneOltTrafficContainerIndex.setStatus("current")


class _ZhoneOltTrafficContainerGuaranteedBW_Type(Unsigned32):
    """Custom type zhoneOltTrafficContainerGuaranteedBW based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneOltTrafficContainerGuaranteedBW_Type.__name__ = "Unsigned32"
_ZhoneOltTrafficContainerGuaranteedBW_Object = MibTableColumn
zhoneOltTrafficContainerGuaranteedBW = _ZhoneOltTrafficContainerGuaranteedBW_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 9, 1, 2),
    _ZhoneOltTrafficContainerGuaranteedBW_Type()
)
zhoneOltTrafficContainerGuaranteedBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneOltTrafficContainerGuaranteedBW.setStatus("current")
if mibBuilder.loadTexts:
    zhoneOltTrafficContainerGuaranteedBW.setUnits("Megabits per second")


class _ZhoneOltTrafficContainerMaximumBW_Type(Unsigned32):
    """Custom type zhoneOltTrafficContainerMaximumBW based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneOltTrafficContainerMaximumBW_Type.__name__ = "Unsigned32"
_ZhoneOltTrafficContainerMaximumBW_Object = MibTableColumn
zhoneOltTrafficContainerMaximumBW = _ZhoneOltTrafficContainerMaximumBW_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 9, 1, 3),
    _ZhoneOltTrafficContainerMaximumBW_Type()
)
zhoneOltTrafficContainerMaximumBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneOltTrafficContainerMaximumBW.setStatus("current")


class _ZhoneOltTrafficContainerCBR_Type(TruthValue):
    """Custom type zhoneOltTrafficContainerCBR based on TruthValue"""


_ZhoneOltTrafficContainerCBR_Object = MibTableColumn
zhoneOltTrafficContainerCBR = _ZhoneOltTrafficContainerCBR_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 9, 1, 4),
    _ZhoneOltTrafficContainerCBR_Type()
)
zhoneOltTrafficContainerCBR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneOltTrafficContainerCBR.setStatus("current")


class _ZhoneOltTrafficContainerCbrCompensate_Type(TruthValue):
    """Custom type zhoneOltTrafficContainerCbrCompensate based on TruthValue"""


_ZhoneOltTrafficContainerCbrCompensate_Object = MibTableColumn
zhoneOltTrafficContainerCbrCompensate = _ZhoneOltTrafficContainerCbrCompensate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 9, 1, 5),
    _ZhoneOltTrafficContainerCbrCompensate_Type()
)
zhoneOltTrafficContainerCbrCompensate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneOltTrafficContainerCbrCompensate.setStatus("current")
_ZhoneOltTrafficContainerRowStatus_Type = ZhoneRowStatus
_ZhoneOltTrafficContainerRowStatus_Object = MibTableColumn
zhoneOltTrafficContainerRowStatus = _ZhoneOltTrafficContainerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 1, 9, 1, 6),
    _ZhoneOltTrafficContainerRowStatus_Type()
)
zhoneOltTrafficContainerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneOltTrafficContainerRowStatus.setStatus("current")
_ZhoneAponTraps_ObjectIdentity = ObjectIdentity
zhoneAponTraps = _ZhoneAponTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 3)
)
if mibBuilder.loadTexts:
    zhoneAponTraps.setStatus("current")
_ZhoneAPONV2Traps_ObjectIdentity = ObjectIdentity
zhoneAPONV2Traps = _ZhoneAPONV2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 3, 0)
)
if mibBuilder.loadTexts:
    zhoneAPONV2Traps.setStatus("current")

# Managed Objects groups

zhoneAponOltConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 2)
)
zhoneAponOltConfigGroup.setObjects(
      *(("ZhoneAPON-MIB", "zhoneOltConfigCellScrambling"),
        ("ZhoneAPON-MIB", "zhoneOltConfigBip8"),
        ("ZhoneAPON-MIB", "zhoneOltConfigHec"),
        ("ZhoneAPON-MIB", "zhoneOltConfigHecRxBypass"),
        ("ZhoneAPON-MIB", "zhoneOltConfigCrcRx"),
        ("ZhoneAPON-MIB", "zhoneOltConfigOverheadSize"),
        ("ZhoneAPON-MIB", "zhoneOltConfigDelimiterPattern"),
        ("ZhoneAPON-MIB", "zhoneOltConfigDelimiterSize"),
        ("ZhoneAPON-MIB", "zhoneOltConfigCdrPattern"),
        ("ZhoneAPON-MIB", "zhoneOltConfigCdrLocation"),
        ("ZhoneAPON-MIB", "zhoneOltConfigCdrActiveHigh"),
        ("ZhoneAPON-MIB", "zhoneOltConfigCpeLimit"),
        ("ZhoneAPON-MIB", "zhoneOltConfigLcdLimit"),
        ("ZhoneAPON-MIB", "zhoneOltConfigLcdAlpha"),
        ("ZhoneAPON-MIB", "zhoneOltConfigLcdDelta"),
        ("ZhoneAPON-MIB", "zhoneOltConfigTxDiscardNonMatchingVpi"),
        ("ZhoneAPON-MIB", "zhoneOltConfigUtopiaDiscard"),
        ("ZhoneAPON-MIB", "zhoneOltConfigLineStatusChangeTrapEnable"),
        ("ZhoneAPON-MIB", "zhoneOltConfigLoopback"),
        ("ZhoneAPON-MIB", "zhoneOltConfigAutoLearn"),
        ("ZhoneAPON-MIB", "zhoneOltConfigSyncBytesClkDivisor"),
        ("ZhoneAPON-MIB", "zhoneOltConfigTxSyncBytes"),
        ("ZhoneAPON-MIB", "zhoneOltConfigMaxPonDistance"))
)
if mibBuilder.loadTexts:
    zhoneAponOltConfigGroup.setStatus("current")

zhoneAponOltStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 3)
)
zhoneAponOltStatusGroup.setObjects(
      *(("ZhoneAPON-MIB", "zhoneOltStatusState"),
        ("ZhoneAPON-MIB", "zhoneOltStatusLoopback"),
        ("ZhoneAPON-MIB", "zhoneOltStatusPonAlarmLPHY"),
        ("ZhoneAPON-MIB", "zhoneOltStatusPonAlarmTF"),
        ("ZhoneAPON-MIB", "zhoneOltStatusPonAlarmSUF"),
        ("ZhoneAPON-MIB", "zhoneOltStatusPonAlarmPEE"),
        ("ZhoneAPON-MIB", "zhoneOltStatusPonAlarmLCD"),
        ("ZhoneAPON-MIB", "zhoneOltStatusPonAlarmLOS"),
        ("ZhoneAPON-MIB", "zhoneOltStatusPonAlarmOAML"),
        ("ZhoneAPON-MIB", "zhoneOltStatusPonAlarmCPE"),
        ("ZhoneAPON-MIB", "zhoneOltStatusLastChange"))
)
if mibBuilder.loadTexts:
    zhoneAponOltStatusGroup.setStatus("current")

zhoneAponOltOnuConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 4)
)
zhoneAponOltOnuConfigGroup.setObjects(
      *(("ZhoneAPON-MIB", "zhoneOltOnuConfigPassword"),
        ("ZhoneAPON-MIB", "zhoneOltOnuConfigSerialNum"),
        ("ZhoneAPON-MIB", "zhoneOltOnuConfigChurnkey"),
        ("ZhoneAPON-MIB", "zhoneOltOnuConfigLineStatusChangeTrapEnable"))
)
if mibBuilder.loadTexts:
    zhoneAponOltOnuConfigGroup.setStatus("current")

zhoneAponOltOnuStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 5)
)
zhoneAponOltOnuStatusGroup.setObjects(
      *(("ZhoneAPON-MIB", "zhoneOltOnuStatusPonAlarmLOA"),
        ("ZhoneAPON-MIB", "zhoneOltOnuStatusPonAlarmERR"),
        ("ZhoneAPON-MIB", "zhoneOltOnuStatusPonAlarmSD"),
        ("ZhoneAPON-MIB", "zhoneOltOnuStatusPonAlarmREI"),
        ("ZhoneAPON-MIB", "zhoneOltOnuStatusPonAlarmMEM"),
        ("ZhoneAPON-MIB", "zhoneOltOnuStatusPonAlarmRXINH"))
)
if mibBuilder.loadTexts:
    zhoneAponOltOnuStatusGroup.setStatus("current")

zhoneAponOnuConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 6)
)
zhoneAponOnuConfigGroup.setObjects(
      *(("ZhoneAPON-MIB", "zhoneOnuConfigSerialNumber"),
        ("ZhoneAPON-MIB", "zhoneOnuConfigPassword"),
        ("ZhoneAPON-MIB", "zhoneOnuConfigNetworkRefClk"),
        ("ZhoneAPON-MIB", "zhoneOnuConfigHEC"),
        ("ZhoneAPON-MIB", "zhoneOnuConfigLoopback"),
        ("ZhoneAPON-MIB", "zhoneOnuConfigOverheadSize"))
)
if mibBuilder.loadTexts:
    zhoneAponOnuConfigGroup.setStatus("current")

zhoneAponOnuStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 7)
)
zhoneAponOnuStatusGroup.setObjects(
      *(("ZhoneAPON-MIB", "zhoneOnuStatusLoopback"),
        ("ZhoneAPON-MIB", "zhoneOnuStatusAlarmTF"),
        ("ZhoneAPON-MIB", "zhoneOnuStatusAlarmLOS"),
        ("ZhoneAPON-MIB", "zhoneOnuStatusAlarmPEE"),
        ("ZhoneAPON-MIB", "zhoneOnuStatusAlarmSUF"),
        ("ZhoneAPON-MIB", "zhoneOnuStatusAlarmOAML"),
        ("ZhoneAPON-MIB", "zhoneOnuStatusAlarmLCD"),
        ("ZhoneAPON-MIB", "zhoneOnuStatusAlarmFRML"),
        ("ZhoneAPON-MIB", "zhoneOnuStatusAlarmERR"),
        ("ZhoneAPON-MIB", "zhoneOnuStatusAlarmSD"),
        ("ZhoneAPON-MIB", "zhoneOnuStatusAlarmMEM"),
        ("ZhoneAPON-MIB", "zhoneOnuStatusAlarmDACT"),
        ("ZhoneAPON-MIB", "zhoneOnuStatusAlarmDIS"),
        ("ZhoneAPON-MIB", "zhoneOnuStatusAlarmMIS"),
        ("ZhoneAPON-MIB", "zhoneOnuStatusOperStatus"))
)
if mibBuilder.loadTexts:
    zhoneAponOnuStatusGroup.setStatus("current")

zhoneAponOltTrafficContainerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 8)
)
zhoneAponOltTrafficContainerGroup.setObjects(
      *(("ZhoneAPON-MIB", "zhoneOltTrafficContainerMaximumBW"),
        ("ZhoneAPON-MIB", "zhoneOltTrafficContainerCBR"),
        ("ZhoneAPON-MIB", "zhoneOltTrafficContainerIndexNext"),
        ("ZhoneAPON-MIB", "zhoneOltTrafficContainerCbrCompensate"),
        ("ZhoneAPON-MIB", "zhoneOltTrafficContainerRowStatus"),
        ("ZhoneAPON-MIB", "zhoneOltTrafficContainerGuaranteedBW"))
)
if mibBuilder.loadTexts:
    zhoneAponOltTrafficContainerGroup.setStatus("current")


# Notification objects

zhoneOltLineStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 3, 0, 1)
)
zhoneOltLineStatusChangeTrap.setObjects(
      *(("ZhoneAPON-MIB", "zhoneOltStatusLastChange"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    zhoneOltLineStatusChangeTrap.setStatus(
        "current"
    )

zhoneOnuLineStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 12, 3, 0, 2)
)
zhoneOnuLineStatusChangeTrap.setObjects(
      *(("ZhoneAPON-MIB", "zhoneOnuStatusLastChange"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    zhoneOnuLineStatusChangeTrap.setStatus(
        "current"
    )


# Notifications groups

zhoneAponTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 9)
)
zhoneAponTrapsGroup.setObjects(
    ("ZhoneAPON-MIB", "zhoneOltLineStatusChangeTrap")
)
if mibBuilder.loadTexts:
    zhoneAponTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZhoneAPON-MIB",
    **{"zhoneApon": zhoneApon,
       "zhoneAponMIB": zhoneAponMIB,
       "zhoneOltConfigTable": zhoneOltConfigTable,
       "zhoneOltConfigEntry": zhoneOltConfigEntry,
       "zhoneOltConfigAutoLearn": zhoneOltConfigAutoLearn,
       "zhoneOltConfigCellScrambling": zhoneOltConfigCellScrambling,
       "zhoneOltConfigBip8": zhoneOltConfigBip8,
       "zhoneOltConfigHec": zhoneOltConfigHec,
       "zhoneOltConfigHecRxBypass": zhoneOltConfigHecRxBypass,
       "zhoneOltConfigCrcRx": zhoneOltConfigCrcRx,
       "zhoneOltConfigOverheadSize": zhoneOltConfigOverheadSize,
       "zhoneOltConfigDelimiterPattern": zhoneOltConfigDelimiterPattern,
       "zhoneOltConfigDelimiterSize": zhoneOltConfigDelimiterSize,
       "zhoneOltConfigCdrPattern": zhoneOltConfigCdrPattern,
       "zhoneOltConfigCdrLocation": zhoneOltConfigCdrLocation,
       "zhoneOltConfigCdrActiveHigh": zhoneOltConfigCdrActiveHigh,
       "zhoneOltConfigCpeLimit": zhoneOltConfigCpeLimit,
       "zhoneOltConfigLcdLimit": zhoneOltConfigLcdLimit,
       "zhoneOltConfigLcdAlpha": zhoneOltConfigLcdAlpha,
       "zhoneOltConfigLcdDelta": zhoneOltConfigLcdDelta,
       "zhoneOltConfigTxDiscardNonMatchingVpi": zhoneOltConfigTxDiscardNonMatchingVpi,
       "zhoneOltConfigUtopiaDiscard": zhoneOltConfigUtopiaDiscard,
       "zhoneOltConfigSyncBytesClkDivisor": zhoneOltConfigSyncBytesClkDivisor,
       "zhoneOltConfigTxSyncBytes": zhoneOltConfigTxSyncBytes,
       "zhoneOltConfigLoopback": zhoneOltConfigLoopback,
       "zhoneOltConfigMaxPonDistance": zhoneOltConfigMaxPonDistance,
       "zhoneOltConfigLineStatusChangeTrapEnable": zhoneOltConfigLineStatusChangeTrapEnable,
       "zhoneOltStatusTable": zhoneOltStatusTable,
       "zhoneOltStatusEntry": zhoneOltStatusEntry,
       "zhoneOltStatusState": zhoneOltStatusState,
       "zhoneOltStatusLoopback": zhoneOltStatusLoopback,
       "zhoneOltStatusPonAlarmLPHY": zhoneOltStatusPonAlarmLPHY,
       "zhoneOltStatusPonAlarmTF": zhoneOltStatusPonAlarmTF,
       "zhoneOltStatusPonAlarmSUF": zhoneOltStatusPonAlarmSUF,
       "zhoneOltStatusPonAlarmPEE": zhoneOltStatusPonAlarmPEE,
       "zhoneOltStatusPonAlarmLCD": zhoneOltStatusPonAlarmLCD,
       "zhoneOltStatusPonAlarmLOS": zhoneOltStatusPonAlarmLOS,
       "zhoneOltStatusPonAlarmOAML": zhoneOltStatusPonAlarmOAML,
       "zhoneOltStatusPonAlarmCPE": zhoneOltStatusPonAlarmCPE,
       "zhoneOltStatusLastChange": zhoneOltStatusLastChange,
       "zhoneOltOnuConfigTable": zhoneOltOnuConfigTable,
       "zhoneOltOnuConfigEntry": zhoneOltOnuConfigEntry,
       "zhoneOltOnuConfigPassword": zhoneOltOnuConfigPassword,
       "zhoneOltOnuConfigSerialNum": zhoneOltOnuConfigSerialNum,
       "zhoneOltOnuConfigChurnkey": zhoneOltOnuConfigChurnkey,
       "zhoneOltOnuConfigLineStatusChangeTrapEnable": zhoneOltOnuConfigLineStatusChangeTrapEnable,
       "zhoneOltOnuStatusTable": zhoneOltOnuStatusTable,
       "zhoneOltOnuStatusEntry": zhoneOltOnuStatusEntry,
       "zhoneOltOnuStatusPonAlarmLOA": zhoneOltOnuStatusPonAlarmLOA,
       "zhoneOltOnuStatusPonAlarmERR": zhoneOltOnuStatusPonAlarmERR,
       "zhoneOltOnuStatusPonAlarmSD": zhoneOltOnuStatusPonAlarmSD,
       "zhoneOltOnuStatusPonAlarmREI": zhoneOltOnuStatusPonAlarmREI,
       "zhoneOltOnuStatusPonAlarmMEM": zhoneOltOnuStatusPonAlarmMEM,
       "zhoneOltOnuStatusPonAlarmRXINH": zhoneOltOnuStatusPonAlarmRXINH,
       "zhoneOltOnuStatusPonAlarmLOS": zhoneOltOnuStatusPonAlarmLOS,
       "zhoneOltOnuStatusPonAlarmPEE": zhoneOltOnuStatusPonAlarmPEE,
       "zhoneOltOnuStatusPonAlarmSUF": zhoneOltOnuStatusPonAlarmSUF,
       "zhoneOltOnuStatusPonAlarmOAML": zhoneOltOnuStatusPonAlarmOAML,
       "zhoneOltOnuStatusPonAlarmLCD": zhoneOltOnuStatusPonAlarmLCD,
       "zhoneOnuConfigTable": zhoneOnuConfigTable,
       "zhoneOnuConfigEntry": zhoneOnuConfigEntry,
       "zhoneOnuConfigSerialNumber": zhoneOnuConfigSerialNumber,
       "zhoneOnuConfigPassword": zhoneOnuConfigPassword,
       "zhoneOnuConfigNetworkRefClk": zhoneOnuConfigNetworkRefClk,
       "zhoneOnuConfigHEC": zhoneOnuConfigHEC,
       "zhoneOnuConfigLoopback": zhoneOnuConfigLoopback,
       "zhoneOnuConfigOverheadSize": zhoneOnuConfigOverheadSize,
       "zhoneOnuConfigRfVideo": zhoneOnuConfigRfVideo,
       "zhoneOnuStatusTable": zhoneOnuStatusTable,
       "zhoneOnuStatusEntry": zhoneOnuStatusEntry,
       "zhoneOnuStatusOperStatus": zhoneOnuStatusOperStatus,
       "zhoneOnuStatusLoopback": zhoneOnuStatusLoopback,
       "zhoneOnuStatusAlarmTF": zhoneOnuStatusAlarmTF,
       "zhoneOnuStatusAlarmLOS": zhoneOnuStatusAlarmLOS,
       "zhoneOnuStatusAlarmPEE": zhoneOnuStatusAlarmPEE,
       "zhoneOnuStatusAlarmSUF": zhoneOnuStatusAlarmSUF,
       "zhoneOnuStatusAlarmOAML": zhoneOnuStatusAlarmOAML,
       "zhoneOnuStatusAlarmLCD": zhoneOnuStatusAlarmLCD,
       "zhoneOnuStatusAlarmFRML": zhoneOnuStatusAlarmFRML,
       "zhoneOnuStatusAlarmERR": zhoneOnuStatusAlarmERR,
       "zhoneOnuStatusAlarmSD": zhoneOnuStatusAlarmSD,
       "zhoneOnuStatusAlarmMEM": zhoneOnuStatusAlarmMEM,
       "zhoneOnuStatusAlarmDACT": zhoneOnuStatusAlarmDACT,
       "zhoneOnuStatusAlarmDIS": zhoneOnuStatusAlarmDIS,
       "zhoneOnuStatusAlarmMIS": zhoneOnuStatusAlarmMIS,
       "zhoneOnuStatusLastChange": zhoneOnuStatusLastChange,
       "zhoneOltTrafficContainerIndexNext": zhoneOltTrafficContainerIndexNext,
       "zhoneOltTrafficContainerTable": zhoneOltTrafficContainerTable,
       "zhoneOltTrafficContainerEntry": zhoneOltTrafficContainerEntry,
       "zhoneOltTrafficContainerIndex": zhoneOltTrafficContainerIndex,
       "zhoneOltTrafficContainerGuaranteedBW": zhoneOltTrafficContainerGuaranteedBW,
       "zhoneOltTrafficContainerMaximumBW": zhoneOltTrafficContainerMaximumBW,
       "zhoneOltTrafficContainerCBR": zhoneOltTrafficContainerCBR,
       "zhoneOltTrafficContainerCbrCompensate": zhoneOltTrafficContainerCbrCompensate,
       "zhoneOltTrafficContainerRowStatus": zhoneOltTrafficContainerRowStatus,
       "zhoneAponTraps": zhoneAponTraps,
       "zhoneAPONV2Traps": zhoneAPONV2Traps,
       "zhoneOltLineStatusChangeTrap": zhoneOltLineStatusChangeTrap,
       "zhoneOnuLineStatusChangeTrap": zhoneOnuLineStatusChangeTrap,
       "zhoneAponOltConfigGroup": zhoneAponOltConfigGroup,
       "zhoneAponOltStatusGroup": zhoneAponOltStatusGroup,
       "zhoneAponOltOnuConfigGroup": zhoneAponOltOnuConfigGroup,
       "zhoneAponOltOnuStatusGroup": zhoneAponOltOnuStatusGroup,
       "zhoneAponOnuConfigGroup": zhoneAponOnuConfigGroup,
       "zhoneAponOnuStatusGroup": zhoneAponOnuStatusGroup,
       "zhoneAponOltTrafficContainerGroup": zhoneAponOltTrafficContainerGroup,
       "zhoneAponTrapsGroup": zhoneAponTrapsGroup}
)
