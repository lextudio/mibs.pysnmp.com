# SNMP MIB module (XYPLEX-IEEE-HUB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYPLEX-IEEE-HUB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:49 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Xyplex_ObjectIdentity = ObjectIdentity
xyplex = _Xyplex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33)
)
_IeeeHub_ObjectIdentity = ObjectIdentity
ieeeHub = _IeeeHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10001)
)
_HmBasicCapability_ObjectIdentity = ObjectIdentity
hmBasicCapability = _HmBasicCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10001, 1)
)
_HmBasicHubTable_ObjectIdentity = ObjectIdentity
hmBasicHubTable = _HmBasicHubTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10001, 1, 1)
)
_HmBasicHubEntry_ObjectIdentity = ObjectIdentity
hmBasicHubEntry = _HmBasicHubEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10001, 1, 1, 1)
)


class _HubID_Type(OctetString):
    """Custom type hubID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HubID_Type.__name__ = "OctetString"
_HubID_Object = MibScalar
hubID = _HubID_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 1, 1, 1, 1),
    _HubID_Type()
)
hubID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubID.setStatus("mandatory")


class _HubGroupCapacity_Type(Integer32):
    """Custom type hubGroupCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HubGroupCapacity_Type.__name__ = "Integer32"
_HubGroupCapacity_Object = MibScalar
hubGroupCapacity = _HubGroupCapacity_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 1, 1, 1, 2),
    _HubGroupCapacity_Type()
)
hubGroupCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubGroupCapacity.setStatus("mandatory")


class _HubGroupMap_Type(OctetString):
    """Custom type hubGroupMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HubGroupMap_Type.__name__ = "OctetString"
_HubGroupMap_Object = MibScalar
hubGroupMap = _HubGroupMap_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 1, 1, 1, 3),
    _HubGroupMap_Type()
)
hubGroupMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubGroupMap.setStatus("mandatory")
_HmBasicGroupTable_ObjectIdentity = ObjectIdentity
hmBasicGroupTable = _HmBasicGroupTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10001, 1, 2)
)
_HmBasicGroupEntry_ObjectIdentity = ObjectIdentity
hmBasicGroupEntry = _HmBasicGroupEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10001, 1, 2, 1)
)


class _GroupHubID_Type(OctetString):
    """Custom type groupHubID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_GroupHubID_Type.__name__ = "OctetString"
_GroupHubID_Object = MibScalar
groupHubID = _GroupHubID_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 1, 2, 1, 1),
    _GroupHubID_Type()
)
groupHubID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupHubID.setStatus("mandatory")


class _GroupID_Type(Integer32):
    """Custom type groupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GroupID_Type.__name__ = "Integer32"
_GroupID_Object = MibScalar
groupID = _GroupID_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 1, 2, 1, 2),
    _GroupID_Type()
)
groupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupID.setStatus("mandatory")


class _GroupNumberOfPorts_Type(Integer32):
    """Custom type groupNumberOfPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GroupNumberOfPorts_Type.__name__ = "Integer32"
_GroupNumberOfPorts_Object = MibScalar
groupNumberOfPorts = _GroupNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 1, 2, 1, 3),
    _GroupNumberOfPorts_Type()
)
groupNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupNumberOfPorts.setStatus("mandatory")
_HmBasicPortTable_Object = MibTable
hmBasicPortTable = _HmBasicPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 1, 3)
)
if mibBuilder.loadTexts:
    hmBasicPortTable.setStatus("mandatory")
_HmBasicPortEntry_Object = MibTableRow
hmBasicPortEntry = _HmBasicPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 1, 3, 1)
)
hmBasicPortEntry.setIndexNames(
    (0, "XYPLEX-IEEE-HUB-MIB", "portHubBasicID"),
)
if mibBuilder.loadTexts:
    hmBasicPortEntry.setStatus("mandatory")


class _PortHubBasicID_Type(OctetString):
    """Custom type portHubBasicID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PortHubBasicID_Type.__name__ = "OctetString"
_PortHubBasicID_Object = MibTableColumn
portHubBasicID = _PortHubBasicID_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 1, 3, 1, 1),
    _PortHubBasicID_Type()
)
portHubBasicID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHubBasicID.setStatus("mandatory")


class _PortGroupBasicID_Type(Integer32):
    """Custom type portGroupBasicID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortGroupBasicID_Type.__name__ = "Integer32"
_PortGroupBasicID_Object = MibTableColumn
portGroupBasicID = _PortGroupBasicID_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 1, 3, 1, 2),
    _PortGroupBasicID_Type()
)
portGroupBasicID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portGroupBasicID.setStatus("mandatory")


