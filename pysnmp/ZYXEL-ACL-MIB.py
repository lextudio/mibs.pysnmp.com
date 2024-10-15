# SNMP MIB module (ZYXEL-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-ACL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:19 2024
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

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelAcl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelClassifierStatus_ObjectIdentity = ObjectIdentity
zyxelClassifierStatus = _ZyxelClassifierStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1)
)
_ZyxelClassifierTable_Object = MibTable
zyxelClassifierTable = _ZyxelClassifierTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelClassifierTable.setStatus("current")
_ZyxelClassifierEntry_Object = MibTableRow
zyxelClassifierEntry = _ZyxelClassifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1)
)
zyxelClassifierEntry.setIndexNames(
    (0, "ZYXEL-ACL-MIB", "zyClassifierName"),
)
if mibBuilder.loadTexts:
    zyxelClassifierEntry.setStatus("current")
_ZyClassifierName_Type = DisplayString
_ZyClassifierName_Object = MibTableColumn
zyClassifierName = _ZyClassifierName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 1),
    _ZyClassifierName_Type()
)
zyClassifierName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyClassifierName.setStatus("current")
_ZyClassifierState_Type = EnabledStatus
_ZyClassifierState_Object = MibTableColumn
zyClassifierState = _ZyClassifierState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 2),
    _ZyClassifierState_Type()
)
zyClassifierState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifierState.setStatus("current")


class _ZyClassifierPacketFormat_Type(Integer32):
    """Custom type zyClassifierPacketFormat based on Integer32"""
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
        *(("all", 1),
          ("ethernet802dot3Tagged", 5),
          ("ethernet802dot3Untagged", 4),
          ("ethernetIITagged", 3),
          ("ethernetIIUntagged", 2))
    )


