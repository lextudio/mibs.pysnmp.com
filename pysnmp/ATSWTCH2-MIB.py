# SNMP MIB module (ATSWTCH2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATSWTCH2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:39 2024
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
_MibObject_ObjectIdentity = ObjectIdentity
mibObject = _MibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8)
)
_AtswitchMib_ObjectIdentity = ObjectIdentity
atswitchMib = _AtswitchMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10)
)
_AtswitchSysGroup_ObjectIdentity = ObjectIdentity
atswitchSysGroup = _AtswitchSysGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 1)
)


class _AtswitchProductType_Type(Integer32):
    """Custom type atswitchProductType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("at-3714", 2),
          ("at-3714FXL", 6),
          ("at-3716XL", 7),
          ("at-3726", 1),
          ("at-3726XL", 5),
          ("at-8118", 4),
          ("at-8124XL", 3),
          ("other", 10))
    )


_AtswitchProductType_Type.__name__ = "Integer32"
_AtswitchProductType_Object = MibScalar
atswitchProductType = _AtswitchProductType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 1, 1),
    _AtswitchProductType_Type()
)
atswitchProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchProductType.setStatus("mandatory")
_AtswitchEthernetPortCount_Type = Integer32
_AtswitchEthernetPortCount_Object = MibScalar
atswitchEthernetPortCount = _AtswitchEthernetPortCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 1, 2),
    _AtswitchEthernetPortCount_Type()
)
atswitchEthernetPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchEthernetPortCount.setStatus("mandatory")


class _AtswitchReset_Type(Integer32):
    """Custom type atswitchReset based on Integer32"""
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


_AtswitchReset_Type.__name__ = "Integer32"
_AtswitchReset_Object = MibScalar
atswitchReset = _AtswitchReset_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 1, 3),
    _AtswitchReset_Type()
)
atswitchReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchReset.setStatus("mandatory")


class _AtswitchMDA1Type_Type(Integer32):
    """Custom type atswitchMDA1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fiber", 2),
          ("none", 3),
          ("rj45-mii", 1))
    )


_AtswitchMDA1Type_Type.__name__ = "Integer32"
_AtswitchMDA1Type_Object = MibScalar
atswitchMDA1Type = _AtswitchMDA1Type_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 1, 4),
    _AtswitchMDA1Type_Type()
)
atswitchMDA1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchMDA1Type.setStatus("mandatory")


class _AtswitchMDA2Type_Type(Integer32):
    """Custom type atswitchMDA2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fiber", 2),
          ("none", 3),
          ("rj45-mii", 1))
    )


_AtswitchMDA2Type_Type.__name__ = "Integer32"
_AtswitchMDA2Type_Object = MibScalar
atswitchMDA2Type = _AtswitchMDA2Type_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 1, 5),
    _AtswitchMDA2Type_Type()
)
atswitchMDA2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchMDA2Type.setStatus("mandatory")


class _AtswitchDeviceFlowControl_Type(Integer32):
    """Custom type atswitchDeviceFlowControl based on Integer32"""
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


_AtswitchDeviceFlowControl_Type.__name__ = "Integer32"
_AtswitchDeviceFlowControl_Object = MibScalar
atswitchDeviceFlowControl = _AtswitchDeviceFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 1, 6),
    _AtswitchDeviceFlowControl_Type()
)
atswitchDeviceFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchDeviceFlowControl.setStatus("mandatory")
_AtswitchSwGroup_ObjectIdentity = ObjectIdentity
atswitchSwGroup = _AtswitchSwGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 1, 7)
)


class _AtswitchSwProduct_Type(DisplayString):
    """Custom type atswitchSwProduct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtswitchSwProduct_Type.__name__ = "DisplayString"
_AtswitchSwProduct_Object = MibScalar
atswitchSwProduct = _AtswitchSwProduct_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 1, 7, 1),
    _AtswitchSwProduct_Type()
)
atswitchSwProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchSwProduct.setStatus("mandatory")


class _AtswitchSwVersion_Type(DisplayString):
    """Custom type atswitchSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtswitchSwVersion_Type.__name__ = "DisplayString"
_AtswitchSwVersion_Object = MibScalar
atswitchSwVersion = _AtswitchSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 1, 7, 2),
    _AtswitchSwVersion_Type()
)
atswitchSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchSwVersion.setStatus("mandatory")
_AtswitchIpGroup_ObjectIdentity = ObjectIdentity
atswitchIpGroup = _AtswitchIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 1, 8)
)
_AtswitchCurrentIpAddress_Type = IpAddress
_AtswitchCurrentIpAddress_Object = MibScalar
atswitchCurrentIpAddress = _AtswitchCurrentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 1, 8, 1),
    _AtswitchCurrentIpAddress_Type()
)
atswitchCurrentIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchCurrentIpAddress.setStatus("mandatory")
_AtswitchConfiguredIpAddress_Type = IpAddress
_AtswitchConfiguredIpAddress_Object = MibScalar
atswitchConfiguredIpAddress = _AtswitchConfiguredIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 1, 8, 2),
    _AtswitchConfiguredIpAddress_Type()
)
atswitchConfiguredIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchConfiguredIpAddress.setStatus("mandatory")
_AtswitchConfiguredSubnetMask_Type = IpAddress
_AtswitchConfiguredSubnetMask_Object = MibScalar
atswitchConfiguredSubnetMask = _AtswitchConfiguredSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 1, 8, 3),
    _AtswitchConfiguredSubnetMask_Type()
)
atswitchConfiguredSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchConfiguredSubnetMask.setStatus("mandatory")
_AtswitchConfiguredRouter_Type = IpAddress
_AtswitchConfiguredRouter_Object = MibScalar
atswitchConfiguredRouter = _AtswitchConfiguredRouter_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 1, 8, 4),
    _AtswitchConfiguredRouter_Type()
)
atswitchConfiguredRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchConfiguredRouter.setStatus("mandatory")


class _AtswitchIPAddressStatus_Type(Integer32):
    """Custom type atswitchIPAddressStatus based on Integer32"""
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


_AtswitchIPAddressStatus_Type.__name__ = "Integer32"
_AtswitchIPAddressStatus_Object = MibScalar
atswitchIPAddressStatus = _AtswitchIPAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 1, 8, 5),
    _AtswitchIPAddressStatus_Type()
)
atswitchIPAddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchIPAddressStatus.setStatus("mandatory")
_AtswitchDNServer_Type = IpAddress
_AtswitchDNServer_Object = MibScalar
atswitchDNServer = _AtswitchDNServer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 1, 8, 6),
    _AtswitchDNServer_Type()
)
atswitchDNServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchDNServer.setStatus("mandatory")


class _AtswitchDefaultDomainName_Type(DisplayString):
    """Custom type atswitchDefaultDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtswitchDefaultDomainName_Type.__name__ = "DisplayString"
_AtswitchDefaultDomainName_Object = MibScalar
atswitchDefaultDomainName = _AtswitchDefaultDomainName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 1, 8, 7),
    _AtswitchDefaultDomainName_Type()
)
atswitchDefaultDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchDefaultDomainName.setStatus("mandatory")
_AtswitchNMGroup_ObjectIdentity = ObjectIdentity
atswitchNMGroup = _AtswitchNMGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 1, 9)
)
_AtswitchNwMgrTable_Object = MibTable
atswitchNwMgrTable = _AtswitchNwMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 1, 9, 1)
)
if mibBuilder.loadTexts:
    atswitchNwMgrTable.setStatus("mandatory")
_AtswitchNwMgrEntry_Object = MibTableRow
atswitchNwMgrEntry = _AtswitchNwMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 1, 9, 1, 1)
)
atswitchNwMgrEntry.setIndexNames(
    (0, "ATSWTCH2-MIB", "atswitchNwMgrIndex"),
)
if mibBuilder.loadTexts:
    atswitchNwMgrEntry.setStatus("mandatory")


class _AtswitchNwMgrIndex_Type(Integer32):
    """Custom type atswitchNwMgrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AtswitchNwMgrIndex_Type.__name__ = "Integer32"
_AtswitchNwMgrIndex_Object = MibTableColumn
atswitchNwMgrIndex = _AtswitchNwMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 1, 9, 1, 1, 1),
    _AtswitchNwMgrIndex_Type()
)
atswitchNwMgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchNwMgrIndex.setStatus("mandatory")
_AtswitchNwMgrIpAddr_Type = IpAddress
_AtswitchNwMgrIpAddr_Object = MibTableColumn
atswitchNwMgrIpAddr = _AtswitchNwMgrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 1, 9, 1, 1, 2),
    _AtswitchNwMgrIpAddr_Type()
)
atswitchNwMgrIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchNwMgrIpAddr.setStatus("mandatory")
_AtswitchConfigGroup_ObjectIdentity = ObjectIdentity
atswitchConfigGroup = _AtswitchConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 2)
)


class _AtswitchPortDisableOnSecurityViolation_Type(Integer32):
    """Custom type atswitchPortDisableOnSecurityViolation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable-on-security-voilation", 1),
          ("security-not-yet-initalized", 3),
          ("suspend-on-double-address", 2))
    )


_AtswitchPortDisableOnSecurityViolation_Type.__name__ = "Integer32"
_AtswitchPortDisableOnSecurityViolation_Object = MibScalar
atswitchPortDisableOnSecurityViolation = _AtswitchPortDisableOnSecurityViolation_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 2, 1),
    _AtswitchPortDisableOnSecurityViolation_Type()
)
atswitchPortDisableOnSecurityViolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchPortDisableOnSecurityViolation.setStatus("mandatory")
_AtswitchMirroringSourcePort_Type = Integer32
_AtswitchMirroringSourcePort_Object = MibScalar
atswitchMirroringSourcePort = _AtswitchMirroringSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 2, 2),
    _AtswitchMirroringSourcePort_Type()
)
atswitchMirroringSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchMirroringSourcePort.setStatus("mandatory")


class _AtswitchMirrorState_Type(Integer32):
    """Custom type atswitchMirrorState based on Integer32"""
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
        *(("both", 3),
          ("disabled", 4),
          ("receive", 1),
          ("transmit", 2))
    )


_AtswitchMirrorState_Type.__name__ = "Integer32"
_AtswitchMirrorState_Object = MibScalar
atswitchMirrorState = _AtswitchMirrorState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 2, 3),
    _AtswitchMirrorState_Type()
)
atswitchMirrorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchMirrorState.setStatus("mandatory")
_AtswitchMirroringDestinationPort_Type = Integer32
_AtswitchMirroringDestinationPort_Object = MibScalar
atswitchMirroringDestinationPort = _AtswitchMirroringDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 2, 4),
    _AtswitchMirroringDestinationPort_Type()
)
atswitchMirroringDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchMirroringDestinationPort.setStatus("mandatory")


