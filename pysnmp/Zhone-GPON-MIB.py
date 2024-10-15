# SNMP MIB module (Zhone-GPON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Zhone-GPON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:23:13 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(apsMIB,
 efmCuMIB,
 efmOamMIB,
 pktcIetfSigMib,
 sechtor100,
 sechtor300,
 sipCommonMIB,
 sipTC,
 sipUAMIB,
 zhoneApon,
 zhoneAtm,
 zhoneBonding,
 zhoneBridge,
 zhoneCard,
 zhoneCes,
 zhoneClass5,
 zhoneConsole,
 zhoneDrafts,
 zhoneDs3Ext,
 zhoneDsl,
 zhoneDsx,
 zhoneEnet,
 zhoneGenWtn,
 zhoneGpon,
 zhoneGroups,
 zhoneIma,
 zhoneInterfaceGroup,
 zhoneInterfaceTranslation,
 zhoneIp,
 zhoneIsdn,
 zhoneLineTypes,
 zhoneMalc,
 zhoneMasterAgent,
 zhoneModules,
 zhoneOcx,
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
 zhoneSs7,
 zhoneSubscriber,
 zhoneSystem,
 zhoneTrapModules,
 zhoneVdsl,
 zhoneVideo,
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
    "efmCuMIB",
    "efmOamMIB",
    "pktcIetfSigMib",
    "sechtor100",
    "sechtor300",
    "sipCommonMIB",
    "sipTC",
    "sipUAMIB",
    "zhoneApon",
    "zhoneAtm",
    "zhoneBonding",
    "zhoneBridge",
    "zhoneCard",
    "zhoneCes",
    "zhoneClass5",
    "zhoneConsole",
    "zhoneDrafts",
    "zhoneDs3Ext",
    "zhoneDsl",
    "zhoneDsx",
    "zhoneEnet",
    "zhoneGenWtn",
    "zhoneGpon",
    "zhoneGroups",
    "zhoneIma",
    "zhoneInterfaceGroup",
    "zhoneInterfaceTranslation",
    "zhoneIp",
    "zhoneIsdn",
    "zhoneLineTypes",
    "zhoneMalc",
    "zhoneMasterAgent",
    "zhoneModules",
    "zhoneOcx",
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
    "zhoneSs7",
    "zhoneSubscriber",
    "zhoneSystem",
    "zhoneTrapModules",
    "zhoneVdsl",
    "zhoneVideo",
    "zhoneVoice",
    "zhoneVoiceStats",
    "zhoneVoip",
    "zhoneWtn",
    "zhoneZAP",
    "zhoneZedge",
    "zhoneZmsProduct",
    "zhoneZplex")

(ZhoneAdminString,
 ZhoneEnabledFlag,
 ZhoneRowStatus) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminString",
    "ZhoneEnabledFlag",
    "ZhoneRowStatus")


# MODULE-IDENTITY

zhoneGponOltMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 111)
)
zhoneGponOltMIB.setRevisions(
        ("2014-10-29 02:19",
         "2014-10-17 01:53",
         "2014-06-11 17:38",
         "2014-05-27 10:37",
         "2014-01-22 16:52",
         "2013-12-19 14:08",
         "2013-12-12 15:25",
         "2013-10-02 15:45",
         "2013-06-10 12:25",
         "2013-05-16 14:25",
         "2013-05-08 16:01",
         "2013-05-01 14:25",
         "2012-12-05 11:54",
         "2012-10-19 14:24",
         "2012-10-09 09:16",
         "2012-08-23 14:53",
         "2011-11-10 18:14",
         "2011-10-17 19:43",
         "2011-06-14 15:04",
         "2011-06-02 19:02",
         "2011-04-08 09:50",
         "2011-03-14 12:00",
         "2011-03-01 10:49",
         "2011-02-08 17:08",
         "2011-01-24 16:56",
         "2011-01-17 11:36",
         "2010-11-04 10:36",
         "2010-10-28 14:49",
         "2010-10-19 14:40",
         "2010-09-08 10:18",
         "2010-09-01 16:25",
         "2010-09-01 12:10",
         "2010-08-13 15:29",
         "2010-08-10 16:35",
         "2010-07-27 08:08",
         "2010-07-19 14:23",
         "2010-06-11 14:21",
         "2010-06-01 18:02",
         "2010-05-13 09:02",
         "2010-05-12 09:00",
         "2010-04-13 11:19",
         "2010-04-05 11:37",
         "2010-03-31 07:52",
         "2010-03-16 11:33",
         "2010-01-13 13:01",
         "2009-12-16 07:32",
         "2009-11-14 09:54",
         "2009-11-13 09:13",
         "2009-10-09 11:31",
         "2009-09-24 13:04",
         "2009-09-18 18:40",
         "2009-09-16 07:19",
         "2009-09-15 11:00",
         "2009-09-14 06:38",
         "2009-08-28 14:45",
         "2009-08-19 12:24",
         "2009-07-31 06:32",
         "2009-07-16 10:02",
         "2009-07-07 11:12",
         "2009-06-16 08:36",
         "2009-06-11 15:49",
         "2009-05-22 15:53",
         "2009-05-18 15:08",
         "2009-02-18 11:38",
         "2009-01-15 07:04",
         "2009-01-06 11:33",
         "2008-12-10 09:42",
         "2008-11-11 14:07",
         "2008-10-09 17:08",
         "2008-09-22 07:55",
         "2008-08-12 07:39",
         "2008-06-25 14:49",
         "2008-06-12 17:37",
         "2008-05-23 15:39",
         "2007-08-22 17:34",
         "2007-03-19 17:35",
         "2007-03-01 19:27",
         "2006-10-27 16:06")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OnuUpgradeState(Integer32, TextualConvention):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 6),
          ("complete", 4),
          ("downloaded", 8),
          ("downloading", 3),
          ("error", 5),
          ("fileError", 7),
          ("noUpgrade", 2),
          ("none", 0),
          ("queued", 1))
    )



class GponCacRc(Integer32, TextualConvention):
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
        *(("badParms", 3),
          ("cfgLookup", 4),
          ("dbaStatusChg", 12),
          ("genError", 5),
          ("maxBw", 9),
          ("maxCbrBw", 10),
          ("maxOltAllocIds", 7),
          ("maxOltDbaAllocIds", 8),
          ("maxOnuGemPorts", 6),
          ("noReq", 2),
          ("ok", 1),
          ("testCreateAlreadyExistsIfIndex", 15),
          ("testCreateAlreadyExistsSSPS", 16),
          ("testCreateCannotAddToSecondary", 20),
          ("testCreateCannotFindPrimary", 19),
          ("testCreateInvalidParms", 13),
          ("testCreateMissingParms", 14),
          ("testCreateOnuDoesNotExist", 17),
          ("testCreateOnuNotRegistered", 18),
          ("trafficClassChg", 11))
    )



# MIB Managed Objects in the order of their OIDs

_ZhoneGponObjectID_ObjectIdentity = ObjectIdentity
zhoneGponObjectID = _ZhoneGponObjectID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1)
)
_ZhoneGponOltConfigTable_Object = MibTable
zhoneGponOltConfigTable = _ZhoneGponOltConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1)
)
if mibBuilder.loadTexts:
    zhoneGponOltConfigTable.setStatus("current")
_ZhoneGponOltConfigEntry_Object = MibTableRow
zhoneGponOltConfigEntry = _ZhoneGponOltConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1)
)
zhoneGponOltConfigEntry.setIndexNames(
    (0, "Zhone-GPON-MIB", "zhoneGponOltIfIndex"),
)
if mibBuilder.loadTexts:
    zhoneGponOltConfigEntry.setStatus("current")
_ZhoneGponOltIfIndex_Type = InterfaceIndex
_ZhoneGponOltIfIndex_Object = MibTableColumn
zhoneGponOltIfIndex = _ZhoneGponOltIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 1),
    _ZhoneGponOltIfIndex_Type()
)
zhoneGponOltIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneGponOltIfIndex.setStatus("current")


class _ZhoneGponOltConfigMaxRtPropagationDelay_Type(Integer32):
    """Custom type zhoneGponOltConfigMaxRtPropagationDelay based on Integer32"""
    defaultValue = 200


_ZhoneGponOltConfigMaxRtPropagationDelay_Object = MibTableColumn
zhoneGponOltConfigMaxRtPropagationDelay = _ZhoneGponOltConfigMaxRtPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 2),
    _ZhoneGponOltConfigMaxRtPropagationDelay_Type()
)
zhoneGponOltConfigMaxRtPropagationDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigMaxRtPropagationDelay.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltConfigMaxRtPropagationDelay.setUnits("usec")


class _ZhoneGponOltConfigMaxOnuResponseTime_Type(Integer32):
    """Custom type zhoneGponOltConfigMaxOnuResponseTime based on Integer32"""
    defaultValue = 50


_ZhoneGponOltConfigMaxOnuResponseTime_Object = MibTableColumn
zhoneGponOltConfigMaxOnuResponseTime = _ZhoneGponOltConfigMaxOnuResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 3),
    _ZhoneGponOltConfigMaxOnuResponseTime_Type()
)
zhoneGponOltConfigMaxOnuResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigMaxOnuResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltConfigMaxOnuResponseTime.setUnits("usec")


class _ZhoneGponOltConfigPreassignedEqD_Type(Integer32):
    """Custom type zhoneGponOltConfigPreassignedEqD based on Integer32"""
    defaultValue = 0


_ZhoneGponOltConfigPreassignedEqD_Object = MibTableColumn
zhoneGponOltConfigPreassignedEqD = _ZhoneGponOltConfigPreassignedEqD_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 4),
    _ZhoneGponOltConfigPreassignedEqD_Type()
)
zhoneGponOltConfigPreassignedEqD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigPreassignedEqD.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltConfigPreassignedEqD.setUnits("usec")


class _ZhoneGponOltConfigLosAlpha_Type(Integer32):
    """Custom type zhoneGponOltConfigLosAlpha based on Integer32"""
    defaultValue = 4


_ZhoneGponOltConfigLosAlpha_Object = MibTableColumn
zhoneGponOltConfigLosAlpha = _ZhoneGponOltConfigLosAlpha_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 5),
    _ZhoneGponOltConfigLosAlpha_Type()
)
zhoneGponOltConfigLosAlpha.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigLosAlpha.setStatus("current")


class _ZhoneGponOltConfigLofAlpha_Type(Integer32):
    """Custom type zhoneGponOltConfigLofAlpha based on Integer32"""
    defaultValue = 4


_ZhoneGponOltConfigLofAlpha_Object = MibTableColumn
zhoneGponOltConfigLofAlpha = _ZhoneGponOltConfigLofAlpha_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 6),
    _ZhoneGponOltConfigLofAlpha_Type()
)
zhoneGponOltConfigLofAlpha.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigLofAlpha.setStatus("current")


class _ZhoneGponOltConfigLoamAlpha_Type(Integer32):
    """Custom type zhoneGponOltConfigLoamAlpha based on Integer32"""
    defaultValue = 3


_ZhoneGponOltConfigLoamAlpha_Object = MibTableColumn
zhoneGponOltConfigLoamAlpha = _ZhoneGponOltConfigLoamAlpha_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 7),
    _ZhoneGponOltConfigLoamAlpha_Type()
)
zhoneGponOltConfigLoamAlpha.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigLoamAlpha.setStatus("current")


class _ZhoneGponOltConfigScrambler_Type(ZhoneEnabledFlag):
    """Custom type zhoneGponOltConfigScrambler based on ZhoneEnabledFlag"""


_ZhoneGponOltConfigScrambler_Object = MibTableColumn
zhoneGponOltConfigScrambler = _ZhoneGponOltConfigScrambler_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 8),
    _ZhoneGponOltConfigScrambler_Type()
)
zhoneGponOltConfigScrambler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigScrambler.setStatus("current")


class _ZhoneGponOltConfigFecMode_Type(ZhoneEnabledFlag):
    """Custom type zhoneGponOltConfigFecMode based on ZhoneEnabledFlag"""


_ZhoneGponOltConfigFecMode_Object = MibTableColumn
zhoneGponOltConfigFecMode = _ZhoneGponOltConfigFecMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 9),
    _ZhoneGponOltConfigFecMode_Type()
)
zhoneGponOltConfigFecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigFecMode.setStatus("current")


class _ZhoneGponOltConfigAutoLearn_Type(ZhoneEnabledFlag):
    """Custom type zhoneGponOltConfigAutoLearn based on ZhoneEnabledFlag"""


_ZhoneGponOltConfigAutoLearn_Object = MibTableColumn
zhoneGponOltConfigAutoLearn = _ZhoneGponOltConfigAutoLearn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 10),
    _ZhoneGponOltConfigAutoLearn_Type()
)
zhoneGponOltConfigAutoLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigAutoLearn.setStatus("current")


class _ZhoneGponOltConfigPowerLevel_Type(Unsigned32):
    """Custom type zhoneGponOltConfigPowerLevel based on Unsigned32"""
    defaultValue = 0


_ZhoneGponOltConfigPowerLevel_Object = MibTableColumn
zhoneGponOltConfigPowerLevel = _ZhoneGponOltConfigPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 11),
    _ZhoneGponOltConfigPowerLevel_Type()
)
zhoneGponOltConfigPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltConfigPowerLevel.setUnits("db")


class _ZhoneGponOltConfigGuardBitCount_Type(Integer32):
    """Custom type zhoneGponOltConfigGuardBitCount based on Integer32"""
    defaultValue = 32


_ZhoneGponOltConfigGuardBitCount_Object = MibTableColumn
zhoneGponOltConfigGuardBitCount = _ZhoneGponOltConfigGuardBitCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 12),
    _ZhoneGponOltConfigGuardBitCount_Type()
)
zhoneGponOltConfigGuardBitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigGuardBitCount.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltConfigGuardBitCount.setUnits("bits")


class _ZhoneGponOltConfigDbaMode_Type(Integer32):
    """Custom type zhoneGponOltConfigDbaMode based on Integer32"""
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
        *(("piggyback", 2),
          ("predictive", 1),
          ("wholeReport", 3))
    )


_ZhoneGponOltConfigDbaMode_Type.__name__ = "Integer32"
_ZhoneGponOltConfigDbaMode_Object = MibTableColumn
zhoneGponOltConfigDbaMode = _ZhoneGponOltConfigDbaMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 13),
    _ZhoneGponOltConfigDbaMode_Type()
)
zhoneGponOltConfigDbaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigDbaMode.setStatus("current")


class _ZhoneGponOltConfigGemBlockSize_Type(Integer32):
    """Custom type zhoneGponOltConfigGemBlockSize based on Integer32"""
    defaultValue = 16


_ZhoneGponOltConfigGemBlockSize_Object = MibTableColumn
zhoneGponOltConfigGemBlockSize = _ZhoneGponOltConfigGemBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 14),
    _ZhoneGponOltConfigGemBlockSize_Type()
)
zhoneGponOltConfigGemBlockSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigGemBlockSize.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltConfigGemBlockSize.setUnits("bytes")


class _ZhoneGponOltConfigUsBerInterval_Type(Integer32):
    """Custom type zhoneGponOltConfigUsBerInterval based on Integer32"""
    defaultValue = 5000


_ZhoneGponOltConfigUsBerInterval_Object = MibTableColumn
zhoneGponOltConfigUsBerInterval = _ZhoneGponOltConfigUsBerInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 15),
    _ZhoneGponOltConfigUsBerInterval_Type()
)
zhoneGponOltConfigUsBerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigUsBerInterval.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltConfigUsBerInterval.setUnits("msec")


class _ZhoneGponOltConfigDsBerInterval_Type(Integer32):
    """Custom type zhoneGponOltConfigDsBerInterval based on Integer32"""
    defaultValue = 5000


_ZhoneGponOltConfigDsBerInterval_Object = MibTableColumn
zhoneGponOltConfigDsBerInterval = _ZhoneGponOltConfigDsBerInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 16),
    _ZhoneGponOltConfigDsBerInterval_Type()
)
zhoneGponOltConfigDsBerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigDsBerInterval.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltConfigDsBerInterval.setUnits("msec")


class _ZhoneGponOltConfigBerSfThreshold_Type(Integer32):
    """Custom type zhoneGponOltConfigBerSfThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 8),
    )


_ZhoneGponOltConfigBerSfThreshold_Type.__name__ = "Integer32"
_ZhoneGponOltConfigBerSfThreshold_Object = MibTableColumn
zhoneGponOltConfigBerSfThreshold = _ZhoneGponOltConfigBerSfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 17),
    _ZhoneGponOltConfigBerSfThreshold_Type()
)
zhoneGponOltConfigBerSfThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigBerSfThreshold.setStatus("current")


class _ZhoneGponOltConfigBerSdThreshold_Type(Integer32):
    """Custom type zhoneGponOltConfigBerSdThreshold based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 9),
    )


_ZhoneGponOltConfigBerSdThreshold_Type.__name__ = "Integer32"
_ZhoneGponOltConfigBerSdThreshold_Object = MibTableColumn
zhoneGponOltConfigBerSdThreshold = _ZhoneGponOltConfigBerSdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 18),
    _ZhoneGponOltConfigBerSdThreshold_Type()
)
zhoneGponOltConfigBerSdThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigBerSdThreshold.setStatus("current")


class _ZhoneGponOltConfigFecRequest_Type(ZhoneEnabledFlag):
    """Custom type zhoneGponOltConfigFecRequest based on ZhoneEnabledFlag"""


_ZhoneGponOltConfigFecRequest_Object = MibTableColumn
zhoneGponOltConfigFecRequest = _ZhoneGponOltConfigFecRequest_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 19),
    _ZhoneGponOltConfigFecRequest_Type()
)
zhoneGponOltConfigFecRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigFecRequest.setStatus("current")


class _ZhoneGponOltConfigKeyExchange_Type(ZhoneEnabledFlag):
    """Custom type zhoneGponOltConfigKeyExchange based on ZhoneEnabledFlag"""


_ZhoneGponOltConfigKeyExchange_Object = MibTableColumn
zhoneGponOltConfigKeyExchange = _ZhoneGponOltConfigKeyExchange_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 20),
    _ZhoneGponOltConfigKeyExchange_Type()
)
zhoneGponOltConfigKeyExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigKeyExchange.setStatus("current")


class _ZhoneGponOltConfigMinRtPropagationDelay_Type(Integer32):
    """Custom type zhoneGponOltConfigMinRtPropagationDelay based on Integer32"""
    defaultValue = 0


_ZhoneGponOltConfigMinRtPropagationDelay_Object = MibTableColumn
zhoneGponOltConfigMinRtPropagationDelay = _ZhoneGponOltConfigMinRtPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 21),
    _ZhoneGponOltConfigMinRtPropagationDelay_Type()
)
zhoneGponOltConfigMinRtPropagationDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigMinRtPropagationDelay.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltConfigMinRtPropagationDelay.setUnits("usec")


class _ZhoneGponOltConfigMinOnuResponseTime_Type(Integer32):
    """Custom type zhoneGponOltConfigMinOnuResponseTime based on Integer32"""
    defaultValue = 10


_ZhoneGponOltConfigMinOnuResponseTime_Object = MibTableColumn
zhoneGponOltConfigMinOnuResponseTime = _ZhoneGponOltConfigMinOnuResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 22),
    _ZhoneGponOltConfigMinOnuResponseTime_Type()
)
zhoneGponOltConfigMinOnuResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigMinOnuResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltConfigMinOnuResponseTime.setUnits("usec")


class _ZhoneGponOltConfigEqDMeasureCycles_Type(Integer32):
    """Custom type zhoneGponOltConfigEqDMeasureCycles based on Integer32"""
    defaultValue = 5


_ZhoneGponOltConfigEqDMeasureCycles_Object = MibTableColumn
zhoneGponOltConfigEqDMeasureCycles = _ZhoneGponOltConfigEqDMeasureCycles_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 23),
    _ZhoneGponOltConfigEqDMeasureCycles_Type()
)
zhoneGponOltConfigEqDMeasureCycles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigEqDMeasureCycles.setStatus("current")


class _ZhoneGponOltConfigDriftControlInterval_Type(Integer32):
    """Custom type zhoneGponOltConfigDriftControlInterval based on Integer32"""
    defaultValue = 1000


_ZhoneGponOltConfigDriftControlInterval_Object = MibTableColumn
zhoneGponOltConfigDriftControlInterval = _ZhoneGponOltConfigDriftControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 24),
    _ZhoneGponOltConfigDriftControlInterval_Type()
)
zhoneGponOltConfigDriftControlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigDriftControlInterval.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltConfigDriftControlInterval.setUnits("msec")


class _ZhoneGponOltConfigDriftControlLimit_Type(Integer32):
    """Custom type zhoneGponOltConfigDriftControlLimit based on Integer32"""
    defaultValue = 3


_ZhoneGponOltConfigDriftControlLimit_Object = MibTableColumn
zhoneGponOltConfigDriftControlLimit = _ZhoneGponOltConfigDriftControlLimit_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 25),
    _ZhoneGponOltConfigDriftControlLimit_Type()
)
zhoneGponOltConfigDriftControlLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigDriftControlLimit.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltConfigDriftControlLimit.setUnits("bits")


class _ZhoneGponOltConfigAllocCycleLength_Type(Integer32):
    """Custom type zhoneGponOltConfigAllocCycleLength based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ZhoneGponOltConfigAllocCycleLength_Type.__name__ = "Integer32"
_ZhoneGponOltConfigAllocCycleLength_Object = MibTableColumn
zhoneGponOltConfigAllocCycleLength = _ZhoneGponOltConfigAllocCycleLength_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 26),
    _ZhoneGponOltConfigAllocCycleLength_Type()
)
zhoneGponOltConfigAllocCycleLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigAllocCycleLength.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltConfigAllocCycleLength.setUnits("msec")


class _ZhoneGponOltConfigMinUsAlloc_Type(Integer32):
    """Custom type zhoneGponOltConfigMinUsAlloc based on Integer32"""
    defaultValue = 16


_ZhoneGponOltConfigMinUsAlloc_Object = MibTableColumn
zhoneGponOltConfigMinUsAlloc = _ZhoneGponOltConfigMinUsAlloc_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 27),
    _ZhoneGponOltConfigMinUsAlloc_Type()
)
zhoneGponOltConfigMinUsAlloc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigMinUsAlloc.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltConfigMinUsAlloc.setUnits("bytes")


class _ZhoneGponOltConfigAckTimeout_Type(Integer32):
    """Custom type zhoneGponOltConfigAckTimeout based on Integer32"""
    defaultValue = 2000


_ZhoneGponOltConfigAckTimeout_Object = MibTableColumn
zhoneGponOltConfigAckTimeout = _ZhoneGponOltConfigAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 28),
    _ZhoneGponOltConfigAckTimeout_Type()
)
zhoneGponOltConfigAckTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigAckTimeout.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltConfigAckTimeout.setUnits("msec")


class _ZhoneGponOltConfigPlsMaxAllocSize_Type(Integer32):
    """Custom type zhoneGponOltConfigPlsMaxAllocSize based on Integer32"""
    defaultValue = 120


_ZhoneGponOltConfigPlsMaxAllocSize_Object = MibTableColumn
zhoneGponOltConfigPlsMaxAllocSize = _ZhoneGponOltConfigPlsMaxAllocSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 29),
    _ZhoneGponOltConfigPlsMaxAllocSize_Type()
)
zhoneGponOltConfigPlsMaxAllocSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigPlsMaxAllocSize.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltConfigPlsMaxAllocSize.setUnits("bytes")


class _ZhoneGponOltConfigDbaCycle_Type(Unsigned32):
    """Custom type zhoneGponOltConfigDbaCycle based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_ZhoneGponOltConfigDbaCycle_Type.__name__ = "Unsigned32"
_ZhoneGponOltConfigDbaCycle_Object = MibTableColumn
zhoneGponOltConfigDbaCycle = _ZhoneGponOltConfigDbaCycle_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 30),
    _ZhoneGponOltConfigDbaCycle_Type()
)
zhoneGponOltConfigDbaCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigDbaCycle.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltConfigDbaCycle.setUnits("msec")


class _ZhoneGponOltConfigSrDbaReportingBlockSize_Type(Unsigned32):
    """Custom type zhoneGponOltConfigSrDbaReportingBlockSize based on Unsigned32"""
    defaultValue = 48


_ZhoneGponOltConfigSrDbaReportingBlockSize_Object = MibTableColumn
zhoneGponOltConfigSrDbaReportingBlockSize = _ZhoneGponOltConfigSrDbaReportingBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 31),
    _ZhoneGponOltConfigSrDbaReportingBlockSize_Type()
)
zhoneGponOltConfigSrDbaReportingBlockSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigSrDbaReportingBlockSize.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltConfigSrDbaReportingBlockSize.setUnits("bytes")


class _ZhoneGponOltConfigProtectionSwitchoverTimer_Type(Unsigned32):
    """Custom type zhoneGponOltConfigProtectionSwitchoverTimer based on Unsigned32"""
    defaultValue = 500


_ZhoneGponOltConfigProtectionSwitchoverTimer_Object = MibTableColumn
zhoneGponOltConfigProtectionSwitchoverTimer = _ZhoneGponOltConfigProtectionSwitchoverTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 32),
    _ZhoneGponOltConfigProtectionSwitchoverTimer_Type()
)
zhoneGponOltConfigProtectionSwitchoverTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigProtectionSwitchoverTimer.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltConfigProtectionSwitchoverTimer.setUnits("msec")


class _ZhoneGponOltConfigPreambleOverride_Type(ZhoneEnabledFlag):
    """Custom type zhoneGponOltConfigPreambleOverride based on ZhoneEnabledFlag"""


_ZhoneGponOltConfigPreambleOverride_Object = MibTableColumn
zhoneGponOltConfigPreambleOverride = _ZhoneGponOltConfigPreambleOverride_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 33),
    _ZhoneGponOltConfigPreambleOverride_Type()
)
zhoneGponOltConfigPreambleOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigPreambleOverride.setStatus("current")


class _ZhoneGponOltConfigPreambleType0_Type(OctetString):
    """Custom type zhoneGponOltConfigPreambleType0 based on OctetString"""
    defaultValue = OctetString("0x00")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ZhoneGponOltConfigPreambleType0_Type.__name__ = "OctetString"
_ZhoneGponOltConfigPreambleType0_Object = MibTableColumn
zhoneGponOltConfigPreambleType0 = _ZhoneGponOltConfigPreambleType0_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 34),
    _ZhoneGponOltConfigPreambleType0_Type()
)
zhoneGponOltConfigPreambleType0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigPreambleType0.setStatus("current")


class _ZhoneGponOltConfigPreambleType1_Type(OctetString):
    """Custom type zhoneGponOltConfigPreambleType1 based on OctetString"""
    defaultValue = OctetString("0x00")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ZhoneGponOltConfigPreambleType1_Type.__name__ = "OctetString"
_ZhoneGponOltConfigPreambleType1_Object = MibTableColumn
zhoneGponOltConfigPreambleType1 = _ZhoneGponOltConfigPreambleType1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 35),
    _ZhoneGponOltConfigPreambleType1_Type()
)
zhoneGponOltConfigPreambleType1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigPreambleType1.setStatus("current")


class _ZhoneGponOltConfigPreambleType3PreRange_Type(OctetString):
    """Custom type zhoneGponOltConfigPreambleType3PreRange based on OctetString"""
    defaultValue = OctetString("0x0b")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ZhoneGponOltConfigPreambleType3PreRange_Type.__name__ = "OctetString"
_ZhoneGponOltConfigPreambleType3PreRange_Object = MibTableColumn
zhoneGponOltConfigPreambleType3PreRange = _ZhoneGponOltConfigPreambleType3PreRange_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 36),
    _ZhoneGponOltConfigPreambleType3PreRange_Type()
)
zhoneGponOltConfigPreambleType3PreRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigPreambleType3PreRange.setStatus("current")


class _ZhoneGponOltConfigPreambleType3PostRange_Type(OctetString):
    """Custom type zhoneGponOltConfigPreambleType3PostRange based on OctetString"""
    defaultValue = OctetString("0x08")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ZhoneGponOltConfigPreambleType3PostRange_Type.__name__ = "OctetString"
_ZhoneGponOltConfigPreambleType3PostRange_Object = MibTableColumn
zhoneGponOltConfigPreambleType3PostRange = _ZhoneGponOltConfigPreambleType3PostRange_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 37),
    _ZhoneGponOltConfigPreambleType3PostRange_Type()
)
zhoneGponOltConfigPreambleType3PostRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigPreambleType3PostRange.setStatus("current")


class _ZhoneGponOltConfigPreambleType3Pattern_Type(OctetString):
    """Custom type zhoneGponOltConfigPreambleType3Pattern based on OctetString"""
    defaultValue = OctetString("0xaa")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ZhoneGponOltConfigPreambleType3Pattern_Type.__name__ = "OctetString"
_ZhoneGponOltConfigPreambleType3Pattern_Object = MibTableColumn
zhoneGponOltConfigPreambleType3Pattern = _ZhoneGponOltConfigPreambleType3Pattern_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 38),
    _ZhoneGponOltConfigPreambleType3Pattern_Type()
)
zhoneGponOltConfigPreambleType3Pattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigPreambleType3Pattern.setStatus("current")


class _ZhoneGponOltConfigBipErrorMonitoring_Type(Integer32):
    """Custom type zhoneGponOltConfigBipErrorMonitoring based on Integer32"""
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
        *(("blockOnError", 3),
          ("disabled", 1),
          ("monitorOnly", 2))
    )


_ZhoneGponOltConfigBipErrorMonitoring_Type.__name__ = "Integer32"
_ZhoneGponOltConfigBipErrorMonitoring_Object = MibTableColumn
zhoneGponOltConfigBipErrorMonitoring = _ZhoneGponOltConfigBipErrorMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 39),
    _ZhoneGponOltConfigBipErrorMonitoring_Type()
)
zhoneGponOltConfigBipErrorMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigBipErrorMonitoring.setStatus("current")


class _ZhoneGponOltConfigBipErrorsPerSampleThreshold_Type(Integer32):
    """Custom type zhoneGponOltConfigBipErrorsPerSampleThreshold based on Integer32"""
    defaultValue = 100


_ZhoneGponOltConfigBipErrorsPerSampleThreshold_Object = MibTableColumn
zhoneGponOltConfigBipErrorsPerSampleThreshold = _ZhoneGponOltConfigBipErrorsPerSampleThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 40),
    _ZhoneGponOltConfigBipErrorsPerSampleThreshold_Type()
)
zhoneGponOltConfigBipErrorsPerSampleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigBipErrorsPerSampleThreshold.setStatus("current")


class _ZhoneGponOltConfigBipErroredSamplesThreshold_Type(Integer32):
    """Custom type zhoneGponOltConfigBipErroredSamplesThreshold based on Integer32"""
    defaultValue = 10


_ZhoneGponOltConfigBipErroredSamplesThreshold_Object = MibTableColumn
zhoneGponOltConfigBipErroredSamplesThreshold = _ZhoneGponOltConfigBipErroredSamplesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 41),
    _ZhoneGponOltConfigBipErroredSamplesThreshold_Type()
)
zhoneGponOltConfigBipErroredSamplesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigBipErroredSamplesThreshold.setStatus("current")


class _ZhoneGponOltConfigBipMaxSampleGap_Type(Integer32):
    """Custom type zhoneGponOltConfigBipMaxSampleGap based on Integer32"""
    defaultValue = 10


_ZhoneGponOltConfigBipMaxSampleGap_Object = MibTableColumn
zhoneGponOltConfigBipMaxSampleGap = _ZhoneGponOltConfigBipMaxSampleGap_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 42),
    _ZhoneGponOltConfigBipMaxSampleGap_Type()
)
zhoneGponOltConfigBipMaxSampleGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigBipMaxSampleGap.setStatus("current")


class _ZhoneGponOltConfigRogueOnuDetection_Type(Integer32):
    """Custom type zhoneGponOltConfigRogueOnuDetection based on Integer32"""
    defaultValue = 1

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
        *(("autoRssi", 4),
          ("backgroundProcess", 3),
          ("disabled", 1),
          ("rogueRssi", 2))
    )


