# SNMP MIB module (RBN-L2TP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-L2TP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:13 2024
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

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rbnL2tpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28)
)
rbnL2tpMib.setRevisions(
        ("2009-04-20 00:00",
         "2005-02-28 00:00",
         "2004-02-04 00:00",
         "2003-04-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AuthType(Integer32, TextualConvention):
    status = "current"
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
        *(("chap", 2),
          ("chapPap", 3),
          ("other", 0),
          ("pap", 1))
    )



class LacLnsType(Integer32, TextualConvention):
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
        *(("lac", 2),
          ("lacLns", 4),
          ("lns", 3),
          ("other", 1))
    )



class TunStateType(Integer32, TextualConvention):
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
        *(("created", 3),
          ("deleted", 1),
          ("established", 7),
          ("idle", 2),
          ("invalid", 0),
          ("waitAAA", 4),
          ("waitCtlConn", 6),
          ("waitCtlReply", 5),
          ("waitRouteUp", 8))
    )



class CtlErrType(Integer32, TextualConvention):
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("authFailed", 23),
          ("avp2big", 14),
          ("avp2long", 6),
          ("avpLen", 11),
          ("avpUnknown", 7),
          ("badAvpLen", 15),
          ("badCmType", 5),
          ("badMsgType", 33),
          ("badSCCCN", 32),
          ("badSCCRP", 30),
          ("badSCCRQna", 29),
          ("badVers", 21),
          ("badcrpsesi", 25),
          ("cantUnhide", 10),
          ("cdnBadid", 26),
          ("cdnThrottle", 36),
          ("ctlrunt", 0),
          ("dataRunt", 28),
          ("droppkt", 4),
          ("dupIcrq", 31),
          ("dupSCCRQ", 2),
          ("duppkt", 3),
          ("hdr2long", 1),
          ("iccnBadid", 27),
          ("invalidAvp", 13),
          ("maxRexmts", 19),
          ("missAvp", 12),
          ("mtype000", 9),
          ("noChapRsp", 22),
          ("none", 255),
          ("remWndoful", 18),
          ("remXmtState", 35),
          ("rexmt", 16),
          ("sccrqColide", 20),
          ("sccrqSteal", 34),
          ("scksnderr", 17),
          ("sesExists", 24),
          ("typeNot1st", 8))
    )



class EthEncapType(Integer32, TextualConvention):
    status = "current"
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
        *(("ethMulti", 2),
          ("ethPpoe", 1),
          ("ethernet", 3),
          ("other", 0))
    )



class DNISType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dnis", 1),
          ("dnisonly", 2),
          ("other", 0))
    )



# MIB Managed Objects in the order of their OIDs

_RbnL2tpMibNotifications_ObjectIdentity = ObjectIdentity
rbnL2tpMibNotifications = _RbnL2tpMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 0)
)
_RbnL2tpMibObjects_ObjectIdentity = ObjectIdentity
rbnL2tpMibObjects = _RbnL2tpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1)
)
_RbnL2tpPeerCfgTable_Object = MibTable
rbnL2tpPeerCfgTable = _RbnL2tpPeerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1)
)
if mibBuilder.loadTexts:
    rbnL2tpPeerCfgTable.setStatus("current")
_RbnL2tpPeerCfgEntry_Object = MibTableRow
rbnL2tpPeerCfgEntry = _RbnL2tpPeerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1)
)
rbnL2tpPeerCfgEntry.setIndexNames(
    (1, "RBN-L2TP-MIB", "rbnL2tpMibPeerName"),
)
if mibBuilder.loadTexts:
    rbnL2tpPeerCfgEntry.setStatus("current")


class _RbnL2tpMibPeerName_Type(SnmpAdminString):
    """Custom type rbnL2tpMibPeerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RbnL2tpMibPeerName_Type.__name__ = "SnmpAdminString"
_RbnL2tpMibPeerName_Object = MibTableColumn
rbnL2tpMibPeerName = _RbnL2tpMibPeerName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 1),
    _RbnL2tpMibPeerName_Type()
)
rbnL2tpMibPeerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnL2tpMibPeerName.setStatus("current")


class _RbnL2tpPCfgMedia_Type(SnmpAdminString):
    """Custom type rbnL2tpPCfgMedia based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbnL2tpPCfgMedia_Type.__name__ = "SnmpAdminString"
_RbnL2tpPCfgMedia_Object = MibTableColumn
rbnL2tpPCfgMedia = _RbnL2tpPCfgMedia_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 2),
    _RbnL2tpPCfgMedia_Type()
)
rbnL2tpPCfgMedia.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnL2tpPCfgMedia.setStatus("current")


class _RbnL2tpPCfgVendor_Type(SnmpAdminString):
    """Custom type rbnL2tpPCfgVendor based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_RbnL2tpPCfgVendor_Type.__name__ = "SnmpAdminString"
_RbnL2tpPCfgVendor_Object = MibTableColumn
rbnL2tpPCfgVendor = _RbnL2tpPCfgVendor_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 3),
    _RbnL2tpPCfgVendor_Type()
)
rbnL2tpPCfgVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCfgVendor.setStatus("current")
_RbnL2tpPCfgRev_Type = Unsigned32
_RbnL2tpPCfgRev_Object = MibTableColumn
rbnL2tpPCfgRev = _RbnL2tpPCfgRev_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 4),
    _RbnL2tpPCfgRev_Type()
)
rbnL2tpPCfgRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCfgRev.setStatus("current")


class _RbnL2tpPCfgHostName_Type(SnmpAdminString):
    """Custom type rbnL2tpPCfgHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RbnL2tpPCfgHostName_Type.__name__ = "SnmpAdminString"
_RbnL2tpPCfgHostName_Object = MibTableColumn
rbnL2tpPCfgHostName = _RbnL2tpPCfgHostName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 5),
    _RbnL2tpPCfgHostName_Type()
)
rbnL2tpPCfgHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCfgHostName.setStatus("current")
_RbnL2tpPCfgRadius_Type = TruthValue
_RbnL2tpPCfgRadius_Object = MibTableColumn
rbnL2tpPCfgRadius = _RbnL2tpPCfgRadius_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 6),
    _RbnL2tpPCfgRadius_Type()
)
rbnL2tpPCfgRadius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCfgRadius.setStatus("current")
_RbnL2tpPCfgRemIPAddType_Type = InetAddressType
_RbnL2tpPCfgRemIPAddType_Object = MibTableColumn
rbnL2tpPCfgRemIPAddType = _RbnL2tpPCfgRemIPAddType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 7),
    _RbnL2tpPCfgRemIPAddType_Type()
)
rbnL2tpPCfgRemIPAddType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCfgRemIPAddType.setStatus("current")
_RbnL2tpPCfgRemIPAdd_Type = InetAddress
_RbnL2tpPCfgRemIPAdd_Object = MibTableColumn
rbnL2tpPCfgRemIPAdd = _RbnL2tpPCfgRemIPAdd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 8),
    _RbnL2tpPCfgRemIPAdd_Type()
)
rbnL2tpPCfgRemIPAdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnL2tpPCfgRemIPAdd.setStatus("current")
_RbnL2tpPCfgStatic_Type = TruthValue
_RbnL2tpPCfgStatic_Object = MibTableColumn
rbnL2tpPCfgStatic = _RbnL2tpPCfgStatic_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 9),
    _RbnL2tpPCfgStatic_Type()
)
rbnL2tpPCfgStatic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnL2tpPCfgStatic.setStatus("current")
_RbnL2tpPCfgLocalIPAddType_Type = InetAddressType
_RbnL2tpPCfgLocalIPAddType_Object = MibTableColumn
rbnL2tpPCfgLocalIPAddType = _RbnL2tpPCfgLocalIPAddType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 10),
    _RbnL2tpPCfgLocalIPAddType_Type()
)
rbnL2tpPCfgLocalIPAddType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCfgLocalIPAddType.setStatus("current")
_RbnL2tpPCfgLocalIPAdd_Type = InetAddress
_RbnL2tpPCfgLocalIPAdd_Object = MibTableColumn
rbnL2tpPCfgLocalIPAdd = _RbnL2tpPCfgLocalIPAdd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 11),
    _RbnL2tpPCfgLocalIPAdd_Type()
)
rbnL2tpPCfgLocalIPAdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnL2tpPCfgLocalIPAdd.setStatus("current")
_RbnL2tpPCfgMode_Type = LacLnsType
_RbnL2tpPCfgMode_Object = MibTableColumn
rbnL2tpPCfgMode = _RbnL2tpPCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 12),
    _RbnL2tpPCfgMode_Type()
)
rbnL2tpPCfgMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnL2tpPCfgMode.setStatus("current")
_RbnL2tpPCfgMaxTunnels_Type = Gauge32
_RbnL2tpPCfgMaxTunnels_Object = MibTableColumn
rbnL2tpPCfgMaxTunnels = _RbnL2tpPCfgMaxTunnels_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 14),
    _RbnL2tpPCfgMaxTunnels_Type()
)
rbnL2tpPCfgMaxTunnels.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnL2tpPCfgMaxTunnels.setStatus("current")
_RbnL2tpPCfgMaxSesPerTun_Type = Gauge32
_RbnL2tpPCfgMaxSesPerTun_Object = MibTableColumn
rbnL2tpPCfgMaxSesPerTun = _RbnL2tpPCfgMaxSesPerTun_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 15),
    _RbnL2tpPCfgMaxSesPerTun_Type()
)
rbnL2tpPCfgMaxSesPerTun.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnL2tpPCfgMaxSesPerTun.setStatus("current")
_RbnL2tpPCfgCtlRetranCnt_Type = Counter32
_RbnL2tpPCfgCtlRetranCnt_Object = MibTableColumn
rbnL2tpPCfgCtlRetranCnt = _RbnL2tpPCfgCtlRetranCnt_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 16),
    _RbnL2tpPCfgCtlRetranCnt_Type()
)
rbnL2tpPCfgCtlRetranCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCfgCtlRetranCnt.setStatus("current")