class _AtswitchSecurityConfig_Type(Integer32):
    """Custom type atswitchSecurityConfig based on Integer32"""
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


_AtswitchSecurityConfig_Type.__name__ = "Integer32"
_AtswitchSecurityConfig_Object = MibScalar
atswitchSecurityConfig = _AtswitchSecurityConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 2, 5),
    _AtswitchSecurityConfig_Type()
)
atswitchSecurityConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchSecurityConfig.setStatus("mandatory")


class _AtswitchSecurityAction_Type(Integer32):
    """Custom type atswitchSecurityAction based on Integer32"""
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


_AtswitchSecurityAction_Type.__name__ = "Integer32"
_AtswitchSecurityAction_Object = MibScalar
atswitchSecurityAction = _AtswitchSecurityAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 2, 6),
    _AtswitchSecurityAction_Type()
)
atswitchSecurityAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchSecurityAction.setStatus("mandatory")
_AtswitchDebugAvailableBytes_Type = Integer32
_AtswitchDebugAvailableBytes_Object = MibScalar
atswitchDebugAvailableBytes = _AtswitchDebugAvailableBytes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 2, 7),
    _AtswitchDebugAvailableBytes_Type()
)
atswitchDebugAvailableBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchDebugAvailableBytes.setStatus("mandatory")


class _AtswitchTrunkConfig_Type(Integer32):
    """Custom type atswitchTrunkConfig based on Integer32"""
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


_AtswitchTrunkConfig_Type.__name__ = "Integer32"
_AtswitchTrunkConfig_Object = MibScalar
atswitchTrunkConfig = _AtswitchTrunkConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 2, 8),
    _AtswitchTrunkConfig_Type()
)
atswitchTrunkConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchTrunkConfig.setStatus("mandatory")
_AtswitchPortConfigGroup_ObjectIdentity = ObjectIdentity
atswitchPortConfigGroup = _AtswitchPortConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 3)
)
_AtswitchPortTable_Object = MibTable
atswitchPortTable = _AtswitchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 3, 1)
)
if mibBuilder.loadTexts:
    atswitchPortTable.setStatus("mandatory")
_AtswitchPortEntry_Object = MibTableRow
atswitchPortEntry = _AtswitchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 3, 1, 1)
)
atswitchPortEntry.setIndexNames(
    (0, "ATSWTCH2-MIB", "atswitchPortNumber"),
)
if mibBuilder.loadTexts:
    atswitchPortEntry.setStatus("mandatory")
_AtswitchPortNumber_Type = Integer32
_AtswitchPortNumber_Object = MibTableColumn
atswitchPortNumber = _AtswitchPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 3, 1, 1, 1),
    _AtswitchPortNumber_Type()
)
atswitchPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchPortNumber.setStatus("mandatory")


class _AtswitchPortName_Type(DisplayString):
    """Custom type atswitchPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtswitchPortName_Type.__name__ = "DisplayString"
_AtswitchPortName_Object = MibTableColumn
atswitchPortName = _AtswitchPortName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 3, 1, 1, 2),
    _AtswitchPortName_Type()
)
atswitchPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchPortName.setStatus("mandatory")


class _AtswitchPortAutosenseOrHalfDuplex_Type(Integer32):
    """Custom type atswitchPortAutosenseOrHalfDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceHalfDuplex", 2),
          ("portAutoSense", 1))
    )


_AtswitchPortAutosenseOrHalfDuplex_Type.__name__ = "Integer32"
_AtswitchPortAutosenseOrHalfDuplex_Object = MibTableColumn
atswitchPortAutosenseOrHalfDuplex = _AtswitchPortAutosenseOrHalfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 3, 1, 1, 3),
    _AtswitchPortAutosenseOrHalfDuplex_Type()
)
atswitchPortAutosenseOrHalfDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchPortAutosenseOrHalfDuplex.setStatus("mandatory")


class _AtswitchPortLinkState_Type(Integer32):
    """Custom type atswitchPortLinkState based on Integer32"""
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


_AtswitchPortLinkState_Type.__name__ = "Integer32"
_AtswitchPortLinkState_Object = MibTableColumn
atswitchPortLinkState = _AtswitchPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 3, 1, 1, 4),
    _AtswitchPortLinkState_Type()
)
atswitchPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchPortLinkState.setStatus("mandatory")


class _AtswitchPortDuplexStatus_Type(Integer32):
    """Custom type atswitchPortDuplexStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2))
    )


_AtswitchPortDuplexStatus_Type.__name__ = "Integer32"
_AtswitchPortDuplexStatus_Object = MibTableColumn
atswitchPortDuplexStatus = _AtswitchPortDuplexStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 3, 1, 1, 5),
    _AtswitchPortDuplexStatus_Type()
)
atswitchPortDuplexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchPortDuplexStatus.setStatus("mandatory")


class _AtswitchPortSpeed_Type(Integer32):
    """Custom type atswitchPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hundredMBits", 2),
          ("tenMBits", 1))
    )


_AtswitchPortSpeed_Type.__name__ = "Integer32"
_AtswitchPortSpeed_Object = MibTableColumn
atswitchPortSpeed = _AtswitchPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 3, 1, 1, 6),
    _AtswitchPortSpeed_Type()
)
atswitchPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchPortSpeed.setStatus("mandatory")


class _AtswitchPortState_Type(Integer32):
    """Custom type atswitchPortState based on Integer32"""
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


_AtswitchPortState_Type.__name__ = "Integer32"
_AtswitchPortState_Object = MibTableColumn
atswitchPortState = _AtswitchPortState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 3, 1, 1, 7),
    _AtswitchPortState_Type()
)
atswitchPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchPortState.setStatus("mandatory")


class _AtswitchPortTransmitPacingConfig_Type(Integer32):
    """Custom type atswitchPortTransmitPacingConfig based on Integer32"""
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


_AtswitchPortTransmitPacingConfig_Type.__name__ = "Integer32"
_AtswitchPortTransmitPacingConfig_Object = MibTableColumn
atswitchPortTransmitPacingConfig = _AtswitchPortTransmitPacingConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 3, 1, 1, 8),
    _AtswitchPortTransmitPacingConfig_Type()
)
atswitchPortTransmitPacingConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchPortTransmitPacingConfig.setStatus("mandatory")


class _AtswitchPortSTPConfig_Type(Integer32):
    """Custom type atswitchPortSTPConfig based on Integer32"""
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


_AtswitchPortSTPConfig_Type.__name__ = "Integer32"
_AtswitchPortSTPConfig_Object = MibTableColumn
atswitchPortSTPConfig = _AtswitchPortSTPConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 3, 1, 1, 9),
    _AtswitchPortSTPConfig_Type()
)
atswitchPortSTPConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchPortSTPConfig.setStatus("mandatory")


class _AtswitchPortBridgeid_Type(Integer32):
    """Custom type atswitchPortBridgeid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AtswitchPortBridgeid_Type.__name__ = "Integer32"
_AtswitchPortBridgeid_Object = MibTableColumn
atswitchPortBridgeid = _AtswitchPortBridgeid_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 3, 1, 1, 10),
    _AtswitchPortBridgeid_Type()
)
atswitchPortBridgeid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchPortBridgeid.setStatus("mandatory")


class _AtswitchPortSTPCost_Type(Integer32):
    """Custom type atswitchPortSTPCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtswitchPortSTPCost_Type.__name__ = "Integer32"
_AtswitchPortSTPCost_Object = MibTableColumn
atswitchPortSTPCost = _AtswitchPortSTPCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 3, 1, 1, 11),
    _AtswitchPortSTPCost_Type()
)
atswitchPortSTPCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchPortSTPCost.setStatus("mandatory")


class _AtswitchPortSTPPriority_Type(Integer32):
    """Custom type atswitchPortSTPPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtswitchPortSTPPriority_Type.__name__ = "Integer32"
_AtswitchPortSTPPriority_Object = MibTableColumn
atswitchPortSTPPriority = _AtswitchPortSTPPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 3, 1, 1, 12),
    _AtswitchPortSTPPriority_Type()
)
atswitchPortSTPPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchPortSTPPriority.setStatus("mandatory")


class _AtswitchPortSwitchingType_Type(Integer32):
    """Custom type atswitchPortSwitchingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast-cut-through", 1),
          ("store-and-forward", 2))
    )


_AtswitchPortSwitchingType_Type.__name__ = "Integer32"
_AtswitchPortSwitchingType_Object = MibTableColumn
atswitchPortSwitchingType = _AtswitchPortSwitchingType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 3, 1, 1, 13),
    _AtswitchPortSwitchingType_Type()
)
atswitchPortSwitchingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchPortSwitchingType.setStatus("mandatory")


class _AtswitchPortFlowControlEnable_Type(Integer32):
    """Custom type atswitchPortFlowControlEnable based on Integer32"""
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


_AtswitchPortFlowControlEnable_Type.__name__ = "Integer32"
_AtswitchPortFlowControlEnable_Object = MibTableColumn
atswitchPortFlowControlEnable = _AtswitchPortFlowControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 3, 1, 1, 14),
    _AtswitchPortFlowControlEnable_Type()
)
atswitchPortFlowControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchPortFlowControlEnable.setStatus("deprecated")
_AtswitchPortSecurityNumberOfAddresses_Type = Integer32
_AtswitchPortSecurityNumberOfAddresses_Object = MibTableColumn
atswitchPortSecurityNumberOfAddresses = _AtswitchPortSecurityNumberOfAddresses_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 3, 1, 1, 15),
    _AtswitchPortSecurityNumberOfAddresses_Type()
)
atswitchPortSecurityNumberOfAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchPortSecurityNumberOfAddresses.setStatus("mandatory")
_AtswitchVlanConfigGroup_ObjectIdentity = ObjectIdentity
atswitchVlanConfigGroup = _AtswitchVlanConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 4)
)
_AtswitchBasicVlanTable_Object = MibTable
atswitchBasicVlanTable = _AtswitchBasicVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 4, 1)
)
if mibBuilder.loadTexts:
    atswitchBasicVlanTable.setStatus("mandatory")
_AtswitchBasicVlanEntry_Object = MibTableRow
atswitchBasicVlanEntry = _AtswitchBasicVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 4, 1, 1)
)
atswitchBasicVlanEntry.setIndexNames(
    (0, "ATSWTCH2-MIB", "atswitchBeVlanIndex"),
)
if mibBuilder.loadTexts:
    atswitchBasicVlanEntry.setStatus("mandatory")


