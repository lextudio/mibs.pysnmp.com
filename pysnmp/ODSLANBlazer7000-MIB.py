# SNMP MIB module (ODSLANBlazer7000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ODSLANBlazer7000-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:46 2024
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



class EventValueType(Integer32):
    """Custom type EventValueType based on Integer32"""
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
        *(("integer", 2),
          ("ipAddress", 6),
          ("longInteger", 3),
          ("macAddress", 7),
          ("none", 1),
          ("octets", 5),
          ("string", 4),
          ("timeTicks", 8))
    )





class ResourceType(Integer32):
    """Custom type ResourceType based on Integer32"""
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
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("aft", 11),
          ("alarm", 16),
          ("bridge", 9),
          ("display", 7),
          ("event", 15),
          ("fan", 3),
          ("inboundGroupTable", 12),
          ("interface", 5),
          ("module", 2),
          ("outboundGroupTable", 13),
          ("powerSupply", 6),
          ("switchPort", 8),
          ("system", 1),
          ("temperatureSensor", 4),
          ("threeComMappingTable", 14),
          ("vlan", 10))
    )





class ResourceId(ObjectIdentifier):
    """Custom type ResourceId based on ObjectIdentifier"""




class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )





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




class EventCategory(Integer32):
    """Custom type EventCategory based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("authentication", 11),
          ("bridgeNewRoot", 18),
          ("bridgeTopChange", 19),
          ("coldstart", 2),
          ("configuration", 9),
          ("deletedResource", 7),
          ("fallingThreshold", 14),
          ("fanStatus", 15),
          ("linkDown", 5),
          ("linkUp", 4),
          ("newResource", 6),
          ("powerStatus", 16),
          ("risingThreshold", 13),
          ("scheduled", 10),
          ("status", 17),
          ("switchFabricStatus", 20),
          ("system", 12),
          ("tempStatus", 8),
          ("userDefined", 1),
          ("warmstart", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ods_ObjectIdentity = ObjectIdentity
ods = _Ods_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50)
)
_OdsTPS_ObjectIdentity = ObjectIdentity
odsTPS = _OdsTPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8)
)
_OdsLANBlazer_ObjectIdentity = ObjectIdentity
odsLANBlazer = _OdsLANBlazer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1)
)
_OdsLANBlazerMibs_ObjectIdentity = ObjectIdentity
odsLANBlazerMibs = _OdsLANBlazerMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2)
)
_OdsLANBlazer7000Mib_ObjectIdentity = ObjectIdentity
odsLANBlazer7000Mib = _OdsLANBlazer7000Mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1)
)
_LanBlazer7000Agent_ObjectIdentity = ObjectIdentity
lanBlazer7000Agent = _LanBlazer7000Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 1)
)
_LanBlazer7000AgentGen_ObjectIdentity = ObjectIdentity
lanBlazer7000AgentGen = _LanBlazer7000AgentGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 1, 1)
)


class _LanBlazer7000AgentMIBVersion_Type(DisplayString):
    """Custom type lanBlazer7000AgentMIBVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LanBlazer7000AgentMIBVersion_Type.__name__ = "DisplayString"
_LanBlazer7000AgentMIBVersion_Object = MibScalar
lanBlazer7000AgentMIBVersion = _LanBlazer7000AgentMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 1, 1, 1),
    _LanBlazer7000AgentMIBVersion_Type()
)
lanBlazer7000AgentMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000AgentMIBVersion.setStatus("mandatory")
_LanBlazer7000AgentMgrIndex_Type = Integer32
_LanBlazer7000AgentMgrIndex_Object = MibScalar
lanBlazer7000AgentMgrIndex = _LanBlazer7000AgentMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 1, 1, 2),
    _LanBlazer7000AgentMgrIndex_Type()
)
lanBlazer7000AgentMgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000AgentMgrIndex.setStatus("mandatory")
_LanBlazer7000AgentCommunity_ObjectIdentity = ObjectIdentity
lanBlazer7000AgentCommunity = _LanBlazer7000AgentCommunity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 1, 2)
)
_LanBlazer7000CommunityTable_Object = MibTable
lanBlazer7000CommunityTable = _LanBlazer7000CommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000CommunityTable.setStatus("mandatory")
_LanBlazer7000CommunityEntry_Object = MibTableRow
lanBlazer7000CommunityEntry = _LanBlazer7000CommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 1, 2, 1, 1)
)
lanBlazer7000CommunityEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000CommunityIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000CommunityEntry.setStatus("mandatory")
_LanBlazer7000CommunityIndex_Type = Integer32
_LanBlazer7000CommunityIndex_Object = MibTableColumn
lanBlazer7000CommunityIndex = _LanBlazer7000CommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 1, 2, 1, 1, 1),
    _LanBlazer7000CommunityIndex_Type()
)
lanBlazer7000CommunityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000CommunityIndex.setStatus("mandatory")


class _LanBlazer7000CommunityString_Type(DisplayString):
    """Custom type lanBlazer7000CommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LanBlazer7000CommunityString_Type.__name__ = "DisplayString"
_LanBlazer7000CommunityString_Object = MibTableColumn
lanBlazer7000CommunityString = _LanBlazer7000CommunityString_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 1, 2, 1, 1, 2),
    _LanBlazer7000CommunityString_Type()
)
lanBlazer7000CommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000CommunityString.setStatus("mandatory")


class _LanBlazer7000CommunityAddressType_Type(Integer32):
    """Custom type lanBlazer7000CommunityAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("ipv4", 2))
    )


_LanBlazer7000CommunityAddressType_Type.__name__ = "Integer32"
_LanBlazer7000CommunityAddressType_Object = MibTableColumn
lanBlazer7000CommunityAddressType = _LanBlazer7000CommunityAddressType_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 1, 2, 1, 1, 3),
    _LanBlazer7000CommunityAddressType_Type()
)
lanBlazer7000CommunityAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000CommunityAddressType.setStatus("mandatory")
_LanBlazer7000CommunityAddress_Type = IpAddress
_LanBlazer7000CommunityAddress_Object = MibTableColumn
lanBlazer7000CommunityAddress = _LanBlazer7000CommunityAddress_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 1, 2, 1, 1, 4),
    _LanBlazer7000CommunityAddress_Type()
)
lanBlazer7000CommunityAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000CommunityAddress.setStatus("mandatory")


class _LanBlazer7000CommunityAccess_Type(Integer32):
    """Custom type lanBlazer7000CommunityAccess based on Integer32"""
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
        *(("moreSpecific", 4),
          ("none", 1),
          ("readOnly", 2),
          ("readWrite", 3))
    )


_LanBlazer7000CommunityAccess_Type.__name__ = "Integer32"
_LanBlazer7000CommunityAccess_Object = MibTableColumn
lanBlazer7000CommunityAccess = _LanBlazer7000CommunityAccess_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 1, 2, 1, 1, 5),
    _LanBlazer7000CommunityAccess_Type()
)
lanBlazer7000CommunityAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000CommunityAccess.setStatus("mandatory")


class _LanBlazer7000CommunityTrapReceiver_Type(Integer32):
    """Custom type lanBlazer7000CommunityTrapReceiver based on Integer32"""
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


_LanBlazer7000CommunityTrapReceiver_Type.__name__ = "Integer32"
_LanBlazer7000CommunityTrapReceiver_Object = MibTableColumn
lanBlazer7000CommunityTrapReceiver = _LanBlazer7000CommunityTrapReceiver_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 1, 2, 1, 1, 6),
    _LanBlazer7000CommunityTrapReceiver_Type()
)
lanBlazer7000CommunityTrapReceiver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000CommunityTrapReceiver.setStatus("mandatory")


class _LanBlazer7000CommunitySecurityLevel_Type(Integer32):
    """Custom type lanBlazer7000CommunitySecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("administrator", 2),
          ("normal", 1))
    )


_LanBlazer7000CommunitySecurityLevel_Type.__name__ = "Integer32"
_LanBlazer7000CommunitySecurityLevel_Object = MibTableColumn
lanBlazer7000CommunitySecurityLevel = _LanBlazer7000CommunitySecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 1, 2, 1, 1, 7),
    _LanBlazer7000CommunitySecurityLevel_Type()
)
lanBlazer7000CommunitySecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000CommunitySecurityLevel.setStatus("mandatory")
_LanBlazer7000CommunityStatus_Type = RowStatus
_LanBlazer7000CommunityStatus_Object = MibTableColumn
lanBlazer7000CommunityStatus = _LanBlazer7000CommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 1, 2, 1, 1, 8),
    _LanBlazer7000CommunityStatus_Type()
)
lanBlazer7000CommunityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000CommunityStatus.setStatus("mandatory")
_LanBlazer7000AgentWeb_ObjectIdentity = ObjectIdentity
lanBlazer7000AgentWeb = _LanBlazer7000AgentWeb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 1, 3)
)


class _LanBlazer7000AgentWebServerURL_Type(DisplayString):
    """Custom type lanBlazer7000AgentWebServerURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_LanBlazer7000AgentWebServerURL_Type.__name__ = "DisplayString"
_LanBlazer7000AgentWebServerURL_Object = MibScalar
lanBlazer7000AgentWebServerURL = _LanBlazer7000AgentWebServerURL_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 1, 3, 1),
    _LanBlazer7000AgentWebServerURL_Type()
)
lanBlazer7000AgentWebServerURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000AgentWebServerURL.setStatus("mandatory")


class _LanBlazer7000AgentWebServerHelpDirectory_Type(DisplayString):
    """Custom type lanBlazer7000AgentWebServerHelpDirectory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_LanBlazer7000AgentWebServerHelpDirectory_Type.__name__ = "DisplayString"
_LanBlazer7000AgentWebServerHelpDirectory_Object = MibScalar
lanBlazer7000AgentWebServerHelpDirectory = _LanBlazer7000AgentWebServerHelpDirectory_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 1, 3, 2),
    _LanBlazer7000AgentWebServerHelpDirectory_Type()
)
lanBlazer7000AgentWebServerHelpDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000AgentWebServerHelpDirectory.setStatus("mandatory")
_LanBlazer7000Chassis_ObjectIdentity = ObjectIdentity
lanBlazer7000Chassis = _LanBlazer7000Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3)
)
_LanBlazer7000ChassisGen_ObjectIdentity = ObjectIdentity
lanBlazer7000ChassisGen = _LanBlazer7000ChassisGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 1)
)


class _LanBlazer7000ChassisType_Type(Integer32):
    """Custom type lanBlazer7000ChassisType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("p220", 2),
          ("p550", 1))
    )


_LanBlazer7000ChassisType_Type.__name__ = "Integer32"
_LanBlazer7000ChassisType_Object = MibScalar
lanBlazer7000ChassisType = _LanBlazer7000ChassisType_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 1, 1),
    _LanBlazer7000ChassisType_Type()
)
lanBlazer7000ChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000ChassisType.setStatus("mandatory")
_LanBlazer7000ChassisSlots_Type = Integer32
_LanBlazer7000ChassisSlots_Object = MibScalar
lanBlazer7000ChassisSlots = _LanBlazer7000ChassisSlots_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 1, 2),
    _LanBlazer7000ChassisSlots_Type()
)
lanBlazer7000ChassisSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000ChassisSlots.setStatus("mandatory")
_LanBlazer7000Inventory_ObjectIdentity = ObjectIdentity
lanBlazer7000Inventory = _LanBlazer7000Inventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 2)
)
_LanBlazer7000InventoryTable_Object = MibTable
lanBlazer7000InventoryTable = _LanBlazer7000InventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000InventoryTable.setStatus("mandatory")
_LanBlazer7000InventoryEntry_Object = MibTableRow
lanBlazer7000InventoryEntry = _LanBlazer7000InventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 2, 1, 1)
)
lanBlazer7000InventoryEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000InventoryResourceType"),
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000InventoryResourceIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000InventoryEntry.setStatus("mandatory")
_LanBlazer7000InventoryResourceType_Type = ResourceType
_LanBlazer7000InventoryResourceType_Object = MibTableColumn
lanBlazer7000InventoryResourceType = _LanBlazer7000InventoryResourceType_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 2, 1, 1, 1),
    _LanBlazer7000InventoryResourceType_Type()
)
lanBlazer7000InventoryResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000InventoryResourceType.setStatus("mandatory")
_LanBlazer7000InventoryResourceIndex_Type = ResourceId
_LanBlazer7000InventoryResourceIndex_Object = MibTableColumn
lanBlazer7000InventoryResourceIndex = _LanBlazer7000InventoryResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 2, 1, 1, 2),
    _LanBlazer7000InventoryResourceIndex_Type()
)
lanBlazer7000InventoryResourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000InventoryResourceIndex.setStatus("mandatory")


class _LanBlazer7000InventoryModelNumber_Type(DisplayString):
    """Custom type lanBlazer7000InventoryModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LanBlazer7000InventoryModelNumber_Type.__name__ = "DisplayString"
_LanBlazer7000InventoryModelNumber_Object = MibTableColumn
lanBlazer7000InventoryModelNumber = _LanBlazer7000InventoryModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 2, 1, 1, 3),
    _LanBlazer7000InventoryModelNumber_Type()
)
lanBlazer7000InventoryModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000InventoryModelNumber.setStatus("mandatory")


class _LanBlazer7000InventorySerialNumber_Type(DisplayString):
    """Custom type lanBlazer7000InventorySerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LanBlazer7000InventorySerialNumber_Type.__name__ = "DisplayString"
_LanBlazer7000InventorySerialNumber_Object = MibTableColumn
lanBlazer7000InventorySerialNumber = _LanBlazer7000InventorySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 2, 1, 1, 4),
    _LanBlazer7000InventorySerialNumber_Type()
)
lanBlazer7000InventorySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000InventorySerialNumber.setStatus("mandatory")


class _LanBlazer7000InventoryVersion_Type(DisplayString):
    """Custom type lanBlazer7000InventoryVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LanBlazer7000InventoryVersion_Type.__name__ = "DisplayString"
_LanBlazer7000InventoryVersion_Object = MibTableColumn
lanBlazer7000InventoryVersion = _LanBlazer7000InventoryVersion_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 2, 1, 1, 5),
    _LanBlazer7000InventoryVersion_Type()
)
lanBlazer7000InventoryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000InventoryVersion.setStatus("mandatory")


class _LanBlazer7000InventoryManufactureInfo_Type(DisplayString):
    """Custom type lanBlazer7000InventoryManufactureInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_LanBlazer7000InventoryManufactureInfo_Type.__name__ = "DisplayString"
_LanBlazer7000InventoryManufactureInfo_Object = MibTableColumn
lanBlazer7000InventoryManufactureInfo = _LanBlazer7000InventoryManufactureInfo_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 2, 1, 1, 6),
    _LanBlazer7000InventoryManufactureInfo_Type()
)
lanBlazer7000InventoryManufactureInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000InventoryManufactureInfo.setStatus("mandatory")


class _LanBlazer7000InventoryScratchPad_Type(DisplayString):
    """Custom type lanBlazer7000InventoryScratchPad based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_LanBlazer7000InventoryScratchPad_Type.__name__ = "DisplayString"
_LanBlazer7000InventoryScratchPad_Object = MibTableColumn
lanBlazer7000InventoryScratchPad = _LanBlazer7000InventoryScratchPad_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 2, 1, 1, 7),
    _LanBlazer7000InventoryScratchPad_Type()
)
lanBlazer7000InventoryScratchPad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000InventoryScratchPad.setStatus("mandatory")
_LanBlazer7000PowerSystems_ObjectIdentity = ObjectIdentity
lanBlazer7000PowerSystems = _LanBlazer7000PowerSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 3)
)
_LanBlazer7000PowerSupplies_ObjectIdentity = ObjectIdentity
lanBlazer7000PowerSupplies = _LanBlazer7000PowerSupplies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 3, 1)
)
_LanBlazer7000PowerSupplyTable_Object = MibTable
lanBlazer7000PowerSupplyTable = _LanBlazer7000PowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000PowerSupplyTable.setStatus("mandatory")
_LanBlazer7000PowerSupplyEntry_Object = MibTableRow
lanBlazer7000PowerSupplyEntry = _LanBlazer7000PowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 3, 1, 1, 1)
)
lanBlazer7000PowerSupplyEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000PowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000PowerSupplyEntry.setStatus("mandatory")
_LanBlazer7000PowerSupplyIndex_Type = ResourceId
_LanBlazer7000PowerSupplyIndex_Object = MibTableColumn
lanBlazer7000PowerSupplyIndex = _LanBlazer7000PowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 3, 1, 1, 1, 1),
    _LanBlazer7000PowerSupplyIndex_Type()
)
lanBlazer7000PowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000PowerSupplyIndex.setStatus("mandatory")


class _LanBlazer7000PowerSupplyType_Type(Integer32):
    """Custom type lanBlazer7000PowerSupplyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("psA", 2),
          ("psB", 3),
          ("unknown", 1))
    )


_LanBlazer7000PowerSupplyType_Type.__name__ = "Integer32"
_LanBlazer7000PowerSupplyType_Object = MibTableColumn
lanBlazer7000PowerSupplyType = _LanBlazer7000PowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 3, 1, 1, 1, 2),
    _LanBlazer7000PowerSupplyType_Type()
)
lanBlazer7000PowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000PowerSupplyType.setStatus("mandatory")


class _LanBlazer7000PowerSupplyStatus_Type(Integer32):
    """Custom type lanBlazer7000PowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 2),
          ("okay", 1),
          ("unknown", 3))
    )


_LanBlazer7000PowerSupplyStatus_Type.__name__ = "Integer32"
_LanBlazer7000PowerSupplyStatus_Object = MibTableColumn
lanBlazer7000PowerSupplyStatus = _LanBlazer7000PowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 3, 1, 1, 1, 3),
    _LanBlazer7000PowerSupplyStatus_Type()
)
lanBlazer7000PowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000PowerSupplyStatus.setStatus("mandatory")


class _LanBlazer7000PowerSupplyInputStatus_Type(Integer32):
    """Custom type lanBlazer7000PowerSupplyInputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 2),
          ("okay", 1),
          ("unknown", 3))
    )


_LanBlazer7000PowerSupplyInputStatus_Type.__name__ = "Integer32"
_LanBlazer7000PowerSupplyInputStatus_Object = MibTableColumn
lanBlazer7000PowerSupplyInputStatus = _LanBlazer7000PowerSupplyInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 3, 1, 1, 1, 4),
    _LanBlazer7000PowerSupplyInputStatus_Type()
)
lanBlazer7000PowerSupplyInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000PowerSupplyInputStatus.setStatus("mandatory")


class _LanBlazer7000PowerSupplyOutputStatus_Type(Integer32):
    """Custom type lanBlazer7000PowerSupplyOutputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 2),
          ("okay", 1),
          ("unknown", 3))
    )


_LanBlazer7000PowerSupplyOutputStatus_Type.__name__ = "Integer32"
_LanBlazer7000PowerSupplyOutputStatus_Object = MibTableColumn
lanBlazer7000PowerSupplyOutputStatus = _LanBlazer7000PowerSupplyOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 3, 1, 1, 1, 5),
    _LanBlazer7000PowerSupplyOutputStatus_Type()
)
lanBlazer7000PowerSupplyOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000PowerSupplyOutputStatus.setStatus("mandatory")
_LanBlazer7000PowerSupplyOutputCapacity_Type = Integer32
_LanBlazer7000PowerSupplyOutputCapacity_Object = MibTableColumn
lanBlazer7000PowerSupplyOutputCapacity = _LanBlazer7000PowerSupplyOutputCapacity_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 3, 1, 1, 1, 6),
    _LanBlazer7000PowerSupplyOutputCapacity_Type()
)
lanBlazer7000PowerSupplyOutputCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000PowerSupplyOutputCapacity.setStatus("mandatory")
_LanBlazer7000PowerMgmtGen_ObjectIdentity = ObjectIdentity
lanBlazer7000PowerMgmtGen = _LanBlazer7000PowerMgmtGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 3, 2)
)
_LanBlazer7000PowerCapacity_Type = Integer32
_LanBlazer7000PowerCapacity_Object = MibScalar
lanBlazer7000PowerCapacity = _LanBlazer7000PowerCapacity_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 3, 2, 1),
    _LanBlazer7000PowerCapacity_Type()
)
lanBlazer7000PowerCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000PowerCapacity.setStatus("mandatory")
_LanBlazer7000PowerUsed_Type = Integer32
_LanBlazer7000PowerUsed_Object = MibScalar
lanBlazer7000PowerUsed = _LanBlazer7000PowerUsed_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 3, 2, 2),
    _LanBlazer7000PowerUsed_Type()
)
lanBlazer7000PowerUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000PowerUsed.setStatus("mandatory")
_LanBlazer7000PowerMgmtCtl_ObjectIdentity = ObjectIdentity
lanBlazer7000PowerMgmtCtl = _LanBlazer7000PowerMgmtCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 3, 3)
)
_LanBlazer7000PowerControlTable_Object = MibTable
lanBlazer7000PowerControlTable = _LanBlazer7000PowerControlTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000PowerControlTable.setStatus("mandatory")
_LanBlazer7000PowerControlEntry_Object = MibTableRow
lanBlazer7000PowerControlEntry = _LanBlazer7000PowerControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 3, 3, 1, 1)
)
lanBlazer7000PowerControlEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000ModuleIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000PowerControlEntry.setStatus("mandatory")
_LanBlazer7000PowerControlUsed_Type = Integer32
_LanBlazer7000PowerControlUsed_Object = MibTableColumn
lanBlazer7000PowerControlUsed = _LanBlazer7000PowerControlUsed_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 3, 3, 1, 1, 1),
    _LanBlazer7000PowerControlUsed_Type()
)
lanBlazer7000PowerControlUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000PowerControlUsed.setStatus("mandatory")


class _LanBlazer7000PowerControlPriority_Type(Integer32):
    """Custom type lanBlazer7000PowerControlPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 3),
          ("normal", 2))
    )


_LanBlazer7000PowerControlPriority_Type.__name__ = "Integer32"
_LanBlazer7000PowerControlPriority_Object = MibTableColumn
lanBlazer7000PowerControlPriority = _LanBlazer7000PowerControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 3, 3, 1, 1, 2),
    _LanBlazer7000PowerControlPriority_Type()
)
lanBlazer7000PowerControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000PowerControlPriority.setStatus("mandatory")


class _LanBlazer7000PowerControlMode_Type(Integer32):
    """Custom type lanBlazer7000PowerControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("poweredDown", 3))
    )


_LanBlazer7000PowerControlMode_Type.__name__ = "Integer32"
_LanBlazer7000PowerControlMode_Object = MibTableColumn
lanBlazer7000PowerControlMode = _LanBlazer7000PowerControlMode_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 3, 3, 1, 1, 3),
    _LanBlazer7000PowerControlMode_Type()
)
lanBlazer7000PowerControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000PowerControlMode.setStatus("mandatory")
_LanBlazer7000Temperature_ObjectIdentity = ObjectIdentity
lanBlazer7000Temperature = _LanBlazer7000Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 4)
)
_LanBlazer7000TempTable_Object = MibTable
lanBlazer7000TempTable = _LanBlazer7000TempTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000TempTable.setStatus("mandatory")
_LanBlazer7000TempEntry_Object = MibTableRow
lanBlazer7000TempEntry = _LanBlazer7000TempEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 4, 1, 1)
)
lanBlazer7000TempEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000TempIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000TempEntry.setStatus("mandatory")
_LanBlazer7000TempIndex_Type = ResourceId
_LanBlazer7000TempIndex_Object = MibTableColumn
lanBlazer7000TempIndex = _LanBlazer7000TempIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 4, 1, 1, 1),
    _LanBlazer7000TempIndex_Type()
)
lanBlazer7000TempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000TempIndex.setStatus("mandatory")
_LanBlazer7000TempValue_Type = Integer32
_LanBlazer7000TempValue_Object = MibTableColumn
lanBlazer7000TempValue = _LanBlazer7000TempValue_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 4, 1, 1, 2),
    _LanBlazer7000TempValue_Type()
)
lanBlazer7000TempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000TempValue.setStatus("mandatory")
_LanBlazer7000TempUpperLimit_Type = Integer32
_LanBlazer7000TempUpperLimit_Object = MibTableColumn
lanBlazer7000TempUpperLimit = _LanBlazer7000TempUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 4, 1, 1, 3),
    _LanBlazer7000TempUpperLimit_Type()
)
lanBlazer7000TempUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000TempUpperLimit.setStatus("mandatory")
_LanBlazer7000TempUpperWarning_Type = Integer32
_LanBlazer7000TempUpperWarning_Object = MibTableColumn
lanBlazer7000TempUpperWarning = _LanBlazer7000TempUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 4, 1, 1, 4),
    _LanBlazer7000TempUpperWarning_Type()
)
lanBlazer7000TempUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000TempUpperWarning.setStatus("mandatory")
_LanBlazer7000TempLowerWarning_Type = Integer32
_LanBlazer7000TempLowerWarning_Object = MibTableColumn
lanBlazer7000TempLowerWarning = _LanBlazer7000TempLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 4, 1, 1, 5),
    _LanBlazer7000TempLowerWarning_Type()
)
lanBlazer7000TempLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000TempLowerWarning.setStatus("mandatory")
_LanBlazer7000TempLowerLimit_Type = Integer32
_LanBlazer7000TempLowerLimit_Object = MibTableColumn
lanBlazer7000TempLowerLimit = _LanBlazer7000TempLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 4, 1, 1, 6),
    _LanBlazer7000TempLowerLimit_Type()
)
lanBlazer7000TempLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000TempLowerLimit.setStatus("mandatory")
_LanBlazer7000Modules_ObjectIdentity = ObjectIdentity
lanBlazer7000Modules = _LanBlazer7000Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 5)
)
_LanBlazer7000ModuleTable_Object = MibTable
lanBlazer7000ModuleTable = _LanBlazer7000ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000ModuleTable.setStatus("mandatory")
_LanBlazer7000ModuleEntry_Object = MibTableRow
lanBlazer7000ModuleEntry = _LanBlazer7000ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 5, 1, 1)
)
lanBlazer7000ModuleEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000ModuleIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000ModuleEntry.setStatus("mandatory")
_LanBlazer7000ModuleIndex_Type = ResourceId
_LanBlazer7000ModuleIndex_Object = MibTableColumn
lanBlazer7000ModuleIndex = _LanBlazer7000ModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 5, 1, 1, 1),
    _LanBlazer7000ModuleIndex_Type()
)
lanBlazer7000ModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000ModuleIndex.setStatus("mandatory")


class _LanBlazer7000ModuleName_Type(DisplayString):
    """Custom type lanBlazer7000ModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_LanBlazer7000ModuleName_Type.__name__ = "DisplayString"
