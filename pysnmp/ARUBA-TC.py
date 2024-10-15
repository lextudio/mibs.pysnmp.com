# SNMP MIB module (ARUBA-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARUBA-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:45 2024
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
 ObjectSyntax,
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
    "ObjectSyntax",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class ArubaEnableValue(Integer32, TextualConvention):
    status = "current"
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



class ArubaFrameType(Integer32, TextualConvention):
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
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("associateRequest", 0),
          ("associateResponse", 1),
          ("atim", 9),
          ("auth", 11),
          ("beacon", 8),
          ("deauth", 12),
          ("disassociate", 10),
          ("probeRequest", 4),
          ("probeResponse", 5),
          ("reassociateRequest", 2),
          ("reassociateResponse", 3))
    )



class ArubaPhyType(Integer32, TextualConvention):
    status = "current"
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
        *(("dot11a", 1),
          ("dot11ag", 4),
          ("dot11b", 2),
          ("dot11g", 3),
          ("wired", 5))
    )



class ArubaHTMode(Integer32, TextualConvention):
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
        *(("ht20", 2),
          ("ht40", 3),
          ("none", 1),
          ("vht160", 7),
          ("vht20", 4),
          ("vht40", 5),
          ("vht80", 6),
          ("vht80plus80", 8))
    )



class ArubaHTExtChannel(Integer32, TextualConvention):
    status = "current"
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
        *(("above", 2),
          ("below", 3),
          ("eighty", 4),
          ("none", 1),
          ("onesixty", 5))
    )



class ArubaMonEncryptionType(Integer32, TextualConvention):
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
        *(("open", 0),
          ("wep", 1),
          ("wpa", 2),
          ("wpa2", 3))
    )



class ArubaMonEncryptionCipher(Integer32, TextualConvention):
    status = "current"
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
        *(("aesccmp", 4),
          ("none", 0),
          ("other", 5),
          ("tkip", 3),
          ("wep104", 2),
          ("wep40", 1))
    )



class ArubaMonAuthAlgorithm(Integer32, TextualConvention):
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
        *(("dot1x", 2),
          ("none", 0),
          ("other", 3),
          ("psk", 1))
    )



class ArubaSwitchRole(Integer32, TextualConvention):
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
        *(("backupmaster", 3),
          ("local", 2),
          ("master", 1))
    )



class ArubaSupportStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 2),
          ("unsupported", 1))
    )



class ArubaActiveState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )



class ArubaACLDomain(Integer32, TextualConvention):
    status = "current"
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
        *(("alias", 1),
          ("any", 2),
          ("host", 4),
          ("network", 5),
          ("user", 3))
    )



class ArubaACLNetworkServiceType(Integer32, TextualConvention):
    status = "current"
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
        *(("alias", 1),
          ("any", 2),
          ("protocol", 5),
          ("tcp", 3),
          ("udp", 4))
    )



class ArubaACLAction(Integer32, TextualConvention):
    status = "current"
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
        *(("deny", 1),
          ("dstNAT", 4),
          ("permit", 2),
          ("redirect", 5),
          ("srcNAT", 3))
    )



class ArubaDaysOfWeek(Integer32, TextualConvention):
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
        *(("fri", 6),
          ("mon", 2),
          ("sat", 7),
          ("sun", 1),
          ("thu", 5),
          ("tue", 3),
          ("wed", 4))
    )



class ArubaAuthenticationMethods(Integer32, TextualConvention):
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
              7,
              15,
              16,
              17,
              28,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dot1x", 4),
          ("kerberos", 5),
          ("mac", 2),
          ("none", 0),
          ("other", 255),
          ("pubcookie", 15),
          ("secureId", 7),
          ("via-vpn", 28),
          ("vpn", 3),
          ("web", 1),
          ("xSec", 16),
          ("xSecMachine", 17))
    )