class _AtswitchBeVlanIndex_Type(Integer32):
    """Custom type atswitchBeVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AtswitchBeVlanIndex_Type.__name__ = "Integer32"
_AtswitchBeVlanIndex_Object = MibTableColumn
atswitchBeVlanIndex = _AtswitchBeVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 4, 1, 1, 1),
    _AtswitchBeVlanIndex_Type()
)
atswitchBeVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBeVlanIndex.setStatus("mandatory")


class _AtswitchBeVlanName_Type(DisplayString):
    """Custom type atswitchBeVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtswitchBeVlanName_Type.__name__ = "DisplayString"
_AtswitchBeVlanName_Object = MibTableColumn
atswitchBeVlanName = _AtswitchBeVlanName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 4, 1, 1, 2),
    _AtswitchBeVlanName_Type()
)
atswitchBeVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchBeVlanName.setStatus("mandatory")


class _AtswitchBeVlanTagId_Type(Integer32):
    """Custom type atswitchBeVlanTagId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AtswitchBeVlanTagId_Type.__name__ = "Integer32"
_AtswitchBeVlanTagId_Object = MibTableColumn
atswitchBeVlanTagId = _AtswitchBeVlanTagId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 4, 1, 1, 3),
    _AtswitchBeVlanTagId_Type()
)
atswitchBeVlanTagId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchBeVlanTagId.setStatus("mandatory")
_AtswitchBeVlanPortMask_Type = DisplayString
_AtswitchBeVlanPortMask_Object = MibTableColumn
atswitchBeVlanPortMask = _AtswitchBeVlanPortMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 4, 1, 1, 4),
    _AtswitchBeVlanPortMask_Type()
)
atswitchBeVlanPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchBeVlanPortMask.setStatus("mandatory")


class _AtswitchBeVlanRowStatus_Type(Integer32):
    """Custom type atswitchBeVlanRowStatus based on Integer32"""
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


_AtswitchBeVlanRowStatus_Type.__name__ = "Integer32"
_AtswitchBeVlanRowStatus_Object = MibTableColumn
atswitchBeVlanRowStatus = _AtswitchBeVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 4, 1, 1, 5),
    _AtswitchBeVlanRowStatus_Type()
)
atswitchBeVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchBeVlanRowStatus.setStatus("mandatory")
_AtswitchPort2VlanTable_Object = MibTable
atswitchPort2VlanTable = _AtswitchPort2VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 4, 2)
)
if mibBuilder.loadTexts:
    atswitchPort2VlanTable.setStatus("mandatory")
_AtswitchPort2VlanEntry_Object = MibTableRow
atswitchPort2VlanEntry = _AtswitchPort2VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 4, 2, 1)
)
atswitchPort2VlanEntry.setIndexNames(
    (0, "ATSWTCH2-MIB", "atswitchPvPortNumber"),
)
if mibBuilder.loadTexts:
    atswitchPort2VlanEntry.setStatus("mandatory")
_AtswitchPvPortNumber_Type = Integer32
_AtswitchPvPortNumber_Object = MibTableColumn
atswitchPvPortNumber = _AtswitchPvPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 4, 2, 1, 1),
    _AtswitchPvPortNumber_Type()
)
atswitchPvPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchPvPortNumber.setStatus("mandatory")
_AtswitchPvVlanName_Type = DisplayString
_AtswitchPvVlanName_Object = MibTableColumn
atswitchPvVlanName = _AtswitchPvVlanName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 4, 2, 1, 2),
    _AtswitchPvVlanName_Type()
)
atswitchPvVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchPvVlanName.setStatus("mandatory")
_AtswitchEthernetStatsGroup_ObjectIdentity = ObjectIdentity
atswitchEthernetStatsGroup = _AtswitchEthernetStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 5)
)
_AtswitchEthMonStats_ObjectIdentity = ObjectIdentity
atswitchEthMonStats = _AtswitchEthMonStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 5, 1)
)
_AtswitchEthMonRxGoodFrames_Type = Counter32
_AtswitchEthMonRxGoodFrames_Object = MibScalar
atswitchEthMonRxGoodFrames = _AtswitchEthMonRxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 5, 1, 1),
    _AtswitchEthMonRxGoodFrames_Type()
)
atswitchEthMonRxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchEthMonRxGoodFrames.setStatus("mandatory")
_AtswitchEthMonTxGoodFrames_Type = Counter32
_AtswitchEthMonTxGoodFrames_Object = MibScalar
atswitchEthMonTxGoodFrames = _AtswitchEthMonTxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 5, 1, 2),
    _AtswitchEthMonTxGoodFrames_Type()
)
atswitchEthMonTxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchEthMonTxGoodFrames.setStatus("mandatory")
_AtswitchEthMonTxTotalBytes_Type = Counter32
_AtswitchEthMonTxTotalBytes_Object = MibScalar
atswitchEthMonTxTotalBytes = _AtswitchEthMonTxTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 5, 1, 3),
    _AtswitchEthMonTxTotalBytes_Type()
)
atswitchEthMonTxTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchEthMonTxTotalBytes.setStatus("mandatory")
_AtswitchEthMonTxDeferred_Type = Counter32
_AtswitchEthMonTxDeferred_Object = MibScalar
atswitchEthMonTxDeferred = _AtswitchEthMonTxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 5, 1, 4),
    _AtswitchEthMonTxDeferred_Type()
)
atswitchEthMonTxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchEthMonTxDeferred.setStatus("mandatory")
_AtswitchEthMonTxCollisions_Type = Counter32
_AtswitchEthMonTxCollisions_Object = MibScalar
atswitchEthMonTxCollisions = _AtswitchEthMonTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 5, 1, 5),
    _AtswitchEthMonTxCollisions_Type()
)
atswitchEthMonTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchEthMonTxCollisions.setStatus("mandatory")
_AtswitchEthErrorStats_ObjectIdentity = ObjectIdentity
atswitchEthErrorStats = _AtswitchEthErrorStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 5, 2)
)
_AtswitchEthErrorCRC_Type = Counter32
_AtswitchEthErrorCRC_Object = MibScalar
atswitchEthErrorCRC = _AtswitchEthErrorCRC_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 5, 2, 1),
    _AtswitchEthErrorCRC_Type()
)
atswitchEthErrorCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchEthErrorCRC.setStatus("mandatory")
_AtswitchEthErrorAlignment_Type = Counter32
_AtswitchEthErrorAlignment_Object = MibScalar
atswitchEthErrorAlignment = _AtswitchEthErrorAlignment_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 5, 2, 2),
    _AtswitchEthErrorAlignment_Type()
)
atswitchEthErrorAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchEthErrorAlignment.setStatus("mandatory")
_AtswitchEthErrorRxBadFrames_Type = Counter32
_AtswitchEthErrorRxBadFrames_Object = MibScalar
atswitchEthErrorRxBadFrames = _AtswitchEthErrorRxBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 5, 2, 3),
    _AtswitchEthErrorRxBadFrames_Type()
)
atswitchEthErrorRxBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchEthErrorRxBadFrames.setStatus("mandatory")
_AtswitchEthErrorLateCollisions_Type = Counter32
_AtswitchEthErrorLateCollisions_Object = MibScalar
atswitchEthErrorLateCollisions = _AtswitchEthErrorLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 5, 2, 4),
    _AtswitchEthErrorLateCollisions_Type()
)
atswitchEthErrorLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchEthErrorLateCollisions.setStatus("mandatory")
_AtswitchEthErrorTxTotal_Type = Counter32
_AtswitchEthErrorTxTotal_Object = MibScalar
atswitchEthErrorTxTotal = _AtswitchEthErrorTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 5, 2, 6),
    _AtswitchEthErrorTxTotal_Type()
)
atswitchEthErrorTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchEthErrorTxTotal.setStatus("mandatory")
_AtswitchEthPortStatsGroup_ObjectIdentity = ObjectIdentity
atswitchEthPortStatsGroup = _AtswitchEthPortStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 6)
)
_AtswitchEthPortMonStats_ObjectIdentity = ObjectIdentity
atswitchEthPortMonStats = _AtswitchEthPortMonStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 6, 1)
)
_AtswitchEthPortMonTable_Object = MibTable
atswitchEthPortMonTable = _AtswitchEthPortMonTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 6, 1, 1)
)
if mibBuilder.loadTexts:
    atswitchEthPortMonTable.setStatus("mandatory")
_AtswitchEthPortMonEntry_Object = MibTableRow
atswitchEthPortMonEntry = _AtswitchEthPortMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 6, 1, 1, 1)
)
atswitchEthPortMonEntry.setIndexNames(
    (0, "ATSWTCH2-MIB", "atswitchEthPortMonId"),
)
if mibBuilder.loadTexts:
    atswitchEthPortMonEntry.setStatus("mandatory")
_AtswitchEthPortMonId_Type = Integer32
_AtswitchEthPortMonId_Object = MibTableColumn
atswitchEthPortMonId = _AtswitchEthPortMonId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 6, 1, 1, 1, 1),
    _AtswitchEthPortMonId_Type()
)
atswitchEthPortMonId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchEthPortMonId.setStatus("mandatory")
_AtswitchEthPortMonTxTotalBytes_Type = Counter32
_AtswitchEthPortMonTxTotalBytes_Object = MibTableColumn
atswitchEthPortMonTxTotalBytes = _AtswitchEthPortMonTxTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 6, 1, 1, 1, 2),
    _AtswitchEthPortMonTxTotalBytes_Type()
)
atswitchEthPortMonTxTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchEthPortMonTxTotalBytes.setStatus("mandatory")
_AtswitchRxGoodFrames_Type = Counter32
_AtswitchRxGoodFrames_Object = MibTableColumn
atswitchRxGoodFrames = _AtswitchRxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 6, 1, 1, 1, 3),
    _AtswitchRxGoodFrames_Type()
)
atswitchRxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchRxGoodFrames.setStatus("mandatory")
_AtswitchTxGoodFrames_Type = Counter32
_AtswitchTxGoodFrames_Object = MibTableColumn
atswitchTxGoodFrames = _AtswitchTxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 6, 1, 1, 1, 4),
    _AtswitchTxGoodFrames_Type()
)
atswitchTxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchTxGoodFrames.setStatus("mandatory")
_AtswitchTxBroadcastFrames_Type = Counter32
_AtswitchTxBroadcastFrames_Object = MibTableColumn
atswitchTxBroadcastFrames = _AtswitchTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 6, 1, 1, 1, 5),
    _AtswitchTxBroadcastFrames_Type()
)
atswitchTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchTxBroadcastFrames.setStatus("mandatory")
_AtswitchTxMulticastFrames_Type = Counter32
_AtswitchTxMulticastFrames_Object = MibTableColumn
atswitchTxMulticastFrames = _AtswitchTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 6, 1, 1, 1, 6),
    _AtswitchTxMulticastFrames_Type()
)
atswitchTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchTxMulticastFrames.setStatus("mandatory")
_AtswitchAddrDuplicate_Type = Counter32
_AtswitchAddrDuplicate_Object = MibTableColumn
atswitchAddrDuplicate = _AtswitchAddrDuplicate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 6, 1, 1, 1, 7),
    _AtswitchAddrDuplicate_Type()
)
atswitchAddrDuplicate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchAddrDuplicate.setStatus("mandatory")
_AtswitchAddrMismatches_Type = Counter32
_AtswitchAddrMismatches_Object = MibTableColumn
atswitchAddrMismatches = _AtswitchAddrMismatches_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 6, 1, 1, 1, 8),
    _AtswitchAddrMismatches_Type()
)
atswitchAddrMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchAddrMismatches.setStatus("mandatory")
_AtswitchRxOverruns_Type = Counter32
_AtswitchRxOverruns_Object = MibTableColumn
atswitchRxOverruns = _AtswitchRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 6, 1, 1, 1, 9),
    _AtswitchRxOverruns_Type()
)
atswitchRxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchRxOverruns.setStatus("mandatory")
_AtswitchEthPortError_ObjectIdentity = ObjectIdentity
atswitchEthPortError = _AtswitchEthPortError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 6, 2)
)
_AtswitchEthPortErrorTable_Object = MibTable
atswitchEthPortErrorTable = _AtswitchEthPortErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 6, 2, 1)
)
if mibBuilder.loadTexts:
    atswitchEthPortErrorTable.setStatus("mandatory")
_AtswitchEthPortErrorEntry_Object = MibTableRow
atswitchEthPortErrorEntry = _AtswitchEthPortErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 6, 2, 1, 1)
)
atswitchEthPortErrorEntry.setIndexNames(
    (0, "ATSWTCH2-MIB", "atswitchEthPortErrorId"),
)
if mibBuilder.loadTexts:
    atswitchEthPortErrorEntry.setStatus("mandatory")
_AtswitchEthPortErrorId_Type = Integer32
_AtswitchEthPortErrorId_Object = MibTableColumn
atswitchEthPortErrorId = _AtswitchEthPortErrorId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 6, 2, 1, 1, 1),
    _AtswitchEthPortErrorId_Type()
)
atswitchEthPortErrorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchEthPortErrorId.setStatus("mandatory")
_AtswitchEthPortErrorRxBadFrames_Type = Counter32
_AtswitchEthPortErrorRxBadFrames_Object = MibTableColumn
atswitchEthPortErrorRxBadFrames = _AtswitchEthPortErrorRxBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 6, 2, 1, 1, 2),
    _AtswitchEthPortErrorRxBadFrames_Type()
)
atswitchEthPortErrorRxBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchEthPortErrorRxBadFrames.setStatus("mandatory")
_AtswitchEthPortErrorTxTotal_Type = Counter32
_AtswitchEthPortErrorTxTotal_Object = MibTableColumn
atswitchEthPortErrorTxTotal = _AtswitchEthPortErrorTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 6, 2, 1, 1, 3),
    _AtswitchEthPortErrorTxTotal_Type()
)
atswitchEthPortErrorTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchEthPortErrorTxTotal.setStatus("mandatory")
_AtswitchFwdVlanGroup_ObjectIdentity = ObjectIdentity
atswitchFwdVlanGroup = _AtswitchFwdVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 7)
)
_AtswitchFwdVlanTable_Object = MibTable
atswitchFwdVlanTable = _AtswitchFwdVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 7, 1)
)
if mibBuilder.loadTexts:
    atswitchFwdVlanTable.setStatus("mandatory")
_AtswitchFwdVlanEntry_Object = MibTableRow
atswitchFwdVlanEntry = _AtswitchFwdVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 7, 1, 1)
)
atswitchFwdVlanEntry.setIndexNames(
    (0, "ATSWTCH2-MIB", "atswitchFwdVlanMACAddr"),
)
if mibBuilder.loadTexts:
    atswitchFwdVlanEntry.setStatus("mandatory")
_AtswitchFwdVlanMACAddr_Type = MacAddress
_AtswitchFwdVlanMACAddr_Object = MibTableColumn
atswitchFwdVlanMACAddr = _AtswitchFwdVlanMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 7, 1, 1, 1),
    _AtswitchFwdVlanMACAddr_Type()
)
atswitchFwdVlanMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchFwdVlanMACAddr.setStatus("mandatory")
_AtswitchFwdVlanVlanId_Type = Integer32
_AtswitchFwdVlanVlanId_Object = MibTableColumn
atswitchFwdVlanVlanId = _AtswitchFwdVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 7, 1, 1, 2),
    _AtswitchFwdVlanVlanId_Type()
)
atswitchFwdVlanVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchFwdVlanVlanId.setStatus("mandatory")
_AtswitchFwdVlanAge_Type = Integer32
_AtswitchFwdVlanAge_Object = MibTableColumn
atswitchFwdVlanAge = _AtswitchFwdVlanAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 7, 1, 1, 3),
    _AtswitchFwdVlanAge_Type()
)
atswitchFwdVlanAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchFwdVlanAge.setStatus("mandatory")


class _AtswitchFwdVlanStatus_Type(Integer32):
    """Custom type atswitchFwdVlanStatus based on Integer32"""
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


_AtswitchFwdVlanStatus_Type.__name__ = "Integer32"
_AtswitchFwdVlanStatus_Object = MibTableColumn
atswitchFwdVlanStatus = _AtswitchFwdVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 7, 1, 1, 4),
    _AtswitchFwdVlanStatus_Type()
)
atswitchFwdVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchFwdVlanStatus.setStatus("mandatory")
_AtswitchFwdVlanPort_Type = Integer32
_AtswitchFwdVlanPort_Object = MibTableColumn
atswitchFwdVlanPort = _AtswitchFwdVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 7, 1, 1, 5),
    _AtswitchFwdVlanPort_Type()
)
atswitchFwdVlanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchFwdVlanPort.setStatus("mandatory")
_AtswitchTrapAttrGroup_ObjectIdentity = ObjectIdentity
atswitchTrapAttrGroup = _AtswitchTrapAttrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 8)
)


class _AtswitchDuplicateMacAddress_Type(OctetString):
    """Custom type atswitchDuplicateMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AtswitchDuplicateMacAddress_Type.__name__ = "OctetString"
