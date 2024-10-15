# SNMP MIB module (CM-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CM-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:49 2024
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

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

cmCommonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1)
)
cmCommonMIB.setRevisions(
        ("2016-07-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eth-access", 1),
          ("eth-network", 2))
    )



class TrafficDirection(Integer32, TextualConvention):
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
        *(("a2n", 1),
          ("egress", 4),
          ("ingress", 3),
          ("n2a", 2),
          ("n2n", 5))
    )



class VlanId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class VlanPriority(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class VlanTagType(Integer32, TextualConvention):
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
        *(("encapOuterVlanTag", 6),
          ("inner-vlantag", 1),
          ("mplsLabel", 4),
          ("n2a-priorityMapping", 3),
          ("outer-vlantag", 2),
          ("vcLabel", 5))
    )



class AdminState(Integer32, TextualConvention):
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
        *(("disabled", 4),
          ("in-service", 1),
          ("maintenance", 3),
          ("management", 2),
          ("monitored", 6),
          ("unassigned", 5))
    )



class OperationalState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("outage", 2))
    )



class SecondaryState(Bits, TextualConvention):
    status = "current"


class EthernetPortSpeed(Integer32, TextualConvention):
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("speed-1000MB-full", 5),
          ("speed-1000MB-half", 6),
          ("speed-100MB-full", 3),
          ("speed-100MB-half", 4),
          ("speed-10G-full", 20),
          ("speed-10MB-full", 1),
          ("speed-10MB-half", 2),
          ("speed-auto", 7),
          ("speed-auto-1000MB-full", 12),
          ("speed-auto-1000MB-full-master", 15),
          ("speed-auto-1000MB-full-master-preferred", 18),
          ("speed-auto-1000MB-full-slave", 16),
          ("speed-auto-1000MB-full-slave-preferred", 19),
          ("speed-auto-1000MB-half", 13),
          ("speed-auto-100MB-full", 10),
          ("speed-auto-100MB-half", 11),
          ("speed-auto-10MB-full", 8),
          ("speed-auto-10MB-half", 9),
          ("speed-auto-detect", 21),
          ("speed-negotiating", 14),
          ("speed-none", 17),
          ("speed-unknown", 0))
    )



class EthernetMediaType(Integer32, TextualConvention):
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
        *(("auto", 4),
          ("copper", 1),
          ("coppersfp", 3),
          ("fiber", 2),
          ("none", 5),
          ("not-applicable", 0))
    )



class PerfCounter64(Counter64, TextualConvention):
    status = "current"


class PerfCounter32(Counter32, TextualConvention):
    status = "current"


class IpVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )



class IpPriorityMapMode(Integer32, TextualConvention):
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
        *(("none", 1),
          ("not-applicable", 0),
          ("priomap-dscp", 3),
          ("priomap-tos", 2))
    )



class PriorityMapMode(Integer32, TextualConvention):
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
        *(("priomap-8021p", 4),
          ("priomap-8021p-inner", 5),
          ("priomap-dscp", 3),
          ("priomap-none", 1),
          ("priomap-tos", 2))
    )



class SfpConnectorValue(Integer32, TextualConvention):
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("bnc-tnc", 5),
          ("cupigtail", 14),
          ("fccoaxhdr", 6),
          ("fcs1cu", 3),
          ("fcs2cu", 4),
          ("fjack", 7),
          ("hssdc", 13),
          ("lc", 8),
          ("mt-rj", 9),
          ("mu", 10),
          ("not-applicable", 0),
          ("optpigtail", 12),
          ("rj45", 16),
          ("sc", 2),
          ("sg", 11),
          ("unknown", 1),
          ("vendorspecific", 15))
    )



class RestartType(Integer32, TextualConvention):
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
        *(("cold-start", 2),
          ("not-applicable", 0),
          ("warm-start", 1))
    )



class SfpMediaType(Integer32, TextualConvention):
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
        *(("copper", 4),
          ("multimode", 2),
          ("multimode62-5", 3),
          ("not-applicable", 0),
          ("singlemode", 1))
    )



class ScheduleType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one-shot", 2),
          ("periodic", 1))
    )



class SchedActivityStatus(Integer32, TextualConvention):
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
        *(("active", 2),
          ("completed", 4),
          ("initial", 1),
          ("suspended", 3))
    )



class SchedActivityAction(Integer32, TextualConvention):
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
        *(("not-applicable", 0),
          ("resume", 2),
          ("suspend", 1))
    )



