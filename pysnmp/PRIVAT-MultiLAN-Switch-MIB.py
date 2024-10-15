# SNMP MIB module (PRIVAT-MultiLAN-Switch-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PRIVAT-MultiLAN-Switch-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:42 2024
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




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Hirschmann_ObjectIdentity = ObjectIdentity
hirschmann = _Hirschmann_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248)
)
_MultiLANSwitch_ObjectIdentity = ObjectIdentity
multiLANSwitch = _MultiLANSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 2)
)
_Bridge1_ObjectIdentity = ObjectIdentity
bridge1 = _Bridge1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 2, 1)
)
_Bridgemgmt_ObjectIdentity = ObjectIdentity
bridgemgmt = _Bridgemgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1)
)
_HirmaBasCapability_ObjectIdentity = ObjectIdentity
hirmaBasCapability = _HirmaBasCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1)
)
_HirmaBasBridgeTable_ObjectIdentity = ObjectIdentity
hirmaBasBridgeTable = _HirmaBasBridgeTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 1)
)
_HirmaBasBridgeGroupCapacity_Type = Integer32
_HirmaBasBridgeGroupCapacity_Object = MibScalar
hirmaBasBridgeGroupCapacity = _HirmaBasBridgeGroupCapacity_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 1, 1),
    _HirmaBasBridgeGroupCapacity_Type()
)
hirmaBasBridgeGroupCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasBridgeGroupCapacity.setStatus("mandatory")
_HirmaBasBridgeGroupMap_Type = Integer32
_HirmaBasBridgeGroupMap_Object = MibScalar
hirmaBasBridgeGroupMap = _HirmaBasBridgeGroupMap_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 1, 2),
    _HirmaBasBridgeGroupMap_Type()
)
hirmaBasBridgeGroupMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasBridgeGroupMap.setStatus("mandatory")
_HirmaBasBridgeSoftVersion_Type = DisplayString
_HirmaBasBridgeSoftVersion_Object = MibScalar
hirmaBasBridgeSoftVersion = _HirmaBasBridgeSoftVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 1, 3),
    _HirmaBasBridgeSoftVersion_Type()
)
hirmaBasBridgeSoftVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasBridgeSoftVersion.setStatus("mandatory")
_HirmaBasBridgeHardVersion_Type = DisplayString
_HirmaBasBridgeHardVersion_Object = MibScalar
hirmaBasBridgeHardVersion = _HirmaBasBridgeHardVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 1, 4),
    _HirmaBasBridgeHardVersion_Type()
)
hirmaBasBridgeHardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasBridgeHardVersion.setStatus("mandatory")
_HirmaBasBridgeMibVersion_Type = DisplayString
_HirmaBasBridgeMibVersion_Object = MibScalar
hirmaBasBridgeMibVersion = _HirmaBasBridgeMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 1, 5),
    _HirmaBasBridgeMibVersion_Type()
)
hirmaBasBridgeMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasBridgeMibVersion.setStatus("mandatory")
_HirmaBasBridgeSpanningTreeVersion_Type = DisplayString
_HirmaBasBridgeSpanningTreeVersion_Object = MibScalar
hirmaBasBridgeSpanningTreeVersion = _HirmaBasBridgeSpanningTreeVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 1, 6),
    _HirmaBasBridgeSpanningTreeVersion_Type()
)
hirmaBasBridgeSpanningTreeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasBridgeSpanningTreeVersion.setStatus("mandatory")
_HirmaBasBridgeSwitches_Type = Integer32
_HirmaBasBridgeSwitches_Object = MibScalar
hirmaBasBridgeSwitches = _HirmaBasBridgeSwitches_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 1, 7),
    _HirmaBasBridgeSwitches_Type()
)
hirmaBasBridgeSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasBridgeSwitches.setStatus("mandatory")


class _HirmaBasBridgePwrSplyState_Type(Integer32):
    """Custom type hirmaBasBridgePwrSplyState based on Integer32"""
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
        *(("error5V1", 2),
          ("error5V1and5V2", 4),
          ("error5V1and5V3", 6),
          ("error5V2", 3),
          ("error5V2and5v3", 7),
          ("error5V3", 5),
          ("error5v1and5v2and5v3", 8),
          ("ok", 1))
    )


_HirmaBasBridgePwrSplyState_Type.__name__ = "Integer32"
_HirmaBasBridgePwrSplyState_Object = MibScalar
hirmaBasBridgePwrSplyState = _HirmaBasBridgePwrSplyState_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 1, 8),
    _HirmaBasBridgePwrSplyState_Type()
)
hirmaBasBridgePwrSplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasBridgePwrSplyState.setStatus("mandatory")


class _HirmaBasBridgeFanState_Type(Integer32):
    """Custom type hirmaBasBridgeFanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nofunction", 2),
          ("ok", 1))
    )


_HirmaBasBridgeFanState_Type.__name__ = "Integer32"
_HirmaBasBridgeFanState_Object = MibScalar
hirmaBasBridgeFanState = _HirmaBasBridgeFanState_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 1, 9),
    _HirmaBasBridgeFanState_Type()
)
hirmaBasBridgeFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasBridgeFanState.setStatus("mandatory")


class _HirmaBasBridgePwrAlarm_Type(Integer32):
    """Custom type hirmaBasBridgePwrAlarm based on Integer32"""
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


_HirmaBasBridgePwrAlarm_Type.__name__ = "Integer32"
_HirmaBasBridgePwrAlarm_Object = MibScalar
hirmaBasBridgePwrAlarm = _HirmaBasBridgePwrAlarm_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 1, 10),
    _HirmaBasBridgePwrAlarm_Type()
)
hirmaBasBridgePwrAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaBasBridgePwrAlarm.setStatus("mandatory")


class _HirmaBasBridgeHealthAlarm_Type(Integer32):
    """Custom type hirmaBasBridgeHealthAlarm based on Integer32"""
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


_HirmaBasBridgeHealthAlarm_Type.__name__ = "Integer32"
_HirmaBasBridgeHealthAlarm_Object = MibScalar
hirmaBasBridgeHealthAlarm = _HirmaBasBridgeHealthAlarm_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 1, 11),
    _HirmaBasBridgeHealthAlarm_Type()
)
hirmaBasBridgeHealthAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaBasBridgeHealthAlarm.setStatus("mandatory")


class _HirmaBasBridgeSpanningTree_Type(Integer32):
    """Custom type hirmaBasBridgeSpanningTree based on Integer32"""
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


_HirmaBasBridgeSpanningTree_Type.__name__ = "Integer32"
_HirmaBasBridgeSpanningTree_Object = MibScalar
hirmaBasBridgeSpanningTree = _HirmaBasBridgeSpanningTree_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 1, 12),
    _HirmaBasBridgeSpanningTree_Type()
)
hirmaBasBridgeSpanningTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaBasBridgeSpanningTree.setStatus("mandatory")


class _HirmaBasBridgeHealthState_Type(Integer32):
    """Custom type hirmaBasBridgeHealthState based on Integer32"""
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
        *(("generalFailure", 3),
          ("multiLANSwitchFailure", 4),
          ("ok", 2),
          ("other", 1))
    )


_HirmaBasBridgeHealthState_Type.__name__ = "Integer32"
_HirmaBasBridgeHealthState_Object = MibScalar
hirmaBasBridgeHealthState = _HirmaBasBridgeHealthState_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 1, 13),
    _HirmaBasBridgeHealthState_Type()
)
hirmaBasBridgeHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasBridgeHealthState.setStatus("mandatory")


class _HirmaBasBridgeHealthText_Type(DisplayString):
    """Custom type hirmaBasBridgeHealthText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HirmaBasBridgeHealthText_Type.__name__ = "DisplayString"
