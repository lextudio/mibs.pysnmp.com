# SNMP MIB module (CISCO-FIREWALL-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FIREWALL-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:34 2024
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

ciscoFirewallTc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 488)
)
ciscoFirewallTc.setRevisions(
        ("2006-03-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CFWNetworkProtocol(Integer32, TextualConvention):
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
        *(("gre", 5),
          ("icmp", 4),
          ("ip", 3),
          ("none", 1),
          ("other", 2),
          ("tcp", 7),
          ("udp", 6))
    )



class CFWApplicationProtocol(Integer32, TextualConvention):
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
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
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
              170)
        )
    )
    namedValues = NamedValues(
        *(("aceSvr", 137),
          ("aim", 162),
          ("appleQtc", 82),
          ("bgp", 69),
          ("biff", 85),
          ("bootpc", 51),
          ("bootps", 50),
          ("cddbp", 104),
          ("cifs", 147),
          ("ciscoFna", 58),
          ("ciscoNetMgmt", 133),
          ("ciscoSvcs", 132),
          ("ciscoSys", 60),
          ("ciscoTdp", 100),
          ("ciscoTna", 59),
          ("citrix", 144),
          ("citrixImaClient", 142),
          ("clp", 141),
          ("creativePartnr", 81),
          ("creativeServer", 80),
          ("cuseeme", 31),
          ("daytime", 45),
          ("dbControlAgent", 159),
          ("dbase", 73),
          ("ddnsV3", 136),
          ("dhcpFailover", 96),
          ("discard", 44),
          ("dns", 8),
          ("dnsix", 52),
          ("echo", 43),
          ("entrustSvcHandler", 99),
          ("entrustSvcs", 98),
          ("exec", 23),
          ("fcipPort", 150),
          ("finger", 13),
          ("ftp", 3),
          ("ftps", 105),
          ("gdoi", 102),
          ("giop", 138),
          ("gopher", 12),
          ("gtpV0", 41),
          ("gtpV1", 42),
          ("h323", 30),
          ("h323CallSigAlt", 168),
          ("h323Gatestat", 124),
          ("hpAlarmMgr", 78),
          ("hpCollector", 76),
          ("hpManagedNode", 77),
          ("hsrp", 127),
          ("http", 6),
          ("https", 10),
          ("ica", 115),
          ("icabrowser", 119),
          ("ident", 54),
          ("ieee80211Iapp", 156),
          ("igmpV3Lite", 83),
          ("imap", 21),
          ("imap3", 74),
          ("imaps", 107),
          ("ipass", 140),
          ("ipsecMsft", 160),
          ("ipx", 72),
          ("irc", 70),
          ("ircServ", 91),
          ("ircs", 108),
          ("ircu", 166),
          ("isakmp", 84),
          ("iscsi", 103),
          ("iscsiTarget", 152),
          ("kazaa", 111),
          ("kerberos", 14),
          ("kermit", 120),
          ("l2tp", 122),
          ("ldap", 22),
          ("ldapAdmin", 155),
          ("ldaps", 95),
          ("login", 24),
          ("lotusMtap", 146),
          ("lotusnote", 29),
          ("mgcp", 38),
          ("microsoftDs", 79),
          ("msClusterNet", 154),
          ("msDotnetster", 148),
          ("msRpc", 18),
          ("msSna", 113),
          ("msSql", 26),
          ("msSqlM", 112),
          ("msexchRouting", 97),
          ("msnMsgr", 170),
          ("mySql", 153),
          ("n2h2Server", 167),
          ("ncp", 89),
          ("net8Cman", 128),
          ("netbiosDgm", 62),
          ("netbiosNs", 61),
          ("netbiosSsn", 63),
          ("netshow", 33),
          ("netstat", 46),
          ("nfs", 28),
          ("nntp", 19),
          ("none", 1),
          ("ntp", 56),
          ("oemAgent", 157),
          ("oracle", 131),
          ("oracleEmVp", 129),
          ("oracleNames", 130),
          ("orasrv", 116),
          ("other", 2),
          ("pcAnyWhereData", 163),
          ("pcAnyWhereStat", 164),
          ("pop2", 15),
          ("pop3", 16),
          ("pop3s", 109),
          ("pptp", 123),
          ("pwdgen", 57),
          ("qmtp", 71),
          ("rWinsock", 125),
          ("radius", 126),
          ("rdbDbsDisp", 117),
          ("realSecure", 145),
          ("realmedia", 32),
          ("router", 88),
          ("rsvd", 66),
          ("rsvpEncap", 121),
          ("rsvpTunnel", 75),
          ("rtcPmPort", 158),
          ("rtelnet", 53),
          ("rtsp", 39),
          ("sap", 36),
          ("send", 67),
          ("shell", 25),
          ("sip", 37),
          ("sipTls", 161),
          ("skinny", 40),
          ("sms", 143),
          ("smtp", 5),
          ("snmp", 20),
          ("snmpTrap", 65),
          ("socks", 110),
          ("sqlServ", 55),
          ("sqlSrv", 64),
          ("sqlnet", 9),
          ("ssh", 47),
          ("sshell", 94),
          ("ssp", 151),
          ("streamworks", 34),
          ("stun", 134),
          ("sunRpc", 17),
          ("sybaseSql", 27),
          ("syslog", 87),
          ("syslogConn", 93),
          ("tacacs", 7),
          ("tacacsDs", 49),
          ("tarantella", 149),
          ("telnet", 4),
          ("telnets", 106),
          ("tftp", 11),
          ("time", 48),
          ("timed", 90),
          ("trRsrb", 135),
          ("ttc", 139),
          ("uucp", 92),
          ("vdolive", 35),
          ("vqp", 118),
          ("webster", 101),
          ("who", 86),
          ("wins", 114),
          ("x11", 165),
          ("xdmcp", 68),
          ("yahooMsgr", 169))
    )



class CFWPolicy(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class CFWPolicyTarget(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class CFWPolicyTargetType(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("context", 8),
          ("interface", 3),
          ("other", 2),
          ("user", 6),
          ("usergroup", 7),
          ("zone", 4),
          ("zonepair", 5))
    )



class CFWUrlfVendorId(Integer32, TextualConvention):
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
        *(("n2h2", 3),
          ("other", 1),
          ("websense", 2))
    )



class CFWUrlServerStatus(Integer32, TextualConvention):
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
        *(("indeterminate", 3),
          ("offline", 2),
          ("online", 1))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREWALL-TC",
    **{"CFWNetworkProtocol": CFWNetworkProtocol,
       "CFWApplicationProtocol": CFWApplicationProtocol,
       "CFWPolicy": CFWPolicy,
       "CFWPolicyTarget": CFWPolicyTarget,
       "CFWPolicyTargetType": CFWPolicyTargetType,
       "CFWUrlfVendorId": CFWUrlfVendorId,
       "CFWUrlServerStatus": CFWUrlServerStatus,
       "ciscoFirewallTc": ciscoFirewallTc}
)
