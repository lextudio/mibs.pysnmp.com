# SNMP MIB module (SYMBOL-AP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYMBOL-AP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:36 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TestAndIncr,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TestAndIncr",
    "TruthValue")

(cc802dt1xPortAuthLogin,
 cc802dt1xPortAuthPass,
 cc802dt1xPortAuthSetAp300,
 ccMuAuthenticationMethod,
 ccMuEncryptionMethod,
 ccMuIpAddr,
 ccMuIsDataReady,
 ccMuLastActivity,
 ccMuLastMac,
 ccMuLastPortal,
 ccMuLastReason,
 ccMuMac,
 ccMuMeshMode,
 ccMuPortalIndex,
 ccMuPortalMac,
 ccMuPowerMode,
 ccMuRadioType,
 ccMuRxOctetsAt11Mb,
 ccMuRxOctetsAt12Mb,
 ccMuRxOctetsAt18Mb,
 ccMuRxOctetsAt1Mb,
 ccMuRxOctetsAt22Mb,
 ccMuRxOctetsAt24Mb,
 ccMuRxOctetsAt2Mb,
 ccMuRxOctetsAt36Mb,
 ccMuRxOctetsAt48Mb,
 ccMuRxOctetsAt54Mb,
 ccMuRxOctetsAt5pt5Mb,
 ccMuRxOctetsAt6Mb,
 ccMuRxOctetsAt9Mb,
 ccMuRxOctetsNUcast,
 ccMuRxOctetsUcast,
 ccMuRxPktsAt11Mb,
 ccMuRxPktsAt12Mb,
 ccMuRxPktsAt18Mb,
 ccMuRxPktsAt1Mb,
 ccMuRxPktsAt22Mb,
 ccMuRxPktsAt24Mb,
 ccMuRxPktsAt2Mb,
 ccMuRxPktsAt36Mb,
 ccMuRxPktsAt48Mb,
 ccMuRxPktsAt54Mb,
 ccMuRxPktsAt5pt5Mb,
 ccMuRxPktsAt6Mb,
 ccMuRxPktsAt9Mb,
 ccMuRxPktsNUcast,
 ccMuRxPktsUcast,
 ccMuRxRssiMostRecent,
 ccMuRxRssiNumPkts,
 ccMuRxRssiSum,
 ccMuRxRssiSumSquares,
 ccMuRxUndecryptablePkts,
 ccMuSigStatsNoiseBest,
 ccMuSigStatsNoiseMostRecent,
 ccMuSigStatsNoiseSum,
 ccMuSigStatsNoiseSumSquares,
 ccMuSigStatsNoiseWorst,
 ccMuSigStatsNumPkts,
 ccMuSigStatsSignalBest,
 ccMuSigStatsSignalMostRecent,
 ccMuSigStatsSignalSum,
 ccMuSigStatsSignalSumSquares,
 ccMuSigStatsSignalWorst,
 ccMuSigStatsSnrBest,
 ccMuSigStatsSnrMostRecent,
 ccMuSigStatsSnrSum,
 ccMuSigStatsSnrSumSquares,
 ccMuSigStatsSnrWorst,
 ccMuSumStatsLongAvgBitSpeed,
 ccMuSumStatsLongAvgMuNoise,
 ccMuSumStatsLongAvgMuSignal,
 ccMuSumStatsLongAvgMuSnr,
 ccMuSumStatsLongNumPkts,
 ccMuSumStatsLongPktsPerSec100,
 ccMuSumStatsLongPktsPerSecRx100,
 ccMuSumStatsLongPktsPerSecTx100,
 ccMuSumStatsLongPp10kDropped,
 ccMuSumStatsLongPp10kNUcastPkts,
 ccMuSumStatsLongPp10kRxUndecrypt,
 ccMuSumStatsLongPp10kTxWithRetries,
 ccMuSumStatsLongThroughput,
 ccMuSumStatsLongThroughputRx,
 ccMuSumStatsLongThroughputTx,
 ccMuSumStatsLongTimestamp,
 ccMuSumStatsLongTxAvgRetries100,
 ccMuSumStatsShortAvgBitSpeed,
 ccMuSumStatsShortAvgMuNoise,
 ccMuSumStatsShortAvgMuSignal,
 ccMuSumStatsShortAvgMuSnr,
 ccMuSumStatsShortNumPkts,
 ccMuSumStatsShortPktsPerSec100,
 ccMuSumStatsShortPktsPerSecRx100,
 ccMuSumStatsShortPktsPerSecTx100,
 ccMuSumStatsShortPp10kDropped,
 ccMuSumStatsShortPp10kNUcastPkts,
 ccMuSumStatsShortPp10kRxUndecrypt,
 ccMuSumStatsShortPp10kTxWithRetries,
 ccMuSumStatsShortThroughput,
 ccMuSumStatsShortThroughputRx,
 ccMuSumStatsShortThroughputTx,
 ccMuSumStatsShortTimestamp,
 ccMuSumStatsShortTxAvgRetries100,
 ccMuSupportedRates,
 ccMuSymbolRogueApEna,
 ccMuTxOctetsAt11Mb,
 ccMuTxOctetsAt12Mb,
 ccMuTxOctetsAt18Mb,
 ccMuTxOctetsAt1Mb,
 ccMuTxOctetsAt22Mb,
 ccMuTxOctetsAt24Mb,
 ccMuTxOctetsAt2Mb,
 ccMuTxOctetsAt36Mb,
 ccMuTxOctetsAt48Mb,
 ccMuTxOctetsAt54Mb,
 ccMuTxOctetsAt5pt5Mb,
 ccMuTxOctetsAt6Mb,
 ccMuTxOctetsAt9Mb,
 ccMuTxOctetsUcast,
 ccMuTxPktsAt11Mb,
 ccMuTxPktsAt12Mb,
 ccMuTxPktsAt18Mb,
 ccMuTxPktsAt1Mb,
 ccMuTxPktsAt22Mb,
 ccMuTxPktsAt24Mb,
 ccMuTxPktsAt2Mb,
 ccMuTxPktsAt36Mb,
 ccMuTxPktsAt48Mb,
 ccMuTxPktsAt54Mb,
 ccMuTxPktsAt5pt5Mb,
 ccMuTxPktsAt6Mb,
 ccMuTxPktsAt9Mb,
 ccMuTxPktsUcast,
 ccMuTxRetries01,
 ccMuTxRetries02,
 ccMuTxRetries03,
 ccMuTxRetries04,
 ccMuTxRetries05,
 ccMuTxRetries06,
 ccMuTxRetries07,
 ccMuTxRetries08,
 ccMuTxRetries09,
 ccMuTxRetries10,
 ccMuTxRetries11,
 ccMuTxRetries12,
 ccMuTxRetries13,
 ccMuTxRetries14,
 ccMuTxRetries15,
 ccMuTxRetriesFailed,
 ccMuTxRetriesMostRecent,
 ccMuTxRetriesNone,
 ccMuTxRetriesOctets01,
 ccMuTxRetriesOctets02,
 ccMuTxRetriesOctets03,
 ccMuTxRetriesOctets04,
 ccMuTxRetriesOctets05,
 ccMuTxRetriesOctets06,
 ccMuTxRetriesOctets07,
 ccMuTxRetriesOctets08,
 ccMuTxRetriesOctets09,
 ccMuTxRetriesOctets10,
 ccMuTxRetriesOctets11,
 ccMuTxRetriesOctets12,
 ccMuTxRetriesOctets13,
 ccMuTxRetriesOctets14,
 ccMuTxRetriesOctets15,
 ccMuTxRetriesOctetsFailed,
 ccMuTxRetriesOctetsNone,
 ccMuTxRetriesTotal,
 ccMuType,
 ccMuVlanId,
 ccMuWlanIndex,
 ccMuWlanName,
 ccPortalAdoptionEndMac,
 ccPortalAdoptionIndex,
 ccPortalAdoptionRowStatus,
 ccPortalAdoptionStartMac,
 ccPortalAdoptionWlanPointers,
 ccPortalAssociatedMus,
 ccPortalBackgroundNoiseBest,
 ccPortalBackgroundNoiseNumSamples,
 ccPortalBackgroundNoiseSum,
 ccPortalBackgroundNoiseSumSquares,
 ccPortalBackgroundNoiseWorst,
 ccPortalCfgRadioChannel,
 ccPortalCfgRadioChannelMode,
 ccPortalCfgRadioDefaultChannel,
 ccPortalCfgRadioDefaultChannelMode,
 ccPortalCfgRadioDefaultDesChannel,
 ccPortalCfgRadioDefaultDesPlacement,
 ccPortalCfgRadioDefaultDesPowerInMW,
 ccPortalCfgRadioDefaultDesPowerLevel,
 ccPortalCfgRadioDefaultPlacement,
 ccPortalCfgRadioDefaultPosChannel,
 ccPortalCfgRadioDefaultPosPowerLevel,
 ccPortalCfgRadioDefaultPowerInMW,
 ccPortalCfgRadioDefaultPowerLevel,
 ccPortalCfgRadioDefaultReset,
 ccPortalCfgRadioDefaultSet,
 ccPortalCfgRadioDesChannel,
 ccPortalCfgRadioDesPlacement,
 ccPortalCfgRadioDesPowerInMW,
 ccPortalCfgRadioDesPowerLevel,
 ccPortalCfgRadioPlacement,
 ccPortalCfgRadioPosChannel,
 ccPortalCfgRadioPosPowerLevel,
 ccPortalCfgRadioPowerInMW,
 ccPortalCfgRadioPowerLevel,
 ccPortalCfgRadioRemapChannel,
 ccPortalCfgRadioReset,
 ccPortalCfgRadioSet,
 ccPortalChannel,
 ccPortalIndex,
 ccPortalIpAddress,
 ccPortalLastActivity,
 ccPortalLastAdoption,
 ccPortalLastMac,
 ccPortalLastReason,
 ccPortalLegacyMode,
 ccPortalLocation,
 ccPortalMac,
 ccPortalMeshAvailableBaseChannel,
 ccPortalMeshAvailableBaseMac,
 ccPortalMeshAvailableBaseRssi,
 ccPortalMeshPreferredBaseMac,
 ccPortalMeshPreferredBaseRowStatus,
 ccPortalModeLegacy,
 ccPortalName,
 ccPortalNumberOfBss,
 ccPortalNumberOfEss,
 ccPortalOptions,
 ccPortalPointerToAp,
 ccPortalPointersToWlans,
 ccPortalRadioRemapChannel,
 ccPortalRadioType,
 ccPortalRxOctetsAt11Mb,
 ccPortalRxOctetsAt12Mb,
 ccPortalRxOctetsAt18Mb,
 ccPortalRxOctetsAt1Mb,
 ccPortalRxOctetsAt22Mb,
 ccPortalRxOctetsAt24Mb,
 ccPortalRxOctetsAt2Mb,
 ccPortalRxOctetsAt36Mb,
 ccPortalRxOctetsAt48Mb,
 ccPortalRxOctetsAt54Mb,
 ccPortalRxOctetsAt5pt5Mb,
 ccPortalRxOctetsAt6Mb,
 ccPortalRxOctetsAt9Mb,
 ccPortalRxOctetsNUcast,
 ccPortalRxOctetsUcast,
 ccPortalRxPktsAt11Mb,
 ccPortalRxPktsAt12Mb,
 ccPortalRxPktsAt18Mb,
 ccPortalRxPktsAt1Mb,
 ccPortalRxPktsAt22Mb,
 ccPortalRxPktsAt24Mb,
 ccPortalRxPktsAt2Mb,
 ccPortalRxPktsAt36Mb,
 ccPortalRxPktsAt48Mb,
 ccPortalRxPktsAt54Mb,
 ccPortalRxPktsAt5pt5Mb,
 ccPortalRxPktsAt6Mb,
 ccPortalRxPktsAt9Mb,
 ccPortalRxPktsNUcast,
 ccPortalRxPktsUcast,
 ccPortalRxUndecryptablePkts,
 ccPortalSIPCacMode,
 ccPortalSettingsAdoptedWlan,
 ccPortalSettingsAntenna,
 ccPortalSettingsBGMode,
 ccPortalSettingsBasicRates,
 ccPortalSettingsBeaconInt,
 ccPortalSettingsDefaultAntenna,
 ccPortalSettingsDefaultBGMode,
 ccPortalSettingsDefaultBasicRates,
 ccPortalSettingsDefaultBeaconInt,
 ccPortalSettingsDefaultDtimPrd,
 ccPortalSettingsDefaultDtimPrd2,
 ccPortalSettingsDefaultDtimPrd3,
 ccPortalSettingsDefaultDtimPrd4,
 ccPortalSettingsDefaultIndex,
 ccPortalSettingsDefaultPriWlan,
 ccPortalSettingsDefaultRtsThresh,
 ccPortalSettingsDefaultSecBeacon,
 ccPortalSettingsDefaultShortPreamble,
 ccPortalSettingsDefaultSupportedRates,
 ccPortalSettingsDefaultUniSpread,
 ccPortalSettingsDetector,
 ccPortalSettingsDtimPrd,
 ccPortalSettingsDtimPrd2,
 ccPortalSettingsDtimPrd3,
 ccPortalSettingsDtimPrd4,
 ccPortalSettingsLocation,
 ccPortalSettingsMeshAutoBaseSelection,
 ccPortalSettingsMeshBaseChannel,
 ccPortalSettingsMeshBaseEnable,
 ccPortalSettingsMeshClientEnable,
 ccPortalSettingsMeshClientWlanIndex,
 ccPortalSettingsMeshMaxClients,
 ccPortalSettingsName,
 ccPortalSettingsPriWlan,
 ccPortalSettingsRevertAp,
 ccPortalSettingsRtsThresh,
 ccPortalSettingsSecBeacon,
 ccPortalSettingsShortPreamble,
 ccPortalSettingsSipActiveSessCnt,
 ccPortalSettingsSipAllowedSessCnt,
 ccPortalSettingsSipInActiveSessCnt,
 ccPortalSettingsSipRoamedSessCnt,
 ccPortalSettingsSupportedRates,
 ccPortalSettingsUniSpread,
 ccPortalSettingsWMEProfile,
 ccPortalSigStatsNoiseBest,
 ccPortalSigStatsNoiseMostRecent,
 ccPortalSigStatsNoiseSum,
 ccPortalSigStatsNoiseSumSquares,
 ccPortalSigStatsNoiseWorst,
 ccPortalSigStatsNumPkts,
 ccPortalSigStatsSignalBest,
 ccPortalSigStatsSignalMostRecent,
 ccPortalSigStatsSignalSum,
 ccPortalSigStatsSignalSumSquares,
 ccPortalSigStatsSignalWorst,
 ccPortalSigStatsSnrBest,
 ccPortalSigStatsSnrMostRecent,
 ccPortalSigStatsSnrSum,
 ccPortalSigStatsSnrSumSquares,
 ccPortalSigStatsSnrWorst,
 ccPortalState,
 ccPortalSumStatsLongAvgBitSpeed,
 ccPortalSumStatsLongAvgMuNoise,
 ccPortalSumStatsLongAvgMuSignal,
 ccPortalSumStatsLongAvgMuSnr,
 ccPortalSumStatsLongNumPkts,
 ccPortalSumStatsLongPktsPerSec100,
 ccPortalSumStatsLongPktsPerSecRx100,
 ccPortalSumStatsLongPktsPerSecTx100,
 ccPortalSumStatsLongPp10kDropped,
 ccPortalSumStatsLongPp10kNUcastPkts,
 ccPortalSumStatsLongPp10kRfUtil,
 ccPortalSumStatsLongPp10kRxUndecrypt,
 ccPortalSumStatsLongPp10kTxMaxRetries,
 ccPortalSumStatsLongPp10kTxWithRetries,
 ccPortalSumStatsLongThroughput,
 ccPortalSumStatsLongThroughputRx,
 ccPortalSumStatsLongThroughputTx,
 ccPortalSumStatsLongTimestamp,
 ccPortalSumStatsLongTotalMus,
 ccPortalSumStatsLongTxAvgRetries100,
 ccPortalSumStatsShortAvgBitSpeed,
 ccPortalSumStatsShortAvgMuNoise,
 ccPortalSumStatsShortAvgMuSignal,
 ccPortalSumStatsShortAvgMuSnr,
 ccPortalSumStatsShortNumPkts,
 ccPortalSumStatsShortPktsPerSec100,
 ccPortalSumStatsShortPktsPerSecRx100,
 ccPortalSumStatsShortPktsPerSecTx100,
 ccPortalSumStatsShortPp10kDropped,
 ccPortalSumStatsShortPp10kNUcastPkts,
 ccPortalSumStatsShortPp10kRfUtil,
 ccPortalSumStatsShortPp10kRxUndecrypt,
 ccPortalSumStatsShortPp10kTxMaxRetries,
 ccPortalSumStatsShortPp10kTxWithRetries,
 ccPortalSumStatsShortThroughput,
 ccPortalSumStatsShortThroughputRx,
 ccPortalSumStatsShortThroughputTx,
 ccPortalSumStatsShortTimestamp,
 ccPortalSumStatsShortTotalMus,
 ccPortalSumStatsShortTxAvgRetries100,
 ccPortalSystemStatsBeaconsTx,
 ccPortalSystemStatsBeaconsTxOctets,
 ccPortalSystemStatsProbeReqRx,
 ccPortalSystemStatsProbeReqRxOctets,
 ccPortalSystemStatsProbeRespRetries1,
 ccPortalSystemStatsProbeRespRetries2,
 ccPortalSystemStatsProbeRespRetries3OrMore,
 ccPortalSystemStatsProbeRespRetriesFailed,
 ccPortalSystemStatsProbeRespRetriesNone,
 ccPortalSystemStatsProbeRespTxOctets,
 ccPortalTxOctetsAt11Mb,
 ccPortalTxOctetsAt12Mb,
 ccPortalTxOctetsAt18Mb,
 ccPortalTxOctetsAt1Mb,
 ccPortalTxOctetsAt22Mb,
 ccPortalTxOctetsAt24Mb,
 ccPortalTxOctetsAt2Mb,
 ccPortalTxOctetsAt36Mb,
 ccPortalTxOctetsAt48Mb,
 ccPortalTxOctetsAt54Mb,
 ccPortalTxOctetsAt5pt5Mb,
 ccPortalTxOctetsAt6Mb,
 ccPortalTxOctetsAt9Mb,
 ccPortalTxOctetsUcast,
 ccPortalTxPktsAt11Mb,
 ccPortalTxPktsAt12Mb,
 ccPortalTxPktsAt18Mb,
 ccPortalTxPktsAt1Mb,
 ccPortalTxPktsAt22Mb,
 ccPortalTxPktsAt24Mb,
 ccPortalTxPktsAt2Mb,
 ccPortalTxPktsAt36Mb,
 ccPortalTxPktsAt48Mb,
 ccPortalTxPktsAt54Mb,
 ccPortalTxPktsAt5pt5Mb,
 ccPortalTxPktsAt6Mb,
 ccPortalTxPktsAt9Mb,
 ccPortalTxPktsUcast,
 ccPortalTxPowerLevel,
 ccPortalTxRetriesOctets01,
 ccPortalTxRetriesOctets02,
 ccPortalTxRetriesOctets03,
 ccPortalTxRetriesOctets04,
 ccPortalTxRetriesOctets05,
 ccPortalTxRetriesOctets06,
 ccPortalTxRetriesOctets07,
 ccPortalTxRetriesOctets08,
 ccPortalTxRetriesOctets09,
 ccPortalTxRetriesOctets10,
 ccPortalTxRetriesOctets11,
 ccPortalTxRetriesOctets12,
 ccPortalTxRetriesOctets13,
 ccPortalTxRetriesOctets14,
 ccPortalTxRetriesOctets15,
 ccPortalTxRetriesOctetsFailed,
 ccPortalTxRetriesOctetsNone,
 ccPortalTxRetriesPkts01,
 ccPortalTxRetriesPkts02,
 ccPortalTxRetriesPkts03,
 ccPortalTxRetriesPkts04,
 ccPortalTxRetriesPkts05,
 ccPortalTxRetriesPkts06,
 ccPortalTxRetriesPkts07,
 ccPortalTxRetriesPkts08,
 ccPortalTxRetriesPkts09,
 ccPortalTxRetriesPkts10,
 ccPortalTxRetriesPkts11,
 ccPortalTxRetriesPkts12,
 ccPortalTxRetriesPkts13,
 ccPortalTxRetriesPkts14,
 ccPortalTxRetriesPkts15,
 ccPortalTxRetriesPktsFailed,
 ccPortalTxRetriesPktsNone,
 ccSubnetEntry,
 ccWanVpnEntry,
 ccWlanAnswerBroadcastEss,
 ccWlanAuthEapMuMaxRetries,
 ccWlanAuthEapMuQuietPeriod,
 ccWlanAuthEapMuTimeout,
 ccWlanAuthEapMuTxPeriod,
 ccWlanAuthEapRadius1Port,
 ccWlanAuthEapRadius1Server,
 ccWlanAuthEapRadius1SharedSecret,
 ccWlanAuthEapRadius2Port,
 ccWlanAuthEapRadius2Server,
 ccWlanAuthEapRadius2SharedSecret,
 ccWlanAuthEapRadiusAcctMode,
 ccWlanAuthEapRadiusAcctMuRetries,
 ccWlanAuthEapRadiusAcctMuTimeout,
 ccWlanAuthEapReauthenticationEnable,
 ccWlanAuthEapReauthenticationMaxRetries,
 ccWlanAuthEapReauthenticationPeriod,
 ccWlanAuthEapServerMaxRetries,
 ccWlanAuthEapServerTimeout,
 ccWlanAuthEapSyslogMode,
 ccWlanAuthEapSyslogSeverIp,
 ccWlanAuthKerberosKdcPort1,
 ccWlanAuthKerberosKdcPort2,
 ccWlanAuthKerberosKdcPortR,
 ccWlanAuthKerberosKdcServerIp1,
 ccWlanAuthKerberosKdcServerIp2,
 ccWlanAuthKerberosKdcServerIpR,
 ccWlanAuthKerberosPassword,
 ccWlanAuthKerberosRealmName,
 ccWlanAuthKerberosUsername,
 ccWlanAuthentication,
 ccWlanBwShareMode,
 ccWlanCryptoKeyguardKey1,
 ccWlanCryptoKeyguardKey2,
 ccWlanCryptoKeyguardKey3,
 ccWlanCryptoKeyguardKey4,
 ccWlanCryptoKeyguardKeyToUse,
 ccWlanCryptoKeyguardPasskey,
 ccWlanCryptoUseWpa2,
 ccWlanCryptoWepKey1,
 ccWlanCryptoWepKey2,
 ccWlanCryptoWepKey3,
 ccWlanCryptoWepKey4,
 ccWlanCryptoWepKeyToUse,
 ccWlanCryptoWepPassKey,
 ccWlanCryptoWpaBcastKeyRotation,
 ccWlanCryptoWpaKey,
 ccWlanCryptoWpaKeyRotationInterval,
 ccWlanCryptoWpaKeyToUse,
 ccWlanCryptoWpaPassphrase,
 ccWlanCryptoWpaTwoAllowTkipClient,
 ccWlanCryptoWpaTwoBcastKeyRotation,
 ccWlanCryptoWpaTwoFastRoamKeyCache,
 ccWlanCryptoWpaTwoFastRoamPreAuth,
 ccWlanCryptoWpaTwoKey,
 ccWlanCryptoWpaTwoKeyRotationInterval,
 ccWlanCryptoWpaTwoKeyToUse,
 ccWlanCryptoWpaTwoPassphrase,
 ccWlanDisallowMuToMu,
 ccWlanEnable,
 ccWlanEncryption,
 ccWlanEssid,
 ccWlanIndex,
 ccWlanLastActivity,
 ccWlanMuAclDefault,
 ccWlanMuAclEndingMac,
 ccWlanMuAclIndex,
 ccWlanMuAclName,
 ccWlanMuAclRowStatus,
 ccWlanMuAclStartingMac,
 ccWlanMuInactivityTimeout,
 ccWlanMulticastAddr1,
 ccWlanMulticastAddr2,
 ccWlanName,
 ccWlanPortalsAdopted,
 ccWlanQosMonitorDropped,
 ccWlanQosMonitorSent,
 ccWlanQosWMEPriorityConversion,
 ccWlanQosWMEProfileBackgroundAifsn,
 ccWlanQosWMEProfileBackgroundECwmax,
 ccWlanQosWMEProfileBackgroundECwmin,
 ccWlanQosWMEProfileBackgroundTxopsTime,
 ccWlanQosWMEProfileBestEffortAifsn,
 ccWlanQosWMEProfileBestEffortECwmax,
 ccWlanQosWMEProfileBestEffortECwmin,
 ccWlanQosWMEProfileBestEffortTxopsTime,
 ccWlanQosWMEProfileIndex,
 ccWlanQosWMEProfileName,
 ccWlanQosWMEProfileRowStatus,
 ccWlanQosWMEProfileVideoAifsn,
 ccWlanQosWMEProfileVideoECwmax,
 ccWlanQosWMEProfileVideoECwmin,
 ccWlanQosWMEProfileVideoTxopsTime,
 ccWlanQosWMEProfileVoiceAifsn,
 ccWlanQosWMEProfileVoiceECwmax,
 ccWlanQosWMEProfileVoiceECwmin,
 ccWlanQosWMEProfileVoiceTxopsTime,
 ccWlanQosWMETrafficAccessCategory,
 ccWlanQosWMETrafficDestIp,
 ccWlanQosWMETrafficDestMask,
 ccWlanQosWMETrafficDestPortEnd,
 ccWlanQosWMETrafficDestPortStart,
 ccWlanQosWMETrafficIndex,
 ccWlanQosWMETrafficRowStatus,
 ccWlanQosWMETrafficSrcIp,
 ccWlanQosWMETrafficSrcMask,
 ccWlanQosWMETrafficSrcPortEnd,
 ccWlanQosWMETrafficSrcPortStart,
 ccWlanQosWMEWlanProfile,
 ccWlanRxOctetsAt11Mb,
 ccWlanRxOctetsAt12Mb,
 ccWlanRxOctetsAt18Mb,
 ccWlanRxOctetsAt1Mb,
 ccWlanRxOctetsAt22Mb,
 ccWlanRxOctetsAt24Mb,
 ccWlanRxOctetsAt2Mb,
 ccWlanRxOctetsAt36Mb,
 ccWlanRxOctetsAt48Mb,
 ccWlanRxOctetsAt54Mb,
 ccWlanRxOctetsAt5pt5Mb,
 ccWlanRxOctetsAt6Mb,
 ccWlanRxOctetsAt9Mb,
 ccWlanRxOctetsNUcast,
 ccWlanRxOctetsUcast,
 ccWlanRxPktsAt11Mb,
 ccWlanRxPktsAt12Mb,
 ccWlanRxPktsAt18Mb,
 ccWlanRxPktsAt1Mb,
 ccWlanRxPktsAt22Mb,
 ccWlanRxPktsAt24Mb,
 ccWlanRxPktsAt2Mb,
 ccWlanRxPktsAt36Mb,
 ccWlanRxPktsAt48Mb,
 ccWlanRxPktsAt54Mb,
 ccWlanRxPktsAt5pt5Mb,
 ccWlanRxPktsAt6Mb,
 ccWlanRxPktsAt9Mb,
 ccWlanRxPktsNUcast,
 ccWlanRxPktsUcast,
 ccWlanRxUndecryptablePkts,
 ccWlanSecBeacon,
 ccWlanSigStatsNoiseBest,
 ccWlanSigStatsNoiseSum,
 ccWlanSigStatsNoiseSumSquares,
 ccWlanSigStatsNoiseWorst,
 ccWlanSigStatsNumPkts,
 ccWlanSigStatsSignalBest,
 ccWlanSigStatsSignalSum,
 ccWlanSigStatsSignalSumSquares,
 ccWlanSigStatsSignalWorst,
 ccWlanSigStatsSnrBest,
 ccWlanSigStatsSnrSum,
 ccWlanSigStatsSnrSumSquares,
 ccWlanSigStatsSnrWorst,
 ccWlanSubnet,
 ccWlanSumStatsLongAvgBitSpeed,
 ccWlanSumStatsLongAvgMuNoise,
 ccWlanSumStatsLongAvgMuSignal,
 ccWlanSumStatsLongAvgMuSnr,
 ccWlanSumStatsLongNumPkts,
 ccWlanSumStatsLongPktsPerSec100,
 ccWlanSumStatsLongPktsPerSecRx100,
 ccWlanSumStatsLongPktsPerSecTx100,
 ccWlanSumStatsLongPp10kDropped,
 ccWlanSumStatsLongPp10kNUcastPkts,
 ccWlanSumStatsLongPp10kRxUndecrypt,
 ccWlanSumStatsLongPp10kTxWithRetries,
 ccWlanSumStatsLongSkip1,
 ccWlanSumStatsLongThroughput,
 ccWlanSumStatsLongThroughputRx,
 ccWlanSumStatsLongThroughputTx,
 ccWlanSumStatsLongTimestamp,
 ccWlanSumStatsLongTotalMus,
 ccWlanSumStatsLongTxAvgRetries100,
 ccWlanSumStatsShortAvgBitSpeed,
 ccWlanSumStatsShortAvgMuNoise,
 ccWlanSumStatsShortAvgMuSignal,
 ccWlanSumStatsShortAvgMuSnr,
 ccWlanSumStatsShortNumPkts,
 ccWlanSumStatsShortPktsPerSec100,
 ccWlanSumStatsShortPktsPerSecRx100,
 ccWlanSumStatsShortPktsPerSecTx100,
 ccWlanSumStatsShortPp10kDropped,
 ccWlanSumStatsShortPp10kNUcastPkts,
 ccWlanSumStatsShortPp10kRxUndecrypt,
 ccWlanSumStatsShortPp10kTxWithRetries,
 ccWlanSumStatsShortSkip1,
 ccWlanSumStatsShortThroughput,
 ccWlanSumStatsShortThroughputRx,
 ccWlanSumStatsShortThroughputTx,
 ccWlanSumStatsShortTimestamp,
 ccWlanSumStatsShortTotalMus,
 ccWlanSumStatsShortTxAvgRetries100,
 ccWlanThresholdRate,
 ccWlanTxOctetsAt11Mb,
 ccWlanTxOctetsAt12Mb,
 ccWlanTxOctetsAt18Mb,
 ccWlanTxOctetsAt1Mb,
 ccWlanTxOctetsAt22Mb,
 ccWlanTxOctetsAt24Mb,
 ccWlanTxOctetsAt2Mb,
 ccWlanTxOctetsAt36Mb,
 ccWlanTxOctetsAt48Mb,
 ccWlanTxOctetsAt54Mb,
 ccWlanTxOctetsAt5pt5Mb,
 ccWlanTxOctetsAt6Mb,
 ccWlanTxOctetsAt9Mb,
 ccWlanTxOctetsUcast,
 ccWlanTxPktsAt11Mb,
 ccWlanTxPktsAt12Mb,
 ccWlanTxPktsAt18Mb,
 ccWlanTxPktsAt1Mb,
 ccWlanTxPktsAt22Mb,
 ccWlanTxPktsAt24Mb,
 ccWlanTxPktsAt2Mb,
 ccWlanTxPktsAt36Mb,
 ccWlanTxPktsAt48Mb,
 ccWlanTxPktsAt54Mb,
 ccWlanTxPktsAt5pt5Mb,
 ccWlanTxPktsAt6Mb,
 ccWlanTxPktsAt9Mb,
 ccWlanTxPktsUcast,
 ccWlanTxRetriesOctets01,
 ccWlanTxRetriesOctets02,
 ccWlanTxRetriesOctets03,
 ccWlanTxRetriesOctets04,
 ccWlanTxRetriesOctets05,
 ccWlanTxRetriesOctets06,
 ccWlanTxRetriesOctets07,
 ccWlanTxRetriesOctets08,
 ccWlanTxRetriesOctets09,
 ccWlanTxRetriesOctets10,
 ccWlanTxRetriesOctets11,
 ccWlanTxRetriesOctets12,
 ccWlanTxRetriesOctets13,
 ccWlanTxRetriesOctets14,
 ccWlanTxRetriesOctets15,
 ccWlanTxRetriesOctetsFailed,
 ccWlanTxRetriesOctetsNone,
 ccWlanTxRetriesPkts01,
 ccWlanTxRetriesPkts02,
 ccWlanTxRetriesPkts03,
 ccWlanTxRetriesPkts04,
 ccWlanTxRetriesPkts05,
 ccWlanTxRetriesPkts06,
 ccWlanTxRetriesPkts07,
 ccWlanTxRetriesPkts08,
 ccWlanTxRetriesPkts09,
 ccWlanTxRetriesPkts10,
 ccWlanTxRetriesPkts11,
 ccWlanTxRetriesPkts12,
 ccWlanTxRetriesPkts13,
 ccWlanTxRetriesPkts14,
 ccWlanTxRetriesPkts15,
 ccWlanTxRetriesPktsFailed,
 ccWlanTxRetriesPktsNone,
 ccWlanVlanId,
 ccWlanVoicePrioritization,
 ccWlanWEPSharedMode,
 ccWlanWeight) = mibBuilder.importSymbols(
    "SYMBOL-CC-WS2000-MIB",
    "cc802dt1xPortAuthLogin",
    "cc802dt1xPortAuthPass",
    "cc802dt1xPortAuthSetAp300",
    "ccMuAuthenticationMethod",
    "ccMuEncryptionMethod",
    "ccMuIpAddr",
    "ccMuIsDataReady",
    "ccMuLastActivity",
    "ccMuLastMac",
    "ccMuLastPortal",
    "ccMuLastReason",
    "ccMuMac",
    "ccMuMeshMode",
    "ccMuPortalIndex",
    "ccMuPortalMac",
    "ccMuPowerMode",
    "ccMuRadioType",
    "ccMuRxOctetsAt11Mb",
    "ccMuRxOctetsAt12Mb",
    "ccMuRxOctetsAt18Mb",
    "ccMuRxOctetsAt1Mb",
    "ccMuRxOctetsAt22Mb",
    "ccMuRxOctetsAt24Mb",
    "ccMuRxOctetsAt2Mb",
    "ccMuRxOctetsAt36Mb",
    "ccMuRxOctetsAt48Mb",
    "ccMuRxOctetsAt54Mb",
    "ccMuRxOctetsAt5pt5Mb",
    "ccMuRxOctetsAt6Mb",
    "ccMuRxOctetsAt9Mb",
    "ccMuRxOctetsNUcast",
    "ccMuRxOctetsUcast",
    "ccMuRxPktsAt11Mb",
    "ccMuRxPktsAt12Mb",
    "ccMuRxPktsAt18Mb",
    "ccMuRxPktsAt1Mb",
    "ccMuRxPktsAt22Mb",
    "ccMuRxPktsAt24Mb",
    "ccMuRxPktsAt2Mb",
    "ccMuRxPktsAt36Mb",
    "ccMuRxPktsAt48Mb",
    "ccMuRxPktsAt54Mb",
    "ccMuRxPktsAt5pt5Mb",
    "ccMuRxPktsAt6Mb",
    "ccMuRxPktsAt9Mb",
    "ccMuRxPktsNUcast",
    "ccMuRxPktsUcast",
    "ccMuRxRssiMostRecent",
    "ccMuRxRssiNumPkts",
    "ccMuRxRssiSum",
    "ccMuRxRssiSumSquares",
    "ccMuRxUndecryptablePkts",
    "ccMuSigStatsNoiseBest",
    "ccMuSigStatsNoiseMostRecent",
    "ccMuSigStatsNoiseSum",
    "ccMuSigStatsNoiseSumSquares",
    "ccMuSigStatsNoiseWorst",
    "ccMuSigStatsNumPkts",
    "ccMuSigStatsSignalBest",
    "ccMuSigStatsSignalMostRecent",
    "ccMuSigStatsSignalSum",
    "ccMuSigStatsSignalSumSquares",
    "ccMuSigStatsSignalWorst",
    "ccMuSigStatsSnrBest",
    "ccMuSigStatsSnrMostRecent",
    "ccMuSigStatsSnrSum",
    "ccMuSigStatsSnrSumSquares",
    "ccMuSigStatsSnrWorst",
    "ccMuSumStatsLongAvgBitSpeed",
    "ccMuSumStatsLongAvgMuNoise",
    "ccMuSumStatsLongAvgMuSignal",
    "ccMuSumStatsLongAvgMuSnr",
    "ccMuSumStatsLongNumPkts",
    "ccMuSumStatsLongPktsPerSec100",
    "ccMuSumStatsLongPktsPerSecRx100",
    "ccMuSumStatsLongPktsPerSecTx100",
    "ccMuSumStatsLongPp10kDropped",
    "ccMuSumStatsLongPp10kNUcastPkts",
    "ccMuSumStatsLongPp10kRxUndecrypt",
    "ccMuSumStatsLongPp10kTxWithRetries",
    "ccMuSumStatsLongThroughput",
    "ccMuSumStatsLongThroughputRx",
    "ccMuSumStatsLongThroughputTx",
    "ccMuSumStatsLongTimestamp",
    "ccMuSumStatsLongTxAvgRetries100",
    "ccMuSumStatsShortAvgBitSpeed",
    "ccMuSumStatsShortAvgMuNoise",
    "ccMuSumStatsShortAvgMuSignal",
    "ccMuSumStatsShortAvgMuSnr",
    "ccMuSumStatsShortNumPkts",
    "ccMuSumStatsShortPktsPerSec100",
    "ccMuSumStatsShortPktsPerSecRx100",
    "ccMuSumStatsShortPktsPerSecTx100",
    "ccMuSumStatsShortPp10kDropped",
    "ccMuSumStatsShortPp10kNUcastPkts",
    "ccMuSumStatsShortPp10kRxUndecrypt",
    "ccMuSumStatsShortPp10kTxWithRetries",
    "ccMuSumStatsShortThroughput",
    "ccMuSumStatsShortThroughputRx",
    "ccMuSumStatsShortThroughputTx",
    "ccMuSumStatsShortTimestamp",
    "ccMuSumStatsShortTxAvgRetries100",
    "ccMuSupportedRates",
    "ccMuSymbolRogueApEna",
    "ccMuTxOctetsAt11Mb",
    "ccMuTxOctetsAt12Mb",
    "ccMuTxOctetsAt18Mb",
    "ccMuTxOctetsAt1Mb",
    "ccMuTxOctetsAt22Mb",
    "ccMuTxOctetsAt24Mb",
    "ccMuTxOctetsAt2Mb",
    "ccMuTxOctetsAt36Mb",
    "ccMuTxOctetsAt48Mb",
    "ccMuTxOctetsAt54Mb",
    "ccMuTxOctetsAt5pt5Mb",
    "ccMuTxOctetsAt6Mb",
    "ccMuTxOctetsAt9Mb",
    "ccMuTxOctetsUcast",
    "ccMuTxPktsAt11Mb",
    "ccMuTxPktsAt12Mb",
    "ccMuTxPktsAt18Mb",
    "ccMuTxPktsAt1Mb",
    "ccMuTxPktsAt22Mb",
    "ccMuTxPktsAt24Mb",
    "ccMuTxPktsAt2Mb",
    "ccMuTxPktsAt36Mb",
    "ccMuTxPktsAt48Mb",
    "ccMuTxPktsAt54Mb",
    "ccMuTxPktsAt5pt5Mb",
    "ccMuTxPktsAt6Mb",
    "ccMuTxPktsAt9Mb",
    "ccMuTxPktsUcast",
    "ccMuTxRetries01",
    "ccMuTxRetries02",
    "ccMuTxRetries03",
    "ccMuTxRetries04",
    "ccMuTxRetries05",
    "ccMuTxRetries06",
    "ccMuTxRetries07",
    "ccMuTxRetries08",
    "ccMuTxRetries09",
    "ccMuTxRetries10",
    "ccMuTxRetries11",
    "ccMuTxRetries12",
    "ccMuTxRetries13",
    "ccMuTxRetries14",
    "ccMuTxRetries15",
    "ccMuTxRetriesFailed",
    "ccMuTxRetriesMostRecent",
    "ccMuTxRetriesNone",
    "ccMuTxRetriesOctets01",
    "ccMuTxRetriesOctets02",
    "ccMuTxRetriesOctets03",
    "ccMuTxRetriesOctets04",
    "ccMuTxRetriesOctets05",
    "ccMuTxRetriesOctets06",
    "ccMuTxRetriesOctets07",
    "ccMuTxRetriesOctets08",
    "ccMuTxRetriesOctets09",
    "ccMuTxRetriesOctets10",
    "ccMuTxRetriesOctets11",
    "ccMuTxRetriesOctets12",
    "ccMuTxRetriesOctets13",
    "ccMuTxRetriesOctets14",
    "ccMuTxRetriesOctets15",
    "ccMuTxRetriesOctetsFailed",
    "ccMuTxRetriesOctetsNone",
    "ccMuTxRetriesTotal",
    "ccMuType",
    "ccMuVlanId",
    "ccMuWlanIndex",
    "ccMuWlanName",
    "ccPortalAdoptionEndMac",
    "ccPortalAdoptionIndex",
    "ccPortalAdoptionRowStatus",
    "ccPortalAdoptionStartMac",
    "ccPortalAdoptionWlanPointers",
    "ccPortalAssociatedMus",
    "ccPortalBackgroundNoiseBest",
    "ccPortalBackgroundNoiseNumSamples",
    "ccPortalBackgroundNoiseSum",
    "ccPortalBackgroundNoiseSumSquares",
    "ccPortalBackgroundNoiseWorst",
    "ccPortalCfgRadioChannel",
    "ccPortalCfgRadioChannelMode",
    "ccPortalCfgRadioDefaultChannel",
    "ccPortalCfgRadioDefaultChannelMode",
    "ccPortalCfgRadioDefaultDesChannel",
    "ccPortalCfgRadioDefaultDesPlacement",
    "ccPortalCfgRadioDefaultDesPowerInMW",
    "ccPortalCfgRadioDefaultDesPowerLevel",
    "ccPortalCfgRadioDefaultPlacement",
    "ccPortalCfgRadioDefaultPosChannel",
    "ccPortalCfgRadioDefaultPosPowerLevel",
    "ccPortalCfgRadioDefaultPowerInMW",
    "ccPortalCfgRadioDefaultPowerLevel",
    "ccPortalCfgRadioDefaultReset",
    "ccPortalCfgRadioDefaultSet",
    "ccPortalCfgRadioDesChannel",
    "ccPortalCfgRadioDesPlacement",
    "ccPortalCfgRadioDesPowerInMW",
    "ccPortalCfgRadioDesPowerLevel",
    "ccPortalCfgRadioPlacement",
    "ccPortalCfgRadioPosChannel",
    "ccPortalCfgRadioPosPowerLevel",
    "ccPortalCfgRadioPowerInMW",
    "ccPortalCfgRadioPowerLevel",
    "ccPortalCfgRadioRemapChannel",
    "ccPortalCfgRadioReset",
    "ccPortalCfgRadioSet",
    "ccPortalChannel",
    "ccPortalIndex",
    "ccPortalIpAddress",
    "ccPortalLastActivity",
    "ccPortalLastAdoption",
    "ccPortalLastMac",
    "ccPortalLastReason",
    "ccPortalLegacyMode",
    "ccPortalLocation",
    "ccPortalMac",
    "ccPortalMeshAvailableBaseChannel",
    "ccPortalMeshAvailableBaseMac",
    "ccPortalMeshAvailableBaseRssi",
    "ccPortalMeshPreferredBaseMac",
    "ccPortalMeshPreferredBaseRowStatus",
    "ccPortalModeLegacy",
    "ccPortalName",
    "ccPortalNumberOfBss",
    "ccPortalNumberOfEss",
    "ccPortalOptions",
    "ccPortalPointerToAp",
    "ccPortalPointersToWlans",
    "ccPortalRadioRemapChannel",
    "ccPortalRadioType",
    "ccPortalRxOctetsAt11Mb",
    "ccPortalRxOctetsAt12Mb",
    "ccPortalRxOctetsAt18Mb",
    "ccPortalRxOctetsAt1Mb",
    "ccPortalRxOctetsAt22Mb",
    "ccPortalRxOctetsAt24Mb",
    "ccPortalRxOctetsAt2Mb",
    "ccPortalRxOctetsAt36Mb",
    "ccPortalRxOctetsAt48Mb",
    "ccPortalRxOctetsAt54Mb",
    "ccPortalRxOctetsAt5pt5Mb",
    "ccPortalRxOctetsAt6Mb",
    "ccPortalRxOctetsAt9Mb",
    "ccPortalRxOctetsNUcast",
    "ccPortalRxOctetsUcast",
    "ccPortalRxPktsAt11Mb",
    "ccPortalRxPktsAt12Mb",
    "ccPortalRxPktsAt18Mb",
    "ccPortalRxPktsAt1Mb",
    "ccPortalRxPktsAt22Mb",
    "ccPortalRxPktsAt24Mb",
    "ccPortalRxPktsAt2Mb",
    "ccPortalRxPktsAt36Mb",
    "ccPortalRxPktsAt48Mb",
    "ccPortalRxPktsAt54Mb",
    "ccPortalRxPktsAt5pt5Mb",
    "ccPortalRxPktsAt6Mb",
    "ccPortalRxPktsAt9Mb",
    "ccPortalRxPktsNUcast",
    "ccPortalRxPktsUcast",
    "ccPortalRxUndecryptablePkts",
    "ccPortalSIPCacMode",
    "ccPortalSettingsAdoptedWlan",
    "ccPortalSettingsAntenna",
    "ccPortalSettingsBGMode",
    "ccPortalSettingsBasicRates",
    "ccPortalSettingsBeaconInt",
    "ccPortalSettingsDefaultAntenna",
    "ccPortalSettingsDefaultBGMode",
    "ccPortalSettingsDefaultBasicRates",
    "ccPortalSettingsDefaultBeaconInt",
    "ccPortalSettingsDefaultDtimPrd",
    "ccPortalSettingsDefaultDtimPrd2",
    "ccPortalSettingsDefaultDtimPrd3",
    "ccPortalSettingsDefaultDtimPrd4",
    "ccPortalSettingsDefaultIndex",
    "ccPortalSettingsDefaultPriWlan",
    "ccPortalSettingsDefaultRtsThresh",
    "ccPortalSettingsDefaultSecBeacon",
    "ccPortalSettingsDefaultShortPreamble",
    "ccPortalSettingsDefaultSupportedRates",
    "ccPortalSettingsDefaultUniSpread",
    "ccPortalSettingsDetector",
    "ccPortalSettingsDtimPrd",
    "ccPortalSettingsDtimPrd2",
    "ccPortalSettingsDtimPrd3",
    "ccPortalSettingsDtimPrd4",
    "ccPortalSettingsLocation",
    "ccPortalSettingsMeshAutoBaseSelection",
    "ccPortalSettingsMeshBaseChannel",
    "ccPortalSettingsMeshBaseEnable",
    "ccPortalSettingsMeshClientEnable",
    "ccPortalSettingsMeshClientWlanIndex",
    "ccPortalSettingsMeshMaxClients",
    "ccPortalSettingsName",
    "ccPortalSettingsPriWlan",
    "ccPortalSettingsRevertAp",
    "ccPortalSettingsRtsThresh",
    "ccPortalSettingsSecBeacon",
    "ccPortalSettingsShortPreamble",
    "ccPortalSettingsSipActiveSessCnt",
    "ccPortalSettingsSipAllowedSessCnt",
    "ccPortalSettingsSipInActiveSessCnt",
    "ccPortalSettingsSipRoamedSessCnt",
    "ccPortalSettingsSupportedRates",
    "ccPortalSettingsUniSpread",
    "ccPortalSettingsWMEProfile",
    "ccPortalSigStatsNoiseBest",
    "ccPortalSigStatsNoiseMostRecent",
    "ccPortalSigStatsNoiseSum",
    "ccPortalSigStatsNoiseSumSquares",
    "ccPortalSigStatsNoiseWorst",
    "ccPortalSigStatsNumPkts",
    "ccPortalSigStatsSignalBest",
    "ccPortalSigStatsSignalMostRecent",
    "ccPortalSigStatsSignalSum",
    "ccPortalSigStatsSignalSumSquares",
    "ccPortalSigStatsSignalWorst",
    "ccPortalSigStatsSnrBest",
    "ccPortalSigStatsSnrMostRecent",
    "ccPortalSigStatsSnrSum",
    "ccPortalSigStatsSnrSumSquares",
    "ccPortalSigStatsSnrWorst",
    "ccPortalState",
    "ccPortalSumStatsLongAvgBitSpeed",
    "ccPortalSumStatsLongAvgMuNoise",
    "ccPortalSumStatsLongAvgMuSignal",
    "ccPortalSumStatsLongAvgMuSnr",
    "ccPortalSumStatsLongNumPkts",
    "ccPortalSumStatsLongPktsPerSec100",
    "ccPortalSumStatsLongPktsPerSecRx100",
    "ccPortalSumStatsLongPktsPerSecTx100",
    "ccPortalSumStatsLongPp10kDropped",
    "ccPortalSumStatsLongPp10kNUcastPkts",
    "ccPortalSumStatsLongPp10kRfUtil",
    "ccPortalSumStatsLongPp10kRxUndecrypt",
    "ccPortalSumStatsLongPp10kTxMaxRetries",
    "ccPortalSumStatsLongPp10kTxWithRetries",
    "ccPortalSumStatsLongThroughput",
    "ccPortalSumStatsLongThroughputRx",
    "ccPortalSumStatsLongThroughputTx",
    "ccPortalSumStatsLongTimestamp",
    "ccPortalSumStatsLongTotalMus",
    "ccPortalSumStatsLongTxAvgRetries100",
    "ccPortalSumStatsShortAvgBitSpeed",
    "ccPortalSumStatsShortAvgMuNoise",
    "ccPortalSumStatsShortAvgMuSignal",
    "ccPortalSumStatsShortAvgMuSnr",
    "ccPortalSumStatsShortNumPkts",
    "ccPortalSumStatsShortPktsPerSec100",
    "ccPortalSumStatsShortPktsPerSecRx100",
    "ccPortalSumStatsShortPktsPerSecTx100",
    "ccPortalSumStatsShortPp10kDropped",
    "ccPortalSumStatsShortPp10kNUcastPkts",
    "ccPortalSumStatsShortPp10kRfUtil",
    "ccPortalSumStatsShortPp10kRxUndecrypt",
    "ccPortalSumStatsShortPp10kTxMaxRetries",
    "ccPortalSumStatsShortPp10kTxWithRetries",
    "ccPortalSumStatsShortThroughput",
    "ccPortalSumStatsShortThroughputRx",
    "ccPortalSumStatsShortThroughputTx",
    "ccPortalSumStatsShortTimestamp",
    "ccPortalSumStatsShortTotalMus",
    "ccPortalSumStatsShortTxAvgRetries100",
    "ccPortalSystemStatsBeaconsTx",
    "ccPortalSystemStatsBeaconsTxOctets",
    "ccPortalSystemStatsProbeReqRx",
    "ccPortalSystemStatsProbeReqRxOctets",
    "ccPortalSystemStatsProbeRespRetries1",
    "ccPortalSystemStatsProbeRespRetries2",
    "ccPortalSystemStatsProbeRespRetries3OrMore",
    "ccPortalSystemStatsProbeRespRetriesFailed",
    "ccPortalSystemStatsProbeRespRetriesNone",
    "ccPortalSystemStatsProbeRespTxOctets",
    "ccPortalTxOctetsAt11Mb",
    "ccPortalTxOctetsAt12Mb",
    "ccPortalTxOctetsAt18Mb",
    "ccPortalTxOctetsAt1Mb",
    "ccPortalTxOctetsAt22Mb",
    "ccPortalTxOctetsAt24Mb",
    "ccPortalTxOctetsAt2Mb",
    "ccPortalTxOctetsAt36Mb",
    "ccPortalTxOctetsAt48Mb",
    "ccPortalTxOctetsAt54Mb",
    "ccPortalTxOctetsAt5pt5Mb",
    "ccPortalTxOctetsAt6Mb",
    "ccPortalTxOctetsAt9Mb",
    "ccPortalTxOctetsUcast",
    "ccPortalTxPktsAt11Mb",
    "ccPortalTxPktsAt12Mb",
    "ccPortalTxPktsAt18Mb",
    "ccPortalTxPktsAt1Mb",
    "ccPortalTxPktsAt22Mb",
    "ccPortalTxPktsAt24Mb",
    "ccPortalTxPktsAt2Mb",
    "ccPortalTxPktsAt36Mb",
    "ccPortalTxPktsAt48Mb",
    "ccPortalTxPktsAt54Mb",
    "ccPortalTxPktsAt5pt5Mb",
    "ccPortalTxPktsAt6Mb",
    "ccPortalTxPktsAt9Mb",
    "ccPortalTxPktsUcast",
    "ccPortalTxPowerLevel",
    "ccPortalTxRetriesOctets01",
    "ccPortalTxRetriesOctets02",
    "ccPortalTxRetriesOctets03",
    "ccPortalTxRetriesOctets04",
    "ccPortalTxRetriesOctets05",
    "ccPortalTxRetriesOctets06",
    "ccPortalTxRetriesOctets07",
    "ccPortalTxRetriesOctets08",
    "ccPortalTxRetriesOctets09",
    "ccPortalTxRetriesOctets10",
    "ccPortalTxRetriesOctets11",
    "ccPortalTxRetriesOctets12",
    "ccPortalTxRetriesOctets13",
    "ccPortalTxRetriesOctets14",
    "ccPortalTxRetriesOctets15",
    "ccPortalTxRetriesOctetsFailed",
    "ccPortalTxRetriesOctetsNone",
    "ccPortalTxRetriesPkts01",
    "ccPortalTxRetriesPkts02",
    "ccPortalTxRetriesPkts03",
    "ccPortalTxRetriesPkts04",
    "ccPortalTxRetriesPkts05",
    "ccPortalTxRetriesPkts06",
    "ccPortalTxRetriesPkts07",
    "ccPortalTxRetriesPkts08",
    "ccPortalTxRetriesPkts09",
    "ccPortalTxRetriesPkts10",
    "ccPortalTxRetriesPkts11",
    "ccPortalTxRetriesPkts12",
    "ccPortalTxRetriesPkts13",
    "ccPortalTxRetriesPkts14",
    "ccPortalTxRetriesPkts15",
    "ccPortalTxRetriesPktsFailed",
    "ccPortalTxRetriesPktsNone",
    "ccSubnetEntry",
    "ccWanVpnEntry",
    "ccWlanAnswerBroadcastEss",
    "ccWlanAuthEapMuMaxRetries",
    "ccWlanAuthEapMuQuietPeriod",
    "ccWlanAuthEapMuTimeout",
    "ccWlanAuthEapMuTxPeriod",
    "ccWlanAuthEapRadius1Port",
    "ccWlanAuthEapRadius1Server",
    "ccWlanAuthEapRadius1SharedSecret",
    "ccWlanAuthEapRadius2Port",
    "ccWlanAuthEapRadius2Server",
    "ccWlanAuthEapRadius2SharedSecret",
    "ccWlanAuthEapRadiusAcctMode",
    "ccWlanAuthEapRadiusAcctMuRetries",
    "ccWlanAuthEapRadiusAcctMuTimeout",
    "ccWlanAuthEapReauthenticationEnable",
    "ccWlanAuthEapReauthenticationMaxRetries",
    "ccWlanAuthEapReauthenticationPeriod",
    "ccWlanAuthEapServerMaxRetries",
    "ccWlanAuthEapServerTimeout",
    "ccWlanAuthEapSyslogMode",
    "ccWlanAuthEapSyslogSeverIp",
    "ccWlanAuthKerberosKdcPort1",
    "ccWlanAuthKerberosKdcPort2",
    "ccWlanAuthKerberosKdcPortR",
    "ccWlanAuthKerberosKdcServerIp1",
    "ccWlanAuthKerberosKdcServerIp2",
    "ccWlanAuthKerberosKdcServerIpR",
    "ccWlanAuthKerberosPassword",
    "ccWlanAuthKerberosRealmName",
    "ccWlanAuthKerberosUsername",
    "ccWlanAuthentication",
    "ccWlanBwShareMode",
    "ccWlanCryptoKeyguardKey1",
    "ccWlanCryptoKeyguardKey2",
    "ccWlanCryptoKeyguardKey3",
    "ccWlanCryptoKeyguardKey4",
    "ccWlanCryptoKeyguardKeyToUse",
    "ccWlanCryptoKeyguardPasskey",
    "ccWlanCryptoUseWpa2",
    "ccWlanCryptoWepKey1",
    "ccWlanCryptoWepKey2",
    "ccWlanCryptoWepKey3",
    "ccWlanCryptoWepKey4",
    "ccWlanCryptoWepKeyToUse",
    "ccWlanCryptoWepPassKey",
    "ccWlanCryptoWpaBcastKeyRotation",
    "ccWlanCryptoWpaKey",
    "ccWlanCryptoWpaKeyRotationInterval",
    "ccWlanCryptoWpaKeyToUse",
    "ccWlanCryptoWpaPassphrase",
    "ccWlanCryptoWpaTwoAllowTkipClient",
    "ccWlanCryptoWpaTwoBcastKeyRotation",
    "ccWlanCryptoWpaTwoFastRoamKeyCache",
    "ccWlanCryptoWpaTwoFastRoamPreAuth",
    "ccWlanCryptoWpaTwoKey",
    "ccWlanCryptoWpaTwoKeyRotationInterval",
    "ccWlanCryptoWpaTwoKeyToUse",
    "ccWlanCryptoWpaTwoPassphrase",
    "ccWlanDisallowMuToMu",
    "ccWlanEnable",
    "ccWlanEncryption",
    "ccWlanEssid",
    "ccWlanIndex",
    "ccWlanLastActivity",
    "ccWlanMuAclDefault",
    "ccWlanMuAclEndingMac",
    "ccWlanMuAclIndex",
    "ccWlanMuAclName",
    "ccWlanMuAclRowStatus",
    "ccWlanMuAclStartingMac",
    "ccWlanMuInactivityTimeout",
    "ccWlanMulticastAddr1",
    "ccWlanMulticastAddr2",
    "ccWlanName",
    "ccWlanPortalsAdopted",
    "ccWlanQosMonitorDropped",
    "ccWlanQosMonitorSent",
    "ccWlanQosWMEPriorityConversion",
    "ccWlanQosWMEProfileBackgroundAifsn",
    "ccWlanQosWMEProfileBackgroundECwmax",
    "ccWlanQosWMEProfileBackgroundECwmin",
    "ccWlanQosWMEProfileBackgroundTxopsTime",
    "ccWlanQosWMEProfileBestEffortAifsn",
    "ccWlanQosWMEProfileBestEffortECwmax",
    "ccWlanQosWMEProfileBestEffortECwmin",
    "ccWlanQosWMEProfileBestEffortTxopsTime",
    "ccWlanQosWMEProfileIndex",
    "ccWlanQosWMEProfileName",
    "ccWlanQosWMEProfileRowStatus",
    "ccWlanQosWMEProfileVideoAifsn",
    "ccWlanQosWMEProfileVideoECwmax",
    "ccWlanQosWMEProfileVideoECwmin",
    "ccWlanQosWMEProfileVideoTxopsTime",
    "ccWlanQosWMEProfileVoiceAifsn",
    "ccWlanQosWMEProfileVoiceECwmax",
    "ccWlanQosWMEProfileVoiceECwmin",
    "ccWlanQosWMEProfileVoiceTxopsTime",
    "ccWlanQosWMETrafficAccessCategory",
    "ccWlanQosWMETrafficDestIp",
    "ccWlanQosWMETrafficDestMask",
    "ccWlanQosWMETrafficDestPortEnd",
    "ccWlanQosWMETrafficDestPortStart",
    "ccWlanQosWMETrafficIndex",
    "ccWlanQosWMETrafficRowStatus",
    "ccWlanQosWMETrafficSrcIp",
    "ccWlanQosWMETrafficSrcMask",
    "ccWlanQosWMETrafficSrcPortEnd",
    "ccWlanQosWMETrafficSrcPortStart",
    "ccWlanQosWMEWlanProfile",
    "ccWlanRxOctetsAt11Mb",
    "ccWlanRxOctetsAt12Mb",
    "ccWlanRxOctetsAt18Mb",
    "ccWlanRxOctetsAt1Mb",
    "ccWlanRxOctetsAt22Mb",
    "ccWlanRxOctetsAt24Mb",
    "ccWlanRxOctetsAt2Mb",
    "ccWlanRxOctetsAt36Mb",
    "ccWlanRxOctetsAt48Mb",
    "ccWlanRxOctetsAt54Mb",
    "ccWlanRxOctetsAt5pt5Mb",
    "ccWlanRxOctetsAt6Mb",
    "ccWlanRxOctetsAt9Mb",
    "ccWlanRxOctetsNUcast",
    "ccWlanRxOctetsUcast",
    "ccWlanRxPktsAt11Mb",
    "ccWlanRxPktsAt12Mb",
    "ccWlanRxPktsAt18Mb",
    "ccWlanRxPktsAt1Mb",
    "ccWlanRxPktsAt22Mb",
    "ccWlanRxPktsAt24Mb",
    "ccWlanRxPktsAt2Mb",
    "ccWlanRxPktsAt36Mb",
    "ccWlanRxPktsAt48Mb",
    "ccWlanRxPktsAt54Mb",
    "ccWlanRxPktsAt5pt5Mb",
    "ccWlanRxPktsAt6Mb",
    "ccWlanRxPktsAt9Mb",
    "ccWlanRxPktsNUcast",
    "ccWlanRxPktsUcast",
    "ccWlanRxUndecryptablePkts",
    "ccWlanSecBeacon",
    "ccWlanSigStatsNoiseBest",
    "ccWlanSigStatsNoiseSum",
    "ccWlanSigStatsNoiseSumSquares",
    "ccWlanSigStatsNoiseWorst",
    "ccWlanSigStatsNumPkts",
    "ccWlanSigStatsSignalBest",
    "ccWlanSigStatsSignalSum",
    "ccWlanSigStatsSignalSumSquares",
    "ccWlanSigStatsSignalWorst",
    "ccWlanSigStatsSnrBest",
    "ccWlanSigStatsSnrSum",
    "ccWlanSigStatsSnrSumSquares",
    "ccWlanSigStatsSnrWorst",
    "ccWlanSubnet",
    "ccWlanSumStatsLongAvgBitSpeed",
    "ccWlanSumStatsLongAvgMuNoise",
    "ccWlanSumStatsLongAvgMuSignal",
    "ccWlanSumStatsLongAvgMuSnr",
    "ccWlanSumStatsLongNumPkts",
    "ccWlanSumStatsLongPktsPerSec100",
    "ccWlanSumStatsLongPktsPerSecRx100",
    "ccWlanSumStatsLongPktsPerSecTx100",
    "ccWlanSumStatsLongPp10kDropped",
    "ccWlanSumStatsLongPp10kNUcastPkts",
    "ccWlanSumStatsLongPp10kRxUndecrypt",
    "ccWlanSumStatsLongPp10kTxWithRetries",
    "ccWlanSumStatsLongSkip1",
    "ccWlanSumStatsLongThroughput",
    "ccWlanSumStatsLongThroughputRx",
    "ccWlanSumStatsLongThroughputTx",
    "ccWlanSumStatsLongTimestamp",
    "ccWlanSumStatsLongTotalMus",
    "ccWlanSumStatsLongTxAvgRetries100",
    "ccWlanSumStatsShortAvgBitSpeed",
    "ccWlanSumStatsShortAvgMuNoise",
    "ccWlanSumStatsShortAvgMuSignal",
    "ccWlanSumStatsShortAvgMuSnr",
    "ccWlanSumStatsShortNumPkts",
    "ccWlanSumStatsShortPktsPerSec100",
    "ccWlanSumStatsShortPktsPerSecRx100",
    "ccWlanSumStatsShortPktsPerSecTx100",
    "ccWlanSumStatsShortPp10kDropped",
    "ccWlanSumStatsShortPp10kNUcastPkts",
    "ccWlanSumStatsShortPp10kRxUndecrypt",
    "ccWlanSumStatsShortPp10kTxWithRetries",
    "ccWlanSumStatsShortSkip1",
    "ccWlanSumStatsShortThroughput",
    "ccWlanSumStatsShortThroughputRx",
    "ccWlanSumStatsShortThroughputTx",
    "ccWlanSumStatsShortTimestamp",
    "ccWlanSumStatsShortTotalMus",
    "ccWlanSumStatsShortTxAvgRetries100",
    "ccWlanThresholdRate",
    "ccWlanTxOctetsAt11Mb",
    "ccWlanTxOctetsAt12Mb",
    "ccWlanTxOctetsAt18Mb",
    "ccWlanTxOctetsAt1Mb",
    "ccWlanTxOctetsAt22Mb",
    "ccWlanTxOctetsAt24Mb",
    "ccWlanTxOctetsAt2Mb",
    "ccWlanTxOctetsAt36Mb",
    "ccWlanTxOctetsAt48Mb",
    "ccWlanTxOctetsAt54Mb",
    "ccWlanTxOctetsAt5pt5Mb",
    "ccWlanTxOctetsAt6Mb",
    "ccWlanTxOctetsAt9Mb",
    "ccWlanTxOctetsUcast",
    "ccWlanTxPktsAt11Mb",
    "ccWlanTxPktsAt12Mb",
    "ccWlanTxPktsAt18Mb",
    "ccWlanTxPktsAt1Mb",
    "ccWlanTxPktsAt22Mb",
    "ccWlanTxPktsAt24Mb",
    "ccWlanTxPktsAt2Mb",
    "ccWlanTxPktsAt36Mb",
    "ccWlanTxPktsAt48Mb",
    "ccWlanTxPktsAt54Mb",
    "ccWlanTxPktsAt5pt5Mb",
    "ccWlanTxPktsAt6Mb",
    "ccWlanTxPktsAt9Mb",
    "ccWlanTxPktsUcast",
    "ccWlanTxRetriesOctets01",
    "ccWlanTxRetriesOctets02",
    "ccWlanTxRetriesOctets03",
    "ccWlanTxRetriesOctets04",
    "ccWlanTxRetriesOctets05",
    "ccWlanTxRetriesOctets06",
    "ccWlanTxRetriesOctets07",
    "ccWlanTxRetriesOctets08",
    "ccWlanTxRetriesOctets09",
    "ccWlanTxRetriesOctets10",
    "ccWlanTxRetriesOctets11",
    "ccWlanTxRetriesOctets12",
    "ccWlanTxRetriesOctets13",
    "ccWlanTxRetriesOctets14",
    "ccWlanTxRetriesOctets15",
    "ccWlanTxRetriesOctetsFailed",
    "ccWlanTxRetriesOctetsNone",
    "ccWlanTxRetriesPkts01",
    "ccWlanTxRetriesPkts02",
    "ccWlanTxRetriesPkts03",
    "ccWlanTxRetriesPkts04",
    "ccWlanTxRetriesPkts05",
    "ccWlanTxRetriesPkts06",
    "ccWlanTxRetriesPkts07",
    "ccWlanTxRetriesPkts08",
    "ccWlanTxRetriesPkts09",
    "ccWlanTxRetriesPkts10",
    "ccWlanTxRetriesPkts11",
    "ccWlanTxRetriesPkts12",
    "ccWlanTxRetriesPkts13",
    "ccWlanTxRetriesPkts14",
    "ccWlanTxRetriesPkts15",
    "ccWlanTxRetriesPktsFailed",
    "ccWlanTxRetriesPktsNone",
    "ccWlanVlanId",
    "ccWlanVoicePrioritization",
    "ccWlanWEPSharedMode",
    "ccWlanWeight")


# MODULE-IDENTITY

moduleid = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 1)
)
moduleid.setRevisions(
        ("2009-12-30 13:36",)
)


# Types definitions



class SinglePointer(Integer32):
    """Custom type SinglePointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class MultiPointer63(Bits):
    """Custom type MultiPointer63 based on Bits"""




class MultiPointer255(Bits):
    """Custom type MultiPointer255 based on Bits"""




class DoActionNow(Integer32):
    """Custom type DoActionNow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doActionRightNow", 1),
          ("idleState", 2))
    )





class RadioType(Integer32):
    """Custom type RadioType based on Integer32"""
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
        *(("radio802dot11A", 1),
          ("radio802dot11B", 2),
          ("radio802dot11FH", 4),
          ("radio802dot11G", 3))
    )





class Password(OctetString):
    """Custom type Password based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )





class StaticRowEnable(Integer32):
    """Custom type StaticRowEnable based on Integer32"""
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





class PartsPer10k(Unsigned32):
    """Custom type PartsPer10k based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )





class ScaleBy100(Unsigned32):
    """Custom type ScaleBy100 based on Unsigned32"""




class AbbrevRowStatus(Integer32):
    """Custom type AbbrevRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("createAndGo", 4),
          ("destroy", 6))
    )





class DoActionShowProgress(Integer32):
    """Custom type DoActionShowProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doActionRightNow", 1),
          ("idleState", 2))
    )





class HexPassword(OctetString):
    """Custom type HexPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )





class TransmitRate(Bits):
    """Custom type TransmitRate based on Bits"""




class AllowedChannels(Integer32):
    """Custom type AllowedChannels based on Integer32"""
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
              36,
              40,
              44,
              48,
              52,
              56,
              60,
              64,
              100,
              104,
              108,
              112,
              116,
              120,
              124,
              128,
              132,
              136,
              140,
              149,
              153,
              157,
              161,
              165)
        )
    )
    namedValues = NamedValues(
        *(("channel1", 1),
          ("channel10", 10),
          ("channel100", 100),
          ("channel104", 104),
          ("channel108", 108),
          ("channel11", 11),
          ("channel112", 112),
          ("channel116", 116),
          ("channel12", 12),
          ("channel120", 120),
          ("channel124", 124),
          ("channel128", 128),
          ("channel13", 13),
          ("channel132", 132),
          ("channel136", 136),
          ("channel14", 14),
          ("channel140", 140),
          ("channel149", 149),
          ("channel153", 153),
          ("channel157", 157),
          ("channel161", 161),
          ("channel165", 165),
          ("channel2", 2),
          ("channel3", 3),
          ("channel36", 36),
          ("channel4", 4),
          ("channel40", 40),
          ("channel44", 44),
          ("channel48", 48),
          ("channel5", 5),
          ("channel52", 52),
          ("channel56", 56),
          ("channel6", 6),
          ("channel60", 60),
          ("channel64", 64),
          ("channel7", 7),
          ("channel8", 8),
          ("channel9", 9))
    )




# TEXTUAL-CONVENTIONS



class RowStatus(Integer32, TextualConvention):
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )



class DateAndTime(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d-1d-1d,1d:1d:1d.1d,1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )



class EthernetType(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x "
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



# MIB Managed Objects in the order of their OIDs

_Symbol_ObjectIdentity = ObjectIdentity
symbol = _Symbol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388)
)
_Wsd_ObjectIdentity = ObjectIdentity
wsd = _Wsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11)
)
_Sysoids_ObjectIdentity = ObjectIdentity
sysoids = _Sysoids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 1)
)
_Ap5131_ObjectIdentity = ObjectIdentity
ap5131 = _Ap5131_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 1, 2)
)
if mibBuilder.loadTexts:
    ap5131.setStatus("current")
_Ap5181_ObjectIdentity = ObjectIdentity
ap5181 = _Ap5181_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 1, 3)
)
if mibBuilder.loadTexts:
    ap5181.setStatus("current")
_Ap7131_ObjectIdentity = ObjectIdentity
ap7131 = _Ap7131_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 1, 4)
)
if mibBuilder.loadTexts:
    ap7131.setStatus("current")
_Ap7181_ObjectIdentity = ObjectIdentity
ap7181 = _Ap7181_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 1, 5)
)
if mibBuilder.loadTexts:
    ap7181.setStatus("current")
_AbgAP_ObjectIdentity = ObjectIdentity
abgAP = _AbgAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3)
)
_Dot1x_ObjectIdentity = ObjectIdentity
dot1x = _Dot1x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3)
)
_Dot1xPaeAuthenticator_ObjectIdentity = ObjectIdentity
dot1xPaeAuthenticator = _Dot1xPaeAuthenticator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1)
)
_Dot1xAuthConfigTable_Object = MibTable
dot1xAuthConfigTable = _Dot1xAuthConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dot1xAuthConfigTable.setStatus("current")
_Dot1xAuthConfigEntry_Object = MibTableRow
dot1xAuthConfigEntry = _Dot1xAuthConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 1, 1)
)
dot1xAuthConfigEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    dot1xAuthConfigEntry.setStatus("current")


class _Dot1xPaePortNumber_Type(Integer32):
    """Custom type dot1xPaePortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_Dot1xPaePortNumber_Type.__name__ = "Integer32"
_Dot1xPaePortNumber_Object = MibTableColumn
dot1xPaePortNumber = _Dot1xPaePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 1, 1, 1),
    _Dot1xPaePortNumber_Type()
)
dot1xPaePortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dot1xPaePortNumber.setStatus("current")


class _Dot1xPaeState_Type(Integer32):
    """Custom type dot1xPaeState based on Integer32"""
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
        *(("aborting", 6),
          ("authenticated", 5),
          ("authenticating", 4),
          ("connecting", 3),
          ("disconnected", 2),
          ("forceAuth", 8),
          ("forceUnauth", 9),
          ("held", 7),
          ("intialize", 1))
    )


_Dot1xPaeState_Type.__name__ = "Integer32"
_Dot1xPaeState_Object = MibTableColumn
dot1xPaeState = _Dot1xPaeState_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 1, 1, 2),
    _Dot1xPaeState_Type()
)
dot1xPaeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xPaeState.setStatus("current")


class _Dot1xAuthBackendAuthState_Type(Integer32):
    """Custom type dot1xAuthBackendAuthState based on Integer32"""
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
        *(("fail", 4),
          ("idle", 6),
          ("initialize", 7),
          ("request", 1),
          ("response", 2),
          ("success", 3),
          ("timeout", 5))
    )


_Dot1xAuthBackendAuthState_Type.__name__ = "Integer32"
_Dot1xAuthBackendAuthState_Object = MibTableColumn
dot1xAuthBackendAuthState = _Dot1xAuthBackendAuthState_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 1, 1, 3),
    _Dot1xAuthBackendAuthState_Type()
)
dot1xAuthBackendAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthBackendAuthState.setStatus("current")
_Dot1xAuthAdminControlledDirections_Type = Integer32
_Dot1xAuthAdminControlledDirections_Object = MibTableColumn
dot1xAuthAdminControlledDirections = _Dot1xAuthAdminControlledDirections_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 1, 1, 4),
    _Dot1xAuthAdminControlledDirections_Type()
)
dot1xAuthAdminControlledDirections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthAdminControlledDirections.setStatus("current")
_Dot1xAuthOperControlledDirections_Type = Integer32
_Dot1xAuthOperControlledDirections_Object = MibTableColumn
dot1xAuthOperControlledDirections = _Dot1xAuthOperControlledDirections_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 1, 1, 5),
    _Dot1xAuthOperControlledDirections_Type()
)
dot1xAuthOperControlledDirections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthOperControlledDirections.setStatus("current")
_Dot1xAuthAuthControlledPortStatus_Type = Integer32
_Dot1xAuthAuthControlledPortStatus_Object = MibTableColumn
dot1xAuthAuthControlledPortStatus = _Dot1xAuthAuthControlledPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 1, 1, 6),
    _Dot1xAuthAuthControlledPortStatus_Type()
)
dot1xAuthAuthControlledPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthAuthControlledPortStatus.setStatus("current")
_Dot1xAuthAuthControlledPortControl_Type = Integer32
_Dot1xAuthAuthControlledPortControl_Object = MibTableColumn
dot1xAuthAuthControlledPortControl = _Dot1xAuthAuthControlledPortControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 1, 1, 7),
    _Dot1xAuthAuthControlledPortControl_Type()
)
dot1xAuthAuthControlledPortControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthAuthControlledPortControl.setStatus("current")
_Dot1xAuthQuietPeriod_Type = Unsigned32
_Dot1xAuthQuietPeriod_Object = MibTableColumn
dot1xAuthQuietPeriod = _Dot1xAuthQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 1, 1, 8),
    _Dot1xAuthQuietPeriod_Type()
)
dot1xAuthQuietPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthQuietPeriod.setStatus("current")
_Dot1xAuthTxPeriod_Type = Unsigned32
_Dot1xAuthTxPeriod_Object = MibTableColumn
dot1xAuthTxPeriod = _Dot1xAuthTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 1, 1, 9),
    _Dot1xAuthTxPeriod_Type()
)
dot1xAuthTxPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthTxPeriod.setStatus("current")
_Dot1xAuthSuppTimeout_Type = Unsigned32
_Dot1xAuthSuppTimeout_Object = MibTableColumn
dot1xAuthSuppTimeout = _Dot1xAuthSuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 1, 1, 10),
    _Dot1xAuthSuppTimeout_Type()
)
dot1xAuthSuppTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthSuppTimeout.setStatus("current")
_Dot1xAuthServerTimeout_Type = Unsigned32
_Dot1xAuthServerTimeout_Object = MibTableColumn
dot1xAuthServerTimeout = _Dot1xAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 1, 1, 11),
    _Dot1xAuthServerTimeout_Type()
)
dot1xAuthServerTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthServerTimeout.setStatus("current")
_Dot1xAuthMaxReq_Type = Unsigned32
_Dot1xAuthMaxReq_Object = MibTableColumn
dot1xAuthMaxReq = _Dot1xAuthMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 1, 1, 12),
    _Dot1xAuthMaxReq_Type()
)
dot1xAuthMaxReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthMaxReq.setStatus("current")
_Dot1xAuthReAuthPeriod_Type = Unsigned32
_Dot1xAuthReAuthPeriod_Object = MibTableColumn
dot1xAuthReAuthPeriod = _Dot1xAuthReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 1, 1, 13),
    _Dot1xAuthReAuthPeriod_Type()
)
dot1xAuthReAuthPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthReAuthPeriod.setStatus("current")
_Dot1xAuthReAuthEnabled_Type = TruthValue
_Dot1xAuthReAuthEnabled_Object = MibTableColumn
dot1xAuthReAuthEnabled = _Dot1xAuthReAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 1, 1, 14),
    _Dot1xAuthReAuthEnabled_Type()
)
dot1xAuthReAuthEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthReAuthEnabled.setStatus("current")
_Dot1xAuthKeyTxEnabled_Type = TruthValue
_Dot1xAuthKeyTxEnabled_Object = MibTableColumn
dot1xAuthKeyTxEnabled = _Dot1xAuthKeyTxEnabled_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 1, 1, 15),
    _Dot1xAuthKeyTxEnabled_Type()
)
dot1xAuthKeyTxEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthKeyTxEnabled.setStatus("current")
_Dot1xAuthStatsTable_Object = MibTable
dot1xAuthStatsTable = _Dot1xAuthStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    dot1xAuthStatsTable.setStatus("current")
_Dot1xAuthStatsEntry_Object = MibTableRow
dot1xAuthStatsEntry = _Dot1xAuthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 2, 1)
)
dot1xAuthStatsEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    dot1xAuthStatsEntry.setStatus("current")
_Dot1xAuthEapolFramesRx_Type = Counter32
_Dot1xAuthEapolFramesRx_Object = MibTableColumn
dot1xAuthEapolFramesRx = _Dot1xAuthEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 2, 1, 1),
    _Dot1xAuthEapolFramesRx_Type()
)
dot1xAuthEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthEapolFramesRx.setStatus("current")
_Dot1xAuthEapolFramesTx_Type = Counter32
_Dot1xAuthEapolFramesTx_Object = MibTableColumn
dot1xAuthEapolFramesTx = _Dot1xAuthEapolFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 2, 1, 2),
    _Dot1xAuthEapolFramesTx_Type()
)
dot1xAuthEapolFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthEapolFramesTx.setStatus("current")
_Dot1xAuthEapolStartFramesRx_Type = Counter32
_Dot1xAuthEapolStartFramesRx_Object = MibTableColumn
dot1xAuthEapolStartFramesRx = _Dot1xAuthEapolStartFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 2, 1, 3),
    _Dot1xAuthEapolStartFramesRx_Type()
)
dot1xAuthEapolStartFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthEapolStartFramesRx.setStatus("current")
_Dot1xAuthEapolLogoffFramesRx_Type = Counter32
_Dot1xAuthEapolLogoffFramesRx_Object = MibTableColumn
dot1xAuthEapolLogoffFramesRx = _Dot1xAuthEapolLogoffFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 2, 1, 4),
    _Dot1xAuthEapolLogoffFramesRx_Type()
)
dot1xAuthEapolLogoffFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthEapolLogoffFramesRx.setStatus("current")
_Dot1xAuthEapolRespIdFramesRx_Type = Counter32
_Dot1xAuthEapolRespIdFramesRx_Object = MibTableColumn
dot1xAuthEapolRespIdFramesRx = _Dot1xAuthEapolRespIdFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 2, 1, 5),
    _Dot1xAuthEapolRespIdFramesRx_Type()
)
dot1xAuthEapolRespIdFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthEapolRespIdFramesRx.setStatus("current")
_Dot1xAuthEapolRespFramesRx_Type = Counter32
_Dot1xAuthEapolRespFramesRx_Object = MibTableColumn
dot1xAuthEapolRespFramesRx = _Dot1xAuthEapolRespFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 2, 1, 6),
    _Dot1xAuthEapolRespFramesRx_Type()
)
dot1xAuthEapolRespFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthEapolRespFramesRx.setStatus("current")
_Dot1xAuthEapolReqIdFramesTx_Type = Counter32
_Dot1xAuthEapolReqIdFramesTx_Object = MibTableColumn
dot1xAuthEapolReqIdFramesTx = _Dot1xAuthEapolReqIdFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 2, 1, 7),
    _Dot1xAuthEapolReqIdFramesTx_Type()
)
dot1xAuthEapolReqIdFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthEapolReqIdFramesTx.setStatus("current")
_Dot1xAuthEapolReqFramesTx_Type = Counter32
_Dot1xAuthEapolReqFramesTx_Object = MibTableColumn
dot1xAuthEapolReqFramesTx = _Dot1xAuthEapolReqFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 2, 1, 8),
    _Dot1xAuthEapolReqFramesTx_Type()
)
dot1xAuthEapolReqFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthEapolReqFramesTx.setStatus("current")
_Dot1xAuthInvalidEapolFramesRx_Type = Counter32
_Dot1xAuthInvalidEapolFramesRx_Object = MibTableColumn
dot1xAuthInvalidEapolFramesRx = _Dot1xAuthInvalidEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 2, 1, 9),
    _Dot1xAuthInvalidEapolFramesRx_Type()
)
dot1xAuthInvalidEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthInvalidEapolFramesRx.setStatus("current")
_Dot1xAuthEapLengthErrorFramesRx_Type = Counter32
_Dot1xAuthEapLengthErrorFramesRx_Object = MibTableColumn
dot1xAuthEapLengthErrorFramesRx = _Dot1xAuthEapLengthErrorFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 2, 1, 10),
    _Dot1xAuthEapLengthErrorFramesRx_Type()
)
dot1xAuthEapLengthErrorFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthEapLengthErrorFramesRx.setStatus("current")


class _Dot1xAuthLastEapolFrameVersion_Type(OctetString):
    """Custom type dot1xAuthLastEapolFrameVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Dot1xAuthLastEapolFrameVersion_Type.__name__ = "OctetString"
_Dot1xAuthLastEapolFrameVersion_Object = MibTableColumn
dot1xAuthLastEapolFrameVersion = _Dot1xAuthLastEapolFrameVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 2, 1, 11),
    _Dot1xAuthLastEapolFrameVersion_Type()
)
dot1xAuthLastEapolFrameVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthLastEapolFrameVersion.setStatus("current")
_Dot1xAuthLastEapolFrameSource_Type = PhysAddress
_Dot1xAuthLastEapolFrameSource_Object = MibTableColumn
dot1xAuthLastEapolFrameSource = _Dot1xAuthLastEapolFrameSource_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 2, 1, 12),
    _Dot1xAuthLastEapolFrameSource_Type()
)
dot1xAuthLastEapolFrameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthLastEapolFrameSource.setStatus("current")
_Dot1xAuthDiagTable_Object = MibTable
dot1xAuthDiagTable = _Dot1xAuthDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 3)
)
if mibBuilder.loadTexts:
    dot1xAuthDiagTable.setStatus("current")
_Dot1xAuthDiagEntry_Object = MibTableRow
dot1xAuthDiagEntry = _Dot1xAuthDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 3, 1)
)
dot1xAuthDiagEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    dot1xAuthDiagEntry.setStatus("current")
_Dot1xAuthEntersConnecting_Type = Counter32
_Dot1xAuthEntersConnecting_Object = MibTableColumn
dot1xAuthEntersConnecting = _Dot1xAuthEntersConnecting_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 3, 1, 1),
    _Dot1xAuthEntersConnecting_Type()
)
dot1xAuthEntersConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthEntersConnecting.setStatus("current")
_Dot1xAuthEapLogoffsWhileConnecting_Type = Counter32
_Dot1xAuthEapLogoffsWhileConnecting_Object = MibTableColumn
dot1xAuthEapLogoffsWhileConnecting = _Dot1xAuthEapLogoffsWhileConnecting_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 3, 1, 2),
    _Dot1xAuthEapLogoffsWhileConnecting_Type()
)
dot1xAuthEapLogoffsWhileConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthEapLogoffsWhileConnecting.setStatus("current")
_Dot1xAuthEntersAuthenticating_Type = Counter32
_Dot1xAuthEntersAuthenticating_Object = MibTableColumn
dot1xAuthEntersAuthenticating = _Dot1xAuthEntersAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 3, 1, 3),
    _Dot1xAuthEntersAuthenticating_Type()
)
dot1xAuthEntersAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthEntersAuthenticating.setStatus("current")
_Dot1xAuthAuthSuccessWhileAuthenticating_Type = Counter32
_Dot1xAuthAuthSuccessWhileAuthenticating_Object = MibTableColumn
dot1xAuthAuthSuccessWhileAuthenticating = _Dot1xAuthAuthSuccessWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 3, 1, 4),
    _Dot1xAuthAuthSuccessWhileAuthenticating_Type()
)
dot1xAuthAuthSuccessWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthAuthSuccessWhileAuthenticating.setStatus("current")
_Dot1xAuthAuthTimeoutsWhileAuthenticating_Type = Counter32
_Dot1xAuthAuthTimeoutsWhileAuthenticating_Object = MibTableColumn
dot1xAuthAuthTimeoutsWhileAuthenticating = _Dot1xAuthAuthTimeoutsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 3, 1, 5),
    _Dot1xAuthAuthTimeoutsWhileAuthenticating_Type()
)
dot1xAuthAuthTimeoutsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthAuthTimeoutsWhileAuthenticating.setStatus("current")
_Dot1xAuthAuthFailWhileAuthenticating_Type = Counter32
_Dot1xAuthAuthFailWhileAuthenticating_Object = MibTableColumn
dot1xAuthAuthFailWhileAuthenticating = _Dot1xAuthAuthFailWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 3, 1, 6),
    _Dot1xAuthAuthFailWhileAuthenticating_Type()
)
dot1xAuthAuthFailWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthAuthFailWhileAuthenticating.setStatus("current")
_Dot1xAuthAuthReauthsWhileAuthenticating_Type = Counter32
_Dot1xAuthAuthReauthsWhileAuthenticating_Object = MibTableColumn
dot1xAuthAuthReauthsWhileAuthenticating = _Dot1xAuthAuthReauthsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 3, 1, 7),
    _Dot1xAuthAuthReauthsWhileAuthenticating_Type()
)
dot1xAuthAuthReauthsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthAuthReauthsWhileAuthenticating.setStatus("current")
_Dot1xAuthAuthEapStartsWhileAuthenticating_Type = Counter32
_Dot1xAuthAuthEapStartsWhileAuthenticating_Object = MibTableColumn
dot1xAuthAuthEapStartsWhileAuthenticating = _Dot1xAuthAuthEapStartsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 3, 1, 8),
    _Dot1xAuthAuthEapStartsWhileAuthenticating_Type()
)
dot1xAuthAuthEapStartsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthAuthEapStartsWhileAuthenticating.setStatus("current")
_Dot1xAuthAuthEapLogoffWhileAuthenticating_Type = Counter32
_Dot1xAuthAuthEapLogoffWhileAuthenticating_Object = MibTableColumn
dot1xAuthAuthEapLogoffWhileAuthenticating = _Dot1xAuthAuthEapLogoffWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 3, 1, 9),
    _Dot1xAuthAuthEapLogoffWhileAuthenticating_Type()
)
dot1xAuthAuthEapLogoffWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthAuthEapLogoffWhileAuthenticating.setStatus("current")
_Dot1xAuthAuthReauthsWhileAuthenticated_Type = Counter32
_Dot1xAuthAuthReauthsWhileAuthenticated_Object = MibTableColumn
dot1xAuthAuthReauthsWhileAuthenticated = _Dot1xAuthAuthReauthsWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 3, 1, 10),
    _Dot1xAuthAuthReauthsWhileAuthenticated_Type()
)
dot1xAuthAuthReauthsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthAuthReauthsWhileAuthenticated.setStatus("current")
_Dot1xAuthAuthEapStartsWhileAuthenticated_Type = Counter32
_Dot1xAuthAuthEapStartsWhileAuthenticated_Object = MibTableColumn
dot1xAuthAuthEapStartsWhileAuthenticated = _Dot1xAuthAuthEapStartsWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 3, 1, 11),
    _Dot1xAuthAuthEapStartsWhileAuthenticated_Type()
)
dot1xAuthAuthEapStartsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthAuthEapStartsWhileAuthenticated.setStatus("current")
_Dot1xAuthAuthEapLogoffWhileAuthenticated_Type = Counter32
_Dot1xAuthAuthEapLogoffWhileAuthenticated_Object = MibTableColumn
dot1xAuthAuthEapLogoffWhileAuthenticated = _Dot1xAuthAuthEapLogoffWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 3, 1, 12),
    _Dot1xAuthAuthEapLogoffWhileAuthenticated_Type()
)
dot1xAuthAuthEapLogoffWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthAuthEapLogoffWhileAuthenticated.setStatus("current")
_Dot1xAuthBackendResponses_Type = Counter32
_Dot1xAuthBackendResponses_Object = MibTableColumn
dot1xAuthBackendResponses = _Dot1xAuthBackendResponses_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 3, 1, 13),
    _Dot1xAuthBackendResponses_Type()
)
dot1xAuthBackendResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthBackendResponses.setStatus("current")
_Dot1xAuthBackendAccessChallenges_Type = Counter32
_Dot1xAuthBackendAccessChallenges_Object = MibTableColumn
dot1xAuthBackendAccessChallenges = _Dot1xAuthBackendAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 3, 1, 14),
    _Dot1xAuthBackendAccessChallenges_Type()
)
dot1xAuthBackendAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthBackendAccessChallenges.setStatus("current")
_Dot1xAuthBackendOtherRequestsToSupplicant_Type = Counter32
_Dot1xAuthBackendOtherRequestsToSupplicant_Object = MibTableColumn
dot1xAuthBackendOtherRequestsToSupplicant = _Dot1xAuthBackendOtherRequestsToSupplicant_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 3, 1, 15),
    _Dot1xAuthBackendOtherRequestsToSupplicant_Type()
)
dot1xAuthBackendOtherRequestsToSupplicant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthBackendOtherRequestsToSupplicant.setStatus("current")
_Dot1xAuthBackendNonNakResponsesFromSupplicant_Type = Counter32
_Dot1xAuthBackendNonNakResponsesFromSupplicant_Object = MibTableColumn
dot1xAuthBackendNonNakResponsesFromSupplicant = _Dot1xAuthBackendNonNakResponsesFromSupplicant_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 3, 1, 16),
    _Dot1xAuthBackendNonNakResponsesFromSupplicant_Type()
)
dot1xAuthBackendNonNakResponsesFromSupplicant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthBackendNonNakResponsesFromSupplicant.setStatus("current")
_Dot1xAuthBackendAuthSuccesses_Type = Counter32
_Dot1xAuthBackendAuthSuccesses_Object = MibTableColumn
dot1xAuthBackendAuthSuccesses = _Dot1xAuthBackendAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 3, 1, 17),
    _Dot1xAuthBackendAuthSuccesses_Type()
)
dot1xAuthBackendAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthBackendAuthSuccesses.setStatus("current")
_Dot1xAuthBackendAuthFails_Type = Counter32
_Dot1xAuthBackendAuthFails_Object = MibTableColumn
dot1xAuthBackendAuthFails = _Dot1xAuthBackendAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 3, 1, 18),
    _Dot1xAuthBackendAuthFails_Type()
)
dot1xAuthBackendAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthBackendAuthFails.setStatus("current")
_Dot1xAuthSessionStatsTable_Object = MibTable
dot1xAuthSessionStatsTable = _Dot1xAuthSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 4)
)
if mibBuilder.loadTexts:
    dot1xAuthSessionStatsTable.setStatus("current")
_Dot1xAuthSessionStatsEntry_Object = MibTableRow
dot1xAuthSessionStatsEntry = _Dot1xAuthSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 4, 1)
)
dot1xAuthSessionStatsEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    dot1xAuthSessionStatsEntry.setStatus("current")
_Dot1xAuthSessionOctetsRx_Type = Counter32
_Dot1xAuthSessionOctetsRx_Object = MibTableColumn
dot1xAuthSessionOctetsRx = _Dot1xAuthSessionOctetsRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 4, 1, 1),
    _Dot1xAuthSessionOctetsRx_Type()
)
dot1xAuthSessionOctetsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthSessionOctetsRx.setStatus("current")
_Dot1xAuthSessionOctetsTx_Type = Counter32
_Dot1xAuthSessionOctetsTx_Object = MibTableColumn
dot1xAuthSessionOctetsTx = _Dot1xAuthSessionOctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 4, 1, 2),
    _Dot1xAuthSessionOctetsTx_Type()
)
dot1xAuthSessionOctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthSessionOctetsTx.setStatus("current")
_Dot1xAuthSessionFramesRx_Type = Counter32
_Dot1xAuthSessionFramesRx_Object = MibTableColumn
dot1xAuthSessionFramesRx = _Dot1xAuthSessionFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 4, 1, 3),
    _Dot1xAuthSessionFramesRx_Type()
)
dot1xAuthSessionFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthSessionFramesRx.setStatus("current")
_Dot1xAuthSessionFramesTx_Type = Counter32
_Dot1xAuthSessionFramesTx_Object = MibTableColumn
dot1xAuthSessionFramesTx = _Dot1xAuthSessionFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 4, 1, 4),
    _Dot1xAuthSessionFramesTx_Type()
)
dot1xAuthSessionFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthSessionFramesTx.setStatus("current")


class _Dot1xAuthSessionId_Type(OctetString):
    """Custom type dot1xAuthSessionId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Dot1xAuthSessionId_Type.__name__ = "OctetString"
_Dot1xAuthSessionId_Object = MibTableColumn
dot1xAuthSessionId = _Dot1xAuthSessionId_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 4, 1, 5),
    _Dot1xAuthSessionId_Type()
)
dot1xAuthSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthSessionId.setStatus("current")


class _Dot1xAuthSessionAuthenticMethod_Type(Integer32):
    """Custom type dot1xAuthSessionAuthenticMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localAuthServer", 2),
          ("remoteAuthServer", 1))
    )


_Dot1xAuthSessionAuthenticMethod_Type.__name__ = "Integer32"
_Dot1xAuthSessionAuthenticMethod_Object = MibTableColumn
dot1xAuthSessionAuthenticMethod = _Dot1xAuthSessionAuthenticMethod_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 4, 1, 6),
    _Dot1xAuthSessionAuthenticMethod_Type()
)
dot1xAuthSessionAuthenticMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthSessionAuthenticMethod.setStatus("current")
_Dot1xAuthSessionTime_Type = TimeTicks
_Dot1xAuthSessionTime_Object = MibTableColumn
dot1xAuthSessionTime = _Dot1xAuthSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 4, 1, 7),
    _Dot1xAuthSessionTime_Type()
)
dot1xAuthSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthSessionTime.setStatus("current")


class _Dot1xAuthSessionTerminateCause_Type(Integer32):
    """Custom type dot1xAuthSessionTerminateCause based on Integer32"""
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
              999)
        )
    )
    namedValues = NamedValues(
        *(("authControlForceUnauth", 5),
          ("notTerminatedYet", 999),
          ("portAdminDisabled", 7),
          ("portFailure", 2),
          ("portReInit", 6),
          ("reauthFailed", 4),
          ("supplicantLogoff", 1),
          ("supplicantRestart", 3))
    )


_Dot1xAuthSessionTerminateCause_Type.__name__ = "Integer32"
_Dot1xAuthSessionTerminateCause_Object = MibTableColumn
dot1xAuthSessionTerminateCause = _Dot1xAuthSessionTerminateCause_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 4, 1, 8),
    _Dot1xAuthSessionTerminateCause_Type()
)
dot1xAuthSessionTerminateCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthSessionTerminateCause.setStatus("current")


class _Dot1xAuthSessionUserName_Type(OctetString):
    """Custom type dot1xAuthSessionUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Dot1xAuthSessionUserName_Type.__name__ = "OctetString"
_Dot1xAuthSessionUserName_Object = MibTableColumn
dot1xAuthSessionUserName = _Dot1xAuthSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 3, 1, 4, 1, 9),
    _Dot1xAuthSessionUserName_Type()
)
dot1xAuthSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthSessionUserName.setStatus("current")
_ApRf_ObjectIdentity = ObjectIdentity
apRf = _ApRf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4)
)
_ApRadio_ObjectIdentity = ObjectIdentity
apRadio = _ApRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1)
)
_ApRadioSettingsTable_Object = MibTable
apRadioSettingsTable = _ApRadioSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    apRadioSettingsTable.setStatus("current")
_ApRadioSettingsEntry_Object = MibTableRow
apRadioSettingsEntry = _ApRadioSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1)
)
apRadioSettingsEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apRadioSettingsIndex"),
)
if mibBuilder.loadTexts:
    apRadioSettingsEntry.setStatus("current")


class _ApRadioSettingsIndex_Type(Integer32):
    """Custom type apRadioSettingsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ApRadioSettingsIndex_Type.__name__ = "Integer32"
_ApRadioSettingsIndex_Object = MibTableColumn
apRadioSettingsIndex = _ApRadioSettingsIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 1),
    _ApRadioSettingsIndex_Type()
)
apRadioSettingsIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apRadioSettingsIndex.setStatus("current")
_ApRadioSettingsEnable_Type = TruthValue
_ApRadioSettingsEnable_Object = MibTableColumn
apRadioSettingsEnable = _ApRadioSettingsEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 2),
    _ApRadioSettingsEnable_Type()
)
apRadioSettingsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsEnable.setStatus("current")


class _ApRadioSettingsBand_Type(Integer32):
    """Custom type apRadioSettingsBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aRadio", 1),
          ("bgRadio", 2))
    )


_ApRadioSettingsBand_Type.__name__ = "Integer32"
_ApRadioSettingsBand_Object = MibTableColumn
apRadioSettingsBand = _ApRadioSettingsBand_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 3),
    _ApRadioSettingsBand_Type()
)
apRadioSettingsBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsBand.setStatus("current")
_ApRadioSettingsPointersToWlans_Type = MultiPointer63
_ApRadioSettingsPointersToWlans_Object = MibTableColumn
apRadioSettingsPointersToWlans = _ApRadioSettingsPointersToWlans_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 4),
    _ApRadioSettingsPointersToWlans_Type()
)
apRadioSettingsPointersToWlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioSettingsPointersToWlans.setStatus("current")


class _ApRadioSettingsName_Type(Integer32):
    """Custom type apRadioSettingsName based on Integer32"""
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
        *(("radio802dt11a", 1),
          ("radio802dt11bg", 2),
          ("radio802dt11n2400MHz", 3),
          ("radio802dt11n5000MHz", 4))
    )


_ApRadioSettingsName_Type.__name__ = "Integer32"
_ApRadioSettingsName_Object = MibTableColumn
apRadioSettingsName = _ApRadioSettingsName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 5),
    _ApRadioSettingsName_Type()
)
apRadioSettingsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioSettingsName.setStatus("current")
_ApRadioSettingsMacAddress_Type = PhysAddress
_ApRadioSettingsMacAddress_Object = MibTableColumn
apRadioSettingsMacAddress = _ApRadioSettingsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 6),
    _ApRadioSettingsMacAddress_Type()
)
apRadioSettingsMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioSettingsMacAddress.setStatus("current")


class _ApRadioSettingsAntenna_Type(Integer32):
    """Custom type apRadioSettingsAntenna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullDiversity", 1),
          ("primaryOnly", 2),
          ("secondaryOnly", 3))
    )


_ApRadioSettingsAntenna_Type.__name__ = "Integer32"
_ApRadioSettingsAntenna_Object = MibTableColumn
apRadioSettingsAntenna = _ApRadioSettingsAntenna_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 7),
    _ApRadioSettingsAntenna_Type()
)
apRadioSettingsAntenna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsAntenna.setStatus("current")
_ApRadioSettingsShortPreamble_Type = TruthValue
_ApRadioSettingsShortPreamble_Object = MibTableColumn
apRadioSettingsShortPreamble = _ApRadioSettingsShortPreamble_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 8),
    _ApRadioSettingsShortPreamble_Type()
)
apRadioSettingsShortPreamble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsShortPreamble.setStatus("current")
_ApRadioSettingsRtsThresh_Type = Integer32
_ApRadioSettingsRtsThresh_Object = MibTableColumn
apRadioSettingsRtsThresh = _ApRadioSettingsRtsThresh_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 9),
    _ApRadioSettingsRtsThresh_Type()
)
apRadioSettingsRtsThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsRtsThresh.setStatus("current")


class _ApRadioSettingsBeaconInt_Type(Integer32):
    """Custom type apRadioSettingsBeaconInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 200),
    )


_ApRadioSettingsBeaconInt_Type.__name__ = "Integer32"
_ApRadioSettingsBeaconInt_Object = MibTableColumn
apRadioSettingsBeaconInt = _ApRadioSettingsBeaconInt_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 10),
    _ApRadioSettingsBeaconInt_Type()
)
apRadioSettingsBeaconInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsBeaconInt.setStatus("current")


class _ApRadioSettingsDtimPrd_Type(Integer32):
    """Custom type apRadioSettingsDtimPrd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_ApRadioSettingsDtimPrd_Type.__name__ = "Integer32"
_ApRadioSettingsDtimPrd_Object = MibTableColumn
apRadioSettingsDtimPrd = _ApRadioSettingsDtimPrd_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 11),
    _ApRadioSettingsDtimPrd_Type()
)
apRadioSettingsDtimPrd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsDtimPrd.setStatus("current")


class _ApRadioSettingsBasicRates_Type(Bits):
    """Custom type apRadioSettingsBasicRates based on Bits"""
    namedValues = NamedValues(
        *(("null", 0),
          ("rate11Mb", 6),
          ("rate12Mb", 7),
          ("rate18Mb", 8),
          ("rate1Mb", 1),
          ("rate22Mb", 9),
          ("rate24Mb", 10),
          ("rate2Mb", 2),
          ("rate36Mb", 11),
          ("rate48Mb", 12),
          ("rate54Mb", 13),
          ("rate5pt5Mb", 3),
          ("rate6Mb", 4),
          ("rate9Mb", 5))
    )

_ApRadioSettingsBasicRates_Type.__name__ = "Bits"
_ApRadioSettingsBasicRates_Object = MibTableColumn
apRadioSettingsBasicRates = _ApRadioSettingsBasicRates_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 12),
    _ApRadioSettingsBasicRates_Type()
)
apRadioSettingsBasicRates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsBasicRates.setStatus("current")


class _ApRadioSettingsSupportedRates_Type(Bits):
    """Custom type apRadioSettingsSupportedRates based on Bits"""
    namedValues = NamedValues(
        *(("null", 0),
          ("rate11Mb", 6),
          ("rate12Mb", 7),
          ("rate18Mb", 8),
          ("rate1Mb", 1),
          ("rate22Mb", 9),
          ("rate24Mb", 10),
          ("rate2Mb", 2),
          ("rate36Mb", 11),
          ("rate48Mb", 12),
          ("rate54Mb", 13),
          ("rate5pt5Mb", 3),
          ("rate6Mb", 4),
          ("rate9Mb", 5))
    )

_ApRadioSettingsSupportedRates_Type.__name__ = "Bits"
_ApRadioSettingsSupportedRates_Object = MibTableColumn
apRadioSettingsSupportedRates = _ApRadioSettingsSupportedRates_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 13),
    _ApRadioSettingsSupportedRates_Type()
)
apRadioSettingsSupportedRates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsSupportedRates.setStatus("current")


class _ApRadioSettingsBGMode_Type(Integer32):
    """Custom type apRadioSettingsBGMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("modeB", 3),
          ("modeBandG", 1),
          ("modeG", 2))
    )


_ApRadioSettingsBGMode_Type.__name__ = "Integer32"
_ApRadioSettingsBGMode_Object = MibTableColumn
apRadioSettingsBGMode = _ApRadioSettingsBGMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 14),
    _ApRadioSettingsBGMode_Type()
)
apRadioSettingsBGMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsBGMode.setStatus("current")
_ApRadioSettingsBackgroundMode_Type = TruthValue
_ApRadioSettingsBackgroundMode_Object = MibTableColumn
apRadioSettingsBackgroundMode = _ApRadioSettingsBackgroundMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 15),
    _ApRadioSettingsBackgroundMode_Type()
)
apRadioSettingsBackgroundMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsBackgroundMode.setStatus("obsolete")
_ApRadioSettingsBackgroundCwMin_Type = Integer32
_ApRadioSettingsBackgroundCwMin_Object = MibTableColumn
apRadioSettingsBackgroundCwMin = _ApRadioSettingsBackgroundCwMin_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 16),
    _ApRadioSettingsBackgroundCwMin_Type()
)
apRadioSettingsBackgroundCwMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsBackgroundCwMin.setStatus("current")
_ApRadioSettingsBackgroundCwMax_Type = Integer32
_ApRadioSettingsBackgroundCwMax_Object = MibTableColumn
apRadioSettingsBackgroundCwMax = _ApRadioSettingsBackgroundCwMax_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 17),
    _ApRadioSettingsBackgroundCwMax_Type()
)
apRadioSettingsBackgroundCwMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsBackgroundCwMax.setStatus("current")
_ApRadioSettingsBackgroundAifsn_Type = Integer32
_ApRadioSettingsBackgroundAifsn_Object = MibTableColumn
apRadioSettingsBackgroundAifsn = _ApRadioSettingsBackgroundAifsn_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 18),
    _ApRadioSettingsBackgroundAifsn_Type()
)
apRadioSettingsBackgroundAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsBackgroundAifsn.setStatus("current")
_ApRadioSettingsBackgroundTxopsTime_Type = Integer32
_ApRadioSettingsBackgroundTxopsTime_Object = MibTableColumn
apRadioSettingsBackgroundTxopsTime = _ApRadioSettingsBackgroundTxopsTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 19),
    _ApRadioSettingsBackgroundTxopsTime_Type()
)
apRadioSettingsBackgroundTxopsTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsBackgroundTxopsTime.setStatus("current")
_ApRadioSettingsBackgroundTxopsTimeInMS_Type = Integer32
_ApRadioSettingsBackgroundTxopsTimeInMS_Object = MibTableColumn
apRadioSettingsBackgroundTxopsTimeInMS = _ApRadioSettingsBackgroundTxopsTimeInMS_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 20),
    _ApRadioSettingsBackgroundTxopsTimeInMS_Type()
)
apRadioSettingsBackgroundTxopsTimeInMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioSettingsBackgroundTxopsTimeInMS.setStatus("current")
_ApRadioSettingsBestEffortMode_Type = TruthValue
_ApRadioSettingsBestEffortMode_Object = MibTableColumn
apRadioSettingsBestEffortMode = _ApRadioSettingsBestEffortMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 21),
    _ApRadioSettingsBestEffortMode_Type()
)
apRadioSettingsBestEffortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsBestEffortMode.setStatus("obsolete")
_ApRadioSettingsBestEffortCwMin_Type = Integer32
_ApRadioSettingsBestEffortCwMin_Object = MibTableColumn
apRadioSettingsBestEffortCwMin = _ApRadioSettingsBestEffortCwMin_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 22),
    _ApRadioSettingsBestEffortCwMin_Type()
)
apRadioSettingsBestEffortCwMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsBestEffortCwMin.setStatus("current")
_ApRadioSettingsBestEffortCwMax_Type = Integer32
_ApRadioSettingsBestEffortCwMax_Object = MibTableColumn
apRadioSettingsBestEffortCwMax = _ApRadioSettingsBestEffortCwMax_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 23),
    _ApRadioSettingsBestEffortCwMax_Type()
)
apRadioSettingsBestEffortCwMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsBestEffortCwMax.setStatus("current")
_ApRadioSettingsBestEffortAifsn_Type = Integer32
_ApRadioSettingsBestEffortAifsn_Object = MibTableColumn
apRadioSettingsBestEffortAifsn = _ApRadioSettingsBestEffortAifsn_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 24),
    _ApRadioSettingsBestEffortAifsn_Type()
)
apRadioSettingsBestEffortAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsBestEffortAifsn.setStatus("current")
_ApRadioSettingsBestEffortTxopsTime_Type = Integer32
_ApRadioSettingsBestEffortTxopsTime_Object = MibTableColumn
apRadioSettingsBestEffortTxopsTime = _ApRadioSettingsBestEffortTxopsTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 25),
    _ApRadioSettingsBestEffortTxopsTime_Type()
)
apRadioSettingsBestEffortTxopsTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsBestEffortTxopsTime.setStatus("current")
_ApRadioSettingsBestEffortTxopsTimeInMS_Type = Integer32
_ApRadioSettingsBestEffortTxopsTimeInMS_Object = MibTableColumn
apRadioSettingsBestEffortTxopsTimeInMS = _ApRadioSettingsBestEffortTxopsTimeInMS_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 26),
    _ApRadioSettingsBestEffortTxopsTimeInMS_Type()
)
apRadioSettingsBestEffortTxopsTimeInMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioSettingsBestEffortTxopsTimeInMS.setStatus("current")
_ApRadioSettingsVideoMode_Type = TruthValue
_ApRadioSettingsVideoMode_Object = MibTableColumn
apRadioSettingsVideoMode = _ApRadioSettingsVideoMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 27),
    _ApRadioSettingsVideoMode_Type()
)
apRadioSettingsVideoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsVideoMode.setStatus("obsolete")
_ApRadioSettingsVideoCwMin_Type = Integer32
_ApRadioSettingsVideoCwMin_Object = MibTableColumn
apRadioSettingsVideoCwMin = _ApRadioSettingsVideoCwMin_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 28),
    _ApRadioSettingsVideoCwMin_Type()
)
apRadioSettingsVideoCwMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsVideoCwMin.setStatus("current")
_ApRadioSettingsVideoCwMax_Type = Integer32
_ApRadioSettingsVideoCwMax_Object = MibTableColumn
apRadioSettingsVideoCwMax = _ApRadioSettingsVideoCwMax_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 29),
    _ApRadioSettingsVideoCwMax_Type()
)
apRadioSettingsVideoCwMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsVideoCwMax.setStatus("current")
_ApRadioSettingsVideoAifsn_Type = Integer32
_ApRadioSettingsVideoAifsn_Object = MibTableColumn
apRadioSettingsVideoAifsn = _ApRadioSettingsVideoAifsn_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 30),
    _ApRadioSettingsVideoAifsn_Type()
)
apRadioSettingsVideoAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsVideoAifsn.setStatus("current")
_ApRadioSettingsVideoTxopsTime_Type = Integer32
_ApRadioSettingsVideoTxopsTime_Object = MibTableColumn
apRadioSettingsVideoTxopsTime = _ApRadioSettingsVideoTxopsTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 31),
    _ApRadioSettingsVideoTxopsTime_Type()
)
apRadioSettingsVideoTxopsTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsVideoTxopsTime.setStatus("current")
_ApRadioSettingsVideoTxopsTimeInMS_Type = Integer32
_ApRadioSettingsVideoTxopsTimeInMS_Object = MibTableColumn
apRadioSettingsVideoTxopsTimeInMS = _ApRadioSettingsVideoTxopsTimeInMS_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 32),
    _ApRadioSettingsVideoTxopsTimeInMS_Type()
)
apRadioSettingsVideoTxopsTimeInMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioSettingsVideoTxopsTimeInMS.setStatus("current")
_ApRadioSettingsVoiceMode_Type = TruthValue
_ApRadioSettingsVoiceMode_Object = MibTableColumn
apRadioSettingsVoiceMode = _ApRadioSettingsVoiceMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 33),
    _ApRadioSettingsVoiceMode_Type()
)
apRadioSettingsVoiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsVoiceMode.setStatus("obsolete")
_ApRadioSettingsVoiceCwMin_Type = Integer32
_ApRadioSettingsVoiceCwMin_Object = MibTableColumn
apRadioSettingsVoiceCwMin = _ApRadioSettingsVoiceCwMin_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 34),
    _ApRadioSettingsVoiceCwMin_Type()
)
apRadioSettingsVoiceCwMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsVoiceCwMin.setStatus("current")
_ApRadioSettingsVoiceCwMax_Type = Integer32
_ApRadioSettingsVoiceCwMax_Object = MibTableColumn
apRadioSettingsVoiceCwMax = _ApRadioSettingsVoiceCwMax_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 35),
    _ApRadioSettingsVoiceCwMax_Type()
)
apRadioSettingsVoiceCwMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsVoiceCwMax.setStatus("current")
_ApRadioSettingsVoiceAifsn_Type = Integer32
_ApRadioSettingsVoiceAifsn_Object = MibTableColumn
apRadioSettingsVoiceAifsn = _ApRadioSettingsVoiceAifsn_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 36),
    _ApRadioSettingsVoiceAifsn_Type()
)
apRadioSettingsVoiceAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsVoiceAifsn.setStatus("current")
_ApRadioSettingsVoiceTxopsTime_Type = Integer32
_ApRadioSettingsVoiceTxopsTime_Object = MibTableColumn
apRadioSettingsVoiceTxopsTime = _ApRadioSettingsVoiceTxopsTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 37),
    _ApRadioSettingsVoiceTxopsTime_Type()
)
apRadioSettingsVoiceTxopsTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsVoiceTxopsTime.setStatus("current")
_ApRadioSettingsVoiceTxopsTimeInMS_Type = Integer32
_ApRadioSettingsVoiceTxopsTimeInMS_Object = MibTableColumn
apRadioSettingsVoiceTxopsTimeInMS = _ApRadioSettingsVoiceTxopsTimeInMS_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 38),
    _ApRadioSettingsVoiceTxopsTimeInMS_Type()
)
apRadioSettingsVoiceTxopsTimeInMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioSettingsVoiceTxopsTimeInMS.setStatus("current")
_ApRadioSettingsE2BMapMessage_Type = DisplayString
_ApRadioSettingsE2BMapMessage_Object = MibTableColumn
apRadioSettingsE2BMapMessage = _ApRadioSettingsE2BMapMessage_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 39),
    _ApRadioSettingsE2BMapMessage_Type()
)
apRadioSettingsE2BMapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioSettingsE2BMapMessage.setStatus("current")
_ApRadioSettingsERPProtectionStatus_Type = TruthValue
_ApRadioSettingsERPProtectionStatus_Object = MibTableColumn
apRadioSettingsERPProtectionStatus = _ApRadioSettingsERPProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 40),
    _ApRadioSettingsERPProtectionStatus_Type()
)
apRadioSettingsERPProtectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioSettingsERPProtectionStatus.setStatus("current")


class _ApRadioSettingsWMMQosParam_Type(Integer32):
    """Custom type apRadioSettingsWMMQosParam based on Integer32"""
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
        *(("default11agn", 4),
          ("default11b", 5),
          ("manual", 1),
          ("voice11agn", 6),
          ("voice11b", 7),
          ("wifi11agn", 2),
          ("wifi11b", 3))
    )


_ApRadioSettingsWMMQosParam_Type.__name__ = "Integer32"
_ApRadioSettingsWMMQosParam_Object = MibTableColumn
apRadioSettingsWMMQosParam = _ApRadioSettingsWMMQosParam_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 41),
    _ApRadioSettingsWMMQosParam_Type()
)
apRadioSettingsWMMQosParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsWMMQosParam.setStatus("current")


class _ApRadioSettingsQBSSChannelBeaconInt_Type(Integer32):
    """Custom type apRadioSettingsQBSSChannelBeaconInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 200),
    )


_ApRadioSettingsQBSSChannelBeaconInt_Type.__name__ = "Integer32"
_ApRadioSettingsQBSSChannelBeaconInt_Object = MibTableColumn
apRadioSettingsQBSSChannelBeaconInt = _ApRadioSettingsQBSSChannelBeaconInt_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 42),
    _ApRadioSettingsQBSSChannelBeaconInt_Type()
)
apRadioSettingsQBSSChannelBeaconInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsQBSSChannelBeaconInt.setStatus("current")


class _ApRadioSettingsQBSSLoadElementMode_Type(Integer32):
    """Custom type apRadioSettingsQBSSLoadElementMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApRadioSettingsQBSSLoadElementMode_Type.__name__ = "Integer32"
_ApRadioSettingsQBSSLoadElementMode_Object = MibTableColumn
apRadioSettingsQBSSLoadElementMode = _ApRadioSettingsQBSSLoadElementMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 1, 1, 43),
    _ApRadioSettingsQBSSLoadElementMode_Type()
)
apRadioSettingsQBSSLoadElementMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSettingsQBSSLoadElementMode.setStatus("current")
_ApRadioCfgTable_Object = MibTable
apRadioCfgTable = _ApRadioCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 2)
)
if mibBuilder.loadTexts:
    apRadioCfgTable.setStatus("current")
_ApRadioCfgEntry_Object = MibTableRow
apRadioCfgEntry = _ApRadioCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 2, 1)
)
apRadioCfgEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apRadioSettingsIndex"),
)
if mibBuilder.loadTexts:
    apRadioCfgEntry.setStatus("current")


class _ApRadioCfgChannelMode_Type(Integer32):
    """Custom type apRadioCfgChannelMode based on Integer32"""
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
        *(("autoSelect", 2),
          ("autoSelect40", 4),
          ("uniformSpreading", 3),
          ("uniformSpreading40", 5),
          ("userSelect", 1))
    )


_ApRadioCfgChannelMode_Type.__name__ = "Integer32"
_ApRadioCfgChannelMode_Object = MibTableColumn
apRadioCfgChannelMode = _ApRadioCfgChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 2, 1, 1),
    _ApRadioCfgChannelMode_Type()
)
apRadioCfgChannelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioCfgChannelMode.setStatus("current")


class _ApRadioCfgDesPlacement_Type(Integer32):
    """Custom type apRadioCfgDesPlacement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("indoor", 1),
          ("outdoor", 2))
    )


_ApRadioCfgDesPlacement_Type.__name__ = "Integer32"
_ApRadioCfgDesPlacement_Object = MibTableColumn
apRadioCfgDesPlacement = _ApRadioCfgDesPlacement_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 2, 1, 2),
    _ApRadioCfgDesPlacement_Type()
)
apRadioCfgDesPlacement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioCfgDesPlacement.setStatus("current")


class _ApRadioCfgPosChannel_Type(Bits):
    """Custom type apRadioCfgPosChannel based on Bits"""
    namedValues = NamedValues(
        *(("achannel149", 23),
          ("achannel153", 24),
          ("achannel157", 25),
          ("achannel161", 26),
          ("achannel165", 27),
          ("achannel36", 15),
          ("achannel40", 16),
          ("achannel44", 17),
          ("achannel48", 18),
          ("achannel52", 19),
          ("achannel56", 20),
          ("achannel60", 21),
          ("achannel64", 22),
          ("bchannel01", 1),
          ("bchannel02", 2),
          ("bchannel03", 3),
          ("bchannel04", 4),
          ("bchannel05", 5),
          ("bchannel06", 6),
          ("bchannel07", 7),
          ("bchannel08", 8),
          ("bchannel09", 9),
          ("bchannel10", 10),
          ("bchannel11", 11),
          ("bchannel12", 12),
          ("bchannel13", 13),
          ("bchannel14", 14),
          ("null", 0))
    )

_ApRadioCfgPosChannel_Type.__name__ = "Bits"
_ApRadioCfgPosChannel_Object = MibTableColumn
apRadioCfgPosChannel = _ApRadioCfgPosChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 2, 1, 3),
    _ApRadioCfgPosChannel_Type()
)
apRadioCfgPosChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioCfgPosChannel.setStatus("current")


class _ApRadioCfgDesChannel_Type(Integer32):
    """Custom type apRadioCfgDesChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              36,
              40,
              44,
              48,
              52,
              56,
              60,
              64,
              149,
              153,
              157,
              161,
              165)
        )
    )
    namedValues = NamedValues(
        *(("achannel149", 149),
          ("achannel153", 153),
          ("achannel157", 157),
          ("achannel161", 161),
          ("achannel165", 165),
          ("achannel36", 36),
          ("achannel40", 40),
          ("achannel44", 44),
          ("achannel48", 48),
          ("achannel52", 52),
          ("achannel56", 56),
          ("achannel60", 60),
          ("achannel64", 64),
          ("bchannel01", 1),
          ("bchannel02", 2),
          ("bchannel03", 3),
          ("bchannel04", 4),
          ("bchannel05", 5),
          ("bchannel06", 6),
          ("bchannel07", 7),
          ("bchannel08", 8),
          ("bchannel09", 9),
          ("bchannel10", 10),
          ("bchannel11", 11),
          ("bchannel12", 12),
          ("bchannel13", 13),
          ("bchannel14", 14),
          ("null", 0))
    )


_ApRadioCfgDesChannel_Type.__name__ = "Integer32"
_ApRadioCfgDesChannel_Object = MibTableColumn
apRadioCfgDesChannel = _ApRadioCfgDesChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 2, 1, 4),
    _ApRadioCfgDesChannel_Type()
)
apRadioCfgDesChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioCfgDesChannel.setStatus("current")
_ApRadioCfgPosPowerLevel_Type = Integer32
_ApRadioCfgPosPowerLevel_Object = MibTableColumn
apRadioCfgPosPowerLevel = _ApRadioCfgPosPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 2, 1, 5),
    _ApRadioCfgPosPowerLevel_Type()
)
apRadioCfgPosPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioCfgPosPowerLevel.setStatus("current")


class _ApRadioCfgDesPowerLevel_Type(Integer32):
    """Custom type apRadioCfgDesPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 20),
    )


_ApRadioCfgDesPowerLevel_Type.__name__ = "Integer32"
_ApRadioCfgDesPowerLevel_Object = MibTableColumn
apRadioCfgDesPowerLevel = _ApRadioCfgDesPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 2, 1, 6),
    _ApRadioCfgDesPowerLevel_Type()
)
apRadioCfgDesPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioCfgDesPowerLevel.setStatus("current")
_ApRadioCfgDesPowerInMW_Type = Integer32
_ApRadioCfgDesPowerInMW_Object = MibTableColumn
apRadioCfgDesPowerInMW = _ApRadioCfgDesPowerInMW_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 2, 1, 7),
    _ApRadioCfgDesPowerInMW_Type()
)
apRadioCfgDesPowerInMW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioCfgDesPowerInMW.setStatus("current")
_ApRadioCfgSet_Type = DoActionShowProgress
_ApRadioCfgSet_Object = MibTableColumn
apRadioCfgSet = _ApRadioCfgSet_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 2, 1, 8),
    _ApRadioCfgSet_Type()
)
apRadioCfgSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioCfgSet.setStatus("current")
_ApRadioCfgReset_Type = DoActionShowProgress
_ApRadioCfgReset_Object = MibTableColumn
apRadioCfgReset = _ApRadioCfgReset_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 2, 1, 9),
    _ApRadioCfgReset_Type()
)
apRadioCfgReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioCfgReset.setStatus("current")


class _ApRadioCfgPlacement_Type(Integer32):
    """Custom type apRadioCfgPlacement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("indoor", 1),
          ("outdoor", 2))
    )


_ApRadioCfgPlacement_Type.__name__ = "Integer32"
_ApRadioCfgPlacement_Object = MibTableColumn
apRadioCfgPlacement = _ApRadioCfgPlacement_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 2, 1, 10),
    _ApRadioCfgPlacement_Type()
)
apRadioCfgPlacement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioCfgPlacement.setStatus("current")


class _ApRadioCfgChannel_Type(Integer32):
    """Custom type apRadioCfgChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              36,
              40,
              44,
              48,
              52,
              56,
              60,
              64,
              149,
              153,
              157,
              161,
              165)
        )
    )
    namedValues = NamedValues(
        *(("achannel149", 149),
          ("achannel153", 153),
          ("achannel157", 157),
          ("achannel161", 161),
          ("achannel165", 165),
          ("achannel36", 36),
          ("achannel40", 40),
          ("achannel44", 44),
          ("achannel48", 48),
          ("achannel52", 52),
          ("achannel56", 56),
          ("achannel60", 60),
          ("achannel64", 64),
          ("bchannel01", 1),
          ("bchannel02", 2),
          ("bchannel03", 3),
          ("bchannel04", 4),
          ("bchannel05", 5),
          ("bchannel06", 6),
          ("bchannel07", 7),
          ("bchannel08", 8),
          ("bchannel09", 9),
          ("bchannel10", 10),
          ("bchannel11", 11),
          ("null", 0))
    )


_ApRadioCfgChannel_Type.__name__ = "Integer32"
_ApRadioCfgChannel_Object = MibTableColumn
apRadioCfgChannel = _ApRadioCfgChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 2, 1, 11),
    _ApRadioCfgChannel_Type()
)
apRadioCfgChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioCfgChannel.setStatus("current")
_ApRadioCfgPowerLevel_Type = Integer32
_ApRadioCfgPowerLevel_Object = MibTableColumn
apRadioCfgPowerLevel = _ApRadioCfgPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 2, 1, 12),
    _ApRadioCfgPowerLevel_Type()
)
apRadioCfgPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioCfgPowerLevel.setStatus("current")
_ApRadioCfgPowerInMW_Type = Integer32
_ApRadioCfgPowerInMW_Object = MibTableColumn
apRadioCfgPowerInMW = _ApRadioCfgPowerInMW_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 2, 1, 13),
    _ApRadioCfgPowerInMW_Type()
)
apRadioCfgPowerInMW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioCfgPowerInMW.setStatus("current")


class _ApRadioCfgRfFunction_Type(Integer32):
    """Custom type apRadioCfgRfFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wips", 2),
          ("wlan", 1))
    )


_ApRadioCfgRfFunction_Type.__name__ = "Integer32"
_ApRadioCfgRfFunction_Object = MibTableColumn
apRadioCfgRfFunction = _ApRadioCfgRfFunction_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 2, 1, 14),
    _ApRadioCfgRfFunction_Type()
)
apRadioCfgRfFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioCfgRfFunction.setStatus("current")


class _ApRadioCfgExceptionChannel_Type(Bits):
    """Custom type apRadioCfgExceptionChannel based on Bits"""
    namedValues = NamedValues(
        *(("achannel149", 23),
          ("achannel153", 24),
          ("achannel157", 25),
          ("achannel161", 26),
          ("achannel165", 27),
          ("achannel36", 15),
          ("achannel40", 16),
          ("achannel44", 17),
          ("achannel48", 18),
          ("achannel52", 19),
          ("achannel56", 20),
          ("achannel60", 21),
          ("achannel64", 22),
          ("bchannel01", 1),
          ("bchannel02", 2),
          ("bchannel03", 3),
          ("bchannel04", 4),
          ("bchannel05", 5),
          ("bchannel06", 6),
          ("bchannel07", 7),
          ("bchannel08", 8),
          ("bchannel09", 9),
          ("bchannel10", 10),
          ("bchannel11", 11),
          ("bchannel12", 12),
          ("bchannel13", 13),
          ("bchannel14", 14),
          ("null", 0))
    )

_ApRadioCfgExceptionChannel_Type.__name__ = "Bits"
_ApRadioCfgExceptionChannel_Object = MibTableColumn
apRadioCfgExceptionChannel = _ApRadioCfgExceptionChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 2, 1, 15),
    _ApRadioCfgExceptionChannel_Type()
)
apRadioCfgExceptionChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioCfgExceptionChannel.setStatus("current")
_ApRadioWlanBssTable_Object = MibTable
apRadioWlanBssTable = _ApRadioWlanBssTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 3)
)
if mibBuilder.loadTexts:
    apRadioWlanBssTable.setStatus("current")
_ApRadioWlanBssEntry_Object = MibTableRow
apRadioWlanBssEntry = _ApRadioWlanBssEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 3, 1)
)
apRadioWlanBssEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apRadioSettingsIndex"),
    (0, "SYMBOL-AP-MIB", "apWlanIndex"),
)
if mibBuilder.loadTexts:
    apRadioWlanBssEntry.setStatus("current")
_ApRadioWlanBssid_Type = Integer32
_ApRadioWlanBssid_Object = MibTableColumn
apRadioWlanBssid = _ApRadioWlanBssid_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 3, 1, 1),
    _ApRadioWlanBssid_Type()
)
apRadioWlanBssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioWlanBssid.setStatus("current")
_ApRadioBssTable_Object = MibTable
apRadioBssTable = _ApRadioBssTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 4)
)
if mibBuilder.loadTexts:
    apRadioBssTable.setStatus("current")
_ApRadioBssEntry_Object = MibTableRow
apRadioBssEntry = _ApRadioBssEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 4, 1)
)
apRadioBssEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apRadioSettingsIndex"),
    (0, "SYMBOL-AP-MIB", "apRadioBssIndex"),
)
if mibBuilder.loadTexts:
    apRadioBssEntry.setStatus("current")


class _ApRadioBssIndex_Type(Integer32):
    """Custom type apRadioBssIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ApRadioBssIndex_Type.__name__ = "Integer32"
_ApRadioBssIndex_Object = MibTableColumn
apRadioBssIndex = _ApRadioBssIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 4, 1, 1),
    _ApRadioBssIndex_Type()
)
apRadioBssIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apRadioBssIndex.setStatus("current")


class _ApRadioBssPrimaryWlan_Type(Integer32):
    """Custom type apRadioBssPrimaryWlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ApRadioBssPrimaryWlan_Type.__name__ = "Integer32"
_ApRadioBssPrimaryWlan_Object = MibTableColumn
apRadioBssPrimaryWlan = _ApRadioBssPrimaryWlan_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 4, 1, 2),
    _ApRadioBssPrimaryWlan_Type()
)
apRadioBssPrimaryWlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioBssPrimaryWlan.setStatus("current")


class _ApRadioBssDtimPrd_Type(Integer32):
    """Custom type apRadioBssDtimPrd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_ApRadioBssDtimPrd_Type.__name__ = "Integer32"
_ApRadioBssDtimPrd_Object = MibTableColumn
apRadioBssDtimPrd = _ApRadioBssDtimPrd_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 4, 1, 3),
    _ApRadioBssDtimPrd_Type()
)
apRadioBssDtimPrd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioBssDtimPrd.setStatus("current")
_ApRadioE2BMapStatusTable_Object = MibTable
apRadioE2BMapStatusTable = _ApRadioE2BMapStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 5)
)
if mibBuilder.loadTexts:
    apRadioE2BMapStatusTable.setStatus("current")
_ApRadioE2BMapStatusEntry_Object = MibTableRow
apRadioE2BMapStatusEntry = _ApRadioE2BMapStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 5, 1)
)
apRadioE2BMapStatusEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apRadioSettingsIndex"),
    (0, "SYMBOL-AP-MIB", "apWlanIndex"),
)
if mibBuilder.loadTexts:
    apRadioE2BMapStatusEntry.setStatus("current")


class _ApRadioE2BMapStatusBcMcEncCipher_Type(Integer32):
    """Custom type apRadioE2BMapStatusBcMcEncCipher based on Integer32"""
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
        *(("keyguard", 4),
          ("open", 1),
          ("wep128", 3),
          ("wep64", 2),
          ("wpa2Ccmp", 6),
          ("wpaTkip", 5))
    )


_ApRadioE2BMapStatusBcMcEncCipher_Type.__name__ = "Integer32"
_ApRadioE2BMapStatusBcMcEncCipher_Object = MibTableColumn
apRadioE2BMapStatusBcMcEncCipher = _ApRadioE2BMapStatusBcMcEncCipher_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 5, 1, 1),
    _ApRadioE2BMapStatusBcMcEncCipher_Type()
)
apRadioE2BMapStatusBcMcEncCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioE2BMapStatusBcMcEncCipher.setStatus("current")


class _ApRadioE2BMapStatus_Type(Integer32):
    """Custom type apRadioE2BMapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 3),
          ("good", 1),
          ("warning", 2))
    )


_ApRadioE2BMapStatus_Type.__name__ = "Integer32"
_ApRadioE2BMapStatus_Object = MibTableColumn
apRadioE2BMapStatus = _ApRadioE2BMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 5, 1, 2),
    _ApRadioE2BMapStatus_Type()
)
apRadioE2BMapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioE2BMapStatus.setStatus("current")
_ApRadioE2BMapStatusMessage_Type = DisplayString
_ApRadioE2BMapStatusMessage_Object = MibTableColumn
apRadioE2BMapStatusMessage = _ApRadioE2BMapStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 5, 1, 3),
    _ApRadioE2BMapStatusMessage_Type()
)
apRadioE2BMapStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioE2BMapStatusMessage.setStatus("current")
_ApRadioMesh_ObjectIdentity = ObjectIdentity
apRadioMesh = _ApRadioMesh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 6)
)
_ApRadioMeshTable_Object = MibTable
apRadioMeshTable = _ApRadioMeshTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 6, 1)
)
if mibBuilder.loadTexts:
    apRadioMeshTable.setStatus("current")
_ApRadioMeshEntry_Object = MibTableRow
apRadioMeshEntry = _ApRadioMeshEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 6, 1, 1)
)
apRadioMeshEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apRadioSettingsIndex"),
)
if mibBuilder.loadTexts:
    apRadioMeshEntry.setStatus("current")
_ApRadioMeshBaseBridgeMode_Type = TruthValue
_ApRadioMeshBaseBridgeMode_Object = MibTableColumn
apRadioMeshBaseBridgeMode = _ApRadioMeshBaseBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 6, 1, 1, 1),
    _ApRadioMeshBaseBridgeMode_Type()
)
apRadioMeshBaseBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioMeshBaseBridgeMode.setStatus("current")


class _ApRadioMeshMaxClients_Type(Integer32):
    """Custom type apRadioMeshMaxClients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ApRadioMeshMaxClients_Type.__name__ = "Integer32"
_ApRadioMeshMaxClients_Object = MibTableColumn
apRadioMeshMaxClients = _ApRadioMeshMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 6, 1, 1, 2),
    _ApRadioMeshMaxClients_Type()
)
apRadioMeshMaxClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioMeshMaxClients.setStatus("current")
_ApRadioMeshClientBridgeMode_Type = TruthValue
_ApRadioMeshClientBridgeMode_Object = MibTableColumn
apRadioMeshClientBridgeMode = _ApRadioMeshClientBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 6, 1, 1, 3),
    _ApRadioMeshClientBridgeMode_Type()
)
apRadioMeshClientBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioMeshClientBridgeMode.setStatus("current")


class _ApRadioMeshWlanPtr_Type(SinglePointer):
    """Custom type apRadioMeshWlanPtr based on SinglePointer"""
    subtypeSpec = SinglePointer.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ApRadioMeshWlanPtr_Type.__name__ = "SinglePointer"
_ApRadioMeshWlanPtr_Object = MibTableColumn
apRadioMeshWlanPtr = _ApRadioMeshWlanPtr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 6, 1, 1, 4),
    _ApRadioMeshWlanPtr_Type()
)
apRadioMeshWlanPtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioMeshWlanPtr.setStatus("current")
_ApRadioMeshConnAutoSelect_Type = TruthValue
_ApRadioMeshConnAutoSelect_Object = MibTableColumn
apRadioMeshConnAutoSelect = _ApRadioMeshConnAutoSelect_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 6, 1, 1, 5),
    _ApRadioMeshConnAutoSelect_Type()
)
apRadioMeshConnAutoSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioMeshConnAutoSelect.setStatus("current")


class _ApRadioMeshTimeout_Type(Integer32):
    """Custom type apRadioMeshTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 2),
          ("uplinkDetect", 1))
    )


_ApRadioMeshTimeout_Type.__name__ = "Integer32"
_ApRadioMeshTimeout_Object = MibTableColumn
apRadioMeshTimeout = _ApRadioMeshTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 6, 1, 1, 6),
    _ApRadioMeshTimeout_Type()
)
apRadioMeshTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioMeshTimeout.setStatus("current")


class _ApRadioMeshTimeoutValue_Type(Integer32):
    """Custom type apRadioMeshTimeoutValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(45, 65535),
    )


_ApRadioMeshTimeoutValue_Type.__name__ = "Integer32"
_ApRadioMeshTimeoutValue_Object = MibTableColumn
apRadioMeshTimeoutValue = _ApRadioMeshTimeoutValue_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 6, 1, 1, 7),
    _ApRadioMeshTimeoutValue_Type()
)
apRadioMeshTimeoutValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioMeshTimeoutValue.setStatus("current")
_ApRadioMeshAvailableConnTable_Object = MibTable
apRadioMeshAvailableConnTable = _ApRadioMeshAvailableConnTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 6, 2)
)
if mibBuilder.loadTexts:
    apRadioMeshAvailableConnTable.setStatus("current")
_ApRadioMeshAvailableConnEntry_Object = MibTableRow
apRadioMeshAvailableConnEntry = _ApRadioMeshAvailableConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 6, 2, 1)
)
apRadioMeshAvailableConnEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apRadioSettingsIndex"),
    (0, "SYMBOL-AP-MIB", "apRadioMeshAvailableConnIndex"),
)
if mibBuilder.loadTexts:
    apRadioMeshAvailableConnEntry.setStatus("current")


class _ApRadioMeshAvailableConnIndex_Type(Integer32):
    """Custom type apRadioMeshAvailableConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ApRadioMeshAvailableConnIndex_Type.__name__ = "Integer32"
_ApRadioMeshAvailableConnIndex_Object = MibTableColumn
apRadioMeshAvailableConnIndex = _ApRadioMeshAvailableConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 6, 2, 1, 1),
    _ApRadioMeshAvailableConnIndex_Type()
)
apRadioMeshAvailableConnIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apRadioMeshAvailableConnIndex.setStatus("current")
_ApRadioMeshAvailableConnMac_Type = PhysAddress
_ApRadioMeshAvailableConnMac_Object = MibTableColumn
apRadioMeshAvailableConnMac = _ApRadioMeshAvailableConnMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 6, 2, 1, 2),
    _ApRadioMeshAvailableConnMac_Type()
)
apRadioMeshAvailableConnMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioMeshAvailableConnMac.setStatus("current")
_ApRadioMeshAvailableConnChannel_Type = Integer32
_ApRadioMeshAvailableConnChannel_Object = MibTableColumn
apRadioMeshAvailableConnChannel = _ApRadioMeshAvailableConnChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 6, 2, 1, 3),
    _ApRadioMeshAvailableConnChannel_Type()
)
apRadioMeshAvailableConnChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioMeshAvailableConnChannel.setStatus("current")
_ApRadioMeshAvailableConnRssi_Type = Integer32
_ApRadioMeshAvailableConnRssi_Object = MibTableColumn
apRadioMeshAvailableConnRssi = _ApRadioMeshAvailableConnRssi_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 6, 2, 1, 4),
    _ApRadioMeshAvailableConnRssi_Type()
)
apRadioMeshAvailableConnRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioMeshAvailableConnRssi.setStatus("current")
_ApRadioMeshPreferredConnTable_Object = MibTable
apRadioMeshPreferredConnTable = _ApRadioMeshPreferredConnTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 6, 3)
)
if mibBuilder.loadTexts:
    apRadioMeshPreferredConnTable.setStatus("current")
_ApRadioMeshPreferredConnEntry_Object = MibTableRow
apRadioMeshPreferredConnEntry = _ApRadioMeshPreferredConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 6, 3, 1)
)
apRadioMeshPreferredConnEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apRadioSettingsIndex"),
    (0, "SYMBOL-AP-MIB", "apRadioMeshPreferredConnIndex"),
)
if mibBuilder.loadTexts:
    apRadioMeshPreferredConnEntry.setStatus("current")


class _ApRadioMeshPreferredConnIndex_Type(Integer32):
    """Custom type apRadioMeshPreferredConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ApRadioMeshPreferredConnIndex_Type.__name__ = "Integer32"
_ApRadioMeshPreferredConnIndex_Object = MibTableColumn
apRadioMeshPreferredConnIndex = _ApRadioMeshPreferredConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 6, 3, 1, 1),
    _ApRadioMeshPreferredConnIndex_Type()
)
apRadioMeshPreferredConnIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apRadioMeshPreferredConnIndex.setStatus("current")
_ApRadioMeshPreferredConnPriority_Type = Integer32
_ApRadioMeshPreferredConnPriority_Object = MibTableColumn
apRadioMeshPreferredConnPriority = _ApRadioMeshPreferredConnPriority_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 6, 3, 1, 2),
    _ApRadioMeshPreferredConnPriority_Type()
)
apRadioMeshPreferredConnPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioMeshPreferredConnPriority.setStatus("current")
_ApRadioMeshPreferredConnMac_Type = PhysAddress
_ApRadioMeshPreferredConnMac_Object = MibTableColumn
apRadioMeshPreferredConnMac = _ApRadioMeshPreferredConnMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 6, 3, 1, 3),
    _ApRadioMeshPreferredConnMac_Type()
)
apRadioMeshPreferredConnMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioMeshPreferredConnMac.setStatus("current")
_ApRadioMeshPreferredConnRowStatus_Type = AbbrevRowStatus
_ApRadioMeshPreferredConnRowStatus_Object = MibTableColumn
apRadioMeshPreferredConnRowStatus = _ApRadioMeshPreferredConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 6, 3, 1, 4),
    _ApRadioMeshPreferredConnRowStatus_Type()
)
apRadioMeshPreferredConnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioMeshPreferredConnRowStatus.setStatus("current")
_ApRadioWlanBandwidthTable_Object = MibTable
apRadioWlanBandwidthTable = _ApRadioWlanBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 7)
)
if mibBuilder.loadTexts:
    apRadioWlanBandwidthTable.setStatus("current")
_ApRadioWlanBandwidthEntry_Object = MibTableRow
apRadioWlanBandwidthEntry = _ApRadioWlanBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 7, 1)
)
apRadioWlanBandwidthEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apRadioSettingsIndex"),
    (0, "SYMBOL-AP-MIB", "apWlanIndex"),
)
if mibBuilder.loadTexts:
    apRadioWlanBandwidthEntry.setStatus("current")
_ApRadioWlanWeight_Type = Integer32
_ApRadioWlanWeight_Object = MibTableColumn
apRadioWlanWeight = _ApRadioWlanWeight_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 7, 1, 1),
    _ApRadioWlanWeight_Type()
)
apRadioWlanWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioWlanWeight.setStatus("current")
_ApRadioNSettingsTable_Object = MibTable
apRadioNSettingsTable = _ApRadioNSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 8)
)
if mibBuilder.loadTexts:
    apRadioNSettingsTable.setStatus("current")
_ApRadioNSettingsEntry_Object = MibTableRow
apRadioNSettingsEntry = _ApRadioNSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 8, 1)
)
apRadioNSettingsEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apRadioSettingsIndex"),
)
if mibBuilder.loadTexts:
    apRadioNSettingsEntry.setStatus("current")


class _ApRadioNSettingsMode_Type(Integer32):
    """Custom type apRadioNSettingsMode based on Integer32"""
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
        *(("modeA", 1),
          ("modeAandN", 6),
          ("modeB", 2),
          ("modeBGandN", 9),
          ("modeBandG", 7),
          ("modeG", 3),
          ("modeGandN", 8),
          ("modeN2400MHz", 4),
          ("modeN5000MHz", 5))
    )


_ApRadioNSettingsMode_Type.__name__ = "Integer32"
_ApRadioNSettingsMode_Object = MibTableColumn
apRadioNSettingsMode = _ApRadioNSettingsMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 8, 1, 1),
    _ApRadioNSettingsMode_Type()
)
apRadioNSettingsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioNSettingsMode.setStatus("current")


class _ApRadioNSettingsHTProtectionStatus_Type(Integer32):
    """Custom type apRadioNSettingsHTProtectionStatus based on Integer32"""
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
        *(("htWith20MHzOnlySta", 3),
          ("nonHtStaAssociated", 4),
          ("nonHtStaOnChannel", 2),
          ("pureHt", 1))
    )


_ApRadioNSettingsHTProtectionStatus_Type.__name__ = "Integer32"
_ApRadioNSettingsHTProtectionStatus_Object = MibTableColumn
apRadioNSettingsHTProtectionStatus = _ApRadioNSettingsHTProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 8, 1, 2),
    _ApRadioNSettingsHTProtectionStatus_Type()
)
apRadioNSettingsHTProtectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioNSettingsHTProtectionStatus.setStatus("current")


class _ApRadioNSettingsBasicRates_Type(Integer32):
    """Custom type apRadioNSettingsBasicRates based on Integer32"""
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
        *(("rate1and2Mbps", 1),
          ("rate1and2and5point5and11Mbps", 2),
          ("rate1and2and5point5and11and6and12and24Mbps", 3),
          ("rate1and2and5point5and11and6and12and24MbpsandMCS0to7", 7),
          ("rate6and12and24Mbps", 4),
          ("rate6and12and24MbpsandMCS0to7", 6),
          ("rateMCS0to7", 5))
    )


_ApRadioNSettingsBasicRates_Type.__name__ = "Integer32"
_ApRadioNSettingsBasicRates_Object = MibTableColumn
apRadioNSettingsBasicRates = _ApRadioNSettingsBasicRates_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 8, 1, 3),
    _ApRadioNSettingsBasicRates_Type()
)
apRadioNSettingsBasicRates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioNSettingsBasicRates.setStatus("current")
_ApRadioNCfgTable_Object = MibTable
apRadioNCfgTable = _ApRadioNCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 9)
)
if mibBuilder.loadTexts:
    apRadioNCfgTable.setStatus("current")
_ApRadioNCfgEntry_Object = MibTableRow
apRadioNCfgEntry = _ApRadioNCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 9, 1)
)
apRadioNCfgEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apRadioSettingsIndex"),
)
if mibBuilder.loadTexts:
    apRadioNCfgEntry.setStatus("current")


class _ApRadioNCfgPosChannel_Type(Bits):
    """Custom type apRadioNCfgPosChannel based on Bits"""
    namedValues = NamedValues(
        *(("anChannel100", 23),
          ("anChannel104", 24),
          ("anChannel108", 25),
          ("anChannel112", 26),
          ("anChannel116", 27),
          ("anChannel120", 28),
          ("anChannel124", 29),
          ("anChannel128", 30),
          ("anChannel132", 31),
          ("anChannel136", 32),
          ("anChannel140", 33),
          ("anChannel149", 34),
          ("anChannel153", 35),
          ("anChannel157", 36),
          ("anChannel161", 37),
          ("anChannel165", 38),
          ("anChannel36", 15),
          ("anChannel40", 16),
          ("anChannel44", 17),
          ("anChannel48", 18),
          ("anChannel52", 19),
          ("anChannel56", 20),
          ("anChannel60", 21),
          ("anChannel64", 22),
          ("bgnChannel1", 1),
          ("bgnChannel10", 10),
          ("bgnChannel11", 11),
          ("bgnChannel12", 12),
          ("bgnChannel13", 13),
          ("bgnChannel14", 14),
          ("bgnChannel2", 2),
          ("bgnChannel3", 3),
          ("bgnChannel4", 4),
          ("bgnChannel5", 5),
          ("bgnChannel6", 6),
          ("bgnChannel7", 7),
          ("bgnChannel8", 8),
          ("bgnChannel9", 9),
          ("null", 0))
    )

_ApRadioNCfgPosChannel_Type.__name__ = "Bits"
_ApRadioNCfgPosChannel_Object = MibTableColumn
apRadioNCfgPosChannel = _ApRadioNCfgPosChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 9, 1, 1),
    _ApRadioNCfgPosChannel_Type()
)
apRadioNCfgPosChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioNCfgPosChannel.setStatus("current")
_ApRadioNCfgDesChannel_Type = AllowedChannels
_ApRadioNCfgDesChannel_Object = MibTableColumn
apRadioNCfgDesChannel = _ApRadioNCfgDesChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 9, 1, 2),
    _ApRadioNCfgDesChannel_Type()
)
apRadioNCfgDesChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioNCfgDesChannel.setStatus("current")
_ApRadioNCfgChannel_Type = Integer32
_ApRadioNCfgChannel_Object = MibTableColumn
apRadioNCfgChannel = _ApRadioNCfgChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 9, 1, 3),
    _ApRadioNCfgChannel_Type()
)
apRadioNCfgChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioNCfgChannel.setStatus("current")


class _ApRadioNCfgChannelWidth_Type(Integer32):
    """Custom type apRadioNCfgChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("twentyMHz", 1))
    )


_ApRadioNCfgChannelWidth_Type.__name__ = "Integer32"
_ApRadioNCfgChannelWidth_Object = MibTableColumn
apRadioNCfgChannelWidth = _ApRadioNCfgChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 9, 1, 4),
    _ApRadioNCfgChannelWidth_Type()
)
apRadioNCfgChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioNCfgChannelWidth.setStatus("current")


class _ApRadioNCfgAmsduAggregationMaxRecvSize_Type(Integer32):
    """Custom type apRadioNCfgAmsduAggregationMaxRecvSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3839
        )
    )
    namedValues = NamedValues(
        ("size3839", 3839)
    )


_ApRadioNCfgAmsduAggregationMaxRecvSize_Type.__name__ = "Integer32"
_ApRadioNCfgAmsduAggregationMaxRecvSize_Object = MibTableColumn
apRadioNCfgAmsduAggregationMaxRecvSize = _ApRadioNCfgAmsduAggregationMaxRecvSize_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 9, 1, 5),
    _ApRadioNCfgAmsduAggregationMaxRecvSize_Type()
)
apRadioNCfgAmsduAggregationMaxRecvSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioNCfgAmsduAggregationMaxRecvSize.setStatus("current")
if mibBuilder.loadTexts:
    apRadioNCfgAmsduAggregationMaxRecvSize.setUnits("bytes")
_ApRadioNCfgAmsduTransmitEnabled_Type = TruthValue
_ApRadioNCfgAmsduTransmitEnabled_Object = MibTableColumn
apRadioNCfgAmsduTransmitEnabled = _ApRadioNCfgAmsduTransmitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 9, 1, 6),
    _ApRadioNCfgAmsduTransmitEnabled_Type()
)
apRadioNCfgAmsduTransmitEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioNCfgAmsduTransmitEnabled.setStatus("current")


class _ApRadioNCfgAmpduAggregationMaxRecvSize_Type(Integer32):
    """Custom type apRadioNCfgAmpduAggregationMaxRecvSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8191,
              16383,
              32767,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("size0", 0),
          ("size16383", 16383),
          ("size32767", 32767),
          ("size65535", 65535),
          ("size8191", 8191))
    )


_ApRadioNCfgAmpduAggregationMaxRecvSize_Type.__name__ = "Integer32"
_ApRadioNCfgAmpduAggregationMaxRecvSize_Object = MibTableColumn
apRadioNCfgAmpduAggregationMaxRecvSize = _ApRadioNCfgAmpduAggregationMaxRecvSize_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 9, 1, 7),
    _ApRadioNCfgAmpduAggregationMaxRecvSize_Type()
)
apRadioNCfgAmpduAggregationMaxRecvSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioNCfgAmpduAggregationMaxRecvSize.setStatus("current")
if mibBuilder.loadTexts:
    apRadioNCfgAmpduAggregationMaxRecvSize.setUnits("bytes")


class _ApRadioNCfgAmpduAggregationDensity_Type(Integer32):
    """Custom type apRadioNCfgAmpduAggregationDensity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              250,
              500,
              1000,
              2000,
              4000,
              8000)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8000),
          ("four", 4000),
          ("one", 1000),
          ("onefourth", 250),
          ("onehalf", 500),
          ("two", 2000),
          ("zero", 0))
    )


_ApRadioNCfgAmpduAggregationDensity_Type.__name__ = "Integer32"
_ApRadioNCfgAmpduAggregationDensity_Object = MibTableColumn
apRadioNCfgAmpduAggregationDensity = _ApRadioNCfgAmpduAggregationDensity_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 9, 1, 8),
    _ApRadioNCfgAmpduAggregationDensity_Type()
)
apRadioNCfgAmpduAggregationDensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioNCfgAmpduAggregationDensity.setStatus("current")
if mibBuilder.loadTexts:
    apRadioNCfgAmpduAggregationDensity.setUnits("nanoseconds")


class _ApRadioNCfgAmpduTransmitSizeLimit_Type(Integer32):
    """Custom type apRadioNCfgAmpduTransmitSizeLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApRadioNCfgAmpduTransmitSizeLimit_Type.__name__ = "Integer32"
_ApRadioNCfgAmpduTransmitSizeLimit_Object = MibTableColumn
apRadioNCfgAmpduTransmitSizeLimit = _ApRadioNCfgAmpduTransmitSizeLimit_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 9, 1, 9),
    _ApRadioNCfgAmpduTransmitSizeLimit_Type()
)
apRadioNCfgAmpduTransmitSizeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioNCfgAmpduTransmitSizeLimit.setStatus("current")
_ApRadioNCfgShortGuardInterval_Type = TruthValue
_ApRadioNCfgShortGuardInterval_Object = MibTableColumn
apRadioNCfgShortGuardInterval = _ApRadioNCfgShortGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 9, 1, 10),
    _ApRadioNCfgShortGuardInterval_Type()
)
apRadioNCfgShortGuardInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioNCfgShortGuardInterval.setStatus("current")
_ApRadioNCfgAmpduTransmitEnabled_Type = TruthValue
_ApRadioNCfgAmpduTransmitEnabled_Object = MibTableColumn
apRadioNCfgAmpduTransmitEnabled = _ApRadioNCfgAmpduTransmitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 9, 1, 11),
    _ApRadioNCfgAmpduTransmitEnabled_Type()
)
apRadioNCfgAmpduTransmitEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioNCfgAmpduTransmitEnabled.setStatus("current")


class _ApRadioNCfgChannelOffset_Type(Integer32):
    """Custom type apRadioNCfgChannelOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("above", 2),
          ("below", 3),
          ("none", 1))
    )


_ApRadioNCfgChannelOffset_Type.__name__ = "Integer32"
_ApRadioNCfgChannelOffset_Object = MibTableColumn
apRadioNCfgChannelOffset = _ApRadioNCfgChannelOffset_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 9, 1, 12),
    _ApRadioNCfgChannelOffset_Type()
)
apRadioNCfgChannelOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioNCfgChannelOffset.setStatus("current")
_ApRadioNMcsRateTable_Object = MibTable
apRadioNMcsRateTable = _ApRadioNMcsRateTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 10)
)
if mibBuilder.loadTexts:
    apRadioNMcsRateTable.setStatus("current")
_ApRadioNMcsRateEntry_Object = MibTableRow
apRadioNMcsRateEntry = _ApRadioNMcsRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 10, 1)
)
apRadioNMcsRateEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apRadioSettingsIndex"),
    (0, "SYMBOL-AP-MIB", "apRadioNMcsRateIndex"),
)
if mibBuilder.loadTexts:
    apRadioNMcsRateEntry.setStatus("current")


class _ApRadioNMcsRateIndex_Type(Integer32):
    """Custom type apRadioNMcsRateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ApRadioNMcsRateIndex_Type.__name__ = "Integer32"
_ApRadioNMcsRateIndex_Object = MibTableColumn
apRadioNMcsRateIndex = _ApRadioNMcsRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 10, 1, 1),
    _ApRadioNMcsRateIndex_Type()
)
apRadioNMcsRateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioNMcsRateIndex.setStatus("current")
_ApRadioNMcsRate20MHzChanSgiDisabled_Type = Integer32
_ApRadioNMcsRate20MHzChanSgiDisabled_Object = MibTableColumn
apRadioNMcsRate20MHzChanSgiDisabled = _ApRadioNMcsRate20MHzChanSgiDisabled_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 10, 1, 2),
    _ApRadioNMcsRate20MHzChanSgiDisabled_Type()
)
apRadioNMcsRate20MHzChanSgiDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioNMcsRate20MHzChanSgiDisabled.setStatus("current")
if mibBuilder.loadTexts:
    apRadioNMcsRate20MHzChanSgiDisabled.setUnits("Kbps")
_ApRadioNMcsRate20MHzChanSgiEnabled_Type = Integer32
_ApRadioNMcsRate20MHzChanSgiEnabled_Object = MibTableColumn
apRadioNMcsRate20MHzChanSgiEnabled = _ApRadioNMcsRate20MHzChanSgiEnabled_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 10, 1, 3),
    _ApRadioNMcsRate20MHzChanSgiEnabled_Type()
)
apRadioNMcsRate20MHzChanSgiEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioNMcsRate20MHzChanSgiEnabled.setStatus("deprecated")
if mibBuilder.loadTexts:
    apRadioNMcsRate20MHzChanSgiEnabled.setUnits("Kbps")
_ApRadioNMcsRate40MHzChanSgiDisabled_Type = Integer32
_ApRadioNMcsRate40MHzChanSgiDisabled_Object = MibTableColumn
apRadioNMcsRate40MHzChanSgiDisabled = _ApRadioNMcsRate40MHzChanSgiDisabled_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 10, 1, 4),
    _ApRadioNMcsRate40MHzChanSgiDisabled_Type()
)
apRadioNMcsRate40MHzChanSgiDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioNMcsRate40MHzChanSgiDisabled.setStatus("current")
if mibBuilder.loadTexts:
    apRadioNMcsRate40MHzChanSgiDisabled.setUnits("Kbps")
_ApRadioNMcsRate40MHzChanSgiEnabled_Type = Integer32
_ApRadioNMcsRate40MHzChanSgiEnabled_Object = MibTableColumn
apRadioNMcsRate40MHzChanSgiEnabled = _ApRadioNMcsRate40MHzChanSgiEnabled_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 10, 1, 5),
    _ApRadioNMcsRate40MHzChanSgiEnabled_Type()
)
apRadioNMcsRate40MHzChanSgiEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioNMcsRate40MHzChanSgiEnabled.setStatus("current")
if mibBuilder.loadTexts:
    apRadioNMcsRate40MHzChanSgiEnabled.setUnits("Kbps")


class _ApRadioNMcsRateType_Type(Integer32):
    """Custom type apRadioNMcsRateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("supported", 2))
    )


_ApRadioNMcsRateType_Type.__name__ = "Integer32"
_ApRadioNMcsRateType_Object = MibTableColumn
apRadioNMcsRateType = _ApRadioNMcsRateType_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 10, 1, 6),
    _ApRadioNMcsRateType_Type()
)
apRadioNMcsRateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioNMcsRateType.setStatus("current")
_ApRadioNMcsRateEnabled_Type = TruthValue
_ApRadioNMcsRateEnabled_Object = MibTableColumn
apRadioNMcsRateEnabled = _ApRadioNMcsRateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 1, 10, 1, 7),
    _ApRadioNMcsRateEnabled_Type()
)
apRadioNMcsRateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioNMcsRateEnabled.setStatus("current")
_ApWlan_ObjectIdentity = ObjectIdentity
apWlan = _ApWlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2)
)
_ApWlanTable_Object = MibTable
apWlanTable = _ApWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    apWlanTable.setStatus("current")
_ApWlanEntry_Object = MibTableRow
apWlanEntry = _ApWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 1, 1)
)
apWlanEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apWlanIndex"),
)
if mibBuilder.loadTexts:
    apWlanEntry.setStatus("current")


class _ApWlanIndex_Type(Integer32):
    """Custom type apWlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ApWlanIndex_Type.__name__ = "Integer32"
_ApWlanIndex_Object = MibTableColumn
apWlanIndex = _ApWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 1, 1, 1),
    _ApWlanIndex_Type()
)
apWlanIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apWlanIndex.setStatus("current")
_ApWlanName_Type = DisplayString
_ApWlanName_Object = MibTableColumn
apWlanName = _ApWlanName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 1, 1, 2),
    _ApWlanName_Type()
)
apWlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanName.setStatus("current")
_ApWlanEssid_Type = DisplayString
_ApWlanEssid_Object = MibTableColumn
apWlanEssid = _ApWlanEssid_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 1, 1, 3),
    _ApWlanEssid_Type()
)
apWlanEssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanEssid.setStatus("current")


class _ApWlanUseRadio_Type(Integer32):
    """Custom type apWlanUseRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("aRadio", 2),
          ("bgRadio", 1),
          ("bothBand", 3),
          ("nRadio2400MHz", 4),
          ("nRadio5000MHz", 5),
          ("noneBand", 0))
    )


_ApWlanUseRadio_Type.__name__ = "Integer32"
_ApWlanUseRadio_Object = MibTableColumn
apWlanUseRadio = _ApWlanUseRadio_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 1, 1, 4),
    _ApWlanUseRadio_Type()
)
apWlanUseRadio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanUseRadio.setStatus("current")
_ApWlanMaxMus_Type = Integer32
_ApWlanMaxMus_Object = MibTableColumn
apWlanMaxMus = _ApWlanMaxMus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 1, 1, 5),
    _ApWlanMaxMus_Type()
)
apWlanMaxMus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanMaxMus.setStatus("current")
_ApWlanAclPolicy_Type = SinglePointer
_ApWlanAclPolicy_Object = MibTableColumn
apWlanAclPolicy = _ApWlanAclPolicy_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 1, 1, 6),
    _ApWlanAclPolicy_Type()
)
apWlanAclPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAclPolicy.setStatus("current")
_ApWlanSecurityPolicy_Type = SinglePointer
_ApWlanSecurityPolicy_Object = MibTableColumn
apWlanSecurityPolicy = _ApWlanSecurityPolicy_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 1, 1, 7),
    _ApWlanSecurityPolicy_Type()
)
apWlanSecurityPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanSecurityPolicy.setStatus("current")
_ApWlanQosPolicy_Type = SinglePointer
_ApWlanQosPolicy_Object = MibTableColumn
apWlanQosPolicy = _ApWlanQosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 1, 1, 8),
    _ApWlanQosPolicy_Type()
)
apWlanQosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanQosPolicy.setStatus("current")
_ApWlanAuthKerberosUsername_Type = DisplayString
_ApWlanAuthKerberosUsername_Object = MibTableColumn
apWlanAuthKerberosUsername = _ApWlanAuthKerberosUsername_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 1, 1, 9),
    _ApWlanAuthKerberosUsername_Type()
)
apWlanAuthKerberosUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanAuthKerberosUsername.setStatus("current")
_ApWlanAuthKerberosPassword_Type = Password
_ApWlanAuthKerberosPassword_Object = MibTableColumn
apWlanAuthKerberosPassword = _ApWlanAuthKerberosPassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 1, 1, 10),
    _ApWlanAuthKerberosPassword_Type()
)
apWlanAuthKerberosPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthKerberosPassword.setStatus("current")
_ApWlanDisallowMuToMu_Type = TruthValue
_ApWlanDisallowMuToMu_Object = MibTableColumn
apWlanDisallowMuToMu = _ApWlanDisallowMuToMu_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 1, 1, 11),
    _ApWlanDisallowMuToMu_Type()
)
apWlanDisallowMuToMu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanDisallowMuToMu.setStatus("current")
_ApWlanUseSecureBeacon_Type = TruthValue
_ApWlanUseSecureBeacon_Object = MibTableColumn
apWlanUseSecureBeacon = _ApWlanUseSecureBeacon_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 1, 1, 12),
    _ApWlanUseSecureBeacon_Type()
)
apWlanUseSecureBeacon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanUseSecureBeacon.setStatus("current")
_ApWlanAnswerBroadcastEss_Type = TruthValue
_ApWlanAnswerBroadcastEss_Object = MibTableColumn
apWlanAnswerBroadcastEss = _ApWlanAnswerBroadcastEss_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 1, 1, 13),
    _ApWlanAnswerBroadcastEss_Type()
)
apWlanAnswerBroadcastEss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAnswerBroadcastEss.setStatus("current")
_ApWlanWeight_Type = Integer32
_ApWlanWeight_Object = MibTableColumn
apWlanWeight = _ApWlanWeight_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 1, 1, 14),
    _ApWlanWeight_Type()
)
apWlanWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanWeight.setStatus("obsolete")


class _ApWlanVlanMode_Type(Integer32):
    """Custom type apWlanVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modeDynamic", 1),
          ("modeStatic", 2))
    )


_ApWlanVlanMode_Type.__name__ = "Integer32"
_ApWlanVlanMode_Object = MibTableColumn
apWlanVlanMode = _ApWlanVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 1, 1, 15),
    _ApWlanVlanMode_Type()
)
apWlanVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanVlanMode.setStatus("current")
_ApWlanVlanId_Type = SinglePointer
_ApWlanVlanId_Object = MibTableColumn
apWlanVlanId = _ApWlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 1, 1, 16),
    _ApWlanVlanId_Type()
)
apWlanVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanVlanId.setStatus("current")


class _ApWlanSubnet_Type(Integer32):
    """Custom type apWlanSubnet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lan1", 1),
          ("lan2", 2))
    )


_ApWlanSubnet_Type.__name__ = "Integer32"
_ApWlanSubnet_Object = MibTableColumn
apWlanSubnet = _ApWlanSubnet_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 1, 1, 17),
    _ApWlanSubnet_Type()
)
apWlanSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanSubnet.setStatus("current")
_ApWlanClientBackHaul_Type = TruthValue
_ApWlanClientBackHaul_Object = MibTableColumn
apWlanClientBackHaul = _ApWlanClientBackHaul_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 1, 1, 18),
    _ApWlanClientBackHaul_Type()
)
apWlanClientBackHaul.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanClientBackHaul.setStatus("current")
_ApWlanHotspot_Type = TruthValue
_ApWlanHotspot_Object = MibTableColumn
apWlanHotspot = _ApWlanHotspot_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 1, 1, 19),
    _ApWlanHotspot_Type()
)
apWlanHotspot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanHotspot.setStatus("current")
_ApWlanEnable_Type = TruthValue
_ApWlanEnable_Object = MibTableColumn
apWlanEnable = _ApWlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 1, 1, 20),
    _ApWlanEnable_Type()
)
apWlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanEnable.setStatus("current")


class _ApWlanMuIdleTimeout_Type(Integer32):
    """Custom type apWlanMuIdleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_ApWlanMuIdleTimeout_Type.__name__ = "Integer32"
_ApWlanMuIdleTimeout_Object = MibTableColumn
apWlanMuIdleTimeout = _ApWlanMuIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 1, 1, 21),
    _ApWlanMuIdleTimeout_Type()
)
apWlanMuIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanMuIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    apWlanMuIdleTimeout.setUnits("minutes")
_ApWlanSecPolicyTable_Object = MibTable
apWlanSecPolicyTable = _ApWlanSecPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 2)
)
if mibBuilder.loadTexts:
    apWlanSecPolicyTable.setStatus("current")
_ApWlanSecPolicyEntry_Object = MibTableRow
apWlanSecPolicyEntry = _ApWlanSecPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 2, 1)
)
apWlanSecPolicyEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apWlanSecPolicyIndex"),
)
if mibBuilder.loadTexts:
    apWlanSecPolicyEntry.setStatus("current")


class _ApWlanSecPolicyIndex_Type(Integer32):
    """Custom type apWlanSecPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ApWlanSecPolicyIndex_Type.__name__ = "Integer32"
_ApWlanSecPolicyIndex_Object = MibTableColumn
apWlanSecPolicyIndex = _ApWlanSecPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 2, 1, 1),
    _ApWlanSecPolicyIndex_Type()
)
apWlanSecPolicyIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apWlanSecPolicyIndex.setStatus("current")
_ApWlanSecPolicyName_Type = DisplayString
_ApWlanSecPolicyName_Object = MibTableColumn
apWlanSecPolicyName = _ApWlanSecPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 2, 1, 2),
    _ApWlanSecPolicyName_Type()
)
apWlanSecPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanSecPolicyName.setStatus("current")


class _ApWlanSecPolicyAuthentication_Type(Integer32):
    """Custom type apWlanSecPolicyAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auth802dot1xEap", 2),
          ("authKerberos", 3),
          ("authNone", 1))
    )


_ApWlanSecPolicyAuthentication_Type.__name__ = "Integer32"
_ApWlanSecPolicyAuthentication_Object = MibTableColumn
apWlanSecPolicyAuthentication = _ApWlanSecPolicyAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 2, 1, 3),
    _ApWlanSecPolicyAuthentication_Type()
)
apWlanSecPolicyAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanSecPolicyAuthentication.setStatus("current")


class _ApWlanSecPolicyEncryption_Type(Integer32):
    """Custom type apWlanSecPolicyEncryption based on Integer32"""
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
        *(("cryptoCcmp", 6),
          ("cryptoKeyguardMcm", 4),
          ("cryptoNone", 1),
          ("cryptoWep128", 3),
          ("cryptoWep40", 2),
          ("cryptoWpaTkip", 5))
    )


_ApWlanSecPolicyEncryption_Type.__name__ = "Integer32"
_ApWlanSecPolicyEncryption_Object = MibTableColumn
apWlanSecPolicyEncryption = _ApWlanSecPolicyEncryption_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 2, 1, 4),
    _ApWlanSecPolicyEncryption_Type()
)
apWlanSecPolicyEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanSecPolicyEncryption.setStatus("current")
_ApWlanSecPolicyPointerToWlan_Type = MultiPointer63
_ApWlanSecPolicyPointerToWlan_Object = MibTableColumn
apWlanSecPolicyPointerToWlan = _ApWlanSecPolicyPointerToWlan_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 2, 1, 5),
    _ApWlanSecPolicyPointerToWlan_Type()
)
apWlanSecPolicyPointerToWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanSecPolicyPointerToWlan.setStatus("current")
_ApWlanSecPolicyRowStatus_Type = AbbrevRowStatus
_ApWlanSecPolicyRowStatus_Object = MibTableColumn
apWlanSecPolicyRowStatus = _ApWlanSecPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 2, 1, 6),
    _ApWlanSecPolicyRowStatus_Type()
)
apWlanSecPolicyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanSecPolicyRowStatus.setStatus("current")
_ApWlanAuth_ObjectIdentity = ObjectIdentity
apWlanAuth = _ApWlanAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3)
)
_ApWlanAuthEapTable_Object = MibTable
apWlanAuthEapTable = _ApWlanAuthEapTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    apWlanAuthEapTable.setStatus("current")
_ApWlanAuthEapEntry_Object = MibTableRow
apWlanAuthEapEntry = _ApWlanAuthEapEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1, 1)
)
apWlanAuthEapEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apWlanSecPolicyIndex"),
)
if mibBuilder.loadTexts:
    apWlanAuthEapEntry.setStatus("current")
_ApWlanAuthEapReauthenticationEnable_Type = TruthValue
_ApWlanAuthEapReauthenticationEnable_Object = MibTableColumn
apWlanAuthEapReauthenticationEnable = _ApWlanAuthEapReauthenticationEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1, 1, 1),
    _ApWlanAuthEapReauthenticationEnable_Type()
)
apWlanAuthEapReauthenticationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthEapReauthenticationEnable.setStatus("current")


class _ApWlanAuthEapReauthenticationPeriod_Type(Unsigned32):
    """Custom type apWlanAuthEapReauthenticationPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 9999),
    )


_ApWlanAuthEapReauthenticationPeriod_Type.__name__ = "Unsigned32"
_ApWlanAuthEapReauthenticationPeriod_Object = MibTableColumn
apWlanAuthEapReauthenticationPeriod = _ApWlanAuthEapReauthenticationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1, 1, 2),
    _ApWlanAuthEapReauthenticationPeriod_Type()
)
apWlanAuthEapReauthenticationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthEapReauthenticationPeriod.setStatus("current")
if mibBuilder.loadTexts:
    apWlanAuthEapReauthenticationPeriod.setUnits("seconds")


class _ApWlanAuthEapReauthenticationMaxRetries_Type(Unsigned32):
    """Custom type apWlanAuthEapReauthenticationMaxRetries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_ApWlanAuthEapReauthenticationMaxRetries_Type.__name__ = "Unsigned32"
_ApWlanAuthEapReauthenticationMaxRetries_Object = MibTableColumn
apWlanAuthEapReauthenticationMaxRetries = _ApWlanAuthEapReauthenticationMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1, 1, 3),
    _ApWlanAuthEapReauthenticationMaxRetries_Type()
)
apWlanAuthEapReauthenticationMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthEapReauthenticationMaxRetries.setStatus("current")
_ApWlanAuthEapRadius1Server_Type = IpAddress
_ApWlanAuthEapRadius1Server_Object = MibTableColumn
apWlanAuthEapRadius1Server = _ApWlanAuthEapRadius1Server_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1, 1, 4),
    _ApWlanAuthEapRadius1Server_Type()
)
apWlanAuthEapRadius1Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthEapRadius1Server.setStatus("current")
_ApWlanAuthEapRadius1Port_Type = Unsigned32
_ApWlanAuthEapRadius1Port_Object = MibTableColumn
apWlanAuthEapRadius1Port = _ApWlanAuthEapRadius1Port_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1, 1, 5),
    _ApWlanAuthEapRadius1Port_Type()
)
apWlanAuthEapRadius1Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthEapRadius1Port.setStatus("current")
_ApWlanAuthEapRadius1SharedSecret_Type = Password
_ApWlanAuthEapRadius1SharedSecret_Object = MibTableColumn
apWlanAuthEapRadius1SharedSecret = _ApWlanAuthEapRadius1SharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1, 1, 6),
    _ApWlanAuthEapRadius1SharedSecret_Type()
)
apWlanAuthEapRadius1SharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthEapRadius1SharedSecret.setStatus("current")
_ApWlanAuthEapRadius2Server_Type = IpAddress
_ApWlanAuthEapRadius2Server_Object = MibTableColumn
apWlanAuthEapRadius2Server = _ApWlanAuthEapRadius2Server_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1, 1, 7),
    _ApWlanAuthEapRadius2Server_Type()
)
apWlanAuthEapRadius2Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthEapRadius2Server.setStatus("current")
_ApWlanAuthEapRadius2Port_Type = Unsigned32
_ApWlanAuthEapRadius2Port_Object = MibTableColumn
apWlanAuthEapRadius2Port = _ApWlanAuthEapRadius2Port_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1, 1, 8),
    _ApWlanAuthEapRadius2Port_Type()
)
apWlanAuthEapRadius2Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthEapRadius2Port.setStatus("current")
_ApWlanAuthEapRadius2SharedSecret_Type = Password
_ApWlanAuthEapRadius2SharedSecret_Object = MibTableColumn
apWlanAuthEapRadius2SharedSecret = _ApWlanAuthEapRadius2SharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1, 1, 9),
    _ApWlanAuthEapRadius2SharedSecret_Type()
)
apWlanAuthEapRadius2SharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthEapRadius2SharedSecret.setStatus("current")


class _ApWlanAuthEapMuQuietPeriod_Type(Unsigned32):
    """Custom type apWlanAuthEapMuQuietPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApWlanAuthEapMuQuietPeriod_Type.__name__ = "Unsigned32"
_ApWlanAuthEapMuQuietPeriod_Object = MibTableColumn
apWlanAuthEapMuQuietPeriod = _ApWlanAuthEapMuQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1, 1, 10),
    _ApWlanAuthEapMuQuietPeriod_Type()
)
apWlanAuthEapMuQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthEapMuQuietPeriod.setStatus("current")
if mibBuilder.loadTexts:
    apWlanAuthEapMuQuietPeriod.setUnits("seconds")


class _ApWlanAuthEapMuTimeout_Type(Unsigned32):
    """Custom type apWlanAuthEapMuTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ApWlanAuthEapMuTimeout_Type.__name__ = "Unsigned32"
_ApWlanAuthEapMuTimeout_Object = MibTableColumn
apWlanAuthEapMuTimeout = _ApWlanAuthEapMuTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1, 1, 11),
    _ApWlanAuthEapMuTimeout_Type()
)
apWlanAuthEapMuTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthEapMuTimeout.setStatus("current")
if mibBuilder.loadTexts:
    apWlanAuthEapMuTimeout.setUnits("seconds")


class _ApWlanAuthEapMuTxPeriod_Type(Unsigned32):
    """Custom type apWlanAuthEapMuTxPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApWlanAuthEapMuTxPeriod_Type.__name__ = "Unsigned32"
_ApWlanAuthEapMuTxPeriod_Object = MibTableColumn
apWlanAuthEapMuTxPeriod = _ApWlanAuthEapMuTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1, 1, 12),
    _ApWlanAuthEapMuTxPeriod_Type()
)
apWlanAuthEapMuTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthEapMuTxPeriod.setStatus("current")
if mibBuilder.loadTexts:
    apWlanAuthEapMuTxPeriod.setUnits("seconds")


class _ApWlanAuthEapMuMaxRetries_Type(Unsigned32):
    """Custom type apWlanAuthEapMuMaxRetries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ApWlanAuthEapMuMaxRetries_Type.__name__ = "Unsigned32"
_ApWlanAuthEapMuMaxRetries_Object = MibTableColumn
apWlanAuthEapMuMaxRetries = _ApWlanAuthEapMuMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1, 1, 13),
    _ApWlanAuthEapMuMaxRetries_Type()
)
apWlanAuthEapMuMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthEapMuMaxRetries.setStatus("current")


class _ApWlanAuthEapServerTimeout_Type(Unsigned32):
    """Custom type apWlanAuthEapServerTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ApWlanAuthEapServerTimeout_Type.__name__ = "Unsigned32"
_ApWlanAuthEapServerTimeout_Object = MibTableColumn
apWlanAuthEapServerTimeout = _ApWlanAuthEapServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1, 1, 14),
    _ApWlanAuthEapServerTimeout_Type()
)
apWlanAuthEapServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthEapServerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    apWlanAuthEapServerTimeout.setUnits("seconds")


class _ApWlanAuthEapServerMaxRetries_Type(Unsigned32):
    """Custom type apWlanAuthEapServerMaxRetries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ApWlanAuthEapServerMaxRetries_Type.__name__ = "Unsigned32"
_ApWlanAuthEapServerMaxRetries_Object = MibTableColumn
apWlanAuthEapServerMaxRetries = _ApWlanAuthEapServerMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1, 1, 15),
    _ApWlanAuthEapServerMaxRetries_Type()
)
apWlanAuthEapServerMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthEapServerMaxRetries.setStatus("current")
_ApWlanAuthEapRadiusAcctMode_Type = TruthValue
_ApWlanAuthEapRadiusAcctMode_Object = MibTableColumn
apWlanAuthEapRadiusAcctMode = _ApWlanAuthEapRadiusAcctMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1, 1, 16),
    _ApWlanAuthEapRadiusAcctMode_Type()
)
apWlanAuthEapRadiusAcctMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthEapRadiusAcctMode.setStatus("current")


class _ApWlanAuthEapRadiusAcctMuTimeout_Type(Unsigned32):
    """Custom type apWlanAuthEapRadiusAcctMuTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ApWlanAuthEapRadiusAcctMuTimeout_Type.__name__ = "Unsigned32"
_ApWlanAuthEapRadiusAcctMuTimeout_Object = MibTableColumn
apWlanAuthEapRadiusAcctMuTimeout = _ApWlanAuthEapRadiusAcctMuTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1, 1, 17),
    _ApWlanAuthEapRadiusAcctMuTimeout_Type()
)
apWlanAuthEapRadiusAcctMuTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthEapRadiusAcctMuTimeout.setStatus("current")


class _ApWlanAuthEapRadiusAcctMuRetries_Type(Unsigned32):
    """Custom type apWlanAuthEapRadiusAcctMuRetries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ApWlanAuthEapRadiusAcctMuRetries_Type.__name__ = "Unsigned32"
_ApWlanAuthEapRadiusAcctMuRetries_Object = MibTableColumn
apWlanAuthEapRadiusAcctMuRetries = _ApWlanAuthEapRadiusAcctMuRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1, 1, 18),
    _ApWlanAuthEapRadiusAcctMuRetries_Type()
)
apWlanAuthEapRadiusAcctMuRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthEapRadiusAcctMuRetries.setStatus("current")
_ApWlanAuthEapSyslogMode_Type = TruthValue
_ApWlanAuthEapSyslogMode_Object = MibTableColumn
apWlanAuthEapSyslogMode = _ApWlanAuthEapSyslogMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1, 1, 19),
    _ApWlanAuthEapSyslogMode_Type()
)
apWlanAuthEapSyslogMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthEapSyslogMode.setStatus("current")
_ApWlanAuthEapSyslogServerIp_Type = IpAddress
_ApWlanAuthEapSyslogServerIp_Object = MibTableColumn
apWlanAuthEapSyslogServerIp = _ApWlanAuthEapSyslogServerIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1, 1, 20),
    _ApWlanAuthEapSyslogServerIp_Type()
)
apWlanAuthEapSyslogServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthEapSyslogServerIp.setStatus("current")
_ApWlanAuthEapRadiusExtAcctServer_Type = IpAddress
_ApWlanAuthEapRadiusExtAcctServer_Object = MibTableColumn
apWlanAuthEapRadiusExtAcctServer = _ApWlanAuthEapRadiusExtAcctServer_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1, 1, 21),
    _ApWlanAuthEapRadiusExtAcctServer_Type()
)
apWlanAuthEapRadiusExtAcctServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthEapRadiusExtAcctServer.setStatus("current")
_ApWlanAuthEapRadiusExtPort_Type = Unsigned32
_ApWlanAuthEapRadiusExtPort_Object = MibTableColumn
apWlanAuthEapRadiusExtPort = _ApWlanAuthEapRadiusExtPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1, 1, 22),
    _ApWlanAuthEapRadiusExtPort_Type()
)
apWlanAuthEapRadiusExtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthEapRadiusExtPort.setStatus("current")
_ApWlanAuthEapRadiusExtSharedSecret_Type = Password
_ApWlanAuthEapRadiusExtSharedSecret_Object = MibTableColumn
apWlanAuthEapRadiusExtSharedSecret = _ApWlanAuthEapRadiusExtSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 1, 1, 23),
    _ApWlanAuthEapRadiusExtSharedSecret_Type()
)
apWlanAuthEapRadiusExtSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthEapRadiusExtSharedSecret.setStatus("current")
_ApWlanAuthKerberosTable_Object = MibTable
apWlanAuthKerberosTable = _ApWlanAuthKerberosTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 2)
)
if mibBuilder.loadTexts:
    apWlanAuthKerberosTable.setStatus("current")
_ApWlanAuthKerberosEntry_Object = MibTableRow
apWlanAuthKerberosEntry = _ApWlanAuthKerberosEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 2, 1)
)
apWlanAuthKerberosEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apWlanSecPolicyIndex"),
)
if mibBuilder.loadTexts:
    apWlanAuthKerberosEntry.setStatus("current")
_ApWlanAuthKerberosRealmName_Type = DisplayString
_ApWlanAuthKerberosRealmName_Object = MibTableColumn
apWlanAuthKerberosRealmName = _ApWlanAuthKerberosRealmName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 2, 1, 1),
    _ApWlanAuthKerberosRealmName_Type()
)
apWlanAuthKerberosRealmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthKerberosRealmName.setStatus("current")
_ApWlanAuthKerberosKdcServerIp1_Type = IpAddress
_ApWlanAuthKerberosKdcServerIp1_Object = MibTableColumn
apWlanAuthKerberosKdcServerIp1 = _ApWlanAuthKerberosKdcServerIp1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 2, 1, 2),
    _ApWlanAuthKerberosKdcServerIp1_Type()
)
apWlanAuthKerberosKdcServerIp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthKerberosKdcServerIp1.setStatus("current")
_ApWlanAuthKerberosKdcPort1_Type = Unsigned32
_ApWlanAuthKerberosKdcPort1_Object = MibTableColumn
apWlanAuthKerberosKdcPort1 = _ApWlanAuthKerberosKdcPort1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 2, 1, 3),
    _ApWlanAuthKerberosKdcPort1_Type()
)
apWlanAuthKerberosKdcPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthKerberosKdcPort1.setStatus("current")
_ApWlanAuthKerberosKdcServerIp2_Type = IpAddress
_ApWlanAuthKerberosKdcServerIp2_Object = MibTableColumn
apWlanAuthKerberosKdcServerIp2 = _ApWlanAuthKerberosKdcServerIp2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 2, 1, 4),
    _ApWlanAuthKerberosKdcServerIp2_Type()
)
apWlanAuthKerberosKdcServerIp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthKerberosKdcServerIp2.setStatus("current")
_ApWlanAuthKerberosKdcPort2_Type = Unsigned32
_ApWlanAuthKerberosKdcPort2_Object = MibTableColumn
apWlanAuthKerberosKdcPort2 = _ApWlanAuthKerberosKdcPort2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 2, 1, 5),
    _ApWlanAuthKerberosKdcPort2_Type()
)
apWlanAuthKerberosKdcPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthKerberosKdcPort2.setStatus("current")
_ApWlanAuthKerberosKdcServerIpR_Type = IpAddress
_ApWlanAuthKerberosKdcServerIpR_Object = MibTableColumn
apWlanAuthKerberosKdcServerIpR = _ApWlanAuthKerberosKdcServerIpR_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 2, 1, 6),
    _ApWlanAuthKerberosKdcServerIpR_Type()
)
apWlanAuthKerberosKdcServerIpR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthKerberosKdcServerIpR.setStatus("current")
_ApWlanAuthKerberosKdcPortR_Type = Unsigned32
_ApWlanAuthKerberosKdcPortR_Object = MibTableColumn
apWlanAuthKerberosKdcPortR = _ApWlanAuthKerberosKdcPortR_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 3, 2, 1, 7),
    _ApWlanAuthKerberosKdcPortR_Type()
)
apWlanAuthKerberosKdcPortR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanAuthKerberosKdcPortR.setStatus("current")
_ApWlanCrypto_ObjectIdentity = ObjectIdentity
apWlanCrypto = _ApWlanCrypto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4)
)
_ApWlanCryptoWepTable_Object = MibTable
apWlanCryptoWepTable = _ApWlanCryptoWepTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 1)
)
if mibBuilder.loadTexts:
    apWlanCryptoWepTable.setStatus("current")
_ApWlanCryptoWepEntry_Object = MibTableRow
apWlanCryptoWepEntry = _ApWlanCryptoWepEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 1, 1)
)
apWlanCryptoWepEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apWlanSecPolicyIndex"),
)
if mibBuilder.loadTexts:
    apWlanCryptoWepEntry.setStatus("current")


class _ApWlanCryptoWepPassKey_Type(Password):
    """Custom type apWlanCryptoWepPassKey based on Password"""
    subtypeSpec = Password.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 32),
    )


_ApWlanCryptoWepPassKey_Type.__name__ = "Password"
_ApWlanCryptoWepPassKey_Object = MibTableColumn
apWlanCryptoWepPassKey = _ApWlanCryptoWepPassKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 1, 1, 1),
    _ApWlanCryptoWepPassKey_Type()
)
apWlanCryptoWepPassKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoWepPassKey.setStatus("current")


class _ApWlanCryptoWepKey1_Type(OctetString):
    """Custom type apWlanCryptoWepKey1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_ApWlanCryptoWepKey1_Type.__name__ = "OctetString"
_ApWlanCryptoWepKey1_Object = MibTableColumn
apWlanCryptoWepKey1 = _ApWlanCryptoWepKey1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 1, 1, 2),
    _ApWlanCryptoWepKey1_Type()
)
apWlanCryptoWepKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoWepKey1.setStatus("current")


class _ApWlanCryptoWepKey2_Type(OctetString):
    """Custom type apWlanCryptoWepKey2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_ApWlanCryptoWepKey2_Type.__name__ = "OctetString"
_ApWlanCryptoWepKey2_Object = MibTableColumn
apWlanCryptoWepKey2 = _ApWlanCryptoWepKey2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 1, 1, 3),
    _ApWlanCryptoWepKey2_Type()
)
apWlanCryptoWepKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoWepKey2.setStatus("current")


class _ApWlanCryptoWepKey3_Type(OctetString):
    """Custom type apWlanCryptoWepKey3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_ApWlanCryptoWepKey3_Type.__name__ = "OctetString"
_ApWlanCryptoWepKey3_Object = MibTableColumn
apWlanCryptoWepKey3 = _ApWlanCryptoWepKey3_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 1, 1, 4),
    _ApWlanCryptoWepKey3_Type()
)
apWlanCryptoWepKey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoWepKey3.setStatus("current")


class _ApWlanCryptoWepKey4_Type(OctetString):
    """Custom type apWlanCryptoWepKey4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_ApWlanCryptoWepKey4_Type.__name__ = "OctetString"
_ApWlanCryptoWepKey4_Object = MibTableColumn
apWlanCryptoWepKey4 = _ApWlanCryptoWepKey4_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 1, 1, 5),
    _ApWlanCryptoWepKey4_Type()
)
apWlanCryptoWepKey4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoWepKey4.setStatus("current")


class _ApWlanCryptoWepKeyToUse_Type(Integer32):
    """Custom type apWlanCryptoWepKeyToUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ApWlanCryptoWepKeyToUse_Type.__name__ = "Integer32"
_ApWlanCryptoWepKeyToUse_Object = MibTableColumn
apWlanCryptoWepKeyToUse = _ApWlanCryptoWepKeyToUse_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 1, 1, 6),
    _ApWlanCryptoWepKeyToUse_Type()
)
apWlanCryptoWepKeyToUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoWepKeyToUse.setStatus("current")
_ApWlanCryptoWepMixedMode_Type = TruthValue
_ApWlanCryptoWepMixedMode_Object = MibTableColumn
apWlanCryptoWepMixedMode = _ApWlanCryptoWepMixedMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 1, 1, 7),
    _ApWlanCryptoWepMixedMode_Type()
)
apWlanCryptoWepMixedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoWepMixedMode.setStatus("current")
_ApWlanCryptoTkipTable_Object = MibTable
apWlanCryptoTkipTable = _ApWlanCryptoTkipTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 2)
)
if mibBuilder.loadTexts:
    apWlanCryptoTkipTable.setStatus("current")
_ApWlanCryptoTkipEntry_Object = MibTableRow
apWlanCryptoTkipEntry = _ApWlanCryptoTkipEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 2, 1)
)
apWlanCryptoTkipEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apWlanSecPolicyIndex"),
)
if mibBuilder.loadTexts:
    apWlanCryptoTkipEntry.setStatus("current")
_ApWlanCryptoTkipBcastKeyRotation_Type = TruthValue
_ApWlanCryptoTkipBcastKeyRotation_Object = MibTableColumn
apWlanCryptoTkipBcastKeyRotation = _ApWlanCryptoTkipBcastKeyRotation_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 2, 1, 1),
    _ApWlanCryptoTkipBcastKeyRotation_Type()
)
apWlanCryptoTkipBcastKeyRotation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoTkipBcastKeyRotation.setStatus("current")


class _ApWlanCryptoTkipKeyRotationInterval_Type(Unsigned32):
    """Custom type apWlanCryptoTkipKeyRotationInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 604800),
    )


_ApWlanCryptoTkipKeyRotationInterval_Type.__name__ = "Unsigned32"
_ApWlanCryptoTkipKeyRotationInterval_Object = MibTableColumn
apWlanCryptoTkipKeyRotationInterval = _ApWlanCryptoTkipKeyRotationInterval_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 2, 1, 2),
    _ApWlanCryptoTkipKeyRotationInterval_Type()
)
apWlanCryptoTkipKeyRotationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoTkipKeyRotationInterval.setStatus("current")
if mibBuilder.loadTexts:
    apWlanCryptoTkipKeyRotationInterval.setUnits("seconds")


class _ApWlanCryptoTkipKeyToUse_Type(Integer32):
    """Custom type apWlanCryptoTkipKeyToUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("use256bitKey", 2),
          ("useAsciiPassphrase", 1))
    )


_ApWlanCryptoTkipKeyToUse_Type.__name__ = "Integer32"
_ApWlanCryptoTkipKeyToUse_Object = MibTableColumn
apWlanCryptoTkipKeyToUse = _ApWlanCryptoTkipKeyToUse_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 2, 1, 3),
    _ApWlanCryptoTkipKeyToUse_Type()
)
apWlanCryptoTkipKeyToUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoTkipKeyToUse.setStatus("current")


class _ApWlanCryptoTkipPassphrase_Type(OctetString):
    """Custom type apWlanCryptoTkipPassphrase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_ApWlanCryptoTkipPassphrase_Type.__name__ = "OctetString"
_ApWlanCryptoTkipPassphrase_Object = MibTableColumn
apWlanCryptoTkipPassphrase = _ApWlanCryptoTkipPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 2, 1, 4),
    _ApWlanCryptoTkipPassphrase_Type()
)
apWlanCryptoTkipPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoTkipPassphrase.setStatus("current")


class _ApWlanCryptoTkipKey_Type(OctetString):
    """Custom type apWlanCryptoTkipKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_ApWlanCryptoTkipKey_Type.__name__ = "OctetString"
_ApWlanCryptoTkipKey_Object = MibTableColumn
apWlanCryptoTkipKey = _ApWlanCryptoTkipKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 2, 1, 5),
    _ApWlanCryptoTkipKey_Type()
)
apWlanCryptoTkipKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoTkipKey.setStatus("current")


class _ApWlanCryptoTkipAllowWpa2Client_Type(Integer32):
    """Custom type apWlanCryptoTkipAllowWpa2Client based on Integer32"""
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


_ApWlanCryptoTkipAllowWpa2Client_Type.__name__ = "Integer32"
_ApWlanCryptoTkipAllowWpa2Client_Object = MibTableColumn
apWlanCryptoTkipAllowWpa2Client = _ApWlanCryptoTkipAllowWpa2Client_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 2, 1, 6),
    _ApWlanCryptoTkipAllowWpa2Client_Type()
)
apWlanCryptoTkipAllowWpa2Client.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoTkipAllowWpa2Client.setStatus("current")


class _ApWlanCryptoTkipFastRoamPreAuth_Type(Integer32):
    """Custom type apWlanCryptoTkipFastRoamPreAuth based on Integer32"""
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


_ApWlanCryptoTkipFastRoamPreAuth_Type.__name__ = "Integer32"
_ApWlanCryptoTkipFastRoamPreAuth_Object = MibTableColumn
apWlanCryptoTkipFastRoamPreAuth = _ApWlanCryptoTkipFastRoamPreAuth_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 2, 1, 7),
    _ApWlanCryptoTkipFastRoamPreAuth_Type()
)
apWlanCryptoTkipFastRoamPreAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoTkipFastRoamPreAuth.setStatus("current")
_ApWlanCryptoCcmpTable_Object = MibTable
apWlanCryptoCcmpTable = _ApWlanCryptoCcmpTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 3)
)
if mibBuilder.loadTexts:
    apWlanCryptoCcmpTable.setStatus("current")
_ApWlanCryptoCcmpEntry_Object = MibTableRow
apWlanCryptoCcmpEntry = _ApWlanCryptoCcmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 3, 1)
)
apWlanCryptoCcmpEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apWlanSecPolicyIndex"),
)
if mibBuilder.loadTexts:
    apWlanCryptoCcmpEntry.setStatus("current")
_ApWlanCryptoCcmpBcastKeyRotation_Type = TruthValue
_ApWlanCryptoCcmpBcastKeyRotation_Object = MibTableColumn
apWlanCryptoCcmpBcastKeyRotation = _ApWlanCryptoCcmpBcastKeyRotation_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 3, 1, 1),
    _ApWlanCryptoCcmpBcastKeyRotation_Type()
)
apWlanCryptoCcmpBcastKeyRotation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoCcmpBcastKeyRotation.setStatus("current")


class _ApWlanCryptoCcmpKeyRotationInterval_Type(Unsigned32):
    """Custom type apWlanCryptoCcmpKeyRotationInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 604800),
    )


_ApWlanCryptoCcmpKeyRotationInterval_Type.__name__ = "Unsigned32"
_ApWlanCryptoCcmpKeyRotationInterval_Object = MibTableColumn
apWlanCryptoCcmpKeyRotationInterval = _ApWlanCryptoCcmpKeyRotationInterval_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 3, 1, 2),
    _ApWlanCryptoCcmpKeyRotationInterval_Type()
)
apWlanCryptoCcmpKeyRotationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoCcmpKeyRotationInterval.setStatus("current")
if mibBuilder.loadTexts:
    apWlanCryptoCcmpKeyRotationInterval.setUnits("seconds")


class _ApWlanCryptoCcmpKeyToUse_Type(Integer32):
    """Custom type apWlanCryptoCcmpKeyToUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("use256bitKey", 2),
          ("useAsciiPassphrase", 1))
    )


_ApWlanCryptoCcmpKeyToUse_Type.__name__ = "Integer32"
_ApWlanCryptoCcmpKeyToUse_Object = MibTableColumn
apWlanCryptoCcmpKeyToUse = _ApWlanCryptoCcmpKeyToUse_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 3, 1, 3),
    _ApWlanCryptoCcmpKeyToUse_Type()
)
apWlanCryptoCcmpKeyToUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoCcmpKeyToUse.setStatus("current")


class _ApWlanCryptoCcmpPassphrase_Type(OctetString):
    """Custom type apWlanCryptoCcmpPassphrase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_ApWlanCryptoCcmpPassphrase_Type.__name__ = "OctetString"
_ApWlanCryptoCcmpPassphrase_Object = MibTableColumn
apWlanCryptoCcmpPassphrase = _ApWlanCryptoCcmpPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 3, 1, 4),
    _ApWlanCryptoCcmpPassphrase_Type()
)
apWlanCryptoCcmpPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoCcmpPassphrase.setStatus("current")


class _ApWlanCryptoCcmpKey_Type(OctetString):
    """Custom type apWlanCryptoCcmpKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_ApWlanCryptoCcmpKey_Type.__name__ = "OctetString"
_ApWlanCryptoCcmpKey_Object = MibTableColumn
apWlanCryptoCcmpKey = _ApWlanCryptoCcmpKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 3, 1, 5),
    _ApWlanCryptoCcmpKey_Type()
)
apWlanCryptoCcmpKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoCcmpKey.setStatus("current")
_ApWlanCryptoCcmpMixedMode_Type = TruthValue
_ApWlanCryptoCcmpMixedMode_Object = MibTableColumn
apWlanCryptoCcmpMixedMode = _ApWlanCryptoCcmpMixedMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 3, 1, 6),
    _ApWlanCryptoCcmpMixedMode_Type()
)
apWlanCryptoCcmpMixedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoCcmpMixedMode.setStatus("current")
_ApWlanCryptoCcmpFastRoamPreAuth_Type = TruthValue
_ApWlanCryptoCcmpFastRoamPreAuth_Object = MibTableColumn
apWlanCryptoCcmpFastRoamPreAuth = _ApWlanCryptoCcmpFastRoamPreAuth_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 3, 1, 7),
    _ApWlanCryptoCcmpFastRoamPreAuth_Type()
)
apWlanCryptoCcmpFastRoamPreAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoCcmpFastRoamPreAuth.setStatus("current")
_ApWlanCryptoKeyguardTable_Object = MibTable
apWlanCryptoKeyguardTable = _ApWlanCryptoKeyguardTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 4)
)
if mibBuilder.loadTexts:
    apWlanCryptoKeyguardTable.setStatus("current")
_ApWlanCryptoKeyguardEntry_Object = MibTableRow
apWlanCryptoKeyguardEntry = _ApWlanCryptoKeyguardEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 4, 1)
)
apWlanCryptoKeyguardEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apWlanSecPolicyIndex"),
)
if mibBuilder.loadTexts:
    apWlanCryptoKeyguardEntry.setStatus("current")


class _ApWlanCryptoKeyguardPassKey_Type(OctetString):
    """Custom type apWlanCryptoKeyguardPassKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 32),
    )


_ApWlanCryptoKeyguardPassKey_Type.__name__ = "OctetString"
_ApWlanCryptoKeyguardPassKey_Object = MibTableColumn
apWlanCryptoKeyguardPassKey = _ApWlanCryptoKeyguardPassKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 4, 1, 1),
    _ApWlanCryptoKeyguardPassKey_Type()
)
apWlanCryptoKeyguardPassKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoKeyguardPassKey.setStatus("current")


class _ApWlanCryptoKeyguardKey1_Type(OctetString):
    """Custom type apWlanCryptoKeyguardKey1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_ApWlanCryptoKeyguardKey1_Type.__name__ = "OctetString"
_ApWlanCryptoKeyguardKey1_Object = MibTableColumn
apWlanCryptoKeyguardKey1 = _ApWlanCryptoKeyguardKey1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 4, 1, 2),
    _ApWlanCryptoKeyguardKey1_Type()
)
apWlanCryptoKeyguardKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoKeyguardKey1.setStatus("current")


class _ApWlanCryptoKeyguardKey2_Type(OctetString):
    """Custom type apWlanCryptoKeyguardKey2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_ApWlanCryptoKeyguardKey2_Type.__name__ = "OctetString"
_ApWlanCryptoKeyguardKey2_Object = MibTableColumn
apWlanCryptoKeyguardKey2 = _ApWlanCryptoKeyguardKey2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 4, 1, 3),
    _ApWlanCryptoKeyguardKey2_Type()
)
apWlanCryptoKeyguardKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoKeyguardKey2.setStatus("current")


class _ApWlanCryptoKeyguardKey3_Type(OctetString):
    """Custom type apWlanCryptoKeyguardKey3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_ApWlanCryptoKeyguardKey3_Type.__name__ = "OctetString"
_ApWlanCryptoKeyguardKey3_Object = MibTableColumn
apWlanCryptoKeyguardKey3 = _ApWlanCryptoKeyguardKey3_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 4, 1, 4),
    _ApWlanCryptoKeyguardKey3_Type()
)
apWlanCryptoKeyguardKey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoKeyguardKey3.setStatus("current")


class _ApWlanCryptoKeyguardKey4_Type(OctetString):
    """Custom type apWlanCryptoKeyguardKey4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_ApWlanCryptoKeyguardKey4_Type.__name__ = "OctetString"
_ApWlanCryptoKeyguardKey4_Object = MibTableColumn
apWlanCryptoKeyguardKey4 = _ApWlanCryptoKeyguardKey4_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 4, 1, 5),
    _ApWlanCryptoKeyguardKey4_Type()
)
apWlanCryptoKeyguardKey4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoKeyguardKey4.setStatus("current")


class _ApWlanCryptoKeyguardKeyToUse_Type(Integer32):
    """Custom type apWlanCryptoKeyguardKeyToUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ApWlanCryptoKeyguardKeyToUse_Type.__name__ = "Integer32"
_ApWlanCryptoKeyguardKeyToUse_Object = MibTableColumn
apWlanCryptoKeyguardKeyToUse = _ApWlanCryptoKeyguardKeyToUse_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 4, 1, 6),
    _ApWlanCryptoKeyguardKeyToUse_Type()
)
apWlanCryptoKeyguardKeyToUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoKeyguardKeyToUse.setStatus("current")
_ApWlanCryptoKeyguardMixedMode_Type = TruthValue
_ApWlanCryptoKeyguardMixedMode_Object = MibTableColumn
apWlanCryptoKeyguardMixedMode = _ApWlanCryptoKeyguardMixedMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 4, 4, 1, 7),
    _ApWlanCryptoKeyguardMixedMode_Type()
)
apWlanCryptoKeyguardMixedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanCryptoKeyguardMixedMode.setStatus("current")
_ApWlanMuAclPolicyTable_Object = MibTable
apWlanMuAclPolicyTable = _ApWlanMuAclPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 5)
)
if mibBuilder.loadTexts:
    apWlanMuAclPolicyTable.setStatus("current")
_ApWlanMuAclPolicyEntry_Object = MibTableRow
apWlanMuAclPolicyEntry = _ApWlanMuAclPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 5, 1)
)
apWlanMuAclPolicyEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apWlanMuAclPolicyIndex"),
)
if mibBuilder.loadTexts:
    apWlanMuAclPolicyEntry.setStatus("current")


class _ApWlanMuAclPolicyIndex_Type(Integer32):
    """Custom type apWlanMuAclPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ApWlanMuAclPolicyIndex_Type.__name__ = "Integer32"
_ApWlanMuAclPolicyIndex_Object = MibTableColumn
apWlanMuAclPolicyIndex = _ApWlanMuAclPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 5, 1, 1),
    _ApWlanMuAclPolicyIndex_Type()
)
apWlanMuAclPolicyIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apWlanMuAclPolicyIndex.setStatus("current")
_ApWlanMuAclPolicyName_Type = DisplayString
_ApWlanMuAclPolicyName_Object = MibTableColumn
apWlanMuAclPolicyName = _ApWlanMuAclPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 5, 1, 2),
    _ApWlanMuAclPolicyName_Type()
)
apWlanMuAclPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanMuAclPolicyName.setStatus("current")


class _ApWlanMuAclPolicyAccessMode_Type(Integer32):
    """Custom type apWlanMuAclPolicyAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_ApWlanMuAclPolicyAccessMode_Type.__name__ = "Integer32"
_ApWlanMuAclPolicyAccessMode_Object = MibTableColumn
apWlanMuAclPolicyAccessMode = _ApWlanMuAclPolicyAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 5, 1, 3),
    _ApWlanMuAclPolicyAccessMode_Type()
)
apWlanMuAclPolicyAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanMuAclPolicyAccessMode.setStatus("current")
_ApWlanMuAclPolicyPointerToWlan_Type = MultiPointer63
_ApWlanMuAclPolicyPointerToWlan_Object = MibTableColumn
apWlanMuAclPolicyPointerToWlan = _ApWlanMuAclPolicyPointerToWlan_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 5, 1, 4),
    _ApWlanMuAclPolicyPointerToWlan_Type()
)
apWlanMuAclPolicyPointerToWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanMuAclPolicyPointerToWlan.setStatus("current")
_ApWlanMuAclPolicyRowStatus_Type = AbbrevRowStatus
_ApWlanMuAclPolicyRowStatus_Object = MibTableColumn
apWlanMuAclPolicyRowStatus = _ApWlanMuAclPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 5, 1, 5),
    _ApWlanMuAclPolicyRowStatus_Type()
)
apWlanMuAclPolicyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanMuAclPolicyRowStatus.setStatus("current")
_ApWlanMuAclTable_Object = MibTable
apWlanMuAclTable = _ApWlanMuAclTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 6)
)
if mibBuilder.loadTexts:
    apWlanMuAclTable.setStatus("current")
_ApWlanMuAclEntry_Object = MibTableRow
apWlanMuAclEntry = _ApWlanMuAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 6, 1)
)
apWlanMuAclEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apWlanMuAclIndex"),
)
if mibBuilder.loadTexts:
    apWlanMuAclEntry.setStatus("current")


class _ApWlanMuAclIndex_Type(Integer32):
    """Custom type apWlanMuAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_ApWlanMuAclIndex_Type.__name__ = "Integer32"
_ApWlanMuAclIndex_Object = MibTableColumn
apWlanMuAclIndex = _ApWlanMuAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 6, 1, 1),
    _ApWlanMuAclIndex_Type()
)
apWlanMuAclIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apWlanMuAclIndex.setStatus("current")
_ApWlanMuAclStartingMac_Type = PhysAddress
_ApWlanMuAclStartingMac_Object = MibTableColumn
apWlanMuAclStartingMac = _ApWlanMuAclStartingMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 6, 1, 2),
    _ApWlanMuAclStartingMac_Type()
)
apWlanMuAclStartingMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanMuAclStartingMac.setStatus("current")
_ApWlanMuAclEndingMac_Type = PhysAddress
_ApWlanMuAclEndingMac_Object = MibTableColumn
apWlanMuAclEndingMac = _ApWlanMuAclEndingMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 6, 1, 3),
    _ApWlanMuAclEndingMac_Type()
)
apWlanMuAclEndingMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanMuAclEndingMac.setStatus("current")
_ApWlanMuAclPointerToAclPolicy_Type = SinglePointer
_ApWlanMuAclPointerToAclPolicy_Object = MibTableColumn
apWlanMuAclPointerToAclPolicy = _ApWlanMuAclPointerToAclPolicy_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 6, 1, 4),
    _ApWlanMuAclPointerToAclPolicy_Type()
)
apWlanMuAclPointerToAclPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanMuAclPointerToAclPolicy.setStatus("current")
_ApWlanMuAclRowStatus_Type = AbbrevRowStatus
_ApWlanMuAclRowStatus_Object = MibTableColumn
apWlanMuAclRowStatus = _ApWlanMuAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 6, 1, 5),
    _ApWlanMuAclRowStatus_Type()
)
apWlanMuAclRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanMuAclRowStatus.setStatus("current")
_ApWlanQosPolicyTable_Object = MibTable
apWlanQosPolicyTable = _ApWlanQosPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7)
)
if mibBuilder.loadTexts:
    apWlanQosPolicyTable.setStatus("current")
_ApWlanQosPolicyEntry_Object = MibTableRow
apWlanQosPolicyEntry = _ApWlanQosPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1)
)
apWlanQosPolicyEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apWlanQosPolicyIndex"),
)
if mibBuilder.loadTexts:
    apWlanQosPolicyEntry.setStatus("current")


class _ApWlanQosPolicyIndex_Type(Integer32):
    """Custom type apWlanQosPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ApWlanQosPolicyIndex_Type.__name__ = "Integer32"
_ApWlanQosPolicyIndex_Object = MibTableColumn
apWlanQosPolicyIndex = _ApWlanQosPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 1),
    _ApWlanQosPolicyIndex_Type()
)
apWlanQosPolicyIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apWlanQosPolicyIndex.setStatus("current")
_ApWlanQosPolicyName_Type = DisplayString
_ApWlanQosPolicyName_Object = MibTableColumn
apWlanQosPolicyName = _ApWlanQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 2),
    _ApWlanQosPolicyName_Type()
)
apWlanQosPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanQosPolicyName.setStatus("current")
_ApWlanEnableWMM_Type = TruthValue
_ApWlanEnableWMM_Object = MibTableColumn
apWlanEnableWMM = _ApWlanEnableWMM_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 3),
    _ApWlanEnableWMM_Type()
)
apWlanEnableWMM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanEnableWMM.setStatus("current")


class _ApWlanWMMQosParam_Type(Integer32):
    """Custom type apWlanWMMQosParam based on Integer32"""
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
        *(("default11agn", 4),
          ("default11b", 5),
          ("manual", 1),
          ("voice11agn", 6),
          ("voice11b", 7),
          ("wifi11agn", 2),
          ("wifi11b", 3))
    )


_ApWlanWMMQosParam_Type.__name__ = "Integer32"
_ApWlanWMMQosParam_Object = MibTableColumn
apWlanWMMQosParam = _ApWlanWMMQosParam_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 4),
    _ApWlanWMMQosParam_Type()
)
apWlanWMMQosParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanWMMQosParam.setStatus("current")
_ApWlanQosPolicyBackgroundCwMin_Type = Integer32
_ApWlanQosPolicyBackgroundCwMin_Object = MibTableColumn
apWlanQosPolicyBackgroundCwMin = _ApWlanQosPolicyBackgroundCwMin_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 5),
    _ApWlanQosPolicyBackgroundCwMin_Type()
)
apWlanQosPolicyBackgroundCwMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanQosPolicyBackgroundCwMin.setStatus("current")
_ApWlanQosPolicyBackgroundCwMax_Type = Integer32
_ApWlanQosPolicyBackgroundCwMax_Object = MibTableColumn
apWlanQosPolicyBackgroundCwMax = _ApWlanQosPolicyBackgroundCwMax_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 6),
    _ApWlanQosPolicyBackgroundCwMax_Type()
)
apWlanQosPolicyBackgroundCwMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanQosPolicyBackgroundCwMax.setStatus("current")
_ApWlanQosPolicyBackgroundAifsn_Type = Integer32
_ApWlanQosPolicyBackgroundAifsn_Object = MibTableColumn
apWlanQosPolicyBackgroundAifsn = _ApWlanQosPolicyBackgroundAifsn_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 7),
    _ApWlanQosPolicyBackgroundAifsn_Type()
)
apWlanQosPolicyBackgroundAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanQosPolicyBackgroundAifsn.setStatus("current")
_ApWlanQosPolicyBackgroundTxopsTime_Type = Integer32
_ApWlanQosPolicyBackgroundTxopsTime_Object = MibTableColumn
apWlanQosPolicyBackgroundTxopsTime = _ApWlanQosPolicyBackgroundTxopsTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 8),
    _ApWlanQosPolicyBackgroundTxopsTime_Type()
)
apWlanQosPolicyBackgroundTxopsTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanQosPolicyBackgroundTxopsTime.setStatus("current")
_ApWlanQosPolicyBackgroundTxopsTimeInMS_Type = Integer32
_ApWlanQosPolicyBackgroundTxopsTimeInMS_Object = MibTableColumn
apWlanQosPolicyBackgroundTxopsTimeInMS = _ApWlanQosPolicyBackgroundTxopsTimeInMS_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 9),
    _ApWlanQosPolicyBackgroundTxopsTimeInMS_Type()
)
apWlanQosPolicyBackgroundTxopsTimeInMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanQosPolicyBackgroundTxopsTimeInMS.setStatus("current")
_ApWlanQosPolicyBestEffortCwMin_Type = Integer32
_ApWlanQosPolicyBestEffortCwMin_Object = MibTableColumn
apWlanQosPolicyBestEffortCwMin = _ApWlanQosPolicyBestEffortCwMin_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 10),
    _ApWlanQosPolicyBestEffortCwMin_Type()
)
apWlanQosPolicyBestEffortCwMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanQosPolicyBestEffortCwMin.setStatus("current")
_ApWlanQosPolicyBestEffortCwMax_Type = Integer32
_ApWlanQosPolicyBestEffortCwMax_Object = MibTableColumn
apWlanQosPolicyBestEffortCwMax = _ApWlanQosPolicyBestEffortCwMax_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 11),
    _ApWlanQosPolicyBestEffortCwMax_Type()
)
apWlanQosPolicyBestEffortCwMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanQosPolicyBestEffortCwMax.setStatus("current")
_ApWlanQosPolicyBestEffortAifsn_Type = Integer32
_ApWlanQosPolicyBestEffortAifsn_Object = MibTableColumn
apWlanQosPolicyBestEffortAifsn = _ApWlanQosPolicyBestEffortAifsn_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 12),
    _ApWlanQosPolicyBestEffortAifsn_Type()
)
apWlanQosPolicyBestEffortAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanQosPolicyBestEffortAifsn.setStatus("current")
_ApWlanQosPolicyBestEffortTxopsTime_Type = Integer32
_ApWlanQosPolicyBestEffortTxopsTime_Object = MibTableColumn
apWlanQosPolicyBestEffortTxopsTime = _ApWlanQosPolicyBestEffortTxopsTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 13),
    _ApWlanQosPolicyBestEffortTxopsTime_Type()
)
apWlanQosPolicyBestEffortTxopsTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanQosPolicyBestEffortTxopsTime.setStatus("current")
_ApWlanQosPolicyBestEffortTxopsTimeInMS_Type = Integer32
_ApWlanQosPolicyBestEffortTxopsTimeInMS_Object = MibTableColumn
apWlanQosPolicyBestEffortTxopsTimeInMS = _ApWlanQosPolicyBestEffortTxopsTimeInMS_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 14),
    _ApWlanQosPolicyBestEffortTxopsTimeInMS_Type()
)
apWlanQosPolicyBestEffortTxopsTimeInMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanQosPolicyBestEffortTxopsTimeInMS.setStatus("current")
_ApWlanQosPolicyVideoCwMin_Type = Integer32
_ApWlanQosPolicyVideoCwMin_Object = MibTableColumn
apWlanQosPolicyVideoCwMin = _ApWlanQosPolicyVideoCwMin_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 15),
    _ApWlanQosPolicyVideoCwMin_Type()
)
apWlanQosPolicyVideoCwMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanQosPolicyVideoCwMin.setStatus("current")
_ApWlanQosPolicyVideoCwMax_Type = Integer32
_ApWlanQosPolicyVideoCwMax_Object = MibTableColumn
apWlanQosPolicyVideoCwMax = _ApWlanQosPolicyVideoCwMax_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 16),
    _ApWlanQosPolicyVideoCwMax_Type()
)
apWlanQosPolicyVideoCwMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanQosPolicyVideoCwMax.setStatus("current")
_ApWlanQosPolicyVideoAifsn_Type = Integer32
_ApWlanQosPolicyVideoAifsn_Object = MibTableColumn
apWlanQosPolicyVideoAifsn = _ApWlanQosPolicyVideoAifsn_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 17),
    _ApWlanQosPolicyVideoAifsn_Type()
)
apWlanQosPolicyVideoAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanQosPolicyVideoAifsn.setStatus("current")
_ApWlanQosPolicyVideoTxopsTime_Type = Integer32
_ApWlanQosPolicyVideoTxopsTime_Object = MibTableColumn
apWlanQosPolicyVideoTxopsTime = _ApWlanQosPolicyVideoTxopsTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 18),
    _ApWlanQosPolicyVideoTxopsTime_Type()
)
apWlanQosPolicyVideoTxopsTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanQosPolicyVideoTxopsTime.setStatus("current")
_ApWlanQosPolicyVideoTxopsTimeInMS_Type = Integer32
_ApWlanQosPolicyVideoTxopsTimeInMS_Object = MibTableColumn
apWlanQosPolicyVideoTxopsTimeInMS = _ApWlanQosPolicyVideoTxopsTimeInMS_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 19),
    _ApWlanQosPolicyVideoTxopsTimeInMS_Type()
)
apWlanQosPolicyVideoTxopsTimeInMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanQosPolicyVideoTxopsTimeInMS.setStatus("current")
_ApWlanQosPolicyVoiceCwMin_Type = Integer32
_ApWlanQosPolicyVoiceCwMin_Object = MibTableColumn
apWlanQosPolicyVoiceCwMin = _ApWlanQosPolicyVoiceCwMin_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 20),
    _ApWlanQosPolicyVoiceCwMin_Type()
)
apWlanQosPolicyVoiceCwMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanQosPolicyVoiceCwMin.setStatus("current")
_ApWlanQosPolicyVoiceCwMax_Type = Integer32
_ApWlanQosPolicyVoiceCwMax_Object = MibTableColumn
apWlanQosPolicyVoiceCwMax = _ApWlanQosPolicyVoiceCwMax_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 21),
    _ApWlanQosPolicyVoiceCwMax_Type()
)
apWlanQosPolicyVoiceCwMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanQosPolicyVoiceCwMax.setStatus("current")
_ApWlanQosPolicyVoiceAifsn_Type = Integer32
_ApWlanQosPolicyVoiceAifsn_Object = MibTableColumn
apWlanQosPolicyVoiceAifsn = _ApWlanQosPolicyVoiceAifsn_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 22),
    _ApWlanQosPolicyVoiceAifsn_Type()
)
apWlanQosPolicyVoiceAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanQosPolicyVoiceAifsn.setStatus("current")
_ApWlanQosPolicyVoiceTxopsTime_Type = Integer32
_ApWlanQosPolicyVoiceTxopsTime_Object = MibTableColumn
apWlanQosPolicyVoiceTxopsTime = _ApWlanQosPolicyVoiceTxopsTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 23),
    _ApWlanQosPolicyVoiceTxopsTime_Type()
)
apWlanQosPolicyVoiceTxopsTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanQosPolicyVoiceTxopsTime.setStatus("current")
_ApWlanQosPolicyVoiceTxopsTimeInMS_Type = Integer32
_ApWlanQosPolicyVoiceTxopsTimeInMS_Object = MibTableColumn
apWlanQosPolicyVoiceTxopsTimeInMS = _ApWlanQosPolicyVoiceTxopsTimeInMS_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 24),
    _ApWlanQosPolicyVoiceTxopsTimeInMS_Type()
)
apWlanQosPolicyVoiceTxopsTimeInMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanQosPolicyVoiceTxopsTimeInMS.setStatus("current")
_ApWlanVoicePrioritization_Type = TruthValue
_ApWlanVoicePrioritization_Object = MibTableColumn
apWlanVoicePrioritization = _ApWlanVoicePrioritization_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 25),
    _ApWlanVoicePrioritization_Type()
)
apWlanVoicePrioritization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanVoicePrioritization.setStatus("current")
_ApWlanMulticastAddr1_Type = PhysAddress
_ApWlanMulticastAddr1_Object = MibTableColumn
apWlanMulticastAddr1 = _ApWlanMulticastAddr1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 26),
    _ApWlanMulticastAddr1_Type()
)
apWlanMulticastAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanMulticastAddr1.setStatus("current")
_ApWlanMulticastAddr2_Type = PhysAddress
_ApWlanMulticastAddr2_Object = MibTableColumn
apWlanMulticastAddr2 = _ApWlanMulticastAddr2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 27),
    _ApWlanMulticastAddr2_Type()
)
apWlanMulticastAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanMulticastAddr2.setStatus("current")
_ApWlanQosPolicyPointerToWlan_Type = MultiPointer63
_ApWlanQosPolicyPointerToWlan_Object = MibTableColumn
apWlanQosPolicyPointerToWlan = _ApWlanQosPolicyPointerToWlan_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 28),
    _ApWlanQosPolicyPointerToWlan_Type()
)
apWlanQosPolicyPointerToWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanQosPolicyPointerToWlan.setStatus("current")
_ApWlanQosPolicyRowStatus_Type = AbbrevRowStatus
_ApWlanQosPolicyRowStatus_Object = MibTableColumn
apWlanQosPolicyRowStatus = _ApWlanQosPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 7, 1, 29),
    _ApWlanQosPolicyRowStatus_Type()
)
apWlanQosPolicyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanQosPolicyRowStatus.setStatus("current")
_ApWlanBwShareModeTable_Object = MibTable
apWlanBwShareModeTable = _ApWlanBwShareModeTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 8)
)
if mibBuilder.loadTexts:
    apWlanBwShareModeTable.setStatus("current")
_ApWlanBwShareModeEntry_Object = MibTableRow
apWlanBwShareModeEntry = _ApWlanBwShareModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 8, 1)
)
apWlanBwShareModeEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apRadioSettingsIndex"),
)
if mibBuilder.loadTexts:
    apWlanBwShareModeEntry.setStatus("current")


class _ApWlanBwShareMode_Type(Integer32):
    """Custom type apWlanBwShareMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("firstInFirstOut", 0),
          ("roundRobin", 1),
          ("weightedRoundRobin", 2))
    )


_ApWlanBwShareMode_Type.__name__ = "Integer32"
_ApWlanBwShareMode_Object = MibTableColumn
apWlanBwShareMode = _ApWlanBwShareMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 2, 8, 1, 1),
    _ApWlanBwShareMode_Type()
)
apWlanBwShareMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanBwShareMode.setStatus("current")
_ApHotSpot_ObjectIdentity = ObjectIdentity
apHotSpot = _ApHotSpot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3)
)
_ApHotSpotTable_Object = MibTable
apHotSpotTable = _ApHotSpotTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 1)
)
if mibBuilder.loadTexts:
    apHotSpotTable.setStatus("current")
_ApHotSpotEntry_Object = MibTableRow
apHotSpotEntry = _ApHotSpotEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 1, 1)
)
apHotSpotEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apWlanIndex"),
)
if mibBuilder.loadTexts:
    apHotSpotEntry.setStatus("current")


class _ApHotSpotDefaultFileMode_Type(Integer32):
    """Custom type apHotSpotDefaultFileMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("externalURL", 2))
    )


_ApHotSpotDefaultFileMode_Type.__name__ = "Integer32"
_ApHotSpotDefaultFileMode_Object = MibTableColumn
apHotSpotDefaultFileMode = _ApHotSpotDefaultFileMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 1, 1, 1),
    _ApHotSpotDefaultFileMode_Type()
)
apHotSpotDefaultFileMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHotSpotDefaultFileMode.setStatus("current")
_ApHotSpotExternalLoginPageUrl_Type = DisplayString
_ApHotSpotExternalLoginPageUrl_Object = MibTableColumn
apHotSpotExternalLoginPageUrl = _ApHotSpotExternalLoginPageUrl_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 1, 1, 2),
    _ApHotSpotExternalLoginPageUrl_Type()
)
apHotSpotExternalLoginPageUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHotSpotExternalLoginPageUrl.setStatus("current")
_ApHotSpotExternalWelomePageUrl_Type = DisplayString
_ApHotSpotExternalWelomePageUrl_Object = MibTableColumn
apHotSpotExternalWelomePageUrl = _ApHotSpotExternalWelomePageUrl_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 1, 1, 3),
    _ApHotSpotExternalWelomePageUrl_Type()
)
apHotSpotExternalWelomePageUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHotSpotExternalWelomePageUrl.setStatus("current")
_ApHotSpotExternalFailPageUrl_Type = DisplayString
_ApHotSpotExternalFailPageUrl_Object = MibTableColumn
apHotSpotExternalFailPageUrl = _ApHotSpotExternalFailPageUrl_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 1, 1, 4),
    _ApHotSpotExternalFailPageUrl_Type()
)
apHotSpotExternalFailPageUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHotSpotExternalFailPageUrl.setStatus("current")
_ApHotSpotPriRadiusServerIp_Type = IpAddress
_ApHotSpotPriRadiusServerIp_Object = MibTableColumn
apHotSpotPriRadiusServerIp = _ApHotSpotPriRadiusServerIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 1, 1, 5),
    _ApHotSpotPriRadiusServerIp_Type()
)
apHotSpotPriRadiusServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHotSpotPriRadiusServerIp.setStatus("current")
_ApHotSpotPriRadiusPort_Type = Integer32
_ApHotSpotPriRadiusPort_Object = MibTableColumn
apHotSpotPriRadiusPort = _ApHotSpotPriRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 1, 1, 6),
    _ApHotSpotPriRadiusPort_Type()
)
apHotSpotPriRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHotSpotPriRadiusPort.setStatus("current")
_ApHotSpotPriRadiusSecret_Type = Password
_ApHotSpotPriRadiusSecret_Object = MibTableColumn
apHotSpotPriRadiusSecret = _ApHotSpotPriRadiusSecret_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 1, 1, 7),
    _ApHotSpotPriRadiusSecret_Type()
)
apHotSpotPriRadiusSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHotSpotPriRadiusSecret.setStatus("current")
_ApHotSpotSecRadiusServerIp_Type = IpAddress
_ApHotSpotSecRadiusServerIp_Object = MibTableColumn
apHotSpotSecRadiusServerIp = _ApHotSpotSecRadiusServerIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 1, 1, 8),
    _ApHotSpotSecRadiusServerIp_Type()
)
apHotSpotSecRadiusServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHotSpotSecRadiusServerIp.setStatus("current")
_ApHotSpotSecRadiusPort_Type = Integer32
_ApHotSpotSecRadiusPort_Object = MibTableColumn
apHotSpotSecRadiusPort = _ApHotSpotSecRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 1, 1, 9),
    _ApHotSpotSecRadiusPort_Type()
)
apHotSpotSecRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHotSpotSecRadiusPort.setStatus("current")
_ApHotSpotSecRadiusSecret_Type = Password
_ApHotSpotSecRadiusSecret_Object = MibTableColumn
apHotSpotSecRadiusSecret = _ApHotSpotSecRadiusSecret_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 1, 1, 10),
    _ApHotSpotSecRadiusSecret_Type()
)
apHotSpotSecRadiusSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHotSpotSecRadiusSecret.setStatus("current")
_ApHotSpotRadiusAcctMode_Type = TruthValue
_ApHotSpotRadiusAcctMode_Object = MibTableColumn
apHotSpotRadiusAcctMode = _ApHotSpotRadiusAcctMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 1, 1, 11),
    _ApHotSpotRadiusAcctMode_Type()
)
apHotSpotRadiusAcctMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHotSpotRadiusAcctMode.setStatus("current")
_ApHotSpotRadiusAcctServerIp_Type = IpAddress
_ApHotSpotRadiusAcctServerIp_Object = MibTableColumn
apHotSpotRadiusAcctServerIp = _ApHotSpotRadiusAcctServerIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 1, 1, 12),
    _ApHotSpotRadiusAcctServerIp_Type()
)
apHotSpotRadiusAcctServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHotSpotRadiusAcctServerIp.setStatus("current")
_ApHotSpotRadiusAcctPort_Type = Integer32
_ApHotSpotRadiusAcctPort_Object = MibTableColumn
apHotSpotRadiusAcctPort = _ApHotSpotRadiusAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 1, 1, 13),
    _ApHotSpotRadiusAcctPort_Type()
)
apHotSpotRadiusAcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHotSpotRadiusAcctPort.setStatus("current")
_ApHotSpotRadiusAcctSecret_Type = Password
_ApHotSpotRadiusAcctSecret_Object = MibTableColumn
apHotSpotRadiusAcctSecret = _ApHotSpotRadiusAcctSecret_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 1, 1, 14),
    _ApHotSpotRadiusAcctSecret_Type()
)
apHotSpotRadiusAcctSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHotSpotRadiusAcctSecret.setStatus("current")


class _ApHotSpotRadiusAcctTimeout_Type(Integer32):
    """Custom type apHotSpotRadiusAcctTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ApHotSpotRadiusAcctTimeout_Type.__name__ = "Integer32"
_ApHotSpotRadiusAcctTimeout_Object = MibTableColumn
apHotSpotRadiusAcctTimeout = _ApHotSpotRadiusAcctTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 1, 1, 15),
    _ApHotSpotRadiusAcctTimeout_Type()
)
apHotSpotRadiusAcctTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHotSpotRadiusAcctTimeout.setStatus("current")


class _ApHotSpotRadiusAcctRetryCount_Type(Integer32):
    """Custom type apHotSpotRadiusAcctRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ApHotSpotRadiusAcctRetryCount_Type.__name__ = "Integer32"
_ApHotSpotRadiusAcctRetryCount_Object = MibTableColumn
apHotSpotRadiusAcctRetryCount = _ApHotSpotRadiusAcctRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 1, 1, 16),
    _ApHotSpotRadiusAcctRetryCount_Type()
)
apHotSpotRadiusAcctRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHotSpotRadiusAcctRetryCount.setStatus("current")
_ApHotSpotRadiusSessMode_Type = TruthValue
_ApHotSpotRadiusSessMode_Object = MibTableColumn
apHotSpotRadiusSessMode = _ApHotSpotRadiusSessMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 1, 1, 17),
    _ApHotSpotRadiusSessMode_Type()
)
apHotSpotRadiusSessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHotSpotRadiusSessMode.setStatus("current")
_ApHotSpotRadiusSessTimeout_Type = Integer32
_ApHotSpotRadiusSessTimeout_Object = MibTableColumn
apHotSpotRadiusSessTimeout = _ApHotSpotRadiusSessTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 1, 1, 18),
    _ApHotSpotRadiusSessTimeout_Type()
)
apHotSpotRadiusSessTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHotSpotRadiusSessTimeout.setStatus("current")
_ApHotSpotWhiteListTable_Object = MibTable
apHotSpotWhiteListTable = _ApHotSpotWhiteListTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 2)
)
if mibBuilder.loadTexts:
    apHotSpotWhiteListTable.setStatus("current")
_ApHotSpotWhiteListEntry_Object = MibTableRow
apHotSpotWhiteListEntry = _ApHotSpotWhiteListEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 2, 1)
)
apHotSpotWhiteListEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apWlanIndex"),
    (0, "SYMBOL-AP-MIB", "apHotSpotWhiteListIndex"),
)
if mibBuilder.loadTexts:
    apHotSpotWhiteListEntry.setStatus("current")


class _ApHotSpotWhiteListIndex_Type(Integer32):
    """Custom type apHotSpotWhiteListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ApHotSpotWhiteListIndex_Type.__name__ = "Integer32"
_ApHotSpotWhiteListIndex_Object = MibTableColumn
apHotSpotWhiteListIndex = _ApHotSpotWhiteListIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 2, 1, 1),
    _ApHotSpotWhiteListIndex_Type()
)
apHotSpotWhiteListIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apHotSpotWhiteListIndex.setStatus("current")
_ApHotSpotWhiteListWalledGardenIp_Type = IpAddress
_ApHotSpotWhiteListWalledGardenIp_Object = MibTableColumn
apHotSpotWhiteListWalledGardenIp = _ApHotSpotWhiteListWalledGardenIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 2, 1, 2),
    _ApHotSpotWhiteListWalledGardenIp_Type()
)
apHotSpotWhiteListWalledGardenIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHotSpotWhiteListWalledGardenIp.setStatus("current")
_ApHotSpotWhiteListRowStatus_Type = AbbrevRowStatus
_ApHotSpotWhiteListRowStatus_Object = MibTableColumn
apHotSpotWhiteListRowStatus = _ApHotSpotWhiteListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 3, 2, 1, 3),
    _ApHotSpotWhiteListRowStatus_Type()
)
apHotSpotWhiteListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHotSpotWhiteListRowStatus.setStatus("current")
_ApMus_ObjectIdentity = ObjectIdentity
apMus = _ApMus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 4)
)
_ApMuLocationing_ObjectIdentity = ObjectIdentity
apMuLocationing = _ApMuLocationing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 4, 1)
)
_ApMuLocationingEnable_Type = TruthValue
_ApMuLocationingEnable_Object = MibScalar
apMuLocationingEnable = _ApMuLocationingEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 4, 1, 1),
    _ApMuLocationingEnable_Type()
)
apMuLocationingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMuLocationingEnable.setStatus("current")
_ApMuLocationingClear_Type = DoActionNow
_ApMuLocationingClear_Object = MibScalar
apMuLocationingClear = _ApMuLocationingClear_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 4, 1, 2),
    _ApMuLocationingClear_Type()
)
apMuLocationingClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMuLocationingClear.setStatus("current")


class _ApMuLocationingMaxMus_Type(Integer32):
    """Custom type apMuLocationingMaxMus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 200),
    )


_ApMuLocationingMaxMus_Type.__name__ = "Integer32"
_ApMuLocationingMaxMus_Object = MibScalar
apMuLocationingMaxMus = _ApMuLocationingMaxMus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 4, 1, 3),
    _ApMuLocationingMaxMus_Type()
)
apMuLocationingMaxMus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMuLocationingMaxMus.setStatus("current")
_ApMuLocationingTable_Object = MibTable
apMuLocationingTable = _ApMuLocationingTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 4, 1, 4)
)
if mibBuilder.loadTexts:
    apMuLocationingTable.setStatus("current")
_ApMuLocationingEntry_Object = MibTableRow
apMuLocationingEntry = _ApMuLocationingEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 4, 1, 4, 1)
)
apMuLocationingEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apMuLocationingIndex"),
)
if mibBuilder.loadTexts:
    apMuLocationingEntry.setStatus("current")


class _ApMuLocationingIndex_Type(Integer32):
    """Custom type apMuLocationingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2400),
    )


_ApMuLocationingIndex_Type.__name__ = "Integer32"
_ApMuLocationingIndex_Object = MibTableColumn
apMuLocationingIndex = _ApMuLocationingIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 4, 1, 4, 1, 1),
    _ApMuLocationingIndex_Type()
)
apMuLocationingIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apMuLocationingIndex.setStatus("current")
_ApMuLocationingMuMac_Type = PhysAddress
_ApMuLocationingMuMac_Object = MibTableColumn
apMuLocationingMuMac = _ApMuLocationingMuMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 4, 1, 4, 1, 2),
    _ApMuLocationingMuMac_Type()
)
apMuLocationingMuMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMuLocationingMuMac.setStatus("current")
_ApMuLocationingPortalMac_Type = PhysAddress
_ApMuLocationingPortalMac_Object = MibTableColumn
apMuLocationingPortalMac = _ApMuLocationingPortalMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 4, 1, 4, 1, 3),
    _ApMuLocationingPortalMac_Type()
)
apMuLocationingPortalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMuLocationingPortalMac.setStatus("current")
_ApMuLocationingSignalStrength_Type = Integer32
_ApMuLocationingSignalStrength_Object = MibTableColumn
apMuLocationingSignalStrength = _ApMuLocationingSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 4, 1, 4, 1, 4),
    _ApMuLocationingSignalStrength_Type()
)
apMuLocationingSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMuLocationingSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    apMuLocationingSignalStrength.setUnits("dBm")
_ApMuLocationingHeardChannel_Type = Integer32
_ApMuLocationingHeardChannel_Object = MibTableColumn
apMuLocationingHeardChannel = _ApMuLocationingHeardChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 4, 1, 4, 1, 5),
    _ApMuLocationingHeardChannel_Type()
)
apMuLocationingHeardChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMuLocationingHeardChannel.setStatus("current")
_ApMuLocationingHeardTime_Type = TimeTicks
_ApMuLocationingHeardTime_Object = MibTableColumn
apMuLocationingHeardTime = _ApMuLocationingHeardTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 4, 1, 4, 1, 6),
    _ApMuLocationingHeardTime_Type()
)
apMuLocationingHeardTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMuLocationingHeardTime.setStatus("current")
_ApMuLocationingAddEntryToTable_Object = MibTable
apMuLocationingAddEntryToTable = _ApMuLocationingAddEntryToTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 4, 1, 5)
)
if mibBuilder.loadTexts:
    apMuLocationingAddEntryToTable.setStatus("current")
_ApMuLocationingAddEntryToEntry_Object = MibTableRow
apMuLocationingAddEntryToEntry = _ApMuLocationingAddEntryToEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 4, 1, 5, 1)
)
apMuLocationingAddEntryToEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apMuLocationingIndex"),
)
if mibBuilder.loadTexts:
    apMuLocationingAddEntryToEntry.setStatus("current")
_ApMuLocationingAddMuMac_Type = PhysAddress
_ApMuLocationingAddMuMac_Object = MibTableColumn
apMuLocationingAddMuMac = _ApMuLocationingAddMuMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 4, 1, 5, 1, 1),
    _ApMuLocationingAddMuMac_Type()
)
apMuLocationingAddMuMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMuLocationingAddMuMac.setStatus("current")
_ApMuLocationingAddPortalMac_Type = PhysAddress
_ApMuLocationingAddPortalMac_Object = MibTableColumn
apMuLocationingAddPortalMac = _ApMuLocationingAddPortalMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 4, 1, 5, 1, 2),
    _ApMuLocationingAddPortalMac_Type()
)
apMuLocationingAddPortalMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMuLocationingAddPortalMac.setStatus("current")
_ApMuLocationingAddSignalStrength_Type = Integer32
_ApMuLocationingAddSignalStrength_Object = MibTableColumn
apMuLocationingAddSignalStrength = _ApMuLocationingAddSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 4, 1, 5, 1, 3),
    _ApMuLocationingAddSignalStrength_Type()
)
apMuLocationingAddSignalStrength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMuLocationingAddSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    apMuLocationingAddSignalStrength.setUnits("dBm")
_ApMuLocationingAddHeardChannel_Type = Integer32
_ApMuLocationingAddHeardChannel_Object = MibTableColumn
apMuLocationingAddHeardChannel = _ApMuLocationingAddHeardChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 4, 1, 5, 1, 4),
    _ApMuLocationingAddHeardChannel_Type()
)
apMuLocationingAddHeardChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMuLocationingAddHeardChannel.setStatus("current")
_ApMuLocationingAddHeardTime_Type = TimeTicks
_ApMuLocationingAddHeardTime_Object = MibTableColumn
apMuLocationingAddHeardTime = _ApMuLocationingAddHeardTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 4, 1, 5, 1, 5),
    _ApMuLocationingAddHeardTime_Type()
)
apMuLocationingAddHeardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMuLocationingAddHeardTime.setStatus("current")
_ApIpFilter_ObjectIdentity = ObjectIdentity
apIpFilter = _ApIpFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5)
)
_ApIpFilterPolicyTable_Object = MibTable
apIpFilterPolicyTable = _ApIpFilterPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 1)
)
if mibBuilder.loadTexts:
    apIpFilterPolicyTable.setStatus("current")
_ApIpFilterPolicyEntry_Object = MibTableRow
apIpFilterPolicyEntry = _ApIpFilterPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 1, 1)
)
apIpFilterPolicyEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apIpFilterPolicyIndex"),
)
if mibBuilder.loadTexts:
    apIpFilterPolicyEntry.setStatus("current")


class _ApIpFilterPolicyIndex_Type(Integer32):
    """Custom type apIpFilterPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ApIpFilterPolicyIndex_Type.__name__ = "Integer32"
_ApIpFilterPolicyIndex_Object = MibTableColumn
apIpFilterPolicyIndex = _ApIpFilterPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 1, 1, 1),
    _ApIpFilterPolicyIndex_Type()
)
apIpFilterPolicyIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apIpFilterPolicyIndex.setStatus("current")
_ApIpFilterPolicyName_Type = DisplayString
_ApIpFilterPolicyName_Object = MibTableColumn
apIpFilterPolicyName = _ApIpFilterPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 1, 1, 2),
    _ApIpFilterPolicyName_Type()
)
apIpFilterPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterPolicyName.setStatus("current")


class _ApIpFilterPolicyProtocol_Type(Integer32):
    """Custom type apIpFilterPolicyProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              12,
              17,
              22,
              41,
              46,
              47,
              50,
              51,
              103,
              108,
              255,
              256)
        )
    )
    namedValues = NamedValues(
        *(("ah", 51),
          ("all", 256),
          ("comp", 108),
          ("egp", 8),
          ("esp", 50),
          ("gre", 47),
          ("icmp", 1),
          ("idp", 22),
          ("igmp", 2),
          ("ipip", 4),
          ("ipv6", 41),
          ("pim", 103),
          ("pup", 12),
          ("rawip", 255),
          ("rsvp", 46),
          ("tcp", 6),
          ("udp", 17))
    )


_ApIpFilterPolicyProtocol_Type.__name__ = "Integer32"
_ApIpFilterPolicyProtocol_Object = MibTableColumn
apIpFilterPolicyProtocol = _ApIpFilterPolicyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 1, 1, 3),
    _ApIpFilterPolicyProtocol_Type()
)
apIpFilterPolicyProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterPolicyProtocol.setStatus("current")


class _ApIpFilterPolicyStartPort_Type(Integer32):
    """Custom type apIpFilterPolicyStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApIpFilterPolicyStartPort_Type.__name__ = "Integer32"
_ApIpFilterPolicyStartPort_Object = MibTableColumn
apIpFilterPolicyStartPort = _ApIpFilterPolicyStartPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 1, 1, 4),
    _ApIpFilterPolicyStartPort_Type()
)
apIpFilterPolicyStartPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterPolicyStartPort.setStatus("current")


class _ApIpFilterPolicyEndPort_Type(Integer32):
    """Custom type apIpFilterPolicyEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApIpFilterPolicyEndPort_Type.__name__ = "Integer32"
_ApIpFilterPolicyEndPort_Object = MibTableColumn
apIpFilterPolicyEndPort = _ApIpFilterPolicyEndPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 1, 1, 5),
    _ApIpFilterPolicyEndPort_Type()
)
apIpFilterPolicyEndPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterPolicyEndPort.setStatus("current")
_ApIpFilterPolicySrcStartIp_Type = IpAddress
_ApIpFilterPolicySrcStartIp_Object = MibTableColumn
apIpFilterPolicySrcStartIp = _ApIpFilterPolicySrcStartIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 1, 1, 6),
    _ApIpFilterPolicySrcStartIp_Type()
)
apIpFilterPolicySrcStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterPolicySrcStartIp.setStatus("current")
_ApIpFilterPolicySrcEndIp_Type = IpAddress
_ApIpFilterPolicySrcEndIp_Object = MibTableColumn
apIpFilterPolicySrcEndIp = _ApIpFilterPolicySrcEndIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 1, 1, 7),
    _ApIpFilterPolicySrcEndIp_Type()
)
apIpFilterPolicySrcEndIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterPolicySrcEndIp.setStatus("current")
_ApIpFilterPolicyDestStartIp_Type = IpAddress
_ApIpFilterPolicyDestStartIp_Object = MibTableColumn
apIpFilterPolicyDestStartIp = _ApIpFilterPolicyDestStartIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 1, 1, 8),
    _ApIpFilterPolicyDestStartIp_Type()
)
apIpFilterPolicyDestStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterPolicyDestStartIp.setStatus("current")
_ApIpFilterPolicyDestEndIp_Type = IpAddress
_ApIpFilterPolicyDestEndIp_Object = MibTableColumn
apIpFilterPolicyDestEndIp = _ApIpFilterPolicyDestEndIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 1, 1, 9),
    _ApIpFilterPolicyDestEndIp_Type()
)
apIpFilterPolicyDestEndIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterPolicyDestEndIp.setStatus("current")
_ApIpFilterPolicyUseStatus_Type = DisplayString
_ApIpFilterPolicyUseStatus_Object = MibTableColumn
apIpFilterPolicyUseStatus = _ApIpFilterPolicyUseStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 1, 1, 10),
    _ApIpFilterPolicyUseStatus_Type()
)
apIpFilterPolicyUseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpFilterPolicyUseStatus.setStatus("current")
_ApIpFilterPolicyRowStatus_Type = AbbrevRowStatus
_ApIpFilterPolicyRowStatus_Object = MibTableColumn
apIpFilterPolicyRowStatus = _ApIpFilterPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 1, 1, 11),
    _ApIpFilterPolicyRowStatus_Type()
)
apIpFilterPolicyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterPolicyRowStatus.setStatus("current")


class _ApIpFilterPolicySrcStartPort_Type(Integer32):
    """Custom type apIpFilterPolicySrcStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApIpFilterPolicySrcStartPort_Type.__name__ = "Integer32"
_ApIpFilterPolicySrcStartPort_Object = MibTableColumn
apIpFilterPolicySrcStartPort = _ApIpFilterPolicySrcStartPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 1, 1, 12),
    _ApIpFilterPolicySrcStartPort_Type()
)
apIpFilterPolicySrcStartPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterPolicySrcStartPort.setStatus("current")


class _ApIpFilterPolicySrcEndPort_Type(Integer32):
    """Custom type apIpFilterPolicySrcEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApIpFilterPolicySrcEndPort_Type.__name__ = "Integer32"
_ApIpFilterPolicySrcEndPort_Object = MibTableColumn
apIpFilterPolicySrcEndPort = _ApIpFilterPolicySrcEndPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 1, 1, 13),
    _ApIpFilterPolicySrcEndPort_Type()
)
apIpFilterPolicySrcEndPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterPolicySrcEndPort.setStatus("current")
_ApIpFilterWlan_ObjectIdentity = ObjectIdentity
apIpFilterWlan = _ApIpFilterWlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 2)
)
_ApIpFilterWlanTable_Object = MibTable
apIpFilterWlanTable = _ApIpFilterWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 2, 1)
)
if mibBuilder.loadTexts:
    apIpFilterWlanTable.setStatus("current")
_ApIpFilterWlanEntry_Object = MibTableRow
apIpFilterWlanEntry = _ApIpFilterWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 2, 1, 1)
)
apIpFilterWlanEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apWlanIndex"),
)
if mibBuilder.loadTexts:
    apIpFilterWlanEntry.setStatus("current")
_ApIpFilterWlanMode_Type = TruthValue
_ApIpFilterWlanMode_Object = MibTableColumn
apIpFilterWlanMode = _ApIpFilterWlanMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 2, 1, 1, 1),
    _ApIpFilterWlanMode_Type()
)
apIpFilterWlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterWlanMode.setStatus("current")


class _ApIpFilterWlanDefInAction_Type(Integer32):
    """Custom type apIpFilterWlanDefInAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_ApIpFilterWlanDefInAction_Type.__name__ = "Integer32"
_ApIpFilterWlanDefInAction_Object = MibTableColumn
apIpFilterWlanDefInAction = _ApIpFilterWlanDefInAction_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 2, 1, 1, 2),
    _ApIpFilterWlanDefInAction_Type()
)
apIpFilterWlanDefInAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterWlanDefInAction.setStatus("current")


class _ApIpFilterWlanDefOutAction_Type(Integer32):
    """Custom type apIpFilterWlanDefOutAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_ApIpFilterWlanDefOutAction_Type.__name__ = "Integer32"
_ApIpFilterWlanDefOutAction_Object = MibTableColumn
apIpFilterWlanDefOutAction = _ApIpFilterWlanDefOutAction_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 2, 1, 1, 3),
    _ApIpFilterWlanDefOutAction_Type()
)
apIpFilterWlanDefOutAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterWlanDefOutAction.setStatus("current")
_ApIpFilterWlanInPackets_Type = Counter32
_ApIpFilterWlanInPackets_Object = MibTableColumn
apIpFilterWlanInPackets = _ApIpFilterWlanInPackets_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 2, 1, 1, 4),
    _ApIpFilterWlanInPackets_Type()
)
apIpFilterWlanInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpFilterWlanInPackets.setStatus("current")
_ApIpFilterWlanOutPackets_Type = Counter32
_ApIpFilterWlanOutPackets_Object = MibTableColumn
apIpFilterWlanOutPackets = _ApIpFilterWlanOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 2, 1, 1, 5),
    _ApIpFilterWlanOutPackets_Type()
)
apIpFilterWlanOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpFilterWlanOutPackets.setStatus("current")
_ApIpFilterWlanPolicyTable_Object = MibTable
apIpFilterWlanPolicyTable = _ApIpFilterWlanPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 2, 2)
)
if mibBuilder.loadTexts:
    apIpFilterWlanPolicyTable.setStatus("current")
_ApIpFilterWlanPolicyEntry_Object = MibTableRow
apIpFilterWlanPolicyEntry = _ApIpFilterWlanPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 2, 2, 1)
)
apIpFilterWlanPolicyEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apWlanIndex"),
    (0, "SYMBOL-AP-MIB", "apIpFilterWlanPolicyIndex"),
)
if mibBuilder.loadTexts:
    apIpFilterWlanPolicyEntry.setStatus("current")


class _ApIpFilterWlanPolicyIndex_Type(Integer32):
    """Custom type apIpFilterWlanPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ApIpFilterWlanPolicyIndex_Type.__name__ = "Integer32"
_ApIpFilterWlanPolicyIndex_Object = MibTableColumn
apIpFilterWlanPolicyIndex = _ApIpFilterWlanPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 2, 2, 1, 1),
    _ApIpFilterWlanPolicyIndex_Type()
)
apIpFilterWlanPolicyIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apIpFilterWlanPolicyIndex.setStatus("current")
_ApIpFilterWlanPolicyPolicy_Type = DisplayString
_ApIpFilterWlanPolicyPolicy_Object = MibTableColumn
apIpFilterWlanPolicyPolicy = _ApIpFilterWlanPolicyPolicy_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 2, 2, 1, 2),
    _ApIpFilterWlanPolicyPolicy_Type()
)
apIpFilterWlanPolicyPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterWlanPolicyPolicy.setStatus("current")


class _ApIpFilterWlanPolicyDirection_Type(Integer32):
    """Custom type apIpFilterWlanPolicyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_ApIpFilterWlanPolicyDirection_Type.__name__ = "Integer32"
_ApIpFilterWlanPolicyDirection_Object = MibTableColumn
apIpFilterWlanPolicyDirection = _ApIpFilterWlanPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 2, 2, 1, 3),
    _ApIpFilterWlanPolicyDirection_Type()
)
apIpFilterWlanPolicyDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterWlanPolicyDirection.setStatus("current")


class _ApIpFilterWlanPolicyAction_Type(Integer32):
    """Custom type apIpFilterWlanPolicyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_ApIpFilterWlanPolicyAction_Type.__name__ = "Integer32"
_ApIpFilterWlanPolicyAction_Object = MibTableColumn
apIpFilterWlanPolicyAction = _ApIpFilterWlanPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 2, 2, 1, 4),
    _ApIpFilterWlanPolicyAction_Type()
)
apIpFilterWlanPolicyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterWlanPolicyAction.setStatus("current")
_ApIpFilterWlanPolicyRowStatus_Type = AbbrevRowStatus
_ApIpFilterWlanPolicyRowStatus_Object = MibTableColumn
apIpFilterWlanPolicyRowStatus = _ApIpFilterWlanPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 2, 2, 1, 5),
    _ApIpFilterWlanPolicyRowStatus_Type()
)
apIpFilterWlanPolicyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterWlanPolicyRowStatus.setStatus("current")
_ApIpFilterWlanPolicyPackets_Type = Counter32
_ApIpFilterWlanPolicyPackets_Object = MibTableColumn
apIpFilterWlanPolicyPackets = _ApIpFilterWlanPolicyPackets_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 2, 2, 1, 6),
    _ApIpFilterWlanPolicyPackets_Type()
)
apIpFilterWlanPolicyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpFilterWlanPolicyPackets.setStatus("current")
_ApIpFilterLan_ObjectIdentity = ObjectIdentity
apIpFilterLan = _ApIpFilterLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 3)
)
_ApIpFilterLanTable_Object = MibTable
apIpFilterLanTable = _ApIpFilterLanTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 3, 1)
)
if mibBuilder.loadTexts:
    apIpFilterLanTable.setStatus("current")
_ApIpFilterLanEntry_Object = MibTableRow
apIpFilterLanEntry = _ApIpFilterLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 3, 1, 1)
)
apIpFilterLanEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apIpFilterLanIndex"),
)
if mibBuilder.loadTexts:
    apIpFilterLanEntry.setStatus("current")


class _ApIpFilterLanIndex_Type(Integer32):
    """Custom type apIpFilterLanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ApIpFilterLanIndex_Type.__name__ = "Integer32"
_ApIpFilterLanIndex_Object = MibTableColumn
apIpFilterLanIndex = _ApIpFilterLanIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 3, 1, 1, 1),
    _ApIpFilterLanIndex_Type()
)
apIpFilterLanIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apIpFilterLanIndex.setStatus("current")
_ApIpFilterLanMode_Type = TruthValue
_ApIpFilterLanMode_Object = MibTableColumn
apIpFilterLanMode = _ApIpFilterLanMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 3, 1, 1, 2),
    _ApIpFilterLanMode_Type()
)
apIpFilterLanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterLanMode.setStatus("current")


class _ApIpFilterLanDefInAction_Type(Integer32):
    """Custom type apIpFilterLanDefInAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_ApIpFilterLanDefInAction_Type.__name__ = "Integer32"
_ApIpFilterLanDefInAction_Object = MibTableColumn
apIpFilterLanDefInAction = _ApIpFilterLanDefInAction_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 3, 1, 1, 3),
    _ApIpFilterLanDefInAction_Type()
)
apIpFilterLanDefInAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterLanDefInAction.setStatus("current")


class _ApIpFilterLanDefOutAction_Type(Integer32):
    """Custom type apIpFilterLanDefOutAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_ApIpFilterLanDefOutAction_Type.__name__ = "Integer32"
_ApIpFilterLanDefOutAction_Object = MibTableColumn
apIpFilterLanDefOutAction = _ApIpFilterLanDefOutAction_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 3, 1, 1, 4),
    _ApIpFilterLanDefOutAction_Type()
)
apIpFilterLanDefOutAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterLanDefOutAction.setStatus("current")
_ApIpFilterLanInPackets_Type = Counter32
_ApIpFilterLanInPackets_Object = MibTableColumn
apIpFilterLanInPackets = _ApIpFilterLanInPackets_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 3, 1, 1, 5),
    _ApIpFilterLanInPackets_Type()
)
apIpFilterLanInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpFilterLanInPackets.setStatus("current")
_ApIpFilterLanOutPackets_Type = Counter32
_ApIpFilterLanOutPackets_Object = MibTableColumn
apIpFilterLanOutPackets = _ApIpFilterLanOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 3, 1, 1, 6),
    _ApIpFilterLanOutPackets_Type()
)
apIpFilterLanOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpFilterLanOutPackets.setStatus("current")
_ApIpFilterLanPolicyTable_Object = MibTable
apIpFilterLanPolicyTable = _ApIpFilterLanPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 3, 2)
)
if mibBuilder.loadTexts:
    apIpFilterLanPolicyTable.setStatus("current")
_ApIpFilterLanPolicyEntry_Object = MibTableRow
apIpFilterLanPolicyEntry = _ApIpFilterLanPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 3, 2, 1)
)
apIpFilterLanPolicyEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apIpFilterLanIndex"),
    (0, "SYMBOL-AP-MIB", "apIpFilterLanPolicyIndex"),
)
if mibBuilder.loadTexts:
    apIpFilterLanPolicyEntry.setStatus("current")


class _ApIpFilterLanPolicyIndex_Type(Integer32):
    """Custom type apIpFilterLanPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ApIpFilterLanPolicyIndex_Type.__name__ = "Integer32"
_ApIpFilterLanPolicyIndex_Object = MibTableColumn
apIpFilterLanPolicyIndex = _ApIpFilterLanPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 3, 2, 1, 1),
    _ApIpFilterLanPolicyIndex_Type()
)
apIpFilterLanPolicyIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apIpFilterLanPolicyIndex.setStatus("current")
_ApIpFilterLanPolicyPolicy_Type = DisplayString
_ApIpFilterLanPolicyPolicy_Object = MibTableColumn
apIpFilterLanPolicyPolicy = _ApIpFilterLanPolicyPolicy_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 3, 2, 1, 2),
    _ApIpFilterLanPolicyPolicy_Type()
)
apIpFilterLanPolicyPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterLanPolicyPolicy.setStatus("current")


class _ApIpFilterLanPolicyDirection_Type(Integer32):
    """Custom type apIpFilterLanPolicyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_ApIpFilterLanPolicyDirection_Type.__name__ = "Integer32"
_ApIpFilterLanPolicyDirection_Object = MibTableColumn
apIpFilterLanPolicyDirection = _ApIpFilterLanPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 3, 2, 1, 3),
    _ApIpFilterLanPolicyDirection_Type()
)
apIpFilterLanPolicyDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterLanPolicyDirection.setStatus("current")


class _ApIpFilterLanPolicyAction_Type(Integer32):
    """Custom type apIpFilterLanPolicyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_ApIpFilterLanPolicyAction_Type.__name__ = "Integer32"
_ApIpFilterLanPolicyAction_Object = MibTableColumn
apIpFilterLanPolicyAction = _ApIpFilterLanPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 3, 2, 1, 4),
    _ApIpFilterLanPolicyAction_Type()
)
apIpFilterLanPolicyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterLanPolicyAction.setStatus("current")
_ApIpFilterLanPolicyRowStatus_Type = AbbrevRowStatus
_ApIpFilterLanPolicyRowStatus_Object = MibTableColumn
apIpFilterLanPolicyRowStatus = _ApIpFilterLanPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 3, 2, 1, 5),
    _ApIpFilterLanPolicyRowStatus_Type()
)
apIpFilterLanPolicyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpFilterLanPolicyRowStatus.setStatus("current")
_ApIpFilterLanPolicyPackets_Type = Counter32
_ApIpFilterLanPolicyPackets_Object = MibTableColumn
apIpFilterLanPolicyPackets = _ApIpFilterLanPolicyPackets_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 5, 3, 2, 1, 6),
    _ApIpFilterLanPolicyPackets_Type()
)
apIpFilterLanPolicyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpFilterLanPolicyPackets.setStatus("current")
_ApReliableMulticast_ObjectIdentity = ObjectIdentity
apReliableMulticast = _ApReliableMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 6)
)
_ApReliableMulticastMode_Type = TruthValue
_ApReliableMulticastMode_Object = MibScalar
apReliableMulticastMode = _ApReliableMulticastMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 6, 1),
    _ApReliableMulticastMode_Type()
)
apReliableMulticastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apReliableMulticastMode.setStatus("current")
_ApReliableMulticastWlan_Type = DisplayString
_ApReliableMulticastWlan_Object = MibScalar
apReliableMulticastWlan = _ApReliableMulticastWlan_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 6, 2),
    _ApReliableMulticastWlan_Type()
)
apReliableMulticastWlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apReliableMulticastWlan.setStatus("current")


class _ApReliableMulticastMaxStreams_Type(Integer32):
    """Custom type apReliableMulticastMaxStreams based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ApReliableMulticastMaxStreams_Type.__name__ = "Integer32"
_ApReliableMulticastMaxStreams_Object = MibScalar
apReliableMulticastMaxStreams = _ApReliableMulticastMaxStreams_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 6, 3),
    _ApReliableMulticastMaxStreams_Type()
)
apReliableMulticastMaxStreams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apReliableMulticastMaxStreams.setStatus("current")
_ApReliableMulticastStandaloneMode_Type = TruthValue
_ApReliableMulticastStandaloneMode_Object = MibScalar
apReliableMulticastStandaloneMode = _ApReliableMulticastStandaloneMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 6, 4),
    _ApReliableMulticastStandaloneMode_Type()
)
apReliableMulticastStandaloneMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apReliableMulticastStandaloneMode.setStatus("current")


class _ApReliableMulticastIgmpQueryVersion_Type(Integer32):
    """Custom type apReliableMulticastIgmpQueryVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igmpv1", 1),
          ("igmpv2", 2),
          ("igmpv3", 3))
    )


_ApReliableMulticastIgmpQueryVersion_Type.__name__ = "Integer32"
_ApReliableMulticastIgmpQueryVersion_Object = MibScalar
apReliableMulticastIgmpQueryVersion = _ApReliableMulticastIgmpQueryVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 6, 5),
    _ApReliableMulticastIgmpQueryVersion_Type()
)
apReliableMulticastIgmpQueryVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apReliableMulticastIgmpQueryVersion.setStatus("current")


class _ApReliableMulticastIgmpQueryInterval_Type(Integer32):
    """Custom type apReliableMulticastIgmpQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_ApReliableMulticastIgmpQueryInterval_Type.__name__ = "Integer32"
_ApReliableMulticastIgmpQueryInterval_Object = MibScalar
apReliableMulticastIgmpQueryInterval = _ApReliableMulticastIgmpQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 6, 6),
    _ApReliableMulticastIgmpQueryInterval_Type()
)
apReliableMulticastIgmpQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apReliableMulticastIgmpQueryInterval.setStatus("current")
_ApReliableMulticastTxMulticast_Type = TruthValue
_ApReliableMulticastTxMulticast_Object = MibScalar
apReliableMulticastTxMulticast = _ApReliableMulticastTxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 6, 7),
    _ApReliableMulticastTxMulticast_Type()
)
apReliableMulticastTxMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apReliableMulticastTxMulticast.setStatus("current")
_ApReliableMulticastTable_Object = MibTable
apReliableMulticastTable = _ApReliableMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 6, 8)
)
if mibBuilder.loadTexts:
    apReliableMulticastTable.setStatus("current")
_ApReliableMulticastEntry_Object = MibTableRow
apReliableMulticastEntry = _ApReliableMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 6, 8, 1)
)
apReliableMulticastEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apReliableMulticastAddrIndex"),
)
if mibBuilder.loadTexts:
    apReliableMulticastEntry.setStatus("current")


class _ApReliableMulticastAddrIndex_Type(Integer32):
    """Custom type apReliableMulticastAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ApReliableMulticastAddrIndex_Type.__name__ = "Integer32"
_ApReliableMulticastAddrIndex_Object = MibTableColumn
apReliableMulticastAddrIndex = _ApReliableMulticastAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 6, 8, 1, 1),
    _ApReliableMulticastAddrIndex_Type()
)
apReliableMulticastAddrIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apReliableMulticastAddrIndex.setStatus("current")
_ApReliableMulticastAddress_Type = IpAddress
_ApReliableMulticastAddress_Object = MibTableColumn
apReliableMulticastAddress = _ApReliableMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 6, 8, 1, 2),
    _ApReliableMulticastAddress_Type()
)
apReliableMulticastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apReliableMulticastAddress.setStatus("current")
_ApReliableMulticastTableRowEnable_Type = TruthValue
_ApReliableMulticastTableRowEnable_Object = MibTableColumn
apReliableMulticastTableRowEnable = _ApReliableMulticastTableRowEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 6, 8, 1, 3),
    _ApReliableMulticastTableRowEnable_Type()
)
apReliableMulticastTableRowEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apReliableMulticastTableRowEnable.setStatus("current")
_ApReliableMulticastMUTable_Object = MibTable
apReliableMulticastMUTable = _ApReliableMulticastMUTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 6, 9)
)
if mibBuilder.loadTexts:
    apReliableMulticastMUTable.setStatus("current")
_ApReliableMulticastMUEntry_Object = MibTableRow
apReliableMulticastMUEntry = _ApReliableMulticastMUEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 6, 9, 1)
)
apReliableMulticastMUEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apReliableMulticastMUStatsIndex"),
)
if mibBuilder.loadTexts:
    apReliableMulticastMUEntry.setStatus("current")


class _ApReliableMulticastMUStatsIndex_Type(Integer32):
    """Custom type apReliableMulticastMUStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ApReliableMulticastMUStatsIndex_Type.__name__ = "Integer32"
_ApReliableMulticastMUStatsIndex_Object = MibTableColumn
apReliableMulticastMUStatsIndex = _ApReliableMulticastMUStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 6, 9, 1, 1),
    _ApReliableMulticastMUStatsIndex_Type()
)
apReliableMulticastMUStatsIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apReliableMulticastMUStatsIndex.setStatus("current")
_ApReliableMulticastMUStatsIPAddr_Type = IpAddress
_ApReliableMulticastMUStatsIPAddr_Object = MibTableColumn
apReliableMulticastMUStatsIPAddr = _ApReliableMulticastMUStatsIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 6, 9, 1, 2),
    _ApReliableMulticastMUStatsIPAddr_Type()
)
apReliableMulticastMUStatsIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apReliableMulticastMUStatsIPAddr.setStatus("current")
_ApReliableMulticastMUMacAddr_Type = PhysAddress
_ApReliableMulticastMUMacAddr_Object = MibTableColumn
apReliableMulticastMUMacAddr = _ApReliableMulticastMUMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 4, 6, 9, 1, 3),
    _ApReliableMulticastMUMacAddr_Type()
)
apReliableMulticastMUMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apReliableMulticastMUMacAddr.setStatus("current")
_ApSwitch_ObjectIdentity = ObjectIdentity
apSwitch = _ApSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5)
)
_ApWan_ObjectIdentity = ObjectIdentity
apWan = _ApWan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1)
)
_ApWanVpn_ObjectIdentity = ObjectIdentity
apWanVpn = _ApWanVpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 1)
)
_ApWanVpnTunnelConfig_ObjectIdentity = ObjectIdentity
apWanVpnTunnelConfig = _ApWanVpnTunnelConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 1, 1)
)
_ApWanVpnKeyAutoTable_Object = MibTable
apWanVpnKeyAutoTable = _ApWanVpnKeyAutoTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    apWanVpnKeyAutoTable.setStatus("current")
_ApWanVpnKeyAutoEntry_Object = MibTableRow
apWanVpnKeyAutoEntry = _ApWanVpnKeyAutoEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    apWanVpnKeyAutoEntry.setStatus("current")


class _ApWanVpnKeyAutoSALifeTime_Type(Unsigned32):
    """Custom type apWanVpnKeyAutoSALifeTime based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 4294967295),
    )


_ApWanVpnKeyAutoSALifeTime_Type.__name__ = "Unsigned32"
_ApWanVpnKeyAutoSALifeTime_Object = MibTableColumn
apWanVpnKeyAutoSALifeTime = _ApWanVpnKeyAutoSALifeTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 1, 1, 1, 1, 1),
    _ApWanVpnKeyAutoSALifeTime_Type()
)
apWanVpnKeyAutoSALifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWanVpnKeyAutoSALifeTime.setStatus("current")
if mibBuilder.loadTexts:
    apWanVpnKeyAutoSALifeTime.setUnits("seconds")
_ApWanPppoe_ObjectIdentity = ObjectIdentity
apWanPppoe = _ApWanPppoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 2)
)
_ApWanPppoeClientTable_Object = MibTable
apWanPppoeClientTable = _ApWanPppoeClientTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    apWanPppoeClientTable.setStatus("current")
_ApWanPppoeClientEntry_Object = MibTableRow
apWanPppoeClientEntry = _ApWanPppoeClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 2, 1, 1)
)
apWanPppoeClientEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apWanPppoeClientIndex"),
)
if mibBuilder.loadTexts:
    apWanPppoeClientEntry.setStatus("current")


class _ApWanPppoeClientIndex_Type(Integer32):
    """Custom type apWanPppoeClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ApWanPppoeClientIndex_Type.__name__ = "Integer32"
_ApWanPppoeClientIndex_Object = MibTableColumn
apWanPppoeClientIndex = _ApWanPppoeClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 2, 1, 1, 1),
    _ApWanPppoeClientIndex_Type()
)
apWanPppoeClientIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apWanPppoeClientIndex.setStatus("current")
_ApWanPppoeClientIp_Type = IpAddress
_ApWanPppoeClientIp_Object = MibTableColumn
apWanPppoeClientIp = _ApWanPppoeClientIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 2, 1, 1, 2),
    _ApWanPppoeClientIp_Type()
)
apWanPppoeClientIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWanPppoeClientIp.setStatus("current")
_ApWanPppoeClientGateway_Type = IpAddress
_ApWanPppoeClientGateway_Object = MibTableColumn
apWanPppoeClientGateway = _ApWanPppoeClientGateway_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 2, 1, 1, 3),
    _ApWanPppoeClientGateway_Type()
)
apWanPppoeClientGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWanPppoeClientGateway.setStatus("current")
_ApWanPppoeClientPrimaryDNSServer_Type = IpAddress
_ApWanPppoeClientPrimaryDNSServer_Object = MibTableColumn
apWanPppoeClientPrimaryDNSServer = _ApWanPppoeClientPrimaryDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 2, 1, 1, 4),
    _ApWanPppoeClientPrimaryDNSServer_Type()
)
apWanPppoeClientPrimaryDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWanPppoeClientPrimaryDNSServer.setStatus("current")
_ApWanPppoeClientSecondaryDNSServer_Type = IpAddress
_ApWanPppoeClientSecondaryDNSServer_Object = MibTableColumn
apWanPppoeClientSecondaryDNSServer = _ApWanPppoeClientSecondaryDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 2, 1, 1, 5),
    _ApWanPppoeClientSecondaryDNSServer_Type()
)
apWanPppoeClientSecondaryDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWanPppoeClientSecondaryDNSServer.setStatus("current")
_ApWanPort_ObjectIdentity = ObjectIdentity
apWanPort = _ApWanPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 3)
)


class _ApWanPortAutoNegotiation_Type(Integer32):
    """Custom type apWanPortAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ApWanPortAutoNegotiation_Type.__name__ = "Integer32"
_ApWanPortAutoNegotiation_Object = MibScalar
apWanPortAutoNegotiation = _ApWanPortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 3, 1),
    _ApWanPortAutoNegotiation_Type()
)
apWanPortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWanPortAutoNegotiation.setStatus("current")


class _ApWanPortSpeed_Type(Integer32):
    """Custom type apWanPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hundredMbps", 1),
          ("oneGbps", 2),
          ("tenMbps", 0))
    )


_ApWanPortSpeed_Type.__name__ = "Integer32"
_ApWanPortSpeed_Object = MibScalar
apWanPortSpeed = _ApWanPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 3, 2),
    _ApWanPortSpeed_Type()
)
apWanPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWanPortSpeed.setStatus("current")


class _ApWanPortDuplex_Type(Integer32):
    """Custom type apWanPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 0))
    )


_ApWanPortDuplex_Type.__name__ = "Integer32"
_ApWanPortDuplex_Object = MibScalar
apWanPortDuplex = _ApWanPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 3, 3),
    _ApWanPortDuplex_Type()
)
apWanPortDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWanPortDuplex.setStatus("current")
_ApWanDynDNS_ObjectIdentity = ObjectIdentity
apWanDynDNS = _ApWanDynDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 4)
)
_ApWanDynDNSMode_Type = TruthValue
_ApWanDynDNSMode_Object = MibScalar
apWanDynDNSMode = _ApWanDynDNSMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 4, 1),
    _ApWanDynDNSMode_Type()
)
apWanDynDNSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWanDynDNSMode.setStatus("current")
_ApWanDynDNSTable_Object = MibTable
apWanDynDNSTable = _ApWanDynDNSTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 4, 2)
)
if mibBuilder.loadTexts:
    apWanDynDNSTable.setStatus("current")
_ApWanDynDNSEntry_Object = MibTableRow
apWanDynDNSEntry = _ApWanDynDNSEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 4, 2, 1)
)
apWanDynDNSEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apWanDynDNSIndex"),
)
if mibBuilder.loadTexts:
    apWanDynDNSEntry.setStatus("current")
_ApWanDynDNSUsername_Type = DisplayString
_ApWanDynDNSUsername_Object = MibTableColumn
apWanDynDNSUsername = _ApWanDynDNSUsername_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 4, 2, 1, 1),
    _ApWanDynDNSUsername_Type()
)
apWanDynDNSUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWanDynDNSUsername.setStatus("current")
_ApWanDynDNSPassword_Type = DisplayString
_ApWanDynDNSPassword_Object = MibTableColumn
apWanDynDNSPassword = _ApWanDynDNSPassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 4, 2, 1, 2),
    _ApWanDynDNSPassword_Type()
)
apWanDynDNSPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWanDynDNSPassword.setStatus("current")
_ApWanDynDNSHostname_Type = DisplayString
_ApWanDynDNSHostname_Object = MibTableColumn
apWanDynDNSHostname = _ApWanDynDNSHostname_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 4, 2, 1, 3),
    _ApWanDynDNSHostname_Type()
)
apWanDynDNSHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWanDynDNSHostname.setStatus("current")


class _ApWanDynDNSIndex_Type(Integer32):
    """Custom type apWanDynDNSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ApWanDynDNSIndex_Type.__name__ = "Integer32"
_ApWanDynDNSIndex_Object = MibTableColumn
apWanDynDNSIndex = _ApWanDynDNSIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 4, 2, 1, 4),
    _ApWanDynDNSIndex_Type()
)
apWanDynDNSIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apWanDynDNSIndex.setStatus("current")
_ApWanDynDNSUpdateResponseTable_Object = MibTable
apWanDynDNSUpdateResponseTable = _ApWanDynDNSUpdateResponseTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 4, 3)
)
if mibBuilder.loadTexts:
    apWanDynDNSUpdateResponseTable.setStatus("current")
_ApWanDynDNSUpdateResponseEntry_Object = MibTableRow
apWanDynDNSUpdateResponseEntry = _ApWanDynDNSUpdateResponseEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 4, 3, 1)
)
apWanDynDNSUpdateResponseEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apWanDynDNSUpdateResponseIndex"),
)
if mibBuilder.loadTexts:
    apWanDynDNSUpdateResponseEntry.setStatus("current")
_ApWanDynDNSUpdateHostname_Type = DisplayString
_ApWanDynDNSUpdateHostname_Object = MibTableColumn
apWanDynDNSUpdateHostname = _ApWanDynDNSUpdateHostname_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 4, 3, 1, 1),
    _ApWanDynDNSUpdateHostname_Type()
)
apWanDynDNSUpdateHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWanDynDNSUpdateHostname.setStatus("current")
_ApWanDynDNSUpdateIp_Type = Integer32
_ApWanDynDNSUpdateIp_Object = MibTableColumn
apWanDynDNSUpdateIp = _ApWanDynDNSUpdateIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 4, 3, 1, 2),
    _ApWanDynDNSUpdateIp_Type()
)
apWanDynDNSUpdateIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWanDynDNSUpdateIp.setStatus("current")
_ApWanDynDNSUpdateStatus_Type = Integer32
_ApWanDynDNSUpdateStatus_Object = MibTableColumn
apWanDynDNSUpdateStatus = _ApWanDynDNSUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 4, 3, 1, 3),
    _ApWanDynDNSUpdateStatus_Type()
)
apWanDynDNSUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWanDynDNSUpdateStatus.setStatus("current")


class _ApWanDynDNSUpdateResponseIndex_Type(Integer32):
    """Custom type apWanDynDNSUpdateResponseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ApWanDynDNSUpdateResponseIndex_Type.__name__ = "Integer32"
_ApWanDynDNSUpdateResponseIndex_Object = MibTableColumn
apWanDynDNSUpdateResponseIndex = _ApWanDynDNSUpdateResponseIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 4, 3, 1, 4),
    _ApWanDynDNSUpdateResponseIndex_Type()
)
apWanDynDNSUpdateResponseIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apWanDynDNSUpdateResponseIndex.setStatus("current")
_ApWanDynDNSPerformUpdate_Type = DoActionNow
_ApWanDynDNSPerformUpdate_Object = MibScalar
apWanDynDNSPerformUpdate = _ApWanDynDNSPerformUpdate_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 1, 4, 4),
    _ApWanDynDNSPerformUpdate_Type()
)
apWanDynDNSPerformUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWanDynDNSPerformUpdate.setStatus("current")
_ApLan_ObjectIdentity = ObjectIdentity
apLan = _ApLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2)
)
_ApLanEnable_Type = TruthValue
_ApLanEnable_Object = MibScalar
apLanEnable = _ApLanEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 1),
    _ApLanEnable_Type()
)
apLanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanEnable.setStatus("deprecated")


class _ApLanTimeOut_Type(Integer32):
    """Custom type apLanTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 3),
          ("hardwareDefect", 2))
    )


_ApLanTimeOut_Type.__name__ = "Integer32"
_ApLanTimeOut_Object = MibScalar
apLanTimeOut = _ApLanTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 2),
    _ApLanTimeOut_Type()
)
apLanTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanTimeOut.setStatus("current")
_ApLanTimeOutValue_Type = Integer32
_ApLanTimeOutValue_Object = MibScalar
apLanTimeOutValue = _ApLanTimeOutValue_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 3),
    _ApLanTimeOutValue_Type()
)
apLanTimeOutValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanTimeOutValue.setStatus("current")
_ApLanVlanEnable_Type = TruthValue
_ApLanVlanEnable_Object = MibScalar
apLanVlanEnable = _ApLanVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 4),
    _ApLanVlanEnable_Type()
)
apLanVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanVlanEnable.setStatus("obsolete")
_ApLanAdminVlanTag_Type = Integer32
_ApLanAdminVlanTag_Object = MibScalar
apLanAdminVlanTag = _ApLanAdminVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 5),
    _ApLanAdminVlanTag_Type()
)
apLanAdminVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanAdminVlanTag.setStatus("obsolete")
_ApLanNativeVlanTag_Type = Integer32
_ApLanNativeVlanTag_Object = MibScalar
apLanNativeVlanTag = _ApLanNativeVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 6),
    _ApLanNativeVlanTag_Type()
)
apLanNativeVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanNativeVlanTag.setStatus("obsolete")
_ApLan802dt1xAuth_ObjectIdentity = ObjectIdentity
apLan802dt1xAuth = _ApLan802dt1xAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 17)
)


class _ApLan802dt1xAuthLogin_Type(DisplayString):
    """Custom type apLan802dt1xAuthLogin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApLan802dt1xAuthLogin_Type.__name__ = "DisplayString"
_ApLan802dt1xAuthLogin_Object = MibScalar
apLan802dt1xAuthLogin = _ApLan802dt1xAuthLogin_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 17, 2),
    _ApLan802dt1xAuthLogin_Type()
)
apLan802dt1xAuthLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLan802dt1xAuthLogin.setStatus("current")
_ApLan802dt1xAuthPass_Type = Password
_ApLan802dt1xAuthPass_Object = MibScalar
apLan802dt1xAuthPass = _ApLan802dt1xAuthPass_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 17, 3),
    _ApLan802dt1xAuthPass_Type()
)
apLan802dt1xAuthPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLan802dt1xAuthPass.setStatus("current")
_ApLanVlan_ObjectIdentity = ObjectIdentity
apLanVlan = _ApLanVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 18)
)
_ApVlanTable_Object = MibTable
apVlanTable = _ApVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 18, 1)
)
if mibBuilder.loadTexts:
    apVlanTable.setStatus("current")
_ApVlanEntry_Object = MibTableRow
apVlanEntry = _ApVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 18, 1, 1)
)
apVlanEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apVlanIndex"),
)
if mibBuilder.loadTexts:
    apVlanEntry.setStatus("current")


class _ApVlanIndex_Type(Integer32):
    """Custom type apVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ApVlanIndex_Type.__name__ = "Integer32"
_ApVlanIndex_Object = MibTableColumn
apVlanIndex = _ApVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 18, 1, 1, 1),
    _ApVlanIndex_Type()
)
apVlanIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apVlanIndex.setStatus("current")


class _ApVlanId_Type(Integer32):
    """Custom type apVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_ApVlanId_Type.__name__ = "Integer32"
_ApVlanId_Object = MibTableColumn
apVlanId = _ApVlanId_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 18, 1, 1, 2),
    _ApVlanId_Type()
)
apVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVlanId.setStatus("current")
_ApVlanName_Type = DisplayString
_ApVlanName_Object = MibTableColumn
apVlanName = _ApVlanName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 18, 1, 1, 3),
    _ApVlanName_Type()
)
apVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVlanName.setStatus("current")
_ApVlanPointerToWlan_Type = MultiPointer63
_ApVlanPointerToWlan_Object = MibTableColumn
apVlanPointerToWlan = _ApVlanPointerToWlan_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 18, 1, 1, 4),
    _ApVlanPointerToWlan_Type()
)
apVlanPointerToWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVlanPointerToWlan.setStatus("current")
_ApVlanRowStatus_Type = AbbrevRowStatus
_ApVlanRowStatus_Object = MibTableColumn
apVlanRowStatus = _ApVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 18, 1, 1, 5),
    _ApVlanRowStatus_Type()
)
apVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVlanRowStatus.setStatus("current")
_ApSubnet_ObjectIdentity = ObjectIdentity
apSubnet = _ApSubnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 19)
)
_ApSubnetTable_Object = MibTable
apSubnetTable = _ApSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 19, 1)
)
if mibBuilder.loadTexts:
    apSubnetTable.setStatus("current")
_ApSubnetEntry_Object = MibTableRow
apSubnetEntry = _ApSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 19, 1, 1)
)
if mibBuilder.loadTexts:
    apSubnetEntry.setStatus("current")


class _ApSubnetDhcpState_Type(Integer32):
    """Custom type apSubnetDhcpState based on Integer32"""
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
        *(("dhcpBootp", 4),
          ("dhcpClient", 1),
          ("dhcpNone", 3),
          ("dhcpServer", 2))
    )


_ApSubnetDhcpState_Type.__name__ = "Integer32"
_ApSubnetDhcpState_Object = MibTableColumn
apSubnetDhcpState = _ApSubnetDhcpState_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 19, 1, 1, 1),
    _ApSubnetDhcpState_Type()
)
apSubnetDhcpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSubnetDhcpState.setStatus("current")
_ApSubnetVlanEnable_Type = TruthValue
_ApSubnetVlanEnable_Object = MibTableColumn
apSubnetVlanEnable = _ApSubnetVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 19, 1, 1, 2),
    _ApSubnetVlanEnable_Type()
)
apSubnetVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSubnetVlanEnable.setStatus("current")


class _ApSubnetTypeFilterAccessMode_Type(Integer32):
    """Custom type apSubnetTypeFilterAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_ApSubnetTypeFilterAccessMode_Type.__name__ = "Integer32"
_ApSubnetTypeFilterAccessMode_Object = MibTableColumn
apSubnetTypeFilterAccessMode = _ApSubnetTypeFilterAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 19, 1, 1, 3),
    _ApSubnetTypeFilterAccessMode_Type()
)
apSubnetTypeFilterAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSubnetTypeFilterAccessMode.setStatus("current")
_ApSubnetAdminVlanTag_Type = Integer32
_ApSubnetAdminVlanTag_Object = MibTableColumn
apSubnetAdminVlanTag = _ApSubnetAdminVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 19, 1, 1, 4),
    _ApSubnetAdminVlanTag_Type()
)
apSubnetAdminVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSubnetAdminVlanTag.setStatus("current")
_ApSubnetNativeVlanTag_Type = Integer32
_ApSubnetNativeVlanTag_Object = MibTableColumn
apSubnetNativeVlanTag = _ApSubnetNativeVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 19, 1, 1, 5),
    _ApSubnetNativeVlanTag_Type()
)
apSubnetNativeVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSubnetNativeVlanTag.setStatus("current")


class _ApLanTypeFilterAccessMode_Type(Integer32):
    """Custom type apLanTypeFilterAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_ApLanTypeFilterAccessMode_Type.__name__ = "Integer32"
_ApLanTypeFilterAccessMode_Object = MibScalar
apLanTypeFilterAccessMode = _ApLanTypeFilterAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 20),
    _ApLanTypeFilterAccessMode_Type()
)
apLanTypeFilterAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanTypeFilterAccessMode.setStatus("obsolete")
_ApLanTypeFilterTable_Object = MibTable
apLanTypeFilterTable = _ApLanTypeFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 21)
)
if mibBuilder.loadTexts:
    apLanTypeFilterTable.setStatus("current")
_ApLanTypeFilterEntry_Object = MibTableRow
apLanTypeFilterEntry = _ApLanTypeFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 21, 1)
)
apLanTypeFilterEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apLanTypeFilterSubnetIndex"),
    (0, "SYMBOL-AP-MIB", "apLanTypeFilterIndex"),
)
if mibBuilder.loadTexts:
    apLanTypeFilterEntry.setStatus("current")


class _ApLanTypeFilterSubnetIndex_Type(Integer32):
    """Custom type apLanTypeFilterSubnetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ApLanTypeFilterSubnetIndex_Type.__name__ = "Integer32"
_ApLanTypeFilterSubnetIndex_Object = MibTableColumn
apLanTypeFilterSubnetIndex = _ApLanTypeFilterSubnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 21, 1, 1),
    _ApLanTypeFilterSubnetIndex_Type()
)
apLanTypeFilterSubnetIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apLanTypeFilterSubnetIndex.setStatus("current")


class _ApLanTypeFilterIndex_Type(Integer32):
    """Custom type apLanTypeFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ApLanTypeFilterIndex_Type.__name__ = "Integer32"
_ApLanTypeFilterIndex_Object = MibTableColumn
apLanTypeFilterIndex = _ApLanTypeFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 21, 1, 2),
    _ApLanTypeFilterIndex_Type()
)
apLanTypeFilterIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apLanTypeFilterIndex.setStatus("current")
_ApLanTypeFilter_Type = EthernetType
_ApLanTypeFilter_Object = MibTableColumn
apLanTypeFilter = _ApLanTypeFilter_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 21, 1, 3),
    _ApLanTypeFilter_Type()
)
apLanTypeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanTypeFilter.setStatus("current")
_ApLanTypeFilterRowStatus_Type = AbbrevRowStatus
_ApLanTypeFilterRowStatus_Object = MibTableColumn
apLanTypeFilterRowStatus = _ApLanTypeFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 21, 1, 4),
    _ApLanTypeFilterRowStatus_Type()
)
apLanTypeFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanTypeFilterRowStatus.setStatus("current")


class _ApLanEthernetPort_Type(Integer32):
    """Custom type apLanEthernetPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lan1", 1),
          ("lan2", 2))
    )


_ApLanEthernetPort_Type.__name__ = "Integer32"
_ApLanEthernetPort_Object = MibScalar
apLanEthernetPort = _ApLanEthernetPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 22),
    _ApLanEthernetPort_Type()
)
apLanEthernetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanEthernetPort.setStatus("current")
_ApLanBridgeTable_Object = MibTable
apLanBridgeTable = _ApLanBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 23)
)
if mibBuilder.loadTexts:
    apLanBridgeTable.setStatus("current")
_ApLanBridgeEntry_Object = MibTableRow
apLanBridgeEntry = _ApLanBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 23, 1)
)
if mibBuilder.loadTexts:
    apLanBridgeEntry.setStatus("current")


class _ApLanBridgePriority_Type(Integer32):
    """Custom type apLanBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApLanBridgePriority_Type.__name__ = "Integer32"
_ApLanBridgePriority_Object = MibTableColumn
apLanBridgePriority = _ApLanBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 23, 1, 1),
    _ApLanBridgePriority_Type()
)
apLanBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanBridgePriority.setStatus("current")


class _ApLanBridgeMaxMsgAge_Type(Integer32):
    """Custom type apLanBridgeMaxMsgAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_ApLanBridgeMaxMsgAge_Type.__name__ = "Integer32"
_ApLanBridgeMaxMsgAge_Object = MibTableColumn
apLanBridgeMaxMsgAge = _ApLanBridgeMaxMsgAge_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 23, 1, 2),
    _ApLanBridgeMaxMsgAge_Type()
)
apLanBridgeMaxMsgAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanBridgeMaxMsgAge.setStatus("current")
if mibBuilder.loadTexts:
    apLanBridgeMaxMsgAge.setUnits("seconds")


class _ApLanBridgeHelloTime_Type(Integer32):
    """Custom type apLanBridgeHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ApLanBridgeHelloTime_Type.__name__ = "Integer32"
_ApLanBridgeHelloTime_Object = MibTableColumn
apLanBridgeHelloTime = _ApLanBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 23, 1, 3),
    _ApLanBridgeHelloTime_Type()
)
apLanBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanBridgeHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    apLanBridgeHelloTime.setUnits("seconds")


class _ApLanBridgeFwdDelay_Type(Integer32):
    """Custom type apLanBridgeFwdDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_ApLanBridgeFwdDelay_Type.__name__ = "Integer32"
_ApLanBridgeFwdDelay_Object = MibTableColumn
apLanBridgeFwdDelay = _ApLanBridgeFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 23, 1, 4),
    _ApLanBridgeFwdDelay_Type()
)
apLanBridgeFwdDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanBridgeFwdDelay.setStatus("current")
if mibBuilder.loadTexts:
    apLanBridgeFwdDelay.setUnits("seconds")


class _ApLanBridgeEntryAgeout_Type(Integer32):
    """Custom type apLanBridgeEntryAgeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 3600),
    )


_ApLanBridgeEntryAgeout_Type.__name__ = "Integer32"
_ApLanBridgeEntryAgeout_Object = MibTableColumn
apLanBridgeEntryAgeout = _ApLanBridgeEntryAgeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 23, 1, 5),
    _ApLanBridgeEntryAgeout_Type()
)
apLanBridgeEntryAgeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanBridgeEntryAgeout.setStatus("current")
if mibBuilder.loadTexts:
    apLanBridgeEntryAgeout.setUnits("seconds")
_ApLanPort_ObjectIdentity = ObjectIdentity
apLanPort = _ApLanPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 24)
)


class _ApLanPortAutoNegotiation_Type(Integer32):
    """Custom type apLanPortAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ApLanPortAutoNegotiation_Type.__name__ = "Integer32"
_ApLanPortAutoNegotiation_Object = MibScalar
apLanPortAutoNegotiation = _ApLanPortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 24, 1),
    _ApLanPortAutoNegotiation_Type()
)
apLanPortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanPortAutoNegotiation.setStatus("current")


class _ApLanPortSpeed_Type(Integer32):
    """Custom type apLanPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hundredMbps", 1),
          ("oneGbps", 2),
          ("tenMbps", 0))
    )


_ApLanPortSpeed_Type.__name__ = "Integer32"
_ApLanPortSpeed_Object = MibScalar
apLanPortSpeed = _ApLanPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 24, 2),
    _ApLanPortSpeed_Type()
)
apLanPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanPortSpeed.setStatus("current")


class _ApLanPortDuplex_Type(Integer32):
    """Custom type apLanPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 0))
    )


_ApLanPortDuplex_Type.__name__ = "Integer32"
_ApLanPortDuplex_Object = MibScalar
apLanPortDuplex = _ApLanPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 2, 24, 3),
    _ApLanPortDuplex_Type()
)
apLanPortDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanPortDuplex.setStatus("current")
_ApWnmpPing_ObjectIdentity = ObjectIdentity
apWnmpPing = _ApWnmpPing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 3)
)
_ApWnmpPingDestMu_Type = PhysAddress
_ApWnmpPingDestMu_Object = MibScalar
apWnmpPingDestMu = _ApWnmpPingDestMu_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 3, 1),
    _ApWnmpPingDestMu_Type()
)
apWnmpPingDestMu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWnmpPingDestMu.setStatus("current")
_ApWnmpPingDestAP_Type = PhysAddress
_ApWnmpPingDestAP_Object = MibScalar
apWnmpPingDestAP = _ApWnmpPingDestAP_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 3, 2),
    _ApWnmpPingDestAP_Type()
)
apWnmpPingDestAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWnmpPingDestAP.setStatus("current")


class _ApWnmpPingDest_Type(Integer32):
    """Custom type apWnmpPingDest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ap", 2),
          ("mu", 1))
    )


_ApWnmpPingDest_Type.__name__ = "Integer32"
_ApWnmpPingDest_Object = MibScalar
apWnmpPingDest = _ApWnmpPingDest_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 3, 3),
    _ApWnmpPingDest_Type()
)
apWnmpPingDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWnmpPingDest.setStatus("current")


class _ApWnmpPingNum_Type(Integer32):
    """Custom type apWnmpPingNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 539),
    )


_ApWnmpPingNum_Type.__name__ = "Integer32"
_ApWnmpPingNum_Object = MibScalar
apWnmpPingNum = _ApWnmpPingNum_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 3, 4),
    _ApWnmpPingNum_Type()
)
apWnmpPingNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWnmpPingNum.setStatus("current")


class _ApWnmpPingPacketLength_Type(Integer32):
    """Custom type apWnmpPingPacketLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 539),
    )


_ApWnmpPingPacketLength_Type.__name__ = "Integer32"
_ApWnmpPingPacketLength_Object = MibScalar
apWnmpPingPacketLength = _ApWnmpPingPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 3, 5),
    _ApWnmpPingPacketLength_Type()
)
apWnmpPingPacketLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWnmpPingPacketLength.setStatus("current")
if mibBuilder.loadTexts:
    apWnmpPingPacketLength.setUnits("byte")


class _ApWnmpPingPacketData_Type(OctetString):
    """Custom type apWnmpPingPacketData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ApWnmpPingPacketData_Type.__name__ = "OctetString"
_ApWnmpPingPacketData_Object = MibScalar
apWnmpPingPacketData = _ApWnmpPingPacketData_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 3, 6),
    _ApWnmpPingPacketData_Type()
)
apWnmpPingPacketData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWnmpPingPacketData.setStatus("current")
_ApWnmpPingAction_Type = TruthValue
_ApWnmpPingAction_Object = MibScalar
apWnmpPingAction = _ApWnmpPingAction_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 3, 7),
    _ApWnmpPingAction_Type()
)
apWnmpPingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWnmpPingAction.setStatus("current")
_ApWnmpPingNumResponses_Type = Integer32
_ApWnmpPingNumResponses_Object = MibScalar
apWnmpPingNumResponses = _ApWnmpPingNumResponses_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 3, 8),
    _ApWnmpPingNumResponses_Type()
)
apWnmpPingNumResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWnmpPingNumResponses.setStatus("current")
_ApFlashLed_ObjectIdentity = ObjectIdentity
apFlashLed = _ApFlashLed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 4)
)
_ApFlashLedDestAP_Type = PhysAddress
_ApFlashLedDestAP_Object = MibScalar
apFlashLedDestAP = _ApFlashLedDestAP_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 4, 1),
    _ApFlashLedDestAP_Type()
)
apFlashLedDestAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apFlashLedDestAP.setStatus("current")
_ApFlashLedAction_Type = TruthValue
_ApFlashLedAction_Object = MibScalar
apFlashLedAction = _ApFlashLedAction_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 4, 2),
    _ApFlashLedAction_Type()
)
apFlashLedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apFlashLedAction.setStatus("current")
_ApKnownAPList_ObjectIdentity = ObjectIdentity
apKnownAPList = _ApKnownAPList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5)
)
_ApKnownApTable_Object = MibTable
apKnownApTable = _ApKnownApTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5, 1)
)
if mibBuilder.loadTexts:
    apKnownApTable.setStatus("current")
_ApKnownApEntry_Object = MibTableRow
apKnownApEntry = _ApKnownApEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5, 1, 1)
)
apKnownApEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apKnownApIndex"),
)
if mibBuilder.loadTexts:
    apKnownApEntry.setStatus("current")


class _ApKnownApIndex_Type(Integer32):
    """Custom type apKnownApIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_ApKnownApIndex_Type.__name__ = "Integer32"
_ApKnownApIndex_Object = MibTableColumn
apKnownApIndex = _ApKnownApIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5, 1, 1, 1),
    _ApKnownApIndex_Type()
)
apKnownApIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apKnownApIndex.setStatus("current")
_ApKnownApMac_Type = PhysAddress
_ApKnownApMac_Object = MibTableColumn
apKnownApMac = _ApKnownApMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5, 1, 1, 2),
    _ApKnownApMac_Type()
)
apKnownApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apKnownApMac.setStatus("current")
_ApKnownApIp_Type = IpAddress
_ApKnownApIp_Object = MibTableColumn
apKnownApIp = _ApKnownApIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5, 1, 1, 3),
    _ApKnownApIp_Type()
)
apKnownApIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apKnownApIp.setStatus("current")
_ApKnownApChannel1_Type = Integer32
_ApKnownApChannel1_Object = MibTableColumn
apKnownApChannel1 = _ApKnownApChannel1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5, 1, 1, 4),
    _ApKnownApChannel1_Type()
)
apKnownApChannel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apKnownApChannel1.setStatus("current")
_ApKnownApChannel2_Type = Integer32
_ApKnownApChannel2_Object = MibTableColumn
apKnownApChannel2 = _ApKnownApChannel2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5, 1, 1, 5),
    _ApKnownApChannel2_Type()
)
apKnownApChannel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apKnownApChannel2.setStatus("current")
_ApKnownApMu_Type = Integer32
_ApKnownApMu_Object = MibTableColumn
apKnownApMu = _ApKnownApMu_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5, 1, 1, 6),
    _ApKnownApMu_Type()
)
apKnownApMu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apKnownApMu.setStatus("current")
_ApKnownApKbPerSec_Type = Integer32
_ApKnownApKbPerSec_Object = MibTableColumn
apKnownApKbPerSec = _ApKnownApKbPerSec_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5, 1, 1, 7),
    _ApKnownApKbPerSec_Type()
)
apKnownApKbPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apKnownApKbPerSec.setStatus("current")
_ApKnownApPktsPerSec_Type = Integer32
_ApKnownApPktsPerSec_Object = MibTableColumn
apKnownApPktsPerSec = _ApKnownApPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5, 1, 1, 8),
    _ApKnownApPktsPerSec_Type()
)
apKnownApPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apKnownApPktsPerSec.setStatus("current")


class _ApKnownApRadioType1_Type(Integer32):
    """Custom type apKnownApRadioType1 based on Integer32"""
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
        *(("radioA", 1),
          ("radioB", 2),
          ("radioBG", 3),
          ("radioFH", 4),
          ("radioN", 5))
    )


_ApKnownApRadioType1_Type.__name__ = "Integer32"
_ApKnownApRadioType1_Object = MibTableColumn
apKnownApRadioType1 = _ApKnownApRadioType1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5, 1, 1, 9),
    _ApKnownApRadioType1_Type()
)
apKnownApRadioType1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apKnownApRadioType1.setStatus("current")


class _ApKnownApRadioType2_Type(Integer32):
    """Custom type apKnownApRadioType2 based on Integer32"""
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
        *(("radioA", 1),
          ("radioB", 2),
          ("radioBG", 3),
          ("radioFH", 4),
          ("radioN", 5))
    )


_ApKnownApRadioType2_Type.__name__ = "Integer32"
_ApKnownApRadioType2_Object = MibTableColumn
apKnownApRadioType2 = _ApKnownApRadioType2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5, 1, 1, 10),
    _ApKnownApRadioType2_Type()
)
apKnownApRadioType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apKnownApRadioType2.setStatus("current")


class _ApKnownApType_Type(Integer32):
    """Custom type apKnownApType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ap302x", 4),
          ("ap4131", 2),
          ("ap41x1", 3),
          ("ap5131", 1),
          ("ap71x1", 5),
          ("unknown", 0))
    )


_ApKnownApType_Type.__name__ = "Integer32"
_ApKnownApType_Object = MibTableColumn
apKnownApType = _ApKnownApType_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5, 1, 1, 11),
    _ApKnownApType_Type()
)
apKnownApType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apKnownApType.setStatus("current")
_ApKnownApFwVers_Type = DisplayString
_ApKnownApFwVers_Object = MibTableColumn
apKnownApFwVers = _ApKnownApFwVers_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5, 1, 1, 12),
    _ApKnownApFwVers_Type()
)
apKnownApFwVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apKnownApFwVers.setStatus("current")
_ApKnownApUnitName_Type = DisplayString
_ApKnownApUnitName_Object = MibTableColumn
apKnownApUnitName = _ApKnownApUnitName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5, 1, 1, 13),
    _ApKnownApUnitName_Type()
)
apKnownApUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apKnownApUnitName.setStatus("current")
_ApKnownApEssName_Type = DisplayString
_ApKnownApEssName_Object = MibTableColumn
apKnownApEssName = _ApKnownApEssName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5, 1, 1, 14),
    _ApKnownApEssName_Type()
)
apKnownApEssName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apKnownApEssName.setStatus("current")
_ApKnownApSendCfg_Type = DoActionNow
_ApKnownApSendCfg_Object = MibTableColumn
apKnownApSendCfg = _ApKnownApSendCfg_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5, 1, 1, 15),
    _ApKnownApSendCfg_Type()
)
apKnownApSendCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apKnownApSendCfg.setStatus("current")
_ApKnownApSendCfgStatus_Type = TruthValue
_ApKnownApSendCfgStatus_Object = MibTableColumn
apKnownApSendCfgStatus = _ApKnownApSendCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5, 1, 1, 16),
    _ApKnownApSendCfgStatus_Type()
)
apKnownApSendCfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apKnownApSendCfgStatus.setStatus("current")
_ApKnownApRadio1ClientBridgeMac1_Type = PhysAddress
_ApKnownApRadio1ClientBridgeMac1_Object = MibTableColumn
apKnownApRadio1ClientBridgeMac1 = _ApKnownApRadio1ClientBridgeMac1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5, 1, 1, 17),
    _ApKnownApRadio1ClientBridgeMac1_Type()
)
apKnownApRadio1ClientBridgeMac1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apKnownApRadio1ClientBridgeMac1.setStatus("current")
_ApKnownApRadio1ClientBridgeMac2_Type = PhysAddress
_ApKnownApRadio1ClientBridgeMac2_Object = MibTableColumn
apKnownApRadio1ClientBridgeMac2 = _ApKnownApRadio1ClientBridgeMac2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5, 1, 1, 18),
    _ApKnownApRadio1ClientBridgeMac2_Type()
)
apKnownApRadio1ClientBridgeMac2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apKnownApRadio1ClientBridgeMac2.setStatus("current")
_ApKnownApRadio1ClientBridgeMac3_Type = PhysAddress
_ApKnownApRadio1ClientBridgeMac3_Object = MibTableColumn
apKnownApRadio1ClientBridgeMac3 = _ApKnownApRadio1ClientBridgeMac3_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5, 1, 1, 19),
    _ApKnownApRadio1ClientBridgeMac3_Type()
)
apKnownApRadio1ClientBridgeMac3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apKnownApRadio1ClientBridgeMac3.setStatus("current")
_ApKnownApRadio2ClientBridgeMac1_Type = PhysAddress
_ApKnownApRadio2ClientBridgeMac1_Object = MibTableColumn
apKnownApRadio2ClientBridgeMac1 = _ApKnownApRadio2ClientBridgeMac1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5, 1, 1, 20),
    _ApKnownApRadio2ClientBridgeMac1_Type()
)
apKnownApRadio2ClientBridgeMac1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apKnownApRadio2ClientBridgeMac1.setStatus("current")
_ApKnownApRadio2ClientBridgeMac2_Type = PhysAddress
_ApKnownApRadio2ClientBridgeMac2_Object = MibTableColumn
apKnownApRadio2ClientBridgeMac2 = _ApKnownApRadio2ClientBridgeMac2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5, 1, 1, 21),
    _ApKnownApRadio2ClientBridgeMac2_Type()
)
apKnownApRadio2ClientBridgeMac2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apKnownApRadio2ClientBridgeMac2.setStatus("current")
_ApKnownApRadio2ClientBridgeMac3_Type = PhysAddress
_ApKnownApRadio2ClientBridgeMac3_Object = MibTableColumn
apKnownApRadio2ClientBridgeMac3 = _ApKnownApRadio2ClientBridgeMac3_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 5, 1, 1, 22),
    _ApKnownApRadio2ClientBridgeMac3_Type()
)
apKnownApRadio2ClientBridgeMac3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apKnownApRadio2ClientBridgeMac3.setStatus("current")
_ApAap_ObjectIdentity = ObjectIdentity
apAap = _ApAap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 6)
)
_ApAapSwitchAutoDiscoveryEnable_Type = TruthValue
_ApAapSwitchAutoDiscoveryEnable_Object = MibScalar
apAapSwitchAutoDiscoveryEnable = _ApAapSwitchAutoDiscoveryEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 6, 1),
    _ApAapSwitchAutoDiscoveryEnable_Type()
)
apAapSwitchAutoDiscoveryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAapSwitchAutoDiscoveryEnable.setStatus("current")


class _ApAapSwitchDiscoveryInterface_Type(Integer32):
    """Custom type apAapSwitchDiscoveryInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lan1", 2),
          ("lan2", 3),
          ("wan", 1))
    )


_ApAapSwitchDiscoveryInterface_Type.__name__ = "Integer32"
_ApAapSwitchDiscoveryInterface_Object = MibScalar
apAapSwitchDiscoveryInterface = _ApAapSwitchDiscoveryInterface_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 6, 2),
    _ApAapSwitchDiscoveryInterface_Type()
)
apAapSwitchDiscoveryInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAapSwitchDiscoveryInterface.setStatus("current")
_ApAapSwitchDiscoveryIPAddressTable_Object = MibTable
apAapSwitchDiscoveryIPAddressTable = _ApAapSwitchDiscoveryIPAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 6, 3)
)
if mibBuilder.loadTexts:
    apAapSwitchDiscoveryIPAddressTable.setStatus("current")
_ApAapSwitchDiscoveryIPAddressEntry_Object = MibTableRow
apAapSwitchDiscoveryIPAddressEntry = _ApAapSwitchDiscoveryIPAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 6, 3, 1)
)
apAapSwitchDiscoveryIPAddressEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apAapSwitchDiscoveryIPAddressIndex"),
)
if mibBuilder.loadTexts:
    apAapSwitchDiscoveryIPAddressEntry.setStatus("current")


class _ApAapSwitchDiscoveryIPAddressIndex_Type(Integer32):
    """Custom type apAapSwitchDiscoveryIPAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_ApAapSwitchDiscoveryIPAddressIndex_Type.__name__ = "Integer32"
_ApAapSwitchDiscoveryIPAddressIndex_Object = MibTableColumn
apAapSwitchDiscoveryIPAddressIndex = _ApAapSwitchDiscoveryIPAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 6, 3, 1, 1),
    _ApAapSwitchDiscoveryIPAddressIndex_Type()
)
apAapSwitchDiscoveryIPAddressIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apAapSwitchDiscoveryIPAddressIndex.setStatus("current")
_ApAapSwitchDiscoveryIPAddress_Type = IpAddress
_ApAapSwitchDiscoveryIPAddress_Object = MibTableColumn
apAapSwitchDiscoveryIPAddress = _ApAapSwitchDiscoveryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 6, 3, 1, 2),
    _ApAapSwitchDiscoveryIPAddress_Type()
)
apAapSwitchDiscoveryIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAapSwitchDiscoveryIPAddress.setStatus("current")


class _ApAapSwitchDiscoveryIPAddressRowStatus_Type(Integer32):
    """Custom type apAapSwitchDiscoveryIPAddressRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("destroy", 1)
    )


_ApAapSwitchDiscoveryIPAddressRowStatus_Type.__name__ = "Integer32"
_ApAapSwitchDiscoveryIPAddressRowStatus_Object = MibTableColumn
apAapSwitchDiscoveryIPAddressRowStatus = _ApAapSwitchDiscoveryIPAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 6, 3, 1, 3),
    _ApAapSwitchDiscoveryIPAddressRowStatus_Type()
)
apAapSwitchDiscoveryIPAddressRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAapSwitchDiscoveryIPAddressRowStatus.setStatus("current")


class _ApAapSwitchDiscoveryDomainName_Type(DisplayString):
    """Custom type apAapSwitchDiscoveryDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ApAapSwitchDiscoveryDomainName_Type.__name__ = "DisplayString"
_ApAapSwitchDiscoveryDomainName_Object = MibScalar
apAapSwitchDiscoveryDomainName = _ApAapSwitchDiscoveryDomainName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 6, 4),
    _ApAapSwitchDiscoveryDomainName_Type()
)
apAapSwitchDiscoveryDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAapSwitchDiscoveryDomainName.setStatus("current")


class _ApAapSwitchDiscoveryPort_Type(Integer32):
    """Custom type apAapSwitchDiscoveryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApAapSwitchDiscoveryPort_Type.__name__ = "Integer32"
_ApAapSwitchDiscoveryPort_Object = MibScalar
apAapSwitchDiscoveryPort = _ApAapSwitchDiscoveryPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 6, 5),
    _ApAapSwitchDiscoveryPort_Type()
)
apAapSwitchDiscoveryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAapSwitchDiscoveryPort.setStatus("current")


class _ApAapPassphrase_Type(Password):
    """Custom type apAapPassphrase based on Password"""
    subtypeSpec = Password.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ApAapPassphrase_Type.__name__ = "Password"
_ApAapPassphrase_Object = MibScalar
apAapPassphrase = _ApAapPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 6, 6),
    _ApAapPassphrase_Type()
)
apAapPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAapPassphrase.setStatus("current")
_ApAapTunnelToSwitchEnable_Type = TruthValue
_ApAapTunnelToSwitchEnable_Object = MibScalar
apAapTunnelToSwitchEnable = _ApAapTunnelToSwitchEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 6, 7),
    _ApAapTunnelToSwitchEnable_Type()
)
apAapTunnelToSwitchEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAapTunnelToSwitchEnable.setStatus("current")


class _ApAapAcKeepAlive_Type(Integer32):
    """Custom type apAapAcKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ApAapAcKeepAlive_Type.__name__ = "Integer32"
_ApAapAcKeepAlive_Object = MibScalar
apAapAcKeepAlive = _ApAapAcKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 6, 8),
    _ApAapAcKeepAlive_Type()
)
apAapAcKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAapAcKeepAlive.setStatus("current")


class _ApAapAdoptionState_Type(Integer32):
    """Custom type apAapAdoptionState based on Integer32"""
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
        *(("adopted", 4),
          ("adoptionFailed", 3),
          ("connectionLoss", 5),
          ("standAlone", 1),
          ("waiting", 2))
    )


_ApAapAdoptionState_Type.__name__ = "Integer32"
_ApAapAdoptionState_Object = MibScalar
apAapAdoptionState = _ApAapAdoptionState_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 6, 9),
    _ApAapAdoptionState_Type()
)
apAapAdoptionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAapAdoptionState.setStatus("current")
_ApAapAdoptingSwitchIP_Type = IpAddress
_ApAapAdoptingSwitchIP_Object = MibScalar
apAapAdoptingSwitchIP = _ApAapAdoptingSwitchIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 5, 6, 10),
    _ApAapAdoptingSwitchIP_Type()
)
apAapAdoptingSwitchIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAapAdoptingSwitchIP.setStatus("current")
_ApNotifications_ObjectIdentity = ObjectIdentity
apNotifications = _ApNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6)
)
_ApTrapCtrl_ObjectIdentity = ObjectIdentity
apTrapCtrl = _ApTrapCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000)
)
_ApTrapCtrlEnableTable_Object = MibTable
apTrapCtrlEnableTable = _ApTrapCtrlEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 1)
)
if mibBuilder.loadTexts:
    apTrapCtrlEnableTable.setStatus("current")
_ApTrapCtrlEnableEntry_Object = MibTableRow
apTrapCtrlEnableEntry = _ApTrapCtrlEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 1, 1)
)
apTrapCtrlEnableEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apTrapCtrlEnableIndex"),
)
if mibBuilder.loadTexts:
    apTrapCtrlEnableEntry.setStatus("current")


class _ApTrapCtrlEnableIndex_Type(Integer32):
    """Custom type apTrapCtrlEnableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17),
    )


_ApTrapCtrlEnableIndex_Type.__name__ = "Integer32"
_ApTrapCtrlEnableIndex_Object = MibTableColumn
apTrapCtrlEnableIndex = _ApTrapCtrlEnableIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 1, 1, 1),
    _ApTrapCtrlEnableIndex_Type()
)
apTrapCtrlEnableIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apTrapCtrlEnableIndex.setStatus("current")
_ApTrapCtrlEnableName_Type = DisplayString
_ApTrapCtrlEnableName_Object = MibTableColumn
apTrapCtrlEnableName = _ApTrapCtrlEnableName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 1, 1, 2),
    _ApTrapCtrlEnableName_Type()
)
apTrapCtrlEnableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapCtrlEnableName.setStatus("current")
_ApTrapCtrlEnable_Type = TruthValue
_ApTrapCtrlEnable_Object = MibTableColumn
apTrapCtrlEnable = _ApTrapCtrlEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 1, 1, 3),
    _ApTrapCtrlEnable_Type()
)
apTrapCtrlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTrapCtrlEnable.setStatus("current")


class _ApTrapCtrlRateLimit_Type(Unsigned32):
    """Custom type apTrapCtrlRateLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_ApTrapCtrlRateLimit_Type.__name__ = "Unsigned32"
_ApTrapCtrlRateLimit_Object = MibScalar
apTrapCtrlRateLimit = _ApTrapCtrlRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 2),
    _ApTrapCtrlRateLimit_Type()
)
apTrapCtrlRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTrapCtrlRateLimit.setStatus("current")
_ApTrapCtrlSumStats_ObjectIdentity = ObjectIdentity
apTrapCtrlSumStats = _ApTrapCtrlSumStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 3)
)
_ApTrapCtrlSumStatsTable_Object = MibTable
apTrapCtrlSumStatsTable = _ApTrapCtrlSumStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 3, 1)
)
if mibBuilder.loadTexts:
    apTrapCtrlSumStatsTable.setStatus("current")
_ApTrapCtrlSumStatsEntry_Object = MibTableRow
apTrapCtrlSumStatsEntry = _ApTrapCtrlSumStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 3, 1, 1)
)
apTrapCtrlSumStatsEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apTrapCtrlSumStatsIndex"),
)
if mibBuilder.loadTexts:
    apTrapCtrlSumStatsEntry.setStatus("current")


class _ApTrapCtrlSumStatsIndex_Type(Integer32):
    """Custom type apTrapCtrlSumStatsIndex based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("thresholdsAvgBitSpeed", 9),
          ("thresholdsAvgMuNoise", 11),
          ("thresholdsAvgMuSignal", 10),
          ("thresholdsAvgMuSnr", 12),
          ("thresholdsPctDropped", 20),
          ("thresholdsPctNUcastPkts", 13),
          ("thresholdsPctRfUtil", 19),
          ("thresholdsPktsPerSec", 3),
          ("thresholdsPpmRxUndecrypt", 17),
          ("thresholdsPpmTxDropped", 15),
          ("thresholdsPpmTxWithRetires", 14),
          ("thresholdsThroughput", 6),
          ("thresholdsTotalMus", 18),
          ("thresholdsTxAvgRetries", 16),
          ("unusedNumPkts", 2),
          ("unusedPktsPerSecRx", 5),
          ("unusedPktsPerSecTx", 4),
          ("unusedThroughputRx", 8),
          ("unusedThroughputTx", 7),
          ("unusedTimestamp", 1))
    )


_ApTrapCtrlSumStatsIndex_Type.__name__ = "Integer32"
_ApTrapCtrlSumStatsIndex_Object = MibTableColumn
apTrapCtrlSumStatsIndex = _ApTrapCtrlSumStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 3, 1, 1, 1),
    _ApTrapCtrlSumStatsIndex_Type()
)
apTrapCtrlSumStatsIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apTrapCtrlSumStatsIndex.setStatus("current")
_ApTrapCtrlSumStatsDescr_Type = DisplayString
_ApTrapCtrlSumStatsDescr_Object = MibTableColumn
apTrapCtrlSumStatsDescr = _ApTrapCtrlSumStatsDescr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 3, 1, 1, 2),
    _ApTrapCtrlSumStatsDescr_Type()
)
apTrapCtrlSumStatsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapCtrlSumStatsDescr.setStatus("current")
_ApTrapCtrlSumStatsUnits_Type = DisplayString
_ApTrapCtrlSumStatsUnits_Object = MibTableColumn
apTrapCtrlSumStatsUnits = _ApTrapCtrlSumStatsUnits_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 3, 1, 1, 3),
    _ApTrapCtrlSumStatsUnits_Type()
)
apTrapCtrlSumStatsUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapCtrlSumStatsUnits.setStatus("current")
_ApTrapCtrlSumStatsCanBeSetMu_Type = TruthValue
_ApTrapCtrlSumStatsCanBeSetMu_Object = MibTableColumn
apTrapCtrlSumStatsCanBeSetMu = _ApTrapCtrlSumStatsCanBeSetMu_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 3, 1, 1, 4),
    _ApTrapCtrlSumStatsCanBeSetMu_Type()
)
apTrapCtrlSumStatsCanBeSetMu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapCtrlSumStatsCanBeSetMu.setStatus("current")
_ApTrapCtrlSumStatsThresholdMu_Type = Unsigned32
_ApTrapCtrlSumStatsThresholdMu_Object = MibTableColumn
apTrapCtrlSumStatsThresholdMu = _ApTrapCtrlSumStatsThresholdMu_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 3, 1, 1, 5),
    _ApTrapCtrlSumStatsThresholdMu_Type()
)
apTrapCtrlSumStatsThresholdMu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTrapCtrlSumStatsThresholdMu.setStatus("current")
_ApTrapCtrlSumStatsCanBeSetRadioA_Type = TruthValue
_ApTrapCtrlSumStatsCanBeSetRadioA_Object = MibTableColumn
apTrapCtrlSumStatsCanBeSetRadioA = _ApTrapCtrlSumStatsCanBeSetRadioA_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 3, 1, 1, 6),
    _ApTrapCtrlSumStatsCanBeSetRadioA_Type()
)
apTrapCtrlSumStatsCanBeSetRadioA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapCtrlSumStatsCanBeSetRadioA.setStatus("current")
_ApTrapCtrlSumStatsThresholdRadioA_Type = Unsigned32
_ApTrapCtrlSumStatsThresholdRadioA_Object = MibTableColumn
apTrapCtrlSumStatsThresholdRadioA = _ApTrapCtrlSumStatsThresholdRadioA_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 3, 1, 1, 7),
    _ApTrapCtrlSumStatsThresholdRadioA_Type()
)
apTrapCtrlSumStatsThresholdRadioA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTrapCtrlSumStatsThresholdRadioA.setStatus("current")
_ApTrapCtrlSumStatsCanBeSetRadioBG_Type = TruthValue
_ApTrapCtrlSumStatsCanBeSetRadioBG_Object = MibTableColumn
apTrapCtrlSumStatsCanBeSetRadioBG = _ApTrapCtrlSumStatsCanBeSetRadioBG_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 3, 1, 1, 8),
    _ApTrapCtrlSumStatsCanBeSetRadioBG_Type()
)
apTrapCtrlSumStatsCanBeSetRadioBG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapCtrlSumStatsCanBeSetRadioBG.setStatus("current")
_ApTrapCtrlSumStatsThresholdRadioBG_Type = Unsigned32
_ApTrapCtrlSumStatsThresholdRadioBG_Object = MibTableColumn
apTrapCtrlSumStatsThresholdRadioBG = _ApTrapCtrlSumStatsThresholdRadioBG_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 3, 1, 1, 9),
    _ApTrapCtrlSumStatsThresholdRadioBG_Type()
)
apTrapCtrlSumStatsThresholdRadioBG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTrapCtrlSumStatsThresholdRadioBG.setStatus("current")
_ApTrapCtrlSumStatsCanBeSetWlan_Type = TruthValue
_ApTrapCtrlSumStatsCanBeSetWlan_Object = MibTableColumn
apTrapCtrlSumStatsCanBeSetWlan = _ApTrapCtrlSumStatsCanBeSetWlan_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 3, 1, 1, 10),
    _ApTrapCtrlSumStatsCanBeSetWlan_Type()
)
apTrapCtrlSumStatsCanBeSetWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapCtrlSumStatsCanBeSetWlan.setStatus("current")
_ApTrapCtrlSumStatsThresholdWlans_Type = Unsigned32
_ApTrapCtrlSumStatsThresholdWlans_Object = MibTableColumn
apTrapCtrlSumStatsThresholdWlans = _ApTrapCtrlSumStatsThresholdWlans_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 3, 1, 1, 11),
    _ApTrapCtrlSumStatsThresholdWlans_Type()
)
apTrapCtrlSumStatsThresholdWlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTrapCtrlSumStatsThresholdWlans.setStatus("current")
_ApTrapCtrlSumStatsCanBeSetAccessPoint_Type = TruthValue
_ApTrapCtrlSumStatsCanBeSetAccessPoint_Object = MibTableColumn
apTrapCtrlSumStatsCanBeSetAccessPoint = _ApTrapCtrlSumStatsCanBeSetAccessPoint_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 3, 1, 1, 12),
    _ApTrapCtrlSumStatsCanBeSetAccessPoint_Type()
)
apTrapCtrlSumStatsCanBeSetAccessPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapCtrlSumStatsCanBeSetAccessPoint.setStatus("current")
_ApTrapCtrlSumStatsThresholdAccessPoint_Type = Unsigned32
_ApTrapCtrlSumStatsThresholdAccessPoint_Object = MibTableColumn
apTrapCtrlSumStatsThresholdAccessPoint = _ApTrapCtrlSumStatsThresholdAccessPoint_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 3, 1, 1, 13),
    _ApTrapCtrlSumStatsThresholdAccessPoint_Type()
)
apTrapCtrlSumStatsThresholdAccessPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTrapCtrlSumStatsThresholdAccessPoint.setStatus("current")
_ApTrapCtrlSumStatsCanBeSetRadioN5000MHz_Type = TruthValue
_ApTrapCtrlSumStatsCanBeSetRadioN5000MHz_Object = MibTableColumn
apTrapCtrlSumStatsCanBeSetRadioN5000MHz = _ApTrapCtrlSumStatsCanBeSetRadioN5000MHz_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 3, 1, 1, 14),
    _ApTrapCtrlSumStatsCanBeSetRadioN5000MHz_Type()
)
apTrapCtrlSumStatsCanBeSetRadioN5000MHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapCtrlSumStatsCanBeSetRadioN5000MHz.setStatus("current")
_ApTrapCtrlSumStatsThresholdRadioN5000MHz_Type = Unsigned32
_ApTrapCtrlSumStatsThresholdRadioN5000MHz_Object = MibTableColumn
apTrapCtrlSumStatsThresholdRadioN5000MHz = _ApTrapCtrlSumStatsThresholdRadioN5000MHz_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 3, 1, 1, 15),
    _ApTrapCtrlSumStatsThresholdRadioN5000MHz_Type()
)
apTrapCtrlSumStatsThresholdRadioN5000MHz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTrapCtrlSumStatsThresholdRadioN5000MHz.setStatus("current")
_ApTrapCtrlSumStatsCanBeSetRadioN2400MHz_Type = TruthValue
_ApTrapCtrlSumStatsCanBeSetRadioN2400MHz_Object = MibTableColumn
apTrapCtrlSumStatsCanBeSetRadioN2400MHz = _ApTrapCtrlSumStatsCanBeSetRadioN2400MHz_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 3, 1, 1, 16),
    _ApTrapCtrlSumStatsCanBeSetRadioN2400MHz_Type()
)
apTrapCtrlSumStatsCanBeSetRadioN2400MHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapCtrlSumStatsCanBeSetRadioN2400MHz.setStatus("current")
_ApTrapCtrlSumStatsThresholdRadioN2400MHz_Type = Unsigned32
_ApTrapCtrlSumStatsThresholdRadioN2400MHz_Object = MibTableColumn
apTrapCtrlSumStatsThresholdRadioN2400MHz = _ApTrapCtrlSumStatsThresholdRadioN2400MHz_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 3, 1, 1, 17),
    _ApTrapCtrlSumStatsThresholdRadioN2400MHz_Type()
)
apTrapCtrlSumStatsThresholdRadioN2400MHz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTrapCtrlSumStatsThresholdRadioN2400MHz.setStatus("current")
_ApTrapMuVlan_ObjectIdentity = ObjectIdentity
apTrapMuVlan = _ApTrapMuVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 4)
)
_ApTrapMuMac_Type = PhysAddress
_ApTrapMuMac_Object = MibScalar
apTrapMuMac = _ApTrapMuMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 4, 1),
    _ApTrapMuMac_Type()
)
apTrapMuMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apTrapMuMac.setStatus("current")
_ApTrapRadioMac_Type = PhysAddress
_ApTrapRadioMac_Object = MibScalar
apTrapRadioMac = _ApTrapRadioMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 4, 2),
    _ApTrapRadioMac_Type()
)
apTrapRadioMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apTrapRadioMac.setStatus("current")
_ApTrapVlanId_Type = Integer32
_ApTrapVlanId_Object = MibScalar
apTrapVlanId = _ApTrapVlanId_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 4, 3),
    _ApTrapVlanId_Type()
)
apTrapVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apTrapVlanId.setStatus("current")
_ApTrapLanMonitor_ObjectIdentity = ObjectIdentity
apTrapLanMonitor = _ApTrapLanMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 5)
)


class _ApTrapLanMonitorMode_Type(Integer32):
    """Custom type apTrapLanMonitorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radioRestore", 2),
          ("radioShutdown", 1))
    )


_ApTrapLanMonitorMode_Type.__name__ = "Integer32"
_ApTrapLanMonitorMode_Object = MibScalar
apTrapLanMonitorMode = _ApTrapLanMonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 5, 1),
    _ApTrapLanMonitorMode_Type()
)
apTrapLanMonitorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTrapLanMonitorMode.setStatus("current")


class _ApTrapLanMonitorReason_Type(Integer32):
    """Custom type apTrapLanMonitorReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("hardwareDetect", 2),
          ("timeout", 3))
    )


_ApTrapLanMonitorReason_Type.__name__ = "Integer32"
_ApTrapLanMonitorReason_Object = MibScalar
apTrapLanMonitorReason = _ApTrapLanMonitorReason_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 5, 2),
    _ApTrapLanMonitorReason_Type()
)
apTrapLanMonitorReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apTrapLanMonitorReason.setStatus("current")
_ApTrapWpaCounterMeasure_ObjectIdentity = ObjectIdentity
apTrapWpaCounterMeasure = _ApTrapWpaCounterMeasure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 6)
)
_ApTrapWpaCounterMeasureEssid_Type = DisplayString
_ApTrapWpaCounterMeasureEssid_Object = MibScalar
apTrapWpaCounterMeasureEssid = _ApTrapWpaCounterMeasureEssid_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 6, 1),
    _ApTrapWpaCounterMeasureEssid_Type()
)
apTrapWpaCounterMeasureEssid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apTrapWpaCounterMeasureEssid.setStatus("current")
_ApTrapCtrlMuHotspotState_ObjectIdentity = ObjectIdentity
apTrapCtrlMuHotspotState = _ApTrapCtrlMuHotspotState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 7)
)
_ApTrapCtrlMuMac_Type = PhysAddress
_ApTrapCtrlMuMac_Object = MibScalar
apTrapCtrlMuMac = _ApTrapCtrlMuMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 7, 1),
    _ApTrapCtrlMuMac_Type()
)
apTrapCtrlMuMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apTrapCtrlMuMac.setStatus("current")


class _ApTrapCtrlMuHotspotStateChange_Type(Integer32):
    """Custom type apTrapCtrlMuHotspotStateChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fromDataReadyToHotspot", 2),
          ("fromHotspotToDataReady", 1))
    )


_ApTrapCtrlMuHotspotStateChange_Type.__name__ = "Integer32"
_ApTrapCtrlMuHotspotStateChange_Object = MibScalar
apTrapCtrlMuHotspotStateChange = _ApTrapCtrlMuHotspotStateChange_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 7, 2),
    _ApTrapCtrlMuHotspotStateChange_Type()
)
apTrapCtrlMuHotspotStateChange.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apTrapCtrlMuHotspotStateChange.setStatus("current")
_ApTrapCtrlDynDNSUpdate_ObjectIdentity = ObjectIdentity
apTrapCtrlDynDNSUpdate = _ApTrapCtrlDynDNSUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 8)
)
_ApTrapCtrlDynDNSUpdateIp_Type = OctetString
_ApTrapCtrlDynDNSUpdateIp_Object = MibScalar
apTrapCtrlDynDNSUpdateIp = _ApTrapCtrlDynDNSUpdateIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 8, 1),
    _ApTrapCtrlDynDNSUpdateIp_Type()
)
apTrapCtrlDynDNSUpdateIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTrapCtrlDynDNSUpdateIp.setStatus("current")
_ApTrapCtrlDynDNSUpdateHostname_Type = OctetString
_ApTrapCtrlDynDNSUpdateHostname_Object = MibScalar
apTrapCtrlDynDNSUpdateHostname = _ApTrapCtrlDynDNSUpdateHostname_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 8, 2),
    _ApTrapCtrlDynDNSUpdateHostname_Type()
)
apTrapCtrlDynDNSUpdateHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTrapCtrlDynDNSUpdateHostname.setStatus("current")
_ApTrapCtrlDynDNSUpdateStatus_Type = OctetString
_ApTrapCtrlDynDNSUpdateStatus_Object = MibScalar
apTrapCtrlDynDNSUpdateStatus = _ApTrapCtrlDynDNSUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1000, 8, 3),
    _ApTrapCtrlDynDNSUpdateStatus_Type()
)
apTrapCtrlDynDNSUpdateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTrapCtrlDynDNSUpdateStatus.setStatus("current")
_ApRap_ObjectIdentity = ObjectIdentity
apRap = _ApRap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 7)
)
_ApRapControl_ObjectIdentity = ObjectIdentity
apRapControl = _ApRapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 7, 1)
)
_ApRapControlDetectors_ObjectIdentity = ObjectIdentity
apRapControlDetectors = _ApRapControlDetectors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 7, 1, 1)
)


class _ApRapDetectorMode_Type(Integer32):
    """Custom type apRapDetectorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("scanA", 2),
          ("scanBG", 3),
          ("scanDisable", 1))
    )


_ApRapDetectorMode_Type.__name__ = "Integer32"
_ApRapDetectorMode_Object = MibScalar
apRapDetectorMode = _ApRapDetectorMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 7, 1, 1, 1),
    _ApRapDetectorMode_Type()
)
apRapDetectorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRapDetectorMode.setStatus("current")


class _ApRapDetectorABGMode_Type(Integer32):
    """Custom type apRapDetectorABGMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApRapDetectorABGMode_Type.__name__ = "Integer32"
_ApRapDetectorABGMode_Object = MibScalar
apRapDetectorABGMode = _ApRapDetectorABGMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 7, 1, 1, 2),
    _ApRapDetectorABGMode_Type()
)
apRapDetectorABGMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRapDetectorABGMode.setStatus("current")
_ApLoadCfg_ObjectIdentity = ObjectIdentity
apLoadCfg = _ApLoadCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 8)
)


class _ApLoadCfgOperation_Type(Integer32):
    """Custom type apLoadCfgOperation based on Integer32"""
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
        *(("ftpConfigAPToServer", 3),
          ("ftpConfigServerToAP", 2),
          ("sftpConfigAPToServer", 7),
          ("sftpConfigServerToAP", 6),
          ("tftpConfigAPToServer", 5),
          ("tftpConfigServerToAP", 4),
          ("unspecified", 1))
    )


_ApLoadCfgOperation_Type.__name__ = "Integer32"
_ApLoadCfgOperation_Object = MibScalar
apLoadCfgOperation = _ApLoadCfgOperation_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 8, 1),
    _ApLoadCfgOperation_Type()
)
apLoadCfgOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLoadCfgOperation.setStatus("current")


class _ApLoadCfgServerPath_Type(DisplayString):
    """Custom type apLoadCfgServerPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_ApLoadCfgServerPath_Type.__name__ = "DisplayString"
_ApLoadCfgServerPath_Object = MibScalar
apLoadCfgServerPath = _ApLoadCfgServerPath_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 8, 2),
    _ApLoadCfgServerPath_Type()
)
apLoadCfgServerPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLoadCfgServerPath.setStatus("current")


class _ApLoadCfgServerFilename_Type(DisplayString):
    """Custom type apLoadCfgServerFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_ApLoadCfgServerFilename_Type.__name__ = "DisplayString"
_ApLoadCfgServerFilename_Object = MibScalar
apLoadCfgServerFilename = _ApLoadCfgServerFilename_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 8, 3),
    _ApLoadCfgServerFilename_Type()
)
apLoadCfgServerFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLoadCfgServerFilename.setStatus("current")
_ApLoadCfgServerIpAddr_Type = IpAddress
_ApLoadCfgServerIpAddr_Object = MibScalar
apLoadCfgServerIpAddr = _ApLoadCfgServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 8, 4),
    _ApLoadCfgServerIpAddr_Type()
)
apLoadCfgServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLoadCfgServerIpAddr.setStatus("current")


class _ApLoadCfgFtpUsername_Type(DisplayString):
    """Custom type apLoadCfgFtpUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_ApLoadCfgFtpUsername_Type.__name__ = "DisplayString"
_ApLoadCfgFtpUsername_Object = MibScalar
apLoadCfgFtpUsername = _ApLoadCfgFtpUsername_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 8, 5),
    _ApLoadCfgFtpUsername_Type()
)
apLoadCfgFtpUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLoadCfgFtpUsername.setStatus("current")


class _ApLoadCfgFtpPassword_Type(DisplayString):
    """Custom type apLoadCfgFtpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_ApLoadCfgFtpPassword_Type.__name__ = "DisplayString"
_ApLoadCfgFtpPassword_Object = MibScalar
apLoadCfgFtpPassword = _ApLoadCfgFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 8, 6),
    _ApLoadCfgFtpPassword_Type()
)
apLoadCfgFtpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLoadCfgFtpPassword.setStatus("current")
_ApLoadCfgStart_Type = TruthValue
_ApLoadCfgStart_Object = MibScalar
apLoadCfgStart = _ApLoadCfgStart_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 8, 7),
    _ApLoadCfgStart_Type()
)
apLoadCfgStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLoadCfgStart.setStatus("current")
_ApLoadCfgOperationsDone_Type = Counter32
_ApLoadCfgOperationsDone_Object = MibScalar
apLoadCfgOperationsDone = _ApLoadCfgOperationsDone_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 8, 8),
    _ApLoadCfgOperationsDone_Type()
)
apLoadCfgOperationsDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLoadCfgOperationsDone.setStatus("current")
_ApLoadCfgResult_Type = DisplayString
_ApLoadCfgResult_Object = MibScalar
apLoadCfgResult = _ApLoadCfgResult_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 8, 9),
    _ApLoadCfgResult_Type()
)
apLoadCfgResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLoadCfgResult.setStatus("current")
_ApLoadCfgSuccess_Type = TruthValue
_ApLoadCfgSuccess_Object = MibScalar
apLoadCfgSuccess = _ApLoadCfgSuccess_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 8, 10),
    _ApLoadCfgSuccess_Type()
)
apLoadCfgSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLoadCfgSuccess.setStatus("current")
_ApStats_ObjectIdentity = ObjectIdentity
apStats = _ApStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9)
)
_ApWanClearStats_Type = DoActionNow
_ApWanClearStats_Object = MibScalar
apWanClearStats = _ApWanClearStats_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 1),
    _ApWanClearStats_Type()
)
apWanClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWanClearStats.setStatus("current")


class _ApLanClearStats_Type(Integer32):
    """Custom type apLanClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lan1", 1),
          ("lan2", 2))
    )


_ApLanClearStats_Type.__name__ = "Integer32"
_ApLanClearStats_Object = MibScalar
apLanClearStats = _ApLanClearStats_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 2),
    _ApLanClearStats_Type()
)
apLanClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanClearStats.setStatus("current")
_ApRadioClearStats_Type = DoActionNow
_ApRadioClearStats_Object = MibScalar
apRadioClearStats = _ApRadioClearStats_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 3),
    _ApRadioClearStats_Type()
)
apRadioClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioClearStats.setStatus("current")
_ApWlanClearStats_Type = DoActionNow
_ApWlanClearStats_Object = MibScalar
apWlanClearStats = _ApWlanClearStats_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 4),
    _ApWlanClearStats_Type()
)
apWlanClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWlanClearStats.setStatus("current")
_ApMuClearStats_Type = DoActionNow
_ApMuClearStats_Object = MibScalar
apMuClearStats = _ApMuClearStats_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 5),
    _ApMuClearStats_Type()
)
apMuClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMuClearStats.setStatus("current")
_ApKnownAPClearStats_Type = DoActionNow
_ApKnownAPClearStats_Object = MibScalar
apKnownAPClearStats = _ApKnownAPClearStats_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 6),
    _ApKnownAPClearStats_Type()
)
apKnownAPClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apKnownAPClearStats.setStatus("current")
_ApWirelessAPStats_ObjectIdentity = ObjectIdentity
apWirelessAPStats = _ApWirelessAPStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7)
)
_ApMeshStatsTable_Object = MibTable
apMeshStatsTable = _ApMeshStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 1)
)
if mibBuilder.loadTexts:
    apMeshStatsTable.setStatus("current")
_ApMeshStatsEntry_Object = MibTableRow
apMeshStatsEntry = _ApMeshStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 1, 1)
)
apMeshStatsEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apMeshStatsIndex"),
)
if mibBuilder.loadTexts:
    apMeshStatsEntry.setStatus("current")


class _ApMeshStatsIndex_Type(Integer32):
    """Custom type apMeshStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_ApMeshStatsIndex_Type.__name__ = "Integer32"
_ApMeshStatsIndex_Object = MibTableColumn
apMeshStatsIndex = _ApMeshStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 1, 1, 1),
    _ApMeshStatsIndex_Type()
)
apMeshStatsIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apMeshStatsIndex.setStatus("current")


class _ApMeshStatsConnType_Type(Integer32):
    """Custom type apMeshStatsConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("baseBridge", 2),
          ("clientBridge", 3),
          ("none", 1))
    )


_ApMeshStatsConnType_Type.__name__ = "Integer32"
_ApMeshStatsConnType_Object = MibTableColumn
apMeshStatsConnType = _ApMeshStatsConnType_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 1, 1, 2),
    _ApMeshStatsConnType_Type()
)
apMeshStatsConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshStatsConnType.setStatus("current")
_ApMeshStatsMac_Type = PhysAddress
_ApMeshStatsMac_Object = MibTableColumn
apMeshStatsMac = _ApMeshStatsMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 1, 1, 3),
    _ApMeshStatsMac_Type()
)
apMeshStatsMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshStatsMac.setStatus("current")
_ApMeshStatsWlanPtr_Type = SinglePointer
_ApMeshStatsWlanPtr_Object = MibTableColumn
apMeshStatsWlanPtr = _ApMeshStatsWlanPtr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 1, 1, 4),
    _ApMeshStatsWlanPtr_Type()
)
apMeshStatsWlanPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshStatsWlanPtr.setStatus("current")


class _ApMeshStatsRadioType_Type(Integer32):
    """Custom type apMeshStatsRadioType based on Integer32"""
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
        *(("dot11a", 1),
          ("dot11bg", 2),
          ("dot11n2400MHz", 3),
          ("dot11n5000MHz", 4))
    )


_ApMeshStatsRadioType_Type.__name__ = "Integer32"
_ApMeshStatsRadioType_Object = MibTableColumn
apMeshStatsRadioType = _ApMeshStatsRadioType_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 1, 1, 5),
    _ApMeshStatsRadioType_Type()
)
apMeshStatsRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshStatsRadioType.setStatus("current")
_ApMeshStatsThroughput_Type = Integer32
_ApMeshStatsThroughput_Object = MibTableColumn
apMeshStatsThroughput = _ApMeshStatsThroughput_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 1, 1, 6),
    _ApMeshStatsThroughput_Type()
)
apMeshStatsThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshStatsThroughput.setStatus("current")
_ApMeshStatsAvgBitSpeed_Type = Integer32
_ApMeshStatsAvgBitSpeed_Object = MibTableColumn
apMeshStatsAvgBitSpeed = _ApMeshStatsAvgBitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 1, 1, 7),
    _ApMeshStatsAvgBitSpeed_Type()
)
apMeshStatsAvgBitSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshStatsAvgBitSpeed.setStatus("current")
_ApMeshStatsRetries_Type = Integer32
_ApMeshStatsRetries_Object = MibTableColumn
apMeshStatsRetries = _ApMeshStatsRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 1, 1, 8),
    _ApMeshStatsRetries_Type()
)
apMeshStatsRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshStatsRetries.setStatus("current")
_ApMeshBridgeStatsTable_Object = MibTable
apMeshBridgeStatsTable = _ApMeshBridgeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 2)
)
if mibBuilder.loadTexts:
    apMeshBridgeStatsTable.setStatus("current")
_ApMeshBridgeStatsEntry_Object = MibTableRow
apMeshBridgeStatsEntry = _ApMeshBridgeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 2, 1)
)
apMeshBridgeStatsEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apMeshBridgeStatsIndex"),
)
if mibBuilder.loadTexts:
    apMeshBridgeStatsEntry.setStatus("current")


class _ApMeshBridgeStatsIndex_Type(Integer32):
    """Custom type apMeshBridgeStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_ApMeshBridgeStatsIndex_Type.__name__ = "Integer32"
_ApMeshBridgeStatsIndex_Object = MibTableColumn
apMeshBridgeStatsIndex = _ApMeshBridgeStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 2, 1, 1),
    _ApMeshBridgeStatsIndex_Type()
)
apMeshBridgeStatsIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apMeshBridgeStatsIndex.setStatus("current")
_ApMeshBridgeStatsMac_Type = PhysAddress
_ApMeshBridgeStatsMac_Object = MibTableColumn
apMeshBridgeStatsMac = _ApMeshBridgeStatsMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 2, 1, 2),
    _ApMeshBridgeStatsMac_Type()
)
apMeshBridgeStatsMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshBridgeStatsMac.setStatus("current")
_ApMeshBridgeStatsWlanPtr_Type = SinglePointer
_ApMeshBridgeStatsWlanPtr_Object = MibTableColumn
apMeshBridgeStatsWlanPtr = _ApMeshBridgeStatsWlanPtr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 2, 1, 3),
    _ApMeshBridgeStatsWlanPtr_Type()
)
apMeshBridgeStatsWlanPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshBridgeStatsWlanPtr.setStatus("current")
_ApMeshBridgeStatsLanPtr_Type = SinglePointer
_ApMeshBridgeStatsLanPtr_Object = MibTableColumn
apMeshBridgeStatsLanPtr = _ApMeshBridgeStatsLanPtr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 2, 1, 4),
    _ApMeshBridgeStatsLanPtr_Type()
)
apMeshBridgeStatsLanPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshBridgeStatsLanPtr.setStatus("current")


class _ApMeshBridgeStatsRadioType_Type(Integer32):
    """Custom type apMeshBridgeStatsRadioType based on Integer32"""
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
        *(("dot11a", 1),
          ("dot11bg", 2),
          ("dot11n2400MHz", 3),
          ("dot11n5000MHz", 4))
    )


_ApMeshBridgeStatsRadioType_Type.__name__ = "Integer32"
_ApMeshBridgeStatsRadioType_Object = MibTableColumn
apMeshBridgeStatsRadioType = _ApMeshBridgeStatsRadioType_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 2, 1, 5),
    _ApMeshBridgeStatsRadioType_Type()
)
apMeshBridgeStatsRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshBridgeStatsRadioType.setStatus("current")


class _ApMeshBridgeStatsAuthType_Type(Integer32):
    """Custom type apMeshBridgeStatsAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eap", 2),
          ("kerberos", 3),
          ("none", 1))
    )


_ApMeshBridgeStatsAuthType_Type.__name__ = "Integer32"
_ApMeshBridgeStatsAuthType_Object = MibTableColumn
apMeshBridgeStatsAuthType = _ApMeshBridgeStatsAuthType_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 2, 1, 6),
    _ApMeshBridgeStatsAuthType_Type()
)
apMeshBridgeStatsAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshBridgeStatsAuthType.setStatus("current")


class _ApMeshBridgeStatsEncType_Type(Integer32):
    """Custom type apMeshBridgeStatsEncType based on Integer32"""
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
        *(("keyguard", 4),
          ("none", 1),
          ("wep128", 3),
          ("wep64", 2),
          ("wpa2Ccmp", 6),
          ("wpaTkip", 5))
    )


_ApMeshBridgeStatsEncType_Type.__name__ = "Integer32"
_ApMeshBridgeStatsEncType_Object = MibTableColumn
apMeshBridgeStatsEncType = _ApMeshBridgeStatsEncType_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 2, 1, 7),
    _ApMeshBridgeStatsEncType_Type()
)
apMeshBridgeStatsEncType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshBridgeStatsEncType.setStatus("current")
_ApMeshBridgeStatsPktsPerSecRx_Type = Integer32
_ApMeshBridgeStatsPktsPerSecRx_Object = MibTableColumn
apMeshBridgeStatsPktsPerSecRx = _ApMeshBridgeStatsPktsPerSecRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 2, 1, 8),
    _ApMeshBridgeStatsPktsPerSecRx_Type()
)
apMeshBridgeStatsPktsPerSecRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshBridgeStatsPktsPerSecRx.setStatus("current")
_ApMeshBridgeStatsPksPerSecTx_Type = Integer32
_ApMeshBridgeStatsPksPerSecTx_Object = MibTableColumn
apMeshBridgeStatsPksPerSecTx = _ApMeshBridgeStatsPksPerSecTx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 2, 1, 9),
    _ApMeshBridgeStatsPksPerSecTx_Type()
)
apMeshBridgeStatsPksPerSecTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshBridgeStatsPksPerSecTx.setStatus("current")
_ApMeshBridgeStatsPktsPerSecTotal_Type = Integer32
_ApMeshBridgeStatsPktsPerSecTotal_Object = MibTableColumn
apMeshBridgeStatsPktsPerSecTotal = _ApMeshBridgeStatsPktsPerSecTotal_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 2, 1, 10),
    _ApMeshBridgeStatsPktsPerSecTotal_Type()
)
apMeshBridgeStatsPktsPerSecTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshBridgeStatsPktsPerSecTotal.setStatus("current")
_ApMeshBridgeStatsThroughputRx_Type = Integer32
_ApMeshBridgeStatsThroughputRx_Object = MibTableColumn
apMeshBridgeStatsThroughputRx = _ApMeshBridgeStatsThroughputRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 2, 1, 11),
    _ApMeshBridgeStatsThroughputRx_Type()
)
apMeshBridgeStatsThroughputRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshBridgeStatsThroughputRx.setStatus("current")
_ApMeshBridgeStatsThroughputTx_Type = Integer32
_ApMeshBridgeStatsThroughputTx_Object = MibTableColumn
apMeshBridgeStatsThroughputTx = _ApMeshBridgeStatsThroughputTx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 2, 1, 12),
    _ApMeshBridgeStatsThroughputTx_Type()
)
apMeshBridgeStatsThroughputTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshBridgeStatsThroughputTx.setStatus("current")
_ApMeshBridgeStatsThroughputTotal_Type = Integer32
_ApMeshBridgeStatsThroughputTotal_Object = MibTableColumn
apMeshBridgeStatsThroughputTotal = _ApMeshBridgeStatsThroughputTotal_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 2, 1, 13),
    _ApMeshBridgeStatsThroughputTotal_Type()
)
apMeshBridgeStatsThroughputTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshBridgeStatsThroughputTotal.setStatus("current")
_ApMeshBridgeStatsAvgBitSpeed_Type = Integer32
_ApMeshBridgeStatsAvgBitSpeed_Object = MibTableColumn
apMeshBridgeStatsAvgBitSpeed = _ApMeshBridgeStatsAvgBitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 2, 1, 14),
    _ApMeshBridgeStatsAvgBitSpeed_Type()
)
apMeshBridgeStatsAvgBitSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshBridgeStatsAvgBitSpeed.setStatus("current")
_ApMeshBridgeStatsAvgMuSignal_Type = Integer32
_ApMeshBridgeStatsAvgMuSignal_Object = MibTableColumn
apMeshBridgeStatsAvgMuSignal = _ApMeshBridgeStatsAvgMuSignal_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 2, 1, 15),
    _ApMeshBridgeStatsAvgMuSignal_Type()
)
apMeshBridgeStatsAvgMuSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshBridgeStatsAvgMuSignal.setStatus("current")
_ApMeshBridgeStatsAvgMuNoise_Type = Integer32
_ApMeshBridgeStatsAvgMuNoise_Object = MibTableColumn
apMeshBridgeStatsAvgMuNoise = _ApMeshBridgeStatsAvgMuNoise_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 2, 1, 16),
    _ApMeshBridgeStatsAvgMuNoise_Type()
)
apMeshBridgeStatsAvgMuNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshBridgeStatsAvgMuNoise.setStatus("current")
_ApMeshBridgeStatsAvgMuSnr_Type = Integer32
_ApMeshBridgeStatsAvgMuSnr_Object = MibTableColumn
apMeshBridgeStatsAvgMuSnr = _ApMeshBridgeStatsAvgMuSnr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 2, 1, 17),
    _ApMeshBridgeStatsAvgMuSnr_Type()
)
apMeshBridgeStatsAvgMuSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshBridgeStatsAvgMuSnr.setStatus("current")
_ApMeshBridgeStatsAvgRetries_Type = Integer32
_ApMeshBridgeStatsAvgRetries_Object = MibTableColumn
apMeshBridgeStatsAvgRetries = _ApMeshBridgeStatsAvgRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 2, 1, 18),
    _ApMeshBridgeStatsAvgRetries_Type()
)
apMeshBridgeStatsAvgRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshBridgeStatsAvgRetries.setStatus("current")
_ApMeshBridgeStatsPktsDropped_Type = Integer32
_ApMeshBridgeStatsPktsDropped_Object = MibTableColumn
apMeshBridgeStatsPktsDropped = _ApMeshBridgeStatsPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 2, 1, 19),
    _ApMeshBridgeStatsPktsDropped_Type()
)
apMeshBridgeStatsPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshBridgeStatsPktsDropped.setStatus("current")
_ApMeshBridgeStatsUndecryptablePkts_Type = Integer32
_ApMeshBridgeStatsUndecryptablePkts_Object = MibTableColumn
apMeshBridgeStatsUndecryptablePkts = _ApMeshBridgeStatsUndecryptablePkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 2, 1, 20),
    _ApMeshBridgeStatsUndecryptablePkts_Type()
)
apMeshBridgeStatsUndecryptablePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMeshBridgeStatsUndecryptablePkts.setStatus("current")
_ApLanSTPStatsTable_Object = MibTable
apLanSTPStatsTable = _ApLanSTPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 3)
)
if mibBuilder.loadTexts:
    apLanSTPStatsTable.setStatus("current")
_ApLanSTPStatsEntry_Object = MibTableRow
apLanSTPStatsEntry = _ApLanSTPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 3, 1)
)
if mibBuilder.loadTexts:
    apLanSTPStatsEntry.setStatus("current")


class _ApLanSTPStatsDesignatedRoot_Type(OctetString):
    """Custom type apLanSTPStatsDesignatedRoot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApLanSTPStatsDesignatedRoot_Type.__name__ = "OctetString"
_ApLanSTPStatsDesignatedRoot_Object = MibTableColumn
apLanSTPStatsDesignatedRoot = _ApLanSTPStatsDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 3, 1, 1),
    _ApLanSTPStatsDesignatedRoot_Type()
)
apLanSTPStatsDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanSTPStatsDesignatedRoot.setStatus("current")


class _ApLanSTPStatsBridgeId_Type(OctetString):
    """Custom type apLanSTPStatsBridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApLanSTPStatsBridgeId_Type.__name__ = "OctetString"
_ApLanSTPStatsBridgeId_Object = MibTableColumn
apLanSTPStatsBridgeId = _ApLanSTPStatsBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 3, 1, 2),
    _ApLanSTPStatsBridgeId_Type()
)
apLanSTPStatsBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanSTPStatsBridgeId.setStatus("current")
_ApLanSTPStatsRootPort_Type = Integer32
_ApLanSTPStatsRootPort_Object = MibTableColumn
apLanSTPStatsRootPort = _ApLanSTPStatsRootPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 3, 1, 3),
    _ApLanSTPStatsRootPort_Type()
)
apLanSTPStatsRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanSTPStatsRootPort.setStatus("current")
_ApLanSTPStatsRootPathCost_Type = Integer32
_ApLanSTPStatsRootPathCost_Object = MibTableColumn
apLanSTPStatsRootPathCost = _ApLanSTPStatsRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 3, 1, 4),
    _ApLanSTPStatsRootPathCost_Type()
)
apLanSTPStatsRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanSTPStatsRootPathCost.setStatus("current")
_ApLanSTPStatsBridgeMaxMsgAge_Type = Integer32
_ApLanSTPStatsBridgeMaxMsgAge_Object = MibTableColumn
apLanSTPStatsBridgeMaxMsgAge = _ApLanSTPStatsBridgeMaxMsgAge_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 3, 1, 5),
    _ApLanSTPStatsBridgeMaxMsgAge_Type()
)
apLanSTPStatsBridgeMaxMsgAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanSTPStatsBridgeMaxMsgAge.setStatus("current")
_ApLanSTPStatsBridgeHelloTime_Type = Integer32
_ApLanSTPStatsBridgeHelloTime_Object = MibTableColumn
apLanSTPStatsBridgeHelloTime = _ApLanSTPStatsBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 3, 1, 6),
    _ApLanSTPStatsBridgeHelloTime_Type()
)
apLanSTPStatsBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanSTPStatsBridgeHelloTime.setStatus("current")
_ApLanSTPStatsBridgeFwDelay_Type = Integer32
_ApLanSTPStatsBridgeFwDelay_Object = MibTableColumn
apLanSTPStatsBridgeFwDelay = _ApLanSTPStatsBridgeFwDelay_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 3, 1, 7),
    _ApLanSTPStatsBridgeFwDelay_Type()
)
apLanSTPStatsBridgeFwDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanSTPStatsBridgeFwDelay.setStatus("current")
_ApLanSTPStatsPortIntfTable_Object = MibTable
apLanSTPStatsPortIntfTable = _ApLanSTPStatsPortIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 4)
)
if mibBuilder.loadTexts:
    apLanSTPStatsPortIntfTable.setStatus("current")
_ApLanSTPStatsPortIntfEntry_Object = MibTableRow
apLanSTPStatsPortIntfEntry = _ApLanSTPStatsPortIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 4, 1)
)
apLanSTPStatsPortIntfEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apLanSTPStatsPortIntfLanIndex"),
    (0, "SYMBOL-AP-MIB", "apLanSTPStatsPortIntfPortIndex"),
)
if mibBuilder.loadTexts:
    apLanSTPStatsPortIntfEntry.setStatus("current")


class _ApLanSTPStatsPortIntfLanIndex_Type(Integer32):
    """Custom type apLanSTPStatsPortIntfLanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ApLanSTPStatsPortIntfLanIndex_Type.__name__ = "Integer32"
_ApLanSTPStatsPortIntfLanIndex_Object = MibTableColumn
apLanSTPStatsPortIntfLanIndex = _ApLanSTPStatsPortIntfLanIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 4, 1, 1),
    _ApLanSTPStatsPortIntfLanIndex_Type()
)
apLanSTPStatsPortIntfLanIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apLanSTPStatsPortIntfLanIndex.setStatus("current")


class _ApLanSTPStatsPortIntfPortIndex_Type(Integer32):
    """Custom type apLanSTPStatsPortIntfPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 33),
    )


_ApLanSTPStatsPortIntfPortIndex_Type.__name__ = "Integer32"
_ApLanSTPStatsPortIntfPortIndex_Object = MibTableColumn
apLanSTPStatsPortIntfPortIndex = _ApLanSTPStatsPortIntfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 4, 1, 2),
    _ApLanSTPStatsPortIntfPortIndex_Type()
)
apLanSTPStatsPortIntfPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLanSTPStatsPortIntfPortIndex.setStatus("current")
_ApLanSTPStatsPortIntfPortName_Type = DisplayString
_ApLanSTPStatsPortIntfPortName_Object = MibTableColumn
apLanSTPStatsPortIntfPortName = _ApLanSTPStatsPortIntfPortName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 4, 1, 3),
    _ApLanSTPStatsPortIntfPortName_Type()
)
apLanSTPStatsPortIntfPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanSTPStatsPortIntfPortName.setStatus("current")


class _ApLanSTPStatsPortIntfState_Type(Integer32):
    """Custom type apLanSTPStatsPortIntfState based on Integer32"""
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
        *(("blocking", 5),
          ("disabled", 1),
          ("forwarding", 4),
          ("learning", 3),
          ("listening", 2),
          ("unknown", 6))
    )


_ApLanSTPStatsPortIntfState_Type.__name__ = "Integer32"
_ApLanSTPStatsPortIntfState_Object = MibTableColumn
apLanSTPStatsPortIntfState = _ApLanSTPStatsPortIntfState_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 4, 1, 4),
    _ApLanSTPStatsPortIntfState_Type()
)
apLanSTPStatsPortIntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanSTPStatsPortIntfState.setStatus("current")
_ApLanSTPStatsPortIntfPathCost_Type = Integer32
_ApLanSTPStatsPortIntfPathCost_Object = MibTableColumn
apLanSTPStatsPortIntfPathCost = _ApLanSTPStatsPortIntfPathCost_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 4, 1, 5),
    _ApLanSTPStatsPortIntfPathCost_Type()
)
apLanSTPStatsPortIntfPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanSTPStatsPortIntfPathCost.setStatus("current")


class _ApLanSTPStatsPortIntfDsgRoot_Type(OctetString):
    """Custom type apLanSTPStatsPortIntfDsgRoot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApLanSTPStatsPortIntfDsgRoot_Type.__name__ = "OctetString"
_ApLanSTPStatsPortIntfDsgRoot_Object = MibTableColumn
apLanSTPStatsPortIntfDsgRoot = _ApLanSTPStatsPortIntfDsgRoot_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 4, 1, 6),
    _ApLanSTPStatsPortIntfDsgRoot_Type()
)
apLanSTPStatsPortIntfDsgRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanSTPStatsPortIntfDsgRoot.setStatus("current")


class _ApLanSTPStatsPortIntfDsgBridge_Type(OctetString):
    """Custom type apLanSTPStatsPortIntfDsgBridge based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApLanSTPStatsPortIntfDsgBridge_Type.__name__ = "OctetString"
_ApLanSTPStatsPortIntfDsgBridge_Object = MibTableColumn
apLanSTPStatsPortIntfDsgBridge = _ApLanSTPStatsPortIntfDsgBridge_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 4, 1, 7),
    _ApLanSTPStatsPortIntfDsgBridge_Type()
)
apLanSTPStatsPortIntfDsgBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanSTPStatsPortIntfDsgBridge.setStatus("current")


class _ApLanSTPStatsPortIntfDsgPort_Type(OctetString):
    """Custom type apLanSTPStatsPortIntfDsgPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApLanSTPStatsPortIntfDsgPort_Type.__name__ = "OctetString"
_ApLanSTPStatsPortIntfDsgPort_Object = MibTableColumn
apLanSTPStatsPortIntfDsgPort = _ApLanSTPStatsPortIntfDsgPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 4, 1, 8),
    _ApLanSTPStatsPortIntfDsgPort_Type()
)
apLanSTPStatsPortIntfDsgPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanSTPStatsPortIntfDsgPort.setStatus("current")
_ApLanSTPStatsPortIntfDsgCost_Type = Integer32
_ApLanSTPStatsPortIntfDsgCost_Object = MibTableColumn
apLanSTPStatsPortIntfDsgCost = _ApLanSTPStatsPortIntfDsgCost_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 7, 4, 1, 9),
    _ApLanSTPStatsPortIntfDsgCost_Type()
)
apLanSTPStatsPortIntfDsgCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanSTPStatsPortIntfDsgCost.setStatus("current")
_ApnStats_ObjectIdentity = ObjectIdentity
apnStats = _ApnStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8)
)
_ApnRadioStatsTable_Object = MibTable
apnRadioStatsTable = _ApnRadioStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 1)
)
if mibBuilder.loadTexts:
    apnRadioStatsTable.setStatus("current")
_ApnRadioStatsEntry_Object = MibTableRow
apnRadioStatsEntry = _ApnRadioStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 1, 1)
)
apnRadioStatsEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apnRadioStatsIndex"),
)
if mibBuilder.loadTexts:
    apnRadioStatsEntry.setStatus("current")


class _ApnRadioStatsIndex_Type(Integer32):
    """Custom type apnRadioStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ApnRadioStatsIndex_Type.__name__ = "Integer32"
_ApnRadioStatsIndex_Object = MibTableColumn
apnRadioStatsIndex = _ApnRadioStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 1, 1, 2),
    _ApnRadioStatsIndex_Type()
)
apnRadioStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnRadioStatsIndex.setStatus("current")
_ApnRadioStatsBssid_Type = PhysAddress
_ApnRadioStatsBssid_Object = MibTableColumn
apnRadioStatsBssid = _ApnRadioStatsBssid_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 1, 1, 3),
    _ApnRadioStatsBssid_Type()
)
apnRadioStatsBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnRadioStatsBssid.setStatus("current")
_ApnRadioStatsApSsid_Type = DisplayString
_ApnRadioStatsApSsid_Object = MibTableColumn
apnRadioStatsApSsid = _ApnRadioStatsApSsid_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 1, 1, 4),
    _ApnRadioStatsApSsid_Type()
)
apnRadioStatsApSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnRadioStatsApSsid.setStatus("current")
_ApnRadioStatsChannel_Type = Integer32
_ApnRadioStatsChannel_Object = MibTableColumn
apnRadioStatsChannel = _ApnRadioStatsChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 1, 1, 5),
    _ApnRadioStatsChannel_Type()
)
apnRadioStatsChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnRadioStatsChannel.setStatus("current")
_ApnRadioStatsExtnChannel_Type = Integer32
_ApnRadioStatsExtnChannel_Object = MibTableColumn
apnRadioStatsExtnChannel = _ApnRadioStatsExtnChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 1, 1, 6),
    _ApnRadioStatsExtnChannel_Type()
)
apnRadioStatsExtnChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnRadioStatsExtnChannel.setStatus("current")
_ApnRadioStatsRssiAvgAcrossAntennas_Type = Integer32
_ApnRadioStatsRssiAvgAcrossAntennas_Object = MibTableColumn
apnRadioStatsRssiAvgAcrossAntennas = _ApnRadioStatsRssiAvgAcrossAntennas_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 1, 1, 7),
    _ApnRadioStatsRssiAvgAcrossAntennas_Type()
)
apnRadioStatsRssiAvgAcrossAntennas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnRadioStatsRssiAvgAcrossAntennas.setStatus("current")
if mibBuilder.loadTexts:
    apnRadioStatsRssiAvgAcrossAntennas.setUnits("dBm")


class _ApnRadioStatsChannelWidthMode_Type(Integer32):
    """Custom type apnRadioStatsChannelWidthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fortyMHz", 2),
          ("pco", 3),
          ("twentyMHz", 1))
    )


_ApnRadioStatsChannelWidthMode_Type.__name__ = "Integer32"
_ApnRadioStatsChannelWidthMode_Object = MibTableColumn
apnRadioStatsChannelWidthMode = _ApnRadioStatsChannelWidthMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 1, 1, 8),
    _ApnRadioStatsChannelWidthMode_Type()
)
apnRadioStatsChannelWidthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnRadioStatsChannelWidthMode.setStatus("current")


class _ApnRadioStatsOpFreq_Type(Integer32):
    """Custom type apnRadioStatsOpFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("freq2400MHz", 1),
          ("freq2400MHzAnd5000MHz", 3),
          ("freq5000MHz", 2))
    )


_ApnRadioStatsOpFreq_Type.__name__ = "Integer32"
_ApnRadioStatsOpFreq_Object = MibTableColumn
apnRadioStatsOpFreq = _ApnRadioStatsOpFreq_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 1, 1, 9),
    _ApnRadioStatsOpFreq_Type()
)
apnRadioStatsOpFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnRadioStatsOpFreq.setStatus("current")
_ApnRadioStatsNumPktsRxSGI400ns_Type = Counter32
_ApnRadioStatsNumPktsRxSGI400ns_Object = MibTableColumn
apnRadioStatsNumPktsRxSGI400ns = _ApnRadioStatsNumPktsRxSGI400ns_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 1, 1, 10),
    _ApnRadioStatsNumPktsRxSGI400ns_Type()
)
apnRadioStatsNumPktsRxSGI400ns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnRadioStatsNumPktsRxSGI400ns.setStatus("current")
_ApnRadioStatsNumPktsRxSGI800ns_Type = Counter32
_ApnRadioStatsNumPktsRxSGI800ns_Object = MibTableColumn
apnRadioStatsNumPktsRxSGI800ns = _ApnRadioStatsNumPktsRxSGI800ns_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 1, 1, 11),
    _ApnRadioStatsNumPktsRxSGI800ns_Type()
)
apnRadioStatsNumPktsRxSGI800ns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnRadioStatsNumPktsRxSGI800ns.setStatus("current")
_ApnRadioStatsNumPktsTxSGI400ns_Type = Counter32
_ApnRadioStatsNumPktsTxSGI400ns_Object = MibTableColumn
apnRadioStatsNumPktsTxSGI400ns = _ApnRadioStatsNumPktsTxSGI400ns_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 1, 1, 12),
    _ApnRadioStatsNumPktsTxSGI400ns_Type()
)
apnRadioStatsNumPktsTxSGI400ns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnRadioStatsNumPktsTxSGI400ns.setStatus("current")
_ApnRadioStatsNumPktsTxSGI800ns_Type = Counter32
_ApnRadioStatsNumPktsTxSGI800ns_Object = MibTableColumn
apnRadioStatsNumPktsTxSGI800ns = _ApnRadioStatsNumPktsTxSGI800ns_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 1, 1, 13),
    _ApnRadioStatsNumPktsTxSGI800ns_Type()
)
apnRadioStatsNumPktsTxSGI800ns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnRadioStatsNumPktsTxSGI800ns.setStatus("current")
_ApnRadioStatsNumPktsRxChanWidth20MHz_Type = Counter32
_ApnRadioStatsNumPktsRxChanWidth20MHz_Object = MibTableColumn
apnRadioStatsNumPktsRxChanWidth20MHz = _ApnRadioStatsNumPktsRxChanWidth20MHz_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 1, 1, 14),
    _ApnRadioStatsNumPktsRxChanWidth20MHz_Type()
)
apnRadioStatsNumPktsRxChanWidth20MHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnRadioStatsNumPktsRxChanWidth20MHz.setStatus("current")
_ApnRadioStatsNumPktsRxChanWidth40MHz_Type = Counter32
_ApnRadioStatsNumPktsRxChanWidth40MHz_Object = MibTableColumn
apnRadioStatsNumPktsRxChanWidth40MHz = _ApnRadioStatsNumPktsRxChanWidth40MHz_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 1, 1, 15),
    _ApnRadioStatsNumPktsRxChanWidth40MHz_Type()
)
apnRadioStatsNumPktsRxChanWidth40MHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnRadioStatsNumPktsRxChanWidth40MHz.setStatus("current")
_ApnRadioStatsNumPktsTxChanWidth20MHz_Type = Counter32
_ApnRadioStatsNumPktsTxChanWidth20MHz_Object = MibTableColumn
apnRadioStatsNumPktsTxChanWidth20MHz = _ApnRadioStatsNumPktsTxChanWidth20MHz_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 1, 1, 16),
    _ApnRadioStatsNumPktsTxChanWidth20MHz_Type()
)
apnRadioStatsNumPktsTxChanWidth20MHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnRadioStatsNumPktsTxChanWidth20MHz.setStatus("current")
_ApnRadioStatsNumPktsTxChanWidth40MHz_Type = Counter32
_ApnRadioStatsNumPktsTxChanWidth40MHz_Object = MibTableColumn
apnRadioStatsNumPktsTxChanWidth40MHz = _ApnRadioStatsNumPktsTxChanWidth40MHz_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 1, 1, 17),
    _ApnRadioStatsNumPktsTxChanWidth40MHz_Type()
)
apnRadioStatsNumPktsTxChanWidth40MHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnRadioStatsNumPktsTxChanWidth40MHz.setStatus("current")
_ApnPortalRxPktsTable_Object = MibTable
apnPortalRxPktsTable = _ApnPortalRxPktsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2)
)
if mibBuilder.loadTexts:
    apnPortalRxPktsTable.setStatus("current")
_ApnPortalRxPktsEntry_Object = MibTableRow
apnPortalRxPktsEntry = _ApnPortalRxPktsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1)
)
apnPortalRxPktsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    apnPortalRxPktsEntry.setStatus("current")
_ApnPortalRxPktsAt1Mb_Type = Counter32
_ApnPortalRxPktsAt1Mb_Object = MibTableColumn
apnPortalRxPktsAt1Mb = _ApnPortalRxPktsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 1),
    _ApnPortalRxPktsAt1Mb_Type()
)
apnPortalRxPktsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAt1Mb.setStatus("current")
_ApnPortalRxPktsAt2Mb_Type = Counter32
_ApnPortalRxPktsAt2Mb_Object = MibTableColumn
apnPortalRxPktsAt2Mb = _ApnPortalRxPktsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 2),
    _ApnPortalRxPktsAt2Mb_Type()
)
apnPortalRxPktsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAt2Mb.setStatus("current")
_ApnPortalRxPktsAt5pt5Mb_Type = Counter32
_ApnPortalRxPktsAt5pt5Mb_Object = MibTableColumn
apnPortalRxPktsAt5pt5Mb = _ApnPortalRxPktsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 3),
    _ApnPortalRxPktsAt5pt5Mb_Type()
)
apnPortalRxPktsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAt5pt5Mb.setStatus("current")
_ApnPortalRxPktsAt6Mb_Type = Counter32
_ApnPortalRxPktsAt6Mb_Object = MibTableColumn
apnPortalRxPktsAt6Mb = _ApnPortalRxPktsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 4),
    _ApnPortalRxPktsAt6Mb_Type()
)
apnPortalRxPktsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAt6Mb.setStatus("current")
_ApnPortalRxPktsAt9Mb_Type = Counter32
_ApnPortalRxPktsAt9Mb_Object = MibTableColumn
apnPortalRxPktsAt9Mb = _ApnPortalRxPktsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 5),
    _ApnPortalRxPktsAt9Mb_Type()
)
apnPortalRxPktsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAt9Mb.setStatus("current")
_ApnPortalRxPktsAt11Mb_Type = Counter32
_ApnPortalRxPktsAt11Mb_Object = MibTableColumn
apnPortalRxPktsAt11Mb = _ApnPortalRxPktsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 6),
    _ApnPortalRxPktsAt11Mb_Type()
)
apnPortalRxPktsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAt11Mb.setStatus("current")
_ApnPortalRxPktsAt12Mb_Type = Counter32
_ApnPortalRxPktsAt12Mb_Object = MibTableColumn
apnPortalRxPktsAt12Mb = _ApnPortalRxPktsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 7),
    _ApnPortalRxPktsAt12Mb_Type()
)
apnPortalRxPktsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAt12Mb.setStatus("current")
_ApnPortalRxPktsAt18Mb_Type = Counter32
_ApnPortalRxPktsAt18Mb_Object = MibTableColumn
apnPortalRxPktsAt18Mb = _ApnPortalRxPktsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 8),
    _ApnPortalRxPktsAt18Mb_Type()
)
apnPortalRxPktsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAt18Mb.setStatus("current")
_ApnPortalRxPktsAt24Mb_Type = Counter32
_ApnPortalRxPktsAt24Mb_Object = MibTableColumn
apnPortalRxPktsAt24Mb = _ApnPortalRxPktsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 9),
    _ApnPortalRxPktsAt24Mb_Type()
)
apnPortalRxPktsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAt24Mb.setStatus("current")
_ApnPortalRxPktsAt36Mb_Type = Counter32
_ApnPortalRxPktsAt36Mb_Object = MibTableColumn
apnPortalRxPktsAt36Mb = _ApnPortalRxPktsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 10),
    _ApnPortalRxPktsAt36Mb_Type()
)
apnPortalRxPktsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAt36Mb.setStatus("current")
_ApnPortalRxPktsAt48Mb_Type = Counter32
_ApnPortalRxPktsAt48Mb_Object = MibTableColumn
apnPortalRxPktsAt48Mb = _ApnPortalRxPktsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 11),
    _ApnPortalRxPktsAt48Mb_Type()
)
apnPortalRxPktsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAt48Mb.setStatus("current")
_ApnPortalRxPktsAt54Mb_Type = Counter32
_ApnPortalRxPktsAt54Mb_Object = MibTableColumn
apnPortalRxPktsAt54Mb = _ApnPortalRxPktsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 12),
    _ApnPortalRxPktsAt54Mb_Type()
)
apnPortalRxPktsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAt54Mb.setStatus("current")
_ApnPortalRxPktsAtMCS0_Type = Counter32
_ApnPortalRxPktsAtMCS0_Object = MibTableColumn
apnPortalRxPktsAtMCS0 = _ApnPortalRxPktsAtMCS0_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 13),
    _ApnPortalRxPktsAtMCS0_Type()
)
apnPortalRxPktsAtMCS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAtMCS0.setStatus("current")
_ApnPortalRxPktsAtMCS1_Type = Counter32
_ApnPortalRxPktsAtMCS1_Object = MibTableColumn
apnPortalRxPktsAtMCS1 = _ApnPortalRxPktsAtMCS1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 14),
    _ApnPortalRxPktsAtMCS1_Type()
)
apnPortalRxPktsAtMCS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAtMCS1.setStatus("current")
_ApnPortalRxPktsAtMCS2_Type = Counter32
_ApnPortalRxPktsAtMCS2_Object = MibTableColumn
apnPortalRxPktsAtMCS2 = _ApnPortalRxPktsAtMCS2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 15),
    _ApnPortalRxPktsAtMCS2_Type()
)
apnPortalRxPktsAtMCS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAtMCS2.setStatus("current")
_ApnPortalRxPktsAtMCS3_Type = Counter32
_ApnPortalRxPktsAtMCS3_Object = MibTableColumn
apnPortalRxPktsAtMCS3 = _ApnPortalRxPktsAtMCS3_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 16),
    _ApnPortalRxPktsAtMCS3_Type()
)
apnPortalRxPktsAtMCS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAtMCS3.setStatus("current")
_ApnPortalRxPktsAtMCS4_Type = Counter32
_ApnPortalRxPktsAtMCS4_Object = MibTableColumn
apnPortalRxPktsAtMCS4 = _ApnPortalRxPktsAtMCS4_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 17),
    _ApnPortalRxPktsAtMCS4_Type()
)
apnPortalRxPktsAtMCS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAtMCS4.setStatus("current")
_ApnPortalRxPktsAtMCS5_Type = Counter32
_ApnPortalRxPktsAtMCS5_Object = MibTableColumn
apnPortalRxPktsAtMCS5 = _ApnPortalRxPktsAtMCS5_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 18),
    _ApnPortalRxPktsAtMCS5_Type()
)
apnPortalRxPktsAtMCS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAtMCS5.setStatus("current")
_ApnPortalRxPktsAtMCS6_Type = Counter32
_ApnPortalRxPktsAtMCS6_Object = MibTableColumn
apnPortalRxPktsAtMCS6 = _ApnPortalRxPktsAtMCS6_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 19),
    _ApnPortalRxPktsAtMCS6_Type()
)
apnPortalRxPktsAtMCS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAtMCS6.setStatus("current")
_ApnPortalRxPktsAtMCS7_Type = Counter32
_ApnPortalRxPktsAtMCS7_Object = MibTableColumn
apnPortalRxPktsAtMCS7 = _ApnPortalRxPktsAtMCS7_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 20),
    _ApnPortalRxPktsAtMCS7_Type()
)
apnPortalRxPktsAtMCS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAtMCS7.setStatus("current")
_ApnPortalRxPktsAtMCS8_Type = Counter32
_ApnPortalRxPktsAtMCS8_Object = MibTableColumn
apnPortalRxPktsAtMCS8 = _ApnPortalRxPktsAtMCS8_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 21),
    _ApnPortalRxPktsAtMCS8_Type()
)
apnPortalRxPktsAtMCS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAtMCS8.setStatus("current")
_ApnPortalRxPktsAtMCS9_Type = Counter32
_ApnPortalRxPktsAtMCS9_Object = MibTableColumn
apnPortalRxPktsAtMCS9 = _ApnPortalRxPktsAtMCS9_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 22),
    _ApnPortalRxPktsAtMCS9_Type()
)
apnPortalRxPktsAtMCS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAtMCS9.setStatus("current")
_ApnPortalRxPktsAtMCS10_Type = Counter32
_ApnPortalRxPktsAtMCS10_Object = MibTableColumn
apnPortalRxPktsAtMCS10 = _ApnPortalRxPktsAtMCS10_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 23),
    _ApnPortalRxPktsAtMCS10_Type()
)
apnPortalRxPktsAtMCS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAtMCS10.setStatus("current")
_ApnPortalRxPktsAtMCS11_Type = Counter32
_ApnPortalRxPktsAtMCS11_Object = MibTableColumn
apnPortalRxPktsAtMCS11 = _ApnPortalRxPktsAtMCS11_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 24),
    _ApnPortalRxPktsAtMCS11_Type()
)
apnPortalRxPktsAtMCS11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAtMCS11.setStatus("current")
_ApnPortalRxPktsAtMCS12_Type = Counter32
_ApnPortalRxPktsAtMCS12_Object = MibTableColumn
apnPortalRxPktsAtMCS12 = _ApnPortalRxPktsAtMCS12_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 25),
    _ApnPortalRxPktsAtMCS12_Type()
)
apnPortalRxPktsAtMCS12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAtMCS12.setStatus("current")
_ApnPortalRxPktsAtMCS13_Type = Counter32
_ApnPortalRxPktsAtMCS13_Object = MibTableColumn
apnPortalRxPktsAtMCS13 = _ApnPortalRxPktsAtMCS13_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 26),
    _ApnPortalRxPktsAtMCS13_Type()
)
apnPortalRxPktsAtMCS13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAtMCS13.setStatus("current")
_ApnPortalRxPktsAtMCS14_Type = Counter32
_ApnPortalRxPktsAtMCS14_Object = MibTableColumn
apnPortalRxPktsAtMCS14 = _ApnPortalRxPktsAtMCS14_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 27),
    _ApnPortalRxPktsAtMCS14_Type()
)
apnPortalRxPktsAtMCS14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAtMCS14.setStatus("current")
_ApnPortalRxPktsAtMCS15_Type = Counter32
_ApnPortalRxPktsAtMCS15_Object = MibTableColumn
apnPortalRxPktsAtMCS15 = _ApnPortalRxPktsAtMCS15_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 2, 1, 28),
    _ApnPortalRxPktsAtMCS15_Type()
)
apnPortalRxPktsAtMCS15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxPktsAtMCS15.setStatus("current")
_ApnPortalTxPktsTable_Object = MibTable
apnPortalTxPktsTable = _ApnPortalTxPktsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3)
)
if mibBuilder.loadTexts:
    apnPortalTxPktsTable.setStatus("current")
_ApnPortalTxPktsEntry_Object = MibTableRow
apnPortalTxPktsEntry = _ApnPortalTxPktsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1)
)
apnPortalTxPktsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    apnPortalTxPktsEntry.setStatus("current")
_ApnPortalTxPktsAt1Mb_Type = Counter32
_ApnPortalTxPktsAt1Mb_Object = MibTableColumn
apnPortalTxPktsAt1Mb = _ApnPortalTxPktsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 1),
    _ApnPortalTxPktsAt1Mb_Type()
)
apnPortalTxPktsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAt1Mb.setStatus("current")
_ApnPortalTxPktsAt2Mb_Type = Counter32
_ApnPortalTxPktsAt2Mb_Object = MibTableColumn
apnPortalTxPktsAt2Mb = _ApnPortalTxPktsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 2),
    _ApnPortalTxPktsAt2Mb_Type()
)
apnPortalTxPktsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAt2Mb.setStatus("current")
_ApnPortalTxPktsAt5pt5Mb_Type = Counter32
_ApnPortalTxPktsAt5pt5Mb_Object = MibTableColumn
apnPortalTxPktsAt5pt5Mb = _ApnPortalTxPktsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 3),
    _ApnPortalTxPktsAt5pt5Mb_Type()
)
apnPortalTxPktsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAt5pt5Mb.setStatus("current")
_ApnPortalTxPktsAt6Mb_Type = Counter32
_ApnPortalTxPktsAt6Mb_Object = MibTableColumn
apnPortalTxPktsAt6Mb = _ApnPortalTxPktsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 4),
    _ApnPortalTxPktsAt6Mb_Type()
)
apnPortalTxPktsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAt6Mb.setStatus("current")
_ApnPortalTxPktsAt9Mb_Type = Counter32
_ApnPortalTxPktsAt9Mb_Object = MibTableColumn
apnPortalTxPktsAt9Mb = _ApnPortalTxPktsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 5),
    _ApnPortalTxPktsAt9Mb_Type()
)
apnPortalTxPktsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAt9Mb.setStatus("current")
_ApnPortalTxPktsAt11Mb_Type = Counter32
_ApnPortalTxPktsAt11Mb_Object = MibTableColumn
apnPortalTxPktsAt11Mb = _ApnPortalTxPktsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 6),
    _ApnPortalTxPktsAt11Mb_Type()
)
apnPortalTxPktsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAt11Mb.setStatus("current")
_ApnPortalTxPktsAt12Mb_Type = Counter32
_ApnPortalTxPktsAt12Mb_Object = MibTableColumn
apnPortalTxPktsAt12Mb = _ApnPortalTxPktsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 7),
    _ApnPortalTxPktsAt12Mb_Type()
)
apnPortalTxPktsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAt12Mb.setStatus("current")
_ApnPortalTxPktsAt18Mb_Type = Counter32
_ApnPortalTxPktsAt18Mb_Object = MibTableColumn
apnPortalTxPktsAt18Mb = _ApnPortalTxPktsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 8),
    _ApnPortalTxPktsAt18Mb_Type()
)
apnPortalTxPktsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAt18Mb.setStatus("current")
_ApnPortalTxPktsAt24Mb_Type = Counter32
_ApnPortalTxPktsAt24Mb_Object = MibTableColumn
apnPortalTxPktsAt24Mb = _ApnPortalTxPktsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 9),
    _ApnPortalTxPktsAt24Mb_Type()
)
apnPortalTxPktsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAt24Mb.setStatus("current")
_ApnPortalTxPktsAt36Mb_Type = Counter32
_ApnPortalTxPktsAt36Mb_Object = MibTableColumn
apnPortalTxPktsAt36Mb = _ApnPortalTxPktsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 10),
    _ApnPortalTxPktsAt36Mb_Type()
)
apnPortalTxPktsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAt36Mb.setStatus("current")
_ApnPortalTxPktsAt48Mb_Type = Counter32
_ApnPortalTxPktsAt48Mb_Object = MibTableColumn
apnPortalTxPktsAt48Mb = _ApnPortalTxPktsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 11),
    _ApnPortalTxPktsAt48Mb_Type()
)
apnPortalTxPktsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAt48Mb.setStatus("current")
_ApnPortalTxPktsAt54Mb_Type = Counter32
_ApnPortalTxPktsAt54Mb_Object = MibTableColumn
apnPortalTxPktsAt54Mb = _ApnPortalTxPktsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 12),
    _ApnPortalTxPktsAt54Mb_Type()
)
apnPortalTxPktsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAt54Mb.setStatus("current")
_ApnPortalTxPktsAtMCS0_Type = Counter32
_ApnPortalTxPktsAtMCS0_Object = MibTableColumn
apnPortalTxPktsAtMCS0 = _ApnPortalTxPktsAtMCS0_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 13),
    _ApnPortalTxPktsAtMCS0_Type()
)
apnPortalTxPktsAtMCS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAtMCS0.setStatus("current")
_ApnPortalTxPktsAtMCS1_Type = Counter32
_ApnPortalTxPktsAtMCS1_Object = MibTableColumn
apnPortalTxPktsAtMCS1 = _ApnPortalTxPktsAtMCS1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 14),
    _ApnPortalTxPktsAtMCS1_Type()
)
apnPortalTxPktsAtMCS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAtMCS1.setStatus("current")
_ApnPortalTxPktsAtMCS2_Type = Counter32
_ApnPortalTxPktsAtMCS2_Object = MibTableColumn
apnPortalTxPktsAtMCS2 = _ApnPortalTxPktsAtMCS2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 15),
    _ApnPortalTxPktsAtMCS2_Type()
)
apnPortalTxPktsAtMCS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAtMCS2.setStatus("current")
_ApnPortalTxPktsAtMCS3_Type = Counter32
_ApnPortalTxPktsAtMCS3_Object = MibTableColumn
apnPortalTxPktsAtMCS3 = _ApnPortalTxPktsAtMCS3_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 16),
    _ApnPortalTxPktsAtMCS3_Type()
)
apnPortalTxPktsAtMCS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAtMCS3.setStatus("current")
_ApnPortalTxPktsAtMCS4_Type = Counter32
_ApnPortalTxPktsAtMCS4_Object = MibTableColumn
apnPortalTxPktsAtMCS4 = _ApnPortalTxPktsAtMCS4_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 17),
    _ApnPortalTxPktsAtMCS4_Type()
)
apnPortalTxPktsAtMCS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAtMCS4.setStatus("current")
_ApnPortalTxPktsAtMCS5_Type = Counter32
_ApnPortalTxPktsAtMCS5_Object = MibTableColumn
apnPortalTxPktsAtMCS5 = _ApnPortalTxPktsAtMCS5_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 18),
    _ApnPortalTxPktsAtMCS5_Type()
)
apnPortalTxPktsAtMCS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAtMCS5.setStatus("current")
_ApnPortalTxPktsAtMCS6_Type = Counter32
_ApnPortalTxPktsAtMCS6_Object = MibTableColumn
apnPortalTxPktsAtMCS6 = _ApnPortalTxPktsAtMCS6_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 19),
    _ApnPortalTxPktsAtMCS6_Type()
)
apnPortalTxPktsAtMCS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAtMCS6.setStatus("current")
_ApnPortalTxPktsAtMCS7_Type = Counter32
_ApnPortalTxPktsAtMCS7_Object = MibTableColumn
apnPortalTxPktsAtMCS7 = _ApnPortalTxPktsAtMCS7_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 20),
    _ApnPortalTxPktsAtMCS7_Type()
)
apnPortalTxPktsAtMCS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAtMCS7.setStatus("current")
_ApnPortalTxPktsAtMCS8_Type = Counter32
_ApnPortalTxPktsAtMCS8_Object = MibTableColumn
apnPortalTxPktsAtMCS8 = _ApnPortalTxPktsAtMCS8_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 21),
    _ApnPortalTxPktsAtMCS8_Type()
)
apnPortalTxPktsAtMCS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAtMCS8.setStatus("current")
_ApnPortalTxPktsAtMCS9_Type = Counter32
_ApnPortalTxPktsAtMCS9_Object = MibTableColumn
apnPortalTxPktsAtMCS9 = _ApnPortalTxPktsAtMCS9_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 22),
    _ApnPortalTxPktsAtMCS9_Type()
)
apnPortalTxPktsAtMCS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAtMCS9.setStatus("current")
_ApnPortalTxPktsAtMCS10_Type = Counter32
_ApnPortalTxPktsAtMCS10_Object = MibTableColumn
apnPortalTxPktsAtMCS10 = _ApnPortalTxPktsAtMCS10_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 23),
    _ApnPortalTxPktsAtMCS10_Type()
)
apnPortalTxPktsAtMCS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAtMCS10.setStatus("current")
_ApnPortalTxPktsAtMCS11_Type = Counter32
_ApnPortalTxPktsAtMCS11_Object = MibTableColumn
apnPortalTxPktsAtMCS11 = _ApnPortalTxPktsAtMCS11_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 24),
    _ApnPortalTxPktsAtMCS11_Type()
)
apnPortalTxPktsAtMCS11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAtMCS11.setStatus("current")
_ApnPortalTxPktsAtMCS12_Type = Counter32
_ApnPortalTxPktsAtMCS12_Object = MibTableColumn
apnPortalTxPktsAtMCS12 = _ApnPortalTxPktsAtMCS12_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 25),
    _ApnPortalTxPktsAtMCS12_Type()
)
apnPortalTxPktsAtMCS12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAtMCS12.setStatus("current")
_ApnPortalTxPktsAtMCS13_Type = Counter32
_ApnPortalTxPktsAtMCS13_Object = MibTableColumn
apnPortalTxPktsAtMCS13 = _ApnPortalTxPktsAtMCS13_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 26),
    _ApnPortalTxPktsAtMCS13_Type()
)
apnPortalTxPktsAtMCS13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAtMCS13.setStatus("current")
_ApnPortalTxPktsAtMCS14_Type = Counter32
_ApnPortalTxPktsAtMCS14_Object = MibTableColumn
apnPortalTxPktsAtMCS14 = _ApnPortalTxPktsAtMCS14_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 27),
    _ApnPortalTxPktsAtMCS14_Type()
)
apnPortalTxPktsAtMCS14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAtMCS14.setStatus("current")
_ApnPortalTxPktsAtMCS15_Type = Counter32
_ApnPortalTxPktsAtMCS15_Object = MibTableColumn
apnPortalTxPktsAtMCS15 = _ApnPortalTxPktsAtMCS15_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 3, 1, 28),
    _ApnPortalTxPktsAtMCS15_Type()
)
apnPortalTxPktsAtMCS15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxPktsAtMCS15.setStatus("current")
_ApnPortalRxOctetsTable_Object = MibTable
apnPortalRxOctetsTable = _ApnPortalRxOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4)
)
if mibBuilder.loadTexts:
    apnPortalRxOctetsTable.setStatus("current")
_ApnPortalRxOctetsEntry_Object = MibTableRow
apnPortalRxOctetsEntry = _ApnPortalRxOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1)
)
apnPortalRxOctetsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    apnPortalRxOctetsEntry.setStatus("current")
_ApnPortalRxOctetsAt1Mb_Type = Counter32
_ApnPortalRxOctetsAt1Mb_Object = MibTableColumn
apnPortalRxOctetsAt1Mb = _ApnPortalRxOctetsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 1),
    _ApnPortalRxOctetsAt1Mb_Type()
)
apnPortalRxOctetsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAt1Mb.setStatus("current")
_ApnPortalRxOctetsAt2Mb_Type = Counter32
_ApnPortalRxOctetsAt2Mb_Object = MibTableColumn
apnPortalRxOctetsAt2Mb = _ApnPortalRxOctetsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 2),
    _ApnPortalRxOctetsAt2Mb_Type()
)
apnPortalRxOctetsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAt2Mb.setStatus("current")
_ApnPortalRxOctetsAt5pt5Mb_Type = Counter32
_ApnPortalRxOctetsAt5pt5Mb_Object = MibTableColumn
apnPortalRxOctetsAt5pt5Mb = _ApnPortalRxOctetsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 3),
    _ApnPortalRxOctetsAt5pt5Mb_Type()
)
apnPortalRxOctetsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAt5pt5Mb.setStatus("current")
_ApnPortalRxOctetsAt6Mb_Type = Counter32
_ApnPortalRxOctetsAt6Mb_Object = MibTableColumn
apnPortalRxOctetsAt6Mb = _ApnPortalRxOctetsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 4),
    _ApnPortalRxOctetsAt6Mb_Type()
)
apnPortalRxOctetsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAt6Mb.setStatus("current")
_ApnPortalRxOctetsAt9Mb_Type = Counter32
_ApnPortalRxOctetsAt9Mb_Object = MibTableColumn
apnPortalRxOctetsAt9Mb = _ApnPortalRxOctetsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 5),
    _ApnPortalRxOctetsAt9Mb_Type()
)
apnPortalRxOctetsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAt9Mb.setStatus("current")
_ApnPortalRxOctetsAt11Mb_Type = Counter32
_ApnPortalRxOctetsAt11Mb_Object = MibTableColumn
apnPortalRxOctetsAt11Mb = _ApnPortalRxOctetsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 6),
    _ApnPortalRxOctetsAt11Mb_Type()
)
apnPortalRxOctetsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAt11Mb.setStatus("current")
_ApnPortalRxOctetsAt12Mb_Type = Counter32
_ApnPortalRxOctetsAt12Mb_Object = MibTableColumn
apnPortalRxOctetsAt12Mb = _ApnPortalRxOctetsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 7),
    _ApnPortalRxOctetsAt12Mb_Type()
)
apnPortalRxOctetsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAt12Mb.setStatus("current")
_ApnPortalRxOctetsAt18Mb_Type = Counter32
_ApnPortalRxOctetsAt18Mb_Object = MibTableColumn
apnPortalRxOctetsAt18Mb = _ApnPortalRxOctetsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 8),
    _ApnPortalRxOctetsAt18Mb_Type()
)
apnPortalRxOctetsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAt18Mb.setStatus("current")
_ApnPortalRxOctetsAt24Mb_Type = Counter32
_ApnPortalRxOctetsAt24Mb_Object = MibTableColumn
apnPortalRxOctetsAt24Mb = _ApnPortalRxOctetsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 9),
    _ApnPortalRxOctetsAt24Mb_Type()
)
apnPortalRxOctetsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAt24Mb.setStatus("current")
_ApnPortalRxOctetsAt36Mb_Type = Counter32
_ApnPortalRxOctetsAt36Mb_Object = MibTableColumn
apnPortalRxOctetsAt36Mb = _ApnPortalRxOctetsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 10),
    _ApnPortalRxOctetsAt36Mb_Type()
)
apnPortalRxOctetsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAt36Mb.setStatus("current")
_ApnPortalRxOctetsAt48Mb_Type = Counter32
_ApnPortalRxOctetsAt48Mb_Object = MibTableColumn
apnPortalRxOctetsAt48Mb = _ApnPortalRxOctetsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 11),
    _ApnPortalRxOctetsAt48Mb_Type()
)
apnPortalRxOctetsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAt48Mb.setStatus("current")
_ApnPortalRxOctetsAt54Mb_Type = Counter32
_ApnPortalRxOctetsAt54Mb_Object = MibTableColumn
apnPortalRxOctetsAt54Mb = _ApnPortalRxOctetsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 12),
    _ApnPortalRxOctetsAt54Mb_Type()
)
apnPortalRxOctetsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAt54Mb.setStatus("current")
_ApnPortalRxOctetsAtMCS0_Type = Counter32
_ApnPortalRxOctetsAtMCS0_Object = MibTableColumn
apnPortalRxOctetsAtMCS0 = _ApnPortalRxOctetsAtMCS0_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 13),
    _ApnPortalRxOctetsAtMCS0_Type()
)
apnPortalRxOctetsAtMCS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAtMCS0.setStatus("current")
_ApnPortalRxOctetsAtMCS1_Type = Counter32
_ApnPortalRxOctetsAtMCS1_Object = MibTableColumn
apnPortalRxOctetsAtMCS1 = _ApnPortalRxOctetsAtMCS1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 14),
    _ApnPortalRxOctetsAtMCS1_Type()
)
apnPortalRxOctetsAtMCS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAtMCS1.setStatus("current")
_ApnPortalRxOctetsAtMCS2_Type = Counter32
_ApnPortalRxOctetsAtMCS2_Object = MibTableColumn
apnPortalRxOctetsAtMCS2 = _ApnPortalRxOctetsAtMCS2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 15),
    _ApnPortalRxOctetsAtMCS2_Type()
)
apnPortalRxOctetsAtMCS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAtMCS2.setStatus("current")
_ApnPortalRxOctetsAtMCS3_Type = Counter32
_ApnPortalRxOctetsAtMCS3_Object = MibTableColumn
apnPortalRxOctetsAtMCS3 = _ApnPortalRxOctetsAtMCS3_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 16),
    _ApnPortalRxOctetsAtMCS3_Type()
)
apnPortalRxOctetsAtMCS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAtMCS3.setStatus("current")
_ApnPortalRxOctetsAtMCS4_Type = Counter32
_ApnPortalRxOctetsAtMCS4_Object = MibTableColumn
apnPortalRxOctetsAtMCS4 = _ApnPortalRxOctetsAtMCS4_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 17),
    _ApnPortalRxOctetsAtMCS4_Type()
)
apnPortalRxOctetsAtMCS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAtMCS4.setStatus("current")
_ApnPortalRxOctetsAtMCS5_Type = Counter32
_ApnPortalRxOctetsAtMCS5_Object = MibTableColumn
apnPortalRxOctetsAtMCS5 = _ApnPortalRxOctetsAtMCS5_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 18),
    _ApnPortalRxOctetsAtMCS5_Type()
)
apnPortalRxOctetsAtMCS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAtMCS5.setStatus("current")
_ApnPortalRxOctetsAtMCS6_Type = Counter32
_ApnPortalRxOctetsAtMCS6_Object = MibTableColumn
apnPortalRxOctetsAtMCS6 = _ApnPortalRxOctetsAtMCS6_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 19),
    _ApnPortalRxOctetsAtMCS6_Type()
)
apnPortalRxOctetsAtMCS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAtMCS6.setStatus("current")
_ApnPortalRxOctetsAtMCS7_Type = Counter32
_ApnPortalRxOctetsAtMCS7_Object = MibTableColumn
apnPortalRxOctetsAtMCS7 = _ApnPortalRxOctetsAtMCS7_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 20),
    _ApnPortalRxOctetsAtMCS7_Type()
)
apnPortalRxOctetsAtMCS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAtMCS7.setStatus("current")
_ApnPortalRxOctetsAtMCS8_Type = Counter32
_ApnPortalRxOctetsAtMCS8_Object = MibTableColumn
apnPortalRxOctetsAtMCS8 = _ApnPortalRxOctetsAtMCS8_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 21),
    _ApnPortalRxOctetsAtMCS8_Type()
)
apnPortalRxOctetsAtMCS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAtMCS8.setStatus("current")
_ApnPortalRxOctetsAtMCS9_Type = Counter32
_ApnPortalRxOctetsAtMCS9_Object = MibTableColumn
apnPortalRxOctetsAtMCS9 = _ApnPortalRxOctetsAtMCS9_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 22),
    _ApnPortalRxOctetsAtMCS9_Type()
)
apnPortalRxOctetsAtMCS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAtMCS9.setStatus("current")
_ApnPortalRxOctetsAtMCS10_Type = Counter32
_ApnPortalRxOctetsAtMCS10_Object = MibTableColumn
apnPortalRxOctetsAtMCS10 = _ApnPortalRxOctetsAtMCS10_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 23),
    _ApnPortalRxOctetsAtMCS10_Type()
)
apnPortalRxOctetsAtMCS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAtMCS10.setStatus("current")
_ApnPortalRxOctetsAtMCS11_Type = Counter32
_ApnPortalRxOctetsAtMCS11_Object = MibTableColumn
apnPortalRxOctetsAtMCS11 = _ApnPortalRxOctetsAtMCS11_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 24),
    _ApnPortalRxOctetsAtMCS11_Type()
)
apnPortalRxOctetsAtMCS11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAtMCS11.setStatus("current")
_ApnPortalRxOctetsAtMCS12_Type = Counter32
_ApnPortalRxOctetsAtMCS12_Object = MibTableColumn
apnPortalRxOctetsAtMCS12 = _ApnPortalRxOctetsAtMCS12_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 25),
    _ApnPortalRxOctetsAtMCS12_Type()
)
apnPortalRxOctetsAtMCS12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAtMCS12.setStatus("current")
_ApnPortalRxOctetsAtMCS13_Type = Counter32
_ApnPortalRxOctetsAtMCS13_Object = MibTableColumn
apnPortalRxOctetsAtMCS13 = _ApnPortalRxOctetsAtMCS13_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 26),
    _ApnPortalRxOctetsAtMCS13_Type()
)
apnPortalRxOctetsAtMCS13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAtMCS13.setStatus("current")
_ApnPortalRxOctetsAtMCS14_Type = Counter32
_ApnPortalRxOctetsAtMCS14_Object = MibTableColumn
apnPortalRxOctetsAtMCS14 = _ApnPortalRxOctetsAtMCS14_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 27),
    _ApnPortalRxOctetsAtMCS14_Type()
)
apnPortalRxOctetsAtMCS14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAtMCS14.setStatus("current")
_ApnPortalRxOctetsAtMCS15_Type = Counter32
_ApnPortalRxOctetsAtMCS15_Object = MibTableColumn
apnPortalRxOctetsAtMCS15 = _ApnPortalRxOctetsAtMCS15_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 4, 1, 28),
    _ApnPortalRxOctetsAtMCS15_Type()
)
apnPortalRxOctetsAtMCS15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalRxOctetsAtMCS15.setStatus("current")
_ApnPortalTxOctetsTable_Object = MibTable
apnPortalTxOctetsTable = _ApnPortalTxOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5)
)
if mibBuilder.loadTexts:
    apnPortalTxOctetsTable.setStatus("current")
_ApnPortalTxOctetsEntry_Object = MibTableRow
apnPortalTxOctetsEntry = _ApnPortalTxOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1)
)
apnPortalTxOctetsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    apnPortalTxOctetsEntry.setStatus("current")
_ApnPortalTxOctetsAt1Mb_Type = Counter32
_ApnPortalTxOctetsAt1Mb_Object = MibTableColumn
apnPortalTxOctetsAt1Mb = _ApnPortalTxOctetsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 2),
    _ApnPortalTxOctetsAt1Mb_Type()
)
apnPortalTxOctetsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAt1Mb.setStatus("current")
_ApnPortalTxOctetsAt2Mb_Type = Counter32
_ApnPortalTxOctetsAt2Mb_Object = MibTableColumn
apnPortalTxOctetsAt2Mb = _ApnPortalTxOctetsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 3),
    _ApnPortalTxOctetsAt2Mb_Type()
)
apnPortalTxOctetsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAt2Mb.setStatus("current")
_ApnPortalTxOctetsAt5pt5Mb_Type = Counter32
_ApnPortalTxOctetsAt5pt5Mb_Object = MibTableColumn
apnPortalTxOctetsAt5pt5Mb = _ApnPortalTxOctetsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 4),
    _ApnPortalTxOctetsAt5pt5Mb_Type()
)
apnPortalTxOctetsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAt5pt5Mb.setStatus("current")
_ApnPortalTxOctetsAt6Mb_Type = Counter32
_ApnPortalTxOctetsAt6Mb_Object = MibTableColumn
apnPortalTxOctetsAt6Mb = _ApnPortalTxOctetsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 5),
    _ApnPortalTxOctetsAt6Mb_Type()
)
apnPortalTxOctetsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAt6Mb.setStatus("current")
_ApnPortalTxOctetsAt9Mb_Type = Counter32
_ApnPortalTxOctetsAt9Mb_Object = MibTableColumn
apnPortalTxOctetsAt9Mb = _ApnPortalTxOctetsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 6),
    _ApnPortalTxOctetsAt9Mb_Type()
)
apnPortalTxOctetsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAt9Mb.setStatus("current")
_ApnPortalTxOctetsAt11Mb_Type = Counter32
_ApnPortalTxOctetsAt11Mb_Object = MibTableColumn
apnPortalTxOctetsAt11Mb = _ApnPortalTxOctetsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 7),
    _ApnPortalTxOctetsAt11Mb_Type()
)
apnPortalTxOctetsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAt11Mb.setStatus("current")
_ApnPortalTxOctetsAt12Mb_Type = Counter32
_ApnPortalTxOctetsAt12Mb_Object = MibTableColumn
apnPortalTxOctetsAt12Mb = _ApnPortalTxOctetsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 8),
    _ApnPortalTxOctetsAt12Mb_Type()
)
apnPortalTxOctetsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAt12Mb.setStatus("current")
_ApnPortalTxOctetsAt18Mb_Type = Counter32
_ApnPortalTxOctetsAt18Mb_Object = MibTableColumn
apnPortalTxOctetsAt18Mb = _ApnPortalTxOctetsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 9),
    _ApnPortalTxOctetsAt18Mb_Type()
)
apnPortalTxOctetsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAt18Mb.setStatus("current")
_ApnPortalTxOctetsAt24Mb_Type = Counter32
_ApnPortalTxOctetsAt24Mb_Object = MibTableColumn
apnPortalTxOctetsAt24Mb = _ApnPortalTxOctetsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 10),
    _ApnPortalTxOctetsAt24Mb_Type()
)
apnPortalTxOctetsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAt24Mb.setStatus("current")
_ApnPortalTxOctetsAt36Mb_Type = Counter32
_ApnPortalTxOctetsAt36Mb_Object = MibTableColumn
apnPortalTxOctetsAt36Mb = _ApnPortalTxOctetsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 11),
    _ApnPortalTxOctetsAt36Mb_Type()
)
apnPortalTxOctetsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAt36Mb.setStatus("current")
_ApnPortalTxOctetsAt48Mb_Type = Counter32
_ApnPortalTxOctetsAt48Mb_Object = MibTableColumn
apnPortalTxOctetsAt48Mb = _ApnPortalTxOctetsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 12),
    _ApnPortalTxOctetsAt48Mb_Type()
)
apnPortalTxOctetsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAt48Mb.setStatus("current")
_ApnPortalTxOctetsAt54Mb_Type = Counter32
_ApnPortalTxOctetsAt54Mb_Object = MibTableColumn
apnPortalTxOctetsAt54Mb = _ApnPortalTxOctetsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 13),
    _ApnPortalTxOctetsAt54Mb_Type()
)
apnPortalTxOctetsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAt54Mb.setStatus("current")
_ApnPortalTxOctetsAtMCS0_Type = Counter32
_ApnPortalTxOctetsAtMCS0_Object = MibTableColumn
apnPortalTxOctetsAtMCS0 = _ApnPortalTxOctetsAtMCS0_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 14),
    _ApnPortalTxOctetsAtMCS0_Type()
)
apnPortalTxOctetsAtMCS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAtMCS0.setStatus("current")
_ApnPortalTxOctetsAtMCS1_Type = Counter32
_ApnPortalTxOctetsAtMCS1_Object = MibTableColumn
apnPortalTxOctetsAtMCS1 = _ApnPortalTxOctetsAtMCS1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 15),
    _ApnPortalTxOctetsAtMCS1_Type()
)
apnPortalTxOctetsAtMCS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAtMCS1.setStatus("current")
_ApnPortalTxOctetsAtMCS2_Type = Counter32
_ApnPortalTxOctetsAtMCS2_Object = MibTableColumn
apnPortalTxOctetsAtMCS2 = _ApnPortalTxOctetsAtMCS2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 16),
    _ApnPortalTxOctetsAtMCS2_Type()
)
apnPortalTxOctetsAtMCS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAtMCS2.setStatus("current")
_ApnPortalTxOctetsAtMCS3_Type = Counter32
_ApnPortalTxOctetsAtMCS3_Object = MibTableColumn
apnPortalTxOctetsAtMCS3 = _ApnPortalTxOctetsAtMCS3_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 17),
    _ApnPortalTxOctetsAtMCS3_Type()
)
apnPortalTxOctetsAtMCS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAtMCS3.setStatus("current")
_ApnPortalTxOctetsAtMCS4_Type = Counter32
_ApnPortalTxOctetsAtMCS4_Object = MibTableColumn
apnPortalTxOctetsAtMCS4 = _ApnPortalTxOctetsAtMCS4_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 18),
    _ApnPortalTxOctetsAtMCS4_Type()
)
apnPortalTxOctetsAtMCS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAtMCS4.setStatus("current")
_ApnPortalTxOctetsAtMCS5_Type = Counter32
_ApnPortalTxOctetsAtMCS5_Object = MibTableColumn
apnPortalTxOctetsAtMCS5 = _ApnPortalTxOctetsAtMCS5_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 19),
    _ApnPortalTxOctetsAtMCS5_Type()
)
apnPortalTxOctetsAtMCS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAtMCS5.setStatus("current")
_ApnPortalTxOctetsAtMCS6_Type = Counter32
_ApnPortalTxOctetsAtMCS6_Object = MibTableColumn
apnPortalTxOctetsAtMCS6 = _ApnPortalTxOctetsAtMCS6_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 20),
    _ApnPortalTxOctetsAtMCS6_Type()
)
apnPortalTxOctetsAtMCS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAtMCS6.setStatus("current")
_ApnPortalTxOctetsAtMCS7_Type = Counter32
_ApnPortalTxOctetsAtMCS7_Object = MibTableColumn
apnPortalTxOctetsAtMCS7 = _ApnPortalTxOctetsAtMCS7_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 21),
    _ApnPortalTxOctetsAtMCS7_Type()
)
apnPortalTxOctetsAtMCS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAtMCS7.setStatus("current")
_ApnPortalTxOctetsAtMCS8_Type = Counter32
_ApnPortalTxOctetsAtMCS8_Object = MibTableColumn
apnPortalTxOctetsAtMCS8 = _ApnPortalTxOctetsAtMCS8_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 22),
    _ApnPortalTxOctetsAtMCS8_Type()
)
apnPortalTxOctetsAtMCS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAtMCS8.setStatus("current")
_ApnPortalTxOctetsAtMCS9_Type = Counter32
_ApnPortalTxOctetsAtMCS9_Object = MibTableColumn
apnPortalTxOctetsAtMCS9 = _ApnPortalTxOctetsAtMCS9_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 23),
    _ApnPortalTxOctetsAtMCS9_Type()
)
apnPortalTxOctetsAtMCS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAtMCS9.setStatus("current")
_ApnPortalTxOctetsAtMCS10_Type = Counter32
_ApnPortalTxOctetsAtMCS10_Object = MibTableColumn
apnPortalTxOctetsAtMCS10 = _ApnPortalTxOctetsAtMCS10_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 24),
    _ApnPortalTxOctetsAtMCS10_Type()
)
apnPortalTxOctetsAtMCS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAtMCS10.setStatus("current")
_ApnPortalTxOctetsAtMCS11_Type = Counter32
_ApnPortalTxOctetsAtMCS11_Object = MibTableColumn
apnPortalTxOctetsAtMCS11 = _ApnPortalTxOctetsAtMCS11_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 25),
    _ApnPortalTxOctetsAtMCS11_Type()
)
apnPortalTxOctetsAtMCS11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAtMCS11.setStatus("current")
_ApnPortalTxOctetsAtMCS12_Type = Counter32
_ApnPortalTxOctetsAtMCS12_Object = MibTableColumn
apnPortalTxOctetsAtMCS12 = _ApnPortalTxOctetsAtMCS12_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 26),
    _ApnPortalTxOctetsAtMCS12_Type()
)
apnPortalTxOctetsAtMCS12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAtMCS12.setStatus("current")
_ApnPortalTxOctetsAtMCS13_Type = Counter32
_ApnPortalTxOctetsAtMCS13_Object = MibTableColumn
apnPortalTxOctetsAtMCS13 = _ApnPortalTxOctetsAtMCS13_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 27),
    _ApnPortalTxOctetsAtMCS13_Type()
)
apnPortalTxOctetsAtMCS13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAtMCS13.setStatus("current")
_ApnPortalTxOctetsAtMCS14_Type = Counter32
_ApnPortalTxOctetsAtMCS14_Object = MibTableColumn
apnPortalTxOctetsAtMCS14 = _ApnPortalTxOctetsAtMCS14_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 28),
    _ApnPortalTxOctetsAtMCS14_Type()
)
apnPortalTxOctetsAtMCS14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAtMCS14.setStatus("current")
_ApnPortalTxOctetsAtMCS15_Type = Counter32
_ApnPortalTxOctetsAtMCS15_Object = MibTableColumn
apnPortalTxOctetsAtMCS15 = _ApnPortalTxOctetsAtMCS15_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 5, 1, 29),
    _ApnPortalTxOctetsAtMCS15_Type()
)
apnPortalTxOctetsAtMCS15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnPortalTxOctetsAtMCS15.setStatus("current")
_ApnMuRxPktsTable_Object = MibTable
apnMuRxPktsTable = _ApnMuRxPktsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6)
)
if mibBuilder.loadTexts:
    apnMuRxPktsTable.setStatus("current")
_ApnMuRxPktsEntry_Object = MibTableRow
apnMuRxPktsEntry = _ApnMuRxPktsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1)
)
apnMuRxPktsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    apnMuRxPktsEntry.setStatus("current")
_ApnMuRxPktsAt1Mb_Type = Counter32
_ApnMuRxPktsAt1Mb_Object = MibTableColumn
apnMuRxPktsAt1Mb = _ApnMuRxPktsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 1),
    _ApnMuRxPktsAt1Mb_Type()
)
apnMuRxPktsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAt1Mb.setStatus("current")
_ApnMuRxPktsAt2Mb_Type = Counter32
_ApnMuRxPktsAt2Mb_Object = MibTableColumn
apnMuRxPktsAt2Mb = _ApnMuRxPktsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 2),
    _ApnMuRxPktsAt2Mb_Type()
)
apnMuRxPktsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAt2Mb.setStatus("current")
_ApnMuRxPktsAt5pt5Mb_Type = Counter32
_ApnMuRxPktsAt5pt5Mb_Object = MibTableColumn
apnMuRxPktsAt5pt5Mb = _ApnMuRxPktsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 3),
    _ApnMuRxPktsAt5pt5Mb_Type()
)
apnMuRxPktsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAt5pt5Mb.setStatus("current")
_ApnMuRxPktsAt6Mb_Type = Counter32
_ApnMuRxPktsAt6Mb_Object = MibTableColumn
apnMuRxPktsAt6Mb = _ApnMuRxPktsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 4),
    _ApnMuRxPktsAt6Mb_Type()
)
apnMuRxPktsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAt6Mb.setStatus("current")
_ApnMuRxPktsAt9Mb_Type = Counter32
_ApnMuRxPktsAt9Mb_Object = MibTableColumn
apnMuRxPktsAt9Mb = _ApnMuRxPktsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 5),
    _ApnMuRxPktsAt9Mb_Type()
)
apnMuRxPktsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAt9Mb.setStatus("current")
_ApnMuRxPktsAt11Mb_Type = Counter32
_ApnMuRxPktsAt11Mb_Object = MibTableColumn
apnMuRxPktsAt11Mb = _ApnMuRxPktsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 6),
    _ApnMuRxPktsAt11Mb_Type()
)
apnMuRxPktsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAt11Mb.setStatus("current")
_ApnMuRxPktsAt12Mb_Type = Counter32
_ApnMuRxPktsAt12Mb_Object = MibTableColumn
apnMuRxPktsAt12Mb = _ApnMuRxPktsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 7),
    _ApnMuRxPktsAt12Mb_Type()
)
apnMuRxPktsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAt12Mb.setStatus("current")
_ApnMuRxPktsAt18Mb_Type = Counter32
_ApnMuRxPktsAt18Mb_Object = MibTableColumn
apnMuRxPktsAt18Mb = _ApnMuRxPktsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 8),
    _ApnMuRxPktsAt18Mb_Type()
)
apnMuRxPktsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAt18Mb.setStatus("current")
_ApnMuRxPktsAt24Mb_Type = Counter32
_ApnMuRxPktsAt24Mb_Object = MibTableColumn
apnMuRxPktsAt24Mb = _ApnMuRxPktsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 9),
    _ApnMuRxPktsAt24Mb_Type()
)
apnMuRxPktsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAt24Mb.setStatus("current")
_ApnMuRxPktsAt36Mb_Type = Counter32
_ApnMuRxPktsAt36Mb_Object = MibTableColumn
apnMuRxPktsAt36Mb = _ApnMuRxPktsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 10),
    _ApnMuRxPktsAt36Mb_Type()
)
apnMuRxPktsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAt36Mb.setStatus("current")
_ApnMuRxPktsAt48Mb_Type = Counter32
_ApnMuRxPktsAt48Mb_Object = MibTableColumn
apnMuRxPktsAt48Mb = _ApnMuRxPktsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 11),
    _ApnMuRxPktsAt48Mb_Type()
)
apnMuRxPktsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAt48Mb.setStatus("current")
_ApnMuRxPktsAt54Mb_Type = Counter32
_ApnMuRxPktsAt54Mb_Object = MibTableColumn
apnMuRxPktsAt54Mb = _ApnMuRxPktsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 12),
    _ApnMuRxPktsAt54Mb_Type()
)
apnMuRxPktsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAt54Mb.setStatus("current")
_ApnMuRxPktsAtMCS0_Type = Counter32
_ApnMuRxPktsAtMCS0_Object = MibTableColumn
apnMuRxPktsAtMCS0 = _ApnMuRxPktsAtMCS0_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 13),
    _ApnMuRxPktsAtMCS0_Type()
)
apnMuRxPktsAtMCS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAtMCS0.setStatus("current")
_ApnMuRxPktsAtMCS1_Type = Counter32
_ApnMuRxPktsAtMCS1_Object = MibTableColumn
apnMuRxPktsAtMCS1 = _ApnMuRxPktsAtMCS1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 14),
    _ApnMuRxPktsAtMCS1_Type()
)
apnMuRxPktsAtMCS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAtMCS1.setStatus("current")
_ApnMuRxPktsAtMCS2_Type = Counter32
_ApnMuRxPktsAtMCS2_Object = MibTableColumn
apnMuRxPktsAtMCS2 = _ApnMuRxPktsAtMCS2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 15),
    _ApnMuRxPktsAtMCS2_Type()
)
apnMuRxPktsAtMCS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAtMCS2.setStatus("current")
_ApnMuRxPktsAtMCS3_Type = Counter32
_ApnMuRxPktsAtMCS3_Object = MibTableColumn
apnMuRxPktsAtMCS3 = _ApnMuRxPktsAtMCS3_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 16),
    _ApnMuRxPktsAtMCS3_Type()
)
apnMuRxPktsAtMCS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAtMCS3.setStatus("current")
_ApnMuRxPktsAtMCS4_Type = Counter32
_ApnMuRxPktsAtMCS4_Object = MibTableColumn
apnMuRxPktsAtMCS4 = _ApnMuRxPktsAtMCS4_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 17),
    _ApnMuRxPktsAtMCS4_Type()
)
apnMuRxPktsAtMCS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAtMCS4.setStatus("current")
_ApnMuRxPktsAtMCS5_Type = Counter32
_ApnMuRxPktsAtMCS5_Object = MibTableColumn
apnMuRxPktsAtMCS5 = _ApnMuRxPktsAtMCS5_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 18),
    _ApnMuRxPktsAtMCS5_Type()
)
apnMuRxPktsAtMCS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAtMCS5.setStatus("current")
_ApnMuRxPktsAtMCS6_Type = Counter32
_ApnMuRxPktsAtMCS6_Object = MibTableColumn
apnMuRxPktsAtMCS6 = _ApnMuRxPktsAtMCS6_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 19),
    _ApnMuRxPktsAtMCS6_Type()
)
apnMuRxPktsAtMCS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAtMCS6.setStatus("current")
_ApnMuRxPktsAtMCS7_Type = Counter32
_ApnMuRxPktsAtMCS7_Object = MibTableColumn
apnMuRxPktsAtMCS7 = _ApnMuRxPktsAtMCS7_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 20),
    _ApnMuRxPktsAtMCS7_Type()
)
apnMuRxPktsAtMCS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAtMCS7.setStatus("current")
_ApnMuRxPktsAtMCS8_Type = Counter32
_ApnMuRxPktsAtMCS8_Object = MibTableColumn
apnMuRxPktsAtMCS8 = _ApnMuRxPktsAtMCS8_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 21),
    _ApnMuRxPktsAtMCS8_Type()
)
apnMuRxPktsAtMCS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAtMCS8.setStatus("current")
_ApnMuRxPktsAtMCS9_Type = Counter32
_ApnMuRxPktsAtMCS9_Object = MibTableColumn
apnMuRxPktsAtMCS9 = _ApnMuRxPktsAtMCS9_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 22),
    _ApnMuRxPktsAtMCS9_Type()
)
apnMuRxPktsAtMCS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAtMCS9.setStatus("current")
_ApnMuRxPktsAtMCS10_Type = Counter32
_ApnMuRxPktsAtMCS10_Object = MibTableColumn
apnMuRxPktsAtMCS10 = _ApnMuRxPktsAtMCS10_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 23),
    _ApnMuRxPktsAtMCS10_Type()
)
apnMuRxPktsAtMCS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAtMCS10.setStatus("current")
_ApnMuRxPktsAtMCS11_Type = Counter32
_ApnMuRxPktsAtMCS11_Object = MibTableColumn
apnMuRxPktsAtMCS11 = _ApnMuRxPktsAtMCS11_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 24),
    _ApnMuRxPktsAtMCS11_Type()
)
apnMuRxPktsAtMCS11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAtMCS11.setStatus("current")
_ApnMuRxPktsAtMCS12_Type = Counter32
_ApnMuRxPktsAtMCS12_Object = MibTableColumn
apnMuRxPktsAtMCS12 = _ApnMuRxPktsAtMCS12_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 25),
    _ApnMuRxPktsAtMCS12_Type()
)
apnMuRxPktsAtMCS12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAtMCS12.setStatus("current")
_ApnMuRxPktsAtMCS13_Type = Counter32
_ApnMuRxPktsAtMCS13_Object = MibTableColumn
apnMuRxPktsAtMCS13 = _ApnMuRxPktsAtMCS13_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 26),
    _ApnMuRxPktsAtMCS13_Type()
)
apnMuRxPktsAtMCS13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAtMCS13.setStatus("current")
_ApnMuRxPktsAtMCS14_Type = Counter32
_ApnMuRxPktsAtMCS14_Object = MibTableColumn
apnMuRxPktsAtMCS14 = _ApnMuRxPktsAtMCS14_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 27),
    _ApnMuRxPktsAtMCS14_Type()
)
apnMuRxPktsAtMCS14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAtMCS14.setStatus("current")
_ApnMuRxPktsAtMCS15_Type = Counter32
_ApnMuRxPktsAtMCS15_Object = MibTableColumn
apnMuRxPktsAtMCS15 = _ApnMuRxPktsAtMCS15_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 6, 1, 28),
    _ApnMuRxPktsAtMCS15_Type()
)
apnMuRxPktsAtMCS15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxPktsAtMCS15.setStatus("current")
_ApnMuTxPktsTable_Object = MibTable
apnMuTxPktsTable = _ApnMuTxPktsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7)
)
if mibBuilder.loadTexts:
    apnMuTxPktsTable.setStatus("current")
_ApnMuTxPktsEntry_Object = MibTableRow
apnMuTxPktsEntry = _ApnMuTxPktsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1)
)
apnMuTxPktsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    apnMuTxPktsEntry.setStatus("current")
_ApnMuTxPktsAt1Mb_Type = Counter32
_ApnMuTxPktsAt1Mb_Object = MibTableColumn
apnMuTxPktsAt1Mb = _ApnMuTxPktsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 1),
    _ApnMuTxPktsAt1Mb_Type()
)
apnMuTxPktsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAt1Mb.setStatus("current")
_ApnMuTxPktsAt2Mb_Type = Counter32
_ApnMuTxPktsAt2Mb_Object = MibTableColumn
apnMuTxPktsAt2Mb = _ApnMuTxPktsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 2),
    _ApnMuTxPktsAt2Mb_Type()
)
apnMuTxPktsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAt2Mb.setStatus("current")
_ApnMuTxPktsAt5pt5Mb_Type = Counter32
_ApnMuTxPktsAt5pt5Mb_Object = MibTableColumn
apnMuTxPktsAt5pt5Mb = _ApnMuTxPktsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 3),
    _ApnMuTxPktsAt5pt5Mb_Type()
)
apnMuTxPktsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAt5pt5Mb.setStatus("current")
_ApnMuTxPktsAt6Mb_Type = Counter32
_ApnMuTxPktsAt6Mb_Object = MibTableColumn
apnMuTxPktsAt6Mb = _ApnMuTxPktsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 4),
    _ApnMuTxPktsAt6Mb_Type()
)
apnMuTxPktsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAt6Mb.setStatus("current")
_ApnMuTxPktsAt9Mb_Type = Counter32
_ApnMuTxPktsAt9Mb_Object = MibTableColumn
apnMuTxPktsAt9Mb = _ApnMuTxPktsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 5),
    _ApnMuTxPktsAt9Mb_Type()
)
apnMuTxPktsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAt9Mb.setStatus("current")
_ApnMuTxPktsAt11Mb_Type = Counter32
_ApnMuTxPktsAt11Mb_Object = MibTableColumn
apnMuTxPktsAt11Mb = _ApnMuTxPktsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 6),
    _ApnMuTxPktsAt11Mb_Type()
)
apnMuTxPktsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAt11Mb.setStatus("current")
_ApnMuTxPktsAt12Mb_Type = Counter32
_ApnMuTxPktsAt12Mb_Object = MibTableColumn
apnMuTxPktsAt12Mb = _ApnMuTxPktsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 7),
    _ApnMuTxPktsAt12Mb_Type()
)
apnMuTxPktsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAt12Mb.setStatus("current")
_ApnMuTxPktsAt18Mb_Type = Counter32
_ApnMuTxPktsAt18Mb_Object = MibTableColumn
apnMuTxPktsAt18Mb = _ApnMuTxPktsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 8),
    _ApnMuTxPktsAt18Mb_Type()
)
apnMuTxPktsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAt18Mb.setStatus("current")
_ApnMuTxPktsAt24Mb_Type = Counter32
_ApnMuTxPktsAt24Mb_Object = MibTableColumn
apnMuTxPktsAt24Mb = _ApnMuTxPktsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 9),
    _ApnMuTxPktsAt24Mb_Type()
)
apnMuTxPktsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAt24Mb.setStatus("current")
_ApnMuTxPktsAt36Mb_Type = Counter32
_ApnMuTxPktsAt36Mb_Object = MibTableColumn
apnMuTxPktsAt36Mb = _ApnMuTxPktsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 10),
    _ApnMuTxPktsAt36Mb_Type()
)
apnMuTxPktsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAt36Mb.setStatus("current")
_ApnMuTxPktsAt48Mb_Type = Counter32
_ApnMuTxPktsAt48Mb_Object = MibTableColumn
apnMuTxPktsAt48Mb = _ApnMuTxPktsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 11),
    _ApnMuTxPktsAt48Mb_Type()
)
apnMuTxPktsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAt48Mb.setStatus("current")
_ApnMuTxPktsAt54Mb_Type = Counter32
_ApnMuTxPktsAt54Mb_Object = MibTableColumn
apnMuTxPktsAt54Mb = _ApnMuTxPktsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 12),
    _ApnMuTxPktsAt54Mb_Type()
)
apnMuTxPktsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAt54Mb.setStatus("current")
_ApnMuTxPktsAtMCS0_Type = Counter32
_ApnMuTxPktsAtMCS0_Object = MibTableColumn
apnMuTxPktsAtMCS0 = _ApnMuTxPktsAtMCS0_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 13),
    _ApnMuTxPktsAtMCS0_Type()
)
apnMuTxPktsAtMCS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAtMCS0.setStatus("current")
_ApnMuTxPktsAtMCS1_Type = Counter32
_ApnMuTxPktsAtMCS1_Object = MibTableColumn
apnMuTxPktsAtMCS1 = _ApnMuTxPktsAtMCS1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 14),
    _ApnMuTxPktsAtMCS1_Type()
)
apnMuTxPktsAtMCS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAtMCS1.setStatus("current")
_ApnMuTxPktsAtMCS2_Type = Counter32
_ApnMuTxPktsAtMCS2_Object = MibTableColumn
apnMuTxPktsAtMCS2 = _ApnMuTxPktsAtMCS2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 15),
    _ApnMuTxPktsAtMCS2_Type()
)
apnMuTxPktsAtMCS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAtMCS2.setStatus("current")
_ApnMuTxPktsAtMCS3_Type = Counter32
_ApnMuTxPktsAtMCS3_Object = MibTableColumn
apnMuTxPktsAtMCS3 = _ApnMuTxPktsAtMCS3_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 16),
    _ApnMuTxPktsAtMCS3_Type()
)
apnMuTxPktsAtMCS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAtMCS3.setStatus("current")
_ApnMuTxPktsAtMCS4_Type = Counter32
_ApnMuTxPktsAtMCS4_Object = MibTableColumn
apnMuTxPktsAtMCS4 = _ApnMuTxPktsAtMCS4_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 17),
    _ApnMuTxPktsAtMCS4_Type()
)
apnMuTxPktsAtMCS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAtMCS4.setStatus("current")
_ApnMuTxPktsAtMCS5_Type = Counter32
_ApnMuTxPktsAtMCS5_Object = MibTableColumn
apnMuTxPktsAtMCS5 = _ApnMuTxPktsAtMCS5_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 18),
    _ApnMuTxPktsAtMCS5_Type()
)
apnMuTxPktsAtMCS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAtMCS5.setStatus("current")
_ApnMuTxPktsAtMCS6_Type = Counter32
_ApnMuTxPktsAtMCS6_Object = MibTableColumn
apnMuTxPktsAtMCS6 = _ApnMuTxPktsAtMCS6_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 19),
    _ApnMuTxPktsAtMCS6_Type()
)
apnMuTxPktsAtMCS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAtMCS6.setStatus("current")
_ApnMuTxPktsAtMCS7_Type = Counter32
_ApnMuTxPktsAtMCS7_Object = MibTableColumn
apnMuTxPktsAtMCS7 = _ApnMuTxPktsAtMCS7_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 20),
    _ApnMuTxPktsAtMCS7_Type()
)
apnMuTxPktsAtMCS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAtMCS7.setStatus("current")
_ApnMuTxPktsAtMCS8_Type = Counter32
_ApnMuTxPktsAtMCS8_Object = MibTableColumn
apnMuTxPktsAtMCS8 = _ApnMuTxPktsAtMCS8_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 21),
    _ApnMuTxPktsAtMCS8_Type()
)
apnMuTxPktsAtMCS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAtMCS8.setStatus("current")
_ApnMuTxPktsAtMCS9_Type = Counter32
_ApnMuTxPktsAtMCS9_Object = MibTableColumn
apnMuTxPktsAtMCS9 = _ApnMuTxPktsAtMCS9_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 22),
    _ApnMuTxPktsAtMCS9_Type()
)
apnMuTxPktsAtMCS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAtMCS9.setStatus("current")
_ApnMuTxPktsAtMCS10_Type = Counter32
_ApnMuTxPktsAtMCS10_Object = MibTableColumn
apnMuTxPktsAtMCS10 = _ApnMuTxPktsAtMCS10_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 23),
    _ApnMuTxPktsAtMCS10_Type()
)
apnMuTxPktsAtMCS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAtMCS10.setStatus("current")
_ApnMuTxPktsAtMCS11_Type = Counter32
_ApnMuTxPktsAtMCS11_Object = MibTableColumn
apnMuTxPktsAtMCS11 = _ApnMuTxPktsAtMCS11_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 24),
    _ApnMuTxPktsAtMCS11_Type()
)
apnMuTxPktsAtMCS11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAtMCS11.setStatus("current")
_ApnMuTxPktsAtMCS12_Type = Counter32
_ApnMuTxPktsAtMCS12_Object = MibTableColumn
apnMuTxPktsAtMCS12 = _ApnMuTxPktsAtMCS12_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 25),
    _ApnMuTxPktsAtMCS12_Type()
)
apnMuTxPktsAtMCS12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAtMCS12.setStatus("current")
_ApnMuTxPktsAtMCS13_Type = Counter32
_ApnMuTxPktsAtMCS13_Object = MibTableColumn
apnMuTxPktsAtMCS13 = _ApnMuTxPktsAtMCS13_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 26),
    _ApnMuTxPktsAtMCS13_Type()
)
apnMuTxPktsAtMCS13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAtMCS13.setStatus("current")
_ApnMuTxPktsAtMCS14_Type = Counter32
_ApnMuTxPktsAtMCS14_Object = MibTableColumn
apnMuTxPktsAtMCS14 = _ApnMuTxPktsAtMCS14_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 27),
    _ApnMuTxPktsAtMCS14_Type()
)
apnMuTxPktsAtMCS14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAtMCS14.setStatus("current")
_ApnMuTxPktsAtMCS15_Type = Counter32
_ApnMuTxPktsAtMCS15_Object = MibTableColumn
apnMuTxPktsAtMCS15 = _ApnMuTxPktsAtMCS15_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 7, 1, 28),
    _ApnMuTxPktsAtMCS15_Type()
)
apnMuTxPktsAtMCS15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxPktsAtMCS15.setStatus("current")
_ApnMuRxOctetsTable_Object = MibTable
apnMuRxOctetsTable = _ApnMuRxOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8)
)
if mibBuilder.loadTexts:
    apnMuRxOctetsTable.setStatus("current")
_ApnMuRxOctetsEntry_Object = MibTableRow
apnMuRxOctetsEntry = _ApnMuRxOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1)
)
apnMuRxOctetsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    apnMuRxOctetsEntry.setStatus("current")
_ApnMuRxOctetsAt1Mb_Type = Counter32
_ApnMuRxOctetsAt1Mb_Object = MibTableColumn
apnMuRxOctetsAt1Mb = _ApnMuRxOctetsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 1),
    _ApnMuRxOctetsAt1Mb_Type()
)
apnMuRxOctetsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAt1Mb.setStatus("current")
_ApnMuRxOctetsAt2Mb_Type = Counter32
_ApnMuRxOctetsAt2Mb_Object = MibTableColumn
apnMuRxOctetsAt2Mb = _ApnMuRxOctetsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 2),
    _ApnMuRxOctetsAt2Mb_Type()
)
apnMuRxOctetsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAt2Mb.setStatus("current")
_ApnMuRxOctetsAt5pt5Mb_Type = Counter32
_ApnMuRxOctetsAt5pt5Mb_Object = MibTableColumn
apnMuRxOctetsAt5pt5Mb = _ApnMuRxOctetsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 3),
    _ApnMuRxOctetsAt5pt5Mb_Type()
)
apnMuRxOctetsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAt5pt5Mb.setStatus("current")
_ApnMuRxOctetsAt6Mb_Type = Counter32
_ApnMuRxOctetsAt6Mb_Object = MibTableColumn
apnMuRxOctetsAt6Mb = _ApnMuRxOctetsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 4),
    _ApnMuRxOctetsAt6Mb_Type()
)
apnMuRxOctetsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAt6Mb.setStatus("current")
_ApnMuRxOctetsAt9Mb_Type = Counter32
_ApnMuRxOctetsAt9Mb_Object = MibTableColumn
apnMuRxOctetsAt9Mb = _ApnMuRxOctetsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 5),
    _ApnMuRxOctetsAt9Mb_Type()
)
apnMuRxOctetsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAt9Mb.setStatus("current")
_ApnMuRxOctetsAt11Mb_Type = Counter32
_ApnMuRxOctetsAt11Mb_Object = MibTableColumn
apnMuRxOctetsAt11Mb = _ApnMuRxOctetsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 6),
    _ApnMuRxOctetsAt11Mb_Type()
)
apnMuRxOctetsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAt11Mb.setStatus("current")
_ApnMuRxOctetsAt12Mb_Type = Counter32
_ApnMuRxOctetsAt12Mb_Object = MibTableColumn
apnMuRxOctetsAt12Mb = _ApnMuRxOctetsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 7),
    _ApnMuRxOctetsAt12Mb_Type()
)
apnMuRxOctetsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAt12Mb.setStatus("current")
_ApnMuRxOctetsAt18Mb_Type = Counter32
_ApnMuRxOctetsAt18Mb_Object = MibTableColumn
apnMuRxOctetsAt18Mb = _ApnMuRxOctetsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 8),
    _ApnMuRxOctetsAt18Mb_Type()
)
apnMuRxOctetsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAt18Mb.setStatus("current")
_ApnMuRxOctetsAt24Mb_Type = Counter32
_ApnMuRxOctetsAt24Mb_Object = MibTableColumn
apnMuRxOctetsAt24Mb = _ApnMuRxOctetsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 9),
    _ApnMuRxOctetsAt24Mb_Type()
)
apnMuRxOctetsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAt24Mb.setStatus("current")
_ApnMuRxOctetsAt36Mb_Type = Counter32
_ApnMuRxOctetsAt36Mb_Object = MibTableColumn
apnMuRxOctetsAt36Mb = _ApnMuRxOctetsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 10),
    _ApnMuRxOctetsAt36Mb_Type()
)
apnMuRxOctetsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAt36Mb.setStatus("current")
_ApnMuRxOctetsAt48Mb_Type = Counter32
_ApnMuRxOctetsAt48Mb_Object = MibTableColumn
apnMuRxOctetsAt48Mb = _ApnMuRxOctetsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 11),
    _ApnMuRxOctetsAt48Mb_Type()
)
apnMuRxOctetsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAt48Mb.setStatus("current")
_ApnMuRxOctetsAt54Mb_Type = Counter32
_ApnMuRxOctetsAt54Mb_Object = MibTableColumn
apnMuRxOctetsAt54Mb = _ApnMuRxOctetsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 12),
    _ApnMuRxOctetsAt54Mb_Type()
)
apnMuRxOctetsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAt54Mb.setStatus("current")
_ApnMuRxOctetsAtMCS0_Type = Counter32
_ApnMuRxOctetsAtMCS0_Object = MibTableColumn
apnMuRxOctetsAtMCS0 = _ApnMuRxOctetsAtMCS0_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 13),
    _ApnMuRxOctetsAtMCS0_Type()
)
apnMuRxOctetsAtMCS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAtMCS0.setStatus("current")
_ApnMuRxOctetsAtMCS1_Type = Counter32
_ApnMuRxOctetsAtMCS1_Object = MibTableColumn
apnMuRxOctetsAtMCS1 = _ApnMuRxOctetsAtMCS1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 14),
    _ApnMuRxOctetsAtMCS1_Type()
)
apnMuRxOctetsAtMCS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAtMCS1.setStatus("current")
_ApnMuRxOctetsAtMCS2_Type = Counter32
_ApnMuRxOctetsAtMCS2_Object = MibTableColumn
apnMuRxOctetsAtMCS2 = _ApnMuRxOctetsAtMCS2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 15),
    _ApnMuRxOctetsAtMCS2_Type()
)
apnMuRxOctetsAtMCS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAtMCS2.setStatus("current")
_ApnMuRxOctetsAtMCS3_Type = Counter32
_ApnMuRxOctetsAtMCS3_Object = MibTableColumn
apnMuRxOctetsAtMCS3 = _ApnMuRxOctetsAtMCS3_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 16),
    _ApnMuRxOctetsAtMCS3_Type()
)
apnMuRxOctetsAtMCS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAtMCS3.setStatus("current")
_ApnMuRxOctetsAtMCS4_Type = Counter32
_ApnMuRxOctetsAtMCS4_Object = MibTableColumn
apnMuRxOctetsAtMCS4 = _ApnMuRxOctetsAtMCS4_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 17),
    _ApnMuRxOctetsAtMCS4_Type()
)
apnMuRxOctetsAtMCS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAtMCS4.setStatus("current")
_ApnMuRxOctetsAtMCS5_Type = Counter32
_ApnMuRxOctetsAtMCS5_Object = MibTableColumn
apnMuRxOctetsAtMCS5 = _ApnMuRxOctetsAtMCS5_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 18),
    _ApnMuRxOctetsAtMCS5_Type()
)
apnMuRxOctetsAtMCS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAtMCS5.setStatus("current")
_ApnMuRxOctetsAtMCS6_Type = Counter32
_ApnMuRxOctetsAtMCS6_Object = MibTableColumn
apnMuRxOctetsAtMCS6 = _ApnMuRxOctetsAtMCS6_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 19),
    _ApnMuRxOctetsAtMCS6_Type()
)
apnMuRxOctetsAtMCS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAtMCS6.setStatus("current")
_ApnMuRxOctetsAtMCS7_Type = Counter32
_ApnMuRxOctetsAtMCS7_Object = MibTableColumn
apnMuRxOctetsAtMCS7 = _ApnMuRxOctetsAtMCS7_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 20),
    _ApnMuRxOctetsAtMCS7_Type()
)
apnMuRxOctetsAtMCS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAtMCS7.setStatus("current")
_ApnMuRxOctetsAtMCS8_Type = Counter32
_ApnMuRxOctetsAtMCS8_Object = MibTableColumn
apnMuRxOctetsAtMCS8 = _ApnMuRxOctetsAtMCS8_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 21),
    _ApnMuRxOctetsAtMCS8_Type()
)
apnMuRxOctetsAtMCS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAtMCS8.setStatus("current")
_ApnMuRxOctetsAtMCS9_Type = Counter32
_ApnMuRxOctetsAtMCS9_Object = MibTableColumn
apnMuRxOctetsAtMCS9 = _ApnMuRxOctetsAtMCS9_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 22),
    _ApnMuRxOctetsAtMCS9_Type()
)
apnMuRxOctetsAtMCS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAtMCS9.setStatus("current")
_ApnMuRxOctetsAtMCS10_Type = Counter32
_ApnMuRxOctetsAtMCS10_Object = MibTableColumn
apnMuRxOctetsAtMCS10 = _ApnMuRxOctetsAtMCS10_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 23),
    _ApnMuRxOctetsAtMCS10_Type()
)
apnMuRxOctetsAtMCS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAtMCS10.setStatus("current")
_ApnMuRxOctetsAtMCS11_Type = Counter32
_ApnMuRxOctetsAtMCS11_Object = MibTableColumn
apnMuRxOctetsAtMCS11 = _ApnMuRxOctetsAtMCS11_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 24),
    _ApnMuRxOctetsAtMCS11_Type()
)
apnMuRxOctetsAtMCS11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAtMCS11.setStatus("current")
_ApnMuRxOctetsAtMCS12_Type = Counter32
_ApnMuRxOctetsAtMCS12_Object = MibTableColumn
apnMuRxOctetsAtMCS12 = _ApnMuRxOctetsAtMCS12_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 25),
    _ApnMuRxOctetsAtMCS12_Type()
)
apnMuRxOctetsAtMCS12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAtMCS12.setStatus("current")
_ApnMuRxOctetsAtMCS13_Type = Counter32
_ApnMuRxOctetsAtMCS13_Object = MibTableColumn
apnMuRxOctetsAtMCS13 = _ApnMuRxOctetsAtMCS13_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 26),
    _ApnMuRxOctetsAtMCS13_Type()
)
apnMuRxOctetsAtMCS13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAtMCS13.setStatus("current")
_ApnMuRxOctetsAtMCS14_Type = Counter32
_ApnMuRxOctetsAtMCS14_Object = MibTableColumn
apnMuRxOctetsAtMCS14 = _ApnMuRxOctetsAtMCS14_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 27),
    _ApnMuRxOctetsAtMCS14_Type()
)
apnMuRxOctetsAtMCS14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAtMCS14.setStatus("current")
_ApnMuRxOctetsAtMCS15_Type = Counter32
_ApnMuRxOctetsAtMCS15_Object = MibTableColumn
apnMuRxOctetsAtMCS15 = _ApnMuRxOctetsAtMCS15_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 8, 1, 28),
    _ApnMuRxOctetsAtMCS15_Type()
)
apnMuRxOctetsAtMCS15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuRxOctetsAtMCS15.setStatus("current")
_ApnMuTxOctetsTable_Object = MibTable
apnMuTxOctetsTable = _ApnMuTxOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9)
)
if mibBuilder.loadTexts:
    apnMuTxOctetsTable.setStatus("current")
_ApnMuTxOctetsEntry_Object = MibTableRow
apnMuTxOctetsEntry = _ApnMuTxOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1)
)
apnMuTxOctetsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    apnMuTxOctetsEntry.setStatus("current")
_ApnMuTxOctetsAt1Mb_Type = Counter32
_ApnMuTxOctetsAt1Mb_Object = MibTableColumn
apnMuTxOctetsAt1Mb = _ApnMuTxOctetsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 2),
    _ApnMuTxOctetsAt1Mb_Type()
)
apnMuTxOctetsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAt1Mb.setStatus("current")
_ApnMuTxOctetsAt2Mb_Type = Counter32
_ApnMuTxOctetsAt2Mb_Object = MibTableColumn
apnMuTxOctetsAt2Mb = _ApnMuTxOctetsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 3),
    _ApnMuTxOctetsAt2Mb_Type()
)
apnMuTxOctetsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAt2Mb.setStatus("current")
_ApnMuTxOctetsAt5pt5Mb_Type = Counter32
_ApnMuTxOctetsAt5pt5Mb_Object = MibTableColumn
apnMuTxOctetsAt5pt5Mb = _ApnMuTxOctetsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 4),
    _ApnMuTxOctetsAt5pt5Mb_Type()
)
apnMuTxOctetsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAt5pt5Mb.setStatus("current")
_ApnMuTxOctetsAt6Mb_Type = Counter32
_ApnMuTxOctetsAt6Mb_Object = MibTableColumn
apnMuTxOctetsAt6Mb = _ApnMuTxOctetsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 5),
    _ApnMuTxOctetsAt6Mb_Type()
)
apnMuTxOctetsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAt6Mb.setStatus("current")
_ApnMuTxOctetsAt9Mb_Type = Counter32
_ApnMuTxOctetsAt9Mb_Object = MibTableColumn
apnMuTxOctetsAt9Mb = _ApnMuTxOctetsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 6),
    _ApnMuTxOctetsAt9Mb_Type()
)
apnMuTxOctetsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAt9Mb.setStatus("current")
_ApnMuTxOctetsAt11Mb_Type = Counter32
_ApnMuTxOctetsAt11Mb_Object = MibTableColumn
apnMuTxOctetsAt11Mb = _ApnMuTxOctetsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 7),
    _ApnMuTxOctetsAt11Mb_Type()
)
apnMuTxOctetsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAt11Mb.setStatus("current")
_ApnMuTxOctetsAt12Mb_Type = Counter32
_ApnMuTxOctetsAt12Mb_Object = MibTableColumn
apnMuTxOctetsAt12Mb = _ApnMuTxOctetsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 8),
    _ApnMuTxOctetsAt12Mb_Type()
)
apnMuTxOctetsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAt12Mb.setStatus("current")
_ApnMuTxOctetsAt18Mb_Type = Counter32
_ApnMuTxOctetsAt18Mb_Object = MibTableColumn
apnMuTxOctetsAt18Mb = _ApnMuTxOctetsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 9),
    _ApnMuTxOctetsAt18Mb_Type()
)
apnMuTxOctetsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAt18Mb.setStatus("current")
_ApnMuTxOctetsAt24Mb_Type = Counter32
_ApnMuTxOctetsAt24Mb_Object = MibTableColumn
apnMuTxOctetsAt24Mb = _ApnMuTxOctetsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 10),
    _ApnMuTxOctetsAt24Mb_Type()
)
apnMuTxOctetsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAt24Mb.setStatus("current")
_ApnMuTxOctetsAt36Mb_Type = Counter32
_ApnMuTxOctetsAt36Mb_Object = MibTableColumn
apnMuTxOctetsAt36Mb = _ApnMuTxOctetsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 11),
    _ApnMuTxOctetsAt36Mb_Type()
)
apnMuTxOctetsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAt36Mb.setStatus("current")
_ApnMuTxOctetsAt48Mb_Type = Counter32
_ApnMuTxOctetsAt48Mb_Object = MibTableColumn
apnMuTxOctetsAt48Mb = _ApnMuTxOctetsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 12),
    _ApnMuTxOctetsAt48Mb_Type()
)
apnMuTxOctetsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAt48Mb.setStatus("current")
_ApnMuTxOctetsAt54Mb_Type = Counter32
_ApnMuTxOctetsAt54Mb_Object = MibTableColumn
apnMuTxOctetsAt54Mb = _ApnMuTxOctetsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 13),
    _ApnMuTxOctetsAt54Mb_Type()
)
apnMuTxOctetsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAt54Mb.setStatus("current")
_ApnMuTxOctetsAtMCS0_Type = Counter32
_ApnMuTxOctetsAtMCS0_Object = MibTableColumn
apnMuTxOctetsAtMCS0 = _ApnMuTxOctetsAtMCS0_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 14),
    _ApnMuTxOctetsAtMCS0_Type()
)
apnMuTxOctetsAtMCS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAtMCS0.setStatus("current")
_ApnMuTxOctetsAtMCS1_Type = Counter32
_ApnMuTxOctetsAtMCS1_Object = MibTableColumn
apnMuTxOctetsAtMCS1 = _ApnMuTxOctetsAtMCS1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 15),
    _ApnMuTxOctetsAtMCS1_Type()
)
apnMuTxOctetsAtMCS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAtMCS1.setStatus("current")
_ApnMuTxOctetsAtMCS2_Type = Counter32
_ApnMuTxOctetsAtMCS2_Object = MibTableColumn
apnMuTxOctetsAtMCS2 = _ApnMuTxOctetsAtMCS2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 16),
    _ApnMuTxOctetsAtMCS2_Type()
)
apnMuTxOctetsAtMCS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAtMCS2.setStatus("current")
_ApnMuTxOctetsAtMCS3_Type = Counter32
_ApnMuTxOctetsAtMCS3_Object = MibTableColumn
apnMuTxOctetsAtMCS3 = _ApnMuTxOctetsAtMCS3_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 17),
    _ApnMuTxOctetsAtMCS3_Type()
)
apnMuTxOctetsAtMCS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAtMCS3.setStatus("current")
_ApnMuTxOctetsAtMCS4_Type = Counter32
_ApnMuTxOctetsAtMCS4_Object = MibTableColumn
apnMuTxOctetsAtMCS4 = _ApnMuTxOctetsAtMCS4_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 18),
    _ApnMuTxOctetsAtMCS4_Type()
)
apnMuTxOctetsAtMCS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAtMCS4.setStatus("current")
_ApnMuTxOctetsAtMCS5_Type = Counter32
_ApnMuTxOctetsAtMCS5_Object = MibTableColumn
apnMuTxOctetsAtMCS5 = _ApnMuTxOctetsAtMCS5_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 19),
    _ApnMuTxOctetsAtMCS5_Type()
)
apnMuTxOctetsAtMCS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAtMCS5.setStatus("current")
_ApnMuTxOctetsAtMCS6_Type = Counter32
_ApnMuTxOctetsAtMCS6_Object = MibTableColumn
apnMuTxOctetsAtMCS6 = _ApnMuTxOctetsAtMCS6_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 20),
    _ApnMuTxOctetsAtMCS6_Type()
)
apnMuTxOctetsAtMCS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAtMCS6.setStatus("current")
_ApnMuTxOctetsAtMCS7_Type = Counter32
_ApnMuTxOctetsAtMCS7_Object = MibTableColumn
apnMuTxOctetsAtMCS7 = _ApnMuTxOctetsAtMCS7_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 21),
    _ApnMuTxOctetsAtMCS7_Type()
)
apnMuTxOctetsAtMCS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAtMCS7.setStatus("current")
_ApnMuTxOctetsAtMCS8_Type = Counter32
_ApnMuTxOctetsAtMCS8_Object = MibTableColumn
apnMuTxOctetsAtMCS8 = _ApnMuTxOctetsAtMCS8_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 22),
    _ApnMuTxOctetsAtMCS8_Type()
)
apnMuTxOctetsAtMCS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAtMCS8.setStatus("current")
_ApnMuTxOctetsAtMCS9_Type = Counter32
_ApnMuTxOctetsAtMCS9_Object = MibTableColumn
apnMuTxOctetsAtMCS9 = _ApnMuTxOctetsAtMCS9_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 23),
    _ApnMuTxOctetsAtMCS9_Type()
)
apnMuTxOctetsAtMCS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAtMCS9.setStatus("current")
_ApnMuTxOctetsAtMCS10_Type = Counter32
_ApnMuTxOctetsAtMCS10_Object = MibTableColumn
apnMuTxOctetsAtMCS10 = _ApnMuTxOctetsAtMCS10_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 24),
    _ApnMuTxOctetsAtMCS10_Type()
)
apnMuTxOctetsAtMCS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAtMCS10.setStatus("current")
_ApnMuTxOctetsAtMCS11_Type = Counter32
_ApnMuTxOctetsAtMCS11_Object = MibTableColumn
apnMuTxOctetsAtMCS11 = _ApnMuTxOctetsAtMCS11_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 25),
    _ApnMuTxOctetsAtMCS11_Type()
)
apnMuTxOctetsAtMCS11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAtMCS11.setStatus("current")
_ApnMuTxOctetsAtMCS12_Type = Counter32
_ApnMuTxOctetsAtMCS12_Object = MibTableColumn
apnMuTxOctetsAtMCS12 = _ApnMuTxOctetsAtMCS12_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 26),
    _ApnMuTxOctetsAtMCS12_Type()
)
apnMuTxOctetsAtMCS12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAtMCS12.setStatus("current")
_ApnMuTxOctetsAtMCS13_Type = Counter32
_ApnMuTxOctetsAtMCS13_Object = MibTableColumn
apnMuTxOctetsAtMCS13 = _ApnMuTxOctetsAtMCS13_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 27),
    _ApnMuTxOctetsAtMCS13_Type()
)
apnMuTxOctetsAtMCS13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAtMCS13.setStatus("current")
_ApnMuTxOctetsAtMCS14_Type = Counter32
_ApnMuTxOctetsAtMCS14_Object = MibTableColumn
apnMuTxOctetsAtMCS14 = _ApnMuTxOctetsAtMCS14_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 28),
    _ApnMuTxOctetsAtMCS14_Type()
)
apnMuTxOctetsAtMCS14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAtMCS14.setStatus("current")
_ApnMuTxOctetsAtMCS15_Type = Counter32
_ApnMuTxOctetsAtMCS15_Object = MibTableColumn
apnMuTxOctetsAtMCS15 = _ApnMuTxOctetsAtMCS15_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 9, 1, 29),
    _ApnMuTxOctetsAtMCS15_Type()
)
apnMuTxOctetsAtMCS15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnMuTxOctetsAtMCS15.setStatus("current")
_ApnWlanRxPktsTable_Object = MibTable
apnWlanRxPktsTable = _ApnWlanRxPktsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10)
)
if mibBuilder.loadTexts:
    apnWlanRxPktsTable.setStatus("current")
_ApnWlanRxPktsEntry_Object = MibTableRow
apnWlanRxPktsEntry = _ApnWlanRxPktsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1)
)
apnWlanRxPktsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
)
if mibBuilder.loadTexts:
    apnWlanRxPktsEntry.setStatus("current")
_ApnWlanRxPktsAt1Mb_Type = Counter32
_ApnWlanRxPktsAt1Mb_Object = MibTableColumn
apnWlanRxPktsAt1Mb = _ApnWlanRxPktsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 1),
    _ApnWlanRxPktsAt1Mb_Type()
)
apnWlanRxPktsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAt1Mb.setStatus("current")
_ApnWlanRxPktsAt2Mb_Type = Counter32
_ApnWlanRxPktsAt2Mb_Object = MibTableColumn
apnWlanRxPktsAt2Mb = _ApnWlanRxPktsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 2),
    _ApnWlanRxPktsAt2Mb_Type()
)
apnWlanRxPktsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAt2Mb.setStatus("current")
_ApnWlanRxPktsAt5pt5Mb_Type = Counter32
_ApnWlanRxPktsAt5pt5Mb_Object = MibTableColumn
apnWlanRxPktsAt5pt5Mb = _ApnWlanRxPktsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 3),
    _ApnWlanRxPktsAt5pt5Mb_Type()
)
apnWlanRxPktsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAt5pt5Mb.setStatus("current")
_ApnWlanRxPktsAt6Mb_Type = Counter32
_ApnWlanRxPktsAt6Mb_Object = MibTableColumn
apnWlanRxPktsAt6Mb = _ApnWlanRxPktsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 4),
    _ApnWlanRxPktsAt6Mb_Type()
)
apnWlanRxPktsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAt6Mb.setStatus("current")
_ApnWlanRxPktsAt9Mb_Type = Counter32
_ApnWlanRxPktsAt9Mb_Object = MibTableColumn
apnWlanRxPktsAt9Mb = _ApnWlanRxPktsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 5),
    _ApnWlanRxPktsAt9Mb_Type()
)
apnWlanRxPktsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAt9Mb.setStatus("current")
_ApnWlanRxPktsAt11Mb_Type = Counter32
_ApnWlanRxPktsAt11Mb_Object = MibTableColumn
apnWlanRxPktsAt11Mb = _ApnWlanRxPktsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 6),
    _ApnWlanRxPktsAt11Mb_Type()
)
apnWlanRxPktsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAt11Mb.setStatus("current")
_ApnWlanRxPktsAt12Mb_Type = Counter32
_ApnWlanRxPktsAt12Mb_Object = MibTableColumn
apnWlanRxPktsAt12Mb = _ApnWlanRxPktsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 7),
    _ApnWlanRxPktsAt12Mb_Type()
)
apnWlanRxPktsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAt12Mb.setStatus("current")
_ApnWlanRxPktsAt18Mb_Type = Counter32
_ApnWlanRxPktsAt18Mb_Object = MibTableColumn
apnWlanRxPktsAt18Mb = _ApnWlanRxPktsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 8),
    _ApnWlanRxPktsAt18Mb_Type()
)
apnWlanRxPktsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAt18Mb.setStatus("current")
_ApnWlanRxPktsAt24Mb_Type = Counter32
_ApnWlanRxPktsAt24Mb_Object = MibTableColumn
apnWlanRxPktsAt24Mb = _ApnWlanRxPktsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 9),
    _ApnWlanRxPktsAt24Mb_Type()
)
apnWlanRxPktsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAt24Mb.setStatus("current")
_ApnWlanRxPktsAt36Mb_Type = Counter32
_ApnWlanRxPktsAt36Mb_Object = MibTableColumn
apnWlanRxPktsAt36Mb = _ApnWlanRxPktsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 10),
    _ApnWlanRxPktsAt36Mb_Type()
)
apnWlanRxPktsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAt36Mb.setStatus("current")
_ApnWlanRxPktsAt48Mb_Type = Counter32
_ApnWlanRxPktsAt48Mb_Object = MibTableColumn
apnWlanRxPktsAt48Mb = _ApnWlanRxPktsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 11),
    _ApnWlanRxPktsAt48Mb_Type()
)
apnWlanRxPktsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAt48Mb.setStatus("current")
_ApnWlanRxPktsAt54Mb_Type = Counter32
_ApnWlanRxPktsAt54Mb_Object = MibTableColumn
apnWlanRxPktsAt54Mb = _ApnWlanRxPktsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 12),
    _ApnWlanRxPktsAt54Mb_Type()
)
apnWlanRxPktsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAt54Mb.setStatus("current")
_ApnWlanRxPktsAtMCS0_Type = Counter32
_ApnWlanRxPktsAtMCS0_Object = MibTableColumn
apnWlanRxPktsAtMCS0 = _ApnWlanRxPktsAtMCS0_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 13),
    _ApnWlanRxPktsAtMCS0_Type()
)
apnWlanRxPktsAtMCS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAtMCS0.setStatus("current")
_ApnWlanRxPktsAtMCS1_Type = Counter32
_ApnWlanRxPktsAtMCS1_Object = MibTableColumn
apnWlanRxPktsAtMCS1 = _ApnWlanRxPktsAtMCS1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 14),
    _ApnWlanRxPktsAtMCS1_Type()
)
apnWlanRxPktsAtMCS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAtMCS1.setStatus("current")
_ApnWlanRxPktsAtMCS2_Type = Counter32
_ApnWlanRxPktsAtMCS2_Object = MibTableColumn
apnWlanRxPktsAtMCS2 = _ApnWlanRxPktsAtMCS2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 15),
    _ApnWlanRxPktsAtMCS2_Type()
)
apnWlanRxPktsAtMCS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAtMCS2.setStatus("current")
_ApnWlanRxPktsAtMCS3_Type = Counter32
_ApnWlanRxPktsAtMCS3_Object = MibTableColumn
apnWlanRxPktsAtMCS3 = _ApnWlanRxPktsAtMCS3_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 16),
    _ApnWlanRxPktsAtMCS3_Type()
)
apnWlanRxPktsAtMCS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAtMCS3.setStatus("current")
_ApnWlanRxPktsAtMCS4_Type = Counter32
_ApnWlanRxPktsAtMCS4_Object = MibTableColumn
apnWlanRxPktsAtMCS4 = _ApnWlanRxPktsAtMCS4_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 17),
    _ApnWlanRxPktsAtMCS4_Type()
)
apnWlanRxPktsAtMCS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAtMCS4.setStatus("current")
_ApnWlanRxPktsAtMCS5_Type = Counter32
_ApnWlanRxPktsAtMCS5_Object = MibTableColumn
apnWlanRxPktsAtMCS5 = _ApnWlanRxPktsAtMCS5_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 18),
    _ApnWlanRxPktsAtMCS5_Type()
)
apnWlanRxPktsAtMCS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAtMCS5.setStatus("current")
_ApnWlanRxPktsAtMCS6_Type = Counter32
_ApnWlanRxPktsAtMCS6_Object = MibTableColumn
apnWlanRxPktsAtMCS6 = _ApnWlanRxPktsAtMCS6_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 19),
    _ApnWlanRxPktsAtMCS6_Type()
)
apnWlanRxPktsAtMCS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAtMCS6.setStatus("current")
_ApnWlanRxPktsAtMCS7_Type = Counter32
_ApnWlanRxPktsAtMCS7_Object = MibTableColumn
apnWlanRxPktsAtMCS7 = _ApnWlanRxPktsAtMCS7_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 20),
    _ApnWlanRxPktsAtMCS7_Type()
)
apnWlanRxPktsAtMCS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAtMCS7.setStatus("current")
_ApnWlanRxPktsAtMCS8_Type = Counter32
_ApnWlanRxPktsAtMCS8_Object = MibTableColumn
apnWlanRxPktsAtMCS8 = _ApnWlanRxPktsAtMCS8_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 21),
    _ApnWlanRxPktsAtMCS8_Type()
)
apnWlanRxPktsAtMCS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAtMCS8.setStatus("current")
_ApnWlanRxPktsAtMCS9_Type = Counter32
_ApnWlanRxPktsAtMCS9_Object = MibTableColumn
apnWlanRxPktsAtMCS9 = _ApnWlanRxPktsAtMCS9_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 22),
    _ApnWlanRxPktsAtMCS9_Type()
)
apnWlanRxPktsAtMCS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAtMCS9.setStatus("current")
_ApnWlanRxPktsAtMCS10_Type = Counter32
_ApnWlanRxPktsAtMCS10_Object = MibTableColumn
apnWlanRxPktsAtMCS10 = _ApnWlanRxPktsAtMCS10_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 23),
    _ApnWlanRxPktsAtMCS10_Type()
)
apnWlanRxPktsAtMCS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAtMCS10.setStatus("current")
_ApnWlanRxPktsAtMCS11_Type = Counter32
_ApnWlanRxPktsAtMCS11_Object = MibTableColumn
apnWlanRxPktsAtMCS11 = _ApnWlanRxPktsAtMCS11_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 24),
    _ApnWlanRxPktsAtMCS11_Type()
)
apnWlanRxPktsAtMCS11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAtMCS11.setStatus("current")
_ApnWlanRxPktsAtMCS12_Type = Counter32
_ApnWlanRxPktsAtMCS12_Object = MibTableColumn
apnWlanRxPktsAtMCS12 = _ApnWlanRxPktsAtMCS12_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 25),
    _ApnWlanRxPktsAtMCS12_Type()
)
apnWlanRxPktsAtMCS12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAtMCS12.setStatus("current")
_ApnWlanRxPktsAtMCS13_Type = Counter32
_ApnWlanRxPktsAtMCS13_Object = MibTableColumn
apnWlanRxPktsAtMCS13 = _ApnWlanRxPktsAtMCS13_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 26),
    _ApnWlanRxPktsAtMCS13_Type()
)
apnWlanRxPktsAtMCS13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAtMCS13.setStatus("current")
_ApnWlanRxPktsAtMCS14_Type = Counter32
_ApnWlanRxPktsAtMCS14_Object = MibTableColumn
apnWlanRxPktsAtMCS14 = _ApnWlanRxPktsAtMCS14_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 27),
    _ApnWlanRxPktsAtMCS14_Type()
)
apnWlanRxPktsAtMCS14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAtMCS14.setStatus("current")
_ApnWlanRxPktsAtMCS15_Type = Counter32
_ApnWlanRxPktsAtMCS15_Object = MibTableColumn
apnWlanRxPktsAtMCS15 = _ApnWlanRxPktsAtMCS15_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 10, 1, 28),
    _ApnWlanRxPktsAtMCS15_Type()
)
apnWlanRxPktsAtMCS15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxPktsAtMCS15.setStatus("current")
_ApnWlanTxPktsTable_Object = MibTable
apnWlanTxPktsTable = _ApnWlanTxPktsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11)
)
if mibBuilder.loadTexts:
    apnWlanTxPktsTable.setStatus("current")
_ApnWlanTxPktsEntry_Object = MibTableRow
apnWlanTxPktsEntry = _ApnWlanTxPktsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1)
)
apnWlanTxPktsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
)
if mibBuilder.loadTexts:
    apnWlanTxPktsEntry.setStatus("current")
_ApnWlanTxPktsAt1Mb_Type = Counter32
_ApnWlanTxPktsAt1Mb_Object = MibTableColumn
apnWlanTxPktsAt1Mb = _ApnWlanTxPktsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 1),
    _ApnWlanTxPktsAt1Mb_Type()
)
apnWlanTxPktsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAt1Mb.setStatus("current")
_ApnWlanTxPktsAt2Mb_Type = Counter32
_ApnWlanTxPktsAt2Mb_Object = MibTableColumn
apnWlanTxPktsAt2Mb = _ApnWlanTxPktsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 2),
    _ApnWlanTxPktsAt2Mb_Type()
)
apnWlanTxPktsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAt2Mb.setStatus("current")
_ApnWlanTxPktsAt5pt5Mb_Type = Counter32
_ApnWlanTxPktsAt5pt5Mb_Object = MibTableColumn
apnWlanTxPktsAt5pt5Mb = _ApnWlanTxPktsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 3),
    _ApnWlanTxPktsAt5pt5Mb_Type()
)
apnWlanTxPktsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAt5pt5Mb.setStatus("current")
_ApnWlanTxPktsAt6Mb_Type = Counter32
_ApnWlanTxPktsAt6Mb_Object = MibTableColumn
apnWlanTxPktsAt6Mb = _ApnWlanTxPktsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 4),
    _ApnWlanTxPktsAt6Mb_Type()
)
apnWlanTxPktsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAt6Mb.setStatus("current")
_ApnWlanTxPktsAt9Mb_Type = Counter32
_ApnWlanTxPktsAt9Mb_Object = MibTableColumn
apnWlanTxPktsAt9Mb = _ApnWlanTxPktsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 5),
    _ApnWlanTxPktsAt9Mb_Type()
)
apnWlanTxPktsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAt9Mb.setStatus("current")
_ApnWlanTxPktsAt11Mb_Type = Counter32
_ApnWlanTxPktsAt11Mb_Object = MibTableColumn
apnWlanTxPktsAt11Mb = _ApnWlanTxPktsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 6),
    _ApnWlanTxPktsAt11Mb_Type()
)
apnWlanTxPktsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAt11Mb.setStatus("current")
_ApnWlanTxPktsAt12Mb_Type = Counter32
_ApnWlanTxPktsAt12Mb_Object = MibTableColumn
apnWlanTxPktsAt12Mb = _ApnWlanTxPktsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 7),
    _ApnWlanTxPktsAt12Mb_Type()
)
apnWlanTxPktsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAt12Mb.setStatus("current")
_ApnWlanTxPktsAt18Mb_Type = Counter32
_ApnWlanTxPktsAt18Mb_Object = MibTableColumn
apnWlanTxPktsAt18Mb = _ApnWlanTxPktsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 8),
    _ApnWlanTxPktsAt18Mb_Type()
)
apnWlanTxPktsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAt18Mb.setStatus("current")
_ApnWlanTxPktsAt24Mb_Type = Counter32
_ApnWlanTxPktsAt24Mb_Object = MibTableColumn
apnWlanTxPktsAt24Mb = _ApnWlanTxPktsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 9),
    _ApnWlanTxPktsAt24Mb_Type()
)
apnWlanTxPktsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAt24Mb.setStatus("current")
_ApnWlanTxPktsAt36Mb_Type = Counter32
_ApnWlanTxPktsAt36Mb_Object = MibTableColumn
apnWlanTxPktsAt36Mb = _ApnWlanTxPktsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 10),
    _ApnWlanTxPktsAt36Mb_Type()
)
apnWlanTxPktsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAt36Mb.setStatus("current")
_ApnWlanTxPktsAt48Mb_Type = Counter32
_ApnWlanTxPktsAt48Mb_Object = MibTableColumn
apnWlanTxPktsAt48Mb = _ApnWlanTxPktsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 11),
    _ApnWlanTxPktsAt48Mb_Type()
)
apnWlanTxPktsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAt48Mb.setStatus("current")
_ApnWlanTxPktsAt54Mb_Type = Counter32
_ApnWlanTxPktsAt54Mb_Object = MibTableColumn
apnWlanTxPktsAt54Mb = _ApnWlanTxPktsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 12),
    _ApnWlanTxPktsAt54Mb_Type()
)
apnWlanTxPktsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAt54Mb.setStatus("current")
_ApnWlanTxPktsAtMCS0_Type = Counter32
_ApnWlanTxPktsAtMCS0_Object = MibTableColumn
apnWlanTxPktsAtMCS0 = _ApnWlanTxPktsAtMCS0_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 13),
    _ApnWlanTxPktsAtMCS0_Type()
)
apnWlanTxPktsAtMCS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAtMCS0.setStatus("current")
_ApnWlanTxPktsAtMCS1_Type = Counter32
_ApnWlanTxPktsAtMCS1_Object = MibTableColumn
apnWlanTxPktsAtMCS1 = _ApnWlanTxPktsAtMCS1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 14),
    _ApnWlanTxPktsAtMCS1_Type()
)
apnWlanTxPktsAtMCS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAtMCS1.setStatus("current")
_ApnWlanTxPktsAtMCS2_Type = Counter32
_ApnWlanTxPktsAtMCS2_Object = MibTableColumn
apnWlanTxPktsAtMCS2 = _ApnWlanTxPktsAtMCS2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 15),
    _ApnWlanTxPktsAtMCS2_Type()
)
apnWlanTxPktsAtMCS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAtMCS2.setStatus("current")
_ApnWlanTxPktsAtMCS3_Type = Counter32
_ApnWlanTxPktsAtMCS3_Object = MibTableColumn
apnWlanTxPktsAtMCS3 = _ApnWlanTxPktsAtMCS3_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 16),
    _ApnWlanTxPktsAtMCS3_Type()
)
apnWlanTxPktsAtMCS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAtMCS3.setStatus("current")
_ApnWlanTxPktsAtMCS4_Type = Counter32
_ApnWlanTxPktsAtMCS4_Object = MibTableColumn
apnWlanTxPktsAtMCS4 = _ApnWlanTxPktsAtMCS4_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 17),
    _ApnWlanTxPktsAtMCS4_Type()
)
apnWlanTxPktsAtMCS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAtMCS4.setStatus("current")
_ApnWlanTxPktsAtMCS5_Type = Counter32
_ApnWlanTxPktsAtMCS5_Object = MibTableColumn
apnWlanTxPktsAtMCS5 = _ApnWlanTxPktsAtMCS5_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 18),
    _ApnWlanTxPktsAtMCS5_Type()
)
apnWlanTxPktsAtMCS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAtMCS5.setStatus("current")
_ApnWlanTxPktsAtMCS6_Type = Counter32
_ApnWlanTxPktsAtMCS6_Object = MibTableColumn
apnWlanTxPktsAtMCS6 = _ApnWlanTxPktsAtMCS6_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 19),
    _ApnWlanTxPktsAtMCS6_Type()
)
apnWlanTxPktsAtMCS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAtMCS6.setStatus("current")
_ApnWlanTxPktsAtMCS7_Type = Counter32
_ApnWlanTxPktsAtMCS7_Object = MibTableColumn
apnWlanTxPktsAtMCS7 = _ApnWlanTxPktsAtMCS7_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 20),
    _ApnWlanTxPktsAtMCS7_Type()
)
apnWlanTxPktsAtMCS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAtMCS7.setStatus("current")
_ApnWlanTxPktsAtMCS8_Type = Counter32
_ApnWlanTxPktsAtMCS8_Object = MibTableColumn
apnWlanTxPktsAtMCS8 = _ApnWlanTxPktsAtMCS8_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 21),
    _ApnWlanTxPktsAtMCS8_Type()
)
apnWlanTxPktsAtMCS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAtMCS8.setStatus("current")
_ApnWlanTxPktsAtMCS9_Type = Counter32
_ApnWlanTxPktsAtMCS9_Object = MibTableColumn
apnWlanTxPktsAtMCS9 = _ApnWlanTxPktsAtMCS9_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 22),
    _ApnWlanTxPktsAtMCS9_Type()
)
apnWlanTxPktsAtMCS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAtMCS9.setStatus("current")
_ApnWlanTxPktsAtMCS10_Type = Counter32
_ApnWlanTxPktsAtMCS10_Object = MibTableColumn
apnWlanTxPktsAtMCS10 = _ApnWlanTxPktsAtMCS10_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 23),
    _ApnWlanTxPktsAtMCS10_Type()
)
apnWlanTxPktsAtMCS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAtMCS10.setStatus("current")
_ApnWlanTxPktsAtMCS11_Type = Counter32
_ApnWlanTxPktsAtMCS11_Object = MibTableColumn
apnWlanTxPktsAtMCS11 = _ApnWlanTxPktsAtMCS11_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 24),
    _ApnWlanTxPktsAtMCS11_Type()
)
apnWlanTxPktsAtMCS11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAtMCS11.setStatus("current")
_ApnWlanTxPktsAtMCS12_Type = Counter32
_ApnWlanTxPktsAtMCS12_Object = MibTableColumn
apnWlanTxPktsAtMCS12 = _ApnWlanTxPktsAtMCS12_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 25),
    _ApnWlanTxPktsAtMCS12_Type()
)
apnWlanTxPktsAtMCS12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAtMCS12.setStatus("current")
_ApnWlanTxPktsAtMCS13_Type = Counter32
_ApnWlanTxPktsAtMCS13_Object = MibTableColumn
apnWlanTxPktsAtMCS13 = _ApnWlanTxPktsAtMCS13_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 26),
    _ApnWlanTxPktsAtMCS13_Type()
)
apnWlanTxPktsAtMCS13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAtMCS13.setStatus("current")
_ApnWlanTxPktsAtMCS14_Type = Counter32
_ApnWlanTxPktsAtMCS14_Object = MibTableColumn
apnWlanTxPktsAtMCS14 = _ApnWlanTxPktsAtMCS14_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 27),
    _ApnWlanTxPktsAtMCS14_Type()
)
apnWlanTxPktsAtMCS14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAtMCS14.setStatus("current")
_ApnWlanTxPktsAtMCS15_Type = Counter32
_ApnWlanTxPktsAtMCS15_Object = MibTableColumn
apnWlanTxPktsAtMCS15 = _ApnWlanTxPktsAtMCS15_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 11, 1, 28),
    _ApnWlanTxPktsAtMCS15_Type()
)
apnWlanTxPktsAtMCS15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxPktsAtMCS15.setStatus("current")
_ApnWlanRxOctetsTable_Object = MibTable
apnWlanRxOctetsTable = _ApnWlanRxOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12)
)
if mibBuilder.loadTexts:
    apnWlanRxOctetsTable.setStatus("current")
_ApnWlanRxOctetsEntry_Object = MibTableRow
apnWlanRxOctetsEntry = _ApnWlanRxOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1)
)
apnWlanRxOctetsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
)
if mibBuilder.loadTexts:
    apnWlanRxOctetsEntry.setStatus("current")
_ApnWlanRxOctetsAt1Mb_Type = Counter32
_ApnWlanRxOctetsAt1Mb_Object = MibTableColumn
apnWlanRxOctetsAt1Mb = _ApnWlanRxOctetsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 1),
    _ApnWlanRxOctetsAt1Mb_Type()
)
apnWlanRxOctetsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAt1Mb.setStatus("current")
_ApnWlanRxOctetsAt2Mb_Type = Counter32
_ApnWlanRxOctetsAt2Mb_Object = MibTableColumn
apnWlanRxOctetsAt2Mb = _ApnWlanRxOctetsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 2),
    _ApnWlanRxOctetsAt2Mb_Type()
)
apnWlanRxOctetsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAt2Mb.setStatus("current")
_ApnWlanRxOctetsAt5pt5Mb_Type = Counter32
_ApnWlanRxOctetsAt5pt5Mb_Object = MibTableColumn
apnWlanRxOctetsAt5pt5Mb = _ApnWlanRxOctetsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 3),
    _ApnWlanRxOctetsAt5pt5Mb_Type()
)
apnWlanRxOctetsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAt5pt5Mb.setStatus("current")
_ApnWlanRxOctetsAt6Mb_Type = Counter32
_ApnWlanRxOctetsAt6Mb_Object = MibTableColumn
apnWlanRxOctetsAt6Mb = _ApnWlanRxOctetsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 4),
    _ApnWlanRxOctetsAt6Mb_Type()
)
apnWlanRxOctetsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAt6Mb.setStatus("current")
_ApnWlanRxOctetsAt9Mb_Type = Counter32
_ApnWlanRxOctetsAt9Mb_Object = MibTableColumn
apnWlanRxOctetsAt9Mb = _ApnWlanRxOctetsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 5),
    _ApnWlanRxOctetsAt9Mb_Type()
)
apnWlanRxOctetsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAt9Mb.setStatus("current")
_ApnWlanRxOctetsAt11Mb_Type = Counter32
_ApnWlanRxOctetsAt11Mb_Object = MibTableColumn
apnWlanRxOctetsAt11Mb = _ApnWlanRxOctetsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 6),
    _ApnWlanRxOctetsAt11Mb_Type()
)
apnWlanRxOctetsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAt11Mb.setStatus("current")
_ApnWlanRxOctetsAt12Mb_Type = Counter32
_ApnWlanRxOctetsAt12Mb_Object = MibTableColumn
apnWlanRxOctetsAt12Mb = _ApnWlanRxOctetsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 7),
    _ApnWlanRxOctetsAt12Mb_Type()
)
apnWlanRxOctetsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAt12Mb.setStatus("current")
_ApnWlanRxOctetsAt18Mb_Type = Counter32
_ApnWlanRxOctetsAt18Mb_Object = MibTableColumn
apnWlanRxOctetsAt18Mb = _ApnWlanRxOctetsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 8),
    _ApnWlanRxOctetsAt18Mb_Type()
)
apnWlanRxOctetsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAt18Mb.setStatus("current")
_ApnWlanRxOctetsAt24Mb_Type = Counter32
_ApnWlanRxOctetsAt24Mb_Object = MibTableColumn
apnWlanRxOctetsAt24Mb = _ApnWlanRxOctetsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 9),
    _ApnWlanRxOctetsAt24Mb_Type()
)
apnWlanRxOctetsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAt24Mb.setStatus("current")
_ApnWlanRxOctetsAt36Mb_Type = Counter32
_ApnWlanRxOctetsAt36Mb_Object = MibTableColumn
apnWlanRxOctetsAt36Mb = _ApnWlanRxOctetsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 10),
    _ApnWlanRxOctetsAt36Mb_Type()
)
apnWlanRxOctetsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAt36Mb.setStatus("current")
_ApnWlanRxOctetsAt48Mb_Type = Counter32
_ApnWlanRxOctetsAt48Mb_Object = MibTableColumn
apnWlanRxOctetsAt48Mb = _ApnWlanRxOctetsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 11),
    _ApnWlanRxOctetsAt48Mb_Type()
)
apnWlanRxOctetsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAt48Mb.setStatus("current")
_ApnWlanRxOctetsAt54Mb_Type = Counter32
_ApnWlanRxOctetsAt54Mb_Object = MibTableColumn
apnWlanRxOctetsAt54Mb = _ApnWlanRxOctetsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 12),
    _ApnWlanRxOctetsAt54Mb_Type()
)
apnWlanRxOctetsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAt54Mb.setStatus("current")
_ApnWlanRxOctetsAtMCS0_Type = Counter32
_ApnWlanRxOctetsAtMCS0_Object = MibTableColumn
apnWlanRxOctetsAtMCS0 = _ApnWlanRxOctetsAtMCS0_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 13),
    _ApnWlanRxOctetsAtMCS0_Type()
)
apnWlanRxOctetsAtMCS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAtMCS0.setStatus("current")
_ApnWlanRxOctetsAtMCS1_Type = Counter32
_ApnWlanRxOctetsAtMCS1_Object = MibTableColumn
apnWlanRxOctetsAtMCS1 = _ApnWlanRxOctetsAtMCS1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 14),
    _ApnWlanRxOctetsAtMCS1_Type()
)
apnWlanRxOctetsAtMCS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAtMCS1.setStatus("current")
_ApnWlanRxOctetsAtMCS2_Type = Counter32
_ApnWlanRxOctetsAtMCS2_Object = MibTableColumn
apnWlanRxOctetsAtMCS2 = _ApnWlanRxOctetsAtMCS2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 15),
    _ApnWlanRxOctetsAtMCS2_Type()
)
apnWlanRxOctetsAtMCS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAtMCS2.setStatus("current")
_ApnWlanRxOctetsAtMCS3_Type = Counter32
_ApnWlanRxOctetsAtMCS3_Object = MibTableColumn
apnWlanRxOctetsAtMCS3 = _ApnWlanRxOctetsAtMCS3_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 16),
    _ApnWlanRxOctetsAtMCS3_Type()
)
apnWlanRxOctetsAtMCS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAtMCS3.setStatus("current")
_ApnWlanRxOctetsAtMCS4_Type = Counter32
_ApnWlanRxOctetsAtMCS4_Object = MibTableColumn
apnWlanRxOctetsAtMCS4 = _ApnWlanRxOctetsAtMCS4_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 17),
    _ApnWlanRxOctetsAtMCS4_Type()
)
apnWlanRxOctetsAtMCS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAtMCS4.setStatus("current")
_ApnWlanRxOctetsAtMCS5_Type = Counter32
_ApnWlanRxOctetsAtMCS5_Object = MibTableColumn
apnWlanRxOctetsAtMCS5 = _ApnWlanRxOctetsAtMCS5_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 18),
    _ApnWlanRxOctetsAtMCS5_Type()
)
apnWlanRxOctetsAtMCS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAtMCS5.setStatus("current")
_ApnWlanRxOctetsAtMCS6_Type = Counter32
_ApnWlanRxOctetsAtMCS6_Object = MibTableColumn
apnWlanRxOctetsAtMCS6 = _ApnWlanRxOctetsAtMCS6_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 19),
    _ApnWlanRxOctetsAtMCS6_Type()
)
apnWlanRxOctetsAtMCS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAtMCS6.setStatus("current")
_ApnWlanRxOctetsAtMCS7_Type = Counter32
_ApnWlanRxOctetsAtMCS7_Object = MibTableColumn
apnWlanRxOctetsAtMCS7 = _ApnWlanRxOctetsAtMCS7_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 20),
    _ApnWlanRxOctetsAtMCS7_Type()
)
apnWlanRxOctetsAtMCS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAtMCS7.setStatus("current")
_ApnWlanRxOctetsAtMCS8_Type = Counter32
_ApnWlanRxOctetsAtMCS8_Object = MibTableColumn
apnWlanRxOctetsAtMCS8 = _ApnWlanRxOctetsAtMCS8_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 21),
    _ApnWlanRxOctetsAtMCS8_Type()
)
apnWlanRxOctetsAtMCS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAtMCS8.setStatus("current")
_ApnWlanRxOctetsAtMCS9_Type = Counter32
_ApnWlanRxOctetsAtMCS9_Object = MibTableColumn
apnWlanRxOctetsAtMCS9 = _ApnWlanRxOctetsAtMCS9_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 22),
    _ApnWlanRxOctetsAtMCS9_Type()
)
apnWlanRxOctetsAtMCS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAtMCS9.setStatus("current")
_ApnWlanRxOctetsAtMCS10_Type = Counter32
_ApnWlanRxOctetsAtMCS10_Object = MibTableColumn
apnWlanRxOctetsAtMCS10 = _ApnWlanRxOctetsAtMCS10_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 23),
    _ApnWlanRxOctetsAtMCS10_Type()
)
apnWlanRxOctetsAtMCS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAtMCS10.setStatus("current")
_ApnWlanRxOctetsAtMCS11_Type = Counter32
_ApnWlanRxOctetsAtMCS11_Object = MibTableColumn
apnWlanRxOctetsAtMCS11 = _ApnWlanRxOctetsAtMCS11_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 24),
    _ApnWlanRxOctetsAtMCS11_Type()
)
apnWlanRxOctetsAtMCS11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAtMCS11.setStatus("current")
_ApnWlanRxOctetsAtMCS12_Type = Counter32
_ApnWlanRxOctetsAtMCS12_Object = MibTableColumn
apnWlanRxOctetsAtMCS12 = _ApnWlanRxOctetsAtMCS12_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 25),
    _ApnWlanRxOctetsAtMCS12_Type()
)
apnWlanRxOctetsAtMCS12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAtMCS12.setStatus("current")
_ApnWlanRxOctetsAtMCS13_Type = Counter32
_ApnWlanRxOctetsAtMCS13_Object = MibTableColumn
apnWlanRxOctetsAtMCS13 = _ApnWlanRxOctetsAtMCS13_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 26),
    _ApnWlanRxOctetsAtMCS13_Type()
)
apnWlanRxOctetsAtMCS13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAtMCS13.setStatus("current")
_ApnWlanRxOctetsAtMCS14_Type = Counter32
_ApnWlanRxOctetsAtMCS14_Object = MibTableColumn
apnWlanRxOctetsAtMCS14 = _ApnWlanRxOctetsAtMCS14_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 27),
    _ApnWlanRxOctetsAtMCS14_Type()
)
apnWlanRxOctetsAtMCS14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAtMCS14.setStatus("current")
_ApnWlanRxOctetsAtMCS15_Type = Counter32
_ApnWlanRxOctetsAtMCS15_Object = MibTableColumn
apnWlanRxOctetsAtMCS15 = _ApnWlanRxOctetsAtMCS15_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 12, 1, 28),
    _ApnWlanRxOctetsAtMCS15_Type()
)
apnWlanRxOctetsAtMCS15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanRxOctetsAtMCS15.setStatus("current")
_ApnWlanTxOctetsTable_Object = MibTable
apnWlanTxOctetsTable = _ApnWlanTxOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13)
)
if mibBuilder.loadTexts:
    apnWlanTxOctetsTable.setStatus("current")
_ApnWlanTxOctetsEntry_Object = MibTableRow
apnWlanTxOctetsEntry = _ApnWlanTxOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1)
)
apnWlanTxOctetsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
)
if mibBuilder.loadTexts:
    apnWlanTxOctetsEntry.setStatus("current")
_ApnWlanTxOctetsAt1Mb_Type = Counter32
_ApnWlanTxOctetsAt1Mb_Object = MibTableColumn
apnWlanTxOctetsAt1Mb = _ApnWlanTxOctetsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 1),
    _ApnWlanTxOctetsAt1Mb_Type()
)
apnWlanTxOctetsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAt1Mb.setStatus("current")
_ApnWlanTxOctetsAt2Mb_Type = Counter32
_ApnWlanTxOctetsAt2Mb_Object = MibTableColumn
apnWlanTxOctetsAt2Mb = _ApnWlanTxOctetsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 2),
    _ApnWlanTxOctetsAt2Mb_Type()
)
apnWlanTxOctetsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAt2Mb.setStatus("current")
_ApnWlanTxOctetsAt5pt5Mb_Type = Counter32
_ApnWlanTxOctetsAt5pt5Mb_Object = MibTableColumn
apnWlanTxOctetsAt5pt5Mb = _ApnWlanTxOctetsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 3),
    _ApnWlanTxOctetsAt5pt5Mb_Type()
)
apnWlanTxOctetsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAt5pt5Mb.setStatus("current")
_ApnWlanTxOctetsAt6Mb_Type = Counter32
_ApnWlanTxOctetsAt6Mb_Object = MibTableColumn
apnWlanTxOctetsAt6Mb = _ApnWlanTxOctetsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 4),
    _ApnWlanTxOctetsAt6Mb_Type()
)
apnWlanTxOctetsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAt6Mb.setStatus("current")
_ApnWlanTxOctetsAt9Mb_Type = Counter32
_ApnWlanTxOctetsAt9Mb_Object = MibTableColumn
apnWlanTxOctetsAt9Mb = _ApnWlanTxOctetsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 5),
    _ApnWlanTxOctetsAt9Mb_Type()
)
apnWlanTxOctetsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAt9Mb.setStatus("current")
_ApnWlanTxOctetsAt11Mb_Type = Counter32
_ApnWlanTxOctetsAt11Mb_Object = MibTableColumn
apnWlanTxOctetsAt11Mb = _ApnWlanTxOctetsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 6),
    _ApnWlanTxOctetsAt11Mb_Type()
)
apnWlanTxOctetsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAt11Mb.setStatus("current")
_ApnWlanTxOctetsAt12Mb_Type = Counter32
_ApnWlanTxOctetsAt12Mb_Object = MibTableColumn
apnWlanTxOctetsAt12Mb = _ApnWlanTxOctetsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 7),
    _ApnWlanTxOctetsAt12Mb_Type()
)
apnWlanTxOctetsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAt12Mb.setStatus("current")
_ApnWlanTxOctetsAt18Mb_Type = Counter32
_ApnWlanTxOctetsAt18Mb_Object = MibTableColumn
apnWlanTxOctetsAt18Mb = _ApnWlanTxOctetsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 8),
    _ApnWlanTxOctetsAt18Mb_Type()
)
apnWlanTxOctetsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAt18Mb.setStatus("current")
_ApnWlanTxOctetsAt24Mb_Type = Counter32
_ApnWlanTxOctetsAt24Mb_Object = MibTableColumn
apnWlanTxOctetsAt24Mb = _ApnWlanTxOctetsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 9),
    _ApnWlanTxOctetsAt24Mb_Type()
)
apnWlanTxOctetsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAt24Mb.setStatus("current")
_ApnWlanTxOctetsAt36Mb_Type = Counter32
_ApnWlanTxOctetsAt36Mb_Object = MibTableColumn
apnWlanTxOctetsAt36Mb = _ApnWlanTxOctetsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 10),
    _ApnWlanTxOctetsAt36Mb_Type()
)
apnWlanTxOctetsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAt36Mb.setStatus("current")
_ApnWlanTxOctetsAt48Mb_Type = Counter32
_ApnWlanTxOctetsAt48Mb_Object = MibTableColumn
apnWlanTxOctetsAt48Mb = _ApnWlanTxOctetsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 11),
    _ApnWlanTxOctetsAt48Mb_Type()
)
apnWlanTxOctetsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAt48Mb.setStatus("current")
_ApnWlanTxOctetsAt54Mb_Type = Counter32
_ApnWlanTxOctetsAt54Mb_Object = MibTableColumn
apnWlanTxOctetsAt54Mb = _ApnWlanTxOctetsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 12),
    _ApnWlanTxOctetsAt54Mb_Type()
)
apnWlanTxOctetsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAt54Mb.setStatus("current")
_ApnWlanTxOctetsAtMCS0_Type = Counter32
_ApnWlanTxOctetsAtMCS0_Object = MibTableColumn
apnWlanTxOctetsAtMCS0 = _ApnWlanTxOctetsAtMCS0_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 13),
    _ApnWlanTxOctetsAtMCS0_Type()
)
apnWlanTxOctetsAtMCS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAtMCS0.setStatus("current")
_ApnWlanTxOctetsAtMCS1_Type = Counter32
_ApnWlanTxOctetsAtMCS1_Object = MibTableColumn
apnWlanTxOctetsAtMCS1 = _ApnWlanTxOctetsAtMCS1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 14),
    _ApnWlanTxOctetsAtMCS1_Type()
)
apnWlanTxOctetsAtMCS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAtMCS1.setStatus("current")
_ApnWlanTxOctetsAtMCS2_Type = Counter32
_ApnWlanTxOctetsAtMCS2_Object = MibTableColumn
apnWlanTxOctetsAtMCS2 = _ApnWlanTxOctetsAtMCS2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 15),
    _ApnWlanTxOctetsAtMCS2_Type()
)
apnWlanTxOctetsAtMCS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAtMCS2.setStatus("current")
_ApnWlanTxOctetsAtMCS3_Type = Counter32
_ApnWlanTxOctetsAtMCS3_Object = MibTableColumn
apnWlanTxOctetsAtMCS3 = _ApnWlanTxOctetsAtMCS3_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 16),
    _ApnWlanTxOctetsAtMCS3_Type()
)
apnWlanTxOctetsAtMCS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAtMCS3.setStatus("current")
_ApnWlanTxOctetsAtMCS4_Type = Counter32
_ApnWlanTxOctetsAtMCS4_Object = MibTableColumn
apnWlanTxOctetsAtMCS4 = _ApnWlanTxOctetsAtMCS4_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 17),
    _ApnWlanTxOctetsAtMCS4_Type()
)
apnWlanTxOctetsAtMCS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAtMCS4.setStatus("current")
_ApnWlanTxOctetsAtMCS5_Type = Counter32
_ApnWlanTxOctetsAtMCS5_Object = MibTableColumn
apnWlanTxOctetsAtMCS5 = _ApnWlanTxOctetsAtMCS5_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 18),
    _ApnWlanTxOctetsAtMCS5_Type()
)
apnWlanTxOctetsAtMCS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAtMCS5.setStatus("current")
_ApnWlanTxOctetsAtMCS6_Type = Counter32
_ApnWlanTxOctetsAtMCS6_Object = MibTableColumn
apnWlanTxOctetsAtMCS6 = _ApnWlanTxOctetsAtMCS6_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 19),
    _ApnWlanTxOctetsAtMCS6_Type()
)
apnWlanTxOctetsAtMCS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAtMCS6.setStatus("current")
_ApnWlanTxOctetsAtMCS7_Type = Counter32
_ApnWlanTxOctetsAtMCS7_Object = MibTableColumn
apnWlanTxOctetsAtMCS7 = _ApnWlanTxOctetsAtMCS7_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 20),
    _ApnWlanTxOctetsAtMCS7_Type()
)
apnWlanTxOctetsAtMCS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAtMCS7.setStatus("current")
_ApnWlanTxOctetsAtMCS8_Type = Counter32
_ApnWlanTxOctetsAtMCS8_Object = MibTableColumn
apnWlanTxOctetsAtMCS8 = _ApnWlanTxOctetsAtMCS8_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 21),
    _ApnWlanTxOctetsAtMCS8_Type()
)
apnWlanTxOctetsAtMCS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAtMCS8.setStatus("current")
_ApnWlanTxOctetsAtMCS9_Type = Counter32
_ApnWlanTxOctetsAtMCS9_Object = MibTableColumn
apnWlanTxOctetsAtMCS9 = _ApnWlanTxOctetsAtMCS9_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 22),
    _ApnWlanTxOctetsAtMCS9_Type()
)
apnWlanTxOctetsAtMCS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAtMCS9.setStatus("current")
_ApnWlanTxOctetsAtMCS10_Type = Counter32
_ApnWlanTxOctetsAtMCS10_Object = MibTableColumn
apnWlanTxOctetsAtMCS10 = _ApnWlanTxOctetsAtMCS10_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 23),
    _ApnWlanTxOctetsAtMCS10_Type()
)
apnWlanTxOctetsAtMCS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAtMCS10.setStatus("current")
_ApnWlanTxOctetsAtMCS11_Type = Counter32
_ApnWlanTxOctetsAtMCS11_Object = MibTableColumn
apnWlanTxOctetsAtMCS11 = _ApnWlanTxOctetsAtMCS11_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 24),
    _ApnWlanTxOctetsAtMCS11_Type()
)
apnWlanTxOctetsAtMCS11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAtMCS11.setStatus("current")
_ApnWlanTxOctetsAtMCS12_Type = Counter32
_ApnWlanTxOctetsAtMCS12_Object = MibTableColumn
apnWlanTxOctetsAtMCS12 = _ApnWlanTxOctetsAtMCS12_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 25),
    _ApnWlanTxOctetsAtMCS12_Type()
)
apnWlanTxOctetsAtMCS12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAtMCS12.setStatus("current")
_ApnWlanTxOctetsAtMCS13_Type = Counter32
_ApnWlanTxOctetsAtMCS13_Object = MibTableColumn
apnWlanTxOctetsAtMCS13 = _ApnWlanTxOctetsAtMCS13_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 26),
    _ApnWlanTxOctetsAtMCS13_Type()
)
apnWlanTxOctetsAtMCS13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAtMCS13.setStatus("current")
_ApnWlanTxOctetsAtMCS14_Type = Counter32
_ApnWlanTxOctetsAtMCS14_Object = MibTableColumn
apnWlanTxOctetsAtMCS14 = _ApnWlanTxOctetsAtMCS14_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 27),
    _ApnWlanTxOctetsAtMCS14_Type()
)
apnWlanTxOctetsAtMCS14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAtMCS14.setStatus("current")
_ApnWlanTxOctetsAtMCS15_Type = Counter32
_ApnWlanTxOctetsAtMCS15_Object = MibTableColumn
apnWlanTxOctetsAtMCS15 = _ApnWlanTxOctetsAtMCS15_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 8, 13, 1, 28),
    _ApnWlanTxOctetsAtMCS15_Type()
)
apnWlanTxOctetsAtMCS15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnWlanTxOctetsAtMCS15.setStatus("current")
_ApDiagStats_ObjectIdentity = ObjectIdentity
apDiagStats = _ApDiagStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 9)
)
_ApDiagCpuStats_ObjectIdentity = ObjectIdentity
apDiagCpuStats = _ApDiagCpuStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 9, 1)
)


class _ApDiagCpuLoad1Min_Type(Unsigned32):
    """Custom type apDiagCpuLoad1Min based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ApDiagCpuLoad1Min_Type.__name__ = "Unsigned32"
_ApDiagCpuLoad1Min_Object = MibScalar
apDiagCpuLoad1Min = _ApDiagCpuLoad1Min_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 9, 1, 1),
    _ApDiagCpuLoad1Min_Type()
)
apDiagCpuLoad1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDiagCpuLoad1Min.setStatus("current")
if mibBuilder.loadTexts:
    apDiagCpuLoad1Min.setUnits("%")


class _ApDiagCpuLoad5Min_Type(Unsigned32):
    """Custom type apDiagCpuLoad5Min based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ApDiagCpuLoad5Min_Type.__name__ = "Unsigned32"
_ApDiagCpuLoad5Min_Object = MibScalar
apDiagCpuLoad5Min = _ApDiagCpuLoad5Min_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 9, 1, 2),
    _ApDiagCpuLoad5Min_Type()
)
apDiagCpuLoad5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDiagCpuLoad5Min.setStatus("current")
if mibBuilder.loadTexts:
    apDiagCpuLoad5Min.setUnits("%")


class _ApDiagCpuLoad15Min_Type(Unsigned32):
    """Custom type apDiagCpuLoad15Min based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ApDiagCpuLoad15Min_Type.__name__ = "Unsigned32"
_ApDiagCpuLoad15Min_Object = MibScalar
apDiagCpuLoad15Min = _ApDiagCpuLoad15Min_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 9, 1, 3),
    _ApDiagCpuLoad15Min_Type()
)
apDiagCpuLoad15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDiagCpuLoad15Min.setStatus("current")
if mibBuilder.loadTexts:
    apDiagCpuLoad15Min.setUnits("%")
_ApDiagRamStats_ObjectIdentity = ObjectIdentity
apDiagRamStats = _ApDiagRamStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 9, 2)
)
_ApDiagRamTotal_Type = Unsigned32
_ApDiagRamTotal_Object = MibScalar
apDiagRamTotal = _ApDiagRamTotal_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 9, 2, 1),
    _ApDiagRamTotal_Type()
)
apDiagRamTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDiagRamTotal.setStatus("current")
if mibBuilder.loadTexts:
    apDiagRamTotal.setUnits("megabytes")
_ApDiagRamUsed_Type = Unsigned32
_ApDiagRamUsed_Object = MibScalar
apDiagRamUsed = _ApDiagRamUsed_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 9, 2, 2),
    _ApDiagRamUsed_Type()
)
apDiagRamUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDiagRamUsed.setStatus("current")
if mibBuilder.loadTexts:
    apDiagRamUsed.setUnits("megabytes")


class _ApDiagRamPercentageUsed_Type(Unsigned32):
    """Custom type apDiagRamPercentageUsed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ApDiagRamPercentageUsed_Type.__name__ = "Unsigned32"
_ApDiagRamPercentageUsed_Object = MibScalar
apDiagRamPercentageUsed = _ApDiagRamPercentageUsed_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 9, 2, 3),
    _ApDiagRamPercentageUsed_Type()
)
apDiagRamPercentageUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDiagRamPercentageUsed.setStatus("current")
if mibBuilder.loadTexts:
    apDiagRamPercentageUsed.setUnits("0.1%")
_ApLanStats_ObjectIdentity = ObjectIdentity
apLanStats = _ApLanStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 10)
)
_ApLanInfoTable_Object = MibTable
apLanInfoTable = _ApLanInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 10, 1)
)
if mibBuilder.loadTexts:
    apLanInfoTable.setStatus("current")
_ApLanInfoEntry_Object = MibTableRow
apLanInfoEntry = _ApLanInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 10, 1, 1)
)
apLanInfoEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apLanInfoIndex"),
)
if mibBuilder.loadTexts:
    apLanInfoEntry.setStatus("current")


class _ApLanInfoIndex_Type(Integer32):
    """Custom type apLanInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ApLanInfoIndex_Type.__name__ = "Integer32"
_ApLanInfoIndex_Object = MibTableColumn
apLanInfoIndex = _ApLanInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 10, 1, 1, 1),
    _ApLanInfoIndex_Type()
)
apLanInfoIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apLanInfoIndex.setStatus("current")
_ApLanInfoEnabled_Type = TruthValue
_ApLanInfoEnabled_Object = MibTableColumn
apLanInfoEnabled = _ApLanInfoEnabled_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 10, 1, 1, 2),
    _ApLanInfoEnabled_Type()
)
apLanInfoEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanInfoEnabled.setStatus("current")
_ApLanInfoIpAddress_Type = IpAddress
_ApLanInfoIpAddress_Object = MibTableColumn
apLanInfoIpAddress = _ApLanInfoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 10, 1, 1, 3),
    _ApLanInfoIpAddress_Type()
)
apLanInfoIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanInfoIpAddress.setStatus("current")
_ApLanInfoNetworkMask_Type = IpAddress
_ApLanInfoNetworkMask_Object = MibTableColumn
apLanInfoNetworkMask = _ApLanInfoNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 10, 1, 1, 4),
    _ApLanInfoNetworkMask_Type()
)
apLanInfoNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanInfoNetworkMask.setStatus("current")
_ApLanInfoEthernetAddress_Type = PhysAddress
_ApLanInfoEthernetAddress_Object = MibTableColumn
apLanInfoEthernetAddress = _ApLanInfoEthernetAddress_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 10, 1, 1, 5),
    _ApLanInfoEthernetAddress_Type()
)
apLanInfoEthernetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanInfoEthernetAddress.setStatus("current")
_ApLanInfoSpeed_Type = Unsigned32
_ApLanInfoSpeed_Object = MibTableColumn
apLanInfoSpeed = _ApLanInfoSpeed_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 10, 1, 1, 6),
    _ApLanInfoSpeed_Type()
)
apLanInfoSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanInfoSpeed.setStatus("current")
if mibBuilder.loadTexts:
    apLanInfoSpeed.setUnits("mbps")


class _ApLanInfoDuplexMode_Type(Integer32):
    """Custom type apLanInfoDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 0))
    )


_ApLanInfoDuplexMode_Type.__name__ = "Integer32"
_ApLanInfoDuplexMode_Object = MibTableColumn
apLanInfoDuplexMode = _ApLanInfoDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 10, 1, 1, 7),
    _ApLanInfoDuplexMode_Type()
)
apLanInfoDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanInfoDuplexMode.setStatus("current")
_ApLanRxPktsTable_Object = MibTable
apLanRxPktsTable = _ApLanRxPktsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 10, 2)
)
if mibBuilder.loadTexts:
    apLanRxPktsTable.setStatus("current")
_ApLanRxPktsEntry_Object = MibTableRow
apLanRxPktsEntry = _ApLanRxPktsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 10, 2, 1)
)
apLanRxPktsEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apLanInfoIndex"),
)
if mibBuilder.loadTexts:
    apLanRxPktsEntry.setStatus("current")
_ApLanRxPkts_Type = Counter32
_ApLanRxPkts_Object = MibTableColumn
apLanRxPkts = _ApLanRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 10, 2, 1, 1),
    _ApLanRxPkts_Type()
)
apLanRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanRxPkts.setStatus("current")
_ApLanRxBytes_Type = Counter32
_ApLanRxBytes_Object = MibTableColumn
apLanRxBytes = _ApLanRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 10, 2, 1, 2),
    _ApLanRxBytes_Type()
)
apLanRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanRxBytes.setStatus("current")
_ApLanRxErrors_Type = Counter32
_ApLanRxErrors_Object = MibTableColumn
apLanRxErrors = _ApLanRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 10, 2, 1, 3),
    _ApLanRxErrors_Type()
)
apLanRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanRxErrors.setStatus("current")
_ApLanRxDropped_Type = Counter32
_ApLanRxDropped_Object = MibTableColumn
apLanRxDropped = _ApLanRxDropped_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 10, 2, 1, 4),
    _ApLanRxDropped_Type()
)
apLanRxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanRxDropped.setStatus("current")
_ApLanRxFrameErrors_Type = Counter32
_ApLanRxFrameErrors_Object = MibTableColumn
apLanRxFrameErrors = _ApLanRxFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 10, 2, 1, 5),
    _ApLanRxFrameErrors_Type()
)
apLanRxFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanRxFrameErrors.setStatus("current")
_ApLanTxPktsTable_Object = MibTable
apLanTxPktsTable = _ApLanTxPktsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 10, 4)
)
if mibBuilder.loadTexts:
    apLanTxPktsTable.setStatus("current")
_ApLanTxPktsEntry_Object = MibTableRow
apLanTxPktsEntry = _ApLanTxPktsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 10, 4, 1)
)
apLanTxPktsEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apLanInfoIndex"),
)
if mibBuilder.loadTexts:
    apLanTxPktsEntry.setStatus("current")
_ApLanTxPkts_Type = Counter32
_ApLanTxPkts_Object = MibTableColumn
apLanTxPkts = _ApLanTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 10, 4, 1, 1),
    _ApLanTxPkts_Type()
)
apLanTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanTxPkts.setStatus("current")
_ApLanTxBytes_Type = Counter32
_ApLanTxBytes_Object = MibTableColumn
apLanTxBytes = _ApLanTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 10, 4, 1, 2),
    _ApLanTxBytes_Type()
)
apLanTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanTxBytes.setStatus("current")
_ApLanTxErrors_Type = Counter32
_ApLanTxErrors_Object = MibTableColumn
apLanTxErrors = _ApLanTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 10, 4, 1, 3),
    _ApLanTxErrors_Type()
)
apLanTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanTxErrors.setStatus("current")
_ApLanTxDropped_Type = Counter32
_ApLanTxDropped_Object = MibTableColumn
apLanTxDropped = _ApLanTxDropped_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 10, 4, 1, 4),
    _ApLanTxDropped_Type()
)
apLanTxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanTxDropped.setStatus("current")
_ApLanTxFrameErrors_Type = Counter32
_ApLanTxFrameErrors_Object = MibTableColumn
apLanTxFrameErrors = _ApLanTxFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 9, 10, 4, 1, 5),
    _ApLanTxFrameErrors_Type()
)
apLanTxFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanTxFrameErrors.setStatus("current")
_ApMgmtAccess_ObjectIdentity = ObjectIdentity
apMgmtAccess = _ApMgmtAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 10)
)


class _ApMgmtAccessToAllow_Type(Bits):
    """Custom type apMgmtAccessToAllow based on Bits"""
    namedValues = NamedValues(
        *(("fromLan1AppletHttp", 0),
          ("fromLan1AppletHttps", 1),
          ("fromLan1CliTelnet", 2),
          ("fromLan1Snmp", 4),
          ("fromLan1Ssh", 3),
          ("fromLan2AppletHttp", 5),
          ("fromLan2AppletHttps", 6),
          ("fromLan2CliTelnet", 7),
          ("fromLan2Snmp", 9),
          ("fromLan2Ssh", 8),
          ("fromWanAppletHttp", 10),
          ("fromWanAppletHttps", 11),
          ("fromWanCliTelnet", 12),
          ("fromWanSnmp", 14),
          ("fromWanSsh", 13))
    )

_ApMgmtAccessToAllow_Type.__name__ = "Bits"
_ApMgmtAccessToAllow_Object = MibScalar
apMgmtAccessToAllow = _ApMgmtAccessToAllow_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 10, 1),
    _ApMgmtAccessToAllow_Type()
)
apMgmtAccessToAllow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMgmtAccessToAllow.setStatus("current")
_ApTrustedHost_ObjectIdentity = ObjectIdentity
apTrustedHost = _ApTrustedHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 10, 2)
)
_ApTrustedHostEnable_Type = TruthValue
_ApTrustedHostEnable_Object = MibScalar
apTrustedHostEnable = _ApTrustedHostEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 10, 2, 1),
    _ApTrustedHostEnable_Type()
)
apTrustedHostEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTrustedHostEnable.setStatus("current")
_ApTrustedHostRangeTable_Object = MibTable
apTrustedHostRangeTable = _ApTrustedHostRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 10, 2, 2)
)
if mibBuilder.loadTexts:
    apTrustedHostRangeTable.setStatus("current")
_ApTrustedHostRangeEntry_Object = MibTableRow
apTrustedHostRangeEntry = _ApTrustedHostRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 10, 2, 2, 1)
)
apTrustedHostRangeEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apTrustedHostRangeIndex"),
)
if mibBuilder.loadTexts:
    apTrustedHostRangeEntry.setStatus("current")


class _ApTrustedHostRangeIndex_Type(Integer32):
    """Custom type apTrustedHostRangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ApTrustedHostRangeIndex_Type.__name__ = "Integer32"
_ApTrustedHostRangeIndex_Object = MibTableColumn
apTrustedHostRangeIndex = _ApTrustedHostRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 10, 2, 2, 1, 1),
    _ApTrustedHostRangeIndex_Type()
)
apTrustedHostRangeIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apTrustedHostRangeIndex.setStatus("current")
_ApTrustedHostRangeLowerIp_Type = IpAddress
_ApTrustedHostRangeLowerIp_Object = MibTableColumn
apTrustedHostRangeLowerIp = _ApTrustedHostRangeLowerIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 10, 2, 2, 1, 2),
    _ApTrustedHostRangeLowerIp_Type()
)
apTrustedHostRangeLowerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTrustedHostRangeLowerIp.setStatus("current")
_ApTrustedHostRangeUpperIp_Type = IpAddress
_ApTrustedHostRangeUpperIp_Object = MibTableColumn
apTrustedHostRangeUpperIp = _ApTrustedHostRangeUpperIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 10, 2, 2, 1, 3),
    _ApTrustedHostRangeUpperIp_Type()
)
apTrustedHostRangeUpperIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTrustedHostRangeUpperIp.setStatus("current")
_ApRouter_ObjectIdentity = ObjectIdentity
apRouter = _ApRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 11)
)


class _ApRouterDefaultGatewayInterface_Type(Integer32):
    """Custom type apRouterDefaultGatewayInterface based on Integer32"""
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
        *(("lan1", 1),
          ("lan2", 2),
          ("none", 4),
          ("wan", 3))
    )


_ApRouterDefaultGatewayInterface_Type.__name__ = "Integer32"
_ApRouterDefaultGatewayInterface_Object = MibScalar
apRouterDefaultGatewayInterface = _ApRouterDefaultGatewayInterface_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 11, 1),
    _ApRouterDefaultGatewayInterface_Type()
)
apRouterDefaultGatewayInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRouterDefaultGatewayInterface.setStatus("current")
_ApManualTime_ObjectIdentity = ObjectIdentity
apManualTime = _ApManualTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 12)
)
_ApManualCurrSystemDateTime_Type = DisplayString
_ApManualCurrSystemDateTime_Object = MibScalar
apManualCurrSystemDateTime = _ApManualCurrSystemDateTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 12, 1),
    _ApManualCurrSystemDateTime_Type()
)
apManualCurrSystemDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apManualCurrSystemDateTime.setStatus("current")
_ApManualTimeZoneSetting_ObjectIdentity = ObjectIdentity
apManualTimeZoneSetting = _ApManualTimeZoneSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 12, 2)
)
_ApManualTimeZoneTable_Object = MibTable
apManualTimeZoneTable = _ApManualTimeZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 12, 2, 1)
)
if mibBuilder.loadTexts:
    apManualTimeZoneTable.setStatus("current")
_ApManualTimeZoneEntry_Object = MibTableRow
apManualTimeZoneEntry = _ApManualTimeZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 12, 2, 1, 1)
)
apManualTimeZoneEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apManualTimeZoneIndex"),
)
if mibBuilder.loadTexts:
    apManualTimeZoneEntry.setStatus("current")


class _ApManualTimeZoneIndex_Type(Integer32):
    """Custom type apManualTimeZoneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 550),
    )


_ApManualTimeZoneIndex_Type.__name__ = "Integer32"
_ApManualTimeZoneIndex_Object = MibTableColumn
apManualTimeZoneIndex = _ApManualTimeZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 12, 2, 1, 1, 1),
    _ApManualTimeZoneIndex_Type()
)
apManualTimeZoneIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apManualTimeZoneIndex.setStatus("current")
_ApManualTimeZoneName_Type = DisplayString
_ApManualTimeZoneName_Object = MibTableColumn
apManualTimeZoneName = _ApManualTimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 12, 2, 1, 1, 2),
    _ApManualTimeZoneName_Type()
)
apManualTimeZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apManualTimeZoneName.setStatus("current")
_ApManualExpectedTimeZone_Type = SinglePointer
_ApManualExpectedTimeZone_Object = MibScalar
apManualExpectedTimeZone = _ApManualExpectedTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 12, 2, 2),
    _ApManualExpectedTimeZone_Type()
)
apManualExpectedTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apManualExpectedTimeZone.setStatus("current")
_ApManualTimeZoneSet_Type = DoActionNow
_ApManualTimeZoneSet_Object = MibScalar
apManualTimeZoneSet = _ApManualTimeZoneSet_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 12, 2, 3),
    _ApManualTimeZoneSet_Type()
)
apManualTimeZoneSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apManualTimeZoneSet.setStatus("current")
_ApManualDateTimeSetting_ObjectIdentity = ObjectIdentity
apManualDateTimeSetting = _ApManualDateTimeSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 12, 3)
)


class _ApManualExpectedYear_Type(Integer32):
    """Custom type apManualExpectedYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1970, 9999),
    )


_ApManualExpectedYear_Type.__name__ = "Integer32"
_ApManualExpectedYear_Object = MibScalar
apManualExpectedYear = _ApManualExpectedYear_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 12, 3, 1),
    _ApManualExpectedYear_Type()
)
apManualExpectedYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apManualExpectedYear.setStatus("current")


class _ApManualExpectedMonth_Type(Integer32):
    """Custom type apManualExpectedMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ApManualExpectedMonth_Type.__name__ = "Integer32"
_ApManualExpectedMonth_Object = MibScalar
apManualExpectedMonth = _ApManualExpectedMonth_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 12, 3, 2),
    _ApManualExpectedMonth_Type()
)
apManualExpectedMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apManualExpectedMonth.setStatus("current")


class _ApManualExpectedDay_Type(Integer32):
    """Custom type apManualExpectedDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_ApManualExpectedDay_Type.__name__ = "Integer32"
_ApManualExpectedDay_Object = MibScalar
apManualExpectedDay = _ApManualExpectedDay_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 12, 3, 3),
    _ApManualExpectedDay_Type()
)
apManualExpectedDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apManualExpectedDay.setStatus("current")


class _ApManualExpectedHour_Type(Integer32):
    """Custom type apManualExpectedHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_ApManualExpectedHour_Type.__name__ = "Integer32"
_ApManualExpectedHour_Object = MibScalar
apManualExpectedHour = _ApManualExpectedHour_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 12, 3, 4),
    _ApManualExpectedHour_Type()
)
apManualExpectedHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apManualExpectedHour.setStatus("current")


class _ApManualExpectedMinutes_Type(Integer32):
    """Custom type apManualExpectedMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_ApManualExpectedMinutes_Type.__name__ = "Integer32"
_ApManualExpectedMinutes_Object = MibScalar
apManualExpectedMinutes = _ApManualExpectedMinutes_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 12, 3, 5),
    _ApManualExpectedMinutes_Type()
)
apManualExpectedMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apManualExpectedMinutes.setStatus("current")


class _ApManualExpectedSeconds_Type(Integer32):
    """Custom type apManualExpectedSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_ApManualExpectedSeconds_Type.__name__ = "Integer32"
_ApManualExpectedSeconds_Object = MibScalar
apManualExpectedSeconds = _ApManualExpectedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 12, 3, 6),
    _ApManualExpectedSeconds_Type()
)
apManualExpectedSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apManualExpectedSeconds.setStatus("current")
_ApManualDateTimeSet_Type = DoActionNow
_ApManualDateTimeSet_Object = MibScalar
apManualDateTimeSet = _ApManualDateTimeSet_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 12, 3, 7),
    _ApManualDateTimeSet_Type()
)
apManualDateTimeSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apManualDateTimeSet.setStatus("current")
_ApAdmin_ObjectIdentity = ObjectIdentity
apAdmin = _ApAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 13)
)
_ApLoginMessage_ObjectIdentity = ObjectIdentity
apLoginMessage = _ApLoginMessage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 13, 1)
)
_ApLoginMessageMode_Type = TruthValue
_ApLoginMessageMode_Object = MibScalar
apLoginMessageMode = _ApLoginMessageMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 13, 1, 1),
    _ApLoginMessageMode_Type()
)
apLoginMessageMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLoginMessageMode.setStatus("current")
_ApLoginMessageText_Type = DisplayString
_ApLoginMessageText_Object = MibScalar
apLoginMessageText = _ApLoginMessageText_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 13, 1, 2),
    _ApLoginMessageText_Type()
)
apLoginMessageText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLoginMessageText.setStatus("current")
_ApRadiusServer_ObjectIdentity = ObjectIdentity
apRadiusServer = _ApRadiusServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 14)
)
_ApRadiusUsers_ObjectIdentity = ObjectIdentity
apRadiusUsers = _ApRadiusUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 14, 1)
)
_ApRadiusUsersGroupTable_Object = MibTable
apRadiusUsersGroupTable = _ApRadiusUsersGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 14, 1, 1)
)
if mibBuilder.loadTexts:
    apRadiusUsersGroupTable.setStatus("current")
_ApRadiusUsersGroupEntry_Object = MibTableRow
apRadiusUsersGroupEntry = _ApRadiusUsersGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 14, 1, 1, 1)
)
apRadiusUsersGroupEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apRadiusUsersGroup"),
)
if mibBuilder.loadTexts:
    apRadiusUsersGroupEntry.setStatus("current")
_ApRadiusUsersGroup_Type = DisplayString
_ApRadiusUsersGroup_Object = MibTableColumn
apRadiusUsersGroup = _ApRadiusUsersGroup_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 14, 1, 1, 1, 1),
    _ApRadiusUsersGroup_Type()
)
apRadiusUsersGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadiusUsersGroup.setStatus("current")
_ApRadiusUsersGroupRowStatus_Type = AbbrevRowStatus
_ApRadiusUsersGroupRowStatus_Object = MibTableColumn
apRadiusUsersGroupRowStatus = _ApRadiusUsersGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 14, 1, 1, 1, 2),
    _ApRadiusUsersGroupRowStatus_Type()
)
apRadiusUsersGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadiusUsersGroupRowStatus.setStatus("current")
_ApRadiusUsersGroupId_Type = Integer32
_ApRadiusUsersGroupId_Object = MibTableColumn
apRadiusUsersGroupId = _ApRadiusUsersGroupId_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 14, 1, 1, 1, 3),
    _ApRadiusUsersGroupId_Type()
)
apRadiusUsersGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadiusUsersGroupId.setStatus("current")
_ApRadiusAccess_ObjectIdentity = ObjectIdentity
apRadiusAccess = _ApRadiusAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 14, 2)
)
_ApRadiusAccessTable_Object = MibTable
apRadiusAccessTable = _ApRadiusAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 14, 2, 1)
)
if mibBuilder.loadTexts:
    apRadiusAccessTable.setStatus("current")
_ApRadiusAccessEntry_Object = MibTableRow
apRadiusAccessEntry = _ApRadiusAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 14, 2, 1, 1)
)
apRadiusAccessEntry.setIndexNames(
    (0, "SYMBOL-AP-MIB", "apRadiusUsersGroup"),
)
if mibBuilder.loadTexts:
    apRadiusAccessEntry.setStatus("current")


class _ApRadiusAccessWlanPtrs_Type(Bits):
    """Custom type apRadiusAccessWlanPtrs based on Bits"""
    namedValues = NamedValues(
        *(("null", 0),
          ("wlan1", 1),
          ("wlan2", 2),
          ("wlan3", 3),
          ("wlan4", 4))
    )

_ApRadiusAccessWlanPtrs_Type.__name__ = "Bits"
_ApRadiusAccessWlanPtrs_Object = MibTableColumn
apRadiusAccessWlanPtrs = _ApRadiusAccessWlanPtrs_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 14, 2, 1, 1, 2),
    _ApRadiusAccessWlanPtrs_Type()
)
apRadiusAccessWlanPtrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadiusAccessWlanPtrs.setStatus("current")
_ApRadiusAccessTimeRule_Type = DisplayString
_ApRadiusAccessTimeRule_Object = MibTableColumn
apRadiusAccessTimeRule = _ApRadiusAccessTimeRule_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 14, 2, 1, 1, 3),
    _ApRadiusAccessTimeRule_Type()
)
apRadiusAccessTimeRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadiusAccessTimeRule.setStatus("current")
_ApWips_ObjectIdentity = ObjectIdentity
apWips = _ApWips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 15)
)
_ApWipsPrimaryServerAddr_Type = IpAddress
_ApWipsPrimaryServerAddr_Object = MibScalar
apWipsPrimaryServerAddr = _ApWipsPrimaryServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 15, 1),
    _ApWipsPrimaryServerAddr_Type()
)
apWipsPrimaryServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWipsPrimaryServerAddr.setStatus("current")
_ApWipsSecondaryServerAddr_Type = IpAddress
_ApWipsSecondaryServerAddr_Object = MibScalar
apWipsSecondaryServerAddr = _ApWipsSecondaryServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 15, 2),
    _ApWipsSecondaryServerAddr_Type()
)
apWipsSecondaryServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWipsSecondaryServerAddr.setStatus("current")
_ApPower_ObjectIdentity = ObjectIdentity
apPower = _ApPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 16)
)


class _ApPowerMode_Type(Integer32):
    """Custom type apPowerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode3af", 2),
          ("modeAuto", 1))
    )


_ApPowerMode_Type.__name__ = "Integer32"
_ApPowerMode_Object = MibScalar
apPowerMode = _ApPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 16, 1),
    _ApPowerMode_Type()
)
apPowerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPowerMode.setStatus("current")


class _ApPowerDefRadio_Type(Integer32):
    """Custom type apPowerDefRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radio1", 1),
          ("radio2", 2))
    )


_ApPowerDefRadio_Type.__name__ = "Integer32"
_ApPowerDefRadio_Object = MibScalar
apPowerDefRadio = _ApPowerDefRadio_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 16, 2),
    _ApPowerDefRadio_Type()
)
apPowerDefRadio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPowerDefRadio.setStatus("current")


class _ApPowerStatus_Type(Integer32):
    """Custom type apPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullAvailable", 3),
          ("mid", 2),
          ("power3af", 1))
    )


_ApPowerStatus_Type.__name__ = "Integer32"
_ApPowerStatus_Object = MibScalar
apPowerStatus = _ApPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 16, 3),
    _ApPowerStatus_Type()
)
apPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPowerStatus.setStatus("current")
_ApGroups_ObjectIdentity = ObjectIdentity
apGroups = _ApGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 1000)
)
_ApGroupsV1dot0_ObjectIdentity = ObjectIdentity
apGroupsV1dot0 = _ApGroupsV1dot0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 1000, 1)
)
_ApGroupsV1dot1_ObjectIdentity = ObjectIdentity
apGroupsV1dot1 = _ApGroupsV1dot1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 1000, 2)
)
_ApGroupsV2dot2_ObjectIdentity = ObjectIdentity
apGroupsV2dot2 = _ApGroupsV2dot2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 1000, 3)
)
ccWanVpnEntry.registerAugmentions(
    ("SYMBOL-AP-MIB",
     "apWanVpnKeyAutoEntry")
)
apWanVpnKeyAutoEntry.setIndexNames(*ccWanVpnEntry.getIndexNames())
ccSubnetEntry.registerAugmentions(
    ("SYMBOL-AP-MIB",
     "apSubnetEntry")
)
apSubnetEntry.setIndexNames(*ccSubnetEntry.getIndexNames())
ccSubnetEntry.registerAugmentions(
    ("SYMBOL-AP-MIB",
     "apLanBridgeEntry")
)
apLanBridgeEntry.setIndexNames(*ccSubnetEntry.getIndexNames())
ccSubnetEntry.registerAugmentions(
    ("SYMBOL-AP-MIB",
     "apLanSTPStatsEntry")
)
apLanSTPStatsEntry.setIndexNames(*ccSubnetEntry.getIndexNames())

# Managed Objects groups

dot1xGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 1000, 1, 1)
)
dot1xGroup.setObjects(
      *(("SYMBOL-AP-MIB", "dot1xPaePortNumber"),
        ("SYMBOL-AP-MIB", "dot1xPaeState"),
        ("SYMBOL-AP-MIB", "dot1xAuthBackendAuthState"),
        ("SYMBOL-AP-MIB", "dot1xAuthAdminControlledDirections"),
        ("SYMBOL-AP-MIB", "dot1xAuthOperControlledDirections"),
        ("SYMBOL-AP-MIB", "dot1xAuthAuthControlledPortStatus"),
        ("SYMBOL-AP-MIB", "dot1xAuthAuthControlledPortControl"),
        ("SYMBOL-AP-MIB", "dot1xAuthQuietPeriod"),
        ("SYMBOL-AP-MIB", "dot1xAuthTxPeriod"),
        ("SYMBOL-AP-MIB", "dot1xAuthSuppTimeout"),
        ("SYMBOL-AP-MIB", "dot1xAuthServerTimeout"),
        ("SYMBOL-AP-MIB", "dot1xAuthMaxReq"),
        ("SYMBOL-AP-MIB", "dot1xAuthReAuthPeriod"),
        ("SYMBOL-AP-MIB", "dot1xAuthReAuthEnabled"),
        ("SYMBOL-AP-MIB", "dot1xAuthKeyTxEnabled"),
        ("SYMBOL-AP-MIB", "dot1xAuthEapolFramesRx"),
        ("SYMBOL-AP-MIB", "dot1xAuthEapolFramesTx"),
        ("SYMBOL-AP-MIB", "dot1xAuthEapolStartFramesRx"),
        ("SYMBOL-AP-MIB", "dot1xAuthEapolLogoffFramesRx"),
        ("SYMBOL-AP-MIB", "dot1xAuthEapolRespIdFramesRx"),
        ("SYMBOL-AP-MIB", "dot1xAuthEapolRespFramesRx"),
        ("SYMBOL-AP-MIB", "dot1xAuthEapolReqIdFramesTx"),
        ("SYMBOL-AP-MIB", "dot1xAuthEapolReqFramesTx"),
        ("SYMBOL-AP-MIB", "dot1xAuthInvalidEapolFramesRx"),
        ("SYMBOL-AP-MIB", "dot1xAuthEapLengthErrorFramesRx"),
        ("SYMBOL-AP-MIB", "dot1xAuthLastEapolFrameVersion"),
        ("SYMBOL-AP-MIB", "dot1xAuthLastEapolFrameSource"),
        ("SYMBOL-AP-MIB", "dot1xAuthEntersConnecting"),
        ("SYMBOL-AP-MIB", "dot1xAuthEapLogoffsWhileConnecting"),
        ("SYMBOL-AP-MIB", "dot1xAuthEntersAuthenticating"),
        ("SYMBOL-AP-MIB", "dot1xAuthAuthSuccessWhileAuthenticating"),
        ("SYMBOL-AP-MIB", "dot1xAuthAuthTimeoutsWhileAuthenticating"),
        ("SYMBOL-AP-MIB", "dot1xAuthAuthFailWhileAuthenticating"),
        ("SYMBOL-AP-MIB", "dot1xAuthAuthReauthsWhileAuthenticating"),
        ("SYMBOL-AP-MIB", "dot1xAuthAuthEapStartsWhileAuthenticating"),
        ("SYMBOL-AP-MIB", "dot1xAuthAuthEapLogoffWhileAuthenticating"),
        ("SYMBOL-AP-MIB", "dot1xAuthAuthReauthsWhileAuthenticated"),
        ("SYMBOL-AP-MIB", "dot1xAuthAuthEapStartsWhileAuthenticated"),
        ("SYMBOL-AP-MIB", "dot1xAuthAuthEapLogoffWhileAuthenticated"),
        ("SYMBOL-AP-MIB", "dot1xAuthBackendResponses"),
        ("SYMBOL-AP-MIB", "dot1xAuthBackendAccessChallenges"),
        ("SYMBOL-AP-MIB", "dot1xAuthBackendOtherRequestsToSupplicant"),
        ("SYMBOL-AP-MIB", "dot1xAuthBackendNonNakResponsesFromSupplicant"),
        ("SYMBOL-AP-MIB", "dot1xAuthBackendAuthSuccesses"),
        ("SYMBOL-AP-MIB", "dot1xAuthBackendAuthFails"),
        ("SYMBOL-AP-MIB", "dot1xAuthSessionOctetsRx"),
        ("SYMBOL-AP-MIB", "dot1xAuthSessionOctetsTx"),
        ("SYMBOL-AP-MIB", "dot1xAuthSessionFramesRx"),
        ("SYMBOL-AP-MIB", "dot1xAuthSessionFramesTx"),
        ("SYMBOL-AP-MIB", "dot1xAuthSessionId"),
        ("SYMBOL-AP-MIB", "dot1xAuthSessionAuthenticMethod"),
        ("SYMBOL-AP-MIB", "dot1xAuthSessionTime"),
        ("SYMBOL-AP-MIB", "dot1xAuthSessionTerminateCause"),
        ("SYMBOL-AP-MIB", "dot1xAuthSessionUserName"))
)
if mibBuilder.loadTexts:
    dot1xGroup.setStatus("current")

apRfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 1000, 1, 2)
)
apRfGroup.setObjects(
      *(("SYMBOL-AP-MIB", "apRadioSettingsIndex"),
        ("SYMBOL-AP-MIB", "apRadioSettingsName"),
        ("SYMBOL-AP-MIB", "apRadioSettingsMacAddress"),
        ("SYMBOL-AP-MIB", "apRadioSettingsAntenna"),
        ("SYMBOL-AP-MIB", "apRadioSettingsShortPreamble"),
        ("SYMBOL-AP-MIB", "apRadioSettingsRtsThresh"),
        ("SYMBOL-AP-MIB", "apRadioSettingsBeaconInt"),
        ("SYMBOL-AP-MIB", "apRadioSettingsEnable"),
        ("SYMBOL-AP-MIB", "apRadioSettingsBand"),
        ("SYMBOL-AP-MIB", "apRadioSettingsPointersToWlans"),
        ("SYMBOL-AP-MIB", "apRadioCfgDesPlacement"),
        ("SYMBOL-AP-MIB", "apRadioCfgPosChannel"),
        ("SYMBOL-AP-MIB", "apRadioCfgDesChannel"),
        ("SYMBOL-AP-MIB", "apRadioCfgPosPowerLevel"),
        ("SYMBOL-AP-MIB", "apRadioCfgDesPowerLevel"),
        ("SYMBOL-AP-MIB", "apRadioCfgPowerInMW"),
        ("SYMBOL-AP-MIB", "apRadioCfgSet"),
        ("SYMBOL-AP-MIB", "apRadioCfgReset"),
        ("SYMBOL-AP-MIB", "apRadioCfgPlacement"),
        ("SYMBOL-AP-MIB", "apRadioCfgChannel"),
        ("SYMBOL-AP-MIB", "apRadioCfgPowerLevel"),
        ("SYMBOL-AP-MIB", "apRadioBssIndex"),
        ("SYMBOL-AP-MIB", "apRadioBssPrimaryWlan"),
        ("SYMBOL-AP-MIB", "apWlanMuAclPointerToAclPolicy"),
        ("SYMBOL-AP-MIB", "apRadioSettingsBasicRates"),
        ("SYMBOL-AP-MIB", "apRadioSettingsSupportedRates"),
        ("SYMBOL-AP-MIB", "apRadioSettingsBackgroundCwMin"),
        ("SYMBOL-AP-MIB", "apRadioSettingsBackgroundCwMax"),
        ("SYMBOL-AP-MIB", "apRadioSettingsBackgroundAifsn"),
        ("SYMBOL-AP-MIB", "apRadioSettingsBackgroundTxopsTime"),
        ("SYMBOL-AP-MIB", "apRadioSettingsBestEffortCwMin"),
        ("SYMBOL-AP-MIB", "apRadioSettingsBestEffortCwMax"),
        ("SYMBOL-AP-MIB", "apRadioSettingsBestEffortAifsn"),
        ("SYMBOL-AP-MIB", "apRadioSettingsBestEffortTxopsTime"),
        ("SYMBOL-AP-MIB", "apRadioSettingsVideoCwMin"),
        ("SYMBOL-AP-MIB", "apRadioSettingsVideoCwMax"),
        ("SYMBOL-AP-MIB", "apRadioSettingsVideoAifsn"),
        ("SYMBOL-AP-MIB", "apRadioSettingsVideoTxopsTime"),
        ("SYMBOL-AP-MIB", "apRadioSettingsVoiceCwMin"),
        ("SYMBOL-AP-MIB", "apRadioSettingsVoiceCwMax"),
        ("SYMBOL-AP-MIB", "apRadioSettingsVoiceAifsn"),
        ("SYMBOL-AP-MIB", "apRadioSettingsVoiceTxopsTime"),
        ("SYMBOL-AP-MIB", "apWlanIndex"),
        ("SYMBOL-AP-MIB", "apWlanName"),
        ("SYMBOL-AP-MIB", "apWlanEssid"),
        ("SYMBOL-AP-MIB", "apWlanEnable"),
        ("SYMBOL-AP-MIB", "apWlanUseRadio"),
        ("SYMBOL-AP-MIB", "apWlanMaxMus"),
        ("SYMBOL-AP-MIB", "apWlanAclPolicy"),
        ("SYMBOL-AP-MIB", "apWlanSecurityPolicy"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicy"),
        ("SYMBOL-AP-MIB", "apWlanAuthKerberosPassword"),
        ("SYMBOL-AP-MIB", "apWlanDisallowMuToMu"),
        ("SYMBOL-AP-MIB", "apWlanUseSecureBeacon"),
        ("SYMBOL-AP-MIB", "apWlanAnswerBroadcastEss"),
        ("SYMBOL-AP-MIB", "apWlanSecPolicyIndex"),
        ("SYMBOL-AP-MIB", "apWlanSecPolicyName"),
        ("SYMBOL-AP-MIB", "apWlanSecPolicyAuthentication"),
        ("SYMBOL-AP-MIB", "apWlanSecPolicyEncryption"),
        ("SYMBOL-AP-MIB", "apWlanAuthEapReauthenticationEnable"),
        ("SYMBOL-AP-MIB", "apWlanAuthEapReauthenticationPeriod"),
        ("SYMBOL-AP-MIB", "apWlanAuthEapReauthenticationMaxRetries"),
        ("SYMBOL-AP-MIB", "apWlanAuthEapRadius1Server"),
        ("SYMBOL-AP-MIB", "apWlanAuthEapRadius1Port"),
        ("SYMBOL-AP-MIB", "apWlanAuthEapRadius1SharedSecret"),
        ("SYMBOL-AP-MIB", "apWlanAuthEapRadius2Server"),
        ("SYMBOL-AP-MIB", "apWlanAuthEapRadius2Port"),
        ("SYMBOL-AP-MIB", "apWlanAuthEapRadius2SharedSecret"),
        ("SYMBOL-AP-MIB", "apWlanAuthEapMuQuietPeriod"),
        ("SYMBOL-AP-MIB", "apWlanAuthEapMuTimeout"),
        ("SYMBOL-AP-MIB", "apWlanAuthEapMuTxPeriod"),
        ("SYMBOL-AP-MIB", "apWlanAuthEapMuMaxRetries"),
        ("SYMBOL-AP-MIB", "apWlanAuthEapServerTimeout"),
        ("SYMBOL-AP-MIB", "apWlanAuthEapServerMaxRetries"),
        ("SYMBOL-AP-MIB", "apWlanAuthKerberosRealmName"),
        ("SYMBOL-AP-MIB", "apWlanAuthKerberosKdcServerIp1"),
        ("SYMBOL-AP-MIB", "apWlanAuthKerberosKdcPort1"),
        ("SYMBOL-AP-MIB", "apWlanAuthKerberosKdcServerIp2"),
        ("SYMBOL-AP-MIB", "apWlanAuthKerberosKdcPort2"),
        ("SYMBOL-AP-MIB", "apWlanAuthKerberosKdcServerIpR"),
        ("SYMBOL-AP-MIB", "apWlanAuthKerberosKdcPortR"),
        ("SYMBOL-AP-MIB", "apWlanCryptoWepPassKey"),
        ("SYMBOL-AP-MIB", "apWlanCryptoWepKey1"),
        ("SYMBOL-AP-MIB", "apWlanCryptoWepKey2"),
        ("SYMBOL-AP-MIB", "apWlanCryptoWepKey3"),
        ("SYMBOL-AP-MIB", "apWlanCryptoWepKey4"),
        ("SYMBOL-AP-MIB", "apWlanCryptoWepKeyToUse"),
        ("SYMBOL-AP-MIB", "apWlanCryptoTkipBcastKeyRotation"),
        ("SYMBOL-AP-MIB", "apWlanCryptoTkipKeyRotationInterval"),
        ("SYMBOL-AP-MIB", "apWlanCryptoTkipKeyToUse"),
        ("SYMBOL-AP-MIB", "apWlanCryptoTkipPassphrase"),
        ("SYMBOL-AP-MIB", "apWlanCryptoTkipKey"),
        ("SYMBOL-AP-MIB", "apWlanCryptoCcmpBcastKeyRotation"),
        ("SYMBOL-AP-MIB", "apWlanCryptoCcmpKeyRotationInterval"),
        ("SYMBOL-AP-MIB", "apWlanCryptoCcmpKeyToUse"),
        ("SYMBOL-AP-MIB", "apWlanCryptoCcmpPassphrase"),
        ("SYMBOL-AP-MIB", "apWlanCryptoCcmpKey"),
        ("SYMBOL-AP-MIB", "apWlanCryptoKeyguardKey1"),
        ("SYMBOL-AP-MIB", "apWlanCryptoKeyguardKey2"),
        ("SYMBOL-AP-MIB", "apWlanCryptoKeyguardKey3"),
        ("SYMBOL-AP-MIB", "apWlanCryptoKeyguardKey4"),
        ("SYMBOL-AP-MIB", "apWlanCryptoKeyguardKeyToUse"),
        ("SYMBOL-AP-MIB", "apWlanMuAclPolicyIndex"),
        ("SYMBOL-AP-MIB", "apWlanMuAclPolicyName"),
        ("SYMBOL-AP-MIB", "apWlanMuAclPolicyAccessMode"),
        ("SYMBOL-AP-MIB", "apWlanMuAclIndex"),
        ("SYMBOL-AP-MIB", "apWlanMuAclStartingMac"),
        ("SYMBOL-AP-MIB", "apWlanMuAclEndingMac"),
        ("SYMBOL-AP-MIB", "apWlanMuAclRowStatus"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicyIndex"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicyName"),
        ("SYMBOL-AP-MIB", "apWlanEnableWMM"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicyBackgroundCwMin"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicyBackgroundCwMax"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicyBackgroundAifsn"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicyBackgroundTxopsTime"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicyBestEffortCwMin"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicyBestEffortCwMax"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicyBestEffortAifsn"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicyBestEffortTxopsTime"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicyVideoCwMin"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicyVideoCwMax"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicyVideoAifsn"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicyVideoTxopsTime"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicyVoiceCwMin"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicyVoiceCwMax"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicyVoiceAifsn"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicyVoiceTxopsTime"),
        ("SYMBOL-AP-MIB", "apWlanVoicePrioritization"),
        ("SYMBOL-AP-MIB", "apWlanMulticastAddr1"),
        ("SYMBOL-AP-MIB", "apWlanVlanId"),
        ("SYMBOL-AP-MIB", "apWlanSecPolicyRowStatus"),
        ("SYMBOL-AP-MIB", "apWlanMulticastAddr2"),
        ("SYMBOL-AP-MIB", "apWlanAuthEapRadiusAcctMode"),
        ("SYMBOL-AP-MIB", "apWlanAuthEapRadiusAcctMuTimeout"),
        ("SYMBOL-AP-MIB", "apWlanAuthEapRadiusAcctMuRetries"),
        ("SYMBOL-AP-MIB", "apWlanAuthEapSyslogMode"),
        ("SYMBOL-AP-MIB", "apWlanAuthEapSyslogServerIp"),
        ("SYMBOL-AP-MIB", "apWlanSecPolicyPointerToWlan"),
        ("SYMBOL-AP-MIB", "apWlanMuAclPolicyPointerToWlan"),
        ("SYMBOL-AP-MIB", "apWlanMuAclPolicyRowStatus"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicyPointerToWlan"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicyBackgroundTxopsTimeInMS"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicyBestEffortTxopsTimeInMS"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicyVideoTxopsTimeInMS"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicyVoiceTxopsTimeInMS"),
        ("SYMBOL-AP-MIB", "apRadioSettingsBGMode"),
        ("SYMBOL-AP-MIB", "apRadioSettingsBackgroundTxopsTimeInMS"),
        ("SYMBOL-AP-MIB", "apRadioSettingsVideoTxopsTimeInMS"),
        ("SYMBOL-AP-MIB", "apRadioCfgDesPowerInMW"),
        ("SYMBOL-AP-MIB", "apWlanQosPolicyRowStatus"),
        ("SYMBOL-AP-MIB", "apWlanBwShareMode"),
        ("SYMBOL-AP-MIB", "apRadioE2BMapStatus"),
        ("SYMBOL-AP-MIB", "apRadioE2BMapStatusMessage"),
        ("SYMBOL-AP-MIB", "apWlanCryptoCcmpFastRoamPreAuth"),
        ("SYMBOL-AP-MIB", "apWlanCryptoCcmpMixedMode"),
        ("SYMBOL-AP-MIB", "apRadioCfgChannelMode"),
        ("SYMBOL-AP-MIB", "apWlanAuthKerberosUsername"),
        ("SYMBOL-AP-MIB", "apRadioWlanBssid"),
        ("SYMBOL-AP-MIB", "apRadioSettingsE2BMapMessage"),
        ("SYMBOL-AP-MIB", "apRadioCfgRfFunction"),
        ("SYMBOL-AP-MIB", "apIpFilterPolicyIndex"),
        ("SYMBOL-AP-MIB", "apIpFilterPolicyName"),
        ("SYMBOL-AP-MIB", "apIpFilterPolicyProtocol"),
        ("SYMBOL-AP-MIB", "apIpFilterPolicySrcStartIp"),
        ("SYMBOL-AP-MIB", "apIpFilterPolicySrcEndIp"),
        ("SYMBOL-AP-MIB", "apIpFilterPolicyDestStartIp"),
        ("SYMBOL-AP-MIB", "apIpFilterPolicyDestEndIp"),
        ("SYMBOL-AP-MIB", "apIpFilterPolicyUseStatus"),
        ("SYMBOL-AP-MIB", "apIpFilterPolicyRowStatus"),
        ("SYMBOL-AP-MIB", "apIpFilterWlanMode"),
        ("SYMBOL-AP-MIB", "apIpFilterWlanDefInAction"),
        ("SYMBOL-AP-MIB", "apIpFilterWlanDefOutAction"),
        ("SYMBOL-AP-MIB", "apIpFilterWlanPolicyIndex"),
        ("SYMBOL-AP-MIB", "apIpFilterWlanPolicyPolicy"),
        ("SYMBOL-AP-MIB", "apIpFilterWlanPolicyDirection"),
        ("SYMBOL-AP-MIB", "apIpFilterWlanPolicyAction"),
        ("SYMBOL-AP-MIB", "apIpFilterWlanPolicyRowStatus"),
        ("SYMBOL-AP-MIB", "apIpFilterLanMode"),
        ("SYMBOL-AP-MIB", "apIpFilterLanDefInAction"),
        ("SYMBOL-AP-MIB", "apIpFilterLanDefOutAction"),
        ("SYMBOL-AP-MIB", "apIpFilterLanPolicyIndex"),
        ("SYMBOL-AP-MIB", "apIpFilterLanPolicyPolicy"),
        ("SYMBOL-AP-MIB", "apIpFilterLanPolicyDirection"),
        ("SYMBOL-AP-MIB", "apIpFilterLanPolicyAction"),
        ("SYMBOL-AP-MIB", "apIpFilterLanPolicyRowStatus"),
        ("SYMBOL-AP-MIB", "apIpFilterLanIndex"),
        ("SYMBOL-AP-MIB", "apWlanMuIdleTimeout"),
        ("SYMBOL-AP-MIB", "apRadioCfgExceptionChannel"),
        ("SYMBOL-AP-MIB", "apRadioNSettingsMode"),
        ("SYMBOL-AP-MIB", "apRadioNSettingsHTProtectionStatus"),
        ("SYMBOL-AP-MIB", "apRadioNSettingsBasicRates"),
        ("SYMBOL-AP-MIB", "apRadioNCfgPosChannel"),
        ("SYMBOL-AP-MIB", "apRadioNCfgDesChannel"),
        ("SYMBOL-AP-MIB", "apRadioNCfgChannel"),
        ("SYMBOL-AP-MIB", "apRadioNCfgChannelWidth"),
        ("SYMBOL-AP-MIB", "apRadioNCfgAmsduAggregationMaxRecvSize"),
        ("SYMBOL-AP-MIB", "apRadioNCfgAmsduTransmitEnabled"),
        ("SYMBOL-AP-MIB", "apRadioNCfgAmpduAggregationMaxRecvSize"),
        ("SYMBOL-AP-MIB", "apRadioNCfgAmpduAggregationDensity"),
        ("SYMBOL-AP-MIB", "apRadioNCfgAmpduTransmitSizeLimit"),
        ("SYMBOL-AP-MIB", "apRadioNCfgShortGuardInterval"),
        ("SYMBOL-AP-MIB", "apRadioNCfgAmpduTransmitEnabled"),
        ("SYMBOL-AP-MIB", "apRadioNCfgChannelOffset"),
        ("SYMBOL-AP-MIB", "apRadioNMcsRateIndex"),
        ("SYMBOL-AP-MIB", "apRadioNMcsRate20MHzChanSgiDisabled"),
        ("SYMBOL-AP-MIB", "apRadioNMcsRate40MHzChanSgiDisabled"),
        ("SYMBOL-AP-MIB", "apRadioNMcsRate40MHzChanSgiEnabled"),
        ("SYMBOL-AP-MIB", "apRadioNMcsRateType"),
        ("SYMBOL-AP-MIB", "apRadioNMcsRateEnabled"),
        ("SYMBOL-AP-MIB", "apPowerMode"),
        ("SYMBOL-AP-MIB", "apPowerDefRadio"),
        ("SYMBOL-AP-MIB", "apPowerStatus"),
        ("SYMBOL-AP-MIB", "apIpFilterWlanInPackets"),
        ("SYMBOL-AP-MIB", "apIpFilterWlanOutPackets"),
        ("SYMBOL-AP-MIB", "apIpFilterWlanPolicyPackets"),
        ("SYMBOL-AP-MIB", "apIpFilterLanInPackets"),
        ("SYMBOL-AP-MIB", "apIpFilterLanOutPackets"),
        ("SYMBOL-AP-MIB", "apIpFilterLanPolicyPackets"),
        ("SYMBOL-AP-MIB", "apWlanVlanMode"),
        ("SYMBOL-AP-MIB", "apRadioSettingsBestEffortTxopsTimeInMS"),
        ("SYMBOL-AP-MIB", "apRadioSettingsVoiceTxopsTimeInMS"),
        ("SYMBOL-AP-MIB", "apRadioE2BMapStatusBcMcEncCipher"),
        ("SYMBOL-AP-MIB", "apWlanCryptoKeyguardPassKey"),
        ("SYMBOL-AP-MIB", "apIpFilterPolicyStartPort"),
        ("SYMBOL-AP-MIB", "apIpFilterPolicyEndPort"),
        ("SYMBOL-AP-MIB", "apIpFilterPolicySrcStartPort"),
        ("SYMBOL-AP-MIB", "apIpFilterPolicySrcEndPort"))
)
if mibBuilder.loadTexts:
    apRfGroup.setStatus("current")

apSwitchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 1000, 1, 3)
)
apSwitchGroup.setObjects(
      *(("SYMBOL-AP-MIB", "apVlanIndex"),
        ("SYMBOL-AP-MIB", "apVlanId"),
        ("SYMBOL-AP-MIB", "apVlanRowStatus"),
        ("SYMBOL-AP-MIB", "apVlanPointerToWlan"),
        ("SYMBOL-AP-MIB", "apVlanName"),
        ("SYMBOL-AP-MIB", "apWnmpPingDestMu"),
        ("SYMBOL-AP-MIB", "apWnmpPingDestAP"),
        ("SYMBOL-AP-MIB", "apWnmpPingDest"),
        ("SYMBOL-AP-MIB", "apWnmpPingNum"),
        ("SYMBOL-AP-MIB", "apWnmpPingPacketLength"),
        ("SYMBOL-AP-MIB", "apWnmpPingPacketData"),
        ("SYMBOL-AP-MIB", "apWnmpPingAction"),
        ("SYMBOL-AP-MIB", "apWnmpPingNumResponses"),
        ("SYMBOL-AP-MIB", "apFlashLedDestAP"),
        ("SYMBOL-AP-MIB", "apFlashLedAction"),
        ("SYMBOL-AP-MIB", "apKnownApMac"),
        ("SYMBOL-AP-MIB", "apKnownApIndex"),
        ("SYMBOL-AP-MIB", "apKnownApIp"),
        ("SYMBOL-AP-MIB", "apKnownApMu"),
        ("SYMBOL-AP-MIB", "apKnownApType"),
        ("SYMBOL-AP-MIB", "apKnownApUnitName"),
        ("SYMBOL-AP-MIB", "apKnownApPktsPerSec"),
        ("SYMBOL-AP-MIB", "apSubnetDhcpState"),
        ("SYMBOL-AP-MIB", "apLan802dt1xAuthLogin"),
        ("SYMBOL-AP-MIB", "apLan802dt1xAuthPass"),
        ("SYMBOL-AP-MIB", "apKnownApKbPerSec"),
        ("SYMBOL-AP-MIB", "apKnownApFwVers"),
        ("SYMBOL-AP-MIB", "apLanTypeFilterIndex"),
        ("SYMBOL-AP-MIB", "apLanTypeFilter"),
        ("SYMBOL-AP-MIB", "apLanTypeFilterRowStatus"),
        ("SYMBOL-AP-MIB", "apWanVpnKeyAutoSALifeTime"),
        ("SYMBOL-AP-MIB", "apLanTimeOutValue"),
        ("SYMBOL-AP-MIB", "apLanTimeOut"),
        ("SYMBOL-AP-MIB", "apKnownApEssName"),
        ("SYMBOL-AP-MIB", "apKnownApRadioType1"),
        ("SYMBOL-AP-MIB", "apKnownApRadioType2"),
        ("SYMBOL-AP-MIB", "apKnownApChannel1"),
        ("SYMBOL-AP-MIB", "apKnownApChannel2"),
        ("SYMBOL-AP-MIB", "apKnownApSendCfgStatus"),
        ("SYMBOL-AP-MIB", "apKnownApSendCfg"))
)
if mibBuilder.loadTexts:
    apSwitchGroup.setStatus("current")

apTrapCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 1000, 1, 4)
)
apTrapCtrlGroup.setObjects(
      *(("SYMBOL-AP-MIB", "apTrapCtrlRateLimit"),
        ("SYMBOL-AP-MIB", "apTrapCtrlSumStatsIndex"),
        ("SYMBOL-AP-MIB", "apTrapCtrlSumStatsDescr"),
        ("SYMBOL-AP-MIB", "apTrapCtrlSumStatsUnits"),
        ("SYMBOL-AP-MIB", "apTrapCtrlSumStatsCanBeSetMu"),
        ("SYMBOL-AP-MIB", "apTrapCtrlSumStatsThresholdMu"),
        ("SYMBOL-AP-MIB", "apTrapCtrlSumStatsCanBeSetRadioA"),
        ("SYMBOL-AP-MIB", "apTrapCtrlSumStatsThresholdRadioA"),
        ("SYMBOL-AP-MIB", "apTrapCtrlSumStatsCanBeSetRadioBG"),
        ("SYMBOL-AP-MIB", "apTrapCtrlSumStatsThresholdRadioBG"),
        ("SYMBOL-AP-MIB", "apTrapCtrlSumStatsCanBeSetWlan"),
        ("SYMBOL-AP-MIB", "apTrapCtrlSumStatsThresholdWlans"),
        ("SYMBOL-AP-MIB", "apTrapCtrlSumStatsCanBeSetAccessPoint"),
        ("SYMBOL-AP-MIB", "apTrapCtrlSumStatsThresholdAccessPoint"),
        ("SYMBOL-AP-MIB", "apTrapCtrlEnableIndex"),
        ("SYMBOL-AP-MIB", "apTrapCtrlEnableName"),
        ("SYMBOL-AP-MIB", "apTrapCtrlEnable"),
        ("SYMBOL-AP-MIB", "apTrapRadioMac"),
        ("SYMBOL-AP-MIB", "apTrapLanMonitorReason"),
        ("SYMBOL-AP-MIB", "apTrapWpaCounterMeasureEssid"),
        ("SYMBOL-AP-MIB", "apTrapCtrlSumStatsCanBeSetRadioN2400MHz"),
        ("SYMBOL-AP-MIB", "apTrapCtrlSumStatsThresholdRadioN2400MHz"),
        ("SYMBOL-AP-MIB", "apTrapCtrlSumStatsCanBeSetRadioN5000MHz"),
        ("SYMBOL-AP-MIB", "apTrapCtrlSumStatsThresholdRadioN5000MHz"),
        ("SYMBOL-AP-MIB", "apTrapLanMonitorMode"),
        ("SYMBOL-AP-MIB", "apTrapMuMac"))
)
if mibBuilder.loadTexts:
    apTrapCtrlGroup.setStatus("current")

apRapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 1000, 1, 5)
)
apRapGroup.setObjects(
    ("SYMBOL-AP-MIB", "apRapDetectorMode")
)
if mibBuilder.loadTexts:
    apRapGroup.setStatus("current")

apLoadCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 1000, 1, 6)
)
apLoadCfgGroup.setObjects(
      *(("SYMBOL-AP-MIB", "apLoadCfgOperation"),
        ("SYMBOL-AP-MIB", "apLoadCfgServerPath"),
        ("SYMBOL-AP-MIB", "apLoadCfgServerFilename"),
        ("SYMBOL-AP-MIB", "apLoadCfgServerIpAddr"),
        ("SYMBOL-AP-MIB", "apLoadCfgFtpUsername"),
        ("SYMBOL-AP-MIB", "apLoadCfgFtpPassword"),
        ("SYMBOL-AP-MIB", "apLoadCfgStart"),
        ("SYMBOL-AP-MIB", "apLoadCfgOperationsDone"),
        ("SYMBOL-AP-MIB", "apLoadCfgResult"),
        ("SYMBOL-AP-MIB", "apLoadCfgSuccess"))
)
if mibBuilder.loadTexts:
    apLoadCfgGroup.setStatus("current")

apStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 1000, 1, 7)
)
apStatsGroup.setObjects(
      *(("SYMBOL-AP-MIB", "apWanClearStats"),
        ("SYMBOL-AP-MIB", "apLanClearStats"),
        ("SYMBOL-AP-MIB", "apRadioClearStats"),
        ("SYMBOL-AP-MIB", "apWlanClearStats"),
        ("SYMBOL-AP-MIB", "apMuClearStats"),
        ("SYMBOL-AP-MIB", "apKnownAPClearStats"),
        ("SYMBOL-AP-MIB", "apDiagRamTotal"),
        ("SYMBOL-AP-MIB", "apnRadioStatsIndex"),
        ("SYMBOL-AP-MIB", "apnRadioStatsBssid"),
        ("SYMBOL-AP-MIB", "apnRadioStatsApSsid"),
        ("SYMBOL-AP-MIB", "apnRadioStatsChannel"),
        ("SYMBOL-AP-MIB", "apnRadioStatsExtnChannel"),
        ("SYMBOL-AP-MIB", "apnRadioStatsRssiAvgAcrossAntennas"),
        ("SYMBOL-AP-MIB", "apnRadioStatsChannelWidthMode"),
        ("SYMBOL-AP-MIB", "apnRadioStatsOpFreq"),
        ("SYMBOL-AP-MIB", "apnRadioStatsNumPktsRxSGI400ns"),
        ("SYMBOL-AP-MIB", "apnRadioStatsNumPktsRxSGI800ns"),
        ("SYMBOL-AP-MIB", "apnRadioStatsNumPktsTxSGI400ns"),
        ("SYMBOL-AP-MIB", "apnRadioStatsNumPktsTxSGI800ns"),
        ("SYMBOL-AP-MIB", "apnRadioStatsNumPktsRxChanWidth20MHz"),
        ("SYMBOL-AP-MIB", "apnRadioStatsNumPktsRxChanWidth40MHz"),
        ("SYMBOL-AP-MIB", "apnRadioStatsNumPktsTxChanWidth20MHz"),
        ("SYMBOL-AP-MIB", "apnRadioStatsNumPktsTxChanWidth40MHz"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAt1Mb"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAt2Mb"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAt5pt5Mb"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAt6Mb"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAt9Mb"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAt11Mb"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAt12Mb"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAt18Mb"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAt24Mb"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAt36Mb"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAt48Mb"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAt54Mb"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAtMCS0"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAtMCS1"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAtMCS2"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAtMCS3"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAtMCS4"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAtMCS5"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAtMCS6"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAtMCS7"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAtMCS8"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAtMCS9"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAtMCS10"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAtMCS11"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAtMCS12"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAtMCS13"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAtMCS14"),
        ("SYMBOL-AP-MIB", "apnPortalRxPktsAtMCS15"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAt1Mb"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAt2Mb"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAt5pt5Mb"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAt6Mb"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAt9Mb"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAt11Mb"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAt12Mb"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAt18Mb"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAt24Mb"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAt36Mb"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAt48Mb"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAt54Mb"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAtMCS0"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAtMCS1"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAtMCS2"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAtMCS3"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAtMCS4"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAtMCS5"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAtMCS6"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAtMCS7"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAtMCS8"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAtMCS9"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAtMCS10"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAtMCS11"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAtMCS12"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAtMCS13"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAtMCS14"),
        ("SYMBOL-AP-MIB", "apnPortalTxPktsAtMCS15"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAt1Mb"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAt2Mb"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAt5pt5Mb"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAt6Mb"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAt9Mb"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAt11Mb"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAt12Mb"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAt18Mb"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAt24Mb"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAt36Mb"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAt48Mb"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAt54Mb"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAtMCS0"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAtMCS1"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAtMCS2"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAtMCS3"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAtMCS4"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAtMCS5"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAtMCS6"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAtMCS7"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAtMCS8"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAtMCS9"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAtMCS10"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAtMCS11"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAtMCS12"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAtMCS13"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAtMCS14"),
        ("SYMBOL-AP-MIB", "apnPortalRxOctetsAtMCS15"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAt1Mb"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAt2Mb"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAt5pt5Mb"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAt6Mb"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAt9Mb"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAt11Mb"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAt12Mb"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAt18Mb"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAt24Mb"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAt36Mb"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAt48Mb"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAt54Mb"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAtMCS0"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAtMCS1"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAtMCS2"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAtMCS3"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAtMCS4"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAtMCS5"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAtMCS6"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAtMCS7"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAtMCS8"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAtMCS9"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAtMCS10"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAtMCS11"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAtMCS12"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAtMCS13"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAtMCS14"),
        ("SYMBOL-AP-MIB", "apnPortalTxOctetsAtMCS15"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAt1Mb"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAt2Mb"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAt5pt5Mb"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAt6Mb"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAt9Mb"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAt11Mb"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAt12Mb"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAt18Mb"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAt24Mb"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAt36Mb"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAt48Mb"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAt54Mb"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAtMCS0"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAtMCS1"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAtMCS2"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAtMCS3"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAtMCS4"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAtMCS5"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAtMCS6"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAtMCS7"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAtMCS8"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAtMCS9"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAtMCS10"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAtMCS11"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAtMCS12"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAtMCS13"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAtMCS14"),
        ("SYMBOL-AP-MIB", "apnMuRxPktsAtMCS15"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAt1Mb"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAt2Mb"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAt5pt5Mb"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAt6Mb"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAt9Mb"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAt11Mb"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAt12Mb"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAt18Mb"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAt24Mb"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAt36Mb"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAt48Mb"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAt54Mb"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAtMCS0"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAtMCS1"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAtMCS2"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAtMCS3"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAtMCS4"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAtMCS5"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAtMCS6"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAtMCS7"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAtMCS8"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAtMCS9"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAtMCS10"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAtMCS11"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAtMCS12"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAtMCS13"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAtMCS14"),
        ("SYMBOL-AP-MIB", "apnMuTxPktsAtMCS15"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAt1Mb"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAt2Mb"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAt5pt5Mb"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAt6Mb"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAt9Mb"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAt11Mb"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAt12Mb"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAt18Mb"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAt24Mb"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAt36Mb"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAt48Mb"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAt54Mb"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAtMCS0"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAtMCS1"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAtMCS2"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAtMCS3"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAtMCS4"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAtMCS5"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAtMCS6"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAtMCS7"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAtMCS8"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAtMCS9"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAtMCS10"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAtMCS11"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAtMCS12"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAtMCS13"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAtMCS14"),
        ("SYMBOL-AP-MIB", "apnMuRxOctetsAtMCS15"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAt1Mb"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAt2Mb"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAt5pt5Mb"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAt6Mb"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAt9Mb"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAt11Mb"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAt12Mb"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAt18Mb"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAt24Mb"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAt36Mb"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAt48Mb"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAt54Mb"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAtMCS0"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAtMCS1"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAtMCS2"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAtMCS3"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAtMCS4"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAtMCS5"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAtMCS6"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAtMCS7"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAtMCS8"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAtMCS9"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAtMCS10"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAtMCS11"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAtMCS12"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAtMCS13"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAtMCS14"),
        ("SYMBOL-AP-MIB", "apnMuTxOctetsAtMCS15"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAt1Mb"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAt2Mb"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAt5pt5Mb"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAt6Mb"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAt9Mb"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAt11Mb"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAt12Mb"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAt18Mb"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAt24Mb"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAt36Mb"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAt48Mb"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAt54Mb"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAtMCS0"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAtMCS1"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAtMCS2"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAtMCS3"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAtMCS4"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAtMCS5"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAtMCS6"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAtMCS7"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAtMCS8"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAtMCS9"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAtMCS10"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAtMCS11"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAtMCS12"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAtMCS13"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAtMCS14"),
        ("SYMBOL-AP-MIB", "apnWlanRxPktsAtMCS15"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAt1Mb"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAt2Mb"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAt5pt5Mb"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAt6Mb"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAt9Mb"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAt11Mb"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAt12Mb"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAt18Mb"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAt24Mb"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAt36Mb"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAt48Mb"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAt54Mb"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAtMCS0"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAtMCS1"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAtMCS2"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAtMCS3"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAtMCS4"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAtMCS5"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAtMCS6"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAtMCS7"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAtMCS8"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAtMCS9"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAtMCS10"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAtMCS11"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAtMCS12"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAtMCS13"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAtMCS14"),
        ("SYMBOL-AP-MIB", "apnWlanTxPktsAtMCS15"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAt1Mb"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAt2Mb"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAt5pt5Mb"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAt6Mb"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAt9Mb"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAt11Mb"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAt12Mb"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAt18Mb"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAt24Mb"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAt36Mb"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAt48Mb"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAt54Mb"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAtMCS0"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAtMCS1"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAtMCS2"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAtMCS3"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAtMCS4"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAtMCS5"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAtMCS6"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAtMCS7"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAtMCS8"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAtMCS9"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAtMCS10"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAtMCS11"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAtMCS12"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAtMCS13"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAtMCS14"),
        ("SYMBOL-AP-MIB", "apnWlanRxOctetsAtMCS15"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAt1Mb"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAt2Mb"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAt5pt5Mb"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAt6Mb"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAt9Mb"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAt11Mb"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAt12Mb"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAt18Mb"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAt24Mb"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAt36Mb"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAt48Mb"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAt54Mb"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAtMCS0"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAtMCS1"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAtMCS2"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAtMCS3"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAtMCS4"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAtMCS5"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAtMCS6"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAtMCS7"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAtMCS8"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAtMCS9"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAtMCS10"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAtMCS11"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAtMCS12"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAtMCS13"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAtMCS14"),
        ("SYMBOL-AP-MIB", "apnWlanTxOctetsAtMCS15"),
        ("SYMBOL-AP-MIB", "apLanRxDropped"),
        ("SYMBOL-AP-MIB", "apLanRxFrameErrors"),
        ("SYMBOL-AP-MIB", "apLanInfoSpeed"),
        ("SYMBOL-AP-MIB", "apLanInfoDuplexMode"),
        ("SYMBOL-AP-MIB", "apLanRxPkts"),
        ("SYMBOL-AP-MIB", "apLanRxBytes"),
        ("SYMBOL-AP-MIB", "apLanRxErrors"),
        ("SYMBOL-AP-MIB", "apLanInfoIndex"),
        ("SYMBOL-AP-MIB", "apLanInfoEnabled"),
        ("SYMBOL-AP-MIB", "apLanInfoIpAddress"),
        ("SYMBOL-AP-MIB", "apLanInfoNetworkMask"),
        ("SYMBOL-AP-MIB", "apLanInfoEthernetAddress"),
        ("SYMBOL-AP-MIB", "apLanTxPkts"),
        ("SYMBOL-AP-MIB", "apLanTxBytes"),
        ("SYMBOL-AP-MIB", "apLanTxErrors"),
        ("SYMBOL-AP-MIB", "apLanTxDropped"),
        ("SYMBOL-AP-MIB", "apLanTxFrameErrors"),
        ("SYMBOL-AP-MIB", "apDiagRamUsed"),
        ("SYMBOL-AP-MIB", "apDiagCpuLoad1Min"),
        ("SYMBOL-AP-MIB", "apDiagCpuLoad5Min"),
        ("SYMBOL-AP-MIB", "apDiagCpuLoad15Min"),
        ("SYMBOL-AP-MIB", "apDiagRamPercentageUsed"))
)
if mibBuilder.loadTexts:
    apStatsGroup.setStatus("current")

apGroupV1dot1variables = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 1000, 2, 1)
)
apGroupV1dot1variables.setObjects(
      *(("SYMBOL-AP-MIB", "apSubnetTypeFilterAccessMode"),
        ("SYMBOL-AP-MIB", "apSubnetVlanEnable"),
        ("SYMBOL-AP-MIB", "apLanTypeFilterSubnetIndex"),
        ("SYMBOL-AP-MIB", "apMgmtAccessToAllow"),
        ("SYMBOL-AP-MIB", "apTrapCtrlMuMac"),
        ("SYMBOL-AP-MIB", "apTrapCtrlMuHotspotStateChange"),
        ("SYMBOL-AP-MIB", "apHotSpotDefaultFileMode"),
        ("SYMBOL-AP-MIB", "apHotSpotExternalLoginPageUrl"),
        ("SYMBOL-AP-MIB", "apHotSpotExternalWelomePageUrl"),
        ("SYMBOL-AP-MIB", "apHotSpotExternalFailPageUrl"),
        ("SYMBOL-AP-MIB", "apHotSpotRadiusAcctMode"),
        ("SYMBOL-AP-MIB", "apHotSpotRadiusAcctTimeout"),
        ("SYMBOL-AP-MIB", "apHotSpotRadiusAcctRetryCount"),
        ("SYMBOL-AP-MIB", "apHotSpotPriRadiusServerIp"),
        ("SYMBOL-AP-MIB", "apHotSpotPriRadiusPort"),
        ("SYMBOL-AP-MIB", "apHotSpotPriRadiusSecret"),
        ("SYMBOL-AP-MIB", "apHotSpotSecRadiusServerIp"),
        ("SYMBOL-AP-MIB", "apHotSpotSecRadiusPort"),
        ("SYMBOL-AP-MIB", "apHotSpotSecRadiusSecret"),
        ("SYMBOL-AP-MIB", "apHotSpotWhiteListIndex"),
        ("SYMBOL-AP-MIB", "apHotSpotWhiteListWalledGardenIp"),
        ("SYMBOL-AP-MIB", "apHotSpotWhiteListRowStatus"),
        ("SYMBOL-AP-MIB", "apLanEthernetPort"),
        ("SYMBOL-AP-MIB", "apWlanSubnet"),
        ("SYMBOL-AP-MIB", "apRouterDefaultGatewayInterface"),
        ("SYMBOL-AP-MIB", "apWlanAuthEapRadiusExtAcctServer"),
        ("SYMBOL-AP-MIB", "apWlanAuthEapRadiusExtPort"),
        ("SYMBOL-AP-MIB", "apWlanAuthEapRadiusExtSharedSecret"),
        ("SYMBOL-AP-MIB", "apManualCurrSystemDateTime"),
        ("SYMBOL-AP-MIB", "apManualTimeZoneIndex"),
        ("SYMBOL-AP-MIB", "apManualTimeZoneName"),
        ("SYMBOL-AP-MIB", "apManualExpectedTimeZone"),
        ("SYMBOL-AP-MIB", "apHotSpotRadiusAcctServerIp"),
        ("SYMBOL-AP-MIB", "apHotSpotRadiusAcctPort"),
        ("SYMBOL-AP-MIB", "apHotSpotRadiusAcctSecret"),
        ("SYMBOL-AP-MIB", "apRadioSettingsERPProtectionStatus"),
        ("SYMBOL-AP-MIB", "apWlanClientBackHaul"),
        ("SYMBOL-AP-MIB", "apKnownApIndex"),
        ("SYMBOL-AP-MIB", "apKnownApRadio1ClientBridgeMac1"),
        ("SYMBOL-AP-MIB", "apKnownApRadio1ClientBridgeMac2"),
        ("SYMBOL-AP-MIB", "apKnownApRadio1ClientBridgeMac3"),
        ("SYMBOL-AP-MIB", "apKnownApRadio2ClientBridgeMac1"),
        ("SYMBOL-AP-MIB", "apKnownApRadio2ClientBridgeMac2"),
        ("SYMBOL-AP-MIB", "apKnownApRadio2ClientBridgeMac3"),
        ("SYMBOL-AP-MIB", "apWanPppoeClientIndex"),
        ("SYMBOL-AP-MIB", "apWanPppoeClientIp"),
        ("SYMBOL-AP-MIB", "apWanPppoeClientGateway"),
        ("SYMBOL-AP-MIB", "apWanPppoeClientPrimaryDNSServer"),
        ("SYMBOL-AP-MIB", "apWanPppoeClientSecondaryDNSServer"),
        ("SYMBOL-AP-MIB", "apSubnetAdminVlanTag"),
        ("SYMBOL-AP-MIB", "apSubnetNativeVlanTag"),
        ("SYMBOL-AP-MIB", "apRadioBssDtimPrd"),
        ("SYMBOL-AP-MIB", "apWlanHotspot"),
        ("SYMBOL-AP-MIB", "apManualTimeZoneSet"),
        ("SYMBOL-AP-MIB", "apManualExpectedYear"),
        ("SYMBOL-AP-MIB", "apManualExpectedMonth"),
        ("SYMBOL-AP-MIB", "apManualExpectedDay"),
        ("SYMBOL-AP-MIB", "apManualExpectedHour"),
        ("SYMBOL-AP-MIB", "apManualExpectedMinutes"),
        ("SYMBOL-AP-MIB", "apManualExpectedSeconds"),
        ("SYMBOL-AP-MIB", "apManualDateTimeSet"),
        ("SYMBOL-AP-MIB", "apWlanWMMQosParam"),
        ("SYMBOL-AP-MIB", "apRadioSettingsWMMQosParam"),
        ("SYMBOL-AP-MIB", "apRadioMeshBaseBridgeMode"),
        ("SYMBOL-AP-MIB", "apRadioMeshMaxClients"),
        ("SYMBOL-AP-MIB", "apRadioMeshClientBridgeMode"),
        ("SYMBOL-AP-MIB", "apRadioMeshWlanPtr"),
        ("SYMBOL-AP-MIB", "apLanBridgePriority"),
        ("SYMBOL-AP-MIB", "apLanBridgeMaxMsgAge"),
        ("SYMBOL-AP-MIB", "apMeshStatsIndex"),
        ("SYMBOL-AP-MIB", "apMeshStatsConnType"),
        ("SYMBOL-AP-MIB", "apMeshStatsMac"),
        ("SYMBOL-AP-MIB", "apMeshStatsWlanPtr"),
        ("SYMBOL-AP-MIB", "apMeshStatsRadioType"),
        ("SYMBOL-AP-MIB", "apMeshStatsThroughput"),
        ("SYMBOL-AP-MIB", "apMeshStatsAvgBitSpeed"),
        ("SYMBOL-AP-MIB", "apMeshStatsRetries"),
        ("SYMBOL-AP-MIB", "apMeshBridgeStatsIndex"),
        ("SYMBOL-AP-MIB", "apMeshBridgeStatsMac"),
        ("SYMBOL-AP-MIB", "apMeshBridgeStatsWlanPtr"),
        ("SYMBOL-AP-MIB", "apMeshBridgeStatsLanPtr"),
        ("SYMBOL-AP-MIB", "apMeshBridgeStatsRadioType"),
        ("SYMBOL-AP-MIB", "apMeshBridgeStatsAuthType"),
        ("SYMBOL-AP-MIB", "apMeshBridgeStatsEncType"),
        ("SYMBOL-AP-MIB", "apMeshBridgeStatsPktsPerSecRx"),
        ("SYMBOL-AP-MIB", "apMeshBridgeStatsPksPerSecTx"),
        ("SYMBOL-AP-MIB", "apMeshBridgeStatsPktsPerSecTotal"),
        ("SYMBOL-AP-MIB", "apMeshBridgeStatsThroughputRx"),
        ("SYMBOL-AP-MIB", "apMeshBridgeStatsThroughputTx"),
        ("SYMBOL-AP-MIB", "apMeshBridgeStatsThroughputTotal"),
        ("SYMBOL-AP-MIB", "apMeshBridgeStatsAvgBitSpeed"),
        ("SYMBOL-AP-MIB", "apMeshBridgeStatsAvgMuSignal"),
        ("SYMBOL-AP-MIB", "apMeshBridgeStatsAvgMuNoise"),
        ("SYMBOL-AP-MIB", "apMeshBridgeStatsAvgMuSnr"),
        ("SYMBOL-AP-MIB", "apMeshBridgeStatsAvgRetries"),
        ("SYMBOL-AP-MIB", "apMeshBridgeStatsPktsDropped"),
        ("SYMBOL-AP-MIB", "apLanSTPStatsDesignatedRoot"),
        ("SYMBOL-AP-MIB", "apLanSTPStatsBridgeId"),
        ("SYMBOL-AP-MIB", "apLanSTPStatsRootPort"),
        ("SYMBOL-AP-MIB", "apLanSTPStatsRootPathCost"),
        ("SYMBOL-AP-MIB", "apLanSTPStatsBridgeMaxMsgAge"),
        ("SYMBOL-AP-MIB", "apLanSTPStatsBridgeHelloTime"),
        ("SYMBOL-AP-MIB", "apLanSTPStatsBridgeFwDelay"),
        ("SYMBOL-AP-MIB", "apLanSTPStatsPortIntfLanIndex"),
        ("SYMBOL-AP-MIB", "apLanSTPStatsPortIntfPortIndex"),
        ("SYMBOL-AP-MIB", "apLanSTPStatsPortIntfPortName"),
        ("SYMBOL-AP-MIB", "apLanSTPStatsPortIntfState"),
        ("SYMBOL-AP-MIB", "apLanSTPStatsPortIntfPathCost"),
        ("SYMBOL-AP-MIB", "apLanSTPStatsPortIntfDsgRoot"),
        ("SYMBOL-AP-MIB", "apLanSTPStatsPortIntfDsgBridge"),
        ("SYMBOL-AP-MIB", "apLanSTPStatsPortIntfDsgPort"),
        ("SYMBOL-AP-MIB", "apLanSTPStatsPortIntfDsgCost"),
        ("SYMBOL-AP-MIB", "apWlanCryptoKeyguardMixedMode"),
        ("SYMBOL-AP-MIB", "apWlanCryptoWepMixedMode"),
        ("SYMBOL-AP-MIB", "apRadioMeshConnAutoSelect"),
        ("SYMBOL-AP-MIB", "apRadioMeshAvailableConnIndex"),
        ("SYMBOL-AP-MIB", "apRadioMeshAvailableConnMac"),
        ("SYMBOL-AP-MIB", "apRadioMeshAvailableConnChannel"),
        ("SYMBOL-AP-MIB", "apRadioMeshAvailableConnRssi"),
        ("SYMBOL-AP-MIB", "apRadioMeshPreferredConnPriority"),
        ("SYMBOL-AP-MIB", "apRadioMeshPreferredConnMac"),
        ("SYMBOL-AP-MIB", "apRadioMeshPreferredConnRowStatus"),
        ("SYMBOL-AP-MIB", "apRadioMeshPreferredConnIndex"),
        ("SYMBOL-AP-MIB", "apTrapVlanId"),
        ("SYMBOL-AP-MIB", "apHotSpotRadiusSessMode"),
        ("SYMBOL-AP-MIB", "apHotSpotRadiusSessTimeout"),
        ("SYMBOL-AP-MIB", "apLanPortDuplex"),
        ("SYMBOL-AP-MIB", "apLanPortSpeed"),
        ("SYMBOL-AP-MIB", "apLanPortAutoNegotiation"),
        ("SYMBOL-AP-MIB", "apWanPortDuplex"),
        ("SYMBOL-AP-MIB", "apWanPortSpeed"),
        ("SYMBOL-AP-MIB", "apWanPortAutoNegotiation"),
        ("SYMBOL-AP-MIB", "apRadioMeshTimeout"),
        ("SYMBOL-AP-MIB", "apRadioMeshTimeoutValue"),
        ("SYMBOL-AP-MIB", "apWlanCryptoTkipFastRoamPreAuth"),
        ("SYMBOL-AP-MIB", "apWlanCryptoTkipAllowWpa2Client"),
        ("SYMBOL-AP-MIB", "apWanDynDNSMode"),
        ("SYMBOL-AP-MIB", "apWanDynDNSUsername"),
        ("SYMBOL-AP-MIB", "apWanDynDNSPassword"),
        ("SYMBOL-AP-MIB", "apWanDynDNSHostname"),
        ("SYMBOL-AP-MIB", "apWanDynDNSIndex"),
        ("SYMBOL-AP-MIB", "apWanDynDNSUpdateHostname"),
        ("SYMBOL-AP-MIB", "apWanDynDNSUpdateIp"),
        ("SYMBOL-AP-MIB", "apWanDynDNSUpdateStatus"),
        ("SYMBOL-AP-MIB", "apWanDynDNSUpdateResponseIndex"),
        ("SYMBOL-AP-MIB", "apWanDynDNSPerformUpdate"),
        ("SYMBOL-AP-MIB", "apTrapCtrlDynDNSUpdateIp"),
        ("SYMBOL-AP-MIB", "apTrapCtrlDynDNSUpdateHostname"),
        ("SYMBOL-AP-MIB", "apTrapCtrlDynDNSUpdateStatus"),
        ("SYMBOL-AP-MIB", "apLoginMessageMode"),
        ("SYMBOL-AP-MIB", "apLoginMessageText"),
        ("SYMBOL-AP-MIB", "apRadioSettingsQBSSChannelBeaconInt"),
        ("SYMBOL-AP-MIB", "apRadioWlanWeight"),
        ("SYMBOL-AP-MIB", "apRadiusUsersGroup"),
        ("SYMBOL-AP-MIB", "apRadiusUsersGroupRowStatus"),
        ("SYMBOL-AP-MIB", "apRadiusUsersGroupId"),
        ("SYMBOL-AP-MIB", "apRadiusAccessWlanPtrs"),
        ("SYMBOL-AP-MIB", "apRadiusAccessTimeRule"),
        ("SYMBOL-AP-MIB", "apRadioSettingsQBSSLoadElementMode"),
        ("SYMBOL-AP-MIB", "apRapDetectorABGMode"),
        ("SYMBOL-AP-MIB", "apMeshBridgeStatsUndecryptablePkts"),
        ("SYMBOL-AP-MIB", "apLanBridgeHelloTime"),
        ("SYMBOL-AP-MIB", "apLanBridgeFwdDelay"),
        ("SYMBOL-AP-MIB", "apLanBridgeEntryAgeout"),
        ("SYMBOL-AP-MIB", "apAapSwitchDiscoveryIPAddressRowStatus"),
        ("SYMBOL-AP-MIB", "apAapSwitchDiscoveryIPAddress"),
        ("SYMBOL-AP-MIB", "apAapSwitchDiscoveryIPAddressIndex"),
        ("SYMBOL-AP-MIB", "apAapSwitchDiscoveryPort"),
        ("SYMBOL-AP-MIB", "apAapSwitchDiscoveryInterface"),
        ("SYMBOL-AP-MIB", "apAapSwitchDiscoveryDomainName"),
        ("SYMBOL-AP-MIB", "apAapTunnelToSwitchEnable"),
        ("SYMBOL-AP-MIB", "apAapAcKeepAlive"),
        ("SYMBOL-AP-MIB", "apAapAdoptionState"),
        ("SYMBOL-AP-MIB", "apAapAdoptingSwitchIP"),
        ("SYMBOL-AP-MIB", "apMuLocationingIndex"),
        ("SYMBOL-AP-MIB", "apMuLocationingMuMac"),
        ("SYMBOL-AP-MIB", "apMuLocationingPortalMac"),
        ("SYMBOL-AP-MIB", "apMuLocationingSignalStrength"),
        ("SYMBOL-AP-MIB", "apMuLocationingHeardChannel"),
        ("SYMBOL-AP-MIB", "apMuLocationingHeardTime"),
        ("SYMBOL-AP-MIB", "apMuLocationingAddMuMac"),
        ("SYMBOL-AP-MIB", "apMuLocationingAddPortalMac"),
        ("SYMBOL-AP-MIB", "apMuLocationingAddSignalStrength"),
        ("SYMBOL-AP-MIB", "apMuLocationingAddHeardChannel"),
        ("SYMBOL-AP-MIB", "apMuLocationingAddHeardTime"),
        ("SYMBOL-AP-MIB", "apAapPassphrase"),
        ("SYMBOL-AP-MIB", "apWipsSecondaryServerAddr"),
        ("SYMBOL-AP-MIB", "apWipsPrimaryServerAddr"),
        ("SYMBOL-AP-MIB", "apTrustedHostEnable"),
        ("SYMBOL-AP-MIB", "apTrustedHostRangeIndex"),
        ("SYMBOL-AP-MIB", "apTrustedHostRangeLowerIp"),
        ("SYMBOL-AP-MIB", "apTrustedHostRangeUpperIp"),
        ("SYMBOL-AP-MIB", "apAapSwitchAutoDiscoveryEnable"),
        ("SYMBOL-AP-MIB", "apMuLocationingEnable"),
        ("SYMBOL-AP-MIB", "apMuLocationingClear"),
        ("SYMBOL-AP-MIB", "apMuLocationingMaxMus"))
)
if mibBuilder.loadTexts:
    apGroupV1dot1variables.setStatus("current")

apGroupV1dot1obsoleted = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 1000, 2, 2)
)
apGroupV1dot1obsoleted.setObjects(
      *(("SYMBOL-AP-MIB", "apLanAdminVlanTag"),
        ("SYMBOL-AP-MIB", "apLanNativeVlanTag"),
        ("SYMBOL-AP-MIB", "apRadioSettingsDtimPrd"),
        ("SYMBOL-AP-MIB", "apRadioSettingsVoiceMode"),
        ("SYMBOL-AP-MIB", "apRadioSettingsVideoMode"),
        ("SYMBOL-AP-MIB", "apRadioSettingsBestEffortMode"),
        ("SYMBOL-AP-MIB", "apRadioSettingsBackgroundMode"),
        ("SYMBOL-AP-MIB", "apWlanWeight"),
        ("SYMBOL-AP-MIB", "apLanTypeFilterAccessMode"),
        ("SYMBOL-AP-MIB", "apLanVlanEnable"))
)
if mibBuilder.loadTexts:
    apGroupV1dot1obsoleted.setStatus("obsolete")

apGroupV1dot1deprecated = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 1000, 2, 3)
)
apGroupV1dot1deprecated.setObjects(
      *(("SYMBOL-AP-MIB", "apLanEnable"),
        ("SYMBOL-AP-MIB", "apRadioNMcsRate20MHzChanSgiEnabled"))
)
if mibBuilder.loadTexts:
    apGroupV1dot1deprecated.setStatus("deprecated")

apGroupV2dot2variables = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 1000, 3, 1)
)
apGroupV2dot2variables.setObjects(
      *(("SYMBOL-AP-MIB", "apReliableMulticastMode"),
        ("SYMBOL-AP-MIB", "apReliableMulticastWlan"),
        ("SYMBOL-AP-MIB", "apReliableMulticastStandaloneMode"),
        ("SYMBOL-AP-MIB", "apReliableMulticastIgmpQueryVersion"),
        ("SYMBOL-AP-MIB", "apReliableMulticastIgmpQueryInterval"),
        ("SYMBOL-AP-MIB", "apReliableMulticastAddrIndex"),
        ("SYMBOL-AP-MIB", "apReliableMulticastAddress"),
        ("SYMBOL-AP-MIB", "apReliableMulticastMUStatsIPAddr"),
        ("SYMBOL-AP-MIB", "apReliableMulticastMUMacAddr"),
        ("SYMBOL-AP-MIB", "apReliableMulticastTxMulticast"),
        ("SYMBOL-AP-MIB", "apReliableMulticastTableRowEnable"),
        ("SYMBOL-AP-MIB", "apReliableMulticastMUStatsIndex"),
        ("SYMBOL-AP-MIB", "apReliableMulticastMaxStreams"))
)
if mibBuilder.loadTexts:
    apGroupV2dot2variables.setStatus("current")


# Notification objects

apMuVlan = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 1)
)
apMuVlan.setObjects(
      *(("SYMBOL-AP-MIB", "apTrapMuMac"),
        ("SYMBOL-AP-MIB", "apTrapRadioMac"),
        ("SYMBOL-AP-MIB", "apTrapVlanId"))
)
if mibBuilder.loadTexts:
    apMuVlan.setStatus(
        "current"
    )

apLanMonitor = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 2)
)
apLanMonitor.setObjects(
      *(("SYMBOL-AP-MIB", "apTrapLanMonitorMode"),
        ("SYMBOL-AP-MIB", "apTrapLanMonitorReason"))
)
if mibBuilder.loadTexts:
    apLanMonitor.setStatus(
        "current"
    )

apWpaCounterMeasure = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 3)
)
apWpaCounterMeasure.setObjects(
    ("SYMBOL-AP-MIB", "apTrapWpaCounterMeasureEssid")
)
if mibBuilder.loadTexts:
    apWpaCounterMeasure.setStatus(
        "current"
    )

apMuHotspotState = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 4)
)
apMuHotspotState.setObjects(
      *(("SYMBOL-AP-MIB", "apTrapCtrlMuMac"),
        ("SYMBOL-AP-MIB", "apTrapCtrlMuHotspotStateChange"))
)
if mibBuilder.loadTexts:
    apMuHotspotState.setStatus(
        "current"
    )

apDynDNSUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 6, 5)
)
apDynDNSUpdate.setObjects(
      *(("SYMBOL-AP-MIB", "apTrapCtrlDynDNSUpdateIp"),
        ("SYMBOL-AP-MIB", "apTrapCtrlDynDNSUpdateHostname"),
        ("SYMBOL-AP-MIB", "apTrapCtrlDynDNSUpdateStatus"))
)
if mibBuilder.loadTexts:
    apDynDNSUpdate.setStatus(
        "current"
    )


# Notifications groups

apNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 1000, 1, 8)
)
apNotificationsGroup.setObjects(
      *(("SYMBOL-AP-MIB", "apWpaCounterMeasure"),
        ("SYMBOL-AP-MIB", "apLanMonitor"),
        ("SYMBOL-AP-MIB", "apMuVlan"))
)
if mibBuilder.loadTexts:
    apNotificationsGroup.setStatus(
        "current"
    )

apGroupV1dot1notifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 3, 1000, 2, 4)
)
apGroupV1dot1notifications.setObjects(
      *(("SYMBOL-AP-MIB", "apMuHotspotState"),
        ("SYMBOL-AP-MIB", "apDynDNSUpdate"))
)
if mibBuilder.loadTexts:
    apGroupV1dot1notifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYMBOL-AP-MIB",
    **{"SinglePointer": SinglePointer,
       "MultiPointer63": MultiPointer63,
       "MultiPointer255": MultiPointer255,
       "DoActionNow": DoActionNow,
       "RadioType": RadioType,
       "Password": Password,
       "StaticRowEnable": StaticRowEnable,
       "PartsPer10k": PartsPer10k,
       "ScaleBy100": ScaleBy100,
       "AbbrevRowStatus": AbbrevRowStatus,
       "DoActionShowProgress": DoActionShowProgress,
       "HexPassword": HexPassword,
       "TransmitRate": TransmitRate,
       "AllowedChannels": AllowedChannels,
       "RowStatus": RowStatus,
       "DateAndTime": DateAndTime,
       "EthernetType": EthernetType,
       "symbol": symbol,
       "wsd": wsd,
       "sysoids": sysoids,
       "ap5131": ap5131,
       "ap5181": ap5181,
       "ap7131": ap7131,
       "ap7181": ap7181,
       "abgAP": abgAP,
       "moduleid": moduleid,
       "dot1x": dot1x,
       "dot1xPaeAuthenticator": dot1xPaeAuthenticator,
       "dot1xAuthConfigTable": dot1xAuthConfigTable,
       "dot1xAuthConfigEntry": dot1xAuthConfigEntry,
       "dot1xPaePortNumber": dot1xPaePortNumber,
       "dot1xPaeState": dot1xPaeState,
       "dot1xAuthBackendAuthState": dot1xAuthBackendAuthState,
       "dot1xAuthAdminControlledDirections": dot1xAuthAdminControlledDirections,
       "dot1xAuthOperControlledDirections": dot1xAuthOperControlledDirections,
       "dot1xAuthAuthControlledPortStatus": dot1xAuthAuthControlledPortStatus,
       "dot1xAuthAuthControlledPortControl": dot1xAuthAuthControlledPortControl,
       "dot1xAuthQuietPeriod": dot1xAuthQuietPeriod,
       "dot1xAuthTxPeriod": dot1xAuthTxPeriod,
       "dot1xAuthSuppTimeout": dot1xAuthSuppTimeout,
       "dot1xAuthServerTimeout": dot1xAuthServerTimeout,
       "dot1xAuthMaxReq": dot1xAuthMaxReq,
       "dot1xAuthReAuthPeriod": dot1xAuthReAuthPeriod,
       "dot1xAuthReAuthEnabled": dot1xAuthReAuthEnabled,
       "dot1xAuthKeyTxEnabled": dot1xAuthKeyTxEnabled,
       "dot1xAuthStatsTable": dot1xAuthStatsTable,
       "dot1xAuthStatsEntry": dot1xAuthStatsEntry,
       "dot1xAuthEapolFramesRx": dot1xAuthEapolFramesRx,
       "dot1xAuthEapolFramesTx": dot1xAuthEapolFramesTx,
       "dot1xAuthEapolStartFramesRx": dot1xAuthEapolStartFramesRx,
       "dot1xAuthEapolLogoffFramesRx": dot1xAuthEapolLogoffFramesRx,
       "dot1xAuthEapolRespIdFramesRx": dot1xAuthEapolRespIdFramesRx,
       "dot1xAuthEapolRespFramesRx": dot1xAuthEapolRespFramesRx,
       "dot1xAuthEapolReqIdFramesTx": dot1xAuthEapolReqIdFramesTx,
       "dot1xAuthEapolReqFramesTx": dot1xAuthEapolReqFramesTx,
       "dot1xAuthInvalidEapolFramesRx": dot1xAuthInvalidEapolFramesRx,
       "dot1xAuthEapLengthErrorFramesRx": dot1xAuthEapLengthErrorFramesRx,
       "dot1xAuthLastEapolFrameVersion": dot1xAuthLastEapolFrameVersion,
       "dot1xAuthLastEapolFrameSource": dot1xAuthLastEapolFrameSource,
       "dot1xAuthDiagTable": dot1xAuthDiagTable,
       "dot1xAuthDiagEntry": dot1xAuthDiagEntry,
       "dot1xAuthEntersConnecting": dot1xAuthEntersConnecting,
       "dot1xAuthEapLogoffsWhileConnecting": dot1xAuthEapLogoffsWhileConnecting,
       "dot1xAuthEntersAuthenticating": dot1xAuthEntersAuthenticating,
       "dot1xAuthAuthSuccessWhileAuthenticating": dot1xAuthAuthSuccessWhileAuthenticating,
       "dot1xAuthAuthTimeoutsWhileAuthenticating": dot1xAuthAuthTimeoutsWhileAuthenticating,
       "dot1xAuthAuthFailWhileAuthenticating": dot1xAuthAuthFailWhileAuthenticating,
       "dot1xAuthAuthReauthsWhileAuthenticating": dot1xAuthAuthReauthsWhileAuthenticating,
       "dot1xAuthAuthEapStartsWhileAuthenticating": dot1xAuthAuthEapStartsWhileAuthenticating,
       "dot1xAuthAuthEapLogoffWhileAuthenticating": dot1xAuthAuthEapLogoffWhileAuthenticating,
       "dot1xAuthAuthReauthsWhileAuthenticated": dot1xAuthAuthReauthsWhileAuthenticated,
       "dot1xAuthAuthEapStartsWhileAuthenticated": dot1xAuthAuthEapStartsWhileAuthenticated,
       "dot1xAuthAuthEapLogoffWhileAuthenticated": dot1xAuthAuthEapLogoffWhileAuthenticated,
       "dot1xAuthBackendResponses": dot1xAuthBackendResponses,
       "dot1xAuthBackendAccessChallenges": dot1xAuthBackendAccessChallenges,
       "dot1xAuthBackendOtherRequestsToSupplicant": dot1xAuthBackendOtherRequestsToSupplicant,
       "dot1xAuthBackendNonNakResponsesFromSupplicant": dot1xAuthBackendNonNakResponsesFromSupplicant,
       "dot1xAuthBackendAuthSuccesses": dot1xAuthBackendAuthSuccesses,
       "dot1xAuthBackendAuthFails": dot1xAuthBackendAuthFails,
       "dot1xAuthSessionStatsTable": dot1xAuthSessionStatsTable,
       "dot1xAuthSessionStatsEntry": dot1xAuthSessionStatsEntry,
       "dot1xAuthSessionOctetsRx": dot1xAuthSessionOctetsRx,
       "dot1xAuthSessionOctetsTx": dot1xAuthSessionOctetsTx,
       "dot1xAuthSessionFramesRx": dot1xAuthSessionFramesRx,
       "dot1xAuthSessionFramesTx": dot1xAuthSessionFramesTx,
       "dot1xAuthSessionId": dot1xAuthSessionId,
       "dot1xAuthSessionAuthenticMethod": dot1xAuthSessionAuthenticMethod,
       "dot1xAuthSessionTime": dot1xAuthSessionTime,
       "dot1xAuthSessionTerminateCause": dot1xAuthSessionTerminateCause,
       "dot1xAuthSessionUserName": dot1xAuthSessionUserName,
       "apRf": apRf,
       "apRadio": apRadio,
       "apRadioSettingsTable": apRadioSettingsTable,
       "apRadioSettingsEntry": apRadioSettingsEntry,
       "apRadioSettingsIndex": apRadioSettingsIndex,
       "apRadioSettingsEnable": apRadioSettingsEnable,
       "apRadioSettingsBand": apRadioSettingsBand,
       "apRadioSettingsPointersToWlans": apRadioSettingsPointersToWlans,
       "apRadioSettingsName": apRadioSettingsName,
       "apRadioSettingsMacAddress": apRadioSettingsMacAddress,
       "apRadioSettingsAntenna": apRadioSettingsAntenna,
       "apRadioSettingsShortPreamble": apRadioSettingsShortPreamble,
       "apRadioSettingsRtsThresh": apRadioSettingsRtsThresh,
       "apRadioSettingsBeaconInt": apRadioSettingsBeaconInt,
       "apRadioSettingsDtimPrd": apRadioSettingsDtimPrd,
       "apRadioSettingsBasicRates": apRadioSettingsBasicRates,
       "apRadioSettingsSupportedRates": apRadioSettingsSupportedRates,
       "apRadioSettingsBGMode": apRadioSettingsBGMode,
       "apRadioSettingsBackgroundMode": apRadioSettingsBackgroundMode,
       "apRadioSettingsBackgroundCwMin": apRadioSettingsBackgroundCwMin,
       "apRadioSettingsBackgroundCwMax": apRadioSettingsBackgroundCwMax,
       "apRadioSettingsBackgroundAifsn": apRadioSettingsBackgroundAifsn,
       "apRadioSettingsBackgroundTxopsTime": apRadioSettingsBackgroundTxopsTime,
       "apRadioSettingsBackgroundTxopsTimeInMS": apRadioSettingsBackgroundTxopsTimeInMS,
       "apRadioSettingsBestEffortMode": apRadioSettingsBestEffortMode,
       "apRadioSettingsBestEffortCwMin": apRadioSettingsBestEffortCwMin,
       "apRadioSettingsBestEffortCwMax": apRadioSettingsBestEffortCwMax,
       "apRadioSettingsBestEffortAifsn": apRadioSettingsBestEffortAifsn,
       "apRadioSettingsBestEffortTxopsTime": apRadioSettingsBestEffortTxopsTime,
       "apRadioSettingsBestEffortTxopsTimeInMS": apRadioSettingsBestEffortTxopsTimeInMS,
       "apRadioSettingsVideoMode": apRadioSettingsVideoMode,
       "apRadioSettingsVideoCwMin": apRadioSettingsVideoCwMin,
       "apRadioSettingsVideoCwMax": apRadioSettingsVideoCwMax,
       "apRadioSettingsVideoAifsn": apRadioSettingsVideoAifsn,
       "apRadioSettingsVideoTxopsTime": apRadioSettingsVideoTxopsTime,
       "apRadioSettingsVideoTxopsTimeInMS": apRadioSettingsVideoTxopsTimeInMS,
       "apRadioSettingsVoiceMode": apRadioSettingsVoiceMode,
       "apRadioSettingsVoiceCwMin": apRadioSettingsVoiceCwMin,
       "apRadioSettingsVoiceCwMax": apRadioSettingsVoiceCwMax,
       "apRadioSettingsVoiceAifsn": apRadioSettingsVoiceAifsn,
       "apRadioSettingsVoiceTxopsTime": apRadioSettingsVoiceTxopsTime,
       "apRadioSettingsVoiceTxopsTimeInMS": apRadioSettingsVoiceTxopsTimeInMS,
       "apRadioSettingsE2BMapMessage": apRadioSettingsE2BMapMessage,
       "apRadioSettingsERPProtectionStatus": apRadioSettingsERPProtectionStatus,
       "apRadioSettingsWMMQosParam": apRadioSettingsWMMQosParam,
       "apRadioSettingsQBSSChannelBeaconInt": apRadioSettingsQBSSChannelBeaconInt,
       "apRadioSettingsQBSSLoadElementMode": apRadioSettingsQBSSLoadElementMode,
       "apRadioCfgTable": apRadioCfgTable,
       "apRadioCfgEntry": apRadioCfgEntry,
       "apRadioCfgChannelMode": apRadioCfgChannelMode,
       "apRadioCfgDesPlacement": apRadioCfgDesPlacement,
       "apRadioCfgPosChannel": apRadioCfgPosChannel,
       "apRadioCfgDesChannel": apRadioCfgDesChannel,
       "apRadioCfgPosPowerLevel": apRadioCfgPosPowerLevel,
       "apRadioCfgDesPowerLevel": apRadioCfgDesPowerLevel,
       "apRadioCfgDesPowerInMW": apRadioCfgDesPowerInMW,
       "apRadioCfgSet": apRadioCfgSet,
       "apRadioCfgReset": apRadioCfgReset,
       "apRadioCfgPlacement": apRadioCfgPlacement,
       "apRadioCfgChannel": apRadioCfgChannel,
       "apRadioCfgPowerLevel": apRadioCfgPowerLevel,
       "apRadioCfgPowerInMW": apRadioCfgPowerInMW,
       "apRadioCfgRfFunction": apRadioCfgRfFunction,
       "apRadioCfgExceptionChannel": apRadioCfgExceptionChannel,
       "apRadioWlanBssTable": apRadioWlanBssTable,
       "apRadioWlanBssEntry": apRadioWlanBssEntry,
       "apRadioWlanBssid": apRadioWlanBssid,
       "apRadioBssTable": apRadioBssTable,
       "apRadioBssEntry": apRadioBssEntry,
       "apRadioBssIndex": apRadioBssIndex,
       "apRadioBssPrimaryWlan": apRadioBssPrimaryWlan,
       "apRadioBssDtimPrd": apRadioBssDtimPrd,
       "apRadioE2BMapStatusTable": apRadioE2BMapStatusTable,
       "apRadioE2BMapStatusEntry": apRadioE2BMapStatusEntry,
       "apRadioE2BMapStatusBcMcEncCipher": apRadioE2BMapStatusBcMcEncCipher,
       "apRadioE2BMapStatus": apRadioE2BMapStatus,
       "apRadioE2BMapStatusMessage": apRadioE2BMapStatusMessage,
       "apRadioMesh": apRadioMesh,
       "apRadioMeshTable": apRadioMeshTable,
       "apRadioMeshEntry": apRadioMeshEntry,
       "apRadioMeshBaseBridgeMode": apRadioMeshBaseBridgeMode,
       "apRadioMeshMaxClients": apRadioMeshMaxClients,
       "apRadioMeshClientBridgeMode": apRadioMeshClientBridgeMode,
       "apRadioMeshWlanPtr": apRadioMeshWlanPtr,
       "apRadioMeshConnAutoSelect": apRadioMeshConnAutoSelect,
       "apRadioMeshTimeout": apRadioMeshTimeout,
       "apRadioMeshTimeoutValue": apRadioMeshTimeoutValue,
       "apRadioMeshAvailableConnTable": apRadioMeshAvailableConnTable,
       "apRadioMeshAvailableConnEntry": apRadioMeshAvailableConnEntry,
       "apRadioMeshAvailableConnIndex": apRadioMeshAvailableConnIndex,
       "apRadioMeshAvailableConnMac": apRadioMeshAvailableConnMac,
       "apRadioMeshAvailableConnChannel": apRadioMeshAvailableConnChannel,
       "apRadioMeshAvailableConnRssi": apRadioMeshAvailableConnRssi,
       "apRadioMeshPreferredConnTable": apRadioMeshPreferredConnTable,
       "apRadioMeshPreferredConnEntry": apRadioMeshPreferredConnEntry,
       "apRadioMeshPreferredConnIndex": apRadioMeshPreferredConnIndex,
       "apRadioMeshPreferredConnPriority": apRadioMeshPreferredConnPriority,
       "apRadioMeshPreferredConnMac": apRadioMeshPreferredConnMac,
       "apRadioMeshPreferredConnRowStatus": apRadioMeshPreferredConnRowStatus,
       "apRadioWlanBandwidthTable": apRadioWlanBandwidthTable,
       "apRadioWlanBandwidthEntry": apRadioWlanBandwidthEntry,
       "apRadioWlanWeight": apRadioWlanWeight,
       "apRadioNSettingsTable": apRadioNSettingsTable,
       "apRadioNSettingsEntry": apRadioNSettingsEntry,
       "apRadioNSettingsMode": apRadioNSettingsMode,
       "apRadioNSettingsHTProtectionStatus": apRadioNSettingsHTProtectionStatus,
       "apRadioNSettingsBasicRates": apRadioNSettingsBasicRates,
       "apRadioNCfgTable": apRadioNCfgTable,
       "apRadioNCfgEntry": apRadioNCfgEntry,
       "apRadioNCfgPosChannel": apRadioNCfgPosChannel,
       "apRadioNCfgDesChannel": apRadioNCfgDesChannel,
       "apRadioNCfgChannel": apRadioNCfgChannel,
       "apRadioNCfgChannelWidth": apRadioNCfgChannelWidth,
       "apRadioNCfgAmsduAggregationMaxRecvSize": apRadioNCfgAmsduAggregationMaxRecvSize,
       "apRadioNCfgAmsduTransmitEnabled": apRadioNCfgAmsduTransmitEnabled,
       "apRadioNCfgAmpduAggregationMaxRecvSize": apRadioNCfgAmpduAggregationMaxRecvSize,
       "apRadioNCfgAmpduAggregationDensity": apRadioNCfgAmpduAggregationDensity,
       "apRadioNCfgAmpduTransmitSizeLimit": apRadioNCfgAmpduTransmitSizeLimit,
       "apRadioNCfgShortGuardInterval": apRadioNCfgShortGuardInterval,
       "apRadioNCfgAmpduTransmitEnabled": apRadioNCfgAmpduTransmitEnabled,
       "apRadioNCfgChannelOffset": apRadioNCfgChannelOffset,
       "apRadioNMcsRateTable": apRadioNMcsRateTable,
       "apRadioNMcsRateEntry": apRadioNMcsRateEntry,
       "apRadioNMcsRateIndex": apRadioNMcsRateIndex,
       "apRadioNMcsRate20MHzChanSgiDisabled": apRadioNMcsRate20MHzChanSgiDisabled,
       "apRadioNMcsRate20MHzChanSgiEnabled": apRadioNMcsRate20MHzChanSgiEnabled,
       "apRadioNMcsRate40MHzChanSgiDisabled": apRadioNMcsRate40MHzChanSgiDisabled,
       "apRadioNMcsRate40MHzChanSgiEnabled": apRadioNMcsRate40MHzChanSgiEnabled,
       "apRadioNMcsRateType": apRadioNMcsRateType,
       "apRadioNMcsRateEnabled": apRadioNMcsRateEnabled,
       "apWlan": apWlan,
       "apWlanTable": apWlanTable,
       "apWlanEntry": apWlanEntry,
       "apWlanIndex": apWlanIndex,
       "apWlanName": apWlanName,
       "apWlanEssid": apWlanEssid,
       "apWlanUseRadio": apWlanUseRadio,
       "apWlanMaxMus": apWlanMaxMus,
       "apWlanAclPolicy": apWlanAclPolicy,
       "apWlanSecurityPolicy": apWlanSecurityPolicy,
       "apWlanQosPolicy": apWlanQosPolicy,
       "apWlanAuthKerberosUsername": apWlanAuthKerberosUsername,
       "apWlanAuthKerberosPassword": apWlanAuthKerberosPassword,
       "apWlanDisallowMuToMu": apWlanDisallowMuToMu,
       "apWlanUseSecureBeacon": apWlanUseSecureBeacon,
       "apWlanAnswerBroadcastEss": apWlanAnswerBroadcastEss,
       "apWlanWeight": apWlanWeight,
       "apWlanVlanMode": apWlanVlanMode,
       "apWlanVlanId": apWlanVlanId,
       "apWlanSubnet": apWlanSubnet,
       "apWlanClientBackHaul": apWlanClientBackHaul,
       "apWlanHotspot": apWlanHotspot,
       "apWlanEnable": apWlanEnable,
       "apWlanMuIdleTimeout": apWlanMuIdleTimeout,
       "apWlanSecPolicyTable": apWlanSecPolicyTable,
       "apWlanSecPolicyEntry": apWlanSecPolicyEntry,
       "apWlanSecPolicyIndex": apWlanSecPolicyIndex,
       "apWlanSecPolicyName": apWlanSecPolicyName,
       "apWlanSecPolicyAuthentication": apWlanSecPolicyAuthentication,
       "apWlanSecPolicyEncryption": apWlanSecPolicyEncryption,
       "apWlanSecPolicyPointerToWlan": apWlanSecPolicyPointerToWlan,
       "apWlanSecPolicyRowStatus": apWlanSecPolicyRowStatus,
       "apWlanAuth": apWlanAuth,
       "apWlanAuthEapTable": apWlanAuthEapTable,
       "apWlanAuthEapEntry": apWlanAuthEapEntry,
       "apWlanAuthEapReauthenticationEnable": apWlanAuthEapReauthenticationEnable,
       "apWlanAuthEapReauthenticationPeriod": apWlanAuthEapReauthenticationPeriod,
       "apWlanAuthEapReauthenticationMaxRetries": apWlanAuthEapReauthenticationMaxRetries,
       "apWlanAuthEapRadius1Server": apWlanAuthEapRadius1Server,
       "apWlanAuthEapRadius1Port": apWlanAuthEapRadius1Port,
       "apWlanAuthEapRadius1SharedSecret": apWlanAuthEapRadius1SharedSecret,
       "apWlanAuthEapRadius2Server": apWlanAuthEapRadius2Server,
       "apWlanAuthEapRadius2Port": apWlanAuthEapRadius2Port,
       "apWlanAuthEapRadius2SharedSecret": apWlanAuthEapRadius2SharedSecret,
       "apWlanAuthEapMuQuietPeriod": apWlanAuthEapMuQuietPeriod,
       "apWlanAuthEapMuTimeout": apWlanAuthEapMuTimeout,
       "apWlanAuthEapMuTxPeriod": apWlanAuthEapMuTxPeriod,
       "apWlanAuthEapMuMaxRetries": apWlanAuthEapMuMaxRetries,
       "apWlanAuthEapServerTimeout": apWlanAuthEapServerTimeout,
       "apWlanAuthEapServerMaxRetries": apWlanAuthEapServerMaxRetries,
       "apWlanAuthEapRadiusAcctMode": apWlanAuthEapRadiusAcctMode,
       "apWlanAuthEapRadiusAcctMuTimeout": apWlanAuthEapRadiusAcctMuTimeout,
       "apWlanAuthEapRadiusAcctMuRetries": apWlanAuthEapRadiusAcctMuRetries,
       "apWlanAuthEapSyslogMode": apWlanAuthEapSyslogMode,
       "apWlanAuthEapSyslogServerIp": apWlanAuthEapSyslogServerIp,
       "apWlanAuthEapRadiusExtAcctServer": apWlanAuthEapRadiusExtAcctServer,
       "apWlanAuthEapRadiusExtPort": apWlanAuthEapRadiusExtPort,
       "apWlanAuthEapRadiusExtSharedSecret": apWlanAuthEapRadiusExtSharedSecret,
       "apWlanAuthKerberosTable": apWlanAuthKerberosTable,
       "apWlanAuthKerberosEntry": apWlanAuthKerberosEntry,
       "apWlanAuthKerberosRealmName": apWlanAuthKerberosRealmName,
       "apWlanAuthKerberosKdcServerIp1": apWlanAuthKerberosKdcServerIp1,
       "apWlanAuthKerberosKdcPort1": apWlanAuthKerberosKdcPort1,
       "apWlanAuthKerberosKdcServerIp2": apWlanAuthKerberosKdcServerIp2,
       "apWlanAuthKerberosKdcPort2": apWlanAuthKerberosKdcPort2,
       "apWlanAuthKerberosKdcServerIpR": apWlanAuthKerberosKdcServerIpR,
       "apWlanAuthKerberosKdcPortR": apWlanAuthKerberosKdcPortR,
       "apWlanCrypto": apWlanCrypto,
       "apWlanCryptoWepTable": apWlanCryptoWepTable,
       "apWlanCryptoWepEntry": apWlanCryptoWepEntry,
       "apWlanCryptoWepPassKey": apWlanCryptoWepPassKey,
       "apWlanCryptoWepKey1": apWlanCryptoWepKey1,
       "apWlanCryptoWepKey2": apWlanCryptoWepKey2,
       "apWlanCryptoWepKey3": apWlanCryptoWepKey3,
       "apWlanCryptoWepKey4": apWlanCryptoWepKey4,
       "apWlanCryptoWepKeyToUse": apWlanCryptoWepKeyToUse,
       "apWlanCryptoWepMixedMode": apWlanCryptoWepMixedMode,
       "apWlanCryptoTkipTable": apWlanCryptoTkipTable,
       "apWlanCryptoTkipEntry": apWlanCryptoTkipEntry,
       "apWlanCryptoTkipBcastKeyRotation": apWlanCryptoTkipBcastKeyRotation,
       "apWlanCryptoTkipKeyRotationInterval": apWlanCryptoTkipKeyRotationInterval,
       "apWlanCryptoTkipKeyToUse": apWlanCryptoTkipKeyToUse,
       "apWlanCryptoTkipPassphrase": apWlanCryptoTkipPassphrase,
       "apWlanCryptoTkipKey": apWlanCryptoTkipKey,
       "apWlanCryptoTkipAllowWpa2Client": apWlanCryptoTkipAllowWpa2Client,
       "apWlanCryptoTkipFastRoamPreAuth": apWlanCryptoTkipFastRoamPreAuth,
       "apWlanCryptoCcmpTable": apWlanCryptoCcmpTable,
       "apWlanCryptoCcmpEntry": apWlanCryptoCcmpEntry,
       "apWlanCryptoCcmpBcastKeyRotation": apWlanCryptoCcmpBcastKeyRotation,
       "apWlanCryptoCcmpKeyRotationInterval": apWlanCryptoCcmpKeyRotationInterval,
       "apWlanCryptoCcmpKeyToUse": apWlanCryptoCcmpKeyToUse,
       "apWlanCryptoCcmpPassphrase": apWlanCryptoCcmpPassphrase,
       "apWlanCryptoCcmpKey": apWlanCryptoCcmpKey,
       "apWlanCryptoCcmpMixedMode": apWlanCryptoCcmpMixedMode,
       "apWlanCryptoCcmpFastRoamPreAuth": apWlanCryptoCcmpFastRoamPreAuth,
       "apWlanCryptoKeyguardTable": apWlanCryptoKeyguardTable,
       "apWlanCryptoKeyguardEntry": apWlanCryptoKeyguardEntry,
       "apWlanCryptoKeyguardPassKey": apWlanCryptoKeyguardPassKey,
       "apWlanCryptoKeyguardKey1": apWlanCryptoKeyguardKey1,
       "apWlanCryptoKeyguardKey2": apWlanCryptoKeyguardKey2,
       "apWlanCryptoKeyguardKey3": apWlanCryptoKeyguardKey3,
       "apWlanCryptoKeyguardKey4": apWlanCryptoKeyguardKey4,
       "apWlanCryptoKeyguardKeyToUse": apWlanCryptoKeyguardKeyToUse,
       "apWlanCryptoKeyguardMixedMode": apWlanCryptoKeyguardMixedMode,
       "apWlanMuAclPolicyTable": apWlanMuAclPolicyTable,
       "apWlanMuAclPolicyEntry": apWlanMuAclPolicyEntry,
       "apWlanMuAclPolicyIndex": apWlanMuAclPolicyIndex,
       "apWlanMuAclPolicyName": apWlanMuAclPolicyName,
       "apWlanMuAclPolicyAccessMode": apWlanMuAclPolicyAccessMode,
       "apWlanMuAclPolicyPointerToWlan": apWlanMuAclPolicyPointerToWlan,
       "apWlanMuAclPolicyRowStatus": apWlanMuAclPolicyRowStatus,
       "apWlanMuAclTable": apWlanMuAclTable,
       "apWlanMuAclEntry": apWlanMuAclEntry,
       "apWlanMuAclIndex": apWlanMuAclIndex,
       "apWlanMuAclStartingMac": apWlanMuAclStartingMac,
       "apWlanMuAclEndingMac": apWlanMuAclEndingMac,
       "apWlanMuAclPointerToAclPolicy": apWlanMuAclPointerToAclPolicy,
       "apWlanMuAclRowStatus": apWlanMuAclRowStatus,
       "apWlanQosPolicyTable": apWlanQosPolicyTable,
       "apWlanQosPolicyEntry": apWlanQosPolicyEntry,
       "apWlanQosPolicyIndex": apWlanQosPolicyIndex,
       "apWlanQosPolicyName": apWlanQosPolicyName,
       "apWlanEnableWMM": apWlanEnableWMM,
       "apWlanWMMQosParam": apWlanWMMQosParam,
       "apWlanQosPolicyBackgroundCwMin": apWlanQosPolicyBackgroundCwMin,
       "apWlanQosPolicyBackgroundCwMax": apWlanQosPolicyBackgroundCwMax,
       "apWlanQosPolicyBackgroundAifsn": apWlanQosPolicyBackgroundAifsn,
       "apWlanQosPolicyBackgroundTxopsTime": apWlanQosPolicyBackgroundTxopsTime,
       "apWlanQosPolicyBackgroundTxopsTimeInMS": apWlanQosPolicyBackgroundTxopsTimeInMS,
       "apWlanQosPolicyBestEffortCwMin": apWlanQosPolicyBestEffortCwMin,
       "apWlanQosPolicyBestEffortCwMax": apWlanQosPolicyBestEffortCwMax,
       "apWlanQosPolicyBestEffortAifsn": apWlanQosPolicyBestEffortAifsn,
       "apWlanQosPolicyBestEffortTxopsTime": apWlanQosPolicyBestEffortTxopsTime,
       "apWlanQosPolicyBestEffortTxopsTimeInMS": apWlanQosPolicyBestEffortTxopsTimeInMS,
       "apWlanQosPolicyVideoCwMin": apWlanQosPolicyVideoCwMin,
       "apWlanQosPolicyVideoCwMax": apWlanQosPolicyVideoCwMax,
       "apWlanQosPolicyVideoAifsn": apWlanQosPolicyVideoAifsn,
       "apWlanQosPolicyVideoTxopsTime": apWlanQosPolicyVideoTxopsTime,
       "apWlanQosPolicyVideoTxopsTimeInMS": apWlanQosPolicyVideoTxopsTimeInMS,
       "apWlanQosPolicyVoiceCwMin": apWlanQosPolicyVoiceCwMin,
       "apWlanQosPolicyVoiceCwMax": apWlanQosPolicyVoiceCwMax,
       "apWlanQosPolicyVoiceAifsn": apWlanQosPolicyVoiceAifsn,
       "apWlanQosPolicyVoiceTxopsTime": apWlanQosPolicyVoiceTxopsTime,
       "apWlanQosPolicyVoiceTxopsTimeInMS": apWlanQosPolicyVoiceTxopsTimeInMS,
       "apWlanVoicePrioritization": apWlanVoicePrioritization,
       "apWlanMulticastAddr1": apWlanMulticastAddr1,
       "apWlanMulticastAddr2": apWlanMulticastAddr2,
       "apWlanQosPolicyPointerToWlan": apWlanQosPolicyPointerToWlan,
       "apWlanQosPolicyRowStatus": apWlanQosPolicyRowStatus,
       "apWlanBwShareModeTable": apWlanBwShareModeTable,
       "apWlanBwShareModeEntry": apWlanBwShareModeEntry,
       "apWlanBwShareMode": apWlanBwShareMode,
       "apHotSpot": apHotSpot,
       "apHotSpotTable": apHotSpotTable,
       "apHotSpotEntry": apHotSpotEntry,
       "apHotSpotDefaultFileMode": apHotSpotDefaultFileMode,
       "apHotSpotExternalLoginPageUrl": apHotSpotExternalLoginPageUrl,
       "apHotSpotExternalWelomePageUrl": apHotSpotExternalWelomePageUrl,
       "apHotSpotExternalFailPageUrl": apHotSpotExternalFailPageUrl,
       "apHotSpotPriRadiusServerIp": apHotSpotPriRadiusServerIp,
       "apHotSpotPriRadiusPort": apHotSpotPriRadiusPort,
       "apHotSpotPriRadiusSecret": apHotSpotPriRadiusSecret,
       "apHotSpotSecRadiusServerIp": apHotSpotSecRadiusServerIp,
       "apHotSpotSecRadiusPort": apHotSpotSecRadiusPort,
       "apHotSpotSecRadiusSecret": apHotSpotSecRadiusSecret,
       "apHotSpotRadiusAcctMode": apHotSpotRadiusAcctMode,
       "apHotSpotRadiusAcctServerIp": apHotSpotRadiusAcctServerIp,
       "apHotSpotRadiusAcctPort": apHotSpotRadiusAcctPort,
       "apHotSpotRadiusAcctSecret": apHotSpotRadiusAcctSecret,
       "apHotSpotRadiusAcctTimeout": apHotSpotRadiusAcctTimeout,
       "apHotSpotRadiusAcctRetryCount": apHotSpotRadiusAcctRetryCount,
       "apHotSpotRadiusSessMode": apHotSpotRadiusSessMode,
       "apHotSpotRadiusSessTimeout": apHotSpotRadiusSessTimeout,
       "apHotSpotWhiteListTable": apHotSpotWhiteListTable,
       "apHotSpotWhiteListEntry": apHotSpotWhiteListEntry,
       "apHotSpotWhiteListIndex": apHotSpotWhiteListIndex,
       "apHotSpotWhiteListWalledGardenIp": apHotSpotWhiteListWalledGardenIp,
       "apHotSpotWhiteListRowStatus": apHotSpotWhiteListRowStatus,
       "apMus": apMus,
       "apMuLocationing": apMuLocationing,
       "apMuLocationingEnable": apMuLocationingEnable,
       "apMuLocationingClear": apMuLocationingClear,
       "apMuLocationingMaxMus": apMuLocationingMaxMus,
       "apMuLocationingTable": apMuLocationingTable,
       "apMuLocationingEntry": apMuLocationingEntry,
       "apMuLocationingIndex": apMuLocationingIndex,
       "apMuLocationingMuMac": apMuLocationingMuMac,
       "apMuLocationingPortalMac": apMuLocationingPortalMac,
       "apMuLocationingSignalStrength": apMuLocationingSignalStrength,
       "apMuLocationingHeardChannel": apMuLocationingHeardChannel,
       "apMuLocationingHeardTime": apMuLocationingHeardTime,
       "apMuLocationingAddEntryToTable": apMuLocationingAddEntryToTable,
       "apMuLocationingAddEntryToEntry": apMuLocationingAddEntryToEntry,
       "apMuLocationingAddMuMac": apMuLocationingAddMuMac,
       "apMuLocationingAddPortalMac": apMuLocationingAddPortalMac,
       "apMuLocationingAddSignalStrength": apMuLocationingAddSignalStrength,
       "apMuLocationingAddHeardChannel": apMuLocationingAddHeardChannel,
       "apMuLocationingAddHeardTime": apMuLocationingAddHeardTime,
       "apIpFilter": apIpFilter,
       "apIpFilterPolicyTable": apIpFilterPolicyTable,
       "apIpFilterPolicyEntry": apIpFilterPolicyEntry,
       "apIpFilterPolicyIndex": apIpFilterPolicyIndex,
       "apIpFilterPolicyName": apIpFilterPolicyName,
       "apIpFilterPolicyProtocol": apIpFilterPolicyProtocol,
       "apIpFilterPolicyStartPort": apIpFilterPolicyStartPort,
       "apIpFilterPolicyEndPort": apIpFilterPolicyEndPort,
       "apIpFilterPolicySrcStartIp": apIpFilterPolicySrcStartIp,
       "apIpFilterPolicySrcEndIp": apIpFilterPolicySrcEndIp,
       "apIpFilterPolicyDestStartIp": apIpFilterPolicyDestStartIp,
       "apIpFilterPolicyDestEndIp": apIpFilterPolicyDestEndIp,
       "apIpFilterPolicyUseStatus": apIpFilterPolicyUseStatus,
       "apIpFilterPolicyRowStatus": apIpFilterPolicyRowStatus,
       "apIpFilterPolicySrcStartPort": apIpFilterPolicySrcStartPort,
       "apIpFilterPolicySrcEndPort": apIpFilterPolicySrcEndPort,
       "apIpFilterWlan": apIpFilterWlan,
       "apIpFilterWlanTable": apIpFilterWlanTable,
       "apIpFilterWlanEntry": apIpFilterWlanEntry,
       "apIpFilterWlanMode": apIpFilterWlanMode,
       "apIpFilterWlanDefInAction": apIpFilterWlanDefInAction,
       "apIpFilterWlanDefOutAction": apIpFilterWlanDefOutAction,
       "apIpFilterWlanInPackets": apIpFilterWlanInPackets,
       "apIpFilterWlanOutPackets": apIpFilterWlanOutPackets,
       "apIpFilterWlanPolicyTable": apIpFilterWlanPolicyTable,
       "apIpFilterWlanPolicyEntry": apIpFilterWlanPolicyEntry,
       "apIpFilterWlanPolicyIndex": apIpFilterWlanPolicyIndex,
       "apIpFilterWlanPolicyPolicy": apIpFilterWlanPolicyPolicy,
       "apIpFilterWlanPolicyDirection": apIpFilterWlanPolicyDirection,
       "apIpFilterWlanPolicyAction": apIpFilterWlanPolicyAction,
       "apIpFilterWlanPolicyRowStatus": apIpFilterWlanPolicyRowStatus,
       "apIpFilterWlanPolicyPackets": apIpFilterWlanPolicyPackets,
       "apIpFilterLan": apIpFilterLan,
       "apIpFilterLanTable": apIpFilterLanTable,
       "apIpFilterLanEntry": apIpFilterLanEntry,
       "apIpFilterLanIndex": apIpFilterLanIndex,
       "apIpFilterLanMode": apIpFilterLanMode,
       "apIpFilterLanDefInAction": apIpFilterLanDefInAction,
       "apIpFilterLanDefOutAction": apIpFilterLanDefOutAction,
       "apIpFilterLanInPackets": apIpFilterLanInPackets,
       "apIpFilterLanOutPackets": apIpFilterLanOutPackets,
       "apIpFilterLanPolicyTable": apIpFilterLanPolicyTable,
       "apIpFilterLanPolicyEntry": apIpFilterLanPolicyEntry,
       "apIpFilterLanPolicyIndex": apIpFilterLanPolicyIndex,
       "apIpFilterLanPolicyPolicy": apIpFilterLanPolicyPolicy,
       "apIpFilterLanPolicyDirection": apIpFilterLanPolicyDirection,
       "apIpFilterLanPolicyAction": apIpFilterLanPolicyAction,
       "apIpFilterLanPolicyRowStatus": apIpFilterLanPolicyRowStatus,
       "apIpFilterLanPolicyPackets": apIpFilterLanPolicyPackets,
       "apReliableMulticast": apReliableMulticast,
       "apReliableMulticastMode": apReliableMulticastMode,
       "apReliableMulticastWlan": apReliableMulticastWlan,
       "apReliableMulticastMaxStreams": apReliableMulticastMaxStreams,
       "apReliableMulticastStandaloneMode": apReliableMulticastStandaloneMode,
       "apReliableMulticastIgmpQueryVersion": apReliableMulticastIgmpQueryVersion,
       "apReliableMulticastIgmpQueryInterval": apReliableMulticastIgmpQueryInterval,
       "apReliableMulticastTxMulticast": apReliableMulticastTxMulticast,
       "apReliableMulticastTable": apReliableMulticastTable,
       "apReliableMulticastEntry": apReliableMulticastEntry,
       "apReliableMulticastAddrIndex": apReliableMulticastAddrIndex,
       "apReliableMulticastAddress": apReliableMulticastAddress,
       "apReliableMulticastTableRowEnable": apReliableMulticastTableRowEnable,
       "apReliableMulticastMUTable": apReliableMulticastMUTable,
       "apReliableMulticastMUEntry": apReliableMulticastMUEntry,
       "apReliableMulticastMUStatsIndex": apReliableMulticastMUStatsIndex,
       "apReliableMulticastMUStatsIPAddr": apReliableMulticastMUStatsIPAddr,
       "apReliableMulticastMUMacAddr": apReliableMulticastMUMacAddr,
       "apSwitch": apSwitch,
       "apWan": apWan,
       "apWanVpn": apWanVpn,
       "apWanVpnTunnelConfig": apWanVpnTunnelConfig,
       "apWanVpnKeyAutoTable": apWanVpnKeyAutoTable,
       "apWanVpnKeyAutoEntry": apWanVpnKeyAutoEntry,
       "apWanVpnKeyAutoSALifeTime": apWanVpnKeyAutoSALifeTime,
       "apWanPppoe": apWanPppoe,
       "apWanPppoeClientTable": apWanPppoeClientTable,
       "apWanPppoeClientEntry": apWanPppoeClientEntry,
       "apWanPppoeClientIndex": apWanPppoeClientIndex,
       "apWanPppoeClientIp": apWanPppoeClientIp,
       "apWanPppoeClientGateway": apWanPppoeClientGateway,
       "apWanPppoeClientPrimaryDNSServer": apWanPppoeClientPrimaryDNSServer,
       "apWanPppoeClientSecondaryDNSServer": apWanPppoeClientSecondaryDNSServer,
       "apWanPort": apWanPort,
       "apWanPortAutoNegotiation": apWanPortAutoNegotiation,
       "apWanPortSpeed": apWanPortSpeed,
       "apWanPortDuplex": apWanPortDuplex,
       "apWanDynDNS": apWanDynDNS,
       "apWanDynDNSMode": apWanDynDNSMode,
       "apWanDynDNSTable": apWanDynDNSTable,
       "apWanDynDNSEntry": apWanDynDNSEntry,
       "apWanDynDNSUsername": apWanDynDNSUsername,
       "apWanDynDNSPassword": apWanDynDNSPassword,
       "apWanDynDNSHostname": apWanDynDNSHostname,
       "apWanDynDNSIndex": apWanDynDNSIndex,
       "apWanDynDNSUpdateResponseTable": apWanDynDNSUpdateResponseTable,
       "apWanDynDNSUpdateResponseEntry": apWanDynDNSUpdateResponseEntry,
       "apWanDynDNSUpdateHostname": apWanDynDNSUpdateHostname,
       "apWanDynDNSUpdateIp": apWanDynDNSUpdateIp,
       "apWanDynDNSUpdateStatus": apWanDynDNSUpdateStatus,
       "apWanDynDNSUpdateResponseIndex": apWanDynDNSUpdateResponseIndex,
       "apWanDynDNSPerformUpdate": apWanDynDNSPerformUpdate,
       "apLan": apLan,
       "apLanEnable": apLanEnable,
       "apLanTimeOut": apLanTimeOut,
       "apLanTimeOutValue": apLanTimeOutValue,
       "apLanVlanEnable": apLanVlanEnable,
       "apLanAdminVlanTag": apLanAdminVlanTag,
       "apLanNativeVlanTag": apLanNativeVlanTag,
       "apLan802dt1xAuth": apLan802dt1xAuth,
       "apLan802dt1xAuthLogin": apLan802dt1xAuthLogin,
       "apLan802dt1xAuthPass": apLan802dt1xAuthPass,
       "apLanVlan": apLanVlan,
       "apVlanTable": apVlanTable,
       "apVlanEntry": apVlanEntry,
       "apVlanIndex": apVlanIndex,
       "apVlanId": apVlanId,
       "apVlanName": apVlanName,
       "apVlanPointerToWlan": apVlanPointerToWlan,
       "apVlanRowStatus": apVlanRowStatus,
       "apSubnet": apSubnet,
       "apSubnetTable": apSubnetTable,
       "apSubnetEntry": apSubnetEntry,
       "apSubnetDhcpState": apSubnetDhcpState,
       "apSubnetVlanEnable": apSubnetVlanEnable,
       "apSubnetTypeFilterAccessMode": apSubnetTypeFilterAccessMode,
       "apSubnetAdminVlanTag": apSubnetAdminVlanTag,
       "apSubnetNativeVlanTag": apSubnetNativeVlanTag,
       "apLanTypeFilterAccessMode": apLanTypeFilterAccessMode,
       "apLanTypeFilterTable": apLanTypeFilterTable,
       "apLanTypeFilterEntry": apLanTypeFilterEntry,
       "apLanTypeFilterSubnetIndex": apLanTypeFilterSubnetIndex,
       "apLanTypeFilterIndex": apLanTypeFilterIndex,
       "apLanTypeFilter": apLanTypeFilter,
       "apLanTypeFilterRowStatus": apLanTypeFilterRowStatus,
       "apLanEthernetPort": apLanEthernetPort,
       "apLanBridgeTable": apLanBridgeTable,
       "apLanBridgeEntry": apLanBridgeEntry,
       "apLanBridgePriority": apLanBridgePriority,
       "apLanBridgeMaxMsgAge": apLanBridgeMaxMsgAge,
       "apLanBridgeHelloTime": apLanBridgeHelloTime,
       "apLanBridgeFwdDelay": apLanBridgeFwdDelay,
       "apLanBridgeEntryAgeout": apLanBridgeEntryAgeout,
       "apLanPort": apLanPort,
       "apLanPortAutoNegotiation": apLanPortAutoNegotiation,
       "apLanPortSpeed": apLanPortSpeed,
       "apLanPortDuplex": apLanPortDuplex,
       "apWnmpPing": apWnmpPing,
       "apWnmpPingDestMu": apWnmpPingDestMu,
       "apWnmpPingDestAP": apWnmpPingDestAP,
       "apWnmpPingDest": apWnmpPingDest,
       "apWnmpPingNum": apWnmpPingNum,
       "apWnmpPingPacketLength": apWnmpPingPacketLength,
       "apWnmpPingPacketData": apWnmpPingPacketData,
       "apWnmpPingAction": apWnmpPingAction,
       "apWnmpPingNumResponses": apWnmpPingNumResponses,
       "apFlashLed": apFlashLed,
       "apFlashLedDestAP": apFlashLedDestAP,
       "apFlashLedAction": apFlashLedAction,
       "apKnownAPList": apKnownAPList,
       "apKnownApTable": apKnownApTable,
       "apKnownApEntry": apKnownApEntry,
       "apKnownApIndex": apKnownApIndex,
       "apKnownApMac": apKnownApMac,
       "apKnownApIp": apKnownApIp,
       "apKnownApChannel1": apKnownApChannel1,
       "apKnownApChannel2": apKnownApChannel2,
       "apKnownApMu": apKnownApMu,
       "apKnownApKbPerSec": apKnownApKbPerSec,
       "apKnownApPktsPerSec": apKnownApPktsPerSec,
       "apKnownApRadioType1": apKnownApRadioType1,
       "apKnownApRadioType2": apKnownApRadioType2,
       "apKnownApType": apKnownApType,
       "apKnownApFwVers": apKnownApFwVers,
       "apKnownApUnitName": apKnownApUnitName,
       "apKnownApEssName": apKnownApEssName,
       "apKnownApSendCfg": apKnownApSendCfg,
       "apKnownApSendCfgStatus": apKnownApSendCfgStatus,
       "apKnownApRadio1ClientBridgeMac1": apKnownApRadio1ClientBridgeMac1,
       "apKnownApRadio1ClientBridgeMac2": apKnownApRadio1ClientBridgeMac2,
       "apKnownApRadio1ClientBridgeMac3": apKnownApRadio1ClientBridgeMac3,
       "apKnownApRadio2ClientBridgeMac1": apKnownApRadio2ClientBridgeMac1,
       "apKnownApRadio2ClientBridgeMac2": apKnownApRadio2ClientBridgeMac2,
       "apKnownApRadio2ClientBridgeMac3": apKnownApRadio2ClientBridgeMac3,
       "apAap": apAap,
       "apAapSwitchAutoDiscoveryEnable": apAapSwitchAutoDiscoveryEnable,
       "apAapSwitchDiscoveryInterface": apAapSwitchDiscoveryInterface,
       "apAapSwitchDiscoveryIPAddressTable": apAapSwitchDiscoveryIPAddressTable,
       "apAapSwitchDiscoveryIPAddressEntry": apAapSwitchDiscoveryIPAddressEntry,
       "apAapSwitchDiscoveryIPAddressIndex": apAapSwitchDiscoveryIPAddressIndex,
       "apAapSwitchDiscoveryIPAddress": apAapSwitchDiscoveryIPAddress,
       "apAapSwitchDiscoveryIPAddressRowStatus": apAapSwitchDiscoveryIPAddressRowStatus,
       "apAapSwitchDiscoveryDomainName": apAapSwitchDiscoveryDomainName,
       "apAapSwitchDiscoveryPort": apAapSwitchDiscoveryPort,
       "apAapPassphrase": apAapPassphrase,
       "apAapTunnelToSwitchEnable": apAapTunnelToSwitchEnable,
       "apAapAcKeepAlive": apAapAcKeepAlive,
       "apAapAdoptionState": apAapAdoptionState,
       "apAapAdoptingSwitchIP": apAapAdoptingSwitchIP,
       "apNotifications": apNotifications,
       "apMuVlan": apMuVlan,
       "apLanMonitor": apLanMonitor,
       "apWpaCounterMeasure": apWpaCounterMeasure,
       "apMuHotspotState": apMuHotspotState,
       "apDynDNSUpdate": apDynDNSUpdate,
       "apTrapCtrl": apTrapCtrl,
       "apTrapCtrlEnableTable": apTrapCtrlEnableTable,
       "apTrapCtrlEnableEntry": apTrapCtrlEnableEntry,
       "apTrapCtrlEnableIndex": apTrapCtrlEnableIndex,
       "apTrapCtrlEnableName": apTrapCtrlEnableName,
       "apTrapCtrlEnable": apTrapCtrlEnable,
       "apTrapCtrlRateLimit": apTrapCtrlRateLimit,
       "apTrapCtrlSumStats": apTrapCtrlSumStats,
       "apTrapCtrlSumStatsTable": apTrapCtrlSumStatsTable,
       "apTrapCtrlSumStatsEntry": apTrapCtrlSumStatsEntry,
       "apTrapCtrlSumStatsIndex": apTrapCtrlSumStatsIndex,
       "apTrapCtrlSumStatsDescr": apTrapCtrlSumStatsDescr,
       "apTrapCtrlSumStatsUnits": apTrapCtrlSumStatsUnits,
       "apTrapCtrlSumStatsCanBeSetMu": apTrapCtrlSumStatsCanBeSetMu,
       "apTrapCtrlSumStatsThresholdMu": apTrapCtrlSumStatsThresholdMu,
       "apTrapCtrlSumStatsCanBeSetRadioA": apTrapCtrlSumStatsCanBeSetRadioA,
       "apTrapCtrlSumStatsThresholdRadioA": apTrapCtrlSumStatsThresholdRadioA,
       "apTrapCtrlSumStatsCanBeSetRadioBG": apTrapCtrlSumStatsCanBeSetRadioBG,
       "apTrapCtrlSumStatsThresholdRadioBG": apTrapCtrlSumStatsThresholdRadioBG,
       "apTrapCtrlSumStatsCanBeSetWlan": apTrapCtrlSumStatsCanBeSetWlan,
       "apTrapCtrlSumStatsThresholdWlans": apTrapCtrlSumStatsThresholdWlans,
       "apTrapCtrlSumStatsCanBeSetAccessPoint": apTrapCtrlSumStatsCanBeSetAccessPoint,
       "apTrapCtrlSumStatsThresholdAccessPoint": apTrapCtrlSumStatsThresholdAccessPoint,
       "apTrapCtrlSumStatsCanBeSetRadioN5000MHz": apTrapCtrlSumStatsCanBeSetRadioN5000MHz,
       "apTrapCtrlSumStatsThresholdRadioN5000MHz": apTrapCtrlSumStatsThresholdRadioN5000MHz,
       "apTrapCtrlSumStatsCanBeSetRadioN2400MHz": apTrapCtrlSumStatsCanBeSetRadioN2400MHz,
       "apTrapCtrlSumStatsThresholdRadioN2400MHz": apTrapCtrlSumStatsThresholdRadioN2400MHz,
       "apTrapMuVlan": apTrapMuVlan,
       "apTrapMuMac": apTrapMuMac,
       "apTrapRadioMac": apTrapRadioMac,
       "apTrapVlanId": apTrapVlanId,
       "apTrapLanMonitor": apTrapLanMonitor,
       "apTrapLanMonitorMode": apTrapLanMonitorMode,
       "apTrapLanMonitorReason": apTrapLanMonitorReason,
       "apTrapWpaCounterMeasure": apTrapWpaCounterMeasure,
       "apTrapWpaCounterMeasureEssid": apTrapWpaCounterMeasureEssid,
       "apTrapCtrlMuHotspotState": apTrapCtrlMuHotspotState,
       "apTrapCtrlMuMac": apTrapCtrlMuMac,
       "apTrapCtrlMuHotspotStateChange": apTrapCtrlMuHotspotStateChange,
       "apTrapCtrlDynDNSUpdate": apTrapCtrlDynDNSUpdate,
       "apTrapCtrlDynDNSUpdateIp": apTrapCtrlDynDNSUpdateIp,
       "apTrapCtrlDynDNSUpdateHostname": apTrapCtrlDynDNSUpdateHostname,
       "apTrapCtrlDynDNSUpdateStatus": apTrapCtrlDynDNSUpdateStatus,
       "apRap": apRap,
       "apRapControl": apRapControl,
       "apRapControlDetectors": apRapControlDetectors,
       "apRapDetectorMode": apRapDetectorMode,
       "apRapDetectorABGMode": apRapDetectorABGMode,
       "apLoadCfg": apLoadCfg,
       "apLoadCfgOperation": apLoadCfgOperation,
       "apLoadCfgServerPath": apLoadCfgServerPath,
       "apLoadCfgServerFilename": apLoadCfgServerFilename,
       "apLoadCfgServerIpAddr": apLoadCfgServerIpAddr,
       "apLoadCfgFtpUsername": apLoadCfgFtpUsername,
       "apLoadCfgFtpPassword": apLoadCfgFtpPassword,
       "apLoadCfgStart": apLoadCfgStart,
       "apLoadCfgOperationsDone": apLoadCfgOperationsDone,
       "apLoadCfgResult": apLoadCfgResult,
       "apLoadCfgSuccess": apLoadCfgSuccess,
       "apStats": apStats,
       "apWanClearStats": apWanClearStats,
       "apLanClearStats": apLanClearStats,
       "apRadioClearStats": apRadioClearStats,
       "apWlanClearStats": apWlanClearStats,
       "apMuClearStats": apMuClearStats,
       "apKnownAPClearStats": apKnownAPClearStats,
       "apWirelessAPStats": apWirelessAPStats,
       "apMeshStatsTable": apMeshStatsTable,
       "apMeshStatsEntry": apMeshStatsEntry,
       "apMeshStatsIndex": apMeshStatsIndex,
       "apMeshStatsConnType": apMeshStatsConnType,
       "apMeshStatsMac": apMeshStatsMac,
       "apMeshStatsWlanPtr": apMeshStatsWlanPtr,
       "apMeshStatsRadioType": apMeshStatsRadioType,
       "apMeshStatsThroughput": apMeshStatsThroughput,
       "apMeshStatsAvgBitSpeed": apMeshStatsAvgBitSpeed,
       "apMeshStatsRetries": apMeshStatsRetries,
       "apMeshBridgeStatsTable": apMeshBridgeStatsTable,
       "apMeshBridgeStatsEntry": apMeshBridgeStatsEntry,
       "apMeshBridgeStatsIndex": apMeshBridgeStatsIndex,
       "apMeshBridgeStatsMac": apMeshBridgeStatsMac,
       "apMeshBridgeStatsWlanPtr": apMeshBridgeStatsWlanPtr,
       "apMeshBridgeStatsLanPtr": apMeshBridgeStatsLanPtr,
       "apMeshBridgeStatsRadioType": apMeshBridgeStatsRadioType,
       "apMeshBridgeStatsAuthType": apMeshBridgeStatsAuthType,
       "apMeshBridgeStatsEncType": apMeshBridgeStatsEncType,
       "apMeshBridgeStatsPktsPerSecRx": apMeshBridgeStatsPktsPerSecRx,
       "apMeshBridgeStatsPksPerSecTx": apMeshBridgeStatsPksPerSecTx,
       "apMeshBridgeStatsPktsPerSecTotal": apMeshBridgeStatsPktsPerSecTotal,
       "apMeshBridgeStatsThroughputRx": apMeshBridgeStatsThroughputRx,
       "apMeshBridgeStatsThroughputTx": apMeshBridgeStatsThroughputTx,
       "apMeshBridgeStatsThroughputTotal": apMeshBridgeStatsThroughputTotal,
       "apMeshBridgeStatsAvgBitSpeed": apMeshBridgeStatsAvgBitSpeed,
       "apMeshBridgeStatsAvgMuSignal": apMeshBridgeStatsAvgMuSignal,
       "apMeshBridgeStatsAvgMuNoise": apMeshBridgeStatsAvgMuNoise,
       "apMeshBridgeStatsAvgMuSnr": apMeshBridgeStatsAvgMuSnr,
       "apMeshBridgeStatsAvgRetries": apMeshBridgeStatsAvgRetries,
       "apMeshBridgeStatsPktsDropped": apMeshBridgeStatsPktsDropped,
       "apMeshBridgeStatsUndecryptablePkts": apMeshBridgeStatsUndecryptablePkts,
       "apLanSTPStatsTable": apLanSTPStatsTable,
       "apLanSTPStatsEntry": apLanSTPStatsEntry,
       "apLanSTPStatsDesignatedRoot": apLanSTPStatsDesignatedRoot,
       "apLanSTPStatsBridgeId": apLanSTPStatsBridgeId,
       "apLanSTPStatsRootPort": apLanSTPStatsRootPort,
       "apLanSTPStatsRootPathCost": apLanSTPStatsRootPathCost,
       "apLanSTPStatsBridgeMaxMsgAge": apLanSTPStatsBridgeMaxMsgAge,
       "apLanSTPStatsBridgeHelloTime": apLanSTPStatsBridgeHelloTime,
       "apLanSTPStatsBridgeFwDelay": apLanSTPStatsBridgeFwDelay,
       "apLanSTPStatsPortIntfTable": apLanSTPStatsPortIntfTable,
       "apLanSTPStatsPortIntfEntry": apLanSTPStatsPortIntfEntry,
       "apLanSTPStatsPortIntfLanIndex": apLanSTPStatsPortIntfLanIndex,
       "apLanSTPStatsPortIntfPortIndex": apLanSTPStatsPortIntfPortIndex,
       "apLanSTPStatsPortIntfPortName": apLanSTPStatsPortIntfPortName,
       "apLanSTPStatsPortIntfState": apLanSTPStatsPortIntfState,
       "apLanSTPStatsPortIntfPathCost": apLanSTPStatsPortIntfPathCost,
       "apLanSTPStatsPortIntfDsgRoot": apLanSTPStatsPortIntfDsgRoot,
       "apLanSTPStatsPortIntfDsgBridge": apLanSTPStatsPortIntfDsgBridge,
       "apLanSTPStatsPortIntfDsgPort": apLanSTPStatsPortIntfDsgPort,
       "apLanSTPStatsPortIntfDsgCost": apLanSTPStatsPortIntfDsgCost,
       "apnStats": apnStats,
       "apnRadioStatsTable": apnRadioStatsTable,
       "apnRadioStatsEntry": apnRadioStatsEntry,
       "apnRadioStatsIndex": apnRadioStatsIndex,
       "apnRadioStatsBssid": apnRadioStatsBssid,
       "apnRadioStatsApSsid": apnRadioStatsApSsid,
       "apnRadioStatsChannel": apnRadioStatsChannel,
       "apnRadioStatsExtnChannel": apnRadioStatsExtnChannel,
       "apnRadioStatsRssiAvgAcrossAntennas": apnRadioStatsRssiAvgAcrossAntennas,
       "apnRadioStatsChannelWidthMode": apnRadioStatsChannelWidthMode,
       "apnRadioStatsOpFreq": apnRadioStatsOpFreq,
       "apnRadioStatsNumPktsRxSGI400ns": apnRadioStatsNumPktsRxSGI400ns,
       "apnRadioStatsNumPktsRxSGI800ns": apnRadioStatsNumPktsRxSGI800ns,
       "apnRadioStatsNumPktsTxSGI400ns": apnRadioStatsNumPktsTxSGI400ns,
       "apnRadioStatsNumPktsTxSGI800ns": apnRadioStatsNumPktsTxSGI800ns,
       "apnRadioStatsNumPktsRxChanWidth20MHz": apnRadioStatsNumPktsRxChanWidth20MHz,
       "apnRadioStatsNumPktsRxChanWidth40MHz": apnRadioStatsNumPktsRxChanWidth40MHz,
       "apnRadioStatsNumPktsTxChanWidth20MHz": apnRadioStatsNumPktsTxChanWidth20MHz,
       "apnRadioStatsNumPktsTxChanWidth40MHz": apnRadioStatsNumPktsTxChanWidth40MHz,
       "apnPortalRxPktsTable": apnPortalRxPktsTable,
       "apnPortalRxPktsEntry": apnPortalRxPktsEntry,
       "apnPortalRxPktsAt1Mb": apnPortalRxPktsAt1Mb,
       "apnPortalRxPktsAt2Mb": apnPortalRxPktsAt2Mb,
       "apnPortalRxPktsAt5pt5Mb": apnPortalRxPktsAt5pt5Mb,
       "apnPortalRxPktsAt6Mb": apnPortalRxPktsAt6Mb,
       "apnPortalRxPktsAt9Mb": apnPortalRxPktsAt9Mb,
       "apnPortalRxPktsAt11Mb": apnPortalRxPktsAt11Mb,
       "apnPortalRxPktsAt12Mb": apnPortalRxPktsAt12Mb,
       "apnPortalRxPktsAt18Mb": apnPortalRxPktsAt18Mb,
       "apnPortalRxPktsAt24Mb": apnPortalRxPktsAt24Mb,
       "apnPortalRxPktsAt36Mb": apnPortalRxPktsAt36Mb,
       "apnPortalRxPktsAt48Mb": apnPortalRxPktsAt48Mb,
       "apnPortalRxPktsAt54Mb": apnPortalRxPktsAt54Mb,
       "apnPortalRxPktsAtMCS0": apnPortalRxPktsAtMCS0,
       "apnPortalRxPktsAtMCS1": apnPortalRxPktsAtMCS1,
       "apnPortalRxPktsAtMCS2": apnPortalRxPktsAtMCS2,
       "apnPortalRxPktsAtMCS3": apnPortalRxPktsAtMCS3,
       "apnPortalRxPktsAtMCS4": apnPortalRxPktsAtMCS4,
       "apnPortalRxPktsAtMCS5": apnPortalRxPktsAtMCS5,
       "apnPortalRxPktsAtMCS6": apnPortalRxPktsAtMCS6,
       "apnPortalRxPktsAtMCS7": apnPortalRxPktsAtMCS7,
       "apnPortalRxPktsAtMCS8": apnPortalRxPktsAtMCS8,
       "apnPortalRxPktsAtMCS9": apnPortalRxPktsAtMCS9,
       "apnPortalRxPktsAtMCS10": apnPortalRxPktsAtMCS10,
       "apnPortalRxPktsAtMCS11": apnPortalRxPktsAtMCS11,
       "apnPortalRxPktsAtMCS12": apnPortalRxPktsAtMCS12,
       "apnPortalRxPktsAtMCS13": apnPortalRxPktsAtMCS13,
       "apnPortalRxPktsAtMCS14": apnPortalRxPktsAtMCS14,
       "apnPortalRxPktsAtMCS15": apnPortalRxPktsAtMCS15,
       "apnPortalTxPktsTable": apnPortalTxPktsTable,
       "apnPortalTxPktsEntry": apnPortalTxPktsEntry,
       "apnPortalTxPktsAt1Mb": apnPortalTxPktsAt1Mb,
       "apnPortalTxPktsAt2Mb": apnPortalTxPktsAt2Mb,
       "apnPortalTxPktsAt5pt5Mb": apnPortalTxPktsAt5pt5Mb,
       "apnPortalTxPktsAt6Mb": apnPortalTxPktsAt6Mb,
       "apnPortalTxPktsAt9Mb": apnPortalTxPktsAt9Mb,
       "apnPortalTxPktsAt11Mb": apnPortalTxPktsAt11Mb,
       "apnPortalTxPktsAt12Mb": apnPortalTxPktsAt12Mb,
       "apnPortalTxPktsAt18Mb": apnPortalTxPktsAt18Mb,
       "apnPortalTxPktsAt24Mb": apnPortalTxPktsAt24Mb,
       "apnPortalTxPktsAt36Mb": apnPortalTxPktsAt36Mb,
       "apnPortalTxPktsAt48Mb": apnPortalTxPktsAt48Mb,
       "apnPortalTxPktsAt54Mb": apnPortalTxPktsAt54Mb,
       "apnPortalTxPktsAtMCS0": apnPortalTxPktsAtMCS0,
       "apnPortalTxPktsAtMCS1": apnPortalTxPktsAtMCS1,
       "apnPortalTxPktsAtMCS2": apnPortalTxPktsAtMCS2,
       "apnPortalTxPktsAtMCS3": apnPortalTxPktsAtMCS3,
       "apnPortalTxPktsAtMCS4": apnPortalTxPktsAtMCS4,
       "apnPortalTxPktsAtMCS5": apnPortalTxPktsAtMCS5,
       "apnPortalTxPktsAtMCS6": apnPortalTxPktsAtMCS6,
       "apnPortalTxPktsAtMCS7": apnPortalTxPktsAtMCS7,
       "apnPortalTxPktsAtMCS8": apnPortalTxPktsAtMCS8,
       "apnPortalTxPktsAtMCS9": apnPortalTxPktsAtMCS9,
       "apnPortalTxPktsAtMCS10": apnPortalTxPktsAtMCS10,
       "apnPortalTxPktsAtMCS11": apnPortalTxPktsAtMCS11,
       "apnPortalTxPktsAtMCS12": apnPortalTxPktsAtMCS12,
       "apnPortalTxPktsAtMCS13": apnPortalTxPktsAtMCS13,
       "apnPortalTxPktsAtMCS14": apnPortalTxPktsAtMCS14,
       "apnPortalTxPktsAtMCS15": apnPortalTxPktsAtMCS15,
       "apnPortalRxOctetsTable": apnPortalRxOctetsTable,
       "apnPortalRxOctetsEntry": apnPortalRxOctetsEntry,
       "apnPortalRxOctetsAt1Mb": apnPortalRxOctetsAt1Mb,
       "apnPortalRxOctetsAt2Mb": apnPortalRxOctetsAt2Mb,
       "apnPortalRxOctetsAt5pt5Mb": apnPortalRxOctetsAt5pt5Mb,
       "apnPortalRxOctetsAt6Mb": apnPortalRxOctetsAt6Mb,
       "apnPortalRxOctetsAt9Mb": apnPortalRxOctetsAt9Mb,
       "apnPortalRxOctetsAt11Mb": apnPortalRxOctetsAt11Mb,
       "apnPortalRxOctetsAt12Mb": apnPortalRxOctetsAt12Mb,
       "apnPortalRxOctetsAt18Mb": apnPortalRxOctetsAt18Mb,
       "apnPortalRxOctetsAt24Mb": apnPortalRxOctetsAt24Mb,
       "apnPortalRxOctetsAt36Mb": apnPortalRxOctetsAt36Mb,
       "apnPortalRxOctetsAt48Mb": apnPortalRxOctetsAt48Mb,
       "apnPortalRxOctetsAt54Mb": apnPortalRxOctetsAt54Mb,
       "apnPortalRxOctetsAtMCS0": apnPortalRxOctetsAtMCS0,
       "apnPortalRxOctetsAtMCS1": apnPortalRxOctetsAtMCS1,
       "apnPortalRxOctetsAtMCS2": apnPortalRxOctetsAtMCS2,
       "apnPortalRxOctetsAtMCS3": apnPortalRxOctetsAtMCS3,
       "apnPortalRxOctetsAtMCS4": apnPortalRxOctetsAtMCS4,
       "apnPortalRxOctetsAtMCS5": apnPortalRxOctetsAtMCS5,
       "apnPortalRxOctetsAtMCS6": apnPortalRxOctetsAtMCS6,
       "apnPortalRxOctetsAtMCS7": apnPortalRxOctetsAtMCS7,
       "apnPortalRxOctetsAtMCS8": apnPortalRxOctetsAtMCS8,
       "apnPortalRxOctetsAtMCS9": apnPortalRxOctetsAtMCS9,
       "apnPortalRxOctetsAtMCS10": apnPortalRxOctetsAtMCS10,
       "apnPortalRxOctetsAtMCS11": apnPortalRxOctetsAtMCS11,
       "apnPortalRxOctetsAtMCS12": apnPortalRxOctetsAtMCS12,
       "apnPortalRxOctetsAtMCS13": apnPortalRxOctetsAtMCS13,
       "apnPortalRxOctetsAtMCS14": apnPortalRxOctetsAtMCS14,
       "apnPortalRxOctetsAtMCS15": apnPortalRxOctetsAtMCS15,
       "apnPortalTxOctetsTable": apnPortalTxOctetsTable,
       "apnPortalTxOctetsEntry": apnPortalTxOctetsEntry,
       "apnPortalTxOctetsAt1Mb": apnPortalTxOctetsAt1Mb,
       "apnPortalTxOctetsAt2Mb": apnPortalTxOctetsAt2Mb,
       "apnPortalTxOctetsAt5pt5Mb": apnPortalTxOctetsAt5pt5Mb,
       "apnPortalTxOctetsAt6Mb": apnPortalTxOctetsAt6Mb,
       "apnPortalTxOctetsAt9Mb": apnPortalTxOctetsAt9Mb,
       "apnPortalTxOctetsAt11Mb": apnPortalTxOctetsAt11Mb,
       "apnPortalTxOctetsAt12Mb": apnPortalTxOctetsAt12Mb,
       "apnPortalTxOctetsAt18Mb": apnPortalTxOctetsAt18Mb,
       "apnPortalTxOctetsAt24Mb": apnPortalTxOctetsAt24Mb,
       "apnPortalTxOctetsAt36Mb": apnPortalTxOctetsAt36Mb,
       "apnPortalTxOctetsAt48Mb": apnPortalTxOctetsAt48Mb,
       "apnPortalTxOctetsAt54Mb": apnPortalTxOctetsAt54Mb,
       "apnPortalTxOctetsAtMCS0": apnPortalTxOctetsAtMCS0,
       "apnPortalTxOctetsAtMCS1": apnPortalTxOctetsAtMCS1,
       "apnPortalTxOctetsAtMCS2": apnPortalTxOctetsAtMCS2,
       "apnPortalTxOctetsAtMCS3": apnPortalTxOctetsAtMCS3,
       "apnPortalTxOctetsAtMCS4": apnPortalTxOctetsAtMCS4,
       "apnPortalTxOctetsAtMCS5": apnPortalTxOctetsAtMCS5,
       "apnPortalTxOctetsAtMCS6": apnPortalTxOctetsAtMCS6,
       "apnPortalTxOctetsAtMCS7": apnPortalTxOctetsAtMCS7,
       "apnPortalTxOctetsAtMCS8": apnPortalTxOctetsAtMCS8,
       "apnPortalTxOctetsAtMCS9": apnPortalTxOctetsAtMCS9,
       "apnPortalTxOctetsAtMCS10": apnPortalTxOctetsAtMCS10,
       "apnPortalTxOctetsAtMCS11": apnPortalTxOctetsAtMCS11,
       "apnPortalTxOctetsAtMCS12": apnPortalTxOctetsAtMCS12,
       "apnPortalTxOctetsAtMCS13": apnPortalTxOctetsAtMCS13,
       "apnPortalTxOctetsAtMCS14": apnPortalTxOctetsAtMCS14,
       "apnPortalTxOctetsAtMCS15": apnPortalTxOctetsAtMCS15,
       "apnMuRxPktsTable": apnMuRxPktsTable,
       "apnMuRxPktsEntry": apnMuRxPktsEntry,
       "apnMuRxPktsAt1Mb": apnMuRxPktsAt1Mb,
       "apnMuRxPktsAt2Mb": apnMuRxPktsAt2Mb,
       "apnMuRxPktsAt5pt5Mb": apnMuRxPktsAt5pt5Mb,
       "apnMuRxPktsAt6Mb": apnMuRxPktsAt6Mb,
       "apnMuRxPktsAt9Mb": apnMuRxPktsAt9Mb,
       "apnMuRxPktsAt11Mb": apnMuRxPktsAt11Mb,
       "apnMuRxPktsAt12Mb": apnMuRxPktsAt12Mb,
       "apnMuRxPktsAt18Mb": apnMuRxPktsAt18Mb,
       "apnMuRxPktsAt24Mb": apnMuRxPktsAt24Mb,
       "apnMuRxPktsAt36Mb": apnMuRxPktsAt36Mb,
       "apnMuRxPktsAt48Mb": apnMuRxPktsAt48Mb,
       "apnMuRxPktsAt54Mb": apnMuRxPktsAt54Mb,
       "apnMuRxPktsAtMCS0": apnMuRxPktsAtMCS0,
       "apnMuRxPktsAtMCS1": apnMuRxPktsAtMCS1,
       "apnMuRxPktsAtMCS2": apnMuRxPktsAtMCS2,
       "apnMuRxPktsAtMCS3": apnMuRxPktsAtMCS3,
       "apnMuRxPktsAtMCS4": apnMuRxPktsAtMCS4,
       "apnMuRxPktsAtMCS5": apnMuRxPktsAtMCS5,
       "apnMuRxPktsAtMCS6": apnMuRxPktsAtMCS6,
       "apnMuRxPktsAtMCS7": apnMuRxPktsAtMCS7,
       "apnMuRxPktsAtMCS8": apnMuRxPktsAtMCS8,
       "apnMuRxPktsAtMCS9": apnMuRxPktsAtMCS9,
       "apnMuRxPktsAtMCS10": apnMuRxPktsAtMCS10,
       "apnMuRxPktsAtMCS11": apnMuRxPktsAtMCS11,
       "apnMuRxPktsAtMCS12": apnMuRxPktsAtMCS12,
       "apnMuRxPktsAtMCS13": apnMuRxPktsAtMCS13,
       "apnMuRxPktsAtMCS14": apnMuRxPktsAtMCS14,
       "apnMuRxPktsAtMCS15": apnMuRxPktsAtMCS15,
       "apnMuTxPktsTable": apnMuTxPktsTable,
       "apnMuTxPktsEntry": apnMuTxPktsEntry,
       "apnMuTxPktsAt1Mb": apnMuTxPktsAt1Mb,
       "apnMuTxPktsAt2Mb": apnMuTxPktsAt2Mb,
       "apnMuTxPktsAt5pt5Mb": apnMuTxPktsAt5pt5Mb,
       "apnMuTxPktsAt6Mb": apnMuTxPktsAt6Mb,
       "apnMuTxPktsAt9Mb": apnMuTxPktsAt9Mb,
       "apnMuTxPktsAt11Mb": apnMuTxPktsAt11Mb,
       "apnMuTxPktsAt12Mb": apnMuTxPktsAt12Mb,
       "apnMuTxPktsAt18Mb": apnMuTxPktsAt18Mb,
       "apnMuTxPktsAt24Mb": apnMuTxPktsAt24Mb,
       "apnMuTxPktsAt36Mb": apnMuTxPktsAt36Mb,
       "apnMuTxPktsAt48Mb": apnMuTxPktsAt48Mb,
       "apnMuTxPktsAt54Mb": apnMuTxPktsAt54Mb,
       "apnMuTxPktsAtMCS0": apnMuTxPktsAtMCS0,
       "apnMuTxPktsAtMCS1": apnMuTxPktsAtMCS1,
       "apnMuTxPktsAtMCS2": apnMuTxPktsAtMCS2,
       "apnMuTxPktsAtMCS3": apnMuTxPktsAtMCS3,
       "apnMuTxPktsAtMCS4": apnMuTxPktsAtMCS4,
       "apnMuTxPktsAtMCS5": apnMuTxPktsAtMCS5,
       "apnMuTxPktsAtMCS6": apnMuTxPktsAtMCS6,
       "apnMuTxPktsAtMCS7": apnMuTxPktsAtMCS7,
       "apnMuTxPktsAtMCS8": apnMuTxPktsAtMCS8,
       "apnMuTxPktsAtMCS9": apnMuTxPktsAtMCS9,
       "apnMuTxPktsAtMCS10": apnMuTxPktsAtMCS10,
       "apnMuTxPktsAtMCS11": apnMuTxPktsAtMCS11,
       "apnMuTxPktsAtMCS12": apnMuTxPktsAtMCS12,
       "apnMuTxPktsAtMCS13": apnMuTxPktsAtMCS13,
       "apnMuTxPktsAtMCS14": apnMuTxPktsAtMCS14,
       "apnMuTxPktsAtMCS15": apnMuTxPktsAtMCS15,
       "apnMuRxOctetsTable": apnMuRxOctetsTable,
       "apnMuRxOctetsEntry": apnMuRxOctetsEntry,
       "apnMuRxOctetsAt1Mb": apnMuRxOctetsAt1Mb,
       "apnMuRxOctetsAt2Mb": apnMuRxOctetsAt2Mb,
       "apnMuRxOctetsAt5pt5Mb": apnMuRxOctetsAt5pt5Mb,
       "apnMuRxOctetsAt6Mb": apnMuRxOctetsAt6Mb,
       "apnMuRxOctetsAt9Mb": apnMuRxOctetsAt9Mb,
       "apnMuRxOctetsAt11Mb": apnMuRxOctetsAt11Mb,
       "apnMuRxOctetsAt12Mb": apnMuRxOctetsAt12Mb,
       "apnMuRxOctetsAt18Mb": apnMuRxOctetsAt18Mb,
       "apnMuRxOctetsAt24Mb": apnMuRxOctetsAt24Mb,
       "apnMuRxOctetsAt36Mb": apnMuRxOctetsAt36Mb,
       "apnMuRxOctetsAt48Mb": apnMuRxOctetsAt48Mb,
       "apnMuRxOctetsAt54Mb": apnMuRxOctetsAt54Mb,
       "apnMuRxOctetsAtMCS0": apnMuRxOctetsAtMCS0,
       "apnMuRxOctetsAtMCS1": apnMuRxOctetsAtMCS1,
       "apnMuRxOctetsAtMCS2": apnMuRxOctetsAtMCS2,
       "apnMuRxOctetsAtMCS3": apnMuRxOctetsAtMCS3,
       "apnMuRxOctetsAtMCS4": apnMuRxOctetsAtMCS4,
       "apnMuRxOctetsAtMCS5": apnMuRxOctetsAtMCS5,
       "apnMuRxOctetsAtMCS6": apnMuRxOctetsAtMCS6,
       "apnMuRxOctetsAtMCS7": apnMuRxOctetsAtMCS7,
       "apnMuRxOctetsAtMCS8": apnMuRxOctetsAtMCS8,
       "apnMuRxOctetsAtMCS9": apnMuRxOctetsAtMCS9,
       "apnMuRxOctetsAtMCS10": apnMuRxOctetsAtMCS10,
       "apnMuRxOctetsAtMCS11": apnMuRxOctetsAtMCS11,
       "apnMuRxOctetsAtMCS12": apnMuRxOctetsAtMCS12,
       "apnMuRxOctetsAtMCS13": apnMuRxOctetsAtMCS13,
       "apnMuRxOctetsAtMCS14": apnMuRxOctetsAtMCS14,
       "apnMuRxOctetsAtMCS15": apnMuRxOctetsAtMCS15,
       "apnMuTxOctetsTable": apnMuTxOctetsTable,
       "apnMuTxOctetsEntry": apnMuTxOctetsEntry,
       "apnMuTxOctetsAt1Mb": apnMuTxOctetsAt1Mb,
       "apnMuTxOctetsAt2Mb": apnMuTxOctetsAt2Mb,
       "apnMuTxOctetsAt5pt5Mb": apnMuTxOctetsAt5pt5Mb,
       "apnMuTxOctetsAt6Mb": apnMuTxOctetsAt6Mb,
       "apnMuTxOctetsAt9Mb": apnMuTxOctetsAt9Mb,
       "apnMuTxOctetsAt11Mb": apnMuTxOctetsAt11Mb,
       "apnMuTxOctetsAt12Mb": apnMuTxOctetsAt12Mb,
       "apnMuTxOctetsAt18Mb": apnMuTxOctetsAt18Mb,
       "apnMuTxOctetsAt24Mb": apnMuTxOctetsAt24Mb,
       "apnMuTxOctetsAt36Mb": apnMuTxOctetsAt36Mb,
       "apnMuTxOctetsAt48Mb": apnMuTxOctetsAt48Mb,
       "apnMuTxOctetsAt54Mb": apnMuTxOctetsAt54Mb,
       "apnMuTxOctetsAtMCS0": apnMuTxOctetsAtMCS0,
       "apnMuTxOctetsAtMCS1": apnMuTxOctetsAtMCS1,
       "apnMuTxOctetsAtMCS2": apnMuTxOctetsAtMCS2,
       "apnMuTxOctetsAtMCS3": apnMuTxOctetsAtMCS3,
       "apnMuTxOctetsAtMCS4": apnMuTxOctetsAtMCS4,
       "apnMuTxOctetsAtMCS5": apnMuTxOctetsAtMCS5,
       "apnMuTxOctetsAtMCS6": apnMuTxOctetsAtMCS6,
       "apnMuTxOctetsAtMCS7": apnMuTxOctetsAtMCS7,
       "apnMuTxOctetsAtMCS8": apnMuTxOctetsAtMCS8,
       "apnMuTxOctetsAtMCS9": apnMuTxOctetsAtMCS9,
       "apnMuTxOctetsAtMCS10": apnMuTxOctetsAtMCS10,
       "apnMuTxOctetsAtMCS11": apnMuTxOctetsAtMCS11,
       "apnMuTxOctetsAtMCS12": apnMuTxOctetsAtMCS12,
       "apnMuTxOctetsAtMCS13": apnMuTxOctetsAtMCS13,
       "apnMuTxOctetsAtMCS14": apnMuTxOctetsAtMCS14,
       "apnMuTxOctetsAtMCS15": apnMuTxOctetsAtMCS15,
       "apnWlanRxPktsTable": apnWlanRxPktsTable,
       "apnWlanRxPktsEntry": apnWlanRxPktsEntry,
       "apnWlanRxPktsAt1Mb": apnWlanRxPktsAt1Mb,
       "apnWlanRxPktsAt2Mb": apnWlanRxPktsAt2Mb,
       "apnWlanRxPktsAt5pt5Mb": apnWlanRxPktsAt5pt5Mb,
       "apnWlanRxPktsAt6Mb": apnWlanRxPktsAt6Mb,
       "apnWlanRxPktsAt9Mb": apnWlanRxPktsAt9Mb,
       "apnWlanRxPktsAt11Mb": apnWlanRxPktsAt11Mb,
       "apnWlanRxPktsAt12Mb": apnWlanRxPktsAt12Mb,
       "apnWlanRxPktsAt18Mb": apnWlanRxPktsAt18Mb,
       "apnWlanRxPktsAt24Mb": apnWlanRxPktsAt24Mb,
       "apnWlanRxPktsAt36Mb": apnWlanRxPktsAt36Mb,
       "apnWlanRxPktsAt48Mb": apnWlanRxPktsAt48Mb,
       "apnWlanRxPktsAt54Mb": apnWlanRxPktsAt54Mb,
       "apnWlanRxPktsAtMCS0": apnWlanRxPktsAtMCS0,
       "apnWlanRxPktsAtMCS1": apnWlanRxPktsAtMCS1,
       "apnWlanRxPktsAtMCS2": apnWlanRxPktsAtMCS2,
       "apnWlanRxPktsAtMCS3": apnWlanRxPktsAtMCS3,
       "apnWlanRxPktsAtMCS4": apnWlanRxPktsAtMCS4,
       "apnWlanRxPktsAtMCS5": apnWlanRxPktsAtMCS5,
       "apnWlanRxPktsAtMCS6": apnWlanRxPktsAtMCS6,
       "apnWlanRxPktsAtMCS7": apnWlanRxPktsAtMCS7,
       "apnWlanRxPktsAtMCS8": apnWlanRxPktsAtMCS8,
       "apnWlanRxPktsAtMCS9": apnWlanRxPktsAtMCS9,
       "apnWlanRxPktsAtMCS10": apnWlanRxPktsAtMCS10,
       "apnWlanRxPktsAtMCS11": apnWlanRxPktsAtMCS11,
       "apnWlanRxPktsAtMCS12": apnWlanRxPktsAtMCS12,
       "apnWlanRxPktsAtMCS13": apnWlanRxPktsAtMCS13,
       "apnWlanRxPktsAtMCS14": apnWlanRxPktsAtMCS14,
       "apnWlanRxPktsAtMCS15": apnWlanRxPktsAtMCS15,
       "apnWlanTxPktsTable": apnWlanTxPktsTable,
       "apnWlanTxPktsEntry": apnWlanTxPktsEntry,
       "apnWlanTxPktsAt1Mb": apnWlanTxPktsAt1Mb,
       "apnWlanTxPktsAt2Mb": apnWlanTxPktsAt2Mb,
       "apnWlanTxPktsAt5pt5Mb": apnWlanTxPktsAt5pt5Mb,
       "apnWlanTxPktsAt6Mb": apnWlanTxPktsAt6Mb,
       "apnWlanTxPktsAt9Mb": apnWlanTxPktsAt9Mb,
       "apnWlanTxPktsAt11Mb": apnWlanTxPktsAt11Mb,
       "apnWlanTxPktsAt12Mb": apnWlanTxPktsAt12Mb,
       "apnWlanTxPktsAt18Mb": apnWlanTxPktsAt18Mb,
       "apnWlanTxPktsAt24Mb": apnWlanTxPktsAt24Mb,
       "apnWlanTxPktsAt36Mb": apnWlanTxPktsAt36Mb,
       "apnWlanTxPktsAt48Mb": apnWlanTxPktsAt48Mb,
       "apnWlanTxPktsAt54Mb": apnWlanTxPktsAt54Mb,
       "apnWlanTxPktsAtMCS0": apnWlanTxPktsAtMCS0,
       "apnWlanTxPktsAtMCS1": apnWlanTxPktsAtMCS1,
       "apnWlanTxPktsAtMCS2": apnWlanTxPktsAtMCS2,
       "apnWlanTxPktsAtMCS3": apnWlanTxPktsAtMCS3,
       "apnWlanTxPktsAtMCS4": apnWlanTxPktsAtMCS4,
       "apnWlanTxPktsAtMCS5": apnWlanTxPktsAtMCS5,
       "apnWlanTxPktsAtMCS6": apnWlanTxPktsAtMCS6,
       "apnWlanTxPktsAtMCS7": apnWlanTxPktsAtMCS7,
       "apnWlanTxPktsAtMCS8": apnWlanTxPktsAtMCS8,
       "apnWlanTxPktsAtMCS9": apnWlanTxPktsAtMCS9,
       "apnWlanTxPktsAtMCS10": apnWlanTxPktsAtMCS10,
       "apnWlanTxPktsAtMCS11": apnWlanTxPktsAtMCS11,
       "apnWlanTxPktsAtMCS12": apnWlanTxPktsAtMCS12,
       "apnWlanTxPktsAtMCS13": apnWlanTxPktsAtMCS13,
       "apnWlanTxPktsAtMCS14": apnWlanTxPktsAtMCS14,
       "apnWlanTxPktsAtMCS15": apnWlanTxPktsAtMCS15,
       "apnWlanRxOctetsTable": apnWlanRxOctetsTable,
       "apnWlanRxOctetsEntry": apnWlanRxOctetsEntry,
       "apnWlanRxOctetsAt1Mb": apnWlanRxOctetsAt1Mb,
       "apnWlanRxOctetsAt2Mb": apnWlanRxOctetsAt2Mb,
       "apnWlanRxOctetsAt5pt5Mb": apnWlanRxOctetsAt5pt5Mb,
       "apnWlanRxOctetsAt6Mb": apnWlanRxOctetsAt6Mb,
       "apnWlanRxOctetsAt9Mb": apnWlanRxOctetsAt9Mb,
       "apnWlanRxOctetsAt11Mb": apnWlanRxOctetsAt11Mb,
       "apnWlanRxOctetsAt12Mb": apnWlanRxOctetsAt12Mb,
       "apnWlanRxOctetsAt18Mb": apnWlanRxOctetsAt18Mb,
       "apnWlanRxOctetsAt24Mb": apnWlanRxOctetsAt24Mb,
       "apnWlanRxOctetsAt36Mb": apnWlanRxOctetsAt36Mb,
       "apnWlanRxOctetsAt48Mb": apnWlanRxOctetsAt48Mb,
       "apnWlanRxOctetsAt54Mb": apnWlanRxOctetsAt54Mb,
       "apnWlanRxOctetsAtMCS0": apnWlanRxOctetsAtMCS0,
       "apnWlanRxOctetsAtMCS1": apnWlanRxOctetsAtMCS1,
       "apnWlanRxOctetsAtMCS2": apnWlanRxOctetsAtMCS2,
       "apnWlanRxOctetsAtMCS3": apnWlanRxOctetsAtMCS3,
       "apnWlanRxOctetsAtMCS4": apnWlanRxOctetsAtMCS4,
       "apnWlanRxOctetsAtMCS5": apnWlanRxOctetsAtMCS5,
       "apnWlanRxOctetsAtMCS6": apnWlanRxOctetsAtMCS6,
       "apnWlanRxOctetsAtMCS7": apnWlanRxOctetsAtMCS7,
       "apnWlanRxOctetsAtMCS8": apnWlanRxOctetsAtMCS8,
       "apnWlanRxOctetsAtMCS9": apnWlanRxOctetsAtMCS9,
       "apnWlanRxOctetsAtMCS10": apnWlanRxOctetsAtMCS10,
       "apnWlanRxOctetsAtMCS11": apnWlanRxOctetsAtMCS11,
       "apnWlanRxOctetsAtMCS12": apnWlanRxOctetsAtMCS12,
       "apnWlanRxOctetsAtMCS13": apnWlanRxOctetsAtMCS13,
       "apnWlanRxOctetsAtMCS14": apnWlanRxOctetsAtMCS14,
       "apnWlanRxOctetsAtMCS15": apnWlanRxOctetsAtMCS15,
       "apnWlanTxOctetsTable": apnWlanTxOctetsTable,
       "apnWlanTxOctetsEntry": apnWlanTxOctetsEntry,
       "apnWlanTxOctetsAt1Mb": apnWlanTxOctetsAt1Mb,
       "apnWlanTxOctetsAt2Mb": apnWlanTxOctetsAt2Mb,
       "apnWlanTxOctetsAt5pt5Mb": apnWlanTxOctetsAt5pt5Mb,
       "apnWlanTxOctetsAt6Mb": apnWlanTxOctetsAt6Mb,
       "apnWlanTxOctetsAt9Mb": apnWlanTxOctetsAt9Mb,
       "apnWlanTxOctetsAt11Mb": apnWlanTxOctetsAt11Mb,
       "apnWlanTxOctetsAt12Mb": apnWlanTxOctetsAt12Mb,
       "apnWlanTxOctetsAt18Mb": apnWlanTxOctetsAt18Mb,
       "apnWlanTxOctetsAt24Mb": apnWlanTxOctetsAt24Mb,
       "apnWlanTxOctetsAt36Mb": apnWlanTxOctetsAt36Mb,
       "apnWlanTxOctetsAt48Mb": apnWlanTxOctetsAt48Mb,
       "apnWlanTxOctetsAt54Mb": apnWlanTxOctetsAt54Mb,
       "apnWlanTxOctetsAtMCS0": apnWlanTxOctetsAtMCS0,
       "apnWlanTxOctetsAtMCS1": apnWlanTxOctetsAtMCS1,
       "apnWlanTxOctetsAtMCS2": apnWlanTxOctetsAtMCS2,
       "apnWlanTxOctetsAtMCS3": apnWlanTxOctetsAtMCS3,
       "apnWlanTxOctetsAtMCS4": apnWlanTxOctetsAtMCS4,
       "apnWlanTxOctetsAtMCS5": apnWlanTxOctetsAtMCS5,
       "apnWlanTxOctetsAtMCS6": apnWlanTxOctetsAtMCS6,
       "apnWlanTxOctetsAtMCS7": apnWlanTxOctetsAtMCS7,
       "apnWlanTxOctetsAtMCS8": apnWlanTxOctetsAtMCS8,
       "apnWlanTxOctetsAtMCS9": apnWlanTxOctetsAtMCS9,
       "apnWlanTxOctetsAtMCS10": apnWlanTxOctetsAtMCS10,
       "apnWlanTxOctetsAtMCS11": apnWlanTxOctetsAtMCS11,
       "apnWlanTxOctetsAtMCS12": apnWlanTxOctetsAtMCS12,
       "apnWlanTxOctetsAtMCS13": apnWlanTxOctetsAtMCS13,
       "apnWlanTxOctetsAtMCS14": apnWlanTxOctetsAtMCS14,
       "apnWlanTxOctetsAtMCS15": apnWlanTxOctetsAtMCS15,
       "apDiagStats": apDiagStats,
       "apDiagCpuStats": apDiagCpuStats,
       "apDiagCpuLoad1Min": apDiagCpuLoad1Min,
       "apDiagCpuLoad5Min": apDiagCpuLoad5Min,
       "apDiagCpuLoad15Min": apDiagCpuLoad15Min,
       "apDiagRamStats": apDiagRamStats,
       "apDiagRamTotal": apDiagRamTotal,
       "apDiagRamUsed": apDiagRamUsed,
       "apDiagRamPercentageUsed": apDiagRamPercentageUsed,
       "apLanStats": apLanStats,
       "apLanInfoTable": apLanInfoTable,
       "apLanInfoEntry": apLanInfoEntry,
       "apLanInfoIndex": apLanInfoIndex,
       "apLanInfoEnabled": apLanInfoEnabled,
       "apLanInfoIpAddress": apLanInfoIpAddress,
       "apLanInfoNetworkMask": apLanInfoNetworkMask,
       "apLanInfoEthernetAddress": apLanInfoEthernetAddress,
       "apLanInfoSpeed": apLanInfoSpeed,
       "apLanInfoDuplexMode": apLanInfoDuplexMode,
       "apLanRxPktsTable": apLanRxPktsTable,
       "apLanRxPktsEntry": apLanRxPktsEntry,
       "apLanRxPkts": apLanRxPkts,
       "apLanRxBytes": apLanRxBytes,
       "apLanRxErrors": apLanRxErrors,
       "apLanRxDropped": apLanRxDropped,
       "apLanRxFrameErrors": apLanRxFrameErrors,
       "apLanTxPktsTable": apLanTxPktsTable,
       "apLanTxPktsEntry": apLanTxPktsEntry,
       "apLanTxPkts": apLanTxPkts,
       "apLanTxBytes": apLanTxBytes,
       "apLanTxErrors": apLanTxErrors,
       "apLanTxDropped": apLanTxDropped,
       "apLanTxFrameErrors": apLanTxFrameErrors,
       "apMgmtAccess": apMgmtAccess,
       "apMgmtAccessToAllow": apMgmtAccessToAllow,
       "apTrustedHost": apTrustedHost,
       "apTrustedHostEnable": apTrustedHostEnable,
       "apTrustedHostRangeTable": apTrustedHostRangeTable,
       "apTrustedHostRangeEntry": apTrustedHostRangeEntry,
       "apTrustedHostRangeIndex": apTrustedHostRangeIndex,
       "apTrustedHostRangeLowerIp": apTrustedHostRangeLowerIp,
       "apTrustedHostRangeUpperIp": apTrustedHostRangeUpperIp,
       "apRouter": apRouter,
       "apRouterDefaultGatewayInterface": apRouterDefaultGatewayInterface,
       "apManualTime": apManualTime,
       "apManualCurrSystemDateTime": apManualCurrSystemDateTime,
       "apManualTimeZoneSetting": apManualTimeZoneSetting,
       "apManualTimeZoneTable": apManualTimeZoneTable,
       "apManualTimeZoneEntry": apManualTimeZoneEntry,
       "apManualTimeZoneIndex": apManualTimeZoneIndex,
       "apManualTimeZoneName": apManualTimeZoneName,
       "apManualExpectedTimeZone": apManualExpectedTimeZone,
       "apManualTimeZoneSet": apManualTimeZoneSet,
       "apManualDateTimeSetting": apManualDateTimeSetting,
       "apManualExpectedYear": apManualExpectedYear,
       "apManualExpectedMonth": apManualExpectedMonth,
       "apManualExpectedDay": apManualExpectedDay,
       "apManualExpectedHour": apManualExpectedHour,
       "apManualExpectedMinutes": apManualExpectedMinutes,
       "apManualExpectedSeconds": apManualExpectedSeconds,
       "apManualDateTimeSet": apManualDateTimeSet,
       "apAdmin": apAdmin,
       "apLoginMessage": apLoginMessage,
       "apLoginMessageMode": apLoginMessageMode,
       "apLoginMessageText": apLoginMessageText,
       "apRadiusServer": apRadiusServer,
       "apRadiusUsers": apRadiusUsers,
       "apRadiusUsersGroupTable": apRadiusUsersGroupTable,
       "apRadiusUsersGroupEntry": apRadiusUsersGroupEntry,
       "apRadiusUsersGroup": apRadiusUsersGroup,
       "apRadiusUsersGroupRowStatus": apRadiusUsersGroupRowStatus,
       "apRadiusUsersGroupId": apRadiusUsersGroupId,
       "apRadiusAccess": apRadiusAccess,
       "apRadiusAccessTable": apRadiusAccessTable,
       "apRadiusAccessEntry": apRadiusAccessEntry,
       "apRadiusAccessWlanPtrs": apRadiusAccessWlanPtrs,
       "apRadiusAccessTimeRule": apRadiusAccessTimeRule,
       "apWips": apWips,
       "apWipsPrimaryServerAddr": apWipsPrimaryServerAddr,
       "apWipsSecondaryServerAddr": apWipsSecondaryServerAddr,
       "apPower": apPower,
       "apPowerMode": apPowerMode,
       "apPowerDefRadio": apPowerDefRadio,
       "apPowerStatus": apPowerStatus,
       "apGroups": apGroups,
       "apGroupsV1dot0": apGroupsV1dot0,
       "dot1xGroup": dot1xGroup,
       "apRfGroup": apRfGroup,
       "apSwitchGroup": apSwitchGroup,
       "apTrapCtrlGroup": apTrapCtrlGroup,
       "apRapGroup": apRapGroup,
       "apLoadCfgGroup": apLoadCfgGroup,
       "apStatsGroup": apStatsGroup,
       "apNotificationsGroup": apNotificationsGroup,
       "apGroupsV1dot1": apGroupsV1dot1,
       "apGroupV1dot1variables": apGroupV1dot1variables,
       "apGroupV1dot1obsoleted": apGroupV1dot1obsoleted,
       "apGroupV1dot1deprecated": apGroupV1dot1deprecated,
       "apGroupV1dot1notifications": apGroupV1dot1notifications,
       "apGroupsV2dot2": apGroupsV2dot2,
       "apGroupV2dot2variables": apGroupV2dot2variables}
)
