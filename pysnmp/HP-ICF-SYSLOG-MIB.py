# SNMP MIB module (HP-ICF-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-SYSLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:16 2024
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

(hpicfSyslog,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpicfSyslog")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

hpicfSyslogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1)
)
hpicfSyslogMIB.setRevisions(
        ("2015-09-11 05:26",
         "2015-09-04 00:00",
         "2015-09-03 00:00",
         "2015-08-31 00:00",
         "2015-08-28 00:00",
         "2015-05-09 00:00",
         "2015-04-16 00:00",
         "2014-11-13 00:00",
         "2014-07-17 00:00",
         "2013-11-06 00:00",
         "2013-09-24 00:00",
         "2013-09-14 00:00",
         "2013-09-05 00:00",
         "2013-06-25 00:00",
         "2013-08-07 00:00",
         "2012-03-15 00:00",
         "2012-01-30 00:00",
         "2011-10-11 00:00",
         "2011-08-24 00:00",
         "2011-07-19 00:00",
         "2011-06-13 00:00",
         "2011-05-27 00:00",
         "2011-03-21 00:00",
         "2011-03-05 00:00",
         "2010-11-09 00:00",
         "2010-10-25 00:00",
         "2010-08-11 00:00",
         "2010-06-20 00:00",
         "2010-03-20 00:00",
         "2010-03-12 00:00",
         "2010-01-27 00:00",
         "2009-08-19 00:00",
         "2009-02-18 00:00",
         "2009-01-30 00:00",
         "2008-11-18 00:00",
         "2008-07-09 00:00",
         "2008-06-26 00:00",
         "2008-06-25 00:00",
         "2008-01-25 00:00",
         "2008-01-01 11:21")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpicfSyslogFacility(Integer32, TextualConvention):
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("auth", 4),
          ("cron", 15),
          ("daemon", 3),
          ("kern", 0),
          ("local0", 16),
          ("local1", 17),
          ("local2", 18),
          ("local3", 19),
          ("local4", 20),
          ("local5", 21),
          ("local6", 22),
          ("local7", 23),
          ("lpr", 6),
          ("mail", 2),
          ("news", 7),
          ("sys10", 10),
          ("sys11", 11),
          ("sys12", 12),
          ("sys13", 13),
          ("sys14", 14),
          ("sys9", 9),
          ("syslog", 5),
          ("user", 1),
          ("uucp", 8))
    )



class HpicfSyslogSeverity(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("error", 3),
          ("info", 6),
          ("major", 0),
          ("notice", 5),
          ("warning", 4))
    )



class HpicfSyslogSystemModule(Integer32, TextualConvention):
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
              100,
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
              120,
              122,
              123,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133)
        )
    )
    namedValues = NamedValues(
        *(("acct", 115),
          ("acl", 48),
          ("addrmgr", 21),
          ("agp", 22),
          ("all-pass", 0),
          ("arp-protect", 64),
          ("arpthrottle", 120),
          ("auth", 35),
          ("autorun", 70),
          ("bfd", 129),
          ("bgp", 81),
          ("bpdu", 111),
          ("bridge", 19),
          ("byod-redirect", 112),
          ("captive-portal", 131),
          ("cdp", 34),
          ("chassis", 7),
          ("connfilt", 54),
          ("console", 8),
          ("cos", 27),
          ("crypto", 90),
          ("dca", 68),
          ("dcbx", 85),
          ("dhcp", 10),
          ("dhcp-server", 103),
          ("dhcp-snoop", 58),
          ("dhcpr", 29),
          ("dhcpv6c", 65),
          ("dhcpv6r", 80),
          ("dipld", 73),
          ("dipldv6", 106),
          ("dldp", 113),
          ("dma", 31),
          ("download", 11),
          ("dsnoopv6", 105),
          ("dt", 84),
          ("eSatProxy", 98),
          ("ecm", 93),
          ("fault", 23),
          ("ffi", 71),
          ("fips", 83),
          ("garp", 25),
          ("gvrp", 26),
          ("hpesp", 52),
          ("hpespcm", 99),
          ("hpespip", 94),
          ("hpsm", 74),
          ("http", 109),
          ("idm", 56),
          ("ieee8021x", 33),
          ("igmp", 3),
          ("inst-mon", 50),
          ("insysprog", 102),
          ("ip", 2),
          ("ipaddrmgr", 43),
          ("iplock", 57),
          ("ipx", 4),
          ("job", 104),
          ("kms", 45),
          ("lacp", 28),
          ("ldbal", 24),
          ("licensing", 61),
          ("lldp", 53),
          ("lldpmad", 130),
          ("loop-protect", 62),
          ("mSatProxy", 97),
          ("macauth", 44),
          ("maclock", 47),
          ("macsec", 114),
          ("mdns", 126),
          ("mgr", 18),
          ("mld", 67),
          ("mobility-agent", 95),
          ("mtm", 66),
          ("mvrp", 127),
          ("ndsnoop", 122),
          ("netinet", 39),
          ("ntp", 123),
          ("oobm", 77),
          ("openflow", 100),
          ("ospf", 40),
          ("ospf3", 79),
          ("pim", 46),
          ("policy", 76),
          ("ports", 9),
          ("profile-manager", 132),
          ("qinq", 69),
          ("ra-guard", 92),
          ("radius", 37),
          ("ratelim", 55),
          ("rfs", 88),
          ("rip", 128),
          ("ripng", 117),
          ("securemode", 96),
          ("servicetunnel", 107),
          ("sflow", 63),
          ("sftp", 86),
          ("slp", 91),
          ("smart-link", 101),
          ("snmp", 20),
          ("sntp", 32),
          ("srcip", 75),
          ("ssh", 38),
          ("ssl", 42),
          ("stack", 30),
          ("stacking", 87),
          ("stp", 5),
          ("system", 6),
          ("tacacs", 36),
          ("tcp", 12),
          ("telnet", 13),
          ("testmode", 89),
          ("tftp", 15),
          ("timep", 14),
          ("tls", 116),
          ("tr069", 108),
          ("trmode", 78),
          ("udld", 51),
          ("udpf", 49),
          ("ufd", 82),
          ("update", 17),
          ("usb", 60),
          ("vlan", 1),
          ("vrrp", 59),
          ("vsf", 133),
          ("vxlantunnel", 110),
          ("wsm", 72),
          ("xmodem", 16),
          ("xrrp", 41))
    )