class _RbnL2tpPCfgCtlRetranTO_Type(Unsigned32):
    """Custom type rbnL2tpPCfgCtlRetranTO based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RbnL2tpPCfgCtlRetranTO_Type.__name__ = "Unsigned32"
_RbnL2tpPCfgCtlRetranTO_Object = MibTableColumn
rbnL2tpPCfgCtlRetranTO = _RbnL2tpPCfgCtlRetranTO_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 17),
    _RbnL2tpPCfgCtlRetranTO_Type()
)
rbnL2tpPCfgCtlRetranTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnL2tpPCfgCtlRetranTO.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpPCfgCtlRetranTO.setUnits("seconds")
_RbnL2tpPCfgSessAuth_Type = AuthType
_RbnL2tpPCfgSessAuth_Object = MibTableColumn
rbnL2tpPCfgSessAuth = _RbnL2tpPCfgSessAuth_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 18),
    _RbnL2tpPCfgSessAuth_Type()
)
rbnL2tpPCfgSessAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnL2tpPCfgSessAuth.setStatus("current")


class _RbnL2tpPCfgCtlWin_Type(Gauge32):
    """Custom type rbnL2tpPCfgCtlWin based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RbnL2tpPCfgCtlWin_Type.__name__ = "Gauge32"
_RbnL2tpPCfgCtlWin_Object = MibTableColumn
rbnL2tpPCfgCtlWin = _RbnL2tpPCfgCtlWin_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 19),
    _RbnL2tpPCfgCtlWin_Type()
)
rbnL2tpPCfgCtlWin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnL2tpPCfgCtlWin.setStatus("current")
_RbnL2tpPCfgDNIS_Type = DNISType
_RbnL2tpPCfgDNIS_Object = MibTableColumn
rbnL2tpPCfgDNIS = _RbnL2tpPCfgDNIS_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 20),
    _RbnL2tpPCfgDNIS_Type()
)
rbnL2tpPCfgDNIS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnL2tpPCfgDNIS.setStatus("current")
_RbnL2tpPCfgPoliceRate_Type = Unsigned32
_RbnL2tpPCfgPoliceRate_Object = MibTableColumn
rbnL2tpPCfgPoliceRate = _RbnL2tpPCfgPoliceRate_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 21),
    _RbnL2tpPCfgPoliceRate_Type()
)
rbnL2tpPCfgPoliceRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnL2tpPCfgPoliceRate.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpPCfgPoliceRate.setUnits("kbps")
_RbnL2tpPCfgPoliceBurst_Type = Unsigned32
_RbnL2tpPCfgPoliceBurst_Object = MibTableColumn
rbnL2tpPCfgPoliceBurst = _RbnL2tpPCfgPoliceBurst_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 22),
    _RbnL2tpPCfgPoliceBurst_Type()
)
rbnL2tpPCfgPoliceBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnL2tpPCfgPoliceBurst.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpPCfgPoliceBurst.setUnits("kbps")
_RbnL2tpPCfgLimitRate_Type = Unsigned32
_RbnL2tpPCfgLimitRate_Object = MibTableColumn
rbnL2tpPCfgLimitRate = _RbnL2tpPCfgLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 23),
    _RbnL2tpPCfgLimitRate_Type()
)
rbnL2tpPCfgLimitRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnL2tpPCfgLimitRate.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpPCfgLimitRate.setUnits("kbps")
_RbnL2tpPCfgLimitBurst_Type = Unsigned32
_RbnL2tpPCfgLimitBurst_Object = MibTableColumn
rbnL2tpPCfgLimitBurst = _RbnL2tpPCfgLimitBurst_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 24),
    _RbnL2tpPCfgLimitBurst_Type()
)
rbnL2tpPCfgLimitBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnL2tpPCfgLimitBurst.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpPCfgLimitBurst.setUnits("kbps")
_RbnL2tpPCfgGroup_Type = SnmpAdminString
_RbnL2tpPCfgGroup_Object = MibTableColumn
rbnL2tpPCfgGroup = _RbnL2tpPCfgGroup_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 25),
    _RbnL2tpPCfgGroup_Type()
)
rbnL2tpPCfgGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnL2tpPCfgGroup.setStatus("current")
_RbnL2tpPCfgPref_Type = Unsigned32
_RbnL2tpPCfgPref_Object = MibTableColumn
rbnL2tpPCfgPref = _RbnL2tpPCfgPref_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 26),
    _RbnL2tpPCfgPref_Type()
)
rbnL2tpPCfgPref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnL2tpPCfgPref.setStatus("current")


class _RbnL2tpPCfgPasswd_Type(SnmpAdminString):
    """Custom type rbnL2tpPCfgPasswd based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RbnL2tpPCfgPasswd_Type.__name__ = "SnmpAdminString"
_RbnL2tpPCfgPasswd_Object = MibTableColumn
rbnL2tpPCfgPasswd = _RbnL2tpPCfgPasswd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 27),
    _RbnL2tpPCfgPasswd_Type()
)
rbnL2tpPCfgPasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnL2tpPCfgPasswd.setStatus("current")


class _RbnL2tpPCfgHelloTimer_Type(Unsigned32):
    """Custom type rbnL2tpPCfgHelloTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_RbnL2tpPCfgHelloTimer_Type.__name__ = "Unsigned32"
_RbnL2tpPCfgHelloTimer_Object = MibTableColumn
rbnL2tpPCfgHelloTimer = _RbnL2tpPCfgHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 28),
    _RbnL2tpPCfgHelloTimer_Type()
)
rbnL2tpPCfgHelloTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnL2tpPCfgHelloTimer.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpPCfgHelloTimer.setUnits("seconds")
_RbnL2tpPCfgRecQue_Type = TruthValue
_RbnL2tpPCfgRecQue_Object = MibTableColumn
rbnL2tpPCfgRecQue = _RbnL2tpPCfgRecQue_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 29),
    _RbnL2tpPCfgRecQue_Type()
)
rbnL2tpPCfgRecQue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCfgRecQue.setStatus("current")


class _RbnL2tpPCfgSessContext_Type(SnmpAdminString):
    """Custom type rbnL2tpPCfgSessContext based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RbnL2tpPCfgSessContext_Type.__name__ = "SnmpAdminString"
_RbnL2tpPCfgSessContext_Object = MibTableColumn
rbnL2tpPCfgSessContext = _RbnL2tpPCfgSessContext_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 30),
    _RbnL2tpPCfgSessContext_Type()
)
rbnL2tpPCfgSessContext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnL2tpPCfgSessContext.setStatus("current")


class _RbnL2tpPCfgSessService_Type(SnmpAdminString):
    """Custom type rbnL2tpPCfgSessService based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RbnL2tpPCfgSessService_Type.__name__ = "SnmpAdminString"
_RbnL2tpPCfgSessService_Object = MibTableColumn
rbnL2tpPCfgSessService = _RbnL2tpPCfgSessService_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 31),
    _RbnL2tpPCfgSessService_Type()
)
rbnL2tpPCfgSessService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnL2tpPCfgSessService.setStatus("current")
_RbnL2tpPCfgEthEncap_Type = EthEncapType
_RbnL2tpPCfgEthEncap_Object = MibTableColumn
rbnL2tpPCfgEthEncap = _RbnL2tpPCfgEthEncap_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 32),
    _RbnL2tpPCfgEthEncap_Type()
)
rbnL2tpPCfgEthEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnL2tpPCfgEthEncap.setStatus("current")


class _RbnL2tpPCfgEthSession_Type(SnmpAdminString):
    """Custom type rbnL2tpPCfgEthSession based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RbnL2tpPCfgEthSession_Type.__name__ = "SnmpAdminString"
_RbnL2tpPCfgEthSession_Object = MibTableColumn
rbnL2tpPCfgEthSession = _RbnL2tpPCfgEthSession_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 33),
    _RbnL2tpPCfgEthSession_Type()
)
rbnL2tpPCfgEthSession.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnL2tpPCfgEthSession.setStatus("current")
_RbnL2tpPCfgTunnelCount_Type = Counter32
_RbnL2tpPCfgTunnelCount_Object = MibTableColumn
rbnL2tpPCfgTunnelCount = _RbnL2tpPCfgTunnelCount_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 34),
    _RbnL2tpPCfgTunnelCount_Type()
)
rbnL2tpPCfgTunnelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCfgTunnelCount.setStatus("current")
_RbnL2tpPCfgTunCtlErrs_Type = Counter32
_RbnL2tpPCfgTunCtlErrs_Object = MibTableColumn
rbnL2tpPCfgTunCtlErrs = _RbnL2tpPCfgTunCtlErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 35),
    _RbnL2tpPCfgTunCtlErrs_Type()
)
rbnL2tpPCfgTunCtlErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCfgTunCtlErrs.setStatus("current")
_RbnL2tpPCfgSessionCount_Type = Counter32
_RbnL2tpPCfgSessionCount_Object = MibTableColumn
rbnL2tpPCfgSessionCount = _RbnL2tpPCfgSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 1, 1, 36),
    _RbnL2tpPCfgSessionCount_Type()
)
rbnL2tpPCfgSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCfgSessionCount.setStatus("current")
_RbnL2tpTunnelCfgTable_Object = MibTable
rbnL2tpTunnelCfgTable = _RbnL2tpTunnelCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 2)
)
if mibBuilder.loadTexts:
    rbnL2tpTunnelCfgTable.setStatus("current")
_RbnL2tpTunnelCfgEntry_Object = MibTableRow
rbnL2tpTunnelCfgEntry = _RbnL2tpTunnelCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 2, 1)
)
rbnL2tpTunnelCfgEntry.setIndexNames(
    (0, "RBN-L2TP-MIB", "rbnL2tpMibTunnelID"),
)
if mibBuilder.loadTexts:
    rbnL2tpTunnelCfgEntry.setStatus("current")


class _RbnL2tpMibTunnelID_Type(Unsigned32):
    """Custom type rbnL2tpMibTunnelID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RbnL2tpMibTunnelID_Type.__name__ = "Unsigned32"
_RbnL2tpMibTunnelID_Object = MibTableColumn
rbnL2tpMibTunnelID = _RbnL2tpMibTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 2, 1, 1),
    _RbnL2tpMibTunnelID_Type()
)
rbnL2tpMibTunnelID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnL2tpMibTunnelID.setStatus("current")


