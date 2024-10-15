# SNMP MIB module (WWP-EXT-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-EXT-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:39 2024
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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpExtBridgeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4)
)
wwpExtBridgeMIB.setRevisions(
        ("2005-11-23 09:00",
         "2001-04-03 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class VlanId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_WwpExtBridgeMIBObjects_ObjectIdentity = ObjectIdentity
wwpExtBridgeMIBObjects = _WwpExtBridgeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1)
)
_WwpPort_ObjectIdentity = ObjectIdentity
wwpPort = _WwpPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 1)
)
_WwpPortTable_Object = MibTable
wwpPortTable = _WwpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wwpPortTable.setStatus("current")
_WwpPortEntry_Object = MibTableRow
wwpPortEntry = _WwpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 1, 1, 1)
)
wwpPortEntry.setIndexNames(
    (0, "WWP-EXT-BRIDGE-MIB", "wwpPortId"),
)
if mibBuilder.loadTexts:
    wwpPortEntry.setStatus("current")


class _WwpPortId_Type(Integer32):
    """Custom type wwpPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpPortId_Type.__name__ = "Integer32"
_WwpPortId_Object = MibTableColumn
wwpPortId = _WwpPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 1, 1, 1, 1),
    _WwpPortId_Type()
)
wwpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPortId.setStatus("current")


class _WwpPortType_Type(Integer32):
    """Custom type wwpPortType based on Integer32"""
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
        *(("fastEth", 2),
          ("hundredFx", 5),
          ("lx", 1),
          ("sx", 4),
          ("unknown", 6),
          ("voip", 3))
    )


_WwpPortType_Type.__name__ = "Integer32"
_WwpPortType_Object = MibTableColumn
wwpPortType = _WwpPortType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 1, 1, 1, 2),
    _WwpPortType_Type()
)
wwpPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPortType.setStatus("current")


class _WwpPortName_Type(DisplayString):
    """Custom type wwpPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WwpPortName_Type.__name__ = "DisplayString"
_WwpPortName_Object = MibTableColumn
wwpPortName = _WwpPortName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 1, 1, 1, 3),
    _WwpPortName_Type()
)
wwpPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpPortName.setStatus("current")
_WwpPortPhysAddr_Type = MacAddress
_WwpPortPhysAddr_Object = MibTableColumn
wwpPortPhysAddr = _WwpPortPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 1, 1, 1, 4),
    _WwpPortPhysAddr_Type()
)
wwpPortPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPortPhysAddr.setStatus("current")
_WwpPortAutoNeg_Type = TruthValue
_WwpPortAutoNeg_Object = MibTableColumn
wwpPortAutoNeg = _WwpPortAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 1, 1, 1, 5),
    _WwpPortAutoNeg_Type()
)
wwpPortAutoNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpPortAutoNeg.setStatus("current")


class _WwpPortAdminStatus_Type(Integer32):
    """Custom type wwpPortAdminStatus based on Integer32"""
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


_WwpPortAdminStatus_Type.__name__ = "Integer32"
_WwpPortAdminStatus_Object = MibTableColumn
wwpPortAdminStatus = _WwpPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 1, 1, 1, 6),
    _WwpPortAdminStatus_Type()
)
wwpPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpPortAdminStatus.setStatus("current")


class _WwpPortOperStatus_Type(Integer32):
    """Custom type wwpPortOperStatus based on Integer32"""
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


_WwpPortOperStatus_Type.__name__ = "Integer32"
_WwpPortOperStatus_Object = MibTableColumn
wwpPortOperStatus = _WwpPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 1, 1, 1, 7),
    _WwpPortOperStatus_Type()
)
wwpPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPortOperStatus.setStatus("current")


class _WwpPortAdminSpeed_Type(Integer32):
    """Custom type wwpPortAdminSpeed based on Integer32"""
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
        *(("auto", 4),
          ("gig", 3),
          ("hundredMb", 2),
          ("tenMb", 1))
    )


