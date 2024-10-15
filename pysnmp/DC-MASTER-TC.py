# SNMP MIB module (DC-MASTER-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DC-MASTER-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:22 2024
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

dcMasterTc = ModuleIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 41, 1)
)
dcMasterTc.setRevisions(
        ("2014-04-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AdminStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminStatusDown", 2),
          ("adminStatusUp", 1))
    )



class OperStatus(Integer32, TextualConvention):
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
        *(("operStatusActFailed", 5),
          ("operStatusDown", 2),
          ("operStatusGoingDown", 4),
          ("operStatusGoingUp", 3),
          ("operStatusUp", 1))
    )



class BaseOperStatus(Integer32, TextualConvention):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("operStatusActFailed", 5),
          ("operStatusDown", 2),
          ("operStatusFailed", 8),
          ("operStatusFailedPerm", 10),
          ("operStatusFailing", 11),
          ("operStatusGoingDown", 4),
          ("operStatusGoingUp", 3),
          ("operStatusNotReady", 7),
          ("operStatusPrntFailed", 9),
          ("operStatusQuiescing", 6),
          ("operStatusUp", 1))
    )



class NpgOperStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("operStatusActFailed", 5),
          ("operStatusDown", 2),
          ("operStatusFailed", 8),
          ("operStatusFailedPerm", 10),
          ("operStatusFailing", 11),
          ("operStatusGoingDown", 4),
          ("operStatusGoingUp", 3),
          ("operStatusUp", 1))
    )



class Unsigned32NonZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class NumericIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class NumericIndexOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class EntityIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class EntityIndexOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class AuthUserDataString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )



class StdAccessListListIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class StdAccessListListIndexOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class StdAccessListRuleIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class ExtAccessListListIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class ExtAccessListListIndexOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class ExtAccessListRuleIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class RouteAction(Integer32, TextualConvention):
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
        *(("routeActionDiscard", 4),
          ("routeActionForward", 2),
          ("routeActionLocal", 1),
          ("routeActionReject", 3),
          ("routeActionTunnel", 5))
    )



class AdminDistance(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class PathType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              65536,
              131072,
              131073,
              131074,
              196608,
              262144,
              327680,
              393216,
              458752,
              524288,
              589824,
              589825,
              589826,
              589827,
              655360,
              720896,
              786432,
              851968,
              851969,
              851970,
              851971,
              917504,
              917505,
              917506,
              983040,
              1048576,
              1048577,
              1048578,
              1114112)
        )
    )
    namedValues = NamedValues(
        *(("pathTypeBbnspfigp", 786432),
          ("pathTypeBgpExt", 917505),
          ("pathTypeBgpInt", 917504),
          ("pathTypeBgpVpn", 917506),
          ("pathTypeConfiguredConnected", 131074),
          ("pathTypeConfiguredLocal", 131073),
          ("pathTypeConnected", 131072),
          ("pathTypeDvmrp", 1114112),
          ("pathTypeEgp", 327680),
          ("pathTypeEigrp", 1048576),
          ("pathTypeEigrpExt", 1048578),
          ("pathTypeEigrpInt", 1048577),
          ("pathTypeEsis", 655360),
          ("pathTypeHello", 458752),
          ("pathTypeIcmp", 262144),
          ("pathTypeIdpr", 983040),
          ("pathTypeIgrp", 720896),
          ("pathTypeIsisLevel1Ext", 589826),
          ("pathTypeIsisLevel1Int", 589824),
          ("pathTypeIsisLevel2Ext", 589827),
          ("pathTypeIsisLevel2Int", 589825),
          ("pathTypeNone", 0),
          ("pathTypeOspfInterArea", 851969),
          ("pathTypeOspfIntraArea", 851968),
          ("pathTypeOspfType1Ext", 851970),
          ("pathTypeOspfType2Ext", 851971),
          ("pathTypeOther", 65536),
          ("pathTypePd", 393216),
          ("pathTypeRip", 524288),
          ("pathTypeStatic", 196608))
    )