_LanBlazer7000ModuleName_Object = MibTableColumn
lanBlazer7000ModuleName = _LanBlazer7000ModuleName_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 5, 1, 1, 2),
    _LanBlazer7000ModuleName_Type()
)
lanBlazer7000ModuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000ModuleName.setStatus("mandatory")


class _LanBlazer7000ModuleType_Type(Integer32):
    """Custom type lanBlazer7000ModuleType based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("m2200-SUP", 15),
          ("m2201-1000", 8),
          ("m2202-100FX", 10),
          ("m2204-100TX", 16),
          ("m2206-1000", 3),
          ("m2224-100TX", 17),
          ("m5500-SUP", 6),
          ("m5500R-SUP", 13),
          ("m5502-1000", 2),
          ("m5502R-1000", 14),
          ("m5504-1000", 7),
          ("m5510-100FX", 5),
          ("m5510R-100FX", 11),
          ("m5512R-100TX", 12),
          ("m5520-100TX-I", 9),
          ("m5520-100TX-QS", 4),
          ("unknown", 1))
    )


_LanBlazer7000ModuleType_Type.__name__ = "Integer32"
_LanBlazer7000ModuleType_Object = MibTableColumn
lanBlazer7000ModuleType = _LanBlazer7000ModuleType_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 5, 1, 1, 3),
    _LanBlazer7000ModuleType_Type()
)
lanBlazer7000ModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000ModuleType.setStatus("mandatory")


class _LanBlazer7000ModuleBaseType_Type(Integer32):
    """Custom type lanBlazer7000ModuleBaseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fastEthernet", 2),
          ("gigabit", 1),
          ("supervisor", 3))
    )


_LanBlazer7000ModuleBaseType_Type.__name__ = "Integer32"
_LanBlazer7000ModuleBaseType_Object = MibTableColumn
lanBlazer7000ModuleBaseType = _LanBlazer7000ModuleBaseType_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 5, 1, 1, 4),
    _LanBlazer7000ModuleBaseType_Type()
)
lanBlazer7000ModuleBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000ModuleBaseType.setStatus("mandatory")
_LanBlazer7000ModuleSlotWidth_Type = Integer32
_LanBlazer7000ModuleSlotWidth_Object = MibTableColumn
lanBlazer7000ModuleSlotWidth = _LanBlazer7000ModuleSlotWidth_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 5, 1, 1, 5),
    _LanBlazer7000ModuleSlotWidth_Type()
)
lanBlazer7000ModuleSlotWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000ModuleSlotWidth.setStatus("mandatory")
_LanBlazer7000ModuleSlotOffset_Type = Integer32
_LanBlazer7000ModuleSlotOffset_Object = MibTableColumn
lanBlazer7000ModuleSlotOffset = _LanBlazer7000ModuleSlotOffset_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 5, 1, 1, 6),
    _LanBlazer7000ModuleSlotOffset_Type()
)
lanBlazer7000ModuleSlotOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000ModuleSlotOffset.setStatus("mandatory")
_LanBlazer7000ModulePorts_Type = Integer32
_LanBlazer7000ModulePorts_Object = MibTableColumn
lanBlazer7000ModulePorts = _LanBlazer7000ModulePorts_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 5, 1, 1, 7),
    _LanBlazer7000ModulePorts_Type()
)
lanBlazer7000ModulePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000ModulePorts.setStatus("mandatory")
_LanBlazer7000Ports_ObjectIdentity = ObjectIdentity
lanBlazer7000Ports = _LanBlazer7000Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6)
)
_LanBlazer7000PortMgt_ObjectIdentity = ObjectIdentity
lanBlazer7000PortMgt = _LanBlazer7000PortMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 1)
)
_LanBlazer7000PortTable_Object = MibTable
lanBlazer7000PortTable = _LanBlazer7000PortTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 1, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000PortTable.setStatus("mandatory")
_LanBlazer7000PortEntry_Object = MibTableRow
lanBlazer7000PortEntry = _LanBlazer7000PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 1, 1, 1)
)
lanBlazer7000PortEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000PortIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000PortEntry.setStatus("mandatory")
_LanBlazer7000PortIndex_Type = ResourceId
_LanBlazer7000PortIndex_Object = MibTableColumn
lanBlazer7000PortIndex = _LanBlazer7000PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 1, 1, 1, 1),
    _LanBlazer7000PortIndex_Type()
)
lanBlazer7000PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000PortIndex.setStatus("mandatory")


class _LanBlazer7000PortName_Type(DisplayString):
    """Custom type lanBlazer7000PortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_LanBlazer7000PortName_Type.__name__ = "DisplayString"
_LanBlazer7000PortName_Object = MibTableColumn
lanBlazer7000PortName = _LanBlazer7000PortName_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 1, 1, 1, 2),
    _LanBlazer7000PortName_Type()
)
lanBlazer7000PortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000PortName.setStatus("mandatory")


class _LanBlazer7000PortType_Type(Integer32):
    """Custom type lanBlazer7000PortType based on Integer32"""
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
        *(("ether-gigabit", 4),
          ("ether-oneHundred", 3),
          ("ether-ten-oneHundred", 2),
          ("internal", 1))
    )


_LanBlazer7000PortType_Type.__name__ = "Integer32"
_LanBlazer7000PortType_Object = MibTableColumn
lanBlazer7000PortType = _LanBlazer7000PortType_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 1, 1, 1, 3),
    _LanBlazer7000PortType_Type()
)
lanBlazer7000PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000PortType.setStatus("mandatory")


class _LanBlazer7000PortBaseType_Type(Integer32):
    """Custom type lanBlazer7000PortBaseType based on Integer32"""
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
        *(("ether-gigabit", 4),
          ("ether-oneHundred", 3),
          ("ether-ten-oneHundred", 2),
          ("internal", 1))
    )


_LanBlazer7000PortBaseType_Type.__name__ = "Integer32"
_LanBlazer7000PortBaseType_Object = MibTableColumn
lanBlazer7000PortBaseType = _LanBlazer7000PortBaseType_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 1, 1, 1, 4),
    _LanBlazer7000PortBaseType_Type()
)
lanBlazer7000PortBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000PortBaseType.setStatus("mandatory")


class _LanBlazer7000PortMode_Type(Integer32):
    """Custom type lanBlazer7000PortMode based on Integer32"""
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


_LanBlazer7000PortMode_Type.__name__ = "Integer32"
_LanBlazer7000PortMode_Object = MibTableColumn
lanBlazer7000PortMode = _LanBlazer7000PortMode_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 1, 1, 1, 5),
    _LanBlazer7000PortMode_Type()
)
lanBlazer7000PortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000PortMode.setStatus("mandatory")


class _LanBlazer7000PortStatus_Type(Integer32):
    """Custom type lanBlazer7000PortStatus based on Integer32"""
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
        *(("disabled", 1),
          ("disabledButOkay", 4),
          ("linkFailure", 5),
          ("okay", 2),
          ("warning", 3))
    )


_LanBlazer7000PortStatus_Type.__name__ = "Integer32"
_LanBlazer7000PortStatus_Object = MibTableColumn
lanBlazer7000PortStatus = _LanBlazer7000PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 1, 1, 1, 6),
    _LanBlazer7000PortStatus_Type()
)
lanBlazer7000PortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000PortStatus.setStatus("mandatory")


class _LanBlazer7000PortConnector_Type(Integer32):
    """Custom type lanBlazer7000PortConnector based on Integer32"""
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
        *(("aui", 6),
          ("fiber-SC", 4),
          ("fiber-ST", 3),
          ("internal", 1),
          ("rj45", 2),
          ("rs-232", 5))
    )


_LanBlazer7000PortConnector_Type.__name__ = "Integer32"
_LanBlazer7000PortConnector_Object = MibTableColumn
lanBlazer7000PortConnector = _LanBlazer7000PortConnector_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 1, 1, 1, 7),
    _LanBlazer7000PortConnector_Type()
)
lanBlazer7000PortConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000PortConnector.setStatus("mandatory")


class _LanBlazer7000PortSpeedState_Type(Integer32):
    """Custom type lanBlazer7000PortSpeedState based on Integer32"""
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
        *(("one-gigabit-per-second", 3),
          ("one-hundred-megabits-per-second", 2),
          ("ten-megabits-per-second", 1),
          ("under-negotiation", 4))
    )


_LanBlazer7000PortSpeedState_Type.__name__ = "Integer32"
_LanBlazer7000PortSpeedState_Object = MibTableColumn
lanBlazer7000PortSpeedState = _LanBlazer7000PortSpeedState_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 1, 1, 1, 8),
    _LanBlazer7000PortSpeedState_Type()
)
lanBlazer7000PortSpeedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000PortSpeedState.setStatus("mandatory")


class _LanBlazer7000PortDuplexState_Type(Integer32):
    """Custom type lanBlazer7000PortDuplexState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 2),
          ("half-duplex", 1),
          ("under-negotiation", 3))
    )


_LanBlazer7000PortDuplexState_Type.__name__ = "Integer32"
_LanBlazer7000PortDuplexState_Object = MibTableColumn
lanBlazer7000PortDuplexState = _LanBlazer7000PortDuplexState_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 1, 1, 1, 9),
    _LanBlazer7000PortDuplexState_Type()
)
lanBlazer7000PortDuplexState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000PortDuplexState.setStatus("mandatory")
_LanBlazer7000PortGroupBinding_Type = ResourceId
_LanBlazer7000PortGroupBinding_Object = MibTableColumn
lanBlazer7000PortGroupBinding = _LanBlazer7000PortGroupBinding_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 1, 1, 1, 10),
    _LanBlazer7000PortGroupBinding_Type()
)
lanBlazer7000PortGroupBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000PortGroupBinding.setStatus("mandatory")
_LanBlazer7000PortFlowControlMgt_ObjectIdentity = ObjectIdentity
lanBlazer7000PortFlowControlMgt = _LanBlazer7000PortFlowControlMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 2)
)
_LanBlazer7000PortFlowControlTable_Object = MibTable
lanBlazer7000PortFlowControlTable = _LanBlazer7000PortFlowControlTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 2, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000PortFlowControlTable.setStatus("mandatory")
_LanBlazer7000PortFlowControlEntry_Object = MibTableRow
lanBlazer7000PortFlowControlEntry = _LanBlazer7000PortFlowControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 2, 1, 1)
)
lanBlazer7000PortFlowControlEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000PortIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000PortFlowControlEntry.setStatus("mandatory")


class _LanBlazer7000PortFlowControlMode_Type(Integer32):
    """Custom type lanBlazer7000PortFlowControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("enable-with-aggressive-backoff", 3))
    )


_LanBlazer7000PortFlowControlMode_Type.__name__ = "Integer32"
_LanBlazer7000PortFlowControlMode_Object = MibTableColumn
lanBlazer7000PortFlowControlMode = _LanBlazer7000PortFlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 2, 1, 1, 21),
    _LanBlazer7000PortFlowControlMode_Type()
)
lanBlazer7000PortFlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000PortFlowControlMode.setStatus("mandatory")
_LanBlazer7000PortDuplexMgt_ObjectIdentity = ObjectIdentity
lanBlazer7000PortDuplexMgt = _LanBlazer7000PortDuplexMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 3)
)
_LanBlazer7000PortDuplexTable_Object = MibTable
lanBlazer7000PortDuplexTable = _LanBlazer7000PortDuplexTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 3, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000PortDuplexTable.setStatus("mandatory")
_LanBlazer7000PortDuplexEntry_Object = MibTableRow
lanBlazer7000PortDuplexEntry = _LanBlazer7000PortDuplexEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 3, 1, 1)
)
lanBlazer7000PortDuplexEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000PortIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000PortDuplexEntry.setStatus("mandatory")


class _LanBlazer7000PortDuplexMode_Type(Integer32):
    """Custom type lanBlazer7000PortDuplexMode based on Integer32"""
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


_LanBlazer7000PortDuplexMode_Type.__name__ = "Integer32"
_LanBlazer7000PortDuplexMode_Object = MibTableColumn
lanBlazer7000PortDuplexMode = _LanBlazer7000PortDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 3, 1, 1, 31),
    _LanBlazer7000PortDuplexMode_Type()
)
lanBlazer7000PortDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000PortDuplexMode.setStatus("mandatory")
_LanBlazer7000PortSpeedMgt_ObjectIdentity = ObjectIdentity
lanBlazer7000PortSpeedMgt = _LanBlazer7000PortSpeedMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 4)
)
_LanBlazer7000PortSpeedTable_Object = MibTable
lanBlazer7000PortSpeedTable = _LanBlazer7000PortSpeedTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 4, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000PortSpeedTable.setStatus("mandatory")
_LanBlazer7000PortSpeedEntry_Object = MibTableRow
lanBlazer7000PortSpeedEntry = _LanBlazer7000PortSpeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 4, 1, 1)
)
lanBlazer7000PortSpeedEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000PortIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000PortSpeedEntry.setStatus("mandatory")


class _LanBlazer7000PortSpeedMode_Type(Integer32):
    """Custom type lanBlazer7000PortSpeedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one-hundred-megabits-per-second", 2),
          ("ten-megabits-per-second", 1))
    )


_LanBlazer7000PortSpeedMode_Type.__name__ = "Integer32"
_LanBlazer7000PortSpeedMode_Object = MibTableColumn
lanBlazer7000PortSpeedMode = _LanBlazer7000PortSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 4, 1, 1, 41),
    _LanBlazer7000PortSpeedMode_Type()
)
lanBlazer7000PortSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000PortSpeedMode.setStatus("mandatory")
_LanBlazer7000PortAutoNegotiationMgt_ObjectIdentity = ObjectIdentity
lanBlazer7000PortAutoNegotiationMgt = _LanBlazer7000PortAutoNegotiationMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 5)
)
_LanBlazer7000PortAutoNegotiationTable_Object = MibTable
lanBlazer7000PortAutoNegotiationTable = _LanBlazer7000PortAutoNegotiationTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 5, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000PortAutoNegotiationTable.setStatus("mandatory")
_LanBlazer7000PortAutoNegotiationEntry_Object = MibTableRow
lanBlazer7000PortAutoNegotiationEntry = _LanBlazer7000PortAutoNegotiationEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 5, 1, 1)
)
lanBlazer7000PortAutoNegotiationEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000PortIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000PortAutoNegotiationEntry.setStatus("mandatory")


class _LanBlazer7000PortAutoNegotiationMode_Type(Integer32):
    """Custom type lanBlazer7000PortAutoNegotiationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiate", 1),
          ("manualConfiguration", 2))
    )


_LanBlazer7000PortAutoNegotiationMode_Type.__name__ = "Integer32"
_LanBlazer7000PortAutoNegotiationMode_Object = MibTableColumn
lanBlazer7000PortAutoNegotiationMode = _LanBlazer7000PortAutoNegotiationMode_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 5, 1, 1, 51),
    _LanBlazer7000PortAutoNegotiationMode_Type()
)
lanBlazer7000PortAutoNegotiationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000PortAutoNegotiationMode.setStatus("mandatory")


class _LanBlazer7000PortAutoNegotiationSpeedAdvertisement_Type(Integer32):
    """Custom type lanBlazer7000PortAutoNegotiationSpeedAdvertisement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("one-hundred-megabits-per-second", 2),
          ("ten-and-one-hundred-megabits-per-second", 1),
          ("ten-megabits-per-second", 3))
    )


_LanBlazer7000PortAutoNegotiationSpeedAdvertisement_Type.__name__ = "Integer32"
_LanBlazer7000PortAutoNegotiationSpeedAdvertisement_Object = MibTableColumn
lanBlazer7000PortAutoNegotiationSpeedAdvertisement = _LanBlazer7000PortAutoNegotiationSpeedAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 5, 1, 1, 52),
    _LanBlazer7000PortAutoNegotiationSpeedAdvertisement_Type()
)
lanBlazer7000PortAutoNegotiationSpeedAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000PortAutoNegotiationSpeedAdvertisement.setStatus("mandatory")


class _LanBlazer7000PortAutoNegotiationDuplexAdvertisement_Type(Integer32):
    """Custom type lanBlazer7000PortAutoNegotiationDuplexAdvertisement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full-and-half-duplex", 1),
          ("half-duplex", 2))
    )


_LanBlazer7000PortAutoNegotiationDuplexAdvertisement_Type.__name__ = "Integer32"
_LanBlazer7000PortAutoNegotiationDuplexAdvertisement_Object = MibTableColumn
lanBlazer7000PortAutoNegotiationDuplexAdvertisement = _LanBlazer7000PortAutoNegotiationDuplexAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 5, 1, 1, 53),
    _LanBlazer7000PortAutoNegotiationDuplexAdvertisement_Type()
)
lanBlazer7000PortAutoNegotiationDuplexAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000PortAutoNegotiationDuplexAdvertisement.setStatus("mandatory")
_LanBlazer7000PortRateLimitMgt_ObjectIdentity = ObjectIdentity
lanBlazer7000PortRateLimitMgt = _LanBlazer7000PortRateLimitMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 6)
)
_LanBlazer7000PortRateLimitTable_Object = MibTable
lanBlazer7000PortRateLimitTable = _LanBlazer7000PortRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 6, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000PortRateLimitTable.setStatus("mandatory")
_LanBlazer7000PortRateLimitEntry_Object = MibTableRow
lanBlazer7000PortRateLimitEntry = _LanBlazer7000PortRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 6, 1, 1)
)
lanBlazer7000PortRateLimitEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000PortIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000PortRateLimitEntry.setStatus("mandatory")


class _LanBlazer7000PortRateLimitMode_Type(Integer32):
    """Custom type lanBlazer7000PortRateLimitMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("enableIncludeKnownMulticast", 3))
    )


_LanBlazer7000PortRateLimitMode_Type.__name__ = "Integer32"
_LanBlazer7000PortRateLimitMode_Object = MibTableColumn
lanBlazer7000PortRateLimitMode = _LanBlazer7000PortRateLimitMode_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 6, 1, 1, 61),
    _LanBlazer7000PortRateLimitMode_Type()
)
lanBlazer7000PortRateLimitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000PortRateLimitMode.setStatus("mandatory")


class _LanBlazer7000PortRateLimitRate_Type(Integer32):
    """Custom type lanBlazer7000PortRateLimitRate based on Integer32"""
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
        *(("eighty-percent", 7),
          ("five-percent", 3),
          ("forty-percent", 6),
          ("one-percent", 1),
          ("ten-percent", 4),
          ("twenty-percent", 5),
          ("two-percent", 2))
    )


_LanBlazer7000PortRateLimitRate_Type.__name__ = "Integer32"
_LanBlazer7000PortRateLimitRate_Object = MibTableColumn
lanBlazer7000PortRateLimitRate = _LanBlazer7000PortRateLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 6, 1, 1, 62),
    _LanBlazer7000PortRateLimitRate_Type()
)
lanBlazer7000PortRateLimitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000PortRateLimitRate.setStatus("mandatory")


class _LanBlazer7000PortRateLimitBurstSize_Type(Integer32):
    """Custom type lanBlazer7000PortRateLimitBurstSize based on Integer32"""
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
        *(("rateLimit1", 1),
          ("rateLimit1024", 10),
          ("rateLimit128", 8),
          ("rateLimit16", 5),
          ("rateLimit2", 2),
          ("rateLimit2048", 11),
          ("rateLimit256", 9),
          ("rateLimit32", 6),
          ("rateLimit4", 3),
          ("rateLimit64", 7),
          ("rateLimit8", 4))
    )


_LanBlazer7000PortRateLimitBurstSize_Type.__name__ = "Integer32"
_LanBlazer7000PortRateLimitBurstSize_Object = MibTableColumn
lanBlazer7000PortRateLimitBurstSize = _LanBlazer7000PortRateLimitBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 6, 1, 1, 63),
    _LanBlazer7000PortRateLimitBurstSize_Type()
)
lanBlazer7000PortRateLimitBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000PortRateLimitBurstSize.setStatus("mandatory")
_LanBlazer7000PortPacePriorityMgt_ObjectIdentity = ObjectIdentity
lanBlazer7000PortPacePriorityMgt = _LanBlazer7000PortPacePriorityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 7)
)
_LanBlazer7000PortPacePriorityTable_Object = MibTable
lanBlazer7000PortPacePriorityTable = _LanBlazer7000PortPacePriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 7, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000PortPacePriorityTable.setStatus("mandatory")
_LanBlazer7000PortPacePriorityEntry_Object = MibTableRow
lanBlazer7000PortPacePriorityEntry = _LanBlazer7000PortPacePriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 7, 1, 1)
)
lanBlazer7000PortPacePriorityEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000PortIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000PortPacePriorityEntry.setStatus("mandatory")


class _LanBlazer7000PortPacePriorityMode_Type(Integer32):
    """Custom type lanBlazer7000PortPacePriorityMode based on Integer32"""
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


_LanBlazer7000PortPacePriorityMode_Type.__name__ = "Integer32"
_LanBlazer7000PortPacePriorityMode_Object = MibTableColumn
lanBlazer7000PortPacePriorityMode = _LanBlazer7000PortPacePriorityMode_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 7, 1, 1, 71),
    _LanBlazer7000PortPacePriorityMode_Type()
)
lanBlazer7000PortPacePriorityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000PortPacePriorityMode.setStatus("mandatory")
_LanBlazer7000PortCategoryMgt_ObjectIdentity = ObjectIdentity
lanBlazer7000PortCategoryMgt = _LanBlazer7000PortCategoryMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 8)
)
_LanBlazer7000PortCategoryTable_Object = MibTable
lanBlazer7000PortCategoryTable = _LanBlazer7000PortCategoryTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 8, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000PortCategoryTable.setStatus("mandatory")
_LanBlazer7000PortCategoryEntry_Object = MibTableRow
lanBlazer7000PortCategoryEntry = _LanBlazer7000PortCategoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 8, 1, 1)
)
lanBlazer7000PortCategoryEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000PortIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000PortCategoryEntry.setStatus("mandatory")


class _LanBlazer7000PortCategoryMode_Type(Integer32):
    """Custom type lanBlazer7000PortCategoryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("servicePort", 2),
          ("userPort", 1))
    )


_LanBlazer7000PortCategoryMode_Type.__name__ = "Integer32"
_LanBlazer7000PortCategoryMode_Object = MibTableColumn
lanBlazer7000PortCategoryMode = _LanBlazer7000PortCategoryMode_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 6, 8, 1, 1, 81),
    _LanBlazer7000PortCategoryMode_Type()
)
lanBlazer7000PortCategoryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000PortCategoryMode.setStatus("mandatory")
_LanBlazer7000BufferMgt_ObjectIdentity = ObjectIdentity
lanBlazer7000BufferMgt = _LanBlazer7000BufferMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 7)
)
_LanBlazer7000BufferTable_Object = MibTable
lanBlazer7000BufferTable = _LanBlazer7000BufferTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 7, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000BufferTable.setStatus("mandatory")
_LanBlazer7000BufferEntry_Object = MibTableRow
lanBlazer7000BufferEntry = _LanBlazer7000BufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 7, 1, 1)
)
lanBlazer7000BufferEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000BufferIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000BufferEntry.setStatus("mandatory")
_LanBlazer7000BufferIndex_Type = ResourceId
_LanBlazer7000BufferIndex_Object = MibTableColumn
lanBlazer7000BufferIndex = _LanBlazer7000BufferIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 7, 1, 1, 1),
    _LanBlazer7000BufferIndex_Type()
)
lanBlazer7000BufferIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BufferIndex.setStatus("mandatory")
_LanBlazer7000BufferFabricPort_Type = ResourceId
_LanBlazer7000BufferFabricPort_Object = MibTableColumn
lanBlazer7000BufferFabricPort = _LanBlazer7000BufferFabricPort_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 7, 1, 1, 2),
    _LanBlazer7000BufferFabricPort_Type()
)
lanBlazer7000BufferFabricPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BufferFabricPort.setStatus("mandatory")


class _LanBlazer7000BufferFabricPortDirection_Type(Integer32):
    """Custom type lanBlazer7000BufferFabricPortDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_LanBlazer7000BufferFabricPortDirection_Type.__name__ = "Integer32"