_HirmaBasBridgeHealthText_Object = MibScalar
hirmaBasBridgeHealthText = _HirmaBasBridgeHealthText_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 1, 14),
    _HirmaBasBridgeHealthText_Type()
)
hirmaBasBridgeHealthText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasBridgeHealthText.setStatus("mandatory")


class _HirmaBasBridgeHealthData_Type(OctetString):
    """Custom type hirmaBasBridgeHealthData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HirmaBasBridgeHealthData_Type.__name__ = "OctetString"
_HirmaBasBridgeHealthData_Object = MibScalar
hirmaBasBridgeHealthData = _HirmaBasBridgeHealthData_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 1, 15),
    _HirmaBasBridgeHealthData_Type()
)
hirmaBasBridgeHealthData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasBridgeHealthData.setStatus("mandatory")


class _HirmaBasBridgeCounterReset_Type(Integer32):
    """Custom type hirmaBasBridgeCounterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-reset", 2),
          ("reset", 1))
    )


_HirmaBasBridgeCounterReset_Type.__name__ = "Integer32"
_HirmaBasBridgeCounterReset_Object = MibScalar
hirmaBasBridgeCounterReset = _HirmaBasBridgeCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 1, 16),
    _HirmaBasBridgeCounterReset_Type()
)
hirmaBasBridgeCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaBasBridgeCounterReset.setStatus("mandatory")
_HirmaBasBridgeEventTable_Object = MibTable
hirmaBasBridgeEventTable = _HirmaBasBridgeEventTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hirmaBasBridgeEventTable.setStatus("mandatory")
_HirmaBasBridgeEventEntry_Object = MibTableRow
hirmaBasBridgeEventEntry = _HirmaBasBridgeEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 2, 1)
)
hirmaBasBridgeEventEntry.setIndexNames(
    (0, "PRIVAT-MultiLAN-Switch-MIB", "hirmaBasBridgeMessageID"),
)
if mibBuilder.loadTexts:
    hirmaBasBridgeEventEntry.setStatus("mandatory")
_HirmaBasBridgeMessageID_Type = Integer32
_HirmaBasBridgeMessageID_Object = MibTableColumn
hirmaBasBridgeMessageID = _HirmaBasBridgeMessageID_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 2, 1, 1),
    _HirmaBasBridgeMessageID_Type()
)
hirmaBasBridgeMessageID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasBridgeMessageID.setStatus("mandatory")
_HirmaBasBridgeMessageIfIndex_Type = Integer32
_HirmaBasBridgeMessageIfIndex_Object = MibTableColumn
hirmaBasBridgeMessageIfIndex = _HirmaBasBridgeMessageIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 2, 1, 2),
    _HirmaBasBridgeMessageIfIndex_Type()
)
hirmaBasBridgeMessageIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasBridgeMessageIfIndex.setStatus("mandatory")
_HirmaBasBridgeMessage_Type = OctetString
_HirmaBasBridgeMessage_Object = MibTableColumn
hirmaBasBridgeMessage = _HirmaBasBridgeMessage_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 2, 1, 3),
    _HirmaBasBridgeMessage_Type()
)
hirmaBasBridgeMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasBridgeMessage.setStatus("mandatory")
_HirmaBasBridgeMessageTime_Type = TimeTicks
_HirmaBasBridgeMessageTime_Object = MibTableColumn
hirmaBasBridgeMessageTime = _HirmaBasBridgeMessageTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 2, 1, 4),
    _HirmaBasBridgeMessageTime_Type()
)
hirmaBasBridgeMessageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasBridgeMessageTime.setStatus("mandatory")
_HirmaBasGroupTable_Object = MibTable
hirmaBasGroupTable = _HirmaBasGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hirmaBasGroupTable.setStatus("mandatory")
_HirmaBasGroupEntry_Object = MibTableRow
hirmaBasGroupEntry = _HirmaBasGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 3, 1)
)
hirmaBasGroupEntry.setIndexNames(
    (0, "PRIVAT-MultiLAN-Switch-MIB", "hirmaBasGroupID"),
)
if mibBuilder.loadTexts:
    hirmaBasGroupEntry.setStatus("mandatory")