class ArubaSubAuthenticationMethods(Integer32, TextualConvention):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("authCHAP", 2),
          ("authMSCHAP", 3),
          ("authMSCHAPv2", 4),
          ("authPAP", 1),
          ("eapLEAP", 7),
          ("eapMD5", 8),
          ("eapPEAP", 9),
          ("eapTLS", 5),
          ("eapTTLS", 6))
    )



class ArubaEncryptionType(Integer32, TextualConvention):
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("aes-128-cmac", 14),
          ("bSec-128", 12),
          ("bSec-256", 13),
          ("dynamic-wep", 2),
          ("none", 0),
          ("static-wep", 1),
          ("unknown", 15),
          ("wpa-aes", 6),
          ("wpa-psk-aes", 5),
          ("wpa-psk-tkip", 3),
          ("wpa-tkip", 4),
          ("wpa2-aes", 10),
          ("wpa2-psk-aes", 9),
          ("wpa2-psk-tkip", 7),
          ("wpa2-tkip", 8),
          ("xSec", 11))
    )



class ArubaUserForwardMode(Integer32, TextualConvention):
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
        *(("bridge", 1),
          ("split-tunnel", 3),
          ("tunnel-decrypted", 2),
          ("tunnel-encrypted", 0))
    )



class ArubaRogueApType(Integer32, TextualConvention):
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
        *(("dos", 4),
          ("interfering", 2),
          ("knownInterfering", 6),
          ("suspectedUnsecure", 7),
          ("unknown", 5),
          ("unsecure", 3),
          ("valid", 1))
    )



class ArubaAPMatchType(Integer32, TextualConvention):
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("apBSSID", 10),
          ("apRule", 12),
          ("apWiredMac", 3),
          ("baseBSSIDOverride", 6),
          ("classificationDisabled", 9),
          ("configuredWiredMac", 1),
          ("ethernetGatewayWiredMac", 8),
          ("ethernetWiredMac", 2),
          ("externalWiredMac", 4),
          ("manual", 5),
          ("mms", 7),
          ("propagatedEthernetWiredMac", 11),
          ("systemGatewayMac", 14),
          ("systemWiredMac", 13),
          ("unknown", 0))
    )



class ArubaAPMatchMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("exactMatch", 1),
          ("minusOneMatch", 3),
          ("notApplicable", 0),
          ("ouiMatch", 4),
          ("plusOneMatch", 2))
    )



class ArubaStationType(Integer32, TextualConvention):
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
        *(("dos", 3),
          ("interfering", 2),
          ("unknown", 0),
          ("valid", 1))
    )



class ArubaEncryptionMethods(Bits, TextualConvention):
    status = "current"


class ArubaHashAlgorithms(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha", 2))
    )



class ArubaVlanValidRange(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )



class ArubaPortMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("dot1q", 2))
    )



class ArubaDot1dState(Integer32, TextualConvention):
    status = "current"
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
        *(("blocked", 2),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )



class ArubaAPDot1dState(Integer32, TextualConvention):
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
        *(("blocking", 7),
          ("disabled", 3),
          ("forwarding", 6),
          ("learning", 5),
          ("listening", 4),
          ("notAvailable", 1),
          ("off", 2))
    )



class ArubaPoeState(Integer32, TextualConvention):
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
        *(("disabled", 1),
          ("enabled", 2),
          ("enabledCisco", 3),
          ("notAvailable", 4))
    )



class ArubaCardType(Integer32, TextualConvention):
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
              29)
        )
    )
    namedValues = NamedValues(
        *(("lc1", 1),
          ("lc2", 2),
          ("m3mk1", 8),
          ("reserved1", 14),
          ("reserved2", 15),
          ("sc1", 3),
          ("sc2", 4),
          ("sw1500", 22),
          ("sw200", 7),
          ("sw2400", 5),
          ("sw2500", 21),
          ("sw3200", 9),
          ("sw3400", 10),
          ("sw3500", 20),
          ("sw3600", 11),
          ("sw620", 16),
          ("sw650", 12),
          ("sw651", 13),
          ("sw7005", 24),
          ("sw7008", 29),
          ("sw7010", 23),
          ("sw7024", 27),
          ("sw7030", 25),
          ("sw7205", 26),
          ("sw7210", 17),
          ("sw7220", 18),
          ("sw7240", 19),
          ("sw7240xm", 28),
          ("sw800", 6))
    )