_ZyClassifierPacketFormat_Type.__name__ = "Integer32"
_ZyClassifierPacketFormat_Object = MibTableColumn
zyClassifierPacketFormat = _ZyClassifierPacketFormat_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 3),
    _ZyClassifierPacketFormat_Type()
)
zyClassifierPacketFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifierPacketFormat.setStatus("current")
_ZyClassifierVid_Type = Integer32
_ZyClassifierVid_Object = MibTableColumn
zyClassifierVid = _ZyClassifierVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 4),
    _ZyClassifierVid_Type()
)
zyClassifierVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifierVid.setStatus("current")
_ZyClassifier8021pPriority_Type = Integer32
_ZyClassifier8021pPriority_Object = MibTableColumn
zyClassifier8021pPriority = _ZyClassifier8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 5),
    _ZyClassifier8021pPriority_Type()
)
zyClassifier8021pPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifier8021pPriority.setStatus("current")
_ZyClassifierEthernetType_Type = Integer32
_ZyClassifierEthernetType_Object = MibTableColumn
zyClassifierEthernetType = _ZyClassifierEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 6),
    _ZyClassifierEthernetType_Type()
)
zyClassifierEthernetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifierEthernetType.setStatus("current")
_ZyClassifierSourceMacAddress_Type = MacAddress
_ZyClassifierSourceMacAddress_Object = MibTableColumn
zyClassifierSourceMacAddress = _ZyClassifierSourceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 7),
    _ZyClassifierSourceMacAddress_Type()
)
zyClassifierSourceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifierSourceMacAddress.setStatus("current")
_ZyClassifierIncomingPort_Type = Integer32
_ZyClassifierIncomingPort_Object = MibTableColumn
zyClassifierIncomingPort = _ZyClassifierIncomingPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 8),
    _ZyClassifierIncomingPort_Type()
)
zyClassifierIncomingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifierIncomingPort.setStatus("current")
_ZyClassifierDestinationMacAddress_Type = MacAddress
_ZyClassifierDestinationMacAddress_Object = MibTableColumn
zyClassifierDestinationMacAddress = _ZyClassifierDestinationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 9),
    _ZyClassifierDestinationMacAddress_Type()
)
zyClassifierDestinationMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifierDestinationMacAddress.setStatus("current")
_ZyClassifierDSCP_Type = Integer32
_ZyClassifierDSCP_Object = MibTableColumn
zyClassifierDSCP = _ZyClassifierDSCP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 10),
    _ZyClassifierDSCP_Type()
)
zyClassifierDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifierDSCP.setStatus("current")
_ZyClassifierIpProtocol_Type = Integer32
_ZyClassifierIpProtocol_Object = MibTableColumn
zyClassifierIpProtocol = _ZyClassifierIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 11),
    _ZyClassifierIpProtocol_Type()
)
zyClassifierIpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifierIpProtocol.setStatus("current")
_ZyClassifierEstablishOnly_Type = EnabledStatus
_ZyClassifierEstablishOnly_Object = MibTableColumn
zyClassifierEstablishOnly = _ZyClassifierEstablishOnly_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 12),
    _ZyClassifierEstablishOnly_Type()
)
zyClassifierEstablishOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifierEstablishOnly.setStatus("current")
_ZyClassifierSourceIpAddress_Type = IpAddress
_ZyClassifierSourceIpAddress_Object = MibTableColumn
zyClassifierSourceIpAddress = _ZyClassifierSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 13),
    _ZyClassifierSourceIpAddress_Type()
)
zyClassifierSourceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifierSourceIpAddress.setStatus("current")
_ZyClassifierSourceIpMaskBits_Type = Integer32
_ZyClassifierSourceIpMaskBits_Object = MibTableColumn
zyClassifierSourceIpMaskBits = _ZyClassifierSourceIpMaskBits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 14),
    _ZyClassifierSourceIpMaskBits_Type()
)
zyClassifierSourceIpMaskBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifierSourceIpMaskBits.setStatus("current")
_ZyClassifierSourceSocket_Type = Integer32
_ZyClassifierSourceSocket_Object = MibTableColumn
zyClassifierSourceSocket = _ZyClassifierSourceSocket_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 15),
    _ZyClassifierSourceSocket_Type()
)
zyClassifierSourceSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifierSourceSocket.setStatus("current")
_ZyClassifierDestinationIpAddress_Type = IpAddress
_ZyClassifierDestinationIpAddress_Object = MibTableColumn
zyClassifierDestinationIpAddress = _ZyClassifierDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 16),
    _ZyClassifierDestinationIpAddress_Type()
)
zyClassifierDestinationIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifierDestinationIpAddress.setStatus("current")
_ZyClassifierDestinationIpMaskBits_Type = Integer32
_ZyClassifierDestinationIpMaskBits_Object = MibTableColumn
zyClassifierDestinationIpMaskBits = _ZyClassifierDestinationIpMaskBits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 17),
    _ZyClassifierDestinationIpMaskBits_Type()
)
zyClassifierDestinationIpMaskBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifierDestinationIpMaskBits.setStatus("current")
_ZyClassifierDestinationSocket_Type = Integer32
_ZyClassifierDestinationSocket_Object = MibTableColumn
zyClassifierDestinationSocket = _ZyClassifierDestinationSocket_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 18),
    _ZyClassifierDestinationSocket_Type()
)
zyClassifierDestinationSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifierDestinationSocket.setStatus("current")
_ZyClassifierIPv6DSCP_Type = Integer32
_ZyClassifierIPv6DSCP_Object = MibTableColumn
zyClassifierIPv6DSCP = _ZyClassifierIPv6DSCP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 19),
    _ZyClassifierIPv6DSCP_Type()
)
zyClassifierIPv6DSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifierIPv6DSCP.setStatus("current")
_ZyClassifierIPv6NextHeader_Type = Integer32
_ZyClassifierIPv6NextHeader_Object = MibTableColumn
zyClassifierIPv6NextHeader = _ZyClassifierIPv6NextHeader_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 20),
    _ZyClassifierIPv6NextHeader_Type()
)
zyClassifierIPv6NextHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifierIPv6NextHeader.setStatus("current")
_ZyClassifierIPv6EstablishOnly_Type = EnabledStatus
_ZyClassifierIPv6EstablishOnly_Object = MibTableColumn
zyClassifierIPv6EstablishOnly = _ZyClassifierIPv6EstablishOnly_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 21),
    _ZyClassifierIPv6EstablishOnly_Type()
)
zyClassifierIPv6EstablishOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifierIPv6EstablishOnly.setStatus("current")
_ZyClassifierIPv6SourceIpAddress_Type = InetAddress
_ZyClassifierIPv6SourceIpAddress_Object = MibTableColumn
zyClassifierIPv6SourceIpAddress = _ZyClassifierIPv6SourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 22),
    _ZyClassifierIPv6SourceIpAddress_Type()
)
zyClassifierIPv6SourceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifierIPv6SourceIpAddress.setStatus("current")
_ZyClassifierIPv6SourceIpPrefixLength_Type = Integer32
_ZyClassifierIPv6SourceIpPrefixLength_Object = MibTableColumn
zyClassifierIPv6SourceIpPrefixLength = _ZyClassifierIPv6SourceIpPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 23),
    _ZyClassifierIPv6SourceIpPrefixLength_Type()
)
zyClassifierIPv6SourceIpPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifierIPv6SourceIpPrefixLength.setStatus("current")
_ZyClassifierIPv6DestinationIpAddress_Type = InetAddress
_ZyClassifierIPv6DestinationIpAddress_Object = MibTableColumn
zyClassifierIPv6DestinationIpAddress = _ZyClassifierIPv6DestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 24),
    _ZyClassifierIPv6DestinationIpAddress_Type()
)
zyClassifierIPv6DestinationIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifierIPv6DestinationIpAddress.setStatus("current")
_ZyClassifierIPv6DestinationIpPrefixLength_Type = Integer32
_ZyClassifierIPv6DestinationIpPrefixLength_Object = MibTableColumn
zyClassifierIPv6DestinationIpPrefixLength = _ZyClassifierIPv6DestinationIpPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 25),
    _ZyClassifierIPv6DestinationIpPrefixLength_Type()
)
zyClassifierIPv6DestinationIpPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifierIPv6DestinationIpPrefixLength.setStatus("current")
_ZyClassifierRowstatus_Type = RowStatus
_ZyClassifierRowstatus_Object = MibTableColumn
zyClassifierRowstatus = _ZyClassifierRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 26),
    _ZyClassifierRowstatus_Type()
)
zyClassifierRowstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClassifierRowstatus.setStatus("current")
_ZyxelPolicyStatus_ObjectIdentity = ObjectIdentity
zyxelPolicyStatus = _ZyxelPolicyStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2)
)
_ZyxelPolicyTable_Object = MibTable
zyxelPolicyTable = _ZyxelPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1)
)
if mibBuilder.loadTexts:
    zyxelPolicyTable.setStatus("current")