_WwpPortAdminSpeed_Type.__name__ = "Integer32"
_WwpPortAdminSpeed_Object = MibTableColumn
wwpPortAdminSpeed = _WwpPortAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 1, 1, 1, 8),
    _WwpPortAdminSpeed_Type()
)
wwpPortAdminSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpPortAdminSpeed.setStatus("current")
_WwpPortOperSpeed_Type = Integer32
_WwpPortOperSpeed_Object = MibTableColumn
wwpPortOperSpeed = _WwpPortOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 1, 1, 1, 9),
    _WwpPortOperSpeed_Type()
)
wwpPortOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPortOperSpeed.setStatus("current")


class _WwpPortAdminDuplex_Type(Integer32):
    """Custom type wwpPortAdminDuplex based on Integer32"""
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


_WwpPortAdminDuplex_Type.__name__ = "Integer32"
_WwpPortAdminDuplex_Object = MibTableColumn
wwpPortAdminDuplex = _WwpPortAdminDuplex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 1, 1, 1, 10),
    _WwpPortAdminDuplex_Type()
)
wwpPortAdminDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpPortAdminDuplex.setStatus("current")


class _WwpPortOperDuplex_Type(Integer32):
    """Custom type wwpPortOperDuplex based on Integer32"""
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


_WwpPortOperDuplex_Type.__name__ = "Integer32"
_WwpPortOperDuplex_Object = MibTableColumn
wwpPortOperDuplex = _WwpPortOperDuplex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 1, 1, 1, 11),
    _WwpPortOperDuplex_Type()
)
wwpPortOperDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPortOperDuplex.setStatus("current")


class _WwpPortAdminFlowCtrl_Type(Integer32):
    """Custom type wwpPortAdminFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_WwpPortAdminFlowCtrl_Type.__name__ = "Integer32"
_WwpPortAdminFlowCtrl_Object = MibTableColumn
wwpPortAdminFlowCtrl = _WwpPortAdminFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 1, 1, 1, 12),
    _WwpPortAdminFlowCtrl_Type()
)
wwpPortAdminFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpPortAdminFlowCtrl.setStatus("current")


class _WwpPortOperFlowCtrl_Type(Integer32):
    """Custom type wwpPortOperFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WwpPortOperFlowCtrl_Type.__name__ = "Integer32"
_WwpPortOperFlowCtrl_Object = MibTableColumn
wwpPortOperFlowCtrl = _WwpPortOperFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 1, 1, 1, 13),
    _WwpPortOperFlowCtrl_Type()
)
wwpPortOperFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPortOperFlowCtrl.setStatus("current")


class _WwpPortTagged_Type(Integer32):
    """Custom type wwpPortTagged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 1),
          ("untagged", 0))
    )


_WwpPortTagged_Type.__name__ = "Integer32"
_WwpPortTagged_Object = MibTableColumn
wwpPortTagged = _WwpPortTagged_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 1, 1, 1, 14),
    _WwpPortTagged_Type()
)
wwpPortTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpPortTagged.setStatus("current")


class _WwpPortUntaggedPriority_Type(Integer32):
    """Custom type wwpPortUntaggedPriority based on Integer32"""
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
        *(("p0", 0),
          ("p1", 1),
          ("p2", 2),
          ("p3", 3),
          ("p4", 4),
          ("p5", 5),
          ("p6", 6),
          ("p7", 7))
    )


_WwpPortUntaggedPriority_Type.__name__ = "Integer32"
_WwpPortUntaggedPriority_Object = MibTableColumn
wwpPortUntaggedPriority = _WwpPortUntaggedPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 1, 1, 1, 15),
    _WwpPortUntaggedPriority_Type()
)
wwpPortUntaggedPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpPortUntaggedPriority.setStatus("current")


class _WwpPortMaxFrameSize_Type(Integer32):
    """Custom type wwpPortMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1522, 9126),
    )