_LanBlazer7000BufferFabricPortDirection_Object = MibTableColumn
lanBlazer7000BufferFabricPortDirection = _LanBlazer7000BufferFabricPortDirection_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 7, 1, 1, 3),
    _LanBlazer7000BufferFabricPortDirection_Type()
)
lanBlazer7000BufferFabricPortDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BufferFabricPortDirection.setStatus("mandatory")
_LanBlazer7000BufferSwitchPort_Type = ResourceId
_LanBlazer7000BufferSwitchPort_Object = MibTableColumn
lanBlazer7000BufferSwitchPort = _LanBlazer7000BufferSwitchPort_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 7, 1, 1, 4),
    _LanBlazer7000BufferSwitchPort_Type()
)
lanBlazer7000BufferSwitchPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BufferSwitchPort.setStatus("mandatory")
_LanBlazer7000BufferMemory_Type = Integer32
_LanBlazer7000BufferMemory_Object = MibTableColumn
lanBlazer7000BufferMemory = _LanBlazer7000BufferMemory_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 7, 1, 1, 5),
    _LanBlazer7000BufferMemory_Type()
)
lanBlazer7000BufferMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BufferMemory.setStatus("mandatory")


class _LanBlazer7000BufferAgeTimer_Type(Integer32):
    """Custom type lanBlazer7000BufferAgeTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("one-second", 3),
          ("quarter-second", 2))
    )


_LanBlazer7000BufferAgeTimer_Type.__name__ = "Integer32"
_LanBlazer7000BufferAgeTimer_Object = MibTableColumn
lanBlazer7000BufferAgeTimer = _LanBlazer7000BufferAgeTimer_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 7, 1, 1, 6),
    _LanBlazer7000BufferAgeTimer_Type()
)
lanBlazer7000BufferAgeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000BufferAgeTimer.setStatus("mandatory")


class _LanBlazer7000BufferPriorityServicing_Type(Integer32):
    """Custom type lanBlazer7000BufferPriorityServicing based on Integer32"""
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
        *(("everyFour", 5),
          ("everyHundred", 4),
          ("everyTenThousand", 2),
          ("everyThousand", 3),
          ("strictPriority", 1))
    )


_LanBlazer7000BufferPriorityServicing_Type.__name__ = "Integer32"
_LanBlazer7000BufferPriorityServicing_Object = MibTableColumn
lanBlazer7000BufferPriorityServicing = _LanBlazer7000BufferPriorityServicing_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 7, 1, 1, 7),
    _LanBlazer7000BufferPriorityServicing_Type()
)
lanBlazer7000BufferPriorityServicing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000BufferPriorityServicing.setStatus("mandatory")


class _LanBlazer7000BufferPriorityAllocation_Type(Integer32):
    """Custom type lanBlazer7000BufferPriorityAllocation based on Integer32"""
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
        *(("fiftyPercent", 6),
          ("fortyPercent", 5),
          ("none", 1),
          ("tenPercent", 2),
          ("thirtyPercent", 4),
          ("twentyPercent", 3))
    )


_LanBlazer7000BufferPriorityAllocation_Type.__name__ = "Integer32"
_LanBlazer7000BufferPriorityAllocation_Object = MibTableColumn
lanBlazer7000BufferPriorityAllocation = _LanBlazer7000BufferPriorityAllocation_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 7, 1, 1, 8),
    _LanBlazer7000BufferPriorityAllocation_Type()
)
lanBlazer7000BufferPriorityAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000BufferPriorityAllocation.setStatus("mandatory")


class _LanBlazer7000BufferPriorityThreshold_Type(Integer32):
    """Custom type lanBlazer7000BufferPriorityThreshold based on Integer32"""
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
        *(("five", 6),
          ("four", 5),
          ("none", 1),
          ("one", 2),
          ("seven", 8),
          ("six", 7),
          ("three", 4),
          ("two", 3))
    )


_LanBlazer7000BufferPriorityThreshold_Type.__name__ = "Integer32"
_LanBlazer7000BufferPriorityThreshold_Object = MibTableColumn
lanBlazer7000BufferPriorityThreshold = _LanBlazer7000BufferPriorityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 7, 1, 1, 9),
    _LanBlazer7000BufferPriorityThreshold_Type()
)
lanBlazer7000BufferPriorityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000BufferPriorityThreshold.setStatus("mandatory")


class _LanBlazer7000BufferCongestion_Type(Integer32):
    """Custom type lanBlazer7000BufferCongestion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("congested", 3),
          ("informationNotAvailable", 1),
          ("notCongested", 2))
    )


_LanBlazer7000BufferCongestion_Type.__name__ = "Integer32"
_LanBlazer7000BufferCongestion_Object = MibTableColumn
lanBlazer7000BufferCongestion = _LanBlazer7000BufferCongestion_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 7, 1, 1, 10),
    _LanBlazer7000BufferCongestion_Type()
)
lanBlazer7000BufferCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BufferCongestion.setStatus("mandatory")
_LanBlazer7000BufferHighOverflowDrops_Type = Counter32
_LanBlazer7000BufferHighOverflowDrops_Object = MibTableColumn
lanBlazer7000BufferHighOverflowDrops = _LanBlazer7000BufferHighOverflowDrops_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 7, 1, 1, 11),
    _LanBlazer7000BufferHighOverflowDrops_Type()
)
lanBlazer7000BufferHighOverflowDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BufferHighOverflowDrops.setStatus("mandatory")
_LanBlazer7000BufferLowOverflowDrops_Type = Counter32
_LanBlazer7000BufferLowOverflowDrops_Object = MibTableColumn
lanBlazer7000BufferLowOverflowDrops = _LanBlazer7000BufferLowOverflowDrops_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 7, 1, 1, 12),
    _LanBlazer7000BufferLowOverflowDrops_Type()
)
lanBlazer7000BufferLowOverflowDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BufferLowOverflowDrops.setStatus("mandatory")
_LanBlazer7000BufferHighStaleDrops_Type = Counter32
_LanBlazer7000BufferHighStaleDrops_Object = MibTableColumn
lanBlazer7000BufferHighStaleDrops = _LanBlazer7000BufferHighStaleDrops_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 7, 1, 1, 13),
    _LanBlazer7000BufferHighStaleDrops_Type()
)
lanBlazer7000BufferHighStaleDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BufferHighStaleDrops.setStatus("mandatory")
_LanBlazer7000BufferLowStaleDrops_Type = Counter32
_LanBlazer7000BufferLowStaleDrops_Object = MibTableColumn
lanBlazer7000BufferLowStaleDrops = _LanBlazer7000BufferLowStaleDrops_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 7, 1, 1, 14),
    _LanBlazer7000BufferLowStaleDrops_Type()
)
lanBlazer7000BufferLowStaleDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BufferLowStaleDrops.setStatus("mandatory")
_LanBlazer7000BufferCongestionDrops_Type = Counter32
_LanBlazer7000BufferCongestionDrops_Object = MibTableColumn
lanBlazer7000BufferCongestionDrops = _LanBlazer7000BufferCongestionDrops_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 3, 7, 1, 1, 16),
    _LanBlazer7000BufferCongestionDrops_Type()
)
lanBlazer7000BufferCongestionDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BufferCongestionDrops.setStatus("mandatory")
_LanBlazer7000Switching_ObjectIdentity = ObjectIdentity
lanBlazer7000Switching = _LanBlazer7000Switching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5)
)
_LanBlazer7000SwitchingLayerII_ObjectIdentity = ObjectIdentity
lanBlazer7000SwitchingLayerII = _LanBlazer7000SwitchingLayerII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1)
)
_LanBlazer7000SwitchGen_ObjectIdentity = ObjectIdentity
lanBlazer7000SwitchGen = _LanBlazer7000SwitchGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 1)
)


class _LanBlazer7000SwitchSTPConfig_Type(Integer32):
    """Custom type lanBlazer7000SwitchSTPConfig based on Integer32"""
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
        *(("disable", 4),
          ("ieee8021dStp", 1),
          ("stpPerVlan", 2),
          ("twoLayerStp", 3))
    )


_LanBlazer7000SwitchSTPConfig_Type.__name__ = "Integer32"
_LanBlazer7000SwitchSTPConfig_Object = MibScalar
lanBlazer7000SwitchSTPConfig = _LanBlazer7000SwitchSTPConfig_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 1, 1),
    _LanBlazer7000SwitchSTPConfig_Type()
)
lanBlazer7000SwitchSTPConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000SwitchSTPConfig.setStatus("mandatory")


class _LanBlazer7000SwitchAgingTime_Type(Integer32):
    """Custom type lanBlazer7000SwitchAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_LanBlazer7000SwitchAgingTime_Type.__name__ = "Integer32"
_LanBlazer7000SwitchAgingTime_Object = MibScalar
lanBlazer7000SwitchAgingTime = _LanBlazer7000SwitchAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 1, 2),
    _LanBlazer7000SwitchAgingTime_Type()
)
lanBlazer7000SwitchAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000SwitchAgingTime.setStatus("mandatory")


class _LanBlazer7000SwitchSuperAgingTime_Type(Integer32):
    """Custom type lanBlazer7000SwitchSuperAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_LanBlazer7000SwitchSuperAgingTime_Type.__name__ = "Integer32"
_LanBlazer7000SwitchSuperAgingTime_Object = MibScalar
lanBlazer7000SwitchSuperAgingTime = _LanBlazer7000SwitchSuperAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 1, 3),
    _LanBlazer7000SwitchSuperAgingTime_Type()
)
lanBlazer7000SwitchSuperAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000SwitchSuperAgingTime.setStatus("mandatory")
_LanBlazer7000BridgeMgmt_ObjectIdentity = ObjectIdentity
lanBlazer7000BridgeMgmt = _LanBlazer7000BridgeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 2)
)
_LanBlazer7000BridgeTable_Object = MibTable
lanBlazer7000BridgeTable = _LanBlazer7000BridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000BridgeTable.setStatus("mandatory")
_LanBlazer7000BridgeEntry_Object = MibTableRow
lanBlazer7000BridgeEntry = _LanBlazer7000BridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 2, 1, 1)
)
lanBlazer7000BridgeEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000BridgeIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000BridgeEntry.setStatus("mandatory")
_LanBlazer7000BridgeIndex_Type = ResourceId
_LanBlazer7000BridgeIndex_Object = MibTableColumn
lanBlazer7000BridgeIndex = _LanBlazer7000BridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 2, 1, 1, 1),
    _LanBlazer7000BridgeIndex_Type()
)
lanBlazer7000BridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BridgeIndex.setStatus("mandatory")


class _LanBlazer7000BridgeType_Type(Integer32):
    """Custom type lanBlazer7000BridgeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1d", 1),
          ("virtual", 2))
    )


_LanBlazer7000BridgeType_Type.__name__ = "Integer32"
_LanBlazer7000BridgeType_Object = MibTableColumn
lanBlazer7000BridgeType = _LanBlazer7000BridgeType_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 2, 1, 1, 2),
    _LanBlazer7000BridgeType_Type()
)
lanBlazer7000BridgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BridgeType.setStatus("mandatory")


class _LanBlazer7000BridgeMode_Type(Integer32):
    """Custom type lanBlazer7000BridgeMode based on Integer32"""
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


_LanBlazer7000BridgeMode_Type.__name__ = "Integer32"
_LanBlazer7000BridgeMode_Object = MibTableColumn
lanBlazer7000BridgeMode = _LanBlazer7000BridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 2, 1, 1, 3),
    _LanBlazer7000BridgeMode_Type()
)
lanBlazer7000BridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000BridgeMode.setStatus("mandatory")


class _LanBlazer7000BridgeStatus_Type(Integer32):
    """Custom type lanBlazer7000BridgeStatus based on Integer32"""
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


_LanBlazer7000BridgeStatus_Type.__name__ = "Integer32"
_LanBlazer7000BridgeStatus_Object = MibTableColumn
lanBlazer7000BridgeStatus = _LanBlazer7000BridgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 2, 1, 1, 4),
    _LanBlazer7000BridgeStatus_Type()
)
lanBlazer7000BridgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BridgeStatus.setStatus("mandatory")


class _LanBlazer7000BridgeStpPriority_Type(Integer32):
    """Custom type lanBlazer7000BridgeStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LanBlazer7000BridgeStpPriority_Type.__name__ = "Integer32"
_LanBlazer7000BridgeStpPriority_Object = MibTableColumn
lanBlazer7000BridgeStpPriority = _LanBlazer7000BridgeStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 2, 1, 1, 5),
    _LanBlazer7000BridgeStpPriority_Type()
)
lanBlazer7000BridgeStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000BridgeStpPriority.setStatus("mandatory")
_LanBlazer7000BridgeStpTimeSinceTopologyChange_Type = TimeTicks
_LanBlazer7000BridgeStpTimeSinceTopologyChange_Object = MibTableColumn
lanBlazer7000BridgeStpTimeSinceTopologyChange = _LanBlazer7000BridgeStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 2, 1, 1, 6),
    _LanBlazer7000BridgeStpTimeSinceTopologyChange_Type()
)
lanBlazer7000BridgeStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BridgeStpTimeSinceTopologyChange.setStatus("mandatory")
_LanBlazer7000BridgeStpTopChanges_Type = Counter32
_LanBlazer7000BridgeStpTopChanges_Object = MibTableColumn
lanBlazer7000BridgeStpTopChanges = _LanBlazer7000BridgeStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 2, 1, 1, 7),
    _LanBlazer7000BridgeStpTopChanges_Type()
)
lanBlazer7000BridgeStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BridgeStpTopChanges.setStatus("mandatory")
_LanBlazer7000BridgeStpDesignatedRoot_Type = BridgeId
_LanBlazer7000BridgeStpDesignatedRoot_Object = MibTableColumn
lanBlazer7000BridgeStpDesignatedRoot = _LanBlazer7000BridgeStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 2, 1, 1, 8),
    _LanBlazer7000BridgeStpDesignatedRoot_Type()
)
lanBlazer7000BridgeStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BridgeStpDesignatedRoot.setStatus("mandatory")
_LanBlazer7000BridgeStpRootCost_Type = Integer32
_LanBlazer7000BridgeStpRootCost_Object = MibTableColumn
lanBlazer7000BridgeStpRootCost = _LanBlazer7000BridgeStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 2, 1, 1, 9),
    _LanBlazer7000BridgeStpRootCost_Type()
)
lanBlazer7000BridgeStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BridgeStpRootCost.setStatus("mandatory")
_LanBlazer7000BridgeStpRootPort_Type = Integer32
_LanBlazer7000BridgeStpRootPort_Object = MibTableColumn
lanBlazer7000BridgeStpRootPort = _LanBlazer7000BridgeStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 2, 1, 1, 10),
    _LanBlazer7000BridgeStpRootPort_Type()
)
lanBlazer7000BridgeStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BridgeStpRootPort.setStatus("mandatory")
_LanBlazer7000BridgeStpMaxAge_Type = Timeout
_LanBlazer7000BridgeStpMaxAge_Object = MibTableColumn
lanBlazer7000BridgeStpMaxAge = _LanBlazer7000BridgeStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 2, 1, 1, 11),
    _LanBlazer7000BridgeStpMaxAge_Type()
)
lanBlazer7000BridgeStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BridgeStpMaxAge.setStatus("mandatory")
_LanBlazer7000BridgeStpHelloTime_Type = Timeout
_LanBlazer7000BridgeStpHelloTime_Object = MibTableColumn
lanBlazer7000BridgeStpHelloTime = _LanBlazer7000BridgeStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 2, 1, 1, 12),
    _LanBlazer7000BridgeStpHelloTime_Type()
)
lanBlazer7000BridgeStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BridgeStpHelloTime.setStatus("mandatory")
_LanBlazer7000BridgeStpHoldTime_Type = Integer32
_LanBlazer7000BridgeStpHoldTime_Object = MibTableColumn
lanBlazer7000BridgeStpHoldTime = _LanBlazer7000BridgeStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 2, 1, 1, 13),
    _LanBlazer7000BridgeStpHoldTime_Type()
)
lanBlazer7000BridgeStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BridgeStpHoldTime.setStatus("mandatory")
_LanBlazer7000BridgeStpForwardDelay_Type = Timeout
_LanBlazer7000BridgeStpForwardDelay_Object = MibTableColumn
lanBlazer7000BridgeStpForwardDelay = _LanBlazer7000BridgeStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 2, 1, 1, 14),
    _LanBlazer7000BridgeStpForwardDelay_Type()
)
lanBlazer7000BridgeStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BridgeStpForwardDelay.setStatus("mandatory")


class _LanBlazer7000BridgeStpBridgeMaxAge_Type(Timeout):
    """Custom type lanBlazer7000BridgeStpBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_LanBlazer7000BridgeStpBridgeMaxAge_Type.__name__ = "Timeout"
_LanBlazer7000BridgeStpBridgeMaxAge_Object = MibTableColumn
lanBlazer7000BridgeStpBridgeMaxAge = _LanBlazer7000BridgeStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 2, 1, 1, 15),
    _LanBlazer7000BridgeStpBridgeMaxAge_Type()
)
lanBlazer7000BridgeStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000BridgeStpBridgeMaxAge.setStatus("mandatory")


class _LanBlazer7000BridgeStpBridgeHelloTime_Type(Timeout):
    """Custom type lanBlazer7000BridgeStpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_LanBlazer7000BridgeStpBridgeHelloTime_Type.__name__ = "Timeout"
_LanBlazer7000BridgeStpBridgeHelloTime_Object = MibTableColumn
lanBlazer7000BridgeStpBridgeHelloTime = _LanBlazer7000BridgeStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 2, 1, 1, 16),
    _LanBlazer7000BridgeStpBridgeHelloTime_Type()
)
lanBlazer7000BridgeStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000BridgeStpBridgeHelloTime.setStatus("mandatory")


class _LanBlazer7000BridgeStpBridgeForwardDelay_Type(Timeout):
    """Custom type lanBlazer7000BridgeStpBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_LanBlazer7000BridgeStpBridgeForwardDelay_Type.__name__ = "Timeout"
_LanBlazer7000BridgeStpBridgeForwardDelay_Object = MibTableColumn
lanBlazer7000BridgeStpBridgeForwardDelay = _LanBlazer7000BridgeStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 2, 1, 1, 17),
    _LanBlazer7000BridgeStpBridgeForwardDelay_Type()
)
lanBlazer7000BridgeStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000BridgeStpBridgeForwardDelay.setStatus("mandatory")
_LanBlazer7000BridgePortMgmt_ObjectIdentity = ObjectIdentity
lanBlazer7000BridgePortMgmt = _LanBlazer7000BridgePortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 3)
)
_LanBlazer7000BridgePortTable_Object = MibTable
lanBlazer7000BridgePortTable = _LanBlazer7000BridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000BridgePortTable.setStatus("mandatory")
_LanBlazer7000BridgePortEntry_Object = MibTableRow
lanBlazer7000BridgePortEntry = _LanBlazer7000BridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 3, 1, 1)
)
lanBlazer7000BridgePortEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000BridgePortIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000BridgePortEntry.setStatus("mandatory")
_LanBlazer7000BridgePortIndex_Type = ResourceId
_LanBlazer7000BridgePortIndex_Object = MibTableColumn
lanBlazer7000BridgePortIndex = _LanBlazer7000BridgePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 3, 1, 1, 1),
    _LanBlazer7000BridgePortIndex_Type()
)
lanBlazer7000BridgePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BridgePortIndex.setStatus("mandatory")


class _LanBlazer7000BridgePortPriority_Type(Integer32):
    """Custom type lanBlazer7000BridgePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LanBlazer7000BridgePortPriority_Type.__name__ = "Integer32"
_LanBlazer7000BridgePortPriority_Object = MibTableColumn
lanBlazer7000BridgePortPriority = _LanBlazer7000BridgePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 3, 1, 1, 2),
    _LanBlazer7000BridgePortPriority_Type()
)
lanBlazer7000BridgePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000BridgePortPriority.setStatus("mandatory")


class _LanBlazer7000BridgePortState_Type(Integer32):
    """Custom type lanBlazer7000BridgePortState based on Integer32"""
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


_LanBlazer7000BridgePortState_Type.__name__ = "Integer32"
_LanBlazer7000BridgePortState_Object = MibTableColumn
lanBlazer7000BridgePortState = _LanBlazer7000BridgePortState_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 3, 1, 1, 3),
    _LanBlazer7000BridgePortState_Type()
)
lanBlazer7000BridgePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BridgePortState.setStatus("mandatory")


class _LanBlazer7000BridgePortEnable_Type(Integer32):
    """Custom type lanBlazer7000BridgePortEnable based on Integer32"""
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


_LanBlazer7000BridgePortEnable_Type.__name__ = "Integer32"
_LanBlazer7000BridgePortEnable_Object = MibTableColumn
lanBlazer7000BridgePortEnable = _LanBlazer7000BridgePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 3, 1, 1, 4),
    _LanBlazer7000BridgePortEnable_Type()
)
lanBlazer7000BridgePortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000BridgePortEnable.setStatus("mandatory")


class _LanBlazer7000BridgePortPathCost_Type(Integer32):
    """Custom type lanBlazer7000BridgePortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LanBlazer7000BridgePortPathCost_Type.__name__ = "Integer32"
_LanBlazer7000BridgePortPathCost_Object = MibTableColumn
lanBlazer7000BridgePortPathCost = _LanBlazer7000BridgePortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 3, 1, 1, 5),
    _LanBlazer7000BridgePortPathCost_Type()
)
lanBlazer7000BridgePortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000BridgePortPathCost.setStatus("mandatory")
_LanBlazer7000BridgePortDesignatedRoot_Type = BridgeId
_LanBlazer7000BridgePortDesignatedRoot_Object = MibTableColumn
lanBlazer7000BridgePortDesignatedRoot = _LanBlazer7000BridgePortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 3, 1, 1, 6),
    _LanBlazer7000BridgePortDesignatedRoot_Type()
)
lanBlazer7000BridgePortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BridgePortDesignatedRoot.setStatus("mandatory")
_LanBlazer7000BridgePortDesignatedCost_Type = Integer32
_LanBlazer7000BridgePortDesignatedCost_Object = MibTableColumn
lanBlazer7000BridgePortDesignatedCost = _LanBlazer7000BridgePortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 3, 1, 1, 7),
    _LanBlazer7000BridgePortDesignatedCost_Type()
)
lanBlazer7000BridgePortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BridgePortDesignatedCost.setStatus("mandatory")
_LanBlazer7000BridgePortDesignatedBridge_Type = BridgeId
_LanBlazer7000BridgePortDesignatedBridge_Object = MibTableColumn
lanBlazer7000BridgePortDesignatedBridge = _LanBlazer7000BridgePortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 3, 1, 1, 8),
    _LanBlazer7000BridgePortDesignatedBridge_Type()
)
lanBlazer7000BridgePortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BridgePortDesignatedBridge.setStatus("mandatory")


class _LanBlazer7000BridgePortDesignatedPort_Type(OctetString):
    """Custom type lanBlazer7000BridgePortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LanBlazer7000BridgePortDesignatedPort_Type.__name__ = "OctetString"
_LanBlazer7000BridgePortDesignatedPort_Object = MibTableColumn
lanBlazer7000BridgePortDesignatedPort = _LanBlazer7000BridgePortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 3, 1, 1, 9),
    _LanBlazer7000BridgePortDesignatedPort_Type()
)
lanBlazer7000BridgePortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BridgePortDesignatedPort.setStatus("mandatory")
_LanBlazer7000BridgePortForwardTransitions_Type = Counter32
_LanBlazer7000BridgePortForwardTransitions_Object = MibTableColumn
lanBlazer7000BridgePortForwardTransitions = _LanBlazer7000BridgePortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 3, 1, 1, 10),
    _LanBlazer7000BridgePortForwardTransitions_Type()
)
lanBlazer7000BridgePortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000BridgePortForwardTransitions.setStatus("mandatory")


class _LanBlazer7000BridgePortFastStart_Type(Integer32):
    """Custom type lanBlazer7000BridgePortFastStart based on Integer32"""
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


_LanBlazer7000BridgePortFastStart_Type.__name__ = "Integer32"
_LanBlazer7000BridgePortFastStart_Object = MibTableColumn
lanBlazer7000BridgePortFastStart = _LanBlazer7000BridgePortFastStart_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 3, 1, 1, 11),
    _LanBlazer7000BridgePortFastStart_Type()
)
lanBlazer7000BridgePortFastStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000BridgePortFastStart.setStatus("deprecated")