class _RbnL2tpTCfgTunnelNm_Type(SnmpAdminString):
    """Custom type rbnL2tpTCfgTunnelNm based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RbnL2tpTCfgTunnelNm_Type.__name__ = "SnmpAdminString"
_RbnL2tpTCfgTunnelNm_Object = MibTableColumn
rbnL2tpTCfgTunnelNm = _RbnL2tpTCfgTunnelNm_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 2, 1, 2),
    _RbnL2tpTCfgTunnelNm_Type()
)
rbnL2tpTCfgTunnelNm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCfgTunnelNm.setStatus("current")


class _RbnL2tpTCfgPeerName_Type(SnmpAdminString):
    """Custom type rbnL2tpTCfgPeerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RbnL2tpTCfgPeerName_Type.__name__ = "SnmpAdminString"
_RbnL2tpTCfgPeerName_Object = MibTableColumn
rbnL2tpTCfgPeerName = _RbnL2tpTCfgPeerName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 2, 1, 3),
    _RbnL2tpTCfgPeerName_Type()
)
rbnL2tpTCfgPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCfgPeerName.setStatus("current")
_RbnL2tpTCfgTunCtlErrs_Type = Counter32
_RbnL2tpTCfgTunCtlErrs_Object = MibTableColumn
rbnL2tpTCfgTunCtlErrs = _RbnL2tpTCfgTunCtlErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 2, 1, 4),
    _RbnL2tpTCfgTunCtlErrs_Type()
)
rbnL2tpTCfgTunCtlErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCfgTunCtlErrs.setStatus("current")
_RbnL2tpTCfgLastCtlErr_Type = CtlErrType
_RbnL2tpTCfgLastCtlErr_Object = MibTableColumn
rbnL2tpTCfgLastCtlErr = _RbnL2tpTCfgLastCtlErr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 2, 1, 5),
    _RbnL2tpTCfgLastCtlErr_Type()
)
rbnL2tpTCfgLastCtlErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCfgLastCtlErr.setStatus("current")
_RbnL2tpTCfgLastCErrTime_Type = DateAndTime
_RbnL2tpTCfgLastCErrTime_Object = MibTableColumn
rbnL2tpTCfgLastCErrTime = _RbnL2tpTCfgLastCErrTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 2, 1, 6),
    _RbnL2tpTCfgLastCErrTime_Type()
)
rbnL2tpTCfgLastCErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCfgLastCErrTime.setStatus("current")
_RbnL2tpTCfgTunDataErrs_Type = Counter32
_RbnL2tpTCfgTunDataErrs_Object = MibTableColumn
rbnL2tpTCfgTunDataErrs = _RbnL2tpTCfgTunDataErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 2, 1, 7),
    _RbnL2tpTCfgTunDataErrs_Type()
)
rbnL2tpTCfgTunDataErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCfgTunDataErrs.setStatus("current")
_RbnL2tpTCfgLastDataErr_Type = Unsigned32
_RbnL2tpTCfgLastDataErr_Object = MibTableColumn
rbnL2tpTCfgLastDataErr = _RbnL2tpTCfgLastDataErr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 2, 1, 8),
    _RbnL2tpTCfgLastDataErr_Type()
)
rbnL2tpTCfgLastDataErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCfgLastDataErr.setStatus("current")
_RbnL2tpTCfgLastDErrTime_Type = DateAndTime
_RbnL2tpTCfgLastDErrTime_Object = MibTableColumn
rbnL2tpTCfgLastDErrTime = _RbnL2tpTCfgLastDErrTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 2, 1, 9),
    _RbnL2tpTCfgLastDErrTime_Type()
)
rbnL2tpTCfgLastDErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCfgLastDErrTime.setStatus("current")
_RbnL2tpTCfgSessionCount_Type = Gauge32
_RbnL2tpTCfgSessionCount_Object = MibTableColumn
rbnL2tpTCfgSessionCount = _RbnL2tpTCfgSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 2, 1, 10),
    _RbnL2tpTCfgSessionCount_Type()
)
rbnL2tpTCfgSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCfgSessionCount.setStatus("current")
_RbnL2tpTCfgTotActSessions_Type = Counter32
_RbnL2tpTCfgTotActSessions_Object = MibTableColumn
rbnL2tpTCfgTotActSessions = _RbnL2tpTCfgTotActSessions_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 2, 1, 11),
    _RbnL2tpTCfgTotActSessions_Type()
)
rbnL2tpTCfgTotActSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCfgTotActSessions.setStatus("current")
_RbnL2tpTCfgActSessCnt_Type = Gauge32
_RbnL2tpTCfgActSessCnt_Object = MibTableColumn
rbnL2tpTCfgActSessCnt = _RbnL2tpTCfgActSessCnt_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 2, 1, 12),
    _RbnL2tpTCfgActSessCnt_Type()
)
rbnL2tpTCfgActSessCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCfgActSessCnt.setStatus("current")
_RbnL2tpTCfgTotFailSessions_Type = Counter32
_RbnL2tpTCfgTotFailSessions_Object = MibTableColumn
rbnL2tpTCfgTotFailSessions = _RbnL2tpTCfgTotFailSessions_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 2, 1, 13),
    _RbnL2tpTCfgTotFailSessions_Type()
)
rbnL2tpTCfgTotFailSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCfgTotFailSessions.setStatus("current")
_RbnL2tpMibTunnelState_Type = TunStateType
_RbnL2tpMibTunnelState_Object = MibTableColumn
rbnL2tpMibTunnelState = _RbnL2tpMibTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 2, 1, 14),
    _RbnL2tpMibTunnelState_Type()
)
rbnL2tpMibTunnelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpMibTunnelState.setStatus("current")


class _RbnL2tpTCfgRemoteTunnelID_Type(Unsigned32):
    """Custom type rbnL2tpTCfgRemoteTunnelID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RbnL2tpTCfgRemoteTunnelID_Type.__name__ = "Unsigned32"
_RbnL2tpTCfgRemoteTunnelID_Object = MibTableColumn
rbnL2tpTCfgRemoteTunnelID = _RbnL2tpTCfgRemoteTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 2, 1, 15),
    _RbnL2tpTCfgRemoteTunnelID_Type()
)
rbnL2tpTCfgRemoteTunnelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCfgRemoteTunnelID.setStatus("current")


class _RbnL2tpTCfgTunnelContext_Type(SnmpAdminString):
    """Custom type rbnL2tpTCfgTunnelContext based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RbnL2tpTCfgTunnelContext_Type.__name__ = "SnmpAdminString"
_RbnL2tpTCfgTunnelContext_Object = MibTableColumn
rbnL2tpTCfgTunnelContext = _RbnL2tpTCfgTunnelContext_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 2, 1, 16),
    _RbnL2tpTCfgTunnelContext_Type()
)
rbnL2tpTCfgTunnelContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCfgTunnelContext.setStatus("current")
_RbnL2tpPeerCntTable_Object = MibTable
rbnL2tpPeerCntTable = _RbnL2tpPeerCntTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 4)
)
if mibBuilder.loadTexts:
    rbnL2tpPeerCntTable.setStatus("current")
_RbnL2tpPeerCntEntry_Object = MibTableRow
rbnL2tpPeerCntEntry = _RbnL2tpPeerCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 4, 1)
)
rbnL2tpPeerCntEntry.setIndexNames(
    (1, "RBN-L2TP-MIB", "rbnL2tpMibPeerName"),
)
if mibBuilder.loadTexts:
    rbnL2tpPeerCntEntry.setStatus("current")
