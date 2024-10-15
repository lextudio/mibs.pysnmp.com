# SNMP MIB module (FORTINET-FORTIGATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FORTINET-FORTIGATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:33 2024
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

(FnBoolState,
 FnIndex,
 fnAdminEntry,
 fnSysSerial,
 fortinet) = mibBuilder.importSymbols(
    "FORTINET-CORE-MIB",
    "FnBoolState",
    "FnIndex",
    "fnAdminEntry",
    "fnSysSerial",
    "fortinet")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(ifEntry,
 ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry",
    "ifIndex",
    "ifName")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

(AutonomousType,
 DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fnFortiGateMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101)
)
fnFortiGateMib.setRevisions(
        ("2016-06-17 00:00",
         "2015-04-23 00:00",
         "2015-03-16 00:00",
         "2015-01-10 00:00",
         "2014-12-04 00:00",
         "2014-06-04 00:00",
         "2014-02-13 00:00",
         "2013-08-12 00:00",
         "2013-07-26 00:00",
         "2013-04-12 00:00",
         "2013-04-06 00:00",
         "2012-11-29 00:00",
         "2012-07-10 00:00",
         "2012-05-16 00:00",
         "2012-02-06 00:00",
         "2011-09-12 00:00",
         "2011-01-10 00:00",
         "2009-11-03 00:00",
         "2009-10-01 00:00",
         "2009-07-07 00:00",
         "2008-11-03 00:00",
         "2008-09-02 00:00",
         "2008-08-19 00:00",
         "2008-06-16 00:00",
         "2008-04-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FgVdIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class FgOpMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nat", 1),
          ("transparent", 2))
    )



class FgHaMode(Integer32, TextualConvention):
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
        *(("activeActive", 2),
          ("activePassive", 3),
          ("standalone", 1))
    )



class FgHaState(Integer32, TextualConvention):
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
          ("master", 1),
          ("standalone", 3))
    )



class FgHaLBSchedule(Integer32, TextualConvention):
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
        *(("hub", 2),
          ("ipBased", 7),
          ("ipPortBased", 8),
          ("leastConnections", 3),
          ("none", 1),
          ("random", 6),
          ("roundRobin", 4),
          ("weightedRoundRobin", 5))
    )



class FgAdminPermLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              15,
              255)
        )
    )
    namedValues = NamedValues(
        *(("domainAdmin", 15),
          ("readAdmin", 0),
          ("superAdmin", 255),
          ("writeAdmin", 1))
    )



class FgFwUserAuthType(Integer32, TextualConvention):
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
        *(("ldap", 4),
          ("local", 1),
          ("radiusMultiple", 3),
          ("radiusSingle", 2))
    )



class FgSessProto(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6,
              8,
              12,
              17,
              22,
              41,
              46,
              47,
              50,
              51,
              89,
              103,
              108,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ah", 51),
          ("comp", 108),
          ("egp", 8),
          ("esp", 50),
          ("gre", 47),
          ("icmp", 1),
          ("idp", 22),
          ("igmp", 2),
          ("ip", 0),
          ("ipip", 4),
          ("ipv6", 41),
          ("ospf", 89),
          ("pim", 103),
          ("pup", 12),
          ("raw", 255),
          ("rsvp", 46),
          ("tcp", 6),
          ("udp", 17))
    )



class FgP2PProto(Integer32, TextualConvention):
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
        *(("bitTorrent", 0),
          ("eDonkey", 1),
          ("gnutella", 2),
          ("kaZaa", 3),
          ("skype", 4),
          ("winNY", 5))
    )



class FgScanAvDisposition(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 2),
          ("detected", 1))
    )



class FgWanOptProtocols(Integer32, TextualConvention):
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
        *(("cifs", 3),
          ("ftp", 4),
          ("http", 1),
          ("mapi", 2),
          ("tcp", 5))
    )



class FgWanOptHistPeriods(Integer32, TextualConvention):
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
        *(("last10Min", 1),
          ("lastDay", 3),
          ("lastHour", 2),
          ("lastMonth", 4))
    )



class FgHaStatsSyncStatusType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("synchronized", 1),
          ("unsynchronized", 0))
    )



class FgWcWlanSecurityType(Integer32, TextualConvention):
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("captivePortal", 2),
          ("open", 1),
          ("other", 0),
          ("wep128", 4),
          ("wep64", 3),
          ("wpa2OnlyEnterprise", 8),
          ("wpa2OnlyPersonal", 7),
          ("wpa2OnlyPersonalCaptivePortal", 12),
          ("wpaEnterprise", 10),
          ("wpaOnlyEnterprise", 6),
          ("wpaOnlyPersonal", 5),
          ("wpaOnlyPersonalCaptivePortal", 11),
          ("wpaPersonal", 9),
          ("wpaPersonalCaptivePortal", 13))
    )



class FgWcWlanAuthenticationType(Integer32, TextualConvention):
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
        *(("other", 0),
          ("psk", 1),
          ("radiusServer", 2),
          ("userGroup", 3))
    )



class FgWcWlanEncryptionType(Integer32, TextualConvention):
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
        *(("aes", 3),
          ("none", 1),
          ("other", 0),
          ("tkip", 2),
          ("tkipAes", 4))
    )



class FgWcWtpRadioId(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )



class FgWcWtpRadioType(Integer32, TextualConvention):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 1),
          ("dot11ac", 6),
          ("dot11acOnly", 12),
          ("dot11acnOnly", 11),
          ("dot11b", 2),
          ("dot11g", 3),
          ("dot11gOnly", 8),
          ("dot11n2GHzOnly", 9),
          ("dot11n2g", 5),
          ("dot11n5GHzOnly", 10),
          ("dot11n5g", 4),
          ("dot11ngOnly", 7),
          ("other", 0))
    )



class FgWcWtpChannelWidthType(Integer32, TextualConvention):
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
        *(("other", 0),
          ("width20MHz", 1),
          ("width40MHz", 2),
          ("width80MHz", 3))
    )



class FgWcWtpRadioBandType(Integer32, TextualConvention):
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
        *(("band2GHz", 1),
          ("band5GHz", 2),
          ("other", 0))
    )



class FgWcWtpRadioChannelNumber(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )



class FgWcWtpRadioMode(Integer32, TextualConvention):
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
        *(("ap", 3),
          ("disabled", 2),
          ("monitor", 4),
          ("notExist", 1),
          ("other", 0),
          ("sniffer", 5))
    )



class FgWcCountryString(OctetString, TextualConvention):
    status = "current"
    displayHint = "3a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



# MIB Managed Objects in the order of their OIDs

_FgModel_ObjectIdentity = ObjectIdentity
fgModel = _FgModel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1)
)
_FgtVM64_ObjectIdentity = ObjectIdentity
fgtVM64 = _FgtVM64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 30)
)
_FgtVM64VMX_ObjectIdentity = ObjectIdentity
fgtVM64VMX = _FgtVM64VMX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 31)
)
_FgtVM64SVM_ObjectIdentity = ObjectIdentity
fgtVM64SVM = _FgtVM64SVM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 32)
)
_FgtVM64XEN_ObjectIdentity = ObjectIdentity
fgtVM64XEN = _FgtVM64XEN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 40)
)
_FgtVM64AWS_ObjectIdentity = ObjectIdentity
fgtVM64AWS = _FgtVM64AWS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 45)
)
_FgtVM64AWSONDEMAND_ObjectIdentity = ObjectIdentity
fgtVM64AWSONDEMAND = _FgtVM64AWSONDEMAND_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 46)
)
_FgtVM64KVm_ObjectIdentity = ObjectIdentity
fgtVM64KVm = _FgtVM64KVm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 60)
)
_FgtVM64HV_ObjectIdentity = ObjectIdentity
fgtVM64HV = _FgtVM64HV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 70)
)
_Fgt30D_ObjectIdentity = ObjectIdentity
fgt30D = _Fgt30D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 304)
)
_Fgt30DPOE_ObjectIdentity = ObjectIdentity
fgt30DPOE = _Fgt30DPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 305)
)
_Fgt30E_ObjectIdentity = ObjectIdentity
fgt30E = _Fgt30E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 306)
)
_Fwf30D_ObjectIdentity = ObjectIdentity
fwf30D = _Fwf30D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 314)
)
_Fwf30DPOE_ObjectIdentity = ObjectIdentity
fwf30DPOE = _Fwf30DPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 315)
)
_Fwf30E_ObjectIdentity = ObjectIdentity
fwf30E = _Fwf30E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 316)
)
_Fgt50E_ObjectIdentity = ObjectIdentity
fgt50E = _Fgt50E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 505)
)
_Fwf50E_ObjectIdentity = ObjectIdentity
fwf50E = _Fwf50E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 506)
)
_Fgt51E_ObjectIdentity = ObjectIdentity
fgt51E = _Fgt51E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 515)
)
_Fwf51E_ObjectIdentity = ObjectIdentity
fwf51E = _Fwf51E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 516)
)
_Fgt60D_ObjectIdentity = ObjectIdentity
fgt60D = _Fgt60D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 624)
)
_Fgt60DPOE_ObjectIdentity = ObjectIdentity
fgt60DPOE = _Fgt60DPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 625)
)
_Fwf60D_ObjectIdentity = ObjectIdentity
fwf60D = _Fwf60D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 626)
)
_Fw60DP_ObjectIdentity = ObjectIdentity
fw60DP = _Fw60DP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 627)
)
_Fgtsoc3_ObjectIdentity = ObjectIdentity
fgtsoc3 = _Fgtsoc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 628)
)
_Fgt90D_ObjectIdentity = ObjectIdentity
fgt90D = _Fgt90D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 630)
)
_Fgt90DPOE_ObjectIdentity = ObjectIdentity
fgt90DPOE = _Fgt90DPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 631)
)
_Fwf90D_ObjectIdentity = ObjectIdentity
fwf90D = _Fwf90D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 632)
)
_Fwf90DPOE_ObjectIdentity = ObjectIdentity
fwf90DPOE = _Fwf90DPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 633)
)
_Fgt94DPOE_ObjectIdentity = ObjectIdentity
fgt94DPOE = _Fgt94DPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 634)
)
_Fgt98DPOE_ObjectIdentity = ObjectIdentity
fgt98DPOE = _Fgt98DPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 635)
)
_Fgt92D_ObjectIdentity = ObjectIdentity
fgt92D = _Fgt92D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 636)
)
_Fwf92D_ObjectIdentity = ObjectIdentity
fwf92D = _Fwf92D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 637)
)
_Fgr90D_ObjectIdentity = ObjectIdentity
fgr90D = _Fgr90D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 638)
)
_Fgr60D_ObjectIdentity = ObjectIdentity
fgr60D = _Fgr60D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 643)
)
_Fgt70D_ObjectIdentity = ObjectIdentity
fgt70D = _Fgt70D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 700)
)
_Fgt70DPOE_ObjectIdentity = ObjectIdentity
fgt70DPOE = _Fgt70DPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 701)
)
_Fgt80C_ObjectIdentity = ObjectIdentity
fgt80C = _Fgt80C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 800)
)
_Fgt80CM_ObjectIdentity = ObjectIdentity
fgt80CM = _Fgt80CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 801)
)
_Fgt80D_ObjectIdentity = ObjectIdentity
fgt80D = _Fgt80D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 803)
)
_Fwf80CM_ObjectIdentity = ObjectIdentity
fwf80CM = _Fwf80CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 810)
)
_Fwf81CM_ObjectIdentity = ObjectIdentity
fwf81CM = _Fwf81CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 811)
)
_Fg900D_ObjectIdentity = ObjectIdentity
fg900D = _Fg900D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 900)
)
_Fgt100D_ObjectIdentity = ObjectIdentity
fgt100D = _Fgt100D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 1004)
)
_Fgt140D_ObjectIdentity = ObjectIdentity
fgt140D = _Fgt140D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 1401)
)
_Fgt140P_ObjectIdentity = ObjectIdentity
fgt140P = _Fgt140P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 1402)
)
_Fgt200D_ObjectIdentity = ObjectIdentity
fgt200D = _Fgt200D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 2005)
)
_Fgt240D_ObjectIdentity = ObjectIdentity
fgt240D = _Fgt240D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 2006)
)
_Fgt200DP_ObjectIdentity = ObjectIdentity
fgt200DP = _Fgt200DP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 2007)
)
_Fgt240DP_ObjectIdentity = ObjectIdentity
fgt240DP = _Fgt240DP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 2008)
)
_Fgt280D_ObjectIdentity = ObjectIdentity
fgt280D = _Fgt280D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 2013)
)
_Fgt3HD_ObjectIdentity = ObjectIdentity
fgt3HD = _Fgt3HD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 3006)
)
_Fgt400D_ObjectIdentity = ObjectIdentity
fgt400D = _Fgt400D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 4004)
)
_Fgt500D_ObjectIdentity = ObjectIdentity
fgt500D = _Fgt500D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 5004)
)
_Fgt600C_ObjectIdentity = ObjectIdentity
fgt600C = _Fgt600C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 6003)
)
_Fgt600D_ObjectIdentity = ObjectIdentity
fgt600D = _Fgt600D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 6004)
)
_Fgt800C_ObjectIdentity = ObjectIdentity
fgt800C = _Fgt800C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 8003)
)
_Fgt800D_ObjectIdentity = ObjectIdentity
fgt800D = _Fgt800D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 8004)
)
_Fgt1000C_ObjectIdentity = ObjectIdentity
fgt1000C = _Fgt1000C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 10004)
)
_Fgt1000D_ObjectIdentity = ObjectIdentity
fgt1000D = _Fgt1000D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 10005)
)
_Fgt1200D_ObjectIdentity = ObjectIdentity
fgt1200D = _Fgt1200D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 12000)
)
_Fgt1500D_ObjectIdentity = ObjectIdentity
fgt1500D = _Fgt1500D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 15000)
)
_Fgt1500DT_ObjectIdentity = ObjectIdentity
fgt1500DT = _Fgt1500DT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 15001)
)
_Fgt3000D_ObjectIdentity = ObjectIdentity
fgt3000D = _Fgt3000D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 30000)
)
_Fgt3100D_ObjectIdentity = ObjectIdentity
fgt3100D = _Fgt3100D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 31000)
)
_Fgt3200D_ObjectIdentity = ObjectIdentity
fgt3200D = _Fgt3200D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 32000)
)
_Fgt3240C_ObjectIdentity = ObjectIdentity
fgt3240C = _Fgt3240C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 32401)
)
_Fgt3600C_ObjectIdentity = ObjectIdentity
fgt3600C = _Fgt3600C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 36004)
)
_Fgt3700D_ObjectIdentity = ObjectIdentity
fgt3700D = _Fgt3700D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 37000)
)
_Fgt3700DX_ObjectIdentity = ObjectIdentity
fgt3700DX = _Fgt3700DX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 37001)
)
_Fgt3810D_ObjectIdentity = ObjectIdentity
fgt3810D = _Fgt3810D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 38101)
)
_Fgt3815D_ObjectIdentity = ObjectIdentity
fgt3815D = _Fgt3815D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 38150)
)
_Fgt5001C_ObjectIdentity = ObjectIdentity
fgt5001C = _Fgt5001C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 50014)
)
_Fgt5001D_ObjectIdentity = ObjectIdentity
fgt5001D = _Fgt5001D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 50015)
)
_FosVM64_ObjectIdentity = ObjectIdentity
fosVM64 = _FosVM64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 90000)
)
_FosVM64KVM_ObjectIdentity = ObjectIdentity
fosVM64KVM = _FosVM64KVM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 90060)
)
_FgTraps_ObjectIdentity = ObjectIdentity
fgTraps = _FgTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2)
)
_FgTrapPrefix_ObjectIdentity = ObjectIdentity
fgTrapPrefix = _FgTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0)
)
_FgVirtualDomain_ObjectIdentity = ObjectIdentity
fgVirtualDomain = _FgVirtualDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3)
)
_FgVdInfo_ObjectIdentity = ObjectIdentity
fgVdInfo = _FgVdInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 1)
)
_FgVdNumber_Type = Integer32
_FgVdNumber_Object = MibScalar
fgVdNumber = _FgVdNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 1, 1),
    _FgVdNumber_Type()
)
fgVdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdNumber.setStatus("current")
_FgVdMaxVdoms_Type = Integer32
_FgVdMaxVdoms_Object = MibScalar
fgVdMaxVdoms = _FgVdMaxVdoms_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 1, 2),
    _FgVdMaxVdoms_Type()
)
fgVdMaxVdoms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdMaxVdoms.setStatus("current")
_FgVdEnabled_Type = FnBoolState
_FgVdEnabled_Object = MibScalar
fgVdEnabled = _FgVdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 1, 3),
    _FgVdEnabled_Type()
)
fgVdEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdEnabled.setStatus("current")
_FgVdTables_ObjectIdentity = ObjectIdentity
fgVdTables = _FgVdTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2)
)
_FgVdTable_Object = MibTable
fgVdTable = _FgVdTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 1)
)
if mibBuilder.loadTexts:
    fgVdTable.setStatus("current")
_FgVdEntry_Object = MibTableRow
fgVdEntry = _FgVdEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 1, 1)
)
fgVdEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
)
if mibBuilder.loadTexts:
    fgVdEntry.setStatus("current")
_FgVdEntIndex_Type = FgVdIndex
_FgVdEntIndex_Object = MibTableColumn
fgVdEntIndex = _FgVdEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 1, 1, 1),
    _FgVdEntIndex_Type()
)
fgVdEntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdEntIndex.setStatus("current")
_FgVdEntName_Type = DisplayString
_FgVdEntName_Object = MibTableColumn
fgVdEntName = _FgVdEntName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 1, 1, 2),
    _FgVdEntName_Type()
)
fgVdEntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdEntName.setStatus("current")
_FgVdEntOpMode_Type = FgOpMode
_FgVdEntOpMode_Object = MibTableColumn
fgVdEntOpMode = _FgVdEntOpMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 1, 1, 3),
    _FgVdEntOpMode_Type()
)
fgVdEntOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdEntOpMode.setStatus("current")
_FgVdEntHaState_Type = FgHaState
_FgVdEntHaState_Object = MibTableColumn
fgVdEntHaState = _FgVdEntHaState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 1, 1, 4),
    _FgVdEntHaState_Type()
)
fgVdEntHaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdEntHaState.setStatus("current")


class _FgVdEntCpuUsage_Type(Gauge32):
    """Custom type fgVdEntCpuUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgVdEntCpuUsage_Type.__name__ = "Gauge32"
_FgVdEntCpuUsage_Object = MibTableColumn
fgVdEntCpuUsage = _FgVdEntCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 1, 1, 5),
    _FgVdEntCpuUsage_Type()
)
fgVdEntCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdEntCpuUsage.setStatus("current")


class _FgVdEntMemUsage_Type(Gauge32):
    """Custom type fgVdEntMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgVdEntMemUsage_Type.__name__ = "Gauge32"
_FgVdEntMemUsage_Object = MibTableColumn
fgVdEntMemUsage = _FgVdEntMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 1, 1, 6),
    _FgVdEntMemUsage_Type()
)
fgVdEntMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdEntMemUsage.setStatus("current")
_FgVdEntSesCount_Type = Gauge32
_FgVdEntSesCount_Object = MibTableColumn
fgVdEntSesCount = _FgVdEntSesCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 1, 1, 7),
    _FgVdEntSesCount_Type()
)
fgVdEntSesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdEntSesCount.setStatus("current")
_FgVdEntSesRate_Type = Gauge32
_FgVdEntSesRate_Object = MibTableColumn
fgVdEntSesRate = _FgVdEntSesRate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 1, 1, 8),
    _FgVdEntSesRate_Type()
)
fgVdEntSesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdEntSesRate.setStatus("current")
if mibBuilder.loadTexts:
    fgVdEntSesRate.setUnits("Sessions Per Second")
_FgVdTpTable_Object = MibTable
fgVdTpTable = _FgVdTpTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 2)
)
if mibBuilder.loadTexts:
    fgVdTpTable.setStatus("current")
_FgVdTpEntry_Object = MibTableRow
fgVdTpEntry = _FgVdTpEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 2, 1)
)
fgVdTpEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
)
if mibBuilder.loadTexts:
    fgVdTpEntry.setStatus("current")
_FgVdTpMgmtAddrType_Type = InetAddressType
_FgVdTpMgmtAddrType_Object = MibTableColumn
fgVdTpMgmtAddrType = _FgVdTpMgmtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 2, 1, 1),
    _FgVdTpMgmtAddrType_Type()
)
fgVdTpMgmtAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdTpMgmtAddrType.setStatus("current")
_FgVdTpMgmtAddr_Type = InetAddress
_FgVdTpMgmtAddr_Object = MibTableColumn
fgVdTpMgmtAddr = _FgVdTpMgmtAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 2, 1, 2),
    _FgVdTpMgmtAddr_Type()
)
fgVdTpMgmtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdTpMgmtAddr.setStatus("current")
_FgVdTpMgmtMask_Type = InetAddressPrefixLength
_FgVdTpMgmtMask_Object = MibTableColumn
fgVdTpMgmtMask = _FgVdTpMgmtMask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 2, 1, 3),
    _FgVdTpMgmtMask_Type()
)
fgVdTpMgmtMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdTpMgmtMask.setStatus("current")
_FgSystem_ObjectIdentity = ObjectIdentity
fgSystem = _FgSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4)
)
_FgSystemInfo_ObjectIdentity = ObjectIdentity
fgSystemInfo = _FgSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1)
)


class _FgSysVersion_Type(DisplayString):
    """Custom type fgSysVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FgSysVersion_Type.__name__ = "DisplayString"
_FgSysVersion_Object = MibScalar
fgSysVersion = _FgSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 1),
    _FgSysVersion_Type()
)
fgSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysVersion.setStatus("current")
_FgSysMgmtVdom_Type = FgVdIndex
_FgSysMgmtVdom_Object = MibScalar
fgSysMgmtVdom = _FgSysMgmtVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 2),
    _FgSysMgmtVdom_Type()
)
fgSysMgmtVdom.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgSysMgmtVdom.setStatus("current")


class _FgSysCpuUsage_Type(Gauge32):
    """Custom type fgSysCpuUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgSysCpuUsage_Type.__name__ = "Gauge32"
_FgSysCpuUsage_Object = MibScalar
fgSysCpuUsage = _FgSysCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 3),
    _FgSysCpuUsage_Type()
)
fgSysCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysCpuUsage.setStatus("current")


class _FgSysMemUsage_Type(Gauge32):
    """Custom type fgSysMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgSysMemUsage_Type.__name__ = "Gauge32"
_FgSysMemUsage_Object = MibScalar
fgSysMemUsage = _FgSysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 4),
    _FgSysMemUsage_Type()
)
fgSysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysMemUsage.setStatus("current")
_FgSysMemCapacity_Type = Gauge32
_FgSysMemCapacity_Object = MibScalar
fgSysMemCapacity = _FgSysMemCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 5),
    _FgSysMemCapacity_Type()
)
fgSysMemCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysMemCapacity.setStatus("current")
_FgSysDiskUsage_Type = Gauge32
_FgSysDiskUsage_Object = MibScalar
fgSysDiskUsage = _FgSysDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 6),
    _FgSysDiskUsage_Type()
)
fgSysDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysDiskUsage.setStatus("current")
_FgSysDiskCapacity_Type = Gauge32
_FgSysDiskCapacity_Object = MibScalar
fgSysDiskCapacity = _FgSysDiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 7),
    _FgSysDiskCapacity_Type()
)
fgSysDiskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysDiskCapacity.setStatus("current")
_FgSysSesCount_Type = Gauge32
_FgSysSesCount_Object = MibScalar
fgSysSesCount = _FgSysSesCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 8),
    _FgSysSesCount_Type()
)
fgSysSesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysSesCount.setStatus("current")


class _FgSysLowMemUsage_Type(Gauge32):
    """Custom type fgSysLowMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgSysLowMemUsage_Type.__name__ = "Gauge32"
_FgSysLowMemUsage_Object = MibScalar
fgSysLowMemUsage = _FgSysLowMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 9),
    _FgSysLowMemUsage_Type()
)
fgSysLowMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysLowMemUsage.setStatus("current")
_FgSysLowMemCapacity_Type = Gauge32
_FgSysLowMemCapacity_Object = MibScalar
fgSysLowMemCapacity = _FgSysLowMemCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 10),
    _FgSysLowMemCapacity_Type()
)
fgSysLowMemCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysLowMemCapacity.setStatus("current")
_FgSysSesRate1_Type = Gauge32
_FgSysSesRate1_Object = MibScalar
fgSysSesRate1 = _FgSysSesRate1_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 11),
    _FgSysSesRate1_Type()
)
fgSysSesRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysSesRate1.setStatus("current")
if mibBuilder.loadTexts:
    fgSysSesRate1.setUnits("Sessions Per Second")
_FgSysSesRate10_Type = Gauge32
_FgSysSesRate10_Object = MibScalar
fgSysSesRate10 = _FgSysSesRate10_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 12),
    _FgSysSesRate10_Type()
)
fgSysSesRate10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysSesRate10.setStatus("current")
if mibBuilder.loadTexts:
    fgSysSesRate10.setUnits("Sessions Per Second")
_FgSysSesRate30_Type = Gauge32
_FgSysSesRate30_Object = MibScalar
fgSysSesRate30 = _FgSysSesRate30_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 13),
    _FgSysSesRate30_Type()
)
fgSysSesRate30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysSesRate30.setStatus("current")
if mibBuilder.loadTexts:
    fgSysSesRate30.setUnits("Sessions Per Second")
_FgSysSesRate60_Type = Gauge32
_FgSysSesRate60_Object = MibScalar
fgSysSesRate60 = _FgSysSesRate60_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 14),
    _FgSysSesRate60_Type()
)
fgSysSesRate60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysSesRate60.setStatus("current")
if mibBuilder.loadTexts:
    fgSysSesRate60.setUnits("Sessions Per Second")
_FgSysSes6Count_Type = Gauge32
_FgSysSes6Count_Object = MibScalar
fgSysSes6Count = _FgSysSes6Count_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 15),
    _FgSysSes6Count_Type()
)
fgSysSes6Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysSes6Count.setStatus("current")
_FgSysSes6Rate1_Type = Gauge32
_FgSysSes6Rate1_Object = MibScalar
fgSysSes6Rate1 = _FgSysSes6Rate1_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 16),
    _FgSysSes6Rate1_Type()
)
fgSysSes6Rate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysSes6Rate1.setStatus("current")
if mibBuilder.loadTexts:
    fgSysSes6Rate1.setUnits("Sessions Per Second")
_FgSysSes6Rate10_Type = Gauge32
_FgSysSes6Rate10_Object = MibScalar
fgSysSes6Rate10 = _FgSysSes6Rate10_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 17),
    _FgSysSes6Rate10_Type()
)
fgSysSes6Rate10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysSes6Rate10.setStatus("current")
if mibBuilder.loadTexts:
    fgSysSes6Rate10.setUnits("Sessions Per Second")
_FgSysSes6Rate30_Type = Gauge32
_FgSysSes6Rate30_Object = MibScalar
fgSysSes6Rate30 = _FgSysSes6Rate30_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 18),
    _FgSysSes6Rate30_Type()
)
fgSysSes6Rate30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysSes6Rate30.setStatus("current")
if mibBuilder.loadTexts:
    fgSysSes6Rate30.setUnits("Sessions Per Second")
_FgSysSes6Rate60_Type = Gauge32
_FgSysSes6Rate60_Object = MibScalar
fgSysSes6Rate60 = _FgSysSes6Rate60_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 19),
    _FgSysSes6Rate60_Type()
)
fgSysSes6Rate60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysSes6Rate60.setStatus("current")
if mibBuilder.loadTexts:
    fgSysSes6Rate60.setUnits("Sessions Per Second")
_FgSysUpTime_Type = Counter64
_FgSysUpTime_Object = MibScalar
fgSysUpTime = _FgSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 20),
    _FgSysUpTime_Type()
)
fgSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysUpTime.setStatus("current")
if mibBuilder.loadTexts:
    fgSysUpTime.setUnits("hundredths of a second")
_FgSoftware_ObjectIdentity = ObjectIdentity
fgSoftware = _FgSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 2)
)


class _FgSysVersionAv_Type(DisplayString):
    """Custom type fgSysVersionAv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FgSysVersionAv_Type.__name__ = "DisplayString"
_FgSysVersionAv_Object = MibScalar
fgSysVersionAv = _FgSysVersionAv_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 2, 1),
    _FgSysVersionAv_Type()
)
fgSysVersionAv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysVersionAv.setStatus("current")


class _FgSysVersionIps_Type(DisplayString):
    """Custom type fgSysVersionIps based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FgSysVersionIps_Type.__name__ = "DisplayString"
_FgSysVersionIps_Object = MibScalar
fgSysVersionIps = _FgSysVersionIps_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 2, 2),
    _FgSysVersionIps_Type()
)
fgSysVersionIps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysVersionIps.setStatus("current")
_FgHwSensors_ObjectIdentity = ObjectIdentity
fgHwSensors = _FgHwSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 3)
)
_FgHwSensorCount_Type = Integer32
_FgHwSensorCount_Object = MibScalar
fgHwSensorCount = _FgHwSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 3, 1),
    _FgHwSensorCount_Type()
)
fgHwSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHwSensorCount.setStatus("current")
_FgHwSensorTable_Object = MibTable
fgHwSensorTable = _FgHwSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 3, 2)
)
if mibBuilder.loadTexts:
    fgHwSensorTable.setStatus("current")
_FgHwSensorEntry_Object = MibTableRow
fgHwSensorEntry = _FgHwSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 3, 2, 1)
)
fgHwSensorEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgHwSensorEntIndex"),
)
if mibBuilder.loadTexts:
    fgHwSensorEntry.setStatus("current")
_FgHwSensorEntIndex_Type = FnIndex
_FgHwSensorEntIndex_Object = MibTableColumn
fgHwSensorEntIndex = _FgHwSensorEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 3, 2, 1, 1),
    _FgHwSensorEntIndex_Type()
)
fgHwSensorEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgHwSensorEntIndex.setStatus("current")
_FgHwSensorEntName_Type = DisplayString
_FgHwSensorEntName_Object = MibTableColumn
fgHwSensorEntName = _FgHwSensorEntName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 3, 2, 1, 2),
    _FgHwSensorEntName_Type()
)
fgHwSensorEntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHwSensorEntName.setStatus("current")
_FgHwSensorEntValue_Type = DisplayString
_FgHwSensorEntValue_Object = MibTableColumn
fgHwSensorEntValue = _FgHwSensorEntValue_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 3, 2, 1, 3),
    _FgHwSensorEntValue_Type()
)
fgHwSensorEntValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHwSensorEntValue.setStatus("current")


class _FgHwSensorEntAlarmStatus_Type(Integer32):
    """Custom type fgHwSensorEntAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_FgHwSensorEntAlarmStatus_Type.__name__ = "Integer32"
_FgHwSensorEntAlarmStatus_Object = MibTableColumn
fgHwSensorEntAlarmStatus = _FgHwSensorEntAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 3, 2, 1, 4),
    _FgHwSensorEntAlarmStatus_Type()
)
fgHwSensorEntAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHwSensorEntAlarmStatus.setStatus("current")
_FgProcessors_ObjectIdentity = ObjectIdentity
fgProcessors = _FgProcessors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4)
)
_FgProcessorCount_Type = Integer32
_FgProcessorCount_Object = MibScalar
fgProcessorCount = _FgProcessorCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 1),
    _FgProcessorCount_Type()
)
fgProcessorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcessorCount.setStatus("current")
_FgProcessorTable_Object = MibTable
fgProcessorTable = _FgProcessorTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2)
)
if mibBuilder.loadTexts:
    fgProcessorTable.setStatus("current")
_FgProcessorEntry_Object = MibTableRow
fgProcessorEntry = _FgProcessorEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2, 1)
)
fgProcessorEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgProcessorEntIndex"),
)
if mibBuilder.loadTexts:
    fgProcessorEntry.setStatus("current")
_FgProcessorEntIndex_Type = FnIndex
_FgProcessorEntIndex_Object = MibTableColumn
fgProcessorEntIndex = _FgProcessorEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2, 1, 1),
    _FgProcessorEntIndex_Type()
)
fgProcessorEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgProcessorEntIndex.setStatus("current")


class _FgProcessorUsage_Type(Gauge32):
    """Custom type fgProcessorUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgProcessorUsage_Type.__name__ = "Gauge32"
_FgProcessorUsage_Object = MibTableColumn
fgProcessorUsage = _FgProcessorUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2, 1, 2),
    _FgProcessorUsage_Type()
)
fgProcessorUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcessorUsage.setStatus("current")
if mibBuilder.loadTexts:
    fgProcessorUsage.setUnits("%")


class _FgProcessorUsage5sec_Type(Gauge32):
    """Custom type fgProcessorUsage5sec based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgProcessorUsage5sec_Type.__name__ = "Gauge32"
_FgProcessorUsage5sec_Object = MibTableColumn
fgProcessorUsage5sec = _FgProcessorUsage5sec_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2, 1, 3),
    _FgProcessorUsage5sec_Type()
)
fgProcessorUsage5sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcessorUsage5sec.setStatus("current")
if mibBuilder.loadTexts:
    fgProcessorUsage5sec.setUnits("%")
_FgProcessorType_Type = AutonomousType
_FgProcessorType_Object = MibTableColumn
fgProcessorType = _FgProcessorType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2, 1, 4),
    _FgProcessorType_Type()
)
fgProcessorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcessorType.setStatus("current")
_FgProcessorContainedIn_Type = FnIndex
_FgProcessorContainedIn_Object = MibTableColumn
fgProcessorContainedIn = _FgProcessorContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2, 1, 5),
    _FgProcessorContainedIn_Type()
)
fgProcessorContainedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcessorContainedIn.setStatus("current")
_FgProcessorPktRxCount_Type = Counter64
_FgProcessorPktRxCount_Object = MibTableColumn
fgProcessorPktRxCount = _FgProcessorPktRxCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2, 1, 6),
    _FgProcessorPktRxCount_Type()
)
fgProcessorPktRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcessorPktRxCount.setStatus("current")
_FgProcessorPktTxCount_Type = Counter64
_FgProcessorPktTxCount_Object = MibTableColumn
fgProcessorPktTxCount = _FgProcessorPktTxCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2, 1, 7),
    _FgProcessorPktTxCount_Type()
)
fgProcessorPktTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcessorPktTxCount.setStatus("current")
_FgProcessorPktDroppedCount_Type = Counter64
_FgProcessorPktDroppedCount_Object = MibTableColumn
fgProcessorPktDroppedCount = _FgProcessorPktDroppedCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2, 1, 8),
    _FgProcessorPktDroppedCount_Type()
)
fgProcessorPktDroppedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcessorPktDroppedCount.setStatus("current")


class _FgProcessorUserUsage_Type(Gauge32):
    """Custom type fgProcessorUserUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgProcessorUserUsage_Type.__name__ = "Gauge32"
_FgProcessorUserUsage_Object = MibTableColumn
fgProcessorUserUsage = _FgProcessorUserUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2, 1, 9),
    _FgProcessorUserUsage_Type()
)
fgProcessorUserUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcessorUserUsage.setStatus("current")
if mibBuilder.loadTexts:
    fgProcessorUserUsage.setUnits("%")


class _FgProcessorSysUsage_Type(Gauge32):
    """Custom type fgProcessorSysUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgProcessorSysUsage_Type.__name__ = "Gauge32"
_FgProcessorSysUsage_Object = MibTableColumn
fgProcessorSysUsage = _FgProcessorSysUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2, 1, 10),
    _FgProcessorSysUsage_Type()
)
fgProcessorSysUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcessorSysUsage.setStatus("current")
if mibBuilder.loadTexts:
    fgProcessorSysUsage.setUnits("%")
_FgProcessorTypes_ObjectIdentity = ObjectIdentity
fgProcessorTypes = _FgProcessorTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 3)
)
_FgProcessorOther_ObjectIdentity = ObjectIdentity
fgProcessorOther = _FgProcessorOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 3, 1)
)
if mibBuilder.loadTexts:
    fgProcessorOther.setStatus("current")
_FgProcessorIntel_ObjectIdentity = ObjectIdentity
fgProcessorIntel = _FgProcessorIntel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 3, 2)
)
if mibBuilder.loadTexts:
    fgProcessorIntel.setStatus("current")
_FgProcessorAMD_ObjectIdentity = ObjectIdentity
fgProcessorAMD = _FgProcessorAMD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 3, 3)
)
if mibBuilder.loadTexts:
    fgProcessorAMD.setStatus("current")
_FgProcessorXlr_ObjectIdentity = ObjectIdentity
fgProcessorXlr = _FgProcessorXlr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 3, 4)
)
if mibBuilder.loadTexts:
    fgProcessorXlr.setStatus("current")
_FgProcessorFnSoc_ObjectIdentity = ObjectIdentity
fgProcessorFnSoc = _FgProcessorFnSoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 3, 5)
)
if mibBuilder.loadTexts:
    fgProcessorFnSoc.setStatus("current")
_FgProcessorFnNP2_ObjectIdentity = ObjectIdentity
fgProcessorFnNP2 = _FgProcessorFnNP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 3, 6)
)
if mibBuilder.loadTexts:
    fgProcessorFnNP2.setStatus("current")
_FgProcessorFnNP4_ObjectIdentity = ObjectIdentity
fgProcessorFnNP4 = _FgProcessorFnNP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 3, 7)
)
if mibBuilder.loadTexts:
    fgProcessorFnNP4.setStatus("current")
_FgProcessorFnNP6_ObjectIdentity = ObjectIdentity
fgProcessorFnNP6 = _FgProcessorFnNP6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 3, 8)
)
if mibBuilder.loadTexts:
    fgProcessorFnNP6.setStatus("current")
_FgProcessorModules_ObjectIdentity = ObjectIdentity
fgProcessorModules = _FgProcessorModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5)
)
_FgProcessorModuleTypes_ObjectIdentity = ObjectIdentity
fgProcessorModuleTypes = _FgProcessorModuleTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 1)
)
_FgProcModOther_ObjectIdentity = ObjectIdentity
fgProcModOther = _FgProcModOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 1, 1)
)
if mibBuilder.loadTexts:
    fgProcModOther.setStatus("current")
_FgProcModIntegrated_ObjectIdentity = ObjectIdentity
fgProcModIntegrated = _FgProcModIntegrated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 1, 2)
)
if mibBuilder.loadTexts:
    fgProcModIntegrated.setStatus("current")
_FgProcModFnXE2_ObjectIdentity = ObjectIdentity
fgProcModFnXE2 = _FgProcModFnXE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 1, 3)
)
if mibBuilder.loadTexts:
    fgProcModFnXE2.setStatus("current")
_FgProcModFnCE4_ObjectIdentity = ObjectIdentity
fgProcModFnCE4 = _FgProcModFnCE4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 1, 4)
)
if mibBuilder.loadTexts:
    fgProcModFnCE4.setStatus("current")
_FgProcModFnFE8_ObjectIdentity = ObjectIdentity
fgProcModFnFE8 = _FgProcModFnFE8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 1, 5)
)
if mibBuilder.loadTexts:
    fgProcModFnFE8.setStatus("current")
_FgProcModFnXG2_ObjectIdentity = ObjectIdentity
fgProcModFnXG2 = _FgProcModFnXG2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 1, 6)
)
if mibBuilder.loadTexts:
    fgProcModFnXG2.setStatus("current")
_FgProcModIntegratedNPU_ObjectIdentity = ObjectIdentity
fgProcModIntegratedNPU = _FgProcModIntegratedNPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 1, 7)
)
if mibBuilder.loadTexts:
    fgProcModIntegratedNPU.setStatus("current")
_FgProcModFnXD2_ObjectIdentity = ObjectIdentity
fgProcModFnXD2 = _FgProcModFnXD2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 1, 8)
)
if mibBuilder.loadTexts:
    fgProcModFnXD2.setStatus("current")
_FgProcModFnF20_ObjectIdentity = ObjectIdentity
fgProcModFnF20 = _FgProcModFnF20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 1, 9)
)
if mibBuilder.loadTexts:
    fgProcModFnF20.setStatus("current")
_FgProcModFnC20_ObjectIdentity = ObjectIdentity
fgProcModFnC20 = _FgProcModFnC20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 1, 10)
)
if mibBuilder.loadTexts:
    fgProcModFnC20.setStatus("current")
_FgProcModFnXD4_ObjectIdentity = ObjectIdentity
fgProcModFnXD4 = _FgProcModFnXD4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 1, 11)
)
if mibBuilder.loadTexts:
    fgProcModFnXD4.setStatus("current")
_FgProcModFnFB4_ObjectIdentity = ObjectIdentity
fgProcModFnFB4 = _FgProcModFnFB4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 1, 12)
)
if mibBuilder.loadTexts:
    fgProcModFnFB4.setStatus("current")
_FgProcModFnFB8_ObjectIdentity = ObjectIdentity
fgProcModFnFB8 = _FgProcModFnFB8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 1, 13)
)
if mibBuilder.loadTexts:
    fgProcModFnFB8.setStatus("current")
_FgProcModFnXB2_ObjectIdentity = ObjectIdentity
fgProcModFnXB2 = _FgProcModFnXB2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 1, 14)
)
if mibBuilder.loadTexts:
    fgProcModFnXB2.setStatus("current")
_FgProcessorModuleCount_Type = Integer32
_FgProcessorModuleCount_Object = MibScalar
fgProcessorModuleCount = _FgProcessorModuleCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 2),
    _FgProcessorModuleCount_Type()
)
fgProcessorModuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcessorModuleCount.setStatus("current")
_FgProcessorModuleTable_Object = MibTable
fgProcessorModuleTable = _FgProcessorModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 3)
)
if mibBuilder.loadTexts:
    fgProcessorModuleTable.setStatus("current")
_FgProcessorModuleEntry_Object = MibTableRow
fgProcessorModuleEntry = _FgProcessorModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 3, 1)
)
fgProcessorModuleEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgProcModIndex"),
)
if mibBuilder.loadTexts:
    fgProcessorModuleEntry.setStatus("current")
_FgProcModIndex_Type = FnIndex
_FgProcModIndex_Object = MibTableColumn
fgProcModIndex = _FgProcModIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 3, 1, 1),
    _FgProcModIndex_Type()
)
fgProcModIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgProcModIndex.setStatus("current")
_FgProcModType_Type = AutonomousType
_FgProcModType_Object = MibTableColumn
fgProcModType = _FgProcModType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 3, 1, 2),
    _FgProcModType_Type()
)
fgProcModType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcModType.setStatus("current")


class _FgProcModName_Type(DisplayString):
    """Custom type fgProcModName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgProcModName_Type.__name__ = "DisplayString"
_FgProcModName_Object = MibTableColumn
fgProcModName = _FgProcModName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 3, 1, 3),
    _FgProcModName_Type()
)
fgProcModName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcModName.setStatus("current")


class _FgProcModDescr_Type(DisplayString):
    """Custom type fgProcModDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FgProcModDescr_Type.__name__ = "DisplayString"
_FgProcModDescr_Object = MibTableColumn
fgProcModDescr = _FgProcModDescr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 3, 1, 4),
    _FgProcModDescr_Type()
)
fgProcModDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcModDescr.setStatus("current")
_FgProcModProcessorCount_Type = Integer32
_FgProcModProcessorCount_Object = MibTableColumn
fgProcModProcessorCount = _FgProcModProcessorCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 3, 1, 5),
    _FgProcModProcessorCount_Type()
)
fgProcModProcessorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcModProcessorCount.setStatus("current")
_FgProcModMemCapacity_Type = Gauge32
_FgProcModMemCapacity_Object = MibTableColumn
fgProcModMemCapacity = _FgProcModMemCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 3, 1, 6),
    _FgProcModMemCapacity_Type()
)
fgProcModMemCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcModMemCapacity.setStatus("current")


class _FgProcModMemUsage_Type(Gauge32):
    """Custom type fgProcModMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgProcModMemUsage_Type.__name__ = "Gauge32"
_FgProcModMemUsage_Object = MibTableColumn
fgProcModMemUsage = _FgProcModMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 3, 1, 7),
    _FgProcModMemUsage_Type()
)
fgProcModMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcModMemUsage.setStatus("current")
_FgProcModSessionCount_Type = Gauge32
_FgProcModSessionCount_Object = MibTableColumn
fgProcModSessionCount = _FgProcModSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 3, 1, 8),
    _FgProcModSessionCount_Type()
)
fgProcModSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcModSessionCount.setStatus("current")
_FgProcModSACount_Type = Gauge32
_FgProcModSACount_Object = MibTableColumn
fgProcModSACount = _FgProcModSACount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 3, 1, 9),
    _FgProcModSACount_Type()
)
fgProcModSACount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcModSACount.setStatus("current")
_FgSystemInfoAdvanced_ObjectIdentity = ObjectIdentity
fgSystemInfoAdvanced = _FgSystemInfoAdvanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6)
)
_FgSysInfoAdvMem_ObjectIdentity = ObjectIdentity
fgSysInfoAdvMem = _FgSysInfoAdvMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 1)
)
_FgSIAdvMemPageCache_Type = Gauge32
_FgSIAdvMemPageCache_Object = MibScalar
fgSIAdvMemPageCache = _FgSIAdvMemPageCache_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 1, 1),
    _FgSIAdvMemPageCache_Type()
)
fgSIAdvMemPageCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvMemPageCache.setStatus("current")
if mibBuilder.loadTexts:
    fgSIAdvMemPageCache.setUnits("KB")
_FgSIAdvMemCacheActive_Type = Gauge32
_FgSIAdvMemCacheActive_Object = MibScalar
fgSIAdvMemCacheActive = _FgSIAdvMemCacheActive_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 1, 2),
    _FgSIAdvMemCacheActive_Type()
)
fgSIAdvMemCacheActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvMemCacheActive.setStatus("current")
if mibBuilder.loadTexts:
    fgSIAdvMemCacheActive.setUnits("KB")
_FgSIAdvMemCacheInactive_Type = Gauge32
_FgSIAdvMemCacheInactive_Object = MibScalar
fgSIAdvMemCacheInactive = _FgSIAdvMemCacheInactive_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 1, 3),
    _FgSIAdvMemCacheInactive_Type()
)
fgSIAdvMemCacheInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvMemCacheInactive.setStatus("current")
if mibBuilder.loadTexts:
    fgSIAdvMemCacheInactive.setUnits("KB")
_FgSIAdvMemBuffer_Type = Gauge32
_FgSIAdvMemBuffer_Object = MibScalar
fgSIAdvMemBuffer = _FgSIAdvMemBuffer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 1, 4),
    _FgSIAdvMemBuffer_Type()
)
fgSIAdvMemBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvMemBuffer.setStatus("current")
if mibBuilder.loadTexts:
    fgSIAdvMemBuffer.setUnits("KB")
_FgSIAdvMemEnterKerConsThrsh_Type = Gauge32
_FgSIAdvMemEnterKerConsThrsh_Object = MibScalar
fgSIAdvMemEnterKerConsThrsh = _FgSIAdvMemEnterKerConsThrsh_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 1, 5),
    _FgSIAdvMemEnterKerConsThrsh_Type()
)
fgSIAdvMemEnterKerConsThrsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvMemEnterKerConsThrsh.setStatus("current")
if mibBuilder.loadTexts:
    fgSIAdvMemEnterKerConsThrsh.setUnits("KB")
_FgSIAdvMemLeaveKerConsThrsh_Type = Gauge32
_FgSIAdvMemLeaveKerConsThrsh_Object = MibScalar
fgSIAdvMemLeaveKerConsThrsh = _FgSIAdvMemLeaveKerConsThrsh_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 1, 6),
    _FgSIAdvMemLeaveKerConsThrsh_Type()
)
fgSIAdvMemLeaveKerConsThrsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvMemLeaveKerConsThrsh.setStatus("current")
if mibBuilder.loadTexts:
    fgSIAdvMemLeaveKerConsThrsh.setUnits("KB")
_FgSIAdvMemEnterProxyConsThrsh_Type = Gauge32
_FgSIAdvMemEnterProxyConsThrsh_Object = MibScalar
fgSIAdvMemEnterProxyConsThrsh = _FgSIAdvMemEnterProxyConsThrsh_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 1, 7),
    _FgSIAdvMemEnterProxyConsThrsh_Type()
)
fgSIAdvMemEnterProxyConsThrsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvMemEnterProxyConsThrsh.setStatus("current")
if mibBuilder.loadTexts:
    fgSIAdvMemEnterProxyConsThrsh.setUnits("KB")
_FgSIAdvMemLeaveProxyConsThrsh_Type = Gauge32
_FgSIAdvMemLeaveProxyConsThrsh_Object = MibScalar
fgSIAdvMemLeaveProxyConsThrsh = _FgSIAdvMemLeaveProxyConsThrsh_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 1, 8),
    _FgSIAdvMemLeaveProxyConsThrsh_Type()
)
fgSIAdvMemLeaveProxyConsThrsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvMemLeaveProxyConsThrsh.setStatus("current")
if mibBuilder.loadTexts:
    fgSIAdvMemLeaveProxyConsThrsh.setUnits("KB")
_FgSysInfoAdvSessions_ObjectIdentity = ObjectIdentity
fgSysInfoAdvSessions = _FgSysInfoAdvSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 2)
)
_FgSIAdvSesEphemeralCount_Type = Gauge32
_FgSIAdvSesEphemeralCount_Object = MibScalar
fgSIAdvSesEphemeralCount = _FgSIAdvSesEphemeralCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 2, 1),
    _FgSIAdvSesEphemeralCount_Type()
)
fgSIAdvSesEphemeralCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvSesEphemeralCount.setStatus("current")
_FgSIAdvSesEphemeralLimit_Type = Gauge32
_FgSIAdvSesEphemeralLimit_Object = MibScalar
fgSIAdvSesEphemeralLimit = _FgSIAdvSesEphemeralLimit_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 2, 2),
    _FgSIAdvSesEphemeralLimit_Type()
)
fgSIAdvSesEphemeralLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvSesEphemeralLimit.setStatus("current")
_FgSIAdvSesClashCount_Type = Gauge32
_FgSIAdvSesClashCount_Object = MibScalar
fgSIAdvSesClashCount = _FgSIAdvSesClashCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 2, 3),
    _FgSIAdvSesClashCount_Type()
)
fgSIAdvSesClashCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvSesClashCount.setStatus("current")
_FgSIAdvSesExpCount_Type = Gauge32
_FgSIAdvSesExpCount_Object = MibScalar
fgSIAdvSesExpCount = _FgSIAdvSesExpCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 2, 4),
    _FgSIAdvSesExpCount_Type()
)
fgSIAdvSesExpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvSesExpCount.setStatus("current")
_FgSIAdvSesSyncQFCount_Type = Gauge32
_FgSIAdvSesSyncQFCount_Object = MibScalar
fgSIAdvSesSyncQFCount = _FgSIAdvSesSyncQFCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 2, 5),
    _FgSIAdvSesSyncQFCount_Type()
)
fgSIAdvSesSyncQFCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvSesSyncQFCount.setStatus("current")
_FgSIAdvSesAcceptQFCount_Type = Gauge32
_FgSIAdvSesAcceptQFCount_Object = MibScalar
fgSIAdvSesAcceptQFCount = _FgSIAdvSesAcceptQFCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 2, 6),
    _FgSIAdvSesAcceptQFCount_Type()
)
fgSIAdvSesAcceptQFCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvSesAcceptQFCount.setStatus("current")
_FgSIAdvSesNoListenerCount_Type = Gauge32
_FgSIAdvSesNoListenerCount_Object = MibScalar
fgSIAdvSesNoListenerCount = _FgSIAdvSesNoListenerCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 2, 7),
    _FgSIAdvSesNoListenerCount_Type()
)
fgSIAdvSesNoListenerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvSesNoListenerCount.setStatus("current")
_FgUsbports_ObjectIdentity = ObjectIdentity
fgUsbports = _FgUsbports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7)
)
_FgUsbportCount_Type = Integer32
_FgUsbportCount_Object = MibScalar
fgUsbportCount = _FgUsbportCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 1),
    _FgUsbportCount_Type()
)
fgUsbportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbportCount.setStatus("current")
_FgUsbportTable_Object = MibTable
fgUsbportTable = _FgUsbportTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 2)
)
if mibBuilder.loadTexts:
    fgUsbportTable.setStatus("current")
_FgUsbportEntry_Object = MibTableRow
fgUsbportEntry = _FgUsbportEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 2, 1)
)
fgUsbportEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgUsbportEntIndex"),
)
if mibBuilder.loadTexts:
    fgUsbportEntry.setStatus("current")
_FgUsbportEntIndex_Type = FnIndex
_FgUsbportEntIndex_Object = MibTableColumn
fgUsbportEntIndex = _FgUsbportEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 2, 1, 1),
    _FgUsbportEntIndex_Type()
)
fgUsbportEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgUsbportEntIndex.setStatus("current")


class _FgUsbportPlugged_Type(Integer32):
    """Custom type fgUsbportPlugged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("plugged", 1),
          ("unplugged", 0))
    )


_FgUsbportPlugged_Type.__name__ = "Integer32"
_FgUsbportPlugged_Object = MibTableColumn
fgUsbportPlugged = _FgUsbportPlugged_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 2, 1, 2),
    _FgUsbportPlugged_Type()
)
fgUsbportPlugged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbportPlugged.setStatus("current")
_FgUsbportVersion_Type = DisplayString
_FgUsbportVersion_Object = MibTableColumn
fgUsbportVersion = _FgUsbportVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 2, 1, 3),
    _FgUsbportVersion_Type()
)
fgUsbportVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbportVersion.setStatus("current")


class _FgUsbportClass_Type(Integer32):
    """Custom type fgUsbportClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              13,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("appSpec", 254),
          ("audio", 1),
          ("cdcData", 10),
          ("chipSmartCard", 11),
          ("comm", 2),
          ("contentSecurity", 13),
          ("hid", 3),
          ("hub", 9),
          ("ifc", 0),
          ("image", 6),
          ("physical", 5),
          ("printer", 7),
          ("storage", 8),
          ("vendorSpec", 255))
    )


_FgUsbportClass_Type.__name__ = "Integer32"
_FgUsbportClass_Object = MibTableColumn
fgUsbportClass = _FgUsbportClass_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 2, 1, 4),
    _FgUsbportClass_Type()
)
fgUsbportClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbportClass.setStatus("current")
_FgUsbportVendId_Type = OctetString
_FgUsbportVendId_Object = MibTableColumn
fgUsbportVendId = _FgUsbportVendId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 2, 1, 5),
    _FgUsbportVendId_Type()
)
fgUsbportVendId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbportVendId.setStatus("current")
_FgUsbportProdId_Type = OctetString
_FgUsbportProdId_Object = MibTableColumn
fgUsbportProdId = _FgUsbportProdId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 2, 1, 6),
    _FgUsbportProdId_Type()
)
fgUsbportProdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbportProdId.setStatus("current")
_FgUsbportRevision_Type = DisplayString
_FgUsbportRevision_Object = MibTableColumn
fgUsbportRevision = _FgUsbportRevision_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 2, 1, 7),
    _FgUsbportRevision_Type()
)
fgUsbportRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbportRevision.setStatus("current")
_FgUsbportManufacturer_Type = DisplayString
_FgUsbportManufacturer_Object = MibTableColumn
fgUsbportManufacturer = _FgUsbportManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 2, 1, 8),
    _FgUsbportManufacturer_Type()
)
fgUsbportManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbportManufacturer.setStatus("current")
_FgUsbportProduct_Type = DisplayString
_FgUsbportProduct_Object = MibTableColumn
fgUsbportProduct = _FgUsbportProduct_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 2, 1, 9),
    _FgUsbportProduct_Type()
)
fgUsbportProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbportProduct.setStatus("current")
_FgUsbportSerial_Type = DisplayString
_FgUsbportSerial_Object = MibTableColumn
fgUsbportSerial = _FgUsbportSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 2, 1, 10),
    _FgUsbportSerial_Type()
)
fgUsbportSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbportSerial.setStatus("current")
_FgLinkMonitor_ObjectIdentity = ObjectIdentity
fgLinkMonitor = _FgLinkMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8)
)
_FgLinkMonitorNumber_Type = Integer32
_FgLinkMonitorNumber_Object = MibScalar
fgLinkMonitorNumber = _FgLinkMonitorNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 1),
    _FgLinkMonitorNumber_Type()
)
fgLinkMonitorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLinkMonitorNumber.setStatus("current")
_FgLinkMonitorTable_Object = MibTable
fgLinkMonitorTable = _FgLinkMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2)
)
if mibBuilder.loadTexts:
    fgLinkMonitorTable.setStatus("current")
_FgLinkMonitorEntry_Object = MibTableRow
fgLinkMonitorEntry = _FgLinkMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1)
)
fgLinkMonitorEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgLinkMonitorID"),
)
if mibBuilder.loadTexts:
    fgLinkMonitorEntry.setStatus("current")
_FgLinkMonitorID_Type = FnIndex
_FgLinkMonitorID_Object = MibTableColumn
fgLinkMonitorID = _FgLinkMonitorID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1, 1),
    _FgLinkMonitorID_Type()
)
fgLinkMonitorID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgLinkMonitorID.setStatus("current")
_FgLinkMonitorName_Type = DisplayString
_FgLinkMonitorName_Object = MibTableColumn
fgLinkMonitorName = _FgLinkMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1, 2),
    _FgLinkMonitorName_Type()
)
fgLinkMonitorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLinkMonitorName.setStatus("current")


class _FgLinkMonitorState_Type(Integer32):
    """Custom type fgLinkMonitorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alive", 0),
          ("dead", 1))
    )


_FgLinkMonitorState_Type.__name__ = "Integer32"
_FgLinkMonitorState_Object = MibTableColumn
fgLinkMonitorState = _FgLinkMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1, 3),
    _FgLinkMonitorState_Type()
)
fgLinkMonitorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLinkMonitorState.setStatus("current")
_FgLinkMonitorLatency_Type = DisplayString
_FgLinkMonitorLatency_Object = MibTableColumn
fgLinkMonitorLatency = _FgLinkMonitorLatency_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1, 4),
    _FgLinkMonitorLatency_Type()
)
fgLinkMonitorLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLinkMonitorLatency.setStatus("current")
_FgLinkMonitorJitter_Type = DisplayString
_FgLinkMonitorJitter_Object = MibTableColumn
fgLinkMonitorJitter = _FgLinkMonitorJitter_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1, 5),
    _FgLinkMonitorJitter_Type()
)
fgLinkMonitorJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLinkMonitorJitter.setStatus("current")
_FgLinkMonitorPacketSend_Type = Counter64
_FgLinkMonitorPacketSend_Object = MibTableColumn
fgLinkMonitorPacketSend = _FgLinkMonitorPacketSend_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1, 6),
    _FgLinkMonitorPacketSend_Type()
)
fgLinkMonitorPacketSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLinkMonitorPacketSend.setStatus("current")
_FgLinkMonitorPacketRecv_Type = Counter64
_FgLinkMonitorPacketRecv_Object = MibTableColumn
fgLinkMonitorPacketRecv = _FgLinkMonitorPacketRecv_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1, 7),
    _FgLinkMonitorPacketRecv_Type()
)
fgLinkMonitorPacketRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLinkMonitorPacketRecv.setStatus("current")
_FgLinkMonitorPacketLoss_Type = DisplayString
_FgLinkMonitorPacketLoss_Object = MibTableColumn
fgLinkMonitorPacketLoss = _FgLinkMonitorPacketLoss_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1, 8),
    _FgLinkMonitorPacketLoss_Type()
)
fgLinkMonitorPacketLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLinkMonitorPacketLoss.setStatus("current")
_FgLinkMonitorVdom_Type = DisplayString
_FgLinkMonitorVdom_Object = MibTableColumn
fgLinkMonitorVdom = _FgLinkMonitorVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1, 9),
    _FgLinkMonitorVdom_Type()
)
fgLinkMonitorVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLinkMonitorVdom.setStatus("current")
_FgFirewall_ObjectIdentity = ObjectIdentity
fgFirewall = _FgFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5)
)
_FgFwPolicies_ObjectIdentity = ObjectIdentity
fgFwPolicies = _FgFwPolicies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1)
)
_FgFwPolInfo_ObjectIdentity = ObjectIdentity
fgFwPolInfo = _FgFwPolInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 1)
)
_FgFwPolTables_ObjectIdentity = ObjectIdentity
fgFwPolTables = _FgFwPolTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2)
)
_FgFwPolStatsTable_Object = MibTable
fgFwPolStatsTable = _FgFwPolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fgFwPolStatsTable.setStatus("current")
_FgFwPolStatsEntry_Object = MibTableRow
fgFwPolStatsEntry = _FgFwPolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 1, 1)
)
fgFwPolStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgFwPolID"),
)
if mibBuilder.loadTexts:
    fgFwPolStatsEntry.setStatus("current")
_FgFwPolID_Type = FnIndex
_FgFwPolID_Object = MibTableColumn
fgFwPolID = _FgFwPolID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 1, 1, 1),
    _FgFwPolID_Type()
)
fgFwPolID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgFwPolID.setStatus("current")
_FgFwPolPktCount_Type = Counter32
_FgFwPolPktCount_Object = MibTableColumn
fgFwPolPktCount = _FgFwPolPktCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 1, 1, 2),
    _FgFwPolPktCount_Type()
)
fgFwPolPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwPolPktCount.setStatus("current")
_FgFwPolByteCount_Type = Counter32
_FgFwPolByteCount_Object = MibTableColumn
fgFwPolByteCount = _FgFwPolByteCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 1, 1, 3),
    _FgFwPolByteCount_Type()
)
fgFwPolByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwPolByteCount.setStatus("current")
_FgFwPolLastUsed_Type = DisplayString
_FgFwPolLastUsed_Object = MibTableColumn
fgFwPolLastUsed = _FgFwPolLastUsed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 1, 1, 4),
    _FgFwPolLastUsed_Type()
)
fgFwPolLastUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwPolLastUsed.setStatus("current")
_FgFwPolPktCountHc_Type = Counter64
_FgFwPolPktCountHc_Object = MibTableColumn
fgFwPolPktCountHc = _FgFwPolPktCountHc_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 1, 1, 5),
    _FgFwPolPktCountHc_Type()
)
fgFwPolPktCountHc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwPolPktCountHc.setStatus("current")
_FgFwPolByteCountHc_Type = Counter64
_FgFwPolByteCountHc_Object = MibTableColumn
fgFwPolByteCountHc = _FgFwPolByteCountHc_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 1, 1, 6),
    _FgFwPolByteCountHc_Type()
)
fgFwPolByteCountHc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwPolByteCountHc.setStatus("current")
_FgFwPol6StatsTable_Object = MibTable
fgFwPol6StatsTable = _FgFwPol6StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fgFwPol6StatsTable.setStatus("current")
_FgFwPol6StatsEntry_Object = MibTableRow
fgFwPol6StatsEntry = _FgFwPol6StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 2, 1)
)
fgFwPol6StatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgFwPol6ID"),
)
if mibBuilder.loadTexts:
    fgFwPol6StatsEntry.setStatus("current")
_FgFwPol6ID_Type = FnIndex
_FgFwPol6ID_Object = MibTableColumn
fgFwPol6ID = _FgFwPol6ID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 2, 1, 1),
    _FgFwPol6ID_Type()
)
fgFwPol6ID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgFwPol6ID.setStatus("current")
_FgFwPol6PktCount_Type = Counter64
_FgFwPol6PktCount_Object = MibTableColumn
fgFwPol6PktCount = _FgFwPol6PktCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 2, 1, 2),
    _FgFwPol6PktCount_Type()
)
fgFwPol6PktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwPol6PktCount.setStatus("current")
_FgFwPol6ByteCount_Type = Counter64
_FgFwPol6ByteCount_Object = MibTableColumn
fgFwPol6ByteCount = _FgFwPol6ByteCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 2, 1, 3),
    _FgFwPol6ByteCount_Type()
)
fgFwPol6ByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwPol6ByteCount.setStatus("current")
_FgFwPol6LastUsed_Type = DisplayString
_FgFwPol6LastUsed_Object = MibTableColumn
fgFwPol6LastUsed = _FgFwPol6LastUsed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 2, 1, 4),
    _FgFwPol6LastUsed_Type()
)
fgFwPol6LastUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwPol6LastUsed.setStatus("current")
_FgFwUsers_ObjectIdentity = ObjectIdentity
fgFwUsers = _FgFwUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2)
)
_FgFwUserInfo_ObjectIdentity = ObjectIdentity
fgFwUserInfo = _FgFwUserInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 1)
)
_FgFwUserNumber_Type = Integer32
_FgFwUserNumber_Object = MibScalar
fgFwUserNumber = _FgFwUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 1, 1),
    _FgFwUserNumber_Type()
)
fgFwUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwUserNumber.setStatus("current")
_FgFwUserAuthTimeout_Type = Integer32
_FgFwUserAuthTimeout_Object = MibScalar
fgFwUserAuthTimeout = _FgFwUserAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 1, 2),
    _FgFwUserAuthTimeout_Type()
)
fgFwUserAuthTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwUserAuthTimeout.setStatus("current")
_FgFwUserTables_ObjectIdentity = ObjectIdentity
fgFwUserTables = _FgFwUserTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 2)
)
_FgFwUserTable_Object = MibTable
fgFwUserTable = _FgFwUserTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fgFwUserTable.setStatus("current")
_FgFwUserEntry_Object = MibTableRow
fgFwUserEntry = _FgFwUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 2, 1, 1)
)
fgFwUserEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgFwUserIndex"),
)
if mibBuilder.loadTexts:
    fgFwUserEntry.setStatus("current")
_FgFwUserIndex_Type = FnIndex
_FgFwUserIndex_Object = MibTableColumn
fgFwUserIndex = _FgFwUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 2, 1, 1, 1),
    _FgFwUserIndex_Type()
)
fgFwUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgFwUserIndex.setStatus("current")
_FgFwUserName_Type = DisplayString
_FgFwUserName_Object = MibTableColumn
fgFwUserName = _FgFwUserName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 2, 1, 1, 2),
    _FgFwUserName_Type()
)
fgFwUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwUserName.setStatus("current")
_FgFwUserAuth_Type = FgFwUserAuthType
_FgFwUserAuth_Object = MibTableColumn
fgFwUserAuth = _FgFwUserAuth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 2, 1, 1, 3),
    _FgFwUserAuth_Type()
)
fgFwUserAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwUserAuth.setStatus("current")
_FgFwUserState_Type = FnBoolState
_FgFwUserState_Object = MibTableColumn
fgFwUserState = _FgFwUserState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 2, 1, 1, 4),
    _FgFwUserState_Type()
)
fgFwUserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwUserState.setStatus("current")
_FgFwUserVdom_Type = FgVdIndex
_FgFwUserVdom_Object = MibTableColumn
fgFwUserVdom = _FgFwUserVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 2, 1, 1, 5),
    _FgFwUserVdom_Type()
)
fgFwUserVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwUserVdom.setStatus("current")
_FgMgmt_ObjectIdentity = ObjectIdentity
fgMgmt = _FgMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6)
)
_FgFmTrapPrefix_ObjectIdentity = ObjectIdentity
fgFmTrapPrefix = _FgFmTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 0)
)
_FgAdmin_ObjectIdentity = ObjectIdentity
fgAdmin = _FgAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 1)
)
_FgAdminOptions_ObjectIdentity = ObjectIdentity
fgAdminOptions = _FgAdminOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 1, 1)
)
_FgAdminIdleTimeout_Type = Integer32
_FgAdminIdleTimeout_Object = MibScalar
fgAdminIdleTimeout = _FgAdminIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 1, 1, 1),
    _FgAdminIdleTimeout_Type()
)
fgAdminIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAdminIdleTimeout.setStatus("current")
_FgAdminLcdProtection_Type = FnBoolState
_FgAdminLcdProtection_Object = MibScalar
fgAdminLcdProtection = _FgAdminLcdProtection_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 1, 1, 2),
    _FgAdminLcdProtection_Type()
)
fgAdminLcdProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAdminLcdProtection.setStatus("current")
_FgAdminTables_ObjectIdentity = ObjectIdentity
fgAdminTables = _FgAdminTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 1, 2)
)
_FgAdminTable_Object = MibTable
fgAdminTable = _FgAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fgAdminTable.setStatus("current")
_FgAdminEntry_Object = MibTableRow
fgAdminEntry = _FgAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fgAdminEntry.setStatus("current")
_FgAdminVdom_Type = FgVdIndex
_FgAdminVdom_Object = MibTableColumn
fgAdminVdom = _FgAdminVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 1, 2, 1, 1, 1),
    _FgAdminVdom_Type()
)
fgAdminVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAdminVdom.setStatus("current")
_FgMgmtTrapObjects_ObjectIdentity = ObjectIdentity
fgMgmtTrapObjects = _FgMgmtTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 2)
)
_FgManIfIp_Type = IpAddress
_FgManIfIp_Object = MibScalar
fgManIfIp = _FgManIfIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 2, 1),
    _FgManIfIp_Type()
)
fgManIfIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgManIfIp.setStatus("current")
_FgManIfMask_Type = IpAddress
_FgManIfMask_Object = MibScalar
fgManIfMask = _FgManIfMask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 2, 2),
    _FgManIfMask_Type()
)
fgManIfMask.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgManIfMask.setStatus("current")
_FgManIfIp6_Type = Ipv6Address
_FgManIfIp6_Object = MibScalar
fgManIfIp6 = _FgManIfIp6_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 2, 3),
    _FgManIfIp6_Type()
)
fgManIfIp6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgManIfIp6.setStatus("current")
_FgIntf_ObjectIdentity = ObjectIdentity
fgIntf = _FgIntf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7)
)
_FgIntfInfo_ObjectIdentity = ObjectIdentity
fgIntfInfo = _FgIntfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 1)
)
_FgIntfTables_ObjectIdentity = ObjectIdentity
fgIntfTables = _FgIntfTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 2)
)
_FgIntfTable_Object = MibTable
fgIntfTable = _FgIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 2, 1)
)
if mibBuilder.loadTexts:
    fgIntfTable.setStatus("current")
_FgIntfEntry_Object = MibTableRow
fgIntfEntry = _FgIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fgIntfEntry.setStatus("current")
_FgIntfEntVdom_Type = FgVdIndex
_FgIntfEntVdom_Object = MibTableColumn
fgIntfEntVdom = _FgIntfEntVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 2, 1, 1, 1),
    _FgIntfEntVdom_Type()
)
fgIntfEntVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfEntVdom.setStatus("current")
_FgIntfVrrps_ObjectIdentity = ObjectIdentity
fgIntfVrrps = _FgIntfVrrps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 3)
)
_FgIntfVrrpCount_Type = Integer32
_FgIntfVrrpCount_Object = MibScalar
fgIntfVrrpCount = _FgIntfVrrpCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 3, 1),
    _FgIntfVrrpCount_Type()
)
fgIntfVrrpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfVrrpCount.setStatus("current")
_FgIntfVrrpTable_Object = MibTable
fgIntfVrrpTable = _FgIntfVrrpTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 3, 2)
)
if mibBuilder.loadTexts:
    fgIntfVrrpTable.setStatus("current")
_FgIntfVrrpEntry_Object = MibTableRow
fgIntfVrrpEntry = _FgIntfVrrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 3, 2, 1)
)
fgIntfVrrpEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgIntfVrrpEntIndex"),
)
if mibBuilder.loadTexts:
    fgIntfVrrpEntry.setStatus("current")
_FgIntfVrrpEntIndex_Type = FnIndex
_FgIntfVrrpEntIndex_Object = MibTableColumn
fgIntfVrrpEntIndex = _FgIntfVrrpEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 3, 2, 1, 1),
    _FgIntfVrrpEntIndex_Type()
)
fgIntfVrrpEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgIntfVrrpEntIndex.setStatus("current")
_FgIntfVrrpEntVrId_Type = FnIndex
_FgIntfVrrpEntVrId_Object = MibTableColumn
fgIntfVrrpEntVrId = _FgIntfVrrpEntVrId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 3, 2, 1, 2),
    _FgIntfVrrpEntVrId_Type()
)
fgIntfVrrpEntVrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfVrrpEntVrId.setStatus("current")
_FgIntfVrrpEntGrpId_Type = FnIndex
_FgIntfVrrpEntGrpId_Object = MibTableColumn
fgIntfVrrpEntGrpId = _FgIntfVrrpEntGrpId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 3, 2, 1, 3),
    _FgIntfVrrpEntGrpId_Type()
)
fgIntfVrrpEntGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfVrrpEntGrpId.setStatus("current")
_FgIntfVrrpEntIfName_Type = DisplayString
_FgIntfVrrpEntIfName_Object = MibTableColumn
fgIntfVrrpEntIfName = _FgIntfVrrpEntIfName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 3, 2, 1, 4),
    _FgIntfVrrpEntIfName_Type()
)
fgIntfVrrpEntIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfVrrpEntIfName.setStatus("current")


class _FgIntfVrrpEntState_Type(Integer32):
    """Custom type fgIntfVrrpEntState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("master", 2))
    )


_FgIntfVrrpEntState_Type.__name__ = "Integer32"
_FgIntfVrrpEntState_Object = MibTableColumn
fgIntfVrrpEntState = _FgIntfVrrpEntState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 3, 2, 1, 5),
    _FgIntfVrrpEntState_Type()
)
fgIntfVrrpEntState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfVrrpEntState.setStatus("current")
_FgIntfVrrpEntVrIp_Type = IpAddress
_FgIntfVrrpEntVrIp_Object = MibTableColumn
fgIntfVrrpEntVrIp = _FgIntfVrrpEntVrIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 3, 2, 1, 6),
    _FgIntfVrrpEntVrIp_Type()
)
fgIntfVrrpEntVrIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfVrrpEntVrIp.setStatus("current")
_FgIntfVlanHbs_ObjectIdentity = ObjectIdentity
fgIntfVlanHbs = _FgIntfVlanHbs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 4)
)
_FgIntfVlanHbCount_Type = Integer32
_FgIntfVlanHbCount_Object = MibScalar
fgIntfVlanHbCount = _FgIntfVlanHbCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 4, 1),
    _FgIntfVlanHbCount_Type()
)
fgIntfVlanHbCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfVlanHbCount.setStatus("current")
_FgIntfVlanHbTable_Object = MibTable
fgIntfVlanHbTable = _FgIntfVlanHbTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 4, 2)
)
if mibBuilder.loadTexts:
    fgIntfVlanHbTable.setStatus("current")
_FgIntfVlanHbEntry_Object = MibTableRow
fgIntfVlanHbEntry = _FgIntfVlanHbEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 4, 2, 1)
)
fgIntfVlanHbEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgIntfVlanHbEntIndex"),
)
if mibBuilder.loadTexts:
    fgIntfVlanHbEntry.setStatus("current")
_FgIntfVlanHbEntIndex_Type = FnIndex
_FgIntfVlanHbEntIndex_Object = MibTableColumn
fgIntfVlanHbEntIndex = _FgIntfVlanHbEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 4, 2, 1, 1),
    _FgIntfVlanHbEntIndex_Type()
)
fgIntfVlanHbEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgIntfVlanHbEntIndex.setStatus("current")
_FgIntfVlanHbEntIfName_Type = DisplayString
_FgIntfVlanHbEntIfName_Object = MibTableColumn
fgIntfVlanHbEntIfName = _FgIntfVlanHbEntIfName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 4, 2, 1, 2),
    _FgIntfVlanHbEntIfName_Type()
)
fgIntfVlanHbEntIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfVlanHbEntIfName.setStatus("current")
_FgIntfVlanHbEntSerial_Type = DisplayString
_FgIntfVlanHbEntSerial_Object = MibTableColumn
fgIntfVlanHbEntSerial = _FgIntfVlanHbEntSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 4, 2, 1, 3),
    _FgIntfVlanHbEntSerial_Type()
)
fgIntfVlanHbEntSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfVlanHbEntSerial.setStatus("current")


class _FgIntfVlanHbEntState_Type(Integer32):
    """Custom type fgIntfVlanHbEntState based on Integer32"""
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


_FgIntfVlanHbEntState_Type.__name__ = "Integer32"
_FgIntfVlanHbEntState_Object = MibTableColumn
fgIntfVlanHbEntState = _FgIntfVlanHbEntState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 4, 2, 1, 4),
    _FgIntfVlanHbEntState_Type()
)
fgIntfVlanHbEntState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfVlanHbEntState.setStatus("current")
_FgAntivirus_ObjectIdentity = ObjectIdentity
fgAntivirus = _FgAntivirus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8)
)
_FgAvInfo_ObjectIdentity = ObjectIdentity
fgAvInfo = _FgAvInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 1)
)
_FgAvTables_ObjectIdentity = ObjectIdentity
fgAvTables = _FgAvTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2)
)
_FgAvStatsTable_Object = MibTable
fgAvStatsTable = _FgAvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1)
)
if mibBuilder.loadTexts:
    fgAvStatsTable.setStatus("current")
_FgAvStatsEntry_Object = MibTableRow
fgAvStatsEntry = _FgAvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fgAvStatsEntry.setStatus("current")
_FgAvVirusDetected_Type = Counter32
_FgAvVirusDetected_Object = MibTableColumn
fgAvVirusDetected = _FgAvVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 1),
    _FgAvVirusDetected_Type()
)
fgAvVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvVirusDetected.setStatus("current")
_FgAvVirusBlocked_Type = Counter32
_FgAvVirusBlocked_Object = MibTableColumn
fgAvVirusBlocked = _FgAvVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 2),
    _FgAvVirusBlocked_Type()
)
fgAvVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvVirusBlocked.setStatus("current")
_FgAvHTTPVirusDetected_Type = Counter32
_FgAvHTTPVirusDetected_Object = MibTableColumn
fgAvHTTPVirusDetected = _FgAvHTTPVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 3),
    _FgAvHTTPVirusDetected_Type()
)
fgAvHTTPVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvHTTPVirusDetected.setStatus("current")
_FgAvHTTPVirusBlocked_Type = Counter32
_FgAvHTTPVirusBlocked_Object = MibTableColumn
fgAvHTTPVirusBlocked = _FgAvHTTPVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 4),
    _FgAvHTTPVirusBlocked_Type()
)
fgAvHTTPVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvHTTPVirusBlocked.setStatus("current")
_FgAvSMTPVirusDetected_Type = Counter32
_FgAvSMTPVirusDetected_Object = MibTableColumn
fgAvSMTPVirusDetected = _FgAvSMTPVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 5),
    _FgAvSMTPVirusDetected_Type()
)
fgAvSMTPVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvSMTPVirusDetected.setStatus("current")
_FgAvSMTPVirusBlocked_Type = Counter32
_FgAvSMTPVirusBlocked_Object = MibTableColumn
fgAvSMTPVirusBlocked = _FgAvSMTPVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 6),
    _FgAvSMTPVirusBlocked_Type()
)
fgAvSMTPVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvSMTPVirusBlocked.setStatus("current")
_FgAvPOP3VirusDetected_Type = Counter32
_FgAvPOP3VirusDetected_Object = MibTableColumn
fgAvPOP3VirusDetected = _FgAvPOP3VirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 7),
    _FgAvPOP3VirusDetected_Type()
)
fgAvPOP3VirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvPOP3VirusDetected.setStatus("current")
_FgAvPOP3VirusBlocked_Type = Counter32
_FgAvPOP3VirusBlocked_Object = MibTableColumn
fgAvPOP3VirusBlocked = _FgAvPOP3VirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 8),
    _FgAvPOP3VirusBlocked_Type()
)
fgAvPOP3VirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvPOP3VirusBlocked.setStatus("current")
_FgAvIMAPVirusDetected_Type = Counter32
_FgAvIMAPVirusDetected_Object = MibTableColumn
fgAvIMAPVirusDetected = _FgAvIMAPVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 9),
    _FgAvIMAPVirusDetected_Type()
)
fgAvIMAPVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvIMAPVirusDetected.setStatus("current")
_FgAvIMAPVirusBlocked_Type = Counter32
_FgAvIMAPVirusBlocked_Object = MibTableColumn
fgAvIMAPVirusBlocked = _FgAvIMAPVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 10),
    _FgAvIMAPVirusBlocked_Type()
)
fgAvIMAPVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvIMAPVirusBlocked.setStatus("current")
_FgAvFTPVirusDetected_Type = Counter32
_FgAvFTPVirusDetected_Object = MibTableColumn
fgAvFTPVirusDetected = _FgAvFTPVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 11),
    _FgAvFTPVirusDetected_Type()
)
fgAvFTPVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvFTPVirusDetected.setStatus("current")
_FgAvFTPVirusBlocked_Type = Counter32
_FgAvFTPVirusBlocked_Object = MibTableColumn
fgAvFTPVirusBlocked = _FgAvFTPVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 12),
    _FgAvFTPVirusBlocked_Type()
)
fgAvFTPVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvFTPVirusBlocked.setStatus("current")
_FgAvIMVirusDetected_Type = Counter32
_FgAvIMVirusDetected_Object = MibTableColumn
fgAvIMVirusDetected = _FgAvIMVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 13),
    _FgAvIMVirusDetected_Type()
)
fgAvIMVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvIMVirusDetected.setStatus("current")
_FgAvIMVirusBlocked_Type = Counter32
_FgAvIMVirusBlocked_Object = MibTableColumn
fgAvIMVirusBlocked = _FgAvIMVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 14),
    _FgAvIMVirusBlocked_Type()
)
fgAvIMVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvIMVirusBlocked.setStatus("current")
_FgAvNNTPVirusDetected_Type = Counter32
_FgAvNNTPVirusDetected_Object = MibTableColumn
fgAvNNTPVirusDetected = _FgAvNNTPVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 15),
    _FgAvNNTPVirusDetected_Type()
)
fgAvNNTPVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvNNTPVirusDetected.setStatus("current")
_FgAvNNTPVirusBlocked_Type = Counter32
_FgAvNNTPVirusBlocked_Object = MibTableColumn
fgAvNNTPVirusBlocked = _FgAvNNTPVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 16),
    _FgAvNNTPVirusBlocked_Type()
)
fgAvNNTPVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvNNTPVirusBlocked.setStatus("current")
_FgAvOversizedDetected_Type = Counter32
_FgAvOversizedDetected_Object = MibTableColumn
fgAvOversizedDetected = _FgAvOversizedDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 17),
    _FgAvOversizedDetected_Type()
)
fgAvOversizedDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvOversizedDetected.setStatus("current")
_FgAvOversizedBlocked_Type = Counter32
_FgAvOversizedBlocked_Object = MibTableColumn
fgAvOversizedBlocked = _FgAvOversizedBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 18),
    _FgAvOversizedBlocked_Type()
)
fgAvOversizedBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvOversizedBlocked.setStatus("current")
_FgAvTrapObjects_ObjectIdentity = ObjectIdentity
fgAvTrapObjects = _FgAvTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 3)
)
_FgAvTrapVirName_Type = DisplayString
_FgAvTrapVirName_Object = MibScalar
fgAvTrapVirName = _FgAvTrapVirName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 3, 1),
    _FgAvTrapVirName_Type()
)
fgAvTrapVirName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgAvTrapVirName.setStatus("current")
_FgIps_ObjectIdentity = ObjectIdentity
fgIps = _FgIps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9)
)
_FgIpsInfo_ObjectIdentity = ObjectIdentity
fgIpsInfo = _FgIpsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 1)
)
_FgIpsTables_ObjectIdentity = ObjectIdentity
fgIpsTables = _FgIpsTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 2)
)
_FgIpsStatsTable_Object = MibTable
fgIpsStatsTable = _FgIpsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 2, 1)
)
if mibBuilder.loadTexts:
    fgIpsStatsTable.setStatus("current")
_FgIpsStatsEntry_Object = MibTableRow
fgIpsStatsEntry = _FgIpsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fgIpsStatsEntry.setStatus("current")
_FgIpsIntrusionsDetected_Type = Counter32
_FgIpsIntrusionsDetected_Object = MibTableColumn
fgIpsIntrusionsDetected = _FgIpsIntrusionsDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 2, 1, 1, 1),
    _FgIpsIntrusionsDetected_Type()
)
fgIpsIntrusionsDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpsIntrusionsDetected.setStatus("current")
_FgIpsIntrusionsBlocked_Type = Counter32
_FgIpsIntrusionsBlocked_Object = MibTableColumn
fgIpsIntrusionsBlocked = _FgIpsIntrusionsBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 2, 1, 1, 2),
    _FgIpsIntrusionsBlocked_Type()
)
fgIpsIntrusionsBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpsIntrusionsBlocked.setStatus("current")
_FgIpsCritSevDetections_Type = Counter32
_FgIpsCritSevDetections_Object = MibTableColumn
fgIpsCritSevDetections = _FgIpsCritSevDetections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 2, 1, 1, 3),
    _FgIpsCritSevDetections_Type()
)
fgIpsCritSevDetections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpsCritSevDetections.setStatus("current")
_FgIpsHighSevDetections_Type = Counter32
_FgIpsHighSevDetections_Object = MibTableColumn
fgIpsHighSevDetections = _FgIpsHighSevDetections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 2, 1, 1, 4),
    _FgIpsHighSevDetections_Type()
)
fgIpsHighSevDetections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpsHighSevDetections.setStatus("current")
_FgIpsMedSevDetections_Type = Counter32
_FgIpsMedSevDetections_Object = MibTableColumn
fgIpsMedSevDetections = _FgIpsMedSevDetections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 2, 1, 1, 5),
    _FgIpsMedSevDetections_Type()
)
fgIpsMedSevDetections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpsMedSevDetections.setStatus("current")
_FgIpsLowSevDetections_Type = Counter32
_FgIpsLowSevDetections_Object = MibTableColumn
fgIpsLowSevDetections = _FgIpsLowSevDetections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 2, 1, 1, 6),
    _FgIpsLowSevDetections_Type()
)
fgIpsLowSevDetections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpsLowSevDetections.setStatus("current")
_FgIpsInfoSevDetections_Type = Counter32
_FgIpsInfoSevDetections_Object = MibTableColumn
fgIpsInfoSevDetections = _FgIpsInfoSevDetections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 2, 1, 1, 7),
    _FgIpsInfoSevDetections_Type()
)
fgIpsInfoSevDetections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpsInfoSevDetections.setStatus("current")
_FgIpsSignatureDetections_Type = Counter32
_FgIpsSignatureDetections_Object = MibTableColumn
fgIpsSignatureDetections = _FgIpsSignatureDetections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 2, 1, 1, 8),
    _FgIpsSignatureDetections_Type()
)
fgIpsSignatureDetections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpsSignatureDetections.setStatus("current")
_FgIpsAnomalyDetections_Type = Counter32
_FgIpsAnomalyDetections_Object = MibTableColumn
fgIpsAnomalyDetections = _FgIpsAnomalyDetections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 2, 1, 1, 9),
    _FgIpsAnomalyDetections_Type()
)
fgIpsAnomalyDetections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpsAnomalyDetections.setStatus("current")
_FgIpsTrapObjects_ObjectIdentity = ObjectIdentity
fgIpsTrapObjects = _FgIpsTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 3)
)
_FgIpsTrapSigId_Type = FnIndex
_FgIpsTrapSigId_Object = MibScalar
fgIpsTrapSigId = _FgIpsTrapSigId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 3, 1),
    _FgIpsTrapSigId_Type()
)
fgIpsTrapSigId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgIpsTrapSigId.setStatus("current")
_FgIpsTrapSrcIp_Type = IpAddress
_FgIpsTrapSrcIp_Object = MibScalar
fgIpsTrapSrcIp = _FgIpsTrapSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 3, 2),
    _FgIpsTrapSrcIp_Type()
)
fgIpsTrapSrcIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgIpsTrapSrcIp.setStatus("current")
_FgIpsTrapSigMsg_Type = DisplayString
_FgIpsTrapSigMsg_Object = MibScalar
fgIpsTrapSigMsg = _FgIpsTrapSigMsg_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 3, 3),
    _FgIpsTrapSigMsg_Type()
)
fgIpsTrapSigMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgIpsTrapSigMsg.setStatus("current")
_FgApplications_ObjectIdentity = ObjectIdentity
fgApplications = _FgApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10)
)
_FgWebfilter_ObjectIdentity = ObjectIdentity
fgWebfilter = _FgWebfilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1)
)
_FgWebfilterInfo_ObjectIdentity = ObjectIdentity
fgWebfilterInfo = _FgWebfilterInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 1)
)
_FgWebfilterTables_ObjectIdentity = ObjectIdentity
fgWebfilterTables = _FgWebfilterTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2)
)
_FgWebfilterStatsTable_Object = MibTable
fgWebfilterStatsTable = _FgWebfilterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fgWebfilterStatsTable.setStatus("current")
_FgWebfilterStatsEntry_Object = MibTableRow
fgWebfilterStatsEntry = _FgWebfilterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fgWebfilterStatsEntry.setStatus("current")
_FgWfHTTPBlocked_Type = Counter32
_FgWfHTTPBlocked_Object = MibTableColumn
fgWfHTTPBlocked = _FgWfHTTPBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 1, 1, 1),
    _FgWfHTTPBlocked_Type()
)
fgWfHTTPBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWfHTTPBlocked.setStatus("current")
_FgWfHTTPSBlocked_Type = Counter32
_FgWfHTTPSBlocked_Object = MibTableColumn
fgWfHTTPSBlocked = _FgWfHTTPSBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 1, 1, 2),
    _FgWfHTTPSBlocked_Type()
)
fgWfHTTPSBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWfHTTPSBlocked.setStatus("current")
_FgWfHTTPURLBlocked_Type = Counter32
_FgWfHTTPURLBlocked_Object = MibTableColumn
fgWfHTTPURLBlocked = _FgWfHTTPURLBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 1, 1, 3),
    _FgWfHTTPURLBlocked_Type()
)
fgWfHTTPURLBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWfHTTPURLBlocked.setStatus("current")
_FgWfHTTPSURLBlocked_Type = Counter32
_FgWfHTTPSURLBlocked_Object = MibTableColumn
fgWfHTTPSURLBlocked = _FgWfHTTPSURLBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 1, 1, 4),
    _FgWfHTTPSURLBlocked_Type()
)
fgWfHTTPSURLBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWfHTTPSURLBlocked.setStatus("current")
_FgWfActiveXBlocked_Type = Counter32
_FgWfActiveXBlocked_Object = MibTableColumn
fgWfActiveXBlocked = _FgWfActiveXBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 1, 1, 5),
    _FgWfActiveXBlocked_Type()
)
fgWfActiveXBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWfActiveXBlocked.setStatus("current")
_FgWfCookieBlocked_Type = Counter32
_FgWfCookieBlocked_Object = MibTableColumn
fgWfCookieBlocked = _FgWfCookieBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 1, 1, 6),
    _FgWfCookieBlocked_Type()
)
fgWfCookieBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWfCookieBlocked.setStatus("current")
_FgWfAppletBlocked_Type = Counter32
_FgWfAppletBlocked_Object = MibTableColumn
fgWfAppletBlocked = _FgWfAppletBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 1, 1, 7),
    _FgWfAppletBlocked_Type()
)
fgWfAppletBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWfAppletBlocked.setStatus("current")
_FgFortiGuardStatsTable_Object = MibTable
fgFortiGuardStatsTable = _FgFortiGuardStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fgFortiGuardStatsTable.setStatus("current")
_FgFortiGuardStatsEntry_Object = MibTableRow
fgFortiGuardStatsEntry = _FgFortiGuardStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fgFortiGuardStatsEntry.setStatus("current")
_FgFgWfHTTPExamined_Type = Counter32
_FgFgWfHTTPExamined_Object = MibTableColumn
fgFgWfHTTPExamined = _FgFgWfHTTPExamined_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 2, 1, 1),
    _FgFgWfHTTPExamined_Type()
)
fgFgWfHTTPExamined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFgWfHTTPExamined.setStatus("current")
_FgFgWfHTTPSExamined_Type = Counter32
_FgFgWfHTTPSExamined_Object = MibTableColumn
fgFgWfHTTPSExamined = _FgFgWfHTTPSExamined_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 2, 1, 2),
    _FgFgWfHTTPSExamined_Type()
)
fgFgWfHTTPSExamined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFgWfHTTPSExamined.setStatus("current")
_FgFgWfHTTPAllowed_Type = Counter32
_FgFgWfHTTPAllowed_Object = MibTableColumn
fgFgWfHTTPAllowed = _FgFgWfHTTPAllowed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 2, 1, 3),
    _FgFgWfHTTPAllowed_Type()
)
fgFgWfHTTPAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFgWfHTTPAllowed.setStatus("current")
_FgFgWfHTTPSAllowed_Type = Counter32
_FgFgWfHTTPSAllowed_Object = MibTableColumn
fgFgWfHTTPSAllowed = _FgFgWfHTTPSAllowed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 2, 1, 4),
    _FgFgWfHTTPSAllowed_Type()
)
fgFgWfHTTPSAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFgWfHTTPSAllowed.setStatus("current")
_FgFgWfHTTPBlocked_Type = Counter32
_FgFgWfHTTPBlocked_Object = MibTableColumn
fgFgWfHTTPBlocked = _FgFgWfHTTPBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 2, 1, 5),
    _FgFgWfHTTPBlocked_Type()
)
fgFgWfHTTPBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFgWfHTTPBlocked.setStatus("current")
_FgFgWfHTTPSBlocked_Type = Counter32
_FgFgWfHTTPSBlocked_Object = MibTableColumn
fgFgWfHTTPSBlocked = _FgFgWfHTTPSBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 2, 1, 6),
    _FgFgWfHTTPSBlocked_Type()
)
fgFgWfHTTPSBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFgWfHTTPSBlocked.setStatus("current")
_FgFgWfHTTPLogged_Type = Counter32
_FgFgWfHTTPLogged_Object = MibTableColumn
fgFgWfHTTPLogged = _FgFgWfHTTPLogged_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 2, 1, 7),
    _FgFgWfHTTPLogged_Type()
)
fgFgWfHTTPLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFgWfHTTPLogged.setStatus("current")
_FgFgWfHTTPSLogged_Type = Counter32
_FgFgWfHTTPSLogged_Object = MibTableColumn
fgFgWfHTTPSLogged = _FgFgWfHTTPSLogged_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 2, 1, 8),
    _FgFgWfHTTPSLogged_Type()
)
fgFgWfHTTPSLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFgWfHTTPSLogged.setStatus("current")
_FgFgWfHTTPOverridden_Type = Counter32
_FgFgWfHTTPOverridden_Object = MibTableColumn
fgFgWfHTTPOverridden = _FgFgWfHTTPOverridden_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 2, 1, 9),
    _FgFgWfHTTPOverridden_Type()
)
fgFgWfHTTPOverridden.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFgWfHTTPOverridden.setStatus("current")
_FgFgWfHTTPSOverridden_Type = Counter32
_FgFgWfHTTPSOverridden_Object = MibTableColumn
fgFgWfHTTPSOverridden = _FgFgWfHTTPSOverridden_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 2, 1, 10),
    _FgFgWfHTTPSOverridden_Type()
)
fgFgWfHTTPSOverridden.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFgWfHTTPSOverridden.setStatus("current")
_FgAppProxyHTTP_ObjectIdentity = ObjectIdentity
fgAppProxyHTTP = _FgAppProxyHTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 100)
)
_FgApHTTPUpTime_Type = Counter32
_FgApHTTPUpTime_Object = MibScalar
fgApHTTPUpTime = _FgApHTTPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 100, 1),
    _FgApHTTPUpTime_Type()
)
fgApHTTPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApHTTPUpTime.setStatus("deprecated")


class _FgApHTTPMemUsage_Type(Gauge32):
    """Custom type fgApHTTPMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgApHTTPMemUsage_Type.__name__ = "Gauge32"
_FgApHTTPMemUsage_Object = MibScalar
fgApHTTPMemUsage = _FgApHTTPMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 100, 2),
    _FgApHTTPMemUsage_Type()
)
fgApHTTPMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApHTTPMemUsage.setStatus("deprecated")
_FgApHTTPStatsTable_Object = MibTable
fgApHTTPStatsTable = _FgApHTTPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 100, 3)
)
if mibBuilder.loadTexts:
    fgApHTTPStatsTable.setStatus("current")
_FgApHTTPStatsEntry_Object = MibTableRow
fgApHTTPStatsEntry = _FgApHTTPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 100, 3, 1)
)
if mibBuilder.loadTexts:
    fgApHTTPStatsEntry.setStatus("current")
_FgApHTTPReqProcessed_Type = Counter32
_FgApHTTPReqProcessed_Object = MibTableColumn
fgApHTTPReqProcessed = _FgApHTTPReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 100, 3, 1, 1),
    _FgApHTTPReqProcessed_Type()
)
fgApHTTPReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApHTTPReqProcessed.setStatus("current")
_FgApHTTPConnections_Type = Unsigned32
_FgApHTTPConnections_Object = MibScalar
fgApHTTPConnections = _FgApHTTPConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 100, 4),
    _FgApHTTPConnections_Type()
)
fgApHTTPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApHTTPConnections.setStatus("current")
_FgApHTTPMaxConnections_Type = Unsigned32
_FgApHTTPMaxConnections_Object = MibScalar
fgApHTTPMaxConnections = _FgApHTTPMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 100, 5),
    _FgApHTTPMaxConnections_Type()
)
fgApHTTPMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApHTTPMaxConnections.setStatus("current")
_FgAppProxySMTP_ObjectIdentity = ObjectIdentity
fgAppProxySMTP = _FgAppProxySMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 101)
)
_FgApSMTPUpTime_Type = Counter32
_FgApSMTPUpTime_Object = MibScalar
fgApSMTPUpTime = _FgApSMTPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 101, 1),
    _FgApSMTPUpTime_Type()
)
fgApSMTPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApSMTPUpTime.setStatus("deprecated")


class _FgApSMTPMemUsage_Type(Gauge32):
    """Custom type fgApSMTPMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgApSMTPMemUsage_Type.__name__ = "Gauge32"
_FgApSMTPMemUsage_Object = MibScalar
fgApSMTPMemUsage = _FgApSMTPMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 101, 2),
    _FgApSMTPMemUsage_Type()
)
fgApSMTPMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApSMTPMemUsage.setStatus("deprecated")
_FgApSMTPStatsTable_Object = MibTable
fgApSMTPStatsTable = _FgApSMTPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 101, 3)
)
if mibBuilder.loadTexts:
    fgApSMTPStatsTable.setStatus("current")
_FgApSMTPStatsEntry_Object = MibTableRow
fgApSMTPStatsEntry = _FgApSMTPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 101, 3, 1)
)
if mibBuilder.loadTexts:
    fgApSMTPStatsEntry.setStatus("current")
_FgApSMTPReqProcessed_Type = Counter32
_FgApSMTPReqProcessed_Object = MibTableColumn
fgApSMTPReqProcessed = _FgApSMTPReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 101, 3, 1, 1),
    _FgApSMTPReqProcessed_Type()
)
fgApSMTPReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApSMTPReqProcessed.setStatus("current")
_FgApSMTPSpamDetected_Type = Counter32
_FgApSMTPSpamDetected_Object = MibTableColumn
fgApSMTPSpamDetected = _FgApSMTPSpamDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 101, 3, 1, 2),
    _FgApSMTPSpamDetected_Type()
)
fgApSMTPSpamDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApSMTPSpamDetected.setStatus("current")
_FgApSMTPConnections_Type = Unsigned32
_FgApSMTPConnections_Object = MibScalar
fgApSMTPConnections = _FgApSMTPConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 101, 4),
    _FgApSMTPConnections_Type()
)
fgApSMTPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApSMTPConnections.setStatus("current")
_FgApSMTPMaxConnections_Type = Unsigned32
_FgApSMTPMaxConnections_Object = MibScalar
fgApSMTPMaxConnections = _FgApSMTPMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 101, 5),
    _FgApSMTPMaxConnections_Type()
)
fgApSMTPMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApSMTPMaxConnections.setStatus("current")
_FgAppProxyPOP3_ObjectIdentity = ObjectIdentity
fgAppProxyPOP3 = _FgAppProxyPOP3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 102)
)
_FgApPOP3UpTime_Type = Counter32
_FgApPOP3UpTime_Object = MibScalar
fgApPOP3UpTime = _FgApPOP3UpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 102, 1),
    _FgApPOP3UpTime_Type()
)
fgApPOP3UpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApPOP3UpTime.setStatus("deprecated")


class _FgApPOP3MemUsage_Type(Gauge32):
    """Custom type fgApPOP3MemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgApPOP3MemUsage_Type.__name__ = "Gauge32"
_FgApPOP3MemUsage_Object = MibScalar
fgApPOP3MemUsage = _FgApPOP3MemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 102, 2),
    _FgApPOP3MemUsage_Type()
)
fgApPOP3MemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApPOP3MemUsage.setStatus("deprecated")
_FgApPOP3StatsTable_Object = MibTable
fgApPOP3StatsTable = _FgApPOP3StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 102, 3)
)
if mibBuilder.loadTexts:
    fgApPOP3StatsTable.setStatus("current")
_FgApPOP3StatsEntry_Object = MibTableRow
fgApPOP3StatsEntry = _FgApPOP3StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 102, 3, 1)
)
if mibBuilder.loadTexts:
    fgApPOP3StatsEntry.setStatus("current")
_FgApPOP3ReqProcessed_Type = Counter32
_FgApPOP3ReqProcessed_Object = MibTableColumn
fgApPOP3ReqProcessed = _FgApPOP3ReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 102, 3, 1, 1),
    _FgApPOP3ReqProcessed_Type()
)
fgApPOP3ReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApPOP3ReqProcessed.setStatus("current")
_FgApPOP3SpamDetected_Type = Counter32
_FgApPOP3SpamDetected_Object = MibTableColumn
fgApPOP3SpamDetected = _FgApPOP3SpamDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 102, 3, 1, 2),
    _FgApPOP3SpamDetected_Type()
)
fgApPOP3SpamDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApPOP3SpamDetected.setStatus("current")
_FgApPOP3Connections_Type = Unsigned32
_FgApPOP3Connections_Object = MibScalar
fgApPOP3Connections = _FgApPOP3Connections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 102, 4),
    _FgApPOP3Connections_Type()
)
fgApPOP3Connections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApPOP3Connections.setStatus("current")
_FgApPOP3MaxConnections_Type = Unsigned32
_FgApPOP3MaxConnections_Object = MibScalar
fgApPOP3MaxConnections = _FgApPOP3MaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 102, 5),
    _FgApPOP3MaxConnections_Type()
)
fgApPOP3MaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApPOP3MaxConnections.setStatus("current")
_FgAppProxyIMAP_ObjectIdentity = ObjectIdentity
fgAppProxyIMAP = _FgAppProxyIMAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 103)
)
_FgApIMAPUpTime_Type = Counter32
_FgApIMAPUpTime_Object = MibScalar
fgApIMAPUpTime = _FgApIMAPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 103, 1),
    _FgApIMAPUpTime_Type()
)
fgApIMAPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApIMAPUpTime.setStatus("deprecated")


class _FgApIMAPMemUsage_Type(Gauge32):
    """Custom type fgApIMAPMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgApIMAPMemUsage_Type.__name__ = "Gauge32"
_FgApIMAPMemUsage_Object = MibScalar
fgApIMAPMemUsage = _FgApIMAPMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 103, 2),
    _FgApIMAPMemUsage_Type()
)
fgApIMAPMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApIMAPMemUsage.setStatus("deprecated")
_FgApIMAPStatsTable_Object = MibTable
fgApIMAPStatsTable = _FgApIMAPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 103, 3)
)
if mibBuilder.loadTexts:
    fgApIMAPStatsTable.setStatus("current")
_FgApIMAPStatsEntry_Object = MibTableRow
fgApIMAPStatsEntry = _FgApIMAPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 103, 3, 1)
)
if mibBuilder.loadTexts:
    fgApIMAPStatsEntry.setStatus("current")
_FgApIMAPReqProcessed_Type = Counter32
_FgApIMAPReqProcessed_Object = MibTableColumn
fgApIMAPReqProcessed = _FgApIMAPReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 103, 3, 1, 1),
    _FgApIMAPReqProcessed_Type()
)
fgApIMAPReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApIMAPReqProcessed.setStatus("current")
_FgApIMAPSpamDetected_Type = Counter32
_FgApIMAPSpamDetected_Object = MibTableColumn
fgApIMAPSpamDetected = _FgApIMAPSpamDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 103, 3, 1, 2),
    _FgApIMAPSpamDetected_Type()
)
fgApIMAPSpamDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApIMAPSpamDetected.setStatus("current")
_FgApIMAPConnections_Type = Unsigned32
_FgApIMAPConnections_Object = MibScalar
fgApIMAPConnections = _FgApIMAPConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 103, 4),
    _FgApIMAPConnections_Type()
)
fgApIMAPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApIMAPConnections.setStatus("current")
_FgApIMAPMaxConnections_Type = Unsigned32
_FgApIMAPMaxConnections_Object = MibScalar
fgApIMAPMaxConnections = _FgApIMAPMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 103, 5),
    _FgApIMAPMaxConnections_Type()
)
fgApIMAPMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApIMAPMaxConnections.setStatus("current")
_FgAppProxyNNTP_ObjectIdentity = ObjectIdentity
fgAppProxyNNTP = _FgAppProxyNNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 104)
)
_FgApNNTPUpTime_Type = Counter32
_FgApNNTPUpTime_Object = MibScalar
fgApNNTPUpTime = _FgApNNTPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 104, 1),
    _FgApNNTPUpTime_Type()
)
fgApNNTPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApNNTPUpTime.setStatus("deprecated")


class _FgApNNTPMemUsage_Type(Gauge32):
    """Custom type fgApNNTPMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgApNNTPMemUsage_Type.__name__ = "Gauge32"
_FgApNNTPMemUsage_Object = MibScalar
fgApNNTPMemUsage = _FgApNNTPMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 104, 2),
    _FgApNNTPMemUsage_Type()
)
fgApNNTPMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApNNTPMemUsage.setStatus("deprecated")
_FgApNNTPStatsTable_Object = MibTable
fgApNNTPStatsTable = _FgApNNTPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 104, 3)
)
if mibBuilder.loadTexts:
    fgApNNTPStatsTable.setStatus("current")
_FgApNNTPStatsEntry_Object = MibTableRow
fgApNNTPStatsEntry = _FgApNNTPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 104, 3, 1)
)
if mibBuilder.loadTexts:
    fgApNNTPStatsEntry.setStatus("current")
_FgApNNTPReqProcessed_Type = Counter32
_FgApNNTPReqProcessed_Object = MibTableColumn
fgApNNTPReqProcessed = _FgApNNTPReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 104, 3, 1, 1),
    _FgApNNTPReqProcessed_Type()
)
fgApNNTPReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApNNTPReqProcessed.setStatus("current")
_FgApNNTPConnections_Type = Unsigned32
_FgApNNTPConnections_Object = MibScalar
fgApNNTPConnections = _FgApNNTPConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 104, 4),
    _FgApNNTPConnections_Type()
)
fgApNNTPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApNNTPConnections.setStatus("current")
_FgApNNTPMaxConnections_Type = Unsigned32
_FgApNNTPMaxConnections_Object = MibScalar
fgApNNTPMaxConnections = _FgApNNTPMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 104, 5),
    _FgApNNTPMaxConnections_Type()
)
fgApNNTPMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApNNTPMaxConnections.setStatus("current")
_FgAppProxyIM_ObjectIdentity = ObjectIdentity
fgAppProxyIM = _FgAppProxyIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 105)
)
_FgApIMUpTime_Type = Counter32
_FgApIMUpTime_Object = MibScalar
fgApIMUpTime = _FgApIMUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 105, 1),
    _FgApIMUpTime_Type()
)
fgApIMUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApIMUpTime.setStatus("current")


class _FgApIMMemUsage_Type(Gauge32):
    """Custom type fgApIMMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgApIMMemUsage_Type.__name__ = "Gauge32"
_FgApIMMemUsage_Object = MibScalar
fgApIMMemUsage = _FgApIMMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 105, 2),
    _FgApIMMemUsage_Type()
)
fgApIMMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApIMMemUsage.setStatus("current")
_FgApIMStatsTable_Object = MibTable
fgApIMStatsTable = _FgApIMStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 105, 3)
)
if mibBuilder.loadTexts:
    fgApIMStatsTable.setStatus("current")
_FgApIMStatsEntry_Object = MibTableRow
fgApIMStatsEntry = _FgApIMStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 105, 3, 1)
)
if mibBuilder.loadTexts:
    fgApIMStatsEntry.setStatus("current")
_FgApIMReqProcessed_Type = Counter32
_FgApIMReqProcessed_Object = MibTableColumn
fgApIMReqProcessed = _FgApIMReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 105, 3, 1, 1),
    _FgApIMReqProcessed_Type()
)
fgApIMReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApIMReqProcessed.setStatus("current")
_FgAppProxySIP_ObjectIdentity = ObjectIdentity
fgAppProxySIP = _FgAppProxySIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 106)
)
_FgApSIPUpTime_Type = Counter32
_FgApSIPUpTime_Object = MibScalar
fgApSIPUpTime = _FgApSIPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 106, 1),
    _FgApSIPUpTime_Type()
)
fgApSIPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApSIPUpTime.setStatus("current")


class _FgApSIPMemUsage_Type(Gauge32):
    """Custom type fgApSIPMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgApSIPMemUsage_Type.__name__ = "Gauge32"
_FgApSIPMemUsage_Object = MibScalar
fgApSIPMemUsage = _FgApSIPMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 106, 2),
    _FgApSIPMemUsage_Type()
)
fgApSIPMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApSIPMemUsage.setStatus("current")
_FgApSIPStatsTable_Object = MibTable
fgApSIPStatsTable = _FgApSIPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 106, 3)
)
if mibBuilder.loadTexts:
    fgApSIPStatsTable.setStatus("current")
_FgApSIPStatsEntry_Object = MibTableRow
fgApSIPStatsEntry = _FgApSIPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 106, 3, 1)
)
if mibBuilder.loadTexts:
    fgApSIPStatsEntry.setStatus("current")
_FgApSIPClientReg_Type = Counter32
_FgApSIPClientReg_Object = MibTableColumn
fgApSIPClientReg = _FgApSIPClientReg_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 106, 3, 1, 1),
    _FgApSIPClientReg_Type()
)
fgApSIPClientReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApSIPClientReg.setStatus("current")
_FgApSIPCallHandling_Type = Counter32
_FgApSIPCallHandling_Object = MibTableColumn
fgApSIPCallHandling = _FgApSIPCallHandling_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 106, 3, 1, 2),
    _FgApSIPCallHandling_Type()
)
fgApSIPCallHandling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApSIPCallHandling.setStatus("current")
_FgApSIPServices_Type = Counter32
_FgApSIPServices_Object = MibTableColumn
fgApSIPServices = _FgApSIPServices_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 106, 3, 1, 3),
    _FgApSIPServices_Type()
)
fgApSIPServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApSIPServices.setStatus("current")
_FgApSIPOtherReq_Type = Counter32
_FgApSIPOtherReq_Object = MibTableColumn
fgApSIPOtherReq = _FgApSIPOtherReq_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 106, 3, 1, 4),
    _FgApSIPOtherReq_Type()
)
fgApSIPOtherReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApSIPOtherReq.setStatus("current")
_FgAppScanUnit_ObjectIdentity = ObjectIdentity
fgAppScanUnit = _FgAppScanUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 107)
)
_FgAppSuNumber_Type = Gauge32
_FgAppSuNumber_Object = MibScalar
fgAppSuNumber = _FgAppSuNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 107, 1),
    _FgAppSuNumber_Type()
)
fgAppSuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppSuNumber.setStatus("current")
_FgAppSuStatsTable_Object = MibTable
fgAppSuStatsTable = _FgAppSuStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 107, 2)
)
if mibBuilder.loadTexts:
    fgAppSuStatsTable.setStatus("current")
_FgAppSuStatsEntry_Object = MibTableRow
fgAppSuStatsEntry = _FgAppSuStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 107, 2, 1)
)
fgAppSuStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgAppSuIndex"),
)
if mibBuilder.loadTexts:
    fgAppSuStatsEntry.setStatus("current")
_FgAppSuIndex_Type = FnIndex
_FgAppSuIndex_Object = MibTableColumn
fgAppSuIndex = _FgAppSuIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 107, 2, 1, 1),
    _FgAppSuIndex_Type()
)
fgAppSuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgAppSuIndex.setStatus("current")
_FgAppSuFileScanned_Type = Counter32
_FgAppSuFileScanned_Object = MibTableColumn
fgAppSuFileScanned = _FgAppSuFileScanned_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 107, 2, 1, 2),
    _FgAppSuFileScanned_Type()
)
fgAppSuFileScanned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppSuFileScanned.setStatus("current")
_FgAppVoIP_ObjectIdentity = ObjectIdentity
fgAppVoIP = _FgAppVoIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 108)
)
_FgAppVoIPStatsTable_Object = MibTable
fgAppVoIPStatsTable = _FgAppVoIPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 108, 1)
)
if mibBuilder.loadTexts:
    fgAppVoIPStatsTable.setStatus("current")
_FgAppVoIPStatsEntry_Object = MibTableRow
fgAppVoIPStatsEntry = _FgAppVoIPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 108, 1, 1)
)
if mibBuilder.loadTexts:
    fgAppVoIPStatsEntry.setStatus("current")
_FgAppVoIPConn_Type = Gauge32
_FgAppVoIPConn_Object = MibTableColumn
fgAppVoIPConn = _FgAppVoIPConn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 108, 1, 1, 1),
    _FgAppVoIPConn_Type()
)
fgAppVoIPConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppVoIPConn.setStatus("current")
_FgAppVoIPCallBlocked_Type = Counter32
_FgAppVoIPCallBlocked_Object = MibTableColumn
fgAppVoIPCallBlocked = _FgAppVoIPCallBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 108, 1, 1, 2),
    _FgAppVoIPCallBlocked_Type()
)
fgAppVoIPCallBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppVoIPCallBlocked.setStatus("current")
_FgAppP2P_ObjectIdentity = ObjectIdentity
fgAppP2P = _FgAppP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 109)
)
_FgAppP2PStatsTable_Object = MibTable
fgAppP2PStatsTable = _FgAppP2PStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 109, 1)
)
if mibBuilder.loadTexts:
    fgAppP2PStatsTable.setStatus("current")
_FgAppP2PStatsEntry_Object = MibTableRow
fgAppP2PStatsEntry = _FgAppP2PStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 109, 1, 1)
)
if mibBuilder.loadTexts:
    fgAppP2PStatsEntry.setStatus("current")
_FgAppP2PConnBlocked_Type = Counter32
_FgAppP2PConnBlocked_Object = MibTableColumn
fgAppP2PConnBlocked = _FgAppP2PConnBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 109, 1, 1, 1),
    _FgAppP2PConnBlocked_Type()
)
fgAppP2PConnBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppP2PConnBlocked.setStatus("current")
_FgAppP2PProtoTable_Object = MibTable
fgAppP2PProtoTable = _FgAppP2PProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 109, 2)
)
if mibBuilder.loadTexts:
    fgAppP2PProtoTable.setStatus("current")
_FgAppP2PProtoEntry_Object = MibTableRow
fgAppP2PProtoEntry = _FgAppP2PProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 109, 2, 1)
)
fgAppP2PProtoEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgAppP2PProtEntProto"),
)
if mibBuilder.loadTexts:
    fgAppP2PProtoEntry.setStatus("current")
_FgAppP2PProtEntProto_Type = FgP2PProto
_FgAppP2PProtEntProto_Object = MibTableColumn
fgAppP2PProtEntProto = _FgAppP2PProtEntProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 109, 2, 1, 1),
    _FgAppP2PProtEntProto_Type()
)
fgAppP2PProtEntProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgAppP2PProtEntProto.setStatus("current")
_FgAppP2PProtEntBytes_Type = Counter64
_FgAppP2PProtEntBytes_Object = MibTableColumn
fgAppP2PProtEntBytes = _FgAppP2PProtEntBytes_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 109, 2, 1, 2),
    _FgAppP2PProtEntBytes_Type()
)
fgAppP2PProtEntBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppP2PProtEntBytes.setStatus("current")
_FgAppP2PProtoEntLastReset_Type = TimeTicks
_FgAppP2PProtoEntLastReset_Object = MibTableColumn
fgAppP2PProtoEntLastReset = _FgAppP2PProtoEntLastReset_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 109, 2, 1, 3),
    _FgAppP2PProtoEntLastReset_Type()
)
fgAppP2PProtoEntLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppP2PProtoEntLastReset.setStatus("current")
_FgAppIM_ObjectIdentity = ObjectIdentity
fgAppIM = _FgAppIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 110)
)
_FgAppIMStatsTable_Object = MibTable
fgAppIMStatsTable = _FgAppIMStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 110, 1)
)
if mibBuilder.loadTexts:
    fgAppIMStatsTable.setStatus("current")
_FgAppIMStatsEntry_Object = MibTableRow
fgAppIMStatsEntry = _FgAppIMStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 110, 1, 1)
)
if mibBuilder.loadTexts:
    fgAppIMStatsEntry.setStatus("current")
_FgAppIMMessages_Type = Counter32
_FgAppIMMessages_Object = MibTableColumn
fgAppIMMessages = _FgAppIMMessages_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 110, 1, 1, 1),
    _FgAppIMMessages_Type()
)
fgAppIMMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppIMMessages.setStatus("current")
_FgAppIMFileTransfered_Type = Counter32
_FgAppIMFileTransfered_Object = MibTableColumn
fgAppIMFileTransfered = _FgAppIMFileTransfered_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 110, 1, 1, 2),
    _FgAppIMFileTransfered_Type()
)
fgAppIMFileTransfered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppIMFileTransfered.setStatus("current")
_FgAppIMFileTxBlocked_Type = Counter32
_FgAppIMFileTxBlocked_Object = MibTableColumn
fgAppIMFileTxBlocked = _FgAppIMFileTxBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 110, 1, 1, 3),
    _FgAppIMFileTxBlocked_Type()
)
fgAppIMFileTxBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppIMFileTxBlocked.setStatus("current")
_FgAppIMConnBlocked_Type = Counter32
_FgAppIMConnBlocked_Object = MibTableColumn
fgAppIMConnBlocked = _FgAppIMConnBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 110, 1, 1, 4),
    _FgAppIMConnBlocked_Type()
)
fgAppIMConnBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppIMConnBlocked.setStatus("current")
_FgAppProxyFTP_ObjectIdentity = ObjectIdentity
fgAppProxyFTP = _FgAppProxyFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 111)
)
_FgApFTPUpTime_Type = Counter32
_FgApFTPUpTime_Object = MibScalar
fgApFTPUpTime = _FgApFTPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 111, 1),
    _FgApFTPUpTime_Type()
)
fgApFTPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApFTPUpTime.setStatus("deprecated")


class _FgApFTPMemUsage_Type(Gauge32):
    """Custom type fgApFTPMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgApFTPMemUsage_Type.__name__ = "Gauge32"
_FgApFTPMemUsage_Object = MibScalar
fgApFTPMemUsage = _FgApFTPMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 111, 2),
    _FgApFTPMemUsage_Type()
)
fgApFTPMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApFTPMemUsage.setStatus("deprecated")
_FgApFTPStatsTable_Object = MibTable
fgApFTPStatsTable = _FgApFTPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 111, 3)
)
if mibBuilder.loadTexts:
    fgApFTPStatsTable.setStatus("current")
_FgApFTPStatsEntry_Object = MibTableRow
fgApFTPStatsEntry = _FgApFTPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 111, 3, 1)
)
if mibBuilder.loadTexts:
    fgApFTPStatsEntry.setStatus("current")
_FgApFTPReqProcessed_Type = Counter32
_FgApFTPReqProcessed_Object = MibTableColumn
fgApFTPReqProcessed = _FgApFTPReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 111, 3, 1, 1),
    _FgApFTPReqProcessed_Type()
)
fgApFTPReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApFTPReqProcessed.setStatus("current")
_FgApFTPConnections_Type = Unsigned32
_FgApFTPConnections_Object = MibScalar
fgApFTPConnections = _FgApFTPConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 111, 4),
    _FgApFTPConnections_Type()
)
fgApFTPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApFTPConnections.setStatus("current")
_FgApFTPMaxConnections_Type = Unsigned32
_FgApFTPMaxConnections_Object = MibScalar
fgApFTPMaxConnections = _FgApFTPMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 111, 5),
    _FgApFTPMaxConnections_Type()
)
fgApFTPMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApFTPMaxConnections.setStatus("current")
_FgAppExplicitProxy_ObjectIdentity = ObjectIdentity
fgAppExplicitProxy = _FgAppExplicitProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112)
)
_FgExplicitProxyInfo_ObjectIdentity = ObjectIdentity
fgExplicitProxyInfo = _FgExplicitProxyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 1)
)
_FgExplicitProxyUpTime_Type = Counter32
_FgExplicitProxyUpTime_Object = MibScalar
fgExplicitProxyUpTime = _FgExplicitProxyUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 1, 1),
    _FgExplicitProxyUpTime_Type()
)
fgExplicitProxyUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyUpTime.setStatus("current")


class _FgExplicitProxyMemUsage_Type(Gauge32):
    """Custom type fgExplicitProxyMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgExplicitProxyMemUsage_Type.__name__ = "Gauge32"
_FgExplicitProxyMemUsage_Object = MibScalar
fgExplicitProxyMemUsage = _FgExplicitProxyMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 1, 2),
    _FgExplicitProxyMemUsage_Type()
)
fgExplicitProxyMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyMemUsage.setStatus("current")
_FgExplicitProxyRequests_Type = Counter64
_FgExplicitProxyRequests_Object = MibScalar
fgExplicitProxyRequests = _FgExplicitProxyRequests_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 1, 3),
    _FgExplicitProxyRequests_Type()
)
fgExplicitProxyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyRequests.setStatus("current")
_FgExplicitProxyStatsTable_Object = MibTable
fgExplicitProxyStatsTable = _FgExplicitProxyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 2)
)
if mibBuilder.loadTexts:
    fgExplicitProxyStatsTable.setStatus("current")
_FgExplicitProxyStatsEntry_Object = MibTableRow
fgExplicitProxyStatsEntry = _FgExplicitProxyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 2, 1)
)
fgExplicitProxyStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
)
if mibBuilder.loadTexts:
    fgExplicitProxyStatsEntry.setStatus("current")
_FgExplicitProxyUsers_Type = Integer32
_FgExplicitProxyUsers_Object = MibTableColumn
fgExplicitProxyUsers = _FgExplicitProxyUsers_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 2, 1, 1),
    _FgExplicitProxyUsers_Type()
)
fgExplicitProxyUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyUsers.setStatus("current")
_FgExplicitProxySessions_Type = Integer32
_FgExplicitProxySessions_Object = MibTableColumn
fgExplicitProxySessions = _FgExplicitProxySessions_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 2, 1, 2),
    _FgExplicitProxySessions_Type()
)
fgExplicitProxySessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxySessions.setStatus("current")
_FgExplicitProxyScanStatsTable_Object = MibTable
fgExplicitProxyScanStatsTable = _FgExplicitProxyScanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3)
)
if mibBuilder.loadTexts:
    fgExplicitProxyScanStatsTable.setStatus("current")
_FgExplicitProxyScanStatsEntry_Object = MibTableRow
fgExplicitProxyScanStatsEntry = _FgExplicitProxyScanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1)
)
fgExplicitProxyScanStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgExplicitProxyScanStatsDisp"),
)
if mibBuilder.loadTexts:
    fgExplicitProxyScanStatsEntry.setStatus("current")
_FgExplicitProxyScanStatsDisp_Type = FgScanAvDisposition
_FgExplicitProxyScanStatsDisp_Object = MibTableColumn
fgExplicitProxyScanStatsDisp = _FgExplicitProxyScanStatsDisp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1, 1),
    _FgExplicitProxyScanStatsDisp_Type()
)
fgExplicitProxyScanStatsDisp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgExplicitProxyScanStatsDisp.setStatus("current")
_FgExplicitProxyVirus_Type = Counter32
_FgExplicitProxyVirus_Object = MibTableColumn
fgExplicitProxyVirus = _FgExplicitProxyVirus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1, 2),
    _FgExplicitProxyVirus_Type()
)
fgExplicitProxyVirus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyVirus.setStatus("current")
_FgExplicitProxyBannedWords_Type = Counter32
_FgExplicitProxyBannedWords_Object = MibTableColumn
fgExplicitProxyBannedWords = _FgExplicitProxyBannedWords_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1, 3),
    _FgExplicitProxyBannedWords_Type()
)
fgExplicitProxyBannedWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyBannedWords.setStatus("current")
_FgExplicitProxyPolicy_Type = Counter32
_FgExplicitProxyPolicy_Object = MibTableColumn
fgExplicitProxyPolicy = _FgExplicitProxyPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1, 4),
    _FgExplicitProxyPolicy_Type()
)
fgExplicitProxyPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyPolicy.setStatus("current")
_FgExplicitProxyOversized_Type = Counter32
_FgExplicitProxyOversized_Object = MibTableColumn
fgExplicitProxyOversized = _FgExplicitProxyOversized_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1, 5),
    _FgExplicitProxyOversized_Type()
)
fgExplicitProxyOversized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyOversized.setStatus("current")
_FgExplicitProxyArchNest_Type = Counter32
_FgExplicitProxyArchNest_Object = MibTableColumn
fgExplicitProxyArchNest = _FgExplicitProxyArchNest_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1, 6),
    _FgExplicitProxyArchNest_Type()
)
fgExplicitProxyArchNest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyArchNest.setStatus("current")
_FgExplicitProxyArchSize_Type = Counter32
_FgExplicitProxyArchSize_Object = MibTableColumn
fgExplicitProxyArchSize = _FgExplicitProxyArchSize_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1, 7),
    _FgExplicitProxyArchSize_Type()
)
fgExplicitProxyArchSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyArchSize.setStatus("current")
_FgExplicitProxyArchEncrypted_Type = Counter32
_FgExplicitProxyArchEncrypted_Object = MibTableColumn
fgExplicitProxyArchEncrypted = _FgExplicitProxyArchEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1, 8),
    _FgExplicitProxyArchEncrypted_Type()
)
fgExplicitProxyArchEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyArchEncrypted.setStatus("current")
_FgExplicitProxyArchMultiPart_Type = Counter32
_FgExplicitProxyArchMultiPart_Object = MibTableColumn
fgExplicitProxyArchMultiPart = _FgExplicitProxyArchMultiPart_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1, 9),
    _FgExplicitProxyArchMultiPart_Type()
)
fgExplicitProxyArchMultiPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyArchMultiPart.setStatus("current")
_FgExplicitProxyArchUnsupported_Type = Counter32
_FgExplicitProxyArchUnsupported_Object = MibTableColumn
fgExplicitProxyArchUnsupported = _FgExplicitProxyArchUnsupported_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1, 10),
    _FgExplicitProxyArchUnsupported_Type()
)
fgExplicitProxyArchUnsupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyArchUnsupported.setStatus("current")
_FgExplicitProxyArchBomb_Type = Counter32
_FgExplicitProxyArchBomb_Object = MibTableColumn
fgExplicitProxyArchBomb = _FgExplicitProxyArchBomb_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1, 11),
    _FgExplicitProxyArchBomb_Type()
)
fgExplicitProxyArchBomb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyArchBomb.setStatus("current")
_FgExplicitProxyArchCorrupt_Type = Counter32
_FgExplicitProxyArchCorrupt_Object = MibTableColumn
fgExplicitProxyArchCorrupt = _FgExplicitProxyArchCorrupt_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1, 12),
    _FgExplicitProxyArchCorrupt_Type()
)
fgExplicitProxyArchCorrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyArchCorrupt.setStatus("current")
_FgExplicitProxyScriptStatsTable_Object = MibTable
fgExplicitProxyScriptStatsTable = _FgExplicitProxyScriptStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 4)
)
if mibBuilder.loadTexts:
    fgExplicitProxyScriptStatsTable.setStatus("current")
_FgExplicitProxyScriptStatsEntry_Object = MibTableRow
fgExplicitProxyScriptStatsEntry = _FgExplicitProxyScriptStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 4, 1)
)
fgExplicitProxyScriptStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
)
if mibBuilder.loadTexts:
    fgExplicitProxyScriptStatsEntry.setStatus("current")
_FgExplicitProxyFilteredApplets_Type = Counter32
_FgExplicitProxyFilteredApplets_Object = MibTableColumn
fgExplicitProxyFilteredApplets = _FgExplicitProxyFilteredApplets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 4, 1, 1),
    _FgExplicitProxyFilteredApplets_Type()
)
fgExplicitProxyFilteredApplets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyFilteredApplets.setStatus("current")
_FgExplicitProxyFilteredActiveX_Type = Counter32
_FgExplicitProxyFilteredActiveX_Object = MibTableColumn
fgExplicitProxyFilteredActiveX = _FgExplicitProxyFilteredActiveX_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 4, 1, 2),
    _FgExplicitProxyFilteredActiveX_Type()
)
fgExplicitProxyFilteredActiveX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyFilteredActiveX.setStatus("current")
_FgExplicitProxyFilteredJScript_Type = Counter32
_FgExplicitProxyFilteredJScript_Object = MibTableColumn
fgExplicitProxyFilteredJScript = _FgExplicitProxyFilteredJScript_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 4, 1, 3),
    _FgExplicitProxyFilteredJScript_Type()
)
fgExplicitProxyFilteredJScript.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyFilteredJScript.setStatus("current")
_FgExplicitProxyFilteredJS_Type = Counter32
_FgExplicitProxyFilteredJS_Object = MibTableColumn
fgExplicitProxyFilteredJS = _FgExplicitProxyFilteredJS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 4, 1, 4),
    _FgExplicitProxyFilteredJS_Type()
)
fgExplicitProxyFilteredJS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyFilteredJS.setStatus("current")
_FgExplicitProxyFilteredVBS_Type = Counter32
_FgExplicitProxyFilteredVBS_Object = MibTableColumn
fgExplicitProxyFilteredVBS = _FgExplicitProxyFilteredVBS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 4, 1, 5),
    _FgExplicitProxyFilteredVBS_Type()
)
fgExplicitProxyFilteredVBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyFilteredVBS.setStatus("current")
_FgExplicitProxyFilteredOthScript_Type = Counter32
_FgExplicitProxyFilteredOthScript_Object = MibTableColumn
fgExplicitProxyFilteredOthScript = _FgExplicitProxyFilteredOthScript_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 4, 1, 6),
    _FgExplicitProxyFilteredOthScript_Type()
)
fgExplicitProxyFilteredOthScript.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyFilteredOthScript.setStatus("current")
_FgExplicitProxyFilterStatsTable_Object = MibTable
fgExplicitProxyFilterStatsTable = _FgExplicitProxyFilterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 5)
)
if mibBuilder.loadTexts:
    fgExplicitProxyFilterStatsTable.setStatus("current")
_FgExplicitProxyFilterStatsEntry_Object = MibTableRow
fgExplicitProxyFilterStatsEntry = _FgExplicitProxyFilterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 5, 1)
)
fgExplicitProxyFilterStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
)
if mibBuilder.loadTexts:
    fgExplicitProxyFilterStatsEntry.setStatus("current")
_FgExplicitProxyBlockedDLP_Type = Counter32
_FgExplicitProxyBlockedDLP_Object = MibTableColumn
fgExplicitProxyBlockedDLP = _FgExplicitProxyBlockedDLP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 5, 1, 1),
    _FgExplicitProxyBlockedDLP_Type()
)
fgExplicitProxyBlockedDLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyBlockedDLP.setStatus("current")
_FgExplicitProxyBlockedConType_Type = Counter32
_FgExplicitProxyBlockedConType_Object = MibTableColumn
fgExplicitProxyBlockedConType = _FgExplicitProxyBlockedConType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 5, 1, 2),
    _FgExplicitProxyBlockedConType_Type()
)
fgExplicitProxyBlockedConType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyBlockedConType.setStatus("current")
_FgExplicitProxyExaminedURLs_Type = Counter32
_FgExplicitProxyExaminedURLs_Object = MibTableColumn
fgExplicitProxyExaminedURLs = _FgExplicitProxyExaminedURLs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 5, 1, 3),
    _FgExplicitProxyExaminedURLs_Type()
)
fgExplicitProxyExaminedURLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyExaminedURLs.setStatus("current")
_FgExplicitProxyAllowedURLs_Type = Counter32
_FgExplicitProxyAllowedURLs_Object = MibTableColumn
fgExplicitProxyAllowedURLs = _FgExplicitProxyAllowedURLs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 5, 1, 4),
    _FgExplicitProxyAllowedURLs_Type()
)
fgExplicitProxyAllowedURLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyAllowedURLs.setStatus("current")
_FgExplicitProxyBlockedURLs_Type = Counter32
_FgExplicitProxyBlockedURLs_Object = MibTableColumn
fgExplicitProxyBlockedURLs = _FgExplicitProxyBlockedURLs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 5, 1, 5),
    _FgExplicitProxyBlockedURLs_Type()
)
fgExplicitProxyBlockedURLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyBlockedURLs.setStatus("current")
_FgExplicitProxyLoggedURLs_Type = Counter32
_FgExplicitProxyLoggedURLs_Object = MibTableColumn
fgExplicitProxyLoggedURLs = _FgExplicitProxyLoggedURLs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 5, 1, 6),
    _FgExplicitProxyLoggedURLs_Type()
)
fgExplicitProxyLoggedURLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyLoggedURLs.setStatus("current")
_FgExplicitProxyOverriddenURLs_Type = Counter32
_FgExplicitProxyOverriddenURLs_Object = MibTableColumn
fgExplicitProxyOverriddenURLs = _FgExplicitProxyOverriddenURLs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 5, 1, 7),
    _FgExplicitProxyOverriddenURLs_Type()
)
fgExplicitProxyOverriddenURLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyOverriddenURLs.setStatus("current")
_FgAppWebCache_ObjectIdentity = ObjectIdentity
fgAppWebCache = _FgAppWebCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113)
)
_FgWebCacheInfo_ObjectIdentity = ObjectIdentity
fgWebCacheInfo = _FgWebCacheInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 1)
)
_FgWebCacheRAMLimit_Type = Gauge32
_FgWebCacheRAMLimit_Object = MibScalar
fgWebCacheRAMLimit = _FgWebCacheRAMLimit_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 1, 1),
    _FgWebCacheRAMLimit_Type()
)
fgWebCacheRAMLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWebCacheRAMLimit.setStatus("current")
_FgWebCacheRAMUsage_Type = Gauge32
_FgWebCacheRAMUsage_Object = MibScalar
fgWebCacheRAMUsage = _FgWebCacheRAMUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 1, 2),
    _FgWebCacheRAMUsage_Type()
)
fgWebCacheRAMUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWebCacheRAMUsage.setStatus("current")
_FgWebCacheRAMHits_Type = Gauge32
_FgWebCacheRAMHits_Object = MibScalar
fgWebCacheRAMHits = _FgWebCacheRAMHits_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 1, 3),
    _FgWebCacheRAMHits_Type()
)
fgWebCacheRAMHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWebCacheRAMHits.setStatus("current")
_FgWebCacheRAMMisses_Type = Gauge32
_FgWebCacheRAMMisses_Object = MibScalar
fgWebCacheRAMMisses = _FgWebCacheRAMMisses_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 1, 4),
    _FgWebCacheRAMMisses_Type()
)
fgWebCacheRAMMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWebCacheRAMMisses.setStatus("current")
_FgWebCacheRequests_Type = Gauge32
_FgWebCacheRequests_Object = MibScalar
fgWebCacheRequests = _FgWebCacheRequests_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 1, 5),
    _FgWebCacheRequests_Type()
)
fgWebCacheRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWebCacheRequests.setStatus("current")
_FgWebCacheBypass_Type = Gauge32
_FgWebCacheBypass_Object = MibScalar
fgWebCacheBypass = _FgWebCacheBypass_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 1, 6),
    _FgWebCacheBypass_Type()
)
fgWebCacheBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWebCacheBypass.setStatus("current")
_FgWebCacheUpTime_Type = Counter32
_FgWebCacheUpTime_Object = MibScalar
fgWebCacheUpTime = _FgWebCacheUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 1, 7),
    _FgWebCacheUpTime_Type()
)
fgWebCacheUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWebCacheUpTime.setStatus("current")
_FgWebCacheDiskStatsTable_Object = MibTable
fgWebCacheDiskStatsTable = _FgWebCacheDiskStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 2)
)
if mibBuilder.loadTexts:
    fgWebCacheDiskStatsTable.setStatus("current")
_FgWebCacheDiskStatsEntry_Object = MibTableRow
fgWebCacheDiskStatsEntry = _FgWebCacheDiskStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 2, 1)
)
fgWebCacheDiskStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgWebCacheDisk"),
)
if mibBuilder.loadTexts:
    fgWebCacheDiskStatsEntry.setStatus("current")
_FgWebCacheDisk_Type = Unsigned32
_FgWebCacheDisk_Object = MibTableColumn
fgWebCacheDisk = _FgWebCacheDisk_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 2, 1, 1),
    _FgWebCacheDisk_Type()
)
fgWebCacheDisk.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWebCacheDisk.setStatus("current")
_FgWebCacheDiskLimit_Type = CounterBasedGauge64
_FgWebCacheDiskLimit_Object = MibTableColumn
fgWebCacheDiskLimit = _FgWebCacheDiskLimit_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 2, 1, 2),
    _FgWebCacheDiskLimit_Type()
)
fgWebCacheDiskLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWebCacheDiskLimit.setStatus("current")
_FgWebCacheDiskUsage_Type = CounterBasedGauge64
_FgWebCacheDiskUsage_Object = MibTableColumn
fgWebCacheDiskUsage = _FgWebCacheDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 2, 1, 3),
    _FgWebCacheDiskUsage_Type()
)
fgWebCacheDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWebCacheDiskUsage.setStatus("current")
_FgWebCacheDiskHits_Type = Counter32
_FgWebCacheDiskHits_Object = MibTableColumn
fgWebCacheDiskHits = _FgWebCacheDiskHits_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 2, 1, 4),
    _FgWebCacheDiskHits_Type()
)
fgWebCacheDiskHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWebCacheDiskHits.setStatus("current")
_FgWebCacheDiskMisses_Type = Counter32
_FgWebCacheDiskMisses_Object = MibTableColumn
fgWebCacheDiskMisses = _FgWebCacheDiskMisses_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 2, 1, 5),
    _FgWebCacheDiskMisses_Type()
)
fgWebCacheDiskMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWebCacheDiskMisses.setStatus("current")
_FgAppWanOpt_ObjectIdentity = ObjectIdentity
fgAppWanOpt = _FgAppWanOpt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114)
)
_FgWanOptInfo_ObjectIdentity = ObjectIdentity
fgWanOptInfo = _FgWanOptInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 1)
)
_FgMemCacheLimit_Type = Gauge32
_FgMemCacheLimit_Object = MibScalar
fgMemCacheLimit = _FgMemCacheLimit_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 1, 1),
    _FgMemCacheLimit_Type()
)
fgMemCacheLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMemCacheLimit.setStatus("current")
_FgMemCacheUsage_Type = Gauge32
_FgMemCacheUsage_Object = MibScalar
fgMemCacheUsage = _FgMemCacheUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 1, 2),
    _FgMemCacheUsage_Type()
)
fgMemCacheUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMemCacheUsage.setStatus("current")
_FgMemCacheHits_Type = Gauge32
_FgMemCacheHits_Object = MibScalar
fgMemCacheHits = _FgMemCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 1, 3),
    _FgMemCacheHits_Type()
)
fgMemCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMemCacheHits.setStatus("current")
_FgMemCacheMisses_Type = Gauge32
_FgMemCacheMisses_Object = MibScalar
fgMemCacheMisses = _FgMemCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 1, 4),
    _FgMemCacheMisses_Type()
)
fgMemCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMemCacheMisses.setStatus("current")
_FgByteCacheRAMLimit_Type = Gauge32
_FgByteCacheRAMLimit_Object = MibScalar
fgByteCacheRAMLimit = _FgByteCacheRAMLimit_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 1, 5),
    _FgByteCacheRAMLimit_Type()
)
fgByteCacheRAMLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgByteCacheRAMLimit.setStatus("current")
_FgByteCacheRAMUsage_Type = Gauge32
_FgByteCacheRAMUsage_Object = MibScalar
fgByteCacheRAMUsage = _FgByteCacheRAMUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 1, 6),
    _FgByteCacheRAMUsage_Type()
)
fgByteCacheRAMUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgByteCacheRAMUsage.setStatus("current")
_FgWanOptUpTime_Type = Counter32
_FgWanOptUpTime_Object = MibScalar
fgWanOptUpTime = _FgWanOptUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 1, 7),
    _FgWanOptUpTime_Type()
)
fgWanOptUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptUpTime.setStatus("current")
_FgWanOptStatsTable_Object = MibTable
fgWanOptStatsTable = _FgWanOptStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 2)
)
if mibBuilder.loadTexts:
    fgWanOptStatsTable.setStatus("current")
_FgWanOptStatsEntry_Object = MibTableRow
fgWanOptStatsEntry = _FgWanOptStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 2, 1)
)
fgWanOptStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
)
if mibBuilder.loadTexts:
    fgWanOptStatsEntry.setStatus("current")
_FgWanOptTunnels_Type = Gauge32
_FgWanOptTunnels_Object = MibTableColumn
fgWanOptTunnels = _FgWanOptTunnels_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 2, 1, 1),
    _FgWanOptTunnels_Type()
)
fgWanOptTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptTunnels.setStatus("current")
_FgWanOptLANBytesIn_Type = Gauge32
_FgWanOptLANBytesIn_Object = MibTableColumn
fgWanOptLANBytesIn = _FgWanOptLANBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 2, 1, 2),
    _FgWanOptLANBytesIn_Type()
)
fgWanOptLANBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptLANBytesIn.setStatus("current")
_FgWanOptLANBytesOut_Type = Gauge32
_FgWanOptLANBytesOut_Object = MibTableColumn
fgWanOptLANBytesOut = _FgWanOptLANBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 2, 1, 3),
    _FgWanOptLANBytesOut_Type()
)
fgWanOptLANBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptLANBytesOut.setStatus("current")
_FgWanOptWANBytesIn_Type = Gauge32
_FgWanOptWANBytesIn_Object = MibTableColumn
fgWanOptWANBytesIn = _FgWanOptWANBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 2, 1, 4),
    _FgWanOptWANBytesIn_Type()
)
fgWanOptWANBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptWANBytesIn.setStatus("current")
_FgWanOptWANBytesOut_Type = Gauge32
_FgWanOptWANBytesOut_Object = MibTableColumn
fgWanOptWANBytesOut = _FgWanOptWANBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 2, 1, 5),
    _FgWanOptWANBytesOut_Type()
)
fgWanOptWANBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptWANBytesOut.setStatus("current")
_FgWanOptHistoryStatsTable_Object = MibTable
fgWanOptHistoryStatsTable = _FgWanOptHistoryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 3)
)
if mibBuilder.loadTexts:
    fgWanOptHistoryStatsTable.setStatus("current")
_FgWanOptHistoryStatsEntry_Object = MibTableRow
fgWanOptHistoryStatsEntry = _FgWanOptHistoryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 3, 1)
)
fgWanOptHistoryStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWanOptHistPeriod"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWanOptProtocol"),
)
if mibBuilder.loadTexts:
    fgWanOptHistoryStatsEntry.setStatus("current")
_FgWanOptHistPeriod_Type = FgWanOptHistPeriods
_FgWanOptHistPeriod_Object = MibTableColumn
fgWanOptHistPeriod = _FgWanOptHistPeriod_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 3, 1, 1),
    _FgWanOptHistPeriod_Type()
)
fgWanOptHistPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWanOptHistPeriod.setStatus("current")
_FgWanOptProtocol_Type = FgWanOptProtocols
_FgWanOptProtocol_Object = MibTableColumn
fgWanOptProtocol = _FgWanOptProtocol_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 3, 1, 2),
    _FgWanOptProtocol_Type()
)
fgWanOptProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWanOptProtocol.setStatus("current")


class _FgWanOptReductionRate_Type(Gauge32):
    """Custom type fgWanOptReductionRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgWanOptReductionRate_Type.__name__ = "Gauge32"
_FgWanOptReductionRate_Object = MibTableColumn
fgWanOptReductionRate = _FgWanOptReductionRate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 3, 1, 3),
    _FgWanOptReductionRate_Type()
)
fgWanOptReductionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptReductionRate.setStatus("current")
_FgWanOptLanTraffic_Type = CounterBasedGauge64
_FgWanOptLanTraffic_Object = MibTableColumn
fgWanOptLanTraffic = _FgWanOptLanTraffic_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 3, 1, 4),
    _FgWanOptLanTraffic_Type()
)
fgWanOptLanTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptLanTraffic.setStatus("current")
_FgWanOptWanTraffic_Type = CounterBasedGauge64
_FgWanOptWanTraffic_Object = MibTableColumn
fgWanOptWanTraffic = _FgWanOptWanTraffic_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 3, 1, 5),
    _FgWanOptWanTraffic_Type()
)
fgWanOptWanTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptWanTraffic.setStatus("current")
_FgWanOptTrafficStatsTable_Object = MibTable
fgWanOptTrafficStatsTable = _FgWanOptTrafficStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 4)
)
if mibBuilder.loadTexts:
    fgWanOptTrafficStatsTable.setStatus("current")
_FgWanOptTrafficStatsEntry_Object = MibTableRow
fgWanOptTrafficStatsEntry = _FgWanOptTrafficStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 4, 1)
)
fgWanOptTrafficStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWanOptProtocol"),
)
if mibBuilder.loadTexts:
    fgWanOptTrafficStatsEntry.setStatus("current")
_FgWanOptLanInTraffic_Type = Counter64
_FgWanOptLanInTraffic_Object = MibTableColumn
fgWanOptLanInTraffic = _FgWanOptLanInTraffic_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 4, 1, 1),
    _FgWanOptLanInTraffic_Type()
)
fgWanOptLanInTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptLanInTraffic.setStatus("current")
_FgWanOptLanOutTraffic_Type = Counter64
_FgWanOptLanOutTraffic_Object = MibTableColumn
fgWanOptLanOutTraffic = _FgWanOptLanOutTraffic_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 4, 1, 2),
    _FgWanOptLanOutTraffic_Type()
)
fgWanOptLanOutTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptLanOutTraffic.setStatus("current")
_FgWanOptWanInTraffic_Type = Counter64
_FgWanOptWanInTraffic_Object = MibTableColumn
fgWanOptWanInTraffic = _FgWanOptWanInTraffic_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 4, 1, 3),
    _FgWanOptWanInTraffic_Type()
)
fgWanOptWanInTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptWanInTraffic.setStatus("current")
_FgWanOptWanOutTraffic_Type = Counter64
_FgWanOptWanOutTraffic_Object = MibTableColumn
fgWanOptWanOutTraffic = _FgWanOptWanOutTraffic_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 4, 1, 4),
    _FgWanOptWanOutTraffic_Type()
)
fgWanOptWanOutTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptWanOutTraffic.setStatus("current")
_FgWanOptDiskStatsTable_Object = MibTable
fgWanOptDiskStatsTable = _FgWanOptDiskStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 5)
)
if mibBuilder.loadTexts:
    fgWanOptDiskStatsTable.setStatus("current")
_FgWanOptDiskStatsEntry_Object = MibTableRow
fgWanOptDiskStatsEntry = _FgWanOptDiskStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 5, 1)
)
fgWanOptDiskStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgWanOptDisk"),
)
if mibBuilder.loadTexts:
    fgWanOptDiskStatsEntry.setStatus("current")
_FgWanOptDisk_Type = Unsigned32
_FgWanOptDisk_Object = MibTableColumn
fgWanOptDisk = _FgWanOptDisk_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 5, 1, 1),
    _FgWanOptDisk_Type()
)
fgWanOptDisk.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWanOptDisk.setStatus("current")
_FgWanOptDiskLimit_Type = CounterBasedGauge64
_FgWanOptDiskLimit_Object = MibTableColumn
fgWanOptDiskLimit = _FgWanOptDiskLimit_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 5, 1, 2),
    _FgWanOptDiskLimit_Type()
)
fgWanOptDiskLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptDiskLimit.setStatus("current")
_FgWanOptDiskUsage_Type = CounterBasedGauge64
_FgWanOptDiskUsage_Object = MibTableColumn
fgWanOptDiskUsage = _FgWanOptDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 5, 1, 3),
    _FgWanOptDiskUsage_Type()
)
fgWanOptDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptDiskUsage.setStatus("current")
_FgWanOptDiskHits_Type = Counter32
_FgWanOptDiskHits_Object = MibTableColumn
fgWanOptDiskHits = _FgWanOptDiskHits_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 5, 1, 4),
    _FgWanOptDiskHits_Type()
)
fgWanOptDiskHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptDiskHits.setStatus("current")
_FgWanOptDiskMisses_Type = Counter32
_FgWanOptDiskMisses_Object = MibTableColumn
fgWanOptDiskMisses = _FgWanOptDiskMisses_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 5, 1, 5),
    _FgWanOptDiskMisses_Type()
)
fgWanOptDiskMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptDiskMisses.setStatus("current")
_FgInetProto_ObjectIdentity = ObjectIdentity
fgInetProto = _FgInetProto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11)
)
_FgInetProtoInfo_ObjectIdentity = ObjectIdentity
fgInetProtoInfo = _FgInetProtoInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 1)
)
_FgInetProtoTables_ObjectIdentity = ObjectIdentity
fgInetProtoTables = _FgInetProtoTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2)
)
_FgIpSessTable_Object = MibTable
fgIpSessTable = _FgIpSessTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 1)
)
if mibBuilder.loadTexts:
    fgIpSessTable.setStatus("current")
_FgIpSessEntry_Object = MibTableRow
fgIpSessEntry = _FgIpSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 1, 1)
)
fgIpSessEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgIpSessIndex"),
)
if mibBuilder.loadTexts:
    fgIpSessEntry.setStatus("current")
_FgIpSessIndex_Type = FnIndex
_FgIpSessIndex_Object = MibTableColumn
fgIpSessIndex = _FgIpSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 1, 1, 1),
    _FgIpSessIndex_Type()
)
fgIpSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgIpSessIndex.setStatus("current")
_FgIpSessProto_Type = FgSessProto
_FgIpSessProto_Object = MibTableColumn
fgIpSessProto = _FgIpSessProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 1, 1, 2),
    _FgIpSessProto_Type()
)
fgIpSessProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpSessProto.setStatus("current")
_FgIpSessFromAddr_Type = IpAddress
_FgIpSessFromAddr_Object = MibTableColumn
fgIpSessFromAddr = _FgIpSessFromAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 1, 1, 3),
    _FgIpSessFromAddr_Type()
)
fgIpSessFromAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpSessFromAddr.setStatus("current")
_FgIpSessFromPort_Type = InetPortNumber
_FgIpSessFromPort_Object = MibTableColumn
fgIpSessFromPort = _FgIpSessFromPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 1, 1, 4),
    _FgIpSessFromPort_Type()
)
fgIpSessFromPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpSessFromPort.setStatus("current")
_FgIpSessToAddr_Type = IpAddress
_FgIpSessToAddr_Object = MibTableColumn
fgIpSessToAddr = _FgIpSessToAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 1, 1, 5),
    _FgIpSessToAddr_Type()
)
fgIpSessToAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpSessToAddr.setStatus("current")
_FgIpSessToPort_Type = InetPortNumber
_FgIpSessToPort_Object = MibTableColumn
fgIpSessToPort = _FgIpSessToPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 1, 1, 6),
    _FgIpSessToPort_Type()
)
fgIpSessToPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpSessToPort.setStatus("current")
_FgIpSessExp_Type = Gauge32
_FgIpSessExp_Object = MibTableColumn
fgIpSessExp = _FgIpSessExp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 1, 1, 7),
    _FgIpSessExp_Type()
)
fgIpSessExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpSessExp.setStatus("current")
_FgIpSessVdom_Type = FgVdIndex
_FgIpSessVdom_Object = MibTableColumn
fgIpSessVdom = _FgIpSessVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 1, 1, 8),
    _FgIpSessVdom_Type()
)
fgIpSessVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpSessVdom.setStatus("current")
_FgIpSessStatsTable_Object = MibTable
fgIpSessStatsTable = _FgIpSessStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 2)
)
if mibBuilder.loadTexts:
    fgIpSessStatsTable.setStatus("current")
_FgIpSessStatsEntry_Object = MibTableRow
fgIpSessStatsEntry = _FgIpSessStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fgIpSessStatsEntry.setStatus("current")
_FgIpSessNumber_Type = Gauge32
_FgIpSessNumber_Object = MibTableColumn
fgIpSessNumber = _FgIpSessNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 2, 1, 1),
    _FgIpSessNumber_Type()
)
fgIpSessNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpSessNumber.setStatus("current")
_FgIp6SessStatsTable_Object = MibTable
fgIp6SessStatsTable = _FgIp6SessStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 3)
)
if mibBuilder.loadTexts:
    fgIp6SessStatsTable.setStatus("current")
_FgIp6SessStatsEntry_Object = MibTableRow
fgIp6SessStatsEntry = _FgIp6SessStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 3, 1)
)
if mibBuilder.loadTexts:
    fgIp6SessStatsEntry.setStatus("current")
_FgIp6SessNumber_Type = Gauge32
_FgIp6SessNumber_Object = MibTableColumn
fgIp6SessNumber = _FgIp6SessNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 3, 1, 1),
    _FgIp6SessNumber_Type()
)
fgIp6SessNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIp6SessNumber.setStatus("current")
_FgVpn_ObjectIdentity = ObjectIdentity
fgVpn = _FgVpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12)
)
_FgVpnInfo_ObjectIdentity = ObjectIdentity
fgVpnInfo = _FgVpnInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 1)
)
_FgVpnTunnelUpCount_Type = Integer32
_FgVpnTunnelUpCount_Object = MibScalar
fgVpnTunnelUpCount = _FgVpnTunnelUpCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 1, 1),
    _FgVpnTunnelUpCount_Type()
)
fgVpnTunnelUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunnelUpCount.setStatus("current")
_FgVpnTables_ObjectIdentity = ObjectIdentity
fgVpnTables = _FgVpnTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2)
)
_FgVpnDialupTable_Object = MibTable
fgVpnDialupTable = _FgVpnDialupTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 1)
)
if mibBuilder.loadTexts:
    fgVpnDialupTable.setStatus("current")
_FgVpnDialupEntry_Object = MibTableRow
fgVpnDialupEntry = _FgVpnDialupEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 1, 1)
)
fgVpnDialupEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVpnDialupIndex"),
)
if mibBuilder.loadTexts:
    fgVpnDialupEntry.setStatus("current")
_FgVpnDialupIndex_Type = FnIndex
_FgVpnDialupIndex_Object = MibTableColumn
fgVpnDialupIndex = _FgVpnDialupIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 1, 1, 1),
    _FgVpnDialupIndex_Type()
)
fgVpnDialupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgVpnDialupIndex.setStatus("current")
_FgVpnDialupGateway_Type = IpAddress
_FgVpnDialupGateway_Object = MibTableColumn
fgVpnDialupGateway = _FgVpnDialupGateway_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 1, 1, 2),
    _FgVpnDialupGateway_Type()
)
fgVpnDialupGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnDialupGateway.setStatus("current")
_FgVpnDialupLifetime_Type = Integer32
_FgVpnDialupLifetime_Object = MibTableColumn
fgVpnDialupLifetime = _FgVpnDialupLifetime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 1, 1, 3),
    _FgVpnDialupLifetime_Type()
)
fgVpnDialupLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnDialupLifetime.setStatus("current")
_FgVpnDialupTimeout_Type = Integer32
_FgVpnDialupTimeout_Object = MibTableColumn
fgVpnDialupTimeout = _FgVpnDialupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 1, 1, 4),
    _FgVpnDialupTimeout_Type()
)
fgVpnDialupTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnDialupTimeout.setStatus("current")
_FgVpnDialupSrcBegin_Type = IpAddress
_FgVpnDialupSrcBegin_Object = MibTableColumn
fgVpnDialupSrcBegin = _FgVpnDialupSrcBegin_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 1, 1, 5),
    _FgVpnDialupSrcBegin_Type()
)
fgVpnDialupSrcBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnDialupSrcBegin.setStatus("current")
_FgVpnDialupSrcEnd_Type = IpAddress
_FgVpnDialupSrcEnd_Object = MibTableColumn
fgVpnDialupSrcEnd = _FgVpnDialupSrcEnd_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 1, 1, 6),
    _FgVpnDialupSrcEnd_Type()
)
fgVpnDialupSrcEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnDialupSrcEnd.setStatus("current")
_FgVpnDialupDstAddr_Type = IpAddress
_FgVpnDialupDstAddr_Object = MibTableColumn
fgVpnDialupDstAddr = _FgVpnDialupDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 1, 1, 7),
    _FgVpnDialupDstAddr_Type()
)
fgVpnDialupDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnDialupDstAddr.setStatus("current")
_FgVpnDialupVdom_Type = FgVdIndex
_FgVpnDialupVdom_Object = MibTableColumn
fgVpnDialupVdom = _FgVpnDialupVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 1, 1, 8),
    _FgVpnDialupVdom_Type()
)
fgVpnDialupVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnDialupVdom.setStatus("current")
_FgVpnDialupInOctets_Type = Counter64
_FgVpnDialupInOctets_Object = MibTableColumn
fgVpnDialupInOctets = _FgVpnDialupInOctets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 1, 1, 9),
    _FgVpnDialupInOctets_Type()
)
fgVpnDialupInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnDialupInOctets.setStatus("current")
_FgVpnDialupOutOctets_Type = Counter64
_FgVpnDialupOutOctets_Object = MibTableColumn
fgVpnDialupOutOctets = _FgVpnDialupOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 1, 1, 10),
    _FgVpnDialupOutOctets_Type()
)
fgVpnDialupOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnDialupOutOctets.setStatus("current")
_FgVpnTunTable_Object = MibTable
fgVpnTunTable = _FgVpnTunTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2)
)
if mibBuilder.loadTexts:
    fgVpnTunTable.setStatus("current")
_FgVpnTunEntry_Object = MibTableRow
fgVpnTunEntry = _FgVpnTunEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1)
)
fgVpnTunEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVpnTunEntIndex"),
)
if mibBuilder.loadTexts:
    fgVpnTunEntry.setStatus("current")
_FgVpnTunEntIndex_Type = FnIndex
_FgVpnTunEntIndex_Object = MibTableColumn
fgVpnTunEntIndex = _FgVpnTunEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 1),
    _FgVpnTunEntIndex_Type()
)
fgVpnTunEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgVpnTunEntIndex.setStatus("current")
_FgVpnTunEntPhase1Name_Type = DisplayString
_FgVpnTunEntPhase1Name_Object = MibTableColumn
fgVpnTunEntPhase1Name = _FgVpnTunEntPhase1Name_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 2),
    _FgVpnTunEntPhase1Name_Type()
)
fgVpnTunEntPhase1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntPhase1Name.setStatus("current")
_FgVpnTunEntPhase2Name_Type = DisplayString
_FgVpnTunEntPhase2Name_Object = MibTableColumn
fgVpnTunEntPhase2Name = _FgVpnTunEntPhase2Name_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 3),
    _FgVpnTunEntPhase2Name_Type()
)
fgVpnTunEntPhase2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntPhase2Name.setStatus("current")
_FgVpnTunEntRemGwyIp_Type = IpAddress
_FgVpnTunEntRemGwyIp_Object = MibTableColumn
fgVpnTunEntRemGwyIp = _FgVpnTunEntRemGwyIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 4),
    _FgVpnTunEntRemGwyIp_Type()
)
fgVpnTunEntRemGwyIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntRemGwyIp.setStatus("current")
_FgVpnTunEntRemGwyPort_Type = InetPortNumber
_FgVpnTunEntRemGwyPort_Object = MibTableColumn
fgVpnTunEntRemGwyPort = _FgVpnTunEntRemGwyPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 5),
    _FgVpnTunEntRemGwyPort_Type()
)
fgVpnTunEntRemGwyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntRemGwyPort.setStatus("current")
_FgVpnTunEntLocGwyIp_Type = IpAddress
_FgVpnTunEntLocGwyIp_Object = MibTableColumn
fgVpnTunEntLocGwyIp = _FgVpnTunEntLocGwyIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 6),
    _FgVpnTunEntLocGwyIp_Type()
)
fgVpnTunEntLocGwyIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntLocGwyIp.setStatus("current")
_FgVpnTunEntLocGwyPort_Type = InetPortNumber
_FgVpnTunEntLocGwyPort_Object = MibTableColumn
fgVpnTunEntLocGwyPort = _FgVpnTunEntLocGwyPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 7),
    _FgVpnTunEntLocGwyPort_Type()
)
fgVpnTunEntLocGwyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntLocGwyPort.setStatus("current")
_FgVpnTunEntSelectorSrcBeginIp_Type = IpAddress
_FgVpnTunEntSelectorSrcBeginIp_Object = MibTableColumn
fgVpnTunEntSelectorSrcBeginIp = _FgVpnTunEntSelectorSrcBeginIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 8),
    _FgVpnTunEntSelectorSrcBeginIp_Type()
)
fgVpnTunEntSelectorSrcBeginIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntSelectorSrcBeginIp.setStatus("current")
_FgVpnTunEntSelectorSrcEndIp_Type = IpAddress
_FgVpnTunEntSelectorSrcEndIp_Object = MibTableColumn
fgVpnTunEntSelectorSrcEndIp = _FgVpnTunEntSelectorSrcEndIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 9),
    _FgVpnTunEntSelectorSrcEndIp_Type()
)
fgVpnTunEntSelectorSrcEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntSelectorSrcEndIp.setStatus("current")
_FgVpnTunEntSelectorSrcPort_Type = InetPortNumber
_FgVpnTunEntSelectorSrcPort_Object = MibTableColumn
fgVpnTunEntSelectorSrcPort = _FgVpnTunEntSelectorSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 10),
    _FgVpnTunEntSelectorSrcPort_Type()
)
fgVpnTunEntSelectorSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntSelectorSrcPort.setStatus("current")
_FgVpnTunEntSelectorDstBeginIp_Type = IpAddress
_FgVpnTunEntSelectorDstBeginIp_Object = MibTableColumn
fgVpnTunEntSelectorDstBeginIp = _FgVpnTunEntSelectorDstBeginIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 11),
    _FgVpnTunEntSelectorDstBeginIp_Type()
)
fgVpnTunEntSelectorDstBeginIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntSelectorDstBeginIp.setStatus("current")
_FgVpnTunEntSelectorDstEndIp_Type = IpAddress
_FgVpnTunEntSelectorDstEndIp_Object = MibTableColumn
fgVpnTunEntSelectorDstEndIp = _FgVpnTunEntSelectorDstEndIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 12),
    _FgVpnTunEntSelectorDstEndIp_Type()
)
fgVpnTunEntSelectorDstEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntSelectorDstEndIp.setStatus("current")
_FgVpnTunEntSelectorDstPort_Type = InetPortNumber
_FgVpnTunEntSelectorDstPort_Object = MibTableColumn
fgVpnTunEntSelectorDstPort = _FgVpnTunEntSelectorDstPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 13),
    _FgVpnTunEntSelectorDstPort_Type()
)
fgVpnTunEntSelectorDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntSelectorDstPort.setStatus("current")
_FgVpnTunEntSelectorProto_Type = Integer32
_FgVpnTunEntSelectorProto_Object = MibTableColumn
fgVpnTunEntSelectorProto = _FgVpnTunEntSelectorProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 14),
    _FgVpnTunEntSelectorProto_Type()
)
fgVpnTunEntSelectorProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntSelectorProto.setStatus("current")
_FgVpnTunEntLifeSecs_Type = Gauge32
_FgVpnTunEntLifeSecs_Object = MibTableColumn
fgVpnTunEntLifeSecs = _FgVpnTunEntLifeSecs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 15),
    _FgVpnTunEntLifeSecs_Type()
)
fgVpnTunEntLifeSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntLifeSecs.setStatus("current")
_FgVpnTunEntLifeBytes_Type = Gauge32
_FgVpnTunEntLifeBytes_Object = MibTableColumn
fgVpnTunEntLifeBytes = _FgVpnTunEntLifeBytes_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 16),
    _FgVpnTunEntLifeBytes_Type()
)
fgVpnTunEntLifeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntLifeBytes.setStatus("current")
_FgVpnTunEntTimeout_Type = Gauge32
_FgVpnTunEntTimeout_Object = MibTableColumn
fgVpnTunEntTimeout = _FgVpnTunEntTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 17),
    _FgVpnTunEntTimeout_Type()
)
fgVpnTunEntTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntTimeout.setStatus("current")
_FgVpnTunEntInOctets_Type = Counter64
_FgVpnTunEntInOctets_Object = MibTableColumn
fgVpnTunEntInOctets = _FgVpnTunEntInOctets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 18),
    _FgVpnTunEntInOctets_Type()
)
fgVpnTunEntInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntInOctets.setStatus("current")
_FgVpnTunEntOutOctets_Type = Counter64
_FgVpnTunEntOutOctets_Object = MibTableColumn
fgVpnTunEntOutOctets = _FgVpnTunEntOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 19),
    _FgVpnTunEntOutOctets_Type()
)
fgVpnTunEntOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntOutOctets.setStatus("current")


class _FgVpnTunEntStatus_Type(Integer32):
    """Custom type fgVpnTunEntStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_FgVpnTunEntStatus_Type.__name__ = "Integer32"
_FgVpnTunEntStatus_Object = MibTableColumn
fgVpnTunEntStatus = _FgVpnTunEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 20),
    _FgVpnTunEntStatus_Type()
)
fgVpnTunEntStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntStatus.setStatus("current")
_FgVpnTunEntVdom_Type = FgVdIndex
_FgVpnTunEntVdom_Object = MibTableColumn
fgVpnTunEntVdom = _FgVpnTunEntVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 21),
    _FgVpnTunEntVdom_Type()
)
fgVpnTunEntVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntVdom.setStatus("current")
_FgVpnSslStatsTable_Object = MibTable
fgVpnSslStatsTable = _FgVpnSslStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 3)
)
if mibBuilder.loadTexts:
    fgVpnSslStatsTable.setStatus("current")
_FgVpnSslStatsEntry_Object = MibTableRow
fgVpnSslStatsEntry = _FgVpnSslStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 3, 1)
)
if mibBuilder.loadTexts:
    fgVpnSslStatsEntry.setStatus("current")
_FgVpnSslState_Type = FnBoolState
_FgVpnSslState_Object = MibTableColumn
fgVpnSslState = _FgVpnSslState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 3, 1, 1),
    _FgVpnSslState_Type()
)
fgVpnSslState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslState.setStatus("current")
_FgVpnSslStatsLoginUsers_Type = Gauge32
_FgVpnSslStatsLoginUsers_Object = MibTableColumn
fgVpnSslStatsLoginUsers = _FgVpnSslStatsLoginUsers_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 3, 1, 2),
    _FgVpnSslStatsLoginUsers_Type()
)
fgVpnSslStatsLoginUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslStatsLoginUsers.setStatus("current")
_FgVpnSslStatsMaxUsers_Type = Counter32
_FgVpnSslStatsMaxUsers_Object = MibTableColumn
fgVpnSslStatsMaxUsers = _FgVpnSslStatsMaxUsers_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 3, 1, 3),
    _FgVpnSslStatsMaxUsers_Type()
)
fgVpnSslStatsMaxUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslStatsMaxUsers.setStatus("current")
_FgVpnSslStatsActiveWebSessions_Type = Gauge32
_FgVpnSslStatsActiveWebSessions_Object = MibTableColumn
fgVpnSslStatsActiveWebSessions = _FgVpnSslStatsActiveWebSessions_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 3, 1, 4),
    _FgVpnSslStatsActiveWebSessions_Type()
)
fgVpnSslStatsActiveWebSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslStatsActiveWebSessions.setStatus("current")
_FgVpnSslStatsMaxWebSessions_Type = Counter32
_FgVpnSslStatsMaxWebSessions_Object = MibTableColumn
fgVpnSslStatsMaxWebSessions = _FgVpnSslStatsMaxWebSessions_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 3, 1, 5),
    _FgVpnSslStatsMaxWebSessions_Type()
)
fgVpnSslStatsMaxWebSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslStatsMaxWebSessions.setStatus("current")
_FgVpnSslStatsActiveTunnels_Type = Gauge32
_FgVpnSslStatsActiveTunnels_Object = MibTableColumn
fgVpnSslStatsActiveTunnels = _FgVpnSslStatsActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 3, 1, 6),
    _FgVpnSslStatsActiveTunnels_Type()
)
fgVpnSslStatsActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslStatsActiveTunnels.setStatus("current")
_FgVpnSslStatsMaxTunnels_Type = Counter32
_FgVpnSslStatsMaxTunnels_Object = MibTableColumn
fgVpnSslStatsMaxTunnels = _FgVpnSslStatsMaxTunnels_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 3, 1, 7),
    _FgVpnSslStatsMaxTunnels_Type()
)
fgVpnSslStatsMaxTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslStatsMaxTunnels.setStatus("current")
_FgVpnSslTunnelTable_Object = MibTable
fgVpnSslTunnelTable = _FgVpnSslTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 4)
)
if mibBuilder.loadTexts:
    fgVpnSslTunnelTable.setStatus("current")
_FgVpnSslTunnelEntry_Object = MibTableRow
fgVpnSslTunnelEntry = _FgVpnSslTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 4, 1)
)
fgVpnSslTunnelEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVpnSslTunnelIndex"),
)
if mibBuilder.loadTexts:
    fgVpnSslTunnelEntry.setStatus("current")
_FgVpnSslTunnelIndex_Type = FnIndex
_FgVpnSslTunnelIndex_Object = MibTableColumn
fgVpnSslTunnelIndex = _FgVpnSslTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 4, 1, 1),
    _FgVpnSslTunnelIndex_Type()
)
fgVpnSslTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgVpnSslTunnelIndex.setStatus("current")
_FgVpnSslTunnelVdom_Type = FgVdIndex
_FgVpnSslTunnelVdom_Object = MibTableColumn
fgVpnSslTunnelVdom = _FgVpnSslTunnelVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 4, 1, 2),
    _FgVpnSslTunnelVdom_Type()
)
fgVpnSslTunnelVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslTunnelVdom.setStatus("current")
_FgVpnSslTunnelUserName_Type = DisplayString
_FgVpnSslTunnelUserName_Object = MibTableColumn
fgVpnSslTunnelUserName = _FgVpnSslTunnelUserName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 4, 1, 3),
    _FgVpnSslTunnelUserName_Type()
)
fgVpnSslTunnelUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslTunnelUserName.setStatus("current")
_FgVpnSslTunnelSrcIp_Type = IpAddress
_FgVpnSslTunnelSrcIp_Object = MibTableColumn
fgVpnSslTunnelSrcIp = _FgVpnSslTunnelSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 4, 1, 4),
    _FgVpnSslTunnelSrcIp_Type()
)
fgVpnSslTunnelSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslTunnelSrcIp.setStatus("current")
_FgVpnSslTunnelIp_Type = IpAddress
_FgVpnSslTunnelIp_Object = MibTableColumn
fgVpnSslTunnelIp = _FgVpnSslTunnelIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 4, 1, 5),
    _FgVpnSslTunnelIp_Type()
)
fgVpnSslTunnelIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslTunnelIp.setStatus("current")
_FgVpnSslTunnelUpTime_Type = Counter32
_FgVpnSslTunnelUpTime_Object = MibTableColumn
fgVpnSslTunnelUpTime = _FgVpnSslTunnelUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 4, 1, 6),
    _FgVpnSslTunnelUpTime_Type()
)
fgVpnSslTunnelUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslTunnelUpTime.setStatus("current")
_FgVpnSslTunnelBytesIn_Type = Counter64
_FgVpnSslTunnelBytesIn_Object = MibTableColumn
fgVpnSslTunnelBytesIn = _FgVpnSslTunnelBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 4, 1, 7),
    _FgVpnSslTunnelBytesIn_Type()
)
fgVpnSslTunnelBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslTunnelBytesIn.setStatus("current")
_FgVpnSslTunnelBytesOut_Type = Counter64
_FgVpnSslTunnelBytesOut_Object = MibTableColumn
fgVpnSslTunnelBytesOut = _FgVpnSslTunnelBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 4, 1, 8),
    _FgVpnSslTunnelBytesOut_Type()
)
fgVpnSslTunnelBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslTunnelBytesOut.setStatus("current")
_FgVpnTrapObjects_ObjectIdentity = ObjectIdentity
fgVpnTrapObjects = _FgVpnTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 3)
)
_FgVpnTrapLocalGateway_Type = IpAddress
_FgVpnTrapLocalGateway_Object = MibScalar
fgVpnTrapLocalGateway = _FgVpnTrapLocalGateway_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 3, 2),
    _FgVpnTrapLocalGateway_Type()
)
fgVpnTrapLocalGateway.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgVpnTrapLocalGateway.setStatus("current")
_FgVpnTrapRemoteGateway_Type = IpAddress
_FgVpnTrapRemoteGateway_Object = MibScalar
fgVpnTrapRemoteGateway = _FgVpnTrapRemoteGateway_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 3, 3),
    _FgVpnTrapRemoteGateway_Type()
)
fgVpnTrapRemoteGateway.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgVpnTrapRemoteGateway.setStatus("current")
_FgVpnTrapPhase1Name_Type = DisplayString
_FgVpnTrapPhase1Name_Object = MibScalar
fgVpnTrapPhase1Name = _FgVpnTrapPhase1Name_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 3, 4),
    _FgVpnTrapPhase1Name_Type()
)
fgVpnTrapPhase1Name.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgVpnTrapPhase1Name.setStatus("current")
_FgHighAvailability_ObjectIdentity = ObjectIdentity
fgHighAvailability = _FgHighAvailability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13)
)
_FgHaInfo_ObjectIdentity = ObjectIdentity
fgHaInfo = _FgHaInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 1)
)
_FgHaSystemMode_Type = FgHaMode
_FgHaSystemMode_Object = MibScalar
fgHaSystemMode = _FgHaSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 1, 1),
    _FgHaSystemMode_Type()
)
fgHaSystemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaSystemMode.setStatus("current")
_FgHaGroupId_Type = FnIndex
_FgHaGroupId_Object = MibScalar
fgHaGroupId = _FgHaGroupId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 1, 2),
    _FgHaGroupId_Type()
)
fgHaGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaGroupId.setStatus("current")


class _FgHaPriority_Type(Integer32):
    """Custom type fgHaPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FgHaPriority_Type.__name__ = "Integer32"
_FgHaPriority_Object = MibScalar
fgHaPriority = _FgHaPriority_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 1, 3),
    _FgHaPriority_Type()
)
fgHaPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaPriority.setStatus("current")
_FgHaOverride_Type = FnBoolState
_FgHaOverride_Object = MibScalar
fgHaOverride = _FgHaOverride_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 1, 4),
    _FgHaOverride_Type()
)
fgHaOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaOverride.setStatus("current")
_FgHaAutoSync_Type = FnBoolState
_FgHaAutoSync_Object = MibScalar
fgHaAutoSync = _FgHaAutoSync_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 1, 5),
    _FgHaAutoSync_Type()
)
fgHaAutoSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaAutoSync.setStatus("current")
_FgHaSchedule_Type = FgHaLBSchedule
_FgHaSchedule_Object = MibScalar
fgHaSchedule = _FgHaSchedule_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 1, 6),
    _FgHaSchedule_Type()
)
fgHaSchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaSchedule.setStatus("current")
_FgHaGroupName_Type = DisplayString
_FgHaGroupName_Object = MibScalar
fgHaGroupName = _FgHaGroupName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 1, 7),
    _FgHaGroupName_Type()
)
fgHaGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaGroupName.setStatus("current")
_FgHaTables_ObjectIdentity = ObjectIdentity
fgHaTables = _FgHaTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2)
)
_FgHaStatsTable_Object = MibTable
fgHaStatsTable = _FgHaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1)
)
if mibBuilder.loadTexts:
    fgHaStatsTable.setStatus("current")
_FgHaStatsEntry_Object = MibTableRow
fgHaStatsEntry = _FgHaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1)
)
fgHaStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgHaStatsIndex"),
)
if mibBuilder.loadTexts:
    fgHaStatsEntry.setStatus("current")
_FgHaStatsIndex_Type = FnIndex
_FgHaStatsIndex_Object = MibTableColumn
fgHaStatsIndex = _FgHaStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 1),
    _FgHaStatsIndex_Type()
)
fgHaStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgHaStatsIndex.setStatus("current")


class _FgHaStatsSerial_Type(DisplayString):
    """Custom type fgHaStatsSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgHaStatsSerial_Type.__name__ = "DisplayString"
_FgHaStatsSerial_Object = MibTableColumn
fgHaStatsSerial = _FgHaStatsSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 2),
    _FgHaStatsSerial_Type()
)
fgHaStatsSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsSerial.setStatus("current")


class _FgHaStatsCpuUsage_Type(Gauge32):
    """Custom type fgHaStatsCpuUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgHaStatsCpuUsage_Type.__name__ = "Gauge32"
_FgHaStatsCpuUsage_Object = MibTableColumn
fgHaStatsCpuUsage = _FgHaStatsCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 3),
    _FgHaStatsCpuUsage_Type()
)
fgHaStatsCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsCpuUsage.setStatus("current")


class _FgHaStatsMemUsage_Type(Gauge32):
    """Custom type fgHaStatsMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgHaStatsMemUsage_Type.__name__ = "Gauge32"
_FgHaStatsMemUsage_Object = MibTableColumn
fgHaStatsMemUsage = _FgHaStatsMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 4),
    _FgHaStatsMemUsage_Type()
)
fgHaStatsMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsMemUsage.setStatus("current")
_FgHaStatsNetUsage_Type = Gauge32
_FgHaStatsNetUsage_Object = MibTableColumn
fgHaStatsNetUsage = _FgHaStatsNetUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 5),
    _FgHaStatsNetUsage_Type()
)
fgHaStatsNetUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsNetUsage.setStatus("current")
_FgHaStatsSesCount_Type = Gauge32
_FgHaStatsSesCount_Object = MibTableColumn
fgHaStatsSesCount = _FgHaStatsSesCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 6),
    _FgHaStatsSesCount_Type()
)
fgHaStatsSesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsSesCount.setStatus("current")
_FgHaStatsPktCount_Type = Counter32
_FgHaStatsPktCount_Object = MibTableColumn
fgHaStatsPktCount = _FgHaStatsPktCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 7),
    _FgHaStatsPktCount_Type()
)
fgHaStatsPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsPktCount.setStatus("current")
_FgHaStatsByteCount_Type = Counter32
_FgHaStatsByteCount_Object = MibTableColumn
fgHaStatsByteCount = _FgHaStatsByteCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 8),
    _FgHaStatsByteCount_Type()
)
fgHaStatsByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsByteCount.setStatus("current")
_FgHaStatsIdsCount_Type = Counter32
_FgHaStatsIdsCount_Object = MibTableColumn
fgHaStatsIdsCount = _FgHaStatsIdsCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 9),
    _FgHaStatsIdsCount_Type()
)
fgHaStatsIdsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsIdsCount.setStatus("current")
_FgHaStatsAvCount_Type = Counter32
_FgHaStatsAvCount_Object = MibTableColumn
fgHaStatsAvCount = _FgHaStatsAvCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 10),
    _FgHaStatsAvCount_Type()
)
fgHaStatsAvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsAvCount.setStatus("current")


class _FgHaStatsHostname_Type(DisplayString):
    """Custom type fgHaStatsHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FgHaStatsHostname_Type.__name__ = "DisplayString"
_FgHaStatsHostname_Object = MibTableColumn
fgHaStatsHostname = _FgHaStatsHostname_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 11),
    _FgHaStatsHostname_Type()
)
fgHaStatsHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsHostname.setStatus("current")
_FgHaStatsSyncStatus_Type = FgHaStatsSyncStatusType
_FgHaStatsSyncStatus_Object = MibTableColumn
fgHaStatsSyncStatus = _FgHaStatsSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 12),
    _FgHaStatsSyncStatus_Type()
)
fgHaStatsSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsSyncStatus.setStatus("current")
_FgHaStatsSyncDatimeSucc_Type = DateAndTime
_FgHaStatsSyncDatimeSucc_Object = MibTableColumn
fgHaStatsSyncDatimeSucc = _FgHaStatsSyncDatimeSucc_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 13),
    _FgHaStatsSyncDatimeSucc_Type()
)
fgHaStatsSyncDatimeSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsSyncDatimeSucc.setStatus("current")
_FgHaStatsSyncDatimeUnsucc_Type = DateAndTime
_FgHaStatsSyncDatimeUnsucc_Object = MibTableColumn
fgHaStatsSyncDatimeUnsucc = _FgHaStatsSyncDatimeUnsucc_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 14),
    _FgHaStatsSyncDatimeUnsucc_Type()
)
fgHaStatsSyncDatimeUnsucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsSyncDatimeUnsucc.setStatus("current")


class _FgHaStatsGlobalChecksum_Type(DisplayString):
    """Custom type fgHaStatsGlobalChecksum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgHaStatsGlobalChecksum_Type.__name__ = "DisplayString"
_FgHaStatsGlobalChecksum_Object = MibTableColumn
fgHaStatsGlobalChecksum = _FgHaStatsGlobalChecksum_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 15),
    _FgHaStatsGlobalChecksum_Type()
)
fgHaStatsGlobalChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsGlobalChecksum.setStatus("current")


class _FgHaStatsMasterSerial_Type(DisplayString):
    """Custom type fgHaStatsMasterSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgHaStatsMasterSerial_Type.__name__ = "DisplayString"
_FgHaStatsMasterSerial_Object = MibTableColumn
fgHaStatsMasterSerial = _FgHaStatsMasterSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 16),
    _FgHaStatsMasterSerial_Type()
)
fgHaStatsMasterSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsMasterSerial.setStatus("current")
_FgHaTrapObjects_ObjectIdentity = ObjectIdentity
fgHaTrapObjects = _FgHaTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 3)
)
_FgHaTrapMemberSerial_Type = DisplayString
_FgHaTrapMemberSerial_Object = MibScalar
fgHaTrapMemberSerial = _FgHaTrapMemberSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 3, 1),
    _FgHaTrapMemberSerial_Type()
)
fgHaTrapMemberSerial.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgHaTrapMemberSerial.setStatus("current")
_FgWc_ObjectIdentity = ObjectIdentity
fgWc = _FgWc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14)
)
_FgWcTrapObjects_ObjectIdentity = ObjectIdentity
fgWcTrapObjects = _FgWcTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 1)
)
_FgWcApVdom_Type = FgVdIndex
_FgWcApVdom_Object = MibScalar
fgWcApVdom = _FgWcApVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 1, 1),
    _FgWcApVdom_Type()
)
fgWcApVdom.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgWcApVdom.setStatus("current")


class _FgWcApSerial_Type(DisplayString):
    """Custom type fgWcApSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgWcApSerial_Type.__name__ = "DisplayString"
_FgWcApSerial_Object = MibScalar
fgWcApSerial = _FgWcApSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 1, 2),
    _FgWcApSerial_Type()
)
fgWcApSerial.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgWcApSerial.setStatus("current")


class _FgWcApName_Type(DisplayString):
    """Custom type fgWcApName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgWcApName_Type.__name__ = "DisplayString"
_FgWcApName_Object = MibScalar
fgWcApName = _FgWcApName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 1, 3),
    _FgWcApName_Type()
)
fgWcApName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgWcApName.setStatus("current")
_FgWcInfo_ObjectIdentity = ObjectIdentity
fgWcInfo = _FgWcInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 2)
)
_FgWcInfoName_Type = DisplayString
_FgWcInfoName_Object = MibScalar
fgWcInfoName = _FgWcInfoName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 2, 1),
    _FgWcInfoName_Type()
)
fgWcInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcInfoName.setStatus("current")
_FgWcInfoLocation_Type = DisplayString
_FgWcInfoLocation_Object = MibScalar
fgWcInfoLocation = _FgWcInfoLocation_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 2, 2),
    _FgWcInfoLocation_Type()
)
fgWcInfoLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcInfoLocation.setStatus("current")
_FgWcInfoWtpCapacity_Type = Unsigned32
_FgWcInfoWtpCapacity_Object = MibScalar
fgWcInfoWtpCapacity = _FgWcInfoWtpCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 2, 3),
    _FgWcInfoWtpCapacity_Type()
)
fgWcInfoWtpCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcInfoWtpCapacity.setStatus("current")
_FgWcInfoWtpManaged_Type = Unsigned32
_FgWcInfoWtpManaged_Object = MibScalar
fgWcInfoWtpManaged = _FgWcInfoWtpManaged_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 2, 4),
    _FgWcInfoWtpManaged_Type()
)
fgWcInfoWtpManaged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcInfoWtpManaged.setStatus("current")
_FgWcInfoWtpSessions_Type = Gauge32
_FgWcInfoWtpSessions_Object = MibScalar
fgWcInfoWtpSessions = _FgWcInfoWtpSessions_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 2, 5),
    _FgWcInfoWtpSessions_Type()
)
fgWcInfoWtpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcInfoWtpSessions.setStatus("current")
_FgWcInfoStationCapacity_Type = Unsigned32
_FgWcInfoStationCapacity_Object = MibScalar
fgWcInfoStationCapacity = _FgWcInfoStationCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 2, 6),
    _FgWcInfoStationCapacity_Type()
)
fgWcInfoStationCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcInfoStationCapacity.setStatus("current")
_FgWcInfoStationCount_Type = Gauge32
_FgWcInfoStationCount_Object = MibScalar
fgWcInfoStationCount = _FgWcInfoStationCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 2, 7),
    _FgWcInfoStationCount_Type()
)
fgWcInfoStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcInfoStationCount.setStatus("current")
_FgWcWlanTable_Object = MibTable
fgWcWlanTable = _FgWcWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3)
)
if mibBuilder.loadTexts:
    fgWcWlanTable.setStatus("current")
_FgWcWlanEntry_Object = MibTableRow
fgWcWlanEntry = _FgWcWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1)
)
fgWcWlanEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fgWcWlanEntry.setStatus("current")


class _FgWcWlanSsid_Type(OctetString):
    """Custom type fgWcWlanSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgWcWlanSsid_Type.__name__ = "OctetString"
_FgWcWlanSsid_Object = MibTableColumn
fgWcWlanSsid = _FgWcWlanSsid_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 1),
    _FgWcWlanSsid_Type()
)
fgWcWlanSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanSsid.setStatus("current")
_FgWcWlanBroadcastSsid_Type = FnBoolState
_FgWcWlanBroadcastSsid_Object = MibTableColumn
fgWcWlanBroadcastSsid = _FgWcWlanBroadcastSsid_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 2),
    _FgWcWlanBroadcastSsid_Type()
)
fgWcWlanBroadcastSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanBroadcastSsid.setStatus("current")
_FgWcWlanSecurity_Type = FgWcWlanSecurityType
_FgWcWlanSecurity_Object = MibTableColumn
fgWcWlanSecurity = _FgWcWlanSecurity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 3),
    _FgWcWlanSecurity_Type()
)
fgWcWlanSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanSecurity.setStatus("current")
_FgWcWlanEncryption_Type = FgWcWlanEncryptionType
_FgWcWlanEncryption_Object = MibTableColumn
fgWcWlanEncryption = _FgWcWlanEncryption_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 4),
    _FgWcWlanEncryption_Type()
)
fgWcWlanEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanEncryption.setStatus("current")
_FgWcWlanAuthentication_Type = FgWcWlanAuthenticationType
_FgWcWlanAuthentication_Object = MibTableColumn
fgWcWlanAuthentication = _FgWcWlanAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 5),
    _FgWcWlanAuthentication_Type()
)
fgWcWlanAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanAuthentication.setStatus("current")
_FgWcWlanRadiusServer_Type = DisplayString
_FgWcWlanRadiusServer_Object = MibTableColumn
fgWcWlanRadiusServer = _FgWcWlanRadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 6),
    _FgWcWlanRadiusServer_Type()
)
fgWcWlanRadiusServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanRadiusServer.setStatus("current")
_FgWcWlanUserGroup_Type = DisplayString
_FgWcWlanUserGroup_Object = MibTableColumn
fgWcWlanUserGroup = _FgWcWlanUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 7),
    _FgWcWlanUserGroup_Type()
)
fgWcWlanUserGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanUserGroup.setStatus("current")
_FgWcWlanLocalBridging_Type = FnBoolState
_FgWcWlanLocalBridging_Object = MibTableColumn
fgWcWlanLocalBridging = _FgWcWlanLocalBridging_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 8),
    _FgWcWlanLocalBridging_Type()
)
fgWcWlanLocalBridging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanLocalBridging.setStatus("current")


class _FgWcWlanVlanId_Type(Integer32):
    """Custom type fgWcWlanVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_FgWcWlanVlanId_Type.__name__ = "Integer32"
_FgWcWlanVlanId_Object = MibTableColumn
fgWcWlanVlanId = _FgWcWlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 9),
    _FgWcWlanVlanId_Type()
)
fgWcWlanVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanVlanId.setStatus("current")
_FgWcWlanMeshBackhaul_Type = FnBoolState
_FgWcWlanMeshBackhaul_Object = MibTableColumn
fgWcWlanMeshBackhaul = _FgWcWlanMeshBackhaul_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 10),
    _FgWcWlanMeshBackhaul_Type()
)
fgWcWlanMeshBackhaul.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanMeshBackhaul.setStatus("current")
_FgWcWlanStationCapacity_Type = Unsigned32
_FgWcWlanStationCapacity_Object = MibTableColumn
fgWcWlanStationCapacity = _FgWcWlanStationCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 11),
    _FgWcWlanStationCapacity_Type()
)
fgWcWlanStationCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanStationCapacity.setStatus("current")
_FgWcWlanStationCount_Type = Gauge32
_FgWcWlanStationCount_Object = MibTableColumn
fgWcWlanStationCount = _FgWcWlanStationCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 12),
    _FgWcWlanStationCount_Type()
)
fgWcWlanStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanStationCount.setStatus("current")
_FgWcWtpTables_ObjectIdentity = ObjectIdentity
fgWcWtpTables = _FgWcWtpTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4)
)
_FgWcWtpProfileTable_Object = MibTable
fgWcWtpProfileTable = _FgWcWtpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 1)
)
if mibBuilder.loadTexts:
    fgWcWtpProfileTable.setStatus("current")
_FgWcWtpProfileEntry_Object = MibTableRow
fgWcWtpProfileEntry = _FgWcWtpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 1, 1)
)
fgWcWtpProfileEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWcWtpProfileName"),
)
if mibBuilder.loadTexts:
    fgWcWtpProfileEntry.setStatus("current")


class _FgWcWtpProfileName_Type(DisplayString):
    """Custom type fgWcWtpProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_FgWcWtpProfileName_Type.__name__ = "DisplayString"
_FgWcWtpProfileName_Object = MibTableColumn
fgWcWtpProfileName = _FgWcWtpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 1, 1, 1),
    _FgWcWtpProfileName_Type()
)
fgWcWtpProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWcWtpProfileName.setStatus("current")
_FgWcWtpProfilePlatform_Type = DisplayString
_FgWcWtpProfilePlatform_Object = MibTableColumn
fgWcWtpProfilePlatform = _FgWcWtpProfilePlatform_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 1, 1, 2),
    _FgWcWtpProfilePlatform_Type()
)
fgWcWtpProfilePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfilePlatform.setStatus("current")


class _FgWcWtpProfileDataChannelDtlsPolicy_Type(Bits):
    """Custom type fgWcWtpProfileDataChannelDtlsPolicy based on Bits"""
    namedValues = NamedValues(
        *(("clear", 1),
          ("dtls", 2),
          ("other", 0))
    )

_FgWcWtpProfileDataChannelDtlsPolicy_Type.__name__ = "Bits"
_FgWcWtpProfileDataChannelDtlsPolicy_Object = MibTableColumn
fgWcWtpProfileDataChannelDtlsPolicy = _FgWcWtpProfileDataChannelDtlsPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 1, 1, 3),
    _FgWcWtpProfileDataChannelDtlsPolicy_Type()
)
fgWcWtpProfileDataChannelDtlsPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileDataChannelDtlsPolicy.setStatus("current")
_FgWcWtpProfileCountryString_Type = FgWcCountryString
_FgWcWtpProfileCountryString_Object = MibTableColumn
fgWcWtpProfileCountryString = _FgWcWtpProfileCountryString_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 1, 1, 4),
    _FgWcWtpProfileCountryString_Type()
)
fgWcWtpProfileCountryString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileCountryString.setStatus("current")
_FgWcWtpProfileRadioTable_Object = MibTable
fgWcWtpProfileRadioTable = _FgWcWtpProfileRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2)
)
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioTable.setStatus("current")
_FgWcWtpProfileRadioEntry_Object = MibTableRow
fgWcWtpProfileRadioEntry = _FgWcWtpProfileRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1)
)
fgWcWtpProfileRadioEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioProfileName"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioRadioId"),
)
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioEntry.setStatus("current")


class _FgWcWtpProfileRadioProfileName_Type(DisplayString):
    """Custom type fgWcWtpProfileRadioProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_FgWcWtpProfileRadioProfileName_Type.__name__ = "DisplayString"
_FgWcWtpProfileRadioProfileName_Object = MibTableColumn
fgWcWtpProfileRadioProfileName = _FgWcWtpProfileRadioProfileName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 1),
    _FgWcWtpProfileRadioProfileName_Type()
)
fgWcWtpProfileRadioProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioProfileName.setStatus("current")
_FgWcWtpProfileRadioRadioId_Type = FgWcWtpRadioId
_FgWcWtpProfileRadioRadioId_Object = MibTableColumn
fgWcWtpProfileRadioRadioId = _FgWcWtpProfileRadioRadioId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 2),
    _FgWcWtpProfileRadioRadioId_Type()
)
fgWcWtpProfileRadioRadioId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioRadioId.setStatus("current")
_FgWcWtpProfileRadioMode_Type = FgWcWtpRadioMode
_FgWcWtpProfileRadioMode_Object = MibTableColumn
fgWcWtpProfileRadioMode = _FgWcWtpProfileRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 3),
    _FgWcWtpProfileRadioMode_Type()
)
fgWcWtpProfileRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioMode.setStatus("current")
_FgWcWtpProfileRadioApScan_Type = FnBoolState
_FgWcWtpProfileRadioApScan_Object = MibTableColumn
fgWcWtpProfileRadioApScan = _FgWcWtpProfileRadioApScan_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 4),
    _FgWcWtpProfileRadioApScan_Type()
)
fgWcWtpProfileRadioApScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioApScan.setStatus("current")
_FgWcWtpProfileRadioWidsProfile_Type = DisplayString
_FgWcWtpProfileRadioWidsProfile_Object = MibTableColumn
fgWcWtpProfileRadioWidsProfile = _FgWcWtpProfileRadioWidsProfile_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 5),
    _FgWcWtpProfileRadioWidsProfile_Type()
)
fgWcWtpProfileRadioWidsProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioWidsProfile.setStatus("current")
_FgWcWtpProfileRadioDarrp_Type = FnBoolState
_FgWcWtpProfileRadioDarrp_Object = MibTableColumn
fgWcWtpProfileRadioDarrp = _FgWcWtpProfileRadioDarrp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 6),
    _FgWcWtpProfileRadioDarrp_Type()
)
fgWcWtpProfileRadioDarrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioDarrp.setStatus("current")
_FgWcWtpProfileRadioFrequencyHandoff_Type = FnBoolState
_FgWcWtpProfileRadioFrequencyHandoff_Object = MibTableColumn
fgWcWtpProfileRadioFrequencyHandoff = _FgWcWtpProfileRadioFrequencyHandoff_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 7),
    _FgWcWtpProfileRadioFrequencyHandoff_Type()
)
fgWcWtpProfileRadioFrequencyHandoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioFrequencyHandoff.setStatus("current")
_FgWcWtpProfileRadioApHandoff_Type = FnBoolState
_FgWcWtpProfileRadioApHandoff_Object = MibTableColumn
fgWcWtpProfileRadioApHandoff = _FgWcWtpProfileRadioApHandoff_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 8),
    _FgWcWtpProfileRadioApHandoff_Type()
)
fgWcWtpProfileRadioApHandoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioApHandoff.setStatus("current")


class _FgWcWtpProfileRadioBeaconInterval_Type(Integer32):
    """Custom type fgWcWtpProfileRadioBeaconInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FgWcWtpProfileRadioBeaconInterval_Type.__name__ = "Integer32"
_FgWcWtpProfileRadioBeaconInterval_Object = MibTableColumn
fgWcWtpProfileRadioBeaconInterval = _FgWcWtpProfileRadioBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 9),
    _FgWcWtpProfileRadioBeaconInterval_Type()
)
fgWcWtpProfileRadioBeaconInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioBeaconInterval.setStatus("current")


class _FgWcWtpProfileRadioDtimPeriod_Type(Integer32):
    """Custom type fgWcWtpProfileRadioDtimPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FgWcWtpProfileRadioDtimPeriod_Type.__name__ = "Integer32"
_FgWcWtpProfileRadioDtimPeriod_Object = MibTableColumn
fgWcWtpProfileRadioDtimPeriod = _FgWcWtpProfileRadioDtimPeriod_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 10),
    _FgWcWtpProfileRadioDtimPeriod_Type()
)
fgWcWtpProfileRadioDtimPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioDtimPeriod.setStatus("current")
_FgWcWtpProfileRadioBand_Type = FgWcWtpRadioType
_FgWcWtpProfileRadioBand_Object = MibTableColumn
fgWcWtpProfileRadioBand = _FgWcWtpProfileRadioBand_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 11),
    _FgWcWtpProfileRadioBand_Type()
)
fgWcWtpProfileRadioBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioBand.setStatus("current")
_FgWcWtpProfileRadioChannelBonding_Type = FnBoolState
_FgWcWtpProfileRadioChannelBonding_Object = MibTableColumn
fgWcWtpProfileRadioChannelBonding = _FgWcWtpProfileRadioChannelBonding_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 12),
    _FgWcWtpProfileRadioChannelBonding_Type()
)
fgWcWtpProfileRadioChannelBonding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioChannelBonding.setStatus("current")
_FgWcWtpProfileRadioChannel_Type = DisplayString
_FgWcWtpProfileRadioChannel_Object = MibTableColumn
fgWcWtpProfileRadioChannel = _FgWcWtpProfileRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 13),
    _FgWcWtpProfileRadioChannel_Type()
)
fgWcWtpProfileRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioChannel.setStatus("current")
_FgWcWtpProfileRadioAutoTxPowerControl_Type = FnBoolState
_FgWcWtpProfileRadioAutoTxPowerControl_Object = MibTableColumn
fgWcWtpProfileRadioAutoTxPowerControl = _FgWcWtpProfileRadioAutoTxPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 14),
    _FgWcWtpProfileRadioAutoTxPowerControl_Type()
)
fgWcWtpProfileRadioAutoTxPowerControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioAutoTxPowerControl.setStatus("current")
_FgWcWtpProfileRadioAutoTxPowerLow_Type = Integer32
_FgWcWtpProfileRadioAutoTxPowerLow_Object = MibTableColumn
fgWcWtpProfileRadioAutoTxPowerLow = _FgWcWtpProfileRadioAutoTxPowerLow_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 15),
    _FgWcWtpProfileRadioAutoTxPowerLow_Type()
)
fgWcWtpProfileRadioAutoTxPowerLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioAutoTxPowerLow.setStatus("current")
_FgWcWtpProfileRadioAutoTxPowerHigh_Type = Integer32
_FgWcWtpProfileRadioAutoTxPowerHigh_Object = MibTableColumn
fgWcWtpProfileRadioAutoTxPowerHigh = _FgWcWtpProfileRadioAutoTxPowerHigh_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 16),
    _FgWcWtpProfileRadioAutoTxPowerHigh_Type()
)
fgWcWtpProfileRadioAutoTxPowerHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioAutoTxPowerHigh.setStatus("current")


class _FgWcWtpProfileRadioTxPowerLevel_Type(Gauge32):
    """Custom type fgWcWtpProfileRadioTxPowerLevel based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgWcWtpProfileRadioTxPowerLevel_Type.__name__ = "Gauge32"
_FgWcWtpProfileRadioTxPowerLevel_Object = MibTableColumn
fgWcWtpProfileRadioTxPowerLevel = _FgWcWtpProfileRadioTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 17),
    _FgWcWtpProfileRadioTxPowerLevel_Type()
)
fgWcWtpProfileRadioTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioTxPowerLevel.setStatus("current")
_FgWcWtpProfileRadioVaps_Type = DisplayString
_FgWcWtpProfileRadioVaps_Object = MibTableColumn
fgWcWtpProfileRadioVaps = _FgWcWtpProfileRadioVaps_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 18),
    _FgWcWtpProfileRadioVaps_Type()
)
fgWcWtpProfileRadioVaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioVaps.setStatus("current")
_FgWcWtpProfileRadioStationCapacity_Type = Unsigned32
_FgWcWtpProfileRadioStationCapacity_Object = MibTableColumn
fgWcWtpProfileRadioStationCapacity = _FgWcWtpProfileRadioStationCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 19),
    _FgWcWtpProfileRadioStationCapacity_Type()
)
fgWcWtpProfileRadioStationCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioStationCapacity.setStatus("current")
_FgWcWtpProfileRadioChannelWidth_Type = FgWcWtpChannelWidthType
_FgWcWtpProfileRadioChannelWidth_Object = MibTableColumn
fgWcWtpProfileRadioChannelWidth = _FgWcWtpProfileRadioChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 20),
    _FgWcWtpProfileRadioChannelWidth_Type()
)
fgWcWtpProfileRadioChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioChannelWidth.setStatus("current")
_FgWcWtpConfigTable_Object = MibTable
fgWcWtpConfigTable = _FgWcWtpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3)
)
if mibBuilder.loadTexts:
    fgWcWtpConfigTable.setStatus("current")
_FgWcWtpConfigEntry_Object = MibTableRow
fgWcWtpConfigEntry = _FgWcWtpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1)
)
fgWcWtpConfigEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWcWtpConfigWtpId"),
)
if mibBuilder.loadTexts:
    fgWcWtpConfigEntry.setStatus("current")


class _FgWcWtpConfigWtpId_Type(DisplayString):
    """Custom type fgWcWtpConfigWtpId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_FgWcWtpConfigWtpId_Type.__name__ = "DisplayString"
_FgWcWtpConfigWtpId_Object = MibTableColumn
fgWcWtpConfigWtpId = _FgWcWtpConfigWtpId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 1),
    _FgWcWtpConfigWtpId_Type()
)
fgWcWtpConfigWtpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWcWtpConfigWtpId.setStatus("current")


class _FgWcWtpConfigWtpAdmin_Type(Integer32):
    """Custom type fgWcWtpConfigWtpAdmin based on Integer32"""
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
        *(("disable", 2),
          ("discovered", 1),
          ("enable", 3),
          ("other", 0))
    )


_FgWcWtpConfigWtpAdmin_Type.__name__ = "Integer32"
_FgWcWtpConfigWtpAdmin_Object = MibTableColumn
fgWcWtpConfigWtpAdmin = _FgWcWtpConfigWtpAdmin_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 2),
    _FgWcWtpConfigWtpAdmin_Type()
)
fgWcWtpConfigWtpAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigWtpAdmin.setStatus("current")
_FgWcWtpConfigWtpName_Type = DisplayString
_FgWcWtpConfigWtpName_Object = MibTableColumn
fgWcWtpConfigWtpName = _FgWcWtpConfigWtpName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 3),
    _FgWcWtpConfigWtpName_Type()
)
fgWcWtpConfigWtpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigWtpName.setStatus("current")
_FgWcWtpConfigWtpLocation_Type = DisplayString
_FgWcWtpConfigWtpLocation_Object = MibTableColumn
fgWcWtpConfigWtpLocation = _FgWcWtpConfigWtpLocation_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 4),
    _FgWcWtpConfigWtpLocation_Type()
)
fgWcWtpConfigWtpLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigWtpLocation.setStatus("current")
_FgWcWtpConfigWtpProfile_Type = DisplayString
_FgWcWtpConfigWtpProfile_Object = MibTableColumn
fgWcWtpConfigWtpProfile = _FgWcWtpConfigWtpProfile_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 5),
    _FgWcWtpConfigWtpProfile_Type()
)
fgWcWtpConfigWtpProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigWtpProfile.setStatus("current")
_FgWcWtpConfigRadioEnable_Type = FnBoolState
_FgWcWtpConfigRadioEnable_Object = MibTableColumn
fgWcWtpConfigRadioEnable = _FgWcWtpConfigRadioEnable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 6),
    _FgWcWtpConfigRadioEnable_Type()
)
fgWcWtpConfigRadioEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigRadioEnable.setStatus("current")
_FgWcWtpConfigRadioAutoTxPowerControl_Type = FnBoolState
_FgWcWtpConfigRadioAutoTxPowerControl_Object = MibTableColumn
fgWcWtpConfigRadioAutoTxPowerControl = _FgWcWtpConfigRadioAutoTxPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 7),
    _FgWcWtpConfigRadioAutoTxPowerControl_Type()
)
fgWcWtpConfigRadioAutoTxPowerControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigRadioAutoTxPowerControl.setStatus("current")
_FgWcWtpConfigRadioAutoTxPowerLow_Type = Integer32
_FgWcWtpConfigRadioAutoTxPowerLow_Object = MibTableColumn
fgWcWtpConfigRadioAutoTxPowerLow = _FgWcWtpConfigRadioAutoTxPowerLow_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 8),
    _FgWcWtpConfigRadioAutoTxPowerLow_Type()
)
fgWcWtpConfigRadioAutoTxPowerLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigRadioAutoTxPowerLow.setStatus("current")
_FgWcWtpConfigRadioAutoTxPowerHigh_Type = Integer32
_FgWcWtpConfigRadioAutoTxPowerHigh_Object = MibTableColumn
fgWcWtpConfigRadioAutoTxPowerHigh = _FgWcWtpConfigRadioAutoTxPowerHigh_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 9),
    _FgWcWtpConfigRadioAutoTxPowerHigh_Type()
)
fgWcWtpConfigRadioAutoTxPowerHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigRadioAutoTxPowerHigh.setStatus("current")


class _FgWcWtpConfigRadioTxPowerLevel_Type(Gauge32):
    """Custom type fgWcWtpConfigRadioTxPowerLevel based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgWcWtpConfigRadioTxPowerLevel_Type.__name__ = "Gauge32"
_FgWcWtpConfigRadioTxPowerLevel_Object = MibTableColumn
fgWcWtpConfigRadioTxPowerLevel = _FgWcWtpConfigRadioTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 10),
    _FgWcWtpConfigRadioTxPowerLevel_Type()
)
fgWcWtpConfigRadioTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigRadioTxPowerLevel.setStatus("current")
_FgWcWtpConfigRadioBand_Type = FgWcWtpRadioBandType
_FgWcWtpConfigRadioBand_Object = MibTableColumn
fgWcWtpConfigRadioBand = _FgWcWtpConfigRadioBand_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 11),
    _FgWcWtpConfigRadioBand_Type()
)
fgWcWtpConfigRadioBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigRadioBand.setStatus("current")
_FgWcWtpConfigRadioApScan_Type = FnBoolState
_FgWcWtpConfigRadioApScan_Object = MibTableColumn
fgWcWtpConfigRadioApScan = _FgWcWtpConfigRadioApScan_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 12),
    _FgWcWtpConfigRadioApScan_Type()
)
fgWcWtpConfigRadioApScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigRadioApScan.setStatus("current")
_FgWcWtpConfigVapAll_Type = FnBoolState
_FgWcWtpConfigVapAll_Object = MibTableColumn
fgWcWtpConfigVapAll = _FgWcWtpConfigVapAll_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 13),
    _FgWcWtpConfigVapAll_Type()
)
fgWcWtpConfigVapAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigVapAll.setStatus("current")
_FgWcWtpConfigVaps_Type = DisplayString
_FgWcWtpConfigVaps_Object = MibTableColumn
fgWcWtpConfigVaps = _FgWcWtpConfigVaps_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 14),
    _FgWcWtpConfigVaps_Type()
)
fgWcWtpConfigVaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigVaps.setStatus("current")
_FgWcWtpSessionTable_Object = MibTable
fgWcWtpSessionTable = _FgWcWtpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4)
)
if mibBuilder.loadTexts:
    fgWcWtpSessionTable.setStatus("current")
_FgWcWtpSessionEntry_Object = MibTableRow
fgWcWtpSessionEntry = _FgWcWtpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1)
)
fgWcWtpSessionEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpId"),
)
if mibBuilder.loadTexts:
    fgWcWtpSessionEntry.setStatus("current")


class _FgWcWtpSessionWtpId_Type(DisplayString):
    """Custom type fgWcWtpSessionWtpId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_FgWcWtpSessionWtpId_Type.__name__ = "DisplayString"
_FgWcWtpSessionWtpId_Object = MibTableColumn
fgWcWtpSessionWtpId = _FgWcWtpSessionWtpId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 1),
    _FgWcWtpSessionWtpId_Type()
)
fgWcWtpSessionWtpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpId.setStatus("current")
_FgWcWtpSessionWtpIpAddressType_Type = InetAddressType
_FgWcWtpSessionWtpIpAddressType_Object = MibTableColumn
fgWcWtpSessionWtpIpAddressType = _FgWcWtpSessionWtpIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 2),
    _FgWcWtpSessionWtpIpAddressType_Type()
)
fgWcWtpSessionWtpIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpIpAddressType.setStatus("current")
_FgWcWtpSessionWtpIpAddress_Type = InetAddress
_FgWcWtpSessionWtpIpAddress_Object = MibTableColumn
fgWcWtpSessionWtpIpAddress = _FgWcWtpSessionWtpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 3),
    _FgWcWtpSessionWtpIpAddress_Type()
)
fgWcWtpSessionWtpIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpIpAddress.setStatus("current")
_FgWcWtpSessionWtpLocalIpAddressType_Type = InetAddressType
_FgWcWtpSessionWtpLocalIpAddressType_Object = MibTableColumn
fgWcWtpSessionWtpLocalIpAddressType = _FgWcWtpSessionWtpLocalIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 4),
    _FgWcWtpSessionWtpLocalIpAddressType_Type()
)
fgWcWtpSessionWtpLocalIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpLocalIpAddressType.setStatus("current")
_FgWcWtpSessionWtpLocalIpAddress_Type = InetAddress
_FgWcWtpSessionWtpLocalIpAddress_Object = MibTableColumn
fgWcWtpSessionWtpLocalIpAddress = _FgWcWtpSessionWtpLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 5),
    _FgWcWtpSessionWtpLocalIpAddress_Type()
)
fgWcWtpSessionWtpLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpLocalIpAddress.setStatus("current")


class _FgWcWtpSessionWtpBaseMacAddress_Type(PhysAddress):
    """Custom type fgWcWtpSessionWtpBaseMacAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
    )


_FgWcWtpSessionWtpBaseMacAddress_Type.__name__ = "PhysAddress"
_FgWcWtpSessionWtpBaseMacAddress_Object = MibTableColumn
fgWcWtpSessionWtpBaseMacAddress = _FgWcWtpSessionWtpBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 6),
    _FgWcWtpSessionWtpBaseMacAddress_Type()
)
fgWcWtpSessionWtpBaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpBaseMacAddress.setStatus("current")


class _FgWcWtpSessionConnectionState_Type(Integer32):
    """Custom type fgWcWtpSessionConnectionState based on Integer32"""
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
        *(("connectedImage", 4),
          ("downloadingImage", 3),
          ("offLine", 1),
          ("onLine", 2),
          ("other", 0))
    )


_FgWcWtpSessionConnectionState_Type.__name__ = "Integer32"
_FgWcWtpSessionConnectionState_Object = MibTableColumn
fgWcWtpSessionConnectionState = _FgWcWtpSessionConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 7),
    _FgWcWtpSessionConnectionState_Type()
)
fgWcWtpSessionConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionConnectionState.setStatus("current")
_FgWcWtpSessionWtpUpTime_Type = TimeTicks
_FgWcWtpSessionWtpUpTime_Object = MibTableColumn
fgWcWtpSessionWtpUpTime = _FgWcWtpSessionWtpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 8),
    _FgWcWtpSessionWtpUpTime_Type()
)
fgWcWtpSessionWtpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpUpTime.setStatus("current")
_FgWcWtpSessionWtpDaemonUpTime_Type = TimeTicks
_FgWcWtpSessionWtpDaemonUpTime_Object = MibTableColumn
fgWcWtpSessionWtpDaemonUpTime = _FgWcWtpSessionWtpDaemonUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 9),
    _FgWcWtpSessionWtpDaemonUpTime_Type()
)
fgWcWtpSessionWtpDaemonUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpDaemonUpTime.setStatus("current")
_FgWcWtpSessionWtpSessionUpTime_Type = TimeTicks
_FgWcWtpSessionWtpSessionUpTime_Object = MibTableColumn
fgWcWtpSessionWtpSessionUpTime = _FgWcWtpSessionWtpSessionUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 10),
    _FgWcWtpSessionWtpSessionUpTime_Type()
)
fgWcWtpSessionWtpSessionUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpSessionUpTime.setStatus("current")
_FgWcWtpSessionWtpProfileName_Type = DisplayString
_FgWcWtpSessionWtpProfileName_Object = MibTableColumn
fgWcWtpSessionWtpProfileName = _FgWcWtpSessionWtpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 11),
    _FgWcWtpSessionWtpProfileName_Type()
)
fgWcWtpSessionWtpProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpProfileName.setStatus("current")
_FgWcWtpSessionWtpModelNumber_Type = DisplayString
_FgWcWtpSessionWtpModelNumber_Object = MibTableColumn
fgWcWtpSessionWtpModelNumber = _FgWcWtpSessionWtpModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 12),
    _FgWcWtpSessionWtpModelNumber_Type()
)
fgWcWtpSessionWtpModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpModelNumber.setStatus("current")
_FgWcWtpSessionWtpHwVersion_Type = DisplayString
_FgWcWtpSessionWtpHwVersion_Object = MibTableColumn
fgWcWtpSessionWtpHwVersion = _FgWcWtpSessionWtpHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 13),
    _FgWcWtpSessionWtpHwVersion_Type()
)
fgWcWtpSessionWtpHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpHwVersion.setStatus("current")
_FgWcWtpSessionWtpSwVersion_Type = DisplayString
_FgWcWtpSessionWtpSwVersion_Object = MibTableColumn
fgWcWtpSessionWtpSwVersion = _FgWcWtpSessionWtpSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 14),
    _FgWcWtpSessionWtpSwVersion_Type()
)
fgWcWtpSessionWtpSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpSwVersion.setStatus("current")
_FgWcWtpSessionWtpBootVersion_Type = DisplayString
_FgWcWtpSessionWtpBootVersion_Object = MibTableColumn
fgWcWtpSessionWtpBootVersion = _FgWcWtpSessionWtpBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 15),
    _FgWcWtpSessionWtpBootVersion_Type()
)
fgWcWtpSessionWtpBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpBootVersion.setStatus("current")
_FgWcWtpSessionWtpRegionCode_Type = DisplayString
_FgWcWtpSessionWtpRegionCode_Object = MibTableColumn
fgWcWtpSessionWtpRegionCode = _FgWcWtpSessionWtpRegionCode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 16),
    _FgWcWtpSessionWtpRegionCode_Type()
)
fgWcWtpSessionWtpRegionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpRegionCode.setStatus("current")
_FgWcWtpSessionWtpStationCount_Type = Gauge32
_FgWcWtpSessionWtpStationCount_Object = MibTableColumn
fgWcWtpSessionWtpStationCount = _FgWcWtpSessionWtpStationCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 17),
    _FgWcWtpSessionWtpStationCount_Type()
)
fgWcWtpSessionWtpStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpStationCount.setStatus("current")
_FgWcWtpSessionWtpByteRxCount_Type = Counter64
_FgWcWtpSessionWtpByteRxCount_Object = MibTableColumn
fgWcWtpSessionWtpByteRxCount = _FgWcWtpSessionWtpByteRxCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 18),
    _FgWcWtpSessionWtpByteRxCount_Type()
)
fgWcWtpSessionWtpByteRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpByteRxCount.setStatus("current")
_FgWcWtpSessionWtpByteTxCount_Type = Counter64
_FgWcWtpSessionWtpByteTxCount_Object = MibTableColumn
fgWcWtpSessionWtpByteTxCount = _FgWcWtpSessionWtpByteTxCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 19),
    _FgWcWtpSessionWtpByteTxCount_Type()
)
fgWcWtpSessionWtpByteTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpByteTxCount.setStatus("current")


class _FgWcWtpSessionWtpCpuUsage_Type(Gauge32):
    """Custom type fgWcWtpSessionWtpCpuUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgWcWtpSessionWtpCpuUsage_Type.__name__ = "Gauge32"
_FgWcWtpSessionWtpCpuUsage_Object = MibTableColumn
fgWcWtpSessionWtpCpuUsage = _FgWcWtpSessionWtpCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 20),
    _FgWcWtpSessionWtpCpuUsage_Type()
)
fgWcWtpSessionWtpCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpCpuUsage.setStatus("current")


class _FgWcWtpSessionWtpMemoryUsage_Type(Gauge32):
    """Custom type fgWcWtpSessionWtpMemoryUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgWcWtpSessionWtpMemoryUsage_Type.__name__ = "Gauge32"
_FgWcWtpSessionWtpMemoryUsage_Object = MibTableColumn
fgWcWtpSessionWtpMemoryUsage = _FgWcWtpSessionWtpMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 21),
    _FgWcWtpSessionWtpMemoryUsage_Type()
)
fgWcWtpSessionWtpMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpMemoryUsage.setStatus("current")
_FgWcWtpSessionWtpMemoryCapacity_Type = Unsigned32
_FgWcWtpSessionWtpMemoryCapacity_Object = MibTableColumn
fgWcWtpSessionWtpMemoryCapacity = _FgWcWtpSessionWtpMemoryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 22),
    _FgWcWtpSessionWtpMemoryCapacity_Type()
)
fgWcWtpSessionWtpMemoryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpMemoryCapacity.setStatus("current")
_FgWcWtpSessionRadioTable_Object = MibTable
fgWcWtpSessionRadioTable = _FgWcWtpSessionRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 5)
)
if mibBuilder.loadTexts:
    fgWcWtpSessionRadioTable.setStatus("current")
_FgWcWtpSessionRadioEntry_Object = MibTableRow
fgWcWtpSessionRadioEntry = _FgWcWtpSessionRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 5, 1)
)
fgWcWtpSessionRadioEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWcWtpSessionRadioWtpId"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWcWtpSessionRadioRadioId"),
)
if mibBuilder.loadTexts:
    fgWcWtpSessionRadioEntry.setStatus("current")


class _FgWcWtpSessionRadioWtpId_Type(DisplayString):
    """Custom type fgWcWtpSessionRadioWtpId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_FgWcWtpSessionRadioWtpId_Type.__name__ = "DisplayString"
_FgWcWtpSessionRadioWtpId_Object = MibTableColumn
fgWcWtpSessionRadioWtpId = _FgWcWtpSessionRadioWtpId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 5, 1, 1),
    _FgWcWtpSessionRadioWtpId_Type()
)
fgWcWtpSessionRadioWtpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWcWtpSessionRadioWtpId.setStatus("current")
_FgWcWtpSessionRadioRadioId_Type = FgWcWtpRadioId
_FgWcWtpSessionRadioRadioId_Object = MibTableColumn
fgWcWtpSessionRadioRadioId = _FgWcWtpSessionRadioRadioId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 5, 1, 2),
    _FgWcWtpSessionRadioRadioId_Type()
)
fgWcWtpSessionRadioRadioId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWcWtpSessionRadioRadioId.setStatus("current")
_FgWcWtpSessionRadioMode_Type = FgWcWtpRadioMode
_FgWcWtpSessionRadioMode_Object = MibTableColumn
fgWcWtpSessionRadioMode = _FgWcWtpSessionRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 5, 1, 3),
    _FgWcWtpSessionRadioMode_Type()
)
fgWcWtpSessionRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionRadioMode.setStatus("current")


class _FgWcWtpSessionRadioBaseBssid_Type(PhysAddress):
    """Custom type fgWcWtpSessionRadioBaseBssid based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
    )


_FgWcWtpSessionRadioBaseBssid_Type.__name__ = "PhysAddress"
_FgWcWtpSessionRadioBaseBssid_Object = MibTableColumn
fgWcWtpSessionRadioBaseBssid = _FgWcWtpSessionRadioBaseBssid_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 5, 1, 4),
    _FgWcWtpSessionRadioBaseBssid_Type()
)
fgWcWtpSessionRadioBaseBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionRadioBaseBssid.setStatus("current")
_FgWcWtpSessionRadioCountryString_Type = FgWcCountryString
_FgWcWtpSessionRadioCountryString_Object = MibTableColumn
fgWcWtpSessionRadioCountryString = _FgWcWtpSessionRadioCountryString_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 5, 1, 5),
    _FgWcWtpSessionRadioCountryString_Type()
)
fgWcWtpSessionRadioCountryString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionRadioCountryString.setStatus("current")
_FgWcWtpSessionRadioCountryCode_Type = Integer32
_FgWcWtpSessionRadioCountryCode_Object = MibTableColumn
fgWcWtpSessionRadioCountryCode = _FgWcWtpSessionRadioCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 5, 1, 6),
    _FgWcWtpSessionRadioCountryCode_Type()
)
fgWcWtpSessionRadioCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionRadioCountryCode.setStatus("current")
_FgWcWtpSessionRadioOperatingChannel_Type = FgWcWtpRadioChannelNumber
_FgWcWtpSessionRadioOperatingChannel_Object = MibTableColumn
fgWcWtpSessionRadioOperatingChannel = _FgWcWtpSessionRadioOperatingChannel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 5, 1, 7),
    _FgWcWtpSessionRadioOperatingChannel_Type()
)
fgWcWtpSessionRadioOperatingChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionRadioOperatingChannel.setStatus("current")
_FgWcWtpSessionRadioOperatingPower_Type = Integer32
_FgWcWtpSessionRadioOperatingPower_Object = MibTableColumn
fgWcWtpSessionRadioOperatingPower = _FgWcWtpSessionRadioOperatingPower_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 5, 1, 8),
    _FgWcWtpSessionRadioOperatingPower_Type()
)
fgWcWtpSessionRadioOperatingPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionRadioOperatingPower.setStatus("current")
_FgWcWtpSessionRadioStationCount_Type = Gauge32
_FgWcWtpSessionRadioStationCount_Object = MibTableColumn
fgWcWtpSessionRadioStationCount = _FgWcWtpSessionRadioStationCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 5, 1, 9),
    _FgWcWtpSessionRadioStationCount_Type()
)
fgWcWtpSessionRadioStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionRadioStationCount.setStatus("current")
_FgWcWtpSessionVapTable_Object = MibTable
fgWcWtpSessionVapTable = _FgWcWtpSessionVapTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 6)
)
if mibBuilder.loadTexts:
    fgWcWtpSessionVapTable.setStatus("current")
_FgWcWtpSessionVapEntry_Object = MibTableRow
fgWcWtpSessionVapEntry = _FgWcWtpSessionVapEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 6, 1)
)
fgWcWtpSessionVapEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWcWtpSessionVapWtpId"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWcWtpSessionVapRadioId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fgWcWtpSessionVapEntry.setStatus("current")


class _FgWcWtpSessionVapWtpId_Type(DisplayString):
    """Custom type fgWcWtpSessionVapWtpId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_FgWcWtpSessionVapWtpId_Type.__name__ = "DisplayString"
_FgWcWtpSessionVapWtpId_Object = MibTableColumn
fgWcWtpSessionVapWtpId = _FgWcWtpSessionVapWtpId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 6, 1, 1),
    _FgWcWtpSessionVapWtpId_Type()
)
fgWcWtpSessionVapWtpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWcWtpSessionVapWtpId.setStatus("current")
_FgWcWtpSessionVapRadioId_Type = FgWcWtpRadioId
_FgWcWtpSessionVapRadioId_Object = MibTableColumn
fgWcWtpSessionVapRadioId = _FgWcWtpSessionVapRadioId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 6, 1, 2),
    _FgWcWtpSessionVapRadioId_Type()
)
fgWcWtpSessionVapRadioId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWcWtpSessionVapRadioId.setStatus("current")


class _FgWcWtpSessionVapSsid_Type(OctetString):
    """Custom type fgWcWtpSessionVapSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgWcWtpSessionVapSsid_Type.__name__ = "OctetString"
_FgWcWtpSessionVapSsid_Object = MibTableColumn
fgWcWtpSessionVapSsid = _FgWcWtpSessionVapSsid_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 6, 1, 3),
    _FgWcWtpSessionVapSsid_Type()
)
fgWcWtpSessionVapSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionVapSsid.setStatus("current")
_FgWcWtpSessionVapStationCount_Type = Gauge32
_FgWcWtpSessionVapStationCount_Object = MibTableColumn
fgWcWtpSessionVapStationCount = _FgWcWtpSessionVapStationCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 6, 1, 4),
    _FgWcWtpSessionVapStationCount_Type()
)
fgWcWtpSessionVapStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionVapStationCount.setStatus("current")
_FgWcWtpSessionVapByteRxCount_Type = Counter64
_FgWcWtpSessionVapByteRxCount_Object = MibTableColumn
fgWcWtpSessionVapByteRxCount = _FgWcWtpSessionVapByteRxCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 6, 1, 5),
    _FgWcWtpSessionVapByteRxCount_Type()
)
fgWcWtpSessionVapByteRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionVapByteRxCount.setStatus("current")
_FgWcWtpSessionVapByteTxCount_Type = Counter64
_FgWcWtpSessionVapByteTxCount_Object = MibTableColumn
fgWcWtpSessionVapByteTxCount = _FgWcWtpSessionVapByteTxCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 6, 1, 6),
    _FgWcWtpSessionVapByteTxCount_Type()
)
fgWcWtpSessionVapByteTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionVapByteTxCount.setStatus("current")
_FgWcStaTable_Object = MibTable
fgWcStaTable = _FgWcStaTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5)
)
if mibBuilder.loadTexts:
    fgWcStaTable.setStatus("current")
_FgWcStaEntry_Object = MibTableRow
fgWcStaEntry = _FgWcStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1)
)
fgWcStaEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "IF-MIB", "ifIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWcStaMacAddress"),
)
if mibBuilder.loadTexts:
    fgWcStaEntry.setStatus("current")


class _FgWcStaMacAddress_Type(PhysAddress):
    """Custom type fgWcStaMacAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
    )


_FgWcStaMacAddress_Type.__name__ = "PhysAddress"
_FgWcStaMacAddress_Object = MibTableColumn
fgWcStaMacAddress = _FgWcStaMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 1),
    _FgWcStaMacAddress_Type()
)
fgWcStaMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWcStaMacAddress.setStatus("current")
_FgWcStaWlan_Type = DisplayString
_FgWcStaWlan_Object = MibTableColumn
fgWcStaWlan = _FgWcStaWlan_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 2),
    _FgWcStaWlan_Type()
)
fgWcStaWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaWlan.setStatus("current")
_FgWcStaWtpId_Type = DisplayString
_FgWcStaWtpId_Object = MibTableColumn
fgWcStaWtpId = _FgWcStaWtpId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 3),
    _FgWcStaWtpId_Type()
)
fgWcStaWtpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaWtpId.setStatus("current")
_FgWcStaRadioId_Type = FgWcWtpRadioId
_FgWcStaRadioId_Object = MibTableColumn
fgWcStaRadioId = _FgWcStaRadioId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 4),
    _FgWcStaRadioId_Type()
)
fgWcStaRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaRadioId.setStatus("current")


class _FgWcStaVlanId_Type(Integer32):
    """Custom type fgWcStaVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_FgWcStaVlanId_Type.__name__ = "Integer32"
_FgWcStaVlanId_Object = MibTableColumn
fgWcStaVlanId = _FgWcStaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 5),
    _FgWcStaVlanId_Type()
)
fgWcStaVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaVlanId.setStatus("current")
_FgWcStaIpAddressType_Type = InetAddressType
_FgWcStaIpAddressType_Object = MibTableColumn
fgWcStaIpAddressType = _FgWcStaIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 6),
    _FgWcStaIpAddressType_Type()
)
fgWcStaIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaIpAddressType.setStatus("current")
_FgWcStaIpAddress_Type = InetAddress
_FgWcStaIpAddress_Object = MibTableColumn
fgWcStaIpAddress = _FgWcStaIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 7),
    _FgWcStaIpAddress_Type()
)
fgWcStaIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaIpAddress.setStatus("current")
_FgWcStaVci_Type = DisplayString
_FgWcStaVci_Object = MibTableColumn
fgWcStaVci = _FgWcStaVci_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 8),
    _FgWcStaVci_Type()
)
fgWcStaVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaVci.setStatus("current")
_FgWcStaHost_Type = DisplayString
_FgWcStaHost_Object = MibTableColumn
fgWcStaHost = _FgWcStaHost_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 9),
    _FgWcStaHost_Type()
)
fgWcStaHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaHost.setStatus("current")
_FgWcStaUser_Type = DisplayString
_FgWcStaUser_Object = MibTableColumn
fgWcStaUser = _FgWcStaUser_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 10),
    _FgWcStaUser_Type()
)
fgWcStaUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaUser.setStatus("current")
_FgWcStaGroup_Type = DisplayString
_FgWcStaGroup_Object = MibTableColumn
fgWcStaGroup = _FgWcStaGroup_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 11),
    _FgWcStaGroup_Type()
)
fgWcStaGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaGroup.setStatus("current")
_FgWcStaSignal_Type = Integer32
_FgWcStaSignal_Object = MibTableColumn
fgWcStaSignal = _FgWcStaSignal_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 12),
    _FgWcStaSignal_Type()
)
fgWcStaSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaSignal.setStatus("current")
_FgWcStaNoise_Type = Integer32
_FgWcStaNoise_Object = MibTableColumn
fgWcStaNoise = _FgWcStaNoise_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 13),
    _FgWcStaNoise_Type()
)
fgWcStaNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaNoise.setStatus("current")
_FgWcStaIdle_Type = Gauge32
_FgWcStaIdle_Object = MibTableColumn
fgWcStaIdle = _FgWcStaIdle_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 14),
    _FgWcStaIdle_Type()
)
fgWcStaIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaIdle.setStatus("current")
_FgWcStaBandwidthTx_Type = Gauge32
_FgWcStaBandwidthTx_Object = MibTableColumn
fgWcStaBandwidthTx = _FgWcStaBandwidthTx_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 15),
    _FgWcStaBandwidthTx_Type()
)
fgWcStaBandwidthTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaBandwidthTx.setStatus("current")
_FgWcStaBandwidthRx_Type = Gauge32
_FgWcStaBandwidthRx_Object = MibTableColumn
fgWcStaBandwidthRx = _FgWcStaBandwidthRx_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 16),
    _FgWcStaBandwidthRx_Type()
)
fgWcStaBandwidthRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaBandwidthRx.setStatus("current")
_FgWcStaChannel_Type = FgWcWtpRadioChannelNumber
_FgWcStaChannel_Object = MibTableColumn
fgWcStaChannel = _FgWcStaChannel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 17),
    _FgWcStaChannel_Type()
)
fgWcStaChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaChannel.setStatus("current")
_FgWcStaRadioType_Type = FgWcWtpRadioType
_FgWcStaRadioType_Object = MibTableColumn
fgWcStaRadioType = _FgWcStaRadioType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 18),
    _FgWcStaRadioType_Type()
)
fgWcStaRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaRadioType.setStatus("current")
_FgWcStaSecurity_Type = FgWcWlanSecurityType
_FgWcStaSecurity_Object = MibTableColumn
fgWcStaSecurity = _FgWcStaSecurity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 19),
    _FgWcStaSecurity_Type()
)
fgWcStaSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaSecurity.setStatus("current")
_FgWcStaEncrypt_Type = FgWcWlanEncryptionType
_FgWcStaEncrypt_Object = MibTableColumn
fgWcStaEncrypt = _FgWcStaEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 20),
    _FgWcStaEncrypt_Type()
)
fgWcStaEncrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaEncrypt.setStatus("current")


class _FgWcStaOnline_Type(Integer32):
    """Custom type fgWcStaOnline based on Integer32"""
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


_FgWcStaOnline_Type.__name__ = "Integer32"
_FgWcStaOnline_Object = MibTableColumn
fgWcStaOnline = _FgWcStaOnline_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 21),
    _FgWcStaOnline_Type()
)
fgWcStaOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaOnline.setStatus("current")
_FgFc_ObjectIdentity = ObjectIdentity
fgFc = _FgFc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 15)
)
_FgFcTrapObjects_ObjectIdentity = ObjectIdentity
fgFcTrapObjects = _FgFcTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 15, 1)
)
_FgFcSwVdom_Type = FgVdIndex
_FgFcSwVdom_Object = MibScalar
fgFcSwVdom = _FgFcSwVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 15, 1, 1),
    _FgFcSwVdom_Type()
)
fgFcSwVdom.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgFcSwVdom.setStatus("current")


class _FgFcSwSerial_Type(DisplayString):
    """Custom type fgFcSwSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgFcSwSerial_Type.__name__ = "DisplayString"
_FgFcSwSerial_Object = MibScalar
fgFcSwSerial = _FgFcSwSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 15, 1, 2),
    _FgFcSwSerial_Type()
)
fgFcSwSerial.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgFcSwSerial.setStatus("current")


class _FgFcSwName_Type(DisplayString):
    """Custom type fgFcSwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgFcSwName_Type.__name__ = "DisplayString"
_FgFcSwName_Object = MibScalar
fgFcSwName = _FgFcSwName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 15, 1, 3),
    _FgFcSwName_Type()
)
fgFcSwName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgFcSwName.setStatus("current")
_FgServerLoadBalance_ObjectIdentity = ObjectIdentity
fgServerLoadBalance = _FgServerLoadBalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 16)
)
_FgServerLoadBalanceTrapObjects_ObjectIdentity = ObjectIdentity
fgServerLoadBalanceTrapObjects = _FgServerLoadBalanceTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 16, 1)
)
_FgServerLoadBalanceRealServerAddress_Type = IpAddress
_FgServerLoadBalanceRealServerAddress_Object = MibScalar
fgServerLoadBalanceRealServerAddress = _FgServerLoadBalanceRealServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 16, 1, 1),
    _FgServerLoadBalanceRealServerAddress_Type()
)
fgServerLoadBalanceRealServerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgServerLoadBalanceRealServerAddress.setStatus("current")


class _FgServerLoadBalanceVirtualServerName_Type(DisplayString):
    """Custom type fgServerLoadBalanceVirtualServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FgServerLoadBalanceVirtualServerName_Type.__name__ = "DisplayString"
_FgServerLoadBalanceVirtualServerName_Object = MibScalar
fgServerLoadBalanceVirtualServerName = _FgServerLoadBalanceVirtualServerName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 16, 1, 2),
    _FgServerLoadBalanceVirtualServerName_Type()
)
fgServerLoadBalanceVirtualServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgServerLoadBalanceVirtualServerName.setStatus("current")
_FgUsbModemInfo_ObjectIdentity = ObjectIdentity
fgUsbModemInfo = _FgUsbModemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 17)
)
_FgUsbModemInfoObjects_ObjectIdentity = ObjectIdentity
fgUsbModemInfoObjects = _FgUsbModemInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 17, 1)
)


class _FgUsbModemSignalStrength_Type(Integer32):
    """Custom type fgUsbModemSignalStrength based on Integer32"""
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
        *(("level0", 0),
          ("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4))
    )


_FgUsbModemSignalStrength_Type.__name__ = "Integer32"
_FgUsbModemSignalStrength_Object = MibScalar
fgUsbModemSignalStrength = _FgUsbModemSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 17, 1, 1),
    _FgUsbModemSignalStrength_Type()
)
fgUsbModemSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbModemSignalStrength.setStatus("current")


class _FgUsbModemStatus_Type(Integer32):
    """Custom type fgUsbModemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 0))
    )


_FgUsbModemStatus_Type.__name__ = "Integer32"
_FgUsbModemStatus_Object = MibScalar
fgUsbModemStatus = _FgUsbModemStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 17, 1, 2),
    _FgUsbModemStatus_Type()
)
fgUsbModemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbModemStatus.setStatus("current")


class _FgUsbModemSimState_Type(Integer32):
    """Custom type fgUsbModemSimState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_FgUsbModemSimState_Type.__name__ = "Integer32"
_FgUsbModemSimState_Object = MibScalar
fgUsbModemSimState = _FgUsbModemSimState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 17, 1, 3),
    _FgUsbModemSimState_Type()
)
fgUsbModemSimState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbModemSimState.setStatus("current")


class _FgUsbModemVendor_Type(DisplayString):
    """Custom type fgUsbModemVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FgUsbModemVendor_Type.__name__ = "DisplayString"
_FgUsbModemVendor_Object = MibScalar
fgUsbModemVendor = _FgUsbModemVendor_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 17, 1, 4),
    _FgUsbModemVendor_Type()
)
fgUsbModemVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbModemVendor.setStatus("current")


class _FgUsbModemProduct_Type(DisplayString):
    """Custom type fgUsbModemProduct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FgUsbModemProduct_Type.__name__ = "DisplayString"
_FgUsbModemProduct_Object = MibScalar
fgUsbModemProduct = _FgUsbModemProduct_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 17, 1, 5),
    _FgUsbModemProduct_Type()
)
fgUsbModemProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbModemProduct.setStatus("current")


class _FgUsbModemNetwork_Type(Integer32):
    """Custom type fgUsbModemNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("network3G", 0),
          ("networkLTE", 1))
    )


_FgUsbModemNetwork_Type.__name__ = "Integer32"
_FgUsbModemNetwork_Object = MibScalar
fgUsbModemNetwork = _FgUsbModemNetwork_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 17, 1, 6),
    _FgUsbModemNetwork_Type()
)
fgUsbModemNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbModemNetwork.setStatus("current")


class _FgUsbModemId_Type(DisplayString):
    """Custom type fgUsbModemId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FgUsbModemId_Type.__name__ = "DisplayString"
_FgUsbModemId_Object = MibScalar
fgUsbModemId = _FgUsbModemId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 17, 1, 7),
    _FgUsbModemId_Type()
)
fgUsbModemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbModemId.setStatus("current")


class _FgUsbModemSimId_Type(DisplayString):
    """Custom type fgUsbModemSimId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FgUsbModemSimId_Type.__name__ = "DisplayString"
_FgUsbModemSimId_Object = MibScalar
fgUsbModemSimId = _FgUsbModemSimId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 17, 1, 8),
    _FgUsbModemSimId_Type()
)
fgUsbModemSimId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbModemSimId.setStatus("current")
_FgDevice_ObjectIdentity = ObjectIdentity
fgDevice = _FgDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 18)
)
_FgDeviceTrapObjects_ObjectIdentity = ObjectIdentity
fgDeviceTrapObjects = _FgDeviceTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 18, 1)
)


class _FgDeviceMacAddress_Type(DisplayString):
    """Custom type fgDeviceMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FgDeviceMacAddress_Type.__name__ = "DisplayString"
_FgDeviceMacAddress_Object = MibScalar
fgDeviceMacAddress = _FgDeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 18, 1, 1),
    _FgDeviceMacAddress_Type()
)
fgDeviceMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgDeviceMacAddress.setStatus("current")
_FgDeviceCreated_Type = Gauge32
_FgDeviceCreated_Object = MibScalar
fgDeviceCreated = _FgDeviceCreated_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 18, 1, 2),
    _FgDeviceCreated_Type()
)
fgDeviceCreated.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgDeviceCreated.setStatus("current")
_FgDeviceLastSeen_Type = Gauge32
_FgDeviceLastSeen_Object = MibScalar
fgDeviceLastSeen = _FgDeviceLastSeen_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 18, 1, 3),
    _FgDeviceLastSeen_Type()
)
fgDeviceLastSeen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgDeviceLastSeen.setStatus("current")
_FgMibConformance_ObjectIdentity = ObjectIdentity
fgMibConformance = _FgMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100)
)
fnAdminEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgAdminEntry")
)
fgAdminEntry.setIndexNames(*fnAdminEntry.getIndexNames())
ifEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgIntfEntry")
)
fgIntfEntry.setIndexNames(*ifEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgAvStatsEntry")
)
fgAvStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgIpsStatsEntry")
)
fgIpsStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgWebfilterStatsEntry")
)
fgWebfilterStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgFortiGuardStatsEntry")
)
fgFortiGuardStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgApHTTPStatsEntry")
)
fgApHTTPStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgApSMTPStatsEntry")
)
fgApSMTPStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgApPOP3StatsEntry")
)
fgApPOP3StatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgApIMAPStatsEntry")
)
fgApIMAPStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgApNNTPStatsEntry")
)
fgApNNTPStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgApIMStatsEntry")
)
fgApIMStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgApSIPStatsEntry")
)
fgApSIPStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgAppVoIPStatsEntry")
)
fgAppVoIPStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgAppP2PStatsEntry")
)
fgAppP2PStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgAppIMStatsEntry")
)
fgAppIMStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgApFTPStatsEntry")
)
fgApFTPStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgIpSessStatsEntry")
)
fgIpSessStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgIp6SessStatsEntry")
)
fgIp6SessStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgVpnSslStatsEntry")
)
fgVpnSslStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())

# Managed Objects groups

fgFmTrapObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 2)
)
fgFmTrapObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgManIfIp"),
        ("FORTINET-FORTIGATE-MIB", "fgManIfMask"),
        ("FORTINET-FORTIGATE-MIB", "fgManIfIp6"))
)
if mibBuilder.loadTexts:
    fgFmTrapObjectGroup.setStatus("current")

fgAdminObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 3)
)
fgAdminObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgAdminIdleTimeout"),
        ("FORTINET-FORTIGATE-MIB", "fgAdminLcdProtection"))
)
if mibBuilder.loadTexts:
    fgAdminObjectGroup.setStatus("current")

fgSystemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 4)
)
fgSystemObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgSysVersion"),
        ("FORTINET-FORTIGATE-MIB", "fgSysCpuUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgSysMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgSysMemCapacity"),
        ("FORTINET-FORTIGATE-MIB", "fgSysDiskUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgSysDiskCapacity"),
        ("FORTINET-FORTIGATE-MIB", "fgSysSesCount"),
        ("FORTINET-FORTIGATE-MIB", "fgSysLowMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgSysLowMemCapacity"),
        ("FORTINET-FORTIGATE-MIB", "fgSysSesRate1"),
        ("FORTINET-FORTIGATE-MIB", "fgSysSesRate10"),
        ("FORTINET-FORTIGATE-MIB", "fgSysSesRate30"),
        ("FORTINET-FORTIGATE-MIB", "fgSysSesRate60"),
        ("FORTINET-FORTIGATE-MIB", "fgSysSes6Count"),
        ("FORTINET-FORTIGATE-MIB", "fgSysSes6Rate1"),
        ("FORTINET-FORTIGATE-MIB", "fgSysSes6Rate10"),
        ("FORTINET-FORTIGATE-MIB", "fgSysSes6Rate30"),
        ("FORTINET-FORTIGATE-MIB", "fgSysSes6Rate60"),
        ("FORTINET-FORTIGATE-MIB", "fgSysUpTime"))
)
if mibBuilder.loadTexts:
    fgSystemObjectGroup.setStatus("current")

fgSoftwareObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 5)
)
fgSoftwareObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgSysVersionAv"),
        ("FORTINET-FORTIGATE-MIB", "fgSysVersionIps"))
)
if mibBuilder.loadTexts:
    fgSoftwareObjectGroup.setStatus("current")

fgHwSensorsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 6)
)
fgHwSensorsObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgHwSensorCount"),
        ("FORTINET-FORTIGATE-MIB", "fgHwSensorEntName"),
        ("FORTINET-FORTIGATE-MIB", "fgHwSensorEntValue"),
        ("FORTINET-FORTIGATE-MIB", "fgHwSensorEntAlarmStatus"))
)
if mibBuilder.loadTexts:
    fgHwSensorsObjectGroup.setStatus("current")

fgHighAvailabilityObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 7)
)
fgHighAvailabilityObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgHaSystemMode"),
        ("FORTINET-FORTIGATE-MIB", "fgHaGroupId"),
        ("FORTINET-FORTIGATE-MIB", "fgHaPriority"),
        ("FORTINET-FORTIGATE-MIB", "fgHaOverride"),
        ("FORTINET-FORTIGATE-MIB", "fgHaAutoSync"),
        ("FORTINET-FORTIGATE-MIB", "fgHaSchedule"),
        ("FORTINET-FORTIGATE-MIB", "fgHaGroupName"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsSerial"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsCpuUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsNetUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsSesCount"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsPktCount"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsByteCount"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsIdsCount"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsAvCount"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsHostname"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsSyncStatus"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsSyncDatimeSucc"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsSyncDatimeUnsucc"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsGlobalChecksum"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsMasterSerial"),
        ("FORTINET-FORTIGATE-MIB", "fgHaTrapMemberSerial"))
)
if mibBuilder.loadTexts:
    fgHighAvailabilityObjectGroup.setStatus("current")

fgVpnObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 8)
)
fgVpnObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgVpnDialupGateway"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnDialupLifetime"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnDialupTimeout"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnDialupSrcBegin"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnDialupSrcEnd"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnDialupDstAddr"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnDialupVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnDialupInOctets"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnDialupOutOctets"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntPhase1Name"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntPhase2Name"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntRemGwyIp"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntRemGwyPort"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntLocGwyIp"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntLocGwyPort"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntSelectorSrcBeginIp"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntSelectorSrcEndIp"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntSelectorSrcPort"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntSelectorDstBeginIp"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntSelectorDstEndIp"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntSelectorDstPort"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntSelectorProto"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntLifeSecs"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntLifeBytes"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntTimeout"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntInOctets"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntOutOctets"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntStatus"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslState"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslStatsLoginUsers"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslStatsMaxUsers"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslStatsActiveWebSessions"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslStatsMaxWebSessions"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslStatsActiveTunnels"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslStatsMaxTunnels"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslTunnelVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslTunnelUserName"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslTunnelSrcIp"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslTunnelIp"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslTunnelUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslTunnelBytesIn"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslTunnelBytesOut"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTrapLocalGateway"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTrapRemoteGateway"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTrapPhase1Name"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunnelUpCount"))
)
if mibBuilder.loadTexts:
    fgVpnObjectGroup.setStatus("current")

fgFirewallObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 9)
)
fgFirewallObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgFwPolPktCount"),
        ("FORTINET-FORTIGATE-MIB", "fgFwPolByteCount"),
        ("FORTINET-FORTIGATE-MIB", "fgFwUserNumber"),
        ("FORTINET-FORTIGATE-MIB", "fgFwPolPktCountHc"),
        ("FORTINET-FORTIGATE-MIB", "fgFwPolByteCountHc"),
        ("FORTINET-FORTIGATE-MIB", "fgFwUserAuthTimeout"),
        ("FORTINET-FORTIGATE-MIB", "fgFwUserName"),
        ("FORTINET-FORTIGATE-MIB", "fgFwUserAuth"),
        ("FORTINET-FORTIGATE-MIB", "fgFwUserState"),
        ("FORTINET-FORTIGATE-MIB", "fgFwUserVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgIpSessProto"),
        ("FORTINET-FORTIGATE-MIB", "fgIpSessFromAddr"),
        ("FORTINET-FORTIGATE-MIB", "fgIpSessFromPort"),
        ("FORTINET-FORTIGATE-MIB", "fgIpSessToAddr"),
        ("FORTINET-FORTIGATE-MIB", "fgIpSessToPort"),
        ("FORTINET-FORTIGATE-MIB", "fgIpSessExp"),
        ("FORTINET-FORTIGATE-MIB", "fgIpSessVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgIpSessNumber"),
        ("FORTINET-FORTIGATE-MIB", "fgIp6SessNumber"),
        ("FORTINET-FORTIGATE-MIB", "fgFwPol6PktCount"),
        ("FORTINET-FORTIGATE-MIB", "fgFwPol6ByteCount"),
        ("FORTINET-FORTIGATE-MIB", "fgFwPolLastUsed"),
        ("FORTINET-FORTIGATE-MIB", "fgFwPol6LastUsed"))
)
if mibBuilder.loadTexts:
    fgFirewallObjectGroup.setStatus("current")

fgAppServicesObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 10)
)
fgAppServicesObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgApHTTPReqProcessed"),
        ("FORTINET-FORTIGATE-MIB", "fgApSMTPReqProcessed"),
        ("FORTINET-FORTIGATE-MIB", "fgApSMTPSpamDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgApPOP3ReqProcessed"),
        ("FORTINET-FORTIGATE-MIB", "fgApPOP3SpamDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgApIMAPReqProcessed"),
        ("FORTINET-FORTIGATE-MIB", "fgApIMAPSpamDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgApNNTPReqProcessed"),
        ("FORTINET-FORTIGATE-MIB", "fgApIMUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgApIMMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgApIMReqProcessed"),
        ("FORTINET-FORTIGATE-MIB", "fgApSIPUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgApSIPMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgApSIPClientReg"),
        ("FORTINET-FORTIGATE-MIB", "fgApSIPCallHandling"),
        ("FORTINET-FORTIGATE-MIB", "fgApSIPServices"),
        ("FORTINET-FORTIGATE-MIB", "fgApSIPOtherReq"),
        ("FORTINET-FORTIGATE-MIB", "fgAppSuNumber"),
        ("FORTINET-FORTIGATE-MIB", "fgAppSuFileScanned"),
        ("FORTINET-FORTIGATE-MIB", "fgAppVoIPConn"),
        ("FORTINET-FORTIGATE-MIB", "fgAppVoIPCallBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAppP2PConnBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAppP2PProtEntBytes"),
        ("FORTINET-FORTIGATE-MIB", "fgAppP2PProtoEntLastReset"),
        ("FORTINET-FORTIGATE-MIB", "fgAppIMMessages"),
        ("FORTINET-FORTIGATE-MIB", "fgAppIMFileTransfered"),
        ("FORTINET-FORTIGATE-MIB", "fgAppIMFileTxBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAppIMConnBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgApFTPReqProcessed"),
        ("FORTINET-FORTIGATE-MIB", "fgApHTTPConnections"),
        ("FORTINET-FORTIGATE-MIB", "fgApFTPConnections"),
        ("FORTINET-FORTIGATE-MIB", "fgApSMTPConnections"),
        ("FORTINET-FORTIGATE-MIB", "fgApPOP3Connections"),
        ("FORTINET-FORTIGATE-MIB", "fgApIMAPConnections"),
        ("FORTINET-FORTIGATE-MIB", "fgApNNTPConnections"),
        ("FORTINET-FORTIGATE-MIB", "fgApHTTPMaxConnections"),
        ("FORTINET-FORTIGATE-MIB", "fgApFTPMaxConnections"),
        ("FORTINET-FORTIGATE-MIB", "fgApSMTPMaxConnections"),
        ("FORTINET-FORTIGATE-MIB", "fgApPOP3MaxConnections"),
        ("FORTINET-FORTIGATE-MIB", "fgApIMAPMaxConnections"),
        ("FORTINET-FORTIGATE-MIB", "fgApNNTPMaxConnections"))
)
if mibBuilder.loadTexts:
    fgAppServicesObjectGroup.setStatus("current")

fgAntivirusObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 11)
)
fgAntivirusObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgAvVirusDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgAvVirusBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAvHTTPVirusDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgAvHTTPVirusBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAvSMTPVirusDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgAvSMTPVirusBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAvPOP3VirusDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgAvPOP3VirusBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAvIMAPVirusDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgAvIMAPVirusBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAvFTPVirusDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgAvFTPVirusBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAvIMVirusDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgAvIMVirusBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAvNNTPVirusDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgAvNNTPVirusBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAvOversizedDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgAvOversizedBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAvTrapVirName"))
)
if mibBuilder.loadTexts:
    fgAntivirusObjectGroup.setStatus("current")

fgIntrusionPrevtObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 12)
)
fgIntrusionPrevtObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgIpsTrapSigId"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsTrapSrcIp"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsTrapSigMsg"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsIntrusionsDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsIntrusionsBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsCritSevDetections"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsHighSevDetections"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsMedSevDetections"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsLowSevDetections"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsInfoSevDetections"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsSignatureDetections"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsAnomalyDetections"))
)
if mibBuilder.loadTexts:
    fgIntrusionPrevtObjectGroup.setStatus("current")

fgWebFilterObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 13)
)
fgWebFilterObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgWfHTTPBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgWfHTTPSBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgWfHTTPURLBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgWfHTTPSURLBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgWfActiveXBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgWfCookieBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgWfAppletBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgFgWfHTTPExamined"),
        ("FORTINET-FORTIGATE-MIB", "fgFgWfHTTPSExamined"),
        ("FORTINET-FORTIGATE-MIB", "fgFgWfHTTPAllowed"),
        ("FORTINET-FORTIGATE-MIB", "fgFgWfHTTPSAllowed"),
        ("FORTINET-FORTIGATE-MIB", "fgFgWfHTTPBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgFgWfHTTPSBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgFgWfHTTPLogged"),
        ("FORTINET-FORTIGATE-MIB", "fgFgWfHTTPSLogged"),
        ("FORTINET-FORTIGATE-MIB", "fgFgWfHTTPOverridden"),
        ("FORTINET-FORTIGATE-MIB", "fgFgWfHTTPSOverridden"))
)
if mibBuilder.loadTexts:
    fgWebFilterObjectGroup.setStatus("current")

fgVirtualDomainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 14)
)
fgVirtualDomainObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgVdNumber"),
        ("FORTINET-FORTIGATE-MIB", "fgVdMaxVdoms"),
        ("FORTINET-FORTIGATE-MIB", "fgVdEnabled"),
        ("FORTINET-FORTIGATE-MIB", "fgVdEntName"),
        ("FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
        ("FORTINET-FORTIGATE-MIB", "fgVdEntOpMode"),
        ("FORTINET-FORTIGATE-MIB", "fgVdTpMgmtAddrType"),
        ("FORTINET-FORTIGATE-MIB", "fgVdTpMgmtAddr"),
        ("FORTINET-FORTIGATE-MIB", "fgVdEntCpuUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgVdEntMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgVdEntSesCount"),
        ("FORTINET-FORTIGATE-MIB", "fgVdEntSesRate"),
        ("FORTINET-FORTIGATE-MIB", "fgVdTpMgmtMask"),
        ("FORTINET-FORTIGATE-MIB", "fgVdEntHaState"))
)
if mibBuilder.loadTexts:
    fgVirtualDomainObjectGroup.setStatus("current")

fgAdministrationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 15)
)
fgAdministrationObjectGroup.setObjects(
    ("FORTINET-FORTIGATE-MIB", "fgAdminVdom")
)
if mibBuilder.loadTexts:
    fgAdministrationObjectGroup.setStatus("current")

fgIntfObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 16)
)
fgIntfObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgIntfEntVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfVrrpCount"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfVrrpEntVrId"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfVrrpEntGrpId"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfVrrpEntIfName"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfVrrpEntState"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfVrrpEntVrIp"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfVlanHbCount"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfVlanHbEntIfName"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfVlanHbEntSerial"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfVlanHbEntState"))
)
if mibBuilder.loadTexts:
    fgIntfObjectGroup.setStatus("current")

fgProcessorsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 17)
)
fgProcessorsObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgProcessorCount"),
        ("FORTINET-FORTIGATE-MIB", "fgProcessorUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgProcessorUsage5sec"),
        ("FORTINET-FORTIGATE-MIB", "fgProcessorType"),
        ("FORTINET-FORTIGATE-MIB", "fgProcessorContainedIn"),
        ("FORTINET-FORTIGATE-MIB", "fgProcessorPktRxCount"),
        ("FORTINET-FORTIGATE-MIB", "fgProcessorPktTxCount"),
        ("FORTINET-FORTIGATE-MIB", "fgProcessorPktDroppedCount"),
        ("FORTINET-FORTIGATE-MIB", "fgProcessorUserUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgProcessorSysUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgProcessorModuleCount"),
        ("FORTINET-FORTIGATE-MIB", "fgProcModType"),
        ("FORTINET-FORTIGATE-MIB", "fgProcModName"),
        ("FORTINET-FORTIGATE-MIB", "fgProcModDescr"),
        ("FORTINET-FORTIGATE-MIB", "fgProcModProcessorCount"),
        ("FORTINET-FORTIGATE-MIB", "fgProcModMemCapacity"),
        ("FORTINET-FORTIGATE-MIB", "fgProcModMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgProcModSessionCount"),
        ("FORTINET-FORTIGATE-MIB", "fgProcModSACount"))
)
if mibBuilder.loadTexts:
    fgProcessorsObjectGroup.setStatus("current")

fgExplicitProxyObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 20)
)
fgExplicitProxyObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgExplicitProxyUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyRequests"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyUsers"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxySessions"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyVirus"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyBannedWords"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyPolicy"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyOversized"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyArchNest"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyArchSize"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyArchEncrypted"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyArchMultiPart"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyArchUnsupported"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyArchBomb"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyArchCorrupt"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyFilteredApplets"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyFilteredActiveX"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyFilteredJScript"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyFilteredJS"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyFilteredVBS"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyFilteredOthScript"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyBlockedDLP"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyBlockedConType"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyExaminedURLs"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyAllowedURLs"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyBlockedURLs"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyLoggedURLs"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyOverriddenURLs"))
)
if mibBuilder.loadTexts:
    fgExplicitProxyObjectGroup.setStatus("current")

fgWebCacheObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 21)
)
fgWebCacheObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgWebCacheUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgWebCacheRAMLimit"),
        ("FORTINET-FORTIGATE-MIB", "fgWebCacheRAMUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgWebCacheRAMHits"),
        ("FORTINET-FORTIGATE-MIB", "fgWebCacheRAMMisses"),
        ("FORTINET-FORTIGATE-MIB", "fgWebCacheRequests"),
        ("FORTINET-FORTIGATE-MIB", "fgWebCacheBypass"),
        ("FORTINET-FORTIGATE-MIB", "fgWebCacheDiskLimit"),
        ("FORTINET-FORTIGATE-MIB", "fgWebCacheDiskUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgWebCacheDiskHits"),
        ("FORTINET-FORTIGATE-MIB", "fgWebCacheDiskMisses"))
)
if mibBuilder.loadTexts:
    fgWebCacheObjectGroup.setStatus("current")

fgWanOptObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 22)
)
fgWanOptObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgMemCacheLimit"),
        ("FORTINET-FORTIGATE-MIB", "fgMemCacheUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgMemCacheHits"),
        ("FORTINET-FORTIGATE-MIB", "fgMemCacheMisses"),
        ("FORTINET-FORTIGATE-MIB", "fgByteCacheRAMLimit"),
        ("FORTINET-FORTIGATE-MIB", "fgByteCacheRAMUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptReductionRate"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptLanTraffic"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptWanTraffic"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptLanInTraffic"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptLanOutTraffic"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptWanInTraffic"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptWanOutTraffic"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptTunnels"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptLANBytesIn"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptLANBytesOut"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptWANBytesIn"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptWANBytesOut"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptDiskLimit"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptDiskUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptDiskHits"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptDiskMisses"))
)
if mibBuilder.loadTexts:
    fgWanOptObjectGroup.setStatus("current")

fgObsoleteAppServicesObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 23)
)
fgObsoleteAppServicesObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgApHTTPUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgApHTTPMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgApSMTPUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgApSMTPMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgApPOP3UpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgApPOP3MemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgApIMAPUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgApIMAPMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgApNNTPUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgApNNTPMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgApFTPUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgApFTPMemUsage"))
)
if mibBuilder.loadTexts:
    fgObsoleteAppServicesObjectGroup.setStatus("deprecated")

fgSystemAdvancedObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 24)
)
fgSystemAdvancedObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgSIAdvMemPageCache"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvMemCacheActive"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvMemCacheInactive"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvMemBuffer"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvMemEnterKerConsThrsh"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvMemLeaveKerConsThrsh"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvMemEnterProxyConsThrsh"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvMemLeaveProxyConsThrsh"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvSesEphemeralCount"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvSesEphemeralLimit"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvSesClashCount"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvSesExpCount"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvSesSyncQFCount"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvSesAcceptQFCount"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvSesNoListenerCount"))
)
if mibBuilder.loadTexts:
    fgSystemAdvancedObjectGroup.setStatus("current")

fgWcObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 25)
)
fgWcObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgWcApVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgWcApSerial"),
        ("FORTINET-FORTIGATE-MIB", "fgWcApName"),
        ("FORTINET-FORTIGATE-MIB", "fgWcInfoName"),
        ("FORTINET-FORTIGATE-MIB", "fgWcInfoLocation"),
        ("FORTINET-FORTIGATE-MIB", "fgWcInfoWtpCapacity"),
        ("FORTINET-FORTIGATE-MIB", "fgWcInfoWtpManaged"),
        ("FORTINET-FORTIGATE-MIB", "fgWcInfoWtpSessions"),
        ("FORTINET-FORTIGATE-MIB", "fgWcInfoStationCapacity"),
        ("FORTINET-FORTIGATE-MIB", "fgWcInfoStationCount"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanSsid"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanBroadcastSsid"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanSecurity"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanEncryption"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanAuthentication"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanRadiusServer"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanUserGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanLocalBridging"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanVlanId"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanMeshBackhaul"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanStationCapacity"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanStationCount"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfilePlatform"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileDataChannelDtlsPolicy"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileCountryString"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioMode"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioApScan"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioWidsProfile"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioDarrp"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioFrequencyHandoff"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioApHandoff"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioBeaconInterval"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioDtimPeriod"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioBand"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioChannelBonding"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioChannel"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioAutoTxPowerControl"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioAutoTxPowerLow"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioAutoTxPowerHigh"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioTxPowerLevel"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioVaps"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioStationCapacity"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioChannelWidth"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigWtpAdmin"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigWtpName"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigWtpLocation"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigWtpProfile"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigRadioEnable"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigRadioAutoTxPowerControl"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigRadioAutoTxPowerLow"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigRadioAutoTxPowerHigh"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigRadioTxPowerLevel"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigRadioBand"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigRadioApScan"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigVapAll"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigVaps"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpIpAddressType"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpIpAddress"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpLocalIpAddressType"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpLocalIpAddress"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpBaseMacAddress"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionConnectionState"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpDaemonUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpSessionUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpProfileName"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpModelNumber"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpHwVersion"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpSwVersion"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpBootVersion"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpRegionCode"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpStationCount"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpByteRxCount"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpByteTxCount"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpCpuUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpMemoryUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpMemoryCapacity"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionRadioMode"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionRadioBaseBssid"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionRadioCountryString"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionRadioCountryCode"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionRadioOperatingChannel"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionRadioOperatingPower"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionRadioStationCount"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionVapSsid"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionVapStationCount"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionVapByteRxCount"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionVapByteTxCount"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaWlan"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaWtpId"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaRadioId"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaVlanId"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaIpAddressType"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaIpAddress"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaVci"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaHost"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaUser"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaSignal"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaNoise"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaIdle"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaBandwidthTx"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaBandwidthRx"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaChannel"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaRadioType"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaSecurity"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaEncrypt"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaOnline"))
)
if mibBuilder.loadTexts:
    fgWcObjectGroup.setStatus("current")

fgFcObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 26)
)
fgFcObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgFcSwVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgFcSwSerial"),
        ("FORTINET-FORTIGATE-MIB", "fgFcSwName"))
)
if mibBuilder.loadTexts:
    fgFcObjectGroup.setStatus("current")

fgServerLoadBalanceObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 27)
)
fgServerLoadBalanceObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgServerLoadBalanceRealServerAddress"),
        ("FORTINET-FORTIGATE-MIB", "fgServerLoadBalanceVirtualServerName"))
)
if mibBuilder.loadTexts:
    fgServerLoadBalanceObjectGroup.setStatus("current")

fgUsbportsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 28)
)
fgUsbportsObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgUsbportCount"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbportPlugged"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbportVersion"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbportClass"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbportVendId"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbportProdId"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbportRevision"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbportManufacturer"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbportProduct"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbportSerial"))
)
if mibBuilder.loadTexts:
    fgUsbportsObjectGroup.setStatus("current")

fgUsbModemInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 29)
)
fgUsbModemInfoGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgUsbModemSignalStrength"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbModemStatus"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbModemSimState"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbModemVendor"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbModemProduct"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbModemNetwork"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbModemId"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbModemSimId"))
)
if mibBuilder.loadTexts:
    fgUsbModemInfoGroup.setStatus("current")

fgDeviceObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 30)
)
fgDeviceObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgDeviceMacAddress"),
        ("FORTINET-FORTIGATE-MIB", "fgDeviceCreated"),
        ("FORTINET-FORTIGATE-MIB", "fgDeviceLastSeen"))
)
if mibBuilder.loadTexts:
    fgDeviceObjectGroup.setStatus("current")

fgLinkMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 31)
)
fgLinkMonitorGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgLinkMonitorNumber"),
        ("FORTINET-FORTIGATE-MIB", "fgLinkMonitorName"),
        ("FORTINET-FORTIGATE-MIB", "fgLinkMonitorState"),
        ("FORTINET-FORTIGATE-MIB", "fgLinkMonitorLatency"),
        ("FORTINET-FORTIGATE-MIB", "fgLinkMonitorJitter"),
        ("FORTINET-FORTIGATE-MIB", "fgLinkMonitorPacketSend"),
        ("FORTINET-FORTIGATE-MIB", "fgLinkMonitorPacketRecv"),
        ("FORTINET-FORTIGATE-MIB", "fgLinkMonitorPacketLoss"),
        ("FORTINET-FORTIGATE-MIB", "fgLinkMonitorVdom"))
)
if mibBuilder.loadTexts:
    fgLinkMonitorGroup.setStatus("current")


# Notification objects

fgTrapVpnTunUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 301)
)
fgTrapVpnTunUp.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTrapLocalGateway"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTrapRemoteGateway"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTrapPhase1Name"))
)
if mibBuilder.loadTexts:
    fgTrapVpnTunUp.setStatus(
        "current"
    )

fgTrapVpnTunDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 302)
)
fgTrapVpnTunDown.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTrapLocalGateway"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTrapRemoteGateway"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTrapPhase1Name"))
)
if mibBuilder.loadTexts:
    fgTrapVpnTunDown.setStatus(
        "current"
    )

fgTrapHaSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 401)
)
fgTrapHaSwitch.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fgTrapHaSwitch.setStatus(
        "current"
    )

fgTrapHaStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 402)
)
fgTrapHaStateChange.setObjects(
    ("FORTINET-CORE-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fgTrapHaStateChange.setStatus(
        "deprecated"
    )

fgTrapHaHBFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 403)
)
fgTrapHaHBFail.setObjects(
    ("FORTINET-CORE-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fgTrapHaHBFail.setStatus(
        "current"
    )

fgTrapHaMemberDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 404)
)
fgTrapHaMemberDown.setObjects(
    ("FORTINET-CORE-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fgTrapHaMemberDown.setStatus(
        "current"
    )

fgTrapHaMemberUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 405)
)
fgTrapHaMemberUp.setObjects(
    ("FORTINET-CORE-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fgTrapHaMemberUp.setStatus(
        "current"
    )

fgTrapIpsSignature = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 503)
)
fgTrapIpsSignature.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsTrapSigId"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsTrapSrcIp"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsTrapSigMsg"))
)
if mibBuilder.loadTexts:
    fgTrapIpsSignature.setStatus(
        "current"
    )

fgTrapIpsAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 504)
)
fgTrapIpsAnomaly.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsTrapSigId"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsTrapSrcIp"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsTrapSigMsg"))
)
if mibBuilder.loadTexts:
    fgTrapIpsAnomaly.setStatus(
        "current"
    )

fgTrapIpsPkgUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 505)
)
fgTrapIpsPkgUpdate.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fgTrapIpsPkgUpdate.setStatus(
        "current"
    )

fgTrapIpsFailOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 506)
)
fgTrapIpsFailOpen.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fgTrapIpsFailOpen.setStatus(
        "current"
    )

fgTrapAvVirus = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 601)
)
fgTrapAvVirus.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgAvTrapVirName"))
)
if mibBuilder.loadTexts:
    fgTrapAvVirus.setStatus(
        "current"
    )

fgTrapAvOversize = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 602)
)
fgTrapAvOversize.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fgTrapAvOversize.setStatus(
        "current"
    )

fgTrapAvPattern = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 603)
)
fgTrapAvPattern.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fgTrapAvPattern.setStatus(
        "current"
    )

fgTrapAvFragmented = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 604)
)
fgTrapAvFragmented.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fgTrapAvFragmented.setStatus(
        "current"
    )

fgTrapAvEnterConserve = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 605)
)
fgTrapAvEnterConserve.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fgTrapAvEnterConserve.setStatus(
        "current"
    )

fgTrapAvBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 606)
)
fgTrapAvBypass.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fgTrapAvBypass.setStatus(
        "current"
    )

fgTrapAvOversizePass = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 607)
)
fgTrapAvOversizePass.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fgTrapAvOversizePass.setStatus(
        "current"
    )

fgTrapAvOversizeBlock = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 608)
)
fgTrapAvOversizeBlock.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fgTrapAvOversizeBlock.setStatus(
        "current"
    )

fgTrapFazDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 701)
)
fgTrapFazDisconnect.setObjects(
    ("FORTINET-CORE-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fgTrapFazDisconnect.setStatus(
        "current"
    )

fgTrapWcApUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 801)
)
fgTrapWcApUp.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgWcApVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgWcApSerial"),
        ("FORTINET-FORTIGATE-MIB", "fgWcApName"))
)
if mibBuilder.loadTexts:
    fgTrapWcApUp.setStatus(
        "current"
    )

fgTrapWcApDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 802)
)
fgTrapWcApDown.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgWcApVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgWcApSerial"),
        ("FORTINET-FORTIGATE-MIB", "fgWcApName"))
)
if mibBuilder.loadTexts:
    fgTrapWcApDown.setStatus(
        "current"
    )

fgTrapFcSwUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 901)
)
fgTrapFcSwUp.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgFcSwVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgFcSwSerial"),
        ("FORTINET-FORTIGATE-MIB", "fgFcSwName"))
)
if mibBuilder.loadTexts:
    fgTrapFcSwUp.setStatus(
        "current"
    )

fgTrapFcSwDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 902)
)
fgTrapFcSwDown.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgFcSwVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgFcSwSerial"),
        ("FORTINET-FORTIGATE-MIB", "fgFcSwName"))
)
if mibBuilder.loadTexts:
    fgTrapFcSwDown.setStatus(
        "current"
    )

fgTrapServerLoadBalanceRealServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 1101)
)
fgTrapServerLoadBalanceRealServerDown.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgServerLoadBalanceRealServerAddress"),
        ("FORTINET-FORTIGATE-MIB", "fgServerLoadBalanceVirtualServerName"))
)
if mibBuilder.loadTexts:
    fgTrapServerLoadBalanceRealServerDown.setStatus(
        "current"
    )

fgTrapDeviceNew = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 1201)
)
fgTrapDeviceNew.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
        ("FORTINET-FORTIGATE-MIB", "fgDeviceCreated"),
        ("FORTINET-FORTIGATE-MIB", "fgDeviceLastSeen"),
        ("FORTINET-FORTIGATE-MIB", "fgDeviceMacAddress"))
)
if mibBuilder.loadTexts:
    fgTrapDeviceNew.setStatus(
        "current"
    )

fgFmTrapDeployComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 0, 1000)
)
fgFmTrapDeployComplete.setObjects(
    ("FORTINET-CORE-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fgFmTrapDeployComplete.setStatus(
        "current"
    )

fgFmTrapDeployInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 0, 1002)
)
fgFmTrapDeployInProgress.setObjects(
    ("FORTINET-CORE-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fgFmTrapDeployInProgress.setStatus(
        "current"
    )

fgFmTrapConfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 0, 1003)
)
fgFmTrapConfChange.setObjects(
    ("FORTINET-CORE-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fgFmTrapConfChange.setStatus(
        "current"
    )

fgFmTrapIfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 0, 1004)
)
fgFmTrapIfChange.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("IF-MIB", "ifName"),
        ("FORTINET-FORTIGATE-MIB", "fgManIfIp"),
        ("FORTINET-FORTIGATE-MIB", "fgManIfMask"),
        ("FORTINET-FORTIGATE-MIB", "fgManIfIp6"))
)
if mibBuilder.loadTexts:
    fgFmTrapIfChange.setStatus(
        "current"
    )


# Notifications groups

fgFmTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 1)
)
fgFmTrapGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgFmTrapDeployComplete"),
        ("FORTINET-FORTIGATE-MIB", "fgFmTrapDeployInProgress"),
        ("FORTINET-FORTIGATE-MIB", "fgFmTrapConfChange"),
        ("FORTINET-FORTIGATE-MIB", "fgFmTrapIfChange"))
)
if mibBuilder.loadTexts:
    fgFmTrapGroup.setStatus(
        "current"
    )

fgNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 18)
)
fgNotificationGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgTrapVpnTunUp"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapVpnTunDown"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapHaSwitch"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapHaHBFail"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapHaMemberDown"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapHaMemberUp"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapIpsSignature"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapIpsAnomaly"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapIpsPkgUpdate"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapIpsFailOpen"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapAvVirus"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapAvOversize"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapAvPattern"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapAvFragmented"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapAvEnterConserve"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapAvBypass"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapAvOversizePass"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapAvOversizeBlock"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapFazDisconnect"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapWcApUp"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapWcApDown"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapDeviceNew"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapFcSwUp"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapFcSwDown"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapServerLoadBalanceRealServerDown"))
)
if mibBuilder.loadTexts:
    fgNotificationGroup.setStatus(
        "current"
    )

fgObsoleteNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 19)
)
fgObsoleteNotificationsGroup.setObjects(
    ("FORTINET-FORTIGATE-MIB", "fgTrapHaStateChange")
)
if mibBuilder.loadTexts:
    fgObsoleteNotificationsGroup.setStatus(
        "deprecated"
    )


# Agent capabilities


# Module compliance

fgMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 100)
)
if mibBuilder.loadTexts:
    fgMIBCompliance.setStatus(
        "current"
    )

fg300MibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 101)
)
if mibBuilder.loadTexts:
    fg300MibCompliance.setStatus(
        "deprecated"
    )

fgObsolteMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 102)
)
if mibBuilder.loadTexts:
    fgObsolteMIBCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORTINET-FORTIGATE-MIB",
    **{"FgVdIndex": FgVdIndex,
       "FgOpMode": FgOpMode,
       "FgHaMode": FgHaMode,
       "FgHaState": FgHaState,
       "FgHaLBSchedule": FgHaLBSchedule,
       "FgAdminPermLevel": FgAdminPermLevel,
       "FgFwUserAuthType": FgFwUserAuthType,
       "FgSessProto": FgSessProto,
       "FgP2PProto": FgP2PProto,
       "FgScanAvDisposition": FgScanAvDisposition,
       "FgWanOptProtocols": FgWanOptProtocols,
       "FgWanOptHistPeriods": FgWanOptHistPeriods,
       "FgHaStatsSyncStatusType": FgHaStatsSyncStatusType,
       "FgWcWlanSecurityType": FgWcWlanSecurityType,
       "FgWcWlanAuthenticationType": FgWcWlanAuthenticationType,
       "FgWcWlanEncryptionType": FgWcWlanEncryptionType,
       "FgWcWtpRadioId": FgWcWtpRadioId,
       "FgWcWtpRadioType": FgWcWtpRadioType,
       "FgWcWtpChannelWidthType": FgWcWtpChannelWidthType,
       "FgWcWtpRadioBandType": FgWcWtpRadioBandType,
       "FgWcWtpRadioChannelNumber": FgWcWtpRadioChannelNumber,
       "FgWcWtpRadioMode": FgWcWtpRadioMode,
       "FgWcCountryString": FgWcCountryString,
       "fnFortiGateMib": fnFortiGateMib,
       "fgModel": fgModel,
       "fgtVM64": fgtVM64,
       "fgtVM64VMX": fgtVM64VMX,
       "fgtVM64SVM": fgtVM64SVM,
       "fgtVM64XEN": fgtVM64XEN,
       "fgtVM64AWS": fgtVM64AWS,
       "fgtVM64AWSONDEMAND": fgtVM64AWSONDEMAND,
       "fgtVM64KVm": fgtVM64KVm,
       "fgtVM64HV": fgtVM64HV,
       "fgt30D": fgt30D,
       "fgt30DPOE": fgt30DPOE,
       "fgt30E": fgt30E,
       "fwf30D": fwf30D,
       "fwf30DPOE": fwf30DPOE,
       "fwf30E": fwf30E,
       "fgt50E": fgt50E,
       "fwf50E": fwf50E,
       "fgt51E": fgt51E,
       "fwf51E": fwf51E,
       "fgt60D": fgt60D,
       "fgt60DPOE": fgt60DPOE,
       "fwf60D": fwf60D,
       "fw60DP": fw60DP,
       "fgtsoc3": fgtsoc3,
       "fgt90D": fgt90D,
       "fgt90DPOE": fgt90DPOE,
       "fwf90D": fwf90D,
       "fwf90DPOE": fwf90DPOE,
       "fgt94DPOE": fgt94DPOE,
       "fgt98DPOE": fgt98DPOE,
       "fgt92D": fgt92D,
       "fwf92D": fwf92D,
       "fgr90D": fgr90D,
       "fgr60D": fgr60D,
       "fgt70D": fgt70D,
       "fgt70DPOE": fgt70DPOE,
       "fgt80C": fgt80C,
       "fgt80CM": fgt80CM,
       "fgt80D": fgt80D,
       "fwf80CM": fwf80CM,
       "fwf81CM": fwf81CM,
       "fg900D": fg900D,
       "fgt100D": fgt100D,
       "fgt140D": fgt140D,
       "fgt140P": fgt140P,
       "fgt200D": fgt200D,
       "fgt240D": fgt240D,
       "fgt200DP": fgt200DP,
       "fgt240DP": fgt240DP,
       "fgt280D": fgt280D,
       "fgt3HD": fgt3HD,
       "fgt400D": fgt400D,
       "fgt500D": fgt500D,
       "fgt600C": fgt600C,
       "fgt600D": fgt600D,
       "fgt800C": fgt800C,
       "fgt800D": fgt800D,
       "fgt1000C": fgt1000C,
       "fgt1000D": fgt1000D,
       "fgt1200D": fgt1200D,
       "fgt1500D": fgt1500D,
       "fgt1500DT": fgt1500DT,
       "fgt3000D": fgt3000D,
       "fgt3100D": fgt3100D,
       "fgt3200D": fgt3200D,
       "fgt3240C": fgt3240C,
       "fgt3600C": fgt3600C,
       "fgt3700D": fgt3700D,
       "fgt3700DX": fgt3700DX,
       "fgt3810D": fgt3810D,
       "fgt3815D": fgt3815D,
       "fgt5001C": fgt5001C,
       "fgt5001D": fgt5001D,
       "fosVM64": fosVM64,
       "fosVM64KVM": fosVM64KVM,
       "fgTraps": fgTraps,
       "fgTrapPrefix": fgTrapPrefix,
       "fgTrapVpnTunUp": fgTrapVpnTunUp,
       "fgTrapVpnTunDown": fgTrapVpnTunDown,
       "fgTrapHaSwitch": fgTrapHaSwitch,
       "fgTrapHaStateChange": fgTrapHaStateChange,
       "fgTrapHaHBFail": fgTrapHaHBFail,
       "fgTrapHaMemberDown": fgTrapHaMemberDown,
       "fgTrapHaMemberUp": fgTrapHaMemberUp,
       "fgTrapIpsSignature": fgTrapIpsSignature,
       "fgTrapIpsAnomaly": fgTrapIpsAnomaly,
       "fgTrapIpsPkgUpdate": fgTrapIpsPkgUpdate,
       "fgTrapIpsFailOpen": fgTrapIpsFailOpen,
       "fgTrapAvVirus": fgTrapAvVirus,
       "fgTrapAvOversize": fgTrapAvOversize,
       "fgTrapAvPattern": fgTrapAvPattern,
       "fgTrapAvFragmented": fgTrapAvFragmented,
       "fgTrapAvEnterConserve": fgTrapAvEnterConserve,
       "fgTrapAvBypass": fgTrapAvBypass,
       "fgTrapAvOversizePass": fgTrapAvOversizePass,
       "fgTrapAvOversizeBlock": fgTrapAvOversizeBlock,
       "fgTrapFazDisconnect": fgTrapFazDisconnect,
       "fgTrapWcApUp": fgTrapWcApUp,
       "fgTrapWcApDown": fgTrapWcApDown,
       "fgTrapFcSwUp": fgTrapFcSwUp,
       "fgTrapFcSwDown": fgTrapFcSwDown,
       "fgTrapServerLoadBalanceRealServerDown": fgTrapServerLoadBalanceRealServerDown,
       "fgTrapDeviceNew": fgTrapDeviceNew,
       "fgVirtualDomain": fgVirtualDomain,
       "fgVdInfo": fgVdInfo,
       "fgVdNumber": fgVdNumber,
       "fgVdMaxVdoms": fgVdMaxVdoms,
       "fgVdEnabled": fgVdEnabled,
       "fgVdTables": fgVdTables,
       "fgVdTable": fgVdTable,
       "fgVdEntry": fgVdEntry,
       "fgVdEntIndex": fgVdEntIndex,
       "fgVdEntName": fgVdEntName,
       "fgVdEntOpMode": fgVdEntOpMode,
       "fgVdEntHaState": fgVdEntHaState,
       "fgVdEntCpuUsage": fgVdEntCpuUsage,
       "fgVdEntMemUsage": fgVdEntMemUsage,
       "fgVdEntSesCount": fgVdEntSesCount,
       "fgVdEntSesRate": fgVdEntSesRate,
       "fgVdTpTable": fgVdTpTable,
       "fgVdTpEntry": fgVdTpEntry,
       "fgVdTpMgmtAddrType": fgVdTpMgmtAddrType,
       "fgVdTpMgmtAddr": fgVdTpMgmtAddr,
       "fgVdTpMgmtMask": fgVdTpMgmtMask,
       "fgSystem": fgSystem,
       "fgSystemInfo": fgSystemInfo,
       "fgSysVersion": fgSysVersion,
       "fgSysMgmtVdom": fgSysMgmtVdom,
       "fgSysCpuUsage": fgSysCpuUsage,
       "fgSysMemUsage": fgSysMemUsage,
       "fgSysMemCapacity": fgSysMemCapacity,
       "fgSysDiskUsage": fgSysDiskUsage,
       "fgSysDiskCapacity": fgSysDiskCapacity,
       "fgSysSesCount": fgSysSesCount,
       "fgSysLowMemUsage": fgSysLowMemUsage,
       "fgSysLowMemCapacity": fgSysLowMemCapacity,
       "fgSysSesRate1": fgSysSesRate1,
       "fgSysSesRate10": fgSysSesRate10,
       "fgSysSesRate30": fgSysSesRate30,
       "fgSysSesRate60": fgSysSesRate60,
       "fgSysSes6Count": fgSysSes6Count,
       "fgSysSes6Rate1": fgSysSes6Rate1,
       "fgSysSes6Rate10": fgSysSes6Rate10,
       "fgSysSes6Rate30": fgSysSes6Rate30,
       "fgSysSes6Rate60": fgSysSes6Rate60,
       "fgSysUpTime": fgSysUpTime,
       "fgSoftware": fgSoftware,
       "fgSysVersionAv": fgSysVersionAv,
       "fgSysVersionIps": fgSysVersionIps,
       "fgHwSensors": fgHwSensors,
       "fgHwSensorCount": fgHwSensorCount,
       "fgHwSensorTable": fgHwSensorTable,
       "fgHwSensorEntry": fgHwSensorEntry,
       "fgHwSensorEntIndex": fgHwSensorEntIndex,
       "fgHwSensorEntName": fgHwSensorEntName,
       "fgHwSensorEntValue": fgHwSensorEntValue,
       "fgHwSensorEntAlarmStatus": fgHwSensorEntAlarmStatus,
       "fgProcessors": fgProcessors,
       "fgProcessorCount": fgProcessorCount,
       "fgProcessorTable": fgProcessorTable,
       "fgProcessorEntry": fgProcessorEntry,
       "fgProcessorEntIndex": fgProcessorEntIndex,
       "fgProcessorUsage": fgProcessorUsage,
       "fgProcessorUsage5sec": fgProcessorUsage5sec,
       "fgProcessorType": fgProcessorType,
       "fgProcessorContainedIn": fgProcessorContainedIn,
       "fgProcessorPktRxCount": fgProcessorPktRxCount,
       "fgProcessorPktTxCount": fgProcessorPktTxCount,
       "fgProcessorPktDroppedCount": fgProcessorPktDroppedCount,
       "fgProcessorUserUsage": fgProcessorUserUsage,
       "fgProcessorSysUsage": fgProcessorSysUsage,
       "fgProcessorTypes": fgProcessorTypes,
       "fgProcessorOther": fgProcessorOther,
       "fgProcessorIntel": fgProcessorIntel,
       "fgProcessorAMD": fgProcessorAMD,
       "fgProcessorXlr": fgProcessorXlr,
       "fgProcessorFnSoc": fgProcessorFnSoc,
       "fgProcessorFnNP2": fgProcessorFnNP2,
       "fgProcessorFnNP4": fgProcessorFnNP4,
       "fgProcessorFnNP6": fgProcessorFnNP6,
       "fgProcessorModules": fgProcessorModules,
       "fgProcessorModuleTypes": fgProcessorModuleTypes,
       "fgProcModOther": fgProcModOther,
       "fgProcModIntegrated": fgProcModIntegrated,
       "fgProcModFnXE2": fgProcModFnXE2,
       "fgProcModFnCE4": fgProcModFnCE4,
       "fgProcModFnFE8": fgProcModFnFE8,
       "fgProcModFnXG2": fgProcModFnXG2,
       "fgProcModIntegratedNPU": fgProcModIntegratedNPU,
       "fgProcModFnXD2": fgProcModFnXD2,
       "fgProcModFnF20": fgProcModFnF20,
       "fgProcModFnC20": fgProcModFnC20,
       "fgProcModFnXD4": fgProcModFnXD4,
       "fgProcModFnFB4": fgProcModFnFB4,
       "fgProcModFnFB8": fgProcModFnFB8,
       "fgProcModFnXB2": fgProcModFnXB2,
       "fgProcessorModuleCount": fgProcessorModuleCount,
       "fgProcessorModuleTable": fgProcessorModuleTable,
       "fgProcessorModuleEntry": fgProcessorModuleEntry,
       "fgProcModIndex": fgProcModIndex,
       "fgProcModType": fgProcModType,
       "fgProcModName": fgProcModName,
       "fgProcModDescr": fgProcModDescr,
       "fgProcModProcessorCount": fgProcModProcessorCount,
       "fgProcModMemCapacity": fgProcModMemCapacity,
       "fgProcModMemUsage": fgProcModMemUsage,
       "fgProcModSessionCount": fgProcModSessionCount,
       "fgProcModSACount": fgProcModSACount,
       "fgSystemInfoAdvanced": fgSystemInfoAdvanced,
       "fgSysInfoAdvMem": fgSysInfoAdvMem,
       "fgSIAdvMemPageCache": fgSIAdvMemPageCache,
       "fgSIAdvMemCacheActive": fgSIAdvMemCacheActive,
       "fgSIAdvMemCacheInactive": fgSIAdvMemCacheInactive,
       "fgSIAdvMemBuffer": fgSIAdvMemBuffer,
       "fgSIAdvMemEnterKerConsThrsh": fgSIAdvMemEnterKerConsThrsh,
       "fgSIAdvMemLeaveKerConsThrsh": fgSIAdvMemLeaveKerConsThrsh,
       "fgSIAdvMemEnterProxyConsThrsh": fgSIAdvMemEnterProxyConsThrsh,
       "fgSIAdvMemLeaveProxyConsThrsh": fgSIAdvMemLeaveProxyConsThrsh,
       "fgSysInfoAdvSessions": fgSysInfoAdvSessions,
       "fgSIAdvSesEphemeralCount": fgSIAdvSesEphemeralCount,
       "fgSIAdvSesEphemeralLimit": fgSIAdvSesEphemeralLimit,
       "fgSIAdvSesClashCount": fgSIAdvSesClashCount,
       "fgSIAdvSesExpCount": fgSIAdvSesExpCount,
       "fgSIAdvSesSyncQFCount": fgSIAdvSesSyncQFCount,
       "fgSIAdvSesAcceptQFCount": fgSIAdvSesAcceptQFCount,
       "fgSIAdvSesNoListenerCount": fgSIAdvSesNoListenerCount,
       "fgUsbports": fgUsbports,
       "fgUsbportCount": fgUsbportCount,
       "fgUsbportTable": fgUsbportTable,
       "fgUsbportEntry": fgUsbportEntry,
       "fgUsbportEntIndex": fgUsbportEntIndex,
       "fgUsbportPlugged": fgUsbportPlugged,
       "fgUsbportVersion": fgUsbportVersion,
       "fgUsbportClass": fgUsbportClass,
       "fgUsbportVendId": fgUsbportVendId,
       "fgUsbportProdId": fgUsbportProdId,
       "fgUsbportRevision": fgUsbportRevision,
       "fgUsbportManufacturer": fgUsbportManufacturer,
       "fgUsbportProduct": fgUsbportProduct,
       "fgUsbportSerial": fgUsbportSerial,
       "fgLinkMonitor": fgLinkMonitor,
       "fgLinkMonitorNumber": fgLinkMonitorNumber,
       "fgLinkMonitorTable": fgLinkMonitorTable,
       "fgLinkMonitorEntry": fgLinkMonitorEntry,
       "fgLinkMonitorID": fgLinkMonitorID,
       "fgLinkMonitorName": fgLinkMonitorName,
       "fgLinkMonitorState": fgLinkMonitorState,
       "fgLinkMonitorLatency": fgLinkMonitorLatency,
       "fgLinkMonitorJitter": fgLinkMonitorJitter,
       "fgLinkMonitorPacketSend": fgLinkMonitorPacketSend,
       "fgLinkMonitorPacketRecv": fgLinkMonitorPacketRecv,
       "fgLinkMonitorPacketLoss": fgLinkMonitorPacketLoss,
       "fgLinkMonitorVdom": fgLinkMonitorVdom,
       "fgFirewall": fgFirewall,
       "fgFwPolicies": fgFwPolicies,
       "fgFwPolInfo": fgFwPolInfo,
       "fgFwPolTables": fgFwPolTables,
       "fgFwPolStatsTable": fgFwPolStatsTable,
       "fgFwPolStatsEntry": fgFwPolStatsEntry,
       "fgFwPolID": fgFwPolID,
       "fgFwPolPktCount": fgFwPolPktCount,
       "fgFwPolByteCount": fgFwPolByteCount,
       "fgFwPolLastUsed": fgFwPolLastUsed,
       "fgFwPolPktCountHc": fgFwPolPktCountHc,
       "fgFwPolByteCountHc": fgFwPolByteCountHc,
       "fgFwPol6StatsTable": fgFwPol6StatsTable,
       "fgFwPol6StatsEntry": fgFwPol6StatsEntry,
       "fgFwPol6ID": fgFwPol6ID,
       "fgFwPol6PktCount": fgFwPol6PktCount,
       "fgFwPol6ByteCount": fgFwPol6ByteCount,
       "fgFwPol6LastUsed": fgFwPol6LastUsed,
       "fgFwUsers": fgFwUsers,
       "fgFwUserInfo": fgFwUserInfo,
       "fgFwUserNumber": fgFwUserNumber,
       "fgFwUserAuthTimeout": fgFwUserAuthTimeout,
       "fgFwUserTables": fgFwUserTables,
       "fgFwUserTable": fgFwUserTable,
       "fgFwUserEntry": fgFwUserEntry,
       "fgFwUserIndex": fgFwUserIndex,
       "fgFwUserName": fgFwUserName,
       "fgFwUserAuth": fgFwUserAuth,
       "fgFwUserState": fgFwUserState,
       "fgFwUserVdom": fgFwUserVdom,
       "fgMgmt": fgMgmt,
       "fgFmTrapPrefix": fgFmTrapPrefix,
       "fgFmTrapDeployComplete": fgFmTrapDeployComplete,
       "fgFmTrapDeployInProgress": fgFmTrapDeployInProgress,
       "fgFmTrapConfChange": fgFmTrapConfChange,
       "fgFmTrapIfChange": fgFmTrapIfChange,
       "fgAdmin": fgAdmin,
       "fgAdminOptions": fgAdminOptions,
       "fgAdminIdleTimeout": fgAdminIdleTimeout,
       "fgAdminLcdProtection": fgAdminLcdProtection,
       "fgAdminTables": fgAdminTables,
       "fgAdminTable": fgAdminTable,
       "fgAdminEntry": fgAdminEntry,
       "fgAdminVdom": fgAdminVdom,
       "fgMgmtTrapObjects": fgMgmtTrapObjects,
       "fgManIfIp": fgManIfIp,
       "fgManIfMask": fgManIfMask,
       "fgManIfIp6": fgManIfIp6,
       "fgIntf": fgIntf,
       "fgIntfInfo": fgIntfInfo,
       "fgIntfTables": fgIntfTables,
       "fgIntfTable": fgIntfTable,
       "fgIntfEntry": fgIntfEntry,
       "fgIntfEntVdom": fgIntfEntVdom,
       "fgIntfVrrps": fgIntfVrrps,
       "fgIntfVrrpCount": fgIntfVrrpCount,
       "fgIntfVrrpTable": fgIntfVrrpTable,
       "fgIntfVrrpEntry": fgIntfVrrpEntry,
       "fgIntfVrrpEntIndex": fgIntfVrrpEntIndex,
       "fgIntfVrrpEntVrId": fgIntfVrrpEntVrId,
       "fgIntfVrrpEntGrpId": fgIntfVrrpEntGrpId,
       "fgIntfVrrpEntIfName": fgIntfVrrpEntIfName,
       "fgIntfVrrpEntState": fgIntfVrrpEntState,
       "fgIntfVrrpEntVrIp": fgIntfVrrpEntVrIp,
       "fgIntfVlanHbs": fgIntfVlanHbs,
       "fgIntfVlanHbCount": fgIntfVlanHbCount,
       "fgIntfVlanHbTable": fgIntfVlanHbTable,
       "fgIntfVlanHbEntry": fgIntfVlanHbEntry,
       "fgIntfVlanHbEntIndex": fgIntfVlanHbEntIndex,
       "fgIntfVlanHbEntIfName": fgIntfVlanHbEntIfName,
       "fgIntfVlanHbEntSerial": fgIntfVlanHbEntSerial,
       "fgIntfVlanHbEntState": fgIntfVlanHbEntState,
       "fgAntivirus": fgAntivirus,
       "fgAvInfo": fgAvInfo,
       "fgAvTables": fgAvTables,
       "fgAvStatsTable": fgAvStatsTable,
       "fgAvStatsEntry": fgAvStatsEntry,
       "fgAvVirusDetected": fgAvVirusDetected,
       "fgAvVirusBlocked": fgAvVirusBlocked,
       "fgAvHTTPVirusDetected": fgAvHTTPVirusDetected,
       "fgAvHTTPVirusBlocked": fgAvHTTPVirusBlocked,
       "fgAvSMTPVirusDetected": fgAvSMTPVirusDetected,
       "fgAvSMTPVirusBlocked": fgAvSMTPVirusBlocked,
       "fgAvPOP3VirusDetected": fgAvPOP3VirusDetected,
       "fgAvPOP3VirusBlocked": fgAvPOP3VirusBlocked,
       "fgAvIMAPVirusDetected": fgAvIMAPVirusDetected,
       "fgAvIMAPVirusBlocked": fgAvIMAPVirusBlocked,
       "fgAvFTPVirusDetected": fgAvFTPVirusDetected,
       "fgAvFTPVirusBlocked": fgAvFTPVirusBlocked,
       "fgAvIMVirusDetected": fgAvIMVirusDetected,
       "fgAvIMVirusBlocked": fgAvIMVirusBlocked,
       "fgAvNNTPVirusDetected": fgAvNNTPVirusDetected,
       "fgAvNNTPVirusBlocked": fgAvNNTPVirusBlocked,
       "fgAvOversizedDetected": fgAvOversizedDetected,
       "fgAvOversizedBlocked": fgAvOversizedBlocked,
       "fgAvTrapObjects": fgAvTrapObjects,
       "fgAvTrapVirName": fgAvTrapVirName,
       "fgIps": fgIps,
       "fgIpsInfo": fgIpsInfo,
       "fgIpsTables": fgIpsTables,
       "fgIpsStatsTable": fgIpsStatsTable,
       "fgIpsStatsEntry": fgIpsStatsEntry,
       "fgIpsIntrusionsDetected": fgIpsIntrusionsDetected,
       "fgIpsIntrusionsBlocked": fgIpsIntrusionsBlocked,
       "fgIpsCritSevDetections": fgIpsCritSevDetections,
       "fgIpsHighSevDetections": fgIpsHighSevDetections,
       "fgIpsMedSevDetections": fgIpsMedSevDetections,
       "fgIpsLowSevDetections": fgIpsLowSevDetections,
       "fgIpsInfoSevDetections": fgIpsInfoSevDetections,
       "fgIpsSignatureDetections": fgIpsSignatureDetections,
       "fgIpsAnomalyDetections": fgIpsAnomalyDetections,
       "fgIpsTrapObjects": fgIpsTrapObjects,
       "fgIpsTrapSigId": fgIpsTrapSigId,
       "fgIpsTrapSrcIp": fgIpsTrapSrcIp,
       "fgIpsTrapSigMsg": fgIpsTrapSigMsg,
       "fgApplications": fgApplications,
       "fgWebfilter": fgWebfilter,
       "fgWebfilterInfo": fgWebfilterInfo,
       "fgWebfilterTables": fgWebfilterTables,
       "fgWebfilterStatsTable": fgWebfilterStatsTable,
       "fgWebfilterStatsEntry": fgWebfilterStatsEntry,
       "fgWfHTTPBlocked": fgWfHTTPBlocked,
       "fgWfHTTPSBlocked": fgWfHTTPSBlocked,
       "fgWfHTTPURLBlocked": fgWfHTTPURLBlocked,
       "fgWfHTTPSURLBlocked": fgWfHTTPSURLBlocked,
       "fgWfActiveXBlocked": fgWfActiveXBlocked,
       "fgWfCookieBlocked": fgWfCookieBlocked,
       "fgWfAppletBlocked": fgWfAppletBlocked,
       "fgFortiGuardStatsTable": fgFortiGuardStatsTable,
       "fgFortiGuardStatsEntry": fgFortiGuardStatsEntry,
       "fgFgWfHTTPExamined": fgFgWfHTTPExamined,
       "fgFgWfHTTPSExamined": fgFgWfHTTPSExamined,
       "fgFgWfHTTPAllowed": fgFgWfHTTPAllowed,
       "fgFgWfHTTPSAllowed": fgFgWfHTTPSAllowed,
       "fgFgWfHTTPBlocked": fgFgWfHTTPBlocked,
       "fgFgWfHTTPSBlocked": fgFgWfHTTPSBlocked,
       "fgFgWfHTTPLogged": fgFgWfHTTPLogged,
       "fgFgWfHTTPSLogged": fgFgWfHTTPSLogged,
       "fgFgWfHTTPOverridden": fgFgWfHTTPOverridden,
       "fgFgWfHTTPSOverridden": fgFgWfHTTPSOverridden,
       "fgAppProxyHTTP": fgAppProxyHTTP,
       "fgApHTTPUpTime": fgApHTTPUpTime,
       "fgApHTTPMemUsage": fgApHTTPMemUsage,
       "fgApHTTPStatsTable": fgApHTTPStatsTable,
       "fgApHTTPStatsEntry": fgApHTTPStatsEntry,
       "fgApHTTPReqProcessed": fgApHTTPReqProcessed,
       "fgApHTTPConnections": fgApHTTPConnections,
       "fgApHTTPMaxConnections": fgApHTTPMaxConnections,
       "fgAppProxySMTP": fgAppProxySMTP,
       "fgApSMTPUpTime": fgApSMTPUpTime,
       "fgApSMTPMemUsage": fgApSMTPMemUsage,
       "fgApSMTPStatsTable": fgApSMTPStatsTable,
       "fgApSMTPStatsEntry": fgApSMTPStatsEntry,
       "fgApSMTPReqProcessed": fgApSMTPReqProcessed,
       "fgApSMTPSpamDetected": fgApSMTPSpamDetected,
       "fgApSMTPConnections": fgApSMTPConnections,
       "fgApSMTPMaxConnections": fgApSMTPMaxConnections,
       "fgAppProxyPOP3": fgAppProxyPOP3,
       "fgApPOP3UpTime": fgApPOP3UpTime,
       "fgApPOP3MemUsage": fgApPOP3MemUsage,
       "fgApPOP3StatsTable": fgApPOP3StatsTable,
       "fgApPOP3StatsEntry": fgApPOP3StatsEntry,
       "fgApPOP3ReqProcessed": fgApPOP3ReqProcessed,
       "fgApPOP3SpamDetected": fgApPOP3SpamDetected,
       "fgApPOP3Connections": fgApPOP3Connections,
       "fgApPOP3MaxConnections": fgApPOP3MaxConnections,
       "fgAppProxyIMAP": fgAppProxyIMAP,
       "fgApIMAPUpTime": fgApIMAPUpTime,
       "fgApIMAPMemUsage": fgApIMAPMemUsage,
       "fgApIMAPStatsTable": fgApIMAPStatsTable,
       "fgApIMAPStatsEntry": fgApIMAPStatsEntry,
       "fgApIMAPReqProcessed": fgApIMAPReqProcessed,
       "fgApIMAPSpamDetected": fgApIMAPSpamDetected,
       "fgApIMAPConnections": fgApIMAPConnections,
       "fgApIMAPMaxConnections": fgApIMAPMaxConnections,
       "fgAppProxyNNTP": fgAppProxyNNTP,
       "fgApNNTPUpTime": fgApNNTPUpTime,
       "fgApNNTPMemUsage": fgApNNTPMemUsage,
       "fgApNNTPStatsTable": fgApNNTPStatsTable,
       "fgApNNTPStatsEntry": fgApNNTPStatsEntry,
       "fgApNNTPReqProcessed": fgApNNTPReqProcessed,
       "fgApNNTPConnections": fgApNNTPConnections,
       "fgApNNTPMaxConnections": fgApNNTPMaxConnections,
       "fgAppProxyIM": fgAppProxyIM,
       "fgApIMUpTime": fgApIMUpTime,
       "fgApIMMemUsage": fgApIMMemUsage,
       "fgApIMStatsTable": fgApIMStatsTable,
       "fgApIMStatsEntry": fgApIMStatsEntry,
       "fgApIMReqProcessed": fgApIMReqProcessed,
       "fgAppProxySIP": fgAppProxySIP,
       "fgApSIPUpTime": fgApSIPUpTime,
       "fgApSIPMemUsage": fgApSIPMemUsage,
       "fgApSIPStatsTable": fgApSIPStatsTable,
       "fgApSIPStatsEntry": fgApSIPStatsEntry,
       "fgApSIPClientReg": fgApSIPClientReg,
       "fgApSIPCallHandling": fgApSIPCallHandling,
       "fgApSIPServices": fgApSIPServices,
       "fgApSIPOtherReq": fgApSIPOtherReq,
       "fgAppScanUnit": fgAppScanUnit,
       "fgAppSuNumber": fgAppSuNumber,
       "fgAppSuStatsTable": fgAppSuStatsTable,
       "fgAppSuStatsEntry": fgAppSuStatsEntry,
       "fgAppSuIndex": fgAppSuIndex,
       "fgAppSuFileScanned": fgAppSuFileScanned,
       "fgAppVoIP": fgAppVoIP,
       "fgAppVoIPStatsTable": fgAppVoIPStatsTable,
       "fgAppVoIPStatsEntry": fgAppVoIPStatsEntry,
       "fgAppVoIPConn": fgAppVoIPConn,
       "fgAppVoIPCallBlocked": fgAppVoIPCallBlocked,
       "fgAppP2P": fgAppP2P,
       "fgAppP2PStatsTable": fgAppP2PStatsTable,
       "fgAppP2PStatsEntry": fgAppP2PStatsEntry,
       "fgAppP2PConnBlocked": fgAppP2PConnBlocked,
       "fgAppP2PProtoTable": fgAppP2PProtoTable,
       "fgAppP2PProtoEntry": fgAppP2PProtoEntry,
       "fgAppP2PProtEntProto": fgAppP2PProtEntProto,
       "fgAppP2PProtEntBytes": fgAppP2PProtEntBytes,
       "fgAppP2PProtoEntLastReset": fgAppP2PProtoEntLastReset,
       "fgAppIM": fgAppIM,
       "fgAppIMStatsTable": fgAppIMStatsTable,
       "fgAppIMStatsEntry": fgAppIMStatsEntry,
       "fgAppIMMessages": fgAppIMMessages,
       "fgAppIMFileTransfered": fgAppIMFileTransfered,
       "fgAppIMFileTxBlocked": fgAppIMFileTxBlocked,
       "fgAppIMConnBlocked": fgAppIMConnBlocked,
       "fgAppProxyFTP": fgAppProxyFTP,
       "fgApFTPUpTime": fgApFTPUpTime,
       "fgApFTPMemUsage": fgApFTPMemUsage,
       "fgApFTPStatsTable": fgApFTPStatsTable,
       "fgApFTPStatsEntry": fgApFTPStatsEntry,
       "fgApFTPReqProcessed": fgApFTPReqProcessed,
       "fgApFTPConnections": fgApFTPConnections,
       "fgApFTPMaxConnections": fgApFTPMaxConnections,
       "fgAppExplicitProxy": fgAppExplicitProxy,
       "fgExplicitProxyInfo": fgExplicitProxyInfo,
       "fgExplicitProxyUpTime": fgExplicitProxyUpTime,
       "fgExplicitProxyMemUsage": fgExplicitProxyMemUsage,
       "fgExplicitProxyRequests": fgExplicitProxyRequests,
       "fgExplicitProxyStatsTable": fgExplicitProxyStatsTable,
       "fgExplicitProxyStatsEntry": fgExplicitProxyStatsEntry,
       "fgExplicitProxyUsers": fgExplicitProxyUsers,
       "fgExplicitProxySessions": fgExplicitProxySessions,
       "fgExplicitProxyScanStatsTable": fgExplicitProxyScanStatsTable,
       "fgExplicitProxyScanStatsEntry": fgExplicitProxyScanStatsEntry,
       "fgExplicitProxyScanStatsDisp": fgExplicitProxyScanStatsDisp,
       "fgExplicitProxyVirus": fgExplicitProxyVirus,
       "fgExplicitProxyBannedWords": fgExplicitProxyBannedWords,
       "fgExplicitProxyPolicy": fgExplicitProxyPolicy,
       "fgExplicitProxyOversized": fgExplicitProxyOversized,
       "fgExplicitProxyArchNest": fgExplicitProxyArchNest,
       "fgExplicitProxyArchSize": fgExplicitProxyArchSize,
       "fgExplicitProxyArchEncrypted": fgExplicitProxyArchEncrypted,
       "fgExplicitProxyArchMultiPart": fgExplicitProxyArchMultiPart,
       "fgExplicitProxyArchUnsupported": fgExplicitProxyArchUnsupported,
       "fgExplicitProxyArchBomb": fgExplicitProxyArchBomb,
       "fgExplicitProxyArchCorrupt": fgExplicitProxyArchCorrupt,
       "fgExplicitProxyScriptStatsTable": fgExplicitProxyScriptStatsTable,
       "fgExplicitProxyScriptStatsEntry": fgExplicitProxyScriptStatsEntry,
       "fgExplicitProxyFilteredApplets": fgExplicitProxyFilteredApplets,
       "fgExplicitProxyFilteredActiveX": fgExplicitProxyFilteredActiveX,
       "fgExplicitProxyFilteredJScript": fgExplicitProxyFilteredJScript,
       "fgExplicitProxyFilteredJS": fgExplicitProxyFilteredJS,
       "fgExplicitProxyFilteredVBS": fgExplicitProxyFilteredVBS,
       "fgExplicitProxyFilteredOthScript": fgExplicitProxyFilteredOthScript,
       "fgExplicitProxyFilterStatsTable": fgExplicitProxyFilterStatsTable,
       "fgExplicitProxyFilterStatsEntry": fgExplicitProxyFilterStatsEntry,
       "fgExplicitProxyBlockedDLP": fgExplicitProxyBlockedDLP,
       "fgExplicitProxyBlockedConType": fgExplicitProxyBlockedConType,
       "fgExplicitProxyExaminedURLs": fgExplicitProxyExaminedURLs,
       "fgExplicitProxyAllowedURLs": fgExplicitProxyAllowedURLs,
       "fgExplicitProxyBlockedURLs": fgExplicitProxyBlockedURLs,
       "fgExplicitProxyLoggedURLs": fgExplicitProxyLoggedURLs,
       "fgExplicitProxyOverriddenURLs": fgExplicitProxyOverriddenURLs,
       "fgAppWebCache": fgAppWebCache,
       "fgWebCacheInfo": fgWebCacheInfo,
       "fgWebCacheRAMLimit": fgWebCacheRAMLimit,
       "fgWebCacheRAMUsage": fgWebCacheRAMUsage,
       "fgWebCacheRAMHits": fgWebCacheRAMHits,
       "fgWebCacheRAMMisses": fgWebCacheRAMMisses,
       "fgWebCacheRequests": fgWebCacheRequests,
       "fgWebCacheBypass": fgWebCacheBypass,
       "fgWebCacheUpTime": fgWebCacheUpTime,
       "fgWebCacheDiskStatsTable": fgWebCacheDiskStatsTable,
       "fgWebCacheDiskStatsEntry": fgWebCacheDiskStatsEntry,
       "fgWebCacheDisk": fgWebCacheDisk,
       "fgWebCacheDiskLimit": fgWebCacheDiskLimit,
       "fgWebCacheDiskUsage": fgWebCacheDiskUsage,
       "fgWebCacheDiskHits": fgWebCacheDiskHits,
       "fgWebCacheDiskMisses": fgWebCacheDiskMisses,
       "fgAppWanOpt": fgAppWanOpt,
       "fgWanOptInfo": fgWanOptInfo,
       "fgMemCacheLimit": fgMemCacheLimit,
       "fgMemCacheUsage": fgMemCacheUsage,
       "fgMemCacheHits": fgMemCacheHits,
       "fgMemCacheMisses": fgMemCacheMisses,
       "fgByteCacheRAMLimit": fgByteCacheRAMLimit,
       "fgByteCacheRAMUsage": fgByteCacheRAMUsage,
       "fgWanOptUpTime": fgWanOptUpTime,
       "fgWanOptStatsTable": fgWanOptStatsTable,
       "fgWanOptStatsEntry": fgWanOptStatsEntry,
       "fgWanOptTunnels": fgWanOptTunnels,
       "fgWanOptLANBytesIn": fgWanOptLANBytesIn,
       "fgWanOptLANBytesOut": fgWanOptLANBytesOut,
       "fgWanOptWANBytesIn": fgWanOptWANBytesIn,
       "fgWanOptWANBytesOut": fgWanOptWANBytesOut,
       "fgWanOptHistoryStatsTable": fgWanOptHistoryStatsTable,
       "fgWanOptHistoryStatsEntry": fgWanOptHistoryStatsEntry,
       "fgWanOptHistPeriod": fgWanOptHistPeriod,
       "fgWanOptProtocol": fgWanOptProtocol,
       "fgWanOptReductionRate": fgWanOptReductionRate,
       "fgWanOptLanTraffic": fgWanOptLanTraffic,
       "fgWanOptWanTraffic": fgWanOptWanTraffic,
       "fgWanOptTrafficStatsTable": fgWanOptTrafficStatsTable,
       "fgWanOptTrafficStatsEntry": fgWanOptTrafficStatsEntry,
       "fgWanOptLanInTraffic": fgWanOptLanInTraffic,
       "fgWanOptLanOutTraffic": fgWanOptLanOutTraffic,
       "fgWanOptWanInTraffic": fgWanOptWanInTraffic,
       "fgWanOptWanOutTraffic": fgWanOptWanOutTraffic,
       "fgWanOptDiskStatsTable": fgWanOptDiskStatsTable,
       "fgWanOptDiskStatsEntry": fgWanOptDiskStatsEntry,
       "fgWanOptDisk": fgWanOptDisk,
       "fgWanOptDiskLimit": fgWanOptDiskLimit,
       "fgWanOptDiskUsage": fgWanOptDiskUsage,
       "fgWanOptDiskHits": fgWanOptDiskHits,
       "fgWanOptDiskMisses": fgWanOptDiskMisses,
       "fgInetProto": fgInetProto,
       "fgInetProtoInfo": fgInetProtoInfo,
       "fgInetProtoTables": fgInetProtoTables,
       "fgIpSessTable": fgIpSessTable,
       "fgIpSessEntry": fgIpSessEntry,
       "fgIpSessIndex": fgIpSessIndex,
       "fgIpSessProto": fgIpSessProto,
       "fgIpSessFromAddr": fgIpSessFromAddr,
       "fgIpSessFromPort": fgIpSessFromPort,
       "fgIpSessToAddr": fgIpSessToAddr,
       "fgIpSessToPort": fgIpSessToPort,
       "fgIpSessExp": fgIpSessExp,
       "fgIpSessVdom": fgIpSessVdom,
       "fgIpSessStatsTable": fgIpSessStatsTable,
       "fgIpSessStatsEntry": fgIpSessStatsEntry,
       "fgIpSessNumber": fgIpSessNumber,
       "fgIp6SessStatsTable": fgIp6SessStatsTable,
       "fgIp6SessStatsEntry": fgIp6SessStatsEntry,
       "fgIp6SessNumber": fgIp6SessNumber,
       "fgVpn": fgVpn,
       "fgVpnInfo": fgVpnInfo,
       "fgVpnTunnelUpCount": fgVpnTunnelUpCount,
       "fgVpnTables": fgVpnTables,
       "fgVpnDialupTable": fgVpnDialupTable,
       "fgVpnDialupEntry": fgVpnDialupEntry,
       "fgVpnDialupIndex": fgVpnDialupIndex,
       "fgVpnDialupGateway": fgVpnDialupGateway,
       "fgVpnDialupLifetime": fgVpnDialupLifetime,
       "fgVpnDialupTimeout": fgVpnDialupTimeout,
       "fgVpnDialupSrcBegin": fgVpnDialupSrcBegin,
       "fgVpnDialupSrcEnd": fgVpnDialupSrcEnd,
       "fgVpnDialupDstAddr": fgVpnDialupDstAddr,
       "fgVpnDialupVdom": fgVpnDialupVdom,
       "fgVpnDialupInOctets": fgVpnDialupInOctets,
       "fgVpnDialupOutOctets": fgVpnDialupOutOctets,
       "fgVpnTunTable": fgVpnTunTable,
       "fgVpnTunEntry": fgVpnTunEntry,
       "fgVpnTunEntIndex": fgVpnTunEntIndex,
       "fgVpnTunEntPhase1Name": fgVpnTunEntPhase1Name,
       "fgVpnTunEntPhase2Name": fgVpnTunEntPhase2Name,
       "fgVpnTunEntRemGwyIp": fgVpnTunEntRemGwyIp,
       "fgVpnTunEntRemGwyPort": fgVpnTunEntRemGwyPort,
       "fgVpnTunEntLocGwyIp": fgVpnTunEntLocGwyIp,
       "fgVpnTunEntLocGwyPort": fgVpnTunEntLocGwyPort,
       "fgVpnTunEntSelectorSrcBeginIp": fgVpnTunEntSelectorSrcBeginIp,
       "fgVpnTunEntSelectorSrcEndIp": fgVpnTunEntSelectorSrcEndIp,
       "fgVpnTunEntSelectorSrcPort": fgVpnTunEntSelectorSrcPort,
       "fgVpnTunEntSelectorDstBeginIp": fgVpnTunEntSelectorDstBeginIp,
       "fgVpnTunEntSelectorDstEndIp": fgVpnTunEntSelectorDstEndIp,
       "fgVpnTunEntSelectorDstPort": fgVpnTunEntSelectorDstPort,
       "fgVpnTunEntSelectorProto": fgVpnTunEntSelectorProto,
       "fgVpnTunEntLifeSecs": fgVpnTunEntLifeSecs,
       "fgVpnTunEntLifeBytes": fgVpnTunEntLifeBytes,
       "fgVpnTunEntTimeout": fgVpnTunEntTimeout,
       "fgVpnTunEntInOctets": fgVpnTunEntInOctets,
       "fgVpnTunEntOutOctets": fgVpnTunEntOutOctets,
       "fgVpnTunEntStatus": fgVpnTunEntStatus,
       "fgVpnTunEntVdom": fgVpnTunEntVdom,
       "fgVpnSslStatsTable": fgVpnSslStatsTable,
       "fgVpnSslStatsEntry": fgVpnSslStatsEntry,
       "fgVpnSslState": fgVpnSslState,
       "fgVpnSslStatsLoginUsers": fgVpnSslStatsLoginUsers,
       "fgVpnSslStatsMaxUsers": fgVpnSslStatsMaxUsers,
       "fgVpnSslStatsActiveWebSessions": fgVpnSslStatsActiveWebSessions,
       "fgVpnSslStatsMaxWebSessions": fgVpnSslStatsMaxWebSessions,
       "fgVpnSslStatsActiveTunnels": fgVpnSslStatsActiveTunnels,
       "fgVpnSslStatsMaxTunnels": fgVpnSslStatsMaxTunnels,
       "fgVpnSslTunnelTable": fgVpnSslTunnelTable,
       "fgVpnSslTunnelEntry": fgVpnSslTunnelEntry,
       "fgVpnSslTunnelIndex": fgVpnSslTunnelIndex,
       "fgVpnSslTunnelVdom": fgVpnSslTunnelVdom,
       "fgVpnSslTunnelUserName": fgVpnSslTunnelUserName,
       "fgVpnSslTunnelSrcIp": fgVpnSslTunnelSrcIp,
       "fgVpnSslTunnelIp": fgVpnSslTunnelIp,
       "fgVpnSslTunnelUpTime": fgVpnSslTunnelUpTime,
       "fgVpnSslTunnelBytesIn": fgVpnSslTunnelBytesIn,
       "fgVpnSslTunnelBytesOut": fgVpnSslTunnelBytesOut,
       "fgVpnTrapObjects": fgVpnTrapObjects,
       "fgVpnTrapLocalGateway": fgVpnTrapLocalGateway,
       "fgVpnTrapRemoteGateway": fgVpnTrapRemoteGateway,
       "fgVpnTrapPhase1Name": fgVpnTrapPhase1Name,
       "fgHighAvailability": fgHighAvailability,
       "fgHaInfo": fgHaInfo,
       "fgHaSystemMode": fgHaSystemMode,
       "fgHaGroupId": fgHaGroupId,
       "fgHaPriority": fgHaPriority,
       "fgHaOverride": fgHaOverride,
       "fgHaAutoSync": fgHaAutoSync,
       "fgHaSchedule": fgHaSchedule,
       "fgHaGroupName": fgHaGroupName,
       "fgHaTables": fgHaTables,
       "fgHaStatsTable": fgHaStatsTable,
       "fgHaStatsEntry": fgHaStatsEntry,
       "fgHaStatsIndex": fgHaStatsIndex,
       "fgHaStatsSerial": fgHaStatsSerial,
       "fgHaStatsCpuUsage": fgHaStatsCpuUsage,
       "fgHaStatsMemUsage": fgHaStatsMemUsage,
       "fgHaStatsNetUsage": fgHaStatsNetUsage,
       "fgHaStatsSesCount": fgHaStatsSesCount,
       "fgHaStatsPktCount": fgHaStatsPktCount,
       "fgHaStatsByteCount": fgHaStatsByteCount,
       "fgHaStatsIdsCount": fgHaStatsIdsCount,
       "fgHaStatsAvCount": fgHaStatsAvCount,
       "fgHaStatsHostname": fgHaStatsHostname,
       "fgHaStatsSyncStatus": fgHaStatsSyncStatus,
       "fgHaStatsSyncDatimeSucc": fgHaStatsSyncDatimeSucc,
       "fgHaStatsSyncDatimeUnsucc": fgHaStatsSyncDatimeUnsucc,
       "fgHaStatsGlobalChecksum": fgHaStatsGlobalChecksum,
       "fgHaStatsMasterSerial": fgHaStatsMasterSerial,
       "fgHaTrapObjects": fgHaTrapObjects,
       "fgHaTrapMemberSerial": fgHaTrapMemberSerial,
       "fgWc": fgWc,
       "fgWcTrapObjects": fgWcTrapObjects,
       "fgWcApVdom": fgWcApVdom,
       "fgWcApSerial": fgWcApSerial,
       "fgWcApName": fgWcApName,
       "fgWcInfo": fgWcInfo,
       "fgWcInfoName": fgWcInfoName,
       "fgWcInfoLocation": fgWcInfoLocation,
       "fgWcInfoWtpCapacity": fgWcInfoWtpCapacity,
       "fgWcInfoWtpManaged": fgWcInfoWtpManaged,
       "fgWcInfoWtpSessions": fgWcInfoWtpSessions,
       "fgWcInfoStationCapacity": fgWcInfoStationCapacity,
       "fgWcInfoStationCount": fgWcInfoStationCount,
       "fgWcWlanTable": fgWcWlanTable,
       "fgWcWlanEntry": fgWcWlanEntry,
       "fgWcWlanSsid": fgWcWlanSsid,
       "fgWcWlanBroadcastSsid": fgWcWlanBroadcastSsid,
       "fgWcWlanSecurity": fgWcWlanSecurity,
       "fgWcWlanEncryption": fgWcWlanEncryption,
       "fgWcWlanAuthentication": fgWcWlanAuthentication,
       "fgWcWlanRadiusServer": fgWcWlanRadiusServer,
       "fgWcWlanUserGroup": fgWcWlanUserGroup,
       "fgWcWlanLocalBridging": fgWcWlanLocalBridging,
       "fgWcWlanVlanId": fgWcWlanVlanId,
       "fgWcWlanMeshBackhaul": fgWcWlanMeshBackhaul,
       "fgWcWlanStationCapacity": fgWcWlanStationCapacity,
       "fgWcWlanStationCount": fgWcWlanStationCount,
       "fgWcWtpTables": fgWcWtpTables,
       "fgWcWtpProfileTable": fgWcWtpProfileTable,
       "fgWcWtpProfileEntry": fgWcWtpProfileEntry,
       "fgWcWtpProfileName": fgWcWtpProfileName,
       "fgWcWtpProfilePlatform": fgWcWtpProfilePlatform,
       "fgWcWtpProfileDataChannelDtlsPolicy": fgWcWtpProfileDataChannelDtlsPolicy,
       "fgWcWtpProfileCountryString": fgWcWtpProfileCountryString,
       "fgWcWtpProfileRadioTable": fgWcWtpProfileRadioTable,
       "fgWcWtpProfileRadioEntry": fgWcWtpProfileRadioEntry,
       "fgWcWtpProfileRadioProfileName": fgWcWtpProfileRadioProfileName,
       "fgWcWtpProfileRadioRadioId": fgWcWtpProfileRadioRadioId,
       "fgWcWtpProfileRadioMode": fgWcWtpProfileRadioMode,
       "fgWcWtpProfileRadioApScan": fgWcWtpProfileRadioApScan,
       "fgWcWtpProfileRadioWidsProfile": fgWcWtpProfileRadioWidsProfile,
       "fgWcWtpProfileRadioDarrp": fgWcWtpProfileRadioDarrp,
       "fgWcWtpProfileRadioFrequencyHandoff": fgWcWtpProfileRadioFrequencyHandoff,
       "fgWcWtpProfileRadioApHandoff": fgWcWtpProfileRadioApHandoff,
       "fgWcWtpProfileRadioBeaconInterval": fgWcWtpProfileRadioBeaconInterval,
       "fgWcWtpProfileRadioDtimPeriod": fgWcWtpProfileRadioDtimPeriod,
       "fgWcWtpProfileRadioBand": fgWcWtpProfileRadioBand,
       "fgWcWtpProfileRadioChannelBonding": fgWcWtpProfileRadioChannelBonding,
       "fgWcWtpProfileRadioChannel": fgWcWtpProfileRadioChannel,
       "fgWcWtpProfileRadioAutoTxPowerControl": fgWcWtpProfileRadioAutoTxPowerControl,
       "fgWcWtpProfileRadioAutoTxPowerLow": fgWcWtpProfileRadioAutoTxPowerLow,
       "fgWcWtpProfileRadioAutoTxPowerHigh": fgWcWtpProfileRadioAutoTxPowerHigh,
       "fgWcWtpProfileRadioTxPowerLevel": fgWcWtpProfileRadioTxPowerLevel,
       "fgWcWtpProfileRadioVaps": fgWcWtpProfileRadioVaps,
       "fgWcWtpProfileRadioStationCapacity": fgWcWtpProfileRadioStationCapacity,
       "fgWcWtpProfileRadioChannelWidth": fgWcWtpProfileRadioChannelWidth,
       "fgWcWtpConfigTable": fgWcWtpConfigTable,
       "fgWcWtpConfigEntry": fgWcWtpConfigEntry,
       "fgWcWtpConfigWtpId": fgWcWtpConfigWtpId,
       "fgWcWtpConfigWtpAdmin": fgWcWtpConfigWtpAdmin,
       "fgWcWtpConfigWtpName": fgWcWtpConfigWtpName,
       "fgWcWtpConfigWtpLocation": fgWcWtpConfigWtpLocation,
       "fgWcWtpConfigWtpProfile": fgWcWtpConfigWtpProfile,
       "fgWcWtpConfigRadioEnable": fgWcWtpConfigRadioEnable,
       "fgWcWtpConfigRadioAutoTxPowerControl": fgWcWtpConfigRadioAutoTxPowerControl,
       "fgWcWtpConfigRadioAutoTxPowerLow": fgWcWtpConfigRadioAutoTxPowerLow,
       "fgWcWtpConfigRadioAutoTxPowerHigh": fgWcWtpConfigRadioAutoTxPowerHigh,
       "fgWcWtpConfigRadioTxPowerLevel": fgWcWtpConfigRadioTxPowerLevel,
       "fgWcWtpConfigRadioBand": fgWcWtpConfigRadioBand,
       "fgWcWtpConfigRadioApScan": fgWcWtpConfigRadioApScan,
       "fgWcWtpConfigVapAll": fgWcWtpConfigVapAll,
       "fgWcWtpConfigVaps": fgWcWtpConfigVaps,
       "fgWcWtpSessionTable": fgWcWtpSessionTable,
       "fgWcWtpSessionEntry": fgWcWtpSessionEntry,
       "fgWcWtpSessionWtpId": fgWcWtpSessionWtpId,
       "fgWcWtpSessionWtpIpAddressType": fgWcWtpSessionWtpIpAddressType,
       "fgWcWtpSessionWtpIpAddress": fgWcWtpSessionWtpIpAddress,
       "fgWcWtpSessionWtpLocalIpAddressType": fgWcWtpSessionWtpLocalIpAddressType,
       "fgWcWtpSessionWtpLocalIpAddress": fgWcWtpSessionWtpLocalIpAddress,
       "fgWcWtpSessionWtpBaseMacAddress": fgWcWtpSessionWtpBaseMacAddress,
       "fgWcWtpSessionConnectionState": fgWcWtpSessionConnectionState,
       "fgWcWtpSessionWtpUpTime": fgWcWtpSessionWtpUpTime,
       "fgWcWtpSessionWtpDaemonUpTime": fgWcWtpSessionWtpDaemonUpTime,
       "fgWcWtpSessionWtpSessionUpTime": fgWcWtpSessionWtpSessionUpTime,
       "fgWcWtpSessionWtpProfileName": fgWcWtpSessionWtpProfileName,
       "fgWcWtpSessionWtpModelNumber": fgWcWtpSessionWtpModelNumber,
       "fgWcWtpSessionWtpHwVersion": fgWcWtpSessionWtpHwVersion,
       "fgWcWtpSessionWtpSwVersion": fgWcWtpSessionWtpSwVersion,
       "fgWcWtpSessionWtpBootVersion": fgWcWtpSessionWtpBootVersion,
       "fgWcWtpSessionWtpRegionCode": fgWcWtpSessionWtpRegionCode,
       "fgWcWtpSessionWtpStationCount": fgWcWtpSessionWtpStationCount,
       "fgWcWtpSessionWtpByteRxCount": fgWcWtpSessionWtpByteRxCount,
       "fgWcWtpSessionWtpByteTxCount": fgWcWtpSessionWtpByteTxCount,
       "fgWcWtpSessionWtpCpuUsage": fgWcWtpSessionWtpCpuUsage,
       "fgWcWtpSessionWtpMemoryUsage": fgWcWtpSessionWtpMemoryUsage,
       "fgWcWtpSessionWtpMemoryCapacity": fgWcWtpSessionWtpMemoryCapacity,
       "fgWcWtpSessionRadioTable": fgWcWtpSessionRadioTable,
       "fgWcWtpSessionRadioEntry": fgWcWtpSessionRadioEntry,
       "fgWcWtpSessionRadioWtpId": fgWcWtpSessionRadioWtpId,
       "fgWcWtpSessionRadioRadioId": fgWcWtpSessionRadioRadioId,
       "fgWcWtpSessionRadioMode": fgWcWtpSessionRadioMode,
       "fgWcWtpSessionRadioBaseBssid": fgWcWtpSessionRadioBaseBssid,
       "fgWcWtpSessionRadioCountryString": fgWcWtpSessionRadioCountryString,
       "fgWcWtpSessionRadioCountryCode": fgWcWtpSessionRadioCountryCode,
       "fgWcWtpSessionRadioOperatingChannel": fgWcWtpSessionRadioOperatingChannel,
       "fgWcWtpSessionRadioOperatingPower": fgWcWtpSessionRadioOperatingPower,
       "fgWcWtpSessionRadioStationCount": fgWcWtpSessionRadioStationCount,
       "fgWcWtpSessionVapTable": fgWcWtpSessionVapTable,
       "fgWcWtpSessionVapEntry": fgWcWtpSessionVapEntry,
       "fgWcWtpSessionVapWtpId": fgWcWtpSessionVapWtpId,
       "fgWcWtpSessionVapRadioId": fgWcWtpSessionVapRadioId,
       "fgWcWtpSessionVapSsid": fgWcWtpSessionVapSsid,
       "fgWcWtpSessionVapStationCount": fgWcWtpSessionVapStationCount,
       "fgWcWtpSessionVapByteRxCount": fgWcWtpSessionVapByteRxCount,
       "fgWcWtpSessionVapByteTxCount": fgWcWtpSessionVapByteTxCount,
       "fgWcStaTable": fgWcStaTable,
       "fgWcStaEntry": fgWcStaEntry,
       "fgWcStaMacAddress": fgWcStaMacAddress,
       "fgWcStaWlan": fgWcStaWlan,
       "fgWcStaWtpId": fgWcStaWtpId,
       "fgWcStaRadioId": fgWcStaRadioId,
       "fgWcStaVlanId": fgWcStaVlanId,
       "fgWcStaIpAddressType": fgWcStaIpAddressType,
       "fgWcStaIpAddress": fgWcStaIpAddress,
       "fgWcStaVci": fgWcStaVci,
       "fgWcStaHost": fgWcStaHost,
       "fgWcStaUser": fgWcStaUser,
       "fgWcStaGroup": fgWcStaGroup,
       "fgWcStaSignal": fgWcStaSignal,
       "fgWcStaNoise": fgWcStaNoise,
       "fgWcStaIdle": fgWcStaIdle,
       "fgWcStaBandwidthTx": fgWcStaBandwidthTx,
       "fgWcStaBandwidthRx": fgWcStaBandwidthRx,
       "fgWcStaChannel": fgWcStaChannel,
       "fgWcStaRadioType": fgWcStaRadioType,
       "fgWcStaSecurity": fgWcStaSecurity,
       "fgWcStaEncrypt": fgWcStaEncrypt,
       "fgWcStaOnline": fgWcStaOnline,
       "fgFc": fgFc,
       "fgFcTrapObjects": fgFcTrapObjects,
       "fgFcSwVdom": fgFcSwVdom,
       "fgFcSwSerial": fgFcSwSerial,
       "fgFcSwName": fgFcSwName,
       "fgServerLoadBalance": fgServerLoadBalance,
       "fgServerLoadBalanceTrapObjects": fgServerLoadBalanceTrapObjects,
       "fgServerLoadBalanceRealServerAddress": fgServerLoadBalanceRealServerAddress,
       "fgServerLoadBalanceVirtualServerName": fgServerLoadBalanceVirtualServerName,
       "fgUsbModemInfo": fgUsbModemInfo,
       "fgUsbModemInfoObjects": fgUsbModemInfoObjects,
       "fgUsbModemSignalStrength": fgUsbModemSignalStrength,
       "fgUsbModemStatus": fgUsbModemStatus,
       "fgUsbModemSimState": fgUsbModemSimState,
       "fgUsbModemVendor": fgUsbModemVendor,
       "fgUsbModemProduct": fgUsbModemProduct,
       "fgUsbModemNetwork": fgUsbModemNetwork,
       "fgUsbModemId": fgUsbModemId,
       "fgUsbModemSimId": fgUsbModemSimId,
       "fgDevice": fgDevice,
       "fgDeviceTrapObjects": fgDeviceTrapObjects,
       "fgDeviceMacAddress": fgDeviceMacAddress,
       "fgDeviceCreated": fgDeviceCreated,
       "fgDeviceLastSeen": fgDeviceLastSeen,
       "fgMibConformance": fgMibConformance,
       "fgFmTrapGroup": fgFmTrapGroup,
       "fgFmTrapObjectGroup": fgFmTrapObjectGroup,
       "fgAdminObjectGroup": fgAdminObjectGroup,
       "fgSystemObjectGroup": fgSystemObjectGroup,
       "fgSoftwareObjectGroup": fgSoftwareObjectGroup,
       "fgHwSensorsObjectGroup": fgHwSensorsObjectGroup,
       "fgHighAvailabilityObjectGroup": fgHighAvailabilityObjectGroup,
       "fgVpnObjectGroup": fgVpnObjectGroup,
       "fgFirewallObjectGroup": fgFirewallObjectGroup,
       "fgAppServicesObjectGroup": fgAppServicesObjectGroup,
       "fgAntivirusObjectGroup": fgAntivirusObjectGroup,
       "fgIntrusionPrevtObjectGroup": fgIntrusionPrevtObjectGroup,
       "fgWebFilterObjectGroup": fgWebFilterObjectGroup,
       "fgVirtualDomainObjectGroup": fgVirtualDomainObjectGroup,
       "fgAdministrationObjectGroup": fgAdministrationObjectGroup,
       "fgIntfObjectGroup": fgIntfObjectGroup,
       "fgProcessorsObjectGroup": fgProcessorsObjectGroup,
       "fgNotificationGroup": fgNotificationGroup,
       "fgObsoleteNotificationsGroup": fgObsoleteNotificationsGroup,
       "fgExplicitProxyObjectGroup": fgExplicitProxyObjectGroup,
       "fgWebCacheObjectGroup": fgWebCacheObjectGroup,
       "fgWanOptObjectGroup": fgWanOptObjectGroup,
       "fgObsoleteAppServicesObjectGroup": fgObsoleteAppServicesObjectGroup,
       "fgSystemAdvancedObjectGroup": fgSystemAdvancedObjectGroup,
       "fgWcObjectGroup": fgWcObjectGroup,
       "fgFcObjectGroup": fgFcObjectGroup,
       "fgServerLoadBalanceObjectGroup": fgServerLoadBalanceObjectGroup,
       "fgUsbportsObjectGroup": fgUsbportsObjectGroup,
       "fgUsbModemInfoGroup": fgUsbModemInfoGroup,
       "fgDeviceObjectGroup": fgDeviceObjectGroup,
       "fgLinkMonitorGroup": fgLinkMonitorGroup,
       "fgMIBCompliance": fgMIBCompliance,
       "fg300MibCompliance": fg300MibCompliance,
       "fgObsolteMIBCompliance": fgObsolteMIBCompliance}
)