_HirmaBasGroupID_Type = Integer32
_HirmaBasGroupID_Object = MibTableColumn
hirmaBasGroupID = _HirmaBasGroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 3, 1, 1),
    _HirmaBasGroupID_Type()
)
hirmaBasGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasGroupID.setStatus("mandatory")
_HirmaBasGroupNumOfPorts_Type = Integer32
_HirmaBasGroupNumOfPorts_Object = MibTableColumn
hirmaBasGroupNumOfPorts = _HirmaBasGroupNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 3, 1, 2),
    _HirmaBasGroupNumOfPorts_Type()
)
hirmaBasGroupNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasGroupNumOfPorts.setStatus("mandatory")
_HirmaBasGroupPortMap_Type = DisplayString
_HirmaBasGroupPortMap_Object = MibTableColumn
hirmaBasGroupPortMap = _HirmaBasGroupPortMap_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 3, 1, 3),
    _HirmaBasGroupPortMap_Type()
)
hirmaBasGroupPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasGroupPortMap.setStatus("mandatory")
_HirmaBasGroupName_Type = DisplayString
_HirmaBasGroupName_Object = MibTableColumn
hirmaBasGroupName = _HirmaBasGroupName_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 3, 1, 4),
    _HirmaBasGroupName_Type()
)
hirmaBasGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasGroupName.setStatus("mandatory")
_HirmaBasPortTable_Object = MibTable
hirmaBasPortTable = _HirmaBasPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hirmaBasPortTable.setStatus("mandatory")
_HirmaBasPortEntry_Object = MibTableRow
hirmaBasPortEntry = _HirmaBasPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 4, 1)
)
hirmaBasPortEntry.setIndexNames(
    (0, "PRIVAT-MultiLAN-Switch-MIB", "hirmaBasPortID"),
)
if mibBuilder.loadTexts:
    hirmaBasPortEntry.setStatus("mandatory")
_HirmaBasPortID_Type = Integer32
_HirmaBasPortID_Object = MibTableColumn
hirmaBasPortID = _HirmaBasPortID_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 4, 1, 1),
    _HirmaBasPortID_Type()
)
hirmaBasPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasPortID.setStatus("mandatory")
_HirmaBasPortGroupID_Type = Integer32
_HirmaBasPortGroupID_Object = MibTableColumn
hirmaBasPortGroupID = _HirmaBasPortGroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 4, 1, 2),
    _HirmaBasPortGroupID_Type()
)
hirmaBasPortGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasPortGroupID.setStatus("mandatory")


class _HirmaBasPortLanType_Type(Integer32):
    """Custom type hirmaBasPortLanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("fddi", 2))
    )


_HirmaBasPortLanType_Type.__name__ = "Integer32"
_HirmaBasPortLanType_Object = MibTableColumn
hirmaBasPortLanType = _HirmaBasPortLanType_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 4, 1, 3),
    _HirmaBasPortLanType_Type()
)
hirmaBasPortLanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasPortLanType.setStatus("mandatory")


class _HirmaBasPortType_Type(Integer32):
    """Custom type hirmaBasPortType based on Integer32"""
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
        *(("aui", 1),
          ("optical-asynch-1300-16", 3),
          ("optical-asynch-1300-40", 4),
          ("optical-asynch-850", 2),
          ("unshielded-TP-10BaseT", 5))
    )


_HirmaBasPortType_Type.__name__ = "Integer32"
_HirmaBasPortType_Object = MibTableColumn
hirmaBasPortType = _HirmaBasPortType_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 4, 1, 4),
    _HirmaBasPortType_Type()
)
hirmaBasPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasPortType.setStatus("mandatory")


class _HirmaBasPortShortDelay_Type(Integer32):
    """Custom type hirmaBasPortShortDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-switch", 2),
          ("ieee802-3", 1))
    )


_HirmaBasPortShortDelay_Type.__name__ = "Integer32"
_HirmaBasPortShortDelay_Object = MibTableColumn
hirmaBasPortShortDelay = _HirmaBasPortShortDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 4, 1, 5),
    _HirmaBasPortShortDelay_Type()
)
hirmaBasPortShortDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaBasPortShortDelay.setStatus("mandatory")


class _HirmaBasPortLearning_Type(Integer32):
    """Custom type hirmaBasPortLearning based on Integer32"""
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


_HirmaBasPortLearning_Type.__name__ = "Integer32"
_HirmaBasPortLearning_Object = MibTableColumn
hirmaBasPortLearning = _HirmaBasPortLearning_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 4, 1, 6),
    _HirmaBasPortLearning_Type()
)
hirmaBasPortLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaBasPortLearning.setStatus("mandatory")


class _HirmaBasPortFiltering_Type(Integer32):
    """Custom type hirmaBasPortFiltering based on Integer32"""
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


_HirmaBasPortFiltering_Type.__name__ = "Integer32"
_HirmaBasPortFiltering_Object = MibTableColumn
hirmaBasPortFiltering = _HirmaBasPortFiltering_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 4, 1, 7),
    _HirmaBasPortFiltering_Type()
)
hirmaBasPortFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaBasPortFiltering.setStatus("mandatory")


class _HirmaBasPortRelay_Type(Integer32):
    """Custom type hirmaBasPortRelay based on Integer32"""
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


_HirmaBasPortRelay_Type.__name__ = "Integer32"
_HirmaBasPortRelay_Object = MibTableColumn
hirmaBasPortRelay = _HirmaBasPortRelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 4, 1, 8),
    _HirmaBasPortRelay_Type()
)
hirmaBasPortRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaBasPortRelay.setStatus("mandatory")


class _HirmaBasPortMode_Type(Integer32):
    """Custom type hirmaBasPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 2),
          ("half-duplex", 1))
    )


_HirmaBasPortMode_Type.__name__ = "Integer32"
_HirmaBasPortMode_Object = MibTableColumn
hirmaBasPortMode = _HirmaBasPortMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 4, 1, 9),
    _HirmaBasPortMode_Type()
)
hirmaBasPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasPortMode.setStatus("mandatory")


class _HirmaBasPortCounterReset_Type(Integer32):
    """Custom type hirmaBasPortCounterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-reset", 2),
          ("reset", 1))
    )


_HirmaBasPortCounterReset_Type.__name__ = "Integer32"
_HirmaBasPortCounterReset_Object = MibTableColumn
hirmaBasPortCounterReset = _HirmaBasPortCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 4, 1, 10),
    _HirmaBasPortCounterReset_Type()
)
hirmaBasPortCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaBasPortCounterReset.setStatus("mandatory")
_HirmaBasPortState_Type = DisplayString
_HirmaBasPortState_Object = MibTableColumn
hirmaBasPortState = _HirmaBasPortState_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 1, 4, 1, 11),
    _HirmaBasPortState_Type()
)
hirmaBasPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaBasPortState.setStatus("mandatory")
_HirmaSelfTestCapability_ObjectIdentity = ObjectIdentity
hirmaSelfTestCapability = _HirmaSelfTestCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 2)
)