_ZhoneGponOltConfigRogueOnuDetection_Type.__name__ = "Integer32"
_ZhoneGponOltConfigRogueOnuDetection_Object = MibTableColumn
zhoneGponOltConfigRogueOnuDetection = _ZhoneGponOltConfigRogueOnuDetection_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 43),
    _ZhoneGponOltConfigRogueOnuDetection_Type()
)
zhoneGponOltConfigRogueOnuDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigRogueOnuDetection.setStatus("current")


class _ZhoneGponOltConfigRogueOnuDetectFrequency_Type(Integer32):
    """Custom type zhoneGponOltConfigRogueOnuDetectFrequency based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ZhoneGponOltConfigRogueOnuDetectFrequency_Type.__name__ = "Integer32"
_ZhoneGponOltConfigRogueOnuDetectFrequency_Object = MibTableColumn
zhoneGponOltConfigRogueOnuDetectFrequency = _ZhoneGponOltConfigRogueOnuDetectFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 44),
    _ZhoneGponOltConfigRogueOnuDetectFrequency_Type()
)
zhoneGponOltConfigRogueOnuDetectFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigRogueOnuDetectFrequency.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltConfigRogueOnuDetectFrequency.setUnits("seconds")


class _ZhoneGponOltConfigRogueOnuRxPowerThreshold_Type(Integer32):
    """Custom type zhoneGponOltConfigRogueOnuRxPowerThreshold based on Integer32"""
    defaultValue = -30


_ZhoneGponOltConfigRogueOnuRxPowerThreshold_Object = MibTableColumn
zhoneGponOltConfigRogueOnuRxPowerThreshold = _ZhoneGponOltConfigRogueOnuRxPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 1, 1, 45),
    _ZhoneGponOltConfigRogueOnuRxPowerThreshold_Type()
)
zhoneGponOltConfigRogueOnuRxPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltConfigRogueOnuRxPowerThreshold.setStatus("current")
_ZhoneGponOltOnuConfigTable_Object = MibTable
zhoneGponOltOnuConfigTable = _ZhoneGponOltOnuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2)
)
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigTable.setStatus("current")
_ZhoneGponOltOnuConfigEntry_Object = MibTableRow
zhoneGponOltOnuConfigEntry = _ZhoneGponOltOnuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1)
)
zhoneGponOltOnuConfigEntry.setIndexNames(
    (0, "Zhone-GPON-MIB", "zhoneGponOltOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigEntry.setStatus("current")
_ZhoneGponOltOnuIfIndex_Type = InterfaceIndex
_ZhoneGponOltOnuIfIndex_Object = MibTableColumn
zhoneGponOltOnuIfIndex = _ZhoneGponOltOnuIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 1),
    _ZhoneGponOltOnuIfIndex_Type()
)
zhoneGponOltOnuIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneGponOltOnuIfIndex.setStatus("current")


class _ZhoneGponOltOnuConfigSerialNoVendorId_Type(ZhoneAdminString):
    """Custom type zhoneGponOltOnuConfigSerialNoVendorId based on ZhoneAdminString"""
    defaultValue = OctetString("ZNTS")

    subtypeSpec = ZhoneAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ZhoneGponOltOnuConfigSerialNoVendorId_Type.__name__ = "ZhoneAdminString"
_ZhoneGponOltOnuConfigSerialNoVendorId_Object = MibTableColumn
zhoneGponOltOnuConfigSerialNoVendorId = _ZhoneGponOltOnuConfigSerialNoVendorId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 2),
    _ZhoneGponOltOnuConfigSerialNoVendorId_Type()
)
zhoneGponOltOnuConfigSerialNoVendorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigSerialNoVendorId.setStatus("current")


class _ZhoneGponOltOnuConfigSerialNoVendorSpecific_Type(ZhoneAdminString):
    """Custom type zhoneGponOltOnuConfigSerialNoVendorSpecific based on ZhoneAdminString"""
    defaultValue = OctetString("0")

    subtypeSpec = ZhoneAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ZhoneGponOltOnuConfigSerialNoVendorSpecific_Type.__name__ = "ZhoneAdminString"
_ZhoneGponOltOnuConfigSerialNoVendorSpecific_Object = MibTableColumn
zhoneGponOltOnuConfigSerialNoVendorSpecific = _ZhoneGponOltOnuConfigSerialNoVendorSpecific_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 3),
    _ZhoneGponOltOnuConfigSerialNoVendorSpecific_Type()
)
zhoneGponOltOnuConfigSerialNoVendorSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigSerialNoVendorSpecific.setStatus("current")


class _ZhoneGponOltOnuConfigPassword_Type(ZhoneAdminString):
    """Custom type zhoneGponOltOnuConfigPassword based on ZhoneAdminString"""
    subtypeSpec = ZhoneAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ZhoneGponOltOnuConfigPassword_Type.__name__ = "ZhoneAdminString"
_ZhoneGponOltOnuConfigPassword_Object = MibTableColumn
zhoneGponOltOnuConfigPassword = _ZhoneGponOltOnuConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 4),
    _ZhoneGponOltOnuConfigPassword_Type()
)
zhoneGponOltOnuConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigPassword.setStatus("current")


class _ZhoneGponOltOnuConfigAutoLearn_Type(ZhoneEnabledFlag):
    """Custom type zhoneGponOltOnuConfigAutoLearn based on ZhoneEnabledFlag"""


_ZhoneGponOltOnuConfigAutoLearn_Object = MibTableColumn
zhoneGponOltOnuConfigAutoLearn = _ZhoneGponOltOnuConfigAutoLearn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 5),
    _ZhoneGponOltOnuConfigAutoLearn_Type()
)
zhoneGponOltOnuConfigAutoLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigAutoLearn.setStatus("current")


class _ZhoneGponOltOnuConfigPowerLevel_Type(Integer32):
    """Custom type zhoneGponOltOnuConfigPowerLevel based on Integer32"""
    defaultValue = 0


_ZhoneGponOltOnuConfigPowerLevel_Object = MibTableColumn
zhoneGponOltOnuConfigPowerLevel = _ZhoneGponOltOnuConfigPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 6),
    _ZhoneGponOltOnuConfigPowerLevel_Type()
)
zhoneGponOltOnuConfigPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigPowerLevel.setUnits("db")


class _ZhoneGponOltOnuConfigUsBerInterval_Type(Integer32):
    """Custom type zhoneGponOltOnuConfigUsBerInterval based on Integer32"""
    defaultValue = 5000


_ZhoneGponOltOnuConfigUsBerInterval_Object = MibTableColumn
zhoneGponOltOnuConfigUsBerInterval = _ZhoneGponOltOnuConfigUsBerInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 7),
    _ZhoneGponOltOnuConfigUsBerInterval_Type()
)
zhoneGponOltOnuConfigUsBerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigUsBerInterval.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigUsBerInterval.setUnits("msec")


class _ZhoneGponOltOnuConfigDsBerInterval_Type(Integer32):
    """Custom type zhoneGponOltOnuConfigDsBerInterval based on Integer32"""
    defaultValue = 5000


_ZhoneGponOltOnuConfigDsBerInterval_Object = MibTableColumn
zhoneGponOltOnuConfigDsBerInterval = _ZhoneGponOltOnuConfigDsBerInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 8),
    _ZhoneGponOltOnuConfigDsBerInterval_Type()
)
zhoneGponOltOnuConfigDsBerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigDsBerInterval.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigDsBerInterval.setUnits("msec")


class _ZhoneGponOltOnuConfigOnuAdded_Type(TruthValue):
    """Custom type zhoneGponOltOnuConfigOnuAdded based on TruthValue"""


_ZhoneGponOltOnuConfigOnuAdded_Object = MibTableColumn
zhoneGponOltOnuConfigOnuAdded = _ZhoneGponOltOnuConfigOnuAdded_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 9),
    _ZhoneGponOltOnuConfigOnuAdded_Type()
)
zhoneGponOltOnuConfigOnuAdded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigOnuAdded.setStatus("current")
_ZhoneGponOltOnuConfigOmciFileName_Type = ZhoneAdminString
_ZhoneGponOltOnuConfigOmciFileName_Object = MibTableColumn
zhoneGponOltOnuConfigOmciFileName = _ZhoneGponOltOnuConfigOmciFileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 10),
    _ZhoneGponOltOnuConfigOmciFileName_Type()
)
zhoneGponOltOnuConfigOmciFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigOmciFileName.setStatus("current")
_ZhoneGponOltOnuConfigMEProfileName_Type = ZhoneAdminString
_ZhoneGponOltOnuConfigMEProfileName_Object = MibTableColumn
zhoneGponOltOnuConfigMEProfileName = _ZhoneGponOltOnuConfigMEProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 11),
    _ZhoneGponOltOnuConfigMEProfileName_Type()
)
zhoneGponOltOnuConfigMEProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigMEProfileName.setStatus("current")
_ZhoneGponOltOnuConfigGenericProfileName_Type = ZhoneAdminString
_ZhoneGponOltOnuConfigGenericProfileName_Object = MibTableColumn
zhoneGponOltOnuConfigGenericProfileName = _ZhoneGponOltOnuConfigGenericProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 12),
    _ZhoneGponOltOnuConfigGenericProfileName_Type()
)
zhoneGponOltOnuConfigGenericProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigGenericProfileName.setStatus("current")


class _ZhoneGponOltOnuConfigPhysicalTraps_Type(ZhoneEnabledFlag):
    """Custom type zhoneGponOltOnuConfigPhysicalTraps based on ZhoneEnabledFlag"""


_ZhoneGponOltOnuConfigPhysicalTraps_Object = MibTableColumn
zhoneGponOltOnuConfigPhysicalTraps = _ZhoneGponOltOnuConfigPhysicalTraps_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 13),
    _ZhoneGponOltOnuConfigPhysicalTraps_Type()
)
zhoneGponOltOnuConfigPhysicalTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigPhysicalTraps.setStatus("current")


class _ZhoneGponOltOnuConfigOntTraps_Type(ZhoneEnabledFlag):
    """Custom type zhoneGponOltOnuConfigOntTraps based on ZhoneEnabledFlag"""


_ZhoneGponOltOnuConfigOntTraps_Object = MibTableColumn
zhoneGponOltOnuConfigOntTraps = _ZhoneGponOltOnuConfigOntTraps_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 14),
    _ZhoneGponOltOnuConfigOntTraps_Type()
)
zhoneGponOltOnuConfigOntTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigOntTraps.setStatus("current")


class _ZhoneGponOltOnuConfigLineStatusTraps_Type(Integer32):
    """Custom type zhoneGponOltOnuConfigLineStatusTraps based on Integer32"""
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
        *(("auto", 3),
          ("disabled", 2),
          ("enabled", 1),
          ("linkonly", 4))
    )


_ZhoneGponOltOnuConfigLineStatusTraps_Type.__name__ = "Integer32"
_ZhoneGponOltOnuConfigLineStatusTraps_Object = MibTableColumn
zhoneGponOltOnuConfigLineStatusTraps = _ZhoneGponOltOnuConfigLineStatusTraps_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 15),
    _ZhoneGponOltOnuConfigLineStatusTraps_Type()
)
zhoneGponOltOnuConfigLineStatusTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigLineStatusTraps.setStatus("current")


class _ZhoneGponOltOnuConfigAutoUpgrade_Type(ZhoneEnabledFlag):
    """Custom type zhoneGponOltOnuConfigAutoUpgrade based on ZhoneEnabledFlag"""


_ZhoneGponOltOnuConfigAutoUpgrade_Object = MibTableColumn
zhoneGponOltOnuConfigAutoUpgrade = _ZhoneGponOltOnuConfigAutoUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 16),
    _ZhoneGponOltOnuConfigAutoUpgrade_Type()
)
zhoneGponOltOnuConfigAutoUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigAutoUpgrade.setStatus("current")


class _ZhoneGponOltOnuConfigSerialNoVendorSpecificFsan_Type(OctetString):
    """Custom type zhoneGponOltOnuConfigSerialNoVendorSpecificFsan based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_ZhoneGponOltOnuConfigSerialNoVendorSpecificFsan_Type.__name__ = "OctetString"
_ZhoneGponOltOnuConfigSerialNoVendorSpecificFsan_Object = MibTableColumn
zhoneGponOltOnuConfigSerialNoVendorSpecificFsan = _ZhoneGponOltOnuConfigSerialNoVendorSpecificFsan_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 17),
    _ZhoneGponOltOnuConfigSerialNoVendorSpecificFsan_Type()
)
zhoneGponOltOnuConfigSerialNoVendorSpecificFsan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigSerialNoVendorSpecificFsan.setStatus("current")


class _ZhoneGponOltOnuConfigUseRegId_Type(ZhoneEnabledFlag):
    """Custom type zhoneGponOltOnuConfigUseRegId based on ZhoneEnabledFlag"""


_ZhoneGponOltOnuConfigUseRegId_Object = MibTableColumn
zhoneGponOltOnuConfigUseRegId = _ZhoneGponOltOnuConfigUseRegId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 18),
    _ZhoneGponOltOnuConfigUseRegId_Type()
)
zhoneGponOltOnuConfigUseRegId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigUseRegId.setStatus("current")


class _ZhoneGponOltOnuConfigModel_Type(OctetString):
    """Custom type zhoneGponOltOnuConfigModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ZhoneGponOltOnuConfigModel_Type.__name__ = "OctetString"
_ZhoneGponOltOnuConfigModel_Object = MibTableColumn
zhoneGponOltOnuConfigModel = _ZhoneGponOltOnuConfigModel_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 19),
    _ZhoneGponOltOnuConfigModel_Type()
)
zhoneGponOltOnuConfigModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigModel.setStatus("current")


class _ZhoneGponOltOnuConfigOntVersion_Type(OctetString):
    """Custom type zhoneGponOltOnuConfigOntVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ZhoneGponOltOnuConfigOntVersion_Type.__name__ = "OctetString"
_ZhoneGponOltOnuConfigOntVersion_Object = MibTableColumn
zhoneGponOltOnuConfigOntVersion = _ZhoneGponOltOnuConfigOntVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 20),
    _ZhoneGponOltOnuConfigOntVersion_Type()
)
zhoneGponOltOnuConfigOntVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigOntVersion.setStatus("current")


class _ZhoneGponOltOnuConfigImageVersionActive_Type(OctetString):
    """Custom type zhoneGponOltOnuConfigImageVersionActive based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZhoneGponOltOnuConfigImageVersionActive_Type.__name__ = "OctetString"
_ZhoneGponOltOnuConfigImageVersionActive_Object = MibTableColumn
zhoneGponOltOnuConfigImageVersionActive = _ZhoneGponOltOnuConfigImageVersionActive_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 21),
    _ZhoneGponOltOnuConfigImageVersionActive_Type()
)
zhoneGponOltOnuConfigImageVersionActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigImageVersionActive.setStatus("current")


class _ZhoneGponOltOnuConfigImageVersionStandby_Type(OctetString):
    """Custom type zhoneGponOltOnuConfigImageVersionStandby based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZhoneGponOltOnuConfigImageVersionStandby_Type.__name__ = "OctetString"
_ZhoneGponOltOnuConfigImageVersionStandby_Object = MibTableColumn
zhoneGponOltOnuConfigImageVersionStandby = _ZhoneGponOltOnuConfigImageVersionStandby_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 22),
    _ZhoneGponOltOnuConfigImageVersionStandby_Type()
)
zhoneGponOltOnuConfigImageVersionStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigImageVersionStandby.setStatus("current")


class _ZhoneGponOltOnuConfigUsRxPowerMonitoring_Type(Integer32):
    """Custom type zhoneGponOltOnuConfigUsRxPowerMonitoring based on Integer32"""
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
        *(("blockOnError", 3),
          ("disabled", 1),
          ("monitorOnly", 2))
    )


_ZhoneGponOltOnuConfigUsRxPowerMonitoring_Type.__name__ = "Integer32"
_ZhoneGponOltOnuConfigUsRxPowerMonitoring_Object = MibTableColumn
zhoneGponOltOnuConfigUsRxPowerMonitoring = _ZhoneGponOltOnuConfigUsRxPowerMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 23),
    _ZhoneGponOltOnuConfigUsRxPowerMonitoring_Type()
)
zhoneGponOltOnuConfigUsRxPowerMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigUsRxPowerMonitoring.setStatus("current")


class _ZhoneGponOltOnuConfigUsRxPowerHighThreshold_Type(Integer32):
    """Custom type zhoneGponOltOnuConfigUsRxPowerHighThreshold based on Integer32"""
    defaultValue = -10


_ZhoneGponOltOnuConfigUsRxPowerHighThreshold_Object = MibTableColumn
zhoneGponOltOnuConfigUsRxPowerHighThreshold = _ZhoneGponOltOnuConfigUsRxPowerHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 24),
    _ZhoneGponOltOnuConfigUsRxPowerHighThreshold_Type()
)
zhoneGponOltOnuConfigUsRxPowerHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigUsRxPowerHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigUsRxPowerHighThreshold.setUnits("dBm")


class _ZhoneGponOltOnuConfigUsRxPowerLowThreshold_Type(Integer32):
    """Custom type zhoneGponOltOnuConfigUsRxPowerLowThreshold based on Integer32"""
    defaultValue = -30


_ZhoneGponOltOnuConfigUsRxPowerLowThreshold_Object = MibTableColumn
zhoneGponOltOnuConfigUsRxPowerLowThreshold = _ZhoneGponOltOnuConfigUsRxPowerLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 25),
    _ZhoneGponOltOnuConfigUsRxPowerLowThreshold_Type()
)
zhoneGponOltOnuConfigUsRxPowerLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigUsRxPowerLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigUsRxPowerLowThreshold.setUnits("dBm")


class _ZhoneGponOltOnuConfigDbaStatusReporting_Type(ZhoneEnabledFlag):
    """Custom type zhoneGponOltOnuConfigDbaStatusReporting based on ZhoneEnabledFlag"""


_ZhoneGponOltOnuConfigDbaStatusReporting_Object = MibTableColumn
zhoneGponOltOnuConfigDbaStatusReporting = _ZhoneGponOltOnuConfigDbaStatusReporting_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 26),
    _ZhoneGponOltOnuConfigDbaStatusReporting_Type()
)
zhoneGponOltOnuConfigDbaStatusReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigDbaStatusReporting.setStatus("current")


class _ZhoneGponOltOnuConfigOmciDataSync_Type(Unsigned32):
    """Custom type zhoneGponOltOnuConfigOmciDataSync based on Unsigned32"""
    defaultValue = 0


_ZhoneGponOltOnuConfigOmciDataSync_Object = MibTableColumn
zhoneGponOltOnuConfigOmciDataSync = _ZhoneGponOltOnuConfigOmciDataSync_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 27),
    _ZhoneGponOltOnuConfigOmciDataSync_Type()
)
zhoneGponOltOnuConfigOmciDataSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigOmciDataSync.setStatus("current")


class _ZhoneGponOltOnuConfigSnmpDataSync_Type(Unsigned32):
    """Custom type zhoneGponOltOnuConfigSnmpDataSync based on Unsigned32"""
    defaultValue = 0


_ZhoneGponOltOnuConfigSnmpDataSync_Object = MibTableColumn
zhoneGponOltOnuConfigSnmpDataSync = _ZhoneGponOltOnuConfigSnmpDataSync_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 28),
    _ZhoneGponOltOnuConfigSnmpDataSync_Type()
)
zhoneGponOltOnuConfigSnmpDataSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigSnmpDataSync.setStatus("current")


class _ZhoneGponOltOnuConfigNextAvailableGemPort_Type(Integer32):
    """Custom type zhoneGponOltOnuConfigNextAvailableGemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(257, 3828),
    )


_ZhoneGponOltOnuConfigNextAvailableGemPort_Type.__name__ = "Integer32"
_ZhoneGponOltOnuConfigNextAvailableGemPort_Object = MibTableColumn
zhoneGponOltOnuConfigNextAvailableGemPort = _ZhoneGponOltOnuConfigNextAvailableGemPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 29),
    _ZhoneGponOltOnuConfigNextAvailableGemPort_Type()
)
zhoneGponOltOnuConfigNextAvailableGemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigNextAvailableGemPort.setStatus("current")


class _ZhoneGponOltOnuConfigAutoConfigState_Type(Integer32):
    """Custom type zhoneGponOltOnuConfigAutoConfigState based on Integer32"""
    defaultValue = 1

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
        *(("disabled", 3),
          ("done", 2),
          ("error", 4),
          ("init", 1))
    )


_ZhoneGponOltOnuConfigAutoConfigState_Type.__name__ = "Integer32"
_ZhoneGponOltOnuConfigAutoConfigState_Object = MibTableColumn
zhoneGponOltOnuConfigAutoConfigState = _ZhoneGponOltOnuConfigAutoConfigState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 30),
    _ZhoneGponOltOnuConfigAutoConfigState_Type()
)
zhoneGponOltOnuConfigAutoConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigAutoConfigState.setStatus("current")


class _ZhoneGponOltOnuConfigLinkStatusAlarmSeverity_Type(Integer32):
    """Custom type zhoneGponOltOnuConfigLinkStatusAlarmSeverity based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3))
    )


_ZhoneGponOltOnuConfigLinkStatusAlarmSeverity_Type.__name__ = "Integer32"
_ZhoneGponOltOnuConfigLinkStatusAlarmSeverity_Object = MibTableColumn
zhoneGponOltOnuConfigLinkStatusAlarmSeverity = _ZhoneGponOltOnuConfigLinkStatusAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 2, 1, 31),
    _ZhoneGponOltOnuConfigLinkStatusAlarmSeverity_Type()
)
zhoneGponOltOnuConfigLinkStatusAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltOnuConfigLinkStatusAlarmSeverity.setStatus("current")
_ZhoneGponPortConfigTable_Object = MibTable
zhoneGponPortConfigTable = _ZhoneGponPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 3)
)
if mibBuilder.loadTexts:
    zhoneGponPortConfigTable.setStatus("current")
_ZhoneGponPortConfigEntry_Object = MibTableRow
zhoneGponPortConfigEntry = _ZhoneGponPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 3, 1)
)
zhoneGponPortConfigEntry.setIndexNames(
    (0, "Zhone-GPON-MIB", "zhoneGponPortIfIndex"),
)
if mibBuilder.loadTexts:
    zhoneGponPortConfigEntry.setStatus("current")
_ZhoneGponPortIfIndex_Type = InterfaceIndex
_ZhoneGponPortIfIndex_Object = MibTableColumn
zhoneGponPortIfIndex = _ZhoneGponPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 3, 1, 1),
    _ZhoneGponPortIfIndex_Type()
)
zhoneGponPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneGponPortIfIndex.setStatus("current")
_ZhoneGponPortConfigRowStatus_Type = ZhoneRowStatus
_ZhoneGponPortConfigRowStatus_Object = MibTableColumn
zhoneGponPortConfigRowStatus = _ZhoneGponPortConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 3, 1, 2),
    _ZhoneGponPortConfigRowStatus_Type()
)
zhoneGponPortConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponPortConfigRowStatus.setStatus("current")


class _ZhoneGponPortConfigMulticast_Type(TruthValue):
    """Custom type zhoneGponPortConfigMulticast based on TruthValue"""


_ZhoneGponPortConfigMulticast_Object = MibTableColumn
zhoneGponPortConfigMulticast = _ZhoneGponPortConfigMulticast_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 3, 1, 3),
    _ZhoneGponPortConfigMulticast_Type()
)
zhoneGponPortConfigMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponPortConfigMulticast.setStatus("current")


class _ZhoneGponPortConfigEncrypted_Type(TruthValue):
    """Custom type zhoneGponPortConfigEncrypted based on TruthValue"""


_ZhoneGponPortConfigEncrypted_Object = MibTableColumn
zhoneGponPortConfigEncrypted = _ZhoneGponPortConfigEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 3, 1, 4),
    _ZhoneGponPortConfigEncrypted_Type()
)
zhoneGponPortConfigEncrypted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponPortConfigEncrypted.setStatus("current")


class _ZhoneGponPortConfigDirection_Type(Integer32):
    """Custom type zhoneGponPortConfigDirection based on Integer32"""
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
        *(("bidirectional", 3),
          ("down", 1),
          ("up", 2))
    )


_ZhoneGponPortConfigDirection_Type.__name__ = "Integer32"
_ZhoneGponPortConfigDirection_Object = MibTableColumn
zhoneGponPortConfigDirection = _ZhoneGponPortConfigDirection_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 3, 1, 5),
    _ZhoneGponPortConfigDirection_Type()
)
zhoneGponPortConfigDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponPortConfigDirection.setStatus("current")


class _ZhoneGponPortConfigTrafficProfile_Type(Unsigned32):
    """Custom type zhoneGponPortConfigTrafficProfile based on Unsigned32"""
    defaultValue = 0


_ZhoneGponPortConfigTrafficProfile_Object = MibTableColumn
zhoneGponPortConfigTrafficProfile = _ZhoneGponPortConfigTrafficProfile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 3, 1, 6),
    _ZhoneGponPortConfigTrafficProfile_Type()
)
zhoneGponPortConfigTrafficProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponPortConfigTrafficProfile.setStatus("current")


class _ZhoneGponPortConfigRowShelf_Type(Unsigned32):
    """Custom type zhoneGponPortConfigRowShelf based on Unsigned32"""
    defaultBinValue = 0


_ZhoneGponPortConfigRowShelf_Object = MibTableColumn
zhoneGponPortConfigRowShelf = _ZhoneGponPortConfigRowShelf_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 3, 1, 7),
    _ZhoneGponPortConfigRowShelf_Type()
)
zhoneGponPortConfigRowShelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponPortConfigRowShelf.setStatus("current")


class _ZhoneGponPortConfigRowSlot_Type(Unsigned32):
    """Custom type zhoneGponPortConfigRowSlot based on Unsigned32"""
    defaultBinValue = 0


_ZhoneGponPortConfigRowSlot_Object = MibTableColumn
zhoneGponPortConfigRowSlot = _ZhoneGponPortConfigRowSlot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 3, 1, 8),
    _ZhoneGponPortConfigRowSlot_Type()
)
zhoneGponPortConfigRowSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponPortConfigRowSlot.setStatus("current")


class _ZhoneGponPortConfigRowOlt_Type(Unsigned32):
    """Custom type zhoneGponPortConfigRowOlt based on Unsigned32"""
    defaultBinValue = 0


_ZhoneGponPortConfigRowOlt_Object = MibTableColumn
zhoneGponPortConfigRowOlt = _ZhoneGponPortConfigRowOlt_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 3, 1, 9),
    _ZhoneGponPortConfigRowOlt_Type()
)
zhoneGponPortConfigRowOlt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponPortConfigRowOlt.setStatus("current")


class _ZhoneGponPortConfigRowPort_Type(Unsigned32):
    """Custom type zhoneGponPortConfigRowPort based on Unsigned32"""
    defaultBinValue = 0


_ZhoneGponPortConfigRowPort_Object = MibTableColumn
zhoneGponPortConfigRowPort = _ZhoneGponPortConfigRowPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 3, 1, 10),
    _ZhoneGponPortConfigRowPort_Type()
)
zhoneGponPortConfigRowPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponPortConfigRowPort.setStatus("current")


class _ZhoneGponPortConfigRowTrafficProfile_Type(Unsigned32):
    """Custom type zhoneGponPortConfigRowTrafficProfile based on Unsigned32"""
    defaultBinValue = 0


_ZhoneGponPortConfigRowTrafficProfile_Object = MibTableColumn
zhoneGponPortConfigRowTrafficProfile = _ZhoneGponPortConfigRowTrafficProfile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 3, 1, 11),
    _ZhoneGponPortConfigRowTrafficProfile_Type()
)
zhoneGponPortConfigRowTrafficProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponPortConfigRowTrafficProfile.setStatus("current")
_ZhoneGponPortConfigRowOnuId_Type = Unsigned32
_ZhoneGponPortConfigRowOnuId_Object = MibTableColumn
zhoneGponPortConfigRowOnuId = _ZhoneGponPortConfigRowOnuId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 3, 1, 12),
    _ZhoneGponPortConfigRowOnuId_Type()
)
zhoneGponPortConfigRowOnuId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponPortConfigRowOnuId.setStatus("current")


class _ZhoneGponPortConfigTrafficManagementProfileIndex_Type(Unsigned32):
    """Custom type zhoneGponPortConfigTrafficManagementProfileIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneGponPortConfigTrafficManagementProfileIndex_Type.__name__ = "Unsigned32"
_ZhoneGponPortConfigTrafficManagementProfileIndex_Object = MibTableColumn
zhoneGponPortConfigTrafficManagementProfileIndex = _ZhoneGponPortConfigTrafficManagementProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 3, 1, 13),
    _ZhoneGponPortConfigTrafficManagementProfileIndex_Type()
)
zhoneGponPortConfigTrafficManagementProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponPortConfigTrafficManagementProfileIndex.setStatus("current")
_ZhoneGponAllocIdTable_Object = MibTable
zhoneGponAllocIdTable = _ZhoneGponAllocIdTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 4)
)
if mibBuilder.loadTexts:
    zhoneGponAllocIdTable.setStatus("current")
_ZhoneGponAllocIdEntry_Object = MibTableRow
zhoneGponAllocIdEntry = _ZhoneGponAllocIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 4, 1)
)
zhoneGponAllocIdEntry.setIndexNames(
    (0, "Zhone-GPON-MIB", "zhoneGponOltIfIndex"),
    (0, "Zhone-GPON-MIB", "zhoneGponAllocIdIndex"),
)
if mibBuilder.loadTexts:
    zhoneGponAllocIdEntry.setStatus("current")


class _ZhoneGponAllocIdIndex_Type(Integer32):
    """Custom type zhoneGponAllocIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneGponAllocIdIndex_Type.__name__ = "Integer32"
_ZhoneGponAllocIdIndex_Object = MibTableColumn
zhoneGponAllocIdIndex = _ZhoneGponAllocIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 4, 1, 1),
    _ZhoneGponAllocIdIndex_Type()
)
zhoneGponAllocIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneGponAllocIdIndex.setStatus("current")
_ZhoneGponAllocIdRowStatus_Type = ZhoneRowStatus
_ZhoneGponAllocIdRowStatus_Object = MibTableColumn
zhoneGponAllocIdRowStatus = _ZhoneGponAllocIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 4, 1, 2),
    _ZhoneGponAllocIdRowStatus_Type()
)
zhoneGponAllocIdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponAllocIdRowStatus.setStatus("current")
_ZhoneGponAllocIdOnuId_Type = Integer32
_ZhoneGponAllocIdOnuId_Object = MibTableColumn
zhoneGponAllocIdOnuId = _ZhoneGponAllocIdOnuId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 4, 1, 3),
    _ZhoneGponAllocIdOnuId_Type()
)
zhoneGponAllocIdOnuId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponAllocIdOnuId.setStatus("current")
_ZhoneGponAllocIdGuaranteedBw_Type = Integer32
_ZhoneGponAllocIdGuaranteedBw_Object = MibTableColumn
zhoneGponAllocIdGuaranteedBw = _ZhoneGponAllocIdGuaranteedBw_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 4, 1, 4),
    _ZhoneGponAllocIdGuaranteedBw_Type()
)
zhoneGponAllocIdGuaranteedBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponAllocIdGuaranteedBw.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponAllocIdGuaranteedBw.setUnits("kilobits")


