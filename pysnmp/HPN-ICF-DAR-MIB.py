# SNMP MIB module (HPN-ICF-DAR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DAR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:37 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

hpnicfDar = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfDarProtocol(Integer32, TextualConvention):
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
              89)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 2),
          ("cifs", 3),
          ("citrix", 4),
          ("cuseeme", 5),
          ("dhcp", 6),
          ("dns", 7),
          ("egp", 8),
          ("eigrp", 9),
          ("exchange", 10),
          ("fasttrack", 11),
          ("finger", 12),
          ("ftp", 13),
          ("gnutella", 14),
          ("gopher", 15),
          ("gre", 16),
          ("h323", 18),
          ("http", 17),
          ("icmp", 19),
          ("igmp", 20),
          ("imap", 21),
          ("invalidProtocol", 1),
          ("ip", 22),
          ("ipinip", 23),
          ("ipsec", 24),
          ("ipv6", 25),
          ("irc", 26),
          ("kerberos", 27),
          ("l2tp", 28),
          ("ldap", 29),
          ("mgcp", 30),
          ("napster", 31),
          ("netbios", 32),
          ("netshow", 33),
          ("nfs", 34),
          ("nntp", 35),
          ("notes", 36),
          ("novadign", 37),
          ("ntp", 38),
          ("pcanywhere", 39),
          ("pop3", 40),
          ("pptp", 41),
          ("printer", 42),
          ("rcmd", 43),
          ("rip", 44),
          ("rsvp", 45),
          ("rtcp", 46),
          ("rtp", 47),
          ("rtsp", 48),
          ("secureftp", 49),
          ("securehttp", 50),
          ("secureimap", 51),
          ("secureirc", 52),
          ("secureldap", 53),
          ("securenntp", 54),
          ("securepop3", 55),
          ("securetelnet", 56),
          ("sip", 57),
          ("skinny", 58),
          ("smtp", 59),
          ("snmp", 60),
          ("socks", 61),
          ("sqlnet", 62),
          ("sqlserver", 63),
          ("ssh", 64),
          ("streamwork", 65),
          ("sunrpc", 66),
          ("syslog", 67),
          ("tcp", 68),
          ("tcphandshake", 69),
          ("telnet", 70),
          ("tftp", 71),
          ("total", 72),
          ("udp", 73),
          ("unknownothers", 74),
          ("unknowntcp", 75),
          ("unknownudp", 76),
          ("userdefine001", 77),
          ("userdefine002", 78),
          ("userdefine003", 79),
          ("userdefine004", 80),
          ("userdefine005", 81),
          ("userdefine006", 82),
          ("userdefine007", 83),
          ("userdefine008", 84),
          ("userdefine009", 85),
          ("userdefine010", 86),
          ("vdolive", 87),
          ("winmx", 88),
          ("xwindows", 89))
    )



# MIB Managed Objects in the order of their OIDs

_HpnicfDarIfObjects_ObjectIdentity = ObjectIdentity
hpnicfDarIfObjects = _HpnicfDarIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1)
)
_HpnicfDarIfStatisticsObjects_ObjectIdentity = ObjectIdentity
hpnicfDarIfStatisticsObjects = _HpnicfDarIfStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1)
)
_HpnicfDarStatisticsTable_Object = MibTable
hpnicfDarStatisticsTable = _HpnicfDarStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfDarStatisticsTable.setStatus("current")
_HpnicfDarStatisticsEntry_Object = MibTableRow
hpnicfDarStatisticsEntry = _HpnicfDarStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1, 1, 1)
)
hpnicfDarStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-DAR-MIB", "hpnicfDarStatisticsProtocolID"),
)
if mibBuilder.loadTexts:
    hpnicfDarStatisticsEntry.setStatus("current")