_RbnL2tpPCDataPktSent_Type = Counter32
_RbnL2tpPCDataPktSent_Object = MibTableColumn
rbnL2tpPCDataPktSent = _RbnL2tpPCDataPktSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 4, 1, 1),
    _RbnL2tpPCDataPktSent_Type()
)
rbnL2tpPCDataPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCDataPktSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpPCDataPktSent.setUnits("packets")
_RbnL2tpPCDataPktRx_Type = Counter32
_RbnL2tpPCDataPktRx_Object = MibTableColumn
rbnL2tpPCDataPktRx = _RbnL2tpPCDataPktRx_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 4, 1, 2),
    _RbnL2tpPCDataPktRx_Type()
)
rbnL2tpPCDataPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCDataPktRx.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpPCDataPktRx.setUnits("packets")
_RbnL2tpPCDataByteSent_Type = Counter32
_RbnL2tpPCDataByteSent_Object = MibTableColumn
rbnL2tpPCDataByteSent = _RbnL2tpPCDataByteSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 4, 1, 3),
    _RbnL2tpPCDataByteSent_Type()
)
rbnL2tpPCDataByteSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCDataByteSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpPCDataByteSent.setUnits("bytes")
_RbnL2tpPCDataByteRx_Type = Counter32
_RbnL2tpPCDataByteRx_Object = MibTableColumn
rbnL2tpPCDataByteRx = _RbnL2tpPCDataByteRx_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 4, 1, 4),
    _RbnL2tpPCDataByteRx_Type()
)
rbnL2tpPCDataByteRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCDataByteRx.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpPCDataByteRx.setUnits("bytes")
_RbnL2tpPCCtlPktSent_Type = Counter32
_RbnL2tpPCCtlPktSent_Object = MibTableColumn
rbnL2tpPCCtlPktSent = _RbnL2tpPCCtlPktSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 4, 1, 5),
    _RbnL2tpPCCtlPktSent_Type()
)
rbnL2tpPCCtlPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCCtlPktSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpPCCtlPktSent.setUnits("packets")
_RbnL2tpPCCtlPktRx_Type = Counter32
_RbnL2tpPCCtlPktRx_Object = MibTableColumn
rbnL2tpPCCtlPktRx = _RbnL2tpPCCtlPktRx_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 4, 1, 6),
    _RbnL2tpPCCtlPktRx_Type()
)
rbnL2tpPCCtlPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCCtlPktRx.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpPCCtlPktRx.setUnits("packets")
_RbnL2tpPCCtlByteSent_Type = Counter32
_RbnL2tpPCCtlByteSent_Object = MibTableColumn
rbnL2tpPCCtlByteSent = _RbnL2tpPCCtlByteSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 4, 1, 7),
    _RbnL2tpPCCtlByteSent_Type()
)
rbnL2tpPCCtlByteSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCCtlByteSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpPCCtlByteSent.setUnits("bytes")
_RbnL2tpPCCtlByteRx_Type = Counter32
_RbnL2tpPCCtlByteRx_Object = MibTableColumn
rbnL2tpPCCtlByteRx = _RbnL2tpPCCtlByteRx_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 4, 1, 8),
    _RbnL2tpPCCtlByteRx_Type()
)
rbnL2tpPCCtlByteRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCCtlByteRx.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpPCCtlByteRx.setUnits("bytes")
_RbnL2tpPCPolicePktDrop_Type = Counter32
_RbnL2tpPCPolicePktDrop_Object = MibTableColumn
rbnL2tpPCPolicePktDrop = _RbnL2tpPCPolicePktDrop_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 4, 1, 9),
    _RbnL2tpPCPolicePktDrop_Type()
)
rbnL2tpPCPolicePktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCPolicePktDrop.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpPCPolicePktDrop.setUnits("packets")
_RbnL2tpPCRatePktDrop_Type = Counter32
_RbnL2tpPCRatePktDrop_Object = MibTableColumn
rbnL2tpPCRatePktDrop = _RbnL2tpPCRatePktDrop_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 4, 1, 10),
    _RbnL2tpPCRatePktDrop_Type()
)
rbnL2tpPCRatePktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCRatePktDrop.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpPCRatePktDrop.setUnits("packets")
_RbnL2tpPCTxSCCRQCnt_Type = Counter32
_RbnL2tpPCTxSCCRQCnt_Object = MibTableColumn
rbnL2tpPCTxSCCRQCnt = _RbnL2tpPCTxSCCRQCnt_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 4, 1, 11),
    _RbnL2tpPCTxSCCRQCnt_Type()
)
rbnL2tpPCTxSCCRQCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCTxSCCRQCnt.setStatus("current")
_RbnL2tpPCRxSCCRQCnt_Type = Counter32
_RbnL2tpPCRxSCCRQCnt_Object = MibTableColumn
rbnL2tpPCRxSCCRQCnt = _RbnL2tpPCRxSCCRQCnt_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 4, 1, 12),
    _RbnL2tpPCRxSCCRQCnt_Type()
)
rbnL2tpPCRxSCCRQCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCRxSCCRQCnt.setStatus("current")
_RbnL2tpPCActTunnels_Type = Gauge32
_RbnL2tpPCActTunnels_Object = MibTableColumn
rbnL2tpPCActTunnels = _RbnL2tpPCActTunnels_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 4, 1, 13),
    _RbnL2tpPCActTunnels_Type()
)
rbnL2tpPCActTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCActTunnels.setStatus("current")
_RbnL2tpPCTunnelCtlErr_Type = Counter32
_RbnL2tpPCTunnelCtlErr_Object = MibTableColumn
rbnL2tpPCTunnelCtlErr = _RbnL2tpPCTunnelCtlErr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 4, 1, 14),
    _RbnL2tpPCTunnelCtlErr_Type()
)
rbnL2tpPCTunnelCtlErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCTunnelCtlErr.setStatus("current")
_RbnL2tpPCSessionCount_Type = Gauge32
_RbnL2tpPCSessionCount_Object = MibTableColumn
rbnL2tpPCSessionCount = _RbnL2tpPCSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 4, 1, 15),
    _RbnL2tpPCSessionCount_Type()
)
rbnL2tpPCSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCSessionCount.setStatus("current")
_RbnL2tpPCTunnelDataErr_Type = Counter32
_RbnL2tpPCTunnelDataErr_Object = MibTableColumn
rbnL2tpPCTunnelDataErr = _RbnL2tpPCTunnelDataErr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 4, 1, 16),
    _RbnL2tpPCTunnelDataErr_Type()
)
rbnL2tpPCTunnelDataErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPCTunnelDataErr.setStatus("current")
_RbnL2tpTunnelCntTable_Object = MibTable
rbnL2tpTunnelCntTable = _RbnL2tpTunnelCntTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 5)
)
if mibBuilder.loadTexts:
    rbnL2tpTunnelCntTable.setStatus("current")
_RbnL2tpTunnelCntEntry_Object = MibTableRow
rbnL2tpTunnelCntEntry = _RbnL2tpTunnelCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 5, 1)
)
rbnL2tpTunnelCntEntry.setIndexNames(
    (0, "RBN-L2TP-MIB", "rbnL2tpMibTunnelID"),
)
if mibBuilder.loadTexts:
    rbnL2tpTunnelCntEntry.setStatus("current")
_RbnL2tpTCDataPktSent_Type = Counter32
_RbnL2tpTCDataPktSent_Object = MibTableColumn
rbnL2tpTCDataPktSent = _RbnL2tpTCDataPktSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 5, 1, 1),
    _RbnL2tpTCDataPktSent_Type()
)
rbnL2tpTCDataPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCDataPktSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpTCDataPktSent.setUnits("packets")
_RbnL2tpTCDataPktRcvd_Type = Counter32
_RbnL2tpTCDataPktRcvd_Object = MibTableColumn
rbnL2tpTCDataPktRcvd = _RbnL2tpTCDataPktRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 5, 1, 2),
    _RbnL2tpTCDataPktRcvd_Type()
)
rbnL2tpTCDataPktRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCDataPktRcvd.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpTCDataPktRcvd.setUnits("packets")
_RbnL2tpTCDataByteSent_Type = Counter32
_RbnL2tpTCDataByteSent_Object = MibTableColumn
rbnL2tpTCDataByteSent = _RbnL2tpTCDataByteSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 5, 1, 3),
    _RbnL2tpTCDataByteSent_Type()
)
rbnL2tpTCDataByteSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCDataByteSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpTCDataByteSent.setUnits("bytes")
_RbnL2tpTCDataByteRcvd_Type = Counter32
_RbnL2tpTCDataByteRcvd_Object = MibTableColumn
rbnL2tpTCDataByteRcvd = _RbnL2tpTCDataByteRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 5, 1, 4),
    _RbnL2tpTCDataByteRcvd_Type()
)
rbnL2tpTCDataByteRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCDataByteRcvd.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpTCDataByteRcvd.setUnits("bytes")
_RbnL2tpTCCntrlPktSent_Type = Counter32
_RbnL2tpTCCntrlPktSent_Object = MibTableColumn
rbnL2tpTCCntrlPktSent = _RbnL2tpTCCntrlPktSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 5, 1, 5),
    _RbnL2tpTCCntrlPktSent_Type()
)
rbnL2tpTCCntrlPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCCntrlPktSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpTCCntrlPktSent.setUnits("packets")
_RbnL2tpTCCntrlPktRcvd_Type = Counter32
_RbnL2tpTCCntrlPktRcvd_Object = MibTableColumn
rbnL2tpTCCntrlPktRcvd = _RbnL2tpTCCntrlPktRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 5, 1, 6),
    _RbnL2tpTCCntrlPktRcvd_Type()
)
rbnL2tpTCCntrlPktRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCCntrlPktRcvd.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpTCCntrlPktRcvd.setUnits("packets")
_RbnL2tpTCCntrlByteSent_Type = Counter32
_RbnL2tpTCCntrlByteSent_Object = MibTableColumn
rbnL2tpTCCntrlByteSent = _RbnL2tpTCCntrlByteSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 5, 1, 7),
    _RbnL2tpTCCntrlByteSent_Type()
)
rbnL2tpTCCntrlByteSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCCntrlByteSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpTCCntrlByteSent.setUnits("bytes")
_RbnL2tpTCCntrlByteRcvd_Type = Counter32
_RbnL2tpTCCntrlByteRcvd_Object = MibTableColumn
rbnL2tpTCCntrlByteRcvd = _RbnL2tpTCCntrlByteRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 5, 1, 8),
    _RbnL2tpTCCntrlByteRcvd_Type()
)
rbnL2tpTCCntrlByteRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCCntrlByteRcvd.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpTCCntrlByteRcvd.setUnits("bytes")
_RbnL2tpTCPolicePktDrop_Type = Counter32
_RbnL2tpTCPolicePktDrop_Object = MibTableColumn
rbnL2tpTCPolicePktDrop = _RbnL2tpTCPolicePktDrop_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 5, 1, 9),
    _RbnL2tpTCPolicePktDrop_Type()
)
rbnL2tpTCPolicePktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCPolicePktDrop.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpTCPolicePktDrop.setUnits("packets")
_RbnL2tpTCRatePktDrop_Type = Counter32
_RbnL2tpTCRatePktDrop_Object = MibTableColumn
rbnL2tpTCRatePktDrop = _RbnL2tpTCRatePktDrop_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 5, 1, 10),
    _RbnL2tpTCRatePktDrop_Type()
)
rbnL2tpTCRatePktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCRatePktDrop.setStatus("current")
if mibBuilder.loadTexts:
    rbnL2tpTCRatePktDrop.setUnits("packets")
