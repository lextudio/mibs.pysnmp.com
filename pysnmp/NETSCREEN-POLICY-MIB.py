# SNMP MIB module (NETSCREEN-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:49 2024
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

(netscreenPolicy,) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenPolicy")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

netscreenPolicyMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 10, 0)
)
netscreenPolicyMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-08-13 00:00",
         "2001-05-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsPlyTable_Object = MibTable
nsPlyTable = _NsPlyTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1)
)
if mibBuilder.loadTexts:
    nsPlyTable.setStatus("current")
_NsPlyEntry_Object = MibTableRow
nsPlyEntry = _NsPlyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1)
)
nsPlyEntry.setIndexNames(
    (0, "NETSCREEN-POLICY-MIB", "nsPlyVsys"),
    (0, "NETSCREEN-POLICY-MIB", "nsPlyId"),
)
if mibBuilder.loadTexts:
    nsPlyEntry.setStatus("current")


class _NsPlyId_Type(Integer32):
    """Custom type nsPlyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsPlyId_Type.__name__ = "Integer32"
_NsPlyId_Object = MibTableColumn
nsPlyId = _NsPlyId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 1),
    _NsPlyId_Type()
)
nsPlyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyId.setStatus("current")


class _NsPlyVsys_Type(Integer32):
    """Custom type nsPlyVsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsPlyVsys_Type.__name__ = "Integer32"
_NsPlyVsys_Object = MibTableColumn
nsPlyVsys = _NsPlyVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 2),
    _NsPlyVsys_Type()
)
nsPlyVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyVsys.setStatus("current")


class _NsPlySrcZone_Type(DisplayString):
    """Custom type nsPlySrcZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsPlySrcZone_Type.__name__ = "DisplayString"
_NsPlySrcZone_Object = MibTableColumn
nsPlySrcZone = _NsPlySrcZone_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 3),
    _NsPlySrcZone_Type()
)
nsPlySrcZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlySrcZone.setStatus("current")


class _NsPlyDstZone_Type(DisplayString):
    """Custom type nsPlyDstZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsPlyDstZone_Type.__name__ = "DisplayString"
_NsPlyDstZone_Object = MibTableColumn
nsPlyDstZone = _NsPlyDstZone_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 4),
    _NsPlyDstZone_Type()
)
nsPlyDstZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyDstZone.setStatus("current")


class _NsPlySrcAddr_Type(DisplayString):
    """Custom type nsPlySrcAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsPlySrcAddr_Type.__name__ = "DisplayString"
_NsPlySrcAddr_Object = MibTableColumn
nsPlySrcAddr = _NsPlySrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 5),
    _NsPlySrcAddr_Type()
)
nsPlySrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlySrcAddr.setStatus("current")


class _NsPlyDstAddr_Type(DisplayString):
    """Custom type nsPlyDstAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsPlyDstAddr_Type.__name__ = "DisplayString"
_NsPlyDstAddr_Object = MibTableColumn
nsPlyDstAddr = _NsPlyDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 6),
    _NsPlyDstAddr_Type()
)
nsPlyDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyDstAddr.setStatus("current")


class _NsPlyService_Type(Integer32):
    """Custom type nsPlyService based on Integer32"""
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
              50)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("aol", 1),
          ("bgp", 2),
          ("dns", 4),
          ("dpcp-relay", 3),
          ("finger", 5),
          ("ftp", 6),
          ("ftp-get", 7),
          ("ftp-put", 8),
          ("gopher", 9),
          ("h323", 10),
          ("http", 11),
          ("https", 12),
          ("icmp-info", 13),
          ("icmp-timestamp", 14),
          ("ike", 15),
          ("imap", 16),
          ("internet-locator-service", 17),
          ("irc", 18),
          ("l2tp", 19),
          ("ldap", 20),
          ("mail", 21),
          ("netmeeting", 22),
          ("nfs", 23),
          ("nntp", 24),
          ("ns-global", 25),
          ("ns-global-pro", 26),
          ("ntp", 27),
          ("ospf", 28),
          ("other", 50),
          ("pc-anywhere", 29),
          ("ping", 30),
          ("pop3", 31),
          ("pptp", 32),
          ("real-media", 33),
          ("rip", 34),
          ("rlogin", 35),
          ("snmp", 36),
          ("ssh", 37),
          ("syslog", 38),
          ("talk", 39),
          ("tcp-any", 40),
          ("telnet", 41),
          ("tftp", 42),
          ("traceroute", 43),
          ("udp-any", 44),
          ("uucp", 45),
          ("vdo-live", 46),
          ("wais", 47),
          ("winframe", 48),
          ("x-windows", 49))
    )


_NsPlyService_Type.__name__ = "Integer32"
_NsPlyService_Object = MibTableColumn
nsPlyService = _NsPlyService_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 7),
    _NsPlyService_Type()
)
nsPlyService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyService.setStatus("current")


