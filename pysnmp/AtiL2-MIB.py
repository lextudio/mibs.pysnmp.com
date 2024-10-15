# SNMP MIB module (AtiL2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AtiL2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:09 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class BridgeId(OctetString):
    """Custom type BridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class Timeout(Integer32):
    """Custom type Timeout based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlliedTelesyn_ObjectIdentity = ObjectIdentity
alliedTelesyn = _AlliedTelesyn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207)
)
_AtiProduct_ObjectIdentity = ObjectIdentity
atiProduct = _AtiProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1)
)
_Swhub_ObjectIdentity = ObjectIdentity
swhub = _Swhub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4)
)
_At_8324_ObjectIdentity = ObjectIdentity
at_8324 = _At_8324_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 37)
)
_At_8124XL_V2_ObjectIdentity = ObjectIdentity
at_8124XL_V2 = _At_8124XL_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 52)
)
_At_8326GB_ObjectIdentity = ObjectIdentity
at_8326GB = _At_8326GB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 72)
)
_At_9410GB_ObjectIdentity = ObjectIdentity
at_9410GB = _At_9410GB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 73)
)
_At_8350GB_ObjectIdentity = ObjectIdentity
at_8350GB = _At_8350GB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 74)
)
_At_8316F_ObjectIdentity = ObjectIdentity
at_8316F = _At_8316F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 77)
)
_MibObject_ObjectIdentity = ObjectIdentity
mibObject = _MibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8)
)
_AtiL2Mib_ObjectIdentity = ObjectIdentity
atiL2Mib = _AtiL2Mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 33)
)
_AtiL2GlobalGroup_ObjectIdentity = ObjectIdentity
atiL2GlobalGroup = _AtiL2GlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 1)
)


class _AtiL2SwProduct_Type(DisplayString):
    """Custom type atiL2SwProduct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtiL2SwProduct_Type.__name__ = "DisplayString"
_AtiL2SwProduct_Object = MibScalar
atiL2SwProduct = _AtiL2SwProduct_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 1, 1),
    _AtiL2SwProduct_Type()
)
atiL2SwProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2SwProduct.setStatus("mandatory")


class _AtiL2SwVersion_Type(DisplayString):
    """Custom type atiL2SwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtiL2SwVersion_Type.__name__ = "DisplayString"
_AtiL2SwVersion_Object = MibScalar
atiL2SwVersion = _AtiL2SwVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 1, 2),
    _AtiL2SwVersion_Type()
)
atiL2SwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2SwVersion.setStatus("mandatory")


class _AtiL2Reset_Type(Integer32):
    """Custom type atiL2Reset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switch-no-reset", 1),
          ("switch-reset", 2))
    )


_AtiL2Reset_Type.__name__ = "Integer32"
_AtiL2Reset_Object = MibScalar
atiL2Reset = _AtiL2Reset_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 1, 3),
    _AtiL2Reset_Type()
)
atiL2Reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2Reset.setStatus("mandatory")
_AtiL2MirroringSourceModule_Type = Integer32
_AtiL2MirroringSourceModule_Object = MibScalar
atiL2MirroringSourceModule = _AtiL2MirroringSourceModule_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 1, 4),
    _AtiL2MirroringSourceModule_Type()
)
atiL2MirroringSourceModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2MirroringSourceModule.setStatus("mandatory")
_AtiL2MirroringSourcePort_Type = Integer32
_AtiL2MirroringSourcePort_Object = MibScalar
atiL2MirroringSourcePort = _AtiL2MirroringSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 1, 5),
    _AtiL2MirroringSourcePort_Type()
)
atiL2MirroringSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2MirroringSourcePort.setStatus("mandatory")
_AtiL2MirroringDestinationModule_Type = Integer32
_AtiL2MirroringDestinationModule_Object = MibScalar
atiL2MirroringDestinationModule = _AtiL2MirroringDestinationModule_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 1, 6),
    _AtiL2MirroringDestinationModule_Type()
)
atiL2MirroringDestinationModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2MirroringDestinationModule.setStatus("mandatory")
_AtiL2MirroringDestinationPort_Type = Integer32
_AtiL2MirroringDestinationPort_Object = MibScalar
atiL2MirroringDestinationPort = _AtiL2MirroringDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 1, 7),
    _AtiL2MirroringDestinationPort_Type()
)
atiL2MirroringDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2MirroringDestinationPort.setStatus("mandatory")


class _AtiL2MirrorState_Type(Integer32):
    """Custom type atiL2MirrorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("receive-and-transmit", 1))
    )


_AtiL2MirrorState_Type.__name__ = "Integer32"
_AtiL2MirrorState_Object = MibScalar
atiL2MirrorState = _AtiL2MirrorState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 1, 8),
    _AtiL2MirrorState_Type()
)
atiL2MirrorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2MirrorState.setStatus("mandatory")


class _AtiL2IGMPState_Type(Integer32):
    """Custom type atiL2IGMPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtiL2IGMPState_Type.__name__ = "Integer32"
_AtiL2IGMPState_Object = MibScalar
atiL2IGMPState = _AtiL2IGMPState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 1, 9),
    _AtiL2IGMPState_Type()
)
atiL2IGMPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2IGMPState.setStatus("mandatory")
_AtiL2DeviceNumber_Type = Integer32
_AtiL2DeviceNumber_Object = MibScalar
atiL2DeviceNumber = _AtiL2DeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 1, 10),
    _AtiL2DeviceNumber_Type()
)
atiL2DeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2DeviceNumber.setStatus("mandatory")
_AtiL2IpGroup_ObjectIdentity = ObjectIdentity
atiL2IpGroup = _AtiL2IpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 2)
)
_AtiL2CurrentIpAddress_Type = IpAddress
_AtiL2CurrentIpAddress_Object = MibScalar
atiL2CurrentIpAddress = _AtiL2CurrentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 2, 1),
    _AtiL2CurrentIpAddress_Type()
)
atiL2CurrentIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2CurrentIpAddress.setStatus("mandatory")
_AtiL2ConfiguredIpAddress_Type = IpAddress
_AtiL2ConfiguredIpAddress_Object = MibScalar
atiL2ConfiguredIpAddress = _AtiL2ConfiguredIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 2, 2),
    _AtiL2ConfiguredIpAddress_Type()
)
atiL2ConfiguredIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2ConfiguredIpAddress.setStatus("mandatory")
_AtiL2ConfiguredSubnetMask_Type = IpAddress
_AtiL2ConfiguredSubnetMask_Object = MibScalar
atiL2ConfiguredSubnetMask = _AtiL2ConfiguredSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 2, 3),
    _AtiL2ConfiguredSubnetMask_Type()
)
atiL2ConfiguredSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2ConfiguredSubnetMask.setStatus("mandatory")
_AtiL2ConfiguredRouter_Type = IpAddress
_AtiL2ConfiguredRouter_Object = MibScalar
atiL2ConfiguredRouter = _AtiL2ConfiguredRouter_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 2, 4),
    _AtiL2ConfiguredRouter_Type()
)
atiL2ConfiguredRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2ConfiguredRouter.setStatus("mandatory")


class _AtiL2IPAddressStatus_Type(Integer32):
    """Custom type atiL2IPAddressStatus based on Integer32"""
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
        *(("from-Omega", 4),
          ("from-bootp", 2),
          ("from-dhcp", 1),
          ("from-psuedoip", 3))
    )


_AtiL2IPAddressStatus_Type.__name__ = "Integer32"
_AtiL2IPAddressStatus_Object = MibScalar
atiL2IPAddressStatus = _AtiL2IPAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 2, 5),
    _AtiL2IPAddressStatus_Type()
)
atiL2IPAddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2IPAddressStatus.setStatus("mandatory")
_AtiL2DNServer_Type = IpAddress
_AtiL2DNServer_Object = MibScalar
atiL2DNServer = _AtiL2DNServer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 2, 6),
    _AtiL2DNServer_Type()
)
atiL2DNServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2DNServer.setStatus("mandatory")


class _AtiL2DefaultDomainName_Type(DisplayString):
    """Custom type atiL2DefaultDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtiL2DefaultDomainName_Type.__name__ = "DisplayString"
_AtiL2DefaultDomainName_Object = MibScalar
atiL2DefaultDomainName = _AtiL2DefaultDomainName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 2, 7),
    _AtiL2DefaultDomainName_Type()
)
atiL2DefaultDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2DefaultDomainName.setStatus("mandatory")
_AtiL2NMGroup_ObjectIdentity = ObjectIdentity
atiL2NMGroup = _AtiL2NMGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 3)
)
_AtiL2NwMgrTable_Object = MibTable
atiL2NwMgrTable = _AtiL2NwMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 3, 1)
)
if mibBuilder.loadTexts:
    atiL2NwMgrTable.setStatus("mandatory")
_AtiL2NwMgrEntry_Object = MibTableRow
atiL2NwMgrEntry = _AtiL2NwMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 3, 1, 1)
)
atiL2NwMgrEntry.setIndexNames(
    (0, "AtiL2-MIB", "atiL2NwMgrIndex"),
)
if mibBuilder.loadTexts:
    atiL2NwMgrEntry.setStatus("mandatory")


class _AtiL2NwMgrIndex_Type(Integer32):
    """Custom type atiL2NwMgrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AtiL2NwMgrIndex_Type.__name__ = "Integer32"
_AtiL2NwMgrIndex_Object = MibTableColumn
atiL2NwMgrIndex = _AtiL2NwMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 3, 1, 1, 1),
    _AtiL2NwMgrIndex_Type()
)
atiL2NwMgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2NwMgrIndex.setStatus("mandatory")
_AtiL2NwMgrIpAddr_Type = IpAddress
_AtiL2NwMgrIpAddr_Object = MibTableColumn
atiL2NwMgrIpAddr = _AtiL2NwMgrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 3, 1, 1, 2),
    _AtiL2NwMgrIpAddr_Type()
)
atiL2NwMgrIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2NwMgrIpAddr.setStatus("mandatory")
_AtiL2DHCPGroup_ObjectIdentity = ObjectIdentity
atiL2DHCPGroup = _AtiL2DHCPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 4)
)
_AtiL2DHCPSysGroup_ObjectIdentity = ObjectIdentity
atiL2DHCPSysGroup = _AtiL2DHCPSysGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 4, 1)
)
_AtiL2DHCPCurrentDHCPClientAddress_Type = IpAddress
_AtiL2DHCPCurrentDHCPClientAddress_Object = MibScalar
atiL2DHCPCurrentDHCPClientAddress = _AtiL2DHCPCurrentDHCPClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 4, 1, 1),
    _AtiL2DHCPCurrentDHCPClientAddress_Type()
)
atiL2DHCPCurrentDHCPClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2DHCPCurrentDHCPClientAddress.setStatus("mandatory")
_AtiL2DHCPSubnetMask_Type = IpAddress
_AtiL2DHCPSubnetMask_Object = MibScalar
atiL2DHCPSubnetMask = _AtiL2DHCPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 4, 1, 2),
    _AtiL2DHCPSubnetMask_Type()
)
atiL2DHCPSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2DHCPSubnetMask.setStatus("mandatory")
_AtiL2DHCPCurrentRelayAgentAddress_Type = IpAddress
_AtiL2DHCPCurrentRelayAgentAddress_Object = MibScalar
atiL2DHCPCurrentRelayAgentAddress = _AtiL2DHCPCurrentRelayAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 4, 1, 3),
    _AtiL2DHCPCurrentRelayAgentAddress_Type()
)
atiL2DHCPCurrentRelayAgentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2DHCPCurrentRelayAgentAddress.setStatus("mandatory")
_AtiL2DHCPNextDHCPServerAddress_Type = IpAddress
_AtiL2DHCPNextDHCPServerAddress_Object = MibScalar
atiL2DHCPNextDHCPServerAddress = _AtiL2DHCPNextDHCPServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 4, 1, 4),
    _AtiL2DHCPNextDHCPServerAddress_Type()
)
atiL2DHCPNextDHCPServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2DHCPNextDHCPServerAddress.setStatus("mandatory")
_AtiL2DHCPTimerGroup_ObjectIdentity = ObjectIdentity
atiL2DHCPTimerGroup = _AtiL2DHCPTimerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 4, 2)
)
_AtiL2DHCPLeaseTimer_Type = TimeTicks
_AtiL2DHCPLeaseTimer_Object = MibScalar
atiL2DHCPLeaseTimer = _AtiL2DHCPLeaseTimer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 4, 2, 1),
    _AtiL2DHCPLeaseTimer_Type()
)
atiL2DHCPLeaseTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2DHCPLeaseTimer.setStatus("mandatory")
_AtiL2DHCPReacquisitionTimer_Type = TimeTicks
_AtiL2DHCPReacquisitionTimer_Object = MibScalar
atiL2DHCPReacquisitionTimer = _AtiL2DHCPReacquisitionTimer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 4, 2, 2),
    _AtiL2DHCPReacquisitionTimer_Type()
)
atiL2DHCPReacquisitionTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2DHCPReacquisitionTimer.setStatus("mandatory")
_AtiL2DHCPExpirationTimer_Type = TimeTicks
_AtiL2DHCPExpirationTimer_Object = MibScalar
atiL2DHCPExpirationTimer = _AtiL2DHCPExpirationTimer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 4, 2, 3),
    _AtiL2DHCPExpirationTimer_Type()
)
atiL2DHCPExpirationTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2DHCPExpirationTimer.setStatus("mandatory")
_AtiL2DeviceGroup_ObjectIdentity = ObjectIdentity
atiL2DeviceGroup = _AtiL2DeviceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 5)
)
_AtiL2deviceTable_Object = MibTable
atiL2deviceTable = _AtiL2deviceTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 5, 1)
)
if mibBuilder.loadTexts:
    atiL2deviceTable.setStatus("mandatory")
_AtiL2deviceEntry_Object = MibTableRow
atiL2deviceEntry = _AtiL2deviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 5, 1, 1)
)
atiL2deviceEntry.setIndexNames(
    (0, "AtiL2-MIB", "atiL2deviceIndex"),
)
if mibBuilder.loadTexts:
    atiL2deviceEntry.setStatus("mandatory")


class _AtiL2deviceIndex_Type(Integer32):
    """Custom type atiL2deviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiL2deviceIndex_Type.__name__ = "Integer32"