class HpicfSyslogOriginId(Integer32, TextualConvention):
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
        *(("hostname", 2),
          ("ip-address", 1),
          ("none", 3))
    )



# MIB Managed Objects in the order of their OIDs

_HpicfSyslogNotifications_ObjectIdentity = ObjectIdentity
hpicfSyslogNotifications = _HpicfSyslogNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 0)
)
_HpicfSyslogObjects_ObjectIdentity = ObjectIdentity
hpicfSyslogObjects = _HpicfSyslogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1)
)
_HpicfSyslogControlTable_Object = MibTable
hpicfSyslogControlTable = _HpicfSyslogControlTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfSyslogControlTable.setStatus("current")
_HpicfSyslogControlEntry_Object = MibTableRow
hpicfSyslogControlEntry = _HpicfSyslogControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 1, 1)
)
hpicfSyslogControlEntry.setIndexNames(
    (0, "HP-ICF-SYSLOG-MIB", "hpicfSyslogControlIndex"),
)
if mibBuilder.loadTexts:
    hpicfSyslogControlEntry.setStatus("current")
_HpicfSyslogControlIndex_Type = Integer32
_HpicfSyslogControlIndex_Object = MibTableColumn
hpicfSyslogControlIndex = _HpicfSyslogControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 1, 1, 1),
    _HpicfSyslogControlIndex_Type()
)
hpicfSyslogControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSyslogControlIndex.setStatus("current")
_HpicfSyslogControlDescr_Type = SnmpAdminString
_HpicfSyslogControlDescr_Object = MibTableColumn
hpicfSyslogControlDescr = _HpicfSyslogControlDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 1, 1, 2),
    _HpicfSyslogControlDescr_Type()
)
hpicfSyslogControlDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSyslogControlDescr.setStatus("current")
_HpicfSyslogControlBindAddrType_Type = InetAddressType
_HpicfSyslogControlBindAddrType_Object = MibTableColumn
hpicfSyslogControlBindAddrType = _HpicfSyslogControlBindAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 1, 1, 3),
    _HpicfSyslogControlBindAddrType_Type()
)
hpicfSyslogControlBindAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSyslogControlBindAddrType.setStatus("current")
_HpicfSyslogControlBindAddr_Type = InetAddress
_HpicfSyslogControlBindAddr_Object = MibTableColumn
hpicfSyslogControlBindAddr = _HpicfSyslogControlBindAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 1, 1, 4),
    _HpicfSyslogControlBindAddr_Type()
)
hpicfSyslogControlBindAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSyslogControlBindAddr.setStatus("current")
_HpicfSyslogControlRowStatus_Type = RowStatus
_HpicfSyslogControlRowStatus_Object = MibTableColumn
hpicfSyslogControlRowStatus = _HpicfSyslogControlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 1, 1, 5),
    _HpicfSyslogControlRowStatus_Type()
)
hpicfSyslogControlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSyslogControlRowStatus.setStatus("current")


class _HpicfSyslogControlBindAddrIsOobm_Type(TruthValue):
    """Custom type hpicfSyslogControlBindAddrIsOobm based on TruthValue"""


_HpicfSyslogControlBindAddrIsOobm_Object = MibTableColumn
hpicfSyslogControlBindAddrIsOobm = _HpicfSyslogControlBindAddrIsOobm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 1, 1, 6),
    _HpicfSyslogControlBindAddrIsOobm_Type()
)
hpicfSyslogControlBindAddrIsOobm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSyslogControlBindAddrIsOobm.setStatus("current")


class _HpicfSyslogControlSmmLog_Type(Integer32):
    """Custom type hpicfSyslogControlSmmLog based on Integer32"""
    defaultValue = 2

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


_HpicfSyslogControlSmmLog_Type.__name__ = "Integer32"
_HpicfSyslogControlSmmLog_Object = MibTableColumn
hpicfSyslogControlSmmLog = _HpicfSyslogControlSmmLog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 1, 1, 7),
    _HpicfSyslogControlSmmLog_Type()
)
hpicfSyslogControlSmmLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSyslogControlSmmLog.setStatus("current")


class _HpicfSyslogControlTransportProtocol_Type(Integer32):
    """Custom type hpicfSyslogControlTransportProtocol based on Integer32"""
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
        *(("tcp", 2),
          ("tls", 3),
          ("udp", 1))
    )