_AtswitchDuplicateMacAddress_Object = MibScalar
atswitchDuplicateMacAddress = _AtswitchDuplicateMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 8, 1),
    _AtswitchDuplicateMacAddress_Type()
)
atswitchDuplicateMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atswitchDuplicateMacAddress.setStatus("mandatory")


class _AtswitchIntruderMacAddress_Type(OctetString):
    """Custom type atswitchIntruderMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AtswitchIntruderMacAddress_Type.__name__ = "OctetString"
_AtswitchIntruderMacAddress_Object = MibScalar
atswitchIntruderMacAddress = _AtswitchIntruderMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 8, 2),
    _AtswitchIntruderMacAddress_Type()
)
atswitchIntruderMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atswitchIntruderMacAddress.setStatus("mandatory")
_AtswitchSecuredPortNumber_Type = Integer32
_AtswitchSecuredPortNumber_Object = MibScalar
atswitchSecuredPortNumber = _AtswitchSecuredPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 8, 3),
    _AtswitchSecuredPortNumber_Type()
)
atswitchSecuredPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atswitchSecuredPortNumber.setStatus("mandatory")
_AtswitchBridgeMib_ObjectIdentity = ObjectIdentity
atswitchBridgeMib = _AtswitchBridgeMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9)
)
_AtswitchBrBase_ObjectIdentity = ObjectIdentity
atswitchBrBase = _AtswitchBrBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 1)
)
_AtswitchBrBaseTable_Object = MibTable
atswitchBrBaseTable = _AtswitchBrBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 1, 1)
)
if mibBuilder.loadTexts:
    atswitchBrBaseTable.setStatus("mandatory")
_AtswitchBrBaseEntry_Object = MibTableRow
atswitchBrBaseEntry = _AtswitchBrBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 1, 1, 1)
)
atswitchBrBaseEntry.setIndexNames(
    (0, "ATSWTCH2-MIB", "atswitchBrBaseLanId"),
)
if mibBuilder.loadTexts:
    atswitchBrBaseEntry.setStatus("mandatory")
_AtswitchBrBaseLanId_Type = Integer32
_AtswitchBrBaseLanId_Object = MibTableColumn
atswitchBrBaseLanId = _AtswitchBrBaseLanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 1, 1, 1, 1),
    _AtswitchBrBaseLanId_Type()
)
atswitchBrBaseLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrBaseLanId.setStatus("mandatory")
_AtswitchBrBaseBridgeAddress_Type = MacAddress
_AtswitchBrBaseBridgeAddress_Object = MibTableColumn
atswitchBrBaseBridgeAddress = _AtswitchBrBaseBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 1, 1, 1, 2),
    _AtswitchBrBaseBridgeAddress_Type()
)
atswitchBrBaseBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrBaseBridgeAddress.setStatus("mandatory")
_AtswitchBrBaseNumPorts_Type = Integer32
_AtswitchBrBaseNumPorts_Object = MibTableColumn
atswitchBrBaseNumPorts = _AtswitchBrBaseNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 1, 1, 1, 3),
    _AtswitchBrBaseNumPorts_Type()
)
atswitchBrBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrBaseNumPorts.setStatus("mandatory")


class _AtswitchBrBaseType_Type(Integer32):
    """Custom type atswitchBrBaseType based on Integer32"""
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


_AtswitchBrBaseType_Type.__name__ = "Integer32"
_AtswitchBrBaseType_Object = MibTableColumn
atswitchBrBaseType = _AtswitchBrBaseType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 1, 1, 1, 4),
    _AtswitchBrBaseType_Type()
)
atswitchBrBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrBaseType.setStatus("mandatory")
_AtswitchBrBasePortTable_Object = MibTable
atswitchBrBasePortTable = _AtswitchBrBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 1, 4)
)
if mibBuilder.loadTexts:
    atswitchBrBasePortTable.setStatus("mandatory")
_AtswitchBrBasePortEntry_Object = MibTableRow
atswitchBrBasePortEntry = _AtswitchBrBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 1, 4, 1)
)
atswitchBrBasePortEntry.setIndexNames(
    (0, "ATSWTCH2-MIB", "atswitchBrBasePortLanId"),
    (0, "ATSWTCH2-MIB", "atswitchBrBasePort"),
)
if mibBuilder.loadTexts:
    atswitchBrBasePortEntry.setStatus("mandatory")
_AtswitchBrBasePortLanId_Type = Integer32
_AtswitchBrBasePortLanId_Object = MibTableColumn
atswitchBrBasePortLanId = _AtswitchBrBasePortLanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 1, 4, 1, 1),
    _AtswitchBrBasePortLanId_Type()
)
atswitchBrBasePortLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrBasePortLanId.setStatus("mandatory")


class _AtswitchBrBasePort_Type(Integer32):
    """Custom type atswitchBrBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtswitchBrBasePort_Type.__name__ = "Integer32"