_AtiL2deviceIndex_Object = MibTableColumn
atiL2deviceIndex = _AtiL2deviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 5, 1, 1, 2),
    _AtiL2deviceIndex_Type()
)
atiL2deviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2deviceIndex.setStatus("mandatory")


class _AtiL2deviceDescr_Type(DisplayString):
    """Custom type atiL2deviceDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtiL2deviceDescr_Type.__name__ = "DisplayString"
_AtiL2deviceDescr_Object = MibTableColumn
atiL2deviceDescr = _AtiL2deviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 5, 1, 1, 3),
    _AtiL2deviceDescr_Type()
)
atiL2deviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2deviceDescr.setStatus("mandatory")


class _AtiL2deviceProductType_Type(Integer32):
    """Custom type atiL2deviceProductType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              20)
        )
    )
    namedValues = NamedValues(
        *(("at-8124XL-V2", 3),
          ("at-8316F", 2),
          ("at-8324", 1),
          ("at-8326GB", 4),
          ("at-8350GB", 6),
          ("at-9410GB", 5),
          ("other", 20))
    )


_AtiL2deviceProductType_Type.__name__ = "Integer32"
_AtiL2deviceProductType_Object = MibTableColumn
atiL2deviceProductType = _AtiL2deviceProductType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 5, 1, 1, 4),
    _AtiL2deviceProductType_Type()
)
atiL2deviceProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2deviceProductType.setStatus("mandatory")


class _AtiL2devicePortCount_Type(Integer32):
    """Custom type atiL2devicePortCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_AtiL2devicePortCount_Type.__name__ = "Integer32"
_AtiL2devicePortCount_Object = MibTableColumn
atiL2devicePortCount = _AtiL2devicePortCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 5, 1, 1, 5),
    _AtiL2devicePortCount_Type()
)
atiL2devicePortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2devicePortCount.setStatus("mandatory")


class _AtiL2deviceSecurityConfig_Type(Integer32):
    """Custom type atiL2deviceSecurityConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled-with-learning-locked", 2),
          ("limited-enabled", 3))
    )


_AtiL2deviceSecurityConfig_Type.__name__ = "Integer32"
_AtiL2deviceSecurityConfig_Object = MibTableColumn
atiL2deviceSecurityConfig = _AtiL2deviceSecurityConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 5, 1, 1, 6),
    _AtiL2deviceSecurityConfig_Type()
)
atiL2deviceSecurityConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2deviceSecurityConfig.setStatus("mandatory")


class _AtiL2deviceSecurityAction_Type(Integer32):
    """Custom type atiL2deviceSecurityAction based on Integer32"""
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
        *(("disable-port-and-send-trap", 3),
          ("disable-port-only", 2),
          ("do-nothing", 4),
          ("send-trap-only", 1))
    )


_AtiL2deviceSecurityAction_Type.__name__ = "Integer32"
_AtiL2deviceSecurityAction_Object = MibTableColumn
atiL2deviceSecurityAction = _AtiL2deviceSecurityAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 5, 1, 1, 7),
    _AtiL2deviceSecurityAction_Type()
)
atiL2deviceSecurityAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2deviceSecurityAction.setStatus("mandatory")
_AtiL2deviceDebugAvailableBytes_Type = Integer32
_AtiL2deviceDebugAvailableBytes_Object = MibTableColumn
atiL2deviceDebugAvailableBytes = _AtiL2deviceDebugAvailableBytes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 5, 1, 1, 8),
    _AtiL2deviceDebugAvailableBytes_Type()
)
atiL2deviceDebugAvailableBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2deviceDebugAvailableBytes.setStatus("mandatory")


class _AtiL2deviceMDA1Type_Type(Integer32):
    """Custom type atiL2deviceMDA1Type based on Integer32"""
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
        *(("hundredfiber-mii", 2),
          ("none", 5),
          ("oneGb-Fiber", 4),
          ("oneGb-rj45", 3),
          ("ten-100rj45-mii", 1))
    )


_AtiL2deviceMDA1Type_Type.__name__ = "Integer32"
_AtiL2deviceMDA1Type_Object = MibTableColumn
atiL2deviceMDA1Type = _AtiL2deviceMDA1Type_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 5, 1, 1, 9),
    _AtiL2deviceMDA1Type_Type()
)
atiL2deviceMDA1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2deviceMDA1Type.setStatus("mandatory")


class _AtiL2deviceMDA2Type_Type(Integer32):
    """Custom type atiL2deviceMDA2Type based on Integer32"""
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
        *(("hundredfiber-mii", 2),
          ("none", 5),
          ("oneGb-Fiber", 4),
          ("oneGb-rj45", 3),
          ("ten-100rj45-mii", 1))
    )


_AtiL2deviceMDA2Type_Type.__name__ = "Integer32"
_AtiL2deviceMDA2Type_Object = MibTableColumn
atiL2deviceMDA2Type = _AtiL2deviceMDA2Type_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 5, 1, 1, 10),
    _AtiL2deviceMDA2Type_Type()
)
atiL2deviceMDA2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2deviceMDA2Type.setStatus("mandatory")