class _HirmaSelfTestBridgeReset_Type(Integer32):
    """Custom type hirmaSelfTestBridgeReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-reset", 2),
          ("reset", 1))
    )


_HirmaSelfTestBridgeReset_Type.__name__ = "Integer32"
_HirmaSelfTestBridgeReset_Object = MibScalar
hirmaSelfTestBridgeReset = _HirmaSelfTestBridgeReset_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 2, 1),
    _HirmaSelfTestBridgeReset_Type()
)
hirmaSelfTestBridgeReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaSelfTestBridgeReset.setStatus("mandatory")


class _HirmaSelfTestBridgeResetType_Type(Integer32):
    """Custom type hirmaSelfTestBridgeResetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cold-start", 2),
          ("warm-start", 1))
    )


_HirmaSelfTestBridgeResetType_Type.__name__ = "Integer32"
_HirmaSelfTestBridgeResetType_Object = MibScalar
hirmaSelfTestBridgeResetType = _HirmaSelfTestBridgeResetType_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 2, 2),
    _HirmaSelfTestBridgeResetType_Type()
)
hirmaSelfTestBridgeResetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaSelfTestBridgeResetType.setStatus("mandatory")


class _HirmaSelfTestBridgeSetDefaults_Type(Integer32):
    """Custom type hirmaSelfTestBridgeSetDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-reset", 2),
          ("reset", 1))
    )


_HirmaSelfTestBridgeSetDefaults_Type.__name__ = "Integer32"
_HirmaSelfTestBridgeSetDefaults_Object = MibScalar
hirmaSelfTestBridgeSetDefaults = _HirmaSelfTestBridgeSetDefaults_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 2, 3),
    _HirmaSelfTestBridgeSetDefaults_Type()
)
hirmaSelfTestBridgeSetDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaSelfTestBridgeSetDefaults.setStatus("mandatory")
_HirmaSelfTestGroupTable_Object = MibTable
hirmaSelfTestGroupTable = _HirmaSelfTestGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hirmaSelfTestGroupTable.setStatus("mandatory")
_HirmaSelfTestGroupEntry_Object = MibTableRow
hirmaSelfTestGroupEntry = _HirmaSelfTestGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 2, 4, 1)
)
hirmaSelfTestGroupEntry.setIndexNames(
    (0, "PRIVAT-MultiLAN-Switch-MIB", "hirmaSelfTestGroupID"),
)
if mibBuilder.loadTexts:
    hirmaSelfTestGroupEntry.setStatus("mandatory")
_HirmaSelfTestGroupID_Type = Integer32
_HirmaSelfTestGroupID_Object = MibTableColumn
hirmaSelfTestGroupID = _HirmaSelfTestGroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 2, 4, 1, 1),
    _HirmaSelfTestGroupID_Type()
)
hirmaSelfTestGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaSelfTestGroupID.setStatus("mandatory")


class _HirmaSelfTestGroupDisplayTest_Type(Integer32):
    """Custom type hirmaSelfTestGroupDisplayTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-test", 2),
          ("test", 1))
    )


_HirmaSelfTestGroupDisplayTest_Type.__name__ = "Integer32"
_HirmaSelfTestGroupDisplayTest_Object = MibTableColumn
hirmaSelfTestGroupDisplayTest = _HirmaSelfTestGroupDisplayTest_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 2, 4, 1, 2),
    _HirmaSelfTestGroupDisplayTest_Type()
)
hirmaSelfTestGroupDisplayTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaSelfTestGroupDisplayTest.setStatus("mandatory")


class _HirmaSelfTestGroupSQETest_Type(Integer32):
    """Custom type hirmaSelfTestGroupSQETest based on Integer32"""
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
          ("enabled-ok", 1),
          ("not-ok", 3))
    )


_HirmaSelfTestGroupSQETest_Type.__name__ = "Integer32"
_HirmaSelfTestGroupSQETest_Object = MibTableColumn
hirmaSelfTestGroupSQETest = _HirmaSelfTestGroupSQETest_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 2, 4, 1, 3),
    _HirmaSelfTestGroupSQETest_Type()
)
hirmaSelfTestGroupSQETest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaSelfTestGroupSQETest.setStatus("mandatory")
_HirmaFilterCapability_ObjectIdentity = ObjectIdentity
hirmaFilterCapability = _HirmaFilterCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 3)
)
_HirmaFilterMaxNumOfFilters_Type = Integer32
_HirmaFilterMaxNumOfFilters_Object = MibScalar
hirmaFilterMaxNumOfFilters = _HirmaFilterMaxNumOfFilters_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 3, 1),
    _HirmaFilterMaxNumOfFilters_Type()
)
hirmaFilterMaxNumOfFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaFilterMaxNumOfFilters.setStatus("mandatory")
_HirmaFilterTable_Object = MibTable
hirmaFilterTable = _HirmaFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hirmaFilterTable.setStatus("mandatory")
_HirmaFilterTableEntry_Object = MibTableRow
hirmaFilterTableEntry = _HirmaFilterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 3, 2, 1)
)
hirmaFilterTableEntry.setIndexNames(
    (0, "PRIVAT-MultiLAN-Switch-MIB", "hirmaFilterID"),
)
if mibBuilder.loadTexts:
    hirmaFilterTableEntry.setStatus("mandatory")
_HirmaFilterID_Type = Integer32
_HirmaFilterID_Object = MibTableColumn
hirmaFilterID = _HirmaFilterID_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 3, 2, 1, 1),
    _HirmaFilterID_Type()
)
hirmaFilterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaFilterID.setStatus("mandatory")


class _HirmaFilterMode_Type(Integer32):
    """Custom type hirmaFilterMode based on Integer32"""
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
        *(("alone", 4),
          ("channel", 5),
          ("delete", 6),
          ("disable", 2),
          ("discard", 3),
          ("forward", 1))
    )