class _LanBlazer7000BridgePortSetDefault_Type(Integer32):
    """Custom type lanBlazer7000BridgePortSetDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setDefault", 2),
          ("useCurrentValues", 1))
    )


_LanBlazer7000BridgePortSetDefault_Type.__name__ = "Integer32"
_LanBlazer7000BridgePortSetDefault_Object = MibTableColumn
lanBlazer7000BridgePortSetDefault = _LanBlazer7000BridgePortSetDefault_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 3, 1, 1, 12),
    _LanBlazer7000BridgePortSetDefault_Type()
)
lanBlazer7000BridgePortSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000BridgePortSetDefault.setStatus("mandatory")


class _LanBlazer7000BridgePortEnableChangeDetection_Type(Integer32):
    """Custom type lanBlazer7000BridgePortEnableChangeDetection based on Integer32"""
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


_LanBlazer7000BridgePortEnableChangeDetection_Type.__name__ = "Integer32"
_LanBlazer7000BridgePortEnableChangeDetection_Object = MibTableColumn
lanBlazer7000BridgePortEnableChangeDetection = _LanBlazer7000BridgePortEnableChangeDetection_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 3, 1, 1, 13),
    _LanBlazer7000BridgePortEnableChangeDetection_Type()
)
lanBlazer7000BridgePortEnableChangeDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000BridgePortEnableChangeDetection.setStatus("mandatory")
_LanBlazer7000L2AddrMgmt_ObjectIdentity = ObjectIdentity
lanBlazer7000L2AddrMgmt = _LanBlazer7000L2AddrMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4)
)
_LanBlazer7000L2AddrDatabaseMgt_ObjectIdentity = ObjectIdentity
lanBlazer7000L2AddrDatabaseMgt = _LanBlazer7000L2AddrDatabaseMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 1)
)
_LanBlazer7000L2AddressTable_Object = MibTable
lanBlazer7000L2AddressTable = _LanBlazer7000L2AddressTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressTable.setStatus("mandatory")
_LanBlazer7000L2AddressEntry_Object = MibTableRow
lanBlazer7000L2AddressEntry = _LanBlazer7000L2AddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 1, 1, 1)
)
lanBlazer7000L2AddressEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000L2AddressIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressEntry.setStatus("mandatory")
_LanBlazer7000L2AddressIndex_Type = Integer32
_LanBlazer7000L2AddressIndex_Object = MibTableColumn
lanBlazer7000L2AddressIndex = _LanBlazer7000L2AddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 1, 1, 1, 1),
    _LanBlazer7000L2AddressIndex_Type()
)
lanBlazer7000L2AddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressIndex.setStatus("mandatory")
_LanBlazer7000L2AddressTableIndex_Type = Integer32
_LanBlazer7000L2AddressTableIndex_Object = MibTableColumn
lanBlazer7000L2AddressTableIndex = _LanBlazer7000L2AddressTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 1, 1, 1, 2),
    _LanBlazer7000L2AddressTableIndex_Type()
)
lanBlazer7000L2AddressTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressTableIndex.setStatus("mandatory")
_LanBlazer7000L2AddressMacAddress_Type = MacAddress
_LanBlazer7000L2AddressMacAddress_Object = MibTableColumn
lanBlazer7000L2AddressMacAddress = _LanBlazer7000L2AddressMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 1, 1, 1, 3),
    _LanBlazer7000L2AddressMacAddress_Type()
)
lanBlazer7000L2AddressMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressMacAddress.setStatus("mandatory")
_LanBlazer7000L2AddressPortBinding_Type = ResourceId
_LanBlazer7000L2AddressPortBinding_Object = MibTableColumn
lanBlazer7000L2AddressPortBinding = _LanBlazer7000L2AddressPortBinding_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 1, 1, 1, 4),
    _LanBlazer7000L2AddressPortBinding_Type()
)
lanBlazer7000L2AddressPortBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressPortBinding.setStatus("mandatory")


class _LanBlazer7000L2AddressBindingValid_Type(Integer32):
    """Custom type lanBlazer7000L2AddressBindingValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_LanBlazer7000L2AddressBindingValid_Type.__name__ = "Integer32"
_LanBlazer7000L2AddressBindingValid_Object = MibTableColumn
lanBlazer7000L2AddressBindingValid = _LanBlazer7000L2AddressBindingValid_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 1, 1, 1, 5),
    _LanBlazer7000L2AddressBindingValid_Type()
)
lanBlazer7000L2AddressBindingValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressBindingValid.setStatus("mandatory")
_LanBlazer7000L2AddressVlanID_Type = Integer32
_LanBlazer7000L2AddressVlanID_Object = MibTableColumn
lanBlazer7000L2AddressVlanID = _LanBlazer7000L2AddressVlanID_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 1, 1, 1, 6),
    _LanBlazer7000L2AddressVlanID_Type()
)
lanBlazer7000L2AddressVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressVlanID.setStatus("mandatory")


class _LanBlazer7000L2AddressPriority_Type(Integer32):
    """Custom type lanBlazer7000L2AddressPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("priorityFour", 2),
          ("priorityZero", 1))
    )


_LanBlazer7000L2AddressPriority_Type.__name__ = "Integer32"
_LanBlazer7000L2AddressPriority_Object = MibTableColumn
lanBlazer7000L2AddressPriority = _LanBlazer7000L2AddressPriority_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 1, 1, 1, 7),
    _LanBlazer7000L2AddressPriority_Type()
)
lanBlazer7000L2AddressPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressPriority.setStatus("mandatory")


class _LanBlazer7000L2AddressForward_Type(Integer32):
    """Custom type lanBlazer7000L2AddressForward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalForward", 1),
          ("specialDelivery", 2))
    )


_LanBlazer7000L2AddressForward_Type.__name__ = "Integer32"
_LanBlazer7000L2AddressForward_Object = MibTableColumn
lanBlazer7000L2AddressForward = _LanBlazer7000L2AddressForward_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 1, 1, 1, 8),
    _LanBlazer7000L2AddressForward_Type()
)
lanBlazer7000L2AddressForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressForward.setStatus("mandatory")


class _LanBlazer7000L2AddressCopy_Type(Integer32):
    """Custom type lanBlazer7000L2AddressCopy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copyCPU", 2),
          ("normalForward", 1))
    )


_LanBlazer7000L2AddressCopy_Type.__name__ = "Integer32"
_LanBlazer7000L2AddressCopy_Object = MibTableColumn
lanBlazer7000L2AddressCopy = _LanBlazer7000L2AddressCopy_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 1, 1, 1, 9),
    _LanBlazer7000L2AddressCopy_Type()
)
lanBlazer7000L2AddressCopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressCopy.setStatus("mandatory")


class _LanBlazer7000L2AddressPersistence_Type(Integer32):
    """Custom type lanBlazer7000L2AddressPersistence based on Integer32"""
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
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_LanBlazer7000L2AddressPersistence_Type.__name__ = "Integer32"
_LanBlazer7000L2AddressPersistence_Object = MibTableColumn
lanBlazer7000L2AddressPersistence = _LanBlazer7000L2AddressPersistence_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 1, 1, 1, 10),
    _LanBlazer7000L2AddressPersistence_Type()
)
lanBlazer7000L2AddressPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressPersistence.setStatus("mandatory")


class _LanBlazer7000L2AddressStatus_Type(Integer32):
    """Custom type lanBlazer7000L2AddressStatus based on Integer32"""
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
        *(("learned", 2),
          ("mgmt", 4),
          ("other", 1),
          ("self", 3))
    )


_LanBlazer7000L2AddressStatus_Type.__name__ = "Integer32"
_LanBlazer7000L2AddressStatus_Object = MibTableColumn
lanBlazer7000L2AddressStatus = _LanBlazer7000L2AddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 1, 1, 1, 11),
    _LanBlazer7000L2AddressStatus_Type()
)
lanBlazer7000L2AddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressStatus.setStatus("mandatory")
_LanBlazer7000L2AddrSummaryMgt_ObjectIdentity = ObjectIdentity
lanBlazer7000L2AddrSummaryMgt = _LanBlazer7000L2AddrSummaryMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 2)
)
_LanBlazer7000L2AddrSummaryTable_Object = MibTable
lanBlazer7000L2AddrSummaryTable = _LanBlazer7000L2AddrSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000L2AddrSummaryTable.setStatus("mandatory")
_LanBlazer7000L2AddrSummaryEntry_Object = MibTableRow
lanBlazer7000L2AddrSummaryEntry = _LanBlazer7000L2AddrSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 2, 1, 1)
)
lanBlazer7000L2AddrSummaryEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000L2AddressIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000L2AddrSummaryEntry.setStatus("mandatory")


class _LanBlazer7000L2AddrSummary_Type(OctetString):
    """Custom type lanBlazer7000L2AddrSummary based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 4096),
    )


_LanBlazer7000L2AddrSummary_Type.__name__ = "OctetString"
_LanBlazer7000L2AddrSummary_Object = MibTableColumn
lanBlazer7000L2AddrSummary = _LanBlazer7000L2AddrSummary_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 2, 1, 1, 1),
    _LanBlazer7000L2AddrSummary_Type()
)
lanBlazer7000L2AddrSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddrSummary.setStatus("mandatory")
_LanBlazer7000L2AddrControlMgt_ObjectIdentity = ObjectIdentity
lanBlazer7000L2AddrControlMgt = _LanBlazer7000L2AddrControlMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 3)
)
_LanBlazer7000L2AddressControlTable_Object = MibTable
lanBlazer7000L2AddressControlTable = _LanBlazer7000L2AddressControlTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressControlTable.setStatus("mandatory")
_LanBlazer7000L2AddressControlEntry_Object = MibTableRow
lanBlazer7000L2AddressControlEntry = _LanBlazer7000L2AddressControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 3, 1, 1)
)
lanBlazer7000L2AddressControlEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000AgentMgrIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressControlEntry.setStatus("mandatory")
_LanBlazer7000L2AddressControlIndex_Type = Integer32
_LanBlazer7000L2AddressControlIndex_Object = MibTableColumn
lanBlazer7000L2AddressControlIndex = _LanBlazer7000L2AddressControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 3, 1, 1, 1),
    _LanBlazer7000L2AddressControlIndex_Type()
)
lanBlazer7000L2AddressControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressControlIndex.setStatus("mandatory")
_LanBlazer7000L2AddressControlMacAddress_Type = MacAddress
_LanBlazer7000L2AddressControlMacAddress_Object = MibTableColumn
lanBlazer7000L2AddressControlMacAddress = _LanBlazer7000L2AddressControlMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 3, 1, 1, 2),
    _LanBlazer7000L2AddressControlMacAddress_Type()
)
lanBlazer7000L2AddressControlMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressControlMacAddress.setStatus("mandatory")
_LanBlazer7000L2AddressControlPortBinding_Type = ResourceId
_LanBlazer7000L2AddressControlPortBinding_Object = MibTableColumn
lanBlazer7000L2AddressControlPortBinding = _LanBlazer7000L2AddressControlPortBinding_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 3, 1, 1, 3),
    _LanBlazer7000L2AddressControlPortBinding_Type()
)
lanBlazer7000L2AddressControlPortBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressControlPortBinding.setStatus("mandatory")
_LanBlazer7000L2AddressControlVlanID_Type = Integer32
_LanBlazer7000L2AddressControlVlanID_Object = MibTableColumn
lanBlazer7000L2AddressControlVlanID = _LanBlazer7000L2AddressControlVlanID_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 3, 1, 1, 4),
    _LanBlazer7000L2AddressControlVlanID_Type()
)
lanBlazer7000L2AddressControlVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressControlVlanID.setStatus("mandatory")


class _LanBlazer7000L2AddressControlPriority_Type(Integer32):
    """Custom type lanBlazer7000L2AddressControlPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("priorityFour", 2),
          ("priorityZero", 1))
    )


_LanBlazer7000L2AddressControlPriority_Type.__name__ = "Integer32"
_LanBlazer7000L2AddressControlPriority_Object = MibTableColumn
lanBlazer7000L2AddressControlPriority = _LanBlazer7000L2AddressControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 3, 1, 1, 5),
    _LanBlazer7000L2AddressControlPriority_Type()
)
lanBlazer7000L2AddressControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressControlPriority.setStatus("mandatory")


class _LanBlazer7000L2AddressControlPersistence_Type(Integer32):
    """Custom type lanBlazer7000L2AddressControlPersistence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deleteOnReset", 2),
          ("deleteOnTimeout", 3),
          ("permanent", 1))
    )


_LanBlazer7000L2AddressControlPersistence_Type.__name__ = "Integer32"
_LanBlazer7000L2AddressControlPersistence_Object = MibTableColumn
lanBlazer7000L2AddressControlPersistence = _LanBlazer7000L2AddressControlPersistence_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 3, 1, 1, 6),
    _LanBlazer7000L2AddressControlPersistence_Type()
)
lanBlazer7000L2AddressControlPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressControlPersistence.setStatus("mandatory")


class _LanBlazer7000L2AddressControlStatus_Type(Integer32):
    """Custom type lanBlazer7000L2AddressControlStatus based on Integer32"""
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
        *(("createRequest", 1),
          ("entryExistsError", 5),
          ("invalidMacAddress", 6),
          ("invalidPortBinding", 7),
          ("invalidVlanID", 8),
          ("otherError", 4),
          ("success", 3),
          ("underCreation", 2))
    )


_LanBlazer7000L2AddressControlStatus_Type.__name__ = "Integer32"
_LanBlazer7000L2AddressControlStatus_Object = MibTableColumn
lanBlazer7000L2AddressControlStatus = _LanBlazer7000L2AddressControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 3, 1, 1, 7),
    _LanBlazer7000L2AddressControlStatus_Type()
)
lanBlazer7000L2AddressControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressControlStatus.setStatus("mandatory")
_LanBlazer7000L2AddrChangeMgt_ObjectIdentity = ObjectIdentity
lanBlazer7000L2AddrChangeMgt = _LanBlazer7000L2AddrChangeMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 4)
)
_LanBlazer7000L2AddressChangeLast_Type = Integer32
_LanBlazer7000L2AddressChangeLast_Object = MibScalar
lanBlazer7000L2AddressChangeLast = _LanBlazer7000L2AddressChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 4, 1),
    _LanBlazer7000L2AddressChangeLast_Type()
)
lanBlazer7000L2AddressChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressChangeLast.setStatus("mandatory")
_LanBlazer7000L2AddressChangeWraps_Type = Counter32
_LanBlazer7000L2AddressChangeWraps_Object = MibScalar
lanBlazer7000L2AddressChangeWraps = _LanBlazer7000L2AddressChangeWraps_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 4, 2),
    _LanBlazer7000L2AddressChangeWraps_Type()
)
lanBlazer7000L2AddressChangeWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressChangeWraps.setStatus("mandatory")


class _LanBlazer7000L2AddressChangeMaxEntries_Type(Integer32):
    """Custom type lanBlazer7000L2AddressChangeMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 4096),
    )


_LanBlazer7000L2AddressChangeMaxEntries_Type.__name__ = "Integer32"
_LanBlazer7000L2AddressChangeMaxEntries_Object = MibScalar
lanBlazer7000L2AddressChangeMaxEntries = _LanBlazer7000L2AddressChangeMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 4, 3),
    _LanBlazer7000L2AddressChangeMaxEntries_Type()
)
lanBlazer7000L2AddressChangeMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressChangeMaxEntries.setStatus("mandatory")
_LanBlazer7000L2AddressChangeTable_Object = MibTable
lanBlazer7000L2AddressChangeTable = _LanBlazer7000L2AddressChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 4, 4)
)
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressChangeTable.setStatus("mandatory")
_LanBlazer7000L2AddressChangeEntry_Object = MibTableRow
lanBlazer7000L2AddressChangeEntry = _LanBlazer7000L2AddressChangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 4, 4, 1)
)
lanBlazer7000L2AddressChangeEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000L2AddressChangeWrapCount"),
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000L2AddressChangeIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressChangeEntry.setStatus("mandatory")
_LanBlazer7000L2AddressChangeWrapCount_Type = Integer32
_LanBlazer7000L2AddressChangeWrapCount_Object = MibTableColumn
lanBlazer7000L2AddressChangeWrapCount = _LanBlazer7000L2AddressChangeWrapCount_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 4, 4, 1, 1),
    _LanBlazer7000L2AddressChangeWrapCount_Type()
)
lanBlazer7000L2AddressChangeWrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressChangeWrapCount.setStatus("mandatory")
_LanBlazer7000L2AddressChangeIndex_Type = Integer32
_LanBlazer7000L2AddressChangeIndex_Object = MibTableColumn
lanBlazer7000L2AddressChangeIndex = _LanBlazer7000L2AddressChangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 4, 4, 1, 2),
    _LanBlazer7000L2AddressChangeIndex_Type()
)
lanBlazer7000L2AddressChangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressChangeIndex.setStatus("mandatory")
_LanBlazer7000L2AddressChangeIndexChanged_Type = Integer32
_LanBlazer7000L2AddressChangeIndexChanged_Object = MibTableColumn
lanBlazer7000L2AddressChangeIndexChanged = _LanBlazer7000L2AddressChangeIndexChanged_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 4, 4, 1, 3),
    _LanBlazer7000L2AddressChangeIndexChanged_Type()
)
lanBlazer7000L2AddressChangeIndexChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressChangeIndexChanged.setStatus("mandatory")


class _LanBlazer7000L2AddressChangeSummary_Type(OctetString):
    """Custom type lanBlazer7000L2AddressChangeSummary based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_LanBlazer7000L2AddressChangeSummary_Type.__name__ = "OctetString"
_LanBlazer7000L2AddressChangeSummary_Object = MibTableColumn
lanBlazer7000L2AddressChangeSummary = _LanBlazer7000L2AddressChangeSummary_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 1, 4, 4, 4, 1, 4),
    _LanBlazer7000L2AddressChangeSummary_Type()
)
lanBlazer7000L2AddressChangeSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000L2AddressChangeSummary.setStatus("mandatory")
_LanBlazer7000SwitchPortMgt_ObjectIdentity = ObjectIdentity
lanBlazer7000SwitchPortMgt = _LanBlazer7000SwitchPortMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 2)
)
_LanBlazer7000SwitchPortTable_Object = MibTable
lanBlazer7000SwitchPortTable = _LanBlazer7000SwitchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000SwitchPortTable.setStatus("mandatory")
_LanBlazer7000SwitchPortEntry_Object = MibTableRow
lanBlazer7000SwitchPortEntry = _LanBlazer7000SwitchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 2, 1, 1)
)
lanBlazer7000SwitchPortEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000SwitchPortIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000SwitchPortEntry.setStatus("mandatory")
_LanBlazer7000SwitchPortIndex_Type = ResourceId
_LanBlazer7000SwitchPortIndex_Object = MibTableColumn
lanBlazer7000SwitchPortIndex = _LanBlazer7000SwitchPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 2, 1, 1, 1),
    _LanBlazer7000SwitchPortIndex_Type()
)
lanBlazer7000SwitchPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000SwitchPortIndex.setStatus("mandatory")


class _LanBlazer7000SwitchPortSTAPMode_Type(Integer32):
    """Custom type lanBlazer7000SwitchPortSTAPMode based on Integer32"""
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


_LanBlazer7000SwitchPortSTAPMode_Type.__name__ = "Integer32"
_LanBlazer7000SwitchPortSTAPMode_Object = MibTableColumn
lanBlazer7000SwitchPortSTAPMode = _LanBlazer7000SwitchPortSTAPMode_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 2, 1, 1, 2),
    _LanBlazer7000SwitchPortSTAPMode_Type()
)
lanBlazer7000SwitchPortSTAPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000SwitchPortSTAPMode.setStatus("mandatory")


class _LanBlazer7000SwitchPortConvertToStatic_Type(Integer32):
    """Custom type lanBlazer7000SwitchPortConvertToStatic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("convertToStatic", 2),
          ("learnAsDynamic", 1))
    )


_LanBlazer7000SwitchPortConvertToStatic_Type.__name__ = "Integer32"
_LanBlazer7000SwitchPortConvertToStatic_Object = MibTableColumn
lanBlazer7000SwitchPortConvertToStatic = _LanBlazer7000SwitchPortConvertToStatic_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 2, 1, 1, 3),
    _LanBlazer7000SwitchPortConvertToStatic_Type()
)
lanBlazer7000SwitchPortConvertToStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000SwitchPortConvertToStatic.setStatus("mandatory")


class _LanBlazer7000SwitchPortLearningMode_Type(Integer32):
    """Custom type lanBlazer7000SwitchPortLearningMode based on Integer32"""
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


_LanBlazer7000SwitchPortLearningMode_Type.__name__ = "Integer32"
_LanBlazer7000SwitchPortLearningMode_Object = MibTableColumn
lanBlazer7000SwitchPortLearningMode = _LanBlazer7000SwitchPortLearningMode_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 2, 1, 1, 4),
    _LanBlazer7000SwitchPortLearningMode_Type()
)
lanBlazer7000SwitchPortLearningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000SwitchPortLearningMode.setStatus("mandatory")
_LanBlazer7000SwitchPortHuntGroup_Type = Integer32
_LanBlazer7000SwitchPortHuntGroup_Object = MibTableColumn
lanBlazer7000SwitchPortHuntGroup = _LanBlazer7000SwitchPortHuntGroup_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 2, 1, 1, 5),
    _LanBlazer7000SwitchPortHuntGroup_Type()
)
lanBlazer7000SwitchPortHuntGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000SwitchPortHuntGroup.setStatus("mandatory")
_LanBlazer7000SwitchPortPhysicalPort_Type = ResourceId
_LanBlazer7000SwitchPortPhysicalPort_Object = MibTableColumn
lanBlazer7000SwitchPortPhysicalPort = _LanBlazer7000SwitchPortPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 2, 1, 1, 6),
    _LanBlazer7000SwitchPortPhysicalPort_Type()
)
lanBlazer7000SwitchPortPhysicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000SwitchPortPhysicalPort.setStatus("mandatory")


class _LanBlazer7000SwitchPortKnownMode_Type(Integer32):
    """Custom type lanBlazer7000SwitchPortKnownMode based on Integer32"""
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


_LanBlazer7000SwitchPortKnownMode_Type.__name__ = "Integer32"
_LanBlazer7000SwitchPortKnownMode_Object = MibTableColumn
lanBlazer7000SwitchPortKnownMode = _LanBlazer7000SwitchPortKnownMode_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 2, 1, 1, 7),
    _LanBlazer7000SwitchPortKnownMode_Type()
)
lanBlazer7000SwitchPortKnownMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000SwitchPortKnownMode.setStatus("mandatory")


class _LanBlazer7000SwitchPortMappingMethod_Type(Integer32):
    """Custom type lanBlazer7000SwitchPortMappingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("port-based", 1)
    )


_LanBlazer7000SwitchPortMappingMethod_Type.__name__ = "Integer32"
_LanBlazer7000SwitchPortMappingMethod_Object = MibTableColumn
lanBlazer7000SwitchPortMappingMethod = _LanBlazer7000SwitchPortMappingMethod_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 2, 1, 1, 8),
    _LanBlazer7000SwitchPortMappingMethod_Type()
)
lanBlazer7000SwitchPortMappingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000SwitchPortMappingMethod.setStatus("mandatory")


class _LanBlazer7000SwitchPortTrunkingMode_Type(Integer32):
    """Custom type lanBlazer7000SwitchPortTrunkingMode based on Integer32"""
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
        *(("clear", 1),
          ("ieee8021q", 2),
          ("multiLevel", 3),
          ("trunk3Com", 4))
    )


_LanBlazer7000SwitchPortTrunkingMode_Type.__name__ = "Integer32"
_LanBlazer7000SwitchPortTrunkingMode_Object = MibTableColumn
lanBlazer7000SwitchPortTrunkingMode = _LanBlazer7000SwitchPortTrunkingMode_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 2, 1, 1, 9),
    _LanBlazer7000SwitchPortTrunkingMode_Type()
)
lanBlazer7000SwitchPortTrunkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000SwitchPortTrunkingMode.setStatus("mandatory")


class _LanBlazer7000SwitchPortVlanBindingMethod_Type(Integer32):
    """Custom type lanBlazer7000SwitchPortVlanBindingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 3),
          ("persistent", 2),
          ("static", 1))
    )


_LanBlazer7000SwitchPortVlanBindingMethod_Type.__name__ = "Integer32"
_LanBlazer7000SwitchPortVlanBindingMethod_Object = MibTableColumn
lanBlazer7000SwitchPortVlanBindingMethod = _LanBlazer7000SwitchPortVlanBindingMethod_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 2, 1, 1, 10),
    _LanBlazer7000SwitchPortVlanBindingMethod_Type()
)
lanBlazer7000SwitchPortVlanBindingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000SwitchPortVlanBindingMethod.setStatus("mandatory")


class _LanBlazer7000SwitchPortIgnoreTag_Type(Integer32):
    """Custom type lanBlazer7000SwitchPortIgnoreTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignoreTag", 2),
          ("useTag", 1))
    )


_LanBlazer7000SwitchPortIgnoreTag_Type.__name__ = "Integer32"
_LanBlazer7000SwitchPortIgnoreTag_Object = MibTableColumn
lanBlazer7000SwitchPortIgnoreTag = _LanBlazer7000SwitchPortIgnoreTag_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 2, 1, 1, 11),
    _LanBlazer7000SwitchPortIgnoreTag_Type()
)
lanBlazer7000SwitchPortIgnoreTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000SwitchPortIgnoreTag.setStatus("mandatory")
_LanBlazer7000SwitchPortVlanID_Type = Integer32
_LanBlazer7000SwitchPortVlanID_Object = MibTableColumn
lanBlazer7000SwitchPortVlanID = _LanBlazer7000SwitchPortVlanID_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 2, 1, 1, 12),
    _LanBlazer7000SwitchPortVlanID_Type()
)
lanBlazer7000SwitchPortVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000SwitchPortVlanID.setStatus("mandatory")