class _NsPlyAction_Type(Integer32):
    """Custom type nsPlyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1),
          ("tunnel", 2))
    )


_NsPlyAction_Type.__name__ = "Integer32"
_NsPlyAction_Object = MibTableColumn
nsPlyAction = _NsPlyAction_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 8),
    _NsPlyAction_Type()
)
nsPlyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyAction.setStatus("current")


class _NsPlyNat_Type(Integer32):
    """Custom type nsPlyNat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsPlyNat_Type.__name__ = "Integer32"
_NsPlyNat_Object = MibTableColumn
nsPlyNat = _NsPlyNat_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 9),
    _NsPlyNat_Type()
)
nsPlyNat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyNat.setStatus("current")


class _NsPlyFixPort_Type(Integer32):
    """Custom type nsPlyFixPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NsPlyFixPort_Type.__name__ = "Integer32"
_NsPlyFixPort_Object = MibTableColumn
nsPlyFixPort = _NsPlyFixPort_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 10),
    _NsPlyFixPort_Type()
)
nsPlyFixPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyFixPort.setStatus("current")
_NsPlyDipId_Type = Integer32
_NsPlyDipId_Object = MibTableColumn
nsPlyDipId = _NsPlyDipId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 11),
    _NsPlyDipId_Type()
)
nsPlyDipId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyDipId.setStatus("current")


class _NsPlyVpnTunnel_Type(DisplayString):
    """Custom type nsPlyVpnTunnel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsPlyVpnTunnel_Type.__name__ = "DisplayString"
_NsPlyVpnTunnel_Object = MibTableColumn
nsPlyVpnTunnel = _NsPlyVpnTunnel_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 12),
    _NsPlyVpnTunnel_Type()
)
nsPlyVpnTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyVpnTunnel.setStatus("current")


class _NsPlyL2tpTunnel_Type(DisplayString):
    """Custom type nsPlyL2tpTunnel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsPlyL2tpTunnel_Type.__name__ = "DisplayString"
_NsPlyL2tpTunnel_Object = MibTableColumn
nsPlyL2tpTunnel = _NsPlyL2tpTunnel_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 13),
    _NsPlyL2tpTunnel_Type()
)
nsPlyL2tpTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyL2tpTunnel.setStatus("current")


class _NsPlyAuth_Type(Integer32):
    """Custom type nsPlyAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsPlyAuth_Type.__name__ = "Integer32"
_NsPlyAuth_Object = MibTableColumn
nsPlyAuth = _NsPlyAuth_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 14),
    _NsPlyAuth_Type()
)
nsPlyAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyAuth.setStatus("current")


class _NsPlyLogEnable_Type(Integer32):
    """Custom type nsPlyLogEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsPlyLogEnable_Type.__name__ = "Integer32"
_NsPlyLogEnable_Object = MibTableColumn
nsPlyLogEnable = _NsPlyLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 15),
    _NsPlyLogEnable_Type()
)
nsPlyLogEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyLogEnable.setStatus("current")


class _NsPlyCountEnable_Type(Integer32):
    """Custom type nsPlyCountEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsPlyCountEnable_Type.__name__ = "Integer32"
_NsPlyCountEnable_Object = MibTableColumn
nsPlyCountEnable = _NsPlyCountEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 16),
    _NsPlyCountEnable_Type()
)
nsPlyCountEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyCountEnable.setStatus("current")
_NsPlyAlarmBPS_Type = Integer32
_NsPlyAlarmBPS_Object = MibTableColumn
nsPlyAlarmBPS = _NsPlyAlarmBPS_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 17),
    _NsPlyAlarmBPS_Type()
)
nsPlyAlarmBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyAlarmBPS.setStatus("current")
_NsPlyAlarmBPM_Type = Integer32
_NsPlyAlarmBPM_Object = MibTableColumn
nsPlyAlarmBPM = _NsPlyAlarmBPM_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 18),
    _NsPlyAlarmBPM_Type()
)
nsPlyAlarmBPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyAlarmBPM.setStatus("current")


class _NsPlySchedule_Type(DisplayString):
    """Custom type nsPlySchedule based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsPlySchedule_Type.__name__ = "DisplayString"
_NsPlySchedule_Object = MibTableColumn
nsPlySchedule = _NsPlySchedule_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 19),
    _NsPlySchedule_Type()
)
nsPlySchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlySchedule.setStatus("current")


class _NsPlyTrafficShapeEnable_Type(Integer32):
    """Custom type nsPlyTrafficShapeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NsPlyTrafficShapeEnable_Type.__name__ = "Integer32"
_NsPlyTrafficShapeEnable_Object = MibTableColumn
nsPlyTrafficShapeEnable = _NsPlyTrafficShapeEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 20),
    _NsPlyTrafficShapeEnable_Type()
)
nsPlyTrafficShapeEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyTrafficShapeEnable.setStatus("current")