_WwpPortMaxFrameSize_Type.__name__ = "Integer32"
_WwpPortMaxFrameSize_Object = MibTableColumn
wwpPortMaxFrameSize = _WwpPortMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 1, 1, 1, 16),
    _WwpPortMaxFrameSize_Type()
)
wwpPortMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpPortMaxFrameSize.setStatus("current")


class _WwpPortIngressFiltering_Type(Integer32):
    """Custom type wwpPortIngressFiltering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_WwpPortIngressFiltering_Type.__name__ = "Integer32"
_WwpPortIngressFiltering_Object = MibTableColumn
wwpPortIngressFiltering = _WwpPortIngressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 1, 1, 1, 17),
    _WwpPortIngressFiltering_Type()
)
wwpPortIngressFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpPortIngressFiltering.setStatus("current")


class _WwpPortRateLimitState_Type(TruthValue):
    """Custom type wwpPortRateLimitState based on TruthValue"""


_WwpPortRateLimitState_Object = MibTableColumn
wwpPortRateLimitState = _WwpPortRateLimitState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 1, 1, 1, 18),
    _WwpPortRateLimitState_Type()
)
wwpPortRateLimitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpPortRateLimitState.setStatus("current")


class _WwpPortRateLimitValue_Type(Integer32):
    """Custom type wwpPortRateLimitValue based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpPortRateLimitValue_Type.__name__ = "Integer32"
_WwpPortRateLimitValue_Object = MibTableColumn
wwpPortRateLimitValue = _WwpPortRateLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 1, 1, 1, 19),
    _WwpPortRateLimitValue_Type()
)
wwpPortRateLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpPortRateLimitValue.setStatus("current")
if mibBuilder.loadTexts:
    wwpPortRateLimitValue.setUnits("Bits per second")


class _WwpLocalMgmtPortEnable_Type(TruthValue):
    """Custom type wwpLocalMgmtPortEnable based on TruthValue"""


_WwpLocalMgmtPortEnable_Object = MibScalar
wwpLocalMgmtPortEnable = _WwpLocalMgmtPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 1, 2),
    _WwpLocalMgmtPortEnable_Type()
)
wwpLocalMgmtPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLocalMgmtPortEnable.setStatus("deprecated")
_WwpVlan_ObjectIdentity = ObjectIdentity
wwpVlan = _WwpVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 2)
)


class _WwpVlanVersionNumber_Type(Integer32):
    """Custom type wwpVlanVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("version1", 1)
    )


_WwpVlanVersionNumber_Type.__name__ = "Integer32"
_WwpVlanVersionNumber_Object = MibScalar
wwpVlanVersionNumber = _WwpVlanVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 2, 1),
    _WwpVlanVersionNumber_Type()
)
wwpVlanVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpVlanVersionNumber.setStatus("current")
_WwpMaxVlanId_Type = VlanId
_WwpMaxVlanId_Object = MibScalar
wwpMaxVlanId = _WwpMaxVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 2, 2),
    _WwpMaxVlanId_Type()
)
wwpMaxVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpMaxVlanId.setStatus("current")
_WwpMaxSupportedVlans_Type = Unsigned32
_WwpMaxSupportedVlans_Object = MibScalar
wwpMaxSupportedVlans = _WwpMaxSupportedVlans_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 2, 3),
    _WwpMaxSupportedVlans_Type()
)
wwpMaxSupportedVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpMaxSupportedVlans.setStatus("current")
_WwpNumVlans_Type = Unsigned32
_WwpNumVlans_Object = MibScalar
wwpNumVlans = _WwpNumVlans_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 2, 4),
    _WwpNumVlans_Type()
)
wwpNumVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpNumVlans.setStatus("current")
_WwpVlanTable_Object = MibTable
wwpVlanTable = _WwpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 2, 5)
)
if mibBuilder.loadTexts:
    wwpVlanTable.setStatus("current")
_WwpVlanEntry_Object = MibTableRow
wwpVlanEntry = _WwpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 2, 5, 1)
)
wwpVlanEntry.setIndexNames(
    (0, "WWP-EXT-BRIDGE-MIB", "wwpVlanId"),
)
if mibBuilder.loadTexts:
    wwpVlanEntry.setStatus("current")
_WwpVlanId_Type = VlanId
_WwpVlanId_Object = MibTableColumn
wwpVlanId = _WwpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 2, 5, 1, 1),
    _WwpVlanId_Type()
)
wwpVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpVlanId.setStatus("current")


class _WwpVlanName_Type(DisplayString):
    """Custom type wwpVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WwpVlanName_Type.__name__ = "DisplayString"
