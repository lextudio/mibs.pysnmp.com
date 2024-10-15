# SNMP MIB module (IEEE8021-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:29 2024
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
 iso,
 org) = mibBuilder.importSymbols(
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
    "iso",
    "org")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ieee8021TcMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 1)
)
ieee8021TcMib.setRevisions(
        ("2018-06-21 00:00",
         "2014-12-15 00:00",
         "2012-02-15 00:00",
         "2011-08-23 00:00",
         "2011-04-06 00:00",
         "2011-02-27 00:00",
         "2008-11-18 00:00",
         "2008-10-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IEEE8021PbbComponentIdentifier(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class IEEE8021PbbComponentIdentifierOrZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )



class IEEE8021PbbServiceIdentifier(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 16777214),
    )



class IEEE8021PbbServiceIdentifierOrUnassigned(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(256, 16777214),
    )



class IEEE8021PbbIngressEgress(Bits, TextualConvention):
    status = "current"


class IEEE8021PriorityCodePoint(Integer32, TextualConvention):
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
        *(("codePoint5p3d", 4),
          ("codePoint6p2d", 3),
          ("codePoint7p1d", 2),
          ("codePoint8p0d", 1))
    )



class IEEE8021BridgePortNumber(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class IEEE8021BridgePortNumberOrZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class IEEE8021BridgePortType(Integer32, TextualConvention):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("customerBackbonePort", 6),
          ("customerEdgePort", 5),
          ("customerNetworkPort", 4),
          ("customerVlanPort", 2),
          ("dBridgePort", 8),
          ("none", 1),
          ("providerNetworkPort", 3),
          ("remoteCustomerAccessPort", 9),
          ("stationFacingBridgePort", 10),
          ("uplinkAccessPort", 11),
          ("uplinkRelayPort", 12),
          ("virtualInstancePort", 7))
    )



class IEEE8021VlanIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4096, 4294967295),
    )



class IEEE8021VlanIndexOrWildcard(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class IEEE8021MstIdentifier(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class IEEE8021ServiceSelectorType(Integer32, TextualConvention):
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
        *(("group-isid", 6),
          ("ieeeReserved", 7),
          ("isid", 2),
          ("path-tesid", 5),
          ("segid", 4),
          ("tesid", 3),
          ("vlanId", 1))
    )



class IEEE8021ServiceSelectorValueOrNone(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )



class IEEE8021ServiceSelectorValue(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class IEEE8021PortAcceptableFrameTypes(Integer32, TextualConvention):
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
        *(("admitAll", 1),
          ("admitTagged", 3),
          ("admitUntaggedAndPriority", 2))
    )



class IEEE8021PriorityValue(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class IEEE8021PbbTeProtectionGroupId(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429467295),
    )



class IEEE8021PbbTeEsp(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )



class IEEE8021PbbTeTSidId(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 42947295),
    )



class IEEE8021PbbTeProtectionGroupConfigAdmin(Integer32, TextualConvention):
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
        *(("clear", 1),
          ("forceSwitch", 3),
          ("lockOutProtection", 2),
          ("manualSwitchToProtection", 4),
          ("manualSwitchToWorking", 5))
    )



class IEEE8021PbbTeProtectionGroupActiveRequests(Integer32, TextualConvention):
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
        *(("fs", 3),
          ("loP", 2),
          ("manualSwitchToProtection", 6),
          ("manualSwitchToWorking", 7),
          ("noRequest", 1),
          ("pSFH", 4),
          ("wSFH", 5))
    )



class IEEE8021TeipsIpgid(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429467295),
    )



class IEEE8021TeipsSegid(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 42947295),
    )



class IEEE8021TeipsSmpid(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )



class IEEE8021TeipsIpgConfigAdmin(Integer32, TextualConvention):
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
        *(("clear", 1),
          ("forceSwitch", 3),
          ("lockOutProtection", 2),
          ("manualSwitchToProtection", 4),
          ("manualSwitchToWorking", 5))
    )



class IEEE8021TeipsIpgConfigActiveRequests(Integer32, TextualConvention):
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
        *(("fs", 3),
          ("loP", 2),
          ("manualSwitchToProtection", 6),
          ("manualSwitchToWorking", 7),
          ("noRequest", 1),
          ("pSFH", 4),
          ("wSFH", 5))
    )



# MIB Managed Objects in the order of their OIDs

_Ieee802dot1mibs_ObjectIdentity = ObjectIdentity
ieee802dot1mibs = _Ieee802dot1mibs_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-TC-MIB",
    **{"IEEE8021PbbComponentIdentifier": IEEE8021PbbComponentIdentifier,
       "IEEE8021PbbComponentIdentifierOrZero": IEEE8021PbbComponentIdentifierOrZero,
       "IEEE8021PbbServiceIdentifier": IEEE8021PbbServiceIdentifier,
       "IEEE8021PbbServiceIdentifierOrUnassigned": IEEE8021PbbServiceIdentifierOrUnassigned,
       "IEEE8021PbbIngressEgress": IEEE8021PbbIngressEgress,
       "IEEE8021PriorityCodePoint": IEEE8021PriorityCodePoint,
       "IEEE8021BridgePortNumber": IEEE8021BridgePortNumber,
       "IEEE8021BridgePortNumberOrZero": IEEE8021BridgePortNumberOrZero,
       "IEEE8021BridgePortType": IEEE8021BridgePortType,
       "IEEE8021VlanIndex": IEEE8021VlanIndex,
       "IEEE8021VlanIndexOrWildcard": IEEE8021VlanIndexOrWildcard,
       "IEEE8021MstIdentifier": IEEE8021MstIdentifier,
       "IEEE8021ServiceSelectorType": IEEE8021ServiceSelectorType,
       "IEEE8021ServiceSelectorValueOrNone": IEEE8021ServiceSelectorValueOrNone,
       "IEEE8021ServiceSelectorValue": IEEE8021ServiceSelectorValue,
       "IEEE8021PortAcceptableFrameTypes": IEEE8021PortAcceptableFrameTypes,
       "IEEE8021PriorityValue": IEEE8021PriorityValue,
       "IEEE8021PbbTeProtectionGroupId": IEEE8021PbbTeProtectionGroupId,
       "IEEE8021PbbTeEsp": IEEE8021PbbTeEsp,
       "IEEE8021PbbTeTSidId": IEEE8021PbbTeTSidId,
       "IEEE8021PbbTeProtectionGroupConfigAdmin": IEEE8021PbbTeProtectionGroupConfigAdmin,
       "IEEE8021PbbTeProtectionGroupActiveRequests": IEEE8021PbbTeProtectionGroupActiveRequests,
       "IEEE8021TeipsIpgid": IEEE8021TeipsIpgid,
       "IEEE8021TeipsSegid": IEEE8021TeipsSegid,
       "IEEE8021TeipsSmpid": IEEE8021TeipsSmpid,
       "IEEE8021TeipsIpgConfigAdmin": IEEE8021TeipsIpgConfigAdmin,
       "IEEE8021TeipsIpgConfigActiveRequests": IEEE8021TeipsIpgConfigActiveRequests,
       "ieee802dot1mibs": ieee802dot1mibs,
       "ieee8021TcMib": ieee8021TcMib}
)