_ZyxelPolicyEntry_Object = MibTableRow
zyxelPolicyEntry = _ZyxelPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1)
)
zyxelPolicyEntry.setIndexNames(
    (0, "ZYXEL-ACL-MIB", "zyPolicyName"),
)
if mibBuilder.loadTexts:
    zyxelPolicyEntry.setStatus("current")
_ZyPolicyName_Type = DisplayString
_ZyPolicyName_Object = MibTableColumn
zyPolicyName = _ZyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 1),
    _ZyPolicyName_Type()
)
zyPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyPolicyName.setStatus("current")
_ZyPolicyState_Type = EnabledStatus
_ZyPolicyState_Object = MibTableColumn
zyPolicyState = _ZyPolicyState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 2),
    _ZyPolicyState_Type()
)
zyPolicyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPolicyState.setStatus("current")
_ZyPolicyClassifier_Type = DisplayString
_ZyPolicyClassifier_Object = MibTableColumn
zyPolicyClassifier = _ZyPolicyClassifier_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 3),
    _ZyPolicyClassifier_Type()
)
zyPolicyClassifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPolicyClassifier.setStatus("current")
_ZyPolicyVid_Type = Integer32
_ZyPolicyVid_Object = MibTableColumn
zyPolicyVid = _ZyPolicyVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 4),
    _ZyPolicyVid_Type()
)
zyPolicyVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPolicyVid.setStatus("current")
_ZyPolicyEgressPort_Type = Integer32
_ZyPolicyEgressPort_Object = MibTableColumn
zyPolicyEgressPort = _ZyPolicyEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 5),
    _ZyPolicyEgressPort_Type()
)
zyPolicyEgressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPolicyEgressPort.setStatus("current")
_ZyPolicy8021pPriority_Type = Integer32
_ZyPolicy8021pPriority_Object = MibTableColumn
zyPolicy8021pPriority = _ZyPolicy8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 6),
    _ZyPolicy8021pPriority_Type()
)
zyPolicy8021pPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPolicy8021pPriority.setStatus("current")
_ZyPolicyDSCP_Type = Integer32
_ZyPolicyDSCP_Object = MibTableColumn
zyPolicyDSCP = _ZyPolicyDSCP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 7),
    _ZyPolicyDSCP_Type()
)
zyPolicyDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPolicyDSCP.setStatus("current")
_ZyPolicyTOS_Type = Integer32
_ZyPolicyTOS_Object = MibTableColumn
zyPolicyTOS = _ZyPolicyTOS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 8),
    _ZyPolicyTOS_Type()
)
zyPolicyTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPolicyTOS.setStatus("current")
_ZyPolicyBandwidth_Type = Integer32
_ZyPolicyBandwidth_Object = MibTableColumn
zyPolicyBandwidth = _ZyPolicyBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 9),
    _ZyPolicyBandwidth_Type()
)
zyPolicyBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPolicyBandwidth.setStatus("current")
_ZyPolicyOutOfProfileDSCP_Type = Integer32
_ZyPolicyOutOfProfileDSCP_Object = MibTableColumn
zyPolicyOutOfProfileDSCP = _ZyPolicyOutOfProfileDSCP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 10),
    _ZyPolicyOutOfProfileDSCP_Type()
)
zyPolicyOutOfProfileDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPolicyOutOfProfileDSCP.setStatus("current")