_HpicfSyslogControlTransportProtocol_Type.__name__ = "Integer32"
_HpicfSyslogControlTransportProtocol_Object = MibTableColumn
hpicfSyslogControlTransportProtocol = _HpicfSyslogControlTransportProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 1, 1, 8),
    _HpicfSyslogControlTransportProtocol_Type()
)
hpicfSyslogControlTransportProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSyslogControlTransportProtocol.setStatus("current")
_HpicfSyslogControlDestinationPort_Type = InetPortNumber
_HpicfSyslogControlDestinationPort_Object = MibTableColumn
hpicfSyslogControlDestinationPort = _HpicfSyslogControlDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 1, 1, 9),
    _HpicfSyslogControlDestinationPort_Type()
)
hpicfSyslogControlDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSyslogControlDestinationPort.setStatus("current")
_HpicfSyslogOperations_ObjectIdentity = ObjectIdentity
hpicfSyslogOperations = _HpicfSyslogOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 2)
)
_HpicfSyslogOperationsMsgsTransmitted_Type = Counter32
_HpicfSyslogOperationsMsgsTransmitted_Object = MibScalar
hpicfSyslogOperationsMsgsTransmitted = _HpicfSyslogOperationsMsgsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 2, 1),
    _HpicfSyslogOperationsMsgsTransmitted_Type()
)
hpicfSyslogOperationsMsgsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogOperationsMsgsTransmitted.setStatus("current")
_HpicfSyslogOperationsMsgsDropped_Type = Counter32
_HpicfSyslogOperationsMsgsDropped_Object = MibScalar
hpicfSyslogOperationsMsgsDropped = _HpicfSyslogOperationsMsgsDropped_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 2, 2),
    _HpicfSyslogOperationsMsgsDropped_Type()
)
hpicfSyslogOperationsMsgsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogOperationsMsgsDropped.setStatus("current")
_HpicfSyslogOperationsLastMsgTransmittedTime_Type = TimeStamp
_HpicfSyslogOperationsLastMsgTransmittedTime_Object = MibScalar
hpicfSyslogOperationsLastMsgTransmittedTime = _HpicfSyslogOperationsLastMsgTransmittedTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 2, 3),
    _HpicfSyslogOperationsLastMsgTransmittedTime_Type()
)
hpicfSyslogOperationsLastMsgTransmittedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogOperationsLastMsgTransmittedTime.setStatus("current")
_HpicfSyslogOperationsStartTime_Type = TimeStamp
_HpicfSyslogOperationsStartTime_Object = MibScalar
hpicfSyslogOperationsStartTime = _HpicfSyslogOperationsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 2, 4),
    _HpicfSyslogOperationsStartTime_Type()
)
hpicfSyslogOperationsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogOperationsStartTime.setStatus("current")
_HpicfSyslogOperationsLastError_Type = SnmpAdminString
_HpicfSyslogOperationsLastError_Object = MibScalar
hpicfSyslogOperationsLastError = _HpicfSyslogOperationsLastError_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 2, 5),
    _HpicfSyslogOperationsLastError_Type()
)
hpicfSyslogOperationsLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogOperationsLastError.setStatus("current")
_HpicfSyslogOperationsLastErrorTime_Type = TimeStamp
_HpicfSyslogOperationsLastErrorTime_Object = MibScalar
hpicfSyslogOperationsLastErrorTime = _HpicfSyslogOperationsLastErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 2, 6),
    _HpicfSyslogOperationsLastErrorTime_Type()
)
hpicfSyslogOperationsLastErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogOperationsLastErrorTime.setStatus("current")
_HpicfSyslogOperationsCounterDiscontinuityTime_Type = TimeStamp
_HpicfSyslogOperationsCounterDiscontinuityTime_Object = MibScalar
hpicfSyslogOperationsCounterDiscontinuityTime = _HpicfSyslogOperationsCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 2, 7),
    _HpicfSyslogOperationsCounterDiscontinuityTime_Type()
)
hpicfSyslogOperationsCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogOperationsCounterDiscontinuityTime.setStatus("current")


class _HpicfSyslogOperationsStatus_Type(Integer32):
    """Custom type hpicfSyslogOperationsStatus based on Integer32"""
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
        *(("started", 2),
          ("stopped", 4),
          ("suspended", 3),
          ("unknown", 1))
    )


_HpicfSyslogOperationsStatus_Type.__name__ = "Integer32"
_HpicfSyslogOperationsStatus_Object = MibScalar
hpicfSyslogOperationsStatus = _HpicfSyslogOperationsStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 2, 8),
    _HpicfSyslogOperationsStatus_Type()
)
hpicfSyslogOperationsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogOperationsStatus.setStatus("current")
_HpicfSyslogPriority_ObjectIdentity = ObjectIdentity
hpicfSyslogPriority = _HpicfSyslogPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 3)
)


class _HpicfSyslogPriorityFacility_Type(HpicfSyslogFacility):
    """Custom type hpicfSyslogPriorityFacility based on HpicfSyslogFacility"""


_HpicfSyslogPriorityFacility_Object = MibScalar
hpicfSyslogPriorityFacility = _HpicfSyslogPriorityFacility_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 3, 1),
    _HpicfSyslogPriorityFacility_Type()
)
hpicfSyslogPriorityFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSyslogPriorityFacility.setStatus("current")


class _HpicfSyslogPrioritySeverity_Type(HpicfSyslogSeverity):
    """Custom type hpicfSyslogPrioritySeverity based on HpicfSyslogSeverity"""


_HpicfSyslogPrioritySeverity_Object = MibScalar
hpicfSyslogPrioritySeverity = _HpicfSyslogPrioritySeverity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 3, 2),
    _HpicfSyslogPrioritySeverity_Type()
)
hpicfSyslogPrioritySeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSyslogPrioritySeverity.setStatus("current")
_HpicfSyslogPriorityDescr_Type = SnmpAdminString
_HpicfSyslogPriorityDescr_Object = MibScalar
hpicfSyslogPriorityDescr = _HpicfSyslogPriorityDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 3, 3),
    _HpicfSyslogPriorityDescr_Type()
)
hpicfSyslogPriorityDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSyslogPriorityDescr.setStatus("current")


class _HpicfSyslogSystemModule_Type(HpicfSyslogSystemModule):
    """Custom type hpicfSyslogSystemModule based on HpicfSyslogSystemModule"""


_HpicfSyslogSystemModule_Object = MibScalar
hpicfSyslogSystemModule = _HpicfSyslogSystemModule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 3, 4),
    _HpicfSyslogSystemModule_Type()
)
hpicfSyslogSystemModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSyslogSystemModule.setStatus("current")


class _HpicfSyslogOriginId_Type(HpicfSyslogOriginId):
    """Custom type hpicfSyslogOriginId based on HpicfSyslogOriginId"""


