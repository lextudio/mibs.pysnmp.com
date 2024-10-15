# SNMP MIB module (ALCATEL-IND1-TIMETRA-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-TIMETRA-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:47 2024
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

(timetraModules,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-GLOBAL-MIB",
    "timetraModules")

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

timetraTCMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 2)
)
timetraTCMIBModule.setRevisions(
        ("1908-01-01 00:00",
         "1907-01-01 00:00",
         "1906-03-23 00:00",
         "1905-08-31 00:00",
         "1905-01-24 00:00",
         "1904-01-15 00:00",
         "1903-08-15 00:00",
         "1903-01-20 00:00",
         "1901-05-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"


class TmnxPortID(Unsigned32, TextualConvention):
    status = "current"


class TmnxEncapVal(Unsigned32, TextualConvention):
    status = "current"


class QTag(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class QTagOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )



class TmnxStrSapId(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class IpAddressPrefixLength(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )



class TmnxActionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doAction", 1),
          ("notApplicable", 2))
    )



class TmnxAdminState(Integer32, TextualConvention):
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
        *(("inService", 2),
          ("noop", 1),
          ("outOfService", 3))
    )



class TmnxOperState(Integer32, TextualConvention):
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
        *(("inService", 2),
          ("outOfService", 3),
          ("transition", 4),
          ("unknown", 1))
    )



class TmnxStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )



class TmnxEnabledDisabled(Integer32, TextualConvention):
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



class TNamedItem(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TNamedItemOrEmpty(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )



class TItemDescription(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )



class TItemLongDescription(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )



class TmnxVRtrID(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )



class TmnxVRtrIDOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )



class TmnxBgpAutonomousSystem(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TmnxBgpLocalPreference(Unsigned32, TextualConvention):
    status = "current"


class TmnxBgpPreference(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TmnxCustId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )



class TmnxServId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )



class ServiceAdminStatus(Integer32, TextualConvention):
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



class ServiceOperStatus(Integer32, TextualConvention):
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



class TPolicyID(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TSapIngressPolicyID(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TSapEgressPolicyID(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TPolicyStatementNameOrEmpty(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )



class TmnxVcType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              9,
              10,
              11,
              17,
              18,
              19,
              20,
              21,
              23,
              25,
              4096)
        )
    )
    namedValues = NamedValues(
        *(("atmCell", 3),
          ("atmSdu", 2),
          ("atmVccCell", 9),
          ("atmVpcCell", 10),
          ("cesopsn", 21),
          ("cesopsnCas", 23),
          ("ethernet", 5),
          ("ethernetVlan", 4),
          ("frDlci", 25),
          ("frDlciMartini", 1),
          ("ipipe", 11),
          ("mirrorDest", 4096),
          ("satopE1", 17),
          ("satopE3", 19),
          ("satopT1", 18),
          ("satopT3", 20))
    )



class TmnxVcId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TmnxVcIdOrNone(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )



class Dot1PPriority(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )



class ServiceAccessPoint(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )



class TLspExpValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )



class TIpProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )



class TIpOption(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TTcpUdpPort(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )



class TTcpUdpPortOperator(Integer32, TextualConvention):
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
        *(("eq", 1),
          ("gt", 4),
          ("lt", 3),
          ("none", 0),
          ("range", 2))
    )



class TFrameType(Integer32, TextualConvention):
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
        *(("e802dot2LLC", 1),
          ("e802dot2SNAP", 2),
          ("e802dot3", 0),
          ("ethernetII", 3))
    )



class TQueueId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )



class TIngressQueueId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )



class TEgressQueueId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )



class TDSCPName(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TDSCPNameOrEmpty(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )



class TDSCPValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class TDSCPValueOrNone(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )



class TDSCPFilterActionValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )



class TFCName(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TFCNameOrEmpty(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )



class TFCSet(Bits, TextualConvention):
    status = "current"


class TFCType(Integer32, TextualConvention):
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
        *(("af", 2),
          ("be", 0),
          ("ef", 5),
          ("h1", 6),
          ("h2", 4),
          ("l1", 3),
          ("l2", 1),
          ("nc", 7))
    )



class TmnxTunnelType(Integer32, TextualConvention):
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
        *(("bypass", 5),
          ("gre", 4),
          ("invalid", 6),
          ("ldp", 2),
          ("rsvp", 3),
          ("sdp", 1))
    )



class TmnxTunnelID(Unsigned32, TextualConvention):
    status = "current"