_HirmaFilterMode_Type.__name__ = "Integer32"
_HirmaFilterMode_Object = MibTableColumn
hirmaFilterMode = _HirmaFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 3, 2, 1, 2),
    _HirmaFilterMode_Type()
)
hirmaFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaFilterMode.setStatus("mandatory")
_HirmaFilterDest_Type = DisplayString
_HirmaFilterDest_Object = MibTableColumn
hirmaFilterDest = _HirmaFilterDest_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 3, 2, 1, 3),
    _HirmaFilterDest_Type()
)
hirmaFilterDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaFilterDest.setStatus("mandatory")
_HirmaFilterSrc_Type = DisplayString
_HirmaFilterSrc_Object = MibTableColumn
hirmaFilterSrc = _HirmaFilterSrc_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 3, 2, 1, 4),
    _HirmaFilterSrc_Type()
)
hirmaFilterSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaFilterSrc.setStatus("mandatory")
_HirmaFilterType_Type = DisplayString
_HirmaFilterType_Object = MibTableColumn
hirmaFilterType = _HirmaFilterType_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 3, 2, 1, 5),
    _HirmaFilterType_Type()
)
hirmaFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaFilterType.setStatus("mandatory")
_HirmaFilterPortIn_Type = DisplayString
_HirmaFilterPortIn_Object = MibTableColumn
hirmaFilterPortIn = _HirmaFilterPortIn_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 3, 2, 1, 6),
    _HirmaFilterPortIn_Type()
)
hirmaFilterPortIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaFilterPortIn.setStatus("mandatory")
_HirmaFilterPortOut_Type = DisplayString
_HirmaFilterPortOut_Object = MibTableColumn
hirmaFilterPortOut = _HirmaFilterPortOut_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 3, 2, 1, 7),
    _HirmaFilterPortOut_Type()
)
hirmaFilterPortOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaFilterPortOut.setStatus("mandatory")
_HirmaAddrBTCapability_ObjectIdentity = ObjectIdentity
hirmaAddrBTCapability = _HirmaAddrBTCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 4)
)
_HirmaAddrBTAddr_Type = MacAddress
_HirmaAddrBTAddr_Object = MibScalar
hirmaAddrBTAddr = _HirmaAddrBTAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 4, 1),
    _HirmaAddrBTAddr_Type()
)
hirmaAddrBTAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaAddrBTAddr.setStatus("mandatory")
_HirmaAddrBTBlock_Type = OctetString
_HirmaAddrBTBlock_Object = MibScalar
hirmaAddrBTBlock = _HirmaAddrBTBlock_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 4, 2),
    _HirmaAddrBTBlock_Type()
)
hirmaAddrBTBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaAddrBTBlock.setStatus("mandatory")
_HirmaLoadCapability_ObjectIdentity = ObjectIdentity
hirmaLoadCapability = _HirmaLoadCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 5)
)
_HirmaFlashUpdate_ObjectIdentity = ObjectIdentity
hirmaFlashUpdate = _HirmaFlashUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 5, 1)
)
_HirmaFlashUpdateIPAddr_Type = IpAddress
_HirmaFlashUpdateIPAddr_Object = MibScalar
hirmaFlashUpdateIPAddr = _HirmaFlashUpdateIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 5, 1, 1),
    _HirmaFlashUpdateIPAddr_Type()
)
hirmaFlashUpdateIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaFlashUpdateIPAddr.setStatus("mandatory")
_HirmaFlashUpdateName_Type = DisplayString
_HirmaFlashUpdateName_Object = MibScalar
hirmaFlashUpdateName = _HirmaFlashUpdateName_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 5, 1, 2),
    _HirmaFlashUpdateName_Type()
)
hirmaFlashUpdateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaFlashUpdateName.setStatus("mandatory")


class _HirmaFlashUpdateAction_Type(Integer32):
    """Custom type hirmaFlashUpdateAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal-mode", 2),
          ("program", 1))
    )


_HirmaFlashUpdateAction_Type.__name__ = "Integer32"
_HirmaFlashUpdateAction_Object = MibScalar
hirmaFlashUpdateAction = _HirmaFlashUpdateAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 5, 1, 3),
    _HirmaFlashUpdateAction_Type()
)
hirmaFlashUpdateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaFlashUpdateAction.setStatus("mandatory")
_HirmaLoadSaveConfig_ObjectIdentity = ObjectIdentity
hirmaLoadSaveConfig = _HirmaLoadSaveConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 5, 2)
)
_HirmaLoadSaveConIPAddr_Type = IpAddress
_HirmaLoadSaveConIPAddr_Object = MibScalar
hirmaLoadSaveConIPAddr = _HirmaLoadSaveConIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 5, 2, 1),
    _HirmaLoadSaveConIPAddr_Type()
)
hirmaLoadSaveConIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaLoadSaveConIPAddr.setStatus("mandatory")
_HirmaLoadSaveConName_Type = DisplayString
_HirmaLoadSaveConName_Object = MibScalar
hirmaLoadSaveConName = _HirmaLoadSaveConName_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 5, 2, 2),
    _HirmaLoadSaveConName_Type()
)
hirmaLoadSaveConName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaLoadSaveConName.setStatus("mandatory")


class _HirmaLoadSaveConAction_Type(Integer32):
    """Custom type hirmaLoadSaveConAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("load", 1),
          ("normal-mode", 2),
          ("save", 3))
    )


_HirmaLoadSaveConAction_Type.__name__ = "Integer32"
_HirmaLoadSaveConAction_Object = MibScalar
hirmaLoadSaveConAction = _HirmaLoadSaveConAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 1, 5, 2, 3),
    _HirmaLoadSaveConAction_Type()
)
hirmaLoadSaveConAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaLoadSaveConAction.setStatus("mandatory")
_HirmaMibhHandler_ObjectIdentity = ObjectIdentity
hirmaMibhHandler = _HirmaMibhHandler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 2)
)
_HirmaMibhCommTable_Object = MibTable
hirmaMibhCommTable = _HirmaMibhCommTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hirmaMibhCommTable.setStatus("mandatory")
_HirmaMibhCommEntry_Object = MibTableRow
hirmaMibhCommEntry = _HirmaMibhCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 2, 1, 1)
)
hirmaMibhCommEntry.setIndexNames(
    (0, "PRIVAT-MultiLAN-Switch-MIB", "hirmaMibhCommIndex"),
)
if mibBuilder.loadTexts:
    hirmaMibhCommEntry.setStatus("mandatory")
_HirmaMibhCommIndex_Type = Integer32
_HirmaMibhCommIndex_Object = MibTableColumn
hirmaMibhCommIndex = _HirmaMibhCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 2, 1, 1, 1),
    _HirmaMibhCommIndex_Type()
)
hirmaMibhCommIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaMibhCommIndex.setStatus("mandatory")
_HirmaMibhCommCommunity_Type = DisplayString
_HirmaMibhCommCommunity_Object = MibTableColumn
hirmaMibhCommCommunity = _HirmaMibhCommCommunity_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 2, 1, 1, 2),
    _HirmaMibhCommCommunity_Type()
)
hirmaMibhCommCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaMibhCommCommunity.setStatus("mandatory")