class _AtiL2deviceReset_Type(Integer32):
    """Custom type atiL2deviceReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switch-no-reset", 1),
          ("switch-reset", 2))
    )


_AtiL2deviceReset_Type.__name__ = "Integer32"
_AtiL2deviceReset_Object = MibTableColumn
atiL2deviceReset = _AtiL2deviceReset_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 5, 1, 1, 11),
    _AtiL2deviceReset_Type()
)
atiL2deviceReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2deviceReset.setStatus("mandatory")
_AtiL2EthernetStatsGroup_ObjectIdentity = ObjectIdentity
atiL2EthernetStatsGroup = _AtiL2EthernetStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6)
)
_AtiL2EthMonStatsGroup_ObjectIdentity = ObjectIdentity
atiL2EthMonStatsGroup = _AtiL2EthMonStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 1)
)
_AtiL2EthMonStatsTable_Object = MibTable
atiL2EthMonStatsTable = _AtiL2EthMonStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 1, 1)
)
if mibBuilder.loadTexts:
    atiL2EthMonStatsTable.setStatus("mandatory")
_AtiL2EthMonStatsEntry_Object = MibTableRow
atiL2EthMonStatsEntry = _AtiL2EthMonStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 1, 1, 1)
)
atiL2EthMonStatsEntry.setIndexNames(
    (0, "AtiL2-MIB", "atiL2EthMonModuleId"),
)
if mibBuilder.loadTexts:
    atiL2EthMonStatsEntry.setStatus("mandatory")
_AtiL2EthMonModuleId_Type = Integer32
_AtiL2EthMonModuleId_Object = MibTableColumn
atiL2EthMonModuleId = _AtiL2EthMonModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 1, 1, 1, 1),
    _AtiL2EthMonModuleId_Type()
)
atiL2EthMonModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthMonModuleId.setStatus("mandatory")
_AtiL2EthMonRxGoodFrames_Type = Counter32
_AtiL2EthMonRxGoodFrames_Object = MibTableColumn
atiL2EthMonRxGoodFrames = _AtiL2EthMonRxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 1, 1, 1, 2),
    _AtiL2EthMonRxGoodFrames_Type()
)
atiL2EthMonRxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthMonRxGoodFrames.setStatus("mandatory")
_AtiL2EthMonTxGoodFrames_Type = Counter32
_AtiL2EthMonTxGoodFrames_Object = MibTableColumn
atiL2EthMonTxGoodFrames = _AtiL2EthMonTxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 1, 1, 1, 3),
    _AtiL2EthMonTxGoodFrames_Type()
)
atiL2EthMonTxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthMonTxGoodFrames.setStatus("mandatory")
_AtiL2EthMonTxTotalBytes_Type = Counter32
_AtiL2EthMonTxTotalBytes_Object = MibTableColumn
atiL2EthMonTxTotalBytes = _AtiL2EthMonTxTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 1, 1, 1, 4),
    _AtiL2EthMonTxTotalBytes_Type()
)
atiL2EthMonTxTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthMonTxTotalBytes.setStatus("mandatory")
_AtiL2EthMonTxDeferred_Type = Counter32
_AtiL2EthMonTxDeferred_Object = MibTableColumn
atiL2EthMonTxDeferred = _AtiL2EthMonTxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 1, 1, 1, 5),
    _AtiL2EthMonTxDeferred_Type()
)
atiL2EthMonTxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthMonTxDeferred.setStatus("deprecated")
_AtiL2EthMonTxCollisions_Type = Counter32
_AtiL2EthMonTxCollisions_Object = MibTableColumn
atiL2EthMonTxCollisions = _AtiL2EthMonTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 1, 1, 1, 6),
    _AtiL2EthMonTxCollisions_Type()
)
atiL2EthMonTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthMonTxCollisions.setStatus("mandatory")
_AtiL2EthMonTxBroadcastFrames_Type = Counter32
_AtiL2EthMonTxBroadcastFrames_Object = MibTableColumn
atiL2EthMonTxBroadcastFrames = _AtiL2EthMonTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 1, 1, 1, 7),
    _AtiL2EthMonTxBroadcastFrames_Type()
)
atiL2EthMonTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthMonTxBroadcastFrames.setStatus("mandatory")
_AtiL2EthMonTxMulticastFrames_Type = Counter32
_AtiL2EthMonTxMulticastFrames_Object = MibTableColumn
atiL2EthMonTxMulticastFrames = _AtiL2EthMonTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 1, 1, 1, 8),
    _AtiL2EthMonTxMulticastFrames_Type()
)
atiL2EthMonTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthMonTxMulticastFrames.setStatus("mandatory")
_AtiL2EthMonRxOverruns_Type = Counter32
_AtiL2EthMonRxOverruns_Object = MibTableColumn
atiL2EthMonRxOverruns = _AtiL2EthMonRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 1, 1, 1, 9),
    _AtiL2EthMonRxOverruns_Type()
)
atiL2EthMonRxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthMonRxOverruns.setStatus("mandatory")
_AtiL2EthPortMonStatsTable_Object = MibTable
atiL2EthPortMonStatsTable = _AtiL2EthPortMonStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 1, 2)
)
if mibBuilder.loadTexts:
    atiL2EthPortMonStatsTable.setStatus("mandatory")
_AtiL2EthPortMonStatsEntry_Object = MibTableRow
atiL2EthPortMonStatsEntry = _AtiL2EthPortMonStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 1, 2, 1)
)
atiL2EthPortMonStatsEntry.setIndexNames(
    (0, "AtiL2-MIB", "atiL2EthPortMonModuleId"),
    (0, "AtiL2-MIB", "atiL2EthPortMonPortId"),
)
if mibBuilder.loadTexts:
    atiL2EthPortMonStatsEntry.setStatus("mandatory")
_AtiL2EthPortMonModuleId_Type = Integer32
_AtiL2EthPortMonModuleId_Object = MibTableColumn
atiL2EthPortMonModuleId = _AtiL2EthPortMonModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 1, 2, 1, 1),
    _AtiL2EthPortMonModuleId_Type()
)
atiL2EthPortMonModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthPortMonModuleId.setStatus("mandatory")
_AtiL2EthPortMonPortId_Type = Integer32
_AtiL2EthPortMonPortId_Object = MibTableColumn
atiL2EthPortMonPortId = _AtiL2EthPortMonPortId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 1, 2, 1, 2),
    _AtiL2EthPortMonPortId_Type()
)
atiL2EthPortMonPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthPortMonPortId.setStatus("mandatory")
_AtiL2EthPortMonRxGoodFrames_Type = Counter32
_AtiL2EthPortMonRxGoodFrames_Object = MibTableColumn
atiL2EthPortMonRxGoodFrames = _AtiL2EthPortMonRxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 1, 2, 1, 3),
    _AtiL2EthPortMonRxGoodFrames_Type()
)
atiL2EthPortMonRxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthPortMonRxGoodFrames.setStatus("mandatory")
_AtiL2EthPortMonTxGoodFrames_Type = Counter32
_AtiL2EthPortMonTxGoodFrames_Object = MibTableColumn
atiL2EthPortMonTxGoodFrames = _AtiL2EthPortMonTxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 1, 2, 1, 4),
    _AtiL2EthPortMonTxGoodFrames_Type()
)
atiL2EthPortMonTxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthPortMonTxGoodFrames.setStatus("mandatory")
_AtiL2EthPortMonTxTotalBytes_Type = Counter32
_AtiL2EthPortMonTxTotalBytes_Object = MibTableColumn
atiL2EthPortMonTxTotalBytes = _AtiL2EthPortMonTxTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 1, 2, 1, 5),
    _AtiL2EthPortMonTxTotalBytes_Type()
)
atiL2EthPortMonTxTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthPortMonTxTotalBytes.setStatus("mandatory")
_AtiL2EthPortMonTxDeferred_Type = Counter32
_AtiL2EthPortMonTxDeferred_Object = MibTableColumn
atiL2EthPortMonTxDeferred = _AtiL2EthPortMonTxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 1, 2, 1, 6),
    _AtiL2EthPortMonTxDeferred_Type()
)
atiL2EthPortMonTxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthPortMonTxDeferred.setStatus("deprecated")
_AtiL2EthPortMonTxCollisions_Type = Counter32
_AtiL2EthPortMonTxCollisions_Object = MibTableColumn
atiL2EthPortMonTxCollisions = _AtiL2EthPortMonTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 1, 2, 1, 7),
    _AtiL2EthPortMonTxCollisions_Type()
)
atiL2EthPortMonTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthPortMonTxCollisions.setStatus("mandatory")
_AtiL2EthPortMonTxBroadcastFrames_Type = Counter32
_AtiL2EthPortMonTxBroadcastFrames_Object = MibTableColumn
atiL2EthPortMonTxBroadcastFrames = _AtiL2EthPortMonTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 1, 2, 1, 8),
    _AtiL2EthPortMonTxBroadcastFrames_Type()
)
atiL2EthPortMonTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthPortMonTxBroadcastFrames.setStatus("mandatory")
_AtiL2EthPortMonTxMulticastFrames_Type = Counter32
_AtiL2EthPortMonTxMulticastFrames_Object = MibTableColumn
atiL2EthPortMonTxMulticastFrames = _AtiL2EthPortMonTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 1, 2, 1, 9),
    _AtiL2EthPortMonTxMulticastFrames_Type()
)
atiL2EthPortMonTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthPortMonTxMulticastFrames.setStatus("mandatory")
_AtiL2EthPortMonRxOverruns_Type = Counter32
_AtiL2EthPortMonRxOverruns_Object = MibTableColumn
atiL2EthPortMonRxOverruns = _AtiL2EthPortMonRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 1, 2, 1, 10),
    _AtiL2EthPortMonRxOverruns_Type()
)
atiL2EthPortMonRxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthPortMonRxOverruns.setStatus("mandatory")
_AtiL2EthErrStatsGroup_ObjectIdentity = ObjectIdentity
atiL2EthErrStatsGroup = _AtiL2EthErrStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 2)
)
_AtiL2EthErrStatsTable_Object = MibTable
atiL2EthErrStatsTable = _AtiL2EthErrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 2, 1)
)
if mibBuilder.loadTexts:
    atiL2EthErrStatsTable.setStatus("mandatory")
_AtiL2EthErrorStatsEntry_Object = MibTableRow
atiL2EthErrorStatsEntry = _AtiL2EthErrorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 2, 1, 1)
)
atiL2EthErrorStatsEntry.setIndexNames(
    (0, "AtiL2-MIB", "atiL2EthErrModuleId"),
)
if mibBuilder.loadTexts:
    atiL2EthErrorStatsEntry.setStatus("mandatory")
_AtiL2EthErrModuleId_Type = Integer32
_AtiL2EthErrModuleId_Object = MibTableColumn
atiL2EthErrModuleId = _AtiL2EthErrModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 2, 1, 1, 1),
    _AtiL2EthErrModuleId_Type()
)
atiL2EthErrModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthErrModuleId.setStatus("mandatory")
_AtiL2EthErrorCRC_Type = Counter32
_AtiL2EthErrorCRC_Object = MibTableColumn
atiL2EthErrorCRC = _AtiL2EthErrorCRC_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 2, 1, 1, 2),
    _AtiL2EthErrorCRC_Type()
)
atiL2EthErrorCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthErrorCRC.setStatus("mandatory")
_AtiL2EthErrorAlignment_Type = Counter32
_AtiL2EthErrorAlignment_Object = MibTableColumn
atiL2EthErrorAlignment = _AtiL2EthErrorAlignment_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 2, 1, 1, 3),
    _AtiL2EthErrorAlignment_Type()
)
atiL2EthErrorAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthErrorAlignment.setStatus("mandatory")
_AtiL2EthErrorRxBadFrames_Type = Counter32
_AtiL2EthErrorRxBadFrames_Object = MibTableColumn
atiL2EthErrorRxBadFrames = _AtiL2EthErrorRxBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 2, 1, 1, 4),
    _AtiL2EthErrorRxBadFrames_Type()
)
atiL2EthErrorRxBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthErrorRxBadFrames.setStatus("mandatory")
_AtiL2EthErrorLateCollisions_Type = Counter32
_AtiL2EthErrorLateCollisions_Object = MibTableColumn
atiL2EthErrorLateCollisions = _AtiL2EthErrorLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 2, 1, 1, 5),
    _AtiL2EthErrorLateCollisions_Type()
)
atiL2EthErrorLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthErrorLateCollisions.setStatus("mandatory")
_AtiL2EthErrorTxTotal_Type = Counter32
_AtiL2EthErrorTxTotal_Object = MibTableColumn
atiL2EthErrorTxTotal = _AtiL2EthErrorTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 2, 1, 1, 6),
    _AtiL2EthErrorTxTotal_Type()
)
atiL2EthErrorTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthErrorTxTotal.setStatus("mandatory")
_AtiL2EthPortErrStatsTable_Object = MibTable
atiL2EthPortErrStatsTable = _AtiL2EthPortErrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 2, 2)
)
if mibBuilder.loadTexts:
    atiL2EthPortErrStatsTable.setStatus("mandatory")
_AtiL2EthPortErrorStatsEntry_Object = MibTableRow
atiL2EthPortErrorStatsEntry = _AtiL2EthPortErrorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 2, 2, 1)
)
atiL2EthPortErrorStatsEntry.setIndexNames(
    (0, "AtiL2-MIB", "atiL2EthPortErrModuleId"),
    (0, "AtiL2-MIB", "atiL2EthPortErrPortId"),
)
if mibBuilder.loadTexts:
    atiL2EthPortErrorStatsEntry.setStatus("mandatory")
_AtiL2EthPortErrModuleId_Type = Integer32
_AtiL2EthPortErrModuleId_Object = MibTableColumn
atiL2EthPortErrModuleId = _AtiL2EthPortErrModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 2, 2, 1, 1),
    _AtiL2EthPortErrModuleId_Type()
)
atiL2EthPortErrModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthPortErrModuleId.setStatus("mandatory")
_AtiL2EthPortErrPortId_Type = Integer32
_AtiL2EthPortErrPortId_Object = MibTableColumn
atiL2EthPortErrPortId = _AtiL2EthPortErrPortId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 2, 2, 1, 2),
    _AtiL2EthPortErrPortId_Type()
)
atiL2EthPortErrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthPortErrPortId.setStatus("mandatory")
_AtiL2EthPortErrorCRC_Type = Counter32
_AtiL2EthPortErrorCRC_Object = MibTableColumn
atiL2EthPortErrorCRC = _AtiL2EthPortErrorCRC_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 2, 2, 1, 3),
    _AtiL2EthPortErrorCRC_Type()
)
atiL2EthPortErrorCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthPortErrorCRC.setStatus("mandatory")
_AtiL2EthPortErrorAlignment_Type = Counter32
_AtiL2EthPortErrorAlignment_Object = MibTableColumn
atiL2EthPortErrorAlignment = _AtiL2EthPortErrorAlignment_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 2, 2, 1, 4),
    _AtiL2EthPortErrorAlignment_Type()
)
atiL2EthPortErrorAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthPortErrorAlignment.setStatus("mandatory")
_AtiL2EthPortErrorRxBadFrames_Type = Counter32
_AtiL2EthPortErrorRxBadFrames_Object = MibTableColumn
atiL2EthPortErrorRxBadFrames = _AtiL2EthPortErrorRxBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 2, 2, 1, 5),
    _AtiL2EthPortErrorRxBadFrames_Type()
)
atiL2EthPortErrorRxBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthPortErrorRxBadFrames.setStatus("mandatory")
_AtiL2EthPortErrorLateCollisions_Type = Counter32
_AtiL2EthPortErrorLateCollisions_Object = MibTableColumn
atiL2EthPortErrorLateCollisions = _AtiL2EthPortErrorLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 2, 2, 1, 6),
    _AtiL2EthPortErrorLateCollisions_Type()
)
atiL2EthPortErrorLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthPortErrorLateCollisions.setStatus("mandatory")
_AtiL2EthPortErrorTxTotal_Type = Counter32
_AtiL2EthPortErrorTxTotal_Object = MibTableColumn
atiL2EthPortErrorTxTotal = _AtiL2EthPortErrorTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 6, 2, 2, 1, 7),
    _AtiL2EthPortErrorTxTotal_Type()
)
atiL2EthPortErrorTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2EthPortErrorTxTotal.setStatus("mandatory")
_AtiL2DevicePortConfigGroup_ObjectIdentity = ObjectIdentity
atiL2DevicePortConfigGroup = _AtiL2DevicePortConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 7)
)
_AtiL2DevicePortTable_Object = MibTable
atiL2DevicePortTable = _AtiL2DevicePortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 7, 1)
)
if mibBuilder.loadTexts:
    atiL2DevicePortTable.setStatus("mandatory")
_AtiL2DevicePortEntry_Object = MibTableRow
atiL2DevicePortEntry = _AtiL2DevicePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 7, 1, 1)
)
atiL2DevicePortEntry.setIndexNames(
    (0, "AtiL2-MIB", "atiL2DeviceId"),
    (0, "AtiL2-MIB", "atiL2DevicePortNumber"),
)
if mibBuilder.loadTexts:
    atiL2DevicePortEntry.setStatus("mandatory")
_AtiL2DeviceId_Type = Integer32
_AtiL2DeviceId_Object = MibTableColumn
atiL2DeviceId = _AtiL2DeviceId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 7, 1, 1, 1),
    _AtiL2DeviceId_Type()
)
atiL2DeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2DeviceId.setStatus("mandatory")
_AtiL2DevicePortNumber_Type = Integer32
_AtiL2DevicePortNumber_Object = MibTableColumn
atiL2DevicePortNumber = _AtiL2DevicePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 7, 1, 1, 2),
    _AtiL2DevicePortNumber_Type()
)
atiL2DevicePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2DevicePortNumber.setStatus("mandatory")


class _AtiL2DevicePortName_Type(DisplayString):
    """Custom type atiL2DevicePortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtiL2DevicePortName_Type.__name__ = "DisplayString"
_AtiL2DevicePortName_Object = MibTableColumn
atiL2DevicePortName = _AtiL2DevicePortName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 7, 1, 1, 3),
    _AtiL2DevicePortName_Type()
)
atiL2DevicePortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2DevicePortName.setStatus("mandatory")


class _AtiL2DevicePortAutosenseOrHalfDuplex_Type(Integer32):
    """Custom type atiL2DevicePortAutosenseOrHalfDuplex based on Integer32"""
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
        *(("forceFullDuplex-100M", 5),
          ("forceFullDuplex-10M", 4),
          ("forceFullDuplex-1G", 7),
          ("forceHalfDuplex-100M", 3),
          ("forceHalfDuplex-10M", 2),
          ("forceHalfDuplex-1G", 6),
          ("portAutoSense", 1))
    )


_AtiL2DevicePortAutosenseOrHalfDuplex_Type.__name__ = "Integer32"
_AtiL2DevicePortAutosenseOrHalfDuplex_Object = MibTableColumn
atiL2DevicePortAutosenseOrHalfDuplex = _AtiL2DevicePortAutosenseOrHalfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 7, 1, 1, 4),
    _AtiL2DevicePortAutosenseOrHalfDuplex_Type()
)
atiL2DevicePortAutosenseOrHalfDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2DevicePortAutosenseOrHalfDuplex.setStatus("mandatory")


class _AtiL2DevicePortLinkState_Type(Integer32):
    """Custom type atiL2DevicePortLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_AtiL2DevicePortLinkState_Type.__name__ = "Integer32"
_AtiL2DevicePortLinkState_Object = MibTableColumn
atiL2DevicePortLinkState = _AtiL2DevicePortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 7, 1, 1, 5),
    _AtiL2DevicePortLinkState_Type()
)
atiL2DevicePortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2DevicePortLinkState.setStatus("mandatory")


class _AtiL2DevicePortDuplexStatus_Type(Integer32):
    """Custom type atiL2DevicePortDuplexStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autosense", 3),
          ("fullDuplex", 1),
          ("halfDuplex", 2))
    )


_AtiL2DevicePortDuplexStatus_Type.__name__ = "Integer32"
_AtiL2DevicePortDuplexStatus_Object = MibTableColumn
atiL2DevicePortDuplexStatus = _AtiL2DevicePortDuplexStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 7, 1, 1, 6),
    _AtiL2DevicePortDuplexStatus_Type()
)
atiL2DevicePortDuplexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2DevicePortDuplexStatus.setStatus("mandatory")


class _AtiL2DevicePortSpeed_Type(Integer32):
    """Custom type atiL2DevicePortSpeed based on Integer32"""
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
        *(("gigaBits", 3),
          ("hundredMBits", 2),
          ("tenMBits", 1),
          ("unknown", 4))
    )


_AtiL2DevicePortSpeed_Type.__name__ = "Integer32"
_AtiL2DevicePortSpeed_Object = MibTableColumn
atiL2DevicePortSpeed = _AtiL2DevicePortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 7, 1, 1, 7),
    _AtiL2DevicePortSpeed_Type()
)
atiL2DevicePortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2DevicePortSpeed.setStatus("mandatory")


class _AtiL2DevicePortState_Type(Integer32):
    """Custom type atiL2DevicePortState based on Integer32"""
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
        *(("blocking", 3),
          ("disabled", 2),
          ("enabled", 1),
          ("learning", 5),
          ("listening", 4))
    )