_HpicfSyslogOriginId_Object = MibScalar
hpicfSyslogOriginId = _HpicfSyslogOriginId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 3, 5),
    _HpicfSyslogOriginId_Type()
)
hpicfSyslogOriginId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSyslogOriginId.setStatus("current")
_HpicfSyslogStatistics_ObjectIdentity = ObjectIdentity
hpicfSyslogStatistics = _HpicfSyslogStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4)
)
_HpicfSyslogGeneralStatistics_ObjectIdentity = ObjectIdentity
hpicfSyslogGeneralStatistics = _HpicfSyslogGeneralStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 1)
)
_HpicfSyslogGeneralLogSent_Type = Counter32
_HpicfSyslogGeneralLogSent_Object = MibScalar
hpicfSyslogGeneralLogSent = _HpicfSyslogGeneralLogSent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 1, 1),
    _HpicfSyslogGeneralLogSent_Type()
)
hpicfSyslogGeneralLogSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogGeneralLogSent.setStatus("current")
_HpicfSyslogGeneralLogRecv_Type = Counter32
_HpicfSyslogGeneralLogRecv_Object = MibScalar
hpicfSyslogGeneralLogRecv = _HpicfSyslogGeneralLogRecv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 1, 2),
    _HpicfSyslogGeneralLogRecv_Type()
)
hpicfSyslogGeneralLogRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogGeneralLogRecv.setStatus("current")
_HpicfSyslogGeneralLogRelay_Type = Counter32
_HpicfSyslogGeneralLogRelay_Object = MibScalar
hpicfSyslogGeneralLogRelay = _HpicfSyslogGeneralLogRelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 1, 3),
    _HpicfSyslogGeneralLogRelay_Type()
)
hpicfSyslogGeneralLogRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogGeneralLogRelay.setStatus("current")
_HpicfSyslogGeneralSendError_Type = Counter32
_HpicfSyslogGeneralSendError_Object = MibScalar
hpicfSyslogGeneralSendError = _HpicfSyslogGeneralSendError_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 1, 4),
    _HpicfSyslogGeneralSendError_Type()
)
hpicfSyslogGeneralSendError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogGeneralSendError.setStatus("current")
_HpicfSyslogGeneralLogResend_Type = Counter32
_HpicfSyslogGeneralLogResend_Object = MibScalar
hpicfSyslogGeneralLogResend = _HpicfSyslogGeneralLogResend_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 1, 5),
    _HpicfSyslogGeneralLogResend_Type()
)
hpicfSyslogGeneralLogResend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogGeneralLogResend.setStatus("current")
_HpicfSyslogGeneralResendError_Type = Counter32
_HpicfSyslogGeneralResendError_Object = MibScalar
hpicfSyslogGeneralResendError = _HpicfSyslogGeneralResendError_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 1, 6),
    _HpicfSyslogGeneralResendError_Type()
)
hpicfSyslogGeneralResendError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogGeneralResendError.setStatus("current")
_HpicfSyslogGeneralLogBuffered_Type = Counter32
_HpicfSyslogGeneralLogBuffered_Object = MibScalar
hpicfSyslogGeneralLogBuffered = _HpicfSyslogGeneralLogBuffered_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 1, 7),
    _HpicfSyslogGeneralLogBuffered_Type()
)
hpicfSyslogGeneralLogBuffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogGeneralLogBuffered.setStatus("current")
_HpicfSyslogSeverityStatistics_ObjectIdentity = ObjectIdentity
hpicfSyslogSeverityStatistics = _HpicfSyslogSeverityStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 2)
)
_HpicfSyslogSeverityCounterInfoTable_Object = MibTable
hpicfSyslogSeverityCounterInfoTable = _HpicfSyslogSeverityCounterInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfSyslogSeverityCounterInfoTable.setStatus("current")
_HpicfSyslogSeverityCounterInfoEntry_Object = MibTableRow
hpicfSyslogSeverityCounterInfoEntry = _HpicfSyslogSeverityCounterInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 2, 1, 1)
)
hpicfSyslogSeverityCounterInfoEntry.setIndexNames(
    (0, "HP-ICF-SYSLOG-MIB", "hpicfSyslogSeverityTypeIndex"),
)
if mibBuilder.loadTexts:
    hpicfSyslogSeverityCounterInfoEntry.setStatus("current")
_HpicfSyslogSeverityTypeIndex_Type = Integer32
_HpicfSyslogSeverityTypeIndex_Object = MibTableColumn
hpicfSyslogSeverityTypeIndex = _HpicfSyslogSeverityTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 2, 1, 1, 1),
    _HpicfSyslogSeverityTypeIndex_Type()
)
hpicfSyslogSeverityTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSyslogSeverityTypeIndex.setStatus("current")
_HpicfSyslogSeverityType_Type = HpicfSyslogSeverity
_HpicfSyslogSeverityType_Object = MibTableColumn
hpicfSyslogSeverityType = _HpicfSyslogSeverityType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 2, 1, 1, 2),
    _HpicfSyslogSeverityType_Type()
)
hpicfSyslogSeverityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogSeverityType.setStatus("current")
_HpicfSyslogSeverityCounter_Type = Counter32
_HpicfSyslogSeverityCounter_Object = MibTableColumn
hpicfSyslogSeverityCounter = _HpicfSyslogSeverityCounter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 2, 1, 1, 3),
    _HpicfSyslogSeverityCounter_Type()
)
hpicfSyslogSeverityCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogSeverityCounter.setStatus("current")
_HpicfSyslogFacilityStatistics_ObjectIdentity = ObjectIdentity
hpicfSyslogFacilityStatistics = _HpicfSyslogFacilityStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 3)
)
_HpicfSyslogFacilityCounterInfoTable_Object = MibTable
hpicfSyslogFacilityCounterInfoTable = _HpicfSyslogFacilityCounterInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    hpicfSyslogFacilityCounterInfoTable.setStatus("current")
_HpicfSyslogFacilityCounterInfoEntry_Object = MibTableRow
hpicfSyslogFacilityCounterInfoEntry = _HpicfSyslogFacilityCounterInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 3, 1, 1)
)
hpicfSyslogFacilityCounterInfoEntry.setIndexNames(
    (0, "HP-ICF-SYSLOG-MIB", "hpicfSyslogfacilityCounterIndex"),
)
if mibBuilder.loadTexts:
    hpicfSyslogFacilityCounterInfoEntry.setStatus("current")
