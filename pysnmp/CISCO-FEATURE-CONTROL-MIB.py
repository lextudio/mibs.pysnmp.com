# SNMP MIB module (CISCO-FEATURE-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FEATURE-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:30 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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


# MODULE-IDENTITY

ciscoFeatureCtrlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 377)
)
ciscoFeatureCtrlMIB.setRevisions(
        ("2016-11-16 00:00",
         "2016-10-25 00:00",
         "2016-03-11 00:00",
         "2015-10-09 00:00",
         "2014-12-24 00:00",
         "2014-04-09 00:00",
         "2013-07-29 00:00",
         "2013-05-28 00:00",
         "2012-03-22 00:00",
         "2011-06-09 00:00",
         "2009-08-11 00:00",
         "2008-12-05 00:00",
         "2008-06-27 00:00",
         "2008-06-12 00:00",
         "2008-03-13 00:00",
         "2007-05-04 00:00",
         "2007-01-22 00:00",
         "2005-12-27 00:00",
         "2004-12-28 00:00",
         "2004-07-06 00:00",
         "2003-11-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoOptionalFeature(Integer32, TextualConvention):
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
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              200,
              264,
              9875)
        )
    )
    namedValues = NamedValues(
        *(("amt", 35),
          ("analytics", 161),
          ("assocMgr", 79),
          ("bashShell", 153),
          ("bbu", 130),
          ("bfd", 87),
          ("bfdApp", 88),
          ("bgp", 25),
          ("bulkStat", 129),
          ("catena", 173),
          ("cimServer", 58),
          ("cloudDiscovery", 20),
          ("cluster", 32),
          ("cmm", 124),
          ("copp", 49),
          ("dciTunnelInterop", 167),
          ("dhcpSnooping", 40),
          ("dmm", 62),
          ("dot1x", 36),
          ("dpt", 165),
          ("dpvm", 18),
          ("drap", 86),
          ("eigrp", 30),
          ("elo", 9875),
          ("ethPortSec", 46),
          ("ethernetNpv", 105),
          ("evb", 132),
          ("evc", 151),
          ("evfp", 68),
          ("evmed", 138),
          ("evpn", 157),
          ("ewise", 112),
          ("extenedCredit", 19),
          ("fabricAccess", 126),
          ("fabricBinding", 9),
          ("fabricTelemetry", 168),
          ("fcip", 2),
          ("fcoe", 66),
          ("fcsp", 3),
          ("fdmi", 123),
          ("fex", 89),
          ("ficon", 4),
          ("flexlink", 109),
          ("glbp", 39),
          ("hmm", 135),
          ("hsrp", 41),
          ("httpServer", 75),
          ("icam", 172),
          ("igmp", 27),
          ("ike", 11),
          ("imp", 150),
          ("ioa", 72),
          ("ipPool", 102),
          ("ipSec", 13),
          ("ipp", 162),
          ("isapi", 54),
          ("iscsi", 5),
          ("iscsiInterfaceVsanMembership", 10),
          ("isis", 21),
          ("isisL2", 57),
          ("isisOtv", 64),
          ("isns", 12),
          ("itd", 144),
          ("itronMcastAgent", 118),
          ("ivr", 1),
          ("l2nac", 38),
          ("l2vpn", 85),
          ("l3vpn", 99),
          ("lacp", 34),
          ("ldap", 92),
          ("ldbmgr", 171),
          ("ldp", 82),
          ("licensePlr", 174),
          ("licenseSmart", 163),
          ("lisp", 47),
          ("lldp", 80),
          ("mcecm", 51),
          ("mld", 156),
          ("mplsMgr", 95),
          ("mplsOam", 84),
          ("mplsSegmentRouting", 160),
          ("mplsStatic", 149),
          ("msdp", 28),
          ("mvpn", 101),
          ("mvrp", 137),
          ("nSegMgr", 139),
          ("nasb", 61),
          ("nat", 127),
          ("netSift", 56),
          ("nfm", 53),
          ("ngMvpn", 134),
          ("ngmvpn", 166),
          ("ngoam", 155),
          ("niv", 110),
          ("npiv", 16),
          ("npv", 37),
          ("ntp", 125),
          ("nxapi", 143),
          ("nxdb", 154),
          ("nxschema", 148),
          ("oim", 94),
          ("onep", 113),
          ("openFlow", 159),
          ("orib", 65),
          ("ospf", 22),
          ("ospfV3", 23),
          ("otv", 59),
          ("pbr", 52),
          ("pim", 26),
          ("pim6", 29),
          ("plb", 169),
          ("pmn", 164),
          ("poap", 200),
          ("poe", 108),
          ("pong", 90),
          ("portSecurity", 8),
          ("portTracker", 14),
          ("pppManager", 117),
          ("privilege", 93),
          ("ptp", 152),
          ("pvlan", 44),
          ("qosManager", 7),
          ("rip", 24),
          ("rise", 116),
          ("rsvp", 81),
          ("rtp", 91),
          ("sanExtTuner", 17),
          ("sanTap", 60),
          ("scadaGw", 107),
          ("scheduler", 15),
          ("scp", 97),
          ("sdv", 31),
          ("segmentation", 120),
          ("sflow", 264),
          ("sfm", 71),
          ("sftp", 98),
          ("siaServiceBroker", 67),
          ("siaSve", 77),
          ("slaR", 115),
          ("slaS", 114),
          ("smartChannel", 158),
          ("sme", 33),
          ("sol", 141),
          ("splitter", 70),
          ("sshServer", 74),
          ("svi", 42),
          ("tacacs", 6),
          ("te", 83),
          ("telnetServer", 73),
          ("trustSec", 48),
          ("tunnelManager", 45),
          ("u2rib", 63),
          ("udld", 50),
          ("ulib", 96),
          ("umfb", 104),
          ("uufb", 103),
          ("vTracker", 122),
          ("vem", 111),
          ("vff", 140),
          ("vlanVnSeg", 128),
          ("vmTracker", 145),
          ("vmis", 170),
          ("vmm", 43),
          ("vnSegment", 131),
          ("vrrp", 55),
          ("vrrpv3", 121),
          ("vsmAggregation", 119),
          ("vtp", 69),
          ("vxlan", 136),
          ("wccp", 76),
          ("wccpClient", 106),
          ("xcvrFreq", 78),
          ("xosFeatureTest", 146),
          ("xosMIFeatureTest", 147))
    )