class _ZhoneGponAllocIdTrafficClass_Type(Integer32):
    """Custom type zhoneGponAllocIdTrafficClass based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 1),
          ("ubr", 2))
    )


_ZhoneGponAllocIdTrafficClass_Type.__name__ = "Integer32"
_ZhoneGponAllocIdTrafficClass_Object = MibTableColumn
zhoneGponAllocIdTrafficClass = _ZhoneGponAllocIdTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 4, 1, 5),
    _ZhoneGponAllocIdTrafficClass_Type()
)
zhoneGponAllocIdTrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponAllocIdTrafficClass.setStatus("current")


class _ZhoneGponAllocIdCompensated_Type(TruthValue):
    """Custom type zhoneGponAllocIdCompensated based on TruthValue"""


_ZhoneGponAllocIdCompensated_Object = MibTableColumn
zhoneGponAllocIdCompensated = _ZhoneGponAllocIdCompensated_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 4, 1, 6),
    _ZhoneGponAllocIdCompensated_Type()
)
zhoneGponAllocIdCompensated.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponAllocIdCompensated.setStatus("current")
_ZhoneGponSerialNoTable_Object = MibTable
zhoneGponSerialNoTable = _ZhoneGponSerialNoTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 5)
)
if mibBuilder.loadTexts:
    zhoneGponSerialNoTable.setStatus("current")
_ZhoneGponSerialNoEntry_Object = MibTableRow
zhoneGponSerialNoEntry = _ZhoneGponSerialNoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 5, 1)
)
zhoneGponSerialNoEntry.setIndexNames(
    (0, "Zhone-GPON-MIB", "zhoneGponSerialNoOltLgIfIndex"),
    (0, "Zhone-GPON-MIB", "zhoneGponSerialNoIndexId"),
)
if mibBuilder.loadTexts:
    zhoneGponSerialNoEntry.setStatus("current")
_ZhoneGponSerialNoOltLgIfIndex_Type = InterfaceIndex
_ZhoneGponSerialNoOltLgIfIndex_Object = MibTableColumn
zhoneGponSerialNoOltLgIfIndex = _ZhoneGponSerialNoOltLgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 5, 1, 1),
    _ZhoneGponSerialNoOltLgIfIndex_Type()
)
zhoneGponSerialNoOltLgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneGponSerialNoOltLgIfIndex.setStatus("current")
_ZhoneGponSerialNoIndexId_Type = Unsigned32
_ZhoneGponSerialNoIndexId_Object = MibTableColumn
zhoneGponSerialNoIndexId = _ZhoneGponSerialNoIndexId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 5, 1, 2),
    _ZhoneGponSerialNoIndexId_Type()
)
zhoneGponSerialNoIndexId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneGponSerialNoIndexId.setStatus("current")


class _ZhoneGponSerialNoVendorId_Type(ZhoneAdminString):
    """Custom type zhoneGponSerialNoVendorId based on ZhoneAdminString"""
    subtypeSpec = ZhoneAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ZhoneGponSerialNoVendorId_Type.__name__ = "ZhoneAdminString"
_ZhoneGponSerialNoVendorId_Object = MibTableColumn
zhoneGponSerialNoVendorId = _ZhoneGponSerialNoVendorId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 5, 1, 3),
    _ZhoneGponSerialNoVendorId_Type()
)
zhoneGponSerialNoVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponSerialNoVendorId.setStatus("current")


class _ZhoneGponSerialNoVendorSpecific_Type(ZhoneAdminString):
    """Custom type zhoneGponSerialNoVendorSpecific based on ZhoneAdminString"""
    subtypeSpec = ZhoneAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ZhoneGponSerialNoVendorSpecific_Type.__name__ = "ZhoneAdminString"
_ZhoneGponSerialNoVendorSpecific_Object = MibTableColumn
zhoneGponSerialNoVendorSpecific = _ZhoneGponSerialNoVendorSpecific_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 5, 1, 4),
    _ZhoneGponSerialNoVendorSpecific_Type()
)
zhoneGponSerialNoVendorSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponSerialNoVendorSpecific.setStatus("current")


class _ZhoneGponSerialNoTimeStamp_Type(OctetString):
    """Custom type zhoneGponSerialNoTimeStamp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZhoneGponSerialNoTimeStamp_Type.__name__ = "OctetString"
_ZhoneGponSerialNoTimeStamp_Object = MibTableColumn
zhoneGponSerialNoTimeStamp = _ZhoneGponSerialNoTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 5, 1, 5),
    _ZhoneGponSerialNoTimeStamp_Type()
)
zhoneGponSerialNoTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponSerialNoTimeStamp.setStatus("current")
_ZhoneGponTrapPrefix_ObjectIdentity = ObjectIdentity
zhoneGponTrapPrefix = _ZhoneGponTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 6)
)
if mibBuilder.loadTexts:
    zhoneGponTrapPrefix.setStatus("current")
_ZhoneGponTraps_ObjectIdentity = ObjectIdentity
zhoneGponTraps = _ZhoneGponTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 6, 0)
)
if mibBuilder.loadTexts:
    zhoneGponTraps.setStatus("current")
_ZhoneGponOnuStatusTable_Object = MibTable
zhoneGponOnuStatusTable = _ZhoneGponOnuStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 7)
)
if mibBuilder.loadTexts:
    zhoneGponOnuStatusTable.setStatus("current")
_ZhoneGponOnuStatusEntry_Object = MibTableRow
zhoneGponOnuStatusEntry = _ZhoneGponOnuStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 7, 1)
)
zhoneGponOnuStatusEntry.setIndexNames(
    (0, "Zhone-GPON-MIB", "zhoneGponOltOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zhoneGponOnuStatusEntry.setStatus("current")


class _ZhoneGponOnuStatusWord_Type(Bits):
    """Custom type zhoneGponOnuStatusWord based on Bits"""
    namedValues = NamedValues(
        *(("bit16notUsed", 16),
          ("bit17notUsed", 17),
          ("driftOfWindow", 4),
          ("dyingGasp", 12),
          ("excessiveBipErrorsOnuDisabled", 18),
          ("excessiveBipErrorsOnuNotDisabled", 19),
          ("inactive", 1),
          ("lossOfAck", 11),
          ("lossOfFrame", 3),
          ("lossOfGemChanDelin", 7),
          ("lossOfPloamSync", 13),
          ("lossOfSignal", 2),
          ("manualOnuRebooted", 23),
          ("messageError", 14),
          ("noAlarm", 0),
          ("physEquipError", 15),
          ("remoteDefect", 8),
          ("rogueOnu", 22),
          ("signalDegrade", 6),
          ("signalFail", 5),
          ("startUpFailure", 10),
          ("transmitterFailure", 9),
          ("usRxPowerErrorOnuDisabled", 20),
          ("usRxPowerErrorOnuNotDisabled", 21))
    )

_ZhoneGponOnuStatusWord_Type.__name__ = "Bits"
_ZhoneGponOnuStatusWord_Object = MibTableColumn
zhoneGponOnuStatusWord = _ZhoneGponOnuStatusWord_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 7, 1, 1),
    _ZhoneGponOnuStatusWord_Type()
)
zhoneGponOnuStatusWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOnuStatusWord.setStatus("current")


class _ZhoneGponOnuOmciState_Type(Integer32):
    """Custom type zhoneGponOnuOmciState based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 7),
          ("config", 3),
          ("done", 5),
          ("down", 9),
          ("download", 6),
          ("error", 4),
          ("noConfig", 10),
          ("omciErrAndPostCfgErr", 17),
          ("omciErrAndRgComErr", 14),
          ("omciErrAndRgServErr", 15),
          ("omciFailed", 13),
          ("pending", 2),
          ("postCfgError", 16),
          ("rgComError", 11),
          ("rgServiceSetupErr", 12),
          ("unknown", 8),
          ("waiting", 1))
    )


_ZhoneGponOnuOmciState_Type.__name__ = "Integer32"
_ZhoneGponOnuOmciState_Object = MibTableColumn
zhoneGponOnuOmciState = _ZhoneGponOnuOmciState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 7, 1, 2),
    _ZhoneGponOnuOmciState_Type()
)
zhoneGponOnuOmciState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOnuOmciState.setStatus("current")


class _ZhoneGponOnuOpticRssi_Type(Integer32):
    """Custom type zhoneGponOnuOpticRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 200),
    )


_ZhoneGponOnuOpticRssi_Type.__name__ = "Integer32"
_ZhoneGponOnuOpticRssi_Object = MibTableColumn
zhoneGponOnuOpticRssi = _ZhoneGponOnuOpticRssi_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 7, 1, 3),
    _ZhoneGponOnuOpticRssi_Type()
)
zhoneGponOnuOpticRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOnuOpticRssi.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOnuOpticRssi.setUnits("tenths of dB")


class _ZhoneGponOntRxPower_Type(Integer32):
    """Custom type zhoneGponOntRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 200),
    )


_ZhoneGponOntRxPower_Type.__name__ = "Integer32"
_ZhoneGponOntRxPower_Object = MibTableColumn
zhoneGponOntRxPower = _ZhoneGponOntRxPower_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 7, 1, 4),
    _ZhoneGponOntRxPower_Type()
)
zhoneGponOntRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOntRxPower.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOntRxPower.setUnits("tenths of dB")


class _ZhoneGponOntVersion_Type(OctetString):
    """Custom type zhoneGponOntVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ZhoneGponOntVersion_Type.__name__ = "OctetString"
_ZhoneGponOntVersion_Object = MibTableColumn
zhoneGponOntVersion = _ZhoneGponOntVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 7, 1, 5),
    _ZhoneGponOntVersion_Type()
)
zhoneGponOntVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOntVersion.setStatus("current")
_ZhoneGponOnuDistance_Type = Unsigned32
_ZhoneGponOnuDistance_Object = MibTableColumn
zhoneGponOnuDistance = _ZhoneGponOnuDistance_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 7, 1, 6),
    _ZhoneGponOnuDistance_Type()
)
zhoneGponOnuDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOnuDistance.setStatus("current")
_ZhoneOnuOmciMEProfileTable_Object = MibTable
zhoneOnuOmciMEProfileTable = _ZhoneOnuOmciMEProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 8)
)
if mibBuilder.loadTexts:
    zhoneOnuOmciMEProfileTable.setStatus("current")
_ZhoneOnuOmciMEProfileEntry_Object = MibTableRow
zhoneOnuOmciMEProfileEntry = _ZhoneOnuOmciMEProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 8, 1)
)
zhoneOnuOmciMEProfileEntry.setIndexNames(
    (0, "Zhone-GPON-MIB", "zhoneOnuOmciMEProfileIndex"),
)
if mibBuilder.loadTexts:
    zhoneOnuOmciMEProfileEntry.setStatus("current")
_ZhoneOnuOmciMEProfileIndex_Type = Unsigned32
_ZhoneOnuOmciMEProfileIndex_Object = MibTableColumn
zhoneOnuOmciMEProfileIndex = _ZhoneOnuOmciMEProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 8, 1, 1),
    _ZhoneOnuOmciMEProfileIndex_Type()
)
zhoneOnuOmciMEProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneOnuOmciMEProfileIndex.setStatus("current")


class _ZhoneOnuOmciMEProfileRowStatus_Type(Integer32):
    """Custom type zhoneOnuOmciMEProfileRowStatus based on Integer32"""
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
        *(("active", 1),
          ("append", 6),
          ("create", 2),
          ("destroy", 3),
          ("export", 4),
          ("import", 5),
          ("revert", 7))
    )


_ZhoneOnuOmciMEProfileRowStatus_Type.__name__ = "Integer32"
_ZhoneOnuOmciMEProfileRowStatus_Object = MibTableColumn
zhoneOnuOmciMEProfileRowStatus = _ZhoneOnuOmciMEProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 8, 1, 2),
    _ZhoneOnuOmciMEProfileRowStatus_Type()
)
zhoneOnuOmciMEProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneOnuOmciMEProfileRowStatus.setStatus("current")


class _ZhoneOnuOmciMEProfileName_Type(OctetString):
    """Custom type zhoneOnuOmciMEProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZhoneOnuOmciMEProfileName_Type.__name__ = "OctetString"
_ZhoneOnuOmciMEProfileName_Object = MibTableColumn
zhoneOnuOmciMEProfileName = _ZhoneOnuOmciMEProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 8, 1, 3),
    _ZhoneOnuOmciMEProfileName_Type()
)
zhoneOnuOmciMEProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneOnuOmciMEProfileName.setStatus("current")


class _ZhoneOnuOmciMEProfileOmciCommands_Type(OctetString):
    """Custom type zhoneOnuOmciMEProfileOmciCommands based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64000),
    )


_ZhoneOnuOmciMEProfileOmciCommands_Type.__name__ = "OctetString"
_ZhoneOnuOmciMEProfileOmciCommands_Object = MibTableColumn
zhoneOnuOmciMEProfileOmciCommands = _ZhoneOnuOmciMEProfileOmciCommands_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 8, 1, 4),
    _ZhoneOnuOmciMEProfileOmciCommands_Type()
)
zhoneOnuOmciMEProfileOmciCommands.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneOnuOmciMEProfileOmciCommands.setStatus("current")


class _ZhoneOnuOmciMEProfileFileName_Type(OctetString):
    """Custom type zhoneOnuOmciMEProfileFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZhoneOnuOmciMEProfileFileName_Type.__name__ = "OctetString"
_ZhoneOnuOmciMEProfileFileName_Object = MibTableColumn
zhoneOnuOmciMEProfileFileName = _ZhoneOnuOmciMEProfileFileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 8, 1, 5),
    _ZhoneOnuOmciMEProfileFileName_Type()
)
zhoneOnuOmciMEProfileFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneOnuOmciMEProfileFileName.setStatus("current")
_ZhoneOnuOmciGenericProfileTable_Object = MibTable
zhoneOnuOmciGenericProfileTable = _ZhoneOnuOmciGenericProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 9)
)
if mibBuilder.loadTexts:
    zhoneOnuOmciGenericProfileTable.setStatus("current")
_ZhoneOnuOmciGenericProfileEntry_Object = MibTableRow
zhoneOnuOmciGenericProfileEntry = _ZhoneOnuOmciGenericProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 9, 1)
)
zhoneOnuOmciGenericProfileEntry.setIndexNames(
    (0, "Zhone-GPON-MIB", "zhoneOnuOmciGenericProfileIndex"),
)
if mibBuilder.loadTexts:
    zhoneOnuOmciGenericProfileEntry.setStatus("current")
_ZhoneOnuOmciGenericProfileIndex_Type = Unsigned32
_ZhoneOnuOmciGenericProfileIndex_Object = MibTableColumn
zhoneOnuOmciGenericProfileIndex = _ZhoneOnuOmciGenericProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 9, 1, 1),
    _ZhoneOnuOmciGenericProfileIndex_Type()
)
zhoneOnuOmciGenericProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneOnuOmciGenericProfileIndex.setStatus("current")


class _ZhoneOnuOmciGenericProfileRowStatus_Type(Integer32):
    """Custom type zhoneOnuOmciGenericProfileRowStatus based on Integer32"""
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
        *(("active", 1),
          ("create", 2),
          ("destroy", 3),
          ("export", 4),
          ("import", 5))
    )


_ZhoneOnuOmciGenericProfileRowStatus_Type.__name__ = "Integer32"
_ZhoneOnuOmciGenericProfileRowStatus_Object = MibTableColumn
zhoneOnuOmciGenericProfileRowStatus = _ZhoneOnuOmciGenericProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 9, 1, 2),
    _ZhoneOnuOmciGenericProfileRowStatus_Type()
)
zhoneOnuOmciGenericProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneOnuOmciGenericProfileRowStatus.setStatus("current")


class _ZhoneOnuOmciGenericProfileName_Type(OctetString):
    """Custom type zhoneOnuOmciGenericProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZhoneOnuOmciGenericProfileName_Type.__name__ = "OctetString"
_ZhoneOnuOmciGenericProfileName_Object = MibTableColumn
zhoneOnuOmciGenericProfileName = _ZhoneOnuOmciGenericProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 9, 1, 3),
    _ZhoneOnuOmciGenericProfileName_Type()
)
zhoneOnuOmciGenericProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneOnuOmciGenericProfileName.setStatus("current")


class _ZhoneOnuOmciGenericProfileOmciCommands_Type(OctetString):
    """Custom type zhoneOnuOmciGenericProfileOmciCommands based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15000),
    )


_ZhoneOnuOmciGenericProfileOmciCommands_Type.__name__ = "OctetString"
_ZhoneOnuOmciGenericProfileOmciCommands_Object = MibTableColumn
zhoneOnuOmciGenericProfileOmciCommands = _ZhoneOnuOmciGenericProfileOmciCommands_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 9, 1, 4),
    _ZhoneOnuOmciGenericProfileOmciCommands_Type()
)
zhoneOnuOmciGenericProfileOmciCommands.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneOnuOmciGenericProfileOmciCommands.setStatus("current")


class _ZhoneOnuOmciGenericProfileMESrcProfileName_Type(OctetString):
    """Custom type zhoneOnuOmciGenericProfileMESrcProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZhoneOnuOmciGenericProfileMESrcProfileName_Type.__name__ = "OctetString"
_ZhoneOnuOmciGenericProfileMESrcProfileName_Object = MibTableColumn
zhoneOnuOmciGenericProfileMESrcProfileName = _ZhoneOnuOmciGenericProfileMESrcProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 9, 1, 5),
    _ZhoneOnuOmciGenericProfileMESrcProfileName_Type()
)
zhoneOnuOmciGenericProfileMESrcProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneOnuOmciGenericProfileMESrcProfileName.setStatus("current")


class _ZhoneOnuOmciGenericProfileFileName_Type(OctetString):
    """Custom type zhoneOnuOmciGenericProfileFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZhoneOnuOmciGenericProfileFileName_Type.__name__ = "OctetString"
_ZhoneOnuOmciGenericProfileFileName_Object = MibTableColumn
zhoneOnuOmciGenericProfileFileName = _ZhoneOnuOmciGenericProfileFileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 9, 1, 6),
    _ZhoneOnuOmciGenericProfileFileName_Type()
)
zhoneOnuOmciGenericProfileFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneOnuOmciGenericProfileFileName.setStatus("current")
_ZhoneOnuOmciSpecificProfileTable_Object = MibTable
zhoneOnuOmciSpecificProfileTable = _ZhoneOnuOmciSpecificProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 10)
)
if mibBuilder.loadTexts:
    zhoneOnuOmciSpecificProfileTable.setStatus("current")
_ZhoneOnuOmciSpecificProfileEntry_Object = MibTableRow
zhoneOnuOmciSpecificProfileEntry = _ZhoneOnuOmciSpecificProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 10, 1)
)
zhoneOnuOmciSpecificProfileEntry.setIndexNames(
    (0, "Zhone-GPON-MIB", "zhoneOnuOmciSpecificProfileIndex"),
)
if mibBuilder.loadTexts:
    zhoneOnuOmciSpecificProfileEntry.setStatus("current")
_ZhoneOnuOmciSpecificProfileIndex_Type = InterfaceIndex
_ZhoneOnuOmciSpecificProfileIndex_Object = MibTableColumn
zhoneOnuOmciSpecificProfileIndex = _ZhoneOnuOmciSpecificProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 10, 1, 1),
    _ZhoneOnuOmciSpecificProfileIndex_Type()
)
zhoneOnuOmciSpecificProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneOnuOmciSpecificProfileIndex.setStatus("current")


class _ZhoneOnuOmciSpecificProfileRowStatus_Type(Integer32):
    """Custom type zhoneOnuOmciSpecificProfileRowStatus based on Integer32"""
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
        *(("active", 1),
          ("create", 2),
          ("destroy", 3),
          ("export", 4),
          ("import", 5))
    )


_ZhoneOnuOmciSpecificProfileRowStatus_Type.__name__ = "Integer32"
_ZhoneOnuOmciSpecificProfileRowStatus_Object = MibTableColumn
zhoneOnuOmciSpecificProfileRowStatus = _ZhoneOnuOmciSpecificProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 10, 1, 2),
    _ZhoneOnuOmciSpecificProfileRowStatus_Type()
)
zhoneOnuOmciSpecificProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneOnuOmciSpecificProfileRowStatus.setStatus("current")


class _ZhoneOnuOmciSpecificProfileOmciCommands_Type(OctetString):
    """Custom type zhoneOnuOmciSpecificProfileOmciCommands based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8000),
    )


_ZhoneOnuOmciSpecificProfileOmciCommands_Type.__name__ = "OctetString"
_ZhoneOnuOmciSpecificProfileOmciCommands_Object = MibTableColumn
zhoneOnuOmciSpecificProfileOmciCommands = _ZhoneOnuOmciSpecificProfileOmciCommands_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 10, 1, 3),
    _ZhoneOnuOmciSpecificProfileOmciCommands_Type()
)
zhoneOnuOmciSpecificProfileOmciCommands.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneOnuOmciSpecificProfileOmciCommands.setStatus("current")


class _ZhoneOnuOmciSpecificProfileMESrcProfileName_Type(OctetString):
    """Custom type zhoneOnuOmciSpecificProfileMESrcProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZhoneOnuOmciSpecificProfileMESrcProfileName_Type.__name__ = "OctetString"
_ZhoneOnuOmciSpecificProfileMESrcProfileName_Object = MibTableColumn
zhoneOnuOmciSpecificProfileMESrcProfileName = _ZhoneOnuOmciSpecificProfileMESrcProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 10, 1, 4),
    _ZhoneOnuOmciSpecificProfileMESrcProfileName_Type()
)
zhoneOnuOmciSpecificProfileMESrcProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneOnuOmciSpecificProfileMESrcProfileName.setStatus("current")


class _ZhoneOnuOmciSpecificProfileFileName_Type(OctetString):
    """Custom type zhoneOnuOmciSpecificProfileFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZhoneOnuOmciSpecificProfileFileName_Type.__name__ = "OctetString"
_ZhoneOnuOmciSpecificProfileFileName_Object = MibTableColumn
zhoneOnuOmciSpecificProfileFileName = _ZhoneOnuOmciSpecificProfileFileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 10, 1, 5),
    _ZhoneOnuOmciSpecificProfileFileName_Type()
)
zhoneOnuOmciSpecificProfileFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneOnuOmciSpecificProfileFileName.setStatus("current")
_ZhoneGponOmciOnuAlarmsTable_Object = MibTable
zhoneGponOmciOnuAlarmsTable = _ZhoneGponOmciOnuAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 11)
)
if mibBuilder.loadTexts:
    zhoneGponOmciOnuAlarmsTable.setStatus("current")
_ZhoneGponOmciOnuAlarmsEntry_Object = MibTableRow
zhoneGponOmciOnuAlarmsEntry = _ZhoneGponOmciOnuAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 11, 1)
)
zhoneGponOmciOnuAlarmsEntry.setIndexNames(
    (0, "Zhone-GPON-MIB", "zhoneGponOltOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zhoneGponOmciOnuAlarmsEntry.setStatus("current")


class _ZhoneGponOmciOnuAlarmsText_Type(OctetString):
    """Custom type zhoneGponOmciOnuAlarmsText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16000),
    )


_ZhoneGponOmciOnuAlarmsText_Type.__name__ = "OctetString"
_ZhoneGponOmciOnuAlarmsText_Object = MibTableColumn
zhoneGponOmciOnuAlarmsText = _ZhoneGponOmciOnuAlarmsText_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 11, 1, 1),
    _ZhoneGponOmciOnuAlarmsText_Type()
)
zhoneGponOmciOnuAlarmsText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOmciOnuAlarmsText.setStatus("current")
_ZhoneGponTrafficProfileTable_Object = MibTable
zhoneGponTrafficProfileTable = _ZhoneGponTrafficProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 12)
)
if mibBuilder.loadTexts:
    zhoneGponTrafficProfileTable.setStatus("current")
_ZhoneGponTrafficProfileEntry_Object = MibTableRow
zhoneGponTrafficProfileEntry = _ZhoneGponTrafficProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 12, 1)
)
zhoneGponTrafficProfileEntry.setIndexNames(
    (0, "Zhone-GPON-MIB", "zhoneGponTrafficProfileIndex"),
)
if mibBuilder.loadTexts:
    zhoneGponTrafficProfileEntry.setStatus("current")
_ZhoneGponTrafficProfileIndex_Type = Unsigned32
_ZhoneGponTrafficProfileIndex_Object = MibTableColumn
zhoneGponTrafficProfileIndex = _ZhoneGponTrafficProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 12, 1, 1),
    _ZhoneGponTrafficProfileIndex_Type()
)
zhoneGponTrafficProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneGponTrafficProfileIndex.setStatus("current")
_ZhoneGponTrafficProfileRowStatus_Type = ZhoneRowStatus
_ZhoneGponTrafficProfileRowStatus_Object = MibTableColumn
zhoneGponTrafficProfileRowStatus = _ZhoneGponTrafficProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 12, 1, 2),
    _ZhoneGponTrafficProfileRowStatus_Type()
)
zhoneGponTrafficProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponTrafficProfileRowStatus.setStatus("current")


class _ZhoneGponTrafficProfileGuaranteedUpstreamBw_Type(Integer32):
    """Custom type zhoneGponTrafficProfileGuaranteedUpstreamBw based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048576),
    )


_ZhoneGponTrafficProfileGuaranteedUpstreamBw_Type.__name__ = "Integer32"
_ZhoneGponTrafficProfileGuaranteedUpstreamBw_Object = MibTableColumn
zhoneGponTrafficProfileGuaranteedUpstreamBw = _ZhoneGponTrafficProfileGuaranteedUpstreamBw_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 12, 1, 3),
    _ZhoneGponTrafficProfileGuaranteedUpstreamBw_Type()
)
zhoneGponTrafficProfileGuaranteedUpstreamBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponTrafficProfileGuaranteedUpstreamBw.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponTrafficProfileGuaranteedUpstreamBw.setUnits("kilobits")


class _ZhoneGponTrafficProfileClass_Type(Integer32):
    """Custom type zhoneGponTrafficProfileClass based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 1),
          ("ubr", 2))
    )


_ZhoneGponTrafficProfileClass_Type.__name__ = "Integer32"
_ZhoneGponTrafficProfileClass_Object = MibTableColumn
zhoneGponTrafficProfileClass = _ZhoneGponTrafficProfileClass_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 12, 1, 4),
    _ZhoneGponTrafficProfileClass_Type()
)
zhoneGponTrafficProfileClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponTrafficProfileClass.setStatus("current")


class _ZhoneGponTrafficProfileCompensated_Type(TruthValue):
    """Custom type zhoneGponTrafficProfileCompensated based on TruthValue"""


_ZhoneGponTrafficProfileCompensated_Object = MibTableColumn
zhoneGponTrafficProfileCompensated = _ZhoneGponTrafficProfileCompensated_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 12, 1, 5),
    _ZhoneGponTrafficProfileCompensated_Type()
)
zhoneGponTrafficProfileCompensated.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponTrafficProfileCompensated.setStatus("current")


class _ZhoneGponTrafficProfileShared_Type(TruthValue):
    """Custom type zhoneGponTrafficProfileShared based on TruthValue"""


_ZhoneGponTrafficProfileShared_Object = MibTableColumn
zhoneGponTrafficProfileShared = _ZhoneGponTrafficProfileShared_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 12, 1, 6),
    _ZhoneGponTrafficProfileShared_Type()
)
zhoneGponTrafficProfileShared.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponTrafficProfileShared.setStatus("current")


class _ZhoneGponTrafficProfileDbaEnabled_Type(TruthValue):
    """Custom type zhoneGponTrafficProfileDbaEnabled based on TruthValue"""


_ZhoneGponTrafficProfileDbaEnabled_Object = MibTableColumn
zhoneGponTrafficProfileDbaEnabled = _ZhoneGponTrafficProfileDbaEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 12, 1, 7),
    _ZhoneGponTrafficProfileDbaEnabled_Type()
)
zhoneGponTrafficProfileDbaEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponTrafficProfileDbaEnabled.setStatus("current")


class _ZhoneGponTrafficProfileDbaFixedUsUbrBw_Type(Unsigned32):
    """Custom type zhoneGponTrafficProfileDbaFixedUsUbrBw based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048576),
    )


_ZhoneGponTrafficProfileDbaFixedUsUbrBw_Type.__name__ = "Unsigned32"
_ZhoneGponTrafficProfileDbaFixedUsUbrBw_Object = MibTableColumn
zhoneGponTrafficProfileDbaFixedUsUbrBw = _ZhoneGponTrafficProfileDbaFixedUsUbrBw_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 12, 1, 8),
    _ZhoneGponTrafficProfileDbaFixedUsUbrBw_Type()
)
zhoneGponTrafficProfileDbaFixedUsUbrBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponTrafficProfileDbaFixedUsUbrBw.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponTrafficProfileDbaFixedUsUbrBw.setUnits("kilobits")


class _ZhoneGponTrafficProfileDbaFixedUsCbrBw_Type(Unsigned32):
    """Custom type zhoneGponTrafficProfileDbaFixedUsCbrBw based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 454208),
    )


_ZhoneGponTrafficProfileDbaFixedUsCbrBw_Type.__name__ = "Unsigned32"
_ZhoneGponTrafficProfileDbaFixedUsCbrBw_Object = MibTableColumn
zhoneGponTrafficProfileDbaFixedUsCbrBw = _ZhoneGponTrafficProfileDbaFixedUsCbrBw_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 12, 1, 9),
    _ZhoneGponTrafficProfileDbaFixedUsCbrBw_Type()
)
zhoneGponTrafficProfileDbaFixedUsCbrBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponTrafficProfileDbaFixedUsCbrBw.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponTrafficProfileDbaFixedUsCbrBw.setUnits("kilobits")


class _ZhoneGponTrafficProfileDbaAssuredUsBw_Type(Unsigned32):
    """Custom type zhoneGponTrafficProfileDbaAssuredUsBw based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048576),
    )


_ZhoneGponTrafficProfileDbaAssuredUsBw_Type.__name__ = "Unsigned32"
_ZhoneGponTrafficProfileDbaAssuredUsBw_Object = MibTableColumn
zhoneGponTrafficProfileDbaAssuredUsBw = _ZhoneGponTrafficProfileDbaAssuredUsBw_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 12, 1, 10),
    _ZhoneGponTrafficProfileDbaAssuredUsBw_Type()
)
zhoneGponTrafficProfileDbaAssuredUsBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponTrafficProfileDbaAssuredUsBw.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponTrafficProfileDbaAssuredUsBw.setUnits("kilobits")


class _ZhoneGponTrafficProfileMaxUsBw_Type(Unsigned32):
    """Custom type zhoneGponTrafficProfileMaxUsBw based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048576),
    )


_ZhoneGponTrafficProfileMaxUsBw_Type.__name__ = "Unsigned32"
_ZhoneGponTrafficProfileMaxUsBw_Object = MibTableColumn
zhoneGponTrafficProfileMaxUsBw = _ZhoneGponTrafficProfileMaxUsBw_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 12, 1, 11),
    _ZhoneGponTrafficProfileMaxUsBw_Type()
)
zhoneGponTrafficProfileMaxUsBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponTrafficProfileMaxUsBw.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponTrafficProfileMaxUsBw.setUnits("kilobits")


class _ZhoneGponTrafficProfileExtraUsBwType_Type(Integer32):
    """Custom type zhoneGponTrafficProfileExtraUsBwType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("besteffort", 2),
          ("nonassured", 1))
    )


_ZhoneGponTrafficProfileExtraUsBwType_Type.__name__ = "Integer32"
_ZhoneGponTrafficProfileExtraUsBwType_Object = MibTableColumn
zhoneGponTrafficProfileExtraUsBwType = _ZhoneGponTrafficProfileExtraUsBwType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 12, 1, 12),
    _ZhoneGponTrafficProfileExtraUsBwType_Type()
)
zhoneGponTrafficProfileExtraUsBwType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponTrafficProfileExtraUsBwType.setStatus("current")
_ZhoneGponPortStatusTable_Object = MibTable
zhoneGponPortStatusTable = _ZhoneGponPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 13)
)
if mibBuilder.loadTexts:
    zhoneGponPortStatusTable.setStatus("current")
_ZhoneGponPortStatusEntry_Object = MibTableRow
zhoneGponPortStatusEntry = _ZhoneGponPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 13, 1)
)
zhoneGponPortStatusEntry.setIndexNames(
    (0, "Zhone-GPON-MIB", "zhoneGponOltOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zhoneGponPortStatusEntry.setStatus("current")


class _ZhoneGponPortStatusAllocId_Type(Unsigned32):
    """Custom type zhoneGponPortStatusAllocId based on Unsigned32"""
    defaultValue = 0


_ZhoneGponPortStatusAllocId_Object = MibTableColumn
zhoneGponPortStatusAllocId = _ZhoneGponPortStatusAllocId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 13, 1, 1),
    _ZhoneGponPortStatusAllocId_Type()
)
zhoneGponPortStatusAllocId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponPortStatusAllocId.setStatus("current")


class _ZhoneGponPortStatusDbaStatus_Type(Integer32):
    """Custom type zhoneGponPortStatusDbaStatus based on Integer32"""
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
        *(("error", 7),
          ("notAdded", 6),
          ("notAvailable", 5),
          ("notEnabled", 4),
          ("nsr", 2),
          ("nsrError", 3),
          ("sr", 1))
    )