class _HirmaMibhCommAccess_Type(Integer32):
    """Custom type hirmaMibhCommAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-accesible", 1),
          ("read-only", 2),
          ("read-write", 3))
    )


_HirmaMibhCommAccess_Type.__name__ = "Integer32"
_HirmaMibhCommAccess_Object = MibTableColumn
hirmaMibhCommAccess = _HirmaMibhCommAccess_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 2, 1, 1, 3),
    _HirmaMibhCommAccess_Type()
)
hirmaMibhCommAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaMibhCommAccess.setStatus("mandatory")
_HirmaMibhAccessTable_Object = MibTable
hirmaMibhAccessTable = _HirmaMibhAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hirmaMibhAccessTable.setStatus("mandatory")
_HirmaMibhAccessEntry_Object = MibTableRow
hirmaMibhAccessEntry = _HirmaMibhAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 2, 2, 1)
)
hirmaMibhAccessEntry.setIndexNames(
    (0, "PRIVAT-MultiLAN-Switch-MIB", "hirmaMibhAccessCommIndex"),
    (0, "PRIVAT-MultiLAN-Switch-MIB", "hirmaMibhAccessIPAddr"),
    (0, "PRIVAT-MultiLAN-Switch-MIB", "hirmaMibhAccessPort"),
)
if mibBuilder.loadTexts:
    hirmaMibhAccessEntry.setStatus("mandatory")
_HirmaMibhAccessCommIndex_Type = Integer32
_HirmaMibhAccessCommIndex_Object = MibTableColumn
hirmaMibhAccessCommIndex = _HirmaMibhAccessCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 2, 2, 1, 1),
    _HirmaMibhAccessCommIndex_Type()
)
hirmaMibhAccessCommIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaMibhAccessCommIndex.setStatus("mandatory")
_HirmaMibhAccessIPAddr_Type = IpAddress
_HirmaMibhAccessIPAddr_Object = MibTableColumn
hirmaMibhAccessIPAddr = _HirmaMibhAccessIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 2, 2, 1, 2),
    _HirmaMibhAccessIPAddr_Type()
)
hirmaMibhAccessIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaMibhAccessIPAddr.setStatus("mandatory")
_HirmaMibhAccessPort_Type = Integer32
_HirmaMibhAccessPort_Object = MibTableColumn
hirmaMibhAccessPort = _HirmaMibhAccessPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 2, 2, 1, 3),
    _HirmaMibhAccessPort_Type()
)
hirmaMibhAccessPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaMibhAccessPort.setStatus("mandatory")
_HirmaMibhAccessCommunity_Type = DisplayString
_HirmaMibhAccessCommunity_Object = MibTableColumn
hirmaMibhAccessCommunity = _HirmaMibhAccessCommunity_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 2, 2, 1, 4),
    _HirmaMibhAccessCommunity_Type()
)
hirmaMibhAccessCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaMibhAccessCommunity.setStatus("mandatory")


class _HirmaMibhAccessAccess_Type(Integer32):
    """Custom type hirmaMibhAccessAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("read-only", 1),
          ("read-write", 3))
    )


_HirmaMibhAccessAccess_Type.__name__ = "Integer32"
_HirmaMibhAccessAccess_Object = MibTableColumn
hirmaMibhAccessAccess = _HirmaMibhAccessAccess_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 2, 2, 1, 5),
    _HirmaMibhAccessAccess_Type()
)
hirmaMibhAccessAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaMibhAccessAccess.setStatus("mandatory")


class _HirmaMibhAccessState_Type(Integer32):
    """Custom type hirmaMibhAccessState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_HirmaMibhAccessState_Type.__name__ = "Integer32"
_HirmaMibhAccessState_Object = MibTableColumn
hirmaMibhAccessState = _HirmaMibhAccessState_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 2, 2, 1, 6),
    _HirmaMibhAccessState_Type()
)
hirmaMibhAccessState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaMibhAccessState.setStatus("mandatory")
_HirmaMibhTrapTable_Object = MibTable
hirmaMibhTrapTable = _HirmaMibhTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hirmaMibhTrapTable.setStatus("mandatory")
_HirmaMibhTrapEntry_Object = MibTableRow
hirmaMibhTrapEntry = _HirmaMibhTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 2, 3, 1)
)
hirmaMibhTrapEntry.setIndexNames(
    (0, "PRIVAT-MultiLAN-Switch-MIB", "hirmaMibhTrapCommIndex"),
    (0, "PRIVAT-MultiLAN-Switch-MIB", "hirmaMibhTrapIPAddr"),
    (0, "PRIVAT-MultiLAN-Switch-MIB", "hirmaMibhTrapPort"),
)
if mibBuilder.loadTexts:
    hirmaMibhTrapEntry.setStatus("mandatory")
_HirmaMibhTrapCommIndex_Type = Integer32
_HirmaMibhTrapCommIndex_Object = MibTableColumn
hirmaMibhTrapCommIndex = _HirmaMibhTrapCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 2, 3, 1, 1),
    _HirmaMibhTrapCommIndex_Type()
)
hirmaMibhTrapCommIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaMibhTrapCommIndex.setStatus("mandatory")
_HirmaMibhTrapIPAddr_Type = IpAddress
_HirmaMibhTrapIPAddr_Object = MibTableColumn
hirmaMibhTrapIPAddr = _HirmaMibhTrapIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 2, 3, 1, 2),
    _HirmaMibhTrapIPAddr_Type()
)
hirmaMibhTrapIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaMibhTrapIPAddr.setStatus("mandatory")
_HirmaMibhTrapPort_Type = Integer32
_HirmaMibhTrapPort_Object = MibTableColumn
hirmaMibhTrapPort = _HirmaMibhTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 2, 3, 1, 3),
    _HirmaMibhTrapPort_Type()
)
hirmaMibhTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaMibhTrapPort.setStatus("mandatory")
_HirmaMibhTrapCommunity_Type = DisplayString
_HirmaMibhTrapCommunity_Object = MibTableColumn
hirmaMibhTrapCommunity = _HirmaMibhTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 2, 3, 1, 4),
    _HirmaMibhTrapCommunity_Type()
)
hirmaMibhTrapCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaMibhTrapCommunity.setStatus("mandatory")


class _HirmaMibhTrapState_Type(Integer32):
    """Custom type hirmaMibhTrapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_HirmaMibhTrapState_Type.__name__ = "Integer32"