class CiscoOptionalFeatureSet(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("fabric", 7),
          ("fcoe", 1),
          ("fcoenpv", 8),
          ("fex", 3),
          ("l2mp", 2),
          ("mpls", 4))
    )



class CiscoFeatureAction(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("allow", 6),
          ("disable", 3),
          ("disallow", 7),
          ("enable", 2),
          ("install", 4),
          ("noOp", 1),
          ("uninstall", 5))
    )



class CiscoFeatureStatus(Integer32, TextualConvention):
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
        *(("disabled", 3),
          ("enabled", 2),
          ("enabledNotRunning", 6),
          ("installed", 4),
          ("uninstalled", 5),
          ("unknown", 1))
    )



class CiscoFeatureActionResult(Integer32, TextualConvention):
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
        *(("actionFailed", 3),
          ("actionInProgress", 4),
          ("actionSuccess", 2),
          ("none", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoFeatureCtrlMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoFeatureCtrlMIBNotifs = _CiscoFeatureCtrlMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 0)
)
_CiscoFeatureCtrlMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFeatureCtrlMIBObjects = _CiscoFeatureCtrlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1)
)
_CfcFeature_ObjectIdentity = ObjectIdentity
cfcFeature = _CfcFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1)
)
_CfcFeatureCtrlTable_Object = MibTable
cfcFeatureCtrlTable = _CfcFeatureCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfcFeatureCtrlTable.setStatus("deprecated")
_CfcFeatureCtrlEntry_Object = MibTableRow
cfcFeatureCtrlEntry = _CfcFeatureCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 1, 1)
)
cfcFeatureCtrlEntry.setIndexNames(
    (0, "CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlIndex"),
)
if mibBuilder.loadTexts:
    cfcFeatureCtrlEntry.setStatus("deprecated")
_CfcFeatureCtrlIndex_Type = CiscoOptionalFeature
_CfcFeatureCtrlIndex_Object = MibTableColumn
cfcFeatureCtrlIndex = _CfcFeatureCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 1, 1, 1),
    _CfcFeatureCtrlIndex_Type()
)
cfcFeatureCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfcFeatureCtrlIndex.setStatus("deprecated")