_RbnL2tpTCCntrlErr_Type = Unsigned32
_RbnL2tpTCCntrlErr_Object = MibTableColumn
rbnL2tpTCCntrlErr = _RbnL2tpTCCntrlErr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 5, 1, 11),
    _RbnL2tpTCCntrlErr_Type()
)
rbnL2tpTCCntrlErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCCntrlErr.setStatus("current")
_RbnL2tpTCLastCtlErr_Type = CtlErrType
_RbnL2tpTCLastCtlErr_Object = MibTableColumn
rbnL2tpTCLastCtlErr = _RbnL2tpTCLastCtlErr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 5, 1, 12),
    _RbnL2tpTCLastCtlErr_Type()
)
rbnL2tpTCLastCtlErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCLastCtlErr.setStatus("current")
_RbnL2tpTCLastCtlErrTime_Type = DateAndTime
_RbnL2tpTCLastCtlErrTime_Object = MibTableColumn
rbnL2tpTCLastCtlErrTime = _RbnL2tpTCLastCtlErrTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 5, 1, 13),
    _RbnL2tpTCLastCtlErrTime_Type()
)
rbnL2tpTCLastCtlErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCLastCtlErrTime.setStatus("current")
_RbnL2tpTCMaxResendQ_Type = Gauge32
_RbnL2tpTCMaxResendQ_Object = MibTableColumn
rbnL2tpTCMaxResendQ = _RbnL2tpTCMaxResendQ_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 5, 1, 14),
    _RbnL2tpTCMaxResendQ_Type()
)
rbnL2tpTCMaxResendQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCMaxResendQ.setStatus("current")
_RbnL2tpTCMaxUnsentQ_Type = Gauge32
_RbnL2tpTCMaxUnsentQ_Object = MibTableColumn
rbnL2tpTCMaxUnsentQ = _RbnL2tpTCMaxUnsentQ_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 5, 1, 15),
    _RbnL2tpTCMaxUnsentQ_Type()
)
rbnL2tpTCMaxUnsentQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCMaxUnsentQ.setStatus("current")
_RbnL2tpTCCurResendQ_Type = Gauge32
_RbnL2tpTCCurResendQ_Object = MibTableColumn
rbnL2tpTCCurResendQ = _RbnL2tpTCCurResendQ_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 5, 1, 16),
    _RbnL2tpTCCurResendQ_Type()
)
rbnL2tpTCCurResendQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCCurResendQ.setStatus("current")
_RbnL2tpTCCurUnsentQ_Type = Gauge32
_RbnL2tpTCCurUnsentQ_Object = MibTableColumn
rbnL2tpTCCurUnsentQ = _RbnL2tpTCCurUnsentQ_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 5, 1, 17),
    _RbnL2tpTCCurUnsentQ_Type()
)
rbnL2tpTCCurUnsentQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCCurUnsentQ.setStatus("current")
_RbnL2tpTCCurWindow_Type = Gauge32
_RbnL2tpTCCurWindow_Object = MibTableColumn
rbnL2tpTCCurWindow = _RbnL2tpTCCurWindow_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 5, 1, 18),
    _RbnL2tpTCCurWindow_Type()
)
rbnL2tpTCCurWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpTCCurWindow.setStatus("current")
_RbnL2tpSessionCntTable_Object = MibTable
rbnL2tpSessionCntTable = _RbnL2tpSessionCntTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 6)
)
if mibBuilder.loadTexts:
    rbnL2tpSessionCntTable.setStatus("current")
_RbnL2tpSessionCntEntry_Object = MibTableRow
rbnL2tpSessionCntEntry = _RbnL2tpSessionCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 6, 1)
)
rbnL2tpSessionCntEntry.setIndexNames(
    (0, "RBN-L2TP-MIB", "rbnL2tpMibTunnelID"),
    (0, "RBN-L2TP-MIB", "rbnL2tpMibSessionID"),
)
if mibBuilder.loadTexts:
    rbnL2tpSessionCntEntry.setStatus("current")


class _RbnL2tpMibSessionID_Type(Unsigned32):
    """Custom type rbnL2tpMibSessionID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RbnL2tpMibSessionID_Type.__name__ = "Unsigned32"
_RbnL2tpMibSessionID_Object = MibTableColumn
rbnL2tpMibSessionID = _RbnL2tpMibSessionID_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 6, 1, 1),
    _RbnL2tpMibSessionID_Type()
)
rbnL2tpMibSessionID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnL2tpMibSessionID.setStatus("current")
_RbnL2tpSCPktSent_Type = Counter32
_RbnL2tpSCPktSent_Object = MibTableColumn
rbnL2tpSCPktSent = _RbnL2tpSCPktSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 6, 1, 2),
    _RbnL2tpSCPktSent_Type()
)
rbnL2tpSCPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpSCPktSent.setStatus("current")
_RbnL2tpSCPktRcvd_Type = Counter32
_RbnL2tpSCPktRcvd_Object = MibTableColumn
rbnL2tpSCPktRcvd = _RbnL2tpSCPktRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 6, 1, 3),
    _RbnL2tpSCPktRcvd_Type()
)
rbnL2tpSCPktRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpSCPktRcvd.setStatus("current")
_RbnL2tpSCByteSent_Type = Counter32
_RbnL2tpSCByteSent_Object = MibTableColumn
rbnL2tpSCByteSent = _RbnL2tpSCByteSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 6, 1, 4),
    _RbnL2tpSCByteSent_Type()
)
rbnL2tpSCByteSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpSCByteSent.setStatus("current")
_RbnL2tpSCByteRcvd_Type = Counter32
_RbnL2tpSCByteRcvd_Object = MibTableColumn
rbnL2tpSCByteRcvd = _RbnL2tpSCByteRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 6, 1, 5),
    _RbnL2tpSCByteRcvd_Type()
)
rbnL2tpSCByteRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpSCByteRcvd.setStatus("current")
_RbnL2tpSCMcastPktSent_Type = Counter64
_RbnL2tpSCMcastPktSent_Object = MibTableColumn
rbnL2tpSCMcastPktSent = _RbnL2tpSCMcastPktSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 6, 1, 6),
    _RbnL2tpSCMcastPktSent_Type()
)
rbnL2tpSCMcastPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpSCMcastPktSent.setStatus("current")
_RbnL2tpSCMcastPktRcvd_Type = Counter64
_RbnL2tpSCMcastPktRcvd_Object = MibTableColumn
rbnL2tpSCMcastPktRcvd = _RbnL2tpSCMcastPktRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 6, 1, 7),
    _RbnL2tpSCMcastPktRcvd_Type()
)
rbnL2tpSCMcastPktRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpSCMcastPktRcvd.setStatus("current")
_RbnL2tpSCMcastByteSent_Type = Counter64
_RbnL2tpSCMcastByteSent_Object = MibTableColumn
rbnL2tpSCMcastByteSent = _RbnL2tpSCMcastByteSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 6, 1, 8),
    _RbnL2tpSCMcastByteSent_Type()
)
rbnL2tpSCMcastByteSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpSCMcastByteSent.setStatus("current")
_RbnL2tpSCMcastByteRcvd_Type = Counter64
_RbnL2tpSCMcastByteRcvd_Object = MibTableColumn
rbnL2tpSCMcastByteRcvd = _RbnL2tpSCMcastByteRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 6, 1, 9),
    _RbnL2tpSCMcastByteRcvd_Type()
)
rbnL2tpSCMcastByteRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpSCMcastByteRcvd.setStatus("current")
_RbnL2tpMibTrapObj_ObjectIdentity = ObjectIdentity
rbnL2tpMibTrapObj = _RbnL2tpMibTrapObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 7)
)


class _RbnL2tpMibTunnelTrapContext_Type(SnmpAdminString):
    """Custom type rbnL2tpMibTunnelTrapContext based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RbnL2tpMibTunnelTrapContext_Type.__name__ = "SnmpAdminString"
_RbnL2tpMibTunnelTrapContext_Object = MibScalar
rbnL2tpMibTunnelTrapContext = _RbnL2tpMibTunnelTrapContext_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 7, 1),
    _RbnL2tpMibTunnelTrapContext_Type()
)
rbnL2tpMibTunnelTrapContext.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnL2tpMibTunnelTrapContext.setStatus("deprecated")
_RbnL2tpMibTunnelTrapState_Type = TruthValue
_RbnL2tpMibTunnelTrapState_Object = MibScalar
rbnL2tpMibTunnelTrapState = _RbnL2tpMibTunnelTrapState_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 7, 2),
    _RbnL2tpMibTunnelTrapState_Type()
)
rbnL2tpMibTunnelTrapState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnL2tpMibTunnelTrapState.setStatus("deprecated")


class _RbnL2tpMibDisableTrap_Type(TruthValue):
    """Custom type rbnL2tpMibDisableTrap based on TruthValue"""


_RbnL2tpMibDisableTrap_Object = MibScalar
rbnL2tpMibDisableTrap = _RbnL2tpMibDisableTrap_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 7, 3),
    _RbnL2tpMibDisableTrap_Type()
)
rbnL2tpMibDisableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnL2tpMibDisableTrap.setStatus("current")
_RbnL2tpPeerTunCfgTable_Object = MibTable
rbnL2tpPeerTunCfgTable = _RbnL2tpPeerTunCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 8)
)
if mibBuilder.loadTexts:
    rbnL2tpPeerTunCfgTable.setStatus("current")
_RbnL2tpPeerTunCfgEntry_Object = MibTableRow
rbnL2tpPeerTunCfgEntry = _RbnL2tpPeerTunCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 8, 1)
)
rbnL2tpPeerTunCfgEntry.setIndexNames(
    (0, "RBN-L2TP-MIB", "rbnL2tpMibPeerName"),
    (0, "RBN-L2TP-MIB", "rbnL2tpMibTunnelID"),
)
if mibBuilder.loadTexts:
    rbnL2tpPeerTunCfgEntry.setStatus("current")


class _RbnL2tpPTCfgTunnelRemoteID_Type(Unsigned32):
    """Custom type rbnL2tpPTCfgTunnelRemoteID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RbnL2tpPTCfgTunnelRemoteID_Type.__name__ = "Unsigned32"
_RbnL2tpPTCfgTunnelRemoteID_Object = MibTableColumn
rbnL2tpPTCfgTunnelRemoteID = _RbnL2tpPTCfgTunnelRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 8, 1, 1),
    _RbnL2tpPTCfgTunnelRemoteID_Type()
)
rbnL2tpPTCfgTunnelRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPTCfgTunnelRemoteID.setStatus("current")


class _RbnL2tpPTCfgTunnelLocalNm_Type(SnmpAdminString):
    """Custom type rbnL2tpPTCfgTunnelLocalNm based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RbnL2tpPTCfgTunnelLocalNm_Type.__name__ = "SnmpAdminString"
_RbnL2tpPTCfgTunnelLocalNm_Object = MibTableColumn
rbnL2tpPTCfgTunnelLocalNm = _RbnL2tpPTCfgTunnelLocalNm_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 8, 1, 2),
    _RbnL2tpPTCfgTunnelLocalNm_Type()
)
rbnL2tpPTCfgTunnelLocalNm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPTCfgTunnelLocalNm.setStatus("current")