_HpicfSyslogfacilityCounterIndex_Type = Integer32
_HpicfSyslogfacilityCounterIndex_Object = MibTableColumn
hpicfSyslogfacilityCounterIndex = _HpicfSyslogfacilityCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 3, 1, 1, 1),
    _HpicfSyslogfacilityCounterIndex_Type()
)
hpicfSyslogfacilityCounterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSyslogfacilityCounterIndex.setStatus("current")
_HpicfSyslogfacilityType_Type = HpicfSyslogFacility
_HpicfSyslogfacilityType_Object = MibTableColumn
hpicfSyslogfacilityType = _HpicfSyslogfacilityType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 3, 1, 1, 2),
    _HpicfSyslogfacilityType_Type()
)
hpicfSyslogfacilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogfacilityType.setStatus("current")
_HpicfSyslogfacilityCounter_Type = Counter32
_HpicfSyslogfacilityCounter_Object = MibTableColumn
hpicfSyslogfacilityCounter = _HpicfSyslogfacilityCounter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 3, 1, 1, 3),
    _HpicfSyslogfacilityCounter_Type()
)
hpicfSyslogfacilityCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogfacilityCounter.setStatus("current")
_HpicfSyslogLogMsgOptions_ObjectIdentity = ObjectIdentity
hpicfSyslogLogMsgOptions = _HpicfSyslogLogMsgOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 5)
)
_HpicfSyslogClearLog_Type = TruthValue
_HpicfSyslogClearLog_Object = MibScalar
hpicfSyslogClearLog = _HpicfSyslogClearLog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 5, 1),
    _HpicfSyslogClearLog_Type()
)
hpicfSyslogClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSyslogClearLog.setStatus("current")
_HpicfSyslogSecClearLog_Type = TruthValue
_HpicfSyslogSecClearLog_Object = MibScalar
hpicfSyslogSecClearLog = _HpicfSyslogSecClearLog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 5, 2),
    _HpicfSyslogSecClearLog_Type()
)
hpicfSyslogSecClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSyslogSecClearLog.setStatus("current")
_HpicfSyslogServerStatisticsTable_Object = MibTable
hpicfSyslogServerStatisticsTable = _HpicfSyslogServerStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hpicfSyslogServerStatisticsTable.setStatus("current")
_HpicfSyslogServerStatisticsEntry_Object = MibTableRow
hpicfSyslogServerStatisticsEntry = _HpicfSyslogServerStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 6, 1)
)
hpicfSyslogServerStatisticsEntry.setIndexNames(
    (0, "HP-ICF-SYSLOG-MIB", "hpicfSyslogControlIndex"),
)
if mibBuilder.loadTexts:
    hpicfSyslogServerStatisticsEntry.setStatus("current")
_HpicfSyslogServerLogSent_Type = Counter32
_HpicfSyslogServerLogSent_Object = MibTableColumn
hpicfSyslogServerLogSent = _HpicfSyslogServerLogSent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 6, 1, 1),
    _HpicfSyslogServerLogSent_Type()
)
hpicfSyslogServerLogSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogServerLogSent.setStatus("current")
_HpicfSyslogServerLogRecv_Type = Counter32
_HpicfSyslogServerLogRecv_Object = MibTableColumn
hpicfSyslogServerLogRecv = _HpicfSyslogServerLogRecv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 6, 1, 2),
    _HpicfSyslogServerLogRecv_Type()
)
hpicfSyslogServerLogRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogServerLogRecv.setStatus("current")
_HpicfSyslogServerLogRelay_Type = Counter32
_HpicfSyslogServerLogRelay_Object = MibTableColumn
hpicfSyslogServerLogRelay = _HpicfSyslogServerLogRelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 6, 1, 3),
    _HpicfSyslogServerLogRelay_Type()
)
hpicfSyslogServerLogRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogServerLogRelay.setStatus("current")
_HpicfSyslogServerSendError_Type = Counter32
_HpicfSyslogServerSendError_Object = MibTableColumn
hpicfSyslogServerSendError = _HpicfSyslogServerSendError_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 6, 1, 4),
    _HpicfSyslogServerSendError_Type()
)
hpicfSyslogServerSendError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogServerSendError.setStatus("current")
_HpicfSyslogServerLogResend_Type = Counter32
_HpicfSyslogServerLogResend_Object = MibTableColumn
hpicfSyslogServerLogResend = _HpicfSyslogServerLogResend_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 6, 1, 5),
    _HpicfSyslogServerLogResend_Type()
)
hpicfSyslogServerLogResend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogServerLogResend.setStatus("current")
_HpicfSyslogServerResendError_Type = Counter32
_HpicfSyslogServerResendError_Object = MibTableColumn
hpicfSyslogServerResendError = _HpicfSyslogServerResendError_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 6, 1, 6),
    _HpicfSyslogServerResendError_Type()
)
hpicfSyslogServerResendError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogServerResendError.setStatus("current")
_HpicfSyslogServerLogBuffered_Type = Counter32
_HpicfSyslogServerLogBuffered_Object = MibTableColumn
hpicfSyslogServerLogBuffered = _HpicfSyslogServerLogBuffered_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 6, 1, 7),
    _HpicfSyslogServerLogBuffered_Type()
)
hpicfSyslogServerLogBuffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSyslogServerLogBuffered.setStatus("current")
_HpicfSyslogAlerts_ObjectIdentity = ObjectIdentity
hpicfSyslogAlerts = _HpicfSyslogAlerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 7)
)
_HpicfSyslogAlertsTable_Object = MibTable
hpicfSyslogAlertsTable = _HpicfSyslogAlertsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hpicfSyslogAlertsTable.setStatus("current")
_HpicfSyslogAlertsEntry_Object = MibTableRow
hpicfSyslogAlertsEntry = _HpicfSyslogAlertsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 7, 1, 1)
)
hpicfSyslogAlertsEntry.setIndexNames(
    (0, "HP-ICF-SYSLOG-MIB", "hpicfSyslogAlertIndex"),
)
if mibBuilder.loadTexts:
    hpicfSyslogAlertsEntry.setStatus("current")