class _PortBasicID_Type(Integer32):
    """Custom type portBasicID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortBasicID_Type.__name__ = "Integer32"
_PortBasicID_Object = MibTableColumn
portBasicID = _PortBasicID_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 1, 3, 1, 3),
    _PortBasicID_Type()
)
portBasicID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBasicID.setStatus("mandatory")


class _PortType_Type(Integer32):
    """Custom type portType based on Integer32"""
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
        *(("other", 1),
          ("repeater", 2),
          ("tenBASE-FAsync", 3),
          ("tenBASE-FSynch", 4))
    )


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 1, 3, 1, 4),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("mandatory")


class _PortAdminState_Type(Integer32):
    """Custom type portAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_PortAdminState_Type.__name__ = "Integer32"
_PortAdminState_Object = MibTableColumn
portAdminState = _PortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 1, 3, 1, 5),
    _PortAdminState_Type()
)
portAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAdminState.setStatus("mandatory")


class _PortAutoPartitionState_Type(Integer32):
    """Custom type portAutoPartitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoPartitioned", 3),
          ("notAutoPartitioned", 2),
          ("other", 1))
    )


_PortAutoPartitionState_Type.__name__ = "Integer32"
_PortAutoPartitionState_Object = MibTableColumn
portAutoPartitionState = _PortAutoPartitionState_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 1, 3, 1, 6),
    _PortAutoPartitionState_Type()
)
portAutoPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAutoPartitionState.setStatus("mandatory")
_HmSelfTestCapability_ObjectIdentity = ObjectIdentity
hmSelfTestCapability = _HmSelfTestCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10001, 2)
)
_HmSelfTestHubTable_ObjectIdentity = ObjectIdentity
hmSelfTestHubTable = _HmSelfTestHubTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10001, 2, 1)
)
_HmSelfTestHubEntry_ObjectIdentity = ObjectIdentity
hmSelfTestHubEntry = _HmSelfTestHubEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1)
)


class _HubSelfTestID_Type(OctetString):
    """Custom type hubSelfTestID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HubSelfTestID_Type.__name__ = "OctetString"
_HubSelfTestID_Object = MibScalar
hubSelfTestID = _HubSelfTestID_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1, 1),
    _HubSelfTestID_Type()
)
hubSelfTestID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubSelfTestID.setStatus("mandatory")
_HubResetTimeStamp_Type = TimeTicks
_HubResetTimeStamp_Object = MibScalar
hubResetTimeStamp = _HubResetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1, 2),
    _HubResetTimeStamp_Type()
)
hubResetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubResetTimeStamp.setStatus("mandatory")


class _HubHealthState_Type(Integer32):
    """Custom type hubHealthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("ok", 2),
          ("other", 1))
    )


_HubHealthState_Type.__name__ = "Integer32"
_HubHealthState_Object = MibScalar
hubHealthState = _HubHealthState_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1, 3),
    _HubHealthState_Type()
)
hubHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubHealthState.setStatus("mandatory")


class _HubHealthText_Type(DisplayString):
    """Custom type hubHealthText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HubHealthText_Type.__name__ = "DisplayString"
_HubHealthText_Object = MibScalar
hubHealthText = _HubHealthText_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1, 4),
    _HubHealthText_Type()
)
hubHealthText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubHealthText.setStatus("mandatory")


class _HubHealthData_Type(OctetString):
    """Custom type hubHealthData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HubHealthData_Type.__name__ = "OctetString"
_HubHealthData_Object = MibScalar
hubHealthData = _HubHealthData_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1, 5),
    _HubHealthData_Type()
)
hubHealthData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubHealthData.setStatus("mandatory")


class _HubSystemResetting_Type(Integer32):
    """Custom type hubSystemResetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notResetting", 1),
          ("resetting", 2))
    )


_HubSystemResetting_Type.__name__ = "Integer32"
_HubSystemResetting_Object = MibScalar
hubSystemResetting = _HubSystemResetting_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1, 6),
    _HubSystemResetting_Type()
)
hubSystemResetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubSystemResetting.setStatus("mandatory")


class _HubResetting_Type(Integer32):
    """Custom type hubResetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notResetting", 1),
          ("resetting", 2))
    )


_HubResetting_Type.__name__ = "Integer32"
_HubResetting_Object = MibScalar
hubResetting = _HubResetting_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1, 7),
    _HubResetting_Type()
)
hubResetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubResetting.setStatus("mandatory")


class _HubExecutingSelfTest_Type(Integer32):
    """Custom type hubExecutingSelfTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSelfTesting", 1),
          ("selfTesting", 2))
    )