_HirmaMibhTrapState_Object = MibTableColumn
hirmaMibhTrapState = _HirmaMibhTrapState_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 2, 3, 1, 5),
    _HirmaMibhTrapState_Type()
)
hirmaMibhTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaMibhTrapState.setStatus("mandatory")
_HirmaUserInterface_ObjectIdentity = ObjectIdentity
hirmaUserInterface = _HirmaUserInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 3)
)
_HirmaLuiSystemTable_ObjectIdentity = ObjectIdentity
hirmaLuiSystemTable = _HirmaLuiSystemTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 3, 1)
)
_HirmaLuiLocalIPAddr_Type = IpAddress
_HirmaLuiLocalIPAddr_Object = MibScalar
hirmaLuiLocalIPAddr = _HirmaLuiLocalIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 3, 1, 1),
    _HirmaLuiLocalIPAddr_Type()
)
hirmaLuiLocalIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaLuiLocalIPAddr.setStatus("mandatory")
_HirmaLuiGatewayIPAddr_Type = IpAddress
_HirmaLuiGatewayIPAddr_Object = MibScalar
hirmaLuiGatewayIPAddr = _HirmaLuiGatewayIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 3, 1, 2),
    _HirmaLuiGatewayIPAddr_Type()
)
hirmaLuiGatewayIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaLuiGatewayIPAddr.setStatus("mandatory")
_HirmaLuiNetMask_Type = IpAddress
_HirmaLuiNetMask_Object = MibScalar
hirmaLuiNetMask = _HirmaLuiNetMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 3, 1, 3),
    _HirmaLuiNetMask_Type()
)
hirmaLuiNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaLuiNetMask.setStatus("mandatory")
_HirmaLuiUserTable_Object = MibTable
hirmaLuiUserTable = _HirmaLuiUserTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hirmaLuiUserTable.setStatus("mandatory")
_HirmaLuiUserEntry_Object = MibTableRow
hirmaLuiUserEntry = _HirmaLuiUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 3, 2, 1)
)
hirmaLuiUserEntry.setIndexNames(
    (0, "PRIVAT-MultiLAN-Switch-MIB", "hirmaLuiUserID"),
)
if mibBuilder.loadTexts:
    hirmaLuiUserEntry.setStatus("mandatory")
_HirmaLuiUserID_Type = Integer32
_HirmaLuiUserID_Object = MibTableColumn
hirmaLuiUserID = _HirmaLuiUserID_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 3, 2, 1, 1),
    _HirmaLuiUserID_Type()
)
hirmaLuiUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hirmaLuiUserID.setStatus("mandatory")
_HirmaLuiUserName_Type = DisplayString
_HirmaLuiUserName_Object = MibTableColumn
hirmaLuiUserName = _HirmaLuiUserName_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 3, 2, 1, 2),
    _HirmaLuiUserName_Type()
)
hirmaLuiUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaLuiUserName.setStatus("mandatory")
_HirmaLuiUserPasswd_Type = DisplayString
_HirmaLuiUserPasswd_Object = MibTableColumn
hirmaLuiUserPasswd = _HirmaLuiUserPasswd_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 3, 2, 1, 3),
    _HirmaLuiUserPasswd_Type()
)
hirmaLuiUserPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaLuiUserPasswd.setStatus("mandatory")
_HirmaLuiUserCommunity_Type = DisplayString
_HirmaLuiUserCommunity_Object = MibTableColumn
hirmaLuiUserCommunity = _HirmaLuiUserCommunity_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 3, 2, 1, 4),
    _HirmaLuiUserCommunity_Type()
)
hirmaLuiUserCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hirmaLuiUserCommunity.setStatus("mandatory")

# Managed Objects groups


# Notification objects

