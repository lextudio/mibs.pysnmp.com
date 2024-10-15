# SNMP MIB module (Zhone-CPE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Zhone-CPE-MIB
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

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

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
 zhoneCpe,
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
 zhoneWdm,
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
    "zhoneCpe",
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
    "zhoneWdm",
    "zhoneWtn",
    "zhoneZAP",
    "zhoneZedge",
    "zhoneZmsProduct",
    "zhoneZplex")

(ZhoneAdminState,
 ZhoneAdminString,
 ZhoneAlarmSeverity,
 ZhoneEnabledFlag,
 ZhoneRowStatus) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminState",
    "ZhoneAdminString",
    "ZhoneAlarmSeverity",
    "ZhoneEnabledFlag",
    "ZhoneRowStatus")


# MODULE-IDENTITY

zhoneCpeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 118)
)
zhoneCpeMIB.setRevisions(
        ("2014-05-05 11:09",
         "2014-04-18 18:44",
         "2014-04-22 15:49",
         "2014-03-21 11:35",
         "2014-03-13 16:36",
         "2014-03-10 11:27",
         "2014-03-07 13:15",
         "2014-03-05 11:38",
         "2014-02-24 13:07",
         "2014-02-03 12:52",
         "2014-01-24 15:31",
         "2013-12-16 08:17",
         "2013-12-04 13:35",
         "2013-11-18 16:19",
         "2013-09-24 14:35",
         "2013-08-19 14:47",
         "2013-08-07 10:54",
         "2013-07-25 13:40",
         "2013-07-18 08:54",
         "2013-06-27 23:26",
         "2013-06-24 11:43",
         "2013-06-23 23:58",
         "2013-06-06 18:55",
         "2013-06-06 11:26",
         "2013-06-06 10:03",
         "2013-06-04 23:14",
         "2013-05-15 09:35",
         "2013-04-22 12:46",
         "2013-04-11 14:16",
         "2013-03-18 11:51",
         "2013-03-01 14:17",
         "2013-01-11 23:10",
         "2012-12-18 10:18",
         "2013-01-02 18:30",
         "2012-11-19 12:29",
         "2012-10-31 06:49",
         "2012-09-24 10:48",
         "2012-08-05 23:50",
         "2012-07-12 14:37",
         "2012-07-03 09:57",
         "2012-06-21 12:02",
         "2012-06-20 09:52",
         "2012-06-12 11:57",
         "2012-05-20 23:49",
         "2012-05-09 16:26",
         "2012-04-30 09:52",
         "2012-04-25 10:24",
         "2012-04-20 22:45",
         "2012-04-12 16:15",
         "2012-03-28 10:52",
         "2012-03-26 09:58",
         "2012-03-19 10:43",
         "2012-02-13 15:49",
         "2012-01-28 10:47",
         "2011-11-11 15:05",
         "2011-09-23 14:04",
         "2011-09-08 14:16",
         "2011-07-12 15:17",
         "2011-07-05 14:15",
         "2011-06-16 11:18",
         "2011-06-03 01:04",
         "2011-05-23 09:25",
         "2011-05-18 00:15",
         "2011-04-27 10:14",
         "2011-04-12 15:36",
         "2011-03-28 10:07",
         "2011-03-01 10:29",
         "2011-02-18 14:51",
         "2011-02-03 10:48",
         "2011-01-19 14:20",
         "2011-01-20 12:01",
         "2011-01-12 14:01",
         "2010-12-17 10:02",
         "2010-12-09 12:51")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TpType(Integer32, TextualConvention):
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
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("dot11TerminationPoint", 18),
          ("ethernetFlowTerminationPoint", 9),
          ("fiberLanTerminationPoint", 19),
          ("gemInterworkingTerminationPoint", 5),
          ("h248VoiceTerminationPoint", 13),
          ("interworkingVCCTerminationPoint", 2),
          ("ipHostConfigData", 4),
          ("mapperServiceProfile", 3),
          ("mgcpVoiceTerminationPoint", 22),
          ("mgmtTerminationPoint", 21),
          ("multicastGEMInterworkingTerminationPoint", 6),
          ("physicalPathTerminationPointEthernetUNI", 1),
          ("physicalPathTerminationPointIPTVUNI", 12),
          ("physicalPathTerminationPointRFvideoUNI", 11),
          ("physicalPathTerminationPointUNI", 10),
          ("physicalPathTerminationPointVDSLUNI", 8),
          ("physicalPathTerminationPointxDSLUNIPartOne", 7),
          ("pweTerminationPoint", 16),
          ("sipPlarVoiceTerminationPoint", 15),
          ("sipVoiceTerminationPoint", 14),
          ("tr69TerminationPoint", 20),
          ("virtualEthernetInterfacePoint", 17))
    )



class ZhoneCpeTemplateType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(668,
              669,
              670,
              671,
              672)
        )
    )
    namedValues = NamedValues(
        *(("data", 671),
          ("pwe", 669),
          ("video", 672),
          ("voip", 668),
          ("wifi", 670))
    )



# MIB Managed Objects in the order of their OIDs

_ZhoneCpeObjectID_ObjectIdentity = ObjectIdentity
zhoneCpeObjectID = _ZhoneCpeObjectID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1)
)
_ZhoneCpeSipDialPlan_ObjectIdentity = ObjectIdentity
zhoneCpeSipDialPlan = _ZhoneCpeSipDialPlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 1)
)
if mibBuilder.loadTexts:
    zhoneCpeSipDialPlan.setStatus("current")
_ZhoneCpeSipDialPlanIndexTable_Object = MibTable
zhoneCpeSipDialPlanIndexTable = _ZhoneCpeSipDialPlanIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 1, 1)
)
if mibBuilder.loadTexts:
    zhoneCpeSipDialPlanIndexTable.setStatus("current")
_ZhoneCpeSipDialPlanIndexEntry_Object = MibTableRow
zhoneCpeSipDialPlanIndexEntry = _ZhoneCpeSipDialPlanIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 1, 1, 1)
)
zhoneCpeSipDialPlanIndexEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeVoipServerIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeSipDialPlanIndexEntry.setStatus("current")


class _ZhoneCpeSipDialPlanIndexNext_Type(Unsigned32):
    """Custom type zhoneCpeSipDialPlanIndexNext based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeSipDialPlanIndexNext_Type.__name__ = "Unsigned32"
_ZhoneCpeSipDialPlanIndexNext_Object = MibTableColumn
zhoneCpeSipDialPlanIndexNext = _ZhoneCpeSipDialPlanIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 1, 1, 1, 1),
    _ZhoneCpeSipDialPlanIndexNext_Type()
)
zhoneCpeSipDialPlanIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeSipDialPlanIndexNext.setStatus("current")
_ZhoneCpeSipDialPlanTable_Object = MibTable
zhoneCpeSipDialPlanTable = _ZhoneCpeSipDialPlanTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 1, 2)
)
if mibBuilder.loadTexts:
    zhoneCpeSipDialPlanTable.setStatus("current")
_ZhoneCpeSipDialPlanEntry_Object = MibTableRow
zhoneCpeSipDialPlanEntry = _ZhoneCpeSipDialPlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 1, 2, 1)
)
zhoneCpeSipDialPlanEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeSipServerIndex"),
    (0, "Zhone-CPE-MIB", "zhoneCpeSipDialPlanIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeSipDialPlanEntry.setStatus("current")


class _ZhoneCpeSipServerIndex_Type(Unsigned32):
    """Custom type zhoneCpeSipServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeSipServerIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeSipServerIndex_Object = MibTableColumn
zhoneCpeSipServerIndex = _ZhoneCpeSipServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 1, 2, 1, 1),
    _ZhoneCpeSipServerIndex_Type()
)
zhoneCpeSipServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeSipServerIndex.setStatus("current")


class _ZhoneCpeSipDialPlanIndex_Type(Unsigned32):
    """Custom type zhoneCpeSipDialPlanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeSipDialPlanIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeSipDialPlanIndex_Object = MibTableColumn
zhoneCpeSipDialPlanIndex = _ZhoneCpeSipDialPlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 1, 2, 1, 2),
    _ZhoneCpeSipDialPlanIndex_Type()
)
zhoneCpeSipDialPlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeSipDialPlanIndex.setStatus("current")


class _ZhoneCpeSipDialPlanRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpeSipDialPlanRowStatus based on ZhoneRowStatus"""


_ZhoneCpeSipDialPlanRowStatus_Object = MibTableColumn
zhoneCpeSipDialPlanRowStatus = _ZhoneCpeSipDialPlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 1, 2, 1, 3),
    _ZhoneCpeSipDialPlanRowStatus_Type()
)
zhoneCpeSipDialPlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeSipDialPlanRowStatus.setStatus("current")


class _ZhoneCpeSipDialPlanFormat_Type(Integer32):
    """Custom type zhoneCpeSipDialPlanFormat based on Integer32"""
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
        *(("h248", 1),
          ("nsc", 2),
          ("vendorspecific", 3))
    )


_ZhoneCpeSipDialPlanFormat_Type.__name__ = "Integer32"
_ZhoneCpeSipDialPlanFormat_Object = MibTableColumn
zhoneCpeSipDialPlanFormat = _ZhoneCpeSipDialPlanFormat_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 1, 2, 1, 4),
    _ZhoneCpeSipDialPlanFormat_Type()
)
zhoneCpeSipDialPlanFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeSipDialPlanFormat.setStatus("current")


class _ZhoneCpeSipDialPlanString_Type(OctetString):
    """Custom type zhoneCpeSipDialPlanString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZhoneCpeSipDialPlanString_Type.__name__ = "OctetString"
_ZhoneCpeSipDialPlanString_Object = MibTableColumn
zhoneCpeSipDialPlanString = _ZhoneCpeSipDialPlanString_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 1, 2, 1, 5),
    _ZhoneCpeSipDialPlanString_Type()
)
zhoneCpeSipDialPlanString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeSipDialPlanString.setStatus("current")
_ZhoneCpeVoipServer_ObjectIdentity = ObjectIdentity
zhoneCpeVoipServer = _ZhoneCpeVoipServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2)
)
if mibBuilder.loadTexts:
    zhoneCpeVoipServer.setStatus("current")
_ZhoneCpeVoipServerIndexNext_Type = Integer32
_ZhoneCpeVoipServerIndexNext_Object = MibScalar
zhoneCpeVoipServerIndexNext = _ZhoneCpeVoipServerIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 1),
    _ZhoneCpeVoipServerIndexNext_Type()
)
zhoneCpeVoipServerIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeVoipServerIndexNext.setStatus("current")
_ZhoneCpeVoipServerTable_Object = MibTable
zhoneCpeVoipServerTable = _ZhoneCpeVoipServerTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2)
)
if mibBuilder.loadTexts:
    zhoneCpeVoipServerTable.setStatus("current")
_ZhoneCpeVoipServerEntry_Object = MibTableRow
zhoneCpeVoipServerEntry = _ZhoneCpeVoipServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1)
)
zhoneCpeVoipServerEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeVoipServerIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeVoipServerEntry.setStatus("current")


class _ZhoneCpeVoipServerIndex_Type(Unsigned32):
    """Custom type zhoneCpeVoipServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeVoipServerIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeVoipServerIndex_Object = MibTableColumn
zhoneCpeVoipServerIndex = _ZhoneCpeVoipServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 1),
    _ZhoneCpeVoipServerIndex_Type()
)
zhoneCpeVoipServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeVoipServerIndex.setStatus("current")


class _ZhoneCpeVoipServerRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpeVoipServerRowStatus based on ZhoneRowStatus"""


_ZhoneCpeVoipServerRowStatus_Object = MibTableColumn
zhoneCpeVoipServerRowStatus = _ZhoneCpeVoipServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 2),
    _ZhoneCpeVoipServerRowStatus_Type()
)
zhoneCpeVoipServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipServerRowStatus.setStatus("current")
_ZhoneCpeVoipProfileName_Type = ZhoneAdminString
_ZhoneCpeVoipProfileName_Object = MibTableColumn
zhoneCpeVoipProfileName = _ZhoneCpeVoipProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 3),
    _ZhoneCpeVoipProfileName_Type()
)
zhoneCpeVoipProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipProfileName.setStatus("current")
_ZhoneCpeVoipPrimaryServer_Type = InetAddress
_ZhoneCpeVoipPrimaryServer_Object = MibTableColumn
zhoneCpeVoipPrimaryServer = _ZhoneCpeVoipPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 4),
    _ZhoneCpeVoipPrimaryServer_Type()
)
zhoneCpeVoipPrimaryServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipPrimaryServer.setStatus("current")
_ZhoneCpeVoipSecondaryServer_Type = InetAddress
_ZhoneCpeVoipSecondaryServer_Object = MibTableColumn
zhoneCpeVoipSecondaryServer = _ZhoneCpeVoipSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 5),
    _ZhoneCpeVoipSecondaryServer_Type()
)
zhoneCpeVoipSecondaryServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipSecondaryServer.setStatus("current")


class _ZhoneCpeVoipServerSignallingProtocol_Type(Integer32):
    """Custom type zhoneCpeVoipServerSignallingProtocol based on Integer32"""
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
        *(("h248", 3),
          ("mgcp", 4),
          ("sip", 1),
          ("sipplar", 2))
    )


_ZhoneCpeVoipServerSignallingProtocol_Type.__name__ = "Integer32"
_ZhoneCpeVoipServerSignallingProtocol_Object = MibTableColumn
zhoneCpeVoipServerSignallingProtocol = _ZhoneCpeVoipServerSignallingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 6),
    _ZhoneCpeVoipServerSignallingProtocol_Type()
)
zhoneCpeVoipServerSignallingProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipServerSignallingProtocol.setStatus("current")


class _ZhoneCpeVoipSipRegExpirationTime_Type(Unsigned32):
    """Custom type zhoneCpeVoipSipRegExpirationTime based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeVoipSipRegExpirationTime_Type.__name__ = "Unsigned32"
_ZhoneCpeVoipSipRegExpirationTime_Object = MibTableColumn
zhoneCpeVoipSipRegExpirationTime = _ZhoneCpeVoipSipRegExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 7),
    _ZhoneCpeVoipSipRegExpirationTime_Type()
)
zhoneCpeVoipSipRegExpirationTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipSipRegExpirationTime.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeVoipSipRegExpirationTime.setUnits("seconds")


class _ZhoneCpeVoipSipReRegHeadStartTime_Type(Unsigned32):
    """Custom type zhoneCpeVoipSipReRegHeadStartTime based on Unsigned32"""
    defaultValue = 360

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeVoipSipReRegHeadStartTime_Type.__name__ = "Unsigned32"
_ZhoneCpeVoipSipReRegHeadStartTime_Object = MibTableColumn
zhoneCpeVoipSipReRegHeadStartTime = _ZhoneCpeVoipSipReRegHeadStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 8),
    _ZhoneCpeVoipSipReRegHeadStartTime_Type()
)
zhoneCpeVoipSipReRegHeadStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipSipReRegHeadStartTime.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeVoipSipReRegHeadStartTime.setUnits("seconds")
_ZhoneCpeVoipSipDomain_Type = InetAddress
_ZhoneCpeVoipSipDomain_Object = MibTableColumn
zhoneCpeVoipSipDomain = _ZhoneCpeVoipSipDomain_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 9),
    _ZhoneCpeVoipSipDomain_Type()
)
zhoneCpeVoipSipDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipSipDomain.setStatus("current")
_ZhoneCpeVoipSipRegistrar_Type = InetAddress
_ZhoneCpeVoipSipRegistrar_Object = MibTableColumn
zhoneCpeVoipSipRegistrar = _ZhoneCpeVoipSipRegistrar_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 10),
    _ZhoneCpeVoipSipRegistrar_Type()
)
zhoneCpeVoipSipRegistrar.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipSipRegistrar.setStatus("current")
_ZhoneCpeVoipSoftSwitch_Type = ZhoneAdminString
_ZhoneCpeVoipSoftSwitch_Object = MibTableColumn
zhoneCpeVoipSoftSwitch = _ZhoneCpeVoipSoftSwitch_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 11),
    _ZhoneCpeVoipSoftSwitch_Type()
)
zhoneCpeVoipSoftSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipSoftSwitch.setStatus("current")


class _ZhoneCpeVoipMgcVersion_Type(Integer32):
    """Custom type zhoneCpeVoipMgcVersion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneCpeVoipMgcVersion_Type.__name__ = "Integer32"
_ZhoneCpeVoipMgcVersion_Object = MibTableColumn
zhoneCpeVoipMgcVersion = _ZhoneCpeVoipMgcVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 12),
    _ZhoneCpeVoipMgcVersion_Type()
)
zhoneCpeVoipMgcVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipMgcVersion.setStatus("current")


class _ZhoneCpeVoipMgcMessageFormat_Type(Integer32):
    """Custom type zhoneCpeVoipMgcMessageFormat based on Integer32"""
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
        *(("binary", 3),
          ("long", 1),
          ("short", 2))
    )


_ZhoneCpeVoipMgcMessageFormat_Type.__name__ = "Integer32"
_ZhoneCpeVoipMgcMessageFormat_Object = MibTableColumn
zhoneCpeVoipMgcMessageFormat = _ZhoneCpeVoipMgcMessageFormat_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 13),
    _ZhoneCpeVoipMgcMessageFormat_Type()
)
zhoneCpeVoipMgcMessageFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipMgcMessageFormat.setStatus("current")


class _ZhoneCpeVoipMgcMaximumRetryTime_Type(Integer32):
    """Custom type zhoneCpeVoipMgcMaximumRetryTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneCpeVoipMgcMaximumRetryTime_Type.__name__ = "Integer32"
_ZhoneCpeVoipMgcMaximumRetryTime_Object = MibTableColumn
zhoneCpeVoipMgcMaximumRetryTime = _ZhoneCpeVoipMgcMaximumRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 14),
    _ZhoneCpeVoipMgcMaximumRetryTime_Type()
)
zhoneCpeVoipMgcMaximumRetryTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipMgcMaximumRetryTime.setStatus("current")


class _ZhoneCpeVoipMgcMaximumRetryAttempts_Type(Integer32):
    """Custom type zhoneCpeVoipMgcMaximumRetryAttempts based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneCpeVoipMgcMaximumRetryAttempts_Type.__name__ = "Integer32"
_ZhoneCpeVoipMgcMaximumRetryAttempts_Object = MibTableColumn
zhoneCpeVoipMgcMaximumRetryAttempts = _ZhoneCpeVoipMgcMaximumRetryAttempts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 15),
    _ZhoneCpeVoipMgcMaximumRetryAttempts_Type()
)
zhoneCpeVoipMgcMaximumRetryAttempts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipMgcMaximumRetryAttempts.setStatus("current")


class _ZhoneCpeVoipMgcServiceChangeDelay_Type(Integer32):
    """Custom type zhoneCpeVoipMgcServiceChangeDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneCpeVoipMgcServiceChangeDelay_Type.__name__ = "Integer32"
_ZhoneCpeVoipMgcServiceChangeDelay_Object = MibTableColumn
zhoneCpeVoipMgcServiceChangeDelay = _ZhoneCpeVoipMgcServiceChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 16),
    _ZhoneCpeVoipMgcServiceChangeDelay_Type()
)
zhoneCpeVoipMgcServiceChangeDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipMgcServiceChangeDelay.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeVoipMgcServiceChangeDelay.setUnits("seconds")


class _ZhoneCpeVoipMgcTerminationIdBase_Type(OctetString):
    """Custom type zhoneCpeVoipMgcTerminationIdBase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_ZhoneCpeVoipMgcTerminationIdBase_Type.__name__ = "OctetString"
_ZhoneCpeVoipMgcTerminationIdBase_Object = MibTableColumn
zhoneCpeVoipMgcTerminationIdBase = _ZhoneCpeVoipMgcTerminationIdBase_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 17),
    _ZhoneCpeVoipMgcTerminationIdBase_Type()
)
zhoneCpeVoipMgcTerminationIdBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipMgcTerminationIdBase.setStatus("current")


class _ZhoneCpeVoipReleaseTimer_Type(Integer32):
    """Custom type zhoneCpeVoipReleaseTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneCpeVoipReleaseTimer_Type.__name__ = "Integer32"
_ZhoneCpeVoipReleaseTimer_Object = MibTableColumn
zhoneCpeVoipReleaseTimer = _ZhoneCpeVoipReleaseTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 18),
    _ZhoneCpeVoipReleaseTimer_Type()
)
zhoneCpeVoipReleaseTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipReleaseTimer.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeVoipReleaseTimer.setUnits("seconds")


class _ZhoneCpeVoipRohTimer_Type(Integer32):
    """Custom type zhoneCpeVoipRohTimer based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneCpeVoipRohTimer_Type.__name__ = "Integer32"
_ZhoneCpeVoipRohTimer_Object = MibTableColumn
zhoneCpeVoipRohTimer = _ZhoneCpeVoipRohTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 19),
    _ZhoneCpeVoipRohTimer_Type()
)
zhoneCpeVoipRohTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipRohTimer.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeVoipRohTimer.setUnits("seconds")


class _ZhoneCpeVoipDscpMark_Type(Integer32):
    """Custom type zhoneCpeVoipDscpMark based on Integer32"""
    defaultValue = 46

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneCpeVoipDscpMark_Type.__name__ = "Integer32"
_ZhoneCpeVoipDscpMark_Object = MibTableColumn
zhoneCpeVoipDscpMark = _ZhoneCpeVoipDscpMark_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 20),
    _ZhoneCpeVoipDscpMark_Type()
)
zhoneCpeVoipDscpMark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipDscpMark.setStatus("current")


class _ZhoneCpeVoipPiggyBackEvents_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeVoipPiggyBackEvents based on ZhoneEnabledFlag"""


_ZhoneCpeVoipPiggyBackEvents_Object = MibTableColumn
zhoneCpeVoipPiggyBackEvents = _ZhoneCpeVoipPiggyBackEvents_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 21),
    _ZhoneCpeVoipPiggyBackEvents_Type()
)
zhoneCpeVoipPiggyBackEvents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipPiggyBackEvents.setStatus("current")


class _ZhoneCpeVoipOobToneEvents_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeVoipOobToneEvents based on ZhoneEnabledFlag"""


_ZhoneCpeVoipOobToneEvents_Object = MibTableColumn
zhoneCpeVoipOobToneEvents = _ZhoneCpeVoipOobToneEvents_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 22),
    _ZhoneCpeVoipOobToneEvents_Type()
)
zhoneCpeVoipOobToneEvents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipOobToneEvents.setStatus("current")


class _ZhoneCpeVoipOobDtmfEvents_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeVoipOobDtmfEvents based on ZhoneEnabledFlag"""


_ZhoneCpeVoipOobDtmfEvents_Object = MibTableColumn
zhoneCpeVoipOobDtmfEvents = _ZhoneCpeVoipOobDtmfEvents_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 23),
    _ZhoneCpeVoipOobDtmfEvents_Type()
)
zhoneCpeVoipOobDtmfEvents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipOobDtmfEvents.setStatus("current")


class _ZhoneCpeVoipOobCasEvents_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeVoipOobCasEvents based on ZhoneEnabledFlag"""


_ZhoneCpeVoipOobCasEvents_Object = MibTableColumn
zhoneCpeVoipOobCasEvents = _ZhoneCpeVoipOobCasEvents_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 24),
    _ZhoneCpeVoipOobCasEvents_Type()
)
zhoneCpeVoipOobCasEvents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipOobCasEvents.setStatus("current")


class _ZhoneCpeVoipPartialDialTimeout_Type(Integer32):
    """Custom type zhoneCpeVoipPartialDialTimeout based on Integer32"""
    defaultValue = 16000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneCpeVoipPartialDialTimeout_Type.__name__ = "Integer32"
_ZhoneCpeVoipPartialDialTimeout_Object = MibTableColumn
zhoneCpeVoipPartialDialTimeout = _ZhoneCpeVoipPartialDialTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 25),
    _ZhoneCpeVoipPartialDialTimeout_Type()
)
zhoneCpeVoipPartialDialTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipPartialDialTimeout.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeVoipPartialDialTimeout.setUnits("milli seconds")


class _ZhoneCpeVoipCriticalDialTimeout_Type(Integer32):
    """Custom type zhoneCpeVoipCriticalDialTimeout based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneCpeVoipCriticalDialTimeout_Type.__name__ = "Integer32"
_ZhoneCpeVoipCriticalDialTimeout_Object = MibTableColumn
zhoneCpeVoipCriticalDialTimeout = _ZhoneCpeVoipCriticalDialTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 26),
    _ZhoneCpeVoipCriticalDialTimeout_Type()
)
zhoneCpeVoipCriticalDialTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipCriticalDialTimeout.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeVoipCriticalDialTimeout.setUnits("milli seconds")
_ZhoneCpeVoipServerOutboundServer_Type = InetAddress
_ZhoneCpeVoipServerOutboundServer_Object = MibTableColumn
zhoneCpeVoipServerOutboundServer = _ZhoneCpeVoipServerOutboundServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 27),
    _ZhoneCpeVoipServerOutboundServer_Type()
)
zhoneCpeVoipServerOutboundServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipServerOutboundServer.setStatus("current")


class _ZhoneCpeVoipServerPortId_Type(Integer32):
    """Custom type zhoneCpeVoipServerPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_ZhoneCpeVoipServerPortId_Type.__name__ = "Integer32"
_ZhoneCpeVoipServerPortId_Object = MibTableColumn
zhoneCpeVoipServerPortId = _ZhoneCpeVoipServerPortId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 28),
    _ZhoneCpeVoipServerPortId_Type()
)
zhoneCpeVoipServerPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipServerPortId.setStatus("current")


class _ZhoneCpeVoipDtmfEventsPassingMethod_Type(Integer32):
    """Custom type zhoneCpeVoipDtmfEventsPassingMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rfc4733", 1),
          ("sipinfo", 2))
    )


_ZhoneCpeVoipDtmfEventsPassingMethod_Type.__name__ = "Integer32"
_ZhoneCpeVoipDtmfEventsPassingMethod_Object = MibTableColumn
zhoneCpeVoipDtmfEventsPassingMethod = _ZhoneCpeVoipDtmfEventsPassingMethod_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 29),
    _ZhoneCpeVoipDtmfEventsPassingMethod_Type()
)
zhoneCpeVoipDtmfEventsPassingMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipDtmfEventsPassingMethod.setStatus("current")


class _ZhoneCpeVoipCasEventsPassingMethod_Type(Integer32):
    """Custom type zhoneCpeVoipCasEventsPassingMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rfc4733", 1),
          ("sipinfo", 2))
    )


_ZhoneCpeVoipCasEventsPassingMethod_Type.__name__ = "Integer32"
_ZhoneCpeVoipCasEventsPassingMethod_Object = MibTableColumn
zhoneCpeVoipCasEventsPassingMethod = _ZhoneCpeVoipCasEventsPassingMethod_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 30),
    _ZhoneCpeVoipCasEventsPassingMethod_Type()
)
zhoneCpeVoipCasEventsPassingMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipCasEventsPassingMethod.setStatus("current")


class _ZhoneCpeVoipRtpDscp_Type(OctetString):
    """Custom type zhoneCpeVoipRtpDscp based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ZhoneCpeVoipRtpDscp_Type.__name__ = "OctetString"
_ZhoneCpeVoipRtpDscp_Object = MibTableColumn
zhoneCpeVoipRtpDscp = _ZhoneCpeVoipRtpDscp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 31),
    _ZhoneCpeVoipRtpDscp_Type()
)
zhoneCpeVoipRtpDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipRtpDscp.setStatus("current")


class _ZhoneCpeVoipSignalingDscp_Type(OctetString):
    """Custom type zhoneCpeVoipSignalingDscp based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ZhoneCpeVoipSignalingDscp_Type.__name__ = "OctetString"
_ZhoneCpeVoipSignalingDscp_Object = MibTableColumn
zhoneCpeVoipSignalingDscp = _ZhoneCpeVoipSignalingDscp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 32),
    _ZhoneCpeVoipSignalingDscp_Type()
)
zhoneCpeVoipSignalingDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipSignalingDscp.setStatus("current")


class _ZhoneCpeVoipSipRegRetryTime_Type(Unsigned32):
    """Custom type zhoneCpeVoipSipRegRetryTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeVoipSipRegRetryTime_Type.__name__ = "Unsigned32"
_ZhoneCpeVoipSipRegRetryTime_Object = MibTableColumn
zhoneCpeVoipSipRegRetryTime = _ZhoneCpeVoipSipRegRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 33),
    _ZhoneCpeVoipSipRegRetryTime_Type()
)
zhoneCpeVoipSipRegRetryTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipSipRegRetryTime.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeVoipSipRegRetryTime.setUnits("seconds")


class _ZhoneCpeVoipMgcpClientAddressMode_Type(Integer32):
    """Custom type zhoneCpeVoipMgcpClientAddressMode based on Integer32"""
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
        *(("domainName", 3),
          ("ip", 1),
          ("ipBracketed", 2))
    )


_ZhoneCpeVoipMgcpClientAddressMode_Type.__name__ = "Integer32"
_ZhoneCpeVoipMgcpClientAddressMode_Object = MibTableColumn
zhoneCpeVoipMgcpClientAddressMode = _ZhoneCpeVoipMgcpClientAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 34),
    _ZhoneCpeVoipMgcpClientAddressMode_Type()
)
zhoneCpeVoipMgcpClientAddressMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipMgcpClientAddressMode.setStatus("current")


class _ZhoneCpeVoipMgcpPersistentNotify_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeVoipMgcpPersistentNotify based on ZhoneEnabledFlag"""


_ZhoneCpeVoipMgcpPersistentNotify_Object = MibTableColumn
zhoneCpeVoipMgcpPersistentNotify = _ZhoneCpeVoipMgcpPersistentNotify_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 2, 2, 1, 35),
    _ZhoneCpeVoipMgcpPersistentNotify_Type()
)
zhoneCpeVoipMgcpPersistentNotify.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipMgcpPersistentNotify.setStatus("current")
_ZhoneCpeIpTable_Object = MibTable
zhoneCpeIpTable = _ZhoneCpeIpTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 3)
)
if mibBuilder.loadTexts:
    zhoneCpeIpTable.setStatus("current")
_ZhoneCpeIpEntry_Object = MibTableRow
zhoneCpeIpEntry = _ZhoneCpeIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 3, 1)
)
zhoneCpeIpEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeIfIndex"),
    (0, "Zhone-CPE-MIB", "zhoneCpeIpServiceType"),
)
if mibBuilder.loadTexts:
    zhoneCpeIpEntry.setStatus("current")
_ZhoneCpeIfIndex_Type = InterfaceIndex
_ZhoneCpeIfIndex_Object = MibTableColumn
zhoneCpeIfIndex = _ZhoneCpeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 3, 1, 1),
    _ZhoneCpeIfIndex_Type()
)
zhoneCpeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeIfIndex.setStatus("current")


class _ZhoneCpeIpServiceType_Type(Integer32):
    """Custom type zhoneCpeIpServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pwe", 2),
          ("voip", 1),
          ("wifi", 3))
    )


_ZhoneCpeIpServiceType_Type.__name__ = "Integer32"
_ZhoneCpeIpServiceType_Object = MibTableColumn
zhoneCpeIpServiceType = _ZhoneCpeIpServiceType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 3, 1, 2),
    _ZhoneCpeIpServiceType_Type()
)
zhoneCpeIpServiceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeIpServiceType.setStatus("current")


class _ZhoneCpeIpRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpeIpRowStatus based on ZhoneRowStatus"""


_ZhoneCpeIpRowStatus_Object = MibTableColumn
zhoneCpeIpRowStatus = _ZhoneCpeIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 3, 1, 3),
    _ZhoneCpeIpRowStatus_Type()
)
zhoneCpeIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeIpRowStatus.setStatus("current")
_ZhoneCpeHostIp_Type = IpAddress
_ZhoneCpeHostIp_Object = MibTableColumn
zhoneCpeHostIp = _ZhoneCpeHostIp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 3, 1, 4),
    _ZhoneCpeHostIp_Type()
)
zhoneCpeHostIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeHostIp.setStatus("current")


class _ZhoneCpeIpServerProfileIndex_Type(Integer32):
    """Custom type zhoneCpeIpServerProfileIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeIpServerProfileIndex_Type.__name__ = "Integer32"
_ZhoneCpeIpServerProfileIndex_Object = MibTableColumn
zhoneCpeIpServerProfileIndex = _ZhoneCpeIpServerProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 3, 1, 5),
    _ZhoneCpeIpServerProfileIndex_Type()
)
zhoneCpeIpServerProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeIpServerProfileIndex.setStatus("current")
_ZhoneCpeIpServer_ObjectIdentity = ObjectIdentity
zhoneCpeIpServer = _ZhoneCpeIpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 4)
)
if mibBuilder.loadTexts:
    zhoneCpeIpServer.setStatus("current")
_ZhoneCpeIpServerIndexNext_Type = Integer32
_ZhoneCpeIpServerIndexNext_Object = MibScalar
zhoneCpeIpServerIndexNext = _ZhoneCpeIpServerIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 4, 2),
    _ZhoneCpeIpServerIndexNext_Type()
)
zhoneCpeIpServerIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeIpServerIndexNext.setStatus("current")
_ZhoneCpeIpServerTable_Object = MibTable
zhoneCpeIpServerTable = _ZhoneCpeIpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 4, 3)
)
if mibBuilder.loadTexts:
    zhoneCpeIpServerTable.setStatus("current")
_ZhoneCpeIpServerEntry_Object = MibTableRow
zhoneCpeIpServerEntry = _ZhoneCpeIpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 4, 3, 1)
)
zhoneCpeIpServerEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeIpServerIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeIpServerEntry.setStatus("current")


class _ZhoneCpeIpServerIndex_Type(Unsigned32):
    """Custom type zhoneCpeIpServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeIpServerIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeIpServerIndex_Object = MibTableColumn
zhoneCpeIpServerIndex = _ZhoneCpeIpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 4, 3, 1, 1),
    _ZhoneCpeIpServerIndex_Type()
)
zhoneCpeIpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeIpServerIndex.setStatus("current")


class _ZhoneCpeIpServerRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpeIpServerRowStatus based on ZhoneRowStatus"""


_ZhoneCpeIpServerRowStatus_Object = MibTableColumn
zhoneCpeIpServerRowStatus = _ZhoneCpeIpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 4, 3, 1, 2),
    _ZhoneCpeIpServerRowStatus_Type()
)
zhoneCpeIpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeIpServerRowStatus.setStatus("current")
_ZhoneCpeIpServerProfileName_Type = ZhoneAdminString
_ZhoneCpeIpServerProfileName_Object = MibTableColumn
zhoneCpeIpServerProfileName = _ZhoneCpeIpServerProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 4, 3, 1, 3),
    _ZhoneCpeIpServerProfileName_Type()
)
zhoneCpeIpServerProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeIpServerProfileName.setStatus("current")


class _ZhoneCpeIpServerHostIpOption_Type(Integer32):
    """Custom type zhoneCpeIpServerHostIpOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("static", 2))
    )


_ZhoneCpeIpServerHostIpOption_Type.__name__ = "Integer32"
_ZhoneCpeIpServerHostIpOption_Object = MibTableColumn
zhoneCpeIpServerHostIpOption = _ZhoneCpeIpServerHostIpOption_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 4, 3, 1, 4),
    _ZhoneCpeIpServerHostIpOption_Type()
)
zhoneCpeIpServerHostIpOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeIpServerHostIpOption.setStatus("current")


class _ZhoneCpeIpServerNetmask_Type(IpAddress):
    """Custom type zhoneCpeIpServerNetmask based on IpAddress"""
    defaultHexValue = "ffffff00"


_ZhoneCpeIpServerNetmask_Object = MibTableColumn
zhoneCpeIpServerNetmask = _ZhoneCpeIpServerNetmask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 4, 3, 1, 5),
    _ZhoneCpeIpServerNetmask_Type()
)
zhoneCpeIpServerNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeIpServerNetmask.setStatus("current")
_ZhoneCpeIpServerGateway_Type = IpAddress
_ZhoneCpeIpServerGateway_Object = MibTableColumn
zhoneCpeIpServerGateway = _ZhoneCpeIpServerGateway_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 4, 3, 1, 6),
    _ZhoneCpeIpServerGateway_Type()
)
zhoneCpeIpServerGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeIpServerGateway.setStatus("current")
_ZhoneCpeIpServerPrimaryDns_Type = IpAddress
_ZhoneCpeIpServerPrimaryDns_Object = MibTableColumn
zhoneCpeIpServerPrimaryDns = _ZhoneCpeIpServerPrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 4, 3, 1, 7),
    _ZhoneCpeIpServerPrimaryDns_Type()
)
zhoneCpeIpServerPrimaryDns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeIpServerPrimaryDns.setStatus("current")
_ZhoneCpeIpServerSecondaryDns_Type = IpAddress
_ZhoneCpeIpServerSecondaryDns_Object = MibTableColumn
zhoneCpeIpServerSecondaryDns = _ZhoneCpeIpServerSecondaryDns_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 4, 3, 1, 8),
    _ZhoneCpeIpServerSecondaryDns_Type()
)
zhoneCpeIpServerSecondaryDns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeIpServerSecondaryDns.setStatus("current")


class _ZhoneCpeIpServerFirewallAccess_Type(Bits):
    """Custom type zhoneCpeIpServerFirewallAccess based on Bits"""
    namedValues = NamedValues(
        *(("http", 0),
          ("ping", 1),
          ("snmp", 2),
          ("snmptrap", 3),
          ("ssh", 4),
          ("telnet", 5))
    )

_ZhoneCpeIpServerFirewallAccess_Type.__name__ = "Bits"
_ZhoneCpeIpServerFirewallAccess_Object = MibTableColumn
zhoneCpeIpServerFirewallAccess = _ZhoneCpeIpServerFirewallAccess_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 4, 3, 1, 9),
    _ZhoneCpeIpServerFirewallAccess_Type()
)
zhoneCpeIpServerFirewallAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeIpServerFirewallAccess.setStatus("current")


class _ZhoneCpeIpServerNat_Type(Integer32):
    """Custom type zhoneCpeIpServerNat based on Integer32"""
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
        *(("disabled", 3),
          ("napt", 2),
          ("nat", 1))
    )


_ZhoneCpeIpServerNat_Type.__name__ = "Integer32"
_ZhoneCpeIpServerNat_Object = MibTableColumn
zhoneCpeIpServerNat = _ZhoneCpeIpServerNat_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 4, 3, 1, 10),
    _ZhoneCpeIpServerNat_Type()
)
zhoneCpeIpServerNat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeIpServerNat.setStatus("current")


class _ZhoneCpeIpServerSecureForward_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeIpServerSecureForward based on ZhoneEnabledFlag"""


_ZhoneCpeIpServerSecureForward_Object = MibTableColumn
zhoneCpeIpServerSecureForward = _ZhoneCpeIpServerSecureForward_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 4, 3, 1, 11),
    _ZhoneCpeIpServerSecureForward_Type()
)
zhoneCpeIpServerSecureForward.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeIpServerSecureForward.setStatus("current")


class _ZhoneCpeIpServerIgmpFunction_Type(Integer32):
    """Custom type zhoneCpeIpServerIgmpFunction based on Integer32"""
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
        *(("none", 1),
          ("proxy", 3),
          ("snooping", 2),
          ("snoopingproxy", 4))
    )


_ZhoneCpeIpServerIgmpFunction_Type.__name__ = "Integer32"
_ZhoneCpeIpServerIgmpFunction_Object = MibTableColumn
zhoneCpeIpServerIgmpFunction = _ZhoneCpeIpServerIgmpFunction_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 4, 3, 1, 12),
    _ZhoneCpeIpServerIgmpFunction_Type()
)
zhoneCpeIpServerIgmpFunction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeIpServerIgmpFunction.setStatus("current")


class _ZhoneCpeIpServerDefaultIface_Type(TruthValue):
    """Custom type zhoneCpeIpServerDefaultIface based on TruthValue"""


_ZhoneCpeIpServerDefaultIface_Object = MibTableColumn
zhoneCpeIpServerDefaultIface = _ZhoneCpeIpServerDefaultIface_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 4, 3, 1, 13),
    _ZhoneCpeIpServerDefaultIface_Type()
)
zhoneCpeIpServerDefaultIface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeIpServerDefaultIface.setStatus("current")


class _ZhoneCpeIpServerDnsSrc_Type(TruthValue):
    """Custom type zhoneCpeIpServerDnsSrc based on TruthValue"""


_ZhoneCpeIpServerDnsSrc_Object = MibTableColumn
zhoneCpeIpServerDnsSrc = _ZhoneCpeIpServerDnsSrc_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 4, 3, 1, 14),
    _ZhoneCpeIpServerDnsSrc_Type()
)
zhoneCpeIpServerDnsSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeIpServerDnsSrc.setStatus("current")


class _ZhoneCpeIpServerDnsType_Type(Integer32):
    """Custom type zhoneCpeIpServerDnsType based on Integer32"""
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
        *(("default", 1),
          ("proxy", 3),
          ("static", 2))
    )


_ZhoneCpeIpServerDnsType_Type.__name__ = "Integer32"
_ZhoneCpeIpServerDnsType_Object = MibTableColumn
zhoneCpeIpServerDnsType = _ZhoneCpeIpServerDnsType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 4, 3, 1, 15),
    _ZhoneCpeIpServerDnsType_Type()
)
zhoneCpeIpServerDnsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeIpServerDnsType.setStatus("current")
_ZhoneCpeVoipFeatures_ObjectIdentity = ObjectIdentity
zhoneCpeVoipFeatures = _ZhoneCpeVoipFeatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 5)
)
if mibBuilder.loadTexts:
    zhoneCpeVoipFeatures.setStatus("current")
_ZhoneCpeVoipFeaturesIndexNext_Type = Integer32
_ZhoneCpeVoipFeaturesIndexNext_Object = MibScalar
zhoneCpeVoipFeaturesIndexNext = _ZhoneCpeVoipFeaturesIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 5, 1),
    _ZhoneCpeVoipFeaturesIndexNext_Type()
)
zhoneCpeVoipFeaturesIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeVoipFeaturesIndexNext.setStatus("current")
_ZhoneCpeVoipFeaturesTable_Object = MibTable
zhoneCpeVoipFeaturesTable = _ZhoneCpeVoipFeaturesTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 5, 2)
)
if mibBuilder.loadTexts:
    zhoneCpeVoipFeaturesTable.setStatus("current")
_ZhoneCpeVoipFeaturesEntry_Object = MibTableRow
zhoneCpeVoipFeaturesEntry = _ZhoneCpeVoipFeaturesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 5, 2, 1)
)
zhoneCpeVoipFeaturesEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeVoipFeaturesIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeVoipFeaturesEntry.setStatus("current")


class _ZhoneCpeVoipFeaturesIndex_Type(Unsigned32):
    """Custom type zhoneCpeVoipFeaturesIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeVoipFeaturesIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeVoipFeaturesIndex_Object = MibTableColumn
zhoneCpeVoipFeaturesIndex = _ZhoneCpeVoipFeaturesIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 5, 2, 1, 1),
    _ZhoneCpeVoipFeaturesIndex_Type()
)
zhoneCpeVoipFeaturesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeVoipFeaturesIndex.setStatus("current")


class _ZhoneCpeVoipFeaturesRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpeVoipFeaturesRowStatus based on ZhoneRowStatus"""


_ZhoneCpeVoipFeaturesRowStatus_Object = MibTableColumn
zhoneCpeVoipFeaturesRowStatus = _ZhoneCpeVoipFeaturesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 5, 2, 1, 2),
    _ZhoneCpeVoipFeaturesRowStatus_Type()
)
zhoneCpeVoipFeaturesRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipFeaturesRowStatus.setStatus("current")
_ZhoneCpeVoipFeaturesProfileName_Type = ZhoneAdminString
_ZhoneCpeVoipFeaturesProfileName_Object = MibTableColumn
zhoneCpeVoipFeaturesProfileName = _ZhoneCpeVoipFeaturesProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 5, 2, 1, 3),
    _ZhoneCpeVoipFeaturesProfileName_Type()
)
zhoneCpeVoipFeaturesProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipFeaturesProfileName.setStatus("current")


class _ZhoneCpeVoipFeaturesAnnouncementType_Type(Integer32):
    """Custom type zhoneCpeVoipFeaturesAnnouncementType based on Integer32"""
    defaultValue = 2

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
        *(("fastbusy", 3),
          ("notapplicable", 5),
          ("reordertone", 2),
          ("silence", 1),
          ("voice", 4))
    )


_ZhoneCpeVoipFeaturesAnnouncementType_Type.__name__ = "Integer32"
_ZhoneCpeVoipFeaturesAnnouncementType_Object = MibTableColumn
zhoneCpeVoipFeaturesAnnouncementType = _ZhoneCpeVoipFeaturesAnnouncementType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 5, 2, 1, 4),
    _ZhoneCpeVoipFeaturesAnnouncementType_Type()
)
zhoneCpeVoipFeaturesAnnouncementType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipFeaturesAnnouncementType.setStatus("current")


class _ZhoneCpeVoipCidFeatures_Type(Bits):
    """Custom type zhoneCpeVoipCidFeatures based on Bits"""
    namedValues = NamedValues(
        *(("anonymouscidblocking", 5),
          ("callingname", 1),
          ("callingnumber", 0),
          ("cidblocking", 2),
          ("cidname", 4),
          ("cidnumber", 3))
    )

_ZhoneCpeVoipCidFeatures_Type.__name__ = "Bits"
_ZhoneCpeVoipCidFeatures_Object = MibTableColumn
zhoneCpeVoipCidFeatures = _ZhoneCpeVoipCidFeatures_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 5, 2, 1, 5),
    _ZhoneCpeVoipCidFeatures_Type()
)
zhoneCpeVoipCidFeatures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipCidFeatures.setStatus("current")


class _ZhoneCpeVoipCallWaitingFeatures_Type(Bits):
    """Custom type zhoneCpeVoipCallWaitingFeatures based on Bits"""
    namedValues = NamedValues(
        *(("callwaiting", 0),
          ("cidannouncement", 1))
    )

_ZhoneCpeVoipCallWaitingFeatures_Type.__name__ = "Bits"
_ZhoneCpeVoipCallWaitingFeatures_Object = MibTableColumn
zhoneCpeVoipCallWaitingFeatures = _ZhoneCpeVoipCallWaitingFeatures_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 5, 2, 1, 6),
    _ZhoneCpeVoipCallWaitingFeatures_Type()
)
zhoneCpeVoipCallWaitingFeatures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipCallWaitingFeatures.setStatus("current")


class _ZhoneCpeVoipCallProgressOrTransferFeatures_Type(Bits):
    """Custom type zhoneCpeVoipCallProgressOrTransferFeatures based on Bits"""
    namedValues = NamedValues(
        *(("callhold", 2),
          ("callpark", 3),
          ("calltransfer", 1),
          ("donotdisturb", 4),
          ("emergencyhold", 6),
          ("flashonemergency", 5),
          ("sixway", 7),
          ("threeway", 0))
    )

_ZhoneCpeVoipCallProgressOrTransferFeatures_Type.__name__ = "Bits"
_ZhoneCpeVoipCallProgressOrTransferFeatures_Object = MibTableColumn
zhoneCpeVoipCallProgressOrTransferFeatures = _ZhoneCpeVoipCallProgressOrTransferFeatures_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 5, 2, 1, 7),
    _ZhoneCpeVoipCallProgressOrTransferFeatures_Type()
)
zhoneCpeVoipCallProgressOrTransferFeatures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipCallProgressOrTransferFeatures.setStatus("current")


class _ZhoneCpeVoipCallPresentationFeatures_Type(Bits):
    """Custom type zhoneCpeVoipCallPresentationFeatures based on Bits"""
    namedValues = NamedValues(
        *(("callfwd", 3),
          ("msgwaitspecialdialtone", 1),
          ("msgwaitsplashring", 0),
          ("msgwaitvisual", 2))
    )

_ZhoneCpeVoipCallPresentationFeatures_Type.__name__ = "Bits"
_ZhoneCpeVoipCallPresentationFeatures_Object = MibTableColumn
zhoneCpeVoipCallPresentationFeatures = _ZhoneCpeVoipCallPresentationFeatures_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 5, 2, 1, 8),
    _ZhoneCpeVoipCallPresentationFeatures_Type()
)
zhoneCpeVoipCallPresentationFeatures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipCallPresentationFeatures.setStatus("current")


class _ZhoneCpeVoipFeaturesHotLine_Type(Integer32):
    """Custom type zhoneCpeVoipFeaturesHotLine based on Integer32"""
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
        *(("disabled", 1),
          ("hot", 2),
          ("warm", 3))
    )


_ZhoneCpeVoipFeaturesHotLine_Type.__name__ = "Integer32"
_ZhoneCpeVoipFeaturesHotLine_Object = MibTableColumn
zhoneCpeVoipFeaturesHotLine = _ZhoneCpeVoipFeaturesHotLine_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 5, 2, 1, 9),
    _ZhoneCpeVoipFeaturesHotLine_Type()
)
zhoneCpeVoipFeaturesHotLine.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipFeaturesHotLine.setStatus("current")


class _ZhoneCpeVoipFeaturesHotLineNumber_Type(OctetString):
    """Custom type zhoneCpeVoipFeaturesHotLineNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ZhoneCpeVoipFeaturesHotLineNumber_Type.__name__ = "OctetString"
_ZhoneCpeVoipFeaturesHotLineNumber_Object = MibTableColumn
zhoneCpeVoipFeaturesHotLineNumber = _ZhoneCpeVoipFeaturesHotLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 5, 2, 1, 10),
    _ZhoneCpeVoipFeaturesHotLineNumber_Type()
)
zhoneCpeVoipFeaturesHotLineNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipFeaturesHotLineNumber.setStatus("current")


class _ZhoneCpeVoipFeaturesWarmLineTimer_Type(Unsigned32):
    """Custom type zhoneCpeVoipFeaturesWarmLineTimer based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 30000),
    )


_ZhoneCpeVoipFeaturesWarmLineTimer_Type.__name__ = "Unsigned32"
_ZhoneCpeVoipFeaturesWarmLineTimer_Object = MibTableColumn
zhoneCpeVoipFeaturesWarmLineTimer = _ZhoneCpeVoipFeaturesWarmLineTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 5, 2, 1, 11),
    _ZhoneCpeVoipFeaturesWarmLineTimer_Type()
)
zhoneCpeVoipFeaturesWarmLineTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipFeaturesWarmLineTimer.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeVoipFeaturesWarmLineTimer.setUnits("ms")
_ZhoneCpeVoipMedia_ObjectIdentity = ObjectIdentity
zhoneCpeVoipMedia = _ZhoneCpeVoipMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 6)
)
if mibBuilder.loadTexts:
    zhoneCpeVoipMedia.setStatus("current")
_ZhoneCpeVoipMediaIndexNext_Type = Integer32
_ZhoneCpeVoipMediaIndexNext_Object = MibScalar
zhoneCpeVoipMediaIndexNext = _ZhoneCpeVoipMediaIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 6, 1),
    _ZhoneCpeVoipMediaIndexNext_Type()
)
zhoneCpeVoipMediaIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeVoipMediaIndexNext.setStatus("current")
_ZhoneCpeVoipMediaTable_Object = MibTable
zhoneCpeVoipMediaTable = _ZhoneCpeVoipMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 6, 2)
)
if mibBuilder.loadTexts:
    zhoneCpeVoipMediaTable.setStatus("current")
_ZhoneCpeVoipMediaEntry_Object = MibTableRow
zhoneCpeVoipMediaEntry = _ZhoneCpeVoipMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 6, 2, 1)
)
zhoneCpeVoipMediaEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeVoipMediaIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeVoipMediaEntry.setStatus("current")


class _ZhoneCpeVoipMediaIndex_Type(Unsigned32):
    """Custom type zhoneCpeVoipMediaIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeVoipMediaIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeVoipMediaIndex_Object = MibTableColumn
zhoneCpeVoipMediaIndex = _ZhoneCpeVoipMediaIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 6, 2, 1, 1),
    _ZhoneCpeVoipMediaIndex_Type()
)
zhoneCpeVoipMediaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeVoipMediaIndex.setStatus("current")


class _ZhoneCpeVoipMediaRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpeVoipMediaRowStatus based on ZhoneRowStatus"""


_ZhoneCpeVoipMediaRowStatus_Object = MibTableColumn
zhoneCpeVoipMediaRowStatus = _ZhoneCpeVoipMediaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 6, 2, 1, 2),
    _ZhoneCpeVoipMediaRowStatus_Type()
)
zhoneCpeVoipMediaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipMediaRowStatus.setStatus("current")
_ZhoneCpeVoipMediaProfileName_Type = ZhoneAdminString
_ZhoneCpeVoipMediaProfileName_Object = MibTableColumn
zhoneCpeVoipMediaProfileName = _ZhoneCpeVoipMediaProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 6, 2, 1, 3),
    _ZhoneCpeVoipMediaProfileName_Type()
)
zhoneCpeVoipMediaProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipMediaProfileName.setStatus("current")


class _ZhoneCpeVoipMediaEchoCancel_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeVoipMediaEchoCancel based on ZhoneEnabledFlag"""


_ZhoneCpeVoipMediaEchoCancel_Object = MibTableColumn
zhoneCpeVoipMediaEchoCancel = _ZhoneCpeVoipMediaEchoCancel_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 6, 2, 1, 4),
    _ZhoneCpeVoipMediaEchoCancel_Type()
)
zhoneCpeVoipMediaEchoCancel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipMediaEchoCancel.setStatus("current")


class _ZhoneCpeVoipFaxMode_Type(Integer32):
    """Custom type zhoneCpeVoipFaxMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passthrough", 1),
          ("t38", 2))
    )


_ZhoneCpeVoipFaxMode_Type.__name__ = "Integer32"
_ZhoneCpeVoipFaxMode_Object = MibTableColumn
zhoneCpeVoipFaxMode = _ZhoneCpeVoipFaxMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 6, 2, 1, 5),
    _ZhoneCpeVoipFaxMode_Type()
)
zhoneCpeVoipFaxMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipFaxMode.setStatus("current")


class _ZhoneCpeVoipCodecSelectionFirstOrder_Type(Integer32):
    """Custom type zhoneCpeVoipCodecSelectionFirstOrder based on Integer32"""
    defaultValue = 1

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
        *(("cn", 12),
          ("dvi411", 15),
          ("dvi422", 16),
          ("dvi4eightKHz", 4),
          ("dvi4sixteenKHz", 5),
          ("g722", 8),
          ("g723", 3),
          ("g728", 14),
          ("g729", 17),
          ("gsm", 2),
          ("l16onechannel", 10),
          ("l16twochannels", 9),
          ("lpc", 6),
          ("mpa", 13),
          ("pcma", 7),
          ("pcmu", 1),
          ("qcelp", 11))
    )


_ZhoneCpeVoipCodecSelectionFirstOrder_Type.__name__ = "Integer32"
_ZhoneCpeVoipCodecSelectionFirstOrder_Object = MibTableColumn
zhoneCpeVoipCodecSelectionFirstOrder = _ZhoneCpeVoipCodecSelectionFirstOrder_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 6, 2, 1, 6),
    _ZhoneCpeVoipCodecSelectionFirstOrder_Type()
)
zhoneCpeVoipCodecSelectionFirstOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipCodecSelectionFirstOrder.setStatus("current")


class _ZhoneCpeVoipPacketPeriodSelectionFirstOrder_Type(Integer32):
    """Custom type zhoneCpeVoipPacketPeriodSelectionFirstOrder based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_ZhoneCpeVoipPacketPeriodSelectionFirstOrder_Type.__name__ = "Integer32"
_ZhoneCpeVoipPacketPeriodSelectionFirstOrder_Object = MibTableColumn
zhoneCpeVoipPacketPeriodSelectionFirstOrder = _ZhoneCpeVoipPacketPeriodSelectionFirstOrder_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 6, 2, 1, 7),
    _ZhoneCpeVoipPacketPeriodSelectionFirstOrder_Type()
)
zhoneCpeVoipPacketPeriodSelectionFirstOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipPacketPeriodSelectionFirstOrder.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeVoipPacketPeriodSelectionFirstOrder.setUnits("milli seconds")


class _ZhoneCpeVoipSilenceSuppressionFirstOrder_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeVoipSilenceSuppressionFirstOrder based on ZhoneEnabledFlag"""


_ZhoneCpeVoipSilenceSuppressionFirstOrder_Object = MibTableColumn
zhoneCpeVoipSilenceSuppressionFirstOrder = _ZhoneCpeVoipSilenceSuppressionFirstOrder_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 6, 2, 1, 8),
    _ZhoneCpeVoipSilenceSuppressionFirstOrder_Type()
)
zhoneCpeVoipSilenceSuppressionFirstOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipSilenceSuppressionFirstOrder.setStatus("current")


class _ZhoneCpeVoipCodecSelectionSecondOrder_Type(Integer32):
    """Custom type zhoneCpeVoipCodecSelectionSecondOrder based on Integer32"""
    defaultValue = 1

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
        *(("cn", 12),
          ("dvi411", 15),
          ("dvi422", 16),
          ("dvi4eightKHz", 4),
          ("dvi4sixteenKHz", 5),
          ("g722", 8),
          ("g723", 3),
          ("g728", 14),
          ("g729", 17),
          ("gsm", 2),
          ("l16onechannel", 10),
          ("l16twochannels", 9),
          ("lpc", 6),
          ("mpa", 13),
          ("pcma", 7),
          ("pcmu", 1),
          ("qcelp", 11))
    )


_ZhoneCpeVoipCodecSelectionSecondOrder_Type.__name__ = "Integer32"
_ZhoneCpeVoipCodecSelectionSecondOrder_Object = MibTableColumn
zhoneCpeVoipCodecSelectionSecondOrder = _ZhoneCpeVoipCodecSelectionSecondOrder_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 6, 2, 1, 9),
    _ZhoneCpeVoipCodecSelectionSecondOrder_Type()
)
zhoneCpeVoipCodecSelectionSecondOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipCodecSelectionSecondOrder.setStatus("current")


class _ZhoneCpeVoipPacketPeriodSelectionSecondOrder_Type(Integer32):
    """Custom type zhoneCpeVoipPacketPeriodSelectionSecondOrder based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_ZhoneCpeVoipPacketPeriodSelectionSecondOrder_Type.__name__ = "Integer32"
_ZhoneCpeVoipPacketPeriodSelectionSecondOrder_Object = MibTableColumn
zhoneCpeVoipPacketPeriodSelectionSecondOrder = _ZhoneCpeVoipPacketPeriodSelectionSecondOrder_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 6, 2, 1, 10),
    _ZhoneCpeVoipPacketPeriodSelectionSecondOrder_Type()
)
zhoneCpeVoipPacketPeriodSelectionSecondOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipPacketPeriodSelectionSecondOrder.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeVoipPacketPeriodSelectionSecondOrder.setUnits("milli seconds")


class _ZhoneCpeVoipSilenceSuppressionSecondOrder_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeVoipSilenceSuppressionSecondOrder based on ZhoneEnabledFlag"""


_ZhoneCpeVoipSilenceSuppressionSecondOrder_Object = MibTableColumn
zhoneCpeVoipSilenceSuppressionSecondOrder = _ZhoneCpeVoipSilenceSuppressionSecondOrder_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 6, 2, 1, 11),
    _ZhoneCpeVoipSilenceSuppressionSecondOrder_Type()
)
zhoneCpeVoipSilenceSuppressionSecondOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipSilenceSuppressionSecondOrder.setStatus("current")


class _ZhoneCpeVoipCodecSelectionThirdOrder_Type(Integer32):
    """Custom type zhoneCpeVoipCodecSelectionThirdOrder based on Integer32"""
    defaultValue = 1

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
        *(("cn", 12),
          ("dvi411", 15),
          ("dvi422", 16),
          ("dvi4eightKHz", 4),
          ("dvi4sixteenKHz", 5),
          ("g722", 8),
          ("g723", 3),
          ("g728", 14),
          ("g729", 17),
          ("gsm", 2),
          ("l16onechannel", 10),
          ("l16twochannels", 9),
          ("lpc", 6),
          ("mpa", 13),
          ("pcma", 7),
          ("pcmu", 1),
          ("qcelp", 11))
    )


_ZhoneCpeVoipCodecSelectionThirdOrder_Type.__name__ = "Integer32"
_ZhoneCpeVoipCodecSelectionThirdOrder_Object = MibTableColumn
zhoneCpeVoipCodecSelectionThirdOrder = _ZhoneCpeVoipCodecSelectionThirdOrder_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 6, 2, 1, 12),
    _ZhoneCpeVoipCodecSelectionThirdOrder_Type()
)
zhoneCpeVoipCodecSelectionThirdOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipCodecSelectionThirdOrder.setStatus("current")


class _ZhoneCpeVoipPacketPeriodSelectionThirdOrder_Type(Integer32):
    """Custom type zhoneCpeVoipPacketPeriodSelectionThirdOrder based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_ZhoneCpeVoipPacketPeriodSelectionThirdOrder_Type.__name__ = "Integer32"
_ZhoneCpeVoipPacketPeriodSelectionThirdOrder_Object = MibTableColumn
zhoneCpeVoipPacketPeriodSelectionThirdOrder = _ZhoneCpeVoipPacketPeriodSelectionThirdOrder_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 6, 2, 1, 13),
    _ZhoneCpeVoipPacketPeriodSelectionThirdOrder_Type()
)
zhoneCpeVoipPacketPeriodSelectionThirdOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipPacketPeriodSelectionThirdOrder.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeVoipPacketPeriodSelectionThirdOrder.setUnits("milli seconds")


class _ZhoneCpeVoipSilenceSuppressionThirdOrder_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeVoipSilenceSuppressionThirdOrder based on ZhoneEnabledFlag"""


_ZhoneCpeVoipSilenceSuppressionThirdOrder_Object = MibTableColumn
zhoneCpeVoipSilenceSuppressionThirdOrder = _ZhoneCpeVoipSilenceSuppressionThirdOrder_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 6, 2, 1, 14),
    _ZhoneCpeVoipSilenceSuppressionThirdOrder_Type()
)
zhoneCpeVoipSilenceSuppressionThirdOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipSilenceSuppressionThirdOrder.setStatus("current")


class _ZhoneCpeVoipCodecSelectionFourthOrder_Type(Integer32):
    """Custom type zhoneCpeVoipCodecSelectionFourthOrder based on Integer32"""
    defaultValue = 1

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
        *(("cn", 12),
          ("dvi411", 15),
          ("dvi422", 16),
          ("dvi4eightKHz", 4),
          ("dvi4sixteenKHz", 5),
          ("g722", 8),
          ("g723", 3),
          ("g728", 14),
          ("g729", 17),
          ("gsm", 2),
          ("l16onechannel", 10),
          ("l16twochannels", 9),
          ("lpc", 6),
          ("mpa", 13),
          ("pcma", 7),
          ("pcmu", 1),
          ("qcelp", 11))
    )


_ZhoneCpeVoipCodecSelectionFourthOrder_Type.__name__ = "Integer32"
_ZhoneCpeVoipCodecSelectionFourthOrder_Object = MibTableColumn
zhoneCpeVoipCodecSelectionFourthOrder = _ZhoneCpeVoipCodecSelectionFourthOrder_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 6, 2, 1, 15),
    _ZhoneCpeVoipCodecSelectionFourthOrder_Type()
)
zhoneCpeVoipCodecSelectionFourthOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipCodecSelectionFourthOrder.setStatus("current")


class _ZhoneCpeVoipPacketPeriodSelectionFourthOrder_Type(Integer32):
    """Custom type zhoneCpeVoipPacketPeriodSelectionFourthOrder based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_ZhoneCpeVoipPacketPeriodSelectionFourthOrder_Type.__name__ = "Integer32"
_ZhoneCpeVoipPacketPeriodSelectionFourthOrder_Object = MibTableColumn
zhoneCpeVoipPacketPeriodSelectionFourthOrder = _ZhoneCpeVoipPacketPeriodSelectionFourthOrder_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 6, 2, 1, 16),
    _ZhoneCpeVoipPacketPeriodSelectionFourthOrder_Type()
)
zhoneCpeVoipPacketPeriodSelectionFourthOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipPacketPeriodSelectionFourthOrder.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeVoipPacketPeriodSelectionFourthOrder.setUnits("milli seconds")


class _ZhoneCpeVoipSilenceSuppressionFourthOrder_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeVoipSilenceSuppressionFourthOrder based on ZhoneEnabledFlag"""


_ZhoneCpeVoipSilenceSuppressionFourthOrder_Object = MibTableColumn
zhoneCpeVoipSilenceSuppressionFourthOrder = _ZhoneCpeVoipSilenceSuppressionFourthOrder_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 6, 2, 1, 17),
    _ZhoneCpeVoipSilenceSuppressionFourthOrder_Type()
)
zhoneCpeVoipSilenceSuppressionFourthOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipSilenceSuppressionFourthOrder.setStatus("current")
_ZhoneCpeVoipSubscriberTable_Object = MibTable
zhoneCpeVoipSubscriberTable = _ZhoneCpeVoipSubscriberTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 7)
)
if mibBuilder.loadTexts:
    zhoneCpeVoipSubscriberTable.setStatus("current")
_ZhoneCpeVoipSubscriberEntry_Object = MibTableRow
zhoneCpeVoipSubscriberEntry = _ZhoneCpeVoipSubscriberEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 7, 1)
)
zhoneCpeVoipSubscriberEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeIfIndex"),
    (0, "Zhone-CPE-MIB", "zhoneCpeVoipSubscriberPortNumber"),
)
if mibBuilder.loadTexts:
    zhoneCpeVoipSubscriberEntry.setStatus("current")


class _ZhoneCpeVoipSubscriberPortNumber_Type(Unsigned32):
    """Custom type zhoneCpeVoipSubscriberPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeVoipSubscriberPortNumber_Type.__name__ = "Unsigned32"
_ZhoneCpeVoipSubscriberPortNumber_Object = MibTableColumn
zhoneCpeVoipSubscriberPortNumber = _ZhoneCpeVoipSubscriberPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 7, 1, 1),
    _ZhoneCpeVoipSubscriberPortNumber_Type()
)
zhoneCpeVoipSubscriberPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeVoipSubscriberPortNumber.setStatus("current")


class _ZhoneCpeVoipSubscriberRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpeVoipSubscriberRowStatus based on ZhoneRowStatus"""


_ZhoneCpeVoipSubscriberRowStatus_Object = MibTableColumn
zhoneCpeVoipSubscriberRowStatus = _ZhoneCpeVoipSubscriberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 7, 1, 2),
    _ZhoneCpeVoipSubscriberRowStatus_Type()
)
zhoneCpeVoipSubscriberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipSubscriberRowStatus.setStatus("current")


class _ZhoneCpeVoipSubscriberAdminState_Type(ZhoneAdminState):
    """Custom type zhoneCpeVoipSubscriberAdminState based on ZhoneAdminState"""
    defaultValue = 1


_ZhoneCpeVoipSubscriberAdminState_Object = MibTableColumn
zhoneCpeVoipSubscriberAdminState = _ZhoneCpeVoipSubscriberAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 7, 1, 3),
    _ZhoneCpeVoipSubscriberAdminState_Type()
)
zhoneCpeVoipSubscriberAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipSubscriberAdminState.setStatus("current")
_ZhoneCpeVoipSubscriberDialNumber_Type = ZhoneAdminString
_ZhoneCpeVoipSubscriberDialNumber_Object = MibTableColumn
zhoneCpeVoipSubscriberDialNumber = _ZhoneCpeVoipSubscriberDialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 7, 1, 4),
    _ZhoneCpeVoipSubscriberDialNumber_Type()
)
zhoneCpeVoipSubscriberDialNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipSubscriberDialNumber.setStatus("current")


class _ZhoneCpeVoipSubscriberDisplayName_Type(OctetString):
    """Custom type zhoneCpeVoipSubscriberDisplayName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_ZhoneCpeVoipSubscriberDisplayName_Type.__name__ = "OctetString"
_ZhoneCpeVoipSubscriberDisplayName_Object = MibTableColumn
zhoneCpeVoipSubscriberDisplayName = _ZhoneCpeVoipSubscriberDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 7, 1, 5),
    _ZhoneCpeVoipSubscriberDisplayName_Type()
)
zhoneCpeVoipSubscriberDisplayName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipSubscriberDisplayName.setStatus("current")


class _ZhoneCpeVoipSubscriberUserName_Type(OctetString):
    """Custom type zhoneCpeVoipSubscriberUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_ZhoneCpeVoipSubscriberUserName_Type.__name__ = "OctetString"
_ZhoneCpeVoipSubscriberUserName_Object = MibTableColumn
zhoneCpeVoipSubscriberUserName = _ZhoneCpeVoipSubscriberUserName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 7, 1, 6),
    _ZhoneCpeVoipSubscriberUserName_Type()
)
zhoneCpeVoipSubscriberUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipSubscriberUserName.setStatus("current")


class _ZhoneCpeVoipSubscriberPassword_Type(OctetString):
    """Custom type zhoneCpeVoipSubscriberPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZhoneCpeVoipSubscriberPassword_Type.__name__ = "OctetString"
_ZhoneCpeVoipSubscriberPassword_Object = MibTableColumn
zhoneCpeVoipSubscriberPassword = _ZhoneCpeVoipSubscriberPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 7, 1, 7),
    _ZhoneCpeVoipSubscriberPassword_Type()
)
zhoneCpeVoipSubscriberPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipSubscriberPassword.setStatus("current")


class _ZhoneCpeVoipSubscriberImpedance_Type(Integer32):
    """Custom type zhoneCpeVoipSubscriberImpedance based on Integer32"""
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
        *(("complex1", 3),
          ("complex2", 4),
          ("complex3", 5),
          ("ohm600", 1),
          ("ohm900", 2))
    )


_ZhoneCpeVoipSubscriberImpedance_Type.__name__ = "Integer32"
_ZhoneCpeVoipSubscriberImpedance_Object = MibTableColumn
zhoneCpeVoipSubscriberImpedance = _ZhoneCpeVoipSubscriberImpedance_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 7, 1, 8),
    _ZhoneCpeVoipSubscriberImpedance_Type()
)
zhoneCpeVoipSubscriberImpedance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipSubscriberImpedance.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeVoipSubscriberImpedance.setUnits("ohm")


class _ZhoneCpeVoipSubscriberRxGain_Type(Integer32):
    """Custom type zhoneCpeVoipSubscriberRxGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 6),
    )


_ZhoneCpeVoipSubscriberRxGain_Type.__name__ = "Integer32"
_ZhoneCpeVoipSubscriberRxGain_Object = MibTableColumn
zhoneCpeVoipSubscriberRxGain = _ZhoneCpeVoipSubscriberRxGain_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 7, 1, 9),
    _ZhoneCpeVoipSubscriberRxGain_Type()
)
zhoneCpeVoipSubscriberRxGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipSubscriberRxGain.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeVoipSubscriberRxGain.setUnits("dB")


class _ZhoneCpeVoipSubscriberTxGain_Type(Integer32):
    """Custom type zhoneCpeVoipSubscriberTxGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 6),
    )


_ZhoneCpeVoipSubscriberTxGain_Type.__name__ = "Integer32"
_ZhoneCpeVoipSubscriberTxGain_Object = MibTableColumn
zhoneCpeVoipSubscriberTxGain = _ZhoneCpeVoipSubscriberTxGain_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 7, 1, 10),
    _ZhoneCpeVoipSubscriberTxGain_Type()
)
zhoneCpeVoipSubscriberTxGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipSubscriberTxGain.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeVoipSubscriberTxGain.setUnits("dB")


class _ZhoneCpeVoipSubscriberTransmissionPath_Type(Integer32):
    """Custom type zhoneCpeVoipSubscriberTransmissionPath based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fulltimeonhookxmit", 1),
          ("parttimeonhookxmit", 2))
    )


_ZhoneCpeVoipSubscriberTransmissionPath_Type.__name__ = "Integer32"
_ZhoneCpeVoipSubscriberTransmissionPath_Object = MibTableColumn
zhoneCpeVoipSubscriberTransmissionPath = _ZhoneCpeVoipSubscriberTransmissionPath_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 7, 1, 11),
    _ZhoneCpeVoipSubscriberTransmissionPath_Type()
)
zhoneCpeVoipSubscriberTransmissionPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipSubscriberTransmissionPath.setStatus("current")


class _ZhoneCpeVoipSubscriberSignallingCode_Type(Integer32):
    """Custom type zhoneCpeVoipSubscriberSignallingCode based on Integer32"""
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
        *(("coinfirst", 4),
          ("dialtonefirst", 5),
          ("groundstart", 2),
          ("loopreversebattery", 3),
          ("loopstart", 1),
          ("multiparty", 6))
    )


_ZhoneCpeVoipSubscriberSignallingCode_Type.__name__ = "Integer32"
_ZhoneCpeVoipSubscriberSignallingCode_Object = MibTableColumn
zhoneCpeVoipSubscriberSignallingCode = _ZhoneCpeVoipSubscriberSignallingCode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 7, 1, 12),
    _ZhoneCpeVoipSubscriberSignallingCode_Type()
)
zhoneCpeVoipSubscriberSignallingCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipSubscriberSignallingCode.setStatus("current")


class _ZhoneCpeVoipServerProfileIndex_Type(Unsigned32):
    """Custom type zhoneCpeVoipServerProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeVoipServerProfileIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeVoipServerProfileIndex_Object = MibTableColumn
zhoneCpeVoipServerProfileIndex = _ZhoneCpeVoipServerProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 7, 1, 13),
    _ZhoneCpeVoipServerProfileIndex_Type()
)
zhoneCpeVoipServerProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipServerProfileIndex.setStatus("current")


class _ZhoneCpeVoipFeaturesProfileIndex_Type(Unsigned32):
    """Custom type zhoneCpeVoipFeaturesProfileIndex based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeVoipFeaturesProfileIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeVoipFeaturesProfileIndex_Object = MibTableColumn
zhoneCpeVoipFeaturesProfileIndex = _ZhoneCpeVoipFeaturesProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 7, 1, 14),
    _ZhoneCpeVoipFeaturesProfileIndex_Type()
)
zhoneCpeVoipFeaturesProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipFeaturesProfileIndex.setStatus("current")


class _ZhoneCpeVoipMediaProfileIndex_Type(Unsigned32):
    """Custom type zhoneCpeVoipMediaProfileIndex based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeVoipMediaProfileIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeVoipMediaProfileIndex_Object = MibTableColumn
zhoneCpeVoipMediaProfileIndex = _ZhoneCpeVoipMediaProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 7, 1, 15),
    _ZhoneCpeVoipMediaProfileIndex_Type()
)
zhoneCpeVoipMediaProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipMediaProfileIndex.setStatus("current")


class _ZhoneCpeVoipSubscriberPhoneFollowsWan_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeVoipSubscriberPhoneFollowsWan based on ZhoneEnabledFlag"""


_ZhoneCpeVoipSubscriberPhoneFollowsWan_Object = MibTableColumn
zhoneCpeVoipSubscriberPhoneFollowsWan = _ZhoneCpeVoipSubscriberPhoneFollowsWan_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 7, 1, 16),
    _ZhoneCpeVoipSubscriberPhoneFollowsWan_Type()
)
zhoneCpeVoipSubscriberPhoneFollowsWan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVoipSubscriberPhoneFollowsWan.setStatus("current")
_ZhoneCpeEthSubscriberTable_Object = MibTable
zhoneCpeEthSubscriberTable = _ZhoneCpeEthSubscriberTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 8)
)
if mibBuilder.loadTexts:
    zhoneCpeEthSubscriberTable.setStatus("current")
_ZhoneCpeEthSubscriberEntry_Object = MibTableRow
zhoneCpeEthSubscriberEntry = _ZhoneCpeEthSubscriberEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 8, 1)
)
zhoneCpeEthSubscriberEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeIfIndex"),
    (0, "Zhone-CPE-MIB", "zhoneCpeEthSubscriberPortNumber"),
)
if mibBuilder.loadTexts:
    zhoneCpeEthSubscriberEntry.setStatus("current")


class _ZhoneCpeEthSubscriberPortNumber_Type(Unsigned32):
    """Custom type zhoneCpeEthSubscriberPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeEthSubscriberPortNumber_Type.__name__ = "Unsigned32"
_ZhoneCpeEthSubscriberPortNumber_Object = MibTableColumn
zhoneCpeEthSubscriberPortNumber = _ZhoneCpeEthSubscriberPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 8, 1, 1),
    _ZhoneCpeEthSubscriberPortNumber_Type()
)
zhoneCpeEthSubscriberPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeEthSubscriberPortNumber.setStatus("current")


class _ZhoneCpeEthSubscriberRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpeEthSubscriberRowStatus based on ZhoneRowStatus"""


_ZhoneCpeEthSubscriberRowStatus_Object = MibTableColumn
zhoneCpeEthSubscriberRowStatus = _ZhoneCpeEthSubscriberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 8, 1, 2),
    _ZhoneCpeEthSubscriberRowStatus_Type()
)
zhoneCpeEthSubscriberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeEthSubscriberRowStatus.setStatus("current")


class _ZhoneCpeEthSubscriberAdminState_Type(ZhoneAdminState):
    """Custom type zhoneCpeEthSubscriberAdminState based on ZhoneAdminState"""
    defaultValue = 1


_ZhoneCpeEthSubscriberAdminState_Object = MibTableColumn
zhoneCpeEthSubscriberAdminState = _ZhoneCpeEthSubscriberAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 8, 1, 3),
    _ZhoneCpeEthSubscriberAdminState_Type()
)
zhoneCpeEthSubscriberAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeEthSubscriberAdminState.setStatus("current")


class _ZhoneCpeEthSubscriberLoopback_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeEthSubscriberLoopback based on ZhoneEnabledFlag"""


_ZhoneCpeEthSubscriberLoopback_Object = MibTableColumn
zhoneCpeEthSubscriberLoopback = _ZhoneCpeEthSubscriberLoopback_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 8, 1, 4),
    _ZhoneCpeEthSubscriberLoopback_Type()
)
zhoneCpeEthSubscriberLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeEthSubscriberLoopback.setStatus("current")


class _ZhoneCpeEthSubscriberRate_Type(Integer32):
    """Custom type zhoneCpeEthSubscriberRate based on Integer32"""
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
        *(("auto", 1),
          ("oneHundredMbps", 3),
          ("oneThousandMbps", 4),
          ("tenMbps", 2))
    )


_ZhoneCpeEthSubscriberRate_Type.__name__ = "Integer32"
_ZhoneCpeEthSubscriberRate_Object = MibTableColumn
zhoneCpeEthSubscriberRate = _ZhoneCpeEthSubscriberRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 8, 1, 5),
    _ZhoneCpeEthSubscriberRate_Type()
)
zhoneCpeEthSubscriberRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeEthSubscriberRate.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeEthSubscriberRate.setUnits("Mbps")


class _ZhoneCpeEthSubscriberDuplex_Type(Integer32):
    """Custom type zhoneCpeEthSubscriberDuplex based on Integer32"""
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
        *(("auto", 1),
          ("full", 2),
          ("half", 3))
    )


_ZhoneCpeEthSubscriberDuplex_Type.__name__ = "Integer32"
_ZhoneCpeEthSubscriberDuplex_Object = MibTableColumn
zhoneCpeEthSubscriberDuplex = _ZhoneCpeEthSubscriberDuplex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 8, 1, 6),
    _ZhoneCpeEthSubscriberDuplex_Type()
)
zhoneCpeEthSubscriberDuplex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeEthSubscriberDuplex.setStatus("current")


class _ZhoneCpeEthSubscriberMtu_Type(Unsigned32):
    """Custom type zhoneCpeEthSubscriberMtu based on Unsigned32"""
    defaultValue = 1518

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneCpeEthSubscriberMtu_Type.__name__ = "Unsigned32"
_ZhoneCpeEthSubscriberMtu_Object = MibTableColumn
zhoneCpeEthSubscriberMtu = _ZhoneCpeEthSubscriberMtu_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 8, 1, 7),
    _ZhoneCpeEthSubscriberMtu_Type()
)
zhoneCpeEthSubscriberMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeEthSubscriberMtu.setStatus("current")


class _ZhoneCpeEthSubscriberPortType_Type(Integer32):
    """Custom type zhoneCpeEthSubscriberPortType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 2))
    )


_ZhoneCpeEthSubscriberPortType_Type.__name__ = "Integer32"
_ZhoneCpeEthSubscriberPortType_Object = MibTableColumn
zhoneCpeEthSubscriberPortType = _ZhoneCpeEthSubscriberPortType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 8, 1, 8),
    _ZhoneCpeEthSubscriberPortType_Type()
)
zhoneCpeEthSubscriberPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeEthSubscriberPortType.setStatus("current")


class _ZhoneCpeEthSubscriberPauseTime_Type(Unsigned32):
    """Custom type zhoneCpeEthSubscriberPauseTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneCpeEthSubscriberPauseTime_Type.__name__ = "Unsigned32"
_ZhoneCpeEthSubscriberPauseTime_Object = MibTableColumn
zhoneCpeEthSubscriberPauseTime = _ZhoneCpeEthSubscriberPauseTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 8, 1, 9),
    _ZhoneCpeEthSubscriberPauseTime_Type()
)
zhoneCpeEthSubscriberPauseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeEthSubscriberPauseTime.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeEthSubscriberPauseTime.setUnits("quanta")


class _ZhoneCpeEthSubscriberMode_Type(Integer32):
    """Custom type zhoneCpeEthSubscriberMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridged", 1),
          ("routed", 2))
    )


_ZhoneCpeEthSubscriberMode_Type.__name__ = "Integer32"
_ZhoneCpeEthSubscriberMode_Object = MibTableColumn
zhoneCpeEthSubscriberMode = _ZhoneCpeEthSubscriberMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 8, 1, 10),
    _ZhoneCpeEthSubscriberMode_Type()
)
zhoneCpeEthSubscriberMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeEthSubscriberMode.setStatus("current")


class _ZhoneCpeEthSubscriberPowerFeed_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeEthSubscriberPowerFeed based on ZhoneEnabledFlag"""


_ZhoneCpeEthSubscriberPowerFeed_Object = MibTableColumn
zhoneCpeEthSubscriberPowerFeed = _ZhoneCpeEthSubscriberPowerFeed_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 8, 1, 11),
    _ZhoneCpeEthSubscriberPowerFeed_Type()
)
zhoneCpeEthSubscriberPowerFeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeEthSubscriberPowerFeed.setStatus("current")


class _ZhoneCpeVideoProfileIndex_Type(Unsigned32):
    """Custom type zhoneCpeVideoProfileIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeVideoProfileIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeVideoProfileIndex_Object = MibTableColumn
zhoneCpeVideoProfileIndex = _ZhoneCpeVideoProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 8, 1, 12),
    _ZhoneCpeVideoProfileIndex_Type()
)
zhoneCpeVideoProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVideoProfileIndex.setStatus("current")


class _ZhoneCpeTrafficManagementProfileIndex_Type(Unsigned32):
    """Custom type zhoneCpeTrafficManagementProfileIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeTrafficManagementProfileIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeTrafficManagementProfileIndex_Object = MibTableColumn
zhoneCpeTrafficManagementProfileIndex = _ZhoneCpeTrafficManagementProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 8, 1, 13),
    _ZhoneCpeTrafficManagementProfileIndex_Type()
)
zhoneCpeTrafficManagementProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeTrafficManagementProfileIndex.setStatus("current")


class _ZhoneCpeEthSubscriberLineStatusAlarm_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeEthSubscriberLineStatusAlarm based on ZhoneEnabledFlag"""


_ZhoneCpeEthSubscriberLineStatusAlarm_Object = MibTableColumn
zhoneCpeEthSubscriberLineStatusAlarm = _ZhoneCpeEthSubscriberLineStatusAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 8, 1, 14),
    _ZhoneCpeEthSubscriberLineStatusAlarm_Type()
)
zhoneCpeEthSubscriberLineStatusAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeEthSubscriberLineStatusAlarm.setStatus("current")


class _ZhoneCpeEthSubscriberAlarmSeverity_Type(ZhoneAlarmSeverity):
    """Custom type zhoneCpeEthSubscriberAlarmSeverity based on ZhoneAlarmSeverity"""


_ZhoneCpeEthSubscriberAlarmSeverity_Object = MibTableColumn
zhoneCpeEthSubscriberAlarmSeverity = _ZhoneCpeEthSubscriberAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 8, 1, 15),
    _ZhoneCpeEthSubscriberAlarmSeverity_Type()
)
zhoneCpeEthSubscriberAlarmSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeEthSubscriberAlarmSeverity.setStatus("current")


class _ZhoneCpeEthSubscriberPowerShed_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeEthSubscriberPowerShed based on ZhoneEnabledFlag"""


_ZhoneCpeEthSubscriberPowerShed_Object = MibTableColumn
zhoneCpeEthSubscriberPowerShed = _ZhoneCpeEthSubscriberPowerShed_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 8, 1, 16),
    _ZhoneCpeEthSubscriberPowerShed_Type()
)
zhoneCpeEthSubscriberPowerShed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeEthSubscriberPowerShed.setStatus("current")


class _ZhoneCpeEthSubscriberPowerRange_Type(Integer32):
    """Custom type zhoneCpeEthSubscriberPowerRange based on Integer32"""
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
        *(("disabled", 1),
          ("high", 4),
          ("low", 2),
          ("medium", 3))
    )


_ZhoneCpeEthSubscriberPowerRange_Type.__name__ = "Integer32"
_ZhoneCpeEthSubscriberPowerRange_Object = MibTableColumn
zhoneCpeEthSubscriberPowerRange = _ZhoneCpeEthSubscriberPowerRange_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 8, 1, 17),
    _ZhoneCpeEthSubscriberPowerRange_Type()
)
zhoneCpeEthSubscriberPowerRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeEthSubscriberPowerRange.setStatus("current")
_ZhoneCpeEthSubscriberLldpMedList_Type = Unsigned32
_ZhoneCpeEthSubscriberLldpMedList_Object = MibTableColumn
zhoneCpeEthSubscriberLldpMedList = _ZhoneCpeEthSubscriberLldpMedList_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 8, 1, 18),
    _ZhoneCpeEthSubscriberLldpMedList_Type()
)
zhoneCpeEthSubscriberLldpMedList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeEthSubscriberLldpMedList.setStatus("current")
_ZhoneCpeVideo_ObjectIdentity = ObjectIdentity
zhoneCpeVideo = _ZhoneCpeVideo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 9)
)
if mibBuilder.loadTexts:
    zhoneCpeVideo.setStatus("current")
_ZhoneCpeVideoIndexNext_Type = Integer32
_ZhoneCpeVideoIndexNext_Object = MibScalar
zhoneCpeVideoIndexNext = _ZhoneCpeVideoIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 9, 1),
    _ZhoneCpeVideoIndexNext_Type()
)
zhoneCpeVideoIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeVideoIndexNext.setStatus("current")
_ZhoneCpeVideoTable_Object = MibTable
zhoneCpeVideoTable = _ZhoneCpeVideoTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 9, 2)
)
if mibBuilder.loadTexts:
    zhoneCpeVideoTable.setStatus("current")
_ZhoneCpeVideoEntry_Object = MibTableRow
zhoneCpeVideoEntry = _ZhoneCpeVideoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 9, 2, 1)
)
zhoneCpeVideoEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeVideoIndex"),
    (0, "Zhone-CPE-MIB", "zhoneCpeGemPort"),
    (0, "Zhone-CPE-MIB", "zhoneCpeVlan"),
)
if mibBuilder.loadTexts:
    zhoneCpeVideoEntry.setStatus("current")


class _ZhoneCpeVideoIndex_Type(Unsigned32):
    """Custom type zhoneCpeVideoIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeVideoIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeVideoIndex_Object = MibTableColumn
zhoneCpeVideoIndex = _ZhoneCpeVideoIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 9, 2, 1, 1),
    _ZhoneCpeVideoIndex_Type()
)
zhoneCpeVideoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeVideoIndex.setStatus("current")


class _ZhoneCpeGemPort_Type(Unsigned32):
    """Custom type zhoneCpeGemPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_ZhoneCpeGemPort_Type.__name__ = "Unsigned32"
_ZhoneCpeGemPort_Object = MibTableColumn
zhoneCpeGemPort = _ZhoneCpeGemPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 9, 2, 1, 2),
    _ZhoneCpeGemPort_Type()
)
zhoneCpeGemPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeGemPort.setStatus("current")


class _ZhoneCpeVlan_Type(Unsigned32):
    """Custom type zhoneCpeVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_ZhoneCpeVlan_Type.__name__ = "Unsigned32"
_ZhoneCpeVlan_Object = MibTableColumn
zhoneCpeVlan = _ZhoneCpeVlan_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 9, 2, 1, 3),
    _ZhoneCpeVlan_Type()
)
zhoneCpeVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeVlan.setStatus("current")


class _ZhoneCpeVideoRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpeVideoRowStatus based on ZhoneRowStatus"""


_ZhoneCpeVideoRowStatus_Object = MibTableColumn
zhoneCpeVideoRowStatus = _ZhoneCpeVideoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 9, 2, 1, 4),
    _ZhoneCpeVideoRowStatus_Type()
)
zhoneCpeVideoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVideoRowStatus.setStatus("current")
_ZhoneCpeVideoProfileName_Type = ZhoneAdminString
_ZhoneCpeVideoProfileName_Object = MibTableColumn
zhoneCpeVideoProfileName = _ZhoneCpeVideoProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 9, 2, 1, 5),
    _ZhoneCpeVideoProfileName_Type()
)
zhoneCpeVideoProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVideoProfileName.setStatus("current")


class _ZhoneCpeVideoMaxSimultaneousGroups_Type(Unsigned32):
    """Custom type zhoneCpeVideoMaxSimultaneousGroups based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneCpeVideoMaxSimultaneousGroups_Type.__name__ = "Unsigned32"
_ZhoneCpeVideoMaxSimultaneousGroups_Object = MibTableColumn
zhoneCpeVideoMaxSimultaneousGroups = _ZhoneCpeVideoMaxSimultaneousGroups_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 9, 2, 1, 6),
    _ZhoneCpeVideoMaxSimultaneousGroups_Type()
)
zhoneCpeVideoMaxSimultaneousGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVideoMaxSimultaneousGroups.setStatus("current")


class _ZhoneCpeVideoMaxMulticastBandwidth_Type(Unsigned32):
    """Custom type zhoneCpeVideoMaxMulticastBandwidth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeVideoMaxMulticastBandwidth_Type.__name__ = "Unsigned32"
_ZhoneCpeVideoMaxMulticastBandwidth_Object = MibTableColumn
zhoneCpeVideoMaxMulticastBandwidth = _ZhoneCpeVideoMaxMulticastBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 9, 2, 1, 7),
    _ZhoneCpeVideoMaxMulticastBandwidth_Type()
)
zhoneCpeVideoMaxMulticastBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVideoMaxMulticastBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeVideoMaxMulticastBandwidth.setUnits("bytes/second")


class _ZhoneCpeVideoBandwidthEnforce_Type(TruthValue):
    """Custom type zhoneCpeVideoBandwidthEnforce based on TruthValue"""


_ZhoneCpeVideoBandwidthEnforce_Object = MibTableColumn
zhoneCpeVideoBandwidthEnforce = _ZhoneCpeVideoBandwidthEnforce_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 9, 2, 1, 8),
    _ZhoneCpeVideoBandwidthEnforce_Type()
)
zhoneCpeVideoBandwidthEnforce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVideoBandwidthEnforce.setStatus("current")


class _ZhoneCpeVideoIgmpVersion_Type(Integer32):
    """Custom type zhoneCpeVideoIgmpVersion based on Integer32"""
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
        *(("version1", 1),
          ("version2", 2),
          ("version3", 3))
    )


_ZhoneCpeVideoIgmpVersion_Type.__name__ = "Integer32"
_ZhoneCpeVideoIgmpVersion_Object = MibTableColumn
zhoneCpeVideoIgmpVersion = _ZhoneCpeVideoIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 9, 2, 1, 9),
    _ZhoneCpeVideoIgmpVersion_Type()
)
zhoneCpeVideoIgmpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVideoIgmpVersion.setStatus("current")


class _ZhoneCpeVideoIgmpFunction_Type(Integer32):
    """Custom type zhoneCpeVideoIgmpFunction based on Integer32"""
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
        *(("proxy", 3),
          ("snoopwithproxy", 2),
          ("transparentsnooping", 1))
    )


_ZhoneCpeVideoIgmpFunction_Type.__name__ = "Integer32"
_ZhoneCpeVideoIgmpFunction_Object = MibTableColumn
zhoneCpeVideoIgmpFunction = _ZhoneCpeVideoIgmpFunction_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 9, 2, 1, 10),
    _ZhoneCpeVideoIgmpFunction_Type()
)
zhoneCpeVideoIgmpFunction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVideoIgmpFunction.setStatus("current")


class _ZhoneCpeVideoImmediateLeave_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeVideoImmediateLeave based on ZhoneEnabledFlag"""


_ZhoneCpeVideoImmediateLeave_Object = MibTableColumn
zhoneCpeVideoImmediateLeave = _ZhoneCpeVideoImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 9, 2, 1, 11),
    _ZhoneCpeVideoImmediateLeave_Type()
)
zhoneCpeVideoImmediateLeave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVideoImmediateLeave.setStatus("current")


class _ZhoneCpeVideoUpstreamIgmpRate_Type(Unsigned32):
    """Custom type zhoneCpeVideoUpstreamIgmpRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeVideoUpstreamIgmpRate_Type.__name__ = "Unsigned32"
_ZhoneCpeVideoUpstreamIgmpRate_Object = MibTableColumn
zhoneCpeVideoUpstreamIgmpRate = _ZhoneCpeVideoUpstreamIgmpRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 9, 2, 1, 12),
    _ZhoneCpeVideoUpstreamIgmpRate_Type()
)
zhoneCpeVideoUpstreamIgmpRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVideoUpstreamIgmpRate.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeVideoUpstreamIgmpRate.setUnits("messages/second")


class _ZhoneCpeVideoRobustness_Type(Unsigned32):
    """Custom type zhoneCpeVideoRobustness based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneCpeVideoRobustness_Type.__name__ = "Unsigned32"
_ZhoneCpeVideoRobustness_Object = MibTableColumn
zhoneCpeVideoRobustness = _ZhoneCpeVideoRobustness_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 9, 2, 1, 13),
    _ZhoneCpeVideoRobustness_Type()
)
zhoneCpeVideoRobustness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVideoRobustness.setStatus("current")


class _ZhoneCpeVideoAccessControlList_Type(Unsigned32):
    """Custom type zhoneCpeVideoAccessControlList based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeVideoAccessControlList_Type.__name__ = "Unsigned32"
_ZhoneCpeVideoAccessControlList_Object = MibTableColumn
zhoneCpeVideoAccessControlList = _ZhoneCpeVideoAccessControlList_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 9, 2, 1, 14),
    _ZhoneCpeVideoAccessControlList_Type()
)
zhoneCpeVideoAccessControlList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVideoAccessControlList.setStatus("current")
_ZhoneCpeVideoAccessControl_ObjectIdentity = ObjectIdentity
zhoneCpeVideoAccessControl = _ZhoneCpeVideoAccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 10)
)
if mibBuilder.loadTexts:
    zhoneCpeVideoAccessControl.setStatus("current")
_ZhoneCpeVideoAccessControlIndexTable_Object = MibTable
zhoneCpeVideoAccessControlIndexTable = _ZhoneCpeVideoAccessControlIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 10, 1)
)
if mibBuilder.loadTexts:
    zhoneCpeVideoAccessControlIndexTable.setStatus("current")
_ZhoneCpeVideoAccessControlIndexEntry_Object = MibTableRow
zhoneCpeVideoAccessControlIndexEntry = _ZhoneCpeVideoAccessControlIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 10, 1, 1)
)
zhoneCpeVideoAccessControlIndexEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeVideoAccessControlListIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeVideoAccessControlIndexEntry.setStatus("current")


class _ZhoneCpeVideoAccessControlIndexNext_Type(Unsigned32):
    """Custom type zhoneCpeVideoAccessControlIndexNext based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeVideoAccessControlIndexNext_Type.__name__ = "Unsigned32"
_ZhoneCpeVideoAccessControlIndexNext_Object = MibTableColumn
zhoneCpeVideoAccessControlIndexNext = _ZhoneCpeVideoAccessControlIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 10, 1, 1, 1),
    _ZhoneCpeVideoAccessControlIndexNext_Type()
)
zhoneCpeVideoAccessControlIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeVideoAccessControlIndexNext.setStatus("current")
_ZhoneCpeVideoAccessControlTable_Object = MibTable
zhoneCpeVideoAccessControlTable = _ZhoneCpeVideoAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 10, 2)
)
if mibBuilder.loadTexts:
    zhoneCpeVideoAccessControlTable.setStatus("current")
_ZhoneCpeVideoAccessControlEntry_Object = MibTableRow
zhoneCpeVideoAccessControlEntry = _ZhoneCpeVideoAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 10, 2, 1)
)
zhoneCpeVideoAccessControlEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeVideoAccessControlListIndex"),
    (0, "Zhone-CPE-MIB", "zhoneCpeVideoAccessControlEntryIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeVideoAccessControlEntry.setStatus("current")


class _ZhoneCpeVideoAccessControlListIndex_Type(Unsigned32):
    """Custom type zhoneCpeVideoAccessControlListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeVideoAccessControlListIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeVideoAccessControlListIndex_Object = MibTableColumn
zhoneCpeVideoAccessControlListIndex = _ZhoneCpeVideoAccessControlListIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 10, 2, 1, 1),
    _ZhoneCpeVideoAccessControlListIndex_Type()
)
zhoneCpeVideoAccessControlListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeVideoAccessControlListIndex.setStatus("current")


class _ZhoneCpeVideoAccessControlEntryIndex_Type(Unsigned32):
    """Custom type zhoneCpeVideoAccessControlEntryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeVideoAccessControlEntryIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeVideoAccessControlEntryIndex_Object = MibTableColumn
zhoneCpeVideoAccessControlEntryIndex = _ZhoneCpeVideoAccessControlEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 10, 2, 1, 2),
    _ZhoneCpeVideoAccessControlEntryIndex_Type()
)
zhoneCpeVideoAccessControlEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeVideoAccessControlEntryIndex.setStatus("current")


class _ZhoneCpeVideoAccessControlRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpeVideoAccessControlRowStatus based on ZhoneRowStatus"""


_ZhoneCpeVideoAccessControlRowStatus_Object = MibTableColumn
zhoneCpeVideoAccessControlRowStatus = _ZhoneCpeVideoAccessControlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 10, 2, 1, 3),
    _ZhoneCpeVideoAccessControlRowStatus_Type()
)
zhoneCpeVideoAccessControlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVideoAccessControlRowStatus.setStatus("current")
_ZhoneCpeVideoAccessControlProfileName_Type = ZhoneAdminString
_ZhoneCpeVideoAccessControlProfileName_Object = MibTableColumn
zhoneCpeVideoAccessControlProfileName = _ZhoneCpeVideoAccessControlProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 10, 2, 1, 4),
    _ZhoneCpeVideoAccessControlProfileName_Type()
)
zhoneCpeVideoAccessControlProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVideoAccessControlProfileName.setStatus("current")


class _ZhoneCpeVideoAccessControlType_Type(Integer32):
    """Custom type zhoneCpeVideoAccessControlType based on Integer32"""
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
        *(("alwayson", 2),
          ("normal", 1),
          ("periodic", 3))
    )


_ZhoneCpeVideoAccessControlType_Type.__name__ = "Integer32"
_ZhoneCpeVideoAccessControlType_Object = MibTableColumn
zhoneCpeVideoAccessControlType = _ZhoneCpeVideoAccessControlType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 10, 2, 1, 5),
    _ZhoneCpeVideoAccessControlType_Type()
)
zhoneCpeVideoAccessControlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVideoAccessControlType.setStatus("current")
_ZhoneCpeVideoAccessControlSrcIp_Type = IpAddress
_ZhoneCpeVideoAccessControlSrcIp_Object = MibTableColumn
zhoneCpeVideoAccessControlSrcIp = _ZhoneCpeVideoAccessControlSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 10, 2, 1, 6),
    _ZhoneCpeVideoAccessControlSrcIp_Type()
)
zhoneCpeVideoAccessControlSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVideoAccessControlSrcIp.setStatus("current")
_ZhoneCpeVideoAccessControlDstIpStart_Type = IpAddress
_ZhoneCpeVideoAccessControlDstIpStart_Object = MibTableColumn
zhoneCpeVideoAccessControlDstIpStart = _ZhoneCpeVideoAccessControlDstIpStart_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 10, 2, 1, 7),
    _ZhoneCpeVideoAccessControlDstIpStart_Type()
)
zhoneCpeVideoAccessControlDstIpStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVideoAccessControlDstIpStart.setStatus("current")
_ZhoneCpeVideoAccessControlDstIpEnd_Type = IpAddress
_ZhoneCpeVideoAccessControlDstIpEnd_Object = MibTableColumn
zhoneCpeVideoAccessControlDstIpEnd = _ZhoneCpeVideoAccessControlDstIpEnd_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 10, 2, 1, 8),
    _ZhoneCpeVideoAccessControlDstIpEnd_Type()
)
zhoneCpeVideoAccessControlDstIpEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVideoAccessControlDstIpEnd.setStatus("current")


class _ZhoneCpeVideoAccessControlImputedGroupBw_Type(Unsigned32):
    """Custom type zhoneCpeVideoAccessControlImputedGroupBw based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeVideoAccessControlImputedGroupBw_Type.__name__ = "Unsigned32"
_ZhoneCpeVideoAccessControlImputedGroupBw_Object = MibTableColumn
zhoneCpeVideoAccessControlImputedGroupBw = _ZhoneCpeVideoAccessControlImputedGroupBw_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 10, 2, 1, 9),
    _ZhoneCpeVideoAccessControlImputedGroupBw_Type()
)
zhoneCpeVideoAccessControlImputedGroupBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeVideoAccessControlImputedGroupBw.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeVideoAccessControlImputedGroupBw.setUnits("bytes/second")
_ZhoneCpePweSubscriberTable_Object = MibTable
zhoneCpePweSubscriberTable = _ZhoneCpePweSubscriberTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 11)
)
if mibBuilder.loadTexts:
    zhoneCpePweSubscriberTable.setStatus("current")
_ZhoneCpePweSubscriberEntry_Object = MibTableRow
zhoneCpePweSubscriberEntry = _ZhoneCpePweSubscriberEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 11, 1)
)
zhoneCpePweSubscriberEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeIfIndex"),
    (0, "Zhone-CPE-MIB", "zhoneCpePweSubscriberPortNumber"),
)
if mibBuilder.loadTexts:
    zhoneCpePweSubscriberEntry.setStatus("current")


class _ZhoneCpePweSubscriberPortNumber_Type(Unsigned32):
    """Custom type zhoneCpePweSubscriberPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpePweSubscriberPortNumber_Type.__name__ = "Unsigned32"
_ZhoneCpePweSubscriberPortNumber_Object = MibTableColumn
zhoneCpePweSubscriberPortNumber = _ZhoneCpePweSubscriberPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 11, 1, 1),
    _ZhoneCpePweSubscriberPortNumber_Type()
)
zhoneCpePweSubscriberPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpePweSubscriberPortNumber.setStatus("current")


class _ZhoneCpePweSubscriberRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpePweSubscriberRowStatus based on ZhoneRowStatus"""


_ZhoneCpePweSubscriberRowStatus_Object = MibTableColumn
zhoneCpePweSubscriberRowStatus = _ZhoneCpePweSubscriberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 11, 1, 2),
    _ZhoneCpePweSubscriberRowStatus_Type()
)
zhoneCpePweSubscriberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweSubscriberRowStatus.setStatus("current")


class _ZhoneCpePweSubscriberAdminState_Type(ZhoneAdminState):
    """Custom type zhoneCpePweSubscriberAdminState based on ZhoneAdminState"""
    defaultValue = 1


_ZhoneCpePweSubscriberAdminState_Object = MibTableColumn
zhoneCpePweSubscriberAdminState = _ZhoneCpePweSubscriberAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 11, 1, 3),
    _ZhoneCpePweSubscriberAdminState_Type()
)
zhoneCpePweSubscriberAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweSubscriberAdminState.setStatus("current")


class _ZhoneCpePweSubscriberLoopback_Type(Integer32):
    """Custom type zhoneCpePweSubscriberLoopback based on Integer32"""
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
        *(("cesside", 5),
          ("line", 3),
          ("noloop", 1),
          ("payload", 2),
          ("ponside", 4))
    )


_ZhoneCpePweSubscriberLoopback_Type.__name__ = "Integer32"
_ZhoneCpePweSubscriberLoopback_Object = MibTableColumn
zhoneCpePweSubscriberLoopback = _ZhoneCpePweSubscriberLoopback_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 11, 1, 4),
    _ZhoneCpePweSubscriberLoopback_Type()
)
zhoneCpePweSubscriberLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweSubscriberLoopback.setStatus("current")


class _ZhoneCpePweSubscriberNearEndPort_Type(Unsigned32):
    """Custom type zhoneCpePweSubscriberNearEndPort based on Unsigned32"""
    defaultValue = 57000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneCpePweSubscriberNearEndPort_Type.__name__ = "Unsigned32"
_ZhoneCpePweSubscriberNearEndPort_Object = MibTableColumn
zhoneCpePweSubscriberNearEndPort = _ZhoneCpePweSubscriberNearEndPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 11, 1, 5),
    _ZhoneCpePweSubscriberNearEndPort_Type()
)
zhoneCpePweSubscriberNearEndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweSubscriberNearEndPort.setStatus("current")
_ZhoneCpePweSubscriberFarEndIp_Type = IpAddress
_ZhoneCpePweSubscriberFarEndIp_Object = MibTableColumn
zhoneCpePweSubscriberFarEndIp = _ZhoneCpePweSubscriberFarEndIp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 11, 1, 6),
    _ZhoneCpePweSubscriberFarEndIp_Type()
)
zhoneCpePweSubscriberFarEndIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweSubscriberFarEndIp.setStatus("current")


class _ZhoneCpePweSubscriberFarEndPort_Type(Unsigned32):
    """Custom type zhoneCpePweSubscriberFarEndPort based on Unsigned32"""
    defaultValue = 57000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneCpePweSubscriberFarEndPort_Type.__name__ = "Unsigned32"
_ZhoneCpePweSubscriberFarEndPort_Object = MibTableColumn
zhoneCpePweSubscriberFarEndPort = _ZhoneCpePweSubscriberFarEndPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 11, 1, 7),
    _ZhoneCpePweSubscriberFarEndPort_Type()
)
zhoneCpePweSubscriberFarEndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweSubscriberFarEndPort.setStatus("current")


class _ZhoneCpePweSubscriberLineLength_Type(Unsigned32):
    """Custom type zhoneCpePweSubscriberLineLength based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneCpePweSubscriberLineLength_Type.__name__ = "Unsigned32"
_ZhoneCpePweSubscriberLineLength_Object = MibTableColumn
zhoneCpePweSubscriberLineLength = _ZhoneCpePweSubscriberLineLength_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 11, 1, 8),
    _ZhoneCpePweSubscriberLineLength_Type()
)
zhoneCpePweSubscriberLineLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweSubscriberLineLength.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpePweSubscriberLineLength.setUnits("feet")


class _ZhoneCpePweProfileIndex_Type(Unsigned32):
    """Custom type zhoneCpePweProfileIndex based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpePweProfileIndex_Type.__name__ = "Unsigned32"
_ZhoneCpePweProfileIndex_Object = MibTableColumn
zhoneCpePweProfileIndex = _ZhoneCpePweProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 11, 1, 9),
    _ZhoneCpePweProfileIndex_Type()
)
zhoneCpePweProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweProfileIndex.setStatus("current")


class _ZhoneCpePweSubscriberLineStatusAlarm_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpePweSubscriberLineStatusAlarm based on ZhoneEnabledFlag"""


_ZhoneCpePweSubscriberLineStatusAlarm_Object = MibTableColumn
zhoneCpePweSubscriberLineStatusAlarm = _ZhoneCpePweSubscriberLineStatusAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 11, 1, 10),
    _ZhoneCpePweSubscriberLineStatusAlarm_Type()
)
zhoneCpePweSubscriberLineStatusAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweSubscriberLineStatusAlarm.setStatus("current")


class _ZhoneCpePweSubscriberAlarmSeverity_Type(ZhoneAlarmSeverity):
    """Custom type zhoneCpePweSubscriberAlarmSeverity based on ZhoneAlarmSeverity"""


_ZhoneCpePweSubscriberAlarmSeverity_Object = MibTableColumn
zhoneCpePweSubscriberAlarmSeverity = _ZhoneCpePweSubscriberAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 11, 1, 11),
    _ZhoneCpePweSubscriberAlarmSeverity_Type()
)
zhoneCpePweSubscriberAlarmSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweSubscriberAlarmSeverity.setStatus("current")
_ZhoneCpePwe_ObjectIdentity = ObjectIdentity
zhoneCpePwe = _ZhoneCpePwe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12)
)
if mibBuilder.loadTexts:
    zhoneCpePwe.setStatus("current")
_ZhoneCpePweIndexNext_Type = Integer32
_ZhoneCpePweIndexNext_Object = MibScalar
zhoneCpePweIndexNext = _ZhoneCpePweIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 1),
    _ZhoneCpePweIndexNext_Type()
)
zhoneCpePweIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpePweIndexNext.setStatus("current")
_ZhoneCpePweTable_Object = MibTable
zhoneCpePweTable = _ZhoneCpePweTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2)
)
if mibBuilder.loadTexts:
    zhoneCpePweTable.setStatus("current")
_ZhoneCpePweEntry_Object = MibTableRow
zhoneCpePweEntry = _ZhoneCpePweEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1)
)
zhoneCpePweEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpePweIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpePweEntry.setStatus("current")


class _ZhoneCpePweIndex_Type(Unsigned32):
    """Custom type zhoneCpePweIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpePweIndex_Type.__name__ = "Unsigned32"
_ZhoneCpePweIndex_Object = MibTableColumn
zhoneCpePweIndex = _ZhoneCpePweIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 1),
    _ZhoneCpePweIndex_Type()
)
zhoneCpePweIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpePweIndex.setStatus("current")


class _ZhoneCpePweRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpePweRowStatus based on ZhoneRowStatus"""


_ZhoneCpePweRowStatus_Object = MibTableColumn
zhoneCpePweRowStatus = _ZhoneCpePweRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 2),
    _ZhoneCpePweRowStatus_Type()
)
zhoneCpePweRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweRowStatus.setStatus("current")
_ZhoneCpePweProfileName_Type = ZhoneAdminString
_ZhoneCpePweProfileName_Object = MibTableColumn
zhoneCpePweProfileName = _ZhoneCpePweProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 3),
    _ZhoneCpePweProfileName_Type()
)
zhoneCpePweProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweProfileName.setStatus("current")


class _ZhoneCpePweLineType_Type(Integer32):
    """Custom type zhoneCpePweLineType based on Integer32"""
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
        *(("ds1", 1),
          ("e1", 2),
          ("other", 3))
    )


_ZhoneCpePweLineType_Type.__name__ = "Integer32"
_ZhoneCpePweLineType_Object = MibTableColumn
zhoneCpePweLineType = _ZhoneCpePweLineType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 4),
    _ZhoneCpePweLineType_Type()
)
zhoneCpePweLineType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweLineType.setStatus("current")


class _ZhoneCpePweEncoding_Type(Integer32):
    """Custom type zhoneCpePweEncoding based on Integer32"""
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
        *(("ami", 2),
          ("b3zs", 4),
          ("b8zs", 1),
          ("hdb3", 3))
    )


_ZhoneCpePweEncoding_Type.__name__ = "Integer32"
_ZhoneCpePweEncoding_Object = MibTableColumn
zhoneCpePweEncoding = _ZhoneCpePweEncoding_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 5),
    _ZhoneCpePweEncoding_Type()
)
zhoneCpePweEncoding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweEncoding.setStatus("current")


class _ZhoneCpePweDs1Mode_Type(Integer32):
    """Custom type zhoneCpePweDs1Mode based on Integer32"""
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
        *(("longhaulnopwr", 2),
          ("niulonghaulnopwr", 3),
          ("niulonghaulpwr", 4),
          ("shorthaulnopwr", 1))
    )


_ZhoneCpePweDs1Mode_Type.__name__ = "Integer32"
_ZhoneCpePweDs1Mode_Object = MibTableColumn
zhoneCpePweDs1Mode = _ZhoneCpePweDs1Mode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 6),
    _ZhoneCpePweDs1Mode_Type()
)
zhoneCpePweDs1Mode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweDs1Mode.setStatus("current")


class _ZhoneCpePweDs1Framing_Type(Integer32):
    """Custom type zhoneCpePweDs1Framing based on Integer32"""
    defaultValue = 3

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
        *(("extsuperframe", 1),
          ("g704", 4),
          ("jtg704", 5),
          ("superframe", 2),
          ("unframed", 3))
    )


_ZhoneCpePweDs1Framing_Type.__name__ = "Integer32"
_ZhoneCpePweDs1Framing_Object = MibTableColumn
zhoneCpePweDs1Framing = _ZhoneCpePweDs1Framing_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 7),
    _ZhoneCpePweDs1Framing_Type()
)
zhoneCpePweDs1Framing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweDs1Framing.setStatus("current")


class _ZhoneCpePweTransport_Type(Integer32):
    """Custom type zhoneCpePweTransport based on Integer32"""
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
        *(("ethernet", 1),
          ("mpls", 3),
          ("udp", 2))
    )


_ZhoneCpePweTransport_Type.__name__ = "Integer32"
_ZhoneCpePweTransport_Object = MibTableColumn
zhoneCpePweTransport = _ZhoneCpePweTransport_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 8),
    _ZhoneCpePweTransport_Type()
)
zhoneCpePweTransport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweTransport.setStatus("current")


class _ZhoneCpePweServiceType_Type(Integer32):
    """Custom type zhoneCpePweServiceType based on Integer32"""
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
        *(("octetalignedunstruct", 2),
          ("structured", 3),
          ("unstructured", 1))
    )


_ZhoneCpePweServiceType_Type.__name__ = "Integer32"
_ZhoneCpePweServiceType_Object = MibTableColumn
zhoneCpePweServiceType = _ZhoneCpePweServiceType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 9),
    _ZhoneCpePweServiceType_Type()
)
zhoneCpePweServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweServiceType.setStatus("current")


class _ZhoneCpePweSignalling_Type(Integer32):
    """Custom type zhoneCpePweSignalling based on Integer32"""
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
        *(("inbandcas", 2),
          ("nosignalling", 1),
          ("outofbandcas", 3))
    )


_ZhoneCpePweSignalling_Type.__name__ = "Integer32"
_ZhoneCpePweSignalling_Object = MibTableColumn
zhoneCpePweSignalling = _ZhoneCpePweSignalling_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 10),
    _ZhoneCpePweSignalling_Type()
)
zhoneCpePweSignalling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweSignalling.setStatus("current")


class _ZhoneCpePwePayloadSize_Type(Unsigned32):
    """Custom type zhoneCpePwePayloadSize based on Unsigned32"""
    defaultValue = 250

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneCpePwePayloadSize_Type.__name__ = "Unsigned32"
_ZhoneCpePwePayloadSize_Object = MibTableColumn
zhoneCpePwePayloadSize = _ZhoneCpePwePayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 11),
    _ZhoneCpePwePayloadSize_Type()
)
zhoneCpePwePayloadSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePwePayloadSize.setStatus("current")


class _ZhoneCpePwePayloadEncapsulationDelay_Type(Integer32):
    """Custom type zhoneCpePwePayloadEncapsulationDelay based on Integer32"""
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
        *(("ds1cas", 4),
          ("e1cas", 5),
          ("nosignallingandNvalueis1", 1),
          ("nosignallingandNvalueis2to4", 2),
          ("nosignallingandNvalueisgreaterthan4", 3))
    )


_ZhoneCpePwePayloadEncapsulationDelay_Type.__name__ = "Integer32"
_ZhoneCpePwePayloadEncapsulationDelay_Object = MibTableColumn
zhoneCpePwePayloadEncapsulationDelay = _ZhoneCpePwePayloadEncapsulationDelay_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 12),
    _ZhoneCpePwePayloadEncapsulationDelay_Type()
)
zhoneCpePwePayloadEncapsulationDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePwePayloadEncapsulationDelay.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpePwePayloadEncapsulationDelay.setUnits("number of frames")


class _ZhoneCpePweTimingMode_Type(Integer32):
    """Custom type zhoneCpePweTimingMode based on Integer32"""
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
        *(("adaptive", 3),
          ("differential", 2),
          ("loop", 4),
          ("network", 1))
    )


_ZhoneCpePweTimingMode_Type.__name__ = "Integer32"
_ZhoneCpePweTimingMode_Object = MibTableColumn
zhoneCpePweTimingMode = _ZhoneCpePweTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 13),
    _ZhoneCpePweTimingMode_Type()
)
zhoneCpePweTimingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweTimingMode.setStatus("current")


class _ZhoneCpePweChannelAssign_Type(Bits):
    """Custom type zhoneCpePweChannelAssign based on Bits"""
    namedValues = NamedValues(
        *(("channel0", 0),
          ("channel1", 1),
          ("channel10", 10),
          ("channel11", 11),
          ("channel12", 12),
          ("channel13", 13),
          ("channel14", 14),
          ("channel15", 15),
          ("channel16", 16),
          ("channel17", 17),
          ("channel18", 18),
          ("channel19", 19),
          ("channel2", 2),
          ("channel20", 20),
          ("channel21", 21),
          ("channel22", 22),
          ("channel23", 23),
          ("channel24", 24),
          ("channel25", 25),
          ("channel26", 26),
          ("channel27", 27),
          ("channel28", 28),
          ("channel29", 29),
          ("channel3", 3),
          ("channel30", 30),
          ("channel31", 31),
          ("channel4", 4),
          ("channel5", 5),
          ("channel6", 6),
          ("channel7", 7),
          ("channel8", 8),
          ("channel9", 9))
    )

_ZhoneCpePweChannelAssign_Type.__name__ = "Bits"
_ZhoneCpePweChannelAssign_Object = MibTableColumn
zhoneCpePweChannelAssign = _ZhoneCpePweChannelAssign_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 14),
    _ZhoneCpePweChannelAssign_Type()
)
zhoneCpePweChannelAssign.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweChannelAssign.setStatus("current")


class _ZhoneCpePweClockReference_Type(Unsigned32):
    """Custom type zhoneCpePweClockReference based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZhoneCpePweClockReference_Type.__name__ = "Unsigned32"
_ZhoneCpePweClockReference_Object = MibTableColumn
zhoneCpePweClockReference = _ZhoneCpePweClockReference_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 15),
    _ZhoneCpePweClockReference_Type()
)
zhoneCpePweClockReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweClockReference.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpePweClockReference.setUnits("kHz")


class _ZhoneCpePweRtpTimeStampMode_Type(Integer32):
    """Custom type zhoneCpePweRtpTimeStampMode based on Integer32"""
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
        *(("absolute", 2),
          ("differential", 3),
          ("unknown", 1))
    )


_ZhoneCpePweRtpTimeStampMode_Type.__name__ = "Integer32"
_ZhoneCpePweRtpTimeStampMode_Object = MibTableColumn
zhoneCpePweRtpTimeStampMode = _ZhoneCpePweRtpTimeStampMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 16),
    _ZhoneCpePweRtpTimeStampMode_Type()
)
zhoneCpePweRtpTimeStampMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweRtpTimeStampMode.setStatus("current")


class _ZhoneCpePwePtypePayload_Type(Unsigned32):
    """Custom type zhoneCpePwePtypePayload based on Unsigned32"""
    defaultValue = 96

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_ZhoneCpePwePtypePayload_Type.__name__ = "Unsigned32"
_ZhoneCpePwePtypePayload_Object = MibTableColumn
zhoneCpePwePtypePayload = _ZhoneCpePwePtypePayload_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 17),
    _ZhoneCpePwePtypePayload_Type()
)
zhoneCpePwePtypePayload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePwePtypePayload.setStatus("current")


class _ZhoneCpePwePtypeSignalling_Type(Unsigned32):
    """Custom type zhoneCpePwePtypeSignalling based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_ZhoneCpePwePtypeSignalling_Type.__name__ = "Unsigned32"
_ZhoneCpePwePtypeSignalling_Object = MibTableColumn
zhoneCpePwePtypeSignalling = _ZhoneCpePwePtypeSignalling_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 18),
    _ZhoneCpePwePtypeSignalling_Type()
)
zhoneCpePwePtypeSignalling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePwePtypeSignalling.setStatus("current")


class _ZhoneCpePweSSrcPayload_Type(Unsigned32):
    """Custom type zhoneCpePweSSrcPayload based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpePweSSrcPayload_Type.__name__ = "Unsigned32"
_ZhoneCpePweSSrcPayload_Object = MibTableColumn
zhoneCpePweSSrcPayload = _ZhoneCpePweSSrcPayload_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 19),
    _ZhoneCpePweSSrcPayload_Type()
)
zhoneCpePweSSrcPayload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweSSrcPayload.setStatus("current")


class _ZhoneCpePweSSrcSignalling_Type(Unsigned32):
    """Custom type zhoneCpePweSSrcSignalling based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpePweSSrcSignalling_Type.__name__ = "Unsigned32"
_ZhoneCpePweSSrcSignalling_Object = MibTableColumn
zhoneCpePweSSrcSignalling = _ZhoneCpePweSSrcSignalling_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 20),
    _ZhoneCpePweSSrcSignalling_Type()
)
zhoneCpePweSSrcSignalling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweSSrcSignalling.setStatus("current")


class _ZhoneCpePweExpectedPTypePayload_Type(Unsigned32):
    """Custom type zhoneCpePweExpectedPTypePayload based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneCpePweExpectedPTypePayload_Type.__name__ = "Unsigned32"
_ZhoneCpePweExpectedPTypePayload_Object = MibTableColumn
zhoneCpePweExpectedPTypePayload = _ZhoneCpePweExpectedPTypePayload_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 21),
    _ZhoneCpePweExpectedPTypePayload_Type()
)
zhoneCpePweExpectedPTypePayload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweExpectedPTypePayload.setStatus("current")


class _ZhoneCpePweExpectedPTypeSignalling_Type(Unsigned32):
    """Custom type zhoneCpePweExpectedPTypeSignalling based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneCpePweExpectedPTypeSignalling_Type.__name__ = "Unsigned32"
_ZhoneCpePweExpectedPTypeSignalling_Object = MibTableColumn
zhoneCpePweExpectedPTypeSignalling = _ZhoneCpePweExpectedPTypeSignalling_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 22),
    _ZhoneCpePweExpectedPTypeSignalling_Type()
)
zhoneCpePweExpectedPTypeSignalling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweExpectedPTypeSignalling.setStatus("current")


class _ZhoneCpePweExpectedSSrcPayload_Type(Unsigned32):
    """Custom type zhoneCpePweExpectedSSrcPayload based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpePweExpectedSSrcPayload_Type.__name__ = "Unsigned32"
_ZhoneCpePweExpectedSSrcPayload_Object = MibTableColumn
zhoneCpePweExpectedSSrcPayload = _ZhoneCpePweExpectedSSrcPayload_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 23),
    _ZhoneCpePweExpectedSSrcPayload_Type()
)
zhoneCpePweExpectedSSrcPayload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweExpectedSSrcPayload.setStatus("current")


class _ZhoneCpePweExpectedSSrcSignalling_Type(Unsigned32):
    """Custom type zhoneCpePweExpectedSSrcSignalling based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpePweExpectedSSrcSignalling_Type.__name__ = "Unsigned32"
_ZhoneCpePweExpectedSSrcSignalling_Object = MibTableColumn
zhoneCpePweExpectedSSrcSignalling = _ZhoneCpePweExpectedSSrcSignalling_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 24),
    _ZhoneCpePweExpectedSSrcSignalling_Type()
)
zhoneCpePweExpectedSSrcSignalling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweExpectedSSrcSignalling.setStatus("current")


class _ZhoneCpePweJitterBufMax_Type(Unsigned32):
    """Custom type zhoneCpePweJitterBufMax based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneCpePweJitterBufMax_Type.__name__ = "Unsigned32"
_ZhoneCpePweJitterBufMax_Object = MibTableColumn
zhoneCpePweJitterBufMax = _ZhoneCpePweJitterBufMax_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 25),
    _ZhoneCpePweJitterBufMax_Type()
)
zhoneCpePweJitterBufMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweJitterBufMax.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpePweJitterBufMax.setUnits("micro seconds")


class _ZhoneCpePweJitterBufDesired_Type(Unsigned32):
    """Custom type zhoneCpePweJitterBufDesired based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneCpePweJitterBufDesired_Type.__name__ = "Unsigned32"
_ZhoneCpePweJitterBufDesired_Object = MibTableColumn
zhoneCpePweJitterBufDesired = _ZhoneCpePweJitterBufDesired_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 26),
    _ZhoneCpePweJitterBufDesired_Type()
)
zhoneCpePweJitterBufDesired.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweJitterBufDesired.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpePweJitterBufDesired.setUnits("micro seconds")


class _ZhoneCpePweFillPolicy_Type(Integer32):
    """Custom type zhoneCpePweFillPolicy based on Integer32"""
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
        *(("ais", 2),
          ("allones", 3),
          ("allzeros", 4),
          ("ds1idle", 6),
          ("repeatprevdata", 5),
          ("vendorspecific", 1))
    )


_ZhoneCpePweFillPolicy_Type.__name__ = "Integer32"
_ZhoneCpePweFillPolicy_Object = MibTableColumn
zhoneCpePweFillPolicy = _ZhoneCpePweFillPolicy_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 27),
    _ZhoneCpePweFillPolicy_Type()
)
zhoneCpePweFillPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweFillPolicy.setStatus("current")


class _ZhoneCpePweMisconnectedDeclarePolicy_Type(Unsigned32):
    """Custom type zhoneCpePweMisconnectedDeclarePolicy based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZhoneCpePweMisconnectedDeclarePolicy_Type.__name__ = "Unsigned32"
_ZhoneCpePweMisconnectedDeclarePolicy_Object = MibTableColumn
zhoneCpePweMisconnectedDeclarePolicy = _ZhoneCpePweMisconnectedDeclarePolicy_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 28),
    _ZhoneCpePweMisconnectedDeclarePolicy_Type()
)
zhoneCpePweMisconnectedDeclarePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweMisconnectedDeclarePolicy.setStatus("current")


class _ZhoneCpePweMisconnectedClearPolicy_Type(Unsigned32):
    """Custom type zhoneCpePweMisconnectedClearPolicy based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneCpePweMisconnectedClearPolicy_Type.__name__ = "Unsigned32"
_ZhoneCpePweMisconnectedClearPolicy_Object = MibTableColumn
zhoneCpePweMisconnectedClearPolicy = _ZhoneCpePweMisconnectedClearPolicy_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 29),
    _ZhoneCpePweMisconnectedClearPolicy_Type()
)
zhoneCpePweMisconnectedClearPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweMisconnectedClearPolicy.setStatus("current")


class _ZhoneCpePweLossPacketDeclarePolicy_Type(Unsigned32):
    """Custom type zhoneCpePweLossPacketDeclarePolicy based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZhoneCpePweLossPacketDeclarePolicy_Type.__name__ = "Unsigned32"
_ZhoneCpePweLossPacketDeclarePolicy_Object = MibTableColumn
zhoneCpePweLossPacketDeclarePolicy = _ZhoneCpePweLossPacketDeclarePolicy_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 30),
    _ZhoneCpePweLossPacketDeclarePolicy_Type()
)
zhoneCpePweLossPacketDeclarePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweLossPacketDeclarePolicy.setStatus("current")


class _ZhoneCpePweLossPacketClearPolicy_Type(Unsigned32):
    """Custom type zhoneCpePweLossPacketClearPolicy based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneCpePweLossPacketClearPolicy_Type.__name__ = "Unsigned32"
_ZhoneCpePweLossPacketClearPolicy_Object = MibTableColumn
zhoneCpePweLossPacketClearPolicy = _ZhoneCpePweLossPacketClearPolicy_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 31),
    _ZhoneCpePweLossPacketClearPolicy_Type()
)
zhoneCpePweLossPacketClearPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweLossPacketClearPolicy.setStatus("current")


class _ZhoneCpePweOverrunUnderrunDeclarePolicy_Type(Unsigned32):
    """Custom type zhoneCpePweOverrunUnderrunDeclarePolicy based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZhoneCpePweOverrunUnderrunDeclarePolicy_Type.__name__ = "Unsigned32"
_ZhoneCpePweOverrunUnderrunDeclarePolicy_Object = MibTableColumn
zhoneCpePweOverrunUnderrunDeclarePolicy = _ZhoneCpePweOverrunUnderrunDeclarePolicy_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 32),
    _ZhoneCpePweOverrunUnderrunDeclarePolicy_Type()
)
zhoneCpePweOverrunUnderrunDeclarePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweOverrunUnderrunDeclarePolicy.setStatus("current")


class _ZhoneCpePweOverrunUnderrunClearPolicy_Type(Unsigned32):
    """Custom type zhoneCpePweOverrunUnderrunClearPolicy based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneCpePweOverrunUnderrunClearPolicy_Type.__name__ = "Unsigned32"
_ZhoneCpePweOverrunUnderrunClearPolicy_Object = MibTableColumn
zhoneCpePweOverrunUnderrunClearPolicy = _ZhoneCpePweOverrunUnderrunClearPolicy_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 33),
    _ZhoneCpePweOverrunUnderrunClearPolicy_Type()
)
zhoneCpePweOverrunUnderrunClearPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweOverrunUnderrunClearPolicy.setStatus("current")


class _ZhoneCpePweMalformedDeclarePolicy_Type(Unsigned32):
    """Custom type zhoneCpePweMalformedDeclarePolicy based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZhoneCpePweMalformedDeclarePolicy_Type.__name__ = "Unsigned32"
_ZhoneCpePweMalformedDeclarePolicy_Object = MibTableColumn
zhoneCpePweMalformedDeclarePolicy = _ZhoneCpePweMalformedDeclarePolicy_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 34),
    _ZhoneCpePweMalformedDeclarePolicy_Type()
)
zhoneCpePweMalformedDeclarePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweMalformedDeclarePolicy.setStatus("current")


class _ZhoneCpePweMalformedClearPolicy_Type(Unsigned32):
    """Custom type zhoneCpePweMalformedClearPolicy based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneCpePweMalformedClearPolicy_Type.__name__ = "Unsigned32"
_ZhoneCpePweMalformedClearPolicy_Object = MibTableColumn
zhoneCpePweMalformedClearPolicy = _ZhoneCpePweMalformedClearPolicy_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 35),
    _ZhoneCpePweMalformedClearPolicy_Type()
)
zhoneCpePweMalformedClearPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweMalformedClearPolicy.setStatus("current")


class _ZhoneCpePweRBitTransmitSetPolicy_Type(Unsigned32):
    """Custom type zhoneCpePweRBitTransmitSetPolicy based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneCpePweRBitTransmitSetPolicy_Type.__name__ = "Unsigned32"
_ZhoneCpePweRBitTransmitSetPolicy_Object = MibTableColumn
zhoneCpePweRBitTransmitSetPolicy = _ZhoneCpePweRBitTransmitSetPolicy_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 36),
    _ZhoneCpePweRBitTransmitSetPolicy_Type()
)
zhoneCpePweRBitTransmitSetPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweRBitTransmitSetPolicy.setStatus("current")


class _ZhoneCpePweRBitTransmitClearPolicy_Type(Unsigned32):
    """Custom type zhoneCpePweRBitTransmitClearPolicy based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneCpePweRBitTransmitClearPolicy_Type.__name__ = "Unsigned32"
_ZhoneCpePweRBitTransmitClearPolicy_Object = MibTableColumn
zhoneCpePweRBitTransmitClearPolicy = _ZhoneCpePweRBitTransmitClearPolicy_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 37),
    _ZhoneCpePweRBitTransmitClearPolicy_Type()
)
zhoneCpePweRBitTransmitClearPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweRBitTransmitClearPolicy.setStatus("current")


class _ZhoneCpePweRBitReceivePolicy_Type(Integer32):
    """Custom type zhoneCpePweRBitReceivePolicy based on Integer32"""
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
        *(("alarm", 2),
          ("idlechannel", 3),
          ("nothing", 1))
    )


_ZhoneCpePweRBitReceivePolicy_Type.__name__ = "Integer32"
_ZhoneCpePweRBitReceivePolicy_Object = MibTableColumn
zhoneCpePweRBitReceivePolicy = _ZhoneCpePweRBitReceivePolicy_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 38),
    _ZhoneCpePweRBitReceivePolicy_Type()
)
zhoneCpePweRBitReceivePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweRBitReceivePolicy.setStatus("current")


class _ZhoneCpePweLBitReceivePolicy_Type(Integer32):
    """Custom type zhoneCpePweLBitReceivePolicy based on Integer32"""
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
        *(("ais", 1),
          ("idlechannel", 3),
          ("repeatlastpkt", 2))
    )


_ZhoneCpePweLBitReceivePolicy_Type.__name__ = "Integer32"
_ZhoneCpePweLBitReceivePolicy_Object = MibTableColumn
zhoneCpePweLBitReceivePolicy = _ZhoneCpePweLBitReceivePolicy_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 39),
    _ZhoneCpePweLBitReceivePolicy_Type()
)
zhoneCpePweLBitReceivePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweLBitReceivePolicy.setStatus("current")


class _ZhoneCpePweSesThreshold_Type(Unsigned32):
    """Custom type zhoneCpePweSesThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneCpePweSesThreshold_Type.__name__ = "Unsigned32"
_ZhoneCpePweSesThreshold_Object = MibTableColumn
zhoneCpePweSesThreshold = _ZhoneCpePweSesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 40),
    _ZhoneCpePweSesThreshold_Type()
)
zhoneCpePweSesThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweSesThreshold.setStatus("current")


class _ZhoneCpePweCdvTolerance_Type(Unsigned32):
    """Custom type zhoneCpePweCdvTolerance based on Unsigned32"""
    defaultValue = 750

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneCpePweCdvTolerance_Type.__name__ = "Unsigned32"
_ZhoneCpePweCdvTolerance_Object = MibTableColumn
zhoneCpePweCdvTolerance = _ZhoneCpePweCdvTolerance_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 41),
    _ZhoneCpePweCdvTolerance_Type()
)
zhoneCpePweCdvTolerance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweCdvTolerance.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpePweCdvTolerance.setUnits("microseconds")


class _ZhoneCpePweChannelAssociatedSignalling_Type(Integer32):
    """Custom type zhoneCpePweChannelAssociatedSignalling based on Integer32"""
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
        *(("base", 1),
          ("ds1esfcas", 4),
          ("e1cas", 2),
          ("j2cas", 5),
          ("sfcas", 3))
    )


_ZhoneCpePweChannelAssociatedSignalling_Type.__name__ = "Integer32"
_ZhoneCpePweChannelAssociatedSignalling_Object = MibTableColumn
zhoneCpePweChannelAssociatedSignalling = _ZhoneCpePweChannelAssociatedSignalling_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 42),
    _ZhoneCpePweChannelAssociatedSignalling_Type()
)
zhoneCpePweChannelAssociatedSignalling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweChannelAssociatedSignalling.setStatus("current")


class _ZhoneCpePweMplsTpType_Type(Integer32):
    """Custom type zhoneCpePweMplsTpType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("gem", 2))
    )


_ZhoneCpePweMplsTpType_Type.__name__ = "Integer32"
_ZhoneCpePweMplsTpType_Object = MibTableColumn
zhoneCpePweMplsTpType = _ZhoneCpePweMplsTpType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 43),
    _ZhoneCpePweMplsTpType_Type()
)
zhoneCpePweMplsTpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweMplsTpType.setStatus("current")


class _ZhoneCpePweDscp_Type(OctetString):
    """Custom type zhoneCpePweDscp based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ZhoneCpePweDscp_Type.__name__ = "OctetString"
_ZhoneCpePweDscp_Object = MibTableColumn
zhoneCpePweDscp = _ZhoneCpePweDscp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 12, 2, 1, 44),
    _ZhoneCpePweDscp_Type()
)
zhoneCpePweDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePweDscp.setStatus("current")
_ZhoneCpeOnuModelInfoTable_Object = MibTable
zhoneCpeOnuModelInfoTable = _ZhoneCpeOnuModelInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13)
)
if mibBuilder.loadTexts:
    zhoneCpeOnuModelInfoTable.setStatus("current")
_ZhoneCpeOnuModelInfoEntry_Object = MibTableRow
zhoneCpeOnuModelInfoEntry = _ZhoneCpeOnuModelInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1)
)
zhoneCpeOnuModelInfoEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeOnuModelInfoIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeOnuModelInfoEntry.setStatus("current")


class _ZhoneCpeOnuModelInfoIndex_Type(Unsigned32):
    """Custom type zhoneCpeOnuModelInfoIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeOnuModelInfoIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeOnuModelInfoIndex_Object = MibTableColumn
zhoneCpeOnuModelInfoIndex = _ZhoneCpeOnuModelInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1, 1),
    _ZhoneCpeOnuModelInfoIndex_Type()
)
zhoneCpeOnuModelInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeOnuModelInfoIndex.setStatus("current")
_ZhoneCpeOnuModelName_Type = ZhoneAdminString
_ZhoneCpeOnuModelName_Object = MibTableColumn
zhoneCpeOnuModelName = _ZhoneCpeOnuModelName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1, 2),
    _ZhoneCpeOnuModelName_Type()
)
zhoneCpeOnuModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeOnuModelName.setStatus("current")
_ZhoneCpeOnuBatteryBackup_Type = TruthValue
_ZhoneCpeOnuBatteryBackup_Object = MibTableColumn
zhoneCpeOnuBatteryBackup = _ZhoneCpeOnuBatteryBackup_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1, 3),
    _ZhoneCpeOnuBatteryBackup_Type()
)
zhoneCpeOnuBatteryBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeOnuBatteryBackup.setStatus("current")
_ZhoneCpeOnuSipPlarSupported_Type = TruthValue
_ZhoneCpeOnuSipPlarSupported_Object = MibTableColumn
zhoneCpeOnuSipPlarSupported = _ZhoneCpeOnuSipPlarSupported_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1, 4),
    _ZhoneCpeOnuSipPlarSupported_Type()
)
zhoneCpeOnuSipPlarSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeOnuSipPlarSupported.setStatus("current")


class _ZhoneCpeOnuEthSlotNumber_Type(Unsigned32):
    """Custom type zhoneCpeOnuEthSlotNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeOnuEthSlotNumber_Type.__name__ = "Unsigned32"
_ZhoneCpeOnuEthSlotNumber_Object = MibTableColumn
zhoneCpeOnuEthSlotNumber = _ZhoneCpeOnuEthSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1, 5),
    _ZhoneCpeOnuEthSlotNumber_Type()
)
zhoneCpeOnuEthSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeOnuEthSlotNumber.setStatus("current")


class _ZhoneCpeOnuNumberOfEthPorts_Type(Unsigned32):
    """Custom type zhoneCpeOnuNumberOfEthPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeOnuNumberOfEthPorts_Type.__name__ = "Unsigned32"
_ZhoneCpeOnuNumberOfEthPorts_Object = MibTableColumn
zhoneCpeOnuNumberOfEthPorts = _ZhoneCpeOnuNumberOfEthPorts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1, 6),
    _ZhoneCpeOnuNumberOfEthPorts_Type()
)
zhoneCpeOnuNumberOfEthPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeOnuNumberOfEthPorts.setStatus("current")


class _ZhoneCpeOnuPotsSlotNumber_Type(Unsigned32):
    """Custom type zhoneCpeOnuPotsSlotNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeOnuPotsSlotNumber_Type.__name__ = "Unsigned32"
_ZhoneCpeOnuPotsSlotNumber_Object = MibTableColumn
zhoneCpeOnuPotsSlotNumber = _ZhoneCpeOnuPotsSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1, 7),
    _ZhoneCpeOnuPotsSlotNumber_Type()
)
zhoneCpeOnuPotsSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeOnuPotsSlotNumber.setStatus("current")


class _ZhoneCpeOnuNumberOfPotsPorts_Type(Unsigned32):
    """Custom type zhoneCpeOnuNumberOfPotsPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeOnuNumberOfPotsPorts_Type.__name__ = "Unsigned32"
_ZhoneCpeOnuNumberOfPotsPorts_Object = MibTableColumn
zhoneCpeOnuNumberOfPotsPorts = _ZhoneCpeOnuNumberOfPotsPorts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1, 8),
    _ZhoneCpeOnuNumberOfPotsPorts_Type()
)
zhoneCpeOnuNumberOfPotsPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeOnuNumberOfPotsPorts.setStatus("current")


class _ZhoneCpeOnuRfVideoSlotNumber_Type(Unsigned32):
    """Custom type zhoneCpeOnuRfVideoSlotNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeOnuRfVideoSlotNumber_Type.__name__ = "Unsigned32"
_ZhoneCpeOnuRfVideoSlotNumber_Object = MibTableColumn
zhoneCpeOnuRfVideoSlotNumber = _ZhoneCpeOnuRfVideoSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1, 9),
    _ZhoneCpeOnuRfVideoSlotNumber_Type()
)
zhoneCpeOnuRfVideoSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeOnuRfVideoSlotNumber.setStatus("current")


class _ZhoneCpeOnuNumberOfRfVideoPorts_Type(Unsigned32):
    """Custom type zhoneCpeOnuNumberOfRfVideoPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeOnuNumberOfRfVideoPorts_Type.__name__ = "Unsigned32"
_ZhoneCpeOnuNumberOfRfVideoPorts_Object = MibTableColumn
zhoneCpeOnuNumberOfRfVideoPorts = _ZhoneCpeOnuNumberOfRfVideoPorts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1, 10),
    _ZhoneCpeOnuNumberOfRfVideoPorts_Type()
)
zhoneCpeOnuNumberOfRfVideoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeOnuNumberOfRfVideoPorts.setStatus("current")


class _ZhoneCpeOnuCesSlotNumber_Type(Unsigned32):
    """Custom type zhoneCpeOnuCesSlotNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeOnuCesSlotNumber_Type.__name__ = "Unsigned32"
_ZhoneCpeOnuCesSlotNumber_Object = MibTableColumn
zhoneCpeOnuCesSlotNumber = _ZhoneCpeOnuCesSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1, 11),
    _ZhoneCpeOnuCesSlotNumber_Type()
)
zhoneCpeOnuCesSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeOnuCesSlotNumber.setStatus("current")


class _ZhoneCpeOnuNumberOfCesPorts_Type(Unsigned32):
    """Custom type zhoneCpeOnuNumberOfCesPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeOnuNumberOfCesPorts_Type.__name__ = "Unsigned32"
_ZhoneCpeOnuNumberOfCesPorts_Object = MibTableColumn
zhoneCpeOnuNumberOfCesPorts = _ZhoneCpeOnuNumberOfCesPorts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1, 12),
    _ZhoneCpeOnuNumberOfCesPorts_Type()
)
zhoneCpeOnuNumberOfCesPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeOnuNumberOfCesPorts.setStatus("current")
_ZhoneCpeOnuModelInfoRGBridged_Type = TruthValue
_ZhoneCpeOnuModelInfoRGBridged_Object = MibTableColumn
zhoneCpeOnuModelInfoRGBridged = _ZhoneCpeOnuModelInfoRGBridged_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1, 13),
    _ZhoneCpeOnuModelInfoRGBridged_Type()
)
zhoneCpeOnuModelInfoRGBridged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeOnuModelInfoRGBridged.setStatus("current")
_ZhoneCpeOnuNumberOfWlanPorts_Type = Unsigned32
_ZhoneCpeOnuNumberOfWlanPorts_Object = MibTableColumn
zhoneCpeOnuNumberOfWlanPorts = _ZhoneCpeOnuNumberOfWlanPorts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1, 14),
    _ZhoneCpeOnuNumberOfWlanPorts_Type()
)
zhoneCpeOnuNumberOfWlanPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeOnuNumberOfWlanPorts.setStatus("current")
_ZhoneCpeOnuModelInfoRg_Type = TruthValue
_ZhoneCpeOnuModelInfoRg_Object = MibTableColumn
zhoneCpeOnuModelInfoRg = _ZhoneCpeOnuModelInfoRg_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1, 15),
    _ZhoneCpeOnuModelInfoRg_Type()
)
zhoneCpeOnuModelInfoRg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeOnuModelInfoRg.setStatus("current")
_ZhoneCpeOnuModelInfoRgVoip_Type = TruthValue
_ZhoneCpeOnuModelInfoRgVoip_Object = MibTableColumn
zhoneCpeOnuModelInfoRgVoip = _ZhoneCpeOnuModelInfoRgVoip_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1, 16),
    _ZhoneCpeOnuModelInfoRgVoip_Type()
)
zhoneCpeOnuModelInfoRgVoip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeOnuModelInfoRgVoip.setStatus("current")
_ZhoneCpeOnuModelInfoRgPwe_Type = TruthValue
_ZhoneCpeOnuModelInfoRgPwe_Object = MibTableColumn
zhoneCpeOnuModelInfoRgPwe = _ZhoneCpeOnuModelInfoRgPwe_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1, 17),
    _ZhoneCpeOnuModelInfoRgPwe_Type()
)
zhoneCpeOnuModelInfoRgPwe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeOnuModelInfoRgPwe.setStatus("current")
_ZhoneCpeOnuModelInfoTftpDnld_Type = TruthValue
_ZhoneCpeOnuModelInfoTftpDnld_Object = MibTableColumn
zhoneCpeOnuModelInfoTftpDnld = _ZhoneCpeOnuModelInfoTftpDnld_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1, 18),
    _ZhoneCpeOnuModelInfoTftpDnld_Type()
)
zhoneCpeOnuModelInfoTftpDnld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeOnuModelInfoTftpDnld.setStatus("current")
_ZhoneCpeOnuSipSupported_Type = TruthValue
_ZhoneCpeOnuSipSupported_Object = MibTableColumn
zhoneCpeOnuSipSupported = _ZhoneCpeOnuSipSupported_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1, 19),
    _ZhoneCpeOnuSipSupported_Type()
)
zhoneCpeOnuSipSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeOnuSipSupported.setStatus("current")
_ZhoneCpeOnuH248Supported_Type = TruthValue
_ZhoneCpeOnuH248Supported_Object = MibTableColumn
zhoneCpeOnuH248Supported = _ZhoneCpeOnuH248Supported_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1, 20),
    _ZhoneCpeOnuH248Supported_Type()
)
zhoneCpeOnuH248Supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeOnuH248Supported.setStatus("current")
_ZhoneCpeOnuMgcpSupported_Type = TruthValue
_ZhoneCpeOnuMgcpSupported_Object = MibTableColumn
zhoneCpeOnuMgcpSupported = _ZhoneCpeOnuMgcpSupported_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1, 21),
    _ZhoneCpeOnuMgcpSupported_Type()
)
zhoneCpeOnuMgcpSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeOnuMgcpSupported.setStatus("current")
_ZhoneCpeOnuT1Supported_Type = TruthValue
_ZhoneCpeOnuT1Supported_Object = MibTableColumn
zhoneCpeOnuT1Supported = _ZhoneCpeOnuT1Supported_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1, 22),
    _ZhoneCpeOnuT1Supported_Type()
)
zhoneCpeOnuT1Supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeOnuT1Supported.setStatus("current")
_ZhoneCpeOnuE1Supported_Type = TruthValue
_ZhoneCpeOnuE1Supported_Object = MibTableColumn
zhoneCpeOnuE1Supported = _ZhoneCpeOnuE1Supported_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1, 23),
    _ZhoneCpeOnuE1Supported_Type()
)
zhoneCpeOnuE1Supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeOnuE1Supported.setStatus("current")


class _ZhoneCpeOnuNumberOfPoEPorts_Type(Unsigned32):
    """Custom type zhoneCpeOnuNumberOfPoEPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeOnuNumberOfPoEPorts_Type.__name__ = "Unsigned32"
_ZhoneCpeOnuNumberOfPoEPorts_Object = MibTableColumn
zhoneCpeOnuNumberOfPoEPorts = _ZhoneCpeOnuNumberOfPoEPorts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 13, 1, 24),
    _ZhoneCpeOnuNumberOfPoEPorts_Type()
)
zhoneCpeOnuNumberOfPoEPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeOnuNumberOfPoEPorts.setStatus("current")
_ZhoneCpeConnectionTable_Object = MibTable
zhoneCpeConnectionTable = _ZhoneCpeConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 14)
)
if mibBuilder.loadTexts:
    zhoneCpeConnectionTable.setStatus("current")
_ZhoneCpeConnectionEntry_Object = MibTableRow
zhoneCpeConnectionEntry = _ZhoneCpeConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 14, 1)
)
zhoneCpeConnectionEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpePortIfIndex"),
    (0, "Zhone-CPE-MIB", "zhoneCpeTpType"),
    (0, "Zhone-CPE-MIB", "zhoneCpeTpIndex"),
    (0, "Zhone-CPE-MIB", "zhoneCpeVlanId"),
    (0, "Zhone-CPE-MIB", "zhoneCpeSlanId"),
)
if mibBuilder.loadTexts:
    zhoneCpeConnectionEntry.setStatus("current")
_ZhoneCpePortIfIndex_Type = InterfaceIndex
_ZhoneCpePortIfIndex_Object = MibTableColumn
zhoneCpePortIfIndex = _ZhoneCpePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 14, 1, 1),
    _ZhoneCpePortIfIndex_Type()
)
zhoneCpePortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpePortIfIndex.setStatus("current")
_ZhoneCpeTpType_Type = TpType
_ZhoneCpeTpType_Object = MibTableColumn
zhoneCpeTpType = _ZhoneCpeTpType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 14, 1, 2),
    _ZhoneCpeTpType_Type()
)
zhoneCpeTpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeTpType.setStatus("current")


class _ZhoneCpeTpIndex_Type(Unsigned32):
    """Custom type zhoneCpeTpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneCpeTpIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeTpIndex_Object = MibTableColumn
zhoneCpeTpIndex = _ZhoneCpeTpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 14, 1, 3),
    _ZhoneCpeTpIndex_Type()
)
zhoneCpeTpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeTpIndex.setStatus("current")


class _ZhoneCpeVlanId_Type(Unsigned32):
    """Custom type zhoneCpeVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ZhoneCpeVlanId_Type.__name__ = "Unsigned32"
_ZhoneCpeVlanId_Object = MibTableColumn
zhoneCpeVlanId = _ZhoneCpeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 14, 1, 4),
    _ZhoneCpeVlanId_Type()
)
zhoneCpeVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeVlanId.setStatus("current")


class _ZhoneCpeSlanId_Type(Unsigned32):
    """Custom type zhoneCpeSlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ZhoneCpeSlanId_Type.__name__ = "Unsigned32"
_ZhoneCpeSlanId_Object = MibTableColumn
zhoneCpeSlanId = _ZhoneCpeSlanId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 14, 1, 5),
    _ZhoneCpeSlanId_Type()
)
zhoneCpeSlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeSlanId.setStatus("current")
_ZhoneCpeConnectionRowStatus_Type = ZhoneRowStatus
_ZhoneCpeConnectionRowStatus_Object = MibTableColumn
zhoneCpeConnectionRowStatus = _ZhoneCpeConnectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 14, 1, 6),
    _ZhoneCpeConnectionRowStatus_Type()
)
zhoneCpeConnectionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeConnectionRowStatus.setStatus("current")


class _ZhoneCpeConnectionVlanCos_Type(Unsigned32):
    """Custom type zhoneCpeConnectionVlanCos based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ZhoneCpeConnectionVlanCos_Type.__name__ = "Unsigned32"
_ZhoneCpeConnectionVlanCos_Object = MibTableColumn
zhoneCpeConnectionVlanCos = _ZhoneCpeConnectionVlanCos_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 14, 1, 7),
    _ZhoneCpeConnectionVlanCos_Type()
)
zhoneCpeConnectionVlanCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeConnectionVlanCos.setStatus("current")


class _ZhoneCpeConnectionVlanTpId_Type(Unsigned32):
    """Custom type zhoneCpeConnectionVlanTpId based on Unsigned32"""
    defaultValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(33024, 33024),
        ValueRangeConstraint(34984, 34984),
        ValueRangeConstraint(37120, 37120),
        ValueRangeConstraint(37376, 37376),
    )


_ZhoneCpeConnectionVlanTpId_Type.__name__ = "Unsigned32"
_ZhoneCpeConnectionVlanTpId_Object = MibTableColumn
zhoneCpeConnectionVlanTpId = _ZhoneCpeConnectionVlanTpId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 14, 1, 8),
    _ZhoneCpeConnectionVlanTpId_Type()
)
zhoneCpeConnectionVlanTpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeConnectionVlanTpId.setStatus("current")


class _ZhoneCpeConnectionSlanCos_Type(Unsigned32):
    """Custom type zhoneCpeConnectionSlanCos based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ZhoneCpeConnectionSlanCos_Type.__name__ = "Unsigned32"
_ZhoneCpeConnectionSlanCos_Object = MibTableColumn
zhoneCpeConnectionSlanCos = _ZhoneCpeConnectionSlanCos_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 14, 1, 9),
    _ZhoneCpeConnectionSlanCos_Type()
)
zhoneCpeConnectionSlanCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeConnectionSlanCos.setStatus("current")


class _ZhoneCpeConnectionSlanTpId_Type(Unsigned32):
    """Custom type zhoneCpeConnectionSlanTpId based on Unsigned32"""
    defaultValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(33024, 33024),
        ValueRangeConstraint(34984, 34984),
        ValueRangeConstraint(37120, 37120),
        ValueRangeConstraint(37376, 37376),
    )


_ZhoneCpeConnectionSlanTpId_Type.__name__ = "Unsigned32"
_ZhoneCpeConnectionSlanTpId_Object = MibTableColumn
zhoneCpeConnectionSlanTpId = _ZhoneCpeConnectionSlanTpId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 14, 1, 10),
    _ZhoneCpeConnectionSlanTpId_Type()
)
zhoneCpeConnectionSlanTpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeConnectionSlanTpId.setStatus("current")


class _ZhoneCpeConnectionTranslateVlanId_Type(Unsigned32):
    """Custom type zhoneCpeConnectionTranslateVlanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ZhoneCpeConnectionTranslateVlanId_Type.__name__ = "Unsigned32"
_ZhoneCpeConnectionTranslateVlanId_Object = MibTableColumn
zhoneCpeConnectionTranslateVlanId = _ZhoneCpeConnectionTranslateVlanId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 14, 1, 11),
    _ZhoneCpeConnectionTranslateVlanId_Type()
)
zhoneCpeConnectionTranslateVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeConnectionTranslateVlanId.setStatus("current")


class _ZhoneCpeConnectionTranslateVlanCos_Type(Unsigned32):
    """Custom type zhoneCpeConnectionTranslateVlanCos based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ZhoneCpeConnectionTranslateVlanCos_Type.__name__ = "Unsigned32"
_ZhoneCpeConnectionTranslateVlanCos_Object = MibTableColumn
zhoneCpeConnectionTranslateVlanCos = _ZhoneCpeConnectionTranslateVlanCos_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 14, 1, 12),
    _ZhoneCpeConnectionTranslateVlanCos_Type()
)
zhoneCpeConnectionTranslateVlanCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeConnectionTranslateVlanCos.setStatus("current")


class _ZhoneCpeConnectionTranslateVlanTpId_Type(Unsigned32):
    """Custom type zhoneCpeConnectionTranslateVlanTpId based on Unsigned32"""
    defaultValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(33024, 33024),
        ValueRangeConstraint(34984, 34984),
        ValueRangeConstraint(37120, 37120),
        ValueRangeConstraint(37376, 37376),
    )


_ZhoneCpeConnectionTranslateVlanTpId_Type.__name__ = "Unsigned32"
_ZhoneCpeConnectionTranslateVlanTpId_Object = MibTableColumn
zhoneCpeConnectionTranslateVlanTpId = _ZhoneCpeConnectionTranslateVlanTpId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 14, 1, 13),
    _ZhoneCpeConnectionTranslateVlanTpId_Type()
)
zhoneCpeConnectionTranslateVlanTpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeConnectionTranslateVlanTpId.setStatus("current")


class _ZhoneCpeConnectionTranslateSlanId_Type(Unsigned32):
    """Custom type zhoneCpeConnectionTranslateSlanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ZhoneCpeConnectionTranslateSlanId_Type.__name__ = "Unsigned32"
_ZhoneCpeConnectionTranslateSlanId_Object = MibTableColumn
zhoneCpeConnectionTranslateSlanId = _ZhoneCpeConnectionTranslateSlanId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 14, 1, 14),
    _ZhoneCpeConnectionTranslateSlanId_Type()
)
zhoneCpeConnectionTranslateSlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeConnectionTranslateSlanId.setStatus("current")


class _ZhoneCpeConnectionTranslateSlanCos_Type(Unsigned32):
    """Custom type zhoneCpeConnectionTranslateSlanCos based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ZhoneCpeConnectionTranslateSlanCos_Type.__name__ = "Unsigned32"
_ZhoneCpeConnectionTranslateSlanCos_Object = MibTableColumn
zhoneCpeConnectionTranslateSlanCos = _ZhoneCpeConnectionTranslateSlanCos_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 14, 1, 15),
    _ZhoneCpeConnectionTranslateSlanCos_Type()
)
zhoneCpeConnectionTranslateSlanCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeConnectionTranslateSlanCos.setStatus("current")


class _ZhoneCpeConnectionTranslateSlanTpId_Type(Unsigned32):
    """Custom type zhoneCpeConnectionTranslateSlanTpId based on Unsigned32"""
    defaultValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(33024, 33024),
        ValueRangeConstraint(34984, 34984),
        ValueRangeConstraint(37120, 37120),
        ValueRangeConstraint(37376, 37376),
    )


_ZhoneCpeConnectionTranslateSlanTpId_Type.__name__ = "Unsigned32"
_ZhoneCpeConnectionTranslateSlanTpId_Object = MibTableColumn
zhoneCpeConnectionTranslateSlanTpId = _ZhoneCpeConnectionTranslateSlanTpId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 14, 1, 16),
    _ZhoneCpeConnectionTranslateSlanTpId_Type()
)
zhoneCpeConnectionTranslateSlanTpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeConnectionTranslateSlanTpId.setStatus("current")


class _ZhoneCpeConnectionFloodingGport_Type(Unsigned32):
    """Custom type zhoneCpeConnectionFloodingGport based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_ZhoneCpeConnectionFloodingGport_Type.__name__ = "Unsigned32"
_ZhoneCpeConnectionFloodingGport_Object = MibTableColumn
zhoneCpeConnectionFloodingGport = _ZhoneCpeConnectionFloodingGport_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 14, 1, 17),
    _ZhoneCpeConnectionFloodingGport_Type()
)
zhoneCpeConnectionFloodingGport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeConnectionFloodingGport.setStatus("current")


class _ZhoneCpeConnectionVideoGport_Type(Unsigned32):
    """Custom type zhoneCpeConnectionVideoGport based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_ZhoneCpeConnectionVideoGport_Type.__name__ = "Unsigned32"
_ZhoneCpeConnectionVideoGport_Object = MibTableColumn
zhoneCpeConnectionVideoGport = _ZhoneCpeConnectionVideoGport_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 14, 1, 18),
    _ZhoneCpeConnectionVideoGport_Type()
)
zhoneCpeConnectionVideoGport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeConnectionVideoGport.setStatus("current")


class _ZhoneCpeConnectionDscpToCosProfileIndex_Type(Unsigned32):
    """Custom type zhoneCpeConnectionDscpToCosProfileIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeConnectionDscpToCosProfileIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeConnectionDscpToCosProfileIndex_Object = MibTableColumn
zhoneCpeConnectionDscpToCosProfileIndex = _ZhoneCpeConnectionDscpToCosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 14, 1, 19),
    _ZhoneCpeConnectionDscpToCosProfileIndex_Type()
)
zhoneCpeConnectionDscpToCosProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeConnectionDscpToCosProfileIndex.setStatus("current")


class _ZhoneCpeConnectionRgMode_Type(Integer32):
    """Custom type zhoneCpeConnectionRgMode based on Integer32"""
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
        *(("bpppoe", 4),
          ("bridged", 5),
          ("brouted", 2),
          ("notApplicable", 6),
          ("routed", 1),
          ("rpppoe", 3))
    )


_ZhoneCpeConnectionRgMode_Type.__name__ = "Integer32"
_ZhoneCpeConnectionRgMode_Object = MibTableColumn
zhoneCpeConnectionRgMode = _ZhoneCpeConnectionRgMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 14, 1, 20),
    _ZhoneCpeConnectionRgMode_Type()
)
zhoneCpeConnectionRgMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeConnectionRgMode.setStatus("current")


class _ZhoneCpeConnectionGuidedVlanId_Type(Unsigned32):
    """Custom type zhoneCpeConnectionGuidedVlanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ZhoneCpeConnectionGuidedVlanId_Type.__name__ = "Unsigned32"
_ZhoneCpeConnectionGuidedVlanId_Object = MibTableColumn
zhoneCpeConnectionGuidedVlanId = _ZhoneCpeConnectionGuidedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 14, 1, 21),
    _ZhoneCpeConnectionGuidedVlanId_Type()
)
zhoneCpeConnectionGuidedVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeConnectionGuidedVlanId.setStatus("current")


class _ZhoneCpeConnectionGuidedCos_Type(Unsigned32):
    """Custom type zhoneCpeConnectionGuidedCos based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ZhoneCpeConnectionGuidedCos_Type.__name__ = "Unsigned32"
_ZhoneCpeConnectionGuidedCos_Object = MibTableColumn
zhoneCpeConnectionGuidedCos = _ZhoneCpeConnectionGuidedCos_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 14, 1, 22),
    _ZhoneCpeConnectionGuidedCos_Type()
)
zhoneCpeConnectionGuidedCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeConnectionGuidedCos.setStatus("current")
_ZhoneCpeRfSubscriberTable_Object = MibTable
zhoneCpeRfSubscriberTable = _ZhoneCpeRfSubscriberTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 15)
)
if mibBuilder.loadTexts:
    zhoneCpeRfSubscriberTable.setStatus("current")
_ZhoneCpeRfSubscriberEntry_Object = MibTableRow
zhoneCpeRfSubscriberEntry = _ZhoneCpeRfSubscriberEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 15, 1)
)
zhoneCpeRfSubscriberEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeIfIndex"),
    (0, "Zhone-CPE-MIB", "zhoneCpeRfSubscriberPortNumber"),
)
if mibBuilder.loadTexts:
    zhoneCpeRfSubscriberEntry.setStatus("current")


class _ZhoneCpeRfSubscriberPortNumber_Type(Unsigned32):
    """Custom type zhoneCpeRfSubscriberPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeRfSubscriberPortNumber_Type.__name__ = "Unsigned32"
_ZhoneCpeRfSubscriberPortNumber_Object = MibTableColumn
zhoneCpeRfSubscriberPortNumber = _ZhoneCpeRfSubscriberPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 15, 1, 1),
    _ZhoneCpeRfSubscriberPortNumber_Type()
)
zhoneCpeRfSubscriberPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeRfSubscriberPortNumber.setStatus("current")


class _ZhoneCpeRfSubscriberRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpeRfSubscriberRowStatus based on ZhoneRowStatus"""


_ZhoneCpeRfSubscriberRowStatus_Object = MibTableColumn
zhoneCpeRfSubscriberRowStatus = _ZhoneCpeRfSubscriberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 15, 1, 2),
    _ZhoneCpeRfSubscriberRowStatus_Type()
)
zhoneCpeRfSubscriberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeRfSubscriberRowStatus.setStatus("current")


class _ZhoneCpeRfSubscriberAdminState_Type(ZhoneAdminState):
    """Custom type zhoneCpeRfSubscriberAdminState based on ZhoneAdminState"""
    defaultValue = 1


_ZhoneCpeRfSubscriberAdminState_Object = MibTableColumn
zhoneCpeRfSubscriberAdminState = _ZhoneCpeRfSubscriberAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 15, 1, 3),
    _ZhoneCpeRfSubscriberAdminState_Type()
)
zhoneCpeRfSubscriberAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeRfSubscriberAdminState.setStatus("current")


class _ZhoneCpeRfSubscriberLineStatusAlarm_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeRfSubscriberLineStatusAlarm based on ZhoneEnabledFlag"""


_ZhoneCpeRfSubscriberLineStatusAlarm_Object = MibTableColumn
zhoneCpeRfSubscriberLineStatusAlarm = _ZhoneCpeRfSubscriberLineStatusAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 15, 1, 4),
    _ZhoneCpeRfSubscriberLineStatusAlarm_Type()
)
zhoneCpeRfSubscriberLineStatusAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeRfSubscriberLineStatusAlarm.setStatus("current")


class _ZhoneCpeRfSubscriberAlarmSeverity_Type(ZhoneAlarmSeverity):
    """Custom type zhoneCpeRfSubscriberAlarmSeverity based on ZhoneAlarmSeverity"""


_ZhoneCpeRfSubscriberAlarmSeverity_Object = MibTableColumn
zhoneCpeRfSubscriberAlarmSeverity = _ZhoneCpeRfSubscriberAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 15, 1, 5),
    _ZhoneCpeRfSubscriberAlarmSeverity_Type()
)
zhoneCpeRfSubscriberAlarmSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeRfSubscriberAlarmSeverity.setStatus("current")
_ZhoneCpeTrafficManagement_ObjectIdentity = ObjectIdentity
zhoneCpeTrafficManagement = _ZhoneCpeTrafficManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 16)
)
if mibBuilder.loadTexts:
    zhoneCpeTrafficManagement.setStatus("current")
_ZhoneCpeTrafficManagementIndexNext_Type = Integer32
_ZhoneCpeTrafficManagementIndexNext_Object = MibScalar
zhoneCpeTrafficManagementIndexNext = _ZhoneCpeTrafficManagementIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 16, 1),
    _ZhoneCpeTrafficManagementIndexNext_Type()
)
zhoneCpeTrafficManagementIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeTrafficManagementIndexNext.setStatus("current")
_ZhoneCpeTrafficManagementTable_Object = MibTable
zhoneCpeTrafficManagementTable = _ZhoneCpeTrafficManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 16, 2)
)
if mibBuilder.loadTexts:
    zhoneCpeTrafficManagementTable.setStatus("current")
_ZhoneCpeTrafficManagementEntry_Object = MibTableRow
zhoneCpeTrafficManagementEntry = _ZhoneCpeTrafficManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 16, 2, 1)
)
zhoneCpeTrafficManagementEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeTrafficManagementIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeTrafficManagementEntry.setStatus("current")


class _ZhoneCpeTrafficManagementIndex_Type(Unsigned32):
    """Custom type zhoneCpeTrafficManagementIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeTrafficManagementIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeTrafficManagementIndex_Object = MibTableColumn
zhoneCpeTrafficManagementIndex = _ZhoneCpeTrafficManagementIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 16, 2, 1, 1),
    _ZhoneCpeTrafficManagementIndex_Type()
)
zhoneCpeTrafficManagementIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeTrafficManagementIndex.setStatus("current")


class _ZhoneCpeTrafficManagementRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpeTrafficManagementRowStatus based on ZhoneRowStatus"""


_ZhoneCpeTrafficManagementRowStatus_Object = MibTableColumn
zhoneCpeTrafficManagementRowStatus = _ZhoneCpeTrafficManagementRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 16, 2, 1, 2),
    _ZhoneCpeTrafficManagementRowStatus_Type()
)
zhoneCpeTrafficManagementRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeTrafficManagementRowStatus.setStatus("current")
_ZhoneCpeTrafficManagementProfileName_Type = ZhoneAdminString
_ZhoneCpeTrafficManagementProfileName_Object = MibTableColumn
zhoneCpeTrafficManagementProfileName = _ZhoneCpeTrafficManagementProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 16, 2, 1, 3),
    _ZhoneCpeTrafficManagementProfileName_Type()
)
zhoneCpeTrafficManagementProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeTrafficManagementProfileName.setStatus("current")


class _ZhoneCpeTrafficManagementUpstreamSIR_Type(Unsigned32):
    """Custom type zhoneCpeTrafficManagementUpstreamSIR based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1310720),
    )


_ZhoneCpeTrafficManagementUpstreamSIR_Type.__name__ = "Unsigned32"
_ZhoneCpeTrafficManagementUpstreamSIR_Object = MibTableColumn
zhoneCpeTrafficManagementUpstreamSIR = _ZhoneCpeTrafficManagementUpstreamSIR_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 16, 2, 1, 4),
    _ZhoneCpeTrafficManagementUpstreamSIR_Type()
)
zhoneCpeTrafficManagementUpstreamSIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeTrafficManagementUpstreamSIR.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeTrafficManagementUpstreamSIR.setUnits("kbps")


class _ZhoneCpeTrafficManagementUpstreamPIR_Type(Unsigned32):
    """Custom type zhoneCpeTrafficManagementUpstreamPIR based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1310720),
    )


_ZhoneCpeTrafficManagementUpstreamPIR_Type.__name__ = "Unsigned32"
_ZhoneCpeTrafficManagementUpstreamPIR_Object = MibTableColumn
zhoneCpeTrafficManagementUpstreamPIR = _ZhoneCpeTrafficManagementUpstreamPIR_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 16, 2, 1, 5),
    _ZhoneCpeTrafficManagementUpstreamPIR_Type()
)
zhoneCpeTrafficManagementUpstreamPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeTrafficManagementUpstreamPIR.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeTrafficManagementUpstreamPIR.setUnits("kbps")


class _ZhoneCpeTrafficManagementUpstreamPriority_Type(Unsigned32):
    """Custom type zhoneCpeTrafficManagementUpstreamPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneCpeTrafficManagementUpstreamPriority_Type.__name__ = "Unsigned32"
_ZhoneCpeTrafficManagementUpstreamPriority_Object = MibTableColumn
zhoneCpeTrafficManagementUpstreamPriority = _ZhoneCpeTrafficManagementUpstreamPriority_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 16, 2, 1, 6),
    _ZhoneCpeTrafficManagementUpstreamPriority_Type()
)
zhoneCpeTrafficManagementUpstreamPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeTrafficManagementUpstreamPriority.setStatus("current")


class _ZhoneCpeTrafficManagementUpstreamWeight_Type(Unsigned32):
    """Custom type zhoneCpeTrafficManagementUpstreamWeight based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneCpeTrafficManagementUpstreamWeight_Type.__name__ = "Unsigned32"
_ZhoneCpeTrafficManagementUpstreamWeight_Object = MibTableColumn
zhoneCpeTrafficManagementUpstreamWeight = _ZhoneCpeTrafficManagementUpstreamWeight_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 16, 2, 1, 7),
    _ZhoneCpeTrafficManagementUpstreamWeight_Type()
)
zhoneCpeTrafficManagementUpstreamWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeTrafficManagementUpstreamWeight.setStatus("current")


class _ZhoneCpeTrafficManagementDownstreamSIR_Type(Unsigned32):
    """Custom type zhoneCpeTrafficManagementDownstreamSIR based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1310720),
    )


_ZhoneCpeTrafficManagementDownstreamSIR_Type.__name__ = "Unsigned32"
_ZhoneCpeTrafficManagementDownstreamSIR_Object = MibTableColumn
zhoneCpeTrafficManagementDownstreamSIR = _ZhoneCpeTrafficManagementDownstreamSIR_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 16, 2, 1, 8),
    _ZhoneCpeTrafficManagementDownstreamSIR_Type()
)
zhoneCpeTrafficManagementDownstreamSIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeTrafficManagementDownstreamSIR.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeTrafficManagementDownstreamSIR.setUnits("kbps")


class _ZhoneCpeTrafficManagementDownstreamPIR_Type(Unsigned32):
    """Custom type zhoneCpeTrafficManagementDownstreamPIR based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1310720),
    )


_ZhoneCpeTrafficManagementDownstreamPIR_Type.__name__ = "Unsigned32"
_ZhoneCpeTrafficManagementDownstreamPIR_Object = MibTableColumn
zhoneCpeTrafficManagementDownstreamPIR = _ZhoneCpeTrafficManagementDownstreamPIR_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 16, 2, 1, 9),
    _ZhoneCpeTrafficManagementDownstreamPIR_Type()
)
zhoneCpeTrafficManagementDownstreamPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeTrafficManagementDownstreamPIR.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeTrafficManagementDownstreamPIR.setUnits("kbps")


class _ZhoneCpeTrafficManagementDownstreamPriority_Type(Unsigned32):
    """Custom type zhoneCpeTrafficManagementDownstreamPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneCpeTrafficManagementDownstreamPriority_Type.__name__ = "Unsigned32"
_ZhoneCpeTrafficManagementDownstreamPriority_Object = MibTableColumn
zhoneCpeTrafficManagementDownstreamPriority = _ZhoneCpeTrafficManagementDownstreamPriority_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 16, 2, 1, 10),
    _ZhoneCpeTrafficManagementDownstreamPriority_Type()
)
zhoneCpeTrafficManagementDownstreamPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeTrafficManagementDownstreamPriority.setStatus("current")


class _ZhoneCpeTrafficManagementDownstreamWeight_Type(Unsigned32):
    """Custom type zhoneCpeTrafficManagementDownstreamWeight based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneCpeTrafficManagementDownstreamWeight_Type.__name__ = "Unsigned32"
_ZhoneCpeTrafficManagementDownstreamWeight_Object = MibTableColumn
zhoneCpeTrafficManagementDownstreamWeight = _ZhoneCpeTrafficManagementDownstreamWeight_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 16, 2, 1, 11),
    _ZhoneCpeTrafficManagementDownstreamWeight_Type()
)
zhoneCpeTrafficManagementDownstreamWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeTrafficManagementDownstreamWeight.setStatus("current")


class _ZhoneCpeTrafficManagementPeakBurstSize_Type(Unsigned32):
    """Custom type zhoneCpeTrafficManagementPeakBurstSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512000),
    )


_ZhoneCpeTrafficManagementPeakBurstSize_Type.__name__ = "Unsigned32"
_ZhoneCpeTrafficManagementPeakBurstSize_Object = MibTableColumn
zhoneCpeTrafficManagementPeakBurstSize = _ZhoneCpeTrafficManagementPeakBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 16, 2, 1, 12),
    _ZhoneCpeTrafficManagementPeakBurstSize_Type()
)
zhoneCpeTrafficManagementPeakBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeTrafficManagementPeakBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeTrafficManagementPeakBurstSize.setUnits("bytes")
_ZhoneCpeSystemTable_Object = MibTable
zhoneCpeSystemTable = _ZhoneCpeSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 17)
)
if mibBuilder.loadTexts:
    zhoneCpeSystemTable.setStatus("current")
_ZhoneCpeSystemEntry_Object = MibTableRow
zhoneCpeSystemEntry = _ZhoneCpeSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 17, 1)
)
zhoneCpeSystemEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeIfIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeSystemEntry.setStatus("current")


class _ZhoneCpeSystemRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpeSystemRowStatus based on ZhoneRowStatus"""


_ZhoneCpeSystemRowStatus_Object = MibTableColumn
zhoneCpeSystemRowStatus = _ZhoneCpeSystemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 17, 1, 1),
    _ZhoneCpeSystemRowStatus_Type()
)
zhoneCpeSystemRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeSystemRowStatus.setStatus("current")


class _ZhoneCpeSystemCommonProfileIndex_Type(Unsigned32):
    """Custom type zhoneCpeSystemCommonProfileIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeSystemCommonProfileIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeSystemCommonProfileIndex_Object = MibTableColumn
zhoneCpeSystemCommonProfileIndex = _ZhoneCpeSystemCommonProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 17, 1, 2),
    _ZhoneCpeSystemCommonProfileIndex_Type()
)
zhoneCpeSystemCommonProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeSystemCommonProfileIndex.setStatus("current")


class _ZhoneCpeSystemMgcpClientName_Type(OctetString):
    """Custom type zhoneCpeSystemMgcpClientName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZhoneCpeSystemMgcpClientName_Type.__name__ = "OctetString"
_ZhoneCpeSystemMgcpClientName_Object = MibTableColumn
zhoneCpeSystemMgcpClientName = _ZhoneCpeSystemMgcpClientName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 17, 1, 3),
    _ZhoneCpeSystemMgcpClientName_Type()
)
zhoneCpeSystemMgcpClientName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeSystemMgcpClientName.setStatus("current")
_ZhoneCpeSystemCommon_ObjectIdentity = ObjectIdentity
zhoneCpeSystemCommon = _ZhoneCpeSystemCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 18)
)
if mibBuilder.loadTexts:
    zhoneCpeSystemCommon.setStatus("current")
_ZhoneCpeSystemCommonIndexNext_Type = Unsigned32
_ZhoneCpeSystemCommonIndexNext_Object = MibScalar
zhoneCpeSystemCommonIndexNext = _ZhoneCpeSystemCommonIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 18, 1),
    _ZhoneCpeSystemCommonIndexNext_Type()
)
zhoneCpeSystemCommonIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeSystemCommonIndexNext.setStatus("current")
_ZhoneCpeSystemCommonTable_Object = MibTable
zhoneCpeSystemCommonTable = _ZhoneCpeSystemCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 18, 2)
)
if mibBuilder.loadTexts:
    zhoneCpeSystemCommonTable.setStatus("current")
_ZhoneCpeSystemCommonEntry_Object = MibTableRow
zhoneCpeSystemCommonEntry = _ZhoneCpeSystemCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 18, 2, 1)
)
zhoneCpeSystemCommonEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeSystemCommonIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeSystemCommonEntry.setStatus("current")


class _ZhoneCpeSystemCommonIndex_Type(Unsigned32):
    """Custom type zhoneCpeSystemCommonIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeSystemCommonIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeSystemCommonIndex_Object = MibTableColumn
zhoneCpeSystemCommonIndex = _ZhoneCpeSystemCommonIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 18, 2, 1, 1),
    _ZhoneCpeSystemCommonIndex_Type()
)
zhoneCpeSystemCommonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeSystemCommonIndex.setStatus("current")


class _ZhoneCpeSystemCommonRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpeSystemCommonRowStatus based on ZhoneRowStatus"""


_ZhoneCpeSystemCommonRowStatus_Object = MibTableColumn
zhoneCpeSystemCommonRowStatus = _ZhoneCpeSystemCommonRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 18, 2, 1, 2),
    _ZhoneCpeSystemCommonRowStatus_Type()
)
zhoneCpeSystemCommonRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeSystemCommonRowStatus.setStatus("current")
_ZhoneCpeSystemCommonProfileName_Type = ZhoneAdminString
_ZhoneCpeSystemCommonProfileName_Object = MibTableColumn
zhoneCpeSystemCommonProfileName = _ZhoneCpeSystemCommonProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 18, 2, 1, 3),
    _ZhoneCpeSystemCommonProfileName_Type()
)
zhoneCpeSystemCommonProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeSystemCommonProfileName.setStatus("current")


class _ZhoneCpeSystemCommonFirewall_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeSystemCommonFirewall based on ZhoneEnabledFlag"""


_ZhoneCpeSystemCommonFirewall_Object = MibTableColumn
zhoneCpeSystemCommonFirewall = _ZhoneCpeSystemCommonFirewall_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 18, 2, 1, 4),
    _ZhoneCpeSystemCommonFirewall_Type()
)
zhoneCpeSystemCommonFirewall.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeSystemCommonFirewall.setStatus("current")


class _ZhoneCpeSystemCommonSyncCookieProtection_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeSystemCommonSyncCookieProtection based on ZhoneEnabledFlag"""


_ZhoneCpeSystemCommonSyncCookieProtection_Object = MibTableColumn
zhoneCpeSystemCommonSyncCookieProtection = _ZhoneCpeSystemCommonSyncCookieProtection_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 18, 2, 1, 5),
    _ZhoneCpeSystemCommonSyncCookieProtection_Type()
)
zhoneCpeSystemCommonSyncCookieProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeSystemCommonSyncCookieProtection.setStatus("current")


class _ZhoneCpeSystemCommonCrossVlanRouting_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeSystemCommonCrossVlanRouting based on ZhoneEnabledFlag"""


_ZhoneCpeSystemCommonCrossVlanRouting_Object = MibTableColumn
zhoneCpeSystemCommonCrossVlanRouting = _ZhoneCpeSystemCommonCrossVlanRouting_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 18, 2, 1, 6),
    _ZhoneCpeSystemCommonCrossVlanRouting_Type()
)
zhoneCpeSystemCommonCrossVlanRouting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeSystemCommonCrossVlanRouting.setStatus("current")


class _ZhoneCpeStaticRouteListProfileIndex_Type(Unsigned32):
    """Custom type zhoneCpeStaticRouteListProfileIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeStaticRouteListProfileIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeStaticRouteListProfileIndex_Object = MibTableColumn
zhoneCpeStaticRouteListProfileIndex = _ZhoneCpeStaticRouteListProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 18, 2, 1, 7),
    _ZhoneCpeStaticRouteListProfileIndex_Type()
)
zhoneCpeStaticRouteListProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeStaticRouteListProfileIndex.setStatus("current")


class _ZhoneCpeDnsHostListProfile_Type(Unsigned32):
    """Custom type zhoneCpeDnsHostListProfile based on Unsigned32"""
    defaultValue = 0


_ZhoneCpeDnsHostListProfile_Object = MibTableColumn
zhoneCpeDnsHostListProfile = _ZhoneCpeDnsHostListProfile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 18, 2, 1, 8),
    _ZhoneCpeDnsHostListProfile_Type()
)
zhoneCpeDnsHostListProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeDnsHostListProfile.setStatus("current")


class _ZhoneCpeSystemCommonTr69Inform_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeSystemCommonTr69Inform based on ZhoneEnabledFlag"""


_ZhoneCpeSystemCommonTr69Inform_Object = MibTableColumn
zhoneCpeSystemCommonTr69Inform = _ZhoneCpeSystemCommonTr69Inform_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 18, 2, 1, 9),
    _ZhoneCpeSystemCommonTr69Inform_Type()
)
zhoneCpeSystemCommonTr69Inform.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeSystemCommonTr69Inform.setStatus("current")
_ZhoneCpeSystemCommonInformInterval_Type = Unsigned32
_ZhoneCpeSystemCommonInformInterval_Object = MibTableColumn
zhoneCpeSystemCommonInformInterval = _ZhoneCpeSystemCommonInformInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 18, 2, 1, 10),
    _ZhoneCpeSystemCommonInformInterval_Type()
)
zhoneCpeSystemCommonInformInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeSystemCommonInformInterval.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeSystemCommonInformInterval.setUnits("seconds")


class _ZhoneCpeSystemCommonAcsUrl_Type(OctetString):
    """Custom type zhoneCpeSystemCommonAcsUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ZhoneCpeSystemCommonAcsUrl_Type.__name__ = "OctetString"
_ZhoneCpeSystemCommonAcsUrl_Object = MibTableColumn
zhoneCpeSystemCommonAcsUrl = _ZhoneCpeSystemCommonAcsUrl_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 18, 2, 1, 11),
    _ZhoneCpeSystemCommonAcsUrl_Type()
)
zhoneCpeSystemCommonAcsUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeSystemCommonAcsUrl.setStatus("current")


class _ZhoneCpeSystemCommonAcsUsername_Type(OctetString):
    """Custom type zhoneCpeSystemCommonAcsUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZhoneCpeSystemCommonAcsUsername_Type.__name__ = "OctetString"
_ZhoneCpeSystemCommonAcsUsername_Object = MibTableColumn
zhoneCpeSystemCommonAcsUsername = _ZhoneCpeSystemCommonAcsUsername_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 18, 2, 1, 12),
    _ZhoneCpeSystemCommonAcsUsername_Type()
)
zhoneCpeSystemCommonAcsUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeSystemCommonAcsUsername.setStatus("current")


class _ZhoneCpeSystemCommonAcsPassword_Type(OctetString):
    """Custom type zhoneCpeSystemCommonAcsPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZhoneCpeSystemCommonAcsPassword_Type.__name__ = "OctetString"
_ZhoneCpeSystemCommonAcsPassword_Object = MibTableColumn
zhoneCpeSystemCommonAcsPassword = _ZhoneCpeSystemCommonAcsPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 18, 2, 1, 13),
    _ZhoneCpeSystemCommonAcsPassword_Type()
)
zhoneCpeSystemCommonAcsPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeSystemCommonAcsPassword.setStatus("current")


class _ZhoneCpeSystemCommonAdminPassword_Type(OctetString):
    """Custom type zhoneCpeSystemCommonAdminPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZhoneCpeSystemCommonAdminPassword_Type.__name__ = "OctetString"
_ZhoneCpeSystemCommonAdminPassword_Object = MibTableColumn
zhoneCpeSystemCommonAdminPassword = _ZhoneCpeSystemCommonAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 18, 2, 1, 14),
    _ZhoneCpeSystemCommonAdminPassword_Type()
)
zhoneCpeSystemCommonAdminPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeSystemCommonAdminPassword.setStatus("current")


class _ZhoneCpeSystemCommonSupportPassword_Type(OctetString):
    """Custom type zhoneCpeSystemCommonSupportPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZhoneCpeSystemCommonSupportPassword_Type.__name__ = "OctetString"
_ZhoneCpeSystemCommonSupportPassword_Object = MibTableColumn
zhoneCpeSystemCommonSupportPassword = _ZhoneCpeSystemCommonSupportPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 18, 2, 1, 15),
    _ZhoneCpeSystemCommonSupportPassword_Type()
)
zhoneCpeSystemCommonSupportPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeSystemCommonSupportPassword.setStatus("current")


class _ZhoneCpeSystemCommonUserPassword_Type(OctetString):
    """Custom type zhoneCpeSystemCommonUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZhoneCpeSystemCommonUserPassword_Type.__name__ = "OctetString"
_ZhoneCpeSystemCommonUserPassword_Object = MibTableColumn
zhoneCpeSystemCommonUserPassword = _ZhoneCpeSystemCommonUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 18, 2, 1, 16),
    _ZhoneCpeSystemCommonUserPassword_Type()
)
zhoneCpeSystemCommonUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeSystemCommonUserPassword.setStatus("current")


class _ZhoneCpeSystemCommonPowerSupply_Type(Unsigned32):
    """Custom type zhoneCpeSystemCommonPowerSupply based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeSystemCommonPowerSupply_Type.__name__ = "Unsigned32"
_ZhoneCpeSystemCommonPowerSupply_Object = MibTableColumn
zhoneCpeSystemCommonPowerSupply = _ZhoneCpeSystemCommonPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 18, 2, 1, 17),
    _ZhoneCpeSystemCommonPowerSupply_Type()
)
zhoneCpeSystemCommonPowerSupply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeSystemCommonPowerSupply.setStatus("current")


class _ZhoneCpeSystemCommonPowerShutdownDelay_Type(Unsigned32):
    """Custom type zhoneCpeSystemCommonPowerShutdownDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_ZhoneCpeSystemCommonPowerShutdownDelay_Type.__name__ = "Unsigned32"
_ZhoneCpeSystemCommonPowerShutdownDelay_Object = MibTableColumn
zhoneCpeSystemCommonPowerShutdownDelay = _ZhoneCpeSystemCommonPowerShutdownDelay_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 18, 2, 1, 18),
    _ZhoneCpeSystemCommonPowerShutdownDelay_Type()
)
zhoneCpeSystemCommonPowerShutdownDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeSystemCommonPowerShutdownDelay.setStatus("current")


class _ZhoneCpeSystemCommonPowerRestoreDelay_Type(Unsigned32):
    """Custom type zhoneCpeSystemCommonPowerRestoreDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_ZhoneCpeSystemCommonPowerRestoreDelay_Type.__name__ = "Unsigned32"
_ZhoneCpeSystemCommonPowerRestoreDelay_Object = MibTableColumn
zhoneCpeSystemCommonPowerRestoreDelay = _ZhoneCpeSystemCommonPowerRestoreDelay_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 18, 2, 1, 19),
    _ZhoneCpeSystemCommonPowerRestoreDelay_Type()
)
zhoneCpeSystemCommonPowerRestoreDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeSystemCommonPowerRestoreDelay.setStatus("current")
_ZhoneCpeInterfaceVlanTable_Object = MibTable
zhoneCpeInterfaceVlanTable = _ZhoneCpeInterfaceVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 19)
)
if mibBuilder.loadTexts:
    zhoneCpeInterfaceVlanTable.setStatus("current")
_ZhoneCpeInterfaceVlanEntry_Object = MibTableRow
zhoneCpeInterfaceVlanEntry = _ZhoneCpeInterfaceVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 19, 1)
)
zhoneCpeInterfaceVlanEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeIfIndex"),
    (0, "Zhone-CPE-MIB", "zhoneCpeTpType"),
    (0, "Zhone-CPE-MIB", "zhoneCpeTpIndex"),
    (0, "Zhone-CPE-MIB", "zhoneCpeVlanId"),
    (0, "Zhone-CPE-MIB", "zhoneCpeSlanId"),
)
if mibBuilder.loadTexts:
    zhoneCpeInterfaceVlanEntry.setStatus("current")


class _ZhoneCpeInterfaceVlanRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpeInterfaceVlanRowStatus based on ZhoneRowStatus"""


_ZhoneCpeInterfaceVlanRowStatus_Object = MibTableColumn
zhoneCpeInterfaceVlanRowStatus = _ZhoneCpeInterfaceVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 19, 1, 1),
    _ZhoneCpeInterfaceVlanRowStatus_Type()
)
zhoneCpeInterfaceVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeInterfaceVlanRowStatus.setStatus("current")


class _ZhoneCpeInterfaceVlanRgMode_Type(Integer32):
    """Custom type zhoneCpeInterfaceVlanRgMode based on Integer32"""
    defaultValue = 2

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
        *(("bridged", 5),
          ("bridgedpppoe", 4),
          ("brouted", 2),
          ("routed", 1),
          ("routedpppoe", 3))
    )


_ZhoneCpeInterfaceVlanRgMode_Type.__name__ = "Integer32"
_ZhoneCpeInterfaceVlanRgMode_Object = MibTableColumn
zhoneCpeInterfaceVlanRgMode = _ZhoneCpeInterfaceVlanRgMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 19, 1, 2),
    _ZhoneCpeInterfaceVlanRgMode_Type()
)
zhoneCpeInterfaceVlanRgMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeInterfaceVlanRgMode.setStatus("current")


class _ZhoneCpeInterfaceVlanTranslateVlanId_Type(Unsigned32):
    """Custom type zhoneCpeInterfaceVlanTranslateVlanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ZhoneCpeInterfaceVlanTranslateVlanId_Type.__name__ = "Unsigned32"
_ZhoneCpeInterfaceVlanTranslateVlanId_Object = MibTableColumn
zhoneCpeInterfaceVlanTranslateVlanId = _ZhoneCpeInterfaceVlanTranslateVlanId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 19, 1, 3),
    _ZhoneCpeInterfaceVlanTranslateVlanId_Type()
)
zhoneCpeInterfaceVlanTranslateVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeInterfaceVlanTranslateVlanId.setStatus("current")


class _ZhoneCpeInterfaceVlanTranslateVlanCos_Type(Unsigned32):
    """Custom type zhoneCpeInterfaceVlanTranslateVlanCos based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ZhoneCpeInterfaceVlanTranslateVlanCos_Type.__name__ = "Unsigned32"
_ZhoneCpeInterfaceVlanTranslateVlanCos_Object = MibTableColumn
zhoneCpeInterfaceVlanTranslateVlanCos = _ZhoneCpeInterfaceVlanTranslateVlanCos_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 19, 1, 4),
    _ZhoneCpeInterfaceVlanTranslateVlanCos_Type()
)
zhoneCpeInterfaceVlanTranslateVlanCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeInterfaceVlanTranslateVlanCos.setStatus("current")


class _ZhoneCpeInterfaceVlanTranslateSlanId_Type(Unsigned32):
    """Custom type zhoneCpeInterfaceVlanTranslateSlanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ZhoneCpeInterfaceVlanTranslateSlanId_Type.__name__ = "Unsigned32"
_ZhoneCpeInterfaceVlanTranslateSlanId_Object = MibTableColumn
zhoneCpeInterfaceVlanTranslateSlanId = _ZhoneCpeInterfaceVlanTranslateSlanId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 19, 1, 5),
    _ZhoneCpeInterfaceVlanTranslateSlanId_Type()
)
zhoneCpeInterfaceVlanTranslateSlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeInterfaceVlanTranslateSlanId.setStatus("current")


class _ZhoneCpeInterfaceVlanTranslateSlanCos_Type(Unsigned32):
    """Custom type zhoneCpeInterfaceVlanTranslateSlanCos based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ZhoneCpeInterfaceVlanTranslateSlanCos_Type.__name__ = "Unsigned32"
_ZhoneCpeInterfaceVlanTranslateSlanCos_Object = MibTableColumn
zhoneCpeInterfaceVlanTranslateSlanCos = _ZhoneCpeInterfaceVlanTranslateSlanCos_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 19, 1, 6),
    _ZhoneCpeInterfaceVlanTranslateSlanCos_Type()
)
zhoneCpeInterfaceVlanTranslateSlanCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeInterfaceVlanTranslateSlanCos.setStatus("current")


class _ZhoneCpeInterfaceVlanTranslateSlanTpId_Type(Unsigned32):
    """Custom type zhoneCpeInterfaceVlanTranslateSlanTpId based on Unsigned32"""
    defaultValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(33024, 33024),
        ValueRangeConstraint(34984, 34984),
        ValueRangeConstraint(37120, 37120),
        ValueRangeConstraint(37376, 37376),
    )


_ZhoneCpeInterfaceVlanTranslateSlanTpId_Type.__name__ = "Unsigned32"
_ZhoneCpeInterfaceVlanTranslateSlanTpId_Object = MibTableColumn
zhoneCpeInterfaceVlanTranslateSlanTpId = _ZhoneCpeInterfaceVlanTranslateSlanTpId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 19, 1, 7),
    _ZhoneCpeInterfaceVlanTranslateSlanTpId_Type()
)
zhoneCpeInterfaceVlanTranslateSlanTpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeInterfaceVlanTranslateSlanTpId.setStatus("current")


class _ZhoneCpeInterfaceVlanIpAddress_Type(IpAddress):
    """Custom type zhoneCpeInterfaceVlanIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_ZhoneCpeInterfaceVlanIpAddress_Object = MibTableColumn
zhoneCpeInterfaceVlanIpAddress = _ZhoneCpeInterfaceVlanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 19, 1, 8),
    _ZhoneCpeInterfaceVlanIpAddress_Type()
)
zhoneCpeInterfaceVlanIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeInterfaceVlanIpAddress.setStatus("current")


class _ZhoneCpeIpServerProfile_Type(Unsigned32):
    """Custom type zhoneCpeIpServerProfile based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeIpServerProfile_Type.__name__ = "Unsigned32"
_ZhoneCpeIpServerProfile_Object = MibTableColumn
zhoneCpeIpServerProfile = _ZhoneCpeIpServerProfile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 19, 1, 9),
    _ZhoneCpeIpServerProfile_Type()
)
zhoneCpeIpServerProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeIpServerProfile.setStatus("current")


class _ZhoneCpeDhcpServerProfileIndex_Type(Unsigned32):
    """Custom type zhoneCpeDhcpServerProfileIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeDhcpServerProfileIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeDhcpServerProfileIndex_Object = MibTableColumn
zhoneCpeDhcpServerProfileIndex = _ZhoneCpeDhcpServerProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 19, 1, 10),
    _ZhoneCpeDhcpServerProfileIndex_Type()
)
zhoneCpeDhcpServerProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeDhcpServerProfileIndex.setStatus("current")


class _ZhoneCpePortFwdListProfileIndex_Type(Unsigned32):
    """Custom type zhoneCpePortFwdListProfileIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpePortFwdListProfileIndex_Type.__name__ = "Unsigned32"
_ZhoneCpePortFwdListProfileIndex_Object = MibTableColumn
zhoneCpePortFwdListProfileIndex = _ZhoneCpePortFwdListProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 19, 1, 11),
    _ZhoneCpePortFwdListProfileIndex_Type()
)
zhoneCpePortFwdListProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePortFwdListProfileIndex.setStatus("current")
_ZhoneCpeDhcpServer_ObjectIdentity = ObjectIdentity
zhoneCpeDhcpServer = _ZhoneCpeDhcpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 20)
)
if mibBuilder.loadTexts:
    zhoneCpeDhcpServer.setStatus("current")
_ZhoneCpeDhcpServerIndexNext_Type = Integer32
_ZhoneCpeDhcpServerIndexNext_Object = MibScalar
zhoneCpeDhcpServerIndexNext = _ZhoneCpeDhcpServerIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 20, 1),
    _ZhoneCpeDhcpServerIndexNext_Type()
)
zhoneCpeDhcpServerIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeDhcpServerIndexNext.setStatus("current")
_ZhoneCpeDhcpServerTable_Object = MibTable
zhoneCpeDhcpServerTable = _ZhoneCpeDhcpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 20, 2)
)
if mibBuilder.loadTexts:
    zhoneCpeDhcpServerTable.setStatus("current")
_ZhoneCpeDhcpServerEntry_Object = MibTableRow
zhoneCpeDhcpServerEntry = _ZhoneCpeDhcpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 20, 2, 1)
)
zhoneCpeDhcpServerEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeDhcpServerIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeDhcpServerEntry.setStatus("current")


class _ZhoneCpeDhcpServerIndex_Type(Unsigned32):
    """Custom type zhoneCpeDhcpServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeDhcpServerIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeDhcpServerIndex_Object = MibTableColumn
zhoneCpeDhcpServerIndex = _ZhoneCpeDhcpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 20, 2, 1, 1),
    _ZhoneCpeDhcpServerIndex_Type()
)
zhoneCpeDhcpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeDhcpServerIndex.setStatus("current")


class _ZhoneCpeDhcpServerRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpeDhcpServerRowStatus based on ZhoneRowStatus"""


_ZhoneCpeDhcpServerRowStatus_Object = MibTableColumn
zhoneCpeDhcpServerRowStatus = _ZhoneCpeDhcpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 20, 2, 1, 2),
    _ZhoneCpeDhcpServerRowStatus_Type()
)
zhoneCpeDhcpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeDhcpServerRowStatus.setStatus("current")
_ZhoneCpeDhcpServerProfileName_Type = ZhoneAdminString
_ZhoneCpeDhcpServerProfileName_Object = MibTableColumn
zhoneCpeDhcpServerProfileName = _ZhoneCpeDhcpServerProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 20, 2, 1, 3),
    _ZhoneCpeDhcpServerProfileName_Type()
)
zhoneCpeDhcpServerProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeDhcpServerProfileName.setStatus("current")


class _ZhoneCpeDhcpServerStartAddress_Type(IpAddress):
    """Custom type zhoneCpeDhcpServerStartAddress based on IpAddress"""
    defaultHexValue = "00000000"


_ZhoneCpeDhcpServerStartAddress_Object = MibTableColumn
zhoneCpeDhcpServerStartAddress = _ZhoneCpeDhcpServerStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 20, 2, 1, 4),
    _ZhoneCpeDhcpServerStartAddress_Type()
)
zhoneCpeDhcpServerStartAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeDhcpServerStartAddress.setStatus("current")


class _ZhoneCpeDhcpServerEndAddress_Type(IpAddress):
    """Custom type zhoneCpeDhcpServerEndAddress based on IpAddress"""
    defaultHexValue = "00000000"


_ZhoneCpeDhcpServerEndAddress_Object = MibTableColumn
zhoneCpeDhcpServerEndAddress = _ZhoneCpeDhcpServerEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 20, 2, 1, 5),
    _ZhoneCpeDhcpServerEndAddress_Type()
)
zhoneCpeDhcpServerEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeDhcpServerEndAddress.setStatus("current")


class _ZhoneCpeDhcpServerLeaseTime_Type(Integer32):
    """Custom type zhoneCpeDhcpServerLeaseTime based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_ZhoneCpeDhcpServerLeaseTime_Type.__name__ = "Integer32"
_ZhoneCpeDhcpServerLeaseTime_Object = MibTableColumn
zhoneCpeDhcpServerLeaseTime = _ZhoneCpeDhcpServerLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 20, 2, 1, 6),
    _ZhoneCpeDhcpServerLeaseTime_Type()
)
zhoneCpeDhcpServerLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeDhcpServerLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeDhcpServerLeaseTime.setUnits("seconds")


class _ZhoneCpeDhcpServerConditionalServerListProfile_Type(Unsigned32):
    """Custom type zhoneCpeDhcpServerConditionalServerListProfile based on Unsigned32"""
    defaultValue = 0


_ZhoneCpeDhcpServerConditionalServerListProfile_Object = MibTableColumn
zhoneCpeDhcpServerConditionalServerListProfile = _ZhoneCpeDhcpServerConditionalServerListProfile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 20, 2, 1, 7),
    _ZhoneCpeDhcpServerConditionalServerListProfile_Type()
)
zhoneCpeDhcpServerConditionalServerListProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeDhcpServerConditionalServerListProfile.setStatus("current")
_ZhoneCpePppoeTable_Object = MibTable
zhoneCpePppoeTable = _ZhoneCpePppoeTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 21)
)
if mibBuilder.loadTexts:
    zhoneCpePppoeTable.setStatus("current")
_ZhoneCpePppoeEntry_Object = MibTableRow
zhoneCpePppoeEntry = _ZhoneCpePppoeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 21, 1)
)
zhoneCpePppoeEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeIfIndex"),
    (0, "Zhone-CPE-MIB", "zhoneCpeTpType"),
    (0, "Zhone-CPE-MIB", "zhoneCpeTpIndex"),
    (0, "Zhone-CPE-MIB", "zhoneCpeVlanId"),
    (0, "Zhone-CPE-MIB", "zhoneCpeSlanId"),
)
if mibBuilder.loadTexts:
    zhoneCpePppoeEntry.setStatus("current")


class _ZhoneCpePppoeRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpePppoeRowStatus based on ZhoneRowStatus"""


_ZhoneCpePppoeRowStatus_Object = MibTableColumn
zhoneCpePppoeRowStatus = _ZhoneCpePppoeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 21, 1, 1),
    _ZhoneCpePppoeRowStatus_Type()
)
zhoneCpePppoeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePppoeRowStatus.setStatus("current")


class _ZhoneCpePppoeUsername_Type(OctetString):
    """Custom type zhoneCpePppoeUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZhoneCpePppoeUsername_Type.__name__ = "OctetString"
_ZhoneCpePppoeUsername_Object = MibTableColumn
zhoneCpePppoeUsername = _ZhoneCpePppoeUsername_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 21, 1, 2),
    _ZhoneCpePppoeUsername_Type()
)
zhoneCpePppoeUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePppoeUsername.setStatus("current")


class _ZhoneCpePppoePassword_Type(OctetString):
    """Custom type zhoneCpePppoePassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_ZhoneCpePppoePassword_Type.__name__ = "OctetString"
_ZhoneCpePppoePassword_Object = MibTableColumn
zhoneCpePppoePassword = _ZhoneCpePppoePassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 21, 1, 3),
    _ZhoneCpePppoePassword_Type()
)
zhoneCpePppoePassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePppoePassword.setStatus("current")


class _ZhoneCpePppoeAuthentication_Type(Integer32):
    """Custom type zhoneCpePppoeAuthentication based on Integer32"""
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
        *(("auto", 1),
          ("chap", 3),
          ("mschap", 4),
          ("pap", 2))
    )


_ZhoneCpePppoeAuthentication_Type.__name__ = "Integer32"
_ZhoneCpePppoeAuthentication_Object = MibTableColumn
zhoneCpePppoeAuthentication = _ZhoneCpePppoeAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 21, 1, 4),
    _ZhoneCpePppoeAuthentication_Type()
)
zhoneCpePppoeAuthentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePppoeAuthentication.setStatus("current")


class _ZhoneCpePppoeRetryInterval_Type(Unsigned32):
    """Custom type zhoneCpePppoeRetryInterval based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpePppoeRetryInterval_Type.__name__ = "Unsigned32"
_ZhoneCpePppoeRetryInterval_Object = MibTableColumn
zhoneCpePppoeRetryInterval = _ZhoneCpePppoeRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 21, 1, 5),
    _ZhoneCpePppoeRetryInterval_Type()
)
zhoneCpePppoeRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePppoeRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpePppoeRetryInterval.setUnits("seconds")
_ZhoneCpeWlanSubscriberTable_Object = MibTable
zhoneCpeWlanSubscriberTable = _ZhoneCpeWlanSubscriberTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 22)
)
if mibBuilder.loadTexts:
    zhoneCpeWlanSubscriberTable.setStatus("current")
_ZhoneCpeWlanSubscriberEntry_Object = MibTableRow
zhoneCpeWlanSubscriberEntry = _ZhoneCpeWlanSubscriberEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 22, 1)
)
zhoneCpeWlanSubscriberEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeIfIndex"),
    (0, "Zhone-CPE-MIB", "zhoneCpeWlanSubscriberIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeWlanSubscriberEntry.setStatus("current")


class _ZhoneCpeWlanSubscriberIndex_Type(Unsigned32):
    """Custom type zhoneCpeWlanSubscriberIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeWlanSubscriberIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeWlanSubscriberIndex_Object = MibTableColumn
zhoneCpeWlanSubscriberIndex = _ZhoneCpeWlanSubscriberIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 22, 1, 1),
    _ZhoneCpeWlanSubscriberIndex_Type()
)
zhoneCpeWlanSubscriberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeWlanSubscriberIndex.setStatus("current")


class _ZhoneCpeWlanSubscriberRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpeWlanSubscriberRowStatus based on ZhoneRowStatus"""


_ZhoneCpeWlanSubscriberRowStatus_Object = MibTableColumn
zhoneCpeWlanSubscriberRowStatus = _ZhoneCpeWlanSubscriberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 22, 1, 2),
    _ZhoneCpeWlanSubscriberRowStatus_Type()
)
zhoneCpeWlanSubscriberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanSubscriberRowStatus.setStatus("current")


class _ZhoneCpeWlanSubscriberAdminState_Type(ZhoneAdminState):
    """Custom type zhoneCpeWlanSubscriberAdminState based on ZhoneAdminState"""
    defaultValue = 1


_ZhoneCpeWlanSubscriberAdminState_Object = MibTableColumn
zhoneCpeWlanSubscriberAdminState = _ZhoneCpeWlanSubscriberAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 22, 1, 3),
    _ZhoneCpeWlanSubscriberAdminState_Type()
)
zhoneCpeWlanSubscriberAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanSubscriberAdminState.setStatus("current")


class _ZhoneCpeWlanSubscriberSsid_Type(OctetString):
    """Custom type zhoneCpeWlanSubscriberSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZhoneCpeWlanSubscriberSsid_Type.__name__ = "OctetString"
_ZhoneCpeWlanSubscriberSsid_Object = MibTableColumn
zhoneCpeWlanSubscriberSsid = _ZhoneCpeWlanSubscriberSsid_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 22, 1, 4),
    _ZhoneCpeWlanSubscriberSsid_Type()
)
zhoneCpeWlanSubscriberSsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanSubscriberSsid.setStatus("current")


class _ZhoneCpeWlanSubscriberEncryptKey_Type(OctetString):
    """Custom type zhoneCpeWlanSubscriberEncryptKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZhoneCpeWlanSubscriberEncryptKey_Type.__name__ = "OctetString"
_ZhoneCpeWlanSubscriberEncryptKey_Object = MibTableColumn
zhoneCpeWlanSubscriberEncryptKey = _ZhoneCpeWlanSubscriberEncryptKey_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 22, 1, 5),
    _ZhoneCpeWlanSubscriberEncryptKey_Type()
)
zhoneCpeWlanSubscriberEncryptKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanSubscriberEncryptKey.setStatus("current")


class _ZhoneCpeWlanSubscriberDevicePin_Type(OctetString):
    """Custom type zhoneCpeWlanSubscriberDevicePin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ZhoneCpeWlanSubscriberDevicePin_Type.__name__ = "OctetString"
_ZhoneCpeWlanSubscriberDevicePin_Object = MibTableColumn
zhoneCpeWlanSubscriberDevicePin = _ZhoneCpeWlanSubscriberDevicePin_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 22, 1, 6),
    _ZhoneCpeWlanSubscriberDevicePin_Type()
)
zhoneCpeWlanSubscriberDevicePin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanSubscriberDevicePin.setStatus("current")


class _ZhoneCpeWlanSubscriberRadiusKey_Type(OctetString):
    """Custom type zhoneCpeWlanSubscriberRadiusKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 13),
    )


_ZhoneCpeWlanSubscriberRadiusKey_Type.__name__ = "OctetString"
_ZhoneCpeWlanSubscriberRadiusKey_Object = MibTableColumn
zhoneCpeWlanSubscriberRadiusKey = _ZhoneCpeWlanSubscriberRadiusKey_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 22, 1, 7),
    _ZhoneCpeWlanSubscriberRadiusKey_Type()
)
zhoneCpeWlanSubscriberRadiusKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanSubscriberRadiusKey.setStatus("current")


class _ZhoneCpeWlanProfileIndex_Type(Unsigned32):
    """Custom type zhoneCpeWlanProfileIndex based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeWlanProfileIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeWlanProfileIndex_Object = MibTableColumn
zhoneCpeWlanProfileIndex = _ZhoneCpeWlanProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 22, 1, 8),
    _ZhoneCpeWlanProfileIndex_Type()
)
zhoneCpeWlanProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanProfileIndex.setStatus("current")


class _ZhoneCpeAccessControlListProfileIndex_Type(Unsigned32):
    """Custom type zhoneCpeAccessControlListProfileIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeAccessControlListProfileIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeAccessControlListProfileIndex_Object = MibTableColumn
zhoneCpeAccessControlListProfileIndex = _ZhoneCpeAccessControlListProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 22, 1, 9),
    _ZhoneCpeAccessControlListProfileIndex_Type()
)
zhoneCpeAccessControlListProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeAccessControlListProfileIndex.setStatus("current")


class _ZhoneCpeWdsMacListProfileIndex_Type(Unsigned32):
    """Custom type zhoneCpeWdsMacListProfileIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeWdsMacListProfileIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeWdsMacListProfileIndex_Object = MibTableColumn
zhoneCpeWdsMacListProfileIndex = _ZhoneCpeWdsMacListProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 22, 1, 10),
    _ZhoneCpeWdsMacListProfileIndex_Type()
)
zhoneCpeWdsMacListProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWdsMacListProfileIndex.setStatus("current")


class _ZhoneCpeWlanAdvProfileIndex_Type(Unsigned32):
    """Custom type zhoneCpeWlanAdvProfileIndex based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeWlanAdvProfileIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeWlanAdvProfileIndex_Object = MibTableColumn
zhoneCpeWlanAdvProfileIndex = _ZhoneCpeWlanAdvProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 22, 1, 11),
    _ZhoneCpeWlanAdvProfileIndex_Type()
)
zhoneCpeWlanAdvProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvProfileIndex.setStatus("current")
_ZhoneCpeWlan_ObjectIdentity = ObjectIdentity
zhoneCpeWlan = _ZhoneCpeWlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 23)
)
if mibBuilder.loadTexts:
    zhoneCpeWlan.setStatus("current")
_ZhoneCpeWlanIndexNext_Type = Integer32
_ZhoneCpeWlanIndexNext_Object = MibScalar
zhoneCpeWlanIndexNext = _ZhoneCpeWlanIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 23, 1),
    _ZhoneCpeWlanIndexNext_Type()
)
zhoneCpeWlanIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeWlanIndexNext.setStatus("current")
_ZhoneCpeWlanTable_Object = MibTable
zhoneCpeWlanTable = _ZhoneCpeWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 23, 2)
)
if mibBuilder.loadTexts:
    zhoneCpeWlanTable.setStatus("current")
_ZhoneCpeWlanEntry_Object = MibTableRow
zhoneCpeWlanEntry = _ZhoneCpeWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 23, 2, 1)
)
zhoneCpeWlanEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeWlanIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeWlanEntry.setStatus("current")


class _ZhoneCpeWlanIndex_Type(Unsigned32):
    """Custom type zhoneCpeWlanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeWlanIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeWlanIndex_Object = MibTableColumn
zhoneCpeWlanIndex = _ZhoneCpeWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 23, 2, 1, 1),
    _ZhoneCpeWlanIndex_Type()
)
zhoneCpeWlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeWlanIndex.setStatus("current")


class _ZhoneCpeWlanRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpeWlanRowStatus based on ZhoneRowStatus"""


_ZhoneCpeWlanRowStatus_Object = MibTableColumn
zhoneCpeWlanRowStatus = _ZhoneCpeWlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 23, 2, 1, 2),
    _ZhoneCpeWlanRowStatus_Type()
)
zhoneCpeWlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanRowStatus.setStatus("current")
_ZhoneCpeWlanProfileName_Type = ZhoneAdminString
_ZhoneCpeWlanProfileName_Object = MibTableColumn
zhoneCpeWlanProfileName = _ZhoneCpeWlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 23, 2, 1, 3),
    _ZhoneCpeWlanProfileName_Type()
)
zhoneCpeWlanProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanProfileName.setStatus("current")


class _ZhoneCpeWlanHideAccessPoint_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeWlanHideAccessPoint based on ZhoneEnabledFlag"""


_ZhoneCpeWlanHideAccessPoint_Object = MibTableColumn
zhoneCpeWlanHideAccessPoint = _ZhoneCpeWlanHideAccessPoint_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 23, 2, 1, 4),
    _ZhoneCpeWlanHideAccessPoint_Type()
)
zhoneCpeWlanHideAccessPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanHideAccessPoint.setStatus("current")


class _ZhoneCpeWlanIsolateClients_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeWlanIsolateClients based on ZhoneEnabledFlag"""


_ZhoneCpeWlanIsolateClients_Object = MibTableColumn
zhoneCpeWlanIsolateClients = _ZhoneCpeWlanIsolateClients_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 23, 2, 1, 5),
    _ZhoneCpeWlanIsolateClients_Type()
)
zhoneCpeWlanIsolateClients.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanIsolateClients.setStatus("current")


class _ZhoneCpeWlanWmmAdvertise_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeWlanWmmAdvertise based on ZhoneEnabledFlag"""


_ZhoneCpeWlanWmmAdvertise_Object = MibTableColumn
zhoneCpeWlanWmmAdvertise = _ZhoneCpeWlanWmmAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 23, 2, 1, 6),
    _ZhoneCpeWlanWmmAdvertise_Type()
)
zhoneCpeWlanWmmAdvertise.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanWmmAdvertise.setStatus("current")


class _ZhoneCpeWlanMcastFwd_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeWlanMcastFwd based on ZhoneEnabledFlag"""


_ZhoneCpeWlanMcastFwd_Object = MibTableColumn
zhoneCpeWlanMcastFwd = _ZhoneCpeWlanMcastFwd_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 23, 2, 1, 7),
    _ZhoneCpeWlanMcastFwd_Type()
)
zhoneCpeWlanMcastFwd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanMcastFwd.setStatus("current")


class _ZhoneCpeWlanMaxClients_Type(Unsigned32):
    """Custom type zhoneCpeWlanMaxClients based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_ZhoneCpeWlanMaxClients_Type.__name__ = "Unsigned32"
_ZhoneCpeWlanMaxClients_Object = MibTableColumn
zhoneCpeWlanMaxClients = _ZhoneCpeWlanMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 23, 2, 1, 8),
    _ZhoneCpeWlanMaxClients_Type()
)
zhoneCpeWlanMaxClients.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanMaxClients.setStatus("current")


class _ZhoneCpeWlanNetAuthentication_Type(Integer32):
    """Custom type zhoneCpeWlanNetAuthentication based on Integer32"""
    defaultValue = 1

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
        *(("dot1x", 3),
          ("mixedwpa2wpa", 8),
          ("mixedwpa2wpapsk", 9),
          ("open", 1),
          ("shared", 2),
          ("wpa", 4),
          ("wpa2", 6),
          ("wpa2psk", 7),
          ("wpapsk", 5))
    )


_ZhoneCpeWlanNetAuthentication_Type.__name__ = "Integer32"
_ZhoneCpeWlanNetAuthentication_Object = MibTableColumn
zhoneCpeWlanNetAuthentication = _ZhoneCpeWlanNetAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 23, 2, 1, 9),
    _ZhoneCpeWlanNetAuthentication_Type()
)
zhoneCpeWlanNetAuthentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanNetAuthentication.setStatus("current")


class _ZhoneCpeWlanWpaGroupRekeyInterval_Type(Unsigned32):
    """Custom type zhoneCpeWlanWpaGroupRekeyInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeWlanWpaGroupRekeyInterval_Type.__name__ = "Unsigned32"
_ZhoneCpeWlanWpaGroupRekeyInterval_Object = MibTableColumn
zhoneCpeWlanWpaGroupRekeyInterval = _ZhoneCpeWlanWpaGroupRekeyInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 23, 2, 1, 10),
    _ZhoneCpeWlanWpaGroupRekeyInterval_Type()
)
zhoneCpeWlanWpaGroupRekeyInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanWpaGroupRekeyInterval.setStatus("current")


class _ZhoneCpeWlanWpaEncryption_Type(Integer32):
    """Custom type zhoneCpeWlanWpaEncryption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aes", 1),
          ("tkipaes", 2))
    )


_ZhoneCpeWlanWpaEncryption_Type.__name__ = "Integer32"
_ZhoneCpeWlanWpaEncryption_Object = MibTableColumn
zhoneCpeWlanWpaEncryption = _ZhoneCpeWlanWpaEncryption_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 23, 2, 1, 11),
    _ZhoneCpeWlanWpaEncryption_Type()
)
zhoneCpeWlanWpaEncryption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanWpaEncryption.setStatus("current")


class _ZhoneCpeWlanWepEncryption_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeWlanWepEncryption based on ZhoneEnabledFlag"""


_ZhoneCpeWlanWepEncryption_Object = MibTableColumn
zhoneCpeWlanWepEncryption = _ZhoneCpeWlanWepEncryption_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 23, 2, 1, 12),
    _ZhoneCpeWlanWepEncryption_Type()
)
zhoneCpeWlanWepEncryption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanWepEncryption.setStatus("current")


class _ZhoneCpeWlanWepStrength_Type(Integer32):
    """Custom type zhoneCpeWlanWepStrength based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bit128", 2),
          ("bit64", 1))
    )


_ZhoneCpeWlanWepStrength_Type.__name__ = "Integer32"
_ZhoneCpeWlanWepStrength_Object = MibTableColumn
zhoneCpeWlanWepStrength = _ZhoneCpeWlanWepStrength_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 23, 2, 1, 13),
    _ZhoneCpeWlanWepStrength_Type()
)
zhoneCpeWlanWepStrength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanWepStrength.setStatus("current")


class _ZhoneCpeWlanRadiusServerIp_Type(IpAddress):
    """Custom type zhoneCpeWlanRadiusServerIp based on IpAddress"""
    defaultHexValue = "00000000"


_ZhoneCpeWlanRadiusServerIp_Object = MibTableColumn
zhoneCpeWlanRadiusServerIp = _ZhoneCpeWlanRadiusServerIp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 23, 2, 1, 14),
    _ZhoneCpeWlanRadiusServerIp_Type()
)
zhoneCpeWlanRadiusServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanRadiusServerIp.setStatus("current")


class _ZhoneCpeWlanRadiusPort_Type(Unsigned32):
    """Custom type zhoneCpeWlanRadiusPort based on Unsigned32"""
    defaultValue = 1812

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_ZhoneCpeWlanRadiusPort_Type.__name__ = "Unsigned32"
_ZhoneCpeWlanRadiusPort_Object = MibTableColumn
zhoneCpeWlanRadiusPort = _ZhoneCpeWlanRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 23, 2, 1, 15),
    _ZhoneCpeWlanRadiusPort_Type()
)
zhoneCpeWlanRadiusPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanRadiusPort.setStatus("current")


class _ZhoneCpeWlanWpa2PreAuthentication_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeWlanWpa2PreAuthentication based on ZhoneEnabledFlag"""


_ZhoneCpeWlanWpa2PreAuthentication_Object = MibTableColumn
zhoneCpeWlanWpa2PreAuthentication = _ZhoneCpeWlanWpa2PreAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 23, 2, 1, 16),
    _ZhoneCpeWlanWpa2PreAuthentication_Type()
)
zhoneCpeWlanWpa2PreAuthentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanWpa2PreAuthentication.setStatus("current")


class _ZhoneCpeWlanNetReAuthenticationInterval_Type(Unsigned32):
    """Custom type zhoneCpeWlanNetReAuthenticationInterval based on Unsigned32"""
    defaultValue = 36000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeWlanNetReAuthenticationInterval_Type.__name__ = "Unsigned32"
_ZhoneCpeWlanNetReAuthenticationInterval_Object = MibTableColumn
zhoneCpeWlanNetReAuthenticationInterval = _ZhoneCpeWlanNetReAuthenticationInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 23, 2, 1, 17),
    _ZhoneCpeWlanNetReAuthenticationInterval_Type()
)
zhoneCpeWlanNetReAuthenticationInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanNetReAuthenticationInterval.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCpeWlanNetReAuthenticationInterval.setUnits("seconds")
_ZhoneCpeStaticRouteList_ObjectIdentity = ObjectIdentity
zhoneCpeStaticRouteList = _ZhoneCpeStaticRouteList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 24)
)
if mibBuilder.loadTexts:
    zhoneCpeStaticRouteList.setStatus("current")
_ZhoneCpeStaticRouteListIndexNext_Type = Integer32
_ZhoneCpeStaticRouteListIndexNext_Object = MibScalar
zhoneCpeStaticRouteListIndexNext = _ZhoneCpeStaticRouteListIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 24, 1),
    _ZhoneCpeStaticRouteListIndexNext_Type()
)
zhoneCpeStaticRouteListIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeStaticRouteListIndexNext.setStatus("current")
_ZhoneCpeStaticRouteListTable_Object = MibTable
zhoneCpeStaticRouteListTable = _ZhoneCpeStaticRouteListTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 24, 2)
)
if mibBuilder.loadTexts:
    zhoneCpeStaticRouteListTable.setStatus("current")
_ZhoneCpeStaticRouteListEntry_Object = MibTableRow
zhoneCpeStaticRouteListEntry = _ZhoneCpeStaticRouteListEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 24, 2, 1)
)
zhoneCpeStaticRouteListEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeStaticRouteListIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeStaticRouteListEntry.setStatus("current")


class _ZhoneCpeStaticRouteListIndex_Type(Unsigned32):
    """Custom type zhoneCpeStaticRouteListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeStaticRouteListIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeStaticRouteListIndex_Object = MibTableColumn
zhoneCpeStaticRouteListIndex = _ZhoneCpeStaticRouteListIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 24, 2, 1, 1),
    _ZhoneCpeStaticRouteListIndex_Type()
)
zhoneCpeStaticRouteListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeStaticRouteListIndex.setStatus("current")


class _ZhoneCpeStaticRouteListRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpeStaticRouteListRowStatus based on ZhoneRowStatus"""


_ZhoneCpeStaticRouteListRowStatus_Object = MibTableColumn
zhoneCpeStaticRouteListRowStatus = _ZhoneCpeStaticRouteListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 24, 2, 1, 2),
    _ZhoneCpeStaticRouteListRowStatus_Type()
)
zhoneCpeStaticRouteListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeStaticRouteListRowStatus.setStatus("current")
_ZhoneCpeStaticRouteListProfileName_Type = ZhoneAdminString
_ZhoneCpeStaticRouteListProfileName_Object = MibTableColumn
zhoneCpeStaticRouteListProfileName = _ZhoneCpeStaticRouteListProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 24, 2, 1, 3),
    _ZhoneCpeStaticRouteListProfileName_Type()
)
zhoneCpeStaticRouteListProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeStaticRouteListProfileName.setStatus("current")
_ZhoneCpeStaticRoute_ObjectIdentity = ObjectIdentity
zhoneCpeStaticRoute = _ZhoneCpeStaticRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 25)
)
if mibBuilder.loadTexts:
    zhoneCpeStaticRoute.setStatus("current")
_ZhoneCpeStaticRouteIndexTable_Object = MibTable
zhoneCpeStaticRouteIndexTable = _ZhoneCpeStaticRouteIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 25, 1)
)
if mibBuilder.loadTexts:
    zhoneCpeStaticRouteIndexTable.setStatus("current")
_ZhoneCpeStaticRouteIndexEntry_Object = MibTableRow
zhoneCpeStaticRouteIndexEntry = _ZhoneCpeStaticRouteIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 25, 1, 1)
)
zhoneCpeStaticRouteIndexEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeStaticRouteListIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeStaticRouteIndexEntry.setStatus("current")
_ZhoneCpeStaticRouteEntryIndexNext_Type = Unsigned32
_ZhoneCpeStaticRouteEntryIndexNext_Object = MibTableColumn
zhoneCpeStaticRouteEntryIndexNext = _ZhoneCpeStaticRouteEntryIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 25, 1, 1, 1),
    _ZhoneCpeStaticRouteEntryIndexNext_Type()
)
zhoneCpeStaticRouteEntryIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeStaticRouteEntryIndexNext.setStatus("current")
_ZhoneCpeStaticRouteTable_Object = MibTable
zhoneCpeStaticRouteTable = _ZhoneCpeStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 25, 2)
)
if mibBuilder.loadTexts:
    zhoneCpeStaticRouteTable.setStatus("current")
_ZhoneCpeStaticRouteEntry_Object = MibTableRow
zhoneCpeStaticRouteEntry = _ZhoneCpeStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 25, 2, 1)
)
zhoneCpeStaticRouteEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeStaticRouteListIndex"),
    (0, "Zhone-CPE-MIB", "zhoneCpeStaticRouteEntryIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeStaticRouteEntry.setStatus("current")


class _ZhoneCpeStaticRouteEntryIndex_Type(Unsigned32):
    """Custom type zhoneCpeStaticRouteEntryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeStaticRouteEntryIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeStaticRouteEntryIndex_Object = MibTableColumn
zhoneCpeStaticRouteEntryIndex = _ZhoneCpeStaticRouteEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 25, 2, 1, 1),
    _ZhoneCpeStaticRouteEntryIndex_Type()
)
zhoneCpeStaticRouteEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeStaticRouteEntryIndex.setStatus("current")


class _ZhoneCpeStaticRouteRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpeStaticRouteRowStatus based on ZhoneRowStatus"""


_ZhoneCpeStaticRouteRowStatus_Object = MibTableColumn
zhoneCpeStaticRouteRowStatus = _ZhoneCpeStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 25, 2, 1, 2),
    _ZhoneCpeStaticRouteRowStatus_Type()
)
zhoneCpeStaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeStaticRouteRowStatus.setStatus("current")


class _ZhoneCpeStaticRouteDestinationIp_Type(IpAddress):
    """Custom type zhoneCpeStaticRouteDestinationIp based on IpAddress"""
    defaultHexValue = "00000000"


_ZhoneCpeStaticRouteDestinationIp_Object = MibTableColumn
zhoneCpeStaticRouteDestinationIp = _ZhoneCpeStaticRouteDestinationIp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 25, 2, 1, 3),
    _ZhoneCpeStaticRouteDestinationIp_Type()
)
zhoneCpeStaticRouteDestinationIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeStaticRouteDestinationIp.setStatus("current")


class _ZhoneCpeStaticRouteNetmask_Type(IpAddress):
    """Custom type zhoneCpeStaticRouteNetmask based on IpAddress"""
    defaultHexValue = "ffffff00"


_ZhoneCpeStaticRouteNetmask_Object = MibTableColumn
zhoneCpeStaticRouteNetmask = _ZhoneCpeStaticRouteNetmask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 25, 2, 1, 4),
    _ZhoneCpeStaticRouteNetmask_Type()
)
zhoneCpeStaticRouteNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeStaticRouteNetmask.setStatus("current")


class _ZhoneCpeStaticRouteGateway_Type(IpAddress):
    """Custom type zhoneCpeStaticRouteGateway based on IpAddress"""
    defaultHexValue = "00000000"


_ZhoneCpeStaticRouteGateway_Object = MibTableColumn
zhoneCpeStaticRouteGateway = _ZhoneCpeStaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 25, 2, 1, 5),
    _ZhoneCpeStaticRouteGateway_Type()
)
zhoneCpeStaticRouteGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeStaticRouteGateway.setStatus("current")


class _ZhoneCpeStaticRouteMetric_Type(Integer32):
    """Custom type zhoneCpeStaticRouteMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeStaticRouteMetric_Type.__name__ = "Integer32"
_ZhoneCpeStaticRouteMetric_Object = MibTableColumn
zhoneCpeStaticRouteMetric = _ZhoneCpeStaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 25, 2, 1, 6),
    _ZhoneCpeStaticRouteMetric_Type()
)
zhoneCpeStaticRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeStaticRouteMetric.setStatus("current")
_ZhoneCpePortFwdList_ObjectIdentity = ObjectIdentity
zhoneCpePortFwdList = _ZhoneCpePortFwdList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 26)
)
if mibBuilder.loadTexts:
    zhoneCpePortFwdList.setStatus("current")
_ZhoneCpePortFwdListIndexNext_Type = Integer32
_ZhoneCpePortFwdListIndexNext_Object = MibScalar
zhoneCpePortFwdListIndexNext = _ZhoneCpePortFwdListIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 26, 1),
    _ZhoneCpePortFwdListIndexNext_Type()
)
zhoneCpePortFwdListIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpePortFwdListIndexNext.setStatus("current")
_ZhoneCpePortFwdListTable_Object = MibTable
zhoneCpePortFwdListTable = _ZhoneCpePortFwdListTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 26, 2)
)
if mibBuilder.loadTexts:
    zhoneCpePortFwdListTable.setStatus("current")
_ZhoneCpePortFwdListEntry_Object = MibTableRow
zhoneCpePortFwdListEntry = _ZhoneCpePortFwdListEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 26, 2, 1)
)
zhoneCpePortFwdListEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpePortFwdListIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpePortFwdListEntry.setStatus("current")


class _ZhoneCpePortFwdListIndex_Type(Unsigned32):
    """Custom type zhoneCpePortFwdListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpePortFwdListIndex_Type.__name__ = "Unsigned32"
_ZhoneCpePortFwdListIndex_Object = MibTableColumn
zhoneCpePortFwdListIndex = _ZhoneCpePortFwdListIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 26, 2, 1, 1),
    _ZhoneCpePortFwdListIndex_Type()
)
zhoneCpePortFwdListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpePortFwdListIndex.setStatus("current")


class _ZhoneCpePortFwdListRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpePortFwdListRowStatus based on ZhoneRowStatus"""


_ZhoneCpePortFwdListRowStatus_Object = MibTableColumn
zhoneCpePortFwdListRowStatus = _ZhoneCpePortFwdListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 26, 2, 1, 2),
    _ZhoneCpePortFwdListRowStatus_Type()
)
zhoneCpePortFwdListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePortFwdListRowStatus.setStatus("current")
_ZhoneCpePortFwdListProfileName_Type = ZhoneAdminString
_ZhoneCpePortFwdListProfileName_Object = MibTableColumn
zhoneCpePortFwdListProfileName = _ZhoneCpePortFwdListProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 26, 2, 1, 3),
    _ZhoneCpePortFwdListProfileName_Type()
)
zhoneCpePortFwdListProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePortFwdListProfileName.setStatus("current")
_ZhoneCpePortFwd_ObjectIdentity = ObjectIdentity
zhoneCpePortFwd = _ZhoneCpePortFwd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 27)
)
if mibBuilder.loadTexts:
    zhoneCpePortFwd.setStatus("current")
_ZhoneCpePortFwdIndexTable_Object = MibTable
zhoneCpePortFwdIndexTable = _ZhoneCpePortFwdIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 27, 1)
)
if mibBuilder.loadTexts:
    zhoneCpePortFwdIndexTable.setStatus("current")
_ZhoneCpePortFwdIndexEntry_Object = MibTableRow
zhoneCpePortFwdIndexEntry = _ZhoneCpePortFwdIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 27, 1, 1)
)
zhoneCpePortFwdIndexEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpePortFwdListIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpePortFwdIndexEntry.setStatus("current")
_ZhoneCpePortFwdEntryIndexNext_Type = Unsigned32
_ZhoneCpePortFwdEntryIndexNext_Object = MibTableColumn
zhoneCpePortFwdEntryIndexNext = _ZhoneCpePortFwdEntryIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 27, 1, 1, 1),
    _ZhoneCpePortFwdEntryIndexNext_Type()
)
zhoneCpePortFwdEntryIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpePortFwdEntryIndexNext.setStatus("current")
_ZhoneCpePortFwdTable_Object = MibTable
zhoneCpePortFwdTable = _ZhoneCpePortFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 27, 2)
)
if mibBuilder.loadTexts:
    zhoneCpePortFwdTable.setStatus("current")
_ZhoneCpePortFwdEntry_Object = MibTableRow
zhoneCpePortFwdEntry = _ZhoneCpePortFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 27, 2, 1)
)
zhoneCpePortFwdEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpePortFwdListIndex"),
    (0, "Zhone-CPE-MIB", "zhoneCpePortFwdEntryIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpePortFwdEntry.setStatus("current")


class _ZhoneCpePortFwdEntryIndex_Type(Unsigned32):
    """Custom type zhoneCpePortFwdEntryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpePortFwdEntryIndex_Type.__name__ = "Unsigned32"
_ZhoneCpePortFwdEntryIndex_Object = MibTableColumn
zhoneCpePortFwdEntryIndex = _ZhoneCpePortFwdEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 27, 2, 1, 1),
    _ZhoneCpePortFwdEntryIndex_Type()
)
zhoneCpePortFwdEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpePortFwdEntryIndex.setStatus("current")


class _ZhoneCpePortFwdRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpePortFwdRowStatus based on ZhoneRowStatus"""


_ZhoneCpePortFwdRowStatus_Object = MibTableColumn
zhoneCpePortFwdRowStatus = _ZhoneCpePortFwdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 27, 2, 1, 2),
    _ZhoneCpePortFwdRowStatus_Type()
)
zhoneCpePortFwdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePortFwdRowStatus.setStatus("current")


class _ZhoneCpePortFwdType_Type(Integer32):
    """Custom type zhoneCpePortFwdType based on Integer32"""
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
        *(("dmz", 1),
          ("portrange", 2),
          ("portremap", 3))
    )


_ZhoneCpePortFwdType_Type.__name__ = "Integer32"
_ZhoneCpePortFwdType_Object = MibTableColumn
zhoneCpePortFwdType = _ZhoneCpePortFwdType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 27, 2, 1, 3),
    _ZhoneCpePortFwdType_Type()
)
zhoneCpePortFwdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePortFwdType.setStatus("current")


class _ZhoneCpePortFwdPortStart_Type(Unsigned32):
    """Custom type zhoneCpePortFwdPortStart based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneCpePortFwdPortStart_Type.__name__ = "Unsigned32"
_ZhoneCpePortFwdPortStart_Object = MibTableColumn
zhoneCpePortFwdPortStart = _ZhoneCpePortFwdPortStart_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 27, 2, 1, 4),
    _ZhoneCpePortFwdPortStart_Type()
)
zhoneCpePortFwdPortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePortFwdPortStart.setStatus("current")


class _ZhoneCpePortFwdPortEnd_Type(Unsigned32):
    """Custom type zhoneCpePortFwdPortEnd based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneCpePortFwdPortEnd_Type.__name__ = "Unsigned32"
_ZhoneCpePortFwdPortEnd_Object = MibTableColumn
zhoneCpePortFwdPortEnd = _ZhoneCpePortFwdPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 27, 2, 1, 5),
    _ZhoneCpePortFwdPortEnd_Type()
)
zhoneCpePortFwdPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePortFwdPortEnd.setStatus("current")


class _ZhoneCpePortFwdProtocol_Type(Integer32):
    """Custom type zhoneCpePortFwdProtocol based on Integer32"""
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
        *(("icmp", 5),
          ("icmpv4", 6),
          ("none", 1),
          ("tcp", 2),
          ("tcpudp", 4),
          ("udp", 3))
    )


_ZhoneCpePortFwdProtocol_Type.__name__ = "Integer32"
_ZhoneCpePortFwdProtocol_Object = MibTableColumn
zhoneCpePortFwdProtocol = _ZhoneCpePortFwdProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 27, 2, 1, 6),
    _ZhoneCpePortFwdProtocol_Type()
)
zhoneCpePortFwdProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePortFwdProtocol.setStatus("current")


class _ZhoneCpePortFwdPrivatePort_Type(Unsigned32):
    """Custom type zhoneCpePortFwdPrivatePort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneCpePortFwdPrivatePort_Type.__name__ = "Unsigned32"
_ZhoneCpePortFwdPrivatePort_Object = MibTableColumn
zhoneCpePortFwdPrivatePort = _ZhoneCpePortFwdPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 27, 2, 1, 7),
    _ZhoneCpePortFwdPrivatePort_Type()
)
zhoneCpePortFwdPrivatePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePortFwdPrivatePort.setStatus("current")


class _ZhoneCpePortFwdPrivateIp_Type(IpAddress):
    """Custom type zhoneCpePortFwdPrivateIp based on IpAddress"""
    defaultHexValue = "00000000"


_ZhoneCpePortFwdPrivateIp_Object = MibTableColumn
zhoneCpePortFwdPrivateIp = _ZhoneCpePortFwdPrivateIp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 27, 2, 1, 8),
    _ZhoneCpePortFwdPrivateIp_Type()
)
zhoneCpePortFwdPrivateIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpePortFwdPrivateIp.setStatus("current")
_ZhoneCpeServiceApplication_ObjectIdentity = ObjectIdentity
zhoneCpeServiceApplication = _ZhoneCpeServiceApplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 28)
)
if mibBuilder.loadTexts:
    zhoneCpeServiceApplication.setStatus("current")
_ZhoneCpeServiceApplicationTable_Object = MibTable
zhoneCpeServiceApplicationTable = _ZhoneCpeServiceApplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 28, 1)
)
if mibBuilder.loadTexts:
    zhoneCpeServiceApplicationTable.setStatus("current")
_ZhoneCpeServiceApplicationEntry_Object = MibTableRow
zhoneCpeServiceApplicationEntry = _ZhoneCpeServiceApplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 28, 1, 1)
)
zhoneCpeServiceApplicationEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeServiceApplicationTemplateType"),
    (0, "Zhone-CPE-MIB", "zhoneCpeServiceApplicationTemplateId"),
    (0, "Zhone-CPE-MIB", "zhoneCpeIfIndex"),
    (0, "Zhone-CPE-MIB", "zhoneCpeServiceApplicationVirtualConnection"),
    (0, "Zhone-CPE-MIB", "zhoneCpeServiceApplicationTpType"),
    (0, "Zhone-CPE-MIB", "zhoneCpeServiceApplicationTpIndex"),
    (0, "Zhone-CPE-MIB", "zhoneCpeServiceApplicationVlan"),
    (0, "Zhone-CPE-MIB", "zhoneCpeServiceApplicationSlan"),
)
if mibBuilder.loadTexts:
    zhoneCpeServiceApplicationEntry.setStatus("current")
_ZhoneCpeServiceApplicationTemplateType_Type = ZhoneCpeTemplateType
_ZhoneCpeServiceApplicationTemplateType_Object = MibTableColumn
zhoneCpeServiceApplicationTemplateType = _ZhoneCpeServiceApplicationTemplateType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 28, 1, 1, 1),
    _ZhoneCpeServiceApplicationTemplateType_Type()
)
zhoneCpeServiceApplicationTemplateType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneCpeServiceApplicationTemplateType.setStatus("current")


class _ZhoneCpeServiceApplicationTemplateId_Type(Unsigned32):
    """Custom type zhoneCpeServiceApplicationTemplateId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeServiceApplicationTemplateId_Type.__name__ = "Unsigned32"
_ZhoneCpeServiceApplicationTemplateId_Object = MibTableColumn
zhoneCpeServiceApplicationTemplateId = _ZhoneCpeServiceApplicationTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 28, 1, 1, 2),
    _ZhoneCpeServiceApplicationTemplateId_Type()
)
zhoneCpeServiceApplicationTemplateId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneCpeServiceApplicationTemplateId.setStatus("current")


class _ZhoneCpeServiceApplicationVirtualConnection_Type(Unsigned32):
    """Custom type zhoneCpeServiceApplicationVirtualConnection based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeServiceApplicationVirtualConnection_Type.__name__ = "Unsigned32"
_ZhoneCpeServiceApplicationVirtualConnection_Object = MibTableColumn
zhoneCpeServiceApplicationVirtualConnection = _ZhoneCpeServiceApplicationVirtualConnection_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 28, 1, 1, 3),
    _ZhoneCpeServiceApplicationVirtualConnection_Type()
)
zhoneCpeServiceApplicationVirtualConnection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneCpeServiceApplicationVirtualConnection.setStatus("current")
_ZhoneCpeServiceApplicationTpType_Type = TpType
_ZhoneCpeServiceApplicationTpType_Object = MibTableColumn
zhoneCpeServiceApplicationTpType = _ZhoneCpeServiceApplicationTpType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 28, 1, 1, 4),
    _ZhoneCpeServiceApplicationTpType_Type()
)
zhoneCpeServiceApplicationTpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneCpeServiceApplicationTpType.setStatus("current")


class _ZhoneCpeServiceApplicationTpIndex_Type(Unsigned32):
    """Custom type zhoneCpeServiceApplicationTpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeServiceApplicationTpIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeServiceApplicationTpIndex_Object = MibTableColumn
zhoneCpeServiceApplicationTpIndex = _ZhoneCpeServiceApplicationTpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 28, 1, 1, 5),
    _ZhoneCpeServiceApplicationTpIndex_Type()
)
zhoneCpeServiceApplicationTpIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneCpeServiceApplicationTpIndex.setStatus("current")


class _ZhoneCpeServiceApplicationRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpeServiceApplicationRowStatus based on ZhoneRowStatus"""


_ZhoneCpeServiceApplicationRowStatus_Object = MibTableColumn
zhoneCpeServiceApplicationRowStatus = _ZhoneCpeServiceApplicationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 28, 1, 1, 6),
    _ZhoneCpeServiceApplicationRowStatus_Type()
)
zhoneCpeServiceApplicationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeServiceApplicationRowStatus.setStatus("current")
_ZhoneCpeServiceApplicationVlan_Type = Unsigned32
_ZhoneCpeServiceApplicationVlan_Object = MibTableColumn
zhoneCpeServiceApplicationVlan = _ZhoneCpeServiceApplicationVlan_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 28, 1, 1, 7),
    _ZhoneCpeServiceApplicationVlan_Type()
)
zhoneCpeServiceApplicationVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneCpeServiceApplicationVlan.setStatus("current")
_ZhoneCpeServiceApplicationSlan_Type = Unsigned32
_ZhoneCpeServiceApplicationSlan_Object = MibTableColumn
zhoneCpeServiceApplicationSlan = _ZhoneCpeServiceApplicationSlan_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 28, 1, 1, 8),
    _ZhoneCpeServiceApplicationSlan_Type()
)
zhoneCpeServiceApplicationSlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneCpeServiceApplicationSlan.setStatus("current")
_ZhoneCpeDnsHostList_ObjectIdentity = ObjectIdentity
zhoneCpeDnsHostList = _ZhoneCpeDnsHostList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 29)
)
if mibBuilder.loadTexts:
    zhoneCpeDnsHostList.setStatus("current")
_ZhoneCpeDnsHostListIndexNext_Type = Integer32
_ZhoneCpeDnsHostListIndexNext_Object = MibScalar
zhoneCpeDnsHostListIndexNext = _ZhoneCpeDnsHostListIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 29, 1),
    _ZhoneCpeDnsHostListIndexNext_Type()
)
zhoneCpeDnsHostListIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeDnsHostListIndexNext.setStatus("current")
_ZhoneCpeDnsHostListTable_Object = MibTable
zhoneCpeDnsHostListTable = _ZhoneCpeDnsHostListTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 29, 2)
)
if mibBuilder.loadTexts:
    zhoneCpeDnsHostListTable.setStatus("current")
_ZhoneCpeDnsHostListEntry_Object = MibTableRow
zhoneCpeDnsHostListEntry = _ZhoneCpeDnsHostListEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 29, 2, 1)
)
zhoneCpeDnsHostListEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeDnsHostListIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeDnsHostListEntry.setStatus("current")
_ZhoneCpeDnsHostListIndex_Type = Unsigned32
_ZhoneCpeDnsHostListIndex_Object = MibTableColumn
zhoneCpeDnsHostListIndex = _ZhoneCpeDnsHostListIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 29, 2, 1, 2),
    _ZhoneCpeDnsHostListIndex_Type()
)
zhoneCpeDnsHostListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeDnsHostListIndex.setStatus("current")


class _ZhoneCpeDnsHostListRowStatus_Type(RowStatus):
    """Custom type zhoneCpeDnsHostListRowStatus based on RowStatus"""


_ZhoneCpeDnsHostListRowStatus_Object = MibTableColumn
zhoneCpeDnsHostListRowStatus = _ZhoneCpeDnsHostListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 29, 2, 1, 3),
    _ZhoneCpeDnsHostListRowStatus_Type()
)
zhoneCpeDnsHostListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeDnsHostListRowStatus.setStatus("current")
_ZhoneCpeDnsHostListProfileName_Type = ZhoneAdminString
_ZhoneCpeDnsHostListProfileName_Object = MibTableColumn
zhoneCpeDnsHostListProfileName = _ZhoneCpeDnsHostListProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 29, 2, 1, 4),
    _ZhoneCpeDnsHostListProfileName_Type()
)
zhoneCpeDnsHostListProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeDnsHostListProfileName.setStatus("current")
_ZhoneCpeDnsHost_ObjectIdentity = ObjectIdentity
zhoneCpeDnsHost = _ZhoneCpeDnsHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 30)
)
if mibBuilder.loadTexts:
    zhoneCpeDnsHost.setStatus("current")
_ZhoneCpeDnsHostIndexTable_Object = MibTable
zhoneCpeDnsHostIndexTable = _ZhoneCpeDnsHostIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 30, 1)
)
if mibBuilder.loadTexts:
    zhoneCpeDnsHostIndexTable.setStatus("current")
_ZhoneCpeDnsHostIndexEntry_Object = MibTableRow
zhoneCpeDnsHostIndexEntry = _ZhoneCpeDnsHostIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 30, 1, 1)
)
zhoneCpeDnsHostIndexEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeDnsHostListIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeDnsHostIndexEntry.setStatus("current")
_ZhoneCpeDnsHostIndexEntryIndexNext_Type = Integer32
_ZhoneCpeDnsHostIndexEntryIndexNext_Object = MibTableColumn
zhoneCpeDnsHostIndexEntryIndexNext = _ZhoneCpeDnsHostIndexEntryIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 30, 1, 1, 1),
    _ZhoneCpeDnsHostIndexEntryIndexNext_Type()
)
zhoneCpeDnsHostIndexEntryIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeDnsHostIndexEntryIndexNext.setStatus("current")
_ZhoneCpeDnsHostTable_Object = MibTable
zhoneCpeDnsHostTable = _ZhoneCpeDnsHostTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 30, 2)
)
if mibBuilder.loadTexts:
    zhoneCpeDnsHostTable.setStatus("current")
_ZhoneCpeDnsHostEntry_Object = MibTableRow
zhoneCpeDnsHostEntry = _ZhoneCpeDnsHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 30, 2, 1)
)
zhoneCpeDnsHostEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeDnsHostListIndex"),
    (0, "Zhone-CPE-MIB", "zhoneCpeDnsHostEntryIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeDnsHostEntry.setStatus("current")
_ZhoneCpeDnsHostEntryIndex_Type = Unsigned32
_ZhoneCpeDnsHostEntryIndex_Object = MibTableColumn
zhoneCpeDnsHostEntryIndex = _ZhoneCpeDnsHostEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 30, 2, 1, 1),
    _ZhoneCpeDnsHostEntryIndex_Type()
)
zhoneCpeDnsHostEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeDnsHostEntryIndex.setStatus("current")


class _ZhoneCpeDnsHostRowStatus_Type(RowStatus):
    """Custom type zhoneCpeDnsHostRowStatus based on RowStatus"""


_ZhoneCpeDnsHostRowStatus_Object = MibTableColumn
zhoneCpeDnsHostRowStatus = _ZhoneCpeDnsHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 30, 2, 1, 2),
    _ZhoneCpeDnsHostRowStatus_Type()
)
zhoneCpeDnsHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeDnsHostRowStatus.setStatus("current")


class _ZhoneCpeDnsHostDomainName_Type(OctetString):
    """Custom type zhoneCpeDnsHostDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ZhoneCpeDnsHostDomainName_Type.__name__ = "OctetString"
_ZhoneCpeDnsHostDomainName_Object = MibTableColumn
zhoneCpeDnsHostDomainName = _ZhoneCpeDnsHostDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 30, 2, 1, 3),
    _ZhoneCpeDnsHostDomainName_Type()
)
zhoneCpeDnsHostDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeDnsHostDomainName.setStatus("current")
_ZhoneCpeDnsHostIpAddress_Type = IpAddress
_ZhoneCpeDnsHostIpAddress_Object = MibTableColumn
zhoneCpeDnsHostIpAddress = _ZhoneCpeDnsHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 30, 2, 1, 4),
    _ZhoneCpeDnsHostIpAddress_Type()
)
zhoneCpeDnsHostIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeDnsHostIpAddress.setStatus("current")
_ZhoneCpeWlanAdvanced_ObjectIdentity = ObjectIdentity
zhoneCpeWlanAdvanced = _ZhoneCpeWlanAdvanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31)
)
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvanced.setStatus("current")
_ZhoneCpeWlanAdvIndexNext_Type = Integer32
_ZhoneCpeWlanAdvIndexNext_Object = MibScalar
zhoneCpeWlanAdvIndexNext = _ZhoneCpeWlanAdvIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 1),
    _ZhoneCpeWlanAdvIndexNext_Type()
)
zhoneCpeWlanAdvIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvIndexNext.setStatus("current")
_ZhoneCpeWlanAdvancedTable_Object = MibTable
zhoneCpeWlanAdvancedTable = _ZhoneCpeWlanAdvancedTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2)
)
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvancedTable.setStatus("current")
_ZhoneCpeWlanAdvancedEntry_Object = MibTableRow
zhoneCpeWlanAdvancedEntry = _ZhoneCpeWlanAdvancedEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1)
)
zhoneCpeWlanAdvancedEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeWlanAdvIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvancedEntry.setStatus("current")


class _ZhoneCpeWlanAdvIndex_Type(Unsigned32):
    """Custom type zhoneCpeWlanAdvIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeWlanAdvIndex_Type.__name__ = "Unsigned32"
_ZhoneCpeWlanAdvIndex_Object = MibTableColumn
zhoneCpeWlanAdvIndex = _ZhoneCpeWlanAdvIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 1),
    _ZhoneCpeWlanAdvIndex_Type()
)
zhoneCpeWlanAdvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvIndex.setStatus("current")


class _ZhoneCpeWlanAdvRowStatus_Type(ZhoneRowStatus):
    """Custom type zhoneCpeWlanAdvRowStatus based on ZhoneRowStatus"""


_ZhoneCpeWlanAdvRowStatus_Object = MibTableColumn
zhoneCpeWlanAdvRowStatus = _ZhoneCpeWlanAdvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 2),
    _ZhoneCpeWlanAdvRowStatus_Type()
)
zhoneCpeWlanAdvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvRowStatus.setStatus("current")
_ZhoneCpeWlanAdvProfileName_Type = ZhoneAdminString
_ZhoneCpeWlanAdvProfileName_Object = MibTableColumn
zhoneCpeWlanAdvProfileName = _ZhoneCpeWlanAdvProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 3),
    _ZhoneCpeWlanAdvProfileName_Type()
)
zhoneCpeWlanAdvProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvProfileName.setStatus("current")


class _ZhoneCpeWlanAdvChannel_Type(Integer32):
    """Custom type zhoneCpeWlanAdvChannel based on Integer32"""
    defaultValue = 1

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
        *(("auto", 1),
          ("c1", 2),
          ("c10", 11),
          ("c11", 12),
          ("c12", 13),
          ("c13", 14),
          ("c2", 3),
          ("c3", 4),
          ("c4", 5),
          ("c5", 6),
          ("c6", 7),
          ("c7", 8),
          ("c8", 9),
          ("c9", 10))
    )


_ZhoneCpeWlanAdvChannel_Type.__name__ = "Integer32"
_ZhoneCpeWlanAdvChannel_Object = MibTableColumn
zhoneCpeWlanAdvChannel = _ZhoneCpeWlanAdvChannel_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 4),
    _ZhoneCpeWlanAdvChannel_Type()
)
zhoneCpeWlanAdvChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvChannel.setStatus("current")


class _ZhoneCpeWlanAdvAutoChanTimer_Type(Unsigned32):
    """Custom type zhoneCpeWlanAdvAutoChanTimer based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneCpeWlanAdvAutoChanTimer_Type.__name__ = "Unsigned32"
_ZhoneCpeWlanAdvAutoChanTimer_Object = MibTableColumn
zhoneCpeWlanAdvAutoChanTimer = _ZhoneCpeWlanAdvAutoChanTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 5),
    _ZhoneCpeWlanAdvAutoChanTimer_Type()
)
zhoneCpeWlanAdvAutoChanTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvAutoChanTimer.setStatus("current")


class _ZhoneCpeWlanAdvDot11nMode_Type(Integer32):
    """Custom type zhoneCpeWlanAdvDot11nMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("disabled", 2))
    )


_ZhoneCpeWlanAdvDot11nMode_Type.__name__ = "Integer32"
_ZhoneCpeWlanAdvDot11nMode_Object = MibTableColumn
zhoneCpeWlanAdvDot11nMode = _ZhoneCpeWlanAdvDot11nMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 6),
    _ZhoneCpeWlanAdvDot11nMode_Type()
)
zhoneCpeWlanAdvDot11nMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvDot11nMode.setStatus("current")


class _ZhoneCpeWlanAdvDot11nRate_Type(Integer32):
    """Custom type zhoneCpeWlanAdvDot11nRate based on Integer32"""
    defaultValue = 1

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
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("rate104m", 12),
          ("rate117m", 13),
          ("rate130m", 14),
          ("rate13m", 4),
          ("rate19dot5m", 5),
          ("rate26m", 6),
          ("rate39m", 7),
          ("rate58dot5m", 9),
          ("rate65m", 10),
          ("rate6dot5m", 3),
          ("rate78m", 11),
          ("use54g", 2))
    )


_ZhoneCpeWlanAdvDot11nRate_Type.__name__ = "Integer32"
_ZhoneCpeWlanAdvDot11nRate_Object = MibTableColumn
zhoneCpeWlanAdvDot11nRate = _ZhoneCpeWlanAdvDot11nRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 7),
    _ZhoneCpeWlanAdvDot11nRate_Type()
)
zhoneCpeWlanAdvDot11nRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvDot11nRate.setStatus("current")


class _ZhoneCpeWlanAdvDot1nProtection_Type(Integer32):
    """Custom type zhoneCpeWlanAdvDot1nProtection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("disabled", 2))
    )


_ZhoneCpeWlanAdvDot1nProtection_Type.__name__ = "Integer32"
_ZhoneCpeWlanAdvDot1nProtection_Object = MibTableColumn
zhoneCpeWlanAdvDot1nProtection = _ZhoneCpeWlanAdvDot1nProtection_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 8),
    _ZhoneCpeWlanAdvDot1nProtection_Type()
)
zhoneCpeWlanAdvDot1nProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvDot1nProtection.setStatus("current")


class _ZhoneCpeWlanAdvDot1nClientOnly_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeWlanAdvDot1nClientOnly based on ZhoneEnabledFlag"""


_ZhoneCpeWlanAdvDot1nClientOnly_Object = MibTableColumn
zhoneCpeWlanAdvDot1nClientOnly = _ZhoneCpeWlanAdvDot1nClientOnly_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 9),
    _ZhoneCpeWlanAdvDot1nClientOnly_Type()
)
zhoneCpeWlanAdvDot1nClientOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvDot1nClientOnly.setStatus("current")


class _ZhoneCpeWlanAdvRate54G_Type(Integer32):
    """Custom type zhoneCpeWlanAdvRate54G based on Integer32"""
    defaultValue = 1

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
        *(("auto", 1),
          ("rate11m", 7),
          ("rate12m", 8),
          ("rate18m", 9),
          ("rate1m", 2),
          ("rate24m", 10),
          ("rate2m", 3),
          ("rate36m", 11),
          ("rate48m", 12),
          ("rate54m", 13),
          ("rate5dot5m", 4),
          ("rate6m", 5),
          ("rate9m", 6))
    )


_ZhoneCpeWlanAdvRate54G_Type.__name__ = "Integer32"
_ZhoneCpeWlanAdvRate54G_Object = MibTableColumn
zhoneCpeWlanAdvRate54G = _ZhoneCpeWlanAdvRate54G_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 10),
    _ZhoneCpeWlanAdvRate54G_Type()
)
zhoneCpeWlanAdvRate54G.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvRate54G.setStatus("current")


class _ZhoneCpeWlanAdvMcastRate_Type(Integer32):
    """Custom type zhoneCpeWlanAdvMcastRate based on Integer32"""
    defaultValue = 1

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
        *(("auto", 1),
          ("rate11m", 7),
          ("rate12m", 8),
          ("rate18m", 9),
          ("rate1m", 2),
          ("rate24m", 10),
          ("rate2m", 3),
          ("rate36m", 11),
          ("rate48m", 12),
          ("rate54m", 13),
          ("rate5dot5m", 4),
          ("rate6m", 5),
          ("rate9m", 6))
    )


_ZhoneCpeWlanAdvMcastRate_Type.__name__ = "Integer32"
_ZhoneCpeWlanAdvMcastRate_Object = MibTableColumn
zhoneCpeWlanAdvMcastRate = _ZhoneCpeWlanAdvMcastRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 11),
    _ZhoneCpeWlanAdvMcastRate_Type()
)
zhoneCpeWlanAdvMcastRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvMcastRate.setStatus("current")


class _ZhoneCpeWlanAdvBasicRate_Type(Integer32):
    """Custom type zhoneCpeWlanAdvBasicRate based on Integer32"""
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
        *(("all", 2),
          ("default", 1),
          ("rate1n2", 3),
          ("stdrates", 4))
    )


_ZhoneCpeWlanAdvBasicRate_Type.__name__ = "Integer32"
_ZhoneCpeWlanAdvBasicRate_Object = MibTableColumn
zhoneCpeWlanAdvBasicRate = _ZhoneCpeWlanAdvBasicRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 12),
    _ZhoneCpeWlanAdvBasicRate_Type()
)
zhoneCpeWlanAdvBasicRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvBasicRate.setStatus("current")


class _ZhoneCpeWlanAdvFragmentationThreshold_Type(Unsigned32):
    """Custom type zhoneCpeWlanAdvFragmentationThreshold based on Unsigned32"""
    defaultValue = 2346

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_ZhoneCpeWlanAdvFragmentationThreshold_Type.__name__ = "Unsigned32"
_ZhoneCpeWlanAdvFragmentationThreshold_Object = MibTableColumn
zhoneCpeWlanAdvFragmentationThreshold = _ZhoneCpeWlanAdvFragmentationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 13),
    _ZhoneCpeWlanAdvFragmentationThreshold_Type()
)
zhoneCpeWlanAdvFragmentationThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvFragmentationThreshold.setStatus("current")


class _ZhoneCpeWlanAdvRtsThreshold_Type(Unsigned32):
    """Custom type zhoneCpeWlanAdvRtsThreshold based on Unsigned32"""
    defaultValue = 2347

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2347),
    )


_ZhoneCpeWlanAdvRtsThreshold_Type.__name__ = "Unsigned32"
_ZhoneCpeWlanAdvRtsThreshold_Object = MibTableColumn
zhoneCpeWlanAdvRtsThreshold = _ZhoneCpeWlanAdvRtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 14),
    _ZhoneCpeWlanAdvRtsThreshold_Type()
)
zhoneCpeWlanAdvRtsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvRtsThreshold.setStatus("current")


class _ZhoneCpeWlanAdvDtimInterval_Type(Unsigned32):
    """Custom type zhoneCpeWlanAdvDtimInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZhoneCpeWlanAdvDtimInterval_Type.__name__ = "Unsigned32"
_ZhoneCpeWlanAdvDtimInterval_Object = MibTableColumn
zhoneCpeWlanAdvDtimInterval = _ZhoneCpeWlanAdvDtimInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 15),
    _ZhoneCpeWlanAdvDtimInterval_Type()
)
zhoneCpeWlanAdvDtimInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvDtimInterval.setStatus("current")


class _ZhoneCpeWlanAdvBeaconInterval_Type(Unsigned32):
    """Custom type zhoneCpeWlanAdvBeaconInterval based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZhoneCpeWlanAdvBeaconInterval_Type.__name__ = "Unsigned32"
_ZhoneCpeWlanAdvBeaconInterval_Object = MibTableColumn
zhoneCpeWlanAdvBeaconInterval = _ZhoneCpeWlanAdvBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 16),
    _ZhoneCpeWlanAdvBeaconInterval_Type()
)
zhoneCpeWlanAdvBeaconInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvBeaconInterval.setStatus("current")


class _ZhoneCpeWlanAdvGlobalMaxClients_Type(Unsigned32):
    """Custom type zhoneCpeWlanAdvGlobalMaxClients based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_ZhoneCpeWlanAdvGlobalMaxClients_Type.__name__ = "Unsigned32"
_ZhoneCpeWlanAdvGlobalMaxClients_Object = MibTableColumn
zhoneCpeWlanAdvGlobalMaxClients = _ZhoneCpeWlanAdvGlobalMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 17),
    _ZhoneCpeWlanAdvGlobalMaxClients_Type()
)
zhoneCpeWlanAdvGlobalMaxClients.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvGlobalMaxClients.setStatus("current")


class _ZhoneCpeWlanAdvXpressTechnology_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeWlanAdvXpressTechnology based on ZhoneEnabledFlag"""


_ZhoneCpeWlanAdvXpressTechnology_Object = MibTableColumn
zhoneCpeWlanAdvXpressTechnology = _ZhoneCpeWlanAdvXpressTechnology_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 18),
    _ZhoneCpeWlanAdvXpressTechnology_Type()
)
zhoneCpeWlanAdvXpressTechnology.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvXpressTechnology.setStatus("current")


class _ZhoneCpeWlanAdvTxPower_Type(Unsigned32):
    """Custom type zhoneCpeWlanAdvTxPower based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ZhoneCpeWlanAdvTxPower_Type.__name__ = "Unsigned32"
_ZhoneCpeWlanAdvTxPower_Object = MibTableColumn
zhoneCpeWlanAdvTxPower = _ZhoneCpeWlanAdvTxPower_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 19),
    _ZhoneCpeWlanAdvTxPower_Type()
)
zhoneCpeWlanAdvTxPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvTxPower.setStatus("current")


class _ZhoneCpeWlanAdvWmm_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeWlanAdvWmm based on ZhoneEnabledFlag"""


_ZhoneCpeWlanAdvWmm_Object = MibTableColumn
zhoneCpeWlanAdvWmm = _ZhoneCpeWlanAdvWmm_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 20),
    _ZhoneCpeWlanAdvWmm_Type()
)
zhoneCpeWlanAdvWmm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvWmm.setStatus("current")


class _ZhoneCpeWlanAdvWmmNoAck_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeWlanAdvWmmNoAck based on ZhoneEnabledFlag"""


_ZhoneCpeWlanAdvWmmNoAck_Object = MibTableColumn
zhoneCpeWlanAdvWmmNoAck = _ZhoneCpeWlanAdvWmmNoAck_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 21),
    _ZhoneCpeWlanAdvWmmNoAck_Type()
)
zhoneCpeWlanAdvWmmNoAck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvWmmNoAck.setStatus("current")


class _ZhoneCpeWlanAdvWmmApsd_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeWlanAdvWmmApsd based on ZhoneEnabledFlag"""


_ZhoneCpeWlanAdvWmmApsd_Object = MibTableColumn
zhoneCpeWlanAdvWmmApsd = _ZhoneCpeWlanAdvWmmApsd_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 22),
    _ZhoneCpeWlanAdvWmmApsd_Type()
)
zhoneCpeWlanAdvWmmApsd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvWmmApsd.setStatus("current")


class _ZhoneCpeWlanAdvApMode_Type(Integer32):
    """Custom type zhoneCpeWlanAdvApMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accesspoint", 1),
          ("wirelessbridge", 2))
    )


_ZhoneCpeWlanAdvApMode_Type.__name__ = "Integer32"
_ZhoneCpeWlanAdvApMode_Object = MibTableColumn
zhoneCpeWlanAdvApMode = _ZhoneCpeWlanAdvApMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 23),
    _ZhoneCpeWlanAdvApMode_Type()
)
zhoneCpeWlanAdvApMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvApMode.setStatus("current")


class _ZhoneCpeWlanAdvBridgeRestrict_Type(Integer32):
    """Custom type zhoneCpeWlanAdvBridgeRestrict based on Integer32"""
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
        *(("disabled", 3),
          ("enabled", 1),
          ("enabledscan", 2))
    )


_ZhoneCpeWlanAdvBridgeRestrict_Type.__name__ = "Integer32"
_ZhoneCpeWlanAdvBridgeRestrict_Object = MibTableColumn
zhoneCpeWlanAdvBridgeRestrict = _ZhoneCpeWlanAdvBridgeRestrict_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 24),
    _ZhoneCpeWlanAdvBridgeRestrict_Type()
)
zhoneCpeWlanAdvBridgeRestrict.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvBridgeRestrict.setStatus("current")


class _ZhoneCpeWlanAdvWps_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeWlanAdvWps based on ZhoneEnabledFlag"""


_ZhoneCpeWlanAdvWps_Object = MibTableColumn
zhoneCpeWlanAdvWps = _ZhoneCpeWlanAdvWps_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 25),
    _ZhoneCpeWlanAdvWps_Type()
)
zhoneCpeWlanAdvWps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvWps.setStatus("current")


class _ZhoneCpeWlanAdvWpsAddClientMethod_Type(Integer32):
    """Custom type zhoneCpeWlanAdvWpsAddClientMethod based on Integer32"""
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
        *(("appin", 3),
          ("pushbutton", 1),
          ("stapin", 2))
    )


_ZhoneCpeWlanAdvWpsAddClientMethod_Type.__name__ = "Integer32"
_ZhoneCpeWlanAdvWpsAddClientMethod_Object = MibTableColumn
zhoneCpeWlanAdvWpsAddClientMethod = _ZhoneCpeWlanAdvWpsAddClientMethod_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 26),
    _ZhoneCpeWlanAdvWpsAddClientMethod_Type()
)
zhoneCpeWlanAdvWpsAddClientMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvWpsAddClientMethod.setStatus("current")


class _ZhoneCpeWlanAdvWpsApMode_Type(Integer32):
    """Custom type zhoneCpeWlanAdvWpsApMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("unconfigured", 2))
    )


_ZhoneCpeWlanAdvWpsApMode_Type.__name__ = "Integer32"
_ZhoneCpeWlanAdvWpsApMode_Object = MibTableColumn
zhoneCpeWlanAdvWpsApMode = _ZhoneCpeWlanAdvWpsApMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 31, 2, 1, 27),
    _ZhoneCpeWlanAdvWpsApMode_Type()
)
zhoneCpeWlanAdvWpsApMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvWpsApMode.setStatus("current")
_ZhoneCpeCondDhcpSrvList_ObjectIdentity = ObjectIdentity
zhoneCpeCondDhcpSrvList = _ZhoneCpeCondDhcpSrvList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 32)
)
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvList.setStatus("current")
_ZhoneCpeCondiDhcpSrvListIndexNext_Type = Integer32
_ZhoneCpeCondiDhcpSrvListIndexNext_Object = MibScalar
zhoneCpeCondiDhcpSrvListIndexNext = _ZhoneCpeCondiDhcpSrvListIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 32, 1),
    _ZhoneCpeCondiDhcpSrvListIndexNext_Type()
)
zhoneCpeCondiDhcpSrvListIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeCondiDhcpSrvListIndexNext.setStatus("current")
_ZhoneCpeCondDhcpSrvListTable_Object = MibTable
zhoneCpeCondDhcpSrvListTable = _ZhoneCpeCondDhcpSrvListTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 32, 2)
)
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvListTable.setStatus("current")
_ZhoneCpeCondDhcpSrvListEntry_Object = MibTableRow
zhoneCpeCondDhcpSrvListEntry = _ZhoneCpeCondDhcpSrvListEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 32, 2, 1)
)
zhoneCpeCondDhcpSrvListEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeCondDhcpSrvListIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvListEntry.setStatus("current")
_ZhoneCpeCondDhcpSrvListIndex_Type = Unsigned32
_ZhoneCpeCondDhcpSrvListIndex_Object = MibTableColumn
zhoneCpeCondDhcpSrvListIndex = _ZhoneCpeCondDhcpSrvListIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 32, 2, 1, 1),
    _ZhoneCpeCondDhcpSrvListIndex_Type()
)
zhoneCpeCondDhcpSrvListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvListIndex.setStatus("current")
_ZhoneCpeCondDhcpSrvListRowStatus_Type = RowStatus
_ZhoneCpeCondDhcpSrvListRowStatus_Object = MibTableColumn
zhoneCpeCondDhcpSrvListRowStatus = _ZhoneCpeCondDhcpSrvListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 32, 2, 1, 2),
    _ZhoneCpeCondDhcpSrvListRowStatus_Type()
)
zhoneCpeCondDhcpSrvListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvListRowStatus.setStatus("current")
_ZhoneCpeCondDhcpSrvListProfileName_Type = ZhoneAdminString
_ZhoneCpeCondDhcpSrvListProfileName_Object = MibTableColumn
zhoneCpeCondDhcpSrvListProfileName = _ZhoneCpeCondDhcpSrvListProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 32, 2, 1, 3),
    _ZhoneCpeCondDhcpSrvListProfileName_Type()
)
zhoneCpeCondDhcpSrvListProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvListProfileName.setStatus("current")
_ZhoneCpeCondDhcpSrv_ObjectIdentity = ObjectIdentity
zhoneCpeCondDhcpSrv = _ZhoneCpeCondDhcpSrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33)
)
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrv.setStatus("current")
_ZhoneCpeCondDhcpSrvIndexTable_Object = MibTable
zhoneCpeCondDhcpSrvIndexTable = _ZhoneCpeCondDhcpSrvIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33, 1)
)
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvIndexTable.setStatus("current")
_ZhoneCpeCondDhcpSrvIndexEntry_Object = MibTableRow
zhoneCpeCondDhcpSrvIndexEntry = _ZhoneCpeCondDhcpSrvIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33, 1, 1)
)
zhoneCpeCondDhcpSrvIndexEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeCondDhcpSrvListIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvIndexEntry.setStatus("current")
_ZhoneCpeCondDhcpSrvIndexEntryIndexNext_Type = Integer32
_ZhoneCpeCondDhcpSrvIndexEntryIndexNext_Object = MibTableColumn
zhoneCpeCondDhcpSrvIndexEntryIndexNext = _ZhoneCpeCondDhcpSrvIndexEntryIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33, 1, 1, 1),
    _ZhoneCpeCondDhcpSrvIndexEntryIndexNext_Type()
)
zhoneCpeCondDhcpSrvIndexEntryIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvIndexEntryIndexNext.setStatus("current")
_ZhoneCpeCondDhcpSrvTable_Object = MibTable
zhoneCpeCondDhcpSrvTable = _ZhoneCpeCondDhcpSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33, 2)
)
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvTable.setStatus("current")
_ZhoneCpeCondDhcpSrvEntry_Object = MibTableRow
zhoneCpeCondDhcpSrvEntry = _ZhoneCpeCondDhcpSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33, 2, 1)
)
zhoneCpeCondDhcpSrvEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeCondDhcpSrvListIndex"),
    (0, "Zhone-CPE-MIB", "zhoneCpeCondDhcpSrvEntryIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvEntry.setStatus("current")
_ZhoneCpeCondDhcpSrvEntryIndex_Type = Unsigned32
_ZhoneCpeCondDhcpSrvEntryIndex_Object = MibTableColumn
zhoneCpeCondDhcpSrvEntryIndex = _ZhoneCpeCondDhcpSrvEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33, 2, 1, 1),
    _ZhoneCpeCondDhcpSrvEntryIndex_Type()
)
zhoneCpeCondDhcpSrvEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvEntryIndex.setStatus("current")
_ZhoneCpeCondDhcpSrvRowStatus_Type = RowStatus
_ZhoneCpeCondDhcpSrvRowStatus_Object = MibTableColumn
zhoneCpeCondDhcpSrvRowStatus = _ZhoneCpeCondDhcpSrvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33, 2, 1, 2),
    _ZhoneCpeCondDhcpSrvRowStatus_Type()
)
zhoneCpeCondDhcpSrvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvRowStatus.setStatus("current")


class _ZhoneCpeCondDhcpSrvAdminState_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeCondDhcpSrvAdminState based on ZhoneEnabledFlag"""


_ZhoneCpeCondDhcpSrvAdminState_Object = MibTableColumn
zhoneCpeCondDhcpSrvAdminState = _ZhoneCpeCondDhcpSrvAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33, 2, 1, 3),
    _ZhoneCpeCondDhcpSrvAdminState_Type()
)
zhoneCpeCondDhcpSrvAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvAdminState.setStatus("current")
_ZhoneCpeCondDhcpSrvPriorityOrder_Type = Integer32
_ZhoneCpeCondDhcpSrvPriorityOrder_Object = MibTableColumn
zhoneCpeCondDhcpSrvPriorityOrder = _ZhoneCpeCondDhcpSrvPriorityOrder_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33, 2, 1, 4),
    _ZhoneCpeCondDhcpSrvPriorityOrder_Type()
)
zhoneCpeCondDhcpSrvPriorityOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvPriorityOrder.setStatus("current")
_ZhoneCpeCondDhcpVciOui_Type = ZhoneAdminString
_ZhoneCpeCondDhcpVciOui_Object = MibTableColumn
zhoneCpeCondDhcpVciOui = _ZhoneCpeCondDhcpVciOui_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33, 2, 1, 5),
    _ZhoneCpeCondDhcpVciOui_Type()
)
zhoneCpeCondDhcpVciOui.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpVciOui.setStatus("current")


class _ZhoneCpeCondDhcpSrvVciMatch_Type(Integer32):
    """Custom type zhoneCpeCondDhcpSrvVciMatch based on Integer32"""
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
        *(("prefix", 1),
          ("substring", 3),
          ("suffix", 2))
    )


_ZhoneCpeCondDhcpSrvVciMatch_Type.__name__ = "Integer32"
_ZhoneCpeCondDhcpSrvVciMatch_Object = MibTableColumn
zhoneCpeCondDhcpSrvVciMatch = _ZhoneCpeCondDhcpSrvVciMatch_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33, 2, 1, 6),
    _ZhoneCpeCondDhcpSrvVciMatch_Type()
)
zhoneCpeCondDhcpSrvVciMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvVciMatch.setStatus("current")
_ZhoneCpeCondDhcpSrvStartAddr_Type = IpAddress
_ZhoneCpeCondDhcpSrvStartAddr_Object = MibTableColumn
zhoneCpeCondDhcpSrvStartAddr = _ZhoneCpeCondDhcpSrvStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33, 2, 1, 7),
    _ZhoneCpeCondDhcpSrvStartAddr_Type()
)
zhoneCpeCondDhcpSrvStartAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvStartAddr.setStatus("current")
_ZhoneCpeCondDhcpSrvEndAddr_Type = IpAddress
_ZhoneCpeCondDhcpSrvEndAddr_Object = MibTableColumn
zhoneCpeCondDhcpSrvEndAddr = _ZhoneCpeCondDhcpSrvEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33, 2, 1, 8),
    _ZhoneCpeCondDhcpSrvEndAddr_Type()
)
zhoneCpeCondDhcpSrvEndAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvEndAddr.setStatus("current")


class _ZhoneCpeCondDhcpSrvWanVlan_Type(Unsigned32):
    """Custom type zhoneCpeCondDhcpSrvWanVlan based on Unsigned32"""
    defaultBinValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ZhoneCpeCondDhcpSrvWanVlan_Type.__name__ = "Unsigned32"
_ZhoneCpeCondDhcpSrvWanVlan_Object = MibTableColumn
zhoneCpeCondDhcpSrvWanVlan = _ZhoneCpeCondDhcpSrvWanVlan_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33, 2, 1, 9),
    _ZhoneCpeCondDhcpSrvWanVlan_Type()
)
zhoneCpeCondDhcpSrvWanVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvWanVlan.setStatus("current")


class _ZhoneCpeCondDhcpSrvPortFwdRule_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeCondDhcpSrvPortFwdRule based on ZhoneEnabledFlag"""


_ZhoneCpeCondDhcpSrvPortFwdRule_Object = MibTableColumn
zhoneCpeCondDhcpSrvPortFwdRule = _ZhoneCpeCondDhcpSrvPortFwdRule_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33, 2, 1, 10),
    _ZhoneCpeCondDhcpSrvPortFwdRule_Type()
)
zhoneCpeCondDhcpSrvPortFwdRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvPortFwdRule.setStatus("current")


class _ZhoneCpeCondDhcpSrvStartPort_Type(Unsigned32):
    """Custom type zhoneCpeCondDhcpSrvStartPort based on Unsigned32"""
    defaultValue = 65501

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneCpeCondDhcpSrvStartPort_Type.__name__ = "Unsigned32"
_ZhoneCpeCondDhcpSrvStartPort_Object = MibTableColumn
zhoneCpeCondDhcpSrvStartPort = _ZhoneCpeCondDhcpSrvStartPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33, 2, 1, 11),
    _ZhoneCpeCondDhcpSrvStartPort_Type()
)
zhoneCpeCondDhcpSrvStartPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvStartPort.setStatus("current")


class _ZhoneCpeCondDhcpSrvPrivatePort_Type(Unsigned32):
    """Custom type zhoneCpeCondDhcpSrvPrivatePort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneCpeCondDhcpSrvPrivatePort_Type.__name__ = "Unsigned32"
_ZhoneCpeCondDhcpSrvPrivatePort_Object = MibTableColumn
zhoneCpeCondDhcpSrvPrivatePort = _ZhoneCpeCondDhcpSrvPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33, 2, 1, 12),
    _ZhoneCpeCondDhcpSrvPrivatePort_Type()
)
zhoneCpeCondDhcpSrvPrivatePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvPrivatePort.setStatus("current")


class _ZhoneCpeCondDhcpSrvProtocol_Type(Integer32):
    """Custom type zhoneCpeCondDhcpSrvProtocol based on Integer32"""
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
        *(("both", 3),
          ("tcp", 1),
          ("udp", 2))
    )


_ZhoneCpeCondDhcpSrvProtocol_Type.__name__ = "Integer32"
_ZhoneCpeCondDhcpSrvProtocol_Object = MibTableColumn
zhoneCpeCondDhcpSrvProtocol = _ZhoneCpeCondDhcpSrvProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33, 2, 1, 13),
    _ZhoneCpeCondDhcpSrvProtocol_Type()
)
zhoneCpeCondDhcpSrvProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvProtocol.setStatus("current")


class _ZhoneCpeCondDhcpSrvPriDns_Type(IpAddress):
    """Custom type zhoneCpeCondDhcpSrvPriDns based on IpAddress"""
    defaultHexValue = "00000000"


_ZhoneCpeCondDhcpSrvPriDns_Object = MibTableColumn
zhoneCpeCondDhcpSrvPriDns = _ZhoneCpeCondDhcpSrvPriDns_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33, 2, 1, 14),
    _ZhoneCpeCondDhcpSrvPriDns_Type()
)
zhoneCpeCondDhcpSrvPriDns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvPriDns.setStatus("current")


class _ZhoneCpeCondDhcpSrvSecDns_Type(IpAddress):
    """Custom type zhoneCpeCondDhcpSrvSecDns based on IpAddress"""
    defaultHexValue = "00000000"


_ZhoneCpeCondDhcpSrvSecDns_Object = MibTableColumn
zhoneCpeCondDhcpSrvSecDns = _ZhoneCpeCondDhcpSrvSecDns_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33, 2, 1, 15),
    _ZhoneCpeCondDhcpSrvSecDns_Type()
)
zhoneCpeCondDhcpSrvSecDns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvSecDns.setStatus("current")


class _ZhoneCpeCondDhcpSrvPriNpt_Type(IpAddress):
    """Custom type zhoneCpeCondDhcpSrvPriNpt based on IpAddress"""
    defaultHexValue = "00000000"


_ZhoneCpeCondDhcpSrvPriNpt_Object = MibTableColumn
zhoneCpeCondDhcpSrvPriNpt = _ZhoneCpeCondDhcpSrvPriNpt_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33, 2, 1, 16),
    _ZhoneCpeCondDhcpSrvPriNpt_Type()
)
zhoneCpeCondDhcpSrvPriNpt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvPriNpt.setStatus("current")


class _ZhoneCpeCondDhcpSrvSecNpt_Type(IpAddress):
    """Custom type zhoneCpeCondDhcpSrvSecNpt based on IpAddress"""
    defaultHexValue = "00000000"


_ZhoneCpeCondDhcpSrvSecNpt_Object = MibTableColumn
zhoneCpeCondDhcpSrvSecNpt = _ZhoneCpeCondDhcpSrvSecNpt_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33, 2, 1, 17),
    _ZhoneCpeCondDhcpSrvSecNpt_Type()
)
zhoneCpeCondDhcpSrvSecNpt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvSecNpt.setStatus("current")
_ZhoneCpeCondDhcpSrvVsi_Type = ZhoneAdminString
_ZhoneCpeCondDhcpSrvVsi_Object = MibTableColumn
zhoneCpeCondDhcpSrvVsi = _ZhoneCpeCondDhcpSrvVsi_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33, 2, 1, 18),
    _ZhoneCpeCondDhcpSrvVsi_Type()
)
zhoneCpeCondDhcpSrvVsi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvVsi.setStatus("current")


class _ZhoneCpeCondDhcpSrvPermanent_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeCondDhcpSrvPermanent based on ZhoneEnabledFlag"""


_ZhoneCpeCondDhcpSrvPermanent_Object = MibTableColumn
zhoneCpeCondDhcpSrvPermanent = _ZhoneCpeCondDhcpSrvPermanent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 33, 2, 1, 19),
    _ZhoneCpeCondDhcpSrvPermanent_Type()
)
zhoneCpeCondDhcpSrvPermanent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvPermanent.setStatus("current")
_ZhoneCpeCmd_ObjectIdentity = ObjectIdentity
zhoneCpeCmd = _ZhoneCpeCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34)
)


class _ZhoneCpeCmdOperation_Type(Integer32):
    """Custom type zhoneCpeCmdOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              10,
              11,
              12,
              13,
              15,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              40,
              41,
              42,
              60,
              61,
              70,
              80)
        )
    )
    namedValues = NamedValues(
        *(("applyCpeToCpe", 42),
          ("applyCpeToPort", 41),
          ("applyCpeToSlot", 40),
          ("applySvcToCpe", 70),
          ("cloneCpeToCpe", 22),
          ("cloneCpeToPort", 26),
          ("cloneCpeToSlot", 25),
          ("clonePortToPort", 21),
          ("cloneServiceToService", 24),
          ("cloneSlotToSlot", 20),
          ("cloneUniToUni", 23),
          ("createVirtualCpe", 60),
          ("deleteCpe", 3),
          ("deletePort", 2),
          ("deleteService", 5),
          ("deleteSlot", 1),
          ("deleteUni", 4),
          ("deleteVirtualCpe", 61),
          ("moveCpeToCpe", 12),
          ("movePortToPort", 11),
          ("moveServiceToService", 15),
          ("moveSlotToSlot", 10),
          ("moveUniToUni", 13),
          ("removeSvcFromCpe", 80))
    )


_ZhoneCpeCmdOperation_Type.__name__ = "Integer32"
_ZhoneCpeCmdOperation_Object = MibScalar
zhoneCpeCmdOperation = _ZhoneCpeCmdOperation_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 1),
    _ZhoneCpeCmdOperation_Type()
)
zhoneCpeCmdOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdOperation.setStatus("current")
_ZhoneCpeCmdSrcIfIndex_Type = Unsigned32
_ZhoneCpeCmdSrcIfIndex_Object = MibScalar
zhoneCpeCmdSrcIfIndex = _ZhoneCpeCmdSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 2),
    _ZhoneCpeCmdSrcIfIndex_Type()
)
zhoneCpeCmdSrcIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdSrcIfIndex.setStatus("current")
_ZhoneCpeCmdSrcShelf_Type = Unsigned32
_ZhoneCpeCmdSrcShelf_Object = MibScalar
zhoneCpeCmdSrcShelf = _ZhoneCpeCmdSrcShelf_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 3),
    _ZhoneCpeCmdSrcShelf_Type()
)
zhoneCpeCmdSrcShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdSrcShelf.setStatus("current")
_ZhoneCpeCmdSrcSlot_Type = Unsigned32
_ZhoneCpeCmdSrcSlot_Object = MibScalar
zhoneCpeCmdSrcSlot = _ZhoneCpeCmdSrcSlot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 4),
    _ZhoneCpeCmdSrcSlot_Type()
)
zhoneCpeCmdSrcSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdSrcSlot.setStatus("current")
_ZhoneCpeCmdSrcPort_Type = Unsigned32
_ZhoneCpeCmdSrcPort_Object = MibScalar
zhoneCpeCmdSrcPort = _ZhoneCpeCmdSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 5),
    _ZhoneCpeCmdSrcPort_Type()
)
zhoneCpeCmdSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdSrcPort.setStatus("current")
_ZhoneCpeCmdSrcSubport_Type = Unsigned32
_ZhoneCpeCmdSrcSubport_Object = MibScalar
zhoneCpeCmdSrcSubport = _ZhoneCpeCmdSrcSubport_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 6),
    _ZhoneCpeCmdSrcSubport_Type()
)
zhoneCpeCmdSrcSubport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdSrcSubport.setStatus("current")
_ZhoneCpeCmdSrcTpType_Type = TpType
_ZhoneCpeCmdSrcTpType_Object = MibScalar
zhoneCpeCmdSrcTpType = _ZhoneCpeCmdSrcTpType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 7),
    _ZhoneCpeCmdSrcTpType_Type()
)
zhoneCpeCmdSrcTpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdSrcTpType.setStatus("current")
_ZhoneCpeCmdSrcTpIndex_Type = Unsigned32
_ZhoneCpeCmdSrcTpIndex_Object = MibScalar
zhoneCpeCmdSrcTpIndex = _ZhoneCpeCmdSrcTpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 8),
    _ZhoneCpeCmdSrcTpIndex_Type()
)
zhoneCpeCmdSrcTpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdSrcTpIndex.setStatus("current")
_ZhoneCpeCmdDstIfIndex_Type = Unsigned32
_ZhoneCpeCmdDstIfIndex_Object = MibScalar
zhoneCpeCmdDstIfIndex = _ZhoneCpeCmdDstIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 9),
    _ZhoneCpeCmdDstIfIndex_Type()
)
zhoneCpeCmdDstIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdDstIfIndex.setStatus("current")
_ZhoneCpeCmdDstShelf_Type = Unsigned32
_ZhoneCpeCmdDstShelf_Object = MibScalar
zhoneCpeCmdDstShelf = _ZhoneCpeCmdDstShelf_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 10),
    _ZhoneCpeCmdDstShelf_Type()
)
zhoneCpeCmdDstShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdDstShelf.setStatus("current")
_ZhoneCpeCmdDstSlot_Type = Unsigned32
_ZhoneCpeCmdDstSlot_Object = MibScalar
zhoneCpeCmdDstSlot = _ZhoneCpeCmdDstSlot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 11),
    _ZhoneCpeCmdDstSlot_Type()
)
zhoneCpeCmdDstSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdDstSlot.setStatus("current")
_ZhoneCpeCmdDstPort_Type = Unsigned32
_ZhoneCpeCmdDstPort_Object = MibScalar
zhoneCpeCmdDstPort = _ZhoneCpeCmdDstPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 12),
    _ZhoneCpeCmdDstPort_Type()
)
zhoneCpeCmdDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdDstPort.setStatus("current")
_ZhoneCpeCmdDstSubport_Type = Unsigned32
_ZhoneCpeCmdDstSubport_Object = MibScalar
zhoneCpeCmdDstSubport = _ZhoneCpeCmdDstSubport_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 13),
    _ZhoneCpeCmdDstSubport_Type()
)
zhoneCpeCmdDstSubport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdDstSubport.setStatus("current")
_ZhoneCpeCmdDstTpType_Type = TpType
_ZhoneCpeCmdDstTpType_Object = MibScalar
zhoneCpeCmdDstTpType = _ZhoneCpeCmdDstTpType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 14),
    _ZhoneCpeCmdDstTpType_Type()
)
zhoneCpeCmdDstTpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdDstTpType.setStatus("current")
_ZhoneCpeCmdDstTpIndex_Type = Unsigned32
_ZhoneCpeCmdDstTpIndex_Object = MibScalar
zhoneCpeCmdDstTpIndex = _ZhoneCpeCmdDstTpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 15),
    _ZhoneCpeCmdDstTpIndex_Type()
)
zhoneCpeCmdDstTpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdDstTpIndex.setStatus("current")
_ZhoneCpeCmdString_Type = ZhoneAdminString
_ZhoneCpeCmdString_Object = MibScalar
zhoneCpeCmdString = _ZhoneCpeCmdString_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 16),
    _ZhoneCpeCmdString_Type()
)
zhoneCpeCmdString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdString.setStatus("current")
_ZhoneCpeCmdSvcTemplateType_Type = ZhoneCpeTemplateType
_ZhoneCpeCmdSvcTemplateType_Object = MibScalar
zhoneCpeCmdSvcTemplateType = _ZhoneCpeCmdSvcTemplateType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 17),
    _ZhoneCpeCmdSvcTemplateType_Type()
)
zhoneCpeCmdSvcTemplateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdSvcTemplateType.setStatus("current")
_ZhoneCpeCmdSvcTemplateId_Type = Unsigned32
_ZhoneCpeCmdSvcTemplateId_Object = MibScalar
zhoneCpeCmdSvcTemplateId = _ZhoneCpeCmdSvcTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 18),
    _ZhoneCpeCmdSvcTemplateId_Type()
)
zhoneCpeCmdSvcTemplateId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdSvcTemplateId.setStatus("current")
_ZhoneCpeCmdSvcTemplateIfIndex_Type = Unsigned32
_ZhoneCpeCmdSvcTemplateIfIndex_Object = MibScalar
zhoneCpeCmdSvcTemplateIfIndex = _ZhoneCpeCmdSvcTemplateIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 19),
    _ZhoneCpeCmdSvcTemplateIfIndex_Type()
)
zhoneCpeCmdSvcTemplateIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdSvcTemplateIfIndex.setStatus("current")
_ZhoneCpeCmdSvcTemplateVirtualConn_Type = Unsigned32
_ZhoneCpeCmdSvcTemplateVirtualConn_Object = MibScalar
zhoneCpeCmdSvcTemplateVirtualConn = _ZhoneCpeCmdSvcTemplateVirtualConn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 20),
    _ZhoneCpeCmdSvcTemplateVirtualConn_Type()
)
zhoneCpeCmdSvcTemplateVirtualConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdSvcTemplateVirtualConn.setStatus("current")
_ZhoneCpeCmdSvcTemplateTpType_Type = TpType
_ZhoneCpeCmdSvcTemplateTpType_Object = MibScalar
zhoneCpeCmdSvcTemplateTpType = _ZhoneCpeCmdSvcTemplateTpType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 21),
    _ZhoneCpeCmdSvcTemplateTpType_Type()
)
zhoneCpeCmdSvcTemplateTpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdSvcTemplateTpType.setStatus("current")
_ZhoneCpeCmdSvcTemplateTpIndex_Type = Unsigned32
_ZhoneCpeCmdSvcTemplateTpIndex_Object = MibScalar
zhoneCpeCmdSvcTemplateTpIndex = _ZhoneCpeCmdSvcTemplateTpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 22),
    _ZhoneCpeCmdSvcTemplateTpIndex_Type()
)
zhoneCpeCmdSvcTemplateTpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdSvcTemplateTpIndex.setStatus("current")
_ZhoneCpeCmdSvcTemplateVlan_Type = Unsigned32
_ZhoneCpeCmdSvcTemplateVlan_Object = MibScalar
zhoneCpeCmdSvcTemplateVlan = _ZhoneCpeCmdSvcTemplateVlan_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 23),
    _ZhoneCpeCmdSvcTemplateVlan_Type()
)
zhoneCpeCmdSvcTemplateVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdSvcTemplateVlan.setStatus("current")
_ZhoneCpeCmdSvcTemplateSlan_Type = Unsigned32
_ZhoneCpeCmdSvcTemplateSlan_Object = MibScalar
zhoneCpeCmdSvcTemplateSlan = _ZhoneCpeCmdSvcTemplateSlan_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 24),
    _ZhoneCpeCmdSvcTemplateSlan_Type()
)
zhoneCpeCmdSvcTemplateSlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdSvcTemplateSlan.setStatus("current")
_ZhoneCpeCmdOverrideTpIndex_Type = Unsigned32
_ZhoneCpeCmdOverrideTpIndex_Object = MibScalar
zhoneCpeCmdOverrideTpIndex = _ZhoneCpeCmdOverrideTpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 25),
    _ZhoneCpeCmdOverrideTpIndex_Type()
)
zhoneCpeCmdOverrideTpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdOverrideTpIndex.setStatus("current")
_ZhoneCpeCmdOverrideVlanId_Type = Unsigned32
_ZhoneCpeCmdOverrideVlanId_Object = MibScalar
zhoneCpeCmdOverrideVlanId = _ZhoneCpeCmdOverrideVlanId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 26),
    _ZhoneCpeCmdOverrideVlanId_Type()
)
zhoneCpeCmdOverrideVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdOverrideVlanId.setStatus("current")
_ZhoneCpeCmdOverrideVlanCos_Type = Unsigned32
_ZhoneCpeCmdOverrideVlanCos_Object = MibScalar
zhoneCpeCmdOverrideVlanCos = _ZhoneCpeCmdOverrideVlanCos_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 27),
    _ZhoneCpeCmdOverrideVlanCos_Type()
)
zhoneCpeCmdOverrideVlanCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdOverrideVlanCos.setStatus("current")
_ZhoneCpeCmdOverrideSlanId_Type = Unsigned32
_ZhoneCpeCmdOverrideSlanId_Object = MibScalar
zhoneCpeCmdOverrideSlanId = _ZhoneCpeCmdOverrideSlanId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 28),
    _ZhoneCpeCmdOverrideSlanId_Type()
)
zhoneCpeCmdOverrideSlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdOverrideSlanId.setStatus("current")
_ZhoneCpeCmdOverrideSlanCos_Type = Unsigned32
_ZhoneCpeCmdOverrideSlanCos_Object = MibScalar
zhoneCpeCmdOverrideSlanCos = _ZhoneCpeCmdOverrideSlanCos_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 34, 29),
    _ZhoneCpeCmdOverrideSlanCos_Type()
)
zhoneCpeCmdOverrideSlanCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCmdOverrideSlanCos.setStatus("current")
_ZhoneCpeLldpMedPolicyList_ObjectIdentity = ObjectIdentity
zhoneCpeLldpMedPolicyList = _ZhoneCpeLldpMedPolicyList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 35)
)
if mibBuilder.loadTexts:
    zhoneCpeLldpMedPolicyList.setStatus("current")
_ZhoneCpeLldpMedPolicyListIndexNext_Type = Integer32
_ZhoneCpeLldpMedPolicyListIndexNext_Object = MibScalar
zhoneCpeLldpMedPolicyListIndexNext = _ZhoneCpeLldpMedPolicyListIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 35, 1),
    _ZhoneCpeLldpMedPolicyListIndexNext_Type()
)
zhoneCpeLldpMedPolicyListIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeLldpMedPolicyListIndexNext.setStatus("current")
_ZhoneCpeLldpMedPolicyListTable_Object = MibTable
zhoneCpeLldpMedPolicyListTable = _ZhoneCpeLldpMedPolicyListTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 35, 2)
)
if mibBuilder.loadTexts:
    zhoneCpeLldpMedPolicyListTable.setStatus("current")
_ZhoneCpeLldpMedPolicyListEntry_Object = MibTableRow
zhoneCpeLldpMedPolicyListEntry = _ZhoneCpeLldpMedPolicyListEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 35, 2, 1)
)
zhoneCpeLldpMedPolicyListEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeLldpMedPolicyListIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeLldpMedPolicyListEntry.setStatus("current")
_ZhoneCpeLldpMedPolicyListIndex_Type = Unsigned32
_ZhoneCpeLldpMedPolicyListIndex_Object = MibTableColumn
zhoneCpeLldpMedPolicyListIndex = _ZhoneCpeLldpMedPolicyListIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 35, 2, 1, 1),
    _ZhoneCpeLldpMedPolicyListIndex_Type()
)
zhoneCpeLldpMedPolicyListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeLldpMedPolicyListIndex.setStatus("current")


class _ZhoneCpeLldpMedPolicyListRowStatus_Type(RowStatus):
    """Custom type zhoneCpeLldpMedPolicyListRowStatus based on RowStatus"""


_ZhoneCpeLldpMedPolicyListRowStatus_Object = MibTableColumn
zhoneCpeLldpMedPolicyListRowStatus = _ZhoneCpeLldpMedPolicyListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 35, 2, 1, 2),
    _ZhoneCpeLldpMedPolicyListRowStatus_Type()
)
zhoneCpeLldpMedPolicyListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeLldpMedPolicyListRowStatus.setStatus("current")
_ZhoneCpeLldpMedPolicyListProfileName_Type = ZhoneAdminString
_ZhoneCpeLldpMedPolicyListProfileName_Object = MibTableColumn
zhoneCpeLldpMedPolicyListProfileName = _ZhoneCpeLldpMedPolicyListProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 35, 2, 1, 3),
    _ZhoneCpeLldpMedPolicyListProfileName_Type()
)
zhoneCpeLldpMedPolicyListProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeLldpMedPolicyListProfileName.setStatus("current")
_ZhoneCpeLldpMedPolicy_ObjectIdentity = ObjectIdentity
zhoneCpeLldpMedPolicy = _ZhoneCpeLldpMedPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 36)
)
if mibBuilder.loadTexts:
    zhoneCpeLldpMedPolicy.setStatus("current")
_ZhoneCpeLldpMedPolicyIndexTable_Object = MibTable
zhoneCpeLldpMedPolicyIndexTable = _ZhoneCpeLldpMedPolicyIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 36, 1)
)
if mibBuilder.loadTexts:
    zhoneCpeLldpMedPolicyIndexTable.setStatus("current")
_ZhoneCpeLldpMedPolicyIndexEntry_Object = MibTableRow
zhoneCpeLldpMedPolicyIndexEntry = _ZhoneCpeLldpMedPolicyIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 36, 1, 1)
)
zhoneCpeLldpMedPolicyIndexEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeLldpMedPolicyListIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeLldpMedPolicyIndexEntry.setStatus("current")
_ZhoneCpeLldpMedPolicyIndexEntryIndexNext_Type = Integer32
_ZhoneCpeLldpMedPolicyIndexEntryIndexNext_Object = MibTableColumn
zhoneCpeLldpMedPolicyIndexEntryIndexNext = _ZhoneCpeLldpMedPolicyIndexEntryIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 36, 1, 1, 1),
    _ZhoneCpeLldpMedPolicyIndexEntryIndexNext_Type()
)
zhoneCpeLldpMedPolicyIndexEntryIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeLldpMedPolicyIndexEntryIndexNext.setStatus("current")
_ZhoneCpeLldpMedPolicyTable_Object = MibTable
zhoneCpeLldpMedPolicyTable = _ZhoneCpeLldpMedPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 36, 2)
)
if mibBuilder.loadTexts:
    zhoneCpeLldpMedPolicyTable.setStatus("current")
_ZhoneCpeLldpMedPolicyEntry_Object = MibTableRow
zhoneCpeLldpMedPolicyEntry = _ZhoneCpeLldpMedPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 36, 2, 1)
)
zhoneCpeLldpMedPolicyEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeLldpMedPolicyListIndex"),
    (0, "Zhone-CPE-MIB", "zhoneCpeLldpMedPolicyEntryIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeLldpMedPolicyEntry.setStatus("current")
_ZhoneCpeLldpMedPolicyEntryIndex_Type = Unsigned32
_ZhoneCpeLldpMedPolicyEntryIndex_Object = MibTableColumn
zhoneCpeLldpMedPolicyEntryIndex = _ZhoneCpeLldpMedPolicyEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 36, 2, 1, 1),
    _ZhoneCpeLldpMedPolicyEntryIndex_Type()
)
zhoneCpeLldpMedPolicyEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeLldpMedPolicyEntryIndex.setStatus("current")


class _ZhoneCpeLldpMedPolicyRowStatus_Type(RowStatus):
    """Custom type zhoneCpeLldpMedPolicyRowStatus based on RowStatus"""


_ZhoneCpeLldpMedPolicyRowStatus_Object = MibTableColumn
zhoneCpeLldpMedPolicyRowStatus = _ZhoneCpeLldpMedPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 36, 2, 1, 2),
    _ZhoneCpeLldpMedPolicyRowStatus_Type()
)
zhoneCpeLldpMedPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeLldpMedPolicyRowStatus.setStatus("current")


class _ZhoneCpeLldpMedPolicyAdminState_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeLldpMedPolicyAdminState based on ZhoneEnabledFlag"""


_ZhoneCpeLldpMedPolicyAdminState_Object = MibTableColumn
zhoneCpeLldpMedPolicyAdminState = _ZhoneCpeLldpMedPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 36, 2, 1, 3),
    _ZhoneCpeLldpMedPolicyAdminState_Type()
)
zhoneCpeLldpMedPolicyAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeLldpMedPolicyAdminState.setStatus("current")


class _ZhoneCpeLldpMedPolicyAppType_Type(Integer32):
    """Custom type zhoneCpeLldpMedPolicyAppType based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("guestvoice", 3),
          ("guestvoicesignal", 4),
          ("softphone", 5),
          ("videoconf", 6),
          ("videosignal", 8),
          ("videostreaming", 7),
          ("voice", 1),
          ("voicesignal", 2))
    )


_ZhoneCpeLldpMedPolicyAppType_Type.__name__ = "Integer32"
_ZhoneCpeLldpMedPolicyAppType_Object = MibTableColumn
zhoneCpeLldpMedPolicyAppType = _ZhoneCpeLldpMedPolicyAppType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 36, 2, 1, 4),
    _ZhoneCpeLldpMedPolicyAppType_Type()
)
zhoneCpeLldpMedPolicyAppType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeLldpMedPolicyAppType.setStatus("current")


class _ZhoneCpeLldpMedPolicyVlanId_Type(Unsigned32):
    """Custom type zhoneCpeLldpMedPolicyVlanId based on Unsigned32"""
    defaultBinValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ZhoneCpeLldpMedPolicyVlanId_Type.__name__ = "Unsigned32"
_ZhoneCpeLldpMedPolicyVlanId_Object = MibTableColumn
zhoneCpeLldpMedPolicyVlanId = _ZhoneCpeLldpMedPolicyVlanId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 36, 2, 1, 5),
    _ZhoneCpeLldpMedPolicyVlanId_Type()
)
zhoneCpeLldpMedPolicyVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeLldpMedPolicyVlanId.setStatus("current")


class _ZhoneCpeLldpMedPolicyCos_Type(Unsigned32):
    """Custom type zhoneCpeLldpMedPolicyCos based on Unsigned32"""
    defaultBinValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ZhoneCpeLldpMedPolicyCos_Type.__name__ = "Unsigned32"
_ZhoneCpeLldpMedPolicyCos_Object = MibTableColumn
zhoneCpeLldpMedPolicyCos = _ZhoneCpeLldpMedPolicyCos_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 36, 2, 1, 6),
    _ZhoneCpeLldpMedPolicyCos_Type()
)
zhoneCpeLldpMedPolicyCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeLldpMedPolicyCos.setStatus("current")


class _ZhoneCpeLldpMedPolicyDscp_Type(OctetString):
    """Custom type zhoneCpeLldpMedPolicyDscp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ZhoneCpeLldpMedPolicyDscp_Type.__name__ = "OctetString"
_ZhoneCpeLldpMedPolicyDscp_Object = MibTableColumn
zhoneCpeLldpMedPolicyDscp = _ZhoneCpeLldpMedPolicyDscp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 36, 2, 1, 7),
    _ZhoneCpeLldpMedPolicyDscp_Type()
)
zhoneCpeLldpMedPolicyDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeLldpMedPolicyDscp.setStatus("current")
_ZhoneCpeAutoCfgRule_ObjectIdentity = ObjectIdentity
zhoneCpeAutoCfgRule = _ZhoneCpeAutoCfgRule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 37)
)
if mibBuilder.loadTexts:
    zhoneCpeAutoCfgRule.setStatus("current")
_ZhoneCpeAutoCfgRuleIndexNext_Type = Unsigned32
_ZhoneCpeAutoCfgRuleIndexNext_Object = MibScalar
zhoneCpeAutoCfgRuleIndexNext = _ZhoneCpeAutoCfgRuleIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 37, 1),
    _ZhoneCpeAutoCfgRuleIndexNext_Type()
)
zhoneCpeAutoCfgRuleIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCpeAutoCfgRuleIndexNext.setStatus("current")
_ZhoneCpeAutoCfgRuleTable_Object = MibTable
zhoneCpeAutoCfgRuleTable = _ZhoneCpeAutoCfgRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 37, 2)
)
if mibBuilder.loadTexts:
    zhoneCpeAutoCfgRuleTable.setStatus("current")
_ZhoneCpeAutoCfgRuleEntry_Object = MibTableRow
zhoneCpeAutoCfgRuleEntry = _ZhoneCpeAutoCfgRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 37, 2, 1)
)
zhoneCpeAutoCfgRuleEntry.setIndexNames(
    (0, "Zhone-CPE-MIB", "zhoneCpeAutoCfgRuleIndex"),
)
if mibBuilder.loadTexts:
    zhoneCpeAutoCfgRuleEntry.setStatus("current")
_ZhoneCpeAutoCfgRuleIndex_Type = Unsigned32
_ZhoneCpeAutoCfgRuleIndex_Object = MibTableColumn
zhoneCpeAutoCfgRuleIndex = _ZhoneCpeAutoCfgRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 37, 2, 1, 1),
    _ZhoneCpeAutoCfgRuleIndex_Type()
)
zhoneCpeAutoCfgRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCpeAutoCfgRuleIndex.setStatus("current")


class _ZhoneCpeAutoCfgRuleAdminState_Type(ZhoneAdminState):
    """Custom type zhoneCpeAutoCfgRuleAdminState based on ZhoneAdminState"""
    defaultValue = 1


_ZhoneCpeAutoCfgRuleAdminState_Object = MibTableColumn
zhoneCpeAutoCfgRuleAdminState = _ZhoneCpeAutoCfgRuleAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 37, 2, 1, 2),
    _ZhoneCpeAutoCfgRuleAdminState_Type()
)
zhoneCpeAutoCfgRuleAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeAutoCfgRuleAdminState.setStatus("current")


class _ZhoneCpeAutoCfgRulePriority_Type(Integer32):
    """Custom type zhoneCpeAutoCfgRulePriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneCpeAutoCfgRulePriority_Type.__name__ = "Integer32"
_ZhoneCpeAutoCfgRulePriority_Object = MibTableColumn
zhoneCpeAutoCfgRulePriority = _ZhoneCpeAutoCfgRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 37, 2, 1, 3),
    _ZhoneCpeAutoCfgRulePriority_Type()
)
zhoneCpeAutoCfgRulePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeAutoCfgRulePriority.setStatus("current")


class _ZhoneCpeAutoCfgRuleMatchExpression_Type(OctetString):
    """Custom type zhoneCpeAutoCfgRuleMatchExpression based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ZhoneCpeAutoCfgRuleMatchExpression_Type.__name__ = "OctetString"
_ZhoneCpeAutoCfgRuleMatchExpression_Object = MibTableColumn
zhoneCpeAutoCfgRuleMatchExpression = _ZhoneCpeAutoCfgRuleMatchExpression_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 37, 2, 1, 4),
    _ZhoneCpeAutoCfgRuleMatchExpression_Type()
)
zhoneCpeAutoCfgRuleMatchExpression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeAutoCfgRuleMatchExpression.setStatus("current")
_ZhoneCpeAutoCfgRuleServiceTemplate_Type = InterfaceIndex
_ZhoneCpeAutoCfgRuleServiceTemplate_Object = MibTableColumn
zhoneCpeAutoCfgRuleServiceTemplate = _ZhoneCpeAutoCfgRuleServiceTemplate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 37, 2, 1, 5),
    _ZhoneCpeAutoCfgRuleServiceTemplate_Type()
)
zhoneCpeAutoCfgRuleServiceTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeAutoCfgRuleServiceTemplate.setStatus("current")


class _ZhoneCpeAutoCfgRuleTargetUni_Type(OctetString):
    """Custom type zhoneCpeAutoCfgRuleTargetUni based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZhoneCpeAutoCfgRuleTargetUni_Type.__name__ = "OctetString"
_ZhoneCpeAutoCfgRuleTargetUni_Object = MibTableColumn
zhoneCpeAutoCfgRuleTargetUni = _ZhoneCpeAutoCfgRuleTargetUni_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 37, 2, 1, 6),
    _ZhoneCpeAutoCfgRuleTargetUni_Type()
)
zhoneCpeAutoCfgRuleTargetUni.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeAutoCfgRuleTargetUni.setStatus("current")


class _ZhoneCpeAutoCfgRuleDeleteBeforeApply_Type(TruthValue):
    """Custom type zhoneCpeAutoCfgRuleDeleteBeforeApply based on TruthValue"""


_ZhoneCpeAutoCfgRuleDeleteBeforeApply_Object = MibTableColumn
zhoneCpeAutoCfgRuleDeleteBeforeApply = _ZhoneCpeAutoCfgRuleDeleteBeforeApply_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 37, 2, 1, 7),
    _ZhoneCpeAutoCfgRuleDeleteBeforeApply_Type()
)
zhoneCpeAutoCfgRuleDeleteBeforeApply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeAutoCfgRuleDeleteBeforeApply.setStatus("current")
_ZhoneCpeAutoCfgRuleRowStatus_Type = ZhoneRowStatus
_ZhoneCpeAutoCfgRuleRowStatus_Object = MibTableColumn
zhoneCpeAutoCfgRuleRowStatus = _ZhoneCpeAutoCfgRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 37, 2, 1, 8),
    _ZhoneCpeAutoCfgRuleRowStatus_Type()
)
zhoneCpeAutoCfgRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeAutoCfgRuleRowStatus.setStatus("current")
_ZhoneCpeAutoCfgRuleProfileName_Type = ZhoneAdminString
_ZhoneCpeAutoCfgRuleProfileName_Object = MibTableColumn
zhoneCpeAutoCfgRuleProfileName = _ZhoneCpeAutoCfgRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 37, 2, 1, 9),
    _ZhoneCpeAutoCfgRuleProfileName_Type()
)
zhoneCpeAutoCfgRuleProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCpeAutoCfgRuleProfileName.setStatus("current")
_ZhoneCpeCfgGlobalSettings_ObjectIdentity = ObjectIdentity
zhoneCpeCfgGlobalSettings = _ZhoneCpeCfgGlobalSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 38)
)
if mibBuilder.loadTexts:
    zhoneCpeCfgGlobalSettings.setStatus("current")


class _ZhoneCpeCfgAutoAssign_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeCfgAutoAssign based on ZhoneEnabledFlag"""


_ZhoneCpeCfgAutoAssign_Object = MibScalar
zhoneCpeCfgAutoAssign = _ZhoneCpeCfgAutoAssign_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 38, 1),
    _ZhoneCpeCfgAutoAssign_Type()
)
zhoneCpeCfgAutoAssign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCfgAutoAssign.setStatus("current")


class _ZhoneCpeCfgAutoConfig_Type(ZhoneEnabledFlag):
    """Custom type zhoneCpeCfgAutoConfig based on ZhoneEnabledFlag"""


_ZhoneCpeCfgAutoConfig_Object = MibScalar
zhoneCpeCfgAutoConfig = _ZhoneCpeCfgAutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 38, 2),
    _ZhoneCpeCfgAutoConfig_Type()
)
zhoneCpeCfgAutoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCfgAutoConfig.setStatus("current")


class _ZhoneCpeCfgParamsStr_Type(OctetString):
    """Custom type zhoneCpeCfgParamsStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ZhoneCpeCfgParamsStr_Type.__name__ = "OctetString"
_ZhoneCpeCfgParamsStr_Object = MibScalar
zhoneCpeCfgParamsStr = _ZhoneCpeCfgParamsStr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 16, 1, 38, 3),
    _ZhoneCpeCfgParamsStr_Type()
)
zhoneCpeCfgParamsStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCpeCfgParamsStr.setStatus("current")

# Managed Objects groups

zhoneCpeSipDialPlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 36)
)
zhoneCpeSipDialPlanGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeSipDialPlanRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeSipDialPlanIndexNext"),
        ("Zhone-CPE-MIB", "zhoneCpeSipDialPlanFormat"),
        ("Zhone-CPE-MIB", "zhoneCpeSipDialPlanString"))
)
if mibBuilder.loadTexts:
    zhoneCpeSipDialPlanGroup.setStatus("current")

zhoneCpeVoipServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 37)
)
zhoneCpeVoipServerGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeVoipServerRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipProfileName"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipPrimaryServer"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipSecondaryServer"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipSipRegExpirationTime"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipSipReRegHeadStartTime"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipSipDomain"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipSipRegistrar"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipSoftSwitch"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipMgcVersion"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipMgcMessageFormat"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipMgcMaximumRetryTime"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipMgcMaximumRetryAttempts"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipMgcServiceChangeDelay"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipMgcTerminationIdBase"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipReleaseTimer"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipRohTimer"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipDscpMark"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipPiggyBackEvents"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipOobToneEvents"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipOobDtmfEvents"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipOobCasEvents"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipPartialDialTimeout"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipServerSignallingProtocol"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipServerPortId"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipServerOutboundServer"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipCasEventsPassingMethod"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipDtmfEventsPassingMethod"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipCriticalDialTimeout"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipServerIndexNext"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipFeaturesWarmLineTimer"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipFeaturesHotLineNumber"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipFeaturesHotLine"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipMgcpPersistentNotify"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipMgcpClientAddressMode"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipSignalingDscp"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipRtpDscp"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipSipRegRetryTime"))
)
if mibBuilder.loadTexts:
    zhoneCpeVoipServerGroup.setStatus("current")

zhoneCpeIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 38)
)
zhoneCpeIpGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeIpRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeHostIp"),
        ("Zhone-CPE-MIB", "zhoneCpeIpServerProfileIndex"))
)
if mibBuilder.loadTexts:
    zhoneCpeIpGroup.setStatus("current")

zhoneCpeIpServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 39)
)
zhoneCpeIpServerGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeIpServerRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeIpServerProfileName"),
        ("Zhone-CPE-MIB", "zhoneCpeIpServerHostIpOption"),
        ("Zhone-CPE-MIB", "zhoneCpeIpServerNetmask"),
        ("Zhone-CPE-MIB", "zhoneCpeIpServerGateway"),
        ("Zhone-CPE-MIB", "zhoneCpeIpServerPrimaryDns"),
        ("Zhone-CPE-MIB", "zhoneCpeIpServerNat"),
        ("Zhone-CPE-MIB", "zhoneCpeIpServerFirewallAccess"),
        ("Zhone-CPE-MIB", "zhoneCpeIpServerIgmpFunction"),
        ("Zhone-CPE-MIB", "zhoneCpeIpServerSecureForward"),
        ("Zhone-CPE-MIB", "zhoneCpeIpServerDnsType"),
        ("Zhone-CPE-MIB", "zhoneCpeIpServerDnsSrc"),
        ("Zhone-CPE-MIB", "zhoneCpeIpServerDefaultIface"),
        ("Zhone-CPE-MIB", "zhoneCpeIpServerSecondaryDns"),
        ("Zhone-CPE-MIB", "zhoneCpeIpServerIndexNext"))
)
if mibBuilder.loadTexts:
    zhoneCpeIpServerGroup.setStatus("current")

zhoneCpeVoipFeaturesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 40)
)
zhoneCpeVoipFeaturesGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeVoipFeaturesRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipFeaturesProfileName"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipFeaturesAnnouncementType"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipCidFeatures"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipCallWaitingFeatures"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipCallProgressOrTransferFeatures"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipFeaturesIndexNext"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipFeaturesWarmLineTimer"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipFeaturesHotLineNumber"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipFeaturesHotLine"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipCallPresentationFeatures"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipServerIndexNext"))
)
if mibBuilder.loadTexts:
    zhoneCpeVoipFeaturesGroup.setStatus("current")

zhoneCpeVoipMediaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 41)
)
zhoneCpeVoipMediaGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeVoipMediaRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipMediaProfileName"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipMediaEchoCancel"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipFaxMode"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipCodecSelectionFirstOrder"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipPacketPeriodSelectionFirstOrder"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipSilenceSuppressionFirstOrder"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipCodecSelectionSecondOrder"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipPacketPeriodSelectionSecondOrder"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipSilenceSuppressionSecondOrder"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipCodecSelectionThirdOrder"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipPacketPeriodSelectionThirdOrder"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipSilenceSuppressionThirdOrder"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipCodecSelectionFourthOrder"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipPacketPeriodSelectionFourthOrder"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipSilenceSuppressionFourthOrder"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipMediaIndexNext"))
)
if mibBuilder.loadTexts:
    zhoneCpeVoipMediaGroup.setStatus("current")

zhoneCpeVoipSubscriberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 42)
)
zhoneCpeVoipSubscriberGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeVoipSubscriberRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipSubscriberAdminState"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipSubscriberDialNumber"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipSubscriberDisplayName"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipSubscriberUserName"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipSubscriberPassword"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipServerProfileIndex"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipFeaturesProfileIndex"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipSubscriberPhoneFollowsWan"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipMediaProfileIndex"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipSubscriberImpedance"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipSubscriberRxGain"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipSubscriberTxGain"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipSubscriberTransmissionPath"),
        ("Zhone-CPE-MIB", "zhoneCpeVoipSubscriberSignallingCode"))
)
if mibBuilder.loadTexts:
    zhoneCpeVoipSubscriberGroup.setStatus("current")

zhoneCpeEthSubscriberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 43)
)
zhoneCpeEthSubscriberGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeEthSubscriberRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeEthSubscriberAdminState"),
        ("Zhone-CPE-MIB", "zhoneCpeEthSubscriberLoopback"),
        ("Zhone-CPE-MIB", "zhoneCpeTrafficManagementProfileIndex"),
        ("Zhone-CPE-MIB", "zhoneCpeEthSubscriberLineStatusAlarm"),
        ("Zhone-CPE-MIB", "zhoneCpeEthSubscriberAlarmSeverity"),
        ("Zhone-CPE-MIB", "zhoneCpeEthSubscriberPowerRange"),
        ("Zhone-CPE-MIB", "zhoneCpeEthSubscriberPowerShed"),
        ("Zhone-CPE-MIB", "zhoneCpeEthSubscriberLldpMedList"),
        ("Zhone-CPE-MIB", "zhoneCpeVideoProfileIndex"),
        ("Zhone-CPE-MIB", "zhoneCpeEthSubscriberRate"),
        ("Zhone-CPE-MIB", "zhoneCpeEthSubscriberDuplex"),
        ("Zhone-CPE-MIB", "zhoneCpeEthSubscriberMtu"),
        ("Zhone-CPE-MIB", "zhoneCpeEthSubscriberPortType"),
        ("Zhone-CPE-MIB", "zhoneCpeEthSubscriberPauseTime"),
        ("Zhone-CPE-MIB", "zhoneCpeEthSubscriberMode"),
        ("Zhone-CPE-MIB", "zhoneCpeEthSubscriberPowerFeed"))
)
if mibBuilder.loadTexts:
    zhoneCpeEthSubscriberGroup.setStatus("current")

zhoneCpeVideoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 44)
)
zhoneCpeVideoGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeVideoRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeVideoProfileName"),
        ("Zhone-CPE-MIB", "zhoneCpeVideoMaxSimultaneousGroups"),
        ("Zhone-CPE-MIB", "zhoneCpeVideoMaxMulticastBandwidth"),
        ("Zhone-CPE-MIB", "zhoneCpeVideoBandwidthEnforce"),
        ("Zhone-CPE-MIB", "zhoneCpeVideoIgmpVersion"),
        ("Zhone-CPE-MIB", "zhoneCpeVideoIgmpFunction"),
        ("Zhone-CPE-MIB", "zhoneCpeVideoImmediateLeave"),
        ("Zhone-CPE-MIB", "zhoneCpeVideoUpstreamIgmpRate"),
        ("Zhone-CPE-MIB", "zhoneCpeVideoRobustness"),
        ("Zhone-CPE-MIB", "zhoneCpeVideoAccessControlList"),
        ("Zhone-CPE-MIB", "zhoneCpeVideoIndexNext"))
)
if mibBuilder.loadTexts:
    zhoneCpeVideoGroup.setStatus("current")

zhoneCpeVideoAccessControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 45)
)
zhoneCpeVideoAccessControlGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeVideoAccessControlRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeVideoAccessControlProfileName"),
        ("Zhone-CPE-MIB", "zhoneCpeVideoAccessControlType"),
        ("Zhone-CPE-MIB", "zhoneCpeVideoAccessControlSrcIp"),
        ("Zhone-CPE-MIB", "zhoneCpeVideoAccessControlDstIpStart"),
        ("Zhone-CPE-MIB", "zhoneCpeVideoAccessControlDstIpEnd"),
        ("Zhone-CPE-MIB", "zhoneCpeVideoAccessControlImputedGroupBw"),
        ("Zhone-CPE-MIB", "zhoneCpeVideoAccessControlIndexNext"))
)
if mibBuilder.loadTexts:
    zhoneCpeVideoAccessControlGroup.setStatus("current")

zhoneCpePweSubscriberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 46)
)
zhoneCpePweSubscriberGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpePweSubscriberRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpePweSubscriberAdminState"),
        ("Zhone-CPE-MIB", "zhoneCpePweSubscriberLoopback"),
        ("Zhone-CPE-MIB", "zhoneCpePweSubscriberNearEndPort"),
        ("Zhone-CPE-MIB", "zhoneCpePweSubscriberFarEndIp"),
        ("Zhone-CPE-MIB", "zhoneCpePweSubscriberFarEndPort"),
        ("Zhone-CPE-MIB", "zhoneCpePweSubscriberAlarmSeverity"),
        ("Zhone-CPE-MIB", "zhoneCpePweSubscriberLineStatusAlarm"),
        ("Zhone-CPE-MIB", "zhoneCpePweProfileIndex"),
        ("Zhone-CPE-MIB", "zhoneCpePweSubscriberLineLength"))
)
if mibBuilder.loadTexts:
    zhoneCpePweSubscriberGroup.setStatus("current")

zhoneCpePweGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 47)
)
zhoneCpePweGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpePweRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpePweProfileName"),
        ("Zhone-CPE-MIB", "zhoneCpePweTransport"),
        ("Zhone-CPE-MIB", "zhoneCpePweServiceType"),
        ("Zhone-CPE-MIB", "zhoneCpePwePayloadSize"),
        ("Zhone-CPE-MIB", "zhoneCpePwePayloadEncapsulationDelay"),
        ("Zhone-CPE-MIB", "zhoneCpePweTimingMode"),
        ("Zhone-CPE-MIB", "zhoneCpePweChannelAssign"),
        ("Zhone-CPE-MIB", "zhoneCpePweClockReference"),
        ("Zhone-CPE-MIB", "zhoneCpePweRtpTimeStampMode"),
        ("Zhone-CPE-MIB", "zhoneCpePweJitterBufMax"),
        ("Zhone-CPE-MIB", "zhoneCpePweJitterBufDesired"),
        ("Zhone-CPE-MIB", "zhoneCpePweFillPolicy"),
        ("Zhone-CPE-MIB", "zhoneCpePweMisconnectedDeclarePolicy"),
        ("Zhone-CPE-MIB", "zhoneCpePweMisconnectedClearPolicy"),
        ("Zhone-CPE-MIB", "zhoneCpePweLossPacketDeclarePolicy"),
        ("Zhone-CPE-MIB", "zhoneCpePweOverrunUnderrunDeclarePolicy"),
        ("Zhone-CPE-MIB", "zhoneCpePweOverrunUnderrunClearPolicy"),
        ("Zhone-CPE-MIB", "zhoneCpePweMalformedDeclarePolicy"),
        ("Zhone-CPE-MIB", "zhoneCpePweMalformedClearPolicy"),
        ("Zhone-CPE-MIB", "zhoneCpePweRBitTransmitSetPolicy"),
        ("Zhone-CPE-MIB", "zhoneCpePweRBitTransmitClearPolicy"),
        ("Zhone-CPE-MIB", "zhoneCpePweRBitReceivePolicy"),
        ("Zhone-CPE-MIB", "zhoneCpePweLBitReceivePolicy"),
        ("Zhone-CPE-MIB", "zhoneCpePweSesThreshold"),
        ("Zhone-CPE-MIB", "zhoneCpePweCdvTolerance"),
        ("Zhone-CPE-MIB", "zhoneCpePweChannelAssociatedSignalling"),
        ("Zhone-CPE-MIB", "zhoneCpePweMplsTpType"),
        ("Zhone-CPE-MIB", "zhoneCpePweSSrcPayload"),
        ("Zhone-CPE-MIB", "zhoneCpePweSSrcSignalling"),
        ("Zhone-CPE-MIB", "zhoneCpePweExpectedSSrcPayload"),
        ("Zhone-CPE-MIB", "zhoneCpePweExpectedSSrcSignalling"),
        ("Zhone-CPE-MIB", "zhoneCpePwePtypePayload"),
        ("Zhone-CPE-MIB", "zhoneCpePwePtypeSignalling"),
        ("Zhone-CPE-MIB", "zhoneCpePweExpectedPTypePayload"),
        ("Zhone-CPE-MIB", "zhoneCpePweDs1Framing"),
        ("Zhone-CPE-MIB", "zhoneCpePweDs1Mode"),
        ("Zhone-CPE-MIB", "zhoneCpePweEncoding"),
        ("Zhone-CPE-MIB", "zhoneCpePweLineType"),
        ("Zhone-CPE-MIB", "zhoneCpePweIndexNext"),
        ("Zhone-CPE-MIB", "zhoneCpePweExpectedPTypeSignalling"),
        ("Zhone-CPE-MIB", "zhoneCpePweSignalling"),
        ("Zhone-CPE-MIB", "zhoneCpePweLossPacketClearPolicy"),
        ("Zhone-CPE-MIB", "zhoneCpePweDscp"))
)
if mibBuilder.loadTexts:
    zhoneCpePweGroup.setStatus("current")

zhoneCpeOnuModelInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 48)
)
zhoneCpeOnuModelInfoGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeOnuModelName"),
        ("Zhone-CPE-MIB", "zhoneCpeOnuBatteryBackup"),
        ("Zhone-CPE-MIB", "zhoneCpeOnuSipPlarSupported"),
        ("Zhone-CPE-MIB", "zhoneCpeOnuEthSlotNumber"),
        ("Zhone-CPE-MIB", "zhoneCpeOnuNumberOfEthPorts"),
        ("Zhone-CPE-MIB", "zhoneCpeOnuPotsSlotNumber"),
        ("Zhone-CPE-MIB", "zhoneCpeOnuNumberOfPotsPorts"),
        ("Zhone-CPE-MIB", "zhoneCpeOnuRfVideoSlotNumber"),
        ("Zhone-CPE-MIB", "zhoneCpeOnuNumberOfRfVideoPorts"),
        ("Zhone-CPE-MIB", "zhoneCpeOnuCesSlotNumber"),
        ("Zhone-CPE-MIB", "zhoneCpeOnuNumberOfCesPorts"),
        ("Zhone-CPE-MIB", "zhoneCpeOnuModelInfoRGBridged"),
        ("Zhone-CPE-MIB", "zhoneCpeOnuNumberOfWlanPorts"),
        ("Zhone-CPE-MIB", "zhoneCpeOnuModelInfoRg"),
        ("Zhone-CPE-MIB", "zhoneCpeOnuModelInfoRgVoip"),
        ("Zhone-CPE-MIB", "zhoneCpeOnuModelInfoRgPwe"),
        ("Zhone-CPE-MIB", "zhoneCpeOnuModelInfoTftpDnld"),
        ("Zhone-CPE-MIB", "zhoneCpeOnuSipSupported"),
        ("Zhone-CPE-MIB", "zhoneCpeOnuH248Supported"),
        ("Zhone-CPE-MIB", "zhoneCpeOnuMgcpSupported"),
        ("Zhone-CPE-MIB", "zhoneCpeOnuT1Supported"),
        ("Zhone-CPE-MIB", "zhoneCpeOnuE1Supported"),
        ("Zhone-CPE-MIB", "zhoneCpeOnuNumberOfPoEPorts"))
)
if mibBuilder.loadTexts:
    zhoneCpeOnuModelInfoGroup.setStatus("current")

zhoneCpeConnectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 49)
)
zhoneCpeConnectionGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeConnectionRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeConnectionVlanCos"),
        ("Zhone-CPE-MIB", "zhoneCpeConnectionSlanCos"),
        ("Zhone-CPE-MIB", "zhoneCpeConnectionVlanTpId"),
        ("Zhone-CPE-MIB", "zhoneCpeConnectionSlanTpId"),
        ("Zhone-CPE-MIB", "zhoneCpeConnectionTranslateVlanId"),
        ("Zhone-CPE-MIB", "zhoneCpeConnectionTranslateVlanCos"),
        ("Zhone-CPE-MIB", "zhoneCpeConnectionTranslateVlanTpId"),
        ("Zhone-CPE-MIB", "zhoneCpeConnectionTranslateSlanId"),
        ("Zhone-CPE-MIB", "zhoneCpeConnectionTranslateSlanCos"),
        ("Zhone-CPE-MIB", "zhoneCpeConnectionFloodingGport"),
        ("Zhone-CPE-MIB", "zhoneCpeConnectionDscpToCosProfileIndex"),
        ("Zhone-CPE-MIB", "zhoneCpeConnectionRgMode"),
        ("Zhone-CPE-MIB", "zhoneCpeConnectionGuidedCos"),
        ("Zhone-CPE-MIB", "zhoneCpeConnectionGuidedVlanId"),
        ("Zhone-CPE-MIB", "zhoneCpeConnectionVideoGport"),
        ("Zhone-CPE-MIB", "zhoneCpeConnectionTranslateSlanTpId"))
)
if mibBuilder.loadTexts:
    zhoneCpeConnectionGroup.setStatus("current")

zhoneCpeRfSubscriberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 50)
)
zhoneCpeRfSubscriberGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeRfSubscriberRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeRfSubscriberAdminState"),
        ("Zhone-CPE-MIB", "zhoneCpeRfSubscriberLineStatusAlarm"),
        ("Zhone-CPE-MIB", "zhoneCpeRfSubscriberAlarmSeverity"))
)
if mibBuilder.loadTexts:
    zhoneCpeRfSubscriberGroup.setStatus("current")

zhoneCpeTrafficManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 51)
)
zhoneCpeTrafficManagementGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeTrafficManagementProfileName"),
        ("Zhone-CPE-MIB", "zhoneCpeTrafficManagementUpstreamSIR"),
        ("Zhone-CPE-MIB", "zhoneCpeTrafficManagementUpstreamPIR"),
        ("Zhone-CPE-MIB", "zhoneCpeTrafficManagementUpstreamPriority"),
        ("Zhone-CPE-MIB", "zhoneCpeTrafficManagementUpstreamWeight"),
        ("Zhone-CPE-MIB", "zhoneCpeTrafficManagementDownstreamSIR"),
        ("Zhone-CPE-MIB", "zhoneCpeTrafficManagementDownstreamPIR"),
        ("Zhone-CPE-MIB", "zhoneCpeTrafficManagementDownstreamPriority"),
        ("Zhone-CPE-MIB", "zhoneCpeTrafficManagementPeakBurstSize"),
        ("Zhone-CPE-MIB", "zhoneCpeTrafficManagementDownstreamWeight"),
        ("Zhone-CPE-MIB", "zhoneCpeTrafficManagementIndexNext"),
        ("Zhone-CPE-MIB", "zhoneCpeTrafficManagementRowStatus"))
)
if mibBuilder.loadTexts:
    zhoneCpeTrafficManagementGroup.setStatus("current")

zhoneCpeSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 53)
)
zhoneCpeSystemGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeSystemRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeSystemCommonProfileIndex"),
        ("Zhone-CPE-MIB", "zhoneCpeSystemMgcpClientName"))
)
if mibBuilder.loadTexts:
    zhoneCpeSystemGroup.setStatus("current")

zhoneCpeSystemCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 54)
)
zhoneCpeSystemCommonGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeSystemCommonProfileIndex"),
        ("Zhone-CPE-MIB", "zhoneCpeSystemCommonIndexNext"),
        ("Zhone-CPE-MIB", "zhoneCpeSystemCommonRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeSystemCommonProfileName"),
        ("Zhone-CPE-MIB", "zhoneCpeSystemCommonFirewall"),
        ("Zhone-CPE-MIB", "zhoneCpeSystemCommonSyncCookieProtection"),
        ("Zhone-CPE-MIB", "zhoneCpeSystemCommonCrossVlanRouting"),
        ("Zhone-CPE-MIB", "zhoneCpeStaticRouteListProfileIndex"),
        ("Zhone-CPE-MIB", "zhoneCpeSystemCommonTr69Inform"),
        ("Zhone-CPE-MIB", "zhoneCpeSystemCommonInformInterval"),
        ("Zhone-CPE-MIB", "zhoneCpeSystemCommonAcsUrl"),
        ("Zhone-CPE-MIB", "zhoneCpeSystemCommonAcsUsername"),
        ("Zhone-CPE-MIB", "zhoneCpeSystemCommonUserPassword"),
        ("Zhone-CPE-MIB", "zhoneCpeSystemCommonSupportPassword"),
        ("Zhone-CPE-MIB", "zhoneCpeSystemCommonAdminPassword"),
        ("Zhone-CPE-MIB", "zhoneCpeSystemCommonPowerRestoreDelay"),
        ("Zhone-CPE-MIB", "zhoneCpeSystemCommonPowerShutdownDelay"),
        ("Zhone-CPE-MIB", "zhoneCpeSystemCommonPowerSupply"),
        ("Zhone-CPE-MIB", "zhoneCpeSystemCommonAcsPassword"),
        ("Zhone-CPE-MIB", "zhoneCpeDnsHostListProfile"))
)
if mibBuilder.loadTexts:
    zhoneCpeSystemCommonGroup.setStatus("current")

zhoneCpeInterfaceVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 55)
)
zhoneCpeInterfaceVlanGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeInterfaceVlanRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeIpServerProfile"),
        ("Zhone-CPE-MIB", "zhoneCpeDhcpServerProfileIndex"),
        ("Zhone-CPE-MIB", "zhoneCpeInterfaceVlanRgMode"),
        ("Zhone-CPE-MIB", "zhoneCpeInterfaceVlanTranslateVlanId"),
        ("Zhone-CPE-MIB", "zhoneCpeInterfaceVlanTranslateVlanCos"),
        ("Zhone-CPE-MIB", "zhoneCpeInterfaceVlanTranslateSlanId"),
        ("Zhone-CPE-MIB", "zhoneCpeInterfaceVlanTranslateSlanCos"),
        ("Zhone-CPE-MIB", "zhoneCpeInterfaceVlanTranslateSlanTpId"),
        ("Zhone-CPE-MIB", "zhoneCpeInterfaceVlanIpAddress"),
        ("Zhone-CPE-MIB", "zhoneCpePortFwdListProfileIndex"))
)
if mibBuilder.loadTexts:
    zhoneCpeInterfaceVlanGroup.setStatus("current")

zhoneCpeDhcpServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 56)
)
zhoneCpeDhcpServerGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeDhcpServerIndexNext"),
        ("Zhone-CPE-MIB", "zhoneCpeDhcpServerRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeDhcpServerProfileName"),
        ("Zhone-CPE-MIB", "zhoneCpeDhcpServerStartAddress"),
        ("Zhone-CPE-MIB", "zhoneCpeDhcpServerEndAddress"),
        ("Zhone-CPE-MIB", "zhoneCpeDhcpServerLeaseTime"),
        ("Zhone-CPE-MIB", "zhoneCpeDhcpServerConditionalServerListProfile"))
)
if mibBuilder.loadTexts:
    zhoneCpeDhcpServerGroup.setStatus("current")

zhoneCpePppoeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 57)
)
zhoneCpePppoeGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpePppoeRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpePppoeUsername"),
        ("Zhone-CPE-MIB", "zhoneCpePppoePassword"),
        ("Zhone-CPE-MIB", "zhoneCpePppoeAuthentication"),
        ("Zhone-CPE-MIB", "zhoneCpePppoeRetryInterval"))
)
if mibBuilder.loadTexts:
    zhoneCpePppoeGroup.setStatus("current")

zhoneCpeWlanSubscriberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 58)
)
zhoneCpeWlanSubscriberGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeWlanSubscriberRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanSubscriberAdminState"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanSubscriberSsid"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanSubscriberEncryptKey"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanSubscriberDevicePin"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanSubscriberRadiusKey"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanProfileIndex"),
        ("Zhone-CPE-MIB", "zhoneCpeAccessControlListProfileIndex"),
        ("Zhone-CPE-MIB", "zhoneCpeWdsMacListProfileIndex"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvProfileIndex"))
)
if mibBuilder.loadTexts:
    zhoneCpeWlanSubscriberGroup.setStatus("current")

zhoneCpeWlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 59)
)
zhoneCpeWlanGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeWlanIndexNext"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanProfileName"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanHideAccessPoint"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanIsolateClients"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanWmmAdvertise"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanMcastFwd"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanMaxClients"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanNetAuthentication"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanWpaGroupRekeyInterval"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanWpaEncryption"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanWepEncryption"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanWepStrength"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanRadiusServerIp"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanRadiusPort"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanWpa2PreAuthentication"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanNetReAuthenticationInterval"))
)
if mibBuilder.loadTexts:
    zhoneCpeWlanGroup.setStatus("current")

zhoneCpeStaticRouteListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 60)
)
zhoneCpeStaticRouteListGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeStaticRouteListIndexNext"),
        ("Zhone-CPE-MIB", "zhoneCpeStaticRouteListRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeStaticRouteListProfileName"))
)
if mibBuilder.loadTexts:
    zhoneCpeStaticRouteListGroup.setStatus("current")

zhoneCpeStaticRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 61)
)
zhoneCpeStaticRouteGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeStaticRouteRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeStaticRouteDestinationIp"),
        ("Zhone-CPE-MIB", "zhoneCpeStaticRouteNetmask"),
        ("Zhone-CPE-MIB", "zhoneCpeStaticRouteGateway"),
        ("Zhone-CPE-MIB", "zhoneCpeStaticRouteMetric"),
        ("Zhone-CPE-MIB", "zhoneCpeStaticRouteEntryIndexNext"))
)
if mibBuilder.loadTexts:
    zhoneCpeStaticRouteGroup.setStatus("current")

zhoneCpePortFwdListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 62)
)
zhoneCpePortFwdListGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpePortFwdListIndexNext"),
        ("Zhone-CPE-MIB", "zhoneCpePortFwdListRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpePortFwdListProfileName"))
)
if mibBuilder.loadTexts:
    zhoneCpePortFwdListGroup.setStatus("current")

zhoneCpePortFwdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 63)
)
zhoneCpePortFwdGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpePortFwdRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpePortFwdType"),
        ("Zhone-CPE-MIB", "zhoneCpePortFwdPortStart"),
        ("Zhone-CPE-MIB", "zhoneCpePortFwdPortEnd"),
        ("Zhone-CPE-MIB", "zhoneCpePortFwdProtocol"),
        ("Zhone-CPE-MIB", "zhoneCpePortFwdPrivatePort"),
        ("Zhone-CPE-MIB", "zhoneCpePortFwdPrivateIp"),
        ("Zhone-CPE-MIB", "zhoneCpePortFwdEntryIndexNext"))
)
if mibBuilder.loadTexts:
    zhoneCpePortFwdGroup.setStatus("current")

zhoneCpeServiceApplicationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 64)
)
zhoneCpeServiceApplicationGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeServiceApplicationTemplateType"),
        ("Zhone-CPE-MIB", "zhoneCpeServiceApplicationTemplateId"),
        ("Zhone-CPE-MIB", "zhoneCpeServiceApplicationVirtualConnection"),
        ("Zhone-CPE-MIB", "zhoneCpeServiceApplicationTpType"),
        ("Zhone-CPE-MIB", "zhoneCpeServiceApplicationTpIndex"),
        ("Zhone-CPE-MIB", "zhoneCpeServiceApplicationRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeServiceApplicationVlan"),
        ("Zhone-CPE-MIB", "zhoneCpeServiceApplicationSlan"))
)
if mibBuilder.loadTexts:
    zhoneCpeServiceApplicationGroup.setStatus("current")

zhoneCpeDnsHostListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 65)
)
zhoneCpeDnsHostListGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeDnsHostListIndexNext"),
        ("Zhone-CPE-MIB", "zhoneCpeDnsHostListRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeDnsHostListProfileName"))
)
if mibBuilder.loadTexts:
    zhoneCpeDnsHostListGroup.setStatus("current")

zhoneCpeDnsHostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 66)
)
zhoneCpeDnsHostGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeDnsHostIndexEntryIndexNext"),
        ("Zhone-CPE-MIB", "zhoneCpeDnsHostRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeDnsHostDomainName"),
        ("Zhone-CPE-MIB", "zhoneCpeDnsHostIpAddress"))
)
if mibBuilder.loadTexts:
    zhoneCpeDnsHostGroup.setStatus("current")

zhoneCpeWlanAdvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 67)
)
zhoneCpeWlanAdvGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeWlanAdvRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvProfileName"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvChannel"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvAutoChanTimer"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvDot11nMode"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvDot11nRate"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvDot1nProtection"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvDot1nClientOnly"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvRate54G"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvMcastRate"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvBasicRate"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvFragmentationThreshold"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvRtsThreshold"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvDtimInterval"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvBeaconInterval"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvGlobalMaxClients"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvXpressTechnology"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvTxPower"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvWmm"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvWmmNoAck"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvWmmApsd"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvApMode"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvBridgeRestrict"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvWps"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvWpsAddClientMethod"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvWpsApMode"),
        ("Zhone-CPE-MIB", "zhoneCpeWlanAdvIndexNext"))
)
if mibBuilder.loadTexts:
    zhoneCpeWlanAdvGroup.setStatus("current")

zhoneCpeCondDhcpSrvListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 68)
)
zhoneCpeCondDhcpSrvListGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeCondDhcpSrvListProfileName"),
        ("Zhone-CPE-MIB", "zhoneCpeCondDhcpSrvIndexEntryIndexNext"),
        ("Zhone-CPE-MIB", "zhoneCpeCondiDhcpSrvListIndexNext"),
        ("Zhone-CPE-MIB", "zhoneCpeCondDhcpSrvListRowStatus"))
)
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvListGroup.setStatus("current")

zhoneCpeCondDhcpSrvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 69)
)
zhoneCpeCondDhcpSrvGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeCondDhcpSrvAdminState"),
        ("Zhone-CPE-MIB", "zhoneCpeCondDhcpSrvPriorityOrder"),
        ("Zhone-CPE-MIB", "zhoneCpeCondDhcpVciOui"),
        ("Zhone-CPE-MIB", "zhoneCpeCondDhcpSrvVciMatch"),
        ("Zhone-CPE-MIB", "zhoneCpeCondDhcpSrvStartAddr"),
        ("Zhone-CPE-MIB", "zhoneCpeCondDhcpSrvEndAddr"),
        ("Zhone-CPE-MIB", "zhoneCpeCondDhcpSrvWanVlan"),
        ("Zhone-CPE-MIB", "zhoneCpeCondDhcpSrvPortFwdRule"),
        ("Zhone-CPE-MIB", "zhoneCpeCondDhcpSrvStartPort"),
        ("Zhone-CPE-MIB", "zhoneCpeCondDhcpSrvPrivatePort"),
        ("Zhone-CPE-MIB", "zhoneCpeCondDhcpSrvProtocol"),
        ("Zhone-CPE-MIB", "zhoneCpeCondDhcpSrvPriDns"),
        ("Zhone-CPE-MIB", "zhoneCpeCondDhcpSrvSecDns"),
        ("Zhone-CPE-MIB", "zhoneCpeCondDhcpSrvPriNpt"),
        ("Zhone-CPE-MIB", "zhoneCpeCondDhcpSrvSecNpt"),
        ("Zhone-CPE-MIB", "zhoneCpeCondDhcpSrvPermanent"),
        ("Zhone-CPE-MIB", "zhoneCpeCondDhcpSrvVsi"),
        ("Zhone-CPE-MIB", "zhoneCpeCondDhcpSrvRowStatus"))
)
if mibBuilder.loadTexts:
    zhoneCpeCondDhcpSrvGroup.setStatus("current")

zhoneCpeCmdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 70)
)
zhoneCpeCmdGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeCmdOperation"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdSrcIfIndex"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdSrcShelf"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdSrcSlot"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdSrcPort"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdSrcSubport"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdSrcTpType"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdSrcTpIndex"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdDstIfIndex"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdDstShelf"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdDstSlot"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdDstPort"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdDstSubport"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdDstTpType"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdDstTpIndex"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdString"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdSvcTemplateType"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdSvcTemplateId"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdSvcTemplateIfIndex"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdSvcTemplateVirtualConn"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdSvcTemplateTpType"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdSvcTemplateTpIndex"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdSvcTemplateVlan"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdSvcTemplateSlan"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdOverrideTpIndex"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdOverrideVlanId"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdOverrideVlanCos"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdOverrideSlanId"),
        ("Zhone-CPE-MIB", "zhoneCpeCmdOverrideSlanCos"))
)
if mibBuilder.loadTexts:
    zhoneCpeCmdGroup.setStatus("current")

zhoneCpeLldpMedPolicyListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 71)
)
zhoneCpeLldpMedPolicyListGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeLldpMedPolicyListIndexNext"),
        ("Zhone-CPE-MIB", "zhoneCpeLldpMedPolicyListRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeLldpMedPolicyListProfileName"))
)
if mibBuilder.loadTexts:
    zhoneCpeLldpMedPolicyListGroup.setStatus("current")

zhoneCpeLldpMedPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 72)
)
zhoneCpeLldpMedPolicyGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeLldpMedPolicyIndexEntryIndexNext"),
        ("Zhone-CPE-MIB", "zhoneCpeLldpMedPolicyRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeLldpMedPolicyAdminState"),
        ("Zhone-CPE-MIB", "zhoneCpeLldpMedPolicyAppType"),
        ("Zhone-CPE-MIB", "zhoneCpeLldpMedPolicyVlanId"),
        ("Zhone-CPE-MIB", "zhoneCpeLldpMedPolicyCos"),
        ("Zhone-CPE-MIB", "zhoneCpeLldpMedPolicyDscp"))
)
if mibBuilder.loadTexts:
    zhoneCpeLldpMedPolicyGroup.setStatus("current")

zhoneCpeAutoCfgRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 73)
)
zhoneCpeAutoCfgRuleGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeAutoCfgRuleAdminState"),
        ("Zhone-CPE-MIB", "zhoneCpeAutoCfgRulePriority"),
        ("Zhone-CPE-MIB", "zhoneCpeAutoCfgRuleMatchExpression"),
        ("Zhone-CPE-MIB", "zhoneCpeAutoCfgRuleTargetUni"),
        ("Zhone-CPE-MIB", "zhoneCpeAutoCfgRuleDeleteBeforeApply"),
        ("Zhone-CPE-MIB", "zhoneCpeAutoCfgRuleRowStatus"),
        ("Zhone-CPE-MIB", "zhoneCpeAutoCfgRuleProfileName"),
        ("Zhone-CPE-MIB", "zhoneCpeAutoCfgRuleServiceTemplate"),
        ("Zhone-CPE-MIB", "zhoneCpeAutoCfgRuleIndexNext"))
)
if mibBuilder.loadTexts:
    zhoneCpeAutoCfgRuleGroup.setStatus("current")

zhoneCpeCfgGlobalSettingsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 74)
)
zhoneCpeCfgGlobalSettingsGroup.setObjects(
      *(("Zhone-CPE-MIB", "zhoneCpeCfgAutoAssign"),
        ("Zhone-CPE-MIB", "zhoneCpeCfgAutoConfig"),
        ("Zhone-CPE-MIB", "zhoneCpeCfgParamsStr"))
)
if mibBuilder.loadTexts:
    zhoneCpeCfgGlobalSettingsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Zhone-CPE-MIB",
    **{"TpType": TpType,
       "ZhoneCpeTemplateType": ZhoneCpeTemplateType,
       "zhoneCpeObjectID": zhoneCpeObjectID,
       "zhoneCpeSipDialPlan": zhoneCpeSipDialPlan,
       "zhoneCpeSipDialPlanIndexTable": zhoneCpeSipDialPlanIndexTable,
       "zhoneCpeSipDialPlanIndexEntry": zhoneCpeSipDialPlanIndexEntry,
       "zhoneCpeSipDialPlanIndexNext": zhoneCpeSipDialPlanIndexNext,
       "zhoneCpeSipDialPlanTable": zhoneCpeSipDialPlanTable,
       "zhoneCpeSipDialPlanEntry": zhoneCpeSipDialPlanEntry,
       "zhoneCpeSipServerIndex": zhoneCpeSipServerIndex,
       "zhoneCpeSipDialPlanIndex": zhoneCpeSipDialPlanIndex,
       "zhoneCpeSipDialPlanRowStatus": zhoneCpeSipDialPlanRowStatus,
       "zhoneCpeSipDialPlanFormat": zhoneCpeSipDialPlanFormat,
       "zhoneCpeSipDialPlanString": zhoneCpeSipDialPlanString,
       "zhoneCpeVoipServer": zhoneCpeVoipServer,
       "zhoneCpeVoipServerIndexNext": zhoneCpeVoipServerIndexNext,
       "zhoneCpeVoipServerTable": zhoneCpeVoipServerTable,
       "zhoneCpeVoipServerEntry": zhoneCpeVoipServerEntry,
       "zhoneCpeVoipServerIndex": zhoneCpeVoipServerIndex,
       "zhoneCpeVoipServerRowStatus": zhoneCpeVoipServerRowStatus,
       "zhoneCpeVoipProfileName": zhoneCpeVoipProfileName,
       "zhoneCpeVoipPrimaryServer": zhoneCpeVoipPrimaryServer,
       "zhoneCpeVoipSecondaryServer": zhoneCpeVoipSecondaryServer,
       "zhoneCpeVoipServerSignallingProtocol": zhoneCpeVoipServerSignallingProtocol,
       "zhoneCpeVoipSipRegExpirationTime": zhoneCpeVoipSipRegExpirationTime,
       "zhoneCpeVoipSipReRegHeadStartTime": zhoneCpeVoipSipReRegHeadStartTime,
       "zhoneCpeVoipSipDomain": zhoneCpeVoipSipDomain,
       "zhoneCpeVoipSipRegistrar": zhoneCpeVoipSipRegistrar,
       "zhoneCpeVoipSoftSwitch": zhoneCpeVoipSoftSwitch,
       "zhoneCpeVoipMgcVersion": zhoneCpeVoipMgcVersion,
       "zhoneCpeVoipMgcMessageFormat": zhoneCpeVoipMgcMessageFormat,
       "zhoneCpeVoipMgcMaximumRetryTime": zhoneCpeVoipMgcMaximumRetryTime,
       "zhoneCpeVoipMgcMaximumRetryAttempts": zhoneCpeVoipMgcMaximumRetryAttempts,
       "zhoneCpeVoipMgcServiceChangeDelay": zhoneCpeVoipMgcServiceChangeDelay,
       "zhoneCpeVoipMgcTerminationIdBase": zhoneCpeVoipMgcTerminationIdBase,
       "zhoneCpeVoipReleaseTimer": zhoneCpeVoipReleaseTimer,
       "zhoneCpeVoipRohTimer": zhoneCpeVoipRohTimer,
       "zhoneCpeVoipDscpMark": zhoneCpeVoipDscpMark,
       "zhoneCpeVoipPiggyBackEvents": zhoneCpeVoipPiggyBackEvents,
       "zhoneCpeVoipOobToneEvents": zhoneCpeVoipOobToneEvents,
       "zhoneCpeVoipOobDtmfEvents": zhoneCpeVoipOobDtmfEvents,
       "zhoneCpeVoipOobCasEvents": zhoneCpeVoipOobCasEvents,
       "zhoneCpeVoipPartialDialTimeout": zhoneCpeVoipPartialDialTimeout,
       "zhoneCpeVoipCriticalDialTimeout": zhoneCpeVoipCriticalDialTimeout,
       "zhoneCpeVoipServerOutboundServer": zhoneCpeVoipServerOutboundServer,
       "zhoneCpeVoipServerPortId": zhoneCpeVoipServerPortId,
       "zhoneCpeVoipDtmfEventsPassingMethod": zhoneCpeVoipDtmfEventsPassingMethod,
       "zhoneCpeVoipCasEventsPassingMethod": zhoneCpeVoipCasEventsPassingMethod,
       "zhoneCpeVoipRtpDscp": zhoneCpeVoipRtpDscp,
       "zhoneCpeVoipSignalingDscp": zhoneCpeVoipSignalingDscp,
       "zhoneCpeVoipSipRegRetryTime": zhoneCpeVoipSipRegRetryTime,
       "zhoneCpeVoipMgcpClientAddressMode": zhoneCpeVoipMgcpClientAddressMode,
       "zhoneCpeVoipMgcpPersistentNotify": zhoneCpeVoipMgcpPersistentNotify,
       "zhoneCpeIpTable": zhoneCpeIpTable,
       "zhoneCpeIpEntry": zhoneCpeIpEntry,
       "zhoneCpeIfIndex": zhoneCpeIfIndex,
       "zhoneCpeIpServiceType": zhoneCpeIpServiceType,
       "zhoneCpeIpRowStatus": zhoneCpeIpRowStatus,
       "zhoneCpeHostIp": zhoneCpeHostIp,
       "zhoneCpeIpServerProfileIndex": zhoneCpeIpServerProfileIndex,
       "zhoneCpeIpServer": zhoneCpeIpServer,
       "zhoneCpeIpServerIndexNext": zhoneCpeIpServerIndexNext,
       "zhoneCpeIpServerTable": zhoneCpeIpServerTable,
       "zhoneCpeIpServerEntry": zhoneCpeIpServerEntry,
       "zhoneCpeIpServerIndex": zhoneCpeIpServerIndex,
       "zhoneCpeIpServerRowStatus": zhoneCpeIpServerRowStatus,
       "zhoneCpeIpServerProfileName": zhoneCpeIpServerProfileName,
       "zhoneCpeIpServerHostIpOption": zhoneCpeIpServerHostIpOption,
       "zhoneCpeIpServerNetmask": zhoneCpeIpServerNetmask,
       "zhoneCpeIpServerGateway": zhoneCpeIpServerGateway,
       "zhoneCpeIpServerPrimaryDns": zhoneCpeIpServerPrimaryDns,
       "zhoneCpeIpServerSecondaryDns": zhoneCpeIpServerSecondaryDns,
       "zhoneCpeIpServerFirewallAccess": zhoneCpeIpServerFirewallAccess,
       "zhoneCpeIpServerNat": zhoneCpeIpServerNat,
       "zhoneCpeIpServerSecureForward": zhoneCpeIpServerSecureForward,
       "zhoneCpeIpServerIgmpFunction": zhoneCpeIpServerIgmpFunction,
       "zhoneCpeIpServerDefaultIface": zhoneCpeIpServerDefaultIface,
       "zhoneCpeIpServerDnsSrc": zhoneCpeIpServerDnsSrc,
       "zhoneCpeIpServerDnsType": zhoneCpeIpServerDnsType,
       "zhoneCpeVoipFeatures": zhoneCpeVoipFeatures,
       "zhoneCpeVoipFeaturesIndexNext": zhoneCpeVoipFeaturesIndexNext,
       "zhoneCpeVoipFeaturesTable": zhoneCpeVoipFeaturesTable,
       "zhoneCpeVoipFeaturesEntry": zhoneCpeVoipFeaturesEntry,
       "zhoneCpeVoipFeaturesIndex": zhoneCpeVoipFeaturesIndex,
       "zhoneCpeVoipFeaturesRowStatus": zhoneCpeVoipFeaturesRowStatus,
       "zhoneCpeVoipFeaturesProfileName": zhoneCpeVoipFeaturesProfileName,
       "zhoneCpeVoipFeaturesAnnouncementType": zhoneCpeVoipFeaturesAnnouncementType,
       "zhoneCpeVoipCidFeatures": zhoneCpeVoipCidFeatures,
       "zhoneCpeVoipCallWaitingFeatures": zhoneCpeVoipCallWaitingFeatures,
       "zhoneCpeVoipCallProgressOrTransferFeatures": zhoneCpeVoipCallProgressOrTransferFeatures,
       "zhoneCpeVoipCallPresentationFeatures": zhoneCpeVoipCallPresentationFeatures,
       "zhoneCpeVoipFeaturesHotLine": zhoneCpeVoipFeaturesHotLine,
       "zhoneCpeVoipFeaturesHotLineNumber": zhoneCpeVoipFeaturesHotLineNumber,
       "zhoneCpeVoipFeaturesWarmLineTimer": zhoneCpeVoipFeaturesWarmLineTimer,
       "zhoneCpeVoipMedia": zhoneCpeVoipMedia,
       "zhoneCpeVoipMediaIndexNext": zhoneCpeVoipMediaIndexNext,
       "zhoneCpeVoipMediaTable": zhoneCpeVoipMediaTable,
       "zhoneCpeVoipMediaEntry": zhoneCpeVoipMediaEntry,
       "zhoneCpeVoipMediaIndex": zhoneCpeVoipMediaIndex,
       "zhoneCpeVoipMediaRowStatus": zhoneCpeVoipMediaRowStatus,
       "zhoneCpeVoipMediaProfileName": zhoneCpeVoipMediaProfileName,
       "zhoneCpeVoipMediaEchoCancel": zhoneCpeVoipMediaEchoCancel,
       "zhoneCpeVoipFaxMode": zhoneCpeVoipFaxMode,
       "zhoneCpeVoipCodecSelectionFirstOrder": zhoneCpeVoipCodecSelectionFirstOrder,
       "zhoneCpeVoipPacketPeriodSelectionFirstOrder": zhoneCpeVoipPacketPeriodSelectionFirstOrder,
       "zhoneCpeVoipSilenceSuppressionFirstOrder": zhoneCpeVoipSilenceSuppressionFirstOrder,
       "zhoneCpeVoipCodecSelectionSecondOrder": zhoneCpeVoipCodecSelectionSecondOrder,
       "zhoneCpeVoipPacketPeriodSelectionSecondOrder": zhoneCpeVoipPacketPeriodSelectionSecondOrder,
       "zhoneCpeVoipSilenceSuppressionSecondOrder": zhoneCpeVoipSilenceSuppressionSecondOrder,
       "zhoneCpeVoipCodecSelectionThirdOrder": zhoneCpeVoipCodecSelectionThirdOrder,
       "zhoneCpeVoipPacketPeriodSelectionThirdOrder": zhoneCpeVoipPacketPeriodSelectionThirdOrder,
       "zhoneCpeVoipSilenceSuppressionThirdOrder": zhoneCpeVoipSilenceSuppressionThirdOrder,
       "zhoneCpeVoipCodecSelectionFourthOrder": zhoneCpeVoipCodecSelectionFourthOrder,
       "zhoneCpeVoipPacketPeriodSelectionFourthOrder": zhoneCpeVoipPacketPeriodSelectionFourthOrder,
       "zhoneCpeVoipSilenceSuppressionFourthOrder": zhoneCpeVoipSilenceSuppressionFourthOrder,
       "zhoneCpeVoipSubscriberTable": zhoneCpeVoipSubscriberTable,
       "zhoneCpeVoipSubscriberEntry": zhoneCpeVoipSubscriberEntry,
       "zhoneCpeVoipSubscriberPortNumber": zhoneCpeVoipSubscriberPortNumber,
       "zhoneCpeVoipSubscriberRowStatus": zhoneCpeVoipSubscriberRowStatus,
       "zhoneCpeVoipSubscriberAdminState": zhoneCpeVoipSubscriberAdminState,
       "zhoneCpeVoipSubscriberDialNumber": zhoneCpeVoipSubscriberDialNumber,
       "zhoneCpeVoipSubscriberDisplayName": zhoneCpeVoipSubscriberDisplayName,
       "zhoneCpeVoipSubscriberUserName": zhoneCpeVoipSubscriberUserName,
       "zhoneCpeVoipSubscriberPassword": zhoneCpeVoipSubscriberPassword,
       "zhoneCpeVoipSubscriberImpedance": zhoneCpeVoipSubscriberImpedance,
       "zhoneCpeVoipSubscriberRxGain": zhoneCpeVoipSubscriberRxGain,
       "zhoneCpeVoipSubscriberTxGain": zhoneCpeVoipSubscriberTxGain,
       "zhoneCpeVoipSubscriberTransmissionPath": zhoneCpeVoipSubscriberTransmissionPath,
       "zhoneCpeVoipSubscriberSignallingCode": zhoneCpeVoipSubscriberSignallingCode,
       "zhoneCpeVoipServerProfileIndex": zhoneCpeVoipServerProfileIndex,
       "zhoneCpeVoipFeaturesProfileIndex": zhoneCpeVoipFeaturesProfileIndex,
       "zhoneCpeVoipMediaProfileIndex": zhoneCpeVoipMediaProfileIndex,
       "zhoneCpeVoipSubscriberPhoneFollowsWan": zhoneCpeVoipSubscriberPhoneFollowsWan,
       "zhoneCpeEthSubscriberTable": zhoneCpeEthSubscriberTable,
       "zhoneCpeEthSubscriberEntry": zhoneCpeEthSubscriberEntry,
       "zhoneCpeEthSubscriberPortNumber": zhoneCpeEthSubscriberPortNumber,
       "zhoneCpeEthSubscriberRowStatus": zhoneCpeEthSubscriberRowStatus,
       "zhoneCpeEthSubscriberAdminState": zhoneCpeEthSubscriberAdminState,
       "zhoneCpeEthSubscriberLoopback": zhoneCpeEthSubscriberLoopback,
       "zhoneCpeEthSubscriberRate": zhoneCpeEthSubscriberRate,
       "zhoneCpeEthSubscriberDuplex": zhoneCpeEthSubscriberDuplex,
       "zhoneCpeEthSubscriberMtu": zhoneCpeEthSubscriberMtu,
       "zhoneCpeEthSubscriberPortType": zhoneCpeEthSubscriberPortType,
       "zhoneCpeEthSubscriberPauseTime": zhoneCpeEthSubscriberPauseTime,
       "zhoneCpeEthSubscriberMode": zhoneCpeEthSubscriberMode,
       "zhoneCpeEthSubscriberPowerFeed": zhoneCpeEthSubscriberPowerFeed,
       "zhoneCpeVideoProfileIndex": zhoneCpeVideoProfileIndex,
       "zhoneCpeTrafficManagementProfileIndex": zhoneCpeTrafficManagementProfileIndex,
       "zhoneCpeEthSubscriberLineStatusAlarm": zhoneCpeEthSubscriberLineStatusAlarm,
       "zhoneCpeEthSubscriberAlarmSeverity": zhoneCpeEthSubscriberAlarmSeverity,
       "zhoneCpeEthSubscriberPowerShed": zhoneCpeEthSubscriberPowerShed,
       "zhoneCpeEthSubscriberPowerRange": zhoneCpeEthSubscriberPowerRange,
       "zhoneCpeEthSubscriberLldpMedList": zhoneCpeEthSubscriberLldpMedList,
       "zhoneCpeVideo": zhoneCpeVideo,
       "zhoneCpeVideoIndexNext": zhoneCpeVideoIndexNext,
       "zhoneCpeVideoTable": zhoneCpeVideoTable,
       "zhoneCpeVideoEntry": zhoneCpeVideoEntry,
       "zhoneCpeVideoIndex": zhoneCpeVideoIndex,
       "zhoneCpeGemPort": zhoneCpeGemPort,
       "zhoneCpeVlan": zhoneCpeVlan,
       "zhoneCpeVideoRowStatus": zhoneCpeVideoRowStatus,
       "zhoneCpeVideoProfileName": zhoneCpeVideoProfileName,
       "zhoneCpeVideoMaxSimultaneousGroups": zhoneCpeVideoMaxSimultaneousGroups,
       "zhoneCpeVideoMaxMulticastBandwidth": zhoneCpeVideoMaxMulticastBandwidth,
       "zhoneCpeVideoBandwidthEnforce": zhoneCpeVideoBandwidthEnforce,
       "zhoneCpeVideoIgmpVersion": zhoneCpeVideoIgmpVersion,
       "zhoneCpeVideoIgmpFunction": zhoneCpeVideoIgmpFunction,
       "zhoneCpeVideoImmediateLeave": zhoneCpeVideoImmediateLeave,
       "zhoneCpeVideoUpstreamIgmpRate": zhoneCpeVideoUpstreamIgmpRate,
       "zhoneCpeVideoRobustness": zhoneCpeVideoRobustness,
       "zhoneCpeVideoAccessControlList": zhoneCpeVideoAccessControlList,
       "zhoneCpeVideoAccessControl": zhoneCpeVideoAccessControl,
       "zhoneCpeVideoAccessControlIndexTable": zhoneCpeVideoAccessControlIndexTable,
       "zhoneCpeVideoAccessControlIndexEntry": zhoneCpeVideoAccessControlIndexEntry,
       "zhoneCpeVideoAccessControlIndexNext": zhoneCpeVideoAccessControlIndexNext,
       "zhoneCpeVideoAccessControlTable": zhoneCpeVideoAccessControlTable,
       "zhoneCpeVideoAccessControlEntry": zhoneCpeVideoAccessControlEntry,
       "zhoneCpeVideoAccessControlListIndex": zhoneCpeVideoAccessControlListIndex,
       "zhoneCpeVideoAccessControlEntryIndex": zhoneCpeVideoAccessControlEntryIndex,
       "zhoneCpeVideoAccessControlRowStatus": zhoneCpeVideoAccessControlRowStatus,
       "zhoneCpeVideoAccessControlProfileName": zhoneCpeVideoAccessControlProfileName,
       "zhoneCpeVideoAccessControlType": zhoneCpeVideoAccessControlType,
       "zhoneCpeVideoAccessControlSrcIp": zhoneCpeVideoAccessControlSrcIp,
       "zhoneCpeVideoAccessControlDstIpStart": zhoneCpeVideoAccessControlDstIpStart,
       "zhoneCpeVideoAccessControlDstIpEnd": zhoneCpeVideoAccessControlDstIpEnd,
       "zhoneCpeVideoAccessControlImputedGroupBw": zhoneCpeVideoAccessControlImputedGroupBw,
       "zhoneCpePweSubscriberTable": zhoneCpePweSubscriberTable,
       "zhoneCpePweSubscriberEntry": zhoneCpePweSubscriberEntry,
       "zhoneCpePweSubscriberPortNumber": zhoneCpePweSubscriberPortNumber,
       "zhoneCpePweSubscriberRowStatus": zhoneCpePweSubscriberRowStatus,
       "zhoneCpePweSubscriberAdminState": zhoneCpePweSubscriberAdminState,
       "zhoneCpePweSubscriberLoopback": zhoneCpePweSubscriberLoopback,
       "zhoneCpePweSubscriberNearEndPort": zhoneCpePweSubscriberNearEndPort,
       "zhoneCpePweSubscriberFarEndIp": zhoneCpePweSubscriberFarEndIp,
       "zhoneCpePweSubscriberFarEndPort": zhoneCpePweSubscriberFarEndPort,
       "zhoneCpePweSubscriberLineLength": zhoneCpePweSubscriberLineLength,
       "zhoneCpePweProfileIndex": zhoneCpePweProfileIndex,
       "zhoneCpePweSubscriberLineStatusAlarm": zhoneCpePweSubscriberLineStatusAlarm,
       "zhoneCpePweSubscriberAlarmSeverity": zhoneCpePweSubscriberAlarmSeverity,
       "zhoneCpePwe": zhoneCpePwe,
       "zhoneCpePweIndexNext": zhoneCpePweIndexNext,
       "zhoneCpePweTable": zhoneCpePweTable,
       "zhoneCpePweEntry": zhoneCpePweEntry,
       "zhoneCpePweIndex": zhoneCpePweIndex,
       "zhoneCpePweRowStatus": zhoneCpePweRowStatus,
       "zhoneCpePweProfileName": zhoneCpePweProfileName,
       "zhoneCpePweLineType": zhoneCpePweLineType,
       "zhoneCpePweEncoding": zhoneCpePweEncoding,
       "zhoneCpePweDs1Mode": zhoneCpePweDs1Mode,
       "zhoneCpePweDs1Framing": zhoneCpePweDs1Framing,
       "zhoneCpePweTransport": zhoneCpePweTransport,
       "zhoneCpePweServiceType": zhoneCpePweServiceType,
       "zhoneCpePweSignalling": zhoneCpePweSignalling,
       "zhoneCpePwePayloadSize": zhoneCpePwePayloadSize,
       "zhoneCpePwePayloadEncapsulationDelay": zhoneCpePwePayloadEncapsulationDelay,
       "zhoneCpePweTimingMode": zhoneCpePweTimingMode,
       "zhoneCpePweChannelAssign": zhoneCpePweChannelAssign,
       "zhoneCpePweClockReference": zhoneCpePweClockReference,
       "zhoneCpePweRtpTimeStampMode": zhoneCpePweRtpTimeStampMode,
       "zhoneCpePwePtypePayload": zhoneCpePwePtypePayload,
       "zhoneCpePwePtypeSignalling": zhoneCpePwePtypeSignalling,
       "zhoneCpePweSSrcPayload": zhoneCpePweSSrcPayload,
       "zhoneCpePweSSrcSignalling": zhoneCpePweSSrcSignalling,
       "zhoneCpePweExpectedPTypePayload": zhoneCpePweExpectedPTypePayload,
       "zhoneCpePweExpectedPTypeSignalling": zhoneCpePweExpectedPTypeSignalling,
       "zhoneCpePweExpectedSSrcPayload": zhoneCpePweExpectedSSrcPayload,
       "zhoneCpePweExpectedSSrcSignalling": zhoneCpePweExpectedSSrcSignalling,
       "zhoneCpePweJitterBufMax": zhoneCpePweJitterBufMax,
       "zhoneCpePweJitterBufDesired": zhoneCpePweJitterBufDesired,
       "zhoneCpePweFillPolicy": zhoneCpePweFillPolicy,
       "zhoneCpePweMisconnectedDeclarePolicy": zhoneCpePweMisconnectedDeclarePolicy,
       "zhoneCpePweMisconnectedClearPolicy": zhoneCpePweMisconnectedClearPolicy,
       "zhoneCpePweLossPacketDeclarePolicy": zhoneCpePweLossPacketDeclarePolicy,
       "zhoneCpePweLossPacketClearPolicy": zhoneCpePweLossPacketClearPolicy,
       "zhoneCpePweOverrunUnderrunDeclarePolicy": zhoneCpePweOverrunUnderrunDeclarePolicy,
       "zhoneCpePweOverrunUnderrunClearPolicy": zhoneCpePweOverrunUnderrunClearPolicy,
       "zhoneCpePweMalformedDeclarePolicy": zhoneCpePweMalformedDeclarePolicy,
       "zhoneCpePweMalformedClearPolicy": zhoneCpePweMalformedClearPolicy,
       "zhoneCpePweRBitTransmitSetPolicy": zhoneCpePweRBitTransmitSetPolicy,
       "zhoneCpePweRBitTransmitClearPolicy": zhoneCpePweRBitTransmitClearPolicy,
       "zhoneCpePweRBitReceivePolicy": zhoneCpePweRBitReceivePolicy,
       "zhoneCpePweLBitReceivePolicy": zhoneCpePweLBitReceivePolicy,
       "zhoneCpePweSesThreshold": zhoneCpePweSesThreshold,
       "zhoneCpePweCdvTolerance": zhoneCpePweCdvTolerance,
       "zhoneCpePweChannelAssociatedSignalling": zhoneCpePweChannelAssociatedSignalling,
       "zhoneCpePweMplsTpType": zhoneCpePweMplsTpType,
       "zhoneCpePweDscp": zhoneCpePweDscp,
       "zhoneCpeOnuModelInfoTable": zhoneCpeOnuModelInfoTable,
       "zhoneCpeOnuModelInfoEntry": zhoneCpeOnuModelInfoEntry,
       "zhoneCpeOnuModelInfoIndex": zhoneCpeOnuModelInfoIndex,
       "zhoneCpeOnuModelName": zhoneCpeOnuModelName,
       "zhoneCpeOnuBatteryBackup": zhoneCpeOnuBatteryBackup,
       "zhoneCpeOnuSipPlarSupported": zhoneCpeOnuSipPlarSupported,
       "zhoneCpeOnuEthSlotNumber": zhoneCpeOnuEthSlotNumber,
       "zhoneCpeOnuNumberOfEthPorts": zhoneCpeOnuNumberOfEthPorts,
       "zhoneCpeOnuPotsSlotNumber": zhoneCpeOnuPotsSlotNumber,
       "zhoneCpeOnuNumberOfPotsPorts": zhoneCpeOnuNumberOfPotsPorts,
       "zhoneCpeOnuRfVideoSlotNumber": zhoneCpeOnuRfVideoSlotNumber,
       "zhoneCpeOnuNumberOfRfVideoPorts": zhoneCpeOnuNumberOfRfVideoPorts,
       "zhoneCpeOnuCesSlotNumber": zhoneCpeOnuCesSlotNumber,
       "zhoneCpeOnuNumberOfCesPorts": zhoneCpeOnuNumberOfCesPorts,
       "zhoneCpeOnuModelInfoRGBridged": zhoneCpeOnuModelInfoRGBridged,
       "zhoneCpeOnuNumberOfWlanPorts": zhoneCpeOnuNumberOfWlanPorts,
       "zhoneCpeOnuModelInfoRg": zhoneCpeOnuModelInfoRg,
       "zhoneCpeOnuModelInfoRgVoip": zhoneCpeOnuModelInfoRgVoip,
       "zhoneCpeOnuModelInfoRgPwe": zhoneCpeOnuModelInfoRgPwe,
       "zhoneCpeOnuModelInfoTftpDnld": zhoneCpeOnuModelInfoTftpDnld,
       "zhoneCpeOnuSipSupported": zhoneCpeOnuSipSupported,
       "zhoneCpeOnuH248Supported": zhoneCpeOnuH248Supported,
       "zhoneCpeOnuMgcpSupported": zhoneCpeOnuMgcpSupported,
       "zhoneCpeOnuT1Supported": zhoneCpeOnuT1Supported,
       "zhoneCpeOnuE1Supported": zhoneCpeOnuE1Supported,
       "zhoneCpeOnuNumberOfPoEPorts": zhoneCpeOnuNumberOfPoEPorts,
       "zhoneCpeConnectionTable": zhoneCpeConnectionTable,
       "zhoneCpeConnectionEntry": zhoneCpeConnectionEntry,
       "zhoneCpePortIfIndex": zhoneCpePortIfIndex,
       "zhoneCpeTpType": zhoneCpeTpType,
       "zhoneCpeTpIndex": zhoneCpeTpIndex,
       "zhoneCpeVlanId": zhoneCpeVlanId,
       "zhoneCpeSlanId": zhoneCpeSlanId,
       "zhoneCpeConnectionRowStatus": zhoneCpeConnectionRowStatus,
       "zhoneCpeConnectionVlanCos": zhoneCpeConnectionVlanCos,
       "zhoneCpeConnectionVlanTpId": zhoneCpeConnectionVlanTpId,
       "zhoneCpeConnectionSlanCos": zhoneCpeConnectionSlanCos,
       "zhoneCpeConnectionSlanTpId": zhoneCpeConnectionSlanTpId,
       "zhoneCpeConnectionTranslateVlanId": zhoneCpeConnectionTranslateVlanId,
       "zhoneCpeConnectionTranslateVlanCos": zhoneCpeConnectionTranslateVlanCos,
       "zhoneCpeConnectionTranslateVlanTpId": zhoneCpeConnectionTranslateVlanTpId,
       "zhoneCpeConnectionTranslateSlanId": zhoneCpeConnectionTranslateSlanId,
       "zhoneCpeConnectionTranslateSlanCos": zhoneCpeConnectionTranslateSlanCos,
       "zhoneCpeConnectionTranslateSlanTpId": zhoneCpeConnectionTranslateSlanTpId,
       "zhoneCpeConnectionFloodingGport": zhoneCpeConnectionFloodingGport,
       "zhoneCpeConnectionVideoGport": zhoneCpeConnectionVideoGport,
       "zhoneCpeConnectionDscpToCosProfileIndex": zhoneCpeConnectionDscpToCosProfileIndex,
       "zhoneCpeConnectionRgMode": zhoneCpeConnectionRgMode,
       "zhoneCpeConnectionGuidedVlanId": zhoneCpeConnectionGuidedVlanId,
       "zhoneCpeConnectionGuidedCos": zhoneCpeConnectionGuidedCos,
       "zhoneCpeRfSubscriberTable": zhoneCpeRfSubscriberTable,
       "zhoneCpeRfSubscriberEntry": zhoneCpeRfSubscriberEntry,
       "zhoneCpeRfSubscriberPortNumber": zhoneCpeRfSubscriberPortNumber,
       "zhoneCpeRfSubscriberRowStatus": zhoneCpeRfSubscriberRowStatus,
       "zhoneCpeRfSubscriberAdminState": zhoneCpeRfSubscriberAdminState,
       "zhoneCpeRfSubscriberLineStatusAlarm": zhoneCpeRfSubscriberLineStatusAlarm,
       "zhoneCpeRfSubscriberAlarmSeverity": zhoneCpeRfSubscriberAlarmSeverity,
       "zhoneCpeTrafficManagement": zhoneCpeTrafficManagement,
       "zhoneCpeTrafficManagementIndexNext": zhoneCpeTrafficManagementIndexNext,
       "zhoneCpeTrafficManagementTable": zhoneCpeTrafficManagementTable,
       "zhoneCpeTrafficManagementEntry": zhoneCpeTrafficManagementEntry,
       "zhoneCpeTrafficManagementIndex": zhoneCpeTrafficManagementIndex,
       "zhoneCpeTrafficManagementRowStatus": zhoneCpeTrafficManagementRowStatus,
       "zhoneCpeTrafficManagementProfileName": zhoneCpeTrafficManagementProfileName,
       "zhoneCpeTrafficManagementUpstreamSIR": zhoneCpeTrafficManagementUpstreamSIR,
       "zhoneCpeTrafficManagementUpstreamPIR": zhoneCpeTrafficManagementUpstreamPIR,
       "zhoneCpeTrafficManagementUpstreamPriority": zhoneCpeTrafficManagementUpstreamPriority,
       "zhoneCpeTrafficManagementUpstreamWeight": zhoneCpeTrafficManagementUpstreamWeight,
       "zhoneCpeTrafficManagementDownstreamSIR": zhoneCpeTrafficManagementDownstreamSIR,
       "zhoneCpeTrafficManagementDownstreamPIR": zhoneCpeTrafficManagementDownstreamPIR,
       "zhoneCpeTrafficManagementDownstreamPriority": zhoneCpeTrafficManagementDownstreamPriority,
       "zhoneCpeTrafficManagementDownstreamWeight": zhoneCpeTrafficManagementDownstreamWeight,
       "zhoneCpeTrafficManagementPeakBurstSize": zhoneCpeTrafficManagementPeakBurstSize,
       "zhoneCpeSystemTable": zhoneCpeSystemTable,
       "zhoneCpeSystemEntry": zhoneCpeSystemEntry,
       "zhoneCpeSystemRowStatus": zhoneCpeSystemRowStatus,
       "zhoneCpeSystemCommonProfileIndex": zhoneCpeSystemCommonProfileIndex,
       "zhoneCpeSystemMgcpClientName": zhoneCpeSystemMgcpClientName,
       "zhoneCpeSystemCommon": zhoneCpeSystemCommon,
       "zhoneCpeSystemCommonIndexNext": zhoneCpeSystemCommonIndexNext,
       "zhoneCpeSystemCommonTable": zhoneCpeSystemCommonTable,
       "zhoneCpeSystemCommonEntry": zhoneCpeSystemCommonEntry,
       "zhoneCpeSystemCommonIndex": zhoneCpeSystemCommonIndex,
       "zhoneCpeSystemCommonRowStatus": zhoneCpeSystemCommonRowStatus,
       "zhoneCpeSystemCommonProfileName": zhoneCpeSystemCommonProfileName,
       "zhoneCpeSystemCommonFirewall": zhoneCpeSystemCommonFirewall,
       "zhoneCpeSystemCommonSyncCookieProtection": zhoneCpeSystemCommonSyncCookieProtection,
       "zhoneCpeSystemCommonCrossVlanRouting": zhoneCpeSystemCommonCrossVlanRouting,
       "zhoneCpeStaticRouteListProfileIndex": zhoneCpeStaticRouteListProfileIndex,
       "zhoneCpeDnsHostListProfile": zhoneCpeDnsHostListProfile,
       "zhoneCpeSystemCommonTr69Inform": zhoneCpeSystemCommonTr69Inform,
       "zhoneCpeSystemCommonInformInterval": zhoneCpeSystemCommonInformInterval,
       "zhoneCpeSystemCommonAcsUrl": zhoneCpeSystemCommonAcsUrl,
       "zhoneCpeSystemCommonAcsUsername": zhoneCpeSystemCommonAcsUsername,
       "zhoneCpeSystemCommonAcsPassword": zhoneCpeSystemCommonAcsPassword,
       "zhoneCpeSystemCommonAdminPassword": zhoneCpeSystemCommonAdminPassword,
       "zhoneCpeSystemCommonSupportPassword": zhoneCpeSystemCommonSupportPassword,
       "zhoneCpeSystemCommonUserPassword": zhoneCpeSystemCommonUserPassword,
       "zhoneCpeSystemCommonPowerSupply": zhoneCpeSystemCommonPowerSupply,
       "zhoneCpeSystemCommonPowerShutdownDelay": zhoneCpeSystemCommonPowerShutdownDelay,
       "zhoneCpeSystemCommonPowerRestoreDelay": zhoneCpeSystemCommonPowerRestoreDelay,
       "zhoneCpeInterfaceVlanTable": zhoneCpeInterfaceVlanTable,
       "zhoneCpeInterfaceVlanEntry": zhoneCpeInterfaceVlanEntry,
       "zhoneCpeInterfaceVlanRowStatus": zhoneCpeInterfaceVlanRowStatus,
       "zhoneCpeInterfaceVlanRgMode": zhoneCpeInterfaceVlanRgMode,
       "zhoneCpeInterfaceVlanTranslateVlanId": zhoneCpeInterfaceVlanTranslateVlanId,
       "zhoneCpeInterfaceVlanTranslateVlanCos": zhoneCpeInterfaceVlanTranslateVlanCos,
       "zhoneCpeInterfaceVlanTranslateSlanId": zhoneCpeInterfaceVlanTranslateSlanId,
       "zhoneCpeInterfaceVlanTranslateSlanCos": zhoneCpeInterfaceVlanTranslateSlanCos,
       "zhoneCpeInterfaceVlanTranslateSlanTpId": zhoneCpeInterfaceVlanTranslateSlanTpId,
       "zhoneCpeInterfaceVlanIpAddress": zhoneCpeInterfaceVlanIpAddress,
       "zhoneCpeIpServerProfile": zhoneCpeIpServerProfile,
       "zhoneCpeDhcpServerProfileIndex": zhoneCpeDhcpServerProfileIndex,
       "zhoneCpePortFwdListProfileIndex": zhoneCpePortFwdListProfileIndex,
       "zhoneCpeDhcpServer": zhoneCpeDhcpServer,
       "zhoneCpeDhcpServerIndexNext": zhoneCpeDhcpServerIndexNext,
       "zhoneCpeDhcpServerTable": zhoneCpeDhcpServerTable,
       "zhoneCpeDhcpServerEntry": zhoneCpeDhcpServerEntry,
       "zhoneCpeDhcpServerIndex": zhoneCpeDhcpServerIndex,
       "zhoneCpeDhcpServerRowStatus": zhoneCpeDhcpServerRowStatus,
       "zhoneCpeDhcpServerProfileName": zhoneCpeDhcpServerProfileName,
       "zhoneCpeDhcpServerStartAddress": zhoneCpeDhcpServerStartAddress,
       "zhoneCpeDhcpServerEndAddress": zhoneCpeDhcpServerEndAddress,
       "zhoneCpeDhcpServerLeaseTime": zhoneCpeDhcpServerLeaseTime,
       "zhoneCpeDhcpServerConditionalServerListProfile": zhoneCpeDhcpServerConditionalServerListProfile,
       "zhoneCpePppoeTable": zhoneCpePppoeTable,
       "zhoneCpePppoeEntry": zhoneCpePppoeEntry,
       "zhoneCpePppoeRowStatus": zhoneCpePppoeRowStatus,
       "zhoneCpePppoeUsername": zhoneCpePppoeUsername,
       "zhoneCpePppoePassword": zhoneCpePppoePassword,
       "zhoneCpePppoeAuthentication": zhoneCpePppoeAuthentication,
       "zhoneCpePppoeRetryInterval": zhoneCpePppoeRetryInterval,
       "zhoneCpeWlanSubscriberTable": zhoneCpeWlanSubscriberTable,
       "zhoneCpeWlanSubscriberEntry": zhoneCpeWlanSubscriberEntry,
       "zhoneCpeWlanSubscriberIndex": zhoneCpeWlanSubscriberIndex,
       "zhoneCpeWlanSubscriberRowStatus": zhoneCpeWlanSubscriberRowStatus,
       "zhoneCpeWlanSubscriberAdminState": zhoneCpeWlanSubscriberAdminState,
       "zhoneCpeWlanSubscriberSsid": zhoneCpeWlanSubscriberSsid,
       "zhoneCpeWlanSubscriberEncryptKey": zhoneCpeWlanSubscriberEncryptKey,
       "zhoneCpeWlanSubscriberDevicePin": zhoneCpeWlanSubscriberDevicePin,
       "zhoneCpeWlanSubscriberRadiusKey": zhoneCpeWlanSubscriberRadiusKey,
       "zhoneCpeWlanProfileIndex": zhoneCpeWlanProfileIndex,
       "zhoneCpeAccessControlListProfileIndex": zhoneCpeAccessControlListProfileIndex,
       "zhoneCpeWdsMacListProfileIndex": zhoneCpeWdsMacListProfileIndex,
       "zhoneCpeWlanAdvProfileIndex": zhoneCpeWlanAdvProfileIndex,
       "zhoneCpeWlan": zhoneCpeWlan,
       "zhoneCpeWlanIndexNext": zhoneCpeWlanIndexNext,
       "zhoneCpeWlanTable": zhoneCpeWlanTable,
       "zhoneCpeWlanEntry": zhoneCpeWlanEntry,
       "zhoneCpeWlanIndex": zhoneCpeWlanIndex,
       "zhoneCpeWlanRowStatus": zhoneCpeWlanRowStatus,
       "zhoneCpeWlanProfileName": zhoneCpeWlanProfileName,
       "zhoneCpeWlanHideAccessPoint": zhoneCpeWlanHideAccessPoint,
       "zhoneCpeWlanIsolateClients": zhoneCpeWlanIsolateClients,
       "zhoneCpeWlanWmmAdvertise": zhoneCpeWlanWmmAdvertise,
       "zhoneCpeWlanMcastFwd": zhoneCpeWlanMcastFwd,
       "zhoneCpeWlanMaxClients": zhoneCpeWlanMaxClients,
       "zhoneCpeWlanNetAuthentication": zhoneCpeWlanNetAuthentication,
       "zhoneCpeWlanWpaGroupRekeyInterval": zhoneCpeWlanWpaGroupRekeyInterval,
       "zhoneCpeWlanWpaEncryption": zhoneCpeWlanWpaEncryption,
       "zhoneCpeWlanWepEncryption": zhoneCpeWlanWepEncryption,
       "zhoneCpeWlanWepStrength": zhoneCpeWlanWepStrength,
       "zhoneCpeWlanRadiusServerIp": zhoneCpeWlanRadiusServerIp,
       "zhoneCpeWlanRadiusPort": zhoneCpeWlanRadiusPort,
       "zhoneCpeWlanWpa2PreAuthentication": zhoneCpeWlanWpa2PreAuthentication,
       "zhoneCpeWlanNetReAuthenticationInterval": zhoneCpeWlanNetReAuthenticationInterval,
       "zhoneCpeStaticRouteList": zhoneCpeStaticRouteList,
       "zhoneCpeStaticRouteListIndexNext": zhoneCpeStaticRouteListIndexNext,
       "zhoneCpeStaticRouteListTable": zhoneCpeStaticRouteListTable,
       "zhoneCpeStaticRouteListEntry": zhoneCpeStaticRouteListEntry,
       "zhoneCpeStaticRouteListIndex": zhoneCpeStaticRouteListIndex,
       "zhoneCpeStaticRouteListRowStatus": zhoneCpeStaticRouteListRowStatus,
       "zhoneCpeStaticRouteListProfileName": zhoneCpeStaticRouteListProfileName,
       "zhoneCpeStaticRoute": zhoneCpeStaticRoute,
       "zhoneCpeStaticRouteIndexTable": zhoneCpeStaticRouteIndexTable,
       "zhoneCpeStaticRouteIndexEntry": zhoneCpeStaticRouteIndexEntry,
       "zhoneCpeStaticRouteEntryIndexNext": zhoneCpeStaticRouteEntryIndexNext,
       "zhoneCpeStaticRouteTable": zhoneCpeStaticRouteTable,
       "zhoneCpeStaticRouteEntry": zhoneCpeStaticRouteEntry,
       "zhoneCpeStaticRouteEntryIndex": zhoneCpeStaticRouteEntryIndex,
       "zhoneCpeStaticRouteRowStatus": zhoneCpeStaticRouteRowStatus,
       "zhoneCpeStaticRouteDestinationIp": zhoneCpeStaticRouteDestinationIp,
       "zhoneCpeStaticRouteNetmask": zhoneCpeStaticRouteNetmask,
       "zhoneCpeStaticRouteGateway": zhoneCpeStaticRouteGateway,
       "zhoneCpeStaticRouteMetric": zhoneCpeStaticRouteMetric,
       "zhoneCpePortFwdList": zhoneCpePortFwdList,
       "zhoneCpePortFwdListIndexNext": zhoneCpePortFwdListIndexNext,
       "zhoneCpePortFwdListTable": zhoneCpePortFwdListTable,
       "zhoneCpePortFwdListEntry": zhoneCpePortFwdListEntry,
       "zhoneCpePortFwdListIndex": zhoneCpePortFwdListIndex,
       "zhoneCpePortFwdListRowStatus": zhoneCpePortFwdListRowStatus,
       "zhoneCpePortFwdListProfileName": zhoneCpePortFwdListProfileName,
       "zhoneCpePortFwd": zhoneCpePortFwd,
       "zhoneCpePortFwdIndexTable": zhoneCpePortFwdIndexTable,
       "zhoneCpePortFwdIndexEntry": zhoneCpePortFwdIndexEntry,
       "zhoneCpePortFwdEntryIndexNext": zhoneCpePortFwdEntryIndexNext,
       "zhoneCpePortFwdTable": zhoneCpePortFwdTable,
       "zhoneCpePortFwdEntry": zhoneCpePortFwdEntry,
       "zhoneCpePortFwdEntryIndex": zhoneCpePortFwdEntryIndex,
       "zhoneCpePortFwdRowStatus": zhoneCpePortFwdRowStatus,
       "zhoneCpePortFwdType": zhoneCpePortFwdType,
       "zhoneCpePortFwdPortStart": zhoneCpePortFwdPortStart,
       "zhoneCpePortFwdPortEnd": zhoneCpePortFwdPortEnd,
       "zhoneCpePortFwdProtocol": zhoneCpePortFwdProtocol,
       "zhoneCpePortFwdPrivatePort": zhoneCpePortFwdPrivatePort,
       "zhoneCpePortFwdPrivateIp": zhoneCpePortFwdPrivateIp,
       "zhoneCpeServiceApplication": zhoneCpeServiceApplication,
       "zhoneCpeServiceApplicationTable": zhoneCpeServiceApplicationTable,
       "zhoneCpeServiceApplicationEntry": zhoneCpeServiceApplicationEntry,
       "zhoneCpeServiceApplicationTemplateType": zhoneCpeServiceApplicationTemplateType,
       "zhoneCpeServiceApplicationTemplateId": zhoneCpeServiceApplicationTemplateId,
       "zhoneCpeServiceApplicationVirtualConnection": zhoneCpeServiceApplicationVirtualConnection,
       "zhoneCpeServiceApplicationTpType": zhoneCpeServiceApplicationTpType,
       "zhoneCpeServiceApplicationTpIndex": zhoneCpeServiceApplicationTpIndex,
       "zhoneCpeServiceApplicationRowStatus": zhoneCpeServiceApplicationRowStatus,
       "zhoneCpeServiceApplicationVlan": zhoneCpeServiceApplicationVlan,
       "zhoneCpeServiceApplicationSlan": zhoneCpeServiceApplicationSlan,
       "zhoneCpeDnsHostList": zhoneCpeDnsHostList,
       "zhoneCpeDnsHostListIndexNext": zhoneCpeDnsHostListIndexNext,
       "zhoneCpeDnsHostListTable": zhoneCpeDnsHostListTable,
       "zhoneCpeDnsHostListEntry": zhoneCpeDnsHostListEntry,
       "zhoneCpeDnsHostListIndex": zhoneCpeDnsHostListIndex,
       "zhoneCpeDnsHostListRowStatus": zhoneCpeDnsHostListRowStatus,
       "zhoneCpeDnsHostListProfileName": zhoneCpeDnsHostListProfileName,
       "zhoneCpeDnsHost": zhoneCpeDnsHost,
       "zhoneCpeDnsHostIndexTable": zhoneCpeDnsHostIndexTable,
       "zhoneCpeDnsHostIndexEntry": zhoneCpeDnsHostIndexEntry,
       "zhoneCpeDnsHostIndexEntryIndexNext": zhoneCpeDnsHostIndexEntryIndexNext,
       "zhoneCpeDnsHostTable": zhoneCpeDnsHostTable,
       "zhoneCpeDnsHostEntry": zhoneCpeDnsHostEntry,
       "zhoneCpeDnsHostEntryIndex": zhoneCpeDnsHostEntryIndex,
       "zhoneCpeDnsHostRowStatus": zhoneCpeDnsHostRowStatus,
       "zhoneCpeDnsHostDomainName": zhoneCpeDnsHostDomainName,
       "zhoneCpeDnsHostIpAddress": zhoneCpeDnsHostIpAddress,
       "zhoneCpeWlanAdvanced": zhoneCpeWlanAdvanced,
       "zhoneCpeWlanAdvIndexNext": zhoneCpeWlanAdvIndexNext,
       "zhoneCpeWlanAdvancedTable": zhoneCpeWlanAdvancedTable,
       "zhoneCpeWlanAdvancedEntry": zhoneCpeWlanAdvancedEntry,
       "zhoneCpeWlanAdvIndex": zhoneCpeWlanAdvIndex,
       "zhoneCpeWlanAdvRowStatus": zhoneCpeWlanAdvRowStatus,
       "zhoneCpeWlanAdvProfileName": zhoneCpeWlanAdvProfileName,
       "zhoneCpeWlanAdvChannel": zhoneCpeWlanAdvChannel,
       "zhoneCpeWlanAdvAutoChanTimer": zhoneCpeWlanAdvAutoChanTimer,
       "zhoneCpeWlanAdvDot11nMode": zhoneCpeWlanAdvDot11nMode,
       "zhoneCpeWlanAdvDot11nRate": zhoneCpeWlanAdvDot11nRate,
       "zhoneCpeWlanAdvDot1nProtection": zhoneCpeWlanAdvDot1nProtection,
       "zhoneCpeWlanAdvDot1nClientOnly": zhoneCpeWlanAdvDot1nClientOnly,
       "zhoneCpeWlanAdvRate54G": zhoneCpeWlanAdvRate54G,
       "zhoneCpeWlanAdvMcastRate": zhoneCpeWlanAdvMcastRate,
       "zhoneCpeWlanAdvBasicRate": zhoneCpeWlanAdvBasicRate,
       "zhoneCpeWlanAdvFragmentationThreshold": zhoneCpeWlanAdvFragmentationThreshold,
       "zhoneCpeWlanAdvRtsThreshold": zhoneCpeWlanAdvRtsThreshold,
       "zhoneCpeWlanAdvDtimInterval": zhoneCpeWlanAdvDtimInterval,
       "zhoneCpeWlanAdvBeaconInterval": zhoneCpeWlanAdvBeaconInterval,
       "zhoneCpeWlanAdvGlobalMaxClients": zhoneCpeWlanAdvGlobalMaxClients,
       "zhoneCpeWlanAdvXpressTechnology": zhoneCpeWlanAdvXpressTechnology,
       "zhoneCpeWlanAdvTxPower": zhoneCpeWlanAdvTxPower,
       "zhoneCpeWlanAdvWmm": zhoneCpeWlanAdvWmm,
       "zhoneCpeWlanAdvWmmNoAck": zhoneCpeWlanAdvWmmNoAck,
       "zhoneCpeWlanAdvWmmApsd": zhoneCpeWlanAdvWmmApsd,
       "zhoneCpeWlanAdvApMode": zhoneCpeWlanAdvApMode,
       "zhoneCpeWlanAdvBridgeRestrict": zhoneCpeWlanAdvBridgeRestrict,
       "zhoneCpeWlanAdvWps": zhoneCpeWlanAdvWps,
       "zhoneCpeWlanAdvWpsAddClientMethod": zhoneCpeWlanAdvWpsAddClientMethod,
       "zhoneCpeWlanAdvWpsApMode": zhoneCpeWlanAdvWpsApMode,
       "zhoneCpeCondDhcpSrvList": zhoneCpeCondDhcpSrvList,
       "zhoneCpeCondiDhcpSrvListIndexNext": zhoneCpeCondiDhcpSrvListIndexNext,
       "zhoneCpeCondDhcpSrvListTable": zhoneCpeCondDhcpSrvListTable,
       "zhoneCpeCondDhcpSrvListEntry": zhoneCpeCondDhcpSrvListEntry,
       "zhoneCpeCondDhcpSrvListIndex": zhoneCpeCondDhcpSrvListIndex,
       "zhoneCpeCondDhcpSrvListRowStatus": zhoneCpeCondDhcpSrvListRowStatus,
       "zhoneCpeCondDhcpSrvListProfileName": zhoneCpeCondDhcpSrvListProfileName,
       "zhoneCpeCondDhcpSrv": zhoneCpeCondDhcpSrv,
       "zhoneCpeCondDhcpSrvIndexTable": zhoneCpeCondDhcpSrvIndexTable,
       "zhoneCpeCondDhcpSrvIndexEntry": zhoneCpeCondDhcpSrvIndexEntry,
       "zhoneCpeCondDhcpSrvIndexEntryIndexNext": zhoneCpeCondDhcpSrvIndexEntryIndexNext,
       "zhoneCpeCondDhcpSrvTable": zhoneCpeCondDhcpSrvTable,
       "zhoneCpeCondDhcpSrvEntry": zhoneCpeCondDhcpSrvEntry,
       "zhoneCpeCondDhcpSrvEntryIndex": zhoneCpeCondDhcpSrvEntryIndex,
       "zhoneCpeCondDhcpSrvRowStatus": zhoneCpeCondDhcpSrvRowStatus,
       "zhoneCpeCondDhcpSrvAdminState": zhoneCpeCondDhcpSrvAdminState,
       "zhoneCpeCondDhcpSrvPriorityOrder": zhoneCpeCondDhcpSrvPriorityOrder,
       "zhoneCpeCondDhcpVciOui": zhoneCpeCondDhcpVciOui,
       "zhoneCpeCondDhcpSrvVciMatch": zhoneCpeCondDhcpSrvVciMatch,
       "zhoneCpeCondDhcpSrvStartAddr": zhoneCpeCondDhcpSrvStartAddr,
       "zhoneCpeCondDhcpSrvEndAddr": zhoneCpeCondDhcpSrvEndAddr,
       "zhoneCpeCondDhcpSrvWanVlan": zhoneCpeCondDhcpSrvWanVlan,
       "zhoneCpeCondDhcpSrvPortFwdRule": zhoneCpeCondDhcpSrvPortFwdRule,
       "zhoneCpeCondDhcpSrvStartPort": zhoneCpeCondDhcpSrvStartPort,
       "zhoneCpeCondDhcpSrvPrivatePort": zhoneCpeCondDhcpSrvPrivatePort,
       "zhoneCpeCondDhcpSrvProtocol": zhoneCpeCondDhcpSrvProtocol,
       "zhoneCpeCondDhcpSrvPriDns": zhoneCpeCondDhcpSrvPriDns,
       "zhoneCpeCondDhcpSrvSecDns": zhoneCpeCondDhcpSrvSecDns,
       "zhoneCpeCondDhcpSrvPriNpt": zhoneCpeCondDhcpSrvPriNpt,
       "zhoneCpeCondDhcpSrvSecNpt": zhoneCpeCondDhcpSrvSecNpt,
       "zhoneCpeCondDhcpSrvVsi": zhoneCpeCondDhcpSrvVsi,
       "zhoneCpeCondDhcpSrvPermanent": zhoneCpeCondDhcpSrvPermanent,
       "zhoneCpeCmd": zhoneCpeCmd,
       "zhoneCpeCmdOperation": zhoneCpeCmdOperation,
       "zhoneCpeCmdSrcIfIndex": zhoneCpeCmdSrcIfIndex,
       "zhoneCpeCmdSrcShelf": zhoneCpeCmdSrcShelf,
       "zhoneCpeCmdSrcSlot": zhoneCpeCmdSrcSlot,
       "zhoneCpeCmdSrcPort": zhoneCpeCmdSrcPort,
       "zhoneCpeCmdSrcSubport": zhoneCpeCmdSrcSubport,
       "zhoneCpeCmdSrcTpType": zhoneCpeCmdSrcTpType,
       "zhoneCpeCmdSrcTpIndex": zhoneCpeCmdSrcTpIndex,
       "zhoneCpeCmdDstIfIndex": zhoneCpeCmdDstIfIndex,
       "zhoneCpeCmdDstShelf": zhoneCpeCmdDstShelf,
       "zhoneCpeCmdDstSlot": zhoneCpeCmdDstSlot,
       "zhoneCpeCmdDstPort": zhoneCpeCmdDstPort,
       "zhoneCpeCmdDstSubport": zhoneCpeCmdDstSubport,
       "zhoneCpeCmdDstTpType": zhoneCpeCmdDstTpType,
       "zhoneCpeCmdDstTpIndex": zhoneCpeCmdDstTpIndex,
       "zhoneCpeCmdString": zhoneCpeCmdString,
       "zhoneCpeCmdSvcTemplateType": zhoneCpeCmdSvcTemplateType,
       "zhoneCpeCmdSvcTemplateId": zhoneCpeCmdSvcTemplateId,
       "zhoneCpeCmdSvcTemplateIfIndex": zhoneCpeCmdSvcTemplateIfIndex,
       "zhoneCpeCmdSvcTemplateVirtualConn": zhoneCpeCmdSvcTemplateVirtualConn,
       "zhoneCpeCmdSvcTemplateTpType": zhoneCpeCmdSvcTemplateTpType,
       "zhoneCpeCmdSvcTemplateTpIndex": zhoneCpeCmdSvcTemplateTpIndex,
       "zhoneCpeCmdSvcTemplateVlan": zhoneCpeCmdSvcTemplateVlan,
       "zhoneCpeCmdSvcTemplateSlan": zhoneCpeCmdSvcTemplateSlan,
       "zhoneCpeCmdOverrideTpIndex": zhoneCpeCmdOverrideTpIndex,
       "zhoneCpeCmdOverrideVlanId": zhoneCpeCmdOverrideVlanId,
       "zhoneCpeCmdOverrideVlanCos": zhoneCpeCmdOverrideVlanCos,
       "zhoneCpeCmdOverrideSlanId": zhoneCpeCmdOverrideSlanId,
       "zhoneCpeCmdOverrideSlanCos": zhoneCpeCmdOverrideSlanCos,
       "zhoneCpeLldpMedPolicyList": zhoneCpeLldpMedPolicyList,
       "zhoneCpeLldpMedPolicyListIndexNext": zhoneCpeLldpMedPolicyListIndexNext,
       "zhoneCpeLldpMedPolicyListTable": zhoneCpeLldpMedPolicyListTable,
       "zhoneCpeLldpMedPolicyListEntry": zhoneCpeLldpMedPolicyListEntry,
       "zhoneCpeLldpMedPolicyListIndex": zhoneCpeLldpMedPolicyListIndex,
       "zhoneCpeLldpMedPolicyListRowStatus": zhoneCpeLldpMedPolicyListRowStatus,
       "zhoneCpeLldpMedPolicyListProfileName": zhoneCpeLldpMedPolicyListProfileName,
       "zhoneCpeLldpMedPolicy": zhoneCpeLldpMedPolicy,
       "zhoneCpeLldpMedPolicyIndexTable": zhoneCpeLldpMedPolicyIndexTable,
       "zhoneCpeLldpMedPolicyIndexEntry": zhoneCpeLldpMedPolicyIndexEntry,
       "zhoneCpeLldpMedPolicyIndexEntryIndexNext": zhoneCpeLldpMedPolicyIndexEntryIndexNext,
       "zhoneCpeLldpMedPolicyTable": zhoneCpeLldpMedPolicyTable,
       "zhoneCpeLldpMedPolicyEntry": zhoneCpeLldpMedPolicyEntry,
       "zhoneCpeLldpMedPolicyEntryIndex": zhoneCpeLldpMedPolicyEntryIndex,
       "zhoneCpeLldpMedPolicyRowStatus": zhoneCpeLldpMedPolicyRowStatus,
       "zhoneCpeLldpMedPolicyAdminState": zhoneCpeLldpMedPolicyAdminState,
       "zhoneCpeLldpMedPolicyAppType": zhoneCpeLldpMedPolicyAppType,
       "zhoneCpeLldpMedPolicyVlanId": zhoneCpeLldpMedPolicyVlanId,
       "zhoneCpeLldpMedPolicyCos": zhoneCpeLldpMedPolicyCos,
       "zhoneCpeLldpMedPolicyDscp": zhoneCpeLldpMedPolicyDscp,
       "zhoneCpeAutoCfgRule": zhoneCpeAutoCfgRule,
       "zhoneCpeAutoCfgRuleIndexNext": zhoneCpeAutoCfgRuleIndexNext,
       "zhoneCpeAutoCfgRuleTable": zhoneCpeAutoCfgRuleTable,
       "zhoneCpeAutoCfgRuleEntry": zhoneCpeAutoCfgRuleEntry,
       "zhoneCpeAutoCfgRuleIndex": zhoneCpeAutoCfgRuleIndex,
       "zhoneCpeAutoCfgRuleAdminState": zhoneCpeAutoCfgRuleAdminState,
       "zhoneCpeAutoCfgRulePriority": zhoneCpeAutoCfgRulePriority,
       "zhoneCpeAutoCfgRuleMatchExpression": zhoneCpeAutoCfgRuleMatchExpression,
       "zhoneCpeAutoCfgRuleServiceTemplate": zhoneCpeAutoCfgRuleServiceTemplate,
       "zhoneCpeAutoCfgRuleTargetUni": zhoneCpeAutoCfgRuleTargetUni,
       "zhoneCpeAutoCfgRuleDeleteBeforeApply": zhoneCpeAutoCfgRuleDeleteBeforeApply,
       "zhoneCpeAutoCfgRuleRowStatus": zhoneCpeAutoCfgRuleRowStatus,
       "zhoneCpeAutoCfgRuleProfileName": zhoneCpeAutoCfgRuleProfileName,
       "zhoneCpeCfgGlobalSettings": zhoneCpeCfgGlobalSettings,
       "zhoneCpeCfgAutoAssign": zhoneCpeCfgAutoAssign,
       "zhoneCpeCfgAutoConfig": zhoneCpeCfgAutoConfig,
       "zhoneCpeCfgParamsStr": zhoneCpeCfgParamsStr,
       "zhoneCpeMIB": zhoneCpeMIB,
       "zhoneCpeSipDialPlanGroup": zhoneCpeSipDialPlanGroup,
       "zhoneCpeVoipServerGroup": zhoneCpeVoipServerGroup,
       "zhoneCpeIpGroup": zhoneCpeIpGroup,
       "zhoneCpeIpServerGroup": zhoneCpeIpServerGroup,
       "zhoneCpeVoipFeaturesGroup": zhoneCpeVoipFeaturesGroup,
       "zhoneCpeVoipMediaGroup": zhoneCpeVoipMediaGroup,
       "zhoneCpeVoipSubscriberGroup": zhoneCpeVoipSubscriberGroup,
       "zhoneCpeEthSubscriberGroup": zhoneCpeEthSubscriberGroup,
       "zhoneCpeVideoGroup": zhoneCpeVideoGroup,
       "zhoneCpeVideoAccessControlGroup": zhoneCpeVideoAccessControlGroup,
       "zhoneCpePweSubscriberGroup": zhoneCpePweSubscriberGroup,
       "zhoneCpePweGroup": zhoneCpePweGroup,
       "zhoneCpeOnuModelInfoGroup": zhoneCpeOnuModelInfoGroup,
       "zhoneCpeConnectionGroup": zhoneCpeConnectionGroup,
       "zhoneCpeRfSubscriberGroup": zhoneCpeRfSubscriberGroup,
       "zhoneCpeTrafficManagementGroup": zhoneCpeTrafficManagementGroup,
       "zhoneCpeSystemGroup": zhoneCpeSystemGroup,
       "zhoneCpeSystemCommonGroup": zhoneCpeSystemCommonGroup,
       "zhoneCpeInterfaceVlanGroup": zhoneCpeInterfaceVlanGroup,
       "zhoneCpeDhcpServerGroup": zhoneCpeDhcpServerGroup,
       "zhoneCpePppoeGroup": zhoneCpePppoeGroup,
       "zhoneCpeWlanSubscriberGroup": zhoneCpeWlanSubscriberGroup,
       "zhoneCpeWlanGroup": zhoneCpeWlanGroup,
       "zhoneCpeStaticRouteListGroup": zhoneCpeStaticRouteListGroup,
       "zhoneCpeStaticRouteGroup": zhoneCpeStaticRouteGroup,
       "zhoneCpePortFwdListGroup": zhoneCpePortFwdListGroup,
       "zhoneCpePortFwdGroup": zhoneCpePortFwdGroup,
       "zhoneCpeServiceApplicationGroup": zhoneCpeServiceApplicationGroup,
       "zhoneCpeDnsHostListGroup": zhoneCpeDnsHostListGroup,
       "zhoneCpeDnsHostGroup": zhoneCpeDnsHostGroup,
       "zhoneCpeWlanAdvGroup": zhoneCpeWlanAdvGroup,
       "zhoneCpeCondDhcpSrvListGroup": zhoneCpeCondDhcpSrvListGroup,
       "zhoneCpeCondDhcpSrvGroup": zhoneCpeCondDhcpSrvGroup,
       "zhoneCpeCmdGroup": zhoneCpeCmdGroup,
       "zhoneCpeLldpMedPolicyListGroup": zhoneCpeLldpMedPolicyListGroup,
       "zhoneCpeLldpMedPolicyGroup": zhoneCpeLldpMedPolicyGroup,
       "zhoneCpeAutoCfgRuleGroup": zhoneCpeAutoCfgRuleGroup,
       "zhoneCpeCfgGlobalSettingsGroup": zhoneCpeCfgGlobalSettingsGroup}
)