class _CfcFeatureCtrlName_Type(SnmpAdminString):
    """Custom type cfcFeatureCtrlName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CfcFeatureCtrlName_Type.__name__ = "SnmpAdminString"
_CfcFeatureCtrlName_Object = MibTableColumn
cfcFeatureCtrlName = _CfcFeatureCtrlName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 1, 1, 2),
    _CfcFeatureCtrlName_Type()
)
cfcFeatureCtrlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcFeatureCtrlName.setStatus("deprecated")
_CfcFeatureCtrlAction_Type = CiscoFeatureAction
_CfcFeatureCtrlAction_Object = MibTableColumn
cfcFeatureCtrlAction = _CfcFeatureCtrlAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 1, 1, 3),
    _CfcFeatureCtrlAction_Type()
)
cfcFeatureCtrlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcFeatureCtrlAction.setStatus("deprecated")
_CfcFeatureCtrlLastAction_Type = CiscoFeatureAction
_CfcFeatureCtrlLastAction_Object = MibTableColumn
cfcFeatureCtrlLastAction = _CfcFeatureCtrlLastAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 1, 1, 4),
    _CfcFeatureCtrlLastAction_Type()
)
cfcFeatureCtrlLastAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcFeatureCtrlLastAction.setStatus("deprecated")
_CfcFeatureCtrlLastActionResult_Type = CiscoFeatureActionResult
_CfcFeatureCtrlLastActionResult_Object = MibTableColumn
cfcFeatureCtrlLastActionResult = _CfcFeatureCtrlLastActionResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 1, 1, 5),
    _CfcFeatureCtrlLastActionResult_Type()
)
cfcFeatureCtrlLastActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcFeatureCtrlLastActionResult.setStatus("deprecated")
_CfcFeatureCtrlLastFailureReason_Type = SnmpAdminString
_CfcFeatureCtrlLastFailureReason_Object = MibTableColumn
cfcFeatureCtrlLastFailureReason = _CfcFeatureCtrlLastFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 1, 1, 6),
    _CfcFeatureCtrlLastFailureReason_Type()
)
cfcFeatureCtrlLastFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcFeatureCtrlLastFailureReason.setStatus("deprecated")
_CfcFeatureCtrlOpStatus_Type = CiscoFeatureStatus
_CfcFeatureCtrlOpStatus_Object = MibTableColumn
cfcFeatureCtrlOpStatus = _CfcFeatureCtrlOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 1, 1, 7),
    _CfcFeatureCtrlOpStatus_Type()
)
cfcFeatureCtrlOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcFeatureCtrlOpStatus.setStatus("deprecated")
_CfcFeatureCtrlOpStatusReason_Type = SnmpAdminString
_CfcFeatureCtrlOpStatusReason_Object = MibTableColumn
cfcFeatureCtrlOpStatusReason = _CfcFeatureCtrlOpStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 1, 1, 8),
    _CfcFeatureCtrlOpStatusReason_Type()
)
cfcFeatureCtrlOpStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcFeatureCtrlOpStatusReason.setStatus("deprecated")
_CfcFeatureCtrl2Table_Object = MibTable
cfcFeatureCtrl2Table = _CfcFeatureCtrl2Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cfcFeatureCtrl2Table.setStatus("current")
_CfcFeatureCtrl2Entry_Object = MibTableRow
cfcFeatureCtrl2Entry = _CfcFeatureCtrl2Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 2, 1)
)
cfcFeatureCtrl2Entry.setIndexNames(
    (0, "CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlIndex2"),
    (0, "CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlInstanceNum2"),
)
if mibBuilder.loadTexts:
    cfcFeatureCtrl2Entry.setStatus("current")
_CfcFeatureCtrlIndex2_Type = CiscoOptionalFeature
_CfcFeatureCtrlIndex2_Object = MibTableColumn
cfcFeatureCtrlIndex2 = _CfcFeatureCtrlIndex2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 2, 1, 1),
    _CfcFeatureCtrlIndex2_Type()
)
cfcFeatureCtrlIndex2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfcFeatureCtrlIndex2.setStatus("current")
_CfcFeatureCtrlInstanceNum2_Type = Unsigned32
_CfcFeatureCtrlInstanceNum2_Object = MibTableColumn
cfcFeatureCtrlInstanceNum2 = _CfcFeatureCtrlInstanceNum2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 2, 1, 2),
    _CfcFeatureCtrlInstanceNum2_Type()
)
cfcFeatureCtrlInstanceNum2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfcFeatureCtrlInstanceNum2.setStatus("current")


class _CfcFeatureCtrlName2_Type(SnmpAdminString):
    """Custom type cfcFeatureCtrlName2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CfcFeatureCtrlName2_Type.__name__ = "SnmpAdminString"