class _NsPlyTrafficPriority_Type(Integer32):
    """Custom type nsPlyTrafficPriority based on Integer32"""
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
        *(("high", 0),
          ("priority2nd", 1),
          ("priority3rd", 2),
          ("priority4th", 3),
          ("priority5th", 4),
          ("priority6th", 5),
          ("priority7th", 6),
          ("priorityLow", 7))
    )


_NsPlyTrafficPriority_Type.__name__ = "Integer32"
_NsPlyTrafficPriority_Object = MibTableColumn
nsPlyTrafficPriority = _NsPlyTrafficPriority_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 21),
    _NsPlyTrafficPriority_Type()
)
nsPlyTrafficPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyTrafficPriority.setStatus("current")


class _NsPlyDSEnable_Type(Integer32):
    """Custom type nsPlyDSEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsPlyDSEnable_Type.__name__ = "Integer32"
_NsPlyDSEnable_Object = MibTableColumn
nsPlyDSEnable = _NsPlyDSEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 22),
    _NsPlyDSEnable_Type()
)
nsPlyDSEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyDSEnable.setStatus("current")


class _NsPlyActiveStatus_Type(Integer32):
    """Custom type nsPlyActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 2),
          ("inactive", 0),
          ("inuse", 1))
    )


_NsPlyActiveStatus_Type.__name__ = "Integer32"
_NsPlyActiveStatus_Object = MibTableColumn
nsPlyActiveStatus = _NsPlyActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 23),
    _NsPlyActiveStatus_Type()
)
nsPlyActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyActiveStatus.setStatus("current")


class _NsPlyName_Type(DisplayString):
    """Custom type nsPlyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsPlyName_Type.__name__ = "DisplayString"
_NsPlyName_Object = MibTableColumn
nsPlyName = _NsPlyName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 24),
    _NsPlyName_Type()
)
nsPlyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyName.setStatus("current")
_NsPlyServiceName_Type = DisplayString
_NsPlyServiceName_Object = MibTableColumn
nsPlyServiceName = _NsPlyServiceName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 1, 1, 25),
    _NsPlyServiceName_Type()
)
nsPlyServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyServiceName.setStatus("current")
_NsPlyMonTable_Object = MibTable
nsPlyMonTable = _NsPlyMonTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 2)
)
if mibBuilder.loadTexts:
    nsPlyMonTable.setStatus("current")
_NsPlyMonEntry_Object = MibTableRow
nsPlyMonEntry = _NsPlyMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 2, 1)
)
nsPlyMonEntry.setIndexNames(
    (0, "NETSCREEN-POLICY-MIB", "nsPlyMonId"),
    (0, "NETSCREEN-POLICY-MIB", "nsPlyMonVsys"),
)
if mibBuilder.loadTexts:
    nsPlyMonEntry.setStatus("current")


class _NsPlyMonId_Type(Integer32):
    """Custom type nsPlyMonId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsPlyMonId_Type.__name__ = "Integer32"
_NsPlyMonId_Object = MibTableColumn
nsPlyMonId = _NsPlyMonId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 2, 1, 1),
    _NsPlyMonId_Type()
)
nsPlyMonId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyMonId.setStatus("current")