class _LanBlazer7000SwitchPort3ComMappingTableIndex_Type(Integer32):
    """Custom type lanBlazer7000SwitchPort3ComMappingTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_LanBlazer7000SwitchPort3ComMappingTableIndex_Type.__name__ = "Integer32"
_LanBlazer7000SwitchPort3ComMappingTableIndex_Object = MibTableColumn
lanBlazer7000SwitchPort3ComMappingTableIndex = _LanBlazer7000SwitchPort3ComMappingTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 2, 1, 1, 13),
    _LanBlazer7000SwitchPort3ComMappingTableIndex_Type()
)
lanBlazer7000SwitchPort3ComMappingTableIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000SwitchPort3ComMappingTableIndex.setStatus("mandatory")


class _LanBlazer7000SwitchPortAutoVlanCreation_Type(Integer32):
    """Custom type lanBlazer7000SwitchPortAutoVlanCreation based on Integer32"""
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


_LanBlazer7000SwitchPortAutoVlanCreation_Type.__name__ = "Integer32"
_LanBlazer7000SwitchPortAutoVlanCreation_Object = MibTableColumn
lanBlazer7000SwitchPortAutoVlanCreation = _LanBlazer7000SwitchPortAutoVlanCreation_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 2, 1, 1, 14),
    _LanBlazer7000SwitchPortAutoVlanCreation_Type()
)
lanBlazer7000SwitchPortAutoVlanCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000SwitchPortAutoVlanCreation.setStatus("mandatory")


class _LanBlazer7000SwitchPortMirrorMode_Type(Integer32):
    """Custom type lanBlazer7000SwitchPortMirrorMode based on Integer32"""
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


_LanBlazer7000SwitchPortMirrorMode_Type.__name__ = "Integer32"
_LanBlazer7000SwitchPortMirrorMode_Object = MibScalar
lanBlazer7000SwitchPortMirrorMode = _LanBlazer7000SwitchPortMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 2, 1, 1, 15),
    _LanBlazer7000SwitchPortMirrorMode_Type()
)
lanBlazer7000SwitchPortMirrorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000SwitchPortMirrorMode.setStatus("mandatory")
_LanBlazer7000SwitchPortIfIndex_Type = Integer32
_LanBlazer7000SwitchPortIfIndex_Object = MibTableColumn
lanBlazer7000SwitchPortIfIndex = _LanBlazer7000SwitchPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 2, 1, 1, 16),
    _LanBlazer7000SwitchPortIfIndex_Type()
)
lanBlazer7000SwitchPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000SwitchPortIfIndex.setStatus("mandatory")


class _LanBlazer7000SwitchPortFastStart_Type(Integer32):
    """Custom type lanBlazer7000SwitchPortFastStart based on Integer32"""
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


_LanBlazer7000SwitchPortFastStart_Type.__name__ = "Integer32"
_LanBlazer7000SwitchPortFastStart_Object = MibTableColumn
lanBlazer7000SwitchPortFastStart = _LanBlazer7000SwitchPortFastStart_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 2, 1, 1, 17),
    _LanBlazer7000SwitchPortFastStart_Type()
)
lanBlazer7000SwitchPortFastStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000SwitchPortFastStart.setStatus("mandatory")


class _LanBlazer7000SwitchPortVlanExchange_Type(Integer32):
    """Custom type lanBlazer7000SwitchPortVlanExchange based on Integer32"""
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


_LanBlazer7000SwitchPortVlanExchange_Type.__name__ = "Integer32"
_LanBlazer7000SwitchPortVlanExchange_Object = MibTableColumn
lanBlazer7000SwitchPortVlanExchange = _LanBlazer7000SwitchPortVlanExchange_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 2, 1, 1, 18),
    _LanBlazer7000SwitchPortVlanExchange_Type()
)
lanBlazer7000SwitchPortVlanExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000SwitchPortVlanExchange.setStatus("mandatory")
_LanBlazer7000HuntGroupMgt_ObjectIdentity = ObjectIdentity
lanBlazer7000HuntGroupMgt = _LanBlazer7000HuntGroupMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 4)
)
_LanBlazer7000HuntGroupTable_Object = MibTable
lanBlazer7000HuntGroupTable = _LanBlazer7000HuntGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 4, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000HuntGroupTable.setStatus("mandatory")
_LanBlazer7000HuntGroupEntry_Object = MibTableRow
lanBlazer7000HuntGroupEntry = _LanBlazer7000HuntGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 4, 1, 1)
)
lanBlazer7000HuntGroupEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000HuntGroupIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000HuntGroupEntry.setStatus("mandatory")
_LanBlazer7000HuntGroupIndex_Type = Integer32
_LanBlazer7000HuntGroupIndex_Object = MibTableColumn
lanBlazer7000HuntGroupIndex = _LanBlazer7000HuntGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 4, 1, 1, 1),
    _LanBlazer7000HuntGroupIndex_Type()
)
lanBlazer7000HuntGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000HuntGroupIndex.setStatus("mandatory")
_LanBlazer7000HuntGroupName_Type = DisplayString
_LanBlazer7000HuntGroupName_Object = MibTableColumn
lanBlazer7000HuntGroupName = _LanBlazer7000HuntGroupName_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 4, 1, 1, 2),
    _LanBlazer7000HuntGroupName_Type()
)
lanBlazer7000HuntGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000HuntGroupName.setStatus("mandatory")
_LanBlazer7000HuntGroupBasePort_Type = ResourceId
_LanBlazer7000HuntGroupBasePort_Object = MibTableColumn
lanBlazer7000HuntGroupBasePort = _LanBlazer7000HuntGroupBasePort_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 4, 1, 1, 3),
    _LanBlazer7000HuntGroupBasePort_Type()
)
lanBlazer7000HuntGroupBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000HuntGroupBasePort.setStatus("mandatory")
_LanBlazer7000HuntGroupNumberOfPorts_Type = Integer32
_LanBlazer7000HuntGroupNumberOfPorts_Object = MibTableColumn
lanBlazer7000HuntGroupNumberOfPorts = _LanBlazer7000HuntGroupNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 4, 1, 1, 4),
    _LanBlazer7000HuntGroupNumberOfPorts_Type()
)
lanBlazer7000HuntGroupNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000HuntGroupNumberOfPorts.setStatus("mandatory")


class _LanBlazer7000HuntGroupLoadSharing_Type(Integer32):
    """Custom type lanBlazer7000HuntGroupLoadSharing based on Integer32"""
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


_LanBlazer7000HuntGroupLoadSharing_Type.__name__ = "Integer32"
_LanBlazer7000HuntGroupLoadSharing_Object = MibTableColumn
lanBlazer7000HuntGroupLoadSharing = _LanBlazer7000HuntGroupLoadSharing_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 4, 1, 1, 5),
    _LanBlazer7000HuntGroupLoadSharing_Type()
)
lanBlazer7000HuntGroupLoadSharing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000HuntGroupLoadSharing.setStatus("mandatory")


class _LanBlazer7000HuntGroupStatus_Type(Integer32):
    """Custom type lanBlazer7000HuntGroupStatus based on Integer32"""
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
        *(("active", 4),
          ("createRequest", 1),
          ("deleteRequest", 3),
          ("underCreation", 2))
    )


_LanBlazer7000HuntGroupStatus_Type.__name__ = "Integer32"
_LanBlazer7000HuntGroupStatus_Object = MibTableColumn
lanBlazer7000HuntGroupStatus = _LanBlazer7000HuntGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 4, 1, 1, 6),
    _LanBlazer7000HuntGroupStatus_Type()
)
lanBlazer7000HuntGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000HuntGroupStatus.setStatus("mandatory")
_LanBlazer7000PortMirroringMgt_ObjectIdentity = ObjectIdentity
lanBlazer7000PortMirroringMgt = _LanBlazer7000PortMirroringMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 5)
)
_LanBlazer7000PortMirroringTable_Object = MibTable
lanBlazer7000PortMirroringTable = _LanBlazer7000PortMirroringTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 5, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000PortMirroringTable.setStatus("mandatory")
_LanBlazer7000PortMirroringEntry_Object = MibTableRow
lanBlazer7000PortMirroringEntry = _LanBlazer7000PortMirroringEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 5, 1, 1)
)
lanBlazer7000PortMirroringEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000PortMirroringIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000PortMirroringEntry.setStatus("mandatory")
_LanBlazer7000PortMirroringIndex_Type = ResourceId
_LanBlazer7000PortMirroringIndex_Object = MibTableColumn
lanBlazer7000PortMirroringIndex = _LanBlazer7000PortMirroringIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 5, 1, 1, 1),
    _LanBlazer7000PortMirroringIndex_Type()
)
lanBlazer7000PortMirroringIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000PortMirroringIndex.setStatus("mandatory")
_LanBlazer7000PortMirroringSourceSubPort_Type = Integer32
_LanBlazer7000PortMirroringSourceSubPort_Object = MibTableColumn
lanBlazer7000PortMirroringSourceSubPort = _LanBlazer7000PortMirroringSourceSubPort_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 5, 1, 1, 2),
    _LanBlazer7000PortMirroringSourceSubPort_Type()
)
lanBlazer7000PortMirroringSourceSubPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000PortMirroringSourceSubPort.setStatus("mandatory")


class _LanBlazer7000PortMirroringSamplerType_Type(Integer32):
    """Custom type lanBlazer7000PortMirroringSamplerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("periodic", 3))
    )


_LanBlazer7000PortMirroringSamplerType_Type.__name__ = "Integer32"
_LanBlazer7000PortMirroringSamplerType_Object = MibTableColumn
lanBlazer7000PortMirroringSamplerType = _LanBlazer7000PortMirroringSamplerType_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 5, 1, 1, 3),
    _LanBlazer7000PortMirroringSamplerType_Type()
)
lanBlazer7000PortMirroringSamplerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000PortMirroringSamplerType.setStatus("mandatory")
_LanBlazer7000PortMirroringRate_Type = Integer32
_LanBlazer7000PortMirroringRate_Object = MibTableColumn
lanBlazer7000PortMirroringRate = _LanBlazer7000PortMirroringRate_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 5, 1, 1, 4),
    _LanBlazer7000PortMirroringRate_Type()
)
lanBlazer7000PortMirroringRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000PortMirroringRate.setStatus("mandatory")
_LanBlazer7000PortMirroringMirrorPort_Type = ResourceId
_LanBlazer7000PortMirroringMirrorPort_Object = MibTableColumn
lanBlazer7000PortMirroringMirrorPort = _LanBlazer7000PortMirroringMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 5, 5, 1, 1, 5),
    _LanBlazer7000PortMirroringMirrorPort_Type()
)
lanBlazer7000PortMirroringMirrorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000PortMirroringMirrorPort.setStatus("mandatory")
_LanBlazer7000VlanMgt_ObjectIdentity = ObjectIdentity
lanBlazer7000VlanMgt = _LanBlazer7000VlanMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7)
)
_LanBlazer7000Vlans_ObjectIdentity = ObjectIdentity
lanBlazer7000Vlans = _LanBlazer7000Vlans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 1)
)
_LanBlazer7000VlanTable_Object = MibTable
lanBlazer7000VlanTable = _LanBlazer7000VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000VlanTable.setStatus("mandatory")
_LanBlazer7000VlanEntry_Object = MibTableRow
lanBlazer7000VlanEntry = _LanBlazer7000VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 1, 1, 1)
)
lanBlazer7000VlanEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000VlanID"),
)
if mibBuilder.loadTexts:
    lanBlazer7000VlanEntry.setStatus("mandatory")
_LanBlazer7000VlanID_Type = Integer32
_LanBlazer7000VlanID_Object = MibTableColumn
lanBlazer7000VlanID = _LanBlazer7000VlanID_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 1, 1, 1, 1),
    _LanBlazer7000VlanID_Type()
)
lanBlazer7000VlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000VlanID.setStatus("mandatory")


class _LanBlazer7000VlanName_Type(DisplayString):
    """Custom type lanBlazer7000VlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_LanBlazer7000VlanName_Type.__name__ = "DisplayString"
_LanBlazer7000VlanName_Object = MibTableColumn
lanBlazer7000VlanName = _LanBlazer7000VlanName_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 1, 1, 1, 2),
    _LanBlazer7000VlanName_Type()
)
lanBlazer7000VlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000VlanName.setStatus("mandatory")
_LanBlazer7000VlanIfIndex_Type = Integer32
_LanBlazer7000VlanIfIndex_Object = MibTableColumn
lanBlazer7000VlanIfIndex = _LanBlazer7000VlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 1, 1, 1, 3),
    _LanBlazer7000VlanIfIndex_Type()
)
lanBlazer7000VlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000VlanIfIndex.setStatus("mandatory")
_LanBlazer7000VlanAFTIndex_Type = Integer32
_LanBlazer7000VlanAFTIndex_Object = MibTableColumn
lanBlazer7000VlanAFTIndex = _LanBlazer7000VlanAFTIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 1, 1, 1, 4),
    _LanBlazer7000VlanAFTIndex_Type()
)
lanBlazer7000VlanAFTIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000VlanAFTIndex.setStatus("mandatory")
_LanBlazer7000VlanBridgeIndex_Type = ResourceId
_LanBlazer7000VlanBridgeIndex_Object = MibTableColumn
lanBlazer7000VlanBridgeIndex = _LanBlazer7000VlanBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 1, 1, 1, 5),
    _LanBlazer7000VlanBridgeIndex_Type()
)
lanBlazer7000VlanBridgeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000VlanBridgeIndex.setStatus("mandatory")


class _LanBlazer7000VlanStatus_Type(Integer32):
    """Custom type lanBlazer7000VlanStatus based on Integer32"""
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
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("active", 5),
          ("createRequest", 1),
          ("destroyRequest", 3),
          ("entryExistsError", 7),
          ("invalidVlanAFTIndex", 10),
          ("invalidVlanAutoIncrementHTSize", 13),
          ("invalidVlanBridgeIndex", 11),
          ("invalidVlanID", 8),
          ("invalidVlanInitialHashTableSize", 12),
          ("invalidVlanName", 9),
          ("otherError", 6),
          ("underCreation", 2),
          ("underDestruction", 4))
    )


_LanBlazer7000VlanStatus_Type.__name__ = "Integer32"
_LanBlazer7000VlanStatus_Object = MibTableColumn
lanBlazer7000VlanStatus = _LanBlazer7000VlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 1, 1, 1, 6),
    _LanBlazer7000VlanStatus_Type()
)
lanBlazer7000VlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000VlanStatus.setStatus("mandatory")


class _LanBlazer7000VlanInitialHashTableSize_Type(Integer32):
    """Custom type lanBlazer7000VlanInitialHashTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 8192),
    )


_LanBlazer7000VlanInitialHashTableSize_Type.__name__ = "Integer32"
_LanBlazer7000VlanInitialHashTableSize_Object = MibTableColumn
lanBlazer7000VlanInitialHashTableSize = _LanBlazer7000VlanInitialHashTableSize_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 1, 1, 1, 7),
    _LanBlazer7000VlanInitialHashTableSize_Type()
)
lanBlazer7000VlanInitialHashTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000VlanInitialHashTableSize.setStatus("mandatory")


class _LanBlazer7000VlanAutoIncrementHTSize_Type(Integer32):
    """Custom type lanBlazer7000VlanAutoIncrementHTSize based on Integer32"""
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


_LanBlazer7000VlanAutoIncrementHTSize_Type.__name__ = "Integer32"
_LanBlazer7000VlanAutoIncrementHTSize_Object = MibTableColumn
lanBlazer7000VlanAutoIncrementHTSize = _LanBlazer7000VlanAutoIncrementHTSize_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 1, 1, 1, 8),
    _LanBlazer7000VlanAutoIncrementHTSize_Type()
)
lanBlazer7000VlanAutoIncrementHTSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000VlanAutoIncrementHTSize.setStatus("mandatory")


class _LanBlazer7000VlanLearnStatus_Type(Integer32):
    """Custom type lanBlazer7000VlanLearnStatus based on Integer32"""
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
          ("notLearned", 1),
          ("vlanExchange", 2))
    )


_LanBlazer7000VlanLearnStatus_Type.__name__ = "Integer32"
_LanBlazer7000VlanLearnStatus_Object = MibTableColumn
lanBlazer7000VlanLearnStatus = _LanBlazer7000VlanLearnStatus_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 1, 1, 1, 9),
    _LanBlazer7000VlanLearnStatus_Type()
)
lanBlazer7000VlanLearnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000VlanLearnStatus.setStatus("mandatory")
_LanBlazer7000VlanMappings_ObjectIdentity = ObjectIdentity
lanBlazer7000VlanMappings = _LanBlazer7000VlanMappings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 3)
)
_LanBlazer70003ComMapping_ObjectIdentity = ObjectIdentity
lanBlazer70003ComMapping = _LanBlazer70003ComMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 3, 1)
)
_LanBlazer70003ComMappingTable_Object = MibTable
lanBlazer70003ComMappingTable = _LanBlazer70003ComMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 3, 1, 1)
)
if mibBuilder.loadTexts:
    lanBlazer70003ComMappingTable.setStatus("mandatory")
_LanBlazer70003ComMappingEntry_Object = MibTableRow
lanBlazer70003ComMappingEntry = _LanBlazer70003ComMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 3, 1, 1, 1)
)
lanBlazer70003ComMappingEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer70003ComMappingTableIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer70003ComMappingEntry.setStatus("mandatory")
_LanBlazer70003ComMappingTableIndex_Type = Integer32
_LanBlazer70003ComMappingTableIndex_Object = MibTableColumn
lanBlazer70003ComMappingTableIndex = _LanBlazer70003ComMappingTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 3, 1, 1, 1, 1),
    _LanBlazer70003ComMappingTableIndex_Type()
)
lanBlazer70003ComMappingTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer70003ComMappingTableIndex.setStatus("mandatory")


class _LanBlazer70003ComMappingTableName_Type(DisplayString):
    """Custom type lanBlazer70003ComMappingTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_LanBlazer70003ComMappingTableName_Type.__name__ = "DisplayString"
_LanBlazer70003ComMappingTableName_Object = MibTableColumn
lanBlazer70003ComMappingTableName = _LanBlazer70003ComMappingTableName_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 3, 1, 1, 1, 2),
    _LanBlazer70003ComMappingTableName_Type()
)
lanBlazer70003ComMappingTableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer70003ComMappingTableName.setStatus("mandatory")


class _LanBlazer70003ComMappingTableStatus_Type(Integer32):
    """Custom type lanBlazer70003ComMappingTableStatus based on Integer32"""
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
        *(("active", 3),
          ("createRequest", 1),
          ("destroyRequest", 2),
          ("entryExistsError", 4),
          ("otherError", 5))
    )


_LanBlazer70003ComMappingTableStatus_Type.__name__ = "Integer32"
_LanBlazer70003ComMappingTableStatus_Object = MibTableColumn
lanBlazer70003ComMappingTableStatus = _LanBlazer70003ComMappingTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 3, 1, 1, 1, 3),
    _LanBlazer70003ComMappingTableStatus_Type()
)
lanBlazer70003ComMappingTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer70003ComMappingTableStatus.setStatus("mandatory")
_LanBlazer7000Vlan3ComMapping_ObjectIdentity = ObjectIdentity
lanBlazer7000Vlan3ComMapping = _LanBlazer7000Vlan3ComMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 3, 2)
)
_LanBlazer7000Vlan3ComMappingTable_Object = MibTable
lanBlazer7000Vlan3ComMappingTable = _LanBlazer7000Vlan3ComMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 3, 2, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000Vlan3ComMappingTable.setStatus("mandatory")
_LanBlazer7000Vlan3ComMappingEntry_Object = MibTableRow
lanBlazer7000Vlan3ComMappingEntry = _LanBlazer7000Vlan3ComMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 3, 2, 1, 1)
)
lanBlazer7000Vlan3ComMappingEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer70003ComMappingTableIndex"),
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000Vlan3ComMappingIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000Vlan3ComMappingEntry.setStatus("mandatory")


class _LanBlazer7000Vlan3ComMappingIndex_Type(Integer32):
    """Custom type lanBlazer7000Vlan3ComMappingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_LanBlazer7000Vlan3ComMappingIndex_Type.__name__ = "Integer32"
_LanBlazer7000Vlan3ComMappingIndex_Object = MibTableColumn
lanBlazer7000Vlan3ComMappingIndex = _LanBlazer7000Vlan3ComMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 3, 2, 1, 1, 1),
    _LanBlazer7000Vlan3ComMappingIndex_Type()
)
lanBlazer7000Vlan3ComMappingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000Vlan3ComMappingIndex.setStatus("mandatory")
_LanBlazer7000Vlan3ComMappingVlanID_Type = Integer32
_LanBlazer7000Vlan3ComMappingVlanID_Object = MibTableColumn
lanBlazer7000Vlan3ComMappingVlanID = _LanBlazer7000Vlan3ComMappingVlanID_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 3, 2, 1, 1, 2),
    _LanBlazer7000Vlan3ComMappingVlanID_Type()
)
lanBlazer7000Vlan3ComMappingVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000Vlan3ComMappingVlanID.setStatus("mandatory")


class _LanBlazer7000Vlan3ComMappingStatus_Type(Integer32):
    """Custom type lanBlazer7000Vlan3ComMappingStatus based on Integer32"""
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
        *(("active", 3),
          ("createRequest", 1),
          ("destroyRequest", 2),
          ("otherError", 4))
    )


_LanBlazer7000Vlan3ComMappingStatus_Type.__name__ = "Integer32"
_LanBlazer7000Vlan3ComMappingStatus_Object = MibTableColumn
lanBlazer7000Vlan3ComMappingStatus = _LanBlazer7000Vlan3ComMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 3, 2, 1, 1, 3),
    _LanBlazer7000Vlan3ComMappingStatus_Type()
)
lanBlazer7000Vlan3ComMappingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000Vlan3ComMappingStatus.setStatus("mandatory")
_LanBlazer7000VirtualPorts_ObjectIdentity = ObjectIdentity
lanBlazer7000VirtualPorts = _LanBlazer7000VirtualPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 4)
)
_LanBlazer7000VirtualSwitchPortTable_Object = MibTable
lanBlazer7000VirtualSwitchPortTable = _LanBlazer7000VirtualSwitchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 4, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000VirtualSwitchPortTable.setStatus("mandatory")
_LanBlazer7000VirtualSwitchPortEntry_Object = MibTableRow
lanBlazer7000VirtualSwitchPortEntry = _LanBlazer7000VirtualSwitchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 4, 1, 1)
)
lanBlazer7000VirtualSwitchPortEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000VirtualSwitchPortIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000VirtualSwitchPortEntry.setStatus("mandatory")
_LanBlazer7000VirtualSwitchPortIndex_Type = ResourceId
_LanBlazer7000VirtualSwitchPortIndex_Object = MibTableColumn
lanBlazer7000VirtualSwitchPortIndex = _LanBlazer7000VirtualSwitchPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 4, 1, 1, 1),
    _LanBlazer7000VirtualSwitchPortIndex_Type()
)
lanBlazer7000VirtualSwitchPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000VirtualSwitchPortIndex.setStatus("mandatory")


class _LanBlazer7000VirtualSwitchPortFormat_Type(Integer32):
    """Custom type lanBlazer7000VirtualSwitchPortFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("trunkingFormat", 2))
    )


_LanBlazer7000VirtualSwitchPortFormat_Type.__name__ = "Integer32"
_LanBlazer7000VirtualSwitchPortFormat_Object = MibTableColumn
lanBlazer7000VirtualSwitchPortFormat = _LanBlazer7000VirtualSwitchPortFormat_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 4, 1, 1, 2),
    _LanBlazer7000VirtualSwitchPortFormat_Type()
)
lanBlazer7000VirtualSwitchPortFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000VirtualSwitchPortFormat.setStatus("mandatory")
_LanBlazer7000VirtualSwitchPortBridgePort_Type = ResourceId
_LanBlazer7000VirtualSwitchPortBridgePort_Object = MibTableColumn
lanBlazer7000VirtualSwitchPortBridgePort = _LanBlazer7000VirtualSwitchPortBridgePort_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 4, 1, 1, 3),
    _LanBlazer7000VirtualSwitchPortBridgePort_Type()
)
lanBlazer7000VirtualSwitchPortBridgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000VirtualSwitchPortBridgePort.setStatus("mandatory")


class _LanBlazer7000VirtualSwitchPortBindingType_Type(Integer32):
    """Custom type lanBlazer7000VirtualSwitchPortBindingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 3),
          ("persistent", 2),
          ("static", 1))
    )


_LanBlazer7000VirtualSwitchPortBindingType_Type.__name__ = "Integer32"
_LanBlazer7000VirtualSwitchPortBindingType_Object = MibTableColumn
lanBlazer7000VirtualSwitchPortBindingType = _LanBlazer7000VirtualSwitchPortBindingType_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 4, 1, 1, 4),
    _LanBlazer7000VirtualSwitchPortBindingType_Type()
)
lanBlazer7000VirtualSwitchPortBindingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000VirtualSwitchPortBindingType.setStatus("mandatory")


class _LanBlazer7000VirtualSwitchPortStatus_Type(Integer32):
    """Custom type lanBlazer7000VirtualSwitchPortStatus based on Integer32"""
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
        *(("active", 3),
          ("createRequest", 1),
          ("destroyRequest", 2),
          ("entryExistsError", 5),
          ("entryNoExistError", 6),
          ("otherError", 4))
    )


_LanBlazer7000VirtualSwitchPortStatus_Type.__name__ = "Integer32"
_LanBlazer7000VirtualSwitchPortStatus_Object = MibTableColumn
lanBlazer7000VirtualSwitchPortStatus = _LanBlazer7000VirtualSwitchPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 7, 4, 1, 1, 5),
    _LanBlazer7000VirtualSwitchPortStatus_Type()
)
lanBlazer7000VirtualSwitchPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000VirtualSwitchPortStatus.setStatus("mandatory")
_LanBlazer7000Events_ObjectIdentity = ObjectIdentity
lanBlazer7000Events = _LanBlazer7000Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10)
)
_LanBlazer7000EventMgt_ObjectIdentity = ObjectIdentity
lanBlazer7000EventMgt = _LanBlazer7000EventMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 1)
)
_LanBlazer7000EventTable_Object = MibTable
lanBlazer7000EventTable = _LanBlazer7000EventTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 1, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000EventTable.setStatus("mandatory")
_LanBlazer7000EventEntry_Object = MibTableRow
lanBlazer7000EventEntry = _LanBlazer7000EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 1, 1, 1)
)
lanBlazer7000EventEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000EventIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000EventEntry.setStatus("mandatory")
_LanBlazer7000EventIndex_Type = Integer32
_LanBlazer7000EventIndex_Object = MibTableColumn
lanBlazer7000EventIndex = _LanBlazer7000EventIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 1, 1, 1, 1),
    _LanBlazer7000EventIndex_Type()
)
lanBlazer7000EventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventIndex.setStatus("mandatory")