_AtiL2DevicePortState_Type.__name__ = "Integer32"
_AtiL2DevicePortState_Object = MibTableColumn
atiL2DevicePortState = _AtiL2DevicePortState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 7, 1, 1, 8),
    _AtiL2DevicePortState_Type()
)
atiL2DevicePortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2DevicePortState.setStatus("mandatory")


class _AtiL2DevicePortTransmitPacingConfig_Type(Integer32):
    """Custom type atiL2DevicePortTransmitPacingConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtiL2DevicePortTransmitPacingConfig_Type.__name__ = "Integer32"
_AtiL2DevicePortTransmitPacingConfig_Object = MibTableColumn
atiL2DevicePortTransmitPacingConfig = _AtiL2DevicePortTransmitPacingConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 7, 1, 1, 9),
    _AtiL2DevicePortTransmitPacingConfig_Type()
)
atiL2DevicePortTransmitPacingConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2DevicePortTransmitPacingConfig.setStatus("mandatory")


class _AtiL2DevicePortSTPConfig_Type(Integer32):
    """Custom type atiL2DevicePortSTPConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtiL2DevicePortSTPConfig_Type.__name__ = "Integer32"
_AtiL2DevicePortSTPConfig_Object = MibTableColumn
atiL2DevicePortSTPConfig = _AtiL2DevicePortSTPConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 7, 1, 1, 10),
    _AtiL2DevicePortSTPConfig_Type()
)
atiL2DevicePortSTPConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2DevicePortSTPConfig.setStatus("mandatory")


class _AtiL2DevicePortBridgeid_Type(Integer32):
    """Custom type atiL2DevicePortBridgeid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AtiL2DevicePortBridgeid_Type.__name__ = "Integer32"
_AtiL2DevicePortBridgeid_Object = MibTableColumn
atiL2DevicePortBridgeid = _AtiL2DevicePortBridgeid_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 7, 1, 1, 11),
    _AtiL2DevicePortBridgeid_Type()
)
atiL2DevicePortBridgeid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2DevicePortBridgeid.setStatus("mandatory")


class _AtiL2DevicePortSTPCost_Type(Integer32):
    """Custom type atiL2DevicePortSTPCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtiL2DevicePortSTPCost_Type.__name__ = "Integer32"
_AtiL2DevicePortSTPCost_Object = MibTableColumn
atiL2DevicePortSTPCost = _AtiL2DevicePortSTPCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 7, 1, 1, 12),
    _AtiL2DevicePortSTPCost_Type()
)
atiL2DevicePortSTPCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2DevicePortSTPCost.setStatus("mandatory")


class _AtiL2DevicePortSTPPriority_Type(Integer32):
    """Custom type atiL2DevicePortSTPPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtiL2DevicePortSTPPriority_Type.__name__ = "Integer32"
_AtiL2DevicePortSTPPriority_Object = MibTableColumn
atiL2DevicePortSTPPriority = _AtiL2DevicePortSTPPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 7, 1, 1, 13),
    _AtiL2DevicePortSTPPriority_Type()
)
atiL2DevicePortSTPPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2DevicePortSTPPriority.setStatus("mandatory")


class _AtiL2DevicePortFlowControlEnable_Type(Integer32):
    """Custom type atiL2DevicePortFlowControlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AtiL2DevicePortFlowControlEnable_Type.__name__ = "Integer32"
_AtiL2DevicePortFlowControlEnable_Object = MibTableColumn
atiL2DevicePortFlowControlEnable = _AtiL2DevicePortFlowControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 7, 1, 1, 14),
    _AtiL2DevicePortFlowControlEnable_Type()
)
atiL2DevicePortFlowControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2DevicePortFlowControlEnable.setStatus("deprecated")


class _AtiL2DevicePortBackPressureEnable_Type(Integer32):
    """Custom type atiL2DevicePortBackPressureEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AtiL2DevicePortBackPressureEnable_Type.__name__ = "Integer32"
_AtiL2DevicePortBackPressureEnable_Object = MibTableColumn
atiL2DevicePortBackPressureEnable = _AtiL2DevicePortBackPressureEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 7, 1, 1, 15),
    _AtiL2DevicePortBackPressureEnable_Type()
)
atiL2DevicePortBackPressureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2DevicePortBackPressureEnable.setStatus("deprecated")


class _AtiL2DevicePortVlanTagPriorityConfig_Type(Integer32):
    """Custom type atiL2DevicePortVlanTagPriorityConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("override-vlan-priority", 2),
          ("use-vlan-priority", 1))
    )


_AtiL2DevicePortVlanTagPriorityConfig_Type.__name__ = "Integer32"
_AtiL2DevicePortVlanTagPriorityConfig_Object = MibTableColumn
atiL2DevicePortVlanTagPriorityConfig = _AtiL2DevicePortVlanTagPriorityConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 7, 1, 1, 16),
    _AtiL2DevicePortVlanTagPriorityConfig_Type()
)
atiL2DevicePortVlanTagPriorityConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2DevicePortVlanTagPriorityConfig.setStatus("deprecated")


class _AtiL2DevicePortQOSPriorityConfig_Type(Integer32):
    """Custom type atiL2DevicePortQOSPriorityConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high-priority", 1),
          ("normal-priority", 2))
    )


_AtiL2DevicePortQOSPriorityConfig_Type.__name__ = "Integer32"
_AtiL2DevicePortQOSPriorityConfig_Object = MibTableColumn
atiL2DevicePortQOSPriorityConfig = _AtiL2DevicePortQOSPriorityConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 7, 1, 1, 17),
    _AtiL2DevicePortQOSPriorityConfig_Type()
)
atiL2DevicePortQOSPriorityConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2DevicePortQOSPriorityConfig.setStatus("deprecated")
_AtiL2VlanConfigGroup_ObjectIdentity = ObjectIdentity
atiL2VlanConfigGroup = _AtiL2VlanConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8)
)
_AtiL2BasicVlanTable_Object = MibTable
atiL2BasicVlanTable = _AtiL2BasicVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 1)
)
if mibBuilder.loadTexts:
    atiL2BasicVlanTable.setStatus("mandatory")
_AtiL2BasicVlanEntry_Object = MibTableRow
atiL2BasicVlanEntry = _AtiL2BasicVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 1, 1)
)
atiL2BasicVlanEntry.setIndexNames(
    (0, "AtiL2-MIB", "atiL2BeVlanIndex"),
)
if mibBuilder.loadTexts:
    atiL2BasicVlanEntry.setStatus("mandatory")


class _AtiL2BeVlanIndex_Type(Integer32):
    """Custom type atiL2BeVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AtiL2BeVlanIndex_Type.__name__ = "Integer32"
_AtiL2BeVlanIndex_Object = MibTableColumn
atiL2BeVlanIndex = _AtiL2BeVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 1, 1, 1),
    _AtiL2BeVlanIndex_Type()
)
atiL2BeVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BeVlanIndex.setStatus("mandatory")


class _AtiL2BeVlanName_Type(DisplayString):
    """Custom type atiL2BeVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtiL2BeVlanName_Type.__name__ = "DisplayString"
_AtiL2BeVlanName_Object = MibTableColumn
atiL2BeVlanName = _AtiL2BeVlanName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 1, 1, 2),
    _AtiL2BeVlanName_Type()
)
atiL2BeVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BeVlanName.setStatus("mandatory")


class _AtiL2BeVlanTagId_Type(Integer32):
    """Custom type atiL2BeVlanTagId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AtiL2BeVlanTagId_Type.__name__ = "Integer32"
_AtiL2BeVlanTagId_Object = MibTableColumn
atiL2BeVlanTagId = _AtiL2BeVlanTagId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 1, 1, 3),
    _AtiL2BeVlanTagId_Type()
)
atiL2BeVlanTagId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BeVlanTagId.setStatus("mandatory")
_AtiL2BeVlanModule1UntaggedPorts_Type = DisplayString
_AtiL2BeVlanModule1UntaggedPorts_Object = MibTableColumn
atiL2BeVlanModule1UntaggedPorts = _AtiL2BeVlanModule1UntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 1, 1, 4),
    _AtiL2BeVlanModule1UntaggedPorts_Type()
)
atiL2BeVlanModule1UntaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BeVlanModule1UntaggedPorts.setStatus("mandatory")
_AtiL2BeVlanModule1TaggedPorts_Type = DisplayString
_AtiL2BeVlanModule1TaggedPorts_Object = MibTableColumn
atiL2BeVlanModule1TaggedPorts = _AtiL2BeVlanModule1TaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 1, 1, 5),
    _AtiL2BeVlanModule1TaggedPorts_Type()
)
atiL2BeVlanModule1TaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BeVlanModule1TaggedPorts.setStatus("mandatory")
_AtiL2BeVlanModule2UntaggedPorts_Type = DisplayString
_AtiL2BeVlanModule2UntaggedPorts_Object = MibTableColumn
atiL2BeVlanModule2UntaggedPorts = _AtiL2BeVlanModule2UntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 1, 1, 6),
    _AtiL2BeVlanModule2UntaggedPorts_Type()
)
atiL2BeVlanModule2UntaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BeVlanModule2UntaggedPorts.setStatus("mandatory")
_AtiL2BeVlanModule2TaggedPorts_Type = DisplayString
_AtiL2BeVlanModule2TaggedPorts_Object = MibTableColumn
atiL2BeVlanModule2TaggedPorts = _AtiL2BeVlanModule2TaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 1, 1, 7),
    _AtiL2BeVlanModule2TaggedPorts_Type()
)
atiL2BeVlanModule2TaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BeVlanModule2TaggedPorts.setStatus("mandatory")
_AtiL2BeVlanModule3UntaggedPorts_Type = DisplayString
_AtiL2BeVlanModule3UntaggedPorts_Object = MibTableColumn
atiL2BeVlanModule3UntaggedPorts = _AtiL2BeVlanModule3UntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 1, 1, 8),
    _AtiL2BeVlanModule3UntaggedPorts_Type()
)
atiL2BeVlanModule3UntaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BeVlanModule3UntaggedPorts.setStatus("mandatory")
_AtiL2BeVlanModule3TaggedPorts_Type = DisplayString
_AtiL2BeVlanModule3TaggedPorts_Object = MibTableColumn
atiL2BeVlanModule3TaggedPorts = _AtiL2BeVlanModule3TaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 1, 1, 9),
    _AtiL2BeVlanModule3TaggedPorts_Type()
)
atiL2BeVlanModule3TaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BeVlanModule3TaggedPorts.setStatus("mandatory")
_AtiL2BeVlanModule4UntaggedPorts_Type = DisplayString
_AtiL2BeVlanModule4UntaggedPorts_Object = MibTableColumn
atiL2BeVlanModule4UntaggedPorts = _AtiL2BeVlanModule4UntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 1, 1, 10),
    _AtiL2BeVlanModule4UntaggedPorts_Type()
)
atiL2BeVlanModule4UntaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BeVlanModule4UntaggedPorts.setStatus("mandatory")
_AtiL2BeVlanModule4TaggedPorts_Type = DisplayString
_AtiL2BeVlanModule4TaggedPorts_Object = MibTableColumn
atiL2BeVlanModule4TaggedPorts = _AtiL2BeVlanModule4TaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 1, 1, 11),
    _AtiL2BeVlanModule4TaggedPorts_Type()
)
atiL2BeVlanModule4TaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BeVlanModule4TaggedPorts.setStatus("mandatory")
_AtiL2BeVlanModule5UntaggedPorts_Type = DisplayString
_AtiL2BeVlanModule5UntaggedPorts_Object = MibTableColumn
atiL2BeVlanModule5UntaggedPorts = _AtiL2BeVlanModule5UntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 1, 1, 12),
    _AtiL2BeVlanModule5UntaggedPorts_Type()
)
atiL2BeVlanModule5UntaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BeVlanModule5UntaggedPorts.setStatus("mandatory")
_AtiL2BeVlanModule5TaggedPorts_Type = DisplayString
_AtiL2BeVlanModule5TaggedPorts_Object = MibTableColumn
atiL2BeVlanModule5TaggedPorts = _AtiL2BeVlanModule5TaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 1, 1, 13),
    _AtiL2BeVlanModule5TaggedPorts_Type()
)
atiL2BeVlanModule5TaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BeVlanModule5TaggedPorts.setStatus("mandatory")
_AtiL2BeVlanModule6UntaggedPorts_Type = DisplayString
_AtiL2BeVlanModule6UntaggedPorts_Object = MibTableColumn
atiL2BeVlanModule6UntaggedPorts = _AtiL2BeVlanModule6UntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 1, 1, 14),
    _AtiL2BeVlanModule6UntaggedPorts_Type()
)
atiL2BeVlanModule6UntaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BeVlanModule6UntaggedPorts.setStatus("mandatory")
_AtiL2BeVlanModule6TaggedPorts_Type = DisplayString
_AtiL2BeVlanModule6TaggedPorts_Object = MibTableColumn
atiL2BeVlanModule6TaggedPorts = _AtiL2BeVlanModule6TaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 1, 1, 15),
    _AtiL2BeVlanModule6TaggedPorts_Type()
)
atiL2BeVlanModule6TaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BeVlanModule6TaggedPorts.setStatus("mandatory")
_AtiL2BeVlanModule7UntaggedPorts_Type = DisplayString
_AtiL2BeVlanModule7UntaggedPorts_Object = MibTableColumn
atiL2BeVlanModule7UntaggedPorts = _AtiL2BeVlanModule7UntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 1, 1, 16),
    _AtiL2BeVlanModule7UntaggedPorts_Type()
)
atiL2BeVlanModule7UntaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BeVlanModule7UntaggedPorts.setStatus("mandatory")
_AtiL2BeVlanModule7TaggedPorts_Type = DisplayString
_AtiL2BeVlanModule7TaggedPorts_Object = MibTableColumn
atiL2BeVlanModule7TaggedPorts = _AtiL2BeVlanModule7TaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 1, 1, 17),
    _AtiL2BeVlanModule7TaggedPorts_Type()
)
atiL2BeVlanModule7TaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BeVlanModule7TaggedPorts.setStatus("mandatory")
_AtiL2BeVlanModule8UntaggedPorts_Type = DisplayString
_AtiL2BeVlanModule8UntaggedPorts_Object = MibTableColumn
atiL2BeVlanModule8UntaggedPorts = _AtiL2BeVlanModule8UntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 1, 1, 18),
    _AtiL2BeVlanModule8UntaggedPorts_Type()
)
atiL2BeVlanModule8UntaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BeVlanModule8UntaggedPorts.setStatus("mandatory")
_AtiL2BeVlanModule8TaggedPorts_Type = DisplayString
_AtiL2BeVlanModule8TaggedPorts_Object = MibTableColumn
atiL2BeVlanModule8TaggedPorts = _AtiL2BeVlanModule8TaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 1, 1, 19),
    _AtiL2BeVlanModule8TaggedPorts_Type()
)
atiL2BeVlanModule8TaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BeVlanModule8TaggedPorts.setStatus("mandatory")