class TmnxBgpRouteTarget(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TmnxVPNRouteDistinguisher(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class SdpBindId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class TmnxVRtrMplsLspID(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TPortSchedulerPIR(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 40000000),
    )



class TPortSchedulerCIR(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 40000000),
    )



class TWeight(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TCIRRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100000000),
    )



class TPIRRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000000),
    )



class TSecondaryShaper10GPIRRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10000),
    )



class TPIRRateOverride(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000000),
    )



class TPIRRateOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100000000),
    )



class TmnxDHCP6MsgType(Integer32, TextualConvention):
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("dhcp6MsgTypeAdvertise", 2),
          ("dhcp6MsgTypeConfirm", 4),
          ("dhcp6MsgTypeDecline", 9),
          ("dhcp6MsgTypeInfoRequest", 11),
          ("dhcp6MsgTypeMaxValue", 14),
          ("dhcp6MsgTypeRebind", 6),
          ("dhcp6MsgTypeReconfigure", 10),
          ("dhcp6MsgTypeRelayForw", 12),
          ("dhcp6MsgTypeRelayReply", 13),
          ("dhcp6MsgTypeRelease", 8),
          ("dhcp6MsgTypeRenew", 5),
          ("dhcp6MsgTypeReply", 7),
          ("dhcp6MsgTypeRequest", 3),
          ("dhcp6MsgTypeSolicit", 1))
    )



class TmnxOspfInstance(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )



class TmnxBGPFamilyType(Bits, TextualConvention):
    status = "current"


class TmnxIgmpGroupFilterMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1))
    )



class TmnxIgmpGroupType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )



class TmnxIgmpVersion(Integer32, TextualConvention):
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
        *(("version1", 1),
          ("version2", 2),
          ("version3", 3))
    )



class TmnxMldGroupFilterMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1))
    )



class TmnxMldGroupType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )



class TmnxMldVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )



class TmnxManagedRouteStatus(Integer32, TextualConvention):
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
        *(("installed", 0),
          ("notYetInstalled", 1),
          ("outOfMemory", 3),
          ("parentInterfaceDown", 6),
          ("routeTableFull", 5),
          ("shadowed", 4),
          ("wrongAntiSpoofType", 2))
    )



class TmnxAncpString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )



class TmnxAncpStringOrZero(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )



class TmnxMulticastAddrFamily(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipv4Multicast", 0),
          ("ipv6Multicast", 1))
    )