class _LanBlazer7000EventMode_Type(Integer32):
    """Custom type lanBlazer7000EventMode based on Integer32"""
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


_LanBlazer7000EventMode_Type.__name__ = "Integer32"
_LanBlazer7000EventMode_Object = MibTableColumn
lanBlazer7000EventMode = _LanBlazer7000EventMode_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 1, 1, 1, 2),
    _LanBlazer7000EventMode_Type()
)
lanBlazer7000EventMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000EventMode.setStatus("mandatory")


class _LanBlazer7000EventLogAction_Type(Integer32):
    """Custom type lanBlazer7000EventLogAction based on Integer32"""
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


_LanBlazer7000EventLogAction_Type.__name__ = "Integer32"
_LanBlazer7000EventLogAction_Object = MibTableColumn
lanBlazer7000EventLogAction = _LanBlazer7000EventLogAction_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 1, 1, 1, 3),
    _LanBlazer7000EventLogAction_Type()
)
lanBlazer7000EventLogAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000EventLogAction.setStatus("mandatory")


class _LanBlazer7000EventTrapAction_Type(Integer32):
    """Custom type lanBlazer7000EventTrapAction based on Integer32"""
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


_LanBlazer7000EventTrapAction_Type.__name__ = "Integer32"
_LanBlazer7000EventTrapAction_Object = MibTableColumn
lanBlazer7000EventTrapAction = _LanBlazer7000EventTrapAction_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 1, 1, 1, 4),
    _LanBlazer7000EventTrapAction_Type()
)
lanBlazer7000EventTrapAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000EventTrapAction.setStatus("mandatory")


class _LanBlazer7000EventConsoleAction_Type(Integer32):
    """Custom type lanBlazer7000EventConsoleAction based on Integer32"""
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


_LanBlazer7000EventConsoleAction_Type.__name__ = "Integer32"
_LanBlazer7000EventConsoleAction_Object = MibTableColumn
lanBlazer7000EventConsoleAction = _LanBlazer7000EventConsoleAction_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 1, 1, 1, 5),
    _LanBlazer7000EventConsoleAction_Type()
)
lanBlazer7000EventConsoleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000EventConsoleAction.setStatus("mandatory")
_LanBlazer7000EventLogMgt_ObjectIdentity = ObjectIdentity
lanBlazer7000EventLogMgt = _LanBlazer7000EventLogMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 2)
)


class _LanBlazer7000LogTableMaxSize_Type(Integer32):
    """Custom type lanBlazer7000LogTableMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_LanBlazer7000LogTableMaxSize_Type.__name__ = "Integer32"
_LanBlazer7000LogTableMaxSize_Object = MibScalar
lanBlazer7000LogTableMaxSize = _LanBlazer7000LogTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 2, 1),
    _LanBlazer7000LogTableMaxSize_Type()
)
lanBlazer7000LogTableMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000LogTableMaxSize.setStatus("mandatory")


class _LanBlazer7000LogLastEntry_Type(Integer32):
    """Custom type lanBlazer7000LogLastEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LanBlazer7000LogLastEntry_Type.__name__ = "Integer32"
_LanBlazer7000LogLastEntry_Object = MibScalar
lanBlazer7000LogLastEntry = _LanBlazer7000LogLastEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 2, 2),
    _LanBlazer7000LogLastEntry_Type()
)
lanBlazer7000LogLastEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000LogLastEntry.setStatus("mandatory")
_LanBlazer7000LogWraps_Type = Counter32
_LanBlazer7000LogWraps_Object = MibScalar
lanBlazer7000LogWraps = _LanBlazer7000LogWraps_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 2, 3),
    _LanBlazer7000LogWraps_Type()
)
lanBlazer7000LogWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000LogWraps.setStatus("mandatory")
_LanBlazer7000EventLog_ObjectIdentity = ObjectIdentity
lanBlazer7000EventLog = _LanBlazer7000EventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 3)
)
_LanBlazer7000EventLogTable_Object = MibTable
lanBlazer7000EventLogTable = _LanBlazer7000EventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 3, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000EventLogTable.setStatus("mandatory")
_LanBlazer7000EventLogEntry_Object = MibTableRow
lanBlazer7000EventLogEntry = _LanBlazer7000EventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 3, 1, 1)
)
lanBlazer7000EventLogEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000EventLogIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000EventLogEntry.setStatus("mandatory")


class _LanBlazer7000EventLogEventIndex_Type(Integer32):
    """Custom type lanBlazer7000EventLogEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LanBlazer7000EventLogEventIndex_Type.__name__ = "Integer32"
_LanBlazer7000EventLogEventIndex_Object = MibTableColumn
lanBlazer7000EventLogEventIndex = _LanBlazer7000EventLogEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 3, 1, 1, 1),
    _LanBlazer7000EventLogEventIndex_Type()
)
lanBlazer7000EventLogEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventLogEventIndex.setStatus("mandatory")


class _LanBlazer7000EventLogIndex_Type(Integer32):
    """Custom type lanBlazer7000EventLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LanBlazer7000EventLogIndex_Type.__name__ = "Integer32"
_LanBlazer7000EventLogIndex_Object = MibTableColumn
lanBlazer7000EventLogIndex = _LanBlazer7000EventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 3, 1, 1, 2),
    _LanBlazer7000EventLogIndex_Type()
)
lanBlazer7000EventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventLogIndex.setStatus("mandatory")
_LanBlazer7000EventLogTime_Type = TimeTicks
_LanBlazer7000EventLogTime_Object = MibTableColumn
lanBlazer7000EventLogTime = _LanBlazer7000EventLogTime_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 3, 1, 1, 3),
    _LanBlazer7000EventLogTime_Type()
)
lanBlazer7000EventLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventLogTime.setStatus("mandatory")


class _LanBlazer7000EventLogDescr_Type(DisplayString):
    """Custom type lanBlazer7000EventLogDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LanBlazer7000EventLogDescr_Type.__name__ = "DisplayString"
_LanBlazer7000EventLogDescr_Object = MibTableColumn
lanBlazer7000EventLogDescr = _LanBlazer7000EventLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 3, 1, 1, 4),
    _LanBlazer7000EventLogDescr_Type()
)
lanBlazer7000EventLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventLogDescr.setStatus("mandatory")
_LanBlazer7000EventLogType_Type = EventCategory
_LanBlazer7000EventLogType_Object = MibTableColumn
lanBlazer7000EventLogType = _LanBlazer7000EventLogType_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 3, 1, 1, 5),
    _LanBlazer7000EventLogType_Type()
)
lanBlazer7000EventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventLogType.setStatus("mandatory")


class _LanBlazer7000EventLogSeverity_Type(Integer32):
    """Custom type lanBlazer7000EventLogSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LanBlazer7000EventLogSeverity_Type.__name__ = "Integer32"
_LanBlazer7000EventLogSeverity_Object = MibTableColumn
lanBlazer7000EventLogSeverity = _LanBlazer7000EventLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 3, 1, 1, 6),
    _LanBlazer7000EventLogSeverity_Type()
)
lanBlazer7000EventLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventLogSeverity.setStatus("mandatory")


class _LanBlazer7000EventLogDTM_Type(DisplayString):
    """Custom type lanBlazer7000EventLogDTM based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_LanBlazer7000EventLogDTM_Type.__name__ = "DisplayString"
_LanBlazer7000EventLogDTM_Object = MibTableColumn
lanBlazer7000EventLogDTM = _LanBlazer7000EventLogDTM_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 3, 1, 1, 7),
    _LanBlazer7000EventLogDTM_Type()
)
lanBlazer7000EventLogDTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventLogDTM.setStatus("mandatory")
_LanBlazer7000EventLogResType_Type = ResourceType
_LanBlazer7000EventLogResType_Object = MibTableColumn
lanBlazer7000EventLogResType = _LanBlazer7000EventLogResType_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 3, 1, 1, 8),
    _LanBlazer7000EventLogResType_Type()
)
lanBlazer7000EventLogResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventLogResType.setStatus("mandatory")
_LanBlazer7000EventLogResID_Type = ResourceId
_LanBlazer7000EventLogResID_Object = MibTableColumn
lanBlazer7000EventLogResID = _LanBlazer7000EventLogResID_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 3, 1, 1, 9),
    _LanBlazer7000EventLogResID_Type()
)
lanBlazer7000EventLogResID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventLogResID.setStatus("mandatory")
_LanBlazer7000EventLogResLeaf_Type = Integer32
_LanBlazer7000EventLogResLeaf_Object = MibTableColumn
lanBlazer7000EventLogResLeaf = _LanBlazer7000EventLogResLeaf_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 3, 1, 1, 10),
    _LanBlazer7000EventLogResLeaf_Type()
)
lanBlazer7000EventLogResLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventLogResLeaf.setStatus("mandatory")
_LanBlazer7000EventLogValueType_Type = EventValueType
_LanBlazer7000EventLogValueType_Object = MibTableColumn
lanBlazer7000EventLogValueType = _LanBlazer7000EventLogValueType_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 3, 1, 1, 11),
    _LanBlazer7000EventLogValueType_Type()
)
lanBlazer7000EventLogValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventLogValueType.setStatus("mandatory")


class _LanBlazer7000EventLogValue_Type(OctetString):
    """Custom type lanBlazer7000EventLogValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_LanBlazer7000EventLogValue_Type.__name__ = "OctetString"
_LanBlazer7000EventLogValue_Object = MibTableColumn
lanBlazer7000EventLogValue = _LanBlazer7000EventLogValue_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 3, 1, 1, 12),
    _LanBlazer7000EventLogValue_Type()
)
lanBlazer7000EventLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventLogValue.setStatus("mandatory")
_LanBlazer7000EventLogEpochTime_Type = Integer32
_LanBlazer7000EventLogEpochTime_Object = MibTableColumn
lanBlazer7000EventLogEpochTime = _LanBlazer7000EventLogEpochTime_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 3, 1, 1, 13),
    _LanBlazer7000EventLogEpochTime_Type()
)
lanBlazer7000EventLogEpochTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventLogEpochTime.setStatus("mandatory")


class _LanBlazer7000EventLogID_Type(Integer32):
    """Custom type lanBlazer7000EventLogID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LanBlazer7000EventLogID_Type.__name__ = "Integer32"
_LanBlazer7000EventLogID_Object = MibTableColumn
lanBlazer7000EventLogID = _LanBlazer7000EventLogID_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 3, 1, 1, 14),
    _LanBlazer7000EventLogID_Type()
)
lanBlazer7000EventLogID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventLogID.setStatus("mandatory")
_LanBlazer7000ShutdownLogMgt_ObjectIdentity = ObjectIdentity
lanBlazer7000ShutdownLogMgt = _LanBlazer7000ShutdownLogMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 4)
)


class _LanBlazer7000ShutdownLogTableMaxSize_Type(Integer32):
    """Custom type lanBlazer7000ShutdownLogTableMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_LanBlazer7000ShutdownLogTableMaxSize_Type.__name__ = "Integer32"
_LanBlazer7000ShutdownLogTableMaxSize_Object = MibScalar
lanBlazer7000ShutdownLogTableMaxSize = _LanBlazer7000ShutdownLogTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 4, 1),
    _LanBlazer7000ShutdownLogTableMaxSize_Type()
)
lanBlazer7000ShutdownLogTableMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000ShutdownLogTableMaxSize.setStatus("mandatory")


class _LanBlazer7000ShutdownLogLastEntry_Type(Integer32):
    """Custom type lanBlazer7000ShutdownLogLastEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LanBlazer7000ShutdownLogLastEntry_Type.__name__ = "Integer32"
_LanBlazer7000ShutdownLogLastEntry_Object = MibScalar
lanBlazer7000ShutdownLogLastEntry = _LanBlazer7000ShutdownLogLastEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 4, 2),
    _LanBlazer7000ShutdownLogLastEntry_Type()
)
lanBlazer7000ShutdownLogLastEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000ShutdownLogLastEntry.setStatus("mandatory")


class _LanBlazer7000ShutdownLogAcknowledged_Type(Integer32):
    """Custom type lanBlazer7000ShutdownLogAcknowledged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acknowledged", 2),
          ("not-acknowledged", 1))
    )


_LanBlazer7000ShutdownLogAcknowledged_Type.__name__ = "Integer32"
_LanBlazer7000ShutdownLogAcknowledged_Object = MibScalar
lanBlazer7000ShutdownLogAcknowledged = _LanBlazer7000ShutdownLogAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 4, 3),
    _LanBlazer7000ShutdownLogAcknowledged_Type()
)
lanBlazer7000ShutdownLogAcknowledged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000ShutdownLogAcknowledged.setStatus("mandatory")
_LanBlazer7000EventShutdownLog_ObjectIdentity = ObjectIdentity
lanBlazer7000EventShutdownLog = _LanBlazer7000EventShutdownLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 5)
)
_LanBlazer7000EventShutdownLogTable_Object = MibTable
lanBlazer7000EventShutdownLogTable = _LanBlazer7000EventShutdownLogTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 5, 1)
)
if mibBuilder.loadTexts:
    lanBlazer7000EventShutdownLogTable.setStatus("mandatory")
_LanBlazer7000EventShutdownLogEntry_Object = MibTableRow
lanBlazer7000EventShutdownLogEntry = _LanBlazer7000EventShutdownLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 5, 1, 1)
)
lanBlazer7000EventShutdownLogEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000EventShutdownLogIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000EventShutdownLogEntry.setStatus("mandatory")


class _LanBlazer7000EventShutdownLogEventIndex_Type(Integer32):
    """Custom type lanBlazer7000EventShutdownLogEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LanBlazer7000EventShutdownLogEventIndex_Type.__name__ = "Integer32"
_LanBlazer7000EventShutdownLogEventIndex_Object = MibTableColumn
lanBlazer7000EventShutdownLogEventIndex = _LanBlazer7000EventShutdownLogEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 5, 1, 1, 1),
    _LanBlazer7000EventShutdownLogEventIndex_Type()
)
lanBlazer7000EventShutdownLogEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventShutdownLogEventIndex.setStatus("mandatory")


class _LanBlazer7000EventShutdownLogIndex_Type(Integer32):
    """Custom type lanBlazer7000EventShutdownLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LanBlazer7000EventShutdownLogIndex_Type.__name__ = "Integer32"
_LanBlazer7000EventShutdownLogIndex_Object = MibTableColumn
lanBlazer7000EventShutdownLogIndex = _LanBlazer7000EventShutdownLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 5, 1, 1, 2),
    _LanBlazer7000EventShutdownLogIndex_Type()
)
lanBlazer7000EventShutdownLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventShutdownLogIndex.setStatus("mandatory")
_LanBlazer7000EventShutdownLogTime_Type = TimeTicks
_LanBlazer7000EventShutdownLogTime_Object = MibTableColumn
lanBlazer7000EventShutdownLogTime = _LanBlazer7000EventShutdownLogTime_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 5, 1, 1, 3),
    _LanBlazer7000EventShutdownLogTime_Type()
)
lanBlazer7000EventShutdownLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventShutdownLogTime.setStatus("mandatory")


class _LanBlazer7000EventShutdownLogDescr_Type(DisplayString):
    """Custom type lanBlazer7000EventShutdownLogDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LanBlazer7000EventShutdownLogDescr_Type.__name__ = "DisplayString"
_LanBlazer7000EventShutdownLogDescr_Object = MibTableColumn
lanBlazer7000EventShutdownLogDescr = _LanBlazer7000EventShutdownLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 5, 1, 1, 4),
    _LanBlazer7000EventShutdownLogDescr_Type()
)
lanBlazer7000EventShutdownLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventShutdownLogDescr.setStatus("mandatory")
_LanBlazer7000EventShutdownLogType_Type = EventCategory
_LanBlazer7000EventShutdownLogType_Object = MibTableColumn
lanBlazer7000EventShutdownLogType = _LanBlazer7000EventShutdownLogType_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 5, 1, 1, 5),
    _LanBlazer7000EventShutdownLogType_Type()
)
lanBlazer7000EventShutdownLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventShutdownLogType.setStatus("mandatory")


class _LanBlazer7000EventShutdownLogSeverity_Type(Integer32):
    """Custom type lanBlazer7000EventShutdownLogSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LanBlazer7000EventShutdownLogSeverity_Type.__name__ = "Integer32"
_LanBlazer7000EventShutdownLogSeverity_Object = MibTableColumn
lanBlazer7000EventShutdownLogSeverity = _LanBlazer7000EventShutdownLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 5, 1, 1, 6),
    _LanBlazer7000EventShutdownLogSeverity_Type()
)
lanBlazer7000EventShutdownLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventShutdownLogSeverity.setStatus("mandatory")


class _LanBlazer7000EventShutdownLogDTM_Type(DisplayString):
    """Custom type lanBlazer7000EventShutdownLogDTM based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_LanBlazer7000EventShutdownLogDTM_Type.__name__ = "DisplayString"
_LanBlazer7000EventShutdownLogDTM_Object = MibTableColumn
lanBlazer7000EventShutdownLogDTM = _LanBlazer7000EventShutdownLogDTM_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 5, 1, 1, 7),
    _LanBlazer7000EventShutdownLogDTM_Type()
)
lanBlazer7000EventShutdownLogDTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventShutdownLogDTM.setStatus("mandatory")
_LanBlazer7000EventShutdownLogResType_Type = ResourceType
_LanBlazer7000EventShutdownLogResType_Object = MibTableColumn
lanBlazer7000EventShutdownLogResType = _LanBlazer7000EventShutdownLogResType_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 5, 1, 1, 8),
    _LanBlazer7000EventShutdownLogResType_Type()
)
lanBlazer7000EventShutdownLogResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventShutdownLogResType.setStatus("mandatory")
_LanBlazer7000EventShutdownLogResID_Type = ResourceId
_LanBlazer7000EventShutdownLogResID_Object = MibTableColumn
lanBlazer7000EventShutdownLogResID = _LanBlazer7000EventShutdownLogResID_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 5, 1, 1, 9),
    _LanBlazer7000EventShutdownLogResID_Type()
)
lanBlazer7000EventShutdownLogResID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventShutdownLogResID.setStatus("mandatory")
_LanBlazer7000EventShutdownLogResLeaf_Type = Integer32
_LanBlazer7000EventShutdownLogResLeaf_Object = MibTableColumn
lanBlazer7000EventShutdownLogResLeaf = _LanBlazer7000EventShutdownLogResLeaf_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 5, 1, 1, 10),
    _LanBlazer7000EventShutdownLogResLeaf_Type()
)
lanBlazer7000EventShutdownLogResLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventShutdownLogResLeaf.setStatus("mandatory")
_LanBlazer7000EventShutdownLogValueType_Type = EventValueType
_LanBlazer7000EventShutdownLogValueType_Object = MibTableColumn
lanBlazer7000EventShutdownLogValueType = _LanBlazer7000EventShutdownLogValueType_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 5, 1, 1, 11),
    _LanBlazer7000EventShutdownLogValueType_Type()
)
lanBlazer7000EventShutdownLogValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventShutdownLogValueType.setStatus("mandatory")


class _LanBlazer7000EventShutdownLogValue_Type(OctetString):
    """Custom type lanBlazer7000EventShutdownLogValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_LanBlazer7000EventShutdownLogValue_Type.__name__ = "OctetString"
_LanBlazer7000EventShutdownLogValue_Object = MibTableColumn
lanBlazer7000EventShutdownLogValue = _LanBlazer7000EventShutdownLogValue_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 5, 1, 1, 12),
    _LanBlazer7000EventShutdownLogValue_Type()
)
lanBlazer7000EventShutdownLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventShutdownLogValue.setStatus("mandatory")
_LanBlazer7000EventShutdownLogEpochTime_Type = Integer32
_LanBlazer7000EventShutdownLogEpochTime_Object = MibTableColumn
lanBlazer7000EventShutdownLogEpochTime = _LanBlazer7000EventShutdownLogEpochTime_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 5, 1, 1, 13),
    _LanBlazer7000EventShutdownLogEpochTime_Type()
)
lanBlazer7000EventShutdownLogEpochTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventShutdownLogEpochTime.setStatus("mandatory")


class _LanBlazer7000EventShutdownLogID_Type(Integer32):
    """Custom type lanBlazer7000EventShutdownLogID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LanBlazer7000EventShutdownLogID_Type.__name__ = "Integer32"
_LanBlazer7000EventShutdownLogID_Object = MibTableColumn
lanBlazer7000EventShutdownLogID = _LanBlazer7000EventShutdownLogID_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 5, 1, 1, 14),
    _LanBlazer7000EventShutdownLogID_Type()
)
lanBlazer7000EventShutdownLogID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventShutdownLogID.setStatus("mandatory")
_LanBlazer7000EventTrapMgmt_ObjectIdentity = ObjectIdentity
lanBlazer7000EventTrapMgmt = _LanBlazer7000EventTrapMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 6)
)


class _LanBlazer7000EventTrapEventIndex_Type(Integer32):
    """Custom type lanBlazer7000EventTrapEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LanBlazer7000EventTrapEventIndex_Type.__name__ = "Integer32"
_LanBlazer7000EventTrapEventIndex_Object = MibScalar
lanBlazer7000EventTrapEventIndex = _LanBlazer7000EventTrapEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 6, 1),
    _LanBlazer7000EventTrapEventIndex_Type()
)
lanBlazer7000EventTrapEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventTrapEventIndex.setStatus("mandatory")
_LanBlazer7000EventTrapTime_Type = TimeTicks
_LanBlazer7000EventTrapTime_Object = MibScalar
lanBlazer7000EventTrapTime = _LanBlazer7000EventTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 6, 2),
    _LanBlazer7000EventTrapTime_Type()
)
lanBlazer7000EventTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventTrapTime.setStatus("mandatory")


class _LanBlazer7000EventTrapDescr_Type(DisplayString):
    """Custom type lanBlazer7000EventTrapDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LanBlazer7000EventTrapDescr_Type.__name__ = "DisplayString"
_LanBlazer7000EventTrapDescr_Object = MibScalar
lanBlazer7000EventTrapDescr = _LanBlazer7000EventTrapDescr_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 6, 3),
    _LanBlazer7000EventTrapDescr_Type()
)
lanBlazer7000EventTrapDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventTrapDescr.setStatus("mandatory")
_LanBlazer7000EventTrapType_Type = EventCategory
_LanBlazer7000EventTrapType_Object = MibScalar
lanBlazer7000EventTrapType = _LanBlazer7000EventTrapType_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 6, 4),
    _LanBlazer7000EventTrapType_Type()
)
lanBlazer7000EventTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventTrapType.setStatus("mandatory")


class _LanBlazer7000EventTrapSeverity_Type(Integer32):
    """Custom type lanBlazer7000EventTrapSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LanBlazer7000EventTrapSeverity_Type.__name__ = "Integer32"
_LanBlazer7000EventTrapSeverity_Object = MibScalar
lanBlazer7000EventTrapSeverity = _LanBlazer7000EventTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 6, 5),
    _LanBlazer7000EventTrapSeverity_Type()
)
lanBlazer7000EventTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventTrapSeverity.setStatus("mandatory")


class _LanBlazer7000EventTrapDTM_Type(DisplayString):
    """Custom type lanBlazer7000EventTrapDTM based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_LanBlazer7000EventTrapDTM_Type.__name__ = "DisplayString"
_LanBlazer7000EventTrapDTM_Object = MibScalar
lanBlazer7000EventTrapDTM = _LanBlazer7000EventTrapDTM_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 6, 6),
    _LanBlazer7000EventTrapDTM_Type()
)
lanBlazer7000EventTrapDTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventTrapDTM.setStatus("mandatory")
_LanBlazer7000EventTrapResType_Type = ResourceType
_LanBlazer7000EventTrapResType_Object = MibScalar
lanBlazer7000EventTrapResType = _LanBlazer7000EventTrapResType_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 6, 7),
    _LanBlazer7000EventTrapResType_Type()
)
lanBlazer7000EventTrapResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventTrapResType.setStatus("mandatory")
_LanBlazer7000EventTrapResID_Type = ResourceId
_LanBlazer7000EventTrapResID_Object = MibScalar
lanBlazer7000EventTrapResID = _LanBlazer7000EventTrapResID_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 6, 8),
    _LanBlazer7000EventTrapResID_Type()
)
lanBlazer7000EventTrapResID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventTrapResID.setStatus("mandatory")
_LanBlazer7000EventTrapResLeaf_Type = Integer32
_LanBlazer7000EventTrapResLeaf_Object = MibScalar
lanBlazer7000EventTrapResLeaf = _LanBlazer7000EventTrapResLeaf_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 6, 9),
    _LanBlazer7000EventTrapResLeaf_Type()
)
lanBlazer7000EventTrapResLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventTrapResLeaf.setStatus("mandatory")
_LanBlazer7000EventTrapValueType_Type = EventValueType
_LanBlazer7000EventTrapValueType_Object = MibScalar
lanBlazer7000EventTrapValueType = _LanBlazer7000EventTrapValueType_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 6, 10),
    _LanBlazer7000EventTrapValueType_Type()
)
lanBlazer7000EventTrapValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventTrapValueType.setStatus("mandatory")


class _LanBlazer7000EventTrapValue_Type(OctetString):
    """Custom type lanBlazer7000EventTrapValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_LanBlazer7000EventTrapValue_Type.__name__ = "OctetString"
