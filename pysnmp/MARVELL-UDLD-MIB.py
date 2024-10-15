# SNMP MIB module (MARVELL-UDLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MARVELL-UDLD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:28 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(rnd,
 rndNotifications) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd",
    "rndNotifications")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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


# MODULE-IDENTITY

rlUdld = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 218)
)
rlUdld.setRevisions(
        ("2012-08-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UdldString(SnmpAdminString, TextualConvention):
    status = "current"


class UdldPortBidirectionalState(Integer32, TextualConvention):
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
        *(("bidirectional", 5),
          ("detection", 3),
          ("idle", 2),
          ("shutdown", 1),
          ("undetermined", 4))
    )



class UdldNeighborCurrentState(Integer32, TextualConvention):
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
        *(("bidirectional", 4),
          ("disabled", 1),
          ("enabled", 2),
          ("undefined", 3))
    )



class UdldGlobalMode(Integer32, TextualConvention):
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
        *(("aggressive", 2),
          ("disabled", 3),
          ("normal", 1))
    )



class UdldPortMode(Integer32, TextualConvention):
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
        *(("aggressive", 2),
          ("default", 4),
          ("disabled", 3),
          ("normal", 1))
    )



# MIB Managed Objects in the order of their OIDs

_RlUdldPortTable_Object = MibTable
rlUdldPortTable = _RlUdldPortTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 218, 1)
)
if mibBuilder.loadTexts:
    rlUdldPortTable.setStatus("current")
_RlUdldPortEntry_Object = MibTableRow
rlUdldPortEntry = _RlUdldPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 218, 1, 1)
)
rlUdldPortEntry.setIndexNames(
    (0, "MARVELL-UDLD-MIB", "rlUdldPortIfIndex"),
)
if mibBuilder.loadTexts:
    rlUdldPortEntry.setStatus("current")
_RlUdldPortIfIndex_Type = InterfaceIndex
_RlUdldPortIfIndex_Object = MibTableColumn
rlUdldPortIfIndex = _RlUdldPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 218, 1, 1, 1),
    _RlUdldPortIfIndex_Type()
)
rlUdldPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlUdldPortIfIndex.setStatus("current")
_RlUdldPortAdminMode_Type = UdldPortMode
_RlUdldPortAdminMode_Object = MibTableColumn
rlUdldPortAdminMode = _RlUdldPortAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 218, 1, 1, 2),
    _RlUdldPortAdminMode_Type()
)
rlUdldPortAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlUdldPortAdminMode.setStatus("current")
_RlUdldPortOperMode_Type = UdldPortMode
_RlUdldPortOperMode_Object = MibTableColumn
rlUdldPortOperMode = _RlUdldPortOperMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 218, 1, 1, 3),
    _RlUdldPortOperMode_Type()
)
rlUdldPortOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlUdldPortOperMode.setStatus("current")
_RlUdldPortDefaultConfiguration_Type = TruthValue
_RlUdldPortDefaultConfiguration_Object = MibTableColumn
rlUdldPortDefaultConfiguration = _RlUdldPortDefaultConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 89, 218, 1, 1, 4),
    _RlUdldPortDefaultConfiguration_Type()
)
rlUdldPortDefaultConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlUdldPortDefaultConfiguration.setStatus("current")
_RlUdldBidirectionalState_Type = UdldPortBidirectionalState
_RlUdldBidirectionalState_Object = MibTableColumn
rlUdldBidirectionalState = _RlUdldBidirectionalState_Object(
    (1, 3, 6, 1, 4, 1, 89, 218, 1, 1, 5),
    _RlUdldBidirectionalState_Type()
)
rlUdldBidirectionalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlUdldBidirectionalState.setStatus("current")
_RlUdldNumberOfDetectedNeighbors_Type = Integer32
_RlUdldNumberOfDetectedNeighbors_Object = MibTableColumn
rlUdldNumberOfDetectedNeighbors = _RlUdldNumberOfDetectedNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 89, 218, 1, 1, 6),
    _RlUdldNumberOfDetectedNeighbors_Type()
)
rlUdldNumberOfDetectedNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlUdldNumberOfDetectedNeighbors.setStatus("current")
_RlUdldNeighborTable_Object = MibTable
rlUdldNeighborTable = _RlUdldNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 218, 2)
)
if mibBuilder.loadTexts:
    rlUdldNeighborTable.setStatus("current")
_RlUdldNeighborEntry_Object = MibTableRow
rlUdldNeighborEntry = _RlUdldNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 218, 2, 1)
)
rlUdldNeighborEntry.setIndexNames(
    (0, "MARVELL-UDLD-MIB", "rlUdldNeighborPortIfIndex"),
    (0, "MARVELL-UDLD-MIB", "rlUdldNeighborDeviceID"),
    (0, "MARVELL-UDLD-MIB", "rlUdldNeighborPortID"),
)
if mibBuilder.loadTexts:
    rlUdldNeighborEntry.setStatus("current")