_ZhoneGponPortStatusDbaStatus_Type.__name__ = "Integer32"
_ZhoneGponPortStatusDbaStatus_Object = MibTableColumn
zhoneGponPortStatusDbaStatus = _ZhoneGponPortStatusDbaStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 13, 1, 2),
    _ZhoneGponPortStatusDbaStatus_Type()
)
zhoneGponPortStatusDbaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponPortStatusDbaStatus.setStatus("current")
_ZhoneGponOmciStatsCurrentTable_Object = MibTable
zhoneGponOmciStatsCurrentTable = _ZhoneGponOmciStatsCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 14)
)
if mibBuilder.loadTexts:
    zhoneGponOmciStatsCurrentTable.setStatus("current")
_ZhoneGponOmciStatsCurrentEntry_Object = MibTableRow
zhoneGponOmciStatsCurrentEntry = _ZhoneGponOmciStatsCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 14, 1)
)
zhoneGponOmciStatsCurrentEntry.setIndexNames(
    (0, "Zhone-GPON-MIB", "zhoneGponOltOnuIfIndex"),
    (0, "Zhone-GPON-MIB", "zhoneGponOmciStatsCurrentMEId"),
    (0, "Zhone-GPON-MIB", "zhoneGponOmciStatsCurrentLogicalPort"),
)
if mibBuilder.loadTexts:
    zhoneGponOmciStatsCurrentEntry.setStatus("current")
_ZhoneGponOmciStatsCurrentMEId_Type = Unsigned32
_ZhoneGponOmciStatsCurrentMEId_Object = MibTableColumn
zhoneGponOmciStatsCurrentMEId = _ZhoneGponOmciStatsCurrentMEId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 14, 1, 1),
    _ZhoneGponOmciStatsCurrentMEId_Type()
)
zhoneGponOmciStatsCurrentMEId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneGponOmciStatsCurrentMEId.setStatus("current")
_ZhoneGponOmciStatsCurrentLogicalPort_Type = Unsigned32
_ZhoneGponOmciStatsCurrentLogicalPort_Object = MibTableColumn
zhoneGponOmciStatsCurrentLogicalPort = _ZhoneGponOmciStatsCurrentLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 14, 1, 2),
    _ZhoneGponOmciStatsCurrentLogicalPort_Type()
)
zhoneGponOmciStatsCurrentLogicalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneGponOmciStatsCurrentLogicalPort.setStatus("current")


class _ZhoneGponOmciStatsCurrentText_Type(OctetString):
    """Custom type zhoneGponOmciStatsCurrentText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ZhoneGponOmciStatsCurrentText_Type.__name__ = "OctetString"
_ZhoneGponOmciStatsCurrentText_Object = MibTableColumn
zhoneGponOmciStatsCurrentText = _ZhoneGponOmciStatsCurrentText_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 14, 1, 3),
    _ZhoneGponOmciStatsCurrentText_Type()
)
zhoneGponOmciStatsCurrentText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOmciStatsCurrentText.setStatus("current")
_ZhoneGponOmciStatsPreviousTable_Object = MibTable
zhoneGponOmciStatsPreviousTable = _ZhoneGponOmciStatsPreviousTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 15)
)
if mibBuilder.loadTexts:
    zhoneGponOmciStatsPreviousTable.setStatus("current")
_ZhoneGponOmciStatsPreviousEntry_Object = MibTableRow
zhoneGponOmciStatsPreviousEntry = _ZhoneGponOmciStatsPreviousEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 15, 1)
)
zhoneGponOmciStatsPreviousEntry.setIndexNames(
    (0, "Zhone-GPON-MIB", "zhoneGponOltOnuIfIndex"),
    (0, "Zhone-GPON-MIB", "zhoneGponOmciStatsPreviousMEId"),
    (0, "Zhone-GPON-MIB", "zhoneGponOmciStatsPreviousLogicalPort"),
)
if mibBuilder.loadTexts:
    zhoneGponOmciStatsPreviousEntry.setStatus("current")
_ZhoneGponOmciStatsPreviousMEId_Type = Unsigned32
_ZhoneGponOmciStatsPreviousMEId_Object = MibTableColumn
zhoneGponOmciStatsPreviousMEId = _ZhoneGponOmciStatsPreviousMEId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 15, 1, 1),
    _ZhoneGponOmciStatsPreviousMEId_Type()
)
zhoneGponOmciStatsPreviousMEId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneGponOmciStatsPreviousMEId.setStatus("current")
_ZhoneGponOmciStatsPreviousLogicalPort_Type = Unsigned32
_ZhoneGponOmciStatsPreviousLogicalPort_Object = MibTableColumn
zhoneGponOmciStatsPreviousLogicalPort = _ZhoneGponOmciStatsPreviousLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 15, 1, 2),
    _ZhoneGponOmciStatsPreviousLogicalPort_Type()
)
zhoneGponOmciStatsPreviousLogicalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneGponOmciStatsPreviousLogicalPort.setStatus("current")


class _ZhoneGponOmciStatsPreviousText_Type(OctetString):
    """Custom type zhoneGponOmciStatsPreviousText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ZhoneGponOmciStatsPreviousText_Type.__name__ = "OctetString"
_ZhoneGponOmciStatsPreviousText_Object = MibTableColumn
zhoneGponOmciStatsPreviousText = _ZhoneGponOmciStatsPreviousText_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 15, 1, 3),
    _ZhoneGponOmciStatsPreviousText_Type()
)
zhoneGponOmciStatsPreviousText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOmciStatsPreviousText.setStatus("current")
_ZhoneGponOmciStatusTable_Object = MibTable
zhoneGponOmciStatusTable = _ZhoneGponOmciStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 16)
)
if mibBuilder.loadTexts:
    zhoneGponOmciStatusTable.setStatus("current")
_ZhoneGponOmciStatusEntry_Object = MibTableRow
zhoneGponOmciStatusEntry = _ZhoneGponOmciStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 16, 1)
)
zhoneGponOmciStatusEntry.setIndexNames(
    (0, "Zhone-GPON-MIB", "zhoneGponOltOnuIfIndex"),
    (0, "Zhone-GPON-MIB", "zhoneGponOmciStatusMEId"),
    (0, "Zhone-GPON-MIB", "zhoneGponOmciStatusLogicalPort"),
)
if mibBuilder.loadTexts:
    zhoneGponOmciStatusEntry.setStatus("current")
_ZhoneGponOmciStatusMEId_Type = Unsigned32
_ZhoneGponOmciStatusMEId_Object = MibTableColumn
zhoneGponOmciStatusMEId = _ZhoneGponOmciStatusMEId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 16, 1, 1),
    _ZhoneGponOmciStatusMEId_Type()
)
zhoneGponOmciStatusMEId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneGponOmciStatusMEId.setStatus("current")
_ZhoneGponOmciStatusLogicalPort_Type = Unsigned32
_ZhoneGponOmciStatusLogicalPort_Object = MibTableColumn
zhoneGponOmciStatusLogicalPort = _ZhoneGponOmciStatusLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 16, 1, 2),
    _ZhoneGponOmciStatusLogicalPort_Type()
)
zhoneGponOmciStatusLogicalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneGponOmciStatusLogicalPort.setStatus("current")


class _ZhoneGponOmciStatusText_Type(OctetString):
    """Custom type zhoneGponOmciStatusText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_ZhoneGponOmciStatusText_Type.__name__ = "OctetString"
_ZhoneGponOmciStatusText_Object = MibTableColumn
zhoneGponOmciStatusText = _ZhoneGponOmciStatusText_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 16, 1, 3),
    _ZhoneGponOmciStatusText_Type()
)
zhoneGponOmciStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOmciStatusText.setStatus("current")
_ZhoneGponOmciOnuRebootTable_Object = MibTable
zhoneGponOmciOnuRebootTable = _ZhoneGponOmciOnuRebootTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 17)
)
if mibBuilder.loadTexts:
    zhoneGponOmciOnuRebootTable.setStatus("current")
_ZhoneGponOmciOnuRebootEntry_Object = MibTableRow
zhoneGponOmciOnuRebootEntry = _ZhoneGponOmciOnuRebootEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 17, 1)
)
zhoneGponOmciOnuRebootEntry.setIndexNames(
    (0, "Zhone-GPON-MIB", "zhoneGponOltOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zhoneGponOmciOnuRebootEntry.setStatus("current")


class _ZhoneGponOmciOnuReboot_Type(Integer32):
    """Custom type zhoneGponOmciOnuReboot based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reboot", 1))
    )


_ZhoneGponOmciOnuReboot_Type.__name__ = "Integer32"
_ZhoneGponOmciOnuReboot_Object = MibTableColumn
zhoneGponOmciOnuReboot = _ZhoneGponOmciOnuReboot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 17, 1, 1),
    _ZhoneGponOmciOnuReboot_Type()
)
zhoneGponOmciOnuReboot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponOmciOnuReboot.setStatus("current")
_ZhoneGponOmciOnuPortAdminTable_Object = MibTable
zhoneGponOmciOnuPortAdminTable = _ZhoneGponOmciOnuPortAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 18)
)
if mibBuilder.loadTexts:
    zhoneGponOmciOnuPortAdminTable.setStatus("current")
_ZhoneGponOmciOnuPortAdminEntry_Object = MibTableRow
zhoneGponOmciOnuPortAdminEntry = _ZhoneGponOmciOnuPortAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 18, 1)
)
zhoneGponOmciOnuPortAdminEntry.setIndexNames(
    (0, "Zhone-GPON-MIB", "zhoneGponOltOnuIfIndex"),
    (0, "Zhone-GPON-MIB", "zhoneGponOmciOnuPortAdminMEId"),
    (0, "Zhone-GPON-MIB", "zhoneGponOmciOnuPortAdminLogicalPort"),
)
if mibBuilder.loadTexts:
    zhoneGponOmciOnuPortAdminEntry.setStatus("current")
_ZhoneGponOmciOnuPortAdminMEId_Type = Unsigned32
_ZhoneGponOmciOnuPortAdminMEId_Object = MibTableColumn
zhoneGponOmciOnuPortAdminMEId = _ZhoneGponOmciOnuPortAdminMEId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 18, 1, 1),
    _ZhoneGponOmciOnuPortAdminMEId_Type()
)
zhoneGponOmciOnuPortAdminMEId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneGponOmciOnuPortAdminMEId.setStatus("current")
_ZhoneGponOmciOnuPortAdminLogicalPort_Type = Unsigned32
_ZhoneGponOmciOnuPortAdminLogicalPort_Object = MibTableColumn
zhoneGponOmciOnuPortAdminLogicalPort = _ZhoneGponOmciOnuPortAdminLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 18, 1, 2),
    _ZhoneGponOmciOnuPortAdminLogicalPort_Type()
)
zhoneGponOmciOnuPortAdminLogicalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneGponOmciOnuPortAdminLogicalPort.setStatus("current")


class _ZhoneGponOmciOnuPortAdminState_Type(Integer32):
    """Custom type zhoneGponOmciOnuPortAdminState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("none", 0),
          ("up", 1))
    )


_ZhoneGponOmciOnuPortAdminState_Type.__name__ = "Integer32"
_ZhoneGponOmciOnuPortAdminState_Object = MibTableColumn
zhoneGponOmciOnuPortAdminState = _ZhoneGponOmciOnuPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 18, 1, 3),
    _ZhoneGponOmciOnuPortAdminState_Type()
)
zhoneGponOmciOnuPortAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponOmciOnuPortAdminState.setStatus("current")


class _ZhoneGponOmciOnuPortAdminAutoDetect_Type(Integer32):
    """Custom type zhoneGponOmciOnuPortAdminAutoDetect based on Integer32"""
    defaultValue = 1

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
              12)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("autoFull", 10),
          ("autoHalf", 11),
          ("hundredAuto", 12),
          ("hundredFull", 3),
          ("hundredHalf", 7),
          ("none", 0),
          ("tenAuto", 5),
          ("tenFull", 2),
          ("tenHalf", 6),
          ("thousandAuto", 9),
          ("thousandFull", 4),
          ("thousandHalf", 8))
    )


_ZhoneGponOmciOnuPortAdminAutoDetect_Type.__name__ = "Integer32"
_ZhoneGponOmciOnuPortAdminAutoDetect_Object = MibTableColumn
zhoneGponOmciOnuPortAdminAutoDetect = _ZhoneGponOmciOnuPortAdminAutoDetect_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 18, 1, 4),
    _ZhoneGponOmciOnuPortAdminAutoDetect_Type()
)
zhoneGponOmciOnuPortAdminAutoDetect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponOmciOnuPortAdminAutoDetect.setStatus("current")
_ZhoneGponOmciOnuImageUpgradeTable_Object = MibTable
zhoneGponOmciOnuImageUpgradeTable = _ZhoneGponOmciOnuImageUpgradeTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 19)
)
if mibBuilder.loadTexts:
    zhoneGponOmciOnuImageUpgradeTable.setStatus("current")
_ZhoneGponOmciOnuImageUpgradeEntry_Object = MibTableRow
zhoneGponOmciOnuImageUpgradeEntry = _ZhoneGponOmciOnuImageUpgradeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 19, 1)
)
zhoneGponOmciOnuImageUpgradeEntry.setIndexNames(
    (0, "Zhone-GPON-MIB", "zhoneGponOltOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zhoneGponOmciOnuImageUpgradeEntry.setStatus("current")


class _ZhoneGponOmciOnuImageUpgradeAction_Type(Integer32):
    """Custom type zhoneGponOmciOnuImageUpgradeAction based on Integer32"""
    defaultValue = 0

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
              7)
        )
    )
    namedValues = NamedValues(
        *(("abortDownload", 6),
          ("activate", 2),
          ("activateCommit", 7),
          ("commit", 3),
          ("download", 1),
          ("downloadActivate", 4),
          ("downloadActivateCommit", 5),
          ("none", 0))
    )


_ZhoneGponOmciOnuImageUpgradeAction_Type.__name__ = "Integer32"
_ZhoneGponOmciOnuImageUpgradeAction_Object = MibTableColumn
zhoneGponOmciOnuImageUpgradeAction = _ZhoneGponOmciOnuImageUpgradeAction_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 19, 1, 1),
    _ZhoneGponOmciOnuImageUpgradeAction_Type()
)
zhoneGponOmciOnuImageUpgradeAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponOmciOnuImageUpgradeAction.setStatus("current")


class _ZhoneOnuOmciImageUpgradeFilename_Type(OctetString):
    """Custom type zhoneOnuOmciImageUpgradeFilename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZhoneOnuOmciImageUpgradeFilename_Type.__name__ = "OctetString"
_ZhoneOnuOmciImageUpgradeFilename_Object = MibTableColumn
zhoneOnuOmciImageUpgradeFilename = _ZhoneOnuOmciImageUpgradeFilename_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 19, 1, 2),
    _ZhoneOnuOmciImageUpgradeFilename_Type()
)
zhoneOnuOmciImageUpgradeFilename.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneOnuOmciImageUpgradeFilename.setStatus("current")


class _ZhoneGponOmciOnuImageUpgradePartition_Type(Integer32):
    """Custom type zhoneGponOmciOnuImageUpgradePartition based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("partitionNumber0", 1),
          ("partitionNumber1", 2))
    )


_ZhoneGponOmciOnuImageUpgradePartition_Type.__name__ = "Integer32"
_ZhoneGponOmciOnuImageUpgradePartition_Object = MibTableColumn
zhoneGponOmciOnuImageUpgradePartition = _ZhoneGponOmciOnuImageUpgradePartition_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 19, 1, 3),
    _ZhoneGponOmciOnuImageUpgradePartition_Type()
)
zhoneGponOmciOnuImageUpgradePartition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneGponOmciOnuImageUpgradePartition.setStatus("current")


class _ZhoneOnuOmciImageUpgradeImageVersionPartition0_Type(OctetString):
    """Custom type zhoneOnuOmciImageUpgradeImageVersionPartition0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZhoneOnuOmciImageUpgradeImageVersionPartition0_Type.__name__ = "OctetString"
_ZhoneOnuOmciImageUpgradeImageVersionPartition0_Object = MibTableColumn
zhoneOnuOmciImageUpgradeImageVersionPartition0 = _ZhoneOnuOmciImageUpgradeImageVersionPartition0_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 19, 1, 4),
    _ZhoneOnuOmciImageUpgradeImageVersionPartition0_Type()
)
zhoneOnuOmciImageUpgradeImageVersionPartition0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuOmciImageUpgradeImageVersionPartition0.setStatus("current")


class _ZhoneOnuOmciImageUpgradeImageVersionPartition1_Type(OctetString):
    """Custom type zhoneOnuOmciImageUpgradeImageVersionPartition1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZhoneOnuOmciImageUpgradeImageVersionPartition1_Type.__name__ = "OctetString"
_ZhoneOnuOmciImageUpgradeImageVersionPartition1_Object = MibTableColumn
zhoneOnuOmciImageUpgradeImageVersionPartition1 = _ZhoneOnuOmciImageUpgradeImageVersionPartition1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 19, 1, 5),
    _ZhoneOnuOmciImageUpgradeImageVersionPartition1_Type()
)
zhoneOnuOmciImageUpgradeImageVersionPartition1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuOmciImageUpgradeImageVersionPartition1.setStatus("current")


class _ZhoneOnuOmciImageUpgradeIsCommittedPartition0_Type(Integer32):
    """Custom type zhoneOnuOmciImageUpgradeIsCommittedPartition0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("none", 0),
          ("true", 1))
    )


_ZhoneOnuOmciImageUpgradeIsCommittedPartition0_Type.__name__ = "Integer32"
_ZhoneOnuOmciImageUpgradeIsCommittedPartition0_Object = MibTableColumn
zhoneOnuOmciImageUpgradeIsCommittedPartition0 = _ZhoneOnuOmciImageUpgradeIsCommittedPartition0_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 19, 1, 6),
    _ZhoneOnuOmciImageUpgradeIsCommittedPartition0_Type()
)
zhoneOnuOmciImageUpgradeIsCommittedPartition0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuOmciImageUpgradeIsCommittedPartition0.setStatus("current")


class _ZhoneOnuOmciImageUpgradeIsCommittedPartition1_Type(Integer32):
    """Custom type zhoneOnuOmciImageUpgradeIsCommittedPartition1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("none", 0),
          ("true", 1))
    )


_ZhoneOnuOmciImageUpgradeIsCommittedPartition1_Type.__name__ = "Integer32"
_ZhoneOnuOmciImageUpgradeIsCommittedPartition1_Object = MibTableColumn
zhoneOnuOmciImageUpgradeIsCommittedPartition1 = _ZhoneOnuOmciImageUpgradeIsCommittedPartition1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 19, 1, 7),
    _ZhoneOnuOmciImageUpgradeIsCommittedPartition1_Type()
)
zhoneOnuOmciImageUpgradeIsCommittedPartition1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuOmciImageUpgradeIsCommittedPartition1.setStatus("current")


class _ZhoneOnuOmciImageUpgradeIsActivatedPartition0_Type(Integer32):
    """Custom type zhoneOnuOmciImageUpgradeIsActivatedPartition0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("none", 0),
          ("true", 1))
    )


_ZhoneOnuOmciImageUpgradeIsActivatedPartition0_Type.__name__ = "Integer32"
_ZhoneOnuOmciImageUpgradeIsActivatedPartition0_Object = MibTableColumn
zhoneOnuOmciImageUpgradeIsActivatedPartition0 = _ZhoneOnuOmciImageUpgradeIsActivatedPartition0_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 19, 1, 8),
    _ZhoneOnuOmciImageUpgradeIsActivatedPartition0_Type()
)
zhoneOnuOmciImageUpgradeIsActivatedPartition0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuOmciImageUpgradeIsActivatedPartition0.setStatus("current")


class _ZhoneOnuOmciImageUpgradeIsActivatedPartition1_Type(Integer32):
    """Custom type zhoneOnuOmciImageUpgradeIsActivatedPartition1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("none", 0),
          ("true", 1))
    )


_ZhoneOnuOmciImageUpgradeIsActivatedPartition1_Type.__name__ = "Integer32"
_ZhoneOnuOmciImageUpgradeIsActivatedPartition1_Object = MibTableColumn
zhoneOnuOmciImageUpgradeIsActivatedPartition1 = _ZhoneOnuOmciImageUpgradeIsActivatedPartition1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 19, 1, 9),
    _ZhoneOnuOmciImageUpgradeIsActivatedPartition1_Type()
)
zhoneOnuOmciImageUpgradeIsActivatedPartition1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuOmciImageUpgradeIsActivatedPartition1.setStatus("current")


class _ZhoneOnuOmciImageUpgradeIsValidPartition0_Type(Integer32):
    """Custom type zhoneOnuOmciImageUpgradeIsValidPartition0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("none", 0),
          ("true", 1))
    )


_ZhoneOnuOmciImageUpgradeIsValidPartition0_Type.__name__ = "Integer32"
_ZhoneOnuOmciImageUpgradeIsValidPartition0_Object = MibTableColumn
zhoneOnuOmciImageUpgradeIsValidPartition0 = _ZhoneOnuOmciImageUpgradeIsValidPartition0_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 19, 1, 10),
    _ZhoneOnuOmciImageUpgradeIsValidPartition0_Type()
)
zhoneOnuOmciImageUpgradeIsValidPartition0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuOmciImageUpgradeIsValidPartition0.setStatus("current")


class _ZhoneOnuOmciImageUpgradeIsValidPartition1_Type(Integer32):
    """Custom type zhoneOnuOmciImageUpgradeIsValidPartition1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("none", 0),
          ("true", 1))
    )


_ZhoneOnuOmciImageUpgradeIsValidPartition1_Type.__name__ = "Integer32"
_ZhoneOnuOmciImageUpgradeIsValidPartition1_Object = MibTableColumn
zhoneOnuOmciImageUpgradeIsValidPartition1 = _ZhoneOnuOmciImageUpgradeIsValidPartition1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 19, 1, 11),
    _ZhoneOnuOmciImageUpgradeIsValidPartition1_Type()
)
zhoneOnuOmciImageUpgradeIsValidPartition1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuOmciImageUpgradeIsValidPartition1.setStatus("current")
_ZhoneOnuOmciImageUpgradeDownloadStatus_Type = OnuUpgradeState
_ZhoneOnuOmciImageUpgradeDownloadStatus_Object = MibTableColumn
zhoneOnuOmciImageUpgradeDownloadStatus = _ZhoneOnuOmciImageUpgradeDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 19, 1, 12),
    _ZhoneOnuOmciImageUpgradeDownloadStatus_Type()
)
zhoneOnuOmciImageUpgradeDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneOnuOmciImageUpgradeDownloadStatus.setStatus("current")


class _ZhoneGponOmciOnuImageUpgradeModel_Type(OctetString):
    """Custom type zhoneGponOmciOnuImageUpgradeModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ZhoneGponOmciOnuImageUpgradeModel_Type.__name__ = "OctetString"
_ZhoneGponOmciOnuImageUpgradeModel_Object = MibTableColumn
zhoneGponOmciOnuImageUpgradeModel = _ZhoneGponOmciOnuImageUpgradeModel_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 19, 1, 13),
    _ZhoneGponOmciOnuImageUpgradeModel_Type()
)
zhoneGponOmciOnuImageUpgradeModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOmciOnuImageUpgradeModel.setStatus("current")


class _ZhoneGponOmciOnuImageUpgradeStartTime_Type(OctetString):
    """Custom type zhoneGponOmciOnuImageUpgradeStartTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZhoneGponOmciOnuImageUpgradeStartTime_Type.__name__ = "OctetString"
_ZhoneGponOmciOnuImageUpgradeStartTime_Object = MibTableColumn
zhoneGponOmciOnuImageUpgradeStartTime = _ZhoneGponOmciOnuImageUpgradeStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 19, 1, 14),
    _ZhoneGponOmciOnuImageUpgradeStartTime_Type()
)
zhoneGponOmciOnuImageUpgradeStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOmciOnuImageUpgradeStartTime.setStatus("current")
_ZhoneGponOmciOnuImageUpgradeWillBeActivated_Type = TruthValue
_ZhoneGponOmciOnuImageUpgradeWillBeActivated_Object = MibTableColumn
zhoneGponOmciOnuImageUpgradeWillBeActivated = _ZhoneGponOmciOnuImageUpgradeWillBeActivated_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 19, 1, 15),
    _ZhoneGponOmciOnuImageUpgradeWillBeActivated_Type()
)
zhoneGponOmciOnuImageUpgradeWillBeActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOmciOnuImageUpgradeWillBeActivated.setStatus("current")
_ZhoneGponOmciOnuImageUpgradeWillBeCommitted_Type = TruthValue
_ZhoneGponOmciOnuImageUpgradeWillBeCommitted_Object = MibTableColumn
zhoneGponOmciOnuImageUpgradeWillBeCommitted = _ZhoneGponOmciOnuImageUpgradeWillBeCommitted_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 19, 1, 16),
    _ZhoneGponOmciOnuImageUpgradeWillBeCommitted_Type()
)
zhoneGponOmciOnuImageUpgradeWillBeCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOmciOnuImageUpgradeWillBeCommitted.setStatus("current")


class _ZhoneGponOmciOnuImageUpgradeType_Type(Integer32):
    """Custom type zhoneGponOmciOnuImageUpgradeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("bulk", 3),
          ("manual", 1),
          ("none", 0))
    )


_ZhoneGponOmciOnuImageUpgradeType_Type.__name__ = "Integer32"
_ZhoneGponOmciOnuImageUpgradeType_Object = MibTableColumn
zhoneGponOmciOnuImageUpgradeType = _ZhoneGponOmciOnuImageUpgradeType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 19, 1, 17),
    _ZhoneGponOmciOnuImageUpgradeType_Type()
)
zhoneGponOmciOnuImageUpgradeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOmciOnuImageUpgradeType.setStatus("current")


class _ZhoneGponOmciOnuImageDownloadProgressPercentage_Type(Integer32):
    """Custom type zhoneGponOmciOnuImageDownloadProgressPercentage based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZhoneGponOmciOnuImageDownloadProgressPercentage_Type.__name__ = "Integer32"
_ZhoneGponOmciOnuImageDownloadProgressPercentage_Object = MibTableColumn
zhoneGponOmciOnuImageDownloadProgressPercentage = _ZhoneGponOmciOnuImageDownloadProgressPercentage_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 19, 1, 18),
    _ZhoneGponOmciOnuImageDownloadProgressPercentage_Type()
)
zhoneGponOmciOnuImageDownloadProgressPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOmciOnuImageDownloadProgressPercentage.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOmciOnuImageDownloadProgressPercentage.setUnits("percent")


class _ZhoneGponOmciOnuImageUpgradeMethod_Type(Integer32):
    """Custom type zhoneGponOmciOnuImageUpgradeMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("omci", 1),
          ("tftp", 2))
    )


_ZhoneGponOmciOnuImageUpgradeMethod_Type.__name__ = "Integer32"
_ZhoneGponOmciOnuImageUpgradeMethod_Object = MibTableColumn
zhoneGponOmciOnuImageUpgradeMethod = _ZhoneGponOmciOnuImageUpgradeMethod_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 19, 1, 19),
    _ZhoneGponOmciOnuImageUpgradeMethod_Type()
)
zhoneGponOmciOnuImageUpgradeMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOmciOnuImageUpgradeMethod.setStatus("current")
_ZhoneGponOltStatusTable_Object = MibTable
zhoneGponOltStatusTable = _ZhoneGponOltStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 20)
)
if mibBuilder.loadTexts:
    zhoneGponOltStatusTable.setStatus("current")
_ZhoneGponOltStatusEntry_Object = MibTableRow
zhoneGponOltStatusEntry = _ZhoneGponOltStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 20, 1)
)
zhoneGponOltStatusEntry.setIndexNames(
    (0, "Zhone-GPON-MIB", "zhoneGponOltIfIndex"),
)
if mibBuilder.loadTexts:
    zhoneGponOltStatusEntry.setStatus("current")


class _ZhoneGponOltOpticTemperature_Type(Integer32):
    """Custom type zhoneGponOltOpticTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_ZhoneGponOltOpticTemperature_Type.__name__ = "Integer32"
_ZhoneGponOltOpticTemperature_Object = MibTableColumn
zhoneGponOltOpticTemperature = _ZhoneGponOltOpticTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 20, 1, 1),
    _ZhoneGponOltOpticTemperature_Type()
)
zhoneGponOltOpticTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltOpticTemperature.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltOpticTemperature.setUnits("celcius")


class _ZhoneGponOltOpticVoltage_Type(Unsigned32):
    """Custom type zhoneGponOltOpticVoltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 655),
    )


_ZhoneGponOltOpticVoltage_Type.__name__ = "Unsigned32"
_ZhoneGponOltOpticVoltage_Object = MibTableColumn
zhoneGponOltOpticVoltage = _ZhoneGponOltOpticVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 20, 1, 2),
    _ZhoneGponOltOpticVoltage_Type()
)
zhoneGponOltOpticVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltOpticVoltage.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltOpticVoltage.setUnits("hundredths of volts")


class _ZhoneGponOltOpticTxBiasCurrent_Type(Unsigned32):
    """Custom type zhoneGponOltOpticTxBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131),
    )


_ZhoneGponOltOpticTxBiasCurrent_Type.__name__ = "Unsigned32"
_ZhoneGponOltOpticTxBiasCurrent_Object = MibTableColumn
zhoneGponOltOpticTxBiasCurrent = _ZhoneGponOltOpticTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 20, 1, 3),
    _ZhoneGponOltOpticTxBiasCurrent_Type()
)
zhoneGponOltOpticTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltOpticTxBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltOpticTxBiasCurrent.setUnits("milliAmperes")


class _ZhoneGponOltOpticTxPower_Type(Integer32):
    """Custom type zhoneGponOltOpticTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 200),
    )


_ZhoneGponOltOpticTxPower_Type.__name__ = "Integer32"
_ZhoneGponOltOpticTxPower_Object = MibTableColumn
zhoneGponOltOpticTxPower = _ZhoneGponOltOpticTxPower_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 20, 1, 4),
    _ZhoneGponOltOpticTxPower_Type()
)
zhoneGponOltOpticTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltOpticTxPower.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltOpticTxPower.setUnits("tenths of dB")