_AtswitchBrBasePort_Object = MibTableColumn
atswitchBrBasePort = _AtswitchBrBasePort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 1, 4, 1, 2),
    _AtswitchBrBasePort_Type()
)
atswitchBrBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrBasePort.setStatus("mandatory")
_AtswitchBrBasePortIfIndex_Type = Integer32
_AtswitchBrBasePortIfIndex_Object = MibTableColumn
atswitchBrBasePortIfIndex = _AtswitchBrBasePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 1, 4, 1, 3),
    _AtswitchBrBasePortIfIndex_Type()
)
atswitchBrBasePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrBasePortIfIndex.setStatus("mandatory")
_AtswitchBrBasePortCircuit_Type = ObjectIdentifier
_AtswitchBrBasePortCircuit_Object = MibTableColumn
atswitchBrBasePortCircuit = _AtswitchBrBasePortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 1, 4, 1, 4),
    _AtswitchBrBasePortCircuit_Type()
)
atswitchBrBasePortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrBasePortCircuit.setStatus("mandatory")
_AtswitchBrBasePortDelayExceededDiscards_Type = Counter32
_AtswitchBrBasePortDelayExceededDiscards_Object = MibTableColumn
atswitchBrBasePortDelayExceededDiscards = _AtswitchBrBasePortDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 1, 4, 1, 5),
    _AtswitchBrBasePortDelayExceededDiscards_Type()
)
atswitchBrBasePortDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrBasePortDelayExceededDiscards.setStatus("mandatory")
_AtswitchBrBasePortMtuExceededDiscards_Type = Counter32
_AtswitchBrBasePortMtuExceededDiscards_Object = MibTableColumn
atswitchBrBasePortMtuExceededDiscards = _AtswitchBrBasePortMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 1, 4, 1, 6),
    _AtswitchBrBasePortMtuExceededDiscards_Type()
)
atswitchBrBasePortMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrBasePortMtuExceededDiscards.setStatus("mandatory")
_AtswitchBrStp_ObjectIdentity = ObjectIdentity
atswitchBrStp = _AtswitchBrStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2)
)
_AtswitchBrStpTable_Object = MibTable
atswitchBrStpTable = _AtswitchBrStpTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 1)
)
if mibBuilder.loadTexts:
    atswitchBrStpTable.setStatus("mandatory")
_AtswitchBrStpEntry_Object = MibTableRow
atswitchBrStpEntry = _AtswitchBrStpEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 1, 1)
)
atswitchBrStpEntry.setIndexNames(
    (0, "ATSWTCH2-MIB", "atswitchBrStpLanId"),
)
if mibBuilder.loadTexts:
    atswitchBrStpEntry.setStatus("mandatory")
_AtswitchBrStpLanId_Type = Integer32
_AtswitchBrStpLanId_Object = MibTableColumn
atswitchBrStpLanId = _AtswitchBrStpLanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 1, 1, 1),
    _AtswitchBrStpLanId_Type()
)
atswitchBrStpLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrStpLanId.setStatus("mandatory")


class _AtswitchBrStpProtocolSpecification_Type(Integer32):
    """Custom type atswitchBrStpProtocolSpecification based on Integer32"""
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


_AtswitchBrStpProtocolSpecification_Type.__name__ = "Integer32"
_AtswitchBrStpProtocolSpecification_Object = MibTableColumn
atswitchBrStpProtocolSpecification = _AtswitchBrStpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 1, 1, 2),
    _AtswitchBrStpProtocolSpecification_Type()
)
atswitchBrStpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrStpProtocolSpecification.setStatus("mandatory")


class _AtswitchBrStpPriority_Type(Integer32):
    """Custom type atswitchBrStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtswitchBrStpPriority_Type.__name__ = "Integer32"
_AtswitchBrStpPriority_Object = MibTableColumn
atswitchBrStpPriority = _AtswitchBrStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 1, 1, 3),
    _AtswitchBrStpPriority_Type()
)
atswitchBrStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchBrStpPriority.setStatus("mandatory")
_AtswitchBrStpTimeSinceTopologyChange_Type = TimeTicks
_AtswitchBrStpTimeSinceTopologyChange_Object = MibTableColumn
atswitchBrStpTimeSinceTopologyChange = _AtswitchBrStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 1, 1, 4),
    _AtswitchBrStpTimeSinceTopologyChange_Type()
)
atswitchBrStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrStpTimeSinceTopologyChange.setStatus("mandatory")
_AtswitchBrStpTopChanges_Type = Counter32
_AtswitchBrStpTopChanges_Object = MibTableColumn
atswitchBrStpTopChanges = _AtswitchBrStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 1, 1, 5),
    _AtswitchBrStpTopChanges_Type()
)
atswitchBrStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrStpTopChanges.setStatus("mandatory")
_AtswitchBrStpDesignatedRoot_Type = BridgeId
_AtswitchBrStpDesignatedRoot_Object = MibTableColumn
atswitchBrStpDesignatedRoot = _AtswitchBrStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 1, 1, 6),
    _AtswitchBrStpDesignatedRoot_Type()
)
atswitchBrStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrStpDesignatedRoot.setStatus("mandatory")
_AtswitchBrStpRootCost_Type = Integer32
_AtswitchBrStpRootCost_Object = MibTableColumn
atswitchBrStpRootCost = _AtswitchBrStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 1, 1, 7),
    _AtswitchBrStpRootCost_Type()
)
atswitchBrStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrStpRootCost.setStatus("mandatory")
_AtswitchBrStpRootPort_Type = Integer32
_AtswitchBrStpRootPort_Object = MibTableColumn
atswitchBrStpRootPort = _AtswitchBrStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 1, 1, 8),
    _AtswitchBrStpRootPort_Type()
)
atswitchBrStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrStpRootPort.setStatus("mandatory")
_AtswitchBrStpMaxAge_Type = Timeout
_AtswitchBrStpMaxAge_Object = MibTableColumn
atswitchBrStpMaxAge = _AtswitchBrStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 1, 1, 9),
    _AtswitchBrStpMaxAge_Type()
)
atswitchBrStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrStpMaxAge.setStatus("mandatory")
_AtswitchBrStpHelloTime_Type = Timeout
_AtswitchBrStpHelloTime_Object = MibTableColumn
atswitchBrStpHelloTime = _AtswitchBrStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 1, 1, 10),
    _AtswitchBrStpHelloTime_Type()
)
atswitchBrStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrStpHelloTime.setStatus("mandatory")
_AtswitchBrStpHoldTime_Type = Integer32
_AtswitchBrStpHoldTime_Object = MibTableColumn
atswitchBrStpHoldTime = _AtswitchBrStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 1, 1, 11),
    _AtswitchBrStpHoldTime_Type()
)
atswitchBrStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrStpHoldTime.setStatus("mandatory")
_AtswitchBrStpForwardDelay_Type = Timeout
_AtswitchBrStpForwardDelay_Object = MibTableColumn
atswitchBrStpForwardDelay = _AtswitchBrStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 1, 1, 12),
    _AtswitchBrStpForwardDelay_Type()
)
atswitchBrStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrStpForwardDelay.setStatus("mandatory")


class _AtswitchBrStpBridgeMaxAge_Type(Timeout):
    """Custom type atswitchBrStpBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_AtswitchBrStpBridgeMaxAge_Type.__name__ = "Timeout"
_AtswitchBrStpBridgeMaxAge_Object = MibTableColumn
atswitchBrStpBridgeMaxAge = _AtswitchBrStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 1, 1, 13),
    _AtswitchBrStpBridgeMaxAge_Type()
)
atswitchBrStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchBrStpBridgeMaxAge.setStatus("mandatory")


class _AtswitchBrStpBridgeHelloTime_Type(Timeout):
    """Custom type atswitchBrStpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_AtswitchBrStpBridgeHelloTime_Type.__name__ = "Timeout"
_AtswitchBrStpBridgeHelloTime_Object = MibTableColumn
atswitchBrStpBridgeHelloTime = _AtswitchBrStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 1, 1, 14),
    _AtswitchBrStpBridgeHelloTime_Type()
)
atswitchBrStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchBrStpBridgeHelloTime.setStatus("mandatory")


class _AtswitchBrStpBridgeForwardDelay_Type(Timeout):
    """Custom type atswitchBrStpBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_AtswitchBrStpBridgeForwardDelay_Type.__name__ = "Timeout"
_AtswitchBrStpBridgeForwardDelay_Object = MibTableColumn
atswitchBrStpBridgeForwardDelay = _AtswitchBrStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 1, 1, 15),
    _AtswitchBrStpBridgeForwardDelay_Type()
)
atswitchBrStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchBrStpBridgeForwardDelay.setStatus("mandatory")
_AtswitchBrStpPortTable_Object = MibTable
atswitchBrStpPortTable = _AtswitchBrStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 15)
)
if mibBuilder.loadTexts:
    atswitchBrStpPortTable.setStatus("mandatory")
_AtswitchBrStpPortEntry_Object = MibTableRow
atswitchBrStpPortEntry = _AtswitchBrStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 15, 1)
)
atswitchBrStpPortEntry.setIndexNames(
    (0, "ATSWTCH2-MIB", "atswitchBrStpPortLanId"),
    (0, "ATSWTCH2-MIB", "atswitchBrStpPort"),
)
if mibBuilder.loadTexts:
    atswitchBrStpPortEntry.setStatus("mandatory")
_AtswitchBrStpPortLanId_Type = Integer32
_AtswitchBrStpPortLanId_Object = MibTableColumn
atswitchBrStpPortLanId = _AtswitchBrStpPortLanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 15, 1, 1),
    _AtswitchBrStpPortLanId_Type()
)
atswitchBrStpPortLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrStpPortLanId.setStatus("mandatory")