class _AtiL2BeVlanRowStatus_Type(Integer32):
    """Custom type atiL2BeVlanRowStatus based on Integer32"""
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
        *(("idle", 1),
          ("not-operational", 4),
          ("operational", 2),
          ("under-construction", 3))
    )


_AtiL2BeVlanRowStatus_Type.__name__ = "Integer32"
_AtiL2BeVlanRowStatus_Object = MibTableColumn
atiL2BeVlanRowStatus = _AtiL2BeVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 1, 1, 20),
    _AtiL2BeVlanRowStatus_Type()
)
atiL2BeVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BeVlanRowStatus.setStatus("mandatory")
_AtiL2Port2VlanTable_Object = MibTable
atiL2Port2VlanTable = _AtiL2Port2VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 2)
)
if mibBuilder.loadTexts:
    atiL2Port2VlanTable.setStatus("mandatory")
_AtiL2Port2VlanEntry_Object = MibTableRow
atiL2Port2VlanEntry = _AtiL2Port2VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 2, 1)
)
atiL2Port2VlanEntry.setIndexNames(
    (0, "AtiL2-MIB", "atiL2PvModuleId"),
    (0, "AtiL2-MIB", "atiL2PvPortNumber"),
)
if mibBuilder.loadTexts:
    atiL2Port2VlanEntry.setStatus("mandatory")
_AtiL2PvModuleId_Type = Integer32
_AtiL2PvModuleId_Object = MibTableColumn
atiL2PvModuleId = _AtiL2PvModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 2, 1, 1),
    _AtiL2PvModuleId_Type()
)
atiL2PvModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2PvModuleId.setStatus("mandatory")
_AtiL2PvPortNumber_Type = Integer32
_AtiL2PvPortNumber_Object = MibTableColumn
atiL2PvPortNumber = _AtiL2PvPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 2, 1, 2),
    _AtiL2PvPortNumber_Type()
)
atiL2PvPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2PvPortNumber.setStatus("mandatory")
_AtiL2PvVlanName_Type = DisplayString
_AtiL2PvVlanName_Object = MibTableColumn
atiL2PvVlanName = _AtiL2PvVlanName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 8, 2, 1, 3),
    _AtiL2PvVlanName_Type()
)
atiL2PvVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2PvVlanName.setStatus("mandatory")
_AtiL2IfExt_ObjectIdentity = ObjectIdentity
atiL2IfExt = _AtiL2IfExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 9)
)
_AtiL2IfExtensions_ObjectIdentity = ObjectIdentity
atiL2IfExtensions = _AtiL2IfExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 9, 1)
)
_AtiIfExtnTable_Object = MibTable
atiIfExtnTable = _AtiIfExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 9, 1, 1)
)
if mibBuilder.loadTexts:
    atiIfExtnTable.setStatus("mandatory")
_AtiIfExtnEntry_Object = MibTableRow
atiIfExtnEntry = _AtiIfExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 9, 1, 1, 1)
)
atiIfExtnEntry.setIndexNames(
    (0, "AtiL2-MIB", "atiIfExtnIndex"),
)
if mibBuilder.loadTexts:
    atiIfExtnEntry.setStatus("mandatory")


class _AtiIfExtnIndex_Type(Integer32):
    """Custom type atiIfExtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_AtiIfExtnIndex_Type.__name__ = "Integer32"
_AtiIfExtnIndex_Object = MibTableColumn
atiIfExtnIndex = _AtiIfExtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 9, 1, 1, 1, 1),
    _AtiIfExtnIndex_Type()
)
atiIfExtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiIfExtnIndex.setStatus("mandatory")


class _AtiIfExtnModuleId_Type(Integer32):
    """Custom type atiIfExtnModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiIfExtnModuleId_Type.__name__ = "Integer32"
_AtiIfExtnModuleId_Object = MibTableColumn
atiIfExtnModuleId = _AtiIfExtnModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 9, 1, 1, 1, 2),
    _AtiIfExtnModuleId_Type()
)
atiIfExtnModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiIfExtnModuleId.setStatus("mandatory")


class _AtiIfExtnPort_Type(Integer32):
    """Custom type atiIfExtnPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtiIfExtnPort_Type.__name__ = "Integer32"
_AtiIfExtnPort_Object = MibTableColumn
atiIfExtnPort = _AtiIfExtnPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 9, 1, 1, 1, 3),
    _AtiIfExtnPort_Type()
)
atiIfExtnPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiIfExtnPort.setStatus("mandatory")
_AtiL2BridgeMib_ObjectIdentity = ObjectIdentity
atiL2BridgeMib = _AtiL2BridgeMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10)
)
_AtiL2BrBase_ObjectIdentity = ObjectIdentity
atiL2BrBase = _AtiL2BrBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 1)
)
_AtiL2BrBaseTable_Object = MibTable
atiL2BrBaseTable = _AtiL2BrBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 1, 1)
)
if mibBuilder.loadTexts:
    atiL2BrBaseTable.setStatus("mandatory")
_AtiL2BrBaseEntry_Object = MibTableRow
atiL2BrBaseEntry = _AtiL2BrBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 1, 1, 1)
)
atiL2BrBaseEntry.setIndexNames(
    (0, "AtiL2-MIB", "atiL2BrBaseLanId"),
)
if mibBuilder.loadTexts:
    atiL2BrBaseEntry.setStatus("mandatory")
_AtiL2BrBaseLanId_Type = Integer32
_AtiL2BrBaseLanId_Object = MibTableColumn
atiL2BrBaseLanId = _AtiL2BrBaseLanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 1, 1, 1, 1),
    _AtiL2BrBaseLanId_Type()
)
atiL2BrBaseLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrBaseLanId.setStatus("mandatory")
_AtiL2BrBaseBridgeAddress_Type = MacAddress
_AtiL2BrBaseBridgeAddress_Object = MibTableColumn
atiL2BrBaseBridgeAddress = _AtiL2BrBaseBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 1, 1, 1, 2),
    _AtiL2BrBaseBridgeAddress_Type()
)
atiL2BrBaseBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrBaseBridgeAddress.setStatus("mandatory")
_AtiL2BrBaseNumPorts_Type = Integer32
_AtiL2BrBaseNumPorts_Object = MibTableColumn
atiL2BrBaseNumPorts = _AtiL2BrBaseNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 1, 1, 1, 3),
    _AtiL2BrBaseNumPorts_Type()
)
atiL2BrBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrBaseNumPorts.setStatus("mandatory")


class _AtiL2BrBaseType_Type(Integer32):
    """Custom type atiL2BrBaseType based on Integer32"""
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
        *(("sourceroute-only", 3),
          ("srt", 4),
          ("transparent-only", 2),
          ("unknown", 1))
    )


_AtiL2BrBaseType_Type.__name__ = "Integer32"
_AtiL2BrBaseType_Object = MibTableColumn
atiL2BrBaseType = _AtiL2BrBaseType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 1, 1, 1, 4),
    _AtiL2BrBaseType_Type()
)
atiL2BrBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrBaseType.setStatus("mandatory")
_AtiL2BrBasePortTable_Object = MibTable
atiL2BrBasePortTable = _AtiL2BrBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 1, 4)
)
if mibBuilder.loadTexts:
    atiL2BrBasePortTable.setStatus("mandatory")
_AtiL2BrBasePortEntry_Object = MibTableRow
atiL2BrBasePortEntry = _AtiL2BrBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 1, 4, 1)
)
atiL2BrBasePortEntry.setIndexNames(
    (0, "AtiL2-MIB", "atiL2BrBasePortLanId"),
    (0, "AtiL2-MIB", "atiL2BrBasePort"),
)
if mibBuilder.loadTexts:
    atiL2BrBasePortEntry.setStatus("mandatory")
_AtiL2BrBasePortLanId_Type = Integer32
_AtiL2BrBasePortLanId_Object = MibTableColumn
atiL2BrBasePortLanId = _AtiL2BrBasePortLanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 1, 4, 1, 1),
    _AtiL2BrBasePortLanId_Type()
)
atiL2BrBasePortLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrBasePortLanId.setStatus("mandatory")


class _AtiL2BrBasePort_Type(Integer32):
    """Custom type atiL2BrBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtiL2BrBasePort_Type.__name__ = "Integer32"
_AtiL2BrBasePort_Object = MibTableColumn
atiL2BrBasePort = _AtiL2BrBasePort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 1, 4, 1, 2),
    _AtiL2BrBasePort_Type()
)
atiL2BrBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrBasePort.setStatus("mandatory")
_AtiL2BrBasePortIfIndex_Type = Integer32
_AtiL2BrBasePortIfIndex_Object = MibTableColumn
atiL2BrBasePortIfIndex = _AtiL2BrBasePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 1, 4, 1, 3),
    _AtiL2BrBasePortIfIndex_Type()
)
atiL2BrBasePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrBasePortIfIndex.setStatus("mandatory")
_AtiL2BrBasePortCircuit_Type = ObjectIdentifier
_AtiL2BrBasePortCircuit_Object = MibTableColumn
atiL2BrBasePortCircuit = _AtiL2BrBasePortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 1, 4, 1, 4),
    _AtiL2BrBasePortCircuit_Type()
)
atiL2BrBasePortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrBasePortCircuit.setStatus("mandatory")
_AtiL2BrBasePortDelayExceededDiscards_Type = Counter32
_AtiL2BrBasePortDelayExceededDiscards_Object = MibTableColumn
atiL2BrBasePortDelayExceededDiscards = _AtiL2BrBasePortDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 1, 4, 1, 5),
    _AtiL2BrBasePortDelayExceededDiscards_Type()
)
atiL2BrBasePortDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrBasePortDelayExceededDiscards.setStatus("mandatory")
_AtiL2BrBasePortMtuExceededDiscards_Type = Counter32
_AtiL2BrBasePortMtuExceededDiscards_Object = MibTableColumn
atiL2BrBasePortMtuExceededDiscards = _AtiL2BrBasePortMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 1, 4, 1, 6),
    _AtiL2BrBasePortMtuExceededDiscards_Type()
)
atiL2BrBasePortMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrBasePortMtuExceededDiscards.setStatus("mandatory")
_AtiL2BrStp_ObjectIdentity = ObjectIdentity
atiL2BrStp = _AtiL2BrStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2)
)
_AtiL2BrStpTable_Object = MibTable
atiL2BrStpTable = _AtiL2BrStpTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 1)
)
if mibBuilder.loadTexts:
    atiL2BrStpTable.setStatus("mandatory")
_AtiL2BrStpEntry_Object = MibTableRow
atiL2BrStpEntry = _AtiL2BrStpEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 1, 1)
)
atiL2BrStpEntry.setIndexNames(
    (0, "AtiL2-MIB", "atiL2BrStpLanId"),
)
if mibBuilder.loadTexts:
    atiL2BrStpEntry.setStatus("mandatory")
_AtiL2BrStpLanId_Type = Integer32
_AtiL2BrStpLanId_Object = MibTableColumn
atiL2BrStpLanId = _AtiL2BrStpLanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 1, 1, 1),
    _AtiL2BrStpLanId_Type()
)
atiL2BrStpLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrStpLanId.setStatus("mandatory")


class _AtiL2BrStpProtocolSpecification_Type(Integer32):
    """Custom type atiL2BrStpProtocolSpecification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decLb100", 2),
          ("ieee8021d", 3),
          ("unknown", 1))
    )


_AtiL2BrStpProtocolSpecification_Type.__name__ = "Integer32"
_AtiL2BrStpProtocolSpecification_Object = MibTableColumn
atiL2BrStpProtocolSpecification = _AtiL2BrStpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 1, 1, 2),
    _AtiL2BrStpProtocolSpecification_Type()
)
atiL2BrStpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrStpProtocolSpecification.setStatus("mandatory")


class _AtiL2BrStpPriority_Type(Integer32):
    """Custom type atiL2BrStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtiL2BrStpPriority_Type.__name__ = "Integer32"