class _ZhoneGponOltOpticStatus_Type(Integer32):
    """Custom type zhoneGponOltOpticStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 4),
          ("ok", 1),
          ("oltactive", 16),
          ("sfpnotpresent", 8),
          ("warning", 2))
    )


_ZhoneGponOltOpticStatus_Type.__name__ = "Integer32"
_ZhoneGponOltOpticStatus_Object = MibTableColumn
zhoneGponOltOpticStatus = _ZhoneGponOltOpticStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 20, 1, 5),
    _ZhoneGponOltOpticStatus_Type()
)
zhoneGponOltOpticStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltOpticStatus.setStatus("current")


class _ZhoneGponOltOpticAlarms_Type(Bits):
    """Custom type zhoneGponOltOpticAlarms based on Bits"""
    namedValues = NamedValues(
        *(("rxPwrHigh", 8),
          ("rxPwrLow", 9),
          ("tempHigh", 0),
          ("tempLow", 1),
          ("txBiasHigh", 4),
          ("txBiasLow", 5),
          ("txPwrHigh", 6),
          ("txPwrLow", 7),
          ("vccHigh", 2),
          ("vccLow", 3))
    )

_ZhoneGponOltOpticAlarms_Type.__name__ = "Bits"
_ZhoneGponOltOpticAlarms_Object = MibTableColumn
zhoneGponOltOpticAlarms = _ZhoneGponOltOpticAlarms_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 20, 1, 6),
    _ZhoneGponOltOpticAlarms_Type()
)
zhoneGponOltOpticAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltOpticAlarms.setStatus("current")


class _ZhoneGponOltStatusWord_Type(Bits):
    """Custom type zhoneGponOltStatusWord based on Bits"""
    namedValues = NamedValues(
        *(("lossOfSignal", 6),
          ("noAlarm", 0),
          ("notused1", 1),
          ("notused2", 2),
          ("notused3", 3),
          ("notused4", 4),
          ("notused5", 5),
          ("notused7", 7),
          ("notused8", 8),
          ("outOfService", 9),
          ("rogueOnu", 10),
          ("rogueOnuRssi", 11),
          ("sgmiiGeLinkDown", 12))
    )

_ZhoneGponOltStatusWord_Type.__name__ = "Bits"
_ZhoneGponOltStatusWord_Object = MibTableColumn
zhoneGponOltStatusWord = _ZhoneGponOltStatusWord_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 20, 1, 7),
    _ZhoneGponOltStatusWord_Type()
)
zhoneGponOltStatusWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatusWord.setStatus("current")
_ZhoneGponOltConfiguredOnuCount_Type = Unsigned32
_ZhoneGponOltConfiguredOnuCount_Object = MibTableColumn
zhoneGponOltConfiguredOnuCount = _ZhoneGponOltConfiguredOnuCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 20, 1, 8),
    _ZhoneGponOltConfiguredOnuCount_Type()
)
zhoneGponOltConfiguredOnuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltConfiguredOnuCount.setStatus("current")
_ZhoneGponOltActiveOnuCount_Type = Unsigned32
_ZhoneGponOltActiveOnuCount_Object = MibTableColumn
zhoneGponOltActiveOnuCount = _ZhoneGponOltActiveOnuCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 20, 1, 9),
    _ZhoneGponOltActiveOnuCount_Type()
)
zhoneGponOltActiveOnuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltActiveOnuCount.setStatus("current")
_ZhoneGponOltDbaStatusTable_Object = MibTable
zhoneGponOltDbaStatusTable = _ZhoneGponOltDbaStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 21)
)
if mibBuilder.loadTexts:
    zhoneGponOltDbaStatusTable.setStatus("current")
_ZhoneGponOltDbaStatusEntry_Object = MibTableRow
zhoneGponOltDbaStatusEntry = _ZhoneGponOltDbaStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 21, 1)
)
zhoneGponOltDbaStatusEntry.setIndexNames(
    (0, "Zhone-GPON-MIB", "zhoneGponOltIfIndex"),
)
if mibBuilder.loadTexts:
    zhoneGponOltDbaStatusEntry.setStatus("current")
_ZhoneGponOltDbaTotalAvailableBw_Type = Unsigned32
_ZhoneGponOltDbaTotalAvailableBw_Object = MibTableColumn
zhoneGponOltDbaTotalAvailableBw = _ZhoneGponOltDbaTotalAvailableBw_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 21, 1, 1),
    _ZhoneGponOltDbaTotalAvailableBw_Type()
)
zhoneGponOltDbaTotalAvailableBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltDbaTotalAvailableBw.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltDbaTotalAvailableBw.setUnits("kilobits")
_ZhoneGponOltDbaTotalAvailableCompensatedCbrBw_Type = Unsigned32
_ZhoneGponOltDbaTotalAvailableCompensatedCbrBw_Object = MibTableColumn
zhoneGponOltDbaTotalAvailableCompensatedCbrBw = _ZhoneGponOltDbaTotalAvailableCompensatedCbrBw_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 21, 1, 2),
    _ZhoneGponOltDbaTotalAvailableCompensatedCbrBw_Type()
)
zhoneGponOltDbaTotalAvailableCompensatedCbrBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltDbaTotalAvailableCompensatedCbrBw.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltDbaTotalAvailableCompensatedCbrBw.setUnits("kilobits")
_ZhoneGponOltDbaAllocatedUbrBw_Type = Unsigned32
_ZhoneGponOltDbaAllocatedUbrBw_Object = MibTableColumn
zhoneGponOltDbaAllocatedUbrBw = _ZhoneGponOltDbaAllocatedUbrBw_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 21, 1, 3),
    _ZhoneGponOltDbaAllocatedUbrBw_Type()
)
zhoneGponOltDbaAllocatedUbrBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltDbaAllocatedUbrBw.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltDbaAllocatedUbrBw.setUnits("kilobits")
_ZhoneGponOltDbaAllocatedCbrBw_Type = Unsigned32
_ZhoneGponOltDbaAllocatedCbrBw_Object = MibTableColumn
zhoneGponOltDbaAllocatedCbrBw = _ZhoneGponOltDbaAllocatedCbrBw_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 21, 1, 4),
    _ZhoneGponOltDbaAllocatedCbrBw_Type()
)
zhoneGponOltDbaAllocatedCbrBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltDbaAllocatedCbrBw.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltDbaAllocatedCbrBw.setUnits("kilobits")
_ZhoneGponOltDbaAllocatedCompensatedCbrBw_Type = Unsigned32
_ZhoneGponOltDbaAllocatedCompensatedCbrBw_Object = MibTableColumn
zhoneGponOltDbaAllocatedCompensatedCbrBw = _ZhoneGponOltDbaAllocatedCompensatedCbrBw_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 21, 1, 5),
    _ZhoneGponOltDbaAllocatedCompensatedCbrBw_Type()
)
zhoneGponOltDbaAllocatedCompensatedCbrBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltDbaAllocatedCompensatedCbrBw.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltDbaAllocatedCompensatedCbrBw.setUnits("kilobits")
_ZhoneGponOltDbaAllocatedAssuredBw_Type = Unsigned32
_ZhoneGponOltDbaAllocatedAssuredBw_Object = MibTableColumn
zhoneGponOltDbaAllocatedAssuredBw = _ZhoneGponOltDbaAllocatedAssuredBw_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 21, 1, 6),
    _ZhoneGponOltDbaAllocatedAssuredBw_Type()
)
zhoneGponOltDbaAllocatedAssuredBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltDbaAllocatedAssuredBw.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltDbaAllocatedAssuredBw.setUnits("kilobits")
_ZhoneGponOltDbaAllocatedNonAssuredBw_Type = Unsigned32
_ZhoneGponOltDbaAllocatedNonAssuredBw_Object = MibTableColumn
zhoneGponOltDbaAllocatedNonAssuredBw = _ZhoneGponOltDbaAllocatedNonAssuredBw_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 21, 1, 7),
    _ZhoneGponOltDbaAllocatedNonAssuredBw_Type()
)
zhoneGponOltDbaAllocatedNonAssuredBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltDbaAllocatedNonAssuredBw.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltDbaAllocatedNonAssuredBw.setUnits("kilobits")
_ZhoneGponOltDbaAllocatedBestEffortBw_Type = Unsigned32
_ZhoneGponOltDbaAllocatedBestEffortBw_Object = MibTableColumn
zhoneGponOltDbaAllocatedBestEffortBw = _ZhoneGponOltDbaAllocatedBestEffortBw_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 21, 1, 8),
    _ZhoneGponOltDbaAllocatedBestEffortBw_Type()
)
zhoneGponOltDbaAllocatedBestEffortBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltDbaAllocatedBestEffortBw.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponOltDbaAllocatedBestEffortBw.setUnits("kilobits")


class _ZhoneGponOltDbaMaxAllocIds_Type(Unsigned32):
    """Custom type zhoneGponOltDbaMaxAllocIds based on Unsigned32"""
    defaultValue = 0


_ZhoneGponOltDbaMaxAllocIds_Object = MibTableColumn
zhoneGponOltDbaMaxAllocIds = _ZhoneGponOltDbaMaxAllocIds_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 21, 1, 9),
    _ZhoneGponOltDbaMaxAllocIds_Type()
)
zhoneGponOltDbaMaxAllocIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltDbaMaxAllocIds.setStatus("current")


class _ZhoneGponOltDbaAvailAllocIds_Type(Unsigned32):
    """Custom type zhoneGponOltDbaAvailAllocIds based on Unsigned32"""
    defaultValue = 0


_ZhoneGponOltDbaAvailAllocIds_Object = MibTableColumn
zhoneGponOltDbaAvailAllocIds = _ZhoneGponOltDbaAvailAllocIds_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 21, 1, 10),
    _ZhoneGponOltDbaAvailAllocIds_Type()
)
zhoneGponOltDbaAvailAllocIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltDbaAvailAllocIds.setStatus("current")


class _ZhoneGponOltDbaUsedAllocIds_Type(Unsigned32):
    """Custom type zhoneGponOltDbaUsedAllocIds based on Unsigned32"""
    defaultValue = 0


_ZhoneGponOltDbaUsedAllocIds_Object = MibTableColumn
zhoneGponOltDbaUsedAllocIds = _ZhoneGponOltDbaUsedAllocIds_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 21, 1, 11),
    _ZhoneGponOltDbaUsedAllocIds_Type()
)
zhoneGponOltDbaUsedAllocIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltDbaUsedAllocIds.setStatus("current")


class _ZhoneGponOltDbaMaxDbaAllocIds_Type(Unsigned32):
    """Custom type zhoneGponOltDbaMaxDbaAllocIds based on Unsigned32"""
    defaultValue = 0


_ZhoneGponOltDbaMaxDbaAllocIds_Object = MibTableColumn
zhoneGponOltDbaMaxDbaAllocIds = _ZhoneGponOltDbaMaxDbaAllocIds_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 21, 1, 12),
    _ZhoneGponOltDbaMaxDbaAllocIds_Type()
)
zhoneGponOltDbaMaxDbaAllocIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltDbaMaxDbaAllocIds.setStatus("current")


class _ZhoneGponOltDbaAvailDbaAllocIds_Type(Unsigned32):
    """Custom type zhoneGponOltDbaAvailDbaAllocIds based on Unsigned32"""
    defaultValue = 0


_ZhoneGponOltDbaAvailDbaAllocIds_Object = MibTableColumn
zhoneGponOltDbaAvailDbaAllocIds = _ZhoneGponOltDbaAvailDbaAllocIds_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 21, 1, 13),
    _ZhoneGponOltDbaAvailDbaAllocIds_Type()
)
zhoneGponOltDbaAvailDbaAllocIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltDbaAvailDbaAllocIds.setStatus("current")


class _ZhoneGponOltDbaUsedDbaAllocIds_Type(Unsigned32):
    """Custom type zhoneGponOltDbaUsedDbaAllocIds based on Unsigned32"""
    defaultValue = 0


_ZhoneGponOltDbaUsedDbaAllocIds_Object = MibTableColumn
zhoneGponOltDbaUsedDbaAllocIds = _ZhoneGponOltDbaUsedDbaAllocIds_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 21, 1, 14),
    _ZhoneGponOltDbaUsedDbaAllocIds_Type()
)
zhoneGponOltDbaUsedDbaAllocIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltDbaUsedDbaAllocIds.setStatus("current")


class _ZhoneGponOltDbaTotalOltGemPorts_Type(Unsigned32):
    """Custom type zhoneGponOltDbaTotalOltGemPorts based on Unsigned32"""
    defaultValue = 0


_ZhoneGponOltDbaTotalOltGemPorts_Object = MibTableColumn
zhoneGponOltDbaTotalOltGemPorts = _ZhoneGponOltDbaTotalOltGemPorts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 21, 1, 15),
    _ZhoneGponOltDbaTotalOltGemPorts_Type()
)
zhoneGponOltDbaTotalOltGemPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltDbaTotalOltGemPorts.setStatus("current")
_ZhoneGponOltDbaLastCacRc_Type = GponCacRc
_ZhoneGponOltDbaLastCacRc_Object = MibTableColumn
zhoneGponOltDbaLastCacRc = _ZhoneGponOltDbaLastCacRc_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 21, 1, 16),
    _ZhoneGponOltDbaLastCacRc_Type()
)
zhoneGponOltDbaLastCacRc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltDbaLastCacRc.setStatus("current")
_ZhoneGponUpgradeByStateTable_Object = MibTable
zhoneGponUpgradeByStateTable = _ZhoneGponUpgradeByStateTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 22)
)
if mibBuilder.loadTexts:
    zhoneGponUpgradeByStateTable.setStatus("current")
_ZhoneGponUpgradeByStateEntry_Object = MibTableRow
zhoneGponUpgradeByStateEntry = _ZhoneGponUpgradeByStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 22, 1)
)
zhoneGponUpgradeByStateEntry.setIndexNames(
    (0, "Zhone-GPON-MIB", "zhoneOnuOmciImageUpgradeDownloadStatus"),
    (0, "Zhone", "zhoneSlotIndex"),
    (0, "Zhone-GPON-MIB", "zhoneGponUpgradeOlt"),
    (0, "Zhone-GPON-MIB", "zhoneGponUpgradeOnu"),
)
if mibBuilder.loadTexts:
    zhoneGponUpgradeByStateEntry.setStatus("current")


class _ZhoneGponUpgradeOlt_Type(Integer32):
    """Custom type zhoneGponUpgradeOlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ZhoneGponUpgradeOlt_Type.__name__ = "Integer32"
_ZhoneGponUpgradeOlt_Object = MibTableColumn
zhoneGponUpgradeOlt = _ZhoneGponUpgradeOlt_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 22, 1, 1),
    _ZhoneGponUpgradeOlt_Type()
)
zhoneGponUpgradeOlt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneGponUpgradeOlt.setStatus("current")


class _ZhoneGponUpgradeOnu_Type(Integer32):
    """Custom type zhoneGponUpgradeOnu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_ZhoneGponUpgradeOnu_Type.__name__ = "Integer32"
_ZhoneGponUpgradeOnu_Object = MibTableColumn
zhoneGponUpgradeOnu = _ZhoneGponUpgradeOnu_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 22, 1, 2),
    _ZhoneGponUpgradeOnu_Type()
)
zhoneGponUpgradeOnu.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneGponUpgradeOnu.setStatus("current")


class _ZhoneGponUpgradeModel_Type(OctetString):
    """Custom type zhoneGponUpgradeModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ZhoneGponUpgradeModel_Type.__name__ = "OctetString"
_ZhoneGponUpgradeModel_Object = MibTableColumn
zhoneGponUpgradeModel = _ZhoneGponUpgradeModel_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 22, 1, 3),
    _ZhoneGponUpgradeModel_Type()
)
zhoneGponUpgradeModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponUpgradeModel.setStatus("current")


class _ZhoneGponUpgradeStartTime_Type(OctetString):
    """Custom type zhoneGponUpgradeStartTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZhoneGponUpgradeStartTime_Type.__name__ = "OctetString"
_ZhoneGponUpgradeStartTime_Object = MibTableColumn
zhoneGponUpgradeStartTime = _ZhoneGponUpgradeStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 22, 1, 4),
    _ZhoneGponUpgradeStartTime_Type()
)
zhoneGponUpgradeStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponUpgradeStartTime.setStatus("current")
_ZhoneGponUpgradeIfIndex_Type = InterfaceIndex
_ZhoneGponUpgradeIfIndex_Object = MibTableColumn
zhoneGponUpgradeIfIndex = _ZhoneGponUpgradeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 22, 1, 5),
    _ZhoneGponUpgradeIfIndex_Type()
)
zhoneGponUpgradeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponUpgradeIfIndex.setStatus("current")
_ZhoneGponUpgradeByStateOnuState_Type = OnuUpgradeState
_ZhoneGponUpgradeByStateOnuState_Object = MibTableColumn
zhoneGponUpgradeByStateOnuState = _ZhoneGponUpgradeByStateOnuState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 22, 1, 6),
    _ZhoneGponUpgradeByStateOnuState_Type()
)
zhoneGponUpgradeByStateOnuState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponUpgradeByStateOnuState.setStatus("current")
_ZhoneGponUpgradeByStateWillBeActivated_Type = TruthValue
_ZhoneGponUpgradeByStateWillBeActivated_Object = MibTableColumn
zhoneGponUpgradeByStateWillBeActivated = _ZhoneGponUpgradeByStateWillBeActivated_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 22, 1, 7),
    _ZhoneGponUpgradeByStateWillBeActivated_Type()
)
zhoneGponUpgradeByStateWillBeActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponUpgradeByStateWillBeActivated.setStatus("current")
_ZhoneGponUpgradeByStateWillBeCommitted_Type = TruthValue
_ZhoneGponUpgradeByStateWillBeCommitted_Object = MibTableColumn
zhoneGponUpgradeByStateWillBeCommitted = _ZhoneGponUpgradeByStateWillBeCommitted_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 22, 1, 8),
    _ZhoneGponUpgradeByStateWillBeCommitted_Type()
)
zhoneGponUpgradeByStateWillBeCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponUpgradeByStateWillBeCommitted.setStatus("current")


class _ZhoneGponUpgradeByStateUpgradeType_Type(Integer32):
    """Custom type zhoneGponUpgradeByStateUpgradeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("bulk", 3),
          ("manual", 1),
          ("none", 0))
    )


_ZhoneGponUpgradeByStateUpgradeType_Type.__name__ = "Integer32"
_ZhoneGponUpgradeByStateUpgradeType_Object = MibTableColumn
zhoneGponUpgradeByStateUpgradeType = _ZhoneGponUpgradeByStateUpgradeType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 22, 1, 9),
    _ZhoneGponUpgradeByStateUpgradeType_Type()
)
zhoneGponUpgradeByStateUpgradeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponUpgradeByStateUpgradeType.setStatus("current")


class _ZhoneGponUpgradeByStatePartition_Type(Integer32):
    """Custom type zhoneGponUpgradeByStatePartition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("partitionNumber0", 1),
          ("partitionNumber1", 2))
    )


_ZhoneGponUpgradeByStatePartition_Type.__name__ = "Integer32"
_ZhoneGponUpgradeByStatePartition_Object = MibTableColumn
zhoneGponUpgradeByStatePartition = _ZhoneGponUpgradeByStatePartition_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 22, 1, 10),
    _ZhoneGponUpgradeByStatePartition_Type()
)
zhoneGponUpgradeByStatePartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponUpgradeByStatePartition.setStatus("current")


class _ZhoneGponUpgradeProgressPercentage_Type(Integer32):
    """Custom type zhoneGponUpgradeProgressPercentage based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZhoneGponUpgradeProgressPercentage_Type.__name__ = "Integer32"
_ZhoneGponUpgradeProgressPercentage_Object = MibTableColumn
zhoneGponUpgradeProgressPercentage = _ZhoneGponUpgradeProgressPercentage_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 22, 1, 11),
    _ZhoneGponUpgradeProgressPercentage_Type()
)
zhoneGponUpgradeProgressPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponUpgradeProgressPercentage.setStatus("current")
if mibBuilder.loadTexts:
    zhoneGponUpgradeProgressPercentage.setUnits("percent")


class _ZhoneGponUpgradeByStateMethod_Type(Integer32):
    """Custom type zhoneGponUpgradeByStateMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("omci", 1),
          ("tftp", 2))
    )


_ZhoneGponUpgradeByStateMethod_Type.__name__ = "Integer32"
_ZhoneGponUpgradeByStateMethod_Object = MibTableColumn
zhoneGponUpgradeByStateMethod = _ZhoneGponUpgradeByStateMethod_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 22, 1, 12),
    _ZhoneGponUpgradeByStateMethod_Type()
)
zhoneGponUpgradeByStateMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponUpgradeByStateMethod.setStatus("current")
_ZhoneGponCmd_ObjectIdentity = ObjectIdentity
zhoneGponCmd = _ZhoneGponCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 23)
)


class _ZhoneGponCmdOperation_Type(Integer32):
    """Custom type zhoneGponCmdOperation based on Integer32"""
    defaultValue = 1

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
        *(("onuApply", 1),
          ("onuDisableAutoCfg", 6),
          ("onuEnableAutoCfg", 5),
          ("onuReboot", 3),
          ("onuResync", 2),
          ("onuSet2default", 4))
    )


_ZhoneGponCmdOperation_Type.__name__ = "Integer32"
_ZhoneGponCmdOperation_Object = MibScalar
zhoneGponCmdOperation = _ZhoneGponCmdOperation_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 23, 1),
    _ZhoneGponCmdOperation_Type()
)
zhoneGponCmdOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponCmdOperation.setStatus("current")


class _ZhoneGponCmdFilterMask_Type(Bits):
    """Custom type zhoneGponCmdFilterMask based on Bits"""
    namedValues = NamedValues(
        *(("filterOlt", 2),
          ("filterOnu", 3),
          ("filterShelf", 0),
          ("filterSlot", 1))
    )

_ZhoneGponCmdFilterMask_Type.__name__ = "Bits"
_ZhoneGponCmdFilterMask_Object = MibScalar
zhoneGponCmdFilterMask = _ZhoneGponCmdFilterMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 23, 2),
    _ZhoneGponCmdFilterMask_Type()
)
zhoneGponCmdFilterMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponCmdFilterMask.setStatus("current")


class _ZhoneGponCmdShelf_Type(Unsigned32):
    """Custom type zhoneGponCmdShelf based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ZhoneGponCmdShelf_Type.__name__ = "Unsigned32"
_ZhoneGponCmdShelf_Object = MibScalar
zhoneGponCmdShelf = _ZhoneGponCmdShelf_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 23, 3),
    _ZhoneGponCmdShelf_Type()
)
zhoneGponCmdShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponCmdShelf.setStatus("current")