class MepDestinationType(Integer32, TextualConvention):
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
        *(("macaddress", 2),
          ("mepid", 1),
          ("not-applicable", 0))
    )



class ClassOfServiceType(Integer32, TextualConvention):
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
        *(("cos-five", 6),
          ("cos-four", 5),
          ("cos-not-applicable", 0),
          ("cos-one", 2),
          ("cos-seven", 8),
          ("cos-six", 7),
          ("cos-three", 4),
          ("cos-two", 3),
          ("cos-zero", 1))
    )



class SignalDirectionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )



class AfpTagControl(Integer32, TextualConvention):
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
        *(("both", 3),
          ("ctag", 1),
          ("stag", 2))
    )



class CmP2PFlowType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eline", 1)
    )



class CmTrafficACLPriorityType(Integer32, TextualConvention):
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
        *(("acl-dscp", 2),
          ("acl-tos", 1),
          ("notApplicable", 0))
    )



class CmTrafficAclFilterActionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )



class CmTrafficAclFilterType(Integer32, TextualConvention):
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
        *(("ipv4", 2),
          ("ipv6", 3),
          ("mac", 1))
    )



class CmTrafficAclProtocolType(Integer32, TextualConvention):
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
        *(("notApplicable", 0),
          ("tcp", 1),
          ("udp", 2))
    )



class VlanEthertype(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cvlan", 1),
          ("svlan", 2))
    )



class CmPmBinAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("not-applicable", 0))
    )



class CmPmIntervalType(Integer32, TextualConvention):
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
        *(("interval-15min", 1),
          ("interval-1day", 2),
          ("interval-5min", 4),
          ("rollover", 3))
    )



class TDMFrequencySourceType(Integer32, TextualConvention):
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
        *(("lineTiming", 3),
          ("loopTiming", 1),
          ("notApplicable", 0),
          ("systemTiming", 2))
    )



class F3DisplayString(OctetString, TextualConvention):
    status = "current"
    displayHint = "2047a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2047),
    )



class Decimal32(Unsigned32, TextualConvention):
    status = "current"


class UserInterfaceType(Integer32, TextualConvention):
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
        *(("cli", 1),
          ("gui", 2),
          ("netconf", 3),
          ("snmp", 4))
    )