class _ZyPolicyForwardingAction_Type(Integer32):
    """Custom type zyPolicyForwardingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discardThePacket", 2),
          ("doNotDropTheMatchingFramePreviouslyMarkedForDropping", 3),
          ("noChange", 1))
    )


_ZyPolicyForwardingAction_Type.__name__ = "Integer32"
_ZyPolicyForwardingAction_Object = MibTableColumn
zyPolicyForwardingAction = _ZyPolicyForwardingAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 11),
    _ZyPolicyForwardingAction_Type()
)
zyPolicyForwardingAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPolicyForwardingAction.setStatus("current")


class _ZyPolicyPriorityAction_Type(Integer32):
    """Custom type zyPolicyPriorityAction based on Integer32"""
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
        *(("noChange", 1),
          ("replaceThe802dot1PriorityFieldWithTheIpTosValue", 4),
          ("sendThePacketToPriorityQueue", 3),
          ("setThePackets802dot1Priority", 2))
    )


_ZyPolicyPriorityAction_Type.__name__ = "Integer32"
_ZyPolicyPriorityAction_Object = MibTableColumn
zyPolicyPriorityAction = _ZyPolicyPriorityAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 12),
    _ZyPolicyPriorityAction_Type()
)
zyPolicyPriorityAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPolicyPriorityAction.setStatus("current")


class _ZyPolicyDiffServAction_Type(Integer32):
    """Custom type zyPolicyDiffServAction based on Integer32"""
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
        *(("noChange", 1),
          ("replaceTheIpTosFieldWithThe802dot1PriorityValue", 3),
          ("setTheDiffservCodepointFieldInTheFrame", 4),
          ("setThePacketsTosField", 2))
    )


_ZyPolicyDiffServAction_Type.__name__ = "Integer32"
_ZyPolicyDiffServAction_Object = MibTableColumn
zyPolicyDiffServAction = _ZyPolicyDiffServAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 13),
    _ZyPolicyDiffServAction_Type()
)
zyPolicyDiffServAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPolicyDiffServAction.setStatus("current")


class _ZyPolicyOutgoingAction_Type(Bits):
    """Custom type zyPolicyOutgoingAction based on Bits"""
    namedValues = NamedValues(
        *(("sendTheMatchingFramesToTheEgressPort", 2),
          ("sendThePacketToTheEgressPort", 1),
          ("sendThePacketToTheMirrorPort", 0),
          ("setThePacketVlanId", 3))
    )

_ZyPolicyOutgoingAction_Type.__name__ = "Bits"
_ZyPolicyOutgoingAction_Object = MibTableColumn
zyPolicyOutgoingAction = _ZyPolicyOutgoingAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 14),
    _ZyPolicyOutgoingAction_Type()
)
zyPolicyOutgoingAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPolicyOutgoingAction.setStatus("current")
_ZyPolicyMeteringState_Type = Integer32
_ZyPolicyMeteringState_Object = MibTableColumn
zyPolicyMeteringState = _ZyPolicyMeteringState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 15),
    _ZyPolicyMeteringState_Type()
)
zyPolicyMeteringState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPolicyMeteringState.setStatus("current")


class _ZyPolicyOutOfProfileAction_Type(Bits):
    """Custom type zyPolicyOutOfProfileAction based on Bits"""
    namedValues = NamedValues(
        *(("changeTheDscpValue", 1),
          ("doNotDropTheMatchingFramePreviouslyMarkedForDropping", 3),
          ("dropThePacket", 0),
          ("setOutDropPrecedence", 2))
    )

_ZyPolicyOutOfProfileAction_Type.__name__ = "Bits"
_ZyPolicyOutOfProfileAction_Object = MibTableColumn
zyPolicyOutOfProfileAction = _ZyPolicyOutOfProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 16),
    _ZyPolicyOutOfProfileAction_Type()
)
zyPolicyOutOfProfileAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPolicyOutOfProfileAction.setStatus("current")
_ZyPolicyRowstatus_Type = RowStatus
_ZyPolicyRowstatus_Object = MibTableColumn
zyPolicyRowstatus = _ZyPolicyRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 17),
    _ZyPolicyRowstatus_Type()
)
zyPolicyRowstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPolicyRowstatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-ACL-MIB",
    **{"zyxelAcl": zyxelAcl,
       "zyxelClassifierStatus": zyxelClassifierStatus,
       "zyxelClassifierTable": zyxelClassifierTable,
       "zyxelClassifierEntry": zyxelClassifierEntry,
       "zyClassifierName": zyClassifierName,
       "zyClassifierState": zyClassifierState,
       "zyClassifierPacketFormat": zyClassifierPacketFormat,
       "zyClassifierVid": zyClassifierVid,
       "zyClassifier8021pPriority": zyClassifier8021pPriority,
       "zyClassifierEthernetType": zyClassifierEthernetType,
       "zyClassifierSourceMacAddress": zyClassifierSourceMacAddress,
       "zyClassifierIncomingPort": zyClassifierIncomingPort,
       "zyClassifierDestinationMacAddress": zyClassifierDestinationMacAddress,
       "zyClassifierDSCP": zyClassifierDSCP,
       "zyClassifierIpProtocol": zyClassifierIpProtocol,
       "zyClassifierEstablishOnly": zyClassifierEstablishOnly,
       "zyClassifierSourceIpAddress": zyClassifierSourceIpAddress,
       "zyClassifierSourceIpMaskBits": zyClassifierSourceIpMaskBits,
       "zyClassifierSourceSocket": zyClassifierSourceSocket,
       "zyClassifierDestinationIpAddress": zyClassifierDestinationIpAddress,
       "zyClassifierDestinationIpMaskBits": zyClassifierDestinationIpMaskBits,
       "zyClassifierDestinationSocket": zyClassifierDestinationSocket,
       "zyClassifierIPv6DSCP": zyClassifierIPv6DSCP,
       "zyClassifierIPv6NextHeader": zyClassifierIPv6NextHeader,
       "zyClassifierIPv6EstablishOnly": zyClassifierIPv6EstablishOnly,
       "zyClassifierIPv6SourceIpAddress": zyClassifierIPv6SourceIpAddress,
       "zyClassifierIPv6SourceIpPrefixLength": zyClassifierIPv6SourceIpPrefixLength,
       "zyClassifierIPv6DestinationIpAddress": zyClassifierIPv6DestinationIpAddress,
       "zyClassifierIPv6DestinationIpPrefixLength": zyClassifierIPv6DestinationIpPrefixLength,
       "zyClassifierRowstatus": zyClassifierRowstatus,
       "zyxelPolicyStatus": zyxelPolicyStatus,
       "zyxelPolicyTable": zyxelPolicyTable,
       "zyxelPolicyEntry": zyxelPolicyEntry,
       "zyPolicyName": zyPolicyName,
       "zyPolicyState": zyPolicyState,
       "zyPolicyClassifier": zyPolicyClassifier,
       "zyPolicyVid": zyPolicyVid,
       "zyPolicyEgressPort": zyPolicyEgressPort,
       "zyPolicy8021pPriority": zyPolicy8021pPriority,
       "zyPolicyDSCP": zyPolicyDSCP,
       "zyPolicyTOS": zyPolicyTOS,
       "zyPolicyBandwidth": zyPolicyBandwidth,
       "zyPolicyOutOfProfileDSCP": zyPolicyOutOfProfileDSCP,
       "zyPolicyForwardingAction": zyPolicyForwardingAction,
       "zyPolicyPriorityAction": zyPolicyPriorityAction,
       "zyPolicyDiffServAction": zyPolicyDiffServAction,
       "zyPolicyOutgoingAction": zyPolicyOutgoingAction,
       "zyPolicyMeteringState": zyPolicyMeteringState,
       "zyPolicyOutOfProfileAction": zyPolicyOutOfProfileAction,
       "zyPolicyRowstatus": zyPolicyRowstatus}
)