_WwpVlanName_Object = MibTableColumn
wwpVlanName = _WwpVlanName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 2, 5, 1, 2),
    _WwpVlanName_Type()
)
wwpVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpVlanName.setStatus("current")


class _WwpVlanCurrentEgressPorts_Type(PortList):
    """Custom type wwpVlanCurrentEgressPorts based on PortList"""
    defaultHexValue = "0000"


_WwpVlanCurrentEgressPorts_Object = MibTableColumn
wwpVlanCurrentEgressPorts = _WwpVlanCurrentEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 2, 5, 1, 3),
    _WwpVlanCurrentEgressPorts_Type()
)
wwpVlanCurrentEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVlanCurrentEgressPorts.setStatus("current")
_WwpVlanCurrentUntaggedPorts_Type = PortList
_WwpVlanCurrentUntaggedPorts_Object = MibTableColumn
wwpVlanCurrentUntaggedPorts = _WwpVlanCurrentUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 2, 5, 1, 4),
    _WwpVlanCurrentUntaggedPorts_Type()
)
wwpVlanCurrentUntaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpVlanCurrentUntaggedPorts.setStatus("current")


class _WwpVlanMgmtStatus_Type(Integer32):
    """Custom type wwpVlanMgmtStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localMgmtVlan", 2),
          ("notMgmtVlan", 0),
          ("remoteMgmtVlan", 1))
    )


_WwpVlanMgmtStatus_Type.__name__ = "Integer32"
_WwpVlanMgmtStatus_Object = MibTableColumn
wwpVlanMgmtStatus = _WwpVlanMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 2, 5, 1, 5),
    _WwpVlanMgmtStatus_Type()
)
wwpVlanMgmtStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVlanMgmtStatus.setStatus("current")
_WwpVlanRowStatus_Type = RowStatus
_WwpVlanRowStatus_Object = MibTableColumn
wwpVlanRowStatus = _WwpVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 2, 5, 1, 6),
    _WwpVlanRowStatus_Type()
)
wwpVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVlanRowStatus.setStatus("current")
_WwpVlanXTable_Object = MibTable
wwpVlanXTable = _WwpVlanXTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 2, 6)
)
if mibBuilder.loadTexts:
    wwpVlanXTable.setStatus("current")
_WwpVlanXEntry_Object = MibTableRow
wwpVlanXEntry = _WwpVlanXEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    wwpVlanXEntry.setStatus("current")


class _WwpVlanTunnel_Type(Integer32):
    """Custom type wwpVlanTunnel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_WwpVlanTunnel_Type.__name__ = "Integer32"