_HpnicfDarStatisticsProtocolID_Type = HpnicfDarProtocol
_HpnicfDarStatisticsProtocolID_Object = MibTableColumn
hpnicfDarStatisticsProtocolID = _HpnicfDarStatisticsProtocolID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1, 1, 1, 1),
    _HpnicfDarStatisticsProtocolID_Type()
)
hpnicfDarStatisticsProtocolID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDarStatisticsProtocolID.setStatus("current")
_HpnicfDarStatisticsProtocolName_Type = OctetString
_HpnicfDarStatisticsProtocolName_Object = MibTableColumn
hpnicfDarStatisticsProtocolName = _HpnicfDarStatisticsProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1, 1, 1, 2),
    _HpnicfDarStatisticsProtocolName_Type()
)
hpnicfDarStatisticsProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDarStatisticsProtocolName.setStatus("current")
_HpnicfDarStatisticsInPkts_Type = Counter64
_HpnicfDarStatisticsInPkts_Object = MibTableColumn
hpnicfDarStatisticsInPkts = _HpnicfDarStatisticsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1, 1, 1, 3),
    _HpnicfDarStatisticsInPkts_Type()
)
hpnicfDarStatisticsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDarStatisticsInPkts.setStatus("current")
_HpnicfDarStatisticsInBytes_Type = Counter64
_HpnicfDarStatisticsInBytes_Object = MibTableColumn
hpnicfDarStatisticsInBytes = _HpnicfDarStatisticsInBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1, 1, 1, 4),
    _HpnicfDarStatisticsInBytes_Type()
)
hpnicfDarStatisticsInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDarStatisticsInBytes.setStatus("current")
_HpnicfDarStatisticsInBitRate_Type = Counter64
_HpnicfDarStatisticsInBitRate_Object = MibTableColumn
hpnicfDarStatisticsInBitRate = _HpnicfDarStatisticsInBitRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1, 1, 1, 5),
    _HpnicfDarStatisticsInBitRate_Type()
)
hpnicfDarStatisticsInBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDarStatisticsInBitRate.setStatus("current")
_HpnicfDarStatisticsMaxInBitRate_Type = Counter64
_HpnicfDarStatisticsMaxInBitRate_Object = MibTableColumn
hpnicfDarStatisticsMaxInBitRate = _HpnicfDarStatisticsMaxInBitRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1, 1, 1, 6),
    _HpnicfDarStatisticsMaxInBitRate_Type()
)
hpnicfDarStatisticsMaxInBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDarStatisticsMaxInBitRate.setStatus("current")
_HpnicfDarStatisticsOutPkts_Type = Counter64
_HpnicfDarStatisticsOutPkts_Object = MibTableColumn
hpnicfDarStatisticsOutPkts = _HpnicfDarStatisticsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1, 1, 1, 7),
    _HpnicfDarStatisticsOutPkts_Type()
)
hpnicfDarStatisticsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDarStatisticsOutPkts.setStatus("current")
_HpnicfDarStatisticsOutBytes_Type = Counter64
_HpnicfDarStatisticsOutBytes_Object = MibTableColumn
hpnicfDarStatisticsOutBytes = _HpnicfDarStatisticsOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1, 1, 1, 8),
    _HpnicfDarStatisticsOutBytes_Type()
)
hpnicfDarStatisticsOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDarStatisticsOutBytes.setStatus("current")
_HpnicfDarStatisticsOutBitRate_Type = Counter64
_HpnicfDarStatisticsOutBitRate_Object = MibTableColumn
hpnicfDarStatisticsOutBitRate = _HpnicfDarStatisticsOutBitRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1, 1, 1, 9),
    _HpnicfDarStatisticsOutBitRate_Type()
)
hpnicfDarStatisticsOutBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDarStatisticsOutBitRate.setStatus("current")
_HpnicfDarStatisticsMaxOutBitRate_Type = Counter64
_HpnicfDarStatisticsMaxOutBitRate_Object = MibTableColumn
hpnicfDarStatisticsMaxOutBitRate = _HpnicfDarStatisticsMaxOutBitRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112, 1, 1, 1, 1, 10),
    _HpnicfDarStatisticsMaxOutBitRate_Type()
)
hpnicfDarStatisticsMaxOutBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDarStatisticsMaxOutBitRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DAR-MIB",
    **{"HpnicfDarProtocol": HpnicfDarProtocol,
       "hpnicfDar": hpnicfDar,
       "hpnicfDarIfObjects": hpnicfDarIfObjects,
       "hpnicfDarIfStatisticsObjects": hpnicfDarIfStatisticsObjects,
       "hpnicfDarStatisticsTable": hpnicfDarStatisticsTable,
       "hpnicfDarStatisticsEntry": hpnicfDarStatisticsEntry,
       "hpnicfDarStatisticsProtocolID": hpnicfDarStatisticsProtocolID,
       "hpnicfDarStatisticsProtocolName": hpnicfDarStatisticsProtocolName,
       "hpnicfDarStatisticsInPkts": hpnicfDarStatisticsInPkts,
       "hpnicfDarStatisticsInBytes": hpnicfDarStatisticsInBytes,
       "hpnicfDarStatisticsInBitRate": hpnicfDarStatisticsInBitRate,
       "hpnicfDarStatisticsMaxInBitRate": hpnicfDarStatisticsMaxInBitRate,
       "hpnicfDarStatisticsOutPkts": hpnicfDarStatisticsOutPkts,
       "hpnicfDarStatisticsOutBytes": hpnicfDarStatisticsOutBytes,
       "hpnicfDarStatisticsOutBitRate": hpnicfDarStatisticsOutBitRate,
       "hpnicfDarStatisticsMaxOutBitRate": hpnicfDarStatisticsMaxOutBitRate}
)