_HubExecutingSelfTest_Type.__name__ = "Integer32"
_HubExecutingSelfTest_Object = MibScalar
hubExecutingSelfTest = _HubExecutingSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1, 8),
    _HubExecutingSelfTest_Type()
)
hubExecutingSelfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubExecutingSelfTest.setStatus("mandatory")
_HmPerfMonCapability_ObjectIdentity = ObjectIdentity
hmPerfMonCapability = _HmPerfMonCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10001, 3)
)
_HmPerfMonRelayTable_ObjectIdentity = ObjectIdentity
hmPerfMonRelayTable = _HmPerfMonRelayTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10001, 3, 1)
)
_HmPerfMonRelayEntry_ObjectIdentity = ObjectIdentity
hmPerfMonRelayEntry = _HmPerfMonRelayEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10001, 3, 1, 1)
)


class _RelayHubPerfID_Type(OctetString):
    """Custom type relayHubPerfID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_RelayHubPerfID_Type.__name__ = "OctetString"
_RelayHubPerfID_Object = MibScalar
relayHubPerfID = _RelayHubPerfID_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 3, 1, 1, 1),
    _RelayHubPerfID_Type()
)
relayHubPerfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayHubPerfID.setStatus("mandatory")


class _RelayPerfID_Type(Integer32):
    """Custom type relayPerfID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RelayPerfID_Type.__name__ = "Integer32"
_RelayPerfID_Object = MibScalar
relayPerfID = _RelayPerfID_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 3, 1, 1, 2),
    _RelayPerfID_Type()
)
relayPerfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayPerfID.setStatus("mandatory")
_RelayTotalCollisions_Type = Counter32
_RelayTotalCollisions_Object = MibScalar
relayTotalCollisions = _RelayTotalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 3, 1, 1, 3),
    _RelayTotalCollisions_Type()
)
relayTotalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayTotalCollisions.setStatus("mandatory")
_HmPerfMonPortTable_Object = MibTable
hmPerfMonPortTable = _HmPerfMonPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 3, 2)
)
if mibBuilder.loadTexts:
    hmPerfMonPortTable.setStatus("mandatory")
_HmPerfMonPortEntry_Object = MibTableRow
hmPerfMonPortEntry = _HmPerfMonPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hmPerfMonPortEntry.setStatus("mandatory")


class _PortHubPerfID_Type(OctetString):
    """Custom type portHubPerfID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PortHubPerfID_Type.__name__ = "OctetString"
_PortHubPerfID_Object = MibTableColumn
portHubPerfID = _PortHubPerfID_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 1),
    _PortHubPerfID_Type()
)
portHubPerfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHubPerfID.setStatus("mandatory")


class _PortGroupPerfID_Type(Integer32):
    """Custom type portGroupPerfID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortGroupPerfID_Type.__name__ = "Integer32"
_PortGroupPerfID_Object = MibTableColumn
portGroupPerfID = _PortGroupPerfID_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 2),
    _PortGroupPerfID_Type()
)
portGroupPerfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portGroupPerfID.setStatus("mandatory")