_CfcFeatureCtrlName2_Object = MibTableColumn
cfcFeatureCtrlName2 = _CfcFeatureCtrlName2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 2, 1, 3),
    _CfcFeatureCtrlName2_Type()
)
cfcFeatureCtrlName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcFeatureCtrlName2.setStatus("current")
_CfcFeatureCtrlAction2_Type = CiscoFeatureAction
_CfcFeatureCtrlAction2_Object = MibTableColumn
cfcFeatureCtrlAction2 = _CfcFeatureCtrlAction2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 2, 1, 4),
    _CfcFeatureCtrlAction2_Type()
)
cfcFeatureCtrlAction2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcFeatureCtrlAction2.setStatus("current")
_CfcFeatureCtrlLastAction2_Type = CiscoFeatureAction
_CfcFeatureCtrlLastAction2_Object = MibTableColumn
cfcFeatureCtrlLastAction2 = _CfcFeatureCtrlLastAction2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 2, 1, 5),
    _CfcFeatureCtrlLastAction2_Type()
)
cfcFeatureCtrlLastAction2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcFeatureCtrlLastAction2.setStatus("current")
_CfcFeatureCtrlLastActionResult2_Type = CiscoFeatureActionResult
_CfcFeatureCtrlLastActionResult2_Object = MibTableColumn
cfcFeatureCtrlLastActionResult2 = _CfcFeatureCtrlLastActionResult2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 2, 1, 6),
    _CfcFeatureCtrlLastActionResult2_Type()
)
cfcFeatureCtrlLastActionResult2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcFeatureCtrlLastActionResult2.setStatus("current")
_CfcFeatureCtrlLastFailureReason2_Type = SnmpAdminString
_CfcFeatureCtrlLastFailureReason2_Object = MibTableColumn
cfcFeatureCtrlLastFailureReason2 = _CfcFeatureCtrlLastFailureReason2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 2, 1, 7),
    _CfcFeatureCtrlLastFailureReason2_Type()
)
cfcFeatureCtrlLastFailureReason2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcFeatureCtrlLastFailureReason2.setStatus("current")
_CfcFeatureCtrlOpStatus2_Type = CiscoFeatureStatus
_CfcFeatureCtrlOpStatus2_Object = MibTableColumn
cfcFeatureCtrlOpStatus2 = _CfcFeatureCtrlOpStatus2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 2, 1, 8),
    _CfcFeatureCtrlOpStatus2_Type()
)
cfcFeatureCtrlOpStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcFeatureCtrlOpStatus2.setStatus("current")
_CfcFeatureCtrlOpStatusReason2_Type = SnmpAdminString
_CfcFeatureCtrlOpStatusReason2_Object = MibTableColumn
cfcFeatureCtrlOpStatusReason2 = _CfcFeatureCtrlOpStatusReason2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 2, 1, 9),
    _CfcFeatureCtrlOpStatusReason2_Type()
)
cfcFeatureCtrlOpStatusReason2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcFeatureCtrlOpStatusReason2.setStatus("current")