_RlUdldNeighborPortIfIndex_Type = InterfaceIndex
_RlUdldNeighborPortIfIndex_Object = MibTableColumn
rlUdldNeighborPortIfIndex = _RlUdldNeighborPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 218, 2, 1, 1),
    _RlUdldNeighborPortIfIndex_Type()
)
rlUdldNeighborPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlUdldNeighborPortIfIndex.setStatus("current")
_RlUdldNeighborDeviceID_Type = UdldString
_RlUdldNeighborDeviceID_Object = MibTableColumn
rlUdldNeighborDeviceID = _RlUdldNeighborDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 89, 218, 2, 1, 2),
    _RlUdldNeighborDeviceID_Type()
)
rlUdldNeighborDeviceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlUdldNeighborDeviceID.setStatus("current")
_RlUdldNeighborPortID_Type = UdldString
_RlUdldNeighborPortID_Object = MibTableColumn
rlUdldNeighborPortID = _RlUdldNeighborPortID_Object(
    (1, 3, 6, 1, 4, 1, 89, 218, 2, 1, 3),
    _RlUdldNeighborPortID_Type()
)
rlUdldNeighborPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlUdldNeighborPortID.setStatus("current")
_RlUdldNeighborDeviceMACAddress_Type = MacAddress
_RlUdldNeighborDeviceMACAddress_Object = MibTableColumn
rlUdldNeighborDeviceMACAddress = _RlUdldNeighborDeviceMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 218, 2, 1, 4),
    _RlUdldNeighborDeviceMACAddress_Type()
)
rlUdldNeighborDeviceMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlUdldNeighborDeviceMACAddress.setStatus("current")
_RlUdldNeighborDeviceName_Type = UdldString
_RlUdldNeighborDeviceName_Object = MibTableColumn
rlUdldNeighborDeviceName = _RlUdldNeighborDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 89, 218, 2, 1, 5),
    _RlUdldNeighborDeviceName_Type()
)
rlUdldNeighborDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlUdldNeighborDeviceName.setStatus("current")
_RlUdldNeighborMessageTime_Type = Integer32
_RlUdldNeighborMessageTime_Object = MibTableColumn
rlUdldNeighborMessageTime = _RlUdldNeighborMessageTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 218, 2, 1, 6),
    _RlUdldNeighborMessageTime_Type()
)
rlUdldNeighborMessageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlUdldNeighborMessageTime.setStatus("current")
_RlUdldNeighborLeftLifeTime_Type = Integer32
_RlUdldNeighborLeftLifeTime_Object = MibTableColumn
rlUdldNeighborLeftLifeTime = _RlUdldNeighborLeftLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 218, 2, 1, 7),
    _RlUdldNeighborLeftLifeTime_Type()
)
rlUdldNeighborLeftLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlUdldNeighborLeftLifeTime.setStatus("current")
_RlUdldNeighborCurrentState_Type = UdldNeighborCurrentState
_RlUdldNeighborCurrentState_Object = MibTableColumn
rlUdldNeighborCurrentState = _RlUdldNeighborCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 89, 218, 2, 1, 8),
    _RlUdldNeighborCurrentState_Type()
)
rlUdldNeighborCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlUdldNeighborCurrentState.setStatus("current")
_RlUdldGlobalUDLDMode_Type = UdldGlobalMode
_RlUdldGlobalUDLDMode_Object = MibScalar
rlUdldGlobalUDLDMode = _RlUdldGlobalUDLDMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 218, 3),
    _RlUdldGlobalUDLDMode_Type()
)
rlUdldGlobalUDLDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlUdldGlobalUDLDMode.setStatus("current")
_RlUdldGlobalMessageTime_Type = Integer32
_RlUdldGlobalMessageTime_Object = MibScalar
rlUdldGlobalMessageTime = _RlUdldGlobalMessageTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 218, 4),
    _RlUdldGlobalMessageTime_Type()
)
rlUdldGlobalMessageTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlUdldGlobalMessageTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MARVELL-UDLD-MIB",
    **{"UdldString": UdldString,
       "UdldPortBidirectionalState": UdldPortBidirectionalState,
       "UdldNeighborCurrentState": UdldNeighborCurrentState,
       "UdldGlobalMode": UdldGlobalMode,
       "UdldPortMode": UdldPortMode,
       "rlUdld": rlUdld,
       "rlUdldPortTable": rlUdldPortTable,
       "rlUdldPortEntry": rlUdldPortEntry,
       "rlUdldPortIfIndex": rlUdldPortIfIndex,
       "rlUdldPortAdminMode": rlUdldPortAdminMode,
       "rlUdldPortOperMode": rlUdldPortOperMode,
       "rlUdldPortDefaultConfiguration": rlUdldPortDefaultConfiguration,
       "rlUdldBidirectionalState": rlUdldBidirectionalState,
       "rlUdldNumberOfDetectedNeighbors": rlUdldNumberOfDetectedNeighbors,
       "rlUdldNeighborTable": rlUdldNeighborTable,
       "rlUdldNeighborEntry": rlUdldNeighborEntry,
       "rlUdldNeighborPortIfIndex": rlUdldNeighborPortIfIndex,
       "rlUdldNeighborDeviceID": rlUdldNeighborDeviceID,
       "rlUdldNeighborPortID": rlUdldNeighborPortID,
       "rlUdldNeighborDeviceMACAddress": rlUdldNeighborDeviceMACAddress,
       "rlUdldNeighborDeviceName": rlUdldNeighborDeviceName,
       "rlUdldNeighborMessageTime": rlUdldNeighborMessageTime,
       "rlUdldNeighborLeftLifeTime": rlUdldNeighborLeftLifeTime,
       "rlUdldNeighborCurrentState": rlUdldNeighborCurrentState,
       "rlUdldGlobalUDLDMode": rlUdldGlobalUDLDMode,
       "rlUdldGlobalMessageTime": rlUdldGlobalMessageTime}
)