class _PortPerfID_Type(Integer32):
    """Custom type portPerfID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortPerfID_Type.__name__ = "Integer32"
_PortPerfID_Object = MibTableColumn
portPerfID = _PortPerfID_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 3),
    _PortPerfID_Type()
)
portPerfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPerfID.setStatus("mandatory")
_PortReadableFrames_Type = Counter32
_PortReadableFrames_Object = MibTableColumn
portReadableFrames = _PortReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 4),
    _PortReadableFrames_Type()
)
portReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portReadableFrames.setStatus("mandatory")
_PortReadableOctets_Type = Counter32
_PortReadableOctets_Object = MibTableColumn
portReadableOctets = _PortReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 5),
    _PortReadableOctets_Type()
)
portReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portReadableOctets.setStatus("mandatory")
_PortPygmys_Type = Counter32
_PortPygmys_Object = MibTableColumn
portPygmys = _PortPygmys_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 6),
    _PortPygmys_Type()
)
portPygmys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPygmys.setStatus("mandatory")
_PortRunts_Type = Counter32
_PortRunts_Object = MibTableColumn
portRunts = _PortRunts_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 7),
    _PortRunts_Type()
)
portRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRunts.setStatus("mandatory")
_PortFrameCheckSeqErrs_Type = Counter32
_PortFrameCheckSeqErrs_Object = MibTableColumn
portFrameCheckSeqErrs = _PortFrameCheckSeqErrs_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 8),
    _PortFrameCheckSeqErrs_Type()
)
portFrameCheckSeqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFrameCheckSeqErrs.setStatus("mandatory")
_PortAlignmentErrors_Type = Counter32
_PortAlignmentErrors_Object = MibTableColumn
portAlignmentErrors = _PortAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 9),
    _PortAlignmentErrors_Type()
)
portAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAlignmentErrors.setStatus("mandatory")
_PortFramesTooLong_Type = Counter32
_PortFramesTooLong_Object = MibTableColumn
portFramesTooLong = _PortFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 10),
    _PortFramesTooLong_Type()
)
portFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFramesTooLong.setStatus("mandatory")
_PortAutoPartitionCount_Type = Counter32
_PortAutoPartitionCount_Object = MibTableColumn
portAutoPartitionCount = _PortAutoPartitionCount_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 11),
    _PortAutoPartitionCount_Type()
)
portAutoPartitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAutoPartitionCount.setStatus("mandatory")
_HmAddrTrackCapability_ObjectIdentity = ObjectIdentity
hmAddrTrackCapability = _HmAddrTrackCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10001, 4)
)
_HmAddrTrackPortTable_Object = MibTable
hmAddrTrackPortTable = _HmAddrTrackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 4, 1)
)
if mibBuilder.loadTexts:
    hmAddrTrackPortTable.setStatus("mandatory")
_HmAddrTrackPortEntry_Object = MibTableRow
hmAddrTrackPortEntry = _HmAddrTrackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hmAddrTrackPortEntry.setStatus("mandatory")


class _PortHubAddrID_Type(OctetString):
    """Custom type portHubAddrID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PortHubAddrID_Type.__name__ = "OctetString"
_PortHubAddrID_Object = MibTableColumn
portHubAddrID = _PortHubAddrID_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 4, 1, 1, 1),
    _PortHubAddrID_Type()
)
portHubAddrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHubAddrID.setStatus("mandatory")


class _PortGroupAddrID_Type(Integer32):
    """Custom type portGroupAddrID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortGroupAddrID_Type.__name__ = "Integer32"
_PortGroupAddrID_Object = MibTableColumn
portGroupAddrID = _PortGroupAddrID_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 4, 1, 1, 2),
    _PortGroupAddrID_Type()
)
portGroupAddrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portGroupAddrID.setStatus("mandatory")


class _PortAddrID_Type(Integer32):
    """Custom type portAddrID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortAddrID_Type.__name__ = "Integer32"
_PortAddrID_Object = MibTableColumn
portAddrID = _PortAddrID_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 4, 1, 1, 3),
    _PortAddrID_Type()
)
portAddrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAddrID.setStatus("mandatory")


class _PortLastSourceAddress_Type(OctetString):
    """Custom type portLastSourceAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PortLastSourceAddress_Type.__name__ = "OctetString"
_PortLastSourceAddress_Object = MibTableColumn
portLastSourceAddress = _PortLastSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 4, 1, 1, 4),
    _PortLastSourceAddress_Type()
)
portLastSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLastSourceAddress.setStatus("mandatory")
_PortSourceAddrChanges_Type = Counter32
_PortSourceAddrChanges_Object = MibTableColumn
portSourceAddrChanges = _PortSourceAddrChanges_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 4, 1, 1, 5),
    _PortSourceAddrChanges_Type()
)
portSourceAddrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSourceAddrChanges.setStatus("mandatory")
_HmBadBitClockCapability_ObjectIdentity = ObjectIdentity
hmBadBitClockCapability = _HmBadBitClockCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10001, 5)
)
_HmBadBitClockPortTable_Object = MibTable
hmBadBitClockPortTable = _HmBadBitClockPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 5, 1)
)
if mibBuilder.loadTexts:
    hmBadBitClockPortTable.setStatus("mandatory")
_HmBadBitClockPortEntry_Object = MibTableRow
hmBadBitClockPortEntry = _HmBadBitClockPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 5, 1, 1)
)
if mibBuilder.loadTexts:
    hmBadBitClockPortEntry.setStatus("mandatory")


class _PortHubClockID_Type(OctetString):
    """Custom type portHubClockID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PortHubClockID_Type.__name__ = "OctetString"
_PortHubClockID_Object = MibTableColumn
portHubClockID = _PortHubClockID_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 5, 1, 1, 1),
    _PortHubClockID_Type()
)
portHubClockID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHubClockID.setStatus("mandatory")