class _AtswitchBrStpPort_Type(Integer32):
    """Custom type atswitchBrStpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtswitchBrStpPort_Type.__name__ = "Integer32"
_AtswitchBrStpPort_Object = MibTableColumn
atswitchBrStpPort = _AtswitchBrStpPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 15, 1, 2),
    _AtswitchBrStpPort_Type()
)
atswitchBrStpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrStpPort.setStatus("mandatory")


class _AtswitchBrStpPortPriority_Type(Integer32):
    """Custom type atswitchBrStpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtswitchBrStpPortPriority_Type.__name__ = "Integer32"
_AtswitchBrStpPortPriority_Object = MibTableColumn
atswitchBrStpPortPriority = _AtswitchBrStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 15, 1, 3),
    _AtswitchBrStpPortPriority_Type()
)
atswitchBrStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchBrStpPortPriority.setStatus("mandatory")


class _AtswitchBrStpPortState_Type(Integer32):
    """Custom type atswitchBrStpPortState based on Integer32"""
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


_AtswitchBrStpPortState_Type.__name__ = "Integer32"
_AtswitchBrStpPortState_Object = MibTableColumn
atswitchBrStpPortState = _AtswitchBrStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 15, 1, 4),
    _AtswitchBrStpPortState_Type()
)
atswitchBrStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrStpPortState.setStatus("mandatory")


class _AtswitchBrStpPortEnable_Type(Integer32):
    """Custom type atswitchBrStpPortEnable based on Integer32"""
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


_AtswitchBrStpPortEnable_Type.__name__ = "Integer32"
_AtswitchBrStpPortEnable_Object = MibTableColumn
atswitchBrStpPortEnable = _AtswitchBrStpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 15, 1, 5),
    _AtswitchBrStpPortEnable_Type()
)
atswitchBrStpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchBrStpPortEnable.setStatus("mandatory")


class _AtswitchBrStpPortPathCost_Type(Integer32):
    """Custom type atswitchBrStpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtswitchBrStpPortPathCost_Type.__name__ = "Integer32"
_AtswitchBrStpPortPathCost_Object = MibTableColumn
atswitchBrStpPortPathCost = _AtswitchBrStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 15, 1, 6),
    _AtswitchBrStpPortPathCost_Type()
)
atswitchBrStpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchBrStpPortPathCost.setStatus("mandatory")
_AtswitchBrStpPortDesignatedRoot_Type = BridgeId
_AtswitchBrStpPortDesignatedRoot_Object = MibTableColumn
atswitchBrStpPortDesignatedRoot = _AtswitchBrStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 15, 1, 7),
    _AtswitchBrStpPortDesignatedRoot_Type()
)
atswitchBrStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrStpPortDesignatedRoot.setStatus("mandatory")
_AtswitchBrStpPortDesignatedCost_Type = Integer32
_AtswitchBrStpPortDesignatedCost_Object = MibTableColumn
atswitchBrStpPortDesignatedCost = _AtswitchBrStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 15, 1, 8),
    _AtswitchBrStpPortDesignatedCost_Type()
)
atswitchBrStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrStpPortDesignatedCost.setStatus("mandatory")
_AtswitchBrStpPortDesignatedBridge_Type = BridgeId
_AtswitchBrStpPortDesignatedBridge_Object = MibTableColumn
atswitchBrStpPortDesignatedBridge = _AtswitchBrStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 15, 1, 9),
    _AtswitchBrStpPortDesignatedBridge_Type()
)
atswitchBrStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrStpPortDesignatedBridge.setStatus("mandatory")


class _AtswitchBrStpPortDesignatedPort_Type(OctetString):
    """Custom type atswitchBrStpPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AtswitchBrStpPortDesignatedPort_Type.__name__ = "OctetString"
_AtswitchBrStpPortDesignatedPort_Object = MibTableColumn
atswitchBrStpPortDesignatedPort = _AtswitchBrStpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 15, 1, 10),
    _AtswitchBrStpPortDesignatedPort_Type()
)
atswitchBrStpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrStpPortDesignatedPort.setStatus("mandatory")
_AtswitchBrStpPortForwardTransitions_Type = Counter32
_AtswitchBrStpPortForwardTransitions_Object = MibTableColumn
atswitchBrStpPortForwardTransitions = _AtswitchBrStpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 2, 15, 1, 11),
    _AtswitchBrStpPortForwardTransitions_Type()
)
atswitchBrStpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrStpPortForwardTransitions.setStatus("mandatory")
_AtswitchBrTp_ObjectIdentity = ObjectIdentity
atswitchBrTp = _AtswitchBrTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 3)
)
_AtswitchBrTpTable_Object = MibTable
atswitchBrTpTable = _AtswitchBrTpTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 3, 1)
)
if mibBuilder.loadTexts:
    atswitchBrTpTable.setStatus("mandatory")
_AtswitchBrTpEntry_Object = MibTableRow
atswitchBrTpEntry = _AtswitchBrTpEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 3, 1, 1)
)
atswitchBrTpEntry.setIndexNames(
    (0, "ATSWTCH2-MIB", "atswitchBrTpLanId"),
)
if mibBuilder.loadTexts:
    atswitchBrTpEntry.setStatus("mandatory")
_AtswitchBrTpLanId_Type = Integer32
_AtswitchBrTpLanId_Object = MibTableColumn
atswitchBrTpLanId = _AtswitchBrTpLanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 3, 1, 1, 1),
    _AtswitchBrTpLanId_Type()
)
atswitchBrTpLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrTpLanId.setStatus("mandatory")
_AtswitchBrTpLearnedEntryDiscards_Type = Counter32
_AtswitchBrTpLearnedEntryDiscards_Object = MibTableColumn
atswitchBrTpLearnedEntryDiscards = _AtswitchBrTpLearnedEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 3, 1, 1, 2),
    _AtswitchBrTpLearnedEntryDiscards_Type()
)
atswitchBrTpLearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrTpLearnedEntryDiscards.setStatus("mandatory")


class _AtswitchBrTpAgingTime_Type(Integer32):
    """Custom type atswitchBrTpAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_AtswitchBrTpAgingTime_Type.__name__ = "Integer32"
_AtswitchBrTpAgingTime_Object = MibTableColumn
atswitchBrTpAgingTime = _AtswitchBrTpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 3, 1, 1, 3),
    _AtswitchBrTpAgingTime_Type()
)
atswitchBrTpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchBrTpAgingTime.setStatus("mandatory")
_AtswitchBrTpFdbTable_Object = MibTable
atswitchBrTpFdbTable = _AtswitchBrTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 3, 3)
)
if mibBuilder.loadTexts:
    atswitchBrTpFdbTable.setStatus("mandatory")
_AtswitchBrTpFdbEntry_Object = MibTableRow
atswitchBrTpFdbEntry = _AtswitchBrTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 3, 3, 1)
)
atswitchBrTpFdbEntry.setIndexNames(
    (0, "ATSWTCH2-MIB", "atswitchBrTpFdbLanId"),
    (0, "ATSWTCH2-MIB", "atswitchBrTpFdbAddress"),
)
if mibBuilder.loadTexts:
    atswitchBrTpFdbEntry.setStatus("mandatory")
_AtswitchBrTpFdbLanId_Type = Integer32
_AtswitchBrTpFdbLanId_Object = MibTableColumn
atswitchBrTpFdbLanId = _AtswitchBrTpFdbLanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 3, 3, 1, 1),
    _AtswitchBrTpFdbLanId_Type()
)
atswitchBrTpFdbLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrTpFdbLanId.setStatus("mandatory")
_AtswitchBrTpFdbAddress_Type = MacAddress
_AtswitchBrTpFdbAddress_Object = MibTableColumn
atswitchBrTpFdbAddress = _AtswitchBrTpFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 3, 3, 1, 2),
    _AtswitchBrTpFdbAddress_Type()
)
atswitchBrTpFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrTpFdbAddress.setStatus("mandatory")
_AtswitchBrTpFdbPort_Type = Integer32
_AtswitchBrTpFdbPort_Object = MibTableColumn
atswitchBrTpFdbPort = _AtswitchBrTpFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 3, 3, 1, 3),
    _AtswitchBrTpFdbPort_Type()
)
atswitchBrTpFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrTpFdbPort.setStatus("mandatory")


class _AtswitchBrTpFdbStatus_Type(Integer32):
    """Custom type atswitchBrTpFdbStatus based on Integer32"""
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


_AtswitchBrTpFdbStatus_Type.__name__ = "Integer32"
_AtswitchBrTpFdbStatus_Object = MibTableColumn
atswitchBrTpFdbStatus = _AtswitchBrTpFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 3, 3, 1, 4),
    _AtswitchBrTpFdbStatus_Type()
)
atswitchBrTpFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrTpFdbStatus.setStatus("mandatory")
_AtswitchBrTpPortTable_Object = MibTable
atswitchBrTpPortTable = _AtswitchBrTpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 3, 4)
)
if mibBuilder.loadTexts:
    atswitchBrTpPortTable.setStatus("mandatory")
_AtswitchBrTpPortEntry_Object = MibTableRow
atswitchBrTpPortEntry = _AtswitchBrTpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 3, 4, 1)
)
atswitchBrTpPortEntry.setIndexNames(
    (0, "ATSWTCH2-MIB", "atswitchBrTpPortLanId"),
    (0, "ATSWTCH2-MIB", "atswitchBrTpPort"),
)
if mibBuilder.loadTexts:
    atswitchBrTpPortEntry.setStatus("mandatory")
_AtswitchBrTpPortLanId_Type = Integer32
_AtswitchBrTpPortLanId_Object = MibTableColumn
atswitchBrTpPortLanId = _AtswitchBrTpPortLanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 3, 4, 1, 1),
    _AtswitchBrTpPortLanId_Type()
)
atswitchBrTpPortLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrTpPortLanId.setStatus("mandatory")


class _AtswitchBrTpPort_Type(Integer32):
    """Custom type atswitchBrTpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtswitchBrTpPort_Type.__name__ = "Integer32"