class FlowSecState(Integer32, TextualConvention):
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
        *(("secureBlocked", 2),
          ("secureNormal", 1),
          ("unsecureBlocked", 4),
          ("unsecureNormal", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Subproducts_ObjectIdentity = ObjectIdentity
subproducts = _Subproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1)
)
_Nemihubshelf_ObjectIdentity = ObjectIdentity
nemihubshelf = _Nemihubshelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 1)
)
_Ge101_ObjectIdentity = ObjectIdentity
ge101 = _Ge101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 2)
)
_Ge206_ObjectIdentity = ObjectIdentity
ge206 = _Ge206_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 3)
)
_Ge201_ObjectIdentity = ObjectIdentity
ge201 = _Ge201_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 4)
)
_Ge201se_ObjectIdentity = ObjectIdentity
ge201se = _Ge201se_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 5)
)
_Ge206f_ObjectIdentity = ObjectIdentity
ge206f = _Ge206f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 6)
)
_Cmagg_ObjectIdentity = ObjectIdentity
cmagg = _Cmagg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 7)
)
_Ge112_ObjectIdentity = ObjectIdentity
ge112 = _Ge112_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 8)
)
_Ge114_ObjectIdentity = ObjectIdentity
ge114 = _Ge114_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 9)
)
_Ge206v_ObjectIdentity = ObjectIdentity
ge206v = _Ge206v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 10)
)
_Xg210_ObjectIdentity = ObjectIdentity
xg210 = _Xg210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 11)
)
_T1804_ObjectIdentity = ObjectIdentity
t1804 = _T1804_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 12)
)
_T3204_ObjectIdentity = ObjectIdentity
t3204 = _T3204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 13)
)
_Gesyncprobe_ObjectIdentity = ObjectIdentity
gesyncprobe = _Gesyncprobe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 14)
)
_Ge114H_ObjectIdentity = ObjectIdentity
ge114H = _Ge114H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 15)
)
_Ge114PH_ObjectIdentity = ObjectIdentity
ge114PH = _Ge114PH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 16)
)
_Ge114S_ObjectIdentity = ObjectIdentity
ge114S = _Ge114S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 17)
)
_Ge114SH_ObjectIdentity = ObjectIdentity
ge114SH = _Ge114SH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 18)
)
_Sh1pcs_ObjectIdentity = ObjectIdentity
sh1pcs = _Sh1pcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 19)
)
_Ge112Pro_ObjectIdentity = ObjectIdentity
ge112Pro = _Ge112Pro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 20)
)
_Ge112ProM_ObjectIdentity = ObjectIdentity
ge112ProM = _Ge112ProM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 21)
)
_Ge114Pro_ObjectIdentity = ObjectIdentity
ge114Pro = _Ge114Pro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 22)
)
_Ge114ProC_ObjectIdentity = ObjectIdentity
ge114ProC = _Ge114ProC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 23)
)
_Ge114ProSH_ObjectIdentity = ObjectIdentity
ge114ProSH = _Ge114ProSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 24)
)
_Ge114ProCSH_ObjectIdentity = ObjectIdentity
ge114ProCSH = _Ge114ProCSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 25)
)
_Ge114ProHE_ObjectIdentity = ObjectIdentity
ge114ProHE = _Ge114ProHE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 26)
)
_Xg210c_ObjectIdentity = ObjectIdentity
xg210c = _Xg210c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 27)
)
_Ge112ProH_ObjectIdentity = ObjectIdentity
ge112ProH = _Ge112ProH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 28)
)
_Ge114G_ObjectIdentity = ObjectIdentity
ge114G = _Ge114G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 29)
)
_F3Capabilities_ObjectIdentity = ObjectIdentity
f3Capabilities = _F3Capabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CM-COMMON-MIB",
    **{"PortType": PortType,
       "TrafficDirection": TrafficDirection,
       "VlanId": VlanId,
       "VlanPriority": VlanPriority,
       "VlanTagType": VlanTagType,
       "AdminState": AdminState,
       "OperationalState": OperationalState,
       "SecondaryState": SecondaryState,
       "EthernetPortSpeed": EthernetPortSpeed,
       "EthernetMediaType": EthernetMediaType,
       "PerfCounter64": PerfCounter64,
       "PerfCounter32": PerfCounter32,
       "IpVersion": IpVersion,
       "IpPriorityMapMode": IpPriorityMapMode,
       "PriorityMapMode": PriorityMapMode,
       "SfpConnectorValue": SfpConnectorValue,
       "RestartType": RestartType,
       "SfpMediaType": SfpMediaType,
       "ScheduleType": ScheduleType,
       "SchedActivityStatus": SchedActivityStatus,
       "SchedActivityAction": SchedActivityAction,
       "MepDestinationType": MepDestinationType,
       "ClassOfServiceType": ClassOfServiceType,
       "SignalDirectionType": SignalDirectionType,
       "AfpTagControl": AfpTagControl,
       "CmP2PFlowType": CmP2PFlowType,
       "CmTrafficACLPriorityType": CmTrafficACLPriorityType,
       "CmTrafficAclFilterActionType": CmTrafficAclFilterActionType,
       "CmTrafficAclFilterType": CmTrafficAclFilterType,
       "CmTrafficAclProtocolType": CmTrafficAclProtocolType,
       "VlanEthertype": VlanEthertype,
       "CmPmBinAction": CmPmBinAction,
       "CmPmIntervalType": CmPmIntervalType,
       "TDMFrequencySourceType": TDMFrequencySourceType,
       "F3DisplayString": F3DisplayString,
       "Decimal32": Decimal32,
       "UserInterfaceType": UserInterfaceType,
       "FlowSecState": FlowSecState,
       "cmCommonMIB": cmCommonMIB,
       "subproducts": subproducts,
       "nemihubshelf": nemihubshelf,
       "ge101": ge101,
       "ge206": ge206,
       "ge201": ge201,
       "ge201se": ge201se,
       "ge206f": ge206f,
       "cmagg": cmagg,
       "ge112": ge112,
       "ge114": ge114,
       "ge206v": ge206v,
       "xg210": xg210,
       "t1804": t1804,
       "t3204": t3204,
       "gesyncprobe": gesyncprobe,
       "ge114H": ge114H,
       "ge114PH": ge114PH,
       "ge114S": ge114S,
       "ge114SH": ge114SH,
       "sh1pcs": sh1pcs,
       "ge112Pro": ge112Pro,
       "ge112ProM": ge112ProM,
       "ge114Pro": ge114Pro,
       "ge114ProC": ge114ProC,
       "ge114ProSH": ge114ProSH,
       "ge114ProCSH": ge114ProCSH,
       "ge114ProHE": ge114ProHE,
       "xg210c": xg210c,
       "ge112ProH": ge112ProH,
       "ge114G": ge114G,
       "f3Capabilities": f3Capabilities}
)