_AtiL2BrStpPriority_Object = MibTableColumn
atiL2BrStpPriority = _AtiL2BrStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 1, 1, 3),
    _AtiL2BrStpPriority_Type()
)
atiL2BrStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BrStpPriority.setStatus("mandatory")
_AtiL2BrStpTimeSinceTopologyChange_Type = TimeTicks
_AtiL2BrStpTimeSinceTopologyChange_Object = MibTableColumn
atiL2BrStpTimeSinceTopologyChange = _AtiL2BrStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 1, 1, 4),
    _AtiL2BrStpTimeSinceTopologyChange_Type()
)
atiL2BrStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrStpTimeSinceTopologyChange.setStatus("mandatory")
_AtiL2BrStpTopChanges_Type = Counter32
_AtiL2BrStpTopChanges_Object = MibTableColumn
atiL2BrStpTopChanges = _AtiL2BrStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 1, 1, 5),
    _AtiL2BrStpTopChanges_Type()
)
atiL2BrStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrStpTopChanges.setStatus("mandatory")
_AtiL2BrStpDesignatedRoot_Type = BridgeId
_AtiL2BrStpDesignatedRoot_Object = MibTableColumn
atiL2BrStpDesignatedRoot = _AtiL2BrStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 1, 1, 6),
    _AtiL2BrStpDesignatedRoot_Type()
)
atiL2BrStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrStpDesignatedRoot.setStatus("mandatory")
_AtiL2BrStpRootCost_Type = Integer32
_AtiL2BrStpRootCost_Object = MibTableColumn
atiL2BrStpRootCost = _AtiL2BrStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 1, 1, 7),
    _AtiL2BrStpRootCost_Type()
)
atiL2BrStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrStpRootCost.setStatus("mandatory")
_AtiL2BrStpRootPort_Type = Integer32
_AtiL2BrStpRootPort_Object = MibTableColumn
atiL2BrStpRootPort = _AtiL2BrStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 1, 1, 8),
    _AtiL2BrStpRootPort_Type()
)
atiL2BrStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrStpRootPort.setStatus("mandatory")
_AtiL2BrStpMaxAge_Type = Timeout
_AtiL2BrStpMaxAge_Object = MibTableColumn
atiL2BrStpMaxAge = _AtiL2BrStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 1, 1, 9),
    _AtiL2BrStpMaxAge_Type()
)
atiL2BrStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrStpMaxAge.setStatus("mandatory")
_AtiL2BrStpHelloTime_Type = Timeout
_AtiL2BrStpHelloTime_Object = MibTableColumn
atiL2BrStpHelloTime = _AtiL2BrStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 1, 1, 10),
    _AtiL2BrStpHelloTime_Type()
)
atiL2BrStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrStpHelloTime.setStatus("mandatory")
_AtiL2BrStpHoldTime_Type = Integer32
_AtiL2BrStpHoldTime_Object = MibTableColumn
atiL2BrStpHoldTime = _AtiL2BrStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 1, 1, 11),
    _AtiL2BrStpHoldTime_Type()
)
atiL2BrStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrStpHoldTime.setStatus("mandatory")
_AtiL2BrStpForwardDelay_Type = Timeout
_AtiL2BrStpForwardDelay_Object = MibTableColumn
atiL2BrStpForwardDelay = _AtiL2BrStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 1, 1, 12),
    _AtiL2BrStpForwardDelay_Type()
)
atiL2BrStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrStpForwardDelay.setStatus("mandatory")


class _AtiL2BrStpBridgeMaxAge_Type(Timeout):
    """Custom type atiL2BrStpBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_AtiL2BrStpBridgeMaxAge_Type.__name__ = "Timeout"
_AtiL2BrStpBridgeMaxAge_Object = MibTableColumn
atiL2BrStpBridgeMaxAge = _AtiL2BrStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 1, 1, 13),
    _AtiL2BrStpBridgeMaxAge_Type()
)
atiL2BrStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BrStpBridgeMaxAge.setStatus("mandatory")


class _AtiL2BrStpBridgeHelloTime_Type(Timeout):
    """Custom type atiL2BrStpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_AtiL2BrStpBridgeHelloTime_Type.__name__ = "Timeout"
_AtiL2BrStpBridgeHelloTime_Object = MibTableColumn
atiL2BrStpBridgeHelloTime = _AtiL2BrStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 1, 1, 14),
    _AtiL2BrStpBridgeHelloTime_Type()
)
atiL2BrStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BrStpBridgeHelloTime.setStatus("mandatory")


class _AtiL2BrStpBridgeForwardDelay_Type(Timeout):
    """Custom type atiL2BrStpBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_AtiL2BrStpBridgeForwardDelay_Type.__name__ = "Timeout"
_AtiL2BrStpBridgeForwardDelay_Object = MibTableColumn
atiL2BrStpBridgeForwardDelay = _AtiL2BrStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 1, 1, 15),
    _AtiL2BrStpBridgeForwardDelay_Type()
)
atiL2BrStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BrStpBridgeForwardDelay.setStatus("mandatory")
_AtiL2BrStpPortTable_Object = MibTable
atiL2BrStpPortTable = _AtiL2BrStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 15)
)
if mibBuilder.loadTexts:
    atiL2BrStpPortTable.setStatus("mandatory")
_AtiL2BrStpPortEntry_Object = MibTableRow
atiL2BrStpPortEntry = _AtiL2BrStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 15, 1)
)
atiL2BrStpPortEntry.setIndexNames(
    (0, "AtiL2-MIB", "atiL2BrStpPortLanId"),
    (0, "AtiL2-MIB", "atiL2BrStpPort"),
)
if mibBuilder.loadTexts:
    atiL2BrStpPortEntry.setStatus("mandatory")
_AtiL2BrStpPortLanId_Type = Integer32
_AtiL2BrStpPortLanId_Object = MibTableColumn
atiL2BrStpPortLanId = _AtiL2BrStpPortLanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 15, 1, 1),
    _AtiL2BrStpPortLanId_Type()
)
atiL2BrStpPortLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrStpPortLanId.setStatus("mandatory")


class _AtiL2BrStpPort_Type(Integer32):
    """Custom type atiL2BrStpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtiL2BrStpPort_Type.__name__ = "Integer32"
_AtiL2BrStpPort_Object = MibTableColumn
atiL2BrStpPort = _AtiL2BrStpPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 15, 1, 2),
    _AtiL2BrStpPort_Type()
)
atiL2BrStpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrStpPort.setStatus("mandatory")


class _AtiL2BrStpPortPriority_Type(Integer32):
    """Custom type atiL2BrStpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtiL2BrStpPortPriority_Type.__name__ = "Integer32"
_AtiL2BrStpPortPriority_Object = MibTableColumn
atiL2BrStpPortPriority = _AtiL2BrStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 15, 1, 3),
    _AtiL2BrStpPortPriority_Type()
)
atiL2BrStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BrStpPortPriority.setStatus("mandatory")


class _AtiL2BrStpPortState_Type(Integer32):
    """Custom type atiL2BrStpPortState based on Integer32"""
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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_AtiL2BrStpPortState_Type.__name__ = "Integer32"
_AtiL2BrStpPortState_Object = MibTableColumn
atiL2BrStpPortState = _AtiL2BrStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 15, 1, 4),
    _AtiL2BrStpPortState_Type()
)
atiL2BrStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrStpPortState.setStatus("mandatory")


class _AtiL2BrStpPortEnable_Type(Integer32):
    """Custom type atiL2BrStpPortEnable based on Integer32"""
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


_AtiL2BrStpPortEnable_Type.__name__ = "Integer32"
_AtiL2BrStpPortEnable_Object = MibTableColumn
atiL2BrStpPortEnable = _AtiL2BrStpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 15, 1, 5),
    _AtiL2BrStpPortEnable_Type()
)
atiL2BrStpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BrStpPortEnable.setStatus("mandatory")


class _AtiL2BrStpPortPathCost_Type(Integer32):
    """Custom type atiL2BrStpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtiL2BrStpPortPathCost_Type.__name__ = "Integer32"
_AtiL2BrStpPortPathCost_Object = MibTableColumn
atiL2BrStpPortPathCost = _AtiL2BrStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 15, 1, 6),
    _AtiL2BrStpPortPathCost_Type()
)
atiL2BrStpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BrStpPortPathCost.setStatus("mandatory")
_AtiL2BrStpPortDesignatedRoot_Type = BridgeId
_AtiL2BrStpPortDesignatedRoot_Object = MibTableColumn
atiL2BrStpPortDesignatedRoot = _AtiL2BrStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 15, 1, 7),
    _AtiL2BrStpPortDesignatedRoot_Type()
)
atiL2BrStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrStpPortDesignatedRoot.setStatus("mandatory")
_AtiL2BrStpPortDesignatedCost_Type = Integer32
_AtiL2BrStpPortDesignatedCost_Object = MibTableColumn
atiL2BrStpPortDesignatedCost = _AtiL2BrStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 15, 1, 8),
    _AtiL2BrStpPortDesignatedCost_Type()
)
atiL2BrStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrStpPortDesignatedCost.setStatus("mandatory")
_AtiL2BrStpPortDesignatedBridge_Type = BridgeId
_AtiL2BrStpPortDesignatedBridge_Object = MibTableColumn
atiL2BrStpPortDesignatedBridge = _AtiL2BrStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 15, 1, 9),
    _AtiL2BrStpPortDesignatedBridge_Type()
)
atiL2BrStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrStpPortDesignatedBridge.setStatus("mandatory")


class _AtiL2BrStpPortDesignatedPort_Type(OctetString):
    """Custom type atiL2BrStpPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AtiL2BrStpPortDesignatedPort_Type.__name__ = "OctetString"
_AtiL2BrStpPortDesignatedPort_Object = MibTableColumn
atiL2BrStpPortDesignatedPort = _AtiL2BrStpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 15, 1, 10),
    _AtiL2BrStpPortDesignatedPort_Type()
)
atiL2BrStpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrStpPortDesignatedPort.setStatus("mandatory")
_AtiL2BrStpPortForwardTransitions_Type = Counter32
_AtiL2BrStpPortForwardTransitions_Object = MibTableColumn
atiL2BrStpPortForwardTransitions = _AtiL2BrStpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 2, 15, 1, 11),
    _AtiL2BrStpPortForwardTransitions_Type()
)
atiL2BrStpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrStpPortForwardTransitions.setStatus("mandatory")
_AtiL2BrTp_ObjectIdentity = ObjectIdentity
atiL2BrTp = _AtiL2BrTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 3)
)
_AtiL2BrTpTable_Object = MibTable
atiL2BrTpTable = _AtiL2BrTpTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 3, 1)
)
if mibBuilder.loadTexts:
    atiL2BrTpTable.setStatus("mandatory")
_AtiL2BrTpEntry_Object = MibTableRow
atiL2BrTpEntry = _AtiL2BrTpEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 3, 1, 1)
)
atiL2BrTpEntry.setIndexNames(
    (0, "AtiL2-MIB", "atiL2BrTpLanId"),
)
if mibBuilder.loadTexts:
    atiL2BrTpEntry.setStatus("mandatory")
_AtiL2BrTpLanId_Type = Integer32
_AtiL2BrTpLanId_Object = MibTableColumn
atiL2BrTpLanId = _AtiL2BrTpLanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 3, 1, 1, 1),
    _AtiL2BrTpLanId_Type()
)
atiL2BrTpLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrTpLanId.setStatus("mandatory")
_AtiL2BrTpLearnedEntryDiscards_Type = Counter32
_AtiL2BrTpLearnedEntryDiscards_Object = MibTableColumn
atiL2BrTpLearnedEntryDiscards = _AtiL2BrTpLearnedEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 3, 1, 1, 2),
    _AtiL2BrTpLearnedEntryDiscards_Type()
)
atiL2BrTpLearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrTpLearnedEntryDiscards.setStatus("mandatory")


class _AtiL2BrTpAgingTime_Type(Integer32):
    """Custom type atiL2BrTpAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_AtiL2BrTpAgingTime_Type.__name__ = "Integer32"
_AtiL2BrTpAgingTime_Object = MibTableColumn
atiL2BrTpAgingTime = _AtiL2BrTpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 3, 1, 1, 3),
    _AtiL2BrTpAgingTime_Type()
)
atiL2BrTpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2BrTpAgingTime.setStatus("mandatory")
_AtiL2BrTpFdbTable_Object = MibTable
atiL2BrTpFdbTable = _AtiL2BrTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 3, 3)
)
if mibBuilder.loadTexts:
    atiL2BrTpFdbTable.setStatus("mandatory")
_AtiL2BrTpFdbEntry_Object = MibTableRow
atiL2BrTpFdbEntry = _AtiL2BrTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 3, 3, 1)
)
atiL2BrTpFdbEntry.setIndexNames(
    (0, "AtiL2-MIB", "atiL2BrTpFdbLanId"),
    (0, "AtiL2-MIB", "atiL2BrTpFdbAddress"),
)
if mibBuilder.loadTexts:
    atiL2BrTpFdbEntry.setStatus("mandatory")
_AtiL2BrTpFdbLanId_Type = Integer32
_AtiL2BrTpFdbLanId_Object = MibTableColumn
atiL2BrTpFdbLanId = _AtiL2BrTpFdbLanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 3, 3, 1, 1),
    _AtiL2BrTpFdbLanId_Type()
)
atiL2BrTpFdbLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrTpFdbLanId.setStatus("mandatory")
_AtiL2BrTpFdbAddress_Type = MacAddress
_AtiL2BrTpFdbAddress_Object = MibTableColumn
atiL2BrTpFdbAddress = _AtiL2BrTpFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 3, 3, 1, 2),
    _AtiL2BrTpFdbAddress_Type()
)
atiL2BrTpFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrTpFdbAddress.setStatus("mandatory")
_AtiL2BrTpFdbPort_Type = Integer32
_AtiL2BrTpFdbPort_Object = MibTableColumn
atiL2BrTpFdbPort = _AtiL2BrTpFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 3, 3, 1, 3),
    _AtiL2BrTpFdbPort_Type()
)
atiL2BrTpFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrTpFdbPort.setStatus("mandatory")