class _PortGroupClockID_Type(Integer32):
    """Custom type portGroupClockID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortGroupClockID_Type.__name__ = "Integer32"
_PortGroupClockID_Object = MibTableColumn
portGroupClockID = _PortGroupClockID_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 5, 1, 1, 2),
    _PortGroupClockID_Type()
)
portGroupClockID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portGroupClockID.setStatus("mandatory")


class _PortClockID_Type(Integer32):
    """Custom type portClockID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortClockID_Type.__name__ = "Integer32"
_PortClockID_Object = MibTableColumn
portClockID = _PortClockID_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 5, 1, 1, 3),
    _PortClockID_Type()
)
portClockID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portClockID.setStatus("mandatory")
_PortOutOfSpecBitRate_Type = Counter32
_PortOutOfSpecBitRate_Object = MibTableColumn
portOutOfSpecBitRate = _PortOutOfSpecBitRate_Object(
    (1, 3, 6, 1, 4, 1, 33, 10001, 5, 1, 1, 4),
    _PortOutOfSpecBitRate_Type()
)
portOutOfSpecBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOutOfSpecBitRate.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYPLEX-IEEE-HUB-MIB",
    **{"xyplex": xyplex,
       "ieeeHub": ieeeHub,
       "hmBasicCapability": hmBasicCapability,
       "hmBasicHubTable": hmBasicHubTable,
       "hmBasicHubEntry": hmBasicHubEntry,
       "hubID": hubID,
       "hubGroupCapacity": hubGroupCapacity,
       "hubGroupMap": hubGroupMap,
       "hmBasicGroupTable": hmBasicGroupTable,
       "hmBasicGroupEntry": hmBasicGroupEntry,
       "groupHubID": groupHubID,
       "groupID": groupID,
       "groupNumberOfPorts": groupNumberOfPorts,
       "hmBasicPortTable": hmBasicPortTable,
       "hmBasicPortEntry": hmBasicPortEntry,
       "portHubBasicID": portHubBasicID,
       "portGroupBasicID": portGroupBasicID,
       "portBasicID": portBasicID,
       "portType": portType,
       "portAdminState": portAdminState,
       "portAutoPartitionState": portAutoPartitionState,
       "hmSelfTestCapability": hmSelfTestCapability,
       "hmSelfTestHubTable": hmSelfTestHubTable,
       "hmSelfTestHubEntry": hmSelfTestHubEntry,
       "hubSelfTestID": hubSelfTestID,
       "hubResetTimeStamp": hubResetTimeStamp,
       "hubHealthState": hubHealthState,
       "hubHealthText": hubHealthText,
       "hubHealthData": hubHealthData,
       "hubSystemResetting": hubSystemResetting,
       "hubResetting": hubResetting,
       "hubExecutingSelfTest": hubExecutingSelfTest,
       "hmPerfMonCapability": hmPerfMonCapability,
       "hmPerfMonRelayTable": hmPerfMonRelayTable,
       "hmPerfMonRelayEntry": hmPerfMonRelayEntry,
       "relayHubPerfID": relayHubPerfID,
       "relayPerfID": relayPerfID,
       "relayTotalCollisions": relayTotalCollisions,
       "hmPerfMonPortTable": hmPerfMonPortTable,
       "hmPerfMonPortEntry": hmPerfMonPortEntry,
       "portHubPerfID": portHubPerfID,
       "portGroupPerfID": portGroupPerfID,
       "portPerfID": portPerfID,
       "portReadableFrames": portReadableFrames,
       "portReadableOctets": portReadableOctets,
       "portPygmys": portPygmys,
       "portRunts": portRunts,
       "portFrameCheckSeqErrs": portFrameCheckSeqErrs,
       "portAlignmentErrors": portAlignmentErrors,
       "portFramesTooLong": portFramesTooLong,
       "portAutoPartitionCount": portAutoPartitionCount,
       "hmAddrTrackCapability": hmAddrTrackCapability,
       "hmAddrTrackPortTable": hmAddrTrackPortTable,
       "hmAddrTrackPortEntry": hmAddrTrackPortEntry,
       "portHubAddrID": portHubAddrID,
       "portGroupAddrID": portGroupAddrID,
       "portAddrID": portAddrID,
       "portLastSourceAddress": portLastSourceAddress,
       "portSourceAddrChanges": portSourceAddrChanges,
       "hmBadBitClockCapability": hmBadBitClockCapability,
       "hmBadBitClockPortTable": hmBadBitClockPortTable,
       "hmBadBitClockPortEntry": hmBadBitClockPortEntry,
       "portHubClockID": portHubClockID,
       "portGroupClockID": portGroupClockID,
       "portClockID": portClockID,
       "portOutOfSpecBitRate": portOutOfSpecBitRate}
)