class _ZhoneGponCmdSlot_Type(Unsigned32):
    """Custom type zhoneGponCmdSlot based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ZhoneGponCmdSlot_Type.__name__ = "Unsigned32"
_ZhoneGponCmdSlot_Object = MibScalar
zhoneGponCmdSlot = _ZhoneGponCmdSlot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 23, 4),
    _ZhoneGponCmdSlot_Type()
)
zhoneGponCmdSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponCmdSlot.setStatus("current")


class _ZhoneGponCmdOlt_Type(Unsigned32):
    """Custom type zhoneGponCmdOlt based on Unsigned32"""
    defaultValue = 1


_ZhoneGponCmdOlt_Object = MibScalar
zhoneGponCmdOlt = _ZhoneGponCmdOlt_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 23, 5),
    _ZhoneGponCmdOlt_Type()
)
zhoneGponCmdOlt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponCmdOlt.setStatus("current")


class _ZhoneGponCmdOnu_Type(Unsigned32):
    """Custom type zhoneGponCmdOnu based on Unsigned32"""
    defaultValue = 1


_ZhoneGponCmdOnu_Object = MibScalar
zhoneGponCmdOnu = _ZhoneGponCmdOnu_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 23, 6),
    _ZhoneGponCmdOnu_Type()
)
zhoneGponCmdOnu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponCmdOnu.setStatus("current")
_ZhoneGponOltStatisticsTable_Object = MibTable
zhoneGponOltStatisticsTable = _ZhoneGponOltStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24)
)
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsTable.setStatus("current")
_ZhoneGponOltStatisticsEntry_Object = MibTableRow
zhoneGponOltStatisticsEntry = _ZhoneGponOltStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1)
)
zhoneGponOltStatisticsEntry.setIndexNames(
    (0, "Zhone-GPON-MIB", "zhoneGponOltIfIndex"),
)
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsEntry.setStatus("current")
_ZhoneGponOltStatisticsUpstreamValidGemFrames_Type = Counter64
_ZhoneGponOltStatisticsUpstreamValidGemFrames_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamValidGemFrames = _ZhoneGponOltStatisticsUpstreamValidGemFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 1),
    _ZhoneGponOltStatisticsUpstreamValidGemFrames_Type()
)
zhoneGponOltStatisticsUpstreamValidGemFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamValidGemFrames.setStatus("current")
_ZhoneGponOltStatisticsUpstreamDiscardedFrames_Type = Counter64
_ZhoneGponOltStatisticsUpstreamDiscardedFrames_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamDiscardedFrames = _ZhoneGponOltStatisticsUpstreamDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 2),
    _ZhoneGponOltStatisticsUpstreamDiscardedFrames_Type()
)
zhoneGponOltStatisticsUpstreamDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamDiscardedFrames.setStatus("current")
_ZhoneGponOltStatisticsUpstreamGemFrames_Type = Counter64
_ZhoneGponOltStatisticsUpstreamGemFrames_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamGemFrames = _ZhoneGponOltStatisticsUpstreamGemFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 3),
    _ZhoneGponOltStatisticsUpstreamGemFrames_Type()
)
zhoneGponOltStatisticsUpstreamGemFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamGemFrames.setStatus("current")
_ZhoneGponOltStatisticsUpstreamOmciFrames_Type = Counter64
_ZhoneGponOltStatisticsUpstreamOmciFrames_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamOmciFrames = _ZhoneGponOltStatisticsUpstreamOmciFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 4),
    _ZhoneGponOltStatisticsUpstreamOmciFrames_Type()
)
zhoneGponOltStatisticsUpstreamOmciFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamOmciFrames.setStatus("current")
_ZhoneGponOltStatisticsUpstreamPloamFrames_Type = Counter64
_ZhoneGponOltStatisticsUpstreamPloamFrames_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamPloamFrames = _ZhoneGponOltStatisticsUpstreamPloamFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 5),
    _ZhoneGponOltStatisticsUpstreamPloamFrames_Type()
)
zhoneGponOltStatisticsUpstreamPloamFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamPloamFrames.setStatus("current")
_ZhoneGponOltStatisticsUpstreamIdlePloamFrames_Type = Counter64
_ZhoneGponOltStatisticsUpstreamIdlePloamFrames_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamIdlePloamFrames = _ZhoneGponOltStatisticsUpstreamIdlePloamFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 6),
    _ZhoneGponOltStatisticsUpstreamIdlePloamFrames_Type()
)
zhoneGponOltStatisticsUpstreamIdlePloamFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamIdlePloamFrames.setStatus("current")
_ZhoneGponOltStatisticsDownstreamValidGemFrames_Type = Counter64
_ZhoneGponOltStatisticsDownstreamValidGemFrames_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamValidGemFrames = _ZhoneGponOltStatisticsDownstreamValidGemFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 7),
    _ZhoneGponOltStatisticsDownstreamValidGemFrames_Type()
)
zhoneGponOltStatisticsDownstreamValidGemFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamValidGemFrames.setStatus("current")
_ZhoneGponOltStatisticsDownstreamDiscardedFrames_Type = Counter64
_ZhoneGponOltStatisticsDownstreamDiscardedFrames_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamDiscardedFrames = _ZhoneGponOltStatisticsDownstreamDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 8),
    _ZhoneGponOltStatisticsDownstreamDiscardedFrames_Type()
)
zhoneGponOltStatisticsDownstreamDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamDiscardedFrames.setStatus("current")
_ZhoneGponOltStatisticsDownstreamGemFrames_Type = Counter64
_ZhoneGponOltStatisticsDownstreamGemFrames_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamGemFrames = _ZhoneGponOltStatisticsDownstreamGemFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 9),
    _ZhoneGponOltStatisticsDownstreamGemFrames_Type()
)
zhoneGponOltStatisticsDownstreamGemFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamGemFrames.setStatus("current")
_ZhoneGponOltStatisticsDownstreamOmciFrames_Type = Counter64
_ZhoneGponOltStatisticsDownstreamOmciFrames_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamOmciFrames = _ZhoneGponOltStatisticsDownstreamOmciFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 10),
    _ZhoneGponOltStatisticsDownstreamOmciFrames_Type()
)
zhoneGponOltStatisticsDownstreamOmciFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamOmciFrames.setStatus("current")
_ZhoneGponOltStatisticsDownstreamPloamFrames_Type = Counter64
_ZhoneGponOltStatisticsDownstreamPloamFrames_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamPloamFrames = _ZhoneGponOltStatisticsDownstreamPloamFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 11),
    _ZhoneGponOltStatisticsDownstreamPloamFrames_Type()
)
zhoneGponOltStatisticsDownstreamPloamFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamPloamFrames.setStatus("current")
_ZhoneGponOltStatisticsDownstreamIdlePloamFrames_Type = Counter64
_ZhoneGponOltStatisticsDownstreamIdlePloamFrames_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamIdlePloamFrames = _ZhoneGponOltStatisticsDownstreamIdlePloamFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 12),
    _ZhoneGponOltStatisticsDownstreamIdlePloamFrames_Type()
)
zhoneGponOltStatisticsDownstreamIdlePloamFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamIdlePloamFrames.setStatus("deprecated")
_ZhoneGponOltStatisticsDownstreamPonValidEthernetPkts_Type = Counter64
_ZhoneGponOltStatisticsDownstreamPonValidEthernetPkts_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamPonValidEthernetPkts = _ZhoneGponOltStatisticsDownstreamPonValidEthernetPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 13),
    _ZhoneGponOltStatisticsDownstreamPonValidEthernetPkts_Type()
)
zhoneGponOltStatisticsDownstreamPonValidEthernetPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamPonValidEthernetPkts.setStatus("current")
_ZhoneGponOltStatisticsDownstreamPonCpuPkts_Type = Counter64
_ZhoneGponOltStatisticsDownstreamPonCpuPkts_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamPonCpuPkts = _ZhoneGponOltStatisticsDownstreamPonCpuPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 14),
    _ZhoneGponOltStatisticsDownstreamPonCpuPkts_Type()
)
zhoneGponOltStatisticsDownstreamPonCpuPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamPonCpuPkts.setStatus("current")
_ZhoneGponOltStatisticsDownstreamTxBytes_Type = Counter64
_ZhoneGponOltStatisticsDownstreamTxBytes_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamTxBytes = _ZhoneGponOltStatisticsDownstreamTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 15),
    _ZhoneGponOltStatisticsDownstreamTxBytes_Type()
)
zhoneGponOltStatisticsDownstreamTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamTxBytes.setStatus("current")
_ZhoneGponOltStatisticsUpstreamPonValidPkts_Type = Counter64
_ZhoneGponOltStatisticsUpstreamPonValidPkts_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamPonValidPkts = _ZhoneGponOltStatisticsUpstreamPonValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 16),
    _ZhoneGponOltStatisticsUpstreamPonValidPkts_Type()
)
zhoneGponOltStatisticsUpstreamPonValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamPonValidPkts.setStatus("current")
_ZhoneGponOltStatisticsUpstreamPonValidNotIdlePloams_Type = Counter64
_ZhoneGponOltStatisticsUpstreamPonValidNotIdlePloams_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamPonValidNotIdlePloams = _ZhoneGponOltStatisticsUpstreamPonValidNotIdlePloams_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 17),
    _ZhoneGponOltStatisticsUpstreamPonValidNotIdlePloams_Type()
)
zhoneGponOltStatisticsUpstreamPonValidNotIdlePloams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamPonValidNotIdlePloams.setStatus("current")
_ZhoneGponOltStatisticsUpstreamPonErrorPloams_Type = Counter64
_ZhoneGponOltStatisticsUpstreamPonErrorPloams_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamPonErrorPloams = _ZhoneGponOltStatisticsUpstreamPonErrorPloams_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 18),
    _ZhoneGponOltStatisticsUpstreamPonErrorPloams_Type()
)
zhoneGponOltStatisticsUpstreamPonErrorPloams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamPonErrorPloams.setStatus("current")
_ZhoneGponOltStatisticsUpstreamPonInvalidPkts_Type = Counter64
_ZhoneGponOltStatisticsUpstreamPonInvalidPkts_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamPonInvalidPkts = _ZhoneGponOltStatisticsUpstreamPonInvalidPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 19),
    _ZhoneGponOltStatisticsUpstreamPonInvalidPkts_Type()
)
zhoneGponOltStatisticsUpstreamPonInvalidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamPonInvalidPkts.setStatus("current")
_ZhoneGponOltStatisticsUpstreamDroppedPktsInactivePorts_Type = Counter64
_ZhoneGponOltStatisticsUpstreamDroppedPktsInactivePorts_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamDroppedPktsInactivePorts = _ZhoneGponOltStatisticsUpstreamDroppedPktsInactivePorts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 20),
    _ZhoneGponOltStatisticsUpstreamDroppedPktsInactivePorts_Type()
)
zhoneGponOltStatisticsUpstreamDroppedPktsInactivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamDroppedPktsInactivePorts.setStatus("current")
_ZhoneGponOltStatisticsUpstreamDroppedPloamsFifoFull_Type = Counter64
_ZhoneGponOltStatisticsUpstreamDroppedPloamsFifoFull_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamDroppedPloamsFifoFull = _ZhoneGponOltStatisticsUpstreamDroppedPloamsFifoFull_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 21),
    _ZhoneGponOltStatisticsUpstreamDroppedPloamsFifoFull_Type()
)
zhoneGponOltStatisticsUpstreamDroppedPloamsFifoFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamDroppedPloamsFifoFull.setStatus("current")
_ZhoneGponOltStatisticsDownstreamTmValidPkts_Type = Counter64
_ZhoneGponOltStatisticsDownstreamTmValidPkts_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamTmValidPkts = _ZhoneGponOltStatisticsDownstreamTmValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 22),
    _ZhoneGponOltStatisticsDownstreamTmValidPkts_Type()
)
zhoneGponOltStatisticsDownstreamTmValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamTmValidPkts.setStatus("current")
_ZhoneGponOltStatisticsDownstreamTmCrcPkts_Type = Counter64
_ZhoneGponOltStatisticsDownstreamTmCrcPkts_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamTmCrcPkts = _ZhoneGponOltStatisticsDownstreamTmCrcPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 23),
    _ZhoneGponOltStatisticsDownstreamTmCrcPkts_Type()
)
zhoneGponOltStatisticsDownstreamTmCrcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamTmCrcPkts.setStatus("current")
_ZhoneGponOltStatisticsDownstreamTmDroppedCpuPkts_Type = Counter64
_ZhoneGponOltStatisticsDownstreamTmDroppedCpuPkts_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamTmDroppedCpuPkts = _ZhoneGponOltStatisticsDownstreamTmDroppedCpuPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 24),
    _ZhoneGponOltStatisticsDownstreamTmDroppedCpuPkts_Type()
)
zhoneGponOltStatisticsDownstreamTmDroppedCpuPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamTmDroppedCpuPkts.setStatus("current")
_ZhoneGponOltStatisticsDownstreamTmMacLookupMiss_Type = Counter64
_ZhoneGponOltStatisticsDownstreamTmMacLookupMiss_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamTmMacLookupMiss = _ZhoneGponOltStatisticsDownstreamTmMacLookupMiss_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 25),
    _ZhoneGponOltStatisticsDownstreamTmMacLookupMiss_Type()
)
zhoneGponOltStatisticsDownstreamTmMacLookupMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamTmMacLookupMiss.setStatus("current")
_ZhoneGponOltStatisticsDownstreamTmPktsForwardedFromHmToPon_Type = Counter64
_ZhoneGponOltStatisticsDownstreamTmPktsForwardedFromHmToPon_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamTmPktsForwardedFromHmToPon = _ZhoneGponOltStatisticsDownstreamTmPktsForwardedFromHmToPon_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 26),
    _ZhoneGponOltStatisticsDownstreamTmPktsForwardedFromHmToPon_Type()
)
zhoneGponOltStatisticsDownstreamTmPktsForwardedFromHmToPon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamTmPktsForwardedFromHmToPon.setStatus("current")
_ZhoneGponOltStatisticsDownstreamTmPktsDroppedGemPidNotEnabled_Type = Counter64
_ZhoneGponOltStatisticsDownstreamTmPktsDroppedGemPidNotEnabled_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamTmPktsDroppedGemPidNotEnabled = _ZhoneGponOltStatisticsDownstreamTmPktsDroppedGemPidNotEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 27),
    _ZhoneGponOltStatisticsDownstreamTmPktsDroppedGemPidNotEnabled_Type()
)
zhoneGponOltStatisticsDownstreamTmPktsDroppedGemPidNotEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamTmPktsDroppedGemPidNotEnabled.setStatus("current")
_ZhoneGponOltStatisticsDownstreamTmQ0ValidPkts_Type = Counter64
_ZhoneGponOltStatisticsDownstreamTmQ0ValidPkts_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamTmQ0ValidPkts = _ZhoneGponOltStatisticsDownstreamTmQ0ValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 28),
    _ZhoneGponOltStatisticsDownstreamTmQ0ValidPkts_Type()
)
zhoneGponOltStatisticsDownstreamTmQ0ValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamTmQ0ValidPkts.setStatus("current")
_ZhoneGponOltStatisticsDownstreamTmQ0DroppedPkts_Type = Counter64
_ZhoneGponOltStatisticsDownstreamTmQ0DroppedPkts_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamTmQ0DroppedPkts = _ZhoneGponOltStatisticsDownstreamTmQ0DroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 29),
    _ZhoneGponOltStatisticsDownstreamTmQ0DroppedPkts_Type()
)
zhoneGponOltStatisticsDownstreamTmQ0DroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamTmQ0DroppedPkts.setStatus("current")
_ZhoneGponOltStatisticsDownstreamTmQ1ValidPkts_Type = Counter64
_ZhoneGponOltStatisticsDownstreamTmQ1ValidPkts_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamTmQ1ValidPkts = _ZhoneGponOltStatisticsDownstreamTmQ1ValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 30),
    _ZhoneGponOltStatisticsDownstreamTmQ1ValidPkts_Type()
)
zhoneGponOltStatisticsDownstreamTmQ1ValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamTmQ1ValidPkts.setStatus("current")
_ZhoneGponOltStatisticsDownstreamTmQ1DroppedPkts_Type = Counter64
_ZhoneGponOltStatisticsDownstreamTmQ1DroppedPkts_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamTmQ1DroppedPkts = _ZhoneGponOltStatisticsDownstreamTmQ1DroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 31),
    _ZhoneGponOltStatisticsDownstreamTmQ1DroppedPkts_Type()
)
zhoneGponOltStatisticsDownstreamTmQ1DroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamTmQ1DroppedPkts.setStatus("current")
_ZhoneGponOltStatisticsDownstreamTmQ2ValidPkts_Type = Counter64
_ZhoneGponOltStatisticsDownstreamTmQ2ValidPkts_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamTmQ2ValidPkts = _ZhoneGponOltStatisticsDownstreamTmQ2ValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 32),
    _ZhoneGponOltStatisticsDownstreamTmQ2ValidPkts_Type()
)
zhoneGponOltStatisticsDownstreamTmQ2ValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamTmQ2ValidPkts.setStatus("current")
_ZhoneGponOltStatisticsDownstreamTmQ2DroppedPkts_Type = Counter64
_ZhoneGponOltStatisticsDownstreamTmQ2DroppedPkts_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamTmQ2DroppedPkts = _ZhoneGponOltStatisticsDownstreamTmQ2DroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 33),
    _ZhoneGponOltStatisticsDownstreamTmQ2DroppedPkts_Type()
)
zhoneGponOltStatisticsDownstreamTmQ2DroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamTmQ2DroppedPkts.setStatus("current")
_ZhoneGponOltStatisticsDownstreamTmQ3ValidPkts_Type = Counter64
_ZhoneGponOltStatisticsDownstreamTmQ3ValidPkts_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamTmQ3ValidPkts = _ZhoneGponOltStatisticsDownstreamTmQ3ValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 34),
    _ZhoneGponOltStatisticsDownstreamTmQ3ValidPkts_Type()
)
zhoneGponOltStatisticsDownstreamTmQ3ValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamTmQ3ValidPkts.setStatus("current")
_ZhoneGponOltStatisticsDownstreamTmQ3DroppedPkts_Type = Counter64
_ZhoneGponOltStatisticsDownstreamTmQ3DroppedPkts_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamTmQ3DroppedPkts = _ZhoneGponOltStatisticsDownstreamTmQ3DroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 35),
    _ZhoneGponOltStatisticsDownstreamTmQ3DroppedPkts_Type()
)
zhoneGponOltStatisticsDownstreamTmQ3DroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamTmQ3DroppedPkts.setStatus("current")
_ZhoneGponOltStatisticsDownstreamTmQ4ValidPkts_Type = Counter64
_ZhoneGponOltStatisticsDownstreamTmQ4ValidPkts_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamTmQ4ValidPkts = _ZhoneGponOltStatisticsDownstreamTmQ4ValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 36),
    _ZhoneGponOltStatisticsDownstreamTmQ4ValidPkts_Type()
)
zhoneGponOltStatisticsDownstreamTmQ4ValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamTmQ4ValidPkts.setStatus("current")
_ZhoneGponOltStatisticsDownstreamTmQ4DroppedPkts_Type = Counter64
_ZhoneGponOltStatisticsDownstreamTmQ4DroppedPkts_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamTmQ4DroppedPkts = _ZhoneGponOltStatisticsDownstreamTmQ4DroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 37),
    _ZhoneGponOltStatisticsDownstreamTmQ4DroppedPkts_Type()
)
zhoneGponOltStatisticsDownstreamTmQ4DroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamTmQ4DroppedPkts.setStatus("current")
_ZhoneGponOltStatisticsDownstreamTmQ5ValidPkts_Type = Counter64
_ZhoneGponOltStatisticsDownstreamTmQ5ValidPkts_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamTmQ5ValidPkts = _ZhoneGponOltStatisticsDownstreamTmQ5ValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 38),
    _ZhoneGponOltStatisticsDownstreamTmQ5ValidPkts_Type()
)
zhoneGponOltStatisticsDownstreamTmQ5ValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamTmQ5ValidPkts.setStatus("current")
_ZhoneGponOltStatisticsDownstreamTmQ5DroppedPkts_Type = Counter64
_ZhoneGponOltStatisticsDownstreamTmQ5DroppedPkts_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamTmQ5DroppedPkts = _ZhoneGponOltStatisticsDownstreamTmQ5DroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 39),
    _ZhoneGponOltStatisticsDownstreamTmQ5DroppedPkts_Type()
)
zhoneGponOltStatisticsDownstreamTmQ5DroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamTmQ5DroppedPkts.setStatus("current")
_ZhoneGponOltStatisticsDownstreamTmQ6ValidPkts_Type = Counter64
_ZhoneGponOltStatisticsDownstreamTmQ6ValidPkts_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamTmQ6ValidPkts = _ZhoneGponOltStatisticsDownstreamTmQ6ValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 40),
    _ZhoneGponOltStatisticsDownstreamTmQ6ValidPkts_Type()
)
zhoneGponOltStatisticsDownstreamTmQ6ValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamTmQ6ValidPkts.setStatus("current")
_ZhoneGponOltStatisticsDownstreamTmQ6DroppedPkts_Type = Counter64
_ZhoneGponOltStatisticsDownstreamTmQ6DroppedPkts_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamTmQ6DroppedPkts = _ZhoneGponOltStatisticsDownstreamTmQ6DroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 41),
    _ZhoneGponOltStatisticsDownstreamTmQ6DroppedPkts_Type()
)
zhoneGponOltStatisticsDownstreamTmQ6DroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamTmQ6DroppedPkts.setStatus("current")
_ZhoneGponOltStatisticsDownstreamTmQ7ValidPkts_Type = Counter64
_ZhoneGponOltStatisticsDownstreamTmQ7ValidPkts_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamTmQ7ValidPkts = _ZhoneGponOltStatisticsDownstreamTmQ7ValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 42),
    _ZhoneGponOltStatisticsDownstreamTmQ7ValidPkts_Type()
)
zhoneGponOltStatisticsDownstreamTmQ7ValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamTmQ7ValidPkts.setStatus("current")
_ZhoneGponOltStatisticsDownstreamTmQ7DroppedPkts_Type = Counter64
_ZhoneGponOltStatisticsDownstreamTmQ7DroppedPkts_Object = MibTableColumn
zhoneGponOltStatisticsDownstreamTmQ7DroppedPkts = _ZhoneGponOltStatisticsDownstreamTmQ7DroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 43),
    _ZhoneGponOltStatisticsDownstreamTmQ7DroppedPkts_Type()
)
zhoneGponOltStatisticsDownstreamTmQ7DroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsDownstreamTmQ7DroppedPkts.setStatus("current")
_ZhoneGponOltStatisticsUpstreamTmDroppedCpuPkts_Type = Counter64
_ZhoneGponOltStatisticsUpstreamTmDroppedCpuPkts_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamTmDroppedCpuPkts = _ZhoneGponOltStatisticsUpstreamTmDroppedCpuPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 44),
    _ZhoneGponOltStatisticsUpstreamTmDroppedCpuPkts_Type()
)
zhoneGponOltStatisticsUpstreamTmDroppedCpuPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamTmDroppedCpuPkts.setStatus("current")
_ZhoneGponOltStatisticsUpstreamTmDroppedPktsCrcError_Type = Counter64
_ZhoneGponOltStatisticsUpstreamTmDroppedPktsCrcError_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamTmDroppedPktsCrcError = _ZhoneGponOltStatisticsUpstreamTmDroppedPktsCrcError_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 45),
    _ZhoneGponOltStatisticsUpstreamTmDroppedPktsCrcError_Type()
)
zhoneGponOltStatisticsUpstreamTmDroppedPktsCrcError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamTmDroppedPktsCrcError.setStatus("current")
_ZhoneGponOltStatisticsUpstreamTmDroppedPktsSecurity_Type = Counter64
_ZhoneGponOltStatisticsUpstreamTmDroppedPktsSecurity_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamTmDroppedPktsSecurity = _ZhoneGponOltStatisticsUpstreamTmDroppedPktsSecurity_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 46),
    _ZhoneGponOltStatisticsUpstreamTmDroppedPktsSecurity_Type()
)
zhoneGponOltStatisticsUpstreamTmDroppedPktsSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamTmDroppedPktsSecurity.setStatus("current")
_ZhoneGponOltStatisticsUpstreamTmLearnFailures_Type = Counter64
_ZhoneGponOltStatisticsUpstreamTmLearnFailures_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamTmLearnFailures = _ZhoneGponOltStatisticsUpstreamTmLearnFailures_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 47),
    _ZhoneGponOltStatisticsUpstreamTmLearnFailures_Type()
)
zhoneGponOltStatisticsUpstreamTmLearnFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamTmLearnFailures.setStatus("current")
_ZhoneGponOltStatisticsUpstreamTmQ0ValidPkts_Type = Counter64
_ZhoneGponOltStatisticsUpstreamTmQ0ValidPkts_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamTmQ0ValidPkts = _ZhoneGponOltStatisticsUpstreamTmQ0ValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 48),
    _ZhoneGponOltStatisticsUpstreamTmQ0ValidPkts_Type()
)
zhoneGponOltStatisticsUpstreamTmQ0ValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamTmQ0ValidPkts.setStatus("current")
_ZhoneGponOltStatisticsUpstreamTmQ0DroppedPkts_Type = Counter64
_ZhoneGponOltStatisticsUpstreamTmQ0DroppedPkts_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamTmQ0DroppedPkts = _ZhoneGponOltStatisticsUpstreamTmQ0DroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 49),
    _ZhoneGponOltStatisticsUpstreamTmQ0DroppedPkts_Type()
)
zhoneGponOltStatisticsUpstreamTmQ0DroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamTmQ0DroppedPkts.setStatus("current")
_ZhoneGponOltStatisticsUpstreamTmQ1ValidPkts_Type = Counter64
_ZhoneGponOltStatisticsUpstreamTmQ1ValidPkts_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamTmQ1ValidPkts = _ZhoneGponOltStatisticsUpstreamTmQ1ValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 50),
    _ZhoneGponOltStatisticsUpstreamTmQ1ValidPkts_Type()
)
zhoneGponOltStatisticsUpstreamTmQ1ValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamTmQ1ValidPkts.setStatus("current")
_ZhoneGponOltStatisticsUpstreamTmQ1DroppedPkts_Type = Counter64
_ZhoneGponOltStatisticsUpstreamTmQ1DroppedPkts_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamTmQ1DroppedPkts = _ZhoneGponOltStatisticsUpstreamTmQ1DroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 51),
    _ZhoneGponOltStatisticsUpstreamTmQ1DroppedPkts_Type()
)
zhoneGponOltStatisticsUpstreamTmQ1DroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamTmQ1DroppedPkts.setStatus("current")
_ZhoneGponOltStatisticsUpstreamTmQ2ValidPkts_Type = Counter64
_ZhoneGponOltStatisticsUpstreamTmQ2ValidPkts_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamTmQ2ValidPkts = _ZhoneGponOltStatisticsUpstreamTmQ2ValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 52),
    _ZhoneGponOltStatisticsUpstreamTmQ2ValidPkts_Type()
)
zhoneGponOltStatisticsUpstreamTmQ2ValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamTmQ2ValidPkts.setStatus("current")
_ZhoneGponOltStatisticsUpstreamTmQ2DroppedPkts_Type = Counter64
_ZhoneGponOltStatisticsUpstreamTmQ2DroppedPkts_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamTmQ2DroppedPkts = _ZhoneGponOltStatisticsUpstreamTmQ2DroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 53),
    _ZhoneGponOltStatisticsUpstreamTmQ2DroppedPkts_Type()
)
zhoneGponOltStatisticsUpstreamTmQ2DroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamTmQ2DroppedPkts.setStatus("current")
_ZhoneGponOltStatisticsUpstreamTmQ3ValidPkts_Type = Counter64
_ZhoneGponOltStatisticsUpstreamTmQ3ValidPkts_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamTmQ3ValidPkts = _ZhoneGponOltStatisticsUpstreamTmQ3ValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 54),
    _ZhoneGponOltStatisticsUpstreamTmQ3ValidPkts_Type()
)
zhoneGponOltStatisticsUpstreamTmQ3ValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamTmQ3ValidPkts.setStatus("current")
_ZhoneGponOltStatisticsUpstreamTmQ3DroppedPkts_Type = Counter64
_ZhoneGponOltStatisticsUpstreamTmQ3DroppedPkts_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamTmQ3DroppedPkts = _ZhoneGponOltStatisticsUpstreamTmQ3DroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 55),
    _ZhoneGponOltStatisticsUpstreamTmQ3DroppedPkts_Type()
)
zhoneGponOltStatisticsUpstreamTmQ3DroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamTmQ3DroppedPkts.setStatus("current")
_ZhoneGponOltStatisticsUpstreamTmQ4ValidPkts_Type = Counter64
_ZhoneGponOltStatisticsUpstreamTmQ4ValidPkts_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamTmQ4ValidPkts = _ZhoneGponOltStatisticsUpstreamTmQ4ValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 56),
    _ZhoneGponOltStatisticsUpstreamTmQ4ValidPkts_Type()
)
zhoneGponOltStatisticsUpstreamTmQ4ValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamTmQ4ValidPkts.setStatus("current")
_ZhoneGponOltStatisticsUpstreamTmQ4DroppedPkts_Type = Counter64
_ZhoneGponOltStatisticsUpstreamTmQ4DroppedPkts_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamTmQ4DroppedPkts = _ZhoneGponOltStatisticsUpstreamTmQ4DroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 57),
    _ZhoneGponOltStatisticsUpstreamTmQ4DroppedPkts_Type()
)
zhoneGponOltStatisticsUpstreamTmQ4DroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamTmQ4DroppedPkts.setStatus("current")
_ZhoneGponOltStatisticsUpstreamTmQ5ValidPkts_Type = Counter64
_ZhoneGponOltStatisticsUpstreamTmQ5ValidPkts_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamTmQ5ValidPkts = _ZhoneGponOltStatisticsUpstreamTmQ5ValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 58),
    _ZhoneGponOltStatisticsUpstreamTmQ5ValidPkts_Type()
)
zhoneGponOltStatisticsUpstreamTmQ5ValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamTmQ5ValidPkts.setStatus("current")
_ZhoneGponOltStatisticsUpstreamTmQ5DroppedPkts_Type = Counter64
_ZhoneGponOltStatisticsUpstreamTmQ5DroppedPkts_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamTmQ5DroppedPkts = _ZhoneGponOltStatisticsUpstreamTmQ5DroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 59),
    _ZhoneGponOltStatisticsUpstreamTmQ5DroppedPkts_Type()
)
zhoneGponOltStatisticsUpstreamTmQ5DroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamTmQ5DroppedPkts.setStatus("current")
_ZhoneGponOltStatisticsUpstreamTmQ6ValidPkts_Type = Counter64
_ZhoneGponOltStatisticsUpstreamTmQ6ValidPkts_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamTmQ6ValidPkts = _ZhoneGponOltStatisticsUpstreamTmQ6ValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 60),
    _ZhoneGponOltStatisticsUpstreamTmQ6ValidPkts_Type()
)
zhoneGponOltStatisticsUpstreamTmQ6ValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamTmQ6ValidPkts.setStatus("current")
_ZhoneGponOltStatisticsUpstreamTmQ6DroppedPkts_Type = Counter64
_ZhoneGponOltStatisticsUpstreamTmQ6DroppedPkts_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamTmQ6DroppedPkts = _ZhoneGponOltStatisticsUpstreamTmQ6DroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 61),
    _ZhoneGponOltStatisticsUpstreamTmQ6DroppedPkts_Type()
)
zhoneGponOltStatisticsUpstreamTmQ6DroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamTmQ6DroppedPkts.setStatus("current")
_ZhoneGponOltStatisticsUpstreamTmQ7ValidPkts_Type = Counter64
_ZhoneGponOltStatisticsUpstreamTmQ7ValidPkts_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamTmQ7ValidPkts = _ZhoneGponOltStatisticsUpstreamTmQ7ValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 62),
    _ZhoneGponOltStatisticsUpstreamTmQ7ValidPkts_Type()
)
zhoneGponOltStatisticsUpstreamTmQ7ValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamTmQ7ValidPkts.setStatus("current")
_ZhoneGponOltStatisticsUpstreamTmQ7DroppedPkts_Type = Counter64
_ZhoneGponOltStatisticsUpstreamTmQ7DroppedPkts_Object = MibTableColumn
zhoneGponOltStatisticsUpstreamTmQ7DroppedPkts = _ZhoneGponOltStatisticsUpstreamTmQ7DroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 63),
    _ZhoneGponOltStatisticsUpstreamTmQ7DroppedPkts_Type()
)
zhoneGponOltStatisticsUpstreamTmQ7DroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsUpstreamTmQ7DroppedPkts.setStatus("current")
_ZhoneGponOltStatisticsClearStats_Type = TruthValue
_ZhoneGponOltStatisticsClearStats_Object = MibTableColumn
zhoneGponOltStatisticsClearStats = _ZhoneGponOltStatisticsClearStats_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 24, 1, 64),
    _ZhoneGponOltStatisticsClearStats_Type()
)
zhoneGponOltStatisticsClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsClearStats.setStatus("current")
_ZhoneGponUpstreamOntStatisticsTable_Object = MibTable
zhoneGponUpstreamOntStatisticsTable = _ZhoneGponUpstreamOntStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 25)
)
if mibBuilder.loadTexts:
    zhoneGponUpstreamOntStatisticsTable.setStatus("current")
_ZhoneGponUpstreamOntStatisticsEntry_Object = MibTableRow
zhoneGponUpstreamOntStatisticsEntry = _ZhoneGponUpstreamOntStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 25, 1)
)
zhoneGponUpstreamOntStatisticsEntry.setIndexNames(
    (0, "Zhone-GPON-MIB", "zhoneGponOltOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zhoneGponUpstreamOntStatisticsEntry.setStatus("current")
_ZhoneGponUpstreamOntStatisticsUpstreamBipErrors_Type = Counter64
_ZhoneGponUpstreamOntStatisticsUpstreamBipErrors_Object = MibTableColumn
zhoneGponUpstreamOntStatisticsUpstreamBipErrors = _ZhoneGponUpstreamOntStatisticsUpstreamBipErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 25, 1, 1),
    _ZhoneGponUpstreamOntStatisticsUpstreamBipErrors_Type()
)
zhoneGponUpstreamOntStatisticsUpstreamBipErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponUpstreamOntStatisticsUpstreamBipErrors.setStatus("current")
_ZhoneGponUpstreamOntStatisticsFecCorrectedBytes_Type = Counter64
_ZhoneGponUpstreamOntStatisticsFecCorrectedBytes_Object = MibTableColumn
zhoneGponUpstreamOntStatisticsFecCorrectedBytes = _ZhoneGponUpstreamOntStatisticsFecCorrectedBytes_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 25, 1, 2),
    _ZhoneGponUpstreamOntStatisticsFecCorrectedBytes_Type()
)
zhoneGponUpstreamOntStatisticsFecCorrectedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponUpstreamOntStatisticsFecCorrectedBytes.setStatus("current")
_ZhoneGponUpstreamOntStatisticsFecCorrectedCodewords_Type = Counter64
_ZhoneGponUpstreamOntStatisticsFecCorrectedCodewords_Object = MibTableColumn
zhoneGponUpstreamOntStatisticsFecCorrectedCodewords = _ZhoneGponUpstreamOntStatisticsFecCorrectedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 25, 1, 3),
    _ZhoneGponUpstreamOntStatisticsFecCorrectedCodewords_Type()
)
zhoneGponUpstreamOntStatisticsFecCorrectedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponUpstreamOntStatisticsFecCorrectedCodewords.setStatus("current")
_ZhoneGponUpstreamOntStatisticsFecUncorrectedCodewords_Type = Counter64
_ZhoneGponUpstreamOntStatisticsFecUncorrectedCodewords_Object = MibTableColumn
zhoneGponUpstreamOntStatisticsFecUncorrectedCodewords = _ZhoneGponUpstreamOntStatisticsFecUncorrectedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 25, 1, 4),
    _ZhoneGponUpstreamOntStatisticsFecUncorrectedCodewords_Type()
)
zhoneGponUpstreamOntStatisticsFecUncorrectedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponUpstreamOntStatisticsFecUncorrectedCodewords.setStatus("current")
_ZhoneGponUpstreamOntStatisticsTotalRxCodewords_Type = Counter64
_ZhoneGponUpstreamOntStatisticsTotalRxCodewords_Object = MibTableColumn
zhoneGponUpstreamOntStatisticsTotalRxCodewords = _ZhoneGponUpstreamOntStatisticsTotalRxCodewords_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 25, 1, 5),
    _ZhoneGponUpstreamOntStatisticsTotalRxCodewords_Type()
)
zhoneGponUpstreamOntStatisticsTotalRxCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponUpstreamOntStatisticsTotalRxCodewords.setStatus("current")
_ZhoneGponUpstreamOntStatisticsUnreceivedBursts_Type = Counter64
_ZhoneGponUpstreamOntStatisticsUnreceivedBursts_Object = MibTableColumn
zhoneGponUpstreamOntStatisticsUnreceivedBursts = _ZhoneGponUpstreamOntStatisticsUnreceivedBursts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 25, 1, 6),
    _ZhoneGponUpstreamOntStatisticsUnreceivedBursts_Type()
)
zhoneGponUpstreamOntStatisticsUnreceivedBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponUpstreamOntStatisticsUnreceivedBursts.setStatus("current")
_ZhoneGponUpstreamOntStatisticsBipErrors_Type = Counter64
_ZhoneGponUpstreamOntStatisticsBipErrors_Object = MibTableColumn
zhoneGponUpstreamOntStatisticsBipErrors = _ZhoneGponUpstreamOntStatisticsBipErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 25, 1, 7),
    _ZhoneGponUpstreamOntStatisticsBipErrors_Type()
)
zhoneGponUpstreamOntStatisticsBipErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponUpstreamOntStatisticsBipErrors.setStatus("current")
_ZhoneGponUpstreamOntStatisticsRemoteBipErrors_Type = Counter64
_ZhoneGponUpstreamOntStatisticsRemoteBipErrors_Object = MibTableColumn
zhoneGponUpstreamOntStatisticsRemoteBipErrors = _ZhoneGponUpstreamOntStatisticsRemoteBipErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 25, 1, 8),
    _ZhoneGponUpstreamOntStatisticsRemoteBipErrors_Type()
)
zhoneGponUpstreamOntStatisticsRemoteBipErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponUpstreamOntStatisticsRemoteBipErrors.setStatus("current")
_ZhoneGponUpstreamOntStatisticsDriftOfWindowIndications_Type = Counter64
_ZhoneGponUpstreamOntStatisticsDriftOfWindowIndications_Object = MibTableColumn
zhoneGponUpstreamOntStatisticsDriftOfWindowIndications = _ZhoneGponUpstreamOntStatisticsDriftOfWindowIndications_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 25, 1, 9),
    _ZhoneGponUpstreamOntStatisticsDriftOfWindowIndications_Type()
)
zhoneGponUpstreamOntStatisticsDriftOfWindowIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponUpstreamOntStatisticsDriftOfWindowIndications.setStatus("current")
_ZhoneGponUpstreamOntStatisticsMessageErrorMessage_Type = Counter64
_ZhoneGponUpstreamOntStatisticsMessageErrorMessage_Object = MibTableColumn
zhoneGponUpstreamOntStatisticsMessageErrorMessage = _ZhoneGponUpstreamOntStatisticsMessageErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 25, 1, 10),
    _ZhoneGponUpstreamOntStatisticsMessageErrorMessage_Type()
)
zhoneGponUpstreamOntStatisticsMessageErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneGponUpstreamOntStatisticsMessageErrorMessage.setStatus("current")
_ZhoneGponUpstreamOntStatisticsClearStats_Type = TruthValue
_ZhoneGponUpstreamOntStatisticsClearStats_Object = MibTableColumn
zhoneGponUpstreamOntStatisticsClearStats = _ZhoneGponUpstreamOntStatisticsClearStats_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 25, 1, 11),
    _ZhoneGponUpstreamOntStatisticsClearStats_Type()
)
zhoneGponUpstreamOntStatisticsClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneGponUpstreamOntStatisticsClearStats.setStatus("current")

# Managed Objects groups

zhoneGponOltConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 10)
)
zhoneGponOltConfigGroup.setObjects(
      *(("Zhone-GPON-MIB", "zhoneGponOltConfigMaxRtPropagationDelay"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigMaxOnuResponseTime"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigPreassignedEqD"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigLosAlpha"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigLofAlpha"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigLoamAlpha"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigScrambler"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigFecMode"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigAutoLearn"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigPowerLevel"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigGuardBitCount"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigDbaMode"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigGemBlockSize"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigUsBerInterval"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigDsBerInterval"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigBerSfThreshold"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigBerSdThreshold"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigFecRequest"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigKeyExchange"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigMinRtPropagationDelay"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigMinOnuResponseTime"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigEqDMeasureCycles"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigDriftControlInterval"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigDriftControlLimit"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigAllocCycleLength"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigMinUsAlloc"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigAckTimeout"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigPlsMaxAllocSize"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigDbaCycle"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigSrDbaReportingBlockSize"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigProtectionSwitchoverTimer"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigPreambleOverride"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigPreambleType0"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigPreambleType1"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigPreambleType3PreRange"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigPreambleType3PostRange"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigPreambleType3Pattern"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigBipErrorMonitoring"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigBipErrorsPerSampleThreshold"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigBipErroredSamplesThreshold"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigBipMaxSampleGap"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigRogueOnuDetectFrequency"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigRogueOnuRxPowerThreshold"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfigRogueOnuDetection"))
)
if mibBuilder.loadTexts:
    zhoneGponOltConfigGroup.setStatus("current")

zhoneGponOnuConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 11)
)
zhoneGponOnuConfigGroup.setObjects(
      *(("Zhone-GPON-MIB", "zhoneGponOltOnuConfigSerialNoVendorId"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigSerialNoVendorSpecific"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigPassword"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigAutoLearn"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigPowerLevel"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigUsBerInterval"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigDsBerInterval"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigOnuAdded"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigOmciFileName"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigMEProfileName"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigGenericProfileName"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigPhysicalTraps"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigOntTraps"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigLineStatusTraps"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigAutoUpgrade"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigSerialNoVendorSpecificFsan"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigUseRegId"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigModel"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigOntVersion"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigImageVersionActive"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigImageVersionStandby"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigUsRxPowerMonitoring"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigUsRxPowerHighThreshold"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigUsRxPowerLowThreshold"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigDbaStatusReporting"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigOmciDataSync"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigSnmpDataSync"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigNextAvailableGemPort"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigAutoConfigState"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigLinkStatusAlarmSeverity"))
)
if mibBuilder.loadTexts:
    zhoneGponOnuConfigGroup.setStatus("current")

zhoneGponPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 12)
)
zhoneGponPortConfigGroup.setObjects(
      *(("Zhone-GPON-MIB", "zhoneGponPortConfigRowStatus"),
        ("Zhone-GPON-MIB", "zhoneGponPortConfigMulticast"),
        ("Zhone-GPON-MIB", "zhoneGponPortConfigEncrypted"),
        ("Zhone-GPON-MIB", "zhoneGponPortConfigDirection"),
        ("Zhone-GPON-MIB", "zhoneGponPortConfigTrafficProfile"),
        ("Zhone-GPON-MIB", "zhoneGponPortConfigRowShelf"),
        ("Zhone-GPON-MIB", "zhoneGponPortConfigRowSlot"),
        ("Zhone-GPON-MIB", "zhoneGponPortConfigRowOlt"),
        ("Zhone-GPON-MIB", "zhoneGponPortConfigRowPort"),
        ("Zhone-GPON-MIB", "zhoneGponPortConfigRowTrafficProfile"),
        ("Zhone-GPON-MIB", "zhoneGponPortConfigRowOnuId"),
        ("Zhone-GPON-MIB", "zhoneGponPortConfigTrafficManagementProfileIndex"))
)
if mibBuilder.loadTexts:
    zhoneGponPortConfigGroup.setStatus("current")

zhoneGponAllocIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 13)
)
zhoneGponAllocIdGroup.setObjects(
      *(("Zhone-GPON-MIB", "zhoneGponAllocIdRowStatus"),
        ("Zhone-GPON-MIB", "zhoneGponAllocIdOnuId"),
        ("Zhone-GPON-MIB", "zhoneGponAllocIdGuaranteedBw"),
        ("Zhone-GPON-MIB", "zhoneGponAllocIdTrafficClass"),
        ("Zhone-GPON-MIB", "zhoneGponAllocIdCompensated"))
)
if mibBuilder.loadTexts:
    zhoneGponAllocIdGroup.setStatus("current")

zhoneGponSerialNoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 14)
)
zhoneGponSerialNoGroup.setObjects(
      *(("Zhone-GPON-MIB", "zhoneGponSerialNoVendorId"),
        ("Zhone-GPON-MIB", "zhoneGponSerialNoVendorSpecific"),
        ("Zhone-GPON-MIB", "zhoneGponSerialNoTimeStamp"))
)
if mibBuilder.loadTexts:
    zhoneGponSerialNoGroup.setStatus("current")

zhoneGponOnuStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 15)
)
zhoneGponOnuStatusGroup.setObjects(
      *(("Zhone-GPON-MIB", "zhoneGponOnuStatusWord"),
        ("Zhone-GPON-MIB", "zhoneGponOnuOmciState"),
        ("Zhone-GPON-MIB", "zhoneGponOnuOpticRssi"),
        ("Zhone-GPON-MIB", "zhoneGponOntRxPower"),
        ("Zhone-GPON-MIB", "zhoneGponOntVersion"))
)
if mibBuilder.loadTexts:
    zhoneGponOnuStatusGroup.setStatus("current")

zhoneOnuOmciMeProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 16)
)
zhoneOnuOmciMeProfileGroup.setObjects(
      *(("Zhone-GPON-MIB", "zhoneOnuOmciMEProfileRowStatus"),
        ("Zhone-GPON-MIB", "zhoneOnuOmciMEProfileName"),
        ("Zhone-GPON-MIB", "zhoneOnuOmciMEProfileOmciCommands"),
        ("Zhone-GPON-MIB", "zhoneOnuOmciMEProfileFileName"))
)
if mibBuilder.loadTexts:
    zhoneOnuOmciMeProfileGroup.setStatus("current")

zhoneOnuOmciGenericProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 17)
)
zhoneOnuOmciGenericProfileGroup.setObjects(
      *(("Zhone-GPON-MIB", "zhoneOnuOmciGenericProfileRowStatus"),
        ("Zhone-GPON-MIB", "zhoneOnuOmciGenericProfileName"),
        ("Zhone-GPON-MIB", "zhoneOnuOmciGenericProfileOmciCommands"),
        ("Zhone-GPON-MIB", "zhoneOnuOmciGenericProfileFileName"),
        ("Zhone-GPON-MIB", "zhoneOnuOmciGenericProfileMESrcProfileName"))
)
if mibBuilder.loadTexts:
    zhoneOnuOmciGenericProfileGroup.setStatus("current")

zhoneOnuOmciSpecificProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 18)
)
zhoneOnuOmciSpecificProfileGroup.setObjects(
      *(("Zhone-GPON-MIB", "zhoneOnuOmciSpecificProfileRowStatus"),
        ("Zhone-GPON-MIB", "zhoneOnuOmciSpecificProfileOmciCommands"),
        ("Zhone-GPON-MIB", "zhoneOnuOmciSpecificProfileMESrcProfileName"),
        ("Zhone-GPON-MIB", "zhoneOnuOmciSpecificProfileFileName"))
)
if mibBuilder.loadTexts:
    zhoneOnuOmciSpecificProfileGroup.setStatus("current")

zhoneGponOmciOnuAlarmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 19)
)
zhoneGponOmciOnuAlarmsGroup.setObjects(
      *(("Zhone-GPON-MIB", "zhoneGponOmciOnuAlarmsText"),
        ("Zhone-GPON-MIB", "zhoneGponOmciStatsCurrentText"),
        ("Zhone-GPON-MIB", "zhoneGponOmciStatsPreviousText"))
)
if mibBuilder.loadTexts:
    zhoneGponOmciOnuAlarmsGroup.setStatus("current")

zhoneGponTrafficProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 21)
)
zhoneGponTrafficProfileGroup.setObjects(
      *(("Zhone-GPON-MIB", "zhoneGponTrafficProfileRowStatus"),
        ("Zhone-GPON-MIB", "zhoneGponTrafficProfileClass"),
        ("Zhone-GPON-MIB", "zhoneGponTrafficProfileDbaEnabled"),
        ("Zhone-GPON-MIB", "zhoneGponTrafficProfileExtraUsBwType"),
        ("Zhone-GPON-MIB", "zhoneGponTrafficProfileMaxUsBw"),
        ("Zhone-GPON-MIB", "zhoneGponTrafficProfileDbaAssuredUsBw"),
        ("Zhone-GPON-MIB", "zhoneGponTrafficProfileDbaFixedUsCbrBw"),
        ("Zhone-GPON-MIB", "zhoneGponTrafficProfileDbaFixedUsUbrBw"),
        ("Zhone-GPON-MIB", "zhoneGponTrafficProfileCompensated"),
        ("Zhone-GPON-MIB", "zhoneGponTrafficProfileGuaranteedUpstreamBw"),
        ("Zhone-GPON-MIB", "zhoneGponTrafficProfileShared"))
)
if mibBuilder.loadTexts:
    zhoneGponTrafficProfileGroup.setStatus("current")

zhoneGponPortStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 22)
)
zhoneGponPortStatusGroup.setObjects(
      *(("Zhone-GPON-MIB", "zhoneGponPortStatusAllocId"),
        ("Zhone-GPON-MIB", "zhoneGponPortStatusDbaStatus"))
)
if mibBuilder.loadTexts:
    zhoneGponPortStatusGroup.setStatus("current")

zhoneGponOmciStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 24)
)
zhoneGponOmciStatusGroup.setObjects(
      *(("Zhone-GPON-MIB", "zhoneGponOmciStatusText"),
        ("Zhone-GPON-MIB", "zhoneGponOnuDistance"))
)
if mibBuilder.loadTexts:
    zhoneGponOmciStatusGroup.setStatus("current")

zhoneGponOmciOnuRebootGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 25)
)
zhoneGponOmciOnuRebootGroup.setObjects(
    ("Zhone-GPON-MIB", "zhoneGponOmciOnuReboot")
)
if mibBuilder.loadTexts:
    zhoneGponOmciOnuRebootGroup.setStatus("current")

zhoneGponOmciOnuPortAdminGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 26)
)
zhoneGponOmciOnuPortAdminGroup.setObjects(
      *(("Zhone-GPON-MIB", "zhoneGponOmciOnuPortAdminState"),
        ("Zhone-GPON-MIB", "zhoneGponOmciOnuPortAdminAutoDetect"))
)
if mibBuilder.loadTexts:
    zhoneGponOmciOnuPortAdminGroup.setStatus("current")

zhoneGponOmciOnuImageUpgradeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 27)
)
zhoneGponOmciOnuImageUpgradeGroup.setObjects(
      *(("Zhone-GPON-MIB", "zhoneGponOmciOnuPortAdminState"),
        ("Zhone-GPON-MIB", "zhoneGponOmciOnuImageUpgradeAction"),
        ("Zhone-GPON-MIB", "zhoneOnuOmciImageUpgradeFilename"),
        ("Zhone-GPON-MIB", "zhoneGponOmciOnuImageUpgradePartition"),
        ("Zhone-GPON-MIB", "zhoneOnuOmciImageUpgradeImageVersionPartition0"),
        ("Zhone-GPON-MIB", "zhoneOnuOmciImageUpgradeImageVersionPartition1"),
        ("Zhone-GPON-MIB", "zhoneOnuOmciImageUpgradeIsCommittedPartition0"),
        ("Zhone-GPON-MIB", "zhoneOnuOmciImageUpgradeIsCommittedPartition1"),
        ("Zhone-GPON-MIB", "zhoneOnuOmciImageUpgradeIsActivatedPartition0"),
        ("Zhone-GPON-MIB", "zhoneOnuOmciImageUpgradeIsActivatedPartition1"),
        ("Zhone-GPON-MIB", "zhoneOnuOmciImageUpgradeIsValidPartition0"),
        ("Zhone-GPON-MIB", "zhoneOnuOmciImageUpgradeIsValidPartition1"),
        ("Zhone-GPON-MIB", "zhoneOnuOmciImageUpgradeDownloadStatus"),
        ("Zhone-GPON-MIB", "zhoneGponUpgradeModel"),
        ("Zhone-GPON-MIB", "zhoneGponUpgradeStartTime"),
        ("Zhone-GPON-MIB", "zhoneGponUpgradeIfIndex"),
        ("Zhone-GPON-MIB", "zhoneGponUpgradeByStateOnuState"),
        ("Zhone-GPON-MIB", "zhoneGponOmciOnuImageUpgradeModel"),
        ("Zhone-GPON-MIB", "zhoneGponOmciOnuImageUpgradeStartTime"),
        ("Zhone-GPON-MIB", "zhoneGponOmciOnuImageUpgradeWillBeActivated"),
        ("Zhone-GPON-MIB", "zhoneGponOmciOnuImageUpgradeWillBeCommitted"),
        ("Zhone-GPON-MIB", "zhoneGponUpgradeByStateWillBeActivated"),
        ("Zhone-GPON-MIB", "zhoneGponUpgradeByStateWillBeCommitted"),
        ("Zhone-GPON-MIB", "zhoneGponUpgradeProgressPercentage"),
        ("Zhone-GPON-MIB", "zhoneGponOmciOnuImageDownloadProgressPercentage"),
        ("Zhone-GPON-MIB", "zhoneGponOmciOnuImageUpgradeMethod"),
        ("Zhone-GPON-MIB", "zhoneGponUpgradeByStateMethod"),
        ("Zhone-GPON-MIB", "zhoneGponUpgradeByStatePartition"),
        ("Zhone-GPON-MIB", "zhoneGponOmciOnuImageUpgradeType"),
        ("Zhone-GPON-MIB", "zhoneGponUpgradeByStateUpgradeType"))
)
if mibBuilder.loadTexts:
    zhoneGponOmciOnuImageUpgradeGroup.setStatus("current")

zhoneGponOltStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 28)
)
zhoneGponOltStatusGroup.setObjects(
      *(("Zhone-GPON-MIB", "zhoneGponOltOpticTemperature"),
        ("Zhone-GPON-MIB", "zhoneGponOltOpticVoltage"),
        ("Zhone-GPON-MIB", "zhoneGponOltOpticTxBiasCurrent"),
        ("Zhone-GPON-MIB", "zhoneGponOltOpticTxPower"),
        ("Zhone-GPON-MIB", "zhoneGponOltOpticStatus"),
        ("Zhone-GPON-MIB", "zhoneGponOltOpticAlarms"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatusWord"),
        ("Zhone-GPON-MIB", "zhoneGponOltConfiguredOnuCount"),
        ("Zhone-GPON-MIB", "zhoneGponOltActiveOnuCount"))
)
if mibBuilder.loadTexts:
    zhoneGponOltStatusGroup.setStatus("current")

zhoneGponeOltDbaStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 29)
)
zhoneGponeOltDbaStatusGroup.setObjects(
      *(("Zhone-GPON-MIB", "zhoneGponOltDbaTotalAvailableBw"),
        ("Zhone-GPON-MIB", "zhoneGponOltDbaTotalAvailableCompensatedCbrBw"),
        ("Zhone-GPON-MIB", "zhoneGponOltDbaAllocatedUbrBw"),
        ("Zhone-GPON-MIB", "zhoneGponOltDbaAllocatedCbrBw"),
        ("Zhone-GPON-MIB", "zhoneGponOltDbaAllocatedCompensatedCbrBw"),
        ("Zhone-GPON-MIB", "zhoneGponOltDbaAllocatedAssuredBw"),
        ("Zhone-GPON-MIB", "zhoneGponOltDbaAllocatedNonAssuredBw"),
        ("Zhone-GPON-MIB", "zhoneGponOltDbaAllocatedBestEffortBw"),
        ("Zhone-GPON-MIB", "zhoneGponOltDbaMaxAllocIds"),
        ("Zhone-GPON-MIB", "zhoneGponOltDbaAvailAllocIds"),
        ("Zhone-GPON-MIB", "zhoneGponOltDbaUsedAllocIds"),
        ("Zhone-GPON-MIB", "zhoneGponOltDbaMaxDbaAllocIds"),
        ("Zhone-GPON-MIB", "zhoneGponOltDbaAvailDbaAllocIds"),
        ("Zhone-GPON-MIB", "zhoneGponOltDbaUsedDbaAllocIds"),
        ("Zhone-GPON-MIB", "zhoneGponOltDbaTotalOltGemPorts"),
        ("Zhone-GPON-MIB", "zhoneGponOltDbaLastCacRc"))
)
if mibBuilder.loadTexts:
    zhoneGponeOltDbaStatusGroup.setStatus("current")

zhoneGponCmdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 31)
)
zhoneGponCmdGroup.setObjects(
      *(("Zhone-GPON-MIB", "zhoneGponCmdOperation"),
        ("Zhone-GPON-MIB", "zhoneGponCmdSlot"),
        ("Zhone-GPON-MIB", "zhoneGponCmdOlt"),
        ("Zhone-GPON-MIB", "zhoneGponCmdOnu"),
        ("Zhone-GPON-MIB", "zhoneGponCmdFilterMask"),
        ("Zhone-GPON-MIB", "zhoneGponCmdShelf"))
)
if mibBuilder.loadTexts:
    zhoneGponCmdGroup.setStatus("current")

zhoneGponOltStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 32)
)
zhoneGponOltStatisticsGroup.setObjects(
      *(("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamValidGemFrames"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamDiscardedFrames"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamGemFrames"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamOmciFrames"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamPloamFrames"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamIdlePloamFrames"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamValidGemFrames"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamDiscardedFrames"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamGemFrames"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamOmciFrames"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamPloamFrames"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamPonValidEthernetPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamPonCpuPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamTxBytes"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamPonValidNotIdlePloams"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamPonErrorPloams"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamPonInvalidPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamDroppedPktsInactivePorts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamDroppedPloamsFifoFull"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamTmValidPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamTmCrcPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamTmDroppedCpuPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamTmMacLookupMiss"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamTmPktsForwardedFromHmToPon"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamTmPktsDroppedGemPidNotEnabled"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamTmQ0ValidPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamTmQ0DroppedPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamTmQ1ValidPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamTmQ1DroppedPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamTmQ2ValidPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamTmQ2DroppedPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamTmQ3ValidPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamTmQ3DroppedPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamTmQ4ValidPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamTmQ4DroppedPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamTmQ5ValidPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamTmQ5DroppedPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamTmQ6ValidPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamTmQ6DroppedPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamTmQ7ValidPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamTmQ7DroppedPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamTmDroppedCpuPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamTmDroppedPktsCrcError"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamTmDroppedPktsSecurity"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamTmLearnFailures"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamTmQ0ValidPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamTmQ0DroppedPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamTmQ1ValidPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamTmQ1DroppedPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamTmQ2ValidPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamTmQ2DroppedPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamTmQ3ValidPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamTmQ3DroppedPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamTmQ4ValidPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamTmQ4DroppedPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamTmQ5ValidPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamTmQ5DroppedPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamTmQ6ValidPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamTmQ6DroppedPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamTmQ7ValidPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamTmQ7DroppedPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsUpstreamPonValidPkts"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatisticsClearStats"))
)
if mibBuilder.loadTexts:
    zhoneGponOltStatisticsGroup.setStatus("current")

zhoneGponUpstreamOntStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 33)
)
zhoneGponUpstreamOntStatisticsGroup.setObjects(
      *(("Zhone-GPON-MIB", "zhoneGponUpstreamOntStatisticsUpstreamBipErrors"),
        ("Zhone-GPON-MIB", "zhoneGponUpstreamOntStatisticsFecCorrectedBytes"),
        ("Zhone-GPON-MIB", "zhoneGponUpstreamOntStatisticsFecCorrectedCodewords"),
        ("Zhone-GPON-MIB", "zhoneGponUpstreamOntStatisticsFecUncorrectedCodewords"),
        ("Zhone-GPON-MIB", "zhoneGponUpstreamOntStatisticsTotalRxCodewords"),
        ("Zhone-GPON-MIB", "zhoneGponUpstreamOntStatisticsUnreceivedBursts"),
        ("Zhone-GPON-MIB", "zhoneGponUpstreamOntStatisticsBipErrors"),
        ("Zhone-GPON-MIB", "zhoneGponUpstreamOntStatisticsRemoteBipErrors"),
        ("Zhone-GPON-MIB", "zhoneGponUpstreamOntStatisticsDriftOfWindowIndications"),
        ("Zhone-GPON-MIB", "zhoneGponUpstreamOntStatisticsMessageErrorMessage"),
        ("Zhone-GPON-MIB", "zhoneGponUpstreamOntStatisticsClearStats"))
)
if mibBuilder.loadTexts:
    zhoneGponUpstreamOntStatisticsGroup.setStatus("current")

zhoneGponDeprecated = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 34)
)
zhoneGponDeprecated.setObjects(
    ("Zhone-GPON-MIB", "zhoneGponOltStatisticsDownstreamIdlePloamFrames")
)
if mibBuilder.loadTexts:
    zhoneGponDeprecated.setStatus("deprecated")


# Notification objects

zhoneGponSerialNumberFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 6, 0, 1)
)
zhoneGponSerialNumberFound.setObjects(
      *(("Zhone-GPON-MIB", "zhoneGponSerialNoVendorId"),
        ("Zhone-GPON-MIB", "zhoneGponSerialNoVendorSpecific"))
)
if mibBuilder.loadTexts:
    zhoneGponSerialNumberFound.setStatus(
        "current"
    )

zhoneGponSerialNumberLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 6, 0, 2)
)
zhoneGponSerialNumberLost.setObjects(
      *(("Zhone-GPON-MIB", "zhoneGponSerialNoVendorId"),
        ("Zhone-GPON-MIB", "zhoneGponSerialNoVendorSpecific"))
)
if mibBuilder.loadTexts:
    zhoneGponSerialNumberLost.setStatus(
        "current"
    )

zhoneGponOnuLineStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 6, 0, 3)
)
zhoneGponOnuLineStatusChange.setObjects(
    ("Zhone-GPON-MIB", "zhoneGponOnuStatusWord")
)
if mibBuilder.loadTexts:
    zhoneGponOnuLineStatusChange.setStatus(
        "current"
    )

zhoneGponOmciOnuAlarmsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 6, 0, 4)
)
zhoneGponOmciOnuAlarmsTrap.setObjects(
    ("Zhone-GPON-MIB", "zhoneGponOmciOnuAlarmsText")
)
if mibBuilder.loadTexts:
    zhoneGponOmciOnuAlarmsTrap.setStatus(
        "current"
    )

zhoneGponOmciOnuDownloadStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 6, 0, 5)
)
zhoneGponOmciOnuDownloadStatusChange.setObjects(
    ("Zhone-GPON-MIB", "zhoneOnuOmciImageUpgradeDownloadStatus")
)
if mibBuilder.loadTexts:
    zhoneGponOmciOnuDownloadStatusChange.setStatus(
        "current"
    )

zhoneGponOltOpticsAlarmsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 6, 0, 6)
)
zhoneGponOltOpticsAlarmsTrap.setObjects(
    ("Zhone-GPON-MIB", "zhoneGponOltOpticAlarms")
)
if mibBuilder.loadTexts:
    zhoneGponOltOpticsAlarmsTrap.setStatus(
        "current"
    )

zhoneGponOnuError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 6, 0, 7)
)
zhoneGponOnuError.setObjects(
    ("Zhone-GPON-MIB", "zhoneGponOnuStatusWord")
)
if mibBuilder.loadTexts:
    zhoneGponOnuError.setStatus(
        "current"
    )

zhoneGponRogueOnuTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 6, 0, 8)
)
zhoneGponRogueOnuTrap.setObjects(
    ("Zhone-GPON-MIB", "zhoneGponOltStatusWord")
)
if mibBuilder.loadTexts:
    zhoneGponRogueOnuTrap.setStatus(
        "current"
    )

zhoneGponRssiRogueOnuTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 6, 0, 9)
)
zhoneGponRssiRogueOnuTrap.setObjects(
    ("Zhone-GPON-MIB", "zhoneGponOltStatusWord")
)
if mibBuilder.loadTexts:
    zhoneGponRssiRogueOnuTrap.setStatus(
        "current"
    )

zhoneGponOltStatusWordTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 6, 0, 10)
)
zhoneGponOltStatusWordTrap.setObjects(
    ("Zhone-GPON-MIB", "zhoneGponOltStatusWord")
)
if mibBuilder.loadTexts:
    zhoneGponOltStatusWordTrap.setStatus(
        "current"
    )

zhoneGponOnuAutoAssign = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 14, 1, 6, 0, 11)
)
zhoneGponOnuAutoAssign.setObjects(
      *(("Zhone-GPON-MIB", "zhoneGponSerialNoVendorId"),
        ("Zhone-GPON-MIB", "zhoneGponSerialNoVendorSpecific"),
        ("Zhone-GPON-MIB", "zhoneGponOltOnuConfigModel"))
)
if mibBuilder.loadTexts:
    zhoneGponOnuAutoAssign.setStatus(
        "current"
    )


# Notifications groups

zhoneGponTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 20)
)
zhoneGponTrapGroup.setObjects(
      *(("Zhone-GPON-MIB", "zhoneGponSerialNumberFound"),
        ("Zhone-GPON-MIB", "zhoneGponSerialNumberLost"),
        ("Zhone-GPON-MIB", "zhoneGponOnuLineStatusChange"),
        ("Zhone-GPON-MIB", "zhoneGponOmciOnuAlarmsTrap"),
        ("Zhone-GPON-MIB", "zhoneGponOmciOnuDownloadStatusChange"),
        ("Zhone-GPON-MIB", "zhoneGponOltOpticsAlarmsTrap"),
        ("Zhone-GPON-MIB", "zhoneGponOnuError"),
        ("Zhone-GPON-MIB", "zhoneGponRogueOnuTrap"),
        ("Zhone-GPON-MIB", "zhoneGponRssiRogueOnuTrap"),
        ("Zhone-GPON-MIB", "zhoneGponOltStatusWordTrap"),
        ("Zhone-GPON-MIB", "zhoneGponOnuAutoAssign"))
)
if mibBuilder.loadTexts:
    zhoneGponTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Zhone-GPON-MIB",
    **{"OnuUpgradeState": OnuUpgradeState,
       "GponCacRc": GponCacRc,
       "zhoneGponObjectID": zhoneGponObjectID,
       "zhoneGponOltConfigTable": zhoneGponOltConfigTable,
       "zhoneGponOltConfigEntry": zhoneGponOltConfigEntry,
       "zhoneGponOltIfIndex": zhoneGponOltIfIndex,
       "zhoneGponOltConfigMaxRtPropagationDelay": zhoneGponOltConfigMaxRtPropagationDelay,
       "zhoneGponOltConfigMaxOnuResponseTime": zhoneGponOltConfigMaxOnuResponseTime,
       "zhoneGponOltConfigPreassignedEqD": zhoneGponOltConfigPreassignedEqD,
       "zhoneGponOltConfigLosAlpha": zhoneGponOltConfigLosAlpha,
       "zhoneGponOltConfigLofAlpha": zhoneGponOltConfigLofAlpha,
       "zhoneGponOltConfigLoamAlpha": zhoneGponOltConfigLoamAlpha,
       "zhoneGponOltConfigScrambler": zhoneGponOltConfigScrambler,
       "zhoneGponOltConfigFecMode": zhoneGponOltConfigFecMode,
       "zhoneGponOltConfigAutoLearn": zhoneGponOltConfigAutoLearn,
       "zhoneGponOltConfigPowerLevel": zhoneGponOltConfigPowerLevel,
       "zhoneGponOltConfigGuardBitCount": zhoneGponOltConfigGuardBitCount,
       "zhoneGponOltConfigDbaMode": zhoneGponOltConfigDbaMode,
       "zhoneGponOltConfigGemBlockSize": zhoneGponOltConfigGemBlockSize,
       "zhoneGponOltConfigUsBerInterval": zhoneGponOltConfigUsBerInterval,
       "zhoneGponOltConfigDsBerInterval": zhoneGponOltConfigDsBerInterval,
       "zhoneGponOltConfigBerSfThreshold": zhoneGponOltConfigBerSfThreshold,
       "zhoneGponOltConfigBerSdThreshold": zhoneGponOltConfigBerSdThreshold,
       "zhoneGponOltConfigFecRequest": zhoneGponOltConfigFecRequest,
       "zhoneGponOltConfigKeyExchange": zhoneGponOltConfigKeyExchange,
       "zhoneGponOltConfigMinRtPropagationDelay": zhoneGponOltConfigMinRtPropagationDelay,
       "zhoneGponOltConfigMinOnuResponseTime": zhoneGponOltConfigMinOnuResponseTime,
       "zhoneGponOltConfigEqDMeasureCycles": zhoneGponOltConfigEqDMeasureCycles,
       "zhoneGponOltConfigDriftControlInterval": zhoneGponOltConfigDriftControlInterval,
       "zhoneGponOltConfigDriftControlLimit": zhoneGponOltConfigDriftControlLimit,
       "zhoneGponOltConfigAllocCycleLength": zhoneGponOltConfigAllocCycleLength,
       "zhoneGponOltConfigMinUsAlloc": zhoneGponOltConfigMinUsAlloc,
       "zhoneGponOltConfigAckTimeout": zhoneGponOltConfigAckTimeout,
       "zhoneGponOltConfigPlsMaxAllocSize": zhoneGponOltConfigPlsMaxAllocSize,
       "zhoneGponOltConfigDbaCycle": zhoneGponOltConfigDbaCycle,
       "zhoneGponOltConfigSrDbaReportingBlockSize": zhoneGponOltConfigSrDbaReportingBlockSize,
       "zhoneGponOltConfigProtectionSwitchoverTimer": zhoneGponOltConfigProtectionSwitchoverTimer,
       "zhoneGponOltConfigPreambleOverride": zhoneGponOltConfigPreambleOverride,
       "zhoneGponOltConfigPreambleType0": zhoneGponOltConfigPreambleType0,
       "zhoneGponOltConfigPreambleType1": zhoneGponOltConfigPreambleType1,
       "zhoneGponOltConfigPreambleType3PreRange": zhoneGponOltConfigPreambleType3PreRange,
       "zhoneGponOltConfigPreambleType3PostRange": zhoneGponOltConfigPreambleType3PostRange,
       "zhoneGponOltConfigPreambleType3Pattern": zhoneGponOltConfigPreambleType3Pattern,
       "zhoneGponOltConfigBipErrorMonitoring": zhoneGponOltConfigBipErrorMonitoring,
       "zhoneGponOltConfigBipErrorsPerSampleThreshold": zhoneGponOltConfigBipErrorsPerSampleThreshold,
       "zhoneGponOltConfigBipErroredSamplesThreshold": zhoneGponOltConfigBipErroredSamplesThreshold,
       "zhoneGponOltConfigBipMaxSampleGap": zhoneGponOltConfigBipMaxSampleGap,
       "zhoneGponOltConfigRogueOnuDetection": zhoneGponOltConfigRogueOnuDetection,
       "zhoneGponOltConfigRogueOnuDetectFrequency": zhoneGponOltConfigRogueOnuDetectFrequency,
       "zhoneGponOltConfigRogueOnuRxPowerThreshold": zhoneGponOltConfigRogueOnuRxPowerThreshold,
       "zhoneGponOltOnuConfigTable": zhoneGponOltOnuConfigTable,
       "zhoneGponOltOnuConfigEntry": zhoneGponOltOnuConfigEntry,
       "zhoneGponOltOnuIfIndex": zhoneGponOltOnuIfIndex,
       "zhoneGponOltOnuConfigSerialNoVendorId": zhoneGponOltOnuConfigSerialNoVendorId,
       "zhoneGponOltOnuConfigSerialNoVendorSpecific": zhoneGponOltOnuConfigSerialNoVendorSpecific,
       "zhoneGponOltOnuConfigPassword": zhoneGponOltOnuConfigPassword,
       "zhoneGponOltOnuConfigAutoLearn": zhoneGponOltOnuConfigAutoLearn,
       "zhoneGponOltOnuConfigPowerLevel": zhoneGponOltOnuConfigPowerLevel,
       "zhoneGponOltOnuConfigUsBerInterval": zhoneGponOltOnuConfigUsBerInterval,
       "zhoneGponOltOnuConfigDsBerInterval": zhoneGponOltOnuConfigDsBerInterval,
       "zhoneGponOltOnuConfigOnuAdded": zhoneGponOltOnuConfigOnuAdded,
       "zhoneGponOltOnuConfigOmciFileName": zhoneGponOltOnuConfigOmciFileName,
       "zhoneGponOltOnuConfigMEProfileName": zhoneGponOltOnuConfigMEProfileName,
       "zhoneGponOltOnuConfigGenericProfileName": zhoneGponOltOnuConfigGenericProfileName,
       "zhoneGponOltOnuConfigPhysicalTraps": zhoneGponOltOnuConfigPhysicalTraps,
       "zhoneGponOltOnuConfigOntTraps": zhoneGponOltOnuConfigOntTraps,
       "zhoneGponOltOnuConfigLineStatusTraps": zhoneGponOltOnuConfigLineStatusTraps,
       "zhoneGponOltOnuConfigAutoUpgrade": zhoneGponOltOnuConfigAutoUpgrade,
       "zhoneGponOltOnuConfigSerialNoVendorSpecificFsan": zhoneGponOltOnuConfigSerialNoVendorSpecificFsan,
       "zhoneGponOltOnuConfigUseRegId": zhoneGponOltOnuConfigUseRegId,
       "zhoneGponOltOnuConfigModel": zhoneGponOltOnuConfigModel,
       "zhoneGponOltOnuConfigOntVersion": zhoneGponOltOnuConfigOntVersion,
       "zhoneGponOltOnuConfigImageVersionActive": zhoneGponOltOnuConfigImageVersionActive,
       "zhoneGponOltOnuConfigImageVersionStandby": zhoneGponOltOnuConfigImageVersionStandby,
       "zhoneGponOltOnuConfigUsRxPowerMonitoring": zhoneGponOltOnuConfigUsRxPowerMonitoring,
       "zhoneGponOltOnuConfigUsRxPowerHighThreshold": zhoneGponOltOnuConfigUsRxPowerHighThreshold,
       "zhoneGponOltOnuConfigUsRxPowerLowThreshold": zhoneGponOltOnuConfigUsRxPowerLowThreshold,
       "zhoneGponOltOnuConfigDbaStatusReporting": zhoneGponOltOnuConfigDbaStatusReporting,
       "zhoneGponOltOnuConfigOmciDataSync": zhoneGponOltOnuConfigOmciDataSync,
       "zhoneGponOltOnuConfigSnmpDataSync": zhoneGponOltOnuConfigSnmpDataSync,
       "zhoneGponOltOnuConfigNextAvailableGemPort": zhoneGponOltOnuConfigNextAvailableGemPort,
       "zhoneGponOltOnuConfigAutoConfigState": zhoneGponOltOnuConfigAutoConfigState,
       "zhoneGponOltOnuConfigLinkStatusAlarmSeverity": zhoneGponOltOnuConfigLinkStatusAlarmSeverity,
       "zhoneGponPortConfigTable": zhoneGponPortConfigTable,
       "zhoneGponPortConfigEntry": zhoneGponPortConfigEntry,
       "zhoneGponPortIfIndex": zhoneGponPortIfIndex,
       "zhoneGponPortConfigRowStatus": zhoneGponPortConfigRowStatus,
       "zhoneGponPortConfigMulticast": zhoneGponPortConfigMulticast,
       "zhoneGponPortConfigEncrypted": zhoneGponPortConfigEncrypted,
       "zhoneGponPortConfigDirection": zhoneGponPortConfigDirection,
       "zhoneGponPortConfigTrafficProfile": zhoneGponPortConfigTrafficProfile,
       "zhoneGponPortConfigRowShelf": zhoneGponPortConfigRowShelf,
       "zhoneGponPortConfigRowSlot": zhoneGponPortConfigRowSlot,
       "zhoneGponPortConfigRowOlt": zhoneGponPortConfigRowOlt,
       "zhoneGponPortConfigRowPort": zhoneGponPortConfigRowPort,
       "zhoneGponPortConfigRowTrafficProfile": zhoneGponPortConfigRowTrafficProfile,
       "zhoneGponPortConfigRowOnuId": zhoneGponPortConfigRowOnuId,
       "zhoneGponPortConfigTrafficManagementProfileIndex": zhoneGponPortConfigTrafficManagementProfileIndex,
       "zhoneGponAllocIdTable": zhoneGponAllocIdTable,
       "zhoneGponAllocIdEntry": zhoneGponAllocIdEntry,
       "zhoneGponAllocIdIndex": zhoneGponAllocIdIndex,
       "zhoneGponAllocIdRowStatus": zhoneGponAllocIdRowStatus,
       "zhoneGponAllocIdOnuId": zhoneGponAllocIdOnuId,
       "zhoneGponAllocIdGuaranteedBw": zhoneGponAllocIdGuaranteedBw,
       "zhoneGponAllocIdTrafficClass": zhoneGponAllocIdTrafficClass,
       "zhoneGponAllocIdCompensated": zhoneGponAllocIdCompensated,
       "zhoneGponSerialNoTable": zhoneGponSerialNoTable,
       "zhoneGponSerialNoEntry": zhoneGponSerialNoEntry,
       "zhoneGponSerialNoOltLgIfIndex": zhoneGponSerialNoOltLgIfIndex,
       "zhoneGponSerialNoIndexId": zhoneGponSerialNoIndexId,
       "zhoneGponSerialNoVendorId": zhoneGponSerialNoVendorId,
       "zhoneGponSerialNoVendorSpecific": zhoneGponSerialNoVendorSpecific,
       "zhoneGponSerialNoTimeStamp": zhoneGponSerialNoTimeStamp,
       "zhoneGponTrapPrefix": zhoneGponTrapPrefix,
       "zhoneGponTraps": zhoneGponTraps,
       "zhoneGponSerialNumberFound": zhoneGponSerialNumberFound,
       "zhoneGponSerialNumberLost": zhoneGponSerialNumberLost,
       "zhoneGponOnuLineStatusChange": zhoneGponOnuLineStatusChange,
       "zhoneGponOmciOnuAlarmsTrap": zhoneGponOmciOnuAlarmsTrap,
       "zhoneGponOmciOnuDownloadStatusChange": zhoneGponOmciOnuDownloadStatusChange,
       "zhoneGponOltOpticsAlarmsTrap": zhoneGponOltOpticsAlarmsTrap,
       "zhoneGponOnuError": zhoneGponOnuError,
       "zhoneGponRogueOnuTrap": zhoneGponRogueOnuTrap,
       "zhoneGponRssiRogueOnuTrap": zhoneGponRssiRogueOnuTrap,
       "zhoneGponOltStatusWordTrap": zhoneGponOltStatusWordTrap,
       "zhoneGponOnuAutoAssign": zhoneGponOnuAutoAssign,
       "zhoneGponOnuStatusTable": zhoneGponOnuStatusTable,
       "zhoneGponOnuStatusEntry": zhoneGponOnuStatusEntry,
       "zhoneGponOnuStatusWord": zhoneGponOnuStatusWord,
       "zhoneGponOnuOmciState": zhoneGponOnuOmciState,
       "zhoneGponOnuOpticRssi": zhoneGponOnuOpticRssi,
       "zhoneGponOntRxPower": zhoneGponOntRxPower,
       "zhoneGponOntVersion": zhoneGponOntVersion,
       "zhoneGponOnuDistance": zhoneGponOnuDistance,
       "zhoneOnuOmciMEProfileTable": zhoneOnuOmciMEProfileTable,
       "zhoneOnuOmciMEProfileEntry": zhoneOnuOmciMEProfileEntry,
       "zhoneOnuOmciMEProfileIndex": zhoneOnuOmciMEProfileIndex,
       "zhoneOnuOmciMEProfileRowStatus": zhoneOnuOmciMEProfileRowStatus,
       "zhoneOnuOmciMEProfileName": zhoneOnuOmciMEProfileName,
       "zhoneOnuOmciMEProfileOmciCommands": zhoneOnuOmciMEProfileOmciCommands,
       "zhoneOnuOmciMEProfileFileName": zhoneOnuOmciMEProfileFileName,
       "zhoneOnuOmciGenericProfileTable": zhoneOnuOmciGenericProfileTable,
       "zhoneOnuOmciGenericProfileEntry": zhoneOnuOmciGenericProfileEntry,
       "zhoneOnuOmciGenericProfileIndex": zhoneOnuOmciGenericProfileIndex,
       "zhoneOnuOmciGenericProfileRowStatus": zhoneOnuOmciGenericProfileRowStatus,
       "zhoneOnuOmciGenericProfileName": zhoneOnuOmciGenericProfileName,
       "zhoneOnuOmciGenericProfileOmciCommands": zhoneOnuOmciGenericProfileOmciCommands,
       "zhoneOnuOmciGenericProfileMESrcProfileName": zhoneOnuOmciGenericProfileMESrcProfileName,
       "zhoneOnuOmciGenericProfileFileName": zhoneOnuOmciGenericProfileFileName,
       "zhoneOnuOmciSpecificProfileTable": zhoneOnuOmciSpecificProfileTable,
       "zhoneOnuOmciSpecificProfileEntry": zhoneOnuOmciSpecificProfileEntry,
       "zhoneOnuOmciSpecificProfileIndex": zhoneOnuOmciSpecificProfileIndex,
       "zhoneOnuOmciSpecificProfileRowStatus": zhoneOnuOmciSpecificProfileRowStatus,
       "zhoneOnuOmciSpecificProfileOmciCommands": zhoneOnuOmciSpecificProfileOmciCommands,
       "zhoneOnuOmciSpecificProfileMESrcProfileName": zhoneOnuOmciSpecificProfileMESrcProfileName,
       "zhoneOnuOmciSpecificProfileFileName": zhoneOnuOmciSpecificProfileFileName,
       "zhoneGponOmciOnuAlarmsTable": zhoneGponOmciOnuAlarmsTable,
       "zhoneGponOmciOnuAlarmsEntry": zhoneGponOmciOnuAlarmsEntry,
       "zhoneGponOmciOnuAlarmsText": zhoneGponOmciOnuAlarmsText,
       "zhoneGponTrafficProfileTable": zhoneGponTrafficProfileTable,
       "zhoneGponTrafficProfileEntry": zhoneGponTrafficProfileEntry,
       "zhoneGponTrafficProfileIndex": zhoneGponTrafficProfileIndex,
       "zhoneGponTrafficProfileRowStatus": zhoneGponTrafficProfileRowStatus,
       "zhoneGponTrafficProfileGuaranteedUpstreamBw": zhoneGponTrafficProfileGuaranteedUpstreamBw,
       "zhoneGponTrafficProfileClass": zhoneGponTrafficProfileClass,
       "zhoneGponTrafficProfileCompensated": zhoneGponTrafficProfileCompensated,
       "zhoneGponTrafficProfileShared": zhoneGponTrafficProfileShared,
       "zhoneGponTrafficProfileDbaEnabled": zhoneGponTrafficProfileDbaEnabled,
       "zhoneGponTrafficProfileDbaFixedUsUbrBw": zhoneGponTrafficProfileDbaFixedUsUbrBw,
       "zhoneGponTrafficProfileDbaFixedUsCbrBw": zhoneGponTrafficProfileDbaFixedUsCbrBw,
       "zhoneGponTrafficProfileDbaAssuredUsBw": zhoneGponTrafficProfileDbaAssuredUsBw,
       "zhoneGponTrafficProfileMaxUsBw": zhoneGponTrafficProfileMaxUsBw,
       "zhoneGponTrafficProfileExtraUsBwType": zhoneGponTrafficProfileExtraUsBwType,
       "zhoneGponPortStatusTable": zhoneGponPortStatusTable,
       "zhoneGponPortStatusEntry": zhoneGponPortStatusEntry,
       "zhoneGponPortStatusAllocId": zhoneGponPortStatusAllocId,
       "zhoneGponPortStatusDbaStatus": zhoneGponPortStatusDbaStatus,
       "zhoneGponOmciStatsCurrentTable": zhoneGponOmciStatsCurrentTable,
       "zhoneGponOmciStatsCurrentEntry": zhoneGponOmciStatsCurrentEntry,
       "zhoneGponOmciStatsCurrentMEId": zhoneGponOmciStatsCurrentMEId,
       "zhoneGponOmciStatsCurrentLogicalPort": zhoneGponOmciStatsCurrentLogicalPort,
       "zhoneGponOmciStatsCurrentText": zhoneGponOmciStatsCurrentText,
       "zhoneGponOmciStatsPreviousTable": zhoneGponOmciStatsPreviousTable,
       "zhoneGponOmciStatsPreviousEntry": zhoneGponOmciStatsPreviousEntry,
       "zhoneGponOmciStatsPreviousMEId": zhoneGponOmciStatsPreviousMEId,
       "zhoneGponOmciStatsPreviousLogicalPort": zhoneGponOmciStatsPreviousLogicalPort,
       "zhoneGponOmciStatsPreviousText": zhoneGponOmciStatsPreviousText,
       "zhoneGponOmciStatusTable": zhoneGponOmciStatusTable,
       "zhoneGponOmciStatusEntry": zhoneGponOmciStatusEntry,
       "zhoneGponOmciStatusMEId": zhoneGponOmciStatusMEId,
       "zhoneGponOmciStatusLogicalPort": zhoneGponOmciStatusLogicalPort,
       "zhoneGponOmciStatusText": zhoneGponOmciStatusText,
       "zhoneGponOmciOnuRebootTable": zhoneGponOmciOnuRebootTable,
       "zhoneGponOmciOnuRebootEntry": zhoneGponOmciOnuRebootEntry,
       "zhoneGponOmciOnuReboot": zhoneGponOmciOnuReboot,
       "zhoneGponOmciOnuPortAdminTable": zhoneGponOmciOnuPortAdminTable,
       "zhoneGponOmciOnuPortAdminEntry": zhoneGponOmciOnuPortAdminEntry,
       "zhoneGponOmciOnuPortAdminMEId": zhoneGponOmciOnuPortAdminMEId,
       "zhoneGponOmciOnuPortAdminLogicalPort": zhoneGponOmciOnuPortAdminLogicalPort,
       "zhoneGponOmciOnuPortAdminState": zhoneGponOmciOnuPortAdminState,
       "zhoneGponOmciOnuPortAdminAutoDetect": zhoneGponOmciOnuPortAdminAutoDetect,
       "zhoneGponOmciOnuImageUpgradeTable": zhoneGponOmciOnuImageUpgradeTable,
       "zhoneGponOmciOnuImageUpgradeEntry": zhoneGponOmciOnuImageUpgradeEntry,
       "zhoneGponOmciOnuImageUpgradeAction": zhoneGponOmciOnuImageUpgradeAction,
       "zhoneOnuOmciImageUpgradeFilename": zhoneOnuOmciImageUpgradeFilename,
       "zhoneGponOmciOnuImageUpgradePartition": zhoneGponOmciOnuImageUpgradePartition,
       "zhoneOnuOmciImageUpgradeImageVersionPartition0": zhoneOnuOmciImageUpgradeImageVersionPartition0,
       "zhoneOnuOmciImageUpgradeImageVersionPartition1": zhoneOnuOmciImageUpgradeImageVersionPartition1,
       "zhoneOnuOmciImageUpgradeIsCommittedPartition0": zhoneOnuOmciImageUpgradeIsCommittedPartition0,
       "zhoneOnuOmciImageUpgradeIsCommittedPartition1": zhoneOnuOmciImageUpgradeIsCommittedPartition1,
       "zhoneOnuOmciImageUpgradeIsActivatedPartition0": zhoneOnuOmciImageUpgradeIsActivatedPartition0,
       "zhoneOnuOmciImageUpgradeIsActivatedPartition1": zhoneOnuOmciImageUpgradeIsActivatedPartition1,
       "zhoneOnuOmciImageUpgradeIsValidPartition0": zhoneOnuOmciImageUpgradeIsValidPartition0,
       "zhoneOnuOmciImageUpgradeIsValidPartition1": zhoneOnuOmciImageUpgradeIsValidPartition1,
       "zhoneOnuOmciImageUpgradeDownloadStatus": zhoneOnuOmciImageUpgradeDownloadStatus,
       "zhoneGponOmciOnuImageUpgradeModel": zhoneGponOmciOnuImageUpgradeModel,
       "zhoneGponOmciOnuImageUpgradeStartTime": zhoneGponOmciOnuImageUpgradeStartTime,
       "zhoneGponOmciOnuImageUpgradeWillBeActivated": zhoneGponOmciOnuImageUpgradeWillBeActivated,
       "zhoneGponOmciOnuImageUpgradeWillBeCommitted": zhoneGponOmciOnuImageUpgradeWillBeCommitted,
       "zhoneGponOmciOnuImageUpgradeType": zhoneGponOmciOnuImageUpgradeType,
       "zhoneGponOmciOnuImageDownloadProgressPercentage": zhoneGponOmciOnuImageDownloadProgressPercentage,
       "zhoneGponOmciOnuImageUpgradeMethod": zhoneGponOmciOnuImageUpgradeMethod,
       "zhoneGponOltStatusTable": zhoneGponOltStatusTable,
       "zhoneGponOltStatusEntry": zhoneGponOltStatusEntry,
       "zhoneGponOltOpticTemperature": zhoneGponOltOpticTemperature,
       "zhoneGponOltOpticVoltage": zhoneGponOltOpticVoltage,
       "zhoneGponOltOpticTxBiasCurrent": zhoneGponOltOpticTxBiasCurrent,
       "zhoneGponOltOpticTxPower": zhoneGponOltOpticTxPower,
       "zhoneGponOltOpticStatus": zhoneGponOltOpticStatus,
       "zhoneGponOltOpticAlarms": zhoneGponOltOpticAlarms,
       "zhoneGponOltStatusWord": zhoneGponOltStatusWord,
       "zhoneGponOltConfiguredOnuCount": zhoneGponOltConfiguredOnuCount,
       "zhoneGponOltActiveOnuCount": zhoneGponOltActiveOnuCount,
       "zhoneGponOltDbaStatusTable": zhoneGponOltDbaStatusTable,
       "zhoneGponOltDbaStatusEntry": zhoneGponOltDbaStatusEntry,
       "zhoneGponOltDbaTotalAvailableBw": zhoneGponOltDbaTotalAvailableBw,
       "zhoneGponOltDbaTotalAvailableCompensatedCbrBw": zhoneGponOltDbaTotalAvailableCompensatedCbrBw,
       "zhoneGponOltDbaAllocatedUbrBw": zhoneGponOltDbaAllocatedUbrBw,
       "zhoneGponOltDbaAllocatedCbrBw": zhoneGponOltDbaAllocatedCbrBw,
       "zhoneGponOltDbaAllocatedCompensatedCbrBw": zhoneGponOltDbaAllocatedCompensatedCbrBw,
       "zhoneGponOltDbaAllocatedAssuredBw": zhoneGponOltDbaAllocatedAssuredBw,
       "zhoneGponOltDbaAllocatedNonAssuredBw": zhoneGponOltDbaAllocatedNonAssuredBw,
       "zhoneGponOltDbaAllocatedBestEffortBw": zhoneGponOltDbaAllocatedBestEffortBw,
       "zhoneGponOltDbaMaxAllocIds": zhoneGponOltDbaMaxAllocIds,
       "zhoneGponOltDbaAvailAllocIds": zhoneGponOltDbaAvailAllocIds,
       "zhoneGponOltDbaUsedAllocIds": zhoneGponOltDbaUsedAllocIds,
       "zhoneGponOltDbaMaxDbaAllocIds": zhoneGponOltDbaMaxDbaAllocIds,
       "zhoneGponOltDbaAvailDbaAllocIds": zhoneGponOltDbaAvailDbaAllocIds,
       "zhoneGponOltDbaUsedDbaAllocIds": zhoneGponOltDbaUsedDbaAllocIds,
       "zhoneGponOltDbaTotalOltGemPorts": zhoneGponOltDbaTotalOltGemPorts,
       "zhoneGponOltDbaLastCacRc": zhoneGponOltDbaLastCacRc,
       "zhoneGponUpgradeByStateTable": zhoneGponUpgradeByStateTable,
       "zhoneGponUpgradeByStateEntry": zhoneGponUpgradeByStateEntry,
       "zhoneGponUpgradeOlt": zhoneGponUpgradeOlt,
       "zhoneGponUpgradeOnu": zhoneGponUpgradeOnu,
       "zhoneGponUpgradeModel": zhoneGponUpgradeModel,
       "zhoneGponUpgradeStartTime": zhoneGponUpgradeStartTime,
       "zhoneGponUpgradeIfIndex": zhoneGponUpgradeIfIndex,
       "zhoneGponUpgradeByStateOnuState": zhoneGponUpgradeByStateOnuState,
       "zhoneGponUpgradeByStateWillBeActivated": zhoneGponUpgradeByStateWillBeActivated,
       "zhoneGponUpgradeByStateWillBeCommitted": zhoneGponUpgradeByStateWillBeCommitted,
       "zhoneGponUpgradeByStateUpgradeType": zhoneGponUpgradeByStateUpgradeType,
       "zhoneGponUpgradeByStatePartition": zhoneGponUpgradeByStatePartition,
       "zhoneGponUpgradeProgressPercentage": zhoneGponUpgradeProgressPercentage,
       "zhoneGponUpgradeByStateMethod": zhoneGponUpgradeByStateMethod,
       "zhoneGponCmd": zhoneGponCmd,
       "zhoneGponCmdOperation": zhoneGponCmdOperation,
       "zhoneGponCmdFilterMask": zhoneGponCmdFilterMask,
       "zhoneGponCmdShelf": zhoneGponCmdShelf,
       "zhoneGponCmdSlot": zhoneGponCmdSlot,
       "zhoneGponCmdOlt": zhoneGponCmdOlt,
       "zhoneGponCmdOnu": zhoneGponCmdOnu,
       "zhoneGponOltStatisticsTable": zhoneGponOltStatisticsTable,
       "zhoneGponOltStatisticsEntry": zhoneGponOltStatisticsEntry,
       "zhoneGponOltStatisticsUpstreamValidGemFrames": zhoneGponOltStatisticsUpstreamValidGemFrames,
       "zhoneGponOltStatisticsUpstreamDiscardedFrames": zhoneGponOltStatisticsUpstreamDiscardedFrames,
       "zhoneGponOltStatisticsUpstreamGemFrames": zhoneGponOltStatisticsUpstreamGemFrames,
       "zhoneGponOltStatisticsUpstreamOmciFrames": zhoneGponOltStatisticsUpstreamOmciFrames,
       "zhoneGponOltStatisticsUpstreamPloamFrames": zhoneGponOltStatisticsUpstreamPloamFrames,
       "zhoneGponOltStatisticsUpstreamIdlePloamFrames": zhoneGponOltStatisticsUpstreamIdlePloamFrames,
       "zhoneGponOltStatisticsDownstreamValidGemFrames": zhoneGponOltStatisticsDownstreamValidGemFrames,
       "zhoneGponOltStatisticsDownstreamDiscardedFrames": zhoneGponOltStatisticsDownstreamDiscardedFrames,
       "zhoneGponOltStatisticsDownstreamGemFrames": zhoneGponOltStatisticsDownstreamGemFrames,
       "zhoneGponOltStatisticsDownstreamOmciFrames": zhoneGponOltStatisticsDownstreamOmciFrames,
       "zhoneGponOltStatisticsDownstreamPloamFrames": zhoneGponOltStatisticsDownstreamPloamFrames,
       "zhoneGponOltStatisticsDownstreamIdlePloamFrames": zhoneGponOltStatisticsDownstreamIdlePloamFrames,
       "zhoneGponOltStatisticsDownstreamPonValidEthernetPkts": zhoneGponOltStatisticsDownstreamPonValidEthernetPkts,
       "zhoneGponOltStatisticsDownstreamPonCpuPkts": zhoneGponOltStatisticsDownstreamPonCpuPkts,
       "zhoneGponOltStatisticsDownstreamTxBytes": zhoneGponOltStatisticsDownstreamTxBytes,
       "zhoneGponOltStatisticsUpstreamPonValidPkts": zhoneGponOltStatisticsUpstreamPonValidPkts,
       "zhoneGponOltStatisticsUpstreamPonValidNotIdlePloams": zhoneGponOltStatisticsUpstreamPonValidNotIdlePloams,
       "zhoneGponOltStatisticsUpstreamPonErrorPloams": zhoneGponOltStatisticsUpstreamPonErrorPloams,
       "zhoneGponOltStatisticsUpstreamPonInvalidPkts": zhoneGponOltStatisticsUpstreamPonInvalidPkts,
       "zhoneGponOltStatisticsUpstreamDroppedPktsInactivePorts": zhoneGponOltStatisticsUpstreamDroppedPktsInactivePorts,
       "zhoneGponOltStatisticsUpstreamDroppedPloamsFifoFull": zhoneGponOltStatisticsUpstreamDroppedPloamsFifoFull,
       "zhoneGponOltStatisticsDownstreamTmValidPkts": zhoneGponOltStatisticsDownstreamTmValidPkts,
       "zhoneGponOltStatisticsDownstreamTmCrcPkts": zhoneGponOltStatisticsDownstreamTmCrcPkts,
       "zhoneGponOltStatisticsDownstreamTmDroppedCpuPkts": zhoneGponOltStatisticsDownstreamTmDroppedCpuPkts,
       "zhoneGponOltStatisticsDownstreamTmMacLookupMiss": zhoneGponOltStatisticsDownstreamTmMacLookupMiss,
       "zhoneGponOltStatisticsDownstreamTmPktsForwardedFromHmToPon": zhoneGponOltStatisticsDownstreamTmPktsForwardedFromHmToPon,
       "zhoneGponOltStatisticsDownstreamTmPktsDroppedGemPidNotEnabled": zhoneGponOltStatisticsDownstreamTmPktsDroppedGemPidNotEnabled,
       "zhoneGponOltStatisticsDownstreamTmQ0ValidPkts": zhoneGponOltStatisticsDownstreamTmQ0ValidPkts,
       "zhoneGponOltStatisticsDownstreamTmQ0DroppedPkts": zhoneGponOltStatisticsDownstreamTmQ0DroppedPkts,
       "zhoneGponOltStatisticsDownstreamTmQ1ValidPkts": zhoneGponOltStatisticsDownstreamTmQ1ValidPkts,
       "zhoneGponOltStatisticsDownstreamTmQ1DroppedPkts": zhoneGponOltStatisticsDownstreamTmQ1DroppedPkts,
       "zhoneGponOltStatisticsDownstreamTmQ2ValidPkts": zhoneGponOltStatisticsDownstreamTmQ2ValidPkts,
       "zhoneGponOltStatisticsDownstreamTmQ2DroppedPkts": zhoneGponOltStatisticsDownstreamTmQ2DroppedPkts,
       "zhoneGponOltStatisticsDownstreamTmQ3ValidPkts": zhoneGponOltStatisticsDownstreamTmQ3ValidPkts,
       "zhoneGponOltStatisticsDownstreamTmQ3DroppedPkts": zhoneGponOltStatisticsDownstreamTmQ3DroppedPkts,
       "zhoneGponOltStatisticsDownstreamTmQ4ValidPkts": zhoneGponOltStatisticsDownstreamTmQ4ValidPkts,
       "zhoneGponOltStatisticsDownstreamTmQ4DroppedPkts": zhoneGponOltStatisticsDownstreamTmQ4DroppedPkts,
       "zhoneGponOltStatisticsDownstreamTmQ5ValidPkts": zhoneGponOltStatisticsDownstreamTmQ5ValidPkts,
       "zhoneGponOltStatisticsDownstreamTmQ5DroppedPkts": zhoneGponOltStatisticsDownstreamTmQ5DroppedPkts,
       "zhoneGponOltStatisticsDownstreamTmQ6ValidPkts": zhoneGponOltStatisticsDownstreamTmQ6ValidPkts,
       "zhoneGponOltStatisticsDownstreamTmQ6DroppedPkts": zhoneGponOltStatisticsDownstreamTmQ6DroppedPkts,
       "zhoneGponOltStatisticsDownstreamTmQ7ValidPkts": zhoneGponOltStatisticsDownstreamTmQ7ValidPkts,
       "zhoneGponOltStatisticsDownstreamTmQ7DroppedPkts": zhoneGponOltStatisticsDownstreamTmQ7DroppedPkts,
       "zhoneGponOltStatisticsUpstreamTmDroppedCpuPkts": zhoneGponOltStatisticsUpstreamTmDroppedCpuPkts,
       "zhoneGponOltStatisticsUpstreamTmDroppedPktsCrcError": zhoneGponOltStatisticsUpstreamTmDroppedPktsCrcError,
       "zhoneGponOltStatisticsUpstreamTmDroppedPktsSecurity": zhoneGponOltStatisticsUpstreamTmDroppedPktsSecurity,
       "zhoneGponOltStatisticsUpstreamTmLearnFailures": zhoneGponOltStatisticsUpstreamTmLearnFailures,
       "zhoneGponOltStatisticsUpstreamTmQ0ValidPkts": zhoneGponOltStatisticsUpstreamTmQ0ValidPkts,
       "zhoneGponOltStatisticsUpstreamTmQ0DroppedPkts": zhoneGponOltStatisticsUpstreamTmQ0DroppedPkts,
       "zhoneGponOltStatisticsUpstreamTmQ1ValidPkts": zhoneGponOltStatisticsUpstreamTmQ1ValidPkts,
       "zhoneGponOltStatisticsUpstreamTmQ1DroppedPkts": zhoneGponOltStatisticsUpstreamTmQ1DroppedPkts,
       "zhoneGponOltStatisticsUpstreamTmQ2ValidPkts": zhoneGponOltStatisticsUpstreamTmQ2ValidPkts,
       "zhoneGponOltStatisticsUpstreamTmQ2DroppedPkts": zhoneGponOltStatisticsUpstreamTmQ2DroppedPkts,
       "zhoneGponOltStatisticsUpstreamTmQ3ValidPkts": zhoneGponOltStatisticsUpstreamTmQ3ValidPkts,
       "zhoneGponOltStatisticsUpstreamTmQ3DroppedPkts": zhoneGponOltStatisticsUpstreamTmQ3DroppedPkts,
       "zhoneGponOltStatisticsUpstreamTmQ4ValidPkts": zhoneGponOltStatisticsUpstreamTmQ4ValidPkts,
       "zhoneGponOltStatisticsUpstreamTmQ4DroppedPkts": zhoneGponOltStatisticsUpstreamTmQ4DroppedPkts,
       "zhoneGponOltStatisticsUpstreamTmQ5ValidPkts": zhoneGponOltStatisticsUpstreamTmQ5ValidPkts,
       "zhoneGponOltStatisticsUpstreamTmQ5DroppedPkts": zhoneGponOltStatisticsUpstreamTmQ5DroppedPkts,
       "zhoneGponOltStatisticsUpstreamTmQ6ValidPkts": zhoneGponOltStatisticsUpstreamTmQ6ValidPkts,
       "zhoneGponOltStatisticsUpstreamTmQ6DroppedPkts": zhoneGponOltStatisticsUpstreamTmQ6DroppedPkts,
       "zhoneGponOltStatisticsUpstreamTmQ7ValidPkts": zhoneGponOltStatisticsUpstreamTmQ7ValidPkts,
       "zhoneGponOltStatisticsUpstreamTmQ7DroppedPkts": zhoneGponOltStatisticsUpstreamTmQ7DroppedPkts,
       "zhoneGponOltStatisticsClearStats": zhoneGponOltStatisticsClearStats,
       "zhoneGponUpstreamOntStatisticsTable": zhoneGponUpstreamOntStatisticsTable,
       "zhoneGponUpstreamOntStatisticsEntry": zhoneGponUpstreamOntStatisticsEntry,
       "zhoneGponUpstreamOntStatisticsUpstreamBipErrors": zhoneGponUpstreamOntStatisticsUpstreamBipErrors,
       "zhoneGponUpstreamOntStatisticsFecCorrectedBytes": zhoneGponUpstreamOntStatisticsFecCorrectedBytes,
       "zhoneGponUpstreamOntStatisticsFecCorrectedCodewords": zhoneGponUpstreamOntStatisticsFecCorrectedCodewords,
       "zhoneGponUpstreamOntStatisticsFecUncorrectedCodewords": zhoneGponUpstreamOntStatisticsFecUncorrectedCodewords,
       "zhoneGponUpstreamOntStatisticsTotalRxCodewords": zhoneGponUpstreamOntStatisticsTotalRxCodewords,
       "zhoneGponUpstreamOntStatisticsUnreceivedBursts": zhoneGponUpstreamOntStatisticsUnreceivedBursts,
       "zhoneGponUpstreamOntStatisticsBipErrors": zhoneGponUpstreamOntStatisticsBipErrors,
       "zhoneGponUpstreamOntStatisticsRemoteBipErrors": zhoneGponUpstreamOntStatisticsRemoteBipErrors,
       "zhoneGponUpstreamOntStatisticsDriftOfWindowIndications": zhoneGponUpstreamOntStatisticsDriftOfWindowIndications,
       "zhoneGponUpstreamOntStatisticsMessageErrorMessage": zhoneGponUpstreamOntStatisticsMessageErrorMessage,
       "zhoneGponUpstreamOntStatisticsClearStats": zhoneGponUpstreamOntStatisticsClearStats,
       "zhoneGponOltMIB": zhoneGponOltMIB,
       "zhoneGponOltConfigGroup": zhoneGponOltConfigGroup,
       "zhoneGponOnuConfigGroup": zhoneGponOnuConfigGroup,
       "zhoneGponPortConfigGroup": zhoneGponPortConfigGroup,
       "zhoneGponAllocIdGroup": zhoneGponAllocIdGroup,
       "zhoneGponSerialNoGroup": zhoneGponSerialNoGroup,
       "zhoneGponOnuStatusGroup": zhoneGponOnuStatusGroup,
       "zhoneOnuOmciMeProfileGroup": zhoneOnuOmciMeProfileGroup,
       "zhoneOnuOmciGenericProfileGroup": zhoneOnuOmciGenericProfileGroup,
       "zhoneOnuOmciSpecificProfileGroup": zhoneOnuOmciSpecificProfileGroup,
       "zhoneGponOmciOnuAlarmsGroup": zhoneGponOmciOnuAlarmsGroup,
       "zhoneGponTrapGroup": zhoneGponTrapGroup,
       "zhoneGponTrafficProfileGroup": zhoneGponTrafficProfileGroup,
       "zhoneGponPortStatusGroup": zhoneGponPortStatusGroup,
       "zhoneGponOmciStatusGroup": zhoneGponOmciStatusGroup,
       "zhoneGponOmciOnuRebootGroup": zhoneGponOmciOnuRebootGroup,
       "zhoneGponOmciOnuPortAdminGroup": zhoneGponOmciOnuPortAdminGroup,
       "zhoneGponOmciOnuImageUpgradeGroup": zhoneGponOmciOnuImageUpgradeGroup,
       "zhoneGponOltStatusGroup": zhoneGponOltStatusGroup,
       "zhoneGponeOltDbaStatusGroup": zhoneGponeOltDbaStatusGroup,
       "zhoneGponCmdGroup": zhoneGponCmdGroup,
       "zhoneGponOltStatisticsGroup": zhoneGponOltStatisticsGroup,
       "zhoneGponUpstreamOntStatisticsGroup": zhoneGponUpstreamOntStatisticsGroup,
       "zhoneGponDeprecated": zhoneGponDeprecated}
)