class _CfcFeatureCtrlTag2_Type(SnmpAdminString):
    """Custom type cfcFeatureCtrlTag2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CfcFeatureCtrlTag2_Type.__name__ = "SnmpAdminString"
_CfcFeatureCtrlTag2_Object = MibTableColumn
cfcFeatureCtrlTag2 = _CfcFeatureCtrlTag2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 2, 1, 10),
    _CfcFeatureCtrlTag2_Type()
)
cfcFeatureCtrlTag2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcFeatureCtrlTag2.setStatus("current")
_CfcFeatureSetTable_Object = MibTable
cfcFeatureSetTable = _CfcFeatureSetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cfcFeatureSetTable.setStatus("current")
_CfcFeatureSetEntry_Object = MibTableRow
cfcFeatureSetEntry = _CfcFeatureSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 3, 1)
)
cfcFeatureSetEntry.setIndexNames(
    (0, "CISCO-FEATURE-CONTROL-MIB", "cfcFeatureSetIndex"),
)
if mibBuilder.loadTexts:
    cfcFeatureSetEntry.setStatus("current")
_CfcFeatureSetIndex_Type = CiscoOptionalFeatureSet
_CfcFeatureSetIndex_Object = MibTableColumn
cfcFeatureSetIndex = _CfcFeatureSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 3, 1, 1),
    _CfcFeatureSetIndex_Type()
)
cfcFeatureSetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfcFeatureSetIndex.setStatus("current")
_CfcFeatureSetName_Type = SnmpAdminString
_CfcFeatureSetName_Object = MibTableColumn
cfcFeatureSetName = _CfcFeatureSetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 3, 1, 2),
    _CfcFeatureSetName_Type()
)
cfcFeatureSetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcFeatureSetName.setStatus("current")
_CfcFeatureSetAction_Type = CiscoFeatureAction
_CfcFeatureSetAction_Object = MibTableColumn
cfcFeatureSetAction = _CfcFeatureSetAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 3, 1, 3),
    _CfcFeatureSetAction_Type()
)
cfcFeatureSetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcFeatureSetAction.setStatus("current")
_CfcFeatureSetLastAction_Type = CiscoFeatureAction
_CfcFeatureSetLastAction_Object = MibTableColumn
cfcFeatureSetLastAction = _CfcFeatureSetLastAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 3, 1, 4),
    _CfcFeatureSetLastAction_Type()
)
cfcFeatureSetLastAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcFeatureSetLastAction.setStatus("current")
_CfcFeatureSetLastActionResult_Type = CiscoFeatureActionResult
_CfcFeatureSetLastActionResult_Object = MibTableColumn
cfcFeatureSetLastActionResult = _CfcFeatureSetLastActionResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 3, 1, 5),
    _CfcFeatureSetLastActionResult_Type()
)
cfcFeatureSetLastActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcFeatureSetLastActionResult.setStatus("current")
_CfcFeatureSetLastFailureReason_Type = SnmpAdminString
_CfcFeatureSetLastFailureReason_Object = MibTableColumn
cfcFeatureSetLastFailureReason = _CfcFeatureSetLastFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 3, 1, 6),
    _CfcFeatureSetLastFailureReason_Type()
)
cfcFeatureSetLastFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcFeatureSetLastFailureReason.setStatus("current")
_CfcFeatureSetOpStatus_Type = CiscoFeatureStatus
_CfcFeatureSetOpStatus_Object = MibTableColumn
cfcFeatureSetOpStatus = _CfcFeatureSetOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 3, 1, 7),
    _CfcFeatureSetOpStatus_Type()
)
cfcFeatureSetOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcFeatureSetOpStatus.setStatus("current")
_CfcFeatureSetOpStatusReason_Type = SnmpAdminString
_CfcFeatureSetOpStatusReason_Object = MibTableColumn
cfcFeatureSetOpStatusReason = _CfcFeatureSetOpStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 3, 1, 8),
    _CfcFeatureSetOpStatusReason_Type()
)
cfcFeatureSetOpStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcFeatureSetOpStatusReason.setStatus("current")
_CfcNotifControl_ObjectIdentity = ObjectIdentity
cfcNotifControl = _CfcNotifControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 2)
)


class _CfcFeatureSetNotifEnable_Type(TruthValue):
    """Custom type cfcFeatureSetNotifEnable based on TruthValue"""


_CfcFeatureSetNotifEnable_Object = MibScalar
cfcFeatureSetNotifEnable = _CfcFeatureSetNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 2, 1),
    _CfcFeatureSetNotifEnable_Type()
)
cfcFeatureSetNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcFeatureSetNotifEnable.setStatus("current")
_CiscoFeatureCtrlMIBConformance_ObjectIdentity = ObjectIdentity
ciscoFeatureCtrlMIBConformance = _CiscoFeatureCtrlMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 2)
)
_CiscoFeatureCtrlMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoFeatureCtrlMIBCompliances = _CiscoFeatureCtrlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 2, 1)
)
_CiscoFeatureCtrlMIBGroups_ObjectIdentity = ObjectIdentity
ciscoFeatureCtrlMIBGroups = _CiscoFeatureCtrlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 2, 2)
)

# Managed Objects groups

cfcFeatureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 2, 2, 1)
)
cfcFeatureGroup.setObjects(
      *(("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlName"),
        ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlAction"),
        ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlLastAction"),
        ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlLastActionResult"),
        ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlLastFailureReason"),
        ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlOpStatus"),
        ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlOpStatusReason"))
)
if mibBuilder.loadTexts:
    cfcFeatureGroup.setStatus("deprecated")

cfcFeatureGroupRev = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 2, 2, 3)
)
cfcFeatureGroupRev.setObjects(
      *(("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlName2"),
        ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlTag2"),
        ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlAction2"),
        ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlLastAction2"),
        ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlLastActionResult2"),
        ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlLastFailureReason2"),
        ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlOpStatus2"),
        ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlOpStatusReason2"))
)
if mibBuilder.loadTexts:
    cfcFeatureGroupRev.setStatus("current")

cfcFeatureSetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 2, 2, 5)
)
cfcFeatureSetGroup.setObjects(
      *(("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureSetName"),
        ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureSetAction"),
        ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureSetLastAction"),
        ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureSetLastActionResult"),
        ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureSetLastFailureReason"),
        ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureSetOpStatus"),
        ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureSetOpStatusReason"))
)
if mibBuilder.loadTexts:
    cfcFeatureSetGroup.setStatus("current")

cfcFeatureSetNotificationCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 2, 2, 6)
)
cfcFeatureSetNotificationCtrlGroup.setObjects(
    ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureSetNotifEnable")
)
if mibBuilder.loadTexts:
    cfcFeatureSetNotificationCtrlGroup.setStatus("current")


# Notification objects

ciscoFeatureOpStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 0, 1)
)
ciscoFeatureOpStatusChange.setObjects(
    ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlOpStatus")
)
if mibBuilder.loadTexts:
    ciscoFeatureOpStatusChange.setStatus(
        "deprecated"
    )

ciscoFeatOpStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 0, 2)
)
ciscoFeatOpStatusChange.setObjects(
    ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlOpStatus2")
)
if mibBuilder.loadTexts:
    ciscoFeatOpStatusChange.setStatus(
        "current"
    )

ciscoFeatureSetOpStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 0, 3)
)
ciscoFeatureSetOpStatusChange.setObjects(
    ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureSetOpStatus")
)
if mibBuilder.loadTexts:
    ciscoFeatureSetOpStatusChange.setStatus(
        "current"
    )


# Notifications groups

cfcNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 2, 2, 2)
)
cfcNotificationGroup.setObjects(
    ("CISCO-FEATURE-CONTROL-MIB", "ciscoFeatureOpStatusChange")
)
if mibBuilder.loadTexts:
    cfcNotificationGroup.setStatus(
        "deprecated"
    )

cfcNotificationGroupRev = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 2, 2, 4)
)
cfcNotificationGroupRev.setObjects(
    ("CISCO-FEATURE-CONTROL-MIB", "ciscoFeatOpStatusChange")
)
if mibBuilder.loadTexts:
    cfcNotificationGroupRev.setStatus(
        "current"
    )

cfcFeatureSetNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 2, 2, 7)
)
cfcFeatureSetNotificationGroup.setObjects(
    ("CISCO-FEATURE-CONTROL-MIB", "ciscoFeatureSetOpStatusChange")
)
if mibBuilder.loadTexts:
    cfcFeatureSetNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoFeatureCtrlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoFeatureCtrlMIBCompliance.setStatus(
        "deprecated"
    )

ciscoFeatureCtrlMIBComplianceRev = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoFeatureCtrlMIBComplianceRev.setStatus(
        "deprecated"
    )

ciscoFeatureSetCtrlMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 377, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoFeatureSetCtrlMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FEATURE-CONTROL-MIB",
    **{"CiscoOptionalFeature": CiscoOptionalFeature,
       "CiscoOptionalFeatureSet": CiscoOptionalFeatureSet,
       "CiscoFeatureAction": CiscoFeatureAction,
       "CiscoFeatureStatus": CiscoFeatureStatus,
       "CiscoFeatureActionResult": CiscoFeatureActionResult,
       "ciscoFeatureCtrlMIB": ciscoFeatureCtrlMIB,
       "ciscoFeatureCtrlMIBNotifs": ciscoFeatureCtrlMIBNotifs,
       "ciscoFeatureOpStatusChange": ciscoFeatureOpStatusChange,
       "ciscoFeatOpStatusChange": ciscoFeatOpStatusChange,
       "ciscoFeatureSetOpStatusChange": ciscoFeatureSetOpStatusChange,
       "ciscoFeatureCtrlMIBObjects": ciscoFeatureCtrlMIBObjects,
       "cfcFeature": cfcFeature,
       "cfcFeatureCtrlTable": cfcFeatureCtrlTable,
       "cfcFeatureCtrlEntry": cfcFeatureCtrlEntry,
       "cfcFeatureCtrlIndex": cfcFeatureCtrlIndex,
       "cfcFeatureCtrlName": cfcFeatureCtrlName,
       "cfcFeatureCtrlAction": cfcFeatureCtrlAction,
       "cfcFeatureCtrlLastAction": cfcFeatureCtrlLastAction,
       "cfcFeatureCtrlLastActionResult": cfcFeatureCtrlLastActionResult,
       "cfcFeatureCtrlLastFailureReason": cfcFeatureCtrlLastFailureReason,
       "cfcFeatureCtrlOpStatus": cfcFeatureCtrlOpStatus,
       "cfcFeatureCtrlOpStatusReason": cfcFeatureCtrlOpStatusReason,
       "cfcFeatureCtrl2Table": cfcFeatureCtrl2Table,
       "cfcFeatureCtrl2Entry": cfcFeatureCtrl2Entry,
       "cfcFeatureCtrlIndex2": cfcFeatureCtrlIndex2,
       "cfcFeatureCtrlInstanceNum2": cfcFeatureCtrlInstanceNum2,
       "cfcFeatureCtrlName2": cfcFeatureCtrlName2,
       "cfcFeatureCtrlAction2": cfcFeatureCtrlAction2,
       "cfcFeatureCtrlLastAction2": cfcFeatureCtrlLastAction2,
       "cfcFeatureCtrlLastActionResult2": cfcFeatureCtrlLastActionResult2,
       "cfcFeatureCtrlLastFailureReason2": cfcFeatureCtrlLastFailureReason2,
       "cfcFeatureCtrlOpStatus2": cfcFeatureCtrlOpStatus2,
       "cfcFeatureCtrlOpStatusReason2": cfcFeatureCtrlOpStatusReason2,
       "cfcFeatureCtrlTag2": cfcFeatureCtrlTag2,
       "cfcFeatureSetTable": cfcFeatureSetTable,
       "cfcFeatureSetEntry": cfcFeatureSetEntry,
       "cfcFeatureSetIndex": cfcFeatureSetIndex,
       "cfcFeatureSetName": cfcFeatureSetName,
       "cfcFeatureSetAction": cfcFeatureSetAction,
       "cfcFeatureSetLastAction": cfcFeatureSetLastAction,
       "cfcFeatureSetLastActionResult": cfcFeatureSetLastActionResult,
       "cfcFeatureSetLastFailureReason": cfcFeatureSetLastFailureReason,
       "cfcFeatureSetOpStatus": cfcFeatureSetOpStatus,
       "cfcFeatureSetOpStatusReason": cfcFeatureSetOpStatusReason,
       "cfcNotifControl": cfcNotifControl,
       "cfcFeatureSetNotifEnable": cfcFeatureSetNotifEnable,
       "ciscoFeatureCtrlMIBConformance": ciscoFeatureCtrlMIBConformance,
       "ciscoFeatureCtrlMIBCompliances": ciscoFeatureCtrlMIBCompliances,
       "ciscoFeatureCtrlMIBCompliance": ciscoFeatureCtrlMIBCompliance,
       "ciscoFeatureCtrlMIBComplianceRev": ciscoFeatureCtrlMIBComplianceRev,
       "ciscoFeatureSetCtrlMIBComplianceRev1": ciscoFeatureSetCtrlMIBComplianceRev1,
       "ciscoFeatureCtrlMIBGroups": ciscoFeatureCtrlMIBGroups,
       "cfcFeatureGroup": cfcFeatureGroup,
       "cfcNotificationGroup": cfcNotificationGroup,
       "cfcFeatureGroupRev": cfcFeatureGroupRev,
       "cfcNotificationGroupRev": cfcNotificationGroupRev,
       "cfcFeatureSetGroup": cfcFeatureSetGroup,
       "cfcFeatureSetNotificationCtrlGroup": cfcFeatureSetNotificationCtrlGroup,
       "cfcFeatureSetNotificationGroup": cfcFeatureSetNotificationGroup}
)