class _AtiL2BrTpFdbStatus_Type(Integer32):
    """Custom type atiL2BrTpFdbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1),
          ("other", 3))
    )


_AtiL2BrTpFdbStatus_Type.__name__ = "Integer32"
_AtiL2BrTpFdbStatus_Object = MibTableColumn
atiL2BrTpFdbStatus = _AtiL2BrTpFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 3, 3, 1, 4),
    _AtiL2BrTpFdbStatus_Type()
)
atiL2BrTpFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrTpFdbStatus.setStatus("mandatory")
_AtiL2BrTpPortTable_Object = MibTable
atiL2BrTpPortTable = _AtiL2BrTpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 3, 4)
)
if mibBuilder.loadTexts:
    atiL2BrTpPortTable.setStatus("mandatory")
_AtiL2BrTpPortEntry_Object = MibTableRow
atiL2BrTpPortEntry = _AtiL2BrTpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 3, 4, 1)
)
atiL2BrTpPortEntry.setIndexNames(
    (0, "AtiL2-MIB", "atiL2BrTpPortLanId"),
    (0, "AtiL2-MIB", "atiL2BrTpPort"),
)
if mibBuilder.loadTexts:
    atiL2BrTpPortEntry.setStatus("mandatory")
_AtiL2BrTpPortLanId_Type = Integer32
_AtiL2BrTpPortLanId_Object = MibTableColumn
atiL2BrTpPortLanId = _AtiL2BrTpPortLanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 3, 4, 1, 1),
    _AtiL2BrTpPortLanId_Type()
)
atiL2BrTpPortLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrTpPortLanId.setStatus("mandatory")


class _AtiL2BrTpPort_Type(Integer32):
    """Custom type atiL2BrTpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtiL2BrTpPort_Type.__name__ = "Integer32"
_AtiL2BrTpPort_Object = MibTableColumn
atiL2BrTpPort = _AtiL2BrTpPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 3, 4, 1, 2),
    _AtiL2BrTpPort_Type()
)
atiL2BrTpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrTpPort.setStatus("mandatory")
_AtiL2BrTpPortMaxInfo_Type = Integer32
_AtiL2BrTpPortMaxInfo_Object = MibTableColumn
atiL2BrTpPortMaxInfo = _AtiL2BrTpPortMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 3, 4, 1, 3),
    _AtiL2BrTpPortMaxInfo_Type()
)
atiL2BrTpPortMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrTpPortMaxInfo.setStatus("mandatory")
_AtiL2BrTpPortInFrames_Type = Counter32
_AtiL2BrTpPortInFrames_Object = MibTableColumn
atiL2BrTpPortInFrames = _AtiL2BrTpPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 3, 4, 1, 4),
    _AtiL2BrTpPortInFrames_Type()
)
atiL2BrTpPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrTpPortInFrames.setStatus("mandatory")
_AtiL2BrTpPortOutFrames_Type = Counter32
_AtiL2BrTpPortOutFrames_Object = MibTableColumn
atiL2BrTpPortOutFrames = _AtiL2BrTpPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 3, 4, 1, 5),
    _AtiL2BrTpPortOutFrames_Type()
)
atiL2BrTpPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrTpPortOutFrames.setStatus("mandatory")
_AtiL2BrTpPortInDiscards_Type = Counter32
_AtiL2BrTpPortInDiscards_Object = MibTableColumn
atiL2BrTpPortInDiscards = _AtiL2BrTpPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 10, 3, 4, 1, 6),
    _AtiL2BrTpPortInDiscards_Type()
)
atiL2BrTpPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2BrTpPortInDiscards.setStatus("mandatory")
_AtiL2TrapAttrGroup_ObjectIdentity = ObjectIdentity
atiL2TrapAttrGroup = _AtiL2TrapAttrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 11)
)


class _AtiL2TrapAttrModuleId_Type(Integer32):
    """Custom type atiL2TrapAttrModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiL2TrapAttrModuleId_Type.__name__ = "Integer32"
_AtiL2TrapAttrModuleId_Object = MibScalar
atiL2TrapAttrModuleId = _AtiL2TrapAttrModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 11, 1),
    _AtiL2TrapAttrModuleId_Type()
)
atiL2TrapAttrModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atiL2TrapAttrModuleId.setStatus("mandatory")


class _AtiL2TrapAttrPortId_Type(Integer32):
    """Custom type atiL2TrapAttrPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtiL2TrapAttrPortId_Type.__name__ = "Integer32"
_AtiL2TrapAttrPortId_Object = MibScalar
atiL2TrapAttrPortId = _AtiL2TrapAttrPortId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 11, 2),
    _AtiL2TrapAttrPortId_Type()
)
atiL2TrapAttrPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atiL2TrapAttrPortId.setStatus("mandatory")
_AtiL2QOSConfigGroup_ObjectIdentity = ObjectIdentity
atiL2QOSConfigGroup = _AtiL2QOSConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 12)
)


class _AtiL2QOSStatus_Type(Integer32):
    """Custom type atiL2QOSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtiL2QOSStatus_Type.__name__ = "Integer32"
_AtiL2QOSStatus_Object = MibScalar
atiL2QOSStatus = _AtiL2QOSStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 12, 1),
    _AtiL2QOSStatus_Type()
)
atiL2QOSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2QOSStatus.setStatus("mandatory")
_AtiL2TrafficMappingTable_Object = MibTable
atiL2TrafficMappingTable = _AtiL2TrafficMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 12, 2)
)
if mibBuilder.loadTexts:
    atiL2TrafficMappingTable.setStatus("mandatory")
_AtiL2TrafficMappingEntry_Object = MibTableRow
atiL2TrafficMappingEntry = _AtiL2TrafficMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 12, 2, 1)
)
atiL2TrafficMappingEntry.setIndexNames(
    (0, "AtiL2-MIB", "atiL2TrafficClassIndex"),
)
if mibBuilder.loadTexts:
    atiL2TrafficMappingEntry.setStatus("mandatory")


class _AtiL2TrafficClassIndex_Type(Integer32):
    """Custom type atiL2TrafficClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AtiL2TrafficClassIndex_Type.__name__ = "Integer32"
_AtiL2TrafficClassIndex_Object = MibTableColumn
atiL2TrafficClassIndex = _AtiL2TrafficClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 12, 2, 1, 1),
    _AtiL2TrafficClassIndex_Type()
)
atiL2TrafficClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiL2TrafficClassIndex.setStatus("mandatory")