class _NsPlyMonVsys_Type(Integer32):
    """Custom type nsPlyMonVsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsPlyMonVsys_Type.__name__ = "Integer32"
_NsPlyMonVsys_Object = MibTableColumn
nsPlyMonVsys = _NsPlyMonVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 2, 1, 2),
    _NsPlyMonVsys_Type()
)
nsPlyMonVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyMonVsys.setStatus("current")
_NsPlyMonPackPerSec_Type = Integer32
_NsPlyMonPackPerSec_Object = MibTableColumn
nsPlyMonPackPerSec = _NsPlyMonPackPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 2, 1, 3),
    _NsPlyMonPackPerSec_Type()
)
nsPlyMonPackPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyMonPackPerSec.setStatus("current")
_NsPlyMonPackPerMin_Type = Integer32
_NsPlyMonPackPerMin_Object = MibTableColumn
nsPlyMonPackPerMin = _NsPlyMonPackPerMin_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 2, 1, 4),
    _NsPlyMonPackPerMin_Type()
)
nsPlyMonPackPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyMonPackPerMin.setStatus("current")
_NsPlyMonTotalPacket_Type = Counter32
_NsPlyMonTotalPacket_Object = MibTableColumn
nsPlyMonTotalPacket = _NsPlyMonTotalPacket_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 2, 1, 5),
    _NsPlyMonTotalPacket_Type()
)
nsPlyMonTotalPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyMonTotalPacket.setStatus("current")
_NsPlyMonBytePerSec_Type = Integer32
_NsPlyMonBytePerSec_Object = MibTableColumn
nsPlyMonBytePerSec = _NsPlyMonBytePerSec_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 2, 1, 6),
    _NsPlyMonBytePerSec_Type()
)
nsPlyMonBytePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyMonBytePerSec.setStatus("current")
_NsPlyMonBytePerMin_Type = Integer32
_NsPlyMonBytePerMin_Object = MibTableColumn
nsPlyMonBytePerMin = _NsPlyMonBytePerMin_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 2, 1, 7),
    _NsPlyMonBytePerMin_Type()
)
nsPlyMonBytePerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyMonBytePerMin.setStatus("current")
_NsPlyMonTotalByte_Type = Counter32
_NsPlyMonTotalByte_Object = MibTableColumn
nsPlyMonTotalByte = _NsPlyMonTotalByte_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 2, 1, 8),
    _NsPlyMonTotalByte_Type()
)
nsPlyMonTotalByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyMonTotalByte.setStatus("current")
_NsPlyMonSessionPerSec_Type = Integer32
_NsPlyMonSessionPerSec_Object = MibTableColumn
nsPlyMonSessionPerSec = _NsPlyMonSessionPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 2, 1, 9),
    _NsPlyMonSessionPerSec_Type()
)
nsPlyMonSessionPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyMonSessionPerSec.setStatus("current")
_NsPlyMonSessionPerMin_Type = Integer32
_NsPlyMonSessionPerMin_Object = MibTableColumn
nsPlyMonSessionPerMin = _NsPlyMonSessionPerMin_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 2, 1, 10),
    _NsPlyMonSessionPerMin_Type()
)
nsPlyMonSessionPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyMonSessionPerMin.setStatus("current")
_NsPlyMonTotalSession_Type = Counter32
_NsPlyMonTotalSession_Object = MibTableColumn
nsPlyMonTotalSession = _NsPlyMonTotalSession_Object(
    (1, 3, 6, 1, 4, 1, 3224, 10, 2, 1, 11),
    _NsPlyMonTotalSession_Type()
)
nsPlyMonTotalSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPlyMonTotalSession.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-POLICY-MIB",
    **{"netscreenPolicyMibModule": netscreenPolicyMibModule,
       "nsPlyTable": nsPlyTable,
       "nsPlyEntry": nsPlyEntry,
       "nsPlyId": nsPlyId,
       "nsPlyVsys": nsPlyVsys,
       "nsPlySrcZone": nsPlySrcZone,
       "nsPlyDstZone": nsPlyDstZone,
       "nsPlySrcAddr": nsPlySrcAddr,
       "nsPlyDstAddr": nsPlyDstAddr,
       "nsPlyService": nsPlyService,
       "nsPlyAction": nsPlyAction,
       "nsPlyNat": nsPlyNat,
       "nsPlyFixPort": nsPlyFixPort,
       "nsPlyDipId": nsPlyDipId,
       "nsPlyVpnTunnel": nsPlyVpnTunnel,
       "nsPlyL2tpTunnel": nsPlyL2tpTunnel,
       "nsPlyAuth": nsPlyAuth,
       "nsPlyLogEnable": nsPlyLogEnable,
       "nsPlyCountEnable": nsPlyCountEnable,
       "nsPlyAlarmBPS": nsPlyAlarmBPS,
       "nsPlyAlarmBPM": nsPlyAlarmBPM,
       "nsPlySchedule": nsPlySchedule,
       "nsPlyTrafficShapeEnable": nsPlyTrafficShapeEnable,
       "nsPlyTrafficPriority": nsPlyTrafficPriority,
       "nsPlyDSEnable": nsPlyDSEnable,
       "nsPlyActiveStatus": nsPlyActiveStatus,
       "nsPlyName": nsPlyName,
       "nsPlyServiceName": nsPlyServiceName,
       "nsPlyMonTable": nsPlyMonTable,
       "nsPlyMonEntry": nsPlyMonEntry,
       "nsPlyMonId": nsPlyMonId,
       "nsPlyMonVsys": nsPlyMonVsys,
       "nsPlyMonPackPerSec": nsPlyMonPackPerSec,
       "nsPlyMonPackPerMin": nsPlyMonPackPerMin,
       "nsPlyMonTotalPacket": nsPlyMonTotalPacket,
       "nsPlyMonBytePerSec": nsPlyMonBytePerSec,
       "nsPlyMonBytePerMin": nsPlyMonBytePerMin,
       "nsPlyMonTotalByte": nsPlyMonTotalByte,
       "nsPlyMonSessionPerSec": nsPlyMonSessionPerSec,
       "nsPlyMonSessionPerMin": nsPlyMonSessionPerMin,
       "nsPlyMonTotalSession": nsPlyMonTotalSession}
)