_LanBlazer7000EventTrapValue_Object = MibScalar
lanBlazer7000EventTrapValue = _LanBlazer7000EventTrapValue_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 6, 11),
    _LanBlazer7000EventTrapValue_Type()
)
lanBlazer7000EventTrapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventTrapValue.setStatus("mandatory")
_LanBlazer7000EventTrapEpochTime_Type = Integer32
_LanBlazer7000EventTrapEpochTime_Object = MibScalar
lanBlazer7000EventTrapEpochTime = _LanBlazer7000EventTrapEpochTime_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 6, 12),
    _LanBlazer7000EventTrapEpochTime_Type()
)
lanBlazer7000EventTrapEpochTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventTrapEpochTime.setStatus("mandatory")


class _LanBlazer7000EventTrapID_Type(Integer32):
    """Custom type lanBlazer7000EventTrapID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LanBlazer7000EventTrapID_Type.__name__ = "Integer32"
_LanBlazer7000EventTrapID_Object = MibScalar
lanBlazer7000EventTrapID = _LanBlazer7000EventTrapID_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 10, 6, 13),
    _LanBlazer7000EventTrapID_Type()
)
lanBlazer7000EventTrapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000EventTrapID.setStatus("mandatory")
_LanBlazer7000AlarmMgt_ObjectIdentity = ObjectIdentity
lanBlazer7000AlarmMgt = _LanBlazer7000AlarmMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 11)
)
_LanBlazer7000AlarmGeneral_ObjectIdentity = ObjectIdentity
lanBlazer7000AlarmGeneral = _LanBlazer7000AlarmGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 11, 1)
)
_LanBlazer7000AlarmGeneralActiveEntries_Type = Gauge32
_LanBlazer7000AlarmGeneralActiveEntries_Object = MibScalar
lanBlazer7000AlarmGeneralActiveEntries = _LanBlazer7000AlarmGeneralActiveEntries_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 11, 1, 1),
    _LanBlazer7000AlarmGeneralActiveEntries_Type()
)
lanBlazer7000AlarmGeneralActiveEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000AlarmGeneralActiveEntries.setStatus("mandatory")
_LanBlazer7000AlarmGeneralTimeStamp_Type = TimeTicks
_LanBlazer7000AlarmGeneralTimeStamp_Object = MibScalar
lanBlazer7000AlarmGeneralTimeStamp = _LanBlazer7000AlarmGeneralTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 11, 1, 2),
    _LanBlazer7000AlarmGeneralTimeStamp_Type()
)
lanBlazer7000AlarmGeneralTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000AlarmGeneralTimeStamp.setStatus("mandatory")
_LanBlazer7000Alarms_ObjectIdentity = ObjectIdentity
lanBlazer7000Alarms = _LanBlazer7000Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 11, 2)
)
_LanBlazer7000ActiveAlarmTable_Object = MibTable
lanBlazer7000ActiveAlarmTable = _LanBlazer7000ActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 11, 2, 2)
)
if mibBuilder.loadTexts:
    lanBlazer7000ActiveAlarmTable.setStatus("mandatory")
_LanBlazer7000ActiveAlarmEntry_Object = MibTableRow
lanBlazer7000ActiveAlarmEntry = _LanBlazer7000ActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 11, 2, 2, 1)
)
lanBlazer7000ActiveAlarmEntry.setIndexNames(
    (0, "ODSLANBlazer7000-MIB", "lanBlazer7000ActiveAlarmIndex"),
)
if mibBuilder.loadTexts:
    lanBlazer7000ActiveAlarmEntry.setStatus("mandatory")
_LanBlazer7000ActiveAlarmIndex_Type = Integer32
_LanBlazer7000ActiveAlarmIndex_Object = MibTableColumn
lanBlazer7000ActiveAlarmIndex = _LanBlazer7000ActiveAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 11, 2, 2, 1, 1),
    _LanBlazer7000ActiveAlarmIndex_Type()
)
lanBlazer7000ActiveAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000ActiveAlarmIndex.setStatus("mandatory")


class _LanBlazer7000ActiveAlarmName_Type(DisplayString):
    """Custom type lanBlazer7000ActiveAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_LanBlazer7000ActiveAlarmName_Type.__name__ = "DisplayString"
_LanBlazer7000ActiveAlarmName_Object = MibTableColumn
lanBlazer7000ActiveAlarmName = _LanBlazer7000ActiveAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 11, 2, 2, 1, 2),
    _LanBlazer7000ActiveAlarmName_Type()
)
lanBlazer7000ActiveAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000ActiveAlarmName.setStatus("mandatory")
_LanBlazer7000ActiveAlarmValueHigh_Type = Integer32
_LanBlazer7000ActiveAlarmValueHigh_Object = MibTableColumn
lanBlazer7000ActiveAlarmValueHigh = _LanBlazer7000ActiveAlarmValueHigh_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 11, 2, 2, 1, 3),
    _LanBlazer7000ActiveAlarmValueHigh_Type()
)
lanBlazer7000ActiveAlarmValueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000ActiveAlarmValueHigh.setStatus("mandatory")
_LanBlazer7000ActiveAlarmValueLow_Type = Integer32
_LanBlazer7000ActiveAlarmValueLow_Object = MibTableColumn
lanBlazer7000ActiveAlarmValueLow = _LanBlazer7000ActiveAlarmValueLow_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 11, 2, 2, 1, 4),
    _LanBlazer7000ActiveAlarmValueLow_Type()
)
lanBlazer7000ActiveAlarmValueLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000ActiveAlarmValueLow.setStatus("mandatory")
_LanBlazer7000ActiveAlarmVariable_Type = ObjectIdentifier
_LanBlazer7000ActiveAlarmVariable_Object = MibTableColumn
lanBlazer7000ActiveAlarmVariable = _LanBlazer7000ActiveAlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 11, 2, 2, 1, 5),
    _LanBlazer7000ActiveAlarmVariable_Type()
)
lanBlazer7000ActiveAlarmVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000ActiveAlarmVariable.setStatus("mandatory")
_LanBlazer7000ActiveAlarmResType_Type = ResourceType
_LanBlazer7000ActiveAlarmResType_Object = MibTableColumn
lanBlazer7000ActiveAlarmResType = _LanBlazer7000ActiveAlarmResType_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 11, 2, 2, 1, 6),
    _LanBlazer7000ActiveAlarmResType_Type()
)
lanBlazer7000ActiveAlarmResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000ActiveAlarmResType.setStatus("mandatory")
_LanBlazer7000ActiveAlarmResID_Type = ResourceId
_LanBlazer7000ActiveAlarmResID_Object = MibTableColumn
lanBlazer7000ActiveAlarmResID = _LanBlazer7000ActiveAlarmResID_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 11, 2, 2, 1, 7),
    _LanBlazer7000ActiveAlarmResID_Type()
)
lanBlazer7000ActiveAlarmResID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000ActiveAlarmResID.setStatus("mandatory")
_LanBlazer7000ActiveAlarmLeaf_Type = Integer32
_LanBlazer7000ActiveAlarmLeaf_Object = MibTableColumn
lanBlazer7000ActiveAlarmLeaf = _LanBlazer7000ActiveAlarmLeaf_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 11, 2, 2, 1, 8),
    _LanBlazer7000ActiveAlarmLeaf_Type()
)
lanBlazer7000ActiveAlarmLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000ActiveAlarmLeaf.setStatus("mandatory")


class _LanBlazer7000ActiveAlarmOwner_Type(DisplayString):
    """Custom type lanBlazer7000ActiveAlarmOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LanBlazer7000ActiveAlarmOwner_Type.__name__ = "DisplayString"
_LanBlazer7000ActiveAlarmOwner_Object = MibTableColumn
lanBlazer7000ActiveAlarmOwner = _LanBlazer7000ActiveAlarmOwner_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 11, 2, 2, 1, 9),
    _LanBlazer7000ActiveAlarmOwner_Type()
)
lanBlazer7000ActiveAlarmOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000ActiveAlarmOwner.setStatus("mandatory")
_LanBlazer7000SnmpTraps_ObjectIdentity = ObjectIdentity
lanBlazer7000SnmpTraps = _LanBlazer7000SnmpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 13)
)
_LanBlazer7000VlanExchange_ObjectIdentity = ObjectIdentity
lanBlazer7000VlanExchange = _LanBlazer7000VlanExchange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 14)
)
_LanBlazer7000VlanExchangeSwitch_ObjectIdentity = ObjectIdentity
lanBlazer7000VlanExchangeSwitch = _LanBlazer7000VlanExchangeSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 14, 1)
)


class _LanBlazer7000VlanExchangeState_Type(Integer32):
    """Custom type lanBlazer7000VlanExchangeState based on Integer32"""
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


_LanBlazer7000VlanExchangeState_Type.__name__ = "Integer32"
_LanBlazer7000VlanExchangeState_Object = MibScalar
lanBlazer7000VlanExchangeState = _LanBlazer7000VlanExchangeState_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 14, 1, 1),
    _LanBlazer7000VlanExchangeState_Type()
)
lanBlazer7000VlanExchangeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000VlanExchangeState.setStatus("mandatory")


class _LanBlazer7000VlanExchangeDomainName_Type(DisplayString):
    """Custom type lanBlazer7000VlanExchangeDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LanBlazer7000VlanExchangeDomainName_Type.__name__ = "DisplayString"
_LanBlazer7000VlanExchangeDomainName_Object = MibScalar
lanBlazer7000VlanExchangeDomainName = _LanBlazer7000VlanExchangeDomainName_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 14, 1, 2),
    _LanBlazer7000VlanExchangeDomainName_Type()
)
lanBlazer7000VlanExchangeDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanBlazer7000VlanExchangeDomainName.setStatus("mandatory")
_LanBlazer7000VlanExchangeUpdaterId_Type = IpAddress
_LanBlazer7000VlanExchangeUpdaterId_Object = MibScalar
lanBlazer7000VlanExchangeUpdaterId = _LanBlazer7000VlanExchangeUpdaterId_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 14, 1, 3),
    _LanBlazer7000VlanExchangeUpdaterId_Type()
)
lanBlazer7000VlanExchangeUpdaterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000VlanExchangeUpdaterId.setStatus("mandatory")