class _AtiL2PriorityQueue_Type(Integer32):
    """Custom type atiL2PriorityQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("highest", 0),
          ("lowest", 1))
    )


_AtiL2PriorityQueue_Type.__name__ = "Integer32"
_AtiL2PriorityQueue_Object = MibTableColumn
atiL2PriorityQueue = _AtiL2PriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 33, 12, 2, 1, 2),
    _AtiL2PriorityQueue_Type()
)
atiL2PriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiL2PriorityQueue.setStatus("mandatory")

# Managed Objects groups


# Notification objects

newRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 0, 101)
)
if mibBuilder.loadTexts:
    newRoot.setStatus(
        ""
    )

topologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 0, 102)
)
if mibBuilder.loadTexts:
    topologyChange.setStatus(
        ""
    )

atiL2FanStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 0, 103)
)
atiL2FanStopTrap.setObjects(
    ("AtiL2-MIB", "atiL2TrapAttrModuleId")
)
if mibBuilder.loadTexts:
    atiL2FanStopTrap.setStatus(
        ""
    )

atiL2TemperatureAbnormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 0, 104)
)
atiL2TemperatureAbnormalTrap.setObjects(
    ("AtiL2-MIB", "atiL2TrapAttrModuleId")
)
if mibBuilder.loadTexts:
    atiL2TemperatureAbnormalTrap.setStatus(
        ""
    )

atiL2PowerSupplyOutage = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 0, 105)
)
atiL2PowerSupplyOutage.setObjects(
    ("AtiL2-MIB", "atiL2TrapAttrModuleId")
)
if mibBuilder.loadTexts:
    atiL2PowerSupplyOutage.setStatus(
        ""
    )

atiL2IntruderAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 0, 106)
)
atiL2IntruderAlert.setObjects(
      *(("AtiL2-MIB", "atiL2TrapAttrModuleId"),
        ("AtiL2-MIB", "atiL2TrapAttrPortId"))
)
if mibBuilder.loadTexts:
    atiL2IntruderAlert.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AtiL2-MIB",
    **{"MacAddress": MacAddress,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "alliedTelesyn": alliedTelesyn,
       "newRoot": newRoot,
       "topologyChange": topologyChange,
       "atiL2FanStopTrap": atiL2FanStopTrap,
       "atiL2TemperatureAbnormalTrap": atiL2TemperatureAbnormalTrap,
       "atiL2PowerSupplyOutage": atiL2PowerSupplyOutage,
       "atiL2IntruderAlert": atiL2IntruderAlert,
       "atiProduct": atiProduct,
       "swhub": swhub,
       "at-8324": at_8324,
       "at-8124XL-V2": at_8124XL_V2,
       "at-8326GB": at_8326GB,
       "at-9410GB": at_9410GB,
       "at-8350GB": at_8350GB,
       "at-8316F": at_8316F,
       "mibObject": mibObject,
       "atiL2Mib": atiL2Mib,
       "atiL2GlobalGroup": atiL2GlobalGroup,
       "atiL2SwProduct": atiL2SwProduct,
       "atiL2SwVersion": atiL2SwVersion,
       "atiL2Reset": atiL2Reset,
       "atiL2MirroringSourceModule": atiL2MirroringSourceModule,
       "atiL2MirroringSourcePort": atiL2MirroringSourcePort,
       "atiL2MirroringDestinationModule": atiL2MirroringDestinationModule,
       "atiL2MirroringDestinationPort": atiL2MirroringDestinationPort,
       "atiL2MirrorState": atiL2MirrorState,
       "atiL2IGMPState": atiL2IGMPState,
       "atiL2DeviceNumber": atiL2DeviceNumber,
       "atiL2IpGroup": atiL2IpGroup,
       "atiL2CurrentIpAddress": atiL2CurrentIpAddress,
       "atiL2ConfiguredIpAddress": atiL2ConfiguredIpAddress,
       "atiL2ConfiguredSubnetMask": atiL2ConfiguredSubnetMask,
       "atiL2ConfiguredRouter": atiL2ConfiguredRouter,
       "atiL2IPAddressStatus": atiL2IPAddressStatus,
       "atiL2DNServer": atiL2DNServer,
       "atiL2DefaultDomainName": atiL2DefaultDomainName,
       "atiL2NMGroup": atiL2NMGroup,
       "atiL2NwMgrTable": atiL2NwMgrTable,
       "atiL2NwMgrEntry": atiL2NwMgrEntry,
       "atiL2NwMgrIndex": atiL2NwMgrIndex,
       "atiL2NwMgrIpAddr": atiL2NwMgrIpAddr,
       "atiL2DHCPGroup": atiL2DHCPGroup,
       "atiL2DHCPSysGroup": atiL2DHCPSysGroup,
       "atiL2DHCPCurrentDHCPClientAddress": atiL2DHCPCurrentDHCPClientAddress,
       "atiL2DHCPSubnetMask": atiL2DHCPSubnetMask,
       "atiL2DHCPCurrentRelayAgentAddress": atiL2DHCPCurrentRelayAgentAddress,
       "atiL2DHCPNextDHCPServerAddress": atiL2DHCPNextDHCPServerAddress,
       "atiL2DHCPTimerGroup": atiL2DHCPTimerGroup,
       "atiL2DHCPLeaseTimer": atiL2DHCPLeaseTimer,
       "atiL2DHCPReacquisitionTimer": atiL2DHCPReacquisitionTimer,
       "atiL2DHCPExpirationTimer": atiL2DHCPExpirationTimer,
       "atiL2DeviceGroup": atiL2DeviceGroup,
       "atiL2deviceTable": atiL2deviceTable,
       "atiL2deviceEntry": atiL2deviceEntry,
       "atiL2deviceIndex": atiL2deviceIndex,
       "atiL2deviceDescr": atiL2deviceDescr,
       "atiL2deviceProductType": atiL2deviceProductType,
       "atiL2devicePortCount": atiL2devicePortCount,
       "atiL2deviceSecurityConfig": atiL2deviceSecurityConfig,
       "atiL2deviceSecurityAction": atiL2deviceSecurityAction,
       "atiL2deviceDebugAvailableBytes": atiL2deviceDebugAvailableBytes,
       "atiL2deviceMDA1Type": atiL2deviceMDA1Type,
       "atiL2deviceMDA2Type": atiL2deviceMDA2Type,
       "atiL2deviceReset": atiL2deviceReset,
       "atiL2EthernetStatsGroup": atiL2EthernetStatsGroup,
       "atiL2EthMonStatsGroup": atiL2EthMonStatsGroup,
       "atiL2EthMonStatsTable": atiL2EthMonStatsTable,
       "atiL2EthMonStatsEntry": atiL2EthMonStatsEntry,
       "atiL2EthMonModuleId": atiL2EthMonModuleId,
       "atiL2EthMonRxGoodFrames": atiL2EthMonRxGoodFrames,
       "atiL2EthMonTxGoodFrames": atiL2EthMonTxGoodFrames,
       "atiL2EthMonTxTotalBytes": atiL2EthMonTxTotalBytes,
       "atiL2EthMonTxDeferred": atiL2EthMonTxDeferred,
       "atiL2EthMonTxCollisions": atiL2EthMonTxCollisions,
       "atiL2EthMonTxBroadcastFrames": atiL2EthMonTxBroadcastFrames,
       "atiL2EthMonTxMulticastFrames": atiL2EthMonTxMulticastFrames,
       "atiL2EthMonRxOverruns": atiL2EthMonRxOverruns,
       "atiL2EthPortMonStatsTable": atiL2EthPortMonStatsTable,
       "atiL2EthPortMonStatsEntry": atiL2EthPortMonStatsEntry,
       "atiL2EthPortMonModuleId": atiL2EthPortMonModuleId,
       "atiL2EthPortMonPortId": atiL2EthPortMonPortId,
       "atiL2EthPortMonRxGoodFrames": atiL2EthPortMonRxGoodFrames,
       "atiL2EthPortMonTxGoodFrames": atiL2EthPortMonTxGoodFrames,
       "atiL2EthPortMonTxTotalBytes": atiL2EthPortMonTxTotalBytes,
       "atiL2EthPortMonTxDeferred": atiL2EthPortMonTxDeferred,
       "atiL2EthPortMonTxCollisions": atiL2EthPortMonTxCollisions,
       "atiL2EthPortMonTxBroadcastFrames": atiL2EthPortMonTxBroadcastFrames,
       "atiL2EthPortMonTxMulticastFrames": atiL2EthPortMonTxMulticastFrames,
       "atiL2EthPortMonRxOverruns": atiL2EthPortMonRxOverruns,
       "atiL2EthErrStatsGroup": atiL2EthErrStatsGroup,
       "atiL2EthErrStatsTable": atiL2EthErrStatsTable,
       "atiL2EthErrorStatsEntry": atiL2EthErrorStatsEntry,
       "atiL2EthErrModuleId": atiL2EthErrModuleId,
       "atiL2EthErrorCRC": atiL2EthErrorCRC,
       "atiL2EthErrorAlignment": atiL2EthErrorAlignment,
       "atiL2EthErrorRxBadFrames": atiL2EthErrorRxBadFrames,
       "atiL2EthErrorLateCollisions": atiL2EthErrorLateCollisions,
       "atiL2EthErrorTxTotal": atiL2EthErrorTxTotal,
       "atiL2EthPortErrStatsTable": atiL2EthPortErrStatsTable,
       "atiL2EthPortErrorStatsEntry": atiL2EthPortErrorStatsEntry,
       "atiL2EthPortErrModuleId": atiL2EthPortErrModuleId,
       "atiL2EthPortErrPortId": atiL2EthPortErrPortId,
       "atiL2EthPortErrorCRC": atiL2EthPortErrorCRC,
       "atiL2EthPortErrorAlignment": atiL2EthPortErrorAlignment,
       "atiL2EthPortErrorRxBadFrames": atiL2EthPortErrorRxBadFrames,
       "atiL2EthPortErrorLateCollisions": atiL2EthPortErrorLateCollisions,
       "atiL2EthPortErrorTxTotal": atiL2EthPortErrorTxTotal,
       "atiL2DevicePortConfigGroup": atiL2DevicePortConfigGroup,
       "atiL2DevicePortTable": atiL2DevicePortTable,
       "atiL2DevicePortEntry": atiL2DevicePortEntry,
       "atiL2DeviceId": atiL2DeviceId,
       "atiL2DevicePortNumber": atiL2DevicePortNumber,
       "atiL2DevicePortName": atiL2DevicePortName,
       "atiL2DevicePortAutosenseOrHalfDuplex": atiL2DevicePortAutosenseOrHalfDuplex,
       "atiL2DevicePortLinkState": atiL2DevicePortLinkState,
       "atiL2DevicePortDuplexStatus": atiL2DevicePortDuplexStatus,
       "atiL2DevicePortSpeed": atiL2DevicePortSpeed,
       "atiL2DevicePortState": atiL2DevicePortState,
       "atiL2DevicePortTransmitPacingConfig": atiL2DevicePortTransmitPacingConfig,
       "atiL2DevicePortSTPConfig": atiL2DevicePortSTPConfig,
       "atiL2DevicePortBridgeid": atiL2DevicePortBridgeid,
       "atiL2DevicePortSTPCost": atiL2DevicePortSTPCost,
       "atiL2DevicePortSTPPriority": atiL2DevicePortSTPPriority,
       "atiL2DevicePortFlowControlEnable": atiL2DevicePortFlowControlEnable,
       "atiL2DevicePortBackPressureEnable": atiL2DevicePortBackPressureEnable,
       "atiL2DevicePortVlanTagPriorityConfig": atiL2DevicePortVlanTagPriorityConfig,
       "atiL2DevicePortQOSPriorityConfig": atiL2DevicePortQOSPriorityConfig,
       "atiL2VlanConfigGroup": atiL2VlanConfigGroup,
       "atiL2BasicVlanTable": atiL2BasicVlanTable,
       "atiL2BasicVlanEntry": atiL2BasicVlanEntry,
       "atiL2BeVlanIndex": atiL2BeVlanIndex,
       "atiL2BeVlanName": atiL2BeVlanName,
       "atiL2BeVlanTagId": atiL2BeVlanTagId,
       "atiL2BeVlanModule1UntaggedPorts": atiL2BeVlanModule1UntaggedPorts,
       "atiL2BeVlanModule1TaggedPorts": atiL2BeVlanModule1TaggedPorts,
       "atiL2BeVlanModule2UntaggedPorts": atiL2BeVlanModule2UntaggedPorts,
       "atiL2BeVlanModule2TaggedPorts": atiL2BeVlanModule2TaggedPorts,
       "atiL2BeVlanModule3UntaggedPorts": atiL2BeVlanModule3UntaggedPorts,
       "atiL2BeVlanModule3TaggedPorts": atiL2BeVlanModule3TaggedPorts,
       "atiL2BeVlanModule4UntaggedPorts": atiL2BeVlanModule4UntaggedPorts,
       "atiL2BeVlanModule4TaggedPorts": atiL2BeVlanModule4TaggedPorts,
       "atiL2BeVlanModule5UntaggedPorts": atiL2BeVlanModule5UntaggedPorts,
       "atiL2BeVlanModule5TaggedPorts": atiL2BeVlanModule5TaggedPorts,
       "atiL2BeVlanModule6UntaggedPorts": atiL2BeVlanModule6UntaggedPorts,
       "atiL2BeVlanModule6TaggedPorts": atiL2BeVlanModule6TaggedPorts,
       "atiL2BeVlanModule7UntaggedPorts": atiL2BeVlanModule7UntaggedPorts,
       "atiL2BeVlanModule7TaggedPorts": atiL2BeVlanModule7TaggedPorts,
       "atiL2BeVlanModule8UntaggedPorts": atiL2BeVlanModule8UntaggedPorts,
       "atiL2BeVlanModule8TaggedPorts": atiL2BeVlanModule8TaggedPorts,
       "atiL2BeVlanRowStatus": atiL2BeVlanRowStatus,
       "atiL2Port2VlanTable": atiL2Port2VlanTable,
       "atiL2Port2VlanEntry": atiL2Port2VlanEntry,
       "atiL2PvModuleId": atiL2PvModuleId,
       "atiL2PvPortNumber": atiL2PvPortNumber,
       "atiL2PvVlanName": atiL2PvVlanName,
       "atiL2IfExt": atiL2IfExt,
       "atiL2IfExtensions": atiL2IfExtensions,
       "atiIfExtnTable": atiIfExtnTable,
       "atiIfExtnEntry": atiIfExtnEntry,
       "atiIfExtnIndex": atiIfExtnIndex,
       "atiIfExtnModuleId": atiIfExtnModuleId,
       "atiIfExtnPort": atiIfExtnPort,
       "atiL2BridgeMib": atiL2BridgeMib,
       "atiL2BrBase": atiL2BrBase,
       "atiL2BrBaseTable": atiL2BrBaseTable,
       "atiL2BrBaseEntry": atiL2BrBaseEntry,
       "atiL2BrBaseLanId": atiL2BrBaseLanId,
       "atiL2BrBaseBridgeAddress": atiL2BrBaseBridgeAddress,
       "atiL2BrBaseNumPorts": atiL2BrBaseNumPorts,
       "atiL2BrBaseType": atiL2BrBaseType,
       "atiL2BrBasePortTable": atiL2BrBasePortTable,
       "atiL2BrBasePortEntry": atiL2BrBasePortEntry,
       "atiL2BrBasePortLanId": atiL2BrBasePortLanId,
       "atiL2BrBasePort": atiL2BrBasePort,
       "atiL2BrBasePortIfIndex": atiL2BrBasePortIfIndex,
       "atiL2BrBasePortCircuit": atiL2BrBasePortCircuit,
       "atiL2BrBasePortDelayExceededDiscards": atiL2BrBasePortDelayExceededDiscards,
       "atiL2BrBasePortMtuExceededDiscards": atiL2BrBasePortMtuExceededDiscards,
       "atiL2BrStp": atiL2BrStp,
       "atiL2BrStpTable": atiL2BrStpTable,
       "atiL2BrStpEntry": atiL2BrStpEntry,
       "atiL2BrStpLanId": atiL2BrStpLanId,
       "atiL2BrStpProtocolSpecification": atiL2BrStpProtocolSpecification,
       "atiL2BrStpPriority": atiL2BrStpPriority,
       "atiL2BrStpTimeSinceTopologyChange": atiL2BrStpTimeSinceTopologyChange,
       "atiL2BrStpTopChanges": atiL2BrStpTopChanges,
       "atiL2BrStpDesignatedRoot": atiL2BrStpDesignatedRoot,
       "atiL2BrStpRootCost": atiL2BrStpRootCost,
       "atiL2BrStpRootPort": atiL2BrStpRootPort,
       "atiL2BrStpMaxAge": atiL2BrStpMaxAge,
       "atiL2BrStpHelloTime": atiL2BrStpHelloTime,
       "atiL2BrStpHoldTime": atiL2BrStpHoldTime,
       "atiL2BrStpForwardDelay": atiL2BrStpForwardDelay,
       "atiL2BrStpBridgeMaxAge": atiL2BrStpBridgeMaxAge,
       "atiL2BrStpBridgeHelloTime": atiL2BrStpBridgeHelloTime,
       "atiL2BrStpBridgeForwardDelay": atiL2BrStpBridgeForwardDelay,
       "atiL2BrStpPortTable": atiL2BrStpPortTable,
       "atiL2BrStpPortEntry": atiL2BrStpPortEntry,
       "atiL2BrStpPortLanId": atiL2BrStpPortLanId,
       "atiL2BrStpPort": atiL2BrStpPort,
       "atiL2BrStpPortPriority": atiL2BrStpPortPriority,
       "atiL2BrStpPortState": atiL2BrStpPortState,
       "atiL2BrStpPortEnable": atiL2BrStpPortEnable,
       "atiL2BrStpPortPathCost": atiL2BrStpPortPathCost,
       "atiL2BrStpPortDesignatedRoot": atiL2BrStpPortDesignatedRoot,
       "atiL2BrStpPortDesignatedCost": atiL2BrStpPortDesignatedCost,
       "atiL2BrStpPortDesignatedBridge": atiL2BrStpPortDesignatedBridge,
       "atiL2BrStpPortDesignatedPort": atiL2BrStpPortDesignatedPort,
       "atiL2BrStpPortForwardTransitions": atiL2BrStpPortForwardTransitions,
       "atiL2BrTp": atiL2BrTp,
       "atiL2BrTpTable": atiL2BrTpTable,
       "atiL2BrTpEntry": atiL2BrTpEntry,
       "atiL2BrTpLanId": atiL2BrTpLanId,
       "atiL2BrTpLearnedEntryDiscards": atiL2BrTpLearnedEntryDiscards,
       "atiL2BrTpAgingTime": atiL2BrTpAgingTime,
       "atiL2BrTpFdbTable": atiL2BrTpFdbTable,
       "atiL2BrTpFdbEntry": atiL2BrTpFdbEntry,
       "atiL2BrTpFdbLanId": atiL2BrTpFdbLanId,
       "atiL2BrTpFdbAddress": atiL2BrTpFdbAddress,
       "atiL2BrTpFdbPort": atiL2BrTpFdbPort,
       "atiL2BrTpFdbStatus": atiL2BrTpFdbStatus,
       "atiL2BrTpPortTable": atiL2BrTpPortTable,
       "atiL2BrTpPortEntry": atiL2BrTpPortEntry,
       "atiL2BrTpPortLanId": atiL2BrTpPortLanId,
       "atiL2BrTpPort": atiL2BrTpPort,
       "atiL2BrTpPortMaxInfo": atiL2BrTpPortMaxInfo,
       "atiL2BrTpPortInFrames": atiL2BrTpPortInFrames,
       "atiL2BrTpPortOutFrames": atiL2BrTpPortOutFrames,
       "atiL2BrTpPortInDiscards": atiL2BrTpPortInDiscards,
       "atiL2TrapAttrGroup": atiL2TrapAttrGroup,
       "atiL2TrapAttrModuleId": atiL2TrapAttrModuleId,
       "atiL2TrapAttrPortId": atiL2TrapAttrPortId,
       "atiL2QOSConfigGroup": atiL2QOSConfigGroup,
       "atiL2QOSStatus": atiL2QOSStatus,
       "atiL2TrafficMappingTable": atiL2TrafficMappingTable,
       "atiL2TrafficMappingEntry": atiL2TrafficMappingEntry,
       "atiL2TrafficClassIndex": atiL2TrafficClassIndex,
       "atiL2PriorityQueue": atiL2PriorityQueue}
)