_WwpVlanTunnel_Object = MibTableColumn
wwpVlanTunnel = _WwpVlanTunnel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 1, 2, 6, 1, 1),
    _WwpVlanTunnel_Type()
)
wwpVlanTunnel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVlanTunnel.setStatus("current")
_WwpExtBridgeMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpExtBridgeMIBNotificationPrefix = _WwpExtBridgeMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 2)
)
_WwpExtBridgeMIBNotifications_ObjectIdentity = ObjectIdentity
wwpExtBridgeMIBNotifications = _WwpExtBridgeMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 2, 0)
)
_WwpExtBridgeMIBConformance_ObjectIdentity = ObjectIdentity
wwpExtBridgeMIBConformance = _WwpExtBridgeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 3)
)
_WwpExtBridgeMIBCompliances_ObjectIdentity = ObjectIdentity
wwpExtBridgeMIBCompliances = _WwpExtBridgeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 3, 1)
)
_WwpExtBridgeMIBGroups_ObjectIdentity = ObjectIdentity
wwpExtBridgeMIBGroups = _WwpExtBridgeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 4, 3, 2)
)
wwpVlanEntry.registerAugmentions(
    ("WWP-EXT-BRIDGE-MIB",
     "wwpVlanXEntry")
)
wwpVlanXEntry.setIndexNames(*wwpVlanEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-EXT-BRIDGE-MIB",
    **{"PortList": PortList,
       "VlanId": VlanId,
       "wwpExtBridgeMIB": wwpExtBridgeMIB,
       "wwpExtBridgeMIBObjects": wwpExtBridgeMIBObjects,
       "wwpPort": wwpPort,
       "wwpPortTable": wwpPortTable,
       "wwpPortEntry": wwpPortEntry,
       "wwpPortId": wwpPortId,
       "wwpPortType": wwpPortType,
       "wwpPortName": wwpPortName,
       "wwpPortPhysAddr": wwpPortPhysAddr,
       "wwpPortAutoNeg": wwpPortAutoNeg,
       "wwpPortAdminStatus": wwpPortAdminStatus,
       "wwpPortOperStatus": wwpPortOperStatus,
       "wwpPortAdminSpeed": wwpPortAdminSpeed,
       "wwpPortOperSpeed": wwpPortOperSpeed,
       "wwpPortAdminDuplex": wwpPortAdminDuplex,
       "wwpPortOperDuplex": wwpPortOperDuplex,
       "wwpPortAdminFlowCtrl": wwpPortAdminFlowCtrl,
       "wwpPortOperFlowCtrl": wwpPortOperFlowCtrl,
       "wwpPortTagged": wwpPortTagged,
       "wwpPortUntaggedPriority": wwpPortUntaggedPriority,
       "wwpPortMaxFrameSize": wwpPortMaxFrameSize,
       "wwpPortIngressFiltering": wwpPortIngressFiltering,
       "wwpPortRateLimitState": wwpPortRateLimitState,
       "wwpPortRateLimitValue": wwpPortRateLimitValue,
       "wwpLocalMgmtPortEnable": wwpLocalMgmtPortEnable,
       "wwpVlan": wwpVlan,
       "wwpVlanVersionNumber": wwpVlanVersionNumber,
       "wwpMaxVlanId": wwpMaxVlanId,
       "wwpMaxSupportedVlans": wwpMaxSupportedVlans,
       "wwpNumVlans": wwpNumVlans,
       "wwpVlanTable": wwpVlanTable,
       "wwpVlanEntry": wwpVlanEntry,
       "wwpVlanId": wwpVlanId,
       "wwpVlanName": wwpVlanName,
       "wwpVlanCurrentEgressPorts": wwpVlanCurrentEgressPorts,
       "wwpVlanCurrentUntaggedPorts": wwpVlanCurrentUntaggedPorts,
       "wwpVlanMgmtStatus": wwpVlanMgmtStatus,
       "wwpVlanRowStatus": wwpVlanRowStatus,
       "wwpVlanXTable": wwpVlanXTable,
       "wwpVlanXEntry": wwpVlanXEntry,
       "wwpVlanTunnel": wwpVlanTunnel,
       "wwpExtBridgeMIBNotificationPrefix": wwpExtBridgeMIBNotificationPrefix,
       "wwpExtBridgeMIBNotifications": wwpExtBridgeMIBNotifications,
       "wwpExtBridgeMIBConformance": wwpExtBridgeMIBConformance,
       "wwpExtBridgeMIBCompliances": wwpExtBridgeMIBCompliances,
       "wwpExtBridgeMIBGroups": wwpExtBridgeMIBGroups}
)