class TmnxSubIdentString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TmnxSubIdentStringOrEmpty(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class TmnxSubProfileString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class TmnxSubProfileStringOrEmpty(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class TmnxSlaProfileString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class TmnxSlaProfileStringOrEmpty(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class TmnxAppProfileString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class TmnxAppProfileStringOrEmpty(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class TmnxSubMgtIntDestIdOrEmpty(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class TmnxSubMgtIntDestId(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TmnxDhcpOptionType(Integer32, TextualConvention):
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
        *(("ascii", 2),
          ("hex", 3),
          ("ipv4", 1))
    )



class TmnxDhcpVendorOption(Bits, TextualConvention):
    status = "current"


class TmnxPppoeUserNameOrEmpty(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class TCpmProtPolicyID(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TMlpppQoSProfileId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-TIMETRA-TC-MIB",
    **{"InterfaceIndex": InterfaceIndex,
       "TmnxPortID": TmnxPortID,
       "TmnxEncapVal": TmnxEncapVal,
       "QTag": QTag,
       "QTagOrZero": QTagOrZero,
       "TmnxStrSapId": TmnxStrSapId,
       "IpAddressPrefixLength": IpAddressPrefixLength,
       "TmnxActionType": TmnxActionType,
       "TmnxAdminState": TmnxAdminState,
       "TmnxOperState": TmnxOperState,
       "TmnxStatus": TmnxStatus,
       "TmnxEnabledDisabled": TmnxEnabledDisabled,
       "TNamedItem": TNamedItem,
       "TNamedItemOrEmpty": TNamedItemOrEmpty,
       "TItemDescription": TItemDescription,
       "TItemLongDescription": TItemLongDescription,
       "TmnxVRtrID": TmnxVRtrID,
       "TmnxVRtrIDOrZero": TmnxVRtrIDOrZero,
       "TmnxBgpAutonomousSystem": TmnxBgpAutonomousSystem,
       "TmnxBgpLocalPreference": TmnxBgpLocalPreference,
       "TmnxBgpPreference": TmnxBgpPreference,
       "TmnxCustId": TmnxCustId,
       "TmnxServId": TmnxServId,
       "ServiceAdminStatus": ServiceAdminStatus,
       "ServiceOperStatus": ServiceOperStatus,
       "TPolicyID": TPolicyID,
       "TSapIngressPolicyID": TSapIngressPolicyID,
       "TSapEgressPolicyID": TSapEgressPolicyID,
       "TPolicyStatementNameOrEmpty": TPolicyStatementNameOrEmpty,
       "TmnxVcType": TmnxVcType,
       "TmnxVcId": TmnxVcId,
       "TmnxVcIdOrNone": TmnxVcIdOrNone,
       "Dot1PPriority": Dot1PPriority,
       "ServiceAccessPoint": ServiceAccessPoint,
       "TLspExpValue": TLspExpValue,
       "TIpProtocol": TIpProtocol,
       "TIpOption": TIpOption,
       "TTcpUdpPort": TTcpUdpPort,
       "TTcpUdpPortOperator": TTcpUdpPortOperator,
       "TFrameType": TFrameType,
       "TQueueId": TQueueId,
       "TIngressQueueId": TIngressQueueId,
       "TEgressQueueId": TEgressQueueId,
       "TDSCPName": TDSCPName,
       "TDSCPNameOrEmpty": TDSCPNameOrEmpty,
       "TDSCPValue": TDSCPValue,
       "TDSCPValueOrNone": TDSCPValueOrNone,
       "TDSCPFilterActionValue": TDSCPFilterActionValue,
       "TFCName": TFCName,
       "TFCNameOrEmpty": TFCNameOrEmpty,
       "TFCSet": TFCSet,
       "TFCType": TFCType,
       "TmnxTunnelType": TmnxTunnelType,
       "TmnxTunnelID": TmnxTunnelID,
       "TmnxBgpRouteTarget": TmnxBgpRouteTarget,
       "TmnxVPNRouteDistinguisher": TmnxVPNRouteDistinguisher,
       "SdpBindId": SdpBindId,
       "TmnxVRtrMplsLspID": TmnxVRtrMplsLspID,
       "TPortSchedulerPIR": TPortSchedulerPIR,
       "TPortSchedulerCIR": TPortSchedulerCIR,
       "TWeight": TWeight,
       "TCIRRate": TCIRRate,
       "TPIRRate": TPIRRate,
       "TSecondaryShaper10GPIRRate": TSecondaryShaper10GPIRRate,
       "TPIRRateOverride": TPIRRateOverride,
       "TPIRRateOrZero": TPIRRateOrZero,
       "TmnxDHCP6MsgType": TmnxDHCP6MsgType,
       "TmnxOspfInstance": TmnxOspfInstance,
       "TmnxBGPFamilyType": TmnxBGPFamilyType,
       "TmnxIgmpGroupFilterMode": TmnxIgmpGroupFilterMode,
       "TmnxIgmpGroupType": TmnxIgmpGroupType,
       "TmnxIgmpVersion": TmnxIgmpVersion,
       "TmnxMldGroupFilterMode": TmnxMldGroupFilterMode,
       "TmnxMldGroupType": TmnxMldGroupType,
       "TmnxMldVersion": TmnxMldVersion,
       "TmnxManagedRouteStatus": TmnxManagedRouteStatus,
       "TmnxAncpString": TmnxAncpString,
       "TmnxAncpStringOrZero": TmnxAncpStringOrZero,
       "TmnxMulticastAddrFamily": TmnxMulticastAddrFamily,
       "TmnxSubIdentString": TmnxSubIdentString,
       "TmnxSubIdentStringOrEmpty": TmnxSubIdentStringOrEmpty,
       "TmnxSubProfileString": TmnxSubProfileString,
       "TmnxSubProfileStringOrEmpty": TmnxSubProfileStringOrEmpty,
       "TmnxSlaProfileString": TmnxSlaProfileString,
       "TmnxSlaProfileStringOrEmpty": TmnxSlaProfileStringOrEmpty,
       "TmnxAppProfileString": TmnxAppProfileString,
       "TmnxAppProfileStringOrEmpty": TmnxAppProfileStringOrEmpty,
       "TmnxSubMgtIntDestIdOrEmpty": TmnxSubMgtIntDestIdOrEmpty,
       "TmnxSubMgtIntDestId": TmnxSubMgtIntDestId,
       "TmnxDhcpOptionType": TmnxDhcpOptionType,
       "TmnxDhcpVendorOption": TmnxDhcpVendorOption,
       "TmnxPppoeUserNameOrEmpty": TmnxPppoeUserNameOrEmpty,
       "TCpmProtPolicyID": TCpmProtPolicyID,
       "TMlpppQoSProfileId": TMlpppQoSProfileId,
       "timetraTCMIBModule": timetraTCMIBModule}
)