class _LanBlazer7000VlanExchangeUpdateTimeStamp_Type(DisplayString):
    """Custom type lanBlazer7000VlanExchangeUpdateTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_LanBlazer7000VlanExchangeUpdateTimeStamp_Type.__name__ = "DisplayString"
_LanBlazer7000VlanExchangeUpdateTimeStamp_Object = MibScalar
lanBlazer7000VlanExchangeUpdateTimeStamp = _LanBlazer7000VlanExchangeUpdateTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 14, 1, 4),
    _LanBlazer7000VlanExchangeUpdateTimeStamp_Type()
)
lanBlazer7000VlanExchangeUpdateTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000VlanExchangeUpdateTimeStamp.setStatus("mandatory")
_LanBlazer7000VlanExchangeConfigRevNum_Type = Integer32
_LanBlazer7000VlanExchangeConfigRevNum_Object = MibScalar
lanBlazer7000VlanExchangeConfigRevNum = _LanBlazer7000VlanExchangeConfigRevNum_Object(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 14, 1, 5),
    _LanBlazer7000VlanExchangeConfigRevNum_Type()
)
lanBlazer7000VlanExchangeConfigRevNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBlazer7000VlanExchangeConfigRevNum.setStatus("mandatory")

# Managed Objects groups


# Notification objects

lanBlazer7000SystemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 13, 0, 2)
)
lanBlazer7000SystemTrap.setObjects(
      *(("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapEventIndex"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapTime"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapDescr"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapType"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapSeverity"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapDTM"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapResType"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapResID"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapResLeaf"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapValueType"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapValue"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapEpochTime"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapID"))
)
if mibBuilder.loadTexts:
    lanBlazer7000SystemTrap.setStatus(
        ""
    )

lanBlazer7000ConfigurationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 13, 0, 3)
)
lanBlazer7000ConfigurationTrap.setObjects(
      *(("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapEventIndex"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapTime"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapDescr"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapType"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapSeverity"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapDTM"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapResType"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapResID"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapResLeaf"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapValueType"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapValue"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapEpochTime"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapID"))
)
if mibBuilder.loadTexts:
    lanBlazer7000ConfigurationTrap.setStatus(
        ""
    )

lanBlazer7000TemperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 13, 0, 4)
)
lanBlazer7000TemperatureTrap.setObjects(
      *(("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapEventIndex"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapTime"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapDescr"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapType"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapSeverity"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapDTM"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapResType"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapResID"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapResLeaf"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapValueType"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapValue"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapEpochTime"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapID"))
)
if mibBuilder.loadTexts:
    lanBlazer7000TemperatureTrap.setStatus(
        ""
    )

lanBlazer7000ResourceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 13, 0, 5)
)
lanBlazer7000ResourceTrap.setObjects(
      *(("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapEventIndex"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapTime"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapDescr"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapType"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapSeverity"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapDTM"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapResType"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapResID"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapResLeaf"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapValueType"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapValue"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapEpochTime"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapID"))
)
if mibBuilder.loadTexts:
    lanBlazer7000ResourceTrap.setStatus(
        ""
    )

lanBlazer7000FanTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 13, 0, 6)
)
lanBlazer7000FanTrap.setObjects(
      *(("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapEventIndex"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapTime"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapDescr"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapType"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapSeverity"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapDTM"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapResType"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapResID"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapResLeaf"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapValueType"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapValue"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapEpochTime"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapID"))
)
if mibBuilder.loadTexts:
    lanBlazer7000FanTrap.setStatus(
        ""
    )

lanBlazer7000PowerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 50, 8, 1, 2, 1, 13, 0, 9)
)
lanBlazer7000PowerTrap.setObjects(
      *(("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapEventIndex"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapTime"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapDescr"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapType"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapSeverity"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapDTM"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapResType"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapResID"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapResLeaf"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapValueType"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapValue"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapEpochTime"),
        ("ODSLANBlazer7000-MIB", "lanBlazer7000EventTrapID"))
)
if mibBuilder.loadTexts:
    lanBlazer7000PowerTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ODSLANBlazer7000-MIB",
    **{"EventValueType": EventValueType,
       "ResourceType": ResourceType,
       "ResourceId": ResourceId,
       "DisplayString": DisplayString,
       "RowStatus": RowStatus,
       "MacAddress": MacAddress,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "EventCategory": EventCategory,
       "ods": ods,
       "odsTPS": odsTPS,
       "odsLANBlazer": odsLANBlazer,
       "odsLANBlazerMibs": odsLANBlazerMibs,
       "odsLANBlazer7000Mib": odsLANBlazer7000Mib,
       "lanBlazer7000Agent": lanBlazer7000Agent,
       "lanBlazer7000AgentGen": lanBlazer7000AgentGen,
       "lanBlazer7000AgentMIBVersion": lanBlazer7000AgentMIBVersion,
       "lanBlazer7000AgentMgrIndex": lanBlazer7000AgentMgrIndex,
       "lanBlazer7000AgentCommunity": lanBlazer7000AgentCommunity,
       "lanBlazer7000CommunityTable": lanBlazer7000CommunityTable,
       "lanBlazer7000CommunityEntry": lanBlazer7000CommunityEntry,
       "lanBlazer7000CommunityIndex": lanBlazer7000CommunityIndex,
       "lanBlazer7000CommunityString": lanBlazer7000CommunityString,
       "lanBlazer7000CommunityAddressType": lanBlazer7000CommunityAddressType,
       "lanBlazer7000CommunityAddress": lanBlazer7000CommunityAddress,
       "lanBlazer7000CommunityAccess": lanBlazer7000CommunityAccess,
       "lanBlazer7000CommunityTrapReceiver": lanBlazer7000CommunityTrapReceiver,
       "lanBlazer7000CommunitySecurityLevel": lanBlazer7000CommunitySecurityLevel,
       "lanBlazer7000CommunityStatus": lanBlazer7000CommunityStatus,
       "lanBlazer7000AgentWeb": lanBlazer7000AgentWeb,
       "lanBlazer7000AgentWebServerURL": lanBlazer7000AgentWebServerURL,
       "lanBlazer7000AgentWebServerHelpDirectory": lanBlazer7000AgentWebServerHelpDirectory,
       "lanBlazer7000Chassis": lanBlazer7000Chassis,
       "lanBlazer7000ChassisGen": lanBlazer7000ChassisGen,
       "lanBlazer7000ChassisType": lanBlazer7000ChassisType,
       "lanBlazer7000ChassisSlots": lanBlazer7000ChassisSlots,
       "lanBlazer7000Inventory": lanBlazer7000Inventory,
       "lanBlazer7000InventoryTable": lanBlazer7000InventoryTable,
       "lanBlazer7000InventoryEntry": lanBlazer7000InventoryEntry,
       "lanBlazer7000InventoryResourceType": lanBlazer7000InventoryResourceType,
       "lanBlazer7000InventoryResourceIndex": lanBlazer7000InventoryResourceIndex,
       "lanBlazer7000InventoryModelNumber": lanBlazer7000InventoryModelNumber,
       "lanBlazer7000InventorySerialNumber": lanBlazer7000InventorySerialNumber,
       "lanBlazer7000InventoryVersion": lanBlazer7000InventoryVersion,
       "lanBlazer7000InventoryManufactureInfo": lanBlazer7000InventoryManufactureInfo,
       "lanBlazer7000InventoryScratchPad": lanBlazer7000InventoryScratchPad,
       "lanBlazer7000PowerSystems": lanBlazer7000PowerSystems,
       "lanBlazer7000PowerSupplies": lanBlazer7000PowerSupplies,
       "lanBlazer7000PowerSupplyTable": lanBlazer7000PowerSupplyTable,
       "lanBlazer7000PowerSupplyEntry": lanBlazer7000PowerSupplyEntry,
       "lanBlazer7000PowerSupplyIndex": lanBlazer7000PowerSupplyIndex,
       "lanBlazer7000PowerSupplyType": lanBlazer7000PowerSupplyType,
       "lanBlazer7000PowerSupplyStatus": lanBlazer7000PowerSupplyStatus,
       "lanBlazer7000PowerSupplyInputStatus": lanBlazer7000PowerSupplyInputStatus,
       "lanBlazer7000PowerSupplyOutputStatus": lanBlazer7000PowerSupplyOutputStatus,
       "lanBlazer7000PowerSupplyOutputCapacity": lanBlazer7000PowerSupplyOutputCapacity,
       "lanBlazer7000PowerMgmtGen": lanBlazer7000PowerMgmtGen,
       "lanBlazer7000PowerCapacity": lanBlazer7000PowerCapacity,
       "lanBlazer7000PowerUsed": lanBlazer7000PowerUsed,
       "lanBlazer7000PowerMgmtCtl": lanBlazer7000PowerMgmtCtl,
       "lanBlazer7000PowerControlTable": lanBlazer7000PowerControlTable,
       "lanBlazer7000PowerControlEntry": lanBlazer7000PowerControlEntry,
       "lanBlazer7000PowerControlUsed": lanBlazer7000PowerControlUsed,
       "lanBlazer7000PowerControlPriority": lanBlazer7000PowerControlPriority,
       "lanBlazer7000PowerControlMode": lanBlazer7000PowerControlMode,
       "lanBlazer7000Temperature": lanBlazer7000Temperature,
       "lanBlazer7000TempTable": lanBlazer7000TempTable,
       "lanBlazer7000TempEntry": lanBlazer7000TempEntry,
       "lanBlazer7000TempIndex": lanBlazer7000TempIndex,
       "lanBlazer7000TempValue": lanBlazer7000TempValue,
       "lanBlazer7000TempUpperLimit": lanBlazer7000TempUpperLimit,
       "lanBlazer7000TempUpperWarning": lanBlazer7000TempUpperWarning,
       "lanBlazer7000TempLowerWarning": lanBlazer7000TempLowerWarning,
       "lanBlazer7000TempLowerLimit": lanBlazer7000TempLowerLimit,
       "lanBlazer7000Modules": lanBlazer7000Modules,
       "lanBlazer7000ModuleTable": lanBlazer7000ModuleTable,
       "lanBlazer7000ModuleEntry": lanBlazer7000ModuleEntry,
       "lanBlazer7000ModuleIndex": lanBlazer7000ModuleIndex,
       "lanBlazer7000ModuleName": lanBlazer7000ModuleName,
       "lanBlazer7000ModuleType": lanBlazer7000ModuleType,
       "lanBlazer7000ModuleBaseType": lanBlazer7000ModuleBaseType,
       "lanBlazer7000ModuleSlotWidth": lanBlazer7000ModuleSlotWidth,
       "lanBlazer7000ModuleSlotOffset": lanBlazer7000ModuleSlotOffset,
       "lanBlazer7000ModulePorts": lanBlazer7000ModulePorts,
       "lanBlazer7000Ports": lanBlazer7000Ports,
       "lanBlazer7000PortMgt": lanBlazer7000PortMgt,
       "lanBlazer7000PortTable": lanBlazer7000PortTable,
       "lanBlazer7000PortEntry": lanBlazer7000PortEntry,
       "lanBlazer7000PortIndex": lanBlazer7000PortIndex,
       "lanBlazer7000PortName": lanBlazer7000PortName,
       "lanBlazer7000PortType": lanBlazer7000PortType,
       "lanBlazer7000PortBaseType": lanBlazer7000PortBaseType,
       "lanBlazer7000PortMode": lanBlazer7000PortMode,
       "lanBlazer7000PortStatus": lanBlazer7000PortStatus,
       "lanBlazer7000PortConnector": lanBlazer7000PortConnector,
       "lanBlazer7000PortSpeedState": lanBlazer7000PortSpeedState,
       "lanBlazer7000PortDuplexState": lanBlazer7000PortDuplexState,
       "lanBlazer7000PortGroupBinding": lanBlazer7000PortGroupBinding,
       "lanBlazer7000PortFlowControlMgt": lanBlazer7000PortFlowControlMgt,
       "lanBlazer7000PortFlowControlTable": lanBlazer7000PortFlowControlTable,
       "lanBlazer7000PortFlowControlEntry": lanBlazer7000PortFlowControlEntry,
       "lanBlazer7000PortFlowControlMode": lanBlazer7000PortFlowControlMode,
       "lanBlazer7000PortDuplexMgt": lanBlazer7000PortDuplexMgt,
       "lanBlazer7000PortDuplexTable": lanBlazer7000PortDuplexTable,
       "lanBlazer7000PortDuplexEntry": lanBlazer7000PortDuplexEntry,
       "lanBlazer7000PortDuplexMode": lanBlazer7000PortDuplexMode,
       "lanBlazer7000PortSpeedMgt": lanBlazer7000PortSpeedMgt,
       "lanBlazer7000PortSpeedTable": lanBlazer7000PortSpeedTable,
       "lanBlazer7000PortSpeedEntry": lanBlazer7000PortSpeedEntry,
       "lanBlazer7000PortSpeedMode": lanBlazer7000PortSpeedMode,
       "lanBlazer7000PortAutoNegotiationMgt": lanBlazer7000PortAutoNegotiationMgt,
       "lanBlazer7000PortAutoNegotiationTable": lanBlazer7000PortAutoNegotiationTable,
       "lanBlazer7000PortAutoNegotiationEntry": lanBlazer7000PortAutoNegotiationEntry,
       "lanBlazer7000PortAutoNegotiationMode": lanBlazer7000PortAutoNegotiationMode,
       "lanBlazer7000PortAutoNegotiationSpeedAdvertisement": lanBlazer7000PortAutoNegotiationSpeedAdvertisement,
       "lanBlazer7000PortAutoNegotiationDuplexAdvertisement": lanBlazer7000PortAutoNegotiationDuplexAdvertisement,
       "lanBlazer7000PortRateLimitMgt": lanBlazer7000PortRateLimitMgt,
       "lanBlazer7000PortRateLimitTable": lanBlazer7000PortRateLimitTable,
       "lanBlazer7000PortRateLimitEntry": lanBlazer7000PortRateLimitEntry,
       "lanBlazer7000PortRateLimitMode": lanBlazer7000PortRateLimitMode,
       "lanBlazer7000PortRateLimitRate": lanBlazer7000PortRateLimitRate,
       "lanBlazer7000PortRateLimitBurstSize": lanBlazer7000PortRateLimitBurstSize,
       "lanBlazer7000PortPacePriorityMgt": lanBlazer7000PortPacePriorityMgt,
       "lanBlazer7000PortPacePriorityTable": lanBlazer7000PortPacePriorityTable,
       "lanBlazer7000PortPacePriorityEntry": lanBlazer7000PortPacePriorityEntry,
       "lanBlazer7000PortPacePriorityMode": lanBlazer7000PortPacePriorityMode,
       "lanBlazer7000PortCategoryMgt": lanBlazer7000PortCategoryMgt,
       "lanBlazer7000PortCategoryTable": lanBlazer7000PortCategoryTable,
       "lanBlazer7000PortCategoryEntry": lanBlazer7000PortCategoryEntry,
       "lanBlazer7000PortCategoryMode": lanBlazer7000PortCategoryMode,
       "lanBlazer7000BufferMgt": lanBlazer7000BufferMgt,
       "lanBlazer7000BufferTable": lanBlazer7000BufferTable,
       "lanBlazer7000BufferEntry": lanBlazer7000BufferEntry,
       "lanBlazer7000BufferIndex": lanBlazer7000BufferIndex,
       "lanBlazer7000BufferFabricPort": lanBlazer7000BufferFabricPort,
       "lanBlazer7000BufferFabricPortDirection": lanBlazer7000BufferFabricPortDirection,
       "lanBlazer7000BufferSwitchPort": lanBlazer7000BufferSwitchPort,
       "lanBlazer7000BufferMemory": lanBlazer7000BufferMemory,
       "lanBlazer7000BufferAgeTimer": lanBlazer7000BufferAgeTimer,
       "lanBlazer7000BufferPriorityServicing": lanBlazer7000BufferPriorityServicing,
       "lanBlazer7000BufferPriorityAllocation": lanBlazer7000BufferPriorityAllocation,
       "lanBlazer7000BufferPriorityThreshold": lanBlazer7000BufferPriorityThreshold,
       "lanBlazer7000BufferCongestion": lanBlazer7000BufferCongestion,
       "lanBlazer7000BufferHighOverflowDrops": lanBlazer7000BufferHighOverflowDrops,
       "lanBlazer7000BufferLowOverflowDrops": lanBlazer7000BufferLowOverflowDrops,
       "lanBlazer7000BufferHighStaleDrops": lanBlazer7000BufferHighStaleDrops,
       "lanBlazer7000BufferLowStaleDrops": lanBlazer7000BufferLowStaleDrops,
       "lanBlazer7000BufferCongestionDrops": lanBlazer7000BufferCongestionDrops,
       "lanBlazer7000Switching": lanBlazer7000Switching,
       "lanBlazer7000SwitchingLayerII": lanBlazer7000SwitchingLayerII,
       "lanBlazer7000SwitchGen": lanBlazer7000SwitchGen,
       "lanBlazer7000SwitchSTPConfig": lanBlazer7000SwitchSTPConfig,
       "lanBlazer7000SwitchAgingTime": lanBlazer7000SwitchAgingTime,
       "lanBlazer7000SwitchSuperAgingTime": lanBlazer7000SwitchSuperAgingTime,
       "lanBlazer7000BridgeMgmt": lanBlazer7000BridgeMgmt,
       "lanBlazer7000BridgeTable": lanBlazer7000BridgeTable,
       "lanBlazer7000BridgeEntry": lanBlazer7000BridgeEntry,
       "lanBlazer7000BridgeIndex": lanBlazer7000BridgeIndex,
       "lanBlazer7000BridgeType": lanBlazer7000BridgeType,
       "lanBlazer7000BridgeMode": lanBlazer7000BridgeMode,
       "lanBlazer7000BridgeStatus": lanBlazer7000BridgeStatus,
       "lanBlazer7000BridgeStpPriority": lanBlazer7000BridgeStpPriority,
       "lanBlazer7000BridgeStpTimeSinceTopologyChange": lanBlazer7000BridgeStpTimeSinceTopologyChange,
       "lanBlazer7000BridgeStpTopChanges": lanBlazer7000BridgeStpTopChanges,
       "lanBlazer7000BridgeStpDesignatedRoot": lanBlazer7000BridgeStpDesignatedRoot,
       "lanBlazer7000BridgeStpRootCost": lanBlazer7000BridgeStpRootCost,
       "lanBlazer7000BridgeStpRootPort": lanBlazer7000BridgeStpRootPort,
       "lanBlazer7000BridgeStpMaxAge": lanBlazer7000BridgeStpMaxAge,
       "lanBlazer7000BridgeStpHelloTime": lanBlazer7000BridgeStpHelloTime,
       "lanBlazer7000BridgeStpHoldTime": lanBlazer7000BridgeStpHoldTime,
       "lanBlazer7000BridgeStpForwardDelay": lanBlazer7000BridgeStpForwardDelay,
       "lanBlazer7000BridgeStpBridgeMaxAge": lanBlazer7000BridgeStpBridgeMaxAge,
       "lanBlazer7000BridgeStpBridgeHelloTime": lanBlazer7000BridgeStpBridgeHelloTime,
       "lanBlazer7000BridgeStpBridgeForwardDelay": lanBlazer7000BridgeStpBridgeForwardDelay,
       "lanBlazer7000BridgePortMgmt": lanBlazer7000BridgePortMgmt,
       "lanBlazer7000BridgePortTable": lanBlazer7000BridgePortTable,
       "lanBlazer7000BridgePortEntry": lanBlazer7000BridgePortEntry,
       "lanBlazer7000BridgePortIndex": lanBlazer7000BridgePortIndex,
       "lanBlazer7000BridgePortPriority": lanBlazer7000BridgePortPriority,
       "lanBlazer7000BridgePortState": lanBlazer7000BridgePortState,
       "lanBlazer7000BridgePortEnable": lanBlazer7000BridgePortEnable,
       "lanBlazer7000BridgePortPathCost": lanBlazer7000BridgePortPathCost,
       "lanBlazer7000BridgePortDesignatedRoot": lanBlazer7000BridgePortDesignatedRoot,
       "lanBlazer7000BridgePortDesignatedCost": lanBlazer7000BridgePortDesignatedCost,
       "lanBlazer7000BridgePortDesignatedBridge": lanBlazer7000BridgePortDesignatedBridge,
       "lanBlazer7000BridgePortDesignatedPort": lanBlazer7000BridgePortDesignatedPort,
       "lanBlazer7000BridgePortForwardTransitions": lanBlazer7000BridgePortForwardTransitions,
       "lanBlazer7000BridgePortFastStart": lanBlazer7000BridgePortFastStart,
       "lanBlazer7000BridgePortSetDefault": lanBlazer7000BridgePortSetDefault,
       "lanBlazer7000BridgePortEnableChangeDetection": lanBlazer7000BridgePortEnableChangeDetection,
       "lanBlazer7000L2AddrMgmt": lanBlazer7000L2AddrMgmt,
       "lanBlazer7000L2AddrDatabaseMgt": lanBlazer7000L2AddrDatabaseMgt,
       "lanBlazer7000L2AddressTable": lanBlazer7000L2AddressTable,
       "lanBlazer7000L2AddressEntry": lanBlazer7000L2AddressEntry,
       "lanBlazer7000L2AddressIndex": lanBlazer7000L2AddressIndex,
       "lanBlazer7000L2AddressTableIndex": lanBlazer7000L2AddressTableIndex,
       "lanBlazer7000L2AddressMacAddress": lanBlazer7000L2AddressMacAddress,
       "lanBlazer7000L2AddressPortBinding": lanBlazer7000L2AddressPortBinding,
       "lanBlazer7000L2AddressBindingValid": lanBlazer7000L2AddressBindingValid,
       "lanBlazer7000L2AddressVlanID": lanBlazer7000L2AddressVlanID,
       "lanBlazer7000L2AddressPriority": lanBlazer7000L2AddressPriority,
       "lanBlazer7000L2AddressForward": lanBlazer7000L2AddressForward,
       "lanBlazer7000L2AddressCopy": lanBlazer7000L2AddressCopy,
       "lanBlazer7000L2AddressPersistence": lanBlazer7000L2AddressPersistence,
       "lanBlazer7000L2AddressStatus": lanBlazer7000L2AddressStatus,
       "lanBlazer7000L2AddrSummaryMgt": lanBlazer7000L2AddrSummaryMgt,
       "lanBlazer7000L2AddrSummaryTable": lanBlazer7000L2AddrSummaryTable,
       "lanBlazer7000L2AddrSummaryEntry": lanBlazer7000L2AddrSummaryEntry,
       "lanBlazer7000L2AddrSummary": lanBlazer7000L2AddrSummary,
       "lanBlazer7000L2AddrControlMgt": lanBlazer7000L2AddrControlMgt,
       "lanBlazer7000L2AddressControlTable": lanBlazer7000L2AddressControlTable,
       "lanBlazer7000L2AddressControlEntry": lanBlazer7000L2AddressControlEntry,
       "lanBlazer7000L2AddressControlIndex": lanBlazer7000L2AddressControlIndex,
       "lanBlazer7000L2AddressControlMacAddress": lanBlazer7000L2AddressControlMacAddress,
       "lanBlazer7000L2AddressControlPortBinding": lanBlazer7000L2AddressControlPortBinding,
       "lanBlazer7000L2AddressControlVlanID": lanBlazer7000L2AddressControlVlanID,
       "lanBlazer7000L2AddressControlPriority": lanBlazer7000L2AddressControlPriority,
       "lanBlazer7000L2AddressControlPersistence": lanBlazer7000L2AddressControlPersistence,
       "lanBlazer7000L2AddressControlStatus": lanBlazer7000L2AddressControlStatus,
       "lanBlazer7000L2AddrChangeMgt": lanBlazer7000L2AddrChangeMgt,
       "lanBlazer7000L2AddressChangeLast": lanBlazer7000L2AddressChangeLast,
       "lanBlazer7000L2AddressChangeWraps": lanBlazer7000L2AddressChangeWraps,
       "lanBlazer7000L2AddressChangeMaxEntries": lanBlazer7000L2AddressChangeMaxEntries,
       "lanBlazer7000L2AddressChangeTable": lanBlazer7000L2AddressChangeTable,
       "lanBlazer7000L2AddressChangeEntry": lanBlazer7000L2AddressChangeEntry,
       "lanBlazer7000L2AddressChangeWrapCount": lanBlazer7000L2AddressChangeWrapCount,
       "lanBlazer7000L2AddressChangeIndex": lanBlazer7000L2AddressChangeIndex,
       "lanBlazer7000L2AddressChangeIndexChanged": lanBlazer7000L2AddressChangeIndexChanged,
       "lanBlazer7000L2AddressChangeSummary": lanBlazer7000L2AddressChangeSummary,
       "lanBlazer7000SwitchPortMgt": lanBlazer7000SwitchPortMgt,
       "lanBlazer7000SwitchPortTable": lanBlazer7000SwitchPortTable,
       "lanBlazer7000SwitchPortEntry": lanBlazer7000SwitchPortEntry,
       "lanBlazer7000SwitchPortIndex": lanBlazer7000SwitchPortIndex,
       "lanBlazer7000SwitchPortSTAPMode": lanBlazer7000SwitchPortSTAPMode,
       "lanBlazer7000SwitchPortConvertToStatic": lanBlazer7000SwitchPortConvertToStatic,
       "lanBlazer7000SwitchPortLearningMode": lanBlazer7000SwitchPortLearningMode,
       "lanBlazer7000SwitchPortHuntGroup": lanBlazer7000SwitchPortHuntGroup,
       "lanBlazer7000SwitchPortPhysicalPort": lanBlazer7000SwitchPortPhysicalPort,
       "lanBlazer7000SwitchPortKnownMode": lanBlazer7000SwitchPortKnownMode,
       "lanBlazer7000SwitchPortMappingMethod": lanBlazer7000SwitchPortMappingMethod,
       "lanBlazer7000SwitchPortTrunkingMode": lanBlazer7000SwitchPortTrunkingMode,
       "lanBlazer7000SwitchPortVlanBindingMethod": lanBlazer7000SwitchPortVlanBindingMethod,
       "lanBlazer7000SwitchPortIgnoreTag": lanBlazer7000SwitchPortIgnoreTag,
       "lanBlazer7000SwitchPortVlanID": lanBlazer7000SwitchPortVlanID,
       "lanBlazer7000SwitchPort3ComMappingTableIndex": lanBlazer7000SwitchPort3ComMappingTableIndex,
       "lanBlazer7000SwitchPortAutoVlanCreation": lanBlazer7000SwitchPortAutoVlanCreation,
       "lanBlazer7000SwitchPortMirrorMode": lanBlazer7000SwitchPortMirrorMode,
       "lanBlazer7000SwitchPortIfIndex": lanBlazer7000SwitchPortIfIndex,
       "lanBlazer7000SwitchPortFastStart": lanBlazer7000SwitchPortFastStart,
       "lanBlazer7000SwitchPortVlanExchange": lanBlazer7000SwitchPortVlanExchange,
       "lanBlazer7000HuntGroupMgt": lanBlazer7000HuntGroupMgt,
       "lanBlazer7000HuntGroupTable": lanBlazer7000HuntGroupTable,
       "lanBlazer7000HuntGroupEntry": lanBlazer7000HuntGroupEntry,
       "lanBlazer7000HuntGroupIndex": lanBlazer7000HuntGroupIndex,
       "lanBlazer7000HuntGroupName": lanBlazer7000HuntGroupName,
       "lanBlazer7000HuntGroupBasePort": lanBlazer7000HuntGroupBasePort,
       "lanBlazer7000HuntGroupNumberOfPorts": lanBlazer7000HuntGroupNumberOfPorts,
       "lanBlazer7000HuntGroupLoadSharing": lanBlazer7000HuntGroupLoadSharing,
       "lanBlazer7000HuntGroupStatus": lanBlazer7000HuntGroupStatus,
       "lanBlazer7000PortMirroringMgt": lanBlazer7000PortMirroringMgt,
       "lanBlazer7000PortMirroringTable": lanBlazer7000PortMirroringTable,
       "lanBlazer7000PortMirroringEntry": lanBlazer7000PortMirroringEntry,
       "lanBlazer7000PortMirroringIndex": lanBlazer7000PortMirroringIndex,
       "lanBlazer7000PortMirroringSourceSubPort": lanBlazer7000PortMirroringSourceSubPort,
       "lanBlazer7000PortMirroringSamplerType": lanBlazer7000PortMirroringSamplerType,
       "lanBlazer7000PortMirroringRate": lanBlazer7000PortMirroringRate,
       "lanBlazer7000PortMirroringMirrorPort": lanBlazer7000PortMirroringMirrorPort,
       "lanBlazer7000VlanMgt": lanBlazer7000VlanMgt,
       "lanBlazer7000Vlans": lanBlazer7000Vlans,
       "lanBlazer7000VlanTable": lanBlazer7000VlanTable,
       "lanBlazer7000VlanEntry": lanBlazer7000VlanEntry,
       "lanBlazer7000VlanID": lanBlazer7000VlanID,
       "lanBlazer7000VlanName": lanBlazer7000VlanName,
       "lanBlazer7000VlanIfIndex": lanBlazer7000VlanIfIndex,
       "lanBlazer7000VlanAFTIndex": lanBlazer7000VlanAFTIndex,
       "lanBlazer7000VlanBridgeIndex": lanBlazer7000VlanBridgeIndex,
       "lanBlazer7000VlanStatus": lanBlazer7000VlanStatus,
       "lanBlazer7000VlanInitialHashTableSize": lanBlazer7000VlanInitialHashTableSize,
       "lanBlazer7000VlanAutoIncrementHTSize": lanBlazer7000VlanAutoIncrementHTSize,
       "lanBlazer7000VlanLearnStatus": lanBlazer7000VlanLearnStatus,
       "lanBlazer7000VlanMappings": lanBlazer7000VlanMappings,
       "lanBlazer70003ComMapping": lanBlazer70003ComMapping,
       "lanBlazer70003ComMappingTable": lanBlazer70003ComMappingTable,
       "lanBlazer70003ComMappingEntry": lanBlazer70003ComMappingEntry,
       "lanBlazer70003ComMappingTableIndex": lanBlazer70003ComMappingTableIndex,
       "lanBlazer70003ComMappingTableName": lanBlazer70003ComMappingTableName,
       "lanBlazer70003ComMappingTableStatus": lanBlazer70003ComMappingTableStatus,
       "lanBlazer7000Vlan3ComMapping": lanBlazer7000Vlan3ComMapping,
       "lanBlazer7000Vlan3ComMappingTable": lanBlazer7000Vlan3ComMappingTable,
       "lanBlazer7000Vlan3ComMappingEntry": lanBlazer7000Vlan3ComMappingEntry,
       "lanBlazer7000Vlan3ComMappingIndex": lanBlazer7000Vlan3ComMappingIndex,
       "lanBlazer7000Vlan3ComMappingVlanID": lanBlazer7000Vlan3ComMappingVlanID,
       "lanBlazer7000Vlan3ComMappingStatus": lanBlazer7000Vlan3ComMappingStatus,
       "lanBlazer7000VirtualPorts": lanBlazer7000VirtualPorts,
       "lanBlazer7000VirtualSwitchPortTable": lanBlazer7000VirtualSwitchPortTable,
       "lanBlazer7000VirtualSwitchPortEntry": lanBlazer7000VirtualSwitchPortEntry,
       "lanBlazer7000VirtualSwitchPortIndex": lanBlazer7000VirtualSwitchPortIndex,
       "lanBlazer7000VirtualSwitchPortFormat": lanBlazer7000VirtualSwitchPortFormat,
       "lanBlazer7000VirtualSwitchPortBridgePort": lanBlazer7000VirtualSwitchPortBridgePort,
       "lanBlazer7000VirtualSwitchPortBindingType": lanBlazer7000VirtualSwitchPortBindingType,
       "lanBlazer7000VirtualSwitchPortStatus": lanBlazer7000VirtualSwitchPortStatus,
       "lanBlazer7000Events": lanBlazer7000Events,
       "lanBlazer7000EventMgt": lanBlazer7000EventMgt,
       "lanBlazer7000EventTable": lanBlazer7000EventTable,
       "lanBlazer7000EventEntry": lanBlazer7000EventEntry,
       "lanBlazer7000EventIndex": lanBlazer7000EventIndex,
       "lanBlazer7000EventMode": lanBlazer7000EventMode,
       "lanBlazer7000EventLogAction": lanBlazer7000EventLogAction,
       "lanBlazer7000EventTrapAction": lanBlazer7000EventTrapAction,
       "lanBlazer7000EventConsoleAction": lanBlazer7000EventConsoleAction,
       "lanBlazer7000EventLogMgt": lanBlazer7000EventLogMgt,
       "lanBlazer7000LogTableMaxSize": lanBlazer7000LogTableMaxSize,
       "lanBlazer7000LogLastEntry": lanBlazer7000LogLastEntry,
       "lanBlazer7000LogWraps": lanBlazer7000LogWraps,
       "lanBlazer7000EventLog": lanBlazer7000EventLog,
       "lanBlazer7000EventLogTable": lanBlazer7000EventLogTable,
       "lanBlazer7000EventLogEntry": lanBlazer7000EventLogEntry,
       "lanBlazer7000EventLogEventIndex": lanBlazer7000EventLogEventIndex,
       "lanBlazer7000EventLogIndex": lanBlazer7000EventLogIndex,
       "lanBlazer7000EventLogTime": lanBlazer7000EventLogTime,
       "lanBlazer7000EventLogDescr": lanBlazer7000EventLogDescr,
       "lanBlazer7000EventLogType": lanBlazer7000EventLogType,
       "lanBlazer7000EventLogSeverity": lanBlazer7000EventLogSeverity,
       "lanBlazer7000EventLogDTM": lanBlazer7000EventLogDTM,
       "lanBlazer7000EventLogResType": lanBlazer7000EventLogResType,
       "lanBlazer7000EventLogResID": lanBlazer7000EventLogResID,
       "lanBlazer7000EventLogResLeaf": lanBlazer7000EventLogResLeaf,
       "lanBlazer7000EventLogValueType": lanBlazer7000EventLogValueType,
       "lanBlazer7000EventLogValue": lanBlazer7000EventLogValue,
       "lanBlazer7000EventLogEpochTime": lanBlazer7000EventLogEpochTime,
       "lanBlazer7000EventLogID": lanBlazer7000EventLogID,
       "lanBlazer7000ShutdownLogMgt": lanBlazer7000ShutdownLogMgt,
       "lanBlazer7000ShutdownLogTableMaxSize": lanBlazer7000ShutdownLogTableMaxSize,
       "lanBlazer7000ShutdownLogLastEntry": lanBlazer7000ShutdownLogLastEntry,
       "lanBlazer7000ShutdownLogAcknowledged": lanBlazer7000ShutdownLogAcknowledged,
       "lanBlazer7000EventShutdownLog": lanBlazer7000EventShutdownLog,
       "lanBlazer7000EventShutdownLogTable": lanBlazer7000EventShutdownLogTable,
       "lanBlazer7000EventShutdownLogEntry": lanBlazer7000EventShutdownLogEntry,
       "lanBlazer7000EventShutdownLogEventIndex": lanBlazer7000EventShutdownLogEventIndex,
       "lanBlazer7000EventShutdownLogIndex": lanBlazer7000EventShutdownLogIndex,
       "lanBlazer7000EventShutdownLogTime": lanBlazer7000EventShutdownLogTime,
       "lanBlazer7000EventShutdownLogDescr": lanBlazer7000EventShutdownLogDescr,
       "lanBlazer7000EventShutdownLogType": lanBlazer7000EventShutdownLogType,
       "lanBlazer7000EventShutdownLogSeverity": lanBlazer7000EventShutdownLogSeverity,
       "lanBlazer7000EventShutdownLogDTM": lanBlazer7000EventShutdownLogDTM,
       "lanBlazer7000EventShutdownLogResType": lanBlazer7000EventShutdownLogResType,
       "lanBlazer7000EventShutdownLogResID": lanBlazer7000EventShutdownLogResID,
       "lanBlazer7000EventShutdownLogResLeaf": lanBlazer7000EventShutdownLogResLeaf,
       "lanBlazer7000EventShutdownLogValueType": lanBlazer7000EventShutdownLogValueType,
       "lanBlazer7000EventShutdownLogValue": lanBlazer7000EventShutdownLogValue,
       "lanBlazer7000EventShutdownLogEpochTime": lanBlazer7000EventShutdownLogEpochTime,
       "lanBlazer7000EventShutdownLogID": lanBlazer7000EventShutdownLogID,
       "lanBlazer7000EventTrapMgmt": lanBlazer7000EventTrapMgmt,
       "lanBlazer7000EventTrapEventIndex": lanBlazer7000EventTrapEventIndex,
       "lanBlazer7000EventTrapTime": lanBlazer7000EventTrapTime,
       "lanBlazer7000EventTrapDescr": lanBlazer7000EventTrapDescr,
       "lanBlazer7000EventTrapType": lanBlazer7000EventTrapType,
       "lanBlazer7000EventTrapSeverity": lanBlazer7000EventTrapSeverity,
       "lanBlazer7000EventTrapDTM": lanBlazer7000EventTrapDTM,
       "lanBlazer7000EventTrapResType": lanBlazer7000EventTrapResType,
       "lanBlazer7000EventTrapResID": lanBlazer7000EventTrapResID,
       "lanBlazer7000EventTrapResLeaf": lanBlazer7000EventTrapResLeaf,
       "lanBlazer7000EventTrapValueType": lanBlazer7000EventTrapValueType,
       "lanBlazer7000EventTrapValue": lanBlazer7000EventTrapValue,
       "lanBlazer7000EventTrapEpochTime": lanBlazer7000EventTrapEpochTime,
       "lanBlazer7000EventTrapID": lanBlazer7000EventTrapID,
       "lanBlazer7000AlarmMgt": lanBlazer7000AlarmMgt,
       "lanBlazer7000AlarmGeneral": lanBlazer7000AlarmGeneral,
       "lanBlazer7000AlarmGeneralActiveEntries": lanBlazer7000AlarmGeneralActiveEntries,
       "lanBlazer7000AlarmGeneralTimeStamp": lanBlazer7000AlarmGeneralTimeStamp,
       "lanBlazer7000Alarms": lanBlazer7000Alarms,
       "lanBlazer7000ActiveAlarmTable": lanBlazer7000ActiveAlarmTable,
       "lanBlazer7000ActiveAlarmEntry": lanBlazer7000ActiveAlarmEntry,
       "lanBlazer7000ActiveAlarmIndex": lanBlazer7000ActiveAlarmIndex,
       "lanBlazer7000ActiveAlarmName": lanBlazer7000ActiveAlarmName,
       "lanBlazer7000ActiveAlarmValueHigh": lanBlazer7000ActiveAlarmValueHigh,
       "lanBlazer7000ActiveAlarmValueLow": lanBlazer7000ActiveAlarmValueLow,
       "lanBlazer7000ActiveAlarmVariable": lanBlazer7000ActiveAlarmVariable,
       "lanBlazer7000ActiveAlarmResType": lanBlazer7000ActiveAlarmResType,
       "lanBlazer7000ActiveAlarmResID": lanBlazer7000ActiveAlarmResID,
       "lanBlazer7000ActiveAlarmLeaf": lanBlazer7000ActiveAlarmLeaf,
       "lanBlazer7000ActiveAlarmOwner": lanBlazer7000ActiveAlarmOwner,
       "lanBlazer7000SnmpTraps": lanBlazer7000SnmpTraps,
       "lanBlazer7000SystemTrap": lanBlazer7000SystemTrap,
       "lanBlazer7000ConfigurationTrap": lanBlazer7000ConfigurationTrap,
       "lanBlazer7000TemperatureTrap": lanBlazer7000TemperatureTrap,
       "lanBlazer7000ResourceTrap": lanBlazer7000ResourceTrap,
       "lanBlazer7000FanTrap": lanBlazer7000FanTrap,
       "lanBlazer7000PowerTrap": lanBlazer7000PowerTrap,
       "lanBlazer7000VlanExchange": lanBlazer7000VlanExchange,
       "lanBlazer7000VlanExchangeSwitch": lanBlazer7000VlanExchangeSwitch,
       "lanBlazer7000VlanExchangeState": lanBlazer7000VlanExchangeState,
       "lanBlazer7000VlanExchangeDomainName": lanBlazer7000VlanExchangeDomainName,
       "lanBlazer7000VlanExchangeUpdaterId": lanBlazer7000VlanExchangeUpdaterId,
       "lanBlazer7000VlanExchangeUpdateTimeStamp": lanBlazer7000VlanExchangeUpdateTimeStamp,
       "lanBlazer7000VlanExchangeConfigRevNum": lanBlazer7000VlanExchangeConfigRevNum}
)