class ArubaESIServerMode(Integer32, TextualConvention):
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
        *(("bridged", 1),
          ("nat", 3),
          ("routed", 2))
    )



class ArubaESIServerStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )



class ArubaIfType(Integer32, TextualConvention):
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
        *(("loopback", 4),
          ("port", 1),
          ("tunnel", 3),
          ("vlan", 2))
    )



class ArubaVoipProtocolType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              9,
              11,
              13,
              15)
        )
    )
    namedValues = NamedValues(
        *(("h323", 13),
          ("sccp", 1),
          ("sip", 9),
          ("svp", 2),
          ("ua", 11),
          ("unknown", 15),
          ("vocera", 3))
    )



class ArubaAccessPointMode(Integer32, TextualConvention):
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
        *(("accessPoint", 2),
          ("accessPointAndMonitor", 3),
          ("airMonitor", 1),
          ("meshPoint", 5),
          ("meshPortal", 4),
          ("rfprotectSensor", 6),
          ("spectrumSensor", 7))
    )



class ArubaAuthServerType(Integer32, TextualConvention):
    status = "current"
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
        *(("internaldb", 1),
          ("kerberos", 4),
          ("ldap", 3),
          ("radius", 2),
          ("tacacs", 5))
    )



class ArubaAddressType(Integer32, TextualConvention):
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
        *(("bssid", 3),
          ("dstAddress", 2),
          ("srcAddress", 1))
    )



class ArubaBlackListReason(Integer32, TextualConvention):
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("authFailure", 3),
          ("esiBlacklist", 9),
          ("ipSpoofing", 8),
          ("mitmAttack", 2),
          ("other", 100),
          ("pingFlood", 4),
          ("sessionBlacklist", 7),
          ("sessionFlood", 5),
          ("synFlood", 6),
          ("userDefined", 1))
    )



class ArubaDBType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mssql", 1),
          ("mysql", 2))
    )



class ArubaVrrpState(Integer32, TextualConvention):
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
        *(("backup", 2),
          ("initialize", 1),
          ("master", 3))
    )



class ArubaOperStateValue(Integer32, TextualConvention):
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )



class ArubaAntennaSetting(Integer32, TextualConvention):
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
        *(("disabled", 3),
          ("enabled", 2),
          ("notPresent", 1))
    )



class ArubaAPStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )



class ArubaPortSpeed(Integer32, TextualConvention):
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
        *(("speed1000Mbps", 3),
          ("speed100Mbps", 2),
          ("speed10Gbps", 5),
          ("speed10Mbps", 1),
          ("speed2Gbps", 6),
          ("speed5Gbps", 7),
          ("speedAuto", 4))
    )



class ArubaPortDuplex(Integer32, TextualConvention):
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
        *(("auto", 3),
          ("full", 2),
          ("half", 1))
    )



class ArubaPortType(Integer32, TextualConvention):
    status = "current"
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
        *(("fastethernet", 1),
          ("fivegigabitethernet", 5),
          ("gigabitethernet", 2),
          ("twogigabitethernet", 4),
          ("xgigabitethernet", 3))
    )



class ArubaEnet1Mode(Integer32, TextualConvention):
    status = "current"
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
        *(("activeStandby", 1),
          ("bridge", 3),
          ("notApplicable", 4),
          ("split", 5),
          ("tunnel", 2))
    )



class ArubaUnprovisionedStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )



class ArubaMonitorMode(Integer32, TextualConvention):
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
        *(("all", 1),
          ("mixed", 3),
          ("none", 2),
          ("unknown", 0))
    )



class ArubaConfigurationState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("success", 1))
    )



class ArubaConfigurationChangeType(Integer32, TextualConvention):
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
        *(("create", 1),
          ("delete", 2),
          ("modify", 3))
    )



class ArubaCallStates(Integer32, TextualConvention):
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 14),
          ("alerting", 6),
          ("blocked", 15),
          ("blockwait", 11),
          ("cancelling", 8),
          ("challenging", 9),
          ("connected", 4),
          ("connecting", 2),
          ("delivered", 3),
          ("fail", 13),
          ("idle", 0),
          ("initiated", 1),
          ("offered", 5),
          ("releasing", 7),
          ("succ", 12),
          ("transient", 10))
    )



class ArubaVoipProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              9,
              11,
              13)
        )
    )
    namedValues = NamedValues(
        *(("h323", 13),
          ("sccp", 1),
          ("sip", 9),
          ("svp", 2),
          ("ua", 11),
          ("vocera", 3))
    )



class ArubaVoipRegState(Integer32, TextualConvention):
    status = "current"
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
        *(("challenge", 3),
          ("registered", 4),
          ("registering", 1),
          ("unknown", 0),
          ("unregistered", 5),
          ("unregistering", 2))
    )



class ArubaVoiceCdrDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ic", 1),
          ("og", 0))
    )



class ArubaVoiceCacBit(Bits, TextualConvention):
    status = "current"


class ArubaMeshRole(Integer32, TextualConvention):
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
        *(("nonmesh", 0),
          ("point", 1),
          ("portal", 2))
    )



class ArubaHTRate(Integer32, TextualConvention):
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
              34)
        )
    )
    namedValues = NamedValues(
        *(("ht104", 20),
          ("ht108", 21),
          ("ht117", 22),
          ("ht120", 23),
          ("ht121dot5", 24),
          ("ht13", 2),
          ("ht130", 25),
          ("ht135", 26),
          ("ht13dot5", 3),
          ("ht15", 4),
          ("ht150", 27),
          ("ht162", 28),
          ("ht180", 29),
          ("ht19dot5", 5),
          ("ht216", 30),
          ("ht240", 31),
          ("ht243", 32),
          ("ht26", 6),
          ("ht27", 7),
          ("ht270", 33),
          ("ht30", 8),
          ("ht300", 34),
          ("ht39", 9),
          ("ht40dot5", 10),
          ("ht45", 11),
          ("ht52", 12),
          ("ht54", 13),
          ("ht58dot5", 14),
          ("ht60", 15),
          ("ht65", 16),
          ("ht6dot5", 1),
          ("ht78", 17),
          ("ht81", 18),
          ("ht90", 19),
          ("unknown", 0))
    )



class ArubaARMChangeReason(Integer32, TextualConvention):
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
              29)
        )
    )
    namedValues = NamedValues(
        *(("airmatchFreeze", 23),
          ("airmatchInit", 26),
          ("airmatchNoise", 21),
          ("airmatchNoiseCleared", 28),
          ("airmatchRogueCont", 29),
          ("airmatchSolver", 22),
          ("airmatchUnfreeze", 24),
          ("armChannelQualityThresh", 18),
          ("armDecreasePower", 14),
          ("armDynamicBW", 19),
          ("armEmptyCh", 12),
          ("armErrorThresh", 10),
          ("armIncreasePower", 15),
          ("armInterference", 8),
          ("armInterferenceCCA", 20),
          ("armInvalidCh", 9),
          ("armNoiseThresh", 11),
          ("armRogueCont", 13),
          ("armTurnOffRadio", 16),
          ("armTurnOnRadio", 17),
          ("cancel40mhzIntol", 6),
          ("fortyMhzAlign", 7),
          ("fortyMhzIntol", 5),
          ("radarCleared", 2),
          ("radarDetected", 1),
          ("random", 25),
          ("txHang", 3),
          ("txHangClear", 4),
          ("unknown", 27))
    )