class _HpicfSyslogAlertIndex_Type(Integer32):
    """Custom type hpicfSyslogAlertIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("runningCfgChg", 1)
    )


_HpicfSyslogAlertIndex_Type.__name__ = "Integer32"
_HpicfSyslogAlertIndex_Object = MibTableColumn
hpicfSyslogAlertIndex = _HpicfSyslogAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 7, 1, 1, 1),
    _HpicfSyslogAlertIndex_Type()
)
hpicfSyslogAlertIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSyslogAlertIndex.setStatus("current")


class _HpicfSyslogAlertAdminStatus_Type(Integer32):
    """Custom type hpicfSyslogAlertAdminStatus based on Integer32"""
    defaultValue = 2

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


_HpicfSyslogAlertAdminStatus_Type.__name__ = "Integer32"
_HpicfSyslogAlertAdminStatus_Object = MibTableColumn
hpicfSyslogAlertAdminStatus = _HpicfSyslogAlertAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 7, 1, 1, 2),
    _HpicfSyslogAlertAdminStatus_Type()
)
hpicfSyslogAlertAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSyslogAlertAdminStatus.setStatus("current")


class _HpicfSyslogAlertTransmitInterval_Type(Unsigned32):
    """Custom type hpicfSyslogAlertTransmitInterval based on Unsigned32"""
    defaultValue = 0


_HpicfSyslogAlertTransmitInterval_Object = MibTableColumn
hpicfSyslogAlertTransmitInterval = _HpicfSyslogAlertTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 7, 1, 1, 3),
    _HpicfSyslogAlertTransmitInterval_Type()
)
hpicfSyslogAlertTransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSyslogAlertTransmitInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpicfSyslogAlertTransmitInterval.setUnits("seconds")
_HpicfSyslogConformance_ObjectIdentity = ObjectIdentity
hpicfSyslogConformance = _HpicfSyslogConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3)
)
_HpicfSyslogGroups_ObjectIdentity = ObjectIdentity
hpicfSyslogGroups = _HpicfSyslogGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1)
)
_HpicfSyslogCompliances_ObjectIdentity = ObjectIdentity
hpicfSyslogCompliances = _HpicfSyslogCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2)
)

# Managed Objects groups

hpicfSyslogOperationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 1)
)
hpicfSyslogOperationsGroup.setObjects(
      *(("HP-ICF-SYSLOG-MIB", "hpicfSyslogOperationsMsgsTransmitted"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogOperationsMsgsDropped"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogOperationsLastMsgTransmittedTime"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogOperationsStartTime"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogOperationsLastError"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogOperationsLastErrorTime"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogOperationsCounterDiscontinuityTime"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogOperationsStatus"))
)
if mibBuilder.loadTexts:
    hpicfSyslogOperationsGroup.setStatus("current")

hpicfSyslogControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 2)
)
hpicfSyslogControlGroup.setObjects(
      *(("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlDescr"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlBindAddrType"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlBindAddr"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfSyslogControlGroup.setStatus("current")

hpicfSyslogPriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 3)
)
hpicfSyslogPriorityGroup.setObjects(
    ("HP-ICF-SYSLOG-MIB", "hpicfSyslogPriorityDescr")
)
if mibBuilder.loadTexts:
    hpicfSyslogPriorityGroup.setStatus("current")

hpicfSyslogControlGroupOobm = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 6)
)
hpicfSyslogControlGroupOobm.setObjects(
      *(("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlBindAddr"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlBindAddrIsOobm"))
)
if mibBuilder.loadTexts:
    hpicfSyslogControlGroupOobm.setStatus("current")

hpicfSyslogGeneralStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 7)
)
hpicfSyslogGeneralStatisticsGroup.setObjects(
      *(("HP-ICF-SYSLOG-MIB", "hpicfSyslogGeneralLogSent"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogGeneralLogRecv"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogGeneralLogRelay"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogGeneralSendError"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogGeneralLogResend"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogGeneralResendError"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogGeneralLogBuffered"))
)
if mibBuilder.loadTexts:
    hpicfSyslogGeneralStatisticsGroup.setStatus("current")

hpicfSyslogSeverityStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 8)
)
hpicfSyslogSeverityStatisticsGroup.setObjects(
      *(("HP-ICF-SYSLOG-MIB", "hpicfSyslogSeverityType"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogSeverityCounter"))
)
if mibBuilder.loadTexts:
    hpicfSyslogSeverityStatisticsGroup.setStatus("current")

hpicfSyslogFacilityStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 9)
)
hpicfSyslogFacilityStatisticsGroup.setObjects(
      *(("HP-ICF-SYSLOG-MIB", "hpicfSyslogfacilityType"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogfacilityCounter"))
)
if mibBuilder.loadTexts:
    hpicfSyslogFacilityStatisticsGroup.setStatus("current")

hpicfSyslogControlGroupSmm = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 10)
)
hpicfSyslogControlGroupSmm.setObjects(
      *(("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlBindAddr"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlSmmLog"))
)
if mibBuilder.loadTexts:
    hpicfSyslogControlGroupSmm.setStatus("current")

hpicfSyslogLogMsgOptionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 11)
)
hpicfSyslogLogMsgOptionsGroup.setObjects(
    ("HP-ICF-SYSLOG-MIB", "hpicfSyslogClearLog")
)
if mibBuilder.loadTexts:
    hpicfSyslogLogMsgOptionsGroup.setStatus("deprecated")

hpicfSyslogControlTransportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 12)
)
hpicfSyslogControlTransportGroup.setObjects(
      *(("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlTransportProtocol"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlDestinationPort"))
)
if mibBuilder.loadTexts:
    hpicfSyslogControlTransportGroup.setStatus("current")

hpicfSyslogServerStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 13)
)
hpicfSyslogServerStatisticsGroup.setObjects(
      *(("HP-ICF-SYSLOG-MIB", "hpicfSyslogServerLogSent"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogServerLogRecv"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogServerLogRelay"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogServerSendError"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogServerLogResend"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogServerResendError"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogServerLogBuffered"))
)
if mibBuilder.loadTexts:
    hpicfSyslogServerStatisticsGroup.setStatus("current")

hpicfSyslogPriorityGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 14)
)
hpicfSyslogPriorityGroup1.setObjects(
      *(("HP-ICF-SYSLOG-MIB", "hpicfSyslogPriorityFacility"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogPrioritySeverity"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogSystemModule"))
)
if mibBuilder.loadTexts:
    hpicfSyslogPriorityGroup1.setStatus("current")

hpicfSyslogAlertsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 15)
)
hpicfSyslogAlertsGroup.setObjects(
      *(("HP-ICF-SYSLOG-MIB", "hpicfSyslogAlertAdminStatus"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogAlertTransmitInterval"))
)
if mibBuilder.loadTexts:
    hpicfSyslogAlertsGroup.setStatus("current")

hpicfSyslogOriginIdGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 16)
)
hpicfSyslogOriginIdGroup1.setObjects(
    ("HP-ICF-SYSLOG-MIB", "hpicfSyslogOriginId")
)
if mibBuilder.loadTexts:
    hpicfSyslogOriginIdGroup1.setStatus("current")

hpicfSyslogLogMsgOptionsGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 17)
)
hpicfSyslogLogMsgOptionsGroup1.setObjects(
      *(("HP-ICF-SYSLOG-MIB", "hpicfSyslogClearLog"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogSecClearLog"))
)
if mibBuilder.loadTexts:
    hpicfSyslogLogMsgOptionsGroup1.setStatus("current")


# Notification objects

hpicfSyslogStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 0, 1)
)
hpicfSyslogStatusChanged.setObjects(
      *(("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlIndex"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlDescr"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlBindAddrType"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlBindAddr"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlRowStatus"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogPriorityDescr"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogPrioritySeverity"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogPriorityFacility"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogSystemModule"),
        ("HP-ICF-SYSLOG-MIB", "hpicfSyslogOperationsStatus"))
)
if mibBuilder.loadTexts:
    hpicfSyslogStatusChanged.setStatus(
        "current"
    )


# Notifications groups

hpicfSyslogNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 5)
)
hpicfSyslogNotificationGroup.setObjects(
    ("HP-ICF-SYSLOG-MIB", "hpicfSyslogStatusChanged")
)
if mibBuilder.loadTexts:
    hpicfSyslogNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfSyslogFullCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfSyslogFullCompliance1.setStatus(
        "current"
    )

hpicfSyslogFullCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfSyslogFullCompliance2.setStatus(
        "current"
    )

hpicfSyslogReadOnlyCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    hpicfSyslogReadOnlyCompliance1.setStatus(
        "current"
    )

hpicfSyslogReadOnlyCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 5)
)
if mibBuilder.loadTexts:
    hpicfSyslogReadOnlyCompliance2.setStatus(
        "current"
    )

hpicfSyslogNotificationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 7)
)
if mibBuilder.loadTexts:
    hpicfSyslogNotificationCompliance.setStatus(
        "current"
    )

hpicfSyslogFullComplianceOobm = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 8)
)
if mibBuilder.loadTexts:
    hpicfSyslogFullComplianceOobm.setStatus(
        "current"
    )

hpicfSyslogStatisticsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 9)
)
if mibBuilder.loadTexts:
    hpicfSyslogStatisticsCompliance.setStatus(
        "current"
    )

hpicfSyslogSmmLogMsgCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 10)
)
if mibBuilder.loadTexts:
    hpicfSyslogSmmLogMsgCompliance.setStatus(
        "deprecated"
    )

hpicfSyslogTransportCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 11)
)
if mibBuilder.loadTexts:
    hpicfSyslogTransportCompliance.setStatus(
        "current"
    )

hpicfSyslogPriorityCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 12)
)
if mibBuilder.loadTexts:
    hpicfSyslogPriorityCompliance.setStatus(
        "current"
    )

hpicfSyslogServerStatisticsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 13)
)
if mibBuilder.loadTexts:
    hpicfSyslogServerStatisticsCompliance.setStatus(
        "current"
    )

hpicfSyslogAlertsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 14)
)
if mibBuilder.loadTexts:
    hpicfSyslogAlertsCompliance.setStatus(
        "current"
    )

hpicfSyslogOriginIdCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 15)
)
if mibBuilder.loadTexts:
    hpicfSyslogOriginIdCompliance.setStatus(
        "current"
    )

hpicfSyslogSmmLogMsgCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 16)
)
if mibBuilder.loadTexts:
    hpicfSyslogSmmLogMsgCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-SYSLOG-MIB",
    **{"HpicfSyslogFacility": HpicfSyslogFacility,
       "HpicfSyslogSeverity": HpicfSyslogSeverity,
       "HpicfSyslogSystemModule": HpicfSyslogSystemModule,
       "HpicfSyslogOriginId": HpicfSyslogOriginId,
       "hpicfSyslogMIB": hpicfSyslogMIB,
       "hpicfSyslogNotifications": hpicfSyslogNotifications,
       "hpicfSyslogStatusChanged": hpicfSyslogStatusChanged,
       "hpicfSyslogObjects": hpicfSyslogObjects,
       "hpicfSyslogControlTable": hpicfSyslogControlTable,
       "hpicfSyslogControlEntry": hpicfSyslogControlEntry,
       "hpicfSyslogControlIndex": hpicfSyslogControlIndex,
       "hpicfSyslogControlDescr": hpicfSyslogControlDescr,
       "hpicfSyslogControlBindAddrType": hpicfSyslogControlBindAddrType,
       "hpicfSyslogControlBindAddr": hpicfSyslogControlBindAddr,
       "hpicfSyslogControlRowStatus": hpicfSyslogControlRowStatus,
       "hpicfSyslogControlBindAddrIsOobm": hpicfSyslogControlBindAddrIsOobm,
       "hpicfSyslogControlSmmLog": hpicfSyslogControlSmmLog,
       "hpicfSyslogControlTransportProtocol": hpicfSyslogControlTransportProtocol,
       "hpicfSyslogControlDestinationPort": hpicfSyslogControlDestinationPort,
       "hpicfSyslogOperations": hpicfSyslogOperations,
       "hpicfSyslogOperationsMsgsTransmitted": hpicfSyslogOperationsMsgsTransmitted,
       "hpicfSyslogOperationsMsgsDropped": hpicfSyslogOperationsMsgsDropped,
       "hpicfSyslogOperationsLastMsgTransmittedTime": hpicfSyslogOperationsLastMsgTransmittedTime,
       "hpicfSyslogOperationsStartTime": hpicfSyslogOperationsStartTime,
       "hpicfSyslogOperationsLastError": hpicfSyslogOperationsLastError,
       "hpicfSyslogOperationsLastErrorTime": hpicfSyslogOperationsLastErrorTime,
       "hpicfSyslogOperationsCounterDiscontinuityTime": hpicfSyslogOperationsCounterDiscontinuityTime,
       "hpicfSyslogOperationsStatus": hpicfSyslogOperationsStatus,
       "hpicfSyslogPriority": hpicfSyslogPriority,
       "hpicfSyslogPriorityFacility": hpicfSyslogPriorityFacility,
       "hpicfSyslogPrioritySeverity": hpicfSyslogPrioritySeverity,
       "hpicfSyslogPriorityDescr": hpicfSyslogPriorityDescr,
       "hpicfSyslogSystemModule": hpicfSyslogSystemModule,
       "hpicfSyslogOriginId": hpicfSyslogOriginId,
       "hpicfSyslogStatistics": hpicfSyslogStatistics,
       "hpicfSyslogGeneralStatistics": hpicfSyslogGeneralStatistics,
       "hpicfSyslogGeneralLogSent": hpicfSyslogGeneralLogSent,
       "hpicfSyslogGeneralLogRecv": hpicfSyslogGeneralLogRecv,
       "hpicfSyslogGeneralLogRelay": hpicfSyslogGeneralLogRelay,
       "hpicfSyslogGeneralSendError": hpicfSyslogGeneralSendError,
       "hpicfSyslogGeneralLogResend": hpicfSyslogGeneralLogResend,
       "hpicfSyslogGeneralResendError": hpicfSyslogGeneralResendError,
       "hpicfSyslogGeneralLogBuffered": hpicfSyslogGeneralLogBuffered,
       "hpicfSyslogSeverityStatistics": hpicfSyslogSeverityStatistics,
       "hpicfSyslogSeverityCounterInfoTable": hpicfSyslogSeverityCounterInfoTable,
       "hpicfSyslogSeverityCounterInfoEntry": hpicfSyslogSeverityCounterInfoEntry,
       "hpicfSyslogSeverityTypeIndex": hpicfSyslogSeverityTypeIndex,
       "hpicfSyslogSeverityType": hpicfSyslogSeverityType,
       "hpicfSyslogSeverityCounter": hpicfSyslogSeverityCounter,
       "hpicfSyslogFacilityStatistics": hpicfSyslogFacilityStatistics,
       "hpicfSyslogFacilityCounterInfoTable": hpicfSyslogFacilityCounterInfoTable,
       "hpicfSyslogFacilityCounterInfoEntry": hpicfSyslogFacilityCounterInfoEntry,
       "hpicfSyslogfacilityCounterIndex": hpicfSyslogfacilityCounterIndex,
       "hpicfSyslogfacilityType": hpicfSyslogfacilityType,
       "hpicfSyslogfacilityCounter": hpicfSyslogfacilityCounter,
       "hpicfSyslogLogMsgOptions": hpicfSyslogLogMsgOptions,
       "hpicfSyslogClearLog": hpicfSyslogClearLog,
       "hpicfSyslogSecClearLog": hpicfSyslogSecClearLog,
       "hpicfSyslogServerStatisticsTable": hpicfSyslogServerStatisticsTable,
       "hpicfSyslogServerStatisticsEntry": hpicfSyslogServerStatisticsEntry,
       "hpicfSyslogServerLogSent": hpicfSyslogServerLogSent,
       "hpicfSyslogServerLogRecv": hpicfSyslogServerLogRecv,
       "hpicfSyslogServerLogRelay": hpicfSyslogServerLogRelay,
       "hpicfSyslogServerSendError": hpicfSyslogServerSendError,
       "hpicfSyslogServerLogResend": hpicfSyslogServerLogResend,
       "hpicfSyslogServerResendError": hpicfSyslogServerResendError,
       "hpicfSyslogServerLogBuffered": hpicfSyslogServerLogBuffered,
       "hpicfSyslogAlerts": hpicfSyslogAlerts,
       "hpicfSyslogAlertsTable": hpicfSyslogAlertsTable,
       "hpicfSyslogAlertsEntry": hpicfSyslogAlertsEntry,
       "hpicfSyslogAlertIndex": hpicfSyslogAlertIndex,
       "hpicfSyslogAlertAdminStatus": hpicfSyslogAlertAdminStatus,
       "hpicfSyslogAlertTransmitInterval": hpicfSyslogAlertTransmitInterval,
       "hpicfSyslogConformance": hpicfSyslogConformance,
       "hpicfSyslogGroups": hpicfSyslogGroups,
       "hpicfSyslogOperationsGroup": hpicfSyslogOperationsGroup,
       "hpicfSyslogControlGroup": hpicfSyslogControlGroup,
       "hpicfSyslogPriorityGroup": hpicfSyslogPriorityGroup,
       "hpicfSyslogNotificationGroup": hpicfSyslogNotificationGroup,
       "hpicfSyslogControlGroupOobm": hpicfSyslogControlGroupOobm,
       "hpicfSyslogGeneralStatisticsGroup": hpicfSyslogGeneralStatisticsGroup,
       "hpicfSyslogSeverityStatisticsGroup": hpicfSyslogSeverityStatisticsGroup,
       "hpicfSyslogFacilityStatisticsGroup": hpicfSyslogFacilityStatisticsGroup,
       "hpicfSyslogControlGroupSmm": hpicfSyslogControlGroupSmm,
       "hpicfSyslogLogMsgOptionsGroup": hpicfSyslogLogMsgOptionsGroup,
       "hpicfSyslogControlTransportGroup": hpicfSyslogControlTransportGroup,
       "hpicfSyslogServerStatisticsGroup": hpicfSyslogServerStatisticsGroup,
       "hpicfSyslogPriorityGroup1": hpicfSyslogPriorityGroup1,
       "hpicfSyslogAlertsGroup": hpicfSyslogAlertsGroup,
       "hpicfSyslogOriginIdGroup1": hpicfSyslogOriginIdGroup1,
       "hpicfSyslogLogMsgOptionsGroup1": hpicfSyslogLogMsgOptionsGroup1,
       "hpicfSyslogCompliances": hpicfSyslogCompliances,
       "hpicfSyslogFullCompliance1": hpicfSyslogFullCompliance1,
       "hpicfSyslogFullCompliance2": hpicfSyslogFullCompliance2,
       "hpicfSyslogReadOnlyCompliance1": hpicfSyslogReadOnlyCompliance1,
       "hpicfSyslogReadOnlyCompliance2": hpicfSyslogReadOnlyCompliance2,
       "hpicfSyslogNotificationCompliance": hpicfSyslogNotificationCompliance,
       "hpicfSyslogFullComplianceOobm": hpicfSyslogFullComplianceOobm,
       "hpicfSyslogStatisticsCompliance": hpicfSyslogStatisticsCompliance,
       "hpicfSyslogSmmLogMsgCompliance": hpicfSyslogSmmLogMsgCompliance,
       "hpicfSyslogTransportCompliance": hpicfSyslogTransportCompliance,
       "hpicfSyslogPriorityCompliance": hpicfSyslogPriorityCompliance,
       "hpicfSyslogServerStatisticsCompliance": hpicfSyslogServerStatisticsCompliance,
       "hpicfSyslogAlertsCompliance": hpicfSyslogAlertsCompliance,
       "hpicfSyslogOriginIdCompliance": hpicfSyslogOriginIdCompliance,
       "hpicfSyslogSmmLogMsgCompliance1": hpicfSyslogSmmLogMsgCompliance1}
)
