# SNMP MIB module (A3COM-HUAWEI-DAR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-DAR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:26 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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

h3cDar = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 112)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cDarProtocol(Integer32, TextualConvention):
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

_H3cDarIfObjects_ObjectIdentity = ObjectIdentity
h3cDarIfObjects = _H3cDarIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 112, 1)
)
_H3cDarIfStatisticsObjects_ObjectIdentity = ObjectIdentity
h3cDarIfStatisticsObjects = _H3cDarIfStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 112, 1, 1)
)
_H3cDarStatisticsTable_Object = MibTable
h3cDarStatisticsTable = _H3cDarStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 112, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cDarStatisticsTable.setStatus("current")
_H3cDarStatisticsEntry_Object = MibTableRow
h3cDarStatisticsEntry = _H3cDarStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 112, 1, 1, 1, 1)
)
h3cDarStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-DAR-MIB", "h3cDarStatisticsProtocolID"),
)
if mibBuilder.loadTexts:
    h3cDarStatisticsEntry.setStatus("current")
_H3cDarStatisticsProtocolID_Type = H3cDarProtocol
_H3cDarStatisticsProtocolID_Object = MibTableColumn
h3cDarStatisticsProtocolID = _H3cDarStatisticsProtocolID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 112, 1, 1, 1, 1, 1),
    _H3cDarStatisticsProtocolID_Type()
)
h3cDarStatisticsProtocolID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDarStatisticsProtocolID.setStatus("current")
_H3cDarStatisticsProtocolName_Type = OctetString
_H3cDarStatisticsProtocolName_Object = MibTableColumn
h3cDarStatisticsProtocolName = _H3cDarStatisticsProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 112, 1, 1, 1, 1, 2),
    _H3cDarStatisticsProtocolName_Type()
)
h3cDarStatisticsProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDarStatisticsProtocolName.setStatus("current")
_H3cDarStatisticsInPkts_Type = Counter64
_H3cDarStatisticsInPkts_Object = MibTableColumn
h3cDarStatisticsInPkts = _H3cDarStatisticsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 112, 1, 1, 1, 1, 3),
    _H3cDarStatisticsInPkts_Type()
)
h3cDarStatisticsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDarStatisticsInPkts.setStatus("current")
_H3cDarStatisticsInBytes_Type = Counter64
_H3cDarStatisticsInBytes_Object = MibTableColumn
h3cDarStatisticsInBytes = _H3cDarStatisticsInBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 112, 1, 1, 1, 1, 4),
    _H3cDarStatisticsInBytes_Type()
)
h3cDarStatisticsInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDarStatisticsInBytes.setStatus("current")
_H3cDarStatisticsInBitRate_Type = Counter64
_H3cDarStatisticsInBitRate_Object = MibTableColumn
h3cDarStatisticsInBitRate = _H3cDarStatisticsInBitRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 112, 1, 1, 1, 1, 5),
    _H3cDarStatisticsInBitRate_Type()
)
h3cDarStatisticsInBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDarStatisticsInBitRate.setStatus("current")
_H3cDarStatisticsMaxInBitRate_Type = Counter64
_H3cDarStatisticsMaxInBitRate_Object = MibTableColumn
h3cDarStatisticsMaxInBitRate = _H3cDarStatisticsMaxInBitRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 112, 1, 1, 1, 1, 6),
    _H3cDarStatisticsMaxInBitRate_Type()
)
h3cDarStatisticsMaxInBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDarStatisticsMaxInBitRate.setStatus("current")
_H3cDarStatisticsOutPkts_Type = Counter64
_H3cDarStatisticsOutPkts_Object = MibTableColumn
h3cDarStatisticsOutPkts = _H3cDarStatisticsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 112, 1, 1, 1, 1, 7),
    _H3cDarStatisticsOutPkts_Type()
)
h3cDarStatisticsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDarStatisticsOutPkts.setStatus("current")
_H3cDarStatisticsOutBytes_Type = Counter64
_H3cDarStatisticsOutBytes_Object = MibTableColumn
h3cDarStatisticsOutBytes = _H3cDarStatisticsOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 112, 1, 1, 1, 1, 8),
    _H3cDarStatisticsOutBytes_Type()
)
h3cDarStatisticsOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDarStatisticsOutBytes.setStatus("current")
_H3cDarStatisticsOutBitRate_Type = Counter64
_H3cDarStatisticsOutBitRate_Object = MibTableColumn
h3cDarStatisticsOutBitRate = _H3cDarStatisticsOutBitRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 112, 1, 1, 1, 1, 9),
    _H3cDarStatisticsOutBitRate_Type()
)
h3cDarStatisticsOutBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDarStatisticsOutBitRate.setStatus("current")
_H3cDarStatisticsMaxOutBitRate_Type = Counter64
_H3cDarStatisticsMaxOutBitRate_Object = MibTableColumn
h3cDarStatisticsMaxOutBitRate = _H3cDarStatisticsMaxOutBitRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 112, 1, 1, 1, 1, 10),
    _H3cDarStatisticsMaxOutBitRate_Type()
)
h3cDarStatisticsMaxOutBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDarStatisticsMaxOutBitRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-DAR-MIB",
    **{"H3cDarProtocol": H3cDarProtocol,
       "h3cDar": h3cDar,
       "h3cDarIfObjects": h3cDarIfObjects,
       "h3cDarIfStatisticsObjects": h3cDarIfStatisticsObjects,
       "h3cDarStatisticsTable": h3cDarStatisticsTable,
       "h3cDarStatisticsEntry": h3cDarStatisticsEntry,
       "h3cDarStatisticsProtocolID": h3cDarStatisticsProtocolID,
       "h3cDarStatisticsProtocolName": h3cDarStatisticsProtocolName,
       "h3cDarStatisticsInPkts": h3cDarStatisticsInPkts,
       "h3cDarStatisticsInBytes": h3cDarStatisticsInBytes,
       "h3cDarStatisticsInBitRate": h3cDarStatisticsInBitRate,
       "h3cDarStatisticsMaxInBitRate": h3cDarStatisticsMaxInBitRate,
       "h3cDarStatisticsOutPkts": h3cDarStatisticsOutPkts,
       "h3cDarStatisticsOutBytes": h3cDarStatisticsOutBytes,
       "h3cDarStatisticsOutBitRate": h3cDarStatisticsOutBitRate,
       "h3cDarStatisticsMaxOutBitRate": h3cDarStatisticsMaxOutBitRate}
)