class ArubaAPMasterStatus(Integer32, TextualConvention):
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
        *(("down", 2),
          ("move", 3),
          ("up", 1))
    )



class ArubaDot3azStatus(Bits, TextualConvention):
    status = "current"


class ArubaThresholdResourceType(Integer32, TextualConvention):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("controlPathCpu", 1),
          ("controlPathMemory", 2),
          ("dataPathCpu", 0),
          ("noofAps", 5),
          ("noofLocals", 6),
          ("totalTunnelCapacity", 3),
          ("userCapacity", 4))
    )



class ArubaStackState(Integer32, TextualConvention):
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
        *(("away", 4),
          ("linecard", 3),
          ("primary", 1),
          ("secondary", 2))
    )



class ArubaStackChangeEvent(Integer32, TextualConvention):
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
        *(("lineCardSlotChanged", 4),
          ("other", 1),
          ("primarySlotChanged", 2),
          ("priorityChanged", 6),
          ("roleChanged", 5),
          ("secondarySlotChanged", 3),
          ("slotExceeded", 8),
          ("versionMismatch", 7))
    )



class ArubaStackIfTopoJoined(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2))
    )



class InterfaceIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class ArubaIfState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )



class ArubaIfStateChangeReason(Integer32, TextualConvention):
    status = "current"
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
        *(("admin", 1),
          ("bpduGuard", 5),
          ("loopProtect", 2),
          ("macLimit", 3),
          ("raGuard", 4))
    )



class ArubaAPUplinkType(Integer32, TextualConvention):
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
        *(("ethernet", 1),
          ("pppoe", 3),
          ("usb", 2),
          ("wifi", 4))
    )



class ArubaAPUplinkChangeReason(Integer32, TextualConvention):
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
        *(("linkFailure", 1),
          ("preemption", 3),
          ("vpnFailure", 2))
    )



class ArubaPortalServerDownReason(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("connectFail", 1)
    )



class ArubaHaRole(Integer32, TextualConvention):
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
        *(("active", 1),
          ("disabled", 3),
          ("dual", 0),
          ("standby", 2))
    )



class ArubaHaConnectivityStatus(Integer32, TextualConvention):
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
        *(("haApDenied", 4),
          ("haCpUnreach", 2),
          ("haHbtFailure", 5),
          ("haImageMissMatch", 3),
          ("haInvalidHelloResponse", 6),
          ("haNetUnreach", 1),
          ("haStandbyTunnelDown", 7),
          ("haSuccess", 0))
    )



class ArubaFlexRadioMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dual2GHzplus5GHzBand", 2),
          ("notApplicable", 4),
          ("single2GHzBand", 0),
          ("single5GHzBand", 1),
          ("unknown", 3))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBA-TC",
    **{"ArubaEnableValue": ArubaEnableValue,
       "ArubaFrameType": ArubaFrameType,
       "ArubaPhyType": ArubaPhyType,
       "ArubaHTMode": ArubaHTMode,
       "ArubaHTExtChannel": ArubaHTExtChannel,
       "ArubaMonEncryptionType": ArubaMonEncryptionType,
       "ArubaMonEncryptionCipher": ArubaMonEncryptionCipher,
       "ArubaMonAuthAlgorithm": ArubaMonAuthAlgorithm,
       "ArubaSwitchRole": ArubaSwitchRole,
       "ArubaSupportStatus": ArubaSupportStatus,
       "ArubaActiveState": ArubaActiveState,
       "ArubaACLDomain": ArubaACLDomain,
       "ArubaACLNetworkServiceType": ArubaACLNetworkServiceType,
       "ArubaACLAction": ArubaACLAction,
       "ArubaDaysOfWeek": ArubaDaysOfWeek,
       "ArubaAuthenticationMethods": ArubaAuthenticationMethods,
       "ArubaSubAuthenticationMethods": ArubaSubAuthenticationMethods,
       "ArubaEncryptionType": ArubaEncryptionType,
       "ArubaUserForwardMode": ArubaUserForwardMode,
       "ArubaRogueApType": ArubaRogueApType,
       "ArubaAPMatchType": ArubaAPMatchType,
       "ArubaAPMatchMethod": ArubaAPMatchMethod,
       "ArubaStationType": ArubaStationType,
       "ArubaEncryptionMethods": ArubaEncryptionMethods,
       "ArubaHashAlgorithms": ArubaHashAlgorithms,
       "ArubaVlanValidRange": ArubaVlanValidRange,
       "ArubaPortMode": ArubaPortMode,
       "ArubaDot1dState": ArubaDot1dState,
       "ArubaAPDot1dState": ArubaAPDot1dState,
       "ArubaPoeState": ArubaPoeState,
       "ArubaCardType": ArubaCardType,
       "ArubaESIServerMode": ArubaESIServerMode,
       "ArubaESIServerStatus": ArubaESIServerStatus,
       "ArubaIfType": ArubaIfType,
       "ArubaVoipProtocolType": ArubaVoipProtocolType,
       "ArubaAccessPointMode": ArubaAccessPointMode,
       "ArubaAuthServerType": ArubaAuthServerType,
       "ArubaAddressType": ArubaAddressType,
       "ArubaBlackListReason": ArubaBlackListReason,
       "ArubaDBType": ArubaDBType,
       "ArubaVrrpState": ArubaVrrpState,
       "ArubaOperStateValue": ArubaOperStateValue,
       "ArubaAntennaSetting": ArubaAntennaSetting,
       "ArubaAPStatus": ArubaAPStatus,
       "ArubaPortSpeed": ArubaPortSpeed,
       "ArubaPortDuplex": ArubaPortDuplex,
       "ArubaPortType": ArubaPortType,
       "ArubaEnet1Mode": ArubaEnet1Mode,
       "ArubaUnprovisionedStatus": ArubaUnprovisionedStatus,
       "ArubaMonitorMode": ArubaMonitorMode,
       "ArubaConfigurationState": ArubaConfigurationState,
       "ArubaConfigurationChangeType": ArubaConfigurationChangeType,
       "ArubaCallStates": ArubaCallStates,
       "ArubaVoipProtocol": ArubaVoipProtocol,
       "ArubaVoipRegState": ArubaVoipRegState,
       "ArubaVoiceCdrDirection": ArubaVoiceCdrDirection,
       "ArubaVoiceCacBit": ArubaVoiceCacBit,
       "ArubaMeshRole": ArubaMeshRole,
       "ArubaHTRate": ArubaHTRate,
       "ArubaARMChangeReason": ArubaARMChangeReason,
       "ArubaAPMasterStatus": ArubaAPMasterStatus,
       "ArubaDot3azStatus": ArubaDot3azStatus,
       "ArubaThresholdResourceType": ArubaThresholdResourceType,
       "ArubaStackState": ArubaStackState,
       "ArubaStackChangeEvent": ArubaStackChangeEvent,
       "ArubaStackIfTopoJoined": ArubaStackIfTopoJoined,
       "InterfaceIndex": InterfaceIndex,
       "ArubaIfState": ArubaIfState,
       "ArubaIfStateChangeReason": ArubaIfStateChangeReason,
       "ArubaAPUplinkType": ArubaAPUplinkType,
       "ArubaAPUplinkChangeReason": ArubaAPUplinkChangeReason,
       "ArubaPortalServerDownReason": ArubaPortalServerDownReason,
       "ArubaHaRole": ArubaHaRole,
       "ArubaHaConnectivityStatus": ArubaHaConnectivityStatus,
       "ArubaFlexRadioMode": ArubaFlexRadioMode}
)