class _RbnL2tpPTCfgTunnelRemoteNm_Type(SnmpAdminString):
    """Custom type rbnL2tpPTCfgTunnelRemoteNm based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RbnL2tpPTCfgTunnelRemoteNm_Type.__name__ = "SnmpAdminString"
_RbnL2tpPTCfgTunnelRemoteNm_Object = MibTableColumn
rbnL2tpPTCfgTunnelRemoteNm = _RbnL2tpPTCfgTunnelRemoteNm_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 8, 1, 3),
    _RbnL2tpPTCfgTunnelRemoteNm_Type()
)
rbnL2tpPTCfgTunnelRemoteNm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPTCfgTunnelRemoteNm.setStatus("current")


class _RbnL2tpPTCfgPeerLocalNm_Type(SnmpAdminString):
    """Custom type rbnL2tpPTCfgPeerLocalNm based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RbnL2tpPTCfgPeerLocalNm_Type.__name__ = "SnmpAdminString"
_RbnL2tpPTCfgPeerLocalNm_Object = MibTableColumn
rbnL2tpPTCfgPeerLocalNm = _RbnL2tpPTCfgPeerLocalNm_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 8, 1, 4),
    _RbnL2tpPTCfgPeerLocalNm_Type()
)
rbnL2tpPTCfgPeerLocalNm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPTCfgPeerLocalNm.setStatus("current")
_RbnL2tpPTCfgTunnelRemoteIPAddrType_Type = InetAddressType
_RbnL2tpPTCfgTunnelRemoteIPAddrType_Object = MibTableColumn
rbnL2tpPTCfgTunnelRemoteIPAddrType = _RbnL2tpPTCfgTunnelRemoteIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 8, 1, 5),
    _RbnL2tpPTCfgTunnelRemoteIPAddrType_Type()
)
rbnL2tpPTCfgTunnelRemoteIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPTCfgTunnelRemoteIPAddrType.setStatus("current")
_RbnL2tpPTCfgTunnelRemoteIPAddr_Type = InetAddress
_RbnL2tpPTCfgTunnelRemoteIPAddr_Object = MibTableColumn
rbnL2tpPTCfgTunnelRemoteIPAddr = _RbnL2tpPTCfgTunnelRemoteIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 8, 1, 6),
    _RbnL2tpPTCfgTunnelRemoteIPAddr_Type()
)
rbnL2tpPTCfgTunnelRemoteIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPTCfgTunnelRemoteIPAddr.setStatus("current")
_RbnL2tpPTCfgTunnelState_Type = TunStateType
_RbnL2tpPTCfgTunnelState_Object = MibTableColumn
rbnL2tpPTCfgTunnelState = _RbnL2tpPTCfgTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 8, 1, 7),
    _RbnL2tpPTCfgTunnelState_Type()
)
rbnL2tpPTCfgTunnelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPTCfgTunnelState.setStatus("current")