class EntityProcType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(553779200,
              587268096,
              1023475712,
              1040252928,
              1040318464,
              1057030144,
              1057095680,
              1090584576,
              1090650112,
              1174470656,
              1241579520,
              1241645056)
        )
    )
    namedValues = NamedValues(
        *(("entityBgpNm", 1090650112),
          ("entityBgpRm", 1090584576),
          ("entityIsisPm", 1057030144),
          ("entityIsisSdc", 1057095680),
          ("entityLdpSc", 587268096),
          ("entityOspfNm", 1040318464),
          ("entityOspfPm", 1040252928),
          ("entityOspfv3Nm", 1241645056),
          ("entityOspfv3Pm", 1241579520),
          ("entityRipPm", 1174470656),
          ("entityRsvp", 553779200),
          ("entityRtm", 1023475712))
    )



class InetSubAddressType(Integer32, TextualConvention):
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
        *(("multicast", 2),
          ("none", 0),
          ("unicast", 1))
    )



class BfdSessionStatus(Integer32, TextualConvention):
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
        *(("bfdSessActivating", 2),
          ("bfdSessActive", 3),
          ("bfdSessAdminDown", 5),
          ("bfdSessInactive", 4),
          ("bfdSessInitial", 1),
          ("bfdSessNoContact", 6),
          ("bfdSessNotRequired", 0))
    )



class IgpShortcutMetricType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("metricTypeAbsolute", 1),
          ("metricTypeRelative", 2))
    )



class IfOperStatus(Integer32, TextualConvention):
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
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )



class MjStatus(Integer32, TextualConvention):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("mjFailed", 10),
          ("mjFailedToAdd", 7),
          ("mjFailedToRegister", 8),
          ("mjFailingOver", 9),
          ("mjJoinActive", 4),
          ("mjNotJoined", 1),
          ("mjSentAddJoin", 2),
          ("mjSentDelJoin", 6),
          ("mjSentRegister", 3),
          ("mjSentUnregister", 5),
          ("mjUnavailable", 11))
    )



class SjStatus(Integer32, TextualConvention):
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
        *(("sjFailed", 6),
          ("sjFailingOver", 5),
          ("sjJoinActive", 4),
          ("sjJoined", 2),
          ("sjNotJoined", 1),
          ("sjRcvdRegister", 3),
          ("sjRcvdUnregister", 7),
          ("sjUnregDone", 8))
    )



class InterfaceScope(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DC-MASTER-TC",
    **{"AdminStatus": AdminStatus,
       "OperStatus": OperStatus,
       "BaseOperStatus": BaseOperStatus,
       "NpgOperStatus": NpgOperStatus,
       "Unsigned32NonZero": Unsigned32NonZero,
       "NumericIndex": NumericIndex,
       "NumericIndexOrZero": NumericIndexOrZero,
       "EntityIndex": EntityIndex,
       "EntityIndexOrZero": EntityIndexOrZero,
       "AuthUserDataString": AuthUserDataString,
       "StdAccessListListIndex": StdAccessListListIndex,
       "StdAccessListListIndexOrZero": StdAccessListListIndexOrZero,
       "StdAccessListRuleIndex": StdAccessListRuleIndex,
       "ExtAccessListListIndex": ExtAccessListListIndex,
       "ExtAccessListListIndexOrZero": ExtAccessListListIndexOrZero,
       "ExtAccessListRuleIndex": ExtAccessListRuleIndex,
       "RouteAction": RouteAction,
       "AdminDistance": AdminDistance,
       "PathType": PathType,
       "EntityProcType": EntityProcType,
       "InetSubAddressType": InetSubAddressType,
       "BfdSessionStatus": BfdSessionStatus,
       "IgpShortcutMetricType": IgpShortcutMetricType,
       "IfOperStatus": IfOperStatus,
       "MjStatus": MjStatus,
       "SjStatus": SjStatus,
       "InterfaceScope": InterfaceScope,
       "dcMasterTc": dcMasterTc}
)