bridgeHealth = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 2, 1, 0, 1)
)
bridgeHealth.setObjects(
    ("PRIVAT-MultiLAN-Switch-MIB", "hirmaBasBridgeHealthState")
)
if mibBuilder.loadTexts:
    bridgeHealth.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRIVAT-MultiLAN-Switch-MIB",
    **{"MacAddress": MacAddress,
       "private": private,
       "enterprises": enterprises,
       "hirschmann": hirschmann,
       "multiLANSwitch": multiLANSwitch,
       "bridge1": bridge1,
       "bridgeHealth": bridgeHealth,
       "bridgemgmt": bridgemgmt,
       "hirmaBasCapability": hirmaBasCapability,
       "hirmaBasBridgeTable": hirmaBasBridgeTable,
       "hirmaBasBridgeGroupCapacity": hirmaBasBridgeGroupCapacity,
       "hirmaBasBridgeGroupMap": hirmaBasBridgeGroupMap,
       "hirmaBasBridgeSoftVersion": hirmaBasBridgeSoftVersion,
       "hirmaBasBridgeHardVersion": hirmaBasBridgeHardVersion,
       "hirmaBasBridgeMibVersion": hirmaBasBridgeMibVersion,
       "hirmaBasBridgeSpanningTreeVersion": hirmaBasBridgeSpanningTreeVersion,
       "hirmaBasBridgeSwitches": hirmaBasBridgeSwitches,
       "hirmaBasBridgePwrSplyState": hirmaBasBridgePwrSplyState,
       "hirmaBasBridgeFanState": hirmaBasBridgeFanState,
       "hirmaBasBridgePwrAlarm": hirmaBasBridgePwrAlarm,
       "hirmaBasBridgeHealthAlarm": hirmaBasBridgeHealthAlarm,
       "hirmaBasBridgeSpanningTree": hirmaBasBridgeSpanningTree,
       "hirmaBasBridgeHealthState": hirmaBasBridgeHealthState,
       "hirmaBasBridgeHealthText": hirmaBasBridgeHealthText,
       "hirmaBasBridgeHealthData": hirmaBasBridgeHealthData,
       "hirmaBasBridgeCounterReset": hirmaBasBridgeCounterReset,
       "hirmaBasBridgeEventTable": hirmaBasBridgeEventTable,
       "hirmaBasBridgeEventEntry": hirmaBasBridgeEventEntry,
       "hirmaBasBridgeMessageID": hirmaBasBridgeMessageID,
       "hirmaBasBridgeMessageIfIndex": hirmaBasBridgeMessageIfIndex,
       "hirmaBasBridgeMessage": hirmaBasBridgeMessage,
       "hirmaBasBridgeMessageTime": hirmaBasBridgeMessageTime,
       "hirmaBasGroupTable": hirmaBasGroupTable,
       "hirmaBasGroupEntry": hirmaBasGroupEntry,
       "hirmaBasGroupID": hirmaBasGroupID,
       "hirmaBasGroupNumOfPorts": hirmaBasGroupNumOfPorts,
       "hirmaBasGroupPortMap": hirmaBasGroupPortMap,
       "hirmaBasGroupName": hirmaBasGroupName,
       "hirmaBasPortTable": hirmaBasPortTable,
       "hirmaBasPortEntry": hirmaBasPortEntry,
       "hirmaBasPortID": hirmaBasPortID,
       "hirmaBasPortGroupID": hirmaBasPortGroupID,
       "hirmaBasPortLanType": hirmaBasPortLanType,
       "hirmaBasPortType": hirmaBasPortType,
       "hirmaBasPortShortDelay": hirmaBasPortShortDelay,
       "hirmaBasPortLearning": hirmaBasPortLearning,
       "hirmaBasPortFiltering": hirmaBasPortFiltering,
       "hirmaBasPortRelay": hirmaBasPortRelay,
       "hirmaBasPortMode": hirmaBasPortMode,
       "hirmaBasPortCounterReset": hirmaBasPortCounterReset,
       "hirmaBasPortState": hirmaBasPortState,
       "hirmaSelfTestCapability": hirmaSelfTestCapability,
       "hirmaSelfTestBridgeReset": hirmaSelfTestBridgeReset,
       "hirmaSelfTestBridgeResetType": hirmaSelfTestBridgeResetType,
       "hirmaSelfTestBridgeSetDefaults": hirmaSelfTestBridgeSetDefaults,
       "hirmaSelfTestGroupTable": hirmaSelfTestGroupTable,
       "hirmaSelfTestGroupEntry": hirmaSelfTestGroupEntry,
       "hirmaSelfTestGroupID": hirmaSelfTestGroupID,
       "hirmaSelfTestGroupDisplayTest": hirmaSelfTestGroupDisplayTest,
       "hirmaSelfTestGroupSQETest": hirmaSelfTestGroupSQETest,
       "hirmaFilterCapability": hirmaFilterCapability,
       "hirmaFilterMaxNumOfFilters": hirmaFilterMaxNumOfFilters,
       "hirmaFilterTable": hirmaFilterTable,
       "hirmaFilterTableEntry": hirmaFilterTableEntry,
       "hirmaFilterID": hirmaFilterID,
       "hirmaFilterMode": hirmaFilterMode,
       "hirmaFilterDest": hirmaFilterDest,
       "hirmaFilterSrc": hirmaFilterSrc,
       "hirmaFilterType": hirmaFilterType,
       "hirmaFilterPortIn": hirmaFilterPortIn,
       "hirmaFilterPortOut": hirmaFilterPortOut,
       "hirmaAddrBTCapability": hirmaAddrBTCapability,
       "hirmaAddrBTAddr": hirmaAddrBTAddr,
       "hirmaAddrBTBlock": hirmaAddrBTBlock,
       "hirmaLoadCapability": hirmaLoadCapability,
       "hirmaFlashUpdate": hirmaFlashUpdate,
       "hirmaFlashUpdateIPAddr": hirmaFlashUpdateIPAddr,
       "hirmaFlashUpdateName": hirmaFlashUpdateName,
       "hirmaFlashUpdateAction": hirmaFlashUpdateAction,
       "hirmaLoadSaveConfig": hirmaLoadSaveConfig,
       "hirmaLoadSaveConIPAddr": hirmaLoadSaveConIPAddr,
       "hirmaLoadSaveConName": hirmaLoadSaveConName,
       "hirmaLoadSaveConAction": hirmaLoadSaveConAction,
       "hirmaMibhHandler": hirmaMibhHandler,
       "hirmaMibhCommTable": hirmaMibhCommTable,
       "hirmaMibhCommEntry": hirmaMibhCommEntry,
       "hirmaMibhCommIndex": hirmaMibhCommIndex,
       "hirmaMibhCommCommunity": hirmaMibhCommCommunity,
       "hirmaMibhCommAccess": hirmaMibhCommAccess,
       "hirmaMibhAccessTable": hirmaMibhAccessTable,
       "hirmaMibhAccessEntry": hirmaMibhAccessEntry,
       "hirmaMibhAccessCommIndex": hirmaMibhAccessCommIndex,
       "hirmaMibhAccessIPAddr": hirmaMibhAccessIPAddr,
       "hirmaMibhAccessPort": hirmaMibhAccessPort,
       "hirmaMibhAccessCommunity": hirmaMibhAccessCommunity,
       "hirmaMibhAccessAccess": hirmaMibhAccessAccess,
       "hirmaMibhAccessState": hirmaMibhAccessState,
       "hirmaMibhTrapTable": hirmaMibhTrapTable,
       "hirmaMibhTrapEntry": hirmaMibhTrapEntry,
       "hirmaMibhTrapCommIndex": hirmaMibhTrapCommIndex,
       "hirmaMibhTrapIPAddr": hirmaMibhTrapIPAddr,
       "hirmaMibhTrapPort": hirmaMibhTrapPort,
       "hirmaMibhTrapCommunity": hirmaMibhTrapCommunity,
       "hirmaMibhTrapState": hirmaMibhTrapState,
       "hirmaUserInterface": hirmaUserInterface,
       "hirmaLuiSystemTable": hirmaLuiSystemTable,
       "hirmaLuiLocalIPAddr": hirmaLuiLocalIPAddr,
       "hirmaLuiGatewayIPAddr": hirmaLuiGatewayIPAddr,
       "hirmaLuiNetMask": hirmaLuiNetMask,
       "hirmaLuiUserTable": hirmaLuiUserTable,
       "hirmaLuiUserEntry": hirmaLuiUserEntry,
       "hirmaLuiUserID": hirmaLuiUserID,
       "hirmaLuiUserName": hirmaLuiUserName,
       "hirmaLuiUserPasswd": hirmaLuiUserPasswd,
       "hirmaLuiUserCommunity": hirmaLuiUserCommunity}
)