class _RbnL2tpPTCfgTunnelContext_Type(SnmpAdminString):
    """Custom type rbnL2tpPTCfgTunnelContext based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RbnL2tpPTCfgTunnelContext_Type.__name__ = "SnmpAdminString"
_RbnL2tpPTCfgTunnelContext_Object = MibTableColumn
rbnL2tpPTCfgTunnelContext = _RbnL2tpPTCfgTunnelContext_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 8, 1, 8),
    _RbnL2tpPTCfgTunnelContext_Type()
)
rbnL2tpPTCfgTunnelContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPTCfgTunnelContext.setStatus("current")
_RbnL2tpPTCfgSessionCount_Type = Gauge32
_RbnL2tpPTCfgSessionCount_Object = MibTableColumn
rbnL2tpPTCfgSessionCount = _RbnL2tpPTCfgSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 8, 1, 9),
    _RbnL2tpPTCfgSessionCount_Type()
)
rbnL2tpPTCfgSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPTCfgSessionCount.setStatus("current")
_RbnL2tpPTCfgActSessCnt_Type = Gauge32
_RbnL2tpPTCfgActSessCnt_Object = MibTableColumn
rbnL2tpPTCfgActSessCnt = _RbnL2tpPTCfgActSessCnt_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 8, 1, 10),
    _RbnL2tpPTCfgActSessCnt_Type()
)
rbnL2tpPTCfgActSessCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPTCfgActSessCnt.setStatus("current")
_RbnL2tpPTCfgTotActSessions_Type = Counter32
_RbnL2tpPTCfgTotActSessions_Object = MibTableColumn
rbnL2tpPTCfgTotActSessions = _RbnL2tpPTCfgTotActSessions_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 8, 1, 11),
    _RbnL2tpPTCfgTotActSessions_Type()
)
rbnL2tpPTCfgTotActSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPTCfgTotActSessions.setStatus("current")
_RbnL2tpPTCfgTotFailSessions_Type = Counter32
_RbnL2tpPTCfgTotFailSessions_Object = MibTableColumn
rbnL2tpPTCfgTotFailSessions = _RbnL2tpPTCfgTotFailSessions_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 1, 8, 1, 12),
    _RbnL2tpPTCfgTotFailSessions_Type()
)
rbnL2tpPTCfgTotFailSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2tpPTCfgTotFailSessions.setStatus("current")
_RbnL2tpMibConformance_ObjectIdentity = ObjectIdentity
rbnL2tpMibConformance = _RbnL2tpMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 2)
)
_RbnL2tpMibGroups_ObjectIdentity = ObjectIdentity
rbnL2tpMibGroups = _RbnL2tpMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 2, 1)
)
_RbnL2tpMibCompliances_ObjectIdentity = ObjectIdentity
rbnL2tpMibCompliances = _RbnL2tpMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 2, 2)
)

# Managed Objects groups

rbnL2tpMibPeerCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 2, 1, 1)
)
rbnL2tpMibPeerCfgGroup.setObjects(
      *(("RBN-L2TP-MIB", "rbnL2tpPCfgMedia"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgVendor"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgRev"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgHostName"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgRadius"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgRemIPAddType"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgRemIPAdd"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgStatic"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgLocalIPAddType"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgLocalIPAdd"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgMode"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgMaxTunnels"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgMaxSesPerTun"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgCtlRetranCnt"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgCtlRetranTO"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgSessAuth"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgCtlWin"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgDNIS"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgPoliceRate"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgPoliceBurst"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgLimitRate"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgLimitBurst"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgGroup"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgPref"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgPasswd"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgHelloTimer"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgRecQue"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgSessContext"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgSessService"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgEthEncap"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgEthSession"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgTunnelCount"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgTunCtlErrs"),
        ("RBN-L2TP-MIB", "rbnL2tpPCfgSessionCount"))
)
if mibBuilder.loadTexts:
    rbnL2tpMibPeerCfgGroup.setStatus("current")

rbnL2tpMibTunnelCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 2, 1, 2)
)
rbnL2tpMibTunnelCfgGroup.setObjects(
      *(("RBN-L2TP-MIB", "rbnL2tpTCfgTunnelNm"),
        ("RBN-L2TP-MIB", "rbnL2tpTCfgPeerName"),
        ("RBN-L2TP-MIB", "rbnL2tpTCfgTunCtlErrs"),
        ("RBN-L2TP-MIB", "rbnL2tpTCfgLastCtlErr"),
        ("RBN-L2TP-MIB", "rbnL2tpTCfgLastCErrTime"),
        ("RBN-L2TP-MIB", "rbnL2tpTCfgTunDataErrs"),
        ("RBN-L2TP-MIB", "rbnL2tpTCfgLastDataErr"),
        ("RBN-L2TP-MIB", "rbnL2tpTCfgLastDErrTime"),
        ("RBN-L2TP-MIB", "rbnL2tpTCfgSessionCount"),
        ("RBN-L2TP-MIB", "rbnL2tpTCfgTotActSessions"),
        ("RBN-L2TP-MIB", "rbnL2tpTCfgActSessCnt"),
        ("RBN-L2TP-MIB", "rbnL2tpTCfgTotFailSessions"),
        ("RBN-L2TP-MIB", "rbnL2tpMibTunnelState"),
        ("RBN-L2TP-MIB", "rbnL2tpTCfgRemoteTunnelID"),
        ("RBN-L2TP-MIB", "rbnL2tpTCfgTunnelContext"))
)
if mibBuilder.loadTexts:
    rbnL2tpMibTunnelCfgGroup.setStatus("current")

rbnL2tpMibPeerCntGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 2, 1, 3)
)
rbnL2tpMibPeerCntGroup.setObjects(
      *(("RBN-L2TP-MIB", "rbnL2tpPCDataPktSent"),
        ("RBN-L2TP-MIB", "rbnL2tpPCDataPktRx"),
        ("RBN-L2TP-MIB", "rbnL2tpPCDataByteSent"),
        ("RBN-L2TP-MIB", "rbnL2tpPCDataByteRx"),
        ("RBN-L2TP-MIB", "rbnL2tpPCCtlPktSent"),
        ("RBN-L2TP-MIB", "rbnL2tpPCCtlPktRx"),
        ("RBN-L2TP-MIB", "rbnL2tpPCCtlByteSent"),
        ("RBN-L2TP-MIB", "rbnL2tpPCCtlByteRx"),
        ("RBN-L2TP-MIB", "rbnL2tpPCPolicePktDrop"),
        ("RBN-L2TP-MIB", "rbnL2tpPCRatePktDrop"),
        ("RBN-L2TP-MIB", "rbnL2tpPCTxSCCRQCnt"),
        ("RBN-L2TP-MIB", "rbnL2tpPCRxSCCRQCnt"),
        ("RBN-L2TP-MIB", "rbnL2tpPCActTunnels"),
        ("RBN-L2TP-MIB", "rbnL2tpPCTunnelCtlErr"),
        ("RBN-L2TP-MIB", "rbnL2tpPCSessionCount"),
        ("RBN-L2TP-MIB", "rbnL2tpPCTunnelDataErr"))
)
if mibBuilder.loadTexts:
    rbnL2tpMibPeerCntGroup.setStatus("current")

rbnL2tpMibTunnelCntGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 2, 1, 4)
)
rbnL2tpMibTunnelCntGroup.setObjects(
      *(("RBN-L2TP-MIB", "rbnL2tpTCDataPktSent"),
        ("RBN-L2TP-MIB", "rbnL2tpTCDataPktRcvd"),
        ("RBN-L2TP-MIB", "rbnL2tpTCDataByteSent"),
        ("RBN-L2TP-MIB", "rbnL2tpTCDataByteRcvd"),
        ("RBN-L2TP-MIB", "rbnL2tpTCCntrlPktSent"),
        ("RBN-L2TP-MIB", "rbnL2tpTCCntrlPktRcvd"),
        ("RBN-L2TP-MIB", "rbnL2tpTCCntrlByteSent"),
        ("RBN-L2TP-MIB", "rbnL2tpTCCntrlByteRcvd"),
        ("RBN-L2TP-MIB", "rbnL2tpTCPolicePktDrop"),
        ("RBN-L2TP-MIB", "rbnL2tpTCRatePktDrop"),
        ("RBN-L2TP-MIB", "rbnL2tpTCCntrlErr"),
        ("RBN-L2TP-MIB", "rbnL2tpTCLastCtlErr"),
        ("RBN-L2TP-MIB", "rbnL2tpTCLastCtlErrTime"),
        ("RBN-L2TP-MIB", "rbnL2tpTCMaxResendQ"),
        ("RBN-L2TP-MIB", "rbnL2tpTCMaxUnsentQ"),
        ("RBN-L2TP-MIB", "rbnL2tpTCCurResendQ"),
        ("RBN-L2TP-MIB", "rbnL2tpTCCurUnsentQ"),
        ("RBN-L2TP-MIB", "rbnL2tpTCCurWindow"))
)
if mibBuilder.loadTexts:
    rbnL2tpMibTunnelCntGroup.setStatus("current")

rbnL2tpMibSessionCntGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 2, 1, 5)
)
rbnL2tpMibSessionCntGroup.setObjects(
      *(("RBN-L2TP-MIB", "rbnL2tpSCPktSent"),
        ("RBN-L2TP-MIB", "rbnL2tpSCPktRcvd"),
        ("RBN-L2TP-MIB", "rbnL2tpSCByteSent"),
        ("RBN-L2TP-MIB", "rbnL2tpSCByteRcvd"),
        ("RBN-L2TP-MIB", "rbnL2tpSCMcastPktSent"),
        ("RBN-L2TP-MIB", "rbnL2tpSCMcastPktRcvd"),
        ("RBN-L2TP-MIB", "rbnL2tpSCMcastByteSent"),
        ("RBN-L2TP-MIB", "rbnL2tpSCMcastByteRcvd"))
)
if mibBuilder.loadTexts:
    rbnL2tpMibSessionCntGroup.setStatus("current")

rbnL2tpMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 2, 1, 7)
)
rbnL2tpMibGroup.setObjects(
      *(("RBN-L2TP-MIB", "rbnL2tpMibTunnelTrapContext"),
        ("RBN-L2TP-MIB", "rbnL2tpMibTunnelTrapState"),
        ("RBN-L2TP-MIB", "rbnL2tpMibDisableTrap"))
)
if mibBuilder.loadTexts:
    rbnL2tpMibGroup.setStatus("deprecated")

rbnL2tpMibGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 2, 1, 9)
)
rbnL2tpMibGroup2.setObjects(
    ("RBN-L2TP-MIB", "rbnL2tpMibDisableTrap")
)
if mibBuilder.loadTexts:
    rbnL2tpMibGroup2.setStatus("current")

rbnL2tpMibPeerTunCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 2, 1, 11)
)
rbnL2tpMibPeerTunCfgGroup.setObjects(
      *(("RBN-L2TP-MIB", "rbnL2tpPTCfgTunnelRemoteID"),
        ("RBN-L2TP-MIB", "rbnL2tpPTCfgTunnelLocalNm"),
        ("RBN-L2TP-MIB", "rbnL2tpPTCfgTunnelRemoteNm"),
        ("RBN-L2TP-MIB", "rbnL2tpPTCfgPeerLocalNm"),
        ("RBN-L2TP-MIB", "rbnL2tpPTCfgTunnelRemoteIPAddrType"),
        ("RBN-L2TP-MIB", "rbnL2tpPTCfgTunnelRemoteIPAddr"),
        ("RBN-L2TP-MIB", "rbnL2tpPTCfgTunnelState"),
        ("RBN-L2TP-MIB", "rbnL2tpPTCfgTunnelContext"),
        ("RBN-L2TP-MIB", "rbnL2tpPTCfgSessionCount"),
        ("RBN-L2TP-MIB", "rbnL2tpPTCfgTotActSessions"),
        ("RBN-L2TP-MIB", "rbnL2tpPTCfgActSessCnt"),
        ("RBN-L2TP-MIB", "rbnL2tpPTCfgTotFailSessions"))
)
if mibBuilder.loadTexts:
    rbnL2tpMibPeerTunCfgGroup.setStatus("current")


# Notification objects

rbnL2tpMibTunnelStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 0, 1)
)
rbnL2tpMibTunnelStateChange.setObjects(
      *(("RBN-L2TP-MIB", "rbnL2tpMibTunnelTrapContext"),
        ("RBN-L2TP-MIB", "rbnL2tpMibTunnelTrapState"))
)
if mibBuilder.loadTexts:
    rbnL2tpMibTunnelStateChange.setStatus(
        "deprecated"
    )

rbnL2tpMibTunnelStateChange2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 0, 2)
)
rbnL2tpMibTunnelStateChange2.setObjects(
      *(("RBN-L2TP-MIB", "rbnL2tpTCfgTunnelContext"),
        ("RBN-L2TP-MIB", "rbnL2tpMibTunnelState"),
        ("RBN-L2TP-MIB", "rbnL2tpTCfgRemoteTunnelID"))
)
if mibBuilder.loadTexts:
    rbnL2tpMibTunnelStateChange2.setStatus(
        "current"
    )


# Notifications groups

rbnL2tpMibNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 2, 1, 8)
)
rbnL2tpMibNotificationGroup.setObjects(
    ("RBN-L2TP-MIB", "rbnL2tpMibTunnelStateChange")
)
if mibBuilder.loadTexts:
    rbnL2tpMibNotificationGroup.setStatus(
        "deprecated"
    )

rbnL2tpMibNotificationGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 2, 1, 10)
)
rbnL2tpMibNotificationGroup2.setObjects(
    ("RBN-L2TP-MIB", "rbnL2tpMibTunnelStateChange2")
)
if mibBuilder.loadTexts:
    rbnL2tpMibNotificationGroup2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnL2tpMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rbnL2tpMibCompliance.setStatus(
        "deprecated"
    )

rbnL2tpMibCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 28, 2, 2, 2)
)
if mibBuilder.loadTexts:
    rbnL2tpMibCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-L2TP-MIB",
    **{"AuthType": AuthType,
       "LacLnsType": LacLnsType,
       "TunStateType": TunStateType,
       "CtlErrType": CtlErrType,
       "EthEncapType": EthEncapType,
       "DNISType": DNISType,
       "rbnL2tpMib": rbnL2tpMib,
       "rbnL2tpMibNotifications": rbnL2tpMibNotifications,
       "rbnL2tpMibTunnelStateChange": rbnL2tpMibTunnelStateChange,
       "rbnL2tpMibTunnelStateChange2": rbnL2tpMibTunnelStateChange2,
       "rbnL2tpMibObjects": rbnL2tpMibObjects,
       "rbnL2tpPeerCfgTable": rbnL2tpPeerCfgTable,
       "rbnL2tpPeerCfgEntry": rbnL2tpPeerCfgEntry,
       "rbnL2tpMibPeerName": rbnL2tpMibPeerName,
       "rbnL2tpPCfgMedia": rbnL2tpPCfgMedia,
       "rbnL2tpPCfgVendor": rbnL2tpPCfgVendor,
       "rbnL2tpPCfgRev": rbnL2tpPCfgRev,
       "rbnL2tpPCfgHostName": rbnL2tpPCfgHostName,
       "rbnL2tpPCfgRadius": rbnL2tpPCfgRadius,
       "rbnL2tpPCfgRemIPAddType": rbnL2tpPCfgRemIPAddType,
       "rbnL2tpPCfgRemIPAdd": rbnL2tpPCfgRemIPAdd,
       "rbnL2tpPCfgStatic": rbnL2tpPCfgStatic,
       "rbnL2tpPCfgLocalIPAddType": rbnL2tpPCfgLocalIPAddType,
       "rbnL2tpPCfgLocalIPAdd": rbnL2tpPCfgLocalIPAdd,
       "rbnL2tpPCfgMode": rbnL2tpPCfgMode,
       "rbnL2tpPCfgMaxTunnels": rbnL2tpPCfgMaxTunnels,
       "rbnL2tpPCfgMaxSesPerTun": rbnL2tpPCfgMaxSesPerTun,
       "rbnL2tpPCfgCtlRetranCnt": rbnL2tpPCfgCtlRetranCnt,
       "rbnL2tpPCfgCtlRetranTO": rbnL2tpPCfgCtlRetranTO,
       "rbnL2tpPCfgSessAuth": rbnL2tpPCfgSessAuth,
       "rbnL2tpPCfgCtlWin": rbnL2tpPCfgCtlWin,
       "rbnL2tpPCfgDNIS": rbnL2tpPCfgDNIS,
       "rbnL2tpPCfgPoliceRate": rbnL2tpPCfgPoliceRate,
       "rbnL2tpPCfgPoliceBurst": rbnL2tpPCfgPoliceBurst,
       "rbnL2tpPCfgLimitRate": rbnL2tpPCfgLimitRate,
       "rbnL2tpPCfgLimitBurst": rbnL2tpPCfgLimitBurst,
       "rbnL2tpPCfgGroup": rbnL2tpPCfgGroup,
       "rbnL2tpPCfgPref": rbnL2tpPCfgPref,
       "rbnL2tpPCfgPasswd": rbnL2tpPCfgPasswd,
       "rbnL2tpPCfgHelloTimer": rbnL2tpPCfgHelloTimer,
       "rbnL2tpPCfgRecQue": rbnL2tpPCfgRecQue,
       "rbnL2tpPCfgSessContext": rbnL2tpPCfgSessContext,
       "rbnL2tpPCfgSessService": rbnL2tpPCfgSessService,
       "rbnL2tpPCfgEthEncap": rbnL2tpPCfgEthEncap,
       "rbnL2tpPCfgEthSession": rbnL2tpPCfgEthSession,
       "rbnL2tpPCfgTunnelCount": rbnL2tpPCfgTunnelCount,
       "rbnL2tpPCfgTunCtlErrs": rbnL2tpPCfgTunCtlErrs,
       "rbnL2tpPCfgSessionCount": rbnL2tpPCfgSessionCount,
       "rbnL2tpTunnelCfgTable": rbnL2tpTunnelCfgTable,
       "rbnL2tpTunnelCfgEntry": rbnL2tpTunnelCfgEntry,
       "rbnL2tpMibTunnelID": rbnL2tpMibTunnelID,
       "rbnL2tpTCfgTunnelNm": rbnL2tpTCfgTunnelNm,
       "rbnL2tpTCfgPeerName": rbnL2tpTCfgPeerName,
       "rbnL2tpTCfgTunCtlErrs": rbnL2tpTCfgTunCtlErrs,
       "rbnL2tpTCfgLastCtlErr": rbnL2tpTCfgLastCtlErr,
       "rbnL2tpTCfgLastCErrTime": rbnL2tpTCfgLastCErrTime,
       "rbnL2tpTCfgTunDataErrs": rbnL2tpTCfgTunDataErrs,
       "rbnL2tpTCfgLastDataErr": rbnL2tpTCfgLastDataErr,
       "rbnL2tpTCfgLastDErrTime": rbnL2tpTCfgLastDErrTime,
       "rbnL2tpTCfgSessionCount": rbnL2tpTCfgSessionCount,
       "rbnL2tpTCfgTotActSessions": rbnL2tpTCfgTotActSessions,
       "rbnL2tpTCfgActSessCnt": rbnL2tpTCfgActSessCnt,
       "rbnL2tpTCfgTotFailSessions": rbnL2tpTCfgTotFailSessions,
       "rbnL2tpMibTunnelState": rbnL2tpMibTunnelState,
       "rbnL2tpTCfgRemoteTunnelID": rbnL2tpTCfgRemoteTunnelID,
       "rbnL2tpTCfgTunnelContext": rbnL2tpTCfgTunnelContext,
       "rbnL2tpPeerCntTable": rbnL2tpPeerCntTable,
       "rbnL2tpPeerCntEntry": rbnL2tpPeerCntEntry,
       "rbnL2tpPCDataPktSent": rbnL2tpPCDataPktSent,
       "rbnL2tpPCDataPktRx": rbnL2tpPCDataPktRx,
       "rbnL2tpPCDataByteSent": rbnL2tpPCDataByteSent,
       "rbnL2tpPCDataByteRx": rbnL2tpPCDataByteRx,
       "rbnL2tpPCCtlPktSent": rbnL2tpPCCtlPktSent,
       "rbnL2tpPCCtlPktRx": rbnL2tpPCCtlPktRx,
       "rbnL2tpPCCtlByteSent": rbnL2tpPCCtlByteSent,
       "rbnL2tpPCCtlByteRx": rbnL2tpPCCtlByteRx,
       "rbnL2tpPCPolicePktDrop": rbnL2tpPCPolicePktDrop,
       "rbnL2tpPCRatePktDrop": rbnL2tpPCRatePktDrop,
       "rbnL2tpPCTxSCCRQCnt": rbnL2tpPCTxSCCRQCnt,
       "rbnL2tpPCRxSCCRQCnt": rbnL2tpPCRxSCCRQCnt,
       "rbnL2tpPCActTunnels": rbnL2tpPCActTunnels,
       "rbnL2tpPCTunnelCtlErr": rbnL2tpPCTunnelCtlErr,
       "rbnL2tpPCSessionCount": rbnL2tpPCSessionCount,
       "rbnL2tpPCTunnelDataErr": rbnL2tpPCTunnelDataErr,
       "rbnL2tpTunnelCntTable": rbnL2tpTunnelCntTable,
       "rbnL2tpTunnelCntEntry": rbnL2tpTunnelCntEntry,
       "rbnL2tpTCDataPktSent": rbnL2tpTCDataPktSent,
       "rbnL2tpTCDataPktRcvd": rbnL2tpTCDataPktRcvd,
       "rbnL2tpTCDataByteSent": rbnL2tpTCDataByteSent,
       "rbnL2tpTCDataByteRcvd": rbnL2tpTCDataByteRcvd,
       "rbnL2tpTCCntrlPktSent": rbnL2tpTCCntrlPktSent,
       "rbnL2tpTCCntrlPktRcvd": rbnL2tpTCCntrlPktRcvd,
       "rbnL2tpTCCntrlByteSent": rbnL2tpTCCntrlByteSent,
       "rbnL2tpTCCntrlByteRcvd": rbnL2tpTCCntrlByteRcvd,
       "rbnL2tpTCPolicePktDrop": rbnL2tpTCPolicePktDrop,
       "rbnL2tpTCRatePktDrop": rbnL2tpTCRatePktDrop,
       "rbnL2tpTCCntrlErr": rbnL2tpTCCntrlErr,
       "rbnL2tpTCLastCtlErr": rbnL2tpTCLastCtlErr,
       "rbnL2tpTCLastCtlErrTime": rbnL2tpTCLastCtlErrTime,
       "rbnL2tpTCMaxResendQ": rbnL2tpTCMaxResendQ,
       "rbnL2tpTCMaxUnsentQ": rbnL2tpTCMaxUnsentQ,
       "rbnL2tpTCCurResendQ": rbnL2tpTCCurResendQ,
       "rbnL2tpTCCurUnsentQ": rbnL2tpTCCurUnsentQ,
       "rbnL2tpTCCurWindow": rbnL2tpTCCurWindow,
       "rbnL2tpSessionCntTable": rbnL2tpSessionCntTable,
       "rbnL2tpSessionCntEntry": rbnL2tpSessionCntEntry,
       "rbnL2tpMibSessionID": rbnL2tpMibSessionID,
       "rbnL2tpSCPktSent": rbnL2tpSCPktSent,
       "rbnL2tpSCPktRcvd": rbnL2tpSCPktRcvd,
       "rbnL2tpSCByteSent": rbnL2tpSCByteSent,
       "rbnL2tpSCByteRcvd": rbnL2tpSCByteRcvd,
       "rbnL2tpSCMcastPktSent": rbnL2tpSCMcastPktSent,
       "rbnL2tpSCMcastPktRcvd": rbnL2tpSCMcastPktRcvd,
       "rbnL2tpSCMcastByteSent": rbnL2tpSCMcastByteSent,
       "rbnL2tpSCMcastByteRcvd": rbnL2tpSCMcastByteRcvd,
       "rbnL2tpMibTrapObj": rbnL2tpMibTrapObj,
       "rbnL2tpMibTunnelTrapContext": rbnL2tpMibTunnelTrapContext,
       "rbnL2tpMibTunnelTrapState": rbnL2tpMibTunnelTrapState,
       "rbnL2tpMibDisableTrap": rbnL2tpMibDisableTrap,
       "rbnL2tpPeerTunCfgTable": rbnL2tpPeerTunCfgTable,
       "rbnL2tpPeerTunCfgEntry": rbnL2tpPeerTunCfgEntry,
       "rbnL2tpPTCfgTunnelRemoteID": rbnL2tpPTCfgTunnelRemoteID,
       "rbnL2tpPTCfgTunnelLocalNm": rbnL2tpPTCfgTunnelLocalNm,
       "rbnL2tpPTCfgTunnelRemoteNm": rbnL2tpPTCfgTunnelRemoteNm,
       "rbnL2tpPTCfgPeerLocalNm": rbnL2tpPTCfgPeerLocalNm,
       "rbnL2tpPTCfgTunnelRemoteIPAddrType": rbnL2tpPTCfgTunnelRemoteIPAddrType,
       "rbnL2tpPTCfgTunnelRemoteIPAddr": rbnL2tpPTCfgTunnelRemoteIPAddr,
       "rbnL2tpPTCfgTunnelState": rbnL2tpPTCfgTunnelState,
       "rbnL2tpPTCfgTunnelContext": rbnL2tpPTCfgTunnelContext,
       "rbnL2tpPTCfgSessionCount": rbnL2tpPTCfgSessionCount,
       "rbnL2tpPTCfgActSessCnt": rbnL2tpPTCfgActSessCnt,
       "rbnL2tpPTCfgTotActSessions": rbnL2tpPTCfgTotActSessions,
       "rbnL2tpPTCfgTotFailSessions": rbnL2tpPTCfgTotFailSessions,
       "rbnL2tpMibConformance": rbnL2tpMibConformance,
       "rbnL2tpMibGroups": rbnL2tpMibGroups,
       "rbnL2tpMibPeerCfgGroup": rbnL2tpMibPeerCfgGroup,
       "rbnL2tpMibTunnelCfgGroup": rbnL2tpMibTunnelCfgGroup,
       "rbnL2tpMibPeerCntGroup": rbnL2tpMibPeerCntGroup,
       "rbnL2tpMibTunnelCntGroup": rbnL2tpMibTunnelCntGroup,
       "rbnL2tpMibSessionCntGroup": rbnL2tpMibSessionCntGroup,
       "rbnL2tpMibGroup": rbnL2tpMibGroup,
       "rbnL2tpMibNotificationGroup": rbnL2tpMibNotificationGroup,
       "rbnL2tpMibGroup2": rbnL2tpMibGroup2,
       "rbnL2tpMibNotificationGroup2": rbnL2tpMibNotificationGroup2,
       "rbnL2tpMibPeerTunCfgGroup": rbnL2tpMibPeerTunCfgGroup,
       "rbnL2tpMibCompliances": rbnL2tpMibCompliances,
       "rbnL2tpMibCompliance": rbnL2tpMibCompliance,
       "rbnL2tpMibCompliance2": rbnL2tpMibCompliance2}
)