_AtswitchBrTpPort_Object = MibTableColumn
atswitchBrTpPort = _AtswitchBrTpPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 3, 4, 1, 2),
    _AtswitchBrTpPort_Type()
)
atswitchBrTpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrTpPort.setStatus("mandatory")
_AtswitchBrTpPortMaxInfo_Type = Integer32
_AtswitchBrTpPortMaxInfo_Object = MibTableColumn
atswitchBrTpPortMaxInfo = _AtswitchBrTpPortMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 3, 4, 1, 3),
    _AtswitchBrTpPortMaxInfo_Type()
)
atswitchBrTpPortMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrTpPortMaxInfo.setStatus("mandatory")
_AtswitchBrTpPortInFrames_Type = Counter32
_AtswitchBrTpPortInFrames_Object = MibTableColumn
atswitchBrTpPortInFrames = _AtswitchBrTpPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 3, 4, 1, 4),
    _AtswitchBrTpPortInFrames_Type()
)
atswitchBrTpPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrTpPortInFrames.setStatus("mandatory")
_AtswitchBrTpPortOutFrames_Type = Counter32
_AtswitchBrTpPortOutFrames_Object = MibTableColumn
atswitchBrTpPortOutFrames = _AtswitchBrTpPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 3, 4, 1, 5),
    _AtswitchBrTpPortOutFrames_Type()
)
atswitchBrTpPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrTpPortOutFrames.setStatus("mandatory")
_AtswitchBrTpPortInDiscards_Type = Counter32
_AtswitchBrTpPortInDiscards_Object = MibTableColumn
atswitchBrTpPortInDiscards = _AtswitchBrTpPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 9, 3, 4, 1, 6),
    _AtswitchBrTpPortInDiscards_Type()
)
atswitchBrTpPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchBrTpPortInDiscards.setStatus("mandatory")
_AtswitchStaticMACGroup_ObjectIdentity = ObjectIdentity
atswitchStaticMACGroup = _AtswitchStaticMACGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 10)
)
_AtswitchStaticMACTable_Object = MibTable
atswitchStaticMACTable = _AtswitchStaticMACTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 10, 1)
)
if mibBuilder.loadTexts:
    atswitchStaticMACTable.setStatus("mandatory")
_AtswitchStaticMACEntry_Object = MibTableRow
atswitchStaticMACEntry = _AtswitchStaticMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 10, 1, 1)
)
atswitchStaticMACEntry.setIndexNames(
    (0, "ATSWTCH2-MIB", "atswitchStaticMACAddress"),
)
if mibBuilder.loadTexts:
    atswitchStaticMACEntry.setStatus("mandatory")
_AtswitchStaticMACAddress_Type = MacAddress
_AtswitchStaticMACAddress_Object = MibTableColumn
atswitchStaticMACAddress = _AtswitchStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 10, 1, 1, 1),
    _AtswitchStaticMACAddress_Type()
)
atswitchStaticMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchStaticMACAddress.setStatus("mandatory")
_AtswitchStaticMACPortNumbers_Type = DisplayString
_AtswitchStaticMACPortNumbers_Object = MibTableColumn
atswitchStaticMACPortNumbers = _AtswitchStaticMACPortNumbers_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 10, 1, 1, 2),
    _AtswitchStaticMACPortNumbers_Type()
)
atswitchStaticMACPortNumbers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchStaticMACPortNumbers.setStatus("mandatory")
_AtswitchStaticMACVlan_Type = Integer32
_AtswitchStaticMACVlan_Object = MibTableColumn
atswitchStaticMACVlan = _AtswitchStaticMACVlan_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 10, 1, 1, 3),
    _AtswitchStaticMACVlan_Type()
)
atswitchStaticMACVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atswitchStaticMACVlan.setStatus("mandatory")
_AtswitchPortMacAddrGroup_ObjectIdentity = ObjectIdentity
atswitchPortMacAddrGroup = _AtswitchPortMacAddrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 12)
)
_AtswitchPortMACTable_Object = MibTable
atswitchPortMACTable = _AtswitchPortMACTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 12, 1)
)
if mibBuilder.loadTexts:
    atswitchPortMACTable.setStatus("mandatory")
_AtswitchPortMACEntry_Object = MibTableRow
atswitchPortMACEntry = _AtswitchPortMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 12, 1, 1)
)
atswitchPortMACEntry.setIndexNames(
    (0, "ATSWTCH2-MIB", "atswitchPortMACAddress"),
    (0, "ATSWTCH2-MIB", "atswitchPortMACPort"),
)
if mibBuilder.loadTexts:
    atswitchPortMACEntry.setStatus("mandatory")
_AtswitchPortMACAddress_Type = MacAddress
_AtswitchPortMACAddress_Object = MibTableColumn
atswitchPortMACAddress = _AtswitchPortMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 12, 1, 1, 1),
    _AtswitchPortMACAddress_Type()
)
atswitchPortMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchPortMACAddress.setStatus("mandatory")
_AtswitchPortMACPort_Type = Integer32
_AtswitchPortMACPort_Object = MibTableColumn
atswitchPortMACPort = _AtswitchPortMACPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 12, 1, 1, 2),
    _AtswitchPortMACPort_Type()
)
atswitchPortMACPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchPortMACPort.setStatus("mandatory")
_AtswitchDebugMallocLogGroup_ObjectIdentity = ObjectIdentity
atswitchDebugMallocLogGroup = _AtswitchDebugMallocLogGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 13)
)
_AtswitchDebugMallocLogTable_Object = MibTable
atswitchDebugMallocLogTable = _AtswitchDebugMallocLogTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 13, 1)
)
if mibBuilder.loadTexts:
    atswitchDebugMallocLogTable.setStatus("deprecated")
_AtswitchMallocLogEntry_Object = MibTableRow
atswitchMallocLogEntry = _AtswitchMallocLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 13, 1, 1)
)
atswitchMallocLogEntry.setIndexNames(
    (0, "ATSWTCH2-MIB", "atswitchDebugMallocLogIndex"),
)
if mibBuilder.loadTexts:
    atswitchMallocLogEntry.setStatus("deprecated")
_AtswitchDebugMallocLogIndex_Type = Integer32
_AtswitchDebugMallocLogIndex_Object = MibTableColumn
atswitchDebugMallocLogIndex = _AtswitchDebugMallocLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 13, 1, 1, 1),
    _AtswitchDebugMallocLogIndex_Type()
)
atswitchDebugMallocLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchDebugMallocLogIndex.setStatus("deprecated")
_AtswitchDebugMallocLogCaller_Type = Integer32
_AtswitchDebugMallocLogCaller_Object = MibTableColumn
atswitchDebugMallocLogCaller = _AtswitchDebugMallocLogCaller_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 13, 1, 1, 2),
    _AtswitchDebugMallocLogCaller_Type()
)
atswitchDebugMallocLogCaller.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchDebugMallocLogCaller.setStatus("deprecated")
_AtswitchDebugMallocLogAddress_Type = Integer32
_AtswitchDebugMallocLogAddress_Object = MibTableColumn
atswitchDebugMallocLogAddress = _AtswitchDebugMallocLogAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 13, 1, 1, 3),
    _AtswitchDebugMallocLogAddress_Type()
)
atswitchDebugMallocLogAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchDebugMallocLogAddress.setStatus("deprecated")

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

intruderTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 0, 105)
)
if mibBuilder.loadTexts:
    intruderTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATSWTCH2-MIB",
    **{"MacAddress": MacAddress,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "alliedTelesyn": alliedTelesyn,
       "newRoot": newRoot,
       "topologyChange": topologyChange,
       "intruderTrap": intruderTrap,
       "atiProduct": atiProduct,
       "mibObject": mibObject,
       "atswitchMib": atswitchMib,
       "atswitchSysGroup": atswitchSysGroup,
       "atswitchProductType": atswitchProductType,
       "atswitchEthernetPortCount": atswitchEthernetPortCount,
       "atswitchReset": atswitchReset,
       "atswitchMDA1Type": atswitchMDA1Type,
       "atswitchMDA2Type": atswitchMDA2Type,
       "atswitchDeviceFlowControl": atswitchDeviceFlowControl,
       "atswitchSwGroup": atswitchSwGroup,
       "atswitchSwProduct": atswitchSwProduct,
       "atswitchSwVersion": atswitchSwVersion,
       "atswitchIpGroup": atswitchIpGroup,
       "atswitchCurrentIpAddress": atswitchCurrentIpAddress,
       "atswitchConfiguredIpAddress": atswitchConfiguredIpAddress,
       "atswitchConfiguredSubnetMask": atswitchConfiguredSubnetMask,
       "atswitchConfiguredRouter": atswitchConfiguredRouter,
       "atswitchIPAddressStatus": atswitchIPAddressStatus,
       "atswitchDNServer": atswitchDNServer,
       "atswitchDefaultDomainName": atswitchDefaultDomainName,
       "atswitchNMGroup": atswitchNMGroup,
       "atswitchNwMgrTable": atswitchNwMgrTable,
       "atswitchNwMgrEntry": atswitchNwMgrEntry,
       "atswitchNwMgrIndex": atswitchNwMgrIndex,
       "atswitchNwMgrIpAddr": atswitchNwMgrIpAddr,
       "atswitchConfigGroup": atswitchConfigGroup,
       "atswitchPortDisableOnSecurityViolation": atswitchPortDisableOnSecurityViolation,
       "atswitchMirroringSourcePort": atswitchMirroringSourcePort,
       "atswitchMirrorState": atswitchMirrorState,
       "atswitchMirroringDestinationPort": atswitchMirroringDestinationPort,
       "atswitchSecurityConfig": atswitchSecurityConfig,
       "atswitchSecurityAction": atswitchSecurityAction,
       "atswitchDebugAvailableBytes": atswitchDebugAvailableBytes,
       "atswitchTrunkConfig": atswitchTrunkConfig,
       "atswitchPortConfigGroup": atswitchPortConfigGroup,
       "atswitchPortTable": atswitchPortTable,
       "atswitchPortEntry": atswitchPortEntry,
       "atswitchPortNumber": atswitchPortNumber,
       "atswitchPortName": atswitchPortName,
       "atswitchPortAutosenseOrHalfDuplex": atswitchPortAutosenseOrHalfDuplex,
       "atswitchPortLinkState": atswitchPortLinkState,
       "atswitchPortDuplexStatus": atswitchPortDuplexStatus,
       "atswitchPortSpeed": atswitchPortSpeed,
       "atswitchPortState": atswitchPortState,
       "atswitchPortTransmitPacingConfig": atswitchPortTransmitPacingConfig,
       "atswitchPortSTPConfig": atswitchPortSTPConfig,
       "atswitchPortBridgeid": atswitchPortBridgeid,
       "atswitchPortSTPCost": atswitchPortSTPCost,
       "atswitchPortSTPPriority": atswitchPortSTPPriority,
       "atswitchPortSwitchingType": atswitchPortSwitchingType,
       "atswitchPortFlowControlEnable": atswitchPortFlowControlEnable,
       "atswitchPortSecurityNumberOfAddresses": atswitchPortSecurityNumberOfAddresses,
       "atswitchVlanConfigGroup": atswitchVlanConfigGroup,
       "atswitchBasicVlanTable": atswitchBasicVlanTable,
       "atswitchBasicVlanEntry": atswitchBasicVlanEntry,
       "atswitchBeVlanIndex": atswitchBeVlanIndex,
       "atswitchBeVlanName": atswitchBeVlanName,
       "atswitchBeVlanTagId": atswitchBeVlanTagId,
       "atswitchBeVlanPortMask": atswitchBeVlanPortMask,
       "atswitchBeVlanRowStatus": atswitchBeVlanRowStatus,
       "atswitchPort2VlanTable": atswitchPort2VlanTable,
       "atswitchPort2VlanEntry": atswitchPort2VlanEntry,
       "atswitchPvPortNumber": atswitchPvPortNumber,
       "atswitchPvVlanName": atswitchPvVlanName,
       "atswitchEthernetStatsGroup": atswitchEthernetStatsGroup,
       "atswitchEthMonStats": atswitchEthMonStats,
       "atswitchEthMonRxGoodFrames": atswitchEthMonRxGoodFrames,
       "atswitchEthMonTxGoodFrames": atswitchEthMonTxGoodFrames,
       "atswitchEthMonTxTotalBytes": atswitchEthMonTxTotalBytes,
       "atswitchEthMonTxDeferred": atswitchEthMonTxDeferred,
       "atswitchEthMonTxCollisions": atswitchEthMonTxCollisions,
       "atswitchEthErrorStats": atswitchEthErrorStats,
       "atswitchEthErrorCRC": atswitchEthErrorCRC,
       "atswitchEthErrorAlignment": atswitchEthErrorAlignment,
       "atswitchEthErrorRxBadFrames": atswitchEthErrorRxBadFrames,
       "atswitchEthErrorLateCollisions": atswitchEthErrorLateCollisions,
       "atswitchEthErrorTxTotal": atswitchEthErrorTxTotal,
       "atswitchEthPortStatsGroup": atswitchEthPortStatsGroup,
       "atswitchEthPortMonStats": atswitchEthPortMonStats,
       "atswitchEthPortMonTable": atswitchEthPortMonTable,
       "atswitchEthPortMonEntry": atswitchEthPortMonEntry,
       "atswitchEthPortMonId": atswitchEthPortMonId,
       "atswitchEthPortMonTxTotalBytes": atswitchEthPortMonTxTotalBytes,
       "atswitchRxGoodFrames": atswitchRxGoodFrames,
       "atswitchTxGoodFrames": atswitchTxGoodFrames,
       "atswitchTxBroadcastFrames": atswitchTxBroadcastFrames,
       "atswitchTxMulticastFrames": atswitchTxMulticastFrames,
       "atswitchAddrDuplicate": atswitchAddrDuplicate,
       "atswitchAddrMismatches": atswitchAddrMismatches,
       "atswitchRxOverruns": atswitchRxOverruns,
       "atswitchEthPortError": atswitchEthPortError,
       "atswitchEthPortErrorTable": atswitchEthPortErrorTable,
       "atswitchEthPortErrorEntry": atswitchEthPortErrorEntry,
       "atswitchEthPortErrorId": atswitchEthPortErrorId,
       "atswitchEthPortErrorRxBadFrames": atswitchEthPortErrorRxBadFrames,
       "atswitchEthPortErrorTxTotal": atswitchEthPortErrorTxTotal,
       "atswitchFwdVlanGroup": atswitchFwdVlanGroup,
       "atswitchFwdVlanTable": atswitchFwdVlanTable,
       "atswitchFwdVlanEntry": atswitchFwdVlanEntry,
       "atswitchFwdVlanMACAddr": atswitchFwdVlanMACAddr,
       "atswitchFwdVlanVlanId": atswitchFwdVlanVlanId,
       "atswitchFwdVlanAge": atswitchFwdVlanAge,
       "atswitchFwdVlanStatus": atswitchFwdVlanStatus,
       "atswitchFwdVlanPort": atswitchFwdVlanPort,
       "atswitchTrapAttrGroup": atswitchTrapAttrGroup,
       "atswitchDuplicateMacAddress": atswitchDuplicateMacAddress,
       "atswitchIntruderMacAddress": atswitchIntruderMacAddress,
       "atswitchSecuredPortNumber": atswitchSecuredPortNumber,
       "atswitchBridgeMib": atswitchBridgeMib,
       "atswitchBrBase": atswitchBrBase,
       "atswitchBrBaseTable": atswitchBrBaseTable,
       "atswitchBrBaseEntry": atswitchBrBaseEntry,
       "atswitchBrBaseLanId": atswitchBrBaseLanId,
       "atswitchBrBaseBridgeAddress": atswitchBrBaseBridgeAddress,
       "atswitchBrBaseNumPorts": atswitchBrBaseNumPorts,
       "atswitchBrBaseType": atswitchBrBaseType,
       "atswitchBrBasePortTable": atswitchBrBasePortTable,
       "atswitchBrBasePortEntry": atswitchBrBasePortEntry,
       "atswitchBrBasePortLanId": atswitchBrBasePortLanId,
       "atswitchBrBasePort": atswitchBrBasePort,
       "atswitchBrBasePortIfIndex": atswitchBrBasePortIfIndex,
       "atswitchBrBasePortCircuit": atswitchBrBasePortCircuit,
       "atswitchBrBasePortDelayExceededDiscards": atswitchBrBasePortDelayExceededDiscards,
       "atswitchBrBasePortMtuExceededDiscards": atswitchBrBasePortMtuExceededDiscards,
       "atswitchBrStp": atswitchBrStp,
       "atswitchBrStpTable": atswitchBrStpTable,
       "atswitchBrStpEntry": atswitchBrStpEntry,
       "atswitchBrStpLanId": atswitchBrStpLanId,
       "atswitchBrStpProtocolSpecification": atswitchBrStpProtocolSpecification,
       "atswitchBrStpPriority": atswitchBrStpPriority,
       "atswitchBrStpTimeSinceTopologyChange": atswitchBrStpTimeSinceTopologyChange,
       "atswitchBrStpTopChanges": atswitchBrStpTopChanges,
       "atswitchBrStpDesignatedRoot": atswitchBrStpDesignatedRoot,
       "atswitchBrStpRootCost": atswitchBrStpRootCost,
       "atswitchBrStpRootPort": atswitchBrStpRootPort,
       "atswitchBrStpMaxAge": atswitchBrStpMaxAge,
       "atswitchBrStpHelloTime": atswitchBrStpHelloTime,
       "atswitchBrStpHoldTime": atswitchBrStpHoldTime,
       "atswitchBrStpForwardDelay": atswitchBrStpForwardDelay,
       "atswitchBrStpBridgeMaxAge": atswitchBrStpBridgeMaxAge,
       "atswitchBrStpBridgeHelloTime": atswitchBrStpBridgeHelloTime,
       "atswitchBrStpBridgeForwardDelay": atswitchBrStpBridgeForwardDelay,
       "atswitchBrStpPortTable": atswitchBrStpPortTable,
       "atswitchBrStpPortEntry": atswitchBrStpPortEntry,
       "atswitchBrStpPortLanId": atswitchBrStpPortLanId,
       "atswitchBrStpPort": atswitchBrStpPort,
       "atswitchBrStpPortPriority": atswitchBrStpPortPriority,
       "atswitchBrStpPortState": atswitchBrStpPortState,
       "atswitchBrStpPortEnable": atswitchBrStpPortEnable,
       "atswitchBrStpPortPathCost": atswitchBrStpPortPathCost,
       "atswitchBrStpPortDesignatedRoot": atswitchBrStpPortDesignatedRoot,
       "atswitchBrStpPortDesignatedCost": atswitchBrStpPortDesignatedCost,
       "atswitchBrStpPortDesignatedBridge": atswitchBrStpPortDesignatedBridge,
       "atswitchBrStpPortDesignatedPort": atswitchBrStpPortDesignatedPort,
       "atswitchBrStpPortForwardTransitions": atswitchBrStpPortForwardTransitions,
       "atswitchBrTp": atswitchBrTp,
       "atswitchBrTpTable": atswitchBrTpTable,
       "atswitchBrTpEntry": atswitchBrTpEntry,
       "atswitchBrTpLanId": atswitchBrTpLanId,
       "atswitchBrTpLearnedEntryDiscards": atswitchBrTpLearnedEntryDiscards,
       "atswitchBrTpAgingTime": atswitchBrTpAgingTime,
       "atswitchBrTpFdbTable": atswitchBrTpFdbTable,
       "atswitchBrTpFdbEntry": atswitchBrTpFdbEntry,
       "atswitchBrTpFdbLanId": atswitchBrTpFdbLanId,
       "atswitchBrTpFdbAddress": atswitchBrTpFdbAddress,
       "atswitchBrTpFdbPort": atswitchBrTpFdbPort,
       "atswitchBrTpFdbStatus": atswitchBrTpFdbStatus,
       "atswitchBrTpPortTable": atswitchBrTpPortTable,
       "atswitchBrTpPortEntry": atswitchBrTpPortEntry,
       "atswitchBrTpPortLanId": atswitchBrTpPortLanId,
       "atswitchBrTpPort": atswitchBrTpPort,
       "atswitchBrTpPortMaxInfo": atswitchBrTpPortMaxInfo,
       "atswitchBrTpPortInFrames": atswitchBrTpPortInFrames,
       "atswitchBrTpPortOutFrames": atswitchBrTpPortOutFrames,
       "atswitchBrTpPortInDiscards": atswitchBrTpPortInDiscards,
       "atswitchStaticMACGroup": atswitchStaticMACGroup,
       "atswitchStaticMACTable": atswitchStaticMACTable,
       "atswitchStaticMACEntry": atswitchStaticMACEntry,
       "atswitchStaticMACAddress": atswitchStaticMACAddress,
       "atswitchStaticMACPortNumbers": atswitchStaticMACPortNumbers,
       "atswitchStaticMACVlan": atswitchStaticMACVlan,
       "atswitchPortMacAddrGroup": atswitchPortMacAddrGroup,
       "atswitchPortMACTable": atswitchPortMACTable,
       "atswitchPortMACEntry": atswitchPortMACEntry,
       "atswitchPortMACAddress": atswitchPortMACAddress,
       "atswitchPortMACPort": atswitchPortMACPort,
       "atswitchDebugMallocLogGroup": atswitchDebugMallocLogGroup,
       "atswitchDebugMallocLogTable": atswitchDebugMallocLogTable,
       "atswitchMallocLogEntry": atswitchMallocLogEntry,
       "atswitchDebugMallocLogIndex": atswitchDebugMallocLogIndex,
       "atswitchDebugMallocLogCaller": atswitchDebugMallocLogCaller,
       "atswitchDebugMallocLogAddress": atswitchDebugMallocLogAddress}
)
